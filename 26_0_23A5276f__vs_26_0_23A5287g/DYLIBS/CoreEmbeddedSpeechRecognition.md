## CoreEmbeddedSpeechRecognition

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/CoreEmbeddedSpeechRecognition`

```diff

-3500.104.2.0.0
-  __TEXT.__text: 0x17e874
-  __TEXT.__auth_stubs: 0x2d70
-  __TEXT.__objc_methlist: 0x3fe0
-  __TEXT.__const: 0x1600
-  __TEXT.__cstring: 0xab7b
+3500.110.4.0.0
+  __TEXT.__text: 0x182d64
+  __TEXT.__auth_stubs: 0x2d80
+  __TEXT.__objc_methlist: 0x41a8
+  __TEXT.__const: 0x1618
+  __TEXT.__cstring: 0xb334
   __TEXT.__swift5_typeref: 0x1c76
-  __TEXT.__swift5_capture: 0x4680
+  __TEXT.__swift5_capture: 0x46c0
   __TEXT.__constg_swiftt: 0xa74
   __TEXT.__swift5_reflstr: 0x893
   __TEXT.__swift5_fieldmd: 0x7f8

   __TEXT.__swift5_assocty: 0x150
   __TEXT.__swift5_proto: 0xa0
   __TEXT.__swift5_types: 0xa0
-  __TEXT.__oslogstring: 0x7d71
+  __TEXT.__oslogstring: 0x8304
   __TEXT.__swift_as_entry: 0x160
   __TEXT.__swift_as_ret: 0x1c0
-  __TEXT.__gcc_except_tab: 0xb58
-  __TEXT.__unwind_info: 0x2268
+  __TEXT.__gcc_except_tab: 0xc40
+  __TEXT.__unwind_info: 0x2360
   __TEXT.__eh_frame: 0x2360
-  __TEXT.__objc_classname: 0xa0f
-  __TEXT.__objc_methname: 0xd573
-  __TEXT.__objc_methtype: 0x2c76
-  __TEXT.__objc_stubs: 0x72a0
-  __DATA_CONST.__got: 0xf48
-  __DATA_CONST.__const: 0x1418
-  __DATA_CONST.__objc_classlist: 0x2b0
+  __TEXT.__objc_classname: 0xa6c
+  __TEXT.__objc_methname: 0xda30
+  __TEXT.__objc_methtype: 0x2cf4
+  __TEXT.__objc_stubs: 0x77a0
+  __DATA_CONST.__got: 0xf78
+  __DATA_CONST.__const: 0x14e0
+  __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0xb8
+  __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c58
+  __DATA_CONST.__objc_selrefs: 0x2d78
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_superrefs: 0x1f0
+  __DATA_CONST.__objc_superrefs: 0x200
   __DATA_CONST.__objc_arraydata: 0x190
-  __AUTH_CONST.__auth_got: 0x16d0
-  __AUTH_CONST.__const: 0xbc88
-  __AUTH_CONST.__cfstring: 0x4860
-  __AUTH_CONST.__objc_const: 0x8110
+  __AUTH_CONST.__auth_got: 0x16d8
+  __AUTH_CONST.__const: 0xbdc0
+  __AUTH_CONST.__cfstring: 0x4960
+  __AUTH_CONST.__objc_const: 0x8388
   __AUTH_CONST.__objc_intobj: 0x630
   __AUTH_CONST.__objc_arrayobj: 0x1e0
-  __AUTH.__objc_data: 0xba0
+  __AUTH.__objc_data: 0xbf0
   __AUTH.__data: 0x808
-  __DATA.__objc_ivar: 0x510
-  __DATA.__data: 0x13f0
-  __DATA.__bss: 0xd68
+  __DATA.__objc_ivar: 0x530
+  __DATA.__data: 0x14b0
+  __DATA.__bss: 0xd88
   __DATA.__common: 0x90
   __DATA_DIRTY.__objc_data: 0xde0
   __DATA_DIRTY.__data: 0x10c8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 17F6997A-679E-32B9-9012-FD9A60445BF3
