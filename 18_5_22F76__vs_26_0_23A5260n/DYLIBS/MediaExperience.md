## MediaExperience

> `/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience`

```diff

-240.6.1.0.0
-  __TEXT.__text: 0x1c2c08
-  __TEXT.__auth_stubs: 0x1f40
-  __TEXT.__objc_methlist: 0x4d5c
-  __TEXT.__cstring: 0x2a246
-  __TEXT.__const: 0x1af8
-  __TEXT.__gcc_except_tab: 0x1f98
-  __TEXT.__oslogstring: 0x3535e
+270.59.4.11.2
+  __TEXT.__text: 0x2a50cc
+  __TEXT.__auth_stubs: 0x1fb0
+  __TEXT.__delay_helper: 0xc8
+  __TEXT.__objc_methlist: 0x5c3c
+  __TEXT.__cstring: 0x4102e
+  __TEXT.__const: 0x1b58
+  __TEXT.__gcc_except_tab: 0x2cd0
+  __TEXT.__oslogstring: 0x63be1
   __TEXT.__dlopen_cstrs: 0x5bd
-  __TEXT.__unwind_info: 0x4468
-  __TEXT.__objc_classname: 0x506
-  __TEXT.__objc_methname: 0x12a21
-  __TEXT.__objc_methtype: 0x1c8b
-  __TEXT.__objc_stubs: 0xb6c0
-  __DATA_CONST.__got: 0xa18
-  __DATA_CONST.__const: 0x6408
-  __DATA_CONST.__objc_classlist: 0x168
+  __TEXT.__unwind_info: 0x4ac8
+  __TEXT.__objc_classname: 0x763
+  __TEXT.__objc_methname: 0x150fc
+  __TEXT.__objc_methtype: 0x20f3
+  __TEXT.__objc_stubs: 0xcfa0
+  __DATA_CONST.__got: 0xa78
+  __DATA_CONST.__const: 0x65e8
+  __DATA_CONST.__objc_classlist: 0x1f0
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x30
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3378
-  __DATA_CONST.__objc_superrefs: 0x150
-  __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0xfb8
-  __AUTH_CONST.__const: 0x3b58
-  __AUTH_CONST.__cfstring: 0x17800
-  __AUTH_CONST.__objc_const: 0x74f8
-  __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__objc_intobj: 0x78
+  __DATA_CONST.__objc_selrefs: 0x3a28
+  __DATA_CONST.__objc_superrefs: 0x1d8
+  __DATA_CONST.__objc_arraydata: 0x60
+  __AUTH_CONST.__auth_got: 0xff0
+  __AUTH_CONST.__const: 0x3da0
+  __AUTH_CONST.__cfstring: 0x188c0
+  __AUTH_CONST.__objc_const: 0x8888
+  __AUTH_CONST.__objc_arrayobj: 0x48
+  __AUTH_CONST.__objc_intobj: 0x1b0
+  __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x500
-  __AUTH.__data: 0x510
-  __DATA.__objc_ivar: 0x758
-  __DATA.__data: 0xf2c
-  __DATA.__bss: 0x15d8
-  __DATA.__common: 0x500
-  __DATA_DIRTY.__objc_data: 0x910
-  __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x4e8
-  __DATA_DIRTY.__common: 0x60
+  __AUTH.__objc_data: 0xa00
+  __AUTH.__data: 0x570
+  __DATA.__objc_ivar: 0x834
+  __DATA.__data: 0xfe0
+  __DATA.__bss: 0x1891
+  __DATA.__common: 0x558
+  __DATA_DIRTY.__objc_data: 0x960
+  __DATA_DIRTY.__bss: 0x420
+  __DATA_DIRTY.__common: 0x90
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
+  - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices
   - /System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore
   - /System/Library/PrivateFrameworks/CPMS.framework/CPMS
+  - /System/Library/PrivateFrameworks/CarKit.framework/CarKit
+  - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
+  - /System/Library/PrivateFrameworks/MXUIServiceClient.framework/MXUIServiceClient
+  - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 15F78A5A-FA94-3F0C-BB4A-0E3E26E38AB3
-  Functions: 5917
-  Symbols:   19776
-  CStrings:  13161
+  UUID: 34FA2FDC-D241-3E34-9A9C-8D57D922E367
+  Functions: 7368
+  Symbols:   23052
+  CStrings:  18272
 
Symbols:
+ +[AVSystemControllerCommon initialize]
+ +[AVSystemControllerCommon postNotificationOnMainQueue:notification:object:]
+ +[MXAudioAccessoryServices isSupported]
+ +[MXAudioAccessoryServices sharedInstance]
+ +[MXAudioAccessoryServices sharedInstance].cold.1
+ +[MXEndpointDescriptorCache getConnectBannerResponseCache]
+ +[MXEndpointDescriptorCache getConnectBannerResponseCache].cold.1
+ +[MXFrontBoardServices sharedInstance]
+ +[MXFrontBoardServices sharedInstance].cold.1
+ +[MXInitialization AirPlayStartServicesInMXProcess]
+ +[MXInitialization LoadAirPlaySenderFramework]
+ +[MXInitialization LoadAirPlaySenderFramework].cold.1
+ +[MXSession(InternalUse) getAudioTrackStatusAsString:]
+ +[MXSession(InternalUse) updateAudioTrackStatus:]
+ +[MXSessionIndependentInputAudioResource getSetPropertiesOrder]
+ +[MXSessionIndependentInputAudioResource initialize]
+ +[MXSessionIndependentInputAudioResource isNonSerializedCopyProperty:]
+ +[MXSessionIndependentInputAudioResource isNonSerializedSetProperty:]
+ +[MXSessionIndependentInputAudioResource isNonSerializedSetPropertyWhenSessionIsInactive:]
+ +[MXSessionManagerBase copyAllMXCoreSessionList]
+ +[MXSessionManagerBase copySessionWithAudioObjectID:]
+ +[MXSessionManagerBase copySessionWithAudioSessionID:]
+ +[MXSessionManagerBase copySessionWithMXCoreSessionID:]
+ +[MXSessionManagerBase copySessionsShadowingAudioSessionID:withShadowingOptions:fromSessionList:]
+ +[MXSessionManagerBase postInterruptionCommandForAudioSessionID:sessionID:interruptiondCmd:interruptionInfo:]
+ +[MXSessionManagerBase setGreenTeaLoggerRecordingState:state:]
+ +[MXSessionManagerBase setGreenTeaLoggerRecordingState:state:].cold.1
+ +[MXSessionManagerIndependentAudioResource sharedInstance]
+ +[MXSessionManagerIndependentAudioResource sharedInstance].cold.1
+ +[MXSystemController allowBluetoothAccessoryToRequestAudioRoute]
+ +[MXSystemController preferHeadphonesOverCarsAndSpeakersEnabled]
+ +[MXSystemController setPreferHeadphonesOverCarsAndSpeakersEnabled:]
+ +[MXSystemController(Common) copyMXSystemControllerList:]
+ +[MXSystemSoundServices sharedInstance]
+ +[MXSystemSoundServices sharedInstance].cold.1
+ +[MXUserPreferredInputRouteCache sharedInstance]
+ +[MXUserPreferredInputRouteCache sharedInstance].cold.1
+ +[MX_BannerManager bannerResponseToString:]
+ +[MX_BannerManager getAwaitingDispatchQueue]
+ +[MX_BannerManager getAwaitingDispatchQueue].cold.1
+ +[MX_BannerManager getSharedBannerClient]
+ +[MX_BannerManager getSharedBannerClient].cold.1
+ +[MX_BannerManager sharedInstance]
+ +[MX_BannerManager sharedInstance].cold.1
+ -[AVSystemController copyAttributeForKeyMappingToFig]
+ -[AVSystemController copySetAttributeForKeyMappingToFig]
+ -[AVSystemController getAudioSessionID:forAttributedPID:]
+ -[AVSystemController releaseSharedInstance]
+ -[AVSystemControllerCommon .cxx_destruct]
+ -[AVSystemControllerCommon attributeForKey:]
+ -[AVSystemControllerCommon copyAttributeForKeyMappingToFig]
+ -[AVSystemControllerCommon copyFigController]
+ -[AVSystemControllerCommon copySetAttributeForKeyMappingToFig]
+ -[AVSystemControllerCommon dealloc]
+ -[AVSystemControllerCommon init]
+ -[AVSystemControllerCommon initializeAttributeForKeyMappingToFig]
+ -[AVSystemControllerCommon releaseSharedInstance]
+ -[AVSystemControllerCommon selfWeak]
+ -[AVSystemControllerCommon setAttribute:forKey:error:]
+ -[AVSystemControllerCommon setSelfWeak:]
+ -[FigRemoteRoutingContextFactory copySystemAudioInputContextWithAllocator:options:context:]
+ -[FigResilientRemoteRoutingContextFactory copySystemAudioInputContextWithAllocator:options:context:]
+ -[MXAdditiveRoutingManager copyVADNamesFromSessionAudioBehavior]
+ -[MXAdditiveRoutingManager discardUnavailableVADInfoFromDetailedRouteDescriptionIfNeeded:]
+ -[MXAdditiveRoutingManager populateVirtualAudioDeviceInfoFromSessionAudioBehaviors:newVADIDToNameMap:]
+ -[MXAudioAccessoryServices clearDevicesStateCache]
+ -[MXAudioAccessoryServices copyDeviceAddressFromVADPort:]
+ -[MXAudioAccessoryServices copyHighestPriorityLocalSession]
+ -[MXAudioAccessoryServices copyPreferredDeviceAddress:andPreemptivePortInfo:]
+ -[MXAudioAccessoryServices copyPreferredDeviceAddress:bundleID:isHypotheticalQuery:reason:]
+ -[MXAudioAccessoryServices dealloc]
+ -[MXAudioAccessoryServices dumpDebugInfo]
+ -[MXAudioAccessoryServices finalizeAudioAccessoryConnection]
+ -[MXAudioAccessoryServices handleBTNotificationAudioRoutingChange]
+ -[MXAudioAccessoryServices handleNewWirelessPortConnected:]
+ -[MXAudioAccessoryServices handlePortDisconnected:]
+ -[MXAudioAccessoryServices handleServerDeath]
+ -[MXAudioAccessoryServices hijackWirelessPort:reason:portWentInEar:]
+ -[MXAudioAccessoryServices init]
+ -[MXAudioAccessoryServices initializeAudioAccessoryConnection]
+ -[MXAudioAccessoryServices isAnyManagedDeviceConnected]
+ -[MXAudioAccessoryServices isPortManaged:]
+ -[MXAudioAccessoryServices routeToBTDeviceIfNeeded:]
+ -[MXAudioAccessoryServices sendAudioRoutingRequestToDevice:appBundleID:audioScore:flags:reason:responseHandler:]
+ -[MXAudioAccessoryServices updateDeviceManagementState:reason:]
+ -[MXConnectBannerResponseInfo connectBannerResponse]
+ -[MXConnectBannerResponseInfo dealloc]
+ -[MXConnectBannerResponseInfo init]
+ -[MXConnectBannerResponseInfo routeSemaphore]
+ -[MXConnectBannerResponseInfo setConnectBannerResponse:]
+ -[MXConnectBannerResponseInfo setRouteSemaphore:]
+ -[MXConnectBannerResponseInfo setTxid:]
+ -[MXConnectBannerResponseInfo txid]
+ -[MXCoreSession .cxx_destruct]
+ -[MXCoreSession additiveRoutingInfo]
+ -[MXCoreSession doesSessionConfigurationChangeRequireOutputUnmute:oldAudioMode:]
+ -[MXCoreSession hasAudioTrack]
+ -[MXCoreSession isEligibleForOutputMuting]
+ -[MXCoreSession isMediaSession]
+ -[MXCoreSession isOutputMuted]
+ -[MXCoreSession prefersBluetoothHighQualityContentCapture]
+ -[MXCoreSession reapplyDeviceSampleRateAndBufferSizeOnVADIfNeeded]
+ -[MXCoreSession requiresExclaveSensor]
+ -[MXCoreSession sendSessionConfigurationInfoToVA]
+ -[MXCoreSession setIsOutputMuted:]
+ -[MXCoreSession setPrefersBluetoothHighQualityContentCapture:]
+ -[MXCoreSession shouldSendSessionConfigurationInfoToVA]
+ -[MXCoreSession(Utilities) copyPreferredAvailableInputPortFromCache]
+ -[MXCoreSession(Utilities) copyPreferredInputPortFromConnectedPorts:]
+ -[MXCoreSession(Utilities) copyUserPreferredInputPort]
+ -[MXCoreSession(Utilities) userPreferredInputPortIsBluetoothManagedAndHighQuality]
+ -[MXCoreSessionBase addSessionAudioObject]
+ -[MXCoreSessionBase allowsBluetoothRecordingCustomization]
+ -[MXCoreSessionBase allowsDefaultBuiltInRouteCustomization]
+ -[MXCoreSessionBase alwaysPlaysAudio]
+ -[MXCoreSessionBase audioObjectID]
+ -[MXCoreSessionBase bundleIdToPAAccessIntervalMap]
+ -[MXCoreSessionBase copyAvailableRouteControlFeatures:]
+ -[MXCoreSessionBase copySessionRoutingInfoFromVA]
+ -[MXCoreSessionBase defaultBuiltInRoutePreferenceSetByClient]
+ -[MXCoreSessionBase defaultBuiltInRoutePreference]
+ -[MXCoreSessionBase defaultBuiltInRouteToUse]
+ -[MXCoreSessionBase didExtractEntitlementsFromAuditToken]
+ -[MXCoreSessionBase dumpDebugConfigInfo]
+ -[MXCoreSessionBase dumpDebugStateInfo]
+ -[MXCoreSessionBase enableBluetoothRecordingPreferenceSetByClient]
+ -[MXCoreSessionBase extractAndSetAuditToken:]
+ -[MXCoreSessionBase getSessionIDFromAudioObject]
+ -[MXCoreSessionBase hasEntitlementToSuppressRecordingStateToSystemStatus]
+ -[MXCoreSessionBase hasExternalMuteNotificationContext]
+ -[MXCoreSessionBase idleSleepPreventorAllocated]
+ -[MXCoreSessionBase idleSleepPreventorCreationTime]
+ -[MXCoreSessionBase idleSleepPreventorName]
+ -[MXCoreSessionBase idleSleepPreventorUpdaterTimer]
+ -[MXCoreSessionBase idleSleepPreventor]
+ -[MXCoreSessionBase isActiveDeviceWithValidSessionID:]
+ -[MXCoreSessionBase isPlayingStartTime]
+ -[MXCoreSessionBase isPlayingStopTime]
+ -[MXCoreSessionBase isRecordingMuted]
+ -[MXCoreSessionBase isRecordingWithBTManagedDevice]
+ -[MXCoreSessionBase isUsingBuiltInMic]
+ -[MXCoreSessionBase mode]
+ -[MXCoreSessionBase mostRecentSessionInfoSetOnVA]
+ -[MXCoreSessionBase playbackAssertionRef]
+ -[MXCoreSessionBase populateAdditiveRoutingInfoWithBTRecordingCustomizations:]
+ -[MXCoreSessionBase populateAdditiveRoutingInfoWithDefaultBuiltInRouteCustomization:]
+ -[MXCoreSessionBase populateAdditiveRoutingInfoWithEchoCancelledInput:]
+ -[MXCoreSessionBase populateAdditiveRoutingInfoWithFollowingVADInformation:inputOnly:]
+ -[MXCoreSessionBase populateAdditiveRoutingInfoWithRouteControlFeatures:]
+ -[MXCoreSessionBase postSessionNotification:payload:]
+ -[MXCoreSessionBase preferredRouteControlFeatures]
+ -[MXCoreSessionBase prefersEchoCancelledInput]
+ -[MXCoreSessionBase prefersSuppressingRecordingState]
+ -[MXCoreSessionBase processActiveDevice:]
+ -[MXCoreSessionBase processOnDemandVADLossIfNeeded:isPreviousInputVADOnDemand:]
+ -[MXCoreSessionBase processSessionRoutingInfo:]
+ -[MXCoreSessionBase processSessionRoutingInfoDidChange]
+ -[MXCoreSessionBase removeSessionAudioObject]
+ -[MXCoreSessionBase requiresExclaveSensor]
+ -[MXCoreSessionBase resumeAssertionRef]
+ -[MXCoreSessionBase resumeBackgroundAppUpdaterTimer]
+ -[MXCoreSessionBase sendSessionConfigurationInfoToVA:]
+ -[MXCoreSessionBase setAllowsBluetoothRecordingCustomization:]
+ -[MXCoreSessionBase setAllowsDefaultBuiltInRouteCustomization:]
+ -[MXCoreSessionBase setAudioObjectID:]
+ -[MXCoreSessionBase setBundleIdToPAAccessIntervalMap:]
+ -[MXCoreSessionBase setDefaultBuiltInRoutePreference:]
+ -[MXCoreSessionBase setDefaultBuiltInRoutePreferenceSetByClient:]
+ -[MXCoreSessionBase setEnableBluetoothRecordingPreferenceSetByClient:]
+ -[MXCoreSessionBase setHasEntitlementToSuppressRecordingStateToSystemStatus:]
+ -[MXCoreSessionBase setHasExternalMuteNotificationContext:]
+ -[MXCoreSessionBase setIdleSleepPreventor:]
+ -[MXCoreSessionBase setIdleSleepPreventorAllocated:]
+ -[MXCoreSessionBase setIdleSleepPreventorCreationTime:]
+ -[MXCoreSessionBase setIdleSleepPreventorName:]
+ -[MXCoreSessionBase setIdleSleepPreventorUpdaterTimer:]
+ -[MXCoreSessionBase setIsPlayingStartTime:]
+ -[MXCoreSessionBase setIsPlayingStopTime:]
+ -[MXCoreSessionBase setIsRecordingMuted:]
+ -[MXCoreSessionBase setMode:]
+ -[MXCoreSessionBase setMostRecentSessionInfoSetOnVA:]
+ -[MXCoreSessionBase setPlaybackAssertionRef:]
+ -[MXCoreSessionBase setPreferredRouteControlFeatures:]
+ -[MXCoreSessionBase setPrefersEchoCancelledInput:]
+ -[MXCoreSessionBase setPrefersSuppressingRecordingState:]
+ -[MXCoreSessionBase setResumeAssertionRef:]
+ -[MXCoreSessionBase setResumeBackgroundAppUpdaterTimer:]
+ -[MXCoreSessionBase setShadowingAudioSessionID:]
+ -[MXCoreSessionBase setShadowingAudioSessionOptions:]
+ -[MXCoreSessionBase setWaitingToResume:]
+ -[MXCoreSessionBase shadowingAudioSessionID]
+ -[MXCoreSessionBase shadowingAudioSessionOptions]
+ -[MXCoreSessionBase shouldEnableBluetoothRecording]
+ -[MXCoreSessionBase shouldSendSessionConfigurationInfoToVA]
+ -[MXCoreSessionBase unregisterSessionAudioObject]
+ -[MXCoreSessionBase updateAudioBehaviorFromVARouteConfig:]
+ -[MXCoreSessionBase updateAudioSessionIDAndAudioObject:]
+ -[MXCoreSessionBase updateIsRecordingMuted:updateBluetoothFrameworkToPlayMuteChime:]
+ -[MXCoreSessionBase updateSessionRoutingInformation:]
+ -[MXCoreSessionBase updateShadowingAudioSessionOptions:shouldUpdateVAConfig:]
+ -[MXCoreSessionBase updateShadowingAudioSessionOptions:shouldUpdateVAConfig:].cold.1
+ -[MXCoreSessionBase updateShadowingAudioSessionOptions:shouldUpdateVAConfig:].cold.2
+ -[MXCoreSessionBase updateShadowingAudioSessionOptions:shouldUpdateVAConfig:].cold.3
+ -[MXCoreSessionBase updateShadowingAudioSessionOptions:shouldUpdateVAConfig:].cold.4
+ -[MXCoreSessionBase waitingToResume]
+ -[MXCoreSessionBase willRouteToOnDemandVADOnActivation:]
+ -[MXCoreSessionIndependentAudioResource activate]
+ -[MXCoreSessionIndependentAudioResource deactivate]
+ -[MXCoreSessionIndependentAudioResource dealloc]
+ -[MXCoreSessionIndependentAudioResource init]
+ -[MXCoreSessionIndependentAudioResource requiresExclaveSensor]
+ -[MXCoreSessionIndependentAudioResource updateIsPlaying:]
+ -[MXCoreSessionIndependentAudioResource updateIsRecording:]
+ -[MXCoreSessionIndependentInputAudioResource _beginInterruptionWithSecTask:andFlags:]
+ -[MXCoreSessionIndependentInputAudioResource _endInterruptionWithSecTask:andStatus:]
+ -[MXCoreSessionIndependentInputAudioResource addMXSessionIndependentInputAudioResource:]
+ -[MXCoreSessionIndependentInputAudioResource additiveRoutingInfo]
+ -[MXCoreSessionIndependentInputAudioResource copyMXSessionIndependentInputAudioResourceList]
+ -[MXCoreSessionIndependentInputAudioResource copyPropertyForKey:valueOut:]
+ -[MXCoreSessionIndependentInputAudioResource copyPropertyForKey:valueOut:].cold.1
+ -[MXCoreSessionIndependentInputAudioResource copyPropertyForKey:valueOut:].cold.2
+ -[MXCoreSessionIndependentInputAudioResource dealloc]
+ -[MXCoreSessionIndependentInputAudioResource dumpDebugInfo]
+ -[MXCoreSessionIndependentInputAudioResource initWithOptions:]
+ -[MXCoreSessionIndependentInputAudioResource populateAdditiveRoutingInfoWithRouteControlFeatures:]
+ -[MXCoreSessionIndependentInputAudioResource removeMXSessionIndependentInputAudioResource:]
+ -[MXCoreSessionIndependentInputAudioResource resetMXSessionIsPlayingStates]
+ -[MXCoreSessionIndependentInputAudioResource resetMXSessionIsRecordingStates]
+ -[MXCoreSessionIndependentInputAudioResource sendSessionConfigurationInfoToVA]
+ -[MXCoreSessionIndependentInputAudioResource setPropertyForKey:value:]
+ -[MXCoreSessionIndependentInputAudioResource setPropertyForKey:value:].cold.1
+ -[MXCoreSessionIndependentInputAudioResource setPropertyForKey:value:].cold.10
+ -[MXCoreSessionIndependentInputAudioResource setPropertyForKey:value:].cold.11
+ -[MXCoreSessionIndependentInputAudioResource setPropertyForKey:value:].cold.12
+ -[MXCoreSessionIndependentInputAudioResource setPropertyForKey:value:].cold.13
+ -[MXCoreSessionIndependentInputAudioResource setPropertyForKey:value:].cold.14
+ -[MXCoreSessionIndependentInputAudioResource setPropertyForKey:value:].cold.15
+ -[MXCoreSessionIndependentInputAudioResource setPropertyForKey:value:].cold.16
+ -[MXCoreSessionIndependentInputAudioResource setPropertyForKey:value:].cold.17
+ -[MXCoreSessionIndependentInputAudioResource setPropertyForKey:value:].cold.18
+ -[MXCoreSessionIndependentInputAudioResource setPropertyForKey:value:].cold.19
+ -[MXCoreSessionIndependentInputAudioResource setPropertyForKey:value:].cold.2
+ -[MXCoreSessionIndependentInputAudioResource setPropertyForKey:value:].cold.20
+ -[MXCoreSessionIndependentInputAudioResource setPropertyForKey:value:].cold.21
+ -[MXCoreSessionIndependentInputAudioResource setPropertyForKey:value:].cold.22
+ -[MXCoreSessionIndependentInputAudioResource setPropertyForKey:value:].cold.23
+ -[MXCoreSessionIndependentInputAudioResource setPropertyForKey:value:].cold.3
+ -[MXCoreSessionIndependentInputAudioResource setPropertyForKey:value:].cold.4
+ -[MXCoreSessionIndependentInputAudioResource setPropertyForKey:value:].cold.5
+ -[MXCoreSessionIndependentInputAudioResource setPropertyForKey:value:].cold.6
+ -[MXCoreSessionIndependentInputAudioResource setPropertyForKey:value:].cold.7
+ -[MXCoreSessionIndependentInputAudioResource setPropertyForKey:value:].cold.8
+ -[MXCoreSessionIndependentInputAudioResource setPropertyForKey:value:].cold.9
+ -[MXCoreSessionIndependentInputAudioResource shouldSendSessionConfigurationInfoToVA]
+ -[MXCoreSessionIndependentInputAudioResource teardown]
+ -[MXCoreSessionIndependentInputAudioResource willRouteToOnDemandVADOnActivation]
+ -[MXCoreSessionSecure additiveRoutingInfo]
+ -[MXCoreSessionSecure copyPropertyForKey:valueOut:].cold.2
+ -[MXCoreSessionSecure copyPropertyForKey:valueOut:].cold.3
+ -[MXCoreSessionSecure sendSessionConfigurationInfoToVA]
+ -[MXCoreSessionSecure shouldSendSessionConfigurationInfoToVA]
+ -[MXCoreSessionSecure willRouteToOnDemandVADOnActivation]
+ -[MXFrontBoardServices clearLayoutRoleCache]
+ -[MXFrontBoardServices copyPrimaryAppDisplayID]
+ -[MXFrontBoardServices getLayoutRoleForDisplayID:layoutRole:]
+ -[MXFrontBoardServices init]
+ -[MXFrontBoardServices init].cold.1
+ -[MXFrontBoardServices init].cold.2
+ -[MXFrontBoardServices init].cold.3
+ -[MXFrontBoardServices init].cold.4
+ -[MXFrontBoardServices isAppInPiP:]
+ -[MXFrontBoardServices isAppInSplitView:]
+ -[MXFrontBoardServices layoutChanged:]
+ -[MXFrontBoardServices updateLayoutRoleCache:displayID:]
+ -[MXMediaEndowmentManager getHostProcessAttributions:]
+ -[MXRoutingContextCallbackHelper initWithRoutingContext:routeConfigUpdateID:correlationID:callback:context:]
+ -[MXRoutingContextModificationMetrics RTCDictionary]
+ -[MXRoutingContextModificationMetrics clientModificationFinishedTimestamp]
+ -[MXRoutingContextModificationMetrics clientModificationStartedTimestamp]
+ -[MXRoutingContextModificationMetrics correlationID]
+ -[MXRoutingContextModificationMetrics dealloc]
+ -[MXRoutingContextModificationMetrics description]
+ -[MXRoutingContextModificationMetrics dictionaryRepresentation]
+ -[MXRoutingContextModificationMetrics figEndpointType]
+ -[MXRoutingContextModificationMetrics initWithCorrelationID:]
+ -[MXRoutingContextModificationMetrics initWithDictionary:]
+ -[MXRoutingContextModificationMetrics serverModificationFinishedTimestamp]
+ -[MXRoutingContextModificationMetrics serverModificationStartedTimestamp]
+ -[MXRoutingContextModificationMetrics setClientModificationFinishedTimestamp:]
+ -[MXRoutingContextModificationMetrics setClientModificationStartedTimestamp:]
+ -[MXRoutingContextModificationMetrics setFigEndpointType:]
+ -[MXRoutingContextModificationMetrics setServerModificationFinishedTimestamp:]
+ -[MXRoutingContextModificationMetrics setServerModificationStartedTimestamp:]
+ -[MXRoutingContextModificationResult dealloc]
+ -[MXRoutingContextModificationResult description]
+ -[MXRoutingContextModificationResult dictionaryRepresentation]
+ -[MXRoutingContextModificationResult initWithDictionary:]
+ -[MXRoutingContextModificationResult initWithRouteConfigUpdatedReason:modificationMetrics:]
+ -[MXRoutingContextModificationResult modificationMetrics]
+ -[MXRoutingContextModificationResult routeConfigUpdateReason]
+ -[MXRoutingContextReportingRTCServiceImpl _configurationDidFinish]
+ -[MXRoutingContextReportingRTCServiceImpl dealloc]
+ -[MXRoutingContextReportingRTCServiceImpl initWithFigEndpointType:]
+ -[MXRoutingContextReportingRTCServiceImpl initWithFigEndpointType:].cold.1
+ -[MXRoutingContextReportingRTCServiceImpl initWithFigEndpointType:].cold.2
+ -[MXRoutingContextReportingRTCServiceImpl initWithFigEndpointType:].cold.3
+ -[MXRoutingContextReportingRTCServiceImpl initWithFigEndpointType:].cold.4
+ -[MXRoutingContextReportingRTCServiceImpl initWithFigEndpointType:].cold.5
+ -[MXRoutingContextReportingRTCServiceImpl initWithFigEndpointType:].cold.6
+ -[MXRoutingContextReportingRTCServiceImpl initWithFigEndpointType:].cold.7
+ -[MXRoutingContextReportingRTCServiceImpl sendModificationResult:]
+ -[MXRoutingContextReportingService dealloc]
+ -[MXRoutingContextReportingService initWithModificationMetrics:useMockService:]
+ -[MXRoutingContextReportingService modificationMetrics]
+ -[MXRoutingContextReportingService sendModificationResult]
+ -[MXSession(InterfaceImpl) setPropertyForKeyInternal:value:fromPropertiesBatch:].cold.20
+ -[MXSession(InterfaceImpl) setPropertyForKeyInternal:value:fromPropertiesBatch:].cold.21
+ -[MXSession(InterfaceImpl) setPropertyForKeyInternal:value:fromPropertiesBatch:].cold.22
+ -[MXSession(InternalUse) getAudioTrackStatus]
+ -[MXSession(InternalUse) getIsPlayerMuted]
+ -[MXSession(InternalUse) getIsPlayingVideoOutput]
+ -[MXSession(InternalUse) setAudioTrackStatus:]
+ -[MXSession(InternalUse) setIsPlayerMuted:]
+ -[MXSession(InternalUse) setIsPlayingVideoOutput:]
+ -[MXSessionIndependentAudioResource audioToolboxIsPlaying]
+ -[MXSessionIndependentAudioResource clientIsPlaying]
+ -[MXSessionIndependentAudioResource dealloc]
+ -[MXSessionIndependentAudioResource dumpDebugInfo]
+ -[MXSessionIndependentAudioResource init]
+ -[MXSessionIndependentAudioResource isPlaying]
+ -[MXSessionIndependentAudioResource isRecording]
+ -[MXSessionIndependentAudioResource setAudioToolboxIsPlaying:]
+ -[MXSessionIndependentAudioResource setClientIsPlaying:]
+ -[MXSessionIndependentAudioResource setIsPlaying:]
+ -[MXSessionIndependentAudioResource setIsRecording:]
+ -[MXSessionIndependentInputAudioResource _beginInterruptionWithSecTask:andFlags:]
+ -[MXSessionIndependentInputAudioResource _copyPropertyForKey:valueOut:]
+ -[MXSessionIndependentInputAudioResource _endInterruptionWithSecTask:andStatus:]
+ -[MXSessionIndependentInputAudioResource _setPropertyForKey:value:]
+ -[MXSessionIndependentInputAudioResource copyPropertyForKeyInternal:valueOut:]
+ -[MXSessionIndependentInputAudioResource copyPropertyForKeyInternal:valueOut:].cold.1
+ -[MXSessionIndependentInputAudioResource copyPropertyForKeyInternal:valueOut:].cold.2
+ -[MXSessionIndependentInputAudioResource copyPropertyForKeyInternal:valueOut:].cold.3
+ -[MXSessionIndependentInputAudioResource dealloc]
+ -[MXSessionIndependentInputAudioResource dumpDebugInfo]
+ -[MXSessionIndependentInputAudioResource initWithOptions:]
+ -[MXSessionIndependentInputAudioResource resetIsPlayingStates]
+ -[MXSessionIndependentInputAudioResource resetIsRecordingState]
+ -[MXSessionIndependentInputAudioResource setPropertyForKeyInternal:value:fromPropertiesBatch:]
+ -[MXSessionIndependentInputAudioResource setPropertyForKeyInternal:value:fromPropertiesBatch:].cold.1
+ -[MXSessionIndependentInputAudioResource setPropertyForKeyInternal:value:fromPropertiesBatch:].cold.2
+ -[MXSessionIndependentInputAudioResource setPropertyForKeyInternal:value:fromPropertiesBatch:].cold.3
+ -[MXSessionIndependentInputAudioResource setPropertyForKeyInternal:value:fromPropertiesBatch:].cold.4
+ -[MXSessionIndependentInputAudioResource setPropertyForKeyInternal:value:fromPropertiesBatch:].cold.5
+ -[MXSessionManager copyActiveCoreSessionControllingRouting]
+ -[MXSessionManager copySessionsThatUserIntendsToUnmute:]
+ -[MXSessionManager handleUserIntentToUnmute:]
+ -[MXSessionManager isVoiceAssistantPlayingToPersonalAudioDeviceOverMedia]
+ -[MXSessionManager setIsVoiceAssistantPlayingToPersonalAudioDeviceOverMedia:]
+ -[MXSessionManager setSomeLongFormVideoClientIsActive:]
+ -[MXSessionManager someLongFormVideoClientIsActive]
+ -[MXSessionManager(ActivationUtilities) prepareSessionActivationBeforeACQDispatch:]
+ -[MXSessionManager(DuckingUtilities) muteOutputForSession:]
+ -[MXSessionManager(DuckingUtilities) unmuteOutputForSession:]
+ -[MXSessionManager(Utilities) canSessionsCoexistDueToMediaMultitasking:victim:]
+ -[MXSessionManager(Utilities) canSessionsCoexistDueToOutputMuting:victim:]
+ -[MXSessionManager(Utilities) copyCoreSessionsShadowingAudioSession:withOptions:]
+ -[MXSessionManager(Utilities) copyDisplayIDForActiveCarPlayVideoSession]
+ -[MXSessionManager(Utilities) getCurrentOutputPort]
+ -[MXSessionManager(Utilities) getShadowingAudioSessionOptionsAsString:]
+ -[MXSessionManager(Utilities) interruptAllIndependentInputAudioResourceSessionsIfNeeded:]
+ -[MXSessionManager(Utilities) isCurrentRouteHeadphoneAndInEar:]
+ -[MXSessionManager(Utilities) isPortHeadphoneWithInEarDetectionSupported:]
+ -[MXSessionManager(Utilities) isSessionConfigurationEligibleForOutputMuting:audioMode:]
+ -[MXSessionManager(Utilities) postStopCommandToShadowingSessionsForSession:withShadowingOptions:]
+ -[MXSessionManager(Utilities) resumeInterruptedIndependentInputAudioResourceSessionsIfNeeded:]
+ -[MXSessionManager(Utilities) shouldAllowBluetoothAccessoryToRequestAudioRoute]
+ -[MXSessionManager(Utilities) synchronizeSessionVolumeWithMediaVolumeIfNeeded:]
+ -[MXSessionManager(Utilities) updateForRecordingStateDidChange]
+ -[MXSessionManager(Utilities) updateSomeLongFormVideoClientIsActive]
+ -[MXSessionManagerIndependentAudioResource _beginInterruption:withSecTask:andFlags:]
+ -[MXSessionManagerIndependentAudioResource _endInterruption:withSecTask:andStatus:]
+ -[MXSessionManagerIndependentAudioResource addMXCoreSessionIndependentInputAudioResource:]
+ -[MXSessionManagerIndependentAudioResource copyIndependentInputAudioResourceSessionWithAudioSessionID:]
+ -[MXSessionManagerIndependentAudioResource copyMXCoreSessionIndependentInputAudioResourceList]
+ -[MXSessionManagerIndependentAudioResource dealloc]
+ -[MXSessionManagerIndependentAudioResource dumpDebugInfo]
+ -[MXSessionManagerIndependentAudioResource init]
+ -[MXSessionManagerIndependentAudioResource interruptAllIndependentInputAudioResourceSessions:interruptorName:]
+ -[MXSessionManagerIndependentAudioResource interruptIndpendentInputAudioResourceSession:interruptorBundleID:interruptorName:fadeDuration:waitingToResume:]
+ -[MXSessionManagerIndependentAudioResource postInterruptionCommandNotification:interruptionCommand:interruptorName:interruptorBundleID:status:volumeChangeDuration:]
+ -[MXSessionManagerIndependentAudioResource postStopCommandToShadowingSessionsForSession:withShadowingOptions:interruptor:waitingToResume:]
+ -[MXSessionManagerIndependentAudioResource removeMXCoreSessionIndependentInputAudioResource:]
+ -[MXSessionManagerIndependentAudioResource resumeAllIndependentInputAudioResourceSessions:interruptorBundleID:interruptorName:]
+ -[MXSessionManagerIndependentAudioResource resumeAllIndependentInputAudioResourceSessionsShadowing:withShadowingOptions:interruptor:status:]
+ -[MXSessionManagerIndependentAudioResource resumeIndependentInputAudioResourceSession:interruptorBundleID:interruptorName:status:fadeDuration:]
+ -[MXSystemController applyPIDToInheritAppStateFrom:].cold.3
+ -[MXSystemController getAudioSessionID:forAttributedPID:]
+ -[MXSystemController(InternalUse) copyAttributeForKeyInternal:withValueOut:].cold.1
+ -[MXSystemController(InternalUse) setAttributeForKeyInternal:andValue:].cold.9
+ -[MXSystemSoundServices dealloc]
+ -[MXSystemSoundServices init]
+ -[MXSystemSoundServices playPrivacyPongSound]
+ -[MXSystemSoundServices playSystemSound:completionBlock:]
+ -[MXSystemSoundServices shouldPrivacyPongPlay]
+ -[MXUndoBannerResponseInfo dealloc]
+ -[MXUndoBannerResponseInfo fromPorts]
+ -[MXUndoBannerResponseInfo init]
+ -[MXUndoBannerResponseInfo routeSemaphore]
+ -[MXUndoBannerResponseInfo setFromPorts:]
+ -[MXUndoBannerResponseInfo setRouteSemaphore:]
+ -[MXUndoBannerResponseInfo setTxid:]
+ -[MXUndoBannerResponseInfo setUndoBannerResponse:]
+ -[MXUndoBannerResponseInfo txid]
+ -[MXUndoBannerResponseInfo undoBannerResponse]
+ -[MXUserPreferredInputRouteCache clearUserPreferredRoute:]
+ -[MXUserPreferredInputRouteCache copyUserPreferredRoute:]
+ -[MXUserPreferredInputRouteCache dealloc]
+ -[MXUserPreferredInputRouteCache init]
+ -[MXUserPreferredInputRouteCache setUserPreferredRoute:hostApplicationBundleID:]
+ -[MXVolumeManager(Internal) updateMediaVolumeForPersonalDevice:oldRoute:]
+ -[MX_BannerManager cleanupConnectBannerIfNeeded:routeName:]
+ -[MX_BannerManager cleanupUndoBannerIfNeeded:routeName:]
+ -[MX_BannerManager copyUndoEndpointsForRoute:]
+ -[MX_BannerManager dealloc]
+ -[MX_BannerManager init]
+ -[MX_BannerManager isAnyConnectBannerActive]
+ -[MX_BannerManager isCarPlayPortRoutableFromCustomizedRoutingPerspective:]
+ -[MX_BannerManager newPortNeedsToShowBanner:newPortIdentifier:newPortType:previousPort:]
+ -[MX_BannerManager promptUserResponseForRoute:newPortIdentifier:newPortName:newPortID:newPortType:newWirelessPorts:oldPort:activatingEndpoint:routingContext:connectHandler:]
+ -[MX_BannerManager promptUserResponseForUndoRoute:newPortIdentifier:newPortName:newPortID:newPortType:oldPort:routingContext:undoHandler:]
+ -[MX_NetworkObserver networkPathUpdate:].cold.3
+ GCC_except_table100
+ GCC_except_table113
+ GCC_except_table115
+ GCC_except_table118
+ GCC_except_table120
+ GCC_except_table122
+ GCC_except_table167
+ GCC_except_table169
+ GCC_except_table171
+ GCC_except_table175
+ GCC_except_table177
+ GCC_except_table179
+ GCC_except_table181
+ GCC_except_table183
+ GCC_except_table196
+ GCC_except_table201
+ GCC_except_table205
+ GCC_except_table211
+ GCC_except_table217
+ GCC_except_table232
+ GCC_except_table36
+ GCC_except_table49
+ GCC_except_table494
+ GCC_except_table495
+ GCC_except_table68
+ GCC_except_table70
+ GCC_except_table76
+ GCC_except_table77
+ _AVSystemController_ActiveCallInfo_AudioSessionID
+ _AVSystemController_AllowBluetoothAccessoryToRequestAudioRouteAttribute
+ _AVSystemController_AllowBluetoothAccessoryToRequestAudioRouteDidChangeNotification
+ _AVSystemController_AllowBluetoothAccessoryToRequestAudioRouteDidChangeNotificationParameter_IsAllowed
+ _AVSystemController_PreferHeadphonesOverCarsAndSpeakersDidChangeNotification
+ _AVSystemController_PreferHeadphonesOverCarsAndSpeakersDidChangeNotificationParameter_Enabled
+ _AVSystemController_PreferHeadphonesOverCarsAndSpeakersEnabledAttribute
+ _AudioServicesPlaySystemSoundWithCompletion
+ _CFAllocatorAllocateTyped
+ _CMBaseObjectCopyProperty
+ _CMSMDeviceState_SupportsMediaMultitasking
+ _CMSMDeviceState_SupportsMediaMultitasking.cold.1
+ _CMSMDeviceState_SupportsMediaMultitasking.onceToken
+ _CMSMDeviceState_SupportsMediaMultitasking.supportsMediaMultitasking
+ _CMSMDeviceState_SupportsShortFormOutputMutingAudioPolicy
+ _CMSMDeviceState_SupportsShortFormOutputMutingAudioPolicy.cold.1
+ _CMSMDeviceState_SupportsShortFormOutputMutingAudioPolicy.onceToken
+ _CMSMDeviceState_SupportsShortFormOutputMutingAudioPolicy.supportsOutputMuting
+ _CMSMDeviceState_UpdateDeviceClass
+ _CMSMNotificationUtility_PostAllowBluetoothAccessoryToRequestAudioRouteDidChangeNotification
+ _CMSMNotificationUtility_PostAllowBluetoothAccessoryToRequestAudioRouteDidChangeNotificationIfNeeded
+ _CMSMNotificationUtility_PostIsOutputMutedDidChange
+ _CMSMNotificationUtility_PostPreferHeadphonesOverCarsAndSpeakersDidChange
+ _CMSMNotificationUtility_PostUserIntentToUnmuteDidChange
+ _CMSMSleep_HandleIdleSleep
+ _CMSMUtility_IsCarPlayVideoActive
+ _CMSMVAUtility_CopyFigIODeviceNameFromVADPorts
+ _CMSMVAUtility_IsAnyBluetoothVehicleConnected
+ _CMSMVAUtility_IsInputPortBluetoothMicrophone
+ _CMSMVAUtility_IsPortOfTypeBluetooth
+ _CMSMVAUtility_IsPortOfTypeBluetoothVehicle
+ _CMSUtilityPredicate_IsAffectedByApplicationStateChange
+ _CMSUtility_ChangeKeepsPhoneCallBehavior
+ _CMSUtility_IsAllowedToStartRecordingCoexistingWithTheAssistant
+ _CMSUtility_IsSessionRouteEligibleForTipi
+ _DisplayModeRefreshRateObserver_ReadHDMILatencyFromCoreAnimation
+ _FigEndpointCentralEntityIsDoingActivity.cold.1
+ _FigEndpointSessionHandleInterruption.cold.1
+ _FigEndpointSessionHandleInterruption.cold.2
+ _FigEndpointSessionHandleInterruption.cold.3
+ _FigEndpointSessionHandleInterruption.cold.4
+ _FigEndpointUIAgentStartServer.cold.2
+ _FigPredictedRouting_IsEndpointThePredictedRoute
+ _FigRouteDiscovererCopyAvailableRouteDescriptors
+ _FigRouteDiscovererCopyAvailableRoutes
+ _FigRouteDiscoveryManagerCopyFallbackRouteDescriptor
+ _FigRouteDiscoveryManagerCopyFallbackRouteDescriptor.cold.1
+ _FigRouteDiscoveryManagerCopyFallbackRouteDescriptor.cold.2
+ _FigRouteDiscoveryManagerCopyFallbackRouteDescriptor.cold.3
+ _FigRouteDiscoveryManagerCopyFallbackRouteDescriptor.cold.4
+ _FigRoutingContextResilientRemoteCopySystemAudioInputContext
+ _FigRoutingContextResilientRemoteCreate.cold.3
+ _FigRoutingContextResilientRemoteCreate.cold.4
+ _FigRoutingContextResilientRemoteCreate.cold.5
+ _FigRoutingContextUtilities_LogCurrentState.cold.1
+ _FigRoutingContextXPCHandleCopyPredictedSelectedRouteDescriptorMessage.cold.1
+ _FigRoutingContextXPCHandleCopyPredictedSelectedRouteDescriptorMessage.cold.2
+ _FigRoutingContextXPCHandleReportModificationMetricsMessage
+ _FigRoutingContextXPCHandleResetPredictedSelectedRouteDescriptorMessage.cold.1
+ _FigRoutingContextXPCHandleResetPredictedSelectedRouteDescriptorMessage.cold.2
+ _FigRoutingManagerCopyPartnerPorts
+ _FigRoutingManagerIsRoutableConsideringBannerState
+ _FigRoutingManagerProcessAirPodsInEarRouting
+ _FigRoutingManagerUtilities_LogPartnerPorts
+ _FigRoutingManagerUtilities_PostEndpointNotification
+ _FigRoutingSessionManagerResilientRemoteCopyLongFormVideoManager.onceToken
+ _FigRoutingSessionManagerResilientRemoteCopyLongFormVideoManager.sLongFormManager
+ _FigSignalErrorAt3
+ _FigStarkModeControllerRemoteCreate.cold.1
+ _FigVibratorInitialize.cold.1
+ _FigVibratorInitialize.cold.2
+ _FigVibratorInitialize.cold.3
+ _FigVibratorInitialize.cold.4
+ _FigVibratorInitialize.cold.5
+ _FigVibratorInitialize.cold.6
+ _FigVibratorInitialize.cold.7
+ _FigVibratorInitialize.cold.8
+ _FigVibratorPlayVibrationWithDictionary.cold.1
+ _HDMILatencyMgr_GetHDMILatencyForCurrentRefreshRate
+ _IOHIDEventSystemClientSetMatchingMultiple
+ _MXCFCopyPrefixSubstring
+ _MXCFNumberCreateFromDouble
+ _MXCFPreferencesGetBooleanWithDefault
+ _MXCoreSessionCopyProperty.cold.167
+ _MXCoreSessionCopyProperty.cold.168
+ _MXCoreSessionCopyProperty.cold.169
+ _MXCoreSessionCopyProperty.cold.170
+ _MXCoreSessionCopyProperty.cold.171
+ _MXCoreSessionSetProperty.cold.100
+ _MXCoreSessionSetProperty.cold.101
+ _MXCoreSessionSetProperty.cold.102
+ _MXCoreSessionSetProperty.cold.103
+ _MXCoreSessionSetProperty.cold.104
+ _MXCoreSessionSetProperty.cold.105
+ _MXCoreSessionSetProperty.cold.106
+ _MXCoreSessionSetProperty.cold.107
+ _MXCoreSessionSetProperty.cold.108
+ _MXCoreSessionSetProperty.cold.109
+ _MXCoreSessionSetProperty.cold.110
+ _MXCoreSessionSetProperty.cold.111
+ _MXCoreSessionSetProperty.cold.112
+ _MXCoreSessionSetProperty.cold.113
+ _MXCoreSessionSetProperty.cold.114
+ _MXCoreSessionSetProperty.cold.115
+ _MXCoreSessionSetProperty.cold.116
+ _MXCoreSessionSetProperty.cold.117
+ _MXCoreSessionSetProperty.cold.118
+ _MXCoreSessionSetProperty.cold.119
+ _MXCoreSessionSetProperty.cold.12
+ _MXCoreSessionSetProperty.cold.120
+ _MXCoreSessionSetProperty.cold.121
+ _MXCoreSessionSetProperty.cold.122
+ _MXCoreSessionSetProperty.cold.123
+ _MXCoreSessionSetProperty.cold.124
+ _MXCoreSessionSetProperty.cold.125
+ _MXCoreSessionSetProperty.cold.126
+ _MXCoreSessionSetProperty.cold.127
+ _MXCoreSessionSetProperty.cold.128
+ _MXCoreSessionSetProperty.cold.129
+ _MXCoreSessionSetProperty.cold.13
+ _MXCoreSessionSetProperty.cold.130
+ _MXCoreSessionSetProperty.cold.131
+ _MXCoreSessionSetProperty.cold.132
+ _MXCoreSessionSetProperty.cold.133
+ _MXCoreSessionSetProperty.cold.134
+ _MXCoreSessionSetProperty.cold.135
+ _MXCoreSessionSetProperty.cold.136
+ _MXCoreSessionSetProperty.cold.137
+ _MXCoreSessionSetProperty.cold.138
+ _MXCoreSessionSetProperty.cold.139
+ _MXCoreSessionSetProperty.cold.14
+ _MXCoreSessionSetProperty.cold.140
+ _MXCoreSessionSetProperty.cold.141
+ _MXCoreSessionSetProperty.cold.142
+ _MXCoreSessionSetProperty.cold.143
+ _MXCoreSessionSetProperty.cold.144
+ _MXCoreSessionSetProperty.cold.145
+ _MXCoreSessionSetProperty.cold.146
+ _MXCoreSessionSetProperty.cold.147
+ _MXCoreSessionSetProperty.cold.148
+ _MXCoreSessionSetProperty.cold.149
+ _MXCoreSessionSetProperty.cold.15
+ _MXCoreSessionSetProperty.cold.150
+ _MXCoreSessionSetProperty.cold.151
+ _MXCoreSessionSetProperty.cold.152
+ _MXCoreSessionSetProperty.cold.153
+ _MXCoreSessionSetProperty.cold.154
+ _MXCoreSessionSetProperty.cold.155
+ _MXCoreSessionSetProperty.cold.156
+ _MXCoreSessionSetProperty.cold.157
+ _MXCoreSessionSetProperty.cold.158
+ _MXCoreSessionSetProperty.cold.159
+ _MXCoreSessionSetProperty.cold.16
+ _MXCoreSessionSetProperty.cold.160
+ _MXCoreSessionSetProperty.cold.161
+ _MXCoreSessionSetProperty.cold.162
+ _MXCoreSessionSetProperty.cold.163
+ _MXCoreSessionSetProperty.cold.164
+ _MXCoreSessionSetProperty.cold.165
+ _MXCoreSessionSetProperty.cold.166
+ _MXCoreSessionSetProperty.cold.167
+ _MXCoreSessionSetProperty.cold.168
+ _MXCoreSessionSetProperty.cold.169
+ _MXCoreSessionSetProperty.cold.17
+ _MXCoreSessionSetProperty.cold.170
+ _MXCoreSessionSetProperty.cold.171
+ _MXCoreSessionSetProperty.cold.172
+ _MXCoreSessionSetProperty.cold.173
+ _MXCoreSessionSetProperty.cold.174
+ _MXCoreSessionSetProperty.cold.175
+ _MXCoreSessionSetProperty.cold.176
+ _MXCoreSessionSetProperty.cold.177
+ _MXCoreSessionSetProperty.cold.178
+ _MXCoreSessionSetProperty.cold.179
+ _MXCoreSessionSetProperty.cold.18
+ _MXCoreSessionSetProperty.cold.180
+ _MXCoreSessionSetProperty.cold.181
+ _MXCoreSessionSetProperty.cold.182
+ _MXCoreSessionSetProperty.cold.183
+ _MXCoreSessionSetProperty.cold.184
+ _MXCoreSessionSetProperty.cold.185
+ _MXCoreSessionSetProperty.cold.186
+ _MXCoreSessionSetProperty.cold.187
+ _MXCoreSessionSetProperty.cold.188
+ _MXCoreSessionSetProperty.cold.189
+ _MXCoreSessionSetProperty.cold.19
+ _MXCoreSessionSetProperty.cold.190
+ _MXCoreSessionSetProperty.cold.191
+ _MXCoreSessionSetProperty.cold.192
+ _MXCoreSessionSetProperty.cold.193
+ _MXCoreSessionSetProperty.cold.194
+ _MXCoreSessionSetProperty.cold.195
+ _MXCoreSessionSetProperty.cold.196
+ _MXCoreSessionSetProperty.cold.197
+ _MXCoreSessionSetProperty.cold.198
+ _MXCoreSessionSetProperty.cold.199
+ _MXCoreSessionSetProperty.cold.20
+ _MXCoreSessionSetProperty.cold.200
+ _MXCoreSessionSetProperty.cold.201
+ _MXCoreSessionSetProperty.cold.202
+ _MXCoreSessionSetProperty.cold.203
+ _MXCoreSessionSetProperty.cold.204
+ _MXCoreSessionSetProperty.cold.205
+ _MXCoreSessionSetProperty.cold.206
+ _MXCoreSessionSetProperty.cold.207
+ _MXCoreSessionSetProperty.cold.208
+ _MXCoreSessionSetProperty.cold.209
+ _MXCoreSessionSetProperty.cold.21
+ _MXCoreSessionSetProperty.cold.210
+ _MXCoreSessionSetProperty.cold.211
+ _MXCoreSessionSetProperty.cold.212
+ _MXCoreSessionSetProperty.cold.213
+ _MXCoreSessionSetProperty.cold.214
+ _MXCoreSessionSetProperty.cold.215
+ _MXCoreSessionSetProperty.cold.216
+ _MXCoreSessionSetProperty.cold.217
+ _MXCoreSessionSetProperty.cold.218
+ _MXCoreSessionSetProperty.cold.219
+ _MXCoreSessionSetProperty.cold.22
+ _MXCoreSessionSetProperty.cold.220
+ _MXCoreSessionSetProperty.cold.221
+ _MXCoreSessionSetProperty.cold.222
+ _MXCoreSessionSetProperty.cold.223
+ _MXCoreSessionSetProperty.cold.224
+ _MXCoreSessionSetProperty.cold.225
+ _MXCoreSessionSetProperty.cold.226
+ _MXCoreSessionSetProperty.cold.227
+ _MXCoreSessionSetProperty.cold.228
+ _MXCoreSessionSetProperty.cold.229
+ _MXCoreSessionSetProperty.cold.23
+ _MXCoreSessionSetProperty.cold.230
+ _MXCoreSessionSetProperty.cold.231
+ _MXCoreSessionSetProperty.cold.232
+ _MXCoreSessionSetProperty.cold.233
+ _MXCoreSessionSetProperty.cold.234
+ _MXCoreSessionSetProperty.cold.235
+ _MXCoreSessionSetProperty.cold.236
+ _MXCoreSessionSetProperty.cold.237
+ _MXCoreSessionSetProperty.cold.238
+ _MXCoreSessionSetProperty.cold.239
+ _MXCoreSessionSetProperty.cold.24
+ _MXCoreSessionSetProperty.cold.240
+ _MXCoreSessionSetProperty.cold.241
+ _MXCoreSessionSetProperty.cold.242
+ _MXCoreSessionSetProperty.cold.243
+ _MXCoreSessionSetProperty.cold.244
+ _MXCoreSessionSetProperty.cold.245
+ _MXCoreSessionSetProperty.cold.246
+ _MXCoreSessionSetProperty.cold.247
+ _MXCoreSessionSetProperty.cold.248
+ _MXCoreSessionSetProperty.cold.249
+ _MXCoreSessionSetProperty.cold.25
+ _MXCoreSessionSetProperty.cold.250
+ _MXCoreSessionSetProperty.cold.251
+ _MXCoreSessionSetProperty.cold.252
+ _MXCoreSessionSetProperty.cold.253
+ _MXCoreSessionSetProperty.cold.254
+ _MXCoreSessionSetProperty.cold.255
+ _MXCoreSessionSetProperty.cold.256
+ _MXCoreSessionSetProperty.cold.257
+ _MXCoreSessionSetProperty.cold.258
+ _MXCoreSessionSetProperty.cold.259
+ _MXCoreSessionSetProperty.cold.26
+ _MXCoreSessionSetProperty.cold.260
+ _MXCoreSessionSetProperty.cold.261
+ _MXCoreSessionSetProperty.cold.262
+ _MXCoreSessionSetProperty.cold.263
+ _MXCoreSessionSetProperty.cold.264
+ _MXCoreSessionSetProperty.cold.265
+ _MXCoreSessionSetProperty.cold.266
+ _MXCoreSessionSetProperty.cold.267
+ _MXCoreSessionSetProperty.cold.268
+ _MXCoreSessionSetProperty.cold.269
+ _MXCoreSessionSetProperty.cold.27
+ _MXCoreSessionSetProperty.cold.270
+ _MXCoreSessionSetProperty.cold.271
+ _MXCoreSessionSetProperty.cold.272
+ _MXCoreSessionSetProperty.cold.273
+ _MXCoreSessionSetProperty.cold.274
+ _MXCoreSessionSetProperty.cold.275
+ _MXCoreSessionSetProperty.cold.276
+ _MXCoreSessionSetProperty.cold.277
+ _MXCoreSessionSetProperty.cold.278
+ _MXCoreSessionSetProperty.cold.279
+ _MXCoreSessionSetProperty.cold.28
+ _MXCoreSessionSetProperty.cold.280
+ _MXCoreSessionSetProperty.cold.281
+ _MXCoreSessionSetProperty.cold.282
+ _MXCoreSessionSetProperty.cold.283
+ _MXCoreSessionSetProperty.cold.284
+ _MXCoreSessionSetProperty.cold.285
+ _MXCoreSessionSetProperty.cold.286
+ _MXCoreSessionSetProperty.cold.287
+ _MXCoreSessionSetProperty.cold.288
+ _MXCoreSessionSetProperty.cold.289
+ _MXCoreSessionSetProperty.cold.29
+ _MXCoreSessionSetProperty.cold.290
+ _MXCoreSessionSetProperty.cold.291
+ _MXCoreSessionSetProperty.cold.292
+ _MXCoreSessionSetProperty.cold.293
+ _MXCoreSessionSetProperty.cold.294
+ _MXCoreSessionSetProperty.cold.295
+ _MXCoreSessionSetProperty.cold.296
+ _MXCoreSessionSetProperty.cold.297
+ _MXCoreSessionSetProperty.cold.298
+ _MXCoreSessionSetProperty.cold.299
+ _MXCoreSessionSetProperty.cold.30
+ _MXCoreSessionSetProperty.cold.300
+ _MXCoreSessionSetProperty.cold.301
+ _MXCoreSessionSetProperty.cold.302
+ _MXCoreSessionSetProperty.cold.303
+ _MXCoreSessionSetProperty.cold.304
+ _MXCoreSessionSetProperty.cold.305
+ _MXCoreSessionSetProperty.cold.306
+ _MXCoreSessionSetProperty.cold.307
+ _MXCoreSessionSetProperty.cold.308
+ _MXCoreSessionSetProperty.cold.309
+ _MXCoreSessionSetProperty.cold.31
+ _MXCoreSessionSetProperty.cold.310
+ _MXCoreSessionSetProperty.cold.311
+ _MXCoreSessionSetProperty.cold.312
+ _MXCoreSessionSetProperty.cold.313
+ _MXCoreSessionSetProperty.cold.314
+ _MXCoreSessionSetProperty.cold.315
+ _MXCoreSessionSetProperty.cold.316
+ _MXCoreSessionSetProperty.cold.317
+ _MXCoreSessionSetProperty.cold.318
+ _MXCoreSessionSetProperty.cold.319
+ _MXCoreSessionSetProperty.cold.32
+ _MXCoreSessionSetProperty.cold.320
+ _MXCoreSessionSetProperty.cold.321
+ _MXCoreSessionSetProperty.cold.322
+ _MXCoreSessionSetProperty.cold.323
+ _MXCoreSessionSetProperty.cold.324
+ _MXCoreSessionSetProperty.cold.325
+ _MXCoreSessionSetProperty.cold.326
+ _MXCoreSessionSetProperty.cold.327
+ _MXCoreSessionSetProperty.cold.328
+ _MXCoreSessionSetProperty.cold.329
+ _MXCoreSessionSetProperty.cold.33
+ _MXCoreSessionSetProperty.cold.34
+ _MXCoreSessionSetProperty.cold.35
+ _MXCoreSessionSetProperty.cold.36
+ _MXCoreSessionSetProperty.cold.37
+ _MXCoreSessionSetProperty.cold.38
+ _MXCoreSessionSetProperty.cold.39
+ _MXCoreSessionSetProperty.cold.40
+ _MXCoreSessionSetProperty.cold.41
+ _MXCoreSessionSetProperty.cold.42
+ _MXCoreSessionSetProperty.cold.43
+ _MXCoreSessionSetProperty.cold.44
+ _MXCoreSessionSetProperty.cold.45
+ _MXCoreSessionSetProperty.cold.46
+ _MXCoreSessionSetProperty.cold.47
+ _MXCoreSessionSetProperty.cold.48
+ _MXCoreSessionSetProperty.cold.49
+ _MXCoreSessionSetProperty.cold.50
+ _MXCoreSessionSetProperty.cold.51
+ _MXCoreSessionSetProperty.cold.52
+ _MXCoreSessionSetProperty.cold.53
+ _MXCoreSessionSetProperty.cold.54
+ _MXCoreSessionSetProperty.cold.55
+ _MXCoreSessionSetProperty.cold.56
+ _MXCoreSessionSetProperty.cold.57
+ _MXCoreSessionSetProperty.cold.58
+ _MXCoreSessionSetProperty.cold.59
+ _MXCoreSessionSetProperty.cold.60
+ _MXCoreSessionSetProperty.cold.61
+ _MXCoreSessionSetProperty.cold.62
+ _MXCoreSessionSetProperty.cold.63
+ _MXCoreSessionSetProperty.cold.64
+ _MXCoreSessionSetProperty.cold.65
+ _MXCoreSessionSetProperty.cold.66
+ _MXCoreSessionSetProperty.cold.67
+ _MXCoreSessionSetProperty.cold.68
+ _MXCoreSessionSetProperty.cold.69
+ _MXCoreSessionSetProperty.cold.70
+ _MXCoreSessionSetProperty.cold.71
+ _MXCoreSessionSetProperty.cold.72
+ _MXCoreSessionSetProperty.cold.73
+ _MXCoreSessionSetProperty.cold.74
+ _MXCoreSessionSetProperty.cold.75
+ _MXCoreSessionSetProperty.cold.76
+ _MXCoreSessionSetProperty.cold.77
+ _MXCoreSessionSetProperty.cold.78
+ _MXCoreSessionSetProperty.cold.79
+ _MXCoreSessionSetProperty.cold.80
+ _MXCoreSessionSetProperty.cold.81
+ _MXCoreSessionSetProperty.cold.82
+ _MXCoreSessionSetProperty.cold.83
+ _MXCoreSessionSetProperty.cold.84
+ _MXCoreSessionSetProperty.cold.85
+ _MXCoreSessionSetProperty.cold.86
+ _MXCoreSessionSetProperty.cold.87
+ _MXCoreSessionSetProperty.cold.88
+ _MXCoreSessionSetProperty.cold.89
+ _MXCoreSessionSetProperty.cold.90
+ _MXCoreSessionSetProperty.cold.91
+ _MXCoreSessionSetProperty.cold.92
+ _MXCoreSessionSetProperty.cold.93
+ _MXCoreSessionSetProperty.cold.94
+ _MXCoreSessionSetProperty.cold.95
+ _MXCoreSessionSetProperty.cold.96
+ _MXCoreSessionSetProperty.cold.97
+ _MXCoreSessionSetProperty.cold.98
+ _MXCoreSessionSetProperty.cold.99
+ _MXDebugInstallSysdiagnoseBlock
+ _MXDispatchUtilityCreateOneShotTimer.cold.1
+ _MX_FeatureFlags_IsAirPlayDaemonEnabled.cold.1
+ _MX_FeatureFlags_IsAirPlayDaemonEnabled.isAirPlayDaemonEnabled
+ _MX_FeatureFlags_IsAirPlayDaemonEnabled.onceToken
+ _MX_FeatureFlags_IsAirPodsInEarRoutingWithCarsAndSpeakersEnabled
+ _MX_FeatureFlags_IsAirPodsInEarRoutingWithCarsAndSpeakersEnabled.cold.1
+ _MX_FeatureFlags_IsAirPodsInEarRoutingWithCarsAndSpeakersEnabled.isAirPodsInEarRoutingWithCarsAndSpeakersEnabled
+ _MX_FeatureFlags_IsAirPodsInEarRoutingWithCarsAndSpeakersEnabled.onceToken
+ _MX_FeatureFlags_IsAirPodsStudioVoiceMicEnabled
+ _MX_FeatureFlags_IsAirPodsStudioVoiceMicEnabled.cold.1
+ _MX_FeatureFlags_IsAirPodsStudioVoiceMicEnabled.onceToken
+ _MX_FeatureFlags_IsAirPodsStudioVoiceMicEnabled.sIsAirPodsStudioVoiceMicEnabled
+ _MX_FeatureFlags_IsCallConnectHapticsEnabled
+ _MX_FeatureFlags_IsCallConnectHapticsEnabled.cold.1
+ _MX_FeatureFlags_IsCallConnectHapticsEnabled.isCallConnectHapticsEnabled
+ _MX_FeatureFlags_IsCallConnectHapticsEnabled.onceToken
+ _MX_FeatureFlags_IsCustomizedRoutingWithCarsAndSpeakersEnabled
+ _MX_FeatureFlags_IsCustomizedRoutingWithCarsAndSpeakersEnabled.cold.1
+ _MX_FeatureFlags_IsCustomizedRoutingWithCarsAndSpeakersEnabled.isCustomizedRoutingWithCarsAndSpeakersEnabled
+ _MX_FeatureFlags_IsCustomizedRoutingWithCarsAndSpeakersEnabled.onceToken
+ _MX_FeatureFlags_IsHighQualityLocalRecordingEnabled
+ _MX_FeatureFlags_IsHighQualityLocalRecordingEnabled.cold.1
+ _MX_FeatureFlags_IsHighQualityLocalRecordingEnabled.onceToken
+ _MX_FeatureFlags_IsHighQualityLocalRecordingEnabled.sIsHighQualityLocalRecordingEnabled
+ _MX_FeatureFlags_IsInputAudioCoexistenceSupportEnabled
+ _MX_FeatureFlags_IsInputAudioCoexistenceSupportEnabled.cold.1
+ _MX_FeatureFlags_IsInputAudioCoexistenceSupportEnabled.isInputAudioCoexistenceSupportEnabled
+ _MX_FeatureFlags_IsInputAudioCoexistenceSupportEnabled.onceToken
+ _MX_FeatureFlags_IsMediaMultitaskingEnabled
+ _MX_FeatureFlags_IsMediaMultitaskingEnabled.cold.1
+ _MX_FeatureFlags_IsMediaMultitaskingEnabled.isMediaMultitaskingEnabled
+ _MX_FeatureFlags_IsMediaMultitaskingEnabled.onceToken
+ _MX_FeatureFlags_IsPersonalDevicesMediaVolumeUpdateEnabled
+ _MX_FeatureFlags_IsPersonalDevicesMediaVolumeUpdateEnabled.cold.1
+ _MX_FeatureFlags_IsPersonalDevicesMediaVolumeUpdateEnabled.onceToken
+ _MX_FeatureFlags_IsPersonalDevicesMediaVolumeUpdateEnabled.sIsPersonalDevicesMediaVolumeUpdateEnabled
+ _MX_FeatureFlags_IsRoutingContextReportingEnabled
+ _MX_FeatureFlags_IsRoutingContextReportingEnabled.cold.1
+ _MX_FeatureFlags_IsRoutingContextReportingEnabled.isRoutingContextReportingEnabled
+ _MX_FeatureFlags_IsRoutingContextReportingEnabled.onceToken
+ _MX_FeatureFlags_IsShortFormOutputMutingEnabled
+ _MX_FeatureFlags_IsShortFormOutputMutingEnabled.cold.1
+ _MX_FeatureFlags_IsShortFormOutputMutingEnabled.isShortFormOutputMutingEnabled
+ _MX_FeatureFlags_IsShortFormOutputMutingEnabled.onceToken
+ _MX_FeatureFlags_IsSynchronizeSiriAlarmVolumesToMediaVolumeEnabled
+ _MX_FeatureFlags_IsSynchronizeSiriAlarmVolumesToMediaVolumeEnabled.cold.1
+ _MX_FeatureFlags_IsSynchronizeSiriAlarmVolumesToMediaVolumeEnabled.onceToken
+ _MX_FeatureFlags_IsSynchronizeSiriAlarmVolumesToMediaVolumeEnabled.sIsSynchronizeSiriAlarmVolumesToMediaVolumeEnabled
+ _MX_FeatureFlags_IsWHAInstantDiscoveryCachingEnabled
+ _MX_FeatureFlags_IsWHAInstantDiscoveryCachingEnabled.cold.1
+ _MX_FeatureFlags_IsWHAInstantDiscoveryCachingEnabled.isWHAInstantDiscoveryCachingEnabled
+ _MX_FeatureFlags_IsWHAInstantDiscoveryCachingEnabled.onceToken
+ _OBJC_CLASS_$_AVSystemControllerCommon
+ _OBJC_CLASS_$_BTAudioRoutingRequest
+ _OBJC_CLASS_$_CRPairedVehicleManager
+ _OBJC_CLASS_$_MXAudioAccessoryServices
+ _OBJC_CLASS_$_MXConnectBannerResponseInfo
+ _OBJC_CLASS_$_MXCoreSessionIndependentAudioResource
+ _OBJC_CLASS_$_MXCoreSessionIndependentInputAudioResource
+ _OBJC_CLASS_$_MXFrontBoardServices
+ _OBJC_CLASS_$_MXRoutingContextModificationMetrics
+ _OBJC_CLASS_$_MXRoutingContextModificationResult
+ _OBJC_CLASS_$_MXRoutingContextReportingRTCServiceImpl
+ _OBJC_CLASS_$_MXRoutingContextReportingService
+ _OBJC_CLASS_$_MXSessionIndependentAudioResource
+ _OBJC_CLASS_$_MXSessionIndependentInputAudioResource
+ _OBJC_CLASS_$_MXSessionManagerIndependentAudioResource
+ _OBJC_CLASS_$_MXSystemSoundServices
+ _OBJC_CLASS_$_MXUIService_Client
+ _OBJC_CLASS_$_MXUndoBannerResponseInfo
+ _OBJC_CLASS_$_MXUserPreferredInputRouteCache
+ _OBJC_CLASS_$_MX_BannerManager
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_PDRRegistry
+ _OBJC_IVAR_$_AVSystemControllerCommon._selfWeak
+ _OBJC_IVAR_$_AVSystemControllerCommon.mFigController
+ _OBJC_IVAR_$_MXAudioAccessoryServices.mAudioRoutingRequest
+ _OBJC_IVAR_$_MXAudioAccessoryServices.mBTNotificationAudioRoutingChangedToken
+ _OBJC_IVAR_$_MXAudioAccessoryServices.mBTNotificationPreemptivePortChangedToken
+ _OBJC_IVAR_$_MXAudioAccessoryServices.mBTNotificationPreemptivePortDisconnectedToken
+ _OBJC_IVAR_$_MXAudioAccessoryServices.mDevicesState
+ _OBJC_IVAR_$_MXAudioAccessoryServices.mPortToDeviceAddressMapping
+ _OBJC_IVAR_$_MXAudioAccessoryServices.mSerialQueue
+ _OBJC_IVAR_$_MXConnectBannerResponseInfo._connectBannerResponse
+ _OBJC_IVAR_$_MXConnectBannerResponseInfo._routeSemaphore
+ _OBJC_IVAR_$_MXConnectBannerResponseInfo._txid
+ _OBJC_IVAR_$_MXCoreSession._isOutputMuted
+ _OBJC_IVAR_$_MXCoreSession._prefersBluetoothHighQualityContentCapture
+ _OBJC_IVAR_$_MXCoreSessionBase._allowsBluetoothRecordingCustomization
+ _OBJC_IVAR_$_MXCoreSessionBase._allowsDefaultBuiltInRouteCustomization
+ _OBJC_IVAR_$_MXCoreSessionBase._audioObjectID
+ _OBJC_IVAR_$_MXCoreSessionBase._bundleIdToPAAccessIntervalMap
+ _OBJC_IVAR_$_MXCoreSessionBase._defaultBuiltInRoutePreference
+ _OBJC_IVAR_$_MXCoreSessionBase._defaultBuiltInRoutePreferenceSetByClient
+ _OBJC_IVAR_$_MXCoreSessionBase._enableBluetoothRecordingPreferenceSetByClient
+ _OBJC_IVAR_$_MXCoreSessionBase._hasEntitlementToSuppressRecordingStateToSystemStatus
+ _OBJC_IVAR_$_MXCoreSessionBase._hasExternalMuteNotificationContext
+ _OBJC_IVAR_$_MXCoreSessionBase._idleSleepPreventor
+ _OBJC_IVAR_$_MXCoreSessionBase._idleSleepPreventorAllocated
+ _OBJC_IVAR_$_MXCoreSessionBase._idleSleepPreventorCreationTime
+ _OBJC_IVAR_$_MXCoreSessionBase._idleSleepPreventorName
+ _OBJC_IVAR_$_MXCoreSessionBase._idleSleepPreventorUpdaterTimer
+ _OBJC_IVAR_$_MXCoreSessionBase._isPlayingStartTime
+ _OBJC_IVAR_$_MXCoreSessionBase._isPlayingStopTime
+ _OBJC_IVAR_$_MXCoreSessionBase._isRecordingMuted
+ _OBJC_IVAR_$_MXCoreSessionBase._mode
+ _OBJC_IVAR_$_MXCoreSessionBase._mostRecentSessionInfoSetOnVA
+ _OBJC_IVAR_$_MXCoreSessionBase._playbackAssertionRef
+ _OBJC_IVAR_$_MXCoreSessionBase._preferredRouteControlFeatures
+ _OBJC_IVAR_$_MXCoreSessionBase._prefersEchoCancelledInput
+ _OBJC_IVAR_$_MXCoreSessionBase._prefersSuppressingRecordingState
+ _OBJC_IVAR_$_MXCoreSessionBase._resumeAssertionRef
+ _OBJC_IVAR_$_MXCoreSessionBase._resumeBackgroundAppUpdaterTimer
+ _OBJC_IVAR_$_MXCoreSessionBase._shadowingAudioSessionID
+ _OBJC_IVAR_$_MXCoreSessionBase._shadowingAudioSessionOptions
+ _OBJC_IVAR_$_MXCoreSessionBase._waitingToResume
+ _OBJC_IVAR_$_MXCoreSessionIndependentInputAudioResource.mMXSessionIndependentInputAudioResourceList
+ _OBJC_IVAR_$_MXCoreSessionIndependentInputAudioResource.mMXSessionIndependentInputAudioResourceListLock
+ _OBJC_IVAR_$_MXFrontBoardServices.mDisplayLayoutCache
+ _OBJC_IVAR_$_MXFrontBoardServices.mDisplayLayoutCacheLock
+ _OBJC_IVAR_$_MXFrontBoardServices.mFrontBoardServicesMonitor
+ _OBJC_IVAR_$_MXRoutingContextCallbackHelper.mCorrelationID
+ _OBJC_IVAR_$_MXRoutingContextCallbackHelper.mRoutingContextModificationMetrics
+ _OBJC_IVAR_$_MXRoutingContextModificationMetrics._clientModificationFinishedTimestamp
+ _OBJC_IVAR_$_MXRoutingContextModificationMetrics._clientModificationStartedTimestamp
+ _OBJC_IVAR_$_MXRoutingContextModificationMetrics._correlationID
+ _OBJC_IVAR_$_MXRoutingContextModificationMetrics._figEndpointType
+ _OBJC_IVAR_$_MXRoutingContextModificationMetrics._serverModificationFinishedTimestamp
+ _OBJC_IVAR_$_MXRoutingContextModificationMetrics._serverModificationStartedTimestamp
+ _OBJC_IVAR_$_MXRoutingContextModificationResult._modificationMetrics
+ _OBJC_IVAR_$_MXRoutingContextModificationResult._routeConfigUpdateReason
+ _OBJC_IVAR_$_MXRoutingContextReportingRTCServiceImpl.mConfigurationCondition
+ _OBJC_IVAR_$_MXRoutingContextReportingRTCServiceImpl.mConfigured
+ _OBJC_IVAR_$_MXRoutingContextReportingRTCServiceImpl.mRTCReporting
+ _OBJC_IVAR_$_MXRoutingContextReportingRTCServiceImpl.mWorkQueue
+ _OBJC_IVAR_$_MXRoutingContextReportingService._modificationMetrics
+ _OBJC_IVAR_$_MXRoutingContextReportingService.mReportingServiceImpl
+ _OBJC_IVAR_$_MXSession.mAudioTrackStatus
+ _OBJC_IVAR_$_MXSession.mIsPlayerMuted
+ _OBJC_IVAR_$_MXSession.mIsPlayingVideoOutput
+ _OBJC_IVAR_$_MXSessionIndependentAudioResource._audioToolboxIsPlaying
+ _OBJC_IVAR_$_MXSessionIndependentAudioResource._clientIsPlaying
+ _OBJC_IVAR_$_MXSessionIndependentAudioResource._isPlaying
+ _OBJC_IVAR_$_MXSessionIndependentAudioResource._isRecording
+ _OBJC_IVAR_$_MXSessionManager._isVoiceAssistantPlayingToPersonalAudioDeviceOverMedia
+ _OBJC_IVAR_$_MXSessionManager._someLongFormVideoClientIsActive
+ _OBJC_IVAR_$_MXSessionManagerIndependentAudioResource.mMXCoreSessionIndependentInputAudioResourceList
+ _OBJC_IVAR_$_MXSessionManagerIndependentAudioResource.mMXCoreSessionIndependentInputAudioResourceListLock
+ _OBJC_IVAR_$_MXSystemSoundServices._shouldPrivacyPongPlay
+ _OBJC_IVAR_$_MXSystemSoundServices.mSerialQueue
+ _OBJC_IVAR_$_MXUndoBannerResponseInfo._fromPorts
+ _OBJC_IVAR_$_MXUndoBannerResponseInfo._routeSemaphore
+ _OBJC_IVAR_$_MXUndoBannerResponseInfo._txid
+ _OBJC_IVAR_$_MXUndoBannerResponseInfo._undoBannerResponse
+ _OBJC_IVAR_$_MXUserPreferredInputRouteCache.mUserPreferredRouteCache
+ _OBJC_IVAR_$_MXUserPreferredInputRouteCache.mUserPreferredRouteCacheLock
+ _OBJC_IVAR_$_MX_BannerManager._connectBannerResponseCache
+ _OBJC_IVAR_$_MX_BannerManager._undoBannerResponseCache
+ _OBJC_METACLASS_$_AVSystemControllerCommon
+ _OBJC_METACLASS_$_MXAudioAccessoryServices
+ _OBJC_METACLASS_$_MXConnectBannerResponseInfo
+ _OBJC_METACLASS_$_MXCoreSessionIndependentAudioResource
+ _OBJC_METACLASS_$_MXCoreSessionIndependentInputAudioResource
+ _OBJC_METACLASS_$_MXFrontBoardServices
+ _OBJC_METACLASS_$_MXRoutingContextModificationMetrics
+ _OBJC_METACLASS_$_MXRoutingContextModificationResult
+ _OBJC_METACLASS_$_MXRoutingContextReportingRTCServiceImpl
+ _OBJC_METACLASS_$_MXRoutingContextReportingService
+ _OBJC_METACLASS_$_MXSessionIndependentAudioResource
+ _OBJC_METACLASS_$_MXSessionIndependentInputAudioResource
+ _OBJC_METACLASS_$_MXSessionManagerIndependentAudioResource
+ _OBJC_METACLASS_$_MXSystemSoundServices
+ _OBJC_METACLASS_$_MXUndoBannerResponseInfo
+ _OBJC_METACLASS_$_MXUserPreferredInputRouteCache
+ _OBJC_METACLASS_$_MX_BannerManager
+ _OUTLINED_FUNCTION_41
+ _OUTLINED_FUNCTION_42
+ _OUTLINED_FUNCTION_43
+ _OUTLINED_FUNCTION_44
+ _OUTLINED_FUNCTION_45
+ _OUTLINED_FUNCTION_46
+ _OUTLINED_FUNCTION_47
+ _OUTLINED_FUNCTION_48
+ _OUTLINED_FUNCTION_49
+ _OUTLINED_FUNCTION_50
+ _OUTLINED_FUNCTION_51
+ _OUTLINED_FUNCTION_52
+ _OUTLINED_FUNCTION_53
+ _OUTLINED_FUNCTION_54
+ _OUTLINED_FUNCTION_55
+ _OUTLINED_FUNCTION_56
+ _OUTLINED_FUNCTION_57
+ _OUTLINED_FUNCTION_58
+ _OUTLINED_FUNCTION_59
+ _OUTLINED_FUNCTION_60
+ _OUTLINED_FUNCTION_61
+ _OUTLINED_FUNCTION_62
+ _OUTLINED_FUNCTION_63
+ _OUTLINED_FUNCTION_64
+ _OUTLINED_FUNCTION_65
+ _OUTLINED_FUNCTION_66
+ _OUTLINED_FUNCTION_67
+ _OUTLINED_FUNCTION_68
+ _OUTLINED_FUNCTION_69
+ _OUTLINED_FUNCTION_70
+ _OUTLINED_FUNCTION_71
+ _OUTLINED_FUNCTION_72
+ _OUTLINED_FUNCTION_73
+ _OUTLINED_FUNCTION_74
+ _OUTLINED_FUNCTION_75
+ _OUTLINED_FUNCTION_76
+ _OUTLINED_FUNCTION_77
+ _OUTLINED_FUNCTION_78
+ _OUTLINED_FUNCTION_79
+ _OUTLINED_FUNCTION_80
+ _OUTLINED_FUNCTION_81
+ _OUTLINED_FUNCTION_82
+ _OUTLINED_FUNCTION_83
+ _OUTLINED_FUNCTION_84
+ _OUTLINED_FUNCTION_85
+ _OUTLINED_FUNCTION_86
+ _OUTLINED_FUNCTION_87
+ _OUTLINED_FUNCTION_88
+ _OUTLINED_FUNCTION_89
+ _OUTLINED_FUNCTION_90
+ _OUTLINED_FUNCTION_91
+ _PVMAreTwoRoutesIdentical
+ _PVMComputeSynchronizedVolume
+ _PVMCopyEndpointDisconnectionTimeInfo
+ _PVMGetMostRecentSynchronizedVolumeActivityTimestamp
+ _PVMGetPersonalAudioDevicesMediaVolumeResetTimerDuration
+ _PVMGetSynchronizedVolumeResetTimerDuration
+ _PVMIsRoutedToAPersonalAudioDevice
+ _PVMSaveEndpointDisconnectionTimeInfo
+ _PVMSetMostRecentSynchronizedVolumeActivityTimestamp
+ _RTCReportingLibrary
+ _RTCReportingLibraryCore.frameworkLibrary
+ _TEMP_kFigEndpointCentralNotification_CarEntityHasScreenForAirPlayVideo
+ __FigEndpointCentralCopyProperty
+ __FigEndpointCentralEntityHoldsResource.cold.1
+ __FigEndpointCentralEntityHoldsResource.cold.2
+ __FigEndpointCentralEntityHoldsResource.cold.3
+ __FigEndpointCentralGetEntityDoingActivity.cold.1
+ __OBJC_$_CLASS_METHODS_AVSystemController
+ __OBJC_$_CLASS_METHODS_AVSystemControllerCommon
+ __OBJC_$_CLASS_METHODS_MXAudioAccessoryServices
+ __OBJC_$_CLASS_METHODS_MXFrontBoardServices
+ __OBJC_$_CLASS_METHODS_MXSessionIndependentInputAudioResource
+ __OBJC_$_CLASS_METHODS_MXSessionManagerBase
+ __OBJC_$_CLASS_METHODS_MXSessionManagerIndependentAudioResource
+ __OBJC_$_CLASS_METHODS_MXSystemSoundServices
+ __OBJC_$_CLASS_METHODS_MXUserPreferredInputRouteCache
+ __OBJC_$_CLASS_METHODS_MX_BannerManager
+ __OBJC_$_CLASS_PROP_LIST_MXSystemController
+ __OBJC_$_INSTANCE_METHODS_AVSystemControllerCommon
+ __OBJC_$_INSTANCE_METHODS_MXAudioAccessoryServices
+ __OBJC_$_INSTANCE_METHODS_MXConnectBannerResponseInfo
+ __OBJC_$_INSTANCE_METHODS_MXCoreSession(Utilities)
+ __OBJC_$_INSTANCE_METHODS_MXCoreSessionIndependentAudioResource
+ __OBJC_$_INSTANCE_METHODS_MXCoreSessionIndependentInputAudioResource
+ __OBJC_$_INSTANCE_METHODS_MXFrontBoardServices
+ __OBJC_$_INSTANCE_METHODS_MXRoutingContextModificationMetrics
+ __OBJC_$_INSTANCE_METHODS_MXRoutingContextModificationResult
+ __OBJC_$_INSTANCE_METHODS_MXRoutingContextReportingRTCServiceImpl
+ __OBJC_$_INSTANCE_METHODS_MXRoutingContextReportingService
+ __OBJC_$_INSTANCE_METHODS_MXSessionIndependentAudioResource
+ __OBJC_$_INSTANCE_METHODS_MXSessionIndependentInputAudioResource
+ __OBJC_$_INSTANCE_METHODS_MXSessionManager(InterruptionActionMapper|DuckingUtilities|MXSessionManagerContinuityScreenOutputPortUtilities|Common|VAUtilities|Utilities|ActivationUtilities)
+ __OBJC_$_INSTANCE_METHODS_MXSessionManagerIndependentAudioResource
+ __OBJC_$_INSTANCE_METHODS_MXSystemSoundServices
+ __OBJC_$_INSTANCE_METHODS_MXUndoBannerResponseInfo
+ __OBJC_$_INSTANCE_METHODS_MXUserPreferredInputRouteCache
+ __OBJC_$_INSTANCE_METHODS_MXVolumeManager(Internal)
+ __OBJC_$_INSTANCE_METHODS_MX_BannerManager
+ __OBJC_$_INSTANCE_VARIABLES_AVSystemControllerCommon
+ __OBJC_$_INSTANCE_VARIABLES_MXAudioAccessoryServices
+ __OBJC_$_INSTANCE_VARIABLES_MXConnectBannerResponseInfo
+ __OBJC_$_INSTANCE_VARIABLES_MXCoreSessionIndependentInputAudioResource
+ __OBJC_$_INSTANCE_VARIABLES_MXFrontBoardServices
+ __OBJC_$_INSTANCE_VARIABLES_MXRoutingContextModificationMetrics
+ __OBJC_$_INSTANCE_VARIABLES_MXRoutingContextModificationResult
+ __OBJC_$_INSTANCE_VARIABLES_MXRoutingContextReportingRTCServiceImpl
+ __OBJC_$_INSTANCE_VARIABLES_MXRoutingContextReportingService
+ __OBJC_$_INSTANCE_VARIABLES_MXSessionIndependentAudioResource
+ __OBJC_$_INSTANCE_VARIABLES_MXSessionManagerIndependentAudioResource
+ __OBJC_$_INSTANCE_VARIABLES_MXSystemSoundServices
+ __OBJC_$_INSTANCE_VARIABLES_MXUndoBannerResponseInfo
+ __OBJC_$_INSTANCE_VARIABLES_MXUserPreferredInputRouteCache
+ __OBJC_$_INSTANCE_VARIABLES_MX_BannerManager
+ __OBJC_$_PROP_LIST_AVSystemControllerCommon
+ __OBJC_$_PROP_LIST_MXConnectBannerResponseInfo
+ __OBJC_$_PROP_LIST_MXRoutingContextModificationMetrics
+ __OBJC_$_PROP_LIST_MXRoutingContextModificationResult
+ __OBJC_$_PROP_LIST_MXRoutingContextReportingRTCServiceImpl
+ __OBJC_$_PROP_LIST_MXRoutingContextReportingService
+ __OBJC_$_PROP_LIST_MXSessionIndependentAudioResource
+ __OBJC_$_PROP_LIST_MXSystemSoundServices
+ __OBJC_$_PROP_LIST_MXUndoBannerResponseInfo
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MXRoutingContextReportingServiceImpl
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MXRoutingContextReportingServiceImpl
+ __OBJC_$_PROTOCOL_REFS_MXRoutingContextReportingServiceImpl
+ __OBJC_CLASS_PROTOCOLS_$_MXRoutingContextReportingRTCServiceImpl
+ __OBJC_CLASS_RO_$_AVSystemControllerCommon
+ __OBJC_CLASS_RO_$_MXAudioAccessoryServices
+ __OBJC_CLASS_RO_$_MXConnectBannerResponseInfo
+ __OBJC_CLASS_RO_$_MXCoreSessionIndependentAudioResource
+ __OBJC_CLASS_RO_$_MXCoreSessionIndependentInputAudioResource
+ __OBJC_CLASS_RO_$_MXFrontBoardServices
+ __OBJC_CLASS_RO_$_MXRoutingContextModificationMetrics
+ __OBJC_CLASS_RO_$_MXRoutingContextModificationResult
+ __OBJC_CLASS_RO_$_MXRoutingContextReportingRTCServiceImpl
+ __OBJC_CLASS_RO_$_MXRoutingContextReportingService
+ __OBJC_CLASS_RO_$_MXSessionIndependentAudioResource
+ __OBJC_CLASS_RO_$_MXSessionIndependentInputAudioResource
+ __OBJC_CLASS_RO_$_MXSessionManagerIndependentAudioResource
+ __OBJC_CLASS_RO_$_MXSystemSoundServices
+ __OBJC_CLASS_RO_$_MXUndoBannerResponseInfo
+ __OBJC_CLASS_RO_$_MXUserPreferredInputRouteCache
+ __OBJC_CLASS_RO_$_MX_BannerManager
+ __OBJC_LABEL_PROTOCOL_$_MXRoutingContextReportingServiceImpl
+ __OBJC_METACLASS_RO_$_AVSystemControllerCommon
+ __OBJC_METACLASS_RO_$_MXAudioAccessoryServices
+ __OBJC_METACLASS_RO_$_MXConnectBannerResponseInfo
+ __OBJC_METACLASS_RO_$_MXCoreSessionIndependentAudioResource
+ __OBJC_METACLASS_RO_$_MXCoreSessionIndependentInputAudioResource
+ __OBJC_METACLASS_RO_$_MXFrontBoardServices
+ __OBJC_METACLASS_RO_$_MXRoutingContextModificationMetrics
+ __OBJC_METACLASS_RO_$_MXRoutingContextModificationResult
+ __OBJC_METACLASS_RO_$_MXRoutingContextReportingRTCServiceImpl
+ __OBJC_METACLASS_RO_$_MXRoutingContextReportingService
+ __OBJC_METACLASS_RO_$_MXSessionIndependentAudioResource
+ __OBJC_METACLASS_RO_$_MXSessionIndependentInputAudioResource
+ __OBJC_METACLASS_RO_$_MXSessionManagerIndependentAudioResource
+ __OBJC_METACLASS_RO_$_MXSystemSoundServices
+ __OBJC_METACLASS_RO_$_MXUndoBannerResponseInfo
+ __OBJC_METACLASS_RO_$_MXUserPreferredInputRouteCache
+ __OBJC_METACLASS_RO_$_MX_BannerManager
+ __OBJC_PROTOCOL_$_MXRoutingContextReportingServiceImpl
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorI11VARouteInfoEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorI12CMSRouteInfoEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__16vectorI11VARouteInfoNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorI12CMSRouteInfoNS_9allocatorIS1_EEE20__throw_length_errorB8ne200100Ev
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ ___108-[MXRoutingContextCallbackHelper initWithRoutingContext:routeConfigUpdateID:correlationID:callback:context:]_block_invoke
+ ___138-[MX_BannerManager promptUserResponseForUndoRoute:newPortIdentifier:newPortName:newPortID:newPortType:oldPort:routingContext:undoHandler:]_block_invoke
+ ___138-[MX_BannerManager promptUserResponseForUndoRoute:newPortIdentifier:newPortName:newPortID:newPortType:oldPort:routingContext:undoHandler:]_block_invoke_2
+ ___164-[MXSessionManagerIndependentAudioResource postInterruptionCommandNotification:interruptionCommand:interruptorName:interruptorBundleID:status:volumeChangeDuration:]_block_invoke
+ ___173-[MX_BannerManager promptUserResponseForRoute:newPortIdentifier:newPortName:newPortID:newPortType:newWirelessPorts:oldPort:activatingEndpoint:routingContext:connectHandler:]_block_invoke
+ ___173-[MX_BannerManager promptUserResponseForRoute:newPortIdentifier:newPortName:newPortID:newPortType:newWirelessPorts:oldPort:activatingEndpoint:routingContext:connectHandler:]_block_invoke.76
+ ___173-[MX_BannerManager promptUserResponseForRoute:newPortIdentifier:newPortName:newPortID:newPortType:newWirelessPorts:oldPort:activatingEndpoint:routingContext:connectHandler:]_block_invoke_2
+ ___173-[MX_BannerManager promptUserResponseForRoute:newPortIdentifier:newPortName:newPortID:newPortType:newWirelessPorts:oldPort:activatingEndpoint:routingContext:connectHandler:]_block_invoke_2.81
+ ___28-[MXFrontBoardServices init]_block_invoke
+ ___28-[MXFrontBoardServices init]_block_invoke_2
+ ___32-[MXAudioAccessoryServices init]_block_invoke
+ ___32-[MXAudioAccessoryServices init]_block_invoke_2
+ ___32-[MXAudioAccessoryServices init]_block_invoke_3
+ ___32-[MXAudioAccessoryServices init]_block_invoke_4
+ ___34+[MX_BannerManager sharedInstance]_block_invoke
+ ___38+[MXFrontBoardServices sharedInstance]_block_invoke
+ ___39+[MXSystemSoundServices sharedInstance]_block_invoke
+ ___41+[MX_BannerManager getSharedBannerClient]_block_invoke
+ ___41-[MXAudioAccessoryServices dumpDebugInfo]_block_invoke
+ ___42+[MXAudioAccessoryServices sharedInstance]_block_invoke
+ ___42-[MXAudioAccessoryServices isPortManaged:]_block_invoke
+ ___44+[MX_BannerManager getAwaitingDispatchQueue]_block_invoke
+ ___45-[MXAudioAccessoryServices handleServerDeath]_block_invoke
+ ___45-[MXCoreSessionBase removeSessionAudioObject]_block_invoke
+ ___45-[MXSystemSoundServices playPrivacyPongSound]_block_invoke
+ ___47-[MXCoreSessionSecure setPropertyForKey:value:]_block_invoke
+ ___48+[MXUserPreferredInputRouteCache sharedInstance]_block_invoke
+ ___50-[MXAudioAccessoryServices clearDevicesStateCache]_block_invoke
+ ___51-[MXAudioAccessoryServices handlePortDisconnected:]_block_invoke
+ ___53-[MXCoreSessionBase postSessionNotification:payload:]_block_invoke
+ ___54-[MXMediaEndowmentManager getHostProcessAttributions:]_block_invoke
+ ___55-[MXAudioAccessoryServices isAnyManagedDeviceConnected]_block_invoke
+ ___57-[MXAudioAccessoryServices copyDeviceAddressFromVADPort:]_block_invoke
+ ___57-[MXSessionManager(Utilities) updateMuteState:muteValue:]_block_invoke.27
+ ___57-[MXSystemSoundServices playSystemSound:completionBlock:]_block_invoke
+ ___58+[MXEndpointDescriptorCache getConnectBannerResponseCache]_block_invoke
+ ___58+[MXSessionManagerIndependentAudioResource sharedInstance]_block_invoke
+ ___59-[MXAudioAccessoryServices handleNewWirelessPortConnected:]_block_invoke
+ ___62+[MXSessionManagerBase setGreenTeaLoggerRecordingState:state:]_block_invoke
+ ___63-[MXAudioAccessoryServices updateDeviceManagementState:reason:]_block_invoke
+ ___63-[MXAudioAccessoryServices updateDeviceManagementState:reason:]_block_invoke_2
+ ___65-[AVSystemControllerCommon initializeAttributeForKeyMappingToFig]_block_invoke
+ ___66-[MXRoutingContextReportingRTCServiceImpl sendModificationResult:]_block_invoke
+ ___66-[MXRoutingContextReportingRTCServiceImpl sendModificationResult:]_block_invoke.cold.1
+ ___66-[MXRoutingContextReportingRTCServiceImpl sendModificationResult:]_block_invoke.cold.2
+ ___66-[MXRoutingContextReportingRTCServiceImpl sendModificationResult:]_block_invoke.cold.3
+ ___67-[MXRoutingContextReportingRTCServiceImpl initWithFigEndpointType:]_block_invoke
+ ___68-[MXAudioAccessoryServices hijackWirelessPort:reason:portWentInEar:]_block_invoke
+ ___68-[MXAudioAccessoryServices hijackWirelessPort:reason:portWentInEar:]_block_invoke_2
+ ___70-[MXCoreSessionIndependentInputAudioResource setPropertyForKey:value:]_block_invoke
+ ___76+[AVSystemControllerCommon postNotificationOnMainQueue:notification:object:]_block_invoke
+ ___77-[MXAudioAccessoryServices copyPreferredDeviceAddress:andPreemptivePortInfo:]_block_invoke
+ ___77-[MXAudioAccessoryServices copyPreferredDeviceAddress:andPreemptivePortInfo:]_block_invoke_2
+ ___79-[MXCoreSessionBase processOnDemandVADLossIfNeeded:isPreviousInputVADOnDemand:]_block_invoke
+ ___83-[MXEndpointDescriptorCache _availableEndpointsDidChangeForEndpointManager:atDate:]_block_invoke.27
+ ___86-[MXSessionManager(Utilities) updateBluetoothFrameworkToPlayMuteChime:playRejectTone:]_block_invoke.46
+ ___86-[MXSessionManager(Utilities) updateBluetoothFrameworkToPlayMuteChime:playRejectTone:]_block_invoke_2.47
+ ___91-[MXAudioAccessoryServices copyPreferredDeviceAddress:bundleID:isHypotheticalQuery:reason:]_block_invoke
+ ___CMSMAP_StartRouteAwayFromAirPlayHandoffTimer_block_invoke.8
+ ___CMSMDeviceState_Initialize_block_invoke
+ ___CMSMDeviceState_SupportsMediaMultitasking_block_invoke
+ ___CMSMDeviceState_SupportsShortFormOutputMutingAudioPolicy_block_invoke
+ ___CMSMNotificationUtility_PostIsOutputMutedDidChange_block_invoke
+ ___CMSMNotificationUtility_PostNowPlayingAppIsPlayingDidChange_block_invoke.21
+ ___CMSMNotificationUtility_PostUserIntentToUnmuteDidChange_block_invoke
+ ___CMSMSleep_HandleIdleSleep_block_invoke
+ ___CMSMSleep_HandleIdleSleep_block_invoke_2
+ ___FigRoutingContextResilientRemoteCopyContextForUUID_block_invoke.7
+ ___FigRoutingContextResilientRemoteCopySystemAudioInputContext_block_invoke
+ ___FigRoutingContextResilientRemoteCopySystemAudioInputContext_block_invoke_2
+ ___FigRoutingContextUtilities_LogCurrentState_block_invoke
+ ___FigRoutingManagerContextUtilities_AddCurrentlyActivatingEndpoint_block_invoke.35
+ ___FigRoutingManagerContextUtilities_RemoveContext_block_invoke.67
+ ___FigRoutingManagerProcessAirPodsInEarRouting_block_invoke
+ ___FigRoutingManagerProcessAirPodsInEarRouting_block_invoke.50
+ ___FigRoutingManagerStartCarPlayAudioMainPortPublishingCheckTimer_block_invoke.4
+ ___FigRoutingManagerStartDeactivateAirPlayEndpointTimer_block_invoke.64
+ ___MXCoreSessionSetProperty_block_invoke.175
+ ___MXCoreSessionSetProperty_block_invoke.180
+ ___MXCoreSessionSetProperty_block_invoke.232
+ ___MXCoreSessionSetProperty_block_invoke.288
+ ___MXDispatchUtilityCreateOneShotTimer_block_invoke
+ ___MXDispatchUtilityCreateOneShotTimer_block_invoke.cold.1
+ ___MXDispatchUtilityCreateOneShotTimer_block_invoke.cold.2
+ ___MX_FeatureFlags_IsAirPlayDaemonEnabled_block_invoke
+ ___MX_FeatureFlags_IsAirPodsInEarRoutingWithCarsAndSpeakersEnabled_block_invoke
+ ___MX_FeatureFlags_IsAirPodsStudioVoiceMicEnabled_block_invoke
+ ___MX_FeatureFlags_IsCallConnectHapticsEnabled_block_invoke
+ ___MX_FeatureFlags_IsCustomizedRoutingWithCarsAndSpeakersEnabled_block_invoke
+ ___MX_FeatureFlags_IsHighQualityLocalRecordingEnabled_block_invoke
+ ___MX_FeatureFlags_IsInputAudioCoexistenceSupportEnabled_block_invoke
+ ___MX_FeatureFlags_IsMediaMultitaskingEnabled_block_invoke
+ ___MX_FeatureFlags_IsPersonalDevicesMediaVolumeUpdateEnabled_block_invoke
+ ___MX_FeatureFlags_IsRoutingContextReportingEnabled_block_invoke
+ ___MX_FeatureFlags_IsShortFormOutputMutingEnabled_block_invoke
+ ___MX_FeatureFlags_IsSynchronizeSiriAlarmVolumesToMediaVolumeEnabled_block_invoke
+ ___MX_FeatureFlags_IsWHAInstantDiscoveryCachingEnabled_block_invoke
+ ___PowerManager_InitializeCPMSForAudio_block_invoke.3
+ ___PowerManager_InitializeCPMSForAudio_block_invoke_2.7
+ ___PowerManager_InitializeCPMSForHaptics_block_invoke.3
+ ___PowerManager_InitializeCPMSForHaptics_block_invoke_2.7
+ ___RTCReportingLibraryCore_block_invoke
+ ___block_descriptor_112_e8_32o40o48b56r64r_e20_v20?0i8"NSError"12lr56l8s32l8s40l8s48l8r64l8
+ ___block_descriptor_112_e8_32o40o48b56r_e5_v8?0ls32l8s40l8s48l8r56l8
+ ___block_descriptor_32_e41_i16?0^{OpaqueFigRoutingSessionManager=}8l
+ ___block_descriptor_32_e60_i24?0^{__CFAllocator=}8^^{OpaqueFigRoutingSessionManager}16l
+ ___block_descriptor_36_e82_v40?0^{__CFArray=}8^{OpaqueFigEndpoint=}16^{OpaqueFigEndpoint=}24^{__CFString=}32l
+ ___block_descriptor_40_e41_i16?0^{OpaqueFigRoutingSessionManager=}8l
+ ___block_descriptor_40_e8_32w_e17_v16?0"NSArray"8lw32l8
+ ___block_descriptor_44_e8_32b_e5_v8?0ls32l8
+ ___block_descriptor_44_e8_32r_e32_v16?0"BTAudioRoutingResponse"8lr32l8
+ ___block_descriptor_44_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e41_i16?0^{OpaqueFigRoutingSessionManager=}8l
+ ___block_descriptor_48_e8_32o40o_e32_v16?0"BTAudioRoutingResponse"8ls32l8s40l8
+ ___block_descriptor_48_e8_32r40r_e32_v16?0"BTAudioRoutingResponse"8lr32l8r40l8
+ ___block_descriptor_52_e51_v32?0^{__CFArray=}8^{__CFArray=}16^{__CFString=}24l
+ ___block_descriptor_52_e5_v8?0l
+ ___block_descriptor_52_e8_32o40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_52_e8_32r40r_e32_v16?0"BTAudioRoutingResponse"8lr32l8r40l8
+ ___block_descriptor_56_e8_32o40o48o_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32o40r48r_e5_v8?0ls32l8r40l8r48l8
+ ___block_descriptor_56_e8_32r40r48r_e5_v8?0lr32l8r40l8r48l8
+ ___block_descriptor_64_e8_32o40b_e5_v8?0ls40l8s32l8
+ ___block_descriptor_64_e8_32r40r48r_e5_v8?0lr32l8r40l8r48l8
+ ___block_descriptor_68_e8_32o40o48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_77_e8_32r40r_e5_v8?0lr32l8r40l8
+ ___block_descriptor_80_e8_32b_e5_v8?0ls32l8
+ ___block_descriptor_80_e8_32o40o48r56r_e5_v8?0lr48l8s32l8s40l8r56l8
+ ___block_descriptor_84_e8_32o40o48o56o64r_e5_v8?0ls32l8s40l8s48l8s56l8r64l8
+ ___block_descriptor_88_e8_32o40o48b56r64r_e20_v20?0i8"NSError"12lr56l8s32l8s40l8s48l8r64l8
+ ___block_literal_global.100
+ ___block_literal_global.107
+ ___block_literal_global.110
+ ___block_literal_global.113
+ ___block_literal_global.118
+ ___block_literal_global.121
+ ___block_literal_global.125
+ ___block_literal_global.128
+ ___block_literal_global.13
+ ___block_literal_global.131
+ ___block_literal_global.134
+ ___block_literal_global.137
+ ___block_literal_global.140
+ ___block_literal_global.143
+ ___block_literal_global.144
+ ___block_literal_global.148
+ ___block_literal_global.159
+ ___block_literal_global.162
+ ___block_literal_global.165
+ ___block_literal_global.167
+ ___block_literal_global.168
+ ___block_literal_global.171
+ ___block_literal_global.174
+ ___block_literal_global.177
+ ___block_literal_global.180
+ ___block_literal_global.182
+ ___block_literal_global.183
+ ___block_literal_global.190
+ ___block_literal_global.20
+ ___block_literal_global.201
+ ___block_literal_global.204
+ ___block_literal_global.211
+ ___block_literal_global.23
+ ___block_literal_global.25
+ ___block_literal_global.252
+ ___block_literal_global.253
+ ___block_literal_global.255
+ ___block_literal_global.278
+ ___block_literal_global.281
+ ___block_literal_global.3
+ ___block_literal_global.30
+ ___block_literal_global.317
+ ___block_literal_global.32
+ ___block_literal_global.399
+ ___block_literal_global.42
+ ___block_literal_global.425
+ ___block_literal_global.44
+ ___block_literal_global.443
+ ___block_literal_global.445
+ ___block_literal_global.467
+ ___block_literal_global.51
+ ___block_literal_global.524
+ ___block_literal_global.535
+ ___block_literal_global.54
+ ___block_literal_global.56
+ ___block_literal_global.577
+ ___block_literal_global.58
+ ___block_literal_global.586
+ ___block_literal_global.59
+ ___block_literal_global.590
+ ___block_literal_global.595
+ ___block_literal_global.61
+ ___block_literal_global.70
+ ___block_literal_global.73
+ ___block_literal_global.744
+ ___block_literal_global.79
+ ___block_literal_global.82
+ ___block_literal_global.84
+ ___block_literal_global.85
+ ___block_literal_global.87
+ ___block_literal_global.89
+ ___block_literal_global.94
+ ___block_literal_global.97
+ ___central_deactivateEndpoint_block_invoke
+ ___central_deactivateEndpoint_block_invoke_2
+ ___cmsSetIsActive_block_invoke.136
+ ___cmsSetIsPlaying_block_invoke.153
+ ___cmsmInitializeCMSessionManager_block_invoke.34
+ ___cmsmInitializeCMSessionManager_block_invoke.49
+ ___cmsmInitializeCMSessionManager_block_invoke_2.40
+ ___cmsmInitializeCMSessionManager_block_invoke_2.52
+ ___cmsmScreenIsBlankedChangedCallback_block_invoke.584
+ ___discoverer_SetProperty_block_invoke_2.55
+ ___discoverer_SetProperty_block_invoke_2.57
+ ___getRTCReportingClass_block_invoke
+ ___getRTCReportingClass_block_invoke.cold.1
+ ___getkRTCReportingMessageParametersCategorySymbolLoc_block_invoke
+ ___getkRTCReportingMessageParametersPayloadSymbolLoc_block_invoke
+ ___getkRTCReportingMessageParametersTypeSymbolLoc_block_invoke
+ ___getkRTCReportingSessionInfoBatchEventSymbolLoc_block_invoke
+ ___getkRTCReportingSessionInfoClientBundleIDSymbolLoc_block_invoke
+ ___getkRTCReportingSessionInfoClientTypeSymbolLoc_block_invoke
+ ___getkRTCReportingSessionInfoClientVersionSymbolLoc_block_invoke
+ ___getkRTCReportingSessionInfoSessionIDSymbolLoc_block_invoke
+ ___getkRTCReportingUserInfoClientNameSymbolLoc_block_invoke
+ ___getkRTCReportingUserInfoServiceNameSymbolLoc_block_invoke
+ ___getnw_path_uses_interface_typeSymbolLoc_block_invoke
+ ___routingContextResilientRemote_ReportModificationMetrics_block_invoke
+ ___routingContext_CopyPredictedSelectedRouteDescriptor_block_invoke.45
+ ___routingManager_createMXSessionForCarPlay_block_invoke
+ ___routingSessionManager_PrepareForPlayback_block_invoke.117
+ ___routingSessionManager_StartSessionWithRouteDescriptors_block_invoke.241
+ ___routingSessionManager_StartSessionWithRouteDescriptors_block_invoke_2.242
+ ___routingSessionManager_UpdateCurrentSessionFromLikelyDestinations_block_invoke.184
+ ___routingSessionManager_findTopAvailablePredictedDestination_block_invoke.214
+ ___routingSessionManager_loadAirPlayRoutePredictionFramework_block_invoke.cold.10
+ ___routingSessionManager_loadAirPlayRoutePredictionFramework_block_invoke.cold.11
+ ___routingSessionManager_loadAirPlayRoutePredictionFramework_block_invoke.cold.12
+ ___routingSessionManager_loadAirPlayRoutePredictionFramework_block_invoke.cold.13
+ ___routingSessionManager_loadAirPlayRoutePredictionFramework_block_invoke.cold.2
+ ___routingSessionManager_loadAirPlayRoutePredictionFramework_block_invoke.cold.3
+ ___routingSessionManager_loadAirPlayRoutePredictionFramework_block_invoke.cold.4
+ ___routingSessionManager_loadAirPlayRoutePredictionFramework_block_invoke.cold.5
+ ___routingSessionManager_loadAirPlayRoutePredictionFramework_block_invoke.cold.6
+ ___routingSessionManager_loadAirPlayRoutePredictionFramework_block_invoke.cold.7
+ ___routingSessionManager_loadAirPlayRoutePredictionFramework_block_invoke.cold.8
+ ___routingSessionManager_loadAirPlayRoutePredictionFramework_block_invoke.cold.9
+ ___routingSessionManager_routeToDestinationOfCurrentSession_block_invoke.126
+ ___routingSessionManager_setDestinationOnRoutingContext_block_invoke.165
+ ___routingSessionManager_setDestinationOnRoutingContext_block_invoke.167
+ ___routingSessionManager_startDiscovery_block_invoke.136
+ ___routingSessionManager_updatePredictedDestinations_block_invoke.301
+ ___routingSessionManager_waitForRecentPredictions_block_invoke.202
+ ___routingSessionManager_waitForRecentPredictions_block_invoke.203
+ ___routingSessionManager_waitForRecentPredictions_block_invoke.205
+ ___vaemCurrentRouteHasVolumeControlListener_block_invoke.163
+ ___vaemInitializePortEndpointCache_block_invoke
+ ___vaemSessionRoutingInfoChangeListener_block_invoke
+ ___vaemUpdateSharedAudioRouteState_block_invoke.83
+ __central_CopyProperty
+ _arc4random
+ _audit_stringRTCReporting
+ _bannerResponseCacheMutex
+ _central_HandleCarModeStateChange
+ _central_deactivateEndpoint
+ _central_requestCarModeChange.cold.1
+ _central_requestCarModeChange.cold.2
+ _cmsToggleMuted
+ _cmsmCreatePickableRoutesForRouteConfiguration
+ _cmsmDefaultVADToSystemSoundVADVolumeRatioForCurrentSystemSoundVADRoute
+ _cmsmInitializeCMSessionManager.cold.1
+ _cmsmInitializeCMSessionManager.cold.2
+ _cmsmInitializeCMSessionManager.cold.3
+ _cmsmInitializeCMSessionManager.cold.4
+ _cmsmInitializeLogging.onceToken
+ _cmsmLoadAudioStatisticsRoutines.once
+ _cmsmLoadClusterSyncMgrRoutines.once
+ _cmsmShouldUpdateMostRecentSynchronizedVolumeActivityTimestamp
+ _cmsmSystemSoundMustBeHeard
+ _cmsmUnrouteAllInputRoutes
+ _cmsmUpdateInEarBasedPlaybackState.sAudioPausedOnBudsOutOfEar
+ _cmsmUpdateInEarBasedPlaybackState.sAudioRouteInEarStatus
+ _cmsmUpdateInEarBasedPlaybackState.sNowPlayingDisplayIDWhenPaused
+ _cmsmUpdateInEarBasedPlaybackState.sPortForWhichLastUpdateWasReceived
+ _cmsmUpdateInEarBasedPlaybackState.sTimestampWhenNoBudWasInEar
+ _cmsmdevicestate_DeviceIsLocked
+ _cmsmdevicestate_RegisterForNotifydStyleNotification
+ _cmsmdevicestate_ScreenIsBlanked
+ _cmsmdevicestate_ScreenIsBlankedByProximitySensor
+ _discoveryManager_resetSwitchDownTime
+ _dispatch_queue_attr_make_with_qos_class
+ _dlopenHelper$AudioAccessoryServices
+ _dlopenHelperFlag$AudioAccessoryServices
+ _fsm_requestResourceModeChangeBorrow
+ _fsm_requestResourceModeChangeTake
+ _fvGetVibeSynthIsAvailableOnce
+ _gAudioDeviceStartNotifyToken
+ _gDefaultVolumeCategory
+ _gFBSDisplayLayoutMonitorClass
+ _gFBSDisplayLayoutMonitorConfigurationClass
+ _gFigEndpointUIAgentXPCRemoteTrace
+ _gFigRSSTrace
+ _gFigRouteDiscovererXPCServerTrace
+ _gFigRoutingContextResilientRemoteTrace
+ _gFigRoutingContextXPCRemoteTrace
+ _gFigRoutingContextXPCServerTrace
+ _gFigRoutingSessionManagerXPCRemoteTrace
+ _gFigRoutingSessionManagerXPCServerTrace
+ _gFigStarkModeControllerRemoteClient
+ _gFigSystemControllerRemoteClient
+ _gFigSystemControllerTrace
+ _gFigVibratorTrace
+ _gFigVolumeControllerRemoteTrace
+ _gFrontboardServicesLib
+ _gMXSystemControllerListLock
+ _gPreferHeadphonesOverCarsAndSpeakersEnabled
+ _gSBSDisplayLayoutRoleDescription
+ _gSTSRemoteTrace
+ _gSTSServerTrace
+ _gSTSTrace
+ _gSpringboardServicesLib
+ _gVAEM
+ _gVibeSynthDylibHandle
+ _getAwaitingDispatchQueue.onceToken
+ _getConnectBannerResponseCache.connectBannerResponseDictionary
+ _getConnectBannerResponseCache.onceTokenConnectBannerResponseDictionary
+ _getRTCReportingClass.softClass
+ _getSharedBannerClient.onceToken
+ _getkRTCReportingMessageParametersCategorySymbolLoc.ptr
+ _getkRTCReportingMessageParametersPayloadSymbolLoc.ptr
+ _getkRTCReportingMessageParametersTypeSymbolLoc.ptr
+ _getkRTCReportingSessionInfoBatchEventSymbolLoc.ptr
+ _getkRTCReportingSessionInfoClientBundleIDSymbolLoc.ptr
+ _getkRTCReportingSessionInfoClientTypeSymbolLoc.ptr
+ _getkRTCReportingSessionInfoClientVersionSymbolLoc.ptr
+ _getkRTCReportingSessionInfoSessionIDSymbolLoc.ptr
+ _getkRTCReportingUserInfoClientNameSymbolLoc.ptr
+ _getkRTCReportingUserInfoServiceNameSymbolLoc.ptr
+ _getnw_path_uses_interface_typeSymbolLoc.ptr
+ _gotLoadHelper_x8$_OBJC_CLASS_$_BTAudioRoutingRequest
+ _init.once_token
+ _initializeAttributeForKeyMappingToFig.onceToken
+ _isRouteInfoInVolumeOperationCurrent
+ _kFigEndpointDescriptorKey_AudioRouteName_BluetoothLEInput
+ _kFigEndpointDescriptorKey_AudioRouteName_LineIn
+ _kFigEndpointDescriptorKey_AudioRouteName_MicrophoneBluetooth
+ _kFigEndpointDescriptorKey_AudioRouteName_MicrophoneWired
+ _kFigEndpointDescriptorKey_AudioRouteName_USBInput
+ _kFigEndpointDescriptorKey_BTDetails_HighQualityContentCaptureEnabled
+ _kFigEndpointDescriptorKey_BTDetails_SupportsHighQualityContentCapture
+ _kFigEndpointDescriptorKey_IsCached
+ _kFigEndpointProperty_AirPlayVideoV2Supported
+ _kFigEndpointProperty_IsCarPlayVideoActive
+ _kFigEndpointProperty_IsCarPlayVideoAllowed
+ _kFigEndpointSubType_visionOS
+ _kFigRouteDiscovererCreationOption_PID
+ _kFigRouteDiscovererNotificationPayloadKey_NotificationTimestamp
+ _kFigRouteDiscovererNotificationPayloadKey_NotificationUUID
+ _kFigRouteDiscovererProperty_CachedDiscovery
+ _kFigRouteDiscovererProperty_FallbackRouteDescriptor
+ _kFigRoutingContextGlobalModificationOption_HostApplicationBundleID
+ _kFigRoutingContextGlobalModificationOption_UserInitiated
+ _kFigRoutingContextXPCMsgParam_ModificationMetrics
+ _kFigSystemControllerProperty_AllowBluetoothAccessoryToRequestAudioRoute
+ _kFigSystemControllerProperty_PreferHeadphonesOverCarsAndSpeakersEnabled
+ _kFigSystemControllerXPCMsgParam_AudioSessionID
+ _kFigSystemControllerXPCMsgParam_HostPID
+ _kFigVAEndpointManagerProperty_FallbackInputRouteEndpoint
+ _kFigVAEndpointProperty_HighQualityContentCaptureEnabled
+ _kFigVAEndpointProperty_SupportsHighQualityContentCapture
+ _kMXSessionAudioCategory_EndOfCallTone_CEPT
+ _kMXSessionAudioCategory_NFCCardComplete
+ _kMXSessionAudioCategory_NFCCardError
+ _kMXSessionAudioCategory_NFCCardProvisioned
+ _kMXSessionAudioMode_ShortFormVideo
+ _kMXSessionInterruptionInfoKey_AudioSessionID
+ _kMXSessionNotificationKey_IsOutputMutedDidChange_Muted
+ _kMXSessionNotificationKey_UserIntentToUnmuteDidChange_UserIntendsToUnmute
+ _kMXSessionNotification_IsOutputMutedDidChange
+ _kMXSessionNotification_UserIntentToUnmuteDidChange
+ _kMXSessionProperty_AudioTrackStatus
+ _kMXSessionProperty_HasExternalMuteNotificationContext
+ _kMXSessionProperty_IsOutputMuted
+ _kMXSessionProperty_IsPlayerMuted
+ _kMXSessionProperty_IsPlayingVideoOutput
+ _kMXSessionProperty_PrefersBluetoothHighQualityContentCapture
+ _kMXSessionProperty_ShadowingAudioSessionOptions
+ _kMXSessionProperty_ShadowingAudioSessionOptionsKey_AudioSessionID
+ _kMXSessionProperty_ShadowingAudioSessionOptionsKey_ShadowingOptions
+ _kMXSessionReporterIDLog_IsIndependentInputAudioResourceSession
+ _kMXSession_InSystemSoundDetailsKey_PrefersToPlayAudioToHeadphonesOnly
+ _kMXSession_RouteDescriptionKey_BTDetails_IsHighQualityContentCaptureEnabled
+ _kMXSession_RouteDescriptionKey_BTDetails_SupportsHighQualityContentCapture
+ _kMXSession_RouteDetailedDescriptionKey_HighQualityContentCaptureEnabled
+ _kMXSession_RouteDetailedDescriptionKey_SupportsHighQualityContentCapture
+ _kMXSystemControllerNotification_AllowBluetoothAccessoryToRequestAudioRouteDidChange
+ _kMXSystemControllerNotification_AllowBluetoothAccessoryToRequestAudioRouteDidChange_IsAllowed
+ _kMXSystemControllerNotification_PreferHeadphonesOverCarsAndSpeakersDidChange
+ _kMXSystemControllerNotification_PreferHeadphonesOverCarsAndSpeakersDidChange_Enabled
+ _kMXSystemControllerProperty_ActivePhoneCallInfo_AudioSessionID
+ _kMXSystemControllerProperty_AllowBluetoothAccessoryToRequestAudioRoute
+ _kMXSystemControllerProperty_PreferHeadphonesOverCarsAndSpeakersEnabled
+ _kVirtualAudioDeviceDescriptionAudioSessionIDsKey_CFString
+ _kVirtualAudioDeviceDescriptionConnectedInputPortsKey_CFString
+ _kVirtualAudioDeviceDescriptionDeviceNameKey_CFString
+ _kVirtualAudioPlugInRouteConfigurationPreferStudioMicInput_CFString
+ _kVirtualAudioPlugInRouteConfigurationRoutableAsFallbackPortsKey_CFString
+ _kVirtualAudioPlugInRouteConfigurationUserPreferredInputKey_CFString
+ _kVirtualAudioPlugInSessionDescriptionFollowVADRoute_CFString
+ _objc_msgSend$AirPlayStartServicesInMXProcess
+ _objc_msgSend$LoadAirPlaySenderFramework
+ _objc_msgSend$RTCDictionary
+ _objc_msgSend$_configurationDidFinish
+ _objc_msgSend$addMXCoreSessionIndependentInputAudioResource:
+ _objc_msgSend$addMXSessionIndependentInputAudioResource:
+ _objc_msgSend$addSessionAudioObject
+ _objc_msgSend$allowBluetoothAccessoryToRequestAudioRoute
+ _objc_msgSend$alwaysPlaysAudio
+ _objc_msgSend$audioObjectID
+ _objc_msgSend$audioToolboxIsPlaying
+ _objc_msgSend$bannerResponseToString:
+ _objc_msgSend$canSessionsCoexistDueToMediaMultitasking:victim:
+ _objc_msgSend$canSessionsCoexistDueToOutputMuting:victim:
+ _objc_msgSend$cleanupConnectBannerIfNeeded:routeName:
+ _objc_msgSend$cleanupUndoBannerIfNeeded:routeName:
+ _objc_msgSend$clearDevicesStateCache
+ _objc_msgSend$clearLayoutRoleCache
+ _objc_msgSend$clearUserPreferredRoute:
+ _objc_msgSend$clientModificationFinishedTimestamp
+ _objc_msgSend$clientModificationStartedTimestamp
+ _objc_msgSend$connectBannerResponse
+ _objc_msgSend$copyActiveCoreSessionControllingRouting
+ _objc_msgSend$copyAllMXCoreSessionList
+ _objc_msgSend$copyAttributeForKeyMappingToFig
+ _objc_msgSend$copyAvailableRouteControlFeatures:
+ _objc_msgSend$copyCoreSessionsShadowingAudioSession:withOptions:
+ _objc_msgSend$copyDeviceAddressFromVADPort:
+ _objc_msgSend$copyDisplayIDForActiveCarPlayVideoSession
+ _objc_msgSend$copyFigController
+ _objc_msgSend$copyHighestPriorityLocalSession
+ _objc_msgSend$copyIndependentInputAudioResourceSessionWithAudioSessionID:
+ _objc_msgSend$copyMXCoreSessionIndependentInputAudioResourceList
+ _objc_msgSend$copyMXSessionIndependentInputAudioResourceList
+ _objc_msgSend$copyMXSystemControllerList:
+ _objc_msgSend$copyPreferredAvailableInputPortFromCache
+ _objc_msgSend$copyPreferredDeviceAddress:andPreemptivePortInfo:
+ _objc_msgSend$copyPreferredDeviceAddress:bundleID:isHypotheticalQuery:reason:
+ _objc_msgSend$copyPreferredInputPortFromConnectedPorts:
+ _objc_msgSend$copyPrimaryAppDisplayID
+ _objc_msgSend$copySessionRoutingInfoFromVA
+ _objc_msgSend$copySessionWithAudioObjectID:
+ _objc_msgSend$copySessionWithMXCoreSessionID:
+ _objc_msgSend$copySessionsShadowingAudioSessionID:withShadowingOptions:fromSessionList:
+ _objc_msgSend$copySessionsThatUserIntendsToUnmute:
+ _objc_msgSend$copySetAttributeForKeyMappingToFig
+ _objc_msgSend$copySystemAudioInputContextWithAllocator:options:context:
+ _objc_msgSend$copyUndoEndpointsForRoute:
+ _objc_msgSend$copyUserPreferredInputPort
+ _objc_msgSend$copyUserPreferredRoute:
+ _objc_msgSend$copyVADNamesFromSessionAudioBehavior
+ _objc_msgSend$correlationID
+ _objc_msgSend$deactivate
+ _objc_msgSend$dictionaryRepresentation
+ _objc_msgSend$discardUnavailableVADInfoFromDetailedRouteDescriptionIfNeeded:
+ _objc_msgSend$dismissBannerWithUUID:withResponse:
+ _objc_msgSend$doesSessionConfigurationChangeRequireOutputUnmute:oldAudioMode:
+ _objc_msgSend$dumpDebugConfigInfo
+ _objc_msgSend$dumpDebugStateInfo
+ _objc_msgSend$extractAndSetAuditToken:
+ _objc_msgSend$figEndpointType
+ _objc_msgSend$finalizeAudioAccessoryConnection
+ _objc_msgSend$fromPorts
+ _objc_msgSend$getAudioSessionID:forAttributedPID:
+ _objc_msgSend$getAudioTrackStatus
+ _objc_msgSend$getAudioTrackStatusAsString:
+ _objc_msgSend$getAwaitingDispatchQueue
+ _objc_msgSend$getCleanupSessionAssertionReasonString:
+ _objc_msgSend$getCurrentOutputPort
+ _objc_msgSend$getHostProcessAttributions:
+ _objc_msgSend$getIsPlayerMuted
+ _objc_msgSend$getIsPlayingVideoOutput
+ _objc_msgSend$getLayoutRoleForDisplayID:layoutRole:
+ _objc_msgSend$getShadowingAudioSessionOptionsAsString:
+ _objc_msgSend$getSharedBannerClient
+ _objc_msgSend$handleBTNotificationAudioRoutingChange
+ _objc_msgSend$handleNewWirelessPortConnected:
+ _objc_msgSend$handlePortDisconnected:
+ _objc_msgSend$handleUserIntentToUnmute:
+ _objc_msgSend$hasAudioTrack
+ _objc_msgSend$hasExternalMuteNotificationContext
+ _objc_msgSend$hijackWirelessPort:reason:portWentInEar:
+ _objc_msgSend$indexOfObject:
+ _objc_msgSend$initWithCorrelationID:
+ _objc_msgSend$initWithFigEndpointType:
+ _objc_msgSend$initWithInteger:
+ _objc_msgSend$initWithModificationMetrics:useMockService:
+ _objc_msgSend$initWithRouteConfigUpdatedReason:modificationMetrics:
+ _objc_msgSend$initWithRoutingContext:routeConfigUpdateID:correlationID:callback:context:
+ _objc_msgSend$initWithSessionInfo:userInfo:frameworksToCheck:
+ _objc_msgSend$initializeAttributeForKeyMappingToFig
+ _objc_msgSend$initializeAudioAccessoryConnection
+ _objc_msgSend$integerValue
+ _objc_msgSend$interruptAllIndependentInputAudioResourceSessions:interruptorName:
+ _objc_msgSend$interruptIndpendentInputAudioResourceSession:interruptorBundleID:interruptorName:fadeDuration:waitingToResume:
+ _objc_msgSend$isActiveDeviceWithValidSessionID:
+ _objc_msgSend$isAnyConnectBannerActive
+ _objc_msgSend$isAnyManagedDeviceConnected
+ _objc_msgSend$isAnySessionWithMappedVolumeCategoryPlaying:
+ _objc_msgSend$isCarPlayPortRoutableFromCustomizedRoutingPerspective:
+ _objc_msgSend$isCurrentRouteHeadphoneAndInEar:
+ _objc_msgSend$isEligibleForOutputMuting
+ _objc_msgSend$isMediaSession
+ _objc_msgSend$isOutputMuted
+ _objc_msgSend$isPortHeadphoneWithInEarDetectionSupported:
+ _objc_msgSend$isPortManaged:
+ _objc_msgSend$isRecordingWithBTManagedDevice
+ _objc_msgSend$isSessionConfigurationEligibleForOutputMuting:audioMode:
+ _objc_msgSend$isSupported
+ _objc_msgSend$isUsingBuiltInMic
+ _objc_msgSend$isVoiceAssistantPlayingToPersonalAudioDeviceOverMedia
+ _objc_msgSend$layoutChanged:
+ _objc_msgSend$modificationMetrics
+ _objc_msgSend$mostRecentSessionInfoSetOnVA
+ _objc_msgSend$muteOutputForSession:
+ _objc_msgSend$newPortNeedsToShowBanner:newPortIdentifier:newPortType:previousPort:
+ _objc_msgSend$numberWithUnsignedChar:
+ _objc_msgSend$playSystemSound:completionBlock:
+ _objc_msgSend$populateAdditiveRoutingInfoWithBTRecordingCustomizations:
+ _objc_msgSend$populateAdditiveRoutingInfoWithDefaultBuiltInRouteCustomization:
+ _objc_msgSend$populateAdditiveRoutingInfoWithEchoCancelledInput:
+ _objc_msgSend$populateAdditiveRoutingInfoWithFollowingVADInformation:inputOnly:
+ _objc_msgSend$populateAdditiveRoutingInfoWithRouteControlFeatures:
+ _objc_msgSend$populateVirtualAudioDeviceInfoFromSessionAudioBehaviors:newVADIDToNameMap:
+ _objc_msgSend$postInterruptionCommandForAudioSessionID:sessionID:interruptiondCmd:interruptionInfo:
+ _objc_msgSend$postInterruptionCommandNotification:interruptionCommand:interruptorName:interruptorBundleID:status:volumeChangeDuration:
+ _objc_msgSend$postStopCommandToShadowingSessionsForSession:withShadowingOptions:
+ _objc_msgSend$postStopCommandToShadowingSessionsForSession:withShadowingOptions:interruptor:waitingToResume:
+ _objc_msgSend$preferHeadphonesOverCarsAndSpeakersEnabled
+ _objc_msgSend$prefersBluetoothHighQualityContentCapture
+ _objc_msgSend$prepareSessionActivationBeforeACQDispatch:
+ _objc_msgSend$processActiveDevice:
+ _objc_msgSend$processName
+ _objc_msgSend$processOnDemandVADLossIfNeeded:isPreviousInputVADOnDemand:
+ _objc_msgSend$processSessionRoutingInfo:
+ _objc_msgSend$processSessionRoutingInfoDidChange
+ _objc_msgSend$promptForConnectDialog:withIconType:callbackHandler:
+ _objc_msgSend$promptForUndoBanner:withIconType:callbackHandler:
+ _objc_msgSend$promptUserResponseForRoute:newPortIdentifier:newPortName:newPortID:newPortType:newWirelessPorts:oldPort:activatingEndpoint:routingContext:connectHandler:
+ _objc_msgSend$promptUserResponseForUndoRoute:newPortIdentifier:newPortName:newPortID:newPortType:oldPort:routingContext:undoHandler:
+ _objc_msgSend$readHDMILatencyFromCoreAnimation
+ _objc_msgSend$reapplyDeviceSampleRateAndBufferSizeOnVADIfNeeded
+ _objc_msgSend$removeSessionAudioObject
+ _objc_msgSend$requiresExclaveSensor
+ _objc_msgSend$resetIsRecordingState
+ _objc_msgSend$resetMXSessionIsPlayingStates
+ _objc_msgSend$resetMXSessionIsRecordingStates
+ _objc_msgSend$resumeAllIndependentInputAudioResourceSessions:interruptorBundleID:interruptorName:
+ _objc_msgSend$resumeAllIndependentInputAudioResourceSessionsShadowing:withShadowingOptions:interruptor:status:
+ _objc_msgSend$resumeIndependentInputAudioResourceSession:interruptorBundleID:interruptorName:status:fadeDuration:
+ _objc_msgSend$routeConfigUpdateReason
+ _objc_msgSend$routeSemaphore
+ _objc_msgSend$routeToBTDeviceIfNeeded:
+ _objc_msgSend$selfWeak
+ _objc_msgSend$sendAudioRoutingRequestToDevice:appBundleID:audioScore:flags:reason:responseHandler:
+ _objc_msgSend$sendMessageWithDictionary:error:
+ _objc_msgSend$sendModificationResult
+ _objc_msgSend$sendModificationResult:
+ _objc_msgSend$sendSessionConfigurationInfoToVA
+ _objc_msgSend$serverModificationFinishedTimestamp
+ _objc_msgSend$serverModificationStartedTimestamp
+ _objc_msgSend$setAudioObjectID:
+ _objc_msgSend$setAudioToolboxIsPlaying:
+ _objc_msgSend$setAudioTrackStatus:
+ _objc_msgSend$setClientModificationFinishedTimestamp:
+ _objc_msgSend$setClientModificationStartedTimestamp:
+ _objc_msgSend$setConnectBannerResponse:
+ _objc_msgSend$setFigEndpointType:
+ _objc_msgSend$setGreenTeaLoggerRecordingState:state:
+ _objc_msgSend$setHasExternalMuteNotificationContext:
+ _objc_msgSend$setIsOutputMuted:
+ _objc_msgSend$setIsPlayerMuted:
+ _objc_msgSend$setIsPlayingVideoOutput:
+ _objc_msgSend$setIsVoiceAssistantPlayingToPersonalAudioDeviceOverMedia:
+ _objc_msgSend$setMostRecentSessionInfoSetOnVA:
+ _objc_msgSend$setPreferHeadphonesOverCarsAndSpeakersEnabled:
+ _objc_msgSend$setPrefersBluetoothHighQualityContentCapture:
+ _objc_msgSend$setReason:
+ _objc_msgSend$setSelfWeak:
+ _objc_msgSend$setServerModificationFinishedTimestamp:
+ _objc_msgSend$setServerModificationStartedTimestamp:
+ _objc_msgSend$setServiceClass:
+ _objc_msgSend$setShadowingAudioSessionOptions:
+ _objc_msgSend$setSomeLongFormVideoClientIsActive:
+ _objc_msgSend$setTxid:
+ _objc_msgSend$setUndoBannerResponse:
+ _objc_msgSend$setUserPreferredRoute:hostApplicationBundleID:
+ _objc_msgSend$shadowingAudioSessionOptions
+ _objc_msgSend$shouldAllowBluetoothAccessoryToRequestAudioRoute
+ _objc_msgSend$shouldSendSessionConfigurationInfoToVA
+ _objc_msgSend$someLongFormVideoClientIsActive
+ _objc_msgSend$startConfigurationWithCompletionHandler:
+ _objc_msgSend$synchronizeSessionVolumeWithMediaVolumeIfNeeded:
+ _objc_msgSend$teardown
+ _objc_msgSend$txid
+ _objc_msgSend$typeAsAString
+ _objc_msgSend$undoBannerResponse
+ _objc_msgSend$unmuteOutputForSession:
+ _objc_msgSend$unregisterSessionAudioObject
+ _objc_msgSend$updateAudioBehaviorFromVARouteConfig:
+ _objc_msgSend$updateAudioSessionIDAndAudioObject:
+ _objc_msgSend$updateAudioTrackStatus:
+ _objc_msgSend$updateDeviceManagementState:reason:
+ _objc_msgSend$updateForRecordingStateDidChange
+ _objc_msgSend$updateIsRecordingMuted:updateBluetoothFrameworkToPlayMuteChime:
+ _objc_msgSend$updateLayoutRoleCache:displayID:
+ _objc_msgSend$updateMediaVolumeForPersonalDevice:oldRoute:
+ _objc_msgSend$updateSessionRoutingInformation:
+ _objc_msgSend$updateShadowingAudioSessionOptions:shouldUpdateVAConfig:
+ _objc_msgSend$updateSomeLongFormVideoClientIsActive
+ _objc_msgSend$userActionToString:
+ _objc_msgSend$userPreferredInputPortIsBluetoothManagedAndHighQuality
+ _objc_msgSend$vehicleForBluetoothAddress:
+ _objc_msgSend$vehicleName
+ _objc_msgSend$willRouteToOnDemandVADOnActivation:
+ _objc_release_x1
+ _objc_storeWeak
+ _objc_sync_enter
+ _objc_sync_exit
+ _os_signpost_id_make_with_pointer
+ _predictedRouting_getUpdatePredictedRouteReason
+ _pvmCopyMappedCategoryAndMode
+ _pvmInitialize
+ _pvmInitialize.cold.1
+ _pvmRawVolumeToVolume
+ _pvmVolumeToRawVolume
+ _remoteFigStarkModeController_EnsureClientEstablished.err
+ _remoteFigStarkModeController_EnsureClientEstablished.lock
+ _remoteSystemController_EnsureClientEstablished.err
+ _remoteSystemController_GetAudioSessionIDForAttributedPID
+ _remoteXPCRoutingContext_CreateInternal.cold.2
+ _remoteXPCRoutingContext_CreateInternal.cold.3
+ _remoteXPCRoutingContext_CreateInternal.cold.4
+ _remoteXPCRoutingContext_CreateInternal.cold.5
+ _remoteXPCRoutingContext_CreateInternal.cold.6
+ _routingContextRemoteXPC_ReportModificationMetrics
+ _routingContextRemoteXPC_SendData.cold.2
+ _routingContextResilientRemote_ReportModificationMetrics
+ _routingContextResilientRemote_replaceRemoteContext.cold.1
+ _routingContextResilientRemote_replaceRemoteContext.cold.2
+ _routingContext_ReportModificationMetrics
+ _routingContext_ReportModificationMetrics.cold.1
+ _routingContext_createWithUUID
+ _sAwaitingDispatchQueue
+ _sBannerClient
+ _sCMSessionClass
+ _sCMSessionID
+ _sOrderedMXSessionIndependentInputAudioResourceProperties
+ _selfWeakAVSCReference
+ _setGreenTeaLoggerRecordingState:state:.greenTeaLogger
+ _setGreenTeaLoggerRecordingState:state:.onceToken
+ _syslog
+ _systemController_GetAudioSessionIDForAttributedPID
+ _systemController_TranslateVolumeOperationName
+ _vaeCopyDeviceAddressFromVADPort
+ _vaeDoesPortSupportBluetoothHighQualityContentCapture
+ _vaeGetBTPortInEarStatusForBud
+ _vaeIsBTPortAdaptiveVolumeEnabled
+ _vaeIsBluetoothHighQualityContentCaptureEnabled
+ _vaeIsSiblingRoutePresent
+ _vaemAQMERestartIOFollowingRouteChange
+ _vaemAddToPortEndpointCache.cold.1
+ _vaemCanEncodeToAC3
+ _vaemClearUserPreferredInputPortInRouteConfigToVA
+ _vaemCopyConnectedInputPortsForDefaultVADFromDeviceListWithRouteConfiguration
+ _vaemCopyConnectedPortsWithDeviceListForRouteConfiguration
+ _vaemCopyEndpointForPort.cold.1
+ _vaemGetVADPortIDFromVADPortType.cold.1
+ _vaemInitializePortEndpointCache.onceToken
+ _vaemIsLocalSystemSoundDeviceType
+ _vaemRemoveAudioDevicesChangedListener
+ _vaemSendUserPreferredInputPortInRouteConfigToVA
+ _vaemSessionRoutingInfoChangeListener
+ _vaemUpdateConnectedInputPortsList
+ _vaemUpdatePortIDEndpointCache
+ _vaemUpdatePortIDEndpointCache.cold.1
+ _vaemUpdatePortListeners
- +[AVSystemController compatibleAudioRouteForRoute:]
- +[AVSystemController compatibleAudioRouteForRoute:].cold.1
- +[AVSystemController initialize]
- +[AVSystemController(InternalUse) postNotificationOnMainQueue:notification:object:]
- +[MXSystemController(Common) mxSystemControllerListBeginIteration]
- +[MXSystemController(Common) mxSystemControllerListEndIteration]
- -[AVSystemController attributeForKey:]
- -[AVSystemController setAttribute:forKey:error:]
- -[MXAdditiveRoutingManager copySessionWithAudioSessionID:]
- -[MXCoreSession allowsBluetoothRecordingCustomization]
- -[MXCoreSession allowsDefaultBuiltInRouteCustomization]
- -[MXCoreSession appendContextToMuteNotification]
- -[MXCoreSession bundleIdToPAAccessIntervalMap]
- -[MXCoreSession defaultBuiltInRoutePreferenceSetByClient]
- -[MXCoreSession defaultBuiltInRoutePreference]
- -[MXCoreSession defaultBuiltInRouteToUse]
- -[MXCoreSession enableBluetoothRecordingPreferenceSetByClient]
- -[MXCoreSession hasEntitlementToSuppressRecordingStateToSystemStatus]
- -[MXCoreSession idleSleepPreventorAllocated]
- -[MXCoreSession idleSleepPreventorCreationTime]
- -[MXCoreSession idleSleepPreventorName]
- -[MXCoreSession idleSleepPreventorUpdaterTimer]
- -[MXCoreSession idleSleepPreventor]
- -[MXCoreSession isPlayingStartTime]
- -[MXCoreSession isPlayingStopTime]
- -[MXCoreSession isRecordingMuted]
- -[MXCoreSession mode]
- -[MXCoreSession playbackAssertionRef]
- -[MXCoreSession preferredRouteControlFeatures]
- -[MXCoreSession prefersEchoCancelledInput]
- -[MXCoreSession prefersSuppressingRecordingState]
- -[MXCoreSession resumeAssertionRef]
- -[MXCoreSession resumeBackgroundAppUpdaterTimer]
- -[MXCoreSession setAllowsBluetoothRecordingCustomization:]
- -[MXCoreSession setAllowsDefaultBuiltInRouteCustomization:]
- -[MXCoreSession setAppendContextToMuteNotification:]
- -[MXCoreSession setBundleIdToPAAccessIntervalMap:]
- -[MXCoreSession setDefaultBuiltInRoutePreference:]
- -[MXCoreSession setDefaultBuiltInRoutePreferenceSetByClient:]
- -[MXCoreSession setEnableBluetoothRecordingPreferenceSetByClient:]
- -[MXCoreSession setHasEntitlementToSuppressRecordingStateToSystemStatus:]
- -[MXCoreSession setIdleSleepPreventor:]
- -[MXCoreSession setIdleSleepPreventorAllocated:]
- -[MXCoreSession setIdleSleepPreventorCreationTime:]
- -[MXCoreSession setIdleSleepPreventorName:]
- -[MXCoreSession setIdleSleepPreventorUpdaterTimer:]
- -[MXCoreSession setIsPlayingStartTime:]
- -[MXCoreSession setIsPlayingStopTime:]
- -[MXCoreSession setIsRecordingMuted:]
- -[MXCoreSession setMode:]
- -[MXCoreSession setPlaybackAssertionRef:]
- -[MXCoreSession setPreferredRouteControlFeatures:]
- -[MXCoreSession setPrefersEchoCancelledInput:]
- -[MXCoreSession setPrefersSuppressingRecordingState:]
- -[MXCoreSession setResumeAssertionRef:]
- -[MXCoreSession setResumeBackgroundAppUpdaterTimer:]
- -[MXCoreSession setShadowingAudioSessionID:]
- -[MXCoreSession setWaitingToResume:]
- -[MXCoreSession shadowingAudioSessionID]
- -[MXCoreSession shouldEnableBluetoothRecording]
- -[MXCoreSession updateAudioBehaviourFromVARouteConfig:]
- -[MXCoreSession waitingToResume]
- -[MXCoreSessionBase updateAudioBehaviourFromVARouteConfig:]
- -[MXCoreSessionSecure hasEntitlementToSetEnrollmentMode]
- -[MXCoreSessionSecure setHasEntitlementToSetEnrollmentMode:]
- -[MXCoreSessionSecure setPropertyForKey:value:].cold.11
- -[MXCoreSessionSecure updateAudioBehaviourFromVARouteConfig:]
- -[MXCoreSessionSecure updateEntitlements]
- -[MXMediaEndowmentManager getRecordingAttributions:]
- -[MXRoutingContextCallbackHelper initWithRoutingContext:routeConfigUpdateID:callback:context:]
- -[MXSessionManager(Utilities) isSessionUsingBuiltInMic:]
- -[MXSessionManager(VAUtilities) updateSecureSpeakerMuteState:]
- GCC_except_table103
- GCC_except_table109
- GCC_except_table111
- GCC_except_table117
- GCC_except_table128
- GCC_except_table166
- GCC_except_table168
- GCC_except_table170
- GCC_except_table174
- GCC_except_table176
- GCC_except_table178
- GCC_except_table180
- GCC_except_table182
- GCC_except_table195
- GCC_except_table200
- GCC_except_table204
- GCC_except_table210
- GCC_except_table216
- GCC_except_table231
- GCC_except_table56
- GCC_except_table58
- GCC_except_table59
- GCC_except_table62
- GCC_except_table73
- GCC_except_table96
- _BTAudioRoutingRequestClass
- _CFAllocatorAllocate
- _CMSMDeviceState_IsMediaserverd
- _CMSMDeviceState_UpdateDeviceConfiguration
- _CMSMDeviceState_UpdateDeviceConfiguration.cold.1
- _CMSMDeviceState_UpdateDeviceConfiguration.once
- _CMSMUtility_AreCategoryAndModeValidForSharePlayCallSession
- _CMSMUtility_CopySystemMusicRoutingContextUUID
- _CMSMVAUtility_CopyBTManagedPorts
- _CMSUtility_SetIsRecording.cold.1
- _CMSUtility_SetIsRecording.greenTeaLogger
- _CMSUtility_SetIsRecording.onceToken
- _DisposeRoutingContextServerState.cold.1
- _FigRouteDiscoveryManagerGetSharedQueue
- _FigRouteDiscoveryManagerGetSharedQueue.cold.1
- _FigRouteDiscoveryManagerRunBlockOnSerialQueueIfOnEmbeddedPlatforms
- _FigRoutingContextRemoteCopyAllAudioContexts.cold.1
- _FigSTSCreate.cold.4
- _FigSignalErrorAt
- _FigVolumeControllerCopySharedController.err
- _FigVolumeControllerCopySharedController.volumeController
- _IOHIDEventSystemClientSetMatching
- _MXBeginUpdatingIncrementalCodeCoverageData
- _MXBluetoothServices_AreManagedPortsAvailable
- _MXBluetoothServices_CopyPreemptivePortInfo
- _MXBluetoothServices_CopyPreferredDeviceAddress
- _MXBluetoothServices_IsPortBTManaged
- _MXBluetoothServices_QueryAudioRoutingActionForNewWirelessPort
- _MXBluetoothServices_RegisterForAudioRoutingChanged
- _MXBluetoothServices_RegisterForAudioRoutingChanged.notifyToken
- _MXBluetoothServices_RegisterForPreemptivePortChanged
- _MXBluetoothServices_RegisterForPreemptivePortChanged.notifyToken
- _MXBluetoothServices_RegisterForPreemptivePortDisconnected
- _MXBluetoothServices_RegisterForPreemptivePortDisconnected.notifyToken
- _MXBluetoothServices_RemoveDisconnectedDeviceIDs
- _MXEnsureReadyToCollectIncrementalCoverageData
- _MXFinishUpdatingIncrementalCodeCoverageData
- _MXHDMILatencyManagerState
- _MXInstallSysdiagnoseBlock
- _MXSetCodeCoverageFilePathPattern
- _MX_FeatureFlags_IsAudiomxdEnabled
- _MX_FeatureFlags_IsOffloadACQEnabled
- _MX_FeatureFlags_IsOffloadACQEnabled.cold.1
- _MX_FeatureFlags_IsOffloadACQEnabled.onceToken
- _MX_FeatureFlags_IsOffloadACQEnabled.sIsOffloadACQEnabled
- _MX_FeatureFlags_IsReduceRouteDiscoveryQueueHoppingEnabled
- _MX_FeatureFlags_IsReduceRouteDiscoveryQueueHoppingEnabled.cold.1
- _MX_FeatureFlags_IsReduceRouteDiscoveryQueueHoppingEnabled.onceToken
- _MX_FeatureFlags_IsReduceRouteDiscoveryQueueHoppingEnabled.reduceRouteDiscoveryQueueHopping
- _MX_FeatureFlags_IsSmartRoutingInEarQueryEnabled
- _MX_FeatureFlags_IsSmartRoutingInEarQueryEnabled.cold.1
- _MX_FeatureFlags_IsSmartRoutingInEarQueryEnabled.onceToken
- _MX_FeatureFlags_IsSmartRoutingInEarQueryEnabled.sIsSmartRoutingInEarQueryEnabled
- _MX_FrontBoardServcies_CopyPrimaryAppDisplayID
- _MX_FrontBoardServices_Initialize
- _NanoRegistryLibraryCore.frameworkLibrary
- _OBJC_IVAR_$_MXCoreSession._allowsBluetoothRecordingCustomization
- _OBJC_IVAR_$_MXCoreSession._allowsDefaultBuiltInRouteCustomization
- _OBJC_IVAR_$_MXCoreSession._appendContextToMuteNotification
- _OBJC_IVAR_$_MXCoreSession._bundleIdToPAAccessIntervalMap
- _OBJC_IVAR_$_MXCoreSession._defaultBuiltInRoutePreference
- _OBJC_IVAR_$_MXCoreSession._defaultBuiltInRoutePreferenceSetByClient
- _OBJC_IVAR_$_MXCoreSession._enableBluetoothRecordingPreferenceSetByClient
- _OBJC_IVAR_$_MXCoreSession._hasEntitlementToSuppressRecordingStateToSystemStatus
- _OBJC_IVAR_$_MXCoreSession._idleSleepPreventor
- _OBJC_IVAR_$_MXCoreSession._idleSleepPreventorAllocated
- _OBJC_IVAR_$_MXCoreSession._idleSleepPreventorCreationTime
- _OBJC_IVAR_$_MXCoreSession._idleSleepPreventorName
- _OBJC_IVAR_$_MXCoreSession._idleSleepPreventorUpdaterTimer
- _OBJC_IVAR_$_MXCoreSession._isPlayingStartTime
- _OBJC_IVAR_$_MXCoreSession._isPlayingStopTime
- _OBJC_IVAR_$_MXCoreSession._isRecordingMuted
- _OBJC_IVAR_$_MXCoreSession._mode
- _OBJC_IVAR_$_MXCoreSession._playbackAssertionRef
- _OBJC_IVAR_$_MXCoreSession._preferredRouteControlFeatures
- _OBJC_IVAR_$_MXCoreSession._prefersEchoCancelledInput
- _OBJC_IVAR_$_MXCoreSession._prefersSuppressingRecordingState
- _OBJC_IVAR_$_MXCoreSession._resumeAssertionRef
- _OBJC_IVAR_$_MXCoreSession._resumeBackgroundAppUpdaterTimer
- _OBJC_IVAR_$_MXCoreSession._shadowingAudioSessionID
- _OBJC_IVAR_$_MXCoreSession._waitingToResume
- _OBJC_IVAR_$_MXCoreSessionSecure._hasEntitlementToSetEnrollmentMode
- _OBJC_IVAR_$_MXRoutingContextCallbackHelper.mCreationTime
- _OBJC_IVAR_$_MXVolumeManager.mRestingVolumeTimer
- _OBJC_IVAR_$_MXVolumeManager.mTimerDuration
- __OBJC_$_CLASS_METHODS_AVSystemController(InternalUse)
- __OBJC_$_INSTANCE_METHODS_MXCoreSession
- __OBJC_$_INSTANCE_METHODS_MXSessionManager(InterruptionActionMapper|DuckingUtilities|MXSessionManagerContinuityScreenOutputPortUtilities|Common|VAUtilities|Utilities)
- __OBJC_$_INSTANCE_METHODS_MXVolumeManager
- __OBJC_$_INSTANCE_VARIABLES_MXVolumeManager
- __ZNKSt3__16vectorI11VARouteInfoNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorI12CMSRouteInfoNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI11VARouteInfoEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI12CMSRouteInfoEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __Znwm
- ___49-[MXSystemController initWithPID:remoteDeviceID:]_block_invoke_2
- ___51+[AVSystemController compatibleAudioRouteForRoute:]_block_invoke
- ___52-[MXMediaEndowmentManager getRecordingAttributions:]_block_invoke
- ___57-[MXSessionManager(Utilities) updateMuteState:muteValue:]_block_invoke.22
- ___83+[AVSystemController(InternalUse) postNotificationOnMainQueue:notification:object:]_block_invoke
- ___83-[MXEndpointDescriptorCache _availableEndpointsDidChangeForEndpointManager:atDate:]_block_invoke_2
- ___86-[MXSessionManager(Utilities) updateBluetoothFrameworkToPlayMuteChime:playRejectTone:]_block_invoke.40
- ___86-[MXSessionManager(Utilities) updateBluetoothFrameworkToPlayMuteChime:playRejectTone:]_block_invoke_2.41
- ___94-[MXRoutingContextCallbackHelper initWithRoutingContext:routeConfigUpdateID:callback:context:]_block_invoke
- ___CMSMAP_StartRouteAwayFromAirPlayHandoffTimer_block_invoke_2
- ___CMSMDeviceState_UpdateDeviceConfiguration_block_invoke
- ___CMSMNotificationUtility_PostNowPlayingAppIsPlayingDidChange_block_invoke.19
- ___CMSUtility_PostInterruptionCommandNotification_block_invoke_2
- ___CMSUtility_SetIsRecording_block_invoke
- ___FigRouteDiscovererCreate_block_invoke_2
- ___FigRouteDiscovererUpdateCachedRouteInformation_block_invoke
- ___FigRouteDiscoveryManagerCopyRouteDescriptorsFromEndpointsAndAudioSessionID_block_invoke
- ___FigRouteDiscoveryManagerRunBlockOnSerialQueueIfOnEmbeddedPlatforms_block_invoke
- ___FigRoutingContextResilientRemoteCopyContextForUUID_block_invoke_2
- ___FigRoutingManagerContextUtilities_AddCurrentlyActivatingEndpoint_block_invoke_3
- ___FigRoutingManagerContextUtilities_RemoveContext_block_invoke_2
- ___FigRoutingManagerSetupEndpointCentralForCarPlay_block_invoke
- ___FigRoutingManagerStartCarPlayAudioMainPortPublishingCheckTimer_block_invoke_2
- ___FigRoutingManagerStartDeactivateAirPlayEndpointTimer_block_invoke_2
- ___MXBluetoothServices_IsPortBTManaged_block_invoke
- ___MXBluetoothServices_QueryAudioRoutingActionForNewWirelessPort_block_invoke
- ___MXBluetoothServices_RegisterForAudioRoutingChanged_block_invoke
- ___MXBluetoothServices_RegisterForPreemptivePortChanged_block_invoke
- ___MXBluetoothServices_RegisterForPreemptivePortDisconnected_block_invoke
- ___MXCoreSessionSetProperty_block_invoke.158
- ___MXCoreSessionSetProperty_block_invoke.167
- ___MXCoreSessionSetProperty_block_invoke_2
- ___MXInitialize_block_invoke.cold.2
- ___MX_FeatureFlags_IsOffloadACQEnabled_block_invoke
- ___MX_FeatureFlags_IsReduceRouteDiscoveryQueueHoppingEnabled_block_invoke
- ___MX_FeatureFlags_IsSmartRoutingInEarQueryEnabled_block_invoke
- ___MX_FrontBoardServices_Initialize_block_invoke
- ___MX_FrontBoardServices_Initialize_block_invoke_2
- ___NanoRegistryLibraryCore_block_invoke
- ___PVMInitialize_block_invoke.cold.1
- ___PowerManager_InitializeCPMSForAudio_block_invoke_2.6
- ___PowerManager_InitializeCPMSForAudio_block_invoke_3
- ___PowerManager_InitializeCPMSForHaptics_block_invoke_2.6
- ___PowerManager_InitializeCPMSForHaptics_block_invoke_3
- ___block_descriptor_32_e34_i16?0^{OpaqueFigRoutingContext=}8l
- ___block_descriptor_40_e8_32b_e5_v8?0ls32l8
- ___block_descriptor_48_e28_i16?0^{OpaqueFigEndpoint=}8l
- ___block_descriptor_48_e8_32r40r_e5_v8?0lr32l8r40l8
- ___block_descriptor_60_e8_32o40o48r_e5_v8?0lr48l8s32l8s40l8
- ___block_descriptor_60_e8_32o40w_e5_v8?0lw40l8s32l8
- ___block_descriptor_61_e8_32r40r_e32_v16?0"BTAudioRoutingResponse"8lr32l8r40l8
- ___block_descriptor_64_e8_32r40r_e32_v16?0"BTAudioRoutingResponse"8lr32l8r40l8
- ___block_descriptor_68_e8_32r40r48r_e5_v8?0lr32l8r40l8r48l8
- ___block_descriptor_72_e8_32o40o48r56r_e5_v8?0lr48l8s32l8s40l8r56l8
- ___block_descriptor_72_e8_32r40r48r_e32_v16?0"BTAudioRoutingResponse"8lr32l8r40l8r48l8
- ___block_descriptor_76_e8_32r40r_e5_v8?0lr32l8r40l8
- ___block_descriptor_tmp
- ___block_descriptor_tmp.10
- ___block_descriptor_tmp.11
- ___block_descriptor_tmp.12
- ___block_descriptor_tmp.13
- ___block_descriptor_tmp.14
- ___block_descriptor_tmp.15
- ___block_descriptor_tmp.16
- ___block_descriptor_tmp.19
- ___block_descriptor_tmp.2
- ___block_descriptor_tmp.3
- ___block_descriptor_tmp.4
- ___block_descriptor_tmp.5
- ___block_descriptor_tmp.7
- ___block_descriptor_tmp.8
- ___block_descriptor_tmp.9
- ___block_literal_global.104
- ___block_literal_global.108
- ___block_literal_global.109
- ___block_literal_global.112
- ___block_literal_global.114
- ___block_literal_global.117
- ___block_literal_global.120
- ___block_literal_global.124
- ___block_literal_global.126
- ___block_literal_global.135
- ___block_literal_global.138
- ___block_literal_global.141
- ___block_literal_global.146
- ___block_literal_global.149
- ___block_literal_global.151
- ___block_literal_global.153
- ___block_literal_global.156
- ___block_literal_global.176
- ___block_literal_global.178
- ___block_literal_global.192
- ___block_literal_global.220
- ___block_literal_global.232
- ___block_literal_global.235
- ___block_literal_global.243
- ___block_literal_global.254
- ___block_literal_global.290
- ___block_literal_global.292
- ___block_literal_global.299
- ___block_literal_global.31
- ___block_literal_global.338
- ___block_literal_global.34
- ___block_literal_global.345
- ___block_literal_global.349
- ___block_literal_global.352
- ___block_literal_global.413
- ___block_literal_global.429
- ___block_literal_global.431
- ___block_literal_global.46
- ___block_literal_global.55
- ___block_literal_global.57
- ___block_literal_global.62
- ___block_literal_global.65
- ___block_literal_global.66
- ___block_literal_global.68
- ___block_literal_global.69
- ___block_literal_global.71
- ___block_literal_global.72
- ___block_literal_global.739
- ___block_literal_global.755
- ___block_literal_global.77
- ___block_literal_global.81
- ___block_literal_global.83
- ___block_literal_global.92
- ___block_literal_global.93
- ___block_literal_global.95
- ___block_literal_global.98
- ___central_Finalize_block_invoke
- ___central_endpointDidDeactivateNotificationCallback_block_invoke
- ___central_resetStates_block_invoke
- ___chkstk_darwin
- ___cmsHandleIdleSleep_block_invoke
- ___cmsHandleIdleSleep_block_invoke_2
- ___cmsSetIsActive_block_invoke.130
- ___cmsSetIsPlaying_block_invoke_2
- ___cmsmInitializeCMSessionManager_block_invoke.31
- ___cmsmInitializeCMSessionManager_block_invoke_4
- ___cmsmInitializeCMSessionManager_block_invoke_5
- ___cmsmInitializeCMSessionManager_block_invoke_6
- ___cmsmScreenIsBlankedChangedCallback_block_invoke.343
- ___discoverer_SetProperty_block_invoke.49
- ___discoverer_SetProperty_block_invoke_2.47
- ___discoverer_SetProperty_block_invoke_3
- ___discoveryManager_iOSCopyAvailableEndpoints_block_invoke
- ___discoveryManager_iOSCopyAvailableEndpoints_block_invoke_2
- ___discoveryManager_postNotificationToAllDiscoverers_block_invoke.52
- ___discoveryManager_postNotificationToAllDiscoverers_block_invoke_2
- ___discoveryManager_shouldSkipAvailableEndpointsQuery_block_invoke
- ___getNRPairedDeviceRegistryClass_block_invoke
- ___getNRPairedDeviceRegistryClass_block_invoke.cold.1
- ___mxBluetoothServices_CopyPreferredDeviceAddress_block_invoke
- ___mxBluetoothServices_getRoutingRequestQueue_block_invoke
- ___mxBluetoothServices_loadFramework_block_invoke
- ___routingSessionManager_PrepareForPlayback_block_invoke.108
- ___routingSessionManager_StartSessionWithRouteDescriptors_block_invoke_4
- ___routingSessionManager_StartSessionWithRouteDescriptors_block_invoke_5
- ___routingSessionManager_UpdateCurrentSessionFromLikelyDestinations_block_invoke_2
- ___routingSessionManager_findTopAvailablePredictedDestination_block_invoke.196
- ___routingSessionManager_routeToDestinationOfCurrentSession_block_invoke.117
- ___routingSessionManager_setDestinationOnRoutingContext_block_invoke.155
- ___routingSessionManager_setDestinationOnRoutingContext_block_invoke_2
- ___routingSessionManager_startDiscovery_block_invoke.127
- ___routingSessionManager_updatePredictedDestinations_block_invoke.274
- ___routingSessionManager_waitForRecentPredictions_block_invoke_3
- ___routingSessionManager_waitForRecentPredictions_block_invoke_4
- ___routingSessionManager_waitForRecentPredictions_block_invoke_5
- ___vaemConnectedPortsPropertyListenerGuts_block_invoke
- ___vaemCurrentRouteHasVolumeControlListener_block_invoke_2
- ___vaemUpdateSharedAudioRouteState_block_invoke_2
- _audit_stringNanoRegistry
- _bzero
- _central_endpointDidDeactivateNotificationCallback
- _central_resetStates
- _cmsmUpdateInEarBasedPlaybackState.audioPausedOnBudsOutOfEar
- _cmsmUpdateInEarBasedPlaybackState.audioRouteInEarStatus
- _cmsmUpdateInEarBasedPlaybackState.nowPlayingDisplayIDWhenPaused
- _cmsmUpdateInEarBasedPlaybackState.portForWhichLastUpdateWasReceived
- _cmsmUpdateInEarBasedPlaybackState.timestampWhenNoBudWasInEar
- _compatibleAudioRouteForRoute:.onceToken
- _compatibleAudioRouteForRoute:.sRouteMap
- _gBluetoothPortsToBTManagedMapping
- _gBluetoothPortsToBTManagedMappingLock
- _gFrontBoardServicesMonitor
- _gMXSystemControllerListActiveReaders
- _gMXSystemControllerListReadLock
- _gMXSystemControllerListWriteSemaphore
- _getHDMILatencyForCurrentRefreshRate
- _getNRPairedDeviceRegistryClass.softClass
- _kMXSessionAudioMode_EchoCancellationInput
- _kMXSessionAudioMode_Enrollment
- _kVirtualAudioDeviceDescriptionAudioSessionIDKey_CFString
- _mxBluetoothServices_CopyPreferredDeviceAddress
- _mxBluetoothServices_SendAudioRoutingRequest
- _mxBluetoothServices_SendAudioRoutingRequest.cold.1
- _mxBluetoothServices_addCachedPort
- _mxBluetoothServices_copyHighestPriorityLocalSessionBundleIDAndAudioScore
- _mxBluetoothServices_getRoutingRequestQueue.once
- _mxBluetoothServices_getRoutingRequestQueue.routingRequestQueue
- _mxBluetoothServices_handleAudioRoutingChanged
- _mxBluetoothServices_isBluetoothServicesLoaded
- _mxBluetoothServices_isBluetoothServicesLoaded.cold.1
- _mxBluetoothServices_loadFramework.onceToken
- _mxBluetoothServices_readCachedPort
- _mxBluetoothServices_routeToBTDeviceIfNeeded
- _objc_msgSend$appendContextToMuteNotification
- _objc_msgSend$compatibleAudioRouteForRoute:
- _objc_msgSend$getRecordingAttributions:
- _objc_msgSend$hasEntitlementToSetEnrollmentMode
- _objc_msgSend$initWithRoutingContext:routeConfigUpdateID:callback:context:
- _objc_msgSend$interruptAllSessionsAndSystemSounds:
- _objc_msgSend$isSessionUsingBuiltInMic:
- _objc_msgSend$isSessionWithAudioModeActive:
- _objc_msgSend$mxSystemControllerListBeginIteration
- _objc_msgSend$mxSystemControllerListEndIteration
- _objc_msgSend$numberWithInteger:
- _objc_msgSend$setAppendContextToMuteNotification:
- _objc_msgSend$setHasEntitlementToSetEnrollmentMode:
- _objc_msgSend$updateAudioBehaviourFromVARouteConfig:
- _objc_msgSend$updateEntitlements
- _objc_msgSend$updateSecureSpeakerMuteState:
- _routingSessionManager_routeConfigUpdated.cold.1
- _sBluetoothServicesLoaded
- _vaeGetSiblingsForPort
- _vaeMakeSiblingPortsRoutable
CStrings:
+ "\t[%ld] Endpoint=%@, routeUID = %@, supportedFeatures=%@\n"
+ " -PVM- %s:  fig volume_trace == %s"
+ " Auth Info should be valid"
+ " GroupID:%@::"
+ " NOT"
+ "! endpointOut"
+ "%@\t[%ld] Endpoint=%@, routeUID = %@, supportedFeatures=%@\n"
+ "%@ (%@)"
+ "%@ UUID:%@::"
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "%{public}s %{public}s:%i Invalid modification metrics"
+ "(Fig)"
+ "+[AVSystemControllerCommon postNotificationOnMainQueue:notification:object:]"
+ "+[AVSystemControllerCommon postNotificationOnMainQueue:notification:object:]_block_invoke"
+ "+[MXInitialization AirPlayStartServicesInMXProcess]"
+ "+[MXInitialization LoadAirPlaySenderFramework]"
+ "+[MXSession(InternalUse) isCoreSessionFormatValidForMaxOutputChannels:]"
+ "+[MXSession(InternalUse) updateAudioTrackStatus:]"
+ "+[MXSessionManager copyDefaultMusicAppFromPlist]"
+ "+[MXSessionManagerBase copySessionsShadowingAudioSessionID:withShadowingOptions:fromSessionList:]"
+ "+[MXSessionManagerBase postInterruptionCommandForAudioSessionID:sessionID:interruptiondCmd:interruptionInfo:]"
+ "+[MXSessionManagerSidekick sharedInstance]_block_invoke"
+ "+[MXSystemController allowBluetoothAccessoryToRequestAudioRoute]"
+ "+[MXSystemController setPreferHeadphonesOverCarsAndSpeakersEnabled:]"
+ "+[MXSystemController(Common) mxSystemControllerListAddInstance:isSidekick:]"
+ "+[MXSystemController(Common) updateMXSystemControllerList]"
+ "+[MXSystemController(InternalUse) getPIDForAnyAppThatWantsVolumeChanges]"
+ "---CMScreen---"
+ "---CMScreen--- %s: Nothing to do. Not in AirPlay Screen mode."
+ "---CMScreen--- %s: Nothing to do. Redundant event notification."
+ "---CMScreen--- %s: Screen is already activated - no-op"
+ "---CMScreen--- %s: State switching from %@ to %@"
+ "---CMScreen--- %s: inEndpointType = %@, screenState = %@"
+ "---CMScreen--- %s: screenState = %@"
+ "---CMScreen--- %s: setClientPID not found."
+ "---CMScreen--- %s: setMirroringMode not found."
+ "---CMScreen--- %s: setting mirroringMode = %d"
+ "---CMScreen--- %s: state = %@, event = %@: %d -> %d"
+ "-666"
+ "-AVSystemController- %s: Failed to create AVSystemController, [super init] returned nil"
+ "-AVSystemController- %s: [%p]"
+ "-AVSystemController- %s: [%p] Category:%@ route:%@ deviceIdentifier:%@ Subtype:%@"
+ "-AVSystemController- %s: [%p] Increment:%d Category:%@"
+ "-AVSystemController- %s: [%p] Increment:%d Category:%@ route:%@ deviceIdentifier:%@ Subtype:%@"
+ "-AVSystemController- %s: [%p] Route:%@ DeviceIdentifier:%@"
+ "-AVSystemController- %s: [%p] VolumeBy:%1.3f Category:%@"
+ "-AVSystemController- %s: [%p] VolumeBy:%1.3f Category:%@ route:%@ deviceIdentifier:%@ Subtype:%@"
+ "-AVSystemController- %s: [%p] VolumeBy:%1.3f Route:%@ DeviceIdentifier:%@"
+ "-AVSystemController- %s: [%p] VolumeBy:%1.3f fallbackCategory:%@"
+ "-AVSystemController- %s: [%p] VolumeTo:%1.3f"
+ "-AVSystemController- %s: [%p] VolumeTo:%1.3f Category:%@"
+ "-AVSystemController- %s: [%p] VolumeTo:%1.3f Category:%@ retainFullMute:%{BOOL}u"
+ "-AVSystemController- %s: [%p] VolumeTo:%1.3f Category:%@ route:%@ deviceIdentifier:%@ Subtype:%@"
+ "-AVSystemController- %s: [%p] VolumeTo:%1.3f Category:%@ route:%@ deviceIdentifier:%@ Subtype:%@ rampUpDuration:%1.3f rampDownDuration:%1.3f retainFullMute:%{BOOL}u"
+ "-AVSystemController- %s: [%p] VolumeTo:%1.3f Category:%@ route:%@ deviceIdentifier:%@ Subtype:%@ rampUpwardDuration:%@ rampDownwardDuration:%@"
+ "-AVSystemController- %s: [%p] VolumeTo:%1.3f Route:%@ DeviceIdentifier:%@"
+ "-AVSystemController- %s: [%p] VolumeTo:%1.3f fallbackCategory:%@"
+ "-AVSystemController- %s: [%p] bundleID:%@"
+ "-AVSystemController- %s: [%p] category: %@ => %@"
+ "-AVSystemController- %s: [%p] category:%@"
+ "-AVSystemController- %s: [%p] category:%@ Mode:%@"
+ "-AVSystemController- %s: [%p] error copying device route for category %@: %d"
+ "-AVSystemController- %s: [%p] error copying pickable routes for category %@ and mode %@: %d"
+ "-AVSystemController- %s: [%p] error copying pickable routes for category %@: %d"
+ "-AVSystemController- %s: [%p] error copying volume category for audio category %@: %d"
+ "-AVSystemController- %s: [%p] fallbackCategory:%@"
+ "-AVSystemController- %s: [%p] increment:%d Route:%@ DeviceIdentifier:%@"
+ "-AVSystemController- %s: [%p] increment:%d fallbackCategory:%@"
+ "-AVSystemController- %s: [%p] posting AVSystemController_EffectiveVolumeDidChangeNotification %@"
+ "-AVSystemController- %s: [%p] routeInfo:%@ Password:-"
+ "-AVSystemController- %s: hostPID cannot be zero!"
+ "-AVSystemController- %s: outAudioSessionID cannot be nil!"
+ "-AVSystemController- %s: shouldClientWithAudioScoreHijackRoute returned error %d"
+ "-AVSystemController_Common- %s:  failed: '%@'"
+ "-AVSystemController_Common- %s: This is an abstract method. Please create an AVSC object only"
+ "-AVSystemController_Common- %s: [%p] %@ -> %@"
+ "-AVSystemController_Common- %s: [%p] %@ forKey:%@"
+ "-AVSystemController_Common- %s: [%p] posting %@ %@"
+ "-AVSystemController_Common- %s: [%p] posting AVSystemController_RecordingStateDidChangeNotification"
+ "-AVSystemController_Common- %s: [%p] posting notification '%@' with payload='%@'"
+ "-CMSMDevState- %s: Can't monitor power"
+ "-CMSMDevState- %s: Can't monitor power: %i"
+ "-CMSMDevState- %s: Device is: %s"
+ "-CMSMDevState- %s: Device supports PiP: %s"
+ "-CMSMDevState- %s: Invalid parameter"
+ "-CMSMDevState- %s: It's a HomePod (AudioAccessory)"
+ "-CMSMDevState- %s: It's a NonUI build."
+ "-CMSMDevState- %s: It's an Apple TV"
+ "-CMSMDevState- %s: It's an Apple Watch"
+ "-CMSMDevState- %s: It's an iPad"
+ "-CMSMDevState- %s: It's an iPhone"
+ "-CMSMDevState- %s: Redundant update, skipping"
+ "-CMSMDevState- %s: Ringer On == %s (read from %s)"
+ "-CMSMDevState- %s: Ringer switch always on for devices without ringer switch and NonUI builds"
+ "-CMSMDevState- %s: Unable to get kMGQMedusaPIPCapability"
+ "-CMSMDevState- %s: buttons-can-change-ringer-volume = %s"
+ "-CMSMDevState- %s: buttons-can-change-ringer-volume default preference : %s"
+ "-CMSMDevState- %s: called"
+ "-CMSMDevState- %s: could not register for %s notification"
+ "-CMSMDevState- %s: deviceIsLocked == %s"
+ "-CMSMDevState- %s: gDeviceState.vibrationDisabled = %s"
+ "-CMSMDevState- %s: screenIsBlanked == %s"
+ "-CMSMDevState- %s: screenIsBlankedByProximitySensor == %s"
+ "-CMSMNotificationUtilities- %s: "
+ "-CMSMNotificationUtilities- %s: Active sessions being notified of SomeOtherNonAmbientSessionIsPlayingDidChange change"
+ "-CMSMNotificationUtilities- %s: Clients being resumed since application is in the foreground"
+ "-CMSMNotificationUtilities- %s: Delaying nowPlayingAppIsPlaying = false notification"
+ "-CMSMNotificationUtilities- %s: ERROR: failed to create gCMSM.nowPlayingAppIsPlayingDidChangeTimer"
+ "-CMSMNotificationUtilities- %s: External mute context added to notification payload"
+ "-CMSMNotificationUtilities- %s: Foreground and active sessions being notified of SomeNonAmbientAudioCategoryClientIsPlayingDidChange change to %d"
+ "-CMSMNotificationUtilities- %s: Going to post AvailableFormatsDidChange"
+ "-CMSMNotificationUtilities- %s: Not posting redundant notification"
+ "-CMSMNotificationUtilities- %s: Notifying client %{public}@ that IsOutputMuted with payload = %{public}@"
+ "-CMSMNotificationUtilities- %s: Notifying client %{public}@ that UserIntentToUnmuteDidChange with payload = %{public}@"
+ "-CMSMNotificationUtilities- %s: Now sending AvailableFormatsDidChange notification with formats = %@"
+ "-CMSMNotificationUtilities- %s: Posting AudioModeDidChange to session '%@', AudioMode changed to '%@'"
+ "-CMSMNotificationUtilities- %s: Posting PreferHeadphonesOverCarsAndSpeakersDidChange notification with %{BOOL}u"
+ "-CMSMNotificationUtilities- %s: Posting ReporterIDsDidChange to session '%@', ReporterIDs changed to '%@'"
+ "-CMSMNotificationUtilities- %s: Posting kCMSessionNotification_PiPIsPossibleDidChange to %@ (%@) to %s"
+ "-CMSMNotificationUtilities- %s: Sending AllowBluetoothAccessoryToRequestAudioRouteDidChange notification with %{BOOL}u"
+ "-CMSMNotificationUtilities- %s: activePhoneCallInfo has changed to %@"
+ "-CMSMNotificationUtilities- %s: creating nowPlayingAppIsPlayingDidChangeTimer"
+ "-CMSMNotificationUtilities- %s: have a timer already; releasing gCMSM.nowPlayingAppIsPlayingDidChangeTimer and rescheduling it"
+ "-CMSMNotificationUtilities- %s: phoneCallOrRingtoneExists has changed to '%{BOOL}u'"
+ "-CMSMNotificationUtilities- %s: releasing gCMSM.nowPlayingAppIsPlayingDidChangeTimer"
+ "-CMSMNotificationUtilities- %s: someSessionIsPlayingDidChange payload: %@"
+ "-CMSMNotificationUtilities- %s: volumeCategory == %@"
+ "-CMSMUtilities-"
+ "-CMSMUtilities- %s: "
+ "-CMSMUtilities- %s: %@(%@)[%p] with audio category = %@ is playing"
+ "-CMSMUtilities- %s: Apply SharePlay special volume behaviors for active call session"
+ "-CMSMUtilities- %s: CATEGORY~MODE: %@"
+ "-CMSMUtilities- %s: Called"
+ "-CMSMUtilities- %s: Called for session: %@"
+ "-CMSMUtilities- %s: Checking if application has any client that is a lock stopper"
+ "-CMSMUtilities- %s: Clearing overrides for an active phoneCall session."
+ "-CMSMUtilities- %s: CurrentlyControllingFlags for SharePlay call: 0x%x; requiredFlags: %s; desiredFlags: %s; HwControlFlags: 0x%x; requiredFlags: %s; desiredFlags: %s;"
+ "-CMSMUtilities- %s: Error calling _CMSessionMgrPerformVolumeOperation for Absolute AudioVideo: %d"
+ "-CMSMUtilities- %s: Error calling _CMSessionMgrPerformVolumeOperation for Absolute PhoneCall: %d"
+ "-CMSMUtilities- %s: Found Match for background GPS entitlement"
+ "-CMSMUtilities- %s: Found SharePlay-capable active call session %@"
+ "-CMSMUtilities- %s: Found SharePlay-capable active media session %@"
+ "-CMSMUtilities- %s: Found a match for AudioSessionID %d: %@. "
+ "-CMSMUtilities- %s: Found a match for CoreSession = '%@'"
+ "-CMSMUtilities- %s: Found playing MXSession %llx with mute priority %@"
+ "-CMSMUtilities- %s: Found presence of MXSession %llx with mute priority %@"
+ "-CMSMUtilities- %s: Getting IAPAppProcessIDIsUsingAccessory for display ID: %@"
+ "-CMSMUtilities- %s: Handing over interruption of session '%@' from session '%@' to interrupting session '%@'"
+ "-CMSMUtilities- %s: HwControlFlags: 0x%x; requiredFlags: %s; desiredFlags: %s;"
+ "-CMSMUtilities- %s: IAPAppProcessIDIsUsingAccessory not found."
+ "-CMSMUtilities- %s: IAPAppProcessIDIsUsingAccessory returned: %d"
+ "-CMSMUtilities- %s: IAPAudioShouldPauseAudioOnHeadsetDisconnect not found."
+ "-CMSMUtilities- %s: Invalid PID in background entitlement check"
+ "-CMSMUtilities- %s: Invalid PID."
+ "-CMSMUtilities- %s: Iterating CoreSession = '%@'"
+ "-CMSMUtilities- %s: Notification and applier are both NULL"
+ "-CMSMUtilities- %s: Notification and applier are both non-NULL"
+ "-CMSMUtilities- %s: Playing a system sound that MUST be heard; CurrentRouteHasVolumeControl = NO"
+ "-CMSMUtilities- %s: Posting notifyd style notification for FadeInAppliedForPlaybackHandoff with duration %llu"
+ "-CMSMUtilities- %s: Posting notifyd style notification for FadeOutAppliedForPlaybackHandoff with duration %llu"
+ "-CMSMUtilities- %s: Returned with err=%d"
+ "-CMSMUtilities- %s: Returning %@ for %@ found in map."
+ "-CMSMUtilities- %s: Returning %{public}@ for %u found in map."
+ "-CMSMUtilities- %s: Route %d: %@"
+ "-CMSMUtilities- %s: Route change involving BT LE with VoiceOver active"
+ "-CMSMUtilities- %s: Sending %@ command to MXSessionID = %llx, part of CoreSession(%@)"
+ "-CMSMUtilities- %s: Setting pidToInheritAppStateFrom for session '%@' to %d"
+ "-CMSMUtilities- %s: Setting userMuted as false for an active session."
+ "-CMSMUtilities- %s: SomeRecordingSessionPresentThatDisallowsSystemSounds: %s Session: %@"
+ "-CMSMUtilities- %s: UIShouldIgnoreRemoteControlEvents for pid %d not found."
+ "-CMSMUtilities- %s: UIShouldIgnoreRemoteControlEvents for pid %d: %@."
+ "-CMSMUtilities- %s: Updating VoiceAssistant Active state for CarPlay Endpoint failed, err = %d."
+ "-CMSMUtilities- %s: Updating sessions with PID %d to %@, the current appState of %d"
+ "-CMSMUtilities- %s: VibePattern is going to (old style) vibe."
+ "-CMSMUtilities- %s: VibePattern is going to vibe with haptic engine style pattern."
+ "-CMSMUtilities- %s: VibePattern is going to vibe."
+ "-CMSMUtilities- %s: VoiceOver duck fade duration == %1.3f sec"
+ "-CMSMUtilities- %s: airPlayVideoIsActive = %s"
+ "-CMSMUtilities- %s: currentRouteTypes=%@"
+ "-CMSMUtilities- %s: longbufferduration == %.3f"
+ "-CMSMUtilities- %s: modeIsValidForCategory %d for %@~%@"
+ "-CMSMUtilities- %s: notification '%@' being posted to client '%@'"
+ "-CMSMUtilities- %s: notification '%@' being posted to client '%@' for session '%@'"
+ "-CMSMUtilities- %s: old playAndRecordSpeechState = %d, new playAndRecordSpeechState = %d"
+ "-CMSMUtilities- %s: pSession->config.routingContextUUID=%@, routingContextUUID=%@"
+ "-CMSMUtilities- %s: playingSessions = %p, playingSessionsCount = %d"
+ "-CMSMUtilities- %s: result = %s"
+ "-CMSMUtilities- %s: returning mostImportantPlayingSession = %@"
+ "-CMSMUtilities- %s: returning someSessionIsActiveThatPrefersNoInterruptionsByRingtonesAndAlerts %d"
+ "-CMSM_CoreServices- %s: '%@' has genre='%@' and genreID='%@'"
+ "-CMSM_CoreServices- %s: LSApplicationExtensionRecord is NULL"
+ "-CMSM_CoreServices- %s: LSApplicationProxy is NULL"
+ "-CMSM_CoreServices- %s: LSApplicationWorkspace is NULL"
+ "-CMSM_CoreServices- %s: LSBundleRecord is NULL"
+ "-CMSM_CoreServices- %s: Observer for monitoring changes in device management policy is NULL"
+ "-CMSM_CoreServices- %s: Unable to dlopen CoreServices framework"
+ "-CMSM_IDSClient- %s: Failed to find kMXSession_IDSSendMessageOptionQueueOneIdentifierKey"
+ "-CMSM_IDSClient- %s: Failed to send the message '%@' with identifier=%@ and error \"%@\"."
+ "-CMSM_IDSClient- %s: No nearby device, dropping the message '%@'"
+ "-CMSM_IDSClient- %s: Successfully sent the message with identifier=%@"
+ "-CMSM_IDSClient- %s: Unable to dlopen idsFramework"
+ "-CMSM_IDSClient- %s: playingSessions is NULL."
+ "-CMSM_IDSConnection- %s: AddRemotePlayingInfo: sIDSInfo.remotePlayingSessions=%@, dict=%@"
+ "-CMSM_IDSConnection- %s: Nothing else to do."
+ "-CMSM_IDSConnection- %s: PickableRoutes has changed"
+ "-CMSM_IDSConnection- %s: Received sharedAudioRouteMacAddress %@ from remote. Current sharedAudioRouteMacAddress: %@. clearSharedAudioRoute %d"
+ "-CMSM_IDSConnection- %s: RemoveRemotePlayingInfo: sIDSInfo.remotePlayingSessions=%@"
+ "-CMSM_IDSConnection- %s: Resetting sIDSInfo.remotePlayingSessions"
+ "-CMSM_IDSConnection- %s: Resetting waitingForGizmoPlayingInfo to NO."
+ "-CMSM_IDSConnection- %s: Timeout occurred at CMSM_IDSConnection_RouteToSharedAudioRouteUponReceivingOwnership"
+ "-CMSM_IDSConnection- %s: calling to set ownership on port=%u"
+ "-CMSM_IDSConnection- %s: creating sIDSInfo.waitForRemoteToReplyWithInitialPlayingInfoTimer, timer delay = %f"
+ "-CMSM_IDSConnection- %s: identifier=%@"
+ "-CMSM_IDSConnection- %s: nearby paired device = %p, uniqueIDOverride=%@"
+ "-CMSM_IDSConnection- %s: port=%u went away, remove it from sIDSInfo.sharedAudioRoutePortIDs"
+ "-CMSM_IDSConnection- %s: releasing sIDSInfo.waitForRemoteToReplyWithInitialPlayingInfoTimer"
+ "-CMSM_IDSConnection- %s: remotePlayingInfo=%@"
+ "-CMSM_IDSConnection- %s: sharedAudioRoutePortIDs=%@"
+ "-CMSM_IDSConnection- %s: someClientIsPlaying on remote=%s"
+ "-CMSM_IDSConnection- %s: waitingForGizmoPlayingInfo = %s"
+ "-CMSM_IDSServer- %s: newSessionIdRef=%@, currentSessionIdRef=%@"
+ "-CMSM_IDSServer- %s: no remote playing sessions for a while; taking ownership to iPhone"
+ "-CMSM_IDSServer- %s: no remote playing sessions; starting timer on iPhone"
+ "-CMSM_IDSServer- %s: playingSessions=%@"
+ "-CMSM_IDSServer- %s: remote playing sessions; resetting timer on iPhone"
+ "-CMSM_IDSServer- %s: remoteRouteIsShared=%s, remotePlayingSessions=%@"
+ "-CMSM_IDSServer- %s: sessionInfo=%@"
+ "-CMSPowerLogs- %s: inPowerLogEventName = %@, inPowerLogData = %@\n"
+ "-CMSSleep- %s: >>> idleSleepPreventorAllocated already allocated"
+ "-CMSSleep- %s: Assertion for client %@ pid %d being released"
+ "-CMSSleep- %s: Extending process assertion for client %@ with PID : %d"
+ "-CMSSleep- %s: Getting process assertion for client %@ -- stopping from being suspended"
+ "-CMSSleep- %s: Getting process assertions for client %@ -- stopping from being suspended"
+ "-CMSSleep- %s: Getting temporary process assertion for client %@ with PID : %d"
+ "-CMSSleep- %s: NO idleSleepPreventor to release"
+ "-CMSSleep- %s: No session"
+ "-CMSSleep- %s: Session is NULL"
+ "-CMSSleep- %s: Session is NULL "
+ "-CMSSleep- %s: called"
+ "-CMSSleep- %s: called [%p] %@"
+ "-CMSSleep- %s: called ssid: %d pid: %d"
+ "-CMSSleep- %s: client '%@' >>> NO idleSleepPreventor to release"
+ "-CMSSleep- %s: client '%@' >>> idleSleepPreventorAllocated already allocated"
+ "-CMSSleep- %s: creating resumeBackgroundAppTimeDidFinish"
+ "-CMSSleep- %s: creating session idleSleepPreventorUpdaterTimer, serial queue(ACQ) = %p"
+ "-CMSSleep- %s: idleSleepPreventor '%@', ID = %d allocated"
+ "-CMSSleep- %s: idleSleepPreventor '%@', NOT allocated"
+ "-CMSSleep- %s: idleSleepPreventor with ID = '%d' NOT released"
+ "-CMSSleep- %s: idleSleepPreventor with ID = '%d' released"
+ "-CMSSleep- %s: releasing [session extendBackgroundAppAssertionTimer]"
+ "-CMSSleep- %s: releasing [session idleSleepPreventorUpdaterTimer]"
+ "-CMSSleep- %s: releasing [session resumeBackgroundAppUpdaterTimer]"
+ "-CMSSleep- %s: releasing session idleSleepPreventorUpdaterTimer"
+ "-CMSSleep- %s: session: '%@' [%p], isPlaying: %d."
+ "-CMSSleep- %s: ssid = %d does NOT need prewarmIdleSleepPreventor"
+ "-CMSUtilities-"
+ "-CMSUtilities- %s: "
+ "-CMSUtilities- %s: %@ (%@) playsToCarAltAudio = %s"
+ "-CMSUtilities- %s: %@ (%@) playsToCarMainAudio = %s"
+ "-CMSUtilities- %s: %@ NOT interrupting %@ because %@ mixes with everyone"
+ "-CMSUtilities- %s: %@ NOT interrupting %@ because processing and recording in same pid is ok"
+ "-CMSUtilities- %s: %@ handing over ducking to %@ because both duck other sessions"
+ "-CMSUtilities- %s: %@ will NOT interrupt %@ because (%@) is an internal MX core session"
+ "-CMSUtilities- %s: Adding the reporterID %@ for session:%@ [%p]"
+ "-CMSUtilities- %s: Application does not have a valid assertions but it is a GPS app; allowing audio playback"
+ "-CMSUtilities- %s: Application does not have a valid reason to play audio in the background running state"
+ "-CMSUtilities- %s: Application has a valid reason to run in the background and play mixable audio, reason %llu"
+ "-CMSUtilities- %s: Application is awake due to a watch connectivity reason and might want to become the now playing app."
+ "-CMSUtilities- %s: Attention :: Client %@ with PID %d being interrupted"
+ "-CMSUtilities- %s: Attention :: Client %@ with PID %d being resumed (most likely as it is back in the foreground), isPlaying : %d ; waitingToResume : %d"
+ "-CMSUtilities- %s: AudioObjectGetPropertyData( kVirtualAudioPlugInPropertyRouteConfigurationIsDisruptive ) failed with err = %d = %.4s"
+ "-CMSUtilities- %s: CMSUtility_CopyCurrentCategoryAndDeviceRoute failed with err = %ld"
+ "-CMSUtilities- %s: Calling AudioToolboxServerHandleInterruption directly to service interruption_cmd for session '%@' %@"
+ "-CMSUtilities- %s: Checking if application has any client that is a lock stopper"
+ "-CMSUtilities- %s: Checking phone call priority entitlement for client %@ with PID: %d"
+ "-CMSUtilities- %s: Checking whether extension has entitlement to record audio for PID: %d"
+ "-CMSUtilities- %s: Client %@ %@ a extension; it %@ record audio."
+ "-CMSUtilities- %s: Client %@ has entitlement to record audio in an extension"
+ "-CMSUtilities- %s: Client %@ with PID %d being interrupted because of smart cover secure microphone policy"
+ "-CMSUtilities- %s: Client '%{public}@' is in the background and isn't allowed to start recording clientPID=%{public}@ hasEntitlementToStartRecordingInTheBackground=%{BOOL}u clientPriority=%{public}@} doesInterAppAudio=%{BOOL}u sessionIsResumingRecordingAfterInterruption=%{BOOL}u sessionIsWithinGracePeriodAfterStoppedInBackground=%{BOOL}u sessionAllowedToStartRecordingTemporarily=%{BOOL}u"
+ "-CMSUtilities- %s: Client allowed to start playing so it can become the NowPlayingApp."
+ "-CMSUtilities- %s: Client can start playing"
+ "-CMSUtilities- %s: Client connects to external accessories."
+ "-CMSUtilities- %s: Client is awake due to a watch connectivity reason and might want to become the now playing app."
+ "-CMSUtilities- %s: Client is the iPod app; can stop any client."
+ "-CMSUtilities- %s: Client is the nowPlayingApp (based on display ID); can do pretty much anything it wants to."
+ "-CMSUtilities- %s: Client is the nowPlayingApp; can do pretty much anything it wants to."
+ "-CMSUtilities- %s: Client temporarily allowed to start playing so it can become the NowPlayingApp."
+ "-CMSUtilities- %s: Device hints not including buffer size because it is invalid"
+ "-CMSUtilities- %s: DisplayID is %@."
+ "-CMSUtilities- %s: Error sending Volume Changes to Audio ToolBox, Reporter not started for session %@: isActive: %s reporterStarted: %s"
+ "-CMSUtilities- %s: Error(%d) setting Interruption style for Alarms on AudioAccessory."
+ "-CMSUtilities- %s: Failed to allocate sessionsToDuck!!!"
+ "-CMSUtilities- %s: For client %@ returning %@"
+ "-CMSUtilities- %s: For client %@ tmpSessionAudioBehaviour %@"
+ "-CMSUtilities- %s: Found a match for CoreSession = '%@'"
+ "-CMSUtilities- %s: Hah ! %@ will NOT interrupt %@ because (%@) plays audio over CarPlay alternate audio"
+ "-CMSUtilities- %s: Hah ! %@ will interrupt %@ because %@ is a high-priority category"
+ "-CMSUtilities- %s: Hah ! %@ will interrupt %@ because %@ is active in the background, not playing and requires routing"
+ "-CMSUtilities- %s: Hah ! %@ will interrupt %@ because %@ is assistant and we don't want mixable audio to corrupt the recording."
+ "-CMSUtilities- %s: II a: destinationVAD = SystemRemote"
+ "-CMSUtilities- %s: II b: destinationVAD = Default"
+ "-CMSUtilities- %s: II c: destinationVAD = SystemLocal; Perhaps VoiceOver, do nothing"
+ "-CMSUtilities- %s: II d: destinationVAD = Siri Output VAD"
+ "-CMSUtilities- %s: Interruptor = VoiceOver, is playing over BT LE; ducking"
+ "-CMSUtilities- %s: Interruptor hardware safety session interrupting victim: %s"
+ "-CMSUtilities- %s: Invalid PID in background entitlement check"
+ "-CMSUtilities- %s: Iterating CoreSession = '%@'"
+ "-CMSUtilities- %s: Mixable session '%@' that wantsToPauseSpokenAudio and victim is a silent primary spoken audio session '%@'; skipping this routine"
+ "-CMSUtilities- %s: Mixable session '%@' that wantsToPauseSpokenAudio and victim is a spoken audio session '%@' that has opted out of being interrupted; skipping this routine"
+ "-CMSUtilities- %s: Mixable session '%@' that wantsToPauseSpokenAudio interrupting non-silent primary spoken audio session '%@'"
+ "-CMSUtilities- %s: Mixable voice assistant session interrupting an actively recording audio session"
+ "-CMSUtilities- %s: No volume pref set for route: '%@' while Siri is active, using default."
+ "-CMSUtilities- %s: None of the cases apply (?) - do nothing"
+ "-CMSUtilities- %s: Not ducking VoiceOver client"
+ "-CMSUtilities- %s: Not interrupting %{public}@, as CarSession is going active for AirPlay Video"
+ "-CMSUtilities- %s: OK, not really"
+ "-CMSUtilities- %s: PhoneCall/Alarm: Category/Priority can interrupt from the background"
+ "-CMSUtilities- %s: Plist has no Default value"
+ "-CMSUtilities- %s: Posting kMXSessionNotification_Interruption to CarSession"
+ "-CMSUtilities- %s: RESUMING session '%@' [%p]%s"
+ "-CMSUtilities- %s: Resetting all individual play states for '%@'"
+ "-CMSUtilities- %s: Returning, as this is not a Sidekick Siri or Alarm session. %@ / %@ (PID)."
+ "-CMSUtilities- %s: Route to preferred route for TipiPriorityChange: oldTipiPriority %d newTipiPriority %d"
+ "-CMSUtilities- %s: Session %@ allowedToInterrupt current AirPlay NP app = %s"
+ "-CMSUtilities- %s: Session '%@' application state is :: '%@'"
+ "-CMSUtilities- %s: Session '%@' has set prefersToInterruptActiveRecordingSessions, interrupting an actively recording audio session"
+ "-CMSUtilities- %s: Session '%@' is a long form video session and is currently system music so we are remaining system music"
+ "-CMSUtilities- %s: Session '%@' is not allowed to interrupt current AirPlaying NP app"
+ "-CMSUtilities- %s: Session '%{public}@' has output muted"
+ "-CMSUtilities- %s: Session is NULL"
+ "-CMSUtilities- %s: Session trying to start recording is %s extension"
+ "-CMSUtilities- %s: Stark is NOT connected; ducking non-Stark session that should be ducked"
+ "-CMSUtilities- %s: There are %ld entries in the reporter ID array. It must not exceed one entry!"
+ "-CMSUtilities- %s: VADs '%@' and '%@' routed to a different physical device"
+ "-CMSUtilities- %s: VADs '%@' and '%@' routed to the same physical device"
+ "-CMSUtilities- %s: VoiceAssistant has started recording & someone else is active. Calling beginInterruption"
+ "-CMSUtilities- %s: VoiceAssistant is allowed to control hardware while attempting to interrupt spoken audio session"
+ "-CMSUtilities- %s: Volume for session '%@' : %f [VAD: '%@' route: '%@' deviceID: '%@' routeSubtype: '%@' category: '%@' mode: '%@']"
+ "-CMSUtilities- %s: [%p] '%@' ducking by %1.3f in %1.3f sec"
+ "-CMSUtilities- %s: activePorts %@ connectedWirelessPorts %@"
+ "-CMSUtilities- %s: airPlayVideoIsActive=%{BOOL}u, session->state.isAudioOnlyAirPlayVideoActive=%{BOOL}u, cmd = %d"
+ "-CMSUtilities- %s: calling _CMSessionEndInterruption because the client is backgrounded"
+ "-CMSUtilities- %s: calling _CMSessionEndInterruption because the client is suspended"
+ "-CMSUtilities- %s: client '%@' state being changed to %d"
+ "-CMSUtilities- %s: found a ducker: [%p] '%@'"
+ "-CMSUtilities- %s: interruptor = '%@' '%@', sessionsToDuckCount = %d"
+ "-CMSUtilities- %s: isSessionRouteEligibleForTipi %d"
+ "-CMSUtilities- %s: mixable session that wants to pause spoken audio but spoken audio session has opted out of being interrupted. skipping this routine"
+ "-CMSUtilities- %s: mixable session that wants to pause spoken audio interrupting spoken audio session"
+ "-CMSUtilities- %s: not a silent ringtone, not interrupting"
+ "-CMSUtilities- %s: number of reporter IDs is 0"
+ "-CMSUtilities- %s: outCategory = %@, outMode = %@, outRoute = %@, outDeviceID = %@, outRouteSubtype = %@"
+ "-CMSUtilities- %s: pid = %d, pidToInheritAppStateFrom = %d, predictableState = %@, state = %@"
+ "-CMSUtilities- %s: returning %s"
+ "-CMSUtilities- %s: session '%@' doesn't actually play audio"
+ "-CMSUtilities- %s: session '%@' is not eligible for SmartRouting"
+ "-CMSUtilities- %s: session '%@' is not eligible for Triangle"
+ "-CMSUtilities- %s: session is NULL"
+ "-CMSUtilities- %s: session is NULL."
+ "-CMSUtilities- %s: session is independent, not eligible for SR"
+ "-CMSUtilities- %s: silent ringtone is active: interrupting"
+ "-CMSUtilities- %s: singleSessionToBeInterruptedForSpecificResource: '%@' [%p] with audioCategory: '%@' is in foreground; CANNOT be interrupted."
+ "-CMSUtilities- %s: value = %1.3f for ThirdPartyTV"
+ "-CMSVARouting-"
+ "-CMSVARouting- %s: "
+ "-CMSVARouting- %s: %@ is A2DP and IS the picked route; Clearing %@"
+ "-CMSVARouting- %s: %@ is A2DP and is NOT the picked route; Clearing"
+ "-CMSVARouting- %s: ( CFGetTypeID( connectedPorts ) != CFArrayGetTypeID() ), return empty array."
+ "-CMSVARouting- %s: ********* cmsmCopyCurrentActiveRoutesInfoForVADUID() didn't come up with one **********"
+ "-CMSVARouting- %s: ********* cmsmUpdateCurrentActiveRoutesInfo didn't come up with one **********"
+ "-CMSVARouting- %s: Adding Receiver to nonDefault builtIn route(s) because Speaker is the defaultPort."
+ "-CMSVARouting- %s: Adding Speaker to nonDefault builtIn route(s) because Receiver is the defaultPort."
+ "-CMSVARouting- %s: Checking port number %d"
+ "-CMSVARouting- %s: Creating PickableRoutes for '%@' since it wasn't found in the cache"
+ "-CMSVARouting- %s: Deaggregating AND making all these ports UNroutable: %@"
+ "-CMSVARouting- %s: Endpoint is NULL"
+ "-CMSVARouting- %s: Found quiesceable wired port [%u]"
+ "-CMSVARouting- %s: GetData(kVirtualAudioPlugInPropertyActiveNonWirelessPortsForRouteConfiguration) failed with err = %d = '%.4s'"
+ "-CMSVARouting- %s: GetData(kVirtualAudioPlugInPropertyActiveNonWirelessPortsForRouteConfiguration) returned NULL."
+ "-CMSVARouting- %s: GetData(kVirtualAudioPlugInPropertyConnectedPorts) failed with err = %d = '%.4s'"
+ "-CMSVARouting- %s: Match found currentEntry: %@ pickedRouteDescription: %@"
+ "-CMSVARouting- %s: No QuiesceableWired ports, returning nil"
+ "-CMSVARouting- %s: No active ports for category '%@'"
+ "-CMSVARouting- %s: No actual change to pickable routes, NOT sending notification to clients"
+ "-CMSVARouting- %s: No connected ports, returning empty array"
+ "-CMSVARouting- %s: No endpoint for port"
+ "-CMSVARouting- %s: Non preferred HFP route description array: %@"
+ "-CMSVARouting- %s: Non-default built-in route description: %@"
+ "-CMSVARouting- %s: Port number %d needs to be added to the list"
+ "-CMSVARouting- %s: Quiesceable wired routes descriptions: %@"
+ "-CMSVARouting- %s: QuiesceableWiredPortsConnection feature is disabled"
+ "-CMSVARouting- %s: Reading PickableRoutes for '%@' from the cache"
+ "-CMSVARouting- %s: Returning route name '%@' since no port is available"
+ "-CMSVARouting- %s: Session '%@' appended sub-port preference"
+ "-CMSVARouting- %s: Session '%@' getting preferred inputs"
+ "-CMSVARouting- %s: Session '%@' replaced sub-port preferences at index %d"
+ "-CMSVARouting- %s: Session '%@' updating sub-port preferences '%@'"
+ "-CMSVARouting- %s: Session is NULL"
+ "-CMSVARouting- %s: SystemInputPicker feature is disabled"
+ "-CMSVARouting- %s: Unconnected BT endpoint ID=%@"
+ "-CMSVARouting- %s: Updating pickable routes descriptions"
+ "-CMSVARouting- %s: Wireless route description: %@"
+ "-CMSVARouting- %s: Zero active devices (or perhaps no active ports for current category"
+ "-CMSVARouting- %s: Zero active devices (or perhaps no active ports for current category."
+ "-CMSVARouting- %s: Zero active ports for current category || ( CFGetTypeID( activePorts ) != CFArrayGetTypeID() )"
+ "-CMSVARouting- %s: [%ld] portNumber = %u, portType = '%.4s'"
+ "-CMSVARouting- %s: allocation for routeDescription failed"
+ "-CMSVARouting- %s: category = %@; mode = %@; activationContext = %@"
+ "-CMSVARouting- %s: category is NULL"
+ "-CMSVARouting- %s: category is NULL, return empty array."
+ "-CMSVARouting- %s: connectedAudioPorts is NULL"
+ "-CMSVARouting- %s: connectedPorts is NULL, return empty array."
+ "-CMSVARouting- %s: connectedPortsList is nil"
+ "-CMSVARouting- %s: connectedPorts[%d] = %d"
+ "-CMSVARouting- %s: currentBTMacAddress=%@, iterBTMacAddress=%@"
+ "-CMSVARouting- %s: currentRouteTypes = %@"
+ "-CMSVARouting- %s: default Route Description= %@"
+ "-CMSVARouting- %s: deviceIDIsCarBluetooth=%s"
+ "-CMSVARouting- %s: did not find any picked route; picking iPhone"
+ "-CMSVARouting- %s: did nothing: all args NULL"
+ "-CMSVARouting- %s: found it!"
+ "-CMSVARouting- %s: making all these ports UNroutable: %@"
+ "-CMSVARouting- %s: mode is NULL"
+ "-CMSVARouting- %s: mode is NULL, return empty array."
+ "-CMSVARouting- %s: no BT endpoints"
+ "-CMSVARouting- %s: numConnectedPorts for category = '%.4s' is %d"
+ "-CMSVARouting- %s: override route could not be unpicked; no session is controlling routing"
+ "-CMSVARouting- %s: picked route description= %@"
+ "-CMSVARouting- %s: port = %d, vadCategory = %.4s"
+ "-CMSVARouting- %s: port = %ld, currentOutputPort = %ld, shouldAutoJackInOnConnect = %s"
+ "-CMSVARouting- %s: portToRoute = %ld"
+ "-CMSVARouting- %s: preferred inputs : '%@'"
+ "-CMSVARouting- %s: productID=%@ for routeUID=%@"
+ "-CMSVARouting- %s: returned '%@'"
+ "-CMSVARouting- %s: returned routeTypes = %@, routeIdentifiers = %@, routeSubtypes = %@"
+ "-CMSVARouting- %s: returning %s"
+ "-CMSVARouting- %s: routeDict could not be created"
+ "-CMSVARouting- %s: wirelessPorts=%@"
+ "-CMSessionManager_IDS- %s: IDSService is NULL"
+ "-CMSessionManager_IDS- %s: sIDSCopyIDForDevice is NULL"
+ "-CMSessionManager_IDS- %s: sIDSHandle is NULL "
+ "-CMSessionManager_InterruptionActionMapper- %s: session '%@' is not eligible to play over SmartRouting shared audio route"
+ "-CMSessionManager_InterruptionActionMapper- %s: session '%@' is not eligible to play over Triangle shared audio route"
+ "-CMSessionManager_NowPlaying- %s: called"
+ "-CMSessionManager_NowPlaying- %s: releasing gCMSM.nowPlayingAppIsPlayingDidChangeTimer"
+ "-CMSessionMgr- %s: "
+ "-CMSessionMgr- %s:      NULL IOProc is NOT running -- will freewheel"
+ "-CMSessionMgr- %s:      NULL IOProc is running -- audio device will not stop"
+ "-CMSessionMgr- %s: %@ [%p]."
+ "-CMSessionMgr- %s: %ld sessions will be ducked by %1.3f in %1.3f sec"
+ "-CMSessionMgr- %s: '%@' %s playing"
+ "-CMSessionMgr- %s: '%@' **** CanBeAndAllowedToBeNowPlayingApp = %s, isNowPlayingApp = %s"
+ "-CMSessionMgr- %s: ... to interrupt '%@' [%p]"
+ "-CMSessionMgr- %s: >>> audio device start idleSleepPreventorAllocated already allocated"
+ "-CMSessionMgr- %s: Active victim %@; Playing %d; Mixable %d; Required flags %s"
+ "-CMSessionMgr- %s: Added resource with token: %p."
+ "-CMSessionMgr- %s: Adding built-in mic to speaker override"
+ "-CMSessionMgr- %s: Audio category for session %@ is phone call; iOS is doing phone call on Stark"
+ "-CMSessionMgr- %s: Audio device has already started! cmsmCreateAudioDeviceStartIdleSleepPreventor NOT called."
+ "-CMSessionMgr- %s: Audio device has already stopped! cmsmReleaseAudioDeviceStartIdleSleepPreventor NOT called."
+ "-CMSessionMgr- %s: Audio device start changed to : %s"
+ "-CMSessionMgr- %s: Audio device start state == %s"
+ "-CMSessionMgr- %s: BeginInterruption is a no-op"
+ "-CMSessionMgr- %s: CANNOT read ResourceList.plist."
+ "-CMSessionMgr- %s: Car session already interrupted synchronously"
+ "-CMSessionMgr- %s: CarOutput port = %u to be made routable, clearing overrides"
+ "-CMSessionMgr- %s: CarSession [%p] going active, make StarkMainAudio port unroutable"
+ "-CMSessionMgr- %s: CarSession going active for AirPlay Video - do not make StarkMainAudio port unroutable"
+ "-CMSessionMgr- %s: Changing A/V volume based on user preference."
+ "-CMSessionMgr- %s: Client %@ should not be using CMSession property PickedRouteWithPassword!"
+ "-CMSessionMgr- %s: Client '%@' did not interrupt '%@'; not sending EndInterruption"
+ "-CMSessionMgr- %s: Client '%@' going active will be disruptive (someClientIsPlaying: %d; isSessionGoingActiveDisruptive: %d; NOT calling BeginInterruption()"
+ "-CMSessionMgr- %s: Client '%@' going active won't be disruptive; calling BeginInterruption()"
+ "-CMSessionMgr- %s: Client '%@' isEligibleForPreemptivePort=%{BOOL}u, isSessionOnlyPlayingLocally=%{BOOL}u"
+ "-CMSessionMgr- %s: Client '%@' sessionIsEligibleForAirPlaySuggestions=%{BOOL}u"
+ "-CMSessionMgr- %s: Client '%@' was suspended while interrupted or client calling EndInterrupted exited; not waking it up"
+ "-CMSessionMgr- %s: Client has set doNotNotifyOtherSessionsOnNextInactive. Skipping notifying other sessions."
+ "-CMSessionMgr- %s: Client was the nowPlayingApp but does not have a background audio entitlement; defaulting to iPod"
+ "-CMSessionMgr- %s: Coriander feature is disabled"
+ "-CMSessionMgr- %s: Could not create sessionsToUpdate."
+ "-CMSessionMgr- %s: ERROR creating theDefaultSession: %d"
+ "-CMSessionMgr- %s: EnableTetheredDisplayPortMode is set to YES"
+ "-CMSessionMgr- %s: Error %d while setting device format to %@"
+ "-CMSessionMgr- %s: Error in copying system audio routing context, err=%d"
+ "-CMSessionMgr- %s: Error in copying system mirroring routing context, err=%d"
+ "-CMSessionMgr- %s: Error retrieving stream formats list from VAD"
+ "-CMSessionMgr- %s: FAILED : CFNumberCreate"
+ "-CMSessionMgr- %s: FAILED: clientName = %@, key = %@, value = %@: returning err = %d"
+ "-CMSessionMgr- %s: FAILED: cmsSetClientPID -- CFNumberRef type expected in parameter"
+ "-CMSessionMgr- %s: FAILED: cmsSetClientPID -- Invalid PID"
+ "-CMSessionMgr- %s: FAILED: cmsSetClientPID -- NULL pointer passed for PID"
+ "-CMSessionMgr- %s: FAILURE: audio device apparently has no available sample rates, sticking with default %.3f Hz"
+ "-CMSessionMgr- %s: FigVibratorInitialize failed with err = %d"
+ "-CMSessionMgr- %s: FigVibratorIsVibratorAvailable available"
+ "-CMSessionMgr- %s: For client %@, AvailableOutputStreamFormats: %@"
+ "-CMSessionMgr- %s: For session: '%@' Original Category: '%@' Category based on default built in route: '%@'"
+ "-CMSessionMgr- %s: For session: '%@' Original Category: '%@' Category based on mode: '%@'"
+ "-CMSessionMgr- %s: For session: '%@' Original Category: '%@' Category based on setting: '%@'"
+ "-CMSessionMgr- %s: Getting nowPlayingAppPID = '%d', nowPlayingAppIsPlaying : %s"
+ "-CMSessionMgr- %s: Going to also interrupt client '%{public}@' as it shadows '%{public}@' for options %{public}@"
+ "-CMSessionMgr- %s: Going to set speech state to speaking"
+ "-CMSessionMgr- %s: Going to unduck car session because the interruptee '%@' [%p] ducked the car session previously."
+ "-CMSessionMgr- %s: Grabbing available routes from %{public}@ for %{public}@"
+ "-CMSessionMgr- %s: Handing over override route PhoneCall<->RemoteVoiceChat"
+ "-CMSessionMgr- %s: Ignoring set of preferredOutputSampleRate; changing sample rate to 48000 instead."
+ "-CMSessionMgr- %s: In SetProperty: Setting numPCMFrames to %d"
+ "-CMSessionMgr- %s: Inactive session starting to play or routingContextChange; let's call BeginInterruption again"
+ "-CMSessionMgr- %s: Invalid CMSessionAudioHardwareControlFlags (0x%x): You cannot both require and desire a particular AudioHardwareControl.\n"
+ "-CMSessionMgr- %s: Invalid PID in application state callback"
+ "-CMSessionMgr- %s: It's a HomePod and '%@' will playing to a different VAD than '%@'"
+ "-CMSessionMgr- %s: Let Now Playable app %{public}@ take control flags from %{public}@ for media multitasking"
+ "-CMSessionMgr- %s: LongFormVideoApps array contained invalid value(s)"
+ "-CMSessionMgr- %s: LongFormVideoApps was not of the expected type"
+ "-CMSessionMgr- %s: MRMediaRemoteSendCommandToApp function is not available on this platform."
+ "-CMSessionMgr- %s: MXCoreSession [%p] is being initialized"
+ "-CMSessionMgr- %s: Mode invalid for current category."
+ "-CMSessionMgr- %s: NO audio device start idleSleepPreventor to release"
+ "-CMSessionMgr- %s: NO volumeButtonClient; we'll just get/set prefs, not current volumes"
+ "-CMSessionMgr- %s: No NowPlayingApp found"
+ "-CMSessionMgr- %s: No active session, reset device format to LPCM"
+ "-CMSessionMgr- %s: No category set: using default (AudioVideo)"
+ "-CMSessionMgr- %s: No mode set: using default mode"
+ "-CMSessionMgr- %s: NonLongFormMediaApps array contained invalid value(s)"
+ "-CMSessionMgr- %s: NonLongFormMediaApps was not of the expected type"
+ "-CMSessionMgr- %s: Not setting device format because a client doesn't want formats to change"
+ "-CMSessionMgr- %s: Output-only session requesting sample rate lower than 22050; trying for 22050."
+ "-CMSessionMgr- %s: PVM is disabled: taking back control, and getting current PVM category again"
+ "-CMSessionMgr- %s: Playing a system sound that MUST be heard; CurrentRouteHasVolumeControl = NO"
+ "-CMSessionMgr- %s: Playing a system sound that MUST be heard; ignoring volume request"
+ "-CMSessionMgr- %s: Posting AudioBehaviorDidChange to '%@' with display ID '%@'"
+ "-CMSessionMgr- %s: PreemptiveConnectedBanner feature is disabled"
+ "-CMSessionMgr- %s: RESUMING SILENT RINGTONE!!!"
+ "-CMSessionMgr- %s: Redundant set of PID %d"
+ "-CMSessionMgr- %s: Redundant update to isActive for '%{public}@'"
+ "-CMSessionMgr- %s: Resetting waitingToResumeWhenDeviceUnlocksOrInForeground on client '%@'"
+ "-CMSessionMgr- %s: Returning Volume operation. PID = %d, Process = '%{public}s', Operation = %{public}s, volume = %1.10f inCategory = %{public}@ inRoute = %{public}@ inDeviceIdentifier = %{public}@ inRouteSubtype = %{public}@ operationCategoryCF = '%{public}@'"
+ "-CMSessionMgr- %s: Returning shouldUpdateTimestamp = %{BOOL}u"
+ "-CMSessionMgr- %s: Session %{public}@ is active for AirPlay Video over CarPlay - do not take mainAudio for iOS"
+ "-CMSessionMgr- %s: Session %{public}@ is active, routing to the device preferred by the app"
+ "-CMSessionMgr- %s: Session %{public}@ setting %{public}@ to %{BOOL}u"
+ "-CMSessionMgr- %s: Session %{public}@ setting %{public}@ to %{BOOL}u from %{BOOL}u."
+ "-CMSessionMgr- %s: Session %{public}@ with category %{public}@ always plays audio, ignoring attempt to set %{public}@."
+ "-CMSessionMgr- %s: Session '%@' %s format changes."
+ "-CMSessionMgr- %s: Session '%@' / %d"
+ "-CMSessionMgr- %s: Session '%@' is updating device format to '%@'"
+ "-CMSessionMgr- %s: Session '%@' is updating sample rate and buffer size"
+ "-CMSessionMgr- %s: Session '%@' not taking over hardware because there is a SpokenAudio app that is currently interrupted by it."
+ "-CMSessionMgr- %s: Session '%@' resetting DuckFadeDuration"
+ "-CMSessionMgr- %s: Session '%@' resetting InterruptionFadeDuration"
+ "-CMSessionMgr- %s: Session '%@' resetting UnduckFadeDuration"
+ "-CMSessionMgr- %s: Session '%@' setting AllowMixableAudioWhileRecording to %s"
+ "-CMSessionMgr- %s: Session '%@' setting DuckFadeDuration value to '%f'"
+ "-CMSessionMgr- %s: Session '%@' setting InterruptionFadeDuration value to '%f'"
+ "-CMSessionMgr- %s: Session '%@' setting ReporterIDs to '%@'"
+ "-CMSessionMgr- %s: Session '%@' setting UnduckFadeDuration value to '%f'"
+ "-CMSessionMgr- %s: Session '%@' setting WantsAutomaticClusterPairingOnPlaybackStart to %s"
+ "-CMSessionMgr- %s: Session '%@' setting cameraParameters to '%@'"
+ "-CMSessionMgr- %s: Session '%@' setting forceSoundCheck to %s"
+ "-CMSessionMgr- %s: Session '%@' setting isUsingCamera %d"
+ "-CMSessionMgr- %s: Session '%@' setting mutesAudioBasedOnRingerSwitchState value to '%d'"
+ "-CMSessionMgr- %s: Session '%@' setting override route to: '%@'"
+ "-CMSessionMgr- %s: Session '%@' taking over hardware because the currently interrupted SpokenAudio app is playing to the another audio destination."
+ "-CMSessionMgr- %s: Session '%@' will have DuckFadeDuration value clamped to the maximum allowed value."
+ "-CMSessionMgr- %s: Session '%@' will have InterruptionFadeDuration value clamped to the maximum allowed value."
+ "-CMSessionMgr- %s: Session '%@' will have UnduckFadeDuration value clamped to the maximum allowed value."
+ "-CMSessionMgr- %s: Session '%{public}@' desires an input but there isn't one, so will not attempt to control routing"
+ "-CMSessionMgr- %s: Session '%{public}@' is subscribing for the following notifications: '%{public}@'"
+ "-CMSessionMgr- %s: Session '%{public}@' isn't playing to the Default VAD, so will not attempt to control routing"
+ "-CMSessionMgr- %s: Session '%{public}@' setting doesntActuallyPlayAudio value to '%d'"
+ "-CMSessionMgr- %s: Session '%{public}@' tried to set ShortFormVideo mode on a device that does not support it"
+ "-CMSessionMgr- %s: Session category changed while active; calling BeginInterruption"
+ "-CMSessionMgr- %s: Session client '%@' resetting DuckToLevelDB"
+ "-CMSessionMgr- %s: Session client '%@' setting DuckToLevelDB value to '%f'"
+ "-CMSessionMgr- %s: Session is NULL"
+ "-CMSessionMgr- %s: Session is NULL "
+ "-CMSessionMgr- %s: Session setting Default mode from FindMyPhone mode; resetting createSpeakerDevice instead."
+ "-CMSessionMgr- %s: Session setting FindMyPhone mode; setting createSpeakerDevice instead."
+ "-CMSessionMgr- %s: Session setting active routes when interrupted to %{public}@"
+ "-CMSessionMgr- %s: SessionAudioBehaviours.plist not found"
+ "-CMSessionMgr- %s: Setting CarFigEndpointCentralObject for session '%@'"
+ "-CMSessionMgr- %s: Setting IAmIDSMXCoreSession value for session '%@' to : %d"
+ "-CMSessionMgr- %s: Setting displayID for client with PID %d to %@"
+ "-CMSessionMgr- %s: Setting doNotNotifyOtherSessionsOnNextInactive value for session '%@' to : %d"
+ "-CMSessionMgr- %s: Setting doNotResetAudioCategoryOnNextInactive value for session '%@' to : %d"
+ "-CMSessionMgr- %s: Setting downlink mute value to : %d"
+ "-CMSessionMgr- %s: Setting isCarSession value for session '%@' to : %d"
+ "-CMSessionMgr- %s: Setting isTheAssistant value for session '%@' to : %{BOOL}u"
+ "-CMSessionMgr- %s: Setting physical stream format with index %u for scope %s"
+ "-CMSessionMgr- %s: Setting policy to category: '%.4s'\n"
+ "-CMSessionMgr- %s: Setting policy to category: '%.4s', input override: '%.4s', output override: '%.4s'\n"
+ "-CMSessionMgr- %s: Setting previous uplink mute value of : %s"
+ "-CMSessionMgr- %s: Setting stark main audio owned by iOS but borrowed by car to : %d"
+ "-CMSessionMgr- %s: Setting temporaryAssertionEnabled value for session '%@' to : %d"
+ "-CMSessionMgr- %s: Setting uplink mute value to : %d"
+ "-CMSessionMgr- %s: Setting value for DoesInterAppAudio for session '%@' to : %d"
+ "-CMSessionMgr- %s: Should not skip begin interruption for %{public}@ because it is mixable, record-only, and has its own recording resources."
+ "-CMSessionMgr- %s: Skip muting client '%{public}@ since it's not eligible for PreemptivePort"
+ "-CMSessionMgr- %s: Skip posting DisallowedActivationDueToContinuityCapture notification on this platform"
+ "-CMSessionMgr- %s: Something weird just happened : The currently recording client just got suspended"
+ "-CMSessionMgr- %s: Stark was plugged in after the session went active; BeginInterruption again with flags = %d"
+ "-CMSessionMgr- %s: Starting session assertion audit timer for client %{public}@"
+ "-CMSessionMgr- %s: Stopping assertion audit timer for client %{public}@ as active state is changing"
+ "-CMSessionMgr- %s: Stopping assertion audit timer for client '%{public}@'"
+ "-CMSessionMgr- %s: This should not be happening. Please file a bug against CoreMedia Session with the steps that caused this."
+ "-CMSessionMgr- %s: Transferring EndInterruption responsibility of client '%@' to CarSession '%@'"
+ "-CMSessionMgr- %s: Transferring EndInterruption responsibility of client '%@' to active client '%@'"
+ "-CMSessionMgr- %s: Transferring EndInterruption responsibility of client '%@' to phone call or ringtone client '%@'"
+ "-CMSessionMgr- %s: Updating allowedPortTypes for session %@ to: %@"
+ "-CMSessionMgr- %s: User has disabled in-ear detection (port=%u currentOutputPort=%u), treating buds as in-ear."
+ "-CMSessionMgr- %s: Using SoloAmbientSound instead of NULL category."
+ "-CMSessionMgr- %s: Vibration stopped"
+ "-CMSessionMgr- %s: Vibrator not available on this device"
+ "-CMSessionMgr- %s: Victim %{public}@ is silent and not the Now Playing app, take its flags"
+ "-CMSessionMgr- %s: VoiceOver is %s"
+ "-CMSessionMgr- %s: VoiceOver is around while the VolumeButtonClient is active but not playing"
+ "-CMSessionMgr- %s: _CanBeginInterruption not supported, reporting that you can, since we don't know"
+ "-CMSessionMgr- %s: active victim is playing with flags %s (required %s, canKeep %s) : flagsToTake shrinking to %s"
+ "-CMSessionMgr- %s: active victim not playing or mixes with everyone: flagsToTake shrinking to %s"
+ "-CMSessionMgr- %s: allow VoiceOver session to assert volume on SystemLocal VAD"
+ "-CMSessionMgr- %s: called"
+ "-CMSessionMgr- %s: called for client '%@' [%p]"
+ "-CMSessionMgr- %s: called for client '%@' [%p] with flags %lld (2=none, 4=no side effects, 8=no hardware flags"
+ "-CMSessionMgr- %s: calling _CMSessionEndInterruption because the client forgot to"
+ "-CMSessionMgr- %s: calling cmsSetIsActive(session, false) because the client forgot to"
+ "-CMSessionMgr- %s: calling cmsSetIsPlaying(session, false) because the client forgot to"
+ "-CMSessionMgr- %s: calling to set ownership on port %u"
+ "-CMSessionMgr- %s: categories DO NOT match: op (%@~%@) != default (%@)"
+ "-CMSessionMgr- %s: category = %@ CANNOT override output to Speaker."
+ "-CMSessionMgr- %s: changing muted from %{BOOL}u to %{BOOL}u"
+ "-CMSessionMgr- %s: checking to see if we should add built-in mic"
+ "-CMSessionMgr- %s: client %@ [%p] required = %s desired = %s flagsToTake = %s"
+ "-CMSessionMgr- %s: client %@ ignoring request to set volume; current route does not have input gain control."
+ "-CMSessionMgr- %s: client %@ setting input gain volume to %@"
+ "-CMSessionMgr- %s: client %@ setting volume to %.3f"
+ "-CMSessionMgr- %s: client '%@' [%p] exited"
+ "-CMSessionMgr- %s: client '%@' mixesWithAudioVideoOnly"
+ "-CMSessionMgr- %s: client '%@': hasPhoneCallBehavior and is%s active"
+ "-CMSessionMgr- %s: client VoiceOver and victim RingtonePreview; not taking any flags; just mixing in."
+ "-CMSessionMgr- %s: clientName = '%@', key = %@, value = %@"
+ "-CMSessionMgr- %s: clients %@ and %@ are playing to same underlying physical device; let %@ keep some flags."
+ "-CMSessionMgr- %s: cmsmSetVADCategory of '%.4s'/'%.4s' failed with %d /'%.4s'\n"
+ "-CMSessionMgr- %s: could not register for audioDeviceStart notification"
+ "-CMSessionMgr- %s: couldn't allocate sessionsToInterrupt(numSessions = %ld), no interruptionCallbacks called"
+ "-CMSessionMgr- %s: couldn't start audio device because we aren't really initialized yet"
+ "-CMSessionMgr- %s: currentRouteTypes=%@"
+ "-CMSessionMgr- %s: denying attempt to mute category that we're not allowed to mute"
+ "-CMSessionMgr- %s: displayID %@ is a video app in an approved list or set the initial route sharing policy to long form video so setting routingContext to systemMusic"
+ "-CMSessionMgr- %s: displayID %@ set the initial route sharing policy to long form video."
+ "-CMSessionMgr- %s: displayID = (%@), avAudioRouteName = %@, pickedRouteUID = %@"
+ "-CMSessionMgr- %s: doesn't control routing"
+ "-CMSessionMgr- %s: doesn't control volume"
+ "-CMSessionMgr- %s: err = %d"
+ "-CMSessionMgr- %s: found a volumeButtonClient; BUT it is not active"
+ "-CMSessionMgr- %s: found a volumeButtonClient; we'll get/set current volumes, which will notify if volume changes"
+ "-CMSessionMgr- %s: getting CurrentPlayingSessionIsRoutedViaCarBT = %s"
+ "-CMSessionMgr- %s: getting IsInputOutputDecoupled = %d, outputVADID = %u, inputVADID = %u"
+ "-CMSessionMgr- %s: getting NowPlayingAppDisplayID = %@"
+ "-CMSessionMgr- %s: getting available input data sources for session %p"
+ "-CMSessionMgr- %s: getting available output data destinations for session %p"
+ "-CMSessionMgr- %s: getting current input data source for session %p"
+ "-CMSessionMgr- %s: getting current output data destination for session %p"
+ "-CMSessionMgr- %s: getting current primary app displayID"
+ "-CMSessionMgr- %s: getting deviceSupportsPiP"
+ "-CMSessionMgr- %s: getting doNotNotifyOtherSessionsOnNextInactive = %s"
+ "-CMSessionMgr- %s: getting doNotResetAudioCategoryOnNextInactive  = %s"
+ "-CMSessionMgr- %s: getting headphone volume limit: %1.3f"
+ "-CMSessionMgr- %s: getting pickableRoutes for category %@ and mode %@ result %@"
+ "-CMSessionMgr- %s: getting vibeIntensity: %1.3f"
+ "-CMSessionMgr- %s: interruptingSession: '%@' [%p] with audioCategory: '%@' **will NOT interrupt** sessionToBeInterrupted: '%@' [%p] with audioCategory: '%@'."
+ "-CMSessionMgr- %s: invariant repair of iterSession currentlyControllingFlags"
+ "-CMSessionMgr- %s: mediaserverd is in SteveNote mode"
+ "-CMSessionMgr- %s: non-CFArray pass in to _ExcludedRoutes"
+ "-CMSessionMgr- %s: okToRouteFromCustomizedRoutingPerspective = %hhu for routeUID = %{private}@"
+ "-CMSessionMgr- %s: operation = %s, value = %1.10f inCategory = %@ inRoute = %@ inDeviceIdentifier = %@ inRouteSubtype = %@"
+ "-CMSessionMgr- %s: outPostMutedNotification is NULL"
+ "-CMSessionMgr- %s: outPostVolumeNotification is NULL"
+ "-CMSessionMgr- %s: outToggleMuted is NULL"
+ "-CMSessionMgr- %s: outVolume is NULL"
+ "-CMSessionMgr- %s: partnerPortsToMakeRoutable = %@"
+ "-CMSessionMgr- %s: propertyKey = %@, propertyValue = %@"
+ "-CMSessionMgr- %s: releasing gCMSM.allowedToFadeInTemporarilyTimer for bundleID: %@"
+ "-CMSessionMgr- %s: releasing gCMSM.allowedToInitiatePlaybackTemporarilyTimer for bundleID: %@"
+ "-CMSessionMgr- %s: returning CurrentRouteHasVolumeControl = %s"
+ "-CMSessionMgr- %s: returning RecordingClientPIDs == %@"
+ "-CMSessionMgr- %s: returning SomeClientIsRecording with PID == %d"
+ "-CMSessionMgr- %s: returning route = %@, deviceIdentifier = %@"
+ "-CMSessionMgr- %s: returning someOtherClientIsPlaying == %s"
+ "-CMSessionMgr- %s: returning volume = %.3f"
+ "-CMSessionMgr- %s: route different so not doing InterruptionEnded callback"
+ "-CMSessionMgr- %s: sampleRate = %.3f"
+ "-CMSessionMgr- %s: session '%@' [%p] setting waitingToResume on session '%@' [%p], wasPlaying=%{BOOL}u, wasRecentlyActivated=%{BOOL}u"
+ "-CMSessionMgr- %s: session '%@' did NOT get StarkMainAudio, playing to %@"
+ "-CMSessionMgr- %s: session '%@' wants to exclude routes = \n%@"
+ "-CMSessionMgr- %s: session = %@ [%p] with audioCategory = %@, audioMode = %@: returning audioBehaviour = %@"
+ "-CMSessionMgr- %s: session = %@ [%p] with audioCategory = %@, audioMode = %@: returning badgeType = %@"
+ "-CMSessionMgr- %s: session = %@, hostApplicationDisplayID = %@"
+ "-CMSessionMgr- %s: session = %@, key = %@"
+ "-CMSessionMgr- %s: session wants to set input gain to %f"
+ "-CMSessionMgr- %s: session: '%@' [%p], resourceType: '%@'."
+ "-CMSessionMgr- %s: session: '%@' [%p], token: %p."
+ "-CMSessionMgr- %s: setting input data source to %d"
+ "-CMSessionMgr- %s: setting kCMSessionGlobalProperty_ThermalGainAdjustment_Haptics to: %.3f"
+ "-CMSessionMgr- %s: setting kCMSessionGlobalProperty_ThermalGainAdjustment_Speaker to: %.3f"
+ "-CMSessionMgr- %s: setting orientation override to %d"
+ "-CMSessionMgr- %s: setting output data destination to %d"
+ "-CMSessionMgr- %s: setting volume limit to %1.3f"
+ "-CMSessionMgr- %s: someClientIsPlaying = %s, isSessionGoingActiveDisruptive = %s, starkWillBeMadeRoutable = %s, isGoingToCauseRemoteInterruption = %s"
+ "-CMSessionMgr- %s: state = %d, applicationState = %d, CMSUtility_HasBackgroundEntitlement = %d"
+ "-CMSessionMgr- %s: taking back control in SetUserVolume!"
+ "-CMSessionMgr- %s: transferType = %@, session = %@ [%p], starkBorrowCount = %d"
+ "-CMSessionMgr- %s: unable to obtain current device format (err=%d['%.4s']), assuming LPCM"
+ "-CMSessionMgr- %s: unrecognized volume operation: %d"
+ "-CMSessionMgr- %s: victimized client found '%@' [%p]"
+ "-CMSessionMgr- %s: volume is NULL"
+ "-CMSessionMgr- %s: volumeClient is NULL"
+ "-CMSessionMgr- %s: wasMutedBeforeInterruption = %d"
+ "-CMSessionMgr_AirPlay- %s: Disconnecting from all airplay sessions; user initiated: %s"
+ "-CMSessionMgr_AirPlay- %s: No AirPlay endpoint found for the current output route"
+ "-CMSessionMgr_AirPlay- %s: creating gCMSM.disconnectAirPlayScreenTimer, serial queue(ACQ) = %p, timer delay = %f"
+ "-CMSessionMgr_AirPlay- %s: creating repeated gCMSM.disconnectAirPlayScreenTimer, serial queue(ACQ) = %p, timer delay = %f"
+ "-CMSessionMgr_AirPlay- %s: creating routeAwayFromAirPlayHandoffTimer, serial queue(ACQ) = %p, timer delay = %f"
+ "-CMSessionMgr_AirPlay- %s: releasing gCMSM.disconnectAirPlayScreenTimer"
+ "-CMSessionMgr_AirPlay- %s: releasing routeAwayFromAirPlayHandoffTimer"
+ "-CMSessionMgr_AirPlay- %s: screenState = %@, screenType = %@, someClientIsPlayingToAirPlay = %s, isScreenBlanked = %s,"
+ "-CMSession_CInterface-"
+ "-CMStringsDef- %s: *** %s != %s ***"
+ "-CMVAEndpoint-"
+ "-CMVAEndpoint- %s: ! hiddenSubPortsRef || ( CFGetTypeID( hiddenSubPortsRef ) != CFArrayGetTypeID() ) || ( CFArrayGetCount( hiddenSubPortsRef ) ==0 )"
+ "-CMVAEndpoint- %s: %@ does not support property for Volume Scalar Factor"
+ "-CMVAEndpoint- %s: AudioObjectGetPropertyData for %{public}s bud status failed with err = %d = %c%c%c%c"
+ "-CMVAEndpoint- %s: AudioObjectGetPropertyData( kVirtualAudioPortPropertyBluetoothAdaptiveVolumeEnabled ) for port %u failed with err = %d = %c%c%c%c"
+ "-CMVAEndpoint- %s: AudioObjectGetPropertyData( kVirtualAudioPortPropertyLiveListenSupported ) failed with err = %d = %.4s"
+ "-CMVAEndpoint- %s: AudioObjectGetPropertyData( kVirtualAudioPortPropertyModelUID ) failed with err = %d = %c%c%c%c"
+ "-CMVAEndpoint- %s: AudioObjectGetPropertyData( kVirtualAudioPortPropertyVoiceProcessingSupported ) failed with err = %d = %.4s"
+ "-CMVAEndpoint- %s: AudioObjectGetPropertyData(kVirtualAudioPortPropertySubType) failed: %d == '%.4s'"
+ "-CMVAEndpoint- %s: AudioObjectGetPropertyData(kVirtualAudioPortPropertyType) failed: %d == '%.4s'"
+ "-CMVAEndpoint- %s: AudioObjectGetPropertyData(kVirtualAudioPortPropertyUID) failed: %d == '%.4s'"
+ "-CMVAEndpoint- %s: AudioObjectSetPropertyData( kBluetoothAudioDevicePropertyAMPAudioInputEnabled ) for port %u failed with err = %d = %c%c%c%c"
+ "-CMVAEndpoint- %s: BT port %d does not support LowLatencyMode"
+ "-CMVAEndpoint- %s: Couldn't make port = %u unroutable, err = %d = %.4s"
+ "-CMVAEndpoint- %s: Either propertyKey=%@ or propertyValue=%@ is NULL"
+ "-CMVAEndpoint- %s: GetData(kVirtualAudioPortPropertyAvailableNativeSubPorts) failed with err = %d = '%.4s'"
+ "-CMVAEndpoint- %s: In-Ear detection disabled for port = %u, treating as if bud is in-ear"
+ "-CMVAEndpoint- %s: Make port [%u] routable, isWireless = %{BOOL}u"
+ "-CMVAEndpoint- %s: Physical description property doesn't exist for sub-port"
+ "-CMVAEndpoint- %s: Picked route is Built-In Microphone "
+ "-CMVAEndpoint- %s: Picking a Default port (eg: wired headset). Making all the wireless and quiesecable ports unroutable"
+ "-CMVAEndpoint- %s: Picking port with ID = %u, is user preferred = %{BOOL}u"
+ "-CMVAEndpoint- %s: Port %d being made %s for voice prompts"
+ "-CMVAEndpoint- %s: PropertyKey=%@ is not yet supported"
+ "-CMVAEndpoint- %s: QuiesceableWiredPortsConnection and SystemInputPicker features are disabled"
+ "-CMVAEndpoint- %s: Requesting ownership for A2DP port %d for reason=%{public}@ instead of HFP port %d."
+ "-CMVAEndpoint- %s: Returning port %d is %s for voice prompts"
+ "-CMVAEndpoint- %s: Set endpoint volume property was called for port=%u, which is not Bluetooth shareable / WHA groupable"
+ "-CMVAEndpoint- %s: Setting BT low latency mode on BT port %d"
+ "-CMVAEndpoint- %s: VAEndpoint %p finalized"
+ "-CMVAEndpoint- %s: Will treat built-in speaker port as groupable -- thank you for setting \"defaults write com.apple.coremedia aggregate_local_playback -bool YES\""
+ "-CMVAEndpoint- %s: [%p] called with reason %@."
+ "-CMVAEndpoint- %s: [%p] called, propertyKey '%@'"
+ "-CMVAEndpoint- %s: [%p] called."
+ "-CMVAEndpoint- %s: [%p] called. propertyKey '%@', propertyValue=%@"
+ "-CMVAEndpoint- %s: couldn't make port=%d routable, err = %d = %.4s"
+ "-CMVAEndpoint- %s: couldn't make wireless port=%d routable, err = %d = %.4s"
+ "-CMVAEndpoint- %s: override route could not be picked; no session is controlling routing"
+ "-CMVAEndpoint- %s: override route could not be unpicked; no session is controlling routing"
+ "-CMVAEndpoint- %s: port has no connection type?"
+ "-CMVAEndpoint- %s: port=%u, HasProperty supportsStereoHFP=%d"
+ "-CMVAEndpoint- %s: port=%u, alternateTransportDefault=%@"
+ "-CMVAEndpoint- %s: port=%u, in-ear status=%s"
+ "-CMVAEndpoint- %s: port=%u, listeningMode=%@"
+ "-CMVAEndpoint- %s: port=%u, spatialAudioMode=%@"
+ "-CMVAEndpoint- %s: port=%u, supportedListeningModes=%u (bitmask where 0: unsupported, 1: ANC, 2: transparency"
+ "-CMVAEndpoint- %s: port=%u, supportsBluetoothHighQualityContentCapture=%{BOOL}u"
+ "-CMVAEndpoint- %s: port=%u, supportsHighQualityBiDirectionalAudio=%s"
+ "-CMVAEndpoint- %s: port=%u, supportsStereoHFP=%d"
+ "-CMVAEndpoint- %s: portID=%u isQuiesceableWiredPort=%u"
+ "-CMVAEndpoint- %s: propertyValue for propertyKey mainVolume is not of type CFNumber"
+ "-CMVAEndpoint- %s: returning %@"
+ "-CMVAEndpoint- %s: returning %@, portType was '%.4s'"
+ "-CMVAEndpoint- %s: returning %{BOOL}u for port %u"
+ "-CMVAEndpoint- %s: routeDescription = %@"
+ "-CMVAEndpoint- %s: setting port = %d isRoutable = %d"
+ "-CMVAEndpoint- %s: vaeMakePortRoutable, making fallback port routable"
+ "-CMVAEndpoint- %s: vaeRouteToSelectedPort port=%u"
+ "-CMVAEndpoint- %s: wired route seen in picker code? (port = %d, routeUID = %@, routeName = %@, avAudioRouteName = %@)"
+ "-CMVAEndptMgr-"
+ "-CMVAEndptMgr- %s: "
+ "-CMVAEndptMgr- %s:  connectedPorts is NULL"
+ "-CMVAEndptMgr- %s: ! activePorts || ( CFGetTypeID( activePorts ) != CFArrayGetTypeID() )"
+ "-CMVAEndptMgr- %s: ! connectedPortsRef || ( CFGetTypeID( routeArray ) != CFArrayGetTypeID() )"
+ "-CMVAEndptMgr- %s: !quiesceableWiredPortsRef || ( CFGetTypeID( quiesceableWiredPortsRef ) != CFArrayGetTypeID() )"
+ "-CMVAEndptMgr- %s: %s VAD %@: range[%d] = max: %.3f min: %.3f ; numChannels: %d; formatID: '%.4s'"
+ "-CMVAEndptMgr- %s: %{public}@ = %{BOOL}u"
+ "-CMVAEndptMgr- %s: Adding: portID = %d, endpoint = %p"
+ "-CMVAEndptMgr- %s: Assigning airplayHandoffOutputPort to %ld"
+ "-CMVAEndptMgr- %s: Atmos as MAT is disabled"
+ "-CMVAEndptMgr- %s: Atmos as MAT is enabled"
+ "-CMVAEndptMgr- %s: Attempting to copy fallback input device for session %d"
+ "-CMVAEndptMgr- %s: Audio hardware already set to AC-3"
+ "-CMVAEndptMgr- %s: Audio hardware already set to MAT Atmos"
+ "-CMVAEndptMgr- %s: AudioObjectAddPropertyListener( kAudioHardwarePropertyDevices ) failed with err = %d"
+ "-CMVAEndptMgr- %s: AudioObjectAddPropertyListener(cmsmAvailableVirtualFormatsListener) failed err = %d = '%.4s'"
+ "-CMVAEndptMgr- %s: AudioObjectAddPropertyListener(cmsmInputSourcesListener) failed err = %d = '%.4s'"
+ "-CMVAEndptMgr- %s: AudioObjectAddPropertyListener(cmsmOutputDestinationsListener) failed err = %d = '%.4s'"
+ "-CMVAEndptMgr- %s: AudioObjectAddPropertyListener(cmsmVADDeviceVolumeChangeListener) failed err = %d = '%.4s'"
+ "-CMVAEndptMgr- %s: AudioObjectAddPropertyListener(vaemCurrentRouteHasVolumeControlListener) failed err = %d = '%.4s'"
+ "-CMVAEndptMgr- %s: AudioObjectAddPropertyListener(vaemVADAvailableSampleRatesListener) failed err = %d = '%.4s'"
+ "-CMVAEndptMgr- %s: AudioObjectAddPropertyListener(vaemVADCurrentBufferFrameSizeListener) failed err = %d = '%.4s'"
+ "-CMVAEndptMgr- %s: AudioObjectAddPropertyListener(vaemVADCurrentSampleRateListener) failed err = %d = '%.4s'"
+ "-CMVAEndptMgr- %s: AudioObjectGetPropertyData( kVirtualAudioDevicePropertyDataDestinations ) failed with err = %d = %.4s"
+ "-CMVAEndptMgr- %s: AudioObjectGetPropertyData( kVirtualAudioDevicePropertyDataSource ) failed with err = %d = %.4s"
+ "-CMVAEndptMgr- %s: AudioObjectGetPropertyData( kVirtualAudioDevicePropertyDataSources ) failed with err = %d = %.4s"
+ "-CMVAEndptMgr- %s: AudioObjectGetPropertyData(kAudioDevicePropertyBufferFrameSizeRange) failed with err = %d = %.4s"
+ "-CMVAEndptMgr- %s: AudioObjectGetPropertyData(kAudioDevicePropertyDefaultChannelLayout) failed with err = %d = %.4s"
+ "-CMVAEndptMgr- %s: AudioObjectGetPropertyData(kAudioDevicePropertyNominalSampleRate) failed with err = %d = %.4s"
+ "-CMVAEndptMgr- %s: AudioObjectGetPropertyData(kAudioDevicePropertyQuietBufferFrameSize) failed with err = %d = %.4s for %@"
+ "-CMVAEndptMgr- %s: AudioObjectGetPropertyData(kAudioDevicePropertyStreams) failed with err = %d = %.4s"
+ "-CMVAEndptMgr- %s: AudioObjectGetPropertyData(kAudioStreamPropertyVirtualFormat) failed with err = %d = %.4s"
+ "-CMVAEndptMgr- %s: AudioObjectGetPropertyData(kVirtualAudioDevicePropertyAtmosSupport) failed with err = %d = %.4s"
+ "-CMVAEndptMgr- %s: AudioObjectGetPropertyData(kVirtualAudioDevicePropertyBufferFrameSizeIsRestricted) failed with err = %d = %.4s"
+ "-CMVAEndptMgr- %s: AudioObjectGetPropertyData(kVirtualAudioDevicePropertyPolicyMute) failed: %d == '%.4s'"
+ "-CMVAEndptMgr- %s: AudioObjectGetPropertyData(kVirtualAudioDevicePropertyThermalBudget) failed with err = %d = %.4s"
+ "-CMVAEndptMgr- %s: AudioObjectGetPropertyData(kVirtualAudioDevicePropertyUIOrientationParam) failed with err = %d = %.4s"
+ "-CMVAEndptMgr- %s: AudioObjectGetPropertyData(kVirtualAudioPlugInPropertyCategoryExt) failed: %d == '%.4s'"
+ "-CMVAEndptMgr- %s: AudioObjectGetPropertyData(kVirtualAudioPlugInPropertyMode) failed: %d == '%.4s'"
+ "-CMVAEndptMgr- %s: AudioObjectGetPropertyData(kVirtualAudioPlugInPropertyQuiesceableWiredPorts) failed with err = %d = '%.4s'"
+ "-CMVAEndptMgr- %s: AudioObjectGetPropertyData(kVirtualAudioStreamPropertyAssociatedPorts) failed with err = %d = %.4s"
+ "-CMVAEndptMgr- %s: AudioObjectGetPropertyDataSize(kAudioDevicePropertyDefaultChannelLayout) failed with err = %d = %.4s"
+ "-CMVAEndptMgr- %s: AudioObjectGetPropertyDataSize(kAudioDevicePropertyStreams) failed with err = %d = %.4s"
+ "-CMVAEndptMgr- %s: AudioObjectRemovePropertyListener(cmsmVADAvailableSampleRatesListener) failed err = %d = '%.4s'"
+ "-CMVAEndptMgr- %s: AudioObjectRemovePropertyListener(kAudioHardwarePropertyDevices) failed with err = %d = '%.4s'"
+ "-CMVAEndptMgr- %s: AudioObjectSetPropertyData(kAudioStreamPropertyVirtualFormat) failed with err = %d = %.4s"
+ "-CMVAEndptMgr- %s: AudioObjectSetPropertyData(kVirtualAudioDevicePropertyCaptureOrientationOverride) failed with err = %d = %.4s"
+ "-CMVAEndptMgr- %s: AudioObjectSetPropertyData(kVirtualAudioDevicePropertyOrientationOverride) failed with err = %d = %.4s"
+ "-CMVAEndptMgr- %s: AudioObjectSetPropertyData(kVirtualAudioDevicePropertyUIOrientationParam) failed with err = %d = %.4s"
+ "-CMVAEndptMgr- %s: AudioToolboxServerAccessTelephonyMutes failed: %d == '%.4s'"
+ "-CMVAEndptMgr- %s: Available Virtual Formats listener fired"
+ "-CMVAEndptMgr- %s: CMSMVAUtility_AudioObjectSetPropertyData( kVirtualAudioDevicePropertyDataDestination ) failed with err = %d = %.4s"
+ "-CMVAEndptMgr- %s: CMSMVAUtility_AudioObjectSetPropertyData( kVirtualAudioDevicePropertyDataSource ) failed with err = %d = %.4s"
+ "-CMVAEndptMgr- %s: CMSMVAUtility_AudioObjectSetPropertyData(fig_kVirtualAudioDevicePropertyLatencyOverride) failed with err = %d = %.4s"
+ "-CMVAEndptMgr- %s: Called for %@, inputStream %d, outputStream %d"
+ "-CMVAEndptMgr- %s: Calling PVMRemoveVolumesForDeviceRoute(%@, NULL, NULL)"
+ "-CMVAEndptMgr- %s: Calling enhanced AQME route changed routine: %@"
+ "-CMVAEndptMgr- %s: Calling pAQMERouteChanged"
+ "-CMVAEndptMgr- %s: CarPlay Headunit published both ports (USB audio ( port %u ) & Stark ( port %u ) ) for main audio."
+ "-CMVAEndptMgr- %s: Channel number %d has channel label: %d"
+ "-CMVAEndptMgr- %s: Checking out stream with sample rate range [%f,%f] and channels [%d]. Requested sample rate [%f] and channels [%d]"
+ "-CMVAEndptMgr- %s: Client (quite likely CMSession) trying to set volume on MusicVAD. We skip this because MusicVAD/AggregateEndpoint volume should only be set by FigVolumeController."
+ "-CMVAEndptMgr- %s: Connected ports: %{public}@, category = %{public}@, mode = %{public}@, count = %lu"
+ "-CMVAEndptMgr- %s: ConnectedInputPorts for session %{public}@: %{public}@"
+ "-CMVAEndptMgr- %s: Couldn't set device volume, err = %d = '%.4s'"
+ "-CMVAEndptMgr- %s: Current input data source : %d"
+ "-CMVAEndptMgr- %s: Current output data destination : %d"
+ "-CMVAEndptMgr- %s: Device %s encode AC3"
+ "-CMVAEndptMgr- %s: Device %s support AC3"
+ "-CMVAEndptMgr- %s: Empty connected input ports for %{public}@"
+ "-CMVAEndptMgr- %s: Endpoint for port = %d not found."
+ "-CMVAEndptMgr- %s: Error getting Stream0 or no stream present"
+ "-CMVAEndptMgr- %s: Error getting stream ID"
+ "-CMVAEndptMgr- %s: Error sending userPreferredInput route while session is active, err = %d"
+ "-CMVAEndptMgr- %s: Error setting kVirtualAudioPlugInPropertyCreateVAD!"
+ "-CMVAEndptMgr- %s: Error setting kVirtualAudioPlugInPropertyDeleteVAD!"
+ "-CMVAEndptMgr- %s: Error setting kVirtualAudioPlugInPropertyRouteConfiguration!"
+ "-CMVAEndptMgr- %s: Forwarding routeConfiguration to VA because of: %{public}@ changed from %{BOOL}u to %{BOOL}u"
+ "-CMVAEndptMgr- %s: Found last-in routable port %{public}@ for session %{public}@"
+ "-CMVAEndptMgr- %s: GetData(kVirtualAudioDevicePropertyVolumeControlSupported) failed with err = %d = '%.4s'"
+ "-CMVAEndptMgr- %s: GetData(kVirtualAudioPlugInPropertyActivePortsForRouteConfiguration) failed with err = %d = '%.4s'"
+ "-CMVAEndptMgr- %s: GetData(kVirtualAudioPlugInPropertyCategoryInfo) failed with err = %d = '%.4s'"
+ "-CMVAEndptMgr- %s: GetData(kVirtualAudioPlugInPropertyConnectedPortsForRouteConfiguration) failed with err = %d = '%.4s'"
+ "-CMVAEndptMgr- %s: GetData(kVirtualAudioPlugInPropertyConnectedPortsWithDeviceForRouteConfiguration) failed with err = %d = '%.4s'"
+ "-CMVAEndptMgr- %s: GetData(kVirtualAudioPlugInPropertyRouteConfigurationSupportsPortType) failed with err = %d = '%.4s'"
+ "-CMVAEndptMgr- %s: GetData(kVirtualAudioPlugInPropertySupportedCategories) failed with err = %d = '%.4s'"
+ "-CMVAEndptMgr- %s: GetPropertyDataSize(kVirtualAudioPlugInPropertySupportedCategories) failed with err = %d = '%.4s'"
+ "-CMVAEndptMgr- %s: Headphones %s input"
+ "-CMVAEndptMgr- %s: Headphones are %s"
+ "-CMVAEndptMgr- %s: INPUT: range[%d] = max: %.3f min: %.3f; numChannels: %d; formatID: '%.4s'"
+ "-CMVAEndptMgr- %s: Input ports are empty for default VAD. Getting input ports from Decoupled input VAD"
+ "-CMVAEndptMgr- %s: Make quiesceable wired port [%u] routable"
+ "-CMVAEndptMgr- %s: Mediaserver main() has not initialized AQMERestartIOFollowingRouteChange. Expect bad things, you must."
+ "-CMVAEndptMgr- %s: Mediaserver main() has not initialized AQMERouteChanged. Expect bad things, you must."
+ "-CMVAEndptMgr- %s: NOT a starkPort"
+ "-CMVAEndptMgr- %s: Newly connected input port: Name='%{public}@' UID='%{public}@' PortType='%{public}.4s' Port='%lu' Quiesceable = '%{BOOL}u' ConnectionType=%{public}.4s"
+ "-CMVAEndptMgr- %s: Nil connected input ports for %{public}@"
+ "-CMVAEndptMgr- %s: No %s streams found; moving on."
+ "-CMVAEndptMgr- %s: No connected input ports"
+ "-CMVAEndptMgr- %s: No connected ports"
+ "-CMVAEndptMgr- %s: No session to copy configuration for, returning nil."
+ "-CMVAEndptMgr- %s: No streams found"
+ "-CMVAEndptMgr- %s: Not doing anything from in-ear status change because the BT port is out-of-ear"
+ "-CMVAEndptMgr- %s: Not setting device format because a client doesn't want formats to change"
+ "-CMVAEndptMgr- %s: Number of %s stream formats: %d"
+ "-CMVAEndptMgr- %s: Number of channel descriptions : %d"
+ "-CMVAEndptMgr- %s: Number of channels for stream %u: %u"
+ "-CMVAEndptMgr- %s: Old stream 0 ID : %d; new stream 0 ID: %d"
+ "-CMVAEndptMgr- %s: Please update your build so we can report the right latency"
+ "-CMVAEndptMgr- %s: Ports for stream %u returning NULL or invalid value."
+ "-CMVAEndptMgr- %s: Processing session routing info change for %{public}@"
+ "-CMVAEndptMgr- %s: Redundant route configuration; skipping."
+ "-CMVAEndptMgr- %s: Removing portID = %d"
+ "-CMVAEndptMgr- %s: Requesting input routes for following category/mode %@ / %@"
+ "-CMVAEndptMgr- %s: Restarting the mix engine ... "
+ "-CMVAEndptMgr- %s: Returning NULL for input route query."
+ "-CMVAEndptMgr- %s: Returning dB = %.3f on virtualAudioDevice %d"
+ "-CMVAEndptMgr- %s: Returning maximumNumberOf%sChannels : %d"
+ "-CMVAEndptMgr- %s: Route changing to receiver; sending ROUTE_WILL_CHANGE_TO_RECEIVER notification."
+ "-CMVAEndptMgr- %s: Session %{public}@ is active, sending the user preferred input to VA"
+ "-CMVAEndptMgr- %s: Session is active, clearing the input device preferred"
+ "-CMVAEndptMgr- %s: Set boot chime volume on speaker port %ld to %f"
+ "-CMVAEndptMgr- %s: Set external ducking on VA to %s"
+ "-CMVAEndptMgr- %s: Setting buffer duration to %.3f for VAD %{public}@"
+ "-CMVAEndptMgr- %s: Setting call screening status to %@"
+ "-CMVAEndptMgr- %s: Setting downlink mute value on AudioToolboxServer to = %d"
+ "-CMVAEndptMgr- %s: Setting full mute value = %d"
+ "-CMVAEndptMgr- %s: Setting orientation override to %d"
+ "-CMVAEndptMgr- %s: Setting routableAsFallback to true"
+ "-CMVAEndptMgr- %s: Setting thermal budget on %@ to %@"
+ "-CMVAEndptMgr- %s: Setting thermal control info on %@ to %@"
+ "-CMVAEndptMgr- %s: Setting thermal gain adjustment for %s to %.4f"
+ "-CMVAEndptMgr- %s: Setting uplink mute value = %d"
+ "-CMVAEndptMgr- %s: Skipping stream with sample rate range [%f,%f] as it does not match the requested format. Stream format = '%.4s'; requested format = '%.4s'"
+ "-CMVAEndptMgr- %s: Stream 0 ID has changed; re-registering stream listeners"
+ "-CMVAEndptMgr- %s: Stream ID %d and stream format %d has %d channel(s)"
+ "-CMVAEndptMgr- %s: Stream formats structure NULL"
+ "-CMVAEndptMgr- %s: Stream no. %ld :: %u"
+ "-CMVAEndptMgr- %s: System %s input device"
+ "-CMVAEndptMgr- %s: System supports PlayAndRecord : %s"
+ "-CMVAEndptMgr- %s: Trying again to request for input routes for the following session = %u as this session controls routing."
+ "-CMVAEndptMgr- %s: Trying to clear the automatic ownership timer."
+ "-CMVAEndptMgr- %s: Unable to set thermal gain adjustment"
+ "-CMVAEndptMgr- %s: Unmuting full mute if muted"
+ "-CMVAEndptMgr- %s: Unrecognized CPMSClientId: %d"
+ "-CMVAEndptMgr- %s: Unsupported discoveryMode = %@"
+ "-CMVAEndptMgr- %s: Unsupported property = %@"
+ "-CMVAEndptMgr- %s: Unsupported property: %@"
+ "-CMVAEndptMgr- %s: Using input gain scalar value of %.4f from saved volumes"
+ "-CMVAEndptMgr- %s: Using input gain scalar value of %.4f from session '%@'"
+ "-CMVAEndptMgr- %s: VA initialization ended - Elapsed time=%llu milliseconds"
+ "-CMVAEndptMgr- %s: VAD returned size : %u, %lu streams."
+ "-CMVAEndptMgr- %s: VAEndpointManager %p finalized"
+ "-CMVAEndptMgr- %s: VAEndpointManager %p invalidated"
+ "-CMVAEndptMgr- %s: Will be requesting for input routes for the following session = %u"
+ "-CMVAEndptMgr- %s: [%p] called. storage->invalid %s, propertyKey '%@'"
+ "-CMVAEndptMgr- %s: audioInput routes = %@"
+ "-CMVAEndptMgr- %s: calling vaemAvailableVirtualFormatsPropertyListenerGuts_f"
+ "-CMVAEndptMgr- %s: calling vaemCurrentRouteHasInputGainControlListenerGuts"
+ "-CMVAEndptMgr- %s: calling vaemCurrentRouteHasVolumeControlListenerGuts"
+ "-CMVAEndptMgr- %s: calling vaemInputSourcesListenerGuts"
+ "-CMVAEndptMgr- %s: category (%.4s) != gCMSM.currentVADCategory (%.4s)"
+ "-CMVAEndptMgr- %s: category = '%{public}.4s'  mostRecentVADCategory = '%{public}.4s' mode = '%{public}.4s' mostRecentVADMode = '%{public}.4s' \n \t\t\t\t\t\t\t\t\t\t\tactivationContext: %{public}@ \n \t\t\t\t\t\t\t\t\t\t\toverridePortsList: %{public}@ mostRecentOverridePortsList: %{public}@ \n \t\t\t\t\t\t\t\t\t\t\troutablePorts:%{public}@ unroutablePorts:%{public}@ \t\t\t\t\t\n  \t\t\t\t\t\t\t\t\t\t\tportsToAggregate:%{public}@ portsToDeaggregate:%{public}@\t\t\t\t\n \t\t\t\t\t\t\t\t\t\t\tsubPortPreferences: %{public}@ mostRecentsubPortPreferences : %{public}@ \n \t\t\t\t\t\t\t\t\t\t\tsetScreenDarkMode = %{public}s \n \t\t\t\t\t\t\t\t\t\t\tcreateSpeakerDevice = %{public}s \n \t\t\t\t\t\t\t\t\t\t\texcludedPortsList : %{public}@ \n \t\t\t\t\t\t\t\t\t\t\tignoreRingerSwitch = %{public}s \n \t\t\t\t\t\t\t\t\t\t\tdecoupledInputOutput = %{public}s \n \t\t\t\t\t\t\t\t\t\t\tallowedPortTypes = %{public}@ \n\t\t\t\t\t\t\t\t\t\t\treporterIDs = %{public}@ \n\t\t\t\t\t\t\t\t\t\t\tcameraParameters = %{public}@\n \t\t\t\t\t\t\t\t\t\t\tupdatePVMOnRedundantRouteConfiguration = %{public}s\n \t\t\t\t\t\t\t\t\t\t\tpersistentRoute = %{public}@ mostRecentPersistentRoute: %{public}@\n                                             userPreferredInputPort = %{public}@ \n"
+ "-CMVAEndptMgr- %s: client set buffer duration explicitly == %.3f"
+ "-CMVAEndptMgr- %s: connectedOutputPorts[%ld] = %{public}@"
+ "-CMVAEndptMgr- %s: connectedPorts is NULL"
+ "-CMVAEndptMgr- %s: connectedPorts is not a CFArray!"
+ "-CMVAEndptMgr- %s: currentPort endpointid = %{public}@"
+ "-CMVAEndptMgr- %s: currentPort[%ld] = %{private}@"
+ "-CMVAEndptMgr- %s: currentRouteIdentifiers[%d] = %{public}@"
+ "-CMVAEndptMgr- %s: currentRoutes = %@, airPlayShouldIgnoreRouteChanges = %s"
+ "-CMVAEndptMgr- %s: default VAD: range[%d] = max: %.3f min: %.3f ; numChannels: %d; formatID: '%.4s'"
+ "-CMVAEndptMgr- %s: defaultVADID = %d speechDetectionVADID = %d systemSoundLocalVADID = %d systemSoundRemoteVADID = %d decoupledInputVAD = %d siriOutputVADID = %d actuatorVADID = %d lowLatencyVADID = %d"
+ "-CMVAEndptMgr- %s: deviceRoute or category did NOT change, don't enable PVM (it was %s enabled)"
+ "-CMVAEndptMgr- %s: deviceType = '%.4s'"
+ "-CMVAEndptMgr- %s: discoveryMode %@"
+ "-CMVAEndptMgr- %s: duration = %.3f, sampleRate = %.3f, numPCMSamples = %u, NearestPowerOf2 = %u, UseQuietBufferSizeProperty = '%{public}@', VAD = %{public}@"
+ "-CMVAEndptMgr- %s: enabling PVM, so deviceRoute change is noticed"
+ "-CMVAEndptMgr- %s: failed with err = %d = '%.4s'"
+ "-CMVAEndptMgr- %s: gCMSM.currentRouteHasInputGainControl = %s, currentRouteNowHasVolumeControl = %s"
+ "-CMVAEndptMgr- %s: index = %d, oldOutputPort = %u, isRouteHeadphonesWithInEarDetectionSupported = %{BOOL}u}"
+ "-CMVAEndptMgr- %s: input gain scalar = %.3f"
+ "-CMVAEndptMgr- %s: inputPort[%u] = %u, outputPort[%u] = %u, endpointType[%u] = %@\n"
+ "-CMVAEndptMgr- %s: isNewRouteHeadphonesAndInEarStatus = %{BOOL}u, didOldRouteSupportInEarDetection = %{BOOL}u"
+ "-CMVAEndptMgr- %s: newWiredPorts count = %lu"
+ "-CMVAEndptMgr- %s: newWirelessPorts count = %lu"
+ "-CMVAEndptMgr- %s: no streams, so couldn't set device format"
+ "-CMVAEndptMgr- %s: no streams, so no device format"
+ "-CMVAEndptMgr- %s: numConnectedPorts for category = '%.4s' mode = '%.4s' allowedPortTypes = %{public}@ is %d"
+ "-CMVAEndptMgr- %s: numPCMFrames = %d"
+ "-CMVAEndptMgr- %s: numPorts = %ld, ports = %@"
+ "-CMVAEndptMgr- %s: outputPort[%u] = %u, endpointType[%u] = %@\n"
+ "-CMVAEndptMgr- %s: portID = 0"
+ "-CMVAEndptMgr- %s: portType = '%.4s', returning port == %d"
+ "-CMVAEndptMgr- %s: portstoadd count = %lu"
+ "-CMVAEndptMgr- %s: portstoadd[%d]  = %{public}@, name = %{public}@"
+ "-CMVAEndptMgr- %s: removing port %@"
+ "-CMVAEndptMgr- %s: returning Atmos Available = %d"
+ "-CMVAEndptMgr- %s: returning FullMute status == %d"
+ "-CMVAEndptMgr- %s: returning bufferFrameSizeShouldBeRestricted = %d"
+ "-CMVAEndptMgr- %s: returning downlink mute status == %d"
+ "-CMVAEndptMgr- %s: returning for VADID %@ Sample rate = %f"
+ "-CMVAEndptMgr- %s: returning for scope %s, VADID %@ channels = %u"
+ "-CMVAEndptMgr- %s: returning minNumPCMFrames = %d, maxNumPCMFrames = %d"
+ "-CMVAEndptMgr- %s: returning mode == %.4s"
+ "-CMVAEndptMgr- %s: returning numPCMFrames = %d"
+ "-CMVAEndptMgr- %s: returning thermalBudget = %@"
+ "-CMVAEndptMgr- %s: returning thermalBudgetRange for %@ = %@"
+ "-CMVAEndptMgr- %s: returning thermalControlInfo = %@"
+ "-CMVAEndptMgr- %s: returning uplink mute status == %d"
+ "-CMVAEndptMgr- %s: returning, key = %@, value = %@"
+ "-CMVAEndptMgr- %s: route change due to unplug: clear all overrides and pending picks"
+ "-CMVAEndptMgr- %s: set default input volume"
+ "-CMVAEndptMgr- %s: set ownership on vPort=%u"
+ "-CMVAEndptMgr- %s: setting default input gain for the session"
+ "-CMVAEndptMgr- %s: setting volume on hardware = %.3f"
+ "-CMVAEndptMgr- %s: setting volume on siri output VAD = %.3f"
+ "-CMVAEndptMgr- %s: setting volume on system sound VAD = %.3f"
+ "-CMVAEndptMgr- %s: starkPort = %u"
+ "-CMVAEndptMgr- %s: streamFormatIndexForBestChannelCount = %d"
+ "-CMVAEndptMgr- %s: streamFormatIndexForChannelCountAndExactSampleRate: %d"
+ "-CMVAEndptMgr- %s: streamFormatIndexForChannelCountAndHigherSampleRate: %d"
+ "-CMVAEndptMgr- %s: streamFormatIndexForChannelCountAndLowerSampleRate: %d"
+ "-CMVAEndptMgr- %s: system remote: range[%d] = max: %.3f min: %.3f ; numChannels: %d; formatID: '%.4s'"
+ "-CMVAEndptMgr- %s: uninteresting <broadcast to different broadcast> route change ignored"
+ "-CMVAEndptMgr- %s: userPreferredInputPort = %{public}@"
+ "-CMVAEndptMgr- %s: using cached volume = %.3f"
+ "-CMVAEndptMgr- %s: using cached volume for system sound VAD = %.3f"
+ "-CMVAEndptMgr- %s: vadReason = '%.4s'"
+ "-CMVAEndptMgr- %s: vaemVADAvailableSampleRatesListener is triggered"
+ "-CMVAEndptMgr- %s: vaemVADInputSampleRateListener is triggered"
+ "-CMVAEndptMgr- %s: vaemVADSampleRateListener is triggered"
+ "-CMVAEndptMgr- %s: volume from VAD (%@) = %f"
+ "-CMVAEndptMgr- %s: volume from VAD (%@~%@) = %f"
+ "-CMVAEndptMgr- %s: whacking VAD to Audio/Video"
+ "-CMVAEndptMgr- %s: wireless splitter session is enabled - do nothing"
+ "-CMVAEndptUtl- %s: Couldn't make port %@ (%u) routable, err = %d = %.4s"
+ "-CMVAEndptUtl- %s: Error getting kVirtualAudioPlugInPropertyOnDemandRouteSupported for session description %{public}@: %d"
+ "-CMVAEndptUtl- %s: Error setting kVirtualAudioPlugInPropertyOverrideToPartnerPort!"
+ "-CMVAEndptUtl- %s: Found connected audio port = %@ (%ld )"
+ "-CMVAEndptUtl- %s: Invalid mode passed in: %@; returning default."
+ "-CMVAEndptUtl- %s: Making port = %u routable"
+ "-CMVAEndptUtl- %s: Mediaserver main() has not initialized pAQMESetAudioObjectPropertyData. Expect bad things, you must."
+ "-CMVAEndptUtl- %s: Not really. A2DP not to be auto-jacked in if LineOut/USB/HDMI/DisplayPort/Thunderbolt/Stark/ContinuityScreenOutput is around."
+ "-CMVAEndptUtl- %s: Port %@ (%u) is made routable."
+ "-CMVAEndptUtl- %s: Port %u is BTManaged but not in-ear, filtering out"
+ "-CMVAEndptUtl- %s: Port %u is out-of-ear, skip asking about the audio routing action"
+ "-CMVAEndptUtl- %s: Sending session going active info to VA: %{public}@ to query on-demand route capability."
+ "-CMVAEndptUtl- %s: Setting sessionInfo on VA plugin ID %d: %@"
+ "-CMVAEndptUtl- %s: Will session with info %{public}@ route to on-demand VAD? %u"
+ "-CMVAEndptUtl- %s: connectedAudioPorts is NULL"
+ "-CMVAEndptUtl- %s: creating PerAppAirPlay VAD with handoff port: %d"
+ "-CMVAEndptUtl- %s: creating PerAppAirPlay VAD with port: %d"
+ "-CMVAEndptUtl- %s: destroying perAppAirPlay because we're no longer in the perAppAirPlay routing configuration"
+ "-CMVAEndptUtl- %s: destroying perAppAirPlayVAD before creating it again ( without processing the route change) "
+ "-CMVAEndptUtl- %s: destroying perAppAirPlayVAD without processing the route change"
+ "-CMVAEndptUtl- %s: in:'%.4s' + out:'%.4s' == %@"
+ "-CMVAEndptUtl- %s: isPortTypeBT = %{BOOL}u, isPortTypeVehicle = %{BOOL}u, isPortTypeBluetoothVehicle = %{BOOL}u for port = %u,"
+ "-CMVAEndptUtl- %s: mapped %@ to '%.4s'"
+ "-CMVAEndptUtl- %s: mapped '%.4s' to %@ "
+ "-CMVAEndptUtl- %s: new route has no input or output ports"
+ "-CMVAEndptUtl- %s: number of wireless ports = 0. Nothing to do."
+ "-CMVAEndptUtl- %s: returning %@, portTypes were in:'%.4s' out:'%.4s'"
+ "-CMVAEndptUtl- %s: routeUID = %@"
+ "-CMVAEndptUtl- %s: shouldAutoRoute=%d for %@"
+ "-CMVAEndptUtl- %s: starkPort=%d, starkPortWasMadeRoutable=%s, gCMSM.doNotMakeStarkPortRoutable=%s, sessionToPlayOverStark=%@"
+ "-FigEndpointDescriptorUtility- %s: endpoint or descriptor is NULL"
+ "-FigEndpointDescriptorUtility- %s: setting %{public}@ to %{BOOL}u"
+ "-FigEndpointUIAgent-"
+ "-FigEndpointUIAgent- %s: Copy password %p for %@"
+ "-FigEndpointUIAgent- %s: Invalidate called %p"
+ "-FigEndpointUIAgent- %s: Set auth value for %p, prompt dismissed %d"
+ "-FigEndpointUIAgent- %s: Set password from keychain value for %p, "
+ "-FigEndpointUIAgentHelper- %s: AirPlayUIAgent callback %@"
+ "-FigEndpointUIAgentHelper- %s: Clean up prompt for %@ %s password"
+ "-FigEndpointUIAgentHelper- %s: EndpointUIAgent (%p) notification received %@"
+ "-FigEndpointUIAgentHelper- %s: Prompt dismissed "
+ "-FigEndpointUIAgentHelper- %s: Saving password %@ "
+ "-FigEndpointUIAgentXPCRemote-"
+ "-FigEndpointUIAgentXPCRemote- %s:  EndpointUIAgent Remote Client created %d"
+ "-FigEndpointUIAgentXPCRemote- %s:  EndpointUIAgent created %p"
+ "-FigEndpointUIAgentXPCRemote- %s:  EndpointUIAgent device awake call %p"
+ "-FigEndpointUIAgentXPCRemote- %s:  EndpointUIAgent setting current ui agent %p (%d)"
+ "-FigEndpointUIAgentXPCRemote- %s: (%p)"
+ "-FigEndpointUIAgentXPCServer-"
+ "-FigEndpointUIAgentXPCServer- %s: Completed opCode '%c%c%c%c' err = %d"
+ "-FigEndpointUIAgentXPCServer- %s: Endpoint agent %p not found"
+ "-FigEndpointUIAgentXPCServer- %s: FigEndpointUIAgent Server Started"
+ "-FigEndpointUIAgentXPCServer- %s: Number of Endpoint Agents %ld"
+ "-FigEndpointUIAgentXPCServer- %s: Posting %@ on Agent %p"
+ "-FigEndpointUIAgentXPCServer- %s: Posting %@ on CURRENT Agent %p"
+ "-FigEndpointUIAgentXPCServer- %s: Posting %@ on agent %p"
+ "-FigEndpointUIAgentXPCServer- %s: Posting %@ on current Agent %p"
+ "-FigEndpointUIAgentXPCServer- %s: Remove endpoint agent %p "
+ "-FigEndpointUIAgentXPCServer- %s: Server not created! "
+ "-FigEndpointUIAgentXPCServer- %s: Set AuthInfo %p "
+ "-FigEndpointUIAgentXPCServer- %s: Set password from keychain %p "
+ "-FigEndpointUIAgentXPCServer- %s: Starting opCode '%c%c%c%c'"
+ "-FigEndpointUIAgentXPCServer- %s: Unknown opCode: 0x%0x"
+ "-FigEndpointUIAgentXPCServer- %s: Updating to current agent %p"
+ "-FigEndpointUIAgentXPCServer- %s: Updating to current agent %p to %{public}@"
+ "-FigPredictedRouting- %s: AirPlay suggestions, preemptive port logic is disabled"
+ "-FigPredictedRouting- %s: Called due to reason=%{public}@, isBTManagedPortPresent=%{BOOL}u, isBTManagedPortInEar=%{BOOL}u, routeIsBuiltIn=%{BOOL}u, predictedRouteConditionChanged=%{BOOL}u, cachedSessionIsPlaying=%{BOOL}u, predictedRouteChanged=%{BOOL}u, sSystemMusicIsIndependent=%{BOOL}u, predictedRouteChangedForSystemMusic=%{BOOL}u, predictedRouteName=%{public}@, predictedRouteUID=%{private}@, predictedModelID=%{public}@"
+ "-FigPredictedRouting- %s: PreemptivePortChanged timer has stopped"
+ "-FigPredictedRouting- %s: PreemptivePortChanged=NO, skip muting audio"
+ "-FigPredictedRouting- %s: Smart Routing, preemptive port logic is disabled"
+ "-FigRouteDiscoverer-"
+ "-FigRouteDiscoverer- %s: (%p) %@"
+ "-FigRouteDiscoverer- %s: Discoverer %p clientName %{public}@ is suspended or terminated"
+ "-FigRouteDiscoverer- %s: Finalizing discoverer of type %{public}@ uuid=%{public}@ pid=%d clientName=%{public}@"
+ "-FigRouteDiscoverer- %s: Posting availableRoutesChanged for discoverer %p"
+ "-FigRouteDiscoverer- %s: Posting notification routePresentChanged for discoverer %p clientName: %{public}@ type: %{public}@"
+ "-FigRouteDiscoverer- %s: Registered discoverer of type %{public}@ uuid=%{public}@ pid=%d clientName=%{public}@"
+ "-FigRouteDiscoverer- %s: Unexpected type %d"
+ "-FigRouteDiscoverer- %s: cache miss for %{public}@"
+ "-FigRouteDiscoverer- %s: cache miss for audioSessionID: %u"
+ "-FigRouteDiscovererXPCRemote-"
+ "-FigRouteDiscovererXPCRemote- %s:  Endpoint Discoverer Remote Client created %d"
+ "-FigRouteDiscovererXPCRemote- %s: (%p) %@"
+ "-FigRouteDiscovererXPCRemote- %s: (%p) Discovered %d Endpoint(s)"
+ "-FigRouteDiscovererXPCRemote- %s: Dead connection callback %lld"
+ "-FigRouteDiscovererXPCServer-"
+ "-FigRouteDiscovererXPCServer- %s: %ld routes reported available by concrete endpoint discoverer"
+ "-FigRouteDiscovererXPCServer- %s: ->for cache endpoint in discoverer %p"
+ "-FigRouteDiscovererXPCServer- %s: Completed opCode '%c%c%c%c' err = %d"
+ "-FigRouteDiscovererXPCServer- %s: Discoverer has entitlements to access available routes: %d"
+ "-FigRouteDiscovererXPCServer- %s: FigRouteDiscoverer Server Started"
+ "-FigRouteDiscovererXPCServer- %s: Replying with objectAdditions %p containing %ld IDs"
+ "-FigRouteDiscovererXPCServer- %s: Replying with objectSubtractions %p containing %ld IDs"
+ "-FigRouteDiscovererXPCServer- %s: Starting opCode '%c%c%c%c'"
+ "-FigRouteDiscovererXPCServer- %s: Unknown opCode: 0x%0x"
+ "-FigRouteDiscoveryManager- %s: %@\n"
+ "-FigRouteDiscoveryManager- %s: AirPlay endpointPresent: %{public}@"
+ "-FigRouteDiscoveryManager- %s: Attempting to copy the fallback endpoint for %d"
+ "-FigRouteDiscoveryManager- %s: Available endpoints (%ld) "
+ "-FigRouteDiscoveryManager- %s: Discoverer '%p' with PID %d has application state %d"
+ "-FigRouteDiscoveryManager- %s: Discoverer '%p' with PID %d is suspended or terminated"
+ "-FigRouteDiscoveryManager- %s: Discovery manager not started!"
+ "-FigRouteDiscoveryManager- %s: Discovery mode: Desired %@ and aggregate: %@"
+ "-FigRouteDiscoveryManager- %s: Endpoint Present %@ for type %d"
+ "-FigRouteDiscoveryManager- %s: Endpoint manager=%@ does not support any of the requested features. Requested: %d, supported: %d"
+ "-FigRouteDiscoveryManager- %s: EndpointManager being registered before DiscoveryManager can initialize! Caching the endpointManager for now."
+ "-FigRouteDiscoveryManager- %s: Error: Something is terribly wrong, we should never come here. Please file a bug against MediaExperience | all discoveryMode=%@"
+ "-FigRouteDiscoveryManager- %s: Invalid requested features"
+ "-FigRouteDiscoveryManager- %s: New discovery mode is higher. oldMode = %@, newMode = %@."
+ "-FigRouteDiscoveryManager- %s: Nil fallbackRouteEndpoint for %d"
+ "-FigRouteDiscoveryManager- %s: No endpoint managers!"
+ "-FigRouteDiscoveryManager- %s: Number of available endpoints %ld for type %d"
+ "-FigRouteDiscoveryManager- %s: Number of discoverers (%ld)"
+ "-FigRouteDiscoveryManager- %s: Number of virtual audio endpoints available %ld"
+ "-FigRouteDiscoveryManager- %s: Original Dictionary:"
+ "-FigRouteDiscoveryManager- %s: Posting availableRoutesChanged for discoverer %p"
+ "-FigRouteDiscoveryManager- %s: Posting notification to all discoverers %@"
+ "-FigRouteDiscoveryManager- %s: Registering a new discoverer (%p)"
+ "-FigRouteDiscoveryManager- %s: Resetting switch down time leaving discovery mode in detailed for type %d"
+ "-FigRouteDiscoveryManager- %s: Starting switch down timer for %lld leaving discovery mode in detailed for type %d"
+ "-FigRouteDiscoveryManager- %s: Store discoverer (%p) for type %u"
+ "-FigRouteDiscoveryManager- %s: Switch down timer expired updating discovery mode to latest requested for type %d"
+ "-FigRouteDiscoveryManager- %s: Switchdown timer fired"
+ "-FigRouteDiscoveryManager- %s: Time taken to run notification handler %fms. Time taken to post %{public}@ to all discoverers: %fms. Average time: %fms. Cache misses this iteration %d. Time taken in RBS: %llu ms. Total calls to RBS: %d."
+ "-FigRouteDiscoveryManager- %s: Unsupported feature %u"
+ "-FigRouteDiscoveryManager- %s: Updated Dictionary"
+ "-FigRouteDiscoveryManager- %s: Updating available endpoints"
+ "-FigRouteDiscoveryManager- %s: Waiting for timer expiry [current %lld, timeout %lld]- leaving discovery mode in detailed for type %d"
+ "-FigRouteDiscoveryManager- %s: Will be setting the following sessionID (%d) on the discoverer"
+ "-FigRouteDiscoveryManager- %s: [%@] Number of available endpoints %ld"
+ "-FigRouteDiscoveryManager- %s: [%@] Number of filtered available endpoints %ld"
+ "-FigRouteDiscoveryManager- %s: endpointManagerType: %{public}@ endpointPresent: %{public}@"
+ "-FigRouteDiscoveryManager- %s: inPowerLogEventName = %{public}@, powerLogData = %{private}@\n"
+ "-FigRouteDiscoveryManager- %s: posting notification: %{public}@ with payload: %{public}@"
+ "-FigRoutingContext-"
+ "-FigRoutingContext- %s: %{public}@"
+ "-FigRoutingContext- %s: (%p) %@"
+ "-FigRoutingContext- %s: BundleID to query is: %{public}@"
+ "-FigRoutingContext- %s: Called"
+ "-FigRoutingContext- %s: Can't copy picked contexts (err = %d)"
+ "-FigRoutingContext- %s: Copied routingContext with context id: %@"
+ "-FigRoutingContext- %s: Copied system context of type %d"
+ "-FigRoutingContext- %s: Creating routingContext with context id: %@"
+ "-FigRoutingContext- %s: Dropped non-AirPlay endpoint %@"
+ "-FigRoutingContext- %s: Include subendpoint %@ in picked endpoint list"
+ "-FigRoutingContext- %s: Not supported on iOS"
+ "-FigRoutingContext- %s: Registered routingContext with context id: %@"
+ "-FigRoutingContext- %s: Subendpoint %@ has invalid type"
+ "-FigRoutingContext- %s: User picked an input route. Update the preferred route cache with the endpoint: %{private}@"
+ "-FigRoutingContext- %s: [%@] Called"
+ "-FigRoutingContext- %s: called (options=%{public}@"
+ "-FigRoutingContext- %s: completionContext is NULL!"
+ "-FigRoutingContext- %s: correlationID: %{public}@. round trip request time: %llu ms. time taken to reach server: %llu ms. time taken for modification result to reach client: %llu ms"
+ "-FigRoutingContext- %s: picked contexts: %@"
+ "-FigRoutingContext- %s: picked endpoints: %@"
+ "-FigRoutingContext- %s: timeTaken to copySelectedBufferedEndpoint: %llu ms. timeTaken to run block: %llu ms."
+ "-FigRoutingContextResilientRemote-"
+ "-FigRoutingContextResilientRemote- %s: Error replacing remote routing context: %d"
+ "-FigRoutingContextResilientRemote- %s: Error: %d"
+ "-FigRoutingContextResilientRemote- %s: Exceeded maximum retry count in %d tries, just failing (err=%d)"
+ "-FigRoutingContextResilientRemote- %s: Failed to post notification %@ from %p"
+ "-FigRoutingContextResilientRemote- %s: Forwarding notification %@ (listener=%p, notifyingObject=%p, payload=%@)"
+ "-FigRoutingContextResilientRemote- %s: No context type specified; falling back to creating a temporary context and asking it for its type.  This is subject to failure if mediaserverd crashes right...about...now"
+ "-FigRoutingContextResilientRemote- %s: Not forwarding notification %@ from not-current remote context %p (current remote context: %p)"
+ "-FigRoutingContextResilientRemote- %s: Server died: Let's make a new remote context (routingContext=%p)"
+ "-FigRoutingContextResilientRemote- %s: Server died: Over retry limit, not making a new remote context (routingContext=%p)"
+ "-FigRoutingContextResilientRemote- %s: Start listening to %@ on %p"
+ "-FigRoutingContextResilientRemote- %s: Stop listening to %@ on %p"
+ "-FigRoutingContextResilientRemote- %s: Successfully created a new remote context; resetting retry count (routingContext=%p)"
+ "-FigRoutingContextResilientRemote- %s: Unhandled routing context type %d.  Falling back to fetching context by ID with options %@"
+ "-FigRoutingContextResilientRemote- %s: Using shared audio context %@"
+ "-FigRoutingContextResilientRemote- %s: [%p] Replacement remote context: %p"
+ "-FigRoutingContextResilientRemote- %s: [%p] Start listening to remote context %p"
+ "-FigRoutingContextResilientRemote- %s: [%p] Stop listening to remote context %p"
+ "-FigRoutingContextXPCRemote-"
+ "-FigRoutingContextXPCRemote- %s:  Copied existing remote context %p with objectID %llx"
+ "-FigRoutingContextXPCRemote- %s:  Copy context for UUID %@..."
+ "-FigRoutingContextXPCRemote- %s:  Copying a system context..."
+ "-FigRoutingContextXPCRemote- %s:  Created new remote context %p with objectID %llx"
+ "-FigRoutingContextXPCRemote- %s:  Creating new context..."
+ "-FigRoutingContextXPCRemote- %s:  Endpoint Name: %@"
+ "-FigRoutingContextXPCRemote- %s:  Routing Context Remote Client created %d"
+ "-FigRoutingContextXPCRemote- %s: (%p) %@"
+ "-FigRoutingContextXPCRemote- %s: (%p) objID %llx uuid %@"
+ "-FigRoutingContextXPCRemote- %s: Completed opCode '%c%c%c%c' err = %d"
+ "-FigRoutingContextXPCRemote- %s: Creating remote context with objectID %llx failed with err=%d"
+ "-FigRoutingContextXPCRemote- %s: Dead connection callback %016llx"
+ "-FigRoutingContextXPCRemote- %s: Failed to find entry for completionID %llu"
+ "-FigRoutingContextXPCRemote- %s: FigXPCRemoteClientRetainCopiedObject failed with err = %d"
+ "-FigRoutingContextXPCRemote- %s: Handling completion callback for entry %llu"
+ "-FigRoutingContextXPCRemote- %s: Removing UUID %@"
+ "-FigRoutingContextXPCRemote- %s: Routing context object ID is 0 for index=%ld"
+ "-FigRoutingContextXPCRemote- %s: Starting opCode '%c%c%c%c'"
+ "-FigRoutingContextXPCRemote- %s: Unknown opCode: 0x%0x"
+ "-FigRoutingContextXPCServer-"
+ "-FigRoutingContextXPCServer- %s:  Endpoint Name: %@"
+ "-FigRoutingContextXPCServer- %s: %ld endpoints reported available FigRoutingContextCopySelectedRoutes"
+ "-FigRoutingContextXPCServer- %s: Associate routingContext [%p] with client pid: %d, server state: [%p]"
+ "-FigRoutingContextXPCServer- %s: Completed opCode '%c%c%c%c' err = %d"
+ "-FigRoutingContextXPCServer- %s: Copying selected route"
+ "-FigRoutingContextXPCServer- %s: Disposing server state [%p]"
+ "-FigRoutingContextXPCServer- %s: FigRouting Context Server Started"
+ "-FigRoutingContextXPCServer- %s: Received send command completion callback for completionID %lld"
+ "-FigRoutingContextXPCServer- %s: Received send command message for completionID: %lld"
+ "-FigRoutingContextXPCServer- %s: Received send command message with no completionCallbackParams"
+ "-FigRoutingContextXPCServer- %s: Received send data completion callback for completionID %lld"
+ "-FigRoutingContextXPCServer- %s: Received send data message for completionID: %lld"
+ "-FigRoutingContextXPCServer- %s: Received send data message with no completionCallbackParams"
+ "-FigRoutingContextXPCServer- %s: Starting opCode '%c%c%c%c'"
+ "-FigRoutingContextXPCServer- %s: Unable to get client PID!"
+ "-FigRoutingContextXPCServer- %s: Unexpected contextType: %llu"
+ "-FigRoutingContextXPCServer- %s: Unknown opCode: 0x%0x"
+ "-FigRoutingContextXPCServer- %s: [%p] Closing commChannels: %@"
+ "-FigRoutingContextXPCServer- %s: [%p] Registered (%@, %@) ==> %@"
+ "-FigRoutingContextXPCServer- %s: [%p] Unregistered (%@, %@) ==> %@"
+ "-FigRoutingContextXPCServer- %s: routingContext isSystemRoutingContext: %d, and has entitlements to set endpoint: %d"
+ "-FigRoutingManager- %s:  Please make sure you have right defaults writes to test SidePlay on iOS."
+ "-FigRoutingManager- %s: %@ %@ %@"
+ "-FigRoutingManager- %s: %@ endpointIDs=%@ %@"
+ "-FigRoutingManager- %s: Activating aggregate endpoint failed with error=%d"
+ "-FigRoutingManager- %s: Adding following options to the aggregate. %{public}@"
+ "-FigRoutingManager- %s: Authorization type is %@, there is no FigEndpointSetProperty associated with it"
+ "-FigRoutingManager- %s: Available endpoints (%ld) "
+ "-FigRoutingManager- %s: Bluetooth endpoint manager created %p\n"
+ "-FigRoutingManager- %s: CFUUIDCreate resulted in NULL UUID"
+ "-FigRoutingManager- %s: Copying available endpoints from AirPlay endpoint manager returned err=%d"
+ "-FigRoutingManager- %s: Copying available endpoints from VA endpoint manager returned err=%d"
+ "-FigRoutingManager- %s: Did not find appropriate mapped BT endpoint. Error=%d"
+ "-FigRoutingManager- %s: Error getting AirPlay endpoint manager"
+ "-FigRoutingManager- %s: FigEndpointAggregateAddEndpoint returned err=%d"
+ "-FigRoutingManager- %s: FigEndpointAggregateRemoveEndpoint returned err=%d"
+ "-FigRoutingManager- %s: FigRoutingManager_HandleDidReceiveDataFromCommChannelDelegate for commChannelUUID=%{public}@"
+ "-FigRoutingManager- %s: FigRoutingManager_HandleDidReceiveDataFromCommChannelDelegate for commChannelUUID=%{public}@, deviceID=%{private}@, endpointName=%{public}@"
+ "-FigRoutingManager- %s: Going to deactivate endpoint=%p with endpointID=%@, endpointName=%@ because port was not published within %f seconds"
+ "-FigRoutingManager- %s: MediaExperience was unable to register AirPlayEndpointManager with err = %d"
+ "-FigRoutingManager- %s: MediaExperience was unable to register BluetoothEndpointManager with err = %d"
+ "-FigRoutingManager- %s: MediaExperience was unable to register CarPlayEndpointManager with err = %d"
+ "-FigRoutingManager- %s: MediaExperience was unable to register NeroEndpointManager"
+ "-FigRoutingManager- %s: No AirPlay endpoint manager was found"
+ "-FigRoutingManager- %s: Picking timeout for %@"
+ "-FigRoutingManager- %s: Queue creation failed for creating BT endpoint manager!"
+ "-FigRoutingManager- %s: Register context called"
+ "-FigRoutingManager- %s: Register context with UUID called"
+ "-FigRoutingManager- %s: Routing context options has both avoidAuthPrompt and SilentSender set to true. It should only be one!"
+ "-FigRoutingManager- %s: The pickedEndpointName=%{public}@, routingContextUUID=%{public}@, pickedEndpointType=%{public}@"
+ "-FigRoutingManager- %s: The selected SidePlay endpoint details are: routingContextType=%{public}@, deviceID(from client)=%{private}@, selectedBufferedEndpointName=%{public}@"
+ "-FigRoutingManager- %s: The selected carPlay endpoint features are: features = %d"
+ "-FigRoutingManager- %s: The selectedBufferedEndpointName=%{public}@"
+ "-FigRoutingManager- %s: Unable to activate endpoint with error=%d"
+ "-FigRoutingManager- %s: Unable to get all available bluetooth endpoints with error %d"
+ "-FigRoutingManager- %s: Will%s enable local playback for aggregate -- thank you for setting \"defaults write com.apple.coremedia aggregate_local_playback -bool %s\""
+ "-FigRoutingManager- %s: creating routingManager->deactivateAirPlayEndpointTimer, routingManager->queue = %p, timer delay = %f"
+ "-FigRoutingManager- %s: endpoint is NULL"
+ "-FigRoutingManager- %s: inCommChannelUUID is NULL"
+ "-FigRoutingManager- %s: inData is NULL"
+ "-FigRoutingManager- %s: inEndpoint is NULL"
+ "-FigRoutingManager- %s: inSubEndpoint is NULL!"
+ "-FigRoutingManager- %s: outGroupUUID is NULL"
+ "-FigRoutingManager- %s: releasing routingManager->deactivateAirPlayEndpointTimer"
+ "-FigRoutingManager- %s: routingContextUUID is NULL"
+ "-FigRoutingManager- %s: routingManager: endpointName = %{public}@, inActivationSeed=%llu, err = %d, inFeatures=%d, routingContextType=%{public}@, correlationID=%{public}@. Time taken to removeEndpoint: %f ms. Time taken to run callback %f ms. Total round trip time: %f ms."
+ "-FigRoutingManager- %s: routingManager_EndpointHelpers: endpointName = %{public}@, inActivationSeed=%llu, err = %d, inFeatures=%d, routingContextType=%{public}@, correlationID=%{public}@. Time taken to addEndpoint: %f ms. Time taken to run callback %f ms. Total round trip time: %f ms."
+ "-FigRoutingManager-Utilities %s: Copying available endpoints from SidePlay endpoint manager returned err=%d"
+ "-FigRoutingManager-Utilities %s: currentPort = %u : partnerPort = %{public}@"
+ "-FigRoutingManager-Utilities %s: port = %u, Endpoint name = %{public}@"
+ "-FigRoutingManagerContextUtilities- %s: %@"
+ "-FigRoutingManagerContextUtilities- %s: Adding activated endpoint [%p] for %@ (%@)"
+ "-FigRoutingManagerContextUtilities- %s: CMSession/MX: endpointToFindID was found to be NULL for device name=%@, type=%@"
+ "-FigRoutingManagerContextUtilities- %s: Checking if following context %@ (%@) has a picked endpoint"
+ "-FigRoutingManagerContextUtilities- %s: Error initializing ContextUtilities: no callback provided"
+ "-FigRoutingManagerContextUtilities- %s: Error initializing ContextUtilities: null ContextState"
+ "-FigRoutingManagerContextUtilities- %s: Leader existed, resetting the leader"
+ "-FigRoutingManagerContextUtilities- %s: Leader for other types should never be more than 1"
+ "-FigRoutingManagerContextUtilities- %s: Removing a leader, current leader count is %ld"
+ "-FigRoutingManagerContextUtilities- %s: Removing activated endpoint [%p] for %@ (%@)"
+ "-FigRoutingManagerContextUtilities- %s: Resetting UUID leader info for follower %@ (%@); no longer following %@ (%@)"
+ "-FigRoutingManagerContextUtilities- %s: Routing Context utilities created"
+ "-FigRoutingManagerContextUtilities- %s: Routing manager %p failed to create system routing context of type %@ with err: %d"
+ "-FigRoutingManagerContextUtilities- %s: Set picking state to %@ for %@ (%@)"
+ "-FigRoutingManagerContextUtilities- %s: Setting UUID leader %@ (%@) for follower %@ (%@)"
+ "-FigRoutingManagerContextUtilities- %s: Setting default leader for %@ (%@) to %@ (%@)"
+ "-FigRoutingManagerContextUtilities- %s: Starting following defaultLeaderUUID since pickedEndpoint is NULL for %@ (%@)"
+ "-FigRoutingManagerContextUtilities- %s: UUID  or endpoint is NULL"
+ "-FigRoutingManagerContextUtilities- %s: UUID  or routeUID is NULL"
+ "-FigRoutingManagerContextUtilities- %s: UUID %@ is unexpected"
+ "-FigRoutingManagerContextUtilities- %s: UUID %@ not found"
+ "-FigRoutingManagerContextUtilities- %s: UUID is NULL"
+ "-FigRoutingManagerContextUtilities- %s: Unexpected UUID %@"
+ "-FigRoutingManagerContextUtilities- %s: Unexpected index value %ld"
+ "-FigRoutingManagerContextUtilities- %s: Unexpected type %d"
+ "-FigRoutingManagerContextUtilities- %s: context was not found for UUID=%@"
+ "-FigRoutingManagerContextUtilities- %s: found leader context %@ (%@) has a picked endpoint"
+ "-FigRoutingManagerContextUtilities- %s: picking timer fired for '%@' '%@'"
+ "-FigRoutingManagerContextUtilities- %s: routingContextUUID %@ not found"
+ "-FigRoutingManagerContextUtilities- %s: routingContextUUID is NULL"
+ "-FigRoutingManager_SystemRemotePool- %s: Extended endpoint is NULL for deviceID=%{private}@, commChannelUUID=%{public}@"
+ "-FigRoutingManager_SystemRemotePool- %s: Extended endpoint is NULL for deviceID=%{private}@, options=%{public}@"
+ "-FigRoutingManager_SystemRemotePool- %s: FigEndpointAggregateAddEndpoint returned err=%d"
+ "-FigRoutingManager_SystemRemotePool- %s: Sub endpoint info was not provided in the inFailureInfo dictionary. Delegate for error=%{public}d, failureType=%{public}@"
+ "-FigRoutingManager_SystemRemotePool- %s: commChannelUUID is NULL"
+ "-FigRoutingManager_SystemRemotePool- %s: completionContext is NULL!"
+ "-FigRoutingManager_SystemRemotePool- %s: data is NULL"
+ "-FigRoutingManager_SystemRemotePool- %s: deviceID is NULL"
+ "-FigRoutingManager_SystemRemotePool- %s: endpointToAdd is NULL - notify clients of no-op operation"
+ "-FigRoutingManager_SystemRemotePool- %s: endpointToRemove is NULL - notify clients of no-op operatio"
+ "-FigRoutingManager_SystemRemotePool- %s: inEndpoint is NULL"
+ "-FigRoutingManager_SystemRemotePool- %s: inFailureInfo is NULL"
+ "-FigRoutingManager_SystemRemotePool- %s: inSubEndpoint is NULL!"
+ "-FigRoutingManager_SystemRemotePool- %s: mxSystemRemotePool: endpointName = %{public}@, inActivationSeed=%llu, err = %d, inFeatures=%d, correlationID=%{public}@. Time taken to activateEndpoint: %f ms. Time taken to run callback %f ms. Total round trip time: %f ms."
+ "-FigRoutingManager_SystemRemotePool- %s: outCommChannelUUID is NULL"
+ "-FigRoutingManager_iOS- %s: '%@' An array of routes is being picked for audio context on non-HomePods. That's not supported"
+ "-FigRoutingManager_iOS- %s: '%@' An array of routes is being picked for something other than SystemAudio, SystemMusic or SystemRemotePool. That's very odd"
+ "-FigRoutingManager_iOS- %s: '%@' Audio context or SystemVideoDisplayMenu context showed up on iOS. That's strange."
+ "-FigRoutingManager_iOS- %s: '%@' PerAppVideo context is following another routingContext; picking on that instead."
+ "-FigRoutingManager_iOS- %s: '%@' PerAppVideo context needs to follow systemAudio at the end of this route change"
+ "-FigRoutingManager_iOS- %s: '%@' SystemMusic is following another routingContext; picking on that instead."
+ "-FigRoutingManager_iOS- %s: '%@' SystemRemotePool is its own leader, always."
+ "-FigRoutingManager_iOS- %s: '%@' Video context was following and is now independent"
+ "-FigRoutingManager_iOS- %s: Add endpoint is not allowed for routing context type %@"
+ "-FigRoutingManager_iOS- %s: Adding partner port %u to result"
+ "-FigRoutingManager_iOS- %s: All output parameters are NULL"
+ "-FigRoutingManager_iOS- %s: ConnectBanner is active, not allowing route picking now, returning false"
+ "-FigRoutingManager_iOS- %s: Endpoint can't be NULL for audio/system audio/system audio input context"
+ "-FigRoutingManager_iOS- %s: FigEndpointAggregateAddEndpoint returned err=%d"
+ "-FigRoutingManager_iOS- %s: FigEndpointAggregateRemoveEndpoint returned err=%d"
+ "-FigRoutingManager_iOS- %s: FigRoutingManagerContextUtilities_SetPickingState returned err=%d"
+ "-FigRoutingManager_iOS- %s: Ignoring routing to BT port %{public}@/%{public}@ since BT port is paired to CarPlay"
+ "-FigRoutingManager_iOS- %s: One of the endpoints is null; unable to update smart routing backoff timer."
+ "-FigRoutingManager_iOS- %s: Pick endpoints is not allowed for routing context type %@"
+ "-FigRoutingManager_iOS- %s: Picking routeName: %{public}@, routeUID : %{public}@, routeMacAddress : %{public}@"
+ "-FigRoutingManager_iOS- %s: Returning true as routeDescriptor = NULL"
+ "-FigRoutingManager_iOS- %s: Reverse endpoint name = %{public}@"
+ "-FigRoutingManager_iOS- %s: Reverse endpoints array = NULL"
+ "-FigRoutingManager_iOS- %s: Reversing from BT speaker"
+ "-FigRoutingManager_iOS- %s: Reversing from CarPlay"
+ "-FigRoutingManager_iOS- %s: Session %{public}@ is nil or has incorrect category %{public}@, returning"
+ "-FigRoutingManager_iOS- %s: _endpointsToRoute = NULL"
+ "-FigRoutingManager_iOS- %s: _routingContextUUID = %{public}@"
+ "-FigRoutingManager_iOS- %s: allAvailableEndpoints = [%p], autoconnectEndpoints = [%p]"
+ "-FigRoutingManager_iOS- %s: endpointToAutoconnect is AirPlay, but we are already routed to an autoconnect AirPlay. Do nothing"
+ "-FigRoutingManager_iOS- %s: endpointToAutoconnect is CarPlay, but CarPlay endpoint is still connected and available. Do nothing"
+ "-FigRoutingManager_iOS- %s: endpointToAutoconnect is Nero, but Nero is already connected. Do nothing"
+ "-FigRoutingManager_iOS- %s: error picking endpoints; there is most likely a problem with the logic in routingManager_copyFilteredEndpoints"
+ "-FigRoutingManager_iOS- %s: inAggregate is NULL!"
+ "-FigRoutingManager_iOS- %s: isrouted = %hhu"
+ "-FigRoutingManager_iOS- %s: mostRecentCurrentlyActivatingEndpoint = NULL"
+ "-FigRoutingManager_iOS- %s: mostRecentCurrentlyActivatingEndpoint name = %{public}@"
+ "-FigRoutingManager_iOS- %s: newPortMacAddress = %{public}@, matchingVehicle = nil }"
+ "-FigRoutingManager_iOS- %s: newPortMacAddress = %{public}@, vehicleName = %{public}@, vehicleIdentifier = %{public}@"
+ "-FigRoutingManager_iOS- %s: newPortName  = %{public}@, newPortSubType = %{public}@, newPortDeviceIdentifier = %{public}@, newPortMacAddress = %{public}@, oldPortName = %{public}@, isCurrentRouteHeadphonesAndInEar = %{public}hhu, isSupportedTargetType = %{public}hhu, newPortType = %{public}@"
+ "-FigRoutingManager_iOS- %s: newPortName  = %{public}@, newPortSubType = %{public}@, portDeviceIdentifier = %{public}@, portMacAddress = %{public}@, mostRecentCurrentlyActivatingEndpoint name = %{public}@, routingType = %ld"
+ "-FigRoutingManager_iOS- %s: oldRouteIdentifiers=%{private}@, newRouteIdentifiers=%{private}@, newInputRouteIdentifiers=%{private}@, userPickedRoute=%{public}s, airPlayShouldIgnoreRouteChange=%{public}s, newRoutingContextType=%{public}@"
+ "-FigRoutingManager_iOS- %s: parent, mostRecentCurrentlyActivatingEndpoint = NULL"
+ "-FigRoutingManager_iOS- %s: parent, mostRecentCurrentlyActivatingEndpoint name = %{public}@"
+ "-FigRoutingManager_iOS- %s: prevEndpoint[%ld] name = %{public}@"
+ "-FigRoutingManager_iOS- %s: routingPreference, preferHeadphonesOverCarsAndSpeakersEnabled = %d"
+ "-FigRoutingManager_iOS- %s: routingType == kMXCustomizedRoutingTypeBTSpeaker"
+ "-FigRoutingManager_iOS- %s: routingType == kMXCustomizedRoutingTypeCarPlay"
+ "-FigRoutingManager_iOS- %s: shouldUseCustomizedRouting = %{public}@"
+ "-FigRoutingManager_iOSAirPlay- %s: FigRoutingManager_iOSActivateEndpoint returned err=%d"
+ "-FigRoutingManager_iOSCarPlay- %s: Duck command sent with inDuckPayload = %@, err = %d"
+ "-FigRoutingManager_iOSCarPlay- %s: Endpoint with endpointID=%@, endpointName=%@ did not publish CarMain audio port within %f seconds"
+ "-FigRoutingManager_iOSCarPlay- %s: NOT sending disable bluetooth command on BT device mac address = %@ because endpoint is NULL"
+ "-FigRoutingManager_iOSCarPlay- %s: Sending CARPLAY_SUPPORT_AUX_STREAM notification of False."
+ "-FigRoutingManager_iOSCarPlay- %s: creating routingManager->carplayAudioMainPortPublishingCheckTimer, routingManager->queue = %p, timer delay = %f"
+ "-FigRoutingManager_iOSCarPlay- %s: inEndpoint is NULL"
+ "-FigRoutingManager_iOSCarPlay- %s: releasing routingManager->carplayAudioMainPortPublishingCheckTimer"
+ "-FigRoutingManager_iOSCarPlay- %s: routingContextUUID is NULL"
+ "-FigRoutingManager_iOSCarPlay- %s: sending disableBluetooth command, BT device mac address = %@, errorCode = %d"
+ "-FigRoutingManager_iOSEndpointHelpers- %s: Endpoint = %@ is already NOT active"
+ "-FigRoutingManager_iOSEndpointHelpers- %s: ErrorInfo is Null!"
+ "-FigRoutingManager_iOSEndpointHelpers- %s: No activation seed was provided for endpoint type=%@, endpoint name=%@"
+ "-FigRoutingManager_iOSEndpointHelpers- %s: No activation seed was provided for endpointType=%@, notificationName=%@"
+ "-FigRoutingManager_iOSEndpointHelpers- %s: Sending CARPLAY_IS_CONNECTED notification."
+ "-FigRoutingManager_iOSEndpointHelpers- %s: called for [%p]"
+ "-FigRoutingManager_iOSEndpointHelpers- %s: called for [%p], routingContextUUID=%@"
+ "-FigRoutingManager_iOSEndpointHelpers- %s: endpoint is NULL"
+ "-FigRoutingManager_iOSEndpointHelpers- %s: endpointToAutoconnect is NULL"
+ "-FigRoutingManager_iOSEndpointHelpers- %s: endpointToDeactivate is NULL"
+ "-FigRoutingManager_iOSEndpointHelpers- %s: inEndpoint is NULL"
+ "-FigRoutingManager_iOSEndpointHelpers- %s: inEndpoint is NULL!"
+ "-FigRoutingManager_iOSEndpointHelpers- %s: inFailureInfo is NULL"
+ "-FigRoutingManager_iOSEndpointHelpers- %s: resetScreenSettings was called with NULL endpoint"
+ "-FigRoutingManager_iOSEndpointHelpers- %s: routingContextUUID is NULL!"
+ "-FigRoutingManager_iOSEndpointHelpers- %s: routingManager_iOS: endpointName = %{public}@, inActivationSeed=%llu, err = %d, inFeatures=%d, correlationID=%{public}@. Time taken to activate endpoint: %f ms. Time taken to run callback: %f ms. Total round trip time: %f ms."
+ "-FigRoutingSession-"
+ "-FigRoutingSessionManager-"
+ "-FigRoutingSessionManager- %s: ...done updating pending route descriptors"
+ "-FigRoutingSessionManager- %s: ...done waiting for new predictions"
+ "-FigRoutingSessionManager- %s: Attempting to invoke completion handler due to already having a prediction from %@ (oldest allowed: %@)"
+ "-FigRoutingSessionManager- %s: Attempting to invoke completion handler due to receiving prediction update"
+ "-FigRoutingSessionManager- %s: Attempting to invoke completion handler due to timeout"
+ "-FigRoutingSessionManager- %s: Could not copy predictions because the route predictor is not available, likely due to rdar://problem/47634814"
+ "-FigRoutingSessionManager- %s: Discovered predicted routes %{public}@ for routing session %@"
+ "-FigRoutingSessionManager- %s: Discovered routes (%@) (err=%d)"
+ "-FigRoutingSessionManager- %s: End current session? %d (now=%f, sessionExpirationTime=%f)"
+ "-FigRoutingSessionManager- %s: Failed to discover new pending route: %d"
+ "-FigRoutingSessionManager- %s: Finished updating route predictions before waiting for recent predictions: %d"
+ "-FigRoutingSessionManager- %s: Finished updating route predictions: %d"
+ "-FigRoutingSessionManager- %s: Forced high-confidence route UID: %@"
+ "-FigRoutingSessionManager- %s: Forced high-confidence route name: %@"
+ "-FigRoutingSessionManager- %s: Forced medium-confidence route UID: %@"
+ "-FigRoutingSessionManager- %s: Forced medium-confidence route name: %@"
+ "-FigRoutingSessionManager- %s: Found routes (%@)"
+ "-FigRoutingSessionManager- %s: Invoke completion handler due to synchronous error"
+ "-FigRoutingSessionManager- %s: Invoking callback %p (callbackContext=%p)"
+ "-FigRoutingSessionManager- %s: Invoking callback %p with error %d (callbackContext=%p)"
+ "-FigRoutingSessionManager- %s: MobileWiFi framework not loaded"
+ "-FigRoutingSessionManager- %s: No current session"
+ "-FigRoutingSessionManager- %s: No session expiration date"
+ "-FigRoutingSessionManager- %s: Non-fatal error establishing session from active SharePlay-capable call session: %d"
+ "-FigRoutingSessionManager- %s: Non-fatal error establishing session from connected in-ear headphones: %d"
+ "-FigRoutingSessionManager- %s: Not updating current session because current session is not the required session %@"
+ "-FigRoutingSessionManager- %s: Not updating session expiration because session has a non-local route"
+ "-FigRoutingSessionManager- %s: Prediction from %@ too old (oldest allowed: %@)"
+ "-FigRoutingSessionManager- %s: Prediction probabilities do not add up to 1.0.  Remaining probability: %f"
+ "-FigRoutingSessionManager- %s: Returning immediately because route predictions are disabled"
+ "-FigRoutingSessionManager- %s: Route descriptor selection failed or was cancelled (configUpdateID=%@, reason=%@)"
+ "-FigRoutingSessionManager- %s: Route prediction disabled, bailing"
+ "-FigRoutingSessionManager- %s: RoutingSessionManagerConfiguration was not of the expected type"
+ "-FigRoutingSessionManager- %s: Successfully selected route descriptors (configUpdateID=%@, reason=%@)"
+ "-FigRoutingSessionManager- %s: Updated current session expiration time to %{public}@"
+ "-FigRoutingSessionManager- %s: Updating pending route descriptors..."
+ "-FigRoutingSessionManager- %s: Updating session without prediction context for now ..."
+ "-FigRoutingSessionManager- %s: Waiting for predictions to update due to new MicroLocation triggered by app launch..."
+ "-FigRoutingSessionManager- %s: called (candidateSession=%@, candidateSessionPredictionContext=%@, candidateSessionHasPendingRoute=%d, candidateSessionIsBasedOnPrediction=%d, reason=%@)"
+ "-FigRoutingSessionManager- %s: called (payload=%@)"
+ "-FigRoutingSessionManager- %s: failed to load AirPlayRoutePrediction.framework: %d"
+ "-FigRoutingSessionManager- %s: outRoutingSessionManager = %p, err = %d"
+ "-FigRoutingSessionManager- %s: returning %@"
+ "-FigRoutingSessionManagerResilientRemote-"
+ "-FigRoutingSessionManagerResilientRemote- %s: Failed to post notification %@ from %p"
+ "-FigRoutingSessionManagerResilientRemote- %s: Forwarding notification %@ (listener=%p, notifyingObject=%p, payload=%@)"
+ "-FigRoutingSessionManagerResilientRemote- %s: Server died: Let's make a new remote manager (manager=%p)"
+ "-FigRoutingSessionManagerResilientRemote- %s: Server died: Over retry limit, not making a new remote manager (mangager=%p)"
+ "-FigRoutingSessionManagerResilientRemote- %s: Successfully created a new remote manager; resetting retry count (manager=%p)"
+ "-FigRoutingSessionManagerXPCRemote-"
+ "-FigRoutingSessionManagerXPCRemote- %s: (%p) objID %llx"
+ "-FigRoutingSessionManagerXPCRemote- %s: Completed opCode '%c%c%c%c' err = %d"
+ "-FigRoutingSessionManagerXPCRemote- %s: Copied existing remote session manager %p with objectID %llx"
+ "-FigRoutingSessionManagerXPCRemote- %s: Created new remote session manager %p with objectID %llx"
+ "-FigRoutingSessionManagerXPCRemote- %s: Dead connection callback %016llx"
+ "-FigRoutingSessionManagerXPCRemote- %s: Handling completion callback for entry %llu"
+ "-FigRoutingSessionManagerXPCRemote- %s: Routing Session Manager Remote Client created %d"
+ "-FigRoutingSessionManagerXPCRemote- %s: Starting opCode '%c%c%c%c'"
+ "-FigRoutingSessionManagerXPCRemote- %s: Unknown opCode: 0x%0x"
+ "-FigRoutingSessionManagerXPCServer-"
+ "-FigRoutingSessionManagerXPCServer- %s: Completed opCode '%c%c%c%c' err = %d"
+ "-FigRoutingSessionManagerXPCServer- %s: FigRoutingSessionManager Server Started"
+ "-FigRoutingSessionManagerXPCServer- %s: Received start high confidence session message for completionID: %lld"
+ "-FigRoutingSessionManagerXPCServer- %s: Received start high confidence session with no callback"
+ "-FigRoutingSessionManagerXPCServer- %s: Received update current session from likely destinations message for completionID: %lld"
+ "-FigRoutingSessionManagerXPCServer- %s: Received update current session from likely destinations with no callback"
+ "-FigRoutingSessionManagerXPCServer- %s: Starting opCode '%c%c%c%c'"
+ "-FigRoutingSessionManagerXPCServer- %s: Unknown opCode: 0x%0x"
+ "-FigRoutingSessionManagerXPCServer- %s: called"
+ "-FigSTSRemote-"
+ "-FigSTSRemote- %s: Created sts %p flavor %@ options {%@} objectID %016llx"
+ "-FigSTSRemote- %s: [%p] %@"
+ "-FigSTSRemote- %s: sts %p objectID %016llx"
+ "-FigSTSRemote- %s: sts %p objectID %016llx label \"%@\" active -> %s"
+ "-FigSTSRemote- %s: sts %p objectID %016llx label \"%@\" isActive == %s"
+ "-FigSTSRemote- %s: sts %p objectID %016llx label \"%@\" propertyKey %@"
+ "-FigSTSRemote- %s: sts %p objectID %016llx shmemName \"%@\""
+ "-FigSTSServer-"
+ "-FigSTSServer- %s: Completed opCode '%c%c%c%c' err = %d"
+ "-FigSTSServer- %s: Disposing sts %p objectID %016llx"
+ "-FigSTSServer- %s: FigSTS server %s is running."
+ "-FigSTSServer- %s: Starting opCode '%c%c%c%c'"
+ "-FigSTSServer- %s: Unknown opCode: 0x%0x"
+ "-FigSTSServer- %s: sts %p objectID %016llx CopyProperty %@"
+ "-FigSTSServer- %s: sts %p objectID %016llx SetProperty %@"
+ "-FigSTSServer- %s: sts %p objectID %016llx label \"%@\" active -> %s"
+ "-FigSTSServer- %s: sts %p objectID %016llx label \"%@\" active == %s"
+ "-FigSTSServer- %s: sts %p objectID %016llx label \"%@\" propertyKey %@"
+ "-FigSTSServer- %s: sts %p objectID %016llx shmemName %@"
+ "-FigSTSServer- %s: stsFlavor %@ options {%@} -> sts %p objectID %016llx"
+ "-FigSTS_Common-"
+ "-FigSTS_Common- %s:  did not find entry point %s of dylib %s"
+ "-FigSTS_Common- %s: Creation function for flavor %@"
+ "-FigSTS_Common- %s: did not find dylib %s - %s"
+ "-FigStarkModeChange_ActionMapper- %s: Could not load ModeChangeRequestActions.plist"
+ "-FigStarkModeChange_ActionMapper- %s: constraint is NULL"
+ "-FigStarkModeChange_ActionMapper- %s: map entry from V1 Table: %ld"
+ "-FigStarkModeChange_ActionMapper- %s: map entry from V2 Table: %ld"
+ "-FigStarkModeChange_ActionMapper- %s: modeChangeActions is NULL"
+ "-FigStarkModeChange_ActionMapper- %s: modeDict is NULL"
+ "-FigStarkModeChange_ActionMapper- %s: modeRequestDict is NULL"
+ "-FigStarkModeChange_ActionMapper- %s: previousModeEncoding=%u, currentModeEncoding=%u, audioRequestEncoding=%llu, screenRequestEncoding=%llu, useActionTableV1=%s"
+ "-FigStarkModeChange_ActionMapper- %s: sFigStarkModeActionMap_V1=%@, numEntries=%ld"
+ "-FigStarkModeChange_ActionMapper- %s: transferPriority is NULL"
+ "-FigStarkModeChange_ActionMapper- %s: transferType is NULL"
+ "-FigStarkModeControllerRemote-"
+ "-FigStarkModeControllerRemote- %s: (%p/%016llx)"
+ "-FigStarkModeControllerRemote- %s: FigStarkModeController remote created %p/%016llx"
+ "-FigStarkModeControllerRemote- %s: FigStarkModeControllerRemoteClient is successfully created %p"
+ "-FigStarkModeControllerRemote- %s: FigXPCRemoteClientCreate failed with error=%d, gFigStarkModeControllerRemoteClient=%p"
+ "-FigStarkModeControllerServer-"
+ "-FigStarkModeControllerServer- %s: Creating FigStarkModeController with PID %d"
+ "-FigStarkModeControllerServer- %s: Finished opCode '%c%c%c%c' object %p/%016llx"
+ "-FigStarkModeControllerServer- %s: Starting opCode '%c%c%c%c' object %p/%016llx"
+ "-FigStarkModeControllerServer- %s: Unknown opCode: '%c%c%c%c'"
+ "-FigSystemController-"
+ "-FigSystemController- %s: (%p) Completed operation = %s, volume = %1.3f, muted = %s, outCategory = %@, outSequenceNumber = %lld"
+ "-FigSystemController- %s: (%p) operation = %s, value = %1.3f, inAudioCategory: %@"
+ "-FigSystemController- %s: *** ** * Unknown property %@"
+ "-FigSystemController- %s: Failed to allocate property mapping dictionary"
+ "-FigSystemController- %s: Finalizing FigSystemController for client with PID %d"
+ "-FigSystemController- %s: NULL payload for the notification : %@"
+ "-FigSystemController- %s: [%p]"
+ "-FigSystemController- %s: [%p] %@"
+ "-FigSystemController- %s: [%p] bundleID: %@"
+ "-FigSystemController- %s: [%p] category: %@"
+ "-FigSystemController- %s: [%p] category: %@, mode: %@"
+ "-FigSystemController- %s: [%p] created MXSystemController %p for client with PID: %d"
+ "-FigSystemController- %s: [%p] property %@"
+ "-FigSystemController- %s: [%p] silentMode: %d, time: %@, reason = %@"
+ "-FigSystemController- %s: couldn't obtain active audio route with err=%d"
+ "-FigSystemController- %s: deviceIdentifier: %@"
+ "-FigSystemController- %s: route: %@"
+ "-FigSystemControllerRemote-"
+ "-FigSystemControllerRemote- %s: (%p/%016llx)"
+ "-FigSystemControllerRemote- %s: (%p/%016llx) bundleID %@"
+ "-FigSystemControllerRemote- %s: (%p/%016llx) category %@"
+ "-FigSystemControllerRemote- %s: (%p/%016llx) category %@ mode %@"
+ "-FigSystemControllerRemote- %s: (%p/%016llx) operation %d (%s) changeValue %1.3f inAudioCategory %@ audioRoute %@ deviceIdentifier %@ rampUpwardDuration %f rampDownwardDuration %f"
+ "-FigSystemControllerRemote- %s: (%p/%016llx) property %@"
+ "-FigSystemControllerRemote- %s: (%p/%016llx) property %@ value %p"
+ "-FigSystemControllerRemote- %s: FigSystemController remote created %p/%016llx"
+ "-FigSystemControllerRemote- %s: FigSystemControllerRemoteClient is successfully created %p"
+ "-FigSystemControllerRemote- %s: FigXPCRemoteClientCreate failed with error=%d, gFigSystemControllerRemoteClient=%p"
+ "-FigSystemControllerRemote- %s: mappedCategory: %@"
+ "-FigSystemControllerRemote- %s: mappedMode: %@"
+ "-FigSystemControllerServer-"
+ "-FigSystemControllerServer- %s: Creating FigSystemController with ClientLinkedSDK=%d clientPID=%d"
+ "-FigSystemControllerServer- %s: Finished no-reply  opCode '%c%c%c%c' object %p/%016llx"
+ "-FigSystemControllerServer- %s: Finished opCode '%c%c%c%c' object %p/%016llx"
+ "-FigSystemControllerServer- %s: Starting no-reply opCode '%c%c%c%c' object %p/%016llx"
+ "-FigSystemControllerServer- %s: Starting opCode '%c%c%c%c' object %p/%016llx"
+ "-FigSystemControllerServer- %s: Unknown no-reply opCode: '%c%c%c%c'"
+ "-FigSystemControllerServer- %s: Unknown opCode: '%c%c%c%c'"
+ "-FigVibrator-"
+ "-FigVibrator- %s: "
+ "-FigVibrator- %s: Could not connect to vibrator IOService."
+ "-FigVibrator- %s: Could not get a token for the notification status; NO VIBE NOTIFICATIONS!!"
+ "-FigVibrator- %s: Could not initialize vibe synth engine"
+ "-FigVibrator- %s: Somebody else initialized the info struct before us but it's OK."
+ "-FigVibrator- %s: VibeSynthEngineHasHardwareSupport() returned %s"
+ "-FigVibrator- %s: Vibrator is already initialized"
+ "-FigVibrator- %s: Vibrator is not initialized"
+ "-FigVibrator- %s: called"
+ "-FigVibrator- %s: called. No-op on IOKit vibrator"
+ "-FigVibrator- %s: calling vibeSynthEngineStartPrewarm"
+ "-FigVibrator- %s: calling vibeSynthEngineStopPrewarm"
+ "-FigVibrator- %s: dlsym of VibeSynthEngineHasHardwareSupport is valid"
+ "-FigVibrator- %s: fv_VibeSynthPlayVibrationWithPatternDictionary returned error"
+ "-FigVibrator- %s: gVibeSynthDylibHandle is NULL"
+ "-FigVibrator- %s: gvVibeSynthIsAvailable available"
+ "-FigVibrator- %s: gvVibeSynthIsAvailable not available"
+ "-FigVibrator- %s: posting %@"
+ "-FigVibrator- %s: scaleIntensity(%d) intensityScalar(%1.3f) VibrationData(%@)"
+ "-FigVibrator- %s: synchronizerToken(%p) loop(%s) stoppedContext(%@)"
+ "-FigVibrator_IOKit-"
+ "-FigVibrator_IOKit- %s: "
+ "-FigVibrator_IOKit- %s: Adjusted time values playDuration(%f) cycleTime(%f) onTime(%f)"
+ "-FigVibrator_IOKit- %s: Could not create a vibePatternArray."
+ "-FigVibrator_IOKit- %s: Could not create an intensity dictionary."
+ "-FigVibrator_IOKit- %s: Couldn't create payload dictionary for VibeStopped notification, but still send notification"
+ "-FigVibrator_IOKit- %s: Error converting time(%1.3fsec) to millisecond"
+ "-FigVibrator_IOKit- %s: Invalid cycleTime(%f) or onTime (%f sec) values."
+ "-FigVibrator_IOKit- %s: Queuing the vibration"
+ "-FigVibrator_IOKit- %s: Starting new vibration ***"
+ "-FigVibrator_IOKit- %s: Starting next vibration ***"
+ "-FigVibrator_IOKit- %s: Stopped current vibration"
+ "-FigVibrator_IOKit- %s: Updating queued vibration intensity from %f to %f"
+ "-FigVibrator_IOKit- %s: Vibration complete"
+ "-FigVibrator_IOKit- %s: Vibration could not be started"
+ "-FigVibrator_IOKit- %s: Vibrator is not initialized"
+ "-FigVibrator_IOKit- %s: intensity(%f) playDuration(%f) cycleTime(%f) onTime(%f)"
+ "-FigVibrator_IOKit- %s: intensity(%f) vibePattern(%@)"
+ "-FigVibrator_IOKit- %s: onTime %dms offTime %dms repeat %d"
+ "-FigVibrator_IOKit- %s: one vibration already queued up, dropping this one"
+ "-FigVibrator_IOKit- %s: posting VibeStopped"
+ "-FigVibrator_IOKit- %s: vibe pattern playDuration(%f)."
+ "-FigVibrator_VS-"
+ "-FigVibrator_VS- %s: Couldn't create payload dictionary for VibeStopped notification, but still send notification"
+ "-FigVibrator_VS- %s: No patterns playing on the vibe synth engine; notify others that vibing has stopped."
+ "-FigVibrator_VS- %s: Starting new vibration ***"
+ "-FigVibrator_VS- %s: Vibe currently playing; this one will be dropped."
+ "-FigVibrator_VS- %s: VibeSynthEnginePlay failed"
+ "-FigVibrator_VS- %s: Vibration stopped playing that has stoppedContext: %@"
+ "-FigVibrator_VS- %s: Vibrator is not initialized"
+ "-FigVibrator_VS- %s: intensity(%f) vibePattern(%@)"
+ "-FigVibrator_VS- %s: posting VibeStopped"
+ "-FigVolumeController- %s: ***** Reached finalize of singleton object = %p! File a bug for component 'CoreMedia Routing'. *****"
+ "-FigVolumeController- %s: Adding volumeNotificationListeners for endpoint = %@"
+ "-FigVolumeController- %s: FigVolumeController currently does not support routingContextUUID=%@, routingContextType=%@"
+ "-FigVolumeController- %s: Mute called for endppointID=%{public}@; however, endpoint is currently not picked! Mute is not set!"
+ "-FigVolumeController- %s: Posting %@ with payload = %@"
+ "-FigVolumeController- %s: Removing volume notification listeners for endpoint = %@"
+ "-FigVolumeController- %s: The Sub-Endpoint ID is Null!"
+ "-FigVolumeController- %s: Unable to find RoutingContextUUID for endpoint=%{public}@. Volume is not set!"
+ "-FigVolumeController- %s: Value for inVolume %f is out of range"
+ "-FigVolumeController- %s: Volume %.3f called for endpointName=%{public}@; however, endpoint is currently not picked! Volume is not set!"
+ "-FigVolumeController- %s: endpoint is NULL, unable to find maxSubEndpointVolume"
+ "-FigVolumeController- %s: endpoint is Null"
+ "-FigVolumeController- %s: endpoint is not a FigEndpoint"
+ "-FigVolumeController- %s: endpointName = %@, endpointID = %@, outSupportsVolumeControl = %s"
+ "-FigVolumeController- %s: endpointName = %@, endpointID = %@, outVolume = %f"
+ "-FigVolumeController- %s: get endpointVolume = %.3f for endpointName=%@"
+ "-FigVolumeController- %s: get mainVolume = %@"
+ "-FigVolumeController- %s: inEndpoint %p or inEndpointID %p is NULL"
+ "-FigVolumeController- %s: inEndpoint %p or outVolume %p is NULL"
+ "-FigVolumeController- %s: inEndpoint is NULL"
+ "-FigVolumeController- %s: inRoutingContext %p is NULL or outSupportsVolumeOperations %p is NULL"
+ "-FigVolumeController- %s: inRoutingContext %p or outMainVolumeControlSupported %p is NULL"
+ "-FigVolumeController- %s: inRoutingContext %p or outMainVolumeControlType %p is NULL"
+ "-FigVolumeController- %s: inRoutingContext is NULL"
+ "-FigVolumeController- %s: inRoutingContextUUID %@ is NULL"
+ "-FigVolumeController- %s: inRoutingContextUUID %@ is NULL or value for inVolume %f is out of range"
+ "-FigVolumeController- %s: inRoutingContextUUID %@ or outMainVolume %p is NULL"
+ "-FigVolumeController- %s: inRoutingContextUUID is NULL"
+ "-FigVolumeController- %s: inSubEndpoint is NULL"
+ "-FigVolumeController- %s: outVolumeController = %p, err = %d"
+ "-FigVolumeController- %s: outVolumeController is NULL"
+ "-FigVolumeController- %s: payload is not a CFDictionary"
+ "-FigVolumeController- %s: routingContext = %@, mainVolumeControlSupported = %s"
+ "-FigVolumeController- %s: routingContext = %@, mainVolumeControlType = %s"
+ "-FigVolumeController- %s: routingContext = %@, outVolume = %f"
+ "-FigVolumeController- %s: routingContext = %@, supportsVolumeOperations = %s"
+ "-FigVolumeController- %s: routingContextUUID %@ is NULL"
+ "-FigVolumeController- %s: set endpointVolume = %@ for endpointName=%@"
+ "-FigVolumeController- %s: set mainVolume = %@"
+ "-FigVolumeController- %s: subEndpointID %{public}@ is not part of PSG Cluster"
+ "-FigVolumeController- %s: supportsVolumeController = true because all endpoints are bluetooth shareable"
+ "-FigVolumeController- %s: supportsVolumeController = true because endpoint is AirPlay aggregate and routing context supports volume controller"
+ "-FigVolumeController- %s: volumeController = %p"
+ "-FigVolumeControllerServer-"
+ "-FigVolumeControllerServer- %s: Handle opCode '%c%c%c%c'"
+ "-FigVolumeControllerServer- %s: Invalid clientPID, Unable to get client name!"
+ "-FigVolumeControllerServer- %s: Unknown opCode: 0x%0x ('%c%c%c%c')"
+ "-FigVolumeControllerServer- %s: volumeController = %p, canUseForRoutingContext = %s"
+ "-FigVolumeControllerServer- %s: volumeController = %p, endpointID = %@, canSetEndpointVolume = %s"
+ "-FigVolumeControllerServer- %s: volumeController = %p, endpointID = %@, endpointVolumeControlType = %d"
+ "-FigVolumeControllerServer- %s: volumeController = %p, endpointID = %@, outVolume = %f"
+ "-FigVolumeControllerServer- %s: volumeController = %p, endpointID = %@, subEndpointID = %@, endpointVolumeControlType = %d"
+ "-FigVolumeControllerServer- %s: volumeController = %p, endpointID = %@, subendpointID = %@ outVolume = %f"
+ "-FigVolumeControllerServer- %s: volumeController = %p, objectID = %llu"
+ "-FigVolumeControllerServer- %s: volumeController = %p, routingContext = %@, canSetMasterVolume = %s"
+ "-FigVolumeControllerServer- %s: volumeController = %p, routingContext = %@, masterVolumeControlType = %d"
+ "-FigVolumeControllerServer- %s: volumeController = %p, routingContext = %@, outVolume = %f"
+ "-HDMILatencyManager- %s: Failed to read measuredHDMILatency because required keys are missing %@"
+ "-HDMILatencyManager- %s: Failed to update measuredHDMILatency because required keys are missing %@"
+ "-HDMILatencyManager- %s: Read Measured HDMI latency values from disk: '%@'"
+ "-HDMILatencyManager- %s: Read back value : %f"
+ "-HDMILatencyManager- %s: Sending MEASURED_HDMI_LATENCY_CHANGED notification."
+ "-MXAdditiveRoutingManager- %s: Active audio sessions info: %@."
+ "-MXAdditiveRoutingManager- %s: Current active sessions info: %@, previous active sessions info: %@"
+ "-MXAdditiveRoutingManager- %s: Iterating over activeDeviceInfo: %{public}@."
+ "-MXAdditiveRoutingManager- %s: Redundant active sessions info change, currently: %@"
+ "-MXAdditiveRoutingManager- %s: Session not found for audio session ID %{public}@"
+ "-MXAdditiveRoutingManager- %s: Skipping sending active session info to VA IsAdditiveRoutingEnabled = %{BOOL}u"
+ "-MXAdditiveRoutingManager- %s: Updating detailed route description with deviceID %{public}@"
+ "-MXAdditiveRoutingManager- %s: previousVirtualAudioDeviceIDs = %{public}@ newVirtualAudioDeviceIDS = %{public}@"
+ "-MXAggregateEndpoint- %s: Called endpoint (%p) inPropertyKey %{public}@"
+ "-MXAggregateEndpoint- %s: Calling FigEndpointActivateWithCompletionCallback endpoint (%p)"
+ "-MXAggregateEndpoint- %s: Calling FigEndpointAggregateAddEndpoint endpoint (%p)"
+ "-MXAggregateEndpoint- %s: Calling FigEndpointAggregateRemoveEndpoint endpoint (%p)"
+ "-MXAggregateEndpoint- %s: Calling FigEndpointCopyProperty endpoint (%p) inPropertyKey %{public}@"
+ "-MXAggregateEndpoint- %s: Calling FigEndpointSendCommandWithCompletionCallback endpoint (%p)"
+ "-MXAggregateEndpoint- %s: Calling FigEndpointSendData endpoint (%p)"
+ "-MXAggregateEndpoint- %s: Calling FigEndpointSetDelegateRemoteControl endpoint (%p)"
+ "-MXAggregateEndpoint- %s: Calling FigEndpointSetDelegateRouting endpoint (%p)"
+ "-MXAggregateEndpoint- %s: Calling FigEndpointSetProperty endpoint (%p) inPropertyKey %{public}@"
+ "-MXAggregateEndpoint- %s: Received notification %{public}@"
+ "-MXAlarmEvents- %s: Received silent mode timer event"
+ "-MXAudioAccessoryServices- %s: \t\t %{private}@: '%{public}@',"
+ "-MXAudioAccessoryServices- %s: \t\t %{public}@: '%{public}@',"
+ "-MXAudioAccessoryServices- %s: \t ================================================== %{public}@ Debug Info =================================================="
+ "-MXAudioAccessoryServices- %s: \t ======================================================================================================================================="
+ "-MXAudioAccessoryServices- %s: \t mDevicesState = {"
+ "-MXAudioAccessoryServices- %s: \t mPortToDeviceAddressMapping = {"
+ "-MXAudioAccessoryServices- %s: \t }"
+ "-MXAudioAccessoryServices- %s: %@ is cached as '%@',"
+ "-MXAudioAccessoryServices- %s: %{private}@ is managed, action='%{public}s', reason='%{public}@'"
+ "-MXAudioAccessoryServices- %s: %{private}@ is unmanaged, action='%{public}s', reason='%{public}@'"
+ "-MXAudioAccessoryServices- %s: Audio routing change notification, managedPorts=%{public}@ unmanagedPorts=%{public}@"
+ "-MXAudioAccessoryServices- %s: BTAudioRoutingRequest failed with error:%{public}@"
+ "-MXAudioAccessoryServices- %s: BTAudioRoutingRequest[deviceAddress='%{private}@', appBundleID='%{private}@', audioScore='%d', flags='%{public}s', reason='%{public}@'] ended - Elapsed time=%llu milliseconds"
+ "-MXAudioAccessoryServices- %s: BTAudioRoutingRequest[deviceAddress='%{private}@', appBundleID='%{private}@', audioScore='%d', flags='%{public}s', reason='%{public}@'] started"
+ "-MXAudioAccessoryServices- %s: Clearing devices status cache"
+ "-MXAudioAccessoryServices- %s: Current route is not eligible for Tipi, skip routing to preferred route"
+ "-MXAudioAccessoryServices- %s: Disable predicted routing.."
+ "-MXAudioAccessoryServices- %s: Failed to copy PreemptivePortInfo, action='%{public}s', deviceAddress='%{private}@', reason='%{public}@', preemptivePortInfo=%{private}@"
+ "-MXAudioAccessoryServices- %s: Ignore port '%u' since it doesn't support multiple connections"
+ "-MXAudioAccessoryServices- %s: Missing required parameter!"
+ "-MXAudioAccessoryServices- %s: Missing required parameter, preemptivePortInfo=%p, deviceAddress=%p"
+ "-MXAudioAccessoryServices- %s: Not taking ownership, BTPort is not inEar"
+ "-MXAudioAccessoryServices- %s: Not taking ownership, current route is not built-in"
+ "-MXAudioAccessoryServices- %s: Not taking ownership, isBluetoothSharingSessionEnabled=%{BOOL}u isPredictedRoutingTimerActive=%{BOOL}u"
+ "-MXAudioAccessoryServices- %s: Port %u doesn't support multiple connections"
+ "-MXAudioAccessoryServices- %s: Port '%u' %{public}@ hijacked, action='%{public}s', reason='%{public}@'"
+ "-MXAudioAccessoryServices- %s: Port '%u' is unmanaged, AudioAccessory cannot decide if port can be hijacked!"
+ "-MXAudioAccessoryServices- %s: Removing disconnected device '%{private}@'"
+ "-MXAudioAccessoryServices- %s: Removing disconnected port '%u'"
+ "-MXAudioAccessoryServices- %s: Routing to preferred address %{public}@ with priority %d"
+ "-MXAudioAccessoryServices- %s: SmartRouting is not supported on this platform"
+ "-MXAudioAccessoryServices- %s: The current route is BT and inEar. Make the ports routable and request for ownership"
+ "-MXAudioAccessoryServices- %s: The predicted route will be reset"
+ "-MXAudioAccessoryServices- %s: audioaccessoryd died :("
+ "-MXAudioAccessoryServices- %s: deviceAddress='%{private}@', action='%{public}s' reason='%{public}@'"
+ "-MXAudioAccessoryServices- %s: deviceAddress='%{private}@', reason='%{public}@', preemptivePortInfo=%{private}@"
+ "-MXAudioAccessoryServices- %s: isManagedDeviceConnected=%{BOOL}u"
+ "-MXCoreSessionBase-"
+ "-MXCoreSessionBase- %s:  --------------- Assertion info --------------- "
+ "-MXCoreSessionBase- %s: Active client %{public}@ has lost on-demand VADs"
+ "-MXCoreSessionBase- %s: Active device info does not contain expected sessionID info"
+ "-MXCoreSessionBase- %s: AudioObjectAddPropertyListener(vaemSessionRoutingInfoChangeListener) failed with err = %d = '%{public}.4s'"
+ "-MXCoreSessionBase- %s: AudioObjectGetPropertyData( temp_kVirtualAudioSessionPropertyRoutingInformation ) failed with err = '%c%c%c%c'"
+ "-MXCoreSessionBase- %s: AudioObjectGetPropertyData(( temp_kVirtualAudioSessionPropertySessionID ) failed with err = '%c%c%c%c'"
+ "-MXCoreSessionBase- %s: AudioObjectRemovePropertyListener(temp_kVirtualAudioSessionPropertyRoutingInformation) failed with err = %d = '%{public}.4s'"
+ "-MXCoreSessionBase- %s: Available route control features are %{public}@, is echo-cancelled input available? = %{BOOL}u for session %{public}@ [%p] with %{public}@ category; willRouteToOnDemandVADOnActivation = %{BOOL}u."
+ "-MXCoreSessionBase- %s: CMSMVAUtility_AudioObjectSetPropertyData( temp_kVirtualAudioPlugInPropertyDeleteSession ) failed with err = '%c%c%c%c'"
+ "-MXCoreSessionBase- %s: Client %@, Redundant sessions info change, current session info: %@"
+ "-MXCoreSessionBase- %s: Client %{public}@ setting session info %{public}@"
+ "-MXCoreSessionBase- %s: Client %{public}@, processing session routing information %{public}@"
+ "-MXCoreSessionBase- %s: Client '%@' %@ recently activated"
+ "-MXCoreSessionBase- %s: Client '%@' hasInput=%{BOOL}u isSessionUsingBuiltInMic=%{BOOL}u"
+ "-MXCoreSessionBase- %s: Client '%@' is setting isActive to '%{BOOL}u'"
+ "-MXCoreSessionBase- %s: Client '%{public}@' changed isRecordingMuted to %{BOOL}u"
+ "-MXCoreSessionBase- %s: Client '%{public}@' failed to change isRecordingMuted to %{BOOL}u with error=%d"
+ "-MXCoreSessionBase- %s: Client doesn't have any entitlements"
+ "-MXCoreSessionBase- %s: Current sessions info: %@, previous sessions info: %@"
+ "-MXCoreSessionBase- %s: De-register audio object for session because client forgot to do so"
+ "-MXCoreSessionBase- %s: Destroying the reporter %lld for session %@."
+ "-MXCoreSessionBase- %s: Device info missing deviceID and deviceUID!"
+ "-MXCoreSessionBase- %s: Encountered error %d querying On-demand-VAD support for session %{public}@ [%p] with additive routing info: %{public}@."
+ "-MXCoreSessionBase- %s: Error setting temp_kVirtualAudioSessionPropertySessionConfiguration!"
+ "-MXCoreSessionBase- %s: Failed to create audio session ID with err = '%c%c%c%c'"
+ "-MXCoreSessionBase- %s: Insufficient information in virtualDeviceInfo = %{public}@, not amending audio behavior dictionary"
+ "-MXCoreSessionBase- %s: Invalid audio session id for client %{public}@ audioSessionID %u audioObjectID %u"
+ "-MXCoreSessionBase- %s: Invalid session audio object"
+ "-MXCoreSessionBase- %s: NOTICE: Active session %{public}@ [%p] has lost an on-demand VAD, call BeginInterruption again."
+ "-MXCoreSessionBase- %s: No audio session ID for '%@', skipping additive routing session info creation."
+ "-MXCoreSessionBase- %s: Notifying client %{public}@ of %{public}@ with payload = %{public}@"
+ "-MXCoreSessionBase- %s: Playback assertion %p explanation = %{public}@"
+ "-MXCoreSessionBase- %s: Releasing MXCoreSessionBase with ID = %@, clientPID = %@"
+ "-MXCoreSessionBase- %s: Resetting %{public}@."
+ "-MXCoreSessionBase- %s: Resetting default audio behavior for session %{public}@ who's VADs went away."
+ "-MXCoreSessionBase- %s: Session %{public}@ [%p] does not have additive routing info; willRouteToOnDemandVADOnActivation is FALSE."
+ "-MXCoreSessionBase- %s: Session %{public}@ is shadowing audioSessionID %u, but a matching core session could not be found."
+ "-MXCoreSessionBase- %s: Session to shadow %{public}@ for %{public}@ is inactive or lacks route control (active=%{BOOL}u, controlsRouting=%{BOOL}u)."
+ "-MXCoreSessionBase- %s: Setting %{public}@ to %{public}@ and %{public}@ to %{public}@ for session %{public}@."
+ "-MXCoreSessionBase- %s: Setting mute value to %{BOOL}u for client %{public}@"
+ "-MXCoreSessionBase- %s: Skipping sending active session configuration info to VA IsAdditiveRoutingEnabled = %{BOOL}u"
+ "-MXCoreSessionBase- %s: Success new audio session id = %d"
+ "-MXCoreSessionBase- %s: Temporary playback assertion %p explanation = %{public}@"
+ "-MXCoreSessionBase- %s: Unexpected audioSessionIDs count of %lu found"
+ "-MXCoreSessionBase- %s: Updating audio behavior from %{public}@ to %{public}@ for %{public}@."
+ "-MXCoreSessionBase- %s: Updating detailed route description deviceID %{public}@"
+ "-MXCoreSessionBase- %s: Will session %{public}@ [%p] with info %{public}@ route to an on-demand VAD? %{BOOL}u"
+ "-MXCoreSessionBase- %s: [%p] '%@' setting CoreSessionID to %d"
+ "-MXCoreSessionBase- %s: auditTokenData cannot be nil!"
+ "-MXCoreSessionBase- %s: cmsBeginInterruptionGuts returned err = %d, INTERRUPTING %{public}@ [%p]."
+ "-MXCoreSessionBase- %s: isRecordingWithBTManagedDevice:%d, isPortManaged:%d"
+ "-MXCoreSessionBase- %s: setting client name of [%p] to: '%@'"
+ "-MXCoreSessionIndependentAudioResource- %s: '%{public}@' with [%{public}@/%{public}@] going active"
+ "-MXCoreSessionIndependentAudioResource- %s: '%{public}@' with [%{public}@/%{public}@] going inactive"
+ "-MXCoreSessionIndependentAudioResource- %s: '%{public}@' with [%{public}@/%{public}@] is %{public}@ playing"
+ "-MXCoreSessionIndependentAudioResource- %s: Client '%{public}@' failed to %{public}s recording with error=%d"
+ "-MXCoreSessionIndependentAudioResource- %s: Client '%{public}@' with [%{public}@/%{public}@] has %{public}@ recording"
+ "-MXCoreSessionIndependentAudioResource- %s: Setting service type for Session %@ with reporterID %@"
+ "-MXCoreSessionIndependentInputAudioResource-"
+ "-MXCoreSessionIndependentInputAudioResource- %s: \t\t #####################################################################################################################################"
+ "-MXCoreSessionIndependentInputAudioResource- %s: \t\t }"
+ "-MXCoreSessionIndependentInputAudioResource- %s: Called for %p client %{public}@"
+ "-MXCoreSessionIndependentInputAudioResource- %s: Client %{public}@ [%p] changing %{public}@ to %{BOOL}u"
+ "-MXCoreSessionIndependentInputAudioResource- %s: Client %{public}@ [%p] setting %{public}@ to %{public}@; session is active = %{BOOL}u"
+ "-MXCoreSessionIndependentInputAudioResource- %s: Client %{public}@ updating ReporterIDs to %{public}@"
+ "-MXCoreSessionIndependentInputAudioResource- %s: Client doesn't have the entitlement to create MXCoreSessionIndependentInputAudioResource!"
+ "-MXCoreSessionIndependentInputAudioResource- %s: Creation options dictionary cannot be nil!"
+ "-MXCoreSessionIndependentInputAudioResource- %s: Failed to copy '%{public}@' property with err=%d"
+ "-MXCoreSessionIndependentInputAudioResource- %s: Failed to set '%{public}@' property with err=%d"
+ "-MXCoreSessionIndependentInputAudioResource- %s: Number of MXSessionIndependentInputAudioResource: %lu"
+ "-MXCoreSessionIndependentInputAudioResource- %s: Number of MXSessions: %lu"
+ "-MXCoreSessionIndependentInputAudioResource- %s: Session %{public}@ setting property = %{public}@, value = %{public}@"
+ "-MXCoreSessionIndependentInputAudioResource- %s: Session '%{public}@' setting %{public}@ to %{BOOL}u"
+ "-MXCoreSessionIndependentInputAudioResource- %s: Session '%{public}@' setting PrefersSuppressingRecordingState value to '%{BOOL}u'"
+ "-MXCoreSessionIndependentInputAudioResource- %s: Skipping sending active session configuration info to VA for client %@ as it will not route to onDemand VAD"
+ "-MXCoreSessionIndependentInputAudioResource- %s: Skipping sending session configuration to VA for client %{public}@"
+ "-MXCoreSessionSecureCommon-"
+ "-MXCoreSessionSecureCommon- %s: Number of MXSessionSecure: %lu"
+ "-MXCoreSessionSecureCommon- %s: Number of MXSessions: %lu"
+ "-MXCoreSessionSecureCommon- %s: Skipping sending active session configuration info to VA for client %@ as it will not route to onDemand VAD"
+ "-MXCoreSessionSecureCommon- %s: Skipping sending session configuration to VA for client %{public}@"
+ "-MXCoreSessionSidekick-"
+ "-MXCoreSessionSidekick- %s: Category %@ %@ for session %@"
+ "-MXCoreSessionSidekick- %s: Mode %@ %@ for category %@"
+ "-MXCoreSessionSidekick- %s: Session client '%@' resetting InterruptionFadeDuration"
+ "-MXCoreSessionSidekick- %s: Setting service type for Session %@ with reporterID %@"
+ "-MXCoreSessionUtilities- %s: Default preferred route is also not available, route to the system preferred microphone"
+ "-MXCoreSessionUtilities- %s: Found preferred portUID='%{public}@' with portID='%{public}@' for session '%{public}@'"
+ "-MXCoreSessionUtilities- %s: Get the default preferred route since either there is no entry in the cache for %{public}@ or there is no corresponding connected input port"
+ "-MXCoreSessionUtilities- %s: Get the user preferred route and connected input port for %{public}@"
+ "-MXCoreSessionUtilities- %s: Port %u for session %{public}@ is Smart-Routing capable, allowing SR to proceed normally and returning nil."
+ "-MXCoreSessionUtilities- %s: User preferred input port %u for %{public}@ is Bluetooth microphone, isWirelessConnection=%{BOOL}u, isPortManaged=%{BOOL}u"
+ "-MXCoreSession_Embedded- %s: '%@' setting interruptionStyle: %s"
+ "-MXCoreSession_Embedded- %s: Changing deprecated StopEveryoneAllowingResumption to %s"
+ "-MXCoreSession_Embedded- %s: Deallocating MXCoreSession [%p]"
+ "-MXCoreSession_Embedded- %s: DidDuck -> WillNotDuck, call unduck."
+ "-MXCoreSession_Embedded- %s: DidNotDuck -> WillDuck, call duck."
+ "-MXCoreSession_Embedded- %s: Initializing MXCoreSession [%p]"
+ "-MXCoreSession_Embedded- %s: Invalid interruptionStyle: %ld\n"
+ "-MXCoreSession_Embedded- %s: Number of MXSessions: %lu"
+ "-MXCoreSession_Embedded- %s: Reapplying sample rate and buffer size directly on VAD as output sample rate is not set by client %{public}@"
+ "-MXCoreSession_Embedded- %s: Session %{public}@ audioTrackStatus = %{public}@"
+ "-MXCoreSession_Embedded- %s: Session '%@' setting pidToInheritAppStateFrom to %d, and initial appState to %@"
+ "-MXCoreSession_Embedded- %s: Skipping sending active session configuration info to VA for client %@ as it will not route to onDemand VAD"
+ "-MXCoreSession_Embedded- %s: Skipping sending session configuration to VA for client %{public}@"
+ "-MXCoreSession_Embedded- %s: Stopping assertion audit timer for client %{public}@"
+ "-MXCoreSession_Embedded- %s: mixing -> non-mixing: calling BeginInterruption"
+ "-MXDebugUtilities- %s: \n\n\n\n\nNext Session:"
+ "-MXDebugUtilities- %s: !!!!!!!!!!!!!!!!!!!!!!!!!!! SmartRouting is not supported on this platform !!!!!!!!!!!!!!!!!!!!!!!!!!!"
+ "-MXDebugUtilities- %s: --------------------------%{public}@, End Session Dump --------------------------"
+ "-MXDebugUtilities- %s: Cannot open /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox"
+ "-MXDebugUtilities- %s: Dump file is not available"
+ "-MXDebugUtilities- %s: KEY: %{public}@\t\t VALUE: %{public}@"
+ "-MXEndpointDescriptorCache- %s:  MXEndpointDescriptorCleanupBannersIfNeeded for routeuid = %{public}@, routeName = %{public}@"
+ "-MXEndpointDescriptorCache- %s: Endpoint added: %{public}@, %{public}@"
+ "-MXEndpointDescriptorCache- %s: Endpoint removed: %{public}@, %{public}@"
+ "-MXExclaves- %s: Session '%{public}@' not updating sensor status, isUsingExclaveSensor=%{BOOL}u requiresExclaveSensor=%{BOOL}u"
+ "-MXInitialzation_Common-"
+ "-MXInitialzation_Common- %s: AirPlayStartServicesInMXProcess is NULL"
+ "-MXInitialzation_Common- %s: Did not find AirPlaySender bundle '%{public}s': %{public}s\n"
+ "-MXInitialzation_Common- %s: MediaExperience framework is fully initialized now, blocked for %llu ms"
+ "-MXInitialzation_Embedded-"
+ "-MXNowPlayingAppManager- %s: Canceling write NowPlaying app to disk timer."
+ "-MXNowPlayingAppManager- %s: PID %d CANNOT be the now playing app because canBeNowPlayingApp = %d, and allowedToBeNowPlayingApp = %d"
+ "-MXNowPlayingAppManager- %s: PID %d is now the new playing app because canBeNowPlayingApp = %d, and allowedToBeNowPlayingApp = %d"
+ "-MXNowPlayingAppManager- %s: Starting writeNowPlayingAppToDisk timer."
+ "-MXRoutingContextCallbackHelper- %s: Called (%p)"
+ "-MXRoutingContextCallbackHelper- %s: Calling client back with reason %{public}@. Time taken %llu ms."
+ "-MXRoutingContextReportingServiceImpl- %s: Called. Backends: %{public}@"
+ "-MXRoutingContextReportingServiceImpl- %s: Called. RTCReporting: %{public}@"
+ "-MXRoutingContextReportingServiceImpl- %s: Message: %{public}@. Error: %{public}@."
+ "-MXRoutingManager_AudioContext- %s: FigEndpointAggregateAddEndpoint returned err=%d for ID=%{private}@, name=%{public}@"
+ "-MXRoutingManager_AudioContext- %s: endpoint to deactivate is NULL"
+ "-MXRoutingManager_AudioContext- %s: endpointName = %{public}@, inActivationSeed=%llu, err = %d, inFeatures=%d, routingContextUUID=%{public}@ routingContextType=%{public}@, correlationID=%{public}@. Time taken to addEndpoint: %f ms. Time taken to run callback %f ms. Total round trip time: %f ms."
+ "-MXRoutingManager_AudioContext- %s: endpointName = %{public}@, inActivationSeed=%llu, err = %d, inFeatures=%d, routingContextUUID=%{public}@, routingContextType=%{public}@, correlationID=%{public}@. Time taken to removeEndpoint: %f ms. Time taken to run callback %f ms. Total round trip time: %f ms."
+ "-MXRoutingManager_AudioContext- %s: inCommChannelUUID is NULL"
+ "-MXRoutingManager_AudioContext- %s: inData is NULL"
+ "-MXRoutingManager_AudioContext- %s: inEndpoint is NULL"
+ "-MXRoutingManager_AudioContext- %s: inFailureInfo is NULL"
+ "-MXRoutingManager_AudioContext- %s: inSubEndpoint is NULL! This should not happen because audio context currently only supports WHA"
+ "-MXRoutingManager_AudioContext- %s: mxAudioContext_handleDidReceiveDataFromCommChannelDelegate for commChannelUUID=%{public}@"
+ "-MXRoutingManager_AudioContext- %s: mxAudioContext_removeEndpointFromAggregate returned err=%d for ID=%{private}@, name=%{public}@"
+ "-MXSession-"
+ "-MXSession- %s: \t IsPlayerMuted = %{BOOL}u, AudioEnabledStatus = %{public}@"
+ "-MXSession- %s: <%{public}@: %p, CoreSessionID = %lld, CoreSession = %{public}@, IsMuted = %{ppublic}@, ClientIsPlaying = %{public}@, AudioToolboxIsPlaying = %{public}@, MXSessionID = %llx, OutputChannels = %u, OutputSampleRate = %f, AudioFormat = %{public}@, MutePriority = %{public}@, IAmPiP = %{public}@, DoesntActuallyPlayAudio = %{public}@, ClientType = %{public}@, IsPlayingOutput = %{BOOL}u, IsPlayingVideoOutput = %{BOOL}u \n Spatial Settings:: sourceFormatInfo: %{public}@"
+ "-MXSession- %s: Calling BeginInterruption because MXSession(%llx) of type %{public}@ isPlaying and expanded to full screen with another app playing."
+ "-MXSession- %s: Copying %@ on MXSession with ID(%llx)/CoreSessionID (%@) --> with value %.3f."
+ "-MXSession- %s: Copying %@ on MXSession with ID(%llx)/CoreSessionID (%@) --> with value %@."
+ "-MXSession- %s: Copying %@ on MXSession with ID(%llx)/CoreSessionID (%@) --> with value %d."
+ "-MXSession- %s: Copying %@ on MXSession with ID(%llx)/CoreSessionID (%@) --> with value %llx."
+ "-MXSession- %s: Core session %{public}@ hasAudioTrack = %{BOOL}u"
+ "-MXSession- %s: Deallocating the MXSession(%llx) belonging to CoreSession %@"
+ "-MXSession- %s: MXSession is nil. Cannot post IsMutedDidChangeNotification.."
+ "-MXSession- %s: MXSession with ID %llx for CoreSession (%@), Copying IsMuted with value %@"
+ "-MXSession- %s: MXSession with ID %llx for CoreSession(%@), Copying AudioTrackStatus with value %@"
+ "-MXSession- %s: MXSession with ID %llx for CoreSession(%@), Copying DoesntActuallyPlayAudio with value %@"
+ "-MXSession- %s: MXSession with ID %llx for CoreSession(%@), Copying IsPlayerMuted with value %@"
+ "-MXSession- %s: MXSession(%llx) of type %{public}@ for CoreSession %{public}@ setting AudioTrackStatus = %{public}@"
+ "-MXSession- %s: MXSession(%llx) of type %{public}@ for CoreSession %{public}@ setting IsPlayerMuted = %{public}@"
+ "-MXSession- %s: MXSession(%llx) of type %{public}@ for CoreSession %{public}@ setting IsPlayingVideoOutput = %{public}@"
+ "-MXSession- %s: Posting kMXSessionNotification_IsMutedDidChange to MXSession(%llx) of type %@ of %@ to %s"
+ "-MXSession- %s: Re-arbitrating properties on MXCoreSession."
+ "-MXSession- %s: Redundant isPlaying change for MXSession belonging to CoreSession(%@)."
+ "-MXSession- %s: Redundant isRecording change for MXSession belonging to CoreSession(%@)."
+ "-MXSession- %s: Refreshing the CoreSession (%@) as one of the MXSession's is being dealloc'd."
+ "-MXSession- %s: Trying to set outputChannels on Session with AC3 or MATATMOS format. Does not apply."
+ "-MXSession- %s: Updated PreferredAudioHardwareFormat value to %@ for MXSession(%llx) of type %@ belonging to CoreSession(%@)."
+ "-MXSession- %s: Updated PreferredNumberOfOutputChannels value to %d for MXSession(%llx) of type %@ belonging to CoreSession(%@)."
+ "-MXSession- %s: Updated PreferredOutputSampleRate value to %.3f for MXSession(%llx) of type %@ belonging to CoreSession(%@)."
+ "-MXSession- %s: Updating MutePriority"
+ "-MXSessionBase-"
+ "-MXSessionIndependentAudioResource- %s: \t\t\t\t ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ %{public}@ {ID: %{public}@} ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
+ "-MXSessionIndependentAudioResource- %s: \t\t\t\t ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
+ "-MXSessionIndependentAudioResource- %s: \t\t\t\t {"
+ "-MXSessionIndependentAudioResource- %s: \t\t\t\t }"
+ "-MXSessionIndependentInputAudioResource-"
+ "-MXSessionIndependentInputAudioResource- %s: \t\t\t\t ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ %{public}@ {ID: %{public}@ isPlaying: %{BOOL}u audioToolboxIsPlaying: %{BOOL}u clientIsPlaying: %{BOOL}u isRecording: %{BOOL}u } ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
+ "-MXSessionIndependentInputAudioResource- %s: \t\t\t\t ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
+ "-MXSessionIndependentInputAudioResource- %s: \t\t\t\t {"
+ "-MXSessionIndependentInputAudioResource- %s: \t\t\t\t }"
+ "-MXSessionIndependentInputAudioResource- %s: Creation options dictionary cannot be nil!"
+ "-MXSessionIndependentInputAudioResource- %s: Failed to create parent CoreSession"
+ "-MXSessionIndependentInputAudioResource- %s: Passthrough property %@ to MXCoreSessionIndependentInputAudioResource"
+ "-MXSessionManager- %s: *** Only posting %f to AVSystemControllers; volume didn't actually change ***"
+ "-MXSessionManager- %s: *** Posting %f to volume button clients and AVSystemControllers; volume actually did change for category %@ ***"
+ "-MXSessionManager- %s: Active audio sessions info: %@."
+ "-MXSessionManager- %s: Cached '%@' sample rate has been updated to %@"
+ "-MXSessionManager- %s: ControlsVolume: calling cmsUpdatePlaybackVolume(%p: %@)"
+ "-MXSessionManager- %s: Could not find defaultMusicApp in %{public}@, using default value."
+ "-MXSessionManager- %s: Could not load %{public}@"
+ "-MXSessionManager- %s: Found active volume client '%{public}@', volumeButtonClientIsMuted = %{BOOL}u"
+ "-MXSessionManager- %s: Found outputMuted session '%{public}@'"
+ "-MXSessionManager- %s: No change in nero mirroring status. Nero mirroring is already %s"
+ "-MXSessionManager- %s: Number of MXCoreSessions: %lu"
+ "-MXSessionManager- %s: Number of Nero MXCoreSessions: %lu"
+ "-MXSessionManager- %s: Ringer switch changed to : %s"
+ "-MXSessionManager- %s: There is currently no phone call session - nothing to do"
+ "-MXSessionManager- %s: Unmuting short-form session %{public}@"
+ "-MXSessionManager- %s: VoiceOver was controlling volume, calling cmsUpdatePlaybackVolume(%p: %@)"
+ "-MXSessionManager- %s: calling cmsUpdatePlaybackVolume(%p: %@) as this session is not playing to default VAD but is active"
+ "-MXSessionManager- %s: session = '%@' [%p], audioCategory = %@, audioMode = %@"
+ "-MXSessionManager- %s: starkPortWasMadeRoutable = %s"
+ "-MXSessionManagerBase- %s: AudioSessionID %d or ShadowingOptions %{public}@ not provided"
+ "-MXSessionManagerBase- %s: gCMSM.audioToolboxRoutines.pAudioToolboxServerHandleInterruptionWithAudioSessionID is NULL for an audio session"
+ "-MXSessionManagerDuckingUtilities- %s: '%@' already unDucked."
+ "-MXSessionManagerDuckingUtilities- %s: '%@' is already ducked"
+ "-MXSessionManagerDuckingUtilities- %s: Adding to duckingSourceList: %u, %u"
+ "-MXSessionManagerDuckingUtilities- %s: Applying OutputMute for session '%{public}@'"
+ "-MXSessionManagerDuckingUtilities- %s: Could not find any duckingSource entry to be removed. This should never happen!"
+ "-MXSessionManagerDuckingUtilities- %s: Ducker and Duckee on the same VAD=%@"
+ "-MXSessionManagerDuckingUtilities- %s: DuckerSession does not exist. Not updating duck volume."
+ "-MXSessionManagerDuckingUtilities- %s: Entry : %u / %u"
+ "-MXSessionManagerDuckingUtilities- %s: Finished sleep %1.3f s for async %{public}s"
+ "-MXSessionManagerDuckingUtilities- %s: NULL duckerSession passed in for session duckerSession. This should never happen!"
+ "-MXSessionManagerDuckingUtilities- %s: Not ducking %{public}@ for VoiceOver."
+ "-MXSessionManagerDuckingUtilities- %s: Not ducking %{public}@ with category/mode %{public}@/%{public}@ for VoiceOver %{public}@"
+ "-MXSessionManagerDuckingUtilities- %s: Not unducking %@ because: %d"
+ "-MXSessionManagerDuckingUtilities- %s: Output muting for input-only session '%{public}@', skipping"
+ "-MXSessionManagerDuckingUtilities- %s: Output un-muting for input-only session '%{public}@', skipping"
+ "-MXSessionManagerDuckingUtilities- %s: Removing all duckers from the list for session %@"
+ "-MXSessionManagerDuckingUtilities- %s: Removing entry for %u / %u. DuckedSession %@"
+ "-MXSessionManagerDuckingUtilities- %s: Returning as Speaker Volume Limit is not enabled"
+ "-MXSessionManagerDuckingUtilities- %s: Returning as current route is not built in speaker."
+ "-MXSessionManagerDuckingUtilities- %s: Returning as session's mapped category is not Audio/Video."
+ "-MXSessionManagerDuckingUtilities- %s: Returning as this is a shareplay session"
+ "-MXSessionManagerDuckingUtilities- %s: Session '%@' is ducked by duckingSource '%@': duckingSourceType %u, duckingSource ID %lld"
+ "-MXSessionManagerDuckingUtilities- %s: Skipping duck because %{public}@ is outputMuted"
+ "-MXSessionManagerDuckingUtilities- %s: There already exists an entry for %u and %u. Ducker session (%@). Not adding a new one."
+ "-MXSessionManagerDuckingUtilities- %s: There already exists an entry for '%{public}@' ducking source. Not adding a new one."
+ "-MXSessionManagerDuckingUtilities- %s: Un-Applying OutputMute for session '%{public}@'"
+ "-MXSessionManagerDuckingUtilities- %s: Updating duck volume to %.4f"
+ "-MXSessionManagerDuckingUtilities- %s: [%p] '%@' ducking by %1.3f in %1.3f sec"
+ "-MXSessionManagerDuckingUtilities- %s: [%p] '%@' unducking"
+ "-MXSessionManagerDuckingUtilities- %s: sessionToDuck: '%@'; duckerSession: '%@'; duckingSourceType: %u; duckingSourceID: %lld"
+ "-MXSessionManagerDuckingUtilities- %s: sessionToUnduck: '%@'; sessionCausingUnduck: '%@'; duckingSourceType: %u; duckingSourceID:%lld "
+ "-MXSessionManagerIndependentAudioResource- %s: \t ================================================== %{public}@ Debug Info =================================================="
+ "-MXSessionManagerIndependentAudioResource- %s: \t ======================================================================================================================================="
+ "-MXSessionManagerIndependentAudioResource- %s: \t MXCoreSessionIndependentInputAudioResource sessions count = %lu"
+ "-MXSessionManagerIndependentAudioResource- %s: '%{public}@' with [%{public}@/%{public}@] going inactive"
+ "-MXSessionManagerIndependentAudioResource- %s: Interrupting all sessions shadowing %{public}@ for %{public}@."
+ "-MXSessionManagerIndependentAudioResource- %s: Interruptor: %{public}@ INTERRUPTING victim: %{public}@ with audioCategory %{public}@"
+ "-MXSessionManagerIndependentAudioResource- %s: No session provided!"
+ "-MXSessionManagerIndependentAudioResource- %s: Number of MXCoreSessionIndependentInputAudioResource: %lu"
+ "-MXSessionManagerIndependentAudioResource- %s: Resuming all independent input audio resource sessions because of %{public}@"
+ "-MXSessionManagerIndependentAudioResource- %s: Sending %{public}@ end-interruption to all sessions shadowing %{public}@ for %{public}@."
+ "-MXSessionManagerIndependentAudioResource- %s: Sending endInterruption with status %{public}@ to session: %{public}@ with audioCategory %{public}@"
+ "-MXSessionManagerIndependentAudioResource- %s: Unable to post interruption command for audio session"
+ "-MXSessionManagerInterruptionActionMapper- %s: Could not load InterruptionPriorityForTipi.plist"
+ "-MXSessionManagerInterruptionActionMapper- %s: Could not load InterruptionPriorityForTriangle.plist"
+ "-MXSessionManagerInterruptionActionMapper- %s: Session %{public}@ has preference for input device that particpates in Smart Routing, upgrading priority to 200 to hijack from idle."
+ "-MXSessionManagerInterruptionActionMapper- %s: Session %{public}@ has set client priority to PhoneCall. Upgrading sessionPriority to kMXCoreSessionPriority_Critical501"
+ "-MXSessionManagerInterruptionActionMapper- %s: Session %{public}@ is recording to Smart Routing capable BT device and prefersNoInterruptionsByRingtonesAndAlerts. Upgrading sessionPriority to kMXCoreSessionPriority_Critical501 to prevent hijack"
+ "-MXSessionManagerInterruptionActionMapper- %s: playingInfo.displayID=%@, playingInfo.audioCategory=%@, playingInfo.audioMode=%@, priority=%d"
+ "-MXSessionManagerSecure- %s: Active secure audio sessions info: %@."
+ "-MXSessionManagerSecure- %s: Number of MXCoreSessionSecure: %lu"
+ "-MXSessionManagerSecure- %s: Number of MXCoreSessions: %lu"
+ "-MXSessionManagerSidekick- %s: Called for MXCoreSessionSidekick: %@ belonging to remoteDeviceID: %@"
+ "-MXSessionManagerSidekick- %s: Called for MXCoreSessionSidekick: %@ belonging to remoteDeviceID: %@, numberOfMXCoreSessionSidekickForRemoteDeviceID %lu"
+ "-MXSessionManagerSidekick- %s: Initializing MXSessionManagerSidekick"
+ "-MXSessionManagerSidekick- %s: Removing remoteDeviceID %@ from the MapTable."
+ "-MXSessionManagerSidekick- %s: remoteDeviceIDToCoreSessionIDList %@"
+ "-MXSessionManagerUtilities- %s: CurrentPort is unknown. Error! We should never come here!"
+ "-MXSessionManagerUtilities- %s: CurrentPorts count = 0. Expected when ringer is silent"
+ "-MXSessionManagerUtilities- %s: INTERRUPTING client '%{public}@' as it shadows '%{public}@' for %{public}@"
+ "-MXSessionManagerUtilities- %s: Interruptor '%{public}@' and victim '%{public}@' can coexist because at least one of them has no audio track"
+ "-MXSessionManagerUtilities- %s: Interruptor '%{public}@' and victim '%{public}@' can coexist because both are media sessions and multitasking is enabled"
+ "-MXSessionManagerUtilities- %s: Interruptor '%{public}@' and victim '%{public}@' can coexist because one is a muted short-form video session"
+ "-MXSessionManagerUtilities- %s: Invalidating un-accounted assertions if needed for session id 0x%x(%u) client %{public}@ for reason %{public}@"
+ "-MXSessionManagerUtilities- %s: No vadOutputPortType"
+ "-MXSessionManagerUtilities- %s: PID %d allowedToBeNowPlayingApp = %{BOOL}u countOfSessionsEligibleToBeNowPlayingApp %d"
+ "-MXSessionManagerUtilities- %s: Setting waitingToResume to NO for session '%@' interrupted by session '%@'"
+ "-MXSessionManagerUtilities- %s: Some long form video client %{public}s active."
+ "-MXSessionManagerUtilities- %s: Synchronizing Voice Assistant volume %f to closely follow media volume %f on personal audio device %{public}@~%{public}@~%{public}@"
+ "-MXSessionManagerUtilities- %s: Synchronizing alarm session volume %f to closely follow media volume %f on broadcast route to personal audio device %{public}@~%{public}@~%{public}@"
+ "-MXSessionManagerUtilities- %s: Voice Assistant session going active over media session on personal audio device %{public}@~%{public}@~%{public}@, mostRecentSynchronizedVolumeActivityTimestamp = %llu, currentTimstamp = %llu, duration = %llu"
+ "-MXSessionManagerUtilities- %s: VoiceOver is playing over BT LE; Using special audioBehavior dictionary"
+ "-MXSessionManagerUtilities- %s: category = %@, defaultBuiltInRoute = %@, newCategory = %@"
+ "-MXSessionManagerUtilities- %s: category = %@, newCategory = %@"
+ "-MXSessionManagerUtilities- %s: isSessionAllowedToStartRecordingTemporarily=%{BOOL}u for '%@'"
+ "-MXSessionManagerUtilities- %s: port = %u does NOT support InEarDetection"
+ "-MXSessionManagerUtilities- %s: port = %u is NOT of type headphones"
+ "-MXSessionManagerUtilities- %s: shouldAllowBluetoothAccessoryToRequestAudioRoute = NO"
+ "-MXSessionManagerUtilities_Desktop- %s: category = %@, enableBluetooth = %s, newCategory = %@"
+ "-MXSessionManagerVAUtilities- %s: QuiesceableWiredPortsConnection feature is disabled"
+ "-MXSessionSecureCommon-"
+ "-MXSessionSidekick-"
+ "-MXSessionSidekick- %s: Copying %@ on MXSessionSidekick with ID(%llx)/CoreSessionID (%@) --> with value %@."
+ "-MXSessionSidekick- %s: Copying %@ on MXSessionSidekick with ID(%llx)/CoreSessionID (%@) --> with value %llx."
+ "-MXSessionSidekick- %s: Deallocating the MXSessionSidekick(%llx) belonging to MXCoreSessionSidekick %@"
+ "-MXSessionSidekick- %s: Passthrough property %@ to MXCoreSessionSidekick"
+ "-MXSessionSidekick- %s: Re-arbitrating properties on MXCoreSessionSidekick"
+ "-MXSessionSidekick- %s: Redundant isPlaying change for MXSessionSidekick belonging to MXCoreSessionSidekick(%@)."
+ "-MXSessionSidekick- %s: Refreshing the MXCoreSessionSidekick (%@) as one of the MXSessionSidekick is being deallocated"
+ "-MXSessionSidekick- %s: Removing CoreSessionID = %lld from the MapTable."
+ "-MXSessionSidekick- %s: Setting ClientType to %@ for MXSessionSidekick with ID = %llx"
+ "-MXSessionSidekick- %s: Setting IsPlaying to %d for MXSessionSidekick with ID = %llx"
+ "-MXSessionSidekick- %s: Updated IsPlaying value for MXSessionSidekick(%llx) to %@ belonging to MXCoreSessionSidekick(%@)."
+ "-MXSessionSidekick- %s: coreSessionIDToMXSessionList %@"
+ "-MXSession_CInterfaceCommon-"
+ "-MXSession_CInterfaceCommon- %s: Failed to create MXSessionIndependentInputAudioResource"
+ "-MXSession_CInterfaceCommon- %s: It's a CMSesssion"
+ "-MXSession_CInterfaceCommon- %s: It's a Sidekick CoreSession"
+ "-MXSession_CInterfaceCommon- %s: Preparing session for activation before dispatching to the ACQ failed with error='%d'"
+ "-MXSystemAudio_Embedded- %s: Endpoint can't be NULL for audio or system audio context"
+ "-MXSystemController-"
+ "-MXSystemController- %s: '%@' '%s' allowed to initiate Playback"
+ "-MXSystemController- %s: Category:%@, Mode = %@, operation = %d, volumeToApply = %1.3f"
+ "-MXSystemController- %s: Category:%@, Mode = %@, operation = %d, volumeToApply = %1.3f rampUpDuration %1.3f rampDownDuration %1.3f"
+ "-MXSystemController- %s: Category:%@, Mode = %@, operation = %d, volumeToApply = %1.3f rampUpDuration %1.3f rampDownDuration %1.3f retainFullMute = %d"
+ "-MXSystemController- %s: Checking mHasEntitlementForPIDInheritance(%@) and PID: %d"
+ "-MXSystemController- %s: Client %@ should not be using MXSystemController property PickedRouteWithPassword!"
+ "-MXSystemController- %s: Completed operation, outCategoryCopy = %@"
+ "-MXSystemController- %s: Completed operation, volume applied = %1.3f, muted = %@"
+ "-MXSystemController- %s: Copying Property %@"
+ "-MXSystemController- %s: FAILED: clientPID=%d, key=%@, value=%@: returning err=%d"
+ "-MXSystemController- %s: FAILED: clientPID=%d, key=%@: returning err=%d"
+ "-MXSystemController- %s: Failed to get default maximum volume limit for built-in speaker, relevant feature flag is disabled"
+ "-MXSystemController- %s: Failed to get maximum volume limit for built-in speaker, relevant feature flag is disabled"
+ "-MXSystemController- %s: Failed to get status of maximum volume limit for built-in speaker, relevant feature flag is disabled"
+ "-MXSystemController- %s: Finalizing MXSystemController for Client with PID = %d"
+ "-MXSystemController- %s: Found session '%{public}@' with {AudioSessionID:'%d', PID:'%{public}@'} attributed to process {BundleID:'%{public}@', PID:'%d'}"
+ "-MXSystemController- %s: Getting nowPlayingAppPID='%d', nowPlayingAppIsPlaying=%{BOOL}u"
+ "-MXSystemController- %s: Invalid PID."
+ "-MXSystemController- %s: IsSomeoneRecording with PID=%d"
+ "-MXSystemController- %s: MXSystemController created for Client with PID = %d/%d"
+ "-MXSystemController- %s: Maximum volume limit for built-in speaker is %1.3f, Speaker Volume Limit is %s"
+ "-MXSystemController- %s: Maximum volume limit for built-in speaker is %s"
+ "-MXSystemController- %s: Notification %@ being posted to non-suspended %@ with payload %@"
+ "-MXSystemController- %s: Notification='%@' client='%@' clientHasSubscribedToNotification=%{BOOL}u notificationShouldBePostedBasedOnApplicationStateOfClient=%{BOOL}u skipNotifyingMusicApp=%{BOOL}u"
+ "-MXSystemController- %s: NowPlayingAppDisplayID=%@"
+ "-MXSystemController- %s: PlayingSessionsDescription=%@"
+ "-MXSystemController- %s: Posting Notification %@ to registered MXSystemControllers with remoteDeviceID %@"
+ "-MXSystemController- %s: Posting notification %@ to MXSystemController %@"
+ "-MXSystemController- %s: PreferHeadphonesOverCarsAndSpeakersEnabled is now %{public}s"
+ "-MXSystemController- %s: Property %@ is unrecognized"
+ "-MXSystemController- %s: Property %@ returned err = %d"
+ "-MXSystemController- %s: RecordingClientPIDs=%@"
+ "-MXSystemController- %s: RecordingSessionsDescription=%@"
+ "-MXSystemController- %s: Returning %@"
+ "-MXSystemController- %s: Setting Property %@ to value %@"
+ "-MXSystemController- %s: Setting downlink mute value to: %{BOOL}u"
+ "-MXSystemController- %s: Setting pidToInheritAppStateFrom for '%@' (transitively) to %d instead of '%d'."
+ "-MXSystemController- %s: Setting pidToInheritAppStateFrom for '%@' to %d"
+ "-MXSystemController- %s: Setting stark main audio owned by iOS but borrowed by car to : %@"
+ "-MXSystemController- %s: Setting uplink mute value to: %{BOOL}u"
+ "-MXSystemController- %s: VibeIntensity=%1.3f"
+ "-MXSystemController- %s: allowBluetoothAccessoryToRequestAudioRoute is %s"
+ "-MXSystemController- %s: cmsFetchCanInheritApplicationStateFromOtherProcesses for pid %d = %d"
+ "-MXSystemController- %s: getting CurrentPlayingSessionIsRoutedViaCarBT = %s"
+ "-MXSystemController- %s: getting FullMute status"
+ "-MXSystemController- %s: getting current primary app displayID"
+ "-MXSystemController- %s: getting deviceSupportsPiP"
+ "-MXSystemController- %s: getting headphone volume limit: %1.3f"
+ "-MXSystemController- %s: hostPID cannot be zero!"
+ "-MXSystemController- %s: isCurrentRouteHeadphonesAndInEar = %hhu, isPreferHeadphonesOverCarsAndSpeakersEnabled = %hhu, allowBluetoothAccessoryToRequestAudioRoute = %d"
+ "-MXSystemController- %s: outAudioSessionID cannot be nil!"
+ "-MXSystemController- %s: preferHeadphonesOverCarsAndSpeakersEnabled is %s"
+ "-MXSystemController- %s: returning CurrentRouteHasVolumeControl = %s"
+ "-MXSystemController- %s: setting ThermalGainAdjustment_Haptics to: %.3f"
+ "-MXSystemController- %s: setting ThermalGainAdjustment_Speaker to: %.3f"
+ "-MXSystemController- %s: setting volume limit to %1.3f"
+ "-MXSystemController_Common- %s: Number of MXSidekickSystemController: %lu"
+ "-MXSystemController_Common- %s: Number of MXSystemController: %lu"
+ "-MXSystemMirroring_Embedded- %s: Endpoint = %@ is already NOT active"
+ "-MXSystemMirroring_Embedded- %s: Endpoint is NULL"
+ "-MXSystemMirroring_Embedded- %s: endpoint is NULL"
+ "-MXSystemMirroring_Embedded- %s: endpointName = %{public}@, inActivationSeed=%llu, err = %d, inFeatures=%d, correlationID=%{public}@. Time taken to activateEndpoint: %f ms. Time taken to run callback %f ms. Total round trip time: %f ms."
+ "-MXSystemMirroring_Embedded- %s: endpointToDeactivate is NULL"
+ "-MXSystemMirroring_Embedded- %s: inEndpoint is NULL"
+ "-MXSystemMirroring_Embedded- %s: inEndpoint is NULL!"
+ "-MXSystemMirroring_Embedded- %s: inFailureInfo is NULL"
+ "-MXSystemSoundServices- %s: Completed request to play privacy pong sound... Resetting conditions to play privacy pong to false"
+ "-MXSystemSoundServices- %s: Invalid system sound:%d"
+ "-MXSystemSounds- %s:  ACTIVATING pid : %d; ssid : %d, prewarmAudio: %d, prewarmVibe: %d audioIsPrewarmed %d vibeIsPrewarmed %d "
+ "-MXSystemSounds- %s:  DEACTIVATING pid : %d; ssid : %d, prewarmAudio: %d, prewarmVibe: %d audioIsPrewarmed %d vibeIsPrewarmed %d "
+ "-MXSystemSounds- %s: !!! called - ssid = %d"
+ "-MXSystemSounds- %s: %@ MUST be heard"
+ "-MXSystemSounds- %s: %@ is an invalid first entry, should be RingVibrate{On,Off,Ignore}"
+ "-MXSystemSounds- %s: %@ is an invalid second entry, should be SilentVibrate{On,Off,Ignore}"
+ "-MXSystemSounds- %s: %@ is an invalid third entry, should be RingerSwitch{On,Off,Ignore}"
+ "-MXSystemSounds- %s: %@ plays to %@ (vadID = %d)"
+ "-MXSystemSounds- %s: ( rawVolume = %f ) <= ( maxVolume = %f )"
+ "-MXSystemSounds- %s: Active client playing to same VAD; system sound cannot take volume"
+ "-MXSystemSounds- %s: Applying scalar volume = %f for category = %{public}@ with max ssid volume = %f over rawVolume = %f"
+ "-MXSystemSounds- %s: Assigning mappedCategory to category because mapped category is NULL."
+ "-MXSystemSounds- %s: Assigning mappedCategory to category because mappedCategory should be suppressed."
+ "-MXSystemSounds- %s: Audio Category OK [%.4s]"
+ "-MXSystemSounds- %s: Called for category: %@"
+ "-MXSystemSounds- %s: Called with ssSynchronizer %p loop %s didFinishContext %@"
+ "-MXSystemSounds- %s: Called with ssid %d vibrateOptions %@"
+ "-MXSystemSounds- %s: Calling AudioToolbox::AudioSessionKillClientSystemSounds for pid = %d"
+ "-MXSystemSounds- %s: Camera is not being used. No need to map categories for always heard sounds."
+ "-MXSystemSounds- %s: Camera shutter should %s click"
+ "-MXSystemSounds- %s: Cannot read SystemSoundVolumeAdjustment.plist"
+ "-MXSystemSounds- %s: Client not allowed to play system sounds."
+ "-MXSystemSounds- %s: Could not create SystemSound array to track Audio prewarming on %{public}@."
+ "-MXSystemSounds- %s: Could not create SystemSound array to track Vibe prewarming."
+ "-MXSystemSounds- %s: Could not create SystemSound dictionary to track Audio prewarming."
+ "-MXSystemSounds- %s: Couldn't prewarm audio for system sounds because we aren't initialized yet."
+ "-MXSystemSounds- %s: Couldn't prewarm vibe for system sounds because we aren't initialized yet or Vibe Synth Engine is unavailable."
+ "-MXSystemSounds- %s: Current route types OK: %@"
+ "-MXSystemSounds- %s: Device is connected to a LineOut accessory"
+ "-MXSystemSounds- %s: Ducking [%p] '%@' by %1.3f"
+ "-MXSystemSounds- %s: Error: audioCategory and/or gSystemSoundVibrationPatterns missing!"
+ "-MXSystemSounds- %s: Error: vibrationStyle is NULL. Perhaps plist is missing?"
+ "-MXSystemSounds- %s: FigVAEndpointManagerCopyPropertyForAudioDevice returned error %d for kFigVAEndpointManagerProperty_DeviceVolume"
+ "-MXSystemSounds- %s: Input is NULL."
+ "-MXSystemSounds- %s: NULL systemSoundDetails dictionary"
+ "-MXSystemSounds- %s: Not playing, as SystemSoundShouldPlay queue is being cleared"
+ "-MXSystemSounds- %s: Not switching to broadcast, just changing volume"
+ "-MXSystemSounds- %s: Process with PID %d not found among callers to prewarm Audio for SSID %d."
+ "-MXSystemSounds- %s: Process with PID %d not found among callers to prewarm Vibe."
+ "-MXSystemSounds- %s: RegionalSystemSoundsThatShareBehaviour.plist cannot be found!"
+ "-MXSystemSounds- %s: Setting to StandardAV"
+ "-MXSystemSounds- %s: Sleeping for async system sound ducking"
+ "-MXSystemSounds- %s: Special case: NOT reconfiguring the device"
+ "-MXSystemSounds- %s: Stark is connected, do not change system sound software volume."
+ "-MXSystemSounds- %s: Stopping vibe with options: %@"
+ "-MXSystemSounds- %s: Suppress shutter sound because carrier network reports outside JP/KH!"
+ "-MXSystemSounds- %s: Suppress shutter sound because carrier voice reports JP/KH sim but roaming!"
+ "-MXSystemSounds- %s: Suppress shutter sound because carrier voice reports not JP/KH sim and not in Japan/South Korea!"
+ "-MXSystemSounds- %s: System Sound can only be played to headphone routes!"
+ "-MXSystemSounds- %s: System sound max volume for route '%@' = %f"
+ "-MXSystemSounds- %s: System sound min volume for route '%@' = %f"
+ "-MXSystemSounds- %s: System sound playing to SystemLocalVAD but it is the same underlying physical device as DefaultVAD. We need to duck normally."
+ "-MXSystemSounds- %s: System sound playing to SystemLocalVAD which is routed to a different route from DefaultVAD; not ducking anyone."
+ "-MXSystemSounds- %s: System sound will play on headphones. Do not suppress system sound due to recording."
+ "-MXSystemSounds- %s: SystemSound plists haven't been loaded: no system sound will play or vibrate"
+ "-MXSystemSounds- %s: SystemSoundAudioBehaviors.plist cannot be found!"
+ "-MXSystemSounds- %s: SystemSoundLowersMusicVolume.plist cannot be found!"
+ "-MXSystemSounds- %s: SystemSoundMaximumVibrationIntensity.plist cannot be found!"
+ "-MXSystemSounds- %s: SystemSoundMaximumVolume.plist cannot be found!"
+ "-MXSystemSounds- %s: SystemSoundMinimumVolume.plist cannot be found on this device!"
+ "-MXSystemSounds- %s: SystemSoundRingerSettings.plist cannot be found!"
+ "-MXSystemSounds- %s: SystemSoundRouting.plist cannot be found! "
+ "-MXSystemSounds- %s: SystemSoundShouldPlay took %ld us; needs a did finish call: %s"
+ "-MXSystemSounds- %s: SystemSoundVibrationPatterns.plist cannot be found!"
+ "-MXSystemSounds- %s: SystemSoundsWithSpecialBehaviours.plist cannot be found! "
+ "-MXSystemSounds- %s: Too late. System sound not playing"
+ "-MXSystemSounds- %s: VC Active; System sound not asserting route"
+ "-MXSystemSounds- %s: Valid vibe pattern passed in but it's not actually going to vibe; not using short vibe"
+ "-MXSystemSounds- %s: Volume is set on hardware"
+ "-MXSystemSounds- %s: Volume multiplier = %f"
+ "-MXSystemSounds- %s: We're going to vibe in a phone call; use short vibe"
+ "-MXSystemSounds- %s: active session is currently vibrating, don't allow system sound vibration"
+ "-MXSystemSounds- %s: activeNonPlayingControllingSession = '%@'[%p] is waitingToTakeControlAfterSystemSound"
+ "-MXSystemSounds- %s: audioCategory = %@ ==> special routing = %@; currentRouteTypesForSystemSound = %@, currentVADCategory = '%.4s'"
+ "-MXSystemSounds- %s: audioCategory = %@, systemSoundVADVolume = %f, defaultVADToSystemSoundVADVolumeRatio = %f, volumeScalar = %f"
+ "-MXSystemSounds- %s: audioCategory is NULL. Returning 1.0"
+ "-MXSystemSounds- %s: called"
+ "-MXSystemSounds- %s: called (ssid = %d, activate = %s)"
+ "-MXSystemSounds- %s: category %@ -> flags %d -> %1.2f"
+ "-MXSystemSounds- %s: category %@ -> vibePattern: %@"
+ "-MXSystemSounds- %s: category is NULL."
+ "-MXSystemSounds- %s: creating clearSystemSoundShouldPlayQueueTimer"
+ "-MXSystemSounds- %s: creating deferFinishSystemSoundThatMustBeHeardTimer for ssid %u; lastSSIDSettingDeferFinishSystemSoundThatMustBeHeardTimer = %u"
+ "-MXSystemSounds- %s: defaultVADToSystemSoundVADVolumeRatios = %@"
+ "-MXSystemSounds- %s: destinations is NULL"
+ "-MXSystemSounds- %s: didn't assert any route; but we will duck others' volume by %1.2f"
+ "-MXSystemSounds- %s: didn't assert any route; just mixed in"
+ "-MXSystemSounds- %s: do nothing because SS is attempting to play before we have initialized Celeste server"
+ "-MXSystemSounds- %s: found active client [%p] '%@', category = %@"
+ "-MXSystemSounds- %s: found active&playing client [%p] '%@'"
+ "-MXSystemSounds- %s: gCMSM.currentRouteTypesForSystemSound is NULL. Returning 1.0"
+ "-MXSystemSounds- %s: gCMSM.playingSystemSoundThatMustBeHeard value : %d"
+ "-MXSystemSounds- %s: gCMSS.defaultVADToSystemSoundVADVolumeRatios is NULL. Returning 1.0"
+ "-MXSystemSounds- %s: gRegionalSystemSoundsThatShareBehaviour is NULL"
+ "-MXSystemSounds- %s: gSystemSoundAudioBehaviors is NULL"
+ "-MXSystemSounds- %s: isTouchTone == %s"
+ "-MXSystemSounds- %s: lastPlayingSession = '%@'[%p] is waitingToTakeControlAfterSystemSound"
+ "-MXSystemSounds- %s: maxVolumeNum is NULL - return 1.0"
+ "-MXSystemSounds- %s: minVolumeNum is NULL - return 0.0"
+ "-MXSystemSounds- %s: mustBeHeard but speaker alert VAD doesn't exist and route is not speaker; setting RingtonePreview category"
+ "-MXSystemSounds- %s: mustBeHeard but speaker alert VAD exists; not taking any control"
+ "-MXSystemSounds- %s: mustBeHeard sound ended with no-one to retake control; setting category and volume to default."
+ "-MXSystemSounds- %s: mustBeHeard ssid will NOT be suppressed because isCarrierNetworkReachable: %d; isoCountryCodeForCarrierNetwork %@ isoCountryCodeForMCC %@ countryNameFromOperatorCountryBundle %@ isCarrierVoiceInJapanOrKorea %d"
+ "-MXSystemSounds- %s: mustBeHeard: speaker alert VAD doesn't exist but route is speaker. Not setting route configuration."
+ "-MXSystemSounds- %s: mustBeHeardSystemSoundBeSuppressed %d"
+ "-MXSystemSounds- %s: no resulting audio (flags = %d, kCMSessionMgrSystemSoundShouldPlayFlag_Audio = %d), so didn't look for special routing"
+ "-MXSystemSounds- %s: no special routing"
+ "-MXSystemSounds- %s: not applying special routing, since it's already set"
+ "-MXSystemSounds- %s: numberOfSystemSoundsPlayingAudio = %d"
+ "-MXSystemSounds- %s: outPlayFlags is NULL"
+ "-MXSystemSounds- %s: pVolume is NULL"
+ "-MXSystemSounds- %s: pid %d audioCategory %@"
+ "-MXSystemSounds- %s: pid %d audioCategory %@ mixesIn %{BOOL}u"
+ "-MXSystemSounds- %s: plist has no Default value"
+ "-MXSystemSounds- %s: posting VibeWillStart"
+ "-MXSystemSounds- %s: ratioRef is NULL. Return 1.0"
+ "-MXSystemSounds- %s: ratiosDictionary = %@, currentSystemSoundVADRoute = %@, ratio = %f"
+ "-MXSystemSounds- %s: ratiosForCategory is NULL even after having tried to get default entry. Returning 1.0"
+ "-MXSystemSounds- %s: releasing gCMSS.clearSystemSoundShouldPlayQueueTimer"
+ "-MXSystemSounds- %s: releasing gCMSS.deferFinishSystemSoundThatMustBeHeardTimer; lastSSIDSettingDeferFinishSystemSoundThatMustBeHeardTimer = %u"
+ "-MXSystemSounds- %s: requested, but we won't duck, duckVolume = %1.3f"
+ "-MXSystemSounds- %s: returning: %@"
+ "-MXSystemSounds- %s: ss max volume = %1.3f"
+ "-MXSystemSounds- %s: ss min volume = %1.3f"
+ "-MXSystemSounds- %s: suppressing system sound due to recording"
+ "-MXSystemSounds- %s: system sound should play over shared audio route, calling to set ownership on port = %u"
+ "-MXSystemSounds- %s: system sounds playing audio: %d"
+ "-MXSystemSounds- %s: systemSoundAudioBehavior is NULL"
+ "-MXSystemSounds- %s: systemSoundMaxVolumes is NULL - return 1.0"
+ "-MXSystemSounds- %s: systemSoundMinVolumes is NULL - return 0.0"
+ "-MXSystemSounds- %s: took %ld us"
+ "-MXSystemSounds- %s: unducking %@ "
+ "-MXSystemSounds- %s: vibrationOptions is NULL."
+ "-MXSystemSounds- %s: we'll duck if requested"
+ "-MXSystemSounds- %s: we'll set our own route configuration"
+ "-MXSystemSounds- %s: we'll set our own volume"
+ "-MXUserPreferredInputRouteCache- %s: Error clearing userPreferredInput route while session is active, err = %d"
+ "-MXUserPreferredInputRouteCache- %s: Missing required parameter! routeName='%{private}@', routeUID='%{public}@', audioRouteName='%{public}@'"
+ "-MXUserPreferredInputRouteCache- %s: No user preferred input entry to remove."
+ "-MXUserPreferredInputRouteCache- %s: Pick system default route '%{public}@'"
+ "-MXUserPreferredInputRouteCache- %s: Pick the defaultVAD input route, endpointToRemove: %{private}@"
+ "-MXUserPreferredInputRouteCache- %s: Removing userPreferredRoute %{public}@ for %{public}@"
+ "-MXUserPreferredInputRouteCache- %s: Updating userPreferredRoute for '%{public}@' to %{private}@"
+ "-MXUserPreferredInputRouteCache- %s: userPreferredRoute for '%@'=%@"
+ "-MXVolumeManager- %s:  Media volume on personal audio device %{public}@~%{public}@~%{public}@~%{public}@ too low (%0.2f). Device connected after %0.2fs (> %0.2fs). Adaptive volume disabled or not present. Updating volume to %0.2f"
+ "-MXVolumeManager- %s: Personal audio device disconnection time: %@"
+ "-MX_BannerManager- %s: AirPods were on A2DP before transfer"
+ "-MX_BannerManager- %s: AirPods were on HFP before transfer"
+ "-MX_BannerManager- %s: Banner entry already deleted, no op"
+ "-MX_BannerManager- %s: Banner entry deleted before banner response, route probably went away"
+ "-MX_BannerManager- %s: Banner not running"
+ "-MX_BannerManager- %s: Cache key NOT present, Route went away, uid = %{public}@, routeName = %{public}@"
+ "-MX_BannerManager- %s: Cache key REMOVED, Route went away, uid = %{public}@, routeName = %{public}@, dismissBanner result = %{public}d, txid = %{public}@"
+ "-MX_BannerManager- %s: Cache key REMOVED, Route went away, uid = %{public}@, routeName = %{public}@, dismissBannerResult = %hhu"
+ "-MX_BannerManager- %s: Caching partner ports, count = %lu"
+ "-MX_BannerManager- %s: Not running"
+ "-MX_BannerManager- %s: Reverse banner entry deleted for newRouteMacAddress = %{private}@"
+ "-MX_BannerManager- %s: Setting newPortNeedsToShowBanner = NO from YES for device = %{public}@"
+ "-MX_BannerManager- %s: Undo banner entry created for newRouteMacAddress = %{private}@, txid = %{public}@"
+ "-MX_BannerManager- %s: Undo banner request for port = %{public}d, id = %{public}@, macAddress=%{public}@, route=%{public}@, cachedUndoBannerResponse = %{public}@"
+ "-MX_BannerManager- %s: Undo banner response = %{public}@ for newRouteMacAddress = %{public}@"
+ "-MX_BannerManager- %s: Undo banner response = do not connect"
+ "-MX_BannerManager- %s: UndoBannerResponse = connect"
+ "-MX_BannerManager- %s: isCarPlayPortRoutableFromCustomizedRoutingPerspective = %{public}@"
+ "-MX_BannerManager- %s: newPortNeedsToShowBanner = %u for newPortId = %{public}@, prevPortIsHfp = %u, newPortIsHfp = %u, prevPortIsA2dp = %u, newPortIsA2dp = %u, isCarPlayMainAudioPortType = %u"
+ "-MX_BannerManager- %s: newPortNeedsToShowBanner = NO. After awaiting, banner object already deleted, means route went away"
+ "-MX_BannerManager- %s: newPortNeedsToShowBanner = NO. After awaiting, response from first banner =  %{public}@"
+ "-MX_BannerManager- %s: newPortNeedsToShowBanner = NO. Awaiting banner response for device = %{public}@, deviceid = %{public}@"
+ "-MX_BannerManager- %s: newPortNeedsToShowBanner = NO. Banner entry present for device = %{public}@"
+ "-MX_BannerManager- %s: newPortNeedsToShowBanner = NO. Creating new banner entry for device = %{public}@"
+ "-MX_BannerManager- %s: newPortNeedsToShowBanner = NO. Creating new banner object for device = %{public}@"
+ "-MX_BannerManager- %s: newPortNeedsToShowBanner = NO. Executing connect on ACQ after awaiting"
+ "-MX_BannerManager- %s: newPortNeedsToShowBanner = NO. Using Connect banner response from cache = connect"
+ "-MX_BannerManager- %s: newPortNeedsToShowBanner = NO. Using Connect banner response from cache = do not connect"
+ "-MX_BannerManager- %s: newPortNeedsToShowBanner = NO. cachedConnectBannerResponse = %{public}@"
+ "-MX_BannerManager- %s: newPortNeedsToShowBanner = NO. cachedConnectBannerResponse after awaiting and signalling, new state = %{public}@"
+ "-MX_BannerManager- %s: newPortNeedsToShowBanner = NO. cachedConnectBannerResponse after awaiting and timedout, new state = %{public}@"
+ "-MX_BannerManager- %s: newPortNeedsToShowBanner = YES.  Connect banner request for port = %{public}d, id = %{public}@, macAddress=%{public}@, route=%{public}@, cachedConnectBannerResponse = %{public}@"
+ "-MX_BannerManager- %s: newPortNeedsToShowBanner = YES. Banner entry created (txid) for newRouteMacAddress = %{private}@, txid = %{public}@"
+ "-MX_BannerManager- %s: newPortNeedsToShowBanner = YES. Banner entry deleted for newRouteMacAddress = %{private}@"
+ "-MX_BannerManager- %s: newPortNeedsToShowBanner = YES. Banner object present for device = %{public}@"
+ "-MX_BannerManager- %s: newPortNeedsToShowBanner = YES. Connect banner response = %{public}@ for newRouteMacAddress = %{public}@"
+ "-MX_BannerManager- %s: newPortNeedsToShowBanner = YES. Creating new banner object for device = %{public}@"
+ "-MX_BannerManager- %s: newPortNeedsToShowBanner = YES. Executing connect in ACQ"
+ "-MX_BannerManager- %s: newPortNeedsToShowBanner = YES. Object deleted before banner response, route probably went away"
+ "-MX_BannerManager- %s: newPortNeedsToShowBanner = YES. connectBannerResponseSemaphore signalled and ConnectBannerResponse = do not connect, userResponse = %{public}@"
+ "-MX_BannerManager- %s: newPortNeedsToShowBanner = YES. connectBannerResponseSemaphore signalled and userResponse = MXUIService_UserAction_Pressed"
+ "-MX_BannerManager- %s: newPortPrefix = %{public}@, newPortSuffix = %{public}@"
+ "-MX_BannerManager- %s: oldEndpoint NOT found for newRouteMacAddress = %{public}@, not performing Undo operation"
+ "-MX_BannerManager- %s: oldEndpoint[%ld] name = %{public}@"
+ "-MX_BannerManager- %s: prevEndpoint = NULL"
+ "-MX_BannerManager- %s: prevPortTypeRef = NULL"
+ "-MX_BannerManager- %s: promptUserResponseForRoute routingContextUUID = %{public}@, oldPort = %u, newPortID = %{public}@"
+ "-MX_BannerManager- %s: promptUserResponseForUndoRoute routingContextUUID = %{public}@, oldPort = %u, newPortID = %{public}@"
+ "-MX_BannerManager- %s: routeUID = %{public}@, portMacAddress = %{public}@ "
+ "-MX_BannerManager- %s: txid = %{public}@"
+ "-MX_BannerManager- %s: undoBannerResponseSemaphore signalled and UndoBannerResponse = connect"
+ "-MX_BannerManager- %s: undoBannerResponseSemaphore signalled and UndoBannerResponse = do not connect, userResponse = %{public}d"
+ "-MX_FeatureFlags- %s: AirPlay/WHAInstantDiscovery_Caching feature is %{public}s"
+ "-MX_FeatureFlags- %s: AudioAccessoryFeatures/AirPodsStudioVoiceMic feature is %{public}@"
+ "-MX_FeatureFlags- %s: BluetoothFeatures/GAPA feature is %s"
+ "-MX_FeatureFlags- %s: MediaExperience/AirPodsInEarRoutingWithCarsAndSpeakers feature is %{public}s"
+ "-MX_FeatureFlags- %s: MediaExperience/CustomizedRoutingWithCarsAndSpeakers feature is %{public}s"
+ "-MX_FeatureFlags- %s: MediaExperience/InputAudioCoexistenceSupport feature is %{public}s"
+ "-MX_FeatureFlags- %s: MediaExperience/MediaMultitasking feature is %{public}s"
+ "-MX_FeatureFlags- %s: MediaExperience/PersonalDevicesMediaVolumeUpdate feature is %{public}@"
+ "-MX_FeatureFlags- %s: MediaExperience/RoutingContextReporting feature is %{public}s"
+ "-MX_FeatureFlags- %s: MediaExperience/ShortFormOutputMuting feature is %{public}s"
+ "-MX_FeatureFlags- %s: MediaExperience/SynchronizeSiriAlarmVolumesToMediaVolume feature is %{public}@"
+ "-MX_FeatureFlags- %s: QuiesceableWiredConnection feature is %{public}s"
+ "-MX_FeatureFlags- %s: SharePlay feature is %s"
+ "-MX_FeatureFlags- %s: SharePlay is disabled on HomePod devices"
+ "-MX_FeatureFlags- %s: TelephonyUtilities/callConnectHaptics feature is %{public}s"
+ "-MX_FeatureFlags- %s: VirtualAudio/input_picker feature is %{public}s"
+ "-MX_FeatureFlags- %s: VirtualAudio/ios_high_quality_local_recording feature is %{public}@"
+ "-MX_FrontBoardServices- %s: DisplayID '%@' has layout role of '%@'"
+ "-MX_FrontBoardServices- %s: Element %li: %{public}@ Layout: %{public}@"
+ "-MX_FrontBoardServices- %s: Layout role not found for %@"
+ "-MX_FrontBoardServices- %s: NULL displayID"
+ "-MX_FrontBoardServices- %s: NULL pLayoutRole"
+ "-MX_FrontBoardServices- %s: Unable to dlopen FrontBoardServices"
+ "-MX_FrontBoardServices- %s: Unable to dlopen SpringboardServices"
+ "-MX_FrontBoardServices- %s: Unable to find class FBSDisplayLayoutMonitor"
+ "-MX_FrontBoardServices- %s: Unable to find class FBSDisplayLayoutMonitorConfiguration"
+ "-MX_FrontBoardServices- %s: primary app bundleID is %@"
+ "-MX_GEOCountryConfiguration- %s: Country code configuration change notification received %@"
+ "-MX_GEOCountryConfiguration- %s: Current country code %@"
+ "-MX_GEOCountryConfiguration- %s: isoCountryCode is empty!"
+ "-MX_HIDEvents- %s: Called for event %u, smartCoverClosedOld %{BOOL}u  smartCoverClosedNew %{BOOL}u"
+ "-MX_NetworkObserver- %s: Network path update received for %@; currentPath: %@"
+ "-MX_NetworkObserver- %s: Updating with new path. Reachable: %i, Cellular: %i"
+ "-MX_NetworkObserver- %s: carrierNetworkReachable: %d"
+ "-MX_PrivacyAccounting- %s: Begin privacy account access interval count : %u"
+ "-MX_PrivacyAccounting- %s: Reporting recording interval end for accessInterval: %@"
+ "-MX_PrivacyAccounting- %s: Reporting recording interval start using audit token for recording client %{public}@"
+ "-MX_PrivacyAccounting- %s: Reporting recording interval start using mic attribution for recording client"
+ "-MX_PrivacyAccounting- %s: Reporting recording interval start using pid for recording client %{public}@"
+ "-MX_RunningBoardServices- %s: Copying assertions for pid %d"
+ "-MX_RunningBoardServices- %s: Could not acquire assertionRef for PID: %d"
+ "-MX_RunningBoardServices- %s: Could not acquire assertionRefForHostProcess for hostPID: %d and PID: %d"
+ "-MX_RunningBoardServices- %s: Could not create assertionRef for PID: %d"
+ "-MX_RunningBoardServices- %s: Could not create assertionRefForHostProcess for hostPID: %d and PID: %d"
+ "-MX_RunningBoardServices- %s: Currently monitoring for predicates %@ after adding %@"
+ "-MX_RunningBoardServices- %s: Currently monitoring for predicates %@ after removing %@"
+ "-MX_RunningBoardServices- %s: Getting host process assertion for client with PID: %d and host PID: %d"
+ "-MX_RunningBoardServices- %s: Invalid PID"
+ "-MX_RunningBoardServices- %s: Process '%{public}@' with state '%{public}@' is added to the cache"
+ "-MX_RunningBoardServices- %s: Process '%{public}@' with state '%{public}@' is removed from the cache"
+ "-MX_RunningBoardServices- %s: Process with pid %d has state update %@"
+ "-MX_RunningBoardServices- %s: Redundant process monitoring change."
+ "-MX_RunningBoardServices- %s: Returning application state %{public}@ from cache for pid %d"
+ "-MX_RunningBoardServices- %s: Returning host process pid %d for pid %d"
+ "-MX_RunningBoardServices- %s: Skipping invalidating assertion %{public}@ as assertionExplanationContainsSessionId = %{BOOL}u accountedAssertionSetContainsAssertion = %{BOOL}u"
+ "-MX_RunningBoardServices- %s: Unaccounted assertion %{public}@"
+ "-MX_RunningBoardServices- %s: process assertion array: %@"
+ "-MX_SystemStatus- %s: signal completionStatusSemaphore"
+ "-MX_TelephonyClient- %s: called"
+ "-MX_TelephonyClient- %s: countryName %{public}@"
+ "-MX_TelephonyClient- %s: isInHomeCountry is not available"
+ "-MX_TelephonyClient- %s: isoCountryCode is empty!"
+ "-MX_TelephonyClient- %s: isoCountryCode is not available"
+ "-MX_TelephonyClient- %s: mcc %{public}@"
+ "-MX_TelephonyClient- %s: mcc is not available"
+ "-MX_TelephonyClient- %s: subscriptionContext %{public}@"
+ "-MX_TelephonyClient- %s: subscriptionContext is not available"
+ "-PVM-"
+ "-PVM- %s: %@~%@ mapped to %@ %s equivalent to %@~%@ mapped to %@"
+ "-PVM- %s: %@~%@ mapped to %@~%@"
+ "-PVM- %s: %s, categoryWithMode = %@"
+ "-PVM- %s: ***FAILED*** (%d)"
+ "-PVM- %s: Adding %@ to list of applicable headphone routes"
+ "-PVM- %s: Adding %@ to list of headphone routes"
+ "-PVM- %s: BOGUS REGIONAL VOLUME LIMIT (%1.3f), using %1.3f instead"
+ "-PVM- %s: Bad value(s) in SystemSoundVolumeAdjustment.plist, ignoring plist entirely and falling back to default volume adjustment"
+ "-PVM- %s: Cannot get the mapped endpoint type as route name is NULL\n"
+ "-PVM- %s: Changing the BT volume entry (%@) to the new format HeadphonesBT~deviceID"
+ "-PVM- %s: Combining the BT key/value pair: %@ / %@ to %@"
+ "-PVM- %s: Computed synchronized volume of %f. Media volume = %f, volume bucket = %{public}@"
+ "-PVM- %s: Current Endpoint type is NULL. Something seems wrong?\n"
+ "-PVM- %s: Current volume will be changed."
+ "-PVM- %s: Endpoint %@ disconnection time from PVM pref: %@"
+ "-PVM- %s: Endpoint (%@) disconnection time saved to PVM pref: %@"
+ "-PVM- %s: Endpoint configuration is not properly set. Something is terribly wrong, Endpoint type is NULL!\n"
+ "-PVM- %s: Endpoint disconnection time info not present in PVM pref, going to bail"
+ "-PVM- %s: Endpoint type present= %@\n"
+ "-PVM- %s: EndpointTypeInfo is nil."
+ "-PVM- %s: Error: failed to register notification handler for HAENVolumeLimitStatusDidChange with status: [%u]."
+ "-PVM- %s: Failed to allocate for endpoingDisconnectionTimeInfoPrefs\n"
+ "-PVM- %s: Failed to save endpoint type"
+ "-PVM- %s: French volume limit %s enabled"
+ "-PVM- %s: HighVolumeLimit read from plist as %1.3f"
+ "-PVM- %s: Invalid device route, going to bail"
+ "-PVM- %s: MappedBluetoothRouteWithDeviceIDAppended for key %@: %@."
+ "-PVM- %s: Mapping %@~%@ to %@"
+ "-PVM- %s: Mapping for %@ in the cache = %@"
+ "-PVM- %s: Not combining BT volumes as it has already been done."
+ "-PVM- %s: Not deleting AirPlay volumes as the cleanup has already been done."
+ "-PVM- %s: Not deleting LowLatencyAirPlay volumes as the cleanup has already been done."
+ "-PVM- %s: Not deleting endpointTypeInfo entries as the cleanup has already been done."
+ "-PVM- %s: PVMDefaultVolumeMultiplier is not defined in %{public}@. Using default multiplier value of %f"
+ "-PVM- %s: PVMInitialize failed. Using default multiplier value of %f"
+ "-PVM- %s: Phone call minimum volume was set to zero!  Changing to %1.3f"
+ "-PVM- %s: Posting notification for category %@, Volume %f, reason %@, refCon %@"
+ "-PVM- %s: Redundant change. Current configuration for MediaPlayback volume limit = %@."
+ "-PVM- %s: Regional legalVolumeLimit read from plist as %1.3f"
+ "-PVM- %s: Removing the following key (%@) and it's value from Volume dictionary."
+ "-PVM- %s: Removing the following key/value pair: %@ / %@"
+ "-PVM- %s: Returned voiceCommandSynchroizedVolumeActivityTimestamp = %llu on %{public}@~%{public}@~%{public}@"
+ "-PVM- %s: Route = %@, Category And Volume = %@ \n"
+ "-PVM- %s: Route name does not exist. Cannot save endpoint type.\n"
+ "-PVM- %s: Saved endpoint type for key = %@, Endpoint = %@"
+ "-PVM- %s: Searching for key (%@) in route Info prefs. Needed to apply volume limit for an endpoint.\n"
+ "-PVM- %s: Setting current endpoint type. Endpoint:%@, Route:%@, RouteSubType:%@, Route Identifier:%@"
+ "-PVM- %s: Something went wrong. Using hard-coded value."
+ "-PVM- %s: Successfully updated the endpointTypeInfo dictionary."
+ "-PVM- %s: SystemSoundVolumeAdjustment.plist is bad: One - Zero < 0.25)"
+ "-PVM- %s: SystemSoundVolumeAdjustment.plist is bad: One > 5.0)"
+ "-PVM- %s: SystemSoundVolumeAdjustment.plist is bad: Zero < 0.0"
+ "-PVM- %s: SystemSoundVolumeAdjustment.plist is bad: Zero > 1.0"
+ "-PVM- %s: The default volume for the current route: %f."
+ "-PVM- %s: Updated deviceID: %@"
+ "-PVM- %s: Updating the endpointTypeInfo with: %@ / %@"
+ "-PVM- %s: Updating voiceCommandSynchroizedVolumeActivityTimestamp on %{public}@~%{public}@~%{public}@ to %llu"
+ "-PVM- %s: Valid endpoint disconnection time not found in PVM pref, going to bail"
+ "-PVM- %s: Volume > 1.0 detected in volumeLimits; reducing to 1.0"
+ "-PVM- %s: Volume being set is nan. Something is terribly wrong. Resetting to default volume = %f\n"
+ "-PVM- %s: VolumePrefs is nil."
+ "-PVM- %s: Writing maximum volume limit for built-in speaker pref to disk"
+ "-PVM- %s: called"
+ "-PVM- %s: called (%1.3f)"
+ "-PVM- %s: called (%1.3f, route = %@, deviceID = %@, routeSubtype = %@)"
+ "-PVM- %s: called (%@)"
+ "-PVM- %s: called (Volume limit available only for route = %@"
+ "-PVM- %s: called (category = %@, mode = %@, endpoint = %@, route = %@, deviceID = %@, routeSubtype = %@)"
+ "-PVM- %s: called (category = %@, mode = %@, route = %@, deviceID = %@, routeSubtype = %@)"
+ "-PVM- %s: called (currentCategory = %@)"
+ "-PVM- %s: called (endpoint Type = %@, volumeLimit = %1.3f, currentRouteInfoRoute = %@)"
+ "-PVM- %s: called (endpointType = %@), route = %@, routeSubtype = %@, returned %1.3f"
+ "-PVM- %s: called (pRVC->route = %@, pRVC->deviceID = %@, pRVC->routeSubtype = %@, pRVC->endpointType = %@, category = %@, mode = %@)"
+ "-PVM- %s: called (returned %1.3f)"
+ "-PVM- %s: called (route = %@), returned %1.3f"
+ "-PVM- %s: called (route = %@, deviceID = %@, routeSubtype = %@)"
+ "-PVM- %s: called (route = %@, deviceID = %@, routeSubtype = %@); returning %s"
+ "-PVM- %s: called (route = %@, volumeLimit = %1.3f)"
+ "-PVM- %s: called (vibeIntensity= %.3f)"
+ "-PVM- %s: called (volume = %1.3f, category = %@, mode = %@, endpoint = %@, route = %@, deviceID = %@, routeSubtype = %@)"
+ "-PVM- %s: called (volume = %1.3f, route = %@, deviceID = %@, routeType = %@)"
+ "-PVM- %s: called, Will only apply to routes Headphone and HeadphonesBT."
+ "-PVM- %s: called, category = %@, mode = %@"
+ "-PVM- %s: called, isCategoryCurrent = %{BOOL}u, isRouteInfoCurrent = %{BOOL}u"
+ "-PVM- %s: category = %@, mode = %@, categoryWithMode = %@"
+ "-PVM- %s: categoryWithMode = %@, outCategory = %@, outMode = %@"
+ "-PVM- %s: couldn't allocate routeInfoOrig"
+ "-PVM- %s: couldn't allocate volumePrefsOrig"
+ "-PVM- %s: currentRouteIsLineOut: %d, setLineOutVolume: %d"
+ "-PVM- %s: ignored because specified device route is not the current route"
+ "-PVM- %s: minVolumes plist missing!"
+ "-PVM- %s: new volume = %1.3f, old raw volume = %1.3f, new limit = %1.3f"
+ "-PVM- %s: no min volume for category '%@'"
+ "-PVM- %s: no test or regional limit found, sticking with %1.3f"
+ "-PVM- %s: not allowing input gain to be saved for non-USB input routes."
+ "-PVM- %s: personalAudioDevicesMediaVolumeResetTimerDuration = %f sec"
+ "-PVM- %s: pinning volume to 1.0"
+ "-PVM- %s: rawVolume = %1.3f, volume = %1.3f"
+ "-PVM- %s: returned %1.3f"
+ "-PVM- %s: returned %1.3f, rawVolume was %1.3f, limit was %1.3f"
+ "-PVM- %s: returning (volume = %1.3f, route = %@, deviceID = %@, routeType = %@)"
+ "-PVM- %s: routeDefaultVolumes plist missing!"
+ "-PVM- %s: setting SystemSoundVolumeMultiplier pref to %1.3f)"
+ "-PVM- %s: setting raw volume pref %1.3f"
+ "-PVM- %s: volume = %.3f => SS multiplier = %.3f"
+ "-PVM- %s: volume = %1.3f, rawVolume = %1.3f"
+ "-PVM- %s: volume = %f, sStorage->ssVolumeAdjustmentZero = %f, sStorage->ssVolumeAdjustmentScalar = %f, adjustedVolumeMultiplier = %f"
+ "-PVM- %s: volume limit behaviour is set"
+ "-PVM- %s: volume limit behaviour not enforced"
+ "-PVM- %s: writing endpoint disconnection time info pref"
+ "-PVM- %s: writing endpoint type info info pref"
+ "-PVM- %s: writing input volume prefs"
+ "-PVM- %s: writing vibe intensity pref"
+ "-PVM- %s: writing volume limit prefs"
+ "-PVM- %s: writing volume multiplier prefs"
+ "-PVM- %s: writing volume prefs"
+ "-PowerManager- %s: Allocated budget by CPMS for audio: %@"
+ "-PowerManager- %s: Creating CPMS client instance for Audio."
+ "-PowerManager- %s: Creating a CPMS client instance for haptics."
+ "-PowerManager- %s: Register client with CPMS for audio %@."
+ "-PowerManager- %s: Register client with CPMS for haptics %@."
+ "-PowerManager- %s: Request power budget from CPMS for audio %@."
+ "-PowerManager- %s: Request power budget from CPMS for haptics %@."
+ "-PowerManager- %s: Returning power budget for audio: %@"
+ "-PowerManager- %s: Returning power budget for haptics: %@"
+ "-PowerManager- %s: allocated budget by CPMS for haptics: %@"
+ "-VolumeControllerRemote-"
+ "-VolumeControllerRemote- %s: #### SINGLETON VOLUME CONTROLLER SHOULD NEVER BE FINALIZED. File a bug for CoreMedia AP Music. ####"
+ "-VolumeControllerRemote- %s: Discovered serverDied, releasing remote volumeController %p"
+ "-VolumeControllerRemote- %s: Need to acquire new remote volumeController..."
+ "-VolumeControllerRemote- %s: Posting notification = %@ with payload = %@"
+ "-VolumeControllerRemote- %s: VolumeController remote client created err = %d"
+ "-VolumeControllerRemote- %s: VolumeController singleton %p forgetting remote volumeController %p, new remote volumeController = %p"
+ "-VolumeControllerRemote- %s: remoteVolumeController = %p"
+ "-VolumeControllerRemote- %s: serverDied"
+ "-VolumeControllerRemote- %s: volumeController = %p, canUseForRoutingContext = %s"
+ "-VolumeControllerRemote- %s: volumeController = %p, endpointID = %@, canSetEndpointVolume = %s"
+ "-VolumeControllerRemote- %s: volumeController = %p, endpointID = %@, delta = %f"
+ "-VolumeControllerRemote- %s: volumeController = %p, endpointID = %@, mute = %s"
+ "-VolumeControllerRemote- %s: volumeController = %p, endpointID = %@, outCanSetMute = %s"
+ "-VolumeControllerRemote- %s: volumeController = %p, endpointID = %@, outEndpointMute = %s"
+ "-VolumeControllerRemote- %s: volumeController = %p, endpointID = %@, outEndpointVolume = %f"
+ "-VolumeControllerRemote- %s: volumeController = %p, endpointID = %@, outEndpointVolumeControlType = %d"
+ "-VolumeControllerRemote- %s: volumeController = %p, endpointID = %@, outMute = %s"
+ "-VolumeControllerRemote- %s: volumeController = %p, endpointID = %@, subEndpointID = %@, mute = %s"
+ "-VolumeControllerRemote- %s: volumeController = %p, endpointID = %@, volume = %f"
+ "-VolumeControllerRemote- %s: volumeController = %p, routingContext = %p, canSetMasterVolume = %s"
+ "-VolumeControllerRemote- %s: volumeController = %p, routingContext = %p, delta = %f"
+ "-VolumeControllerRemote- %s: volumeController = %p, routingContext = %p, masterVolumeControlType = %d"
+ "-VolumeControllerRemote- %s: volumeController = %p, routingContext = %p, mute = %s"
+ "-VolumeControllerRemote- %s: volumeController = %p, routingContext = %p, outCanSetMute = %s"
+ "-VolumeControllerRemote- %s: volumeController = %p, routingContext = %p, outMute = %s"
+ "-VolumeControllerRemote- %s: volumeController = %p, routingContext = %p, outVolume = %f"
+ "-VolumeControllerRemote- %s: volumeController = %p, routingContext = %p, volume = %f"
+ "-[AVSystemController changeActiveCategoryVolume:fallbackCategory:resultVolume:affectedCategory:]"
+ "-[AVSystemController changeActiveCategoryVolume:forRoute:andDeviceIdentifier:]"
+ "-[AVSystemController changeActiveCategoryVolumeBy:fallbackCategory:resultVolume:affectedCategory:]"
+ "-[AVSystemController changeActiveCategoryVolumeBy:forRoute:andDeviceIdentifier:]"
+ "-[AVSystemController changeVolume:forCategory:mode:]"
+ "-[AVSystemController changeVolumeBy:forCategory:]"
+ "-[AVSystemController changeVolumeForRoute:forCategory:mode:route:deviceIdentifier:andRouteSubtype:]"
+ "-[AVSystemController changeVolumeForRouteBy:forCategory:mode:route:deviceIdentifier:andRouteSubtype:]"
+ "-[AVSystemController getActiveCategoryMuted:forRoute:andDeviceIdentifier:]"
+ "-[AVSystemController getActiveCategoryVolume:andName:]"
+ "-[AVSystemController getActiveCategoryVolume:andName:fallbackCategory:]"
+ "-[AVSystemController getActiveCategoryVolume:andName:forRoute:andDeviceIdentifier:]"
+ "-[AVSystemController getAudioSessionID:forAttributedPID:]"
+ "-[AVSystemController getVolume:category:mode:route:deviceIdentifier:routeSubtype:]"
+ "-[AVSystemController getVolumeForRoute:forCategory:mode:route:deviceIdentifier:andRouteSubtype:]"
+ "-[AVSystemController hasRouteSharingPolicyLongFormVideo:]"
+ "-[AVSystemController init]"
+ "-[AVSystemController pickableRoutesForCategory:]"
+ "-[AVSystemController pickableRoutesForCategory:andMode:]"
+ "-[AVSystemController routeForCategory:]"
+ "-[AVSystemController setActiveCategoryVolumeTo:]"
+ "-[AVSystemController setActiveCategoryVolumeTo:fallbackCategory:resultVolume:affectedCategory:]"
+ "-[AVSystemController setActiveCategoryVolumeTo:forRoute:andDeviceIdentifier:]"
+ "-[AVSystemController setPickedRouteWithPassword:withPassword:]"
+ "-[AVSystemController setVolume:category:mode:route:deviceIdentifier:routeSubtype:rampUpDuration:rampDownDuration:]"
+ "-[AVSystemController setVolume:category:mode:route:deviceIdentifier:routeSubtype:rampUpDuration:rampDownDuration:retainFullMute:]"
+ "-[AVSystemController setVolume:category:mode:route:deviceIdentifier:routeSubtype:rampUpwardDuration:rampDownwardDuration:]"
+ "-[AVSystemController setVolumeForRouteTo:forCategory:mode:route:deviceIdentifier:andRouteSubtype:]"
+ "-[AVSystemController setVolumeTo:forCategory:mode:]"
+ "-[AVSystemController setVolumeTo:forCategory:retainFullMute:]"
+ "-[AVSystemController shouldClientWithAudioScore:hijackRoute:hijackDeniedReason:]"
+ "-[AVSystemController toggleActiveCategoryMutedForRoute:andDeviceIdentifier:]"
+ "-[AVSystemController toggleActiveCategoryMuted]"
+ "-[AVSystemController volumeCategoryForAudioCategory:]"
+ "-[AVSystemController(InternalUse) postEffectiveVolumeNotification:]"
+ "-[AVSystemControllerCommon attributeForKey:]"
+ "-[AVSystemControllerCommon copyAttributeForKeyMappingToFig]"
+ "-[AVSystemControllerCommon copySetAttributeForKeyMappingToFig]"
+ "-[AVSystemControllerCommon releaseSharedInstance]"
+ "-[AVSystemControllerCommon setAttribute:forKey:error:]"
+ "-[CMSM_IDSConnection copyNearbyPairedDeviceUniqueID]"
+ "-[FigRemoteRoutingContextFactory copySidePlayContextWithAllocator:options:context:]"
+ "-[FigRemoteRoutingContextFactory copySystemMirroringContextWithAllocator:options:context:]"
+ "-[MXAdditiveRoutingManager copyActiveSessionsInfo]"
+ "-[MXAdditiveRoutingManager discardUnavailableVADInfoFromDetailedRouteDescriptionIfNeeded:]"
+ "-[MXAdditiveRoutingManager populateVirtualAudioDeviceInfoFromSessionAudioBehaviors:newVADIDToNameMap:]"
+ "-[MXAudioAccessoryServices clearDevicesStateCache]"
+ "-[MXAudioAccessoryServices clearDevicesStateCache]_block_invoke"
+ "-[MXAudioAccessoryServices copyDeviceAddressFromVADPort:]"
+ "-[MXAudioAccessoryServices copyPreferredDeviceAddress:andPreemptivePortInfo:]"
+ "-[MXAudioAccessoryServices copyPreferredDeviceAddress:andPreemptivePortInfo:]_block_invoke"
+ "-[MXAudioAccessoryServices copyPreferredDeviceAddress:andPreemptivePortInfo:]_block_invoke_2"
+ "-[MXAudioAccessoryServices copyPreferredDeviceAddress:bundleID:isHypotheticalQuery:reason:]_block_invoke"
+ "-[MXAudioAccessoryServices dumpDebugInfo]"
+ "-[MXAudioAccessoryServices dumpDebugInfo]_block_invoke"
+ "-[MXAudioAccessoryServices handleBTNotificationAudioRoutingChange]"
+ "-[MXAudioAccessoryServices handleNewWirelessPortConnected:]"
+ "-[MXAudioAccessoryServices handlePortDisconnected:]"
+ "-[MXAudioAccessoryServices handlePortDisconnected:]_block_invoke"
+ "-[MXAudioAccessoryServices handleServerDeath]"
+ "-[MXAudioAccessoryServices hijackWirelessPort:reason:portWentInEar:]"
+ "-[MXAudioAccessoryServices hijackWirelessPort:reason:portWentInEar:]_block_invoke_2"
+ "-[MXAudioAccessoryServices init]"
+ "-[MXAudioAccessoryServices isAnyManagedDeviceConnected]"
+ "-[MXAudioAccessoryServices isPortManaged:]"
+ "-[MXAudioAccessoryServices routeToBTDeviceIfNeeded:]"
+ "-[MXAudioAccessoryServices sendAudioRoutingRequestToDevice:appBundleID:audioScore:flags:reason:responseHandler:]"
+ "-[MXAudioAccessoryServices updateDeviceManagementState:reason:]"
+ "-[MXAudioAccessoryServices updateDeviceManagementState:reason:]_block_invoke"
+ "-[MXAudioAccessoryServices updateDeviceManagementState:reason:]_block_invoke_2"
+ "-[MXCoreSession hasAudioTrack]"
+ "-[MXCoreSession init]"
+ "-[MXCoreSession mxSessionListAddSession:]"
+ "-[MXCoreSession reapplyDeviceSampleRateAndBufferSizeOnVADIfNeeded]"
+ "-[MXCoreSession sendSessionConfigurationInfoToVA]"
+ "-[MXCoreSession setUpDefaultBehavioursForCategoryAtClientRequest]"
+ "-[MXCoreSession shouldSendSessionConfigurationInfoToVA]"
+ "-[MXCoreSession(Utilities) copyPreferredAvailableInputPortFromCache]"
+ "-[MXCoreSession(Utilities) copyPreferredInputPortFromConnectedPorts:]"
+ "-[MXCoreSession(Utilities) copyUserPreferredInputPort]"
+ "-[MXCoreSessionBase addSessionAudioObject]"
+ "-[MXCoreSessionBase additiveRoutingInfo]"
+ "-[MXCoreSessionBase copyAvailableRouteControlFeatures:]"
+ "-[MXCoreSessionBase copySessionRoutingInfoFromVA]"
+ "-[MXCoreSessionBase dealloc]"
+ "-[MXCoreSessionBase didExtractEntitlementsFromAuditToken]"
+ "-[MXCoreSessionBase dumpDebugStateInfo]"
+ "-[MXCoreSessionBase extractAndSetAuditToken:]"
+ "-[MXCoreSessionBase getSessionIDFromAudioObject]"
+ "-[MXCoreSessionBase isActiveDeviceWithValidSessionID:]"
+ "-[MXCoreSessionBase isRecordingWithBTManagedDevice]"
+ "-[MXCoreSessionBase isUsingBuiltInMic]"
+ "-[MXCoreSessionBase populateAdditiveRoutingInfoWithFollowingVADInformation:inputOnly:]"
+ "-[MXCoreSessionBase postSessionNotification:payload:]"
+ "-[MXCoreSessionBase postSessionNotification:payload:]_block_invoke"
+ "-[MXCoreSessionBase processOnDemandVADLossIfNeeded:isPreviousInputVADOnDemand:]"
+ "-[MXCoreSessionBase processOnDemandVADLossIfNeeded:isPreviousInputVADOnDemand:]_block_invoke"
+ "-[MXCoreSessionBase processSessionRoutingInfo:]"
+ "-[MXCoreSessionBase removeSessionAudioObject]"
+ "-[MXCoreSessionBase removeSessionAudioObject]_block_invoke"
+ "-[MXCoreSessionBase sendSessionConfigurationInfoToVA:]"
+ "-[MXCoreSessionBase setIsActive:]"
+ "-[MXCoreSessionBase shouldSendSessionConfigurationInfoToVA]"
+ "-[MXCoreSessionBase unregisterSessionAudioObject]"
+ "-[MXCoreSessionBase updateAudioBehaviorFromVARouteConfig:]"
+ "-[MXCoreSessionBase updateAudioSessionIDAndAudioObject:]"
+ "-[MXCoreSessionBase updateClientName:]"
+ "-[MXCoreSessionBase updateIsRecordingMuted:updateBluetoothFrameworkToPlayMuteChime:]"
+ "-[MXCoreSessionBase updateSessionRoutingInformation:]"
+ "-[MXCoreSessionBase updateShadowingAudioSessionOptions:shouldUpdateVAConfig:]"
+ "-[MXCoreSessionBase wasRecentlyActivated]"
+ "-[MXCoreSessionBase willRouteToOnDemandVADOnActivation:]"
+ "-[MXCoreSessionIndependentAudioResource activate]"
+ "-[MXCoreSessionIndependentAudioResource deactivate]"
+ "-[MXCoreSessionIndependentAudioResource updateIsPlaying:]"
+ "-[MXCoreSessionIndependentAudioResource updateIsRecording:]"
+ "-[MXCoreSessionIndependentInputAudioResource addMXSessionIndependentInputAudioResource:]"
+ "-[MXCoreSessionIndependentInputAudioResource copyPropertyForKey:valueOut:]"
+ "-[MXCoreSessionIndependentInputAudioResource dumpDebugInfo]"
+ "-[MXCoreSessionIndependentInputAudioResource initWithOptions:]"
+ "-[MXCoreSessionIndependentInputAudioResource removeMXSessionIndependentInputAudioResource:]"
+ "-[MXCoreSessionIndependentInputAudioResource sendSessionConfigurationInfoToVA]"
+ "-[MXCoreSessionIndependentInputAudioResource setPropertyForKey:value:]"
+ "-[MXCoreSessionIndependentInputAudioResource shouldSendSessionConfigurationInfoToVA]"
+ "-[MXCoreSessionIndependentInputAudioResource teardown]"
+ "-[MXCoreSessionSecure addMXSessionSecure:]"
+ "-[MXCoreSessionSecure removeMXSessionSecure:]"
+ "-[MXCoreSessionSecure sendSessionConfigurationInfoToVA]"
+ "-[MXCoreSessionSecure shouldSendSessionConfigurationInfoToVA]"
+ "-[MXCoreSessionSidekick(InternalUse) isCategoryValid:]"
+ "-[MXCoreSessionSidekick(InternalUse) isModeValidForCategory:]"
+ "-[MXFrontBoardServices copyPrimaryAppDisplayID]"
+ "-[MXFrontBoardServices getLayoutRoleForDisplayID:layoutRole:]"
+ "-[MXFrontBoardServices init]"
+ "-[MXFrontBoardServices layoutChanged:]"
+ "-[MXMediaEndowmentManager getHostProcessAttributions:]"
+ "-[MXNowPlayingAppManager setWriteNowPlayingAppToDiskTimer:]"
+ "-[MXNowPlayingAppManager writeNowPlayingAppInfoToDisk]"
+ "-[MXRoutingContextCallbackHelper dealloc]"
+ "-[MXRoutingContextCallbackHelper initWithRoutingContext:routeConfigUpdateID:correlationID:callback:context:]"
+ "-[MXRoutingContextReportingRTCServiceImpl initWithFigEndpointType:]"
+ "-[MXRoutingContextReportingRTCServiceImpl initWithFigEndpointType:]_block_invoke"
+ "-[MXRoutingContextReportingRTCServiceImpl sendModificationResult:]_block_invoke"
+ "-[MXSession(InterfaceImpl) _dealloc]_block_invoke"
+ "-[MXSession(InterfaceImpl) copyPropertyForKeyInternal:valueOut:]"
+ "-[MXSession(InternalUse) postIsMutedDidChange]_block_invoke"
+ "-[MXSession(InternalUse) setAudioTrackStatus:]"
+ "-[MXSession(InternalUse) setIsPlayerMuted:]"
+ "-[MXSession(InternalUse) setIsPlayingVideoOutput:]"
+ "-[MXSession(InternalUse) setPreferredAudioHardwareFormat:]"
+ "-[MXSession(InternalUse) setPreferredNumberOfOutputChannels:]"
+ "-[MXSession(InternalUse) setPreferredOutputSampleRate:]"
+ "-[MXSessionIndependentAudioResource dumpDebugInfo]"
+ "-[MXSessionIndependentInputAudioResource copyPropertyForKeyInternal:valueOut:]"
+ "-[MXSessionIndependentInputAudioResource dumpDebugInfo]"
+ "-[MXSessionIndependentInputAudioResource initWithOptions:]"
+ "-[MXSessionIndependentInputAudioResource setPropertyForKeyInternal:value:fromPropertiesBatch:]"
+ "-[MXSessionManager addSessionThatWantsToSuspendNeroScreenMirroring:]"
+ "-[MXSessionManager copySessionsThatUserIntendsToUnmute:]"
+ "-[MXSessionManager handleUserIntentToUnmute:]"
+ "-[MXSessionManager makeStarkPortRoutableForPhoneCall:]"
+ "-[MXSessionManager mxCoreSessionListAddSession:]"
+ "-[MXSessionManager mxCoreSessionListRemoveSession:]"
+ "-[MXSessionManager removeSessionThatWantsToSuspendNeroScreenMirroring:]"
+ "-[MXSessionManager ringerIsOnChanged:]"
+ "-[MXSessionManager updateDeviceSampleRate:]"
+ "-[MXSessionManager updateNeroScreenState:suspendScreen:]"
+ "-[MXSessionManager(Common) getBluetoothCustomizedAlternateCategory:enableBluetooth:]"
+ "-[MXSessionManager(DuckingUtilities) addDuckerToSession:duckerSession:duckingSource:]"
+ "-[MXSessionManager(DuckingUtilities) duckSessionIfDuckerIsActive:]"
+ "-[MXSessionManager(DuckingUtilities) getUpdatedDuckVolume:outDuckVolume:]"
+ "-[MXSessionManager(DuckingUtilities) isSessionDucked:duckingSource:]"
+ "-[MXSessionManager(DuckingUtilities) muteOutputForSession:]"
+ "-[MXSessionManager(DuckingUtilities) removeDuckerForSession:sessionCausingUnduck:duckingSource:outLastDuckingSourceWasRemoved:]"
+ "-[MXSessionManager(DuckingUtilities) unduckSessionsForDucker:]"
+ "-[MXSessionManager(DuckingUtilities) unmuteOutputForSession:]"
+ "-[MXSessionManager(Utilities) canSessionsCoexistDueToMediaMultitasking:victim:]"
+ "-[MXSessionManager(Utilities) canSessionsCoexistDueToOutputMuting:victim:]"
+ "-[MXSessionManager(Utilities) cleanupSessionAssertionsIfNeeded:cleanupReason:]_block_invoke"
+ "-[MXSessionManager(Utilities) getCurrentOutputPort]"
+ "-[MXSessionManager(Utilities) getDefaultBuiltInCustomizedAlternateCategory:defaultBuiltInRoute:]"
+ "-[MXSessionManager(Utilities) getUncustomizedCategory:]"
+ "-[MXSessionManager(Utilities) isCurrentPortTypeMuteable:]"
+ "-[MXSessionManager(Utilities) isPIDAllowedToBeNowPlayingApp:]"
+ "-[MXSessionManager(Utilities) isPortHeadphoneWithInEarDetectionSupported:]"
+ "-[MXSessionManager(Utilities) isSessionAllowedToStartRecordingTemporarily:]"
+ "-[MXSessionManager(Utilities) postStopCommandToShadowingSessionsForSession:withShadowingOptions:]"
+ "-[MXSessionManager(Utilities) resetWaitingToResume:]"
+ "-[MXSessionManager(Utilities) shouldAllowBluetoothAccessoryToRequestAudioRoute]"
+ "-[MXSessionManager(Utilities) synchronizeSessionVolumeWithMediaVolumeIfNeeded:]"
+ "-[MXSessionManager(Utilities) updateSomeLongFormVideoClientIsActive]"
+ "-[MXSessionManagerIndependentAudioResource _endInterruption:withSecTask:andStatus:]"
+ "-[MXSessionManagerIndependentAudioResource addMXCoreSessionIndependentInputAudioResource:]"
+ "-[MXSessionManagerIndependentAudioResource dumpDebugInfo]"
+ "-[MXSessionManagerIndependentAudioResource interruptIndpendentInputAudioResourceSession:interruptorBundleID:interruptorName:fadeDuration:waitingToResume:]"
+ "-[MXSessionManagerIndependentAudioResource postInterruptionCommandNotification:interruptionCommand:interruptorName:interruptorBundleID:status:volumeChangeDuration:]"
+ "-[MXSessionManagerIndependentAudioResource postStopCommandToShadowingSessionsForSession:withShadowingOptions:interruptor:waitingToResume:]"
+ "-[MXSessionManagerIndependentAudioResource removeMXCoreSessionIndependentInputAudioResource:]"
+ "-[MXSessionManagerIndependentAudioResource resumeAllIndependentInputAudioResourceSessions:interruptorBundleID:interruptorName:]"
+ "-[MXSessionManagerIndependentAudioResource resumeAllIndependentInputAudioResourceSessionsShadowing:withShadowingOptions:interruptor:status:]"
+ "-[MXSessionManagerIndependentAudioResource resumeIndependentInputAudioResourceSession:interruptorBundleID:interruptorName:status:fadeDuration:]"
+ "-[MXSessionManagerSecure addMXCoreSessionSecure:]"
+ "-[MXSessionManagerSecure removeMXCoreSessionSecure:]"
+ "-[MXSessionManagerSidekick registerMXCoreSessionSidekick:]"
+ "-[MXSessionManagerSidekick unregisterMXCoreSessionSidekick:]"
+ "-[MXSessionSecure copyPropertyForKeyInternal:valueOut:]"
+ "-[MXSessionSecure setPropertyForKeyInternal:value:fromPropertiesBatch:]"
+ "-[MXSessionSidekick copyPropertyForKey:valueOut:]"
+ "-[MXSessionSidekick dealloc]_block_invoke"
+ "-[MXSessionSidekick setIsPlaying:]"
+ "-[MXSystemController _performVolumeOperation:volume:category:mode:routeName:routeDeviceIdentifier:routeSubtype:outVolume:outSequenceNumber:outMuted:outCategoryCopy:outModeCopy:]"
+ "-[MXSystemController _performVolumeOperation:volume:category:mode:routeName:routeDeviceIdentifier:routeSubtype:rampUpDuration:rampDownDuration:outVolume:outSequenceNumber:outMuted:outCategoryCopy:outModeCopy:]"
+ "-[MXSystemController _performVolumeOperation:volume:category:mode:routeName:routeDeviceIdentifier:routeSubtype:rampUpDuration:rampDownDuration:outVolume:outSequenceNumber:outMuted:outCategoryCopy:outModeCopy:retainFullMute:]"
+ "-[MXSystemController _performVolumeOperation:volume:category:mode:routeName:routeDeviceIdentifier:routeSubtype:rampUpwardDuration:rampDownwardDuration:outVolume:outSequenceNumber:outMuted:outCategoryCopy:outModeCopy:]"
+ "-[MXSystemController applyPIDToInheritAppStateFrom:]"
+ "-[MXSystemController getAudioSessionID:forAttributedPID:]"
+ "-[MXSystemSoundServices playPrivacyPongSound]_block_invoke"
+ "-[MXSystemSoundServices playSystemSound:completionBlock:]"
+ "-[MXUserPreferredInputRouteCache clearUserPreferredRoute:]"
+ "-[MXUserPreferredInputRouteCache copyUserPreferredRoute:]"
+ "-[MXUserPreferredInputRouteCache setUserPreferredRoute:hostApplicationBundleID:]"
+ "-[MXVolumeManager(Internal) updateMediaVolumeForPersonalDevice:oldRoute:]"
+ "-[MX_BannerManager cleanupConnectBannerIfNeeded:routeName:]"
+ "-[MX_BannerManager cleanupUndoBannerIfNeeded:routeName:]"
+ "-[MX_BannerManager isCarPlayPortRoutableFromCustomizedRoutingPerspective:]"
+ "-[MX_BannerManager newPortNeedsToShowBanner:newPortIdentifier:newPortType:previousPort:]"
+ "-[MX_BannerManager promptUserResponseForRoute:newPortIdentifier:newPortName:newPortID:newPortType:newWirelessPorts:oldPort:activatingEndpoint:routingContext:connectHandler:]"
+ "-[MX_BannerManager promptUserResponseForRoute:newPortIdentifier:newPortName:newPortID:newPortType:newWirelessPorts:oldPort:activatingEndpoint:routingContext:connectHandler:]_block_invoke"
+ "-[MX_BannerManager promptUserResponseForRoute:newPortIdentifier:newPortName:newPortID:newPortType:newWirelessPorts:oldPort:activatingEndpoint:routingContext:connectHandler:]_block_invoke_2"
+ "-[MX_BannerManager promptUserResponseForUndoRoute:newPortIdentifier:newPortName:newPortID:newPortType:oldPort:routingContext:undoHandler:]"
+ "-[MX_BannerManager promptUserResponseForUndoRoute:newPortIdentifier:newPortName:newPortID:newPortType:oldPort:routingContext:undoHandler:]_block_invoke"
+ "-[MX_BannerManager promptUserResponseForUndoRoute:newPortIdentifier:newPortName:newPortID:newPortType:oldPort:routingContext:undoHandler:]_block_invoke_2"
+ "-[MX_GEOCountryConfigurationObserver countryConfigurationDidChange:]"
+ "-[MX_GEOCountryConfigurationObserver getCurrentCountryCode]_block_invoke"
+ "-[MX_HIDEventObserver handleEvent:]_block_invoke"
+ "-[MX_NetworkObserver isCarrierNetworkReachable]_block_invoke"
+ "-endpoint_central-"
+ "-endpoint_central- %s: After Car initial unborrow nowPlayingApp or active playing client will be %s "
+ "-endpoint_central- %s: Either a session is playing via car's BT or on phone. Send disable bluetooth command, and transfer the playing session to Stark"
+ "-endpoint_central- %s: Either endpoint, entity or resourceType is NULL"
+ "-endpoint_central- %s: Failed to get EndpointCentral storage."
+ "-endpoint_central- %s: If no client is playing and initial mode is User-init/Anytime/Anytime, don't resume nowPlayingApp"
+ "-endpoint_central- %s: Making CarPlay port routable FigStarkModeChangeAction_MakeStarkPortRoutableForPlayingSession"
+ "-endpoint_central- %s: NULL interruptionCommand"
+ "-endpoint_central- %s: NULL interruptionInfo"
+ "-endpoint_central- %s: Nothing to do here, for now"
+ "-endpoint_central- %s: Requested CopyCurrentScreenViewArea on an unsupported endpoint type"
+ "-endpoint_central- %s: Requested CopyHIDInputMode on a non CarPlay endpoint"
+ "-endpoint_central- %s: Requested RequestCarUI on a non CarPlay endpoint"
+ "-endpoint_central- %s: Requested RequestScreenViewArea on an unsupported endpoint type"
+ "-endpoint_central- %s: Requested SendCommand on an unsupported endpoint type"
+ "-endpoint_central- %s: Requested SendData on an unsupported endpoint type"
+ "-endpoint_central- %s: Requested SetHIDInputMode on a non CarPlay endpoint"
+ "-endpoint_central- %s: Requested closeCommChannel on an unsupported endpoint type"
+ "-endpoint_central- %s: Requested createCommChannel on an unsupported endpoint type"
+ "-endpoint_central- %s: Requested createRemoteControlSession on an unsupported endpoint type"
+ "-endpoint_central- %s: Screen is with car; suspend screen"
+ "-endpoint_central- %s: Screen is with iOS; resume screen"
+ "-endpoint_central- %s: Stark mode change action PostiOSEntityIsDoingTurnByTurnChanged"
+ "-endpoint_central- %s: Stark mode change action is LetCarGoActive"
+ "-endpoint_central- %s: Stark mode change action is PostCarEntityHasMainAudio"
+ "-endpoint_central- %s: Stark mode change action is PostNotificationVoicePromptStyleDidChange"
+ "-endpoint_central- %s: Stark mode change action is PostScreenBecameUnavailable"
+ "-endpoint_central- %s: Stark mode change action is PostiOSEntityHasMainAudio"
+ "-endpoint_central- %s: Stark mode change action is ResumeScreenStream_PostScreenBecameAvailable"
+ "-endpoint_central- %s: Stark mode change action is SuspendScreenStream_PostScreenBecameUnavailable"
+ "-endpoint_central- %s: Stark mode main audio owner entity: %d current entity: %d"
+ "-endpoint_central- %s: StopNow and InterruptionEnded were supposed to be synchronous, remember?"
+ "-endpoint_central- %s: Storage has already been invalidated, skipping"
+ "-endpoint_central- %s: Storage invalidated already"
+ "-endpoint_central- %s: Transfer type is %@"
+ "-endpoint_central- %s: Trying to acquire main audio"
+ "-endpoint_central- %s: [%p] called"
+ "-endpoint_central- %s: [%p] called client %@ reason %@"
+ "-endpoint_central- %s: [%p] called closeCommChannel commChannelUUID %@"
+ "-endpoint_central- %s: [%p] called copyCurrentScreenViewArea for displayUUID %@"
+ "-endpoint_central- %s: [%p] called createCommChannel params %@"
+ "-endpoint_central- %s: [%p] called createRemoteControlSession params %@"
+ "-endpoint_central- %s: [%p] called hidUUID %@"
+ "-endpoint_central- %s: [%p] called hidUUID %@ inputMode %@"
+ "-endpoint_central- %s: [%p] called requestScreenViewArea %d for displayUUID %@"
+ "-endpoint_central- %s: [%p] called sendCommand %@ params %@"
+ "-endpoint_central- %s: [%p] called sendData commChannelUUID %@ payload %@"
+ "-endpoint_central- %s: [%p] called setDelegateRemoteControl"
+ "-endpoint_central- %s: a session is playing via car's BT. Send disable bluetooth command, and transfer the playing session to Stark."
+ "-endpoint_central- %s: an active client is already playing, so don't resume nowPlayingApp"
+ "-endpoint_central- %s: called"
+ "-endpoint_central- %s: called with propertyKey %@ returning err=%d"
+ "-endpoint_central- %s: calling setproperty of kFigEndpointProperty_StarkModeController "
+ "-endpoint_central- %s: car is doing phone call with a different phone. DO NOT send disable bluetooth command and let car go active."
+ "-endpoint_central- %s: endpoint is NULL"
+ "-endpoint_central- %s: endpoint is NULL "
+ "-endpoint_central- %s: entity = %@, activity = %@, entityIsDoingActivity = %s"
+ "-endpoint_central- %s: entity = %@, resourceType = %@, entityHoldsResource = %s"
+ "-endpoint_central- %s: entity = %@, resourceType = %@, entityOwnsResource = %s"
+ "-endpoint_central- %s: entity doing activity %@ is %@"
+ "-endpoint_central- %s: iOS phone call is routed to car's BT. Send disable bluetooth command, and transfer the call to Stark."
+ "-endpoint_central- %s: not setting property kFigEndpointProperty_StarkModeController"
+ "-endpoint_central- %s: nothing is going to play. Let car go active"
+ "-endpoint_central- %s: nowPlayingAppCanResume is %s"
+ "-endpoint_central- %s: nowPlayingAppCanResume is False"
+ "-endpoint_central- %s: nowPlayingAppCanResume is true and will play"
+ "-endpoint_central- %s: outStarkModeController is NULL"
+ "-endpoint_central- %s: relaying notification %@"
+ "-endpoint_central- %s: resourceType = %@, gotResource = %s, transferType = %@"
+ "-endpoint_central- %s: resourceType = %@, isPhoneCall = %@, speechRecognitionMode = %@, isTurnByTurnNavigation = %@"
+ "-endpoint_central- %s: resourceType=%@, borrowConstraint=%@"
+ "-endpoint_central- %s: storage is NULL"
+ "-endpoint_central- %s: storage is NULL "
+ "-endpoint_central- %s: storage is NULL."
+ "-endpoint_central- %s: successfully created endpoint central %p"
+ "-stark mode-"
+ "-stark mode- %s: \n\t---------- Current Mode After Mode Change: ----------%@"
+ "-stark mode- %s: \n\t---------- Mode Change Requested: ---------- %@"
+ "-stark mode- %s: Calling send command for stark modes changed, dictionary %{public}@"
+ "-stark mode- %s: Finalizing FigStarkModeController for client with PID %d"
+ "-stark mode- %s: List of borrowers = %@"
+ "-stark mode- %s: Not borrowing screen for car as video is not allowed on screen"
+ "-stark mode- %s: Posted CarEntityHasScreenForAirPlayVideo notification with bundleID:%{public}@"
+ "-stark mode- %s: Posting state changed for token %p"
+ "-stark mode- %s: Returned with err=%d"
+ "-stark mode- %s: Unexpected error: No session active over CarPlay Video"
+ "-stark mode- %s: called"
+ "-stark mode- %s: carPlayEndpoint is NULL"
+ "-stark mode- %s: carPlayEndpoint or currentExtendedEndpoint is NULL"
+ "-stark mode- %s: controller is NULL"
+ ".cxx_destruct"
+ "/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices"
+ "/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices"
+ "0 for ShadowingAudioSessionID, must be non-zero"
+ "1"
+ "22:43:52"
+ "<ID: %llx, CoreSessionID = %lld Name = %@, Muted = %@, ClientIsPlaying = %@, AudioToolboxIsPlaying = %@, MutePriority = %@, PiP = %@, DoesntActuallyPlayAudio = %@, clientType = %x, IsPlayingOutput = %@, IsPlayingVideoOutput = %@"
+ "@\"<MXRoutingContextReportingServiceImpl>\""
+ "@\"BTAudioRoutingRequest\""
+ "@\"FBSDisplayLayoutMonitor\""
+ "@\"MXRoutingContextModificationMetrics\""
+ "@\"NSCondition\""
+ "@\"NSObject<OS_dispatch_semaphore>\""
+ "@\"NSUUID\""
+ "@\"RTCReporting\""
+ "@20@0:8B16"
+ "@20@0:8C16"
+ "@24@0:8I16I20"
+ "@32@0:8I16I20@24"
+ "@40@0:8i16@20B28@32"
+ "@56@0:8^{OpaqueFigRoutingContext=}16@24@32^?40^v48"
+ "AN"
+ "AVAILABLE"
+ "AVAudioSessionCategorySpeechDetection"
+ "AVAudioSessionModeShortFormVideo"
+ "AVAudioSessionModeTelephonyWebcam"
+ "AVSystemControllerCommon"
+ "AVSystemController_Common.m"
+ "ActivationUtilities"
+ "Active MXCoreSessionIndependentAudioResource has lost an on-demand VAD! Please file a radar against 'MediaExperience Session | All'"
+ "Active core session has lost an on-demand VAD! Please file a radar against 'MediaExperience Session | All'"
+ "AirPlayPredictedRouting"
+ "AirPlayVideo"
+ "AirPlayVideoPlaybackAudioOnlyMode"
+ "AirPodsInEarRoutingWithCarsAndSpeakers"
+ "AirPodsStudioVoiceMic"
+ "AllowBluetoothAccessoryToRequestAudioRoute"
+ "AllowBluetoothAccessoryToRequestAudioRouteDidChange"
+ "AllowedRouteTypes can't be set on non-PlayAndRecord categories"
+ "Attempting to set PrefersBluetoothHighQualityContentCapture on a session with a category that does not allow input."
+ "Attempting to set PrefersEchoCancelledInput on a session with a category that does not allow input."
+ "Audible"
+ "AudioAccessory routing request"
+ "AudioAccessorydDiedNotification"
+ "AudioCategory is NULL."
+ "AudioMode is NULL."
+ "AudioSessionID for InterruptAudioSessionIDForHandoff must be non-zero"
+ "AudioTrackStatus"
+ "AvailableEndpointsExtended"
+ "AwaitingUserResponse"
+ "B32@0:8@16^q24"
+ "B32@0:8I16@20B28"
+ "B36@0:8i16I20i24@28"
+ "B40@0:8@16^{__CFString=}24I32I36"
+ "B72@0:8^{__CFString=}16^{__CFString=}24^{__CFString=}32@40I48I52^{__CFString=}56@?64"
+ "B88@0:8^{__CFString=}16^{__CFString=}24^{__CFString=}32@40I48^{__CFArray=}52I60^{OpaqueFigEndpoint=}64^{__CFString=}72@?80"
+ "BTDetails_HighQualityContentCaptureEnabled"
+ "BTDetails_HighQualityContentCaptureSupported"
+ "BTDetails_IsHighQualityContentCaptureEnabled"
+ "BTDetails_SupportsHighQualityContentCapture"
+ "BTNotificationAudioRoutingChange is received"
+ "Bluetooth customization doesn't apply to Multi category"
+ "BluetoothLEInput"
+ "C"
+ "C16@0:8"
+ "CHARGING"
+ "CMSMAP_DisconnectAllAirPlaySessions"
+ "CMSMAP_StartDisconnectAirPlayScreenTimer_block_invoke"
+ "CMSMAP_StartRouteAwayFromAirPlayHandoffTimer_block_invoke"
+ "CMSMAP_StartRouteAwayFromAirPlayHandoffTimer_block_invoke_2"
+ "CMSMAP_StopDisconnectAirPlayScreenTimer_block_invoke"
+ "CMSMAP_StopRouteAwayFromAirPlayHandoffTimer_block_invoke"
+ "CMSMCreateRouteDescriptionFromPortIDOrRouteConfiguration"
+ "CMSMDebugUtility_DumpDebugInfo"
+ "CMSMDeviceState_ButtonsCanChangeRingerVolume"
+ "CMSMDeviceState_Initialize_block_invoke"
+ "CMSMDeviceState_RingerIsOn"
+ "CMSMDeviceState_UpdateDeviceClass"
+ "CMSMNP_NowPlayingAppIsPlayingDidChangeTimerDidFinish"
+ "CMSMNotificationUtility_PostAllowBluetoothAccessoryToRequestAudioRouteDidChangeNotificationIfNeeded"
+ "CMSMNotificationUtility_PostAvailableSampleRatesDidChange_f"
+ "CMSMNotificationUtility_PostAvailableVirtualFormatsDidChange_block_invoke"
+ "CMSMNotificationUtility_PostCallIsActiveDidChangeIfNeeded"
+ "CMSMNotificationUtility_PostCurrentInputDeviceBufferSizeChange"
+ "CMSMNotificationUtility_PostCurrentInputSampleRateDidChange"
+ "CMSMNotificationUtility_PostCurrentOutputDeviceBufferSizeDidChange"
+ "CMSMNotificationUtility_PostCurrentOutputSampleRateDidChange"
+ "CMSMNotificationUtility_PostIsOutputMutedDidChange"
+ "CMSMNotificationUtility_PostIsOutputMutedDidChange_block_invoke"
+ "CMSMNotificationUtility_PostPiPIsPossibleDidChange_f"
+ "CMSMNotificationUtility_PostPickableRoutesDidChange_block_invoke"
+ "CMSMNotificationUtility_PostPreferHeadphonesOverCarsAndSpeakersDidChange"
+ "CMSMNotificationUtility_PostReporterIDsDidChange_block_invoke"
+ "CMSMNotificationUtility_PostResumeCommandToMatchingWaitingClients"
+ "CMSMNotificationUtility_PostSessionAudioModeDidChange_block_invoke"
+ "CMSMNotificationUtility_PostSomeSessionIsPlayingDidChange"
+ "CMSMNotificationUtility_PostSomeSharePlayCapableCallSessionIsActiveDidChange"
+ "CMSMNotificationUtility_PostUserIntentToUnmuteDidChange"
+ "CMSMNotificationUtility_PostUserIntentToUnmuteDidChange_block_invoke"
+ "CMSMNotificationUtility_PostVolumeDidChangeToVolumeButtonClientsWithPayload_block_invoke"
+ "CMSMPowerLogPostPowerLogData_block_invoke"
+ "CMSMSleep_CreateIdleSleepPreventor"
+ "CMSMSleep_CreateIdleSleepPreventorForSession"
+ "CMSMSleep_CreatePrewarmIdleSleepPreventor"
+ "CMSMSleep_FetchPlaybackProcessAssertion"
+ "CMSMSleep_FetchTemporaryPlaybackProcessAssertion"
+ "CMSMSleep_HandleIdleSleep"
+ "CMSMSleep_HandleIdleSleep_block_invoke"
+ "CMSMSleep_ReleaseIdleSleepPreventor"
+ "CMSMSleep_ReleaseIdleSleepPreventorForSession"
+ "CMSMSleep_ReleasePlaybackProcessAssertion"
+ "CMSMSleep_ReleasePrewarmIdleSleepPreventor"
+ "CMSMSleep_UpdateIdleSleepPreventor"
+ "CMSMSleep_UpdatePlaybackProcessAssertionsForHostProcesses"
+ "CMSMStrings_Check"
+ "CMSMUtility_AllowedToUseGPSInBackground"
+ "CMSMUtility_AnySessionBelongingToPIDIsActiveAndStopsWhenBackgrounded"
+ "CMSMUtility_ApplyForEachMatchingSessionGuts"
+ "CMSMUtility_AreVADsRoutedToTheSamePhysicalDevice"
+ "CMSMUtility_ClearOverridesForPhoneCallSessions"
+ "CMSMUtility_CopyActiveCoreSessionsShadowingAudioSessionID"
+ "CMSMUtility_CopyCurrentRouteHasVolumeControl"
+ "CMSMUtility_CopyMostImportantPlayingSession"
+ "CMSMUtility_FetchBackgroundEntitlement"
+ "CMSMUtility_FetchUIShouldIgnoreRemoteControlEvents"
+ "CMSMUtility_GetLongBufferDuration"
+ "CMSMUtility_GetSharePlayCapableActiveCallSession"
+ "CMSMUtility_GetSharePlayCapableActiveMediaSession"
+ "CMSMUtility_GetVADIDForVADName"
+ "CMSMUtility_GetVADNameForVADID"
+ "CMSMUtility_GetVoiceOverDuckFadeDuration"
+ "CMSMUtility_HandOverInterruptionsToSession"
+ "CMSMUtility_IAPAppProcessIDIsUsingAccessory"
+ "CMSMUtility_IAPShouldPauseOnHeadphoneDisconnect"
+ "CMSMUtility_IsAirPlayVideoActive"
+ "CMSMUtility_IsModeValidForCategory"
+ "CMSMUtility_IsSomeRecordingSessionPresentThatDisallowsSystemSounds"
+ "CMSMUtility_PostNotificationToSession"
+ "CMSMUtility_PostNotifyStyleFadeInAppliedForPlaybackHandoff"
+ "CMSMUtility_PostNotifyStyleFadeOutAppliedForPlaybackHandoff"
+ "CMSMUtility_PrintRouteDescriptions"
+ "CMSMUtility_SomePrimaryAudioCategoryClientIsPlaying"
+ "CMSMUtility_SomeSessionIsActiveThatPrefersNoInterruptionsByRingtonesAndAlerts"
+ "CMSMUtility_TransferVolumeControlFlagToSharePlayCapableCallSession"
+ "CMSMUtility_TransferVolumeControlFlagToSharePlayCapableMediaSession"
+ "CMSMUtility_UpdateAudioBehaviourForSessionsUsingRoutingContextUUID"
+ "CMSMUtility_UpdateAudioBehaviourForVoiceOverSessions"
+ "CMSMUtility_UpdatePlayAndRecordAppSpeechState"
+ "CMSMUtility_UpdateVoiceAssistantActiveStateForCarPlay"
+ "CMSMUtility_VibrationPatternIsActuallyGoingToVibe"
+ "CMSMUtility_iOSWillRequestCarMainAudio"
+ "CMSMVAUtility_AudioObjectSetPropertyData"
+ "CMSMVAUtility_CopyFigIODeviceNameFromVADPortTypes"
+ "CMSMVAUtility_CopyFigIODeviceNameFromVADPorts"
+ "CMSMVAUtility_CopyFigInputDeviceNameFromVADPortType"
+ "CMSMVAUtility_CopyFigOutputDeviceNameFromVADPortType"
+ "CMSMVAUtility_CopyRoutesInfoFromInputAndOutputPorts"
+ "CMSMVAUtility_CreatePerAppAirPlayVADIfNeeded"
+ "CMSMVAUtility_CreatePerAppAirPlayVADWithHandOffPort"
+ "CMSMVAUtility_DestroyPerAppAirPlayVAD"
+ "CMSMVAUtility_GetPortOfTypeInArray"
+ "CMSMVAUtility_GetUIDFromRouteDescription"
+ "CMSMVAUtility_GetVADCategoryFromFigCategoryName"
+ "CMSMVAUtility_GetVADInputPortTypeFromFigRouteName"
+ "CMSMVAUtility_GetVADModeFromFigModeName"
+ "CMSMVAUtility_GetVADOutputPortTypeFromFigRouteName"
+ "CMSMVAUtility_IsAnyRouteBTManagedAndInEar"
+ "CMSMVAUtility_IsPortOfTypeBluetoothVehicle"
+ "CMSMVAUtility_MakeConnectedPortRoutable"
+ "CMSMVAUtility_MakeNewlyConnectedWirelessPortsRoutableForEndpoint"
+ "CMSMVAUtility_OverrideToPartnerPort"
+ "CMSMVAUtility_RouteDefaultVADToCarPlayIfNecessary"
+ "CMSMVAUtility_UpdateSessionInfoAndReporterIDsOnVA"
+ "CMSM_GetLocalSessionPriority"
+ "CMSM_IDSClient_Initialize"
+ "CMSM_IDSClient_ReplyToRemote_PlayingInfo"
+ "CMSM_IDSConnection_AddRemotePlayingInfo"
+ "CMSM_IDSConnection_CopySharedAudioRoutePortIDs"
+ "CMSM_IDSConnection_GetRemotePlayingInfo"
+ "CMSM_IDSConnection_IsSomeClientPlayingOverSharedAudioRouteOnRemote"
+ "CMSM_IDSConnection_IsWaitingForGizmoPlayingInfo"
+ "CMSM_IDSConnection_RemoveRemotePlayingInfo"
+ "CMSM_IDSConnection_ResetRemotePlayingInfo"
+ "CMSM_IDSConnection_ResetWaitingForGizmoPlayingInfo"
+ "CMSM_IDSConnection_StartWaitForRemoteToReplyWithInitialPlayingInfoTimer"
+ "CMSM_IDSConnection_StopWaitForRemoteToReplyWithInitialPlayingInfoTimer_block_invoke"
+ "CMSM_IDSConnection_UpdateSharedAudioRouteMacAddressOnLocal"
+ "CMSM_IDSServer_StartAutomaticOwnershipTransferToPhoneTimer"
+ "CMSM_IDS_Initialize"
+ "CMSUtilityApplier_PostNotification_StopCommandWithReason"
+ "CMSUtilityApplier_SetApplicationState"
+ "CMSUtilityPredicate_ShouldDuck"
+ "CMSUtility_ComputePlaybackVolume"
+ "CMSUtility_CopyActiveDuckerForSession"
+ "CMSUtility_CopyCurrentCategoryAndDeviceRoute"
+ "CMSUtility_CopySessionAudioBehaviour"
+ "CMSUtility_CopySessionsToDuck"
+ "CMSUtility_CreateReporterIDIfNeeded"
+ "CMSUtility_FetchGPSEntitlementForSessionWithPID"
+ "CMSUtility_FetchSessionEntitlements"
+ "CMSUtility_GetApplicationStateForSession"
+ "CMSUtility_GetCurrentAudioDestination"
+ "CMSUtility_GetCurrentInputVADUID"
+ "CMSUtility_GetUserVolume"
+ "CMSUtility_GetVolumeDeltaIfRoutedToThirdPartyTV"
+ "CMSUtility_GetWantsAutomaticClusterPairingOnPlaybackStart"
+ "CMSUtility_HasAssertionsToStartNonMixablePlayback"
+ "CMSUtility_InterruptSessionForSecureMicrophonePolicy"
+ "CMSUtility_IsAllowedToStartRecordingCoexistingWithTheAssistant"
+ "CMSUtility_IsAllowedToStopThisSession"
+ "CMSUtility_IsAnExtension"
+ "CMSUtility_IsAudioCategoryPrimary"
+ "CMSUtility_IsAudioCategoryRingtone"
+ "CMSUtility_IsAudioCategoryVoicemail"
+ "CMSUtility_IsAudioModeCameraRelated"
+ "CMSUtility_IsDisruptiveWhenGoingActive"
+ "CMSUtility_IsSessionAllowedToInterruptCurrentlyAirPlayingNowPlayingSession"
+ "CMSUtility_IsSessionRouteEligibleForTipi"
+ "CMSUtility_PlaysToCarAltAudio"
+ "CMSUtility_ResetIsPlayingStates"
+ "CMSUtility_SendSessionReinterruptionDisallowedEventToAudioStatistics"
+ "CMSUtility_SessionWithPIDWasLockStopper"
+ "CMSUtility_SetAudioServiceTypeForReporterID"
+ "CMSUtility_ShouldSessionToInterruptHandOverDucking"
+ "CMSUtility_SomeOtherPrimaryAudioCategoryClientIsPlaying"
+ "CMSessionManager_Sleep.m"
+ "CMSessionManager_VAEndpoint.m"
+ "CMSessionMgrCopyDeviceRouteForRouteConfiguration_block_invoke"
+ "CMSessionMgrCopyDisplayIdentifierToSession_block_invoke"
+ "CMSessionMgrRegisterEndpointManager"
+ "CMSessionMgrSystemSoundActivateForPID_block_invoke"
+ "CMSessionMgrVibrateForSystemSoundWithOptions"
+ "CMSessionMgrVibratorStopWithOptions_block_invoke"
+ "CMSystemSoundManager_GetNumberOfSystemSoundsPlayingAudio"
+ "CMSystemsoundMgr_GetMappedBehaviorCategory"
+ "CachedDiscovery"
+ "Calling process is not entitled to fetch system contexts"
+ "CarEntityHasScreenForAirPlayVideo"
+ "Category is muteable."
+ "CelesteGetRegionSpecificVolumeLimit"
+ "Checking management state for a new connected wireless port"
+ "Client may not change shadowing options when relevant FFs are off"
+ "ClientModificationFinishedTimestamp"
+ "ClientModificationStartedTimestamp"
+ "ClientPID cannot be 0"
+ "Connect"
+ "Copying preemptive port info"
+ "CorrelationID"
+ "Could not allocate PerUIAgent state"
+ "Could not allocate memory for info struct"
+ "Could not create DiscovererServerState"
+ "Could not create RoutingContextServerState"
+ "Could not create a CFDictionary for vibration pattern's intensity."
+ "Could not create a CFMutableArray for playVibrationValue."
+ "Could not create a CFMutableDictionary for playVibrationValue."
+ "Could not create a CFNumber for stopVibrationValue."
+ "Could not create a CFNumber for vibration pattern's Off duration."
+ "Could not create a CFNumber for vibration pattern's On duration."
+ "Could not create a Fig mutex lock"
+ "Could not create a dispatch queue"
+ "Could not create a mutable array"
+ "Could not create endpointAgentServerState"
+ "Could not create endpointUIAgents"
+ "Couldn't find completion entry"
+ "Couldn't find vibe synth routines"
+ "CreateCompletionCallbackParametersFromMessageAndConnection"
+ "CreateDiscovererServerState"
+ "CreateEndpointAgentServerState"
+ "CreatePerUIAgentState"
+ "CreateRoutingContextServerState"
+ "Creating MXCoreSession out of audiomxd process is not allowed"
+ "Current Endpoints: %@ ::"
+ "Current Picked Endpoint Descriptors: %@ ::"
+ "CurrentUIAgent"
+ "CustomizedRoutingWithCarsAndSpeakers"
+ "Determining"
+ "Device became managed"
+ "DisposeRoutingContextServerState"
+ "DoNotConnect"
+ "DuckFadeDuration value is negative"
+ "EndOfCallTone_CEPT"
+ "EndpointType"
+ "Error copying options"
+ "Expected a FigVolumeController"
+ "FALSE"
+ "FVIOKit_ConvertFigTimeToMillisec"
+ "FVIOKit_CreateIntensityDictionary"
+ "FVIOKit_PlayVibration"
+ "FVIOKit_PlayVibrationEndTimeout"
+ "FVIOKit_PlayVibrationWithPattern"
+ "FVIOKit_StartIOServiceVibration"
+ "FVIOKit_StartIOServiceVibrationWithPattern"
+ "FVIOKit_StopVibrator_block_invoke"
+ "FVIOKit_VibePatternArrayCreateDefault"
+ "FVSynthEngine_PlayVibrationWithPatternDictionary"
+ "FVSynthEngine_PostVibrationStoppedNotifications"
+ "FVSynthEngine_SendVibeStoppedNotification_block_invoke"
+ "FVSynthEngine_VibrationPlayedToEnd"
+ "Failed allocating array"
+ "Failed allocating cache queue"
+ "Failed allocating dictionary"
+ "Failed allocating mutex"
+ "Failed allocating notification queue"
+ "Failed allocating queue"
+ "Failed to allocate callback parameters"
+ "Failed to copy FigStarkModeController"
+ "Failed to copy StarkModeController"
+ "Failed to copy descriptor for endpoint"
+ "Failed to copy fallback input route"
+ "Failed to copy fallback route descriptor"
+ "Failed to copy kFigVAEndpointManagerProperty_FallbackInputRouteEndpoint"
+ "Failed to copy predicted selected route descriptor"
+ "Failed to create MXSystemController"
+ "Failed to create dictionary"
+ "Failed to create mutex"
+ "Failed to create notification queue"
+ "Failed to create remote context replacement queue"
+ "Failed to create remote manager replacement queue"
+ "Failed to create session expiration queue"
+ "Failed to dlsym symbol AirPlayStartServicesInMXProcess"
+ "Failed to dlsym symbol FVDUtilsStartXPCServers"
+ "Failed to dlsym symbol FigClusterSynchronizationManager_ClientIsPlaying"
+ "Failed to get PreferHeadphonesOverCarsAndSpeakersEnabled, relevant feature flag is disabled"
+ "Failed to get Virtual Audio endpoint manager"
+ "Failed to get formatter"
+ "Failed to open MediaToolbox"
+ "Failed to reset predicted route"
+ "Failed to start FigStarkModeController server"
+ "Feature flag for maximum volume limit for built-in speaker is disabled"
+ "Feature flag is not on to set this property."
+ "FigEndpointCentral invalidated"
+ "FigEndpointCentralEntityIsDoingActivity"
+ "FigEndpointCentralEntityOwnsResource"
+ "FigEndpointCentralGetResourceTypeBorrowConstraint"
+ "FigEndpointCentralRequestResource"
+ "FigEndpointCentralUpdateIsVoiceAssistantActive"
+ "FigEndpointCentralUpdateiOSDeviceState"
+ "FigEndpointDescriptorUtilitySetUserManualRoute"
+ "FigEndpointUIAgent.m"
+ "FigEndpointUIAgentCopyCurrentEndpointUIAgent"
+ "FigEndpointUIAgentHelper_CleanupPrompt"
+ "FigEndpointUIAgentRemoteXPC.m"
+ "FigEndpointUIAgentRemoteXPC_EnsureClientEstablished_block_invoke"
+ "FigEndpointUIAgentServerXPC.m"
+ "FigEndpointUIAgentStartServer"
+ "FigEndpointUIAgentXPCRemoteCreate"
+ "FigNotificationListenerStartNotifications"
+ "FigPlayerCMSession_SystemWillPowerOn"
+ "FigPlayerCMSession_SystemWillSleep"
+ "FigPredictedRouting.m"
+ "FigPredictedRouting_IsPreemptivePortLogicEnabled"
+ "FigRemoteRoutingContextFactory.m"
+ "FigRouteDiscovererCopyUserSelectionAvailable"
+ "FigRouteDiscovererCopyUserSelectionAvailable_block_invoke"
+ "FigRouteDiscovererRemoteXPC_CopyProperty"
+ "FigRouteDiscovererRemoteXPC_SetProperty"
+ "FigRouteDiscovererServerXPC.m"
+ "FigRouteDiscovererStartServer"
+ "FigRouteDiscovererUpdateCachedUserSelectionAvailable"
+ "FigRouteDiscovereryManagerIsNewDiscoveryModeHigher"
+ "FigRouteDiscoveryManagerAddDiscoverer"
+ "FigRouteDiscoveryManagerCopyFallbackRouteDescriptor"
+ "FigRouteDiscoveryManagerCopyRoutePresentForType"
+ "FigRouteDiscoveryManagerCopyRoutesForTypeAndAudioSessionID"
+ "FigRouteDiscoveryManagerIsClientSuspendedOrTerminated"
+ "FigRouteDiscoveryManagerPowerLogDiscoveryLevelChange_block_invoke"
+ "FigRoutingContextCopyContextForUUID"
+ "FigRoutingContextCopySidePlayContext"
+ "FigRoutingContextCopySystemAudioContext"
+ "FigRoutingContextCopySystemAudioInputContext"
+ "FigRoutingContextCopySystemMirroringContext"
+ "FigRoutingContextCopySystemMusicContext"
+ "FigRoutingContextCopySystemRemoteDisplayContext"
+ "FigRoutingContextCopySystemRemotePoolContext"
+ "FigRoutingContextCreateAudioContext"
+ "FigRoutingContextCreateControlChannelOnlyContext"
+ "FigRoutingContextCreatePerAppSecondDisplayContext"
+ "FigRoutingContextCreateVideoContext"
+ "FigRoutingContextRemoteCopyAllAudioContexts"
+ "FigRoutingContextResilientRemoteCopyContextForUUID"
+ "FigRoutingContextResilientRemoteCopyContextForUUID_block_invoke"
+ "FigRoutingContextResilientRemoteCopyDefaultContext"
+ "FigRoutingContextResilientRemoteCreate"
+ "FigRoutingContextServerStateCloseAndUnregisterAllCommChannels"
+ "FigRoutingContextServerStateRegisterCommChannelForDeviceID"
+ "FigRoutingContextServerStateUnregisterCommChannelForDeviceID"
+ "FigRoutingContextServerXPC.m"
+ "FigRoutingContextStartServer"
+ "FigRoutingContextUtilities_CopyLeaderUUIDForContext_block_invoke"
+ "FigRoutingContextUtilities_CreateStateInfoStringForContext_block_invoke"
+ "FigRoutingContextUtilities_DoesArrayOfEndpointsContainEndpoint"
+ "FigRoutingContextUtilities_IsFollowingAnotherContext_block_invoke"
+ "FigRoutingContextUtilities_LogCurrentState"
+ "FigRoutingContextUtilities_LogCurrentState_block_invoke"
+ "FigRoutingContextUtilities_LogSystemContextCreationErrorIfNeeded"
+ "FigRoutingContextUtilities_UnfollowUUIDFromLeader_block_invoke"
+ "FigRoutingContextXPCHandleCopyPredictedSelectedRouteDescriptorMessage"
+ "FigRoutingContextXPCHandleCopySelectedRouteMessage"
+ "FigRoutingContextXPCHandleCopySelectedRoutesMessage"
+ "FigRoutingContextXPCHandleResetPredictedSelectedRouteDescriptorMessage"
+ "FigRoutingContextXPCHandleSendCommandMessage"
+ "FigRoutingContextXPCHandleSendDataForDeviceIDMessage"
+ "FigRoutingContextXPCHandleSendDataMessage"
+ "FigRoutingContextXPCHandleSetEndpointMessage"
+ "FigRoutingContextXPCHandleSetRouteDescriptorMessage"
+ "FigRoutingCopyDisplayMenuVideoContext"
+ "FigRoutingManagerAddEndpointToAggregate"
+ "FigRoutingManagerContextUtilities_AddActivatedEndpoint_block_invoke"
+ "FigRoutingManagerContextUtilities_AddCurrentlyActivatingEndpoint_block_invoke"
+ "FigRoutingManagerContextUtilities_AddCurrentlyActivatingSubEndpoints_block_invoke"
+ "FigRoutingManagerContextUtilities_CacheSupportedOutputChannelLayouts_block_invoke"
+ "FigRoutingManagerContextUtilities_CopyActivatedEndpointsInfo_block_invoke"
+ "FigRoutingManagerContextUtilities_CopyActivatedEndpoints_block_invoke"
+ "FigRoutingManagerContextUtilities_CopyAggregateEndpointAsFigEndpointAggregate_block_invoke"
+ "FigRoutingManagerContextUtilities_CopyAggregateEndpointAsFigEndpoint_block_invoke"
+ "FigRoutingManagerContextUtilities_CopyArrayOfFollowerUUIDs_block_invoke"
+ "FigRoutingManagerContextUtilities_CopyCachedSelectedRouteDescriptors_block_invoke"
+ "FigRoutingManagerContextUtilities_CopyCurrentlyActivatingEndpointInfoAtIndex_block_invoke"
+ "FigRoutingManagerContextUtilities_CopyCurrentlyActivatingEndpointsInfo_block_invoke"
+ "FigRoutingManagerContextUtilities_CopyCurrentlyActivatingEndpoints_block_invoke"
+ "FigRoutingManagerContextUtilities_CopyCurrentlyActivatingSubEndpoints_block_invoke"
+ "FigRoutingManagerContextUtilities_CopyHijackID_block_invoke"
+ "FigRoutingManagerContextUtilities_CopyPickedEndpointAtIndex_block_invoke"
+ "FigRoutingManagerContextUtilities_CopyPickedEndpoints_block_invoke"
+ "FigRoutingManagerContextUtilities_CopyScreenEndpointUUID_block_invoke"
+ "FigRoutingManagerContextUtilities_CopySupportedOutputChannelLayouts_block_invoke"
+ "FigRoutingManagerContextUtilities_GetActivatedEndpointFeatures_block_invoke"
+ "FigRoutingManagerContextUtilities_GetActivationSeedForEndpoint_block_invoke"
+ "FigRoutingManagerContextUtilities_GetContextType_block_invoke"
+ "FigRoutingManagerContextUtilities_GetMainVolumeScaleFactorForEndpointID_block_invoke"
+ "FigRoutingManagerContextUtilities_GetPickingState_block_invoke"
+ "FigRoutingManagerContextUtilities_IsContextSidePlay_block_invoke"
+ "FigRoutingManagerContextUtilities_IsContextSystemAudio_block_invoke"
+ "FigRoutingManagerContextUtilities_IsContextSystemMusicAndIndependent_block_invoke"
+ "FigRoutingManagerContextUtilities_IsContextSystemRemoteDisplay_block_invoke"
+ "FigRoutingManagerContextUtilities_IsContextVideoAndIndependent_block_invoke"
+ "FigRoutingManagerContextUtilities_IsRoutedToLocalAirplayReceiver_block_invoke"
+ "FigRoutingManagerContextUtilities_RemoveActivatedEndpoint_block_invoke"
+ "FigRoutingManagerContextUtilities_RemoveContext_block_invoke"
+ "FigRoutingManagerContextUtilities_RemoveCurrentlyActivatingEndpointInfoAtIndex_block_invoke"
+ "FigRoutingManagerContextUtilities_RemoveCurrentlyActivatingEndpoint_block_invoke"
+ "FigRoutingManagerContextUtilities_ResetCurrentlyActivatingEndpointInfo_block_invoke"
+ "FigRoutingManagerContextUtilities_ResetCurrentlyActivatingSubEndpointsInfo_block_invoke"
+ "FigRoutingManagerContextUtilities_SaveCommChannelUUID_block_invoke"
+ "FigRoutingManagerContextUtilities_SetAudioEndpoint_block_invoke"
+ "FigRoutingManagerContextUtilities_SetDefaultLeaderUUIDForContext_block_invoke"
+ "FigRoutingManagerContextUtilities_SetMainVolumeScaleFactorForEndpointID_block_invoke"
+ "FigRoutingManagerContextUtilities_SetPickedEndpoints_block_invoke"
+ "FigRoutingManagerContextUtilities_SetPickingState_block_invoke"
+ "FigRoutingManagerContextUtilities_SetScreenEndpoint_block_invoke"
+ "FigRoutingManagerContextUtilities_StopDiscoveryTimer_block_invoke"
+ "FigRoutingManagerContextUtilities_UpdateRouteDescriptorForGivenContext_block_invoke"
+ "FigRoutingManagerCopyAirPlayEndpointsInUseForFeatures"
+ "FigRoutingManagerCopyBluetoothEndpointAssociatedWithVAEndpoint"
+ "FigRoutingManagerCopyCurrentGroupUUID"
+ "FigRoutingManagerCopyEndpointToAutoConnect"
+ "FigRoutingManagerCopyEndpointWithDeviceIDFromBluetoothManager"
+ "FigRoutingManagerCopyLocalAirPlayEndpoint"
+ "FigRoutingManagerCopyPartnerPorts"
+ "FigRoutingManagerCopyWHAGroupableVAEndpoint"
+ "FigRoutingManagerCreateAndActivateAggregateEndpointForContext"
+ "FigRoutingManagerCreateAndActivateAggregateEndpointForLocalPlayback"
+ "FigRoutingManagerCreateEndpointDeactivateOptions"
+ "FigRoutingManagerCreateSubEndpointAddOptions"
+ "FigRoutingManagerDoesDeviceAlwaysHaveAggregateForLocalPlayback"
+ "FigRoutingManagerIsRoutableConsideringBannerState"
+ "FigRoutingManagerNewWirelessPortsAdded"
+ "FigRoutingManagerPerformPostInitOperations"
+ "FigRoutingManagerProcessAirPodsInEarRouting"
+ "FigRoutingManagerProcessAirPodsInEarRouting_block_invoke"
+ "FigRoutingManagerProcessCarPlayEndpointDeactivation"
+ "FigRoutingManagerRegisterAndCopyContext"
+ "FigRoutingManagerRegisterContextWithUUID"
+ "FigRoutingManagerRemoveAllSubEndpointsFromAggregate"
+ "FigRoutingManagerResumeCurrentEndpointScreen"
+ "FigRoutingManagerStartCarPlayAudioMainPortPublishingCheckTimer"
+ "FigRoutingManagerStartCarPlayAudioMainPortPublishingCheckTimer_block_invoke"
+ "FigRoutingManagerStartDeactivateAirPlayEndpointTimer"
+ "FigRoutingManagerStartDeactivateAirPlayEndpointTimer_block_invoke"
+ "FigRoutingManagerStopCarPlayAudioMainPortPublishedCheckTimer"
+ "FigRoutingManagerStopDeactivateAirPlayEndpointTimer"
+ "FigRoutingManagerSuspendCurrentEndpointScreen"
+ "FigRoutingManagerUtilities_CopySidePlayEndpoints"
+ "FigRoutingManagerUtilities_LogPartnerPorts"
+ "FigRoutingManager_HandleDidReceiveDataFromCommChannelDelegate_block_invoke"
+ "FigRoutingManager_SetAuthorizationOnEndpoint"
+ "FigRoutingManager_iOSHandleFigEndpointFeaturesActivation"
+ "FigRoutingManager_iOSHandleFigEndpointFeaturesDeactivation"
+ "FigRoutingManager_iOSHandleStartupFailed"
+ "FigRoutingSession.m"
+ "FigRoutingSessionManagerCopyLongFormVideoManager"
+ "FigRoutingSessionManagerRemoteCopyLongFormVideoManager"
+ "FigRoutingSessionManagerRemoteXPC.m"
+ "FigRoutingSessionManagerResilientRemote.m"
+ "FigRoutingSessionManagerResilientRemoteCopyLongFormVideoManager"
+ "FigRoutingSessionManagerServerXPC.m"
+ "FigRoutingSessionManagerStartServer"
+ "FigSTS Server connection was lost"
+ "FigSTSCreate"
+ "FigSTSServerStart"
+ "FigSTS_Common.m"
+ "FigSTS_Remote.m"
+ "FigSTS_Server.m"
+ "FigStarkModeChangeGetActions"
+ "FigStarkModeControllerRemote.m"
+ "FigStarkModeControllerServer.m"
+ "FigSystemController.m"
+ "FigSystemControllerCreate"
+ "FigSystemController_Remote.m"
+ "FigSystemController_Server.m"
+ "FigVAEndpointCreate"
+ "FigVAEndpointManagerCreate"
+ "FigVAEndpointManagerHandleAvailableEndpointsChanged"
+ "FigVibrator.m"
+ "FigVibratorInitialize"
+ "FigVibratorPlayVibrationWithDictionary"
+ "FigVibratorPostNotification"
+ "FigVibratorStartPrewarm"
+ "FigVibratorStopPrewarm"
+ "FigVibratorStopWithOptions"
+ "FigVibrator_IOKit.m"
+ "FigVibrator_VibeSynthEngine.m"
+ "FigVolumeControllerAddAirPlayVolumeNotificationListeners"
+ "FigVolumeControllerCopySharedController"
+ "FigVolumeControllerRemoteXPC.m"
+ "FigVolumeControllerRemoveAirPlayVolumeNotificationListeners"
+ "FigVolumeControllerServerXPC.m"
+ "Follower Type %@, "
+ "Follower context %@, "
+ "Following context %@ "
+ "HAS an"
+ "HDMILatencyMgr_GetHDMILatencyForCurrentRefreshRate"
+ "HandleCopyAllAudioContextsMessage"
+ "HandleCopyRoutingContextForUUIDMessage"
+ "HandleCopySystemRoutingContextMessage"
+ "HandleCreateRoutingContextMessage"
+ "HandleCreateStarkModeControllerMessage"
+ "HandleCreateSystemControllerMessage"
+ "HandleDeviceWakeStatus"
+ "HandleEndpointUIAgentRemoteMessage"
+ "HandleNoReplySystemControllerMessage"
+ "HandlePrepareForPlaybackMessage"
+ "HandleRouteDiscovererRemoteMessage"
+ "HandleRoutingContextRemoteMessage"
+ "HandleRoutingSessionManagerRemoteMessageWithNoReply"
+ "HandleRoutingSessionManagerRemoteMessageWithReply"
+ "HandleSetAuthInfo"
+ "HandleSetPasswordFromKeychain"
+ "HandleStarkModeControllerMessage"
+ "HandleStartHighConfidenceSessionMessage"
+ "HandleStartSessionWithRouteDescriptorsMessage"
+ "HandleStartSuppressingLikelyDestinationsMessage"
+ "HandleStopSuppressingLikelyDestinationsMessage"
+ "HandleSystemControllerMessage"
+ "HandleUpdateCurrentSessionFromLikelyDestinationsMessage"
+ "Haptic VAD"
+ "HardwareRouteConfiguration"
+ "HasExternalMuteNotificationContext"
+ "HostApplicationBundleID"
+ "HostPID"
+ "IS"
+ "IS NOT"
+ "In-Ear status changed"
+ "Incorrect priority"
+ "Input"
+ "InputAudioCoexistenceSupport"
+ "Internal"
+ "InterruptionFadeDuration value is negative"
+ "Invalid AudioCategory for this session type"
+ "Invalid AudioMode for this session type"
+ "Invalid context type"
+ "Invalid intensity"
+ "Invalid interruption style"
+ "Invalid mutePriority"
+ "Invalid playDuration"
+ "Invalid preferredHardwareFormat"
+ "Invalid vibePattern. Need even number of entries"
+ "Invalid vibePattern. need to specify a series of bool+duration entries in pattern."
+ "IsAllowed"
+ "IsAnyLongFormVideoSessionActive"
+ "IsCached"
+ "IsCallManagementMuteControl Feature not enabled or SessionBasedMuting is enabled and this is not supported for SessionBasedMuting."
+ "IsIndependentInputAudioResourceSession"
+ "IsOutputMuted"
+ "IsOutputMuted requires FF support"
+ "IsOutputMutedDidChange"
+ "IsPlayerMuted"
+ "IsPlayingVideoOutput"
+ "IsRecordingMuted is not supported for IndependentAudioResource sessions while SessionBasedMuting is not enabled."
+ "IsRecordingMutedForRemoteDevice cannot be set to true when Oneness is not active"
+ "IsRecordingMutedForRemoteDevice cannot be set to true when session is recording"
+ "IsRecordingMutedForRemoteDevice requires FF support"
+ "IsRemoteDeviceInputControlAllowed requires FF support"
+ "IsSharePlayCapableCallSession needs to have phone call behavior"
+ "Long-form video routing session manager not yet allocated.  Call FigRoutingSessionManagerInit first"
+ "LookupEndpointUIAgentByObjectIDForConnection"
+ "LookupRouteDiscovererByObjectIDForConnection"
+ "LookupRoutingContextByObjectIDForConnection"
+ "LookupStarkModeControllerByObjectIDForConnection"
+ "LookupSystemControllerByObjectIDForConnection"
+ "MXAudioAccessoryServices"
+ "MXConnectBannerResponseInfo"
+ "MXCoreSessionBase.m"
+ "MXCoreSessionIndependentAudioResource"
+ "MXCoreSessionIndependentInputAudioResource"
+ "MXCoreSessionIndependentInputAudioResource.m"
+ "MXCoreSessionInitialize"
+ "MXCoreSessionSecureCommon.m"
+ "MXCoreSessionSetProperty_block_invoke"
+ "MXDispatchUtilityCreateOneShotTimer_block_invoke"
+ "MXEndpointDescriptorCleanupBannersIfNeeded"
+ "MXFrontBoardServices"
+ "MXInitializationCommon.m"
+ "MXInitialization_Embedded.m"
+ "MXIsTypeOfSession"
+ "MXNowPlayingAppManager.m"
+ "MXRoutingContext"
+ "MXRoutingContextModificationMetrics"
+ "MXRoutingContextModificationResult"
+ "MXRoutingContextReportingRTCServiceImpl"
+ "MXRoutingContextReportingService"
+ "MXRoutingContextReportingServiceImpl"
+ "MXSessionIndependentAudioResource"
+ "MXSessionIndependentInputAudioResource"
+ "MXSessionIndependentInputAudioResource.m"
+ "MXSessionManagerIndependentAudioResource"
+ "MXSessionManagerIndependentAudioResource.m"
+ "MXSessionSecureCommon.m"
+ "MXSystemRemotePool_AddEndpointToContext"
+ "MXSystemRemotePool_RemoveEndpointFromContext"
+ "MXSystemSoundServices"
+ "MXUndoBannerResponseInfo"
+ "MXUserPreferredInputRouteCache"
+ "MX_AudioAccessoryServices.m"
+ "MX_BannerManager"
+ "MX_BannerManager.m"
+ "MX_CoreServices_Initialize_block_invoke"
+ "MX_FeatureFlags_IsAirPodsInEarRoutingWithCarsAndSpeakersEnabled_block_invoke"
+ "MX_FeatureFlags_IsAirPodsStudioVoiceMicEnabled_block_invoke"
+ "MX_FeatureFlags_IsCallConnectHapticsEnabled_block_invoke"
+ "MX_FeatureFlags_IsCounterfeitDetectionEnabled_block_invoke"
+ "MX_FeatureFlags_IsCustomizedRoutingWithCarsAndSpeakersEnabled_block_invoke"
+ "MX_FeatureFlags_IsHighQualityLocalRecordingEnabled_block_invoke"
+ "MX_FeatureFlags_IsInputAudioCoexistenceSupportEnabled_block_invoke"
+ "MX_FeatureFlags_IsMediaMultitaskingEnabled_block_invoke"
+ "MX_FeatureFlags_IsPersonalDevicesMediaVolumeUpdateEnabled_block_invoke"
+ "MX_FeatureFlags_IsRoutingContextReportingEnabled_block_invoke"
+ "MX_FeatureFlags_IsSharePlayEnabled_block_invoke"
+ "MX_FeatureFlags_IsShortFormOutputMutingEnabled_block_invoke"
+ "MX_FeatureFlags_IsSynchronizeSiriAlarmVolumesToMediaVolumeEnabled_block_invoke"
+ "MX_FeatureFlags_IsWHAInstantDiscoveryCachingEnabled_block_invoke"
+ "MX_RunningBoardServices_CopyAssertionReasonsForPID"
+ "MX_RunningBoardServices_CopyDisplayIDForPID"
+ "MX_RunningBoardServices_CreatePlaybackProcessAssertionForPID"
+ "MX_RunningBoardServices_GetApplicationStateForPID"
+ "MX_SystemSoundServices.m"
+ "MX_SystemStatus_PublishRecordingClientsInfo_block_invoke_2"
+ "Managed"
+ "Maximum volume limit for built-in speaker feature is disabled"
+ "May 28 2025"
+ "May not copy Fallback route for non-input discoverers"
+ "May not set IsRecordingMuted on non-Shadowing IndependentAudioResource sessions"
+ "MediaMultitasking"
+ "MirrorActivationLifeCycle"
+ "Missing Entitlement to allow app to initiate recording temporarily"
+ "Missing Entitlement to enable Wombat"
+ "Missing entitlement"
+ "Missing entitlement for DuckScalarForVoiceOver"
+ "Missing entitlement to set PreferredMinimumMicrophoneIndicatorLightOnTime"
+ "Missing entitlement to set PrefersToOptOutOfHardwareSafetyInterruptions"
+ "Missing entitlement."
+ "Missing required entitlement com.apple.avfoundation.allows-set-output-device"
+ "ModificationMetrics"
+ "Multi-channel doesn't apply to Multi category"
+ "Must be properly entitled to use system output contexts"
+ "NFCCardComplete"
+ "NFCCardError"
+ "NFCCardProvisioned"
+ "NOT"
+ "NOT AN"
+ "NOT AVAILABLE"
+ "NOT CHARGING"
+ "NOT CurrentUIAgent"
+ "NOT VALID"
+ "NULL "
+ "NULL CMSession."
+ "NULL bundleID"
+ "NULL category"
+ "NULL commChannelUUID"
+ "NULL command"
+ "NULL context/callbackParams"
+ "NULL contextOut"
+ "NULL data"
+ "NULL deviceID"
+ "NULL endpoint"
+ "NULL initialRemoteContext"
+ "NULL mode"
+ "NULL mutePriority"
+ "NULL mxSession"
+ "NULL mxSessionOut."
+ "NULL newRemoteContext"
+ "NULL newRemoteManager"
+ "NULL notificationBlock"
+ "NULL oldRemoteContext"
+ "NULL oldRemoteManager"
+ "NULL outAirPlayActivePlaying"
+ "NULL outAirPlayVideoActive"
+ "NULL outDestination"
+ "NULL outDestinations"
+ "NULL outHijackDeniedReason"
+ "NULL outIsActive"
+ "NULL outManager"
+ "NULL outPickableRoutes"
+ "NULL outPrefersLikelyDestinations"
+ "NULL outPropertyValue."
+ "NULL outRoutingContext"
+ "NULL outRoutingSessionManagerObjectID"
+ "NULL outSession"
+ "NULL outShouldHijack"
+ "NULL outVolumeController"
+ "NULL parameter"
+ "NULL preferredHardwareFormat"
+ "NULL propertyKey"
+ "NULL propertyKey."
+ "NULL propertyValueOut"
+ "NULL remoteContextCreationBlock"
+ "NULL routeDescription"
+ "NULL session"
+ "NULL session or clientPID is 0"
+ "NULL shmemName"
+ "NULL shmemOut"
+ "NULL stsFlavor"
+ "NULL stsLabel"
+ "NULL stsOut"
+ "NULL sub-port preferences"
+ "NULL systemMusicContext"
+ "NULL valueOut"
+ "NULL vibePattern"
+ "NULL vibePatternArray"
+ "No CaptureOrientationOverride data"
+ "No entitlement for setting emergency alert priority"
+ "No vibration data"
+ "Non-CFBoolean property value"
+ "Non-CFDictionary activation context"
+ "Non-null and non-CFDictionary PreferredRouteControlFeatures"
+ "Not Siri session"
+ "Not VoiceAssistant session"
+ "Not connected to vibrator IOService."
+ "Notification from unexpected CMSession"
+ "Notification from unexpected FigRoutingContext"
+ "NowPlayingAppStack is disabled"
+ "Object is not a FigEndpointUIAgent"
+ "Object is not a FigRouteDiscoverer"
+ "Object is not a FigRoutingContext"
+ "Object is not a FigStarkModeController"
+ "Object is not a FigSystemController"
+ "Out of range ClientType"
+ "Output"
+ "OutputMuteSessionProperty"
+ "PVMCategoriesAreEquivalent"
+ "PVMComputeSynchronizedVolume"
+ "PVMCopyCurrentCategoryAndMode"
+ "PVMCopyCurrentDeviceRoute"
+ "PVMCopyEndpointDisconnectionTimeInfo"
+ "PVMGetCurrentPreferredRawVolume"
+ "PVMGetCurrentPreferredVolume"
+ "PVMGetCurrentPreferredVolumeForDeviceRoute"
+ "PVMGetInputVolumePreference"
+ "PVMGetMappedEndpointType"
+ "PVMGetRawVolumeForCurrentRouteFromVolume"
+ "PVMGetThirdPartyVolumeMultiplier"
+ "PVMGetVibeIntensityPreference"
+ "PVMGetVolumeLimit"
+ "PVMGetVolumeMultiplier"
+ "PVMGetVolumePreference"
+ "PVMInitialize"
+ "PVMInitialize failed"
+ "PVMIsCategoryAndRouteInfoCurrent"
+ "PVMIsCurrentDeviceRoute"
+ "PVMIsOKToMuteCurrentCategory"
+ "PVMSaveEndpointDisconnectionTimeInfo"
+ "PVMSaveEndpointTypeFromCurrentRouteInfo"
+ "PVMSetCurrentCategoryAndModeGuts"
+ "PVMSetCurrentPreferredVolumeForDeviceRoute"
+ "PVMSetCurrentPreferredVolumeWithRefCon"
+ "PVMSetInputVolumePreference"
+ "PVMSetVibeIntensityPreference"
+ "PVMSetVolumeLimit"
+ "PersonalDevicesMediaVolumeUpdate"
+ "Plist key missing"
+ "PostProcessing"
+ "PreferHeadphonesOverCarsAndSpeakersDidChange"
+ "PreferHeadphonesOverCarsAndSpeakersEnabled"
+ "PreferredDecoupledInputOutput can't be set on non-PlayAndRecord or non-eARC categories"
+ "PreferredDecoupledInputOutput can't be set when RequiresAggregatedInputOutput is set to true"
+ "PreferredDecoupledInputOutput can't be set when a session is playing"
+ "PreferredMinimumMicrophoneIndicatorLightOnTime cannot be < 0"
+ "PrefersBluetoothHighQualityContentCapture"
+ "PrefersNoInterruptionsDuringRemoteDeviceControl requires FF support"
+ "PrefersToPlayAudioToHeadphonesOnly"
+ "Prepare session activation"
+ "PrepareForPlaybackCompletionCallback"
+ "Preprocessing"
+ "Preprocessing_RouteToHandoff"
+ "Processing"
+ "Processing_Activated"
+ "Processing_Activated_AudioPortsPublished"
+ "Processing_Activated_WaitingForAudioPortPublication"
+ "Processing_Activating"
+ "Processing_Activating_AudioPortsPublished"
+ "Processing_Activating_WaitingForAudioPortPublication"
+ "QuiesceableWiredConnection"
+ "RTCDictionary"
+ "RTCReporting"
+ "RefconDestructor"
+ "RemoteDeviceIDs may not be set with airplayd FF off."
+ "RequiresAggregatedInputOutput can't be set on non-PlayAndRecord categories"
+ "RequiresAggregatedInputOutput can't be set when a session is playing"
+ "RouteConfigUpdatedReason"
+ "RouteDetailedDescription_HighQualityContentCaptureEnabled"
+ "RouteDetailedDescription_SupportsHighQualityContentCapture"
+ "RoutingContextModificationCallback"
+ "RoutingContextOut cannot be NULL"
+ "RoutingContextReporting"
+ "SBSDisplayLayoutRoleDescription"
+ "STSLoadCreateFunction"
+ "ScreenIsDarkDidChange"
+ "SendCommandCompletionCallback"
+ "SendDataCompletionCallback"
+ "Server connection was lost"
+ "ServerModificationFinishedTimestamp"
+ "ServerModificationStartedTimestamp"
+ "Session cannot do output mute"
+ "Session currently has an invalid category for isSharePlayMediaSession."
+ "SessionInterruption"
+ "SessionOutputUnmuted"
+ "ShadowingAudioSessionOptions"
+ "ShadowingOptions"
+ "ShortFormOutputMuting"
+ "ShortFormVideo"
+ "ShouldMuteBeAppliedToRemoteDevice requires FF support"
+ "Silent"
+ "Single SetProperty has failed"
+ "SiriActivation"
+ "SomeClientIsPlayingToAirPlayDidChange"
+ "SomeLongFormVideoClientIsActiveDidChange"
+ "SourceAppBundleID"
+ "SpatialModeAlways"
+ "Speaker VAD"
+ "SpeechDetect session cannot request audio budget"
+ "StartHighConfidenceSessionCompletionCallback"
+ "Storage has been invalidated"
+ "Stream already suspended"
+ "Stream not suspended"
+ "SynchronizeSiriAlarmVolumesToMediaVolume"
+ "System input picker FF is off, not querying fallback route"
+ "T@\"MXCoreSession\",W,N,V_interruptingSession"
+ "T@\"MXRoutingContextModificationMetrics\",R,&,N,V_modificationMetrics"
+ "T@\"NSDictionary\",&,V_mostRecentSessionInfoSetOnVA"
+ "T@\"NSMutableArray\",&,N,V_fromPorts"
+ "T@\"NSNumber\",&,V_clientModificationFinishedTimestamp"
+ "T@\"NSNumber\",&,V_clientModificationStartedTimestamp"
+ "T@\"NSNumber\",&,V_serverModificationFinishedTimestamp"
+ "T@\"NSNumber\",&,V_serverModificationStartedTimestamp"
+ "T@\"NSObject<OS_dispatch_semaphore>\",&,N,V_routeSemaphore"
+ "T@\"NSString\",&,N,V_figEndpointType"
+ "T@\"NSString\",R,&,N,V_correlationID"
+ "T@\"NSString\",R,&,N,V_routeConfigUpdateReason"
+ "T@\"NSUUID\",&,N,V_txid"
+ "T@,W,V_selfWeak"
+ "TB,N"
+ "TB,N,V_audioToolboxIsPlaying"
+ "TB,N,V_hasExternalMuteNotificationContext"
+ "TB,N,V_isOutputMuted"
+ "TB,N,V_isVoiceAssistantPlayingToPersonalAudioDeviceOverMedia"
+ "TB,N,V_prefersBluetoothHighQualityContentCapture"
+ "TB,N,V_someLongFormVideoClientIsActive"
+ "TB,R,V_shouldPrivacyPongPlay"
+ "TC,N,V_connectBannerResponse"
+ "TC,N,V_undoBannerResponse"
+ "TI,N,V_audioObjectID"
+ "TI,N,V_shadowingAudioSessionOptions"
+ "TRUE"
+ "TelephonyUtilities"
+ "TimeTakenForRequestToReachServer"
+ "TimeTakenToRunClientCallback"
+ "Tipi device hijack was rejected"
+ "TotalRequestTime"
+ "TotalTimeSpentInServer"
+ "True and will play if applicable"
+ "Trying to hijack a new connected wireless port"
+ "UN-Mute"
+ "Unable to copy endpoint for port"
+ "Unable to find fallback port"
+ "Unable to set route sharing policy to long-form audio while AirPlaying long-form media"
+ "Unable to set routing context UUID to system music while AirPlaying long-form media"
+ "UnduckFadeDuration value is negative"
+ "Unexpected NULL shmemObject from the server"
+ "Unknown STS flavor"
+ "Unknown State"
+ "Unknown(%@)"
+ "Unknown(%u)"
+ "Updating PredictedRoute because  of '%@' event"
+ "UserIntendsToUnmute"
+ "UserIntentToUnmuteDidChange"
+ "UserPreferredInputRoute"
+ "VAEM_FallbackInputRouteEndpoint"
+ "VAE_HighQualityContentCaptureEnabled"
+ "VAE_SupportsHighQualityContentCapture"
+ "VALID"
+ "Value received for AirPlayScreenSuspended is not of type NSNumber"
+ "Value received for AllowAppToFadeInTemporarily is not of type NSString"
+ "Value received for AllowAppToInitiatePlaybackTemporarily is not of type NSString"
+ "Value received for AllowAppToInitiateRecordingTemporarily is not of type NSString"
+ "Value received for AppToInterruptCurrentNowPlayingSession is not of type NSString"
+ "Value received for AvailableForVoicePrompts is not of type NSDictionary"
+ "Value received for CallScreeningStatus is not of type NSNumber"
+ "Value received for CarSpeechStateChanged is not of type NSNumber"
+ "Value received for DownlinkMute is not of type NSNumber"
+ "Value received for DuckScalarForVoiceOver is not of type NSNumber"
+ "Value received for FullMute is not of type NSNumber"
+ "Value received for HeadphoneVolumeLimit is not of type NSNumber"
+ "Value received for InterruptAudioSessionIDForHandoff is not of type NSNumber"
+ "Value received for MakeStarkPortRoutableForPhoneCall is not of type NSNumber"
+ "Value received for MakeStarkPortRoutableForPlayingSession is not of type NSNumber"
+ "Value received for NowPlayingAppShouldResumeForCarPlay is not of type NSNumber"
+ "Value received for PickedRoute is not of type NSDictionary"
+ "Value received for PostInterruptionEndedNotification is not of type NSDictionary"
+ "Value received for RemoteDeviceIDs is not of type NSArray or nil"
+ "Value received for RouteAwayFromAirPlay is not of type NSNumber"
+ "Value received for StarkMainAudioIsOwnedByiOSButBorrowedByCar is not of type NSNumber"
+ "Value received for SubscribeToNotifications is not of type NSArray"
+ "Value received for ThermalControlInfo is not of type NSDictionary"
+ "Value received for ThermalGainAdjustment_Haptics is not of type NSNumber"
+ "Value received for ThermalGainAdjustment_Speaker is not of type NSNumber"
+ "Value received for UplinkMute is not of type NSNumber"
+ "Value received for VibeIntensity is not of type NSNumber"
+ "Value received for maximum volume limit for built-in speaker is not of type NSNumber"
+ "Value received to set for AirPods in-ear routing feature is not of type NSNumber"
+ "Vibration parameter dictionary has not been created."
+ "Vibrator is not initialized. This should not happen"
+ "Vibrator is not initialized. This should not happen when timer fires."
+ "WHA"
+ "WHAInstantDiscovery_Caching"
+ "^v20@0:8I16"
+ "^{OpaqueFigSystemController=}16@0:8"
+ "^{__CFArray=}24@0:8@16"
+ "_CMSessionMgrCopyPortDescription"
+ "_FigEndpointCentralGetEntityDoingActivity"
+ "_FigEndpointCentralSendCommand"
+ "_VAEndpointManager_CopyProperty"
+ "_VAEndpointManager_CopyPropertyForAudioDevice"
+ "_VAEndpointManager_CopyPropertyForRouteConfiguration"
+ "_VAEndpointManager_CopyPropertyForScope"
+ "_VAEndpointManager_CopyPropertyWithQualifier"
+ "_VAEndpointManager_Finalize"
+ "_VAEndpointManager_Invalidate"
+ "_VAEndpointManager_SetDiscoveryMode"
+ "_VAEndpointManager_SetProperty"
+ "_VAEndpointManager_SetPropertyForAudioDevice"
+ "_VAEndpoint_CopyProperty"
+ "_VAEndpoint_Finalize"
+ "_audioObjectID"
+ "_audioToolboxIsPlaying"
+ "_central_CopyProperty"
+ "_central_SetProperty"
+ "_clientModificationFinishedTimestamp"
+ "_clientModificationStartedTimestamp"
+ "_configurationDidFinish"
+ "_connectBannerResponse"
+ "_connectBannerResponseCache"
+ "_correlationID"
+ "_figEndpointType"
+ "_fromPorts"
+ "_hasExternalMuteNotificationContext"
+ "_isOutputMuted"
+ "_isVoiceAssistantPlayingToPersonalAudioDeviceOverMedia"
+ "_modificationMetrics"
+ "_mostRecentSessionInfoSetOnVA"
+ "_prefersBluetoothHighQualityContentCapture"
+ "_routeConfigUpdateReason"
+ "_routeSemaphore"
+ "_routingContextUtilities_addLeader"
+ "_routingContextUtilities_checkActivationTimeout"
+ "_routingContextUtilities_copyPickedEndpoints"
+ "_routingContextUtilities_notifyClientsOfChangeInPickedEndpoints"
+ "_selfWeak"
+ "_serverModificationFinishedTimestamp"
+ "_serverModificationStartedTimestamp"
+ "_shadowingAudioSessionOptions"
+ "_shouldPrivacyPongPlay"
+ "_someLongFormVideoClientIsActive"
+ "_txid"
+ "_undoBannerResponse"
+ "_undoBannerResponseCache"
+ "add fallback device"
+ "addMXCoreSessionIndependentInputAudioResource:"
+ "addMXSessionIndependentInputAudioResource:"
+ "addSessionAudioObject"
+ "allowBluetoothAccessoryToRequestAudioRoute"
+ "allowed"
+ "allowing"
+ "already"
+ "alwaysPlaysAudio"
+ "audio session ids"
+ "audioControlQueue is NULL, CMSessionMgr has not been initialized"
+ "audioObjectID"
+ "audioToolboxIsPlaying"
+ "bannerResponseToString:"
+ "cache"
+ "callConnectHaptics"
+ "canSessionsCoexistDueToMediaMultitasking:victim:"
+ "canSessionsCoexistDueToOutputMuting:victim:"
+ "cannot set reporter ID when session is active"
+ "central_BorrowScreen"
+ "central_CloseCommChannel_block_invoke"
+ "central_ConstructModeChangeRequestToGet"
+ "central_ConstructModeChangeRequestToRelease"
+ "central_CopyCurrentScreenViewArea_block_invoke"
+ "central_CopyHIDInputMode_block_invoke"
+ "central_CreateCommChannel_block_invoke"
+ "central_CreateRemoteControlSession_block_invoke"
+ "central_RequestCarUI_block_invoke"
+ "central_RequestScreenViewArea_block_invoke"
+ "central_SendData_block_invoke"
+ "central_SessionHandleInterruptionEnded"
+ "central_SessionHandleStopNow"
+ "central_SetDelegateRemoteControl_block_invoke"
+ "central_SetHIDInputMode_block_invoke"
+ "central_TakeScreen"
+ "central_UnborrowScreen"
+ "central_deactivateEndpoint"
+ "central_deactivateEndpoint_block_invoke"
+ "central_endpointNotificationCallback"
+ "central_requestCarModeChange"
+ "central_requestCarModeChange_block_invoke"
+ "cfVolumeLimit"
+ "cfVolumeMultiplier"
+ "checkRSSTrace"
+ "cleanupConnectBannerIfNeeded:routeName:"
+ "cleanupUndoBannerIfNeeded:routeName:"
+ "clearDevicesStateCache"
+ "clearLayoutRoleCache"
+ "clearUserPreferredRoute:"
+ "clientModificationFinishedTimestamp"
+ "clientModificationStartedTimestamp"
+ "cmsAddResourceToSession"
+ "cmsCopyOverrideRoute"
+ "cmsCopySubPortPreferencesAndInputOverride"
+ "cmsEnableBluetoothRecording"
+ "cmsHandleResponseFromCarMainAudioRequest"
+ "cmsRemoveAllResourcesFromSession"
+ "cmsRemoveResourceFromSession"
+ "cmsRestoreMuted"
+ "cmsSaveAndClearMuted"
+ "cmsSetCategoryOnPVMAndAudioDevice"
+ "cmsSetClientPID"
+ "cmsSetClientPriority"
+ "cmsSetDefaultBuiltInRoute"
+ "cmsSetOverrideRoute"
+ "cmsSetUpSharedAudioRoute"
+ "cmsSetVolume"
+ "cmsShouldVolumeClientTryToTakeControl"
+ "cmsUpdateAllowedRouteTypes"
+ "cmsUpdateCurrentPhoneState"
+ "cmsUpdateExcludedPortsList"
+ "cmsUpdateSessionStateForNewCategory"
+ "cmsUpdateSubPortPreferences"
+ "cmscreenHandleActivation"
+ "cmscreenHandleDeactivation"
+ "cmscreenSetCurrentState"
+ "cmsession_createCFObject"
+ "cmsmAddBTDetailsFromBTEndpointToRouteDescription"
+ "cmsmAddSystemSoundAudioCategoriesThatMixIn"
+ "cmsmAudioDeviceStartChangedCallback"
+ "cmsmBuildResourceTracker"
+ "cmsmCFDictionaryGetValueWithDefaultAsFallback"
+ "cmsmCameraShutterShouldClick"
+ "cmsmClearSystemSoundShouldPlayQueueTimerDidFinish"
+ "cmsmConvertToDecibelInVAD"
+ "cmsmCopyActiveNonWirelessPortsListForRouteConfigurationScopeAndDevice"
+ "cmsmCopyCurrentActiveRouteTypeAtIndex"
+ "cmsmCopyCurrentActiveRouteTypes"
+ "cmsmCopyCurrentActiveRoutesInfoForVADUID"
+ "cmsmCopyDefaultVADToSystemSoundVADVolumeRatios"
+ "cmsmCopyDestinationsWithoutElement"
+ "cmsmCopyNonDefaultBuiltinRouteDescriptionArrayForRouteConfiguration"
+ "cmsmCopyNonPreferredHFPRouteDescriptionArrayForRouteConfiguration"
+ "cmsmCopyPartnerPortsToMakeRoutable"
+ "cmsmCopyPickableQuiesceableWiredPortsForRouteConfiguration"
+ "cmsmCopyPickableRoutesForRouteConfiguration"
+ "cmsmCopyQuiesceableWiredPortsForRouteConfiguration"
+ "cmsmCopyQuiesceableWiredPortsRouteDescriptionArrayForRouteConfiguration"
+ "cmsmCopySelectablePortsForRouteConfiguration"
+ "cmsmCopySessionsToUnduck"
+ "cmsmCopyUpdatedVolumeOperationCategoryForNullDefaultCategory"
+ "cmsmCopyVADPickedRouteDescriptionForRouteConfiguration"
+ "cmsmCopyWirelessPortsArrayForRouteConfiguration"
+ "cmsmCopyWirelessRouteDescriptionArrayForRouteConfiguration"
+ "cmsmCreateAudioDeviceStartIdleSleepPreventor"
+ "cmsmCreateFallbackRouteDescription"
+ "cmsmCreateNonConnectedBTRouteDescription"
+ "cmsmCreatePickableRoutesForRouteConfiguration"
+ "cmsmCreateRouteDescriptionArrayForNonConnectedBT"
+ "cmsmDefaultVADToSystemSoundVADVolumeRatioForCurrentSystemSoundVADRoute"
+ "cmsmDeferFinishSystemSoundThatMustBeHeardTimerDidFinish"
+ "cmsmDoesAudioCategoryMixIn"
+ "cmsmDumpCMSessionStateToFile"
+ "cmsmGetAudioDeviceStart"
+ "cmsmGetCurrentConnectedPortToRoute"
+ "cmsmGetDeviceVolume"
+ "cmsmGetSystemSoundMaxVolume"
+ "cmsmGetSystemSoundMinVolume"
+ "cmsmGetSystemSoundVolumeScalarForSystemSoundVAD"
+ "cmsmInitializeFigVibrator"
+ "cmsmInputPortIsConnectedForRouteConfiguration"
+ "cmsmIsDeviceIDIncludedInCarBluetoothIDs"
+ "cmsmIsSessionEligibleForAirPlaySuggestions"
+ "cmsmIsSessionEligibleForPreemptivePort"
+ "cmsmItsASteveNote"
+ "cmsmLoadAudioToolboxRoutinesOnce"
+ "cmsmLoadClusterSyncMgrRoutines_block_invoke"
+ "cmsmPostVibeWillStartNotification"
+ "cmsmPrewarmAudioForSSID"
+ "cmsmReassertPreferredSampleRate"
+ "cmsmRegisterForAudioDeviceStartNotifications"
+ "cmsmReleaseAudioDeviceStartIdleSleepPreventor"
+ "cmsmRemoveExtraRouteForBTDevicesWithHFPAndA2DP"
+ "cmsmRunSystemSoundWatchdogForAppleTV"
+ "cmsmSetUpSessionAudioBehavioursDictionary"
+ "cmsmSetUpSystemSoundCategoryDictionaries"
+ "cmsmSharedAudioConnectionFailedListener"
+ "cmsmShouldUpdateMostRecentSynchronizedVolumeActivityTimestamp"
+ "cmsmSystemSoundMustBeHeard"
+ "cmsmSystemSoundShouldPlayForActivate"
+ "cmsmUnpickQuiesceableWiredPortsRoutes"
+ "cmsmUnrouteAllInputRoutes"
+ "cmsmUpdateAppsLists"
+ "cmsmUpdateAudioHardwareControlFlagsOnActiveSessions"
+ "cmsmUpdateCurrentActiveRouteTypeForSystemSound"
+ "cmsmUpdateCurrentActiveRoutesInfo"
+ "cmsmUpdateDuckVolume"
+ "cmsmVibeStoppedNotificationCallback"
+ "cmsmVibrateForSystemSoundInternal_block_invoke"
+ "cmsmVoiceOverIsOnChangedCallback_block_invoke"
+ "cmsmWordyToCompact"
+ "cmsm_IDSConnection_UpdateOtherDevicesConnectedInfoInPickableRoutesCache"
+ "cmsm_IDSServer_ProcessLocalIsPlayingDoneMessage"
+ "cmsm_IDSServer_ProcessLocalIsPlayingStartMessage"
+ "cmsm_IDSServer_ProcessRemotePlayingInfoQueryMessage"
+ "cmsmdeviceState_BatteryStateChanged"
+ "cmsmdevicestate_ButtonsCanChangeRingerVolumeChangedNotificationCallback"
+ "cmsmdevicestate_DeviceIsLocked"
+ "cmsmdevicestate_InitializeButtonsCanChangeRingerVolumePreference"
+ "cmsmdevicestate_RegisterForDeviceIsChargingNotification_block_invoke"
+ "cmsmdevicestate_RegisterForNotifydStyleNotification"
+ "cmsmdevicestate_ScreenIsBlanked"
+ "cmsmdevicestate_ScreenIsBlankedByProximitySensor"
+ "cmsmdevicestate_ScreenIsBlankedByProximitySensorChangedCallback"
+ "cmsmdevicestate_ScreenIsBlankedChangedCallback"
+ "cmsmdevicestate_UpdateItsANonUIBuild"
+ "cmsmdevicestate_UpdateRingerIsOn"
+ "cmsmdevicestate_UpdateSupportsPiP"
+ "cmsmdevicestate_UpdateVibrationDisabledFlag"
+ "cmsutility_hasAssertionsToStartMixablePlayback"
+ "cmsutility_hasAssertionsToStartMixableRecording"
+ "cmsutility_sendBeginInterruptionFailureEventToAudioStatistics"
+ "cmsutility_sendStartRecordingEventToAudioStatistics"
+ "com.apple.MediaExperience.ConnectBannerAwaitingDispatchQueue"
+ "com.apple.mediaexperience.AudioAccessoryServices"
+ "com.apple.mediaexperience.MXRoutingContextReportingRTCServiceImpl.queue"
+ "com.apple.mediaexperience.SystemSoundServicesQueue"
+ "com.apple.private.mediaexperience.useindependentinputaudioresourcesession"
+ "connectBannerResponse"
+ "connected input ports"
+ "copyActiveCoreSessionControllingRouting"
+ "copyAllMXCoreSessionList"
+ "copyAttributeForKeyMappingToFig"
+ "copyAvailableRouteControlFeatures:"
+ "copyCoreSessionsShadowingAudioSession:withOptions:"
+ "copyDeviceAddressFromVADPort:"
+ "copyDisplayIDForActiveCarPlayVideoSession"
+ "copyFigController"
+ "copyHighestPriorityLocalSession"
+ "copyIndependentInputAudioResourceSessionWithAudioSessionID:"
+ "copyMXCoreSessionIndependentInputAudioResourceList"
+ "copyMXSessionIndependentInputAudioResourceList"
+ "copyMXSystemControllerList:"
+ "copyMeasuredHDMILatencyFromDisk"
+ "copyPreferredAvailableInputPortFromCache"
+ "copyPreferredDeviceAddress:andPreemptivePortInfo:"
+ "copyPreferredDeviceAddress:bundleID:isHypotheticalQuery:reason:"
+ "copyPreferredInputPortFromConnectedPorts:"
+ "copyPrimaryAppDisplayID"
+ "copySessionRoutingInfoFromVA"
+ "copySessionWithAudioObjectID:"
+ "copySessionWithMXCoreSessionID:"
+ "copySessionsShadowingAudioSessionID:withShadowingOptions:fromSessionList:"
+ "copySessionsThatUserIntendsToUnmute:"
+ "copySetAttributeForKeyMappingToFig"
+ "copySystemAudioInputContextWithAllocator:options:context:"
+ "copyUndoEndpointsForRoute:"
+ "copyUserPreferredInputPort"
+ "copyUserPreferredRoute:"
+ "copyVADNamesFromSessionAudioBehavior"
+ "correlationID"
+ "couldn't allocate session object"
+ "deactivate"
+ "device"
+ "device name"
+ "dictionaryRepresentation"
+ "didExtractEntitlementsFromAuditToken"
+ "disallowing"
+ "discardUnavailableVADInfoFromDetailedRouteDescriptionIfNeeded:"
+ "discovererManager_getDiscoveryModeAsInt"
+ "discovererPID"
+ "discoverer_getTypeString"
+ "discoverer_postRoutePresentChangedIfNecessary_block_invoke"
+ "discoveryManager_appendAvailableEndpoints"
+ "discoveryManager_appendAvailableEndpoints_block_invoke"
+ "discoveryManager_appendAvailableSidePlayEndpoints"
+ "discoveryManager_copyHighestDiscoveryModeForDiscovererType"
+ "discoveryManager_iOSAppendAvailableEndpoints"
+ "discoveryManager_mapDiscovererTypeToEndpointFeatures"
+ "discoveryManager_removeFreedWeakRefs"
+ "discoveryManager_resetSwitchDownTime"
+ "discoveryManager_shouldSwitchDownBeDelayed"
+ "discoveryManager_shouldSwitchDownBeDelayed_block_invoke"
+ "discoveryManager_storeDiscoverer"
+ "dismissBannerWithUUID:withResponse:"
+ "dlopen failed"
+ "dlsym failed"
+ "does"
+ "doesSessionConfigurationChangeRequireOutputUnmute:oldAudioMode:"
+ "don't have"
+ "don't save"
+ "duckToLevelScalar out of range"
+ "dumpDebugConfigInfo"
+ "dumpDebugStateInfo"
+ "endpointAgentOut cannot be NULL"
+ "endpointAggregate_Activate_block_invoke"
+ "endpointAggregate_AddEndpoint_block_invoke"
+ "endpointAggregate_CopyProperty"
+ "endpointAggregate_CopyProperty_block_invoke"
+ "endpointAggregate_RemoveEndpoint_block_invoke"
+ "endpointAggregate_SendCommand_block_invoke"
+ "endpointAggregate_SendData_block_invoke"
+ "endpointAggregate_SetDelegateRemoteControl_block_invoke"
+ "endpointAggregate_SetDelegateRouting_block_invoke"
+ "endpointAggregate_SetProperty_block_invoke"
+ "endpointDisconnectionTimeInfo"
+ "endpointDisconnectionTimeInfoPrefs"
+ "endpointUIAgentHelper_UIAgentCallback"
+ "endpointUIAgentHelper_UIAgentNotificationCallback"
+ "endpointcentral_trace"
+ "endpointuiagentremote_trace"
+ "entitlement missing to set PIDToInheritAppStateFrom"
+ "err"
+ "extractAndSetAuditToken:"
+ "failed to copy remoteManagerCreationBlock"
+ "fallbackRouteDescriptor"
+ "figConnection_ServerConnectionDied_Callback"
+ "figConnection_notificationCallback"
+ "figEndpointDescriptorUtility_addAirPlayDetailsToDescriptor"
+ "figEndpointDescriptorUtility_addBTDetailsToDescriptor"
+ "figEndpointDescriptorUtility_addSidePlayDetailsToDescriptor"
+ "figEndpointDescriptorUtility_addVirtualAudioDetailsToDescriptor"
+ "figEndpointDescriptorUtility_setAirPlayFeatures"
+ "figEndpointDescriptorUtility_setAirPlayRouteSubType"
+ "figEndpointDescriptorUtility_setDescriptorKey"
+ "figEndpointType"
+ "figEndpointUIAgentRemoteXPC_Finalize"
+ "figEndpointUIAgentRemoteXPC_deviceWakeStatus"
+ "figEndpointUIAgentRemoteXPC_setIsCurrentUIAgent"
+ "figEndpointUIAgent_Invalidate"
+ "figEndpointUIAgent_copyPasswordFromKeychain"
+ "figEndpointUIAgent_setAuthValue"
+ "figEndpointUIAgent_setPasswordFromKeychain"
+ "figRouteDiscovererRemoteXPC_EnsureClientEstablished_block_invoke"
+ "figRouteDiscovererXPCHandleCopyAvailableRoutesMessage"
+ "figsystemcontroller_trace"
+ "figsystemcontrollerremote_trace"
+ "figsystemcontrollerserver_trace"
+ "finalizeAudioAccessoryConnection"
+ "follow VAD UID"
+ "frcXPCServer_logEndpoints"
+ "fromPorts"
+ "fsc_createPropertyMappingDicts_block_invoke"
+ "fsm_getFigStarkModeConstraintEncodingFromCFArray"
+ "fsm_getFigStarkModeTransferPriorityEncodingFromCFArray"
+ "fsm_getFigStarkModeTransferTypeEncodingFromCFString"
+ "fsm_postCarPlayVideoActiveNotification"
+ "fsm_requestResourceModeChange"
+ "fsm_requestResourceModeChangeUnborrow"
+ "fsm_setupStarkModeActionMap"
+ "fsm_translateModeChangeActionDict"
+ "fsm_translateModeRequestDict"
+ "fsm_translatePreviousOrCurrentModeDict"
+ "fvGetVibeSynthIsAvailable"
+ "getAudioSessionID:forAttributedPID:"
+ "getAudioTrackStatus"
+ "getAudioTrackStatusAsString:"
+ "getAwaitingDispatchQueue"
+ "getConnectBannerResponseCache"
+ "getCurrentOutputPort"
+ "getHostProcessAttributions:"
+ "getIsPlayerMuted"
+ "getIsPlayingVideoOutput"
+ "getLayoutRoleForDisplayID:layoutRole:"
+ "getSessionIDFromAudioObject"
+ "getShadowingAudioSessionOptionsAsString:"
+ "getSharedBannerClient"
+ "handleBTNotificationAudioRoutingChange"
+ "handleNewWirelessPortConnected:"
+ "handlePortDisconnected:"
+ "handleServerDeath"
+ "handleUserIntentToUnmute:"
+ "has NO"
+ "hasAudioTrack"
+ "hasExternalMuteNotificationContext"
+ "hasExternalMuteNotificationContext ="
+ "have"
+ "hijackWirelessPort:reason:portWentInEar:"
+ "i20@0:8C16"
+ "i28@0:8I16@?20"
+ "i28@0:8^I16i24"
+ "i32@0:8@16^B24"
+ "i68@0:8{MXSessionPlayingInfo=@@IIBBBB@@}16B64"
+ "indexOfObject:"
+ "initWithCorrelationID:"
+ "initWithFigEndpointType:"
+ "initWithInteger:"
+ "initWithModificationMetrics:useMockService:"
+ "initWithRouteConfigUpdatedReason:modificationMetrics:"
+ "initWithRoutingContext:routeConfigUpdateID:correlationID:callback:context:"
+ "initWithSessionInfo:userInfo:frameworksToCheck:"
+ "initializeAttributeForKeyMappingToFig"
+ "initializeAudioAccessoryConnection"
+ "input_picker"
+ "integerValue"
+ "interruptAllIndependentInputAudioResourceSessions:interruptorName:"
+ "interruptAllIndependentInputAudioResourceSessionsIfNeeded:"
+ "interruptIndpendentInputAudioResourceSession:interruptorBundleID:interruptorName:fadeDuration:waitingToResume:"
+ "invalid endpoint in the array"
+ "invalid param"
+ "invalidated"
+ "ios_high_quality_local_recording"
+ "is"
+ "is no longer"
+ "isActiveDeviceWithValidSessionID:"
+ "isAnyConnectBannerActive"
+ "isAnyManagedDeviceConnected"
+ "isAppInPiP:"
+ "isAppInSplitView:"
+ "isCarPlayPortRoutableFromCustomizedRoutingPerspective:"
+ "isCurrentRouteHeadphoneAndInEar:"
+ "isEligibleForOutputMuting"
+ "isMediaSession"
+ "isOutputMuted"
+ "isOutputMuted ="
+ "isPortHeadphoneWithInEarDetectionSupported:"
+ "isPortManaged:"
+ "isRecordingMuted ="
+ "isRecordingWithBTManagedDevice"
+ "isSessionConfigurationEligibleForOutputMuting:audioMode:"
+ "isSharePlayCallSession needs to have IsSharePlayCapableCallSession set"
+ "isSharePlayCallSession needs to have phone call behavior"
+ "isSupported"
+ "isUsingBuiltInMic"
+ "isVoiceAssistantPlayingToPersonalAudioDeviceOverMedia"
+ "isn't"
+ "kAVAudioCategory_Alarm"
+ "kAVAudioCategory_Alert"
+ "kAVAudioCategory_AudioVideo"
+ "kAVAudioCategory_CalendarAlert"
+ "kAVAudioCategory_CameraShutter"
+ "kAVAudioCategory_ConnectedToPower"
+ "kAVAudioCategory_EmergencyAlert"
+ "kAVAudioCategory_EmergencyAlert_Muteable"
+ "kAVAudioCategory_FailedUnlock"
+ "kAVAudioCategory_FindMyPhone"
+ "kAVAudioCategory_Headset_AnswerCall"
+ "kAVAudioCategory_Headset_CallWaitingActions"
+ "kAVAudioCategory_Headset_EndCall"
+ "kAVAudioCategory_Headset_Redial"
+ "kAVAudioCategory_Headset_StartCall"
+ "kAVAudioCategory_Headset_TransitionEnd"
+ "kAVAudioCategory_KeyPressClickPreview"
+ "kAVAudioCategory_KeyPressed"
+ "kAVAudioCategory_LowPower"
+ "kAVAudioCategory_MailReceived"
+ "kAVAudioCategory_MailSent"
+ "kAVAudioCategory_PINKeyPressed"
+ "kAVAudioCategory_PhoneCall"
+ "kAVAudioCategory_PlayAndRecord"
+ "kAVAudioCategory_RadioPresetAdded"
+ "kAVAudioCategory_Record"
+ "kAVAudioCategory_ReminderAlert"
+ "kAVAudioCategory_RingerSwitchIndication"
+ "kAVAudioCategory_RingerVibeChanged"
+ "kAVAudioCategory_Ringtone"
+ "kAVAudioCategory_RingtonePreview"
+ "kAVAudioCategory_SIMToolkitTone"
+ "kAVAudioCategory_SMSReceived"
+ "kAVAudioCategory_SMSReceived_Alert"
+ "kAVAudioCategory_SMSReceived_Selection"
+ "kAVAudioCategory_SMSReceived_Vibrate"
+ "kAVAudioCategory_SMSSent"
+ "kAVAudioCategory_ScreenLocked"
+ "kAVAudioCategory_SilentVibeChanged"
+ "kAVAudioCategory_SystemSoundPreview"
+ "kAVAudioCategory_SystemSoundPreview_IgnoreRingerSwitch"
+ "kAVAudioCategory_SystemSoundPreview_IgnoreRingerSwitch_NoVibe"
+ "kAVAudioCategory_TTYCall"
+ "kAVAudioCategory_TouchTone"
+ "kAVAudioCategory_USSDAlert"
+ "kAVAudioCategory_Voicemail"
+ "kAVAudioCategory_VoicemailGreeting"
+ "kAVAudioCategory_VoicemailReceived"
+ "kAVAudioRoute_AirPlayLowLatency"
+ "kAVAudioRoute_AirTunes"
+ "kAVAudioRoute_AllRoutes"
+ "kAVAudioRoute_BestSpeaker"
+ "kAVAudioRoute_BestSpeakerAndMicrophone"
+ "kAVAudioRoute_BluetoothLEOutput"
+ "kAVAudioRoute_Broadcast"
+ "kAVAudioRoute_DisplayPort"
+ "kAVAudioRoute_HDMI"
+ "kAVAudioRoute_Headphone"
+ "kAVAudioRoute_HeadphonesAndMicrophone"
+ "kAVAudioRoute_HeadphonesBT"
+ "kAVAudioRoute_Headset"
+ "kAVAudioRoute_HeadsetBT"
+ "kAVAudioRoute_HeadsetInOut"
+ "kAVAudioRoute_LineIn"
+ "kAVAudioRoute_LineInOut"
+ "kAVAudioRoute_LineOut"
+ "kAVAudioRoute_MicrophoneBluetooth"
+ "kAVAudioRoute_MicrophoneBuiltIn"
+ "kAVAudioRoute_MicrophoneWired"
+ "kAVAudioRoute_None"
+ "kAVAudioRoute_PersistentLineOut"
+ "kAVAudioRoute_Receiver"
+ "kAVAudioRoute_ReceiverAndMicrophone"
+ "kAVAudioRoute_SPDIF"
+ "kAVAudioRoute_Speaker"
+ "kAVAudioRoute_SpeakerAndMicrophone"
+ "kAVAudioRoute_TTY"
+ "kAVAudioRoute_USB"
+ "kAVAudioRoute_USBInput"
+ "kBluetoothAudioDeviceFeatureStudioMicInput"
+ "kCMBaseObjectError_AllocationFailed"
+ "kCMBaseObjectError_Invalidated"
+ "kCMBaseObjectError_ParamErr"
+ "kCMBaseObjectError_PropertyNotFound"
+ "kCMSessionAudioCategory_Alarm"
+ "kCMSessionAudioCategory_Alert"
+ "kCMSessionAudioCategory_AudioVideo"
+ "kCMSessionAudioCategory_CalendarAlert"
+ "kCMSessionAudioCategory_CameraShutter"
+ "kCMSessionAudioCategory_ConnectedToPower"
+ "kCMSessionAudioCategory_EmergencyAlert"
+ "kCMSessionAudioCategory_EmergencyAlert_Muteable"
+ "kCMSessionAudioCategory_FailedUnlock"
+ "kCMSessionAudioCategory_FindMyPhone"
+ "kCMSessionAudioCategory_Headset_AnswerCall"
+ "kCMSessionAudioCategory_Headset_CallWaitingActions"
+ "kCMSessionAudioCategory_Headset_EndCall"
+ "kCMSessionAudioCategory_Headset_Redial"
+ "kCMSessionAudioCategory_Headset_StartCall"
+ "kCMSessionAudioCategory_Headset_TransitionEnd"
+ "kCMSessionAudioCategory_KeyPressClickPreview"
+ "kCMSessionAudioCategory_KeyPressed"
+ "kCMSessionAudioCategory_LowPower"
+ "kCMSessionAudioCategory_MailReceived"
+ "kCMSessionAudioCategory_MailSent"
+ "kCMSessionAudioCategory_PINKeyPressed"
+ "kCMSessionAudioCategory_PhoneCall"
+ "kCMSessionAudioCategory_PlayAndRecord"
+ "kCMSessionAudioCategory_RadioPresetAdded"
+ "kCMSessionAudioCategory_Record"
+ "kCMSessionAudioCategory_ReminderAlert"
+ "kCMSessionAudioCategory_RingerSwitchIndication"
+ "kCMSessionAudioCategory_RingerVibeChanged"
+ "kCMSessionAudioCategory_Ringtone"
+ "kCMSessionAudioCategory_RingtonePreview"
+ "kCMSessionAudioCategory_SIMToolkitTone"
+ "kCMSessionAudioCategory_SMSReceived"
+ "kCMSessionAudioCategory_SMSReceived_Alert"
+ "kCMSessionAudioCategory_SMSReceived_Selection"
+ "kCMSessionAudioCategory_SMSReceived_Vibrate"
+ "kCMSessionAudioCategory_SMSSent"
+ "kCMSessionAudioCategory_ScreenLocked"
+ "kCMSessionAudioCategory_SilentVibeChanged"
+ "kCMSessionAudioCategory_SystemSoundPreview"
+ "kCMSessionAudioCategory_SystemSoundPreview_IgnoreRingerSwitch"
+ "kCMSessionAudioCategory_SystemSoundPreview_IgnoreRingerSwitch_NoVibe"
+ "kCMSessionAudioCategory_TTYCall"
+ "kCMSessionAudioCategory_TouchTone"
+ "kCMSessionAudioCategory_USSDAlert"
+ "kCMSessionAudioCategory_Voicemail"
+ "kCMSessionAudioCategory_VoicemailGreeting"
+ "kCMSessionAudioCategory_VoicemailReceived"
+ "kCMSessionError_AllocationFailed"
+ "kCMSessionError_InvalidParameter"
+ "kCMSessionError_MissingRequiredParameter"
+ "kCMSessionError_OperationDenied"
+ "kCMSessionError_OperationDenied_CurrentlyPlaying"
+ "kCMSessionError_OperationDenied_MissingEntitlement"
+ "kCMSessionError_OperationIgnored"
+ "kFigEndpointError_AllocationFailed"
+ "kFigEndpointError_InvalidParameter"
+ "kFigEndpointError_NotFound"
+ "kFigEndpointManagerError_AllocationFailed"
+ "kFigEndpointManagerError_InvalidParameter"
+ "kFigEndpointUIAgentError_InvalidParameter"
+ "kFigEndpointUIAgentError_ServerConnectionFailed"
+ "kFigRouteDiscovererError_InvalidParameter"
+ "kFigRouteDiscovererError_ServerConnectionLost"
+ "kFigRoutingContextError_AllocationFailed"
+ "kFigRoutingContextError_FetchSystemContextUnentitled"
+ "kFigRoutingContextError_InvalidParameter"
+ "kFigRoutingContextError_InvalidState"
+ "kFigRoutingContextError_ServerConnectionLost"
+ "kFigRoutingSessionManagerError_AllocationFailed"
+ "kFigRoutingSessionManagerError_InvalidParameter"
+ "kFigRoutingSessionManagerError_MissingEntitlement"
+ "kFigRoutingSessionManagerError_ServerConnectionLost"
+ "kFigSTSError_InternalError"
+ "kFigSTSError_InvalidParameter"
+ "kFigSTSError_ServerConnectionLost"
+ "kFigSTSError_UnknownFlavor"
+ "kFigStarkModeError_InvalidParameter"
+ "kFigStarkModeError_ServerConnectionLost"
+ "kFigSystemControllerError_AllocationFailed"
+ "kFigSystemControllerError_InvalidParameter"
+ "kFigSystemControllerError_ServerConnectionLost"
+ "kFigVibratorError_Device"
+ "kFigVibratorError_MemFullErr"
+ "kFigVibratorError_NotInitialized"
+ "kFigVibratorError_ParamErr"
+ "kFigVolumeControllerError_InvalidParameter"
+ "kFigVolumeControllerError_ServerConnectionLost"
+ "kMXAudioRoute_AirPlayLowLatency"
+ "kMXAudioRoute_AirTunes"
+ "kMXAudioRoute_AllRoutes"
+ "kMXAudioRoute_BestSpeaker"
+ "kMXAudioRoute_BestSpeakerAndMicrophone"
+ "kMXAudioRoute_BluetoothLEOutput"
+ "kMXAudioRoute_Broadcast"
+ "kMXAudioRoute_DisplayPort"
+ "kMXAudioRoute_HDMI"
+ "kMXAudioRoute_Headphone"
+ "kMXAudioRoute_HeadphonesAndMicrophone"
+ "kMXAudioRoute_HeadphonesBT"
+ "kMXAudioRoute_Headset"
+ "kMXAudioRoute_HeadsetBT"
+ "kMXAudioRoute_HeadsetInOut"
+ "kMXAudioRoute_LineIn"
+ "kMXAudioRoute_LineInOut"
+ "kMXAudioRoute_LineOut"
+ "kMXAudioRoute_MicrophoneBluetooth"
+ "kMXAudioRoute_MicrophoneBuiltIn"
+ "kMXAudioRoute_MicrophoneWired"
+ "kMXAudioRoute_None"
+ "kMXAudioRoute_PersistentLineOut"
+ "kMXAudioRoute_Receiver"
+ "kMXAudioRoute_ReceiverAndMicrophone"
+ "kMXAudioRoute_SPDIF"
+ "kMXAudioRoute_Speaker"
+ "kMXAudioRoute_SpeakerAndMicrophone"
+ "kMXAudioRoute_TTY"
+ "kMXAudioRoute_USB"
+ "kMXAudioRoute_USBInput"
+ "kMXError_AllocationFailed"
+ "kMXError_InvalidParameter"
+ "kMXError_MissingRequiredParameter"
+ "kMXError_OperationDenied_MissingEntitlement"
+ "kMXError_UnrecognizedProperty"
+ "kMXSessionError_InvalidParameter"
+ "kMXSessionError_MissingRequiredParameter"
+ "kMXSessionError_OperationDenied"
+ "kMXSessionError_OperationFailed"
+ "kMXSystemControllerError_InvalidParameter"
+ "kMXSystemControllerError_OperationDenied_MissingEntitlement"
+ "kPVMError_AllocationFailed"
+ "kRTCReportingMessageParametersCategory"
+ "kRTCReportingMessageParametersPayload"
+ "kRTCReportingMessageParametersType"
+ "kRTCReportingSessionInfoBatchEvent"
+ "kRTCReportingSessionInfoClientBundleID"
+ "kRTCReportingSessionInfoClientType"
+ "kRTCReportingSessionInfoClientVersion"
+ "kRTCReportingSessionInfoSessionID"
+ "kRTCReportingUserInfoClientName"
+ "kRTCReportingUserInfoServiceName"
+ "layoutChanged:"
+ "loud"
+ "mAudioRoutingRequest"
+ "mAudioTrackStatus"
+ "mBTNotificationAudioRoutingChangedToken"
+ "mBTNotificationPreemptivePortChangedToken"
+ "mBTNotificationPreemptivePortDisconnectedToken"
+ "mConfigurationCondition"
+ "mConfigured"
+ "mCorrelationID"
+ "mDevicesState"
+ "mDisplayLayoutCache"
+ "mDisplayLayoutCacheLock"
+ "mFrontBoardServicesMonitor"
+ "mIsPlayerMuted"
+ "mIsPlayingVideoOutput"
+ "mMXCoreSessionIndependentInputAudioResourceList"
+ "mMXCoreSessionIndependentInputAudioResourceListLock"
+ "mMXSessionIndependentInputAudioResourceList"
+ "mMXSessionIndependentInputAudioResourceListLock"
+ "mPortToDeviceAddressMapping"
+ "mRTCReporting"
+ "mReportingServiceImpl"
+ "mRoutingContextModificationMetrics"
+ "mUserPreferredRouteCache"
+ "mUserPreferredRouteCacheLock"
+ "mWorkQueue"
+ "medium"
+ "modificationMetrics"
+ "mostRecentSessionInfoSetOnVA"
+ "muteOutputForSession:"
+ "mxFigStarkModeController_GetCurrentMode"
+ "mxFigStarkModeController_RequestInitialModeChange"
+ "mxFigStarkModeController_RequestModeChange"
+ "mxSessionOut cannot be NULL"
+ "mxSystemMirroring_iOSHandleFigEndpointFeaturesActivation"
+ "mx_runningBoardServices_getHostProcessIDForProcessID"
+ "mxsRefreshCoreSession"
+ "mxsc_fetchCanInheritApplicationStateFromOtherProcesses"
+ "mxsmInteruptionActionMapper_setUpInterruptionPriorityDictionaries_block_invoke"
+ "newPortNeedsToShowBanner:newPortIdentifier:newPortType:previousPort:"
+ "nil or non-CFBoolean HasExternalMuteNotificationContext"
+ "no property key"
+ "no refcon"
+ "non-Boolean DisallowAudioFormatChanges value"
+ "non-Boolean EnableBluetoothRecording"
+ "non-Boolean IsEligibleForNowPlayingAppConsideration"
+ "non-Boolean IsSharedAVAudioSessionInstance"
+ "non-CFArray AllowedRouteTypes"
+ "non-CFArray SubscribeToNotifications"
+ "non-CFArray preferredPersistentRoute InputPortsUIDs"
+ "non-CFArray preferredPersistentRoute OutputPortsUIDs"
+ "non-CFArray reporterIDs"
+ "non-CFBoolean AirPlayScreenSuspended"
+ "non-CFBoolean AirPlayVideoIsActive"
+ "non-CFBoolean AllowMixableAudioWhileRecording"
+ "non-CFBoolean AudioOnlyAirPlayVideoIsActive"
+ "non-CFBoolean AudioToolboxIsPlaying"
+ "non-CFBoolean AudioTrackStatus"
+ "non-CFBoolean CarSpeechStateChanged"
+ "non-CFBoolean CurrentlyPlayingContentIsEligibleForSpatialization"
+ "non-CFBoolean DoNotResetAudioCategoryOnNextInactive"
+ "non-CFBoolean DoesInterAppAudio"
+ "non-CFBoolean DoesntActuallyPlayAudio"
+ "non-CFBoolean DownlinkMute"
+ "non-CFBoolean ForceSoundCheckOn"
+ "non-CFBoolean IAmHardwareSafetySession"
+ "non-CFBoolean IAmIDSMXCoreSession"
+ "non-CFBoolean IAmPiP"
+ "non-CFBoolean IAmStark"
+ "non-CFBoolean IAmTheAssistant"
+ "non-CFBoolean IAmWiredStark"
+ "non-CFBoolean IsAirPlayReceiverSession"
+ "non-CFBoolean IsAudioSession"
+ "non-CFBoolean IsFigInstantiatedAudioSession"
+ "non-CFBoolean IsOutputMuted"
+ "non-CFBoolean IsPlayerMuted"
+ "non-CFBoolean IsPlaying"
+ "non-CFBoolean IsPlayingOutput"
+ "non-CFBoolean IsPlayingVideoOutput"
+ "non-CFBoolean IsRecording"
+ "non-CFBoolean IsRecordingMuted"
+ "non-CFBoolean IsRecordingMutedForRemoteDevice"
+ "non-CFBoolean IsSharePlayCapableCallSession"
+ "non-CFBoolean IsUsingBuiltInMicForRecording"
+ "non-CFBoolean IsUsingCamera"
+ "non-CFBoolean MakeStarkPortRoutableForPhoneCall"
+ "non-CFBoolean MakeStarkPortRoutableForPlayingSession"
+ "non-CFBoolean MutesAudioBasedOnRingerSwitchState"
+ "non-CFBoolean NeedsAudioBudget"
+ "non-CFBoolean NowPlayingAppShouldResumeForCarPlay"
+ "non-CFBoolean OptOutOfMutePriority"
+ "non-CFBoolean PreferredDecoupledInputOutput"
+ "non-CFBoolean PrefersBeingInterruptedByNextActiveRecordingClient"
+ "non-CFBoolean PrefersBluetoothAccessoryMuting"
+ "non-CFBoolean PrefersBluetoothHighQualityContentCapture"
+ "non-CFBoolean PrefersEchoCancelledInput"
+ "non-CFBoolean PrefersNoDucking"
+ "non-CFBoolean PrefersNoInterruptions"
+ "non-CFBoolean PrefersNoInterruptionsByMixableSessions"
+ "non-CFBoolean PrefersNoInterruptionsDuringRemoteDeviceControl"
+ "non-CFBoolean PrefersSpeechDetectEnabled"
+ "non-CFBoolean PrefersSuppressingRecordingState"
+ "non-CFBoolean PrefersToInterruptActiveRecordingSessions"
+ "non-CFBoolean PrefersToOptOutOfHardwareSafetyInterruptions"
+ "non-CFBoolean PrefersToPlayDuringWombat"
+ "non-CFBoolean PrefersToTakeHWControlFlagsFromAnotherSession"
+ "non-CFBoolean PrefersToVibeWhenVibrationsAreDisabled"
+ "non-CFBoolean RequiresAggregatedInputOutput"
+ "non-CFBoolean StarkMainAudioIsOwnedByiOSButBorrowedByCar"
+ "non-CFBoolean UplinkMute"
+ "non-CFBoolean UserMuted"
+ "non-CFBoolean VibratorOn"
+ "non-CFBoolean WantsAutomaticClusterPairingOnPlaybackStart"
+ "non-CFBoolean WantsToBeVolumeButtonClient"
+ "non-CFBoolean WantsToSendResumableEndInterruptionWhenBackgrounded"
+ "non-CFBoolean WantsVibrationNotifications"
+ "non-CFBoolean WantsVolumeChangesWhenPaused"
+ "non-CFBoolean WantsVolumeChangesWhenPausedOrInactive"
+ "non-CFBoolean _HapticEngineIsPlaying"
+ "non-CFBoolean _MXSessionIsPlaying"
+ "non-CFBoolean allowSystemSoundsWhileRecording"
+ "non-CFBoolean doNotNotifyOtherSessionsOnNextInactive;"
+ "non-CFBoolean isEligibleForBTSmartRoutingConsideration"
+ "non-CFBoolean isEligibleForBTTriangleConsideration"
+ "non-CFBoolean isSharePlayCallSession"
+ "non-CFBoolean isSharePlayMediaSession"
+ "non-CFBoolean prefersConcurrentAirPlayAudio"
+ "non-CFBoolean prefersNoInterruptionWhenSecureMicrophoneIsEngaged"
+ "non-CFBoolean prefersNoInterruptionsByRingtonesAndAlerts"
+ "non-CFBoolean temporaryAssertionEnabled"
+ "non-CFBoolean value for RouteAwayFromAirPlay"
+ "non-CFBoolean wantsToPauseSpokenAudio"
+ "non-CFBoolean/non-CFNumberRef DoesSessionActuallyPlayAudio"
+ "non-CFData AuditToken"
+ "non-CFData CaptureOrientationOverride"
+ "non-CFDictionary AvailableForVoicePrompts"
+ "non-CFDictionary CurrentlyPlayingFormatInfo_BufferedAudio"
+ "non-CFDictionary CurrentlyPlayingSourceFormatInfo"
+ "non-CFDictionary PowerProfile"
+ "non-CFDictionary ShadowingAudioSessionOptions"
+ "non-CFDictionary SourceFormatInfo"
+ "non-CFDictionary UserVolumeWithRefCon"
+ "non-CFDictionary preferredPersistentRoute"
+ "non-CFDictionary routeDescription"
+ "non-CFDictionary thermalControlInfo"
+ "non-CFNumber AudioHardwareControlFlags"
+ "non-CFNumber AudioSessionID"
+ "non-CFNumber ClientPID"
+ "non-CFNumber ClientPriority"
+ "non-CFNumber ClientType"
+ "non-CFNumber CoreSessionID"
+ "non-CFNumber DuckFadeDuration"
+ "non-CFNumber DuckToLevelDB"
+ "non-CFNumber HeadphoneVolumeLimit"
+ "non-CFNumber InputDataSource"
+ "non-CFNumber InterruptionFadeDuration"
+ "non-CFNumber InterruptionStyle"
+ "non-CFNumber OrientationOverride"
+ "non-CFNumber OutputDataDestination"
+ "non-CFNumber PreferredAudioHardwareBufferFrames"
+ "non-CFNumber PreferredAudioHardwareIODuration"
+ "non-CFNumber PreferredInputSampleRate"
+ "non-CFNumber PreferredOutputSampleRate"
+ "non-CFNumber ShadowingAudioSessionID"
+ "non-CFNumber UnduckFadeDuration"
+ "non-CFNumber UserVolume"
+ "non-CFNumber duckToLevelScalar"
+ "non-CFNumber portIDRef"
+ "non-CFNumber preferredNumberOfInputChannels"
+ "non-CFNumber preferredNumberOfOutputChannels"
+ "non-CFNumber preferredStereoInputOrientation"
+ "non-CFNumber routingSharingPolicy"
+ "non-CFNumber thermalGainAdjustment_Haptics intensity"
+ "non-CFNumber thermalGainAdjustment_Speaker intensity"
+ "non-CFNumber unduckToLevelScalar"
+ "non-CFNumber vibe intensity"
+ "non-CFNumber/non-CFBoolean HandsOverInterruptionsToInterruptor"
+ "non-CFString AllowAppToFadeInTemporarily"
+ "non-CFString AllowAppToInitiatePlaybackTemporarily"
+ "non-CFString AppToInterruptCurrentNowPlayingSession"
+ "non-CFString BestAvailableContentType"
+ "non-CFString clientName"
+ "non-CFString routingContextUUID"
+ "non-NSNumber ConstantOutputVolumeLevelDB"
+ "non-NSNumber PIDToInheritAppStateFrom"
+ "non-NSNumber PreferredMinimumMicrophoneIndicatorLightOnTime"
+ "non-NSNumber audioSessionID"
+ "non-NSNumber shadowingOptions"
+ "non-array AuditTokensForProcessAssertions"
+ "non-array ReporterIDs"
+ "non-array deselected inputs"
+ "non-array hostProcessAttribution"
+ "non-array port overrides"
+ "non-array selected inputs"
+ "non-array selected outputs"
+ "non-boolean create speaker device"
+ "non-data AuditToken"
+ "non-dictionary VP block configuration"
+ "non-dictionary cameraparameters description"
+ "non-integer mode"
+ "non-number ClientPID"
+ "non-number CoreSessionID"
+ "non-number IsRecordingMuted"
+ "non-number audioToolboxIsPlaying"
+ "non-number enableBluetoothRecording"
+ "non-number interruption style"
+ "non-number isPlaying"
+ "non-number isRecording"
+ "non-number prefersEchoCancelledInput"
+ "non-string AudioCategory"
+ "non-string AudioMode"
+ "non-string ClientName"
+ "non-string DefaultBuiltInRoute"
+ "non-string audio mode"
+ "non-string propertyKey"
+ "not allowed"
+ "not muted"
+ "not resumed"
+ "notificationTimestamp"
+ "notificationUUID"
+ "numberWithUnsignedChar:"
+ "nw_path_uses_interface_type"
+ "objc_getClass failed"
+ "options cannot be NULL"
+ "outEndpoint in NULL"
+ "outFallbackRouteDescriptor must be non-nil"
+ "outManager in NULL"
+ "playPrivacyPongSound"
+ "playSystemSound:completionBlock:"
+ "populateAdditiveRoutingInfoWithBTRecordingCustomizations:"
+ "populateAdditiveRoutingInfoWithDefaultBuiltInRouteCustomization:"
+ "populateAdditiveRoutingInfoWithEchoCancelledInput:"
+ "populateAdditiveRoutingInfoWithFollowingVADInformation:inputOnly:"
+ "populateAdditiveRoutingInfoWithRouteControlFeatures:"
+ "populateVirtualAudioDeviceInfoFromSessionAudioBehaviors:newVADIDToNameMap:"
+ "portID = 0"
+ "postInterruptionCommandForAudioSessionID:sessionID:interruptiondCmd:interruptionInfo:"
+ "postInterruptionCommandNotification:interruptionCommand:interruptorName:interruptorBundleID:status:volumeChangeDuration:"
+ "postSessionNotification:payload:"
+ "postStopCommandToShadowingSessionsForSession:withShadowingOptions:"
+ "postStopCommandToShadowingSessionsForSession:withShadowingOptions:interruptor:waitingToResume:"
+ "preferHeadphonesOverCarsAndSpeakersEnabled"
+ "preferredNumber of channels can't be < 0 or > maxnumberOfChannels"
+ "preferredNumber of channels can't be <0 or > maxnumberOfChannels"
+ "prefersBluetoothHighQualityContentCapture"
+ "prefersNoInterruptionsByMixableSessions is only valid for sessions using the spokenAudio mode"
+ "prepareSessionActivationBeforeACQDispatch:"
+ "primary"
+ "processActiveDevice:"
+ "processName"
+ "processOnDemandVADLossIfNeeded:isPreviousInputVADOnDemand:"
+ "processSessionRoutingInfo:"
+ "processSessionRoutingInfoDidChange"
+ "promptForConnectDialog:withIconType:callbackHandler:"
+ "promptForUndoBanner:withIconType:callbackHandler:"
+ "promptUserResponseForRoute:newPortIdentifier:newPortName:newPortID:newPortType:newWirelessPorts:oldPort:activatingEndpoint:routingContext:connectHandler:"
+ "promptUserResponseForUndoRoute:newPortIdentifier:newPortName:newPortID:newPortType:oldPort:routingContext:undoHandler:"
+ "propertiesToSet is nil"
+ "pvmAdd100dBVolumeLimitChangedListener"
+ "pvmApplierFunction_CopyValidatedVolumes"
+ "pvmApplierFunction_ValidateVolumesForRoute"
+ "pvmComputeSystemSoundVolumeMultiplier"
+ "pvmCopyMappedCategoryAndMode"
+ "pvmCreateCategoryStringWithModeAppended"
+ "pvmCreateSeparateCategoryAndModeStrings"
+ "pvmDoesCategoryStringIncludeMode"
+ "pvmEndpointTypeInfoCleanup"
+ "pvmGet100dBVolumeLimit"
+ "pvmGetCurrentVolumeLimitForRoute"
+ "pvmGetDefaultVolume"
+ "pvmGetMappedBluetoothRouteWithDeviceIDAppended"
+ "pvmGetMappedCategoryWithModeAppended"
+ "pvmGetMaximumCategoryVolume"
+ "pvmGetMinimumCategoryVolume"
+ "pvmGetMostRecentSynchronizedVolumeActivityTimestampPref"
+ "pvmGetUpdatedDeviceIDForAirPlayRoute"
+ "pvmGetVolumeLimitPref"
+ "pvmGetVolumeMultiplierPref"
+ "pvmGetVolumePref"
+ "pvmPerformOneTimeCleanupOfAirPlayLowLatencyVolumes"
+ "pvmPerformOneTimeCleanupOfAirPlayVolumes"
+ "pvmPerformOneTimeCleanupOfBluetoothVolumes"
+ "pvmRawVolumeToVolume"
+ "pvmReassertAllPreferredVolumesForRoute"
+ "pvmReassertVolume"
+ "pvmSetCurrentRouteInfo"
+ "pvmSetMostRecentSynchronizedVolumeActivityTimestampPref"
+ "pvmSetSystemSoundVolumeMultiplierForVolumeGuts"
+ "pvmSetSystemSoundVolumeMultiplierPref"
+ "pvmSetVolumeLimitPref"
+ "pvmSetVolumePref"
+ "pvmSetVolumePreferenceInternal"
+ "pvmUpdatePreferredVolumeAndLimit"
+ "pvmVolumeToRawVolume"
+ "reapplyDeviceSampleRateAndBufferSizeOnVADIfNeeded"
+ "region_ShouldSetVolumeLimit"
+ "remoteFigStarkModeController_EnsureClientEstablished"
+ "remoteSTS_Finalize"
+ "remoteSTS_GetObjectID"
+ "remoteSystemController_EnsureClientEstablished"
+ "remoteSystemController_GetAudioSessionIDForAttributedPID"
+ "remoteSystemController_SetProperty"
+ "remoteSystemController_getObjectID"
+ "remoteXPCFigRoutingContext_HandleClientMessage"
+ "remoteXPCRouteDiscovererClient_DeadConnectionCallback"
+ "remoteXPCRouteDiscoverer_CopyAvailableEndpoints_block_invoke"
+ "remoteXPCRouteDiscoverer_CreateInternal"
+ "remoteXPCRouteDiscoverer_GetObjectID"
+ "remoteXPCRoutingContext_CreateInternal"
+ "remoteXPCRoutingContext_DeadConnectionCallback_block_invoke"
+ "remoteXPCRoutingContext_GetObjectID"
+ "remoteXPCRoutingContext_handleCompletionCallback_block_invoke"
+ "remoteXPCStarkModeController_GetObjectID"
+ "remoteXPCendpointAgent_GetObjectID"
+ "removeMXCoreSessionIndependentInputAudioResource:"
+ "removeMXSessionIndependentInputAudioResource:"
+ "removeSessionAudioObject"
+ "requiresExclaveSensor"
+ "resetIsRecordingState"
+ "resetMXSessionIsPlayingStates"
+ "resetMXSessionIsRecordingStates"
+ "resumeAllIndependentInputAudioResourceSessions:interruptorBundleID:interruptorName:"
+ "resumeAllIndependentInputAudioResourceSessionsShadowing:withShadowingOptions:interruptor:status:"
+ "resumeIndependentInputAudioResourceSession:interruptorBundleID:interruptorName:status:fadeDuration:"
+ "resumeInterruptedIndependentInputAudioResourceSessionsIfNeeded:"
+ "resumed"
+ "routeSemaphore"
+ "routeToBTDeviceIfNeeded:"
+ "routediscovererserver_trace"
+ "routes_logEndpoints"
+ "routingContextRemoteXPC_AddToSelectedRouteDescriptors"
+ "routingContextRemoteXPC_AddToSelectedRoutes"
+ "routingContextRemoteXPC_CopyProperty"
+ "routingContextRemoteXPC_EnsureClientEstablished"
+ "routingContextRemoteXPC_EnsureClientEstablished_block_invoke"
+ "routingContextRemoteXPC_RemoveFromSelectedRouteDescriptors"
+ "routingContextRemoteXPC_RemoveFromSelectedRoutes"
+ "routingContextRemoteXPC_SelectRoutes"
+ "routingContextRemoteXPC_SendCommand"
+ "routingContextRemoteXPC_SendData"
+ "routingContextRemoteXPC_SendDataForDeviceID"
+ "routingContextRemoteXPC_SetProperty"
+ "routingContextResilientRemote_copySharedAudioContext_block_invoke"
+ "routingContextResilientRemote_fireAllPropertyChangeNotifications"
+ "routingContextResilientRemote_forwardNotificationFromRemoteContext"
+ "routingContextResilientRemote_replaceRemoteContext"
+ "routingContextResilientRemote_serverConnectionDied_block_invoke"
+ "routingContextResilientRemote_startObservingRemoteContext"
+ "routingContextResilientRemote_stopObservingRemoteContext"
+ "routingContextResilientRemote_withRemoteContext"
+ "routingContextServerXPC_CopyOptionsWithClientPIDAndName"
+ "routingContextUtilities_getFeatureString"
+ "routingContextUtilities_getSharedContextUtilities_block_invoke"
+ "routingContext_AddToSelectedRouteDescriptorsWithCompletionCallback"
+ "routingContext_CopyPredictedSelectedRouteDescriptor_block_invoke"
+ "routingContext_CopyProperty_block_invoke"
+ "routingContext_CopyRoute_block_invoke"
+ "routingContext_Finalize_block_invoke"
+ "routingContext_RemoveFromSelectedRouteDescriptorsWithCompletionCallback"
+ "routingContext_ReportModificationMetrics"
+ "routingContext_SelectRouteDescriptorWithCompletionCallback"
+ "routingContext_SelectRouteDescriptor_block_invoke"
+ "routingContext_SelectRouteDescriptorsWithCompletionCallback"
+ "routingContext_SelectRoute_block_invoke"
+ "routingContext_copyAssociatedAudioDeviceForContextAndFeature"
+ "routingContext_copySystemContext"
+ "routingContext_create"
+ "routingContext_createWithUUID"
+ "routingManager_createBluetoothEndpointManager"
+ "routingManager_createMXSessionForCarPlay"
+ "routingManager_generateContextUUID"
+ "routingManager_handleEndpointFailedNotification_block_invoke"
+ "routingManager_isBluetoothPortPairedToCarPlay"
+ "routingManager_pickingTimeoutCallback"
+ "routingManager_resetScreenSettings"
+ "routingManager_shouldUseCustomizedRouting"
+ "routingManager_validateAndCopyLeaderContextForPickingRouteDescriptor"
+ "routingSessionManagerRemote_CopyCurrentSession"
+ "routingSessionManagerRemote_Finalize"
+ "routingSessionManagerRemote_HandleClientMessage"
+ "routingSessionManagerRemote_create"
+ "routingSessionManagerRemote_dequeueAndInvokeCallback"
+ "routingSessionManagerRemote_ensureClientEstablished_block_invoke"
+ "routingSessionManagerRemote_getObjectID"
+ "routingSessionManagerResilientRemote_compareAndSwapRemoteManager"
+ "routingSessionManagerResilientRemote_create"
+ "routingSessionManagerResilientRemote_fireAllPropertyChangeNotifications"
+ "routingSessionManagerResilientRemote_forwardNotificationFromRemoteManager"
+ "routingSessionManagerResilientRemote_serverConnectionDied_block_invoke"
+ "routingSessionManager_StartSessionWithRouteDescriptors"
+ "routingSessionManager_StartSuppressingLikelyDestinations_block_invoke"
+ "routingSessionManager_StopSuppressingLikelyDestinations_block_invoke"
+ "routingSessionManager_airPlayVideoActiveChanged"
+ "routingSessionManager_airPlayVideoPlayingChanged"
+ "routingSessionManager_copySimulatedDestinations"
+ "routingSessionManager_create"
+ "routingSessionManager_create_block_invoke"
+ "routingSessionManager_establishRoutingSessionFromCurrentRoutes"
+ "routingSessionManager_getAirPlayVideoActive"
+ "routingSessionManager_getAirPlayVideoPlaying"
+ "routingSessionManager_loadAirPlayRoutePredictionFramework_block_invoke"
+ "routingSessionManager_loadMobileWiFiFramework"
+ "routingSessionManager_longFormVideoPlayingChanged"
+ "routingSessionManager_predictionsForCurrentContextUpdated_block_invoke"
+ "routingSessionManager_routeConfigUpdated"
+ "routingSessionManager_updateConfiguration"
+ "routingSessionManager_updatePredictedDestinations"
+ "routingSessionManager_vendDiscoveredRoutes"
+ "routingSessionManager_waitForRecentPredictions_block_invoke"
+ "routingSessionManager_waitForRecentPredictions_block_invoke_2"
+ "routingSessionManager_wifiPowerStatusChanged_block_invoke"
+ "routingSession_CopyDestination"
+ "routingSession_createInternal"
+ "routingcontextremote_trace"
+ "routingcontextresilientremote_trace"
+ "routingcontextserver_trace"
+ "routingsessionmanagerremote_trace"
+ "routingsessionmanagerserver_trace"
+ "save"
+ "secondary"
+ "selfWeak"
+ "sendAudioRoutingRequestToDevice:appBundleID:audioScore:flags:reason:responseHandler:"
+ "sendMessageWithDictionary:error:"
+ "sendModificationResult"
+ "sendModificationResult:"
+ "sendSessionConfigurationInfoToVA"
+ "sendSessionConfigurationInfoToVA:"
+ "serverModificationFinishedTimestamp"
+ "serverModificationStartedTimestamp"
+ "session is not active or not playing"
+ "sessionAudioObjectID ="
+ "setAudioObjectID:"
+ "setAudioToolboxIsPlaying:"
+ "setAudioTrackStatus:"
+ "setClientModificationFinishedTimestamp:"
+ "setClientModificationStartedTimestamp:"
+ "setConnectBannerResponse:"
+ "setFigEndpointType:"
+ "setFromPorts:"
+ "setGreenTeaLoggerRecordingState:state:"
+ "setHasExternalMuteNotificationContext:"
+ "setIsOutputMuted:"
+ "setIsPlayerMuted:"
+ "setIsPlayingVideoOutput:"
+ "setIsVoiceAssistantPlayingToPersonalAudioDeviceOverMedia:"
+ "setMostRecentSessionInfoSetOnVA:"
+ "setPreferHeadphonesOverCarsAndSpeakersEnabled:"
+ "setPrefersBluetoothHighQualityContentCapture:"
+ "setReason:"
+ "setRouteSemaphore:"
+ "setSelfWeak:"
+ "setServerModificationFinishedTimestamp:"
+ "setServerModificationStartedTimestamp:"
+ "setServiceClass:"
+ "setShadowingAudioSessionOptions:"
+ "setSomeLongFormVideoClientIsActive:"
+ "setTxid:"
+ "setUndoBannerResponse:"
+ "setUserPreferredRoute:hostApplicationBundleID:"
+ "shadowingAudioSessionOptions"
+ "shadowingAudioSessionOptions ="
+ "shouldAllowBluetoothAccessoryToRequestAudioRoute"
+ "shouldPrivacyPongPlay"
+ "shouldSendSessionConfigurationInfoToVA"
+ "singletonVolumeController_Finalize"
+ "singletonVolumeController_copyCachedRemoteVolumeController"
+ "singletonVolumeController_copyRemoteVolumeController"
+ "singletonVolumeController_handleRemoteVolumeControllerNotifications"
+ "singletonVolumeController_setCachedRemoteVolumController"
+ "soft"
+ "softlink:o:path:/System/Library/PrivateFrameworks/RTCReporting.framework/RTCReporting"
+ "someLongFormVideoClientIsActive"
+ "startConfigurationWithCompletionHandler:"
+ "stsFlavor NULL or not CFString"
+ "stsOut NULL"
+ "stsServer_HandleCopyPropertyByLabelMessage"
+ "stsServer_HandleCopyShmemMessage"
+ "stsServer_HandleCreationMessage"
+ "stsServer_HandleGetActiveMessage"
+ "stsServer_HandleMessage"
+ "stsServer_HandleSetActiveMessage"
+ "stsServer_HandleSetPropertyByLabelMessage"
+ "stsServer_HandleStdCopyPropertyMessage"
+ "stsServer_HandleStdSetPropertyMessage"
+ "sts_trace"
+ "stsremote_trace"
+ "stsserver_trace"
+ "studio mic input"
+ "suspended"
+ "synchronizeSessionVolumeWithMediaVolumeIfNeeded:"
+ "systemController_ClearUplinkMutedCache"
+ "systemController_CopyDeviceRouteForAudioCategory"
+ "systemController_CopyPickableRoutesForCategoryAndMode"
+ "systemController_CopyProperty"
+ "systemController_CopyVolumeCategoryAndMode"
+ "systemController_Finalize"
+ "systemController_GetInputMute"
+ "systemController_GetVolumeButtonDelta"
+ "systemController_HasRouteSharingPolicyLongFormVideo"
+ "systemController_PerformVolumeOperation"
+ "systemController_RemoteDeviceControlIsAllowed"
+ "systemController_SetInputMute"
+ "systemController_SetProperty"
+ "systemController_SetSilentMode"
+ "systemController_ToggleInputMute"
+ "systemController_notificationCallback"
+ "teardown"
+ "txid"
+ "undoBannerResponse"
+ "unduckToLevelScalar out of range"
+ "unknown format"
+ "unmuteOutputForSession:"
+ "unregisterSessionAudioObject"
+ "updateAudioBehaviorFromVARouteConfig:"
+ "updateAudioSessionIDAndAudioObject:"
+ "updateAudioTrackStatus:"
+ "updateDeviceManagementState:reason:"
+ "updateForRecordingStateDidChange"
+ "updateIsRecordingMuted:updateBluetoothFrameworkToPlayMuteChime:"
+ "updateLayoutRoleCache:displayID:"
+ "updateMeasuredHDMILatencyOnCoreAnimationAndHAL"
+ "updateMediaVolumeForPersonalDevice:oldRoute:"
+ "updateSessionRoutingInformation:"
+ "updateShadowingAudioSessionOptions:shouldUpdateVAConfig:"
+ "updateSomeLongFormVideoClientIsActive"
+ "user preferred input"
+ "userActionToString:"
+ "userInitiated"
+ "userPreferredInputPortIsBluetoothManagedAndHighQuality"
+ "v16@?0@\"NSArray\"8"
+ "v20@0:8C16"
+ "v20@?0i8@\"NSError\"12"
+ "v24@0:8@\"MXRoutingContextModificationMetrics\"16"
+ "v28@0:8@16I24"
+ "v32@0:8^@16^@24"
+ "v32@0:8^{__CFString=}16^{__CFString=}24"
+ "v32@0:8q16@24"
+ "v32@?0^{__CFArray=}8^{__CFArray=}16^{__CFString=}24"
+ "v40@0:8@16I24@28B36"
+ "v40@?0^{__CFArray=}8^{OpaqueFigEndpoint=}16^{OpaqueFigEndpoint=}24^{__CFString=}32"
+ "v44@0:8@16I24@28@36"
+ "v52@0:8@16@24@32@40B48"
+ "v56@0:8@16@24i32I36@40@?48"
+ "v60@0:8@16i24@28@36@44@52"
+ "v96@0:8{?=^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFString}}16{?=^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFString}}56"
+ "vaeCopyChannelNamesForPortAndNumberOfChannels"
+ "vaeCopyDeviceIdentifierFromVADPort"
+ "vaeCopyFigInputDeviceNameFromVADPort"
+ "vaeCopyFigOutputDeviceNameFromVADPort"
+ "vaeCopyHiddenSubPortDescriptionsForPort"
+ "vaeCreateRouteDescription"
+ "vaeDoesPortSupportBluetoothHighQualityContentCapture"
+ "vaeDoesPortSupportHighQualityBiDirectionalAudio"
+ "vaeDoesPortSupportMultipleConnections"
+ "vaeGetBTPortInEarStatusForBud"
+ "vaeGetPortSubTypeFromPortID"
+ "vaeGetPortTypeFromPortID"
+ "vaeIsBTPortAdaptiveVolumeEnabled"
+ "vaeIsBluetoothHighQualityContentCaptureEnabled"
+ "vaeIsLiveListenSupportedOnVADPort"
+ "vaeIsPortWHAGroupable"
+ "vaeIsVoiceProcessingSupportedOnVADPort"
+ "vaeMakePortRoutable"
+ "vaeSetBTLowLatencyMode"
+ "vaemAQMERestartIOFollowingRouteChange"
+ "vaemAddAudioDevicesChangedListener"
+ "vaemAddCurrentRouteHasInputGainControl"
+ "vaemAddCurrentRouteHasVolumeControlListener"
+ "vaemAddInputGainScalarListener"
+ "vaemAddInputSourcesListener"
+ "vaemAddOutputDestinationsListener"
+ "vaemAddToPortEndpointCache"
+ "vaemAddVADAvailableSampleRatesListener"
+ "vaemAddVADCurrentDeviceBufferSizeListener"
+ "vaemAddVADCurrentSampleRateListener"
+ "vaemAddVADDeviceVolumeChangeListener"
+ "vaemAirPlayShouldIgnoreChangesForRouteConfiguration"
+ "vaemAvailableVirtualFormatsPropertyListenerGuts_f"
+ "vaemBufferFrameSizeShouldBeRestricted"
+ "vaemCanEncodeToAC3"
+ "vaemClearUserPreferredInputPortInRouteConfigToVA"
+ "vaemConnectedPortsPropertyListenerGuts"
+ "vaemCopyActivePortsListForRouteConfigurationScopeAndDevice"
+ "vaemCopyAssociatedPortsForStreamID"
+ "vaemCopyAudioChannelLayout"
+ "vaemCopyAudioStreamIDsForScope"
+ "vaemCopyCPMSPowerBudget"
+ "vaemCopyConnectedPortsForPortTypeAndScope"
+ "vaemCopyConnectedPortsListForRouteConfiguration"
+ "vaemCopyConnectedPortsWithDeviceListForRouteConfiguration"
+ "vaemCopyCurrentInputDataSource"
+ "vaemCopyCurrentOutputDataDestination"
+ "vaemCopyDetailedRouteDescription"
+ "vaemCopyDeviceFormat"
+ "vaemCopyEndpointForPort"
+ "vaemCopyFallbackInputRouteEndpoint"
+ "vaemCopyInputDataSources"
+ "vaemCopyOutputDataDestinations"
+ "vaemCopyPickableQuiesceableWiredPortsList"
+ "vaemCopyPortDescription"
+ "vaemCopyThermalControlInfo"
+ "vaemCopyVADInputPortsForRouteConfiguration"
+ "vaemCopyVADOutputPortsForRouteConfiguration"
+ "vaemCreateVADWithRouteConfigurationDictionary"
+ "vaemCurrentRouteHasInputGainControl"
+ "vaemCurrentRouteHasInputGainControlListenerGuts"
+ "vaemCurrentRouteHasVolumeControl"
+ "vaemDeleteVADWithRouteConfigurationDictionary"
+ "vaemFindAirPlayHandoffPort"
+ "vaemGetAC3IsSupported"
+ "vaemGetDeviceBufferNumPCMFrames"
+ "vaemGetDeviceBufferNumPCMFramesRange"
+ "vaemGetDeviceFormatID"
+ "vaemGetDownlinkMute"
+ "vaemGetFullMute"
+ "vaemGetMaximumNumberOfChannels"
+ "vaemGetNumberOfChannelsInStream"
+ "vaemGetNumberOfStreams"
+ "vaemGetSampleRateForDevice"
+ "vaemGetStereoInputOrientation"
+ "vaemGetStream0"
+ "vaemGetUplinkMute"
+ "vaemGetVADPortIDFromVADPortType"
+ "vaemGetVirtualAudioPlugInCategory"
+ "vaemGetVirtualAudioPlugInMode"
+ "vaemHasStream0Changed"
+ "vaemHeadphoneJackHasInput"
+ "vaemHeadphoneJackIsConnected"
+ "vaemIsLocalSystemSoundDeviceType"
+ "vaemIsMATAtmosAvailable"
+ "vaemIsMATAtmosEnabled"
+ "vaemProcessCustomizedRouting"
+ "vaemReceiverWillBeUsedListener"
+ "vaemRemoveAudioDevicesChangedListener"
+ "vaemRemoveFromPortEndpointCache"
+ "vaemRemoveVADAvailableSampleRatesListener"
+ "vaemSendUserPreferredInputPortInRouteConfigToVA"
+ "vaemSessionRoutingInfoChangeListener"
+ "vaemSessionRoutingInfoChangeListener_block_invoke"
+ "vaemSetAirPlayDeviceVolumeInPVM"
+ "vaemSetCallScreeningStatus"
+ "vaemSetCaptureOrientationOverride"
+ "vaemSetDefaultInputGain"
+ "vaemSetDeviceBufferNumPCMFramesQuiet"
+ "vaemSetDeviceInputGainScalar"
+ "vaemSetDeviceVolumeIfNotSet"
+ "vaemSetDownlinkMute"
+ "vaemSetInputDataSource"
+ "vaemSetInputGainFromPreferenceIfPresent"
+ "vaemSetOrientationOverride"
+ "vaemSetOutputDataDestination"
+ "vaemSetRouteConfigurationDictionaryOnVAD"
+ "vaemSetStereoInputOrientation"
+ "vaemSetVirtualFormatForScope"
+ "vaemShouldIncludePortTypeForRouteConfiguration"
+ "vaemSystemHasAudioInputDeviceForRouteConfiguration"
+ "vaemTakeOwnershipOnSharedAudioRoute"
+ "vaemUnmuteFullMuteIfMuted"
+ "vaemUpdateConnectedInputPortsList"
+ "vaemUpdateCurrentOutputAndInputPortFromRouteChangeDescription"
+ "vaemUpdateCurrentOutputRoutesInfo"
+ "vaemUpdatePVMSettingsForInputGain"
+ "vaemUpdateSessionStatesForRouteChangeReason"
+ "vaemUpdateThermalGainAdjustment"
+ "vaemVADCopyAvailableStreamFormatsForVADID"
+ "vaemVADDeviceVolumeChangeListenerGuts_f"
+ "vaemVADSupportsPlayAndRecordCategory"
+ "vehicleForBluetoothAddress:"
+ "vehicleName"
+ "vibrator_trace"
+ "voiceCommandSynchroizedVolumeActivityTimestamp"
+ "volumeControllerRemote_deadConnectionCallback"
+ "volumeControllerRemote_ensureClientEstablished_block_invoke"
+ "volumeControllerRemote_getObjectID"
+ "volumeControllerServer_getClientInfo"
+ "volumeControllerServer_handleCanSetEndpointVolumeMessage"
+ "volumeControllerServer_handleCanSetMasterVolumeMessage"
+ "volumeControllerServer_handleCanUseForRoutingContextMessage"
+ "volumeControllerServer_handleCopySharedControllerMessage"
+ "volumeControllerServer_handleGetEndpointVolumeControlTypeMessage"
+ "volumeControllerServer_handleGetEndpointVolumeMessage"
+ "volumeControllerServer_handleGetMasterVolumeControlTypeMessage"
+ "volumeControllerServer_handleGetMasterVolumeMessage"
+ "volumeControllerServer_handleGetSubEndpointVolumeControlTypeMessage"
+ "volumeControllerServer_handleGetSubEndpointVolumeMessage"
+ "volumeControllerServer_handleRemoteMessage"
+ "volumeControllerServer_lookupVolumeControllerByObjectIDForConnection"
+ "volumeController_AreVolumeOperationsSupportedForRoutingContext"
+ "volumeController_CanSetMuteOfSubEndpointWithID"
+ "volumeController_Finalize"
+ "volumeController_GetMainVolumeControlTypeForRoutingContext"
+ "volumeController_GetMainVolumeForRoutingContext"
+ "volumeController_GetMuteOfEndpointWithID"
+ "volumeController_GetMuteOfSubEndpointWithID"
+ "volumeController_GetVolumeControlTypeOfSubEndpointWithID"
+ "volumeController_GetVolumeForEndpointWithID"
+ "volumeController_IsMainVolumeControlSupportedForRoutingContext"
+ "volumeController_IsVolumeControlSupportedForEndpointWithID"
+ "volumeController_SetMuteOfSubEndpointWithID"
+ "volumeController_createOnce"
+ "volumeController_doesEndpointHaveSameID"
+ "volumeController_getMainVolume"
+ "volumeController_getMaxSubEndpointVolume"
+ "volumeController_getMuteByUserForRoutingContext"
+ "volumeController_getVolumeForEndpoint"
+ "volumeController_handleAirPlayVolumeControlTypeDidChangeNotification"
+ "volumeController_isVolumeControllerSupported"
+ "volumeController_postMuteOperationsSupportedForRoutingContextDidChangeNotification"
+ "volumeController_setMainVolume"
+ "volumeController_setVolumeForEndpoint"
+ "volumeLimitPrefs"
+ "volumeMultiplierPrefs"
+ "volumecontroller_getSubEndpointVolume"
+ "volumecontrollerremote_trace"
+ "was"
+ "wasn't"
+ "willRouteToOnDemandVADOnActivation:"
+ "wrong type for ClientAuditToken"
+ "wrong type for ClientSecTask"
+ "yes"
+ "\xf0\xf0\xb1"
- "\t[%ld] Endpoint=%@, supportedFeatures=%@\n"
- "%@\t[%ld] Endpoint=%@, supportedFeatures=%@\n"
- "%{BOOL}u"
- "+[AVSystemController(InternalUse) postNotificationOnMainQueue:notification:object:]"
- "-CMSMDevState- %s: MediaExperience.framework is hosted by audiomxd"
- "-CMSMDevState- %s: MediaExperience.framework is hosted by mediaserverd"
- "-CMSMDevState- %s: Unknown process hosting MediaExperience.framework"
- "-CMSUtilities- %s: Client '%{public}@' is in the background and isn't allowed to start recording clientPID=%{public}@ hasEntitlementToStartRecordingInTheBackground=%{BOOL}u clientPriority=%{public}@} doesInterAppAudio=%{BOOL}u sessionIsResumingRecordingAfterInterruption=%{BOOL}u sessionIsWithinGracePeriodAfterStoppedInBackground=%{BOOL}u sessionAllowedToStartRecordingTemporarily=%{BOOL}u hasEchoCancelledMode=%{BOOL}u"
- "-CMSUtilities- %s: EmergencyAlert priority session should interrupt EchoCancellationInput"
- "-CMSUtilities- %s: Session '%{public}@' has EchoCancellationInput mode, allow it to co-exist with PhoneCall priority sessionToInterrupt '%{public}@'"
- "-CMSUtilities- %s: Will not interrupt because victim '%{public}@' is has EchoCancellationInput mode"
- "-CMSessionMgr- %s: Available route control features are %{public}@, is echo-cancelled input available? = %{BOOL}u for session %{public}@ [%p] with %{public}@ category; willRouteToOnDemandVADOnActivation = %{BOOL}u."
- "-CMSessionMgr- %s: Client '%{public}@' changed isRecordingMuted to %{BOOL}u"
- "-CMSessionMgr- %s: Client '%{public}@' failed to change isRecordingMuted to %{BOOL}u with error=%d"
- "-CMSessionMgr- %s: Setting mute value to %{BOOL}u for client %{public}@"
- "-CMSessionMgr- %s: Skipping begin interruption for %{public}@ because there is an Enrollment session active"
- "-CMVAEndpoint- %s: AudioObjectGetPropertyData( kVirtualAudioPortPropertyInEarBluetoothStatusPrimary ) failed with err = %d = %{public}.4s"
- "-CMVAEndpoint- %s: AudioObjectGetPropertyData( kVirtualAudioPortPropertyInEarBluetoothStatusSecondary ) failed with err = %d = %{public}.4s"
- "-CMVAEndpoint- %s: AudioObjectGetPropertyData( temp_kVirtualAudioPortPropertyModelUID ) failed with err = %d = %c%c%c%c"
- "-CMVAEndpoint- %s: Port has siblings for portID = %u, supports multiple conn = %d, routable = %d"
- "-CMVAEndpoint- %s: Requesting ownership for a2dp port %d for reason=%{public}@ instead of hfp port %d."
- "-CMVAEndpoint- %s: Requesting ownership on BT port = %u"
- "-CMVAEndptMgr- %s:  CarPlay Headunit published both ports (USB audio ( port %u ) & Stark ( port %u ) ) for main audio."
- "-CMVAEndptMgr- %s: Setting buffer duration to %.3f"
- "-CMVAEndptMgr- %s: VA initialization ended - Elapsed time=%.3f milliseconds"
- "-CMVAEndptMgr- %s: category = '%{public}.4s'  mostRecentVADCategory = '%{public}.4s' mode = '%{public}.4s' mostRecentVADMode = '%{public}.4s' \n \t\t\t\t\t\t\t\t\t\t\tactivationContext: %{public}@ \n \t\t\t\t\t\t\t\t\t\t\toverridePortsList: %{public}@ mostRecentOverridePortsList: %{public}@ \n \t\t\t\t\t\t\t\t\t\t\troutablePorts:%{public}@ unroutablePorts:%{public}@ \t\t\t\t\t\n  \t\t\t\t\t\t\t\t\t\t\tportsToAggregate:%{public}@ portsToDeaggregate:%{public}@\t\t\t\t\n \t\t\t\t\t\t\t\t\t\t\tsubPortPreferences: %{public}@ mostRecentsubPortPreferences : %{public}@ \n \t\t\t\t\t\t\t\t\t\t\tsetScreenDarkMode = %{public}s \n \t\t\t\t\t\t\t\t\t\t\tcreateSpeakerDevice = %{public}s \n \t\t\t\t\t\t\t\t\t\t\texcludedPortsList : %{public}@ \n \t\t\t\t\t\t\t\t\t\t\tignoreRingerSwitch = %{public}s \n \t\t\t\t\t\t\t\t\t\t\tdecoupledInputOutput = %{public}s \n \t\t\t\t\t\t\t\t\t\t\tallowedPortTypes = %{public}@ \n\t\t\t\t\t\t\t\t\t\t\treporterIDs = %{public}@ \n\t\t\t\t\t\t\t\t\t\t\tcameraParameters = %{public}@\n \t\t\t\t\t\t\t\t\t\t\tupdatePVMOnRedundantRouteConfiguration = %{public}s\n \t\t\t\t\t\t\t\t\t\t\tpersistentRoute = %{public}@ mostRecentPersistentRoute: %{public}@\n"
- "-CMVAEndptMgr- %s: duration = %.3f, sampleRate = %.3f, numPCMSamples = %u, NearestPowerOf2 = %u, UseQuietBufferSizeProperty = '%{public}@'"
- "-CMVAEndptMgr- %s: isBTManaged = %{BOOL}u, isActionRouting= %{BOOL}u, portIsInEar=%{BOOL}u"
- "-CMVAEndptUtl- %s: BT audio route action is route, but port %ld is not in-ear"
- "-FigPredictedRouting- %s: Called due to reason=%{public}@, isBTManagedPortPresent=%{BOOL}u, isBTManagedPortInEar=%{BOOL}u, routeIsBuiltIn=%{BOOL}u, predictedRouteConditionChanged=%{BOOL}u, cachedSessionIsPlaying=%{BOOL}u, predictedRouteChanged=%{BOOL}u, sSystemMusicIsIndependent=%{BOOL}u, predictedRouteChangedForSystemMusic=%{BOOL}u, predictedRouteName=%{public}@, predictedRouteUID=%{private}@"
- "-FigRouteDiscoverer- %s: Finalizing discoverer of type %{public}@ uuid=%{private}@"
- "-FigRouteDiscoverer- %s: Registered discoverer of type %{public}@ uuid=%{private}@"
- "-FigRouteDiscoverer- %s: SetProperty Discovery mode to none"
- "-FigRouteDiscoveryManager- %s: Time taken to run notification handler %fms. Time taken to post %{public}@ to all discoverers: %fms. Average time: %fms. Cache misses this iteration %d."
- "-FigRoutingContext- %s: Calling client back with reason %{public}@. Time taken %f ms."
- "-FigRoutingManager- %s: routingManager: endpointName = %{public}@, inActivationSeed=%llu, err = %d, inFeatures=%d, routingContextType=%{public}@. Time taken to removeEndpoint: %f ms. Time taken to run callback %f ms. Total round trip time: %f ms."
- "-FigRoutingManager- %s: routingManager_EndpointHelpers: endpointName = %{public}@, inActivationSeed=%llu, err = %d, inFeatures=%d, routingContextType=%{public}@. Time taken to addEndpoint: %f ms. Time taken to run callback %f ms. Total round trip time: %f ms."
- "-FigRoutingManager_SystemRemotePool- %s: mxSystemRemotePool: endpointName = %{public}@, inActivationSeed=%llu, err = %d, inFeatures=%d. Time taken to activateEndpoint: %f ms. Time taken to run callback %f ms. Total round trip time: %f ms."
- "-FigRoutingManager_iOS- %s: oldRouteIdentifiers=%{private}@, newRouteIdentifiers=%{private}@, userPickedRoute=%{public}s, airPlayShouldIgnoreRouteChange=%{public}s, newRoutingContextType=%{public}@"
- "-FigRoutingManager_iOSEndpointHelpers- %s: routingManager_iOS: endpointName = %{public}@, inActivationSeed=%llu, err = %d, inFeatures=%d. Time taken to activate endpoint: %f ms. Time taken to run callback: %f ms. Total round trip time: %f ms."
- "-MXAdditiveRoutingManager- %s: Session not found for audio session ID %d"
- "-MXAdditiveRoutingManager- %s: Updating detailed route description for %{public}@ with deviceID %{public}@"
- "-MXBluetoothServices- %s: Adding device %{private}@ - %{private}@, canCache = %{BOOL}u"
- "-MXBluetoothServices- %s: Adding device %{private}@ - %{private}@, isBTManaged=%{BOOL}u"
- "-MXBluetoothServices- %s: Audio routing update from BluetoothServices, managed ports %{public}@; unmanaged ports %{public}@"
- "-MXBluetoothServices- %s: BTAudioRoutingAction is BTAudioRoutingActionConnecting cache wxInfo=%{private}@"
- "-MXBluetoothServices- %s: BTAudioRoutingAction is BTAudioRoutingActionDontRoute due to rejection, the predicted route will be reset."
- "-MXBluetoothServices- %s: BTAudioRoutingAction is BTAudioRoutingActionHijackBackOff disable predicted routing..."
- "-MXBluetoothServices- %s: BTAudioRoutingAction is BTAudioRoutingActionHijackBackOff during manual picking, do not disable SR."
- "-MXBluetoothServices- %s: BTAudioRoutingAction is BTAudioRoutingActionInvalid possibly due to timeout!"
- "-MXBluetoothServices- %s: BTAudioRoutingAction is BTAudioRoutingActionRejected due to rejection, the predicted route will be reset."
- "-MXBluetoothServices- %s: BTAudioRoutingRequest failed with error:%{public}@"
- "-MXBluetoothServices- %s: BTAudioRoutingRequest[deviceAddress=%{private}@, appBundleID=%{private}@, audioScore=%d, flags=%{public}s] ended - Elapsed time=%.3f milliseconds"
- "-MXBluetoothServices- %s: BTAudioRoutingRequest[deviceAddress=%{private}@, appBundleID=%{private}@, audioScore=%d, flags=%{public}s] started"
- "-MXBluetoothServices- %s: Failed to load BluetoothServices"
- "-MXBluetoothServices- %s: No connected ports found, removing %{private}@"
- "-MXBluetoothServices- %s: Not taking ownership, BTPort is not inEar"
- "-MXBluetoothServices- %s: Not taking ownership, isCurrentRouteBuiltIn=%{BOOL}u isBluetoothSharingSessionEnabled=%{BOOL}u isPredictedRoutingTimerActive=%{BOOL}u"
- "-MXBluetoothServices- %s: PreemptivePortInfo is nil"
- "-MXBluetoothServices- %s: Reading device %{private}@ - %{private}@, isBTManaged=%{BOOL}u"
- "-MXBluetoothServices- %s: Removing %{private}@"
- "-MXBluetoothServices- %s: Route to device =%{private}@"
- "-MXBluetoothServices- %s: Routing action for %{private}@ - %{private}@ is %{public}@"
- "-MXBluetoothServices- %s: Routing to preferred address %{public}@ with priority %d"
- "-MXBluetoothServices- %s: The current route is BT and inEar. Make the ports routable and request for ownership"
- "-MXBluetoothServices- %s: could not register for BTNotificationPreemptivePortChanged notification"
- "-MXBluetoothServices- %s: could not register for BTNotificationPreemptivePortDisconnected notification"
- "-MXBluetoothServices- %s: isBTManaged=%{BOOL}u for %{public}@ - %{private}@, inResponse action = '%{public}s'"
- "-MXCoreSessionSecureCommon- %s: Insufficient information in virtualDeviceInfo = %{public}@, not amending audio behaviour dictionary"
- "-MXCoreSessionSecureCommon- %s: SoundAnalysis doesn't have the entitlement to set Enrollment mode!"
- "-MXCoreSessionSecureCommon- %s: Updating audio behaviour to %{public}@ for %{public}@."
- "-MXCoreSession_Embedded- %s: Encountered error %d querying On-demand-VAD support for session %{public}@ [%p] with additive routing info: %{public}@."
- "-MXCoreSession_Embedded- %s: Insufficient information in virtualDeviceInfo = %{public}@, not amending audio behaviour dictionary"
- "-MXCoreSession_Embedded- %s: Updating audio behaviour to %{public}@ for %{public}@."
- "-MXCoreSession_Embedded- %s: Will session %{public}@ [%p] with info %{public}@ route to an on-demand VAD? %{BOOL}u"
- "-MXDebugUtilities- %s:  --------------- Assertion info --------------- "
- "-MXDebugUtilities- %s: KEY: %{public}@\t\tVALUE: %{public}@"
- "-MXDebugUtilities- %s: Playback assertion %p explanation = %{public}@"
- "-MXDebugUtilities- %s: Temporary playback assertion %p explanation = %{public}@"
- "-MXInitialzation_Common- %s: MediaExperience framework is fully initialized now, blocked for %0.3f ms"
- "-MXInitialzation_Embedded- %s: AirPlayStartServicesInMXProcess is NULL"
- "-MXInitialzation_Embedded- %s: Did not find AirPlaySender bundle '%{public}s': %{public}s\n"
- "-MXRoutingManager_AudioContext- %s: Sub endpoint info was not provided in the inFailureInfo dictionary"
- "-MXRoutingManager_AudioContext- %s: endpointName = %{public}@, inActivationSeed=%llu, err = %d, inFeatures=%d, routingContextUUID=%{public}@ routingContextType=%{public}@. Time taken to addEndpoint: %f ms. Time taken to run callback %f ms. Total round trip time: %f ms."
- "-MXRoutingManager_AudioContext- %s: endpointName = %{public}@, inActivationSeed=%llu, err = %d, inFeatures=%d, routingContextUUID=%{public}@, routingContextType=%{public}@. Time taken to removeEndpoint: %f ms. Time taken to run callback %f ms. Total round trip time: %f ms."
- "-MXSession- %s: <%{public}@: %p, CoreSessionID = %lld, CoreSession = %{public}@, IsMuted = %{ppublic}@, ClientIsPlaying = %{public}@, AudioToolboxIsPlaying = %{public}@, MXSessionID = %llx, OutputChannels = %u, OutputSampleRate = %f, AudioFormat = %{public}@, MutePriority = %{public}@, IAmPiP = %{public}@, DoesntActuallyPlayAudio = %{public}@, ClientType = %{public}@, IsPlayingOutput = %{BOOL}u \n Spatial Settings:: sourceFormatInfo: %{public}@"
- "-MXSessionManagerInterruptionActionMapper- %s: Session has set client priority to PhoneCall. Upgrading sessionPriority to kMXCoreSessionPriority_Critical501"
- "-MXSessionManagerSecure- %s: Enrollment session trying to go active while phone call is active"
- "-MXSessionManagerSecure- %s: Failed to mute secure speaker"
- "-MXSessionManagerSecure- %s: Failed to unmute secure speaker"
- "-MXSessionManagerVAUtilities- %s: AudioObjectSetPropertyData( kVirtualAudioPortPropertySecureSpeakerOutputMute ) failed with err='%c%c%c%c'"
- "-MXSessionManagerVAUtilities- %s: Invalid speaker port ID!"
- "-MXSessionManagerVAUtilities- %s: kVirtualAudioPortPropertySecureSpeakerOutputMute is not supported!"
- "-MXSystemMirroring_Embedded- %s: endpointName = %{public}@, inActivationSeed=%llu, err = %d, inFeatures=%d. Time taken to activateEndpoint: %f ms. Time taken to run callback %f ms. Total round trip time: %f ms."
- "-MXSystemSounds- %s: Session with Enrollment mode is active, suppressing system sounds"
- "-MX_FeatureFlags- %s: AudioAccessoryFeatures/SmartRoutingInEarQuery feature is %{public}@"
- "-MX_FeatureFlags- %s: MediaExperience/OffloadACQ feature is %{public}s"
- "-MX_FeatureFlags- %s: MediaExperience/ReduceRouteDiscoveryQueueHopping feature is %{public}s"
- "-MX_FeatureFlags- %s: MediaExperience/SystemInputPicker feature is %{public}s"
- "-MX_FeatureFlags- %s: VirtualAudio/quiesceable_wired_connection feature is %{public}s"
- "-[MXCoreSession updateAudioBehaviourFromVARouteConfig:]"
- "-[MXCoreSession willRouteToOnDemandVADOnActivation]"
- "-[MXCoreSessionSecure updateAudioBehaviourFromVARouteConfig:]"
- "-[MXCoreSessionSecure updateEntitlements]"
- "-[MXMediaEndowmentManager getRecordingAttributions:]"
- "-[MXSessionManager(VAUtilities) updateSecureSpeakerMuteState:]"
- "-[MXSystemController initWithPID:remoteDeviceID:]_block_invoke"
- "/System/Library/PrivateFrameworks/BluetoothServices.framework/BluetoothServices"
- "01:55:59"
- "<ID: %llx, CoreSessionID = %lld Name = %@, Muted = %@, ClientIsPlaying = %@, AudioToolboxIsPlaying = %@, MutePriority = %@, PiP = %@, DoesntActuallyPlayAudio = %@, clientType = %x, IsPlayingOutput = %@"
- "@48@0:8^{OpaqueFigRoutingContext=}16@24^?32^v40"
- "AVAudioSessionCategorySpeechDetect"
- "AVSystemController.m"
- "Apr 19 2025"
- "AudioWithScreenMirroringOnly"
- "BTAudioRoutingRequest"
- "CMSMDeviceState_UpdateDeviceConfiguration_block_invoke"
- "EchoCancellationInput"
- "EndpointSubType_visionOS"
- "Enrollment"
- "FigRouteDiscoveryManagerCopyRouteDescriptorsFromEndpointsAndAudioSessionID"
- "FigRouteDiscoveryManagerRunBlockOnSerialQueueIfOnEmbeddedPlatforms"
- "FigRoutingManagerContextUtilities_AddCurrentlyActivatingEndpoint_block_invoke_2"
- "FigRoutingManagerSetupEndpointCentralForCarPlay"
- "FigRoutingSessionManagerRemoteXPC.c"
- "FigRoutingSessionManagerResilientRemote.c"
- "FigVibrator_IOKit.c"
- "FigVibrator_VibeSynthEngine.c"
- "IsMediaserverd ="
- "MXBluetoothServices_IsPortBTManaged_block_invoke"
- "MXBluetoothServices_QueryAudioRoutingActionForNewWirelessPort"
- "MXBluetoothServices_QueryAudioRoutingActionForNewWirelessPort_block_invoke"
- "MXBluetoothServices_RegisterForPreemptivePortChanged"
- "MXBluetoothServices_RegisterForPreemptivePortDisconnected"
- "MXBluetoothServices_RemoveDisconnectedDeviceIDs"
- "MX_FeatureFlags_IsOffloadACQEnabled_block_invoke"
- "MX_FeatureFlags_IsReduceRouteDiscoveryQueueHoppingEnabled_block_invoke"
- "MX_FeatureFlags_IsSmartRoutingInEarQueryEnabled_block_invoke"
- "MX_SystemStatus_PublishRecordingClientsInfo_block_invoke_3"
- "NRPairedDeviceRegistry"
- "OffloadACQ"
- "PowerManager_InitializeCPMSForAudio_block_invoke_3"
- "PowerManager_InitializeCPMSForHaptics_block_invoke_3"
- "PredictedRoutingForSystemMusic"
- "ReduceRouteDiscoveryQueueHopping"
- "Rejected"
- "SmartRoutingInEarQuery"
- "SpatialModeOn"
- "SystemInputPicker"
- "T@\"MXCoreSession\",N,V_interruptingSession"
- "TB,N,V_appendContextToMuteNotification"
- "TB,N,V_hasEntitlementToSetEnrollmentMode"
- "_appendContextToMuteNotification"
- "_hasEntitlementToSetEnrollmentMode"
- "appendContextToMuteNotification"
- "appendContextToMuteNotification ="
- "audio session id"
- "central_Finalize"
- "central_endpointDidDeactivateNotificationCallback"
- "cmsHandleIdleSleep"
- "cmsmdevicestate_UpdateDeviceClass"
- "com.apple.mediaexperience.btroutingrequestqueue"
- "com.apple.mediaserverd"
- "com.apple.private.mediaexperience.enrollmentmode.allow"
- "compatibleAudioRouteForRoute:"
- "discoveryManager_shouldSkipAvailableEndpointsQuery"
- "getHDMILatencyForCurrentRefreshRate"
- "getRecordingAttributions:"
- "hasEntitlementToSetEnrollmentMode"
- "i60@0:8{MXSessionPlayingInfo=@@II@@}16B56"
- "initWithRoutingContext:routeConfigUpdateID:callback:context:"
- "invalid ( possibly because of timeout ) "
- "isSessionUsingBuiltInMic:"
- "mCreationTime"
- "mRestingVolumeTimer"
- "mTimerDuration"
- "managed, don't route "
- "managed, route"
- "mxBluetoothServices_CopyPreferredDeviceAddress_block_invoke"
- "mxBluetoothServices_SendAudioRoutingRequest"
- "mxBluetoothServices_addCachedPort"
- "mxBluetoothServices_handleAudioRoutingChanged"
- "mxBluetoothServices_isBluetoothServicesLoaded"
- "mxBluetoothServices_readCachedPort"
- "mxBluetoothServices_routeToBTDeviceIfNeeded"
- "mxSystemControllerListBeginIteration"
- "mxSystemControllerListEndIteration"
- "numberWithInteger:"
- "restingVolumeTimerDuration"
- "routingManager_createCMSessionForCarPlay"
- "secure enrollment session is going active"
- "setAppendContextToMuteNotification:"
- "setHasEntitlementToSetEnrollmentMode:"
- "softlink:r:path:/System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry"
- "unmanaged "
- "updateAudioBehaviourFromVARouteConfig:"
- "updateEntitlements"
- "updateSecureSpeakerMuteState:"
- "vaeGetBTPortPrimaryBudInEarStatus"
- "vaeGetBTPortSecondaryBudInEarStatus"
- "vaeMakeSiblingPortsRoutable"

```
