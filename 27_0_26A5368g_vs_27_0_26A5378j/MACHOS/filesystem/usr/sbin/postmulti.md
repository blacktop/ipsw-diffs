## postmulti

> `/usr/sbin/postmulti`

```diff

-  __TEXT.__text: 0x1a810
+  __TEXT.__text: 0x1a700
   __TEXT.__auth_stubs: 0x7a0
   __TEXT.__cstring: 0x6265
   __TEXT.__const: 0x122
-  __TEXT.__unwind_info: 0x5e8
+  __TEXT.__unwind_info: 0x5f8
   __DATA_CONST.__const: 0x14e0
   __DATA_CONST.__auth_got: 0x3d0
   __DATA_CONST.__got: 0x48
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ sub_1000011e4 : 1032 -> 1004
~ _get_mail_conf_str_table : 100 -> 92
~ _get_mail_conf_str_fn_table : 100 -> 92
~ sub_100005128 -> sub_1000050fc : 1036 -> 1032
~ _clean_env : 288 -> 268
~ _update_env : 224 -> 212
~ _dict_cidr_open : 1720 -> 1696
~ sub_10000a358 -> sub_10000a2f0 : 136 -> 120
~ sub_10000b3cc -> sub_10000b354 : 380 -> 372
~ _dict_unix_open : 284 -> 292
~ _lowercase : 108 -> 100
~ sub_10000ea50 -> sub_10000e9d0 : 1636 -> 1620
~ sub_10000f100 -> sub_10000f070 : 188 -> 180
~ _msg_syslog_facility : 88 -> 104
~ _name_mask_delim_opt : 432 -> 456
~ _long_name_mask_delim_opt : 428 -> 452
~ _printable : 124 -> 120
~ _split_nameval : 412 -> 392
~ _vbuf_print : 2500 -> 2416
~ _vstring_strcpy : 164 -> 148
~ _vstring_strcat : 160 -> 144
~ sub_100018b48 -> sub_100018a64 : 456 -> 448
~ _dict_pipe_open : 680 -> 668
~ _dict_union_open : 680 -> 668
~ _split_qnameval : 372 -> 360

```
