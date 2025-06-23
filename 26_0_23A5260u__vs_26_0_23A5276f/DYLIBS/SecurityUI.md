## SecurityUI

> `/System/Library/Frameworks/SecurityUI.framework/SecurityUI`

```diff

 55210.0.0.0.0
-  __TEXT.__text: 0x18e74
-  __TEXT.__auth_stubs: 0x1260
+  __TEXT.__text: 0x18de0
+  __TEXT.__auth_stubs: 0x1270
   __TEXT.__objc_methlist: 0x5e4
   __TEXT.__const: 0xd14
-  __TEXT.__oslogstring: 0x205
-  __TEXT.__cstring: 0x9ca
+  __TEXT.__oslogstring: 0x175
+  __TEXT.__cstring: 0xa5a
   __TEXT.__swift5_typeref: 0x20a8
   __TEXT.__swift5_capture: 0x13c
   __TEXT.__constg_swiftt: 0x660

   __TEXT.__objc_methtype: 0x336
   __TEXT.__objc_stubs: 0x680
   __DATA_CONST.__got: 0x390
-  __DATA_CONST.__const: 0x1f0
+  __DATA_CONST.__const: 0x1d0
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x400
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x938
+  __AUTH_CONST.__auth_got: 0x940
   __AUTH_CONST.__const: 0xa90
   __AUTH_CONST.__cfstring: 0x1c0
   __AUTH_CONST.__objc_const: 0x1178

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8F322463-43CB-35C1-9837-C966B3C69E8A
+  UUID: D01617F0-936A-32FD-81BB-C2D156CE890D
   Functions: 689
-  Symbols:   2690
+  Symbols:   2683
   CStrings:  335
 
Symbols:
+ _$s2os0A4_log_3dso0B0__ySo0a1_B7_type_ta_SVSo03OS_a1_B0Cs12StaticStringVs7CVarArg_pdtF
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_SecurityUI
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_SecurityUI
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_SecurityUI
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_SecurityUI
Functions:
~ _$s7SwiftUI11EnvironmentV12wrappedValuexvgAA13OpenURLActionV_Tg5 : 640 -> 492
CStrings:
+ "Accessing Environment's value outside of being installed on a View. This will always read the default value and will not update."
- "Accessing Environment<%s>'s value outside of being installed on a View. This will always read the default value and will not update."

```
