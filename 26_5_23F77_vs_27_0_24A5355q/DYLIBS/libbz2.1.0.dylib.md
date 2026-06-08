## libbz2.1.0.dylib

> `/usr/lib/libbz2.1.0.dylib`

```diff

 49.0.0.0.0
-  __TEXT.__text: 0xa9c4
-  __TEXT.__auth_stubs: 0x130
+  __TEXT.__text: 0xb004
   __TEXT.__const: 0x4e0
   __TEXT.__cstring: 0x94b
-  __TEXT.__unwind_info: 0x110
-  __DATA_CONST.__got: 0x20
+  __TEXT.__unwind_info: 0x120
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x80
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__auth_got: 0x98
   __DATA.__data: 0x800
   - /usr/lib/libSystem.B.dylib
-  UUID: EC2C66EE-C164-3F43-B397-967BDD8F54E6
+  UUID: 61A9068B-C5CD-3BDD-851F-791201750406
   Functions: 43
   Symbols:   48
   CStrings:  40
Functions:
~ _BZ2_bzBuffToBuffCompress -> sub_2bd05281c : 260 -> 20
~ sub_2a2ce0920 -> _BZ2_bzBuffToBuffCompress : 20 -> 260
~ sub_2a2ce0ec4 -> sub_2bd052ec4 : 312 -> 324
~ sub_2a2ce0ffc -> sub_2bd053008 : 13504 -> 3984
~ sub_2a2ce44bc -> sub_2bd053f98 : 3884 -> 13968
~ sub_2a2ce53e8 -> sub_2bd057628 : 2224 -> 684
~ sub_2a2ce5e2c -> sub_2bd057a68 : 1008 -> 1168
~ sub_2a2ce6274 -> _BZ2_bzCompressEnd : 16 -> 144
~ _BZ2_bzCompressEnd -> sub_2bd057fe0 : 144 -> 16
~ sub_2a2ce6314 -> sub_2bd057ff0 : 684 -> 100
~ sub_2a2ce65c0 -> sub_2bd058054 : 100 -> 2260
~ _BZ2_bzDecompress : 3448 -> 3488
~ _BZ2_bzWrite : 324 -> 328
~ _BZ2_bzWriteClose64 : 516 -> 520
~ _BZ2_bzRead : 452 -> 456
~ _BZ2_bzclose : 200 -> 204
~ sub_2a2ce856c -> sub_2bd05a8a8 : 10576 -> 11336
~ sub_2a2ceaebc -> sub_2bd05d4f0 : 320 -> 332

```
