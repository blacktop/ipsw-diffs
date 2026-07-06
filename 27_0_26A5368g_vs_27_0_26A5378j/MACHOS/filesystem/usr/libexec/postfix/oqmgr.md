## oqmgr

> `/usr/libexec/postfix/oqmgr`

```diff

-  __TEXT.__text: 0x31404
+  __TEXT.__text: 0x312d4
   __TEXT.__auth_stubs: 0xab0
   __TEXT.__cstring: 0xad24
   __TEXT.__const: 0x1e2
-  __TEXT.__unwind_info: 0x9a8
+  __TEXT.__unwind_info: 0x9b8
   __DATA_CONST.__const: 0x18b8
   __DATA_CONST.__auth_got: 0x558
   __DATA_CONST.__got: 0x58
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ sub_100003890 : 3604 -> 3600
~ _get_mail_conf_raw_table : 100 -> 92
~ _get_mail_conf_raw_fn_table : 100 -> 92
~ _get_mail_conf_str_table : 100 -> 92
~ _get_mail_conf_str_fn_table : 100 -> 92
~ _maps_find : 444 -> 428
~ _maps_free : 160 -> 144
~ sub_1000114dc -> sub_100011498 : 1036 -> 1032
~ sub_100018650 -> sub_100018608 : 2184 -> 2212
~ sub_100019114 -> sub_1000190e8 : 228 -> 220
~ _attr_vprint0 : 1124 -> 1120
~ _base64_encode_opt : 688 -> 672
~ _dict_cidr_open : 1720 -> 1696
~ sub_10001ee9c -> sub_10001ee3c : 136 -> 120
~ sub_10001ff10 -> sub_10001fea0 : 380 -> 372
~ _dict_unix_open : 284 -> 292
~ _lowercase : 108 -> 100
~ sub_100023658 -> sub_1000235e0 : 1636 -> 1620
~ sub_100023d08 -> sub_100023c80 : 188 -> 180
~ _make_dirs : 468 -> 460
~ sub_100024530 -> sub_100024498 : 780 -> 772
~ _msg_syslog_facility : 88 -> 104
~ _name_mask_delim_opt : 432 -> 456
~ _long_name_mask_delim_opt : 428 -> 452
~ _printable : 124 -> 120
~ _split_nameval : 412 -> 392
~ _vbuf_print : 2500 -> 2416
~ _vstring_strcpy : 164 -> 148
~ _vstring_strcat : 160 -> 144
~ _sane_basename : 232 -> 208
~ sub_10002f73c -> sub_10002f638 : 456 -> 448
~ _dict_pipe_open : 680 -> 668
~ _dict_union_open : 680 -> 668
~ _split_qnameval : 372 -> 360

```
