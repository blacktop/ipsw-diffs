## postconf

> `/usr/sbin/postconf`

```diff

-  __TEXT.__text: 0x293b4
+  __TEXT.__text: 0x2923c
   __TEXT.__auth_stubs: 0xc70
   __TEXT.__cstring: 0xec91
   __TEXT.__const: 0x1c2
-  __TEXT.__unwind_info: 0x838
+  __TEXT.__unwind_info: 0x840
   __DATA_CONST.__const: 0x7fb0
   __DATA_CONST.__auth_got: 0x638
   __DATA_CONST.__got: 0x58
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ _pcf_register_builtin_parameters : 1060 -> 972
~ _pcf_set_parameters : 136 -> 120
~ _pcf_show_parameters : 304 -> 296
~ sub_100002a44 -> sub_1000029d4 : 396 -> 400
~ sub_100002bd0 -> sub_100002b64 : 596 -> 600
~ _pcf_show_master_entries : 544 -> 532
~ _pcf_show_master_fields : 668 -> 656
~ _pcf_show_master_params : 632 -> 620
~ _pcf_register_service_parameters : 360 -> 368
~ _pcf_flag_unused_master_parameters : 140 -> 124
~ _pcf_register_user_parameters : 684 -> 668
~ sub_100005140 -> sub_10000509c : 672 -> 664
~ sub_100005480 -> sub_1000053d4 : 484 -> 480
~ _xsasl_server_init : 156 -> 164
~ sub_100008940 -> sub_100008898 : 624 -> 632
~ _get_mail_conf_str_table : 100 -> 92
~ _get_mail_conf_str_fn_table : 100 -> 92
~ sub_10000df20 -> sub_10000de70 : 1036 -> 1032
~ sub_100011be8 -> sub_100011b34 : 2184 -> 2212
~ sub_1000126ac -> sub_100012614 : 228 -> 220
~ _attr_vprint0 : 1124 -> 1120
~ _base64_encode_opt : 688 -> 672
~ _dict_cidr_open : 1720 -> 1696
~ sub_1000182fc -> sub_100018230 : 136 -> 120
~ sub_100019370 -> sub_100019294 : 380 -> 372
~ _dict_unix_open : 284 -> 292
~ _lowercase : 108 -> 100
~ sub_10001c8fc -> sub_10001c818 : 1636 -> 1620
~ sub_10001cfac -> sub_10001ceb8 : 188 -> 180
~ sub_10001d600 -> sub_10001d504 : 780 -> 772
~ _msg_syslog_facility : 88 -> 104
~ _name_mask_delim_opt : 432 -> 456
~ _long_name_mask_delim_opt : 428 -> 452
~ _printable : 124 -> 120
~ _split_nameval : 412 -> 392
~ _translit : 68 -> 72
~ _vbuf_print : 2500 -> 2416
~ _vstring_strcpy : 164 -> 148
~ _vstring_strcat : 160 -> 144
~ sub_1000276c4 -> sub_100027578 : 456 -> 448
~ _dict_pipe_open : 680 -> 668
~ _dict_union_open : 680 -> 668
~ _split_qnameval : 372 -> 360

```
