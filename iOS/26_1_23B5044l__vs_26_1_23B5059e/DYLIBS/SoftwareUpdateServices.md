## SoftwareUpdateServices

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices`

```diff

-950.40.24.0.0
-  __TEXT.__text: 0xaf8f8
-  __TEXT.__auth_stubs: 0xea0
-  __TEXT.__objc_methlist: 0xac7c
-  __TEXT.__const: 0x308
-  __TEXT.__cstring: 0x213cc
-  __TEXT.__gcc_except_tab: 0x1028
+950.40.42.0.0
+  __TEXT.__text: 0xb6868
+  __TEXT.__auth_stubs: 0xf60
+  __TEXT.__objc_methlist: 0xb1a4
+  __TEXT.__const: 0x310
+  __TEXT.__cstring: 0x22be4
+  __TEXT.__gcc_except_tab: 0x11f4
   __TEXT.__oslogstring: 0x85d
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x3178
-  __TEXT.__objc_classname: 0xf08
-  __TEXT.__objc_methname: 0x18d6e
-  __TEXT.__objc_methtype: 0x3450
-  __TEXT.__objc_stubs: 0x142c0
-  __DATA_CONST.__got: 0xd98
-  __DATA_CONST.__const: 0x29a0
-  __DATA_CONST.__objc_classlist: 0x3d8
+  __TEXT.__unwind_info: 0x3308
+  __TEXT.__objc_classname: 0xf4b
+  __TEXT.__objc_methname: 0x19d0c
+  __TEXT.__objc_methtype: 0x34fb
+  __TEXT.__objc_stubs: 0x14d60
+  __DATA_CONST.__got: 0xdc8
+  __DATA_CONST.__const: 0x2a48
+  __DATA_CONST.__objc_classlist: 0x3f0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5c28
+  __DATA_CONST.__objc_selrefs: 0x5f78
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x320
+  __DATA_CONST.__objc_superrefs: 0x330
   __DATA_CONST.__objc_arraydata: 0xa0
-  __AUTH_CONST.__auth_got: 0x760
-  __AUTH_CONST.__const: 0x780
-  __AUTH_CONST.__cfstring: 0x13060
-  __AUTH_CONST.__objc_const: 0x15880
-  __AUTH_CONST.__objc_intobj: 0x240
+  __AUTH_CONST.__auth_got: 0x7c0
+  __AUTH_CONST.__const: 0x7c0
+  __AUTH_CONST.__cfstring: 0x14620
+  __AUTH_CONST.__objc_const: 0x15f90
+  __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0xd8
-  __AUTH.__objc_data: 0x1018
-  __DATA.__objc_ivar: 0x95c
+  __AUTH.__objc_data: 0x1108
+  __DATA.__objc_ivar: 0x9b8
   __DATA.__data: 0xe98
-  __DATA.__bss: 0xe0
+  __DATA.__bss: 0x130
   __DATA_DIRTY.__objc_data: 0x1658
   __DATA_DIRTY.__bss: 0x1f0
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/MobileSoftwareUpdate
   - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi
+  - /System/Library/PrivateFrameworks/PersistentConnection.framework/PersistentConnection
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 6BDCA87E-8F21-3D51-9E90-7B94DE695524
-  Functions: 4475
-  Symbols:   14855
-  CStrings:  10144
+  UUID: EA09EAB7-C77B-3097-B2CA-F69A4A77708A
+  Functions: 4596
+  Symbols:   15288
+  CStrings:  10681
 
