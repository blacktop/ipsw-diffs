## master

> `/usr/libexec/postfix/master`

```diff

-  __TEXT.__text: 0x1e6e8
+  __TEXT.__text: 0x1e5b4
   __TEXT.__auth_stubs: 0x8e0
   __TEXT.__cstring: 0x6f36
   __TEXT.__const: 0x182
-  __TEXT.__unwind_info: 0x680
+  __TEXT.__unwind_info: 0x690
   __DATA_CONST.__const: 0x1568
   __DATA_CONST.__auth_got: 0x470
   __DATA_CONST.__got: 0x48
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ _print_master_ent : 464 -> 456
~ _master_str_watch : 268 -> 252
~ _master_int_watch : 256 -> 240
~ _get_mail_conf_str_table : 100 -> 92
~ _get_mail_conf_str_fn_table : 100 -> 92
~ sub_100006a24 -> sub_1000069ec : 1036 -> 1032
~ _clean_env : 288 -> 268
~ _update_env : 224 -> 212
~ _dict_cidr_open : 1720 -> 1696
~ sub_10000c650 -> sub_10000c5dc : 136 -> 120
~ sub_10000d6c4 -> sub_10000d640 : 380 -> 372
~ _dict_unix_open : 284 -> 292
~ _lowercase : 108 -> 100
~ sub_100011638 -> sub_1000115ac : 1636 -> 1620
~ sub_100011ce8 -> sub_100011c4c : 188 -> 180
~ _msg_syslog_facility : 88 -> 104
~ _name_mask_delim_opt : 432 -> 456
~ _long_name_mask_delim_opt : 428 -> 452
~ _printable : 124 -> 120
~ _split_nameval : 412 -> 392
~ _vbuf_print : 2500 -> 2416
~ _vstring_strcpy : 164 -> 148
~ _vstring_strcat : 160 -> 144
~ _sane_basename : 232 -> 208
~ sub_10001ca20 -> sub_10001c918 : 456 -> 448
~ _dict_pipe_open : 680 -> 668
~ _dict_union_open : 680 -> 668
~ _split_qnameval : 372 -> 360

```
