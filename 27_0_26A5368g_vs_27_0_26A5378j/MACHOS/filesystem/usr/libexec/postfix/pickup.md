## pickup

> `/usr/libexec/postfix/pickup`

```diff

-  __TEXT.__text: 0x29e6c
+  __TEXT.__text: 0x29d38
   __TEXT.__auth_stubs: 0xad0
   __TEXT.__cstring: 0x9567
   __TEXT.__const: 0x1d2
-  __TEXT.__unwind_info: 0x860
+  __TEXT.__unwind_info: 0x870
   __DATA_CONST.__const: 0x1740
   __DATA_CONST.__auth_got: 0x568
   __DATA_CONST.__got: 0x58
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ _cleanup_strerror : 104 -> 120
~ _get_mail_conf_raw_table : 100 -> 92
~ _get_mail_conf_raw_fn_table : 100 -> 92
~ _get_mail_conf_str_table : 100 -> 92
~ _get_mail_conf_str_fn_table : 100 -> 92
~ _mail_date : 640 -> 616
~ _maps_find : 444 -> 428
~ _maps_free : 160 -> 144
~ sub_10000b0e4 -> sub_10000b09c : 1036 -> 1032
~ sub_100010fc0 -> sub_100010f74 : 2184 -> 2212
~ sub_100011a84 -> sub_100011a54 : 228 -> 220
~ _attr_vprint0 : 1124 -> 1120
~ _base64_encode_opt : 688 -> 672
~ _dict_cidr_open : 1720 -> 1696
~ sub_10001780c -> sub_1000177a8 : 136 -> 120
~ sub_100018880 -> sub_10001880c : 380 -> 372
~ _dict_unix_open : 284 -> 292
~ _lowercase : 108 -> 100
~ sub_10001bfc8 -> sub_10001bf4c : 1636 -> 1620
~ sub_10001c678 -> sub_10001c5ec : 188 -> 180
~ _make_dirs : 468 -> 460
~ sub_10001cea0 -> sub_10001ce04 : 780 -> 772
~ _msg_syslog_facility : 88 -> 104
~ _name_mask_delim_opt : 432 -> 456
~ _long_name_mask_delim_opt : 428 -> 452
~ _printable : 124 -> 120
~ _split_nameval : 412 -> 392
~ _vbuf_print : 2500 -> 2416
~ _vstring_strcpy : 164 -> 148
~ _vstring_strcat : 160 -> 144
~ _sane_basename : 232 -> 208
~ sub_1000281a4 -> sub_10002809c : 456 -> 448
~ _dict_pipe_open : 680 -> 668
~ _dict_union_open : 680 -> 668
~ _split_qnameval : 372 -> 360

```
