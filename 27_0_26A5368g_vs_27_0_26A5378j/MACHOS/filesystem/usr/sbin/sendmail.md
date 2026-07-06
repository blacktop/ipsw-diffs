## sendmail

> `/usr/sbin/sendmail`

```diff

-  __TEXT.__text: 0x23e38
+  __TEXT.__text: 0x23d08
   __TEXT.__auth_stubs: 0x8a0
   __TEXT.__cstring: 0x76f3
   __TEXT.__const: 0x162
-  __TEXT.__unwind_info: 0x768
+  __TEXT.__unwind_info: 0x770
   __DATA_CONST.__const: 0x16a0
   __DATA_CONST.__auth_got: 0x450
   __DATA_CONST.__got: 0x48
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ sub_1000019fc : 2572 -> 2564
~ _cleanup_strerror : 104 -> 120
~ _header_opts_find : 820 -> 796
~ _get_mail_conf_str_table : 100 -> 92
~ _get_mail_conf_str_fn_table : 100 -> 92
~ _mime_state_update : 4056 -> 4064
~ _mime_state_error : 92 -> 100
~ _mime_state_detail : 100 -> 92
~ sub_100008bd4 -> sub_100008bbc : 1036 -> 1032
~ _tok822_scan_limit : 1276 -> 1280
~ _base64_encode_opt : 688 -> 672
~ _clean_env : 288 -> 268
~ _update_env : 224 -> 212
~ _dict_cidr_open : 1720 -> 1696
~ sub_100011b74 -> sub_100011b14 : 136 -> 120
~ sub_100012be8 -> sub_100012b78 : 380 -> 372
~ _dict_unix_open : 284 -> 292
~ _lowercase : 108 -> 100
~ sub_1000167d0 -> sub_100016758 : 1636 -> 1620
~ sub_100016e80 -> sub_100016df8 : 188 -> 180
~ _make_dirs : 468 -> 460
~ sub_1000176a8 -> sub_100017610 : 780 -> 772
~ _msg_syslog_facility : 88 -> 104
~ _name_mask_delim_opt : 432 -> 456
~ _long_name_mask_delim_opt : 428 -> 452
~ _printable : 124 -> 120
~ _split_nameval : 412 -> 392
~ _vbuf_print : 2500 -> 2416
~ _vstring_strcpy : 164 -> 148
~ _vstring_strcat : 160 -> 144
~ _sane_basename : 232 -> 208
~ sub_10002215c -> sub_100022058 : 456 -> 448
~ _dict_pipe_open : 680 -> 668
~ _dict_union_open : 680 -> 668
~ _split_qnameval : 372 -> 360

```
