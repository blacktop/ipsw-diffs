## SoftwareUpdateServices

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices`

```diff

-950.80.5.0.0
-  __TEXT.__text: 0xb8a4c
-  __TEXT.__auth_stubs: 0xf70
-  __TEXT.__objc_methlist: 0xb30c
-  __TEXT.__const: 0x318
-  __TEXT.__cstring: 0x2348c
-  __TEXT.__gcc_except_tab: 0x13e0
+950.100.130.0.1
+  __TEXT.__text: 0xc29f8
+  __TEXT.__auth_stubs: 0xe40
+  __TEXT.__objc_methlist: 0xb474
+  __TEXT.__const: 0x328
+  __TEXT.__cstring: 0x23677
+  __TEXT.__gcc_except_tab: 0x125c
   __TEXT.__oslogstring: 0x85d
-  __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x3390
-  __TEXT.__objc_classname: 0xf4b
-  __TEXT.__objc_methname: 0x1a04a
-  __TEXT.__objc_methtype: 0x34fb
-  __TEXT.__objc_stubs: 0x15000
-  __DATA_CONST.__got: 0xde0
-  __DATA_CONST.__const: 0x2a58
-  __DATA_CONST.__objc_classlist: 0x3f0
+  __TEXT.__unwind_info: 0x3680
+  __TEXT.__objc_classname: 0xf77
+  __TEXT.__objc_methname: 0x1a294
+  __TEXT.__objc_methtype: 0x3502
+  __TEXT.__objc_stubs: 0x15300
+  __DATA_CONST.__got: 0xe00
+  __DATA_CONST.__const: 0x2a60
+  __DATA_CONST.__objc_classlist: 0x3f8
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x130
+  __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6028
+  __DATA_CONST.__objc_selrefs: 0x60f0
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x338
+  __DATA_CONST.__objc_superrefs: 0x340
   __DATA_CONST.__objc_arraydata: 0xa0
-  __AUTH_CONST.__auth_got: 0x7c8
-  __AUTH_CONST.__const: 0x7c0
-  __AUTH_CONST.__cfstring: 0x14940
-  __AUTH_CONST.__objc_const: 0x16120
+  __AUTH_CONST.__auth_got: 0x730
+  __AUTH_CONST.__const: 0x7e0
+  __AUTH_CONST.__cfstring: 0x14ae0
+  __AUTH_CONST.__objc_const: 0x16308
   __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0xd8
-  __AUTH.__objc_data: 0x1108
-  __DATA.__objc_ivar: 0x9cc
-  __DATA.__data: 0xe98
-  __DATA.__bss: 0x130
-  __DATA_DIRTY.__objc_data: 0x1658
-  __DATA_DIRTY.__bss: 0x1f0
+  __AUTH.__objc_data: 0x1018
+  __DATA.__objc_ivar: 0x9d8
+  __DATA.__data: 0xef8
+  __DATA.__bss: 0x108
+  __DATA_DIRTY.__objc_data: 0x1798
+  __DATA_DIRTY.__bss: 0x200
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup
+  - /System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/MobileInBoxUpdate
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/MobileSoftwareUpdate
   - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi
   - /System/Library/PrivateFrameworks/PersistentConnection.framework/PersistentConnection
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant
   - /System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore
   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: ECDF78AD-678A-3632-B2C2-BC9A6E90329C
-  Functions: 4639
-  Symbols:   15411
-  CStrings:  10776
+  UUID: 0256C3DC-92CA-377E-BEA0-E277B38F7ACD
+  Functions: 4681
+  Symbols:   15511
+  CStrings:  10823
 
