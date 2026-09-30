## error

> `/usr/libexec/postfix/error`

```diff

-  __TEXT.__text: 0x2a0b8
+  __TEXT.__text: 0x29f8c
   __TEXT.__auth_stubs: 0xa50
   __TEXT.__cstring: 0x9320
   __TEXT.__const: 0x1d2
-  __TEXT.__unwind_info: 0x868
+  __TEXT.__unwind_info: 0x888
   __DATA_CONST.__const: 0x14a0
   __DATA_CONST.__auth_got: 0x528
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
~ sub_10000b168 -> sub_10000b128 : 1036 -> 1032
~ sub_10001126c -> sub_100011228 : 2184 -> 2212
~ sub_100011d30 -> sub_100011d08 : 228 -> 220
~ _attr_vprint0 : 1124 -> 1120
~ _base64_encode_opt : 688 -> 672
~ _dict_cidr_open : 1720 -> 1696
~ sub_100017ab8 -> sub_100017a5c : 136 -> 120
~ sub_100018b2c -> sub_100018ac0 : 380 -> 372
~ _dict_unix_open : 284 -> 292
~ _lowercase : 108 -> 100
~ sub_10001c5fc -> sub_10001c588 : 1636 -> 1620
~ sub_10001ccac -> sub_10001cc28 : 188 -> 180
~ _make_dirs : 468 -> 460
~ sub_10001d4d4 -> sub_10001d440 : 780 -> 772
~ _msg_syslog_facility : 88 -> 104
~ _name_mask_delim_opt : 432 -> 456
~ _long_name_mask_delim_opt : 428 -> 452
~ _printable : 124 -> 120
~ _split_nameval : 412 -> 392
~ _vbuf_print : 2500 -> 2416
~ _vstring_strcpy : 164 -> 148
~ _vstring_strcat : 160 -> 144
~ _sane_basename : 232 -> 208
~ sub_1000283f0 -> sub_1000282f0 : 456 -> 448
~ _dict_pipe_open : 680 -> 668
~ _dict_union_open : 680 -> 668
~ _split_qnameval : 372 -> 360

```
