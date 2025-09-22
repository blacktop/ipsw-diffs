## momentsd

> `/usr/libexec/momentsd`

```diff

-130.0.11.0.0
-  __TEXT.__text: 0x1b4ab4
+130.0.19.0.0
+  __TEXT.__text: 0x1b701c
   __TEXT.__auth_stubs: 0x10d0
-  __TEXT.__objc_stubs: 0x16500
-  __TEXT.__objc_methlist: 0xbdc4
-  __TEXT.__objc_classname: 0x1544
-  __TEXT.__objc_methname: 0x241b5
-  __TEXT.__objc_methtype: 0x23e7
-  __TEXT.__cstring: 0x1d2b4
-  __TEXT.__oslogstring: 0x20b35
+  __TEXT.__objc_stubs: 0x16660
+  __TEXT.__objc_methlist: 0xbef4
+  __TEXT.__objc_classname: 0x155a
+  __TEXT.__objc_methname: 0x243b7
+  __TEXT.__objc_methtype: 0x242c
+  __TEXT.__cstring: 0x1d3e4
+  __TEXT.__oslogstring: 0x20ebe
   __TEXT.__const: 0x7f2
-  __TEXT.__gcc_except_tab: 0x4f00
+  __TEXT.__gcc_except_tab: 0x5098
   __TEXT.__ustring: 0x124
   __TEXT.__dlopen_cstrs: 0x51
   __TEXT.__constg_swiftt: 0x118

   __TEXT.__swift5_capture: 0x70
   __TEXT.__swift5_types: 0x8
   __TEXT.__swift5_reflstr: 0x30
-  __TEXT.__unwind_info: 0x39f8
+  __TEXT.__unwind_info: 0x3a90
   __TEXT.__eh_frame: 0x298
   __DATA_CONST.__auth_got: 0x880
   __DATA_CONST.__got: 0x2f0
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x7a90
-  __DATA_CONST.__cfstring: 0x1d420
-  __DATA_CONST.__objc_classlist: 0x5b0
+  __DATA_CONST.__const: 0x7b28
+  __DATA_CONST.__cfstring: 0x1d520
+  __DATA_CONST.__objc_classlist: 0x5b8
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_classrefs: 0x990
-  __DATA_CONST.__objc_superrefs: 0x4a8
+  __DATA_CONST.__objc_classrefs: 0x998
+  __DATA_CONST.__objc_superrefs: 0x4b0
   __DATA_CONST.__objc_intobj: 0x2b68
   __DATA_CONST.__objc_floatobj: 0x270
   __DATA_CONST.__objc_arraydata: 0xb28
   __DATA_CONST.__objc_arrayobj: 0x4e0
   __DATA_CONST.__objc_doubleobj: 0x2f0
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x15580
-  __DATA.__objc_selrefs: 0x6928
-  __DATA.__objc_ivar: 0xf9c
-  __DATA.__objc_data: 0x3a60
+  __DATA.__objc_const: 0x15740
+  __DATA.__objc_selrefs: 0x6990
+  __DATA.__objc_ivar: 0xfb0
+  __DATA.__objc_data: 0x3ab0
   __DATA.__data: 0x1078
   __DATA.__bss: 0x168
   __DATA.__common: 0xb8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 5DB4B1A7-82E2-347B-BD02-BB98DF64FF6D
-  Functions: 6199
-  Symbols:   44046
-  CStrings:  15581
+  UUID: 4F56066F-B8F1-3EA8-A41B-14C4A4B395FC
+  Functions: 6242
+  Symbols:   44323
+  CStrings:  15637
 
Symbols:
+ -[MODaemonClient _getClientsWithDataAccess:]
+ -[MODaemonClient _registerClientsForDataAccess:]
+ -[MODaemonClient acquireRefreshLock]
+ -[MODaemonClient dataAccessManager]
+ -[MODaemonClient getClientsWithDataAccess:]
+ -[MODaemonClient registerClientsForDataAccess:]
+ -[MODaemonClient releaseRefreshLock]
+ -[MODaemonClient releaseRefreshLock].cold.1
+ -[MODaemonClient setDataAccessManager:]
+ -[MODataAccessManager .cxx_destruct]
+ -[MODataAccessManager defaultsManager]
+ -[MODataAccessManager getApplicationsWithDataAccess:]
+ -[MODataAccessManager getApplicationsWithDataAccess:withinTimeInterval:]
+ -[MODataAccessManager getClientsWithDataAccess:]
+ -[MODataAccessManager getClientsWithDataAccess:withinTimeInterval:]
+ -[MODataAccessManager hasAnyApplicationsWithDataAccessWithinTimeInterval:]
+ -[MODataAccessManager hasAnyClientsWithDataAccessWithinTimeInterval:]
+ -[MODataAccessManager initWithUniverse:]
+ -[MODataAccessManager registerApplicationsForDataAccess:]
+ -[MODataAccessManager registerClientsForDataAccess:]
+ -[MODataAccessManager setDefaultsManager:]
+ -[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:].cold.1
+ -[MOEventRefreshScheduler setUniverse:]
+ -[MOEventRefreshScheduler universe]
+ -[MOOnboardingAndSettingsPersistence _onRoutineStateUpdate:error:currentTime:hasTimedout:]
+ -[MOOnboardingAndSettingsPersistence _onRoutineStateUpdate:error:currentTime:hasTimedout:].cold.1
+ -[MOOnboardingAndSettingsPersistence _onRoutineStateUpdate:error:currentTime:hasTimedout:].cold.2
+ -[MOOnboardingAndSettingsPersistence _onRoutineStateUpdate:error:currentTime:hasTimedout:].cold.3
+ -[MOOnboardingAndSettingsPersistence dataAccessManager]
+ -[MOOnboardingAndSettingsPersistence setDataAccessManager:]
+ /Library/Caches/com.apple.xbs/Binaries/Moments/install/TempContent/Objects/Moments.build/momentsd.build/Objects-normal/arm64e/MODataAccessManager.o
+ GCC_except_table113
+ GCC_except_table119
+ GCC_except_table123
+ GCC_except_table127
+ GCC_except_table135
+ GCC_except_table140
+ GCC_except_table158
+ GCC_except_table164
+ GCC_except_table167
+ GCC_except_table170
+ GCC_except_table173
+ GCC_except_table88
+ GCC_except_table92
+ MODataAccessManager.m
+ OBJC_IVAR_$_MODaemonClient._dataAccessManager
+ OBJC_IVAR_$_MODaemonClient._refreshLock
+ OBJC_IVAR_$_MODataAccessManager._defaultsManager
+ OBJC_IVAR_$_MOEventRefreshScheduler._universe
+ OBJC_IVAR_$_MOOnboardingAndSettingsPersistence._dataAccessManager
+ _OBJC_CLASS_$_MODataAccessManager
+ _OBJC_METACLASS_$_MODataAccessManager
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.230
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.230.cold.1
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.236
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.236.cold.1
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.239
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.239.cold.1
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.241
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.241.cold.1
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.245
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.245.cold.1
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.231
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.237
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.232
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.238
+ __23-[MODaemonUniverse run]_block_invoke.107
+ __38-[MOEventManager storeEvents:handler:]_block_invoke.278
+ __43-[MODaemonClient getClientsWithDataAccess:]_block_invoke.cold.1
+ __44-[MOEventManager _purgePreOnboardingEvents:]_block_invoke.457
+ __44-[MOEventManager _purgePreOnboardingEvents:]_block_invoke.458
+ __47-[MODaemonClient registerClientsForDataAccess:]_block_invoke.cold.1
+ __47-[MOEventManager _rehydrateEvents:withHandler:]_block_invoke.320
+ __48-[MOEventManager _updateEventsDeletedAtSources:]_block_invoke.425
+ __48-[MOEventManager _updateEventsDeletedAtSources:]_block_invoke.426
+ __50-[MODaemonClient getMomentsNotificationsSchedule:]_block_invoke.216
+ __53-[MOManageServer listener:shouldAcceptNewConnection:]_block_invoke.176
+ __56-[MODaemonClient printEvergreenBundlesWithSeed:handler:]_block_invoke.485
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.327
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.331
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.335
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.345
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.355
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.359
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.363
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.367
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.371
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.375
+ __59-[MOEventManager fetchEventsWithOptions:CompletionHandler:]_block_invoke.285
+ __60-[MODaemonClient _logEngagementEvent:timestamp:withContext:]_block_invoke.405
+ __60-[MODaemonClient _logEngagementEvent:timestamp:withContext:]_block_invoke.406
+ __60-[MOEventManager _fetchEventsWithOptions:CompletionHandler:]_block_invoke.289
+ __60-[MOEventManager _fetchEventsWithOptions:CompletionHandler:]_block_invoke.291
+ __60-[MOEventManager _fetchEventsWithOptions:CompletionHandler:]_block_invoke.293
+ __60-[MOEventManager runAnalyticsWithRefreshVariant:andHandler:]_block_invoke.468
+ __60-[MOEventManager runAnalyticsWithRefreshVariant:andHandler:]_block_invoke.484
+ __60-[MOEventManager runAnalyticsWithRefreshVariant:andHandler:]_block_invoke.484.cold.1
+ __61-[MOEventManager _updateEventsDeletedAtSingleSource:handler:]_block_invoke.433
+ __61-[MOEventManager _updateEventsDeletedAtSingleSource:handler:]_block_invoke.437
+ __61-[MOEventManager _updateEventsDeletedAtSingleSource:handler:]_block_invoke.441
+ __61-[MOEventManager _updateEventsDeletedAtSingleSource:handler:]_block_invoke.445
+ __61-[MOEventManager _updateEventsDeletedAtSingleSource:handler:]_block_invoke.449
+ __61-[MOEventManager _updateEventsDeletedAtSingleSource:handler:]_block_invoke.453
+ __61-[MOEventManager cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.379
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.392
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.392.cold.1
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.396
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.403
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.403.cold.1
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.410
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.410.cold.1
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.414
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.414.cold.1
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.418.cold.1
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.419
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.419.cold.1
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.421
+ __65-[MODaemonClient _fetchEventsWithOptions:withContext:andHandler:]_block_invoke.230
+ __65-[MODaemonClient _fetchEventsWithOptions:withContext:andHandler:]_block_invoke.235
+ __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.252
+ __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.253
+ __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.254
+ __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.258
+ __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.259
+ __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.263
+ __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.272
+ __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.273
+ __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.274
+ __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke_2.cold.1
+ __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.177
+ __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.181
+ __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.182
+ __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.186
+ __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.187
+ __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.191
+ __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.192
+ __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.196
+ __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.197
+ __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.201
+ __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.201.cold.1
+ __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.202
+ __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.206
+ __71-[MODaemonClient _fetchEventBundlesWithOptions:withContext:andHandler:]_block_invoke.257
+ __71-[MODaemonClient _purgeEventsWithContext:andRefreshVariant:andHandler:]_block_invoke.281
+ __71-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterOnboarding]_block_invoke.218
+ __71-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterOnboarding]_block_invoke_2.219
+ __74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke.236
+ __74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke.238
+ __74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke.239
+ __74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke.239.cold.1
+ __82-[MODaemonClient _analyzeTrendsInEvents:withContext:andRefreshVariant:andHandler:]_block_invoke.297
+ __82-[MOEventRefreshScheduler _purgeEventsAndBundlesWithRefreshVariant:andCompletion:]_block_invoke.219
+ __84-[MODaemonClient didAppEntryUpdateUsingSuggestions:onEvent:duringInterval:withInfo:]_block_invoke.417
+ __84-[MOEventManager _fetchEventsFromDBAndRehydrateEventsWithOptions:CompletionHandler:]_block_invoke.299
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.333
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.334
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.339
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.343.cold.1
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.345
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.349
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.349.cold.1
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.349.cold.2
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.350
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.354
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.355
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.359
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.359.cold.1
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.360
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.364
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.365
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.369
+ __OBJC_$_INSTANCE_METHODS_MODataAccessManager
+ __OBJC_$_INSTANCE_VARIABLES_MODataAccessManager
+ __OBJC_$_PROP_LIST_MODataAccessManager
+ __OBJC_CLASS_RO_$_MODataAccessManager
+ __OBJC_METACLASS_RO_$_MODataAccessManager
+ ___43-[MODaemonClient getClientsWithDataAccess:]_block_invoke
+ ___47-[MODaemonClient registerClientsForDataAccess:]_block_invoke
+ ___67-[MODataAccessManager getClientsWithDataAccess:withinTimeInterval:]_block_invoke
+ ___69-[MODataAccessManager hasAnyClientsWithDataAccessWithinTimeInterval:]_block_invoke
+ ___72-[MODataAccessManager getApplicationsWithDataAccess:withinTimeInterval:]_block_invoke
+ ___74-[MODataAccessManager hasAnyApplicationsWithDataAccessWithinTimeInterval:]_block_invoke
+ ___79-[MOOnboardingAndSettingsPersistence _fetchSignificantLocationEnablementStatus]_block_invoke_2
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s96r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8r96l8
+ ___block_descriptor_112_e8_32s40s48s56s64s72s80s88s96s104r_e34_v24?0"NSError"8"NSDictionary"16ls32l8s40l8s48l8s56l8s64l8s72l8r104l8s80l8s88l8s96l8
+ ___block_descriptor_112_e8_32s40s48s56s64s72s80s88s96s104s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8
+ ___block_descriptor_113_e8_32s40s48s56s64s72s80bs88r96r_e5_v8?0ls32l8s40l8s80l8s48l8s56l8s64l8r88l8s72l8r96l8
+ ___block_descriptor_120_e8_32s40s48s56s64s72s80s88s96s104s112r_e5_v8?0ls32l8s40l8r112l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8
+ ___block_descriptor_120_e8_32s40s48s56s64s72s80s88s96s104s112r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8r112l8s96l8s104l8
+ ___block_descriptor_120_e8_32s40s48s56s64s72s80s88s96s104s112s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8
+ ___block_descriptor_128_e8_32s40s48s56s64s72s80s88s96s104s112bs120r_e5_v8?0ls32l8s40l8s48l8s56l8r120l8s64l8s72l8s80l8s88l8s96l8s112l8s104l8
+ ___block_descriptor_128_e8_32s40s48s56s64s72s80s88s96s104s112s120r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8r120l8s104l8s112l8
+ ___block_descriptor_56_e8_32bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8
+ ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e34_v24?0"NSError"8"NSDictionary"16ls56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e17_v16?0"NSError"8ls32l8s40l8r64l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56bs64r72r_e5_v8?0ls56l8s32l8r64l8s40l8r72l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56bs64r_e5_v8?0ls56l8r64l8s32l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s64r72r_e29_v24?0"NSArray"8"NSError"16ls32l8r64l8s40l8r72l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8r72l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e34_v24?0"NSError"8"NSDictionary"16ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72r80r_e5_v8?0ls32l8r72l8s40l8r80l8s48l8s56l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80r_e34_v24?0"NSError"8"NSDictionary"16ls32l8s40l8s48l8s56l8r80l8s64l8s72l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80s_e34_v24?0"NSError"8"NSDictionary"16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80s88r_e34_v24?0"NSError"8"NSDictionary"16ls32l8s40l8s48l8s56l8s64l8r88l8s72l8s80l8
+ ___block_descriptor_97_e8_32s40s48s56s64bs72r80r_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s64l8s48l8s56l8r72l8r80l8
+ __block_literal_global.178
+ __block_literal_global.399
+ __block_literal_global.408
+ __block_literal_global.410
+ __block_literal_global.412
+ __block_literal_global.451
+ __block_literal_global.453
+ __block_literal_global.489
+ __block_literal_global.494
+ _objc_msgSend$_getClientsWithDataAccess:
+ _objc_msgSend$_onRoutineStateUpdate:error:currentTime:hasTimedout:
+ _objc_msgSend$_registerClientsForDataAccess:
+ _objc_msgSend$acquireRefreshLock
+ _objc_msgSend$dataAccessManager
+ _objc_msgSend$getApplicationsWithDataAccess:withinTimeInterval:
+ _objc_msgSend$getClientsWithDataAccess:
+ _objc_msgSend$getClientsWithDataAccess:withinTimeInterval:
+ _objc_msgSend$registerApplicationsForDataAccess:
+ _objc_msgSend$registerClientsForDataAccess:
+ _objc_msgSend$releaseRefreshLock
- GCC_except_table111
- GCC_except_table117
- GCC_except_table121
- GCC_except_table125
- GCC_except_table133
- GCC_except_table138
- GCC_except_table150
- GCC_except_table153
- GCC_except_table156
- GCC_except_table159
- GCC_except_table162
- GCC_except_table165
- GCC_except_table90
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.227
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.231
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.231.cold.1
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.237
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.237.cold.1
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.240
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.242
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.242.cold.1
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.242.cold.2
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.232
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.238
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.233
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.239
- __23-[MODaemonUniverse run]_block_invoke.106
- __38-[MOEventManager storeEvents:handler:]_block_invoke.275
- __44-[MOEventManager _purgePreOnboardingEvents:]_block_invoke.454
- __44-[MOEventManager _purgePreOnboardingEvents:]_block_invoke.455
- __47-[MOEventManager _rehydrateEvents:withHandler:]_block_invoke.317
- __48-[MOEventManager _updateEventsDeletedAtSources:]_block_invoke.422
- __48-[MOEventManager _updateEventsDeletedAtSources:]_block_invoke.423
- __50-[MODaemonClient getMomentsNotificationsSchedule:]_block_invoke.215
- __53-[MOManageServer listener:shouldAcceptNewConnection:]_block_invoke.174
- __56-[MODaemonClient printEvergreenBundlesWithSeed:handler:]_block_invoke.479
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.324
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.328
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.332
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.342
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.352
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.356
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.360
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.364
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.368
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.372
- __59-[MOEventManager fetchEventsWithOptions:CompletionHandler:]_block_invoke.282
- __60-[MODaemonClient _logEngagementEvent:timestamp:withContext:]_block_invoke.398
- __60-[MODaemonClient _logEngagementEvent:timestamp:withContext:]_block_invoke.399
- __60-[MOEventManager _fetchEventsWithOptions:CompletionHandler:]_block_invoke.286
- __60-[MOEventManager _fetchEventsWithOptions:CompletionHandler:]_block_invoke.287
- __60-[MOEventManager _fetchEventsWithOptions:CompletionHandler:]_block_invoke.288
- __60-[MOEventManager runAnalyticsWithRefreshVariant:andHandler:]_block_invoke.465
- __60-[MOEventManager runAnalyticsWithRefreshVariant:andHandler:]_block_invoke.481
- __60-[MOEventManager runAnalyticsWithRefreshVariant:andHandler:]_block_invoke.481.cold.1
- __61-[MOEventManager _updateEventsDeletedAtSingleSource:handler:]_block_invoke.430
- __61-[MOEventManager _updateEventsDeletedAtSingleSource:handler:]_block_invoke.434
- __61-[MOEventManager _updateEventsDeletedAtSingleSource:handler:]_block_invoke.438
- __61-[MOEventManager _updateEventsDeletedAtSingleSource:handler:]_block_invoke.442
- __61-[MOEventManager _updateEventsDeletedAtSingleSource:handler:]_block_invoke.446
- __61-[MOEventManager _updateEventsDeletedAtSingleSource:handler:]_block_invoke.450
- __61-[MOEventManager cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.376
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.389
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.389.cold.1
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.393
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.400
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.400.cold.1
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.407
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.407.cold.1
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.411
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.411.cold.1
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.415
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.415.cold.1
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.416
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.416.cold.1
- __65-[MODaemonClient _fetchEventsWithOptions:withContext:andHandler:]_block_invoke.229
- __65-[MODaemonClient _fetchEventsWithOptions:withContext:andHandler:]_block_invoke.234
- __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.249
- __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.250
- __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.251
- __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.255
- __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.256
- __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.260
- __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.264
- __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.265
- __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.266
- __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.174
- __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.178
- __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.179
- __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.183
- __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.184
- __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.188
- __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.189
- __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.193
- __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.194
- __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.198
- __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.198.cold.1
- __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.199
- __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.203
- __71-[MODaemonClient _fetchEventBundlesWithOptions:withContext:andHandler:]_block_invoke.256
- __71-[MODaemonClient _purgeEventsWithContext:andRefreshVariant:andHandler:]_block_invoke.279
- __71-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterOnboarding]_block_invoke.217
- __71-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterOnboarding]_block_invoke_2.218
- __74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke.227
- __74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke.229
- __74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke.230
- __74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke.230.cold.1
- __82-[MODaemonClient _analyzeTrendsInEvents:withContext:andRefreshVariant:andHandler:]_block_invoke.296
- __82-[MOEventRefreshScheduler _purgeEventsAndBundlesWithRefreshVariant:andCompletion:]_block_invoke.208
- __84-[MODaemonClient didAppEntryUpdateUsingSuggestions:onEvent:duringInterval:withInfo:]_block_invoke.410
- __84-[MOEventManager _fetchEventsFromDBAndRehydrateEventsWithOptions:CompletionHandler:]_block_invoke.296
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.326
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.327
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.331
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.332
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.336
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.336.cold.1
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.342
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.342.cold.1
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.342.cold.2
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.347
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.348
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.352
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.352.cold.1
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.353
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.357
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.358
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.362
- ___block_descriptor_104_e8_32s40s48s56s64bs72r80r88r96r_e5_v8?0ls32l8s40l8s48l8s56l8r72l8s64l8r80l8r88l8r96l8
- ___block_descriptor_105_e8_32s40s48s56s64s72bs80r88r_e5_v8?0ls32l8s40l8s48l8s56l8r80l8s64l8r88l8s72l8
- ___block_descriptor_112_e8_32s40s48s56s64s72bs80r88r96r104r_e34_v24?0"NSError"8"NSDictionary"16ls32l8s40l8r80l8s72l8r88l8r96l8r104l8s48l8s56l8s64l8
- ___block_descriptor_112_e8_32s40s48s56s64s72s80s88r96r104r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8r88l8r96l8r104l8s72l8s80l8
- ___block_descriptor_120_e8_32s40s48s56s64s72bs80r88r96r104r112r_e5_v8?0lr80l8r88l8r96l8r104l8r112l8s32l8s40l8s48l8s56l8s72l8s64l8
- ___block_descriptor_120_e8_32s40s48s56s64s72s80bs88r96r104r112r_e5_v8?0ls32l8r88l8r96l8s40l8s48l8s56l8r104l8s80l8r112l8s64l8s72l8
- ___block_descriptor_120_e8_32s40s48s56s64s72s80s88r96r104r112r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8r88l8r96l8r104l8r112l8s72l8s80l8
- ___block_descriptor_128_e8_32s40s48s56s64s72s80s88r96r104r112r120r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8r88l8r96l8r104l8r112l8r120l8s72l8s80l8
- ___block_descriptor_56_e8_32s40r48r_e5_v8?0ls32l8r40l8r48l8
- ___block_descriptor_72_e8_32s40s48bs56r64r_e34_v24?0"NSError"8"NSDictionary"16lr56l8s48l8r64l8s32l8s40l8
- ___block_descriptor_72_e8_32s40s48bs56r_e5_v8?0ls48l8r56l8s32l8s40l8
- ___block_descriptor_72_e8_32s40s48r56r64r_e5_v8?0ls32l8s40l8r48l8r56l8r64l8
- ___block_descriptor_72_e8_32s40s48s56bs64r_e5_v8?0ls56l8s32l8r64l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56r64r_e17_v16?0"NSError"8ls32l8r56l8r64l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56s64r_e29_v24?0"NSArray"8"NSError"16ls32l8r64l8s40l8s48l8s56l8
- ___block_descriptor_80_e8_32s40s48r56r64r72r_e5_v8?0ls32l8s40l8r48l8r56l8r64l8r72l8
- ___block_descriptor_80_e8_32s40s48s56r64r72r_e34_v24?0"NSError"8"NSDictionary"16ls32l8r56l8r64l8r72l8s40l8s48l8
- ___block_descriptor_80_e8_32s40s48s56s64s72r_e5_v8?0ls32l8r72l8s40l8s48l8s56l8s64l8
- ___block_descriptor_88_e8_32s40s48r56r64r72r80r_e5_v8?0ls32l8s40l8r48l8r56l8r64l8r72l8r80l8
- ___block_descriptor_88_e8_32s40s48s56r64r72r80r_e34_v24?0"NSError"8"NSDictionary"16ls32l8r56l8r64l8r72l8r80l8s40l8s48l8
- ___block_descriptor_96_e8_32s40s48s56r64r72r80r88r_e34_v24?0"NSError"8"NSDictionary"16ls32l8r56l8r64l8r72l8r80l8r88l8s40l8s48l8
- ___block_descriptor_97_e8_32s40s48s56s64bs72r80r_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s48l8s56l8r72l8r80l8s64l8
- __block_literal_global.176
- __block_literal_global.392
- __block_literal_global.401
- __block_literal_global.403
- __block_literal_global.405
- __block_literal_global.447
- __block_literal_global.483
- __block_literal_global.488
CStrings:
+ "\x01\x114"
+ "\x11\x1c"
+ "\x1b"
+ "@\"MODataAccessManager\""
+ "B24@0:8d16"
+ "ClientsWithDataAccess"
+ "Conditions for checking RT state: %i,%i,%i"
+ "Delaying RT state retrieval by %f seconds..."
+ "Fetching events for bundling failed. reason, %@"
+ "Keeping cached RT state: %@"
+ "MODataAccessManager"
+ "MOEventRefreshSchduler"
+ "Refresh: RefreshLock is acquired. Running refresh."
+ "Refresh: RefreshLock is in use. Exiting early due to exiting refresh"
+ "Refresh: RefreshLock is released"
+ "RefreshLock is acquired. Eligible to run soft refresh"
+ "RefreshLock is in use. Drop the refresh."
+ "RefreshLock is in use. Drop the soft refresh."
+ "RefreshLock is released."
+ "Release an invalid refresh lock"
+ "Remove old real time visits events failed"
+ "Retrieved RT state from storage: %@"
+ "SettingsOverrideSignificantLocationMasterSwitchRetrievalDelay"
+ "SettingsSignificantLocationMasterSwitchCache"
+ "T@\"MODataAccessManager\",&,N,V_dataAccessManager"
+ "The refresh is dropped due to an existing refresh."
+ "Timedout RT state response with state: %@ and no error"
+ "Unexpected RT state response with state: %@ and no error"
+ "Updated and persisted RT state: %@"
+ "_dataAccessManager"
+ "_getClientsWithDataAccess:"
+ "_onRoutineStateUpdate:error:currentTime:hasTimedout:"
+ "_refreshLock"
+ "_registerClientsForDataAccess:"
+ "_rehydrateEvents, DONE, all original events count, %lu, all rehydrated events count, %lu, error, %@"
+ "_rehydrateEventsAtSingleSource, DONE, keyword, %@, original events count, %lu, rehydrated events count, %lu, error, %@"
+ "acquireRefreshLock"
+ "dataAccessManager"
+ "detected error when trying to remove old real time visits events, %@"
+ "getApplicationsWithDataAccess:withinTimeInterval:"
+ "getClientsWithDataAccess:"
+ "getClientsWithDataAccess:withinTimeInterval:"
+ "hasAnyApplicationsWithDataAccessWithinTimeInterval:"
+ "hasAnyClientsWithDataAccessWithinTimeInterval:"
+ "isHighConfidence == NO"
+ "registerClientsForDataAccess:"
+ "releaseRefreshLock"
+ "remove old real time visits events succeeded and continue refresh, removed events count %lu"
+ "routineStateRetrievalQueue"
+ "setDataAccessManager:"
+ "trying to remove event, id, %@, provider, %@, category, %@, startDate, %@"
+ "v32@0:8@?16d24"
+ "v44@0:8q16@24d32B40"
- "\x01\x113"
- "\x11\x1b"
- "Eligible to run soft refresh"
- "Updated RT state: %@"
- "_rehydrateEvents, DONE, all original events count, %lu, all rehydrated events count, %lu"
- "_rehydrateEventsAtSingleSource, DONE, keyword, %@, original events count, %lu, rehydrated events count, %lu"

```
