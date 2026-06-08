## MCProfile

> `/System/Library/DataClassMigrators/MCProfile.migrator/MCProfile`

```diff

-2438.120.3.0.0
-  __TEXT.__text: 0x1150
+2479.0.0.0.0
+  __TEXT.__text: 0x1014
   __TEXT.__auth_stubs: 0x200
-  __TEXT.__objc_stubs: 0x580
+  __TEXT.__objc_stubs: 0x560
   __TEXT.__objc_methlist: 0xb0
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x471
+  __TEXT.__cstring: 0x44e
   __TEXT.__objc_classname: 0x12
   __TEXT.__objc_methname: 0x54a
   __TEXT.__objc_methtype: 0x3d
   __TEXT.__unwind_info: 0x90
-  __DATA_CONST.__auth_got: 0x108
-  __DATA_CONST.__got: 0xa8
   __DATA_CONST.__const: 0x68
-  __DATA_CONST.__cfstring: 0x340
+  __DATA_CONST.__cfstring: 0x320
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x108
+  __DATA_CONST.__got: 0xa8
   __DATA.__objc_const: 0x90
   __DATA.__objc_selrefs: 0x180
   __DATA.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6139761A-3266-3ED4-9458-AA0D5256D255
+  UUID: 421DDD22-E757-3367-A577-B0E170C4B9D4
   Functions: 17
   Symbols:   63
-  CStrings:  108
+  CStrings:  106
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x2
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x26
- _objc_retain_x28
Functions:
~ sub_ad4 : 1332 -> 1144
~ sub_1008 -> sub_f4c : 720 -> 696
~ sub_12d8 -> sub_1204 : 148 -> 144
~ sub_136c -> sub_1294 : 200 -> 196
~ sub_14ac -> sub_13d0 : 404 -> 376
~ sub_1640 -> sub_1548 : 228 -> 216
~ sub_1724 -> sub_1620 : 420 -> 392
~ sub_18c8 -> sub_17a8 : 220 -> 204
~ sub_19f0 -> sub_18c0 : 240 -> 228
~ sub_1ae0 -> sub_19a4 : 84 -> 80
~ sub_1b98 -> sub_1a58 : 112 -> 116
CStrings:
- "Locking down cloud config details."

```
