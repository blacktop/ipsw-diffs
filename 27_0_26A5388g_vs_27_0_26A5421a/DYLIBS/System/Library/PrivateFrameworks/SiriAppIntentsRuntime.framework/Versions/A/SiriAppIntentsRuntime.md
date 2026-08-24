## SiriAppIntentsRuntime

> `/System/Library/PrivateFrameworks/SiriAppIntentsRuntime.framework/Versions/A/SiriAppIntentsRuntime`

```diff

-3600.82.20.0.0
-  __TEXT.__text: 0x8081c
+3600.82.29.0.0
+  __TEXT.__text: 0x85eec
   __TEXT.__objc_methlist: 0x404
-  __TEXT.__const: 0x27f8
-  __TEXT.__cstring: 0x1641
-  __TEXT.__constg_swiftt: 0xca4
-  __TEXT.__swift5_typeref: 0x1345
-  __TEXT.__swift5_reflstr: 0xcf6
-  __TEXT.__swift5_fieldmd: 0x940
-  __TEXT.__oslogstring: 0x326d
+  __TEXT.__const: 0x29a0
+  __TEXT.__cstring: 0x1681
+  __TEXT.__constg_swiftt: 0xd7c
+  __TEXT.__swift5_typeref: 0x1455
+  __TEXT.__swift5_reflstr: 0xd43
+  __TEXT.__swift5_fieldmd: 0x9a8
+  __TEXT.__oslogstring: 0x359d
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_types: 0xb4
-  __TEXT.__swift_as_entry: 0x1cc
-  __TEXT.__swift_as_ret: 0x17c
-  __TEXT.__swift_as_cont: 0x2f4
+  __TEXT.__swift5_types: 0xbc
+  __TEXT.__swift_as_entry: 0x214
+  __TEXT.__swift_as_ret: 0x1d0
+  __TEXT.__swift_as_cont: 0x374
   __TEXT.__swift5_proto: 0x104
-  __TEXT.__swift5_capture: 0x16c0
+  __TEXT.__swift5_capture: 0x180c
   __TEXT.__swift5_assocty: 0x98
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x1ac0
-  __TEXT.__eh_frame: 0x4848
+  __TEXT.__unwind_info: 0x1ca8
+  __TEXT.__eh_frame: 0x5100
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x178
-  __DATA_CONST.__objc_classlist: 0x70
+  __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x3f8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x4238
-  __AUTH_CONST.__objc_const: 0xcd0
-  __AUTH_CONST.__auth_got: 0x1770
+  __AUTH_CONST.__const: 0x4488
+  __AUTH_CONST.__objc_const: 0xee0
+  __AUTH_CONST.__auth_got: 0x17e8
   __AUTH.__objc_data: 0xa0
-  __AUTH.__data: 0x570
-  __DATA.__data: 0x828
+  __AUTH.__data: 0x6c8
+  __DATA.__data: 0x8a8
   __DATA.__bss: 0x1400
-  __DATA.__common: 0x88
-  __DATA_DIRTY.__objc_data: 0x9d8
-  __DATA_DIRTY.__data: 0xcf8
+  __DATA.__common: 0x90
+  __DATA_DIRTY.__objc_data: 0x9c0
+  __DATA_DIRTY.__data: 0xd38
   __DATA_DIRTY.__bss: 0xb80
-  __DATA_DIRTY.__common: 0x110
+  __DATA_DIRTY.__common: 0x100
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2863
-  Symbols:   168
-  CStrings:  331
+  Functions: 2993
+  Symbols:   172
+  CStrings:  340
 
Symbols:
+ _swift_asyncLet_begin
+ _swift_asyncLet_finish
+ _swift_asyncLet_get
+ _swift_deletedAsyncMethodErrorTu
CStrings:
+ "AIR: inferenceMetrics timeToFirstToken=%s extendLatency=%s totalInferenceTime=%s cachedTokens=%s inputTokens=%s outputTokens=%s thinkingTokens=%s firstTokenPreprocessingMs=%s"
+ "SecurityValidationEventProto"
+ "SessionManager teardown timed out; a Biome subscription may still be live. (rdar://181864363)"
+ "Starting to listen for SecurityValidationEventProto events."
+ "awaitWithTimeout(_:)"
+ "createEventStream: Biome subscription fan-out cancelled."
+ "createEventStream: Biome subscription fan-out failed: %@"
+ "listenSecurityValidationEventsProto: kind=emptyIDs — proto delivered a SecurityValidationEvent with no session/turn/query IDs. The vendored proto may not match IF's wire format (rdar://182856486); falling back to interactionId scoping, reintroducing the fragile lookup this change removes."
+ "listenSecurityValidationEventsProto: kind=streamEnded"
+ "retrieveAppleIntelligenceReportingInvocationStep(for:from:until:continuation:)"
+ "retrieveSecurityValidationEventsProto: kind=summary matched=%ld emptyIDs=%ld total=%ld sessionID=%s"
- "AIR: inferenceMetrics timeToFirstToken=%s extendLatency=%s totalInferenceTime=%s cachedTokens=%s inputTokens=%s outputTokens=%s"
- "Cannot send utterance: no active session. Call startSession() first."
```