Symbols:
+ +[SUGameModeMonitor sharedMonitor]
+ +[SUUtility currentSupplementalBuild]
+ +[SUUtility currentSupplementalBuild].cold.1
+ +[SUUtility fakeOTA]
+ +[SUUtility prettyPrintDate:].cold.1
+ -[SUDescriptor humanReadableUpdateLabel]
+ -[SUDescriptor setHumanReadableUpdateLabel:]
+ -[SUDescriptor(SUBattery) releasedAfter:]
+ -[SUGameModeMonitor .cxx_destruct]
+ -[SUGameModeMonitor _gameModeChangedTo:]
+ -[SUGameModeMonitor addDelegate:]
+ -[SUGameModeMonitor delegates]
+ -[SUGameModeMonitor inGameMode]
+ -[SUGameModeMonitor initForTesting]
+ -[SUGameModeMonitor init]
+ -[SUGameModeMonitor queue]
+ -[SUGameModeMonitor removeDelegate:]
+ -[SUGameModeMonitor setDelegates:]
+ -[SUGameModeMonitor setQueue:]
+ -[SUManagerClient newOSBuildDetected:]
+ -[SUManagerCore dismissSplatFollowUp]
+ -[SUManagerPolicy dismissSplatFollowUp]
+ -[SUManagerServer newOSBuildDetected:]
+ -[SUPreferences hoursSinceUpdateReleaseOverride]
+ -[SUPreferences isInBoxUpdateMode]
+ -[SUPreferences isInPalletUpdateMode]
+ -[SUPreferences scanAsIfBuildVersion]
+ -[SUPreferences scanAsIfProductVersion]
+ -[SUPreferences scanAsIfRestoreVersion]
+ -[SUSHistoryInstalls initWithState:]
+ -[SUSHistoryInstalls setState:]
+ -[SUSHistoryInstalls state]
+ -[SUSHistoryTracker initWithBasePath:]
+ -[SUSHistoryTracker recordError:operation:withInfo:]
+ -[SUSHistoryTracker recordInstallCompleted:]
+ -[SUScheduler gameModeChangedTo:]
+ -[SUScheduler initUsingSUCoreXPCActivityManager:coreScheduler:serverConfigManager:schedulerQueue:manager:autoInstallManager:gameModeMonitor:]
+ -[SUState addHistoryEntry:]
+ -[SUState history]
+ -[SUState loadHistory]
+ -[SUState queue_addHistoryEntry:]
+ -[SUState setHistory:]
+ GCC_except_table115
+ GCC_except_table135
+ GCC_except_table151
+ GCC_except_table351
+ GCC_except_table456
+ OBJC_IVAR_$_SUState._history
+ _BYSetupAssistantBundleIdentifier
+ _OBJC_CLASS_$_MIBUClient
+ _OBJC_CLASS_$_SUGameModeMonitor
+ _OBJC_IVAR_$_SUDescriptor._humanReadableUpdateLabel
+ _OBJC_IVAR_$_SUGameModeMonitor._delegates
+ _OBJC_IVAR_$_SUGameModeMonitor._inGameMode
+ _OBJC_IVAR_$_SUGameModeMonitor._queue
+ _OBJC_IVAR_$_SUSHistoryInstalls._state
+ _OBJC_IVAR_$_SUScheduler._gameModeMonitor
+ _OBJC_METACLASS_$_SUGameModeMonitor
+ _OUTLINED_FUNCTION_2
+ __OBJC_$_CLASS_METHODS_SUGameModeMonitor
+ __OBJC_$_INSTANCE_METHODS_SUGameModeMonitor
+ __OBJC_$_INSTANCE_VARIABLES_SUGameModeMonitor
+ __OBJC_$_PROP_LIST_SUGameModeMonitor
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SUGameModeMonitorDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SUGameModeMonitorDelegate
+ __OBJC_$_PROTOCOL_REFS_SUGameModeMonitorDelegate
+ __OBJC_CLASS_RO_$_SUGameModeMonitor
+ __OBJC_LABEL_PROTOCOL_$_SUGameModeMonitorDelegate
+ __OBJC_METACLASS_RO_$_SUGameModeMonitor
+ __OBJC_PROTOCOL_$_SUGameModeMonitorDelegate
+ ___18-[SUState history]_block_invoke
+ ___22-[SUState setHistory:]_block_invoke
+ ___25-[SUGameModeMonitor init]_block_invoke
+ ___27-[SUState addHistoryEntry:]_block_invoke
+ ___29+[SUUtility prettyPrintDate:]_block_invoke
+ ___31-[SUGameModeMonitor inGameMode]_block_invoke
+ ___32-[SUInstaller installCompleted:]_block_invoke.396
+ ___32-[SUInstaller installCompleted:]_block_invoke_2.397
+ ___32-[SUInstaller installCompleted:]_block_invoke_3.406
+ ___32-[SUInstaller installCompleted:]_block_invoke_4.407
+ ___33-[SUGameModeMonitor addDelegate:]_block_invoke
+ ___33-[SUScheduler gameModeChangedTo:]_block_invoke
+ ___34+[SUGameModeMonitor sharedMonitor]_block_invoke
+ ___36-[SUGameModeMonitor removeDelegate:]_block_invoke
+ ___37+[SUUtility currentSupplementalBuild]_block_invoke
+ ___38-[SUManagerServer newOSBuildDetected:]_block_invoke
+ ___38-[SUManagerServer newOSBuildDetected:]_block_invoke_2
+ ___39-[SUManagerPolicy dismissSplatFollowUp]_block_invoke
+ ___40-[SUAutoInstallManager initWithManager:]_block_invoke
+ ___42-[SUManagerEngine action_RemoveAll:error:]_block_invoke.541
+ ___42-[SUManagerEngine action_RemoveAll:error:]_block_invoke.545
+ ___47-[SUSHistoryInstalls queryLogsFromDate:toDate:]_block_invoke
+ ___86-[SUManagerCore updatesDownloadableWithOptions:alternateDownloadOptions:replyHandler:]_block_invoke.511
+ ___NSArray0__struct
+ ___block_descriptor_48_e8_32s40s_e39_B24?0"NSDictionary"8"NSDictionary"16ls32l8s40l8
+ ___block_literal_global.299
+ ___block_literal_global.302
+ ___block_literal_global.313
+ ___block_literal_global.318
+ ___block_literal_global.323
+ ___block_literal_global.328
+ ___block_literal_global.333
+ ___block_literal_global.338
+ ___block_literal_global.343
+ ___block_literal_global.348
+ ___block_literal_global.353
+ ___block_literal_global.358
+ ___block_literal_global.366
+ ___block_literal_global.371
+ ___block_literal_global.379
+ ___block_literal_global.406
+ ___block_literal_global.408
+ ___block_literal_global.414
+ ___block_literal_global.420
+ ___block_literal_global.442
+ ___block_literal_global.482
+ ___block_literal_global.529
+ ___block_literal_global.551
+ ___block_literal_global.556
+ ___block_literal_global.607
+ ___block_literal_global.618
+ ___block_literal_global.649
+ ___block_literal_global.653
+ _currentSupplementalBuild.__currentSupplementalBuild
+ _currentSupplementalBuild.supplementalBuildPredicate
+ _entryBuild
+ _entryDate
+ _entryName
+ _entryOperationType
+ _humanReadableUpdateLabel
+ _objc_msgSend$_gameModeChangedTo:
+ _objc_msgSend$addDelegate:
+ _objc_msgSend$addHistoryEntry:
+ _objc_msgSend$client:newOSBuildDetected:
+ _objc_msgSend$currentSupplementalBuild
+ _objc_msgSend$delegates
+ _objc_msgSend$dismissSplatFollowUp
+ _objc_msgSend$fakeOTA
+ _objc_msgSend$filteredArrayUsingPredicate:
+ _objc_msgSend$gameModeChangedTo:
+ _objc_msgSend$history
+ _objc_msgSend$hoursSinceUpdateReleaseOverride
+ _objc_msgSend$humanReadableUpdateLabel
+ _objc_msgSend$inGameMode
+ _objc_msgSend$initUsingSUCoreXPCActivityManager:coreScheduler:serverConfigManager:schedulerQueue:manager:autoInstallManager:gameModeMonitor:
+ _objc_msgSend$initWithBasePath:
+ _objc_msgSend$initWithState:
+ _objc_msgSend$isInBoxUpdateMode
+ _objc_msgSend$isInBoxUpdateMode:
+ _objc_msgSend$isInPalletUpdateMode
+ _objc_msgSend$isInPalletUpdateMode:
+ _objc_msgSend$loadHistory
+ _objc_msgSend$newOSBuildDetected:
+ _objc_msgSend$predicateWithBlock:
+ _objc_msgSend$queue_addHistoryEntry:
+ _objc_msgSend$recordError:operation:withInfo:
+ _objc_msgSend$recordInstallCompleted:
+ _objc_msgSend$releasedAfter:
+ _objc_msgSend$removeDelegate:
+ _objc_msgSend$scanAsIfBuildVersion
+ _objc_msgSend$scanAsIfProductVersion
+ _objc_msgSend$scanAsIfRestoreVersion
+ _objc_msgSend$secureCodedObjectForKey:ofClass:encodeClasses:
+ _objc_msgSend$setHistory:
+ _objc_msgSend$setHumanReadableUpdateLabel:
+ _objc_msgSend$setPrerequisiteBuildVersion:
+ _objc_msgSend$setPrerequisiteProductVersion:
+ _objc_msgSend$setPrerequisiteRestoreVersion:
+ _objc_msgSend$sharedMonitor
+ _prettyPrintDate:.dateFormatter
+ _prettyPrintDate:.onceToken
+ _sharedMonitor.onceToken
+ _sharedMonitor.sharedMonitor
- +[SUSHistoryInstalls sharedInstanceWithPath:]
- +[SUSHistoryTracker sharedTracker]
- +[SUSHistoryTracker sharedTracker].cold.1
- +[SUSHistoryTracker trackerWithPath:]
- -[SUDescriptor(SUBattery) releasedBefore:]
- -[SUManagerServer newOSDetected:deleteKeepAlive:]
- -[SUSHistoryInstalls createTableIfNeeded]
- -[SUSHistoryInstalls dealloc]
- -[SUSHistoryInstalls initializeDatabase]
- -[SUSHistoryInstalls path]
- -[SUSHistoryInstalls persistentContainer]
- -[SUSHistoryInstalls setPath:]
- -[SUSHistoryTracker initUsingProtectionQueue:withBasePath:]
- -[SUSHistoryTracker protectionQueue]
- -[SUSHistoryTracker recordInstallCompleted:withError:]
- -[SUScanner isBuddyRunning].cold.1
- -[SUScheduler cancelInstallAlertRegistrationButKeepAlive]
- GCC_except_table101
- GCC_except_table105
- GCC_except_table113
- GCC_except_table137
- GCC_except_table147
- GCC_except_table350
- GCC_except_table454
- GCC_except_table88
- _OBJC_IVAR_$_SUSHistoryInstalls._db
- _OBJC_IVAR_$_SUSHistoryInstalls._path
- _OBJC_IVAR_$_SUSHistoryInstalls._persistentContainer
- _OBJC_IVAR_$_SUSHistoryTracker._protectionQueue
- _SetupAssistantLibraryCore.frameworkLibrary
- __OBJC_$_CLASS_METHODS_SUSHistoryInstalls
- ___32-[SUInstaller installCompleted:]_block_invoke.387
- ___32-[SUInstaller installCompleted:]_block_invoke_2.388
- ___32-[SUInstaller installCompleted:]_block_invoke_3.397
- ___32-[SUInstaller installCompleted:]_block_invoke_4.398
- ___34+[SUSHistoryTracker sharedTracker]_block_invoke
- ___37+[SUSHistoryTracker trackerWithPath:]_block_invoke
- ___40-[SUSHistoryTracker recordHistoryEvent:]_block_invoke
- ___42-[SUManagerEngine action_RemoveAll:error:]_block_invoke.532
- ___42-[SUManagerEngine action_RemoveAll:error:]_block_invoke.536
- ___45+[SUSHistoryInstalls sharedInstanceWithPath:]_block_invoke
- ___57-[SUScheduler cancelInstallAlertRegistrationButKeepAlive]_block_invoke
- ___86-[SUManagerCore updatesDownloadableWithOptions:alternateDownloadOptions:replyHandler:]_block_invoke.501
- ___SetupAssistantLibraryCore_block_invoke
- ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
- ___block_literal_global.290
- ___block_literal_global.293
- ___block_literal_global.304
- ___block_literal_global.309
- ___block_literal_global.314
- ___block_literal_global.319
- ___block_literal_global.324
- ___block_literal_global.329
- ___block_literal_global.334
- ___block_literal_global.339
- ___block_literal_global.344
- ___block_literal_global.352
- ___block_literal_global.357
- ___block_literal_global.365
- ___block_literal_global.397
- ___block_literal_global.399
- ___block_literal_global.405
- ___block_literal_global.411
- ___block_literal_global.433
- ___block_literal_global.473
- ___block_literal_global.520
- ___block_literal_global.545
- ___block_literal_global.550
- ___block_literal_global.583
- ___block_literal_global.588
- ___block_literal_global.630
- ___block_literal_global.640
- ___getBYSetupAssistantBundleIdentifierSymbolLoc_block_invoke
- ___getBYSetupAssistantBundleIdentifierSymbolLoc_block_invoke.cold.1
- __sl_dlopen
- _audit_stringSetupAssistant
- _dlerror
- _getBYSetupAssistantBundleIdentifierSymbolLoc.ptr
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$bundleAttributes
- _objc_msgSend$cancelInstallAlertRegistrationButKeepAlive
- _objc_msgSend$createTableIfNeeded
- _objc_msgSend$deleteKeepAliveFile
- _objc_msgSend$handleFailureInFunction:file:lineNumber:description:
- _objc_msgSend$initUsingProtectionQueue:withBasePath:
- _objc_msgSend$initializeDatabase
- _objc_msgSend$localizedDescription
- _objc_msgSend$newOSDetected:deleteKeepAlive:
- _objc_msgSend$protectionQueue
- _objc_msgSend$recordInstallCompleted:withError:
- _objc_msgSend$releasedBefore:
- _objc_msgSend$setPath:
- _objc_msgSend$sharedInstanceWithPath:
- _objc_msgSend$sharedTracker
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x9
- _prettyPrintDate:.__dateFormatter
- _sharedInstanceWithPath:.onceToken
- _sharedInstanceWithPath:.sharedInstance
- _sharedTracker.onceToken
- _sharedTracker.sharedInstance
- _sqlite3_bind_int64
- _sqlite3_bind_text
- _sqlite3_close
- _sqlite3_column_int64
- _sqlite3_column_text
- _sqlite3_errmsg
- _sqlite3_exec
- _sqlite3_finalize
- _sqlite3_free
- _sqlite3_open_v2
- _sqlite3_prepare_v2
- _sqlite3_step
- _trackerWithPath:.onceToken
- _trackerWithPath:.sharedInstance
CStrings:
+ "%s - will not rescan for Splat -- disabled by default"
+ "%s: MIBUClient isInBoxUpdateMode error: %@"
+ "%s: MIBUClient isInPalletUpdateMode error: %@"
+ "%s: Missing data for history entry"
+ "%s: Recording installed history: %@"
+ "-[SUManagerClient newOSBuildDetected:]"
+ "-[SUManagerServer newOSBuildDetected:]_block_invoke_2"
+ "-[SUSHistoryTracker recordHistoryEvent:]"
+ "-[SUSHistoryTracker recordInstallCompleted:]"
+ "@\"SUGameModeMonitor\""
+ "@68@0:8B16@20@28@36@44@52@60"
+ "B24@?0@\"NSDictionary\"8@\"NSDictionary\"16"
+ "Cannot kill download: installation in progress"
+ "Cannot kill download: no update found"
+ "Cannot kill download: space cleanup in progress"
+ "Cannot kill download: update is installed"
+ "Device is currently in game mode; don't create the keep alive file for auto-update"
+ "Game mode changed from %d to %d"
+ "Game mode is disabled; creating the AU keep alive file for activity %@"
+ "Game mode is enabled; deleting the AU keep alive file, if any"
+ "Got request to dismiss SplatFollowUp"
+ "Ignoring no update found result because this scan didn't include Splat but we do have a previously found Splat update"
+ "In game mode. Skipping auto download attempt"
+ "LastDownload: %@            \npreferredLastScannedCoreDescriptor: %@            \nalternateLastScannedCoreDescriptor: %@            \nFailedPatchBuildVersions: %@            \nScheduledManualDownloadWifiPeriodEndTime: %@            \nScheduledAutoDownloadWifiPeriodEndTime: %@            \nScheduledAutoDownloadPolicyChangeTime: %@            \nLastScanDate: %@            \nLastAutoDownloadDate: %@            \nNeedsOneTimeAutoDownloadRetry: %@            \nLastProductVersion: %@            \nLastProductVersionExtra: %@            \nLastProductBuild: %@            \nLastProductType: %@            \nLastReleaseType: %@            \nLastSplatRestoreVersion: %@            \nLastAutoInstallOperationModel: %@            \nManagedDeviceDelay: %@            \nInstallPolicy: %@            \nMandatoryUpdateDict: %@            \nLastRollbackRecommendedBuildVersion: %@            \rolledBackBuildVersions: %@            \nlastDeletedAssetID: %@            \nlastAssetAudience: %@            \nappliedSate: %@            \nunderExclusiveControl: %@            \nLastRecommendedUpdateVersion: %@            \nLastRecommendedUpdateInterval: %@            \nLastRecommendedUpdateDiscoveryDate: %@            \nUpdateDiscoveryDates: %@            \nLastSpaceCleanupLevel: %@            \nLastPendingSplatAlertDate: %@            \nHistory: %@"
+ "Loaded history: %@"
+ "New fake OS detected; resetting all prior state."
+ "Override the build version used when scanning for updates (e.g. 23E168)"
+ "Override the product version used when scanning for updates (e.g. 26.4)"
+ "Override the restore version used when scanning for updates (e.g. 23.5.168.0.0,0)"
+ "Override update release delta of a descriptor for power policy."
+ "SUGameModeMonitor"
+ "SUGameModeMonitorDelegate"
+ "SUHistory"
+ "SUHoursSinceUpdateReleaseOverride"
+ "SUInBoxUpdateMode"
+ "SUInPalletUpdateMode"
+ "SUScanAsIfBuildVersion"
+ "SUScanAsIfProductVersion"
+ "SUScanAsIfRestoreVersion"
+ "Space cleanup operation is in progress"
+ "SupplementalBuildVersion"
+ "T@\"NSHashTable\",&,N,V_delegates"
+ "T@\"NSMutableArray\",&,N,V_history"
+ "T@\"NSString\",&,N,V_humanReadableUpdateLabel"
+ "T@\"SUState\",&,V_state"
+ "Updating install history: %@ %@"
+ "[Auto download] Beta: Downloading every 1 day"
+ "[PREFERENCES] ! using as-if build ver for policy: %@"
+ "[PREFERENCES] ! using as-if product ver for policy: %@"
+ "[PREFERENCES] ! using as-if restore ver for policy: %@"
+ "[Scheduler] Set auto install activity from %@ to %@"
+ "_delegates"
+ "_gameModeChangedTo:"
+ "_gameModeMonitor"
+ "_history"
+ "_humanReadableUpdateLabel"
+ "_inGameMode"
+ "addDelegate:"
+ "addHistoryEntry:"
+ "client:newOSBuildDetected:"
+ "com.apple.softwareupdateservices.history.AnalyticsSubmissionQueue"
+ "com.apple.sus.gamemodemonitor.q"
+ "com.apple.system.console_mode_changed"
+ "currentSupplementalBuild"
+ "delegates"
+ "dismissSplatFollowUp"
+ "fakeOTA"
+ "filteredArrayUsingPredicate:"
+ "gameModeChangedTo:"
+ "historyType:%@|coreAnalyticsPath:%@|historyLogDirectoryPath:%@|historyLogFileName:%@"
+ "hoursSinceUpdateReleaseOverride"
+ "humanReadableUpdateLabel"
+ "if set to true, inboxupdaterd scans will be for Napoli usecase"
+ "if set to true, inboxupdaterd scans will be for Seaship usecase"
+ "inGameMode"
+ "initForTesting"
+ "initUsingSUCoreXPCActivityManager:coreScheduler:serverConfigManager:schedulerQueue:manager:autoInstallManager:gameModeMonitor:"
+ "initWithBasePath:"
+ "initWithState:"
+ "isInBoxUpdateMode"
+ "isInBoxUpdateMode:"
+ "isInPalletUpdateMode"
+ "isInPalletUpdateMode:"
+ "loadHistory"
+ "newOSBuildDetected:"
+ "predicateWithBlock:"
+ "queue_addHistoryEntry:"
+ "recordError:operation:withInfo:"
+ "recordInstallCompleted:"
+ "releasedAfter:"
+ "removeDelegate:"
+ "scanAsIfBuildVersion"
+ "scanAsIfProductVersion"
+ "scanAsIfRestoreVersion"
+ "secureCodedObjectForKey:ofClass:encodeClasses:"
+ "setDelegates:"
+ "setHistory:"
+ "setHumanReadableUpdateLabel:"
+ "setPrerequisiteBuildVersion:"
+ "setPrerequisiteProductVersion:"
+ "setPrerequisiteRestoreVersion:"
+ "setState:"
+ "sharedMonitor"
+ "v40@0:8@16^q24@32"
- " %@"
- "%s"
- "%s: %@, deleteKeepAlive: %@"
- "%s: Attempting to delete and recreate database due to protection class issue"
- "%s: DB created"
- "%s: DB successfully recreated after deletion"
- "%s: Database file doesn't exist, skipping retry"
- "%s: Error creating table: %s"
- "%s: Error opening database: %s"
- "%s: Failed to delete existing database: %@"
- "%s: Failed to insert log: %s"
- "%s: Failed to open database even after deletion: %s"
- "%s: Failed to prepare insert: %s"
- "%s: Failed to trim old log entries: %s"
- "%s: Success entry insert"
- "%s: Successfully deleted existing database"
- "%s: Trimmed logs to most recent %d entries"
- "%s: failed to query database: %s"
- "%s: query database success"
- "-[SUManagerServer newOSDetected:deleteKeepAlive:]"
- "-[SUSHistoryInstalls createTableIfNeeded]"
- "-[SUSHistoryInstalls initializeDatabase]"
- "-[SUSHistoryInstalls queryAllLogs]"
- "-[SUSHistoryInstalls queryLogsFromDate:toDate:]"
- "-[SUSHistoryTracker recordHistoryEvent:]_block_invoke"
- "@\"NSPersistentContainer\""
- "AssetFormat"
- "BYSetupAssistantBundleIdentifier"
- "CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, build TEXT, date TEXT, operationType INTEGER);"
- "DELETE FROM logs WHERE id NOT IN (SELECT id FROM logs ORDER BY date DESC LIMIT %d);"
- "INSERT INTO logs (name, build, date, operationType) VALUES (?, ?, ?, ?);"
- "LastDownload: %@            \npreferredLastScannedCoreDescriptor: %@            \nalternateLastScannedCoreDescriptor: %@            \nFailedPatchBuildVersions: %@            \nScheduledManualDownloadWifiPeriodEndTime: %@            \nScheduledAutoDownloadWifiPeriodEndTime: %@            \nScheduledAutoDownloadPolicyChangeTime: %@            \nLastScanDate: %@            \nLastAutoDownloadDate: %@            \nNeedsOneTimeAutoDownloadRetry: %@            \nLastProductVersion: %@            \nLastProductVersionExtra: %@            \nLastProductBuild: %@            \nLastProductType: %@            \nLastReleaseType: %@            \nLastSplatRestoreVersion: %@            \nLastAutoInstallOperationModel: %@            \nManagedDeviceDelay: %@            \nInstallPolicy: %@            \nMandatoryUpdateDict: %@            \nLastRollbackRecommendedBuildVersion: %@            \rolledBackBuildVersions: %@            \nlastDeletedAssetID: %@            \nlastAssetAudience: %@            \nappliedSate: %@            \nunderExclusiveControl: %@            \nLastRecommendedUpdateVersion: %@            \nLastRecommendedUpdateInterval: %@            \nLastRecommendedUpdateDiscoveryDate: %@            \nUpdateDiscoveryDates: %@            \nLastSpaceCleanupLevel: %@            \nLastPendingSplatAlertDate: %@"
- "NSString *getBYSetupAssistantBundleIdentifier(void)"
- "SELECT name, build, date, operationType FROM logs ORDER BY date ASC;"
- "SELECT name, build, date, operationType FROM logs WHERE date BETWEEN ? AND ? ORDER BY date ASC;"
- "SUScanner.m"
- "StreamingZip"
- "T@\"NSObject<OS_dispatch_queue>\",R,&,N,V_protectionQueue"
- "T@\"NSPersistentContainer\",R,V_persistentContainer"
- "T@\"NSString\",C,N,V_path"
- "UNKNOWN_BUILD"
- "UNKNOWN_UPDATE"
- "[Auto download] Customer: Downloading every 5 days"
- "^{sqlite3=}"
- "_db"
- "_path"
- "_persistentContainer"
- "_protectionQueue"
- "bundleAttributes"
- "cancelInstallAlertRegistrationButKeepAlive"
- "com.apple.softwareupdateservices.AnalyticsSubmissionQueue"
- "com.apple.softwareupdateservices.ProtectionQueue"
- "createTableIfNeeded"
- "handleFailureInFunction:file:lineNumber:description:"
- "initUsingProtectionQueue:withBasePath:"
- "initializeDatabase"
- "installHistory.db"
- "localizedDescription"
- "newOSDetected:"
- "newOSDetected:deleteKeepAlive:"
- "persistentContainer"
- "protectionQueue"
- "protectionQueue:%@|historyType:%@|coreAnalyticsPath:%@|historyLogDirectoryPath:%@|historyLogFileName:%@"
- "recordInstallCompleted:withError:"
- "releasedBefore:"
- "setPath:"
- "sharedInstanceWithPath:"
- "sharedTracker"
- "softlink:r:path:/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant"
- "trackerWithPath:"
- "v28@0:8@\"NSString\"16B24"
- "void *SetupAssistantLibrary(void)"

```
