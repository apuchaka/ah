#!/usr/bin/env python3
"""
Phase 5 fourth pass — every LEAF subclass of the AMH therapeutic classification.

ENUMERATION SOURCE
South Australian Medicines Formulary Framework, Appendix 1: Therapeutic
Classes of Medicines (AMH), supplied in full by the user. 21 top-level
classes expanded to their bottom-level (leaf) subclasses. This is the first
pass in Phase 5 whose drug list was NOT built by this project: it is external,
complete, and walked item by item with no subsetting.

Each leaf carries the named drugs that populate it. Drug membership is mine —
the source names the classes, not their members — and that is the one part of
this enumeration that is recall-based. It is a soft spot and is reported as
one: a leaf can only be found present through a drug I thought to list.

SCORING (inherits drug_depth.py, including its fixes)
Paragraphs, not character windows. Two verdicts per leaf:
    entry   best SINGLE paragraph — does one place actually teach the class
    corpus  union of every paragraph — is the fact present anywhere at all
`entry` is the primary verdict, because the union score was found last pass to
manufacture ADEQUATE out of mechanism in one file and a dose in another.
Meta files (workflow, tracker) are excluded: they name drugs while describing
the gaps in them, so a scan reading them reports coverage it wrote itself.

A dimension is a keyword proxy and a proxy can be satisfied by a word that has
nothing to do with the class. ADEQUATE therefore means "nothing this scan can
see is missing", never "taught well". Verdicts below ADEQUATE are the findings.
"""
import re, glob, os, sys
from collections import Counter

