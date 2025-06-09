## SiriSuggestionsFlowPlugin

> `/System/Library/Assistant/FlowDelegatePlugins/SiriSuggestionsFlowPlugin.bundle/SiriSuggestionsFlowPlugin`

```diff

-3405.21.1.0.0
-  __TEXT.__text: 0xd038
-  __TEXT.__auth_stubs: 0xcd0
-  __TEXT.__const: 0x37a
-  __TEXT.__cstring: 0x273
-  __TEXT.__constg_swiftt: 0x210
-  __TEXT.__swift5_typeref: 0x1c6
-  __TEXT.__swift5_reflstr: 0x143
-  __TEXT.__swift5_fieldmd: 0xe0
+3500.39.1.0.0
+  __TEXT.__text: 0xd8c0
+  __TEXT.__auth_stubs: 0xc80
+  __TEXT.__const: 0x41a
+  __TEXT.__cstring: 0x293
+  __TEXT.__constg_swiftt: 0x228
+  __TEXT.__swift5_typeref: 0x1cc
+  __TEXT.__swift5_reflstr: 0x163
+  __TEXT.__swift5_fieldmd: 0xec
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_capture: 0x58
-  __TEXT.__oslogstring: 0x77e
+  __TEXT.__oslogstring: 0x81e
   __TEXT.__objc_methname: 0x4f
   __TEXT.__swift5_proto: 0x1c
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift_as_entry: 0x28
   __TEXT.__swift_as_ret: 0x38
-  __TEXT.__unwind_info: 0x370
-  __TEXT.__eh_frame: 0x888
-  __DATA_CONST.__auth_got: 0x668
-  __DATA_CONST.__got: 0x180
+  __TEXT.__unwind_info: 0x368
+  __TEXT.__eh_frame: 0x830
+  __DATA_CONST.__auth_got: 0x640
+  __DATA_CONST.__got: 0x170
   __DATA_CONST.__auth_ptr: 0x1a0
-  __DATA_CONST.__const: 0x1c8
+  __DATA_CONST.__const: 0x1c0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x3e0
+  __DATA.__objc_const: 0x400
   __DATA.__objc_selrefs: 0x28
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x610
+  __DATA.__data: 0x5c8
   __DATA.__bss: 0x380
   __DATA.__common: 0x8
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/SiriFlowEnvironment.framework/SiriFlowEnvironment
   - /System/Library/PrivateFrameworks/SiriInferenceIntents.framework/SiriInferenceIntents
   - /System/Library/PrivateFrameworks/SiriKitFlow.framework/SiriKitFlow

   - /System/Library/PrivateFrameworks/SiriSuggestionsKit.framework/SiriSuggestionsKit
   - /System/Library/PrivateFrameworks/SiriSuggestionsSupport.framework/SiriSuggestionsSupport
   - /System/Library/PrivateFrameworks/SiriUtilities.framework/SiriUtilities
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
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
-  UUID: C2FC9AB9-CF80-3B80-B436-8391621F4760
-  Functions: 303
-  Symbols:   104
-  CStrings:  55
+  UUID: 38F9EBF5-4702-30FF-965B-48879BA07A40
+  Functions: 313
+  Symbols:   96
+  CStrings:  58
 
Symbols:
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _objc_release_x21
+ _swift_arrayDestroy
+ _swift_coroFrameAlloc
- __swift_FORCE_LOAD_$_swiftCryptoTokenKit
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _objc_release_x22
- _objc_release_x9
- _objc_retain_x22
- _swift_bridgeObjectRelease_n
- _swift_release_n
- _swift_retain_n
CStrings:
+ "SiriSuggestionsFlow :: existingSuggestionsFlow has sessionId: %s"
+ "SiriSuggestionsFlow :: previousExecutionSessionId: %s, currentSessionId: %s"
+ "previousExecutionSessionId"

```
