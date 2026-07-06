## scache

> `/usr/libexec/postfix/scache`

```diff

-  __TEXT.__text: 0x27edc
+  __TEXT.__text: 0x27dd0
   __TEXT.__auth_stubs: 0xa40
   __TEXT.__cstring: 0x8e8c
   __TEXT.__const: 0x1c2
-  __TEXT.__unwind_info: 0x800
+  __TEXT.__unwind_info: 0x810
   __DATA_CONST.__const: 0x1520
   __DATA_CONST.__auth_got: 0x520
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
~ sub_10000a0a8 -> sub_10000a068 : 1036 -> 1032
~ sub_10000f9e0 -> sub_10000f99c : 2184 -> 2212
~ sub_1000104a4 -> sub_10001047c : 228 -> 220
~ _attr_vprint0 : 1124 -> 1120
~ _base64_encode_opt : 688 -> 672
~ _dict_cidr_open : 1720 -> 1696
~ sub_10001622c -> sub_1000161d0 : 136 -> 120
~ sub_1000172a0 -> sub_100017234 : 380 -> 372
~ _dict_unix_open : 284 -> 292
~ _lowercase : 108 -> 100
~ sub_10001abb4 -> sub_10001ab40 : 1636 -> 1620
~ sub_10001b264 -> sub_10001b1e0 : 188 -> 180
~ sub_10001b8b8 -> sub_10001b82c : 780 -> 772
~ _msg_syslog_facility : 88 -> 104
~ _name_mask_delim_opt : 432 -> 456
~ _long_name_mask_delim_opt : 428 -> 452
~ _printable : 124 -> 120
~ _split_nameval : 412 -> 392
~ _vbuf_print : 2500 -> 2416
~ _vstring_strcpy : 164 -> 148
~ _vstring_strcat : 160 -> 144
~ sub_100026214 -> sub_100026134 : 456 -> 448
~ _dict_pipe_open : 680 -> 668
~ _dict_union_open : 680 -> 668
~ _split_qnameval : 372 -> 360

```
