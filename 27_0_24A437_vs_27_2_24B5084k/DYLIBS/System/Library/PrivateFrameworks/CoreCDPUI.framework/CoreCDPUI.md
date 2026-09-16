## CoreCDPUI

> `/System/Library/PrivateFrameworks/CoreCDPUI.framework/CoreCDPUI`

```diff

-447.0.0.0.0
-  __TEXT.__text: 0x888a0
+448.125.5.1.0
+  __TEXT.__text: 0x888b0
   __TEXT.__objc_methlist: 0x4a94
   __TEXT.__const: 0x4824
   __TEXT.__cstring: 0x5d42
-  __TEXT.__oslogstring: 0x4aa2
+  __TEXT.__oslogstring: 0x4a92
   __TEXT.__gcc_except_tab: 0xc28
   __TEXT.__dlopen_cstrs: 0x2e8
   __TEXT.__constg_swiftt: 0x1b5c

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1448
+  __DATA_CONST.__const: 0x1458
   __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_catlist2: 0x10

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 3323
-  Symbols:   4980
+  Symbols:   4984
   CStrings:  937
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftAVFoundation_$_CoreCDPUI
+ __swift_FORCE_LOAD_$_swiftIntents
+ __swift_FORCE_LOAD_$_swiftIntents_$_CoreCDPUI
Functions:
~ ___76-[CDPUIStatusChangeController(Presentation) authenticate:completionHandler:]_block_invoke : 444 -> 460
CStrings:
+ "User cancelled ADP disablement: %@"
- "User cancelled ADP disablement...Nothing to do... %@"
```
