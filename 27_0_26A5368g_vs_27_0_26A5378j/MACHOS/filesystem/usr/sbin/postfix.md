## postfix

> `/usr/sbin/postfix`

```diff

-  __TEXT.__text: 0x186e0
+  __TEXT.__text: 0x185ec
   __TEXT.__auth_stubs: 0x6f0
   __TEXT.__cstring: 0x5a48
   __TEXT.__const: 0x122
-  __TEXT.__unwind_info: 0x590
+  __TEXT.__unwind_info: 0x5a0
   __DATA_CONST.__const: 0x1510
   __DATA_CONST.__auth_got: 0x378
   __DATA_CONST.__got: 0x48
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ _get_mail_conf_str_table : 100 -> 92
~ _get_mail_conf_str_fn_table : 100 -> 92
~ sub_100003768 -> sub_100003758 : 1036 -> 1032
~ _clean_env : 288 -> 268
~ _update_env : 224 -> 212
~ _dict_cidr_open : 1720 -> 1696
~ sub_100008998 -> sub_10000894c : 136 -> 120
~ sub_100009a0c -> sub_1000099b0 : 380 -> 372
~ _dict_unix_open : 284 -> 292
~ _lowercase : 108 -> 100
~ sub_10000cf98 -> sub_10000cf34 : 1636 -> 1620
~ sub_10000d648 -> sub_10000d5d4 : 188 -> 180
~ _msg_syslog_facility : 88 -> 104
~ _name_mask_delim_opt : 432 -> 456
~ _long_name_mask_delim_opt : 428 -> 452
~ _printable : 124 -> 120
~ _split_nameval : 412 -> 392
~ _vbuf_print : 2500 -> 2416
~ _vstring_strcpy : 164 -> 148
~ _vstring_strcat : 160 -> 144
~ sub_100016a18 -> sub_100016950 : 456 -> 448
~ _dict_pipe_open : 680 -> 668
~ _dict_union_open : 680 -> 668
~ _split_qnameval : 372 -> 360

```
