## UARPAssetManager

> `/System/Library/PrivateFrameworks/UARPAssetManager.framework/UARPAssetManager`

```diff

-1338.60.22.0.0
-  __TEXT.__text: 0x4088
+1338.80.29.0.0
+  __TEXT.__text: 0x429c
   __TEXT.__auth_stubs: 0x370
-  __TEXT.__objc_methlist: 0x6f4
+  __TEXT.__objc_methlist: 0x724
   __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x573
+  __TEXT.__cstring: 0x5bb
   __TEXT.__gcc_except_tab: 0x18c
   __TEXT.__oslogstring: 0xc8
   __TEXT.__unwind_info: 0x240
   __TEXT.__objc_classname: 0x11b
-  __TEXT.__objc_methname: 0xdad
-  __TEXT.__objc_methtype: 0x356
-  __TEXT.__objc_stubs: 0x980
+  __TEXT.__objc_methname: 0xe72
+  __TEXT.__objc_methtype: 0x35c
+  __TEXT.__objc_stubs: 0x9c0
   __DATA_CONST.__got: 0xa0
   __DATA_CONST.__const: 0x138
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x388
+  __DATA_CONST.__objc_selrefs: 0x3a0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x38
   __AUTH_CONST.__auth_got: 0x1c8
-  __AUTH_CONST.__cfstring: 0x560
-  __AUTH_CONST.__objc_const: 0xdb0
+  __AUTH_CONST.__cfstring: 0x5c0
+  __AUTH_CONST.__objc_const: 0xe40
   __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x78
+  __DATA.__objc_ivar: 0x84
   __DATA.__data: 0x1e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4216CDD7-F27C-30F1-9D45-95AD38CE44C8
-  Functions: 130
-  Symbols:   574
-  CStrings:  337
+  UUID: 900F34AB-AF19-34C3-B804-CBEDB5744ADB
+  Functions: 134
+  Symbols:   587
+  CStrings:  351
 
Symbols:
+ -[UARPAssetManagerCacheConfiguration initWithAppleModelNumber:hwFusing:domain:assetVersion:filePath:usePallas:internalVersion:restoreVersion:]
+ -[UARPAssetManagerCacheConfiguration internalVersion]
+ -[UARPAssetManagerCacheConfiguration restoreVersion]
+ -[UARPEndpointPersonalityMobileAsset internalVariant]
+ -[UARPEndpointPersonalityMobileAsset setInternalVariant:]
+ _OBJC_IVAR_$_UARPAssetManagerCacheConfiguration._internalVersion
+ _OBJC_IVAR_$_UARPAssetManagerCacheConfiguration._restoreVersion
+ _OBJC_IVAR_$_UARPEndpointPersonalityMobileAsset._internalVariant
+ _objc_msgSend$initWithAppleModelNumber:hwFusing:domain:assetVersion:filePath:usePallas:internalVersion:restoreVersion:
+ _objc_msgSend$internalVariant
+ _objc_msgSend$setInternalVariant:
- -[UARPAssetManagerCacheConfiguration initWithAppleModelNumber:hwFusing:domain:assetVersion:filePath:usePallas:]
- _objc_msgSend$initWithAppleModelNumber:hwFusing:domain:assetVersion:filePath:usePallas:
CStrings:
+ "<%@: model=%@ fusing=%@ domain=%@ pallas=%d vers=%@ file=%@ internal=%d restoreVersion=%@>"
+ "@72@0:8@16@24@32@40@48B56B60@64"
+ "T@\"NSString\",R,C,V_restoreVersion"
+ "TB,R,V_internalVariant"
+ "TB,R,V_internalVersion"
+ "_internalVariant"
+ "_internalVersion"
+ "initWithAppleModelNumber:hwFusing:domain:assetVersion:filePath:usePallas:internalVersion:restoreVersion:"
+ "internal "
+ "internalVariant"
+ "internalVersion"
+ "setInternalVariant:"
- "<%@: model=%@ fusing=%@ domain=%@ pallas=%d vers=%@ file=%@>"
- "@60@0:8@16@24@32@40@48B56"
- "initWithAppleModelNumber:hwFusing:domain:assetVersion:filePath:usePallas:"

```
