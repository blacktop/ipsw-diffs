## QuickLook

> `/System/Library/Frameworks/QuickLook.framework/QuickLook`

```diff

-1009.1.101.0.0
-  __TEXT.__text: 0xd39f4
+1011.1.0.0.0
+  __TEXT.__text: 0xd391c
   __TEXT.__auth_stubs: 0x2550
   __TEXT.__delay_stubs: 0x2c
   __TEXT.__delay_helper: 0x814

   __TEXT.__objc_methtype: 0x6ec0
   __TEXT.__objc_stubs: 0x156a0
   __DATA_CONST.__got: 0xf18
-  __DATA_CONST.__const: 0x25f0
+  __DATA_CONST.__const: 0x25e8
   __DATA_CONST.__objc_classlist: 0x468
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x398

   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftMetalKit.dylib
+  - /usr/lib/swift/libswiftModelIO.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftObservation.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 838D001D-45F0-3186-A1B1-A35B24307F7C
+  UUID: C2C27AD2-B943-39A6-A4C2-B0817FF80171
   Functions: 5486
-  Symbols:   13927
+  Symbols:   13925
   CStrings:  7185
 
Symbols:
+ ___block_descriptor_56_e8_32s40s48w_e15_v16?0"NSURL"8ls32l8s40l8w48l8
+ ___block_descriptor_64_e8_32s40s48s56w_e36_v24?0^{__CFString=}8^{__CFError=}16ls32l8s40l8s48l8w56l8
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreLocation_$_QuickLook
+ __swift_FORCE_LOAD_$_swiftMetalKit
+ __swift_FORCE_LOAD_$_swiftMetalKit_$_QuickLook
+ __swift_FORCE_LOAD_$_swiftModelIO
+ __swift_FORCE_LOAD_$_swiftModelIO_$_QuickLook
- ___block_descriptor_48_e8_32s40w_e15_v16?0"NSURL"8ls32l8w40l8
- ___block_descriptor_56_e8_32s40s48w_e36_v24?0^{__CFString=}8^{__CFError=}16ls32l8s40l8w48l8
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_QuickLook
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_QuickLook
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_QuickLook
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_QuickLook
Functions:
~ -[QLPreviewController(Overlay) _copyToButtonTapped:] : 288 -> 328
~ -[QLPreviewController(Overlay) _openInButtonTapped:] : 288 -> 348
~ ___52-[QLPreviewController(Overlay) _openInButtonTapped:]_block_invoke : 268 -> 288
~ ___52-[QLPreviewController(Overlay) _openInButtonTapped:]_block_invoke_2 : 548 -> 592
~ sub_21e8e6614 -> sub_21ed1c660 : 1724 -> 1668
~ sub_21e8e7208 -> sub_21ed1d21c : 3240 -> 3004
~ sub_21e8eb0e0 -> sub_21ed21008 : 2008 -> 1944
~ sub_21e8eca54 -> sub_21ed2293c : 736 -> 712

```
