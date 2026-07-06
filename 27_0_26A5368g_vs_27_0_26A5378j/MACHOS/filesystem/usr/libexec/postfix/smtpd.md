## smtpd

> `/usr/libexec/postfix/smtpd`

```diff

-  __TEXT.__text: 0x565cc
+  __TEXT.__text: 0x56428
   __TEXT.__auth_stubs: 0x1440
   __TEXT.__cstring: 0x14c2f
   __TEXT.__const: 0x2b2
-  __TEXT.__unwind_info: 0xdf8
+  __TEXT.__unwind_info: 0xe00
   __DATA_CONST.__const: 0x4628
   __DATA_CONST.__auth_got: 0xa20
   __DATA_CONST.__got: 0x88
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ sub_100000990 : 900 -> 888
~ sub_100001688 -> sub_10000167c : 3584 -> 3580
~ sub_100007678 -> sub_100007668 : 256 -> 248
~ sub_100012b38 -> sub_100012b20 : 800 -> 792
~ _smtpd_dsn_fix : 360 -> 328
~ sub_1000179a0 -> sub_100017960 : 624 -> 632
~ _xsasl_server_init : 156 -> 164
~ sub_10001db1c -> sub_10001daec : 2408 -> 2416
~ sub_1000209b8 -> sub_100020990 : 412 -> 396
~ _cleanup_strerror : 104 -> 120
~ _header_opts_find : 820 -> 796
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
~ sub_10002f214 -> sub_10002f184 : 1036 -> 1032
~ _tok822_scan_limit : 1276 -> 1280
~ _attr_override : 876 -> 904
~ sub_10003a024 -> sub_100039fb0 : 2184 -> 2212
~ sub_10003aae8 -> sub_10003aa90 : 228 -> 220
~ _attr_vprint0 : 1124 -> 1120
~ _attr_vprint_plain : 968 -> 960
~ _base64_encode_opt : 688 -> 672
~ _clean_env : 288 -> 268
~ _update_env : 224 -> 212
~ _dict_cidr_open : 1720 -> 1696
~ sub_100041d7c -> sub_100041cc8 : 136 -> 120
~ sub_100042df0 -> sub_100042d2c : 380 -> 372
~ _dict_unix_open : 284 -> 292
~ _lowercase : 108 -> 100
~ sub_100047058 -> sub_100046f8c : 1636 -> 1620
~ sub_100047708 -> sub_10004762c : 188 -> 180
~ _make_dirs : 468 -> 460
~ sub_100047f30 -> sub_100047e44 : 780 -> 772
~ _msg_syslog_facility : 88 -> 104
~ _name_mask_delim_opt : 432 -> 456
~ _long_name_mask_delim_opt : 428 -> 452
~ _neuter : 104 -> 88
~ _printable : 124 -> 120
~ _split_nameval : 412 -> 392
~ _uppercase : 108 -> 100
~ _vbuf_print : 2500 -> 2416
~ _vstring_strcpy : 164 -> 148
~ _vstring_strcat : 160 -> 144
~ _sane_basename : 232 -> 208
~ _ip_match_parse : 1124 -> 1116
~ sub_100054904 -> sub_10005478c : 456 -> 448
~ _dict_pipe_open : 680 -> 668
~ _dict_union_open : 680 -> 668
~ _split_qnameval : 372 -> 360

```