Symbols:
+ +[SUAnalyticsManager sharedManagerWithPath:]
+ +[SUSHistoryEvent supportsSecureCoding]
+ +[SUSHistoryInstalls sharedInstanceWithPath:]
+ +[SUSHistoryTracker historyOperationName]
+ +[SUSHistoryTracker nameForHistoryType:]
+ +[SUSHistoryTracker sharedTracker]
+ +[SUSHistoryTracker sharedTracker].cold.1
+ +[SUSHistoryTracker trackerWithPath:]
+ +[SUUtility compareVersionExtra:withVersionExtra:]
+ +[SUUtility currentProductVersionExtra]
+ +[SUUtility currentProductVersionExtra].cold.1
+ -[SUAnalyticsEvent _queue_addEventPayloadEntries:]
+ -[SUAnalyticsEvent addEventPayloadEntries:]
+ -[SUAutoInstallManager installDidFail:withError:]
+ -[SUAutoInstallManager installDidFinish:]
+ -[SUAutoInstallOperation setCanceled:]
+ -[SUAutoInstallOperation setExpired:]
+ -[SUDescriptor matchesDescriptor:comparisonFlags:reason:]
+ -[SUDescriptor minFreeSpacePostStageOptionalAssets]
+ -[SUDescriptor setMinFreeSpacePostStageOptionalAssets:]
+ -[SUDownload(Scanner) matchesScanResults:]
+ -[SUManagerClient fetchInstallHistory:]
+ -[SUManagerCore _checkAndPostSplatFollowUpIfNeeded]
+ -[SUManagerCore resumeOrDisableReserveSpace]
+ -[SUManagerCore scheduleSplatFollowUpDate:]
+ -[SUManagerCore setTracker:]
+ -[SUManagerCore tracker]
+ -[SUManagerCore(Analytics) _preallocatedSpaceMetricInfo]
+ -[SUManagerPolicy checkAndPostSplatFollowUpIfNeeded]
+ -[SUManagerPolicy initWithCore:]
+ -[SUManagerServer fetchInstallHistory:]
+ -[SUManagerServer historyTracker]
+ -[SUPreferences enableRapidReturnToService]
+ -[SUPreferences setEnableRapidReturnToService:]
+ -[SUPreferences setSplatFollowUpDelayOverride:]
+ -[SUPreferences splatFollowUpDelayOverride]
+ -[SUSHistoryEvent .cxx_destruct]
+ -[SUSHistoryEvent description]
+ -[SUSHistoryEvent encodeWithCoder:]
+ -[SUSHistoryEvent eventPayload]
+ -[SUSHistoryEvent extraInfo]
+ -[SUSHistoryEvent historyProtectionQueue]
+ -[SUSHistoryEvent historyType]
+ -[SUSHistoryEvent initWithCoder:]
+ -[SUSHistoryEvent initWithOperation:historyType:extraInfo:]
+ -[SUSHistoryEvent operation]
+ -[SUSHistoryEvent timestamp]
+ -[SUSHistoryEvent toAnalytics]
+ -[SUSHistoryInstalls .cxx_destruct]
+ -[SUSHistoryInstalls addLogWithName:build:date:operationType:]
+ -[SUSHistoryInstalls initializeDatabase]
+ -[SUSHistoryInstalls path]
+ -[SUSHistoryInstalls persistentContainer]
+ -[SUSHistoryInstalls queryAllLogs]
+ -[SUSHistoryInstalls queryLogsFromDate:toDate:]
+ -[SUSHistoryInstalls setPath:]
+ -[SUSHistoryTracker .cxx_destruct]
+ -[SUSHistoryTracker analyticsManager]
+ -[SUSHistoryTracker analyticsSubmissionQueue]
+ -[SUSHistoryTracker analyticsSubmissionTimer]
+ -[SUSHistoryTracker appendToString:key:value:]
+ -[SUSHistoryTracker basePath]
+ -[SUSHistoryTracker coreAnalyticsPath]
+ -[SUSHistoryTracker dealloc]
+ -[SUSHistoryTracker description]
+ -[SUSHistoryTracker descriptorFromRollbackDescriptor:]
+ -[SUSHistoryTracker eventQueue]
+ -[SUSHistoryTracker fetchInstallHistory]
+ -[SUSHistoryTracker formatDownloadEvent:]
+ -[SUSHistoryTracker formatErrorEvent:]
+ -[SUSHistoryTracker formatInstallEvent:]
+ -[SUSHistoryTracker formatScanEvent:]
+ -[SUSHistoryTracker formatSpaceEvent:]
+ -[SUSHistoryTracker handleAnalyticsSubmissionTimer:]
+ -[SUSHistoryTracker historyInstallDBPath]
+ -[SUSHistoryTracker historyLogPath]
+ -[SUSHistoryTracker historyTypeName]
+ -[SUSHistoryTracker historyType]
+ -[SUSHistoryTracker initUsingProtectionQueue:withBasePath:]
+ -[SUSHistoryTracker installHistoryManager]
+ -[SUSHistoryTracker invalidateAnalyticsSubmissionTimer]
+ -[SUSHistoryTracker protectionQueue]
+ -[SUSHistoryTracker recordAutoScanAndDownloadIfAvailable:downloadNow:fromClient:]
+ -[SUSHistoryTracker recordDownloadCompleted:withError:]
+ -[SUSHistoryTracker recordDownloadStarted:fromClient:]
+ -[SUSHistoryTracker recordHistoryEvent:]
+ -[SUSHistoryTracker recordInstallCompleted:withError:]
+ -[SUSHistoryTracker recordInstallStarted:withDownload:]
+ -[SUSHistoryTracker recordRollbackCompleted:withError:]
+ -[SUSHistoryTracker recordRollbackStarted:]
+ -[SUSHistoryTracker recordScanComplete:downloadNow:withError:]
+ -[SUSHistoryTracker recordScanForUpdates:fromClient:]
+ -[SUSHistoryTracker setAnalyticsSubmissionTimer:]
+ -[SUSHistoryTracker setBasePath:]
+ -[SUSHistoryTracker setCoreAnalyticsPath:]
+ -[SUSHistoryTracker setEventQueue:]
+ -[SUSHistoryTracker setHistoryInstallDBPath:]
+ -[SUSHistoryTracker setHistoryLogPath:]
+ -[SUSHistoryTracker setupAnalyticsSubmissionTimer]
+ -[SUSHistoryTracker submitHistoryAnalyticsEvent]
+ -[SUSHistoryTracker updateInstallHistory:build:date:operationType:]
+ -[SUScanOptions scanForSplatIfNecessary]
+ -[SUScanOptions setScanForSplatIfNecessary:]
+ -[SUScheduler _queue_handleSplatFollowUp:info:]
+ -[SUScheduler autoInstallManager]
+ -[SUScheduler cancelAllAutoScanTasks]
+ -[SUScheduler cancelSplatFollowUpNotification]
+ -[SUScheduler manager]
+ -[SUScheduler scheduleSplatFollowUpNotification:]
+ -[SUScheduler schedulerQueue]
+ -[SUScheduler serverConfigManager]
+ -[SUScheduler setAutoInstallManager:]
+ -[SUScheduler setManager:]
+ -[SUScheduler setSchedulerQueue:]
+ -[SUScheduler setServerConfigManager:]
+ -[SUState lastPendingSplatAlertDate]
+ -[SUState lastProductVersionExtra]
+ -[SUState setLastPendingSplatAlertDate:]
+ -[SUState setLastProductVersionExtra:]
+ GCC_except_table101
+ GCC_except_table105
+ GCC_except_table107
+ GCC_except_table113
+ GCC_except_table123
+ GCC_except_table125
+ GCC_except_table129
+ GCC_except_table131
+ GCC_except_table137
+ GCC_except_table147
+ GCC_except_table149
+ GCC_except_table210
+ GCC_except_table218
+ GCC_except_table231
+ GCC_except_table236
+ GCC_except_table244
+ GCC_except_table25
+ GCC_except_table262
+ GCC_except_table29
+ GCC_except_table296
+ GCC_except_table297
+ GCC_except_table298
+ GCC_except_table344
+ GCC_except_table446
+ GCC_except_table50
+ GCC_except_table75
+ GCC_except_table80
+ GCC_except_table88
+ OBJC_IVAR_$_SUState._lastPendingSplatAlertDate
+ OBJC_IVAR_$_SUState._lastProductVersionExtra
+ _NSTemporaryDirectory
+ _OBJC_CLASS_$_MDMConfiguration
+ _OBJC_CLASS_$_NSFileHandle
+ _OBJC_CLASS_$_NSJSONSerialization
+ _OBJC_CLASS_$_PCPersistentTimer
+ _OBJC_CLASS_$_SUSHistoryEvent
+ _OBJC_CLASS_$_SUSHistoryInstalls
+ _OBJC_CLASS_$_SUSHistoryTracker
+ _OBJC_IVAR_$_SUDescriptor._minFreeSpacePostStageOptionalAssets
+ _OBJC_IVAR_$_SUManagerCore._tracker
+ _OBJC_IVAR_$_SUManagerServer._historyTracker
+ _OBJC_IVAR_$_SUSHistoryEvent._eventPayload
+ _OBJC_IVAR_$_SUSHistoryEvent._extraInfo
+ _OBJC_IVAR_$_SUSHistoryEvent._historyProtectionQueue
+ _OBJC_IVAR_$_SUSHistoryEvent._historyType
+ _OBJC_IVAR_$_SUSHistoryEvent._operation
+ _OBJC_IVAR_$_SUSHistoryEvent._timestamp
+ _OBJC_IVAR_$_SUSHistoryInstalls._db
+ _OBJC_IVAR_$_SUSHistoryInstalls._path
+ _OBJC_IVAR_$_SUSHistoryInstalls._persistentContainer
+ _OBJC_IVAR_$_SUSHistoryTracker._analyticsManager
+ _OBJC_IVAR_$_SUSHistoryTracker._analyticsSubmissionQueue
+ _OBJC_IVAR_$_SUSHistoryTracker._analyticsSubmissionTimer
+ _OBJC_IVAR_$_SUSHistoryTracker._basePath
+ _OBJC_IVAR_$_SUSHistoryTracker._coreAnalyticsPath
+ _OBJC_IVAR_$_SUSHistoryTracker._eventQueue
+ _OBJC_IVAR_$_SUSHistoryTracker._historyInstallDBPath
+ _OBJC_IVAR_$_SUSHistoryTracker._historyLogPath
+ _OBJC_IVAR_$_SUSHistoryTracker._historyType
+ _OBJC_IVAR_$_SUSHistoryTracker._installHistoryManager
+ _OBJC_IVAR_$_SUSHistoryTracker._protectionQueue
+ _OBJC_IVAR_$_SUScanOptions._scanForSplatIfNecessary
+ _OBJC_METACLASS_$_SUSHistoryEvent
+ _OBJC_METACLASS_$_SUSHistoryInstalls
+ _OBJC_METACLASS_$_SUSHistoryTracker
+ _SUActivityNameSplatFollowUp
+ __OBJC_$_CLASS_METHODS_SUSHistoryEvent
+ __OBJC_$_CLASS_METHODS_SUSHistoryInstalls
+ __OBJC_$_CLASS_METHODS_SUSHistoryTracker
+ __OBJC_$_CLASS_PROP_LIST_SUSHistoryEvent
+ __OBJC_$_INSTANCE_METHODS_SUDownload(Scanner)
+ __OBJC_$_INSTANCE_METHODS_SUSHistoryEvent
+ __OBJC_$_INSTANCE_METHODS_SUSHistoryInstalls
+ __OBJC_$_INSTANCE_METHODS_SUSHistoryTracker
+ __OBJC_$_INSTANCE_VARIABLES_SUSHistoryEvent
+ __OBJC_$_INSTANCE_VARIABLES_SUSHistoryInstalls
+ __OBJC_$_INSTANCE_VARIABLES_SUSHistoryTracker
+ __OBJC_$_PROP_LIST_SUSHistoryEvent
+ __OBJC_$_PROP_LIST_SUSHistoryInstalls
+ __OBJC_$_PROP_LIST_SUSHistoryTracker
+ __OBJC_CLASS_PROTOCOLS_$_SUSHistoryEvent
+ __OBJC_CLASS_RO_$_SUSHistoryEvent
+ __OBJC_CLASS_RO_$_SUSHistoryInstalls
+ __OBJC_CLASS_RO_$_SUSHistoryTracker
+ __OBJC_METACLASS_RO_$_SUSHistoryEvent
+ __OBJC_METACLASS_RO_$_SUSHistoryInstalls
+ __OBJC_METACLASS_RO_$_SUSHistoryTracker
+ ___32-[SUInstaller installCompleted:]_block_invoke.387
+ ___32-[SUInstaller installCompleted:]_block_invoke_2.388
+ ___32-[SUInstaller installCompleted:]_block_invoke_3.394
+ ___32-[SUInstaller installCompleted:]_block_invoke_4.395
+ ___34+[SUSHistoryTracker sharedTracker]_block_invoke
+ ___34-[SUState lastProductVersionExtra]_block_invoke
+ ___36-[SUState lastPendingSplatAlertDate]_block_invoke
+ ___37+[SUSHistoryTracker trackerWithPath:]_block_invoke
+ ___38-[SUState setLastProductVersionExtra:]_block_invoke
+ ___39+[SUUtility currentProductVersionExtra]_block_invoke
+ ___39-[SUManagerClient fetchInstallHistory:]_block_invoke
+ ___39-[SUManagerClient fetchInstallHistory:]_block_invoke_2
+ ___39-[SUManagerServer fetchInstallHistory:]_block_invoke
+ ___39-[SUManagerServer fetchInstallHistory:]_block_invoke_2
+ ___39-[SUManagerServer fetchInstallHistory:]_block_invoke_3
+ ___40-[SUSHistoryTracker recordHistoryEvent:]_block_invoke
+ ___40-[SUState setLastPendingSplatAlertDate:]_block_invoke
+ ___41-[SUAutoInstallManager installDidFinish:]_block_invoke
+ ___41-[SUAutoInstallManager installDidFinish:]_block_invoke_2
+ ___43-[SUAnalyticsEvent addEventPayloadEntries:]_block_invoke
+ ___44+[SUAnalyticsManager sharedManagerWithPath:]_block_invoke
+ ___45+[SUSHistoryInstalls sharedInstanceWithPath:]_block_invoke
+ ___46-[SUScheduler cancelSplatFollowUpNotification]_block_invoke
+ ___47-[SUScheduler _queue_handleSplatFollowUp:info:]_block_invoke
+ ___52-[SUManagerPolicy checkAndPostSplatFollowUpIfNeeded]_block_invoke
+ ___67-[SUScanner autoScanAndDownloadIfAvailable:downloadNow:withResult:]_block_invoke_7
+ ___86-[SUManagerCore updatesDownloadableWithOptions:alternateDownloadOptions:replyHandler:]_block_invoke.498
+ ___block_descriptor_48_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e26_v16?0"SUCoreDescriptor"8ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls64l8s32l8s40l8s48l8s56l8
+ ___block_literal_global.344
+ ___block_literal_global.357
+ ___block_literal_global.365
+ ___block_literal_global.397
+ ___block_literal_global.399
+ ___block_literal_global.405
+ ___block_literal_global.411
+ ___block_literal_global.433
+ ___block_literal_global.473
+ ___block_literal_global.520
+ ___block_literal_global.545
+ ___block_literal_global.550
+ ___block_literal_global.588
+ ___block_literal_global.602
+ ___block_literal_global.630
+ ___block_literal_global.637
+ _currentProductVersionExtra.__currentProductVersionExtra
+ _currentProductVersionExtra.productVersionExtraPredicate
+ _kSUSHistoryAlternateBuildInfo
+ _kSUSHistoryAlternateVersionInfo
+ _kSUSHistoryAppOffloadEnabled
+ _kSUSHistoryCacheDeleteEnabled
+ _kSUSHistoryDescriptor
+ _kSUSHistoryDisplayNameInfo
+ _kSUSHistoryDownloadNow
+ _kSUSHistoryError
+ _kSUSHistoryEventName
+ _kSUSHistoryIdentifier
+ _kSUSHistoryIsBackground
+ _kSUSHistoryIsSplat
+ _kSUSHistoryIsSplombo
+ _kSUSHistoryPreferredBuildInfo
+ _kSUSHistoryPreferredVersionInfo
+ _kSUSHistoryProductVersionExtra
+ _kSUSHistorySoftwareUpdateType
+ _kSUSHistoryTargetBuildInfo
+ _kSUSHistoryTargetVersionInfo
+ _kSUSHistoryUserInitiated
+ _objc_msgSend$_checkAndPostSplatFollowUpIfNeeded
+ _objc_msgSend$_preallocatedSpaceMetricInfo
+ _objc_msgSend$_queue_addEventPayloadEntries:
+ _objc_msgSend$_queue_handleSplatFollowUp:info:
+ _objc_msgSend$addEventPayloadEntries:
+ _objc_msgSend$addLogWithName:build:date:operationType:
+ _objc_msgSend$analyticsManager
+ _objc_msgSend$analyticsSubmissionQueue
+ _objc_msgSend$appendToString:key:value:
+ _objc_msgSend$basePath
+ _objc_msgSend$cancelAllAutoScanTasks
+ _objc_msgSend$cancelSplatFollowUpNotification
+ _objc_msgSend$checkAndPostSplatFollowUpIfNeeded
+ _objc_msgSend$closeFile
+ _objc_msgSend$compareVersionExtra:withVersionExtra:
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$contentsOfDirectoryAtPath:error:
+ _objc_msgSend$coreAnalyticsPath
+ _objc_msgSend$currentProductVersionExtra
+ _objc_msgSend$dataWithJSONObject:options:error:
+ _objc_msgSend$descriptorFromRollbackDescriptor:
+ _objc_msgSend$enableRapidReturnToService
+ _objc_msgSend$eventQueue
+ _objc_msgSend$extraInfo
+ _objc_msgSend$fetchInstallHistory
+ _objc_msgSend$fetchInstallHistory:
+ _objc_msgSend$fileHandleForWritingAtPath:
+ _objc_msgSend$fileSize
+ _objc_msgSend$formatDownloadEvent:
+ _objc_msgSend$formatErrorEvent:
+ _objc_msgSend$formatInstallEvent:
+ _objc_msgSend$formatScanEvent:
+ _objc_msgSend$formatSpaceEvent:
+ _objc_msgSend$historyInstallDBPath
+ _objc_msgSend$historyLogPath
+ _objc_msgSend$historyOperationName
+ _objc_msgSend$historyTracker
+ _objc_msgSend$historyType
+ _objc_msgSend$initUsingProtectionQueue:withBasePath:
+ _objc_msgSend$initWithData:encoding:
+ _objc_msgSend$initWithOperation:historyType:extraInfo:
+ _objc_msgSend$initWithPath:
+ _objc_msgSend$initWithTimeInterval:serviceIdentifier:target:selector:userInfo:
+ _objc_msgSend$initializeDatabase
+ _objc_msgSend$installHistoryManager
+ _objc_msgSend$invalidateAnalyticsSubmissionTimer
+ _objc_msgSend$isRapidReturnToService
+ _objc_msgSend$isReturnToServiceModeActive
+ _objc_msgSend$lastPendingSplatAlertDate
+ _objc_msgSend$lastProductVersionExtra
+ _objc_msgSend$lengthOfBytesUsingEncoding:
+ _objc_msgSend$matchesDescriptor:comparisonFlags:reason:
+ _objc_msgSend$matchesScanResults:
+ _objc_msgSend$minFreeSpacePostStageOptionalAssets
+ _objc_msgSend$nameForHistoryType:
+ _objc_msgSend$objCType
+ _objc_msgSend$operation
+ _objc_msgSend$protectionQueue
+ _objc_msgSend$queryAllLogs
+ _objc_msgSend$recordAutoScanAndDownloadIfAvailable:downloadNow:fromClient:
+ _objc_msgSend$recordDownloadCompleted:withError:
+ _objc_msgSend$recordDownloadStarted:fromClient:
+ _objc_msgSend$recordHistoryEvent:
+ _objc_msgSend$recordInstallCompleted:withError:
+ _objc_msgSend$recordInstallStarted:withDownload:
+ _objc_msgSend$recordRollbackCompleted:withError:
+ _objc_msgSend$recordRollbackStarted:
+ _objc_msgSend$recordScanComplete:downloadNow:withError:
+ _objc_msgSend$recordScanForUpdates:fromClient:
+ _objc_msgSend$removeEvent:
+ _objc_msgSend$resumeOrDisableReserveSpace
+ _objc_msgSend$scanForSplatIfNecessary
+ _objc_msgSend$scheduleInQueue:
+ _objc_msgSend$scheduleSplatFollowUpDate:
+ _objc_msgSend$scheduleSplatFollowUpNotification:
+ _objc_msgSend$seekToEndReturningOffset:error:
+ _objc_msgSend$setLastPendingSplatAlertDate:
+ _objc_msgSend$setLastProductVersionExtra:
+ _objc_msgSend$setMinFreeSpacePostStageOptionalAssets:
+ _objc_msgSend$setPath:
+ _objc_msgSend$setScanForSplatIfNecessary:
+ _objc_msgSend$setupAnalyticsSubmissionTimer
+ _objc_msgSend$sharedInstanceWithPath:
+ _objc_msgSend$sharedManagerWithPath:
+ _objc_msgSend$sharedTracker
+ _objc_msgSend$sortedArrayUsingSelector:
+ _objc_msgSend$splatFollowUpDelayOverride
+ _objc_msgSend$stringWithContentsOfFile:encoding:error:
+ _objc_msgSend$submitHistoryAnalyticsEvent
+ _objc_msgSend$timestamp
+ _objc_msgSend$toAnalytics
+ _objc_msgSend$tracker
+ _objc_msgSend$updateInstallHistory:build:date:operationType:
+ _objc_msgSend$writeData:error:
+ _objc_msgSend$writeToFile:atomically:encoding:error:
+ _sharedInstanceWithPath:.onceToken
+ _sharedInstanceWithPath:.sharedInstance
+ _sharedManagerWithPath:.__manager
+ _sharedManagerWithPath:.onceToken
+ _sharedTracker.onceToken
+ _sharedTracker.sharedInstance
+ _sqlite3_bind_int64
+ _sqlite3_bind_text
+ _sqlite3_column_int64
+ _sqlite3_column_text
+ _sqlite3_errmsg
+ _sqlite3_exec
+ _sqlite3_finalize
+ _sqlite3_free
+ _sqlite3_open
+ _sqlite3_prepare_v2
+ _sqlite3_step
+ _trackerWithPath:.onceToken
+ _trackerWithPath:.sharedInstance
- +[SUAutoInstallOperation supportsSecureCoding]
- +[SUManagerEngine SUDescriptor:matchesSUCoreDescriptor:comparisonFlags:]
- -[SUAutoInstallForecast firstUnlock]
- -[SUAutoInstallForecast setFirstUnlock:]
- -[SUAutoInstallManager isAutoDownload]
- -[SUAutoInstallManager noteInstallDidFail:withError:]
- -[SUAutoInstallManager noteInstallDidFinish:]
- -[SUAutoInstallOperation _initWithClient:clientOwned:id:forecast:agreementStatus:cancelled:expired:]
- -[SUAutoInstallOperation _initWithClient:clientOwned:id:forecast:agreementStatus:cancelled:expired:].cold.1
- -[SUAutoInstallOperation _initWithClient:clientOwned:id:forecast:agreementStatus:cancelled:expired:].cold.2
- -[SUAutoInstallOperation encodeWithCoder:]
- -[SUAutoInstallOperation initWithCoder:]
- -[SUManagerCore resumeReserveSpaceStateIfNeeded]
- -[SUScheduler _autoScanTimeInterval]
- -[SUScheduler cancelAllAutoscanTasks]
- -[_SUAutoInstallOperationModel setWaitingUntilDownloadComplete:]
- -[_SUAutoInstallOperationModel waitingUntilDownloadComplete]
- GCC_except_table102
- GCC_except_table104
- GCC_except_table110
- GCC_except_table118
- GCC_except_table120
- GCC_except_table122
- GCC_except_table126
- GCC_except_table128
- GCC_except_table134
- GCC_except_table144
- GCC_except_table146
- GCC_except_table201
- GCC_except_table212
- GCC_except_table228
- GCC_except_table233
- GCC_except_table238
- GCC_except_table256
- GCC_except_table290
- GCC_except_table292
- GCC_except_table294
- GCC_except_table341
- GCC_except_table441
- GCC_except_table49
- GCC_except_table51
- GCC_except_table73
- GCC_except_table78
- GCC_except_table86
- GCC_except_table98
- _OBJC_IVAR_$_SUAutoInstallForecast._firstUnlock
- _OBJC_IVAR_$_SUAutoInstallOperation._clientOwned
- _OBJC_IVAR_$__SUAutoInstallOperationModel._waitingUntilDownloadComplete
- __OBJC_$_CLASS_METHODS_SUAutoInstallOperation
- __OBJC_$_CLASS_PROP_LIST_SUAutoInstallOperation
- __OBJC_$_INSTANCE_METHODS_SUDownload
- ___32-[SUInstaller installCompleted:]_block_invoke.384
- ___32-[SUInstaller installCompleted:]_block_invoke_2.385
- ___32-[SUInstaller installCompleted:]_block_invoke_3.391
- ___45-[SUAutoInstallManager noteInstallDidFinish:]_block_invoke
- ___45-[SUAutoInstallManager noteInstallDidFinish:]_block_invoke_2
- ___61-[SURollbackController rollbackUpdateWithOptions:completion:]_block_invoke_5
- ___61-[SURollbackController rollbackUpdateWithOptions:completion:]_block_invoke_6
- ___86-[SUManagerCore updatesDownloadableWithOptions:alternateDownloadOptions:replyHandler:]_block_invoke.494
- ___block_descriptor_48_e8_32s40s_e26_v16?0"SUCoreDescriptor"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40w_e8_v12?0i8ls32l8w40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e45_v28?0B8"SURollbackDescriptor"12"NSError"20ls32l8s56l8s40l8s48l8
- ___block_descriptor_81_e8_32s40s48s56s64s72bs_e5_v8?0ls72l8s32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.347
- ___block_literal_global.360
- ___block_literal_global.396
- ___block_literal_global.398
- ___block_literal_global.404
- ___block_literal_global.410
- ___block_literal_global.432
- ___block_literal_global.463
- ___block_literal_global.510
- ___block_literal_global.535
- ___block_literal_global.540
- ___block_literal_global.574
- ___block_literal_global.593
- ___block_literal_global.615
- ___block_literal_global.625
- _objc_msgSend$SUDescriptor:matchesSUCoreDescriptor:comparisonFlags:
- _objc_msgSend$_initWithClient:clientOwned:id:forecast:agreementStatus:cancelled:expired:
- _objc_msgSend$cancelAllAutoscanTasks
- _objc_msgSend$firstUnlock
- _objc_msgSend$noteInstallDidFail:withError:
- _objc_msgSend$noteInstallDidFinish:
- _objc_msgSend$resumeReserveSpaceStateIfNeeded
- _objc_msgSend$setFirstUnlock:
- _objc_msgSend$setWaitingUntilDownloadComplete:
- _objc_msgSend$waitingUntilDownloadComplete
CStrings:
+ "\n            ClientName: %@\n            Identifier: %@\n            Forced: %@\n            ScanType: %d\n            CollectDoc: %@\n            ScanForSplat: %@\n            Types: %@\n            Requested PMV: %@\n            Requested Build: %@\n            SessionID: %@\n            MDM use delay: %@\n            MDM show RSR: %@\n            =============== MDM: %@ \n            ===================\n            Ignore NoUpdateFound response: %@\n"
+ "\n            Publisher: %@\n            HumanReadableUpdateName: %@\n            ProductSystemName: %@\n            ProductVersion: %@\n            ProductVersionExtra: %@\n            ProductBuildVersion: %@\n            PrerequisiteBuild: %@\n            PrerequisiteOS: %@\n            ReleaseType: %@\n            DownloadSize: %llu\n            UnarchiveSize: %llu\n            MSUPrepareSize: %llu\n            PreparationSize: %llu\n            InstallationSize: %llu\n            PreSUStagingRequiredSize: %llu\n            PreSUStagingOptionalSize: %llu\n            MinFreeSpacePostStageOptionalAssets: %llu\n            UnentitledReserveAmount: %llu\n            UpdateType: %@\n            Downloadable: %@\n            DownloadableOverCellular: %@\n            AutoDownloadableOverCellular: %@\n            AutoUpdateEnabled: %@\n            StreamingZipCapable: %@\n            TotalRequiredFreeSpace: %llu\n            Documentation: %@\n            SiriVoiceDeletion: %d\n            CDLevel4DeletionDisabled: %d\n            appDemotionDisabled: %d\n            maSuspensionDisabled: %d\n            installTonightDisabled: %d\n            rampEnabled: %d\n            granularlyRamped: %d\n            setupCritical: %@\n            criticalOutOfBoxOnly: %d\n            criticalDownloadPolicy: %@\n            releaseDate: %@\n            mdmDelayInterval: %llu\n            assetID: %@\n            hideInstallAlert: %@\n            audienceType: %@\n            preferenceType: %@\n            upgradeType: %@\n            promoteAlternateUpdate: %@\n            isSplatOnly: %@\n            mandatoryUpdateEligible: %@\n            mandatoryUpdateVersionMin: %@\n            mandatoryUpdateVersionMax: %@\n            mandatoryUpdateOptional: %@\n            mandatoryUpdateRestrictedToOutOfTheBox: %@\n            forcePasscodeRequired: %@\n            allowAutoDownloadOnBattery: %@\n            autoDownloadOnBatteryDelay: %u\n            autoDownloadOnBatteryMinbattery: %u%%\n            isSplombo: %@\n            splatComboBuildVersion: %@"
+ " %@"
+ "%@ 'PSUS' ([%llu,%llu] != [%llu,%llu])"
+ "%@ 'Splombo' ([%d, %@] != [%d, %@])"
+ "%@ 'prerequisite OS version' (%@ != %@)"
+ "%@ 'prerequisite build' (%@ != %@)"
+ "%@ 'product build version' (%@ != %@)"
+ "%@ 'product system name' (%@ != %@)"
+ "%@ 'product version' (%@ != %@)"
+ "%@ 'release type' (%@ != %@)"
+ "%@ (download) doesn't match %@ (alternate): %@"
+ "%@ (download) doesn't match %@ (preferred): %@"
+ "%@%@:%@ "
+ "%@(SU) and %@(SU) differ in"
+ "%@(SU) and %@(SUCore) differ in"
+ "%@_%@_%@%s"
+ "%s - [DDM] Fall back to a scan for Splat updates"
+ "%s - [DDM] Fall back to a scan for regular updates"
+ "%s Error converting dictionary to string: %@"
+ "%s Recording unknown type log: %ld"
+ "%s entry: %@"
+ "%s history analytics event: %@"
+ "%s: 24-hour persistent timer fired, submitting analytics"
+ "%s: Analytics submission persistent timer invalidated"
+ "%s: Analytics submission persistent timer scheduled to fire every 24 hours"
+ "%s: DB created"
+ "%s: Entry Name: %@ | Version: %@ | Date: %@"
+ "%s: Error creating table: %s"
+ "%s: Error opening database"
+ "%s: Failed to create new file handle after trimming"
+ "%s: Failed to insert log"
+ "%s: Failed to prepare insert: %s"
+ "%s: Failed to read log file for trimming: %@"
+ "%s: Failed to seek to end of SUSHistory file: %@"
+ "%s: Failed to submit some or all events"
+ "%s: Failed to trim old log entries: %s"
+ "%s: Failed to write SUSHistory entry: %@"
+ "%s: Failed to write trimmed log: %@"
+ "%s: Fetching Install History"
+ "%s: Log file exceeds max size (%llu + %lu > %d), trimming..."
+ "%s: Scans not allowed in RRTS mode"
+ "%s: Splombo is disabled"
+ "%s: Success entry insert"
+ "%s: Successfully submitted all queued events"
+ "%s: Trimmed log to %lu bytes (will be %lu bytes after adding new entry)"
+ "%s: Trimmed logs to most recent %d entries"
+ "%s: failed to query database"
+ "%s: query database success"
+ "-[SUManagerClient fetchInstallHistory:]"
+ "-[SUManagerClient fetchInstallHistory:]_block_invoke"
+ "-[SUManagerServer fetchInstallHistory:]_block_invoke"
+ "-[SURollbackController rollbackUpdateWithOptions:completion:]_block_invoke"
+ "-[SURollbackController rollbackUpdateWithOptions:completion:]_block_invoke_4"
+ "-[SUSHistoryEvent description]"
+ "-[SUSHistoryEvent toAnalytics]"
+ "-[SUSHistoryInstalls addLogWithName:build:date:operationType:]"
+ "-[SUSHistoryInstalls initializeDatabase]"
+ "-[SUSHistoryInstalls queryAllLogs]"
+ "-[SUSHistoryInstalls queryLogsFromDate:toDate:]"
+ "-[SUSHistoryTracker fetchInstallHistory]"
+ "-[SUSHistoryTracker handleAnalyticsSubmissionTimer:]"
+ "-[SUSHistoryTracker invalidateAnalyticsSubmissionTimer]"
+ "-[SUSHistoryTracker recordHistoryEvent:]_block_invoke"
+ "-[SUSHistoryTracker setupAnalyticsSubmissionTimer]"
+ "-[SUSHistoryTracker submitHistoryAnalyticsEvent]"
+ "-[SUSHistoryTracker updateInstallHistory:build:date:operationType:]"
+ "2"
+ "@\"NSPersistentContainer\""
+ "@\"PCPersistentTimer\""
+ "@\"SUSHistoryInstalls\""
+ "@\"SUSHistoryTracker\""
+ "@40@0:8q16q24@32"
+ "ALTERNATE_DOWNLOAD"
+ "AUTO_DOWNLOAD"
+ "AUTO_INSTALL"
+ "AcceptedAgreementStatus=%@|"
+ "Analytics manager savePath returned nil"
+ "Analytics manager unavailable, continuing without analytics support"
+ "Auto scan found a Splat update; download it now"
+ "B40@0:8@16Q24^@32"
+ "BATTERY_ERROR"
+ "CACHE_DELETE_ENTITLED_RESERVATION"
+ "CACHE_DELETE_ENTITLED_RESERVATION_FREE"
+ "CACHE_DELETE_ENTITLED_RESERVATION_SECURED"
+ "CACHE_DELETE_RESERVE_SPACE"
+ "CACHE_DELETE_RESERVE_SPACE_FILESYSTEM_AMOUNT"
+ "CONTINUITY_CAMERA_IN_USE"
+ "CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, build TEXT, date TEXT, operationType INTEGER);"
+ "Cancelled splat follow-up notification"
+ "Clearing lastPendingSplatAlertDate - no current download/descriptor available"
+ "Clearing lastPendingSplatAlertDate - update is no longer splat-only or security response disabled"
+ "CoreAnalytics"
+ "Couldn't read CA directory: %@"
+ "DELETE FROM logs WHERE id NOT IN (SELECT id FROM logs ORDER BY date DESC LIMIT %d);"
+ "DOWNLOAD_COMPLETE"
+ "DOWNLOAD_FAILED"
+ "DOWNLOAD_INITIATED"
+ "Enable Rapid Return to Service for testing"
+ "Enabling Rapid Return to Service"
+ "Failed to create history tracking path, saving to %@"
+ "Failed to create log directory: %@"
+ "HISTORY_TYPE_UNKNOWN"
+ "Handling splat follow-up notification activity"
+ "ID=%@|"
+ "INSERT INTO logs (name, build, date, operationType) VALUES (?, ?, ?, ?);"
+ "INSTALL_COMPLETE"
+ "INSTALL_FAILED"
+ "INSTALL_INITATED"
+ "INTERNAL_ERROR"
+ "LastDownload: %@            \npreferredLastScannedCoreDescriptor: %@            \nalternateLastScannedCoreDescriptor: %@            \nFailedPatchBuildVersions: %@            \nScheduledManualDownloadWifiPeriodEndTime: %@            \nScheduledAutoDownloadWifiPeriodEndTime: %@            \nScheduledAutoDownloadPolicyChangeTime: %@            \nLastScanDate: %@            \nLastAutoDownloadDate: %@            \nNeedsOneTimeAutoDownloadRetry: %@            \nLastProductVersion: %@            \nLastProductVersionExtra: %@            \nLastProductBuild: %@            \nLastProductType: %@            \nLastReleaseType: %@            \nLastSplatRestoreVersion: %@            \nLastAutoInstallOperationModel: %@            \nManagedDeviceDelay: %@            \nInstallPolicy: %@            \nMandatoryUpdateDict: %@            \nLastRollbackRecommendedBuildVersion: %@            \rolledBackBuildVersions: %@            \nlastDeletedAssetID: %@            \nlastAssetAudience: %@            \nappliedSate: %@            \nunderExclusiveControl: %@            \nLastRecommendedUpdateVersion: %@            \nLastRecommendedUpdateInterval: %@            \nLastRecommendedUpdateDiscoveryDate: %@            \nUpdateDiscoveryDates: %@            \nLastSpaceCleanupLevel: %@            \nLastPendingSplatAlertDate: %@"
+ "LastPendingSplatAlertDate"
+ "N"
+ "NEW_BUCKET_CREATED"
+ "New OS detected. Clearing the last auto-install-operation"
+ "No Analytics Manager available"
+ "No install history found"
+ "No pending splat alert date set"
+ "Not allowing download in RRTS mode"
+ "Not allowing download to start in RRTS mode"
+ "Not allowing installation in RRTS mode"
+ "Override splat follow up delay: %@"
+ "Override the 7-day follow-up delay for splat-only updates (in seconds). For testing purposes only."
+ "Posting scheduled splat follow-up notification"
+ "ProductVersionExtra"
+ "QUIET_OPERATION"
+ "ROLLBACK_COMPLETE"
+ "ROLLBACK_FAILED"
+ "ROLLBACK_INITIATED"
+ "Rollback Update"
+ "SCAN_FAILED_NO_NETWORK"
+ "SCAN_FAILED_NO_UPDATE_FOUND"
+ "SCAN_INITIATED"
+ "SCAN_OTA_FOUND"
+ "SCAN_OTA_SLOW_ROLL_FOUND"
+ "SELECT name, build, date, operationType FROM logs ORDER BY date ASC;"
+ "SELECT name, build, date, operationType FROM logs WHERE date BETWEEN ? AND ? ORDER BY date ASC;"
+ "SPACE_PURGED"
+ "STANDARD_ERROR"
+ "STORAGE_ERROR"
+ "SUEnableRapidReturnToService"
+ "SUEntitledReservation"
+ "SUEntitledReservationFree"
+ "SUEntitledReservationSecured"
+ "SUFFICIENT_SPACE"
+ "SUFFICIENT_SPACE_WITH_PURGE"
+ "SUFSReserveRequestedSize"
+ "SUFSReserveSize"
+ "SULastProductVersionExtraKey"
+ "SUSHistoryEvent"
+ "SUSHistoryInstalls"
+ "SUSHistoryTracker"
+ "SUS_History_Tracking.log"
+ "SUSplatFollowUpDelayOverride"
+ "Saved auto-install-operation is expired"
+ "ScanForSplat"
+ "Scanner"
+ "Scheduled immediate follow-up for regular update"
+ "Scheduled splat follow-up notification for %@"
+ "Scheduled splat follow-up notification for %@ after daemon restart"
+ "Software Update not allowed because RRTS is on"
+ "Space"
+ "T@\"<SUManagerInterface>\",&,N,V_manager"
+ "T@\"NSDate\",&,N,V_lastPendingSplatAlertDate"
+ "T@\"NSDate\",R,N,V_timestamp"
+ "T@\"NSDictionary\",R,&,N,V_eventPayload"
+ "T@\"NSDictionary\",R,N,V_extraInfo"
+ "T@\"NSMutableArray\",&,N,V_eventQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_schedulerQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",R,&,N,V_analyticsSubmissionQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",R,&,N,V_historyProtectionQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",R,&,N,V_protectionQueue"
+ "T@\"NSPersistentContainer\",R,V_persistentContainer"
+ "T@\"NSString\",&,N,V_lastProductVersionExtra"
+ "T@\"NSString\",C,N,V_basePath"
+ "T@\"NSString\",C,N,V_coreAnalyticsPath"
+ "T@\"NSString\",C,N,V_historyInstallDBPath"
+ "T@\"NSString\",C,N,V_historyLogPath"
+ "T@\"NSString\",C,N,V_path"
+ "T@\"PCPersistentTimer\",&,N,V_analyticsSubmissionTimer"
+ "T@\"SUAnalyticsManager\",R,&,N,V_analyticsManager"
+ "T@\"SUAutoInstallManager\",&,N,V_autoInstallManager"
+ "T@\"SUSHistoryInstalls\",R,&,N,V_installHistoryManager"
+ "T@\"SUSHistoryTracker\",&,N,V_tracker"
+ "T@\"SUServerConfigurationManager\",&,N,V_serverConfigManager"
+ "TB,N,GisCanceled,V_canceled"
+ "TB,N,GisExpired,V_expired"
+ "TB,N,V_scanForSplatIfNecessary"
+ "TQ,N,V_minFreeSpacePostStageOptionalAssets"
+ "There is a tonight activity scheduled. Skipping auto download attempt"
+ "There is no downloaded asset. Clearing the last auto-install-operation"
+ "Tq,R,N,V_historyType"
+ "Tq,R,N,V_operation"
+ "Tracking history to %@"
+ "Tracking path: %@"
+ "UNKNOWN"
+ "UNKNOWN_BUILD"
+ "UNKNOWN_UPDATE"
+ "Unable to add event from path: %@"
+ "Unexpected class type sent to analytics for key %@: %@"
+ "Unknown Update"
+ "Unknown Version"
+ "Unknown history type: %ld"
+ "Y"
+ "[<%@:%p>"
+ "[<%@:%p>forecast:%@|agreementStatus:%d|id:%@]"
+ "[<%@:%p>unlockStart:%@|unlockEnd:%@|suStart:%@|suEnd:%@|scheduleType:%@]"
+ "[Auto scan] Automatic scan for type [%@] disabled while in Rapid Return to Service Mode."
+ "^{sqlite3=}"
+ "_analyticsManager"
+ "_analyticsSubmissionQueue"
+ "_analyticsSubmissionTimer"
+ "_basePath"
+ "_checkAndPostSplatFollowUpIfNeeded"
+ "_coreAnalyticsPath"
+ "_db"
+ "_eventPayload"
+ "_eventQueue"
+ "_extraInfo"
+ "_historyInstallDBPath"
+ "_historyLogPath"
+ "_historyProtectionQueue"
+ "_historyTracker"
+ "_historyType"
+ "_installHistoryManager"
+ "_lastPendingSplatAlertDate"
+ "_lastProductVersionExtra"
+ "_minFreeSpacePostStageOptionalAssets"
+ "_operation"
+ "_path"
+ "_persistentContainer"
+ "_preallocatedSpaceMetricInfo"
+ "_protectionQueue"
+ "_queue_addEventPayloadEntries:"
+ "_queue_handleSplatFollowUp:info:"
+ "_scanForSplatIfNecessary"
+ "_timestamp"
+ "_tracker"
+ "addEventPayloadEntries:"
+ "addLogWithName:build:date:operationType:"
+ "alternateBuild"
+ "alternateBuild=%@ "
+ "alternateVersion"
+ "analyticsManager"
+ "analyticsSubmissionQueue"
+ "analyticsSubmissionTimer"
+ "appOffloadEnabled=%d "
+ "appendToString:key:value:"
+ "background=%d "
+ "basePath"
+ "cacheDeleteEnabled"
+ "cacheDeleteEnabled=%d "
+ "cancelAllAutoScanTasks"
+ "cancelSplatFollowUpNotification"
+ "checkAndPostSplatFollowUpIfNeeded"
+ "closeFile"
+ "com.apple.SUSHistory"
+ "com.apple.softwareupdateserivces.SUSHistoryEvent"
+ "com.apple.softwareupdateservices.AnalyticsSubmissionQueue"
+ "com.apple.softwareupdateservices.ProtectionQueue"
+ "com.apple.softwareupdateservices.analytics"
+ "com.apple.softwareupdateservicesd.activity.splatFollowUp"
+ "compareVersionExtra:withVersionExtra:"
+ "componentsJoinedByString:"
+ "consent to auto install operation (%@) result: %@, error: %@"
+ "contentsOfDirectoryAtPath:error:"
+ "coreAnalyticsPath"
+ "currentProductVersionExtra"
+ "dataWithJSONObject:options:error:"
+ "descriptorFromRollbackDescriptor:"
+ "displayName"
+ "downloadNow"
+ "downloadNow=%d "
+ "enableRapidReturnToService"
+ "error=%@ "
+ "eventQueue"
+ "extra info = %@\n"
+ "extraInfo"
+ "fetchInstallHistory"
+ "fetchInstallHistory:"
+ "fileHandleForWritingAtPath:"
+ "fileSize"
+ "formatDownloadEvent:"
+ "formatErrorEvent:"
+ "formatInstallEvent:"
+ "formatScanEvent:"
+ "formatSpaceEvent:"
+ "handleAnalyticsSubmissionTimer:"
+ "history"
+ "historyInstallDBPath"
+ "historyLogPath"
+ "historyOperationName"
+ "historyProtectionQueue"
+ "historyTracker"
+ "historyType"
+ "historyTypeName"
+ "id=%@ "
+ "initUsingProtectionQueue:withBasePath:"
+ "initWithData:encoding:"
+ "initWithOperation:historyType:extraInfo:"
+ "initWithTimeInterval:serviceIdentifier:target:selector:userInfo:"
+ "initializeDatabase"
+ "installHistory.db"
+ "installHistoryManager"
+ "invalidateAnalyticsSubmissionTimer"
+ "isBackground"
+ "isCancelled=%@|"
+ "isExpired=%@|"
+ "isRapidReturnToService"
+ "isScheduled=%@|"
+ "isSplat"
+ "isValidForScheduling=%@|"
+ "lastPendingSplatAlertDate"
+ "lastProductVersionExtra"
+ "lengthOfBytesUsingEncoding:"
+ "matchesDescriptor:comparisonFlags:reason:"
+ "matchesScanResults:"
+ "minFreeSpacePostStageOptionalAssets"
+ "name"
+ "nameForHistoryType:"
+ "no other descriptor"
+ "objCType"
+ "op=%@ "
+ "operation"
+ "operation = %@\n"
+ "operationType"
+ "other is '%@'"
+ "persistentContainer"
+ "preSUStagingFinished:"
+ "preferredBuild"
+ "preferredBuild=%@ "
+ "preferredVersion"
+ "protectionQueue"
+ "protectionQueue:%@|historyType:%@|coreAnalyticsPath:%@|historyLogDirectoryPath:%@|historyLogFileName:%@"
+ "queryAllLogs"
+ "queryLogsFromDate:toDate:"
+ "recordAutoScanAndDownloadIfAvailable:downloadNow:fromClient:"
+ "recordDownloadCompleted:withError:"
+ "recordDownloadStarted:fromClient:"
+ "recordHistoryEvent:"
+ "recordInstallCompleted:withError:"
+ "recordInstallStarted:withDownload:"
+ "recordRollbackCompleted:withError:"
+ "recordRollbackStarted:"
+ "recordScanComplete:downloadNow:withError:"
+ "recordScanForUpdates:fromClient:"
+ "resumeOrDisableReserveSpace"
+ "scanForSplatIfNecessary"
+ "scheduleInQueue:"
+ "scheduleSplatFollowUpDate:"
+ "scheduleSplatFollowUpNotification:"
+ "schedulerQueue"
+ "seekToEndReturningOffset:error:"
+ "server fetch history: %@"
+ "serverConfigManager"
+ "setAnalyticsSubmissionTimer:"
+ "setAutoInstallManager:"
+ "setBasePath:"
+ "setCanceled:"
+ "setCoreAnalyticsPath:"
+ "setEnableRapidReturnToService:"
+ "setEventQueue:"
+ "setExpired:"
+ "setHistoryInstallDBPath:"
+ "setHistoryLogPath:"
+ "setLastPendingSplatAlertDate:"
+ "setLastProductVersionExtra:"
+ "setManager:"
+ "setMinFreeSpacePostStageOptionalAssets:"
+ "setPath:"
+ "setScanForSplatIfNecessary:"
+ "setSchedulerQueue:"
+ "setServerConfigManager:"
+ "setSplatFollowUpDelayOverride:"
+ "setTracker:"
+ "setupAnalyticsSubmissionTimer"
+ "sharedInstanceWithPath:"
+ "sharedManagerWithPath:"
+ "sharedTracker"
+ "softwareUpdateType"
+ "sortedArrayUsingSelector:"
+ "splat=%d "
+ "splatFollowUpDelayOverride"
+ "splombo=%d "
+ "stringWithContentsOfFile:encoding:error:"
+ "submitHistoryAnalyticsEvent"
+ "targetBuild"
+ "targetBuild=%@ "
+ "targetVersion"
+ "time=%@ "
+ "timestamp"
+ "timestamp = %@\n"
+ "toAnalytics"
+ "tracker"
+ "trackerWithPath:"
+ "type = %@\n"
+ "updateInstallHistory:build:date:operationType:"
+ "updateTitle=%@ "
+ "updateType=%@ "
+ "userInitiated"
+ "userInitiated=%d "
+ "v24@0:8@\"SUCoreUpdatePreSUStagingOutcome\"16"
+ "v32@0:8i16B20@24"
+ "v48@0:8@16@24@32q40"
+ "writeData:error:"
+ "writeToFile:atomically:encoding:error:"
+ "yyyy-MM-dd HH:mm:ss"
+ "yyyy-MM-dd-HH:mm:ss.SSS"
+ "| "
- "\n            ClientName: %@\n            Identifier: %@\n            Forced: %@\n            ScanType: %d\n            CollectDoc: %@\n            Types: %@\n            Requested PMV: %@\n            Requested Build: %@\n            SessionID: %@\n            MDM use delay: %@\n            MDM show RSR: %@\n            =============== MDM: %@ \n            ===================\n            Ignore NoUpdateFound response: %@\n"
- "\n            Publisher: %@\n            HumanReadableUpdateName: %@\n            ProductSystemName: %@\n            ProductVersion: %@\n            ProductVersionExtra: %@\n            ProductBuildVersion: %@\n            PrerequisiteBuild: %@\n            PrerequisiteOS: %@\n            ReleaseType: %@\n            DownloadSize: %llu\n            UnarchiveSize: %llu\n            MSUPrepareSize: %llu\n            PreparationSize: %llu\n            InstallationSize: %llu\n            PreSUStagingRequiredSize: %llu\n            PreSUStagingOptionalSize: %llu\n            UnentitledReserveAmount: %llu\n            UpdateType: %@\n            Downloadable: %@\n            DownloadableOverCellular: %@\n            AutoDownloadableOverCellular: %@\n            AutoUpdateEnabled: %@\n            StreamingZipCapable: %@\n            TotalRequiredFreeSpace: %llu\n            Documentation: %@\n            SiriVoiceDeletion: %d\n            CDLevel4DeletionDisabled: %d\n            appDemotionDisabled: %d\n            maSuspensionDisabled: %d\n            installTonightDisabled: %d\n            rampEnabled: %d\n            granularlyRamped: %d\n            setupCritical: %@\n            criticalOutOfBoxOnly: %d\n            criticalDownloadPolicy: %@\n            releaseDate: %@\n            mdmDelayInterval: %llu\n            assetID: %@\n            hideInstallAlert: %@\n            audienceType: %@\n            preferenceType: %@\n            upgradeType: %@\n            promoteAlternateUpdate: %@\n            isSplatOnly: %@\n            mandatoryUpdateEligible: %@\n            mandatoryUpdateVersionMin: %@\n            mandatoryUpdateVersionMax: %@\n            mandatoryUpdateOptional: %@\n            mandatoryUpdateRestrictedToOutOfTheBox: %@\n            forcePasscodeRequired: %@\n            allowAutoDownloadOnBattery: %@\n            autoDownloadOnBatteryDelay: %u\n            autoDownloadOnBatteryMinbattery: %u%%\n            isSplombo: %@\n            splatComboBuildVersion: %@"
- "%s - [DDM] Fall back to a scan for Splat updates with options %@"
- "%s - [DDM] Fall back to a scan for regular updates with options %@"
- "-[SURollbackController rollbackUpdateWithOptions:completion:]_block_invoke_3"
- "-[SURollbackController rollbackUpdateWithOptions:completion:]_block_invoke_6"
- "@56@0:8@16B24@28@36i44B48B52"
- "AUTO_SU_FOLLOW_UP_TEXT_RSR_AVAILABLE_BODY"
- "AUTO_SU_FOLLOW_UP_TEXT_RSR_AVAILABLE_BODY_FALLBCAK"
- "AUTO_SU_FOLLOW_UP_TEXT_RSR_TONIGHT"
- "AcceptedAgreementStatus=%@, "
- "AutoInstallForecast <%p> :\n            unlockStart = %@\n            unlockEnd = %@\n            suStart = %@\n            suEnd = %@\n            firstUnlock = %@\n            _scheduleType = %@\n"
- "B40@0:8@16@24Q32"
- "ID=%@, "
- "LastDownload: %@            \npreferredLastScannedCoreDescriptor: %@            \nalternateLastScannedCoreDescriptor: %@            \nFailedPatchBuildVersions: %@            \nScheduledManualDownloadWifiPeriodEndTime: %@            \nScheduledAutoDownloadWifiPeriodEndTime: %@            \nScheduledAutoDownloadPolicyChangeTime: %@            \nLastScanDate: %@            \nLastAutoDownloadDate: %@            \nNeedsOneTimeAutoDownloadRetry: %@            \nLastProductVersion: %@            \nLastProductBuild: %@            \nLastProductType: %@            \nLastReleaseType: %@            \nLastSplatRestoreVersion: %@            \nLastAutoInstallOperationModel: %@            \nManagedDeviceDelay: %@            \nInstallPolicy: %@            \nMandatoryUpdateDict: %@            \nLastRollbackRecommendedBuildVersion: %@            \rolledBackBuildVersions: %@            \nlastDeletedAssetID: %@            \nlastAssetAudience: %@            \nappliedSate: %@            \nunderExclusiveControl: %@            \nLastRecommendedUpdateVersion: %@            \nLastRecommendedUpdateInterval: %@            \nLastRecommendedUpdateDiscoveryDate: %@            \nUpdateDiscoveryDates: %@            \nLastSpaceCleanupLevel: %@"
- "New OS detected. Clearing last SUAutoInstallOperation"
- "SUAutoInstallOperation.m"
- "SUDescriptor:matchesSUCoreDescriptor:comparisonFlags:"
- "Saved SUAutoInstallOperation is expired"
- "T@\"NSDate\",&,N,V_firstUnlock"
- "TB,N,V_waitingUntilDownloadComplete"
- "TB,R,N,GisCanceled,V_canceled"
- "TB,R,N,GisExpired,V_expired"
- "There is no downloaded asset. Clearing last SUAutoInstallOperation"
- "Unable to rollback update because delegate callback not implemented"
- "[<SUAutoInstallOperation:%p> "
- "__agreementStatus"
- "__cancelled"
- "__expired"
- "__forecast"
- "__id"
- "_autoScanTimeInterval"
- "_clientOwned"
- "_firstUnlock"
- "_initWithClient:clientOwned:id:forecast:agreementStatus:cancelled:expired:"
- "_waitingUntilDownloadComplete"
- "cancelAllAutoscanTasks"
- "client"
- "consent auto install operation (%@) result: %@, error: %@"
- "firstUnlock"
- "forecast: %@\n             agreementStatus: %d\n             id: %@             waitingUntilDownloadComplete: %@"
- "isCancelled=%@, "
- "isExpired=%@, "
- "isScheduled=%@, "
- "isValidForScheduling=%@, "
- "noteInstallDidFail:withError:"
- "noteInstallDidFinish:"
- "resumeReserveSpaceStateIfNeeded"
- "setFirstUnlock:"
- "setWaitingUntilDownloadComplete:"
- "unrestricted_sleep_end"
- "uuid"
- "waitingUntilDownloadComplete"

```
