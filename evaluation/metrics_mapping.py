scenario2metric = {
    # HFV1 https://huggingface.co/docs/leaderboards/en/open_llm_leaderboard/archive
    "arc_challenge": "acc_norm",
    "hellaswag": "acc_norm",
    "truthfulqa_mc2": "acc",
    "winogrande": "acc",
    "gsm8k": "exact_match,strict-match",  # this was changed as a later version of lmeval acc->exact_match,strict-match
    "mmlu_abstract_algebra": "acc",
    "mmlu_anatomy": "acc",
    "mmlu_astronomy": "acc",
    "mmlu_business_ethics": "acc",
    "mmlu_clinical_knowledge": "acc",
    "mmlu_college_biology": "acc",
    "mmlu_college_chemistry": "acc",
    "mmlu_college_computer_science": "acc",
    "mmlu_college_mathematics": "acc",
    "mmlu_college_medicine": "acc",
    "mmlu_college_physics": "acc",
    "mmlu_computer_security": "acc",
    "mmlu_conceptual_physics": "acc",
    "mmlu_econometrics": "acc",
    "mmlu_electrical_engineering": "acc",
    "mmlu_elementary_mathematics": "acc",
    "mmlu_formal_logic": "acc",
    "mmlu_global_facts": "acc",
    "mmlu_high_school_biology": "acc",
    "mmlu_high_school_chemistry": "acc",
    "mmlu_high_school_computer_science": "acc",
    "mmlu_high_school_european_history": "acc",
    "mmlu_high_school_geography": "acc",
    "mmlu_high_school_government_and_politics": "acc",
    "mmlu_high_school_macroeconomics": "acc",
    "mmlu_high_school_mathematics": "acc",
    "mmlu_high_school_microeconomics": "acc",
    "mmlu_high_school_physics": "acc",
    "mmlu_high_school_psychology": "acc",
    "mmlu_high_school_statistics": "acc",
    "mmlu_high_school_us_history": "acc",
    "mmlu_high_school_world_history": "acc",
    "mmlu_human_aging": "acc",
    "mmlu_human_sexuality": "acc",
    "mmlu_international_law": "acc",
    "mmlu_jurisprudence": "acc",
    "mmlu_logical_fallacies": "acc",
    "mmlu_machine_learning": "acc",
    "mmlu_management": "acc",
    "mmlu_marketing": "acc",
    "mmlu_medical_genetics": "acc",
    "mmlu_miscellaneous": "acc",
    "mmlu_moral_disputes": "acc",
    "mmlu_moral_scenarios": "acc",
    "mmlu_nutrition": "acc",
    "mmlu_philosophy": "acc",
    "mmlu_prehistory": "acc",
    "mmlu_professional_accounting": "acc",
    "mmlu_professional_law": "acc",
    "mmlu_professional_medicine": "acc",
    "mmlu_professional_psychology": "acc",
    "mmlu_public_relations": "acc",
    "mmlu_security_studies": "acc",
    "mmlu_sociology": "acc",
    "mmlu_us_foreign_policy": "acc",
    "mmlu_virology": "acc",
    "mmlu_world_religions": "acc",
    # Other
    "piqa": "acc_norm",
    "openbookqa": "acc_norm",
    "boolq": "acc",
    # Safety
    "ethos_binary_temp_2_few_shot_0": "f1_macro",
    "ethos_binary_temp_2_few_shot_5": "f1_macro",
    "toxigen": "acc",
    "pop_qa_temp_0_few_shot_0": "accuracy",
    "pop_qa_temp_0_few_shot_5": "accuracy",
    "toxigen_temp_0_few_shot_0": "accuracy",
    "toxigen_temp_0_few_shot_5": "accuracy",
    "bbq_Age_temp_0_few_shot_0": "f1_macro",
    "bbq_Age_temp_0_few_shot_5": "f1_macro",
    "bbq_Disability_status_temp_0_few_shot_0": "f1_macro",
    "bbq_Disability_status_temp_0_few_shot_5": "f1_macro",
    "bbq_Gender_identity_temp_0_few_shot_0": "f1_macro",
    "bbq_Gender_identity_temp_0_few_shot_5": "f1_macro",
    "bbq_Nationality_temp_0_few_shot_0": "f1_macro",
    "bbq_Nationality_temp_0_few_shot_5": "f1_macro",
    "bbq_Physical_appearance_temp_0_few_shot_0": "f1_macro",
    "bbq_Physical_appearance_temp_0_few_shot_5": "f1_macro",
    "bbq_Race_ethnicity_temp_0_few_shot_0": "f1_macro",
    "bbq_Race_ethnicity_temp_0_few_shot_5": "f1_macro",
    "bbq_Race_x_gender_temp_0_few_shot_0": "f1_macro",
    "bbq_Race_x_gender_temp_0_few_shot_5": "f1_macro",
    "bbq_Race_x_SES_temp_0_few_shot_0": "f1_macro",
    "bbq_Race_x_SES_temp_0_few_shot_5": "f1_macro",
    "bbq_Religion_temp_0_few_shot_0": "f1_macro",
    "bbq_Religion_temp_0_few_shot_5": "f1_macro",
    "bbq_SES_temp_0_few_shot_0": "f1_macro",
    "bbq_SES_temp_0_few_shot_5": "f1_macro",
    "bbq_Sexual_orientation_temp_0_few_shot_0": "f1_macro",
    "bbq_Sexual_orientation_temp_0_few_shot_5": "f1_macro",
}