# (top-level class, leaf subclass, {member drug: regex})
LEAVES = [
("1 Allergy and anaphylaxis","Sympathomimetics (anaphylaxis)","adrenaline|epinephrine|EpiPen|Anapen"),
("1 Allergy and anaphylaxis","Sedating antihistamines","promethazine|chlorphenamine|chlorpheniramine|diphenhydramine|cyproheptadine|trimeprazine"),
("1 Allergy and anaphylaxis","Less sedating antihistamines","cetirizine|loratadine|fexofenadine|desloratadine|levocetirizine"),
("2 Anaesthetics","IV general anaesthetics","propofol|ketamine|thiopent|etomidate"),
("2 Anaesthetics","Inhaled anaesthetics","sevoflurane|isoflurane|desflurane|nitrous oxide|halothane"),
("2 Anaesthetics","Non-depolarising neuromuscular blockers","rocuronium|vecuronium|atracurium|cisatracurium|pancuronium"),
("2 Anaesthetics","Depolarising neuromuscular blockers","suxamethonium|succinylcholine"),
("2 Anaesthetics","Alpha2 and imidazoline agonists","dexmedetomidine|clonidine"),
("2 Anaesthetics","Opioids (anaesthesia)","fentanyl|remifentanil|alfentanil|sufentanil"),
("2 Anaesthetics","Anticholinergics (anaesthesia)","atropine|glycopyrrolate|glycopyrronium|hyoscine"),
("2 Anaesthetics","Drugs for reversing neuromuscular blockade","neostigmine|sugammadex"),
("2 Anaesthetics","Local anaesthetics","lignocaine|lidocaine|bupivacaine|ropivacaine|prilocaine|EMLA"),
("3 Analgesics","Non-opioid analgesics","paracetamol|acetaminophen|ibuprofen|aspirin"),
("3 Analgesics","Opioid analgesics","morphine|oxycodone|codeine|tramadol|buprenorphine|hydromorphone|tapentadol|fentanyl"),
("4 Antidotes and antivenoms","Gastrointestinal decontaminants","activated charcoal|whole bowel irrigation|gastric lavage"),
("4 Antidotes and antivenoms","Antidotes","naloxone|acetylcysteine|flumazenil|pralidoxime|digoxin.{0,12}Fab|desferrioxamine|fomepizole|methylene blue|Intralipid|lipid emulsion"),
("4 Antidotes and antivenoms","Snake antivenoms","snake antivenom|brown snake|tiger snake|polyvalent antivenom|taipan|death adder"),
("4 Antidotes and antivenoms","Other antivenoms","redback|funnel.?web|box jellyfish|stonefish|antivenom"),
("5 Anti-infectives","Aminoglycosides","gentamicin|tobramycin|amikacin|aminoglycoside"),
("5 Anti-infectives","Carbapenems","meropenem|imipenem|ertapenem|carbapenem"),
("5 Anti-infectives","Cephalosporins","cefalexin|cephalexin|cefazolin|cephazolin|cefuroxime|ceftriaxone|cefotaxime|ceftazidime|cefepime|cephalosporin"),
("5 Anti-infectives","Glycopeptides","vancomycin|teicoplanin|glycopeptide"),
("5 Anti-infectives","Lincosamides","clindamycin|lincomycin|lincosamide"),
("5 Anti-infectives","Macrolides","azithromycin|clarithromycin|erythromycin|roxithromycin|macrolide"),
("5 Anti-infectives","Penicillins","penicillin|amoxicillin|amoxycillin|ampicillin|flucloxacillin|piperacillin|benzathine"),
("5 Anti-infectives","Quinolones","ciprofloxacin|norfloxacin|moxifloxacin|levofloxacin|ofloxacin|quinolone"),
("5 Anti-infectives","Rifamycins","rifampicin|rifabutin|rifaximin|rifamycin"),
("5 Anti-infectives","Tetracyclines","doxycycline|minocycline|tetracycline|tigecycline"),
("5 Anti-infectives","Antimycobacterials","isoniazid|pyrazinamide|ethambutol|dapsone|clofazimine|antitubercul"),
("5 Anti-infectives","Other antibacterials","trimethoprim|nitrofurantoin|metronidazole|fosfomycin|linezolid|chloramphenicol|sulfamethoxazole"),
("5 Anti-infectives","Azoles (antifungal)","fluconazole|itraconazole|voriconazole|posaconazole|ketoconazole|clotrimazole|miconazole"),
("5 Anti-infectives","Echinocandins","caspofungin|anidulafungin|micafungin|echinocandin"),
("5 Anti-infectives","Other antifungals","terbinafine|amphotericin|nystatin|griseofulvin|flucytosine"),
("5 Anti-infectives","Guanine analogues (antiviral)","aciclovir|acyclovir|valaciclovir|famciclovir|ganciclovir"),
("5 Anti-infectives","Neuraminidase inhibitors","oseltamivir|zanamivir|peramivir"),
("5 Anti-infectives","Antivirals for viral hepatitis","entecavir|sofosbuvir|velpatasvir|glecaprevir|ribavirin|adefovir|direct.acting antiviral"),
("5 Anti-infectives","Other antivirals","cidofovir|foscarnet|palivizumab|nirmatrelvir|molnupiravir|remdesivir"),
("5 Anti-infectives","NRTIs","tenofovir|emtricitabine|lamivudine|abacavir|zidovudine|nucleoside reverse"),
("5 Anti-infectives","NNRTIs","efavirenz|nevirapine|rilpivirine|doravirine|non.nucleoside reverse"),
("5 Anti-infectives","HIV-Protease inhibitors","ritonavir|darunavir|atazanavir|lopinavir|protease inhibitor"),
("5 Anti-infectives","Integrase inhibitors","dolutegravir|raltegravir|bictegravir|elvitegravir|integrase"),
("5 Anti-infectives","Other antiretrovirals","maraviroc|enfuvirtide|cabotegravir"),
("5 Anti-infectives","Antimalarials","artemether|lumefantrine|atovaquone|proguanil|chloroquine|primaquine|mefloquine|quinine|Riamet|Malarone"),
("5 Anti-infectives","Other antiprotozoals","metronidazole|tinidazole|paromomycin|pentamidine|nitazoxanide|pyrimethamine"),
("5 Anti-infectives","Benzimidazoles (anthelmintic)","albendazole|mebendazole|triclabendazole"),
("5 Anti-infectives","Other anthelmintics","praziquantel|ivermectin|pyrantel|niclosamide"),
("6 Cardiovascular","Aldosterone antagonists","spironolactone|eplerenone"),
("6 Cardiovascular","Loop diuretics","frusemide|furosemide|bumetanide|loop diuretic"),
("6 Cardiovascular","Sympathomimetics (cardiovascular)","noradrenaline|norepinephrine|dobutamine|metaraminol|vasopressor|inotrope"),
("6 Cardiovascular","Other drugs for heart failure","digoxin|sacubitril|entresto|ivabradine"),
("6 Cardiovascular","Nitrates","glyceryl trinitrate|\\bGTN\\b|isosorbide|nitrate"),
("6 Cardiovascular","Other antianginal drugs","nicorandil|perhexiline|ranolazine"),
("6 Cardiovascular","Thiazide and related diuretics","hydrochlorothiazide|indapamide|chlortalidone|chlorthalidone|thiazide"),
("6 Cardiovascular","Other diuretics","acetazolamide|amiloride|mannitol|triamterene"),
("6 Cardiovascular","ACE inhibitors","ramipril|perindopril|enalapril|lisinopril|captopril|ACE inhibitor|ACEi"),
("6 Cardiovascular","Sartans","candesartan|irbesartan|telmisartan|valsartan|losartan|\\bARB\\b|angiotensin receptor blocker"),
("6 Cardiovascular","Calcium channel blockers","amlodipine|nifedipine|diltiazem|verapamil|felodipine|calcium channel blocker"),
("6 Cardiovascular","Beta-blockers","metoprolol|atenolol|bisoprolol|carvedilol|propranolol|labetalol|beta.?blocker"),
("6 Cardiovascular","Other antihypertensives","hydralazine|methyldopa|prazosin|minoxidil|moxonidine"),
("6 Cardiovascular","Antiarrhythmics","amiodarone|sotalol|flecainide|adenosine|digoxin|antiarrhythmic"),
("6 Cardiovascular","Statins","atorvastatin|rosuvastatin|simvastatin|pravastatin|\\bstatin"),
("6 Cardiovascular","Fibrates","gemfibrozil|fenofibrate|fibrate"),
("6 Cardiovascular","PCSK9 inhibitors","evolocumab|alirocumab|PCSK9|inclisiran"),
("6 Cardiovascular","Other drugs for dyslipidaemia","ezetimibe|nicotinic acid|colesevelam|cholestyramine|colestyramine"),
("6 Cardiovascular","Prostacyclins","epoprostenol|iloprost|treprostinil|prostacyclin"),
("6 Cardiovascular","Endothelin antagonists","bosentan|ambrisentan|macitentan|endothelin"),
("6 Cardiovascular","PDE5 inhibitors (cardiovascular)","sildenafil|tadalafil|phosphodiesterase 5"),
("6 Cardiovascular","Other drugs for pulmonary hypertension","riociguat|pulmonary hypertension"),
("6 Cardiovascular","Drugs for peripheral vascular disease","cilostazol|pentoxifylline|naftidrofuryl"),
("6 Cardiovascular","Drugs for orthostatic hypotension","fludrocortisone|midodrine|orthostatic hypotension"),
("7 Blood and electrolytes","Heparins","heparin|enoxaparin|dalteparin|Clexane"),
("7 Blood and electrolytes","Vitamin K antagonists","warfarin"),
("7 Blood and electrolytes","Direct thrombin inhibitors","dabigatran|bivalirudin|argatroban"),
("7 Blood and electrolytes","Factor Xa inhibitors","apixaban|rivaroxaban|edoxaban|factor Xa"),
("7 Blood and electrolytes","Glycoprotein IIb/IIIa inhibitors","abciximab|tirofiban|eptifibatide|IIb/IIIa"),
("7 Blood and electrolytes","Thienopyridines","clopidogrel|prasugrel|ticlopidine"),
("7 Blood and electrolytes","Other antiplatelet drugs","aspirin|dipyridamole|ticagrelor|antiplatelet"),
("7 Blood and electrolytes","Thrombolytics","alteplase|tenecteplase|streptokinase|thrombolysis|thrombolytic"),
("7 Blood and electrolytes","Other drugs affecting haemostasis","tranexamic|desmopressin|\\bDDAVP\\b|factor VIII|factor IX|fibrinogen concentrate"),
("7 Blood and electrolytes","Drugs for reversing anticoagulation","protamine|phytomenadione|vitamin K|idarucizumab|andexanet|Prothrombinex|prothrombin complex"),
# SOURCE DEFECT, FIXED HERE SO IT CANNOT PROPAGATE.
# The AMH appendix lists "Drugs for anaemias" TWICE under class 7 — once with
# subclasses (erythropoietin agonists / other drugs for anaemias) and once
# bare, immediately after. The bare repeat carries no subclasses and no
# distinct membership; it is a transcription artifact of the source, not a
# real class. It is deduplicated to the two leaves below, which is why this
# class contributes 16 leaves and not 17. A supplied enumeration is not
# automatically internally coherent: the partition check applies to it too.
# The assertion at the foot of this file makes a future re-transcription that
# reinstates the duplicate fail loudly instead of silently inflating a count.
("7 Blood and electrolytes","Erythropoietin agonists","epoetin|darbepoetin|erythropoietin"),
("7 Blood and electrolytes","Other drugs for anaemias","ferrous|iron polymaltose|ferric carboxymaltose|folic acid|hydroxocobalamin|cyanocobalamin|\\bB12\\b"),
("7 Blood and electrolytes","Drugs that chelate iron","desferrioxamine|deferasirox|deferiprone|iron chelation"),
("7 Blood and electrolytes","Drugs for potassium imbalance","resonium|sodium polystyrene|sodium zirconium|patiromer|potassium chloride|calcium gluconate|insulin.{0,20}dextrose"),
("7 Blood and electrolytes","Phosphate binders","sevelamer|lanthanum|calcium carbonate|phosphate binder"),
("7 Blood and electrolytes","Other drugs for electrolyte imbalance","magnesium sulfate|magnesium sulphate|hypertonic saline|tolvaptan|calcium gluconate|sodium bicarbonate"),
("8 Dermatological","Corticosteroids (skin)","betamethasone|mometasone|methylprednisolone aceponate|hydrocortisone.{0,20}(cream|ointment|topical)|topical (cortico)?steroid"),
("8 Dermatological","Tars","coal tar|\\btar\\b|LPC"),
("8 Dermatological","Other drugs for eczema","pimecrolimus|tacrolimus|emollient|dupilumab|moisturiser"),
("8 Dermatological","Immunosuppressants (psoriasis)","methotrexate|ciclosporin|cyclosporin|secukinumab|ustekinumab"),
("8 Dermatological","Other drugs for psoriasis","calcipotriol|dithranol|acitretin|phototherapy"),
("8 Dermatological","Retinoids (skin)","tretinoin|adapalene|tazarotene"),
("8 Dermatological","Retinoids (oral)","isotretinoin|acitretin"),
("8 Dermatological","Other drugs for acne","benzoyl peroxide|azelaic|spironolactone.{0,30}acne"),
("8 Dermatological","Azoles (skin)","clotrimazole|miconazole|ketoconazole"),
("8 Dermatological","Other antifungals (skin)","terbinafine|nystatin|griseofulvin"),
("8 Dermatological","Antibacterials (skin)","mupirocin|fusidic acid"),
("8 Dermatological","Antivirals (skin)","aciclovir.{0,25}(cream|topical|ointment)|topical aciclovir"),
("8 Dermatological","Scabicides and pediculicides","permethrin|benzyl benzoate|malathion|scabies|head lice"),
("8 Dermatological","Drugs for warts","salicylic acid|podophyllotoxin|imiquimod|cryotherapy|cantharidin"),
("8 Dermatological","Drugs for actinic keratoses","fluorouracil|imiquimod|ingenol|actinic keratos"),
("8 Dermatological","Drugs for alopecia","minoxidil|finasteride|alopecia"),
("8 Dermatological","Other dermatological drugs","hydroquinone|pimecrolimus|urea cream|keratolytic"),
("9 Ear, nose and throat","Antibacterials (ear)","framycetin|ciprofloxacin.{0,25}(ear|otic|drops)|Sofradex|ear drops"),
("9 Ear, nose and throat","Corticosteroids with anti-infectives (ear)","Sofradex|Ciproxin HC|dexamethasone.{0,25}(ear|otic)|Kenacomb"),
("9 Ear, nose and throat","Antiseptics (ear)","acetic acid|aluminium acetate|Burow"),
("9 Ear, nose and throat","Cerumenolytics","cerumenolytic|docusate.{0,20}ear|carbamide peroxide|ear wax|cerumen"),
("9 Ear, nose and throat","Drugs for vestibular disorders","betahistine|prochlorperazine|Stemetil|vestibular sedative"),
("9 Ear, nose and throat","Oral decongestants","pseudoephedrine|phenylephrine.{0,20}oral|oral decongestant"),
("9 Ear, nose and throat","Intranasal decongestants","oxymetazoline|xylometazoline|topical decongestant|nasal decongestant"),
("9 Ear, nose and throat","Corticosteroids (intranasal)","intranasal cortico|mometasone.{0,20}nasal|fluticasone.{0,20}nasal|budesonide.{0,20}nasal|nasal steroid|intranasal steroid"),
("9 Ear, nose and throat","Antihistamines (intranasal)","azelastine|intranasal antihistamine"),
("9 Ear, nose and throat","Other drugs for rhinitis and sinusitis","ipratropium.{0,20}nasal|saline (nasal|irrigation|spray)|nasal irrigation|montelukast"),
("9 Ear, nose and throat","Drugs for other nasal conditions","epistaxis|nasal packing|Naseptin|silver nitrate"),
("9 Ear, nose and throat","Drugs for mouth and throat conditions","chlorhexidine|benzydamine|nystatin.{0,25}(oral|drops|suspension)|oral candid"),
("10 Endocrine","Sulfonylureas","gliclazide|glimepiride|glipizide|glibenclamide|sulfonylurea|sulphonylurea"),
("10 Endocrine","Dipeptidyl peptidase-4 inhibitors","sitagliptin|linagliptin|vildagliptin|saxagliptin|\\bDPP.?4\\b|gliptin"),
("10 Endocrine","Glucagon-like peptide-1 analogues","semaglutide|dulaglutide|exenatide|liraglutide|\\bGLP.?1\\b|Ozempic"),
("10 Endocrine","Sodium-glucose co-transporter 2 inhibitors","empagliflozin|dapagliflozin|ertugliflozin|\\bSGLT2\\b|gliflozin"),
("10 Endocrine","Other drugs for diabetes","metformin|insulin|acarbose|pioglitazone"),
("10 Endocrine","Drugs for hypoglycaemia","glucagon|dextrose|glucose gel|hypoglycaemia"),
("10 Endocrine","Thyroid hormones","thyroxine|levothyroxine|liothyronine|Oroxine"),
("10 Endocrine","Antithyroid drugs","carbimazole|propylthiouracil|\\bPTU\\b|thionamide"),
("10 Endocrine","Other drugs for thyroid disorders","Lugol|radioactive iodine|radioiodine|potassium iodide"),
("10 Endocrine","Bisphosphonates","alendronate|risedronate|zoledronic|pamidronate|bisphosphonate"),
("10 Endocrine","Vitamin D","cholecalciferol|calcitriol|ergocalciferol|vitamin D"),
("10 Endocrine","Other drugs affecting bone","denosumab|teriparatide|raloxifene|romosozumab"),
("10 Endocrine","Corticosteroids (adrenal insufficiency)","hydrocortisone|fludrocortisone|prednisolone|dexamethasone"),
("10 Endocrine","Gonadotrophin-releasing hormone agonists","goserelin|leuprorelin|nafarelin|triptorelin|\\bGnRH\\b"),
("10 Endocrine","Other drugs for infertility","clomifene|clomiphene|letrozole.{0,30}(ovulat|infertil)|follicle stimulating hormone|\\bhCG\\b|ovulation induction"),
("10 Endocrine","Androgens","testosterone|androgen replacement|nandrolone"),
("10 Endocrine","Antidiuretic hormone agonists and antagonists","desmopressin|vasopressin|tolvaptan|\\bDDAVP\\b"),
("10 Endocrine","Growth hormone","somatropin|growth hormone"),
("10 Endocrine","Nonselective alpha-blockers","phenoxybenzamine|phentolamine"),
("10 Endocrine","Somatostatin analogues","octreotide|lanreotide|somatostatin analogue"),
("11 Eye","Aminoglycosides (eye)","(tobramycin|gentamicin|framycetin).{0,40}(eye|drops|ophthal)|(eye|ophthalmic|drops).{0,40}(tobramycin|framycetin)"),
("11 Eye","Quinolones (eye)","ciprofloxacin.{0,20}(eye|drops|ophthal)|ofloxacin.{0,20}(eye|drops|ophthal)"),
("11 Eye","Other antibacterials (eye)","chloramphenicol"),
("11 Eye","Antivirals (eye)","aciclovir.{0,25}(eye|ophthal|ointment)|ganciclovir gel"),
("11 Eye","Beta-blockers (eye)","timolol"),
("11 Eye","Prostaglandin analogues (eye)","latanoprost|bimatoprost|travoprost|prostaglandin analogue"),
("11 Eye","Alpha2 agonists (eye)","brimonidine|apraclonidine"),
("11 Eye","Carbonic anhydrase inhibitors","acetazolamide|dorzolamide|brinzolamide|carbonic anhydrase"),
("11 Eye","Other drugs for glaucoma","pilocarpine|mannitol.{0,25}(eye|glaucoma|IOP)"),
("11 Eye","Vasoconstrictors (eye)","naphazoline|ocular decongestant"),
("11 Eye","Antihistamines (eye)","olopatadine|ketotifen|(topical|ocular).{0,15}antihistamine|antihistamine.{0,25}(drops|eye|conjunctiv)"),
("11 Eye","Mast cell stabilisers","cromogl|nedocromil|lodoxamide|mast cell stabilis"),
("11 Eye","NSAIDs (eye)","ketorolac|diclofenac.{0,20}(eye|drops|ophthal)"),
("11 Eye","Corticosteroids (eye)","steroid eye drop|steroid drops|prednisolone.{0,25}(eye|drops|acetate)|dexamethasone.{0,25}(eye|drops)|topical steroid.{0,25}eye"),
("11 Eye","Other drugs for allergic eye conditions","allergic conjunctivitis"),
("11 Eye","Drugs for dry eyes","artificial tears|ocular lubricant|carmellose|hypromellose|dry eye"),
("11 Eye","Anticholinergics (eye)","cyclopentolate|tropicamide|homatropine|atropine.{0,20}(eye|drops)"),
("11 Eye","Other drugs for mydriasis","phenylephrine.{0,20}(eye|drops|dilat)|mydriatic"),
("11 Eye","Local anaesthetics (eye)","oxybuprocaine|amethocaine|proxymetacaine|tetracaine|topical anaesthetic.{0,20}eye"),
("12 Gastrointestinal","Antacids","antacid|Mylanta|Gaviscon|aluminium hydroxide|magnesium hydroxide"),
("12 Gastrointestinal","H2 antagonists","ranitidine|famotidine|nizatidine|H2.?(receptor )?antagonist|H2 blocker"),
("12 Gastrointestinal","Proton pump inhibitors","omeprazole|pantoprazole|esomeprazole|rabeprazole|lansoprazole|proton pump"),
("12 Gastrointestinal","Other drugs for ulcers","sucralfate|misoprostol"),
("12 Gastrointestinal","Drugs affecting gastrointestinal motility","metoclopramide|domperidone|prokinetic|hyoscine butylbromide|Buscopan"),
("12 Gastrointestinal","Dopamine antagonists (antiemetic)","metoclopramide|prochlorperazine|droperidol|haloperidol.{0,30}(nausea|vomit|emetic)"),
("12 Gastrointestinal","5HT3 antagonists","ondansetron|granisetron|tropisetron|5.?HT3"),
("12 Gastrointestinal","Substance P antagonists","aprepitant|fosaprepitant|substance P|NK1"),
("12 Gastrointestinal","Other drugs for nausea and vomiting","cyclizine|promethazine|dexamethasone.{0,30}(nausea|vomit|emetic)|hyoscine"),
("12 Gastrointestinal","Stool softeners","docusate|liquid paraffin|stool softener"),
("12 Gastrointestinal","Stimulant laxatives","senna|bisacodyl|sennoside|stimulant laxative"),
("12 Gastrointestinal","Osmotic laxatives","lactulose|macrogol|polyethylene glycol|sorbitol|osmotic laxative|Movicol"),
("12 Gastrointestinal","Other laxatives","psyllium|ispaghula|Metamucil|bulk.forming|fibre supplement"),
("12 Gastrointestinal","Opioid antidiarrhoeals","loperamide|diphenoxylate|Imodium"),
("12 Gastrointestinal","Other drugs for diarrhoea","octreotide.{0,30}diarrh|cholestyramine|colestyramine|racecadotril"),
("12 Gastrointestinal","Corticosteroids (gastrointestinal)","budesonide|prednisolone.{0,40}(colitis|Crohn|IBD|inflammatory bowel)|hydrocortisone.{0,40}(colitis|IBD)"),
("12 Gastrointestinal","5-Aminosalicylates","mesalazine|sulfasalazine|sulphasalazine|olsalazine|aminosalicylate|5.?ASA"),
("12 Gastrointestinal","Other drugs for inflammatory bowel disease","azathioprine|infliximab|adalimumab|vedolizumab|ustekinumab"),
("12 Gastrointestinal","Drugs for perianal disorders","haemorrhoid|Rectogesic|glyceryl trinitrate.{0,30}(fissure|anal)|anal fissure|Proctosedyl"),
("12 Gastrointestinal","Other gastrointestinal drugs","ursodeoxycholic|pancreatic enzyme|Creon|rifaximin|lactulose.{0,40}encephalopathy"),
("13 Genitourinary","Anticholinergics (genitourinary)","oxybutynin|solifenacin|tolterodine|darifenacin|antimuscarinic.{0,25}bladder"),
("13 Genitourinary","Other drugs for urinary incontinence","mirabegron|duloxetine.{0,30}(incontinen|stress)|desmopressin.{0,30}(enuresis|nocturia)"),
("13 Genitourinary","Selective alpha-blockers (genitourinary)","tamsulosin|prazosin|alfuzosin|silodosin|alpha.?blocker.{0,30}(prostat|BPH|urinary)"),
("13 Genitourinary","5-Alpha-reductase inhibitors","finasteride|dutasteride|5.?alpha.?reductase"),
("13 Genitourinary","Phosphodiesterase 5 inhibitors","sildenafil|tadalafil|vardenafil|\\bPDE5\\b"),
("13 Genitourinary","Other drugs for sexual dysfunction","alprostadil|erectile dysfunction|intracavernosal"),
("13 Genitourinary","Urinary alkalinisers and acidifiers","sodium citrate|potassium citrate|\\bUral\\b|urinary alkalinis"),
("13 Genitourinary","Drugs for kidney stones","potassium citrate|allopurinol.{0,30}stone|thiazide.{0,30}stone|medical expulsive"),
("13 Genitourinary","Bladder instillations","\\bBCG\\b.{0,40}bladder|mitomycin.{0,30}bladder|intravesical"),
("14 Immunomodulators and antineoplastics","Alkylating agents","cyclophosphamide|ifosfamide|busulfan|temozolomide|chlorambucil|alkylating"),
("14 Immunomodulators and antineoplastics","Anthracyclines","doxorubicin|daunorubicin|epirubicin|idarubicin|anthracycline"),
("14 Immunomodulators and antineoplastics","Antimetabolites","methotrexate|fluorouracil|capecitabine|gemcitabine|cytarabine|mercaptopurine|antimetabolite"),
("14 Immunomodulators and antineoplastics","Platinum compounds","cisplatin|carboplatin|oxaliplatin|platinum"),
("14 Immunomodulators and antineoplastics","Taxanes","paclitaxel|docetaxel|taxane"),
("14 Immunomodulators and antineoplastics","Topoisomerase I inhibitors","irinotecan|topotecan|topoisomerase"),
("14 Immunomodulators and antineoplastics","Vinca alkaloids","vincristine|vinblastine|vinorelbine|vinca"),
("14 Immunomodulators and antineoplastics","Other cytotoxic antineoplastics","bleomycin|etoposide|dacarbazine|mitomycin"),
("14 Immunomodulators and antineoplastics","Antineoplastic antibodies","rituximab|trastuzumab|bevacizumab|pembrolizumab|nivolumab|cetuximab|checkpoint inhibitor"),
("14 Immunomodulators and antineoplastics","Kinase inhibitors","imatinib|erlotinib|ibrutinib|sunitinib|osimertinib|kinase inhibitor|tinib\\b"),
("14 Immunomodulators and antineoplastics","Thalidomide analogues","thalidomide|lenalidomide|pomalidomide"),
("14 Immunomodulators and antineoplastics","Other non-cytotoxic antineoplastics","bortezomib|all.trans retinoic|\\bATRA\\b|azacitidine"),
("14 Immunomodulators and antineoplastics","Anti-androgens","bicalutamide|enzalutamide|abiraterone|cyproterone|anti.?androgen"),
("14 Immunomodulators and antineoplastics","Aromatase inhibitors","anastrozole|letrozole|exemestane|aromatase"),
("14 Immunomodulators and antineoplastics","GnRH agonists (oncology)","goserelin|leuprorelin|Zoladex"),
("14 Immunomodulators and antineoplastics","Selective oestrogen receptor modulators","tamoxifen|raloxifene|\\bSERM\\b"),
("14 Immunomodulators and antineoplastics","Other hormonal antineoplastics","megestrol|medroxyprogesterone.{0,30}(cancer|oncol)|fulvestrant"),
("14 Immunomodulators and antineoplastics","Colony stimulating factors","filgrastim|pegfilgrastim|\\bG.?CSF\\b|colony stimulating"),
("14 Immunomodulators and antineoplastics","Other drugs used with antineoplastics","rasburicase|mesna|folinic acid|leucovorin|allopurinol.{0,40}(tumour lysis|chemo)"),
("14 Immunomodulators and antineoplastics","Calcineurin inhibitors","ciclosporin|cyclosporin|tacrolimus|calcineurin"),
("14 Immunomodulators and antineoplastics","Corticosteroids (immunosuppressant)","prednisolone|prednisone|methylprednisolone|dexamethasone"),
("14 Immunomodulators and antineoplastics","Immunosuppressant antibodies","basiliximab|antithymocyte|\\bATG\\b|alemtuzumab"),
("14 Immunomodulators and antineoplastics","mTOR inhibitors","sirolimus|everolimus|\\bmTOR\\b"),
("14 Immunomodulators and antineoplastics","Other immunosuppressants","azathioprine|mycophenolate|\\bMMF\\b"),
("14 Immunomodulators and antineoplastics","Interferons","interferon"),
("15 Neurological","Barbiturates","phenobarbit|barbiturate|thiopent"),
("15 Neurological","Benzodiazepines (neurology)","diazepam|midazolam|clonazepam|lorazepam"),
("15 Neurological","Other antiepileptics","levetiracetam|valproate|phenytoin|carbamazepine|lamotrigine|topiramate|Keppra"),
("15 Neurological","Dopamine agonists (parkinsonism)","pramipexole|ropinirole|rotigotine|apomorphine|dopamine agonist"),
("15 Neurological","Anticholinergics (parkinsonism)","benztropine|benzhexol|trihexyphenidyl"),
("15 Neurological","Monoamine oxidase type B inhibitors","selegiline|rasagiline|\\bMAO.?B\\b"),
("15 Neurological","Other drugs for Parkinson's disease","levodopa|carbidopa|benserazide|entacapone|amantadine|Madopar|Sinemet"),
("15 Neurological","Triptans","sumatriptan|rizatriptan|zolmitriptan|eletriptan|naratriptan|triptan"),
("15 Neurological","Calcitonin gene-related peptide antagonists","erenumab|fremanezumab|galcanezumab|rimegepant|\\bCGRP\\b"),
("15 Neurological","Other drugs to prevent migraine","pizotifen|propranolol.{0,30}migraine|amitriptyline.{0,30}migraine|topiramate.{0,30}migraine|migraine prophylaxis"),
("15 Neurological","Anticholinesterases in Alzheimer's disease","donepezil|rivastigmine|galantamine|cholinesterase inhibitor"),
("15 Neurological","Other drugs for Alzheimer's disease","memantine"),
("15 Neurological","Drugs for multiple sclerosis","interferon beta|natalizumab|fingolimod|ocrelizumab|glatiramer|dimethyl fumarate|disease.modifying.{0,20}(therapy|MS)"),
("15 Neurological","Anticholinesterases in myasthenia gravis","pyridostigmine|neostigmine.{0,30}myasthen|Mestinon"),
("15 Neurological","Drugs for other neurological conditions","riluzole|tetrabenazine|baclofen|tizanidine|gabapentin|pregabalin"),
("16 Obstetric and gynaecological","Combined oral contraceptives","combined oral contraceptive|\\bCOCP?\\b|ethinyl.?oestradiol|ethinyl.?estradiol|levonorgestrel.{0,30}(pill|contracept)"),
("16 Obstetric and gynaecological","Progestogens","norethisterone|medroxyprogesterone|etonogestrel|Implanon|desogestrel|drospirenone|progestogen.only|\\bPOP\\b|Depo.?Provera"),
("16 Obstetric and gynaecological","Other combined contraceptives","vaginal ring|NuvaRing|contraceptive patch|transdermal contracept"),
("16 Obstetric and gynaecological","Intrauterine devices","Mirena|copper IUD|intrauterine device|\\bIUD\\b|Kyleena"),
("16 Obstetric and gynaecological","Hormone replacement therapy","hormone replacement|\\bHRT\\b|menopausal hormone|\\bMHT\\b|conjugated oestrogen|tibolone"),
("16 Obstetric and gynaecological","Drugs for heavy menstrual bleeding","tranexamic.{0,40}(menorrhag|menstrual|bleeding)|mefenamic|heavy menstrual bleeding"),
("16 Obstetric and gynaecological","Drugs for endometriosis","dienogest|danazol|endometriosis"),
("16 Obstetric and gynaecological","Drugs for preterm labour","nifedipine.{0,30}(tocoly|preterm)|tocoly|atosiban|salbutamol.{0,30}preterm"),
("16 Obstetric and gynaecological","Drugs in pre-eclampsia and eclampsia","magnesium sulfate|magnesium sulphate|labetalol|methyldopa|hydralazine"),
("16 Obstetric and gynaecological","Oxytocic drugs","oxytocin|Syntocinon|ergometrine|Syntometrine|carbetocin"),
("16 Obstetric and gynaecological","Prostaglandins","misoprostol|dinoprostone|carboprost|prostaglandin E"),
("16 Obstetric and gynaecological","Other drugs used in obstetrics","anti.?D|Rh\\(D\\) immunoglobulin"),
("16 Obstetric and gynaecological","Drugs affecting lactation","domperidone.{0,30}lactat|cabergoline|bromocriptine|galactagogue|suppress lactation"),
("16 Obstetric and gynaecological","Azoles (vaginal)","clotrimazole.{0,30}(pessary|vaginal|cream)|vaginal.{0,20}azole|fluconazole.{0,40}(vulvovaginal|thrush)"),
("16 Obstetric and gynaecological","Other vaginal anti-infectives","metronidazole.{0,30}(gel|vaginal)|nystatin.{0,25}pessary|vaginal cream"),
("16 Obstetric and gynaecological","Drugs for menstrual symptoms","mefenamic|dysmenorrh|NSAID.{0,30}(period|menstrual)"),
("17 Psychotropic","Monoamine oxidase inhibitors","phenelzine|tranylcypromine|moclobemide|\\bMAOI\\b"),
("17 Psychotropic","Selective serotonin reuptake inhibitors","sertraline|fluoxetine|citalopram|escitalopram|paroxetine|fluvoxamine|\\bSSRI\\b"),
("17 Psychotropic","Tricyclic antidepressants","amitriptyline|nortriptyline|imipramine|clomipramine|dothiepin|dosulepin|tricyclic|\\bTCA\\b"),
("17 Psychotropic","Serotonin and noradrenaline reuptake inhibitors","venlafaxine|desvenlafaxine|duloxetine|\\bSNRI\\b"),
("17 Psychotropic","Other antidepressants","mirtazapine|agomelatine|vortioxetine|bupropion|reboxetine"),
("17 Psychotropic","Antipsychotics","olanzapine|risperidone|quetiapine|haloperidol|clozapine|aripiprazole|antipsychotic"),
("17 Psychotropic","Drugs for bipolar disorder","lithium|mood stabilis"),
("17 Psychotropic","Benzodiazepines","diazepam|temazepam|oxazepam|lorazepam|alprazolam|benzodiazepine"),
("17 Psychotropic","Non-amphetamine psychostimulants","modafinil|armodafinil"),
("17 Psychotropic","Orexin receptor antagonists","suvorexant|lemborexant|orexin"),
("17 Psychotropic","Other drugs for anxiety and sleep disorders","zopiclone|zolpidem|melatonin|buspirone"),
("17 Psychotropic","Psychostimulants","methylphenidate|dexamphetamine|lisdexamfetamine|Ritalin|Vyvanse"),
("17 Psychotropic","Other drugs for attention deficit hyperactivity disorder","atomoxetine|guanfacine|clonidine.{0,30}ADHD"),
("17 Psychotropic","Drugs for alcohol dependence","naltrexone|acamprosate|disulfiram"),
("17 Psychotropic","Drugs for nicotine dependence","varenicline|nicotine replacement|\\bNRT\\b|bupropion|nicotine patch"),
("17 Psychotropic","Drugs for opioid dependence","methadone|buprenorphine.{0,25}naloxone|Suboxone|opioid substitution|naltrexone.{0,30}opioid"),
("17 Psychotropic","Other psychotropic drugs","thiamine|electroconvulsive|\\bECT\\b|ketamine.{0,30}depress"),
("18 Respiratory","Beta2 agonists","salbutamol|terbutaline|salmeterol|formoterol|vilanterol|beta.?2 agonist|\\bSABA\\b|\\bLABA\\b"),
("18 Respiratory","Anticholinergics (inhaled)","ipratropium|tiotropium|umeclidinium|glycopyrronium.{0,25}inhal|\\bLAMA\\b|\\bSAMA\\b"),
("18 Respiratory","Theophyllines","theophylline|aminophylline"),
("18 Respiratory","Corticosteroids (inhaled)","inhaled cortico|\\bICS\\b|budesonide.{0,25}inhal|fluticasone|beclometasone|beclomethasone|ciclesonide"),
("18 Respiratory","Other drugs for asthma","montelukast|omalizumab|mepolizumab|benralizumab|leukotriene"),
("18 Respiratory","Opioid cough suppressants","pholcodine|dextromethorphan|codeine.{0,25}cough|cough suppress"),
("18 Respiratory","Mucolytics","acetylcysteine|bromhexine|dornase|mucolytic|hypertonic saline.{0,30}(nebul|CF|bronchiol)"),
("18 Respiratory","Drugs used in cystic fibrosis","ivacaftor|lumacaftor|elexacaftor|tezacaftor|\\bCFTR\\b|dornase"),
("18 Respiratory","Pulmonary surfactants","surfactant|poractant|beractant|Curosurf"),
("18 Respiratory","Other respiratory drugs","nintedanib|pirfenidone|roflumilast"),
("19 Rheumatological","TNF-alpha antagonists","infliximab|adalimumab|etanercept|golimumab|certolizumab|\\bTNF\\b"),
("19 Rheumatological","Immunosuppressants (rheumatology)","methotrexate|leflunomide|azathioprine|hydroxychloroquine|sulfasalazine|sulphasalazine|\\bDMARD\\b"),
("19 Rheumatological","Other immunomodulating drugs","tocilizumab|rituximab|abatacept|tofacitinib|baricitinib|\\bJAK\\b"),
("19 Rheumatological","Xanthine oxidase inhibitors","allopurinol|febuxostat|xanthine oxidase"),
("19 Rheumatological","Other drugs for gout","colchicine|probenecid"),
("19 Rheumatological","NSAIDs","ibuprofen|naproxen|diclofenac|indomethacin|celecoxib|meloxicam|\\bNSAID"),
("20 Vaccines","Vaccines","vaccin|immunisation|immunization"),
("21 Miscellaneous","Specialised drugs","enzyme replacement|orphan drug|thrombopoietin|eculizumab"),
("21 Miscellaneous","Blood products","packed red|fresh frozen plasma|\\bFFP\\b|platelet transfusion|cryoprecipitate|albumin.{0,20}(infusion|4%|20%)|red cell transfusion"),
("21 Miscellaneous","Immunoglobulins","immunoglobulin|\\bIVIg\\b|\\bVZIG\\b|\\bHBIG\\b|tetanus immunoglobulin"),
]

