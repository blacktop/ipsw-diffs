## pipe

> `/usr/libexec/postfix/pipe`

```diff

-  __TEXT.__text: 0x2ef0c
+  __TEXT.__text: 0x2edb4
   __TEXT.__auth_stubs: 0xb50
   __TEXT.__cstring: 0xa371
   __TEXT.__const: 0x1d2
-  __TEXT.__unwind_info: 0x920
+  __TEXT.__unwind_info: 0x930
   __DATA_CONST.__const: 0x17b8
   __DATA_CONST.__auth_got: 0x5a8
   __DATA_CONST.__got: 0x58
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ sub_100001bd0 : 176 -> 184
~ _header_opts_find : 820 -> 796
~ _get_mail_conf_raw_table : 100 -> 92
~ _get_mail_conf_raw_fn_table : 100 -> 92
~ _get_mail_conf_str_table : 100 -> 92
~ _get_mail_conf_str_fn_table : 100 -> 92
~ _maps_find : 444 -> 428
~ _maps_free : 160 -> 144
~ sub_10000dc30 -> sub_10000dbe0 : 1036 -> 1032
~ sub_100015600 -> sub_1000155ac : 2184 -> 2212
~ sub_1000160c4 -> sub_10001608c : 228 -> 220
~ _attr_vprint0 : 1124 -> 1120
~ _base64_encode_opt : 688 -> 672
~ _clean_env : 288 -> 268
~ _update_env : 224 -> 212
~ _dict_cidr_open : 1720 -> 1696
~ sub_10001c04c -> sub_10001bfc0 : 136 -> 120
~ sub_10001d0c0 -> sub_10001d024 : 380 -> 372
~ _dict_unix_open : 284 -> 292
~ _lowercase : 108 -> 100
~ sub_100020d1c -> sub_100020c78 : 1636 -> 1620
~ sub_1000213cc -> sub_100021318 : 188 -> 180
~ _make_dirs : 468 -> 460
~ sub_100021bf4 -> sub_100021b30 : 780 -> 772
~ _msg_syslog_facility : 88 -> 104
~ _name_mask_delim_opt : 432 -> 456
~ _long_name_mask_delim_opt : 428 -> 452
~ _printable : 124 -> 120
~ _split_nameval : 412 -> 392
~ _translit : 68 -> 72
~ _vbuf_print : 2500 -> 2416
~ _vstring_strcpy : 164 -> 148
~ _vstring_strcat : 160 -> 144
~ _sane_basename : 232 -> 208
~ sub_10002d294 -> sub_10002d168 : 456 -> 448
~ _dict_pipe_open : 680 -> 668
~ _dict_union_open : 680 -> 668
~ _split_qnameval : 372 -> 360

```
