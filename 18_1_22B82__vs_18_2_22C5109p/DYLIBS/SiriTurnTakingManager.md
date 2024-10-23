## SiriTurnTakingManager

> `/System/Library/PrivateFrameworks/SiriTurnTakingManager.framework/SiriTurnTakingManager`

```diff

-3401.1.1.0.0
-  __TEXT.__text: 0x21dc8
-  __TEXT.__auth_stubs: 0x10b0
-  __TEXT.__objc_methlist: 0xf0
-  __TEXT.__const: 0x1064
-  __TEXT.__cstring: 0xd18
-  __TEXT.__swift5_typeref: 0x57e
-  __TEXT.__swift5_fieldmd: 0x9d8
-  __TEXT.__constg_swiftt: 0xa20
-  __TEXT.__swift5_reflstr: 0x505
-  __TEXT.__swift5_capture: 0x1c4
-  __TEXT.__oslogstring: 0x1b12
+3402.11.1.0.0
+  __TEXT.__text: 0x2454c
+  __TEXT.__auth_stubs: 0x1130
+  __TEXT.__objc_methlist: 0x108
+  __TEXT.__const: 0x10f4
+  __TEXT.__cstring: 0xe78
+  __TEXT.__swift5_typeref: 0x5f2
+  __TEXT.__swift5_fieldmd: 0xa34
+  __TEXT.__constg_swiftt: 0xac0
+  __TEXT.__swift5_reflstr: 0x595
+  __TEXT.__swift5_capture: 0x264
+  __TEXT.__oslogstring: 0x1ca2
   __TEXT.__swift5_protos: 0x1c
-  __TEXT.__swift5_proto: 0xc8
-  __TEXT.__swift5_types: 0x98
+  __TEXT.__swift5_proto: 0xd0
+  __TEXT.__swift5_types: 0xa0
   __TEXT.__swift5_assocty: 0x48
-  __TEXT.__unwind_info: 0x778
-  __TEXT.__eh_frame: 0x790
-  __TEXT.__objc_methname: 0x502
-  __DATA_CONST.__got: 0x238
-  __DATA_CONST.__const: 0x128
-  __DATA_CONST.__objc_classlist: 0x70
+  __TEXT.__unwind_info: 0x878
+  __TEXT.__eh_frame: 0x828
+  __TEXT.__objc_methname: 0x54b
+  __DATA_CONST.__got: 0x260
+  __DATA_CONST.__const: 0x148
+  __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x248
-  __AUTH_CONST.__auth_got: 0x858
-  __AUTH_CONST.__auth_ptr: 0x260
-  __AUTH_CONST.__const: 0x16e8
-  __AUTH_CONST.__objc_const: 0x858
-  __AUTH.__objc_data: 0x1f8
-  __DATA.__data: 0x1c8
-  __DATA.__bss: 0xf00
-  __DATA.__common: 0x20
+  __DATA_CONST.__objc_selrefs: 0x260
+  __AUTH_CONST.__auth_got: 0x898
+  __AUTH_CONST.__auth_ptr: 0x278
+  __AUTH_CONST.__const: 0x1808
+  __AUTH_CONST.__objc_const: 0x930
+  __AUTH.__objc_data: 0x308
+  __AUTH.__data: 0x180
+  __DATA.__data: 0x218
+  __DATA.__bss: 0xf80
+  __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x410
   __DATA_DIRTY.__data: 0x8c0
   __DATA_DIRTY.__common: 0x78

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
+  - /System/Library/PrivateFrameworks/CDMFoundation.framework/CDMFoundation
   - /System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech
   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
   - /System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 878
-  Symbols:   466
-  CStrings:  281
+  Functions: 963
+  Symbols:   490
+  CStrings:  300
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_initStructMetadata
+ _swift_storeEnumTagSinglePayloadGeneric
- _objc_retain_x10
- _objc_retain_x11
CStrings:
+ "    siriIntendedInfo for NC has invocationSource - %!@(MISSING) , spkrIdScore - %!f(MISSING), aftmScore - %!f(MISSING),\n    odldScore - %!f(MISSING), lrnnScore - %!f(MISSING), conversationalScore - %!f(MISSING)"
+ "\", activeRequestState: \""
+ "%!s(MISSING) override matched, skipping other overrides"
+ ", isProcessing:\""
+ ", nlRoutingDecision: \""
+ "Active Request State = %!s(MISSING)"
+ "Candidate request arrived while active request is processing; recommending .mitigate"
+ "Candidate request routed to siriX while active request is processing; Use model decision for mitigation"
+ "Running ConcurrentActiveRequestMatcher override"
+ "_TtC21SiriTurnTakingManager20TTActiveRequestState"
+ "_TtC21SiriTurnTakingManager30ConcurrentActiveRequestMatcher"
+ "concurrentActiveRequestMatcher"
+ "conversationalOdldScore"
+ "executionSource"
+ "executionSource:"
+ "isExecutionInProgress"
+ "matchedUseModelDecision"
+ "overrideDecision is unknown"
+ "setConversationalNldaScore:"
+ "setIsConversational:"
- "siriIntendedInfo for NC has invocationSource - %!@(MISSING) , spkrIdScore - %!f(MISSING), aftmScore - %!f(MISSING), odldScore - %!f(MISSING), lrnnScore - %!f(MISSING)"

```
