## CoreDuet

> `/System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet`

```diff

-1852.4.2.0.3
-  __TEXT.__text: 0x191e14
+1852.4.7.0.3
+  __TEXT.__text: 0x190368
   __TEXT.__auth_stubs: 0x1460
   __TEXT.__objc_methlist: 0xff2c
-  __TEXT.__cstring: 0x17546
-  __TEXT.__oslogstring: 0x17f49
+  __TEXT.__cstring: 0x15941
+  __TEXT.__oslogstring: 0x17fe9
   __TEXT.__const: 0x3d8
-  __TEXT.__gcc_except_tab: 0x6114
+  __TEXT.__gcc_except_tab: 0x6150
   __TEXT.__dlopen_cstrs: 0x5e
-  __TEXT.__unwind_info: 0x532c
+  __TEXT.__unwind_info: 0x52e8
   __TEXT.__objc_classname: 0x2c28
-  __TEXT.__objc_methname: 0x24db7
-  __TEXT.__objc_methtype: 0x6040
-  __TEXT.__objc_stubs: 0x16760
+  __TEXT.__objc_methname: 0x24dc5
+  __TEXT.__objc_methtype: 0x6001
+  __TEXT.__objc_stubs: 0x16780
   __DATA_CONST.__got: 0x340
-  __DATA_CONST.__const: 0x3950
+  __DATA_CONST.__const: 0x37c0
   __DATA_CONST.__objc_classlist: 0xc20
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1c680
-  __DATA_CONST.__objc_selrefs: 0x7bd0
+  __DATA_CONST.__objc_const: 0x1c660
+  __DATA_CONST.__objc_selrefs: 0x7bd8
   __DATA_CONST.__objc_arraydata: 0x630
   __AUTH_CONST.__cfstring: 0x12f00
   __AUTH_CONST.__objc_const: 0x8c30
-  __AUTH_CONST.__const: 0x1860
+  __AUTH_CONST.__const: 0x1880
   __AUTH_CONST.__objc_intobj: 0x2298
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x588

   __DATA.__objc_classrefs: 0xdf8
   __DATA.__objc_superrefs: 0x690
   __DATA.__objc_ivar: 0x179c
-  __DATA.__data: 0x2190
-  __DATA.__bss: 0x390
+  __DATA.__data: 0x2170
+  __DATA.__bss: 0x3b0
   __DATA.__common: 0x38
   __DATA_DIRTY.__const: 0x18
   __DATA_DIRTY.__objc_data: 0x2f30

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9A6A3480-4199-344E-AB28-6F0AFE8A2841
-  Functions: 8825
-  Symbols:   27152
-  CStrings:  14189
+  UUID: ABEB46AC-7135-3D08-84DA-A9FFF9E71CCB
+  Functions: 8769
+  Symbols:   27033
+  CStrings:  14135
 
Symbols:
+ -[_CDInteractionCache _handleInteractionRemoval:]
+ -[_CDInteractionCache initForTestingWithSize:]
+ -[_DKSync2Coordinator fetchSourceDeviceIDFromPeer:]
+ -[_DKSync2Coordinator handleFetchedSourceDeviceID:version:fromPeer:error:]
+ -[_DKSync2Coordinator handleFetchedSourceDeviceID:version:fromPeer:error:].cold.1
+ GCC_except_table107
+ GCC_except_table112
+ GCC_except_table116
+ GCC_except_table119
+ GCC_except_table121
+ GCC_except_table123
+ GCC_except_table125
+ GCC_except_table132
+ GCC_except_table134
+ GCC_except_table136
+ GCC_except_table138
+ GCC_except_table146
+ GCC_except_table155
+ GCC_except_table44
+ GCC_except_table61
+ GCC_except_table64
+ GCC_except_table70
+ GCC_except_table79
+ GCC_except_table85
+ ___100-[_DKXPCKnowledgeStore deleteAllEventsInEventStream:synchronous:error:responseQueue:withCompletion:]_block_invoke.11
+ ___100-[_DKXPCKnowledgeStore deleteAllEventsInEventStream:synchronous:error:responseQueue:withCompletion:]_block_invoke.11.cold.1
+ ___100-[_DKXPCKnowledgeStore deleteAllEventsInEventStream:synchronous:error:responseQueue:withCompletion:]_block_invoke.11.cold.2
+ ___100-[_DKXPCKnowledgeStore deleteAllEventsInEventStream:synchronous:error:responseQueue:withCompletion:]_block_invoke_2.12
+ ___100-[_DKXPCKnowledgeStore deleteAllEventsInEventStream:synchronous:error:responseQueue:withCompletion:]_block_invoke_3.cold.1
+ ___104-[_DKXPCKnowledgeStore deleteAllEventsMatchingPredicate:synchronous:error:responseQueue:withCompletion:]_block_invoke.14
+ ___104-[_DKXPCKnowledgeStore deleteAllEventsMatchingPredicate:synchronous:error:responseQueue:withCompletion:]_block_invoke.14.cold.1
+ ___104-[_DKXPCKnowledgeStore deleteAllEventsMatchingPredicate:synchronous:error:responseQueue:withCompletion:]_block_invoke.14.cold.2
+ ___104-[_DKXPCKnowledgeStore deleteAllEventsMatchingPredicate:synchronous:error:responseQueue:withCompletion:]_block_invoke_2.15
+ ___104-[_DKXPCKnowledgeStore deleteAllEventsMatchingPredicate:synchronous:error:responseQueue:withCompletion:]_block_invoke_3.cold.1
+ ___115-[_DKSyncRapportKnowledgeStorage fetchEventsFromPeer:windows:streamNames:limit:fetchOrder:highPriority:completion:]_block_invoke_2
+ ___34-[_DKXPCKnowledgeStore deviceUUID]_block_invoke.26
+ ___42-[_DKXPCKnowledgeStore deleteRemoteState:]_block_invoke.24
+ ___45-[_DKXPCKnowledgeStore synchronizeWithError:]_block_invoke.21
+ ___51-[_DKSync2Coordinator fetchSourceDeviceIDFromPeer:]_block_invoke
+ ___51-[_DKXPCKnowledgeStore confirmConnectionWithError:]_block_invoke.27
+ ___53-[_CDInteractionStore recordInteractionsBatch:error:]_block_invoke.119
+ ___53-[_CDInteractionStore recordInteractionsBatch:error:]_block_invoke.149
+ ___53-[_CDInteractionStore recordInteractionsBatch:error:]_block_invoke.149.cold.1
+ ___53-[_CDInteractionStore recordInteractionsBatch:error:]_block_invoke.149.cold.2
+ ___54-[_DKXPCKnowledgeStore sourceDeviceIdentityWithError:]_block_invoke.25
+ ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.647
+ ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.647.cold.1
+ ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.647.cold.2
+ ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.647.cold.3
+ ___56-[_DKKnowledgeStorage _databaseChangedWithNotification:]_block_invoke.688
+ ___56-[_DKKnowledgeStorage _databaseChangedWithNotification:]_block_invoke_2.691
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.619
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.619.cold.1
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.619.cold.2
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.619.cold.3
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.619.cold.4
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.619.cold.5
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.619.cold.6
+ ___60-[_DKXPCKnowledgeStore synchronizeWithUrgency:client:error:]_block_invoke.22
+ ___65-[_CDComplications admissionCheckOnComplication:forRemote:error:]_block_invoke.17
+ ___65-[_DKSyncRapportCommonStorage handshakeWithDuetSyncPeer:orError:]_block_invoke.156
+ ___66-[_DKKnowledgeStorage saveHistogram:responseQueue:withCompletion:]_block_invoke.590
+ ___66-[_DKKnowledgeStorage saveHistogram:responseQueue:withCompletion:]_block_invoke_2.cold.1
+ ___72-[_CDPSerializedDataHarvester loadWithLimit:dataPointReader:completion:]_block_invoke.cold.1
+ ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.672
+ ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.674
+ ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.675
+ ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke_3.cold.1
+ ___77-[_DKXPCKnowledgeStore saveObjects:synchronous:responseQueue:withCompletion:]_block_invoke_2.7
+ ___77-[_DKXPCKnowledgeStore saveObjects:synchronous:responseQueue:withCompletion:]_block_invoke_3.cold.1
+ ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.663
+ ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.666
+ ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.668
+ ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke_3.cold.1
+ ___79-[_DKXPCKnowledgeStore deleteObjects:synchronous:responseQueue:withCompletion:]_block_invoke_2.10
+ ___79-[_DKXPCKnowledgeStore deleteObjects:synchronous:responseQueue:withCompletion:]_block_invoke_2.9
+ ___79-[_DKXPCKnowledgeStore deleteObjects:synchronous:responseQueue:withCompletion:]_block_invoke_2.cold.1
+ ___79-[_DKXPCKnowledgeStore deleteObjects:synchronous:responseQueue:withCompletion:]_block_invoke_2.cold.2
+ ___79-[_DKXPCKnowledgeStore synchronizeWithUrgency:client:responseQueue:completion:]_block_invoke_2.23
+ ___79-[_DKXPCKnowledgeStore synchronizeWithUrgency:client:responseQueue:completion:]_block_invoke_3.cold.1
+ ___84-[_DKXPCKnowledgeStore executeQuery:synchronous:error:responseQueue:withCompletion:]_block_invoke_2.17
+ ___84-[_DKXPCKnowledgeStore executeQuery:synchronous:error:responseQueue:withCompletion:]_block_invoke_2.19
+ ___84-[_DKXPCKnowledgeStore executeQuery:synchronous:error:responseQueue:withCompletion:]_block_invoke_2.cold.1
+ ___84-[_DKXPCKnowledgeStore executeQuery:synchronous:error:responseQueue:withCompletion:]_block_invoke_2.cold.2
+ ___86-[_DKCloudUtilities _performUpdateNumberOfSyncedDevicesWithAttempt:completionHandler:]_block_invoke.488
+ ___block_descriptor_56_e8_32s40s48s_e41_v32?0"NSUUID"8"NSString"16"NSError"24ls32l8s40l8s48l8
+ ___block_literal_global.247
+ ___block_literal_global.413
+ ___block_literal_global.458
+ ___block_literal_global.518
+ ___block_literal_global.568
+ ___block_literal_global.571
+ ___block_literal_global.576
+ ___block_literal_global.601
+ ___block_literal_global.634
+ ___block_literal_global.677
+ ___cd_dispatch_async_capture_tx_block_invoke
+ __unnamed_array_storage.201
+ __unnamed_array_storage.213
+ __unnamed_array_storage.219
+ __unnamed_array_storage.291
+ __unnamed_array_storage.486
+ _objc_msgSend$_handleInteractionRemoval:
+ _objc_msgSend$initForTestingWithSize:
+ _sharedInstance.initialized.244
+ _sharedInstance.initialized.410
+ _sharedInstance.sharedInstance.245
+ _sharedInstance.sharedInstance.411
- -[_DKSyncRapportCommonStorage handshakeWithDuetSyncPeer:completion:]
- -[_DKSyncRapportKnowledgeStorage _fetchEventsFromPeer:windows:streamNames:limit:fetchOrder:highPriority:completion:]
- -[_DKSyncRapportStorage handshakeWithDuetSyncPeer:completion:]
- GCC_except_table108
- GCC_except_table110
- GCC_except_table129
- GCC_except_table131
- GCC_except_table135
- GCC_except_table141
- GCC_except_table145
- GCC_except_table153
- GCC_except_table163
- GCC_except_table166
- GCC_except_table170
- GCC_except_table181
- GCC_except_table182
- GCC_except_table59
- GCC_except_table74
- GCC_except_table82
- GCC_except_table83
- GCC_except_table93
- ___100-[_DKXPCKnowledgeStore deleteAllEventsInEventStream:synchronous:error:responseQueue:withCompletion:]_block_invoke.20
- ___100-[_DKXPCKnowledgeStore deleteAllEventsInEventStream:synchronous:error:responseQueue:withCompletion:]_block_invoke.20.cold.1
- ___100-[_DKXPCKnowledgeStore deleteAllEventsInEventStream:synchronous:error:responseQueue:withCompletion:]_block_invoke.20.cold.2
- ___100-[_DKXPCKnowledgeStore deleteAllEventsInEventStream:synchronous:error:responseQueue:withCompletion:]_block_invoke_2.22
- ___100-[_DKXPCKnowledgeStore deleteAllEventsInEventStream:synchronous:error:responseQueue:withCompletion:]_block_invoke_2.24
- ___100-[_DKXPCKnowledgeStore deleteAllEventsInEventStream:synchronous:error:responseQueue:withCompletion:]_block_invoke_3.25
- ___100-[_DKXPCKnowledgeStore deleteAllEventsInEventStream:synchronous:error:responseQueue:withCompletion:]_block_invoke_4
- ___100-[_DKXPCKnowledgeStore deleteAllEventsInEventStream:synchronous:error:responseQueue:withCompletion:]_block_invoke_4.cold.1
- ___104-[_DKXPCKnowledgeStore deleteAllEventsMatchingPredicate:synchronous:error:responseQueue:withCompletion:]_block_invoke.28
- ___104-[_DKXPCKnowledgeStore deleteAllEventsMatchingPredicate:synchronous:error:responseQueue:withCompletion:]_block_invoke.28.cold.1
- ___104-[_DKXPCKnowledgeStore deleteAllEventsMatchingPredicate:synchronous:error:responseQueue:withCompletion:]_block_invoke.28.cold.2
- ___104-[_DKXPCKnowledgeStore deleteAllEventsMatchingPredicate:synchronous:error:responseQueue:withCompletion:]_block_invoke_2.30
- ___104-[_DKXPCKnowledgeStore deleteAllEventsMatchingPredicate:synchronous:error:responseQueue:withCompletion:]_block_invoke_2.32
- ___104-[_DKXPCKnowledgeStore deleteAllEventsMatchingPredicate:synchronous:error:responseQueue:withCompletion:]_block_invoke_3.33
- ___104-[_DKXPCKnowledgeStore deleteAllEventsMatchingPredicate:synchronous:error:responseQueue:withCompletion:]_block_invoke_4
- ___104-[_DKXPCKnowledgeStore deleteAllEventsMatchingPredicate:synchronous:error:responseQueue:withCompletion:]_block_invoke_4.cold.1
- ___116-[_DKSyncRapportKnowledgeStorage _fetchEventsFromPeer:windows:streamNames:limit:fetchOrder:highPriority:completion:]_block_invoke
- ___116-[_DKSyncRapportKnowledgeStorage _fetchEventsFromPeer:windows:streamNames:limit:fetchOrder:highPriority:completion:]_block_invoke_2
- ___25-[_DKCloudUtilities init]_block_invoke_2
- ___34-[_DKXPCKnowledgeStore deviceUUID]_block_invoke.52
- ___36-[_CDPeriodicScheduler registerJob:]_block_invoke.64
- ___39-[_CDInteractionStoreNotifier deleted:]_block_invoke_2
- ___39-[_DKCloudUtilities _accountDidChange:]_block_invoke_2
- ___40-[_CDInteractionStoreNotifier recorded:]_block_invoke_2
- ___42-[_DKXPCKnowledgeStore deleteRemoteState:]_block_invoke.50
- ___45-[CDMonitorManager deliverNotificationEvent:]_block_invoke_2
- ___45-[_DKXPCKnowledgeStore synchronizeWithError:]_block_invoke.44
- ___46-[CDMonitorManager _stopMonitorForStreamName:]_block_invoke_2
- ___46-[_DKCloudUtilities _updateAccountInfo:error:]_block_invoke_2
- ___47-[CDMonitorManager _startMonitorForStreamName:]_block_invoke_2
- ___51-[_DKXPCKnowledgeStore confirmConnectionWithError:]_block_invoke.53
- ___53-[_CDInteractionStore recordInteractionsBatch:error:]_block_invoke.120
- ___53-[_CDInteractionStore recordInteractionsBatch:error:]_block_invoke.150
- ___53-[_CDInteractionStore recordInteractionsBatch:error:]_block_invoke.150.cold.1
- ___53-[_CDInteractionStore recordInteractionsBatch:error:]_block_invoke.150.cold.2
- ___54-[_DKXPCKnowledgeStore sourceDeviceIdentityWithError:]_block_invoke.51
- ___55-[_CDTemporalInteractionAdvisor setConsumerToModelMap:]_block_invoke_2
- ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.655
- ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.655.cold.1
- ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.655.cold.2
- ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.655.cold.3
- ___56-[_DKKnowledgeStorage _databaseChangedWithNotification:]_block_invoke.707
- ___56-[_DKKnowledgeStorage _databaseChangedWithNotification:]_block_invoke_2.708
- ___56-[_DKKnowledgeStorage _databaseChangedWithNotification:]_block_invoke_5
- ___56-[_DKKnowledgeStorage _databaseChangedWithNotification:]_block_invoke_6
- ___56-[_DKKnowledgeStorage _databaseChangedWithNotification:]_block_invoke_7
- ___56-[_DKKnowledgeStorage _databaseChangedWithNotification:]_block_invoke_8
- ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.627
- ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.627.cold.1
- ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.627.cold.2
- ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.627.cold.3
- ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.627.cold.4
- ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.627.cold.5
- ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.627.cold.6
- ___57-[_CDPeopleSuggester suggestPeopleWithCompletionHandler:]_block_invoke_2
- ___60-[_CDInteractionStore recordInteractions:completionHandler:]_block_invoke_2
- ___60-[_DKXPCKnowledgeStore synchronizeWithUrgency:client:error:]_block_invoke.45
- ___63-[_DKKnowledgeStorage _sendEventsNotificationName:withObjects:]_block_invoke_4
- ___63-[_DKKnowledgeStorage _sendEventsNotificationName:withObjects:]_block_invoke_5
- ___63-[_DKKnowledgeStorage _sendEventsNotificationName:withObjects:]_block_invoke_6
- ___64-[_DKKnowledgeStorage saveObjects:responseQueue:withCompletion:]_block_invoke_3
- ___64-[_DKKnowledgeStorage saveObjects:responseQueue:withCompletion:]_block_invoke_4
- ___64-[_DKKnowledgeStore deleteObjects:responseQueue:withCompletion:]_block_invoke_2
- ___65-[_CDComplications admissionCheckOnComplication:forRemote:error:]_block_invoke.18
- ___65-[_CDComplications admissionCheckOnComplication:forRemote:error:]_block_invoke_2
- ___65-[_DKKnowledgeStorage executeQuery:responseQueue:withCompletion:]_block_invoke_3
- ___65-[_DKKnowledgeStorage executeQuery:responseQueue:withCompletion:]_block_invoke_4
- ___65-[_DKSyncRapportCommonStorage handshakeWithDuetSyncPeer:orError:]_block_invoke.158
- ___66-[_DKKnowledgeStorage deleteObjects:responseQueue:withCompletion:]_block_invoke_3
- ___66-[_DKKnowledgeStorage deleteObjects:responseQueue:withCompletion:]_block_invoke_4
- ___66-[_DKKnowledgeStorage saveHistogram:responseQueue:withCompletion:]_block_invoke.597
- ___66-[_DKKnowledgeStorage saveHistogram:responseQueue:withCompletion:]_block_invoke_2.598
- ___66-[_DKKnowledgeStorage saveHistogram:responseQueue:withCompletion:]_block_invoke_3.cold.1
- ___66-[_DKKnowledgeStorage saveHistogram:responseQueue:withCompletion:]_block_invoke_4
- ___66-[_DKKnowledgeStorage saveHistogram:responseQueue:withCompletion:]_block_invoke_5
- ___68-[_DKSyncRapportCommonStorage handshakeWithDuetSyncPeer:completion:]_block_invoke
- ___69-[_CDInteractionStore countContactsUsingPredicate:completionHandler:]_block_invoke_2
- ___70-[_DKKnowledgeStore saveObjects:tracker:responseQueue:withCompletion:]_block_invoke_2
- ___71-[_DKKnowledgeStorage _sendTombstoneNotificationsWithStreamNameCounts:]_block_invoke_2
- ___72-[_CDInteractionStore deleteInteractionsWithBundleId:completionHandler:]_block_invoke_2
- ___72-[_CDPSerializedDataHarvester loadWithLimit:dataPointReader:completion:]_block_invoke_2
- ___72-[_CDPSerializedDataHarvester loadWithLimit:dataPointReader:completion:]_block_invoke_2.cold.1
- ___72-[_DKKnowledgeStorage saveObjects:tracker:responseQueue:withCompletion:]_block_invoke_6
- ___72-[_DKKnowledgeStorage saveObjects:tracker:responseQueue:withCompletion:]_block_invoke_7
- ___73-[_CDInteractionStore countInteractionsUsingPredicate:completionHandler:]_block_invoke_2
- ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.686
- ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.689
- ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.692
- ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke_2.690
- ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke_2.693
- ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke_4
- ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke_4.cold.1
- ___76-[_DKKnowledgeStore synchronizeWithUrgency:client:responseQueue:completion:]_block_invoke_2
- ___77-[_DKXPCKnowledgeStore saveObjects:synchronous:responseQueue:withCompletion:]_block_invoke_2.9
- ___77-[_DKXPCKnowledgeStore saveObjects:synchronous:responseQueue:withCompletion:]_block_invoke_3.10
- ___77-[_DKXPCKnowledgeStore saveObjects:synchronous:responseQueue:withCompletion:]_block_invoke_4
- ___77-[_DKXPCKnowledgeStore saveObjects:synchronous:responseQueue:withCompletion:]_block_invoke_4.cold.1
- ___78-[_CDPInteractionStoreDataHarvester loadWithLimit:dataPointReader:completion:]_block_invoke_3
- ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.672
- ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.676
- ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.680
- ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke_2.677
- ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke_2.681
- ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke_4
- ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke_4.cold.1
- ___79-[_DKXPCKnowledgeStore deleteObjects:synchronous:responseQueue:withCompletion:]_block_invoke_2.14
- ___79-[_DKXPCKnowledgeStore deleteObjects:synchronous:responseQueue:withCompletion:]_block_invoke_2.17
- ___79-[_DKXPCKnowledgeStore deleteObjects:synchronous:responseQueue:withCompletion:]_block_invoke_3.15
- ___79-[_DKXPCKnowledgeStore deleteObjects:synchronous:responseQueue:withCompletion:]_block_invoke_3.18
- ___79-[_DKXPCKnowledgeStore deleteObjects:synchronous:responseQueue:withCompletion:]_block_invoke_3.cold.2
- ___79-[_DKXPCKnowledgeStore deleteObjects:synchronous:responseQueue:withCompletion:]_block_invoke_4
- ___79-[_DKXPCKnowledgeStore deleteObjects:synchronous:responseQueue:withCompletion:]_block_invoke_4.cold.1
- ___79-[_DKXPCKnowledgeStore synchronizeWithUrgency:client:responseQueue:completion:]_block_invoke_2.48
- ___79-[_DKXPCKnowledgeStore synchronizeWithUrgency:client:responseQueue:completion:]_block_invoke_3.49
- ___79-[_DKXPCKnowledgeStore synchronizeWithUrgency:client:responseQueue:completion:]_block_invoke_4
- ___79-[_DKXPCKnowledgeStore synchronizeWithUrgency:client:responseQueue:completion:]_block_invoke_4.cold.1
- ___80-[_CDInteractionStore deleteInteractionsWithBundleId:account:completionHandler:]_block_invoke_2
- ___84-[_DKXPCKnowledgeStore executeQuery:synchronous:error:responseQueue:withCompletion:]_block_invoke_2.37
- ___84-[_DKXPCKnowledgeStore executeQuery:synchronous:error:responseQueue:withCompletion:]_block_invoke_2.41
- ___84-[_DKXPCKnowledgeStore executeQuery:synchronous:error:responseQueue:withCompletion:]_block_invoke_3.38
- ___84-[_DKXPCKnowledgeStore executeQuery:synchronous:error:responseQueue:withCompletion:]_block_invoke_3.42
- ___84-[_DKXPCKnowledgeStore executeQuery:synchronous:error:responseQueue:withCompletion:]_block_invoke_3.cold.2
- ___84-[_DKXPCKnowledgeStore executeQuery:synchronous:error:responseQueue:withCompletion:]_block_invoke_4
- ___84-[_DKXPCKnowledgeStore executeQuery:synchronous:error:responseQueue:withCompletion:]_block_invoke_4.cold.1
- ___85-[_DKKnowledgeStorage deleteAllEventsMatchingPredicate:responseQueue:withCompletion:]_block_invoke_3
- ___85-[_DKKnowledgeStorage deleteAllEventsMatchingPredicate:responseQueue:withCompletion:]_block_invoke_4
- ___86-[_DKCloudUtilities _performUpdateNumberOfSyncedDevicesWithAttempt:completionHandler:]_block_invoke.491
- ___89-[_CDInteractionStore deleteInteractionsWithBundleId:domainIdentifier:completionHandler:]_block_invoke_2
- ___90-[_CDInteractionStore deleteInteractionsWithBundleId:domainIdentifiers:completionHandler:]_block_invoke_2
- ___91-[_CDInteractionStore queryContactsUsingPredicate:sortDescriptors:limit:completionHandler:]_block_invoke_2
- ___95-[_CDInteractionStore queryInteractionsUsingPredicate:sortDescriptors:limit:completionHandler:]_block_invoke_2
- ___99-[_CDInteractionStore deleteInteractionsMatchingPredicate:sortDescriptors:limit:completionHandler:]_block_invoke_2
- ___block_descriptor_56_e8_32s40bs48r_e5_v8?0ls40l8r48l8s32l8
- ___block_descriptor_57_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40bs48r56r_e5_v8?0ls40l8r48l8r56l8s32l8
- ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48bs56bs_e5_v8?0ls32l8s48l8s56l8s40l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e41_v32?0"NSUUID"8"NSString"16"NSError"24ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s64l8s56l8
- ___block_descriptor_80_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s64l8s56l8
- ___block_descriptor_88_e8_32s40s48s56s64r72r_e5_v8?0ls32l8s40l8r64l8s48l8r72l8s56l8
- ___block_descriptor_89_e8_32s40s48s56s64bs_e41_v32?0"NSUUID"8"NSString"16"NSError"24ls32l8s40l8s64l8s48l8s56l8
- ___block_literal_global.249
- ___block_literal_global.415
- ___block_literal_global.522
- ___block_literal_global.572
- ___block_literal_global.575
- ___block_literal_global.580
- ___block_literal_global.609
- ___block_literal_global.642
- ___block_literal_global.695
- __unnamed_array_storage.206
- __unnamed_array_storage.218
- __unnamed_array_storage.224
- __unnamed_array_storage.293
- __unnamed_array_storage.489
- _objc_msgSend$handshakeWithDuetSyncPeer:completion:
- _sharedInstance.initialized.246
- _sharedInstance.initialized.412
- _sharedInstance.sharedInstance.247
- _sharedInstance.sharedInstance.413
CStrings:
+ "%{public}@: Failed while requesting source device id from %{public}@peer %{public}@%{public}@: %{public}@:%lld (%@)"
+ "%{public}@: Missing source device id requested from %{public}@peer %{public}@%{public}@"
+ "%{public}@: Received source device id %{public}@ from %{public}@peer %{public}@%{public}@"
+ "Caching interaction %{sensitive}@ to index %tu"
+ "Deleting interaction %{sensitive}@ at index %tu"
+ "Will truncate interaction %{sensitive}@ at index %tu"
+ "_handleInteractionRemoval:"
+ "cd_dispatch_async_tx"
+ "cd_dispatch_sync_tx"
+ "com.apple.coreduetd.fetch-source-device-id"
+ "initForTestingWithSize:"
- "%{public}@: Handshake completed with peer, fetching events %{public}@peer %{public}@%{public}@"
- "%{public}@: Handshake failed with peer %{public}@peer %{public}@%{public}@"
- "%{public}@: Handshake previously completed with peer %{public}@peer %{public}@%{public}@"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/CDMonitorManager.m:374"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Interaction/_CDInteractionAdviceEngine.m:1166"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Interaction/_CDInteractionStore.m:1381"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Interaction/_CDInteractionStore.m:1414"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Interaction/_CDInteractionStore.m:1602"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Interaction/_CDInteractionStore.m:1716"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Interaction/_CDInteractionStore.m:2363"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Interaction/_CDInteractionStore.m:2375"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Interaction/_CDInteractionStore.m:2387"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Interaction/_CDInteractionStore.m:2401"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Interaction/_CDInteractionStore.m:2415"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Interaction/_CDInteractionStore.m:940"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Interaction/_CDInteractionStoreNotifier.m:144"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Interaction/_CDInteractionStoreNotifier.m:166"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Interaction/_CDPInteractionStoreDataHarvester.m:61"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Interaction/_CDPSerializedDataHarvester.m:54"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Interaction/_CDPeopleSuggester.m:183"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/Storage/_DKKnowledgeStorage.m:1605"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/Storage/_DKKnowledgeStorage.m:1627"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/Storage/_DKKnowledgeStorage.m:1630"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/Storage/_DKKnowledgeStorage.m:2121"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/Storage/_DKKnowledgeStorage.m:2138"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/Storage/_DKKnowledgeStorage.m:2156"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/Storage/_DKKnowledgeStorage.m:2175"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/Storage/_DKKnowledgeStorage.m:2192"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/Storage/_DKKnowledgeStorage.m:2211"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/Storage/_DKKnowledgeStorage.m:2366"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/Storage/_DKKnowledgeStorage.m:2375"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/Storage/_DKKnowledgeStorage.m:2383"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/Storage/_DKKnowledgeStorage.m:2386"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/Storage/_DKKnowledgeStorage.m:431"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/Storage/_DKKnowledgeStorage.m:437"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/Storage/_DKKnowledgeStorage.m:443"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/Storage/_DKKnowledgeStorage.m:462"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/Syncing/_DKCloudUtilities.m:149"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/Syncing/_DKCloudUtilities.m:230"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/Syncing/_DKCloudUtilities.m:320"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/_DKKnowledgeStore.m:172"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/_DKKnowledgeStore.m:219"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/_DKKnowledgeStore.m:340"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/_DKXPCKnowledgeStore.m:110"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/_DKXPCKnowledgeStore.m:163"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/_DKXPCKnowledgeStore.m:176"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/_DKXPCKnowledgeStore.m:199"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/_DKXPCKnowledgeStore.m:241"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/_DKXPCKnowledgeStore.m:260"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/_DKXPCKnowledgeStore.m:286"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/_DKXPCKnowledgeStore.m:327"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/_DKXPCKnowledgeStore.m:346"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/_DKXPCKnowledgeStore.m:371"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/_DKXPCKnowledgeStore.m:419"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/_DKXPCKnowledgeStore.m:432"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/_DKXPCKnowledgeStore.m:460"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/_DKXPCKnowledgeStore.m:574"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/_DKXPCKnowledgeStore.m:588"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/_DKXPCKnowledgeStore.m:88"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Utilities/_CDPeriodicScheduler.m:286"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Utilities/_CDPeriodicScheduler.m:288"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/_CDComplications.m:222"
- "Caching interaction %@"
- "handshakeWithDuetSyncPeer:completion:"
- "v32@0:8@\"_DKSyncPeer\"16@?<v@?@\"NSUUID\"@\"NSString\"@\"NSError\">24"

```
