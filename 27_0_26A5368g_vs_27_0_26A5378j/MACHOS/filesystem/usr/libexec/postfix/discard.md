## discard

> `/usr/libexec/postfix/discard`

```diff

-  __TEXT.__text: 0x2a234
+  __TEXT.__text: 0x2a108
   __TEXT.__auth_stubs: 0xa50
   __TEXT.__cstring: 0x9353
   __TEXT.__const: 0x1d2
-  __TEXT.__unwind_info: 0x870
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
~ sub_10000b0a4 -> sub_10000b064 : 1036 -> 1032
~ sub_1000113e8 -> sub_1000113a4 : 2184 -> 2212
~ sub_100011eac -> sub_100011e84 : 228 -> 220
~ _attr_vprint0 : 1124 -> 1120
~ _base64_encode_opt : 688 -> 672
~ _dict_cidr_open : 1720 -> 1696
~ sub_100017c34 -> sub_100017bd8 : 136 -> 120
~ sub_100018ca8 -> sub_100018c3c : 380 -> 372
~ _dict_unix_open : 284 -> 292
~ _lowercase : 108 -> 100
~ sub_10001c778 -> sub_10001c704 : 1636 -> 1620
~ sub_10001ce28 -> sub_10001cda4 : 188 -> 180
~ _make_dirs : 468 -> 460
~ sub_10001d650 -> sub_10001d5bc : 780 -> 772
~ _msg_syslog_facility : 88 -> 104
~ _name_mask_delim_opt : 432 -> 456
~ _long_name_mask_delim_opt : 428 -> 452
~ _printable : 124 -> 120
~ _split_nameval : 412 -> 392
~ _vbuf_print : 2500 -> 2416
~ _vstring_strcpy : 164 -> 148
~ _vstring_strcat : 160 -> 144
~ _sane_basename : 232 -> 208
~ sub_10002856c -> sub_10002846c : 456 -> 448
~ _dict_pipe_open : 680 -> 668
~ _dict_union_open : 680 -> 668
~ _split_qnameval : 372 -> 360

```
