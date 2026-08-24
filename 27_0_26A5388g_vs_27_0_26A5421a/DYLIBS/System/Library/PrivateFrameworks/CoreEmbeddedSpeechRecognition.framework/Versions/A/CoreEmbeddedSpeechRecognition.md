## CoreEmbeddedSpeechRecognition

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/Versions/A/CoreEmbeddedSpeechRecognition`

```diff

-3600.70.32.0.0
-  __TEXT.__text: 0x3186f8
-  __TEXT.__objc_methlist: 0x4940
-  __TEXT.__const: 0x8298
-  __TEXT.__dlopen_cstrs: 0x6c
-  __TEXT.__swift5_typeref: 0x41f3
-  __TEXT.__cstring: 0xd24e
-  __TEXT.__constg_swiftt: 0x25fc
-  __TEXT.__swift5_reflstr: 0x26b2
-  __TEXT.__swift5_fieldmd: 0x2518
+3600.70.47.0.0
+  __TEXT.__text: 0x323764
+  __TEXT.__objc_methlist: 0x4a58
+  __TEXT.__const: 0x82f0
+  __TEXT.__dlopen_cstrs: 0xdc
+  __TEXT.__swift5_typeref: 0x412a
+  __TEXT.__cstring: 0xd732
+  __TEXT.__constg_swiftt: 0x2648
+  __TEXT.__swift5_reflstr: 0x2753
+  __TEXT.__swift5_fieldmd: 0x2570
   __TEXT.__swift5_builtin: 0x208
   __TEXT.__swift5_assocty: 0x4e0
   __TEXT.__swift5_proto: 0x4cc
-  __TEXT.__swift5_types: 0x280
-  __TEXT.__oslogstring: 0xc384
-  __TEXT.__swift5_capture: 0xc334
+  __TEXT.__swift5_types: 0x284
+  __TEXT.__oslogstring: 0xc61c
+  __TEXT.__swift5_capture: 0xc7a4
   __TEXT.__swift5_protos: 0x20
-  __TEXT.__swift_as_entry: 0x258
-  __TEXT.__swift_as_ret: 0x2bc
-  __TEXT.__swift_as_cont: 0x69c
+  __TEXT.__swift_as_entry: 0x264
+  __TEXT.__swift_as_ret: 0x2c4
+  __TEXT.__swift_as_cont: 0x6b4
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__gcc_except_tab: 0xbc0
+  __TEXT.__gcc_except_tab: 0xc6c
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x4588
-  __TEXT.__eh_frame: 0x5718
+  __TEXT.__unwind_info: 0x46a0
+  __TEXT.__eh_frame: 0x5840
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x800
-  __DATA_CONST.__objc_classlist: 0x418
+  __DATA_CONST.__const: 0x840
+  __DATA_CONST.__objc_classlist: 0x428
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3460
+  __DATA_CONST.__objc_selrefs: 0x3518
   __DATA_CONST.__objc_protorefs: 0x98
-  __DATA_CONST.__objc_superrefs: 0x1f8
+  __DATA_CONST.__objc_superrefs: 0x200
   __DATA_CONST.__objc_arraydata: 0x470
-  __DATA_CONST.__got: 0x1a28
-  __AUTH_CONST.__const: 0x23238
-  __AUTH_CONST.__cfstring: 0x49c0
-  __AUTH_CONST.__objc_const: 0xb2a0
-  __AUTH_CONST.__objc_intobj: 0xdb0
+  __DATA_CONST.__got: 0x1a38
+  __AUTH_CONST.__const: 0x23dd0
+  __AUTH_CONST.__cfstring: 0x4aa0
+  __AUTH_CONST.__objc_const: 0xb470
+  __AUTH_CONST.__objc_intobj: 0xea0
   __AUTH_CONST.__objc_arrayobj: 0x2a0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x2140
