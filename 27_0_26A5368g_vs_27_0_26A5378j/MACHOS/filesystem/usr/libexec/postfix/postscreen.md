## postscreen

> `/usr/libexec/postfix/postscreen`

```diff

-  __TEXT.__text: 0x30300
+  __TEXT.__text: 0x301bc
   __TEXT.__auth_stubs: 0xae0
   __TEXT.__const: 0x222
   __TEXT.__cstring: 0xb8e3
-  __TEXT.__unwind_info: 0x900
+  __TEXT.__unwind_info: 0x910
   __DATA_CONST.__const: 0x2300
   __DATA_CONST.__auth_got: 0x570
   __DATA_CONST.__got: 0x58
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ _psc_dnsbl_request : 776 -> 768
~ sub_1000025a8 -> sub_1000025a0 : 1052 -> 1040
~ sub_100003914 -> sub_100003900 : 3692 -> 3680
~ sub_1000056b0 -> sub_100005690 : 284 -> 272
~ _psc_parse_tests : 272 -> 276
~ _psc_endpt_lookup : 204 -> 220
~ _get_mail_conf_raw_table : 100 -> 92
~ _get_mail_conf_raw_fn_table : 100 -> 92
~ _get_mail_conf_str_table : 100 -> 92
~ _get_mail_conf_str_fn_table : 100 -> 92
~ _maps_find : 444 -> 428
~ _maps_free : 160 -> 144
~ sub_1000102bc -> sub_100010264 : 1036 -> 1032
~ sub_100016208 -> sub_1000161ac : 2184 -> 2212
~ sub_100016ccc -> sub_100016c8c : 228 -> 220
~ _attr_vprint0 : 1124 -> 1120
~ _base64_encode_opt : 688 -> 672
~ _dict_cidr_open : 1720 -> 1696
~ sub_10001ca54 -> sub_10001c9e0 : 136 -> 120
~ sub_10001dac8 -> sub_10001da44 : 380 -> 372
~ _dict_unix_open : 284 -> 292
~ _lowercase : 108 -> 100
~ sub_1000213dc -> sub_100021350 : 1636 -> 1620
~ sub_100021a8c -> sub_1000219f0 : 188 -> 180
~ sub_1000220e0 -> sub_10002203c : 780 -> 772
~ _msg_syslog_facility : 88 -> 104
~ _name_mask_delim_opt : 432 -> 456
~ _long_name_mask_delim_opt : 428 -> 452
~ _printable : 124 -> 120
~ _split_nameval : 412 -> 392
~ _vbuf_print : 2500 -> 2416
~ _vstring_strcpy : 164 -> 148
~ _vstring_strcat : 160 -> 144
~ _sane_basename : 232 -> 208
~ _ip_match_parse : 1124 -> 1116
~ sub_10002e638 -> sub_10002e520 : 456 -> 448
~ _dict_pipe_open : 680 -> 668
~ _dict_union_open : 680 -> 668
~ _split_qnameval : 372 -> 360

```
