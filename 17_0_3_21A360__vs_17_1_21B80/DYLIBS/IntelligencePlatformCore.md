## IntelligencePlatformCore

> `/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/IntelligencePlatformCore`

```diff

-75.0.3.2.0
-  __TEXT.__text: 0xaa3810
-  __TEXT.__auth_stubs: 0x8fa0
+75.3.2.1.0
+  __TEXT.__text: 0xabbda0
+  __TEXT.__auth_stubs: 0x8fb0
   __TEXT.__objc_methlist: 0x1524
-  __TEXT.__const: 0x58d99
-  __TEXT.__swift5_typeref: 0x1958e
-  __TEXT.__cstring: 0x540d2
-  __TEXT.__constg_swiftt: 0x1e0b4
-  __TEXT.__swift5_reflstr: 0x2310c
-  __TEXT.__swift5_fieldmd: 0x1e1d4
+  __TEXT.__const: 0x59e39
+  __TEXT.__swift5_typeref: 0x1974c
+  __TEXT.__cstring: 0x54b62
+  __TEXT.__constg_swiftt: 0x1e5bc
+  __TEXT.__swift5_reflstr: 0x239cc
+  __TEXT.__swift5_fieldmd: 0x1e610
   __TEXT.__swift5_builtin: 0x424
   __TEXT.__swift5_mpenum: 0xf0
   __TEXT.__swift5_assocty: 0x2f18
-  __TEXT.__swift5_proto: 0x4ca8
-  __TEXT.__swift5_types: 0x1bb0
-  __TEXT.__swift5_protos: 0x310
-  __TEXT.__swift5_capture: 0x2d90
+  __TEXT.__swift5_proto: 0x4d0c
+  __TEXT.__swift5_types: 0x1bd0
+  __TEXT.__swift5_protos: 0x314
+  __TEXT.__swift5_capture: 0x2dfc
   __TEXT.__gcc_except_tab: 0xe8
   __TEXT.__oslogstring: 0x385
   __TEXT.__dlopen_cstrs: 0xc0
-  __TEXT.__unwind_info: 0x28d1c
-  __TEXT.__eh_frame: 0x54964
+  __TEXT.__unwind_info: 0x28c1c
+  __TEXT.__eh_frame: 0x552bc
   __TEXT.__objc_classname: 0x470
-  __TEXT.__objc_methname: 0x8958
-  __TEXT.__objc_methtype: 0x1f4d
+  __TEXT.__objc_methname: 0x8966
+  __TEXT.__objc_methtype: 0x1f6d
   __TEXT.__objc_stubs: 0x1160
-  __DATA_CONST.__got: 0x3448
+  __DATA_CONST.__got: 0x3558
   __DATA_CONST.__const: 0x780
-  __DATA_CONST.__objc_classlist: 0xf98
+  __DATA_CONST.__objc_classlist: 0xfb0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x28b08
+  __DATA_CONST.__objc_const: 0x29280
   __DATA_CONST.__objc_selrefs: 0x1c48
-  __AUTH_CONST.__const: 0x3b638
+  __AUTH_CONST.__const: 0x3b960
   __AUTH_CONST.__objc_const: 0x10d0
   __AUTH_CONST.__cfstring: 0x320
-  __AUTH_CONST.__auth_got: 0x47e0
-  __AUTH.__objc_data: 0x3d70
-  __AUTH.__data: 0x19da0
+  __AUTH_CONST.__auth_got: 0x47e8
+  __AUTH.__objc_data: 0x3e10
+  __AUTH.__data: 0x1a5b8
   __DATA.__objc_protorefs: 0x108
   __DATA.__objc_classrefs: 0x758
   __DATA.__objc_superrefs: 0x80
   __DATA.__objc_ivar: 0xc4
-  __DATA.__data: 0x187c8
-  __DATA.__bss: 0x61240
-  __DATA.__common: 0x1ad8
+  __DATA.__data: 0x18af8
+  __DATA.__bss: 0x61e50
+  __DATA.__common: 0x1b60
   __DATA_DIRTY.__const: 0x130
   __DATA_DIRTY.__objc_const: 0x90
   __DATA_DIRTY.__objc_data: 0x29f8
-  __DATA_DIRTY.__data: 0x1ced0
+  __DATA_DIRTY.__data: 0x1cef0
   __DATA_DIRTY.__bss: 0x218a0
   __DATA_DIRTY.__common: 0x1288
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /System/Library/PrivateFrameworks/PegasusKit.framework/PegasusKit
   - /System/Library/PrivateFrameworks/PersonalizationPortrait.framework/PersonalizationPortrait
   - /System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats
+  - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/ProactiveEventTracker.framework/ProactiveEventTracker
   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0F42FE58-6F7A-3BD1-B20D-FEFE1BB33786
-  Functions: 69900
-  Symbols:   755
-  CStrings:  8654
+  UUID: FE25F867-8F63-3099-846C-67F2AA5E0733
+  Functions: 70441
+  Symbols:   757
+  CStrings:  8707
 
Symbols:
+ _PPSCreateTelemetryIdentifier
+ _PPSSendTelemetry
CStrings:
+ " (entityType, entityIdentifier, featurizationDate, isRelevant, numberOfInteractions, queryName, metadata, "
+ " where entityType in ("
+ "%s: Running Entity Relevance data collection."
+ ")\nVALUES (:entityType, :entityIdentifier, :featurizationDate, :isRelevant, :numberOfInteractions, :queryName, :metadata, "
+ "@\"<BMMediaRemoteLibrary>\"16@0:8"
+ "EntityRelevanceDataCollection"
+ "EntityRelevanceDataCollection Fetched: %ld rows"
+ "EntityRelevanceDataCollection: %s does not have keypath defined"
+ "EntityRelevanceDataCollection: message logged to PET2"
+ "EntityRelevanceEvaluationSampleProvider: totalPositiveSamples == 0. found %ld negative samples for %s and %s"
+ "EntityRelevanceEvaluationSampleProvider: totalPositiveSamples > 0. found %ld negative samples for %s and %s"
+ "MediaRemote"
+ "PowerLog"
+ "ViewUpdate: PowerLog: %s"
+ "_TtC24IntelligencePlatformCore33EntityRelevanceDataCollectionTask"
+ "_TtC24IntelligencePlatformCore33EntityRelevanceDataCollectionView"
+ "_TtCV24IntelligencePlatformCore38EntityRelevanceEntityRelevanceFeaturesP33_1772DF20CAD99C453A3113A83A9C8C6313_StorageClass"
+ "_behaviorPopularityGivenContextCoarseGeoHash"
+ "_behaviorPopularityGivenContextCoarseTimeOfDay"
+ "_behaviorPopularityGivenContextDayOfWeek"
+ "_behaviorPopularityGivenContextLoi"
+ "_behaviorPopularityGivenContextSpecificGeoHash"
+ "_behaviorPopularityGivenContextWifi"
+ "_contextPopularityGivenBehaviorCoarseGeoHash"
+ "_contextPopularityGivenBehaviorCoarseTimeOfDay"
+ "_contextPopularityGivenBehaviorDayOfWeek"
+ "_contextPopularityGivenBehaviorLoi"
+ "_contextPopularityGivenBehaviorSpecificGeoHash"
+ "_contextPopularityGivenBehaviorWifi"
+ "_posteriorProbabilityGivenContextCoarseGeoHash"
+ "_posteriorProbabilityGivenContextCoarseGeoHashCoarseTimeOfDay"
+ "_posteriorProbabilityGivenContextCoarseTimeOfDay"
+ "_posteriorProbabilityGivenContextCoarseTimeOfDayDayOfWeek"
+ "_posteriorProbabilityGivenContextCoarseTimeOfDaySpecificGeoHash"
+ "_posteriorProbabilityGivenContextCoarseTimeOfDayWifi"
+ "_posteriorProbabilityGivenContextDayOfWeek"
+ "_posteriorProbabilityGivenContextDayOfWeekSpecificGeoHash"
+ "_posteriorProbabilityGivenContextDayOfWeekWifi"
+ "_posteriorProbabilityGivenContextLoi"
+ "_posteriorProbabilityGivenContextSpecificGeoHash"
+ "_posteriorProbabilityGivenContextWifi"
+ "behaviorPopularityGivenContext_wifi"
+ "commuteConfidenceThreshold"
+ "defaultDecayHalfLife"
+ "deviceLanguageSamePredictedLanguages50Bool"
+ "deviceLanguageSamePredictedLanguagesBool"
+ "deviceLanguageSamePredictedLanguagesHigherThan50Bool"
+ "entityInformation"
+ "entityRelevanceDataCollection"
+ "et.EntityInformation"
+ "et.EntityRelevanceFeatures"
+ "isRelevant"
+ "negativeSampleRateIfNoPositives"
+ "posteriorProbabilityGivenContext:coarseGeoHash"
+ "posteriorProbabilityGivenContext:dayOfWeek+specificGeoHash"
+ "posteriorProbabilityGivenContext_coarseGeoHash"
+ "posteriorProbabilityGivenContext_dayOfWeekSpecificGeoHash"
+ "viewConfig"
- " (entityType, featurizationDate, isRelevant, numberOfInteractions, queryName, "
- ")\nVALUES (:entityType, :featurizationDate, :isRelevant, :numberOfInteractions, :queryName, "
- "EntityRelevanceEvaluationSampleProvider: found %ld negative samples for %s and %s"
- "deviceLanguageSamePredictedLanguages"
- "different"
- "same"

```
