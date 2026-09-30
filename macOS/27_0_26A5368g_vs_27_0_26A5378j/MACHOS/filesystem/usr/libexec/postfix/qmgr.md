## qmgr

> `/usr/libexec/postfix/qmgr`

```diff

-  __TEXT.__text: 0x327d8
+  __TEXT.__text: 0x326a8
   __TEXT.__auth_stubs: 0xab0
   __TEXT.__cstring: 0xb1fc
   __TEXT.__const: 0x1e2
-  __TEXT.__unwind_info: 0x9d0
+  __TEXT.__unwind_info: 0x9e0
   __DATA_CONST.__const: 0x19b8
   __DATA_CONST.__auth_got: 0x558
   __DATA_CONST.__got: 0x58
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ sub_100003b60 : 3800 -> 3796
~ _get_mail_conf_raw_table : 100 -> 92
~ _get_mail_conf_raw_fn_table : 100 -> 92
~ _get_mail_conf_str_table : 100 -> 92
~ _get_mail_conf_str_fn_table : 100 -> 92
~ _maps_find : 444 -> 428
~ _maps_free : 160 -> 144
~ sub_1000127c4 -> sub_100012780 : 1036 -> 1032
~ sub_100019938 -> sub_1000198f0 : 2184 -> 2212
~ sub_10001a3fc -> sub_10001a3d0 : 228 -> 220
~ _attr_vprint0 : 1124 -> 1120
~ _base64_encode_opt : 688 -> 672
~ _dict_cidr_open : 1720 -> 1696
~ sub_100020184 -> sub_100020124 : 136 -> 120
~ sub_1000211f8 -> sub_100021188 : 380 -> 372
~ _dict_unix_open : 284 -> 292
~ _lowercase : 108 -> 100
~ sub_100024940 -> sub_1000248c8 : 1636 -> 1620
~ sub_100024ff0 -> sub_100024f68 : 188 -> 180
~ _make_dirs : 468 -> 460
~ sub_100025818 -> sub_100025780 : 780 -> 772
~ _msg_syslog_facility : 88 -> 104
~ _name_mask_delim_opt : 432 -> 456
~ _long_name_mask_delim_opt : 428 -> 452
~ _printable : 124 -> 120
~ _split_nameval : 412 -> 392
~ _vbuf_print : 2500 -> 2416
~ _vstring_strcpy : 164 -> 148
~ _vstring_strcat : 160 -> 144
~ _sane_basename : 232 -> 208
~ sub_100030b10 -> sub_100030a0c : 456 -> 448
~ _dict_pipe_open : 680 -> 668
~ _dict_union_open : 680 -> 668
~ _split_qnameval : 372 -> 360

```
