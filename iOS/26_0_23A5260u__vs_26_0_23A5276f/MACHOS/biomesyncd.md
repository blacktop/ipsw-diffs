## biomesyncd

> `/usr/libexec/biomesyncd`

```diff

-192.0.0.0.0
-  __TEXT.__text: 0x4bd34
+195.0.0.0.0
+  __TEXT.__text: 0x4be10
   __TEXT.__auth_stubs: 0xcf0
-  __TEXT.__objc_stubs: 0x86a0
+  __TEXT.__objc_stubs: 0x86e0
   __TEXT.__objc_methlist: 0x3ba4
-  __TEXT.__const: 0x1388
+  __TEXT.__const: 0x1338
   __TEXT.__gcc_except_tab: 0x9f8
-  __TEXT.__objc_methname: 0xa0b1
-  __TEXT.__cstring: 0x57d8
+  __TEXT.__objc_methname: 0xa0f1
+  __TEXT.__cstring: 0x57fb
   __TEXT.__objc_classname: 0x83d
   __TEXT.__objc_methtype: 0x16f1
   __TEXT.__oslogstring: 0x604e

   __DATA_CONST.__auth_got: 0x688
   __DATA_CONST.__got: 0x3d0
   __DATA_CONST.__const: 0x10d8
-  __DATA_CONST.__cfstring: 0x45c0
+  __DATA_CONST.__cfstring: 0x45e0
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1a0
-  __DATA_CONST.__objc_arraydata: 0x560
-  __DATA_CONST.__objc_arrayobj: 0x858
-  __DATA_CONST.__objc_intobj: 0x2b8
+  __DATA_CONST.__objc_arraydata: 0x568
+  __DATA_CONST.__objc_arrayobj: 0x870
+  __DATA_CONST.__objc_intobj: 0x2d0
   __DATA_CONST.__linkguard: 0xe
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x7698
-  __DATA.__objc_selrefs: 0x2838
-  __DATA.__objc_ivar: 0x3e0
+  __DATA.__objc_const: 0x76d8
+  __DATA.__objc_selrefs: 0x2848
+  __DATA.__objc_ivar: 0x3e8
   __DATA.__objc_data: 0x1180
   __DATA.__data: 0x840
   __DATA.__bss: 0xf0

   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/BiomeSync.framework/BiomeSync
   - /System/Library/PrivateFrameworks/CascadeEngine.framework/CascadeEngine
+  - /System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets
   - /System/Library/PrivateFrameworks/CloudKitDistributedSync.framework/CloudKitDistributedSync
   - /System/Library/PrivateFrameworks/ContextSync.framework/ContextSync
   - /System/Library/PrivateFrameworks/IntelligencePlatform.framework/IntelligencePlatform

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 8B923C0B-4ECE-33A0-B3C1-54FD35E25420
+  UUID: ECE14147-CC56-3A4B-BDA0-9FB876432992
   Functions: 1598
   Symbols:   347
-  CStrings:  3624
+  CStrings:  3629
 
Functions:
~ sub_100011604 -> sub_100011664 : 432 -> 476
~ sub_100014734 -> sub_1000147c0 : 476 -> 372
~ sub_100014910 -> sub_100014934 : 2080 -> 2288
~ sub_100018278 -> sub_10001836c : 188 -> 212
~ sub_10003aa3c -> sub_10003ab48 : 968 -> 1016
CStrings:
+ "DROP INDEX idx_atom_batch_filename"
+ "_enumeratorCache"
+ "_readerCache"
+ "segmentPath"
+ "skipToBookmarkOffset:"
- "\f"

```
