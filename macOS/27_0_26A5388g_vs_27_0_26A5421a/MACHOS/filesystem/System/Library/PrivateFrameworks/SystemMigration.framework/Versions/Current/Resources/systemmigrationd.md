## systemmigrationd

> `/System/Library/PrivateFrameworks/SystemMigration.framework/Versions/Current/Resources/systemmigrationd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA.__objc_selrefs`

```diff

-6164.0.5.0.0
-  __TEXT.__text: 0x210
-  __TEXT.__auth_stubs: 0x60
+6164.1.2.0.0
+  __TEXT.__text: 0x280
+  __TEXT.__auth_stubs: 0x70
   __TEXT.__objc_stubs: 0xc0
   __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x7b
+  __TEXT.__cstring: 0xbb
   __TEXT.__objc_methname: 0x75
   __TEXT.__unwind_info: 0x58
-  __DATA_CONST.__cfstring: 0x60
+  __DATA_CONST.__cfstring: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x38
+  __DATA_CONST.__auth_got: 0x40
   __DATA_CONST.__got: 0x20
   __DATA.__objc_selrefs: 0x30
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1
-  Symbols:   14
-  CStrings:  10
+  Symbols:   15
+  CStrings:  14
 
Symbols:
+ _os_variant_is_basesystem
Functions:
~ sub_100000a88 : 528 -> 640
CStrings:
+ "BaseSystem"
+ "Boot environment: %s"
+ "com.apple.SystemMigration"
+ "macOS"
```
