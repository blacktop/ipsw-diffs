## patch

> `/usr/bin/patch`

```diff

-  __TEXT.__text: 0x9a88
+  __TEXT.__text: 0x9a54
   __TEXT.__auth_stubs: 0x5b0
   __TEXT.__const: 0x5c
   __TEXT.__cstring: 0x1aad
-  __TEXT.__unwind_info: 0x168
+  __TEXT.__unwind_info: 0x170
   __DATA_CONST.__const: 0xc0
   __DATA_CONST.__auth_got: 0x2d8
   __DATA_CONST.__got: 0x40
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ sub_100002be4 : 684 -> 704
~ sub_1000033cc -> sub_1000033e0 : 3676 -> 3672
~ sub_100004228 -> sub_100004238 : 7896 -> 7904
~ sub_100006254 -> sub_10000626c : 220 -> 208
~ sub_100006840 -> sub_10000684c : 856 -> 860
~ sub_100006b98 -> sub_100006ba8 : 328 -> 332
~ sub_100006ce0 -> sub_100006cf4 : 236 -> 216
~ sub_100007018 : 2320 -> 2284
~ sub_100007f00 -> sub_100007edc : 1388 -> 1392
~ sub_10000846c -> sub_10000844c : 748 -> 728

```
