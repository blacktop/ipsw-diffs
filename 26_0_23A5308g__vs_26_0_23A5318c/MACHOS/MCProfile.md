## MCProfile

> `/System/Library/DataClassMigrators/MCProfile.migrator/MCProfile`

```diff

-2426.1.0.0.0
-  __TEXT.__text: 0xf24
-  __TEXT.__auth_stubs: 0x1e0
-  __TEXT.__objc_stubs: 0x560
-  __TEXT.__objc_methlist: 0xa4
+2428.0.0.0.0
+  __TEXT.__text: 0x1098
+  __TEXT.__auth_stubs: 0x200
+  __TEXT.__objc_stubs: 0x580
+  __TEXT.__objc_methlist: 0xb0
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x385
+  __TEXT.__cstring: 0x471
   __TEXT.__objc_classname: 0x12
-  __TEXT.__objc_methname: 0x521
-  __TEXT.__objc_methtype: 0x2b
+  __TEXT.__objc_methname: 0x54a
+  __TEXT.__objc_methtype: 0x3d
   __TEXT.__unwind_info: 0x90
-  __DATA_CONST.__auth_got: 0xf8
+  __DATA_CONST.__auth_got: 0x108
   __DATA_CONST.__got: 0xa8
   __DATA_CONST.__const: 0x68
-  __DATA_CONST.__cfstring: 0x2c0
+  __DATA_CONST.__cfstring: 0x340
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x178
+  __DATA.__objc_selrefs: 0x180
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 60C7FE8B-2670-31F6-91AA-1B31DC745C3A
-  Functions: 16
-  Symbols:   61
-  CStrings:  98
+  UUID: 514F2D14-4912-3C8F-A7E7-BCAD6D7EF07E
+  Functions: 17
+  Symbols:   63
+  CStrings:  108
 
Symbols:
+ _objc_retain_x2
+ _objc_retain_x20
Functions:
~ sub_ad4 : 1008 -> 1264
CStrings:
+ "B40@0:8@16@24^@32"
+ "Failed to remove cloud config with error: %@."
+ "Failed to remove legacy cloud config with error: %@."
+ "Failed to remove legacy post Setup auto install profile with error: %@."
+ "Failed to remove post Setup auto install profile with error: %@."
+ "_removeFileIfExistsWithFM:path:outError:"

```
