import os
import argparse
import json

SAVENAME = "vulnerACFG.json"

def get_openssl_file_name(PATH, SF, CM, OP, VS):
    F_NAME = []
    for sf in SF:
        for cm in CM:
            for op in OP:
                for vs in VS:
                    F_NAME.append(PATH+sf+cm+op+vs+".json")
    return F_NAME


def compare(F_NAME,all_function):
	function_feature = {}
	for f_name in F_NAME:
		with open(f_name) as inf:
			for line in inf:
				g_info = json.loads(line.strip())
				try:
					for func in all_function:
						if (func in g_info["fname"]):
							function_feature["src"] = g_info["src"]
							function_feature["fname"] = g_info["fname"]
							function_feature["features"] = g_info["features"]
							function_feature["succs"] = g_info["succs"]
							function_feature["n_num"] = g_info["n_num"] 
						
							with open(SAVENAME, "a+", encoding="utf-8") as f:
								f.read()
								f.writelines(json.JSONEncoder().encode(function_feature)+"\n")
				except Exception as e:
					print("exception : ",e)


def generator(F_NAME):

	DATA_PATH = './data/acfgSSL_7/'
	SOFTWARE=('openssl-1.0.1f-', 'openssl-1.0.1u-')	
	COMPILER=('armeb-linux', 'i586-linux', 'mips-linux')
	OPTIMIZATION=('-O0', '-O1','-O2','-O3')
	VERSION=('v54',)
	FILE_NAME = get_openssl_file_name(DATA_PATH, SOFTWARE, COMPILER,OPTIMIZATION, VERSION)
	compare(FILE_NAME,F_NAME)



if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-f','--function', type=str,default='v2i_POLICY_MAPPINGS,genrsa_main,priv_decode_gost,prompt_info,ssl3_get_message',help='The function name you want to get , split by comma')
	args = parser.parse_args()
	
	F_NAME = args.function.split(",")
	generator(F_NAME)
	print("Save file > ",SAVENAME)
