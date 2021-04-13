# VulnerableACFGgenerator
The vulnerable function generate from OpenSSL
抓取Openssl資料集中指定的functionname另存成json檔
預設使用四個漏洞function


# Usage
> git clone https://github.com/doggy33/VulnerableACFGgenerator.git
> python3 VulnerACFGgenerator.py -f <function_name1,function_name2,...>


# Example 
> python3 VulnerACFGgenerator.py
> 

# Vulnerable Function
> 1. v2i_POLICY_MAPPINGS
> 2. genrsa_main
> 3. priv_decode_gost
> 4. prompt_info
> 5. ssl3_get_message
