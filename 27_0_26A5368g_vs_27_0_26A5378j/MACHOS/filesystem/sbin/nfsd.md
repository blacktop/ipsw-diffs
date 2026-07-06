## nfsd

> `/sbin/nfsd`

```diff

-  __TEXT.__text: 0xf72c
+  __TEXT.__text: 0xf6d8
   __TEXT.__auth_stubs: 0xb40
   __TEXT.__const: 0xa0
   __TEXT.__cstring: 0x4429
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__data : content changed
Functions:
~ sub_100000bd4 : 1896 -> 1768
~ sub_1000021b4 -> sub_100002134 : 1220 -> 1232
~ sub_100006f48 -> sub_100006ed4 : 248 -> 264
~ sub_10000b334 -> sub_10000b2d0 : 296 -> 308
~ sub_10000d8c8 -> sub_10000d870 : 1444 -> 1448

```
