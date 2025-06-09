## ActivityAchievements

> `/System/Library/PrivateFrameworks/ActivityAchievements.framework/ActivityAchievements`

```diff

-612.6.0.0.0
-  __TEXT.__text: 0x3ba9c
-  __TEXT.__auth_stubs: 0x5c0
-  __TEXT.__objc_methlist: 0x3884
+643.0.1.0.0
+  __TEXT.__text: 0x3abfc
+  __TEXT.__auth_stubs: 0x590
+  __TEXT.__objc_methlist: 0x381c
   __TEXT.__const: 0x2c8
-  __TEXT.__oslogstring: 0xe80
-  __TEXT.__cstring: 0x6a66
-  __TEXT.__gcc_except_tab: 0x918
-  __TEXT.__unwind_info: 0xcf8
-  __TEXT.__objc_classname: 0x55c
-  __TEXT.__objc_methname: 0x8439
-  __TEXT.__objc_methtype: 0x11a3
-  __TEXT.__objc_stubs: 0x5100
-  __DATA_CONST.__got: 0x298
-  __DATA_CONST.__const: 0xa40
-  __DATA_CONST.__objc_classlist: 0x108
+  __TEXT.__oslogstring: 0xd7c
+  __TEXT.__cstring: 0x6a8a
+  __TEXT.__gcc_except_tab: 0xa50
+  __TEXT.__unwind_info: 0xca0
+  __TEXT.__objc_classname: 0x5a6
+  __TEXT.__objc_methname: 0x7fed
+  __TEXT.__objc_methtype: 0x128d
+  __TEXT.__objc_stubs: 0x5020
+  __DATA_CONST.__got: 0x288
+  __DATA_CONST.__const: 0x790
+  __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d60
-  __DATA_CONST.__objc_protorefs: 0x58
+  __DATA_CONST.__objc_selrefs: 0x1d08
+  __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x100
   __DATA_CONST.__objc_arraydata: 0x9d8
-  __AUTH_CONST.__auth_got: 0x2f0
-  __AUTH_CONST.__const: 0x4c0
-  __AUTH_CONST.__cfstring: 0x7380
-  __AUTH_CONST.__objc_const: 0x75b8
+  __AUTH_CONST.__auth_got: 0x2d8
+  __AUTH_CONST.__const: 0x4e0
+  __AUTH_CONST.__cfstring: 0x7460
+  __AUTH_CONST.__objc_const: 0x6ee8
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_intobj: 0x300
-  __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x3f8
+  __AUTH.__objc_data: 0x208
+  __DATA.__objc_ivar: 0x3e4
   __DATA.__data: 0x6d0
-  __DATA.__bss: 0x100
-  __DATA_DIRTY.__objc_data: 0x8c0
-  __DATA_DIRTY.__bss: 0x140
+  __DATA.__bss: 0xe0
+  __DATA_DIRTY.__objc_data: 0x898
+  __DATA_DIRTY.__bss: 0x170
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0E5249A0-1AE9-31E0-B136-EF63843A5387
-  Functions: 1610
-  Symbols:   4846
-  CStrings:  3495
+  UUID: 5A5B2E97-215B-372A-8B9F-681DE7BFD3E8
+  Functions: 1556
+  Symbols:   4694
+  CStrings:  3486
 
Symbols:
+ +[ACHCodableAchievementAnniversaryRequest templateNamesType]
+ +[ACHCodableTemplateNameArray templateNamesType]
+ -[ACHAwardsClient fetchEarnedInstancesForAnniversaryOfDateComponents:templateUniqueNames:error:]
+ -[ACHAwardsClient fetchEarnedInstancesForDateInterval:error:]
+ -[ACHAwardsKeyValueClient dataForKey:domain:error:]
+ -[ACHAwardsKeyValueClient setData:forKey:domain:error:]
+ -[ACHCloudSyncStatusProvider .cxx_destruct]
+ -[ACHCloudSyncStatusProvider _cloudRestoreStatusCheckEnabled]
+ -[ACHCloudSyncStatusProvider activate]
+ -[ACHCloudSyncStatusProvider cloudRestoreCompletionDate]
+ -[ACHCloudSyncStatusProvider cloudSyncObserver:syncDidStartWithProgress:]
+ -[ACHCloudSyncStatusProvider cloudSyncObserver:syncFailedWithError:]
+ -[ACHCloudSyncStatusProvider cloudSyncObserver:syncFailedWithError:].cold.1
+ -[ACHCloudSyncStatusProvider cloudSyncObserverStatusUpdated:status:]
+ -[ACHCloudSyncStatusProvider cloudSyncObserverSyncCompleted:]
+ -[ACHCloudSyncStatusProvider cloudSyncObserver]
+ -[ACHCloudSyncStatusProvider healthStore]
+ -[ACHCloudSyncStatusProvider initWithHealthStore:]
+ -[ACHCloudSyncStatusProvider isInitialCloudRestoreComplete]
+ -[ACHCloudSyncStatusProvider restoreCompletionDate]
+ -[ACHCloudSyncStatusProvider setCloudSyncObserver:]
+ -[ACHCloudSyncStatusProvider setHealthStore:]
+ -[ACHCloudSyncStatusProvider setRestoreCompletionDate:]
+ -[ACHCodableAchievementAnniversaryRequest .cxx_destruct]
+ -[ACHCodableAchievementAnniversaryRequest addTemplateNames:]
+ -[ACHCodableAchievementAnniversaryRequest clearTemplateNames]
+ -[ACHCodableAchievementAnniversaryRequest copyTo:]
+ -[ACHCodableAchievementAnniversaryRequest copyWithZone:]
+ -[ACHCodableAchievementAnniversaryRequest dateComponents]
+ -[ACHCodableAchievementAnniversaryRequest description]
+ -[ACHCodableAchievementAnniversaryRequest dictionaryRepresentation]
+ -[ACHCodableAchievementAnniversaryRequest hasDateComponents]
+ -[ACHCodableAchievementAnniversaryRequest hash]
+ -[ACHCodableAchievementAnniversaryRequest isEqual:]
+ -[ACHCodableAchievementAnniversaryRequest mergeFrom:]
+ -[ACHCodableAchievementAnniversaryRequest readFrom:]
+ -[ACHCodableAchievementAnniversaryRequest setDateComponents:]
+ -[ACHCodableAchievementAnniversaryRequest setTemplateNames:]
+ -[ACHCodableAchievementAnniversaryRequest templateNamesAtIndex:]
+ -[ACHCodableAchievementAnniversaryRequest templateNamesCount]
+ -[ACHCodableAchievementAnniversaryRequest templateNames]
+ -[ACHCodableAchievementAnniversaryRequest writeTo:]
+ -[ACHCodableAchievementAnniversaryRequest(TransportSerializable) initWithSerializedData:error:]
+ -[ACHCodableDateComponentsInterval .cxx_destruct]
+ -[ACHCodableDateComponentsInterval copyTo:]
+ -[ACHCodableDateComponentsInterval copyWithZone:]
+ -[ACHCodableDateComponentsInterval description]
+ -[ACHCodableDateComponentsInterval dictionaryRepresentation]
+ -[ACHCodableDateComponentsInterval endDateComponents]
+ -[ACHCodableDateComponentsInterval hasEndDateComponents]
+ -[ACHCodableDateComponentsInterval hasStartDateComponents]
+ -[ACHCodableDateComponentsInterval hash]
+ -[ACHCodableDateComponentsInterval isEqual:]
+ -[ACHCodableDateComponentsInterval mergeFrom:]
+ -[ACHCodableDateComponentsInterval readFrom:]
+ -[ACHCodableDateComponentsInterval setEndDateComponents:]
+ -[ACHCodableDateComponentsInterval setStartDateComponents:]
+ -[ACHCodableDateComponentsInterval startDateComponents]
+ -[ACHCodableDateComponentsInterval writeTo:]
+ -[ACHCodableDateComponentsInterval(TransportSerializable) initWithSerializedData:error:]
+ -[ACHCodableTemplateNameArray .cxx_destruct]
+ -[ACHCodableTemplateNameArray addTemplateNames:]
+ -[ACHCodableTemplateNameArray clearTemplateNames]
+ -[ACHCodableTemplateNameArray copyTo:]
+ -[ACHCodableTemplateNameArray copyWithZone:]
+ -[ACHCodableTemplateNameArray description]
+ -[ACHCodableTemplateNameArray dictionaryRepresentation]
+ -[ACHCodableTemplateNameArray hash]
+ -[ACHCodableTemplateNameArray isEqual:]
+ -[ACHCodableTemplateNameArray mergeFrom:]
+ -[ACHCodableTemplateNameArray readFrom:]
+ -[ACHCodableTemplateNameArray setTemplateNames:]
+ -[ACHCodableTemplateNameArray templateNamesAtIndex:]
+ -[ACHCodableTemplateNameArray templateNamesCount]
+ -[ACHCodableTemplateNameArray templateNames]
+ -[ACHCodableTemplateNameArray writeTo:]
+ -[ACHCodableTemplateNameArray(TransportSerializable) initWithCodableTemplateNames:]
+ -[ACHCodableTemplateNameArray(TransportSerializable) initWithSerializedData:error:]
+ GCC_except_table39
+ GCC_except_table43
+ GCC_except_table82
+ GCC_except_table86
+ OBJC_IVAR_$_ACHCodableAchievementAnniversaryRequest._dateComponents
+ OBJC_IVAR_$_ACHCodableAchievementAnniversaryRequest._templateNames
+ OBJC_IVAR_$_ACHCodableDateComponentsInterval._endDateComponents
+ OBJC_IVAR_$_ACHCodableDateComponentsInterval._startDateComponents
+ OBJC_IVAR_$_ACHCodableTemplateNameArray._templateNames
+ _ACHActivityAwardsdBundleIdentifier
+ _ACHAnniversarySuffixFromDateComponents
+ _ACHCloudRestoreStatusCheckEnabledKey
+ _ACHCloudSyncStatusProviderStatusChangeNotification
+ _ACHCodableAchievementAnniversaryRequestReadFrom
+ _ACHCodableDateComponentsIntervalReadFrom
+ _ACHCodableFromAnniversaryRequest
+ _ACHCodableFromDateInterval
+ _ACHCodableFromTemplateNameArray
+ _ACHCodableTemplateNameArrayReadFrom
+ _ACHDateFromCodable
+ _ACHDateIntervalFromCodable
+ _ACHLogScheduler
+ _ACHLogScheduler.category
+ _ACHLogScheduler.cold.1
+ _ACHLogScheduler.onceToken
+ _ACHMonthlyChallengeTemplateNamePrefix
+ _ACHTemplateNameArrayFromCodableAnniversaryRequest
+ _ACHTemplateNameArrayFromCodableTemplateNameArray
+ _ACHYearMonthDayDateComponentsFromDateInterval
+ _ACHYearMonthDayStringFromDate
+ _OBJC_CLASS_$_ACHCloudSyncStatusProvider
+ _OBJC_CLASS_$_ACHCodableAchievementAnniversaryRequest
+ _OBJC_CLASS_$_ACHCodableDateComponentsInterval
+ _OBJC_CLASS_$_ACHCodableTemplateNameArray
+ _OBJC_CLASS_$_HKCloudSyncObserver
+ _OBJC_CLASS_$_NSNotificationCenter
+ _OBJC_CLASS_$_PBRequest
+ _OBJC_IVAR_$_ACHCloudSyncStatusProvider._cloudSyncObserver
+ _OBJC_IVAR_$_ACHCloudSyncStatusProvider._healthStore
+ _OBJC_IVAR_$_ACHCloudSyncStatusProvider._lock
+ _OBJC_IVAR_$_ACHCloudSyncStatusProvider._restoreCompletionDate
+ _OBJC_METACLASS_$_ACHCloudSyncStatusProvider
+ _OBJC_METACLASS_$_ACHCodableAchievementAnniversaryRequest
+ _OBJC_METACLASS_$_ACHCodableDateComponentsInterval
+ _OBJC_METACLASS_$_ACHCodableTemplateNameArray
+ _OBJC_METACLASS_$_PBRequest
+ __OBJC_$_CLASS_METHODS_ACHCodableAchievementAnniversaryRequest
+ __OBJC_$_CLASS_METHODS_ACHCodableTemplateNameArray
+ __OBJC_$_INSTANCE_METHODS_ACHCloudSyncStatusProvider
+ __OBJC_$_INSTANCE_METHODS_ACHCodableAchievementAnniversaryRequest(TransportSerializable)
+ __OBJC_$_INSTANCE_METHODS_ACHCodableDateComponentsInterval(TransportSerializable)
+ __OBJC_$_INSTANCE_METHODS_ACHCodableTemplateNameArray(TransportSerializable)
+ __OBJC_$_INSTANCE_VARIABLES_ACHCloudSyncStatusProvider
+ __OBJC_$_INSTANCE_VARIABLES_ACHCodableAchievementAnniversaryRequest
+ __OBJC_$_INSTANCE_VARIABLES_ACHCodableDateComponentsInterval
+ __OBJC_$_INSTANCE_VARIABLES_ACHCodableTemplateNameArray
+ __OBJC_$_PROP_LIST_ACHCloudSyncStatusProvider
+ __OBJC_$_PROP_LIST_ACHCodableAchievementAnniversaryRequest
+ __OBJC_$_PROP_LIST_ACHCodableDateComponentsInterval
+ __OBJC_$_PROP_LIST_ACHCodableTemplateNameArray
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ACHCloudSyncStatusProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HKCloudSyncObserverDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HKCloudSyncObserverDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ACHCloudSyncStatusProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HKCloudSyncObserverDelegate
+ __OBJC_$_PROTOCOL_REFS_HKCloudSyncObserverDelegate
+ __OBJC_CLASS_PROTOCOLS_$_ACHCloudSyncStatusProvider
+ __OBJC_CLASS_PROTOCOLS_$_ACHCodableAchievementAnniversaryRequest
+ __OBJC_CLASS_PROTOCOLS_$_ACHCodableDateComponentsInterval
+ __OBJC_CLASS_PROTOCOLS_$_ACHCodableTemplateNameArray
+ __OBJC_CLASS_RO_$_ACHCloudSyncStatusProvider
+ __OBJC_CLASS_RO_$_ACHCodableAchievementAnniversaryRequest
+ __OBJC_CLASS_RO_$_ACHCodableDateComponentsInterval
+ __OBJC_CLASS_RO_$_ACHCodableTemplateNameArray
+ __OBJC_LABEL_PROTOCOL_$_ACHCloudSyncStatusProviding
+ __OBJC_LABEL_PROTOCOL_$_HKCloudSyncObserverDelegate
+ __OBJC_METACLASS_RO_$_ACHCloudSyncStatusProvider
+ __OBJC_METACLASS_RO_$_ACHCodableAchievementAnniversaryRequest
+ __OBJC_METACLASS_RO_$_ACHCodableDateComponentsInterval
+ __OBJC_METACLASS_RO_$_ACHCodableTemplateNameArray
+ __OBJC_PROTOCOL_$_ACHCloudSyncStatusProviding
+ __OBJC_PROTOCOL_$_HKCloudSyncObserverDelegate
+ ___51-[ACHAwardsKeyValueClient dataForKey:domain:error:]_block_invoke
+ ___51-[ACHAwardsKeyValueClient dataForKey:domain:error:]_block_invoke_2
+ ___51-[ACHAwardsKeyValueClient dataForKey:domain:error:]_block_invoke_3
+ ___55-[ACHAwardsKeyValueClient setData:forKey:domain:error:]_block_invoke
+ ___55-[ACHAwardsKeyValueClient setData:forKey:domain:error:]_block_invoke_2
+ ___55-[ACHAwardsKeyValueClient setData:forKey:domain:error:]_block_invoke_3
+ ___61-[ACHAwardsClient fetchEarnedInstancesForDateInterval:error:]_block_invoke
+ ___61-[ACHAwardsClient fetchEarnedInstancesForDateInterval:error:]_block_invoke_2
+ ___61-[ACHAwardsClient fetchEarnedInstancesForDateInterval:error:]_block_invoke_3
+ ___96-[ACHAwardsClient fetchEarnedInstancesForAnniversaryOfDateComponents:templateUniqueNames:error:]_block_invoke
+ ___96-[ACHAwardsClient fetchEarnedInstancesForAnniversaryOfDateComponents:templateUniqueNames:error:]_block_invoke_2
+ ___96-[ACHAwardsClient fetchEarnedInstancesForAnniversaryOfDateComponents:templateUniqueNames:error:]_block_invoke_3
+ ___ACHLogScheduler_block_invoke
+ ___block_descriptor_48_e8_32r40r_e28_v24?0"NSData"8"NSError"16lr32l8r40l8
+ ___block_literal_global.310
+ ___block_literal_global.332
+ ___block_literal_global.441
+ ___block_literal_global.446
+ ___block_literal_global.452
+ ___block_literal_global.464
+ ___block_literal_global.466
+ ___block_literal_global.468
+ ___block_literal_global.476
+ ___block_literal_global.500
+ ___block_literal_global.502
+ ___block_literal_global.514
+ ___block_literal_global.519
+ _objc_msgSend$_cloudRestoreStatusCheckEnabled
+ _objc_msgSend$_setError
+ _objc_msgSend$addTemplateNames:
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$clearTemplateNames
+ _objc_msgSend$cloudSyncObserver
+ _objc_msgSend$currentCalendar
+ _objc_msgSend$dateComponents
+ _objc_msgSend$defaultCenter
+ _objc_msgSend$distantPast
+ _objc_msgSend$endDate
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$initWithHealthStore:delegate:
+ _objc_msgSend$position
+ _objc_msgSend$postNotificationName:object:
+ _objc_msgSend$remote_dataForKey:domain:completion:
+ _objc_msgSend$remote_fetchEarnedInstancesForAnniversaryDateComponentsString:templateUniqueNames:completion:
+ _objc_msgSend$remote_fetchEarnedInstancesForDateComponentStringsArray:completion:
+ _objc_msgSend$remote_setData:forKey:domain:completion:
+ _objc_msgSend$restoreCompletionDate
+ _objc_msgSend$setDateComponents:
+ _objc_msgSend$setEndDateComponents:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$setRestoreCompletionDate:
+ _objc_msgSend$setStartDateComponents:
+ _objc_msgSend$setTemplateNames:
+ _objc_msgSend$startDate
+ _objc_msgSend$startObservingSyncStatus
+ _objc_msgSend$status
+ _objc_msgSend$syncEnabled
+ _objc_msgSend$templateNames
+ _objc_msgSend$templateNamesAtIndex:
+ _objc_msgSend$templateNamesCount
- +[ACHCodableAchievement earnedInstancesType]
- +[ACHCurrentActivitySummaryQuery configurationClass]
- +[ACHCurrentActivitySummaryQueryServerConfiguration supportsSecureCoding]
- +[ACHQuery clientInterfaceProtocol]
- +[ACHQuery configureClientInterface:]
- +[ACHQuery supportsTaskServers]
- -[ACHAchievement earnedInstances]
- -[ACHAchievement initWithTemplate:earnedInstances:]
- -[ACHAchievement shallowCopyReplacingEarnedInstances:]
- -[ACHClient .cxx_destruct]
- -[ACHClient _addPluginProxyErrorHandler:]
- -[ACHClient _clientQueueCompletion:]
- -[ACHClient _injectProxyProvider:]
- -[ACHClient _remoteProxy:errorHandler:]
- -[ACHClient addEarnedInstance:completion:]
- -[ACHClient addTemplate:completion:]
- -[ACHClient availableMobileAssetsWithCompletion:]
- -[ACHClient clientQueue]
- -[ACHClient connectionInvalidated]
- -[ACHClient exportedInterface]
- -[ACHClient fetchAchievementWithTemplateUniqueName:completion:]
- -[ACHClient fetchActivityChallengeAssetsServerURLWithCompletion:]
- -[ACHClient fetchAllAchievementsWithCompletion:]
- -[ACHClient fetchAllEarnedInstancesWithCompletion:]
- -[ACHClient fetchAllTemplatesWithCompletion:]
- -[ACHClient fetchEphemeralAchievementWithTemplateUniqueName:completion:]
- -[ACHClient forceAwardingSchedulerWithCompletion:]
- -[ACHClient initWithHealthStore:]
- -[ACHClient injectedErrorHandler]
- -[ACHClient monthlyChallengeForDate:completion:]
- -[ACHClient pluginProxyProvider]
- -[ACHClient remoteInterface]
- -[ACHClient removeAllEarnedInstancesWithCompletion:]
- -[ACHClient removeAllTemplatesWithCompletion:]
- -[ACHClient removeEarnedInstance:completion:]
- -[ACHClient removeTemplate:completion:]
- -[ACHClient runMonthlyChallengesWithCompletion:]
- -[ACHClient serverProxy]
- -[ACHClient serverQueue]
- -[ACHClient setActivityChallengeAssetsServerURL:completion:]
- -[ACHClient setClientQueue:]
- -[ACHClient setInjectedErrorHandler:]
- -[ACHClient setPluginProxyProvider:]
- -[ACHClient setServerProxy:]
- -[ACHClient setServerQueue:]
- -[ACHClient templateForMonthlyChallengeType:completion:]
- -[ACHCodableAchievement addEarnedInstances:]
- -[ACHCodableAchievement clearEarnedInstances]
- -[ACHCodableAchievement earnedInstancesAtIndex:]
- -[ACHCodableAchievement earnedInstancesCount]
- -[ACHCodableAchievement earnedInstances]
- -[ACHCodableAchievement setEarnedInstances:]
- -[ACHCurrentActivitySummaryQuery _setCollectionIntervals:]
- -[ACHCurrentActivitySummaryQuery collectionIntervals]
- -[ACHCurrentActivitySummaryQuery queue_populateConfiguration:]
- -[ACHCurrentActivitySummaryQuery setCollectionIntervals:]
- -[ACHCurrentActivitySummaryQueryServerConfiguration .cxx_destruct]
- -[ACHCurrentActivitySummaryQueryServerConfiguration collectionIntervals]
- -[ACHCurrentActivitySummaryQueryServerConfiguration copyWithZone:]
- -[ACHCurrentActivitySummaryQueryServerConfiguration encodeWithCoder:]
- -[ACHCurrentActivitySummaryQueryServerConfiguration initWithCoder:]
- -[ACHCurrentActivitySummaryQueryServerConfiguration setCollectionIntervals:]
- -[ACHQuery .cxx_destruct]
- -[ACHQuery client_achievementsDidFinishInitialFetch:]
- -[ACHQuery client_deliverNewAchievements:]
- -[ACHQuery client_deliverRemovedAchievements:]
- -[ACHQuery client_deliverUpdatedAchievements:]
- -[ACHQuery errorHandler]
- -[ACHQuery initWithInitialAchievementsHandler:newAchievementsHandler:updatedAchievementsHandler:removedAchievementsHandler:]
- -[ACHQuery initialAchievementsHandler]
- -[ACHQuery newAchievementsHandler]
- -[ACHQuery queue_deliverError:]
- -[ACHQuery queue_queryDidDeactivate:]
- -[ACHQuery removedAchievementsHandler]
- -[ACHQuery setErrorHandler:]
- -[ACHQuery setInitialAchievementsHandler:]
- -[ACHQuery setNewAchievementsHandler:]
- -[ACHQuery setRemovedAchievementsHandler:]
- -[ACHQuery setUpdatedAchievementsHandler:]
- -[ACHQuery updatedAchievementsHandler]
- OBJC_IVAR_$_ACHCodableAchievement._earnedInstances
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _ACHServerInterface
- _ACHShouldUseNewAwardsSystem
- _OBJC_CLASS_$_ACHClient
- _OBJC_CLASS_$_ACHCurrentActivitySummaryQueryServerConfiguration
- _OBJC_CLASS_$_ACHQuery
- _OBJC_CLASS_$_HKPluginProxyProvider
- _OBJC_CLASS_$_HKQueryServerConfiguration
- _OBJC_CLASS_$_MAAsset
- _OBJC_IVAR_$_ACHAchievement._earnedInstances
- _OBJC_IVAR_$_ACHClient._clientQueue
- _OBJC_IVAR_$_ACHClient._injectedErrorHandler
- _OBJC_IVAR_$_ACHClient._pluginProxyProvider
- _OBJC_IVAR_$_ACHClient._serverProxy
- _OBJC_IVAR_$_ACHClient._serverQueue
- _OBJC_IVAR_$_ACHCurrentActivitySummaryQuery._collectionIntervals
- _OBJC_IVAR_$_ACHCurrentActivitySummaryQueryServerConfiguration._collectionIntervals
- _OBJC_IVAR_$_ACHQuery._errorHandler
- _OBJC_IVAR_$_ACHQuery._initialAchievementsHandler
- _OBJC_IVAR_$_ACHQuery._newAchievementsHandler
- _OBJC_IVAR_$_ACHQuery._removedAchievementsHandler
- _OBJC_IVAR_$_ACHQuery._updatedAchievementsHandler
- _OBJC_METACLASS_$_ACHClient
- _OBJC_METACLASS_$_ACHCurrentActivitySummaryQueryServerConfiguration
- _OBJC_METACLASS_$_ACHQuery
- _OBJC_METACLASS_$_HKQueryServerConfiguration
- __OBJC_$_CLASS_METHODS_ACHCurrentActivitySummaryQueryServerConfiguration
- __OBJC_$_CLASS_METHODS_ACHQuery
- __OBJC_$_INSTANCE_METHODS_ACHClient
- __OBJC_$_INSTANCE_METHODS_ACHCurrentActivitySummaryQueryServerConfiguration
- __OBJC_$_INSTANCE_METHODS_ACHQuery
- __OBJC_$_INSTANCE_VARIABLES_ACHClient
- __OBJC_$_INSTANCE_VARIABLES_ACHCurrentActivitySummaryQueryServerConfiguration
- __OBJC_$_INSTANCE_VARIABLES_ACHQuery
- __OBJC_$_PROP_LIST_ACHClient
- __OBJC_$_PROP_LIST_ACHCurrentActivitySummaryQueryServerConfiguration
- __OBJC_$_PROP_LIST_ACHQuery
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_ACHQueryClientInterface
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_ACHServerInterface
- __OBJC_$_PROTOCOL_METHOD_TYPES_ACHQueryClientInterface
- __OBJC_$_PROTOCOL_METHOD_TYPES_ACHServerInterface
- __OBJC_$_PROTOCOL_REFS_ACHQueryClientInterface
- __OBJC_$_PROTOCOL_REFS_ACHServerInterface
- __OBJC_CLASS_PROTOCOLS_$_ACHClient
- __OBJC_CLASS_PROTOCOLS_$_ACHQuery
- __OBJC_CLASS_RO_$_ACHClient
- __OBJC_CLASS_RO_$_ACHCurrentActivitySummaryQueryServerConfiguration
- __OBJC_CLASS_RO_$_ACHQuery
- __OBJC_LABEL_PROTOCOL_$_ACHQueryClientInterface
- __OBJC_LABEL_PROTOCOL_$_ACHServerInterface
- __OBJC_METACLASS_RO_$_ACHClient
- __OBJC_METACLASS_RO_$_ACHCurrentActivitySummaryQueryServerConfiguration
- __OBJC_METACLASS_RO_$_ACHQuery
- __OBJC_PROTOCOL_$_ACHQueryClientInterface
- __OBJC_PROTOCOL_$_ACHServerInterface
- __OBJC_PROTOCOL_REFERENCE_$_ACHQueryClientInterface
- __OBJC_PROTOCOL_REFERENCE_$_ACHServerInterface
- ___28-[ACHQuery setErrorHandler:]_block_invoke
- ___31-[ACHQuery queue_deliverError:]_block_invoke
- ___36-[ACHClient _clientQueueCompletion:]_block_invoke
- ___36-[ACHClient _clientQueueCompletion:]_block_invoke_2
- ___36-[ACHClient addTemplate:completion:]_block_invoke
- ___36-[ACHClient addTemplate:completion:]_block_invoke_2
- ___39-[ACHClient _remoteProxy:errorHandler:]_block_invoke
- ___39-[ACHClient _remoteProxy:errorHandler:]_block_invoke_2
- ___39-[ACHClient _remoteProxy:errorHandler:]_block_invoke_2.cold.1
- ___39-[ACHClient removeTemplate:completion:]_block_invoke
- ___39-[ACHClient removeTemplate:completion:]_block_invoke_2
- ___42-[ACHClient addEarnedInstance:completion:]_block_invoke
- ___42-[ACHClient addEarnedInstance:completion:]_block_invoke_2
- ___42-[ACHQuery client_deliverNewAchievements:]_block_invoke
- ___42-[ACHQuery client_deliverNewAchievements:]_block_invoke.288
- ___45-[ACHClient fetchAllTemplatesWithCompletion:]_block_invoke
- ___45-[ACHClient fetchAllTemplatesWithCompletion:]_block_invoke_2
- ___45-[ACHClient fetchAllTemplatesWithCompletion:]_block_invoke_3
- ___45-[ACHClient fetchAllTemplatesWithCompletion:]_block_invoke_4
- ___45-[ACHClient removeEarnedInstance:completion:]_block_invoke
- ___45-[ACHClient removeEarnedInstance:completion:]_block_invoke_2
- ___46-[ACHClient removeAllTemplatesWithCompletion:]_block_invoke
- ___46-[ACHClient removeAllTemplatesWithCompletion:]_block_invoke_2
- ___46-[ACHQuery client_deliverRemovedAchievements:]_block_invoke
- ___46-[ACHQuery client_deliverRemovedAchievements:]_block_invoke.290
- ___46-[ACHQuery client_deliverUpdatedAchievements:]_block_invoke
- ___46-[ACHQuery client_deliverUpdatedAchievements:]_block_invoke.289
- ___48-[ACHClient fetchAllAchievementsWithCompletion:]_block_invoke
- ___48-[ACHClient fetchAllAchievementsWithCompletion:]_block_invoke_2
- ___48-[ACHClient fetchAllAchievementsWithCompletion:]_block_invoke_3
- ___48-[ACHClient fetchAllAchievementsWithCompletion:]_block_invoke_4
- ___48-[ACHClient monthlyChallengeForDate:completion:]_block_invoke
- ___48-[ACHClient monthlyChallengeForDate:completion:]_block_invoke_2
- ___48-[ACHClient monthlyChallengeForDate:completion:]_block_invoke_3
- ___48-[ACHClient monthlyChallengeForDate:completion:]_block_invoke_4
- ___48-[ACHClient runMonthlyChallengesWithCompletion:]_block_invoke
- ___48-[ACHClient runMonthlyChallengesWithCompletion:]_block_invoke_2
- ___48-[ACHClient runMonthlyChallengesWithCompletion:]_block_invoke_3
- ___48-[ACHClient runMonthlyChallengesWithCompletion:]_block_invoke_4
- ___49-[ACHClient availableMobileAssetsWithCompletion:]_block_invoke
- ___49-[ACHClient availableMobileAssetsWithCompletion:]_block_invoke_2
- ___49-[ACHClient availableMobileAssetsWithCompletion:]_block_invoke_3
- ___49-[ACHClient availableMobileAssetsWithCompletion:]_block_invoke_4
- ___50-[ACHClient forceAwardingSchedulerWithCompletion:]_block_invoke
- ___50-[ACHClient forceAwardingSchedulerWithCompletion:]_block_invoke_2
- ___50-[ACHClient forceAwardingSchedulerWithCompletion:]_block_invoke_3
- ___50-[ACHClient forceAwardingSchedulerWithCompletion:]_block_invoke_4
- ___51-[ACHAchievement initWithTemplate:earnedInstances:]_block_invoke
- ___51-[ACHAchievement initWithTemplate:earnedInstances:]_block_invoke.cold.1
- ___51-[ACHClient fetchAllEarnedInstancesWithCompletion:]_block_invoke
- ___51-[ACHClient fetchAllEarnedInstancesWithCompletion:]_block_invoke_2
- ___51-[ACHClient fetchAllEarnedInstancesWithCompletion:]_block_invoke_3
- ___51-[ACHClient fetchAllEarnedInstancesWithCompletion:]_block_invoke_4
- ___52-[ACHClient removeAllEarnedInstancesWithCompletion:]_block_invoke
- ___52-[ACHClient removeAllEarnedInstancesWithCompletion:]_block_invoke_2
- ___53-[ACHQuery client_achievementsDidFinishInitialFetch:]_block_invoke
- ___53-[ACHQuery client_achievementsDidFinishInitialFetch:]_block_invoke.287
- ___53-[ACHQuery client_achievementsDidFinishInitialFetch:]_block_invoke.cold.1
- ___56-[ACHClient templateForMonthlyChallengeType:completion:]_block_invoke
- ___56-[ACHClient templateForMonthlyChallengeType:completion:]_block_invoke_2
- ___56-[ACHClient templateForMonthlyChallengeType:completion:]_block_invoke_3
- ___56-[ACHClient templateForMonthlyChallengeType:completion:]_block_invoke_4
- ___60-[ACHClient setActivityChallengeAssetsServerURL:completion:]_block_invoke
- ___60-[ACHClient setActivityChallengeAssetsServerURL:completion:]_block_invoke_2
- ___60-[ACHClient setActivityChallengeAssetsServerURL:completion:]_block_invoke_3
- ___60-[ACHClient setActivityChallengeAssetsServerURL:completion:]_block_invoke_4
- ___63-[ACHClient fetchAchievementWithTemplateUniqueName:completion:]_block_invoke
- ___63-[ACHClient fetchAchievementWithTemplateUniqueName:completion:]_block_invoke_2
- ___63-[ACHClient fetchAchievementWithTemplateUniqueName:completion:]_block_invoke_3
- ___63-[ACHClient fetchAchievementWithTemplateUniqueName:completion:]_block_invoke_4
- ___65-[ACHClient fetchActivityChallengeAssetsServerURLWithCompletion:]_block_invoke
- ___65-[ACHClient fetchActivityChallengeAssetsServerURLWithCompletion:]_block_invoke_2
- ___65-[ACHClient fetchActivityChallengeAssetsServerURLWithCompletion:]_block_invoke_3
- ___65-[ACHClient fetchActivityChallengeAssetsServerURLWithCompletion:]_block_invoke_4
- ___72-[ACHClient fetchEphemeralAchievementWithTemplateUniqueName:completion:]_block_invoke
- ___72-[ACHClient fetchEphemeralAchievementWithTemplateUniqueName:completion:]_block_invoke_2
- ___72-[ACHClient fetchEphemeralAchievementWithTemplateUniqueName:completion:]_block_invoke_3
- ___72-[ACHClient fetchEphemeralAchievementWithTemplateUniqueName:completion:]_block_invoke_4
- ___block_descriptor_40_e8_32bs_e17_v16?0"NSError"8ls32l8
- ___block_descriptor_40_e8_32s_e27_B16?0"ACHEarnedInstance"8ls32l8
- ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSArray"8ls40l8s32l8
- ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e20_v20?0B8"NSError"12ls40l8s32l8
- ___block_descriptor_48_e8_32s40bs_e27_v24?0"NSURL"8"NSError"16ls40l8s32l8
- ___block_descriptor_48_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16ls40l8s32l8
- ___block_descriptor_48_e8_32s40bs_e30_v16?0"<ACHServerInterface>"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e30_v16?0"<ACHServerInterface>"8ls40l8s32l8
- ___block_descriptor_48_e8_32s40bs_e33_v24?0"ACHTemplate"8"NSError"16ls40l8s32l8
- ___block_descriptor_48_e8_32s40bs_e36_v24?0"ACHAchievement"8"NSError"16ls40l8s32l8
- ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
- ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_49_e8_32s40bs_e5_v8?0ls40l8s32l8
- ___block_descriptor_56_e8_32s40bs48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40bs_e30_v16?0"<ACHServerInterface>"8ls40l8s32l8
- ___block_descriptor_56_e8_32s40s48bs_e30_v16?0"<ACHServerInterface>"8ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48bs_e30_v16?0"<ACHServerInterface>"8ls32l8s48l8s40l8
- ___block_literal_global.290
- ___block_literal_global.307
- ___block_literal_global.438
- ___block_literal_global.443
- ___block_literal_global.449
- ___block_literal_global.461
- ___block_literal_global.463
- ___block_literal_global.465
- ___block_literal_global.467
- ___block_literal_global.494
- ___block_literal_global.499
- ___block_literal_global.511
- ___block_literal_global.516
- _dispatch_assert_queue$V2
- _dispatch_assert_queue_not$V2
- _dispatch_sync
- _objc_msgSend$_clientQueueCompletion:
- _objc_msgSend$_remoteProxy:errorHandler:
- _objc_msgSend$_throwInvalidArgumentExceptionIfHasBeenExecuted:
- _objc_msgSend$collectionIntervals
- _objc_msgSend$decodeObjectOfClasses:forKey:
- _objc_msgSend$earnedInstances
- _objc_msgSend$errorHandler
- _objc_msgSend$fetchPluginProxyWithHandler:errorHandler:
- _objc_msgSend$hk_filter:
- _objc_msgSend$initWithHealthStore:pluginIdentifier:exportedObject:
- _objc_msgSend$initWithTemplate:earnedInstances:
- _objc_msgSend$initialAchievementsHandler
- _objc_msgSend$injectedErrorHandler
- _objc_msgSend$newAchievementsHandler
- _objc_msgSend$pluginProxyProvider
- _objc_msgSend$remote_addEarnedInstance:completion:
- _objc_msgSend$remote_addTemplate:completion:
- _objc_msgSend$remote_availableMobileAssetsWithCompletion:
- _objc_msgSend$remote_fetchAchievementWithTemplateUniqueName:completion:
- _objc_msgSend$remote_fetchActivityChallengeAssetsServerURLWithCompletion:
- _objc_msgSend$remote_fetchAllAchievementsWithCompletion:
- _objc_msgSend$remote_fetchEphemeralAchievementWithTemplateUniqueName:completion:
- _objc_msgSend$remote_forceAwardingSchedulerWithCompletion:
- _objc_msgSend$remote_monthlyChallengeForDate:completion:
- _objc_msgSend$remote_removeEarnedInstance:completion:
- _objc_msgSend$remote_removeTemplate:completion:
- _objc_msgSend$remote_runMonthlyChallengesWithCompletion:
- _objc_msgSend$remote_setActivityChallengeAssetsServerURL:completion:
- _objc_msgSend$remote_templateForMonthlyChallengeType:completion:
- _objc_msgSend$removedAchievementsHandler
- _objc_msgSend$serverQueue
- _objc_msgSend$setByAddingObject:
- _objc_msgSend$setCollectionIntervals:
- _objc_msgSend$setInitialAchievementsHandler:
- _objc_msgSend$setNewAchievementsHandler:
- _objc_msgSend$setPluginProxyProvider:
- _objc_msgSend$setRemovedAchievementsHandler:
- _objc_msgSend$setUpdatedAchievementsHandler:
- _objc_msgSend$setWithObject:
- _objc_msgSend$setWithObjects:
- _objc_msgSend$updatedAchievementsHandler
CStrings:
+ "-%02ld-%02ld"
+ "@\"HKCloudSyncObserver\""
+ "@\"HKHealthStore\""
+ "@\"NSDate\"16@0:8"
+ "ACHCloudSyncStatusProvider"
+ "ACHCloudSyncStatusProviderStatusChangeNotification"
+ "ACHCloudSyncStatusProviding"
+ "ACHCodableAchievementAnniversaryRequest"
+ "ACHCodableDateComponentsInterval"
+ "ACHCodableTemplateNameArray"
+ "Cloud Sync Observer Error: %@"
+ "Cloud Sync Observer Status Updated: %@"
+ "CloudRestoreStatusCheckEnabled"
+ "HKCloudSyncObserverDelegate"
+ "MonthlyChallengeType"
+ "T@\"HKCloudSyncObserver\",&,V_cloudSyncObserver"
+ "T@\"HKHealthStore\",&,V_healthStore"
+ "T@\"NSDate\",C,V_restoreCompletionDate"
+ "T@\"NSMutableArray\",&,N,V_templateNames"
+ "T@\"NSString\",&,N,V_dateComponents"
+ "T@\"NSString\",&,N,V_endDateComponents"
+ "T@\"NSString\",&,N,V_startDateComponents"
+ "_cloudRestoreStatusCheckEnabled"
+ "_cloudSyncObserver"
+ "_dateComponents"
+ "_healthStore"
+ "_lock"
+ "_restoreCompletionDate"
+ "_setError"
+ "_templateNames"
+ "activate"
+ "addTemplateNames:"
+ "boolForKey:"
+ "clearTemplateNames"
+ "cloudRestoreCompletionDate"
+ "cloudSyncObserver"
+ "cloudSyncObserver:didFailToPopulateStatusWithError:"
+ "cloudSyncObserver:syncCompletedForRequest:"
+ "cloudSyncObserver:syncDidStartWithProgress:"
+ "cloudSyncObserver:syncFailedForRequest:error:"
+ "cloudSyncObserver:syncFailedWithError:"
+ "cloudSyncObserver:syncStartedForRequest:withProgress:"
+ "cloudSyncObserverStatusUpdated:status:"
+ "cloudSyncObserverSyncCompleted:"
+ "currentCalendar"
+ "dataForKey:domain:error:"
+ "dateComponents"
+ "defaultCenter"
+ "distantPast"
+ "endDate"
+ "fetchEarnedInstancesForAnniversaryOfDateComponents:templateUniqueNames:error:"
+ "fetchEarnedInstancesForDateInterval:error:"
+ "getBytes:range:"
+ "hasDateComponents"
+ "hasEndDateComponents"
+ "hasError"
+ "hasStartDateComponents"
+ "healthStore"
+ "initWithCodableTemplateNames:"
+ "initWithHealthStore:delegate:"
+ "isInitialCloudRestoreComplete"
+ "position"
+ "postNotificationName:object:"
+ "remote_dataForKey:domain:completion:"
+ "remote_fetchEarnedInstancesForAnniversaryDateComponentsString:templateUniqueNames:completion:"
+ "remote_fetchEarnedInstancesForDateComponentStringsArray:completion:"
+ "remote_setData:forKey:domain:completion:"
+ "restoreCompletionDate"
+ "scheduler"
+ "setCloudSyncObserver:"
+ "setData:forKey:domain:error:"
+ "setDateComponents:"
+ "setEndDateComponents:"
+ "setHealthStore:"
+ "setPosition:"
+ "setRestoreCompletionDate:"
+ "setStartDateComponents:"
+ "setTemplateNames:"
+ "startDate"
+ "startObservingSyncStatus"
+ "status"
+ "syncEnabled"
+ "templateNames"
+ "templateNamesAtIndex:"
+ "templateNamesCount"
+ "templateNamesType"
+ "v24@0:8@\"HKCloudSyncObserver\"16"
+ "v24@?0@\"NSData\"8@\"NSError\"16"
+ "v32@0:8@\"HKCloudSyncObserver\"16@\"HKCloudSyncObserverStatus\"24"
+ "v32@0:8@\"HKCloudSyncObserver\"16@\"HKCloudSyncRequest\"24"
+ "v32@0:8@\"HKCloudSyncObserver\"16@\"NSError\"24"
+ "v32@0:8@\"HKCloudSyncObserver\"16@\"NSProgress\"24"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v40@0:8@\"HKCloudSyncObserver\"16@\"HKCloudSyncRequest\"24@\"NSError\"32"
+ "v40@0:8@\"HKCloudSyncObserver\"16@\"HKCloudSyncRequest\"24@\"NSProgress\"32"
+ "v40@0:8@\"NSString\"16@\"NSArray\"24@?<v@?@\"NSArray\"@\"NSError\">32"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSData\"@\"NSError\">32"
+ "v48@0:8@\"NSData\"16@\"NSString\"24@\"NSString\"32@?<v@?B@\"NSError\">40"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "@\"<ACHServerInterface>\""
- "@\"HKPluginProxyProvider\""
- "@48@0:8@?16@?24@?32@?40"
- "@?24@0:8@?16"
- "ACHClient"
- "ACHCurrentActivitySummaryQueryServerConfiguration"
- "ACHQuery"
- "ACHQuery initialAchievementsHandler not provided!"
- "ACHQueryClientInterface"
- "ACHServerInterface"
- "B16@?0@\"ACHEarnedInstance\"8"
- "Earned instance not added to achievement for template %{public}@: %{public}@"
- "Failed to fetch plugin proxy with error %{public}@"
- "Query finished initial fetch"
- "Query received [%lu] new achievements"
- "Query received [%lu] removed achievements"
- "Query received [%lu] updated achievements"
- "T@\"<ACHServerInterface>\",&,N,V_serverProxy"
- "T@\"HKPluginProxyProvider\",&,N,V_pluginProxyProvider"
- "T@\"NSArray\",R,V_earnedInstances"
- "T@\"NSDictionary\",&,N,V_collectionIntervals"
- "T@\"NSDictionary\",C,N,V_collectionIntervals"
- "T@?,C,N,V_errorHandler"
- "T@?,C,N,V_initialAchievementsHandler"
- "T@?,C,N,V_newAchievementsHandler"
- "T@?,C,N,V_removedAchievementsHandler"
- "T@?,C,N,V_updatedAchievementsHandler"
- "_clientQueueCompletion:"
- "_collectionIntervals"
- "_errorHandler"
- "_initialAchievementsHandler"
- "_newAchievementsHandler"
- "_pluginProxyProvider"
- "_remoteProxy:errorHandler:"
- "_removedAchievementsHandler"
- "_setCollectionIntervals:"
- "_throwInvalidArgumentExceptionIfHasBeenExecuted:"
- "_updatedAchievementsHandler"
- "addEarnedInstance:completion:"
- "addTemplate:completion:"
- "availableMobileAssetsWithCompletion:"
- "client_achievementsDidFinishInitialFetch:"
- "client_deliverNewAchievements:"
- "client_deliverRemovedAchievements:"
- "client_deliverUpdatedAchievements:"
- "collectionIntervals"
- "configurationClass"
- "configureClientInterface:"
- "decodeObjectOfClasses:forKey:"
- "errorHandler"
- "fetchAchievementWithTemplateUniqueName:completion:"
- "fetchActivityChallengeAssetsServerURLWithCompletion:"
- "fetchAllAchievementsWithCompletion:"
- "fetchAllEarnedInstancesWithCompletion:"
- "fetchAllTemplatesWithCompletion:"
- "fetchEphemeralAchievementWithTemplateUniqueName:completion:"
- "fetchPluginProxyWithHandler:errorHandler:"
- "forceAwardingSchedulerWithCompletion:"
- "hk_filter:"
- "initWithHealthStore:pluginIdentifier:exportedObject:"
- "initWithInitialAchievementsHandler:newAchievementsHandler:updatedAchievementsHandler:removedAchievementsHandler:"
- "initWithTemplate:earnedInstances:"
- "initialAchievementsHandler"
- "intervals"
- "monthlyChallengeForDate:completion:"
- "newAchievementsHandler"
- "pluginProxyProvider"
- "queue_populateConfiguration:"
- "remote_addEarnedInstance:completion:"
- "remote_addTemplate:completion:"
- "remote_availableMobileAssetsWithCompletion:"
- "remote_fetchAchievementWithTemplateUniqueName:completion:"
- "remote_fetchActivityChallengeAssetsServerURLWithCompletion:"
- "remote_fetchAllAchievementsWithCompletion:"
- "remote_fetchEphemeralAchievementWithTemplateUniqueName:completion:"
- "remote_forceAwardingSchedulerWithCompletion:"
- "remote_monthlyChallengeForDate:completion:"
- "remote_removeEarnedInstance:completion:"
- "remote_removeTemplate:completion:"
- "remote_runMonthlyChallengesWithCompletion:"
- "remote_setActivityChallengeAssetsServerURL:completion:"
- "remote_templateForMonthlyChallengeType:completion:"
- "removeAllEarnedInstancesWithCompletion:"
- "removeAllTemplatesWithCompletion:"
- "removeEarnedInstance:completion:"
- "removeTemplate:completion:"
- "removedAchievementsHandler"
- "runMonthlyChallengesWithCompletion:"
- "setActivityChallengeAssetsServerURL:completion:"
- "setByAddingObject:"
- "setCollectionIntervals:"
- "setErrorHandler:"
- "setInitialAchievementsHandler:"
- "setNewAchievementsHandler:"
- "setPluginProxyProvider:"
- "setRemovedAchievementsHandler:"
- "setUpdatedAchievementsHandler:"
- "setWithObject:"
- "setWithObjects:"
- "shallowCopyReplacingEarnedInstances:"
- "supportsTaskServers"
- "templateForMonthlyChallengeType:completion:"
- "updatedAchievementsHandler"
- "v16@?0@\"<ACHServerInterface>\"8"
- "v16@?0@\"NSArray\"8"
- "v24@0:8@\"NSSet\"16"
- "v24@0:8@?<v@?@\"NSArray\">16"
- "v24@0:8@?<v@?@\"NSURL\"@\"NSError\">16"
- "v24@?0@\"ACHAchievement\"8@\"NSError\"16"
- "v24@?0@\"ACHTemplate\"8@\"NSError\"16"
- "v24@?0@\"NSURL\"8@\"NSError\"16"
- "v32@0:8@\"ACHEarnedInstance\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"ACHTemplate\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"NSDate\"16@?<v@?@\"ACHTemplate\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"ACHAchievement\"@\"NSError\">24"
- "v32@0:8@\"NSURL\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@?16@?24"
- "v32@0:8Q16@?24"
- "v32@0:8Q16@?<v@?@\"ACHTemplate\"@\"NSError\">24"

```
