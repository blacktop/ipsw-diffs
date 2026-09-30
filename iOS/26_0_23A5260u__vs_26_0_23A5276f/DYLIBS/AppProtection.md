## AppProtection

> `/System/Library/PrivateFrameworks/AppProtection.framework/AppProtection`

```diff

-38.0.0.0.0
-  __TEXT.__text: 0xa118c
+40.0.0.0.0
+  __TEXT.__text: 0xa1160
   __TEXT.__auth_stubs: 0x1fa0
   __TEXT.__delay_helper: 0xc8
   __TEXT.__objc_methlist: 0x16c4

   __TEXT.__objc_methtype: 0x758
   __TEXT.__objc_stubs: 0x580
   __DATA_CONST.__got: 0x5c0
-  __DATA_CONST.__const: 0x378
+  __DATA_CONST.__const: 0x358
   __DATA_CONST.__objc_classlist: 0x2a0
   __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 22C973FD-F005-3568-8796-65AF37836BE2
+  UUID: 6CDFCE5A-AF26-3323-98F0-EDAC4BCD8015
   Functions: 3568
-  Symbols:   3161
+  Symbols:   3153
   CStrings:  1421
 
Symbols:
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_AppProtection
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_AppProtection
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_AppProtection
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_AppProtection
Functions:
~ sub_24fd55f34 -> sub_2508f1e54 : 1436 -> 1392
CStrings:
+ "client is not entitled to monitor view subject %{public}s"
- "client is not entitled to monitir view subject %{public}s"

```
