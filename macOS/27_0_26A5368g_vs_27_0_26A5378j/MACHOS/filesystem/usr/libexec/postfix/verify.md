## verify

> `/usr/libexec/postfix/verify`

```diff

-  __TEXT.__text: 0x2ab4c
+  __TEXT.__text: 0x2aa14
   __TEXT.__auth_stubs: 0xab0
   __TEXT.__cstring: 0x96a1
   __TEXT.__const: 0x1d2
-  __TEXT.__unwind_info: 0x870
+  __TEXT.__unwind_info: 0x890
   __DATA_CONST.__const: 0x1770
   __DATA_CONST.__auth_got: 0x558
   __DATA_CONST.__got: 0x58
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ _get_mail_conf_raw_table : 100 -> 92
~ _get_mail_conf_raw_fn_table : 100 -> 92
~ _get_mail_conf_str_table : 100 -> 92
~ _get_mail_conf_str_fn_table : 100 -> 92
~ _mail_date : 640 -> 616
~ _maps_find : 444 -> 428
~ _maps_free : 160 -> 144
~ sub_10000a41c -> sub_10000a3c4 : 1036 -> 1032
~ sub_100011898 -> sub_10001183c : 2184 -> 2212
~ sub_10001235c -> sub_10001231c : 228 -> 220
~ _attr_vprint0 : 1124 -> 1120
~ _base64_encode_opt : 688 -> 672
~ _dict_cidr_open : 1720 -> 1696
~ sub_1000180e4 -> sub_100018070 : 136 -> 120
~ sub_100019158 -> sub_1000190d4 : 380 -> 372
~ _dict_unix_open : 284 -> 292
~ _lowercase : 108 -> 100
~ sub_10001ca6c -> sub_10001c9e0 : 1636 -> 1620
~ sub_10001d11c -> sub_10001d080 : 188 -> 180
~ sub_10001d770 -> sub_10001d6cc : 780 -> 772
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
~ sub_100028e84 -> sub_100028d78 : 456 -> 448
~ _dict_pipe_open : 680 -> 668
~ _dict_union_open : 680 -> 668
~ _split_qnameval : 372 -> 360

```
