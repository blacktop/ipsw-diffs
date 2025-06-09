## siriinferenced

> `/System/Library/PrivateFrameworks/SiriInference.framework/Support/siriinferenced`

```diff

-3405.20.2.0.0
-  __TEXT.__text: 0x12fe8
-  __TEXT.__auth_stubs: 0x1120
+3500.67.1.0.0
+  __TEXT.__text: 0x10c54
+  __TEXT.__auth_stubs: 0x10f0
   __TEXT.__objc_methlist: 0x2cc
-  __TEXT.__const: 0x378
-  __TEXT.__cstring: 0xa39
-  __TEXT.__oslogstring: 0xe78
+  __TEXT.__const: 0x3b8
+  __TEXT.__cstring: 0xa89
+  __TEXT.__oslogstring: 0xec8
   __TEXT.__objc_methname: 0x736
   __TEXT.__swift5_typeref: 0x35c
   __TEXT.__swift5_entry: 0x8

   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0x8
-  __TEXT.__unwind_info: 0x410
-  __TEXT.__eh_frame: 0x4c8
-  __DATA_CONST.__auth_got: 0x890
+  __TEXT.__unwind_info: 0x418
+  __TEXT.__eh_frame: 0x4b8
+  __DATA_CONST.__auth_got: 0x878
   __DATA_CONST.__got: 0x200
-  __DATA_CONST.__auth_ptr: 0x198
-  __DATA_CONST.__const: 0x668
+  __DATA_CONST.__auth_ptr: 0x170
+  __DATA_CONST.__const: 0x678
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_const: 0x9a8
   __DATA.__objc_selrefs: 0x278
   __DATA.__objc_data: 0x480
-  __DATA.__data: 0x988
+  __DATA.__data: 0x958
   __DATA.__common: 0xc8
   __DATA.__bss: 0x180
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AIMLExperimentationAnalytics.framework/AIMLExperimentationAnalytics
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary

   - /System/Library/PrivateFrameworks/SiriIntentEvents.framework/SiriIntentEvents
   - /System/Library/PrivateFrameworks/SiriRemembers.framework/SiriRemembers
   - /System/Library/PrivateFrameworks/SiriSignals.framework/SiriSignals
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
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
-  UUID: 3D0B9C62-E3F7-3F34-8AAA-1D038B12CB2D
-  Functions: 414
-  Symbols:   418
-  CStrings:  259
+  UUID: 839D98B0-0914-3248-873E-CBA973E186AE
+  Functions: 386
+  Symbols:   412
+  CStrings:  261
 
Symbols:
+ _$s10Foundation4DataV11InlineSliceV21ensureUniqueReferenceyyF
+ _$s11SiriSignals26AppSelectionActivationFlagC20notHomePodOrIsActiveSbvgZ
+ _$s11SiriSignals26AppSelectionActivationFlagCMa
+ _$s13SiriInference11DASActivityV10unregister6cancelySb_tF
+ _$s13SiriInference11DASActivityV17registerAndSubmityyF
+ _$ss11_StringGutsV16_foreignCopyUTF84intoSiSgSrys5UInt8VG_tF
+ _$ss20__StaticArrayStorageCN
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _memset
- _$s11SiriSignals13DeviceSupportO9isHomePodSbvgZ
- _$s13SiriInference11DASActivityV10unregisteryyF
- _$s13SiriInference11DASActivityV8registeryyF
- _$ss11_StringGutsV8copyUTF84intoSiSgSrys5UInt8VG_tF
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _bzero
- _objc_retain_x25
- _swift_bridgeObjectRelease_n
- _swift_bridgeObjectRetain_n
- _swift_unknownObjectRelease_n
- _swift_unknownObjectRetain_n
CStrings:
+ "AppSelection was activated so siriinferenced should run on the normal schedule"
+ "XPC event [%s] is unhandled"
+ "com.apple.siriinferenced.musicAppSelectionActivationNotification"
- "XPC event is unhandled"

```
