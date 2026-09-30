## PerfPowerServicesMetadata

> `/System/Library/PrivateFrameworks/PerfPowerServicesMetadata.framework/PerfPowerServicesMetadata`

```diff

-2954.0.0.502.3
-  __TEXT.__text: 0x3a57c
-  __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_methlist: 0x2554
-  __TEXT.__const: 0xd8
-  __TEXT.__cstring: 0x3e52
-  __TEXT.__oslogstring: 0x1354
-  __TEXT.__gcc_except_tab: 0xfc
+2964.0.40.502.1
+  __TEXT.__text: 0x3b600
+  __TEXT.__auth_stubs: 0x5c0
+  __TEXT.__objc_methlist: 0x25ac
+  __TEXT.__const: 0xe0
+  __TEXT.__cstring: 0x406a
+  __TEXT.__oslogstring: 0x13bf
+  __TEXT.__gcc_except_tab: 0x12c
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x7f8
+  __TEXT.__unwind_info: 0x820
   __TEXT.__objc_classname: 0x466
-  __TEXT.__objc_methname: 0x3110
-  __TEXT.__objc_methtype: 0x519
-  __TEXT.__objc_stubs: 0x3760
+  __TEXT.__objc_methname: 0x323b
+  __TEXT.__objc_methtype: 0x527
+  __TEXT.__objc_stubs: 0x3860
   __DATA_CONST.__got: 0x1e0
   __DATA_CONST.__const: 0x1a0
   __DATA_CONST.__objc_classlist: 0x1e0
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1108
+  __DATA_CONST.__objc_selrefs: 0x1148
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x98
-  __DATA_CONST.__objc_arraydata: 0x1c0
-  __AUTH_CONST.__auth_got: 0x2e8
+  __DATA_CONST.__objc_arraydata: 0x1b0
+  __AUTH_CONST.__auth_got: 0x2f0
   __AUTH_CONST.__const: 0x500
-  __AUTH_CONST.__cfstring: 0x7fe0
-  __AUTH_CONST.__objc_const: 0x4488
-  __AUTH_CONST.__objc_intobj: 0x120
+  __AUTH_CONST.__cfstring: 0x83c0
+  __AUTH_CONST.__objc_const: 0x44b8
+  __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0xc0
-  __AUTH_CONST.__objc_dictobj: 0x370
+  __AUTH_CONST.__objc_dictobj: 0x348
   __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x150
+  __DATA.__objc_ivar: 0x154
   __DATA.__data: 0x120
   __DATA.__bss: 0x90
   __DATA_DIRTY.__objc_data: 0x1040

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 48CB3E3C-12BB-3AFF-B3C7-9D801D389324
-  Functions: 966
-  Symbols:   3183
-  CStrings:  2998
+  UUID: D6087640-3BB5-3FAF-945D-85DD2B55E716
+  Functions: 976
+  Symbols:   3215
+  CStrings:  3073
 
Symbols:
+ +[PPSAudioMetrics songTransitionMetrics]
+ +[PPSCoreRoutineMetrics predictedContextInferenceMetrics]
+ +[PPSCoreRoutineMetrics predictedContextTrainingMetrics]
+ +[PPSMetadataStore getMetadataHistoryForFilepath:subsystem:category:name:].cold.1
+ +[PPSRenderMetrics edrRequestMetrics]
+ -[PPSMetadataStore getMetadataForConcatenatedString:]
+ -[PPSMetadataStore metadataHistoryCache]
+ -[PPSMetadataStore setMetadataForConcatenatedString:result:]
+ -[PPSMetadataStore setMetadataForConcatenatedString:result:].cold.1
+ -[PPSMetadataStore setMetadataHistoryCache:]
+ GCC_except_table10
+ GCC_except_table11
+ GCC_except_table22
+ _OBJC_IVAR_$_PPSMetadataStore._metadataHistoryCache
+ ___block_literal_global.22
+ _objc_msgSend$edrRequestMetrics
+ _objc_msgSend$getMetadataForConcatenatedString:
+ _objc_msgSend$metadataHistoryCache
+ _objc_msgSend$predictedContextInferenceMetrics
+ _objc_msgSend$predictedContextTrainingMetrics
+ _objc_msgSend$setMetadataForConcatenatedString:result:
+ _objc_msgSend$setMetadataHistoryCache:
+ _objc_msgSend$songTransitionMetrics
+ _objc_retain_x25
- GCC_except_table20
CStrings:
+ "%@_%@_%@_%@"
+ "++metricsSync++"
+ "BestMatchedCrossfade"
+ "ClientRegistration"
+ "DeadAirRemoval"
+ "DominantMotionNotification"
+ "EDRRequests"
+ "EntryCount"
+ "HasEmbeddedSIM"
+ "LegacyCrossfade"
+ "Metadata cache is hit"
+ "MetadataMismatchCrossfade"
+ "NavigationNotification"
+ "P"
+ "PUUID"
+ "PeriodicTrigger"
+ "PredictedContextInferenceEvent"
+ "PredictedContextTrainingEvent"
+ "SingleShot"
+ "SmartCrossfade"
+ "SongTransitions"
+ "T@\"NSMutableDictionary\",&,N,V_metadataHistoryCache"
+ "TimeSinceBootEnd"
+ "TimeSinceBootStart"
+ "TransitionDuration"
+ "TransitionProvided"
+ "VisitNotification"
+ "[John] Cache is not empty and concatenatedPath is %@ and cachedHistoryResult is : %@"
+ "_metadataHistoryCache"
+ "edrRequestMetrics"
+ "getMetadataForConcatenatedString:"
+ "headroom"
+ "inferenceLatency"
+ "inferenceTriggerReason"
+ "max_desired_headroom"
+ "metadataHistoryCache"
+ "predictedContextInferenceMetrics"
+ "predictedContextTrainingMetrics"
+ "predictionCount"
+ "process"
+ "request_type"
+ "setMetadataForConcatenatedString:result:"
+ "setMetadataHistoryCache:"
+ "songTransitionMetrics"
+ "trainingDuration"
+ "v32@0:8@16@24"
- "Power"
- "TimeSinceBoot"

```
