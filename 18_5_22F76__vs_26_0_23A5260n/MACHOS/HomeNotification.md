## HomeNotification

> `/private/var/staged_system_apps/Home.app/PlugIns/HomeNotification.appex/HomeNotification`

```diff

-1026.6.29.1.2
-  __TEXT.__text: 0xafec
+1071.0.4.1.2
+  __TEXT.__text: 0xaf48
   __TEXT.__auth_stubs: 0x4e0
-  __TEXT.__objc_stubs: 0x2aa0
-  __TEXT.__objc_methlist: 0xe04
+  __TEXT.__objc_stubs: 0x2a60
+  __TEXT.__objc_methlist: 0xe2c
   __TEXT.__const: 0xb2
   __TEXT.__gcc_except_tab: 0x268
   __TEXT.__cstring: 0x8ca
-  __TEXT.__objc_methname: 0x387e
+  __TEXT.__objc_methname: 0x38ea
   __TEXT.__oslogstring: 0xa94
   __TEXT.__objc_classname: 0x1ca
   __TEXT.__objc_methtype: 0xa0b
   __TEXT.__constg_swiftt: 0xc
   __TEXT.__swift5_proto: 0x4
-  __TEXT.__unwind_info: 0x368
+  __TEXT.__unwind_info: 0x360
   __DATA_CONST.__auth_got: 0x280
   __DATA_CONST.__got: 0x240
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0xa40
+  __DATA_CONST.__const: 0xa20
   __DATA_CONST.__cfstring: 0x6e0
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x48

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x1438
-  __DATA.__objc_selrefs: 0xee8
+  __DATA.__objc_const: 0x1450
+  __DATA.__objc_selrefs: 0xef0
   __DATA.__objc_ivar: 0xcc
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x378

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCallKit.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
+  - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMapKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftMetalKit.dylib

   - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 7F079CD1-04E7-3E1B-BC62-73A012512EA7
+  UUID: 82353773-EF50-3997-953A-8BA362B3D9D7
   Functions: 267
-  Symbols:   224
-  CStrings:  894
+  Symbols:   220
+  CStrings:  895
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCallKit
+ __swift_FORCE_LOAD_$_swiftMLCompute
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swiftCryptoTokenKit
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
Functions:
~ sub_100006ed0 -> sub_100006df0 : 628 -> 504
~ sub_100007280 -> sub_100007124 : 4 -> 92
~ sub_1000073d0 -> sub_1000072cc : 1028 -> 900
CStrings:
+ "accessory:didUpdateHH1EOLEnabled:"
+ "accessoryDidSetHasOnboardedForAdaptiveTemperatureAutomations:"
+ "accessoryDidSetHasOnboardedForCleanEnergyAutomation:"
- "clearColor"
- "setWantsPreferredContentSize:"

```
