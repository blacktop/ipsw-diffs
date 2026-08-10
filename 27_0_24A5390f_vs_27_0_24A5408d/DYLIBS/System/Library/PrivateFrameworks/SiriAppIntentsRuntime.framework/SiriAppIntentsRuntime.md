## SiriAppIntentsRuntime

> `/System/Library/PrivateFrameworks/SiriAppIntentsRuntime.framework/SiriAppIntentsRuntime`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH.__objc_data`

```diff

-3600.82.20.0.0
-  __TEXT.__text: 0x815b4
+3600.82.29.0.0
+  __TEXT.__text: 0x86c20
   __TEXT.__objc_methlist: 0x404
-  __TEXT.__const: 0x2808
-  __TEXT.__cstring: 0x14b1
-  __TEXT.__constg_swiftt: 0xca4
-  __TEXT.__swift5_typeref: 0x1385
-  __TEXT.__swift5_reflstr: 0xcf6
-  __TEXT.__swift5_fieldmd: 0x940
-  __TEXT.__oslogstring: 0x348d
+  __TEXT.__const: 0x29b0
+  __TEXT.__cstring: 0x14f1
+  __TEXT.__constg_swiftt: 0xd7c
+  __TEXT.__swift5_typeref: 0x1495
+  __TEXT.__swift5_reflstr: 0xd43
+  __TEXT.__swift5_fieldmd: 0x9a8
+  __TEXT.__oslogstring: 0x37bd
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_types: 0xb4
-  __TEXT.__swift_as_entry: 0x1cc
-  __TEXT.__swift_as_ret: 0x17c
-  __TEXT.__swift_as_cont: 0x2ec
+  __TEXT.__swift5_types: 0xbc
+  __TEXT.__swift_as_entry: 0x214
+  __TEXT.__swift_as_ret: 0x1d0
+  __TEXT.__swift_as_cont: 0x36c
   __TEXT.__swift5_proto: 0x104
-  __TEXT.__swift5_capture: 0x1880
+  __TEXT.__swift5_capture: 0x19cc
   __TEXT.__swift5_assocty: 0x98
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x1ac0
-  __TEXT.__eh_frame: 0x4818
+  __TEXT.__unwind_info: 0x1ca0
+  __TEXT.__eh_frame: 0x50d0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x170
-  __DATA_CONST.__objc_classlist: 0x70
+  __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x440
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x4648
-  __AUTH_CONST.__objc_const: 0xcd0
-  __AUTH_CONST.__auth_got: 0x18e8
+  __AUTH_CONST.__const: 0x4898
+  __AUTH_CONST.__objc_const: 0xee0
+  __AUTH_CONST.__auth_got: 0x1960
   __AUTH.__objc_data: 0xa0
-  __AUTH.__data: 0x570
-  __DATA.__data: 0x828
+  __AUTH.__data: 0x6c8
+  __DATA.__data: 0x8a8
   __DATA.__bss: 0x1400
-  __DATA.__common: 0x88
-  __DATA_DIRTY.__objc_data: 0x9d8
-  __DATA_DIRTY.__data: 0xd28
+  __DATA.__common: 0x90
+  __DATA_DIRTY.__objc_data: 0x9c0
+  __DATA_DIRTY.__data: 0xd68
   __DATA_DIRTY.__bss: 0xb80
-  __DATA_DIRTY.__common: 0x110
+  __DATA_DIRTY.__common: 0x100
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2905
-  Symbols:   216
-  CStrings:  337
+  Functions: 3038
+  Symbols:   220
+  CStrings:  346
 
Symbols:
+ _objc_release_x1
+ _swift_asyncLet_begin
+ _swift_asyncLet_finish
+ _swift_asyncLet_get
+ _swift_deletedAsyncMethodErrorTu
- _swift_retain_x9
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
