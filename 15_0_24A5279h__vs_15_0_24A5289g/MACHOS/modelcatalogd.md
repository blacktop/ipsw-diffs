## modelcatalogd

> `/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/Versions/A/modelcatalogd`

```diff

-127.0.0.0.0
+136.100.0.0.0
   __TEXT.__text: 0x38
   __TEXT.__auth_stubs: 0x20
   __TEXT.__swift5_entry: 0x8

   __TEXT.__unwind_info: 0x58
   __DATA_CONST.__auth_got: 0x10
   __DATA_CONST.__got: 0x8
-  __DATA_CONST.__const: 0x50
+  __DATA_CONST.__const: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/Versions/A/ModelCatalogRuntime

   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   Functions: 1
-  Symbols:   13
+  Symbols:   14
   CStrings:  0
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers

```