_seen = [(t, l) for t, l, _ in LEAVES]
assert len(_seen) == len(set(_seen)), \
    f"duplicate leaf in the enumeration: {[k for k in set(_seen) if _seen.count(k) > 1]}"

MECH = re.compile(r"mechanism|inhibit|agonist|antagonist|blocks?\b|receptor|bacteriocid|bactericid|bacteriostat|cell wall|ribosom|beta.?lactam|β.?lactam|DNA gyrase|folate|ergosterol|protein synthesis|binds|acts on|transpeptid|topoisomerase|reverse transcript|reduces? (production|synthesis)|increases? (excretion|uptake)|vasodilat|works by", re.I)
DOSE = re.compile(r"\d+\s*(mg|g|micrograms|mcg|units|IU|mL|%)\b|\bmg/kg\b|\bBD\b|\bTDS\b|\bQID\b|\bnocte\b|\bPRN\b|\bIV\b|\bIM\b|\bsubcut|\boral(ly)?\b|\bdaily\b|\btitrat", re.I)
HARM = re.compile(r"side.?effect|adverse|toxicit|monitor|trough level|nephrotox|ototox|hepatotox|\bQT\b|C\.? ?difficile|diarrhoea|rash|nausea|marrow|neutropen|photosensitiv|tendon|myopath|neuropath|hypotension|bradycard|hyperkalaem|hypokalaem|bleeding risk|weight gain|\bEPSE\b|withdrawal", re.I)
CONTRA = re.compile(r"contraindicat|caution|avoid|not (in|for|used|recommended)|allerg|anaphyla|pregnan|renal impair|hepatic impair|interact|resistan|\bCYP\b|warfarin|breastfeed|asthma\b.{0,20}avoid|do not (give|use)", re.I)
DIMS = (("mech",MECH),("dose",DOSE),("harm",HARM),("contra",CONTRA))

