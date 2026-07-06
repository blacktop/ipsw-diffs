## cleanup

> `/usr/libexec/postfix/cleanup`

```diff

-  __TEXT.__text: 0x3edbc
+  __TEXT.__text: 0x3ec54
   __TEXT.__auth_stubs: 0xba0
   __TEXT.__cstring: 0xd742
   __TEXT.__const: 0x262
-  __TEXT.__unwind_info: 0xae0
+  __TEXT.__unwind_info: 0xaf0
   __DATA_CONST.__const: 0x2608
   __DATA_CONST.__auth_got: 0x5d0
   __DATA_CONST.__got: 0x58
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ sub_100001bb8 : 1020 -> 1028
~ sub_100002fb8 -> sub_100002fc0 : 624 -> 616
~ sub_100003228 : 624 -> 616
~ _cleanup_out_recipient : 1004 -> 996
~ sub_10000ca40 -> sub_10000ca30 : 2408 -> 2416
~ sub_10000f8dc -> sub_10000f8d4 : 412 -> 396
~ _cleanup_strerror : 104 -> 120
~ _header_opts_find : 820 -> 796
~ _mail_addr_crunch_opt : 588 -> 576
~ _get_mail_conf_raw_table : 100 -> 92
~ _get_mail_conf_raw_fn_table : 100 -> 92
~ _get_mail_conf_str_table : 100 -> 92
~ _get_mail_conf_str_fn_table : 100 -> 92
~ _mail_date : 640 -> 616
~ _maps_find : 444 -> 428
~ _maps_free : 160 -> 144
~ _mime_state_update : 4056 -> 4064
~ _mime_state_error : 92 -> 100
~ _mime_state_detail : 100 -> 92
~ sub_10001bb58 -> sub_10001badc : 1036 -> 1032
~ _tok822_scan_limit : 1276 -> 1280
~ _attr_override : 876 -> 904
~ sub_1000249b4 -> sub_100024954 : 2184 -> 2212
~ sub_100025478 -> sub_100025434 : 228 -> 220
~ _attr_vprint0 : 1124 -> 1120
~ _base64_encode_opt : 688 -> 672
~ _clean_env : 288 -> 268
~ _update_env : 224 -> 212
~ _dict_cidr_open : 1720 -> 1696
~ sub_10002b43c -> sub_10002b3a4 : 136 -> 120
~ sub_10002c4b0 -> sub_10002c408 : 380 -> 372
~ _dict_unix_open : 284 -> 292
~ _lowercase : 108 -> 100
~ sub_100030268 -> sub_1000301b8 : 1636 -> 1620
~ sub_100030918 -> sub_100030858 : 188 -> 180
~ _make_dirs : 468 -> 460
~ sub_100031140 -> sub_100031070 : 780 -> 772
~ _msg_syslog_facility : 88 -> 104
~ _name_mask_delim_opt : 432 -> 456
~ _long_name_mask_delim_opt : 428 -> 452
~ _printable : 124 -> 120
~ _split_nameval : 412 -> 392
~ _vbuf_print : 2500 -> 2416
~ _vstring_strcpy : 164 -> 148
~ _vstring_strcat : 160 -> 144
~ _sane_basename : 232 -> 208
~ sub_10003d0f4 -> sub_10003cfb8 : 456 -> 448
~ _dict_pipe_open : 680 -> 668
~ _dict_union_open : 680 -> 668
~ _split_qnameval : 372 -> 360

```
