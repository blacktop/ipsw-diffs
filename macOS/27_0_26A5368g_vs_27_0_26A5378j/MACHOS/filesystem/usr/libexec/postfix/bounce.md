## bounce

> `/usr/libexec/postfix/bounce`

```diff

-  __TEXT.__text: 0x30150
+  __TEXT.__text: 0x3002c
   __TEXT.__auth_stubs: 0xac0
   __TEXT.__cstring: 0xa9a0
   __TEXT.__const: 0x1e2
-  __TEXT.__unwind_info: 0x958
+  __TEXT.__unwind_info: 0x970
   __DATA_CONST.__const: 0x19d8
   __DATA_CONST.__auth_got: 0x560
   __DATA_CONST.__got: 0x58
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ _bounce_template_expand : 252 -> 244
~ sub_1000049d0 -> sub_1000049c8 : 588 -> 624
~ _get_mail_conf_raw_table : 100 -> 92
~ _get_mail_conf_raw_fn_table : 100 -> 92
~ _get_mail_conf_str_table : 100 -> 92
~ _get_mail_conf_str_fn_table : 100 -> 92
~ _mail_date : 640 -> 616
~ _maps_find : 444 -> 428
~ _maps_free : 160 -> 144
~ sub_10001018c -> sub_100010150 : 1036 -> 1032
~ sub_100016ee8 -> sub_100016ea8 : 2184 -> 2212
~ sub_1000179ac -> sub_100017988 : 228 -> 220
~ _attr_vprint0 : 1124 -> 1120
~ _base64_encode_opt : 688 -> 672
~ _dict_cidr_open : 1720 -> 1696
~ sub_10001d734 -> sub_10001d6dc : 136 -> 120
~ sub_10001e7a8 -> sub_10001e740 : 380 -> 372
~ _dict_unix_open : 284 -> 292
~ _lowercase : 108 -> 100
~ sub_100022414 -> sub_1000223a4 : 1636 -> 1620
~ sub_100022ac4 -> sub_100022a44 : 188 -> 180
~ _make_dirs : 468 -> 460
~ sub_1000232ec -> sub_10002325c : 780 -> 772
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
~ sub_10002e488 -> sub_10002e390 : 456 -> 448
~ _dict_pipe_open : 680 -> 668
~ _dict_union_open : 680 -> 668
~ _split_qnameval : 372 -> 360

```