-  Functions: 4558
-  Symbols:   5781
-  CStrings:  4550
+  UUID: 0DDF1FF9-1749-359A-8E1F-BC9BD6DBEAB3
+  Functions: 4628
+  Symbols:   5998
+  CStrings:  4667
 
Symbols:
+ +[CESRSpeechProfileDispatcher _supportedDarwinNotifications]
+ +[CESRSpeechProfileDispatcher sharedDispatcher]
+ +[CoreEmbeddedSpeechRecognizer handlePostInstallSubscriptions]
+ -[CESRBackgroundSystemTask .cxx_destruct]
+ -[CESRBackgroundSystemTask _registerAndSubmitAllBGSystemTasks]
+ -[CESRBackgroundSystemTask init]
+ -[CESRSpeechProfileDispatcher .cxx_destruct]
+ -[CESRSpeechProfileDispatcher _adminServiceProvider]
+ -[CESRSpeechProfileDispatcher _adminServiceShouldAcceptNewConnection:]
+ -[CESRSpeechProfileDispatcher _defaultTaskCoalescerWithQueue:]
+ -[CESRSpeechProfileDispatcher _initWithQueue:]
+ -[CESRSpeechProfileDispatcher _initWithQueue:adminServiceProvider:speechProfileSiteManager:]
+ -[CESRSpeechProfileDispatcher _listenerWithMachServiceName:delegate:]
+ -[CESRSpeechProfileDispatcher _notifyChangeToSets:]
+ -[CESRSpeechProfileDispatcher _speechProfileSiteManager]
+ -[CESRSpeechProfileDispatcher _wait]
+ -[CESRSpeechProfileDispatcher adminServiceListener]
+ -[CESRSpeechProfileDispatcher handleDarwinNotificationEventWithName:]
+ -[CESRSpeechProfileDispatcher init]
+ -[CESRSpeechProfileDispatcher listener:shouldAcceptNewConnection:]
+ -[CESRSpeechProfileDispatcher resourceAvailableForPersona:]
+ -[CESRSpeechProfileDispatcher resourceUnavailableForPersona:]
+ -[CESRSpeechProfileDispatcher resourceUnavailableSoonForPersona:]
+ -[CESRSpeechProfileDispatcher runMaintenanceWithShouldDefer:completion:]
+ -[CESRSpeechProfileDispatcher runMigration:]
+ -[CESRSpeechProfileDispatcher setupXPCListeners]
+ -[CESRSpeechProfileDispatcher snapshotBookmarksForLocale:toPath:]
+ -[CESRSpeechProfileDispatcher taskCoalescer]
+ -[CESRSpeechProfileSiteManager _snapshotBookmarksForLocale:toPath:]
+ -[CESRSpeechProfileSiteManager _snapshotSiteAtURL:locale:changeRegistry:]
+ -[CESRSpeechProfileSiteManager snapshotBookmarksForLocale:toPath:]
+ -[CESRSpeechProfileSiteWriter addBookmarksForLocale:toChangeRegistry:]
+ GCC_except_table1031
+ GCC_except_table1032
+ GCC_except_table1033
+ GCC_except_table1034
+ GCC_except_table1035
+ GCC_except_table1036
+ GCC_except_table104
+ GCC_except_table1040
+ GCC_except_table1041
+ GCC_except_table1044
+ GCC_except_table1181
+ GCC_except_table1271
+ GCC_except_table1277
+ GCC_except_table1282
+ GCC_except_table1286
+ GCC_except_table1330
+ GCC_except_table1338
+ GCC_except_table1343
+ GCC_except_table1347
+ GCC_except_table141
+ GCC_except_table162
+ GCC_except_table175
+ GCC_except_table252
+ GCC_except_table271
+ GCC_except_table274
+ GCC_except_table320
+ GCC_except_table341
+ GCC_except_table491
+ GCC_except_table503
+ GCC_except_table506
+ GCC_except_table509
+ GCC_except_table512
+ GCC_except_table515
+ GCC_except_table518
+ GCC_except_table521
+ GCC_except_table612
+ GCC_except_table647
+ GCC_except_table680
+ GCC_except_table875
+ GCC_except_table880
+ GCC_except_table979
+ _AFIsATVOnly
+ _AFLanguageCodeDidChangeDarwinNotification
+ _OBJC_CLASS_$_CCSetChangeXPCListener
+ _OBJC_CLASS_$_CESRSpeechProfileDispatcher
+ _OBJC_IVAR_$_CESRBackgroundSystemTask._queue
+ _OBJC_IVAR_$_CESRSpeechProfileDispatcher._adminServiceListener
+ _OBJC_IVAR_$_CESRSpeechProfileDispatcher._adminServiceProvider
+ _OBJC_IVAR_$_CESRSpeechProfileDispatcher._queue
+ _OBJC_IVAR_$_CESRSpeechProfileDispatcher._setChangeListener
+ _OBJC_IVAR_$_CESRSpeechProfileDispatcher._speechProfileSiteManager
+ _OBJC_IVAR_$_CESRSpeechProfileDispatcher._supportedNotifications
+ _OBJC_IVAR_$_CESRSpeechProfileDispatcher._taskCoalescer
+ _OBJC_METACLASS_$_CESRSpeechProfileDispatcher
+ __OBJC_$_CLASS_METHODS_CESRSpeechProfileDispatcher
+ __OBJC_$_INSTANCE_METHODS_CESRSpeechProfileDispatcher
+ __OBJC_$_INSTANCE_VARIABLES_CESRBackgroundSystemTask
+ __OBJC_$_INSTANCE_VARIABLES_CESRSpeechProfileDispatcher
+ __OBJC_$_PROP_LIST_CESRSpeechProfileDispatcher
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CESRSpeechProfileResourceMonitorDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSXPCListenerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CESRSpeechProfileResourceMonitorDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSXPCListenerDelegate
+ __OBJC_$_PROTOCOL_REFS_CESRSpeechProfileResourceMonitorDelegate
+ __OBJC_$_PROTOCOL_REFS_NSXPCListenerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_CESRSpeechProfileDispatcher
+ __OBJC_CLASS_RO_$_CESRSpeechProfileDispatcher
+ __OBJC_LABEL_PROTOCOL_$_CESRSpeechProfileResourceMonitorDelegate
+ __OBJC_LABEL_PROTOCOL_$_NSXPCListenerDelegate
+ __OBJC_METACLASS_RO_$_CESRSpeechProfileDispatcher
+ __OBJC_PROTOCOL_$_CESRSpeechProfileResourceMonitorDelegate
+ __OBJC_PROTOCOL_$_NSXPCListenerDelegate
+ ___36-[CESRSpeechProfileDispatcher _wait]_block_invoke
+ ___44-[CESRSpeechProfileDispatcher runMigration:]_block_invoke
+ ___47+[CESRSpeechProfileDispatcher sharedDispatcher]_block_invoke
+ ___48-[CESRSpeechProfileDispatcher setupXPCListeners]_block_invoke
+ ___51-[CESRSpeechProfileDispatcher _notifyChangeToSets:]_block_invoke
+ ___58-[CESRBackgroundSystemTask registerAndSubmitBGSystemTasks]_block_invoke
+ ___59-[CESRSpeechProfileDispatcher resourceAvailableForPersona:]_block_invoke
+ ___60+[CESRSpeechProfileDispatcher _supportedDarwinNotifications]_block_invoke
+ ___61-[CESRSpeechProfileDispatcher resourceUnavailableForPersona:]_block_invoke
+ ___62+[CoreEmbeddedSpeechRecognizer handlePostInstallSubscriptions]_block_invoke
+ ___62+[CoreEmbeddedSpeechRecognizer handlePostInstallSubscriptions]_block_invoke.350
+ ___62-[CESRSpeechProfileSiteManager handleSiteAvailableForPersona:]_block_invoke.316
+ ___65-[CESRSpeechProfileDispatcher resourceUnavailableSoonForPersona:]_block_invoke
+ ___65-[CESRSpeechProfileDispatcher snapshotBookmarksForLocale:toPath:]_block_invoke
+ ___66-[CESRSpeechProfileSiteManager snapshotBookmarksForLocale:toPath:]_block_invoke
+ ___67-[CESRSpeechProfileSiteManager _snapshotBookmarksForLocale:toPath:]_block_invoke
+ ___69-[CESRSpeechProfileDispatcher handleDarwinNotificationEventWithName:]_block_invoke
+ ___69-[CESRSpeechProfileDispatcher handleDarwinNotificationEventWithName:]_block_invoke.55
+ ___69-[CESRSpeechProfileDispatcher handleDarwinNotificationEventWithName:]_block_invoke_2
+ ___69-[CESRSpeechProfileDispatcher handleDarwinNotificationEventWithName:]_block_invoke_3
+ ___69-[CESRSpeechProfileDispatcher handleDarwinNotificationEventWithName:]_block_invoke_4
+ ___69-[CESRSpeechProfileDispatcher handleDarwinNotificationEventWithName:]_block_invoke_5
+ ___70-[CESRSpeechProfileDispatcher _adminServiceShouldAcceptNewConnection:]_block_invoke
+ ___70-[CESRSpeechProfileSiteWriter addBookmarksForLocale:toChangeRegistry:]_block_invoke
+ ___70-[CESRSpeechProfileSiteWriter addBookmarksForLocale:toChangeRegistry:]_block_invoke.296
+ ___72-[CESRSpeechProfileDispatcher runMaintenanceWithShouldDefer:completion:]_block_invoke
+ ___83-[CESRSpeechProfileSiteWriter _updateRequiredProfileInstancesWithSets:shouldDefer:]_block_invoke.311
+ ___Block_byref_object_copy_.1363
+ ___Block_byref_object_copy_.1839
+ ___Block_byref_object_copy_.2090
+ ___Block_byref_object_copy_.2796
+ ___Block_byref_object_copy_.3264
+ ___Block_byref_object_copy_.409
+ ___Block_byref_object_copy_.4382
+ ___Block_byref_object_copy_.475
+ ___Block_byref_object_copy_.878
+ ___Block_byref_object_copy_.992
+ ___Block_byref_object_dispose_.1364
+ ___Block_byref_object_dispose_.1840
+ ___Block_byref_object_dispose_.2091
+ ___Block_byref_object_dispose_.2797
+ ___Block_byref_object_dispose_.3265
+ ___Block_byref_object_dispose_.410
+ ___Block_byref_object_dispose_.4383
+ ___Block_byref_object_dispose_.476
+ ___Block_byref_object_dispose_.879
+ ___Block_byref_object_dispose_.993
+ ____registerAndSubmitDailyAssetSubscriptionCleanupBGST_block_invoke
+ ____registerAndSubmitDailyAssetSubscriptionCleanupBGST_block_invoke_2
+ ____registerAndSubmitDailySpeechProfileMaintenanceBGST_block_invoke
+ ____registerAndSubmitDailySpeechProfileMaintenanceBGST_block_invoke_2
+ ____registerAndSubmitPostInstallANECompilationBGST_block_invoke
+ ____registerAndSubmitPostInstallANECompilationBGST_block_invoke_2
+ ____registerAndSubmitPostInstallAssetSubscriptionBGST_block_invoke
+ ____registerAndSubmitPostInstallAssetSubscriptionBGST_block_invoke_2
+ ____registerAndSubmitPostInstallSpeechProfileMigrationBGST_block_invoke
+ ____registerAndSubmitPostInstallSpeechProfileMigrationBGST_block_invoke_2
+ ____runPostInstallANECompilation_block_invoke
+ ___block_descriptor_40_e8_32s_e15_v16?0"NSSet"8ls32l8
+ ___block_descriptor_48_e8_32s40s_e21_v20?0"NSLocale"8C16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e15_B16?0"NSURL"8ls32l8s40l8r48l8
+ ___block_descriptor_64_e8_32s40s48bs56bs_e5_v8?0ls32l8s48l8s56l8s40l8
+ ___block_descriptor_80_e8_32s40s48s56r64r72r_e32_v24?0"CCSet"8"<BMBookmark>"16ls32l8r56l8s40l8s48l8r64l8r72l8
+ ___block_literal_global.1909
+ ___block_literal_global.2074
+ ___block_literal_global.2186
+ ___block_literal_global.2861
+ ___block_literal_global.327
+ ___block_literal_global.3297
+ ___block_literal_global.336
+ ___block_literal_global.338
+ ___block_literal_global.346
+ ___block_literal_global.348
+ ___block_literal_global.350
+ ___block_literal_global.352
+ ___block_literal_global.356
+ ___block_literal_global.359
+ ___block_literal_global.361
+ ___block_literal_global.363
+ ___block_literal_global.365
+ ___block_literal_global.3660
+ ___block_literal_global.367
+ ___block_literal_global.373
+ ___block_literal_global.402.4378
+ ___block_literal_global.4149
+ ___block_literal_global.4427
+ ___block_literal_global.53
+ ___block_literal_global.672
+ ___block_literal_global.685
+ __createGenericDailyMaintenanceRequest
+ __createGenericPostInstallUtilityRequest
+ __supportedDarwinNotifications.onceToken
+ __supportedDarwinNotifications.supportedNotifications
+ _kAFPreferencesDidChangeDarwinNotification
+ _objc_msgSend$_adminServiceProvider
+ _objc_msgSend$_adminServiceShouldAcceptNewConnection:
+ _objc_msgSend$_defaultTaskCoalescerWithQueue:
+ _objc_msgSend$_initWithQueue:adminServiceProvider:speechProfileSiteManager:
+ _objc_msgSend$_listenerWithMachServiceName:delegate:
+ _objc_msgSend$_notifyChangeToSets:
+ _objc_msgSend$_registerAndSubmitAllBGSystemTasks
+ _objc_msgSend$_snapshotBookmarksForLocale:toPath:
+ _objc_msgSend$_snapshotSiteAtURL:locale:changeRegistry:
+ _objc_msgSend$_speechProfileSiteManager
+ _objc_msgSend$_supportedDarwinNotifications
+ _objc_msgSend$addBookmarksForLocale:toChangeRegistry:
+ _objc_msgSend$addObserver:
+ _objc_msgSend$deleteInactiveSites
+ _objc_msgSend$deleteLegacyProfiles
+ _objc_msgSend$handlePostInstallSubscriptions
+ _objc_msgSend$handleSiteAvailableForPersona:
+ _objc_msgSend$handleSiteUnavailableForPersona:
+ _objc_msgSend$handleSiteUnavailableSoonForPersona:
+ _objc_msgSend$handleSysdiagnoseStarted
+ _objc_msgSend$handleUpdatedSets:
+ _objc_msgSend$initWithIdentifier:batchHandlerBlock:queue:useCase:
+ _objc_msgSend$initWithMachServiceName:
+ _objc_msgSend$initWithManagerName:coalescenceInterval:coalescenceDelay:executionQueue:
+ _objc_msgSend$initWithQueue:speechProfileSiteManager:
+ _objc_msgSend$isASRSpeechProfileSamplingEnabled
+ _objc_msgSend$isCurrentPersonaDefault
+ _objc_msgSend$lastPathComponent
+ _objc_msgSend$processIdentifier
+ _objc_msgSend$runMaintenanceWithShouldDefer:completion:
+ _objc_msgSend$runMigration:
+ _objc_msgSend$setDelegate:
+ _objc_msgSend$setRequiresNetworkConnectivity:
+ _objc_msgSend$setRequiresProtectionClass:
+ _objc_msgSend$setTrySchedulingBefore:
+ _objc_msgSend$sharedDispatcher
+ _objc_msgSend$sharedMonitor
+ _objc_msgSend$snapshotBookmarksForLocale:toPath:
+ _objc_msgSend$stringByDeletingLastPathComponent
+ _objc_msgSend$submitTaskWithId:taskBlock:completion:
+ _objc_msgSend$valueForEntitlement:
+ _sharedDispatcher.onceToken
+ _sharedDispatcher.sharedDispatcher
+ _sharedManager.onceToken.2860
+ _sharedManager.onceToken.671
+ _sharedManager.sharedMyManager.2862
+ _sharedManager.sharedMyManager.673
- +[CoreEmbeddedSpeechRecognizer handlePostUpgradeSubscriptions]
- GCC_except_table1117
- GCC_except_table1207
- GCC_except_table1213
- GCC_except_table1218
- GCC_except_table1222
- GCC_except_table1266
- GCC_except_table1274
- GCC_except_table1279
- GCC_except_table1283
- GCC_except_table136
- GCC_except_table157
- GCC_except_table170
- GCC_except_table242
- GCC_except_table258
- GCC_except_table261
- GCC_except_table307
- GCC_except_table328
- GCC_except_table478
- GCC_except_table483
- GCC_except_table486
- GCC_except_table490
- GCC_except_table493
- GCC_except_table502
- GCC_except_table505
- GCC_except_table508
- GCC_except_table629
- GCC_except_table660
- GCC_except_table855
- GCC_except_table860
- GCC_except_table967
- GCC_except_table968
- GCC_except_table969
- GCC_except_table970
- GCC_except_table971
- GCC_except_table972
- GCC_except_table976
- GCC_except_table977
- GCC_except_table980
- _AFIsATV
- ___62+[CoreEmbeddedSpeechRecognizer handlePostUpgradeSubscriptions]_block_invoke
- ___62+[CoreEmbeddedSpeechRecognizer handlePostUpgradeSubscriptions]_block_invoke.350
- ___62-[CESRSpeechProfileSiteManager handleSiteAvailableForPersona:]_block_invoke.314
- ___83-[CESRSpeechProfileSiteWriter _updateRequiredProfileInstancesWithSets:shouldDefer:]_block_invoke.310
- ___Block_byref_object_copy_.1341
- ___Block_byref_object_copy_.2069
- ___Block_byref_object_copy_.2771
- ___Block_byref_object_copy_.4194
- ___Block_byref_object_copy_.473
- ___Block_byref_object_copy_.866
- ___Block_byref_object_copy_.977
- ___Block_byref_object_dispose_.1342
- ___Block_byref_object_dispose_.2070
- ___Block_byref_object_dispose_.2772
- ___Block_byref_object_dispose_.4195
- ___Block_byref_object_dispose_.474
- ___Block_byref_object_dispose_.867
- ___Block_byref_object_dispose_.978
- ____registerAndSubmitDailySubscriptionCleanupBGST_block_invoke
- ____registerAndSubmitDailySubscriptionCleanupBGST_block_invoke_2
- ____registerAndSubmitPostUpgradeANECompilationBGST_block_invoke
- ____registerAndSubmitPostUpgradeANECompilationBGST_block_invoke_2
- ____registerAndSubmitPostUpgradeSubscriptionsBGST_block_invoke
- ____registerAndSubmitPostUpgradeSubscriptionsBGST_block_invoke_2
- ____runPostUpgradeANECompilation_block_invoke
- ___block_literal_global.1887
- ___block_literal_global.2053
- ___block_literal_global.2165
- ___block_literal_global.2836
- ___block_literal_global.314
- ___block_literal_global.323
- ___block_literal_global.325
- ___block_literal_global.328
- ___block_literal_global.330
- ___block_literal_global.334
- ___block_literal_global.337
- ___block_literal_global.339
- ___block_literal_global.345
- ___block_literal_global.3477
- ___block_literal_global.351
- ___block_literal_global.3963
- ___block_literal_global.402.4190
- ___block_literal_global.4239
- ___block_literal_global.670
- ___block_literal_global.681
- __createDailyMaintenanceRequest
- __createPostInstallUtilityRequest
- _objc_msgSend$handlePostUpgradeSubscriptions
- _sharedManager.onceToken.2835
- _sharedManager.onceToken.669
- _sharedManager.sharedMyManager.2837
- _sharedManager.sharedMyManager.671
CStrings:
+ "%s (%@) Failed to get/create profile instance, error: %@"
+ "%s (%@) [%@] Added %u bookmarks for %u sets to registry: %@"
+ "%s (%@) [%@] Failed to add bookmark to change registry, error: %@"
+ "%s A supported notification was NOT handled: %@"
+ "%s Collecting bookmarks for locale: %@, from site: %@"
+ "%s Connecting process with pid=(%d) is not entitled for the speech profile admin service - rejecting connection."
+ "%s Error requesting post-install subscriptions: %@"
+ "%s Evaluation is enabled, ignoring notification: %@"
+ "%s Failed to commit change registry transaction: %@"
+ "%s Failed to initialize change registry, error: %@"
+ "%s Failed to resolve URL from path: %@"
+ "%s Handling notification: %@"
+ "%s Handling updated sets for persona: %@"
+ "%s Ignoring Cascade change notification because evaluation is enabled."
+ "%s Ignoring request to snapshot bookmarks because sampling is disabled."
+ "%s New connection established to process with pid=(%d)"
+ "%s On-Device ASR: BGST: Done triggering daily speech profile maintenance."
+ "%s On-Device ASR: BGST: Done triggering daily subscription cleanup."
+ "%s On-Device ASR: BGST: Done triggering post-install speech profile migration."
+ "%s On-Device ASR: BGST: Done triggering post-install subscription."
+ "%s On-Device ASR: BGST: Triggering daily speech profile maintenance."
+ "%s On-Device ASR: BGST: Triggering post-install speech profile migration."
+ "%s Performing daily speech profile maintenance."
+ "%s Performing maintenance due to notification: %@"
+ "%s Performing post-upgrade speech profile migration."
+ "%s Received Cascade change notification for sets: %@"
+ "%s Resolved userVaultSiteURL: %@, commonSiteURL: %@"
+ "%s Starting up..."
+ "%s Unrecognized listener passed to delegate: %@"
+ "+[CESRSpeechProfileDispatcher sharedDispatcher]_block_invoke"
+ "+[CoreEmbeddedSpeechRecognizer handlePostInstallSubscriptions]_block_invoke"
+ "-[CESRSpeechProfileDispatcher _adminServiceShouldAcceptNewConnection:]"
+ "-[CESRSpeechProfileDispatcher _notifyChangeToSets:]"
+ "-[CESRSpeechProfileDispatcher handleDarwinNotificationEventWithName:]"
+ "-[CESRSpeechProfileDispatcher handleDarwinNotificationEventWithName:]_block_invoke"
+ "-[CESRSpeechProfileDispatcher listener:shouldAcceptNewConnection:]"
+ "-[CESRSpeechProfileDispatcher runMaintenanceWithShouldDefer:completion:]_block_invoke"
+ "-[CESRSpeechProfileDispatcher runMigration:]_block_invoke"
+ "-[CESRSpeechProfileDispatcher setupXPCListeners]_block_invoke"
+ "-[CESRSpeechProfileDispatcher snapshotBookmarksForLocale:toPath:]"
+ "-[CESRSpeechProfileSiteManager _handleUpdatedSets:]"
+ "-[CESRSpeechProfileSiteManager _snapshotBookmarksForLocale:toPath:]"
+ "-[CESRSpeechProfileSiteManager _snapshotSiteAtURL:locale:changeRegistry:]"
+ "-[CESRSpeechProfileSiteWriter addBookmarksForLocale:toChangeRegistry:]_block_invoke"
+ "@\"CCSetChangeXPCListener\""
+ "@\"CESRTaskCoalescer\""
+ "@\"NSXPCListener\""
+ "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
+ "CESRSpeechProfileDispatcher"
+ "CESRSpeechProfileDispatcher Set Change Queue"
+ "CESRSpeechProfileResourceMonitorDelegate"
+ "NSXPCListenerDelegate"
+ "T@\"CESRTaskCoalescer\",R,N,V_taskCoalescer"
+ "T@\"NSXPCListener\",R,N,V_adminServiceListener"
+ "_Concurrency/arm64e-apple-ios.private.swiftinterface"
+ "_adminServiceListener"
+ "_adminServiceProvider"
+ "_adminServiceShouldAcceptNewConnection:"
+ "_defaultTaskCoalescerWithQueue:"
+ "_initWithQueue:adminServiceProvider:speechProfileSiteManager:"
+ "_listenerWithMachServiceName:delegate:"
+ "_notifyChangeToSets:"
+ "_registerAndSubmitAllBGSystemTasks"
+ "_runDailySpeechProfileMaintenance"
+ "_runPostInstallANECompilation"
+ "_runPostInstallAssetSubscription"
+ "_runPostInstallSpeechProfileMigration"
+ "_setChangeListener"
+ "_snapshotBookmarksForLocale:toPath:"
+ "_snapshotSiteAtURL:locale:changeRegistry:"
+ "_supportedDarwinNotifications"
+ "_supportedNotifications"
+ "_taskCoalescer"
+ "_wait"
+ "addBookmarksForLocale:toChangeRegistry:"
+ "adminServiceListener"
+ "com.apple.MobileAsset.AutoAssetNotification^com.apple.MobileAsset.MAAutoAsset^STARTUP_ACTIVATED"
+ "com.apple.corespeech.corespeechd.speechprofileadmin"
+ "com.apple.corespeechd"
+ "com.apple.corespeechd.speechprofileassetstartup"
+ "com.apple.corespeechd.speechprofileassetupdate"
+ "com.apple.corespeechd.speechprofilefirstunlock"
+ "com.apple.corespeechd.speechprofilemaintenance"
+ "com.apple.corespeechd.speechprofilemigration"
+ "com.apple.corespeechd.speechprofilesetchange"
+ "com.apple.corespeechd.speechprofilesettingschange"
+ "com.apple.corespeechd.speechprofilesysdiagnosestarted"
+ "com.apple.mobile.keybagd.first_unlock"
+ "com.apple.siri.bg_system_task.daily-asset-subscription-cleanup"
+ "com.apple.siri.bg_system_task.daily-speech-profile-maintenance"
+ "com.apple.siri.bg_system_task.post-install-asset-subscription"
+ "com.apple.siri.bg_system_task.post-install-speech-ane-compilation"
+ "com.apple.siri.bg_system_task.post-install-speech-profile-migration"
+ "com.apple.siri.uaf.com.apple.siri.understanding"
+ "com.apple.sysdiagnose.sysdiagnoseStarted"
+ "handleDarwinNotificationEventWithName:"
+ "handlePostInstallSubscriptions"
+ "initWithIdentifier:batchHandlerBlock:queue:useCase:"
+ "initWithMachServiceName:"
+ "isASRSpeechProfileSamplingEnabled"
+ "isCurrentPersonaDefault"
+ "lastPathComponent"
+ "listener:shouldAcceptNewConnection:"
+ "processIdentifier"
+ "resourceAvailableForPersona:"
+ "resourceUnavailableForPersona:"
+ "resourceUnavailableSoonForPersona:"
+ "runMaintenanceWithShouldDefer:completion:"
+ "runMigration:"
+ "setRequiresNetworkConnectivity:"
+ "setRequiresProtectionClass:"
+ "setTrySchedulingBefore:"
+ "setupXPCListeners"
+ "sharedDispatcher"
+ "snapshotBookmarksForLocale:toPath:"
+ "stringByDeletingLastPathComponent"
+ "taskCoalescer"
+ "v16@?0@\"NSSet\"8"
+ "v32@0:8@?16@?24"
+ "valueForEntitlement:"
- "%s Error requesting post-upgrade subscriptions: %@"
- "%s Failed to get/create profile instance, error: %@"
- "%s On-Device ASR: BGST: Done triggering daily subscription cleanup"
- "%s On-Device ASR: BGST: Done triggering post-upgrade subscriptions"
- "+[CoreEmbeddedSpeechRecognizer handlePostUpgradeSubscriptions]_block_invoke"
- "_runPostUpgradeANECompilation"
- "_runPostUpgradeSubscriptions"
- "com.apple.siri.bg_system_task.daily-subscription-cleanup"
- "com.apple.siri.bg_system_task.post-upgrade-speech-ane-compilation"
- "com.apple.siri.bg_system_task.post-upgrade-subscriptions"
- "handlePostUpgradeSubscriptions"

```
