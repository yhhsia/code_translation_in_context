import os
import requests
import openai
from codegen_sources.model.src.evaluation.comp_acc_computation import (
    load_evosuite_transcoder_tests,
    eval_function_output,

)
from codegen_sources.model.src.evaluation.evaluator import (
    compute_bleu
)


hypotheses_path = "./test_data_ids"
# ids_cpp_java_path = hypotheses_path + "/ids.cpp_sa-java_sa.valid.txt"
ids_cpp_java_path = hypotheses_path + "/ids.cpp_sa-java_sa.test.txt"

# ids_cpp_python_path = hypotheses_path + "/ids.cpp_sa-python_sa.valid.txt"

ids_cpp_python_path = hypotheses_path + "/ids.cpp_sa-python_sa.test.txt"

ids_java_python_path = hypotheses_path + "/ids.java_sa-python_sa.test.txt"




# ref_path = hypotheses_path + "/ref.cpp_sa-python_sa.valid.txt"
cpp_python_test_ref_path = hypotheses_path + "/ref.cpp_sa-python_sa.test.txt"
# cpp_python_test_ref_path = hypotheses_path + "/ref.cpp_sa-python_sa.valid.txt"
java_cpp_test_ref_path = hypotheses_path + "/ref.java_sa-cpp_sa.test.txt"
python_java_test_ref_path = hypotheses_path + "/ref.python_sa-java_sa.test.txt"
java_python_test_ref_path = hypotheses_path + "/ref.java_sa-python_sa.test.txt"
python_cpp_test_ref_path = hypotheses_path + "/ref.python_sa-cpp_sa.test.txt"
# hyp_paths = [hypotheses_path+"/hyp0.cpp_sa-python_sa.valid.txt"]
# cpp_python_test_hyp_paths = [hypotheses_path+"/cpp_python.txt"]
# cpp_python_test_hyp_paths = [hypotheses_path+"/cpp-python_one_shot.txt"]
cpp_python_test_hyp_paths = [hypotheses_path+"/cpp_python_mistral.txt"]
# cpp_python_test_hyp_paths = [hypotheses_path+"/cpp_python_mistral_in_context.txt"]
java_cpp_test_hyp_paths = [hypotheses_path+"/java_cpp.txt"]
python_java_test_hyp_paths = [hypotheses_path+"/python_java.txt"]
# java_python_test_hyp_paths = [hypotheses_path+"/java_python.txt"]
# java_python_test_hyp_paths = [hypotheses_path+"/java_python_one_shot.txt"]
# java_python_test_hyp_paths = [hypotheses_path+"/java_python_mistral_in_context.txt"]
java_python_test_hyp_paths = [hypotheses_path+"/java_python_mistral.txt"]
# python_cpp_test_hyp_paths = [hypotheses_path+"/python_cpp.txt"]
python_cpp_test_hyp_paths = [hypotheses_path+"/python_cpp_mistral.txt"]

cpp_python_test_outfolder = "./test_data_ids/unit_tests/cpp_sa-python_sa.test"
# cpp_python_test_outfolder = "./output/transcoder_eval/80hqayml6e/eval_scripts/cpp_sa-python_sa.valid"
java_cpp_test_outfolder = "./test_data_ids/unit_tests/java_sa-cpp_sa.test"
python_java_test_outfolder = "./test_data_ids/unit_tests/python_sa-java_sa.test"
java_python_test_outfolder = "./test_data_ids/unit_tests/java_sa-python_sa.test"
python_cpp_test_outfolder = "./test_data_ids/unit_tests/python_sa-cpp_sa.test"

