## com.apple.Translate.appremoval

> `/System/Library/AppRemovalServices/com.apple.Translate.appremoval.xpc/com.apple.Translate.appremoval`

```diff

-252.12.0.0.0
-  __TEXT.__text: 0x1694
+255.14.0.0.0
+  __TEXT.__text: 0x16c4
   __TEXT.__auth_stubs: 0x3d0
   __TEXT.__objc_methlist: 0x40
   __TEXT.__const: 0xcc
-  __TEXT.__objc_methname: 0x1db
+  __TEXT.__objc_methname: 0x208
   __TEXT.__swift5_entry: 0x8
   __TEXT.__cstring: 0x1b6
   __TEXT.__constg_swiftt: 0x84

   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0x20
   __DATA.__objc_const: 0x428
   __DATA.__objc_selrefs: 0x60
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x20
   __DATA.__objc_data: 0x170
   __DATA.__data: 0x1a0
   __DATA.__common: 0x28
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Translation.framework/Translation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
-  - /System/Library/PrivateFrameworks/Translation.framework/Translation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: AB2F07D7-4C28-3335-BD9F-65787764F933
+  UUID: FACEA444-ED74-37FA-83B5-90310C0A1830
   Functions: 38
-  Symbols:   73
-  CStrings:  68
+  Symbols:   72
+  CStrings:  69
 
Symbols:
+ _objc_retain_x2
+ _objc_retain_x24
+ _objc_retain_x26
- _objc_retain
- _objc_retain_x10
- _objc_retain_x23
- _objc_retain_x8
CStrings:
+ "T@\"NSString\",?,R,C"
+ "_purgeAllAssetsExcludingConfig:completion:"
- "_purgeAllAssets:"

```
