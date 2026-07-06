## qmqpd

> `/usr/libexec/postfix/qmqpd`

```diff

-  __TEXT.__text: 0x2c644
+  __TEXT.__text: 0x2c4d8
   __TEXT.__auth_stubs: 0xb60
   __TEXT.__cstring: 0x9ce4
   __TEXT.__const: 0x1d2
-  __TEXT.__unwind_info: 0x8b0
+  __TEXT.__unwind_info: 0x8c0
   __DATA_CONST.__const: 0x1730
   __DATA_CONST.__auth_got: 0x5b0
   __DATA_CONST.__got: 0x58
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ sub_100000b34 : 2824 -> 2816
~ _get_mail_conf_raw_table : 100 -> 92
~ _get_mail_conf_raw_fn_table : 100 -> 92
~ _get_mail_conf_str_table : 100 -> 92
~ _get_mail_conf_str_fn_table : 100 -> 92
~ _mail_date : 640 -> 616
~ _maps_find : 444 -> 428
~ _maps_free : 160 -> 144
~ sub_10000c6d0 -> sub_10000c670 : 1036 -> 1032
~ sub_100012a00 -> sub_10001299c : 2184 -> 2212
~ sub_1000134c4 -> sub_10001347c : 228 -> 220
~ _attr_vprint0 : 1124 -> 1120
~ _base64_encode_opt : 688 -> 672
~ _clean_env : 288 -> 268
~ _update_env : 224 -> 212
~ _dict_cidr_open : 1720 -> 1696
~ sub_10001944c -> sub_1000193b0 : 136 -> 120
~ sub_10001a4c0 -> sub_10001a414 : 380 -> 372
~ _dict_unix_open : 284 -> 292
~ _lowercase : 108 -> 100
~ sub_10001e1d0 -> sub_10001e11c : 1636 -> 1620
~ sub_10001e880 -> sub_10001e7bc : 188 -> 180
~ _make_dirs : 468 -> 460
~ sub_10001f0a8 -> sub_10001efd4 : 780 -> 772
~ _msg_syslog_facility : 88 -> 104
~ _name_mask_delim_opt : 432 -> 456
~ _long_name_mask_delim_opt : 428 -> 452
~ _printable : 124 -> 120
~ _split_nameval : 412 -> 392
~ _vbuf_print : 2500 -> 2416
~ _vstring_strcpy : 164 -> 148
~ _vstring_strcat : 160 -> 144
~ _sane_basename : 232 -> 208
~ sub_10002a97c -> sub_10002a83c : 456 -> 448
~ _dict_pipe_open : 680 -> 668
~ _dict_union_open : 680 -> 668
~ _split_qnameval : 372 -> 360

```