eval_script_folder = "./../data/transcoder_evaluation_gfg"
# evosuite_test = load_evosuite_transcoder_tests()
scores = {}
def main():
    # CPP TO PYTHON EVAL
    func_run_stats, func_run_out = eval_function_output(
                cpp_python_test_ref_path,
                cpp_python_test_hyp_paths,
                ids_cpp_python_path,
                "cpp",
                "python",
                cpp_python_test_outfolder,
                eval_script_folder,
                False,
                "fastbpe",
                tests_type="GfG"
                # evosuite_tests=evosuite_test
            )

    print(func_run_stats)
    # print(func_run_out)

    compute_bleu(
        cpp_python_test_hyp_paths[0],
        cpp_python_test_ref_path,
        "bleu_stuff_cpp_python",
        scores
    )
    print(scores["bleu_stuff_cpp_python"])



    ### JAVA TO CPP EVAL
    func_run_stats, func_run_out = eval_function_output(
                java_cpp_test_ref_path,
                java_cpp_test_hyp_paths,
                ids_cpp_java_path,
                "java",
                "cpp",
                java_cpp_test_outfolder,
                eval_script_folder,
                False,
                "fastbpe",
                tests_type="GfG"
                # evosuite_tests=evosuite_test
            )

    print(func_run_stats)
    # print(func_run_out)

    compute_bleu(
        java_cpp_test_hyp_paths[0],
        java_cpp_test_ref_path,
        "bleu_stuff_java_cpp",
        scores
    )
    print(scores["bleu_stuff_java_cpp"])


    ##### JAVA TO PYTHON EVAL #######
    func_run_stats, func_run_out = eval_function_output(
                java_python_test_ref_path,
                java_python_test_hyp_paths,
                ids_java_python_path,
                "java",
                "python",
                java_python_test_outfolder,
                eval_script_folder,
                False,
                "fastbpe",
                tests_type="GfG"
                # evosuite_tests=evosuite_test
            )

    print(func_run_stats)
    print(func_run_out)

    compute_bleu(
        java_python_test_hyp_paths[0],
        java_python_test_ref_path,
        "bleu_stuff_java_python",
        scores
    )
    print(scores["bleu_stuff_java_python"])

    #### JAVA TO PYTHON EVAL  ####
    func_run_stats, func_run_out = eval_function_output(
                java_python_test_ref_path,
                java_python_test_hyp_paths,
                ids_java_python_path,
                "java",
                "python",
                java_python_test_outfolder,
                eval_script_folder,
                False,
                "fastbpe",
                tests_type="GfG"
                # evosuite_tests=evosuite_test
            )

    print(func_run_stats)
    print(func_run_out)

    compute_bleu(
        java_python_test_hyp_paths[0],
        java_python_test_ref_path,
        "bleu_stuff_java_python",
        scores
    )
    print(scores["bleu_stuff_java_python"])

    # PYTHON TO CPP EVAL
    func_run_stats, func_run_out = eval_function_output(
                python_cpp_test_ref_path,
                python_cpp_test_hyp_paths,
                ids_cpp_python_path,
                "python",
                "cpp",
                python_cpp_test_outfolder,
                eval_script_folder,
                False,
                "fastbpe",
                tests_type="GfG"
                # evosuite_tests=evosuite_test
            )

    print(func_run_stats)
    # print(func_run_out)

    compute_bleu(
        python_cpp_test_hyp_paths[0],
        python_cpp_test_ref_path,
        "bleu_stuff_python_cpp",
        scores
    )
    print(scores["bleu_stuff_python_cpp"])


    # CPP TO PYTHON EVAL IN CONTEXT
    func_run_stats, func_run_out = eval_function_output(
                cpp_python_test_ref_path,
                cpp_python_one_shot_test_hyp_paths,
                ids_cpp_python_path,
                "cpp",
                "python",
                cpp_python_test_outfolder,
                eval_script_folder,
                False,
                "fastbpe",
                tests_type="GfG"
                # evosuite_tests=evosuite_test
            )

    print(func_run_stats)
    # print(func_run_out)

    compute_bleu(
        cpp_python_one_shot_test_hyp_paths[0],
        cpp_python_test_ref_path,
        "bleu_stuff_cpp_python",
        scores
    )
    print(scores["bleu_stuff_cpp_python"])
if __name__ == '__main__':
    main()

