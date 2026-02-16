## CloudDocs

> `/System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs`

```diff

-4257.80.8.0.0
-  __TEXT.__text: 0x8ba3c
-  __TEXT.__auth_stubs: 0x13c0
-  __TEXT.__objc_methlist: 0x679c
+4479.100.79.0.4
+  __TEXT.__text: 0x85050
+  __TEXT.__auth_stubs: 0x1410
+  __TEXT.__objc_methlist: 0x6554
   __TEXT.__const: 0x1b0
-  __TEXT.__gcc_except_tab: 0x4c08
-  __TEXT.__cstring: 0xb6d6
-  __TEXT.__oslogstring: 0x9587
+  __TEXT.__gcc_except_tab: 0x4284
+  __TEXT.__cstring: 0xb298
+  __TEXT.__oslogstring: 0x8a99
   __TEXT.__dlopen_cstrs: 0x4c
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x2730
-  __TEXT.__objc_classname: 0xdd2
-  __TEXT.__objc_methname: 0x11107
-  __TEXT.__objc_methtype: 0x3c61
-  __TEXT.__objc_stubs: 0xb1a0
+  __TEXT.__unwind_info: 0x25e0
+  __TEXT.__objc_classname: 0xd8a
+  __TEXT.__objc_methname: 0x10e95
+  __TEXT.__objc_methtype: 0x3bfd
+  __TEXT.__objc_stubs: 0xadc0
   __DATA_CONST.__got: 0x8b8
-  __DATA_CONST.__const: 0x2690
-  __DATA_CONST.__objc_classlist: 0x318
+  __DATA_CONST.__const: 0x2448
+  __DATA_CONST.__objc_classlist: 0x308
   __DATA_CONST.__objc_catlist: 0xe8
-  __DATA_CONST.__objc_protolist: 0x118
+  __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4230
+  __DATA_CONST.__objc_selrefs: 0x4198
   __DATA_CONST.__objc_protorefs: 0x68
-  __DATA_CONST.__objc_superrefs: 0x250
+  __DATA_CONST.__objc_superrefs: 0x230
   __DATA_CONST.__objc_arraydata: 0x88
-  __AUTH_CONST.__auth_got: 0x9f0
-  __AUTH_CONST.__const: 0x1120
-  __AUTH_CONST.__cfstring: 0x5d00
-  __AUTH_CONST.__objc_const: 0xcbd0
+  __AUTH_CONST.__auth_got: 0xa18
+  __AUTH_CONST.__const: 0x1040
+  __AUTH_CONST.__cfstring: 0x5de0
+  __AUTH_CONST.__objc_const: 0xc1c8
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x528
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH.__objc_data: 0x1540
+  __AUTH.__objc_data: 0x14f0
   __AUTH.__data: 0xa8
-  __DATA.__objc_ivar: 0x654
-  __DATA.__data: 0xd90
-  __DATA.__bss: 0x3e8
+  __DATA.__objc_ivar: 0x5d0
+  __DATA.__data: 0xd30
+  __DATA.__bss: 0x3f0
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x9b0
+  __DATA_DIRTY.__objc_data: 0x960
   __DATA_DIRTY.__data: 0x28
-  __DATA_DIRTY.__bss: 0x298
+  __DATA_DIRTY.__bss: 0x280
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 26CD2116-6433-3C06-9954-6A2ACFDE1757
-  Functions: 3104
-  Symbols:   10844
-  CStrings:  6260
+  UUID: F1F59A85-E1B5-3069-983B-713B5CD28C07
+  Functions: 2984
+  Symbols:   10559
+  CStrings:  6125
 
Symbols:
+ +[BRContainersMonitor _darwinNotifyEventPacerDelay]
+ +[BRContainersMonitor _foregroundChangesSender]
+ +[BRContainersMonitor _foregroundChangesSender].cold.1
+ +[BRContainersMonitor _userDefaultsForContainersNotifications]
+ +[BRContainersMonitor _userDefaultsForContainersNotifications].cold.1
+ +[BRContainersMonitor _userDefaultsSuiteForContainersNotifications]
+ +[BRContainersMonitor notifyContainer:isForegroundState:]
+ +[BRContainersMonitor notifyContainer:isForegroundState:].cold.1
+ +[BRContainersMonitor resetNotifications]
+ +[BRContainersMonitor resetNotifications].cold.1
+ +[BRFileProviderServicesFactory _fetchSynchronousAutomaticErrorProxyFromURL:serviceName:interface:returnNilIfServiceNotFound:]
+ +[BRRFAEmailSettingRequest isEmailEnabledWithCompletionHandler:]
+ +[BRRFAEmailSettingRequest isEmailEnabledWithCompletionHandler:].cold.1
+ +[BRRFAEmailSettingRequest setEmailEnabled:completionHandler:]
+ +[BRRFAEmailSettingRequest setEmailEnabled:completionHandler:].cold.1
+ +[BRRFAUserNotificationsRequest handleUserNotificationResponse:completionHandler:]
+ +[BRSpecialFolders internalDaemonContainerPathWithError:]
+ +[BRSpecialFolders internalDaemonContainerPathWithError:].cold.1
+ +[BRSpecialFolders internalDaemonContainerPathWithError:].cold.2
+ +[BRSpecialFolders internalDaemonContainerPathWithError:].cold.3
+ +[NSError(BRAdditions) brc_errorZoneResetCrashRecovery]
+ +[NSError(BRAdditions) brc_errorZoneResetHierarchyTooDeep]
+ +[NSError(BRAdditions) brc_errorZoneResetOrphanLive]
+ +[NSError(BRAdditions) brc_errorZoneResetOrphanTombstone]
+ +[NSError(BRAdditions) brc_errorZoneResetStillWantsDataUnlinked]
+ +[NSError(BRAdditions) brc_errorZoneResetTesting]
+ +[NSError(BRAdditions) brc_errorZoneResetZoneBecameHealthy]
+ -[BRContainer setZoneRowID:]
+ -[BRContainer zoneRowID]
+ -[BRContainer(BRXcodeAdditions) currentStatus].cold.1
+ -[BRContainer(BRXcodeAdditions) lastServerUpdate].cold.1
+ -[BRContainersMonitor _checkChangesForConainerID:]
+ -[BRContainersMonitor _scanForChanges]
+ -[BRContainersMonitor _scanForChanges].cold.1
+ -[BRContainersMonitor _signalScanning]
+ -[BRDarwinNotifyReceiver retrieveStateAndNotifyWithToken:]
+ -[BRDarwinNotifySender incrementState]
+ -[BRItemCollectionGatherer _retryDeltaForError:]
+ -[BRItemCollectionGatherer collection:didEncounterError:].cold.1
+ -[BRMangledID obfuscatedDescription]
+ -[BRQueryItem namespacePolicy]
+ -[NSError(BRAdditions) br_isFileProviderInternalErrorCode:]
+ -[NSFileProviderDomain(BRAdditions) br_volumeUUIDForDataSeparated:withError:]
+ -[UMUserPersona(BRAdditions) br_personaIDWithDefault:]
+ GCC_except_table102
+ GCC_except_table115
+ GCC_except_table119
+ GCC_except_table120
+ GCC_except_table124
+ GCC_except_table125
+ GCC_except_table128
+ GCC_except_table130
+ GCC_except_table140
+ GCC_except_table146
+ GCC_except_table149
+ GCC_except_table156
+ GCC_except_table157
+ GCC_except_table162
+ GCC_except_table163
+ GCC_except_table174
+ GCC_except_table175
+ GCC_except_table178
+ GCC_except_table183
+ GCC_except_table187
+ GCC_except_table199
+ GCC_except_table21
+ GCC_except_table221
+ GCC_except_table227
+ GCC_except_table246
+ GCC_except_table247
+ GCC_except_table255
+ GCC_except_table265
+ GCC_except_table39
+ GCC_except_table45
+ GCC_except_table69
+ GCC_except_table77
+ OBJC_IVAR_$_BRQueryItem._namespacePolicy
+ OBJC_IVAR_$_BRQueryItem._userInfo
+ _BRCanGetFPItemIDForCKRecordID
+ _BREntitlementRFAEmailSetting
+ _BREntitlementRFANotificationHandling
+ _BRGetFPItemIDsForCKRecordIDs
+ _CONTAINER_PERSONA_PRIMARY
+ _NSFileProviderInternalErrorDomain
+ _OBJC_CLASS_$_BRRFAEmailSettingRequest
+ _OBJC_CLASS_$_BRRFAUserNotificationsRequest
+ _OBJC_IVAR_$_BRContainer._zoneRowID
+ _OBJC_IVAR_$_BRContainersMonitor._defaults
+ _OBJC_IVAR_$_BRContainersMonitor._foregroundChangesPacer
+ _OBJC_IVAR_$_BRContainersMonitor._foregroundChangesReceiver
+ _OBJC_IVAR_$_BRContainersMonitor._observedContainerIDsToLatestForegroundStatus
+ _OBJC_IVAR_$_BRDarwinNotifyReceiver._handler
+ _OBJC_METACLASS_$_BRRFAEmailSettingRequest
+ _OBJC_METACLASS_$_BRRFAUserNotificationsRequest
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _SpotlightIndexLibrary
+ _SpotlightIndexLibrary.cold.1
+ _SpotlightIndexLibrary.frameworkLibrary
+ __OBJC_$_CLASS_METHODS_BRRFAEmailSettingRequest
+ __OBJC_$_CLASS_METHODS_BRRFAUserNotificationsRequest
+ __OBJC_CLASS_RO_$_BRRFAEmailSettingRequest
+ __OBJC_CLASS_RO_$_BRRFAUserNotificationsRequest
+ __OBJC_METACLASS_RO_$_BRRFAEmailSettingRequest
+ __OBJC_METACLASS_RO_$_BRRFAUserNotificationsRequest
+ ___27-[BRContainersMonitor init]_block_invoke
+ ___27-[BRContainersMonitor init]_block_invoke_2
+ ___27-[BRContainersMonitor init]_block_invoke_2.cold.1
+ ___38-[BRQuery _processProgressUpdateBatch]_block_invoke.63
+ ___40-[BRQuery _applicationWillResignActive:]_block_invoke.88
+ ___40-[BRQuery _applicationWillResignActive:]_block_invoke.88.cold.1
+ ___45-[BRContainerCache initWithHelper:personaID:]_block_invoke.530
+ ___45-[BRContainerCache initWithHelper:personaID:]_block_invoke.530.cold.1
+ ___45-[BRContainerCache initWithHelper:personaID:]_block_invoke.531
+ ___46-[BRContainer(BRXcodeAdditions) currentStatus]_block_invoke.377
+ ___46-[BRQuery itemCollectionGathererDidInvalidate]_block_invoke.73
+ ___46-[BRQuery itemCollectionGathererDidInvalidate]_block_invoke.73.cold.1
+ ___47+[BRContainersMonitor _foregroundChangesSender]_block_invoke
+ ___49-[BRContainer(BRXcodeAdditions) lastServerUpdate]_block_invoke.375
+ ___50-[BRContainersMonitor _checkChangesForConainerID:]_block_invoke
+ ___52-[BRContainerCache subscribeToContainerStatusUpdate]_block_invoke_2
+ ___57+[BRContainersMonitor notifyContainer:isForegroundState:]_block_invoke
+ ___57+[BRContainersMonitor notifyContainer:isForegroundState:]_block_invoke.36
+ ___62+[BRContainersMonitor _userDefaultsForContainersNotifications]_block_invoke
+ ___62+[BRRFAEmailSettingRequest setEmailEnabled:completionHandler:]_block_invoke
+ ___64+[BRRFAEmailSettingRequest isEmailEnabledWithCompletionHandler:]_block_invoke
+ ___82+[BRRFAUserNotificationsRequest handleUserNotificationResponse:completionHandler:]_block_invoke
+ ___83-[BRContainer(BRFinderInternalAdditions) deleteAllContentsOnClientAndServer:error:]_block_invoke.411
+ ___93+[BRContainer(BRInternalAdditions) _generateiOSIconsForMangledID:usingBundle:generatedIcons:]_block_invoke.480
+ ___BRGetFPItemIDsForCKRecordIDs_block_invoke
+ ___block_descriptor_40_e8_32bs_e20_v20?0B8"NSError"12ls32l8
+ ___block_descriptor_40_e8_32s_e21_B16?0"BRContainer"8ls32l8
+ ___block_descriptor_40_e8_32w_e8_v16?0Q8lw32l8
+ ___block_descriptor_49_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_57_e8_32s40s48r_e46_v24?0"BRXPCAutomaticErrorProxy"8"NSError"16lr48l8s32l8s40l8
+ ___block_literal_global.218
+ ___block_literal_global.238
+ ___block_literal_global.34
+ ___block_literal_global.424
+ ___block_literal_global.436
+ ___block_literal_global.451
+ ___block_literal_global.454
+ ___block_literal_global.468
+ ___block_literal_global.470
+ ___block_literal_global.483
+ ___block_literal_global.485
+ ___block_literal_global.546
+ ___block_literal_global.548
+ ___block_literal_global.556
+ ___block_literal_global.563
+ ___block_literal_global.612
+ ___block_literal_global.708
+ __foregroundChangesSender._foregroundChangesSender
+ __foregroundChangesSender.onceToken
+ __userDefaultsForContainersNotifications.defaults
+ __userDefaultsForContainersNotifications.once
+ _container_copy_sandbox_token
+ _container_copy_unlocalized_description
+ _container_error_copy_unlocalized_description
+ _container_get_path
+ _container_query_create
+ _container_query_free
+ _container_query_get_last_error
+ _container_query_get_single_result
+ _container_query_operation_set_flags
+ _container_query_set_class
+ _container_query_set_identifiers
+ _container_query_set_persona_unique_string
+ _notifyContainer:isForegroundState:._foregroundChangesQueue
+ _notifyContainer:isForegroundState:.onceToken
+ _objc_msgSend$_checkChangesForConainerID:
+ _objc_msgSend$_darwinNotifyEventPacerDelay
+ _objc_msgSend$_foregroundChangesSender
+ _objc_msgSend$_retryDeltaForError:
+ _objc_msgSend$_scanForChanges
+ _objc_msgSend$_signalScanning
+ _objc_msgSend$_userDefaultsForContainersNotifications
+ _objc_msgSend$_userDefaultsSuiteForContainersNotifications
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$br_isFileProviderInternalErrorCode:
+ _objc_msgSend$br_obfuscateAliasTarget
+ _objc_msgSend$br_personaIDWithDefault:
+ _objc_msgSend$br_volumeUUIDForDataSeparated:withError:
+ _objc_msgSend$brc_unkownErrorWithDescription:
+ _objc_msgSend$containsValueForKey:
+ _objc_msgSend$getFPItemIDsForCKRecordIDs:reply:
+ _objc_msgSend$handleUserNotificationResponse:reply:
+ _objc_msgSend$incrementState
+ _objc_msgSend$initForEventName:
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$isRFAEmailSettingEnabledWithReply:
+ _objc_msgSend$notifyChangedState:
+ _objc_msgSend$removePersistentDomainForName:
+ _objc_msgSend$retrieveStateAndNotifyWithToken:
+ _objc_msgSend$setBool:forKey:
+ _objc_msgSend$setRFAEmailSettingEnabled:reply:
+ _objc_msgSend$zoneRowID
+ _xpc_string_create
- +[BRContainer(BRInternalAdditions) postContainerStatusChangeNotificationWithID:key:value:]
- +[BRContainer(BRInternalAdditions) postContainerStatusChangeNotificationWithID:key:value:].cold.1
- +[BRFileProviderServicesFactory _fetchSynchronousAutomaticErrorProxyFromURL:serviceName:interface:]
- -[BRNotificationReceiver .cxx_destruct]
- -[BRNotificationReceiver _invalidateAndNotify:]
- -[BRNotificationReceiver _obtainNotificationSenderFromDaemon]
- -[BRNotificationReceiver _obtainNotificationSenderFromDaemon].cold.1
- -[BRNotificationReceiver _obtainNotificationSenderFromDaemon].cold.2
- -[BRNotificationReceiver _receiveUpdates:]
- -[BRNotificationReceiver _signalSourceIfNeeded]
- -[BRNotificationReceiver _signalSourceIfNeeded].cold.1
- -[BRNotificationReceiver _watchUbiquitousScopes:bundleID:predicate:]
- -[BRNotificationReceiver _watchUbiquitousScopes:bundleID:predicate:].cold.1
- -[BRNotificationReceiver _watchUbiquitousScopes:bundleID:predicate:].cold.2
- -[BRNotificationReceiver _watchUbiquitousScopes:bundleID:predicate:].cold.3
- -[BRNotificationReceiver _watchUbiquitousScopes:bundleID:predicate:].cold.4
- -[BRNotificationReceiver _watchUbiquitousScopes:bundleID:predicate:].cold.5
- -[BRNotificationReceiver batchingChanges]
- -[BRNotificationReceiver batchingDelay]
- -[BRNotificationReceiver dealloc]
- -[BRNotificationReceiver dealloc].cold.1
- -[BRNotificationReceiver dealloc].cold.2
- -[BRNotificationReceiver delegate]
- -[BRNotificationReceiver dequeue:block:]
- -[BRNotificationReceiver disableUpdatesFromIPCBeforeStitching]
- -[BRNotificationReceiver enableUpdatesFromIPCAfterStitching]
- -[BRNotificationReceiver flush]
- -[BRNotificationReceiver init]
- -[BRNotificationReceiver init].cold.1
- -[BRNotificationReceiver invalidateAndDontNotifyDelegate]
- -[BRNotificationReceiver invalidateAndNotify:]
- -[BRNotificationReceiver invalidate]
- -[BRNotificationReceiver networkDidChangeReachabilityStatusTo:]
- -[BRNotificationReceiver networkDidChangeReachabilityStatusTo:].cold.1
- -[BRNotificationReceiver pendingCount]
- -[BRNotificationReceiver receiveProgressUpdates:reply:]
- -[BRNotificationReceiver receiveStitchingUpdates:]
- -[BRNotificationReceiver receiveUpdates:reply:]
- -[BRNotificationReceiver resume]
- -[BRNotificationReceiver resume].cold.1
- -[BRNotificationReceiver setBatchingChanges:]
- -[BRNotificationReceiver setBatchingDelay:]
- -[BRNotificationReceiver setDelegate:]
- -[BRNotificationReceiver suspend]
- -[BRNotificationReceiver watchUbiquitousScopes:bundleID:predicate:]
- -[BRQuery _processChanges:]
- -[BRQuery _processChanges:].cold.1
- -[BRQuery _processChanges:].cold.2
- -[BRQuery _processUpdates].cold.6
- -[BRQuery _sendHasUpdateNotificationIfNeeded]
- -[BRQuery _sendHasUpdateNotificationIfNeeded].cold.1
- -[BRQuery dealloc].cold.2
- -[BRQuery notificationReceiverDidReceiveNotifications:]
- -[BRQuery notificationsReceiverDidFinishGathering:]
- -[BRQuery notificationsReceiverDidInvalidate:]
- -[BRQuery notificationsReceiverDidReceiveNotificationsBatch:]
- -[BRQuery receiver]
- -[BRQuery setReceiver:]
- -[BRQueryItem attachLogicalExtension:physicalExtension:]
- -[BRQueryItem attachLogicalExtension:physicalExtension:].cold.1
- -[BRQueryItem attachLogicalExtension:physicalExtension:].cold.2
- -[BRQueryItem attachLogicalExtension:physicalExtension:].cold.3
- -[BRQueryItem attachLogicalExtension:physicalExtension:].cold.4
- -[BRQueryItem attachLogicalExtension:physicalExtension:].cold.5
- -[BRQueryItem attachLogicalExtension:physicalExtension:].cold.6
- -[BRQueryItem fromRelativePath]
- -[BRQueryItem isPreCrash]
- -[BRQueryItem physicalName]
- -[BRQueryItem setIsPreCrash:]
- -[BRQueryItemProgressObserver .cxx_destruct]
- -[BRQueryItemProgressObserver _stopObserving]
- -[BRQueryItemProgressObserver _subscribe]
- -[BRQueryItemProgressObserver dealloc]
- -[BRQueryItemProgressObserver dealloc].cold.1
- -[BRQueryItemProgressObserver dealloc].cold.2
- -[BRQueryItemProgressObserver description]
- -[BRQueryItemProgressObserver initWithItem:]
- -[BRQueryItemProgressObserver item]
- -[BRQueryItemProgressObserver observeValueForKeyPath:ofObject:change:context:]
- -[BRQueryItemProgressObserver observeValueForKeyPath:ofObject:change:context:].cold.1
- -[BRQueryItemProgressObserver progressHandler]
- -[BRQueryItemProgressObserver setProgressHandler:]
- -[BRQueryItemProgressObserver setQueue:]
- -[BRQueryItemProgressObserver start]
- -[BRQueryItemProgressObserver start].cold.1
- -[BRQueryItemProgressObserver start].cold.2
- -[BRQueryItemProgressObserver stop]
- -[BRQueryItemProgressObserver stop].cold.1
- -[BRQueryItemProgressObserver stop].cold.2
- -[BRQueryStitch .cxx_destruct]
- -[BRQueryStitch _creationDone]
- -[BRQueryStitch _creationDone].cold.1
- -[BRQueryStitch _deletionDone]
- -[BRQueryStitch _deletionDone].cold.1
- -[BRQueryStitch _enableUpdatesFromIPCAfterStitchingOnAllQueries]
- -[BRQueryStitch _renameDone]
- -[BRQueryStitch _renameDone].cold.1
- -[BRQueryStitch _renameDone].cold.2
- -[BRQueryStitch contexts]
- -[BRQueryStitch dealloc]
- -[BRQueryStitch description]
- -[BRQueryStitch done]
- -[BRQueryStitch done].cold.1
- -[BRQueryStitch fromURL]
- -[BRQueryStitch initWithURL:objid:kind:]
- -[BRQueryStitch setContexts:]
- -[BRQueryStitch setFromURL:]
- -[BRQueryStitch setQueries:]
- -[BRQueryStitch setQueries:].cold.1
- -[BRQueryStitchingContext .cxx_destruct]
- -[BRQueryStitchingContext initWithQuery:]
- -[BRQueryStitchingContext performAsyncOnReceiver:]
- -[NSFileProviderDomain(BRAdditions) br_volumeUUID]
- GCC_except_table100
- GCC_except_table116
- GCC_except_table117
- GCC_except_table118
- GCC_except_table122
- GCC_except_table123
- GCC_except_table126
- GCC_except_table131
- GCC_except_table138
- GCC_except_table145
- GCC_except_table147
- GCC_except_table150
- GCC_except_table151
- GCC_except_table153
- GCC_except_table158
- GCC_except_table161
- GCC_except_table168
- GCC_except_table176
- GCC_except_table179
- GCC_except_table180
- GCC_except_table181
- GCC_except_table185
- GCC_except_table195
- GCC_except_table219
- GCC_except_table237
- GCC_except_table243
- GCC_except_table244
- GCC_except_table252
- GCC_except_table262
- GCC_except_table33
- GCC_except_table59
- GCC_except_table80
- GCC_except_table83
- OBJC_IVAR_$_BRContainersMonitor._notifyTokenByContainerID
- OBJC_IVAR_$_BRQueryItem._localRepresentationURL
- OBJC_IVAR_$_BRQueryItem._physicalName
- _MobileSpotlightIndexLibrary
- _MobileSpotlightIndexLibrary.cold.1
- _MobileSpotlightIndexLibrary.frameworkLibrary
- _OBJC_CLASS_$_BRNotificationReceiver
- _OBJC_CLASS_$_BRQueryItemProgressObserver
- _OBJC_CLASS_$_BRQueryStitch
- _OBJC_CLASS_$_BRQueryStitchingContext
- _OBJC_IVAR_$_BRContainer._observationSetupQueueForDefaultConnection
- _OBJC_IVAR_$_BRNotificationReceiver._accountTokenDidChangeNotificationObserver
- _OBJC_IVAR_$_BRNotificationReceiver._batchingChanges
- _OBJC_IVAR_$_BRNotificationReceiver._batchingDelay
- _OBJC_IVAR_$_BRNotificationReceiver._delegate
- _OBJC_IVAR_$_BRNotificationReceiver._gatherDones
- _OBJC_IVAR_$_BRNotificationReceiver._ipcQueue
- _OBJC_IVAR_$_BRNotificationReceiver._isInvalidated
- _OBJC_IVAR_$_BRNotificationReceiver._isNetworkReachable
- _OBJC_IVAR_$_BRNotificationReceiver._itemInTransferByID
- _OBJC_IVAR_$_BRNotificationReceiver._lastBatchTime
- _OBJC_IVAR_$_BRNotificationReceiver._networkReachabilityToken
- _OBJC_IVAR_$_BRNotificationReceiver._notifs
- _OBJC_IVAR_$_BRNotificationReceiver._personaID
- _OBJC_IVAR_$_BRNotificationReceiver._progressObserverByID
- _OBJC_IVAR_$_BRNotificationReceiver._queue
- _OBJC_IVAR_$_BRNotificationReceiver._receivedChanges
- _OBJC_IVAR_$_BRNotificationReceiver._sender
- _OBJC_IVAR_$_BRNotificationReceiver._source
- _OBJC_IVAR_$_BRNotificationReceiver._suspendCount
- _OBJC_IVAR_$_BRNotificationReceiver._timer
- _OBJC_IVAR_$_BRQuery._needsCrashEvicting
- _OBJC_IVAR_$_BRQuery._needsCrashMarking
- _OBJC_IVAR_$_BRQuery._receiver
- _OBJC_IVAR_$_BRQueryItemProgressObserver._isUpload
- _OBJC_IVAR_$_BRQueryItemProgressObserver._item
- _OBJC_IVAR_$_BRQueryItemProgressObserver._progress
- _OBJC_IVAR_$_BRQueryItemProgressObserver._progressHandler
- _OBJC_IVAR_$_BRQueryItemProgressObserver._queue
- _OBJC_IVAR_$_BRQueryItemProgressObserver._started
- _OBJC_IVAR_$_BRQueryItemProgressObserver._subscriber
- _OBJC_IVAR_$_BRQueryStitch._contexts
- _OBJC_IVAR_$_BRQueryStitch._fromURL
- _OBJC_IVAR_$_BRQueryStitch._kind
- _OBJC_IVAR_$_BRQueryStitch._objid
- _OBJC_IVAR_$_BRQueryStitch._url
- _OBJC_IVAR_$_BRQueryStitchingContext._query
- _OBJC_IVAR_$_BRQueryStitchingContext._receiver
- _OBJC_METACLASS_$_BRNotificationReceiver
- _OBJC_METACLASS_$_BRQueryItemProgressObserver
- _OBJC_METACLASS_$_BRQueryStitch
- _OBJC_METACLASS_$_BRQueryStitchingContext
- __OBJC_$_INSTANCE_METHODS_BRNotificationReceiver
- __OBJC_$_INSTANCE_METHODS_BRQueryItemProgressObserver
- __OBJC_$_INSTANCE_METHODS_BRQueryStitch
- __OBJC_$_INSTANCE_METHODS_BRQueryStitchingContext
- __OBJC_$_INSTANCE_VARIABLES_BRNotificationReceiver
- __OBJC_$_INSTANCE_VARIABLES_BRQueryItemProgressObserver
- __OBJC_$_INSTANCE_VARIABLES_BRQueryStitch
- __OBJC_$_INSTANCE_VARIABLES_BRQueryStitchingContext
- __OBJC_$_PROP_LIST_BRNotificationReceiver
- __OBJC_$_PROP_LIST_BRQueryItemProgressObserver
- __OBJC_$_PROP_LIST_BRQueryStitch
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_BRNotificationReceiverDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_BRNotificationReceiverDelegate
- __OBJC_$_PROTOCOL_REFS_BRNotificationReceiverDelegate
- __OBJC_CLASS_PROTOCOLS_$_BRNotificationReceiver
- __OBJC_CLASS_RO_$_BRNotificationReceiver
- __OBJC_CLASS_RO_$_BRQueryItemProgressObserver
- __OBJC_CLASS_RO_$_BRQueryStitch
- __OBJC_CLASS_RO_$_BRQueryStitchingContext
- __OBJC_LABEL_PROTOCOL_$_BRNotificationReceiverDelegate
- __OBJC_METACLASS_RO_$_BRNotificationReceiver
- __OBJC_METACLASS_RO_$_BRQueryItemProgressObserver
- __OBJC_METACLASS_RO_$_BRQueryStitch
- __OBJC_METACLASS_RO_$_BRQueryStitchingContext
- __OBJC_PROTOCOL_$_BRNotificationReceiverDelegate
- ___28-[BRQueryStitch _renameDone]_block_invoke
- ___28-[BRQueryStitch setQueries:]_block_invoke
- ___30-[BRNotificationReceiver init]_block_invoke
- ___30-[BRQueryStitch _creationDone]_block_invoke
- ___30-[BRQueryStitch _deletionDone]_block_invoke
- ___31-[BRNotificationReceiver flush]_block_invoke
- ___31-[BRNotificationReceiver flush]_block_invoke_2
- ___35-[BRQueryItemProgressObserver stop]_block_invoke
- ___38-[BRNotificationReceiver pendingCount]_block_invoke
- ___38-[BRQuery _processProgressUpdateBatch]_block_invoke.138
- ___40-[BRQuery _applicationWillResignActive:]_block_invoke.160
- ___40-[BRQuery _applicationWillResignActive:]_block_invoke.160.cold.1
- ___41-[BRQueryItemProgressObserver _subscribe]_block_invoke
- ___41-[BRQueryItemProgressObserver _subscribe]_block_invoke.10
- ___41-[BRQueryItemProgressObserver _subscribe]_block_invoke.10.cold.1
- ___41-[BRQueryItemProgressObserver _subscribe]_block_invoke.7
- ___41-[BRQueryItemProgressObserver _subscribe]_block_invoke.8
- ___41-[BRQueryItemProgressObserver _subscribe]_block_invoke.8.cold.1
- ___41-[BRQueryItemProgressObserver _subscribe]_block_invoke_2
- ___41-[BRQueryItemProgressObserver _subscribe]_block_invoke_2.11
- ___41-[BRQueryItemProgressObserver _subscribe]_block_invoke_2.cold.1
- ___42-[BRNotificationReceiver _receiveUpdates:]_block_invoke
- ___45-[BRContainerCache initWithHelper:personaID:]_block_invoke.527
- ___45-[BRContainerCache initWithHelper:personaID:]_block_invoke.527.cold.1
- ___45-[BRContainerCache initWithHelper:personaID:]_block_invoke.528
- ___46-[BRContainer(BRXcodeAdditions) currentStatus]_block_invoke.371
- ___46-[BRNotificationReceiver invalidateAndNotify:]_block_invoke
- ___46-[BRQuery itemCollectionGathererDidInvalidate]_block_invoke.144
- ___46-[BRQuery itemCollectionGathererDidInvalidate]_block_invoke.144.cold.1
- ___46-[BRQuery notificationsReceiverDidInvalidate:]_block_invoke
- ___46-[BRQuery notificationsReceiverDidInvalidate:]_block_invoke.cold.1
- ___46-[BRQuery notificationsReceiverDidInvalidate:]_block_invoke.cold.2
- ___46-[BRQuery notificationsReceiverDidInvalidate:]_block_invoke.cold.3
- ___47-[BRNotificationReceiver _invalidateAndNotify:]_block_invoke
- ___47-[BRNotificationReceiver _signalSourceIfNeeded]_block_invoke
- ___47-[BRNotificationReceiver receiveUpdates:reply:]_block_invoke
- ___47-[BRNotificationReceiver receiveUpdates:reply:]_block_invoke.cold.1
- ___49-[BRContainer(BRXcodeAdditions) lastServerUpdate]_block_invoke.369
- ___50-[BRContainersMonitor addObserver:forContainerID:]_block_invoke
- ___50-[BRContainersMonitor addObserver:forContainerID:]_block_invoke.15
- ___50-[BRNotificationReceiver receiveStitchingUpdates:]_block_invoke
- ___50-[BRQueryStitchingContext performAsyncOnReceiver:]_block_invoke
- ___51-[BRQuery notificationsReceiverDidFinishGathering:]_block_invoke
- ___51-[BRQuery notificationsReceiverDidFinishGathering:]_block_invoke_2
- ___55-[BRNotificationReceiver receiveProgressUpdates:reply:]_block_invoke
- ___55-[BRQuery notificationReceiverDidReceiveNotifications:]_block_invoke
- ___57-[BRItemCollectionGatherer collection:didEncounterError:]_block_invoke.68.cold.1
- ___61-[BRDarwinNotifyReceiver initForEventName:withQueue:handler:]_block_invoke_2
- ___61-[BRNotificationReceiver _obtainNotificationSenderFromDaemon]_block_invoke
- ___61-[BRNotificationReceiver _obtainNotificationSenderFromDaemon]_block_invoke.14
- ___61-[BRNotificationReceiver _obtainNotificationSenderFromDaemon]_block_invoke.17
- ___61-[BRNotificationReceiver _obtainNotificationSenderFromDaemon]_block_invoke.22
- ___61-[BRNotificationReceiver _obtainNotificationSenderFromDaemon]_block_invoke.22.cold.1
- ___61-[BRNotificationReceiver _obtainNotificationSenderFromDaemon]_block_invoke.22.cold.2
- ___61-[BRNotificationReceiver _obtainNotificationSenderFromDaemon]_block_invoke.22.cold.3
- ___61-[BRNotificationReceiver _obtainNotificationSenderFromDaemon]_block_invoke.22.cold.4
- ___61-[BRNotificationReceiver _obtainNotificationSenderFromDaemon]_block_invoke.22.cold.5
- ___61-[BRNotificationReceiver _obtainNotificationSenderFromDaemon]_block_invoke.8
- ___61-[BRNotificationReceiver _obtainNotificationSenderFromDaemon]_block_invoke.cold.1
- ___61-[BRNotificationReceiver _obtainNotificationSenderFromDaemon]_block_invoke_2
- ___61-[BRQuery notificationsReceiverDidReceiveNotificationsBatch:]_block_invoke
- ___61-[BRQuery notificationsReceiverDidReceiveNotificationsBatch:]_block_invoke_2
- ___62-[BRNotificationReceiver disableUpdatesFromIPCBeforeStitching]_block_invoke
- ___64-[BRQueryStitch _enableUpdatesFromIPCAfterStitchingOnAllQueries]_block_invoke
- ___67-[BRNotificationReceiver watchUbiquitousScopes:bundleID:predicate:]_block_invoke
- ___68-[BRNotificationReceiver _watchUbiquitousScopes:bundleID:predicate:]_block_invoke
- ___68-[BRNotificationReceiver _watchUbiquitousScopes:bundleID:predicate:]_block_invoke.31
- ___68-[BRNotificationReceiver _watchUbiquitousScopes:bundleID:predicate:]_block_invoke.32
- ___68-[BRNotificationReceiver _watchUbiquitousScopes:bundleID:predicate:]_block_invoke.32.cold.1
- ___68-[BRNotificationReceiver _watchUbiquitousScopes:bundleID:predicate:]_block_invoke.32.cold.2
- ___68-[BRNotificationReceiver _watchUbiquitousScopes:bundleID:predicate:]_block_invoke.33
- ___68-[BRNotificationReceiver _watchUbiquitousScopes:bundleID:predicate:]_block_invoke.35
- ___68-[BRNotificationReceiver _watchUbiquitousScopes:bundleID:predicate:]_block_invoke.36
- ___68-[BRNotificationReceiver _watchUbiquitousScopes:bundleID:predicate:]_block_invoke.37
- ___68-[BRNotificationReceiver _watchUbiquitousScopes:bundleID:predicate:]_block_invoke.cold.1
- ___68-[BRNotificationReceiver _watchUbiquitousScopes:bundleID:predicate:]_block_invoke_2
- ___78-[BRQueryItemProgressObserver observeValueForKeyPath:ofObject:change:context:]_block_invoke
- ___78-[BRQueryItemProgressObserver observeValueForKeyPath:ofObject:change:context:]_block_invoke.cold.1
- ___78-[BRQueryItemProgressObserver observeValueForKeyPath:ofObject:change:context:]_block_invoke.cold.2
- ___83-[BRContainer(BRFinderInternalAdditions) deleteAllContentsOnClientAndServer:error:]_block_invoke.405
- ___93+[BRContainer(BRInternalAdditions) _generateiOSIconsForMangledID:usingBundle:generatedIcons:]_block_invoke.475
- ___block_descriptor_32_e39_v32?0"NSString"8"NSDictionary"16^B24l
- ___block_descriptor_32_e61_v32?0"BRNotificationReceiver"8"NSArray"16"NSDictionary"24l
- ___block_descriptor_40_e8_32s_e17_v16?0"NSArray"8ls32l8
- ___block_descriptor_40_e8_32s_e21_v16?0"BRQueryItem"8ls32l8
- ___block_descriptor_40_e8_32s_e24_v16?0"NSNotification"8ls32l8
- ___block_descriptor_40_e8_32s_e61_v32?0"BRNotificationReceiver"8"NSArray"16"NSDictionary"24ls32l8
- ___block_descriptor_44_e8_32bs_e5_v8?0ls32l8
- ___block_descriptor_48_e8_32s40bs_e26_?<v?>16?0"NSProgress"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e8_v12?0i8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e61_v32?0"BRNotificationReceiver"8"NSArray"16"NSDictionary"24ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e86_v32?0"<BRItemNotificationSending><NSXPCProxyCreating>"8"NSDictionary"16"NSError"24ls32l8s40l8
- ___block_descriptor_56_e8_32s40r48r_e28_v24?0"FPItem"8"NSError"16ls32l8r40l8r48l8
- ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
- ___block_descriptor_56_e8_32s40s48r_e46_v24?0"BRXPCAutomaticErrorProxy"8"NSError"16lr48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s48r_e8_v12?0i8lr48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e8_v12?0i8ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_66_e8_32s40s48bs56r_e36_v32?0"NSString"8B16B20"NSError"24ls32l8r56l8s40l8s48l8
- ___block_literal_global.159
- ___block_literal_global.173
- ___block_literal_global.221
- ___block_literal_global.235
- ___block_literal_global.241
- ___block_literal_global.25
- ___block_literal_global.40
- ___block_literal_global.420
- ___block_literal_global.432
- ___block_literal_global.445
- ___block_literal_global.448
- ___block_literal_global.464
- ___block_literal_global.465
- ___block_literal_global.47
- ___block_literal_global.478
- ___block_literal_global.481
- ___block_literal_global.543
- ___block_literal_global.545
- ___block_literal_global.551
- ___block_literal_global.553
- ___block_literal_global.607
- ___block_literal_global.703
- ___fileProgressSubscribeQueue_block_invoke
- __block_invoke_2.__personaOnceToken
- __block_invoke_2.__personalPersona
- __os_feature_enabled_impl
- _dispatch_async_with_logs
- _fileProgressSubscribeQueue
- _fileProgressSubscribeQueue.cold.1
- _fileProgressSubscribeQueue.fileProgressSubscribeQueue
- _fileProgressSubscribeQueue.onceToken
- _kCFURLNameKey
- _notify_is_valid_token
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_collectUpdates:
- _objc_msgSend$_creationDone
- _objc_msgSend$_deletionDone
- _objc_msgSend$_enableUpdatesFromIPCAfterStitchingOnAllQueries
- _objc_msgSend$_invalidateAndNotify:
- _objc_msgSend$_obtainNotificationSenderFromDaemon
- _objc_msgSend$_processChanges:
- _objc_msgSend$_processUpdates
- _objc_msgSend$_receiveUpdates:
- _objc_msgSend$_renameDone
- _objc_msgSend$_sendHasUpdateNotificationIfNeeded
- _objc_msgSend$_signalSourceIfNeeded
- _objc_msgSend$_stopObserving
- _objc_msgSend$_subscribe
- _objc_msgSend$_watchUbiquitousScopes:bundleID:predicate:
- _objc_msgSend$addNotification:asDead:
- _objc_msgSend$addSubscriberForFileURL:usingBlock:
- _objc_msgSend$boostPriority:
- _objc_msgSend$br_isSideFaultName
- _objc_msgSend$br_isStrictlyInSyncedLocation
- _objc_msgSend$dequeue:block:
- _objc_msgSend$disableUpdatesFromIPCBeforeStitching
- _objc_msgSend$done
- _objc_msgSend$enableUpdatesFromIPCAfterStitching
- _objc_msgSend$fetchItemForItemID:completionHandler:
- _objc_msgSend$flush
- _objc_msgSend$folderID
- _objc_msgSend$getItemUpdateSenderWithReceiver:reply:
- _objc_msgSend$initWithArray:copyItems:
- _objc_msgSend$initWithItem:
- _objc_msgSend$initWithObjects:
- _objc_msgSend$initWithQuery:
- _objc_msgSend$invalidateAndNotify:
- _objc_msgSend$isDownloadActive
- _objc_msgSend$isFolderOrAliasID
- _objc_msgSend$isInternalBuild
- _objc_msgSend$isPreCrash
- _objc_msgSend$isUploadActive
- _objc_msgSend$item
- _objc_msgSend$mergeProgressUpdate:
- _objc_msgSend$networkDidChangeReachabilityStatusTo:
- _objc_msgSend$notificationReceiverDidReceiveNotifications:
- _objc_msgSend$notificationsReceiverDidFinishGathering:
- _objc_msgSend$notificationsReceiverDidInvalidate:
- _objc_msgSend$notificationsReceiverDidReceiveNotificationsBatch:
- _objc_msgSend$pendingCount
- _objc_msgSend$performAsyncOnReceiver:
- _objc_msgSend$receiveStitchingUpdates:
- _objc_msgSend$receiver
- _objc_msgSend$removeObserver:forKeyPath:context:
- _objc_msgSend$setIsPreCrash:
- _objc_msgSend$setQueue:
- _objc_msgSend$setReceiver:
- _objc_msgSend$suspend
- _objc_msgSend$watchItemAtURL:options:gatherReply:
- _objc_msgSend$watchItemsNamesPrefixedBy:inScopes:appLibraryIDs:gatherReply:
- _objc_msgSend$watchScopes:appLibraryIDs:gatherReply:
- _objc_msgSend$watchScopes:gatherReply:
- _objc_release_x2
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x9
CStrings:
+ " namespace-policy:%ld"
+ "(?=\"\"{?=\"downloadStatus\"b2\"uploadStatus\"b2\"itemStatus\"b2\"conflicted\"b1\"isUploadActive\"b1\"isDownloadActive\"b1\"isDownloadRequested\"b1\"shareOptions\"b3\"isHiddenExtension\"b1\"isTrashed\"b1\"itemMode\"b3\"fromReadOnlyDB\"b1\"isSharedFolderSubItem\"b1\"isSharedToMeOrContainsSharedToMeItem\"b1\"isSharedByMeOrContainsSharedByMeItem\"b1\"editedSinceShared\"b1\"isNetworkOffline\"b1\"isHiddenItem\"b1\"isTopLevel\"b1\"isEvictable\"b1\"isAppLibraryTrashFolder\"b1\"isAppLibraryRootFolder\"b1\"isAppLibraryDocumentsFolder\"b1\"evadeSpotlightIndexing\"b1\"isContentZoneRoot\"b1\"kind\"C}\"value\"Q)"
+ "+[BRContainersMonitor notifyContainer:isForegroundState:]"
+ "+[BRContainersMonitor resetNotifications]"
+ "+[BRRFAEmailSettingRequest isEmailEnabledWithCompletionHandler:]"
+ "+[BRRFAEmailSettingRequest setEmailEnabled:completionHandler:]"
+ "+[BRSpecialFolders internalDaemonContainerPathWithError:]"
+ "-[BRContainer(BRXcodeAdditions) currentStatus]"
+ "-[BRContainer(BRXcodeAdditions) lastServerUpdate]"
+ "-[BRContainersMonitor _checkChangesForConainerID:]"
+ "-[BRContainersMonitor _checkChangesForConainerID:]_block_invoke"
+ "-[BRContainersMonitor _scanForChanges]"
+ "-[BRContainersMonitor init]_block_invoke_2"
+ "-[NSFileProviderDomain(BRAdditions) br_volumeUUIDForDataSeparated:withError:]"
+ "/Library/Caches/com.apple.xbs/E5C5D336-C551-45E0-90AC-AAB4D76356DA/TemporaryDirectory.8UGCcV/Sources/CloudDocs/framework/BRContainer.m"
+ "/Library/Caches/com.apple.xbs/E5C5D336-C551-45E0-90AC-AAB4D76356DA/TemporaryDirectory.8UGCcV/Sources/CloudDocs/framework/BRDeviceToDevice.m"
+ "/Library/Caches/com.apple.xbs/E5C5D336-C551-45E0-90AC-AAB4D76356DA/TemporaryDirectory.8UGCcV/Sources/CloudDocs/framework/CloudDocs.m"
+ "/Library/Caches/com.apple.xbs/E5C5D336-C551-45E0-90AC-AAB4D76356DA/TemporaryDirectory.8UGCcV/Sources/CloudDocs/framework/SpotlightIndex_SoftLinking.m"
+ "/Library/Caches/com.apple.xbs/E5C5D336-C551-45E0-90AC-AAB4D76356DA/TemporaryDirectory.8UGCcV/Sources/CloudDocs/framework/notifs/BRQuery.m"
+ "/Library/Caches/com.apple.xbs/E5C5D336-C551-45E0-90AC-AAB4D76356DA/TemporaryDirectory.8UGCcV/Sources/CloudDocs/framework/operations/BRShareOperations.m"
+ "/System/Library/PrivateFrameworks/SpotlightIndex.framework/SpotlightIndex"
+ "1"
+ "4479.100.79.0.4"
+ "@\"BRDarwinNotifyReceiver\""
+ "@\"NSUserDefaults\""
+ "BRContainerZoneID"
+ "BRGetFPItemIDsForCKRecordIDs"
+ "BRRFAEmailSettingRequest"
+ "BRRFAUserNotificationsRequest"
+ "Can't find _SIActivityDump in SpotlightIndex framework"
+ "Can't find _SIGetLastUsedDate in SpotlightIndex framework"
+ "Can't find _SISetLastUsedDate in SpotlightIndex framework"
+ "Can't open SpotlightIndex"
+ "Error count mismatch. Expected %@ actual %@"
+ "Failed to execute lookup query for daemon container: %s"
+ "Got NULL container path for daemon data container %s"
+ "SpotlightIndexLibrary"
+ "T@\"NSNumber\",&,N,V_zoneRowID"
+ "[CRIT] API MISUSE: removed non existing observer for %@%@"
+ "[CRIT] Can't find _SIActivityDump in SpotlightIndex framework :%s%@"
+ "[CRIT] Can't find _SIGetLastUsedDate in SpotlightIndex framework :%s%@"
+ "[CRIT] Can't find _SISetLastUsedDate in SpotlightIndex framework :%s%@"
+ "[CRIT] UNREACHABLE: -[BRContainer currentStatus] shouldn't be called by the daemon.%@"
+ "[CRIT] UNREACHABLE: -[BRContainer lastServerUpdate] shouldn't be called by the daemon.%@"
+ "[CRIT] UNREACHABLE: No logical name for item%@"
+ "[DEBUG] %@ - Got domain unavailable error. Need to retry again later%@"
+ "[DEBUG] %@ - restart observing the collection. Failure count [%llu], retrying in %llu nano seconds%@"
+ "[DEBUG] %@ is now %s%@"
+ "[DEBUG] Checking the value of rfa email setting%@"
+ "[DEBUG] Container %@ foreground changed (%@ -> %d)%@"
+ "[DEBUG] Failed to consume daemon container sandbox token: (%s)%@"
+ "[DEBUG] Got user container URL %s from containermanagerd%@"
+ "[DEBUG] Notifying that container %@ is now %s%@"
+ "[DEBUG] Received darwin notification about containers fg/bg changes%@"
+ "[DEBUG] Resetting container fg/bg status from user defautls%@"
+ "[DEBUG] container_copy_sandbox_token returned NULL!%@"
+ "[DEBUG] setEmailEnabled called with %d%@"
+ "[DEBUG] ┏%llx Adding observer for %@%@"
+ "[DEBUG] ┏%llx Removing observer for %@%@"
+ "[DEBUG] ┏%llx Scanning for containers fg/bg changes%@"
+ "[WARNING] Can't open SpotlightIndex : %s%@"
+ "_"
+ "_checkChangesForConainerID:"
+ "_darwinNotifyEventPacerDelay"
+ "_defaults"
+ "_fetchSynchronousAutomaticErrorProxyFromURL:serviceName:interface:returnNilIfServiceNotFound:"
+ "_foregroundChangesPacer"
+ "_foregroundChangesReceiver"
+ "_foregroundChangesSender"
+ "_handler"
+ "_namespacePolicy"
+ "_observedContainerIDsToLatestForegroundStatus"
+ "_retryDeltaForError:"
+ "_scanForChanges"
+ "_signalScanning"
+ "_userDefaultsForContainersNotifications"
+ "_userDefaultsSuiteForContainersNotifications"
+ "_userInfo"
+ "backupDatabaseWithURLWrapper:doNotObfuscate:reply:"
+ "boolForKey:"
+ "br_isFileProviderInternalErrorCode:"
+ "br_personaIDWithDefault:"
+ "br_volumeUUIDForDataSeparated:withError:"
+ "brc_errorZoneResetCrashRecovery"
+ "brc_errorZoneResetHierarchyTooDeep"
+ "brc_errorZoneResetOrphanLive"
+ "brc_errorZoneResetOrphanTombstone"
+ "brc_errorZoneResetStillWantsDataUnlinked"
+ "brc_errorZoneResetTesting"
+ "brc_errorZoneResetZoneBecameHealthy"
+ "com.apple.bird.containers.notifications"
+ "com.apple.private.clouddocs.can-get-fpitemid-for-ckrecordid"
+ "com.apple.private.clouddocs.rfa-email-setting"
+ "com.apple.private.clouddocs.rfa-notification-handling"
+ "computePurgeableSpaceWithReply:"
+ "containsValueForKey:"
+ "crash-recovery"
+ "createItemBasedOnTemplate:fields:contents:options:request:additionalItemAttributes:completionHandler:"
+ "deleteItemWithIdentifier:baseVersion:options:request:completionHandler:"
+ "file-write-data"
+ "foreground-changes-pacer"
+ "foreground-changes-queue"
+ "getFPItemIDsForCKRecordIDs:reply:"
+ "handleUserNotificationResponse:completionHandler:"
+ "handleUserNotificationResponse:reply:"
+ "hierarchy-too-deep"
+ "incrementState"
+ "initWithSuiteName:"
+ "internalDaemonContainerPathWithError:"
+ "isAccountCZM:"
+ "isEmailEnabledWithCompletionHandler:"
+ "isRFAEmailSettingEnabledWithReply:"
+ "modifyItem:baseVersion:changedFields:contents:options:request:additionalAttrs:completionHandler:"
+ "namespacePolicy"
+ "notifyContainer:isForegroundState:"
+ "obfuscatedDescription"
+ "orphan.live"
+ "orphan.tombstone"
+ "q24@0:8@16"
+ "reclaimDiskSpaceWithReply:"
+ "removePersistentDomainForName:"
+ "resetNotifications"
+ "retrieveStateAndNotifyWithToken:"
+ "setBool:forKey:"
+ "setEmailEnabled:completionHandler:"
+ "setRFAEmailSettingEnabled:reply:"
+ "setZoneRowID:"
+ "still-wants-data-unlinked"
+ "testing"
+ "v24@0:8@?<v@?@\"NSNumber\"@\"NSNumber\"@\"NSError\">16"
+ "v24@0:8@?<v@?q>16"
+ "v32@0:8@\"UNNotificationResponse\"16@?<v@?@\"NSError\">24"
+ "v36@0:8@\"FPSandboxingURLWrapper\"16B24@?<v@?@\"NSURL\"@\"NSError\">28"
+ "v56@0:8@\"NSString\"16@\"NSFileProviderItemVersion\"24Q32@\"NSFileProviderRequest\"40@?<v@?@\"NSError\">48"
+ "v56@0:8@16@24Q32@40@?48"
+ "v72@0:8@\"<NSFileProviderItem>\"16Q24@\"FPSandboxingURLWrapper\"32Q40@\"NSFileProviderRequest\"48@\"NSDictionary\"56@?<v@?@\"BRQueryItem\"QB@\"NSError\">64"
+ "v72@0:8@16Q24@32Q40@48@56@?64"
+ "v80@0:8@\"<NSFileProviderItem>\"16@\"NSFileProviderItemVersion\"24Q32@\"FPSandboxingURLWrapper\"40Q48@\"NSFileProviderRequest\"56@\"NSDictionary\"64@?<v@?@\"BRQueryItem\"QB@\"NSError\">72"
+ "v80@0:8@16@24Q32@40Q48@56@64@?72"
+ "zone became healthy"
+ "zoneRowID"
- " br-alias"
- " f:'%@'"
- "\"%@\" possibly interesting %ld queries>"
- "(?=\"\"{?=\"downloadStatus\"b2\"uploadStatus\"b2\"itemStatus\"b2\"conflicted\"b1\"preCrashMarker\"b1\"isUploadActive\"b1\"isDownloadActive\"b1\"isDownloadRequested\"b1\"shareOptions\"b3\"isHiddenExtension\"b1\"isBRAlias\"b1\"isTrashed\"b1\"itemMode\"b3\"fromReadOnlyDB\"b1\"isSharedFolderSubItem\"b1\"isSharedToMeOrContainsSharedToMeItem\"b1\"isSharedByMeOrContainsSharedByMeItem\"b1\"editedSinceShared\"b1\"isNetworkOffline\"b1\"isHiddenItem\"b1\"isTopLevel\"b1\"isEvictable\"b1\"fromRelativePath\"b1\"isAppLibraryTrashFolder\"b1\"isAppLibraryRootFolder\"b1\"isAppLibraryDocumentsFolder\"b1\"evadeSpotlightIndexing\"b1\"isContentZoneRoot\"b1\"kind\"C}\"value\"Q)"
- "+[BRContainer(BRInternalAdditions) postContainerStatusChangeNotificationWithID:key:value:]"
- "-[BRContainersMonitor addObserver:forContainerID:]_block_invoke"
- "-[BRItemCollectionGatherer collection:didEncounterError:]_block_invoke"
- "-[BRNotificationReceiver _obtainNotificationSenderFromDaemon]"
- "-[BRNotificationReceiver _obtainNotificationSenderFromDaemon]_block_invoke"
- "-[BRNotificationReceiver _receiveUpdates:]"
- "-[BRNotificationReceiver _signalSourceIfNeeded]"
- "-[BRNotificationReceiver _signalSourceIfNeeded]_block_invoke"
- "-[BRNotificationReceiver _watchUbiquitousScopes:bundleID:predicate:]"
- "-[BRNotificationReceiver _watchUbiquitousScopes:bundleID:predicate:]_block_invoke"
- "-[BRNotificationReceiver dealloc]"
- "-[BRNotificationReceiver init]"
- "-[BRNotificationReceiver invalidateAndNotify:]"
- "-[BRNotificationReceiver networkDidChangeReachabilityStatusTo:]"
- "-[BRNotificationReceiver receiveProgressUpdates:reply:]"
- "-[BRNotificationReceiver receiveUpdates:reply:]"
- "-[BRNotificationReceiver receiveUpdates:reply:]_block_invoke"
- "-[BRNotificationReceiver resume]"
- "-[BRNotificationReceiver suspend]"
- "-[BRQuery _processChanges:]"
- "-[BRQuery _sendHasUpdateNotificationIfNeeded]"
- "-[BRQuery notificationsReceiverDidFinishGathering:]"
- "-[BRQuery notificationsReceiverDidInvalidate:]_block_invoke"
- "-[BRQuery notificationsReceiverDidReceiveNotificationsBatch:]"
- "-[BRQueryItem attachLogicalExtension:physicalExtension:]"
- "-[BRQueryItemProgressObserver _subscribe]_block_invoke"
- "-[BRQueryItemProgressObserver _subscribe]_block_invoke_2"
- "-[BRQueryItemProgressObserver dealloc]"
- "-[BRQueryItemProgressObserver observeValueForKeyPath:ofObject:change:context:]"
- "-[BRQueryItemProgressObserver observeValueForKeyPath:ofObject:change:context:]_block_invoke"
- "-[BRQueryItemProgressObserver start]"
- "-[BRQueryItemProgressObserver stop]"
- "-[BRQueryStitch _creationDone]"
- "-[BRQueryStitch _creationDone]_block_invoke"
- "-[BRQueryStitch _deletionDone]"
- "-[BRQueryStitch _deletionDone]_block_invoke"
- "-[BRQueryStitch _renameDone]"
- "-[BRQueryStitch _renameDone]_block_invoke"
- "-[BRQueryStitch done]"
- "-[BRQueryStitch setQueries:]"
- "-[NSFileProviderDomain(BRAdditions) br_volumeUUID]"
- "/Library/Caches/com.apple.xbs/Sources/CloudDocs/framework/BRContainer.m"
- "/Library/Caches/com.apple.xbs/Sources/CloudDocs/framework/BRDeviceToDevice.m"
- "/Library/Caches/com.apple.xbs/Sources/CloudDocs/framework/CloudDocs.m"
- "/Library/Caches/com.apple.xbs/Sources/CloudDocs/framework/SpotlightIndex_SoftLinking.m"
- "/Library/Caches/com.apple.xbs/Sources/CloudDocs/framework/notifs/BRQuery.m"
- "/Library/Caches/com.apple.xbs/Sources/CloudDocs/framework/operations/BRShareOperations.m"
- "/System/Library/PrivateFrameworks/MobileSpotlightIndex.framework/MobileSpotlightIndex"
- "4257.80.8"
- "<%@:%p %lld \"%@\">"
- "<BRQueryStitch %p for "
- "@\"<BRItemNotificationSending>\""
- "@\"<BRNotificationReceiverDelegate>\""
- "@\"BRNotificationQueue\""
- "@\"BRNotificationReceiver\""
- "@\"BRQuery\""
- "@\"BRQueryItem\""
- "@36@0:8@16@24c32"
- "A"
- "BRNotificationReceiver"
- "BRNotificationReceiverDelegate"
- "BRQueryItemProgressObserver"
- "BRQueryStitch"
- "BRQueryStitchingContext"
- "Can't find _SIActivityDump in MobileSpotlightIndex framework"
- "Can't find _SIGetLastUsedDate in MobileSpotlightIndex framework"
- "Can't find _SISetLastUsedDate in MobileSpotlightIndex framework"
- "Can't open MobileSpotlightIndex"
- "Error count mismatch.  Expected %@ actual %@"
- "MobileSpotlightIndexLibrary"
- "T@\"<BRNotificationReceiverDelegate>\",&,N,V_delegate"
- "T@\"BRNotificationReceiver\",&,V_receiver"
- "T@\"BRQueryItem\",R,N,V_item"
- "T@\"NSArray\",&,N,V_contexts"
- "T@\"NSURL\",&,N,V_fromURL"
- "TQ,N,V_batchingChanges"
- "Td,N,V_batchingDelay"
- "[CRIT] API MISUSE: It's not allowed to call -watchUbiquitousScopes:predicate: twice%@"
- "[CRIT] API MISUSE: removed non existing observer%@"
- "[CRIT] Assertion failed: _contexts == nil%@"
- "[CRIT] Assertion failed: _progress == nil%@"
- "[CRIT] Assertion failed: _progressObserverByID.count == 0%@"
- "[CRIT] Assertion failed: _receiver.delegate == nil%@"
- "[CRIT] Assertion failed: _source%@"
- "[CRIT] Assertion failed: _subscriber == nil%@"
- "[CRIT] Assertion failed: _timer == nil%@"
- "[CRIT] Assertion failed: fractionCompleted <= 1%@"
- "[CRIT] Assertion failed: fractionCompleted >= 0%@"
- "[CRIT] Assertion failed: physicalURL != (__bridge CFURLRef)_url%@"
- "[CRIT] Assertion failed: progress == _progress%@"
- "[CRIT] Assertion failed: receiver == self->_receiver%@"
- "[CRIT] Assertion failed: self->_subscriber == nil%@"
- "[CRIT] Assertion failed: suspendCount >= 0%@"
- "[CRIT] Assertion failed: value != nil%@"
- "[CRIT] Can't find _SIActivityDump in MobileSpotlightIndex framework :%s%@"
- "[CRIT] Can't find _SIGetLastUsedDate in MobileSpotlightIndex framework :%s%@"
- "[CRIT] Can't find _SISetLastUsedDate in MobileSpotlightIndex framework :%s%@"
- "[CRIT] UNREACHABLE: Couldn't adopt persona in NSMDQ but falling back to daemon%@"
- "[CRIT] UNREACHABLE: No logical name for item. Falling back to physical name if it exists %@%@"
- "[CRIT] UNREACHABLE: there should be a physical URL on url: %@%@"
- "[CRIT] UNREACHABLE: unknown stitching handler%@"
- "[CRIT] UNREACHABLE: we should always have a fileObjectID%@"
- "[DEBUG] %@ - No error and no item so seems the itemID %@ got deleted -> recursive delete.%@"
- "[DEBUG] %@ - restart observing the collection. Failure count [%llu]%@"
- "[DEBUG] %@ is now %s for token %d%@"
- "[DEBUG] %@ notify delegate now%@"
- "[DEBUG] %@ notifying delegate in %.3fs%@"
- "[DEBUG] %@: changed to %@%@"
- "[DEBUG] %@: received %@%@"
- "[DEBUG] %@: remove observer from stale progress%@"
- "[DEBUG] %@: remove observer from unpublished progress%@"
- "[DEBUG] %@: resuming (%d->%d)%@"
- "[DEBUG] %@: start on %@%@"
- "[DEBUG] %@: stopping%@"
- "[DEBUG] %@: suspended (%d->%d)%@"
- "[DEBUG] Crash recovery is done%@"
- "[DEBUG] Registered token %d for %@%@"
- "[DEBUG] Restarting the receiver%@"
- "[DEBUG] Using persona ID for NSMDQ %@%@"
- "[DEBUG] broadcasting to framework clients container %@ change %@=%@%@"
- "[DEBUG] could not get notification, not stitching anything%@"
- "[DEBUG] destination URL is outside of clouddocs, pretend it's a deletion%@"
- "[DEBUG] forcing external documents even if not specified%@"
- "[DEBUG] gathering completed%@"
- "[DEBUG] no update to collect%@"
- "[DEBUG] not iCloud Drive items to query%@"
- "[DEBUG] posting has updates notifications%@"
- "[DEBUG] pruning pre-crash only item %@%@"
- "[DEBUG] received %@%@"
- "[DEBUG] sending update to %@: %@%@"
- "[DEBUG] sending updates to %@: %@%@"
- "[DEBUG] setup the query to restart with Crash Marking on%@"
- "[DEBUG] skiping update process as we were invalidated%@"
- "[DEBUG] the URL is still reachable, not stitching anything%@"
- "[DEBUG] the query is stopped, not processing changes%@"
- "[DEBUG] updating items: %@%@"
- "[DEBUG] ┏%llx %@ got error %@%@"
- "[DEBUG] ┏%llx %@ notification timer fired%@"
- "[DEBUG] ┏%llx %@: processing changes %@%@"
- "[DEBUG] ┏%llx adding observer for %@%@"
- "[DEBUG] ┏%llx invalidating notifications from %@%@"
- "[DEBUG] ┏%llx received gathering done for %@%@"
- "[DEBUG] ┏%llx received notifications for %@%@"
- "[DEBUG] ┏%llx received token change notification, reloading%@"
- "[DEBUG] ┏%llx receiving %@%@"
- "[DEBUG] ┏%llx receiving progress updates %@%@"
- "[DEBUG] ┏%llx remote process is gone for %@%@"
- "[DEBUG] ┏%llx stitching for creation of %@%@"
- "[DEBUG] ┏%llx stitching for deletion at %@%@"
- "[DEBUG] ┏%llx stitching for rename from %@ to %@%@"
- "[ERROR] %@ - Couldn't refresh itemID %@ error [%@]%@"
- "[ERROR] cannot pass more than one URL in the scopes%@"
- "[ERROR] cannot query iCloud Drive items: %@%@"
- "[WARNING] Can't open MobileSpotlightIndex : %s%@"
- "[WARNING] The gathering phase for children of '%@' failed: %@%@"
- "[WARNING] The gathering phase for scopes %@ failed: %@%@"
- "[WARNING] This NSMetadataQuery did not watch anything (scopes: %@)%@"
- "[WARNING] can't determine kind of operation (expected: NSString, actual: %@); %@%@"
- "[WARNING] cannot query iCloud Drive items because we are logged out%@"
- "[WARNING] gathering failed: %@%@"
- "_batchingChanges"
- "_batchingDelay"
- "_contexts"
- "_creationDone"
- "_deletionDone"
- "_enableUpdatesFromIPCAfterStitchingOnAllQueries"
- "_fetchSynchronousAutomaticErrorProxyFromURL:serviceName:interface:"
- "_fromURL"
- "_gatherDones"
- "_invalidateAndNotify:"
- "_ipcQueue"
- "_isInvalidated"
- "_isUpload"
- "_item"
- "_itemInTransferByID"
- "_lastBatchTime"
- "_localRepresentationURL"
- "_needsCrashEvicting"
- "_needsCrashMarking"
- "_notifs"
- "_notifyTokenByContainerID"
- "_objid"
- "_observationSetupQueueForDefaultConnection"
- "_obtainNotificationSenderFromDaemon"
- "_physicalName"
- "_processChanges:"
- "_progressObserverByID"
- "_receiveUpdates:"
- "_receivedChanges"
- "_receiver"
- "_renameDone"
- "_sendHasUpdateNotificationIfNeeded"
- "_signalSourceIfNeeded"
- "_source"
- "_stopObserving"
- "_subscribe"
- "_subscriber"
- "_suspendCount"
- "_watchUbiquitousScopes:bundleID:predicate:"
- "addSubscriberForFileURL:usingBlock:"
- "attachLogicalExtension:physicalExtension:"
- "backupDatabaseWithURLWrapper:reply:"
- "batchingChanges"
- "batchingDelay"
- "clouddocs.container.default"
- "com.apple.br.notifs-receiver"
- "com.apple.br.notifs-receiver.ipc"
- "com.apple.clouddocs.file-progresss-registration"
- "computePurgeableSpaceForAllUrgenciesWithReply:"
- "contexts"
- "createItemBasedOnTemplate:fields:contents:options:additionalItemAttributes:completionHandler:"
- "creation of "
- "deleteItemWithIdentifier:baseVersion:options:completionHandler:"
- "deletion of "
- "disableUpdatesFromIPCBeforeStitching"
- "done"
- "dropSpotlightIndexWithReply:"
- "enableUpdatesFromIPCAfterStitching"
- "fault"
- "fetchItemForItemID:completionHandler:"
- "flush"
- "fromRelativePath"
- "fromURL"
- "iCloudDrive"
- "initWithArray:copyItems:"
- "initWithItem:"
- "initWithObjects:"
- "initWithQuery:"
- "initWithURL:objid:kind:"
- "invalidateAndDontNotifyDelegate"
- "invalidateAndNotify:"
- "isPreCrash"
- "item"
- "kMDQueryHasUpdateNotification"
- "modifyItem:baseVersion:changedFields:contents:options:additionalAttrs:completionHandler:"
- "networkDidChangeReachabilityStatusTo:"
- "notificationReceiverDidReceiveNotifications:"
- "notificationsReceiverDidFinishGathering:"
- "notificationsReceiverDidInvalidate:"
- "notificationsReceiverDidReceiveNotificationsBatch:"
- "pendingCount"
- "performAsyncOnReceiver:"
- "physicalName"
- "postContainerStatusChangeNotificationWithID:key:value:"
- "purgeAmount:withUrgency:reply:"
- "receiveStitchingUpdates:"
- "receiver"
- "reclaimAmount:withUrgency:reply:"
- "removeObserver:forKeyPath:context:"
- "rename to "
- "requestForAccess"
- "setBatchingChanges:"
- "setBatchingDelay:"
- "setContexts:"
- "setFromURL:"
- "setIsPreCrash:"
- "setQueries:"
- "setQueue:"
- "setReceiver:"
- "suspend"
- "v16@?0@\"BRQueryItem\"8"
- "v16@?0@\"NSArray\"8"
- "v24@0:8@\"BRNotificationReceiver\"16"
- "v24@0:8@?<v@?@\"NSDictionary\"@\"NSNumber\"@\"NSError\">16"
- "v24@0:8d16"
- "v32@0:8@\"FPSandboxingURLWrapper\"16@?<v@?@\"NSURL\"@\"NSError\">24"
- "v32@?0@\"<BRItemNotificationSending><NSXPCProxyCreating>\"8@\"NSDictionary\"16@\"NSError\"24"
- "v32@?0@\"BRNotificationReceiver\"8@\"NSArray\"16@\"NSDictionary\"24"
- "v32@?0@\"NSString\"8@\"NSDictionary\"16^B24"
- "v36@0:8q16i24@?28"
- "v36@0:8q16i24@?<v@?q>28"
- "v40@0:8@16@24@32"
- "v48@0:8@\"NSString\"16@\"NSFileProviderItemVersion\"24Q32@?<v@?@\"NSError\">40"
- "v48@0:8@16@24Q32@?40"
- "v64@0:8@\"<NSFileProviderItem>\"16Q24@\"FPSandboxingURLWrapper\"32Q40@\"NSDictionary\"48@?<v@?@\"BRQueryItem\"Q@\"NSError\">56"
- "v64@0:8@16Q24@32Q40@48@?56"
- "v72@0:8@\"<NSFileProviderItem>\"16@\"NSFileProviderItemVersion\"24Q32@\"FPSandboxingURLWrapper\"40Q48@\"NSDictionary\"56@?<v@?@\"BRQueryItem\"Q@\"NSError\">64"
- "v72@0:8@16@24Q32@40Q48@56@?64"
- "watchItemAtURL:options:gatherReply:"
- "watchUbiquitousScopes:bundleID:predicate:"

```
