## tlsmgr

> `/usr/libexec/postfix/tlsmgr`

```diff

-  __TEXT.__text: 0x2a224
+  __TEXT.__text: 0x2a11c
   __TEXT.__auth_stubs: 0xc50
   __TEXT.__cstring: 0xa038
   __TEXT.__const: 0x1c2
-  __TEXT.__unwind_info: 0x868
+  __TEXT.__unwind_info: 0x878
   __DATA_CONST.__const: 0x1e30
   __DATA_CONST.__auth_got: 0x628
   __DATA_CONST.__got: 0x60
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ sub_1000009b8 : 1808 -> 1852
~ sub_1000010c8 -> sub_1000010f4 : 708 -> 692
~ sub_10000138c -> sub_1000013a8 : 216 -> 208
~ sub_100004430 -> sub_100004444 : 624 -> 632
~ _get_mail_conf_raw_table : 100 -> 92
~ _get_mail_conf_raw_fn_table : 100 -> 92
~ _get_mail_conf_str_table : 100 -> 92
~ _get_mail_conf_str_fn_table : 100 -> 92
~ _maps_find : 444 -> 428
~ _maps_free : 160 -> 144
~ sub_10000c644 -> sub_10000c620 : 1036 -> 1032
~ sub_1000119a4 -> sub_10001197c : 2184 -> 2212
~ sub_100012468 -> sub_10001245c : 228 -> 220
~ _attr_vprint0 : 1124 -> 1120
~ _base64_encode_opt : 688 -> 672
~ _dict_cidr_open : 1720 -> 1696
~ sub_1000181f0 -> sub_1000181b0 : 136 -> 120
~ sub_100019264 -> sub_100019214 : 380 -> 372
~ _dict_unix_open : 284 -> 292
~ _lowercase : 108 -> 100
~ sub_10001cdac -> sub_10001cd54 : 1636 -> 1620
~ sub_10001d45c -> sub_10001d3f4 : 188 -> 180
~ sub_10001dab0 -> sub_10001da40 : 780 -> 772
~ _msg_syslog_facility : 88 -> 104
~ _name_mask_delim_opt : 432 -> 456
~ _long_name_mask_delim_opt : 428 -> 452
~ _printable : 124 -> 120
~ _split_nameval : 412 -> 392
~ _vbuf_print : 2500 -> 2416
~ _vstring_strcpy : 164 -> 148
~ _vstring_strcat : 160 -> 144
~ _sane_basename : 232 -> 208
~ sub_1000285ac -> sub_1000284d0 : 456 -> 448
~ _dict_pipe_open : 680 -> 668
~ _dict_union_open : 680 -> 668
~ _split_qnameval : 372 -> 360

```
