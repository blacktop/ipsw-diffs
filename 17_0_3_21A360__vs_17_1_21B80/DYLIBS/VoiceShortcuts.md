## VoiceShortcuts

> `/System/Library/PrivateFrameworks/VoiceShortcuts.framework/VoiceShortcuts`

```diff

-2038.0.1.10.0
-  __TEXT.__text: 0xd8900
-  __TEXT.__auth_stubs: 0x2590
-  __TEXT.__objc_methlist: 0x4bdc
+2106.100.3.1.0
+  __TEXT.__text: 0xd9434
+  __TEXT.__auth_stubs: 0x2570
+  __TEXT.__objc_methlist: 0x4ccc
   __TEXT.__const: 0x28f8
-  __TEXT.__cstring: 0xfac1
-  __TEXT.__swift5_typeref: 0x1a4b
-  __TEXT.__swift5_fieldmd: 0xdb4
+  __TEXT.__cstring: 0xfc02
+  __TEXT.__swift5_typeref: 0x1a23
+  __TEXT.__swift5_fieldmd: 0xdcc
   __TEXT.__constg_swiftt: 0x1460
   __TEXT.__swift5_builtin: 0x118
-  __TEXT.__swift5_reflstr: 0xcf6
+  __TEXT.__swift5_reflstr: 0xd16
   __TEXT.__swift5_assocty: 0x378
   __TEXT.__swift5_protos: 0x3c
   __TEXT.__swift5_proto: 0x23c
   __TEXT.__swift5_types: 0x104
   __TEXT.__swift5_capture: 0x554
   __TEXT.__swift5_mpenum: 0x60
-  __TEXT.__gcc_except_tab: 0xe7c
-  __TEXT.__oslogstring: 0xd394
+  __TEXT.__gcc_except_tab: 0xe94
+  __TEXT.__oslogstring: 0xd3b5
   __TEXT.__dlopen_cstrs: 0x30f
   __TEXT.__ustring: 0x44
-  __TEXT.__unwind_info: 0x3a44
-  __TEXT.__eh_frame: 0x5450
-  __TEXT.__objc_classname: 0xce1
-  __TEXT.__objc_methname: 0x14a10
-  __TEXT.__objc_methtype: 0x4571
-  __TEXT.__objc_stubs: 0xf3e0
-  __DATA_CONST.__got: 0x748
-  __DATA_CONST.__const: 0x2898
+  __TEXT.__unwind_info: 0x39d8
+  __TEXT.__eh_frame: 0x5398
+  __TEXT.__objc_classname: 0xd05
+  __TEXT.__objc_methname: 0x14dae
+  __TEXT.__objc_methtype: 0x4625
+  __TEXT.__objc_stubs: 0xf4e0
+  __DATA_CONST.__got: 0x730
+  __DATA_CONST.__const: 0x2878
   __DATA_CONST.__objc_classlist: 0x288
   __DATA_CONST.__objc_catlist: 0x158
-  __DATA_CONST.__objc_protolist: 0x240
+  __DATA_CONST.__objc_protolist: 0x248
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x9b38
-  __DATA_CONST.__objc_selrefs: 0x4718
+  __DATA_CONST.__objc_const: 0x9ce0
+  __DATA_CONST.__objc_selrefs: 0x47b0
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__const: 0x3630
+  __AUTH_CONST.__const: 0x3650
   __AUTH_CONST.__auth_ptr: 0x98
   __AUTH_CONST.__objc_const: 0x25c0
   __AUTH_CONST.__cfstring: 0x4100
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x12d8
+  __AUTH_CONST.__auth_got: 0x12c8
   __AUTH.__objc_data: 0xdb8
   __AUTH.__data: 0x888
   __DATA.__objc_protorefs: 0x88
   __DATA.__objc_classrefs: 0xd08
   __DATA.__objc_superrefs: 0x1c8
-  __DATA.__objc_ivar: 0x454
+  __DATA.__objc_ivar: 0x45c
   __DATA.__objc_data: 0x90
-  __DATA.__data: 0x2f70
+  __DATA.__data: 0x2ff0
   __DATA.__bss: 0x33a0
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0xf68

   - /System/Library/Frameworks/ContactsUI.framework/ContactsUI
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
-  - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4316
-  Symbols:   9140
-  CStrings:  5702
+  Functions: 4336
+  Symbols:   9210
+  CStrings:  5733
 
Symbols:
+ -[VCVoiceShortcutManager badgeTypeForEntityIdentifier:error:]
+ -[VCVoiceShortcutManager storeSerializedParameters:forAppEntityIdentifier:queryName:badgeType:completion:]
+ -[VCVoiceShortcutManagerAccessWrapper saveOutputActionSmartPromtDataForWorkflowReference:completion:]
+ -[VCVoiceShortcutManagerAccessWrapper storeSerializedParameters:forAppEntityIdentifier:queryName:badgeType:completion:]
+ -[WFBiomeListener isTransactionEventDuplicate:forTrigger:withSeenTransactionIdentifiers:]
+ -[WFBiomeListener seenTransactionIdentifiers]
+ -[WFBiomeListener setSeenTransactionIdentifiers:]
+ -[WFContextualActionSpotlightSyncService systemLanguageUpdated]
+ -[WFTriggerBootManager bootUUIDFileURL]
+ -[WFTriggerBootManager createOrUpdateBootTimeFileIfNeeded]
+ -[WFTriggerBootManager enabledTriggers:]
+ -[WFTriggerBootManager lastKnownBootUUIDDiffersFromCurrentBootUUID]
+ -[WFTriggerBootManager lastKnownBootUUID]
+ -[WFTriggerBootManager queue_postNotification]
+ -[WFTriggerEventQueue initWithDatabaseProvider:notificationManager:notificationScheduler:]
+ -[WFWalletTransactionProvider fetchRemoteTransactionWithIdentifier:passUniqueID:completion:]
+ -[WFWalletTransactionProvider observeForUpdatesWithInitialTransactionIfNeeded:transactionIdentifier:completion:]
+ -[WFWalletTransactionProvider paymentPassWithUniqueIdentifier:didEnableMessageService:]
+ -[WFWalletTransactionProvider paymentPassWithUniqueIdentifier:didEnableTransactionService:]
+ -[WFWalletTransactionProvider paymentPassWithUniqueIdentifier:didUpdateBalanceReminder:forBalance:]
+ -[WFWalletTransactionProvider paymentPassWithUniqueIdentifier:didUpdateWithBalances:]
+ -[WFWalletTransactionProvider paymentPassWithUniqueIdentifier:didUpdateWithCredentials:]
+ -[WFWalletTransactionProvider paymentPassWithUniqueIdentifier:didUpdateWithTransitPassProperties:]
+ -[WFWalletTransactionProvider queue_finishWithPaymentTransaction:]
+ -[WFWalletTransactionProvider remotePaymentServiceConnection]
+ -[WFWalletTransactionProvider setRemotePaymentServiceConnection:]
+ -[WFWalletTransactionProvider transactionIsValid:]
+ -[WFWalletTransactionProvider transactionSourceIdentifier:didRemoveTransactionWithIdentifier:]
+ -[WFWalletTransactionTrigger(BiomeContext) transactionIdentifierWithEvent:]
+ GCC_except_table1126
+ GCC_except_table1161
+ GCC_except_table1167
+ GCC_except_table1198
+ GCC_except_table1318
+ GCC_except_table1330
+ GCC_except_table135
+ GCC_except_table1407
+ GCC_except_table1413
+ GCC_except_table1415
+ GCC_except_table1418
+ GCC_except_table1419
+ GCC_except_table1424
+ GCC_except_table1433
+ GCC_except_table1570
+ GCC_except_table1581
+ GCC_except_table1583
+ GCC_except_table1621
+ GCC_except_table1623
+ GCC_except_table1630
+ GCC_except_table1632
+ GCC_except_table1634
+ GCC_except_table1635
+ GCC_except_table1637
+ GCC_except_table1639
+ GCC_except_table1640
+ GCC_except_table1653
+ GCC_except_table1691
+ GCC_except_table1698
+ GCC_except_table1709
+ GCC_except_table1716
+ GCC_except_table1754
+ GCC_except_table1758
+ GCC_except_table1776
+ GCC_except_table1794
+ GCC_except_table1806
+ GCC_except_table1809
+ GCC_except_table1822
+ GCC_except_table1898
+ GCC_except_table1903
+ GCC_except_table192
+ GCC_except_table1940
+ GCC_except_table1941
+ GCC_except_table1952
+ GCC_except_table1954
+ GCC_except_table197
+ GCC_except_table1987
+ GCC_except_table199
+ GCC_except_table202
+ GCC_except_table285
+ GCC_except_table369
+ GCC_except_table383
+ GCC_except_table398
+ GCC_except_table422
+ GCC_except_table444
+ GCC_except_table463
+ GCC_except_table479
+ GCC_except_table506
+ GCC_except_table520
+ GCC_except_table544
+ GCC_except_table551
+ GCC_except_table560
+ GCC_except_table564
+ GCC_except_table566
+ GCC_except_table616
+ GCC_except_table709
+ GCC_except_table710
+ GCC_except_table725
+ GCC_except_table736
+ GCC_except_table92
+ GCC_except_table98
+ GCC_except_table992
+ _OBJC_CLASS_$_LNEntity
+ _OBJC_IVAR_$_WFBiomeListener._seenTransactionIdentifiers
+ _OBJC_IVAR_$_WFWalletTransactionProvider._remotePaymentServiceConnection
+ _VCXPCEventLanguagePreferencesChanged
+ _WFGetBootSessionUUID
+ _WFSpotlightResultRunnableTopHitBadge
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NPKCompanionAgentConnectionDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NPKCompanionAgentConnectionDelegate
+ __OBJC_$_PROTOCOL_REFS_NPKCompanionAgentConnectionDelegate
+ __OBJC_LABEL_PROTOCOL_$_NPKCompanionAgentConnectionDelegate
+ __OBJC_PROTOCOL_$_NPKCompanionAgentConnectionDelegate
+ ___105-[WFContextualActionSpotlightSyncService reindexSearchableItems:appShortcutBundleIdentifiers:completion:]_block_invoke.195
+ ___105-[WFContextualActionSpotlightSyncService reindexSearchableItems:appShortcutBundleIdentifiers:completion:]_block_invoke_2.197
+ ___105-[WFContextualActionSpotlightSyncService reindexSearchableItems:appShortcutBundleIdentifiers:completion:]_block_invoke_2.230
+ ___112-[WFWalletTransactionProvider observeForUpdatesWithInitialTransactionIfNeeded:transactionIdentifier:completion:]_block_invoke
+ ___112-[WFWalletTransactionProvider observeForUpdatesWithInitialTransactionIfNeeded:transactionIdentifier:completion:]_block_invoke.195
+ ___118-[WFContextualActionSpotlightSyncService queue_getAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.249
+ ___118-[WFContextualActionSpotlightSyncService queue_getAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.254
+ ___118-[WFContextualActionSpotlightSyncService queue_getAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.255
+ ___118-[WFContextualActionSpotlightSyncService queue_getAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.259
+ ___118-[WFContextualActionSpotlightSyncService queue_getAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.264
+ ___118-[WFContextualActionSpotlightSyncService queue_getAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.265
+ ___118-[WFContextualActionSpotlightSyncService queue_getAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.266
+ ___118-[WFContextualActionSpotlightSyncService queue_getAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke_2.260
+ ___136-[WFContextualActionSpotlightSyncService queue_fetchWipeAndIndexActionsInDomainWithDescriptiveName:identifiers:fetcher:completionBlock:]_block_invoke.232
+ ___136-[WFContextualActionSpotlightSyncService queue_fetchWipeAndIndexActionsInDomainWithDescriptiveName:identifiers:fetcher:completionBlock:]_block_invoke.233
+ ___136-[WFContextualActionSpotlightSyncService queue_fetchWipeAndIndexActionsInDomainWithDescriptiveName:identifiers:fetcher:completionBlock:]_block_invoke.234
+ ___136-[WFContextualActionSpotlightSyncService queue_fetchWipeAndIndexActionsInDomainWithDescriptiveName:identifiers:fetcher:completionBlock:]_block_invoke_2.235
+ ___40-[WFTriggerBootManager enabledTriggers:]_block_invoke
+ ___46-[WFTriggerBootManager queue_postNotification]_block_invoke
+ ___52-[WFTriggerBootManager configuredTriggersDidChange:]_block_invoke
+ ___56-[WFTriggerBootManager deviceWasUnlockedForTheFirstTime]_block_invoke
+ ___58-[WFContextualActionSpotlightSyncService subscribeToBiome]_block_invoke.275
+ ___58-[WFContextualActionSpotlightSyncService subscribeToBiome]_block_invoke.276
+ ___58-[WFContextualActionSpotlightSyncService subscribeToBiome]_block_invoke_2.277
+ ___63-[WFContextualActionSpotlightSyncService systemLanguageUpdated]_block_invoke
+ ___69-[WFTriggerRegistrar getConfiguredTriggerDescriptionsWithCompletion:]_block_invoke.186
+ ___92-[WFWalletTransactionProvider fetchRemoteTransactionWithIdentifier:passUniqueID:completion:]_block_invoke
+ ___92-[WFWalletTransactionProvider fetchRemoteTransactionWithIdentifier:passUniqueID:completion:]_block_invoke.189
+ ___92-[WFWalletTransactionProvider fetchRemoteTransactionWithIdentifier:passUniqueID:completion:]_block_invoke_2
+ ___92-[WFWalletTransactionProvider fetchRemoteTransactionWithIdentifier:passUniqueID:completion:]_block_invoke_2.190
+ ___92-[WFWalletTransactionProvider fetchRemoteTransactionWithIdentifier:passUniqueID:completion:]_block_invoke_3
+ ___Block_byref_object_copy_.1133
+ ___Block_byref_object_copy_.3367
+ ___Block_byref_object_copy_.3585
+ ___Block_byref_object_copy_.3809
+ ___Block_byref_object_copy_.4580
+ ___Block_byref_object_copy_.4803
+ ___Block_byref_object_copy_.5817
+ ___Block_byref_object_copy_.6056
+ ___Block_byref_object_copy_.6172
+ ___Block_byref_object_copy_.6312
+ ___Block_byref_object_copy_.6404
+ ___Block_byref_object_copy_.744
+ ___Block_byref_object_dispose_.1134
+ ___Block_byref_object_dispose_.3368
+ ___Block_byref_object_dispose_.3586
+ ___Block_byref_object_dispose_.3810
+ ___Block_byref_object_dispose_.4581
+ ___Block_byref_object_dispose_.4804
+ ___Block_byref_object_dispose_.5818
+ ___Block_byref_object_dispose_.6057
+ ___Block_byref_object_dispose_.6173
+ ___Block_byref_object_dispose_.6313
+ ___Block_byref_object_dispose_.6405
+ ___Block_byref_object_dispose_.745
+ ___block_descriptor_56_e8_32s40bs48w_e15_v16?0"NSSet"8lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48w_e30_v16?0"PKPaymentTransaction"8lw48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e23_v16?0"PKPaymentPass"8ls32l8s40l8s56l8s48l8
+ ___block_literal_global.1147
+ ___block_literal_global.1343
+ ___block_literal_global.1645
+ ___block_literal_global.165
+ ___block_literal_global.172.7386
+ ___block_literal_global.1763
+ ___block_literal_global.179
+ ___block_literal_global.183.3474
+ ___block_literal_global.2376
+ ___block_literal_global.245
+ ___block_literal_global.252.2309
+ ___block_literal_global.256
+ ___block_literal_global.272
+ ___block_literal_global.2837
+ ___block_literal_global.287
+ ___block_literal_global.2975
+ ___block_literal_global.324
+ ___block_literal_global.3469
+ ___block_literal_global.360
+ ___block_literal_global.3603
+ ___block_literal_global.3855
+ ___block_literal_global.4066
+ ___block_literal_global.4192
+ ___block_literal_global.4866
+ ___block_literal_global.5099
+ ___block_literal_global.545
+ ___block_literal_global.5604
+ ___block_literal_global.575
+ ___block_literal_global.5830
+ ___block_literal_global.6055
+ ___block_literal_global.6196
+ ___block_literal_global.6397
+ ___block_literal_global.648
+ ___block_literal_global.6641
+ ___block_literal_global.6879
+ ___block_literal_global.6999
+ ___block_literal_global.7402
+ ___block_literal_global.746
+ ___block_literal_global.7473
+ ___block_literal_global.989
+ ___swift_memcpy32_8
+ __objc_autoreleasePoolPop
+ __objc_autoreleasePoolPush
+ _block_descriptor.1
+ _objc_msgSend$badge
+ _objc_msgSend$badgeTypeForEntityIdentifier:error:
+ _objc_msgSend$bootUUIDFileURL
+ _objc_msgSend$contextualActionIcon
+ _objc_msgSend$createOrUpdateBootTimeFileIfNeeded
+ _objc_msgSend$enabledTriggers:
+ _objc_msgSend$fetchRemoteTransactionWithIdentifier:passUniqueID:completion:
+ _objc_msgSend$indexSearchableItems:completionBlock:
+ _objc_msgSend$initWithDatabaseProvider:notificationManager:notificationScheduler:
+ _objc_msgSend$initWithName:subtitle:icon:badge:
+ _objc_msgSend$instanceIdentifier
+ _objc_msgSend$isTransactionEventDuplicate:forTrigger:withSeenTransactionIdentifiers:
+ _objc_msgSend$lastKnownBootUUID
+ _objc_msgSend$lastKnownBootUUIDDiffersFromCurrentBootUUID
+ _objc_msgSend$observeForUpdatesWithInitialTransactionIfNeeded:transactionIdentifier:completion:
+ _objc_msgSend$queue_finishWithPaymentTransaction:
+ _objc_msgSend$queue_postNotification
+ _objc_msgSend$remotePaymentServiceConnection
+ _objc_msgSend$saveOutputActionSmartPromtDataForWorkflowReference:error:
+ _objc_msgSend$seenTransactionIdentifiers
+ _objc_msgSend$setAppShortcutDisplayRepresentationForPhraseSignature:bundleIdentifier:
+ _objc_msgSend$storeSerializedParameters:forAppEntityIdentifier:queryName:badgeType:completion:
+ _objc_msgSend$storeSerializedParameters:forIdentifier:queryName:badgeType:error:
+ _objc_msgSend$stringWithContentsOfURL:encoding:error:
+ _objc_msgSend$transactionIdentifierWithEvent:
+ _objc_msgSend$transactionIsValid:
+ _objc_msgSend$writeToURL:atomically:encoding:error:
+ _swift_dynamicCastObjCProtocolConditional
- +[WFTriggerBootManager automationsEnabledFileURL]
- +[WFTriggerBootManager createMarkerFileIfNeeded]
- +[WFTriggerBootManager deleteMarkerFile]
- +[WFTriggerBootManager markerFileExists]
- -[VCVoiceShortcutManager storeSerializedParameters:forAppEntityIdentifier:queryName:completion:]
- -[VCVoiceShortcutManagerAccessWrapper storeSerializedParameters:forAppEntityIdentifier:queryName:completion:]
- -[WFTriggerBootManager shouldCreateMarkerFileWithConfiguredTriggers:]
- -[WFWalletTransactionProvider queue_finishWithTransaction:]
- -[WFWalletTransactionTrigger(ContentInput) getRemoteTransactionForUniquePassID:transactionIdentifier:completion:]
- GCC_except_table1100
- GCC_except_table1135
- GCC_except_table1141
- GCC_except_table1172
- GCC_except_table1292
- GCC_except_table1304
- GCC_except_table134
- GCC_except_table1380
- GCC_except_table1386
- GCC_except_table1388
- GCC_except_table1391
- GCC_except_table1392
- GCC_except_table1397
- GCC_except_table1406
- GCC_except_table1541
- GCC_except_table1552
- GCC_except_table1554
- GCC_except_table1565
- GCC_except_table1592
- GCC_except_table1595
- GCC_except_table1601
- GCC_except_table1603
- GCC_except_table1605
- GCC_except_table1606
- GCC_except_table1608
- GCC_except_table1610
- GCC_except_table1611
- GCC_except_table1662
- GCC_except_table1669
- GCC_except_table1680
- GCC_except_table1687
- GCC_except_table1725
- GCC_except_table1729
- GCC_except_table1747
- GCC_except_table1751
- GCC_except_table1765
- GCC_except_table1777
- GCC_except_table178
- GCC_except_table1793
- GCC_except_table182
- GCC_except_table1866
- GCC_except_table1871
- GCC_except_table1908
- GCC_except_table1909
- GCC_except_table1920
- GCC_except_table1922
- GCC_except_table1955
- GCC_except_table1972
- GCC_except_table265
- GCC_except_table349
- GCC_except_table362
- GCC_except_table377
- GCC_except_table401
- GCC_except_table423
- GCC_except_table442
- GCC_except_table458
- GCC_except_table485
- GCC_except_table499
- GCC_except_table523
- GCC_except_table530
- GCC_except_table539
- GCC_except_table543
- GCC_except_table545
- GCC_except_table595
- GCC_except_table688
- GCC_except_table689
- GCC_except_table704
- GCC_except_table715
- GCC_except_table91
- GCC_except_table96
- GCC_except_table967
- _CGDataProviderCopyData
- _CGImageGetDataProvider
- _NSFileProtectionKey
- _NSFileProtectionNone
- _OBJC_CLASS_$_LNImage
- _WFContextualActionIconDisplayStyleForLNImageDisplayStyle
- ___105-[WFContextualActionSpotlightSyncService reindexSearchableItems:appShortcutBundleIdentifiers:completion:]_block_invoke.192
- ___105-[WFContextualActionSpotlightSyncService reindexSearchableItems:appShortcutBundleIdentifiers:completion:]_block_invoke_2.194
- ___105-[WFContextualActionSpotlightSyncService reindexSearchableItems:appShortcutBundleIdentifiers:completion:]_block_invoke_2.227
- ___113-[WFWalletTransactionTrigger(ContentInput) getRemoteTransactionForUniquePassID:transactionIdentifier:completion:]_block_invoke
- ___113-[WFWalletTransactionTrigger(ContentInput) getRemoteTransactionForUniquePassID:transactionIdentifier:completion:]_block_invoke.240
- ___113-[WFWalletTransactionTrigger(ContentInput) getRemoteTransactionForUniquePassID:transactionIdentifier:completion:]_block_invoke.241
- ___118-[WFContextualActionSpotlightSyncService queue_getAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.246
- ___118-[WFContextualActionSpotlightSyncService queue_getAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.247
- ___118-[WFContextualActionSpotlightSyncService queue_getAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.248
- ___118-[WFContextualActionSpotlightSyncService queue_getAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.252
- ___118-[WFContextualActionSpotlightSyncService queue_getAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.261
- ___118-[WFContextualActionSpotlightSyncService queue_getAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.262
- ___118-[WFContextualActionSpotlightSyncService queue_getAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke.263
- ___118-[WFContextualActionSpotlightSyncService queue_getAppShortcutContextualActionsForBundleIdentifiers:completionHandler:]_block_invoke_2.257
- ___136-[WFContextualActionSpotlightSyncService queue_fetchWipeAndIndexActionsInDomainWithDescriptiveName:identifiers:fetcher:completionBlock:]_block_invoke.229
- ___136-[WFContextualActionSpotlightSyncService queue_fetchWipeAndIndexActionsInDomainWithDescriptiveName:identifiers:fetcher:completionBlock:]_block_invoke.230
- ___136-[WFContextualActionSpotlightSyncService queue_fetchWipeAndIndexActionsInDomainWithDescriptiveName:identifiers:fetcher:completionBlock:]_block_invoke.231
- ___136-[WFContextualActionSpotlightSyncService queue_fetchWipeAndIndexActionsInDomainWithDescriptiveName:identifiers:fetcher:completionBlock:]_block_invoke_2.232
- ___58-[WFContextualActionSpotlightSyncService subscribeToBiome]_block_invoke.270
- ___58-[WFContextualActionSpotlightSyncService subscribeToBiome]_block_invoke.272
- ___58-[WFContextualActionSpotlightSyncService subscribeToBiome]_block_invoke_2.274
- ___69-[WFTriggerBootManager shouldCreateMarkerFileWithConfiguredTriggers:]_block_invoke
- ___69-[WFTriggerRegistrar getConfiguredTriggerDescriptionsWithCompletion:]_block_invoke.187
- ___78-[WFWalletTransactionProvider fetchLocalTransactionWithIdentifier:completion:]_block_invoke.188
- ___78-[WFWalletTransactionProvider fetchLocalTransactionWithIdentifier:completion:]_block_invoke_3
- ___Block_byref_object_copy_.1139
- ___Block_byref_object_copy_.3444
- ___Block_byref_object_copy_.3663
- ___Block_byref_object_copy_.3888
- ___Block_byref_object_copy_.4662
- ___Block_byref_object_copy_.4876
- ___Block_byref_object_copy_.5876
- ___Block_byref_object_copy_.6113
- ___Block_byref_object_copy_.6229
- ___Block_byref_object_copy_.6369
- ___Block_byref_object_copy_.6461
- ___Block_byref_object_copy_.740
- ___Block_byref_object_dispose_.1140
- ___Block_byref_object_dispose_.3445
- ___Block_byref_object_dispose_.3664
- ___Block_byref_object_dispose_.3889
- ___Block_byref_object_dispose_.4663
- ___Block_byref_object_dispose_.4877
- ___Block_byref_object_dispose_.5877
- ___Block_byref_object_dispose_.6114
- ___Block_byref_object_dispose_.6230
- ___Block_byref_object_dispose_.6370
- ___Block_byref_object_dispose_.6462
- ___Block_byref_object_dispose_.741
- ___block_descriptor_48_e8_32s40bs_e15_v16?0"NSSet"8ls32l8s40l8
- ___block_descriptor_56_e8_32s40bs48w_e30_v16?0"PKPaymentTransaction"8lw48l8s40l8s32l8
- ___block_descriptor_56_e8_32s40s48bs_e30_v16?0"PKPaymentTransaction"8ls32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e23_v16?0"PKPaymentPass"8ls32l8s64l8s40l8s48l8s56l8
- ___block_literal_global.1012
- ___block_literal_global.1153
- ___block_literal_global.1348
- ___block_literal_global.164
- ___block_literal_global.1651
- ___block_literal_global.172.7434
- ___block_literal_global.180
- ___block_literal_global.183.3551
- ___block_literal_global.1836
- ___block_literal_global.239
- ___block_literal_global.2445
- ___block_literal_global.251
- ___block_literal_global.255
- ___block_literal_global.269
- ___block_literal_global.2921
- ___block_literal_global.3058
- ___block_literal_global.322
- ___block_literal_global.346
- ___block_literal_global.3546
- ___block_literal_global.362.1781
- ___block_literal_global.3681
- ___block_literal_global.3934
- ___block_literal_global.4144
- ___block_literal_global.4272
- ___block_literal_global.4941
- ___block_literal_global.5174
- ___block_literal_global.540
- ___block_literal_global.5666
- ___block_literal_global.5889
- ___block_literal_global.6112
- ___block_literal_global.6253
- ___block_literal_global.644
- ___block_literal_global.6454
- ___block_literal_global.6687
- ___block_literal_global.6927
- ___block_literal_global.7047
- ___block_literal_global.742
- ___block_literal_global.7450
- ___block_literal_global.7544
- _objc_msgSend$CGImage
- _objc_msgSend$automationsEnabledFileURL
- _objc_msgSend$batchedIndexSearchableItems:withBatchSize:completionBlock:
- _objc_msgSend$createFileAtPath:contents:attributes:
- _objc_msgSend$createMarkerFileIfNeeded
- _objc_msgSend$deleteMarkerFile
- _objc_msgSend$getRemoteTransactionForUniquePassID:transactionIdentifier:completion:
- _objc_msgSend$iconWithImageData:scale:displayStyle:
- _objc_msgSend$iconWithImageURL:displayStyle:
- _objc_msgSend$initWithName:subtitle:icon:
- _objc_msgSend$initWithSystemImageNamed:
- _objc_msgSend$markerFileExists
- _objc_msgSend$queue_finishWithTransaction:
- _objc_msgSend$recentlyRunShortcutsWithLimit:
- _objc_msgSend$setAppShortcutDisplayRepresentationForPhraseSignature:
- _objc_msgSend$shouldCreateMarkerFileWithConfiguredTriggers:
- _objc_msgSend$storeSerializedParameters:forAppEntityIdentifier:queryName:completion:
- _objc_msgSend$storeSerializedParameters:forIdentifier:queryName:error:
- _objc_msgSend$symbolName
- _symbolic SaySo29WFCSSearchableItemConvertible_pG
CStrings:
+ "%s Already updated boot uuid not doing!"
+ "%s Could not get last logged boot data error: %@"
+ "%s Failed to remove file with error: %@"
+ "%s Failed to update boot time uuid file with error: %@"
+ "%s Ignoring duplicate transaction identifier %@"
+ "%s Not posting notification because we already have for this boot session (%@) (%@)"
+ "%s System language updated, triggering full reindex"
+ "%s Unable to fetch badge for app %@: %@"
+ "-[WFBiomeListener isTransactionEventDuplicate:forTrigger:withSeenTransactionIdentifiers:]"
+ "-[WFContextualActionSpotlightSyncService systemLanguageUpdated]"
+ "-[WFTriggerBootManager bootUUIDFileURL]"
+ "-[WFTriggerBootManager configuredTriggersDidChange:]"
+ "-[WFTriggerBootManager createOrUpdateBootTimeFileIfNeeded]"
+ "-[WFTriggerBootManager lastKnownBootUUIDDiffersFromCurrentBootUUID]"
+ "-[WFTriggerBootManager lastKnownBootUUID]"
+ "-[WFTriggerBootManager queue_postNotification]_block_invoke"
+ "-[WFWalletTransactionProvider fetchRemoteTransactionWithIdentifier:passUniqueID:completion:]_block_invoke_3"
+ "-[WFWalletTransactionProvider observeForUpdatesWithInitialTransactionIfNeeded:transactionIdentifier:completion:]_block_invoke"
+ "/Library/Caches/com.apple.xbs/Sources/Shortcuts/ShortcutsCore/VoiceShortcuts/Sources/Sync/Toprak/ToprakEngine.swift"
+ "@\"NPKCompanionAgentConnection\""
+ "CSSearchableItemConvertible"
+ "Done indexing %ld items"
+ "Down-casted Array element failed to match the target type\nExpected "
+ "Failed to archive App Intent"
+ "Failed to unarchive App Intent"
+ "Generated searchable item with identifier %s"
+ "NPKCompanionAgentConnectionDelegate"
+ "NSArray element failed to match the Swift Array Element type\nExpected "
+ "Starting indexing %ld items"
+ "T@\"NPKCompanionAgentConnection\",&,N,V_remotePaymentServiceConnection"
+ "T@\"NSMutableDictionary\",&,N,V_seenTransactionIdentifiers"
+ "_remotePaymentServiceConnection"
+ "_seenTransactionIdentifiers"
+ "badge"
+ "badgeTypeForEntityIdentifier:error:"
+ "bootUUIDFileURL"
+ "com.apple.language.changed"
+ "contextualActionIcon"
+ "createOrUpdateBootTimeFileIfNeeded"
+ "enabledTriggers:"
+ "fetchRemoteTransactionWithIdentifier:passUniqueID:completion:"
+ "indexSearchableItems:completionBlock:"
+ "initWithDatabaseProvider:notificationManager:notificationScheduler:"
+ "initWithName:subtitle:icon:badge:"
+ "instanceIdentifier"
+ "isTransactionEventDuplicate:forTrigger:withSeenTransactionIdentifiers:"
+ "lastKnownBootUUID"
+ "lastKnownBootUUIDDiffersFromCurrentBootUUID"
+ "observeForUpdatesWithInitialTransactionIfNeeded:transactionIdentifier:completion:"
+ "paymentPassWithUniqueIdentifier:didUpdateBalanceReminder:forBalance:"
+ "paymentPassWithUniqueIdentifier:didUpdateWithBalances:"
+ "paymentPassWithUniqueIdentifier:didUpdateWithCredentials:"
+ "queue_finishWithPaymentTransaction:"
+ "queue_postNotification"
+ "remotePaymentServiceConnection"
+ "saveOutputActionSmartPromtDataForWorkflowReference:completion:"
+ "saveOutputActionSmartPromtDataForWorkflowReference:error:"
+ "seenTransactionIdentifiers"
+ "setAppShortcutDisplayRepresentationForPhraseSignature:bundleIdentifier:"
+ "setRemotePaymentServiceConnection:"
+ "setSeenTransactionIdentifiers:"
+ "storeSerializedParameters:forAppEntityIdentifier:queryName:badgeType:completion:"
+ "storeSerializedParameters:forIdentifier:queryName:badgeType:error:"
+ "stringWithContentsOfURL:encoding:error:"
+ "systemLanguageUpdated"
+ "transactionIdentifierWithEvent:"
+ "transactionIsValid:"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"WFWorkflowReference\"16@?<v@?@\"NSError\">24"
+ "v40@0:8@\"NSString\"16@\"PKPaymentBalanceReminder\"24@\"PKPaymentBalance\"32"
+ "v56@0:8@\"NSData\"16@\"NSString\"24@\"NSString\"32Q40@?<v@?@\"NSError\">48"
+ "v56@0:8@16@24@32Q40@?48"
+ "writeToURL:atomically:encoding:error:"
- "%s Could not create automations enabled marker file!"
- "%s Creating automations enabled marker file."
- "%s Failed to remove automation enabled file with error: %@"
- "%s Found matching transaction %@"
- "%s Got transactions from watch %@"
- "%s LNDisplayRepresentation has a data backed image, this hurts our footprint (Spotlight sync)"
- "%s Received unhandled App Shortcut image: %@ for app: %@"
- "+[WFTriggerBootManager automationsEnabledFileURL]"
- "+[WFTriggerBootManager createMarkerFileIfNeeded]"
- "+[WFTriggerBootManager deleteMarkerFile]"
- "-[WFWalletTransactionProvider fetchLocalTransactionWithIdentifier:completion:]_block_invoke"
- "-[WFWalletTransactionProvider fetchLocalTransactionWithIdentifier:completion:]_block_invoke_3"
- "-[WFWalletTransactionTrigger(ContentInput) getRemoteTransactionForUniquePassID:transactionIdentifier:completion:]_block_invoke"
- "-[WFWalletTransactionTrigger(ContentInput) getRemoteTransactionForUniquePassID:transactionIdentifier:completion:]_block_invoke_2"
- "...indexing items %ld..<%ld"
- "/Library/Caches/com.apple.xbs/Sources/Shortcuts/VoiceShortcuts/VoiceShortcuts/Sources/Sync/Toprak/ToprakEngine.swift"
- "CGImage"
- "Done indexing items %ld..<%ld"
- "Failed to archive App Intnet"
- "Failed to unarchive App Intnet"
- "Starting a batched index of %ld elements -- in %ld batches"
- "WFTrigger+ContentInput.m"
- "automationsEnabledFileURL"
- "batchedIndexSearchableItems:withBatchSize:completionBlock:"
- "createFileAtPath:contents:attributes:"
- "createMarkerFileIfNeeded"
- "deleteMarkerFile"
- "getRemoteTransactionForUniquePassID:transactionIdentifier:completion:"
- "iconWithImageData:scale:displayStyle:"
- "iconWithImageURL:displayStyle:"
- "initWithName:subtitle:icon:"
- "initWithSystemImageNamed:"
- "markerFileExists"
- "queue_finishWithTransaction:"
- "recentlyRunShortcutsWithLimit:"
- "setAppShortcutDisplayRepresentationForPhraseSignature:"
- "shouldCreateMarkerFileWithConfiguredTriggers:"
- "storeSerializedParameters:forAppEntityIdentifier:queryName:completion:"
- "storeSerializedParameters:forIdentifier:queryName:error:"
- "symbolName"
- "v40@0:8@\"NSArray\"16Q24@?<v@?@\"NSError\">32"
- "v48@0:8@\"NSData\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSError\">40"

```
