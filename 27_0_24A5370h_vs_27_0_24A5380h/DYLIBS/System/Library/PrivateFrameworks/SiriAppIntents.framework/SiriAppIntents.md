## SiriAppIntents

> `/System/Library/PrivateFrameworks/SiriAppIntents.framework/SiriAppIntents`

```diff

-  __TEXT.__text: 0x1298da4
+  __TEXT.__text: 0x12a1ab8
   __TEXT.__objc_methlist: 0x300
-  __TEXT.__const: 0x19ca60
-  __TEXT.__swift5_typeref: 0x2a088
-  __TEXT.__swift5_reflstr: 0x42b7c
-  __TEXT.__swift5_assocty: 0x6ff8
-  __TEXT.__constg_swiftt: 0x3c8dc
-  __TEXT.__swift5_fieldmd: 0x4b3e4
+  __TEXT.__const: 0x19d020
+  __TEXT.__swift5_typeref: 0x2a152
+  __TEXT.__swift5_reflstr: 0x42d7c
+  __TEXT.__swift5_assocty: 0x7070
+  __TEXT.__constg_swiftt: 0x3c9bc
+  __TEXT.__swift5_fieldmd: 0x4b578
   __TEXT.__swift5_builtin: 0x258
-  __TEXT.__swift5_proto: 0x12404
-  __TEXT.__swift5_types: 0x38b0
-  __TEXT.__cstring: 0x25517
-  __TEXT.__oslogstring: 0x233d
-  __TEXT.__swift5_capture: 0x1b88
+  __TEXT.__swift5_proto: 0x12444
+  __TEXT.__swift5_types: 0x38c4
+  __TEXT.__cstring: 0x25667
+  __TEXT.__oslogstring: 0x2b7d
+  __TEXT.__swift5_capture: 0x1d08
   __TEXT.__swift5_mpenum: 0x140
-  __TEXT.__swift_as_entry: 0x194
-  __TEXT.__swift_as_ret: 0x1d8
-  __TEXT.__swift_as_cont: 0x324
+  __TEXT.__swift_as_entry: 0x19c
+  __TEXT.__swift_as_ret: 0x1e0
+  __TEXT.__swift_as_cont: 0x32c
   __TEXT.__swift5_protos: 0x30
-  __TEXT.__unwind_info: 0x80bd0
-  __TEXT.__eh_frame: 0xb5e10
+  __TEXT.__unwind_info: 0x7e998
+  __TEXT.__eh_frame: 0xb5edc
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_selrefs: 0x300
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x364c8
-  __AUTH_CONST.__objc_const: 0x25b88
-  __AUTH_CONST.__auth_got: 0x13a0
-  __AUTH.__objc_data: 0x3ca0
-  __AUTH.__data: 0x834b0
-  __DATA.__data: 0x54f18
-  __DATA.__bss: 0x246e90
-  __DATA.__common: 0xa0
+  __AUTH_CONST.__const: 0x36ae0
+  __AUTH_CONST.__objc_const: 0x25bc8
+  __AUTH_CONST.__auth_got: 0x13c0
+  __AUTH.__data: 0x15ab8
+  __DATA.__data: 0x42138
+  __DATA.__bss: 0x235390
+  __DATA.__common: 0x40
+  __DATA_DIRTY.__objc_data: 0x3ca0
+  __DATA_DIRTY.__data: 0x80b00
+  __DATA_DIRTY.__bss: 0x12300
+  __DATA_DIRTY.__common: 0x78
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 203210
+  Functions: 203415
   Symbols:   232
-  CStrings:  4136
+  CStrings:  4168
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__swift5_protos : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
Symbols:
+ _objc_retain_x27
- _swift_willThrowTypedImpl
CStrings:
+ " orphanedRequests="
+ " orphanedResponses="
+ "%{public}s BidirectionalDelegate: Client is missing service entitlement. Rejecting connection."
+ "%{public}s Delegate: Client is missing service entitlement. Rejecting connection."
+ "PrivateCloudMetrics.Inference"
+ "PrivateCloudMetrics.KVCache"
+ "PrivateCloudMetrics.PrefixTrie"
+ "PrivateCloudMetrics.SpeculativeDecode"
+ "PrivateCloudMetrics.TopologicalPrompt"
+ "SiriTrajectory.extractEntries: failed to decode %s: %@"
+ "SiriTrajectory.extractEntries: failed to read %s: %@"
+ "SiriTrajectory.extractEntries: file not found at %s"
+ "SiriTrajectory.extractEntries: kind=entityIdCollision requestID=%s id=%s"
+ "SiriTrajectory.extractEntries: kind=summary entries=%ld decodeFailures=%ld depthCaps=%ld"
+ "SiriTrajectory: Failed to parse GMSPlannerRequestPayload JSON — replacing payload with redactedMarker"
+ "SiriTrajectory: Failed to parse GMSPlannerResponsePayload JSON — replacing payload with redactedMarker"
+ "SiriTrajectory: Failed to parse GMSTranscriptContent from plannerResponse bytes — replacing plannerResponse with sentinel"
+ "SiriTrajectory: Failed to parse SecurityValidationEventPayload JSON — replacing payload with redactedMarker"
+ "SiriTrajectory: Failed to parse SessionResumptionEventBundlePayload JSON — replacing payload with redactedMarker"
+ "SiriTrajectory: Failed to parse TranscriptProtoEvent JSON — replacing payload with redactedMarker"
+ "SiriTrajectory: Failed to re-serialize redacted GMSTranscriptContent for PlannerResponse — replacing plannerResponse with sentinel"
+ "SpanBuilder: GMSPlannerRequest JSON serialization failed plannerID=%s"
+ "SpanBuilder: GMSPlannerResponse JSON serialization failed plannerID=%s"
+ "SpanBuilder: build complete kind=summary events=%ld sessions=%ld spans=%ld srt=%ld replayPayloads=%ld%s"
+ "SpanBuilder: convertToGenAIInputMessages returned nil for %ld GMS event(s)"
+ "SpanBuilder: convertToGenAIOutputMessages returned nil for plannerID %s"
+ "SpanBuilder: convertToGenAIToolDefinitions returned nil for %ld tool(s)"
+ "SpanBuilder: routed %ld AI metrics event(s) to request groups via plannerID"
+ "XPC Client: bidirectional connection established"
+ "XPC Client: opening event stream for session %s"
+ "allowlisted"
+ "passthrough"
+ "siri.voice.expressivity_preset"
+ "siri.voice.pace_preset"
- "full"
- "seed"

```
