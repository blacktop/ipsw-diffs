## postsuper

> `/usr/sbin/postsuper`

```diff

-  __TEXT.__text: 0x1b560
+  __TEXT.__text: 0x1b424
   __TEXT.__auth_stubs: 0x7c0
   __TEXT.__cstring: 0x6016
   __TEXT.__const: 0x122
-  __TEXT.__unwind_info: 0x608
+  __TEXT.__unwind_info: 0x610
   __DATA_CONST.__const: 0x1410
   __DATA_CONST.__auth_got: 0x3e0
   __DATA_CONST.__got: 0x48
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ sub_100001374 : 2388 -> 2380
~ sub_100001ea4 -> sub_100001e9c : 396 -> 376
~ sub_100002030 -> sub_100002014 : 368 -> 348
~ sub_1000022bc -> sub_10000228c : 116 -> 100
~ _get_mail_conf_str_table : 100 -> 92
~ _get_mail_conf_str_fn_table : 100 -> 92
~ sub_100005948 -> sub_1000058f8 : 1036 -> 1032
~ _clean_env : 288 -> 268
~ _update_env : 224 -> 212
~ _dict_cidr_open : 1720 -> 1696
~ sub_10000afec -> sub_10000af60 : 136 -> 120
~ sub_10000c060 -> sub_10000bfc4 : 380 -> 372
~ _dict_unix_open : 284 -> 292
~ _lowercase : 108 -> 100
~ sub_10000f7a8 -> sub_10000f704 : 1636 -> 1620
~ sub_10000fe58 -> sub_10000fda4 : 188 -> 180
~ _make_dirs : 468 -> 460
~ _msg_syslog_facility : 88 -> 104
~ _name_mask_delim_opt : 432 -> 456
~ _long_name_mask_delim_opt : 428 -> 452
~ _printable : 124 -> 120
~ _split_nameval : 412 -> 392
~ _vbuf_print : 2500 -> 2416
~ _vstring_strcpy : 164 -> 148
~ _vstring_strcat : 160 -> 144
~ sub_100019898 -> sub_100019788 : 456 -> 448
~ _dict_pipe_open : 680 -> 668
~ _dict_union_open : 680 -> 668
~ _split_qnameval : 372 -> 360

```
