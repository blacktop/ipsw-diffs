## PhotoAnalysis

> `/System/Library/PrivateFrameworks/PhotoAnalysis.framework/Versions/A/PhotoAnalysis`

```diff

-700.27.103.0.0
-  __TEXT.__text: 0x1e6490
-  __TEXT.__auth_stubs: 0x3170
-  __TEXT.__objc_methlist: 0x4e40
-  __TEXT.__const: 0x59d0
-  __TEXT.__cstring: 0xef1c
-  __TEXT.__constg_swiftt: 0x2b88
-  __TEXT.__swift5_typeref: 0x2b86
-  __TEXT.__swift5_reflstr: 0x260b
-  __TEXT.__swift5_fieldmd: 0x2380
-  __TEXT.__swift5_capture: 0x21fc
-  __TEXT.__oslogstring: 0xd50d
-  __TEXT.__swift5_builtin: 0x140
-  __TEXT.__swift5_assocty: 0x438
-  __TEXT.__swift5_proto: 0x498
-  __TEXT.__swift5_types: 0x204
+700.21.101.0.0
+  __TEXT.__text: 0x1d1ab8
+  __TEXT.__auth_stubs: 0x2ec0
+  __TEXT.__objc_methlist: 0x4e48
+  __TEXT.__const: 0x5460
+  __TEXT.__cstring: 0xea2f
+  __TEXT.__constg_swiftt: 0x297c
+  __TEXT.__swift5_typeref: 0x29cc
+  __TEXT.__swift5_reflstr: 0x23bb
+  __TEXT.__swift5_fieldmd: 0x2178
+  __TEXT.__swift5_capture: 0x2124
+  __TEXT.__oslogstring: 0xce3d
+  __TEXT.__swift5_builtin: 0x12c
+  __TEXT.__swift5_assocty: 0x3d8
+  __TEXT.__swift5_proto: 0x45c
+  __TEXT.__swift5_types: 0x1e4
   __TEXT.__swift5_mpenum: 0x58
-  __TEXT.__swift5_protos: 0x44
+  __TEXT.__swift5_protos: 0x3c
   __TEXT.__gcc_except_tab: 0x1810
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x7798
-  __TEXT.__eh_frame: 0x1301c
-  __TEXT.__objc_classname: 0x10c7
-  __TEXT.__objc_methname: 0x1485e
-  __TEXT.__objc_methtype: 0x2c6a
-  __TEXT.__objc_stubs: 0xc720
-  __DATA_CONST.__got: 0x1bb8
-  __DATA_CONST.__const: 0xcc0
-  __DATA_CONST.__objc_classlist: 0x560
+  __TEXT.__unwind_info: 0x6f78
+  __TEXT.__eh_frame: 0x120d8
+  __TEXT.__objc_classname: 0x10ea
+  __TEXT.__objc_methname: 0x147b8
+  __TEXT.__objc_methtype: 0x2c4c
+  __TEXT.__objc_stubs: 0xc7e0
+  __DATA_CONST.__got: 0x1b30
+  __DATA_CONST.__const: 0xcb8
+  __DATA_CONST.__objc_classlist: 0x548
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x1a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4270
+  __DATA_CONST.__objc_selrefs: 0x4220
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x210
-  __DATA_CONST.__objc_arraydata: 0xf8
-  __AUTH_CONST.__auth_got: 0x18d0
-  __AUTH_CONST.__auth_ptr: 0xa78
-  __AUTH_CONST.__const: 0x8d50
+  __DATA_CONST.__objc_arraydata: 0xd8
+  __AUTH_CONST.__auth_got: 0x1778
+  __AUTH_CONST.__auth_ptr: 0xa60
+  __AUTH_CONST.__const: 0x89a8
   __AUTH_CONST.__cfstring: 0x7ee0
-  __AUTH_CONST.__objc_const: 0x10c28
+  __AUTH_CONST.__objc_const: 0x10828
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x708
-  __AUTH_CONST.__objc_arrayobj: 0x168
+  __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH.__objc_data: 0x2930
-  __AUTH.__data: 0x5180
-  __DATA.__objc_ivar: 0x4f8
-  __DATA.__data: 0x4038
-  __DATA.__bss: 0x8f98
-  __DATA.__common: 0x280
+  __AUTH.__objc_data: 0x2840
+  __AUTH.__data: 0x4e40
+  __DATA.__objc_ivar: 0x4f4
+  __DATA.__data: 0x3d20
+  __DATA.__bss: 0x8918
+  __DATA.__common: 0x270
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__common: 0x50
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/CoreLocation.framework/Versions/A/CoreLocation
   - /System/Library/Frameworks/CoreML.framework/Versions/A/CoreML
-  - /System/Library/Frameworks/CryptoKit.framework/Versions/A/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/ImageIO.framework/Versions/A/ImageIO
   - /System/Library/Frameworks/Photos.framework/Versions/A/Photos

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7330
-  Symbols:   7534
-  CStrings:  1796
+  Functions: 7079
+  Symbols:   7493
+  CStrings:  1768
 
Symbols:
+ +[PHAJournalPromptSuggestionShim promptFromContextString:]
+ -[PHAHighlightEnrichmentTask didProduceContent]
+ -[PHAMemoryElectionTask didProduceContent]
+ -[PHAStorytellingClientRequestHandler(Pet) requestUpdatePetIdentitiesWithOptions:context:reply:]
+ -[PHAStorytellingClientRequestHandler(Pet) updatePetIdentityWithProcessor:errors:]
+ -[PHASuggestionGenerationTask didProduceContent]
+ -[PHAWallpaperSuggestionGenerationWeeklyTask didProduceContent]
+ GCC_except_table1056
+ GCC_except_table1110
+ GCC_except_table1125
+ GCC_except_table1132
+ GCC_except_table1133
+ GCC_except_table1185
+ GCC_except_table1191
+ GCC_except_table1298
+ GCC_except_table1530
+ GCC_except_table1662
+ GCC_except_table1677
+ GCC_except_table1725
+ GCC_except_table577
+ GCC_except_table585
+ GCC_except_table676
+ GCC_except_table750
+ GCC_except_table758
+ GCC_except_table792
+ GCC_except_table811
+ GCC_except_table830
+ GCC_except_table971
+ GCC_except_table990
+ OBJC_IVAR_$_PHAHighlightEnrichmentTask._didProduceContent
+ OBJC_IVAR_$_PHAMemoryElectionTask._didProduceContent
+ OBJC_IVAR_$_PHASuggestionGenerationTask._didProduceContent
+ _NSMultipleUnderlyingErrorsKey
+ _OBJC_$_PROP_LIST_PHASuggestionGenerationTask.319
+ _OBJC_CLASS_$_PGGraphPetIdentityProcessorCache
+ _OBJC_CLASS_$_PHAJournalPromptSuggestionShim
+ _OBJC_METACLASS_$_PHAJournalPromptSuggestionShim
+ _PLPhotoAnalysisPetOptionsResultKey
+ __84-[PHALocalNotificationInterface fireLocalNotificationWithOptions:completionHandler:]_block_invoke.6
+ __86-[PHAUserFeedbackUpdater _enrichKeyAssetsforHighlightsWithNegativeFeedbackWithAssets:]_block_invoke.350
+ __Block_byref_object_copy_.1074
+ __Block_byref_object_copy_.1247
+ __Block_byref_object_copy_.1364
+ __Block_byref_object_copy_.1734
+ __Block_byref_object_copy_.1968
+ __Block_byref_object_copy_.2240
+ __Block_byref_object_copy_.2767
+ __Block_byref_object_copy_.4982
+ __Block_byref_object_copy_.596
+ __Block_byref_object_copy_.6294
+ __Block_byref_object_copy_.6874
+ __Block_byref_object_copy_.7108
+ __Block_byref_object_dispose_.1075
+ __Block_byref_object_dispose_.1248
+ __Block_byref_object_dispose_.1365
+ __Block_byref_object_dispose_.1735
+ __Block_byref_object_dispose_.1969
+ __Block_byref_object_dispose_.2241
+ __Block_byref_object_dispose_.2768
+ __Block_byref_object_dispose_.4983
+ __Block_byref_object_dispose_.597
+ __Block_byref_object_dispose_.6295
+ __Block_byref_object_dispose_.6875
+ __Block_byref_object_dispose_.7109
+ __OBJC_$_CLASS_METHODS_PHAJournalPromptSuggestionShim
+ __OBJC_$_CLASS_METHODS_PHAStorytellingClientRequestHandler(Graph|Discoverability|UserFeedback|MLModel|Person|Curation|UpNext|Face|Music|Pet|Highlight|Related|Sharing|Title|Memory|Prototype|PFL|CPAnalytics|OneUpRelated|Defaults|Suggestion)
+ __OBJC_$_INSTANCE_METHODS_PHAStorytellingClientRequestHandler(Graph|Discoverability|UserFeedback|MLModel|Person|Curation|UpNext|Face|Music|Pet|Highlight|Related|Sharing|Title|Memory|Prototype|PFL|CPAnalytics|OneUpRelated|Defaults|Suggestion)
+ __OBJC_CLASS_PROTOCOLS_$_PHAStorytellingClientRequestHandler(Graph|Discoverability|UserFeedback|MLModel|Person|Curation|UpNext|Face|Music|Pet|Highlight|Related|Sharing|Title|Memory|Prototype|PFL|CPAnalytics|OneUpRelated|Defaults|Suggestion)
+ __OBJC_CLASS_RO_$_PHAJournalPromptSuggestionShim
+ __OBJC_METACLASS_RO_$_PHAJournalPromptSuggestionShim
+ ___96-[PHAStorytellingClientRequestHandler(Pet) requestUpdatePetIdentitiesWithOptions:context:reply:]_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e24_v16?0"PGGraphEnabler"8l
+ ___swift_memcpy56_8
+ __block_literal_global.10025
+ __block_literal_global.1089
+ __block_literal_global.1300
+ __block_literal_global.1335
+ __block_literal_global.1553
+ __block_literal_global.1825
+ __block_literal_global.1966
+ __block_literal_global.198.2451
+ __block_literal_global.199.6505
+ __block_literal_global.2
+ __block_literal_global.200.2083
+ __block_literal_global.200.3945
+ __block_literal_global.200.4428
+ __block_literal_global.200.7685
+ __block_literal_global.200.8377
+ __block_literal_global.200.853
+ __block_literal_global.203.2454
+ __block_literal_global.2078
+ __block_literal_global.2447
+ __block_literal_global.260.8919
+ __block_literal_global.2729
+ __block_literal_global.2897
+ __block_literal_global.300.8906
+ __block_literal_global.3427
+ __block_literal_global.353
+ __block_literal_global.3871
+ __block_literal_global.3940
+ __block_literal_global.419.8834
+ __block_literal_global.4423
+ __block_literal_global.4767
+ __block_literal_global.4980
+ __block_literal_global.5312
+ __block_literal_global.602
+ __block_literal_global.6228
+ __block_literal_global.6501
+ __block_literal_global.7276
+ __block_literal_global.7680
+ __block_literal_global.8
+ __block_literal_global.8372
+ __block_literal_global.848
+ __block_literal_global.8935
+ __block_literal_global.979
+ __block_literal_global.9861
+ _objc_msgSend$initWithDetectionType:photoLibrary:graph:loggingConnection:cache:
+ _objc_msgSend$initWithGraph:
+ _objc_msgSend$pl_analysisErrorWithCode:localizedDescription:userInfo:
+ _objc_msgSend$textString
+ _objc_msgSend$underlyingErrors
+ _objc_msgSend$updatePetIdentityWithError:progressBlock:
+ _objc_msgSend$updatePetIdentityWithProcessor:errors:
+ block_copy_helper.114
+ block_copy_helper.132
+ block_copy_helper.160
+ block_copy_helper.170
+ block_copy_helper.179
+ block_copy_helper.188
+ block_copy_helper.204
+ block_copy_helper.247
+ block_copy_helper.276
+ block_copy_helper.305
+ block_copy_helper.334
+ block_copy_helper.363
+ block_copy_helper.392
+ block_copy_helper.420
+ block_descriptor.116
+ block_descriptor.134
+ block_descriptor.162
+ block_descriptor.172
+ block_descriptor.181
+ block_descriptor.190
+ block_descriptor.206
+ block_descriptor.249
+ block_descriptor.278
+ block_descriptor.307
+ block_descriptor.336
+ block_descriptor.365
+ block_descriptor.39
+ block_descriptor.394
+ block_descriptor.422
+ block_descriptor.423
+ block_destroy_helper.115
+ block_destroy_helper.133
+ block_destroy_helper.161
+ block_destroy_helper.171
+ block_destroy_helper.180
+ block_destroy_helper.189
+ block_destroy_helper.205
+ block_destroy_helper.248
+ block_destroy_helper.277
+ block_destroy_helper.306
+ block_destroy_helper.335
+ block_destroy_helper.364
+ block_destroy_helper.393
+ block_destroy_helper.421
+ objectdestroy.227Tm
+ objectdestroy.438Tm
+ objectdestroy.448Tm
+ objectdestroy.458Tm
- -[PHAHighlightEnrichmentTask featureAvailable]
- -[PHAHighlightEnrichmentTask featureComplete]
- -[PHAMemoryElectionTask featureAvailable]
- -[PHASuggestionGenerationTask featureAvailable]
- -[PHAWallpaperSuggestionGenerationWeeklyTask featureAvailable]
- GCC_except_table1053
- GCC_except_table1107
- GCC_except_table1121
- GCC_except_table1122
- GCC_except_table1129
- GCC_except_table1179
- GCC_except_table1188
- GCC_except_table1295
- GCC_except_table1527
- GCC_except_table1659
- GCC_except_table1674
- GCC_except_table1722
- GCC_except_table574
- GCC_except_table582
- GCC_except_table673
- GCC_except_table747
- GCC_except_table755
- GCC_except_table789
- GCC_except_table808
- GCC_except_table827
- GCC_except_table968
- GCC_except_table984
- OBJC_IVAR_$_PHAHighlightEnrichmentTask._featureAvailable
- OBJC_IVAR_$_PHAHighlightEnrichmentTask._featureComplete
- OBJC_IVAR_$_PHAMemoryElectionTask._featureAvailable
- OBJC_IVAR_$_PHASuggestionGenerationTask._featureAvailable
- _OBJC_$_PROP_LIST_PHASuggestionGenerationTask.321
- _OBJC_CLASS_$_MOContextContactMetaData
- _OBJC_CLASS_$_MOContextLocationMetaData
- _OBJC_CLASS_$_MOContextMusicMetaData
- _OBJC_CLASS_$_MOContextStringUpdateOptions
- _OBJC_CLASS_$_MOContextTimeMetaData
- _PHAMetricsTaskHealthKeyTaskFeatureCompleteDuration
- __84-[PHALocalNotificationInterface fireLocalNotificationWithOptions:completionHandler:]_block_invoke.33
- __86-[PHAUserFeedbackUpdater _enrichKeyAssetsforHighlightsWithNegativeFeedbackWithAssets:]_block_invoke.336
- __Block_byref_object_copy_.1092
- __Block_byref_object_copy_.1254
- __Block_byref_object_copy_.1360
- __Block_byref_object_copy_.1748
- __Block_byref_object_copy_.1989
- __Block_byref_object_copy_.2243
- __Block_byref_object_copy_.2769
- __Block_byref_object_copy_.5001
- __Block_byref_object_copy_.600
- __Block_byref_object_copy_.6313
- __Block_byref_object_copy_.6898
- __Block_byref_object_copy_.7134
- __Block_byref_object_dispose_.1093
- __Block_byref_object_dispose_.1255
- __Block_byref_object_dispose_.1361
- __Block_byref_object_dispose_.1749
- __Block_byref_object_dispose_.1990
- __Block_byref_object_dispose_.2244
- __Block_byref_object_dispose_.2770
- __Block_byref_object_dispose_.5002
- __Block_byref_object_dispose_.601
- __Block_byref_object_dispose_.6314
- __Block_byref_object_dispose_.6899
- __Block_byref_object_dispose_.7135
- __DATA__TtC13PhotoAnalysis23PromptSuggestionQUCache
- __DATA__TtC13PhotoAnalysis25PromptSuggestionAnnotator
- __DATA__TtC13PhotoAnalysis27PromptSuggestionQUProcessor
- __DATA__TtC13PhotoAnalysis48PromptSuggestionMeaningfulEventGroundingProvider
- __IVARS__TtC13PhotoAnalysis23PromptSuggestionQUCache
- __IVARS__TtC13PhotoAnalysis25PromptSuggestionAnnotator
- __IVARS__TtC13PhotoAnalysis27PromptSuggestionQUProcessor
- __IVARS__TtC13PhotoAnalysis48PromptSuggestionMeaningfulEventGroundingProvider
- __METACLASS_DATA__TtC13PhotoAnalysis23PromptSuggestionQUCache
- __METACLASS_DATA__TtC13PhotoAnalysis25PromptSuggestionAnnotator
- __METACLASS_DATA__TtC13PhotoAnalysis27PromptSuggestionQUProcessor
- __METACLASS_DATA__TtC13PhotoAnalysis48PromptSuggestionMeaningfulEventGroundingProvider
- __OBJC_$_CLASS_METHODS_PHAStorytellingClientRequestHandler(Graph|Discoverability|UserFeedback|MLModel|Person|Curation|UpNext|Face|Music|Highlight|Related|Sharing|Title|Memory|Prototype|PFL|CPAnalytics|OneUpRelated|Defaults|Suggestion)
- __OBJC_$_INSTANCE_METHODS_PHAStorytellingClientRequestHandler(Graph|Discoverability|UserFeedback|MLModel|Person|Curation|UpNext|Face|Music|Highlight|Related|Sharing|Title|Memory|Prototype|PFL|CPAnalytics|OneUpRelated|Defaults|Suggestion)
- __OBJC_CLASS_PROTOCOLS_$_PHAStorytellingClientRequestHandler(Graph|Discoverability|UserFeedback|MLModel|Person|Curation|UpNext|Face|Music|Highlight|Related|Sharing|Title|Memory|Prototype|PFL|CPAnalytics|OneUpRelated|Defaults|Suggestion)
- ___swift_memcpy152_8
- ___swift_memcpy64_8
- __block_literal_global.10050
- __block_literal_global.1110
- __block_literal_global.1307
- __block_literal_global.1337
- __block_literal_global.1558
- __block_literal_global.1848
- __block_literal_global.198.2459
- __block_literal_global.1987
- __block_literal_global.199.6524
- __block_literal_global.200.2086
- __block_literal_global.200.3952
- __block_literal_global.200.4436
- __block_literal_global.200.7709
- __block_literal_global.200.8395
- __block_literal_global.200.861
- __block_literal_global.203.2462
- __block_literal_global.2081
- __block_literal_global.2455
- __block_literal_global.260.8942
- __block_literal_global.27.1325
- __block_literal_global.2728
- __block_literal_global.2893
- __block_literal_global.300.8930
- __block_literal_global.339
- __block_literal_global.3428
- __block_literal_global.35
- __block_literal_global.3878
- __block_literal_global.3947
- __block_literal_global.419.8856
- __block_literal_global.4431
- __block_literal_global.4781
- __block_literal_global.4999
- __block_literal_global.5338
- __block_literal_global.607
- __block_literal_global.6247
- __block_literal_global.6520
- __block_literal_global.7299
- __block_literal_global.7704
- __block_literal_global.8390
- __block_literal_global.856
- __block_literal_global.8958
- __block_literal_global.9882
- __block_literal_global.999
- _associated conformance 13PhotoAnalysis10LLMQUParseVSHAASQ
- _associated conformance 13PhotoAnalysis23PromptSuggestionFetcherC12MCSuggestionV0C8MetadataVSHAASQ
- _associated conformance 13PhotoAnalysis48PromptSuggestionMeaningfulEventGroundingProviderC5Error33_690D087D3592F999307496CB2C4BD94CLLOSHAASQ
- _associated conformance So26MOContextStringContentTypeVs10SetAlgebraSCSQ
- _associated conformance So26MOContextStringContentTypeVs10SetAlgebraSCs25ExpressibleByArrayLiteral
- _associated conformance So26MOContextStringContentTypeVs9OptionSetSCSY
- _associated conformance So26MOContextStringContentTypeVs9OptionSetSCs0F7Algebra
- _objc_msgSend$hasCompletedEnrichmentForLibrary:
- _swift_stdlib_random
- _symbolic $s13PhotoAnalysis31PromptSuggestionQUCacheProviderP
- _symbolic $s13PhotoAnalysis34PromptSuggestionAnnotationProviderP
- _symbolic SDySSShySSGG
- _symbolic SDySS_____GSg 13PhotoAnalysis10LLMQUParseV
- _symbolic SDy_____SDySSShySSGGG 18PhotosIntelligence10QueryTokenV
- _symbolic SDy__________G 18PhotosIntelligence10QueryTokenV AA36MeaningfulEventMomentGroundingResultV
- _symbolic Si6offset______3key_SaySSG5valuet7elementtSg 13PhotoAnalysis23PromptSuggestionFetcherC12MCSuggestionV0C0V
- _symbolic SuSg
- _symbolic _____ 13PhotoAnalysis10LLMQUParseV
- _symbolic _____ 13PhotoAnalysis23PromptSuggestionFetcherC12MCSuggestionV0C8MetadataV
- _symbolic _____ 13PhotoAnalysis23PromptSuggestionQUCacheC
- _symbolic _____ 13PhotoAnalysis25PromptSuggestionAnnotatorC
- _symbolic _____ 13PhotoAnalysis27PromptSuggestionQUProcessorC
- _symbolic _____ 13PhotoAnalysis48PromptSuggestionMeaningfulEventGroundingProviderC
- _symbolic _____ 13PhotoAnalysis48PromptSuggestionMeaningfulEventGroundingProviderC5Error33_690D087D3592F999307496CB2C4BD94CLLO
- _symbolic _____ So26MOContextStringContentTypeV
- _symbolic ______p 10Foundation15ContiguousBytesP
- _symbolic ______p 13PhotoAnalysis31PromptSuggestionQUCacheProviderP
- _symbolic ______p 13PhotoAnalysis34PromptSuggestionAnnotationProviderP
- _symbolic ______pSg 10Foundation15ContiguousBytesP
- _symbolic _____ySS_SStG s23_ContiguousArrayStorageC
- _symbolic _____ySS_____G s18_DictionaryStorageC 13PhotoAnalysis10LLMQUParseV
- _symbolic _____y_____G s23_ContiguousArrayStorageC 18PhotosIntelligence15QueryAnnotationV
- _symbolic _____y_____G s23_ContiguousArrayStorageC 7ToolKit10TypedValueO
- _symbolic _____y______SSSgtG s23_ContiguousArrayStorageC So26MOContextStringContentTypeV
- block_copy_helper.119
- block_copy_helper.126
- block_copy_helper.142
- block_copy_helper.149
- block_copy_helper.167
- block_copy_helper.195
- block_copy_helper.205
- block_copy_helper.214
- block_copy_helper.223
- block_copy_helper.239
- block_copy_helper.282
- block_copy_helper.311
- block_copy_helper.340
- block_copy_helper.369
- block_copy_helper.398
- block_copy_helper.427
- block_copy_helper.455
- block_descriptor.121
- block_descriptor.128
- block_descriptor.144
- block_descriptor.151
- block_descriptor.169
- block_descriptor.197
- block_descriptor.207
- block_descriptor.216
- block_descriptor.225
- block_descriptor.241
- block_descriptor.284
- block_descriptor.313
- block_descriptor.342
- block_descriptor.371
- block_descriptor.400
- block_descriptor.429
- block_descriptor.457
- block_descriptor.458
- block_descriptor.50
- block_destroy_helper.120
- block_destroy_helper.127
- block_destroy_helper.143
- block_destroy_helper.150
- block_destroy_helper.168
- block_destroy_helper.196
- block_destroy_helper.206
- block_destroy_helper.215
- block_destroy_helper.224
- block_destroy_helper.240
- block_destroy_helper.283
- block_destroy_helper.312
- block_destroy_helper.341
- block_destroy_helper.370
- block_destroy_helper.399
- block_destroy_helper.428
- block_destroy_helper.456
- objectdestroy.262Tm
- objectdestroy.473Tm
- objectdestroy.483Tm
- objectdestroy.493Tm
CStrings:
+ "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Swift/workspaces/photoanalysis/PhotoAnalysis/Framework/Storytelling/PHASuggestionController.m"
+ "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Swift/workspaces/photoanalysis/PhotoAnalysis/Framework/Storytelling/Tasks/AnalyticsTasks/PHACachingCPAnalyticsPropertiesTask.m"
+ "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Swift/workspaces/photoanalysis/PhotoAnalysis/Framework/Storytelling/Tasks/AnalyticsTasks/PHAFeaturesUsageReportingTask.m"
+ "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Swift/workspaces/photoanalysis/PhotoAnalysis/Framework/Storytelling/Tasks/AnalyticsTasks/PHAMediaSampleReportingTask.m"
+ "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Swift/workspaces/photoanalysis/PhotoAnalysis/Framework/Storytelling/Tasks/PHAMetricReportingTask.m"
+ "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Swift/workspaces/photoanalysis/PhotoAnalysis/Framework/Storytelling/Tasks/PHAPhotosChallengeTask.m"
+ "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Swift/workspaces/photoanalysis/PhotoAnalysis/Framework/Storytelling/Tasks/PHASyndicationTask.m"
+ "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Swift/workspaces/photoanalysis/PhotoAnalysis/Framework/Storytelling/Tasks/SharedLibraryTasks/PHACameraSmartSharingTask.m"
+ "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Swift/workspaces/photoanalysis/PhotoAnalysis/Framework/Storytelling/Tasks/SharedLibraryTasks/PHASharedLibrarySuggestionGenerationTask.m"
+ "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Swift/workspaces/photoanalysis/PhotoAnalysis/Framework/Storytelling/Tasks/SuggestionTasks/PHASuggestionGenerationTask.m"
+ "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Swift/workspaces/photoanalysis/PhotoAnalysis/Framework/Storytelling/Tasks/SuggestionTasks/PHAWallpaperSettlingEffectGenerationTask.m"
+ "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/Photos_Swift/workspaces/photoanalysis/PhotoAnalysis/Framework/Storytelling/Tasks/SuggestionTasks/PHAWallpaperSuggestionGenerationNightlyTask.m"
+ "Failed to run requestUpdatePetIdentitiesWithOptions"
+ "PetsParity"
- "\n    timeReferenceString: "
- "$__lazy_storage_$_promptSuggestionLLMQUParse"
- "--- Prompt Metadata ---\n    contactName: "
- "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Swift/workspaces/photoanalysis/PhotoAnalysis/Framework/Storytelling/PHASuggestionController.m"
- "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Swift/workspaces/photoanalysis/PhotoAnalysis/Framework/Storytelling/Tasks/AnalyticsTasks/PHACachingCPAnalyticsPropertiesTask.m"
- "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Swift/workspaces/photoanalysis/PhotoAnalysis/Framework/Storytelling/Tasks/AnalyticsTasks/PHAFeaturesUsageReportingTask.m"
- "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Swift/workspaces/photoanalysis/PhotoAnalysis/Framework/Storytelling/Tasks/AnalyticsTasks/PHAMediaSampleReportingTask.m"
- "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Swift/workspaces/photoanalysis/PhotoAnalysis/Framework/Storytelling/Tasks/PHAMetricReportingTask.m"
- "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Swift/workspaces/photoanalysis/PhotoAnalysis/Framework/Storytelling/Tasks/PHAPhotosChallengeTask.m"
- "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Swift/workspaces/photoanalysis/PhotoAnalysis/Framework/Storytelling/Tasks/PHASyndicationTask.m"
- "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Swift/workspaces/photoanalysis/PhotoAnalysis/Framework/Storytelling/Tasks/SharedLibraryTasks/PHACameraSmartSharingTask.m"
- "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Swift/workspaces/photoanalysis/PhotoAnalysis/Framework/Storytelling/Tasks/SharedLibraryTasks/PHASharedLibrarySuggestionGenerationTask.m"
- "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Swift/workspaces/photoanalysis/PhotoAnalysis/Framework/Storytelling/Tasks/SuggestionTasks/PHASuggestionGenerationTask.m"
- "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Swift/workspaces/photoanalysis/PhotoAnalysis/Framework/Storytelling/Tasks/SuggestionTasks/PHAWallpaperSettlingEffectGenerationTask.m"
- "/AppleInternal/Library/BuildRoots/81e2abef-3955-11ef-8e67-e2437461156c/Library/Caches/com.apple.xbs/Sources/Photos_Swift/workspaces/photoanalysis/PhotoAnalysis/Framework/Storytelling/Tasks/SuggestionTasks/PHAWallpaperSuggestionGenerationNightlyTask.m"
- "LLMQUPrompts-1-05282024-photoanalysisd"
- "LLMQUPrompts-2-05282024-photoanalysisd"
- "MomentBasedGroundingAndAssetsFetchingProcessor.locationAssetUUIDs"
- "PromptSuggestionAnnotationProvider"
- "PromptSuggestionFetcher"
- "PromptSuggestionMeaningfulEventGroundingProvider"
- "PromptSuggestionMeaningfulEventGroundingProvider.meaningfulEventResultByQueryToken"
- "PromptSuggestionQUCache"
- "PromptSuggestionQUProcessor"
- "_TtC13PhotoAnalysis23PromptSuggestionQUCache"
- "_TtC13PhotoAnalysis25PromptSuggestionAnnotator"
- "_TtC13PhotoAnalysis27PromptSuggestionQUProcessor"
- "_TtC13PhotoAnalysis48PromptSuggestionMeaningfulEventGroundingProvider"
- "annotationProvider"
- "com.apple.omniSearch.SearchToolExtension.SearchToolControl"
- "com.apple.omniSearch.SearchToolExtension.SearchToolMCGrounding"
- "featureCheckpoint"
- "featureCompleteInterval"
- "locationAssetUUIDs"
- "locationAssetUUIDs is stuck"
- "prewarmMemoryCreationQU"
- "quCache"
- "quProcessor"
- "queryunderstanding"
- "requestPrewarmQueryAnnotator"
- "requestPrewarmQueryAnnotator is stuck"
- "taskFeatureCompleteDuration"

```
