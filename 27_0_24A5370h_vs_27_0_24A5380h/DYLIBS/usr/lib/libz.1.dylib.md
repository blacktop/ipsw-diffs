## libz.1.dylib

> `/usr/lib/libz.1.dylib`

```diff

-  __TEXT.__text: 0xb95c
+  __TEXT.__text: 0xb790
   __TEXT.__const: 0x2748
   __TEXT.__cstring: 0x3b2
-  __TEXT.__unwind_info: 0x218
+  __TEXT.__unwind_info: 0x210
   __TEXT.__eh_frame: 0x50
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0xb0
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
Functions:
~ sub_2c047d9b8 -> sub_2c10c19b8 : 472 -> 484
~ _inflate : 6480 -> 6000
~ _adler32_z : 320 -> 300
~ _adler32 : 8 -> 16
~ sub_2c04819c0 -> sub_2c10c57e0 : 1164 -> 1180
~ _deflateInit_ -> sub_2c10c7f74 : 28 -> 248
~ sub_2c0484160 -> _gzclose_w : 8 -> 220
~ _deflateBound -> _deflateInit_ : 292 -> 28
~ _gzclose_w -> sub_2c10c8164 : 220 -> 8
~ sub_2c0484368 -> _deflateBound : 248 -> 292
~ sub_2c0485410 -> sub_2c10c9240 : 980 -> 984

```