-  __AUTH.__objc_data: 0x1090
-  __AUTH.__data: 0xaf0
-  __DATA.__objc_ivar: 0x4fc
-  __DATA.__data: 0x2260
-  __DATA.__bss: 0x5748
-  __DATA.__common: 0x148
-  __DATA_DIRTY.__objc_data: 0x1b68
-  __DATA_DIRTY.__data: 0x3b28
+  __AUTH_CONST.__auth_got: 0x2150
+  __AUTH.__objc_data: 0x10e0
+  __AUTH.__data: 0xb88
+  __DATA.__objc_ivar: 0x50c
+  __DATA.__data: 0x2318
+  __DATA.__bss: 0x5798
+  __DATA.__common: 0x168
+  __DATA_DIRTY.__objc_data: 0x1b70
+  __DATA_DIRTY.__data: 0x3ab8
   __DATA_DIRTY.__bss: 0x3ef0
   __DATA_DIRTY.__common: 0x238
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio

   - /System/Library/PrivateFrameworks/CacheDelete.framework/Versions/A/CacheDelete
   - /System/Library/PrivateFrameworks/CascadeSets.framework/Versions/A/CascadeSets
   - /System/Library/PrivateFrameworks/CollectionsInternal.framework/Versions/A/CollectionsInternal
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreDuet.framework/Versions/A/CoreDuet
   - /System/Library/PrivateFrameworks/CoreRoutine.framework/Versions/A/CoreRoutine
   - /System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/Versions/A/CoreSpeechFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10306
-  Symbols:   6062
-  CStrings:  2292
+  Functions: 10493
+  Symbols:   6152
+  CStrings:  2331
 
