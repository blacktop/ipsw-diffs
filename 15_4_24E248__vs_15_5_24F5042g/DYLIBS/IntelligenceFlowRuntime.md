## IntelligenceFlowRuntime

> `/System/Library/PrivateFrameworks/IntelligenceFlowRuntime.framework/Versions/A/IntelligenceFlowRuntime`

```diff

-197.0.8.201.0
-  __TEXT.__text: 0x2854c4
-  __TEXT.__auth_stubs: 0x71e0
+218.3.0.0.0
+  __TEXT.__text: 0x291ce0
+  __TEXT.__auth_stubs: 0x7190
   __TEXT.__objc_methlist: 0x56c
-  __TEXT.__const: 0x10318
-  __TEXT.__cstring: 0x3e1f
-  __TEXT.__oslogstring: 0x715c
-  __TEXT.__swift5_typeref: 0x6d90
-  __TEXT.__constg_swiftt: 0x5458
+  __TEXT.__const: 0x105b0
+  __TEXT.__cstring: 0x3f4f
+  __TEXT.__oslogstring: 0x764c
+  __TEXT.__swift5_typeref: 0x6f92
+  __TEXT.__constg_swiftt: 0x54d4
   __TEXT.__swift5_builtin: 0xa0
-  __TEXT.__swift5_reflstr: 0x319d
-  __TEXT.__swift5_fieldmd: 0x48f4
-  __TEXT.__swift5_types: 0x658
-  __TEXT.__swift5_proto: 0x1024
+  __TEXT.__swift5_reflstr: 0x32cd
+  __TEXT.__swift5_fieldmd: 0x499c
+  __TEXT.__swift5_types: 0x664
+  __TEXT.__swift5_proto: 0x104c
   __TEXT.__swift5_protos: 0xc4
-  __TEXT.__swift_as_entry: 0x494
-  __TEXT.__swift_as_ret: 0x4fc
-  __TEXT.__swift5_capture: 0x2eb0
+  __TEXT.__swift_as_entry: 0x4a0
+  __TEXT.__swift_as_ret: 0x50c
+  __TEXT.__swift5_capture: 0x2f88
   __TEXT.__swift5_mpenum: 0x30
   __TEXT.__swift5_assocty: 0x4a0
-  __TEXT.__unwind_info: 0x7778
-  __TEXT.__eh_frame: 0x1116c
+  __TEXT.__unwind_info: 0x78b0
+  __TEXT.__eh_frame: 0x114ec
   __TEXT.__objc_classname: 0x4c
-  __TEXT.__objc_methname: 0xe61
+  __TEXT.__objc_methname: 0xe4f
   __TEXT.__objc_methtype: 0xeb
-  __DATA_CONST.__got: 0x1e80
-  __DATA_CONST.__const: 0x250
+  __DATA_CONST.__got: 0x1e78
+  __DATA_CONST.__const: 0x260
   __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x438
+  __DATA_CONST.__objc_selrefs: 0x428
   __DATA_CONST.__objc_protorefs: 0x60
-  __AUTH_CONST.__auth_got: 0x38f0
-  __AUTH_CONST.__auth_ptr: 0x1928
-  __AUTH_CONST.__const: 0xd9c8
-  __AUTH_CONST.__objc_const: 0x2e38
+  __AUTH_CONST.__auth_got: 0x38c8
+  __AUTH_CONST.__auth_ptr: 0x1948
+  __AUTH_CONST.__const: 0xdd50
+  __AUTH_CONST.__objc_const: 0x2e58
   __AUTH.__objc_data: 0xbb8
-  __AUTH.__data: 0x6188
-  __DATA.__data: 0x5f78
-  __DATA.__bss: 0x1e9b0
+  __AUTH.__data: 0x62c8
+  __DATA.__data: 0x6018
+  __DATA.__bss: 0x1eeb0
   __DATA.__common: 0x218
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine
   - /System/Library/Frameworks/CoreSpotlight.framework/Versions/A/CoreSpotlight
   - /System/Library/Frameworks/CryptoKit.framework/Versions/A/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
-  - /System/Library/Frameworks/Intents.framework/Versions/A/Intents
   - /System/Library/Frameworks/NaturalLanguage.framework/Versions/A/NaturalLanguage
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/Versions/A/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/Versions/A/BiomeStreams

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 12878
-  Symbols:   224
-  CStrings:  954
+  Functions: 13123
+  Symbols:   223
+  CStrings:  971
 
Symbols:
- _OBJC_CLASS_$_INPerson
CStrings:
+ "%s call was made with %@"
+ "/AppleInternal/Library/BuildRoots/7049eb08-072a-11f0-8f70-122ba06eff56/Library/Caches/com.apple.xbs/Sources/IntelligenceFlowRuntime/IntelligenceFlowRuntime/Planner/StandardPlanner.swift"
+ "Cannot log to FeatureStore since executorSELFContext is nil"
+ "DefaultRuntime: Alternative executor is not required. Returning result."
+ "DefaultRuntime: Ignoring returned payload in favor of previous result based on GAT intent output."
+ "DefaultRuntime: Received request to use previous GAT response but the previous result was not a success"
+ "DefaultRuntime: Received request to use previous GAT response but the previous result was not from GAT"
+ "DefaultRuntime: Received request to use previous GAT response but there was no previous response"
+ "DefaultRuntime: Skipping post-processing of GAT intent due to missing properties"
+ "DefaultRuntime: Skipping post-processing of GAT intent due to unexpected return value"
+ "Emitting `ifPlanCycleGenerated` with ifRequestId: %s and planCycleId: %s"
+ "No type information available on the input search entity"
+ "PlanGenerationError"
+ "PlanOverridesService failed with error %s. Proceeding _without_ failing the request"
+ "QueryDecorationXPCServiceServer found previousQueries: %s"
+ "QueryDecorationXPCServiceServer: client %s is missing group-identifier entitlement, no previous queries can be found as seurity policy check can't be completed without a group identifier."
+ "QueryDecorationXPCServiceServer: could not find observable session transcript with SessionID: %s."
+ "Search returned empty results type. Returning empty results with in app search string: %s"
+ "Sending a tuple interaction to Biome..."
+ "Sent a tuple interaction to Biome"
+ "SessionCoordinator found ongoing span to be terminated: %s for participant: %s"
+ "Span %s for participant %s was cancelled while in queue. Skipping accept"
+ "__alternativeExecutorRequired"
+ "__contentReferenceOverride"
+ "_generatePlan(action:sessionState:)"
+ "com.apple.generativeassistanttools.GenerativeAssistantExtension"
+ "emptyPlaceholder"
+ "planCycleIdSeedString"
+ "requestAmendment"
+ "rewrittenRequest"
- "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IntelligenceFlowRuntime/IntelligenceFlowRuntime/Planner/StandardPlanner.swift"
- "ContactSearcher found no candidates"
- "ContactSearcher results post-filtering: %s"
- "ContactSearcher results: %s"
- "FeedbackLearningBiomeDonator#donateInteractionTuples: Sending tupleInteraction to Biome..."
- "FeedbackLearningBiomeDonator#donateInteractionTuples: Sent tupleInteraction to Biome"
- "Initialized PersonCandidateGenerator"
- "No candidates had valid email addresses."
- "No candidates had valid phone numbers."
- "Running PersonCandidateGenerator"
- "participantAlias"
- "personHandle"
- "type"

```
