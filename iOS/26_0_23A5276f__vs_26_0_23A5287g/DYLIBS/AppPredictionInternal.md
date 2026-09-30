## AppPredictionInternal

> `/System/Library/PrivateFrameworks/AppPredictionInternal.framework/AppPredictionInternal`

```diff

-613.0.1.0.0
-  __TEXT.__text: 0x4803b4
-  __TEXT.__auth_stubs: 0x3de0
-  __TEXT.__objc_methlist: 0x38d84
-  __TEXT.__const: 0x3b6a
-  __TEXT.__cstring: 0x5a131
-  __TEXT.__oslogstring: 0x3aa19
-  __TEXT.__gcc_except_tab: 0xfcf8
+615.0.2.0.0
+  __TEXT.__text: 0x482058
+  __TEXT.__auth_stubs: 0x3df0
+  __TEXT.__objc_methlist: 0x38e34
+  __TEXT.__const: 0x3bba
+  __TEXT.__cstring: 0x5a901
+  __TEXT.__oslogstring: 0x3abf9
+  __TEXT.__gcc_except_tab: 0xfd64
   __TEXT.__dlopen_cstrs: 0x1d2
   __TEXT.__ustring: 0x90
-  __TEXT.__swift5_typeref: 0x12aa
-  __TEXT.__constg_swiftt: 0x1b94
-  __TEXT.__swift5_reflstr: 0xabb
+  __TEXT.__swift5_typeref: 0x12ac
+  __TEXT.__constg_swiftt: 0x1be4
+  __TEXT.__swift5_reflstr: 0xad4
   __TEXT.__swift5_fieldmd: 0xef8
   __TEXT.__swift5_proto: 0x134
   __TEXT.__swift5_types: 0x188
-  __TEXT.__swift_as_entry: 0x10c
-  __TEXT.__swift_as_ret: 0xf8
+  __TEXT.__swift_as_entry: 0x110
+  __TEXT.__swift_as_ret: 0xfc
   __TEXT.__swift5_assocty: 0x240
-  __TEXT.__swift5_capture: 0x5e4
+  __TEXT.__swift5_capture: 0x674
   __TEXT.__swift5_protos: 0x24
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0xe350
-  __TEXT.__eh_frame: 0x26fc
+  __TEXT.__unwind_info: 0xe388
+  __TEXT.__eh_frame: 0x2724
   __TEXT.__objc_classname: 0x8c8d
-  __TEXT.__objc_methname: 0xae291
-  __TEXT.__objc_methtype: 0x1806b
-  __TEXT.__objc_stubs: 0x4cf40
-  __DATA_CONST.__got: 0x3948
-  __DATA_CONST.__const: 0xbe48
+  __TEXT.__objc_methname: 0xae495
+  __TEXT.__objc_methtype: 0x18091
+  __TEXT.__objc_stubs: 0x4cfe0
+  __DATA_CONST.__got: 0x3960
+  __DATA_CONST.__const: 0xbed0
   __DATA_CONST.__objc_classlist: 0x1fa0
   __DATA_CONST.__objc_catlist: 0x140
   __DATA_CONST.__objc_protolist: 0x4d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1be00
+  __DATA_CONST.__objc_selrefs: 0x1be58
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x1530
-  __DATA_CONST.__objc_arraydata: 0x1398
-  __AUTH_CONST.__auth_got: 0x1f08
-  __AUTH_CONST.__const: 0x8548
-  __AUTH_CONST.__cfstring: 0x3a860
-  __AUTH_CONST.__objc_const: 0x83cd8
-  __AUTH_CONST.__objc_intobj: 0x3438
-  __AUTH_CONST.__objc_arrayobj: 0x1098
+  __DATA_CONST.__objc_arraydata: 0x13a0
+  __AUTH_CONST.__auth_got: 0x1f10
+  __AUTH_CONST.__const: 0x86d8
+  __AUTH_CONST.__cfstring: 0x3aa80
+  __AUTH_CONST.__objc_const: 0x83d48
+  __AUTH_CONST.__objc_intobj: 0x3450
+  __AUTH_CONST.__objc_arrayobj: 0x10b0
   __AUTH_CONST.__objc_dictobj: 0x1b8
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x70
-  __AUTH.__objc_data: 0x5350
-  __AUTH.__data: 0x2160
-  __DATA.__objc_ivar: 0x4aec
-  __DATA.__data: 0x3d08
+  __AUTH.__objc_data: 0x5380
+  __AUTH.__data: 0x2178
+  __DATA.__objc_ivar: 0x4af0
+  __DATA.__data: 0x3d18
   __DATA.__bss: 0x27e8
   __DATA.__common: 0x108
   __DATA_DIRTY.__objc_data: 0xf028

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A08CF582-C81D-35D9-BD65-4D53BAB18869
-  Functions: 25463
-  Symbols:   76840
-  CStrings:  42882
+  UUID: F4CB48E6-C96F-37F5-BDBE-2BB64DF09CD5
+  Functions: 25515
+  Symbols:   76951
+  CStrings:  42947
 
Symbols:
+ -[ATXParameterSuggestionServer suggestionMetadataForActions:withCompletion:]
+ -[ATXServer _onQueue_notifySpotlightInvoked:]
+ -[_ATXAppInfoManager allRemoteApps]
+ -[_ATXAppInfoManager updateInstallDateForBundleID:timestamp:]
+ -[_ATXDataStore allRemoteApps]
+ -[_ATXDataStore deleteParameterizedSuggestionWithUniqueIdentifier:]
+ -[_ATXDataStore deleteParameterizedSuggestionWithUniqueIdentifier:].cold.1
+ -[_ATXDataStore fetchParameterizedSuggestionWithUniqueIdentifier:]
+ -[_ATXDataStore fetchParameterizedSuggestionWithUniqueIdentifier:].cold.1
+ -[_ATXDataStore recordParamererizedSuggestionWithUniqueIdentifier:encodedTool:encodedSummary:]
+ -[_ATXDataStore recordParamererizedSuggestionWithUniqueIdentifier:encodedTool:encodedSummary:].cold.1
+ -[_ATXDataStore recordParamererizedSuggestionWithUniqueIdentifier:encodedTool:encodedSummary:].cold.2
+ -[_ATXDataStore recordParamererizedSuggestionWithUniqueIdentifier:encodedTool:encodedSummary:].cold.3
+ -[_ATXDataStore resetAllRecordedParameterizedSuggestions]
+ -[_ATXDataStore updateInstallDateForBundleID:timestamp:]
+ -[_ATXDataStore updateOrInsertDataForRemoteAppsWithMappings:]
+ -[_ATXInspectionClient fetchPIDFromServer:]
+ -[_ATXInspectionServer fetchPIDFromServer:]
+ GCC_except_table154
+ GCC_except_table221
+ GCC_except_table222
+ GCC_except_table226
+ GCC_except_table230
+ GCC_except_table234
+ GCC_except_table278
+ GCC_except_table291
+ GCC_except_table328
+ GCC_except_table332
+ GCC_except_table353
+ GCC_except_table357
+ GCC_except_table359
+ GCC_except_table361
+ GCC_except_table375
+ GCC_except_table391
+ GCC_except_table402
+ GCC_except_table418
+ GCC_except_table420
+ GCC_except_table424
+ GCC_except_table434
+ GCC_except_table435
+ GCC_except_table444
+ GCC_except_table481
+ GCC_except_table482
+ GCC_except_table494
+ GCC_except_table498
+ GCC_except_table510
+ GCC_except_table514
+ GCC_except_table548
+ GCC_except_table594
+ GCC_except_table599
+ GCC_except_table628
+ GCC_except_table646
+ _OBJC_CLASS_$_ATXEncodedActionSuggestionMetadata
+ _OBJC_IVAR_$_ATXServer._prewarmingQueue
+ ___191-[_ATXDataStore writeActionType:bundleId:date:action:slotSets:timeZone:prevLocationUUID:locationUUID:weight:actionUUID:motionType:appSessionStartDate:appSessionEndDate:geohash:coarseGeohash:]_block_invoke.521
+ ___191-[_ATXDataStore writeActionType:bundleId:date:action:slotSets:timeZone:prevLocationUUID:locationUUID:weight:actionUUID:motionType:appSessionStartDate:appSessionEndDate:geohash:coarseGeohash:]_block_invoke_2.525
+ ___201-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:appProtectionInfoProvider:]_block_invoke.107
+ ___201-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:appProtectionInfoProvider:]_block_invoke.113
+ ___201-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:appProtectionInfoProvider:]_block_invoke.115
+ ___201-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:appProtectionInfoProvider:]_block_invoke.126
+ ___201-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:appProtectionInfoProvider:]_block_invoke.93
+ ___201-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:appProtectionInfoProvider:]_block_invoke.99
+ ___201-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:appProtectionInfoProvider:]_block_invoke_2.100
+ ___201-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:appProtectionInfoProvider:]_block_invoke_2.108
+ ___201-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:appProtectionInfoProvider:]_block_invoke_2.114
+ ___201-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:appProtectionInfoProvider:]_block_invoke_2.116
+ ___201-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:appProtectionInfoProvider:]_block_invoke_2.127
+ ___201-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:appProtectionInfoProvider:]_block_invoke_2.94
+ ___28-[_ATXDataStore loadAppInfo]_block_invoke.305
+ ___30-[_ATXDataStore allRemoteApps]_block_invoke
+ ___30-[_ATXDataStore allRemoteApps]_block_invoke_2
+ ___36-[ATXServer notifySpotlightInvoked:]_block_invoke
+ ___43-[_ATXDataStore _removeActionsWithoutTitle]_block_invoke.712
+ ___43-[_ATXDataStore _removeActionsWithoutTitle]_block_invoke_2.714
+ ___43-[_ATXDataStore _removeActionsWithoutTitle]_block_invoke_2.714.cold.1
+ ___43-[_ATXInspectionClient fetchPIDFromServer:]_block_invoke
+ ___44-[_ATXDataStore migration_RemoveLinkActions]_block_invoke.976
+ ___44-[_ATXDataStore removeAllSlotsFromActionLog]_block_invoke.690
+ ___44-[_ATXDataStore removeAllSlotsFromActionLog]_block_invoke.690.cold.1
+ ___45-[_ATXDataStore loadLaunchesFollowingBundle:]_block_invoke.345
+ ___48-[ATXServer listener:shouldAcceptNewConnection:]_block_invoke.82
+ ___48-[ATXServer listener:shouldAcceptNewConnection:]_block_invoke.82.cold.1
+ ___48-[_ATXDataStore loadAppActionLaunchesFollowing:]_block_invoke.358
+ ___49-[_ATXDataStore regenerateSlotSetKeyForBundleId:]_block_invoke.633
+ ___50-[_ATXDataStore _regenerateSlotSetKeyForBundleId:]_block_invoke.627
+ ___50-[_ATXDataStore _regenerateSlotSetKeyForBundleId:]_block_invoke.629
+ ___50-[_ATXDataStore _regenerateSlotSetKeyForBundleId:]_block_invoke_2.628
+ ___50-[_ATXDataStore _regenerateSlotSetKeyForBundleId:]_block_invoke_2.630
+ ___51-[_ATXDataStore trimActionHistoryWithAppWhitelist:]_block_invoke.644
+ ___51-[_ATXDataStore trimActionHistoryWithAppWhitelist:]_block_invoke_2.648
+ ___51-[_ATXDataStore trimActionHistoryWithAppWhitelist:]_block_invoke_3.653
+ ___51-[_ATXDataStore trimActionHistoryWithAppWhitelist:]_block_invoke_4.654
+ ___51-[_ATXDataStore trimActionHistoryWithAppWhitelist:]_block_invoke_5.658
+ ___56-[_ATXDataStore updateInstallDateForBundleID:timestamp:]_block_invoke
+ ___57-[_ATXDataStore resetAllRecordedParameterizedSuggestions]_block_invoke
+ ___57-[_ATXDataStore resetAllRecordedParameterizedSuggestions]_block_invoke_2
+ ___57-[_ATXDataStore resetAllRecordedParameterizedSuggestions]_block_invoke_3
+ ___61-[_ATXDataStore updateOrInsertDataForRemoteAppsWithMappings:]_block_invoke
+ ___61-[_ATXDataStore updateOrInsertDataForRemoteAppsWithMappings:]_block_invoke_2
+ ___61-[_ATXDataStore updateOrInsertDataForRemoteAppsWithMappings:]_block_invoke_3
+ ___61-[_ATXDataStore updateOrInsertDataForRemoteAppsWithMappings:]_block_invoke_4
+ ___61-[_ATXDataStore updateOrInsertDataForRemoteAppsWithMappings:]_block_invoke_4.cold.1
+ ___62-[_ATXAppInstallMonitor noSyncUpdateWithWaitTime:andBackdate:]_block_invoke.54
+ ___62-[_ATXDataStore migration_DeprecateIntentForAllAppsHistograms]_block_invoke.853
+ ___62-[_ATXDataStore migration_DeprecateIntentForAllAppsHistograms]_block_invoke_2.856
+ ___62-[_ATXDataStore migration_DeprecateIntentForAllAppsHistograms]_block_invoke_2.856.cold.1
+ ___64-[_ATXDataStore _deserializeActionLogRowWithStmt:invokingBlock:]_block_invoke.530
+ ___65-[_ATXDataStore enumerateFeedbackForActionOfType:bundleId:block:]_block_invoke.686
+ ___66-[_ATXDataStore fetchParameterizedSuggestionWithUniqueIdentifier:]_block_invoke
+ ___66-[_ATXDataStore fetchParameterizedSuggestionWithUniqueIdentifier:]_block_invoke_2
+ ___66-[_ATXDataStore fetchParameterizedSuggestionWithUniqueIdentifier:]_block_invoke_3
+ ___66-[_ATXDataStore fetchParameterizedSuggestionWithUniqueIdentifier:]_block_invoke_4
+ ___66-[_ATXDataStore fetchParameterizedSuggestionWithUniqueIdentifier:]_block_invoke_4.cold.1
+ ___67-[_ATXDataStore deleteParameterizedSuggestionWithUniqueIdentifier:]_block_invoke
+ ___67-[_ATXDataStore deleteParameterizedSuggestionWithUniqueIdentifier:]_block_invoke_2
+ ___67-[_ATXDataStore deleteParameterizedSuggestionWithUniqueIdentifier:]_block_invoke_3
+ ___69-[_ATXDataStore migration_forceUpdateNewCrystalSystemAppsInstallDate]_block_invoke.961
+ ___69-[_ATXDataStore migration_forceUpdateNewCrystalSystemAppsInstallDate]_block_invoke_2.968
+ ___69-[_ATXDataStore migration_forceUpdateNewCrystalSystemAppsInstallDate]_block_invoke_2.968.cold.1
+ ___73-[_ATXDataStore deleteSamplesThatAreMoreThan28DaysOldFromActionDatabases]_block_invoke.1150
+ ___73-[_ATXDataStore deleteSamplesThatAreMoreThan28DaysOldFromActionDatabases]_block_invoke.1157
+ ___73-[_ATXDataStore deleteSamplesThatAreMoreThan28DaysOldFromActionDatabases]_block_invoke_2.1151
+ ___73-[_ATXDataStore deleteSamplesThatAreMoreThan28DaysOldFromActionDatabases]_block_invoke_2.1151.cold.1
+ ___73-[_ATXDataStore deleteSamplesThatAreMoreThan28DaysOldFromActionDatabases]_block_invoke_2.1158
+ ___73-[_ATXDataStore deleteSamplesThatAreMoreThan28DaysOldFromActionDatabases]_block_invoke_2.1158.cold.1
+ ___88-[ATXAppDirectoryOrderingProvider _updateScreenTimeMappingsForAppBundleIds:withRetries:]_block_invoke.211
+ ___88-[ATXAppDirectoryOrderingProvider _updateScreenTimeMappingsForAppBundleIds:withRetries:]_block_invoke.212
+ ___92-[_ATXFeedback populateFeedbackForConsumerType:forBundleId:withContext:forFeedbackCategory:]_block_invoke.cold.4
+ ___92-[_ATXFeedback populateFeedbackForConsumerType:forBundleId:withContext:forFeedbackCategory:]_block_invoke.cold.5
+ ___94-[_ATXDataStore recordParamererizedSuggestionWithUniqueIdentifier:encodedTool:encodedSummary:]_block_invoke
+ ___94-[_ATXDataStore recordParamererizedSuggestionWithUniqueIdentifier:encodedTool:encodedSummary:]_block_invoke_2
+ ___94-[_ATXDataStore recordParamererizedSuggestionWithUniqueIdentifier:encodedTool:encodedSummary:]_block_invoke_3
+ ___block_descriptor_32_e42_v24?0^{ATXPredictionItem=Q[828f]fBB}8d16l
+ ___block_descriptor_40_ea8_32r_e42_v24?0^{ATXPredictionItem=Q[828f]fBB}8d16lr32l8
+ ___block_descriptor_40_ea8_32s_e40_v16?0r^{ATXPredictionItem=Q[828f]fBB}8ls32l8
+ ___block_descriptor_40_ea8_32s_e42_v24?0^{ATXPredictionItem=Q[828f]fBB}8d16ls32l8
+ ___block_descriptor_40_ea8_32s_e64_v24?0"ATXScoredPrediction"8r^{ATXPredictionItem=Q[828f]fBB}16ls32l8
+ ___block_descriptor_48_ea8_32s40r_e40_v16?0r^{ATXPredictionItem=Q[828f]fBB}8lr40l8s32l8
+ ___block_descriptor_48_ea8_32s40r_e42_v24?0^{ATXPredictionItem=Q[828f]fBB}8d16ls32l8r40l8
+ ___block_descriptor_64_ea8_32s40r48r_e40_v16?0r^{ATXPredictionItem=Q[828f]fBB}8ls32l8r40l8r48l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e29_v16?0"_PASSqliteStatement"8ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e54_v32?0"NSString"8"ATXRemoteAppPlaceholderInfo"16^B24ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_80_ea8_32s40s48r56r_e40_v16?0r^{ATXPredictionItem=Q[828f]fBB}8ls32l8r48l8r56l8s40l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_88_ea8_32s40s48s56s64r_e40_v16?0r^{ATXPredictionItem=Q[828f]fBB}8lr64l8s32l8s40l8s48l8s56l8
+ ___block_literal_global.1018
+ ___block_literal_global.1126
+ ___block_literal_global.1131
+ ___block_literal_global.1146
+ ___block_literal_global.1153
+ ___block_literal_global.1160
+ ___block_literal_global.203
+ ___block_literal_global.2499
+ ___block_literal_global.254
+ ___block_literal_global.372
+ ___block_literal_global.380
+ ___block_literal_global.475
+ ___block_literal_global.620
+ ___block_literal_global.632
+ ___block_literal_global.692
+ ___block_literal_global.702
+ ___block_literal_global.721
+ ___block_literal_global.757
+ ___block_literal_global.799
+ ___block_literal_global.804
+ ___block_literal_global.832
+ ___block_literal_global.834
+ ___block_literal_global.842
+ ___block_literal_global.849
+ ___block_literal_global.858
+ ___block_literal_global.887
+ ___block_literal_global.927
+ ___block_literal_global.944
+ ___block_literal_global.963
+ ___block_literal_global.973
+ ___block_literal_global.978
+ ___block_literal_global.994
+ ___block_literal_global.996
+ _block_copy_helper.33
+ _block_copy_helper.77
+ _block_descriptor.35
+ _block_descriptor.79
+ _block_destroy_helper.34
+ _block_destroy_helper.78
+ _getpid
+ _kATXAppDirectoryRecentsCacheBundleIdKey
+ _kATXAppDirectoryRecentsCacheInstallDateKey
+ _kSetInstallDateToDistantOldTimeForRemoteAppsQuery
+ _kUpdateDataForRemoteAppsWithMappingsQuery
+ _objc_msgSend$_onQueue_notifySpotlightInvoked:
+ _objc_msgSend$allRemoteApps
+ _objc_msgSend$fetchPIDFromServer:
+ _objc_msgSend$initWithEncodedInvocation:encodedSummary:canonicalActionID:
+ _objc_msgSend$updateDefaultsWithSystemDescriptors:updateCarPlayDefaults:installDatesCache:reason:
+ _objc_msgSend$updateInstallDateForBundleID:timestamp:
+ _objectdestroy.14Tm
+ _objectdestroy.32Tm
+ _symbolic ______pSg 21AppPredictionInternal23UIContextClientProtocolP
- GCC_except_table121
- GCC_except_table156
- GCC_except_table218
- GCC_except_table219
- GCC_except_table223
- GCC_except_table227
- GCC_except_table231
- GCC_except_table275
- GCC_except_table288
- GCC_except_table325
- GCC_except_table329
- GCC_except_table350
- GCC_except_table354
- GCC_except_table356
- GCC_except_table358
- GCC_except_table372
- GCC_except_table388
- GCC_except_table399
- GCC_except_table415
- GCC_except_table417
- GCC_except_table421
- GCC_except_table425
- GCC_except_table432
- GCC_except_table441
- GCC_except_table478
- GCC_except_table479
- GCC_except_table491
- GCC_except_table495
- GCC_except_table507
- GCC_except_table511
- GCC_except_table540
- GCC_except_table584
- GCC_except_table589
- GCC_except_table619
- ___191-[_ATXDataStore writeActionType:bundleId:date:action:slotSets:timeZone:prevLocationUUID:locationUUID:weight:actionUUID:motionType:appSessionStartDate:appSessionEndDate:geohash:coarseGeohash:]_block_invoke.518
- ___191-[_ATXDataStore writeActionType:bundleId:date:action:slotSets:timeZone:prevLocationUUID:locationUUID:weight:actionUUID:motionType:appSessionStartDate:appSessionEndDate:geohash:coarseGeohash:]_block_invoke_2.522
- ___201-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:appProtectionInfoProvider:]_block_invoke.101
- ___201-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:appProtectionInfoProvider:]_block_invoke.110
- ___201-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:appProtectionInfoProvider:]_block_invoke.112
- ___201-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:appProtectionInfoProvider:]_block_invoke.123
- ___201-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:appProtectionInfoProvider:]_block_invoke.90
- ___201-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:appProtectionInfoProvider:]_block_invoke.96
- ___201-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:appProtectionInfoProvider:]_block_invoke_2.102
- ___201-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:appProtectionInfoProvider:]_block_invoke_2.111
- ___201-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:appProtectionInfoProvider:]_block_invoke_2.113
- ___201-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:appProtectionInfoProvider:]_block_invoke_2.124
- ___201-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:appProtectionInfoProvider:]_block_invoke_2.91
- ___201-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:appProtectionInfoProvider:]_block_invoke_2.97
- ___28-[_ATXDataStore loadAppInfo]_block_invoke.302
- ___43-[_ATXDataStore _removeActionsWithoutTitle]_block_invoke.709
- ___43-[_ATXDataStore _removeActionsWithoutTitle]_block_invoke_2.711
- ___43-[_ATXDataStore _removeActionsWithoutTitle]_block_invoke_2.711.cold.1
- ___44-[_ATXDataStore migration_RemoveLinkActions]_block_invoke.973
- ___44-[_ATXDataStore removeAllSlotsFromActionLog]_block_invoke.687
- ___44-[_ATXDataStore removeAllSlotsFromActionLog]_block_invoke.687.cold.1
- ___45-[_ATXDataStore loadLaunchesFollowingBundle:]_block_invoke.342
- ___48-[ATXServer listener:shouldAcceptNewConnection:]_block_invoke.81
- ___48-[ATXServer listener:shouldAcceptNewConnection:]_block_invoke.81.cold.1
- ___48-[_ATXDataStore loadAppActionLaunchesFollowing:]_block_invoke.355
- ___49-[_ATXDataStore regenerateSlotSetKeyForBundleId:]_block_invoke.630
- ___50-[_ATXDataStore _regenerateSlotSetKeyForBundleId:]_block_invoke.624
- ___50-[_ATXDataStore _regenerateSlotSetKeyForBundleId:]_block_invoke.626
- ___50-[_ATXDataStore _regenerateSlotSetKeyForBundleId:]_block_invoke_2.625
- ___50-[_ATXDataStore _regenerateSlotSetKeyForBundleId:]_block_invoke_2.627
- ___51-[_ATXDataStore trimActionHistoryWithAppWhitelist:]_block_invoke.641
- ___51-[_ATXDataStore trimActionHistoryWithAppWhitelist:]_block_invoke_2.645
- ___51-[_ATXDataStore trimActionHistoryWithAppWhitelist:]_block_invoke_3.650
- ___51-[_ATXDataStore trimActionHistoryWithAppWhitelist:]_block_invoke_4.651
- ___51-[_ATXDataStore trimActionHistoryWithAppWhitelist:]_block_invoke_5.655
- ___62-[_ATXAppInstallMonitor noSyncUpdateWithWaitTime:andBackdate:]_block_invoke.55
- ___62-[_ATXDataStore migration_DeprecateIntentForAllAppsHistograms]_block_invoke.850
- ___62-[_ATXDataStore migration_DeprecateIntentForAllAppsHistograms]_block_invoke_2.853
- ___62-[_ATXDataStore migration_DeprecateIntentForAllAppsHistograms]_block_invoke_2.853.cold.1
- ___64-[_ATXDataStore _deserializeActionLogRowWithStmt:invokingBlock:]_block_invoke.527
- ___65-[_ATXDataStore enumerateFeedbackForActionOfType:bundleId:block:]_block_invoke.683
- ___69-[_ATXDataStore migration_forceUpdateNewCrystalSystemAppsInstallDate]_block_invoke.958
- ___69-[_ATXDataStore migration_forceUpdateNewCrystalSystemAppsInstallDate]_block_invoke_2.965
- ___69-[_ATXDataStore migration_forceUpdateNewCrystalSystemAppsInstallDate]_block_invoke_2.965.cold.1
- ___73-[_ATXDataStore deleteSamplesThatAreMoreThan28DaysOldFromActionDatabases]_block_invoke.1139
- ___73-[_ATXDataStore deleteSamplesThatAreMoreThan28DaysOldFromActionDatabases]_block_invoke.1146
- ___73-[_ATXDataStore deleteSamplesThatAreMoreThan28DaysOldFromActionDatabases]_block_invoke_2.1140
- ___73-[_ATXDataStore deleteSamplesThatAreMoreThan28DaysOldFromActionDatabases]_block_invoke_2.1140.cold.1
- ___73-[_ATXDataStore deleteSamplesThatAreMoreThan28DaysOldFromActionDatabases]_block_invoke_2.1147
- ___73-[_ATXDataStore deleteSamplesThatAreMoreThan28DaysOldFromActionDatabases]_block_invoke_2.1147.cold.1
- ___88-[ATXAppDirectoryOrderingProvider _updateScreenTimeMappingsForAppBundleIds:withRetries:]_block_invoke.224
- ___88-[ATXAppDirectoryOrderingProvider _updateScreenTimeMappingsForAppBundleIds:withRetries:]_block_invoke.225
- ___block_descriptor_32_e42_v24?0^{ATXPredictionItem=Q[827f]fBB}8d16l
- ___block_descriptor_40_ea8_32r_e42_v24?0^{ATXPredictionItem=Q[827f]fBB}8d16lr32l8
- ___block_descriptor_40_ea8_32s_e40_v16?0r^{ATXPredictionItem=Q[827f]fBB}8ls32l8
- ___block_descriptor_40_ea8_32s_e42_v24?0^{ATXPredictionItem=Q[827f]fBB}8d16ls32l8
- ___block_descriptor_40_ea8_32s_e64_v24?0"ATXScoredPrediction"8r^{ATXPredictionItem=Q[827f]fBB}16ls32l8
- ___block_descriptor_48_ea8_32s40r_e40_v16?0r^{ATXPredictionItem=Q[827f]fBB}8lr40l8s32l8
- ___block_descriptor_48_ea8_32s40r_e42_v24?0^{ATXPredictionItem=Q[827f]fBB}8d16ls32l8r40l8
- ___block_descriptor_64_ea8_32s40r48r_e40_v16?0r^{ATXPredictionItem=Q[827f]fBB}8ls32l8r40l8r48l8
- ___block_descriptor_80_ea8_32s40s48r56r_e40_v16?0r^{ATXPredictionItem=Q[827f]fBB}8ls32l8r48l8r56l8s40l8
- ___block_descriptor_88_ea8_32s40s48s56s64r_e40_v16?0r^{ATXPredictionItem=Q[827f]fBB}8lr64l8s32l8s40l8s48l8s56l8
- ___block_literal_global.1002
- ___block_literal_global.1115
- ___block_literal_global.1120
- ___block_literal_global.1135
- ___block_literal_global.1142
- ___block_literal_global.1149
- ___block_literal_global.146
- ___block_literal_global.200
- ___block_literal_global.2496
- ___block_literal_global.281
- ___block_literal_global.369
- ___block_literal_global.377
- ___block_literal_global.472
- ___block_literal_global.517
- ___block_literal_global.617
- ___block_literal_global.629
- ___block_literal_global.689
- ___block_literal_global.694
- ___block_literal_global.699
- ___block_literal_global.754
- ___block_literal_global.796
- ___block_literal_global.801
- ___block_literal_global.829
- ___block_literal_global.831
- ___block_literal_global.839
- ___block_literal_global.846
- ___block_literal_global.852
- ___block_literal_global.884
- ___block_literal_global.924
- ___block_literal_global.941
- ___block_literal_global.960
- ___block_literal_global.970
- ___block_literal_global.972
- ___block_literal_global.988
- _block_copy_helper.32
- _block_copy_helper.36
- _block_copy_helper.72
- _block_descriptor.34
- _block_descriptor.38
- _block_descriptor.74
- _block_destroy_helper.33
- _block_destroy_helper.37
- _block_destroy_helper.73
- _objc_msgSend$updateDefaultsWithSystemDescriptors:installDatesCache:reason:
- _objectdestroy.12Tm
- _objectdestroy.30Tm
- _symbolic ______p 21AppPredictionInternal23UIContextClientProtocolP
CStrings:
+ ":app2vec_clusters"
+ ":bundle_ids"
+ ":encodedSummary"
+ ":encodedTool"
+ ":enterprise_apps"
+ ":genre_ids"
+ ":timestamps"
+ ":uniqueID"
+ ":uuids"
+ "@24@0:8^{ATXPredictionItem=@Q[828f]fBB}16"
+ "@24@0:8r^{ATXPredictionItem=@Q[828f]fBB}16"
+ "@32@0:8^{ATXPredictionItem=@Q[828f]fBB}16@24"
+ "@3352@0:8{ATXPredictionItem=@Q[828f]fBB}16"
+ "@3360@0:8{ATXPredictionItem=@Q[828f]fBB}16@3352"
+ "@3368@0:8{ATXPredictionItem=@Q[828f]fBB}16@3352@3360"
+ "@3388@0:8@16@24@32f40@44{ATXPredictionItem=@Q[828f]fBB}52"
+ "@40@0:8@16r^{ATXPredictionItem=@Q[828f]fBB}24@32"
+ "@56@0:8@16r^{ATXPredictionItem=@Q[828f]fBB}24d32@40@48"
+ "@64@0:8@16@24@32r^{ATXPredictionItem=@Q[828f]fBB}40d48@56"
+ "@72@0:8@16@24r^{ATXPredictionItem=@Q[828f]fBB}32d40@48i56B60@64"
+ "@80@0:8@16@24r^{ATXPredictionItem=@Q[828f]fBB}32d40@48i56B60^v64@72"
+ "ATXConsumerTypeAppDirectory got confirm for %@"
+ "ATXConsumerTypeAppDirectory got reject for %@"
+ "ATXDataStore: Force updating install date for bundle ID: %@"
+ "ATXDataStore: Updating data failed for remote apps error: %{public}@"
+ "B3352@0:8{ATXPredictionItem=@Q[828f]fBB}16"
+ "B40@0:8^{ATXPredictionItem=@Q[828f]fBB}16@?24^@32"
+ "CREATE TABLE IF NOT EXISTS parameterizedSuggestions (uniqueID TEXT PRIMARY KEY, encodedTool BLOB NOT NULL, encodedSummary BLOB NOT NULL)"
+ "DELETE FROM parameterizedSuggestions"
+ "DELETE FROM parameterizedSuggestions WHERE uniqueID = :uniqueID"
+ "Donation Processing - Got Link action in publisher"
+ "Error fetching parameterized suggestion with uniqueID %@: %@"
+ "INSERT INTO appInfo (bundleId, installDate, genreId, app2VecCluster, remoteAppUUID, isEnterpriseApp) SELECT     bundle_ids.value AS bundleId,     timestamps.value AS installDate,     genre_ids.value AS genreId,     app2vec_clusters.value AS app2VecCluster,     uuids.value AS remoteAppUUID,     enterprise_apps.value AS isEnterpriseApp FROM _pas_nsarray(:bundle_ids) bundle_ids JOIN _pas_nsarray(:timestamps) timestamps ON bundle_ids.rowid = timestamps.rowid JOIN _pas_nsarray(:genre_ids) genre_ids ON bundle_ids.rowid = genre_ids.rowid JOIN _pas_nsarray(:app2vec_clusters) app2vec_clusters ON bundle_ids.rowid = app2vec_clusters.rowid JOIN _pas_nsarray(:uuids) uuids ON bundle_ids.rowid = uuids.rowid JOIN _pas_nsarray(:enterprise_apps) enterprise_apps ON bundle_ids.rowid = enterprise_apps.rowid ON CONFLICT(bundleId) DO UPDATE SET installDate = CASE     WHEN installDate IS NULL THEN excluded.installDate     ELSE installDate END, genreId = excluded.genreId, app2VecCluster = excluded.app2VecCluster, remoteAppUUID = excluded.remoteAppUUID, isEnterpriseApp = excluded.isEnterpriseApp"
+ "INSERT OR REPLACE INTO appInfo (bundleId, installDate) SELECT bundle_ids.value, 1 FROM _pas_nsarray(:bundle_ids) AS bundle_ids;"
+ "INSERT OR REPLACE INTO parameterizedSuggestions (uniqueID, encodedTool, encodedSummary) VALUES (:uniqueID, :encodedTool, :encodedSummary)"
+ "IsRemoteApp"
+ "SELECT * FROM appInfo WHERE bundleId LIKE 'remote%';"
+ "SELECT encodedTool, encodedSummary FROM parameterizedSuggestions WHERE uniqueID = :uniqueID"
+ "T^{ATXPredictionItem=@Q[828f]fBB},N,V_predictionItem"
+ "Tr^{ATXPredictionItem=@Q[828f]fBB},R,N"
+ "T{ATXPredictionItem=@Q[828f]fBB},N"
+ "UPDATE appInfo SET installDate = :new_timestamp WHERE bundleId = :bundle_id"
+ "[828f]"
+ "^{ATXPredictionItem=@Q[828f]fBB}16@0:8"
+ "_ATXDataStore: Setting install date to 1 for these existing remote apps: %@"
+ "_ATXDataStore: Updating database with remote apps dictionary: %@"
+ "_ATXScoreInputIsRemoteApp"
+ "_onQueue_notifySpotlightInvoked:"
+ "_prewarmingQueue"
+ "allRemoteApps"
+ "com.apple.Preview"
+ "com.apple.games"
+ "com.apple.journal"
+ "com.apple.proactive.AppPrediction.ATXServer.prewarmingQueue"
+ "d24@0:8^{ATXPredictionItem=@Q[828f]fBB}16"
+ "d28@0:8^{ATXPredictionItem=@Q[828f]fBB}16C24"
+ "d52@0:8^{ATXPredictionItem=@Q[828f]fBB}16@24C32@36@44"
+ "deleteParameterizedSuggestionWithUniqueIdentifier:"
+ "encodedSummary"
+ "encodedTool"
+ "fetchPIDFromServer:"
+ "fetchParameterizedSuggestionWithUniqueIdentifier:"
+ "initWithEncodedInvocation:encodedSummary:canonicalActionID:"
+ "luckMigration"
+ "q3352@0:8{ATXPredictionItem=@Q[828f]fBB}16"
+ "r^{ATXPredictionItem=@Q[828f]fBB}16@0:8"
+ "recordParamererizedSuggestionWithUniqueIdentifier:encodedTool:encodedSummary:"
+ "resetAllRecordedParameterizedSuggestions"
+ "suggestionMetadataForActions:withCompletion:"
+ "uiContextClient"
+ "updateDefaultsWithSystemDescriptors:updateCarPlayDefaults:installDatesCache:reason:"
+ "updateInstallDateForBundleID:timestamp:"
+ "updateOrInsertDataForRemoteAppsWithMappings:"
+ "v16@?0r^{ATXPredictionItem=@Q[828f]fBB}8"
+ "v24@0:8@?<v@?@\"NSNumber\"@\"NSError\">16"
+ "v24@0:8^{ATXPredictionItem=@Q[828f]fBB}16"
+ "v24@0:8r^{ATXPredictionItem=@Q[828f]fBB}16"
+ "v24@?0@\"ATXScoredPrediction\"8r^{ATXPredictionItem=@Q[828f]fBB}16"
+ "v24@?0^{ATXPredictionItem=@Q[828f]fBB}8d16"
+ "v32@0:8^{ATXPredictionItem=@Q[828f]fBB}16@24"
+ "v32@0:8r^{ATXPredictionItem=@Q[828f]fBB}16^{ATXPredictionItem=@Q[828f]fBB}24"
+ "v32@?0@\"NSString\"8@\"ATXRemoteAppPlaceholderInfo\"16^B24"
+ "v3352@0:8{ATXPredictionItem=@Q[828f]fBB}16"
+ "v3360@0:8{ATXPredictionItem=@Q[828f]fBB}16@3352"
+ "v40@0:8@16r^{ATXPredictionItem=@Q[828f]fBB}24d32"
+ "v40@0:8^{ATXPredictionItem=@Q[828f]fBB}16Q24@32"
+ "v48@0:8^{ATXPredictionItem=@Q[828f]fBB}16@24@32@40"
+ "v64@0:8r^{ATXPredictionItem=@Q[828f]fBB}16Q24Q32Q40@48Q56"
+ "{ATXPredictionItem=\"key\"@\"NSString\"\"actionHash\"Q\"inputSignals\"[828f]\"score\"f\"isMediumConfidenceForBlendingLayer\"B\"isHighConfidenceForBlendingLayer\"B}"
+ "{ATXPredictionItem=@Q[828f]fBB}16@0:8"
+ "{ATXPredictionItem=@Q[828f]fBB}24@0:8@16"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xa1"
- ":bundleID"
- "@24@0:8^{ATXPredictionItem=@Q[827f]fBB}16"
- "@24@0:8r^{ATXPredictionItem=@Q[827f]fBB}16"
- "@32@0:8^{ATXPredictionItem=@Q[827f]fBB}16@24"
- "@3352@0:8{ATXPredictionItem=@Q[827f]fBB}16"
- "@3360@0:8{ATXPredictionItem=@Q[827f]fBB}16@3352"
- "@3368@0:8{ATXPredictionItem=@Q[827f]fBB}16@3352@3360"
- "@3388@0:8@16@24@32f40@44{ATXPredictionItem=@Q[827f]fBB}52"
- "@40@0:8@16r^{ATXPredictionItem=@Q[827f]fBB}24@32"
- "@56@0:8@16r^{ATXPredictionItem=@Q[827f]fBB}24d32@40@48"
- "@64@0:8@16@24@32r^{ATXPredictionItem=@Q[827f]fBB}40d48@56"
- "@72@0:8@16@24r^{ATXPredictionItem=@Q[827f]fBB}32d40@48i56B60@64"
- "@80@0:8@16@24r^{ATXPredictionItem=@Q[827f]fBB}32d40@48i56B60^v64@72"
- "B3352@0:8{ATXPredictionItem=@Q[827f]fBB}16"
- "B40@0:8^{ATXPredictionItem=@Q[827f]fBB}16@?24^@32"
- "INSERT INTO appInfo (bundleId, installDate) VALUES (:bundleID, 1) ON CONFLICT(bundleId) DO UPDATE SET installDate = COALESCE(appInfo.installDate, excluded.installDate);"
- "T^{ATXPredictionItem=@Q[827f]fBB},N,V_predictionItem"
- "Tr^{ATXPredictionItem=@Q[827f]fBB},R,N"
- "T{ATXPredictionItem=@Q[827f]fBB},N"
- "[827f]"
- "^{ATXPredictionItem=@Q[827f]fBB}16@0:8"
- "d24@0:8^{ATXPredictionItem=@Q[827f]fBB}16"
- "d28@0:8^{ATXPredictionItem=@Q[827f]fBB}16C24"
- "d52@0:8^{ATXPredictionItem=@Q[827f]fBB}16@24C32@36@44"
- "q3352@0:8{ATXPredictionItem=@Q[827f]fBB}16"
- "r^{ATXPredictionItem=@Q[827f]fBB}16@0:8"
- "updateDefaultsWithSystemDescriptors:installDatesCache:reason:"
- "v16@?0r^{ATXPredictionItem=@Q[827f]fBB}8"
- "v24@0:8^{ATXPredictionItem=@Q[827f]fBB}16"
- "v24@0:8r^{ATXPredictionItem=@Q[827f]fBB}16"
- "v24@?0@\"ATXScoredPrediction\"8r^{ATXPredictionItem=@Q[827f]fBB}16"
- "v24@?0^{ATXPredictionItem=@Q[827f]fBB}8d16"
- "v32@0:8^{ATXPredictionItem=@Q[827f]fBB}16@24"
- "v32@0:8r^{ATXPredictionItem=@Q[827f]fBB}16^{ATXPredictionItem=@Q[827f]fBB}24"
- "v3352@0:8{ATXPredictionItem=@Q[827f]fBB}16"
- "v3360@0:8{ATXPredictionItem=@Q[827f]fBB}16@3352"
- "v40@0:8@16r^{ATXPredictionItem=@Q[827f]fBB}24d32"
- "v40@0:8^{ATXPredictionItem=@Q[827f]fBB}16Q24@32"
- "v48@0:8^{ATXPredictionItem=@Q[827f]fBB}16@24@32@40"
- "v64@0:8r^{ATXPredictionItem=@Q[827f]fBB}16Q24Q32Q40@48Q56"
- "{ATXPredictionItem=\"key\"@\"NSString\"\"actionHash\"Q\"inputSignals\"[827f]\"score\"f\"isMediumConfidenceForBlendingLayer\"B\"isHighConfidenceForBlendingLayer\"B}"
- "{ATXPredictionItem=@Q[827f]fBB}16@0:8"
- "{ATXPredictionItem=@Q[827f]fBB}24@0:8@16"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\x91"

```
