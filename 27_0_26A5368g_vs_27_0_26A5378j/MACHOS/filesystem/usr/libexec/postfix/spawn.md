## spawn

> `/usr/libexec/postfix/spawn`

```diff

-  __TEXT.__text: 0x27f10
+  __TEXT.__text: 0x27dcc
   __TEXT.__auth_stubs: 0xac0
   __TEXT.__cstring: 0x8fde
   __TEXT.__const: 0x1c2
-  __TEXT.__unwind_info: 0x7e0
+  __TEXT.__unwind_info: 0x7f0
   __DATA_CONST.__const: 0x14e0
   __DATA_CONST.__auth_got: 0x560
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
~ sub_1000098ac -> sub_10000986c : 1036 -> 1032
~ sub_10000ea98 -> sub_10000ea54 : 2184 -> 2212
~ sub_10000f55c -> sub_10000f534 : 228 -> 220
~ _attr_vprint0 : 1124 -> 1120
~ _base64_encode_opt : 688 -> 672
~ _clean_env : 288 -> 268
~ _update_env : 224 -> 212
~ _dict_cidr_open : 1720 -> 1696
~ sub_1000154e4 -> sub_100015468 : 136 -> 120
~ sub_100016558 -> sub_1000164cc : 380 -> 372
~ _dict_unix_open : 284 -> 292
~ _lowercase : 108 -> 100
~ sub_100019f50 -> sub_100019ebc : 1636 -> 1620
~ sub_10001a600 -> sub_10001a55c : 188 -> 180
~ sub_10001ac54 -> sub_10001aba8 : 780 -> 772
~ _msg_syslog_facility : 88 -> 104
~ _name_mask_delim_opt : 432 -> 456
~ _long_name_mask_delim_opt : 428 -> 452
~ _printable : 124 -> 120
~ _split_nameval : 412 -> 392
~ _vbuf_print : 2500 -> 2416
~ _vstring_strcpy : 164 -> 148
~ _vstring_strcat : 160 -> 144
~ _sane_basename : 232 -> 208
~ sub_100026248 -> sub_100026130 : 456 -> 448
~ _dict_pipe_open : 680 -> 668
~ _dict_union_open : 680 -> 668
~ _split_qnameval : 372 -> 360

```