META = {"CLAUDE.md","CLAUDE_CODE_PROMPT.md","COWORK_HANDOFF.md",
        "MASTER_VERIFICATION_WORKFLOW.md","PENDING_GUIDELINE_CHECKS.md",
        "PHASE_EXECUTION_WORKFLOW.md","RECOMMENDED_WORKFLOW.md"}

def paragraphs(text, rx):
    out=[]
    for m in rx.finditer(text):
        s=text.rfind("\n\n",0,m.start()); s=0 if s<0 else s+2
        e=text.find("\n\n",m.end()); e=len(text) if e<0 else e
        out.append(text[s:e])
    return out

def score(t): return [d for d,r in DIMS if r.search(t)]
def verdict(dims, any_para):
    if not any_para: return "ABSENT"
    if len(dims)>=3: return "ADEQUATE"
    return "THIN" if dims else "NAMED ONLY"

def main():
    root=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..")
    corpus=[(os.path.basename(f), open(f,encoding="utf-8").read())
            for f in sorted(glob.glob(os.path.join(root,"*.md")))
            if os.path.basename(f) not in META]
    counts=Counter(); splits=[]; n=0
    for top,leaf,pat in LEAVES:
        n+=1
        rx=re.compile(pat,re.I)
        paras=[]; files=set(); hits=0
        for name,text in corpus:
            p=paragraphs(text,rx)
            if p: hits+=len(p); files.add(name)
            paras+=p
        udims=score("\n".join(paras))
        best=max((score(x) for x in paras), key=len, default=[])
        uv=verdict(udims,paras); ev=verdict(best,paras)
        counts[ev]+=1
        if uv!=ev: splits.append((n,leaf,uv,ev))
        # which member drugs are named at all
        # Member-level presence. Splitting the pattern on "|" can cut an
        # alternation group in half, so an unparseable fragment is skipped
        # rather than allowed to abort the run.
        blob="\n".join(paras); members=[]; found=0
        for m_ in pat.split("|"):
            try: rr=re.compile(m_,re.I)
            except re.error: continue
            members.append(m_)
            if rr.search(blob): found+=1
        flag="  <<ASSEMBLED>>" if uv!=ev else ""
        print(f"{n:3d}|{top}|{leaf}|{ev}|{uv}|{hits}|{len(files)}|{found}/{len(members)}|{'+'.join(best) or '-'}{flag}")
    print("---")
    print("ENTRY-LEVEL TOTALS", len(LEAVES), dict(counts))
    print("CORPUS/ENTRY SPLITS", len(splits))
    for s in splits: print("  split:", s)

if __name__=="__main__":
    main()
