## anvil

> `/usr/libexec/postfix/anvil`

```diff

-  __TEXT.__text: 0x28a68
+  __TEXT.__text: 0x2895c
   __TEXT.__auth_stubs: 0xa30
   __TEXT.__cstring: 0x8ddf
   __TEXT.__const: 0x1c2
-  __TEXT.__unwind_info: 0x800
+  __TEXT.__unwind_info: 0x810
   __DATA_CONST.__const: 0x1590
   __DATA_CONST.__auth_got: 0x518
   __DATA_CONST.__got: 0x58
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ sub_100000934 : 408 -> 416
~ _get_mail_conf_raw_table : 100 -> 92
~ _get_mail_conf_raw_fn_table : 100 -> 92
~ _get_mail_conf_str_table : 100 -> 92
~ _get_mail_conf_str_fn_table : 100 -> 92
~ _maps_find : 444 -> 428
~ _maps_free : 160 -> 144
~ sub_10000a7a0 -> sub_10000a768 : 1036 -> 1032
~ sub_10000f898 -> sub_10000f85c : 2184 -> 2212
~ sub_10001035c -> sub_10001033c : 228 -> 220
~ _attr_vprint0 : 1124 -> 1120
~ _attr_vprint_plain : 968 -> 960
~ _base64_encode_opt : 688 -> 672
~ _dict_cidr_open : 1720 -> 1696
~ sub_100016f00 -> sub_100016ea4 : 136 -> 120
~ sub_100017f74 -> sub_100017f08 : 380 -> 372
~ _dict_unix_open : 284 -> 292
~ _lowercase : 108 -> 100
~ sub_10001b888 -> sub_10001b814 : 1636 -> 1620
~ sub_10001bf38 -> sub_10001beb4 : 188 -> 180
~ sub_10001c58c -> sub_10001c500 : 780 -> 772
~ _msg_syslog_facility : 88 -> 104
~ _name_mask_delim_opt : 432 -> 456
~ _long_name_mask_delim_opt : 428 -> 452
~ _printable : 124 -> 120
~ _split_nameval : 412 -> 392
~ _vbuf_print : 2500 -> 2416
~ _vstring_strcpy : 164 -> 148
~ _vstring_strcat : 160 -> 144
~ sub_100026da0 -> sub_100026cc0 : 456 -> 448
~ _dict_pipe_open : 680 -> 668
~ _dict_union_open : 680 -> 668
~ _split_qnameval : 372 -> 360

```
