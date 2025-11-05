## WiFiAnalytics

> `/System/Library/PrivateFrameworks/WiFiAnalytics.framework/Versions/A/WiFiAnalytics`

```diff

-645.4.0.0.0
-  __TEXT.__text: 0xfb700
-  __TEXT.__auth_stubs: 0xd80
-  __TEXT.__objc_methlist: 0xc23c
+675.32.0.0.0
+  __TEXT.__text: 0x10016c
+  __TEXT.__auth_stubs: 0xd50
+  __TEXT.__objc_methlist: 0xc574
   __TEXT.__const: 0x2b0
-  __TEXT.__cstring: 0xdde2
-  __TEXT.__oslogstring: 0xb004
-  __TEXT.__swift5_typeref: 0x128
+  __TEXT.__cstring: 0xdfac
+  __TEXT.__oslogstring: 0xaaba
+  __TEXT.__swift5_typeref: 0xfb
   __TEXT.__constg_swiftt: 0x178
   __TEXT.__swift5_reflstr: 0x61
   __TEXT.__swift5_fieldmd: 0x70
   __TEXT.__swift5_capture: 0x2c0
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0x1114
-  __TEXT.__unwind_info: 0x1d00
+  __TEXT.__gcc_except_tab: 0x17c4
+  __TEXT.__unwind_info: 0x1f78
   __TEXT.__eh_frame: 0x670
-  __TEXT.__objc_classname: 0xaaf
-  __TEXT.__objc_methname: 0x18f7e
-  __TEXT.__objc_methtype: 0x3487
-  __TEXT.__objc_stubs: 0x8c60
-  __DATA_CONST.__got: 0x628
-  __DATA_CONST.__const: 0x1038
-  __DATA_CONST.__objc_classlist: 0x2d8
+  __TEXT.__objc_classname: 0xa6b
+  __TEXT.__objc_methname: 0x19398
+  __TEXT.__objc_methtype: 0x34b7
+  __TEXT.__objc_stubs: 0x91c0
+  __DATA_CONST.__got: 0x5f8
+  __DATA_CONST.__const: 0x1060
+  __DATA_CONST.__objc_classlist: 0x2c0
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6b20
+  __DATA_CONST.__objc_selrefs: 0x6c38
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x238
+  __DATA_CONST.__objc_superrefs: 0x228
   __DATA_CONST.__objc_arraydata: 0xf0
-  __AUTH_CONST.__auth_got: 0x6d0
-  __AUTH_CONST.__const: 0x1d90
-  __AUTH_CONST.__cfstring: 0xb020
-  __AUTH_CONST.__objc_const: 0x10de0
-  __AUTH_CONST.__objc_intobj: 0x90
+  __AUTH_CONST.__auth_got: 0x6b8
+  __AUTH_CONST.__const: 0x1e50
+  __AUTH_CONST.__cfstring: 0xb0e0
+  __AUTH_CONST.__objc_const: 0x10890
+  __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x180
-  __AUTH.__objc_data: 0x1b28
+  __AUTH.__objc_data: 0x1a38
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0xc70
-  __DATA.__data: 0x270
-  __DATA.__bss: 0x18
+  __DATA.__objc_ivar: 0xc5c
+  __DATA.__data: 0x260
   __DATA.__common: 0x11f8
+  __DATA.__bss: 0x18
   __DATA_DIRTY.__objc_data: 0x320
-  __DATA_DIRTY.__bss: 0xe0
+  __DATA_DIRTY.__bss: 0xb0
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/Versions/A/CoreLocation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 740957F9-0718-3DD3-934E-1D64B61434ED
-  Functions: 4619
-  Symbols:   7900
-  CStrings:  9603
+  UUID: BDB8E663-DB6B-3E94-9513-4D27568F9098
+  Functions: 4724
+  Symbols:   8091
+  CStrings:  9625
 
Symbols:
+ +[AnalyticsProcessor analyticsProcessorWithPersistentContainer:]
+ +[AnalyticsStoreDescriptor defaultModelName]
+ +[AnalyticsStoreDescriptor optionDescription:]
+ +[AnalyticsStoreDescriptor storeDescriptor]
+ +[AnalyticsStoreFileWriter analyticsStoreFileWriterDirectory]
+ +[AnalyticsStoreFileWriter writeData:toFile:]
+ +[AnalyticsStoreFileWriter writeObj:toJSONFile:]
+ +[AnalyticsStoreMOHandler sharedAnalyticsStoreMOHandlerWithContainer:]
+ +[NSPersistentContainer(WAPersistentContainer) storeNeedsImmediatePruning:]
+ +[WAAnalyticsAccess accessWithPersistentContainer:]
+ +[WADeviceAnalyticsClient addPersistentStoreRemoteChangeNotificationObserver:selector:coordinator:]
+ +[WADeviceAnalyticsClient removePersistentStoreRemoteChangeNotificationObserver:coordinator:]
+ +[WADeviceAnalyticsClient sharedDeviceAnalyticsClient]
+ +[WAUtil customMigrationOnProcess]
+ +[WAUtil customXPCStoreOnProcess]
+ +[WAUtil isWritingInAnalyticsStoreAllowed]
+ +[WAUtil setFutureApfsPurgeableDeadline:forURL:]
+ -[AnalyticsProcessor getPolicyHandlersConfig]
+ -[AnalyticsProcessor initPolicyHandlers]
+ -[AnalyticsProcessor initWithPersistentContainer:]
+ -[AnalyticsProcessor processWAMessageMetric:data:andSave:]
+ -[AnalyticsProcessor releaseBackgroundProcessingMOC]
+ -[AnalyticsProcessor saveAndResetManagedObjectContext]
+ -[AnalyticsProcessor setPolicyHandlersConfig:]
+ -[AnalyticsProcessor updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:]
+ -[AnalyticsReader apProfileForBssid:andSSID:]
+ -[AnalyticsReader initWithPersistentContainer:]
+ -[AnalyticsReader moc]
+ -[AnalyticsReader persistentContainer]
+ -[AnalyticsReader releaseBackgroundReadingMOC]
+ -[AnalyticsReader resetBackgroundReadingMOC]
+ -[AnalyticsReader setBackgroundReadingMOC:]
+ -[AnalyticsReader setPersistentContainer:]
+ -[AnalyticsStoreDescriptor analyticsStoreOptionsDescription]
+ -[AnalyticsStoreDescriptor description]
+ -[AnalyticsStoreDescriptor initWithStoreURL:modelURL:]
+ -[AnalyticsStoreDescriptor setAnalyticsStoreOptionsDescription:]
+ -[AnalyticsStoreDescriptor setStoreDescription:]
+ -[AnalyticsStoreFileWriter backgroundFileWritingMOC]
+ -[AnalyticsStoreFileWriter initWithPersistentContainer:]
+ -[AnalyticsStoreFileWriter moc]
+ -[AnalyticsStoreFileWriter mom]
+ -[AnalyticsStoreFileWriter persistentContainer]
+ -[AnalyticsStoreFileWriter releaseBackgroundFileWritingMOC]
+ -[AnalyticsStoreFileWriter setBackgroundFileWritingMOC:]
+ -[AnalyticsStoreFileWriter setPersistentContainer:]
+ -[AnalyticsStoreMOHandler backgroundStoreMoHandlerMOC]
+ -[AnalyticsStoreMOHandler initWithContainer:]
+ -[AnalyticsStoreMOHandler persistentContainer]
+ -[AnalyticsStoreMOHandler releaseBackgroundStoreMoHandlerMOC]
+ -[AnalyticsStoreMOHandler setBackgroundStoreMoHandlerMOC:]
+ -[AnalyticsStoreMOHandler setPersistentContainer:]
+ -[NeighborGraph copyNeighborGraphAsDictionaryOnMoc:]
+ -[NeighborGraph initWithBssidArray:ssid:persistentContainer:]
+ -[NeighborGraph persistentContainer]
+ -[NeighborGraph setPersistentContainer:]
+ -[WAAnalyticsAccess _countForFetchRequest:error:onMoc:]
+ -[WAAnalyticsAccess _countForFetchRequestWithBlockAndWait:error:onMoc:]
+ -[WAAnalyticsAccess _performFetch:error:onMoc:]
+ -[WAAnalyticsAccess _performFetchWithBlockAndWait:error:onMoc:]
+ -[WAAnalyticsAccess backgroundRawAccessMOC]
+ -[WAAnalyticsAccess canWrite]
+ -[WAAnalyticsAccess countForFetchRequestWithBlockAndWait:error:]
+ -[WAAnalyticsAccess countForFetchRequestWithBlockAndWaitOnBbMoc:error:]
+ -[WAAnalyticsAccess initWithOptions:andContainer:]
+ -[WAAnalyticsAccess performFetchWithBlockAndWait:error:]
+ -[WAAnalyticsAccess performFetchWithBlockAndWaitOnBbMoc:error:]
+ -[WAAnalyticsAccess persistentContainer]
+ -[WAAnalyticsAccess releaseBackgroundRawAccessMOC]
+ -[WAAnalyticsAccess resetBackgroundRawAccessMOC]
+ -[WAAnalyticsAccess setBackgroundRawAccessMOC:]
+ -[WAAnalyticsAccess setPersistentContainer:]
+ -[WAClient exportedRemoteInterface]
+ -[WAClient setExportedRemoteInterface:]
+ -[WAClient updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:andReply:]
+ -[WAClient updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:andReply:queuedInvocation:]
+ -[WADeviceAnalyticsClient addPersistentStoreRemoteChangeNotificationObserver:selector:]
+ -[WADeviceAnalyticsClient ageOutAnalytics:]
+ -[WADeviceAnalyticsClient analyticsProcessorObj]
+ -[WADeviceAnalyticsClient analyticsProcessor]
+ -[WADeviceAnalyticsClient analyticsRawAccessObj]
+ -[WADeviceAnalyticsClient analyticsRawAccess]
+ -[WADeviceAnalyticsClient apProfileForBssid:andSSID:]
+ -[WADeviceAnalyticsClient countForFetchRequest:error:]
+ -[WADeviceAnalyticsClient dumpDeploymentGraphJSONFile]
+ -[WADeviceAnalyticsClient dumpDeviceAnalyticsCSVsToFileWithBatchSize:maxAge:]
+ -[WADeviceAnalyticsClient dumpDeviceAnalyticsToFileWithFetchLimit:maxAge:]
+ -[WADeviceAnalyticsClient dumpDeviceAnalyticsToFile]
+ -[WADeviceAnalyticsClient dumpDeviceAnalyticsUsingBatchSizeToFileWithBatchSize:maxAge:]
+ -[WADeviceAnalyticsClient getPolicyHandlersConfig]
+ -[WADeviceAnalyticsClient loadStoreIfNeeded]
+ -[WADeviceAnalyticsClient loadStore]
+ -[WADeviceAnalyticsClient performFetch:error:]
+ -[WADeviceAnalyticsClient performPruneBasedOnStoreSizeAndSave]
+ -[WADeviceAnalyticsClient performPruneTestBSSes:]
+ -[WADeviceAnalyticsClient persistentContainer]
+ -[WADeviceAnalyticsClient processDatapathMetricStream:withDate:]
+ -[WADeviceAnalyticsClient processWAMessageMetric:data:]
+ -[WADeviceAnalyticsClient processWAMessageMetric:data:andDeferSaveToDisk:]
+ -[WADeviceAnalyticsClient rawAccessCanWrite]
+ -[WADeviceAnalyticsClient releaseBackgroundFileWritingMOC]
+ -[WADeviceAnalyticsClient releaseBackgroundProcessingMOC]
+ -[WADeviceAnalyticsClient releaseBackgroundRawAccessMOC]
+ -[WADeviceAnalyticsClient releaseBackgroundReadingMOC]
+ -[WADeviceAnalyticsClient removePersistentStoreRemoteChangeNotificationObserver:]
+ -[WADeviceAnalyticsClient resetBackgroundRawAccessMOC]
+ -[WADeviceAnalyticsClient resetBackgroundReadingMOC]
+ -[WADeviceAnalyticsClient saveAndResetBackgroundProcessingMOC]
+ -[WADeviceAnalyticsClient setAnalyticsProcessorObj:]
+ -[WADeviceAnalyticsClient setAnalyticsRawAccessObj:]
+ -[WADeviceAnalyticsClient setPersistentContainer:]
+ -[WADeviceAnalyticsClient setPolicyHandlersConfig:]
+ -[WADeviceAnalyticsClient setStoreLoadError:]
+ -[WADeviceAnalyticsClient setStoreLoaded:]
+ -[WADeviceAnalyticsClient storeLoadError]
+ -[WADeviceAnalyticsClient storeLoaded]
+ -[WADeviceAnalyticsClient updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:]
+ -[WAXPCConnection updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:andReply:]
+ GCC_except_table103
+ GCC_except_table115
+ GCC_except_table12
+ GCC_except_table121
+ GCC_except_table127
+ GCC_except_table139
+ GCC_except_table147
+ GCC_except_table149
+ GCC_except_table2
+ GCC_except_table22
+ GCC_except_table32
+ GCC_except_table40
+ GCC_except_table42
+ GCC_except_table46
+ GCC_except_table48
+ GCC_except_table50
+ GCC_except_table53
+ GCC_except_table54
+ GCC_except_table55
+ GCC_except_table58
+ GCC_except_table60
+ GCC_except_table62
+ GCC_except_table64
+ GCC_except_table66
+ GCC_except_table68
+ GCC_except_table70
+ GCC_except_table72
+ GCC_except_table74
+ GCC_except_table76
+ GCC_except_table78
+ GCC_except_table8
+ GCC_except_table80
+ OBJC_IVAR_$_AnalyticsReader._persistentContainer
+ OBJC_IVAR_$_AnalyticsStoreDescriptor._analyticsStoreOptionsDescription
+ OBJC_IVAR_$_AnalyticsStoreFileWriter._backgroundFileWritingMOC
+ OBJC_IVAR_$_AnalyticsStoreFileWriter._persistentContainer
+ OBJC_IVAR_$_AnalyticsStoreMOHandler._backgroundStoreMoHandlerMOC
+ OBJC_IVAR_$_AnalyticsStoreMOHandler._persistentContainer
+ OBJC_IVAR_$_NeighborGraph._persistentContainer
+ OBJC_IVAR_$_WAAnalyticsAccess._backgroundRawAccessMOC
+ OBJC_IVAR_$_WAAnalyticsAccess._persistentContainer
+ OBJC_IVAR_$_WAClient._exportedRemoteInterface
+ OBJC_IVAR_$_WADeviceAnalyticsClient._analyticsProcessorObj
+ OBJC_IVAR_$_WADeviceAnalyticsClient._analyticsRawAccessObj
+ OBJC_IVAR_$_WADeviceAnalyticsClient._persistentContainer
+ OBJC_IVAR_$_WADeviceAnalyticsClient._storeLoadError
+ OBJC_IVAR_$_WADeviceAnalyticsClient._storeLoaded
+ _NSCocoaErrorDomain
+ _NSMergeByPropertyObjectTrumpMergePolicy
+ _NSMergeByPropertyStoreTrumpMergePolicy
+ _NSPersistentStoreRemoteChangeNotification
+ _OBJC_CLASS_$_NSPersistentContainer
+ __100-[AnalyticsReader copyScoreSortedNetworksAvailableAtLocationWithinDistance:distance:authComparator:]_block_invoke.101
+ __100-[AnalyticsReader copyScoreSortedNetworksAvailableAtLocationWithinDistance:distance:authComparator:]_block_invoke.106
+ __100-[AnalyticsReader copyScoreSortedNetworksAvailableAtLocationWithinDistance:distance:authComparator:]_block_invoke.99
+ __101-[WAClient updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:andReply:queuedInvocation:]_block_invoke.247
+ __101-[WAClient updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:andReply:queuedInvocation:]_block_invoke.250
+ __36-[WADeviceAnalyticsClient loadStore]_block_invoke.62
+ __38-[WAClient _establishDaemonConnection]_block_invoke.196
+ __38-[WAClient _establishDaemonConnection]_block_invoke.198
+ __38-[WAClient _establishDaemonConnection]_block_invoke.200
+ __38-[WAClient _establishDaemonConnection]_block_invoke_2.197
+ __38-[WAClient _establishDaemonConnection]_block_invoke_2.199
+ __46-[WAClient _replyAllWithTimeoutErrorAndRemove]_block_invoke.223
+ __49-[WAClient _killDaemonAndReply:queuedInvocation:]_block_invoke.171
+ __49-[WAClient _killDaemonAndReply:queuedInvocation:]_block_invoke.172
+ __50-[WAClient _getDpsStatsandReply:queuedInvocation:]_block_invoke.164
+ __50-[WAClient _getDpsStatsandReply:queuedInvocation:]_block_invoke.168
+ __52-[NeighborGraph copyNeighborGraphAsDictionaryOnMoc:]_block_invoke.131
+ __52-[WAClient _getUsageStatsandReply:queuedInvocation:]_block_invoke.261
+ __52-[WAClient _getUsageStatsandReply:queuedInvocation:]_block_invoke.265
+ __54-[AnalyticsStoreFileWriter writeDeploymentGraphToFile]_block_invoke.71
+ __56-[WAClient _clearMessageStoreAndReply:queuedInvocation:]_block_invoke.173
+ __56-[WAClient _clearMessageStoreAndReply:queuedInvocation:]_block_invoke.174
+ __58-[AnalyticsProcessor processWAMessageMetric:data:andSave:]_block_invoke.76
+ __64-[WAClient _sendMemoryPressureRequestAndReply:queuedInvocation:]_block_invoke.179
+ __64-[WAClient _sendMemoryPressureRequestAndReply:queuedInvocation:]_block_invoke.180
+ __65-[WAClient _triggerQueryForNWActivity:andReply:queuedInvocation:]_block_invoke.149
+ __65-[WAClient _triggerQueryForNWActivity:andReply:queuedInvocation:]_block_invoke.153
+ __68-[WAClient _getMessagesModelForGroupType:andReply:queuedInvocation:]_block_invoke.175
+ __70-[WAClient _getDeviceAnalyticsConfigurationAndReply:queuedInvocation:]_block_invoke.242
+ __70-[WAClient _getDeviceAnalyticsConfigurationAndReply:queuedInvocation:]_block_invoke.246
+ __70-[WAClient _issueIOReportManagementCommand:andReply:queuedInvocation:]_block_invoke.256
+ __70-[WAClient _issueIOReportManagementCommand:andReply:queuedInvocation:]_block_invoke.260
+ __71-[WAClient _setDeviceAnalyticsConfiguration:andReply:queuedInvocation:]_block_invoke.238
+ __74-[WAClient _submitWiFiAnalyticsMessageAdvanced:andReply:queuedInvocation:]_block_invoke.138
+ __74-[WAClient _submitWiFiAnalyticsMessageAdvanced:andReply:queuedInvocation:]_block_invoke.142
+ __74-[WAClient _submitWiFiAnalyticsMessageAdvanced:andReply:queuedInvocation:]_block_invoke_2.146
+ __74-[WADeviceAnalyticsClient dumpDeviceAnalyticsToFileWithFetchLimit:maxAge:]_block_invoke.90
+ __75-[WAClient _triggerDeviceAnalyticsStoreMigrationAndReply:queuedInvocation:]_block_invoke.251
+ __75-[WAClient _triggerDeviceAnalyticsStoreMigrationAndReply:queuedInvocation:]_block_invoke.255
+ __80-[WAClient _lqmCrashTracerNotifyForInterfaceWithName:andReply:queuedInvocation:]_block_invoke.228
+ __87-[WAClient _lqmCrashTracerReceiveBlock:forInterfaceWithName:andReply:queuedInvocation:]_block_invoke.232
+ __88-[WAClient _trapCrashMiniTracerDumpReadyForInterfaceWithName:andReply:queuedInvocation:]_block_invoke.224
+ __93-[WAClient _triggerDatapathDiagnosticsAndCollectUpdates:waMessage:andReply:queuedInvocation:]_block_invoke.159
+ __93-[WAClient _triggerDatapathDiagnosticsAndCollectUpdates:waMessage:andReply:queuedInvocation:]_block_invoke.163
+ __95-[WAClient convertWiFiStatsIntoPercentile:analysisGroup:groupTarget:andReply:queuedInvocation:]_block_invoke.154
+ __95-[WAClient convertWiFiStatsIntoPercentile:analysisGroup:groupTarget:andReply:queuedInvocation:]_block_invoke.158
+ __Block_byref_object_copy_.84
+ __Block_byref_object_dispose_.85
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSPersistentContainer_$_WAPersistentContainer
+ __OBJC_$_CATEGORY_NSPersistentContainer_$_WAPersistentContainer
+ ___101-[WAClient updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:andReply:queuedInvocation:]_block_invoke
+ ___101-[WAClient updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:andReply:queuedInvocation:]_block_invoke_2
+ ___108-[WADeviceAnalyticsClient copyScoreSortedNetworksAvailableAtLocationWithinDistance:distance:authComparator:]_block_invoke
+ ___31-[WADeviceAnalyticsClient init]_block_invoke
+ ___33+[WAUtil customXPCStoreOnProcess]_block_invoke
+ ___34+[WAUtil customMigrationOnProcess]_block_invoke
+ ___36-[WADeviceAnalyticsClient loadStore]_block_invoke
+ ___36-[WADeviceAnalyticsClient loadStore]_block_invoke_2
+ ___42+[WAUtil isWritingInAnalyticsStoreAllowed]_block_invoke
+ ___42-[WADeviceAnalyticsClient analyticsReader]_block_invoke
+ ___42-[WADeviceAnalyticsClient analyticsReader]_block_invoke_2
+ ___42-[WADeviceAnalyticsClient analyticsReader]_block_invoke_3
+ ___42-[WADeviceAnalyticsClient analyticsReader]_block_invoke_4
+ ___42-[WADeviceAnalyticsClient analyticsReader]_block_invoke_5
+ ___43-[WADeviceAnalyticsClient ageOutAnalytics:]_block_invoke
+ ___43-[WADeviceAnalyticsClient isMovingNetwork:]_block_invoke
+ ___45-[AnalyticsReader apProfileForBssid:andSSID:]_block_invoke
+ ___45-[WADeviceAnalyticsClient analyticsProcessor]_block_invoke
+ ___45-[WADeviceAnalyticsClient analyticsProcessor]_block_invoke_2
+ ___45-[WADeviceAnalyticsClient analyticsProcessor]_block_invoke_3
+ ___45-[WADeviceAnalyticsClient analyticsProcessor]_block_invoke_4
+ ___45-[WADeviceAnalyticsClient analyticsProcessor]_block_invoke_5
+ ___45-[WADeviceAnalyticsClient analyticsRawAccess]_block_invoke
+ ___45-[WADeviceAnalyticsClient analyticsRawAccess]_block_invoke_2
+ ___45-[WADeviceAnalyticsClient analyticsRawAccess]_block_invoke_3
+ ___45-[WADeviceAnalyticsClient analyticsRawAccess]_block_invoke_4
+ ___45-[WADeviceAnalyticsClient analyticsRawAccess]_block_invoke_5
+ ___46-[WADeviceAnalyticsClient analyticsFileWriter]_block_invoke
+ ___46-[WADeviceAnalyticsClient analyticsFileWriter]_block_invoke_2
+ ___46-[WADeviceAnalyticsClient analyticsFileWriter]_block_invoke_3
+ ___46-[WADeviceAnalyticsClient analyticsFileWriter]_block_invoke_4
+ ___46-[WADeviceAnalyticsClient analyticsFileWriter]_block_invoke_5
+ ___46-[WADeviceAnalyticsClient performFetch:error:]_block_invoke
+ ___48-[WAAnalyticsAccess resetBackgroundRawAccessMOC]_block_invoke
+ ___48-[WADeviceAnalyticsClient isOmnipresentNetwork:]_block_invoke
+ ___48-[WADeviceAnalyticsClient neighborsForBSS:ssid:]_block_invoke
+ ___49-[WADeviceAnalyticsClient performPruneTestBSSes:]_block_invoke
+ ___51-[WADeviceAnalyticsClient copyLocationsForNetwork:]_block_invoke
+ ___52-[NeighborGraph copyNeighborGraphAsDictionaryOnMoc:]_block_invoke
+ ___52-[WADeviceAnalyticsClient autoLeaveRssiForBSS:ssid:]_block_invoke
+ ___52-[WADeviceAnalyticsClient copyAllStoredNetworkSsids]_block_invoke
+ ___52-[WADeviceAnalyticsClient dumpDeviceAnalyticsToFile]_block_invoke
+ ___52-[WADeviceAnalyticsClient dumpDeviceAnalyticsToFile]_block_invoke_2
+ ___52-[WADeviceAnalyticsClient dumpDeviceAnalyticsToFile]_block_invoke_3
+ ___52-[WADeviceAnalyticsClient dumpDeviceAnalyticsToFile]_block_invoke_4
+ ___52-[WADeviceAnalyticsClient dumpDeviceAnalyticsToFile]_block_invoke_5
+ ___52-[WADeviceAnalyticsClient resetBackgroundReadingMOC]_block_invoke
+ ___53-[WADeviceAnalyticsClient apProfileForBssid:andSSID:]_block_invoke
+ ___54+[WADeviceAnalyticsClient sharedDeviceAnalyticsClient]_block_invoke
+ ___54-[WADeviceAnalyticsClient copyNetworkUsageDictionary:]_block_invoke
+ ___54-[WADeviceAnalyticsClient countForFetchRequest:error:]_block_invoke
+ ___54-[WADeviceAnalyticsClient dumpDeploymentGraphJSONFile]_block_invoke
+ ___54-[WADeviceAnalyticsClient dumpDeploymentGraphJSONFile]_block_invoke_2
+ ___54-[WADeviceAnalyticsClient dumpDeploymentGraphJSONFile]_block_invoke_3
+ ___54-[WADeviceAnalyticsClient dumpDeploymentGraphJSONFile]_block_invoke_4
+ ___54-[WADeviceAnalyticsClient dumpDeploymentGraphJSONFile]_block_invoke_5
+ ___54-[WADeviceAnalyticsClient releaseBackgroundReadingMOC]_block_invoke
+ ___54-[WADeviceAnalyticsClient resetBackgroundRawAccessMOC]_block_invoke
+ ___54-[WADeviceAnalyticsClient rssiRoamTriggerForBSS:ssid:]_block_invoke
+ ___55-[WADeviceAnalyticsClient copyColocatedScopeIdForSsid:]_block_invoke
+ ___55-[WADeviceAnalyticsClient manualLeaveCountForBss:ssid:]_block_invoke
+ ___55-[WADeviceAnalyticsClient neighborChannelsForBSS:ssid:]_block_invoke
+ ___56-[WADeviceAnalyticsClient releaseBackgroundRawAccessMOC]_block_invoke
+ ___57-[WADeviceAnalyticsClient parsedBeaconInfoIsStored:ssid:]_block_invoke
+ ___57-[WADeviceAnalyticsClient releaseBackgroundProcessingMOC]_block_invoke
+ ___58-[AnalyticsProcessor processWAMessageMetric:data:andSave:]_block_invoke
+ ___58-[AnalyticsProcessor processWAMessageMetric:data:andSave:]_block_invoke_10
+ ___58-[AnalyticsProcessor processWAMessageMetric:data:andSave:]_block_invoke_11
+ ___58-[AnalyticsProcessor processWAMessageMetric:data:andSave:]_block_invoke_12
+ ___58-[AnalyticsProcessor processWAMessageMetric:data:andSave:]_block_invoke_13
+ ___58-[AnalyticsProcessor processWAMessageMetric:data:andSave:]_block_invoke_14
+ ___58-[AnalyticsProcessor processWAMessageMetric:data:andSave:]_block_invoke_2
+ ___58-[AnalyticsProcessor processWAMessageMetric:data:andSave:]_block_invoke_3
+ ___58-[AnalyticsProcessor processWAMessageMetric:data:andSave:]_block_invoke_4
+ ___58-[AnalyticsProcessor processWAMessageMetric:data:andSave:]_block_invoke_5
+ ___58-[AnalyticsProcessor processWAMessageMetric:data:andSave:]_block_invoke_6
+ ___58-[AnalyticsProcessor processWAMessageMetric:data:andSave:]_block_invoke_7
+ ___58-[AnalyticsProcessor processWAMessageMetric:data:andSave:]_block_invoke_8
+ ___58-[AnalyticsProcessor processWAMessageMetric:data:andSave:]_block_invoke_9
+ ___58-[WADeviceAnalyticsClient copyGeoTagsForNetwork:location:]_block_invoke
+ ___58-[WADeviceAnalyticsClient releaseBackgroundFileWritingMOC]_block_invoke
+ ___62-[AnalyticsStoreMOHandler performPruneBasedOnStoreSizeAndSave]_block_invoke
+ ___62-[WADeviceAnalyticsClient copyAllStoredNetworkSsidsWithTrait:]_block_invoke
+ ___62-[WADeviceAnalyticsClient performPruneBasedOnStoreSizeAndSave]_block_invoke
+ ___62-[WADeviceAnalyticsClient saveAndResetBackgroundProcessingMOC]_block_invoke
+ ___63-[WAAnalyticsAccess _performFetchWithBlockAndWait:error:onMoc:]_block_invoke
+ ___63-[WADeviceAnalyticsClient isHistoricallyBadLinkQualityNetwork:]_block_invoke
+ ___64+[AnalyticsProcessor analyticsProcessorWithPersistentContainer:]_block_invoke
+ ___64-[WADeviceAnalyticsClient processDatapathMetricStream:withDate:]_block_invoke
+ ___67-[WADeviceAnalyticsClient copyPreferenceScoreDictionaryForNetwork:]_block_invoke
+ ___70+[AnalyticsStoreMOHandler sharedAnalyticsStoreMOHandlerWithContainer:]_block_invoke
+ ___71-[WAAnalyticsAccess _countForFetchRequestWithBlockAndWait:error:onMoc:]_block_invoke
+ ___73-[WADeviceAnalyticsClient copyAllStoredNetworkSsidsWithColocatedScopeId:]_block_invoke
+ ___73-[WADeviceAnalyticsClient isNetworkWithinRangeOfLocation:range:location:]_block_invoke
+ ___74-[WADeviceAnalyticsClient dumpDeviceAnalyticsToFileWithFetchLimit:maxAge:]_block_invoke
+ ___74-[WADeviceAnalyticsClient dumpDeviceAnalyticsToFileWithFetchLimit:maxAge:]_block_invoke_2
+ ___74-[WADeviceAnalyticsClient dumpDeviceAnalyticsToFileWithFetchLimit:maxAge:]_block_invoke_3
+ ___74-[WADeviceAnalyticsClient dumpDeviceAnalyticsToFileWithFetchLimit:maxAge:]_block_invoke_4
+ ___74-[WADeviceAnalyticsClient processWAMessageMetric:data:andDeferSaveToDisk:]_block_invoke
+ ___77-[WADeviceAnalyticsClient dumpDeviceAnalyticsCSVsToFileWithBatchSize:maxAge:]_block_invoke
+ ___77-[WADeviceAnalyticsClient dumpDeviceAnalyticsCSVsToFileWithBatchSize:maxAge:]_block_invoke_2
+ ___77-[WADeviceAnalyticsClient dumpDeviceAnalyticsCSVsToFileWithBatchSize:maxAge:]_block_invoke_3
+ ___77-[WADeviceAnalyticsClient dumpDeviceAnalyticsCSVsToFileWithBatchSize:maxAge:]_block_invoke_4
+ ___77-[WADeviceAnalyticsClient dumpDeviceAnalyticsCSVsToFileWithBatchSize:maxAge:]_block_invoke_5
+ ___85-[AnalyticsProcessor updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:]_block_invoke
+ ___87-[WADeviceAnalyticsClient copyColocatedScopeTransitionInfo:bssid:minRssi:maxRssi:band:]_block_invoke
+ ___87-[WADeviceAnalyticsClient dumpDeviceAnalyticsUsingBatchSizeToFileWithBatchSize:maxAge:]_block_invoke
+ ___87-[WADeviceAnalyticsClient dumpDeviceAnalyticsUsingBatchSizeToFileWithBatchSize:maxAge:]_block_invoke_2
+ ___87-[WADeviceAnalyticsClient dumpDeviceAnalyticsUsingBatchSizeToFileWithBatchSize:maxAge:]_block_invoke_3
+ ___87-[WADeviceAnalyticsClient dumpDeviceAnalyticsUsingBatchSizeToFileWithBatchSize:maxAge:]_block_invoke_4
+ ___87-[WADeviceAnalyticsClient dumpDeviceAnalyticsUsingBatchSizeToFileWithBatchSize:maxAge:]_block_invoke_5
+ ___90-[WADeviceAnalyticsClient updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:]_block_invoke
+ ___91-[WAXPCConnection updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:andReply:]_block_invoke
+ ___93-[WADeviceAnalyticsClient copyNetworksAvailableAtLocationWithinDistanceInBand:distance:band:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e5_v8?0l
+ ___block_descriptor_40_e8_32r_e18_v16?0"NSString"8l
+ ___block_descriptor_40_e8_32s_e50_v24?0"NSPersistentStoreDescription"8"NSError"16l
+ ___block_descriptor_48_e8_32s_e5_v8?0l
+ ___block_descriptor_57_e8_32s40s48s_e5_v8?0l
+ ___block_descriptor_64_e8_32s40s48r_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48bs56r_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48r56r_e15_v32?08Q16^B24l
+ ___block_descriptor_72_e8_32s40s48s56r_e15_v32?08Q16^B24l
+ ___block_descriptor_72_e8_32s40s48s56r_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48b56r
+ __block_literal_global.144
+ __block_literal_global.151
+ __block_literal_global.156
+ __block_literal_global.161
+ __block_literal_global.166
+ __block_literal_global.177
+ __block_literal_global.226
+ __block_literal_global.230
+ __block_literal_global.234
+ __block_literal_global.240
+ __block_literal_global.244
+ __block_literal_global.249
+ __block_literal_global.253
+ __block_literal_global.258
+ __block_literal_global.263
+ _dispatch_queue_get_label
+ _objc_msgSend$URLWithString:
+ _objc_msgSend$_countForFetchRequest:error:onMoc:
+ _objc_msgSend$_countForFetchRequestWithBlockAndWait:error:onMoc:
+ _objc_msgSend$_performFetch:error:onMoc:
+ _objc_msgSend$_performFetchWithBlockAndWait:error:onMoc:
+ _objc_msgSend$accessWithPersistentContainer:
+ _objc_msgSend$addPersistentStoreRemoteChangeNotificationObserver:selector:coordinator:
+ _objc_msgSend$ageOutAnalytics:
+ _objc_msgSend$analyticsFileWriterObj
+ _objc_msgSend$analyticsProcessor
+ _objc_msgSend$analyticsProcessorObj
+ _objc_msgSend$analyticsProcessorWithPersistentContainer:
+ _objc_msgSend$analyticsRawAccess
+ _objc_msgSend$analyticsRawAccessObj
+ _objc_msgSend$analyticsReaderObj
+ _objc_msgSend$apProfileForBssid:andSSID:
+ _objc_msgSend$backgroundFileWritingMOC
+ _objc_msgSend$backgroundRawAccessMOC
+ _objc_msgSend$backgroundStoreMoHandlerMOC
+ _objc_msgSend$copyNeighborGraphAsDictionaryOnMoc:
+ _objc_msgSend$countForFetchRequestWithBlockAndWait:error:
+ _objc_msgSend$customMigrationOnProcess
+ _objc_msgSend$customXPCStoreOnProcess
+ _objc_msgSend$defaultModelName
+ _objc_msgSend$domain
+ _objc_msgSend$entitiesByName
+ _objc_msgSend$exportedRemoteInterface
+ _objc_msgSend$getLazyNSStringPreference:domain:exists:
+ _objc_msgSend$getPolicyHandlersConfig
+ _objc_msgSend$initPolicyHandlers
+ _objc_msgSend$initWithBssidArray:ssid:persistentContainer:
+ _objc_msgSend$initWithContainer:
+ _objc_msgSend$initWithOptions:andContainer:
+ _objc_msgSend$initWithPersistentContainer:
+ _objc_msgSend$initWithStoreURL:modelURL:
+ _objc_msgSend$isWritingInAnalyticsStoreAllowed
+ _objc_msgSend$loadPersistentStoresWithCompletionHandler:
+ _objc_msgSend$loadStore
+ _objc_msgSend$loadStoreIfNeeded
+ _objc_msgSend$moc
+ _objc_msgSend$mom
+ _objc_msgSend$newBackgroundContext
+ _objc_msgSend$numRoamSamples
+ _objc_msgSend$optionDescription:
+ _objc_msgSend$performFetchWithBlockAndWait:error:
+ _objc_msgSend$performPruneTestBSSes:
+ _objc_msgSend$persistentContainer
+ _objc_msgSend$persistentContainerWithName:managedObjectModel:
+ _objc_msgSend$processDatapathMetricStream:withDate:
+ _objc_msgSend$processWAMessageMetric:data:andDeferSaveToDisk:
+ _objc_msgSend$processWAMessageMetric:data:andSave:
+ _objc_msgSend$releaseBackgroundFileWritingMOC
+ _objc_msgSend$releaseBackgroundProcessingMOC
+ _objc_msgSend$releaseBackgroundRawAccessMOC
+ _objc_msgSend$releaseBackgroundReadingMOC
+ _objc_msgSend$releaseBackgroundStoreMoHandlerMOC
+ _objc_msgSend$removeObserver:name:object:
+ _objc_msgSend$removePersistentStoreRemoteChangeNotificationObserver:coordinator:
+ _objc_msgSend$resetBackgroundRawAccessMOC
+ _objc_msgSend$resetBackgroundReadingMOC
+ _objc_msgSend$saveAndResetManagedObjectContext
+ _objc_msgSend$setBackgroundFileWritingMOC:
+ _objc_msgSend$setBackgroundRawAccessMOC:
+ _objc_msgSend$setBackgroundReadingMOC:
+ _objc_msgSend$setBackgroundStoreMoHandlerMOC:
+ _objc_msgSend$setBss:
+ _objc_msgSend$setDeploymentMetricDiffDays:
+ _objc_msgSend$setExportedRemoteInterface:
+ _objc_msgSend$setFutureApfsPurgeableDeadline:forURL:
+ _objc_msgSend$setNumRoamSamples:
+ _objc_msgSend$setPersistentStoreDescriptions:
+ _objc_msgSend$setPolicyHandlersConfig:
+ _objc_msgSend$setTestDateDiffDays:
+ _objc_msgSend$sharedAnalyticsStoreMOHandlerWithContainer:
+ _objc_msgSend$shouldMigrateStoreAutomatically
+ _objc_msgSend$updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:
+ _objc_msgSend$updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:andReply:
+ _objc_msgSend$updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:andReply:queuedInvocation:
+ _objc_msgSend$viewContext
+ _objc_msgSend$writeData:toFile:
+ _objc_msgSend$writeObj:toJSONFile:
+ _objc_msgSend$xpcConnection:updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:andReply:
+ _sqrt
+ _strcmp
- +[AnalyticsPersistenceManager isStoreCompatibleAtURL:withModel:]
- +[AnalyticsPersistenceManager sharedWAPersistenceCoordinatorWithMOM:]
- +[AnalyticsProcessor sharedAnalyticsProcessor]
- +[AnalyticsStoreDescriptor directStoreDescriptor]
- +[AnalyticsStoreDescriptor serverStoreDescriptor:]
- +[AnalyticsStoreMOContext sharedManagedObjectModel:]
- +[AnalyticsStoreMOHandler isStoreCompatible]
- +[AnalyticsStoreMOHandler sharedAnalyticsStoreMOHandlerWithPersist]
- +[WAAnalyticsAccess accessWithOptions:]
- +[WAAnalyticsAccess sharedWAAnalyticsAccess]
- +[WADeviceAnalyticsClient sharedDeviceAnalyticsClientWithPersist]
- +[WAUtil isAnalyticsProcessorAllowed]
- +[WAUtil shouldEnableXPCStore]
- -[AnalyticsPersistenceManager .cxx_destruct]
- -[AnalyticsPersistenceManager initWithManagedObjectModel:storeDescriptor:]
- -[AnalyticsPersistenceManager managedObjectModel]
- -[AnalyticsPersistenceManager persistenceCoordinator]
- -[AnalyticsPersistenceManager setXpcStoreServer:]
- -[AnalyticsPersistenceManager xpcStoreServer]
- -[AnalyticsProcessor apProfileForBssid:andSSID:]
- -[AnalyticsProcessor initCommmonObjects]
- -[AnalyticsProcessor initWithOptions:]
- -[AnalyticsProcessor initWithOptions:byoMOC:]
- -[AnalyticsProcessor processWAMessageMetric:data:]
- -[AnalyticsProcessor summarizeAnalyticsForNetwork:maxAgeInDays:]
- -[AnalyticsReader initWithAnalyticsStore:]
- -[AnalyticsReader managedObjectHandler]
- -[AnalyticsReader setManagedObjectHandler:]
- -[AnalyticsStoreDescriptor initWithType:storeURL:modelURL:options:]
- -[AnalyticsStoreDescriptor setType:]
- -[AnalyticsStoreDescriptor type]
- -[AnalyticsStoreFileWriter analyticsStoreFileWriterDirectory]
- -[AnalyticsStoreFileWriter initWithAnalyticsStore:]
- -[AnalyticsStoreFileWriter init]
- -[AnalyticsStoreFileWriter managedObjectHandler]
- -[AnalyticsStoreFileWriter setManagedObjectHandler:]
- -[AnalyticsStoreMOContext .cxx_destruct]
- -[AnalyticsStoreMOContext initWithStoreDescriptor:]
- -[AnalyticsStoreMOContext managedObjectModel]
- -[AnalyticsStoreMOContext persistenceManager]
- -[AnalyticsStoreMOContext setPersistenceManager:]
- -[AnalyticsStoreMOContext setSharedManagedObjectModel:]
- -[AnalyticsStoreMOContext setStoreDescriptor:]
- -[AnalyticsStoreMOContext sharedManagedObjectModel]
- -[AnalyticsStoreMOContext storeDescriptor]
- -[AnalyticsStoreMOContext storeNeedsImmediatePruning:]
- -[AnalyticsStoreMOHandler initWithContext:]
- -[AnalyticsStoreMOHandler initWithType:options:]
- -[AnalyticsStoreMOHandler persistenceManager]
- -[AnalyticsStoreMOHandler setManagedObjectContext:]
- -[AnalyticsStoreMOHandler setPersistenceManager:]
- -[AnalyticsStoreMOHandler setStoreMOContext:]
- -[AnalyticsStoreMOHandler setStoreType:]
- -[AnalyticsStoreMOHandler storeMOContext]
- -[AnalyticsStoreMOHandler storeType]
- -[AnalyticsStoreRemoteServerHandlingPolicy shouldAcceptConnectionsFromClientWithContext:]
- -[NeighborGraph copyNeighborGraphAsDictionary]
- -[NeighborGraph initWithBssidArray:ssid:handler:]
- -[NeighborGraph managedObjectHandler]
- -[NeighborGraph setManagedObjectHandler:]
- -[WAAnalyticsAccess copyWithZone:]
- -[WAAnalyticsAccess initWithOptions:]
- -[WAAnalyticsAccess moHandler]
- -[WAAnalyticsAccess persistentStoreError]
- -[WAAnalyticsAccess reset]
- -[WAAnalyticsAccess save]
- -[WAAnalyticsAccess setMoHandler:]
- -[WAAnalyticsAccess setPersistentStoreError:]
- -[WAAnalyticsAccess storeMOContext]
- -[WAClient summarizeDeviceAnalyticsForNetwork:maxAgeInDays:andReply:]
- -[WAClient summarizeDeviceAnalyticsForNetwork:maxAgeInDays:andReply:queuedInvocation:]
- -[WADeviceAnalyticsClient initCommon]
- -[WADeviceAnalyticsClient initWithSharedServerType]
- -[WADeviceAnalyticsClient managedObjectHandler]
- -[WADeviceAnalyticsClient setManagedObjectHandler:]
- -[WAXPCConnection summarizeDeviceAnalyticsForNetwork:maxAgeInDays:andReply:]
- GCC_except_table16
- GCC_except_table28
- GCC_except_table36
- GCC_except_table38
- GCC_except_table52
- GCC_except_table56
- GCC_except_table6
- OBJC_IVAR_$_AnalyticsPersistenceManager._managedObjectModel
- OBJC_IVAR_$_AnalyticsPersistenceManager._persistenceCoordinator
- OBJC_IVAR_$_AnalyticsPersistenceManager._xpcStoreServer
- OBJC_IVAR_$_AnalyticsReader._managedObjectHandler
- OBJC_IVAR_$_AnalyticsStoreDescriptor._type
- OBJC_IVAR_$_AnalyticsStoreFileWriter._managedObjectHandler
- OBJC_IVAR_$_AnalyticsStoreMOContext._managedObjectModel
- OBJC_IVAR_$_AnalyticsStoreMOContext._persistenceManager
- OBJC_IVAR_$_AnalyticsStoreMOContext._sharedManagedObjectModel
- OBJC_IVAR_$_AnalyticsStoreMOContext._storeDescriptor
- OBJC_IVAR_$_AnalyticsStoreMOHandler.__managedObjectContext
- OBJC_IVAR_$_AnalyticsStoreMOHandler._persistenceManager
- OBJC_IVAR_$_AnalyticsStoreMOHandler._storeMOContext
- OBJC_IVAR_$_AnalyticsStoreMOHandler._storeType
- OBJC_IVAR_$_NeighborGraph._managedObjectHandler
- OBJC_IVAR_$_WAAnalyticsAccess.__moHandler
- OBJC_IVAR_$_WAAnalyticsAccess.__persistentStoreCoordinator
- OBJC_IVAR_$_WAAnalyticsAccess.__storeMOContext
- OBJC_IVAR_$_WAAnalyticsAccess._persistentStoreError
- OBJC_IVAR_$_WADeviceAnalyticsClient._managedObjectHandler
- _NSManagedObjectContextDidSaveNotification
- _NSPersistentStoreConnectionPoolMaxSizeKey
- _OBJC_CLASS_$_AnalyticsPersistenceManager
- _OBJC_CLASS_$_AnalyticsStoreMOContext
- _OBJC_CLASS_$_AnalyticsStoreRemoteServerHandlingPolicy
- _OBJC_CLASS_$_NSManagedObjectContext
- _OBJC_CLASS_$_NSMergePolicy
- _OBJC_CLASS_$_NSPersistentStoreCoordinator
- _OBJC_CLASS_$_NSXPCStoreServer
- _OBJC_CLASS_$_NSXPCStoreServerRequestHandlingPolicy
- _OBJC_METACLASS_$_AnalyticsPersistenceManager
- _OBJC_METACLASS_$_AnalyticsStoreMOContext
- _OBJC_METACLASS_$_AnalyticsStoreRemoteServerHandlingPolicy
- _OBJC_METACLASS_$_NSXPCStoreServerRequestHandlingPolicy
- __100-[AnalyticsReader copyScoreSortedNetworksAvailableAtLocationWithinDistance:distance:authComparator:]_block_invoke.75
- __100-[AnalyticsReader copyScoreSortedNetworksAvailableAtLocationWithinDistance:distance:authComparator:]_block_invoke.78
- __100-[AnalyticsReader copyScoreSortedNetworksAvailableAtLocationWithinDistance:distance:authComparator:]_block_invoke.83
- __38-[WAClient _establishDaemonConnection]_block_invoke.199
- __38-[WAClient _establishDaemonConnection]_block_invoke.203
- __38-[WAClient _establishDaemonConnection]_block_invoke.204
- __38-[WAClient _establishDaemonConnection]_block_invoke_2.200
- __38-[WAClient _establishDaemonConnection]_block_invoke_2.202
- __46-[NeighborGraph copyNeighborGraphAsDictionary]_block_invoke.80
- __46-[WAClient _replyAllWithTimeoutErrorAndRemove]_block_invoke.226
- __49-[WAClient _killDaemonAndReply:queuedInvocation:]_block_invoke.174
- __49-[WAClient _killDaemonAndReply:queuedInvocation:]_block_invoke.175
- __50-[AnalyticsProcessor processWAMessageMetric:data:]_block_invoke.74
- __50-[WAClient _getDpsStatsandReply:queuedInvocation:]_block_invoke.170
- __50-[WAClient _getDpsStatsandReply:queuedInvocation:]_block_invoke.171
- __52-[WAClient _getUsageStatsandReply:queuedInvocation:]_block_invoke.267
- __52-[WAClient _getUsageStatsandReply:queuedInvocation:]_block_invoke.268
- __54-[AnalyticsStoreFileWriter writeDeploymentGraphToFile]_block_invoke.72
- __56-[WAClient _clearMessageStoreAndReply:queuedInvocation:]_block_invoke.176
- __56-[WAClient _clearMessageStoreAndReply:queuedInvocation:]_block_invoke.177
- __64-[WAClient _sendMemoryPressureRequestAndReply:queuedInvocation:]_block_invoke.182
- __64-[WAClient _sendMemoryPressureRequestAndReply:queuedInvocation:]_block_invoke.183
- __65-[WAClient _triggerQueryForNWActivity:andReply:queuedInvocation:]_block_invoke.155
- __65-[WAClient _triggerQueryForNWActivity:andReply:queuedInvocation:]_block_invoke.156
- __68-[WAClient _getMessagesModelForGroupType:andReply:queuedInvocation:]_block_invoke.181
- __70-[WAClient _getDeviceAnalyticsConfigurationAndReply:queuedInvocation:]_block_invoke.248
- __70-[WAClient _getDeviceAnalyticsConfigurationAndReply:queuedInvocation:]_block_invoke.249
- __70-[WAClient _issueIOReportManagementCommand:andReply:queuedInvocation:]_block_invoke.262
- __70-[WAClient _issueIOReportManagementCommand:andReply:queuedInvocation:]_block_invoke.263
- __71-[WAClient _setDeviceAnalyticsConfiguration:andReply:queuedInvocation:]_block_invoke.244
- __74-[WAClient _submitWiFiAnalyticsMessageAdvanced:andReply:queuedInvocation:]_block_invoke.144
- __74-[WAClient _submitWiFiAnalyticsMessageAdvanced:andReply:queuedInvocation:]_block_invoke.148
- __74-[WAClient _submitWiFiAnalyticsMessageAdvanced:andReply:queuedInvocation:]_block_invoke_2.149
- __75-[WAClient _triggerDeviceAnalyticsStoreMigrationAndReply:queuedInvocation:]_block_invoke.257
- __75-[WAClient _triggerDeviceAnalyticsStoreMigrationAndReply:queuedInvocation:]_block_invoke.258
- __80-[WAClient _lqmCrashTracerNotifyForInterfaceWithName:andReply:queuedInvocation:]_block_invoke.234
- __86-[WAClient summarizeDeviceAnalyticsForNetwork:maxAgeInDays:andReply:queuedInvocation:]_block_invoke.250
- __86-[WAClient summarizeDeviceAnalyticsForNetwork:maxAgeInDays:andReply:queuedInvocation:]_block_invoke.253
- __87-[WAClient _lqmCrashTracerReceiveBlock:forInterfaceWithName:andReply:queuedInvocation:]_block_invoke.238
- __88-[WAClient _trapCrashMiniTracerDumpReadyForInterfaceWithName:andReply:queuedInvocation:]_block_invoke.230
- __93-[WAClient _triggerDatapathDiagnosticsAndCollectUpdates:waMessage:andReply:queuedInvocation:]_block_invoke.165
- __93-[WAClient _triggerDatapathDiagnosticsAndCollectUpdates:waMessage:andReply:queuedInvocation:]_block_invoke.166
- __95-[WAClient convertWiFiStatsIntoPercentile:analysisGroup:groupTarget:andReply:queuedInvocation:]_block_invoke.160
- __95-[WAClient convertWiFiStatsIntoPercentile:analysisGroup:groupTarget:andReply:queuedInvocation:]_block_invoke.161
- __Block_byref_object_copy_.60
- __Block_byref_object_dispose_.61
- __OBJC_$_CLASS_METHODS_AnalyticsPersistenceManager
- __OBJC_$_CLASS_METHODS_AnalyticsStoreMOContext
- __OBJC_$_INSTANCE_METHODS_AnalyticsPersistenceManager
- __OBJC_$_INSTANCE_METHODS_AnalyticsStoreMOContext
- __OBJC_$_INSTANCE_METHODS_AnalyticsStoreRemoteServerHandlingPolicy
- __OBJC_$_INSTANCE_VARIABLES_AnalyticsPersistenceManager
- __OBJC_$_INSTANCE_VARIABLES_AnalyticsStoreMOContext
- __OBJC_$_PROP_LIST_AnalyticsPersistenceManager
- __OBJC_$_PROP_LIST_AnalyticsStoreMOContext
- __OBJC_CLASS_PROTOCOLS_$_WAAnalyticsAccess
- __OBJC_CLASS_RO_$_AnalyticsPersistenceManager
- __OBJC_CLASS_RO_$_AnalyticsStoreMOContext
- __OBJC_CLASS_RO_$_AnalyticsStoreRemoteServerHandlingPolicy
- __OBJC_METACLASS_RO_$_AnalyticsPersistenceManager
- __OBJC_METACLASS_RO_$_AnalyticsStoreMOContext
- __OBJC_METACLASS_RO_$_AnalyticsStoreRemoteServerHandlingPolicy
- ___30+[WAUtil shouldEnableXPCStore]_block_invoke
- ___44+[WAAnalyticsAccess sharedWAAnalyticsAccess]_block_invoke
- ___46+[AnalyticsProcessor sharedAnalyticsProcessor]_block_invoke
- ___46-[NeighborGraph copyNeighborGraphAsDictionary]_block_invoke
- ___48-[AnalyticsProcessor apProfileForBssid:andSSID:]_block_invoke
- ___50-[AnalyticsProcessor processWAMessageMetric:data:]_block_invoke
- ___50-[AnalyticsProcessor processWAMessageMetric:data:]_block_invoke_10
- ___50-[AnalyticsProcessor processWAMessageMetric:data:]_block_invoke_11
- ___50-[AnalyticsProcessor processWAMessageMetric:data:]_block_invoke_12
- ___50-[AnalyticsProcessor processWAMessageMetric:data:]_block_invoke_13
- ___50-[AnalyticsProcessor processWAMessageMetric:data:]_block_invoke_14
- ___50-[AnalyticsProcessor processWAMessageMetric:data:]_block_invoke_2
- ___50-[AnalyticsProcessor processWAMessageMetric:data:]_block_invoke_3
- ___50-[AnalyticsProcessor processWAMessageMetric:data:]_block_invoke_4
- ___50-[AnalyticsProcessor processWAMessageMetric:data:]_block_invoke_5
- ___50-[AnalyticsProcessor processWAMessageMetric:data:]_block_invoke_6
- ___50-[AnalyticsProcessor processWAMessageMetric:data:]_block_invoke_7
- ___50-[AnalyticsProcessor processWAMessageMetric:data:]_block_invoke_8
- ___50-[AnalyticsProcessor processWAMessageMetric:data:]_block_invoke_9
- ___52+[AnalyticsStoreMOContext sharedManagedObjectModel:]_block_invoke
- ___64+[AnalyticsPersistenceManager isStoreCompatibleAtURL:withModel:]_block_invoke
- ___64-[AnalyticsProcessor summarizeAnalyticsForNetwork:maxAgeInDays:]_block_invoke
- ___65+[WADeviceAnalyticsClient sharedDeviceAnalyticsClientWithPersist]_block_invoke
- ___67+[AnalyticsStoreMOHandler sharedAnalyticsStoreMOHandlerWithPersist]_block_invoke
- ___67-[AnalyticsStoreDescriptor initWithType:storeURL:modelURL:options:]_block_invoke
- ___69+[AnalyticsPersistenceManager sharedWAPersistenceCoordinatorWithMOM:]_block_invoke
- ___74-[AnalyticsPersistenceManager initWithManagedObjectModel:storeDescriptor:]_block_invoke
- ___76-[WAXPCConnection summarizeDeviceAnalyticsForNetwork:maxAgeInDays:andReply:]_block_invoke
- ___86-[WAClient summarizeDeviceAnalyticsForNetwork:maxAgeInDays:andReply:queuedInvocation:]_block_invoke
- ___86-[WAClient summarizeDeviceAnalyticsForNetwork:maxAgeInDays:andReply:queuedInvocation:]_block_invoke_2
- ___block_descriptor_40_e8_32r_e50_v24?0"NSPersistentStoreDescription"8"NSError"16l
- ___block_descriptor_40_e8_32s_e18_v16?0"NSNumber"8l
- ___block_descriptor_64_e8_32s40r48r_e15_v32?08Q16^B24l
- ___block_descriptor_64_e8_32s40s48r_e15_v32?08Q16^B24l
- __block_literal_global.147
- __block_literal_global.154
- __block_literal_global.159
- __block_literal_global.164
- __block_literal_global.169
- __block_literal_global.180
- __block_literal_global.229
- __block_literal_global.233
- __block_literal_global.237
- __block_literal_global.243
- __block_literal_global.247
- __block_literal_global.252
- __block_literal_global.256
- __block_literal_global.261
- __block_literal_global.266
- _fmod
- _fmodf
- _kBSSIDOctetCount
- _kOUIOctetCount
- _objc_msgSend$addFaultsObject:
- _objc_msgSend$addPersistentStoreWithDescription:completionHandler:
- _objc_msgSend$analyticsStoreOptions
- _objc_msgSend$checkResourceIsReachableAndReturnError:
- _objc_msgSend$copyNeighborGraphAsDictionary
- _objc_msgSend$directStoreDescriptor
- _objc_msgSend$initCommmonObjects
- _objc_msgSend$initCommon
- _objc_msgSend$initForStoreWithURL:usingModelAtURL:options:policy:
- _objc_msgSend$initWithBssidArray:ssid:handler:
- _objc_msgSend$initWithConcurrencyType:
- _objc_msgSend$initWithManagedObjectModel:
- _objc_msgSend$initWithManagedObjectModel:storeDescriptor:
- _objc_msgSend$initWithOptions:
- _objc_msgSend$initWithSharedServerType
- _objc_msgSend$initWithStoreDescriptor:
- _objc_msgSend$initWithType:options:
- _objc_msgSend$initWithType:storeURL:modelURL:options:
- _objc_msgSend$isAnalyticsProcessorAllowed
- _objc_msgSend$isConfiguration:compatibleWithStoreMetadata:
- _objc_msgSend$isStoreCompatible
- _objc_msgSend$isStoreCompatibleAtURL:withModel:
- _objc_msgSend$mergeByPropertyObjectTrumpMergePolicy
- _objc_msgSend$metadataForPersistentStoreOfType:URL:options:error:
- _objc_msgSend$modelURL
- _objc_msgSend$persistenceCoordinator
- _objc_msgSend$persistenceManager
- _objc_msgSend$remoteStoreOptions
- _objc_msgSend$serverStoreDescriptor:
- _objc_msgSend$setPersistentStoreCoordinator:
- _objc_msgSend$setTransactionAuthor:
- _objc_msgSend$sharedAnalyticsStoreMOHandlerWithPersist
- _objc_msgSend$sharedManagedObjectModel:
- _objc_msgSend$sharedWAPersistenceCoordinatorWithMOM:
- _objc_msgSend$startListening
- _objc_msgSend$storeMOContext
- _objc_msgSend$summarizeDeviceAnalyticsForNetwork:maxAgeInDays:andReply:
- _objc_msgSend$summarizeDeviceAnalyticsForNetwork:maxAgeInDays:andReply:queuedInvocation:
- _objc_msgSend$xpcConnection:summarizeDeviceAnalyticsForNetwork:maxAgeInDays:andReply:
- _symbolic SS3key_yp5valuetSg
- _symbolic Si6offset_yp7elementtSg
CStrings:
+ "\nmodelURL: %@\nstoreURL:%@\noptions:%@\nstoreDescription:%@"
+ "%{public}s::%d:%s: OVERRIDING %@ to %@"
+ "%{public}s::%d:Adding %@ as observer of NSPersistentStoreRemoteChangeNotification from %@"
+ "%{public}s::%d:AnalyticsStoreMOHandler failed to init"
+ "%{public}s::%d:Dumping %@ entities to %@"
+ "%{public}s::%d:Error creating policy handlers"
+ "%{public}s::%d:Error getting sharedAnalyticsStoreMOHandler"
+ "%{public}s::%d:Error saving context %@: %@ %@"
+ "%{public}s::%d:Error with countForFetchRequest %@. %@ %@"
+ "%{public}s::%d:Error with executeFetchRequest %@. %@ %@"
+ "%{public}s::%d:Initializing WAAnalyticsAccess with option %@"
+ "%{public}s::%d:Invalid fetch request: %@ --> %@"
+ "%{public}s::%d:Nil - invalid geoTag coordinates or geoTag.date %@"
+ "%{public}s::%d:OVERRIDING %@ from %d MB to %lu KB"
+ "%{public}s::%d:Removing %@ as observer of NSPersistentStoreRemoteChangeNotification from %@"
+ "%{public}s::%d:Roam Samples %lu "
+ "%{public}s::%d:Saved context %@"
+ "%{public}s::%d:The store needs migration. Wait for the process in charge of migration to migrate the store"
+ "%{public}s::%d:Unable to create BG MOC"
+ "%{public}s::%d:Unable to create directory at %@: %@"
+ "%{public}s::%d:Unable to get a PersistentContainer for model name: %@ (%@)"
+ "%{public}s::%d:Unable to get model url (%@ - %@) or AnalyticsStoreDescriptor (%@)"
+ "%{public}s::%d:Unable to initialize WADeviceAnalyticsClient"
+ "%{public}s::%d:Unable to instantiate AnalyticsStoreFileWriter"
+ "%{public}s::%d:Unable to load persistent store:%@ error:%@"
+ "%{public}s::%d:Unable to load store. Error available in storeLoadError"
+ "%{public}s::%d:Updated deploymentMetricDiffDays to %lu days"
+ "%{public}s::%d:Updated testDateDiffDays to %lu days"
+ "%{public}s::%d:Writing in the WiFi Analytics Store is disabled on this platform and this class should not be inited"
+ "%{public}s::%d:XPC: WAClient - error: %@"
+ "%{public}s::%d:_analyticsRawAccessObj nil"
+ "%{public}s::%d:_establishDaemonConnection is called with existing connection %@, invalidating and force close before re-establishing..."
+ "%{public}s::%d:apProfileID nil for bssid:%@ and SSID:%@"
+ "%{public}s::%d:applicationSupportDirectoryPath is nil"
+ "%{public}s::%d:bssMO not found for bssid:%@ and SSID:%@"
+ "%{public}s::%d:defaultPersistentStoreURL is nil with path %@"
+ "%{public}s::%d:entityName %@ doesn't (yet) exist"
+ "%{public}s::%d:failed to serialize JSON: %@"
+ "%{public}s::%d:nil PersistentContainer"
+ "%{public}s::%d:nil container - bailing"
+ "%{public}s::%d:persistent container nil"
+ "%{public}s::%d:processName:%@ setupXPCStore: %@ migrateIfNecessary: %@"
+ "%{public}s::%d:resultChannelList empty: %@"
+ "%{public}s::%d:ret: %@"
+ "%{public}s::%d:retrieving %lu entries from request.entityName %@"
+ "%{public}s::%d:store loaded and ready to use: %@"
+ "%{public}s::%d:unable to initialize AnalyticsProcessor"
+ "+[AnalyticsProcessor analyticsProcessorWithPersistentContainer:]"
+ "+[AnalyticsProcessor analyticsProcessorWithPersistentContainer:]_block_invoke"
+ "+[AnalyticsStoreDescriptor defaultPersistentStoreURL]_block_invoke"
+ "+[AnalyticsStoreFileWriter analyticsStoreFileWriterDirectory]"
+ "+[AnalyticsStoreFileWriter exportEntityToCSV:batchSize:maxAge:toURL:fileDate:dateFormatter:inManagedObjectContext:]"
+ "+[AnalyticsStoreFileWriter writeData:toFile:]"
+ "+[AnalyticsStoreFileWriter writeObj:toJSONFile:]"
+ "+[AnalyticsStoreMOHandler sharedAnalyticsStoreMOHandlerWithContainer:]"
+ "+[AnalyticsStoreProxy fetch:withPredicate:moc:]_block_invoke"
+ "+[NSPersistentContainer(WAPersistentContainer) storeNeedsImmediatePruning:]"
+ "+[RoamMO roamsCountBetweenBssids:target:moc:]"
+ "+[WAAnalyticsAccess accessWithPersistentContainer:]"
+ "+[WADeviceAnalyticsClient addPersistentStoreRemoteChangeNotificationObserver:selector:coordinator:]"
+ "+[WADeviceAnalyticsClient removePersistentStoreRemoteChangeNotificationObserver:coordinator:]"
+ "+[WADeviceAnalyticsClient sharedDeviceAnalyticsClient]"
+ "+[WADeviceAnalyticsClient sharedDeviceAnalyticsClient]_block_invoke"
+ "+[WAUtil customMigrationOnProcess]_block_invoke"
+ "+[WAUtil customXPCStoreOnProcess]_block_invoke"
+ "+[WAUtil isWritingInAnalyticsStoreAllowed]"
+ "+[WAUtil isWritingInAnalyticsStoreAllowed]_block_invoke"
+ "+[WAUtil setFutureApfsPurgeableDeadline:forURL:]"
+ "-[AnalyticsProcessor initPolicyHandlers]"
+ "-[AnalyticsProcessor initWithPersistentContainer:]"
+ "-[AnalyticsProcessor processWAMessageMetric:data:andSave:]"
+ "-[AnalyticsProcessor setPolicyHandlersConfig:]"
+ "-[AnalyticsProcessor updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:]"
+ "-[AnalyticsProcessor updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:]_block_invoke"
+ "-[AnalyticsReader apProfileForBssid:andSSID:]_block_invoke"
+ "-[AnalyticsReader backgroundReadingMOC]"
+ "-[AnalyticsReader initWithPersistentContainer:]"
+ "-[AnalyticsStoreDescriptor initWithStoreURL:modelURL:]"
+ "-[AnalyticsStoreFileWriter backgroundFileWritingMOC]"
+ "-[AnalyticsStoreFileWriter initWithPersistentContainer:]"
+ "-[AnalyticsStoreMOHandler backgroundStoreMoHandlerMOC]"
+ "-[AnalyticsStoreMOHandler performPruneBasedOnStoreSizeAndSave]_block_invoke"
+ "-[NeighborGraph copyNeighborGraphAsDictionaryOnMoc:]"
+ "-[NeighborGraph copyNeighborGraphAsDictionaryOnMoc:]_block_invoke"
+ "-[NeighborGraph initWithBssidArray:ssid:persistentContainer:]"
+ "-[WAAnalyticsAccess _countForFetchRequest:error:onMoc:]"
+ "-[WAAnalyticsAccess _performFetch:error:onMoc:]"
+ "-[WAAnalyticsAccess backgroundRawAccessMOC]"
+ "-[WAAnalyticsAccess mainObjectContext]"
+ "-[WAClient updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:andReply:queuedInvocation:]_block_invoke"
+ "-[WADeviceAnalyticsClient analyticsProcessor]"
+ "-[WADeviceAnalyticsClient analyticsRawAccess]"
+ "-[WADeviceAnalyticsClient dumpDeviceAnalyticsCSVsToFileWithBatchSize:maxAge:]"
+ "-[WADeviceAnalyticsClient dumpDeviceAnalyticsToFileWithCompletion:]"
+ "-[WADeviceAnalyticsClient dumpDeviceAnalyticsToFileWithFetchLimit:maxAge:]"
+ "-[WADeviceAnalyticsClient dumpDeviceAnalyticsUsingBatchSizeToFileWithBatchSize:maxAge:]"
+ "-[WADeviceAnalyticsClient init]_block_invoke"
+ "-[WADeviceAnalyticsClient loadStoreIfNeeded]"
+ "-[WADeviceAnalyticsClient loadStore]_block_invoke"
+ "-[WADeviceAnalyticsClient loadStore]_block_invoke_2"
+ "-[WADeviceAnalyticsClient processDatapathMetricStream:withDate:]"
+ "-[WADeviceAnalyticsClient processWAMessageMetric:data:andDeferSaveToDisk:]"
+ "-[WADeviceAnalyticsClient updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:]"
+ "@\"AnalyticsProcessor\""
+ "@\"NSPersistentContainer\""
+ "@\"NSXPCInterface\""
+ "@\"WAAnalyticsAccess\""
+ "@40@0:8@16^@24@32"
+ "AllowMigration "
+ "AnalyticsProcessor init"
+ "AnalyticsProcessor processWAMessageMetric saveMoc"
+ "B32@0:8Q16@24"
+ "FAILURE"
+ "NONE"
+ "Q32@0:8@16^@24"
+ "Q40@0:8@16^@24@32"
+ "SUCCESS"
+ "SetupXPCStore "
+ "T@\"AnalyticsProcessor\",&,N,V_analyticsProcessorObj"
+ "T@\"NSError\",&,V_storeLoadError"
+ "T@\"NSManagedObjectContext\",&,N,V_backgroundFileWritingMOC"
+ "T@\"NSManagedObjectContext\",&,N,V_backgroundRawAccessMOC"
+ "T@\"NSManagedObjectContext\",&,N,V_backgroundReadingMOC"
+ "T@\"NSManagedObjectContext\",&,N,V_backgroundStoreMoHandlerMOC"
+ "T@\"NSPersistentContainer\",&,N,V_persistentContainer"
+ "T@\"NSPersistentStoreDescription\",&,N,V_storeDescription"
+ "T@\"NSString\",&,N,V_analyticsStoreOptionsDescription"
+ "T@\"NSXPCInterface\",&,N,V_exportedRemoteInterface"
+ "T@\"WAAnalyticsAccess\",&,N,V_analyticsRawAccessObj"
+ "TB,V_storeLoaded"
+ "URLWithString:"
+ "WAPersistentContainer"
+ "WAStore_EnableMigrateStoreOnProcess"
+ "WAStore_EnableXPCStoreOnProcess"
+ "WAStore_isWritingInAnalyticsStoreAllowed"
+ "WAStore_maxSize"
+ "WiFiAnalytics-675.32 Mar  7 2025 22:23:03"
+ "WiFiAnalytics-675.32 Mar  7 2025 22:23:04"
+ "_analyticsProcessorObj"
+ "_analyticsRawAccessObj"
+ "_analyticsStoreOptionsDescription"
+ "_backgroundFileWritingMOC"
+ "_backgroundRawAccessMOC"
+ "_backgroundStoreMoHandlerMOC"
+ "_countForFetchRequest:error:onMoc:"
+ "_countForFetchRequestWithBlockAndWait:error:onMoc:"
+ "_exportedRemoteInterface"
+ "_performFetch:error:onMoc:"
+ "_performFetchWithBlockAndWait:error:onMoc:"
+ "_persistentContainer"
+ "_storeLoadError"
+ "_storeLoaded"
+ "accessWithPersistentContainer:"
+ "addPersistentStoreRemoteChangeNotificationObserver:selector:"
+ "addPersistentStoreRemoteChangeNotificationObserver:selector:coordinator:"
+ "analyticsProcessor"
+ "analyticsProcessorObj"
+ "analyticsProcessorWithPersistentContainer:"
+ "analyticsRawAccess"
+ "analyticsRawAccessObj"
+ "analyticsStoreOptionsDescription"
+ "backgroundFileWritingMOC"
+ "backgroundRawAccessMOC"
+ "backgroundStoreMoHandlerMOC"
+ "canWrite"
+ "copyNeighborGraphAsDictionaryOnMoc:"
+ "countForFetchRequestWithBlockAndWait:error:"
+ "countForFetchRequestWithBlockAndWaitOnBbMoc:error:"
+ "customMigrationOnProcess"
+ "customXPCStoreOnProcess"
+ "defaultModelName"
+ "domain"
+ "dumpDeploymentGraphJSONFile"
+ "dumpDeviceAnalyticsCSVsToFileWithBatchSize:maxAge:"
+ "dumpDeviceAnalyticsToFile"
+ "dumpDeviceAnalyticsToFileWithFetchLimit:maxAge:"
+ "dumpDeviceAnalyticsUsingBatchSizeToFileWithBatchSize:maxAge:"
+ "entitiesByName"
+ "exportedRemoteInterface"
+ "getPolicyHandlersConfig"
+ "initPolicyHandlers"
+ "initWithBssidArray:ssid:persistentContainer:"
+ "initWithContainer:"
+ "initWithOptions:andContainer:"
+ "initWithPersistentContainer:"
+ "initWithStoreURL:modelURL:"
+ "isWritingInAnalyticsStoreAllowed"
+ "loadPersistentStoresWithCompletionHandler:"
+ "loadStore"
+ "loadStoreIfNeeded"
+ "moc"
+ "mom"
+ "newBackgroundContext"
+ "optionDescription:"
+ "performFetch:error:"
+ "performFetchWithBlockAndWait:error:"
+ "performFetchWithBlockAndWaitOnBbMoc:error:"
+ "persistentContainer"
+ "persistentContainerWithName:managedObjectModel:"
+ "processWAMessageMetric:data:andDeferSaveToDisk:"
+ "processWAMessageMetric:data:andSave:"
+ "rawAccessCanWrite"
+ "read"
+ "releaseBackgroundFileWritingMOC"
+ "releaseBackgroundProcessingMOC"
+ "releaseBackgroundRawAccessMOC"
+ "releaseBackgroundReadingMOC"
+ "releaseBackgroundStoreMoHandlerMOC"
+ "removeObserver:name:object:"
+ "removePersistentStoreRemoteChangeNotificationObserver:"
+ "removePersistentStoreRemoteChangeNotificationObserver:coordinator:"
+ "resetBackgroundRawAccessMOC"
+ "resetBackgroundReadingMOC"
+ "saveAndResetBackgroundProcessingMOC"
+ "saveAndResetManagedObjectContext"
+ "setAnalyticsProcessorObj:"
+ "setAnalyticsRawAccessObj:"
+ "setAnalyticsStoreOptionsDescription:"
+ "setBackgroundFileWritingMOC:"
+ "setBackgroundRawAccessMOC:"
+ "setBackgroundReadingMOC:"
+ "setBackgroundStoreMoHandlerMOC:"
+ "setBss:"
+ "setExportedRemoteInterface:"
+ "setFutureApfsPurgeableDeadline:forURL:"
+ "setPersistentContainer:"
+ "setPersistentStoreDescriptions:"
+ "setPolicyHandlersConfig:"
+ "setStoreDescription:"
+ "setStoreLoadError:"
+ "setStoreLoaded:"
+ "sharedAnalyticsStoreMOHandlerWithContainer:"
+ "sharedDeviceAnalyticsClient"
+ "shouldMigrateStoreAutomatically"
+ "storeLoadError"
+ "storeLoaded"
+ "updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:"
+ "updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:andReply:"
+ "updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:andReply:queuedInvocation:"
+ "v16@?0@\"NSString\"8"
+ "v32@0:8@16:24"
+ "v36@0:8@16@24B32"
+ "v40@0:8@16:24@32"
+ "v40@0:8{?=qqq}16"
+ "viewContext"
+ "write"
+ "writeData:toFile:"
+ "writeObj:toJSONFile:"
+ "xpcConnection:updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:andReply:"
+ "yyyy'-'MM'-'dd_HH':'mm':'ss'.'SSS"
+ "{?=qqq}16@0:8"
- "%{public}s::%d:%s: OVERRIDING NSPersistentStoreConnectionPoolMaxSizeKey to %u"
- "%{public}s::%d:%s: OVERRIDING isStoreCompatible to %u"
- "%{public}s::%d:%s: Reducing NSPersistentStoreConnectionPoolMaxSizeKey to 2 since proc is not wifianalyticsd"
- "%{public}s::%d:AnalyticsStoreMOHandler failed initWithType -- Store unavailable to this process until reboot"
- "%{public}s::%d:AnalyticsStoreMOHandler isStoreCompatibleAtURL is %d"
- "%{public}s::%d:Attempting Save MOC with save"
- "%{public}s::%d:Attempting to migrate incompatible store at URL %@"
- "%{public}s::%d:Copying persistenceCoordinator from AnalyticsStoreMOHandler"
- "%{public}s::%d:ERROR NSPersistentStoreCoordinator metadataForPersistentStoreOfType failed to alloc"
- "%{public}s::%d:ERROR NSPersistentStoreCoordinator metadataForPersistentStoreOfType returned error %@"
- "%{public}s::%d:Error [self initCommon] failed"
- "%{public}s::%d:Error creating direct store descriptor"
- "%{public}s::%d:Error creating initCommmonObjects"
- "%{public}s::%d:Error creating server store descriptor with options: %lu"
- "%{public}s::%d:Error creating store controller"
- "%{public}s::%d:Error getting managedObjectHandler"
- "%{public}s::%d:Error getting managedObjectHandler with options %lu"
- "%{public}s::%d:Error getting sharedAnalyticsStoreMOHandlerWithPersist"
- "%{public}s::%d:Error given store controller"
- "%{public}s::%d:Error saving context: %@ %@"
- "%{public}s::%d:Error saving moc"
- "%{public}s::%d:Error with byoMOC"
- "%{public}s::%d:Getting NSPersistentStoreCoordinator metadataForPersistentStoreOfType"
- "%{public}s::%d:Initing AnalyticsStoreMOHandler with AnalyticsProcessorMigrationCapable - this should only be proc wifianalyticsd"
- "%{public}s::%d:Initting AnalyticsStoreMOHandler attempting to reuse existing instance for this pid"
- "%{public}s::%d:Migration not enabled on this process.. bailing!"
- "%{public}s::%d:NSManagedObjectModel doesn't exist yet for this process, alloc and init instance for URL: %@"
- "%{public}s::%d:NSPersistentStoreCoordinator doesn't exist yet for this process, alloc and init instance"
- "%{public}s::%d:NSPersistentStoreCoordinator metadataForPersistentStoreOfType metadata is %@"
- "%{public}s::%d:Nil - geoTag coordinates geoTag.date %@"
- "%{public}s::%d:Options have AnalyticsProcessorEnableXPCStore, setting AnalyticsStoreMOSetupXPCStore"
- "%{public}s::%d:Options have AnalyticsProcessorMigrationCapable, setting AnalyticsStoreMOMigration"
- "%{public}s::%d:Saved context"
- "%{public}s::%d:Store at URL %@ may need migration"
- "%{public}s::%d:Store does not exist on this device."
- "%{public}s::%d:Store needs migration - Wait for wifianalyticsd to complete migration and retry"
- "%{public}s::%d:Unhandled options %lu"
- "%{public}s::%d:WAAnalyticsAccess copyWithZone options = %lu, moHandler exists = %d, psc exists = %d"
- "%{public}s::%d:XPC: WAClient - summarizeDeviceAnalyticsForNetwork - error: %@"
- "%{public}s::%d:_persistenceCoordinator is nil"
- "%{public}s::%d:added persistent store with description %@"
- "%{public}s::%d:analyticsStoreMOHandler nil"
- "%{public}s::%d:bssMO nil for bssid:%@ and SSID:%@"
- "%{public}s::%d:bssMO.apProfileID nil for bssid:%@ and SSID:%@"
- "%{public}s::%d:error %@ adding persistent store %@"
- "%{public}s::%d:failed to add persistent store"
- "%{public}s::%d:failed to create managedObjectModel"
- "%{public}s::%d:failed to create persistence manager"
- "%{public}s::%d:initialized remote server %@"
- "%{public}s::%d:managed object model is nil"
- "%{public}s::%d:persistenceCoordinator nil"
- "%{public}s::%d:persistenceManager nil"
- "%{public}s::%d:resultChannelList empty"
- "%{public}s::%d:setupXPCStore: %d migrateIfNecessary: %d"
- "%{public}s::%d:sharedWAAnalyticsAccess doesn't exist yet for this process, alloc and init instance"
- "%{public}s::%d:storeDescriptor is nil"
- "%{public}s::%d:storeMOHandler nil"
- "%{public}s::%d:storeMOHandler nil managedObjectHandler"
- "+[AnalyticsPersistenceManager isStoreCompatibleAtURL:withModel:]"
- "+[AnalyticsPersistenceManager isStoreCompatibleAtURL:withModel:]_block_invoke"
- "+[AnalyticsPersistenceManager sharedWAPersistenceCoordinatorWithMOM:]_block_invoke"
- "+[AnalyticsProcessor sharedAnalyticsProcessor]"
- "+[AnalyticsProcessor sharedAnalyticsProcessor]_block_invoke"
- "+[AnalyticsStoreDescriptor defaultModelURL]"
- "+[AnalyticsStoreDescriptor defaultPersistentStoreURL]"
- "+[AnalyticsStoreMOContext sharedManagedObjectModel:]_block_invoke"
- "+[AnalyticsStoreMOHandler isStoreCompatible]"
- "+[AnalyticsStoreMOHandler sharedAnalyticsStoreMOHandlerWithPersist]"
- "+[WAAnalyticsAccess accessWithOptions:]"
- "+[WAAnalyticsAccess sharedWAAnalyticsAccess]_block_invoke"
- "+[WADeviceAnalyticsClient sharedDeviceAnalyticsClientWithPersist]"
- "+[WADeviceAnalyticsClient sharedDeviceAnalyticsClientWithPersist]_block_invoke"
- "+[WAUtil isAnalyticsProcessorAllowed]"
- "+[WAUtil shouldEnableXPCStore]_block_invoke"
- "-[AnalyticsPersistenceManager initWithManagedObjectModel:storeDescriptor:]"
- "-[AnalyticsPersistenceManager initWithManagedObjectModel:storeDescriptor:]_block_invoke"
- "-[AnalyticsProcessor apProfileForBssid:andSSID:]_block_invoke"
- "-[AnalyticsProcessor initCommmonObjects]"
- "-[AnalyticsProcessor initWithOptions:]"
- "-[AnalyticsProcessor initWithOptions:byoMOC:]"
- "-[AnalyticsProcessor processWAMessageMetric:data:]"
- "-[AnalyticsProcessor summarizeAnalyticsForNetwork:maxAgeInDays:]"
- "-[AnalyticsProcessor summarizeAnalyticsForNetwork:maxAgeInDays:]_block_invoke"
- "-[AnalyticsReader initWithAnalyticsStore:]"
- "-[AnalyticsStoreDescriptor initWithType:storeURL:modelURL:options:]"
- "-[AnalyticsStoreDescriptor initWithType:storeURL:modelURL:options:]_block_invoke"
- "-[AnalyticsStoreFileWriter analyticsStoreFileWriterDirectory]"
- "-[AnalyticsStoreFileWriter initWithAnalyticsStore:]"
- "-[AnalyticsStoreFileWriter init]"
- "-[AnalyticsStoreMOContext initWithStoreDescriptor:]"
- "-[AnalyticsStoreMOContext storeNeedsImmediatePruning:]"
- "-[AnalyticsStoreMOHandler initWithContext:]"
- "-[AnalyticsStoreMOHandler initWithType:options:]"
- "-[AnalyticsStoreMOHandler saveManagedObjectContext]"
- "-[NeighborGraph copyNeighborGraphAsDictionary]"
- "-[NeighborGraph copyNeighborGraphAsDictionary]_block_invoke"
- "-[NeighborGraph initWithBssidArray:ssid:handler:]"
- "-[WAAnalyticsAccess copyWithZone:]"
- "-[WAAnalyticsAccess save]"
- "-[WAClient summarizeDeviceAnalyticsForNetwork:maxAgeInDays:andReply:queuedInvocation:]_block_invoke"
- "-[WADeviceAnalyticsClient initCommon]"
- "-[WADeviceAnalyticsClient initWithSharedServerType]"
- "@\"AnalyticsPersistenceManager\""
- "@\"AnalyticsStoreDescriptor\""
- "@\"AnalyticsStoreMOContext\""
- "@\"NSManagedObjectModel\""
- "@\"NSPersistentStoreCoordinator\""
- "@\"NSXPCStoreServer\""
- "@48@0:8Q16@24@32Q40"
- "AnalyticsPersistenceManager"
- "AnalyticsPersistenceManager Init"
- "AnalyticsPersistenceManager PersistentStoreCoordinatorInit"
- "AnalyticsPersistenceManager XPCStoreInit"
- "AnalyticsProcessor initWithOptions"
- "AnalyticsProcessor initWithOptionsAndMOC"
- "AnalyticsStoreMOContext"
- "AnalyticsStoreRemoteServerHandlingPolicy"
- "Can't construct Array with count < 0"
- "Error in Init"
- "Insufficient space allocated to copy string contents"
- "NSPersistentStoreConnectionPoolMaxSizeKey"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "T@\"AnalyticsPersistenceManager\",&,N,V_persistenceManager"
- "T@\"AnalyticsStoreDescriptor\",&,N,V_storeDescriptor"
- "T@\"AnalyticsStoreMOContext\",&,N,V_storeMOContext"
- "T@\"AnalyticsStoreMOContext\",R,&,N,V__storeMOContext"
- "T@\"AnalyticsStoreMOHandler\",&,N,V__moHandler"
- "T@\"NSError\",&,N,V_persistentStoreError"
- "T@\"NSManagedObjectContext\",&,N,V__managedObjectContext"
- "T@\"NSManagedObjectContext\",R,&,N"
- "T@\"NSManagedObjectContext\",R,N,V_backgroundReadingMOC"
- "T@\"NSManagedObjectModel\",&,N,V_sharedManagedObjectModel"
- "T@\"NSManagedObjectModel\",R,N,V_managedObjectModel"
- "T@\"NSPersistentStoreCoordinator\",R,&,N,V__persistentStoreCoordinator"
- "T@\"NSPersistentStoreCoordinator\",R,N,V_persistenceCoordinator"
- "T@\"NSPersistentStoreDescription\",R,N,V_storeDescription"
- "T@\"NSXPCStoreServer\",&,N,V_xpcStoreServer"
- "TQ,N,V_storeType"
- "TQ,N,V_type"
- "Unable to create directory at %@: %@"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "WAStore_EnableXPCStore"
- "WiFiAnalytics-645.4 Dec 14 2024 18:52:27"
- "WiFiAnalytics-645.4 Dec 14 2024 18:52:28"
- "__managedObjectContext"
- "__moHandler"
- "__persistentStoreCoordinator"
- "__storeMOContext"
- "_managedObjectModel"
- "_persistenceCoordinator"
- "_persistenceManager"
- "_persistentStoreError"
- "_sharedManagedObjectModel"
- "_storeDescriptor"
- "_storeMOContext"
- "_storeType"
- "_xpcStoreServer"
- "accessWithOptions:"
- "addFaultsObject:"
- "addPersistentStoreWithDescription:completionHandler:"
- "applicationSupportDirectoryPath is nil"
- "checkResourceIsReachableAndReturnError:"
- "copyNeighborGraphAsDictionary"
- "defaultPersistentStoreURL is nil with path %@"
- "directStoreDescriptor"
- "initCommmonObjects"
- "initCommon"
- "initForStoreWithURL:usingModelAtURL:options:policy:"
- "initWithBssidArray:ssid:handler:"
- "initWithConcurrencyType:"
- "initWithContext:"
- "initWithManagedObjectModel:"
- "initWithManagedObjectModel:storeDescriptor:"
- "initWithOptions:"
- "initWithOptions:byoMOC:"
- "initWithSharedServerType"
- "initWithStoreDescriptor:"
- "initWithType:options:"
- "initWithType:storeURL:modelURL:options:"
- "invalid Collection: less than 'count' elements in collection"
- "isAnalyticsProcessorAllowed"
- "isConfiguration:compatibleWithStoreMetadata:"
- "isStoreCompatible"
- "isStoreCompatibleAtURL:withModel:"
- "mergeByPropertyObjectTrumpMergePolicy"
- "metadataForPersistentStoreOfType:URL:options:error:"
- "moHandler"
- "options=%lu"
- "persistenceCoordinator"
- "persistenceManager"
- "persistentStoreError"
- "save"
- "serverStoreDescriptor:"
- "setManagedObjectContext:"
- "setMoHandler:"
- "setPersistenceManager:"
- "setPersistentStoreCoordinator:"
- "setPersistentStoreError:"
- "setSharedManagedObjectModel:"
- "setStoreDescriptor:"
- "setStoreMOContext:"
- "setStoreType:"
- "setTransactionAuthor:"
- "setXpcStoreServer:"
- "sharedAnalyticsProcessor"
- "sharedAnalyticsStoreMOHandlerWithPersist"
- "sharedDeviceAnalyticsClientWithPersist"
- "sharedManagedObjectModel"
- "sharedManagedObjectModel:"
- "sharedWAAnalyticsAccess"
- "sharedWAPersistenceCoordinatorWithMOM:"
- "shouldAcceptConnectionsFromClientWithContext:"
- "shouldEnableXPCStore"
- "startListening"
- "storeMOContext"
- "storeType"
- "summarizeAnalyticsForNetwork:maxAgeInDays:"
- "summarizeDeviceAnalyticsForNetwork:maxAgeInDays:andReply:"
- "summarizeDeviceAnalyticsForNetwork:maxAgeInDays:andReply:queuedInvocation:"
- "type %lu migrateOpt %d"
- "xctests"
- "xpcConnection:summarizeDeviceAnalyticsForNetwork:maxAgeInDays:andReply:"
- "xpcStoreServer"
- "yyyy'-'MM'-'dd HH':'mm':'ss'.'SSS"

```
