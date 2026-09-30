## trivial-rewrite

> `/usr/libexec/postfix/trivial-rewrite`

```diff

-  __TEXT.__text: 0x2aab0
+  __TEXT.__text: 0x2a9a8
   __TEXT.__auth_stubs: 0xa20
   __TEXT.__cstring: 0x93ba
   __TEXT.__const: 0x1c2
-  __TEXT.__unwind_info: 0x848
+  __TEXT.__unwind_info: 0x858
   __DATA_CONST.__const: 0x18c8
   __DATA_CONST.__auth_got: 0x510
   __DATA_CONST.__got: 0x58
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ _get_mail_conf_raw_table : 100 -> 92
~ _get_mail_conf_raw_fn_table : 100 -> 92
~ _get_mail_conf_str_table : 100 -> 92
~ _get_mail_conf_str_fn_table : 100 -> 92
~ _maps_find : 444 -> 428
~ _maps_free : 160 -> 144
~ sub_10000ba14 -> sub_10000b9d4 : 1036 -> 1032
~ _tok822_scan_limit : 1276 -> 1280
~ sub_1000126fc -> sub_1000126bc : 2184 -> 2212
~ sub_1000131c0 -> sub_10001319c : 228 -> 220
~ _attr_vprint0 : 1124 -> 1120
~ _base64_encode_opt : 688 -> 672
~ _dict_cidr_open : 1720 -> 1696
~ sub_100018f48 -> sub_100018ef0 : 136 -> 120
~ sub_100019fbc -> sub_100019f54 : 380 -> 372
~ _dict_unix_open : 284 -> 292
~ _lowercase : 108 -> 100
~ sub_10001d8d0 -> sub_10001d860 : 1636 -> 1620
~ sub_10001df80 -> sub_10001df00 : 188 -> 180
~ sub_10001e5d4 -> sub_10001e54c : 780 -> 772
~ _msg_syslog_facility : 88 -> 104
~ _name_mask_delim_opt : 432 -> 456
~ _long_name_mask_delim_opt : 428 -> 452
~ _printable : 124 -> 120
~ _split_nameval : 412 -> 392
~ _vbuf_print : 2500 -> 2416
~ _vstring_strcpy : 164 -> 148
~ _vstring_strcat : 160 -> 144
~ sub_100028de8 -> sub_100028d0c : 456 -> 448
~ _dict_pipe_open : 680 -> 668
~ _dict_union_open : 680 -> 668
~ _split_qnameval : 372 -> 360

```
