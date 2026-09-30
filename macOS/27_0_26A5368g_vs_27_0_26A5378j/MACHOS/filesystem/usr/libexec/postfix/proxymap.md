## proxymap

> `/usr/libexec/postfix/proxymap`

```diff

-  __TEXT.__text: 0x26694
+  __TEXT.__text: 0x26590
   __TEXT.__auth_stubs: 0xa20
   __TEXT.__cstring: 0x8b76
   __TEXT.__const: 0x1c2
-  __TEXT.__unwind_info: 0x7c8
+  __TEXT.__unwind_info: 0x7d8
   __DATA_CONST.__const: 0x1700
   __DATA_CONST.__auth_got: 0x510
   __DATA_CONST.__got: 0x58
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ _dict_proxy_open : 152 -> 164
~ sub_1000012f4 -> sub_100001300 : 452 -> 448
~ _get_mail_conf_raw_table : 100 -> 92
~ _get_mail_conf_raw_fn_table : 100 -> 92
~ _get_mail_conf_str_table : 100 -> 92
~ _get_mail_conf_str_fn_table : 100 -> 92
~ _maps_find : 444 -> 428
~ _maps_free : 160 -> 144
~ sub_1000091e8 -> sub_1000091b0 : 1036 -> 1032
~ sub_10000e2e0 -> sub_10000e2a4 : 2184 -> 2212
~ sub_10000eda4 -> sub_10000ed84 : 228 -> 220
~ _attr_vprint0 : 1124 -> 1120
~ _base64_encode_opt : 688 -> 672
~ _dict_cidr_open : 1720 -> 1696
~ sub_100014b2c -> sub_100014ad8 : 136 -> 120
~ sub_100015ba0 -> sub_100015b3c : 380 -> 372
~ _dict_unix_open : 284 -> 292
~ _lowercase : 108 -> 100
~ sub_1000194b4 -> sub_100019448 : 1636 -> 1620
~ sub_100019b64 -> sub_100019ae8 : 188 -> 180
~ sub_10001a1b8 -> sub_10001a134 : 780 -> 772
~ _msg_syslog_facility : 88 -> 104
~ _name_mask_delim_opt : 432 -> 456
~ _long_name_mask_delim_opt : 428 -> 452
~ _printable : 124 -> 120
~ _split_nameval : 412 -> 392
~ _vbuf_print : 2500 -> 2416
~ _vstring_strcpy : 164 -> 148
~ _vstring_strcat : 160 -> 144
~ sub_1000249cc -> sub_1000248f4 : 456 -> 448
~ _dict_pipe_open : 680 -> 668
~ _dict_union_open : 680 -> 668
~ _split_qnameval : 372 -> 360

```
