## Announce

> `/System/Library/PrivateFrameworks/Announce.framework/Announce`

```diff

-340.0.0.0.0
-  __TEXT.__text: 0x3e6dc
+344.3.0.0.1
+  __TEXT.__text: 0x3ed30
   __TEXT.__objc_methlist: 0x32a0
-  __TEXT.__const: 0x20a4
-  __TEXT.__cstring: 0x4255
-  __TEXT.__oslogstring: 0x2067
+  __TEXT.__const: 0x1fe4
+  __TEXT.__cstring: 0x4265
+  __TEXT.__oslogstring: 0x2077
   __TEXT.__gcc_except_tab: 0x4fc
-  __TEXT.__swift5_typeref: 0x9da
-  __TEXT.__swift5_reflstr: 0x927
+  __TEXT.__swift5_typeref: 0x9ca
+  __TEXT.__swift5_reflstr: 0x907
   __TEXT.__swift5_assocty: 0x1f0
-  __TEXT.__constg_swiftt: 0x8a0
+  __TEXT.__constg_swiftt: 0x8c8
   __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_fieldmd: 0x6f0
-  __TEXT.__swift5_proto: 0x168
+  __TEXT.__swift5_fieldmd: 0x6e4
+  __TEXT.__swift5_proto: 0x15c
   __TEXT.__swift5_types: 0x88
-  __TEXT.__swift5_capture: 0x124
-  __TEXT.__swift_as_entry: 0x38
-  __TEXT.__swift_as_ret: 0x40
-  __TEXT.__swift_as_cont: 0x78
+  __TEXT.__swift5_capture: 0xfc
+  __TEXT.__swift_as_entry: 0x40
+  __TEXT.__swift_as_ret: 0x4c
+  __TEXT.__swift_as_cont: 0x8c
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x17e0
-  __TEXT.__eh_frame: 0x958
+  __TEXT.__unwind_info: 0x1808
+  __TEXT.__eh_frame: 0xa40
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1020
+  __DATA_CONST.__const: 0x1038
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ca0
+  __DATA_CONST.__objc_selrefs: 0x1cb0
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0xb8
-  __DATA_CONST.__got: 0x428
-  __AUTH_CONST.__const: 0x1668
+  __DATA_CONST.__got: 0x430
+  __AUTH_CONST.__const: 0x1628
   __AUTH_CONST.__cfstring: 0x3100
   __AUTH_CONST.__objc_const: 0x5660
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_doubleobj: 0x110
-  __AUTH_CONST.__auth_got: 0x890
-  __AUTH.__objc_data: 0x1058
+  __AUTH_CONST.__auth_got: 0x888
+  __AUTH.__objc_data: 0x1080
   __AUTH.__data: 0x470
   __DATA.__objc_ivar: 0x238
   __DATA.__data: 0x12f0

   - /System/Library/Frameworks/Speech.framework/Speech
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore
+  - /System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech
   - /System/Library/PrivateFrameworks/CoreUtilsSwift.framework/CoreUtilsSwift
   - /System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation
   - /System/Library/PrivateFrameworks/HomeMessagingUtils.framework/HomeMessagingUtils

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
-  - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
-  - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1757
-  Symbols:   2474
-  CStrings:  717
+  Functions: 1765
+  Symbols:   2473
+  CStrings:  719
 
Symbols:
+ +[AVAudioSession(Announce) an_fetchSiriAudioSessionIDWithCompletion:]
+ _OBJC_CLASS_$_CSAudioSessionController
+ ___69+[AVAudioSession(Announce) an_fetchSiriAudioSessionIDWithCompletion:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e20_v20?0I8"NSError"12ls32l8
+ _swift_deletedAsyncMethodErrorTu
+ _symbolic Sccy__________G s6UInt32V s5NeverO
+ _symbolic _____ 8Announce27PersonaSharedUserIDResolverV
- __swift_FORCE_LOAD_$_swiftMLCompute
- __swift_FORCE_LOAD_$_swiftMLCompute_$_Announce
- __swift_FORCE_LOAD_$_swiftNaturalLanguage
- __swift_FORCE_LOAD_$_swiftNaturalLanguage_$_Announce
- _associated conformance 8Announce27SendAnnouncementIntentErrorOSHAASQ
- _objc_retain_x27
- _symbolic So17ANPlaybackCommandC
- _symbolic _____ 8Announce27SendAnnouncementIntentErrorO
CStrings:
+ "%@Failed to fetch Siri audio session ID. Error = %@"
+ "%@Siri audio session ID = %u"
+ "v20@?0I8@\"NSError\"12"
- "Not waiting for playback to complete. Returning success early."
```
