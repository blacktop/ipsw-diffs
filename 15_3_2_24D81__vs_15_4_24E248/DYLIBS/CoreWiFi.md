## CoreWiFi

> `/System/Library/PrivateFrameworks/CoreWiFi.framework/Versions/A/CoreWiFi`

```diff

-845.9.0.0.0
-  __TEXT.__text: 0x22a0bc
-  __TEXT.__auth_stubs: 0xe50
-  __TEXT.__objc_methlist: 0x9ed0
-  __TEXT.__const: 0x140
-  __TEXT.__oslogstring: 0xc436
-  __TEXT.__cstring: 0x10f1e
-  __TEXT.__gcc_except_tab: 0xaa20
-  __TEXT.__dlopen_cstrs: 0x427
+875.42.0.0.0
+  __TEXT.__text: 0x2591ac
+  __TEXT.__auth_stubs: 0xf00
+  __TEXT.__objc_methlist: 0xbe6c
+  __TEXT.__const: 0xa8
+  __TEXT.__oslogstring: 0xdc8c
+  __TEXT.__cstring: 0x14cb0
+  __TEXT.__gcc_except_tab: 0xb1f4
+  __TEXT.__dlopen_cstrs: 0x59f
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x2060
-  __TEXT.__objc_classname: 0x880
-  __TEXT.__objc_methname: 0x165a0
-  __TEXT.__objc_methtype: 0x282a
-  __TEXT.__objc_stubs: 0x114c0
-  __DATA_CONST.__got: 0x5d8
-  __DATA_CONST.__const: 0xa30
-  __DATA_CONST.__objc_classlist: 0x248
+  __TEXT.__unwind_info: 0x2218
+  __TEXT.__objc_classname: 0x962
+  __TEXT.__objc_methname: 0x194db
+  __TEXT.__objc_methtype: 0x299c
+  __TEXT.__objc_stubs: 0x13460
+  __DATA_CONST.__got: 0x648
+  __DATA_CONST.__const: 0xb18
+  __DATA_CONST.__objc_classlist: 0x288
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0xb8
+  __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5250
+  __DATA_CONST.__objc_selrefs: 0x5d60
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0x200
-  __DATA_CONST.__objc_arraydata: 0xe58
-  __AUTH_CONST.__auth_got: 0x738
-  __AUTH_CONST.__const: 0x35f0
-  __AUTH_CONST.__cfstring: 0x11080
-  __AUTH_CONST.__objc_const: 0xfd40
-  __AUTH_CONST.__objc_intobj: 0x3078
-  __AUTH_CONST.__objc_arrayobj: 0x2d0
+  __DATA_CONST.__objc_superrefs: 0x240
+  __DATA_CONST.__objc_arraydata: 0x1340
+  __AUTH_CONST.__auth_got: 0x790
+  __AUTH_CONST.__const: 0x3ad0
+  __AUTH_CONST.__cfstring: 0x13580
+  __AUTH_CONST.__objc_const: 0xf158
+  __AUTH_CONST.__objc_intobj: 0x3120
+  __AUTH_CONST.__objc_arrayobj: 0x348
   __AUTH_CONST.__objc_dictobj: 0x1e0
-  __AUTH.__objc_data: 0x16d0
+  __AUTH.__objc_data: 0x1950
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0xb0c
-  __DATA.__data: 0x928
-  __DATA.__bss: 0x1b8
+  __DATA.__objc_ivar: 0xc80
+  __DATA.__data: 0x988
+  __DATA.__bss: 0x2a0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/Versions/A/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/Versions/A/WiFiPeerToPeer
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmrc.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 44CCDB11-8401-305B-BB05-5796D087443B
-  Functions: 4771
-  Symbols:   9759
-  CStrings:  9732
+  UUID: 59C94F56-4D6B-3B8E-A811-15821EE85C20
+  Functions: 5123
+  Symbols:   10686
+  CStrings:  11004
 
Symbols:
+ +[CWFAssetLocal assetIDFromLocalURL:]
+ +[CWFAssetLocal compareAssetVersion:withVersion:]
+ +[CWFAssetLocal compareOSRestoreVersion:withVersion:]
+ +[CWFAssetLocal compareSUCoreRestoreVersion:withVersion:]
+ +[CWFAssetLocal isValidAssetVersion:]
+ +[CWFAssetLocal isValidOSVersion:]
+ +[CWFAssetManager endAllPreviousLocksForSpecifier:]
+ +[CWFAssetPowerTable assetSpecifierToTrack]
+ +[CWFAssetPowerTable currentLatestAssetVersion]
+ +[CWFAssetPowerTable getDeviceSKU]
+ +[CWFAssetPowerTable hashedChipsetName]
+ +[CWFAssetPowerTable isSupportedChipset]
+ +[CWFAssetPowerTable isSupportedDeviceClass]
+ +[CWFAssetPowerTable isSupportedOTAPTUpdate]
+ +[CWFAssetPowerTable shouldAllowTestingOnUnSupportedChipset]
+ +[CWFHotspotClientManager sharedInstance]
+ +[CWFNearbyDeviceDiscoveryFilter supportsSecureCoding]
+ +[CWFXPCRequest _removesDependenciesAfterFinish]
+ -[CWFAssetLocal .cxx_destruct]
+ -[CWFAssetLocal assetID]
+ -[CWFAssetLocal assetSpecifier]
+ -[CWFAssetLocal assetType]
+ -[CWFAssetLocal assetVersion]
+ -[CWFAssetLocal firstSupportedBuild]
+ -[CWFAssetLocal initWithAssetType:assetSpecifier:assetVersion:attributes:localURL:]
+ -[CWFAssetLocal lastSupportedBuild]
+ -[CWFAssetLocal localURL]
+ -[CWFAssetLocal sanityCheckOSRestoreVersion:]
+ -[CWFAssetLocal sanityCheckSKUVersion:]
+ -[CWFAssetManager .cxx_destruct]
+ -[CWFAssetManager __periodicCheck]
+ -[CWFAssetManager _handleAssetChangedNotification]
+ -[CWFAssetManager _registerForAssetChangedNotification:]
+ -[CWFAssetManager assetDidChangeHandler]
+ -[CWFAssetManager assetPowerTable]
+ -[CWFAssetManager assetSpecifier]
+ -[CWFAssetManager currentLockedAutoAssetSelector]
+ -[CWFAssetManager currentLockedAutoAsset]
+ -[CWFAssetManager dealloc]
+ -[CWFAssetManager enablePeriodicCheck]
+ -[CWFAssetManager eventQueue]
+ -[CWFAssetManager init]
+ -[CWFAssetManager interestSet]
+ -[CWFAssetManager lockAndHandOffCanBlock:]
+ -[CWFAssetManager lockAutoAssetWithReason:isBlocking:]
+ -[CWFAssetManager makeAutoAssetWithSelector:]
+ -[CWFAssetManager notifyTokenVersionDownloaded]
+ -[CWFAssetManager periodicCheckEnabled]
+ -[CWFAssetManager periodicCheckTimer]
+ -[CWFAssetManager periodicityInSecs]
+ -[CWFAssetManager setAssetDidChangeHandler:]
+ -[CWFAssetManager setAssetPowerTable:]
+ -[CWFAssetManager setAssetSpecifier:]
+ -[CWFAssetManager setCurrentLockedAutoAsset:]
+ -[CWFAssetManager setCurrentLockedAutoAssetSelector:]
+ -[CWFAssetManager setEventQueue:]
+ -[CWFAssetManager setInterestSet:]
+ -[CWFAssetManager setNotifyTokenVersionDownloaded:]
+ -[CWFAssetManager setPeriodicCheckEnabled:]
+ -[CWFAssetManager setPeriodicCheckTimer:]
+ -[CWFAssetManager setPeriodicityInSecs:]
+ -[CWFAssetManager startEventMonitoring]
+ -[CWFAssetManager stopEventMonitoring]
+ -[CWFAssetManager unlockAssetWithReason:]
+ -[CWFAssetPowerTable allowTestingOnUnSupportedChipset]
+ -[CWFAssetPowerTable createTopLevelDir]
+ -[CWFAssetPowerTable description]
+ -[CWFAssetPowerTable garbageCollectWithNewAsset:prevAsset:]
+ -[CWFAssetPowerTable init]
+ -[CWFAssetPowerTable processLocalAsset:]
+ -[CWFAssetPowerTable setAllowTestingOnUnSupportedChipset:]
+ -[CWFAssetPowerTable transferAssetFromSrc:toDst:withAsseID:withVersion:firstSupportedBuild:lastSupportedBuild:]
+ -[CWFAutoJoinManager __isEnabledKnownNetworkNearby]
+ -[CWFAutoJoinManager __scheduleDelayedAutoJoinMetricSubmission]
+ -[CWFAutoJoinManager __submitAutoJoinMetric:]
+ -[CWFAutoJoinManager __unscheduleDelayedAutoJoinMetricSubmission]
+ -[CWFAutoJoinManager __updateAutoJoinMetricAndStatistics:]
+ -[CWFAutoJoinManager __updateAutoJoinMetricWithJoinStatus]
+ -[CWFAutoJoinManager displayOff]
+ -[CWFAutoJoinManager joinStatus]
+ -[CWFAutoJoinManager setDisplayOff:]
+ -[CWFAutoJoinManager setJoinStatus:]
+ -[CWFAutoJoinMetric autoHotspotEndedAt]
+ -[CWFAutoJoinMetric autoHotspotJoinStartedAt]
+ -[CWFAutoJoinMetric autoHotspotStartedAt]
+ -[CWFAutoJoinMetric autoJoinedNetwork]
+ -[CWFAutoJoinMetric bestCandidateRSSI]
+ -[CWFAutoJoinMetric candidateBSSCount]
+ -[CWFAutoJoinMetric candidateSSIDCount]
+ -[CWFAutoJoinMetric channelList]
+ -[CWFAutoJoinMetric didExclude6GHzOnlyNetwork]
+ -[CWFAutoJoinMetric didExcludeDisabledNetwork]
+ -[CWFAutoJoinMetric didExcludeDisallowedNetwork]
+ -[CWFAutoJoinMetric didExcludeLowRSSINetwork]
+ -[CWFAutoJoinMetric didExcludePartiallyMatchedNetwork]
+ -[CWFAutoJoinMetric didExcludeStandalone6GHzNetwork]
+ -[CWFAutoJoinMetric didJoinDeferredNetwork]
+ -[CWFAutoJoinMetric didJoinPreviouslyAssociatedNetwork]
+ -[CWFAutoJoinMetric didJoinPreviouslyLowRSSINetwork]
+ -[CWFAutoJoinMetric didUserJoinDeferredNetwork]
+ -[CWFAutoJoinMetric didUserJoinDisallowedNetwork]
+ -[CWFAutoJoinMetric didUserJoinKnownNetwork]
+ -[CWFAutoJoinMetric didUserJoinLowRSSINetwork]
+ -[CWFAutoJoinMetric didUserJoinPartiallyMatchedNetwork]
+ -[CWFAutoJoinMetric endedAt]
+ -[CWFAutoJoinMetric joinEndedAt]
+ -[CWFAutoJoinMetric joinStartedAt]
+ -[CWFAutoJoinMetric linkRecoveryDelay]
+ -[CWFAutoJoinMetric matchedCandidateAt]
+ -[CWFAutoJoinMetric primaryIPv4InterfaceAt]
+ -[CWFAutoJoinMetric primaryIPv6InterfaceAt]
+ -[CWFAutoJoinMetric routableIPv4AddressAt]
+ -[CWFAutoJoinMetric routableIPv6AddressAt]
+ -[CWFAutoJoinMetric setAutoHotspotEndedAt:]
+ -[CWFAutoJoinMetric setAutoHotspotJoinStartedAt:]
+ -[CWFAutoJoinMetric setAutoHotspotStartedAt:]
+ -[CWFAutoJoinMetric setAutoJoinedNetwork:]
+ -[CWFAutoJoinMetric setBestCandidateRSSI:]
+ -[CWFAutoJoinMetric setCandidateBSSCount:]
+ -[CWFAutoJoinMetric setCandidateSSIDCount:]
+ -[CWFAutoJoinMetric setChannelList:]
+ -[CWFAutoJoinMetric setDidExclude6GHzOnlyNetwork:]
+ -[CWFAutoJoinMetric setDidExcludeDisabledNetwork:]
+ -[CWFAutoJoinMetric setDidExcludeDisallowedNetwork:]
+ -[CWFAutoJoinMetric setDidExcludeLowRSSINetwork:]
+ -[CWFAutoJoinMetric setDidExcludePartiallyMatchedNetwork:]
+ -[CWFAutoJoinMetric setDidExcludeStandalone6GHzNetwork:]
+ -[CWFAutoJoinMetric setDidJoinDeferredNetwork:]
+ -[CWFAutoJoinMetric setDidJoinPreviouslyAssociatedNetwork:]
+ -[CWFAutoJoinMetric setDidJoinPreviouslyLowRSSINetwork:]
+ -[CWFAutoJoinMetric setDidUserJoinDeferredNetwork:]
+ -[CWFAutoJoinMetric setDidUserJoinDisallowedNetwork:]
+ -[CWFAutoJoinMetric setDidUserJoinKnownNetwork:]
+ -[CWFAutoJoinMetric setDidUserJoinLowRSSINetwork:]
+ -[CWFAutoJoinMetric setDidUserJoinPartiallyMatchedNetwork:]
+ -[CWFAutoJoinMetric setEndedAt:]
+ -[CWFAutoJoinMetric setJoinEndedAt:]
+ -[CWFAutoJoinMetric setJoinStartedAt:]
+ -[CWFAutoJoinMetric setLinkRecoveryDelay:]
+ -[CWFAutoJoinMetric setMatchedCandidateAt:]
+ -[CWFAutoJoinMetric setPrimaryIPv4InterfaceAt:]
+ -[CWFAutoJoinMetric setPrimaryIPv6InterfaceAt:]
+ -[CWFAutoJoinMetric setRoutableIPv4AddressAt:]
+ -[CWFAutoJoinMetric setRoutableIPv6AddressAt:]
+ -[CWFAutoJoinMetric setStartedAt:]
+ -[CWFAutoJoinMetric setTriggeredByAutoJoinEnabledAt:]
+ -[CWFAutoJoinMetric setTriggeredByDeviceWakeAt:]
+ -[CWFAutoJoinMetric setTriggeredByFirstUnlockAt:]
+ -[CWFAutoJoinMetric setTriggeredByLinkDownAt:]
+ -[CWFAutoJoinMetric setTriggeredByMotionEndedAt:]
+ -[CWFAutoJoinMetric setTriggeredByWiFiOnAt:]
+ -[CWFAutoJoinMetric setUserJoinedNetwork:]
+ -[CWFAutoJoinMetric setUserJoinedNetworkAt:]
+ -[CWFAutoJoinMetric setWasAlreadyAssociatedToNetwork:]
+ -[CWFAutoJoinMetric setWasDiscoveredVia6GHzFollowup:]
+ -[CWFAutoJoinMetric setWasLockdownModeEnabled:]
+ -[CWFAutoJoinMetric startedAt]
+ -[CWFAutoJoinMetric triggeredByAutoJoinEnabledAt]
+ -[CWFAutoJoinMetric triggeredByDeviceWakeAt]
+ -[CWFAutoJoinMetric triggeredByFirstUnlockAt]
+ -[CWFAutoJoinMetric triggeredByLinkDownAt]
+ -[CWFAutoJoinMetric triggeredByMotionEndedAt]
+ -[CWFAutoJoinMetric triggeredByWiFiOnAt]
+ -[CWFAutoJoinMetric userJoinedNetworkAt]
+ -[CWFAutoJoinMetric userJoinedNetwork]
+ -[CWFAutoJoinMetric wasAlreadyAssociatedToNetwork]
+ -[CWFAutoJoinMetric wasDiscoveredVia6GHzFollowup]
+ -[CWFAutoJoinMetric wasLockdownModeEnabled]
+ -[CWFAutoJoinStatistics knownNetworks]
+ -[CWFAutoJoinStatistics setKnownNetworks:]
+ -[CWFConfigurationProfileManager .cxx_destruct]
+ -[CWFConfigurationProfileManager __updateCachedMDMManagedProfileUUIDs:]
+ -[CWFConfigurationProfileManager activate]
+ -[CWFConfigurationProfileManager init]
+ -[CWFConfigurationProfileManager invalidate]
+ -[CWFConfigurationProfileManager isDeviceSupervised]
+ -[CWFConfigurationProfileManager isNetworkManagedByMDM:]
+ -[CWFDevice .cxx_destruct]
+ -[CWFDevice deviceName]
+ -[CWFDevice deviceRapportEffectiveIdentifier]
+ -[CWFDevice hasFetchedDeviceInfo]
+ -[CWFDevice hash]
+ -[CWFDevice initWithRapportDevice:]
+ -[CWFDevice initWithUserInfo:]
+ -[CWFDevice ipAddress]
+ -[CWFDevice isEqual:]
+ -[CWFDevice macAddress]
+ -[CWFDevice model]
+ -[CWFDevice productColor]
+ -[CWFDevice productMarketingName]
+ -[CWFDevice productType]
+ -[CWFDevice retryCount]
+ -[CWFDevice setDeviceName:]
+ -[CWFDevice setDeviceRapportEffectiveIdentifier:]
+ -[CWFDevice setIpAddress:]
+ -[CWFDevice setMacAddress:]
+ -[CWFDevice setModel:]
+ -[CWFDevice setProductColor:]
+ -[CWFDevice setProductMarketingName:]
+ -[CWFDevice setProductType:]
+ -[CWFDevice setRetryCount:]
+ -[CWFDevice userInfo]
+ -[CWFDeviceDiscoveryManager .cxx_destruct]
+ -[CWFDeviceDiscoveryManager _fetchAndUpdateActiveDevicesInfo]
+ -[CWFDeviceDiscoveryManager _fetchWiFiInfoForDevice:rapportDevice:]
+ -[CWFDeviceDiscoveryManager _fetchWiFiInfoForRapportDevice:completion:]
+ -[CWFDeviceDiscoveryManager _invalidateRapportTeardownTimer]
+ -[CWFDeviceDiscoveryManager _invalidateWiFiInfoRetryRequestTimer]
+ -[CWFDeviceDiscoveryManager _isRapportTeardownTimerValid]
+ -[CWFDeviceDiscoveryManager _isSupportedModel:]
+ -[CWFDeviceDiscoveryManager _isWiFiInfoRequestTimerValid]
+ -[CWFDeviceDiscoveryManager _registerExtractWiFiInfo]
+ -[CWFDeviceDiscoveryManager _resetRapportClientWithInvalidation:]
+ -[CWFDeviceDiscoveryManager _sendRapportMessageToDevice:requestID:request:options:completion:]
+ -[CWFDeviceDiscoveryManager _sendRapportMessageToDevice:withRequestID:request:options:completion:]
+ -[CWFDeviceDiscoveryManager _setupRapportClientWithReason:]
+ -[CWFDeviceDiscoveryManager _wifiInfo]
+ -[CWFDeviceDiscoveryManager activeDevices]
+ -[CWFDeviceDiscoveryManager delegates]
+ -[CWFDeviceDiscoveryManager fetchActiveDevices]
+ -[CWFDeviceDiscoveryManager fetchWiFiInfoForDevice:]
+ -[CWFDeviceDiscoveryManager init]
+ -[CWFDeviceDiscoveryManager invalidate]
+ -[CWFDeviceDiscoveryManager rapportClientActivationFailCount]
+ -[CWFDeviceDiscoveryManager rapportClient]
+ -[CWFDeviceDiscoveryManager rapportErrorRegex]
+ -[CWFDeviceDiscoveryManager rapportQueue]
+ -[CWFDeviceDiscoveryManager rapportTeardownTimer]
+ -[CWFDeviceDiscoveryManager registerDelegate:]
+ -[CWFDeviceDiscoveryManager retryDevices]
+ -[CWFDeviceDiscoveryManager setActiveDevices:]
+ -[CWFDeviceDiscoveryManager setDelegates:]
+ -[CWFDeviceDiscoveryManager setRapportClient:]
+ -[CWFDeviceDiscoveryManager setRapportClientActivationFailCount:]
+ -[CWFDeviceDiscoveryManager setRapportErrorRegex:]
+ -[CWFDeviceDiscoveryManager setRapportQueue:]
+ -[CWFDeviceDiscoveryManager setRapportTeardownTimer:]
+ -[CWFDeviceDiscoveryManager setRetryDevices:]
+ -[CWFDeviceDiscoveryManager setSetupReason:]
+ -[CWFDeviceDiscoveryManager setThisDeviceMACAddress:]
+ -[CWFDeviceDiscoveryManager setWifiInfoRetryRequestTimer:]
+ -[CWFDeviceDiscoveryManager setupReason]
+ -[CWFDeviceDiscoveryManager startDiscoveringDevicesIfNeeded:withReason:]
+ -[CWFDeviceDiscoveryManager thisDeviceMACAddress]
+ -[CWFDeviceDiscoveryManager unregisterDelegate:]
+ -[CWFDeviceDiscoveryManager wifiInfoRetryRequestTimer]
+ -[CWFHotspotClientManager .cxx_destruct]
+ -[CWFHotspotClientManager activeHotspotClients]
+ -[CWFHotspotClientManager clientAssociated:thisDeviceMACAddress:]
+ -[CWFHotspotClientManager clientAssociatedToHostPersonalHotspot:]
+ -[CWFHotspotClientManager clientDisassociated:]
+ -[CWFHotspotClientManager dealloc]
+ -[CWFHotspotClientManager deviceDiscoveryManager]
+ -[CWFHotspotClientManager didDiscoverDevice:]
+ -[CWFHotspotClientManager didFetchWifiInfoForDevice:]
+ -[CWFHotspotClientManager didLoseDevice:]
+ -[CWFHotspotClientManager hotspotDisabled]
+ -[CWFHotspotClientManager hotspotQueue]
+ -[CWFHotspotClientManager init]
+ -[CWFHotspotClientManager setActiveHotspotClients:]
+ -[CWFHotspotClientManager setDeviceDiscoveryManager:]
+ -[CWFHotspotClientManager setHotspotQueue:]
+ -[CWFInterface isDeviceSupervised]
+ -[CWFInterface isNetworkManagedByMDM:]
+ -[CWFNearbyDeviceDiscoveryFilter .cxx_destruct]
+ -[CWFNearbyDeviceDiscoveryFilter bssid]
+ -[CWFNearbyDeviceDiscoveryFilter copyWithZone:]
+ -[CWFNearbyDeviceDiscoveryFilter description]
+ -[CWFNearbyDeviceDiscoveryFilter encodeWithCoder:]
+ -[CWFNearbyDeviceDiscoveryFilter frameType]
+ -[CWFNearbyDeviceDiscoveryFilter hash]
+ -[CWFNearbyDeviceDiscoveryFilter initWithCoder:]
+ -[CWFNearbyDeviceDiscoveryFilter init]
+ -[CWFNearbyDeviceDiscoveryFilter isEqual:]
+ -[CWFNearbyDeviceDiscoveryFilter isEqualToNDDFilter:]
+ -[CWFNearbyDeviceDiscoveryFilter numReports]
+ -[CWFNearbyDeviceDiscoveryFilter receiverMacAddress]
+ -[CWFNearbyDeviceDiscoveryFilter setBssid:]
+ -[CWFNearbyDeviceDiscoveryFilter setFrameType:]
+ -[CWFNearbyDeviceDiscoveryFilter setNumReports:]
+ -[CWFNearbyDeviceDiscoveryFilter setReceiverMacAddress:]
+ -[CWFNearbyDeviceDiscoveryFilter setTransmitterMacAddress:]
+ -[CWFNearbyDeviceDiscoveryFilter transmitterMacAddress]
+ -[CWFNearbyDeviceDiscoveryParameter filters]
+ -[CWFNearbyDeviceDiscoveryParameter setFilters:]
+ -[CWFNearbyDeviceDiscoveryReport bssid]
+ -[CWFNearbyDeviceDiscoveryReport isEqualToNDDReport:]
+ -[CWFNearbyDeviceDiscoveryReport receiver]
+ -[CWFNearbyDeviceDiscoveryReport setBssid:]
+ -[CWFNearbyDeviceDiscoveryReport setReceiver:]
+ -[CWFNearbyDeviceDiscoveryReport setTransmitter:]
+ -[CWFNearbyDeviceDiscoveryReport transmitter]
+ -[CWFNetworkProfile cachedNetworkID]
+ -[CWFNetworkProfile deepCopy]
+ -[CWFNetworkProfile defaultPrivateMACMode]
+ -[CWFNetworkProfile effectivePrivateMACModeWithSystemSetting:]
+ -[CWFNetworkProfile isAddReasonCarrierBundle]
+ -[CWFNetworkProfile isPayloadIdentifierTelemetryApproved]
+ -[CWFNetworkProfile payloadIdentifier]
+ -[CWFNetworkProfile setCachedNetworkID:]
+ -[CWFNetworkProfile setPayloadIdentifier:]
+ -[CWFNetworkProfile setPayloadIdentifierTelemetryApproved:]
+ -[CWFPrivateMACManager setUpdatedNetworkIDHandler:]
+ -[CWFPrivateMACManager updatedNetworkIDHandler]
+ -[CWFXPCConnection queryDeviceSupervisedWithRequestParams:reply:]
+ -[CWFXPCConnection queryNetworkManagedByMDM:requestParams:reply:]
+ -[CWFXPCManager autoJoinManager]
+ -[CWFXPCRequest cancel]
+ -[CWFXPCRequest setWaitingToSendResponseBeforeFinish:]
+ -[CWFXPCRequest waitingToSendResponseBeforeFinish]
+ -[CWFXPCRequestProxy __getAutoJoinMetric:]
+ -[CWFXPCRequestProxy __getAutoJoinStatistics:]
+ -[CWFXPCRequestProxy __getDeviceSupervised:]
+ -[CWFXPCRequestProxy __getNetworkManagedByMDM:]
+ -[CWFXPCRequestProxy __hotspotClientManager]
+ -[CWFXPCRequestProxy __resetAutoJoinStatistics:]
+ -[CWFXPCRequestProxy __updateApple80211InterfacesWithReason:reply:]
+ -[CWFXPCRequestProxy __updateSystemConfigurationInterfacesWithReason:reply:]
+ -[CWFXPCRequestProxy __updateWiFiInterfacesWithReason:reply:]
+ -[CWFXPCRequestProxy autoJoinManager]
+ -[NSString(LocalDeviceDiscovery) _stringByReplacingOccurencesWithRegex:replacement:]
+ CWFGetPHOSLog.log
+ CWFGetPHOSLog.onceToken
+ CWFPayloadIdentifierTelemetryApprovedList.onceToken
+ GCC_except_table118
+ GCC_except_table119
+ GCC_except_table131
+ GCC_except_table132
+ GCC_except_table153
+ GCC_except_table171
+ GCC_except_table175
+ GCC_except_table191
+ GCC_except_table195
+ GCC_except_table207
+ GCC_except_table21
+ GCC_except_table221
+ GCC_except_table224
+ GCC_except_table227
+ GCC_except_table228
+ GCC_except_table233
+ GCC_except_table254
+ GCC_except_table26
+ GCC_except_table300
+ GCC_except_table305
+ GCC_except_table309
+ GCC_except_table31
+ GCC_except_table346
+ GCC_except_table35
+ GCC_except_table368
+ GCC_except_table38
+ GCC_except_table384
+ GCC_except_table41
+ GCC_except_table42
+ GCC_except_table484
+ GCC_except_table65
+ GCC_except_table654
+ GCC_except_table657
+ GCC_except_table71
+ GCC_except_table76
+ GCC_except_table82
+ GCC_except_table86
+ MobileAssetLibraryCore.frameworkLibrary
+ OBJC_IVAR_$_CWFAssetLocal._assetID
+ OBJC_IVAR_$_CWFAssetLocal._assetSpecifier
+ OBJC_IVAR_$_CWFAssetLocal._assetType
+ OBJC_IVAR_$_CWFAssetLocal._assetVersion
+ OBJC_IVAR_$_CWFAssetLocal._firstSupportedBuild
+ OBJC_IVAR_$_CWFAssetLocal._lastSupportedBuild
+ OBJC_IVAR_$_CWFAssetLocal._localURL
+ OBJC_IVAR_$_CWFAssetManager._assetDidChangeHandler
+ OBJC_IVAR_$_CWFAssetManager._assetPowerTable
+ OBJC_IVAR_$_CWFAssetManager._assetSpecifier
+ OBJC_IVAR_$_CWFAssetManager._currentLockedAutoAsset
+ OBJC_IVAR_$_CWFAssetManager._currentLockedAutoAssetSelector
+ OBJC_IVAR_$_CWFAssetManager._eventQueue
+ OBJC_IVAR_$_CWFAssetManager._interestSet
+ OBJC_IVAR_$_CWFAssetManager._notifyTokenVersionDownloaded
+ OBJC_IVAR_$_CWFAssetManager._periodicCheckEnabled
+ OBJC_IVAR_$_CWFAssetManager._periodicCheckTimer
+ OBJC_IVAR_$_CWFAssetManager._periodicityInSecs
+ OBJC_IVAR_$_CWFAssetPowerTable._allowTestingOnUnSupportedChipset
+ OBJC_IVAR_$_CWFAssetPowerTable.numberOfCallsToCopyAsset
+ OBJC_IVAR_$_CWFAssetPowerTable.numberOfSuccessfullAssetCopy
+ OBJC_IVAR_$_CWFAssetPowerTable.numberOfTimesAssetExisted
+ OBJC_IVAR_$_CWFAutoJoinManager._delayedAutoJoinMetricSubmissionTimer
+ OBJC_IVAR_$_CWFAutoJoinManager._delayedSubmissionMetric
+ OBJC_IVAR_$_CWFAutoJoinManager._displayOff
+ OBJC_IVAR_$_CWFAutoJoinManager._joinStatus
+ OBJC_IVAR_$_CWFAutoJoinManager._lowRSSICandidates
+ OBJC_IVAR_$_CWFAutoJoinManager._matchedCandidates
+ OBJC_IVAR_$_CWFAutoJoinManager._prevAssocBeforeTimestamp
+ OBJC_IVAR_$_CWFAutoJoinManager._prevAssociatedNetwork
+ OBJC_IVAR_$_CWFAutoJoinManager._prevLowRSSICandidates
+ OBJC_IVAR_$_CWFAutoJoinMetric._autoHotspotEndedAt
+ OBJC_IVAR_$_CWFAutoJoinMetric._autoHotspotJoinStartedAt
+ OBJC_IVAR_$_CWFAutoJoinMetric._autoHotspotStartedAt
+ OBJC_IVAR_$_CWFAutoJoinMetric._autoJoinedNetwork
+ OBJC_IVAR_$_CWFAutoJoinMetric._bestCandidateRSSI
+ OBJC_IVAR_$_CWFAutoJoinMetric._candidateBSSCount
+ OBJC_IVAR_$_CWFAutoJoinMetric._candidateSSIDCount
+ OBJC_IVAR_$_CWFAutoJoinMetric._channelList
+ OBJC_IVAR_$_CWFAutoJoinMetric._didExclude6GHzOnlyNetwork
+ OBJC_IVAR_$_CWFAutoJoinMetric._didExcludeDisabledNetwork
+ OBJC_IVAR_$_CWFAutoJoinMetric._didExcludeDisallowedNetwork
+ OBJC_IVAR_$_CWFAutoJoinMetric._didExcludeLowRSSINetwork
+ OBJC_IVAR_$_CWFAutoJoinMetric._didExcludePartiallyMatchedNetwork
+ OBJC_IVAR_$_CWFAutoJoinMetric._didExcludeStandalone6GHzNetwork
+ OBJC_IVAR_$_CWFAutoJoinMetric._didJoinDeferredNetwork
+ OBJC_IVAR_$_CWFAutoJoinMetric._didJoinPreviouslyAssociatedNetwork
+ OBJC_IVAR_$_CWFAutoJoinMetric._didJoinPreviouslyLowRSSINetwork
+ OBJC_IVAR_$_CWFAutoJoinMetric._didUserJoinDeferredNetwork
+ OBJC_IVAR_$_CWFAutoJoinMetric._didUserJoinDisallowedNetwork
+ OBJC_IVAR_$_CWFAutoJoinMetric._didUserJoinKnownNetwork
+ OBJC_IVAR_$_CWFAutoJoinMetric._didUserJoinLowRSSINetwork
+ OBJC_IVAR_$_CWFAutoJoinMetric._didUserJoinPartiallyMatchedNetwork
+ OBJC_IVAR_$_CWFAutoJoinMetric._endedAt
+ OBJC_IVAR_$_CWFAutoJoinMetric._joinEndedAt
+ OBJC_IVAR_$_CWFAutoJoinMetric._joinStartedAt
+ OBJC_IVAR_$_CWFAutoJoinMetric._linkRecoveryDelay
+ OBJC_IVAR_$_CWFAutoJoinMetric._matchedCandidateAt
+ OBJC_IVAR_$_CWFAutoJoinMetric._primaryIPv4InterfaceAt
+ OBJC_IVAR_$_CWFAutoJoinMetric._primaryIPv6InterfaceAt
+ OBJC_IVAR_$_CWFAutoJoinMetric._routableIPv4AddressAt
+ OBJC_IVAR_$_CWFAutoJoinMetric._routableIPv6AddressAt
+ OBJC_IVAR_$_CWFAutoJoinMetric._startedAt
+ OBJC_IVAR_$_CWFAutoJoinMetric._triggeredByAutoJoinEnabledAt
+ OBJC_IVAR_$_CWFAutoJoinMetric._triggeredByDeviceWakeAt
+ OBJC_IVAR_$_CWFAutoJoinMetric._triggeredByFirstUnlockAt
+ OBJC_IVAR_$_CWFAutoJoinMetric._triggeredByLinkDownAt
+ OBJC_IVAR_$_CWFAutoJoinMetric._triggeredByMotionEndedAt
+ OBJC_IVAR_$_CWFAutoJoinMetric._triggeredByWiFiOnAt
+ OBJC_IVAR_$_CWFAutoJoinMetric._userJoinedNetwork
+ OBJC_IVAR_$_CWFAutoJoinMetric._userJoinedNetworkAt
+ OBJC_IVAR_$_CWFAutoJoinMetric._wasAlreadyAssociatedToNetwork
+ OBJC_IVAR_$_CWFAutoJoinMetric._wasDiscoveredVia6GHzFollowup
+ OBJC_IVAR_$_CWFAutoJoinMetric._wasLockdownModeEnabled
+ OBJC_IVAR_$_CWFAutoJoinStatistics._knownNetworks
+ OBJC_IVAR_$_CWFConfigurationProfileManager._mdmManagedProfileUUIDs
+ OBJC_IVAR_$_CWFConfigurationProfileManager._profileManager
+ OBJC_IVAR_$_CWFDevice._deviceName
+ OBJC_IVAR_$_CWFDevice._deviceRapportEffectiveIdentifier
+ OBJC_IVAR_$_CWFDevice._ipAddress
+ OBJC_IVAR_$_CWFDevice._macAddress
+ OBJC_IVAR_$_CWFDevice._model
+ OBJC_IVAR_$_CWFDevice._productColor
+ OBJC_IVAR_$_CWFDevice._productMarketingName
+ OBJC_IVAR_$_CWFDevice._productType
+ OBJC_IVAR_$_CWFDevice._retryCount
+ OBJC_IVAR_$_CWFDeviceDiscoveryManager._activeDevices
+ OBJC_IVAR_$_CWFDeviceDiscoveryManager._delegates
+ OBJC_IVAR_$_CWFDeviceDiscoveryManager._rapportClient
+ OBJC_IVAR_$_CWFDeviceDiscoveryManager._rapportClientActivationFailCount
+ OBJC_IVAR_$_CWFDeviceDiscoveryManager._rapportErrorRegex
+ OBJC_IVAR_$_CWFDeviceDiscoveryManager._rapportQueue
+ OBJC_IVAR_$_CWFDeviceDiscoveryManager._rapportTeardownTimer
+ OBJC_IVAR_$_CWFDeviceDiscoveryManager._retryDevices
+ OBJC_IVAR_$_CWFDeviceDiscoveryManager._setupReason
+ OBJC_IVAR_$_CWFDeviceDiscoveryManager._thisDeviceMACAddress
+ OBJC_IVAR_$_CWFDeviceDiscoveryManager._wifiInfoRetryRequestTimer
+ OBJC_IVAR_$_CWFHotspotClientManager._activeHotspotClients
+ OBJC_IVAR_$_CWFHotspotClientManager._deviceDiscoveryManager
+ OBJC_IVAR_$_CWFHotspotClientManager._hotspotQueue
+ OBJC_IVAR_$_CWFNearbyDeviceDiscoveryFilter._bssid
+ OBJC_IVAR_$_CWFNearbyDeviceDiscoveryFilter._frameType
+ OBJC_IVAR_$_CWFNearbyDeviceDiscoveryFilter._numReports
+ OBJC_IVAR_$_CWFNearbyDeviceDiscoveryFilter._receiverMacAddress
+ OBJC_IVAR_$_CWFNearbyDeviceDiscoveryFilter._transmitterMacAddress
+ OBJC_IVAR_$_CWFNearbyDeviceDiscoveryParameter._filters
+ OBJC_IVAR_$_CWFNearbyDeviceDiscoveryReport._bssid
+ OBJC_IVAR_$_CWFNearbyDeviceDiscoveryReport._receiver
+ OBJC_IVAR_$_CWFNearbyDeviceDiscoveryReport._transmitter
+ OBJC_IVAR_$_CWFPrivateMACManager._updatedNetworkIDHandler
+ OBJC_IVAR_$_CWFXPCRequest._waitingToSendResponseBeforeFinish
+ OBJC_IVAR_$_CWFXPCRequestProxy._apple80211InterfaceQueue
+ OBJC_IVAR_$_CWFXPCRequestProxy._autoJoinManager
+ OBJC_IVAR_$_CWFXPCRequestProxy._configProfileManager
+ OBJC_IVAR_$_CWFXPCRequestProxy._hotspotClientManager
+ OBJC_IVAR_$_CWFXPCRequestProxy._mobileAssetManager
+ OBJC_IVAR_$_CWFXPCRequestProxy._systemConfigInterfaceQueue
+ RapportLibraryCore.frameworkLibrary
+ SoftwareUpdateCoreSupportLibraryCore.frameworkLibrary
+ _CFNotificationCenterGetDarwinNotifyCenter
+ _CFNotificationCenterGetLocalCenter
+ _CFNotificationCenterPostNotification
+ _CWFDescriptionForXPCRequest
+ _CWFGetPHOSLog
+ _CWFIsPayloadIdentifierTelemetryApproved
+ _CWFNetworkProfilePropertyCachedNetworkIDKey
+ _CWFNetworkProfilePropertyPayloadIdentifierKey
+ _CWFNetworkProfilePropertyPayloadIdentifierTelemetryApprovedKey
+ _CWFNetworkStackMACAddressWithInterfaceName
+ _CWFPayloadIdentifierTelemetryApprovedList
+ _MGCopyAnswer
+ _MGGetStringAnswer
+ _MobileAssetLibraryCore
+ _NSFileGroupOwnerAccountName
+ _NSFileOwnerAccountName
+ _OBJC_CLASS_$_CWFAssetLocal
+ _OBJC_CLASS_$_CWFAssetManager
+ _OBJC_CLASS_$_CWFAssetPowerTable
+ _OBJC_CLASS_$_CWFConfigurationProfileManager
+ _OBJC_CLASS_$_CWFDevice
+ _OBJC_CLASS_$_CWFDeviceDiscoveryManager
+ _OBJC_CLASS_$_CWFHotspotClientManager
+ _OBJC_CLASS_$_CWFNearbyDeviceDiscoveryFilter
+ _OBJC_CLASS_$_NSDistributedNotificationCenter
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_METACLASS_$_CWFAssetLocal
+ _OBJC_METACLASS_$_CWFAssetManager
+ _OBJC_METACLASS_$_CWFAssetPowerTable
+ _OBJC_METACLASS_$_CWFConfigurationProfileManager
+ _OBJC_METACLASS_$_CWFDevice
+ _OBJC_METACLASS_$_CWFDeviceDiscoveryManager
+ _OBJC_METACLASS_$_CWFHotspotClientManager
+ _OBJC_METACLASS_$_CWFNearbyDeviceDiscoveryFilter
+ _RapportLibraryCore
+ _SoftwareUpdateCoreSupportLibraryCore
+ __103-[CWFXPCConnection __addXPCRequestWithType:info:requestParams:parentRequestUUID:isParentRequest:reply:]_block_invoke.132
+ __103-[CWFXPCConnection __addXPCRequestWithType:info:requestParams:parentRequestUUID:isParentRequest:reply:]_block_invoke.136
+ __103-[CWFXPCConnection __addXPCRequestWithType:info:requestParams:parentRequestUUID:isParentRequest:reply:]_block_invoke.137
+ __103-[CWFXPCConnection __addXPCRequestWithType:info:requestParams:parentRequestUUID:isParentRequest:reply:]_block_invoke_2.133
+ __108-[CWFAutoJoinManager __calloutToAllowKnownNetwork:trigger:allowForSeamlessSSIDTransition:defer:queue:error:]_block_invoke.471
+ __108-[CWFAutoJoinManager __calloutToAllowKnownNetwork:trigger:allowForSeamlessSSIDTransition:defer:queue:error:]_block_invoke.472
+ __108-[CWFAutoJoinManager __calloutToAllowKnownNetwork:trigger:allowForSeamlessSSIDTransition:defer:queue:error:]_block_invoke.477
+ __26-[CWFAutoJoinManager init]_block_invoke.13
+ __32-[CWFAutoJoinManager invalidate]_block_invoke.16
+ __35-[CWFAutoJoinManager __addRequest:]_block_invoke.39
+ __35-[CWFAutoJoinManager __addRequest:]_block_invoke.40
+ __39-[CWFAutoJoinManager __performAutoJoin]_block_invoke.64
+ __39-[CWFAutoJoinManager __performAutoJoin]_block_invoke.94
+ __41-[CWFXPCRequestProxy __privateMACManager]_block_invoke.56
+ __41-[CWFXPCRequestProxy __privateMACManager]_block_invoke.57
+ __42-[CWFXPCRequestProxy __setupEventHandlers]_block_invoke.157
+ __42-[CWFXPCRequestProxy __setupEventHandlers]_block_invoke.170
+ __42-[CWFXPCRequestProxy __setupEventHandlers]_block_invoke.172
+ __42-[CWFXPCRequestProxy __setupEventHandlers]_block_invoke.182
+ __51-[CWFAutoJoinManager __sortJoinCandidates:context:]_block_invoke.279
+ __51-[CWFAutoJoinManager __sortJoinCandidates:context:]_block_invoke.305
+ __51-[CWFAutoJoinManager __sortJoinCandidates:context:]_block_invoke_2.314
+ __52-[CWFAutoJoinManager __calloutToAllowHotspot:error:]_block_invoke.515
+ __52-[CWFAutoJoinManager __calloutToAllowHotspot:error:]_block_invoke.516
+ __53-[CWFXPCRequestProxy __stopHostAPMode:XPCConnection:]_block_invoke.306
+ __54-[CWFXPCConnection beginActivity:requestParams:reply:]_block_invoke.153
+ __54-[CWFXPCConnection beginActivity:requestParams:reply:]_block_invoke.154
+ __54-[CWFXPCConnection beginActivity:requestParams:reply:]_block_invoke_2.155
+ __54-[CWFXPCRequestProxy __startHostAPMode:XPCConnection:]_block_invoke.299
+ __56-[CWFAutoJoinManager __calloutToConnectToHotspot:error:]_block_invoke.531
+ __56-[CWFAutoJoinManager __calloutToConnectToHotspot:error:]_block_invoke.532
+ __57-[CWFAutoJoinManager cancelAutoJoinWithUUID:error:reply:]_block_invoke.26
+ __57-[CWFAutoJoinManager cancelAutoJoinWithUUID:error:reply:]_block_invoke.31
+ __57-[CWFAutoJoinManager cancelAutoJoinWithUUID:error:reply:]_block_invoke.35
+ __57-[CWFAutoJoinManager cancelAutoJoinWithUUID:error:reply:]_block_invoke.36
+ __59-[CWFDeviceDiscoveryManager _setupRapportClientWithReason:]_block_invoke.100
+ __59-[CWFDeviceDiscoveryManager _setupRapportClientWithReason:]_block_invoke.101
+ __59-[CWFDeviceDiscoveryManager _setupRapportClientWithReason:]_block_invoke.102
+ __59-[CWFDeviceDiscoveryManager _setupRapportClientWithReason:]_block_invoke.107
+ __59-[CWFDeviceDiscoveryManager _setupRapportClientWithReason:]_block_invoke.108
+ __59-[CWFDeviceDiscoveryManager _setupRapportClientWithReason:]_block_invoke.111
+ __59-[CWFDeviceDiscoveryManager _setupRapportClientWithReason:]_block_invoke.115
+ __60-[CWFXPCConnection endActivityWithUUID:requestParams:reply:]_block_invoke.156
+ __60-[CWFXPCConnection endActivityWithUUID:requestParams:reply:]_block_invoke_2.157
+ __60-[CWFXPCRequestProxy __setupEventHandlersWithInterfaceName:]_block_invoke.104
+ __60-[CWFXPCRequestProxy __setupEventHandlersWithInterfaceName:]_block_invoke.109
+ __60-[CWFXPCRequestProxy __setupEventHandlersWithInterfaceName:]_block_invoke.114
+ __60-[CWFXPCRequestProxy __setupEventHandlersWithInterfaceName:]_block_invoke.115
+ __60-[CWFXPCRequestProxy __setupEventHandlersWithInterfaceName:]_block_invoke.116
+ __60-[CWFXPCRequestProxy __setupEventHandlersWithInterfaceName:]_block_invoke.120
+ __60-[CWFXPCRequestProxy __setupEventHandlersWithInterfaceName:]_block_invoke.130
+ __60-[CWFXPCRequestProxy __setupEventHandlersWithInterfaceName:]_block_invoke.81
+ __60-[CWFXPCRequestProxy __setupEventHandlersWithInterfaceName:]_block_invoke_2.131
+ __62-[CWFXPCRequestProxy __handleKnownNetworkProfileChangedEvent:]_block_invoke.190
+ __62-[CWFXPCRequestProxy __handleKnownNetworkProfileChangedEvent:]_block_invoke.191
+ __63-[CWFAutoJoinManager __calloutToAssociateWithParameters:error:]_block_invoke.500
+ __63-[CWFAutoJoinManager __calloutToAssociateWithParameters:error:]_block_invoke.501
+ __64-[CWFAutoJoinManager __calloutToAllowAutoJoinWithTrigger:error:]_block_invoke.463
+ __64-[CWFAutoJoinManager __calloutToAllowAutoJoinWithTrigger:error:]_block_invoke.464
+ __65-[CWFAutoJoinManager __updateDiscoverTimestampForJoinCandidates:]_block_invoke.147
+ __65-[CWFHotspotClientManager clientAssociated:thisDeviceMACAddress:]_block_invoke.8
+ __66-[CWFXPCConnection performScanWithParameters:requestParams:reply:]_block_invoke.165
+ __67-[CWFAutoJoinManager __calloutToAllowAutoHotspotWithTrigger:error:]_block_invoke.505
+ __67-[CWFAutoJoinManager __calloutToAllowAutoHotspotWithTrigger:error:]_block_invoke.506
+ __67-[CWFDeviceDiscoveryManager _fetchWiFiInfoForDevice:rapportDevice:]_block_invoke.127
+ __67-[CWFDeviceDiscoveryManager _fetchWiFiInfoForDevice:rapportDevice:]_block_invoke.128
+ __67-[CWFXPCConnection stopMonitoringAllEventsWithRequestParams:reply:]_block_invoke.151
+ __67-[CWFXPCConnection stopMonitoringAllEventsWithRequestParams:reply:]_block_invoke_2.152
+ __67-[CWFXPCRequestProxy __didFindMatching80211InterfaceForXPCRequest:]_block_invoke.43
+ __67-[CWFXPCRequestProxy __updateApple80211InterfacesWithReason:reply:]_block_invoke.144
+ __67-[CWFXPCRequestProxy __updateApple80211InterfacesWithReason:reply:]_block_invoke.145
+ __67-[CWFXPCRequestProxy __updateApple80211InterfacesWithReason:reply:]_block_invoke.149
+ __67-[CWFXPCRequestProxy __updateApple80211InterfacesWithReason:reply:]_block_invoke.150
+ __70-[CWFAutoJoinManager __updateRNRChannel:has6GHzOnlyBSS:joinCandidate:]_block_invoke.153
+ __72-[CWFAutoJoinManager __calloutToAllowJoinCandidate:trigger:defer:error:]_block_invoke.491
+ __72-[CWFAutoJoinManager __calloutToAllowJoinCandidate:trigger:defer:error:]_block_invoke.492
+ __76-[CWFXPCRequestProxy __updateSystemConfigurationInterfacesWithReason:reply:]_block_invoke.138
+ __76-[CWFXPCRequestProxy __updateSystemConfigurationInterfacesWithReason:reply:]_block_invoke.140
+ __76-[CWFXPCRequestProxy __updateSystemConfigurationInterfacesWithReason:reply:]_block_invoke.142
+ __79-[CWFXPCRequestProxy __getKnownNetworkInfoForLocalNetworkPrompt:XPCConnection:]_block_invoke.333
+ __80-[CWFXPCRequestProxy __privateMACSettingChangedForNetworkProfile:interfaceName:]_block_invoke.283
+ __81-[CWFXPCRequestProxy __updateCurrentKnownBSSWithIPConfigurationForInterfaceName:]_block_invoke.259
+ __81-[CWFXPCRequestProxy __updateCurrentKnownBSSWithIPConfigurationForInterfaceName:]_block_invoke.265
+ __82-[CWFAutoJoinManager __calloutToScanForNetworksWithParameters:scanChannels:error:]_block_invoke.480
+ __82-[CWFAutoJoinManager __calloutToScanForNetworksWithParameters:scanChannels:error:]_block_invoke.481
+ __86-[CWFAutoJoinManager __calloutToPerformGASQueryWithParameters:GASQueryNetworks:error:]_block_invoke.487
+ __86-[CWFAutoJoinManager __calloutToPerformGASQueryWithParameters:GASQueryNetworks:error:]_block_invoke.488
+ __90-[CWFAutoJoinManager __calloutToBrowseForHotspotsWithTimeout:maxCacheAge:cacheOnly:error:]_block_invoke.522
+ __90-[CWFAutoJoinManager __calloutToBrowseForHotspotsWithTimeout:maxCacheAge:cacheOnly:error:]_block_invoke.523
+ __94-[CWFDeviceDiscoveryManager _sendRapportMessageToDevice:requestID:request:options:completion:]_block_invoke.160
+ __CWFConvertObjectToJSON._dateFormatter
+ __CWFConvertObjectToJSON.onceToken
+ __OBJC_$_CLASS_METHODS_CWFAssetLocal
+ __OBJC_$_CLASS_METHODS_CWFAssetManager
+ __OBJC_$_CLASS_METHODS_CWFAssetPowerTable
+ __OBJC_$_CLASS_METHODS_CWFHotspotClientManager
+ __OBJC_$_CLASS_METHODS_CWFNearbyDeviceDiscoveryFilter
+ __OBJC_$_CLASS_METHODS_CWFXPCRequest
+ __OBJC_$_CLASS_PROP_LIST_CWFNearbyDeviceDiscoveryFilter
+ __OBJC_$_INSTANCE_METHODS_CWFAssetLocal
+ __OBJC_$_INSTANCE_METHODS_CWFAssetManager
+ __OBJC_$_INSTANCE_METHODS_CWFAssetPowerTable
+ __OBJC_$_INSTANCE_METHODS_CWFConfigurationProfileManager
+ __OBJC_$_INSTANCE_METHODS_CWFDevice
+ __OBJC_$_INSTANCE_METHODS_CWFDeviceDiscoveryManager
+ __OBJC_$_INSTANCE_METHODS_CWFHotspotClientManager
+ __OBJC_$_INSTANCE_METHODS_CWFNearbyDeviceDiscoveryFilter
+ __OBJC_$_INSTANCE_VARIABLES_CWFAssetLocal
+ __OBJC_$_INSTANCE_VARIABLES_CWFAssetManager
+ __OBJC_$_INSTANCE_VARIABLES_CWFAssetPowerTable
+ __OBJC_$_INSTANCE_VARIABLES_CWFConfigurationProfileManager
+ __OBJC_$_INSTANCE_VARIABLES_CWFDevice
+ __OBJC_$_INSTANCE_VARIABLES_CWFDeviceDiscoveryManager
+ __OBJC_$_INSTANCE_VARIABLES_CWFHotspotClientManager
+ __OBJC_$_INSTANCE_VARIABLES_CWFNearbyDeviceDiscoveryFilter
+ __OBJC_$_PROP_LIST_CWFAssetLocal
+ __OBJC_$_PROP_LIST_CWFAssetManager
+ __OBJC_$_PROP_LIST_CWFAssetPowerTable
+ __OBJC_$_PROP_LIST_CWFDevice
+ __OBJC_$_PROP_LIST_CWFDeviceDiscoveryManager
+ __OBJC_$_PROP_LIST_CWFHotspotClientManager
+ __OBJC_$_PROP_LIST_CWFNearbyDeviceDiscoveryFilter
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CWFDeviceDiscoveryManagerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CWFDeviceDiscoveryManagerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CWFDeviceDiscoveryManagerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_CWFHotspotClientManager
+ __OBJC_CLASS_PROTOCOLS_$_CWFNearbyDeviceDiscoveryFilter
+ __OBJC_CLASS_RO_$_CWFAssetLocal
+ __OBJC_CLASS_RO_$_CWFAssetManager
+ __OBJC_CLASS_RO_$_CWFAssetPowerTable
+ __OBJC_CLASS_RO_$_CWFConfigurationProfileManager
+ __OBJC_CLASS_RO_$_CWFDevice
+ __OBJC_CLASS_RO_$_CWFDeviceDiscoveryManager
+ __OBJC_CLASS_RO_$_CWFHotspotClientManager
+ __OBJC_CLASS_RO_$_CWFNearbyDeviceDiscoveryFilter
+ __OBJC_LABEL_PROTOCOL_$_CWFDeviceDiscoveryManagerDelegate
+ __OBJC_METACLASS_RO_$_CWFAssetLocal
+ __OBJC_METACLASS_RO_$_CWFAssetManager
+ __OBJC_METACLASS_RO_$_CWFAssetPowerTable
+ __OBJC_METACLASS_RO_$_CWFConfigurationProfileManager
+ __OBJC_METACLASS_RO_$_CWFDevice
+ __OBJC_METACLASS_RO_$_CWFDeviceDiscoveryManager
+ __OBJC_METACLASS_RO_$_CWFHotspotClientManager
+ __OBJC_METACLASS_RO_$_CWFNearbyDeviceDiscoveryFilter
+ __OBJC_PROTOCOL_$_CWFDeviceDiscoveryManagerDelegate
+ ___34-[CWFInterface isDeviceSupervised]_block_invoke
+ ___34-[CWFInterface isDeviceSupervised]_block_invoke_2
+ ___37-[CWFXPCRequestProxy autoJoinManager]_block_invoke
+ ___38-[CWFAssetManager enablePeriodicCheck]_block_invoke
+ ___38-[CWFInterface isNetworkManagedByMDM:]_block_invoke
+ ___38-[CWFInterface isNetworkManagedByMDM:]_block_invoke_2
+ ___39+[CWFAssetPowerTable hashedChipsetName]_block_invoke
+ ___39-[CWFAssetManager startEventMonitoring]_block_invoke
+ ___39-[CWFAssetManager startEventMonitoring]_block_invoke_2
+ ___39-[CWFDeviceDiscoveryManager invalidate]_block_invoke
+ ___41+[CWFHotspotClientManager sharedInstance]_block_invoke
+ ___42-[CWFHotspotClientManager hotspotDisabled]_block_invoke
+ ___45-[CWFAutoJoinManager __submitAutoJoinMetric:]_block_invoke
+ ___46-[CWFAutoJoinMetric coreAnalyticsEventPayload]_block_invoke
+ ___46-[CWFDeviceDiscoveryManager registerDelegate:]_block_invoke
+ ___47-[CWFDeviceDiscoveryManager fetchActiveDevices]_block_invoke
+ ___47-[CWFHotspotClientManager clientDisassociated:]_block_invoke
+ ___48-[CWFDeviceDiscoveryManager unregisterDelegate:]_block_invoke
+ ___49-[CWFXPCRequestProxy __updateWiFiNetworkServices]_block_invoke_3
+ ___52-[CWFDeviceDiscoveryManager fetchWiFiInfoForDevice:]_block_invoke
+ ___52-[CWFDeviceDiscoveryManager fetchWiFiInfoForDevice:]_block_invoke_2
+ ___53-[CWFDeviceDiscoveryManager _registerExtractWiFiInfo]_block_invoke
+ ___53-[CWFHotspotClientManager didFetchWifiInfoForDevice:]_block_invoke
+ ___56-[CWFAssetManager _registerForAssetChangedNotification:]_block_invoke
+ ___59-[CWFDeviceDiscoveryManager _setupRapportClientWithReason:]_block_invoke
+ ___61-[CWFDeviceDiscoveryManager _fetchAndUpdateActiveDevicesInfo]_block_invoke
+ ___61-[CWFXPCRequestProxy __updateWiFiInterfacesWithReason:reply:]_block_invoke
+ ___62-[NSString(LocalDeviceDiscovery) _stringByRemovingServiceName]_block_invoke
+ ___63-[CWFAutoJoinManager __scheduleDelayedAutoJoinMetricSubmission]_block_invoke
+ ___65-[CWFAutoJoinManager __unscheduleDelayedAutoJoinMetricSubmission]_block_invoke
+ ___65-[CWFHotspotClientManager clientAssociated:thisDeviceMACAddress:]_block_invoke
+ ___65-[CWFHotspotClientManager clientAssociatedToHostPersonalHotspot:]_block_invoke
+ ___65-[CWFXPCConnection queryNetworkManagedByMDM:requestParams:reply:]_block_invoke
+ ___65-[CWFXPCConnection queryNetworkManagedByMDM:requestParams:reply:]_block_invoke_2
+ ___67-[CWFDeviceDiscoveryManager _fetchWiFiInfoForDevice:rapportDevice:]_block_invoke
+ ___67-[CWFXPCRequestProxy __updateApple80211InterfacesWithReason:reply:]_block_invoke
+ ___67-[CWFXPCRequestProxy __updateApple80211InterfacesWithReason:reply:]_block_invoke_2
+ ___71-[CWFDeviceDiscoveryManager _fetchWiFiInfoForRapportDevice:completion:]_block_invoke
+ ___72-[CWFDeviceDiscoveryManager startDiscoveringDevicesIfNeeded:withReason:]_block_invoke
+ ___76-[CWFXPCRequestProxy __updateSystemConfigurationInterfacesWithReason:reply:]_block_invoke
+ ___76-[CWFXPCRequestProxy __updateSystemConfigurationInterfacesWithReason:reply:]_block_invoke_2
+ ___80-[CWFPrivateMACManager setNetworkIDForAssociationWithMACAddress:networkProfile:]_block_invoke
+ ___94-[CWFDeviceDiscoveryManager _sendRapportMessageToDevice:requestID:request:options:completion:]_block_invoke
+ ___CWFGetPHOSLog_block_invoke
+ ___CWFPayloadIdentifierTelemetryApprovedList_block_invoke
+ ___MobileAssetLibraryCore_block_invoke
+ ___RapportLibraryCore_block_invoke
+ ___SoftwareUpdateCoreSupportLibraryCore_block_invoke
+ ____CWFColocated6ENetworksMatchingScanResult_block_invoke.280
+ ____CWFColocated6ENetworksMatchingScanResult_block_invoke_2.281
+ _____CWFConvertObjectToJSON_block_invoke
+ ___block_descriptor_100_e8_32s40s48s56s64s72bs_e34_v24?0"NSError"8"NSDictionary"16l
+ ___block_descriptor_116_e8_32s40s48s56s64s72s80s88bs_e5_v8?0l
+ ___block_descriptor_152_e8_32s40s48s56s64s72s80s88bs96r104r112r120r128r136r144r_e5_v8?0l
+ ___block_descriptor_200_e8_32s40s48bs56r64r72r80r88r96r104r112r120r128r136r144r152r160r168r176r184r192r_e5_v8?0l
+ ___block_descriptor_208_e8_32s40s48bs56r64r72r80r88r96r104r112r120r128r136r144r152r160r168r176r184r192r200r_e5_v8?0l
+ ___block_descriptor_32_e27_B24?0"CWFScanResult"8^B16l
+ ___block_descriptor_40_e8_32s_e15_v32?0816^B24l
+ ___block_descriptor_40_e8_32s_e49_v24?0"<CWFDeviceDiscoveryManagerDelegate>"8^B16l
+ ___block_descriptor_40_e8_32s_e57_v24?0"NSObject<CWFDeviceDiscoveryManagerDelegate>"8^B16l
+ ___block_descriptor_40_e8_32s_e8_v12?0i8l
+ ___block_descriptor_40_e8_32w_e31_v16?0"RPCompanionLinkDevice"8l
+ ___block_descriptor_40_e8_32w_e88_v32?0"NSDictionary"8"NSDictionary"16?<v?"NSDictionary""NSDictionary""NSError">24l
+ ___block_descriptor_48_e8_32r40w_e5_v8?0l
+ ___block_descriptor_48_e8_32s40bs_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24l
+ ___block_descriptor_48_e8_32s40r_e38_v32?0"RPCompanionLinkDevice"8Q16^B24l
+ ___block_descriptor_48_e8_32s40s_e12_v24?08^B16l
+ ___block_descriptor_48_e8_32s40s_e19_"NSDictionary"8?0l
+ ___block_descriptor_48_e8_32s40w_e17_v16?0"NSError"8l
+ ___block_descriptor_48_e8_32s40w_e27_v16?0"CWFNetworkProfile"8l
+ ___block_descriptor_48_e8_32s40w_e34_v24?0"NSDictionary"8"NSError"16l
+ ___block_descriptor_48_e8_32w_e31_v16?0"RPCompanionLinkDevice"8l
+ ___block_descriptor_56_e8_32s40s48w_e5_v8?0l
+ ___block_descriptor_56_e8_32s40w_e5_v8?0l
+ ___block_descriptor_61_e8_32s40s48s_e5_v8?0l
+ ___block_descriptor_77_e8_32s40s48s56bs_e5_v8?0l
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e17_v16?0"NSError"8l
+ ___copy_helper_block_e8_32r40w
+ ___copy_helper_block_e8_32s40s48b56r64r72r80r88r96r104r112r120r128r136r144r152r160r168r176r184r192r
+ ___copy_helper_block_e8_32s40s48b56r64r72r80r88r96r104r112r120r128r136r144r152r160r168r176r184r192r200r
+ ___copy_helper_block_e8_32s40s48s56s64s72s80b
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88b96r104r112r120r128r136r144r
+ ___destroy_helper_block_e8_32r40w
+ ___destroy_helper_block_e8_32s40s48s56r64r72r80r88r96r104r112r120r128r136r144r152r160r168r176r184r192r
+ ___destroy_helper_block_e8_32s40s48s56r64r72r80r88r96r104r112r120r128r136r144r152r160r168r176r184r192r200r
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96r104r112r120r128r136r144r
+ ___getCPInstalledProfilesDidChangeNotificationSymbolLoc_block_invoke
+ ___getCPProfileManagerClass_block_invoke
+ ___getCP_DeviceIsSupervisedSymbolLoc_block_invoke
+ ___getCP_ProfileInstalledFromUserEnrollmentMDMSymbolLoc_block_invoke
+ ___getMAAutoAssetClass_block_invoke
+ ___getMAAutoAssetNotificationsClass_block_invoke
+ ___getMAAutoAssetPolicyClass_block_invoke
+ ___getMAAutoAssetSelectorClass_block_invoke
+ ___getRPCompanionLinkClientClass_block_invoke
+ ___getSUCoreDeviceClass_block_invoke
+ ___getSUCoreRestoreVersionClass_block_invoke
+ ___os_log_helper_16_2_12_8_0_8_0_8_66_8_0_8_0_4_0_8_0_8_0_4_0_8_0_8_0_4_0
+ ___os_log_helper_16_2_18_8_0_8_0_8_0_8_0_8_0_8_0_8_66_8_0_8_0_8_66_8_0_8_0_8_66_8_0_8_0_8_66_8_66_8_66
+ ___os_log_helper_16_2_2_8_32_4_0
+ ___os_log_helper_16_2_3_8_0_8_0_8_66
+ ___os_log_helper_16_2_3_8_32_4_0_8_64
+ ___os_log_helper_16_2_3_8_32_4_0_8_66
+ ___os_log_helper_16_2_3_8_32_8_64_8_32
+ ___os_log_helper_16_2_4_8_0_8_0_8_32_8_64
+ ___os_log_helper_16_2_4_8_0_8_0_8_32_8_66
+ ___os_log_helper_16_2_4_8_0_8_0_8_64_8_64
+ ___os_log_helper_16_2_4_8_32_8_64_8_64_8_64
+ ___os_log_helper_16_2_5_8_0_8_0_8_66_8_66_8_66
+ ___os_log_helper_16_2_5_8_34_8_34_4_0_8_32_8_64
+ ___os_log_helper_16_2_5_8_34_8_34_4_0_8_64_8_64
+ ___os_log_helper_16_2_6_8_0_8_0_8_66_8_0_8_0_4_0
+ ___os_log_helper_16_2_6_8_34_8_34_4_0_8_64_8_64_8_64
+ ___os_log_helper_16_2_8_8_0_8_0_8_0_8_0_8_0_8_0_8_66_8_66
+ ___os_log_helper_16_2_8_8_32_8_64_8_64_8_64_8_64_8_64_8_64_8_64
+ __block_literal_global.176
+ __block_literal_global.193
+ __block_literal_global.199
+ __block_literal_global.201
+ __block_literal_global.21
+ __block_literal_global.228
+ __block_literal_global.235
+ __block_literal_global.283
+ __block_literal_global.336
+ __block_literal_global.338
+ __block_literal_global.443
+ __block_literal_global.445
+ __block_literal_global.459
+ __block_literal_global.462
+ __block_literal_global.470
+ __block_literal_global.479
+ __block_literal_global.490
+ __block_literal_global.499
+ __block_literal_global.504
+ __block_literal_global.514
+ __block_literal_global.521
+ __block_literal_global.530
+ _allApproved
+ _audit_stringMobileAsset
+ _audit_stringRapport
+ _audit_stringSoftwareUpdateCoreSupport
+ _dispatch_queue_attr_make_with_qos_class
+ _dispatch_source_testcancel
+ _dispatch_suspend
+ _getCPInstalledProfilesDidChangeNotification
+ _getCPInstalledProfilesDidChangeNotificationSymbolLoc
+ _getCPProfileManagerClass
+ _getCP_DeviceIsSupervised
+ _getCP_DeviceIsSupervisedSymbolLoc
+ _getCP_ProfileInstalledFromUserEnrollmentMDM
+ _getCP_ProfileInstalledFromUserEnrollmentMDMSymbolLoc
+ _getMAAutoAssetClass
+ _getMAAutoAssetNotificationsClass
+ _getMAAutoAssetPolicyClass
+ _getMAAutoAssetSelectorClass
+ _getRPCompanionLinkClientClass
+ _getSUCoreDeviceClass
+ _getSUCoreRestoreVersionClass
+ _kDeviceMACAddressKey
+ _kDeviceModelKey
+ _kDeviceNameKey
+ _kDeviceProductColorKey
+ _kDeviceProductMarketingNameKey
+ _kDeviceProductTypeKey
+ _kDeviceRapportEffectiveIdentifierKey
+ _kExtractWiFiInfoRequestID
+ _kRapportRequestTimeStampKey
+ _kWiFiInfoDeviceMACAddressKey
+ _notify_cancel
+ _notify_register_dispatch
+ _objc_msgSend$URLByAppendingPathComponent:
+ _objc_msgSend$__getAutoJoinMetric:
+ _objc_msgSend$__getAutoJoinStatistics:
+ _objc_msgSend$__getDeviceSupervised:
+ _objc_msgSend$__getNetworkManagedByMDM:
+ _objc_msgSend$__isEnabledKnownNetworkNearby
+ _objc_msgSend$__periodicCheck
+ _objc_msgSend$__resetAutoJoinStatistics:
+ _objc_msgSend$__scheduleDelayedAutoJoinMetricSubmission
+ _objc_msgSend$__submitAutoJoinMetric:
+ _objc_msgSend$__unscheduleDelayedAutoJoinMetricSubmission
+ _objc_msgSend$__updateApple80211InterfacesWithReason:reply:
+ _objc_msgSend$__updateAutoJoinMetricAndStatistics:
+ _objc_msgSend$__updateAutoJoinMetricWithJoinStatus
+ _objc_msgSend$__updateCachedMDMManagedProfileUUIDs:
+ _objc_msgSend$__updateSystemConfigurationInterfacesWithReason:reply:
+ _objc_msgSend$__updateWiFiInterfacesWithReason:reply:
+ _objc_msgSend$_fetchWiFiInfoForDevice:rapportDevice:
+ _objc_msgSend$_fetchWiFiInfoForRapportDevice:completion:
+ _objc_msgSend$_handleAssetChangedNotification
+ _objc_msgSend$_invalidateRapportTeardownTimer
+ _objc_msgSend$_invalidateWiFiInfoRetryRequestTimer
+ _objc_msgSend$_isRapportTeardownTimerValid
+ _objc_msgSend$_isSupportedModel:
+ _objc_msgSend$_isWiFiInfoRequestTimerValid
+ _objc_msgSend$_registerExtractWiFiInfo
+ _objc_msgSend$_registerForAssetChangedNotification:
+ _objc_msgSend$_resetRapportClientWithInvalidation:
+ _objc_msgSend$_sendRapportMessageToDevice:requestID:request:options:completion:
+ _objc_msgSend$_setupRapportClientWithReason:
+ _objc_msgSend$_stringByReplacingOccurencesWithRegex:replacement:
+ _objc_msgSend$_wifiInfo
+ _objc_msgSend$activateWithCompletion:
+ _objc_msgSend$activeDevices
+ _objc_msgSend$activeHotspotClients
+ _objc_msgSend$allProfiles:
+ _objc_msgSend$assetDidChangeHandler
+ _objc_msgSend$assetID
+ _objc_msgSend$assetIDFromLocalURL:
+ _objc_msgSend$assetPowerTable
+ _objc_msgSend$assetSelector
+ _objc_msgSend$assetSpecifier
+ _objc_msgSend$assetSpecifierToTrack
+ _objc_msgSend$assetType
+ _objc_msgSend$assetVersion
+ _objc_msgSend$autoHotspotEndedAt
+ _objc_msgSend$autoHotspotJoinStartedAt
+ _objc_msgSend$autoHotspotStartedAt
+ _objc_msgSend$autoJoinManager
+ _objc_msgSend$autoJoinedNetwork
+ _objc_msgSend$availableForUseAttributes
+ _objc_msgSend$bestCandidateRSSI
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$bssid
+ _objc_msgSend$cachedNetworkID
+ _objc_msgSend$candidateBSSCount
+ _objc_msgSend$candidateSSIDCount
+ _objc_msgSend$channelList
+ _objc_msgSend$checkForNewerSync:withUsagePolicy:withTimeout:discoveredAttributes:error:
+ _objc_msgSend$compareOSRestoreVersion:withVersion:
+ _objc_msgSend$compareSUCoreRestoreVersion:withVersion:
+ _objc_msgSend$contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:
+ _objc_msgSend$copyItemAtURL:toURL:error:
+ _objc_msgSend$createDirectoryAtPath:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$createDirectoryAtURL:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$createTopLevelDir
+ _objc_msgSend$currentLatestAssetVersion
+ _objc_msgSend$currentLockedAutoAsset
+ _objc_msgSend$currentStatusSync:
+ _objc_msgSend$dataWithLength:
+ _objc_msgSend$defaultManager
+ _objc_msgSend$defaultPrivateMACMode
+ _objc_msgSend$delegates
+ _objc_msgSend$deregisterRequestID:
+ _objc_msgSend$deviceColor
+ _objc_msgSend$deviceDiscoveryManager
+ _objc_msgSend$deviceRapportEffectiveIdentifier
+ _objc_msgSend$didDiscoverDevice:
+ _objc_msgSend$didExclude6GHzOnlyNetwork
+ _objc_msgSend$didExcludeDisabledNetwork
+ _objc_msgSend$didExcludeDisallowedNetwork
+ _objc_msgSend$didExcludeLowRSSINetwork
+ _objc_msgSend$didExcludePartiallyMatchedNetwork
+ _objc_msgSend$didExcludeStandalone6GHzNetwork
+ _objc_msgSend$didFetchWifiInfoForDevice:
+ _objc_msgSend$didJoinDeferredNetwork
+ _objc_msgSend$didJoinPreviouslyAssociatedNetwork
+ _objc_msgSend$didJoinPreviouslyLowRSSINetwork
+ _objc_msgSend$didLoseDevice:
+ _objc_msgSend$didUserJoinDeferredNetwork
+ _objc_msgSend$didUserJoinDisallowedNetwork
+ _objc_msgSend$didUserJoinKnownNetwork
+ _objc_msgSend$didUserJoinLowRSSINetwork
+ _objc_msgSend$didUserJoinPartiallyMatchedNetwork
+ _objc_msgSend$displayOff
+ _objc_msgSend$earlierDate:
+ _objc_msgSend$effectiveIdentifier
+ _objc_msgSend$effectivePrivateMACModeWithSystemSetting:
+ _objc_msgSend$endAllPreviousLocksForSpecifier:
+ _objc_msgSend$endAllPreviousLocksOfSelectorSync:forClientName:
+ _objc_msgSend$endLockUsageSync:
+ _objc_msgSend$eventQueue
+ _objc_msgSend$fetchActiveDevices
+ _objc_msgSend$fetchWiFiInfoForDevice:
+ _objc_msgSend$fileExistsAtPath:isDirectory:
+ _objc_msgSend$fileURLWithPath:isDirectory:
+ _objc_msgSend$fileURLWithPathComponents:
+ _objc_msgSend$filters
+ _objc_msgSend$firstMatchInString:options:range:
+ _objc_msgSend$firstSupportedBuild
+ _objc_msgSend$garbageCollectWithNewAsset:prevAsset:
+ _objc_msgSend$getDeviceSKU
+ _objc_msgSend$hasFetchedDeviceInfo
+ _objc_msgSend$hashedChipsetName
+ _objc_msgSend$idsDeviceIdentifier
+ _objc_msgSend$initForAssetType:withAssetSpecifier:
+ _objc_msgSend$initForClientName:selectingAsset:error:
+ _objc_msgSend$initWithAssetType:assetSpecifier:assetVersion:attributes:localURL:
+ _objc_msgSend$initWithContentsOfURL:
+ _objc_msgSend$initWithDictionary:copyItems:
+ _objc_msgSend$initWithPattern:options:error:
+ _objc_msgSend$initWithRapportDevice:
+ _objc_msgSend$initWithRestoreVersion:
+ _objc_msgSend$integerForKey:
+ _objc_msgSend$interestInContentSync:withInterestPolicy:
+ _objc_msgSend$interestSet
+ _objc_msgSend$ipAddress
+ _objc_msgSend$isAddReasonCarrierBundle
+ _objc_msgSend$isComparable:
+ _objc_msgSend$isDeviceSupervised
+ _objc_msgSend$isEqualToNDDFilter:
+ _objc_msgSend$isEqualToNDDReport:
+ _objc_msgSend$isNetworkManagedByMDM:
+ _objc_msgSend$isPayloadIdentifierTelemetryApproved
+ _objc_msgSend$isSupportedChipset
+ _objc_msgSend$isSupportedDeviceClass
+ _objc_msgSend$isSupportedOTAPTUpdate
+ _objc_msgSend$isValidAssetVersion:
+ _objc_msgSend$isValidOSVersion:
+ _objc_msgSend$joinEndedAt
+ _objc_msgSend$joinStartedAt
+ _objc_msgSend$lastSupportedBuild
+ _objc_msgSend$linkRecoveryDelay
+ _objc_msgSend$localDevice
+ _objc_msgSend$localURL
+ _objc_msgSend$lockAndHandOffCanBlock:
+ _objc_msgSend$lockAutoAssetWithReason:isBlocking:
+ _objc_msgSend$lockContentSync:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:
+ _objc_msgSend$macAddress
+ _objc_msgSend$makeAutoAssetWithSelector:
+ _objc_msgSend$matchedCandidateAt
+ _objc_msgSend$metric
+ _objc_msgSend$mutableBytes
+ _objc_msgSend$notifyRegistrationName:forAssetType:forAssetSpecifier:
+ _objc_msgSend$notifyTokenVersionDownloaded
+ _objc_msgSend$numReports
+ _objc_msgSend$objectsPassingTest:
+ _objc_msgSend$path
+ _objc_msgSend$pathComponents
+ _objc_msgSend$payloadIdentifier
+ _objc_msgSend$periodicCheckTimer
+ _objc_msgSend$primaryIPv4InterfaceAt
+ _objc_msgSend$primaryIPv6InterfaceAt
+ _objc_msgSend$processLocalAsset:
+ _objc_msgSend$productColor
+ _objc_msgSend$productMarketingName
+ _objc_msgSend$productType
+ _objc_msgSend$profileUUID
+ _objc_msgSend$queryDeviceSupervisedWithRequestParams:reply:
+ _objc_msgSend$queryNetworkManagedByMDM:requestParams:reply:
+ _objc_msgSend$range
+ _objc_msgSend$rapportClient
+ _objc_msgSend$rapportClientActivationFailCount
+ _objc_msgSend$rapportErrorRegex
+ _objc_msgSend$rapportQueue
+ _objc_msgSend$rapportTeardownTimer
+ _objc_msgSend$receiver
+ _objc_msgSend$receiverMacAddress
+ _objc_msgSend$registerDelegate:
+ _objc_msgSend$registerRequestID:options:handler:
+ _objc_msgSend$removeItemAtURL:error:
+ _objc_msgSend$resetStatistics
+ _objc_msgSend$restoreVersion
+ _objc_msgSend$retryCount
+ _objc_msgSend$retryDevices
+ _objc_msgSend$routableIPv4AddressAt
+ _objc_msgSend$routableIPv6AddressAt
+ _objc_msgSend$sanityCheckOSRestoreVersion:
+ _objc_msgSend$sanityCheckSKUVersion:
+ _objc_msgSend$sendRequestID:request:destinationID:options:responseHandler:
+ _objc_msgSend$setAssetDidChangeHandler:
+ _objc_msgSend$setAttributes:ofItemAtPath:error:
+ _objc_msgSend$setAutoHotspotEndedAt:
+ _objc_msgSend$setAutoHotspotJoinStartedAt:
+ _objc_msgSend$setAutoHotspotStartedAt:
+ _objc_msgSend$setAutoJoinedNetwork:
+ _objc_msgSend$setBestCandidateRSSI:
+ _objc_msgSend$setBssid:
+ _objc_msgSend$setCandidateBSSCount:
+ _objc_msgSend$setCandidateSSIDCount:
+ _objc_msgSend$setChannelList:
+ _objc_msgSend$setControlFlags:
+ _objc_msgSend$setCurrentLockedAutoAsset:
+ _objc_msgSend$setCurrentLockedAutoAssetSelector:
+ _objc_msgSend$setDestinationDevice:
+ _objc_msgSend$setDeviceFoundHandler:
+ _objc_msgSend$setDeviceLostHandler:
+ _objc_msgSend$setDidExclude6GHzOnlyNetwork:
+ _objc_msgSend$setDidExcludeDisabledNetwork:
+ _objc_msgSend$setDidExcludeDisallowedNetwork:
+ _objc_msgSend$setDidExcludeLowRSSINetwork:
+ _objc_msgSend$setDidExcludePartiallyMatchedNetwork:
+ _objc_msgSend$setDidExcludeStandalone6GHzNetwork:
+ _objc_msgSend$setDidJoinDeferredNetwork:
+ _objc_msgSend$setDidJoinPreviouslyAssociatedNetwork:
+ _objc_msgSend$setDidJoinPreviouslyLowRSSINetwork:
+ _objc_msgSend$setDidUserJoinDeferredNetwork:
+ _objc_msgSend$setDidUserJoinDisallowedNetwork:
+ _objc_msgSend$setDidUserJoinKnownNetwork:
+ _objc_msgSend$setDidUserJoinLowRSSINetwork:
+ _objc_msgSend$setDidUserJoinPartiallyMatchedNetwork:
+ _objc_msgSend$setDispatchQueue:
+ _objc_msgSend$setFilters:
+ _objc_msgSend$setJoinEndedAt:
+ _objc_msgSend$setJoinStartedAt:
+ _objc_msgSend$setJoinStatus:
+ _objc_msgSend$setLinkRecoveryDelay:
+ _objc_msgSend$setMacAddress:
+ _objc_msgSend$setMatchedCandidateAt:
+ _objc_msgSend$setNotifyTokenVersionDownloaded:
+ _objc_msgSend$setNumReports:
+ _objc_msgSend$setPayloadIdentifierTelemetryApproved:
+ _objc_msgSend$setPrimaryIPv4InterfaceAt:
+ _objc_msgSend$setPrimaryIPv6InterfaceAt:
+ _objc_msgSend$setProductColor:
+ _objc_msgSend$setProductMarketingName:
+ _objc_msgSend$setRapportClient:
+ _objc_msgSend$setRapportClientActivationFailCount:
+ _objc_msgSend$setRapportTeardownTimer:
+ _objc_msgSend$setReceiver:
+ _objc_msgSend$setReceiverMacAddress:
+ _objc_msgSend$setRetryCount:
+ _objc_msgSend$setRoutableIPv4AddressAt:
+ _objc_msgSend$setRoutableIPv6AddressAt:
+ _objc_msgSend$setTargetUserSession:
+ _objc_msgSend$setThisDeviceMACAddress:
+ _objc_msgSend$setTransmitter:
+ _objc_msgSend$setTransmitterMacAddress:
+ _objc_msgSend$setTriggeredByAutoJoinEnabledAt:
+ _objc_msgSend$setTriggeredByDeviceWakeAt:
+ _objc_msgSend$setTriggeredByFirstUnlockAt:
+ _objc_msgSend$setTriggeredByLinkDownAt:
+ _objc_msgSend$setTriggeredByMotionEndedAt:
+ _objc_msgSend$setTriggeredByWiFiOnAt:
+ _objc_msgSend$setUpdatedNetworkIDHandler:
+ _objc_msgSend$setUserInitiated:
+ _objc_msgSend$setUserJoinedNetwork:
+ _objc_msgSend$setUserJoinedNetworkAt:
+ _objc_msgSend$setWaitingToSendResponseBeforeFinish:
+ _objc_msgSend$setWasAlreadyAssociatedToNetwork:
+ _objc_msgSend$setWasDiscoveredVia6GHzFollowup:
+ _objc_msgSend$setWasLockdownModeEnabled:
+ _objc_msgSend$setWifiInfoRetryRequestTimer:
+ _objc_msgSend$setupReason
+ _objc_msgSend$sharedDevice
+ _objc_msgSend$sharedInstance
+ _objc_msgSend$sharedProfileManager
+ _objc_msgSend$shouldAllowTestingOnUnSupportedChipset
+ _objc_msgSend$startDiscoveringDevicesIfNeeded:withReason:
+ _objc_msgSend$statistics
+ _objc_msgSend$thisDeviceMACAddress
+ _objc_msgSend$timeIntervalSinceNow
+ _objc_msgSend$transferAssetFromSrc:toDst:withAsseID:withVersion:firstSupportedBuild:lastSupportedBuild:
+ _objc_msgSend$transmitter
+ _objc_msgSend$transmitterMacAddress
+ _objc_msgSend$triggeredByAutoJoinEnabledAt
+ _objc_msgSend$triggeredByDeviceWakeAt
+ _objc_msgSend$triggeredByFirstUnlockAt
+ _objc_msgSend$triggeredByLinkDownAt
+ _objc_msgSend$triggeredByMotionEndedAt
+ _objc_msgSend$triggeredByWiFiOnAt
+ _objc_msgSend$unlockAssetWithReason:
+ _objc_msgSend$unregisterDelegate:
+ _objc_msgSend$updatedNetworkIDHandler
+ _objc_msgSend$uppercaseString
+ _objc_msgSend$userJoinedNetwork
+ _objc_msgSend$userJoinedNetworkAt
+ _objc_msgSend$waitingToSendResponseBeforeFinish
+ _objc_msgSend$wasAlreadyAssociatedToNetwork
+ _objc_msgSend$wasDiscoveredVia6GHzFollowup
+ _objc_msgSend$wasLockdownModeEnabled
+ _objc_msgSend$wifiInfoRetryRequestTimer
+ _objc_msgSend$writeToURL:error:
+ _objc_opt_new
+ _rapportClientActivationFailThreshold
+ _rapportTeardownTimeout
+ _stringByRemovingServiceName.onceToken
+ _stringByRemovingServiceName.serviceNameRegex
+ _stringByRemovingUnwantedCharacters.generatedUUIDPrefixRegex
+ _stringByRemovingUnwantedCharacters.localRegexRemovalRegex
+ _wifiInfoRetryThreshold
+ getCPInstalledProfilesDidChangeNotificationSymbolLoc.ptr
+ getCPProfileManagerClass.softClass
+ getCP_DeviceIsSupervisedSymbolLoc.ptr
+ getCP_ProfileInstalledFromUserEnrollmentMDMSymbolLoc.ptr
+ getMAAutoAssetClass.softClass
+ getMAAutoAssetNotificationsClass.softClass
+ getMAAutoAssetPolicyClass.softClass
+ getMAAutoAssetSelectorClass.softClass
+ getRPCompanionLinkClientClass.softClass
+ getSUCoreDeviceClass.softClass
+ getSUCoreRestoreVersionClass.softClass
+ hashedChipsetName.hashedName
+ hashedChipsetName.onceToken
+ sharedInstance.onceToken
+ sharedInstance.sharedClientManager
- -[CWFAutoJoinManager __isAnyKnownNetworkNearby]
- -[CWFAutoJoinManager __updateCachedMetricAndStatistics:]
- -[CWFAutoJoinMetric associatedNetwork]
- -[CWFAutoJoinMetric autoHotspotDuration]
- -[CWFAutoJoinMetric autoHotspotJoinDuration]
- -[CWFAutoJoinMetric candidates]
- -[CWFAutoJoinMetric durationFromDeviceUnlockTrigger]
- -[CWFAutoJoinMetric durationFromDisplayOnTrigger]
- -[CWFAutoJoinMetric durationFromLinkDownTrigger]
- -[CWFAutoJoinMetric durationFromNonRetryAutoJoinTrigger]
- -[CWFAutoJoinMetric durationFromWiFiPowerOnTrigger]
- -[CWFAutoJoinMetric duration]
- -[CWFAutoJoinMetric joinDuration]
- -[CWFAutoJoinMetric knownNetworks]
- -[CWFAutoJoinMetric network]
- -[CWFAutoJoinMetric optimizedChannelList]
- -[CWFAutoJoinMetric previousNonRetryAutoJoinTrigger]
- -[CWFAutoJoinMetric setAssociatedNetwork:]
- -[CWFAutoJoinMetric setAutoHotspotDuration:]
- -[CWFAutoJoinMetric setAutoHotspotJoinDuration:]
- -[CWFAutoJoinMetric setCandidates:]
- -[CWFAutoJoinMetric setDuration:]
- -[CWFAutoJoinMetric setDurationFromDeviceUnlockTrigger:]
- -[CWFAutoJoinMetric setDurationFromDisplayOnTrigger:]
- -[CWFAutoJoinMetric setDurationFromLinkDownTrigger:]
- -[CWFAutoJoinMetric setDurationFromNonRetryAutoJoinTrigger:]
- -[CWFAutoJoinMetric setDurationFromWiFiPowerOnTrigger:]
- -[CWFAutoJoinMetric setJoinDuration:]
- -[CWFAutoJoinMetric setKnownNetworks:]
- -[CWFAutoJoinMetric setNetwork:]
- -[CWFAutoJoinMetric setOptimizedChannelList:]
- -[CWFAutoJoinMetric setPreviousNonRetryAutoJoinTrigger:]
- -[CWFAutoJoinMetric setWasAlreadyAssociated:]
- -[CWFAutoJoinMetric wasAlreadyAssociated]
- -[CWFNearbyDeviceDiscoveryParameter macIds]
- -[CWFNearbyDeviceDiscoveryParameter setMacIds:]
- -[CWFNearbyDeviceDiscoveryReport isEqualToNDDParameters:]
- -[CWFNearbyDeviceDiscoveryReport macId]
- -[CWFNearbyDeviceDiscoveryReport setMacId:]
- -[CWFPrivateMACManager setUpdatedPrivateMACAddressHandler:]
- -[CWFPrivateMACManager updatedPrivateMACAddressHandler]
- -[CWFXPCRequest didSendResponse]
- -[CWFXPCRequest setDidSendResponse:]
- -[CWFXPCRequestProxy __updateWiFiNetworkInterfaces:reply:]
- -[NSString(LocalDeviceDiscovery) _stringByReplacingOccurencesOfRegexPattern:replacement:]
- GCC_except_table108
- GCC_except_table109
- GCC_except_table11
- GCC_except_table122
- GCC_except_table124
- GCC_except_table165
- GCC_except_table174
- GCC_except_table185
- GCC_except_table204
- GCC_except_table210
- GCC_except_table213
- GCC_except_table216
- GCC_except_table222
- GCC_except_table234
- GCC_except_table294
- GCC_except_table296
- GCC_except_table329
- GCC_except_table34
- GCC_except_table361
- GCC_except_table37
- GCC_except_table44
- GCC_except_table480
- GCC_except_table72
- GCC_except_table94
- OBJC_IVAR_$_CWFAutoJoinManager._previousNonRetryTrigger
- OBJC_IVAR_$_CWFAutoJoinMetric._associatedNetwork
- OBJC_IVAR_$_CWFAutoJoinMetric._autoHotspotDuration
- OBJC_IVAR_$_CWFAutoJoinMetric._autoHotspotJoinDuration
- OBJC_IVAR_$_CWFAutoJoinMetric._candidates
- OBJC_IVAR_$_CWFAutoJoinMetric._duration
- OBJC_IVAR_$_CWFAutoJoinMetric._durationFromDeviceUnlockTrigger
- OBJC_IVAR_$_CWFAutoJoinMetric._durationFromDisplayOnTrigger
- OBJC_IVAR_$_CWFAutoJoinMetric._durationFromLinkDownTrigger
- OBJC_IVAR_$_CWFAutoJoinMetric._durationFromNonRetryAutoJoinTrigger
- OBJC_IVAR_$_CWFAutoJoinMetric._durationFromWiFiPowerOnTrigger
- OBJC_IVAR_$_CWFAutoJoinMetric._joinDuration
- OBJC_IVAR_$_CWFAutoJoinMetric._knownNetworks
- OBJC_IVAR_$_CWFAutoJoinMetric._network
- OBJC_IVAR_$_CWFAutoJoinMetric._optimizedChannelList
- OBJC_IVAR_$_CWFAutoJoinMetric._previousNonRetryAutoJoinTrigger
- OBJC_IVAR_$_CWFAutoJoinMetric._wasAlreadyAssociated
- OBJC_IVAR_$_CWFNearbyDeviceDiscoveryParameter._macIds
- OBJC_IVAR_$_CWFNearbyDeviceDiscoveryReport._macId
- OBJC_IVAR_$_CWFPrivateMACManager._networkIDCache
- OBJC_IVAR_$_CWFPrivateMACManager._networkIDCacheIDList
- OBJC_IVAR_$_CWFPrivateMACManager._updatedPrivateMACAddressHandler
- OBJC_IVAR_$_CWFXPCRequest._didSendResponse
- OBJC_IVAR_$_CWFXPCRequestProxy._interfaceQueue
- __103-[CWFXPCConnection __addXPCRequestWithType:info:requestParams:parentRequestUUID:isParentRequest:reply:]_block_invoke.130
- __103-[CWFXPCConnection __addXPCRequestWithType:info:requestParams:parentRequestUUID:isParentRequest:reply:]_block_invoke.134
- __103-[CWFXPCConnection __addXPCRequestWithType:info:requestParams:parentRequestUUID:isParentRequest:reply:]_block_invoke.135
- __103-[CWFXPCConnection __addXPCRequestWithType:info:requestParams:parentRequestUUID:isParentRequest:reply:]_block_invoke_2.131
- __108-[CWFAutoJoinManager __calloutToAllowKnownNetwork:trigger:allowForSeamlessSSIDTransition:defer:queue:error:]_block_invoke.458
- __108-[CWFAutoJoinManager __calloutToAllowKnownNetwork:trigger:allowForSeamlessSSIDTransition:defer:queue:error:]_block_invoke.459
- __108-[CWFAutoJoinManager __calloutToAllowKnownNetwork:trigger:allowForSeamlessSSIDTransition:defer:queue:error:]_block_invoke.464
- __32-[CWFAutoJoinManager invalidate]_block_invoke.15
- __35-[CWFAutoJoinManager __addRequest:]_block_invoke.36
- __35-[CWFAutoJoinManager __addRequest:]_block_invoke.37
- __39-[CWFAutoJoinManager __performAutoJoin]_block_invoke.82
- __39-[CWFAutoJoinManager __performAutoJoin]_block_invoke.86
- __41-[CWFXPCRequestProxy __privateMACManager]_block_invoke.48
- __41-[CWFXPCRequestProxy __privateMACManager]_block_invoke.49
- __42-[CWFXPCRequestProxy __setupEventHandlers]_block_invoke.146
- __42-[CWFXPCRequestProxy __setupEventHandlers]_block_invoke.159
- __42-[CWFXPCRequestProxy __setupEventHandlers]_block_invoke.160
- __42-[CWFXPCRequestProxy __setupEventHandlers]_block_invoke.161
- __51-[CWFAutoJoinManager __sortJoinCandidates:context:]_block_invoke.266
- __51-[CWFAutoJoinManager __sortJoinCandidates:context:]_block_invoke.292
- __51-[CWFAutoJoinManager __sortJoinCandidates:context:]_block_invoke_2.301
- __52-[CWFAutoJoinManager __calloutToAllowHotspot:error:]_block_invoke.502
- __52-[CWFAutoJoinManager __calloutToAllowHotspot:error:]_block_invoke.503
- __53-[CWFXPCRequestProxy __stopHostAPMode:XPCConnection:]_block_invoke.299
- __54-[CWFXPCConnection beginActivity:requestParams:reply:]_block_invoke.151
- __54-[CWFXPCConnection beginActivity:requestParams:reply:]_block_invoke.152
- __54-[CWFXPCConnection beginActivity:requestParams:reply:]_block_invoke_2.153
- __54-[CWFXPCRequestProxy __startHostAPMode:XPCConnection:]_block_invoke.292
- __56-[CWFAutoJoinManager __calloutToConnectToHotspot:error:]_block_invoke.518
- __56-[CWFAutoJoinManager __calloutToConnectToHotspot:error:]_block_invoke.519
- __57-[CWFAutoJoinManager cancelAutoJoinWithUUID:error:reply:]_block_invoke.24
- __57-[CWFAutoJoinManager cancelAutoJoinWithUUID:error:reply:]_block_invoke.27
- __57-[CWFAutoJoinManager cancelAutoJoinWithUUID:error:reply:]_block_invoke.30
- __57-[CWFAutoJoinManager cancelAutoJoinWithUUID:error:reply:]_block_invoke.33
- __58-[CWFXPCRequestProxy __updateWiFiNetworkInterfaces:reply:]_block_invoke.128
- __58-[CWFXPCRequestProxy __updateWiFiNetworkInterfaces:reply:]_block_invoke.130
- __58-[CWFXPCRequestProxy __updateWiFiNetworkInterfaces:reply:]_block_invoke.132
- __58-[CWFXPCRequestProxy __updateWiFiNetworkInterfaces:reply:]_block_invoke.134
- __58-[CWFXPCRequestProxy __updateWiFiNetworkInterfaces:reply:]_block_invoke.136
- __58-[CWFXPCRequestProxy __updateWiFiNetworkInterfaces:reply:]_block_invoke.140
- __58-[CWFXPCRequestProxy __updateWiFiNetworkInterfaces:reply:]_block_invoke.141
- __59-[CWFPrivateMACManager privateMACAddressForNetworkProfile:]_block_invoke.18
- __60-[CWFXPCConnection endActivityWithUUID:requestParams:reply:]_block_invoke.154
- __60-[CWFXPCConnection endActivityWithUUID:requestParams:reply:]_block_invoke_2.155
- __60-[CWFXPCRequestProxy __setupEventHandlersWithInterfaceName:]_block_invoke.105
- __60-[CWFXPCRequestProxy __setupEventHandlersWithInterfaceName:]_block_invoke.106
- __60-[CWFXPCRequestProxy __setupEventHandlersWithInterfaceName:]_block_invoke.107
- __60-[CWFXPCRequestProxy __setupEventHandlersWithInterfaceName:]_block_invoke.111
- __60-[CWFXPCRequestProxy __setupEventHandlersWithInterfaceName:]_block_invoke.121
- __60-[CWFXPCRequestProxy __setupEventHandlersWithInterfaceName:]_block_invoke.72
- __60-[CWFXPCRequestProxy __setupEventHandlersWithInterfaceName:]_block_invoke.82
- __60-[CWFXPCRequestProxy __setupEventHandlersWithInterfaceName:]_block_invoke.95
- __60-[CWFXPCRequestProxy __setupEventHandlersWithInterfaceName:]_block_invoke_2.122
- __62-[CWFXPCRequestProxy __handleKnownNetworkProfileChangedEvent:]_block_invoke.183
- __62-[CWFXPCRequestProxy __handleKnownNetworkProfileChangedEvent:]_block_invoke.184
- __63-[CWFAutoJoinManager __calloutToAssociateWithParameters:error:]_block_invoke.487
- __63-[CWFAutoJoinManager __calloutToAssociateWithParameters:error:]_block_invoke.488
- __64-[CWFAutoJoinManager __calloutToAllowAutoJoinWithTrigger:error:]_block_invoke.450
- __64-[CWFAutoJoinManager __calloutToAllowAutoJoinWithTrigger:error:]_block_invoke.451
- __65-[CWFAutoJoinManager __updateDiscoverTimestampForJoinCandidates:]_block_invoke.139
- __66-[CWFXPCConnection performScanWithParameters:requestParams:reply:]_block_invoke.163
- __67-[CWFAutoJoinManager __calloutToAllowAutoHotspotWithTrigger:error:]_block_invoke.492
- __67-[CWFAutoJoinManager __calloutToAllowAutoHotspotWithTrigger:error:]_block_invoke.493
- __67-[CWFXPCConnection stopMonitoringAllEventsWithRequestParams:reply:]_block_invoke.149
- __67-[CWFXPCConnection stopMonitoringAllEventsWithRequestParams:reply:]_block_invoke_2.150
- __67-[CWFXPCRequestProxy __didFindMatching80211InterfaceForXPCRequest:]_block_invoke.35
- __70-[CWFAutoJoinManager __updateRNRChannel:has6GHzOnlyBSS:joinCandidate:]_block_invoke.145
- __72-[CWFAutoJoinManager __calloutToAllowJoinCandidate:trigger:defer:error:]_block_invoke.478
- __72-[CWFAutoJoinManager __calloutToAllowJoinCandidate:trigger:defer:error:]_block_invoke.479
- __79-[CWFXPCRequestProxy __getKnownNetworkInfoForLocalNetworkPrompt:XPCConnection:]_block_invoke.326
- __80-[CWFXPCRequestProxy __privateMACSettingChangedForNetworkProfile:interfaceName:]_block_invoke.276
- __81-[CWFXPCRequestProxy __updateCurrentKnownBSSWithIPConfigurationForInterfaceName:]_block_invoke.252
- __81-[CWFXPCRequestProxy __updateCurrentKnownBSSWithIPConfigurationForInterfaceName:]_block_invoke.258
- __82-[CWFAutoJoinManager __calloutToScanForNetworksWithParameters:scanChannels:error:]_block_invoke.467
- __82-[CWFAutoJoinManager __calloutToScanForNetworksWithParameters:scanChannels:error:]_block_invoke.468
- __86-[CWFAutoJoinManager __calloutToPerformGASQueryWithParameters:GASQueryNetworks:error:]_block_invoke.474
- __86-[CWFAutoJoinManager __calloutToPerformGASQueryWithParameters:GASQueryNetworks:error:]_block_invoke.475
- __90-[CWFAutoJoinManager __calloutToBrowseForHotspotsWithTimeout:maxCacheAge:cacheOnly:error:]_block_invoke.509
- __90-[CWFAutoJoinManager __calloutToBrowseForHotspotsWithTimeout:maxCacheAge:cacheOnly:error:]_block_invoke.510
- ___58-[CWFXPCRequestProxy __updateWiFiNetworkInterfaces:reply:]_block_invoke
- ___58-[CWFXPCRequestProxy __updateWiFiNetworkInterfaces:reply:]_block_invoke_2
- ___59-[CWFPrivateMACManager privateMACAddressForNetworkProfile:]_block_invoke
- ____CWFColocated6ENetworksMatchingScanResult_block_invoke.275
- ____CWFColocated6ENetworksMatchingScanResult_block_invoke_2.276
- ___block_descriptor_168_e8_32s40s48bs56r64r72r80r88r96r104r112r120r128r136r144r152r160r_e5_v8?0l
- ___block_descriptor_168_e8_32s40s48s56s64s72s80bs88r96r104r112r120r128r136r144r152r160r_e5_v8?0l
- ___block_descriptor_48_e8_32s40w_e40_v24?0"CWFNetworkProfile"8"NSString"16l
- ___block_descriptor_73_e8_32s40s48s56bs_e5_v8?0l
- ___block_descriptor_96_e8_32s40s48s56s64s72bs_e34_v24?0"NSError"8"NSDictionary"16l
- ___copy_helper_block_e8_32s40s48b56r64r72r80r88r96r104r112r120r128r136r144r152r160r
- ___copy_helper_block_e8_32s40s48s56s64s72s80b88r96r104r112r120r128r136r144r152r160r
- ___destroy_helper_block_e8_32s40s48s56r64r72r80r88r96r104r112r120r128r136r144r152r160r
- ___destroy_helper_block_e8_32s40s48s56s64s72s80s88r96r104r112r120r128r136r144r152r160r
- ___os_log_helper_16_2_21_8_0_8_0_8_34_8_34_4_0_8_66_8_0_8_0_8_0_8_0_8_0_8_0_8_0_8_0_8_0_8_0_8_66_8_66_8_66_8_66_8_66
- ___os_log_helper_16_2_7_8_0_8_0_8_34_8_34_4_0_8_32_8_64
- ___os_log_helper_16_2_7_8_0_8_0_8_34_8_34_4_0_8_32_8_66
- __block_literal_global.269
- __block_literal_global.271
- __block_literal_global.286
- __block_literal_global.294
- __block_literal_global.296
- __block_literal_global.446
- __block_literal_global.449
- __block_literal_global.457
- __block_literal_global.466
- __block_literal_global.473
- __block_literal_global.477
- __block_literal_global.491
- __block_literal_global.501
- __block_literal_global.508
- __block_literal_global.517
- __block_literal_global.57
- _objc_msgSend$__isAnyKnownNetworkNearby
- _objc_msgSend$__updateCachedMetricAndStatistics:
- _objc_msgSend$__updateWiFiNetworkInterfaces:reply:
- _objc_msgSend$_stringByReplacingOccurencesOfRegexPattern:replacement:
- _objc_msgSend$autoHotspotDuration
- _objc_msgSend$autoHotspotJoinDuration
- _objc_msgSend$candidates
- _objc_msgSend$didSendResponse
- _objc_msgSend$durationFromDeviceUnlockTrigger
- _objc_msgSend$durationFromDisplayOnTrigger
- _objc_msgSend$durationFromLinkDownTrigger
- _objc_msgSend$durationFromNonRetryAutoJoinTrigger
- _objc_msgSend$durationFromWiFiPowerOnTrigger
- _objc_msgSend$joinDuration
- _objc_msgSend$macId
- _objc_msgSend$macIds
- _objc_msgSend$network
- _objc_msgSend$optimizedChannelList
- _objc_msgSend$previousNonRetryAutoJoinTrigger
- _objc_msgSend$setAssociatedNetwork:
- _objc_msgSend$setAutoHotspotDuration:
- _objc_msgSend$setAutoHotspotJoinDuration:
- _objc_msgSend$setCandidates:
- _objc_msgSend$setDidSendResponse:
- _objc_msgSend$setDuration:
- _objc_msgSend$setDurationFromDeviceUnlockTrigger:
- _objc_msgSend$setDurationFromDisplayOnTrigger:
- _objc_msgSend$setDurationFromLinkDownTrigger:
- _objc_msgSend$setDurationFromNonRetryAutoJoinTrigger:
- _objc_msgSend$setDurationFromWiFiPowerOnTrigger:
- _objc_msgSend$setJoinDuration:
- _objc_msgSend$setMacId:
- _objc_msgSend$setMacIds:
- _objc_msgSend$setNetwork:
- _objc_msgSend$setOptimizedChannelList:
- _objc_msgSend$setPreviousNonRetryAutoJoinTrigger:
- _objc_msgSend$setUpdatedPrivateMACAddressHandler:
- _objc_msgSend$setWasAlreadyAssociated:
- _objc_msgSend$updatedPrivateMACAddressHandler
- _objc_msgSend$wasAlreadyAssociated
CStrings:
+ "![self __isEnabledKnownNetworkNearby]"
+ "%@%s-%ld"
+ "%@-%@"
+ "%@-%ld"
+ "%@/%@/%@"
+ "%@_%@"
+ "(CACHE)"
+ "([CWFAssetLocal isValidOSVersion:_firstSupportedBuild] && [CWFAssetLocal isValidOSVersion:_lastSupportedBuild])"
+ "(assetSpecifier && [assetSpecifier isEqual:[CWFAssetPowerTable assetSpecifierToTrack]])"
+ "(comparisonResult == 0 || comparisonResult == -1)"
+ "(deviceName && ![deviceName isEqual:@\"\"])"
+ "(restoreVersionCompatibilities && [restoreVersionCompatibilities count])"
+ "(supportedBuildRange && [supportedBuildRange count])"
+ "+[CWFAssetLocal isValidAssetVersion:]"
+ "+[CWFAssetLocal isValidOSVersion:]"
+ "+[CWFAssetManager endAllPreviousLocksForSpecifier:]"
+ "+[CWFAssetPowerTable getDeviceSKU]"
+ "-[CWFAssetLocal initWithAssetType:assetSpecifier:assetVersion:attributes:localURL:]"
+ "-[CWFAssetLocal sanityCheckOSRestoreVersion:]"
+ "-[CWFAssetManager __periodicCheck]"
+ "-[CWFAssetManager _registerForAssetChangedNotification:]"
+ "-[CWFAssetManager _registerForAssetChangedNotification:]_block_invoke"
+ "-[CWFAssetManager enablePeriodicCheck]"
+ "-[CWFAssetManager lockAndHandOffCanBlock:]"
+ "-[CWFAssetManager lockAutoAssetWithReason:isBlocking:]"
+ "-[CWFAssetManager makeAutoAssetWithSelector:]"
+ "-[CWFAssetManager startEventMonitoring]"
+ "-[CWFAssetManager startEventMonitoring]_block_invoke_2"
+ "-[CWFAssetManager unlockAssetWithReason:]"
+ "-[CWFAssetPowerTable createTopLevelDir]"
+ "-[CWFAssetPowerTable garbageCollectWithNewAsset:prevAsset:]"
+ "-[CWFAssetPowerTable processLocalAsset:]"
+ "-[CWFAssetPowerTable transferAssetFromSrc:toDst:withAsseID:withVersion:firstSupportedBuild:lastSupportedBuild:]"
+ "-[CWFDeviceDiscoveryManager _fetchWiFiInfoForDevice:rapportDevice:]_block_invoke"
+ "-[CWFDeviceDiscoveryManager _fetchWiFiInfoForRapportDevice:completion:]"
+ "-[CWFDeviceDiscoveryManager _invalidateRapportTeardownTimer]"
+ "-[CWFDeviceDiscoveryManager _invalidateWiFiInfoRetryRequestTimer]"
+ "-[CWFDeviceDiscoveryManager _registerExtractWiFiInfo]"
+ "-[CWFDeviceDiscoveryManager _registerExtractWiFiInfo]_block_invoke"
+ "-[CWFDeviceDiscoveryManager _resetRapportClientWithInvalidation:]"
+ "-[CWFDeviceDiscoveryManager _sendRapportMessageToDevice:requestID:request:options:completion:]"
+ "-[CWFDeviceDiscoveryManager _sendRapportMessageToDevice:requestID:request:options:completion:]_block_invoke"
+ "-[CWFDeviceDiscoveryManager _setupRapportClientWithReason:]"
+ "-[CWFDeviceDiscoveryManager _setupRapportClientWithReason:]_block_invoke"
+ "-[CWFDeviceDiscoveryManager fetchWiFiInfoForDevice:]"
+ "-[CWFDeviceDiscoveryManager invalidate]_block_invoke"
+ "-[CWFHotspotClientManager clientAssociated:thisDeviceMACAddress:]"
+ "-[CWFHotspotClientManager clientAssociated:thisDeviceMACAddress:]_block_invoke"
+ "-[CWFHotspotClientManager clientDisassociated:]"
+ "-[CWFHotspotClientManager clientDisassociated:]_block_invoke"
+ "-[CWFHotspotClientManager dealloc]"
+ "-[CWFHotspotClientManager didDiscoverDevice:]"
+ "-[CWFHotspotClientManager didFetchWifiInfoForDevice:]"
+ "-[CWFHotspotClientManager didLoseDevice:]"
+ "-[CWFHotspotClientManager hotspotDisabled]_block_invoke"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFApple80211.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFAssetLocal.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFAssetManager.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFAssetPowerTable.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFAutoJoinManager.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFBSS.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFHomeManager/CWFHomeManager.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFHomeManager/CWFSensingAutoDataCollector.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFHomeManager/CWFSensingHMADataCollector.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFIO80211.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFKernelEventMonitor.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFNearbyDeviceDiscoveryManager.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFNetworkProfile.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFPrivateMACManager.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFSCNetworkConfiguration.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFSCNetworkInterface.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFUtilInternal.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFUtilPrivate.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFXPCConnection.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFXPCManager.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFXPCProxy.m"
+ "/System/Library/PrivateFrameworks/MobileAsset.framework/Contents/MacOS/MobileAsset"
+ "/System/Library/PrivateFrameworks/Rapport.framework/Contents/MacOS/Rapport"
+ "/System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/Contents/MacOS/SoftwareUpdateCoreSupport"
+ "/private/var/db/ConnectivityPowerTableUpdates/"
+ "1"
+ "2OA"
+ "2OB"
+ "6e-mode=[off (%@)], "
+ "<CWFAssetPowerTable: currentLatestAssetVersion: %@, numberOfCallsToCopyAsset: %llu, numberOfTimesAssetExisted: %llu, numberOfSuccessfullAssetCopy: %llu"
+ "@\"CPProfileManager\""
+ "@\"CWFAssetManager\""
+ "@\"CWFAssetPowerTable\""
+ "@\"CWFAutoJoinManager\""
+ "@\"CWFConfigurationProfileManager\""
+ "@\"CWFDeviceDiscoveryManager\""
+ "@\"CWFHotspotClientManager\""
+ "@\"CWFJoinStatus\""
+ "@\"MAAutoAsset\""
+ "@\"MAAutoAssetSelector\""
+ "@\"NSRegularExpression\""
+ "@\"NSURL\""
+ "@\"RPCompanionLinkClient\""
+ "@56@0:8@16@24@32@40@48"
+ "@64@0:8@16@24@32@40@48@56"
+ "ASSET_VERSION_DOWNLOADED"
+ "B24@?0@\"CWFScanResult\"8^B16"
+ "BOOL getCP_DeviceIsSupervised()"
+ "BOOL getCP_ProfileInstalledFromUserEnrollmentMDM(CPProfile *__strong)"
+ "CPInstalledProfilesDidChangeNotification"
+ "CPProfileManager"
+ "CP_DeviceIsSupervised"
+ "CP_ProfileInstalledFromUserEnrollmentMDM"
+ "CWFAssetLocal"
+ "CWFAssetManager"
+ "CWFAssetPowerTable"
+ "CWFConfigurationProfileManager"
+ "CWFConfigurationProfileManager.m"
+ "CWFDevice"
+ "CWFDeviceDiscoveryManager"
+ "CWFDeviceDiscoveryManager.m"
+ "CWFDeviceDiscoveryManagerDelegate"
+ "CWFHotspotClientManager"
+ "CWFHotspotClientManager.m"
+ "CWFNearbyDeviceDiscoveryFilter"
+ "CachedNetworkID"
+ "CoreWiFiAssetMAClient"
+ "DeviceClass"
+ "DeviceColor"
+ "DeviceEnclosureColor"
+ "DeviceName"
+ "GET DEVICE SUPERVISED"
+ "GET NETWK MANAGED BY MDM"
+ "Info.plist"
+ "InternalBuild"
+ "LastKnownGood"
+ "Latest.plist"
+ "MAAutoAsset"
+ "MAAutoAssetNotifications"
+ "MAAutoAssetPolicy"
+ "MAAutoAssetSelector"
+ "Mac"
+ "NDD DONE"
+ "NDD RESULT"
+ "NSString *getCPInstalledProfilesDidChangeNotification(void)"
+ "OTAPeriodicCheckEnabled"
+ "OTAPeriodicCheckIntervalInSecs"
+ "OTAPowerTableAllowTestingOnUnSupportedChipset"
+ "Open known network profile never joined by user/UI unused for %d seconds"
+ "PayloadIdentifier"
+ "PayloadIdentifierTelemetryApproved"
+ "PowerTable"
+ "RPCompanionLinkClient"
+ "SUCoreDevice"
+ "SUCoreRestoreVersion"
+ "Successfull"
+ "T@\"CLLocation\",C,D"
+ "T@\"CWFAssetPowerTable\",&,N,V_assetPowerTable"
+ "T@\"CWFAutoJoinManager\",R"
+ "T@\"CWFDeviceDiscoveryManager\",&,N,V_deviceDiscoveryManager"
+ "T@\"CWFJoinStatus\",C,D"
+ "T@\"CWFScanResult\",C,D"
+ "T@\"CWFScanResult\",C,N,V_autoJoinedNetwork"
+ "T@\"CWFScanResult\",C,N,V_userJoinedNetwork"
+ "T@\"CWFScanResult\",C,N,V_wasAlreadyAssociatedToNetwork"
+ "T@\"MAAutoAsset\",&,N,V_currentLockedAutoAsset"
+ "T@\"MAAutoAssetSelector\",&,N,V_currentLockedAutoAssetSelector"
+ "T@\"NSArray\",C,N,V_channelList"
+ "T@\"NSArray\",C,N,V_filters"
+ "T@\"NSDate\",C,N,V_autoHotspotEndedAt"
+ "T@\"NSDate\",C,N,V_autoHotspotJoinStartedAt"
+ "T@\"NSDate\",C,N,V_autoHotspotStartedAt"
+ "T@\"NSDate\",C,N,V_joinEndedAt"
+ "T@\"NSDate\",C,N,V_joinStartedAt"
+ "T@\"NSDate\",C,N,V_matchedCandidateAt"
+ "T@\"NSDate\",C,N,V_primaryIPv4InterfaceAt"
+ "T@\"NSDate\",C,N,V_primaryIPv6InterfaceAt"
+ "T@\"NSDate\",C,N,V_routableIPv4AddressAt"
+ "T@\"NSDate\",C,N,V_routableIPv6AddressAt"
+ "T@\"NSDate\",C,N,V_triggeredByAutoJoinEnabledAt"
+ "T@\"NSDate\",C,N,V_triggeredByDeviceWakeAt"
+ "T@\"NSDate\",C,N,V_triggeredByFirstUnlockAt"
+ "T@\"NSDate\",C,N,V_triggeredByLinkDownAt"
+ "T@\"NSDate\",C,N,V_triggeredByMotionEndedAt"
+ "T@\"NSDate\",C,N,V_triggeredByWiFiOnAt"
+ "T@\"NSDate\",C,N,V_userJoinedNetworkAt"
+ "T@\"NSMutableDictionary\",&,N,V_retryDevices"
+ "T@\"NSMutableSet\",&,N,V_activeDevices"
+ "T@\"NSMutableSet\",&,N,V_activeHotspotClients"
+ "T@\"NSMutableSet\",&,N,V_delegates"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_eventQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_hotspotQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_rapportQueue"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_periodicCheckTimer"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_rapportTeardownTimer"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_wifiInfoRetryRequestTimer"
+ "T@\"NSRegularExpression\",&,N,V_rapportErrorRegex"
+ "T@\"NSSet\",C,D"
+ "T@\"NSString\",&,N,V_assetSpecifier"
+ "T@\"NSString\",&,N,V_deviceRapportEffectiveIdentifier"
+ "T@\"NSString\",C,N,V_bssid"
+ "T@\"NSString\",C,N,V_ipAddress"
+ "T@\"NSString\",C,N,V_macAddress"
+ "T@\"NSString\",C,N,V_model"
+ "T@\"NSString\",C,N,V_productColor"
+ "T@\"NSString\",C,N,V_productMarketingName"
+ "T@\"NSString\",C,N,V_productType"
+ "T@\"NSString\",C,N,V_receiver"
+ "T@\"NSString\",C,N,V_receiverMacAddress"
+ "T@\"NSString\",C,N,V_thisDeviceMACAddress"
+ "T@\"NSString\",C,N,V_transmitter"
+ "T@\"NSString\",C,N,V_transmitterMacAddress"
+ "T@\"NSString\",R,N,V_assetID"
+ "T@\"NSString\",R,N,V_assetSpecifier"
+ "T@\"NSString\",R,N,V_assetType"
+ "T@\"NSString\",R,N,V_assetVersion"
+ "T@\"NSString\",R,N,V_firstSupportedBuild"
+ "T@\"NSString\",R,N,V_lastSupportedBuild"
+ "T@\"NSURL\",R,N,V_localURL"
+ "T@\"RPCompanionLinkClient\",&,N,V_rapportClient"
+ "T@?,C,N,V_assetDidChangeHandler"
+ "T@?,C,V_updatedNetworkIDHandler"
+ "TARGET_OS_IOS && [getSUCoreRestoreVersionClass() class] && [getMAAutoAssetClass() class] && (MGCopyAnswer != NULL) && os_feature_enabled(CoreWiFi, WiFiOTAUpdatePT)"
+ "TB,N,V_allowTestingOnUnSupportedChipset"
+ "TB,N,V_didExclude6GHzOnlyNetwork"
+ "TB,N,V_didExcludeDisabledNetwork"
+ "TB,N,V_didExcludeDisallowedNetwork"
+ "TB,N,V_didExcludeLowRSSINetwork"
+ "TB,N,V_didExcludePartiallyMatchedNetwork"
+ "TB,N,V_didExcludeStandalone6GHzNetwork"
+ "TB,N,V_didJoinDeferredNetwork"
+ "TB,N,V_didJoinPreviouslyAssociatedNetwork"
+ "TB,N,V_didJoinPreviouslyLowRSSINetwork"
+ "TB,N,V_didUserJoinDeferredNetwork"
+ "TB,N,V_didUserJoinDisallowedNetwork"
+ "TB,N,V_didUserJoinKnownNetwork"
+ "TB,N,V_didUserJoinLowRSSINetwork"
+ "TB,N,V_didUserJoinPartiallyMatchedNetwork"
+ "TB,N,V_interestSet"
+ "TB,N,V_periodicCheckEnabled"
+ "TB,N,V_wasDiscoveredVia6GHzFollowup"
+ "TB,N,V_wasLockdownModeEnabled"
+ "TB,V_displayOff"
+ "TB,V_waitingToSendResponseBeforeFinish"
+ "TQ,N,V_candidateBSSCount"
+ "TQ,N,V_candidateSSIDCount"
+ "TQ,N,V_linkRecoveryDelay"
+ "TQ,N,V_rapportClientActivationFailCount"
+ "TQ,N,V_retryCount"
+ "TQ,N,V_setupReason"
+ "Ti,N,V_notifyTokenVersionDownloaded"
+ "Tq,N,V_bestCandidateRSSI"
+ "Tq,N,V_numReports"
+ "Tq,N,V_periodicityInSecs"
+ "URLByAppendingPathComponent:"
+ "WiFi/"
+ "WiFiOTAUpdatePT"
+ "WiFiSKU"
+ "WifiChipset"
+ "[A-F0-9]{8}-[A-F0-9]{4}-[A-F0-9]{4}-[A-F0-9]{4}-[A-F0-9]{12}"
+ "[CWFAssetLocal isValidAssetVersion:assetVersion]"
+ "[OTA] %s:  --- Received asset download notificaiton --- "
+ "[OTA] %s:  Begin: notify_register_dispatch's completion handler"
+ "[OTA] %s:  End: notify_register_dispatch's completion handler"
+ "[OTA] %s:  Entered"
+ "[OTA] %s:  Exiting"
+ "[OTA] %s:  Failed to unlock for reason:%@ with error: %@"
+ "[OTA] %s:  Interest registration failed for %@ with error: %@"
+ "[OTA] %s:  Interest registration succeeded for %@"
+ "[OTA] %s:  Not locking asset as interest is not yet set"
+ "[OTA] %s:  Skipping the end asset lock operation as it was never locked."
+ "[OTA] %s:  Unable to initialize autoAsset with requested assetSelector: %@, error: %@"
+ "[OTA] %s:  Unable to lock any version of auto-asset content, lockedAssetSelector: %@ error: %@"
+ "[OTA] %s:  Unlocked Assets"
+ "[OTA] %s:  localAsset did not populate"
+ "[OTA] %s:  notify_register_dispatch() returned token %d"
+ "[OTA] %s: %@: localURL: %@, assetID: %@, assetVersion: %@, firstSupportedBuild: %@, lastSupportedBuild: %@, error: %@"
+ "[OTA] %s: Asset is already locked! Unlocking first."
+ "[OTA] %s: Cannot create auto asset instance with selector: %@, error: %@"
+ "[OTA] %s: Completed for assetSelector: %@ with error: %@"
+ "[OTA] %s: Created .plist %@ with content %@"
+ "[OTA] %s: Current build is larger than last supported build currentRestoreVersion: %@, lastSupportedBuild: %@"
+ "[OTA] %s: Entered"
+ "[OTA] %s: Error: %@"
+ "[OTA] %s: Existing, nil localAsset"
+ "[OTA] %s: Exiting"
+ "[OTA] %s: Failed to copy assets recursively from %@ to %@ with error: %@"
+ "[OTA] %s: Failed to create .plist %@ with content %@ with error: %@"
+ "[OTA] %s: Failed to create new folder %@ with error: %@"
+ "[OTA] %s: Failed to create new folder %@, error: %@"
+ "[OTA] %s: Failed to enumerate all sub-dirs in %@ with error: %@"
+ "[OTA] %s: Failed to remove sub-dir %@ with error: %@"
+ "[OTA] %s: Failed to update .plist %@ atomically with content %@"
+ "[OTA] %s: Fetch status for locked auto asset: %@ completed with error: %@"
+ "[OTA] %s: First build is larger than current build firstSupportedBuild: %@, currentRestoreVersion: %@"
+ "[OTA] %s: First build is larger than last build. firstSupportedBuild: %@, lastSupportedBuild: %@"
+ "[OTA] %s: Found new version of asset with assetSelector: %@ and attributes: %@"
+ "[OTA] %s: Locked Asset: %@, Attributes: %@, localContentURL: %@"
+ "[OTA] %s: Malformed first or last supported builds. firstSupportedBuild: %@, lastSupportedBuild: %@"
+ "[OTA] %s: No availableForUseAttributes for status: %@"
+ "[OTA] %s: Not able to change ownership of %@, error: %@"
+ "[OTA] %s: OTA update of PT is disabled"
+ "[OTA] %s: Running on internal build"
+ "[OTA] %s: Same Version of asset is already downloaded. Error: %@"
+ "[OTA] %s: Setting up dispatch source for periodic check"
+ "[OTA] %s: Successfully locked the asset. currentLockedAutoAsset = %@"
+ "[OTA] %s: Successfully locked the asset. lockedAssetSelector = %@"
+ "[OTA] %s: The URL %@ for new asset already exist, isDirectory:%s. Nothing to do, returning."
+ "[OTA] %s: The URL %@ for new asset already exist, isDirectory:%s. Remvoing it."
+ "[OTA] %s: Unsupported platform"
+ "[OTA] %s: _periodicCheckEnabled from defaults: %@"
+ "[OTA] %s: _periodicityInSecs from defaults: %lld"
+ "[OTA] %s: assetSpecifier:%@ is nil or malformed"
+ "[OTA] %s: assetVersion:%@ is nil or malformed"
+ "[OTA] %s: deviceName is %@"
+ "[OTA] %s: deviceSKUdata = %@ "
+ "[OTA] %s: deviceSKUdata = nil"
+ "[OTA] %s: deviceSKUdata = nil or lesser bytes, %@ "
+ "[OTA] %s: incorrect length %lu"
+ "[OTA] %s: localAsset.attributes is nil"
+ "[OTA] %s: newAssetUUIDString is nil"
+ "[OTA] %s: previousLatestUUIDString is nil"
+ "[OTA] %s: restoreVersionCompatibilities is %@"
+ "[OTA] %s: sanityCheckOSRestoreVersion failed."
+ "[OTA] %s: sanityCheckSKUVersion failed."
+ "[OTA] %s: supportedBuildRange is %@"
+ "[OTA] OTA update of PT is disabled"
+ "[corewifi-PH] %{public}s (%{public}s:%u)  %s"
+ "[corewifi-PH] %{public}s (%{public}s:%u) %s"
+ "[corewifi-PH] %{public}s (%{public}s:%u) %s - [%@]"
+ "[corewifi-PH] %{public}s (%{public}s:%u) %s ENTRY"
+ "[corewifi-PH] %{public}s (%{public}s:%u) %s Invalid macAddress. Returning."
+ "[corewifi-PH] %{public}s (%{public}s:%u) %s Rapport is already active....returning!"
+ "[corewifi-PH] %{public}s (%{public}s:%u) %s macAddress: %@ thisDeviceMACAddress: %@"
+ "[corewifi-PH] %{public}s (%{public}s:%u) %s macAddress: [%@] activeHotspotClients = %@"
+ "[corewifi-PH] %{public}s (%{public}s:%u) (Request %@) Companion link is invalid; error '%@'"
+ "[corewifi-PH] %{public}s (%{public}s:%u) (Request %@) Preparing to send rapport message to '%@'"
+ "[corewifi-PH] %{public}s (%{public}s:%u) (Request %@) rapport message send failed with error: %@"
+ "[corewifi-PH] %{public}s (%{public}s:%u) (Request %@) rapport message sent; response: %@ / options: %@"
+ "[corewifi-PH] %{public}s (%{public}s:%u) Device found from Rapport..%@ ipAddress %@ model %@"
+ "[corewifi-PH] %{public}s (%{public}s:%u) Device lost from Rapport..%@"
+ "[corewifi-PH] %{public}s (%{public}s:%u) ERROR Activating RPCompanionLinkClient %@"
+ "[corewifi-PH] %{public}s (%{public}s:%u) Fetched WiFi Info - %@  with error '%@'"
+ "[corewifi-PH] %{public}s (%{public}s:%u) Gave up rety fetch for device with ID = %@"
+ "[corewifi-PH] %{public}s (%{public}s:%u) INVALIDATING RAPPORT BYE! BYE!"
+ "[corewifi-PH] %{public}s (%{public}s:%u) Invalidating rapportTeardownTimer"
+ "[corewifi-PH] %{public}s (%{public}s:%u) Invalidating wifiInfoRetryRequestTimer"
+ "[corewifi-PH] %{public}s (%{public}s:%u) Now Activating RPCompanionLinkClient..."
+ "[corewifi-PH] %{public}s (%{public}s:%u) RPCompanionLinkClient activation exceeded  (%lu) activation attempts. Seems like a bug in Rapport. Please file a bug."
+ "[corewifi-PH] %{public}s (%{public}s:%u) RPCompanionLinkClient was interrupted."
+ "[corewifi-PH] %{public}s (%{public}s:%u) RPCompanionLinkClient was invalidated."
+ "[corewifi-PH] %{public}s (%{public}s:%u) Rapport activated  successfully ON [%@]"
+ "[corewifi-PH] %{public}s (%{public}s:%u) Received Extract WiFi request %@"
+ "[corewifi] %s: assetVersion: %@ valid: %@"
+ "[corewifi] %s:CWFNDDManager[%d]: Invalid filter %@\n"
+ "[corewifi] %s:CWFNDDManager[%d]: Invalid macId list %{public}@\n"
+ "[corewifi] @[%llu.%06llu] %{public}s (%{public}s:%u) Started mobileAssetManager [%p]"
+ "[corewifi] @[%llu.%06llu] %{public}s (%{public}s:%u) [iflist] CWFIO80211: (%{public}@) (%{public}@)"
+ "[corewifi] @[%llu.%06llu] %{public}s (%{public}s:%u) [iflist] CWFIO80211: (%{public}@) (%{public}@), a11[%p]"
+ "[corewifi] @[%llu.%06llu] %{public}s (%{public}s:%u) [iflist] CWFKernelEventMonitor: (%{public}@) eventCode[0x%08lx/%lu]/(%{public}@)"
+ "[corewifi] @[%llu.%06llu] %{public}s (%{public}s:%u) [iflist] CWFKernelEventMonitor: (%{public}@) eventCode[0x%08lx/%lu]/(%{public}@), update[%u] a11[%p]"
+ "[corewifi] @[%llu.%06llu] %{public}s (%{public}s:%u) mobileAssetManager could not be initialized"
+ "[corewifi] @[%llu.%06llu] Non WiFi interface name specified (name=%{public}@, role=%{public}@, uuid=%{public}@)"
+ "[corewifi] @[%llu.%06llu] Using %{public}@ based on interface role '%{public}@'"
+ "[corewifi] @[%llu.%06llu] Using default interface role '%{public}@' based on '%{public}@' request type"
+ "[corewifi] @[%llu.%06llu] [iflist] %@ is a valid network interface, but was not a valid 80211 interface (non80211=%@)"
+ "[corewifi] @[%llu.%06llu] [iflist] %s CWFApple80211 (%@)"
+ "[corewifi] @[%llu.%06llu] [iflist] %s CWFEAP8021X (%{public}@)"
+ "[corewifi] @[%llu.%06llu] [iflist] %s CWFSCNetworkInterface (%{public}@)"
+ "[corewifi] @[%llu.%06llu] [iflist] %s CWFSCNetworkService (%@)"
+ "[corewifi] @[%llu.%06llu] [iflist] %{public}@: apple80211 [%llu.%06llu] %d"
+ "[corewifi] @[%llu.%06llu] [iflist] %{public}@: scnetsvc [%llu.%06llu] %d, scnetif [%llu.%06llu] %d, eap8021x [%llu.%06llu] %d"
+ "[corewifi] @[%llu.%06llu] [iflist] (SCNetConfig) Updating SystemConfiguration interfaces took [%llu.%06llu], waited [%llu.%06llu], reason=%{public}@, apple80211IntfNames: (%{public}@)"
+ "[corewifi] @[%llu.%06llu] [iflist] CWFSCNetworkConfiguration/kSCDynamicStoreDomainSetup: (%{public}@)"
+ "[corewifi] @[%llu.%06llu] [iflist] CWFSCNetworkConfiguration/kSCEntNetInterface: (%{public}@)"
+ "[corewifi] @[%llu.%06llu] [iflist] Did NOT find matching WiFi interface after interface list refresh (name=%{public}@, role=%{public}@, uuid=%{public}@)"
+ "[corewifi] @[%llu.%06llu] [iflist] Found matching WiFi interface after interface list refresh (name=%{public}@, role=%{public}@, uuid=%{public}@)"
+ "[corewifi] @[%llu.%06llu] [iflist] No WiFi matching interface exists, refreshing interface list (name=%{public}@, role=%{public}@, uuid=%{public}@)"
+ "[corewifi] @[%llu.%06llu] [iflist] Updating Apple80211 interfaces took [%llu.%06llu], waited [%llu.%06llu], reason: (%{public}@), scnet: [%llu.%06llu] (%{public}@), ifnames: [%llu.%06llu] (%{public}@), vifnames: [%llu.%06llu] (%{public}@), apple80211Map: (%{public}@), eligibleForRemoval: (%{public}@)"
+ "[corewifi] @[%llu.%06llu] [iflist] WiFi interface not eligible for removal (%{public}@)"
+ "[corewifi] @[%llu.%06llu] [iflist] WiFi network interface added (%{public}@), posted notification"
+ "[corewifi] @[%llu.%06llu] [iflist] WiFi network interface removed (%{public}@), posted notification"
+ "[corewifi] AUTO-JOIN: Adding adjacent 5GHz channel (%{public}@) for CarPlay network"
+ "[corewifi] AUTO-JOIN: Allowing more-preferred known networks while display is OFF"
+ "[corewifi] AUTO-JOIN: Caching CarPlay preferred channel (%{public}@)"
+ "[corewifi] AUTO-JOIN: Current network is deferrable, allowing non-deferred known networks while display is OFF"
+ "[corewifi] AUTO-JOIN: Delayed auto-join success metric submission (interval=%ds) (%{public}@)"
+ "[corewifi] AUTO-JOIN: Number of preferred channels for CarPlay %lu"
+ "[corewifi] AUTO-JOIN: Preferred channel for CarPlay %lu"
+ "[corewifi] AUTO-JOIN: Sent '%{public}@' CoreAnalytics metric"
+ "[corewifi] AUTO-JOIN: Updated join status (%{public}@)"
+ "[corewifi] AUTO-JOIN: Will not submit '%{public}@' CoreAnalytics metric"
+ "[corewifi] Failed to initialize CWFConfigurationProfileManager"
+ "[corewifi] Found matching already-pending XPC request (name=%{public}@, uuid=%{public}@), creating dependency to force serialization"
+ "[corewifi] PRIVATE MAC: Forgetting IP configuration for updated networkID for network (%{public}@)"
+ "[corewifi] PRIVATE MAC: Forgetting captive configuration for updated networkID for public AirPlay network (%{public}@)"
+ "[corewifi] failed to archive network profile: %@"
+ "[corewifi] failed to unarchive network profile: %@"
+ "[request.filters count] > 0 && [request.filters count] <= MAX_NDD_FILTER"
+ "[self sanityCheckOSRestoreVersion:attributes]"
+ "[self sanityCheckSKUVersion:attributes]"
+ "_MaxOSRestoreVersion"
+ "_MinOSRestoreVersion"
+ "_OSRestoreVersionCompatibilities"
+ "__getAutoJoinMetric:"
+ "__getAutoJoinStatistics:"
+ "__getDeviceSupervised:"
+ "__getNetworkManagedByMDM:"
+ "__hotspotClientManager"
+ "__isEnabledKnownNetworkNearby"
+ "__periodicCheck"
+ "__resetAutoJoinStatistics:"
+ "__scheduleDelayedAutoJoinMetricSubmission"
+ "__submitAutoJoinMetric:"
+ "__unscheduleDelayedAutoJoinMetricSubmission"
+ "__updateApple80211InterfacesWithReason:reply:"
+ "__updateAutoJoinMetricAndStatistics:"
+ "__updateAutoJoinMetricWithJoinStatus"
+ "__updateCachedMDMManagedProfileUUIDs:"
+ "__updateSystemConfigurationInterfacesWithReason:reply:"
+ "__updateWiFiInterfacesWithReason:reply:"
+ "_activeDevices"
+ "_activeHotspotClients"
+ "_allowTestingOnUnSupportedChipset"
+ "_apple80211InterfaceQueue"
+ "_assetDidChangeHandler"
+ "_assetID"
+ "_assetPowerTable"
+ "_assetSpecifier"
+ "_assetType"
+ "_assetVersion"
+ "_autoHotspotEndedAt"
+ "_autoHotspotJoinStartedAt"
+ "_autoHotspotStartedAt"
+ "_autoJoinManager"
+ "_autoJoinedNetwork"
+ "_bestCandidateRSSI"
+ "_bssid"
+ "_candidateBSSCount"
+ "_candidateSSIDCount"
+ "_channelList"
+ "_configProfileManager"
+ "_currentLockedAutoAsset"
+ "_currentLockedAutoAssetSelector"
+ "_delayedAutoJoinMetricSubmissionTimer"
+ "_delayedSubmissionMetric"
+ "_delegates"
+ "_deviceDiscoveryManager"
+ "_deviceRapportEffectiveIdentifier"
+ "_didExclude6GHzOnlyNetwork"
+ "_didExcludeDisabledNetwork"
+ "_didExcludeDisallowedNetwork"
+ "_didExcludeLowRSSINetwork"
+ "_didExcludePartiallyMatchedNetwork"
+ "_didExcludeStandalone6GHzNetwork"
+ "_didJoinDeferredNetwork"
+ "_didJoinPreviouslyAssociatedNetwork"
+ "_didJoinPreviouslyLowRSSINetwork"
+ "_didUserJoinDeferredNetwork"
+ "_didUserJoinDisallowedNetwork"
+ "_didUserJoinKnownNetwork"
+ "_didUserJoinLowRSSINetwork"
+ "_didUserJoinPartiallyMatchedNetwork"
+ "_displayOff"
+ "_fetchAndUpdateActiveDevicesInfo"
+ "_fetchWiFiInfoForDevice:rapportDevice:"
+ "_fetchWiFiInfoForRapportDevice:completion:"
+ "_filters"
+ "_firstSupportedBuild"
+ "_handleAssetChangedNotification"
+ "_hotspotClientManager"
+ "_hotspotQueue"
+ "_interestSet"
+ "_invalidateRapportTeardownTimer"
+ "_invalidateWiFiInfoRetryRequestTimer"
+ "_ipAddress"
+ "_isRapportTeardownTimerValid"
+ "_isSupportedModel:"
+ "_isWiFiInfoRequestTimerValid"
+ "_joinEndedAt"
+ "_joinStartedAt"
+ "_joinStatus"
+ "_joinStatus.scanResult"
+ "_lastSupportedBuild"
+ "_linkRecoveryDelay"
+ "_localURL"
+ "_lowRSSICandidates"
+ "_macAddress"
+ "_matchedCandidateAt"
+ "_matchedCandidates"
+ "_mdmManagedProfileUUIDs"
+ "_mobileAssetManager"
+ "_model"
+ "_notifyTokenVersionDownloaded"
+ "_numReports"
+ "_periodicCheckEnabled"
+ "_periodicCheckTimer"
+ "_periodicityInSecs"
+ "_prevAssocBeforeTimestamp"
+ "_prevAssociatedNetwork"
+ "_prevLowRSSICandidates"
+ "_primaryIPv4InterfaceAt"
+ "_primaryIPv6InterfaceAt"
+ "_productColor"
+ "_productMarketingName"
+ "_productType"
+ "_profileManager"
+ "_rapportClient"
+ "_rapportClientActivationFailCount"
+ "_rapportErrorRegex"
+ "_rapportQueue"
+ "_rapportTeardownTimer"
+ "_receiver"
+ "_receiverMacAddress"
+ "_registerExtractWiFiInfo"
+ "_registerForAssetChangedNotification:"
+ "_removesDependenciesAfterFinish"
+ "_resetRapportClientWithInvalidation:"
+ "_retryCount"
+ "_retryDevices"
+ "_routableIPv4AddressAt"
+ "_routableIPv6AddressAt"
+ "_sendRapportMessageToDevice:requestID:request:options:completion:"
+ "_sendRapportMessageToDevice:withRequestID:request:options:completion:"
+ "_setupRapportClientWithReason:"
+ "_setupReason"
+ "_stringByReplacingOccurencesWithRegex:replacement:"
+ "_systemConfigInterfaceQueue"
+ "_thisDeviceMACAddress"
+ "_transmitter"
+ "_transmitterMacAddress"
+ "_triggeredByAutoJoinEnabledAt"
+ "_triggeredByDeviceWakeAt"
+ "_triggeredByFirstUnlockAt"
+ "_triggeredByLinkDownAt"
+ "_triggeredByMotionEndedAt"
+ "_triggeredByWiFiOnAt"
+ "_updatedNetworkIDHandler"
+ "_userJoinedNetwork"
+ "_userJoinedNetworkAt"
+ "_waitingToSendResponseBeforeFinish"
+ "_wasAlreadyAssociatedToNetwork"
+ "_wasDiscoveredVia6GHzFollowup"
+ "_wasLockdownModeEnabled"
+ "_wifiInfo"
+ "_wifiInfoRetryRequestTimer"
+ "activateWithCompletion:"
+ "activeDevices"
+ "activeHotspotClients"
+ "addedBy3PAppCount"
+ "addedByATJCount"
+ "addedByAccessoryAppCount"
+ "addedByCarrierCount"
+ "addedByCloudSyncCount"
+ "addedByProfileCount"
+ "addedByRecommendationCount"
+ "addedBySSIDGuessingCount"
+ "addedBySetupAssistantCount"
+ "addedBySystemAppCount"
+ "addedByTapToSetupCount"
+ "addedByUnknownReason"
+ "addedByWalletCount"
+ "addedByWiFiMenuCount"
+ "addedByWiFiPasswordSharingCount"
+ "addedByWiFiSettingsCount"
+ "allProfiles:"
+ "allowTestingOnUnSupportedChipset"
+ "assetDidChangeHandler"
+ "assetID"
+ "assetIDFromLocalURL:"
+ "assetPowerTable"
+ "assetSelector"
+ "assetSpecifier"
+ "assetSpecifierToTrack"
+ "assetType"
+ "assetVersion"
+ "attributes"
+ "autoHotspotEndedAt"
+ "autoHotspotJoinStartedAt"
+ "autoHotspotStartedAt"
+ "autoJoinManager"
+ "autoJoinedNetwork"
+ "availableForUseAttributes"
+ "bestCandidateRSSI"
+ "boolForKey:"
+ "c32@0:8@16@24"
+ "cachedNetworkID"
+ "captiveCount"
+ "carplayCount"
+ "carrierPayloadIdentifier=%@, "
+ "channelList"
+ "channelList=%@"
+ "channel_list"
+ "checkForNewerSync:withUsagePolicy:withTimeout:discoveredAttributes:error:"
+ "clientAssociated:thisDeviceMACAddress:"
+ "clientAssociatedToHostPersonalHotspot:"
+ "clientDisassociated:"
+ "com.apple.8ta_za.4a790876-d474-11eb-9b3f-f45c89abb0d9"
+ "com.apple.ATN_gy.5494bc1a-d474-11eb-8acc-f45c89abb0d9"
+ "com.apple.ATT_FirstNet_US.4ebed118-d474-11eb-9328-f45c89abb0d9"
+ "com.apple.ATT_FirstNet_US.4ebed2b2-d474-11eb-9328-f45c89abb0d9"
+ "com.apple.ATT_NR_US.55d0b606-d474-11eb-a328-f45c89abb0d9"
+ "com.apple.ATT_NR_US.55d0b782-d474-11eb-a328-f45c89abb0d9"
+ "com.apple.ATT_US.4d0e3cb4-d474-11eb-b099-f45c89abb0d9"
+ "com.apple.ATT_US.4d0e3e1c-d474-11eb-b099-f45c89abb0d9"
+ "com.apple.ATT_aio_NR_US.4fa4fd6e-d474-11eb-85e4-f45c89abb0d9"
+ "com.apple.ATT_aio_US.5221c68a-d474-11eb-8423-f45c89abb0d9"
+ "com.apple.AWCC_af.50b58a52-d474-11eb-a366-f45c89abb0d9"
+ "com.apple.Altice_LTE_US.4b5d0e5e-d474-11eb-baa6-f45c89abb0d9"
+ "com.apple.BT_Business_uk.4a2d3bf8-d474-11eb-9be0-f45c89abb0d9"
+ "com.apple.BT_Consumer_uk.86F751ED-ED35-4B07-A062-F5C29005E158"
+ "com.apple.BT_OnePhone_uk.51cfa9cc-d474-11eb-ae77-f45c89abb0d9"
+ "com.apple.Batelco_bh.49dd3928-d474-11eb-96db-f45c89abb0d9"
+ "com.apple.Bell_Lucky_ca.5732034c-d474-11eb-8c3d-f45c89abb0d9"
+ "com.apple.Bell_Lucky_ca.573204be-d474-11eb-8c3d-f45c89abb0d9"
+ "com.apple.Bell_ca.56bf4ec4-d474-11eb-b7e0-f45c89abb0d9"
+ "com.apple.Bell_ca.56bf5036-d474-11eb-b7e0-f45c89abb0d9"
+ "com.apple.ChinaTelecom_hk.5532f0e2-d474-11eb-a447-f45c89abb0d9"
+ "com.apple.ChinaTelecom_hk.5532f240-d474-11eb-a447-f45c89abb0d9"
+ "com.apple.Chunghwa_tw.5249f178-d474-11eb-a269-f45c89abb0d9"
+ "com.apple.Cyta_cy.56973dd0-d474-11eb-92bf-f45c89abb0d9"
+ "com.apple.Docomo_gu.4ee4cb20-d474-11eb-a966-f45c89abb0d9"
+ "com.apple.Docomo_jp.56466202-d474-11eb-838e-f45c89abb0d9"
+ "com.apple.Free_fr.517c8666-d474-11eb-ad1d-f45c89abb0d9"
+ "com.apple.FreedomMobile_ca.4d3618ce-d474-11eb-b30b-f45c89abb0d9"
+ "com.apple.FreedomMobile_ca.4d361a2c-d474-11eb-b30b-f45c89abb0d9"
+ "com.apple.Hutchison_hk.4f81c632-d474-11eb-a3f8-f45c89abb0d9"
+ "com.apple.KDDI_LTE_only_jp.51a77b5a-d474-11eb-a5b5-f45c89abb0d9"
+ "com.apple.KTF_kr.50dd6c48-d474-11eb-b746-f45c89abb0d9"
+ "com.apple.KTF_kr.50dd6e6e-d474-11eb-b746-f45c89abb0d9"
+ "com.apple.KTF_kr.50dd6f22-d474-11eb-b746-f45c89abb0d9"
+ "com.apple.KTF_kr.50dd6fae-d474-11eb-b746-f45c89abb0d9"
+ "com.apple.LGU_kr.5386f040-d474-11eb-b687-f45c89abb0d9"
+ "com.apple.LGU_kr.5386f123-d474-11eb-b687-f45c89abb0d9"
+ "com.apple.LGU_kr.5386f216-d474-11eb-b687-f45c89abb0d9"
+ "com.apple.LGU_kr.5386f27a-d474-11eb-b687-f45c89abb0d9"
+ "com.apple.LGU_kr.5386f2c0-d474-11eb-b687-f45c89abb0d9"
+ "com.apple.MTS_ca.4fee1d00-d474-11eb-be58-f45c89abb0d9"
+ "com.apple.Mirs_il.55f7a8c4-d474-11eb-88fe-f45c89abb0d9"
+ "com.apple.MobileAsset.CoreWiFi"
+ "com.apple.MobileOne_sg.4c197f12-d474-11eb-9b40-f45c89abb0d9"
+ "com.apple.O2_Prepaid_UK.4ce4a232-d474-11eb-9ee5-f45c89abb0d9"
+ "com.apple.O2_Prepaid_UK.4ce4a34a-d474-11eb-9ee5-f45c89abb0d9"
+ "com.apple.O2_Prepaid_UK.4ce4a3a4-d474-11eb-9ee5-f45c89abb0d9"
+ "com.apple.O2_UK.4bf32f9c-d474-11eb-9795-f45c89abb0d9"
+ "com.apple.O2_UK.4bf33104-d474-11eb-9795-f45c89abb0d9"
+ "com.apple.O2_UK.4bf33168-d474-11eb-9795-f45c89abb0d9"
+ "com.apple.Omnitel_lt.4ac49048-d474-11eb-92dd-f45c89abb0d9"
+ "com.apple.Orange_md.4a02ca4e-d474-11eb-a41a-f45c89abb0d9"
+ "com.apple.Orange_md.4a02cbb6-d474-11eb-a41a-f45c89abb0d9"
+ "com.apple.Orange_pl.5271f75e-d474-11eb-8c6b-f45c89abb0d9"
+ "com.apple.Orange_ro.4d5d7cde-d474-11eb-97cc-f45c89abb0d9"
+ "com.apple.Orange_ro.4d5d7e5a-d474-11eb-97cc-f45c89abb0d9"
+ "com.apple.Orange_uk.55abf604-d474-11eb-9d62-f45c89abb0d9"
+ "com.apple.RelianceJio_in.53ae41b8-d474-11eb-805d-f45c89abb0d9"
+ "com.apple.SFR_re.4d83283a-d474-11eb-8537-f45c89abb0d9"
+ "com.apple.STC_sa.4daac34a-d474-11eb-acb1-f45c89abb0d9"
+ "com.apple.STC_sa.4daac4d0-d474-11eb-acb1-f45c89abb0d9"
+ "com.apple.Sasktel_ca.52e7bf16-d474-11eb-9183-f45c89abb0d9"
+ "com.apple.Shaw_ca.4c690c44-d474-11eb-83e0-f45c89abb0d9"
+ "com.apple.Shaw_ca.4c690dac-d474-11eb-83e0-f45c89abb0d9"
+ "com.apple.SingTel_sg.52c0b0d8-d474-11eb-abcd-f45c89abb0d9"
+ "com.apple.Softbank_YMobile_jp.4dd55aba-d474-11eb-92a5-f45c89abb0d9"
+ "com.apple.Softbank_jp.535f93b0-d474-11eb-af6d-f45c89abb0d9"
+ "com.apple.Softbank_jp.535f95d6-d474-11eb-af6d-f45c89abb0d9"
+ "com.apple.Sprint_Boost_ISIM_LTE_US.4a9e4c76-d474-11eb-ad83-f45c89abb0d9"
+ "com.apple.Sprint_ISIM_LTE_US.4f0b0d3a-d474-11eb-a9ce-f45c89abb0d9"
+ "com.apple.Sprint_Virgin_ISIM_LTE_US.4e2113ec-d474-11eb-8744-f45c89abb0d9"
+ "com.apple.Swisscom_Wingo_ch.4e45c2a0-d474-11eb-8c7c-f45c89abb0d9"
+ "com.apple.Swisscom_Wingo_ch.4e45c412-d474-11eb-8c7c-f45c89abb0d9"
+ "com.apple.Swisscom_Wingo_ch.4e45c46c-d474-11eb-8c7c-f45c89abb0d9"
+ "com.apple.Swisscom_ch.51f8604c-d474-11eb-8107-f45c89abb0d9"
+ "com.apple.TIM_br.4c405a6a-d474-11eb-92d1-f45c89abb0d9"
+ "com.apple.TMobile_Germany.544c09f2-d474-11eb-acbd-f45c89abb0d9"
+ "com.apple.TMobile_US.4c93231c-d474-11eb-8bf8-f45c89abb0d9"
+ "com.apple.TMobile_uk.555b517c-d474-11eb-abb2-f45c89abb0d9"
+ "com.apple.Telenor_no.4f5a1114-d474-11eb-b7bb-f45c89abb0d9"
+ "com.apple.TrueH_th.4aeb7514-d474-11eb-9c38-f45c89abb0d9"
+ "com.apple.TrueH_th.4aeb767c-d474-11eb-9c38-f45c89abb0d9"
+ "com.apple.Turkcell_tr.512fd942-d474-11eb-8b3f-f45c89abb0d9"
+ "com.apple.Unitel_ao.57551fee-d474-11eb-a109-f45c89abb0d9"
+ "com.apple.Unitel_mn.9A3F6052-532C-4EE5-8951-51A2CBC74CAF"
+ "com.apple.Verizon_LTE_US.4cc0d1d6-d474-11eb-8f79-f45c89abb0d9"
+ "com.apple.Verizon_LTE_US.4cc0d35c-d474-11eb-8f79-f45c89abb0d9"
+ "com.apple.Verizon_LTE_US.4cc0d3d4-d474-11eb-8f79-f45c89abb0d9"
+ "com.apple.Verizon_Response_LTE_US.50420762-d474-11eb-8a26-f45c89abb0d9"
+ "com.apple.Verizon_Response_LTE_US.5042091a-d474-11eb-8a26-f45c89abb0d9"
+ "com.apple.Verizon_Response_LTE_US.50420a0a-d474-11eb-8a26-f45c89abb0d9"
+ "com.apple.VinaPhone_vn.4a550c78-d474-11eb-9fba-f45c89abb0d9"
+ "com.apple.Viva_kw.5107c63c-d474-11eb-90f0-f45c89abb0d9"
+ "com.apple.Vodafone_uk.4dfc7cf8-d474-11eb-9513-f45c89abb0d9"
+ "com.apple.Vodafone_uk.4dfc7e6a-d474-11eb-9513-f45c89abb0d9"
+ "com.apple.Zain_kw.561f3b82-d474-11eb-95d1-f45c89abb0d9"
+ "com.apple.Zain_sa.5583b2fc-d474-11eb-855e-f45c89abb0d9"
+ "com.apple.Zain_sa.5583b464-d474-11eb-855e-f45c89abb0d9"
+ "com.apple.corewifi.HotspotClientManagerQueue"
+ "com.apple.corewifi.MACAddressKey"
+ "com.apple.corewifi.RapportRequest"
+ "com.apple.corewifi.RequestWiFiInfo"
+ "com.apple.corewifi.apple80211-common-intf"
+ "com.apple.corewifi.deviceDiscovered"
+ "com.apple.corewifi.hotspotsessionstarted"
+ "com.apple.corewifi.hotspotsessionstopped"
+ "com.apple.corewifi.rapportQueue"
+ "com.apple.corewifi.sc-common-intf"
+ "com.apple.dtac_th.54238f90-d474-11eb-a237-f45c89abb0d9"
+ "com.apple.dtac_th.542390f8-d474-11eb-a237-f45c89abb0d9"
+ "com.apple.du_Virgin_ae.4b103660-d474-11eb-82ec-f45c89abb0d9"
+ "com.apple.du_ae.4bcc49ae-d474-11eb-8e4a-f45c89abb0d9"
+ "com.apple.mobily_sa.4fcac896-d474-11eb-93df-f45c89abb0d9"
+ "com.apple.mobily_sa.4fcac9fe-d474-11eb-93df-f45c89abb0d9"
+ "com.apple.mobily_sa.4fcaca62-d474-11eb-93df-f45c89abb0d9"
+ "com.apple.wifi.managed.06F791B3-7626-4E6C-A866-3C473D181CC2"
+ "com.apple.wifi.managed.18E94328-39E2-449A-88AE-A04DDCA6C5AE"
+ "com.apple.wifi.managed.2DDBD508-0908-457A-87BC-8094CD3FA84A"
+ "com.apple.wifi.managed.4088E899-6CA9-498F-A459-601459B141F2"
+ "com.apple.wifi.managed.472749CE-5715-4E07-BF06-FA74572C9413"
+ "com.apple.wifi.managed.47BE32E4-3EEC-4ADB-987C-0F143B17F15C"
+ "com.apple.wifi.managed.5018D899-6CA9-498F-A459-601459B15203"
+ "com.apple.wifi.managed.53D6D4B7-744E-44A7-A933-C76C575665CE"
+ "com.apple.wifi.managed.5B16F881-8215-4DE3-BD6E-4FFC2419462D"
+ "com.apple.wifi.managed.5FAA0883-2F04-478E-BD3E-37EF4D38E03A"
+ "com.apple.wifi.managed.6AB6C0AF-4834-4D02-8298-E09BAB8C7260"
+ "com.apple.wifi.managed.8913CDAF-6F0F-4BBC-BF35-976ADFE4E17F"
+ "com.apple.wifi.managed.8936B13F-A1D7-4C04-AB66-9118F174B2C9"
+ "com.apple.wifi.managed.AA245DDE-4BF5-4493-B3BA-66AB9E10CDBC"
+ "com.apple.wifi.managed.AB944BC5-41E6-44AC-880B-C50FD3EC6F13"
+ "com.apple.wifi.managed.B9891EEF-029D-4369-9F4D-F55BF2D1DBB5"
+ "com.apple.wifi.managed.BB245DDE-4BF5-4493-B3BA-66AB9E10CDBC"
+ "com.apple.wifi.managed.CA465CCD-4BF5-4493-B3BC-66AB9E10CDBC"
+ "com.apple.wifi.managed.E395AF22-DC47-480B-A79C-51039C351000"
+ "com.apple.wifi.managed.E9245CCD-4BF5-4493-B3BC-66AB9E10CDBC"
+ "com.apple.wifi.managed.E9245DDE-4BF5-4493-B3BC-66AB9E10CDBD"
+ "com.apple.wifi.managed.E9245DDE-4BF5-4493-B3BC-66AB9E10CDBE"
+ "com.apple.wifi.managed.E9245DDE-4BF5-4493-B3BC-66AB9E10CDBF"
+ "com.apple.wifi.managed.E9245DDE-4BF5-4493-B3BC-66AB9E10CDCA"
+ "com.apple.wifi.managed.EA345CCD-4BF5-4493-B3BC-66AB9E10CDBC"
+ "compareAssetVersion:withVersion:"
+ "compareOSRestoreVersion:withVersion:"
+ "compareSUCoreRestoreVersion:withVersion:"
+ "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
+ "copyItemAtURL:toURL:error:"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
+ "createTopLevelDir"
+ "currentLatestAssetVersion"
+ "currentLockedAutoAsset"
+ "currentLockedAutoAssetSelector"
+ "currentStatusSync:"
+ "dataWithLength:"
+ "defaultManager"
+ "defaultPrivateMACMode"
+ "delegates"
+ "deregisterRequestID:"
+ "deviceColor"
+ "deviceDiscoveryManager"
+ "deviceMACAddress"
+ "deviceMarketingName"
+ "deviceModel"
+ "deviceProductColor"
+ "deviceProductType"
+ "deviceRapportEffectiveIdentifier"
+ "deviceSKUdata && deviceSKUdata.length == kExtractedWSKULength"
+ "didDiscoverDevice:"
+ "didExclude6GHzOnlyNetwork"
+ "didExcludeDisabledNetwork"
+ "didExcludeDisallowedNetwork"
+ "didExcludeLowRSSINetwork"
+ "didExcludePartiallyMatchedNetwork"
+ "didExcludeStandalone6GHzNetwork"
+ "didFetchWifiInfoForDevice:"
+ "didJoinDeferredNetwork"
+ "didJoinDeferredNetworks"
+ "didJoinPreviousAssocNetwork"
+ "didJoinPreviouslyAssociatedNetwork"
+ "didJoinPreviouslyLowRSSINetwork"
+ "didLoseDevice:"
+ "didUserJoin6GHzOnlyNetwork"
+ "didUserJoinDeferredNetwork"
+ "didUserJoinDisabledNetwork"
+ "didUserJoinDisallowedNetwork"
+ "didUserJoinKnownNetwork"
+ "didUserJoinLessPreferredNetwork"
+ "didUserJoinLowRSSINetwork"
+ "didUserJoinPartiallyMatchedNetwork"
+ "didUserJoinStandalone6GHzNetwork"
+ "disableCount"
+ "disabled6EModeCount"
+ "displayOff"
+ "durationFromAutoJoinEnabledTrigger"
+ "durationFromMotionEndedTrigger"
+ "earlierDate:"
+ "effectiveIdentifier"
+ "effectivePrivateMACModeWithSystemSetting:"
+ "empty"
+ "empty string"
+ "enablePeriodicCheck"
+ "endAllPreviousLocksForSpecifier:"
+ "endAllPreviousLocksOfSelectorSync:forClientName:"
+ "endLockUsageSync:"
+ "eventQueue"
+ "fetchActiveDevices"
+ "fetchWiFiInfoForDevice:"
+ "fileExistsAtPath:isDirectory:"
+ "fileURLWithPath:isDirectory:"
+ "fileURLWithPathComponents:"
+ "filters"
+ "filters="
+ "firstMatchInString:options:range:"
+ "firstSupportedBuild"
+ "force"
+ "gD8SNRcHQeIxCAvsp+2vjA"
+ "garbageCollectWithNewAsset:prevAsset:"
+ "getDeviceSKU"
+ "has6GHzBSSCount"
+ "hasFetchedDeviceInfo"
+ "hashedChipsetName"
+ "hiddenCount"
+ "hotspotDisabled"
+ "hotspotQueue"
+ "iPad"
+ "iPhone"
+ "idsDeviceIdentifier"
+ "initForAssetType:withAssetSpecifier:"
+ "initForClientName:selectingAsset:error:"
+ "initWithAssetType:assetSpecifier:assetVersion:attributes:localURL:"
+ "initWithContentsOfURL:"
+ "initWithDictionary:copyItems:"
+ "initWithPattern:options:error:"
+ "initWithRapportDevice:"
+ "initWithRestoreVersion:"
+ "initWithUserInfo:"
+ "integerForKey:"
+ "interestInContentSync:withInterestPolicy:"
+ "interestSet"
+ "io80211"
+ "ipAddress"
+ "isAddReasonCarrierBundle"
+ "isComparable:"
+ "isDeviceSupervised"
+ "isEqualToNDDFilter:"
+ "isEqualToNDDReport:"
+ "isNetworkManagedByMDM:"
+ "isPayloadIdentifierTelemetryApproved"
+ "isSupportedChipset"
+ "isSupportedDeviceClass"
+ "isSupportedOTAPTUpdate"
+ "isValidAssetVersion:"
+ "isValidOSVersion:"
+ "joinEndedAt"
+ "joinLatency"
+ "joinStartedAt"
+ "joinStatus"
+ "joinedInPast2MonthsCount"
+ "joinedInPast2WeeksCount"
+ "joinedInPast2YearsCount"
+ "joinedInPast6MonthsCount"
+ "joinedInPastMonthCount"
+ "joinedInPastWeekCount"
+ "joinedInPastYearCount"
+ "kSCDynamicStoreDomainSetup"
+ "kSCEntNetInterface"
+ "kevent"
+ "lastSupportedBuild"
+ "latestAssetSubDir"
+ "linkRecoveryDelay"
+ "localDevice"
+ "localURL"
+ "lockAndHandOffCanBlock:"
+ "lockAutoAssetWithReason:isBlocking:"
+ "lockContentSync:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:"
+ "macAddress"
+ "makeAutoAssetWithSelector:"
+ "marketing-name"
+ "matchedCandidateAt"
+ "matchedCandidateLatency"
+ "mobile"
+ "movingAttrCount"
+ "mutableBytes"
+ "n3eKwIu1bJzNdojd5qn1YOmiy0ZjQGtS4p6sxTqucbk="
+ "netID=%@, "
+ "networkCarrierPayloadIdentifier"
+ "networkCarrierPayloadIdentifierIsAllowed"
+ "networkIsMoving"
+ "networkIsPublic"
+ "networkIsStandalone6GHz"
+ "nil"
+ "notifyRegistrationName:forAssetType:forAssetSpecifier:"
+ "notifyTokenVersionDownloaded"
+ "numReports"
+ "numReports=%ld, "
+ "numberOfCallsToCopyAsset"
+ "numberOfSuccessfullAssetCopy"
+ "numberOfTimesAssetExisted"
+ "objectsPassingTest:"
+ "openCount"
+ "oweCount"
+ "oweTransitionCount"
+ "passpointCount"
+ "path"
+ "pathComponents"
+ "payloadIdentifier"
+ "payloadIdentifier=%@, "
+ "periodicCheckEnabled"
+ "periodicCheckTimer"
+ "periodicityInSecs"
+ "personalHotspotCount"
+ "primaryIPv4InterfaceAt"
+ "primaryIPv4InterfaceDuration"
+ "primaryIPv4InterfaceLatency"
+ "primaryIPv6InterfaceAt"
+ "primaryIPv6InterfaceDuration"
+ "primaryIPv6InterfaceLatency"
+ "primaryInterfaceDuration"
+ "primaryInterfaceLatency"
+ "privacyProxyDisabledCount"
+ "privateMACOffByDefaultCount"
+ "privateMACOffByProfileCount"
+ "privateMACOffByUserCount"
+ "privateMACRotatingByDefaultCount"
+ "privateMACRotatingByUserCount"
+ "privateMACStaticByDefaultCount"
+ "privateMACStaticByUserCount"
+ "processLocalAsset:"
+ "productColor"
+ "productMarketingName"
+ "productType"
+ "profileUUID"
+ "publicAirPlayCount"
+ "publicAttrCount"
+ "queriedSKUdata"
+ "queriedSKUdata.length == kWSKULength"
+ "queryDeviceSupervisedWithRequestParams:reply:"
+ "queryNetworkManagedByMDM:requestParams:reply:"
+ "range"
+ "rapportClient"
+ "rapportClientActivationFailCount"
+ "rapportErrorRegex"
+ "rapportQueue"
+ "rapportTeardownTimer"
+ "reason-expedite-discovery-for-testing"
+ "reason-need-to-check-version"
+ "reason-started-monitoring"
+ "receiver"
+ "receiver=%@, "
+ "receiverMacAddress"
+ "receiverMacAddress=%@, "
+ "registerDelegate:"
+ "registerRequestID:options:handler:"
+ "removeItemAtURL:error:"
+ "request.filters[i].receiverMacAddress != nil || request.filters[i].transmitterMacAddress != nil || request.filters[i].bssid != nil || request.filters[i].frameType != 0"
+ "restoreVersion"
+ "retryCount"
+ "retryDevices"
+ "routableIPDuration"
+ "routableIPLatency"
+ "routableIPv4AddressAt"
+ "routableIPv4Duration"
+ "routableIPv4Latency"
+ "routableIPv6AddressAt"
+ "routableIPv6Duration"
+ "routableIPv6Latency"
+ "sanityCheckOSRestoreVersion:"
+ "sanityCheckSKUVersion:"
+ "scanLatency"
+ "sendRequestID:request:destinationID:options:responseHandler:"
+ "setActiveDevices:"
+ "setActiveHotspotClients:"
+ "setAllowTestingOnUnSupportedChipset:"
+ "setAssetDidChangeHandler:"
+ "setAssetPowerTable:"
+ "setAssetSpecifier:"
+ "setAttributes:ofItemAtPath:error:"
+ "setAutoHotspotEndedAt:"
+ "setAutoHotspotJoinStartedAt:"
+ "setAutoHotspotStartedAt:"
+ "setAutoJoinedNetwork:"
+ "setBestCandidateRSSI:"
+ "setBssid:"
+ "setCachedNetworkID:"
+ "setCandidateBSSCount:"
+ "setCandidateSSIDCount:"
+ "setChannelList:"
+ "setControlFlags:"
+ "setCurrentLockedAutoAsset:"
+ "setCurrentLockedAutoAssetSelector:"
+ "setDelegates:"
+ "setDestinationDevice:"
+ "setDeviceDiscoveryManager:"
+ "setDeviceFoundHandler:"
+ "setDeviceLostHandler:"
+ "setDeviceRapportEffectiveIdentifier:"
+ "setDidExclude6GHzOnlyNetwork:"
+ "setDidExcludeDisabledNetwork:"
+ "setDidExcludeDisallowedNetwork:"
+ "setDidExcludeLowRSSINetwork:"
+ "setDidExcludePartiallyMatchedNetwork:"
+ "setDidExcludeStandalone6GHzNetwork:"
+ "setDidJoinDeferredNetwork:"
+ "setDidJoinPreviouslyAssociatedNetwork:"
+ "setDidJoinPreviouslyLowRSSINetwork:"
+ "setDidUserJoinDeferredNetwork:"
+ "setDidUserJoinDisallowedNetwork:"
+ "setDidUserJoinKnownNetwork:"
+ "setDidUserJoinLowRSSINetwork:"
+ "setDidUserJoinPartiallyMatchedNetwork:"
+ "setDispatchQueue:"
+ "setDisplayOff:"
+ "setEventQueue:"
+ "setFilters:"
+ "setHotspotQueue:"
+ "setInterestSet:"
+ "setIpAddress:"
+ "setJoinEndedAt:"
+ "setJoinStartedAt:"
+ "setJoinStatus:"
+ "setLinkRecoveryDelay:"
+ "setMacAddress:"
+ "setMatchedCandidateAt:"
+ "setModel:"
+ "setNotifyTokenVersionDownloaded:"
+ "setNumReports:"
+ "setPayloadIdentifier:"
+ "setPayloadIdentifierTelemetryApproved:"
+ "setPeriodicCheckEnabled:"
+ "setPeriodicCheckTimer:"
+ "setPeriodicityInSecs:"
+ "setPrimaryIPv4InterfaceAt:"
+ "setPrimaryIPv6InterfaceAt:"
+ "setProductColor:"
+ "setProductMarketingName:"
+ "setProductType:"
+ "setRapportClient:"
+ "setRapportClientActivationFailCount:"
+ "setRapportErrorRegex:"
+ "setRapportQueue:"
+ "setRapportTeardownTimer:"
+ "setReceiver:"
+ "setReceiverMacAddress:"
+ "setRetryCount:"
+ "setRetryDevices:"
+ "setRoutableIPv4AddressAt:"
+ "setRoutableIPv6AddressAt:"
+ "setSetupReason:"
+ "setTargetUserSession:"
+ "setThisDeviceMACAddress:"
+ "setTransmitter:"
+ "setTransmitterMacAddress:"
+ "setTriggeredByAutoJoinEnabledAt:"
+ "setTriggeredByDeviceWakeAt:"
+ "setTriggeredByFirstUnlockAt:"
+ "setTriggeredByLinkDownAt:"
+ "setTriggeredByMotionEndedAt:"
+ "setTriggeredByWiFiOnAt:"
+ "setUpdatedNetworkIDHandler:"
+ "setUserInitiated:"
+ "setUserJoinedNetwork:"
+ "setUserJoinedNetworkAt:"
+ "setWaitingToSendResponseBeforeFinish:"
+ "setWasAlreadyAssociatedToNetwork:"
+ "setWasDiscoveredVia6GHzFollowup:"
+ "setWasLockdownModeEnabled:"
+ "setWifiInfoRetryRequestTimer:"
+ "setupReason"
+ "sharedDevice"
+ "sharedInstance"
+ "sharedProfileManager"
+ "shouldAllowTestingOnUnSupportedChipset"
+ "softlink:o:path:/System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset"
+ "softlink:o:path:/System/Library/PrivateFrameworks/Rapport.framework/Rapport"
+ "softlink:o:path:/System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport"
+ "standalone6GHzCount"
+ "startDiscoveringDevicesIfNeeded:withReason:"
+ "thisDeviceMACAddress"
+ "timeIntervalSinceNow"
+ "totalKnownNetworkCount"
+ "transferAssetFromSrc:toDst:withAsseID:withVersion:firstSupportedBuild:lastSupportedBuild:"
+ "transmitter"
+ "transmitter=%@, "
+ "transmitterMacAddress"
+ "transmitterMacAddress=%@, "
+ "triggeredByAutoJoinEnabledAt"
+ "triggeredByDeviceWakeAt"
+ "triggeredByFirstUnlockAt"
+ "triggeredByLinkDownAt"
+ "triggeredByMotionEndedAt"
+ "triggeredByWiFiOnAt"
+ "triggers"
+ "triggers=%@"
+ "unknownSecurityCount"
+ "unlockAssetWithReason:"
+ "unregisterDelegate:"
+ "updatedNetworkIDHandler"
+ "uppercaseString"
+ "userJoinDelay"
+ "userJoinPrefCount"
+ "userJoinedNetwork"
+ "userJoinedNetworkAt"
+ "v12@?0i8"
+ "v16@?0@\"CWFNetworkProfile\"8"
+ "v16@?0@\"RPCompanionLinkDevice\"8"
+ "v24@0:8@\"CWFDevice\"16"
+ "v24@?0@\"<CWFDeviceDiscoveryManagerDelegate>\"8^B16"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
+ "v24@?0@\"NSObject<CWFDeviceDiscoveryManagerDelegate>\"8^B16"
+ "v24@?0@8^B16"
+ "v32@?0@\"NSDictionary\"8@\"NSDictionary\"16@\"NSError\"24"
+ "v32@?0@\"NSDictionary\"8@\"NSDictionary\"16@?<v@?@\"NSDictionary\"@\"NSDictionary\"@\"NSError\">24"
+ "v32@?0@\"RPCompanionLinkDevice\"8Q16^B24"
+ "v32@?0@8@16^B24"
+ "waitingToSendResponseBeforeFinish"
+ "wapiCertCount"
+ "wapiPSKCount"
+ "wasAlreadyAssociatedToNetwork"
+ "wasDiscoveredVia6GHzFollowup"
+ "wasLockdownModeEnabled"
+ "wasRecently6GHzOnlyCount"
+ "wepCount"
+ "wifiInfoRetryRequestTimer"
+ "wpa2EnterpriseCount"
+ "wpa2EnterpriseMixedCount"
+ "wpa2PersonalCount"
+ "wpa2PersonalMixedCount"
+ "wpa3EnterpriseCount"
+ "wpa3EnterpriseSuiteBCount"
+ "wpa3SAECount"
+ "wpa3TransitionCount"
+ "wpaEnterpriseCount"
+ "wpaPersonalCount"
+ "writeToURL:error:"
- "![self __isAnyKnownNetworkNearby]"
- "!eachKnownNetwork.autoJoinDisabled"
- "-[CWFNearbyDeviceDiscoveryManager getRequestDataFromParams:]"
- "-[CWFXPCRequestProxy __didFindMatching80211InterfaceForXPCRequest:]"
- "-[CWFXPCRequestProxy __setupEventHandlers]"
- "-[CWFXPCRequestProxy __updateWiFiNetworkInterfaces:reply:]_block_invoke"
- "-[CWFXPCRequestProxy __updateWiFiNetworkInterfaces:reply:]_block_invoke_2"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFApple80211.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFAutoJoinManager.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFBSS.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFHomeManager/CWFHomeManager.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFHomeManager/CWFSensingAutoDataCollector.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFHomeManager/CWFSensingHMADataCollector.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFIO80211.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFKernelEventMonitor.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFNearbyDeviceDiscoveryManager.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFNetworkProfile.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFPrivateMACManager.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFSCNetworkConfiguration.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFSCNetworkInterface.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFUtilInternal.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFUtilPrivate.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFXPCConnection.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFXPCManager.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreWiFi/Framework/CWFXPCProxy.m"
- "6g-mode=[off (%@)], "
- "CWFSCNetworkConfiguration/kSCDynamicStoreDomainSetup"
- "CWFSCNetworkConfiguration/kSCEntNetInterface"
- "CoreWiFi API force refresh"
- "ED SCAN DONE"
- "ED SCAN RESULT"
- "GAS=%lu, "
- "Initial update"
- "MM/dd/yy HH:mm:ss.SSS"
- "T@\"CLLocation\",C"
- "T@\"CWFScanResult\",C"
- "T@\"CWFScanResult\",C,N,V_associatedNetwork"
- "T@\"CWFScanResult\",C,N,V_network"
- "T@\"NSArray\",C,N,V_candidates"
- "T@\"NSArray\",C,N,V_macIds"
- "T@\"NSArray\",C,N,V_optimizedChannelList"
- "T@\"NSSet\",C"
- "T@\"NSString\",C,N,V_macId"
- "T@?,C,V_updatedPrivateMACAddressHandler"
- "TB,N,V_wasAlreadyAssociated"
- "TB,V_didSendResponse"
- "TQ,N,V_autoHotspotDuration"
- "TQ,N,V_autoHotspotJoinDuration"
- "TQ,N,V_duration"
- "TQ,N,V_durationFromDeviceUnlockTrigger"
- "TQ,N,V_durationFromDisplayOnTrigger"
- "TQ,N,V_durationFromLinkDownTrigger"
- "TQ,N,V_durationFromNonRetryAutoJoinTrigger"
- "TQ,N,V_durationFromWiFiPowerOnTrigger"
- "TQ,N,V_joinDuration"
- "Tq,N,V_previousNonRetryAutoJoinTrigger"
- "[corewifi] %{public}s (%{public}s:%u) Invalid macId %{public}@"
- "[corewifi] %{public}s (%{public}s:%u) Invalid macId list %{public}@"
- "[corewifi] @[%llu.%06llu] %{public}s (%{public}s:%u) %@ is a valid network interface, but was not a valid 80211 interface (non80211=%@)"
- "[corewifi] @[%llu.%06llu] %{public}s (%{public}s:%u) %s CWFApple80211 (%@)"
- "[corewifi] @[%llu.%06llu] %{public}s (%{public}s:%u) %s CWFEAP8021X (%{public}@)"
- "[corewifi] @[%llu.%06llu] %{public}s (%{public}s:%u) %s CWFSCNetworkInterface (%{public}@)"
- "[corewifi] @[%llu.%06llu] %{public}s (%{public}s:%u) %s CWFSCNetworkService (%@)"
- "[corewifi] @[%llu.%06llu] %{public}s (%{public}s:%u) Did NOT find matching WiFi interface after interface list refresh (name=%{public}@, role=%{public}@, uuid=%{public}@)"
- "[corewifi] @[%llu.%06llu] %{public}s (%{public}s:%u) Found matching WiFi interface after interface list refresh (name=%{public}@, role=%{public}@, uuid=%{public}@)"
- "[corewifi] @[%llu.%06llu] %{public}s (%{public}s:%u) No WiFi matching interface exists, refreshing interface list (name=%{public}@, role=%{public}@, uuid=%{public}@)"
- "[corewifi] @[%llu.%06llu] %{public}s (%{public}s:%u) Non WiFi interface name specified (name=%{public}@, role=%{public}@, uuid=%{public}@)"
- "[corewifi] @[%llu.%06llu] %{public}s (%{public}s:%u) Using %{public}@ based on interface role '%{public}@'"
- "[corewifi] @[%llu.%06llu] %{public}s (%{public}s:%u) Using default interface role '%{public}@' based on '%{public}@' request type"
- "[corewifi] @[%llu.%06llu] %{public}s (%{public}s:%u) WiFi interface added (%{public}@)"
- "[corewifi] @[%llu.%06llu] %{public}s (%{public}s:%u) WiFi interface added (%{public}@) posted notification"
- "[corewifi] @[%llu.%06llu] %{public}s (%{public}s:%u) WiFi interface not eligible for removal (%{public}@)"
- "[corewifi] @[%llu.%06llu] %{public}s (%{public}s:%u) WiFi interface removed (%{public}@)"
- "[corewifi] @[%llu.%06llu] %{public}s (%{public}s:%u) __updateWiFiNetworkInterfaces: CWFIO80211: (%{public}@) (%{public}@)"
- "[corewifi] @[%llu.%06llu] %{public}s (%{public}s:%u) __updateWiFiNetworkInterfaces: CWFIO80211: (%{public}@) (%{public}@), a11[%p]"
- "[corewifi] @[%llu.%06llu] %{public}s (%{public}s:%u) __updateWiFiNetworkInterfaces: CWFKernelEventMonitor: (%{public}@) eventCode[0x%08lx/%lu]/(%{public}@)"
- "[corewifi] @[%llu.%06llu] %{public}s (%{public}s:%u) __updateWiFiNetworkInterfaces: CWFKernelEventMonitor: (%{public}@) eventCode[0x%08lx/%lu]/(%{public}@), update[%u] a11[%p]"
- "[corewifi] @[%llu.%06llu] %{public}s (%{public}s:%u) __updateWiFiNetworkInterfaces: CWFSCNetworkConfiguration/kSCDynamicStoreDomainSetup: (%{public}@)"
- "[corewifi] @[%llu.%06llu] %{public}s (%{public}s:%u) __updateWiFiNetworkInterfaces: CWFSCNetworkConfiguration/kSCEntNetInterface: (%{public}@)"
- "[corewifi] @[%llu.%06llu] %{public}s (%{public}s:%u) __updateWiFiNetworkInterfaces: Initial update"
- "[corewifi] @[%llu.%06llu] %{public}s (%{public}s:%u) __updateWiFiNetworkInterfaces: updateReason(%{public}@), took [%llu.%06llu], waited [%llu.%06llu] ifq[%llu.%06llu] mutex[%llu.%06llu] scnet[%llu.%06llu], ifnames: (%{public}@), vifnames: (%{public}@), apple80211Map: (%{public}@), eligibleForRemoval: (%{public}@), , networkInterfaceNames: (%{public}@)"
- "[corewifi] AUTO-JOIN: Adding adjacent 5GHz channel (%{public}@) for CarPlay network '%{public}@'"
- "[corewifi] PRIVATE MAC: Did not find cached association network ID, forgetting IP configuration for network (%{public}@)"
- "[corewifi] PRIVATE MAC: Forgetting IP configuration for known network with changed private MAC setting (%{public}@)"
- "[corewifi] PRIVATE MAC: Forgetting IP configuration for updated private MAC address for network (%{public}@)"
- "[corewifi] PRIVATE MAC: Forgetting captive configuration for public AirPlay network with changed private MAC setting (%{public}@)"
- "[corewifi] PRIVATE MAC: Forgetting captive configuration for updated private MAC address for public AirPlay network (%{public}@)"
- "[request.macIds count] > 0 && [request.macIds count] <= MAX_NDD_FILTER"
- "__isAnyKnownNetworkNearby"
- "__updateCachedMetricAndStatistics:"
- "__updateWiFiNetworkInterfaces:reply:"
- "_autoHotspotDuration"
- "_autoHotspotJoinDuration"
- "_candidates"
- "_didSendResponse"
- "_duration"
- "_durationFromDeviceUnlockTrigger"
- "_durationFromDisplayOnTrigger"
- "_durationFromLinkDownTrigger"
- "_durationFromNonRetryAutoJoinTrigger"
- "_durationFromWiFiPowerOnTrigger"
- "_interfaceQueue"
- "_joinDuration"
- "_macId"
- "_macIds"
- "_network"
- "_networkIDCache"
- "_networkIDCacheIDList"
- "_optimizedChannelList"
- "_previousNonRetryAutoJoinTrigger"
- "_previousNonRetryTrigger"
- "_stringByReplacingOccurencesOfRegexPattern:replacement:"
- "_updatedPrivateMACAddressHandler"
- "_wasAlreadyAssociated"
- "autoHotspot=[%lu (candidate=%lu, join=%lu, abort=%lu)], "
- "autoJoin=[%lu (retry=%lu, candidate=%lu, join=%lu, already=%lu, abort=%lu)], "
- "auto_hotspot_aborted_count"
- "auto_hotspot_count"
- "auto_hotspot_did_find_candidate_count"
- "auto_hotspot_did_join_count"
- "auto_join_aborted_count"
- "auto_join_already_assoc_count"
- "auto_join_count"
- "auto_join_did_find_candidate_count"
- "auto_join_did_join_count"
- "auto_join_retry_count"
- "auto_join_trigger_counts"
- "candidates"
- "captiveKnownNetworksCount"
- "com.apple.corewifi.XPC-common-intf"
- "combinedScan=[%lu (2GHz=%lu, 5GHz=%lu, 6GHz=%lu)], "
- "combined_scan_channel_count"
- "combined_scan_channel_count_2ghz"
- "combined_scan_channel_count_5ghz"
- "combined_scan_channel_count_6ghz"
- "didSendResponse"
- "durationFromNonRetryAutoJoinTrigger"
- "durationFromNonRetryTrigger"
- "followup6GHzScan=%lu, "
- "followup_6ghz_scan_channel_count"
- "gas_query_count"
- "hiddenKnownNetworksCount"
- "joinedKnownNetworksCountLast2Years"
- "joinedKnownNetworksCountLast3Months"
- "joinedKnownNetworksCountLast6Months"
- "joinedKnownNetworksCountLastMonth"
- "joinedKnownNetworksCountLastWeek"
- "joinedKnownNetworksCountLastYear"
- "knownNetworksCount"
- "macId"
- "macId=%@, "
- "macIds"
- "macIds="
- "network"
- "networkIsSplitSSID6GHz"
- "nonCaptiveKnownNetworksCount"
- "optimizedChannelList"
- "optimizedChannelList=%@"
- "optimized_channel_list"
- "preAssocScan=[%lu (2GHz=%lu, 5GHz=%lu, 6GHz=%lu)], "
- "pre_assoc_scan_channel_count"
- "pre_assoc_scan_channel_count_2ghz"
- "pre_assoc_scan_channel_count_5ghz"
- "pre_assoc_scan_channel_count_6ghz"
- "previousNonRetryAutoJoinTrigger"
- "previousNonRetryTrigger"
- "scan=[%lu (2GHz=%lu, 5GHz=%lu, 6GHz=%lu)], "
- "scan_channel_count"
- "scan_channel_count_2ghz"
- "scan_channel_count_5ghz"
- "scan_channel_count_6ghz"
- "setAutoHotspotDuration:"
- "setAutoHotspotJoinDuration:"
- "setCandidates:"
- "setDidSendResponse:"
- "setDuration:"
- "setDurationFromDeviceUnlockTrigger:"
- "setDurationFromDisplayOnTrigger:"
- "setDurationFromLinkDownTrigger:"
- "setDurationFromNonRetryAutoJoinTrigger:"
- "setDurationFromWiFiPowerOnTrigger:"
- "setJoinDuration:"
- "setMacId:"
- "setMacIds:"
- "setNetwork:"
- "setOptimizedChannelList:"
- "setPreviousNonRetryAutoJoinTrigger:"
- "setUpdatedPrivateMACAddressHandler:"
- "setWasAlreadyAssociated:"
- "startedAt=%@, "
- "triggers=(%@)"
- "updatedPrivateMACAddressHandler"
- "v24@?0@\"CWFNetworkProfile\"8@\"NSString\"16"
- "yyyy/MM/dd HH:mm:ss:SSS"

```
