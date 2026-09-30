## com.apple.SpeechRecognitionCore.speechrecognitiond

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/XPCServices/com.apple.SpeechRecognitionCore.speechrecognitiond.xpc/com.apple.SpeechRecognitionCore.speechrecognitiond`

```diff

-6.3.60.0.0
-  __TEXT.__text: 0xd4c24
-  __TEXT.__auth_stubs: 0x27e0
-  __TEXT.__objc_stubs: 0x3420
+6.3.62.0.0
+  __TEXT.__text: 0xc0168
+  __TEXT.__auth_stubs: 0x25f0
+  __TEXT.__objc_stubs: 0x3440
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x18d4
-  __TEXT.__const: 0x6546
-  __TEXT.__gcc_except_tab: 0x9438
-  __TEXT.__objc_methname: 0x49a1
-  __TEXT.__cstring: 0x4142
-  __TEXT.__oslogstring: 0x5554
+  __TEXT.__const: 0x5d56
+  __TEXT.__gcc_except_tab: 0x9460
+  __TEXT.__objc_methname: 0x49cd
+  __TEXT.__cstring: 0x4032
+  __TEXT.__oslogstring: 0x5644
   __TEXT.__objc_classname: 0x348
   __TEXT.__objc_methtype: 0x1012
   __TEXT.__dlopen_cstrs: 0x6a
   __TEXT.__ustring: 0x4
-  __TEXT.__swift5_typeref: 0xd34
-  __TEXT.__swift5_reflstr: 0x798
-  __TEXT.__swift5_assocty: 0xa8
-  __TEXT.__swift5_fieldmd: 0x778
-  __TEXT.__constg_swiftt: 0x11c0
-  __TEXT.__swift5_protos: 0x4
-  __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_builtin: 0xdc
-  __TEXT.__swift5_capture: 0x5d4
-  __TEXT.__swift5_types: 0xa8
-  __TEXT.__swift_as_entry: 0xa0
-  __TEXT.__swift_as_ret: 0xac
-  __TEXT.__swift5_mpenum: 0x30
-  __TEXT.__unwind_info: 0x4bb8
-  __TEXT.__eh_frame: 0x36dc
-  __DATA_CONST.__auth_got: 0x1410
-  __DATA_CONST.__got: 0x790
-  __DATA_CONST.__auth_ptr: 0x278
-  __DATA_CONST.__const: 0x76f8
+  __TEXT.__constg_swiftt: 0xacc
+  __TEXT.__swift5_typeref: 0x71a
+  __TEXT.__swift5_reflstr: 0x488
+  __TEXT.__swift5_fieldmd: 0x48c
+  __TEXT.__swift5_builtin: 0xa0
+  __TEXT.__swift5_capture: 0x49c
+  __TEXT.__swift5_types: 0x54
+  __TEXT.__swift_as_entry: 0x5c
+  __TEXT.__swift_as_ret: 0x5c
+  __TEXT.__unwind_info: 0x47f8
+  __TEXT.__eh_frame: 0x2bb4
+  __DATA_CONST.__auth_got: 0x1318
+  __DATA_CONST.__got: 0x758
+  __DATA_CONST.__auth_ptr: 0x1b8
+  __DATA_CONST.__const: 0x6df0
   __DATA_CONST.__cfstring: 0x1cc0
   __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_arraydata: 0x80
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_intobj: 0xa8
-  __DATA.__objc_const: 0x2cb0
-  __DATA.__objc_selrefs: 0x12a8
+  __DATA.__objc_const: 0x2c38
+  __DATA.__objc_selrefs: 0x12b0
   __DATA.__objc_ivar: 0x140
   __DATA.__objc_data: 0x1488
-  __DATA.__data: 0xfb8
-  __DATA.__bss: 0x1000
+  __DATA.__data: 0xf60
+  __DATA.__bss: 0x3e8
   __DATA.__common: 0xa6
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/Frameworks/Speech.framework/Speech
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
+  - /System/Library/PrivateFrameworks/AsyncAlgorithmsInternal.framework/AsyncAlgorithmsInternal
   - /System/Library/PrivateFrameworks/AudioSession.framework/AudioSession
   - /System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore
   - /System/Library/PrivateFrameworks/CarKit.framework/CarKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: ABAC9E9C-5323-353D-A10B-984357D788A3
-  Functions: 3794
-  Symbols:   1134
-  CStrings:  2459
+  UUID: D395AD78-705C-3B01-AEF4-016F24029A6F
+  Functions: 3563
+  Symbols:   1110
+  CStrings:  2456
 
Symbols:
- _os_unfair_lock_lock
- _os_unfair_lock_unlock
- _swift_allocateGenericClassMetadata
- _swift_checkMetadataState
- _swift_continuation_await
- _swift_continuation_init
- _swift_continuation_resume
- _swift_continuation_throwingResume
- _swift_continuation_throwingResumeWithError
- _swift_cvw_allocateGenericValueMetadataWithLayoutString
- _swift_cvw_enumFn_getEnumTag
- _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
- _swift_cvw_initEnumMetadataSingleCaseWithLayoutString
- _swift_cvw_instantiateLayoutString
- _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
- _swift_cvw_multiPayloadEnumGeneric_getEnumTag
- _swift_getEnumCaseMultiPayload
- _swift_getGenericMetadata
- _swift_getTupleTypeLayout2
- _swift_getTupleTypeMetadata2
- _swift_getTupleTypeMetadata3
- _swift_initClassMetadata2
- _swift_storeEnumTagMultiPayload
- _swift_willThrowTypedImpl
CStrings:
+ "SRC:Failed to suppress mic indicator"
+ "SpeechAnalyzer: %s %s firstBestResult %{sensitive}s"
+ "SpeechAnalyzer: %s %s token sausage %{sensitive}s"
+ "result word is an insertion : matches special symbol, do nothing"
+ "setPrefersNoMicrophoneUsageIndicator:error:"
- "Internal inconsistency"
- "base1 base2 base3 "
- "com_apple_SpeechRecognitionCore_speechrecognitiond/ZipStorage.swift"
- "downstreamContinuation result "
- "stateMachine"
- "storage"
- "task upstreams "
- "task upstreams downstreamContinuation "

```
