## AirPlaySender

> `/System/Library/PrivateFrameworks/AirPlaySender.framework/Versions/A/AirPlaySender`

```diff

-980.77.5.3.0
-  __TEXT.__text: 0x1d5f6c
-  __TEXT.__objc_methlist: 0x92c
-  __TEXT.__const: 0xd580
-  __TEXT.__gcc_except_tab: 0x62c
-  __TEXT.__cstring: 0x70df9
+1005.13.1.0.0
+  __TEXT.__text: 0x1d992c
+  __TEXT.__objc_methlist: 0x95c
+  __TEXT.__const: 0xd530
+  __TEXT.__gcc_except_tab: 0x64c
+  __TEXT.__cstring: 0x71e4c
   __TEXT.__dlopen_cstrs: 0x164
   __TEXT.__oslogstring: 0xb55
-  __TEXT.__unwind_info: 0x44c8
+  __TEXT.__unwind_info: 0x4598
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4318
+  __DATA_CONST.__const: 0x4388
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb08
+  __DATA_CONST.__objc_selrefs: 0xb58
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x170
-  __DATA_CONST.__got: 0x1de0
-  __AUTH_CONST.__const: 0x7200
-  __AUTH_CONST.__cfstring: 0x10540
+  __DATA_CONST.__got: 0x1e08
+  __AUTH_CONST.__const: 0x72b0
+  __AUTH_CONST.__cfstring: 0x10660
   __AUTH_CONST.__objc_const: 0xc58
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0x1b8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9057
-  Symbols:   8797
-  CStrings:  9188
+  Functions: 9112
+  Symbols:   8863
+  CStrings:  9269
 
Symbols:
+ -[CUPairingManager(APPairingClientCoreUtils) allPairedPeers]
+ -[CUPairingManager(APPairingClientCoreUtils) migrateUngroupedPeer:groupID:]
+ -[CUPairingManager(APPairingClientCoreUtils) migrateUngroupedPeersForGroup:peers:]
+ -[CUPairingManager(APPairingClientCoreUtils) removePairedPeer:]
+ APEndpointCreateDecoratedName
+ GCC_except_table130
+ GCC_except_table33
+ GCC_except_table37
+ GCC_except_table39
+ GCC_except_table41
+ _APEndpointCopyAudioOutputLatencyMsForStream
+ _APEndpointPayloadRequiresCompositionRefresh
+ _APPairingClientCoreUtilsCopyMigratableUngroupedPeers
+ _APPairingClientCoreUtilsCreateOrphanedPeersFromGroupInfo
+ _APPairingClientCoreUtilsPatchUnpairedPeerWithGroupID
+ _APSAudioHoseMetricCollectorSetSenderRTMetrics
+ _APSCMTimeMakeWithRTPTimestamp
+ _APSGetSurroundRoleFromClusterMemberID
+ _APSIsHomeAccessory
+ _APSIsHomeTheaterSurroundEnabled
+ _APSIsUpdateInfoForwardingEnabled
+ _APSenderSessionGetFallbackToInfraReasonForUnselectedTransport
+ _APTDiagnosticSendStreamInfo
+ _APTNANDataSessionGetDatapathRSSI
+ _APTransportConnectionQoSFromSocketQoS
+ _APTransportDeviceForwardAirPlayInfoToBrowser
+ _FigCFNumberGetCFIndex
+ _FigCFSetGetCount
+ _FigEndpointSetProperty
+ _MGGetBoolAnswer
+ _OBJC_CLASS_$_CUSystemMonitor
+ __60-[CUPairingManager(APPairingClientCoreUtils) allPairedPeers]_block_invoke
+ __63-[CUPairingManager(APPairingClientCoreUtils) removePairedPeer:]_block_invoke
+ __APPairingClientCoreUtilsCreateOrphanedPeersFromGroupInfo_block_invoke
+ ___60-[CUPairingManager(APPairingClientCoreUtils) allPairedPeers]_block_invoke
+ ___63-[CUPairingManager(APPairingClientCoreUtils) removePairedPeer:]_block_invoke
+ ___APPairingClientCoreUtilsCreateOrphanedPeersFromGroupInfo_block_invoke
+ ___block_descriptor_40_e8_32o_e15_v24?0r^v8r^v16l
+ ___block_descriptor_48_e8_32o40o_e29_v32?0"CUPairedPeer"8Q16^B24l
+ ___block_descriptor_48_e8_32o40r_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_56_e15_v24?0r^v8r^v16l
+ ___copy_helper_block_8_32b40r48r56r
+ ___coreUtilsPairing_updatePairingGroupInfoIfNeeded_block_invoke_2
+ ___destroy_helper_block_8_32b40r48r56r
+ ___endpointCluster_reconcileResponsiveAudioTransports_block_invoke
+ ___endpoint_performRemoteTeardown_block_invoke
+ ___endpoint_performRemoteTeardown_block_invoke_2
+ ___endpoint_performRemoteTeardown_block_invoke_3
+ ___endpoint_startPowerSourceMonitorIfNeeded_block_invoke
+ ___endpoint_startPowerSourceMonitorIfNeeded_block_invoke_2
+ ___endpoint_startPowerSourceMonitorIfNeeded_block_invoke_3
+ __coreUtilsPairing_updatePairingGroupInfoIfNeeded_block_invoke_2
+ _airPlayDescription_isAppleHomeAccessory
+ _bufferedAudioEngine_isHoseClusterBuddy
+ _emp_demoteEndpoint
+ _endpointAggregate_handleAudioStreamResumed
+ _endpointCluster_activateSubEndpointForcingTransportIfNeeded
+ _endpointCluster_copyActivatedSubEndpointsByTransportType
+ _endpointCluster_copyActivationOptionsForcingTransportType
+ _endpointCluster_copyForcedTransportForResponsiveAudio
+ _endpointCluster_failureCountForSubEndpoint
+ _endpoint_forwardUpdateInfo
+ _endpoint_handleAudioStreamResumed
+ _endpoint_startPowerSourceMonitorIfNeeded
+ _endpoint_stopPowerSourceMonitor
+ _endpoint_updateInactivityTimer
+ _kAPEndpointAggregateCreationOptionKey_ClusterType
+ _kAPEndpointDescriptionProperty_SurroundRole
+ _kAPEndpointProperty_AudioOutputLatencyMs
+ _kAPEndpointProperty_SurroundRole
+ _kAPEndpointStreamBufferedAudioEngineCreationOption_ForceFirstRemoteMediaTime
+ _kAPEndpointStreamConnectionKey_QoS
+ _kAPSDynamicLatencyManagerVariantIdentifier_B525
+ _kAPSEndpointStreamAudioHoseRegistrarRegistrationOption_SurroundRole
+ _kFigEndpointActivateOptionKey_ForcedTransportType
+ _kFigEndpointForcedTransportType_Infra
+ _kFigEndpointSubType_HomeAccessory
+ _objc_msgSend$UUIDString
+ _objc_msgSend$getPairedPeersWithOptions:completion:
+ _objc_msgSend$migrateUngroupedPeer:groupID:
+ _objc_msgSend$powerUnlimited
+ _objc_msgSend$removePairedPeer:
+ _objc_msgSend$removePairedPeer:options:completion:
+ _objc_msgSend$setInvalidationHandler:
+ _objc_msgSend$setPowerUnlimitedChangedHandler:
+ _sessionfactory_RemoveAirPlaySession
+ _sessionfactory_RemoveSessionClient
+ emp_demoteEndpoint
+ endpointCluster_copyActivatedSubEndpointsByTransportType
+ endpointCluster_copyActivationOptionsForcingTransportType
+ endpointCluster_failDelayMSecsForFailureCount.kFailDelayLadderPercent
+ endpoint_shouldUseInactivityTimer
+ sessionfactory_RemoveAirPlaySession
+ sessionfactory_RemoveSessionClient
- GCC_except_table26
- _APTDiagnosticMulticastDataToAllHosts
- _GestaltGetBoolean
- _OUTLINED_FUNCTION_266
- _OUTLINED_FUNCTION_267
- _OUTLINED_FUNCTION_268
- _OUTLINED_FUNCTION_269
- _OUTLINED_FUNCTION_270
- _OUTLINED_FUNCTION_271
- _OUTLINED_FUNCTION_272
- _OUTLINED_FUNCTION_273
- _OUTLINED_FUNCTION_274
- _OUTLINED_FUNCTION_275
- _OUTLINED_FUNCTION_276
- _OUTLINED_FUNCTION_277
- ___block_descriptor_48_e15_v24?0r^v8r^v16l
- ___copy_helper_block_8_32b40r48r
- ___destroy_helper_block_8_32b40r48r
- ___endpoint_prepareLocalTeardown_block_invoke
- ___endpoint_prepareLocalTeardown_block_invoke_2
- ___endpoint_prepareLocalTeardown_block_invoke_3
- ___epp_EnsureAuthorizedWithCompletionCallback_block_invoke_2
- __coreUtilsPairing_updatePairingGroupInfoIfNeeded_block_invoke
- _apsession_getNANRSSI
- _bufferedAudioEngine_isHoseInStereoPair
- _endpointCluster_getNumSubEndpointsActivated
- _endpoint_startInactivityTimer
- epp_EnsureAuthorizedWithCompletionCallback
CStrings:
+ "\t[indexed] identifier: %@ infoKeys: %@\n"
+ "\t[ungrouped] identifier: %@  publicKey: %@\n"
+ "%@ms"
+ "-[CUPairingManager(APPairingClientCoreUtils) allPairedPeers]"
+ "-[CUPairingManager(APPairingClientCoreUtils) allPairedPeers]_block_invoke"
+ "-[CUPairingManager(APPairingClientCoreUtils) migrateUngroupedPeer:groupID:]"
+ "-[CUPairingManager(APPairingClientCoreUtils) migrateUngroupedPeersForGroup:peers:]"
+ "-[CUPairingManager(APPairingClientCoreUtils) removePairedPeer:]"
+ "-[CUPairingManager(APPairingClientCoreUtils) removePairedPeer:]_block_invoke"
+ "1005.13.1"
+ "<ProactiveNANPairing> [%{ptr}] Feature disabled from prefs"
+ "APEndpointCreateDecoratedName"
+ "APEndpointInactivityTimeoutType endpoint_determineInactivityTimeoutBehavior(FigEndpointRef, FigEndpointFeatures, CFDictionaryRef)"
+ "APPairingClientCoreUtilsPatchUnpairedPeerWithGroupID"
+ "AudioAccessory11"
+ "AudioOutputLatencyMs"
+ "BAE [%{ptr}] %s(startup) maxWaitPhaseTwoClusterBuddyMs set to %d (%lld ticks)\n"
+ "BAE [%{ptr}] %s(test) Forcing firstRemoteMediaTime to %1.6f (%lld/%d)\n"
+ "BAE [%{ptr}] %s[0x%04X] (startup) Cluster Member hose [%{ptr}] (%@) Primed -> Ready %s (clusterUUID %@)\n"
+ "Eligible for fast reactivate"
+ "Failed to get all paired peers: %#m\n"
+ "Failed to patch ungrouped peer %@ for migration\n"
+ "Failed to remove paired peer [%{ptr}]: %#m\n"
+ "Failed to save migrated peer %@ — migration skipped: %#m\n"
+ "Getting all paired peers\n"
+ "Got %d paired peers\n"
+ "HomeAccessory"
+ "Local HT first loss"
+ "Migrated ungrouped peer %@ to group-indexed entry\n"
+ "Never"
+ "NoIdleTimeout activation option"
+ "OSStatus bufferedAudioEngine_createLatencyManagerEndpointOptions(FigEndpointStreamAudioEngineRef, APSAudioProtocolDriverHoseControlRef, APSSurroundRole, CFDictionaryRef *)"
+ "OSStatus endpointCluster_activateSubEndpointForcingTransportIfNeeded(FigEndpointRef, FigEndpointRef)"
+ "OSStatus epp_Dissociate(FigEndpointRef)_block_invoke"
+ "OSStatus sessionfactory_RemoveAirPlaySession(APSenderSessionFactoryRef, CFStringRef)"
+ "P2POnly"
+ "P2POnlyOnBattery"
+ "Removed paired peer [%{ptr}]: %@\n"
+ "Removing paired peer [%{ptr}]: %@\n"
+ "Scheduling kFigEndpointManagerNotification_AvailableEndpointsChanged in %lld ns with %llu ns leeway\n"
+ "SurroundRole"
+ "[%{ptr}] %@ is%s recommended%?{end} with err=%#m"
+ "[%{ptr}] Activation callback %@ for [%{ptr}]"
+ "[%{ptr}] Authorization request callback %@ for [%{ptr}] result %#m"
+ "[%{ptr}] COLLISION %@ clusterPlus [%{ptr}] subEndpointPlus [%{ptr}] has inner [%{ptr}] but found real [%{ptr}]"
+ "[%{ptr}] COLLISION %@ plus [%{ptr}] has inner [%{ptr}] but found real [%{ptr}]"
+ "[%{ptr}] Completion callback %@ for [%{ptr}]"
+ "[%{ptr}] Dissociating inner [%{ptr}]"
+ "[%{ptr}] Duplicate activate in stage %d; keeping current activation\n"
+ "[%{ptr}] Ensure Authorized with inner [%{ptr}] proxyID %@"
+ "[%{ptr}] Fail delay timer already running, discarding requested delay of %llu ms for subEndpoint [%{ptr}]%?{end}, failure count %ld"
+ "[%{ptr}] Failed to remove session for deviceID %@: %#m\n"
+ "[%{ptr}] Forcing %@ transport for activating subEndpoint [%{ptr}]"
+ "[%{ptr}] Ignoring subEndpoint [%{ptr}] failure, cluster is deactivated"
+ "[%{ptr}] Immediately triggering lost cluster buddy reconnect logic for [%{ptr}] (session state: %s, reason: %s)"
+ "[%{ptr}] Inactivity timeout type: %s%?{end} (%s)\n"
+ "[%{ptr}] Monitoring power source for inactivity timer\n"
+ "[%{ptr}] NAN RSSI sample failed: %#m\n"
+ "[%{ptr}] Power source changed: now on %s power\n"
+ "[%{ptr}] Power source monitor creation fail"
+ "[%{ptr}] RA Reconcile: Migrating subEndpoint [%{ptr}] from NAN to Infra"
+ "[%{ptr}] RA Reconcile: Reactivate subEndpoint [%{ptr}] error: %m"
+ "[%{ptr}] RA Reconcile: all subEndpoints already using %@"
+ "[%{ptr}] Removing orphaned pairing group peer [%{ptr}] with identifier %@\n"
+ "[%{ptr}] Removing session client for %@ endpoint [%{ptr}] due to failure in upgrade session path.\n"
+ "[%{ptr}] Removing session for %@ due to failure in new session path.\n"
+ "[%{ptr}] Send Command callback %@ for [%{ptr}] forward? %s"
+ "[%{ptr}] Set up %@ stream and useRealtimeAPAT=%s (localDeviceType=%d receiverSupportsRealtimeAPAT=%s isScreenMirroringUsage=%s engineType=%@"
+ "[%{ptr}] Starting fail delay timer for seed %llu, subEndpoint [%{ptr}], with delay of %llu ms%?{end}, failure count %ld"
+ "[%{ptr}] Stopped monitoring power source\n"
+ "[%{ptr}] SubEndpointStream(%{ptr}) is dissociated, excluding it from aggregate capabilities"
+ "[%{ptr}] Using inactivity timeout? %s%?{end} (type: %s)\n"
+ "[%{ptr}] audio output latency: %@ms\n"
+ "aggregateClusterType"
+ "battery"
+ "because peer was primed or better"
+ "bufferedAudioEngine_isHoseClusterBuddy"
+ "com.apple.private.restrict-post.AirPlay.DACP.mutetoggle"
+ "com.apple.private.restrict-post.AirPlay.DACP.volumedown"
+ "com.apple.private.restrict-post.AirPlay.DACP.volumeup"
+ "due to timeout"
+ "endpointCluster_copyActivatedSubEndpointsByTransportType"
+ "endpointCluster_copyActivationOptionsForcingTransportType"
+ "endpointCluster_reconcileResponsiveAudioTransports"
+ "endpointCluster_reconcileResponsiveAudioTransports_block_invoke"
+ "endpoint_forwardUpdateInfo"
+ "endpoint_shouldUseInactivityTimer"
+ "forceFirstRemoteMediaTime"
+ "group info member count: %lu\n"
+ "group-indexed peers: %lu\n"
+ "maxWaitPhaseTwoClusterBuddyMs"
+ "not responsive audio"
+ "responsive audio, portable Mac"
+ "responsive audio, stationary Mac"
+ "senderClusterType"
+ "sessionfactory_RemoveAirPlaySession"
+ "streamConnectionKeyQoS"
+ "ungrouped peers to migrate: %lu\n"
+ "void bufferedAudioEngine_updateHosesPrimed(FigEndpointStreamAudioEngineRef, uint64_t, uint64_t, Boolean, APAudioEngineBufferedPrimingStats *)"
+ "void coreUtilsPairing_updatePairingGroupInfoIfNeeded(APPairingClientRef, CFDictionaryRef, CUPairedPeer *)_block_invoke_2"
+ "void endpointAggregate_handleAudioStreamResumed(CMNotificationCenterRef, const void *, CFStringRef, const void *, CFTypeRef)"
+ "void endpointCluster_CallActivationCompletionCallback(FigEndpointRef, uint64_t, FigEndpointFeatures, OSStatus, FigEndpointActivationCompletionCallback, void *)"
+ "void endpointCluster_reconcileResponsiveAudioTransports(FigEndpointRef, CFDictionaryRef *)"
+ "void endpointCluster_reconcileResponsiveAudioTransports(FigEndpointRef, CFDictionaryRef *)_block_invoke"
+ "void endpointCluster_startFailDelayTimerIfNeeded(FigEndpointRef, FigEndpointRef)"
+ "void endpoint_handleAudioStreamResumed(CMNotificationCenterRef, const void *, CFStringRef, const void *, CFTypeRef)"
+ "void endpoint_handlePowerSourceChanged(FigEndpointRef)"
+ "void endpoint_performRemoteTeardown(void *)_block_invoke"
+ "void endpoint_startPowerSourceMonitorIfNeeded(FigEndpointRef)"
+ "void endpoint_stopPowerSourceMonitor(FigEndpointRef)"
+ "void endpoint_updateInactivityTimer(FigEndpointRef, Boolean)"
+ "wall"
- "980.77.5.3"
- "BAE [%{ptr}] %s[0x%04X] (startup) Stereo Pair Hoses [%{ptr}] (%@) Primed -> Ready due to timeout\n"
- "BAE [%{ptr}] %s[0x%04X] (startup) Stereo Pair hose (peer) [%{ptr}] (%@) Primed -> Ready because peer was primed or better\n"
- "BAE [%{ptr}] %s[0x%04X] (startup) Stereo Pair hose [%{ptr}] (%@) Primed -> Ready because peer was primed or better\n"
- "OSStatus bufferedAudioEngine_createLatencyManagerEndpointOptions(FigEndpointStreamAudioEngineRef, APSAudioProtocolDriverHoseControlRef, CFDictionaryRef *)"
- "Scheduling kFigEndpointManagerNotification_AvailableEndpointsChanged in %lld ns\n"
- "Terminus_MeshRegistration"
- "[%{ptr}] %@ is%s recommended?{end} with err=%#m"
- "[%{ptr}] Activate SubEndpoint [%{ptr}] on reconcile transports failed %m"
- "[%{ptr}] Activation callback with inner [%{ptr}] context %@ forward? %s"
- "[%{ptr}] Authorization request completion callback for inner %s [%{ptr}] result %#m"
- "[%{ptr}] Completion callback with inner [%{ptr}] context %@ forward? %s"
- "[%{ptr}] Dissociating"
- "[%{ptr}] Ensure Authorized with inner [%{ptr}] context %@"
- "[%{ptr}] Immediately triggering lost cluster buddy reconnect logic for [%{ptr}] during startup\n"
- "[%{ptr}] RA stereo pair transport mismatch detected, [%{ptr}] on %@, [%{ptr}] on %@, forcing [%{ptr}] to Infra"
- "[%{ptr}] RA stereo pair, no transport mismatch [%{ptr}] on %@, [%{ptr}] on %@"
- "[%{ptr}] Send Command callback with inner [%{ptr}] context %@ forward? %s"
- "[%{ptr}] Set up %@ stream and useRealtimeAPAT=%s (localDeviceType=%d receiverSupportsRealtimeAPAT=%s isScreenMirroringUsage=%s"
- "[%{ptr}] Starting fail delay timer for seed %llu with delay of %llu seconds.\n"
- "[%{ptr}] Using inactivity timeout? %d\n"
- "bufferedAudioEngine_isHoseInStereoPair"
- "com.apple.AirTunes.DACP.mutetoggle"
- "com.apple.AirTunes.DACP.volumedown"
- "com.apple.AirTunes.DACP.volumeup"
- "endpointCluster_reconcileSubEndpointTransportsIfNeeded"
- "void bufferedAudioEngine_updateHosesPrimed(FigEndpointStreamAudioEngineRef, uint64_t, Boolean, APAudioEngineBufferedPrimingStats *)"
- "void endpointCluster_reconcileSubEndpointTransportsIfNeeded(FigEndpointRef, FigEndpointRef)"
- "void endpointCluster_startFailDelayTimerIfNeeded(FigEndpointRef)"
- "void endpoint_prepareLocalTeardown(APEndpointDeactivationContext *)_block_invoke"
- "void endpoint_startInactivityTimer(FigEndpointRef)"
```
