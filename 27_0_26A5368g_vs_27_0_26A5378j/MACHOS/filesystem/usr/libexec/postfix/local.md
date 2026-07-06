## local

> `/usr/libexec/postfix/local`

```diff

-  __TEXT.__text: 0x36c8c
+  __TEXT.__text: 0x36afc
   __TEXT.__auth_stubs: 0xbd0
   __TEXT.__cstring: 0xb5f4
   __TEXT.__const: 0x1f2
-  __TEXT.__unwind_info: 0xa10
+  __TEXT.__unwind_info: 0xa20
   __DATA_CONST.__const: 0x1c98
   __DATA_CONST.__auth_got: 0x5e8
   __DATA_CONST.__got: 0x58
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ _deliver_alias : 2148 -> 2132
~ _deliver_resolve_tree : 964 -> 952
~ _header_opts_find : 820 -> 796
~ _get_mail_conf_raw_table : 100 -> 92
~ _get_mail_conf_raw_fn_table : 100 -> 92
~ _get_mail_conf_str_table : 100 -> 92
~ _get_mail_conf_str_fn_table : 100 -> 92
~ _mail_date : 640 -> 616
~ _maps_find : 444 -> 428
~ _maps_free : 160 -> 144
~ sub_1000137a0 -> sub_100013714 : 1036 -> 1032
~ _tok822_scan_limit : 1276 -> 1280
~ sub_10001d4b0 -> sub_10001d424 : 2184 -> 2212
~ sub_10001df74 -> sub_10001df04 : 228 -> 220
~ _attr_vprint0 : 1124 -> 1120
~ _base64_encode_opt : 688 -> 672
~ _clean_env : 288 -> 268
~ _update_env : 224 -> 212
~ _dict_cidr_open : 1720 -> 1696
~ sub_100023efc -> sub_100023e38 : 136 -> 120
~ sub_100024f70 -> sub_100024e9c : 380 -> 372
~ _dict_unix_open : 284 -> 292
~ _lowercase : 108 -> 100
~ sub_100028c44 -> sub_100028b68 : 1636 -> 1620
~ sub_1000292f4 -> sub_100029208 : 188 -> 180
~ _make_dirs : 468 -> 460
~ sub_100029b1c -> sub_100029a20 : 780 -> 772
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
~ sub_100035014 -> sub_100034eb0 : 456 -> 448
~ _dict_pipe_open : 680 -> 668
~ _dict_union_open : 680 -> 668
~ _split_qnameval : 372 -> 360

```
