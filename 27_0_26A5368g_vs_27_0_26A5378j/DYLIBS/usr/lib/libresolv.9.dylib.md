## libresolv.9.dylib

> `/usr/lib/libresolv.9.dylib`

```diff

-  __TEXT.__text: 0x18b84
+  __TEXT.__text: 0x18ad4
   __TEXT.__const: 0x3fa
   __TEXT.__cstring: 0x21c7
   __TEXT.__unwind_info: 0x340
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ _res_9_vinit : 5220 -> 5196
~ _res_next_word : 152 -> 132
~ _res_9_ns_name_pack : 824 -> 828
~ _res_9_ns_makecanon : 244 -> 256
~ _res_9_getservers : 188 -> 196
~ _res_9_b64_ntop : 344 -> 332
~ _res_9_b64_pton : 680 -> 636
~ __check_cache : 1348 -> 1304
~ _res_9_ns_name_pton2 : 1076 -> 1056
~ _res_9_ns_format_ttl : 524 -> 516
~ _res_9_sym_ntop : 160 -> 156
~ _res_9_loc_aton : 1008 -> 992
~ _latlon2ul : 944 -> 948
~ _res_9_nametoclass : 264 -> 256
~ _res_9_nametotype : 264 -> 256
~ _res_9_setservers : 232 -> 220
~ _res_nsearch_2 : 816 -> 812
~ _res_9_hostalias_2 : 492 -> 488
~ ___res_nsearch_list_2 : 832 -> 860
~ _res_9_nsearch : 1000 -> 996

```