Symbols:
+ +[CESRDiagnosticReporter sharedInstance]
+ +[CESRSpeechItemRanker_ASRRankedEntityTerm getRank:forItem:]
+ +[CESRSpeechProfileSelfHelper _cascadeEntitySourcesFromEnrolledCounts:]
+ +[CESRSpeechProfileSelfHelper _updateReasonForTrigger:]
+ -[CESRDiagnosticReporter .cxx_destruct]
+ -[CESRDiagnosticReporter _submitASRIssueReport:withContext:]
+ -[CESRDiagnosticReporter init]
+ -[CESRDiagnosticReporter queue]
+ -[CESRDiagnosticReporter reporter]
+ -[CESRDiagnosticReporter setQueue:]
+ -[CESRDiagnosticReporter setReporter:]
+ -[CESRDiagnosticReporter submitASRIssueReport:withContext:]
+ -[CESRDiagnosticReporter submitASRIssueReportAsync:withContext:]
+ -[CESRSpeechProfileBuilder beginWithCategoriesAndVersions:trigger:error:]
+ -[CESRSpeechProfileMetrics addEnrolledEntitiesCount:forCascadeFieldType:]
+ -[CESRSpeechProfileMetrics addEnrolledEntityForCascadeFieldType:]
+ -[CESRSpeechProfileMetrics numEnrolledEntitiesPerCascadeFieldType]
+ -[CESRSpeechProfileMetrics setSpeechProfileSize:]
+ -[CESRSpeechProfileMetrics speechProfileSize]
+ -[CESRSpeechProfileSelfHelper logASRSpeechProfileUpdateEndedWithTotalNumEntitiesReceived:entityMetrics:entityCleanupMetrics:entityExtractionMetrics:cascadeEntitySources:speechProfileSize:]
+ -[CESRSpeechProfileSelfHelper logASRSpeechProfileUpdateStartedWithTrigger:]
+ -[CESRSpeechProfileSiteManager _rebuildAllSites:trigger:]
+ -[CESRSpeechProfileSiteManager _rebuildSiteAtURL:shouldDefer:trigger:]
+ -[CESRSpeechProfileSiteManager _resetAndRebuildAllSitesWithTrigger:]
+ -[CESRSpeechProfileSiteWriter rebuildRequiredProfileInstances:trigger:]
+ -[CESRSpeechProfileUpdater rebuildCategoryGroup:withSets:version:trigger:totalItems:error:]
+ GCC_except_table1067
+ GCC_except_table1076
+ GCC_except_table1193
+ GCC_except_table1257
+ GCC_except_table1258
+ GCC_except_table1259
+ GCC_except_table1260
+ GCC_except_table1261
+ GCC_except_table1262
+ GCC_except_table1267
+ GCC_except_table1297
+ GCC_except_table1418
+ GCC_except_table1423
+ GCC_except_table1427
+ GCC_except_table1473
+ GCC_except_table1481
+ GCC_except_table1486
+ GCC_except_table1490
+ GCC_except_table222
+ GCC_except_table292
+ GCC_except_table306
+ GCC_except_table343
+ GCC_except_table360
+ GCC_except_table391
+ GCC_except_table418
+ GCC_except_table422
+ GCC_except_table483
+ GCC_except_table504
+ GCC_except_table547
+ GCC_except_table556
+ GCC_except_table658
+ GCC_except_table663
+ GCC_except_table666
+ GCC_except_table670
+ GCC_except_table673
+ GCC_except_table676
+ GCC_except_table679
+ GCC_except_table682
+ GCC_except_table685
+ GCC_except_table688
+ GCC_except_table774
+ GCC_except_table801
+ GCC_except_table858
+ OBJC_IVAR_$_CESRDiagnosticReporter._queue
+ OBJC_IVAR_$_CESRDiagnosticReporter._reporter
+ OBJC_IVAR_$_CESRSpeechProfileMetrics._numEnrolledEntitiesPerCascadeFieldType
+ OBJC_IVAR_$_CESRSpeechProfileMetrics._speechProfileSize
+ SymptomDiagnosticReporterLibraryCore.frameworkLibrary
+ _AnalyticsSendEventLazy
+ _CESRSpeechProfileUpdateTriggerSiriLanguageChanged
+ _CESRSpeechProfileUpdateTriggerTrialExperiment
+ _OBJC_CLASS_$_ASRSpeechProfileSchemaASRSpeechProfileCascadeEntitySource
+ _OBJC_CLASS_$_CESRDiagnosticReporter
+ _OBJC_METACLASS_$_CESRDiagnosticReporter
+ _SymptomDiagnosticReporterLibrary
+ __73-[CESRSpeechProfileBuilder beginWithCategoriesAndVersions:trigger:error:]_block_invoke
+ __DATA__TtC29CoreEmbeddedSpeechRecognition25CESREntityRankingCAHelper
+ __METACLASS_DATA__TtC29CoreEmbeddedSpeechRecognition25CESREntityRankingCAHelper
+ __OBJC_$_CLASS_METHODS_CESRDiagnosticReporter
+ __OBJC_$_CLASS_METHODS_CESRSpeechItemRanker_ASRRankedEntityTerm
+ __OBJC_$_INSTANCE_METHODS_CESRDiagnosticReporter
+ __OBJC_$_INSTANCE_VARIABLES_CESRDiagnosticReporter
+ __OBJC_$_PROP_LIST_CESRDiagnosticReporter
+ __OBJC_CLASS_RO_$_CESRDiagnosticReporter
+ __OBJC_METACLASS_RO_$_CESRDiagnosticReporter
+ ___40+[CESRDiagnosticReporter sharedInstance]_block_invoke
+ ___55+[CESRSpeechProfileSelfHelper _updateReasonForTrigger:]_block_invoke
+ ___57-[CESRSpeechProfileSiteManager _rebuildAllSites:trigger:]_block_invoke
+ ___60-[CESRDiagnosticReporter _submitASRIssueReport:withContext:]_block_invoke
+ ___64-[CESRDiagnosticReporter submitASRIssueReportAsync:withContext:]_block_invoke
+ ___73-[CESRSpeechProfileBuilder beginWithCategoriesAndVersions:trigger:error:]_block_invoke
+ ___91-[CESRSpeechProfileUpdater rebuildCategoryGroup:withSets:version:trigger:totalItems:error:]_block_invoke
+ ___SymptomDiagnosticReporterLibraryCore_block_invoke
+ ___block_descriptor_40_e8_32s_e22_v16?0"NSDictionary"8l
+ ___block_descriptor_56_e8_32s40s48bs_e15_B16?0"NSURL"8l
+ ___block_descriptor_80_e8_32s40bs48r56r64r72r_e39_B32?0"CCSharedItem"8"NSString"16^24l
+ ___copy_helper_block_e8_32s40b48r56r64r72r
+ ___destroy_helper_block_e8_32s40s48r56r64r72r
+ ___getSDRDiagnosticReporterClass_block_invoke
+ ___getkSymptomDiagnosticReplyReasonStringSymbolLoc_block_invoke
+ ___getkSymptomDiagnosticReplyReasonSymbolLoc_block_invoke
+ ___getkSymptomDiagnosticReplySuccessSymbolLoc_block_invoke
+ ___swift_memcpy33_8
+ ___swift_memcpy49_8
+ _audit_stringSymptomDiagnosticReporter
+ _dlerror
+ _dlsym
+ _kCESRDiagnosticReporterASRSnapshotTime
+ _kCESRDiagnosticReporterASRTypeKey
+ _kCESRDiagnosticReporterCancelPreviousRecognitionTimeout
+ _kCESRDiagnosticReporterDomainKey
+ _objc_msgSend$_cascadeEntitySourcesFromEnrolledCounts:
+ _objc_msgSend$_localeIdentifier
+ _objc_msgSend$_rebuildAllSites:trigger:
+ _objc_msgSend$_rebuildSiteAtURL:shouldDefer:trigger:
+ _objc_msgSend$_resetAndRebuildAllSitesWithTrigger:
+ _objc_msgSend$_speechProfileSiteURL
+ _objc_msgSend$_submitASRIssueReport:withContext:
+ _objc_msgSend$_updateReasonForTrigger:
+ _objc_msgSend$addEnrolledEntitiesCount:forCascadeFieldType:
+ _objc_msgSend$beginWithCategoriesAndVersions:trigger:completion:
+ _objc_msgSend$beginWithCategoriesAndVersions:trigger:error:
+ _objc_msgSend$getRank:forItem:
+ _objc_msgSend$initWithSpeechProfileSiteURL:localeIdentifier:
+ _objc_msgSend$logASRSpeechProfileUpdateEndedWithTotalNumEntitiesReceived:entityMetrics:entityCleanupMetrics:entityExtractionMetrics:cascadeEntitySources:speechProfileSize:
+ _objc_msgSend$numEnrolledEntitiesPerCascadeFieldType
+ _objc_msgSend$predicateWithFieldType:equalsStringValue:error:
+ _objc_msgSend$processName
+ _objc_msgSend$queue
+ _objc_msgSend$rebuildCategoryGroup:withSets:version:trigger:totalItems:error:
+ _objc_msgSend$rebuildRequiredProfileInstances:trigger:
+ _objc_msgSend$reporter
+ _objc_msgSend$setCascadeEntitySources:
+ _objc_msgSend$setCascadeFieldType:
+ _objc_msgSend$setNumCandidateInteractions:
+ _objc_msgSend$setNumEnrolledEntities:
+ _objc_msgSend$setSpeechProfileSize:
+ _objc_msgSend$setSpeechProfileUpdateReason:
+ _objc_msgSend$signatureWithDomain:type:subType:detectedProcess:triggerThresholdValues:
+ _objc_msgSend$snapshotWithSignature:duration:event:payload:reply:
+ _objc_msgSend$speechProfileSize
+ _objc_msgSend$submitASRIssueReport:withContext:
+ _symbolic SDySS_____G 29CoreEmbeddedSpeechRecognition24CESREntityRankingMetricsV22DonatedAppEntityMetricV
+ _symbolic SDySS_____G 29CoreEmbeddedSpeechRecognition24CESREntityRankingMetricsV23AcceptedAppEntityMetricV
+ _symbolic SS______t 29CoreEmbeddedSpeechRecognition24CESREntityRankingMetricsV22DonatedAppEntityMetricV
+ _symbolic SS______t 29CoreEmbeddedSpeechRecognition24CESREntityRankingMetricsV23AcceptedAppEntityMetricV
+ _symbolic _____ 29CoreEmbeddedSpeechRecognition25CESREntityRankingCAHelperC
+ _symbolic _____Sg 29CoreEmbeddedSpeechRecognition24CESREntityRankingMetricsV22DonatedAppEntityMetricV
+ _symbolic _____Sg 29CoreEmbeddedSpeechRecognition24CESREntityRankingMetricsV23AcceptedAppEntityMetricV
+ _symbolic _____Sg s6UInt32V
+ _symbolic _____XDXMT 29CoreEmbeddedSpeechRecognition25CESREntityRankingCAHelperC
+ _symbolic _____ySS______G SD4KeysV 29CoreEmbeddedSpeechRecognition24CESREntityRankingMetricsV22DonatedAppEntityMetricV
+ _symbolic _____ySS______G SD4KeysV 29CoreEmbeddedSpeechRecognition24CESREntityRankingMetricsV23AcceptedAppEntityMetricV
+ _symbolic _____ySo12CCSharedItemCG s10ArraySliceV
+ _updateReasonForTrigger:.onceToken
+ _updateReasonForTrigger:.reasonsByTrigger
+ getSDRDiagnosticReporterClass.softClass
+ getkSymptomDiagnosticReplyReasonStringSymbolLoc.ptr
+ getkSymptomDiagnosticReplyReasonSymbolLoc.ptr
+ getkSymptomDiagnosticReplySuccessSymbolLoc.ptr
+ sharedInstance.sharedReporter
- -[CESRSpeechItemRanker_ASRRankedEntityTerm _allCodepathsDetected]
- -[CESRSpeechProfileBuilder beginWithCategoriesAndVersions:error:]
- -[CESRSpeechProfileSelfHelper logASRSpeechProfileUpdateEndedWithTotalNumEntitiesReceived:entityMetrics:entityCleanupMetrics:entityExtractionMetrics:]
- -[CESRSpeechProfileSelfHelper logASRSpeechProfileUpdateStarted]
- -[CESRSpeechProfileSiteManager _rebuildAllSites:]
- -[CESRSpeechProfileSiteManager _rebuildSiteAtURL:shouldDefer:]
- -[CESRSpeechProfileSiteManager _resetAndRebuildAllSites]
- -[CESRSpeechProfileSiteWriter rebuildRequiredProfileInstances:]
- -[CESRSpeechProfileUpdater rebuildCategoryGroup:withSets:version:totalItems:error:]
- GCC_except_table1038
- GCC_except_table1047
- GCC_except_table1164
- GCC_except_table1228
- GCC_except_table1229
- GCC_except_table1230
- GCC_except_table1231
- GCC_except_table1232
- GCC_except_table1233
- GCC_except_table1238
- GCC_except_table1268
- GCC_except_table1389
- GCC_except_table1394
- GCC_except_table1398
- GCC_except_table1444
- GCC_except_table1452
- GCC_except_table1457
- GCC_except_table1461
- GCC_except_table220
- GCC_except_table282
- GCC_except_table296
- GCC_except_table333
- GCC_except_table350
- GCC_except_table381
- GCC_except_table408
- GCC_except_table412
- GCC_except_table473
- GCC_except_table494
- GCC_except_table629
- GCC_except_table634
- GCC_except_table637
- GCC_except_table641
- GCC_except_table644
- GCC_except_table647
- GCC_except_table650
- GCC_except_table653
- GCC_except_table656
- GCC_except_table659
- GCC_except_table745
- GCC_except_table772
- GCC_except_table829
- __65-[CESRSpeechProfileBuilder beginWithCategoriesAndVersions:error:]_block_invoke
- ___49-[CESRSpeechProfileSiteManager _rebuildAllSites:]_block_invoke
- ___65-[CESRSpeechProfileBuilder beginWithCategoriesAndVersions:error:]_block_invoke
- ___83-[CESRSpeechProfileUpdater rebuildCategoryGroup:withSets:version:totalItems:error:]_block_invoke
- ___block_descriptor_48_e8_32s40bs_e15_B16?0"NSURL"8l
- ___block_descriptor_56_e8_32s40bs48r_e39_B32?0"CCSharedItem"8"NSString"16^24l
- ___swift_memcpy12_4
- _objc_msgSend$_allCodepathsDetected
- _objc_msgSend$_rebuildAllSites:
- _objc_msgSend$_rebuildSiteAtURL:shouldDefer:
- _objc_msgSend$_resetAndRebuildAllSites
- _objc_msgSend$beginWithCategoriesAndVersions:completion:
- _objc_msgSend$beginWithCategoriesAndVersions:error:
- _objc_msgSend$generateABCSnapshotForType:subType:context:
- _objc_msgSend$initWithSpeechProfileSiteURL:locale:
- _objc_msgSend$logASRSpeechProfileUpdateEndedWithTotalNumEntitiesReceived:entityMetrics:entityCleanupMetrics:entityExtractionMetrics:
- _objc_msgSend$rebuildCategoryGroup:withSets:version:totalItems:error:
- _objc_msgSend$rebuildRequiredProfileInstances:
- _symbolic SDySSSaySo12CCSharedItemCGG
- _symbolic SDySSSaySo12CCSharedItemCy______So13CCItemMessageCXcGGG So13CCItemContentP
- _symbolic SDySSSo12CCSharedItemCy______So13CCItemMessageCXcGG So13CCItemContentP
- _symbolic SS_SaySo12CCSharedItemCGt
- _symbolic SaySo12CCSharedItemCy______So13CCItemMessageCXcGGIgo_ So13CCItemContentP
- _symbolic SaySo12CCSharedItemCy______So13CCItemMessageCXcGGz_Xx So13CCItemContentP
- _symbolic _____yS2S_G SD6ValuesV
- _symbolic _____ySSSaySo12CCSharedItemCG_G SD4KeysV
- _symbolic _____ySSSaySo12CCSharedItemCG_G SD6ValuesV
CStrings:
+ "  Unranked candidates collected: %ld"
+ "%s App Entities enrolled by rank class: ranked=%lu, incremental=%lu, unranked=%lu"
+ "%s CESRDiagnosticReporter: auto bug capture dampened for signature: %@ with error code: %@ reason: %@"
+ "%s Enrollment %@. Codepaths: didIngestAppEntities=%@, didExtractAppEntities=%@, hadRankedCandidates=%@, hadIncrementalCandidates=%@, hadUnrankedCandidates=%@"
+ "-[CESRDiagnosticReporter _submitASRIssueReport:withContext:]_block_invoke"
+ "-[CESRSpeechProfileBuilder beginWithCategoriesAndVersions:trigger:error:]_block_invoke"
+ "-[CESRSpeechProfileSiteManager _rebuildAllSites:trigger:]"
+ "-[CESRSpeechProfileSiteManager _rebuildSiteAtURL:shouldDefer:trigger:]"
+ "-[CESRSpeechProfileUpdater rebuildCategoryGroup:withSets:version:trigger:totalItems:error:]"
+ "/System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/Contents/MacOS/SymptomDiagnosticReporter"
+ "7e22cf8b-ae4f-41d4-8f00-5cf6fa3c0065"
+ "<%@: %p; totalNumEntitiesReceived: %u; isCleanupIngestionEnabled: %d; numEntitiesContainingEmoji: %u; numEntitiesContainingSpecialCharacters: %u; numEntitiesCleaned: %u; isExtractionIngestionEnabled: %d; isExtractionSetupSuccessful: %d; numEntitiesExtractionAttempted: %u; numEntitiesContainingExtractions: %u; numEntitiesExtracted: %u; speechProfileSize: %llu; numEnrolledEntitiesPerCascadeFieldType: %@>"
+ "<no source id>"
+ "ASR"
+ "App %s summary: sought=%ld found=%ld missed=%ld fillNeeded=%ld"
+ "CESRDiagnosticReporter"
+ "Cannot clear Cascade set: empty LME template."
+ "Cleared %ld of %ld ranked-entity Cascade partitions (kept %ld)."
+ "Cleared Cascade set for LME template %s (full donation with no items)."
+ "Cleared ranked-entity Cascade partition for LME template %s."
+ "CoreSpeech"
+ "Failed to build predicate for id=%s: %@"
+ "Failed to list cache directory: %@"
+ "Failed to remove %s during full purge: %@"
+ "Removed cache file during full purge: %s"
+ "Retrieved %ld of %ld requested items for set %s."
+ "SDRDiagnosticReporter"
+ "Skipping fill-to-minimum for %s: set size %ld exceeds threshold %ld"
+ "Task cancelled during ranked-entity partition cleanup. Stopping."
+ "c186a7a1-882c-4813-86eb-97a5f0365f8d"
+ "com.apple.com.apple.siri.asr.speechprofile.AppEntityPartitionEnumerated"
+ "com.apple.siri.asr.speechprofile.AppEntitiesEnumerated"
+ "extractionOnlyTemplatesOverride"
+ "kSymptomDiagnosticReplyReason"
+ "kSymptomDiagnosticReplyReasonString"
+ "kSymptomDiagnosticReplySuccess"
+ "num_donating_first_party_apps"
+ "num_donating_third_party_apps"
+ "num_empty_title_display_representations"
+ "num_entities_present"
+ "num_ranked_entities_accepted"
+ "num_unranked_entities_accepted"
+ "siri_language_changed"
+ "softlink:r:path:/System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter"
+ "source_bundle_id"
+ "total_num_entities_accepted"
+ "total_num_entities_present"
+ "total_num_ranked_entities_accepted"
+ "total_num_unranked_entities_accepted"
+ "trial_experiment"
+ "v16@?0@\"NSDictionary\"8"
- "  Fill candidates by type: [%s]"
- "%s Enrollment %@. Codepaths: didIngestAppEntities=%@, didQualifyForAppEntityRanking=%@, didExtractAppEntities=%@"
- "-[CESRSpeechProfileBuilder beginWithCategoriesAndVersions:error:]_block_invoke"
- "-[CESRSpeechProfileSiteManager _rebuildAllSites:]"
- "-[CESRSpeechProfileSiteManager _rebuildSiteAtURL:shouldDefer:]"
- "-[CESRSpeechProfileUpdater rebuildCategoryGroup:withSets:version:totalItems:error:]"
- "<%@: %p; totalNumEntitiesReceived: %u; isCleanupIngestionEnabled: %d; numEntitiesContainingEmoji: %u; numEntitiesContainingSpecialCharacters: %u; numEntitiesCleaned: %u; isExtractionIngestionEnabled: %d; isExtractionSetupSuccessful: %d; numEntitiesExtractionAttempted: %u; numEntitiesContainingExtractions: %u; numEntitiesExtracted: %u>"
- "A"
- "App %s summary: sought=%ld found=%ld missed=%ld fillNeeded=%ld foundTypes=[%s]"
- "App %s summary: sought=0 found=0 missed=0 fillNeeded=0 foundTypes=[] (enumeration skipped: interactionOnlyRanking + no ranked IDs)"
- "Failed to list cache directory for purge: %@"
- "corespeechd"
```
