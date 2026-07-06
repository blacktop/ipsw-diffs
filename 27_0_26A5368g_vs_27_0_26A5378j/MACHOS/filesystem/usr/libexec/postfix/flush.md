## flush

> `/usr/libexec/postfix/flush`

```diff

-  __TEXT.__text: 0x29bbc
+  __TEXT.__text: 0x29a90
   __TEXT.__auth_stubs: 0xac0
   __TEXT.__cstring: 0x928e
   __TEXT.__const: 0x1c2
-  __TEXT.__unwind_info: 0x828
+  __TEXT.__unwind_info: 0x838
   __DATA_CONST.__const: 0x1500
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
~ sub_10000b08c -> sub_10000b04c : 1036 -> 1032
~ sub_1000105f8 -> sub_1000105b4 : 2184 -> 2212
~ sub_1000110bc -> sub_100011094 : 228 -> 220
~ _attr_vprint0 : 1124 -> 1120
~ _base64_encode_opt : 688 -> 672
~ _dict_cidr_open : 1720 -> 1696
~ sub_100016e44 -> sub_100016de8 : 136 -> 120
~ sub_100017eb8 -> sub_100017e4c : 380 -> 372
~ _dict_unix_open : 284 -> 292
~ _lowercase : 108 -> 100
~ sub_10001bad0 -> sub_10001ba5c : 1636 -> 1620
~ sub_10001c180 -> sub_10001c0fc : 188 -> 180
~ _make_dirs : 468 -> 460
~ sub_10001c9a8 -> sub_10001c914 : 780 -> 772
~ _msg_syslog_facility : 88 -> 104
~ _name_mask_delim_opt : 432 -> 456
~ _long_name_mask_delim_opt : 428 -> 452
~ _printable : 124 -> 120
~ _split_nameval : 412 -> 392
~ _vbuf_print : 2500 -> 2416
~ _vstring_strcpy : 164 -> 148
~ _vstring_strcat : 160 -> 144
~ _sane_basename : 232 -> 208
~ sub_100027ef4 -> sub_100027df4 : 456 -> 448
~ _dict_pipe_open : 680 -> 668
~ _dict_union_open : 680 -> 668
~ _split_qnameval : 372 -> 360

```
