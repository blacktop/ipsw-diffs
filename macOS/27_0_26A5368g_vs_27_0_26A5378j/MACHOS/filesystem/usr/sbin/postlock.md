## postlock

> `/usr/sbin/postlock`

```diff

-  __TEXT.__text: 0x19910
+  __TEXT.__text: 0x19804
   __TEXT.__auth_stubs: 0x720
   __TEXT.__cstring: 0x5969
   __TEXT.__const: 0x122
-  __TEXT.__unwind_info: 0x5c8
+  __TEXT.__unwind_info: 0x5d8
   __DATA_CONST.__const: 0x1450
   __DATA_CONST.__auth_got: 0x390
   __DATA_CONST.__got: 0x48
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ _get_mail_conf_str_table : 100 -> 92
~ _get_mail_conf_str_fn_table : 100 -> 92
~ sub_10000451c -> sub_10000450c : 1036 -> 1032
~ _clean_env : 288 -> 268
~ _update_env : 224 -> 212
~ _dict_cidr_open : 1720 -> 1696
~ sub_1000094c4 -> sub_100009478 : 136 -> 120
~ sub_10000a538 -> sub_10000a4dc : 380 -> 372
~ _dict_unix_open : 284 -> 292
~ _lowercase : 108 -> 100
~ sub_10000dac4 -> sub_10000da60 : 1636 -> 1620
~ sub_10000e174 -> sub_10000e100 : 188 -> 180
~ _msg_syslog_facility : 88 -> 104
~ _name_mask_delim_opt : 432 -> 456
~ _long_name_mask_delim_opt : 428 -> 452
~ _printable : 124 -> 120
~ _split_nameval : 412 -> 392
~ _vbuf_print : 2500 -> 2416
~ _vstring_strcpy : 164 -> 148
~ _vstring_strcat : 160 -> 144
~ _sane_basename : 232 -> 208
~ sub_100017c34 -> sub_100017b54 : 456 -> 448
~ _dict_pipe_open : 680 -> 668
~ _dict_union_open : 680 -> 668
~ _split_qnameval : 372 -> 360

```
