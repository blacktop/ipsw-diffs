## virtual

> `/usr/libexec/postfix/virtual`

```diff

-  __TEXT.__text: 0x2de9c
+  __TEXT.__text: 0x2dd70
   __TEXT.__auth_stubs: 0xaf0
   __TEXT.__cstring: 0x9e76
   __TEXT.__const: 0x1d2
-  __TEXT.__unwind_info: 0x900
+  __TEXT.__unwind_info: 0x910
   __DATA_CONST.__const: 0x1808
   __DATA_CONST.__auth_got: 0x578
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
~ sub_10000e2b4 -> sub_10000e274 : 1036 -> 1032
~ sub_100014d30 -> sub_100014cec : 2184 -> 2212
~ sub_1000157f4 -> sub_1000157cc : 228 -> 220
~ _attr_vprint0 : 1124 -> 1120
~ _base64_encode_opt : 688 -> 672
~ _dict_cidr_open : 1720 -> 1696
~ sub_10001b57c -> sub_10001b520 : 136 -> 120
~ sub_10001c5f0 -> sub_10001c584 : 380 -> 372
~ _dict_unix_open : 284 -> 292
~ _lowercase : 108 -> 100
~ sub_100020168 -> sub_1000200f4 : 1636 -> 1620
~ sub_100020818 -> sub_100020794 : 188 -> 180
~ _make_dirs : 468 -> 460
~ sub_100021040 -> sub_100020fac : 780 -> 772
~ _msg_syslog_facility : 88 -> 104
~ _name_mask_delim_opt : 432 -> 456
~ _long_name_mask_delim_opt : 428 -> 452
~ _printable : 124 -> 120
~ _split_nameval : 412 -> 392
~ _vbuf_print : 2500 -> 2416
~ _vstring_strcpy : 164 -> 148
~ _vstring_strcat : 160 -> 144
~ _sane_basename : 232 -> 208
~ sub_10002c1d4 -> sub_10002c0d4 : 456 -> 448
~ _dict_pipe_open : 680 -> 668
~ _dict_union_open : 680 -> 668
~ _split_qnameval : 372 -> 360

```
