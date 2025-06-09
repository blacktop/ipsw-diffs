## iconservicesagent

> `/System/Library/CoreServices/iconservicesagent`

```diff

-657.10.0.0.0
-  __TEXT.__text: 0x36c8
-  __TEXT.__auth_stubs: 0x500
-  __TEXT.__objc_stubs: 0xd00
+705.100.0.0.0
+  __TEXT.__text: 0x39c4
+  __TEXT.__auth_stubs: 0x510
+  __TEXT.__objc_stubs: 0xe00
   __TEXT.__objc_methlist: 0x304
   __TEXT.__const: 0x50
-  __TEXT.__oslogstring: 0x635
-  __TEXT.__cstring: 0x1f1
+  __TEXT.__oslogstring: 0x6c9
+  __TEXT.__cstring: 0x1fc
   __TEXT.__gcc_except_tab: 0x88
-  __TEXT.__objc_methname: 0xceb
+  __TEXT.__objc_methname: 0xd8c
   __TEXT.__objc_classname: 0x8a
   __TEXT.__objc_methtype: 0x34c
-  __TEXT.__unwind_info: 0x140
-  __DATA_CONST.__auth_got: 0x290
-  __DATA_CONST.__got: 0x108
+  __TEXT.__unwind_info: 0x148
+  __DATA_CONST.__auth_got: 0x298
+  __DATA_CONST.__got: 0x110
   __DATA_CONST.__const: 0x150
-  __DATA_CONST.__cfstring: 0x180
+  __DATA_CONST.__cfstring: 0x1a0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_intobj: 0x18
   __DATA.__objc_const: 0x670
-  __DATA.__objc_selrefs: 0x458
+  __DATA.__objc_selrefs: 0x498
   __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x120

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /System/Library/Frameworks/ImageIO.framework/ImageIO
+  - /System/Library/Frameworks/Metal.framework/Metal
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/PrivateFrameworks/CoreUI.framework/CoreUI
   - /System/Library/PrivateFrameworks/IconFoundation.framework/IconFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A69C8C31-16FA-3521-89C1-3EB2D10DED32
-  Functions: 66
-  Symbols:   125
-  CStrings:  294
+  UUID: B536602A-594A-30E9-ACEF-4D41F79196A9
+  Functions: 68
+  Symbols:   127
+  CStrings:  307
 
Symbols:
+ _MTLSetShaderCachePath
+ _OBJC_CLASS_$_UTTypeRecord
CStrings:
+ "Client %d requesting a first party icon. Allowing"
+ "Client %d requesting an icon defined by CoreType. Allowing"
+ "Failed to get record for %@. Error: %@"
+ "ISTypeIcon"
+ "absoluteURL"
+ "bundleRecordWithBundleIdentifier:allowPlaceholder:error:"
+ "declaringBundleRecord"
+ "developerType"
+ "isCoreType"
+ "metalCacheURL"
+ "type"
+ "typeRecordWithIdentifier:"

```
