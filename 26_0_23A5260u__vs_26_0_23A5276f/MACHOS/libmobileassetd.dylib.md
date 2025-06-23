## libmobileassetd.dylib

> `/usr/lib/libmobileassetd.dylib`

```diff

-1788.0.0.0.4
-  __TEXT.__text: 0x2db918
+1837.0.0.0.0
+  __TEXT.__text: 0x2e5458
   __TEXT.__auth_stubs: 0x2be0
-  __TEXT.__objc_stubs: 0x22940
-  __TEXT.__objc_methlist: 0x10584
-  __TEXT.__const: 0x7b958
-  __TEXT.__cstring: 0x399fb
-  __TEXT.__objc_methname: 0x3e242
-  __TEXT.__objc_classname: 0xe55
-  __TEXT.__objc_methtype: 0x3f37
-  __TEXT.__oslogstring: 0x4f7a7
-  __TEXT.__gcc_except_tab: 0x4aa0
+  __TEXT.__objc_stubs: 0x22ba0
+  __TEXT.__objc_methlist: 0x1060c
+  __TEXT.__const: 0x7ba18
+  __TEXT.__cstring: 0x39c3b
+  __TEXT.__objc_methname: 0x3e77e
+  __TEXT.__objc_classname: 0xe64
+  __TEXT.__objc_methtype: 0x3f65
+  __TEXT.__oslogstring: 0x54037
+  __TEXT.__gcc_except_tab: 0xd248
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x1332
   __TEXT.__constg_swiftt: 0x1788

   __TEXT.__swift5_protos: 0x6c
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_capture: 0x30
-  __TEXT.__unwind_info: 0x4fa0
+  __TEXT.__unwind_info: 0x5e88
   __TEXT.__eh_frame: 0x3464
   __DATA_CONST.__auth_got: 0x1600
   __DATA_CONST.__got: 0x740
   __DATA_CONST.__auth_ptr: 0xac0
-  __DATA_CONST.__const: 0x85c8
-  __DATA_CONST.__cfstring: 0x2c040
+  __DATA_CONST.__const: 0x8540
+  __DATA_CONST.__cfstring: 0x2c2e0
   __DATA_CONST.__objc_classlist: 0x440
-  __DATA_CONST.__objc_catlist: 0x10
+  __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x99b8
-  __DATA_CONST.__objc_arraydata: 0xbf0
-  __DATA_CONST.__objc_arrayobj: 0x2b8
+  __DATA_CONST.__objc_selrefs: 0x9a58
+  __DATA_CONST.__objc_arraydata: 0xc00
+  __DATA_CONST.__objc_arrayobj: 0x2d0
   __DATA_CONST.__objc_intobj: 0x5b8
   __DATA_CONST.__objc_dictobj: 0x118
-  __DATA.__objc_const: 0x155a8
+  __DATA.__objc_const: 0x15478
   __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x858
+  __DATA.__objc_classrefs: 0x850
   __DATA.__objc_superrefs: 0x2f0
-  __DATA.__objc_ivar: 0x1408
+  __DATA.__objc_ivar: 0x13f0
   __DATA.__objc_data: 0x2b88
   __DATA.__data: 0x2ca8
   __DATA.__bss: 0x6668

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 00648A8B-D643-3E67-90B9-01D4E5857ADE
-  Functions: 9060
-  Symbols:   16235
-  CStrings:  22846
+  UUID: 22043F0B-9434-31BE-ACE0-9A10F67244D8
+  Functions: 9072
+  Symbols:   16609
+  CStrings:  23316
 
Symbols:
+ +[MABAACertManager _checkIsSupported]
+ +[MADAutoAssetControlManager autoJobAssetSetIDsForJob:mostRecentlyReceived:latestToVend:]
+ +[MADAutoAssetControlManager preferenceScheduledOnlyForAssetTypes]
+ -[DownloadInfo extractorRequired]
+ -[DownloadInfo setExtractorRequired:]
+ -[DownloadManager nwActivityObjectsByJobUUID]
+ -[DownloadManager setNwActivityObjectsByJobUUID:]
+ -[MAAutoAssetSelector(DaemonAdditions) isFullAssetSelector]
+ -[MABAACertManager _copyCachedCerts:]
+ -[MABAACertManager invalidateExistingCertsAndWait]
+ -[MABAACertManager issueAndWaitForCerts:]
+ -[MADAutoAssetConnector _chooseOrderForNextAttemptAndStartFirstJob:beginningOSTransaction:]
+ -[MADAutoAssetConnector action_ClearOSTransaction:error:]
+ -[MADAutoAssetConnector action_FiredRetryConnOrderAttemptFirstJobActive:error:]
+ -[MADAutoAssetConnector action_FiredRetryDiscTakeOSXactOrderAttempt1st:error:]
+ -[MADAutoAssetConnector action_OrderAttemptTakeOSXactFirstJobActive:error:]
+ -[MADAutoAssetConnector action_StartBackoffAndRetryWaitTimersClearOSXact:error:]
+ -[MADAutoAssetConnector action_StopBackoffTakeOSXactOrderAttempt1st:error:]
+ -[MADAutoAssetConnector action_StopBackoffTimerTakeOSTransaction:error:]
+ -[MADAutoAssetConnector action_TakeOSTransaction:error:]
+ -[MADAutoAssetConnector activeAttemptOSTransaction]
+ -[MADAutoAssetConnector osTransactionBegin:]
+ -[MADAutoAssetConnector osTransactionEnd:]
+ -[MADAutoAssetConnector setActiveAttemptOSTransaction:]
+ -[MADAutoAssetConnectorParam eventOSTransaction]
+ -[MADAutoAssetConnectorParam initWithMonitorMarkers:withMarkersNoRetry:withMarkersRequiringRetry:withEventOSTransaction:]
+ -[MADAutoAssetConnectorParam initWithParamType:withSafeSummary:withMonitorMarkers:withMarkersNoRetry:withMarkersRequiringRetry:withFinishedMarker:withEventOSTransaction:withPotentialNetworkFailure:withObservedNetworkPath:]
+ -[MADAutoAssetConnectorParam setEventOSTransaction:]
+ -[MADAutoAssetControlManager isAtomicInstancePartOfPSUS:]
+ -[MADAutoAssetControlManager osTransactionNameAutoJob:forJobUUID:]
+ -[MADAutoAssetControlManager osTransactionNameClientRequestedSetJob:]
+ -[MADAutoAssetControlManager osTransactionNameClientRequestedSingletonJob:]
+ -[MADAutoAssetControlManager osTransactionNamePreviouslyInFlightJob:]
+ -[MADAutoAssetControlManager osTransactionNameScheduledSetJob:]
+ -[MADAutoAssetControlManager osTransactionNameScheduledSingletonJob:]
+ -[MADAutoAssetControlManager osTransactionNameStagerDetermineJob:]
+ -[MADAutoAssetControlManager osTransactionNameStagerDownloadJob:]
+ -[MADAutoAssetControlManager preferenceScheduledOnlyForAssetTypes]
+ -[MADAutoAssetControlManager setPreferenceScheduledOnlyForAssetTypes:]
+ -[MADAutoAssetControlManager setStartupPerfResults:]
+ -[MADAutoAssetControlManager setStartupSignpost:]
+ -[MADAutoAssetControlManager startupPerfResults]
+ -[MADAutoAssetControlManager startupSignpost]
+ -[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) notifyCompletionCallbacksForSetJobKey:]
+ -[MADAutoAssetControlManagerParam eventOSTransaction]
+ -[MADAutoAssetControlManagerParam initForTriggeredNoActivity:]
+ -[MADAutoAssetControlManagerParam initForTriggeredSelectors:withEventOSTransaction:]
+ -[MADAutoAssetControlManagerParam initForTriggeredSets:withEventOSTransaction:]
+ -[MADAutoAssetControlManagerParam initWithParamType:withSafeSummary:withEventOSTransaction:withScheduledJobs:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withDownloadOptions:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withSetDescriptor:withAutoAssetDescriptors:withSetPolicy:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withStagedToDownloaded:withStagedLookupResults:withDownloadingDescriptor:withBaseForPatchDescriptor:withBaseForStagingDescriptors:withSchedulerInvolved:withPotentialNetworkFailure:withRequiringLoadPriorToUse:withClientDomainName:withAssetSetIdentifier:withSetConfiguration:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:]
+ -[MADAutoAssetControlManagerParam setEventOSTransaction:]
+ -[MADAutoAssetJob initForDescriptor:withLifetimeOSTransaction:baseForPatchDescriptor:withAutoAssetUUID:]
+ -[MADAutoAssetJob initForInstance:orForSelector:orForDescriptor:orForSetInstance:withLifetimeOSTransaction:withSetDesire:withSchedulerSetPolicy:withStagerSetPolicy:usingSetConfiguration:usingSetDescriptor:withBaseForPatchDescriptor:withAutoAssetUUID:downloadingUserInitiated:asStagerJob:usingCachedAutoAssetCatalog:]
+ -[MADAutoAssetJob initForInstance:withLifetimeOSTransaction:withAutoAssetUUID:downloadingUserInitiated:]
+ -[MADAutoAssetJob initForSelector:withLifetimeOSTransaction:withAutoAssetUUID:]
+ -[MADAutoAssetJob initForSelector:withLifetimeOSTransaction:withAutoAssetUUID:asStagerJob:withStagerSetPolicy:usingCachedAutoAssetCatalog:usingBaseForPatching:]
+ -[MADAutoAssetJob initForSetConfiguration:withLifetimeOSTransaction:withAutoAssetUUID:asStagerJob:withStagerSetPolicy:]
+ -[MADAutoAssetJob initForSetInstance:withLifetimeOSTransaction:withSchedulerSetPolicy:usingSetConfiguration:usingSetDescriptor:withAutoAssetUUID:]
+ -[MADAutoAssetJob initForSetInstance:withLifetimeOSTransaction:withSetDesire:usingSetConfiguration:usingSetDescriptor:withAutoAssetUUID:]
+ -[MADAutoAssetJob lifetimeOSTransaction]
+ -[MADAutoAssetJob setLifetimeOSTransaction:]
+ -[MADAutoAssetLocker _locateLockByPersistentEntryID:]
+ -[MADAutoAssetLocker locateLockByFullAssetSelector:]
+ -[MADAutoAssetLocker locateLocksBySelector:]
+ -[MADAutoAssetPersisted initForModule:ofModuleVersion:usingDispatchQueue:loggingByName:withVersionMigrator:]
+ -[MobileAssetKeyManager shouldDisableUIForUsage:assetAttributes:downloadOptions:]
+ GCC_except_table10
+ GCC_except_table100
+ GCC_except_table102
+ GCC_except_table103
+ GCC_except_table105
+ GCC_except_table106
+ GCC_except_table107
+ GCC_except_table110
+ GCC_except_table111
+ GCC_except_table113
+ GCC_except_table115
+ GCC_except_table116
+ GCC_except_table117
+ GCC_except_table119
+ GCC_except_table120
+ GCC_except_table124
+ GCC_except_table126
+ GCC_except_table127
+ GCC_except_table128
+ GCC_except_table130
+ GCC_except_table131
+ GCC_except_table132
+ GCC_except_table133
+ GCC_except_table134
+ GCC_except_table135
+ GCC_except_table137
+ GCC_except_table138
+ GCC_except_table140
+ GCC_except_table142
+ GCC_except_table145
+ GCC_except_table146
+ GCC_except_table147
+ GCC_except_table148
+ GCC_except_table149
+ GCC_except_table150
+ GCC_except_table151
+ GCC_except_table157
+ GCC_except_table159
+ GCC_except_table163
+ GCC_except_table164
+ GCC_except_table165
+ GCC_except_table166
+ GCC_except_table168
+ GCC_except_table169
+ GCC_except_table170
+ GCC_except_table171
+ GCC_except_table172
+ GCC_except_table174
+ GCC_except_table175
+ GCC_except_table177
+ GCC_except_table178
+ GCC_except_table179
+ GCC_except_table180
+ GCC_except_table181
+ GCC_except_table182
+ GCC_except_table183
+ GCC_except_table184
+ GCC_except_table185
+ GCC_except_table186
+ GCC_except_table187
+ GCC_except_table188
+ GCC_except_table189
+ GCC_except_table19
+ GCC_except_table190
+ GCC_except_table192
+ GCC_except_table194
+ GCC_except_table200
+ GCC_except_table23
+ GCC_except_table254
+ GCC_except_table30
+ GCC_except_table313
+ GCC_except_table32
+ GCC_except_table322
+ GCC_except_table324
+ GCC_except_table326
+ GCC_except_table329
+ GCC_except_table330
+ GCC_except_table331
+ GCC_except_table332
+ GCC_except_table333
+ GCC_except_table334
+ GCC_except_table335
+ GCC_except_table336
+ GCC_except_table337
+ GCC_except_table338
+ GCC_except_table339
+ GCC_except_table34
+ GCC_except_table341
+ GCC_except_table342
+ GCC_except_table343
+ GCC_except_table344
+ GCC_except_table345
+ GCC_except_table349
+ GCC_except_table353
+ GCC_except_table354
+ GCC_except_table355
+ GCC_except_table356
+ GCC_except_table36
+ GCC_except_table361
+ GCC_except_table362
+ GCC_except_table365
+ GCC_except_table366
+ GCC_except_table367
+ GCC_except_table369
+ GCC_except_table370
+ GCC_except_table371
+ GCC_except_table372
+ GCC_except_table373
+ GCC_except_table374
+ GCC_except_table375
+ GCC_except_table40
+ GCC_except_table41
+ GCC_except_table421
+ GCC_except_table427
+ GCC_except_table428
+ GCC_except_table429
+ GCC_except_table430
+ GCC_except_table431
+ GCC_except_table432
+ GCC_except_table433
+ GCC_except_table434
+ GCC_except_table45
+ GCC_except_table50
+ GCC_except_table516
+ GCC_except_table518
+ GCC_except_table52
+ GCC_except_table56
+ GCC_except_table574
+ GCC_except_table59
+ GCC_except_table609
+ GCC_except_table61
+ GCC_except_table617
+ GCC_except_table619
+ GCC_except_table633
+ GCC_except_table660
+ GCC_except_table67
+ GCC_except_table72
+ GCC_except_table73
+ GCC_except_table75
+ GCC_except_table76
+ GCC_except_table767
+ GCC_except_table768
+ GCC_except_table769
+ GCC_except_table77
+ GCC_except_table772
+ GCC_except_table78
+ GCC_except_table79
+ GCC_except_table81
+ GCC_except_table85
+ GCC_except_table87
+ GCC_except_table88
+ GCC_except_table89
+ GCC_except_table90
+ GCC_except_table91
+ GCC_except_table93
+ GCC_except_table94
+ GCC_except_table98
+ GCC_except_table99
+ MALOG_ANALYTICS_OBSERVER_MASK_block_invoke.setupSignalHandlersDispatchOnce
+ MALOG_ANALYTICS_OBSERVER_MASK_block_invoke_2.signalSources
+ MALOG_ANALYTICS_OBSERVER_MASK_block_invoke_2.signals
+ OBJC_IVAR_$_DownloadInfo._extractorRequired
+ OBJC_IVAR_$_DownloadManager._nwActivityObjectsByJobUUID
+ OBJC_IVAR_$_MABAACertManager._cachedCertArray
+ OBJC_IVAR_$_MABAACertManager._cachedKey
+ OBJC_IVAR_$_MABAACertManager._cachedTime
+ OBJC_IVAR_$_MABAACertManager._requestTime
+ OBJC_IVAR_$_MABAACertManager._responseTime
+ OBJC_IVAR_$_MADAutoAssetConnector._activeAttemptOSTransaction
+ OBJC_IVAR_$_MADAutoAssetConnectorParam._eventOSTransaction
+ OBJC_IVAR_$_MADAutoAssetControlManager._preferenceScheduledOnlyForAssetTypes
+ OBJC_IVAR_$_MADAutoAssetControlManager._startupPerfResults
+ OBJC_IVAR_$_MADAutoAssetControlManager._startupSignpost
+ OBJC_IVAR_$_MADAutoAssetControlManagerParam._eventOSTransaction
+ OBJC_IVAR_$_MADAutoAssetJob._lifetimeOSTransaction
+ _AccelerateCrypto_SHA3_keccak_2x_hwassist
+ __105-[MobileAssetKeyManager requestServerForDecryptionKey:recipientPrivateKey:downloadOptions:disableUI:err:]_block_invoke.1248
+ __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1675
+ __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1682
+ __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1683
+ __110-[DownloadManager pallasRequestV2:normalizedType:withPurpose:options:using:with:autoAssetJob:clientName:then:]_block_invoke.2175
+ __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1169
+ __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1173
+ __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1189
+ __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1251
+ __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1256
+ __149-[DownloadManager registerCatalogDownloadJob:withPurpose:usingDownloadOptions:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.2349
+ __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1275
+ __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1285
+ __173-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1158
+ __173-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1159
+ __178-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1167
+ __178-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1168
+ __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2282
+ __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2294
+ __22-[ControlManager init]_block_invoke.1218
+ __24-[MABrainUpdater start:]_block_invoke.1094
+ __24-[MABrainUpdater start:]_block_invoke.1099
+ __24-[MABrainUpdater start:]_block_invoke.1103
+ __27-[MABrainUpdater schedule:]_block_invoke.1110
+ __27-[MABrainUpdater schedule:]_block_invoke.1152
+ __27-[MABrainUpdater schedule:]_block_invoke.1157
+ __27-[MABrainUpdater schedule:]_block_invoke_2.1153
+ __287-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:]_block_invoke.2330
+ __36-[MABrainUpdater update:completion:]_block_invoke.1221
+ __36-[MABrainUpdater update:completion:]_block_invoke.1222
+ __36-[MABrainUpdater update:completion:]_block_invoke.1229
+ __37-[DownloadManager startDownloadTimer]_block_invoke.1753
+ __41-[MobileAssetHealthReport scheduleReport]_block_invoke.1104
+ __44-[ControlManager handleClientConnection:on:]_block_invoke.1732
+ __44-[ControlManager handleClientConnection:on:]_block_invoke.1733
+ __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1201
+ __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1248
+ __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2230
+ __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1902
+ __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1903
+ __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1909
+ __51-[MABrainUpdater install:asset:options:completion:]_block_invoke.1205
+ __51-[MABrainUpdater install:asset:options:completion:]_block_invoke.1206
+ __52-[DownloadManager reportDownloadAttemptResult:with:]_block_invoke.1863
+ __53-[ControlManager getStateOfAsset:incoming:assetType:]_block_invoke.1496
+ __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1300
+ __57-[ControlManager handleUpdateMABrain:message:clientName:]_block_invoke.1965
+ __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1263
+ __60-[ControlManager removeAssetDir:assetType:clientName:using:]_block_invoke.1567
+ __64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke.376
+ __64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke.394
+ __64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke_2.400
+ __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1230
+ __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1252
+ __66-[ControlManager moveAssetIntoRepo:forType:forAsset:cleanUp:with:]_block_invoke.1930
+ __66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke.1190
+ __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke.1217
+ __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke.1224
+ __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke_2.1225
+ __69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.2350
+ __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1086
+ __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1087
+ __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1088
+ __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke.2550
+ __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2551
+ __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1202
+ __77-[ControlManager updateSpaceAttributionForBundleID:assetPath:doRegistration:]_block_invoke.1211
+ __79-[MobileAssetHealthReport _submitReportToCoreAnalytics:commonFields:sessionId:]_block_invoke.1192
+ __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1238
+ __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1241
+ __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.3346
+ __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.3347
+ __MABrainUtilityScheduleDeviceUnlockAction_block_invoke.401
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_MAAutoAssetSelector_$_DaemonAdditions
+ __OBJC_$_CATEGORY_MAAutoAssetSelector_$_DaemonAdditions
+ ___31+[MABAACertManager isSupported]_block_invoke
+ ___37-[MABAACertManager _copyCachedCerts:]_block_invoke
+ ___41-[MABAACertManager issueAndWaitForCerts:]_block_invoke
+ ___50-[MABAACertManager invalidateExistingCertsAndWait]_block_invoke
+ ___89+[MADAutoAssetControlManager autoJobAssetSetIDsForJob:mostRecentlyReceived:latestToVend:]_block_invoke
+ ___block_descriptor_104_e8_32s40s48s56s64bs72r80r88r96r_e11_v16?0B8B12ls32l8r72l8s40l8s48l8r80l8r88l8r96l8s64l8s56l8
+ ___block_descriptor_176_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144bs152r160r_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24lr152l8s32l8s40l8s48l8r160l8s56l8s64l8s72l8s80l8s88l8s144l8s96l8s104l8s112l8s120l8s128l8s136l8
+ ___block_descriptor_40_e8_32s_e87_v32?0^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}8"NSArray"16"NSError"24ls32l8
+ ___block_descriptor_56_e8_32s40s_e87_v32?0^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}8"NSArray"16"NSError"24ls32l8s40l8
+ ___block_descriptor_68_e8_32s40s_e36_v36?0B8Q12"NSString"20"NSError"28ls32l8s40l8
+ ___block_descriptor_80_e8_32s40s48r56r64r_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24lr48l8s32l8r56l8r64l8s40l8
+ __block_descriptor_tmp.151
+ __block_descriptor_tmp.170
+ __block_literal_global.1075
+ __block_literal_global.1083
+ __block_literal_global.1085
+ __block_literal_global.1090
+ __block_literal_global.1097
+ __block_literal_global.1106
+ __block_literal_global.1108
+ __block_literal_global.1115
+ __block_literal_global.1117
+ __block_literal_global.1126
+ __block_literal_global.1127
+ __block_literal_global.1131
+ __block_literal_global.1136
+ __block_literal_global.1153
+ __block_literal_global.1155
+ __block_literal_global.1160
+ __block_literal_global.1185
+ __block_literal_global.1200
+ __block_literal_global.1206
+ __block_literal_global.1229
+ __block_literal_global.1234
+ __block_literal_global.1253
+ __block_literal_global.1254
+ __block_literal_global.1340
+ __block_literal_global.1342
+ __block_literal_global.1349
+ __block_literal_global.1350
+ __block_literal_global.1378
+ __block_literal_global.1384
+ __block_literal_global.1389
+ __block_literal_global.1394
+ __block_literal_global.1399
+ __block_literal_global.1421
+ __block_literal_global.153
+ __block_literal_global.1578
+ __block_literal_global.1611
+ __block_literal_global.1650
+ __block_literal_global.1711
+ __block_literal_global.1716
+ __block_literal_global.172
+ __block_literal_global.1721
+ __block_literal_global.1724
+ __block_literal_global.1755
+ __block_literal_global.1779
+ __block_literal_global.1792
+ __block_literal_global.2080
+ __block_literal_global.2102
+ __block_literal_global.2280
+ __block_literal_global.2288
+ __block_literal_global.2296
+ __block_literal_global.2304
+ __block_literal_global.2312
+ __block_literal_global.2320
+ __block_literal_global.2328
+ __block_literal_global.2342
+ __block_literal_global.2412
+ __block_literal_global.2805
+ __block_literal_global.3976
+ __block_literal_global.411
+ __block_literal_global.5016
+ __handleCacheDeletePurgeCallbackForVolume_block_invoke.1120
+ __handleCacheDeletePurgeableCallbackForVolume_block_invoke.1116
+ _cckeccak_absorb_blocks_parallel
+ _ccsha3_256_vng_hwassist_compress_parallel
+ _ccsha3_384_vng_hwassist_compress_parallel
+ _ccsha3_512_vng_hwassist_compress_parallel
+ _isSoftwareUpdateBrainType
+ _isUserInteractionAllowedType
+ _kMobileAssetPreferencesAutoAssetScheduledOnlyForAssetTypes
+ _objc_msgSend$_checkIsSupported
+ _objc_msgSend$_chooseOrderForNextAttemptAndStartFirstJob:beginningOSTransaction:
+ _objc_msgSend$_copyCachedCerts:
+ _objc_msgSend$_locateLockByPersistentEntryID:
+ _objc_msgSend$action_ClearOSTransaction:error:
+ _objc_msgSend$action_FiredRetryConnOrderAttemptFirstJobActive:error:
+ _objc_msgSend$action_FiredRetryDiscTakeOSXactOrderAttempt1st:error:
+ _objc_msgSend$action_OrderAttemptTakeOSXactFirstJobActive:error:
+ _objc_msgSend$action_StartBackoffAndRetryWaitTimersClearOSXact:error:
+ _objc_msgSend$action_StopBackoffTakeOSXactOrderAttempt1st:error:
+ _objc_msgSend$action_StopBackoffTimerTakeOSTransaction:error:
+ _objc_msgSend$action_TakeOSTransaction:error:
+ _objc_msgSend$activeAttemptOSTransaction
+ _objc_msgSend$autoJobAssetSetIDsForJob:mostRecentlyReceived:latestToVend:
+ _objc_msgSend$destinationOfSymbolicLinkAtPath:error:
+ _objc_msgSend$extractorRequired
+ _objc_msgSend$initForDescriptor:withLifetimeOSTransaction:baseForPatchDescriptor:withAutoAssetUUID:
+ _objc_msgSend$initForInstance:orForSelector:orForDescriptor:orForSetInstance:withLifetimeOSTransaction:withSetDesire:withSchedulerSetPolicy:withStagerSetPolicy:usingSetConfiguration:usingSetDescriptor:withBaseForPatchDescriptor:withAutoAssetUUID:downloadingUserInitiated:asStagerJob:usingCachedAutoAssetCatalog:
+ _objc_msgSend$initForInstance:withLifetimeOSTransaction:withAutoAssetUUID:downloadingUserInitiated:
+ _objc_msgSend$initForModule:ofModuleVersion:usingDispatchQueue:loggingByName:withVersionMigrator:
+ _objc_msgSend$initForSelector:withLifetimeOSTransaction:withAutoAssetUUID:
+ _objc_msgSend$initForSelector:withLifetimeOSTransaction:withAutoAssetUUID:asStagerJob:withStagerSetPolicy:usingCachedAutoAssetCatalog:usingBaseForPatching:
+ _objc_msgSend$initForSetConfiguration:withLifetimeOSTransaction:withAutoAssetUUID:asStagerJob:withStagerSetPolicy:
+ _objc_msgSend$initForSetInstance:withLifetimeOSTransaction:withSchedulerSetPolicy:usingSetConfiguration:usingSetDescriptor:withAutoAssetUUID:
+ _objc_msgSend$initForSetInstance:withLifetimeOSTransaction:withSetDesire:usingSetConfiguration:usingSetDescriptor:withAutoAssetUUID:
+ _objc_msgSend$initForTriggeredNoActivity:
+ _objc_msgSend$initForTriggeredSelectors:withEventOSTransaction:
+ _objc_msgSend$initForTriggeredSets:withEventOSTransaction:
+ _objc_msgSend$initWithMonitorMarkers:withMarkersNoRetry:withMarkersRequiringRetry:withEventOSTransaction:
+ _objc_msgSend$initWithParamType:withSafeSummary:withEventOSTransaction:withScheduledJobs:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withDownloadOptions:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withSetDescriptor:withAutoAssetDescriptors:withSetPolicy:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withStagedToDownloaded:withStagedLookupResults:withDownloadingDescriptor:withBaseForPatchDescriptor:withBaseForStagingDescriptors:withSchedulerInvolved:withPotentialNetworkFailure:withRequiringLoadPriorToUse:withClientDomainName:withAssetSetIdentifier:withSetConfiguration:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:
+ _objc_msgSend$initWithParamType:withSafeSummary:withMonitorMarkers:withMarkersNoRetry:withMarkersRequiringRetry:withFinishedMarker:withEventOSTransaction:withPotentialNetworkFailure:withObservedNetworkPath:
+ _objc_msgSend$invalidateExistingCertsAndWait
+ _objc_msgSend$isAtomicInstancePartOfPSUS:
+ _objc_msgSend$isFullAssetSelector
+ _objc_msgSend$issueAndWaitForCerts:
+ _objc_msgSend$lifetimeOSTransaction
+ _objc_msgSend$locateLockByFullAssetSelector:
+ _objc_msgSend$locateLocksBySelector:
+ _objc_msgSend$notifyCompletionCallbacksForSetJobKey:
+ _objc_msgSend$nwActivityObjectsByJobUUID
+ _objc_msgSend$osTransactionBegin:
+ _objc_msgSend$osTransactionEnd:
+ _objc_msgSend$osTransactionNameAutoJob:forJobUUID:
+ _objc_msgSend$osTransactionNameClientRequestedSetJob:
+ _objc_msgSend$osTransactionNameClientRequestedSingletonJob:
+ _objc_msgSend$osTransactionNamePreviouslyInFlightJob:
+ _objc_msgSend$osTransactionNameScheduledSetJob:
+ _objc_msgSend$osTransactionNameScheduledSingletonJob:
+ _objc_msgSend$osTransactionNameStagerDetermineJob:
+ _objc_msgSend$osTransactionNameStagerDownloadJob:
+ _objc_msgSend$preferenceScheduledOnlyForAssetTypes
+ _objc_msgSend$setActiveAttemptOSTransaction:
+ _objc_msgSend$setExtractorRequired:
+ _objc_msgSend$setLifetimeOSTransaction:
+ _objc_msgSend$setStartupSignpost:
+ _objc_msgSend$shouldDisableUIForUsage:assetAttributes:downloadOptions:
+ _objc_msgSend$startupPerfResults
+ _objc_msgSend$startupSignpost
+ isSupported.once
+ isSupported.supported
- -[DownloadManager nwActivityObjects]
- -[DownloadManager nwQueue]
- -[DownloadManager setNwActivityObjects:]
- -[DownloadManager setNwQueue:]
- -[MABAACertManager copyPreviouslyCreatedCertsIfPresent:]
- -[MABAACertManager issueAndCopyCertsInternal:]
- -[MABAACertManager logger]
- -[MABrainRestartManager logger]
- -[MADAutoAssetConnector _chooseOrderForNextAttemptAndStartFirstJob:]
- -[MADAutoAssetConnector action_FiredRetryWaitOrderAttemptFirstJobActive:error:]
- -[MADAutoAssetConnector action_OrderAttemptFirstJobActive:error:]
- -[MADAutoAssetConnector action_StartBackoffAndRetryWaitTimers:error:]
- -[MADAutoAssetConnector action_StopBackoffOrderAttemptFirstJobActive:error:]
- -[MADAutoAssetConnector logger]
- -[MADAutoAssetConnectorParam initWithMonitorMarkers:withMarkersNoRetry:withMarkersRequiringRetry:]
- -[MADAutoAssetConnectorParam initWithParamType:withSafeSummary:withMonitorMarkers:withMarkersNoRetry:withMarkersRequiringRetry:withFinishedMarker:withPotentialNetworkFailure:withObservedNetworkPath:]
- -[MADAutoAssetControlManager _longSummary]
- -[MADAutoAssetControlManager _removeAllQueuedForEliminateSelector:]
- -[MADAutoAssetControlManager isAnyAssetFromSetFromNewOSPromoted:]
- -[MADAutoAssetControlManager locateSetDescriptorForStagingDescriptor:]
- -[MADAutoAssetControlManager locateStagedSetDescriptorFor:]
- -[MADAutoAssetControlManager logger]
- -[MADAutoAssetControlManager newSetDescriptorIfOtherSatisfying:forSetInfoInstance:]
- -[MADAutoAssetControlManager perfResultsCPI]
- -[MADAutoAssetControlManager setPerfResultsCPI:]
- -[MADAutoAssetControlManager setStagedAssetToSetDescriptorCache:]
- -[MADAutoAssetControlManager setStagedIsNewOSPromotedCache:]
- -[MADAutoAssetControlManager setStagedToDownloaded:]
- -[MADAutoAssetControlManager setStartupSignpostCPI:]
- -[MADAutoAssetControlManager stagedAssetToSetDescriptorCache]
- -[MADAutoAssetControlManager stagedIsNewOSPromotedCache]
- -[MADAutoAssetControlManager stagedToDownloaded]
- -[MADAutoAssetControlManager startupSignpostCPI]
- -[MADAutoAssetControlManagerParam initForTriggeredNoActivity]
- -[MADAutoAssetControlManagerParam initForTriggeredSelectors:]
- -[MADAutoAssetControlManagerParam initForTriggeredSets:]
- -[MADAutoAssetControlManagerParam initWithParamType:withSafeSummary:withScheduledJobs:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withDownloadOptions:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withSetDescriptor:withAutoAssetDescriptors:withSetPolicy:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withStagedToDownloaded:withStagedLookupResults:withDownloadingDescriptor:withBaseForPatchDescriptor:withBaseForStagingDescriptors:withSchedulerInvolved:withPotentialNetworkFailure:withRequiringLoadPriorToUse:withClientDomainName:withAssetSetIdentifier:withSetConfiguration:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:]
- -[MADAutoAssetJob initForDescriptor:baseForPatchDescriptor:withAutoAssetUUID:]
- -[MADAutoAssetJob initForInstance:orForSelector:orForDescriptor:orForSetInstance:withSetDesire:withSchedulerSetPolicy:withStagerSetPolicy:usingSetConfiguration:usingSetDescriptor:withBaseForPatchDescriptor:withAutoAssetUUID:downloadingUserInitiated:asStagerJob:usingCachedAutoAssetCatalog:]
- -[MADAutoAssetJob initForInstance:withAutoAssetUUID:downloadingUserInitiated:]
- -[MADAutoAssetJob initForSelector:withAutoAssetUUID:]
- -[MADAutoAssetJob initForSelector:withAutoAssetUUID:asStagerJob:withStagerSetPolicy:usingCachedAutoAssetCatalog:usingBaseForPatching:]
- -[MADAutoAssetJob initForSetConfiguration:withAutoAssetUUID:asStagerJob:withStagerSetPolicy:]
- -[MADAutoAssetJob initForSetInstance:withSchedulerSetPolicy:usingSetConfiguration:usingSetDescriptor:withAutoAssetUUID:]
- -[MADAutoAssetJob initForSetInstance:withSetDesire:usingSetConfiguration:usingSetDescriptor:withAutoAssetUUID:]
- -[MADAutoAssetJob logger]
- -[MADAutoAssetLocker locateLockBySelector:]
- -[MADAutoAssetLocker logger]
- -[MADAutoAssetPersisted initForModule:ofModuleVersion:usingDispatchQueue:usingLogger:loggingByName:withVersionMigrator:]
- -[MADAutoAssetPersisted logger]
- -[MADAutoAssetScheduler logger]
- -[MADAutoAssetSecure logger]
- -[MADAutoAssetStager logger]
- -[MADCacheDeleteManager logger]
- -[MAKeyManagerDownloadSessionDelegate logger]
- -[MobileAssetKeyManager logger]
- FROM_LOCATION_GRAFT_REPLY_block_invoke.setupSignalHandlersDispatchOnce
- FROM_LOCATION_GRAFT_REPLY_block_invoke_2.signalSources
- FROM_LOCATION_GRAFT_REPLY_block_invoke_2.signals
- GCC_except_table16
- GCC_except_table257
- GCC_except_table415
- GCC_except_table603
- GCC_except_table605
- GCC_except_table613
- GCC_except_table627
- OBJC_IVAR_$_DownloadManager._nwActivityObjects
- OBJC_IVAR_$_DownloadManager._nwQueue
- OBJC_IVAR_$_MABAACertManager._logger
- OBJC_IVAR_$_MABrainRestartManager._logger
- OBJC_IVAR_$_MADAutoAssetConnector._logger
- OBJC_IVAR_$_MADAutoAssetControlManager._logger
- OBJC_IVAR_$_MADAutoAssetControlManager._perfResultsCPI
- OBJC_IVAR_$_MADAutoAssetControlManager._stagedAssetToSetDescriptorCache
- OBJC_IVAR_$_MADAutoAssetControlManager._stagedIsNewOSPromotedCache
- OBJC_IVAR_$_MADAutoAssetControlManager._stagedToDownloaded
- OBJC_IVAR_$_MADAutoAssetControlManager._startupSignpostCPI
- OBJC_IVAR_$_MADAutoAssetJob._logger
- OBJC_IVAR_$_MADAutoAssetLocker._logger
- OBJC_IVAR_$_MADAutoAssetPersisted._logger
- OBJC_IVAR_$_MADAutoAssetScheduler._logger
- OBJC_IVAR_$_MADAutoAssetSecure._logger
- OBJC_IVAR_$_MADAutoAssetStager._logger
- OBJC_IVAR_$_MADCacheDeleteManager._logger
- OBJC_IVAR_$_MAKeyManagerDownloadSessionDelegate._logger
- OBJC_IVAR_$_MobileAssetKeyManager._logger
- _OBJC_CLASS_$_SUCoreLog
- __105-[MobileAssetKeyManager requestServerForDecryptionKey:recipientPrivateKey:downloadOptions:disableUI:err:]_block_invoke.1233
- __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1669
- __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1676
- __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1677
- __110-[DownloadManager pallasRequestV2:normalizedType:withPurpose:options:using:with:autoAssetJob:clientName:then:]_block_invoke.2173
- __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1170
- __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1174
- __121+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:completion:]_block_invoke.1190
- __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1253
- __128+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:completion:]_block_invoke.1257
- __149-[DownloadManager registerCatalogDownloadJob:withPurpose:usingDownloadOptions:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.2350
- __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1276
- __152-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:completion:]_block_invoke.1286
- __173-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1155
- __173-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1156
- __178-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1164
- __178-[MADAutoAssetControlManager(SoftwareUpdateSuspendResume) _handleSuspendForSoftwareUpdate_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1165
- __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2283
- __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2295
- __22-[ControlManager init]_block_invoke.1215
- __24-[MABrainUpdater start:]_block_invoke.1091
- __24-[MABrainUpdater start:]_block_invoke.1096
- __24-[MABrainUpdater start:]_block_invoke.1100
- __27-[MABrainUpdater schedule:]_block_invoke.1107
- __27-[MABrainUpdater schedule:]_block_invoke.1149
- __27-[MABrainUpdater schedule:]_block_invoke.1154
- __27-[MABrainUpdater schedule:]_block_invoke_2.1150
- __287-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:]_block_invoke.2331
- __36-[MABrainUpdater update:completion:]_block_invoke.1218
- __36-[MABrainUpdater update:completion:]_block_invoke.1219
- __36-[MABrainUpdater update:completion:]_block_invoke.1226
- __37-[DownloadManager startDownloadTimer]_block_invoke.1751
- __41-[MobileAssetHealthReport scheduleReport]_block_invoke.1098
- __44-[ControlManager handleClientConnection:on:]_block_invoke.1726
- __44-[ControlManager handleClientConnection:on:]_block_invoke.1727
- __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1199
- __45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1246
- __46-[MABAACertManager issueAndCopyCertsInternal:]_block_invoke.438
- __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2228
- __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1900
- __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1901
- __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1907
- __51-[MABrainUpdater install:asset:options:completion:]_block_invoke.1202
- __51-[MABrainUpdater install:asset:options:completion:]_block_invoke.1203
- __52-[DownloadManager reportDownloadAttemptResult:with:]_block_invoke.1861
- __53-[ControlManager getStateOfAsset:incoming:assetType:]_block_invoke.1493
- __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1295
- __54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1302
- __57-[ControlManager handleUpdateMABrain:message:clientName:]_block_invoke.1959
- __60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1266
- __60-[ControlManager removeAssetDir:assetType:clientName:using:]_block_invoke.1561
- __64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke.373
- __64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke.391
- __64-[MABrainScanner locateAvailableUpdateBrain:options:completion:]_block_invoke_2.397
- __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1232
- __65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1253
- __66-[ControlManager moveAssetIntoRepo:forType:forAsset:cleanUp:with:]_block_invoke.1924
- __66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke.1187
- __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke.1218
- __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke.1225
- __68+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:completion:]_block_invoke_2.1226
- __69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.2323
- __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1083
- __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1084
- __70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1085
- __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke.2520
- __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2521
- __75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1205
- __77-[ControlManager updateSpaceAttributionForBundleID:assetPath:doRegistration:]_block_invoke.1208
- __79-[MobileAssetHealthReport _submitReportToCoreAnalytics:commonFields:sessionId:]_block_invoke.1189
- __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1240
- __90+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:allowingNetwork:completion:]_block_invoke.1242
- __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.3331
- __94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.3332
- __MABrainUtilityScheduleDeviceUnlockAction_block_invoke.398
- ___46-[MABAACertManager issueAndCopyCertsInternal:]_block_invoke
- ___47-[MABAACertManager issueAndCopySelfSignedCert:]_block_invoke
- ___56-[MABAACertManager copyPreviouslyCreatedCertsIfPresent:]_block_invoke
- ___58-[DownloadManager completeNWActivity:withParams:andError:]_block_invoke
- ___67-[MABAACertManager copyBase64EncodedCertificateChain:referenceKey:]_block_invoke
- ___block_descriptor_176_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s152bs160r_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24lr160l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s152l8s104l8s112l8s120l8s128l8s136l8s144l8
- ___block_descriptor_56_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_57_e8_32s40r_e5_v8?0ls32l8r40l8
- ___block_descriptor_60_e8_32s40s_e36_v36?0B8Q12"NSString"20"NSError"28ls32l8s40l8
- ___block_descriptor_65_e8_32s40r48r56r_e87_v32?0^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}8"NSArray"16"NSError"24lr40l8r48l8r56l8s32l8
- ___block_descriptor_72_e8_32s40s48r56r64r_e87_v32?0^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}8"NSArray"16"NSError"24lr48l8r56l8s32l8r64l8s40l8
- ___block_descriptor_72_e8_32s40s48r56r_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24lr48l8s32l8r56l8s40l8
- ___block_descriptor_96_e8_32s40s48s56s64bs72r80r88r_e8_v12?0B8ls32l8r72l8s40l8s48l8s64l8s56l8r80l8r88l8
- __block_descriptor_tmp.150
- __block_descriptor_tmp.169
- __block_literal_global.1069
- __block_literal_global.1084
- __block_literal_global.1086
- __block_literal_global.1087
- __block_literal_global.1094
- __block_literal_global.1102
- __block_literal_global.1103
- __block_literal_global.1112
- __block_literal_global.1114
- __block_literal_global.1118
- __block_literal_global.1123
- __block_literal_global.1128
- __block_literal_global.1133
- __block_literal_global.1150
- __block_literal_global.1152
- __block_literal_global.1157
- __block_literal_global.1182
- __block_literal_global.1196
- __block_literal_global.1203
- __block_literal_global.1228
- __block_literal_global.1250
- __block_literal_global.1255
- __block_literal_global.1334
- __block_literal_global.1336
- __block_literal_global.1341
- __block_literal_global.1343
- __block_literal_global.1375
- __block_literal_global.1381
- __block_literal_global.1386
- __block_literal_global.1391
- __block_literal_global.1396
- __block_literal_global.1418
- __block_literal_global.152
- __block_literal_global.1575
- __block_literal_global.1608
- __block_literal_global.1647
- __block_literal_global.171
- __block_literal_global.1712
- __block_literal_global.1717
- __block_literal_global.1722
- __block_literal_global.1725
- __block_literal_global.1756
- __block_literal_global.1780
- __block_literal_global.1789
- __block_literal_global.2078
- __block_literal_global.2100
- __block_literal_global.2242
- __block_literal_global.2253
- __block_literal_global.2261
- __block_literal_global.2277
- __block_literal_global.2285
- __block_literal_global.2293
- __block_literal_global.2301
- __block_literal_global.2309
- __block_literal_global.2410
- __block_literal_global.2799
- __block_literal_global.3961
- __block_literal_global.408
- __block_literal_global.4986
- __handleCacheDeletePurgeCallbackForVolume_block_invoke.1117
- __handleCacheDeletePurgeableCallbackForVolume_block_invoke.1113
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_CryptoKit_Static
- __swift_FORCE_LOAD_$_swiftDarwin_$_MobileAssetKeyManager
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_CryptoKit_Static
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_MobileAssetKeyManager
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_CryptoKit_Static
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_MobileAssetKeyManager
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_CryptoKit_Static
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_MobileAssetKeyManager
- _objc_msgSend$_chooseOrderForNextAttemptAndStartFirstJob:
- _objc_msgSend$action_FiredRetryWaitOrderAttemptFirstJobActive:error:
- _objc_msgSend$action_OrderAttemptFirstJobActive:error:
- _objc_msgSend$action_StartBackoffAndRetryWaitTimers:error:
- _objc_msgSend$action_StopBackoffOrderAttemptFirstJobActive:error:
- _objc_msgSend$copyPreviouslyCreatedCertsIfPresent:
- _objc_msgSend$doesSetDescriptorWithoutVersion:referenceAssetDescriptor:
- _objc_msgSend$initForDescriptor:baseForPatchDescriptor:withAutoAssetUUID:
- _objc_msgSend$initForInstance:orForSelector:orForDescriptor:orForSetInstance:withSetDesire:withSchedulerSetPolicy:withStagerSetPolicy:usingSetConfiguration:usingSetDescriptor:withBaseForPatchDescriptor:withAutoAssetUUID:downloadingUserInitiated:asStagerJob:usingCachedAutoAssetCatalog:
- _objc_msgSend$initForInstance:withAutoAssetUUID:downloadingUserInitiated:
- _objc_msgSend$initForModule:ofModuleVersion:usingDispatchQueue:usingLogger:loggingByName:withVersionMigrator:
- _objc_msgSend$initForSelector:withAutoAssetUUID:
- _objc_msgSend$initForSelector:withAutoAssetUUID:asStagerJob:withStagerSetPolicy:usingCachedAutoAssetCatalog:usingBaseForPatching:
- _objc_msgSend$initForSetConfiguration:withAutoAssetUUID:asStagerJob:withStagerSetPolicy:
- _objc_msgSend$initForSetInstance:withSchedulerSetPolicy:usingSetConfiguration:usingSetDescriptor:withAutoAssetUUID:
- _objc_msgSend$initForSetInstance:withSetDesire:usingSetConfiguration:usingSetDescriptor:withAutoAssetUUID:
- _objc_msgSend$initForTriggeredNoActivity
- _objc_msgSend$initForTriggeredSelectors:
- _objc_msgSend$initForTriggeredSets:
- _objc_msgSend$initWithCategory:
- _objc_msgSend$initWithMonitorMarkers:withMarkersNoRetry:withMarkersRequiringRetry:
- _objc_msgSend$initWithParamType:withSafeSummary:withMonitorMarkers:withMarkersNoRetry:withMarkersRequiringRetry:withFinishedMarker:withPotentialNetworkFailure:withObservedNetworkPath:
- _objc_msgSend$initWithParamType:withSafeSummary:withScheduledJobs:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withDownloadOptions:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withSetDescriptor:withAutoAssetDescriptors:withSetPolicy:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withStagedToDownloaded:withStagedLookupResults:withDownloadingDescriptor:withBaseForPatchDescriptor:withBaseForStagingDescriptors:withSchedulerInvolved:withPotentialNetworkFailure:withRequiringLoadPriorToUse:withClientDomainName:withAssetSetIdentifier:withSetConfiguration:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:
- _objc_msgSend$isAnyAssetFromSetFromNewOSPromoted:
- _objc_msgSend$issueAndCopyCertsInternal:
- _objc_msgSend$locateLockBySelector:
- _objc_msgSend$locateSetDescriptorForStagingDescriptor:
- _objc_msgSend$locateStagedSetDescriptorFor:
- _objc_msgSend$logger
- _objc_msgSend$nwActivityObjects
- _objc_msgSend$oslog
- _objc_msgSend$perfResultsCPI
- _objc_msgSend$setStagedAssetToSetDescriptorCache:
- _objc_msgSend$setStagedIsNewOSPromotedCache:
- _objc_msgSend$setStagedToDownloaded:
- _objc_msgSend$setStartupSignpostCPI:
- _objc_msgSend$stagedAssetToSetDescriptorCache
- _objc_msgSend$stagedIsNewOSPromotedCache
- _objc_msgSend$startupSignpostCPI
- isExternalPreReleaseAssetType.isVM
- kMADeviceIdentityQueue_block_invoke.storeBootManifestHashDispatchOnce
CStrings:
+ "\n#_%{public}@:%{public}@ (%ld of %ld) [%{public}@] | (%{public}@) intervalSecs:%{public}@ | remainingSecs:%{public}@ | setPolicy:%{public}@"
+ "\"\""
+ "%@:osTransactionBegin"
+ "%@:osTransactionEnd"
+ "%{public, signpost.description:end_time}llu Bytes=%{public, signpost.telemetry:number1,name=Bytes}lld Stalls=%{public, signpost.telemetry:number2,name=Stalls}lldDescriptor=%{public, signpost.telemetry:string1,name=Descriptor}sUrl=%{public, signpost.telemetry:string2,name=Url}s enableTelemetry=YES "
+ "%{public, signpost.description:end_time}llu EnoughSpace=%{public, signpost.telemetry:number1,name=EnoughSpace}lld Urgency=%{public, signpost.telemetry:number2,name=Urgency}lldAssetType=%{public, signpost.telemetry:string1,name=AssetType}sError=%{public, signpost.telemetry:string2,name=Error}s enableTelemetry=YES "
+ "%{public, signpost.description:end_time}llu EnoughSpace=%{public, signpost.telemetry:number1,name=EnoughSpace}lld Urgency=%{public, signpost.telemetry:number2,name=Urgency}lldError=%{public, signpost.telemetry:string1,name=Error}s enableTelemetry=YES "
+ "%{public, signpost.description:end_time}llu Result=%{public, signpost.telemetry:number1,name=Result}lld Catalog=%{public, signpost.telemetry:string1,name=Catalog}sUrl=%{public, signpost.telemetry:string2,name=Url}s enableTelemetry=YES "
+ "%{public, signpost.description:end_time}llu Result=%{public, signpost.telemetry:number1,name=Result}lld Request=%{public, signpost.telemetry:number2,name=Request}lldAssetType=%{public, signpost.telemetry:string1,name=AssetType}sClient=%{public, signpost.telemetry:string2,name=Client}s enableTelemetry=YES "
+ "%{public, signpost.description:end_time}llu Result=%{public, signpost.telemetry:number1,name=Result}lld Request=%{public, signpost.telemetry:number2,name=Request}lldClient=%{public, signpost.telemetry:string1,name=Client}s enableTelemetry=YES "
+ "%{public, signpost.description:end_time}llu Urgency=%{public, signpost.telemetry:number1,name=Urgency}lld Bytes=%{public, signpost.telemetry:number2,name=Bytes}lldVolume=%{public, signpost.telemetry:string1,name=Volume}s enableTelemetry=YES "
+ "%{public}@ {%{public}@}\n#_CONNR: [OS-TRANSACTION-CONNECTOR] [BEGIN]"
+ "%{public}@ {%{public}@}\n#_CONNR: [OS-TRANSACTION-CONNECTOR] [END]"
+ "%{public}@ | {AUTO-SCHEDULER:_registerForAndStartActivity} periodic XPC activity activated with delayPeriod:%{public}@"
+ "%{public}@ | {AUTO-SCHEDULER:_scheduleSelector} asset-type blocked | assetSelector:%{public}@"
+ "%{public}@ | {AUTO-SCHEDULER:_scheduleSelector} unable to determine asset-type | assetSelector:%{public}@"
+ "%{public}@ | {AUTO-SCHEDULER:_setActivityCriteria} [%{public}@] %{public}@-jobs XPC activity started | delayPeriod:%{public}@, grace period:%llu sec%{public}@ | run from power-nap:true"
+ "%{public}@ | {AUTO-SCHEDULER:resumeFromPersisted} asset-type blocked | entryID:%{public}@ | assetSelector:%{public}@"
+ "%{public}@ | {AUTO-SCHEDULER:resumeFromPersisted} migrated set-job entry:%{public}@ | assetSelector:%{public}@ | (fromPersisted)setJob:%{public}@,intervalSecs:%ld,remainingSecs:%ld | (alteringTo)setJob:%{public}@,intervalSecs:%ld,remainingSecs:%ld"
+ "%{public}@ | {AUTO-SCHEDULER:resumeFromPersisted} removed corrupted entry:%{public}@ | assetSelector:%{public}@, assetType:%{public}@, assetSpecifier:%{public}@"
+ "%{public}@ | {AUTO-SCHEDULER:resumeFromPersisted} removed not-configured entry:%{public}@ | assetSelector:%{public}@"
+ "%{public}@ | {AUTO-SCHEDULER:resumeFromPersisted} unable to determine asset-type (ignored) | entryID:%{public}@ | assetSelector:%{public}@"
+ "3.0.3"
+ "@128@0:8@16@24@32@40@48@56@64@72@80@88@96@104B112B116@120"
+ "@348@0:8q16@24@32@40@48@56@64@?72@80@88@96@104@112@120@128@136@144@152@160@168@176@184@192@200@208@216@224@232@240@248@256@264@272@280B288B292B296@300@308@316@324@332@340"
+ "@52@0:8@16@24@32B40@44"
+ "@68@0:8@16@24@32B40@44@52@60"
+ "@84@0:8q16@24@32@40@48@56@64B72@76"
+ "AQ"
+ "AUTO-CONTROL-PROGRESS:{assetDownloadJob} Not routing progress for job since FSM not initialized | jobID:%@ | progressReport:%@"
+ "AUTO-CONTROL-PROGRESS:{autoAssetJobIssueProgress}: Not issuing auto-asset download progress indication since FSM not initialized"
+ "AUTO-CONTROL-PROGRESS:{autoSetJobIssueProgress}: Not issuing set-job download progress indication since FSM not initialized"
+ "AUTO-CONTROL:{assetBeingGarbageCollected} Skipping operation since FSM is not initialized"
+ "AUTO-CONTROL:{autoSetJobAvailableAtomicInstanceForSetDescriptor}: Returning no for atomicInstanceAvailaible since FSM is not initialized"
+ "AUTO-CONTROL:{copyCurrentDownloadedDescriptors} Skipping operation since FSM is not initialized"
+ "AUTO-CONTROL:{garbageCollectionOperationComplete} Skipping operation since FSM is not initialized"
+ "AUTO-CONTROL:{getHealthReportForSets} Skipping operation since FSM is not initialized"
+ "AUTO-CONTROL:{jobDescriptorOnFilesystemConfirmed} Skipping operation since FSM is not initialized"
+ "AUTO-CONTROL:{loadDescriptorsForJobSelector} Skipping operation since FSM is not initialized"
+ "AUTO-CONTROL:{newAtomicInstancesDownloadedForSetIdentifier} Skipping operation since FSM is not initialized"
+ "AUTO-CONTROL:{newestDownloadedForSetDescriptor} Skipping operation since FSM is not initialized"
+ "AUTO-CONTROL:{persistForJobSelector} Skipping operation since FSM is not initialized"
+ "AUTO-CONTROL:{shutdown} Skipping shutdown sequence since FSM not initialized"
+ "AUTO-SET-CONTROL: Not posting notification %@ for clientDomain %@ since FSM is not initialized"
+ "AUTO-SET-CONTROL:{%{public}@} Skipping operation since FSM is not initialized"
+ "AUTO:{assetTypeForClientDomainName} Returning nil for asset type since FSM is not initialized"
+ "After SHORT-TERM locking latest symlink is created, failed to get the destination. %@ >=> %@"
+ "After SHORT-TERM locking latest symlink is created, target is not the expected destination. Expected destination: %@. Current destination: %@"
+ "AppleConnect prompt allowed for %{public}@ (%{public}@)"
+ "AppleConnect prompt disabled for %{public}@ (%{public}@): %{public}@"
+ "Attempting to generate BAA certificate via network"
+ "Attempting to invalidate existing BAA certificate"
+ "AutoAssetScheduledOnlyForAssetTypes"
+ "ClearOSTransaction"
+ "ControlManager:ConfigDownload"
+ "Could not obtain %{public}@"
+ "DEV"
+ "DaemonAdditions"
+ "Download failed due to Data not being allowed."
+ "DownloadInfo taskDescriptor: %@ . task: %@ taskState: %@ statusCode: %lld downloadSize: %lld%@ progress: %lld / %lld isStalled: %@ numStalls: %lld numNoLongerStalls: %lld backtracks: %lld callbackCount: %lld hasExtractor: %@ extractorRequired: %@ originalUrl: %@ cacheServerUrl: %@ assetType: %@ purpose: %@ shouldRetry: %@ ifModifiedDate: %@ options: %@%@%@"
+ "DownloadManager:cancelAssetDownloadJob"
+ "DownloadManager:cancelAssetDownloadTask"
+ "DownloadManager:configAssetDownload"
+ "Existing BAA certificate invalidated"
+ "FPGA"
+ "Failed to generate certificate over network: %{public}@"
+ "Failed to get information about current symbolic link for SHORT-TERM locking latest %@"
+ "Failed to obtain BAA certificate"
+ "Failed to rename temporary symbolic link for SHORT-TERM locking to final name %@ >=> %@.  Errno: %d"
+ "FiredRetryConnOrderAttemptFirstJobActive"
+ "FiredRetryDiscTakeOSXactOrderAttempt1st"
+ "Found previously generated BAA certificate"
+ "ID:%@|lookupWithoutAssetVersion:%@|preInstalled:%@|metadata:%@|patch:%@|filesystem:%@|neverBeenLocked:%@|(secureOperation)inProgress:%@,eliminating:%@|format:%@|build:%@|[OS]min:%@,max:%@|preStaging:%@|(downloaded)user:%@,network:%ld,filesystem:%ld|(patched)base:%@,baseBytes:%ld,attempted:%@,error:%@|(staged)required:%@,prior:%@,fromOSVersion:%@,fromBuild:%@|isBlankEntry:%@"
+ "MABAACertManager not supported in NeRD"
+ "MABAACertManager not supported on %{public}@"
+ "MABAACertManager not supported on virtual machines"
+ "MADAutoControl:AdditionalSynced"
+ "MADAutoControl:AttemptNextGraft"
+ "MADAutoControl:AttemptNextPersonalize"
+ "MADAutoControl:Before1stAssetFinished"
+ "MADAutoControl:Before1stCatalogFinished"
+ "MADAutoControl:Before1stConfigFinished"
+ "MADAutoControl:CancelActivityAck"
+ "MADAutoControl:ClearInProgressSecure"
+ "MADAutoControl:CoalesceLateJobScheduled"
+ "MADAutoControl:CoalesceLateJobSetScheduled"
+ "MADAutoControl:DecideNeedGraft"
+ "MADAutoControl:DecideNeedPersonalize"
+ "MADAutoControl:DecrementTickDriven"
+ "MADAutoControl:EliminateSchedulerDone"
+ "MADAutoControl:EliminateStagerDone"
+ "MADAutoControl:EliminateStagerSetDone"
+ "MADAutoControl:FailClientTimedOut"
+ "MADAutoControl:GraftFailureDecideMore"
+ "MADAutoControl:GraftSuccessDecideMore"
+ "MADAutoControl:HandlePushNotifications"
+ "MADAutoControl:IgnorePushNotifications"
+ "MADAutoControl:InstallAssets"
+ "MADAutoControl:IssueClientReplyJobResponse"
+ "MADAutoControl:IssueClientReplySetJob"
+ "MADAutoControl:LoadPersistedResumeLocker"
+ "MADAutoControl:ObtainLookupGrant"
+ "MADAutoControl:PersonalizeFailureDecideMore"
+ "MADAutoControl:PersonalizeSuccessDecideMore"
+ "MADAutoControl:PollDecideBefore1stUnlock"
+ "MADAutoControl:PromoteStagedMigrate"
+ "MADAutoControl:ProvidePersistedForJob"
+ "MADAutoControl:QueueDownloadManager"
+ "MADAutoControl:ReleaseLookupGrant"
+ "MADAutoControl:RemoveFinishedJob"
+ "MADAutoControl:ResumeJobs"
+ "MADAutoControl:ResumeJobsBefore1st"
+ "MADAutoControl:ResumeScheduler"
+ "MADAutoControl:ResumeStager"
+ "MADAutoControl:RouteAssetFinished"
+ "MADAutoControl:RouteCatalogFinished"
+ "MADAutoControl:RouteConfigFinished"
+ "MADAutoControl:ScheduleJobs"
+ "MADAutoControl:ScheduleJobsBefore1s"
+ "MADAutoControl:ScheduleSetJobs"
+ "MADAutoControl:SchedulerJobDownloaded"
+ "MADAutoControl:SchedulerJobFoundSame"
+ "MADAutoControl:SetJobLookupResponseRcvd"
+ "MADAutoControl:StagerAlreadyDownloaded"
+ "MADAutoControl:StagerJobCancel"
+ "MADAutoControl:StagerJobDoneDetermine"
+ "MADAutoControl:StagerJobDoneDownload"
+ "MADAutoControl:StagerJobStartDetermine"
+ "MADAutoControl:StagerJobStartDownload"
+ "MADAutoControl:StagerRemoveAllNotPromoted"
+ "MADAutoControl:StartUnlockPollingTimer"
+ "MADAutoControl:SyncDecideBefore1st"
+ "MADAutoControl:SyncInFlightDownloads"
+ "MADAutoControl:SyncSkippedDecideBefore1st"
+ "MADAutoControl:Synced"
+ "MADAutoControl:SyncedResumeStager"
+ "MADAutoControl:SyncedReviewBefore1st"
+ "MADAutoControl:SyncedReviewUnlocked"
+ "MADAutoControl:autoAssetJobCoalescePostedToFinishedSetSchedulerTrigger"
+ "MADAutoControl:autoAssetJobCoalescePostedToFinishedSingletonSchedulerTrigger"
+ "MADAutoControl:autoAssetJobFinished"
+ "MADAutoControl:autoAssetStagerJobDownloadDone"
+ "MADAutoControl:autoAssetStagerSetJobDetermineDone"
+ "MADAutoControl:autoSetJobFinished"
+ "MADAutoControl:autoSetJobIssueReply"
+ "MADAutoControl:autoSetJobSchedulerNoClientDownloaded"
+ "MADAutoControl:autoSetJobSchedulerNoClientFoundSame"
+ "MADAutoControl:clientRequestsAwaitingDispatchAll"
+ "MADAutoControl:considerDownloadedWithPSUSLookupResultsForLatestToVend"
+ "MADAutoControl:handleClientAlterLockOperation"
+ "MADAutoControl:handleClientCancelActivityForSelectorRequest"
+ "MADAutoControl:handleClientCurrentStatusRequest"
+ "MADAutoControl:handleClientEliminateAllForAssetTypeRequest"
+ "MADAutoControl:handleClientEliminateAllForSelectorRequest"
+ "MADAutoControl:handleClientEliminatePromotedNeverLockedForSelectorRequest"
+ "MADAutoControl:handleClientMapLockedToExclaveRequest"
+ "MADAutoControl:handleClientPotentialJob"
+ "MADAutoControl:handleClientPotentialSetJob"
+ "MADAutoControl:handleControlClientActiveJobSummaryRequest"
+ "MADAutoControl:handleControlClientAvailableForStagingSummaryRequest"
+ "MADAutoControl:handleControlClientControlStatisticsRequest"
+ "MADAutoControl:handleControlClientForceGlobalAbandonRequest"
+ "MADAutoControl:handleControlClientForceGlobalForgetRequest"
+ "MADAutoControl:handleControlClientForceGlobalPurgeRequest"
+ "MADAutoControl:handleControlClientForceGlobalUnlockRequest"
+ "MADAutoControl:handleControlClientKnownAssetSummaryRequest"
+ "MADAutoControl:handleControlClientLockedAssetSummaryRequest"
+ "MADAutoControl:handleControlClientScheduledJobSummaryRequest"
+ "MADAutoControl:handleControlClientSimulateSetJobOperation"
+ "MADAutoControl:handleControlClientSimulatedCacheDeleteDetermineReclaimableRequest"
+ "MADAutoControl:handleControlClientSimulatedCacheDeleteReclaimSpaceRequest"
+ "MADAutoControl:handleControlClientStagedAssetSummaryRequest"
+ "MADAutoControl:handleReceivedPushNotifications"
+ "MADAutoControl:handleSetClientAlterEntriesRepresentingAtomicRequest"
+ "MADAutoControl:handleSetClientAssetSetForStagingRequest"
+ "MADAutoControl:handleSetClientCheckAtomic"
+ "MADAutoControl:handleSetClientContinueAtomicLockRequest"
+ "MADAutoControl:handleSetClientCurrentStatusRequest"
+ "MADAutoControl:handleSetClientEliminateAtomicRequest"
+ "MADAutoControl:handleSetClientEndAtomicLockRequest"
+ "MADAutoControl:handleSetClientEndAtomicLocksForClientRequest"
+ "MADAutoControl:handleSetClientFormSubAtomicRequest"
+ "MADAutoControl:handleSetClientLockAtomic"
+ "MADAutoControl:handleSetClientMapLockedAtomicEntryRequest"
+ "MADAutoControl:handleSetClientNeedForAtomicRequest"
+ "MADAutoControl:handleSetControlClientAssetSetsOverviewRequest"
+ "MADAutoControl:handleSetControlClientInstanceInfoRequest"
+ "MADAutoControl:handleStagingClientCancelOperation"
+ "MADAutoControl:handleStagingClientDetermineAllAvailableRequest"
+ "MADAutoControl:handleStagingClientDetermineGroupsAvailableForUpdateRequest"
+ "MADAutoControl:handleStagingClientDownloadAllRequest"
+ "MADAutoControl:handleStagingClientDownloadGroupsRequest"
+ "MADAutoControl:handleStagingClientEraseAllRequest"
+ "MADAutoControl:handleStagingClientPurgeAllRequest"
+ "MADAutoControl:lockAutoAssetReplyJobResponse"
+ "MADAutoControl:lockerResumed"
+ "MADAutoControl:removeShortTermLockingOfSetDescriptor"
+ "MADAutoControl:schedulerEliminatedSelector"
+ "MADAutoControl:schedulerEliminatedSetDomainName"
+ "MADAutoControl:schedulerReferencesDescriptor"
+ "MADAutoControl:schedulerResumed"
+ "MADAutoControl:schedulerTickOccurred"
+ "MADAutoControl:schedulerTriggeredNoActivity"
+ "MADAutoControl:schedulerTriggeredSelectors"
+ "MADAutoControl:schedulerTriggeredSets"
+ "MADAutoControl:secureCheckUngraft"
+ "MADAutoControl:secureCheckUngraftAll"
+ "MADAutoControl:secureClearInsecureLatestAtomicInstances"
+ "MADAutoControl:secureForceUngraft"
+ "MADAutoControl:secureOperationsFinished"
+ "MADAutoControl:shortTermLockSetDescriptor"
+ "MADAutoControl:stagerCancelCurrentJob"
+ "MADAutoControl:stagerEliminatedSelector"
+ "MADAutoControl:stagerEliminatedSetConfiguration"
+ "MADAutoControl:stagerPurgeStagedContent"
+ "MADAutoControl:stagerRequestAlreadyDownloadedDescriptors"
+ "MADAutoControl:stagerResumed"
+ "MADAutoControl:stagerStartJobDownloadForStaging"
+ "MADAutoControl:stagerStartSetJobDetermineIfAvailable"
+ "MADAutoControl:startupActivationCompleted"
+ "MADAutoControl:timerStartForRequest"
+ "MADJob:AddAtomicAlterDecideFilesystem"
+ "MADJob:AddAtomicCheckDecideFilesystem"
+ "MADJob:AddAtomicContinueDecideFilesystem"
+ "MADJob:AddAtomicEndDecideFilesystem"
+ "MADJob:AddAtomicLockDecideFilesystem"
+ "MADJob:AddAtomicNeedDecideFilesystem"
+ "MADJob:AddTaskCheckDecideFilesystem"
+ "MADJob:AddTaskDecideFilesystem"
+ "MADJob:AddTaskDetermineDecideFilesystem"
+ "MADJob:AddTaskInterestDecideFilesystem"
+ "MADJob:AddTaskLockDecideFilesystem"
+ "MADJob:AddTaskScheduler"
+ "MADJob:AddTaskSchedulerDecideFilesystem"
+ "MADJob:AdoptRegister"
+ "MADJob:BoostAndRequestLookupGrant"
+ "MADJob:BoostConfig"
+ "MADJob:CancelAssetDownload"
+ "MADJob:CheckSimulateEndStatusRequest"
+ "MADJob:DecideDownloadOrPostpone"
+ "MADJob:DecideStartupDownloading"
+ "MADJob:DoneReportingProgress"
+ "MADJob:DownloadCatalog"
+ "MADJob:DownloadNewestFull"
+ "MADJob:DownloadNewestPatch"
+ "MADJob:DownloadSuccessDecideMore"
+ "MADJob:DownloadSuccessDecidePersonalize"
+ "MADJob:FailRequestCanceling"
+ "MADJob:FailedPatchDecideTryFull"
+ "MADJob:FinishedCoalescedClientReply"
+ "MADJob:JobEndedSchedule"
+ "MADJob:JobFailedAwaiting"
+ "MADJob:JobFailedCanceled"
+ "MADJob:JobFailedSchedule"
+ "MADJob:JobNoNewerSchedule"
+ "MADJob:JobPostponedSchedule"
+ "MADJob:JobRevokedSchedule"
+ "MADJob:JobSuccessAlreadyDownloaded"
+ "MADJob:JobSuccessDownloadedAwaiting"
+ "MADJob:JobSuccessDownloadedSchedule"
+ "MADJob:JobSuccessFoundPromoted"
+ "MADJob:JobSuccessFoundSameSchedule"
+ "MADJob:JobSuccessPatchedAwaiting"
+ "MADJob:JobSuccessPatchedSchedule"
+ "MADJob:JobSuccessPersonalized"
+ "MADJob:LookupFailedContinue"
+ "MADJob:LookupNoNewerContinue"
+ "MADJob:LookupRevokedContinue"
+ "MADJob:LookupSuccessContinue"
+ "MADJob:MergeAddLock"
+ "MADJob:MergeAddLockDecideBoost"
+ "MADJob:MergeAtomicAddLock"
+ "MADJob:MergeAtomicAlterDecideLookup"
+ "MADJob:MergeAtomicAlterDecideLookupBoost"
+ "MADJob:MergeAtomicAlterNeeds"
+ "MADJob:MergeAtomicCntnuDecideLookupBoost"
+ "MADJob:MergeAtomicContinueLock"
+ "MADJob:MergeAtomicEndLockDecideInterest"
+ "MADJob:MergeAtomicLockDecideLookupBoost"
+ "MADJob:MergeAtomicNeeds"
+ "MADJob:MergeAtomicNeedsDecideLookup"
+ "MADJob:MergeAtomicNeedsDecideLookupBoost"
+ "MADJob:MergeContinueLock"
+ "MADJob:MergeContinueLockDecideBoost"
+ "MADJob:MergeNeeds"
+ "MADJob:MergeNeedsDecideBoost"
+ "MADJob:MergeNeedsDecideLookup"
+ "MADJob:MergeNeedsDecideLookupBoost"
+ "MADJob:MergeRemoveLock"
+ "MADJob:MergeRemoveLockDecideInterest"
+ "MADJob:NowDeadClear"
+ "MADJob:PersistedDecideDownload"
+ "MADJob:PersonalizeFailureDecideMore"
+ "MADJob:PersonalizeHealFailureDecideMore"
+ "MADJob:PersonalizeHealSuccessDecideMore"
+ "MADJob:PersonalizeSuccessDecideMore"
+ "MADJob:RecordSimulateOperation"
+ "MADJob:ReleaseGrantCanceling"
+ "MADJob:ReleaseGrantJobFailedCanceled"
+ "MADJob:ReleaseGrantJobFailedSchedule"
+ "MADJob:RemoveClient"
+ "MADJob:RemoveClientDecideInterest"
+ "MADJob:ReportCatalogDecideFound"
+ "MADJob:RequestLookupGrant"
+ "MADJob:RequestSpecificPersisted"
+ "MADJob:RerouteSchedulerTrigger"
+ "MADJob:SecureBundlePersonalize"
+ "MADJob:SetCalculateDownloadSpace"
+ "MADJob:SetDecideDownload"
+ "MADJob:SetDoneDetermine"
+ "MADJob:SetDownloadNewestFull"
+ "MADJob:SetDownloadNext"
+ "MADJob:SetDownloadSameFull"
+ "MADJob:SetJobEndedSchedule"
+ "MADJob:SetJobFailedAwaiting"
+ "MADJob:SetJobFailedSchedule"
+ "MADJob:SetJobHealPersonalizeNext"
+ "MADJob:SetJobLookupRevokedContinue"
+ "MADJob:SetJobNoNewerSchedule"
+ "MADJob:SetJobNoneSchedule"
+ "MADJob:SetJobSuccessAwaiting"
+ "MADJob:SetJobSuccessFoundPromoted"
+ "MADJob:SetJobSuccessFoundSameSchedule"
+ "MADJob:SetJobSuccessSchedule"
+ "MADJob:SetJobTryPersonalizeHeal"
+ "MADJob:SetLookupNoNewerContinue"
+ "MADJob:SetLookupNoneContinue"
+ "MADJob:SetLookupSuccessContinue"
+ "MADJob:SimulatePostponedCalculateSpace"
+ "MADJob:SimulateSuspendCatalogLookupIssue"
+ "MADJob:StagerDetermineDecideFilesystem"
+ "MADJob:StagerDownloadDecideFilesystem"
+ "MADJob:handleClientRequest"
+ "MADJob:startHandlingClientRequest"
+ "MADScheduler:controlEliminateSelector"
+ "MADScheduler:controlEliminateSetDomainName"
+ "MADScheduler:jobFinishedForSelector"
+ "MADScheduler:jobFinishedForSetDomainName"
+ "MADScheduler:resumeFromPersisted"
+ "MADScheduler:schedulePushNotifications"
+ "MADScheduler:scheduleSelector"
+ "MADScheduler:scheduleSetDomainName"
+ "MADScheduler:triggerWithRetrySetDomainName"
+ "MADSecure:commitPrePersonalized"
+ "MADSecure:commitPrePersonalizedSync"
+ "MADSecure:depersonalizeIfSecure"
+ "MADSecure:graftDownloaded"
+ "MADSecure:graftDownloadedSync"
+ "MADSecure:graftSecureAsset"
+ "MADSecure:isPersonalizationRequired"
+ "MADSecure:latestDownloadedAtomicInstanceEntries"
+ "MADSecure:mapToExclave"
+ "MADSecure:personalizeDownloaded"
+ "MADSecure:personalizeGraftDownloaded"
+ "MADSecure:personalizeSetDownloaded"
+ "MADSecure:ungraft"
+ "MADSecure:ungraftAll"
+ "MADSecure:ungraftIfNotAccessible"
+ "MADStager:AddToAvailableDecideAnyAvailable"
+ "MADStager:AddToAvailableDecideMoreCandidates"
+ "MADStager:AddToAvailableDecideRequiredAvailable"
+ "MADStager:AddToStaged"
+ "MADStager:AddToStagedDecideMoreAvailable"
+ "MADStager:CancelActiveJob"
+ "MADStager:ClientAcceptAllDetermine"
+ "MADStager:ClientAcceptCancelActiveJob"
+ "MADStager:ClientAcceptEraseActiveJob"
+ "MADStager:ClientAcceptNextAvailableBeginDownload"
+ "MADStager:ClientAcceptRemoveAllReplyErased"
+ "MADStager:ClientAcceptRemoveAllReplyPurged"
+ "MADStager:ClientCancelDesireForCompletion"
+ "MADStager:ClientCheckGroupsDecideAlreadyDetermined"
+ "MADStager:ClientCheckGroupsReplyAlreadyDetermined"
+ "MADStager:ClientCheckLatchGroupsDetermine"
+ "MADStager:ClientContinueRestartingMaxDetermining"
+ "MADStager:ClientContinueUsingLatestRequest"
+ "MADStager:ClientDecideGroupTargetAvailable"
+ "MADStager:ClientDecideGroupTargetAvailablePurge"
+ "MADStager:ClientEraseDecideStagingClient"
+ "MADStager:ClientFailAlreadyDetermining"
+ "MADStager:ClientFailByGroupAlreadyDownloading"
+ "MADStager:ClientFailGroupDetermining"
+ "MADStager:ClientFailNoGroupsStaged"
+ "MADStager:ClientFailWrongMode"
+ "MADStager:ClientHaveStagedContent"
+ "MADStager:ClientInvalidStagingPhase"
+ "MADStager:ClientNewerReplyEmptyDetermine"
+ "MADStager:ClientNewerReplyEmptyDownload"
+ "MADStager:ClientNewerReplySameOrEmptyDetermine"
+ "MADStager:ClientNewerReplySameOrEmptyDownload"
+ "MADStager:ClientNothingStaged"
+ "MADStager:ClientPurgeDecideStagingClient"
+ "MADStager:ClientRequestAlreadyDownloaded"
+ "MADStager:ControlUnstagedDecideCancelJob"
+ "MADStager:ControlUnstagedDecideRemoveAll"
+ "MADStager:DecideEmptyHaveAvailable"
+ "MADStager:DecideHaveAvailableOtherTargets"
+ "MADStager:DecideHaveRequiredCandidates"
+ "MADStager:DecideMoreAvailable"
+ "MADStager:DecideMoreCandidates"
+ "MADStager:DecideMoreOptionalAvailable"
+ "MADStager:DecideMoreRequiredAvailable"
+ "MADStager:DecideRequiredErrorBlocksOTA"
+ "MADStager:DecideTimerDeterminingValid"
+ "MADStager:DoneAvailableDecideAnyStaged"
+ "MADStager:DoneCandidatesDecideAnyAvailable"
+ "MADStager:DoneCandidatesRequiredDecideOptional"
+ "MADStager:EliminateAvailableDecideEmpty"
+ "MADStager:EliminateCancelActiveJob"
+ "MADStager:EliminateDecideMatch"
+ "MADStager:EliminateDeterminingDecideMatch"
+ "MADStager:EliminateDone"
+ "MADStager:EliminateDoneDecideMoreDownload"
+ "MADStager:EliminateDoneStagedDecideEmpty"
+ "MADStager:FailRequiredDetermineBlocksOTA"
+ "MADStager:FormCandidatesDecideDetermine"
+ "MADStager:IgnoreFailureDecideRequiredAvailable"
+ "MADStager:LoadDecideNewOSPromote"
+ "MADStager:LoadPersistedDecideResume"
+ "MADStager:NextAwaitingBeginDownload"
+ "MADStager:NextCandidateBeginDetermine"
+ "MADStager:RememberEliminateDone"
+ "MADStager:RememberSetEliminateDone"
+ "MADStager:RemoveAllReplyErased"
+ "MADStager:RemoveAllReplyPurged"
+ "MADStager:ReplyFailRequiredDownload"
+ "MADStager:ReplyHaveAvailable"
+ "MADStager:ReplyHaveStaged"
+ "MADStager:ReplyNoCandidates"
+ "MADStager:ReplyNoCandidatesHaveOtherTarget"
+ "MADStager:ReplyNoCandidatesPurgeAll"
+ "MADStager:ReplyNothingStaged"
+ "MADStager:ReplyNothingStagedPurgeAll"
+ "MADStager:ReplyTargetNotAvailable"
+ "MADStager:ReportStagingProgressToClient"
+ "MADStager:RequestAlreadyDownloaded"
+ "MADStager:SetEliminateAvailableDecideEmpty"
+ "MADStager:SetEliminateDecideMatch"
+ "MADStager:SetEliminateDeterminingDecideMatch"
+ "MADStager:SetEliminateDone"
+ "MADStager:SetEliminateDoneStagedDecideEmpty"
+ "MADStager:resumeFromPersisted"
+ "MONITOR_WITH_MARKERS|monitor:%ld|noRetry:%ld|requiringRetry:%ld|osTrans:%@"
+ "MobileAssetServer:MobileAssetServer"
+ "Not recording event for: %{public}@"
+ "OrderAttemptTakeOSXactFirstJobActive"
+ "SCHEDULER_NO_ACTIVITY|osTrans:%@"
+ "SCHEDULER|count:%ld|osTrans:%@"
+ "SCHEDULER|count:%ld|selectors:%@|osTrans:%@"
+ "SET-SCHEDULER|count:%ld|osTrans:%@"
+ "SET-SCHEDULER|count:%ld|triggeredSets:%@|osTrans:%@"
+ "STAGED_LOOKUP_NEWOS_PROMOTE"
+ "StartBackoffAndRetryWaitTimersClearOSXact"
+ "Starting built-in MobileAsset brain built Jun 18 2025 00:13:06"
+ "Starting downloaded MobileAsset brain (version: %@) built Jun 18 2025 00:13:06"
+ "StopBackoffTakeOSXactOrderAttempt1st"
+ "StopBackoffTimerTakeOSTransaction"
+ "Successfully generated certificate over network: %{public}@"
+ "Successfully read current %{public}@"
+ "T@\"MAPerfResults\",&,N,V_startupPerfResults"
+ "T@\"NSMutableDictionary\",&,N,V_nwActivityObjectsByJobUUID"
+ "T@\"NSObject<OS_os_transaction>\",&,N,V_activeAttemptOSTransaction"
+ "T@\"NSObject<OS_os_transaction>\",&,N,V_eventOSTransaction"
+ "T@\"NSObject<OS_os_transaction>\",&,N,V_lifetimeOSTransaction"
+ "T@\"NSString\",&,N,V_preferenceScheduledOnlyForAssetTypes"
+ "TB,V_extractorRequired"
+ "TQ,N,V_startupSignpost"
+ "TakeOSTransaction"
+ "Unable to create symbolic link for SHORT-TERM locking latest | %@ >=> %@"
+ "Unable to create temporary symbolic link for SHORT-TERM locking latest %@"
+ "[AUTO-SHORT-TERM][SYMLINK]{%{public}@:_shortTermCreateSymbolicLink} No SHORT-TERM locking latest symlink exists yet. Creating"
+ "[AUTO-SHORT-TERM][SYMLINK]{%{public}@:_shortTermCreateSymbolicLink} latest symlink already pointed to requested target file: %{public}@.  No change needed"
+ "[AUTO-SHORT-TERM][SYMLINK]{%{public}@:_shortTermCreateSymbolicLink} latest symlink currently pointed to target: %{public}@, but it is not the requested target: %{public}@.  Updating symlink."
+ "[KnoxServerAuth] Failing without Authorization header"
+ "[OS-TRANSACTION-JOB] [BEGIN] %{public}@"
+ "[OS-TRANSACTION-JOB] [END]"
+ "[TaskFinished]: Download failed however we are going to retry at original url: %{public}@"
+ "[TaskFinished]: Download failed. Not attempting retry with original URL ExtractorRequired: %@ ExtractorPresent: %@"
+ "[TaskFinished]: Task finished without a task descriptor, syncing with nsurlsession"
+ "[TaskFinished]: We have no info about this task, cannot reply: %{public}@  The downloads in flight are: %{public}@"
+ "[monitor:%ld,requiringRetry:%ld|triggered(noRetry:%ld,retryRequired:%ld)|osTrans:%@|backoffLevel:%ld|observers:%ld|attempt(activeMarker:%@,remaining:%ld)]"
+ "[overall]instance:%@,selector:%@,UUID:%@,tasks:%lu,requests:%ld,table:%@,FSM:%@,sched:%@,NWFail:%@|beingCancled:%@|[earlier]sched:%@,NWFail:%@|bonded:%@|[active]instance:%@,desire:%@(awaitDownload:%@,checkAwait:%@),found:%@,end:%@,listen:%@,jobInfo:%@|[aggregated]policy:%@,clientRequested:%@|firstClientName:%@,triggeringLayer:%@|onFilesystemByVersion:%ld|[check]Base:%@,UUID:%@,lookupGrant:%@,rampFG:%@,rampLatch:%@,options:%@|[asset]base:%@,patch:%@,full:%@,newer:%@,downloading:%@,scheduler:%@,lookupRsp:%@(forConfig:%@),user:%@,boosting:%@,checking:%@,determining:%@,locking:%@,patched:%@|[installed]:version:%@,build:%@|[status]current:%@,progress:%@,lastPatch:%@|[results]selector:%@,instance:%@,found:%@,end:%@,listen:%@,[set]aggregatedPolicy:%@,descriptor:%@,next:%ld,found:%@"
+ "_AllowUserInteraction"
+ "_activeAttemptOSTransaction"
+ "_cachedCertArray"
+ "_cachedKey"
+ "_cachedTime"
+ "_checkIsSupported"
+ "_chooseOrderForNextAttemptAndStartFirstJob:beginningOSTransaction:"
+ "_copyCachedCerts:"
+ "_eventOSTransaction"
+ "_extractorRequired"
+ "_lifetimeOSTransaction"
+ "_locateLockByPersistentEntryID:"
+ "_nwActivityObjectsByJobUUID"
+ "_preferenceScheduledOnlyForAssetTypes"
+ "_requestTime"
+ "_responseTime"
+ "_startupPerfResults"
+ "_startupSignpost"
+ "action_ClearOSTransaction:error:"
+ "action_FiredRetryConnOrderAttemptFirstJobActive:error:"
+ "action_FiredRetryDiscTakeOSXactOrderAttempt1st:error:"
+ "action_OrderAttemptTakeOSXactFirstJobActive:error:"
+ "action_StartBackoffAndRetryWaitTimersClearOSXact:error:"
+ "action_StopBackoffTakeOSXactOrderAttempt1st:error:"
+ "action_StopBackoffTimerTakeOSTransaction:error:"
+ "action_TakeOSTransaction:error:"
+ "activeAttemptOSTransaction"
+ "any"
+ "autoJobAssetSetIDsForJob:mostRecentlyReceived:latestToVend:"
+ "com.apple.MobileAsset.AutoAssetConnector.TriggeredMarkersAttempt"
+ "com.apple.MobileAsset.AutoAssetConnector.alteredMonitoringMarkers"
+ "com.apple.MobileAsset.AutoControlManager.Job.ClientRequestSet"
+ "com.apple.MobileAsset.AutoControlManager.Job.ClientRequestSingleton"
+ "com.apple.MobileAsset.AutoControlManager.Job.PreviouslyInFlight"
+ "com.apple.MobileAsset.AutoControlManager.Job.SchedulerSetJob"
+ "com.apple.MobileAsset.AutoControlManager.Job.SchedulerSingleton"
+ "com.apple.MobileAsset.AutoControlManager.Job.StagerDetermine"
+ "com.apple.MobileAsset.AutoControlManager.Job.StagerDownload"
+ "com.apple.MobileAsset.AutoControlManager.schedulerTickOccurred"
+ "com.apple.MobileAsset.AutoControlManager.schedulerTriggeredNoActivity"
+ "com.apple.MobileAsset.AutoControlManager.schedulerTriggeredSelectors"
+ "com.apple.MobileAsset.AutoControlManager.schedulerTriggeredSets"
+ "destinationOfSymbolicLinkAtPath:error:"
+ "discretionary download"
+ "eventOSTransaction"
+ "extractorRequired"
+ "initForDescriptor:withLifetimeOSTransaction:baseForPatchDescriptor:withAutoAssetUUID:"
+ "initForInstance:orForSelector:orForDescriptor:orForSetInstance:withLifetimeOSTransaction:withSetDesire:withSchedulerSetPolicy:withStagerSetPolicy:usingSetConfiguration:usingSetDescriptor:withBaseForPatchDescriptor:withAutoAssetUUID:downloadingUserInitiated:asStagerJob:usingCachedAutoAssetCatalog:"
+ "initForInstance:withLifetimeOSTransaction:withAutoAssetUUID:downloadingUserInitiated:"
+ "initForModule:ofModuleVersion:usingDispatchQueue:loggingByName:withVersionMigrator:"
+ "initForSelector:withLifetimeOSTransaction:withAutoAssetUUID:"
+ "initForSelector:withLifetimeOSTransaction:withAutoAssetUUID:asStagerJob:withStagerSetPolicy:usingCachedAutoAssetCatalog:usingBaseForPatching:"
+ "initForSetConfiguration:withLifetimeOSTransaction:withAutoAssetUUID:asStagerJob:withStagerSetPolicy:"
+ "initForSetInstance:withLifetimeOSTransaction:withSchedulerSetPolicy:usingSetConfiguration:usingSetDescriptor:withAutoAssetUUID:"
+ "initForSetInstance:withLifetimeOSTransaction:withSetDesire:usingSetConfiguration:usingSetDescriptor:withAutoAssetUUID:"
+ "initForTriggeredNoActivity:"
+ "initForTriggeredSelectors:withEventOSTransaction:"
+ "initForTriggeredSets:withEventOSTransaction:"
+ "initWithMonitorMarkers:withMarkersNoRetry:withMarkersRequiringRetry:withEventOSTransaction:"
+ "initWithParamType:withSafeSummary:withEventOSTransaction:withScheduledJobs:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withDownloadOptions:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withSetDescriptor:withAutoAssetDescriptors:withSetPolicy:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withStagedToDownloaded:withStagedLookupResults:withDownloadingDescriptor:withBaseForPatchDescriptor:withBaseForStagingDescriptors:withSchedulerInvolved:withPotentialNetworkFailure:withRequiringLoadPriorToUse:withClientDomainName:withAssetSetIdentifier:withSetConfiguration:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:"
+ "initWithParamType:withSafeSummary:withMonitorMarkers:withMarkersNoRetry:withMarkersRequiringRetry:withFinishedMarker:withEventOSTransaction:withPotentialNetworkFailure:withObservedNetworkPath:"
+ "invalidateExistingCertsAndWait"
+ "isAtomicInstancePartOfPSUS:"
+ "isFullAssetSelector"
+ "issueAndWaitForCerts:"
+ "key retrieval"
+ "lifetimeOSTransaction"
+ "locateLockByFullAssetSelector:"
+ "locateLocksBySelector"
+ "locateLocksBySelector:"
+ "locateLocksBySelectorPrefix"
+ "non-ui asset"
+ "non-ui download"
+ "notifyCompletionCallbacksForSetJobKey:"
+ "nwActivityObjectsByJobUUID"
+ "osTransactionBegin:"
+ "osTransactionEnd:"
+ "osTransactionNameAutoJob:forJobUUID:"
+ "osTransactionNameClientRequestedSetJob:"
+ "osTransactionNameClientRequestedSingletonJob:"
+ "osTransactionNamePreviouslyInFlightJob:"
+ "osTransactionNameScheduledSetJob:"
+ "osTransactionNameScheduledSingletonJob:"
+ "osTransactionNameStagerDetermineJob:"
+ "osTransactionNameStagerDownloadJob:"
+ "policy:%@|server:%@|table:%@|FSM:%@|(persisted)active:%@,known:%@,configs:%@,AI:%@|(sets)active:%@,desc:%@,targets:%@,lookups:%@,map:%@"
+ "preferenceScheduledOnlyForAssetTypes"
+ "r*24@0:8@16"
+ "r*32@0:8@16@24"
+ "root-snapshot-name"
+ "server auth"
+ "setActiveAttemptOSTransaction:"
+ "setEventOSTransaction:"
+ "setExtractorRequired:"
+ "setLifetimeOSTransaction:"
+ "setNwActivityObjectsByJobUUID:"
+ "setPreferenceScheduledOnlyForAssetTypes:"
+ "setStartupPerfResults:"
+ "setStartupSignpost:"
+ "shouldDisableUIForUsage:assetAttributes:downloadOptions:"
+ "startupPerfResults"
+ "startupSignpost"
+ "tmpSymlink"
+ "v16@?0B8B12"
+ "v40@0:8@16^@24^@32"
+ "{%@} OS-transaction already being held"
+ "{%@} not holding any OS-transaction"
+ "{%@} unable to create OS-transaction"
+ "{AUTO-LOCKER:%{public}@:_persistAssetLock} | continued lock count for selector not represented in lockCountsBySelector | selector:%{public}@"
+ "{AUTO-LOCKER:locateLockByFullAssetSelector} fullAssetSelector's isFullAssetSelector check failed | fullAssetSelector:%{public}@"
+ "{AUTO-LOCKER:lockedSelectorsForEliminate} | failed alloc of matchedLockedSelectors"
+ "{AUTO-LOCKER:newCurrentLockUsageForSelector} allowed but unexpected naming collision on assetSpecifier | assetSelector:%{public}@ foundFullAssetSelector:%{public}@ prefix:%{public}@"
+ "{AUTO-LOCKER:newCurrentLockUsageForSelector} allowed but unexpected naming collision on assetType | assetSelector:%{public}@ foundFullAssetSelector:%{public}@ prefix:%{public}@"
+ "{AUTO-LOCKER:newCurrentLockUsageForSelector} allowed but unexpected naming collision on assetVersion | assetSelector:%{public}@ foundFullAssetSelector:%{public}@ prefix:%{public}@"
+ "{AUTO-LOCKER:newCurrentLockUsageForSelector} invarient failed, assetType must be non-nil"
+ "{AUTO-LOCKER:newCurrentLockUsageForSelector} lock missing fullAssetSelector | persistedEntryID:%{public}@"
+ "{AUTO-LOCKER:newCurrentLockUsageForSelector} unable to find lock for known persistedEntryID | persistedEntryID:%{public}@"
+ "{AUTO-LOCKER:newCurrentLockUsageForSelector} | bad alloc/init for locatedLocksForSelector"
+ "{AUTO-LOCKER:newCurrentLockUsageForSelector} | bad alloc/init for persistedEntryIDs"
+ "{AUTO-LOCKER:newCurrentLockUsageForSelector} | bad alloc/init for persistedEntryIDsWithPrefix"
+ "{AUTO-LOCKER:newCurrentLockUsageForSelector} | bad alloc/init for prefix"
+ "{AUTO-LOCKER:newCurrentLockUsageForSelector} | missing assetSelector.assetType"
+ "{_handleResumeFromSoftwareUpdateRequest} clearing outstanding completionCallbacksBySetJobKey."
+ "{_handleResumeFromSoftwareUpdateRequest} clearing outstanding evictedCallbacksByAtomicInstanceUUID."
+ "{handleSuspendResumeForSoftwareUpdateDaemonStartup} infeasible path. If callbacks are registered we must be .Suspending"
+ "{handleSuspendResumeForSoftwareUpdateDaemonStartup} notifyEvictedCallbacksForSetDescriptor invoked for locked set descriptor | setDescriptor:%{public}@"
+ "{notifyCompletionCallbacksForSetJobKey} basic invariant violated"
+ "{notifyCompletionCallbacksForSetJobKey} infeasible path. If callbacks are registered we must be .Suspending"
- "\n#_%{public}@:%{public}@ (%ld of %ld) [%{public}@] | (%{public}@) intervalSecs:%{public}@ | remainingSecs:%{public}@ | setPolicy:%@"
- "%@ %@ stashed certificate %@"
- "%@ certificate over network %@"
- "%@:newSetDescriptorIfOtherSatisfying"
- "%@|statusBySelector:%ld(set:%ld)|jobsByInstance:%ld(setJobsByID:%ld)(setJobsCancelingByID:%ld)|jobsByUUID:%ld|stagerJob:%@|DMSync:%@|lookupGrants:%ld|setConfigs:%ld|atomicInstances:%ld|downloaded:%ld|scheduledSelectors:%ld|timedOps:%ld|clientRequests:%ld|awaitingSync:%ld|awaitingUnlock:%ld|awaitingResume:%ld"
- "%{public, signpost.description:begin_time}llu str1=%{public, signpost.telemetry:string1,name=str1}s  enableTelemetry=YES "
- "%{public}@ | {AUTO-SCHEDULER:_registerForAndStartActivity} after re-register attempt still at different than desired delayPeriod:%{public}@"
- "%{public}@ | {AUTO-SCHEDULER:_registerForAndStartActivity} attempt to re-register with desired delayPeriod:%{public}@"
- "%{public}@ | {AUTO-SCHEDULER:_registerForAndStartActivity} periodic XPC activity DISABLED with previous delayPeriod:%{public}@"
- "%{public}@ | {AUTO-SCHEDULER:_registerForAndStartActivity} periodic XPC activity re-activated with delayPeriod:%{public}@"
- "%{public}@ | {AUTO-SCHEDULER:_setActivityCriteria} [%{public}@] %@-jobs XPC activity started | delayPeriod:%{public}@, grace period:%llu sec%@ | run from power-nap:true"
- "%{public}@ | {AUTO-SCHEDULER:resumeFromPersisted} migrated set-job entry:%{public}@ | assetSelector:%@ | (fromPersisted)setJob:%{public}@,intervalSecs:%ld,remainingSecs:%ld | (alteringTo)setJob:%{public}@,intervalSecs:%ld,remainingSecs:%ld"
- "%{public}@ | {AUTO-SCHEDULER:resumeFromPersisted} removed corrupted entry:%{public}@ | assetSelector:%@, assetType:%@, assetSpecifier:%@"
- "%{public}@ | {AUTO-SCHEDULER:resumeFromPersisted} removed not-configured entry:%{public}@ | assetSelector:%@"
- "%{public}@ | {_anyCurrentLocksForEliminate} eliminate-selector for asset-type + asset-specifier + asset-version associated with current lock | eliminateSelector:%{public}@"
- "%{public}@ | {_anyCurrentLocksForEliminate} eliminate-selector for asset-type + asset-specifier associated with current lock | eliminateSelector:%{public}@"
- "%{public}@ | {_anyCurrentLocksForEliminate} eliminate-selector for asset-type associated with current lock | eliminateSelector:%{public}@"
- "%{public}@ | {lockedSelectorsForEliminate} assetLock on locksBySelector with nil fullAssetSelector | assetLock:%{public}@ | eliminateSelector:%{public}@"
- "%{public}@ | {lockedSelectorsForEliminate} eliminate-selector for asset-type + asset-specifier + asset-version associated with current lock | eliminateSelector:%{public}@"
- "%{public}@ | {lockedSelectorsForEliminate} eliminate-selector for asset-type + asset-specifier associated with current lock | eliminateSelector:%{public}@"
- "%{public}@ | {lockedSelectorsForEliminate} eliminate-selector for asset-type associated with current lock | eliminateSelector:%{public}@"
- "3.0.2"
- "?@"
- "@\"SUCoreLog\""
- "@120@0:8@16@24@32@40@48@56@64@72@80@88@96B104B108@112"
- "@340@0:8q16@24@32@40@48@56@?64@72@80@88@96@104@112@120@128@136@144@152@160@168@176@184@192@200@208@216@224@232@240@248@256@264@272B280B284B288@292@300@308@316@324@332"
- "@60@0:8@16@24B32@36@44@52"
- "@64@0:8@16@24@32@40@48@?56"
- "@76@0:8q16@24@32@40@48@56B64@68"
- "Attempting to generate certificate via network"
- "Checking for token with silent interactivity level"
- "Clearing out generated key"
- "DeviceIdentity returned a unexpected number of certs. Skipping returning certs to user"
- "Downlaod failed due to Data not being allowed."
- "Download failed and there is no extractor to retry so failing"
- "Download failed however we are going to retry at original url: %{public}@"
- "DownloadInfo taskDescriptor: %@ . task: %@ taskState: %@ statusCode: %lld downloadSize: %lld%@ progress: %lld / %lld isStalled: %@ numStalls: %lld numNoLongerStalls: %lld backtracks: %lld callbackCount: %lld hasExtractor: %@ originalUrl: %@ cacheServerUrl: %@ assetType: %@ purpose: %@ shouldRetry: %@ ifModifiedDate: %@ options: %@%@%@"
- "FROM_OTHER_DESCRIPTOR"
- "Failed to %@ certificates: %@"
- "Failed to allocate keymanager. Unable to obtain DAW token"
- "Failed to create base64 encoded certificate string for one of the certs in the chain"
- "Failed to generate"
- "Failed to obtain BAA certificate chain"
- "Failed to obtain options to pass to deviceIdentity. Bailing"
- "FiredRetryWaitOrderAttemptFirstJobActive"
- "Found previoulsy generated certs. Returning those"
- "Got back a unexpected number of certificates :%lu"
- "ID:%@|lookupWithoutAssetVersion:%@|preInstalled:%@|patch:%@|filesystem:%@|neverBeenLocked:%@|(secureOperation)inProgress:%@,eliminating:%@|format:%@|build:%@|[OS]min:%@,max:%@|preStaging:%@|(downloaded)user:%@,network:%ld,filesystem:%ld|(patched)base:%@,baseBytes:%ld,attempted:%@,error:%@|(staged)required:%@,prior:%@,fromOSVersion:%@,fromBuild:%@|isBlankEntry:%@"
- "MA-BAA-CERT-MANAGER"
- "MA-KEY-MANAGER"
- "MAB-RESTART"
- "MAKeyManagerDownloadSessionDelegate:%@"
- "MONITOR_WITH_MARKERS|monitor:%ld|noRetry:%ld|requiringRetry:%ld"
- "MobileAssetServer"
- "No error in callback..Num certificates is %lu"
- "Not recording event for : %{public}@"
- "OrderAttemptFirstJobActive"
- "Previously generated certs invalidated successfully"
- "Read stashed cert callback running"
- "SCHEDULER_NO_ACTIVITY"
- "SCHEDULER|count:%ld"
- "SCHEDULER|count:%ld|selectors:%@"
- "SET-SCHEDULER|count:%ld"
- "SET-SCHEDULER|count:%ld|triggeredSets:%@"
- "Saving reference key"
- "StartBackoffAndRetryWaitTimers"
- "Starting built-in MobileAsset brain built May 30 2025 21:57:33"
- "Starting downloaded MobileAsset brain (version: %@) built May 30 2025 21:57:33"
- "StopBackoffOrderAttemptFirstJobActive"
- "Successfully generated"
- "Successfully read current boot-manifest-hash"
- "T@\"MAPerfResults\",&,N,V_perfResultsCPI"
- "T@\"NSCache\",&,N,V_stagedAssetToSetDescriptorCache"
- "T@\"NSCache\",&,N,V_stagedIsNewOSPromotedCache"
- "T@\"NSMutableDictionary\",&,N,V_nwActivityObjects"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_nwQueue"
- "T@\"SUCoreLog\",R,&,N,V_logger"
- "TQ,N,V_startupSignpostCPI"
- "Task finished without a task descriptor, syncing with nsurlsession"
- "Timed out waiting for stashed certs to be returned"
- "Unable to retrieve SSO token even after attempting user prompt : err: %{public}@"
- "Unable to retrieve SSO token. Not prompting for background download due to options. Discretionary: %@ disableUI: %@"
- "Unable to retrieve SSO token. Prompting user for foreground download"
- "Using MobileAsssetToken from override location"
- "Value read from chosen node is invalid. Could not obtain boot-manifest-hash"
- "Waiting for DeviceIdentity to return stashed certificate"
- "We have no info about this task, cannot reply: %{public}@  The downloads in flight are: %{public}@"
- "Will not prompt user for AppleConnect token for key retrieval due to discretionary download"
- "Will not prompt user for AppleConnect token for key retrieval due to override on downloadOptions"
- "[%{public}@] {%{public}@}\n[VEND] new set-descriptor generated without lookup required | setInfoInstance:%{public}@, newSetDescriptor:%{public}@"
- "[AUTO-SHORT-TERM][SYMLINK]{_shortTermCreateSymbolicLink} unable to remove symlink (normal if no symlink yet created) | symbolicLinkFilename:%{public}@ | error:%{public}@"
- "[monitor:%ld,requiringRetry:%ld|triggered(noRetry:%ld,retryRequired:%ld)|backoffLevel:%ld|observers:%ld|attempt(activeMarker:%@,remaining:%ld)]"
- "[overall]instance:%@,selector:%@,UUID:%@,logger:%@,tasks:%lu,requests:%ld,table:%@,FSM:%@,sched:%@,NWFail:%@|beingCancled:%@|[earlier]sched:%@,NWFail:%@|bonded:%@|[active]instance:%@,desire:%@(awaitDownload:%@,checkAwait:%@),found:%@,end:%@,listen:%@,jobInfo:%@|[aggregated]policy:%@,clientRequested:%@|firstClientName:%@,triggeringLayer:%@|onFilesystemByVersion:%ld|[check]Base:%@,UUID:%@,lookupGrant:%@,rampFG:%@,rampLatch:%@,options:%@|[asset]base:%@,patch:%@,full:%@,newer:%@,downloading:%@,scheduler:%@,lookupRsp:%@(forConfig:%@),user:%@,boosting:%@,checking:%@,determining:%@,locking:%@,patched:%@|[installed]:version:%@,build:%@|[status]current:%@,progress:%@,lastPatch:%@|[results]selector:%@,instance:%@,found:%@,end:%@,listen:%@,[set]aggregatedPolicy:%@,descriptor:%@,next:%ld,found:%@"
- "_chooseOrderForNextAttemptAndStartFirstJob:"
- "_logger"
- "_nwActivityObjects"
- "_nwQueue"
- "_perfResultsCPI"
- "_removeAllQueuedForEliminateSelector"
- "_removeAllQueuedForEliminateSelector:"
- "_stagedAssetToSetDescriptorCache"
- "_stagedIsNewOSPromotedCache"
- "_startupSignpostCPI"
- "action_FiredRetryWaitOrderAttemptFirstJobActive:error:"
- "action_OrderAttemptFirstJobActive:error:"
- "action_StartBackoffAndRetryWaitTimers:error:"
- "action_StopBackoffOrderAttemptFirstJobActive:error:"
- "com.apple.MobileAsset.daemon.nwActivity.state"
- "copyPreviouslyCreatedCertsIfPresent:"
- "initForDescriptor:baseForPatchDescriptor:withAutoAssetUUID:"
- "initForInstance:orForSelector:orForDescriptor:orForSetInstance:withSetDesire:withSchedulerSetPolicy:withStagerSetPolicy:usingSetConfiguration:usingSetDescriptor:withBaseForPatchDescriptor:withAutoAssetUUID:downloadingUserInitiated:asStagerJob:usingCachedAutoAssetCatalog:"
- "initForInstance:withAutoAssetUUID:downloadingUserInitiated:"
- "initForModule:ofModuleVersion:usingDispatchQueue:usingLogger:loggingByName:withVersionMigrator:"
- "initForSelector:withAutoAssetUUID:"
- "initForSelector:withAutoAssetUUID:asStagerJob:withStagerSetPolicy:usingCachedAutoAssetCatalog:usingBaseForPatching:"
- "initForSetConfiguration:withAutoAssetUUID:asStagerJob:withStagerSetPolicy:"
- "initForSetInstance:withSchedulerSetPolicy:usingSetConfiguration:usingSetDescriptor:withAutoAssetUUID:"
- "initForSetInstance:withSetDesire:usingSetConfiguration:usingSetDescriptor:withAutoAssetUUID:"
- "initForTriggeredNoActivity"
- "initForTriggeredSelectors:"
- "initForTriggeredSets:"
- "initWithCategory:"
- "initWithMonitorMarkers:withMarkersNoRetry:withMarkersRequiringRetry:"
- "initWithParamType:withSafeSummary:withMonitorMarkers:withMarkersNoRetry:withMarkersRequiringRetry:withFinishedMarker:withPotentialNetworkFailure:withObservedNetworkPath:"
- "initWithParamType:withSafeSummary:withScheduledJobs:withClientID:withClientRequestMessage:withClientProgressProxy:withClientReplyCompletion:withResponseMessage:withResponseError:withDownloadsInFlight:withDownloadOptions:withAutoAssetJobID:withAutoAssetCatalog:withLockForUseError:withFinishedError:withDownloadProgress:withJobCurrentStatus:withAutoAssetSelector:withAutoAssetUUID:withSetOfAutoAssetSelectors:withPushNotifications:withSetDescriptor:withAutoAssetDescriptors:withSetPolicy:withAssetTargetOSVersion:withAssetTargetBuildVersion:withAssetTargetTrainName:withAssetTargetRestoreVersion:withStagedToDownloaded:withStagedLookupResults:withDownloadingDescriptor:withBaseForPatchDescriptor:withBaseForStagingDescriptors:withSchedulerInvolved:withPotentialNetworkFailure:withRequiringLoadPriorToUse:withClientDomainName:withAssetSetIdentifier:withSetConfiguration:withSetAtomicInstance:withSetJobInformation:withTriggeredSets:"
- "invalidating"
- "isAnyAssetFromSetFromNewOSPromoted"
- "isAnyAssetFromSetFromNewOSPromoted:"
- "issueAndCopyCertsInternal:"
- "locateLockBySelector:"
- "locateSetDescriptorForStagingDescriptor:"
- "locateStagedSetDescriptorFor"
- "locateStagedSetDescriptorFor:"
- "logger:%@|policy:%@|server:%@|table:%@|FSM:%@|(persisted)active:%@,known:%@,configs:%@,AI:%@|(sets)active:%@,desc:%@,targets:%@,lookups:%@,map:%@"
- "logger:%@|policy:%@|server:%@|table:%@|FSM:%@|(persisted)activeJobs:%@,knownDescriptors:%@,setConfigurations:%@,setAtomicInstances:%@,activeSes:%@,downloadedSets:%@,setTargets:%@,setLookupConfigurations:%@,setLockUsageMap:%@"
- "newSetDescriptorIfOtherSatisfying:forSetInfoInstance:"
- "nwActivityObjects"
- "nwQueue"
- "oslog"
- "perfResultsCPI"
- "queued job no longer relevant due to elimination of associated asset-selector | eliminateSelector:%@"
- "read back"
- "reading back"
- "setNwActivityObjects:"
- "setNwQueue:"
- "setPerfResultsCPI:"
- "setStagedAssetToSetDescriptorCache:"
- "setStagedIsNewOSPromotedCache:"
- "setStartupSignpostCPI:"
- "stagedAssetToSetDescriptorCache"
- "stagedIsNewOSPromotedCache"
- "stagedToDownloadedFromStager"
- "startupSignpostCPI"
- "unable to create symbolic link for SHORT-TERM locking latest | %@ >=> %@"
- "{%@} duplicate nextAtomicEntry ignored | nextAtomicEntry:%@ | setInfoInstance:%@"
- "{%@} no nextAtomicEntry | nextSetEntry:%@ | satisfyingSetDescriptor:%@"
- "{AUTO-SCHEDULER:_registerForAndStartActivity} made attempt to re-register with desired delayPeriod:%{public}@"
- "{_removeAllQueuedForEliminateSelector:} nil jobParam encountered on clientRequestsAwaitingFirstUnlock | %@"
- "{_removeAllQueuedForEliminateSelector:} nil jobParam encountered on clientRequestsAwaitingSync | %@"

```
