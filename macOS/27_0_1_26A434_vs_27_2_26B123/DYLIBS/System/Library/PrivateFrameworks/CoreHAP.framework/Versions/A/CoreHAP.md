## CoreHAP

> `/System/Library/PrivateFrameworks/CoreHAP.framework/Versions/A/CoreHAP`

```diff

-1493.1.5.4.1
-  __TEXT.__text: 0x2b37f0
-  __TEXT.__objc_methlist: 0x17d80
-  __TEXT.__const: 0x11c8
-  __TEXT.__constg_swiftt: 0x960
-  __TEXT.__swift5_typeref: 0x3e4
-  __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_reflstr: 0x474
-  __TEXT.__swift5_fieldmd: 0x3f0
-  __TEXT.__swift5_assocty: 0xc0
-  __TEXT.__swift5_proto: 0x50
-  __TEXT.__swift5_types: 0x30
-  __TEXT.__cstring: 0x13d35
-  __TEXT.__oslogstring: 0x3d570
-  __TEXT.__swift5_capture: 0x288
-  __TEXT.__gcc_except_tab: 0x5890
-  __TEXT.__unwind_info: 0x7330
-  __TEXT.__eh_frame: 0x1080
+1520.2.7.4.1
+  __TEXT.__text: 0x30c214
+  __TEXT.__objc_methlist: 0x1b9d0
+  __TEXT.__const: 0x1798
+  __TEXT.__constg_swiftt: 0xc20
+  __TEXT.__swift5_typeref: 0x533
+  __TEXT.__swift5_builtin: 0xdc
+  __TEXT.__swift5_reflstr: 0x851
+  __TEXT.__swift5_fieldmd: 0x6a4
+  __TEXT.__swift5_assocty: 0x138
+  __TEXT.__swift5_proto: 0x78
+  __TEXT.__swift5_types: 0x5c
+  __TEXT.__cstring: 0x16d06
+  __TEXT.__oslogstring: 0x42fda
+  __TEXT.__swift5_protos: 0x4
+  __TEXT.__swift5_capture: 0x28c
+  __TEXT.__gcc_except_tab: 0x6964
+  __TEXT.__unwind_info: 0x8340
+  __TEXT.__eh_frame: 0x1078
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2148
-  __DATA_CONST.__objc_classlist: 0xbf8
+  __DATA_CONST.__const: 0x2498
+  __DATA_CONST.__objc_classlist: 0xd78
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x390
+  __DATA_CONST.__objc_protolist: 0x3c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7c28
-  __DATA_CONST.__objc_protorefs: 0x100
-  __DATA_CONST.__objc_superrefs: 0xa40
+  __DATA_CONST.__objc_selrefs: 0x9178
+  __DATA_CONST.__objc_protorefs: 0x110
+  __DATA_CONST.__objc_superrefs: 0xb98
   __DATA_CONST.__objc_arraydata: 0x200
-  __DATA_CONST.__got: 0xfb8
-  __AUTH_CONST.__const: 0x5468
-  __AUTH_CONST.__cfstring: 0xf7a0
-  __AUTH_CONST.__objc_const: 0x29fc8
-  __AUTH_CONST.__objc_intobj: 0x588
+  __DATA_CONST.__got: 0x1150
+  __AUTH_CONST.__const: 0x5dd0
+  __AUTH_CONST.__cfstring: 0x10e80
+  __AUTH_CONST.__objc_const: 0x30ea8
+  __AUTH_CONST.__weak_auth_got: 0x10
+  __AUTH_CONST.__objc_intobj: 0x5a0
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0xc0
-  __AUTH_CONST.__auth_got: 0x10b0
-  __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x7228
-  __AUTH.__data: 0xb0
+  __AUTH_CONST.__auth_got: 0x11b8
+  __AUTH_CONST.__auth_ptr: 0x258
+  __AUTH.__objc_data: 0x8330
+  __AUTH.__data: 0x130
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x28
-  __DATA.__objc_ivar: 0x17fc
-  __DATA.__data: 0x2c22
+  __DATA.__objc_ivar: 0x1cd4
+  __DATA.__data: 0x2fd8
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xd80
-  __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0xfc8
+  __DATA.__bss: 0x11a0
+  __DATA.__common: 0x90
+  __DATA_DIRTY.__objc_data: 0x1108
   __DATA_DIRTY.__data: 0x40
-  __DATA_DIRTY.__bss: 0x88
+  __DATA_DIRTY.__bss: 0xc8
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9510
-  Symbols:   19560
-  CStrings:  6554
+  Functions: 11078
+  Symbols:   22445
+  CStrings:  7135
 
Symbols:
+ +[HAP2AccessoryDeviceIPAddress accessoryDeviceIPAddressWithSerializedData:]
+ +[HAP2AccessoryServerCoordinator(Test) coordinatorForUnitTestsWithBrowser:operationQueue:delegate:]
+ +[HAP2AccessoryServerDiscoveryHAPAccessoryInfo accessoryInfoWithDeviceID:rawDiscoveryInfo:]
+ +[HAP2AccessoryServerIPCacheData dataWithDictionary:deviceID:]
+ +[HAP2AccessoryServerIPCacheData logCategory]
+ +[HAP2SessionKeepAliveConfiguration computeSelectedConfigurationForTransportType:isSleepyEndDevice:supportedMinInterval:supportedMaxInterval:supportedMinRange:]
+ +[HAP2ThreadNetworkUtil _eventQueue]
+ +[HAP2ThreadNetworkUtil _fetchMeshLocalPrefixFromXPC]
+ +[HAP2ThreadNetworkUtil _setSharedThreadClient:]
+ +[HAP2ThreadNetworkUtil forceRefreshMeshLocalPrefix]
+ +[HAP2ThreadNetworkUtil isNetworkLinkManagementEnabled]
+ +[HAP2ThreadNetworkUtil setupEventSubscriptions]
+ +[HAPAVCStreamingControlCommandWrapper parsedFromData:error:]
+ +[HAPAVCStreamingControlRequest parsedFromData:error:]
+ +[HAPAVCStreamingControlResponse parsedFromData:error:]
+ +[HAPAVCStreamingControlStatusWrapper parsedFromData:error:]
+ +[HAPAVCViewerRegistrationOperationWrapper parsedFromData:error:]
+ +[HAPBluetoothMetrics parsedFromData:error:]
+ +[HAPBootReasonsMetrics parsedFromData:error:]
+ +[HAPCHMMetrics parsedFromData:error:]
+ +[HAPConnectionHealthMonitor parsedFromData:error:]
+ +[HAPContributingSensor parsedFromData:error:]
+ +[HAPDefaultWorkQueueFactory sharedFactory]
+ +[HAPErrorCountersMetrics parsedFromData:error:]
+ +[HAPErrorCountersMetricsEntry parsedFromData:error:]
+ +[HAPHKSV3UploadLatencyMetrics parsedFromData:error:]
+ +[HAPMetricEventBluetoothVersionTypeWrapper parsedFromData:error:]
+ +[HAPMetricEventPowerSourcesBitmaskWrapper parsedFromData:error:]
+ +[HAPMetricEventPowerSourcesEnumWrapper parsedFromData:error:]
+ +[HAPMetricEventThreadFirstRestartConnectivityStateWrapper parsedFromData:error:]
+ +[HAPMetricEventWiFiFirstRestartConnectivityStateWrapper parsedFromData:error:]
+ +[HAPMetricEventWiFiVersionTypeWrapper parsedFromData:error:]
+ +[HAPPowerMetrics parsedFromData:error:]
+ +[HAPSaturationMetrics parsedFromData:error:]
+ +[HAPSensorList parsedFromData:error:]
+ +[HAPSessionKeepAliveTransportTypeWrapper parsedFromData:error:]
+ +[HAPStabilityMetrics parsedFromData:error:]
+ +[HAPStabilityMetricsBootReasonTypeWrapper parsedFromData:error:]
+ +[HAPStabilityMetricsHardwareFaultTypeWrapper parsedFromData:error:]
+ +[HAPTLVPreferredWiFiEntry parsedFromData:error:]
+ +[HAPTLVPreferredWiFiList parsedFromData:error:]
+ +[HAPTLVSelectedSessionKeepAliveConfigurationEntry parsedFromData:error:]
+ +[HAPTLVSelectedSessionKeepAliveConfigurationList parsedFromData:error:]
+ +[HAPTLVSupportedSessionKeepAliveConfigurationEntry parsedFromData:error:]
+ +[HAPTLVSupportedSessionKeepAliveConfigurationList parsedFromData:error:]
+ +[HAPThermalMetrics parsedFromData:error:]
+ +[HAPWiFiMetrics parsedFromData:error:]
+ -[HAP2AccessoryAddressLists .cxx_destruct]
+ -[HAP2AccessoryAddressLists cachedPrimary]
+ -[HAP2AccessoryAddressLists cachedSecondary]
+ -[HAP2AccessoryAddressLists description]
+ -[HAP2AccessoryAddressLists initWithPrimary:secondary:]
+ -[HAP2AccessoryAddressLists initWithPrimary:secondary:cachedPrimary:cachedSecondary:]
+ -[HAP2AccessoryAddressLists isEmpty]
+ -[HAP2AccessoryAddressLists primary]
+ -[HAP2AccessoryAddressLists secondary]
+ -[HAP2AccessoryAddressLists setCachedPrimary:]
+ -[HAP2AccessoryAddressLists setCachedSecondary:]
+ -[HAP2AccessoryAddressLists setPrimary:]
+ -[HAP2AccessoryAddressLists setSecondary:]
+ -[HAP2AccessoryAddressResolverPipeline .cxx_destruct]
+ -[HAP2AccessoryAddressResolverPipeline _acquireDNSContextOwnership]
+ -[HAP2AccessoryAddressResolverPipeline _clearAllAddresses]
+ -[HAP2AccessoryAddressResolverPipeline _coapAddressFromGAIResult:outAddress:]
+ -[HAP2AccessoryAddressResolverPipeline _handleGetaddrinfoEvent:error:]
+ -[HAP2AccessoryAddressResolverPipeline _handleGetaddrinfoResults:count:]
+ -[HAP2AccessoryAddressResolverPipeline _handleResolveCallbackWithError:hostname:port:]
+ -[HAP2AccessoryAddressResolverPipeline _recordAddedAddress:]
+ -[HAP2AccessoryAddressResolverPipeline _recordRemovedAddress:]
+ -[HAP2AccessoryAddressResolverPipeline _releaseDNSContextOwnership]
+ -[HAP2AccessoryAddressResolverPipeline _restampWorkingSetWithResolvedPort]
+ -[HAP2AccessoryAddressResolverPipeline _startGetaddrinfoForHostname:]
+ -[HAP2AccessoryAddressResolverPipeline cancel]
+ -[HAP2AccessoryAddressResolverPipeline initWithQueue:updateHandler:errorHandler:]
+ -[HAP2AccessoryAddressResolverPipeline publishedAddresses]
+ -[HAP2AccessoryAddressResolverPipeline startWithServiceName:serviceType:serviceDomain:]
+ -[HAP2AccessoryDNSResolver .cxx_destruct]
+ -[HAP2AccessoryDNSResolver _applyCachedIP:transportType:notifySubscriber:seedAgingClock:]
+ -[HAP2AccessoryDNSResolver _handlePipelineError:]
+ -[HAP2AccessoryDNSResolver _handlePipelineUpdate:]
+ -[HAP2AccessoryDNSResolver _restartPipelineOnQueue]
+ -[HAP2AccessoryDNSResolver _seedCachedIP:transportType:]
+ -[HAP2AccessoryDNSResolver _startPipelineOnQueue]
+ -[HAP2AccessoryDNSResolver _tearDownPipeline]
+ -[HAP2AccessoryDNSResolver _test_setBecameEmptyAt:]
+ -[HAP2AccessoryDNSResolver attachCacheSubscriber:]
+ -[HAP2AccessoryDNSResolver attachDelegate:]
+ -[HAP2AccessoryDNSResolver becameEmptyAt]
+ -[HAP2AccessoryDNSResolver cachedIPDidUpdate:transportType:]
+ -[HAP2AccessoryDNSResolver currentAddresses]
+ -[HAP2AccessoryDNSResolver dealloc]
+ -[HAP2AccessoryDNSResolver deferAgingClockIfRunning]
+ -[HAP2AccessoryDNSResolver detachCacheSubscriber:]
+ -[HAP2AccessoryDNSResolver detachDelegate:]
+ -[HAP2AccessoryDNSResolver deviceID]
+ -[HAP2AccessoryDNSResolver initWithDeviceID:serviceName:managerQueue:pipelineFactory:]
+ -[HAP2AccessoryDNSResolver performHealthCheck]
+ -[HAP2AccessoryDNSResolver serviceName]
+ -[HAP2AccessoryDNSResolver startPipeline]
+ -[HAP2AccessoryDNSResolver stopPipeline]
+ -[HAP2AccessoryDNSResolver updateServiceName:]
+ -[HAP2AccessoryDeviceIPAddress _classifyTransportType:]
+ -[HAP2AccessoryDeviceIPAddress copyWithZone:]
+ -[HAP2AccessoryDeviceIPAddress debugDescription]
+ -[HAP2AccessoryDeviceIPAddress hash]
+ -[HAP2AccessoryDeviceIPAddress isEqual:]
+ -[HAP2AccessoryDeviceIPAddress isIPv6]
+ -[HAP2AccessoryDeviceIPAddress serializedData]
+ -[HAP2AccessoryDeviceIPAddress transportType]
+ -[HAP2AccessoryServer _attachResolverAndForwardToTransport:]
+ -[HAP2AccessoryServer _controllerUnchecked]
+ -[HAP2AccessoryServer _runLostDiscoveryAdvertisementSideEffectsWithWillSleep:]
+ -[HAP2AccessoryServer _runResolverReactiveWorkWithWas:now:connectionState:]
+ -[HAP2AccessoryServer _setHasDiscoveryAdvertisementLockOnly:]
+ -[HAP2AccessoryServer _setHasThreadAdvertisement:]
+ -[HAP2AccessoryServer _setHasWiFiAdvertisement:]
+ -[HAP2AccessoryServer dnsResolver]
+ -[HAP2AccessoryServer hasSeededSinceResolverAttach]
+ -[HAP2AccessoryServer hasThreadAdvertisement]
+ -[HAP2AccessoryServer hasWiFiAdvertisement]
+ -[HAP2AccessoryServer lastObservedHasAdvertisement]
+ -[HAP2AccessoryServer setDnsResolver:]
+ -[HAP2AccessoryServer setHasSeededSinceResolverAttach:]
+ -[HAP2AccessoryServer setHasThreadAdvertisement:]
+ -[HAP2AccessoryServer setHasWiFiAdvertisement:]
+ -[HAP2AccessoryServer setKeepAliveListener:]
+ -[HAP2AccessoryServer setLastObservedHasAdvertisement:]
+ -[HAP2AccessoryServer(Paired) closeSessionWithCompletion:]
+ -[HAP2AccessoryServer(Paired) configureKeepAliveListener:]
+ -[HAP2AccessoryServer(Paired) currentResolverSnapshot]
+ -[HAP2AccessoryServer(Paired) didChangeThreadAdvertisement:]
+ -[HAP2AccessoryServer(Paired) didChangeWiFiAdvertisement:]
+ -[HAP2AccessoryServer(Paired) didReceiveHeartbeatOnTransport:]
+ -[HAP2AccessoryServer(Paired) mergeWithNewlyDiscoveredPairedAccessoryServer:resolver:]
+ -[HAP2AccessoryServer(Paired) pairVerifyDidCompleteOnIPAddress:transportType:]
+ -[HAP2AccessoryServer(Paired) pairVerifyDidFailOnIPAddress:transportType:error:]
+ -[HAP2AccessoryServer(Paired) resolver:didUpdateAddresses:]
+ -[HAP2AccessoryServer(Paired) restartKeepAliveListener]
+ -[HAP2AccessoryServer(PairedInternal) _closeSessionIfConnectedIPAddressStaleForTransport:]
+ -[HAP2AccessoryServer(PairedInternal) _handleProbeCompletion:forKeepAliveTransport:]
+ -[HAP2AccessoryServer(PairedInternal) _haveAllTransportsHitFailureThreshold]
+ -[HAP2AccessoryServer(PairedInternal) keepAliveListener:didMissHeartbeatOnTransport:expectedInterval:timeSinceLastHeartbeat:allTransportsMissed:]
+ -[HAP2AccessoryServer(PairedInternal) keepAliveListenerDidCompleteIPPortPairCheck:]
+ -[HAP2AccessoryServer(Test) _test_becomePaired]
+ -[HAP2AccessoryServer(Test) _test_hasDiscoveryAdvertisement]
+ -[HAP2AccessoryServer(Test) _test_hasSeededSinceResolverAttach]
+ -[HAP2AccessoryServer(Test) _test_isInternallyPaired]
+ -[HAP2AccessoryServer(Test) _test_lastObservedHasAdvertisement]
+ -[HAP2AccessoryServer(Test) _test_reactiveWorkRecorderBlock]
+ -[HAP2AccessoryServer(Test) _test_setConnectionStateUnreachable]
+ -[HAP2AccessoryServer(Test) _test_setHasSeededSinceResolverAttach:]
+ -[HAP2AccessoryServer(Test) _test_setInternallyPaired:]
+ -[HAP2AccessoryServer(Test) set_test_reactiveWorkRecorderBlock:]
+ -[HAP2AccessoryServer(Unpaired) localPairingIdentityForPairingDriver:error:]
+ -[HAP2AccessoryServer(Unpaired) pairingDriver:saveRemoteECDSAPairingKey:forAccessoryIdentifier:error:]
+ -[HAP2AccessoryServer(Unpaired) pairingDriver:saveRemotePairingIdentity:error:]
+ -[HAP2AccessoryServerBrowser _armPTRRevalidationWindow]
+ -[HAP2AccessoryServerBrowser _buildActiveDeviceIDsSet]
+ -[HAP2AccessoryServerBrowser _cancelPTRRevalidationWindow]
+ -[HAP2AccessoryServerBrowser _fireRevalidationSweep]
+ -[HAP2AccessoryServerBrowser _initializeFromCachedRecord:deviceID:]
+ -[HAP2AccessoryServerBrowser _performAuditPass]
+ -[HAP2AccessoryServerBrowser _reinitializeFromCachedRecordsAfterCoordinatorsStarted]
+ -[HAP2AccessoryServerBrowser _restoreCachedAccessoryServersIfNeeded]
+ -[HAP2AccessoryServerBrowser attachSelfAsCacheSubscriberOnResolver:]
+ -[HAP2AccessoryServerBrowser auditScheduler]
+ -[HAP2AccessoryServerBrowser cachedIPDidUpdate:transportType:forDeviceID:]
+ -[HAP2AccessoryServerBrowser currentPTRs]
+ -[HAP2AccessoryServerBrowser dealloc]
+ -[HAP2AccessoryServerBrowser existingPTRs]
+ -[HAP2AccessoryServerBrowser hasCurrentPTRForDeviceID:]
+ -[HAP2AccessoryServerBrowser hasDiscoveryAdvertisementForAccessoryWithID:]
+ -[HAP2AccessoryServerBrowser hasThreadAdvertisementForAccessoryWithID:]
+ -[HAP2AccessoryServerBrowser hasWiFiAdvertisementForAccessoryWithID:]
+ -[HAP2AccessoryServerBrowser ipCache]
+ -[HAP2AccessoryServerBrowser isInitialCacheRestored]
+ -[HAP2AccessoryServerBrowser localPairingIdentityForDeviceID:error:]
+ -[HAP2AccessoryServerBrowser noteBonjourAdvertisementUpdatedForDeviceID:rawDiscoveryInfo:]
+ -[HAP2AccessoryServerBrowser noteBrowsedPTRAddForDeviceID:serviceName:]
+ -[HAP2AccessoryServerBrowser noteBrowsedPTRRemoveForDeviceID:]
+ -[HAP2AccessoryServerBrowser noteResolverReapedForDeviceID:]
+ -[HAP2AccessoryServerBrowser pendingRevalidationPTRs]
+ -[HAP2AccessoryServerBrowser resolverRegistry]
+ -[HAP2AccessoryServerBrowser revalidationTimer]
+ -[HAP2AccessoryServerBrowser setAuditScheduler:]
+ -[HAP2AccessoryServerBrowser setIPCache:]
+ -[HAP2AccessoryServerBrowser setIpCache:]
+ -[HAP2AccessoryServerBrowser setIsInitialCacheRestored:]
+ -[HAP2AccessoryServerBrowser setPendingRevalidationPTRs:]
+ -[HAP2AccessoryServerBrowser setResolverRegistry:]
+ -[HAP2AccessoryServerBrowser setRevalidationTimer:]
+ -[HAP2AccessoryServerBrowser(Test) _test_auditScheduler]
+ -[HAP2AccessoryServerBrowser(Test) _test_hasDiscoveryAdvertisementForAccessoryWithID:]
+ -[HAP2AccessoryServerBrowser(Test) _test_hasThreadAdvertisementForAccessoryWithID:]
+ -[HAP2AccessoryServerBrowser(Test) _test_hasWiFiAdvertisementForAccessoryWithID:]
+ -[HAP2AccessoryServerBrowser(Test) _test_performAuditPass]
+ -[HAP2AccessoryServerBrowser(Test) _test_restoreCachedAccessoryServersIfNeeded]
+ -[HAP2AccessoryServerBrowser(Test) _test_setLivePairedServers:]
+ -[HAP2AccessoryServerBrowser(Test) _test_setResolverRegistry:]
+ -[HAP2AccessoryServerController _announceReestablishedSessionIfNeeded]
+ -[HAP2AccessoryServerController applyResolverAddresses:completion:]
+ -[HAP2AccessoryServerController checkConnectedIPAddressStaleOnTransport:completion:]
+ -[HAP2AccessoryServerController closeSessionWithCompletion:]
+ -[HAP2AccessoryServerController forceSessionExpired]
+ -[HAP2AccessoryServerController hasArmedCacheOnlyLatch]
+ -[HAP2AccessoryServerController isReadingAttributeDatabase]
+ -[HAP2AccessoryServerController localPairingIdentityForSecureTransport:error:]
+ -[HAP2AccessoryServerController readLocalEndpointsWithHandler:]
+ -[HAP2AccessoryServerController secureTransport:didChangeThreadAdvertisement:]
+ -[HAP2AccessoryServerController secureTransport:didChangeWiFiAdvertisement:]
+ -[HAP2AccessoryServerController secureTransport:didReceiveHeartbeatOnTransport:]
+ -[HAP2AccessoryServerController secureTransport:ecdsaLongTermPublicKeyForPeerWithIdentifier:error:]
+ -[HAP2AccessoryServerController secureTransport:localPairingIdentityForECDSAKeyPairSetupSession:error:]
+ -[HAP2AccessoryServerController secureTransport:pairVerifyDidCompleteOnIPAddress:transportType:]
+ -[HAP2AccessoryServerController secureTransport:pairVerifyDidFailOnIPAddress:transportType:error:]
+ -[HAP2AccessoryServerController secureTransport:remotePairingIdentityForDeviceID:error:]
+ -[HAP2AccessoryServerController secureTransportCurrentResolverSnapshot:]
+ -[HAP2AccessoryServerController sendProbeOnTransport:completion:]
+ -[HAP2AccessoryServerController setUnitTest_useHH2:]
+ -[HAP2AccessoryServerCoordinator _didDiscoverAccessory:fromMDNSEvent:completion:]
+ -[HAP2AccessoryServerCoordinator initializePairedAccessoryServerFromCachedInfo:]
+ -[HAP2AccessoryServerCoordinator(Test) _test_deliverDiscovery:]
+ -[HAP2AccessoryServerCoordinator(Test) _test_deliverLoss:]
+ -[HAP2AccessoryServerDiscoveryBonjour lastKnownAccessoryInfoByServiceKey]
+ -[HAP2AccessoryServerEncodingThread _parseCharacteristics:isMultiTransportAccessory:error:]
+ -[HAP2AccessoryServerIPCacheData .cxx_destruct]
+ -[HAP2AccessoryServerIPCacheData cachedPrimaryData]
+ -[HAP2AccessoryServerIPCacheData cachedSecondaryData]
+ -[HAP2AccessoryServerIPCacheData configurationInfo]
+ -[HAP2AccessoryServerIPCacheData deviceID]
+ -[HAP2AccessoryServerIPCacheData dictionaryRepresentation]
+ -[HAP2AccessoryServerIPCacheData initFromDictionary:deviceID:]
+ -[HAP2AccessoryServerIPCacheData initWithDeviceID:cachedPrimaryData:cachedSecondaryData:configurationInfo:]
+ -[HAP2AccessoryServerIPCacheData setCachedPrimaryData:]
+ -[HAP2AccessoryServerIPCacheData setCachedSecondaryData:]
+ -[HAP2AccessoryServerIPCacheData setConfigurationInfo:]
+ -[HAP2AccessoryServerIPCacheData setDeviceID:]
+ -[HAP2AccessoryServerSecureTransportBase applyResolverAddresses:completion:]
+ -[HAP2AccessoryServerSecureTransportBase checkConnectedIPAddressStaleOnTransport:completion:]
+ -[HAP2AccessoryServerSecureTransportBase hasArmedCacheOnlyLatch]
+ -[HAP2AccessoryServerSecureTransportBase lastCompletedMessageID]
+ -[HAP2AccessoryServerSecureTransportBase readLocalEndpointsWithHandler:]
+ -[HAP2AccessoryServerSecureTransportBase sendProbeOnTransport:completion:]
+ -[HAP2AccessoryServerSecureTransportBase setSupportsKeepAlive:]
+ -[HAP2AccessoryServerSecureTransportBase setSupportsThreadTransport:]
+ -[HAP2AccessoryServerSecureTransportBase setSupportsWiFiTransport:]
+ -[HAP2AccessoryServerSecureTransportBase transport:didChangeThreadAdvertisement:]
+ -[HAP2AccessoryServerSecureTransportBase transport:didChangeWiFiAdvertisement:]
+ -[HAP2AccessoryServerSecureTransportBase transport:didReceiveHeartbeatOnTransport:]
+ -[HAP2AccessoryServerSecureTransportBase transport:pairVerifyDidCompleteOnIPAddress:transportType:]
+ -[HAP2AccessoryServerSecureTransportBase transport:pairVerifyDidFailOnIPAddress:transportType:error:]
+ -[HAP2AccessoryServerSecureTransportBase transportCurrentResolverSnapshot:]
+ -[HAP2AccessoryServerSecureTransportPairSetup transport:didReceiveHeartbeatOnTransport:]
+ -[HAP2AccessoryServerSecureTransportPairVerify _claimStateChangeCompletionForGeneration:]
+ -[HAP2AccessoryServerSecureTransportPairVerify _clearECDSAStateForGeneration:]
+ -[HAP2AccessoryServerSecureTransportPairVerify _createSecuritySessionFromECDSASessionForGeneration:]
+ -[HAP2AccessoryServerSecureTransportPairVerify _currentStateChangeGeneration]
+ -[HAP2AccessoryServerSecureTransportPairVerify _handleECDSASessionFailure:generation:]
+ -[HAP2AccessoryServerTransportBase hasQueuedCloseOperation]
+ -[HAP2AccessoryServerTransportBase lastCompletedMessageID]
+ -[HAP2AccessoryServerTransportBase setSupportsKeepAlive:]
+ -[HAP2AccessoryServerTransportBase setSupportsThreadTransport:]
+ -[HAP2AccessoryServerTransportBase setSupportsWiFiTransport:]
+ -[HAP2AccessoryServerTransportBase supportsKeepAlive]
+ -[HAP2AccessoryServerTransportBase supportsThreadTransport]
+ -[HAP2AccessoryServerTransportBase supportsWiFiTransport]
+ -[HAP2AccessoryServerTransportCoAP _applyResolverAddressesOnQueue:]
+ -[HAP2AccessoryServerTransportCoAP _armInitialCacheGracePeriodTimerIfNeeded]
+ -[HAP2AccessoryServerTransportCoAP _beginInitialOpenLoggingAddress:transportLabel:]
+ -[HAP2AccessoryServerTransportCoAP _buildSecondaryCoapClientWithAddress:]
+ -[HAP2AccessoryServerTransportCoAP _cancelFailoverTimer]
+ -[HAP2AccessoryServerTransportCoAP _cancelResolver]
+ -[HAP2AccessoryServerTransportCoAP _completeRequest:error:path:]
+ -[HAP2AccessoryServerTransportCoAP _createCoapClient]
+ -[HAP2AccessoryServerTransportCoAP _evaluateCacheMissCancelIfNeededWithLivePrimaryCount:]
+ -[HAP2AccessoryServerTransportCoAP _executeCacheMissCancel]
+ -[HAP2AccessoryServerTransportCoAP _failInitialOpenWithError:]
+ -[HAP2AccessoryServerTransportCoAP _handleInitialResolvePrimary:]
+ -[HAP2AccessoryServerTransportCoAP _handleInitialResolveSecondary:]
+ -[HAP2AccessoryServerTransportCoAP _handleInitialResolverComplete]
+ -[HAP2AccessoryServerTransportCoAP _handleLiveResolverUpdate]
+ -[HAP2AccessoryServerTransportCoAP _handleRefreshResolve:isFromPrimaryList:]
+ -[HAP2AccessoryServerTransportCoAP _handleResolve:isFromPrimaryList:]
+ -[HAP2AccessoryServerTransportCoAP _logAddress:index:]
+ -[HAP2AccessoryServerTransportCoAP _maybeFireOffQueueCacheMissCancelForAddresses:]
+ -[HAP2AccessoryServerTransportCoAP _openPrimaryClientForRefreshWithAddress:]
+ -[HAP2AccessoryServerTransportCoAP _openPrimaryClientIteratingWithCompletion:]
+ -[HAP2AccessoryServerTransportCoAP _openSecondaryClientForRefreshWithAddress:]
+ -[HAP2AccessoryServerTransportCoAP _openSecondaryClientIteratingIsThreadOnly:completion:]
+ -[HAP2AccessoryServerTransportCoAP _readLocalEndpointForClient:transport:into:completion:]
+ -[HAP2AccessoryServerTransportCoAP _refreshIPAddresses]
+ -[HAP2AccessoryServerTransportCoAP _resetIPsTriedThisSession]
+ -[HAP2AccessoryServerTransportCoAP _resetInitialCacheOnlyStopgapState]
+ -[HAP2AccessoryServerTransportCoAP _resolveAddress]
+ -[HAP2AccessoryServerTransportCoAP _resolveFailedWithError:]
+ -[HAP2AccessoryServerTransportCoAP _sendEndpointRegistration]
+ -[HAP2AccessoryServerTransportCoAP _sendHelloIfReady]
+ -[HAP2AccessoryServerTransportCoAP _sendMultiTransportRequest:path:]
+ -[HAP2AccessoryServerTransportCoAP _sendRegistrationTLVWithAddressBytes:port:]
+ -[HAP2AccessoryServerTransportCoAP _sendWiFiEndpointRegistration]
+ -[HAP2AccessoryServerTransportCoAP _setIpAddress:]
+ -[HAP2AccessoryServerTransportCoAP _shouldRegisterEndpoint]
+ -[HAP2AccessoryServerTransportCoAP _startResolveTimeoutTimer]
+ -[HAP2AccessoryServerTransportCoAP _startResolverIfNeeded]
+ -[HAP2AccessoryServerTransportCoAP _takeNextPrimaryIPToTry]
+ -[HAP2AccessoryServerTransportCoAP _takeNextSecondaryIPToTry]
+ -[HAP2AccessoryServerTransportCoAP _tearDownInitialCacheGracePeriodTimer]
+ -[HAP2AccessoryServerTransportCoAP addressResolverFactory]
+ -[HAP2AccessoryServerTransportCoAP advanceEndpointAfterPairVerifyFailureWithCompletion:]
+ -[HAP2AccessoryServerTransportCoAP applyResolverAddresses:completion:]
+ -[HAP2AccessoryServerTransportCoAP checkConnectedIPAddressStaleOnTransport:completion:]
+ -[HAP2AccessoryServerTransportCoAP clientDidReceivePing:]
+ -[HAP2AccessoryServerTransportCoAP dataStreamPeerAddressWithCompletion:]
+ -[HAP2AccessoryServerTransportCoAP hasArmedCacheOnlyLatch]
+ -[HAP2AccessoryServerTransportCoAP hasRegisteredEndpoint]
+ -[HAP2AccessoryServerTransportCoAP initialACKTimeout]
+ -[HAP2AccessoryServerTransportCoAP initialCacheGracePeriodTimer]
+ -[HAP2AccessoryServerTransportCoAP initialConnectionAttemptStartedAt]
+ -[HAP2AccessoryServerTransportCoAP lastCompletedMessageID]
+ -[HAP2AccessoryServerTransportCoAP lastMessageID]
+ -[HAP2AccessoryServerTransportCoAP logIPAddresses]
+ -[HAP2AccessoryServerTransportCoAP maxTransmitAttempts]
+ -[HAP2AccessoryServerTransportCoAP primaryEffectiveListIsCacheOnly]
+ -[HAP2AccessoryServerTransportCoAP primaryIPsTriedThisSession]
+ -[HAP2AccessoryServerTransportCoAP primaryOpenInFlight]
+ -[HAP2AccessoryServerTransportCoAP readLocalEndpointsWithHandler:]
+ -[HAP2AccessoryServerTransportCoAP resolveTimeoutTimer]
+ -[HAP2AccessoryServerTransportCoAP resolverRestartTimer]
+ -[HAP2AccessoryServerTransportCoAP secondaryAddressList]
+ -[HAP2AccessoryServerTransportCoAP secondaryCoAPClient]
+ -[HAP2AccessoryServerTransportCoAP secondaryIPsTriedThisSession]
+ -[HAP2AccessoryServerTransportCoAP securedClient]
+ -[HAP2AccessoryServerTransportCoAP sendProbeOnTransport:completion:]
+ -[HAP2AccessoryServerTransportCoAP setAddressResolverFactory:]
+ -[HAP2AccessoryServerTransportCoAP setHasRegisteredEndpoint:]
+ -[HAP2AccessoryServerTransportCoAP setInFlightRacingLogEvent:]
+ -[HAP2AccessoryServerTransportCoAP setInitialCacheGracePeriodTimer:]
+ -[HAP2AccessoryServerTransportCoAP setInitialConnectionAttemptStartedAt:]
+ -[HAP2AccessoryServerTransportCoAP setLastCompletedMessageID:]
+ -[HAP2AccessoryServerTransportCoAP setLastMessageID:]
+ -[HAP2AccessoryServerTransportCoAP setNumOfAddresses:]
+ -[HAP2AccessoryServerTransportCoAP setNumOfAddressesTried:]
+ -[HAP2AccessoryServerTransportCoAP setPrimaryEffectiveListIsCacheOnly:]
+ -[HAP2AccessoryServerTransportCoAP setPrimaryOpenInFlight:]
+ -[HAP2AccessoryServerTransportCoAP setResolveTimeoutTimer:]
+ -[HAP2AccessoryServerTransportCoAP setResolverRestartTimer:]
+ -[HAP2AccessoryServerTransportCoAP setSecondaryCoAPClient:]
+ -[HAP2AccessoryServerTransportCoAP setSecuredClient:]
+ -[HAP2AccessoryServerTransportCoAP setTryingInitialCacheOnly:]
+ -[HAP2AccessoryServerTransportCoAP signalPairVerifyFailureToDelegateWithError:]
+ -[HAP2AccessoryServerTransportCoAP signalPairVerifySuccessToDelegate]
+ -[HAP2AccessoryServerTransportCoAP tryingInitialCacheOnly]
+ -[HAP2BrowserResolverRegistry .cxx_destruct]
+ -[HAP2BrowserResolverRegistry _performAuditPassOnQueueWithActiveDeviceIDs:]
+ -[HAP2BrowserResolverRegistry browser]
+ -[HAP2BrowserResolverRegistry createResolverWithDeviceID:serviceName:]
+ -[HAP2BrowserResolverRegistry initWithName:browser:]
+ -[HAP2BrowserResolverRegistry managerQueue]
+ -[HAP2BrowserResolverRegistry name]
+ -[HAP2BrowserResolverRegistry performAuditPassWithActiveDeviceIDs:]
+ -[HAP2BrowserResolverRegistry pipelineFactory]
+ -[HAP2BrowserResolverRegistry propertyLock]
+ -[HAP2BrowserResolverRegistry removeResolverForDeviceID:]
+ -[HAP2BrowserResolverRegistry resolverForDeviceID:]
+ -[HAP2BrowserResolverRegistry resolversByDeviceID]
+ -[HAP2BrowserResolverRegistry setPipelineFactory:]
+ -[HAP2BrowserResolverRegistry updateCachedAddressesForDeviceID:cachedPrimary:cachedSecondary:]
+ -[HAP2BrowserResolverRegistry(Test) _allDeviceIDs]
+ -[HAP2BrowserResolverRegistry(Test) _managerQueue]
+ -[HAP2BrowserResolverRegistry(Test) _pipelineFactory]
+ -[HAP2BrowserResolverRegistry(Test) _privateResolverForDeviceID:]
+ -[HAP2BrowserResolverRegistry(Test) set_pipelineFactory:]
+ -[HAP2CoAPClient _didDisconnectWithError:]
+ -[HAP2CoAPClient _fireProbeCompletionWithResponse:error:]
+ -[HAP2CoAPClient address]
+ -[HAP2CoAPClient didReceivePingInSession:messageID:]
+ -[HAP2CoAPClient getLocalEndpointWithCompletion:]
+ -[HAP2CoAPClient getLocalIPv4EndpointWithCompletion:]
+ -[HAP2CoAPClient getLocalIPv6EndpointWithCompletion:]
+ -[HAP2CoAPClient getRTTStatisticsWithCompletion:]
+ -[HAP2CoAPClient sendProbeWithCompletion:]
+ -[HAP2CoAPClient sendRequestWithMethod:path:payload:messageID:dscpPriority:completion:]
+ -[HAP2DefaultAccessoryAddressResolverPipelineFactory createResolverWithServiceName:serviceType:serviceDomain:queue:updateHandler:errorHandler:]
+ -[HAP2SerializedOperationQueue _applyCallerQoSToOperations:]
+ -[HAP2SerializedOperationQueue addConcurrentBlock:qos:]
+ -[HAP2SessionKeepAliveConfigurationEntry initWithTransportType:minimumInterval:maximumInterval:]
+ -[HAP2SessionKeepAliveConfigurationEntry maximumInterval]
+ -[HAP2SessionKeepAliveConfigurationEntry minimumInterval]
+ -[HAP2SessionKeepAliveConfigurationEntry transportType]
+ -[HAP2SessionKeepAliveListener .cxx_destruct]
+ -[HAP2SessionKeepAliveListener _copyDelegates]
+ -[HAP2SessionKeepAliveListener _handleTimerFireForTransport:]
+ -[HAP2SessionKeepAliveListener addDelegate:]
+ -[HAP2SessionKeepAliveListener dateProvider]
+ -[HAP2SessionKeepAliveListener dealloc]
+ -[HAP2SessionKeepAliveListener delegates]
+ -[HAP2SessionKeepAliveListener didReceiveHeartbeatOnTransport:]
+ -[HAP2SessionKeepAliveListener hasMissedHeartbeatForTransport:]
+ -[HAP2SessionKeepAliveListener initWithConfigurationEntries:workQueue:]
+ -[HAP2SessionKeepAliveListener initWithConfigurationEntries:workQueue:timerProvider:dateProvider:]
+ -[HAP2SessionKeepAliveListener isRunning]
+ -[HAP2SessionKeepAliveListener isTrackingTransport:]
+ -[HAP2SessionKeepAliveListener logIdentifier]
+ -[HAP2SessionKeepAliveListener missCheckTimer]
+ -[HAP2SessionKeepAliveListener removeDelegate:]
+ -[HAP2SessionKeepAliveListener resetHeartbeatTimestamps]
+ -[HAP2SessionKeepAliveListener setDateProvider:]
+ -[HAP2SessionKeepAliveListener setDelegates:]
+ -[HAP2SessionKeepAliveListener setIsRunning:]
+ -[HAP2SessionKeepAliveListener setMissCheckTimer:]
+ -[HAP2SessionKeepAliveListener setTimerProvider:]
+ -[HAP2SessionKeepAliveListener setTransportStates:]
+ -[HAP2SessionKeepAliveListener setWorkQueue:]
+ -[HAP2SessionKeepAliveListener start]
+ -[HAP2SessionKeepAliveListener stop]
+ -[HAP2SessionKeepAliveListener timeSinceLastHeartbeatForTransport:]
+ -[HAP2SessionKeepAliveListener timerDidFire:]
+ -[HAP2SessionKeepAliveListener timerProvider]
+ -[HAP2SessionKeepAliveListener trackedTransportTypes]
+ -[HAP2SessionKeepAliveListener transportStates]
+ -[HAP2SessionKeepAliveListener workQueue]
+ -[HAP2SessionKeepAliveTransportState .cxx_destruct]
+ -[HAP2SessionKeepAliveTransportState hasMissedHeartbeat]
+ -[HAP2SessionKeepAliveTransportState initWithTransportType:maximumInterval:]
+ -[HAP2SessionKeepAliveTransportState lastHeartbeatTime]
+ -[HAP2SessionKeepAliveTransportState maximumInterval]
+ -[HAP2SessionKeepAliveTransportState setHasMissedHeartbeat:]
+ -[HAP2SessionKeepAliveTransportState setLastHeartbeatTime:]
+ -[HAP2SessionKeepAliveTransportState transportType]
+ -[HAPAVCStreamingControlCommandWrapper copyWithZone:]
+ -[HAPAVCStreamingControlCommandWrapper description]
+ -[HAPAVCStreamingControlCommandWrapper initWithValue:]
+ -[HAPAVCStreamingControlCommandWrapper init]
+ -[HAPAVCStreamingControlCommandWrapper isEqual:]
+ -[HAPAVCStreamingControlCommandWrapper parseFromData:error:]
+ -[HAPAVCStreamingControlCommandWrapper serializeWithError:]
+ -[HAPAVCStreamingControlCommandWrapper setValue:]
+ -[HAPAVCStreamingControlCommandWrapper value]
+ -[HAPAVCStreamingControlRequest .cxx_destruct]
+ -[HAPAVCStreamingControlRequest command]
+ -[HAPAVCStreamingControlRequest copyWithZone:]
+ -[HAPAVCStreamingControlRequest description]
+ -[HAPAVCStreamingControlRequest initWithSessionIdentifier:command:]
+ -[HAPAVCStreamingControlRequest init]
+ -[HAPAVCStreamingControlRequest isEqual:]
+ -[HAPAVCStreamingControlRequest parseFromData:error:]
+ -[HAPAVCStreamingControlRequest serializeWithError:]
+ -[HAPAVCStreamingControlRequest sessionIdentifier]
+ -[HAPAVCStreamingControlRequest setCommand:]
+ -[HAPAVCStreamingControlRequest setSessionIdentifier:]
+ -[HAPAVCStreamingControlResponse .cxx_destruct]
+ -[HAPAVCStreamingControlResponse copyWithZone:]
+ -[HAPAVCStreamingControlResponse description]
+ -[HAPAVCStreamingControlResponse initWithSessionIdentifier:status:]
+ -[HAPAVCStreamingControlResponse init]
+ -[HAPAVCStreamingControlResponse isEqual:]
+ -[HAPAVCStreamingControlResponse parseFromData:error:]
+ -[HAPAVCStreamingControlResponse serializeWithError:]
+ -[HAPAVCStreamingControlResponse sessionIdentifier]
+ -[HAPAVCStreamingControlResponse setSessionIdentifier:]
+ -[HAPAVCStreamingControlResponse setStatus:]
+ -[HAPAVCStreamingControlResponse status]
+ -[HAPAVCStreamingControlStatusWrapper copyWithZone:]
+ -[HAPAVCStreamingControlStatusWrapper description]
+ -[HAPAVCStreamingControlStatusWrapper initWithValue:]
+ -[HAPAVCStreamingControlStatusWrapper init]
+ -[HAPAVCStreamingControlStatusWrapper isEqual:]
+ -[HAPAVCStreamingControlStatusWrapper parseFromData:error:]
+ -[HAPAVCStreamingControlStatusWrapper serializeWithError:]
+ -[HAPAVCStreamingControlStatusWrapper setValue:]
+ -[HAPAVCStreamingControlStatusWrapper value]
+ -[HAPAVCViewerRegistrationOperationWrapper copyWithZone:]
+ -[HAPAVCViewerRegistrationOperationWrapper description]
+ -[HAPAVCViewerRegistrationOperationWrapper initWithValue:]
+ -[HAPAVCViewerRegistrationOperationWrapper init]
+ -[HAPAVCViewerRegistrationOperationWrapper isEqual:]
+ -[HAPAVCViewerRegistrationOperationWrapper parseFromData:error:]
+ -[HAPAVCViewerRegistrationOperationWrapper serializeWithError:]
+ -[HAPAVCViewerRegistrationOperationWrapper setValue:]
+ -[HAPAVCViewerRegistrationOperationWrapper value]
+ -[HAPAVCViewerRegistrationRequest initWithSessionIdentifier:viewerParticipantID:viewerNegotiationBlob:operation:]
+ -[HAPAVCViewerRegistrationRequest operation]
+ -[HAPAVCViewerRegistrationRequest setOperation:]
+ -[HAPAccessoryInfo hasAssignedProductPlan]
+ -[HAPAccessoryPairingRequest init]
+ -[HAPAccessoryPairingRequest setShouldAllowECDSAKeyPairSetup:]
+ -[HAPAccessoryPairingRequest shouldAllowECDSAKeyPairSetup]
+ -[HAPAccessoryServer configureKeepAliveListener:]
+ -[HAPAccessoryServer disconnectWithCompletion:]
+ -[HAPAccessoryServer hasThreadAdvertisement]
+ -[HAPAccessoryServer hasWiFiAdvertisement]
+ -[HAPAccessoryServer lastPairSetupWasSpake2]
+ -[HAPAccessoryServer pairSetupLastError]
+ -[HAPAccessoryServer pairSetupM1ToM4Completed]
+ -[HAPAccessoryServer pairSetupM1ToM4DurationMS]
+ -[HAPAccessoryServer pairSetupM1ToM4Error]
+ -[HAPAccessoryServer pairSetupM5ToM6Completed]
+ -[HAPAccessoryServer pairSetupM5ToM6DurationMS]
+ -[HAPAccessoryServer pairSetupM5ToM6Error]
+ -[HAPAccessoryServer pairSetupWorkDurationMS]
+ -[HAPAccessoryServer setHasThreadAdvertisement:]
+ -[HAPAccessoryServer setHasWiFiAdvertisement:]
+ -[HAPAccessoryServer setLastPairSetupWasSpake2:]
+ -[HAPAccessoryServer setPairSetupLastError:]
+ -[HAPAccessoryServer setPairSetupM1ToM4Completed:]
+ -[HAPAccessoryServer setPairSetupM1ToM4DurationMS:]
+ -[HAPAccessoryServer setPairSetupM1ToM4Error:]
+ -[HAPAccessoryServer setPairSetupM5ToM6Completed:]
+ -[HAPAccessoryServer setPairSetupM5ToM6DurationMS:]
+ -[HAPAccessoryServer setPairSetupM5ToM6Error:]
+ -[HAPAccessoryServer setPairSetupWorkDurationMS:]
+ -[HAPAccessoryServer setTokenAuthCompleted:]
+ -[HAPAccessoryServer setTokenAuthDurationMS:]
+ -[HAPAccessoryServer setTokenAuthError:]
+ -[HAPAccessoryServer tokenAuthCompleted]
+ -[HAPAccessoryServer tokenAuthDurationMS]
+ -[HAPAccessoryServer tokenAuthError]
+ -[HAPAccessoryServer workQueueFactory]
+ -[HAPAccessoryServerBrowser hasWiFiAdvertisementForHAP2AccessoryServerIdentifier:]
+ -[HAPAccessoryServerBrowser isThreadAccessoryDiscoveredWithAccessoryServerIdentifier:]
+ -[HAPAccessoryServerBrowserHAP2Adapter hasWiFiAdvertisementForHAP2AccessoryServerIdentifier:]
+ -[HAPAccessoryServerBrowserHAP2Adapter isThreadAccessoryDiscoveredWithAccessoryServerIdentifier:]
+ -[HAPAccessoryServerBrowserHAP2Adapter setIPCache:]
+ -[HAPAccessoryServerHAP2Adapter accessoryServer:didUpdateLocalEndpoints:]
+ -[HAPAccessoryServerHAP2Adapter configureKeepAliveListener:]
+ -[HAPAccessoryServerHAP2Adapter dataStreamPeerAddressWithCompletion:]
+ -[HAPAccessoryServerHAP2Adapter deriveEncryptionForDataStreamWithKeySalt:completionHandler:]
+ -[HAPAccessoryServerHAP2Adapter disconnectWithCompletion:]
+ -[HAPAccessoryServerHAP2Adapter hasThreadAdvertisement]
+ -[HAPAccessoryServerHAP2Adapter hasWiFiAdvertisement]
+ -[HAPAccessoryServerIP disconnectWithCompletion:]
+ -[HAPAccessoryServerIP hasWiFiAdvertisement]
+ -[HAPAccessoryServerIP selfAddress]
+ -[HAPBluetoothMetrics .cxx_destruct]
+ -[HAPBluetoothMetrics bluetoothVersion]
+ -[HAPBluetoothMetrics connectionCount]
+ -[HAPBluetoothMetrics connectionErrorCount]
+ -[HAPBluetoothMetrics connectionStatus]
+ -[HAPBluetoothMetrics copyWithZone:]
+ -[HAPBluetoothMetrics description]
+ -[HAPBluetoothMetrics disconnectionCount]
+ -[HAPBluetoothMetrics disconnectionErrorCount]
+ -[HAPBluetoothMetrics hwExceptionCount]
+ -[HAPBluetoothMetrics initWithBluetoothVersion:rssi:txPowerLevel:packetRxCount:packetTxCount:packetRxErrorCount:packetTxErrorCount:overrunCount:connectionStatus:connectionCount:connectionErrorCount:disconnectionCount:disconnectionErrorCount:hwExceptionCount:]
+ -[HAPBluetoothMetrics init]
+ -[HAPBluetoothMetrics isEqual:]
+ -[HAPBluetoothMetrics overrunCount]
+ -[HAPBluetoothMetrics packetRxCount]
+ -[HAPBluetoothMetrics packetRxErrorCount]
+ -[HAPBluetoothMetrics packetTxCount]
+ -[HAPBluetoothMetrics packetTxErrorCount]
+ -[HAPBluetoothMetrics parseFromData:error:]
+ -[HAPBluetoothMetrics rssi]
+ -[HAPBluetoothMetrics serializeWithError:]
+ -[HAPBluetoothMetrics setBluetoothVersion:]
+ -[HAPBluetoothMetrics setConnectionCount:]
+ -[HAPBluetoothMetrics setConnectionErrorCount:]
+ -[HAPBluetoothMetrics setConnectionStatus:]
+ -[HAPBluetoothMetrics setDisconnectionCount:]
+ -[HAPBluetoothMetrics setDisconnectionErrorCount:]
+ -[HAPBluetoothMetrics setHwExceptionCount:]
+ -[HAPBluetoothMetrics setOverrunCount:]
+ -[HAPBluetoothMetrics setPacketRxCount:]
+ -[HAPBluetoothMetrics setPacketRxErrorCount:]
+ -[HAPBluetoothMetrics setPacketTxCount:]
+ -[HAPBluetoothMetrics setPacketTxErrorCount:]
+ -[HAPBluetoothMetrics setRssi:]
+ -[HAPBluetoothMetrics setTxPowerLevel:]
+ -[HAPBluetoothMetrics txPowerLevel]
+ -[HAPBootReasonsMetrics .cxx_destruct]
+ -[HAPBootReasonsMetrics brownOutResetBootCount]
+ -[HAPBootReasonsMetrics connectivityMonitorBootCount]
+ -[HAPBootReasonsMetrics copyWithZone:]
+ -[HAPBootReasonsMetrics description]
+ -[HAPBootReasonsMetrics hardwareFaultBootCount]
+ -[HAPBootReasonsMetrics hardwareWatchdogResetBootCount]
+ -[HAPBootReasonsMetrics heapOverflowBootCount]
+ -[HAPBootReasonsMetrics initWithUnspecifiedBootCount:powerOnBootCount:brownOutResetBootCount:softwareWatchdogResetBootCount:hardwareWatchdogResetBootCount:softwareUpdateCompletedBootCount:softwareResetBootCount:softwareExceptionBootCount:hardwareFaultBootCount:stackOverflowBootCount:heapOverflowBootCount:temperatureLimitBootCount:connectivityMonitorBootCount:]
+ -[HAPBootReasonsMetrics init]
+ -[HAPBootReasonsMetrics isEqual:]
+ -[HAPBootReasonsMetrics parseFromData:error:]
+ -[HAPBootReasonsMetrics powerOnBootCount]
+ -[HAPBootReasonsMetrics serializeWithError:]
+ -[HAPBootReasonsMetrics setBrownOutResetBootCount:]
+ -[HAPBootReasonsMetrics setConnectivityMonitorBootCount:]
+ -[HAPBootReasonsMetrics setHardwareFaultBootCount:]
+ -[HAPBootReasonsMetrics setHardwareWatchdogResetBootCount:]
+ -[HAPBootReasonsMetrics setHeapOverflowBootCount:]
+ -[HAPBootReasonsMetrics setPowerOnBootCount:]
+ -[HAPBootReasonsMetrics setSoftwareExceptionBootCount:]
+ -[HAPBootReasonsMetrics setSoftwareResetBootCount:]
+ -[HAPBootReasonsMetrics setSoftwareUpdateCompletedBootCount:]
+ -[HAPBootReasonsMetrics setSoftwareWatchdogResetBootCount:]
+ -[HAPBootReasonsMetrics setStackOverflowBootCount:]
+ -[HAPBootReasonsMetrics setTemperatureLimitBootCount:]
+ -[HAPBootReasonsMetrics setUnspecifiedBootCount:]
+ -[HAPBootReasonsMetrics softwareExceptionBootCount]
+ -[HAPBootReasonsMetrics softwareResetBootCount]
+ -[HAPBootReasonsMetrics softwareUpdateCompletedBootCount]
+ -[HAPBootReasonsMetrics softwareWatchdogResetBootCount]
+ -[HAPBootReasonsMetrics stackOverflowBootCount]
+ -[HAPBootReasonsMetrics temperatureLimitBootCount]
+ -[HAPBootReasonsMetrics unspecifiedBootCount]
+ -[HAPCHMMetrics .cxx_destruct]
+ -[HAPCHMMetrics chmAccessoryRebootCompleted]
+ -[HAPCHMMetrics chmAccessoryRebootDurationToRecovery]
+ -[HAPCHMMetrics copyWithZone:]
+ -[HAPCHMMetrics description]
+ -[HAPCHMMetrics hapSessionLossCount]
+ -[HAPCHMMetrics initWithWifiTransportLossCount:wifiRecoveryAttemptCount:wifiRestartCount:wifiFirstRestartRecoveryTime:wifiFirstRestartCompleted:wifiFirstRestartConnectivityState:threadTransportLossCount:threadRecoveryAttemptCount:threadRestartCount:threadFirstRestartRecoveryTime:threadFirstRestartCompleted:threadFirstRestartConnectivityState:hapSessionLossCount:chmAccessoryRebootDurationToRecovery:chmAccessoryRebootCompleted:]
+ -[HAPCHMMetrics init]
+ -[HAPCHMMetrics isEqual:]
+ -[HAPCHMMetrics parseFromData:error:]
+ -[HAPCHMMetrics serializeWithError:]
+ -[HAPCHMMetrics setChmAccessoryRebootCompleted:]
+ -[HAPCHMMetrics setChmAccessoryRebootDurationToRecovery:]
+ -[HAPCHMMetrics setHapSessionLossCount:]
+ -[HAPCHMMetrics setThreadFirstRestartCompleted:]
+ -[HAPCHMMetrics setThreadFirstRestartConnectivityState:]
+ -[HAPCHMMetrics setThreadFirstRestartRecoveryTime:]
+ -[HAPCHMMetrics setThreadRecoveryAttemptCount:]
+ -[HAPCHMMetrics setThreadRestartCount:]
+ -[HAPCHMMetrics setThreadTransportLossCount:]
+ -[HAPCHMMetrics setWifiFirstRestartCompleted:]
+ -[HAPCHMMetrics setWifiFirstRestartConnectivityState:]
+ -[HAPCHMMetrics setWifiFirstRestartRecoveryTime:]
+ -[HAPCHMMetrics setWifiRecoveryAttemptCount:]
+ -[HAPCHMMetrics setWifiRestartCount:]
+ -[HAPCHMMetrics setWifiTransportLossCount:]
+ -[HAPCHMMetrics threadFirstRestartCompleted]
+ -[HAPCHMMetrics threadFirstRestartConnectivityState]
+ -[HAPCHMMetrics threadFirstRestartRecoveryTime]
+ -[HAPCHMMetrics threadRecoveryAttemptCount]
+ -[HAPCHMMetrics threadRestartCount]
+ -[HAPCHMMetrics threadTransportLossCount]
+ -[HAPCHMMetrics wifiFirstRestartCompleted]
+ -[HAPCHMMetrics wifiFirstRestartConnectivityState]
+ -[HAPCHMMetrics wifiFirstRestartRecoveryTime]
+ -[HAPCHMMetrics wifiRecoveryAttemptCount]
+ -[HAPCHMMetrics wifiRestartCount]
+ -[HAPCHMMetrics wifiTransportLossCount]
+ -[HAPCharacteristicResponseTuple coapMessageID]
+ -[HAPCharacteristicResponseTuple setCoapMessageID:]
+ -[HAPConnectionHealthMonitor .cxx_destruct]
+ -[HAPConnectionHealthMonitor copyWithZone:]
+ -[HAPConnectionHealthMonitor description]
+ -[HAPConnectionHealthMonitor deviceRebootDelay]
+ -[HAPConnectionHealthMonitor deviceRebootEnable]
+ -[HAPConnectionHealthMonitor initWithDeviceRebootEnable:threadRecoveryConfiguration:wiFiRecoveryConfiguration:recoveryStaggerDelay:deviceRebootDelay:threadPingTestCount:threadPingTestInterval:threadRestartMinInterval:wiFiPingTestCount:wiFiPingTestInterval:wiFiRestartMinInterval:]
+ -[HAPConnectionHealthMonitor init]
+ -[HAPConnectionHealthMonitor isEqual:]
+ -[HAPConnectionHealthMonitor parseFromData:error:]
+ -[HAPConnectionHealthMonitor recoveryStaggerDelay]
+ -[HAPConnectionHealthMonitor serializeWithError:]
+ -[HAPConnectionHealthMonitor setDeviceRebootDelay:]
+ -[HAPConnectionHealthMonitor setDeviceRebootEnable:]
+ -[HAPConnectionHealthMonitor setRecoveryStaggerDelay:]
+ -[HAPConnectionHealthMonitor setThreadPingTestCount:]
+ -[HAPConnectionHealthMonitor setThreadPingTestInterval:]
+ -[HAPConnectionHealthMonitor setThreadRecoveryConfiguration:]
+ -[HAPConnectionHealthMonitor setThreadRestartMinInterval:]
+ -[HAPConnectionHealthMonitor setWiFiPingTestCount:]
+ -[HAPConnectionHealthMonitor setWiFiPingTestInterval:]
+ -[HAPConnectionHealthMonitor setWiFiRecoveryConfiguration:]
+ -[HAPConnectionHealthMonitor setWiFiRestartMinInterval:]
+ -[HAPConnectionHealthMonitor threadPingTestCount]
+ -[HAPConnectionHealthMonitor threadPingTestInterval]
+ -[HAPConnectionHealthMonitor threadRecoveryConfiguration]
+ -[HAPConnectionHealthMonitor threadRestartMinInterval]
+ -[HAPConnectionHealthMonitor wiFiPingTestCount]
+ -[HAPConnectionHealthMonitor wiFiPingTestInterval]
+ -[HAPConnectionHealthMonitor wiFiRecoveryConfiguration]
+ -[HAPConnectionHealthMonitor wiFiRestartMinInterval]
+ -[HAPContributingSensor .cxx_destruct]
+ -[HAPContributingSensor copyWithZone:]
+ -[HAPContributingSensor description]
+ -[HAPContributingSensor initWithSensorUUID:]
+ -[HAPContributingSensor init]
+ -[HAPContributingSensor isEqual:]
+ -[HAPContributingSensor parseFromData:error:]
+ -[HAPContributingSensor sensorUUID]
+ -[HAPContributingSensor serializeWithError:]
+ -[HAPContributingSensor setSensorUUID:]
+ -[HAPCoreUtilsHTTPClient getSelfAddress:maxLength:outLength:]
+ -[HAPDefaultWorkQueueFactory newQueueWithLabel:attributes:]
+ -[HAPDefaultWorkQueueFactory newQueueWithLabel:attributes:target:]
+ -[HAPErrorCountersMetrics .cxx_destruct]
+ -[HAPErrorCountersMetrics copyWithZone:]
+ -[HAPErrorCountersMetrics description]
+ -[HAPErrorCountersMetrics entries]
+ -[HAPErrorCountersMetrics initWithEntries:]
+ -[HAPErrorCountersMetrics init]
+ -[HAPErrorCountersMetrics isEqual:]
+ -[HAPErrorCountersMetrics parseFromData:error:]
+ -[HAPErrorCountersMetrics serializeWithError:]
+ -[HAPErrorCountersMetrics setEntries:]
+ -[HAPErrorCountersMetricsEntry .cxx_destruct]
+ -[HAPErrorCountersMetricsEntry copyWithZone:]
+ -[HAPErrorCountersMetricsEntry count]
+ -[HAPErrorCountersMetricsEntry description]
+ -[HAPErrorCountersMetricsEntry errorID]
+ -[HAPErrorCountersMetricsEntry initWithErrorID:count:]
+ -[HAPErrorCountersMetricsEntry init]
+ -[HAPErrorCountersMetricsEntry isEqual:]
+ -[HAPErrorCountersMetricsEntry parseFromData:error:]
+ -[HAPErrorCountersMetricsEntry serializeWithError:]
+ -[HAPErrorCountersMetricsEntry setCount:]
+ -[HAPErrorCountersMetricsEntry setErrorID:]
+ -[HAPHKSV3UploadLatencyMetrics .cxx_destruct]
+ -[HAPHKSV3UploadLatencyMetrics abandonedRequestCount]
+ -[HAPHKSV3UploadLatencyMetrics audioOnlyFailureCount]
+ -[HAPHKSV3UploadLatencyMetrics authenticationErrorCount]
+ -[HAPHKSV3UploadLatencyMetrics copyWithZone:]
+ -[HAPHKSV3UploadLatencyMetrics description]
+ -[HAPHKSV3UploadLatencyMetrics fragmentFailureCount]
+ -[HAPHKSV3UploadLatencyMetrics fragmentRetriedCount]
+ -[HAPHKSV3UploadLatencyMetrics fragmentSuccessCount]
+ -[HAPHKSV3UploadLatencyMetrics initWithFragmentSuccessCount:fragmentFailureCount:fragmentRetriedCount:networkErrorCount:authenticationErrorCount:serverReturnedErrorCount:localErrorCount:playlistFailureCount:latencyCount250ms:latencyCount500ms:latencyCount1000ms:latencyCount2000ms:latencyCount3750ms:latencyCountOver3750ms:sessionSuccessCount:partialSuccessCount:sessionFailureCount:uploadWithoutResidentResponseCount:audioOnlyFailureCount:abandonedRequestCount:]
+ -[HAPHKSV3UploadLatencyMetrics init]
+ -[HAPHKSV3UploadLatencyMetrics isEqual:]
+ -[HAPHKSV3UploadLatencyMetrics latencyCount1000ms]
+ -[HAPHKSV3UploadLatencyMetrics latencyCount2000ms]
+ -[HAPHKSV3UploadLatencyMetrics latencyCount250ms]
+ -[HAPHKSV3UploadLatencyMetrics latencyCount3750ms]
+ -[HAPHKSV3UploadLatencyMetrics latencyCount500ms]
+ -[HAPHKSV3UploadLatencyMetrics latencyCountOver3750ms]
+ -[HAPHKSV3UploadLatencyMetrics localErrorCount]
+ -[HAPHKSV3UploadLatencyMetrics networkErrorCount]
+ -[HAPHKSV3UploadLatencyMetrics parseFromData:error:]
+ -[HAPHKSV3UploadLatencyMetrics partialSuccessCount]
+ -[HAPHKSV3UploadLatencyMetrics playlistFailureCount]
+ -[HAPHKSV3UploadLatencyMetrics serializeWithError:]
+ -[HAPHKSV3UploadLatencyMetrics serverReturnedErrorCount]
+ -[HAPHKSV3UploadLatencyMetrics sessionFailureCount]
+ -[HAPHKSV3UploadLatencyMetrics sessionSuccessCount]
+ -[HAPHKSV3UploadLatencyMetrics setAbandonedRequestCount:]
+ -[HAPHKSV3UploadLatencyMetrics setAudioOnlyFailureCount:]
+ -[HAPHKSV3UploadLatencyMetrics setAuthenticationErrorCount:]
+ -[HAPHKSV3UploadLatencyMetrics setFragmentFailureCount:]
+ -[HAPHKSV3UploadLatencyMetrics setFragmentRetriedCount:]
+ -[HAPHKSV3UploadLatencyMetrics setFragmentSuccessCount:]
+ -[HAPHKSV3UploadLatencyMetrics setLatencyCount1000ms:]
+ -[HAPHKSV3UploadLatencyMetrics setLatencyCount2000ms:]
+ -[HAPHKSV3UploadLatencyMetrics setLatencyCount250ms:]
+ -[HAPHKSV3UploadLatencyMetrics setLatencyCount3750ms:]
+ -[HAPHKSV3UploadLatencyMetrics setLatencyCount500ms:]
+ -[HAPHKSV3UploadLatencyMetrics setLatencyCountOver3750ms:]
+ -[HAPHKSV3UploadLatencyMetrics setLocalErrorCount:]
+ -[HAPHKSV3UploadLatencyMetrics setNetworkErrorCount:]
+ -[HAPHKSV3UploadLatencyMetrics setPartialSuccessCount:]
+ -[HAPHKSV3UploadLatencyMetrics setPlaylistFailureCount:]
+ -[HAPHKSV3UploadLatencyMetrics setServerReturnedErrorCount:]
+ -[HAPHKSV3UploadLatencyMetrics setSessionFailureCount:]
+ -[HAPHKSV3UploadLatencyMetrics setSessionSuccessCount:]
+ -[HAPHKSV3UploadLatencyMetrics setUploadWithoutResidentResponseCount:]
+ -[HAPHKSV3UploadLatencyMetrics uploadWithoutResidentResponseCount]
+ -[HAPHTTPClient selfAddress]
+ -[HAPKeyBag cachedAccessoryKeyType]
+ -[HAPKeyBag setCachedAccessoryKeyType:]
+ -[HAPMetricEventBluetoothVersionTypeWrapper copyWithZone:]
+ -[HAPMetricEventBluetoothVersionTypeWrapper description]
+ -[HAPMetricEventBluetoothVersionTypeWrapper initWithValue:]
+ -[HAPMetricEventBluetoothVersionTypeWrapper init]
+ -[HAPMetricEventBluetoothVersionTypeWrapper isEqual:]
+ -[HAPMetricEventBluetoothVersionTypeWrapper parseFromData:error:]
+ -[HAPMetricEventBluetoothVersionTypeWrapper serializeWithError:]
+ -[HAPMetricEventBluetoothVersionTypeWrapper setValue:]
+ -[HAPMetricEventBluetoothVersionTypeWrapper value]
+ -[HAPMetricEventPowerSourcesBitmaskWrapper copyWithZone:]
+ -[HAPMetricEventPowerSourcesBitmaskWrapper description]
+ -[HAPMetricEventPowerSourcesBitmaskWrapper initWithValue:]
+ -[HAPMetricEventPowerSourcesBitmaskWrapper init]
+ -[HAPMetricEventPowerSourcesBitmaskWrapper isEqual:]
+ -[HAPMetricEventPowerSourcesBitmaskWrapper parseFromData:error:]
+ -[HAPMetricEventPowerSourcesBitmaskWrapper serializeWithError:]
+ -[HAPMetricEventPowerSourcesBitmaskWrapper setValue:]
+ -[HAPMetricEventPowerSourcesBitmaskWrapper value]
+ -[HAPMetricEventPowerSourcesEnumWrapper copyWithZone:]
+ -[HAPMetricEventPowerSourcesEnumWrapper description]
+ -[HAPMetricEventPowerSourcesEnumWrapper initWithValue:]
+ -[HAPMetricEventPowerSourcesEnumWrapper init]
+ -[HAPMetricEventPowerSourcesEnumWrapper isEqual:]
+ -[HAPMetricEventPowerSourcesEnumWrapper parseFromData:error:]
+ -[HAPMetricEventPowerSourcesEnumWrapper serializeWithError:]
+ -[HAPMetricEventPowerSourcesEnumWrapper setValue:]
+ -[HAPMetricEventPowerSourcesEnumWrapper value]
+ -[HAPMetricEventThreadFirstRestartConnectivityStateWrapper copyWithZone:]
+ -[HAPMetricEventThreadFirstRestartConnectivityStateWrapper description]
+ -[HAPMetricEventThreadFirstRestartConnectivityStateWrapper initWithValue:]
+ -[HAPMetricEventThreadFirstRestartConnectivityStateWrapper init]
+ -[HAPMetricEventThreadFirstRestartConnectivityStateWrapper isEqual:]
+ -[HAPMetricEventThreadFirstRestartConnectivityStateWrapper parseFromData:error:]
+ -[HAPMetricEventThreadFirstRestartConnectivityStateWrapper serializeWithError:]
+ -[HAPMetricEventThreadFirstRestartConnectivityStateWrapper setValue:]
+ -[HAPMetricEventThreadFirstRestartConnectivityStateWrapper value]
+ -[HAPMetricEventWiFiFirstRestartConnectivityStateWrapper copyWithZone:]
+ -[HAPMetricEventWiFiFirstRestartConnectivityStateWrapper description]
+ -[HAPMetricEventWiFiFirstRestartConnectivityStateWrapper initWithValue:]
+ -[HAPMetricEventWiFiFirstRestartConnectivityStateWrapper init]
+ -[HAPMetricEventWiFiFirstRestartConnectivityStateWrapper isEqual:]
+ -[HAPMetricEventWiFiFirstRestartConnectivityStateWrapper parseFromData:error:]
+ -[HAPMetricEventWiFiFirstRestartConnectivityStateWrapper serializeWithError:]
+ -[HAPMetricEventWiFiFirstRestartConnectivityStateWrapper setValue:]
+ -[HAPMetricEventWiFiFirstRestartConnectivityStateWrapper value]
+ -[HAPMetricEventWiFiVersionTypeWrapper copyWithZone:]
+ -[HAPMetricEventWiFiVersionTypeWrapper description]
+ -[HAPMetricEventWiFiVersionTypeWrapper initWithValue:]
+ -[HAPMetricEventWiFiVersionTypeWrapper init]
+ -[HAPMetricEventWiFiVersionTypeWrapper isEqual:]
+ -[HAPMetricEventWiFiVersionTypeWrapper parseFromData:error:]
+ -[HAPMetricEventWiFiVersionTypeWrapper serializeWithError:]
+ -[HAPMetricEventWiFiVersionTypeWrapper setValue:]
+ -[HAPMetricEventWiFiVersionTypeWrapper value]
+ -[HAPPowerMetrics .cxx_destruct]
+ -[HAPPowerMetrics batteryPercentage]
+ -[HAPPowerMetrics copyWithZone:]
+ -[HAPPowerMetrics currentPowerSource]
+ -[HAPPowerMetrics description]
+ -[HAPPowerMetrics durationOnBatteryPower]
+ -[HAPPowerMetrics durationRemainingOnBatteryPower]
+ -[HAPPowerMetrics initWithSupportedPowerSources:currentPowerSource:durationOnBatteryPower:durationRemainingOnBatteryPower:batteryPercentage:]
+ -[HAPPowerMetrics init]
+ -[HAPPowerMetrics isEqual:]
+ -[HAPPowerMetrics parseFromData:error:]
+ -[HAPPowerMetrics serializeWithError:]
+ -[HAPPowerMetrics setBatteryPercentage:]
+ -[HAPPowerMetrics setCurrentPowerSource:]
+ -[HAPPowerMetrics setDurationOnBatteryPower:]
+ -[HAPPowerMetrics setDurationRemainingOnBatteryPower:]
+ -[HAPPowerMetrics setSupportedPowerSources:]
+ -[HAPPowerMetrics supportedPowerSources]
+ -[HAPSaturationMetrics .cxx_destruct]
+ -[HAPSaturationMetrics averageCPUUtilization]
+ -[HAPSaturationMetrics averageSystemMemoryUtilization]
+ -[HAPSaturationMetrics copyWithZone:]
+ -[HAPSaturationMetrics description]
+ -[HAPSaturationMetrics heapHighwaterCount]
+ -[HAPSaturationMetrics heapOverflowCount]
+ -[HAPSaturationMetrics initWithStackHighwaterCount:lastStackHighwaterTaskName:heapHighwaterCount:lastHeapHighwaterTaskName:stackOverflowCount:lastStackOverflowTaskName:heapOverflowCount:lastHeapOverflowTaskName:averageSystemMemoryUtilization:peakSystemMemoryUtilization:systemMemoryPressureCount:processCriticalMemoryCount:lastProcessCriticalMemoryName:averageCPUUtilization:peakCPUUtilization:taskDeadlineMissCount:totalTasksScheduledCount:maxTaskReadyQueueSize:loadAverage:nonVolatileMemoryWriteCount:nonVolatileMemoryReadCount:nonVolatileMemoryWriteErrorCount:nonVolatileMemoryReadErrorCount:nonVolatileMemoryUtilization:]
+ -[HAPSaturationMetrics init]
+ -[HAPSaturationMetrics isEqual:]
+ -[HAPSaturationMetrics lastHeapHighwaterTaskName]
+ -[HAPSaturationMetrics lastHeapOverflowTaskName]
+ -[HAPSaturationMetrics lastProcessCriticalMemoryName]
+ -[HAPSaturationMetrics lastStackHighwaterTaskName]
+ -[HAPSaturationMetrics lastStackOverflowTaskName]
+ -[HAPSaturationMetrics loadAverage]
+ -[HAPSaturationMetrics maxTaskReadyQueueSize]
+ -[HAPSaturationMetrics nonVolatileMemoryReadCount]
+ -[HAPSaturationMetrics nonVolatileMemoryReadErrorCount]
+ -[HAPSaturationMetrics nonVolatileMemoryUtilization]
+ -[HAPSaturationMetrics nonVolatileMemoryWriteCount]
+ -[HAPSaturationMetrics nonVolatileMemoryWriteErrorCount]
+ -[HAPSaturationMetrics parseFromData:error:]
+ -[HAPSaturationMetrics peakCPUUtilization]
+ -[HAPSaturationMetrics peakSystemMemoryUtilization]
+ -[HAPSaturationMetrics processCriticalMemoryCount]
+ -[HAPSaturationMetrics serializeWithError:]
+ -[HAPSaturationMetrics setAverageCPUUtilization:]
+ -[HAPSaturationMetrics setAverageSystemMemoryUtilization:]
+ -[HAPSaturationMetrics setHeapHighwaterCount:]
+ -[HAPSaturationMetrics setHeapOverflowCount:]
+ -[HAPSaturationMetrics setLastHeapHighwaterTaskName:]
+ -[HAPSaturationMetrics setLastHeapOverflowTaskName:]
+ -[HAPSaturationMetrics setLastProcessCriticalMemoryName:]
+ -[HAPSaturationMetrics setLastStackHighwaterTaskName:]
+ -[HAPSaturationMetrics setLastStackOverflowTaskName:]
+ -[HAPSaturationMetrics setLoadAverage:]
+ -[HAPSaturationMetrics setMaxTaskReadyQueueSize:]
+ -[HAPSaturationMetrics setNonVolatileMemoryReadCount:]
+ -[HAPSaturationMetrics setNonVolatileMemoryReadErrorCount:]
+ -[HAPSaturationMetrics setNonVolatileMemoryUtilization:]
+ -[HAPSaturationMetrics setNonVolatileMemoryWriteCount:]
+ -[HAPSaturationMetrics setNonVolatileMemoryWriteErrorCount:]
+ -[HAPSaturationMetrics setPeakCPUUtilization:]
+ -[HAPSaturationMetrics setPeakSystemMemoryUtilization:]
+ -[HAPSaturationMetrics setProcessCriticalMemoryCount:]
+ -[HAPSaturationMetrics setStackHighwaterCount:]
+ -[HAPSaturationMetrics setStackOverflowCount:]
+ -[HAPSaturationMetrics setSystemMemoryPressureCount:]
+ -[HAPSaturationMetrics setTaskDeadlineMissCount:]
+ -[HAPSaturationMetrics setTotalTasksScheduledCount:]
+ -[HAPSaturationMetrics stackHighwaterCount]
+ -[HAPSaturationMetrics stackOverflowCount]
+ -[HAPSaturationMetrics systemMemoryPressureCount]
+ -[HAPSaturationMetrics taskDeadlineMissCount]
+ -[HAPSaturationMetrics totalTasksScheduledCount]
+ -[HAPSecuritySession deriveEncryptionForDataStreamWithKeySalt:completionHandler:]
+ -[HAPSecuritySession foreignPairVerifySession]
+ -[HAPSecuritySession setForeignPairVerifySession:]
+ -[HAPSensorList .cxx_destruct]
+ -[HAPSensorList contributingSensor]
+ -[HAPSensorList copyWithZone:]
+ -[HAPSensorList description]
+ -[HAPSensorList initWithContributingSensor:]
+ -[HAPSensorList init]
+ -[HAPSensorList isEqual:]
+ -[HAPSensorList parseFromData:error:]
+ -[HAPSensorList serializeWithError:]
+ -[HAPSensorList setContributingSensor:]
+ -[HAPSessionKeepAliveTransportTypeWrapper copyWithZone:]
+ -[HAPSessionKeepAliveTransportTypeWrapper description]
+ -[HAPSessionKeepAliveTransportTypeWrapper initWithValue:]
+ -[HAPSessionKeepAliveTransportTypeWrapper init]
+ -[HAPSessionKeepAliveTransportTypeWrapper isEqual:]
+ -[HAPSessionKeepAliveTransportTypeWrapper parseFromData:error:]
+ -[HAPSessionKeepAliveTransportTypeWrapper serializeWithError:]
+ -[HAPSessionKeepAliveTransportTypeWrapper setValue:]
+ -[HAPSessionKeepAliveTransportTypeWrapper value]
+ -[HAPStabilityMetrics .cxx_destruct]
+ -[HAPStabilityMetrics activeHardwareFaults]
+ -[HAPStabilityMetrics copyWithZone:]
+ -[HAPStabilityMetrics description]
+ -[HAPStabilityMetrics expectedBootCount]
+ -[HAPStabilityMetrics initWithSystemUptime:systemBootCount:expectedBootCount:systemCrashCount:systemHangCount:lastBootReason:activeHardwareFaults:]
+ -[HAPStabilityMetrics init]
+ -[HAPStabilityMetrics isEqual:]
+ -[HAPStabilityMetrics lastBootReason]
+ -[HAPStabilityMetrics parseFromData:error:]
+ -[HAPStabilityMetrics serializeWithError:]
+ -[HAPStabilityMetrics setActiveHardwareFaults:]
+ -[HAPStabilityMetrics setExpectedBootCount:]
+ -[HAPStabilityMetrics setLastBootReason:]
+ -[HAPStabilityMetrics setSystemBootCount:]
+ -[HAPStabilityMetrics setSystemCrashCount:]
+ -[HAPStabilityMetrics setSystemHangCount:]
+ -[HAPStabilityMetrics setSystemUptime:]
+ -[HAPStabilityMetrics systemBootCount]
+ -[HAPStabilityMetrics systemCrashCount]
+ -[HAPStabilityMetrics systemHangCount]
+ -[HAPStabilityMetrics systemUptime]
+ -[HAPStabilityMetricsBootReasonTypeWrapper copyWithZone:]
+ -[HAPStabilityMetricsBootReasonTypeWrapper description]
+ -[HAPStabilityMetricsBootReasonTypeWrapper initWithValue:]
+ -[HAPStabilityMetricsBootReasonTypeWrapper init]
+ -[HAPStabilityMetricsBootReasonTypeWrapper isEqual:]
+ -[HAPStabilityMetricsBootReasonTypeWrapper parseFromData:error:]
+ -[HAPStabilityMetricsBootReasonTypeWrapper serializeWithError:]
+ -[HAPStabilityMetricsBootReasonTypeWrapper setValue:]
+ -[HAPStabilityMetricsBootReasonTypeWrapper value]
+ -[HAPStabilityMetricsHardwareFaultTypeWrapper copyWithZone:]
+ -[HAPStabilityMetricsHardwareFaultTypeWrapper description]
+ -[HAPStabilityMetricsHardwareFaultTypeWrapper initWithValue:]
+ -[HAPStabilityMetricsHardwareFaultTypeWrapper init]
+ -[HAPStabilityMetricsHardwareFaultTypeWrapper isEqual:]
+ -[HAPStabilityMetricsHardwareFaultTypeWrapper parseFromData:error:]
+ -[HAPStabilityMetricsHardwareFaultTypeWrapper serializeWithError:]
+ -[HAPStabilityMetricsHardwareFaultTypeWrapper setValue:]
+ -[HAPStabilityMetricsHardwareFaultTypeWrapper value]
+ -[HAPSystemKeychainStore getHH2ControllerECDSAPublicKeyWithIdentifier:allowBackupRestore:]
+ -[HAPSystemKeychainStore getHH2ControllerKeyWithIdentifier:allowBackupRestore:]
+ -[HAPTLVPreferredWiFiEntry .cxx_destruct]
+ -[HAPTLVPreferredWiFiEntry PSK]
+ -[HAPTLVPreferredWiFiEntry SSID]
+ -[HAPTLVPreferredWiFiEntry copyWithZone:]
+ -[HAPTLVPreferredWiFiEntry description]
+ -[HAPTLVPreferredWiFiEntry initWithSSID:securityMode:PSK:]
+ -[HAPTLVPreferredWiFiEntry init]
+ -[HAPTLVPreferredWiFiEntry isEqual:]
+ -[HAPTLVPreferredWiFiEntry parseFromData:error:]
+ -[HAPTLVPreferredWiFiEntry securityMode]
+ -[HAPTLVPreferredWiFiEntry serializeWithError:]
+ -[HAPTLVPreferredWiFiEntry setPSK:]
+ -[HAPTLVPreferredWiFiEntry setSSID:]
+ -[HAPTLVPreferredWiFiEntry setSecurityMode:]
+ -[HAPTLVPreferredWiFiList .cxx_destruct]
+ -[HAPTLVPreferredWiFiList copyWithZone:]
+ -[HAPTLVPreferredWiFiList description]
+ -[HAPTLVPreferredWiFiList initWithPreferredWiFiList:]
+ -[HAPTLVPreferredWiFiList init]
+ -[HAPTLVPreferredWiFiList isEqual:]
+ -[HAPTLVPreferredWiFiList parseFromData:error:]
+ -[HAPTLVPreferredWiFiList preferredWiFiList]
+ -[HAPTLVPreferredWiFiList serializeWithError:]
+ -[HAPTLVPreferredWiFiList setPreferredWiFiList:]
+ -[HAPTLVSelectedSessionKeepAliveConfigurationEntry .cxx_destruct]
+ -[HAPTLVSelectedSessionKeepAliveConfigurationEntry copyWithZone:]
+ -[HAPTLVSelectedSessionKeepAliveConfigurationEntry description]
+ -[HAPTLVSelectedSessionKeepAliveConfigurationEntry initWithTransportType:minimumInterval:maximumInterval:]
+ -[HAPTLVSelectedSessionKeepAliveConfigurationEntry init]
+ -[HAPTLVSelectedSessionKeepAliveConfigurationEntry isEqual:]
+ -[HAPTLVSelectedSessionKeepAliveConfigurationEntry maximumInterval]
+ -[HAPTLVSelectedSessionKeepAliveConfigurationEntry minimumInterval]
+ -[HAPTLVSelectedSessionKeepAliveConfigurationEntry parseFromData:error:]
+ -[HAPTLVSelectedSessionKeepAliveConfigurationEntry serializeWithError:]
+ -[HAPTLVSelectedSessionKeepAliveConfigurationEntry setMaximumInterval:]
+ -[HAPTLVSelectedSessionKeepAliveConfigurationEntry setMinimumInterval:]
+ -[HAPTLVSelectedSessionKeepAliveConfigurationEntry setTransportType:]
+ -[HAPTLVSelectedSessionKeepAliveConfigurationEntry transportType]
+ -[HAPTLVSelectedSessionKeepAliveConfigurationList .cxx_destruct]
+ -[HAPTLVSelectedSessionKeepAliveConfigurationList copyWithZone:]
+ -[HAPTLVSelectedSessionKeepAliveConfigurationList description]
+ -[HAPTLVSelectedSessionKeepAliveConfigurationList entries]
+ -[HAPTLVSelectedSessionKeepAliveConfigurationList initWithEntries:]
+ -[HAPTLVSelectedSessionKeepAliveConfigurationList init]
+ -[HAPTLVSelectedSessionKeepAliveConfigurationList isEqual:]
+ -[HAPTLVSelectedSessionKeepAliveConfigurationList parseFromData:error:]
+ -[HAPTLVSelectedSessionKeepAliveConfigurationList serializeWithError:]
+ -[HAPTLVSelectedSessionKeepAliveConfigurationList setEntries:]
+ -[HAPTLVSupportedSessionKeepAliveConfigurationEntry .cxx_destruct]
+ -[HAPTLVSupportedSessionKeepAliveConfigurationEntry copyWithZone:]
+ -[HAPTLVSupportedSessionKeepAliveConfigurationEntry description]
+ -[HAPTLVSupportedSessionKeepAliveConfigurationEntry initWithTransportType:minimumInterval:maximumInterval:minimumRange:]
+ -[HAPTLVSupportedSessionKeepAliveConfigurationEntry init]
+ -[HAPTLVSupportedSessionKeepAliveConfigurationEntry isEqual:]
+ -[HAPTLVSupportedSessionKeepAliveConfigurationEntry maximumInterval]
+ -[HAPTLVSupportedSessionKeepAliveConfigurationEntry minimumInterval]
+ -[HAPTLVSupportedSessionKeepAliveConfigurationEntry minimumRange]
+ -[HAPTLVSupportedSessionKeepAliveConfigurationEntry parseFromData:error:]
+ -[HAPTLVSupportedSessionKeepAliveConfigurationEntry serializeWithError:]
+ -[HAPTLVSupportedSessionKeepAliveConfigurationEntry setMaximumInterval:]
+ -[HAPTLVSupportedSessionKeepAliveConfigurationEntry setMinimumInterval:]
+ -[HAPTLVSupportedSessionKeepAliveConfigurationEntry setMinimumRange:]
+ -[HAPTLVSupportedSessionKeepAliveConfigurationEntry setTransportType:]
+ -[HAPTLVSupportedSessionKeepAliveConfigurationEntry transportType]
+ -[HAPTLVSupportedSessionKeepAliveConfigurationList .cxx_destruct]
+ -[HAPTLVSupportedSessionKeepAliveConfigurationList copyWithZone:]
+ -[HAPTLVSupportedSessionKeepAliveConfigurationList description]
+ -[HAPTLVSupportedSessionKeepAliveConfigurationList entries]
+ -[HAPTLVSupportedSessionKeepAliveConfigurationList initWithEntries:]
+ -[HAPTLVSupportedSessionKeepAliveConfigurationList init]
+ -[HAPTLVSupportedSessionKeepAliveConfigurationList isEqual:]
+ -[HAPTLVSupportedSessionKeepAliveConfigurationList parseFromData:error:]
+ -[HAPTLVSupportedSessionKeepAliveConfigurationList serializeWithError:]
+ -[HAPTLVSupportedSessionKeepAliveConfigurationList setEntries:]
+ -[HAPThermalMetrics .cxx_destruct]
+ -[HAPThermalMetrics averageDeviceTemperature]
+ -[HAPThermalMetrics copyWithZone:]
+ -[HAPThermalMetrics description]
+ -[HAPThermalMetrics initWithTemperatureLimitViolationCount:temperatureLimitViolationDuration:minimumDeviceTemperature:maximumDeviceTemperature:averageDeviceTemperature:]
+ -[HAPThermalMetrics init]
+ -[HAPThermalMetrics isEqual:]
+ -[HAPThermalMetrics maximumDeviceTemperature]
+ -[HAPThermalMetrics minimumDeviceTemperature]
+ -[HAPThermalMetrics parseFromData:error:]
+ -[HAPThermalMetrics serializeWithError:]
+ -[HAPThermalMetrics setAverageDeviceTemperature:]
+ -[HAPThermalMetrics setMaximumDeviceTemperature:]
+ -[HAPThermalMetrics setMinimumDeviceTemperature:]
+ -[HAPThermalMetrics setTemperatureLimitViolationCount:]
+ -[HAPThermalMetrics setTemperatureLimitViolationDuration:]
+ -[HAPThermalMetrics temperatureLimitViolationCount]
+ -[HAPThermalMetrics temperatureLimitViolationDuration]
+ -[HAPWebRTCOfferOptions SFrameConfiguration]
+ -[HAPWebRTCOfferOptions initWithSFrameEnabled:SFrameConfiguration:]
+ -[HAPWebRTCOfferOptions setSFrameConfiguration:]
+ -[HAPWiFiMetrics .cxx_destruct]
+ -[HAPWiFiMetrics beaconLostCount]
+ -[HAPWiFiMetrics beaconRxCount]
+ -[HAPWiFiMetrics beaconRxInterval]
+ -[HAPWiFiMetrics bssid]
+ -[HAPWiFiMetrics channelNumber]
+ -[HAPWiFiMetrics connectionStatus]
+ -[HAPWiFiMetrics copyWithZone:]
+ -[HAPWiFiMetrics description]
+ -[HAPWiFiMetrics disconnectionCount]
+ -[HAPWiFiMetrics disconnectionDuration]
+ -[HAPWiFiMetrics gatewayIPv4Address]
+ -[HAPWiFiMetrics gatewayIPv6Address]
+ -[HAPWiFiMetrics gatewayMacAddress]
+ -[HAPWiFiMetrics hwExceptionCount]
+ -[HAPWiFiMetrics initWithGatewayMacAddress:gatewayIPv4Address:gatewayIPv6Address:subnetMask:bssid:wifiVersion:channelNumber:rssi:connectionStatus:disconnectionCount:disconnectionDuration:beaconRxCount:beaconRxInterval:beaconLostCount:ipAddressList:packetMulticastRxCount:packetMulticastRxErrorCount:packetMulticastTxCount:packetMulticastTxErrorCount:packetUnicastRxCount:packetUnicastRxErrorCount:packetUnicastTxCount:packetUnicastTxErrorCount:txPacketCount:txPacketErrorCount:rxPacketCount:rxPacketErrorCount:hwExceptionCount:wifiRestartCount:]
+ -[HAPWiFiMetrics init]
+ -[HAPWiFiMetrics ipAddressList]
+ -[HAPWiFiMetrics isEqual:]
+ -[HAPWiFiMetrics packetMulticastRxCount]
+ -[HAPWiFiMetrics packetMulticastRxErrorCount]
+ -[HAPWiFiMetrics packetMulticastTxCount]
+ -[HAPWiFiMetrics packetMulticastTxErrorCount]
+ -[HAPWiFiMetrics packetUnicastRxCount]
+ -[HAPWiFiMetrics packetUnicastRxErrorCount]
+ -[HAPWiFiMetrics packetUnicastTxCount]
+ -[HAPWiFiMetrics packetUnicastTxErrorCount]
+ -[HAPWiFiMetrics parseFromData:error:]
+ -[HAPWiFiMetrics rssi]
+ -[HAPWiFiMetrics rxPacketCount]
+ -[HAPWiFiMetrics rxPacketErrorCount]
+ -[HAPWiFiMetrics serializeWithError:]
+ -[HAPWiFiMetrics setBeaconLostCount:]
+ -[HAPWiFiMetrics setBeaconRxCount:]
+ -[HAPWiFiMetrics setBeaconRxInterval:]
+ -[HAPWiFiMetrics setBssid:]
+ -[HAPWiFiMetrics setChannelNumber:]
+ -[HAPWiFiMetrics setConnectionStatus:]
+ -[HAPWiFiMetrics setDisconnectionCount:]
+ -[HAPWiFiMetrics setDisconnectionDuration:]
+ -[HAPWiFiMetrics setGatewayIPv4Address:]
+ -[HAPWiFiMetrics setGatewayIPv6Address:]
+ -[HAPWiFiMetrics setGatewayMacAddress:]
+ -[HAPWiFiMetrics setHwExceptionCount:]
+ -[HAPWiFiMetrics setIpAddressList:]
+ -[HAPWiFiMetrics setPacketMulticastRxCount:]
+ -[HAPWiFiMetrics setPacketMulticastRxErrorCount:]
+ -[HAPWiFiMetrics setPacketMulticastTxCount:]
+ -[HAPWiFiMetrics setPacketMulticastTxErrorCount:]
+ -[HAPWiFiMetrics setPacketUnicastRxCount:]
+ -[HAPWiFiMetrics setPacketUnicastRxErrorCount:]
+ -[HAPWiFiMetrics setPacketUnicastTxCount:]
+ -[HAPWiFiMetrics setPacketUnicastTxErrorCount:]
+ -[HAPWiFiMetrics setRssi:]
+ -[HAPWiFiMetrics setRxPacketCount:]
+ -[HAPWiFiMetrics setRxPacketErrorCount:]
+ -[HAPWiFiMetrics setSubnetMask:]
+ -[HAPWiFiMetrics setTxPacketCount:]
+ -[HAPWiFiMetrics setTxPacketErrorCount:]
+ -[HAPWiFiMetrics setWifiRestartCount:]
+ -[HAPWiFiMetrics setWifiVersion:]
+ -[HAPWiFiMetrics subnetMask]
+ -[HAPWiFiMetrics txPacketCount]
+ -[HAPWiFiMetrics txPacketErrorCount]
+ -[HAPWiFiMetrics wifiRestartCount]
+ -[HAPWiFiMetrics wifiVersion]
+ -[NSError(HAPError) containsHAPPortUnreachableError]
+ -[_HAPAccessoryServerBTLE200 _ecdsaKeyPairSetupRefusalError]
+ GCC_except_table10066
+ GCC_except_table10068
+ GCC_except_table10070
+ GCC_except_table10073
+ GCC_except_table10075
+ GCC_except_table10077
+ GCC_except_table10079
+ GCC_except_table10080
+ GCC_except_table10087
+ GCC_except_table10089
+ GCC_except_table10090
+ GCC_except_table1012
+ GCC_except_table1017
+ GCC_except_table1164
+ GCC_except_table1166
+ GCC_except_table1233
+ GCC_except_table1235
+ GCC_except_table1237
+ GCC_except_table1239
+ GCC_except_table1779
+ GCC_except_table1784
+ GCC_except_table18
+ GCC_except_table1802
+ GCC_except_table1816
+ GCC_except_table1818
+ GCC_except_table1820
+ GCC_except_table1822
+ GCC_except_table1952
+ GCC_except_table1958
+ GCC_except_table1960
+ GCC_except_table2162
+ GCC_except_table232
+ GCC_except_table233
+ GCC_except_table236
+ GCC_except_table2378
+ GCC_except_table2380
+ GCC_except_table2385
+ GCC_except_table2391
+ GCC_except_table2393
+ GCC_except_table2399
+ GCC_except_table2401
+ GCC_except_table2405
+ GCC_except_table2413
+ GCC_except_table2417
+ GCC_except_table2423
+ GCC_except_table2425
+ GCC_except_table2427
+ GCC_except_table2429
+ GCC_except_table2435
+ GCC_except_table2439
+ GCC_except_table2447
+ GCC_except_table2449
+ GCC_except_table2462
+ GCC_except_table2470
+ GCC_except_table2477
+ GCC_except_table2527
+ GCC_except_table255
+ GCC_except_table256
+ GCC_except_table258
+ GCC_except_table261
+ GCC_except_table2646
+ GCC_except_table2651
+ GCC_except_table2652
+ GCC_except_table2654
+ GCC_except_table2656
+ GCC_except_table2673
+ GCC_except_table2677
+ GCC_except_table268
+ GCC_except_table2680
+ GCC_except_table2682
+ GCC_except_table270
+ GCC_except_table2714
+ GCC_except_table2716
+ GCC_except_table272
+ GCC_except_table2723
+ GCC_except_table2728
+ GCC_except_table2731
+ GCC_except_table2734
+ GCC_except_table2738
+ GCC_except_table2740
+ GCC_except_table2743
+ GCC_except_table2748
+ GCC_except_table2750
+ GCC_except_table2752
+ GCC_except_table2756
+ GCC_except_table276
+ GCC_except_table2762
+ GCC_except_table2770
+ GCC_except_table2783
+ GCC_except_table280
+ GCC_except_table2826
+ GCC_except_table2827
+ GCC_except_table2828
+ GCC_except_table2830
+ GCC_except_table2831
+ GCC_except_table2832
+ GCC_except_table2834
+ GCC_except_table2838
+ GCC_except_table2839
+ GCC_except_table2865
+ GCC_except_table2869
+ GCC_except_table2873
+ GCC_except_table289
+ GCC_except_table295
+ GCC_except_table299
+ GCC_except_table301
+ GCC_except_table3075
+ GCC_except_table3083
+ GCC_except_table3084
+ GCC_except_table3085
+ GCC_except_table3086
+ GCC_except_table3087
+ GCC_except_table3088
+ GCC_except_table3104
+ GCC_except_table3210
+ GCC_except_table3414
+ GCC_except_table3423
+ GCC_except_table3441
+ GCC_except_table3475
+ GCC_except_table3491
+ GCC_except_table3493
+ GCC_except_table3505
+ GCC_except_table3512
+ GCC_except_table3534
+ GCC_except_table3548
+ GCC_except_table3549
+ GCC_except_table3550
+ GCC_except_table3553
+ GCC_except_table3562
+ GCC_except_table3569
+ GCC_except_table3572
+ GCC_except_table3577
+ GCC_except_table3582
+ GCC_except_table3587
+ GCC_except_table3628
+ GCC_except_table3645
+ GCC_except_table3648
+ GCC_except_table3653
+ GCC_except_table3655
+ GCC_except_table3687
+ GCC_except_table3689
+ GCC_except_table3693
+ GCC_except_table3709
+ GCC_except_table3773
+ GCC_except_table3780
+ GCC_except_table3782
+ GCC_except_table3783
+ GCC_except_table3806
+ GCC_except_table3826
+ GCC_except_table4054
+ GCC_except_table41
+ GCC_except_table4129
+ GCC_except_table4136
+ GCC_except_table4140
+ GCC_except_table4144
+ GCC_except_table4146
+ GCC_except_table4150
+ GCC_except_table4153
+ GCC_except_table4159
+ GCC_except_table4170
+ GCC_except_table4172
+ GCC_except_table4173
+ GCC_except_table4175
+ GCC_except_table4178
+ GCC_except_table4180
+ GCC_except_table4181
+ GCC_except_table4185
+ GCC_except_table4186
+ GCC_except_table4188
+ GCC_except_table4205
+ GCC_except_table4208
+ GCC_except_table4219
+ GCC_except_table4220
+ GCC_except_table4222
+ GCC_except_table4227
+ GCC_except_table4233
+ GCC_except_table4236
+ GCC_except_table4239
+ GCC_except_table4251
+ GCC_except_table4265
+ GCC_except_table4302
+ GCC_except_table4325
+ GCC_except_table4331
+ GCC_except_table4335
+ GCC_except_table4339
+ GCC_except_table4341
+ GCC_except_table4344
+ GCC_except_table4346
+ GCC_except_table4348
+ GCC_except_table4355
+ GCC_except_table4356
+ GCC_except_table4357
+ GCC_except_table4358
+ GCC_except_table4359
+ GCC_except_table4361
+ GCC_except_table4362
+ GCC_except_table4363
+ GCC_except_table4364
+ GCC_except_table4446
+ GCC_except_table4447
+ GCC_except_table4448
+ GCC_except_table4449
+ GCC_except_table4450
+ GCC_except_table4451
+ GCC_except_table4452
+ GCC_except_table4453
+ GCC_except_table4454
+ GCC_except_table4455
+ GCC_except_table4456
+ GCC_except_table4457
+ GCC_except_table4458
+ GCC_except_table4459
+ GCC_except_table4460
+ GCC_except_table4513
+ GCC_except_table4599
+ GCC_except_table4601
+ GCC_except_table4603
+ GCC_except_table4649
+ GCC_except_table4670
+ GCC_except_table4678
+ GCC_except_table4689
+ GCC_except_table4703
+ GCC_except_table4706
+ GCC_except_table4711
+ GCC_except_table4719
+ GCC_except_table4725
+ GCC_except_table4727
+ GCC_except_table4729
+ GCC_except_table4740
+ GCC_except_table4773
+ GCC_except_table4776
+ GCC_except_table4777
+ GCC_except_table4783
+ GCC_except_table4785
+ GCC_except_table4791
+ GCC_except_table4792
+ GCC_except_table4797
+ GCC_except_table4798
+ GCC_except_table4804
+ GCC_except_table4813
+ GCC_except_table4815
+ GCC_except_table4818
+ GCC_except_table4819
+ GCC_except_table4824
+ GCC_except_table4827
+ GCC_except_table4828
+ GCC_except_table4834
+ GCC_except_table4841
+ GCC_except_table4845
+ GCC_except_table4846
+ GCC_except_table4860
+ GCC_except_table4876
+ GCC_except_table4893
+ GCC_except_table4894
+ GCC_except_table4896
+ GCC_except_table4897
+ GCC_except_table4900
+ GCC_except_table4901
+ GCC_except_table4916
+ GCC_except_table4931
+ GCC_except_table4938
+ GCC_except_table4958
+ GCC_except_table4968
+ GCC_except_table4970
+ GCC_except_table5036
+ GCC_except_table5040
+ GCC_except_table5041
+ GCC_except_table5043
+ GCC_except_table5045
+ GCC_except_table5048
+ GCC_except_table5051
+ GCC_except_table5054
+ GCC_except_table5057
+ GCC_except_table5060
+ GCC_except_table5063
+ GCC_except_table5066
+ GCC_except_table5069
+ GCC_except_table5074
+ GCC_except_table5087
+ GCC_except_table5092
+ GCC_except_table5096
+ GCC_except_table5098
+ GCC_except_table5101
+ GCC_except_table5113
+ GCC_except_table5121
+ GCC_except_table5128
+ GCC_except_table5134
+ GCC_except_table5135
+ GCC_except_table5138
+ GCC_except_table5139
+ GCC_except_table5157
+ GCC_except_table5159
+ GCC_except_table5161
+ GCC_except_table5162
+ GCC_except_table5165
+ GCC_except_table5171
+ GCC_except_table5174
+ GCC_except_table5176
+ GCC_except_table5183
+ GCC_except_table5185
+ GCC_except_table5187
+ GCC_except_table5190
+ GCC_except_table5201
+ GCC_except_table5212
+ GCC_except_table5214
+ GCC_except_table5225
+ GCC_except_table5227
+ GCC_except_table5229
+ GCC_except_table5235
+ GCC_except_table5517
+ GCC_except_table5523
+ GCC_except_table5540
+ GCC_except_table5544
+ GCC_except_table5562
+ GCC_except_table5568
+ GCC_except_table5582
+ GCC_except_table5596
+ GCC_except_table5600
+ GCC_except_table571
+ GCC_except_table5744
+ GCC_except_table582
+ GCC_except_table598
+ GCC_except_table610
+ GCC_except_table6202
+ GCC_except_table6211
+ GCC_except_table6212
+ GCC_except_table6225
+ GCC_except_table6267
+ GCC_except_table6270
+ GCC_except_table6271
+ GCC_except_table6272
+ GCC_except_table6273
+ GCC_except_table6372
+ GCC_except_table6373
+ GCC_except_table6374
+ GCC_except_table6375
+ GCC_except_table6376
+ GCC_except_table6377
+ GCC_except_table6378
+ GCC_except_table6379
+ GCC_except_table6381
+ GCC_except_table6402
+ GCC_except_table6413
+ GCC_except_table6415
+ GCC_except_table6420
+ GCC_except_table6423
+ GCC_except_table6426
+ GCC_except_table6430
+ GCC_except_table6434
+ GCC_except_table644
+ GCC_except_table656
+ GCC_except_table659
+ GCC_except_table662
+ GCC_except_table665
+ GCC_except_table679
+ GCC_except_table683
+ GCC_except_table687
+ GCC_except_table694
+ GCC_except_table697
+ GCC_except_table6985
+ GCC_except_table6986
+ GCC_except_table7005
+ GCC_except_table7015
+ GCC_except_table7018
+ GCC_except_table7023
+ GCC_except_table7026
+ GCC_except_table7031
+ GCC_except_table7300
+ GCC_except_table7304
+ GCC_except_table731
+ GCC_except_table7364
+ GCC_except_table7368
+ GCC_except_table7370
+ GCC_except_table7372
+ GCC_except_table741
+ GCC_except_table749
+ GCC_except_table7587
+ GCC_except_table7595
+ GCC_except_table7597
+ GCC_except_table7607
+ GCC_except_table7620
+ GCC_except_table7638
+ GCC_except_table7644
+ GCC_except_table7658
+ GCC_except_table7664
+ GCC_except_table7669
+ GCC_except_table7671
+ GCC_except_table776
+ GCC_except_table7782
+ GCC_except_table7783
+ GCC_except_table7785
+ GCC_except_table7792
+ GCC_except_table780
+ GCC_except_table783
+ GCC_except_table7844
+ GCC_except_table7845
+ GCC_except_table7846
+ GCC_except_table785
+ GCC_except_table7866
+ GCC_except_table7878
+ GCC_except_table7881
+ GCC_except_table7886
+ GCC_except_table7888
+ GCC_except_table7902
+ GCC_except_table797
+ GCC_except_table799
+ GCC_except_table8137
+ GCC_except_table8150
+ GCC_except_table8155
+ GCC_except_table8158
+ GCC_except_table8159
+ GCC_except_table8161
+ GCC_except_table8162
+ GCC_except_table8164
+ GCC_except_table818
+ GCC_except_table8194
+ GCC_except_table8218
+ GCC_except_table8222
+ GCC_except_table8226
+ GCC_except_table8231
+ GCC_except_table8235
+ GCC_except_table8239
+ GCC_except_table824
+ GCC_except_table8243
+ GCC_except_table8247
+ GCC_except_table8255
+ GCC_except_table8257
+ GCC_except_table8261
+ GCC_except_table828
+ GCC_except_table8325
+ GCC_except_table8326
+ GCC_except_table8327
+ GCC_except_table8328
+ GCC_except_table8329
+ GCC_except_table8330
+ GCC_except_table8331
+ GCC_except_table839
+ GCC_except_table8396
+ GCC_except_table8409
+ GCC_except_table8410
+ GCC_except_table8415
+ GCC_except_table8416
+ GCC_except_table8423
+ GCC_except_table8435
+ GCC_except_table8441
+ GCC_except_table8450
+ GCC_except_table8470
+ GCC_except_table8474
+ GCC_except_table8479
+ GCC_except_table848
+ GCC_except_table8482
+ GCC_except_table8489
+ GCC_except_table8492
+ GCC_except_table8506
+ GCC_except_table851
+ GCC_except_table8513
+ GCC_except_table8519
+ GCC_except_table8528
+ GCC_except_table8530
+ GCC_except_table8536
+ GCC_except_table8537
+ GCC_except_table8544
+ GCC_except_table856
+ GCC_except_table8568
+ GCC_except_table8574
+ GCC_except_table8578
+ GCC_except_table8579
+ GCC_except_table8582
+ GCC_except_table8588
+ GCC_except_table8592
+ GCC_except_table8596
+ GCC_except_table8598
+ GCC_except_table860
+ GCC_except_table8600
+ GCC_except_table8604
+ GCC_except_table866
+ GCC_except_table870
+ GCC_except_table8723
+ GCC_except_table8818
+ GCC_except_table8821
+ GCC_except_table8828
+ GCC_except_table8834
+ GCC_except_table8841
+ GCC_except_table8842
+ GCC_except_table8859
+ GCC_except_table8863
+ GCC_except_table8864
+ GCC_except_table8865
+ GCC_except_table8914
+ GCC_except_table8915
+ GCC_except_table8917
+ GCC_except_table8920
+ GCC_except_table8947
+ GCC_except_table8948
+ GCC_except_table8953
+ GCC_except_table8973
+ GCC_except_table899
+ GCC_except_table8991
+ GCC_except_table8992
+ GCC_except_table8993
+ GCC_except_table8998
+ GCC_except_table8999
+ GCC_except_table9001
+ GCC_except_table9003
+ GCC_except_table9004
+ GCC_except_table9006
+ GCC_except_table9007
+ GCC_except_table9011
+ GCC_except_table9012
+ GCC_except_table9014
+ GCC_except_table9024
+ GCC_except_table9026
+ GCC_except_table9031
+ GCC_except_table9036
+ GCC_except_table9037
+ GCC_except_table9038
+ GCC_except_table9054
+ GCC_except_table9056
+ GCC_except_table906
+ GCC_except_table9063
+ GCC_except_table9070
+ GCC_except_table9075
+ GCC_except_table9081
+ GCC_except_table9093
+ GCC_except_table9094
+ GCC_except_table9099
+ GCC_except_table9109
+ GCC_except_table9116
+ GCC_except_table9117
+ GCC_except_table9121
+ GCC_except_table9123
+ GCC_except_table9125
+ GCC_except_table9129
+ GCC_except_table914
+ GCC_except_table915
+ GCC_except_table9150
+ GCC_except_table9152
+ GCC_except_table9153
+ GCC_except_table9179
+ GCC_except_table931
+ GCC_except_table9344
+ GCC_except_table9407
+ GCC_except_table9439
+ GCC_except_table9442
+ GCC_except_table95
+ GCC_except_table953
+ GCC_except_table9609
+ GCC_except_table9647
+ GCC_except_table9684
+ GCC_except_table972
+ GCC_except_table9762
+ GCC_except_table9764
+ GCC_except_table9766
+ GCC_except_table9768
+ GCC_except_table9770
+ GCC_except_table9772
+ GCC_except_table9774
+ GCC_except_table9780
+ GCC_except_table9782
+ GCC_except_table9785
+ GCC_except_table9787
+ GCC_except_table9789
+ GCC_except_table9798
+ GCC_except_table9804
+ GCC_except_table9809
+ GCC_except_table9812
+ GCC_except_table9817
+ GCC_except_table9822
+ GCC_except_table9825
+ GCC_except_table9828
+ GCC_except_table9854
+ GCC_except_table9857
+ GCC_except_table9858
+ GCC_except_table9877
+ GCC_except_table9878
+ GCC_except_table9879
+ GCC_except_table9881
+ GCC_except_table9882
+ GCC_except_table9884
+ GCC_except_table9885
+ GCC_except_table9886
+ GCC_except_table9888
+ GCC_except_table9889
+ GCC_except_table9891
+ GCC_except_table9895
+ GCC_except_table9896
+ GCC_except_table9900
+ GCC_except_table994
+ GCC_except_table9951
+ GCC_except_table9958
+ GCC_except_table998
+ OBJC_IVAR_$_HAP2AccessoryAddressLists._cachedPrimary
+ OBJC_IVAR_$_HAP2AccessoryAddressLists._cachedSecondary
+ OBJC_IVAR_$_HAP2AccessoryAddressLists._primary
+ OBJC_IVAR_$_HAP2AccessoryAddressLists._secondary
+ OBJC_IVAR_$_HAP2AccessoryAddressResolverPipeline._cancelled
+ OBJC_IVAR_$_HAP2AccessoryAddressResolverPipeline._errorHandler
+ OBJC_IVAR_$_HAP2AccessoryAddressResolverPipeline._gai
+ OBJC_IVAR_$_HAP2AccessoryAddressResolverPipeline._queue
+ OBJC_IVAR_$_HAP2AccessoryAddressResolverPipeline._resolvedHostname
+ OBJC_IVAR_$_HAP2AccessoryAddressResolverPipeline._resolvedPort
+ OBJC_IVAR_$_HAP2AccessoryAddressResolverPipeline._retainedContext
+ OBJC_IVAR_$_HAP2AccessoryAddressResolverPipeline._serviceRef
+ OBJC_IVAR_$_HAP2AccessoryAddressResolverPipeline._updateHandler
+ OBJC_IVAR_$_HAP2AccessoryAddressResolverPipeline._workingSet
+ OBJC_IVAR_$_HAP2AccessoryAddressResolverPipeline._workingSetCounts
+ OBJC_IVAR_$_HAP2AccessoryDNSResolver._addresses
+ OBJC_IVAR_$_HAP2AccessoryDNSResolver._becameEmptyAt
+ OBJC_IVAR_$_HAP2AccessoryDNSResolver._cacheSubscriber
+ OBJC_IVAR_$_HAP2AccessoryDNSResolver._cachedPrimaryIP
+ OBJC_IVAR_$_HAP2AccessoryDNSResolver._cachedSecondaryIP
+ OBJC_IVAR_$_HAP2AccessoryDNSResolver._delegates
+ OBJC_IVAR_$_HAP2AccessoryDNSResolver._deviceID
+ OBJC_IVAR_$_HAP2AccessoryDNSResolver._immediateRetrySpent
+ OBJC_IVAR_$_HAP2AccessoryDNSResolver._managerQueue
+ OBJC_IVAR_$_HAP2AccessoryDNSResolver._pipelineCancel
+ OBJC_IVAR_$_HAP2AccessoryDNSResolver._pipelineFactory
+ OBJC_IVAR_$_HAP2AccessoryDNSResolver._pipelineStarted
+ OBJC_IVAR_$_HAP2AccessoryDNSResolver._pipelineTornDown
+ OBJC_IVAR_$_HAP2AccessoryDNSResolver._propertyLock
+ OBJC_IVAR_$_HAP2AccessoryDNSResolver._serviceName
+ OBJC_IVAR_$_HAP2AccessoryDeviceIPAddress._transportType
+ OBJC_IVAR_$_HAP2AccessoryServer._consecutiveProbeFailures
+ OBJC_IVAR_$_HAP2AccessoryServer._dnsResolver
+ OBJC_IVAR_$_HAP2AccessoryServer._hasSeededSinceResolverAttach
+ OBJC_IVAR_$_HAP2AccessoryServer._hasThreadAdvertisement
+ OBJC_IVAR_$_HAP2AccessoryServer._hasWiFiAdvertisement
+ OBJC_IVAR_$_HAP2AccessoryServer._keepAliveListener
+ OBJC_IVAR_$_HAP2AccessoryServer._lastObservedHasAdvertisement
+ OBJC_IVAR_$_HAP2AccessoryServerBrowser._auditScheduler
+ OBJC_IVAR_$_HAP2AccessoryServerBrowser._existingPTRs
+ OBJC_IVAR_$_HAP2AccessoryServerBrowser._ipCache
+ OBJC_IVAR_$_HAP2AccessoryServerBrowser._isInitialCacheRestored
+ OBJC_IVAR_$_HAP2AccessoryServerBrowser._pendingRevalidationPTRs
+ OBJC_IVAR_$_HAP2AccessoryServerBrowser._resolverRegistry
+ OBJC_IVAR_$_HAP2AccessoryServerBrowser._revalidationTimer
+ OBJC_IVAR_$_HAP2AccessoryServerController._lastAnnouncedSessionNumber
+ OBJC_IVAR_$_HAP2AccessoryServerController._unitTest_useHH2
+ OBJC_IVAR_$_HAP2AccessoryServerControllerOperation._coapMessageID
+ OBJC_IVAR_$_HAP2AccessoryServerDiscoveryBonjour._lastKnownAccessoryInfoByServiceKey
+ OBJC_IVAR_$_HAP2AccessoryServerIPCacheData._cachedPrimaryData
+ OBJC_IVAR_$_HAP2AccessoryServerIPCacheData._cachedSecondaryData
+ OBJC_IVAR_$_HAP2AccessoryServerIPCacheData._configurationInfo
+ OBJC_IVAR_$_HAP2AccessoryServerIPCacheData._deviceID
+ OBJC_IVAR_$_HAP2AccessoryServerSecureTransportPairVerify._stateChangeGeneration
+ OBJC_IVAR_$_HAP2AccessoryServerTransportBase._supportsKeepAlive
+ OBJC_IVAR_$_HAP2AccessoryServerTransportBase._supportsThreadTransport
+ OBJC_IVAR_$_HAP2AccessoryServerTransportBase._supportsWiFiTransport
+ OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._activeMessageID
+ OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._addressResolverFactory
+ OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._failoverTimer
+ OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._hasJustCompletedInitialResolve
+ OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._hasPublishedAdvertisementState
+ OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._hasRegisteredEndpoint
+ OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._helloRetryCount
+ OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._helloRetryTimer
+ OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._inFlightRacingLogEvent
+ OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._initialCacheGracePeriodTimer
+ OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._initialConnectionAttemptStartedAt
+ OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._initialResolveCompleted
+ OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._lastCompletedMessageID
+ OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._lastMessageID
+ OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._lastPublishedHasThreadAdvertisement
+ OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._lastPublishedHasWiFiAdvertisement
+ OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._pendingEndpointRegistration
+ OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._pendingIPRefresh
+ OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._primaryEffectiveListIsCacheOnly
+ OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._primaryIPsTriedThisSession
+ OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._primaryOpenInFlight
+ OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._resolveTimeoutTimer
+ OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._resolverCancelBlock
+ OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._resolverRestartTimer
+ OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._secondaryAddressList
+ OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._secondaryCoAPClient
+ OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._secondaryIPsTriedThisSession
+ OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._secondaryOpenInFlight
+ OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._securedClient
+ OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._sendRequestQoS
+ OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._triedIPsLock
+ OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._tryingInitialCacheOnly
+ OBJC_IVAR_$_HAP2BrowserResolverRegistry._browser
+ OBJC_IVAR_$_HAP2BrowserResolverRegistry._managerQueue
+ OBJC_IVAR_$_HAP2BrowserResolverRegistry._name
+ OBJC_IVAR_$_HAP2BrowserResolverRegistry._pipelineFactory
+ OBJC_IVAR_$_HAP2BrowserResolverRegistry._propertyLock
+ OBJC_IVAR_$_HAP2BrowserResolverRegistry._resolversByDeviceID
+ OBJC_IVAR_$_HAP2CoAPClient._pendingProbeCompletion
+ OBJC_IVAR_$_HAP2CoAPClient._pendingProbeMessageID
+ OBJC_IVAR_$_HAP2SessionKeepAliveConfigurationEntry._maximumInterval
+ OBJC_IVAR_$_HAP2SessionKeepAliveConfigurationEntry._minimumInterval
+ OBJC_IVAR_$_HAP2SessionKeepAliveConfigurationEntry._transportType
+ OBJC_IVAR_$_HAP2SessionKeepAliveListener._dateProvider
+ OBJC_IVAR_$_HAP2SessionKeepAliveListener._delegateLock
+ OBJC_IVAR_$_HAP2SessionKeepAliveListener._delegates
+ OBJC_IVAR_$_HAP2SessionKeepAliveListener._isRunning
+ OBJC_IVAR_$_HAP2SessionKeepAliveListener._missCheckTimer
+ OBJC_IVAR_$_HAP2SessionKeepAliveListener._timerProvider
+ OBJC_IVAR_$_HAP2SessionKeepAliveListener._transportStates
+ OBJC_IVAR_$_HAP2SessionKeepAliveListener._workQueue
+ OBJC_IVAR_$_HAP2SessionKeepAliveTransportState._hasMissedHeartbeat
+ OBJC_IVAR_$_HAP2SessionKeepAliveTransportState._lastHeartbeatTime
+ OBJC_IVAR_$_HAP2SessionKeepAliveTransportState._maximumInterval
+ OBJC_IVAR_$_HAP2SessionKeepAliveTransportState._transportType
+ OBJC_IVAR_$_HAPAVCStreamingControlCommandWrapper._value
+ OBJC_IVAR_$_HAPAVCStreamingControlRequest._command
+ OBJC_IVAR_$_HAPAVCStreamingControlRequest._sessionIdentifier
+ OBJC_IVAR_$_HAPAVCStreamingControlResponse._sessionIdentifier
+ OBJC_IVAR_$_HAPAVCStreamingControlResponse._status
+ OBJC_IVAR_$_HAPAVCStreamingControlStatusWrapper._value
+ OBJC_IVAR_$_HAPAVCViewerRegistrationOperationWrapper._value
+ OBJC_IVAR_$_HAPAVCViewerRegistrationRequest._operation
+ OBJC_IVAR_$_HAPAccessoryPairingRequest._shouldAllowECDSAKeyPairSetup
+ OBJC_IVAR_$_HAPAccessoryServer._hasThreadAdvertisement
+ OBJC_IVAR_$_HAPAccessoryServer._hasWiFiAdvertisement
+ OBJC_IVAR_$_HAPAccessoryServer._lastPairSetupWasSpake2
+ OBJC_IVAR_$_HAPAccessoryServer._pairSetupLastError
+ OBJC_IVAR_$_HAPAccessoryServer._pairSetupM1ToM4Completed
+ OBJC_IVAR_$_HAPAccessoryServer._pairSetupM1ToM4DurationMS
+ OBJC_IVAR_$_HAPAccessoryServer._pairSetupM1ToM4Error
+ OBJC_IVAR_$_HAPAccessoryServer._pairSetupM5ToM6Completed
+ OBJC_IVAR_$_HAPAccessoryServer._pairSetupM5ToM6DurationMS
+ OBJC_IVAR_$_HAPAccessoryServer._pairSetupM5ToM6Error
+ OBJC_IVAR_$_HAPAccessoryServer._pairSetupWorkDurationMS
+ OBJC_IVAR_$_HAPAccessoryServer._tokenAuthCompleted
+ OBJC_IVAR_$_HAPAccessoryServer._tokenAuthDurationMS
+ OBJC_IVAR_$_HAPAccessoryServer._tokenAuthError
+ OBJC_IVAR_$_HAPAccessoryServer._workQueueFactory
+ OBJC_IVAR_$_HAPBluetoothMetrics._bluetoothVersion
+ OBJC_IVAR_$_HAPBluetoothMetrics._connectionCount
+ OBJC_IVAR_$_HAPBluetoothMetrics._connectionErrorCount
+ OBJC_IVAR_$_HAPBluetoothMetrics._connectionStatus
+ OBJC_IVAR_$_HAPBluetoothMetrics._disconnectionCount
+ OBJC_IVAR_$_HAPBluetoothMetrics._disconnectionErrorCount
+ OBJC_IVAR_$_HAPBluetoothMetrics._hwExceptionCount
+ OBJC_IVAR_$_HAPBluetoothMetrics._overrunCount
+ OBJC_IVAR_$_HAPBluetoothMetrics._packetRxCount
+ OBJC_IVAR_$_HAPBluetoothMetrics._packetRxErrorCount
+ OBJC_IVAR_$_HAPBluetoothMetrics._packetTxCount
+ OBJC_IVAR_$_HAPBluetoothMetrics._packetTxErrorCount
+ OBJC_IVAR_$_HAPBluetoothMetrics._rssi
+ OBJC_IVAR_$_HAPBluetoothMetrics._txPowerLevel
+ OBJC_IVAR_$_HAPBootReasonsMetrics._brownOutResetBootCount
+ OBJC_IVAR_$_HAPBootReasonsMetrics._connectivityMonitorBootCount
+ OBJC_IVAR_$_HAPBootReasonsMetrics._hardwareFaultBootCount
+ OBJC_IVAR_$_HAPBootReasonsMetrics._hardwareWatchdogResetBootCount
+ OBJC_IVAR_$_HAPBootReasonsMetrics._heapOverflowBootCount
+ OBJC_IVAR_$_HAPBootReasonsMetrics._powerOnBootCount
+ OBJC_IVAR_$_HAPBootReasonsMetrics._softwareExceptionBootCount
+ OBJC_IVAR_$_HAPBootReasonsMetrics._softwareResetBootCount
+ OBJC_IVAR_$_HAPBootReasonsMetrics._softwareUpdateCompletedBootCount
+ OBJC_IVAR_$_HAPBootReasonsMetrics._softwareWatchdogResetBootCount
+ OBJC_IVAR_$_HAPBootReasonsMetrics._stackOverflowBootCount
+ OBJC_IVAR_$_HAPBootReasonsMetrics._temperatureLimitBootCount
+ OBJC_IVAR_$_HAPBootReasonsMetrics._unspecifiedBootCount
+ OBJC_IVAR_$_HAPCHMMetrics._chmAccessoryRebootCompleted
+ OBJC_IVAR_$_HAPCHMMetrics._chmAccessoryRebootDurationToRecovery
+ OBJC_IVAR_$_HAPCHMMetrics._hapSessionLossCount
+ OBJC_IVAR_$_HAPCHMMetrics._threadFirstRestartCompleted
+ OBJC_IVAR_$_HAPCHMMetrics._threadFirstRestartConnectivityState
+ OBJC_IVAR_$_HAPCHMMetrics._threadFirstRestartRecoveryTime
+ OBJC_IVAR_$_HAPCHMMetrics._threadRecoveryAttemptCount
+ OBJC_IVAR_$_HAPCHMMetrics._threadRestartCount
+ OBJC_IVAR_$_HAPCHMMetrics._threadTransportLossCount
+ OBJC_IVAR_$_HAPCHMMetrics._wifiFirstRestartCompleted
+ OBJC_IVAR_$_HAPCHMMetrics._wifiFirstRestartConnectivityState
+ OBJC_IVAR_$_HAPCHMMetrics._wifiFirstRestartRecoveryTime
+ OBJC_IVAR_$_HAPCHMMetrics._wifiRecoveryAttemptCount
+ OBJC_IVAR_$_HAPCHMMetrics._wifiRestartCount
+ OBJC_IVAR_$_HAPCHMMetrics._wifiTransportLossCount
+ OBJC_IVAR_$_HAPCharacteristicResponseTuple._coapMessageID
+ OBJC_IVAR_$_HAPConnectionHealthMonitor._deviceRebootDelay
+ OBJC_IVAR_$_HAPConnectionHealthMonitor._deviceRebootEnable
+ OBJC_IVAR_$_HAPConnectionHealthMonitor._recoveryStaggerDelay
+ OBJC_IVAR_$_HAPConnectionHealthMonitor._threadPingTestCount
+ OBJC_IVAR_$_HAPConnectionHealthMonitor._threadPingTestInterval
+ OBJC_IVAR_$_HAPConnectionHealthMonitor._threadRecoveryConfiguration
+ OBJC_IVAR_$_HAPConnectionHealthMonitor._threadRestartMinInterval
+ OBJC_IVAR_$_HAPConnectionHealthMonitor._wiFiPingTestCount
+ OBJC_IVAR_$_HAPConnectionHealthMonitor._wiFiPingTestInterval
+ OBJC_IVAR_$_HAPConnectionHealthMonitor._wiFiRecoveryConfiguration
+ OBJC_IVAR_$_HAPConnectionHealthMonitor._wiFiRestartMinInterval
+ OBJC_IVAR_$_HAPContributingSensor._sensorUUID
+ OBJC_IVAR_$_HAPErrorCountersMetrics._entries
+ OBJC_IVAR_$_HAPErrorCountersMetricsEntry._count
+ OBJC_IVAR_$_HAPErrorCountersMetricsEntry._errorID
+ OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._abandonedRequestCount
+ OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._audioOnlyFailureCount
+ OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._authenticationErrorCount
+ OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._fragmentFailureCount
+ OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._fragmentRetriedCount
+ OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._fragmentSuccessCount
+ OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._latencyCount1000ms
+ OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._latencyCount2000ms
+ OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._latencyCount250ms
+ OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._latencyCount3750ms
+ OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._latencyCount500ms
+ OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._latencyCountOver3750ms
+ OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._localErrorCount
+ OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._networkErrorCount
+ OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._partialSuccessCount
+ OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._playlistFailureCount
+ OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._serverReturnedErrorCount
+ OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._sessionFailureCount
+ OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._sessionSuccessCount
+ OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._uploadWithoutResidentResponseCount
+ OBJC_IVAR_$_HAPKeyBag._cachedAccessoryKeyType
+ OBJC_IVAR_$_HAPMetricEventBluetoothVersionTypeWrapper._value
+ OBJC_IVAR_$_HAPMetricEventPowerSourcesBitmaskWrapper._value
+ OBJC_IVAR_$_HAPMetricEventPowerSourcesEnumWrapper._value
+ OBJC_IVAR_$_HAPMetricEventThreadFirstRestartConnectivityStateWrapper._value
+ OBJC_IVAR_$_HAPMetricEventWiFiFirstRestartConnectivityStateWrapper._value
+ OBJC_IVAR_$_HAPMetricEventWiFiVersionTypeWrapper._value
+ OBJC_IVAR_$_HAPPowerMetrics._batteryPercentage
+ OBJC_IVAR_$_HAPPowerMetrics._currentPowerSource
+ OBJC_IVAR_$_HAPPowerMetrics._durationOnBatteryPower
+ OBJC_IVAR_$_HAPPowerMetrics._durationRemainingOnBatteryPower
+ OBJC_IVAR_$_HAPPowerMetrics._supportedPowerSources
+ OBJC_IVAR_$_HAPSaturationMetrics._averageCPUUtilization
+ OBJC_IVAR_$_HAPSaturationMetrics._averageSystemMemoryUtilization
+ OBJC_IVAR_$_HAPSaturationMetrics._heapHighwaterCount
+ OBJC_IVAR_$_HAPSaturationMetrics._heapOverflowCount
+ OBJC_IVAR_$_HAPSaturationMetrics._lastHeapHighwaterTaskName
+ OBJC_IVAR_$_HAPSaturationMetrics._lastHeapOverflowTaskName
+ OBJC_IVAR_$_HAPSaturationMetrics._lastProcessCriticalMemoryName
+ OBJC_IVAR_$_HAPSaturationMetrics._lastStackHighwaterTaskName
+ OBJC_IVAR_$_HAPSaturationMetrics._lastStackOverflowTaskName
+ OBJC_IVAR_$_HAPSaturationMetrics._loadAverage
+ OBJC_IVAR_$_HAPSaturationMetrics._maxTaskReadyQueueSize
+ OBJC_IVAR_$_HAPSaturationMetrics._nonVolatileMemoryReadCount
+ OBJC_IVAR_$_HAPSaturationMetrics._nonVolatileMemoryReadErrorCount
+ OBJC_IVAR_$_HAPSaturationMetrics._nonVolatileMemoryUtilization
+ OBJC_IVAR_$_HAPSaturationMetrics._nonVolatileMemoryWriteCount
+ OBJC_IVAR_$_HAPSaturationMetrics._nonVolatileMemoryWriteErrorCount
+ OBJC_IVAR_$_HAPSaturationMetrics._peakCPUUtilization
+ OBJC_IVAR_$_HAPSaturationMetrics._peakSystemMemoryUtilization
+ OBJC_IVAR_$_HAPSaturationMetrics._processCriticalMemoryCount
+ OBJC_IVAR_$_HAPSaturationMetrics._stackHighwaterCount
+ OBJC_IVAR_$_HAPSaturationMetrics._stackOverflowCount
+ OBJC_IVAR_$_HAPSaturationMetrics._systemMemoryPressureCount
+ OBJC_IVAR_$_HAPSaturationMetrics._taskDeadlineMissCount
+ OBJC_IVAR_$_HAPSaturationMetrics._totalTasksScheduledCount
+ OBJC_IVAR_$_HAPSecuritySession._foreignPairVerifySession
+ OBJC_IVAR_$_HAPSensorList._contributingSensor
+ OBJC_IVAR_$_HAPSessionKeepAliveTransportTypeWrapper._value
+ OBJC_IVAR_$_HAPStabilityMetrics._activeHardwareFaults
+ OBJC_IVAR_$_HAPStabilityMetrics._expectedBootCount
+ OBJC_IVAR_$_HAPStabilityMetrics._lastBootReason
+ OBJC_IVAR_$_HAPStabilityMetrics._systemBootCount
+ OBJC_IVAR_$_HAPStabilityMetrics._systemCrashCount
+ OBJC_IVAR_$_HAPStabilityMetrics._systemHangCount
+ OBJC_IVAR_$_HAPStabilityMetrics._systemUptime
+ OBJC_IVAR_$_HAPStabilityMetricsBootReasonTypeWrapper._value
+ OBJC_IVAR_$_HAPStabilityMetricsHardwareFaultTypeWrapper._value
+ OBJC_IVAR_$_HAPTLVPreferredWiFiEntry._PSK
+ OBJC_IVAR_$_HAPTLVPreferredWiFiEntry._SSID
+ OBJC_IVAR_$_HAPTLVPreferredWiFiEntry._securityMode
+ OBJC_IVAR_$_HAPTLVPreferredWiFiList._preferredWiFiList
+ OBJC_IVAR_$_HAPTLVSelectedSessionKeepAliveConfigurationEntry._maximumInterval
+ OBJC_IVAR_$_HAPTLVSelectedSessionKeepAliveConfigurationEntry._minimumInterval
+ OBJC_IVAR_$_HAPTLVSelectedSessionKeepAliveConfigurationEntry._transportType
+ OBJC_IVAR_$_HAPTLVSelectedSessionKeepAliveConfigurationList._entries
+ OBJC_IVAR_$_HAPTLVSupportedSessionKeepAliveConfigurationEntry._maximumInterval
+ OBJC_IVAR_$_HAPTLVSupportedSessionKeepAliveConfigurationEntry._minimumInterval
+ OBJC_IVAR_$_HAPTLVSupportedSessionKeepAliveConfigurationEntry._minimumRange
+ OBJC_IVAR_$_HAPTLVSupportedSessionKeepAliveConfigurationEntry._transportType
+ OBJC_IVAR_$_HAPTLVSupportedSessionKeepAliveConfigurationList._entries
+ OBJC_IVAR_$_HAPThermalMetrics._averageDeviceTemperature
+ OBJC_IVAR_$_HAPThermalMetrics._maximumDeviceTemperature
+ OBJC_IVAR_$_HAPThermalMetrics._minimumDeviceTemperature
+ OBJC_IVAR_$_HAPThermalMetrics._temperatureLimitViolationCount
+ OBJC_IVAR_$_HAPThermalMetrics._temperatureLimitViolationDuration
+ OBJC_IVAR_$_HAPWebRTCOfferOptions._SFrameConfiguration
+ OBJC_IVAR_$_HAPWiFiMetrics._beaconLostCount
+ OBJC_IVAR_$_HAPWiFiMetrics._beaconRxCount
+ OBJC_IVAR_$_HAPWiFiMetrics._beaconRxInterval
+ OBJC_IVAR_$_HAPWiFiMetrics._bssid
+ OBJC_IVAR_$_HAPWiFiMetrics._channelNumber
+ OBJC_IVAR_$_HAPWiFiMetrics._connectionStatus
+ OBJC_IVAR_$_HAPWiFiMetrics._disconnectionCount
+ OBJC_IVAR_$_HAPWiFiMetrics._disconnectionDuration
+ OBJC_IVAR_$_HAPWiFiMetrics._gatewayIPv4Address
+ OBJC_IVAR_$_HAPWiFiMetrics._gatewayIPv6Address
+ OBJC_IVAR_$_HAPWiFiMetrics._gatewayMacAddress
+ OBJC_IVAR_$_HAPWiFiMetrics._hwExceptionCount
+ OBJC_IVAR_$_HAPWiFiMetrics._ipAddressList
+ OBJC_IVAR_$_HAPWiFiMetrics._packetMulticastRxCount
+ OBJC_IVAR_$_HAPWiFiMetrics._packetMulticastRxErrorCount
+ OBJC_IVAR_$_HAPWiFiMetrics._packetMulticastTxCount
+ OBJC_IVAR_$_HAPWiFiMetrics._packetMulticastTxErrorCount
+ OBJC_IVAR_$_HAPWiFiMetrics._packetUnicastRxCount
+ OBJC_IVAR_$_HAPWiFiMetrics._packetUnicastRxErrorCount
+ OBJC_IVAR_$_HAPWiFiMetrics._packetUnicastTxCount
+ OBJC_IVAR_$_HAPWiFiMetrics._packetUnicastTxErrorCount
+ OBJC_IVAR_$_HAPWiFiMetrics._rssi
+ OBJC_IVAR_$_HAPWiFiMetrics._rxPacketCount
+ OBJC_IVAR_$_HAPWiFiMetrics._rxPacketErrorCount
+ OBJC_IVAR_$_HAPWiFiMetrics._subnetMask
+ OBJC_IVAR_$_HAPWiFiMetrics._txPacketCount
+ OBJC_IVAR_$_HAPWiFiMetrics._txPacketErrorCount
+ OBJC_IVAR_$_HAPWiFiMetrics._wifiRestartCount
+ OBJC_IVAR_$_HAPWiFiMetrics._wifiVersion
+ _DNSServiceRefDeallocate
+ _DNSServiceResolve
+ _DNSServiceSetDispatchQueue
+ _HAP2BonjourResolveReply
+ _HAP2CancelResolverAndReportFailure
+ _HAP2CoAPAddressEqualsAddress
+ _HAP2IPv4MappedIPv6BytesFromIPv4Bytes
+ _HAP2PipelineAddressIdentity
+ _HAP2SelectEffectiveList
+ _HAP2SessionKeepAliveSelectedMaxIntervalKey
+ _HAP2SessionKeepAliveSelectedMinIntervalKey
+ _HAP2TakeNextUntriedIP
+ _HAPAVCStreamingControlCommandAsString
+ _HAPAVCStreamingControlStatusAsString
+ _HAPAVCViewerRegistrationOperationAsString
+ _HAPErrorAlreadyPairedPeerIdentifierKey
+ _HAPMetricEventBluetoothVersionTypeAsString
+ _HAPMetricEventPowerSourcesBitmaskAsString
+ _HAPMetricEventPowerSourcesEnumAsString
+ _HAPMetricEventThreadFirstRestartConnectivityStateAsString
+ _HAPMetricEventWiFiFirstRestartConnectivityStateAsString
+ _HAPMetricEventWiFiVersionTypeAsString
+ _HAPSessionKeepAliveTransportTypeAsString
+ _HAPStabilityMetricsBootReasonTypeAsString
+ _HAPStabilityMetricsHardwareFaultTypeAsString
+ _HAPWorkQueueFactoryOrDefault
+ _HTTPClientGetSelfAddress
+ _NSCocoaErrorDomain
+ _OBJC_$_PROP_LIST_HAP2AccessoryDNSResolver
+ _OBJC_CLASS_$_HAP2AccessoryAddressLists
+ _OBJC_CLASS_$_HAP2AccessoryAddressResolverPipeline
+ _OBJC_CLASS_$_HAP2AccessoryDNSResolver
+ _OBJC_CLASS_$_HAP2AccessoryServerIPCacheData
+ _OBJC_CLASS_$_HAP2BrowserResolverRegistry
+ _OBJC_CLASS_$_HAP2CoAPRequestRacingLogEvent
+ _OBJC_CLASS_$_HAP2DefaultAccessoryAddressResolverPipelineFactory
+ _OBJC_CLASS_$_HAP2SessionKeepAliveConfiguration
+ _OBJC_CLASS_$_HAP2SessionKeepAliveConfigurationEntry
+ _OBJC_CLASS_$_HAP2SessionKeepAliveListener
+ _OBJC_CLASS_$_HAP2SessionKeepAliveTransportState
+ _OBJC_CLASS_$_HAPAVCStreamingControlCommandWrapper
+ _OBJC_CLASS_$_HAPAVCStreamingControlRequest
+ _OBJC_CLASS_$_HAPAVCStreamingControlResponse
+ _OBJC_CLASS_$_HAPAVCStreamingControlStatusWrapper
+ _OBJC_CLASS_$_HAPAVCViewerRegistrationOperationWrapper
+ _OBJC_CLASS_$_HAPAccessoryCHMMetricsLogEvent
+ _OBJC_CLASS_$_HAPAccessoryCHMRecoveryLogEvent
+ _OBJC_CLASS_$_HAPBluetoothMetrics
+ _OBJC_CLASS_$_HAPBootReasonsMetrics
+ _OBJC_CLASS_$_HAPCHMMetrics
+ _OBJC_CLASS_$_HAPConnectionHealthMonitor
+ _OBJC_CLASS_$_HAPContributingSensor
+ _OBJC_CLASS_$_HAPDefaultWorkQueueFactory
+ _OBJC_CLASS_$_HAPErrorCountersMetrics
+ _OBJC_CLASS_$_HAPErrorCountersMetricsEntry
+ _OBJC_CLASS_$_HAPHKSV3UploadLatencyMetrics
+ _OBJC_CLASS_$_HAPMetricEventBluetoothVersionTypeWrapper
+ _OBJC_CLASS_$_HAPMetricEventPowerSourcesBitmaskWrapper
+ _OBJC_CLASS_$_HAPMetricEventPowerSourcesEnumWrapper
+ _OBJC_CLASS_$_HAPMetricEventThreadFirstRestartConnectivityStateWrapper
+ _OBJC_CLASS_$_HAPMetricEventWiFiFirstRestartConnectivityStateWrapper
+ _OBJC_CLASS_$_HAPMetricEventWiFiVersionTypeWrapper
+ _OBJC_CLASS_$_HAPPowerMetrics
+ _OBJC_CLASS_$_HAPSaturationMetrics
+ _OBJC_CLASS_$_HAPSensorList
+ _OBJC_CLASS_$_HAPSessionKeepAliveTransportTypeWrapper
+ _OBJC_CLASS_$_HAPStabilityMetrics
+ _OBJC_CLASS_$_HAPStabilityMetricsBootReasonTypeWrapper
+ _OBJC_CLASS_$_HAPStabilityMetricsHardwareFaultTypeWrapper
+ _OBJC_CLASS_$_HAPTLVPreferredWiFiEntry
+ _OBJC_CLASS_$_HAPTLVPreferredWiFiList
+ _OBJC_CLASS_$_HAPTLVSelectedSessionKeepAliveConfigurationEntry
+ _OBJC_CLASS_$_HAPTLVSelectedSessionKeepAliveConfigurationList
+ _OBJC_CLASS_$_HAPTLVSupportedSessionKeepAliveConfigurationEntry
+ _OBJC_CLASS_$_HAPTLVSupportedSessionKeepAliveConfigurationList
+ _OBJC_CLASS_$_HAPThermalMetrics
+ _OBJC_CLASS_$_HAPWiFiMetrics
+ _OBJC_CLASS_$_HMFTimerFactory
+ _OBJC_CLASS_$_NSCountedSet
+ _OBJC_METACLASS_$_HAP2AccessoryAddressLists
+ _OBJC_METACLASS_$_HAP2AccessoryAddressResolverPipeline
+ _OBJC_METACLASS_$_HAP2AccessoryDNSResolver
+ _OBJC_METACLASS_$_HAP2AccessoryServerIPCacheData
+ _OBJC_METACLASS_$_HAP2BrowserResolverRegistry
+ _OBJC_METACLASS_$_HAP2CoAPRequestRacingLogEvent
+ _OBJC_METACLASS_$_HAP2DefaultAccessoryAddressResolverPipelineFactory
+ _OBJC_METACLASS_$_HAP2SessionKeepAliveConfiguration
+ _OBJC_METACLASS_$_HAP2SessionKeepAliveConfigurationEntry
+ _OBJC_METACLASS_$_HAP2SessionKeepAliveListener
+ _OBJC_METACLASS_$_HAP2SessionKeepAliveTransportState
+ _OBJC_METACLASS_$_HAPAVCStreamingControlCommandWrapper
+ _OBJC_METACLASS_$_HAPAVCStreamingControlRequest
+ _OBJC_METACLASS_$_HAPAVCStreamingControlResponse
+ _OBJC_METACLASS_$_HAPAVCStreamingControlStatusWrapper
+ _OBJC_METACLASS_$_HAPAVCViewerRegistrationOperationWrapper
+ _OBJC_METACLASS_$_HAPAccessoryCHMMetricsLogEvent
+ _OBJC_METACLASS_$_HAPAccessoryCHMRecoveryLogEvent
+ _OBJC_METACLASS_$_HAPBluetoothMetrics
+ _OBJC_METACLASS_$_HAPBootReasonsMetrics
+ _OBJC_METACLASS_$_HAPCHMMetrics
+ _OBJC_METACLASS_$_HAPConnectionHealthMonitor
+ _OBJC_METACLASS_$_HAPContributingSensor
+ _OBJC_METACLASS_$_HAPDefaultWorkQueueFactory
+ _OBJC_METACLASS_$_HAPErrorCountersMetrics
+ _OBJC_METACLASS_$_HAPErrorCountersMetricsEntry
+ _OBJC_METACLASS_$_HAPHKSV3UploadLatencyMetrics
+ _OBJC_METACLASS_$_HAPMetricEventBluetoothVersionTypeWrapper
+ _OBJC_METACLASS_$_HAPMetricEventPowerSourcesBitmaskWrapper
+ _OBJC_METACLASS_$_HAPMetricEventPowerSourcesEnumWrapper
+ _OBJC_METACLASS_$_HAPMetricEventThreadFirstRestartConnectivityStateWrapper
+ _OBJC_METACLASS_$_HAPMetricEventWiFiFirstRestartConnectivityStateWrapper
+ _OBJC_METACLASS_$_HAPMetricEventWiFiVersionTypeWrapper
+ _OBJC_METACLASS_$_HAPPowerMetrics
+ _OBJC_METACLASS_$_HAPSaturationMetrics
+ _OBJC_METACLASS_$_HAPSensorList
+ _OBJC_METACLASS_$_HAPSessionKeepAliveTransportTypeWrapper
+ _OBJC_METACLASS_$_HAPStabilityMetrics
+ _OBJC_METACLASS_$_HAPStabilityMetricsBootReasonTypeWrapper
+ _OBJC_METACLASS_$_HAPStabilityMetricsHardwareFaultTypeWrapper
+ _OBJC_METACLASS_$_HAPTLVPreferredWiFiEntry
+ _OBJC_METACLASS_$_HAPTLVPreferredWiFiList
+ _OBJC_METACLASS_$_HAPTLVSelectedSessionKeepAliveConfigurationEntry
+ _OBJC_METACLASS_$_HAPTLVSelectedSessionKeepAliveConfigurationList
+ _OBJC_METACLASS_$_HAPTLVSupportedSessionKeepAliveConfigurationEntry
+ _OBJC_METACLASS_$_HAPTLVSupportedSessionKeepAliveConfigurationList
+ _OBJC_METACLASS_$_HAPThermalMetrics
+ _OBJC_METACLASS_$_HAPWiFiMetrics
+ _PROTOCOLS_HAPAccessoryCHMMetricsLogEvent
+ _PROTOCOLS_HAPAccessoryCHMRecoveryLogEvent
+ __107-[HAP2AccessoryServerTransportCoAP _sendRacingRequest:path:method:messageID:primaryClient:secondaryClient:]_block_invoke
+ __139-[HAP2AccessoryServerTransportCoAP _executeRacingWithRequest:path:method:messageID:primaryClient:secondaryClient:failoverTimeout:rttStats:]_block_invoke
+ __42-[HAP2CoAPClient sendProbeWithCompletion:]_block_invoke
+ __46-[HAP2AccessoryDNSResolver updateServiceName:]_block_invoke
+ __49-[HAP2AccessoryDNSResolver _startPipelineOnQueue]_block_invoke
+ __49-[HAP2CoAPClient getRTTStatisticsWithCompletion:]_block_invoke
+ __50-[HAP2AccessoryDNSResolver _handlePipelineUpdate:]_block_invoke
+ __53-[HAP2AccessoryServerTransportCoAP _sendHelloIfReady]_block_invoke
+ __53-[HAP2CoAPClient getLocalIPv4EndpointWithCompletion:]_block_invoke
+ __53-[HAP2CoAPClient getLocalIPv6EndpointWithCompletion:]_block_invoke
+ __55-[HAP2AccessoryServerTransportCoAP _refreshIPAddresses]_block_invoke
+ __58-[HAP2AccessoryServerTransportCoAP _startResolverIfNeeded]_block_invoke
+ __59-[HAP2AccessoryServer(Paired) resolver:didUpdateAddresses:]_block_invoke
+ __59-[HAP2AccessoryServerBrowser initWithCoordinators:storage:]_block_invoke
+ __60-[HAP2AccessoryServerController closeSessionWithCompletion:]_block_invoke
+ __61-[HAP2AccessoryServerTransportCoAP _sendEndpointRegistration]_block_invoke
+ __61-[HAP2AccessoryServerTransportCoAP _sendEndpointRegistration]_block_invoke_2
+ __62-[HAP2AccessoryServerTransportCoAP clientDidDisconnect:error:]_block_invoke
+ __65-[HAP2AccessoryServerController sendProbeOnTransport:completion:]_block_invoke
+ __65-[HAP2AccessoryServerTransportCoAP _sendWiFiEndpointRegistration]_block_invoke
+ __68-[HAP2AccessoryServerTransportCoAP _resolverDidUpdateWithAddresses:]_block_invoke
+ __68-[HAP2AccessoryServerTransportCoAP _sendMultiTransportRequest:path:]_block_invoke
+ __69-[HAP2AccessoryAddressResolverPipeline _startGetaddrinfoForHostname:]_block_invoke
+ __70-[HAP2AccessoryServerController secureTransport:didChangeState:error:]_block_invoke
+ __72-[HAP2AccessoryServerTransportCoAP _closeMultiTransportClientWithError:]_block_invoke
+ __72-[HAP2AccessoryServerTransportCoAP _closeMultiTransportClientWithError:]_block_invoke_2
+ __73-[HAP2AccessoryServerTransportCoAP _sendProbeOnTransportType:completion:]_block_invoke
+ __74-[HAP2AccessoryServerTransportCoAP _openMultiTransportClientWithActivity:]_block_invoke
+ __75-[HAP2BrowserResolverRegistry _performAuditPassOnQueueWithActiveDeviceIDs:]_block_invoke
+ __78-[HAP2AccessoryServerTransportCoAP _openPrimaryClientIteratingWithCompletion:]_block_invoke
+ __78-[HAP2AccessoryServerTransportCoAP _sendRegistrationTLVWithAddressBytes:port:]_block_invoke
+ __80-[HAP2AccessoryServerCoordinator initializePairedAccessoryServerFromCachedInfo:]_block_invoke
+ __80-[HAP2AccessoryServerCoordinator initializePairedAccessoryServerFromCachedInfo:]_block_invoke_2
+ __81-[HAP2AccessoryServerCoordinator _didDiscoverAccessory:fromMDNSEvent:completion:]_block_invoke
+ __88-[HAP2AccessoryServerTransportCoAP advanceEndpointAfterPairVerifyFailureWithCompletion:]_block_invoke
+ __89-[HAP2AccessoryServerTransportCoAP _openSecondaryClientIteratingIsThreadOnly:completion:]_block_invoke
+ __92-[HAPAccessoryServerHAP2Adapter deriveEncryptionForDataStreamWithKeySalt:completionHandler:]_block_invoke
+ __DATA_HAP2CoAPRequestRacingLogEvent
+ __DATA_HAPAccessoryCHMMetricsLogEvent
+ __DATA_HAPAccessoryCHMRecoveryLogEvent
+ __INSTANCE_METHODS_HAP2CoAPRequestRacingLogEvent
+ __INSTANCE_METHODS_HAPAccessoryCHMMetricsLogEvent
+ __INSTANCE_METHODS_HAPAccessoryCHMRecoveryLogEvent
+ __IVARS_HAP2CoAPRequestRacingLogEvent
+ __IVARS_HAPAccessoryCHMMetricsLogEvent
+ __IVARS_HAPAccessoryCHMRecoveryLogEvent
+ __METACLASS_DATA_HAP2CoAPRequestRacingLogEvent
+ __METACLASS_DATA_HAPAccessoryCHMMetricsLogEvent
+ __METACLASS_DATA_HAPAccessoryCHMRecoveryLogEvent
+ __OBJC_$_CLASS_METHODS_HAP2AccessoryDeviceIPAddress
+ __OBJC_$_CLASS_METHODS_HAP2AccessoryServerCoordinator(Test)
+ __OBJC_$_CLASS_METHODS_HAP2AccessoryServerDiscoveryHAPAccessoryInfo
+ __OBJC_$_CLASS_METHODS_HAP2AccessoryServerIPCacheData
+ __OBJC_$_CLASS_METHODS_HAP2SessionKeepAliveConfiguration
+ __OBJC_$_CLASS_METHODS_HAPAVCStreamingControlCommandWrapper
+ __OBJC_$_CLASS_METHODS_HAPAVCStreamingControlRequest
+ __OBJC_$_CLASS_METHODS_HAPAVCStreamingControlResponse
+ __OBJC_$_CLASS_METHODS_HAPAVCStreamingControlStatusWrapper
+ __OBJC_$_CLASS_METHODS_HAPAVCViewerRegistrationOperationWrapper
+ __OBJC_$_CLASS_METHODS_HAPBluetoothMetrics
+ __OBJC_$_CLASS_METHODS_HAPBootReasonsMetrics
+ __OBJC_$_CLASS_METHODS_HAPCHMMetrics
+ __OBJC_$_CLASS_METHODS_HAPConnectionHealthMonitor
+ __OBJC_$_CLASS_METHODS_HAPContributingSensor
+ __OBJC_$_CLASS_METHODS_HAPDefaultWorkQueueFactory
+ __OBJC_$_CLASS_METHODS_HAPErrorCountersMetrics
+ __OBJC_$_CLASS_METHODS_HAPErrorCountersMetricsEntry
+ __OBJC_$_CLASS_METHODS_HAPHKSV3UploadLatencyMetrics
+ __OBJC_$_CLASS_METHODS_HAPMetricEventBluetoothVersionTypeWrapper
+ __OBJC_$_CLASS_METHODS_HAPMetricEventPowerSourcesBitmaskWrapper
+ __OBJC_$_CLASS_METHODS_HAPMetricEventPowerSourcesEnumWrapper
+ __OBJC_$_CLASS_METHODS_HAPMetricEventThreadFirstRestartConnectivityStateWrapper
+ __OBJC_$_CLASS_METHODS_HAPMetricEventWiFiFirstRestartConnectivityStateWrapper
+ __OBJC_$_CLASS_METHODS_HAPMetricEventWiFiVersionTypeWrapper
+ __OBJC_$_CLASS_METHODS_HAPPowerMetrics
+ __OBJC_$_CLASS_METHODS_HAPSaturationMetrics
+ __OBJC_$_CLASS_METHODS_HAPSensorList
+ __OBJC_$_CLASS_METHODS_HAPSessionKeepAliveTransportTypeWrapper
+ __OBJC_$_CLASS_METHODS_HAPStabilityMetrics
+ __OBJC_$_CLASS_METHODS_HAPStabilityMetricsBootReasonTypeWrapper
+ __OBJC_$_CLASS_METHODS_HAPStabilityMetricsHardwareFaultTypeWrapper
+ __OBJC_$_CLASS_METHODS_HAPTLVPreferredWiFiEntry
+ __OBJC_$_CLASS_METHODS_HAPTLVPreferredWiFiList
+ __OBJC_$_CLASS_METHODS_HAPTLVSelectedSessionKeepAliveConfigurationEntry
+ __OBJC_$_CLASS_METHODS_HAPTLVSelectedSessionKeepAliveConfigurationList
+ __OBJC_$_CLASS_METHODS_HAPTLVSupportedSessionKeepAliveConfigurationEntry
+ __OBJC_$_CLASS_METHODS_HAPTLVSupportedSessionKeepAliveConfigurationList
+ __OBJC_$_CLASS_METHODS_HAPThermalMetrics
+ __OBJC_$_CLASS_METHODS_HAPWiFiMetrics
+ __OBJC_$_CLASS_PROP_LIST_HAPDefaultWorkQueueFactory
+ __OBJC_$_INSTANCE_METHODS_HAP2AccessoryAddressLists
+ __OBJC_$_INSTANCE_METHODS_HAP2AccessoryAddressResolverPipeline
+ __OBJC_$_INSTANCE_METHODS_HAP2AccessoryDNSResolver
+ __OBJC_$_INSTANCE_METHODS_HAP2AccessoryServer(Test|Paired|PairedInternal|Unpaired)
+ __OBJC_$_INSTANCE_METHODS_HAP2AccessoryServerBrowser(Test)
+ __OBJC_$_INSTANCE_METHODS_HAP2AccessoryServerCoordinator(Test)
+ __OBJC_$_INSTANCE_METHODS_HAP2AccessoryServerIPCacheData
+ __OBJC_$_INSTANCE_METHODS_HAP2BrowserResolverRegistry(Test)
+ __OBJC_$_INSTANCE_METHODS_HAP2DefaultAccessoryAddressResolverPipelineFactory
+ __OBJC_$_INSTANCE_METHODS_HAP2SessionKeepAliveConfigurationEntry
+ __OBJC_$_INSTANCE_METHODS_HAP2SessionKeepAliveListener
+ __OBJC_$_INSTANCE_METHODS_HAP2SessionKeepAliveTransportState
+ __OBJC_$_INSTANCE_METHODS_HAPAVCStreamingControlCommandWrapper
+ __OBJC_$_INSTANCE_METHODS_HAPAVCStreamingControlRequest
+ __OBJC_$_INSTANCE_METHODS_HAPAVCStreamingControlResponse
+ __OBJC_$_INSTANCE_METHODS_HAPAVCStreamingControlStatusWrapper
+ __OBJC_$_INSTANCE_METHODS_HAPAVCViewerRegistrationOperationWrapper
+ __OBJC_$_INSTANCE_METHODS_HAPBluetoothMetrics
+ __OBJC_$_INSTANCE_METHODS_HAPBootReasonsMetrics
+ __OBJC_$_INSTANCE_METHODS_HAPCHMMetrics
+ __OBJC_$_INSTANCE_METHODS_HAPConnectionHealthMonitor
+ __OBJC_$_INSTANCE_METHODS_HAPContributingSensor
+ __OBJC_$_INSTANCE_METHODS_HAPDefaultWorkQueueFactory
+ __OBJC_$_INSTANCE_METHODS_HAPErrorCountersMetrics
+ __OBJC_$_INSTANCE_METHODS_HAPErrorCountersMetricsEntry
+ __OBJC_$_INSTANCE_METHODS_HAPHKSV3UploadLatencyMetrics
+ __OBJC_$_INSTANCE_METHODS_HAPMetricEventBluetoothVersionTypeWrapper
+ __OBJC_$_INSTANCE_METHODS_HAPMetricEventPowerSourcesBitmaskWrapper
+ __OBJC_$_INSTANCE_METHODS_HAPMetricEventPowerSourcesEnumWrapper
+ __OBJC_$_INSTANCE_METHODS_HAPMetricEventThreadFirstRestartConnectivityStateWrapper
+ __OBJC_$_INSTANCE_METHODS_HAPMetricEventWiFiFirstRestartConnectivityStateWrapper
+ __OBJC_$_INSTANCE_METHODS_HAPMetricEventWiFiVersionTypeWrapper
+ __OBJC_$_INSTANCE_METHODS_HAPPowerMetrics
+ __OBJC_$_INSTANCE_METHODS_HAPSaturationMetrics
+ __OBJC_$_INSTANCE_METHODS_HAPSensorList
+ __OBJC_$_INSTANCE_METHODS_HAPSessionKeepAliveTransportTypeWrapper
+ __OBJC_$_INSTANCE_METHODS_HAPStabilityMetrics
+ __OBJC_$_INSTANCE_METHODS_HAPStabilityMetricsBootReasonTypeWrapper
+ __OBJC_$_INSTANCE_METHODS_HAPStabilityMetricsHardwareFaultTypeWrapper
+ __OBJC_$_INSTANCE_METHODS_HAPTLVPreferredWiFiEntry
+ __OBJC_$_INSTANCE_METHODS_HAPTLVPreferredWiFiList
+ __OBJC_$_INSTANCE_METHODS_HAPTLVSelectedSessionKeepAliveConfigurationEntry
+ __OBJC_$_INSTANCE_METHODS_HAPTLVSelectedSessionKeepAliveConfigurationList
+ __OBJC_$_INSTANCE_METHODS_HAPTLVSupportedSessionKeepAliveConfigurationEntry
+ __OBJC_$_INSTANCE_METHODS_HAPTLVSupportedSessionKeepAliveConfigurationList
+ __OBJC_$_INSTANCE_METHODS_HAPThermalMetrics
+ __OBJC_$_INSTANCE_METHODS_HAPWiFiMetrics
+ __OBJC_$_INSTANCE_VARIABLES_HAP2AccessoryAddressLists
+ __OBJC_$_INSTANCE_VARIABLES_HAP2AccessoryAddressResolverPipeline
+ __OBJC_$_INSTANCE_VARIABLES_HAP2AccessoryDNSResolver
+ __OBJC_$_INSTANCE_VARIABLES_HAP2AccessoryServerIPCacheData
+ __OBJC_$_INSTANCE_VARIABLES_HAP2BrowserResolverRegistry
+ __OBJC_$_INSTANCE_VARIABLES_HAP2SessionKeepAliveConfigurationEntry
+ __OBJC_$_INSTANCE_VARIABLES_HAP2SessionKeepAliveListener
+ __OBJC_$_INSTANCE_VARIABLES_HAP2SessionKeepAliveTransportState
+ __OBJC_$_INSTANCE_VARIABLES_HAPAVCStreamingControlCommandWrapper
+ __OBJC_$_INSTANCE_VARIABLES_HAPAVCStreamingControlRequest
+ __OBJC_$_INSTANCE_VARIABLES_HAPAVCStreamingControlResponse
+ __OBJC_$_INSTANCE_VARIABLES_HAPAVCStreamingControlStatusWrapper
+ __OBJC_$_INSTANCE_VARIABLES_HAPAVCViewerRegistrationOperationWrapper
+ __OBJC_$_INSTANCE_VARIABLES_HAPBluetoothMetrics
+ __OBJC_$_INSTANCE_VARIABLES_HAPBootReasonsMetrics
+ __OBJC_$_INSTANCE_VARIABLES_HAPCHMMetrics
+ __OBJC_$_INSTANCE_VARIABLES_HAPConnectionHealthMonitor
+ __OBJC_$_INSTANCE_VARIABLES_HAPContributingSensor
+ __OBJC_$_INSTANCE_VARIABLES_HAPErrorCountersMetrics
+ __OBJC_$_INSTANCE_VARIABLES_HAPErrorCountersMetricsEntry
+ __OBJC_$_INSTANCE_VARIABLES_HAPHKSV3UploadLatencyMetrics
+ __OBJC_$_INSTANCE_VARIABLES_HAPMetricEventBluetoothVersionTypeWrapper
+ __OBJC_$_INSTANCE_VARIABLES_HAPMetricEventPowerSourcesBitmaskWrapper
+ __OBJC_$_INSTANCE_VARIABLES_HAPMetricEventPowerSourcesEnumWrapper
+ __OBJC_$_INSTANCE_VARIABLES_HAPMetricEventThreadFirstRestartConnectivityStateWrapper
+ __OBJC_$_INSTANCE_VARIABLES_HAPMetricEventWiFiFirstRestartConnectivityStateWrapper
+ __OBJC_$_INSTANCE_VARIABLES_HAPMetricEventWiFiVersionTypeWrapper
+ __OBJC_$_INSTANCE_VARIABLES_HAPPowerMetrics
+ __OBJC_$_INSTANCE_VARIABLES_HAPSaturationMetrics
+ __OBJC_$_INSTANCE_VARIABLES_HAPSensorList
+ __OBJC_$_INSTANCE_VARIABLES_HAPSessionKeepAliveTransportTypeWrapper
+ __OBJC_$_INSTANCE_VARIABLES_HAPStabilityMetrics
+ __OBJC_$_INSTANCE_VARIABLES_HAPStabilityMetricsBootReasonTypeWrapper
+ __OBJC_$_INSTANCE_VARIABLES_HAPStabilityMetricsHardwareFaultTypeWrapper
+ __OBJC_$_INSTANCE_VARIABLES_HAPTLVPreferredWiFiEntry
+ __OBJC_$_INSTANCE_VARIABLES_HAPTLVPreferredWiFiList
+ __OBJC_$_INSTANCE_VARIABLES_HAPTLVSelectedSessionKeepAliveConfigurationEntry
+ __OBJC_$_INSTANCE_VARIABLES_HAPTLVSelectedSessionKeepAliveConfigurationList
+ __OBJC_$_INSTANCE_VARIABLES_HAPTLVSupportedSessionKeepAliveConfigurationEntry
+ __OBJC_$_INSTANCE_VARIABLES_HAPTLVSupportedSessionKeepAliveConfigurationList
+ __OBJC_$_INSTANCE_VARIABLES_HAPThermalMetrics
+ __OBJC_$_INSTANCE_VARIABLES_HAPWiFiMetrics
+ __OBJC_$_PROP_LIST_HAP2AccessoryAddressLists
+ __OBJC_$_PROP_LIST_HAP2AccessoryAddressResolverPipeline
+ __OBJC_$_PROP_LIST_HAP2AccessoryDNSResolver
+ __OBJC_$_PROP_LIST_HAP2AccessoryDNSResolverPrivate
+ __OBJC_$_PROP_LIST_HAP2AccessoryServerIPCacheData
+ __OBJC_$_PROP_LIST_HAP2BrowserResolverRegistry
+ __OBJC_$_PROP_LIST_HAP2DefaultAccessoryAddressResolverPipelineFactory
+ __OBJC_$_PROP_LIST_HAP2PairedAccessoryServerPrivate
+ __OBJC_$_PROP_LIST_HAP2SessionKeepAliveConfigurationEntry
+ __OBJC_$_PROP_LIST_HAP2SessionKeepAliveListener
+ __OBJC_$_PROP_LIST_HAP2SessionKeepAliveTransportState
+ __OBJC_$_PROP_LIST_HAPAVCStreamingControlCommandWrapper
+ __OBJC_$_PROP_LIST_HAPAVCStreamingControlRequest
+ __OBJC_$_PROP_LIST_HAPAVCStreamingControlResponse
+ __OBJC_$_PROP_LIST_HAPAVCStreamingControlStatusWrapper
+ __OBJC_$_PROP_LIST_HAPAVCViewerRegistrationOperationWrapper
+ __OBJC_$_PROP_LIST_HAPBluetoothMetrics
+ __OBJC_$_PROP_LIST_HAPBootReasonsMetrics
+ __OBJC_$_PROP_LIST_HAPCHMMetrics
+ __OBJC_$_PROP_LIST_HAPConnectionHealthMonitor
+ __OBJC_$_PROP_LIST_HAPContributingSensor
+ __OBJC_$_PROP_LIST_HAPDefaultWorkQueueFactory
+ __OBJC_$_PROP_LIST_HAPErrorCountersMetrics
+ __OBJC_$_PROP_LIST_HAPErrorCountersMetricsEntry
+ __OBJC_$_PROP_LIST_HAPHKSV3UploadLatencyMetrics
+ __OBJC_$_PROP_LIST_HAPMetricEventBluetoothVersionTypeWrapper
+ __OBJC_$_PROP_LIST_HAPMetricEventPowerSourcesBitmaskWrapper
+ __OBJC_$_PROP_LIST_HAPMetricEventPowerSourcesEnumWrapper
+ __OBJC_$_PROP_LIST_HAPMetricEventThreadFirstRestartConnectivityStateWrapper
+ __OBJC_$_PROP_LIST_HAPMetricEventWiFiFirstRestartConnectivityStateWrapper
+ __OBJC_$_PROP_LIST_HAPMetricEventWiFiVersionTypeWrapper
+ __OBJC_$_PROP_LIST_HAPPowerMetrics
+ __OBJC_$_PROP_LIST_HAPSaturationMetrics
+ __OBJC_$_PROP_LIST_HAPSensorList
+ __OBJC_$_PROP_LIST_HAPSessionKeepAliveTransportTypeWrapper
+ __OBJC_$_PROP_LIST_HAPStabilityMetrics
+ __OBJC_$_PROP_LIST_HAPStabilityMetricsBootReasonTypeWrapper
+ __OBJC_$_PROP_LIST_HAPStabilityMetricsHardwareFaultTypeWrapper
+ __OBJC_$_PROP_LIST_HAPTLVPreferredWiFiEntry
+ __OBJC_$_PROP_LIST_HAPTLVPreferredWiFiList
+ __OBJC_$_PROP_LIST_HAPTLVSelectedSessionKeepAliveConfigurationEntry
+ __OBJC_$_PROP_LIST_HAPTLVSelectedSessionKeepAliveConfigurationList
+ __OBJC_$_PROP_LIST_HAPTLVSupportedSessionKeepAliveConfigurationEntry
+ __OBJC_$_PROP_LIST_HAPTLVSupportedSessionKeepAliveConfigurationList
+ __OBJC_$_PROP_LIST_HAPThermalMetrics
+ __OBJC_$_PROP_LIST_HAPWiFiMetrics
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HAP2AccessoryAddressResolverPipelineFactory
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HAP2AccessoryDNSResolver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HAP2AccessoryDNSResolverCacheSubscriber
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HAP2AccessoryDNSResolverDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HAP2AccessoryDNSResolverPrivate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HAPWorkQueueFactory
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HAP2AccessoryServerSecureTransportDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HAP2AccessoryServerTransportDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HAP2AccessoryAddressResolverPipelineFactory
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HAP2AccessoryDNSResolver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HAP2AccessoryDNSResolverCacheSubscriber
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HAP2AccessoryDNSResolverDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HAP2AccessoryDNSResolverPrivate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HAPWorkQueueFactory
+ __OBJC_$_PROTOCOL_REFS_HAP2AccessoryAddressResolverPipelineFactory
+ __OBJC_$_PROTOCOL_REFS_HAP2AccessoryDNSResolver
+ __OBJC_$_PROTOCOL_REFS_HAP2AccessoryDNSResolverCacheSubscriber
+ __OBJC_$_PROTOCOL_REFS_HAP2AccessoryDNSResolverDelegate
+ __OBJC_$_PROTOCOL_REFS_HAP2AccessoryDNSResolverPrivate
+ __OBJC_$_PROTOCOL_REFS_HAPWorkQueueFactory
+ __OBJC_CLASS_PROTOCOLS_$_HAP2AccessoryDNSResolver
+ __OBJC_CLASS_PROTOCOLS_$_HAP2AccessoryDeviceIPAddress
+ __OBJC_CLASS_PROTOCOLS_$_HAP2AccessoryServer(Test|Paired|PairedInternal|Unpaired)
+ __OBJC_CLASS_PROTOCOLS_$_HAP2DefaultAccessoryAddressResolverPipelineFactory
+ __OBJC_CLASS_PROTOCOLS_$_HAP2SessionKeepAliveListener
+ __OBJC_CLASS_PROTOCOLS_$_HAPAVCStreamingControlCommandWrapper
+ __OBJC_CLASS_PROTOCOLS_$_HAPAVCStreamingControlRequest
+ __OBJC_CLASS_PROTOCOLS_$_HAPAVCStreamingControlResponse
+ __OBJC_CLASS_PROTOCOLS_$_HAPAVCStreamingControlStatusWrapper
+ __OBJC_CLASS_PROTOCOLS_$_HAPAVCViewerRegistrationOperationWrapper
+ __OBJC_CLASS_PROTOCOLS_$_HAPBluetoothMetrics
+ __OBJC_CLASS_PROTOCOLS_$_HAPBootReasonsMetrics
+ __OBJC_CLASS_PROTOCOLS_$_HAPCHMMetrics
+ __OBJC_CLASS_PROTOCOLS_$_HAPConnectionHealthMonitor
+ __OBJC_CLASS_PROTOCOLS_$_HAPContributingSensor
+ __OBJC_CLASS_PROTOCOLS_$_HAPDefaultWorkQueueFactory
+ __OBJC_CLASS_PROTOCOLS_$_HAPErrorCountersMetrics
+ __OBJC_CLASS_PROTOCOLS_$_HAPErrorCountersMetricsEntry
+ __OBJC_CLASS_PROTOCOLS_$_HAPHKSV3UploadLatencyMetrics
+ __OBJC_CLASS_PROTOCOLS_$_HAPMetricEventBluetoothVersionTypeWrapper
+ __OBJC_CLASS_PROTOCOLS_$_HAPMetricEventPowerSourcesBitmaskWrapper
+ __OBJC_CLASS_PROTOCOLS_$_HAPMetricEventPowerSourcesEnumWrapper
+ __OBJC_CLASS_PROTOCOLS_$_HAPMetricEventThreadFirstRestartConnectivityStateWrapper
+ __OBJC_CLASS_PROTOCOLS_$_HAPMetricEventWiFiFirstRestartConnectivityStateWrapper
+ __OBJC_CLASS_PROTOCOLS_$_HAPMetricEventWiFiVersionTypeWrapper
+ __OBJC_CLASS_PROTOCOLS_$_HAPPowerMetrics
+ __OBJC_CLASS_PROTOCOLS_$_HAPSaturationMetrics
+ __OBJC_CLASS_PROTOCOLS_$_HAPSensorList
+ __OBJC_CLASS_PROTOCOLS_$_HAPSessionKeepAliveTransportTypeWrapper
+ __OBJC_CLASS_PROTOCOLS_$_HAPStabilityMetrics
+ __OBJC_CLASS_PROTOCOLS_$_HAPStabilityMetricsBootReasonTypeWrapper
+ __OBJC_CLASS_PROTOCOLS_$_HAPStabilityMetricsHardwareFaultTypeWrapper
+ __OBJC_CLASS_PROTOCOLS_$_HAPTLVPreferredWiFiEntry
+ __OBJC_CLASS_PROTOCOLS_$_HAPTLVPreferredWiFiList
+ __OBJC_CLASS_PROTOCOLS_$_HAPTLVSelectedSessionKeepAliveConfigurationEntry
+ __OBJC_CLASS_PROTOCOLS_$_HAPTLVSelectedSessionKeepAliveConfigurationList
+ __OBJC_CLASS_PROTOCOLS_$_HAPTLVSupportedSessionKeepAliveConfigurationEntry
+ __OBJC_CLASS_PROTOCOLS_$_HAPTLVSupportedSessionKeepAliveConfigurationList
+ __OBJC_CLASS_PROTOCOLS_$_HAPThermalMetrics
+ __OBJC_CLASS_PROTOCOLS_$_HAPWiFiMetrics
+ __OBJC_CLASS_RO_$_HAP2AccessoryAddressLists
+ __OBJC_CLASS_RO_$_HAP2AccessoryAddressResolverPipeline
+ __OBJC_CLASS_RO_$_HAP2AccessoryDNSResolver
+ __OBJC_CLASS_RO_$_HAP2AccessoryServerIPCacheData
+ __OBJC_CLASS_RO_$_HAP2BrowserResolverRegistry
+ __OBJC_CLASS_RO_$_HAP2DefaultAccessoryAddressResolverPipelineFactory
+ __OBJC_CLASS_RO_$_HAP2SessionKeepAliveConfiguration
+ __OBJC_CLASS_RO_$_HAP2SessionKeepAliveConfigurationEntry
+ __OBJC_CLASS_RO_$_HAP2SessionKeepAliveListener
+ __OBJC_CLASS_RO_$_HAP2SessionKeepAliveTransportState
+ __OBJC_CLASS_RO_$_HAPAVCStreamingControlCommandWrapper
+ __OBJC_CLASS_RO_$_HAPAVCStreamingControlRequest
+ __OBJC_CLASS_RO_$_HAPAVCStreamingControlResponse
+ __OBJC_CLASS_RO_$_HAPAVCStreamingControlStatusWrapper
+ __OBJC_CLASS_RO_$_HAPAVCViewerRegistrationOperationWrapper
+ __OBJC_CLASS_RO_$_HAPBluetoothMetrics
+ __OBJC_CLASS_RO_$_HAPBootReasonsMetrics
+ __OBJC_CLASS_RO_$_HAPCHMMetrics
+ __OBJC_CLASS_RO_$_HAPConnectionHealthMonitor
+ __OBJC_CLASS_RO_$_HAPContributingSensor
+ __OBJC_CLASS_RO_$_HAPDefaultWorkQueueFactory
+ __OBJC_CLASS_RO_$_HAPErrorCountersMetrics
+ __OBJC_CLASS_RO_$_HAPErrorCountersMetricsEntry
+ __OBJC_CLASS_RO_$_HAPHKSV3UploadLatencyMetrics
+ __OBJC_CLASS_RO_$_HAPMetricEventBluetoothVersionTypeWrapper
+ __OBJC_CLASS_RO_$_HAPMetricEventPowerSourcesBitmaskWrapper
+ __OBJC_CLASS_RO_$_HAPMetricEventPowerSourcesEnumWrapper
+ __OBJC_CLASS_RO_$_HAPMetricEventThreadFirstRestartConnectivityStateWrapper
+ __OBJC_CLASS_RO_$_HAPMetricEventWiFiFirstRestartConnectivityStateWrapper
+ __OBJC_CLASS_RO_$_HAPMetricEventWiFiVersionTypeWrapper
+ __OBJC_CLASS_RO_$_HAPPowerMetrics
+ __OBJC_CLASS_RO_$_HAPSaturationMetrics
+ __OBJC_CLASS_RO_$_HAPSensorList
+ __OBJC_CLASS_RO_$_HAPSessionKeepAliveTransportTypeWrapper
+ __OBJC_CLASS_RO_$_HAPStabilityMetrics
+ __OBJC_CLASS_RO_$_HAPStabilityMetricsBootReasonTypeWrapper
+ __OBJC_CLASS_RO_$_HAPStabilityMetricsHardwareFaultTypeWrapper
+ __OBJC_CLASS_RO_$_HAPTLVPreferredWiFiEntry
+ __OBJC_CLASS_RO_$_HAPTLVPreferredWiFiList
+ __OBJC_CLASS_RO_$_HAPTLVSelectedSessionKeepAliveConfigurationEntry
+ __OBJC_CLASS_RO_$_HAPTLVSelectedSessionKeepAliveConfigurationList
+ __OBJC_CLASS_RO_$_HAPTLVSupportedSessionKeepAliveConfigurationEntry
+ __OBJC_CLASS_RO_$_HAPTLVSupportedSessionKeepAliveConfigurationList
+ __OBJC_CLASS_RO_$_HAPThermalMetrics
+ __OBJC_CLASS_RO_$_HAPWiFiMetrics
+ __OBJC_LABEL_PROTOCOL_$_HAP2AccessoryAddressResolverPipelineFactory
+ __OBJC_LABEL_PROTOCOL_$_HAP2AccessoryDNSResolver
+ __OBJC_LABEL_PROTOCOL_$_HAP2AccessoryDNSResolverCacheSubscriber
+ __OBJC_LABEL_PROTOCOL_$_HAP2AccessoryDNSResolverDelegate
+ __OBJC_LABEL_PROTOCOL_$_HAP2AccessoryDNSResolverPrivate
+ __OBJC_LABEL_PROTOCOL_$_HAPWorkQueueFactory
+ __OBJC_METACLASS_RO_$_HAP2AccessoryAddressLists
+ __OBJC_METACLASS_RO_$_HAP2AccessoryAddressResolverPipeline
+ __OBJC_METACLASS_RO_$_HAP2AccessoryDNSResolver
+ __OBJC_METACLASS_RO_$_HAP2AccessoryServerIPCacheData
+ __OBJC_METACLASS_RO_$_HAP2BrowserResolverRegistry
+ __OBJC_METACLASS_RO_$_HAP2DefaultAccessoryAddressResolverPipelineFactory
+ __OBJC_METACLASS_RO_$_HAP2SessionKeepAliveConfiguration
+ __OBJC_METACLASS_RO_$_HAP2SessionKeepAliveConfigurationEntry
+ __OBJC_METACLASS_RO_$_HAP2SessionKeepAliveListener
+ __OBJC_METACLASS_RO_$_HAP2SessionKeepAliveTransportState
+ __OBJC_METACLASS_RO_$_HAPAVCStreamingControlCommandWrapper
+ __OBJC_METACLASS_RO_$_HAPAVCStreamingControlRequest
+ __OBJC_METACLASS_RO_$_HAPAVCStreamingControlResponse
+ __OBJC_METACLASS_RO_$_HAPAVCStreamingControlStatusWrapper
+ __OBJC_METACLASS_RO_$_HAPAVCViewerRegistrationOperationWrapper
+ __OBJC_METACLASS_RO_$_HAPBluetoothMetrics
+ __OBJC_METACLASS_RO_$_HAPBootReasonsMetrics
+ __OBJC_METACLASS_RO_$_HAPCHMMetrics
+ __OBJC_METACLASS_RO_$_HAPConnectionHealthMonitor
+ __OBJC_METACLASS_RO_$_HAPContributingSensor
+ __OBJC_METACLASS_RO_$_HAPDefaultWorkQueueFactory
+ __OBJC_METACLASS_RO_$_HAPErrorCountersMetrics
+ __OBJC_METACLASS_RO_$_HAPErrorCountersMetricsEntry
+ __OBJC_METACLASS_RO_$_HAPHKSV3UploadLatencyMetrics
+ __OBJC_METACLASS_RO_$_HAPMetricEventBluetoothVersionTypeWrapper
+ __OBJC_METACLASS_RO_$_HAPMetricEventPowerSourcesBitmaskWrapper
+ __OBJC_METACLASS_RO_$_HAPMetricEventPowerSourcesEnumWrapper
+ __OBJC_METACLASS_RO_$_HAPMetricEventThreadFirstRestartConnectivityStateWrapper
+ __OBJC_METACLASS_RO_$_HAPMetricEventWiFiFirstRestartConnectivityStateWrapper
+ __OBJC_METACLASS_RO_$_HAPMetricEventWiFiVersionTypeWrapper
+ __OBJC_METACLASS_RO_$_HAPPowerMetrics
+ __OBJC_METACLASS_RO_$_HAPSaturationMetrics
+ __OBJC_METACLASS_RO_$_HAPSensorList
+ __OBJC_METACLASS_RO_$_HAPSessionKeepAliveTransportTypeWrapper
+ __OBJC_METACLASS_RO_$_HAPStabilityMetrics
+ __OBJC_METACLASS_RO_$_HAPStabilityMetricsBootReasonTypeWrapper
+ __OBJC_METACLASS_RO_$_HAPStabilityMetricsHardwareFaultTypeWrapper
+ __OBJC_METACLASS_RO_$_HAPTLVPreferredWiFiEntry
+ __OBJC_METACLASS_RO_$_HAPTLVPreferredWiFiList
+ __OBJC_METACLASS_RO_$_HAPTLVSelectedSessionKeepAliveConfigurationEntry
+ __OBJC_METACLASS_RO_$_HAPTLVSelectedSessionKeepAliveConfigurationList
+ __OBJC_METACLASS_RO_$_HAPTLVSupportedSessionKeepAliveConfigurationEntry
+ __OBJC_METACLASS_RO_$_HAPTLVSupportedSessionKeepAliveConfigurationList
+ __OBJC_METACLASS_RO_$_HAPThermalMetrics
+ __OBJC_METACLASS_RO_$_HAPWiFiMetrics
+ __OBJC_PROTOCOL_$_HAP2AccessoryAddressResolverPipelineFactory
+ __OBJC_PROTOCOL_$_HAP2AccessoryDNSResolver
+ __OBJC_PROTOCOL_$_HAP2AccessoryDNSResolverCacheSubscriber
+ __OBJC_PROTOCOL_$_HAP2AccessoryDNSResolverDelegate
+ __OBJC_PROTOCOL_$_HAP2AccessoryDNSResolverPrivate
+ __OBJC_PROTOCOL_$_HAPWorkQueueFactory
+ __OBJC_PROTOCOL_REFERENCE_$_HAP2AccessoryDNSResolverPrivate
+ __PROPERTIES_HAP2CoAPRequestRacingLogEvent
+ __PROPERTIES_HAPAccessoryCHMMetricsLogEvent
+ __PROPERTIES_HAPAccessoryCHMRecoveryLogEvent
+ __PROTOCOLS_HAPAccessoryCHMMetricsLogEvent
+ __PROTOCOLS_HAPAccessoryCHMRecoveryLogEvent
+ __ZL10_cacheLock
+ __ZL11_cacheValid
+ __ZL11_eventQueue
+ __ZL11_generation
+ __ZL19_sharedThreadClient
+ __ZL20_eventQueueOnceToken
+ __ZL22_cachedMeshLocalPrefix
+ __ZL22_sharedClientOnceToken
+ __ZL24_lastInstalledNCPHandler
+ __ZL30_lastInstalledPreferredHandler
+ __ZNK6CtrXPC5Event7getNameEv
+ __ZdlPv
+ __ZnwmSt19__type_descriptor_t
+ ___101-[HAP2AccessoryServerSecureTransportBase transport:pairVerifyDidFailOnIPAddress:transportType:error:]_block_invoke
+ ___107-[HAP2AccessoryServerTransportCoAP _sendRacingRequest:path:method:messageID:primaryClient:secondaryClient:]_block_invoke
+ ___139-[HAP2AccessoryServerTransportCoAP _executeRacingWithRequest:path:method:messageID:primaryClient:secondaryClient:failoverTimeout:rttStats:]_block_invoke
+ ___143-[HAP2DefaultAccessoryAddressResolverPipelineFactory createResolverWithServiceName:serviceType:serviceDomain:queue:updateHandler:errorHandler:]_block_invoke
+ ___145-[HAP2AccessoryServer(PairedInternal) keepAliveListener:didMissHeartbeatOnTransport:expectedInterval:timeSinceLastHeartbeat:allTransportsMissed:]_block_invoke
+ ___145-[HAP2AccessoryServer(PairedInternal) keepAliveListener:didMissHeartbeatOnTransport:expectedInterval:timeSinceLastHeartbeat:allTransportsMissed:]_block_invoke_2
+ ___36+[HAP2ThreadNetworkUtil _eventQueue]_block_invoke
+ ___36-[HAP2SessionKeepAliveListener stop]_block_invoke
+ ___37-[HAP2AccessoryServerBrowser ipCache]_block_invoke
+ ___37-[HAP2SessionKeepAliveListener start]_block_invoke
+ ___39-[HAP2AccessoryDNSResolver serviceName]_block_invoke
+ ___40-[HAP2AccessoryDNSResolver stopPipeline]_block_invoke
+ ___41-[HAP2AccessoryDNSResolver becameEmptyAt]_block_invoke
+ ___41-[HAP2AccessoryDNSResolver startPipeline]_block_invoke
+ ___41-[HAP2AccessoryServerBrowser currentPTRs]_block_invoke
+ ___41-[HAP2AccessoryServerBrowser setIPCache:]_block_invoke
+ ___42-[HAP2CoAPClient _didDisconnectWithError:]_block_invoke
+ ___42-[HAP2CoAPClient sendProbeWithCompletion:]_block_invoke
+ ___42-[HAP2CoAPClient sendProbeWithCompletion:]_block_invoke_2
+ ___43+[HAPDefaultWorkQueueFactory sharedFactory]_block_invoke
+ ___43-[HAP2AccessoryDNSResolver attachDelegate:]_block_invoke
+ ___43-[HAP2AccessoryDNSResolver detachDelegate:]_block_invoke
+ ___43-[HAP2AccessoryServer hasWiFiAdvertisement]_block_invoke
+ ___44+[HAP2ThreadNetworkUtil _sharedThreadClient]_block_invoke
+ ___44-[HAP2AccessoryDNSResolver currentAddresses]_block_invoke
+ ___45+[HAP2AccessoryServerIPCacheData logCategory]_block_invoke
+ ___45-[HAP2AccessoryServer hasThreadAdvertisement]_block_invoke
+ ___46-[HAP2AccessoryAddressResolverPipeline cancel]_block_invoke
+ ___46-[HAP2AccessoryDNSResolver updateServiceName:]_block_invoke
+ ___47-[HAP2AccessoryServer setHasWiFiAdvertisement:]_block_invoke
+ ___48+[HAP2ThreadNetworkUtil setupEventSubscriptions]_block_invoke
+ ___48-[HAP2AccessoryServer _setHasWiFiAdvertisement:]_block_invoke
+ ___49-[HAP2AccessoryDNSResolver _startPipelineOnQueue]_block_invoke
+ ___49-[HAP2AccessoryDNSResolver _startPipelineOnQueue]_block_invoke_2
+ ___49-[HAP2AccessoryServer setHasThreadAdvertisement:]_block_invoke
+ ___49-[HAP2CoAPClient getLocalEndpointWithCompletion:]_block_invoke
+ ___49-[HAP2CoAPClient getLocalEndpointWithCompletion:]_block_invoke_2
+ ___49-[HAP2CoAPClient getLocalEndpointWithCompletion:]_block_invoke_3
+ ___49-[HAP2CoAPClient getLocalEndpointWithCompletion:]_block_invoke_4
+ ___49-[HAP2CoAPClient getLocalEndpointWithCompletion:]_block_invoke_5
+ ___49-[HAP2CoAPClient getRTTStatisticsWithCompletion:]_block_invoke
+ ___49-[HAP2CoAPClient getRTTStatisticsWithCompletion:]_block_invoke_2
+ ___49-[HAPAccessoryServerIP disconnectWithCompletion:]_block_invoke
+ ___50-[HAP2AccessoryDNSResolver _handlePipelineUpdate:]_block_invoke
+ ___50-[HAP2AccessoryDNSResolver attachCacheSubscriber:]_block_invoke
+ ___50-[HAP2AccessoryDNSResolver detachCacheSubscriber:]_block_invoke
+ ___50-[HAP2AccessoryServer _setHasThreadAdvertisement:]_block_invoke
+ ___50-[HAP2BrowserResolverRegistry(Test) _allDeviceIDs]_block_invoke
+ ___51-[HAP2AccessoryDNSResolver _test_setBecameEmptyAt:]_block_invoke
+ ___51-[HAP2BrowserResolverRegistry resolverForDeviceID:]_block_invoke
+ ___52-[HAP2AccessoryDNSResolver deferAgingClockIfRunning]_block_invoke
+ ___52-[HAP2AccessoryServerBrowser _fireRevalidationSweep]_block_invoke
+ ___52-[HAP2SessionKeepAliveListener isTrackingTransport:]_block_invoke
+ ___53-[HAP2AccessoryServerTransportCoAP _sendHelloIfReady]_block_invoke
+ ___53-[HAP2AccessoryServerTransportCoAP _sendHelloIfReady]_block_invoke_2
+ ___53-[HAP2CoAPClient getLocalIPv4EndpointWithCompletion:]_block_invoke
+ ___53-[HAP2CoAPClient getLocalIPv4EndpointWithCompletion:]_block_invoke_2
+ ___53-[HAP2CoAPClient getLocalIPv6EndpointWithCompletion:]_block_invoke
+ ___53-[HAP2CoAPClient getLocalIPv6EndpointWithCompletion:]_block_invoke_2
+ ___53-[HAP2SessionKeepAliveListener trackedTransportTypes]_block_invoke
+ ___54-[HAP2AccessoryServerBrowser _buildActiveDeviceIDsSet]_block_invoke
+ ___55-[HAP2AccessoryServerBrowser _armPTRRevalidationWindow]_block_invoke
+ ___55-[HAP2AccessoryServerBrowser _armPTRRevalidationWindow]_block_invoke_2
+ ___55-[HAP2AccessoryServerBrowser hasCurrentPTRForDeviceID:]_block_invoke
+ ___55-[HAP2AccessoryServerTransportCoAP _refreshIPAddresses]_block_invoke
+ ___56-[HAP2SessionKeepAliveListener resetHeartbeatTimestamps]_block_invoke
+ ___57-[HAP2AccessoryServerTransportCoAP clientDidReceivePing:]_block_invoke
+ ___57-[HAP2BrowserResolverRegistry removeResolverForDeviceID:]_block_invoke
+ ___58-[HAP2AccessoryServer(Paired) closeSessionWithCompletion:]_block_invoke
+ ___58-[HAP2AccessoryServer(Paired) configureKeepAliveListener:]_block_invoke
+ ___58-[HAP2AccessoryServerBrowser _cancelPTRRevalidationWindow]_block_invoke
+ ___58-[HAP2AccessoryServerCoordinator(Test) _test_deliverLoss:]_block_invoke
+ ___58-[HAP2AccessoryServerTransportCoAP _startResolverIfNeeded]_block_invoke
+ ___58-[HAPAccessoryServerHAP2Adapter disconnectWithCompletion:]_block_invoke
+ ___59-[HAP2AccessoryServer(Paired) resolver:didUpdateAddresses:]_block_invoke
+ ___59-[HAP2AccessoryServer(Paired) resolver:didUpdateAddresses:]_block_invoke_2
+ ___59-[HAP2AccessoryServerTransportBase hasQueuedCloseOperation]_block_invoke
+ ___59-[HAP2AccessoryServerTransportCoAP _executeCacheMissCancel]_block_invoke
+ ___60-[HAP2AccessoryServerController closeSessionWithCompletion:]_block_invoke
+ ___60-[HAP2SerializedOperationQueue _applyCallerQoSToOperations:]_block_invoke
+ ___61-[HAP2AccessoryServer _setHasDiscoveryAdvertisementLockOnly:]_block_invoke
+ ___61-[HAP2AccessoryServerTransportCoAP _sendEndpointRegistration]_block_invoke
+ ___61-[HAP2AccessoryServerTransportCoAP _sendEndpointRegistration]_block_invoke_2
+ ___61-[HAP2AccessoryServerTransportCoAP _startResolveTimeoutTimer]_block_invoke
+ ___61-[HAP2AccessoryServerTransportCoAP _startResolveTimeoutTimer]_block_invoke_2
+ ___61-[HAP2CoAPClient _ioThreadDidReceivePingInSession:messageID:]_block_invoke
+ ___61-[HAP2CoAPClient _ioThreadDidReceivePongInSession:messageID:]_block_invoke
+ ___62-[HAP2AccessoryServer(Paired) didReceiveHeartbeatOnTransport:]_block_invoke
+ ___62-[HAP2AccessoryServerBrowser noteBrowsedPTRRemoveForDeviceID:]_block_invoke
+ ___62-[HAP2AccessoryServerTransportCoAP _resolverDidFailWithError:]_block_invoke
+ ___62-[HAP2AccessoryServerTransportCoAP clientDidDisconnect:error:]_block_invoke
+ ___63-[HAP2AccessoryServerController readLocalEndpointsWithHandler:]_block_invoke
+ ___63-[HAP2AccessoryServerCoordinator(Test) _test_deliverDiscovery:]_block_invoke
+ ___63-[HAP2AccessoryServerCoordinator(Test) _test_deliverDiscovery:]_block_invoke_2
+ ___63-[HAP2SessionKeepAliveListener didReceiveHeartbeatOnTransport:]_block_invoke
+ ___63-[HAP2SessionKeepAliveListener hasMissedHeartbeatForTransport:]_block_invoke
+ ___64-[HAP2AccessoryServer(Test) _test_setConnectionStateUnreachable]_block_invoke
+ ___65-[HAP2AccessoryServerController sendProbeOnTransport:completion:]_block_invoke
+ ___65-[HAP2AccessoryServerTransportCoAP _sendWiFiEndpointRegistration]_block_invoke
+ ___65-[HAP2AccessoryServerTransportCoAP _sendWiFiEndpointRegistration]_block_invoke_2
+ ___66-[HAP2AccessoryServerTransportCoAP readLocalEndpointsWithHandler:]_block_invoke
+ ___66-[HAP2AccessoryServerTransportCoAP readLocalEndpointsWithHandler:]_block_invoke_2
+ ___66-[HAP2AccessoryServerTransportCoAP readLocalEndpointsWithHandler:]_block_invoke_3
+ ___67-[HAP2BrowserResolverRegistry performAuditPassWithActiveDeviceIDs:]_block_invoke
+ ___67-[HAP2SessionKeepAliveListener timeSinceLastHeartbeatForTransport:]_block_invoke
+ ___68-[HAP2AccessoryServerBrowser _restoreCachedAccessoryServersIfNeeded]_block_invoke
+ ___68-[HAP2AccessoryServerTransportCoAP _resolverDidUpdateWithAddresses:]_block_invoke
+ ___68-[HAP2AccessoryServerTransportCoAP _sendMultiTransportRequest:path:]_block_invoke
+ ___69-[HAP2AccessoryAddressResolverPipeline _startGetaddrinfoForHostname:]_block_invoke
+ ___69-[HAP2AccessoryServerTransportCoAP signalPairVerifySuccessToDelegate]_block_invoke
+ ___69-[HAPAccessoryServerHAP2Adapter dataStreamPeerAddressWithCompletion:]_block_invoke
+ ___70-[HAP2AccessoryServerController _announceReestablishedSessionIfNeeded]_block_invoke
+ ___70-[HAP2AccessoryServerTransportCoAP applyResolverAddresses:completion:]_block_invoke
+ ___70-[HAP2BrowserResolverRegistry createResolverWithDeviceID:serviceName:]_block_invoke
+ ___71-[HAP2AccessoryServerBrowser noteBrowsedPTRAddForDeviceID:serviceName:]_block_invoke
+ ___72-[HAP2AccessoryServerSecureTransportBase readLocalEndpointsWithHandler:]_block_invoke
+ ___72-[HAP2AccessoryServerTransportCoAP _closeMultiTransportClientWithError:]_block_invoke
+ ___72-[HAP2AccessoryServerTransportCoAP _closeMultiTransportClientWithError:]_block_invoke_2
+ ___72-[HAP2AccessoryServerTransportCoAP _scheduleResolverRestartAfterFailure]_block_invoke
+ ___72-[HAP2AccessoryServerTransportCoAP _scheduleResolverRestartAfterFailure]_block_invoke_2
+ ___72-[HAP2AccessoryServerTransportCoAP dataStreamPeerAddressWithCompletion:]_block_invoke
+ ___73-[HAP2AccessoryServerTransportCoAP _sendProbeOnTransportType:completion:]_block_invoke
+ ___74-[HAP2AccessoryServerBrowser cachedIPDidUpdate:transportType:forDeviceID:]_block_invoke
+ ___74-[HAP2AccessoryServerSecureTransportBase sendProbeOnTransport:completion:]_block_invoke
+ ___74-[HAP2AccessoryServerSecureTransportBase sendProbeOnTransport:completion:]_block_invoke_2
+ ___74-[HAP2AccessoryServerTransportCoAP _finalizeRequestCompletion:path:error:]_block_invoke
+ ___74-[HAP2AccessoryServerTransportCoAP _openMultiTransportClientWithActivity:]_block_invoke
+ ___75-[HAP2BrowserResolverRegistry _performAuditPassOnQueueWithActiveDeviceIDs:]_block_invoke
+ ___76-[HAP2AccessoryServerTransportCoAP _armInitialCacheGracePeriodTimerIfNeeded]_block_invoke
+ ___76-[HAP2AccessoryServerTransportCoAP _armInitialCacheGracePeriodTimerIfNeeded]_block_invoke_2
+ ___76-[HAP2AccessoryServerTransportCoAP _openPrimaryClientForRefreshWithAddress:]_block_invoke
+ ___76-[HAP2AccessoryServerTransportCoAP _openPrimaryClientForRefreshWithAddress:]_block_invoke_2
+ ___77-[HAP2AccessoryServerSecureTransportPairVerify _currentStateChangeGeneration]_block_invoke
+ ___78-[HAP2AccessoryServerSecureTransportPairVerify _clearECDSAStateForGeneration:]_block_invoke
+ ___78-[HAP2AccessoryServerTransportCoAP _openPrimaryClientIteratingWithCompletion:]_block_invoke
+ ___78-[HAP2AccessoryServerTransportCoAP _openPrimaryClientIteratingWithCompletion:]_block_invoke_2
+ ___78-[HAP2AccessoryServerTransportCoAP _openSecondaryClientForRefreshWithAddress:]_block_invoke
+ ___78-[HAP2AccessoryServerTransportCoAP _openSecondaryClientForRefreshWithAddress:]_block_invoke_2
+ ___78-[HAP2AccessoryServerTransportCoAP _sendRegistrationTLVWithAddressBytes:port:]_block_invoke
+ ___78-[HAPAccessoryServerBrowserHAP2Adapter discoverAccessoryServerWithIdentifier:]_block_invoke_3
+ ___78-[HAPAccessoryServerBrowserHAP2Adapter discoverAccessoryServerWithIdentifier:]_block_invoke_4
+ ___79-[HAP2AccessoryServerBrowser(Test) _test_restoreCachedAccessoryServersIfNeeded]_block_invoke
+ ___79-[HAP2AccessoryServerSecureTransportBase transport:didChangeWiFiAdvertisement:]_block_invoke
+ ___79-[HAP2AccessoryServerTransportCoAP signalPairVerifyFailureToDelegateWithError:]_block_invoke
+ ___80-[HAP2AccessoryServerCoordinator initializePairedAccessoryServerFromCachedInfo:]_block_invoke
+ ___80-[HAP2AccessoryServerCoordinator initializePairedAccessoryServerFromCachedInfo:]_block_invoke_2
+ ___81-[HAP2AccessoryServerCoordinator _didDiscoverAccessory:fromMDNSEvent:completion:]_block_invoke
+ ___81-[HAP2AccessoryServerSecureTransportBase transport:didChangeThreadAdvertisement:]_block_invoke
+ ___81-[HAPSecuritySession deriveEncryptionForDataStreamWithKeySalt:completionHandler:]_block_invoke
+ ___82-[HAP2AccessoryServerTransportCoAP _maybeFireOffQueueCacheMissCancelForAddresses:]_block_invoke
+ ___83-[HAP2AccessoryServer(PairedInternal) keepAliveListenerDidCompleteIPPortPairCheck:]_block_invoke
+ ___83-[HAP2AccessoryServer(PairedInternal) keepAliveListenerDidCompleteIPPortPairCheck:]_block_invoke_2
+ ___83-[HAP2AccessoryServerSecureTransportBase transport:didReceiveHeartbeatOnTransport:]_block_invoke
+ ___84-[HAP2AccessoryServer(PairedInternal) _handleProbeCompletion:forKeepAliveTransport:]_block_invoke
+ ___84-[HAP2AccessoryServerBrowser _reinitializeFromCachedRecordsAfterCoordinatorsStarted]_block_invoke
+ ___84-[HAP2AccessoryServerController checkConnectedIPAddressStaleOnTransport:completion:]_block_invoke
+ ___86-[HAP2AccessoryServer(Paired) mergeWithNewlyDiscoveredPairedAccessoryServer:resolver:]_block_invoke
+ ___86-[HAP2AccessoryServerSecureTransportPairVerify _handleECDSASessionFailure:generation:]_block_invoke
+ ___86-[HAP2AccessoryServerSecureTransportPairVerify _handleECDSASessionFailure:generation:]_block_invoke_2
+ ___86-[HAP2AccessoryServerSecureTransportPairVerify _handleECDSASessionFailure:generation:]_block_invoke_3
+ ___87-[HAP2AccessoryServerTransportCoAP checkConnectedIPAddressStaleOnTransport:completion:]_block_invoke
+ ___87-[HAP2CoAPClient sendRequestWithMethod:path:payload:messageID:dscpPriority:completion:]_block_invoke
+ ___87-[HAP2CoAPClient sendRequestWithMethod:path:payload:messageID:dscpPriority:completion:]_block_invoke_2
+ ___88-[HAP2AccessoryServerTransportCoAP advanceEndpointAfterPairVerifyFailureWithCompletion:]_block_invoke
+ ___88-[HAP2AccessoryServerTransportCoAP advanceEndpointAfterPairVerifyFailureWithCompletion:]_block_invoke_2
+ ___89-[HAP2AccessoryDNSResolver _applyCachedIP:transportType:notifySubscriber:seedAgingClock:]_block_invoke
+ ___89-[HAP2AccessoryServerSecureTransportPairVerify _claimStateChangeCompletionForGeneration:]_block_invoke
+ ___89-[HAP2AccessoryServerTransportCoAP _createDefaultResolverWithUpdateHandler:errorHandler:]_block_invoke
+ ___89-[HAP2AccessoryServerTransportCoAP _openSecondaryClientIteratingIsThreadOnly:completion:]_block_invoke
+ ___89-[HAP2AccessoryServerTransportCoAP _openSecondaryClientIteratingIsThreadOnly:completion:]_block_invoke_2
+ ___90-[HAP2AccessoryServer(PairedInternal) _closeSessionIfConnectedIPAddressStaleForTransport:]_block_invoke
+ ___90-[HAP2AccessoryServer(PairedInternal) _closeSessionIfConnectedIPAddressStaleForTransport:]_block_invoke_2
+ ___90-[HAP2AccessoryServerBrowser noteBonjourAdvertisementUpdatedForDeviceID:rawDiscoveryInfo:]_block_invoke
+ ___90-[HAP2AccessoryServerTransportCoAP _readLocalEndpointForClient:transport:into:completion:]_block_invoke
+ ___90-[HAP2AccessoryServerTransportCoAP _readLocalEndpointForClient:transport:into:completion:]_block_invoke_2
+ ___91-[HAP2AccessoryServerEncodingThread _parseCharacteristics:isMultiTransportAccessory:error:]_block_invoke
+ ___92-[HAPAccessoryServerHAP2Adapter deriveEncryptionForDataStreamWithKeySalt:completionHandler:]_block_invoke
+ ___93-[HAP2AccessoryServerSecureTransportBase checkConnectedIPAddressStaleOnTransport:completion:]_block_invoke
+ ___94-[HAP2BrowserResolverRegistry updateCachedAddressesForDeviceID:cachedPrimary:cachedSecondary:]_block_invoke
+ ___97-[HAP2CoAPClient _sendRequestWithMethod:path:payload:activity:messageID:dscpPriority:completion:]_block_invoke
+ ___97-[HAP2CoAPClient _sendRequestWithMethod:path:payload:activity:messageID:dscpPriority:completion:]_block_invoke_2
+ ___97-[HAPAccessoryServerBrowserHAP2Adapter isThreadAccessoryDiscoveredWithAccessoryServerIdentifier:]_block_invoke
+ ___99-[HAP2AccessoryServerSecureTransportBase transport:pairVerifyDidCompleteOnIPAddress:transportType:]_block_invoke
+ ___block_descriptor_106_e8_32s40s48s56s64r72r80r88r_e28_v24?0"NSData"8"NSError"16l
+ ___block_descriptor_122_e8_32s40s48s56s64s72r80r88r96r104w_e28_v24?0"NSData"8"NSError"16l
+ ___block_descriptor_123_e8_32s40s48s56s64s72s80r88r96r104r112w_e5_v8?0l
+ ___block_descriptor_32_e716_v24?0"HAP2CoAPClient"8^{coap_session_t=CCCIII{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}}^{coap_endpoint_t}^{coap_context_t}^vSCi^{coap_queue_t}Q[8C]Q^{coap_pdu_t}QQQQQ*Q*Q^vI{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}IidddIddddCddI[32{?=SdC}]}16l
+ ___block_descriptor_40_e28_v32?0"NSOperation"8Q16^B24l
+ ___block_descriptor_40_e65_v24?0{shared_ptr<CtrXPC::Event>=^{Event}^{__shared_weak_count}}8l
+ ___block_descriptor_40_e8_32bs_e41_v32?0"NSData"8"NSString"16"NSError"24l
+ ___block_descriptor_40_e8_32bs_e49_v28?0B8"HAP2AccessorySessionInfo"12"NSError"20l
+ ___block_descriptor_40_e8_32s_e31_v28?0"NSData"8S16"NSError"20l
+ ___block_descriptor_40_e8_32w_e11_v16?0i8i12l
+ ___block_descriptor_40_e8_32w_e12_v24?0^8Q16l
+ ___block_descriptor_40_e8_32w_e15_v16?0?<v?q>8l
+ ___block_descriptor_40_e8_32w_e17_v16?0"NSArray"8l
+ ___block_descriptor_40_e8_32w_e22_v16?0"NSDictionary"8l
+ ___block_descriptor_42_e8_32s_e5_v8?0l
+ ___block_descriptor_48_e716_v24?0"HAP2CoAPClient"8^{coap_session_t=CCCIII{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}}^{coap_endpoint_t}^{coap_context_t}^vSCi^{coap_queue_t}Q[8C]Q^{coap_pdu_t}QQQQQ*Q*Q^vI{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}IidddIddddCddI[32{?=SdC}]}16l
+ ___block_descriptor_48_e8_32bs40r_e28_v24?0"NSData"8"NSError"16l
+ ___block_descriptor_48_e8_32bs40w_e862_v24?0^{coap_context_t=[6S]^{coap_resource_t}^{coap_resource_t}^{coap_async_state_t}Q^{coap_queue_t}^{coap_endpoint_t}^{coap_session_t}^?^?^?^?^?^?^?^?^?^?^v*Q*QIIIII^v}8^{coap_session_t=CCCIII{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}}^{coap_endpoint_t}^{coap_context_t}^vSCi^{coap_queue_t}Q[8C]Q^{coap_pdu_t}QQQQQ*Q*Q^vI{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}IidddIddddCddI[32{?=SdC}]}16l
+ ___block_descriptor_48_e8_32s40bs_e862_v24?0^{coap_context_t=[6S]^{coap_resource_t}^{coap_resource_t}^{coap_async_state_t}Q^{coap_queue_t}^{coap_endpoint_t}^{coap_session_t}^?^?^?^?^?^?^?^?^?^?^v*Q*QIIIII^v}8^{coap_session_t=CCCIII{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}}^{coap_endpoint_t}^{coap_context_t}^vSCi^{coap_queue_t}Q[8C]Q^{coap_pdu_t}QQQQQ*Q*Q^vI{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}IidddIddddCddI[32{?=SdC}]}16l
+ ___block_descriptor_48_e8_32s40s_e28_v32?0"NSOperation"8Q16^B24l
+ ___block_descriptor_48_e8_32w_e8_v12?0B8l
+ ___block_descriptor_49_e8_32bs40w_e17_v16?0"NSError"8l
+ ___block_descriptor_49_e8_32s40bs_e17_v16?0"NSError"8l
+ ___block_descriptor_50_e8_32s40bs_e5_v8?0l
+ ___block_descriptor_50_e8_32s40s_e5_v8?0l
+ ___block_descriptor_50_e8_32w_e5_v8?0l
+ ___block_descriptor_51_e8_32s40s_e17_v16?0"NSError"8l
+ ___block_descriptor_56_e8_32bs40w48w_e5_v8?0l
+ ___block_descriptor_56_e8_32s40r48r_e69_v32?0"HAP2AccessoryServerDiscoveryBonjourBrowseResultTuple"8Q16^B24l
+ ___block_descriptor_56_e8_32s40s48bs_e862_v24?0^{coap_context_t=[6S]^{coap_resource_t}^{coap_resource_t}^{coap_async_state_t}Q^{coap_queue_t}^{coap_endpoint_t}^{coap_session_t}^?^?^?^?^?^?^?^?^?^?^v*Q*QIIIII^v}8^{coap_session_t=CCCIII{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}}^{coap_endpoint_t}^{coap_context_t}^vSCi^{coap_queue_t}Q[8C]Q^{coap_pdu_t}QQQQQ*Q*Q^vI{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}IidddIddddCddI[32{?=SdC}]}16l
+ ___block_descriptor_56_e8_32s40s48r_e72_"HAP2AccessoryServerIPCacheData"16?0"HAP2AccessoryServerIPCacheData"8l
+ ___block_descriptor_56_e8_32s40s48s_e17_v16?0"NSError"8l
+ ___block_descriptor_56_e8_32s40s48w_e20_v20?0B8"NSError"12l
+ ___block_descriptor_56_e8_32s40s_e72_"HAP2AccessoryServerIPCacheData"16?0"HAP2AccessoryServerIPCacheData"8l
+ ___block_descriptor_57_e8_32s40s48r_e45_v32?0"HAP2TLVParamServiceSignature"8Q16^B24l
+ ___block_descriptor_57_e8_32s40s48r_e52_v32?0"HAP2TLVParamCharacteristicSignature"8Q16^B24l
+ ___block_descriptor_58_e8_32s40n9_8_8_s0_s8_e5_v8?0l
+ ___block_descriptor_58_e8_32s40s48s_e5_v8?0l
+ ___block_descriptor_58_e8_32s40s48w_e5_v8?0l
+ ___block_descriptor_59_e8_32s40s48s_e17_v16?0"NSError"8l
+ ___block_descriptor_64_e8_32bs40r48r56r_e5_v8?0l
+ ___block_descriptor_64_e8_32bs40r48w_e5_v8?0l
+ ___block_descriptor_64_e8_32bs40w_e5_v8?0l
+ ___block_descriptor_64_e8_32s40r48r_e5_v8?0l
+ ___block_descriptor_64_e8_32s40s48bs_e31_v28?0"NSData"8S16"NSError"20l
+ ___block_descriptor_65_e8_32s40s48bs56w_e20_v20?0B8"NSError"12l
+ ___block_descriptor_71_e8_32s40s48s_e716_v24?0"HAP2CoAPClient"8^{coap_session_t=CCCIII{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}}^{coap_endpoint_t}^{coap_context_t}^vSCi^{coap_queue_t}Q[8C]Q^{coap_pdu_t}QQQQQ*Q*Q^vI{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}IidddIddddCddI[32{?=SdC}]}16l
+ ___block_descriptor_72_e8_32s40s48s56s_e5_v8?0l
+ ___block_descriptor_74_e8_32s40s48s56bs_e5_v8?0l
+ ___block_descriptor_74_e8_32s40s48s56s_e28_v24?0"NSData"8"NSError"16l
+ ___block_descriptor_75_e8_32s40s48s56s64w_e22_v16?0"NSDictionary"8l
+ ___block_descriptor_81_e8_32s40s48r56r64r_e5_v8?0l
+ ___block_descriptor_82_e8_32s40s48s56w_e5_v8?0l
+ ___block_descriptor_83_e8_32s40s48s56s64bs_e5_v8?0l
+ ___block_descriptor_83_e8_32s40s48s56s64s72w_e5_v8?0l
+ ___copy_helper_block_e8_32b40r48r56r
+ ___copy_helper_block_e8_32b40r48w
+ ___copy_helper_block_e8_32b40w48w
+ ___copy_helper_block_e8_32s40n9_8_8_s0_s8
+ ___copy_helper_block_e8_32s40s48r56r64r
+ ___copy_helper_block_e8_32s40s48s56s64r72r80r88r
+ ___copy_helper_block_e8_32s40s48s56s64s72r80r88r96r104w
+ ___copy_helper_block_e8_32s40s48s56s64s72s80r88r96r104r112w
+ ___copy_helper_block_e8_32s40s48s56s64s72w
+ ___copy_helper_block_e8_32s40s48s56s64w
+ ___destroy_helper_block_e8_32s40n7_8_s0_s8
+ ___destroy_helper_block_e8_32s40s48r56r64r
+ ___destroy_helper_block_e8_32s40s48s56s64r72r80r88r
+ ___destroy_helper_block_e8_32s40s48s56s64s72r80r88r96r104w
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80r88r96r104r112w
+ ___destroy_helper_block_e8_32s40s48s56s64s72w
+ ___removeDependencyOnCompletion_block_invoke
+ __swift_closure_destructor.198Tm
+ __xpc_type_dictionary
+ __xpc_type_string
+ _associated conformance 7CoreHAP17PairSetupTLVErrorOSHAASQ
+ _associated conformance So27HAP2CoAPAccessoryTransportsVs10SetAlgebraSCSQ
+ _associated conformance So27HAP2CoAPAccessoryTransportsVs10SetAlgebraSCs25ExpressibleByArrayLiteral
+ _associated conformance So27HAP2CoAPAccessoryTransportsVs9OptionSetSCSY
+ _associated conformance So27HAP2CoAPAccessoryTransportsVs9OptionSetSCs0F7Algebra
+ _coapPingHandler
+ _coap_cancel_session_messages
+ _coap_session_send_ping
+ _dispatch_activate
+ _dispatch_assert_queue_not$V2
+ _dispatch_queue_attr_make_with_qos_class
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dnssd_getaddrinfo_activate
+ _dnssd_getaddrinfo_create
+ _dnssd_getaddrinfo_invalidate
+ _dnssd_getaddrinfo_result_get_address
+ _dnssd_getaddrinfo_result_get_type
+ _dnssd_getaddrinfo_set_event_handler
+ _dnssd_getaddrinfo_set_flags
+ _dnssd_getaddrinfo_set_hostname
+ _dnssd_getaddrinfo_set_interface_index
+ _dnssd_getaddrinfo_set_protocols
+ _dnssd_getaddrinfo_set_queue
+ _dnssd_getaddrinfo_set_result_handler
+ _get_time_now
+ _objc_msgSend$ECDSAKeyForAccessoryName:error:
+ _objc_msgSend$_acquireDNSContextOwnership
+ _objc_msgSend$_addressToCIDR:withNetmask:
+ _objc_msgSend$_applyCachedIP:transportType:notifySubscriber:seedAgingClock:
+ _objc_msgSend$_applyCallerQoSToOperations:
+ _objc_msgSend$_armInitialCacheGracePeriodTimerIfNeeded
+ _objc_msgSend$_armPTRRevalidationWindow
+ _objc_msgSend$_buildActiveDeviceIDsSet
+ _objc_msgSend$_cancelPTRRevalidationWindow
+ _objc_msgSend$_cancelResolver
+ _objc_msgSend$_claimStateChangeCompletionForGeneration:
+ _objc_msgSend$_classifyTransportType:
+ _objc_msgSend$_clearAllAddresses
+ _objc_msgSend$_clearECDSAStateForGeneration:
+ _objc_msgSend$_closeSessionIfConnectedIPAddressStaleForTransport:
+ _objc_msgSend$_coapAddressFromGAIResult:outAddress:
+ _objc_msgSend$_controllerUnchecked
+ _objc_msgSend$_copyDelegates
+ _objc_msgSend$_createSecuritySessionFromECDSASessionForGeneration:
+ _objc_msgSend$_currentStateChangeGeneration
+ _objc_msgSend$_didDiscoverAccessory:fromMDNSEvent:completion:
+ _objc_msgSend$_ecdsaKeyPairSetupRefusalError
+ _objc_msgSend$_evaluateCacheMissCancelIfNeededWithLivePrimaryCount:
+ _objc_msgSend$_eventQueue
+ _objc_msgSend$_executeCacheMissCancel
+ _objc_msgSend$_fetchMeshLocalPrefixFromXPC
+ _objc_msgSend$_fireRevalidationSweep
+ _objc_msgSend$_handleECDSASessionFailure:generation:
+ _objc_msgSend$_handleGetaddrinfoEvent:error:
+ _objc_msgSend$_handleGetaddrinfoResults:count:
+ _objc_msgSend$_handleLiveResolverUpdate
+ _objc_msgSend$_handlePipelineError:
+ _objc_msgSend$_handlePipelineUpdate:
+ _objc_msgSend$_handleProbeCompletion:forKeepAliveTransport:
+ _objc_msgSend$_handleResolveCallbackWithError:hostname:port:
+ _objc_msgSend$_handleTimerFireForTransport:
+ _objc_msgSend$_haveAllTransportsHitFailureThreshold
+ _objc_msgSend$_initializeFromCachedRecord:deviceID:
+ _objc_msgSend$_maybeFireOffQueueCacheMissCancelForAddresses:
+ _objc_msgSend$_parseCharacteristics:isMultiTransportAccessory:error:
+ _objc_msgSend$_performAuditPass
+ _objc_msgSend$_performAuditPassOnQueueWithActiveDeviceIDs:
+ _objc_msgSend$_recordAddedAddress:
+ _objc_msgSend$_recordRemovedAddress:
+ _objc_msgSend$_refreshIPAddresses
+ _objc_msgSend$_reinitializeFromCachedRecordsAfterCoordinatorsStarted
+ _objc_msgSend$_releaseDNSContextOwnership
+ _objc_msgSend$_resetIPsTriedThisSession
+ _objc_msgSend$_resetInitialCacheOnlyStopgapState
+ _objc_msgSend$_resolveAddress
+ _objc_msgSend$_restampWorkingSetWithResolvedPort
+ _objc_msgSend$_restartPipelineOnQueue
+ _objc_msgSend$_restoreCachedAccessoryServersIfNeeded
+ _objc_msgSend$_seedCachedIP:transportType:
+ _objc_msgSend$_sendEndpointRegistration
+ _objc_msgSend$_sendMultiTransportRequest:path:
+ _objc_msgSend$_sendWiFiEndpointRegistration
+ _objc_msgSend$_setHasDiscoveryAdvertisementLockOnly:
+ _objc_msgSend$_setHasThreadAdvertisement:
+ _objc_msgSend$_setHasWiFiAdvertisement:
+ _objc_msgSend$_sharedThreadClient
+ _objc_msgSend$_shouldRegisterEndpoint
+ _objc_msgSend$_startGetaddrinfoForHostname:
+ _objc_msgSend$_startPipelineOnQueue
+ _objc_msgSend$_startResolverIfNeeded
+ _objc_msgSend$_takeNextPrimaryIPToTry
+ _objc_msgSend$_takeNextSecondaryIPToTry
+ _objc_msgSend$_tearDownPipeline
+ _objc_msgSend$abandonedRequestCount
+ _objc_msgSend$accessory:didUpdateLocalEndpoints:
+ _objc_msgSend$accessoryDeviceIPAddressWithSerializedData:
+ _objc_msgSend$accessoryInfoWithDeviceID:rawDiscoveryInfo:
+ _objc_msgSend$accessoryServer:didUpdateLocalEndpoints:
+ _objc_msgSend$activeHardwareFaults
+ _objc_msgSend$addConcurrentBlock:qos:
+ _objc_msgSend$addDelegate:
+ _objc_msgSend$addressResolverFactory
+ _objc_msgSend$allCachedRecords
+ _objc_msgSend$applyResolverAddresses:completion:
+ _objc_msgSend$arrayByAddingObject:
+ _objc_msgSend$attachCacheSubscriber:
+ _objc_msgSend$attachDelegate:
+ _objc_msgSend$attachSelfAsCacheSubscriberOnResolver:
+ _objc_msgSend$audioOnlyFailureCount
+ _objc_msgSend$auditScheduler
+ _objc_msgSend$authenticationErrorCount
+ _objc_msgSend$averageCPUUtilization
+ _objc_msgSend$averageDeviceTemperature
+ _objc_msgSend$averageSystemMemoryUtilization
+ _objc_msgSend$batteryPercentage
+ _objc_msgSend$beaconLostCount
+ _objc_msgSend$beaconRxCount
+ _objc_msgSend$beaconRxInterval
+ _objc_msgSend$becameEmptyAt
+ _objc_msgSend$bluetoothVersion
+ _objc_msgSend$broadcast
+ _objc_msgSend$brownOutResetBootCount
+ _objc_msgSend$cachedAccessoryKeyType
+ _objc_msgSend$cachedIPDidUpdate:transportType:
+ _objc_msgSend$cachedIPDidUpdate:transportType:forDeviceID:
+ _objc_msgSend$cachedPrimary
+ _objc_msgSend$cachedPrimaryData
+ _objc_msgSend$cachedSecondary
+ _objc_msgSend$cachedSecondaryData
+ _objc_msgSend$checkConnectedIPAddressStaleOnTransport:completion:
+ _objc_msgSend$chmAccessoryRebootCompleted
+ _objc_msgSend$chmAccessoryRebootDurationToRecovery
+ _objc_msgSend$clientDidReceivePing:
+ _objc_msgSend$closeSessionWithCompletion:
+ _objc_msgSend$configurationInfo
+ _objc_msgSend$configureKeepAliveListener:
+ _objc_msgSend$connectionCount
+ _objc_msgSend$connectionErrorCount
+ _objc_msgSend$connectionStatus
+ _objc_msgSend$connectivityMonitorBootCount
+ _objc_msgSend$containsHAPPortUnreachableError
+ _objc_msgSend$contributingSensor
+ _objc_msgSend$controllerKeyForDeviceId:error:
+ _objc_msgSend$controllerKeyForECDSAKeyAccessory:error:
+ _objc_msgSend$countForObject:
+ _objc_msgSend$createResolverWithDeviceID:serviceName:
+ _objc_msgSend$createResolverWithServiceName:serviceType:serviceDomain:queue:updateHandler:errorHandler:
+ _objc_msgSend$currentAddresses
+ _objc_msgSend$currentPTRs
+ _objc_msgSend$currentPowerSource
+ _objc_msgSend$currentResolverSnapshot
+ _objc_msgSend$dataStreamPeerAddressWithCompletion:
+ _objc_msgSend$dateProvider
+ _objc_msgSend$deferAgingClockIfRunning
+ _objc_msgSend$deliverRacingResult:forAccessoryIdentifier:messageID:
+ _objc_msgSend$deriveEncryptionForDataStreamWithKeySalt:completionHandler:
+ _objc_msgSend$detachDelegate:
+ _objc_msgSend$deviceRebootDelay
+ _objc_msgSend$deviceRebootEnable
+ _objc_msgSend$didChangeThreadAdvertisement:
+ _objc_msgSend$didChangeWiFiAdvertisement:
+ _objc_msgSend$didReceiveHeartbeatOnTransport:
+ _objc_msgSend$didReceivePingInSession:messageID:
+ _objc_msgSend$disconnectWithCompletion:
+ _objc_msgSend$disconnectionCount
+ _objc_msgSend$disconnectionDuration
+ _objc_msgSend$disconnectionErrorCount
+ _objc_msgSend$dnsResolver
+ _objc_msgSend$durationOnBatteryPower
+ _objc_msgSend$durationRemainingOnBatteryPower
+ _objc_msgSend$entries
+ _objc_msgSend$errorID
+ _objc_msgSend$expectedBootCount
+ _objc_msgSend$forceRefreshMeshLocalPrefix
+ _objc_msgSend$forceSessionExpired
+ _objc_msgSend$foreignPairVerifySession
+ _objc_msgSend$fragmentFailureCount
+ _objc_msgSend$fragmentRetriedCount
+ _objc_msgSend$fragmentSuccessCount
+ _objc_msgSend$gatewayIPv4Address
+ _objc_msgSend$gatewayIPv6Address
+ _objc_msgSend$gatewayMacAddress
+ _objc_msgSend$getCurrentNetworkInterfaces
+ _objc_msgSend$getHH2ControllerKeyWithIdentifier:allowBackupRestore:
+ _objc_msgSend$getLocalEndpointWithCompletion:
+ _objc_msgSend$getLocalIPv4EndpointWithCompletion:
+ _objc_msgSend$getLocalIPv6EndpointWithCompletion:
+ _objc_msgSend$getProperty:output:
+ _objc_msgSend$getRTTStatisticsWithCompletion:
+ _objc_msgSend$getSelfAddress:maxLength:outLength:
+ _objc_msgSend$hapSessionLossCount
+ _objc_msgSend$hardwareFaultBootCount
+ _objc_msgSend$hardwareWatchdogResetBootCount
+ _objc_msgSend$hasArmedCacheOnlyLatch
+ _objc_msgSend$hasCurrentPTRForDeviceID:
+ _objc_msgSend$hasDiscoveryAdvertisementForAccessoryWithID:
+ _objc_msgSend$hasMissedHeartbeat
+ _objc_msgSend$hasMissedHeartbeatForTransport:
+ _objc_msgSend$hasQueuedCloseOperation
+ _objc_msgSend$hasRegisteredEndpoint
+ _objc_msgSend$hasSeededSinceResolverAttach
+ _objc_msgSend$hasThreadAdvertisement
+ _objc_msgSend$hasThreadAdvertisementForAccessoryWithID:
+ _objc_msgSend$hasWiFiAdvertisement
+ _objc_msgSend$hasWiFiAdvertisementForAccessoryWithID:
+ _objc_msgSend$heapHighwaterCount
+ _objc_msgSend$heapOverflowBootCount
+ _objc_msgSend$heapOverflowCount
+ _objc_msgSend$hwExceptionCount
+ _objc_msgSend$init:
+ _objc_msgSend$initFromDictionary:deviceID:
+ _objc_msgSend$initWithBluetoothVersion:rssi:txPowerLevel:packetRxCount:packetTxCount:packetRxErrorCount:packetTxErrorCount:overrunCount:connectionStatus:connectionCount:connectionErrorCount:disconnectionCount:disconnectionErrorCount:hwExceptionCount:
+ _objc_msgSend$initWithConfigurationEntries:workQueue:timerProvider:dateProvider:
+ _objc_msgSend$initWithContributingSensor:
+ _objc_msgSend$initWithDeviceID:cachedPrimaryData:cachedSecondaryData:configurationInfo:
+ _objc_msgSend$initWithDeviceID:serviceName:managerQueue:pipelineFactory:
+ _objc_msgSend$initWithDeviceRebootEnable:threadRecoveryConfiguration:wiFiRecoveryConfiguration:recoveryStaggerDelay:deviceRebootDelay:threadPingTestCount:threadPingTestInterval:threadRestartMinInterval:wiFiPingTestCount:wiFiPingTestInterval:wiFiRestartMinInterval:
+ _objc_msgSend$initWithEntries:
+ _objc_msgSend$initWithErrorID:count:
+ _objc_msgSend$initWithFragmentSuccessCount:fragmentFailureCount:fragmentRetriedCount:networkErrorCount:authenticationErrorCount:serverReturnedErrorCount:localErrorCount:playlistFailureCount:latencyCount250ms:latencyCount500ms:latencyCount1000ms:latencyCount2000ms:latencyCount3750ms:latencyCountOver3750ms:sessionSuccessCount:partialSuccessCount:sessionFailureCount:uploadWithoutResidentResponseCount:audioOnlyFailureCount:abandonedRequestCount:
+ _objc_msgSend$initWithGatewayMacAddress:gatewayIPv4Address:gatewayIPv6Address:subnetMask:bssid:wifiVersion:channelNumber:rssi:connectionStatus:disconnectionCount:disconnectionDuration:beaconRxCount:beaconRxInterval:beaconLostCount:ipAddressList:packetMulticastRxCount:packetMulticastRxErrorCount:packetMulticastTxCount:packetMulticastTxErrorCount:packetUnicastRxCount:packetUnicastRxErrorCount:packetUnicastTxCount:packetUnicastTxErrorCount:txPacketCount:txPacketErrorCount:rxPacketCount:rxPacketErrorCount:hwExceptionCount:wifiRestartCount:
+ _objc_msgSend$initWithInteger:
+ _objc_msgSend$initWithName:browser:
+ _objc_msgSend$initWithPreferredWiFiList:
+ _objc_msgSend$initWithPrimary:secondary:
+ _objc_msgSend$initWithPrimary:secondary:cachedPrimary:cachedSecondary:
+ _objc_msgSend$initWithQueue:updateHandler:errorHandler:
+ _objc_msgSend$initWithSFrameEnabled:SFrameConfiguration:
+ _objc_msgSend$initWithSensorUUID:
+ _objc_msgSend$initWithSessionIdentifier:viewerParticipantID:viewerNegotiationBlob:operation:
+ _objc_msgSend$initWithStackHighwaterCount:lastStackHighwaterTaskName:heapHighwaterCount:lastHeapHighwaterTaskName:stackOverflowCount:lastStackOverflowTaskName:heapOverflowCount:lastHeapOverflowTaskName:averageSystemMemoryUtilization:peakSystemMemoryUtilization:systemMemoryPressureCount:processCriticalMemoryCount:lastProcessCriticalMemoryName:averageCPUUtilization:peakCPUUtilization:taskDeadlineMissCount:totalTasksScheduledCount:maxTaskReadyQueueSize:loadAverage:nonVolatileMemoryWriteCount:nonVolatileMemoryReadCount:nonVolatileMemoryWriteErrorCount:nonVolatileMemoryReadErrorCount:nonVolatileMemoryUtilization:
+ _objc_msgSend$initWithStartTime:
+ _objc_msgSend$initWithSupportedPowerSources:currentPowerSource:durationOnBatteryPower:durationRemainingOnBatteryPower:batteryPercentage:
+ _objc_msgSend$initWithSystemUptime:systemBootCount:expectedBootCount:systemCrashCount:systemHangCount:lastBootReason:activeHardwareFaults:
+ _objc_msgSend$initWithTemperatureLimitViolationCount:temperatureLimitViolationDuration:minimumDeviceTemperature:maximumDeviceTemperature:averageDeviceTemperature:
+ _objc_msgSend$initWithTransportType:maximumInterval:
+ _objc_msgSend$initWithTransportType:minimumInterval:maximumInterval:
+ _objc_msgSend$initWithTransportType:minimumInterval:maximumInterval:minimumRange:
+ _objc_msgSend$initWithUnsignedInteger:
+ _objc_msgSend$initWithUnspecifiedBootCount:powerOnBootCount:brownOutResetBootCount:softwareWatchdogResetBootCount:hardwareWatchdogResetBootCount:softwareUpdateCompletedBootCount:softwareResetBootCount:softwareExceptionBootCount:hardwareFaultBootCount:stackOverflowBootCount:heapOverflowBootCount:temperatureLimitBootCount:connectivityMonitorBootCount:
+ _objc_msgSend$initWithWifiTransportLossCount:wifiRecoveryAttemptCount:wifiRestartCount:wifiFirstRestartRecoveryTime:wifiFirstRestartCompleted:wifiFirstRestartConnectivityState:threadTransportLossCount:threadRecoveryAttemptCount:threadRestartCount:threadFirstRestartRecoveryTime:threadFirstRestartCompleted:threadFirstRestartConnectivityState:hapSessionLossCount:chmAccessoryRebootDurationToRecovery:chmAccessoryRebootCompleted:
+ _objc_msgSend$initialCacheGracePeriodTimer
+ _objc_msgSend$initialConnectionAttemptStartedAt
+ _objc_msgSend$initializePairedAccessoryServerFromCachedInfo:
+ _objc_msgSend$ipAddressList
+ _objc_msgSend$ipCache
+ _objc_msgSend$isAddress:inNetwork:
+ _objc_msgSend$isEqualToDictionary:
+ _objc_msgSend$isForWriting
+ _objc_msgSend$isIPv6
+ _objc_msgSend$isKnownToSystemCommissioner
+ _objc_msgSend$isThreadIPv6Address:fromInterfaces:
+ _objc_msgSend$isThreadInterface:
+ _objc_msgSend$keepAliveListener:didMissHeartbeatOnTransport:expectedInterval:timeSinceLastHeartbeat:allTransportsMissed:
+ _objc_msgSend$keepAliveListener:didReceiveHeartbeatOnTransport:
+ _objc_msgSend$keepAliveListenerDidCompleteIPPortPairCheck:
+ _objc_msgSend$lastBootReason
+ _objc_msgSend$lastCompletedMessageID
+ _objc_msgSend$lastHeapHighwaterTaskName
+ _objc_msgSend$lastHeapOverflowTaskName
+ _objc_msgSend$lastHeartbeatTime
+ _objc_msgSend$lastKnownAccessoryInfoByServiceKey
+ _objc_msgSend$lastMessageID
+ _objc_msgSend$lastObservedHasAdvertisement
+ _objc_msgSend$lastProcessCriticalMemoryName
+ _objc_msgSend$lastStackHighwaterTaskName
+ _objc_msgSend$lastStackOverflowTaskName
+ _objc_msgSend$latencyCount1000ms
+ _objc_msgSend$latencyCount2000ms
+ _objc_msgSend$latencyCount250ms
+ _objc_msgSend$latencyCount3750ms
+ _objc_msgSend$latencyCount500ms
+ _objc_msgSend$latencyCountOver3750ms
+ _objc_msgSend$loadAverage
+ _objc_msgSend$localErrorCount
+ _objc_msgSend$localPairingIdentityForDeviceID:error:
+ _objc_msgSend$localPairingIdentityForPairingDriver:error:
+ _objc_msgSend$localPairingIdentityForSecureTransport:error:
+ _objc_msgSend$managerQueue
+ _objc_msgSend$maxTaskReadyQueueSize
+ _objc_msgSend$maximumDeviceTemperature
+ _objc_msgSend$maximumInterval
+ _objc_msgSend$mergeWithNewlyDiscoveredPairedAccessoryServer:resolver:
+ _objc_msgSend$minimumDeviceTemperature
+ _objc_msgSend$minimumInterval
+ _objc_msgSend$minimumRange
+ _objc_msgSend$missCheckTimer
+ _objc_msgSend$mutateCachedRecordForDeviceID:usingBlock:
+ _objc_msgSend$networkErrorCount
+ _objc_msgSend$newQueueWithLabel:attributes:target:
+ _objc_msgSend$nonVolatileMemoryReadCount
+ _objc_msgSend$nonVolatileMemoryReadErrorCount
+ _objc_msgSend$nonVolatileMemoryUtilization
+ _objc_msgSend$nonVolatileMemoryWriteCount
+ _objc_msgSend$nonVolatileMemoryWriteErrorCount
+ _objc_msgSend$noteBonjourAdvertisementUpdatedForDeviceID:rawDiscoveryInfo:
+ _objc_msgSend$noteBrowsedPTRAddForDeviceID:serviceName:
+ _objc_msgSend$noteBrowsedPTRRemoveForDeviceID:
+ _objc_msgSend$noteResolverReapedForDeviceID:
+ _objc_msgSend$overrunCount
+ _objc_msgSend$packetMulticastRxCount
+ _objc_msgSend$packetMulticastRxErrorCount
+ _objc_msgSend$packetMulticastTxCount
+ _objc_msgSend$packetMulticastTxErrorCount
+ _objc_msgSend$packetRxCount
+ _objc_msgSend$packetRxErrorCount
+ _objc_msgSend$packetTxCount
+ _objc_msgSend$packetTxErrorCount
+ _objc_msgSend$packetUnicastRxCount
+ _objc_msgSend$packetUnicastRxErrorCount
+ _objc_msgSend$packetUnicastTxCount
+ _objc_msgSend$packetUnicastTxErrorCount
+ _objc_msgSend$pairVerifyDidCompleteOnIPAddress:transportType:
+ _objc_msgSend$pairVerifyDidFailOnIPAddress:transportType:error:
+ _objc_msgSend$pairingDriver:saveRemoteECDSAPairingKey:forAccessoryIdentifier:error:
+ _objc_msgSend$pairingDriver:saveRemotePairingIdentity:error:
+ _objc_msgSend$partialSuccessCount
+ _objc_msgSend$peakCPUUtilization
+ _objc_msgSend$peakSystemMemoryUtilization
+ _objc_msgSend$performAuditPassWithActiveDeviceIDs:
+ _objc_msgSend$performHealthCheck
+ _objc_msgSend$pipelineFactory
+ _objc_msgSend$playlistFailureCount
+ _objc_msgSend$powerOnBootCount
+ _objc_msgSend$preferredWiFiList
+ _objc_msgSend$primary
+ _objc_msgSend$primaryEffectiveListIsCacheOnly
+ _objc_msgSend$primaryIPsTriedThisSession
+ _objc_msgSend$primaryOpenInFlight
+ _objc_msgSend$processCriticalMemoryCount
+ _objc_msgSend$publicKeyForIdentifier:error:
+ _objc_msgSend$racingTriggerReason
+ _objc_msgSend$readLocalEndpointsWithHandler:
+ _objc_msgSend$recoveryStaggerDelay
+ _objc_msgSend$removeCachedRecordForDeviceID:
+ _objc_msgSend$removeDelegate:
+ _objc_msgSend$resetHeartbeatTimestamps
+ _objc_msgSend$resolveTimeoutTimer
+ _objc_msgSend$resolver:didUpdateAddresses:
+ _objc_msgSend$resolverForDeviceID:
+ _objc_msgSend$resolverRegistry
+ _objc_msgSend$resolverRestartTimer
+ _objc_msgSend$restartKeepAliveListener
+ _objc_msgSend$revalidationTimer
+ _objc_msgSend$rxPacketCount
+ _objc_msgSend$rxPacketErrorCount
+ _objc_msgSend$saveECDSAKey:forAccessoryName:error:
+ _objc_msgSend$savePublicKey:forIdentifier:error:
+ _objc_msgSend$secondary
+ _objc_msgSend$secondaryAddressList
+ _objc_msgSend$secondaryCoAPClient
+ _objc_msgSend$secondaryIPsTriedThisSession
+ _objc_msgSend$secureTransport:didChangeThreadAdvertisement:
+ _objc_msgSend$secureTransport:didChangeWiFiAdvertisement:
+ _objc_msgSend$secureTransport:didReceiveHeartbeatOnTransport:
+ _objc_msgSend$secureTransport:ecdsaLongTermPublicKeyForPeerWithIdentifier:error:
+ _objc_msgSend$secureTransport:localPairingIdentityForECDSAKeyPairSetupSession:error:
+ _objc_msgSend$secureTransport:pairVerifyDidCompleteOnIPAddress:transportType:
+ _objc_msgSend$secureTransport:pairVerifyDidFailOnIPAddress:transportType:error:
+ _objc_msgSend$secureTransport:remotePairingIdentityForDeviceID:error:
+ _objc_msgSend$secureTransportCurrentResolverSnapshot:
+ _objc_msgSend$securedClient
+ _objc_msgSend$selfAddress
+ _objc_msgSend$sendProbeOnTransport:completion:
+ _objc_msgSend$sendProbeWithCompletion:
+ _objc_msgSend$sendRequestWithMethod:path:payload:messageID:dscpPriority:completion:
+ _objc_msgSend$sentOverThread
+ _objc_msgSend$sentOverWiFi
+ _objc_msgSend$serializedData
+ _objc_msgSend$serverReturnedErrorCount
+ _objc_msgSend$sessionFailureCount
+ _objc_msgSend$sessionSuccessCount
+ _objc_msgSend$setAbandonedRequestCount:
+ _objc_msgSend$setAccessoryTransports:
+ _objc_msgSend$setActiveHardwareFaults:
+ _objc_msgSend$setAudioOnlyFailureCount:
+ _objc_msgSend$setAuthenticationErrorCount:
+ _objc_msgSend$setAverageCPUUtilization:
+ _objc_msgSend$setAverageDeviceTemperature:
+ _objc_msgSend$setAverageSystemMemoryUtilization:
+ _objc_msgSend$setBatteryPercentage:
+ _objc_msgSend$setBeaconLostCount:
+ _objc_msgSend$setBeaconRxCount:
+ _objc_msgSend$setBeaconRxInterval:
+ _objc_msgSend$setBluetoothVersion:
+ _objc_msgSend$setBrownOutResetBootCount:
+ _objc_msgSend$setBssid:
+ _objc_msgSend$setCachedAccessoryKeyType:
+ _objc_msgSend$setChannelNumber:
+ _objc_msgSend$setChmAccessoryRebootCompleted:
+ _objc_msgSend$setChmAccessoryRebootDurationToRecovery:
+ _objc_msgSend$setClientEventsOn
+ _objc_msgSend$setCoapMessageID:
+ _objc_msgSend$setConnectionCount:
+ _objc_msgSend$setConnectionErrorCount:
+ _objc_msgSend$setConnectionStatus:
+ _objc_msgSend$setConnectivityMonitorBootCount:
+ _objc_msgSend$setContributingSensor:
+ _objc_msgSend$setCount:
+ _objc_msgSend$setCurrentPowerSource:
+ _objc_msgSend$setDeviceRebootDelay:
+ _objc_msgSend$setDeviceRebootEnable:
+ _objc_msgSend$setDisconnectionCount:
+ _objc_msgSend$setDisconnectionDuration:
+ _objc_msgSend$setDisconnectionErrorCount:
+ _objc_msgSend$setDnsResolver:
+ _objc_msgSend$setDurationOnBatteryPower:
+ _objc_msgSend$setDurationRemainingOnBatteryPower:
+ _objc_msgSend$setEntries:
+ _objc_msgSend$setErrorID:
+ _objc_msgSend$setEventHandler:EventBlock:dqueue:
+ _objc_msgSend$setExpectedBootCount:
+ _objc_msgSend$setForeignPairVerifySession:
+ _objc_msgSend$setFragmentFailureCount:
+ _objc_msgSend$setFragmentRetriedCount:
+ _objc_msgSend$setFragmentSuccessCount:
+ _objc_msgSend$setGatewayIPv4Address:
+ _objc_msgSend$setGatewayIPv6Address:
+ _objc_msgSend$setGatewayMacAddress:
+ _objc_msgSend$setHapSessionLossCount:
+ _objc_msgSend$setHardwareFaultBootCount:
+ _objc_msgSend$setHardwareWatchdogResetBootCount:
+ _objc_msgSend$setHasMissedHeartbeat:
+ _objc_msgSend$setHasRegisteredEndpoint:
+ _objc_msgSend$setHasSeededSinceResolverAttach:
+ _objc_msgSend$setHasThreadAdvertisement:
+ _objc_msgSend$setHasWiFiAdvertisement:
+ _objc_msgSend$setHeapHighwaterCount:
+ _objc_msgSend$setHeapOverflowBootCount:
+ _objc_msgSend$setHeapOverflowCount:
+ _objc_msgSend$setHwExceptionCount:
+ _objc_msgSend$setIPCache:
+ _objc_msgSend$setInitialCacheGracePeriodTimer:
+ _objc_msgSend$setInitialConnectionAttemptStartedAt:
+ _objc_msgSend$setIpAddressList:
+ _objc_msgSend$setIsRunning:
+ _objc_msgSend$setIsWrite:
+ _objc_msgSend$setLastBootReason:
+ _objc_msgSend$setLastHeapHighwaterTaskName:
+ _objc_msgSend$setLastHeapOverflowTaskName:
+ _objc_msgSend$setLastHeartbeatTime:
+ _objc_msgSend$setLastMessageID:
+ _objc_msgSend$setLastObservedHasAdvertisement:
+ _objc_msgSend$setLastPairSetupWasSpake2:
+ _objc_msgSend$setLastProcessCriticalMemoryName:
+ _objc_msgSend$setLastStackHighwaterTaskName:
+ _objc_msgSend$setLastStackOverflowTaskName:
+ _objc_msgSend$setLatencyCount1000ms:
+ _objc_msgSend$setLatencyCount2000ms:
+ _objc_msgSend$setLatencyCount250ms:
+ _objc_msgSend$setLatencyCount3750ms:
+ _objc_msgSend$setLatencyCount500ms:
+ _objc_msgSend$setLatencyCountOver3750ms:
+ _objc_msgSend$setLivePairedAccessoryServers:
+ _objc_msgSend$setLoadAverage:
+ _objc_msgSend$setLocalErrorCount:
+ _objc_msgSend$setMaxTaskReadyQueueSize:
+ _objc_msgSend$setMaximumDeviceTemperature:
+ _objc_msgSend$setMaximumInterval:
+ _objc_msgSend$setMinimumDeviceTemperature:
+ _objc_msgSend$setMinimumInterval:
+ _objc_msgSend$setMinimumRange:
+ _objc_msgSend$setMissCheckTimer:
+ _objc_msgSend$setNetworkErrorCount:
+ _objc_msgSend$setNonVolatileMemoryReadCount:
+ _objc_msgSend$setNonVolatileMemoryReadErrorCount:
+ _objc_msgSend$setNonVolatileMemoryUtilization:
+ _objc_msgSend$setNonVolatileMemoryWriteCount:
+ _objc_msgSend$setNonVolatileMemoryWriteErrorCount:
+ _objc_msgSend$setObject:atIndexedSubscript:
+ _objc_msgSend$setOverrunCount:
+ _objc_msgSend$setPacketMulticastRxCount:
+ _objc_msgSend$setPacketMulticastRxErrorCount:
+ _objc_msgSend$setPacketMulticastTxCount:
+ _objc_msgSend$setPacketMulticastTxErrorCount:
+ _objc_msgSend$setPacketRxCount:
+ _objc_msgSend$setPacketRxErrorCount:
+ _objc_msgSend$setPacketTxCount:
+ _objc_msgSend$setPacketTxErrorCount:
+ _objc_msgSend$setPacketUnicastRxCount:
+ _objc_msgSend$setPacketUnicastRxErrorCount:
+ _objc_msgSend$setPacketUnicastTxCount:
+ _objc_msgSend$setPacketUnicastTxErrorCount:
+ _objc_msgSend$setPartialSuccessCount:
+ _objc_msgSend$setPeakCPUUtilization:
+ _objc_msgSend$setPeakSystemMemoryUtilization:
+ _objc_msgSend$setPendingRevalidationPTRs:
+ _objc_msgSend$setPipelineFactory:
+ _objc_msgSend$setPlaylistFailureCount:
+ _objc_msgSend$setPowerOnBootCount:
+ _objc_msgSend$setPreferredWiFiList:
+ _objc_msgSend$setPrimaryEffectiveListIsCacheOnly:
+ _objc_msgSend$setPrimaryOpenInFlight:
+ _objc_msgSend$setProcessCriticalMemoryCount:
+ _objc_msgSend$setRaceTimeout:
+ _objc_msgSend$setRacingTriggerReason:
+ _objc_msgSend$setRecoveryStaggerDelay:
+ _objc_msgSend$setResolveTimeoutTimer:
+ _objc_msgSend$setResolverRegistry:
+ _objc_msgSend$setResolverRestartTimer:
+ _objc_msgSend$setRevalidationTimer:
+ _objc_msgSend$setRssi:
+ _objc_msgSend$setRxPacketCount:
+ _objc_msgSend$setRxPacketErrorCount:
+ _objc_msgSend$setSecondaryCoAPClient:
+ _objc_msgSend$setSecuredClient:
+ _objc_msgSend$setSentOverThread:
+ _objc_msgSend$setSentOverWiFi:
+ _objc_msgSend$setServerReturnedErrorCount:
+ _objc_msgSend$setSessionFailureCount:
+ _objc_msgSend$setSessionSuccessCount:
+ _objc_msgSend$setShouldAllowECDSAKeyPairSetup:
+ _objc_msgSend$setSoftwareExceptionBootCount:
+ _objc_msgSend$setSoftwareResetBootCount:
+ _objc_msgSend$setSoftwareUpdateCompletedBootCount:
+ _objc_msgSend$setSoftwareWatchdogResetBootCount:
+ _objc_msgSend$setStackHighwaterCount:
+ _objc_msgSend$setStackOverflowBootCount:
+ _objc_msgSend$setStackOverflowCount:
+ _objc_msgSend$setSubnetMask:
+ _objc_msgSend$setSupportedPowerSources:
+ _objc_msgSend$setSupportsKeepAlive:
+ _objc_msgSend$setSupportsThreadTransport:
+ _objc_msgSend$setSupportsWiFiTransport:
+ _objc_msgSend$setSystemBootCount:
+ _objc_msgSend$setSystemCrashCount:
+ _objc_msgSend$setSystemHangCount:
+ _objc_msgSend$setSystemMemoryPressureCount:
+ _objc_msgSend$setSystemUptime:
+ _objc_msgSend$setTaskDeadlineMissCount:
+ _objc_msgSend$setTemperatureLimitBootCount:
+ _objc_msgSend$setTemperatureLimitViolationCount:
+ _objc_msgSend$setTemperatureLimitViolationDuration:
+ _objc_msgSend$setThreadError:
+ _objc_msgSend$setThreadFirstRestartCompleted:
+ _objc_msgSend$setThreadFirstRestartConnectivityState:
+ _objc_msgSend$setThreadFirstRestartRecoveryTime:
+ _objc_msgSend$setThreadPingTestCount:
+ _objc_msgSend$setThreadPingTestInterval:
+ _objc_msgSend$setThreadRecoveryAttemptCount:
+ _objc_msgSend$setThreadRecoveryConfiguration:
+ _objc_msgSend$setThreadResponseLatency:
+ _objc_msgSend$setThreadRestartCount:
+ _objc_msgSend$setThreadRestartMinInterval:
+ _objc_msgSend$setThreadTransportLossCount:
+ _objc_msgSend$setTotalTasksScheduledCount:
+ _objc_msgSend$setTryingInitialCacheOnly:
+ _objc_msgSend$setTxPacketCount:
+ _objc_msgSend$setTxPacketErrorCount:
+ _objc_msgSend$setTxPowerLevel:
+ _objc_msgSend$setUnspecifiedBootCount:
+ _objc_msgSend$setUploadWithoutResidentResponseCount:
+ _objc_msgSend$setWiFiPingTestCount:
+ _objc_msgSend$setWiFiPingTestInterval:
+ _objc_msgSend$setWiFiRecoveryConfiguration:
+ _objc_msgSend$setWiFiRestartMinInterval:
+ _objc_msgSend$setWifiError:
+ _objc_msgSend$setWifiFirstRestartCompleted:
+ _objc_msgSend$setWifiFirstRestartConnectivityState:
+ _objc_msgSend$setWifiFirstRestartRecoveryTime:
+ _objc_msgSend$setWifiRTT:
+ _objc_msgSend$setWifiRecoveryAttemptCount:
+ _objc_msgSend$setWifiResponseLatency:
+ _objc_msgSend$setWifiRestartCount:
+ _objc_msgSend$setWifiTransportLossCount:
+ _objc_msgSend$setWifiVersion:
+ _objc_msgSend$setWinningTransport:
+ _objc_msgSend$setupEventSubscriptions
+ _objc_msgSend$sharedFactory
+ _objc_msgSend$shouldAllowECDSAKeyPairSetup
+ _objc_msgSend$signalPairVerifyFailureToDelegateWithError:
+ _objc_msgSend$signalPairVerifySuccessToDelegate
+ _objc_msgSend$softwareExceptionBootCount
+ _objc_msgSend$softwareResetBootCount
+ _objc_msgSend$softwareUpdateCompletedBootCount
+ _objc_msgSend$softwareWatchdogResetBootCount
+ _objc_msgSend$stackHighwaterCount
+ _objc_msgSend$stackOverflowBootCount
+ _objc_msgSend$stackOverflowCount
+ _objc_msgSend$startPipeline
+ _objc_msgSend$startWithServiceName:serviceType:serviceDomain:
+ _objc_msgSend$stopPipeline
+ _objc_msgSend$subnetMask
+ _objc_msgSend$supportedPowerSources
+ _objc_msgSend$supportsKeepAlive
+ _objc_msgSend$supportsThreadTransport
+ _objc_msgSend$supportsWiFiTransport
+ _objc_msgSend$systemBootCount
+ _objc_msgSend$systemCrashCount
+ _objc_msgSend$systemHangCount
+ _objc_msgSend$systemMemoryPressureCount
+ _objc_msgSend$systemUptime
+ _objc_msgSend$taskDeadlineMissCount
+ _objc_msgSend$temperatureLimitBootCount
+ _objc_msgSend$temperatureLimitViolationCount
+ _objc_msgSend$temperatureLimitViolationDuration
+ _objc_msgSend$threadFirstRestartCompleted
+ _objc_msgSend$threadFirstRestartConnectivityState
+ _objc_msgSend$threadFirstRestartRecoveryTime
+ _objc_msgSend$threadPingTestCount
+ _objc_msgSend$threadPingTestInterval
+ _objc_msgSend$threadRecoveryAttemptCount
+ _objc_msgSend$threadRecoveryConfiguration
+ _objc_msgSend$threadRestartCount
+ _objc_msgSend$threadRestartMinInterval
+ _objc_msgSend$threadTransportLossCount
+ _objc_msgSend$timeIntervalSinceNow
+ _objc_msgSend$timerProvider
+ _objc_msgSend$timerWithTimeInterval:options:
+ _objc_msgSend$totalTasksScheduledCount
+ _objc_msgSend$trackedTransportTypes
+ _objc_msgSend$transport:didChangeThreadAdvertisement:
+ _objc_msgSend$transport:didChangeWiFiAdvertisement:
+ _objc_msgSend$transport:didReceiveHeartbeatOnTransport:
+ _objc_msgSend$transport:pairVerifyDidCompleteOnIPAddress:transportType:
+ _objc_msgSend$transport:pairVerifyDidFailOnIPAddress:transportType:error:
+ _objc_msgSend$transportCurrentResolverSnapshot:
+ _objc_msgSend$transportStates
+ _objc_msgSend$tryingInitialCacheOnly
+ _objc_msgSend$txPacketCount
+ _objc_msgSend$txPacketErrorCount
+ _objc_msgSend$txPowerLevel
+ _objc_msgSend$unspecifiedBootCount
+ _objc_msgSend$updateCachedAddressesForDeviceID:cachedPrimary:cachedSecondary:
+ _objc_msgSend$updateServiceName:
+ _objc_msgSend$uploadWithoutResidentResponseCount
+ _objc_msgSend$wiFiPingTestCount
+ _objc_msgSend$wiFiPingTestInterval
+ _objc_msgSend$wiFiRecoveryConfiguration
+ _objc_msgSend$wiFiRestartMinInterval
+ _objc_msgSend$wifiFirstRestartCompleted
+ _objc_msgSend$wifiFirstRestartConnectivityState
+ _objc_msgSend$wifiFirstRestartRecoveryTime
+ _objc_msgSend$wifiRecoveryAttemptCount
+ _objc_msgSend$wifiRestartCount
+ _objc_msgSend$wifiTransportLossCount
+ _objc_msgSend$wifiVersion
+ _os_unfair_lock_lock
+ _record_pending_message
+ _serviceKeyForBrowseResult
+ _swift_deallocClassInstance
+ _symbolic $s7CoreHAP39AccessoryMetricsDictionaryRepresentableP
+ _symbolic SS_So8NSObjectCt
+ _symbolic Si
+ _symbolic So11HMMLogEventC
+ _symbolic So7NSErrorCSg
+ _symbolic _____ 10Foundation4UUIDV
+ _symbolic _____ 7CoreHAP17PairSetupTLVErrorO
+ _symbolic _____ 7CoreHAP25CoAPRequestRacingLogEventC
+ _symbolic _____ 7CoreHAP27AccessoryCHMMetricsLogEventC
+ _symbolic _____ 7CoreHAP28AccessoryCHMRecoveryLogEventC
+ _symbolic _____ So21HAPAccessoryCHMSourceV
+ _symbolic _____ So27HAP2CoAPAccessoryTransportsV
+ _symbolic _____ So27HAP2CoAPRacingTriggerReasonV
+ _symbolic _____ So27HAPAccessoryCHMRecoveryKindV
+ _symbolic _____ So27HAPCHMWiFiConnectivityStateV
+ _symbolic _____ So29HAPCHMThreadConnectivityStateV
+ _symbolic _____ So30HAP2CoAPRacingWinningTransportV
+ _symbolic _____Sg 10Foundation4DateV
+ _symbolic _____Sg6rolled_______pSg5errorAB9echoTokentSg 10Foundation4DataV s5ErrorP
+ _symbolic _____ySSSo8NSObjectCG s18_DictionaryStorageC
+ _symbolic _____ySS_So8NSObjectCtG s23_ContiguousArrayStorageC
+ _symbolic _____y______pG s23_ContiguousArrayStorageC s7CVarArgP
+ _xpc_dictionary_create
+ _xpc_dictionary_get_value
+ _xpc_get_type
+ _xpc_string_get_string_ptr
+ logCategory._hmf_once_t111
+ logCategory._hmf_once_t20
+ logCategory._hmf_once_t216
+ logCategory._hmf_once_t280
+ logCategory._hmf_once_t49
+ logCategory._hmf_once_t8
+ logCategory._hmf_once_t86
+ logCategory._hmf_once_t866
+ logCategory._hmf_once_t903
+ logCategory._hmf_once_t99
+ logCategory._hmf_once_v100
+ logCategory._hmf_once_v112
+ logCategory._hmf_once_v21
+ logCategory._hmf_once_v217
+ logCategory._hmf_once_v281
+ logCategory._hmf_once_v50
+ logCategory._hmf_once_v867
+ logCategory._hmf_once_v87
+ logCategory._hmf_once_v9
+ logCategory._hmf_once_v904
+ sharedFactory.onceToken
+ sharedFactory.sharedFactory
- -[HAP2AccessoryServer _browserFastSetHasDiscoveryAdvertisement:]
- -[HAP2AccessoryServer(Paired) mergeWithNewlyDiscoveredPairedAccessoryServer:]
- -[HAP2AccessoryServer(Unpaired) pairingDriver:didRequestLocalPairingIdentityWithCompletion:]
- -[HAP2AccessoryServer(Unpaired) pairingDriver:didSaveRemoteECDSAPairingKey:forAccessoryIdentifier:completion:]
- -[HAP2AccessoryServer(Unpaired) pairingDriver:didSaveRemotePairingIdentity:completion:]
- -[HAP2AccessoryServerController secureTransport:needsECDSALongTermPublicKeyForPeerWithIdentifier:completion:]
- -[HAP2AccessoryServerController secureTransport:needsLocalPairingIdentityForECDSAKeyPairSetupSession:completion:]
- -[HAP2AccessoryServerController secureTransport:needsLocalPairingIdentityWithCompletion:]
- -[HAP2AccessoryServerController secureTransport:needsRemotePairingIdentityForDeviceID:completion:]
- -[HAP2AccessoryServerCoordinator _didDiscoverAccessory:completion:]
- -[HAP2AccessoryServerSecureTransportPairVerify _createSecuritySessionFromECDSASession]
- -[HAP2AccessoryServerSecureTransportPairVerify _handleECDSASessionFailure:]
- -[HAP2AccessoryServerSecureTransportPairVerify setStateChangeCompletion:]
- -[HAP2CoAPClient sendRequestWithMethod:path:payload:dscpPriority:completion:]
- -[HAPAVCViewerRegistrationRequest initWithSessionIdentifier:viewerParticipantID:viewerNegotiationBlob:]
- -[HAPSystemKeychainStore getHH2ControllerECDSAPublicKeyWithIdentifier:]
- -[HAPSystemKeychainStore getHH2ControllerKeyWithIdentifier:]
- -[HAPWebRTCOfferOptions initWithSFrameEnabled:]
- GCC_except_table1092
- GCC_except_table1094
- GCC_except_table1200
- GCC_except_table1205
- GCC_except_table1209
- GCC_except_table1222
- GCC_except_table1236
- GCC_except_table1238
- GCC_except_table1240
- GCC_except_table1242
- GCC_except_table1368
- GCC_except_table1374
- GCC_except_table1376
- GCC_except_table1578
- GCC_except_table16
- GCC_except_table1790
- GCC_except_table1795
- GCC_except_table1801
- GCC_except_table1803
- GCC_except_table1809
- GCC_except_table1811
- GCC_except_table1815
- GCC_except_table1821
- GCC_except_table1823
- GCC_except_table1825
- GCC_except_table1827
- GCC_except_table1832
- GCC_except_table1836
- GCC_except_table1846
- GCC_except_table1854
- GCC_except_table1861
- GCC_except_table1865
- GCC_except_table1869
- GCC_except_table1874
- GCC_except_table1912
- GCC_except_table2031
- GCC_except_table2036
- GCC_except_table2037
- GCC_except_table2039
- GCC_except_table2041
- GCC_except_table2053
- GCC_except_table2058
- GCC_except_table2062
- GCC_except_table2065
- GCC_except_table2067
- GCC_except_table2072
- GCC_except_table2089
- GCC_except_table2099
- GCC_except_table2101
- GCC_except_table2103
- GCC_except_table2108
- GCC_except_table2111
- GCC_except_table2113
- GCC_except_table2116
- GCC_except_table2119
- GCC_except_table2123
- GCC_except_table2125
- GCC_except_table2128
- GCC_except_table2133
- GCC_except_table2135
- GCC_except_table2137
- GCC_except_table2141
- GCC_except_table2147
- GCC_except_table2155
- GCC_except_table2168
- GCC_except_table2201
- GCC_except_table2208
- GCC_except_table2226
- GCC_except_table2227
- GCC_except_table2228
- GCC_except_table2230
- GCC_except_table2231
- GCC_except_table2232
- GCC_except_table2234
- GCC_except_table2235
- GCC_except_table2257
- GCC_except_table2261
- GCC_except_table2269
- GCC_except_table234
- GCC_except_table235
- GCC_except_table2473
- GCC_except_table2482
- GCC_except_table2483
- GCC_except_table2484
- GCC_except_table2486
- GCC_except_table249
- GCC_except_table2502
- GCC_except_table2516
- GCC_except_table252
- GCC_except_table259
- GCC_except_table2596
- GCC_except_table2608
- GCC_except_table263
- GCC_except_table265
- GCC_except_table266
- GCC_except_table2676
- GCC_except_table269
- GCC_except_table2701
- GCC_except_table2709
- GCC_except_table2724
- GCC_except_table2736
- GCC_except_table2759
- GCC_except_table2765
- GCC_except_table282
- GCC_except_table288
- GCC_except_table2961
- GCC_except_table2970
- GCC_except_table2988
- GCC_except_table3022
- GCC_except_table3038
- GCC_except_table3040
- GCC_except_table3052
- GCC_except_table3059
- GCC_except_table3081
- GCC_except_table3095
- GCC_except_table3096
- GCC_except_table3097
- GCC_except_table3100
- GCC_except_table3108
- GCC_except_table3115
- GCC_except_table3123
- GCC_except_table3128
- GCC_except_table3133
- GCC_except_table3173
- GCC_except_table3190
- GCC_except_table3193
- GCC_except_table3200
- GCC_except_table3216
- GCC_except_table3232
- GCC_except_table3234
- GCC_except_table3238
- GCC_except_table3246
- GCC_except_table3254
- GCC_except_table3318
- GCC_except_table3325
- GCC_except_table3327
- GCC_except_table3328
- GCC_except_table3351
- GCC_except_table3371
- GCC_except_table3599
- GCC_except_table3666
- GCC_except_table3667
- GCC_except_table3674
- GCC_except_table3676
- GCC_except_table3677
- GCC_except_table3681
- GCC_except_table3682
- GCC_except_table3684
- GCC_except_table3691
- GCC_except_table3704
- GCC_except_table3715
- GCC_except_table3716
- GCC_except_table3718
- GCC_except_table3720
- GCC_except_table3723
- GCC_except_table3726
- GCC_except_table3728
- GCC_except_table3731
- GCC_except_table3734
- GCC_except_table3746
- GCC_except_table3748
- GCC_except_table3752
- GCC_except_table3756
- GCC_except_table3760
- GCC_except_table3786
- GCC_except_table3809
- GCC_except_table3815
- GCC_except_table3819
- GCC_except_table3823
- GCC_except_table3825
- GCC_except_table3828
- GCC_except_table3830
- GCC_except_table3832
- GCC_except_table3839
- GCC_except_table3840
- GCC_except_table3841
- GCC_except_table39
- GCC_except_table3918
- GCC_except_table3919
- GCC_except_table3920
- GCC_except_table3921
- GCC_except_table3922
- GCC_except_table3923
- GCC_except_table3924
- GCC_except_table3925
- GCC_except_table3926
- GCC_except_table3927
- GCC_except_table3928
- GCC_except_table3929
- GCC_except_table3930
- GCC_except_table3931
- GCC_except_table3984
- GCC_except_table4089
- GCC_except_table4096
- GCC_except_table4138
- GCC_except_table4145
- GCC_except_table4148
- GCC_except_table4151
- GCC_except_table4154
- GCC_except_table4157
- GCC_except_table4160
- GCC_except_table4163
- GCC_except_table4166
- GCC_except_table4171
- GCC_except_table4184
- GCC_except_table4189
- GCC_except_table4193
- GCC_except_table4198
- GCC_except_table4209
- GCC_except_table4217
- GCC_except_table4230
- GCC_except_table4234
- GCC_except_table4235
- GCC_except_table4255
- GCC_except_table4258
- GCC_except_table4267
- GCC_except_table4272
- GCC_except_table4278
- GCC_except_table4280
- GCC_except_table4294
- GCC_except_table4305
- GCC_except_table4307
- GCC_except_table4316
- GCC_except_table4318
- GCC_except_table4320
- GCC_except_table4326
- GCC_except_table4586
- GCC_except_table4592
- GCC_except_table4609
- GCC_except_table4613
- GCC_except_table4630
- GCC_except_table4651
- GCC_except_table4665
- GCC_except_table4669
- GCC_except_table4782
- GCC_except_table5238
- GCC_except_table5246
- GCC_except_table5257
- GCC_except_table5299
- GCC_except_table5302
- GCC_except_table5303
- GCC_except_table5304
- GCC_except_table5305
- GCC_except_table5387
- GCC_except_table5388
- GCC_except_table5389
- GCC_except_table5390
- GCC_except_table5391
- GCC_except_table5392
- GCC_except_table5398
- GCC_except_table5399
- GCC_except_table5401
- GCC_except_table5408
- GCC_except_table5411
- GCC_except_table5413
- GCC_except_table5418
- GCC_except_table5421
- GCC_except_table5424
- GCC_except_table5428
- GCC_except_table5432
- GCC_except_table545
- GCC_except_table556
- GCC_except_table572
- GCC_except_table584
- GCC_except_table5918
- GCC_except_table5919
- GCC_except_table5938
- GCC_except_table5948
- GCC_except_table5951
- GCC_except_table5956
- GCC_except_table5959
- GCC_except_table618
- GCC_except_table6230
- GCC_except_table6234
- GCC_except_table6279
- GCC_except_table6283
- GCC_except_table6285
- GCC_except_table6287
- GCC_except_table630
- GCC_except_table631
- GCC_except_table633
- GCC_except_table636
- GCC_except_table639
- GCC_except_table6489
- GCC_except_table6495
- GCC_except_table6499
- GCC_except_table6500
- GCC_except_table6501
- GCC_except_table6502
- GCC_except_table6508
- GCC_except_table6524
- GCC_except_table653
- GCC_except_table6560
- GCC_except_table6561
- GCC_except_table6562
- GCC_except_table6582
- GCC_except_table6594
- GCC_except_table6597
- GCC_except_table6602
- GCC_except_table6604
- GCC_except_table661
- GCC_except_table6618
- GCC_except_table668
- GCC_except_table671
- GCC_except_table6853
- GCC_except_table6866
- GCC_except_table6871
- GCC_except_table6874
- GCC_except_table6875
- GCC_except_table6877
- GCC_except_table6878
- GCC_except_table6880
- GCC_except_table6910
- GCC_except_table6932
- GCC_except_table6936
- GCC_except_table6940
- GCC_except_table6945
- GCC_except_table6949
- GCC_except_table6953
- GCC_except_table6957
- GCC_except_table6961
- GCC_except_table6969
- GCC_except_table6971
- GCC_except_table6975
- GCC_except_table7039
- GCC_except_table7040
- GCC_except_table7041
- GCC_except_table7042
- GCC_except_table7043
- GCC_except_table7044
- GCC_except_table7045
- GCC_except_table705
- GCC_except_table7107
- GCC_except_table7117
- GCC_except_table7118
- GCC_except_table7133
- GCC_except_table7134
- GCC_except_table7142
- GCC_except_table7148
- GCC_except_table715
- GCC_except_table7161
- GCC_except_table7164
- GCC_except_table7165
- GCC_except_table7170
- GCC_except_table7173
- GCC_except_table7180
- GCC_except_table7183
- GCC_except_table7197
- GCC_except_table7204
- GCC_except_table7210
- GCC_except_table7219
- GCC_except_table7221
- GCC_except_table7227
- GCC_except_table7228
- GCC_except_table723
- GCC_except_table7235
- GCC_except_table7259
- GCC_except_table7260
- GCC_except_table7265
- GCC_except_table7269
- GCC_except_table7270
- GCC_except_table7273
- GCC_except_table7279
- GCC_except_table7283
- GCC_except_table7287
- GCC_except_table7289
- GCC_except_table7291
- GCC_except_table7295
- GCC_except_table7409
- GCC_except_table7446
- GCC_except_table750
- GCC_except_table7503
- GCC_except_table7506
- GCC_except_table7513
- GCC_except_table7519
- GCC_except_table7526
- GCC_except_table7527
- GCC_except_table754
- GCC_except_table7543
- GCC_except_table7547
- GCC_except_table7548
- GCC_except_table7549
- GCC_except_table757
- GCC_except_table759
- GCC_except_table7598
- GCC_except_table7604
- GCC_except_table7631
- GCC_except_table7632
- GCC_except_table7637
- GCC_except_table7657
- GCC_except_table7676
- GCC_except_table7686
- GCC_except_table7691
- GCC_except_table7692
- GCC_except_table7693
- GCC_except_table7708
- GCC_except_table771
- GCC_except_table7711
- GCC_except_table7718
- GCC_except_table7725
- GCC_except_table773
- GCC_except_table7730
- GCC_except_table7736
- GCC_except_table7748
- GCC_except_table7749
- GCC_except_table7754
- GCC_except_table7763
- GCC_except_table7772
- GCC_except_table7776
- GCC_except_table7780
- GCC_except_table7805
- GCC_except_table7807
- GCC_except_table7834
- GCC_except_table792
- GCC_except_table798
- GCC_except_table7999
- GCC_except_table802
- GCC_except_table8062
- GCC_except_table8094
- GCC_except_table8097
- GCC_except_table813
- GCC_except_table814
- GCC_except_table819
- GCC_except_table822
- GCC_except_table825
- GCC_except_table8264
- GCC_except_table830
- GCC_except_table8302
- GCC_except_table8339
- GCC_except_table834
- GCC_except_table8428
- GCC_except_table8430
- GCC_except_table8432
- GCC_except_table8434
- GCC_except_table8436
- GCC_except_table8438
- GCC_except_table844
- GCC_except_table8440
- GCC_except_table8447
- GCC_except_table8449
- GCC_except_table8451
- GCC_except_table8454
- GCC_except_table8458
- GCC_except_table8467
- GCC_except_table8478
- GCC_except_table8481
- GCC_except_table8486
- GCC_except_table8491
- GCC_except_table8494
- GCC_except_table8497
- GCC_except_table8523
- GCC_except_table8526
- GCC_except_table8527
- GCC_except_table8546
- GCC_except_table8547
- GCC_except_table8548
- GCC_except_table8550
- GCC_except_table8551
- GCC_except_table8553
- GCC_except_table8554
- GCC_except_table8555
- GCC_except_table8557
- GCC_except_table8558
- GCC_except_table8560
- GCC_except_table8564
- GCC_except_table8565
- GCC_except_table8620
- GCC_except_table8627
- GCC_except_table8731
- GCC_except_table8735
- GCC_except_table8737
- GCC_except_table8739
- GCC_except_table8742
- GCC_except_table8744
- GCC_except_table8746
- GCC_except_table8748
- GCC_except_table8749
- GCC_except_table8751
- GCC_except_table8753
- GCC_except_table8758
- GCC_except_table8761
- GCC_except_table878
- GCC_except_table885
- GCC_except_table886
- GCC_except_table902
- GCC_except_table924
- GCC_except_table93
- GCC_except_table942
- GCC_except_table964
- GCC_except_table968
- GCC_except_table982
- GCC_except_table987
- __111-[HAP2AccessoryServerSecureTransportPairVerify securitySession:didReceiveLocalPairingIdentityRequestWithError:]_block_invoke
- __124-[HAP2AccessoryServerSecureTransportPairVerify securitySession:didReceiveRequestForPeerPairingIdentityWithIdentifier:error:]_block_invoke
- __45-[HAP2AccessoryServerController closeSession]_block_invoke
- __51-[HAP2AccessoryServerTransportCoAP _resolveAddress]_block_invoke_2
- __67-[HAP2AccessoryServerCoordinator _didDiscoverAccessory:completion:]_block_invoke
- __78-[HAPAccessoryServerBrowserHAP2Adapter discoverAccessoryServerWithIdentifier:]_block_invoke
- __78-[HAPAccessoryServerBrowserHAP2Adapter discoverAccessoryServerWithIdentifier:]_block_invoke_2
- __82-[HAP2AccessoryServerSecureTransportPairVerify pairSetupSession:didStopWithError:]_block_invoke
- __91-[HAP2AccessoryServerSecureTransportPairVerify ecdsaLongTermPublicKeyOfPeerWithIdentifier:]_block_invoke
- __OBJC_$_INSTANCE_METHODS_HAP2AccessoryServer(Paired|PairedInternal|Unpaired)
- __OBJC_$_INSTANCE_METHODS_HAP2AccessoryServerBrowser
- __OBJC_$_INSTANCE_METHODS_HAP2AccessoryServerCoordinator
- __OBJC_CLASS_PROTOCOLS_$_HAP2AccessoryServer(Paired|PairedInternal|Unpaired)
- ___105-[HAP2AccessoryServerSecureTransportPairVerify localPairingIdentityOfECDSAKeyPairSetupSession:withError:]_block_invoke
- ___105-[HAP2AccessoryServerSecureTransportPairVerify localPairingIdentityOfECDSAKeyPairSetupSession:withError:]_block_invoke_2
- ___109-[HAP2AccessoryServerController secureTransport:needsECDSALongTermPublicKeyForPeerWithIdentifier:completion:]_block_invoke
- ___110-[HAP2AccessoryServer(Unpaired) pairingDriver:didSaveRemoteECDSAPairingKey:forAccessoryIdentifier:completion:]_block_invoke
- ___111-[HAP2AccessoryServerSecureTransportPairVerify securitySession:didReceiveLocalPairingIdentityRequestWithError:]_block_invoke
- ___111-[HAP2AccessoryServerSecureTransportPairVerify securitySession:didReceiveLocalPairingIdentityRequestWithError:]_block_invoke_2
- ___113-[HAP2AccessoryServerController secureTransport:needsLocalPairingIdentityForECDSAKeyPairSetupSession:completion:]_block_invoke
- ___117-[HAP2AccessoryServerPairingDriverPairSetupWorkItem pairSetupSession:didReceiveLocalPairingIdentityRequestWithError:]_block_invoke
- ___118-[HAP2AccessoryServerPairingDriverPairSetupWorkItem pairSetupSession:didPairWithPeerIdentifier:ecdsaPairingKey:error:]_block_invoke
- ___124-[HAP2AccessoryServerSecureTransportPairVerify securitySession:didReceiveRequestForPeerPairingIdentityWithIdentifier:error:]_block_invoke
- ___124-[HAP2AccessoryServerSecureTransportPairVerify securitySession:didReceiveRequestForPeerPairingIdentityWithIdentifier:error:]_block_invoke_2
- ___32-[HAP2CoAPClient _didDisconnect]_block_invoke
- ___43-[HAP2AccessoryServer(Paired) closeSession]_block_invoke
- ___45-[HAP2AccessoryServerController closeSession]_block_invoke
- ___64-[HAP2AccessoryServer _browserFastSetHasDiscoveryAdvertisement:]_block_invoke
- ___65-[HAP2AccessoryServerEncodingThread _parseCharacteristics:error:]_block_invoke
- ___67-[HAP2AccessoryServerCoordinator _didDiscoverAccessory:completion:]_block_invoke
- ___75-[HAP2AccessoryServerSecureTransportPairVerify _handleECDSASessionFailure:]_block_invoke
- ___75-[HAP2AccessoryServerSecureTransportPairVerify _handleECDSASessionFailure:]_block_invoke_2
- ___75-[HAP2AccessoryServerSecureTransportPairVerify _handleECDSASessionFailure:]_block_invoke_3
- ___75-[HAP2AccessoryServerSecureTransportPairVerify _handleECDSASessionFailure:]_block_invoke_4
- ___77-[HAP2AccessoryServer(Paired) mergeWithNewlyDiscoveredPairedAccessoryServer:]_block_invoke
- ___77-[HAP2CoAPClient sendRequestWithMethod:path:payload:dscpPriority:completion:]_block_invoke
- ___77-[HAP2CoAPClient sendRequestWithMethod:path:payload:dscpPriority:completion:]_block_invoke_2
- ___82-[HAP2AccessoryServerSecureTransportPairVerify pairSetupSession:didStopWithError:]_block_invoke_2
- ___82-[HAP2AccessoryServerSecureTransportPairVerify pairSetupSession:didStopWithError:]_block_invoke_3
- ___82-[HAP2AccessoryServerSecureTransportPairVerify pairSetupSession:didStopWithError:]_block_invoke_4
- ___87-[HAP2AccessoryServer(Unpaired) pairingDriver:didSaveRemotePairingIdentity:completion:]_block_invoke
- ___87-[HAP2CoAPClient _sendRequestWithMethod:path:payload:activity:dscpPriority:completion:]_block_invoke
- ___87-[HAP2CoAPClient _sendRequestWithMethod:path:payload:activity:dscpPriority:completion:]_block_invoke_2
- ___91-[HAP2AccessoryServerSecureTransportPairVerify ecdsaLongTermPublicKeyOfPeerWithIdentifier:]_block_invoke
- ___91-[HAP2AccessoryServerSecureTransportPairVerify ecdsaLongTermPublicKeyOfPeerWithIdentifier:]_block_invoke_2
- ___92-[HAP2AccessoryServer(Unpaired) pairingDriver:didRequestLocalPairingIdentityWithCompletion:]_block_invoke
- ___92-[HAP2AccessoryServerPairingDriverPairSetupWorkItem pairSetupSession:didPairWithPeer:error:]_block_invoke
- ___98-[HAP2AccessoryServerController secureTransport:needsRemotePairingIdentityForDeviceID:completion:]_block_invoke
- ___block_descriptor_48_e693_v24?0"HAP2CoAPClient"8^{coap_session_t=CCCIII{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}}^{coap_endpoint_t}^{coap_context_t}^vSCi^{coap_queue_t}Q[8C]Q^{coap_pdu_t}QQQQQ*Q*Q^vI{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}Ii}16l
- ___block_descriptor_48_e8_32bs40w_e839_v24?0^{coap_context_t=[6S]^{coap_resource_t}^{coap_resource_t}^{coap_async_state_t}Q^{coap_queue_t}^{coap_endpoint_t}^{coap_session_t}^?^?^?^?^?^?^?^?^?^?^v*Q*QIIIII^v}8^{coap_session_t=CCCIII{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}}^{coap_endpoint_t}^{coap_context_t}^vSCi^{coap_queue_t}Q[8C]Q^{coap_pdu_t}QQQQQ*Q*Q^vI{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}Ii}16l
- ___block_descriptor_48_e8_32r40r_e69_v32?0"HAP2AccessoryServerDiscoveryBonjourBrowseResultTuple"8Q16^B24l
- ___block_descriptor_48_e8_32s40bs_e40_v24?0"HAPPairingIdentity"8"NSError"16l
- ___block_descriptor_48_e8_32s40r_e17_v16?0"NSError"8l
- ___block_descriptor_56_e8_32s40r48r_e28_v24?0"NSData"8"NSError"16l
- ___block_descriptor_56_e8_32s40r48r_e40_v24?0"HAPPairingIdentity"8"NSError"16l
- ___block_descriptor_56_e8_32s40s48bs_e40_v24?0"HAPECDSAPairingKey"8"NSError"16l
- ___block_descriptor_56_e8_32s40s48r_e45_v32?0"HAP2TLVParamServiceSignature"8Q16^B24l
- ___block_descriptor_56_e8_32s40s48r_e52_v32?0"HAP2TLVParamCharacteristicSignature"8Q16^B24l
- ___block_descriptor_64_e8_32s40s48bs56w_e20_v20?0B8"NSError"12l
- ___block_descriptor_69_e8_32s40s48s_e693_v24?0"HAP2CoAPClient"8^{coap_session_t=CCCIII{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}}^{coap_endpoint_t}^{coap_context_t}^vSCi^{coap_queue_t}Q[8C]Q^{coap_pdu_t}QQQQQ*Q*Q^vI{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}Ii}16l
- ___block_descriptor_80_e8_32s40s48s56s64r72r_e5_v8?0l
- ___block_descriptor_81_e8_32s40s48s56s64bs_e5_v8?0l
- ___copy_helper_block_e8_32s40s48s56s64r72r
- ___destroy_helper_block_e8_32s40s48s56s64r72r
- __swift_closure_destructor.181Tm
- _objc_msgSend$_browserFastSetHasDiscoveryAdvertisement:
- _objc_msgSend$_createSecuritySessionFromECDSASession
- _objc_msgSend$_didDiscoverAccessory:completion:
- _objc_msgSend$_handleECDSASessionFailure:
- _objc_msgSend$_parseCharacteristics:error:
- _objc_msgSend$fetchControllerKeyForECDSAKeyAccessory:completion:
- _objc_msgSend$fetchKeysForIdentifiers:completion:
- _objc_msgSend$getHH2ControllerKeyWithIdentifier:
- _objc_msgSend$initWithSFrameEnabled:
- _objc_msgSend$initWithSessionIdentifier:viewerParticipantID:viewerNegotiationBlob:
- _objc_msgSend$mergeWithNewlyDiscoveredPairedAccessoryServer:
- _objc_msgSend$pairingDriver:didRequestLocalPairingIdentityWithCompletion:
- _objc_msgSend$pairingDriver:didSaveRemoteECDSAPairingKey:forAccessoryIdentifier:completion:
- _objc_msgSend$pairingDriver:didSaveRemotePairingIdentity:completion:
- _objc_msgSend$saveECDSAKey:forAccessoryName:completion:
- _objc_msgSend$savePublicKey:forAccessoryWithID:completion:
- _objc_msgSend$secureTransport:needsECDSALongTermPublicKeyForPeerWithIdentifier:completion:
- _objc_msgSend$secureTransport:needsLocalPairingIdentityForECDSAKeyPairSetupSession:completion:
- _objc_msgSend$secureTransport:needsLocalPairingIdentityWithCompletion:
- _objc_msgSend$secureTransport:needsRemotePairingIdentityForDeviceID:completion:
- _objc_msgSend$sendRequestWithMethod:path:payload:dscpPriority:completion:
- logCategory._hmf_once_t13
- logCategory._hmf_once_t214
- logCategory._hmf_once_t267
- logCategory._hmf_once_t47
- logCategory._hmf_once_t69
- logCategory._hmf_once_t79
- logCategory._hmf_once_t83
- logCategory._hmf_once_t856
- logCategory._hmf_once_t98
- logCategory._hmf_once_v14
- logCategory._hmf_once_v215
- logCategory._hmf_once_v268
- logCategory._hmf_once_v48
- logCategory._hmf_once_v70
- logCategory._hmf_once_v80
- logCategory._hmf_once_v84
- logCategory._hmf_once_v857
- logCategory._hmf_once_v99
CStrings:
+ "\v"
+ "\r"
+ " (Thread-only)"
+ "!Aq\x81"
+ "%@ '%{private}@' Connecting via secondary (Thread) transport"
+ "%@ - close with nothing to close: state change completion already handled"
+ "%@ Close with no client to close; completing the transition"
+ "%@ Failed to send hello: %@, retry count: %lu"
+ "%@ HDS-over-TCP peer selected: %s from %s (%{private}@)"
+ "%@ HDS-over-TCP peer unavailable (coapClient=%p, secondaryCoAPClient=%p)"
+ "%@ Hello deferred: registration not complete"
+ "%@ Hello deferred: secondary client not connected"
+ "%@ Hello sent successfully from secondary transport"
+ "%@ Hello skipped: secondary client is nil"
+ "%@ Lock-only-set hasDiscoveryAdvertisement=%{public}d"
+ "%@ Max hello retries reached, giving up"
+ "%@ NLM Probe: Client for transport %lu not connected, closing and refreshing"
+ "%@ NLM Probe: No CoAP client for transport %lu, refreshing"
+ "%@ NLM Probe: Sending Empty CON probe on transport %lu"
+ "%@ NLM-APPLY hop1 controller: DROPPED, self.transport is nil"
+ "%@ NLM-APPLY hop1 controller: entry"
+ "%@ NLM-APPLY hop1 controller: forwarding to %@"
+ "%@ NLM-APPLY hop2 secure: DROPPED, underlying %@ does not respond to applyResolverAddresses:completion:"
+ "%@ NLM-APPLY hop2 secure: forwarding to underlying %@"
+ "%@ NLM-APPLY hop3 coap: DROPPED, NLM feature not enabled"
+ "%@ NLM-APPLY hop3 coap: entry primary=%lu secondary=%lu, enqueueing onto transport queue"
+ "%@ NLM: Cannot probe, no transport"
+ "%@ NLM: Cannot read local endpoints, no transport"
+ "%@ NLM: Re-advertisement while unreachable, triggering reconnection"
+ "%@ NLM: Session keep-alive %@; connected-only notify %@"
+ "%@ NLM: s# changed %u -> %u while Unreachable — full refresh"
+ "%@ Not announcing re-established session (readingAttributeDatabase=%@, accessories=%lu)"
+ "%@ Resolve completed in state %lu (not Opening), ignoring"
+ "%@ Sending hello from secondary transport"
+ "%@ Session %lu already announced, skipping re-establish"
+ "%@.registry"
+ "%@.registry.propertyLock"
+ "%s|%s|%s"
+ "(nil)"
+ "(none)"
+ "(null)"
+ "(unprintable)"
+ ", Should Allow ECDSA Key Pair Setup: %@"
+ "000000-0000"
+ "00000274-0000-1000-8000-0026BB765291"
+ "00000275-0000-1000-8000-0026BB765291"
+ "3"
+ ": "
+ "<%@: %p primary=%lu secondary=%lu cachedPrimary=%@ cachedSecondary=%@>"
+ "<%s, %@>"
+ "<HAPAVCStreamingControlCommandWrapper value=%@>"
+ "<HAPAVCStreamingControlRequest sessionIdentifier=%@, command=%@>"
+ "<HAPAVCStreamingControlResponse sessionIdentifier=%@, status=%@>"
+ "<HAPAVCStreamingControlStatusWrapper value=%@>"
+ "<HAPAVCViewerRegistrationOperationWrapper value=%@>"
+ "<HAPAVCViewerRegistrationRequest sessionIdentifier=%@, viewerParticipantID=%@, viewerNegotiationBlob=%@, operation=%@>"
+ "<HAPBluetoothMetrics bluetoothVersion=%@, rssi=%@, txPowerLevel=%@, packetRxCount=%@, packetTxCount=%@, packetRxErrorCount=%@, packetTxErrorCount=%@, overrunCount=%@, connectionStatus=%@, connectionCount=%@, connectionErrorCount=%@, disconnectionCount=%@, disconnectionErrorCount=%@, hwExceptionCount=%@>"
+ "<HAPBootReasonsMetrics unspecifiedBootCount=%@, powerOnBootCount=%@, brownOutResetBootCount=%@, softwareWatchdogResetBootCount=%@, hardwareWatchdogResetBootCount=%@, softwareUpdateCompletedBootCount=%@, softwareResetBootCount=%@, softwareExceptionBootCount=%@, hardwareFaultBootCount=%@, stackOverflowBootCount=%@, heapOverflowBootCount=%@, temperatureLimitBootCount=%@, connectivityMonitorBootCount=%@>"
+ "<HAPCHMMetrics wifiTransportLossCount=%@, wifiRecoveryAttemptCount=%@, wifiRestartCount=%@, wifiFirstRestartRecoveryTime=%@, wifiFirstRestartCompleted=%@, wifiFirstRestartConnectivityState=%@, threadTransportLossCount=%@, threadRecoveryAttemptCount=%@, threadRestartCount=%@, threadFirstRestartRecoveryTime=%@, threadFirstRestartCompleted=%@, threadFirstRestartConnectivityState=%@, hapSessionLossCount=%@, chmAccessoryRebootDurationToRecovery=%@, chmAccessoryRebootCompleted=%@>"
+ "<HAPConnectionHealthMonitor deviceRebootEnable=%@, threadRecoveryConfiguration=%@, wiFiRecoveryConfiguration=%@, recoveryStaggerDelay=%@, deviceRebootDelay=%@, threadPingTestCount=%@, threadPingTestInterval=%@, threadRestartMinInterval=%@, wiFiPingTestCount=%@, wiFiPingTestInterval=%@, wiFiRestartMinInterval=%@>"
+ "<HAPContributingSensor sensorUUID=%@>"
+ "<HAPErrorCountersMetrics entries=%@>"
+ "<HAPErrorCountersMetricsEntry errorID=%@, count=%@>"
+ "<HAPHKSV3UploadLatencyMetrics fragmentSuccessCount=%@, fragmentFailureCount=%@, fragmentRetriedCount=%@, networkErrorCount=%@, authenticationErrorCount=%@, serverReturnedErrorCount=%@, localErrorCount=%@, playlistFailureCount=%@, latencyCount250ms=%@, latencyCount500ms=%@, latencyCount1000ms=%@, latencyCount2000ms=%@, latencyCount3750ms=%@, latencyCountOver3750ms=%@, sessionSuccessCount=%@, partialSuccessCount=%@, sessionFailureCount=%@, uploadWithoutResidentResponseCount=%@, audioOnlyFailureCount=%@, abandonedRequestCount=%@>"
+ "<HAPMetricEventBluetoothVersionTypeWrapper value=%@>"
+ "<HAPMetricEventPowerSourcesBitmaskWrapper value=%@>"
+ "<HAPMetricEventPowerSourcesEnumWrapper value=%@>"
+ "<HAPMetricEventThreadFirstRestartConnectivityStateWrapper value=%@>"
+ "<HAPMetricEventWiFiFirstRestartConnectivityStateWrapper value=%@>"
+ "<HAPMetricEventWiFiVersionTypeWrapper value=%@>"
+ "<HAPPowerMetrics supportedPowerSources=%@, currentPowerSource=%@, durationOnBatteryPower=%@, durationRemainingOnBatteryPower=%@, batteryPercentage=%@>"
+ "<HAPSaturationMetrics stackHighwaterCount=%@, lastStackHighwaterTaskName=%@, heapHighwaterCount=%@, lastHeapHighwaterTaskName=%@, stackOverflowCount=%@, lastStackOverflowTaskName=%@, heapOverflowCount=%@, lastHeapOverflowTaskName=%@, averageSystemMemoryUtilization=%@, peakSystemMemoryUtilization=%@, systemMemoryPressureCount=%@, processCriticalMemoryCount=%@, lastProcessCriticalMemoryName=%@, averageCPUUtilization=%@, peakCPUUtilization=%@, taskDeadlineMissCount=%@, totalTasksScheduledCount=%@, maxTaskReadyQueueSize=%@, loadAverage=%@, nonVolatileMemoryWriteCount=%@, nonVolatileMemoryReadCount=%@, nonVolatileMemoryWriteErrorCount=%@, nonVolatileMemoryReadErrorCount=%@, nonVolatileMemoryUtilization=%@>"
+ "<HAPSensorList contributingSensor=%@>"
+ "<HAPSessionKeepAliveTransportTypeWrapper value=%@>"
+ "<HAPStabilityMetrics systemUptime=%@, systemBootCount=%@, expectedBootCount=%@, systemCrashCount=%@, systemHangCount=%@, lastBootReason=%@, activeHardwareFaults=%@>"
+ "<HAPStabilityMetricsBootReasonTypeWrapper value=%@>"
+ "<HAPStabilityMetricsHardwareFaultTypeWrapper value=%@>"
+ "<HAPTLVPreferredWiFiEntry SSID=%@, securityMode=%@, PSK=%@>"
+ "<HAPTLVPreferredWiFiList preferredWiFiList=%@>"
+ "<HAPTLVSelectedSessionKeepAliveConfigurationEntry transportType=%@, minimumInterval=%@, maximumInterval=%@>"
+ "<HAPTLVSelectedSessionKeepAliveConfigurationList entries=%@>"
+ "<HAPTLVSupportedSessionKeepAliveConfigurationEntry transportType=%@, minimumInterval=%@, maximumInterval=%@, minimumRange=%@>"
+ "<HAPTLVSupportedSessionKeepAliveConfigurationList entries=%@>"
+ "<HAPThermalMetrics temperatureLimitViolationCount=%@, temperatureLimitViolationDuration=%@, minimumDeviceTemperature=%@, maximumDeviceTemperature=%@, averageDeviceTemperature=%@>"
+ "<HAPWebRTCOfferOptions SFrameEnabled=%@, SFrameConfiguration=%@>"
+ "<HAPWiFiMetrics gatewayMacAddress=%@, gatewayIPv4Address=%@, gatewayIPv6Address=%@, subnetMask=%@, bssid=%@, wifiVersion=%@, channelNumber=%@, rssi=%@, connectionStatus=%@, disconnectionCount=%@, disconnectionDuration=%@, beaconRxCount=%@, beaconRxInterval=%@, beaconLostCount=%@, ipAddressList=%@, packetMulticastRxCount=%@, packetMulticastRxErrorCount=%@, packetMulticastTxCount=%@, packetMulticastTxErrorCount=%@, packetUnicastRxCount=%@, packetUnicastRxErrorCount=%@, packetUnicastTxCount=%@, packetUnicastTxErrorCount=%@, txPacketCount=%@, txPacketErrorCount=%@, rxPacketCount=%@, rxPacketErrorCount=%@, hwExceptionCount=%@, wifiRestartCount=%@>"
+ "@\"HAP2AccessoryServerIPCacheData\"16@?0@\"HAP2AccessoryServerIPCacheData\"8"
+ "ASSERTION: NLM: %@ Refresh primary bring-up called with live coapClient — skipping to avoid leak"
+ "ASSERTION: NLM: %@ Refresh secondary bring-up called with live secondaryCoAPClient — skipping to avoid leak"
+ "Address %@ does not match any local interface, assuming Thread"
+ "Address %@ matches interface %@ (Thread: %@)"
+ "All addresses already tried"
+ "All transports missed heartbeat"
+ "Attempting to derive HDS keys without an active session"
+ "Audit reap: evicted cache entry deviceID=%{public}@"
+ "B5"
+ "Cache init TXT-parse failed deviceID=%{public}@"
+ "Cache init skip deviceID=%{public}@ isPaired=%d error.code=%ld"
+ "Cache init skip — no serviceName deviceID=%{public}@"
+ "Cache init: no cached records to restore"
+ "Cache init: re-running for %lu cached records after coordinators started"
+ "Cache init: restoring %lu cached accessory servers"
+ "Config UPDATE no-op (unchanged) deviceID=%{public}@"
+ "Config UPDATE persisted deviceID=%{public}@"
+ "Coordinator: dropping discovery for deviceID=%{public}@ — mDNS announcement has no service name; accessory is unreachable until it fixes its advertisement"
+ "CoreHAP"
+ "CoreHAP.AccessoryCHMMetricsLogEvent"
+ "CoreHAP.AccessoryCHMRecoveryLogEvent"
+ "CoreThreadRadio framework not available"
+ "Created shared CtrClient for CoreHAP"
+ "DNS context already retained"
+ "DNS-SD resolve callback delivered fatal error"
+ "DNS-SD resolver delivered fatal error event"
+ "Disconnect request is not supported for %{public}@"
+ "Failed to create XPC dictionary"
+ "Failed to create shared CtrClient instance"
+ "Failed to derive HDS keys from foreign pair-verify session: %@"
+ "Failed to get Thread mesh local prefix: empty string"
+ "Failed to get Thread mesh local prefix: invalid XPC response type"
+ "Failed to get Thread mesh local prefix: property value is not a string"
+ "Failed to remove the pairing identity backups: %ld"
+ "Failed to start address resolver"
+ "Foreign pair-verify HDS key derivation failed"
+ "Found thread accessory with server ID known = %d paired = %d"
+ "HAP2 adapter deallocated before HDS key derivation"
+ "HAP2 secure transport deallocated before HDS key derivation"
+ "HAP2 secure transport unavailable for HDS key derivation"
+ "HAP2 security session unavailable for HDS key derivation"
+ "HAP2AccessoryServerIPCache"
+ "HAP2AccessoryServerTest_reactiveWorkRecorder"
+ "HAP2CoAPClient"
+ "HAP2CoAPClient has no registered IO consumer or session"
+ "HAP2IPCache"
+ "HAP2ThreadNetworkUtil: force-refresh confirmed cached prefix"
+ "HAP2ThreadNetworkUtil: force-refresh detected missed event — cached=%{private}@ fresh=%{private}@ (event subscription drift)"
+ "HAP2ThreadNetworkUtil: invalidating cached mesh-local prefix on event %s"
+ "HAP2ThreadNetworkUtil: registered wpantund event subscriptions"
+ "HAPAVCStreamingControlCommandEnd"
+ "HAPAVCStreamingControlStatusError"
+ "HAPAVCStreamingControlStatusSuccess"
+ "HAPAVCStreamingControlStatusUnknownSessionIdentifier"
+ "HAPAVCViewerRegistrationOperationDeregister"
+ "HAPAVCViewerRegistrationOperationRegister"
+ "HAPAVCViewerRegistrationStatusUnknownParticipant"
+ "HAPErrorAlreadyPairedPeerIdentifierKey"
+ "HAPInternalErrorMarker"
+ "HAPMetadataCharacteristic %@(%@): description: %@"
+ "HAPMetadataUnit %@: description: %@"
+ "HAPMetricEventBluetoothVersionType4_0"
+ "HAPMetricEventBluetoothVersionType4_1"
+ "HAPMetricEventBluetoothVersionType4_2"
+ "HAPMetricEventBluetoothVersionType5_0"
+ "HAPMetricEventBluetoothVersionType5_1"
+ "HAPMetricEventBluetoothVersionType5_2"
+ "HAPMetricEventBluetoothVersionType5_3"
+ "HAPMetricEventBluetoothVersionType5_4"
+ "HAPMetricEventBluetoothVersionType6_0"
+ "HAPMetricEventBluetoothVersionTypeUnknown"
+ "HAPMetricEventPowerSourcesBitmaskRechargableBattery"
+ "HAPMetricEventPowerSourcesBitmaskReplaceableBattery"
+ "HAPMetricEventPowerSourcesBitmaskUnspecified"
+ "HAPMetricEventPowerSourcesBitmaskWired"
+ "HAPMetricEventPowerSourcesEnumRechargableBattery"
+ "HAPMetricEventPowerSourcesEnumReplaceableBattery"
+ "HAPMetricEventPowerSourcesEnumUnspecified"
+ "HAPMetricEventPowerSourcesEnumWired"
+ "HAPMetricEventThreadFirstRestartConnectivityStateBorderRouter"
+ "HAPMetricEventThreadFirstRestartConnectivityStateLeader"
+ "HAPMetricEventThreadFirstRestartConnectivityStateNeighbor"
+ "HAPMetricEventThreadFirstRestartConnectivityStateParent"
+ "HAPMetricEventThreadFirstRestartConnectivityStateResident"
+ "HAPMetricEventWiFiFirstRestartConnectivityStateGateway"
+ "HAPMetricEventWiFiFirstRestartConnectivityStateResident"
+ "HAPMetricEventWiFiVersionType802_11a"
+ "HAPMetricEventWiFiVersionType802_11ac"
+ "HAPMetricEventWiFiVersionType802_11ah"
+ "HAPMetricEventWiFiVersionType802_11ax"
+ "HAPMetricEventWiFiVersionType802_11b"
+ "HAPMetricEventWiFiVersionType802_11g"
+ "HAPMetricEventWiFiVersionType802_11n"
+ "HAPMetricEventWiFiVersionTypeUnknown"
+ "HAPSecuritySession._pairingSession nil during deriveEncryptionForDataStream"
+ "HAPSessionKeepAliveTransportTypeEthernet"
+ "HAPSessionKeepAliveTransportTypeThread"
+ "HAPSessionKeepAliveTransportTypeWiFi"
+ "HAPStabilityMetricsBootReasonTypeBrownOutReset"
+ "HAPStabilityMetricsBootReasonTypeConnectivityMonitorReset"
+ "HAPStabilityMetricsBootReasonTypeHardwareFault"
+ "HAPStabilityMetricsBootReasonTypeHardwareWatchdogReset"
+ "HAPStabilityMetricsBootReasonTypeHeapOverflow"
+ "HAPStabilityMetricsBootReasonTypePowerOnReboot"
+ "HAPStabilityMetricsBootReasonTypeSoftwareException"
+ "HAPStabilityMetricsBootReasonTypeSoftwareReset"
+ "HAPStabilityMetricsBootReasonTypeSoftwareUpdateCompleted"
+ "HAPStabilityMetricsBootReasonTypeSoftwareWatchdogReset"
+ "HAPStabilityMetricsBootReasonTypeStackOverflow"
+ "HAPStabilityMetricsBootReasonTypeTemperatureLimit"
+ "HAPStabilityMetricsBootReasonTypeUnspecified"
+ "HAPStabilityMetricsHardwareFaultTypeAudioInputFault"
+ "HAPStabilityMetricsHardwareFaultTypeAudioOutputFault"
+ "HAPStabilityMetricsHardwareFaultTypeNetworkInterfaceFault"
+ "HAPStabilityMetricsHardwareFaultTypeNonResettableOverTemp"
+ "HAPStabilityMetricsHardwareFaultTypeNonVolatileMemoryError"
+ "HAPStabilityMetricsHardwareFaultTypePowerSource"
+ "HAPStabilityMetricsHardwareFaultTypeRadio"
+ "HAPStabilityMetricsHardwareFaultTypeRegisterException"
+ "HAPStabilityMetricsHardwareFaultTypeResettableOverTemp"
+ "HAPStabilityMetricsHardwareFaultTypeSensor"
+ "HAPStabilityMetricsHardwareFaultTypeTamperDetected"
+ "HAPStabilityMetricsHardwareFaultTypeUnspecified"
+ "HAPStabilityMetricsHardwareFaultTypeUserInterfaceFault"
+ "HAPStabilityMetricsHardwareFaultTypeVisualDisplayFault"
+ "HDS key derivation failed (pairedServer=%p controller=%p secureTransport=%p)"
+ "HDS key derivation failed: no security session on HAP2 secure transport"
+ "HDS peer address unavailable (pairedServer=%p controller=%p secureTransport=%p coapTransport=%p)"
+ "ICMP port unreachable; failing this session's queued messages now"
+ "IPv4"
+ "IPv6"
+ "IPv6:MeshLocalPrefix"
+ "Invalid cachedPrimaryData type for device %{public}@"
+ "Invalid cachedSecondaryData type for device %{public}@"
+ "Invalid or missing configurationInfo for device %{public}@"
+ "KeepAlive"
+ "Legacy WAC accessory Bonjour event - hasPairings %d continuingLegacyPairing: %d"
+ "Live resolver completed with empty endpoint set"
+ "Local endpoint is neither AF_INET nor AF_INET6"
+ "Local endpoint is not IPv4"
+ "Local endpoint is not IPv6"
+ "M%hhu: accessory rejected pair-setup with error %llu (%{public}s) — failing with HAP error %ld"
+ "M5: owner additional-pairing info unavailable, failing pair-setup: %{public}s"
+ "MFi early-auth: DISMISSED — the tap-time validate+roll does not cover M4's full token (%ld bytes); abandoning it and validating the M4 token"
+ "MFi early-auth: M4 echoed the tap-time token and its validate+roll already finished — using its result for M5"
+ "MFi early-auth: M4 echoed the tap-time token but its validate+roll is still in flight — M5 will continue when it returns"
+ "MFi early-auth: M4 hash verified and validate+roll already finished — resolving M5 from its result"
+ "MFi early-auth: the adopted validate+roll returned nothing usable; validating M4's echoed token instead"
+ "MFi early-auth: the tap-time validate+roll has nothing usable for M4's echoed token; validating it instead"
+ "MFi pre-consent roll: consuming the result that arrived during the consent wait"
+ "MFi pre-consent roll: finished after %{public}sms, before consent; parking its result until commit"
+ "MFi pre-consent roll: still in flight at consent after %{public}sms; M5 will continue when it returns"
+ "MFi pre-consent roll: validating M4's token during the consent wait, off the on-tag critical path"
+ "MFi validate+roll resolved after teardown — discarding"
+ "NCP:State"
+ "NLM keep-alive listener active, skipping reachability client"
+ "NLM-ADDR %@ _setIpAddress: %{private}s -> %{private}s"
+ "NLM-APPLY hop3 coap: DROPPED, transport deallocated before the queued block ran"
+ "NLM: %@ '%{private}@'   [%lu] IPv4: %s (port: %d, %@)"
+ "NLM: %@ '%{private}@'   [%lu] IPv6: %s (port: %d, %@)"
+ "NLM: %@ '%{private}@'   [%lu] Unknown address family: %d"
+ "NLM: %@ '%{private}@' Connecting via primary transport"
+ "NLM: %@ '%{private}@' Discovered primary address: %@"
+ "NLM: %@ '%{private}@' Discovered secondary (Thread) address: %@"
+ "NLM: %@ '%{private}@' Duplicate IP address in secondary list - skipping"
+ "NLM: %@ '%{private}@' Initial resolver complete with addresses present but all already tried — unable to connect"
+ "NLM: %@ '%{private}@' Initial resolver complete; connecting via primary transport"
+ "NLM: %@ '%{private}@' Initial resolver complete; connecting via secondary (Thread) transport"
+ "NLM: %@ '%{private}@' Primary addresses:"
+ "NLM: %@ '%{private}@' Primary addresses: %lu, Secondary (Thread) addresses: %lu"
+ "NLM: %@ '%{private}@' Resolver pipeline died; scheduled restart in %.1fs"
+ "NLM: %@ '%{private}@' Resolver pipeline failed: %@"
+ "NLM: %@ '%{private}@' Resolver restart timer fired in state %lu (not Open/Opening), ignoring"
+ "NLM: %@ '%{private}@' Resolver restart timer fired; re-arming pipeline"
+ "NLM: %@ '%{private}@' Resolver snapshot empty on open; awaiting live update with resolve-timeout backstop"
+ "NLM: %@ '%{private}@' Resolver snapshot empty on open; falling back to %lu mirrored address(es)"
+ "NLM: %@ '%{private}@' Resolver timed out after %.1fs without first usable update"
+ "NLM: %@ '%{private}@' Resolver update primary=%lu secondary=%lu"
+ "NLM: %@ '%{private}@' Secondary (Thread) addresses:"
+ "NLM: %@ '%{private}@' Seeding open from pulled resolver snapshot (primary=%lu secondary=%lu)"
+ "NLM: %@ '%{private}@' Skipping IPv6 for primary (IPv4-only policy): %@"
+ "NLM: %@ '%{private}@' Started resolver"
+ "NLM: %@ '%{private}@' resolved %lu IP address(es) - Primary: %lu, Secondary: %lu"
+ "NLM: %@ - close (primary): state change completion has already been handled"
+ "NLM: %@ - close (single): state change completion has already been handled"
+ "NLM: %@ - finalize request: completion has already been handled"
+ "NLM: %@ - open (WiFi+Thread): state change completion has already been handled"
+ "NLM: %@ Accessory does not support full NLM (WiFi:%{BOOL}d Thread:%{BOOL}d KeepAlive:%{BOOL}d), skipping registration"
+ "NLM: %@ All interfaces: %@"
+ "NLM: %@ Cache-miss cancel close returned: code=%ld domain=%{public}@"
+ "NLM: %@ Cache-miss cancel-and-restart: clearing latch, resetting tried-set, canceling in-flight primary open"
+ "NLM: %@ Cache-miss grace expired; executing cancel"
+ "NLM: %@ Cache-miss grace timer fired but latch already clear; no-op"
+ "NLM: %@ Cancelled resolver"
+ "NLM: %@ Client to register not yet connected, deferring endpoint registration"
+ "NLM: %@ Close of exhausted primary client returned: %@"
+ "NLM: %@ Close of failed PV client returned: %@"
+ "NLM: %@ Close of failed primary client returned: %@"
+ "NLM: %@ Close of failed secondary client returned: %@"
+ "NLM: %@ Closed"
+ "NLM: %@ Closed%@"
+ "NLM: %@ Closing client while an open is in flight (primary=%d secondary=%d)"
+ "NLM: %@ Closing primary client"
+ "NLM: %@ Closing secondary client first"
+ "NLM: %@ Connected address for transport %lu is no longer advertised; %lu resolver address(es) available"
+ "NLM: %@ Created Thread client during refresh, opening..."
+ "NLM: %@ Created WiFi client during refresh, opening..."
+ "NLM: %@ Created secondary CoAP client for Thread address: %{private}s"
+ "NLM: %@ Creating secondary client alongside primary, %lu secondary addresses available"
+ "NLM: %@ Effective address selection fell back to cache (primary=%{BOOL}d secondary=%{BOOL}d)"
+ "NLM: %@ Endpoint already registered, skipping"
+ "NLM: %@ Executing deferred endpoint registration"
+ "NLM: %@ Failed to close dead primary client: %@"
+ "NLM: %@ Failed to close dead probe client: %@"
+ "NLM: %@ Failed to close dead secondary client: %@"
+ "NLM: %@ Failed to close secondary: %@"
+ "NLM: %@ Failed to close%@: %@"
+ "NLM: %@ Failed to close: %@"
+ "NLM: %@ Failed to get WiFi local endpoint: %@"
+ "NLM: %@ Failed to get secondary local endpoint: %@"
+ "NLM: %@ Failed to map WiFi IPv4 endpoint to IPv4-mapped IPv6"
+ "NLM: %@ Failed to open Thread client during refresh: %@"
+ "NLM: %@ Failed to open WiFi client during refresh: %@"
+ "NLM: %@ Failed to open primary client: %@"
+ "NLM: %@ Failed to open secondary client: %@"
+ "NLM: %@ Failed to register WiFi endpoint: %@"
+ "NLM: %@ Failed to register endpoint: %@"
+ "NLM: %@ Failed to start address resolver"
+ "NLM: %@ Initial primary list is cache-only; arming stopgap latch at connect start"
+ "NLM: %@ Initial resolver complete in state %lu (not Opening), ignoring"
+ "NLM: %@ Last client disconnected, tearing down transport"
+ "NLM: %@ Live primary IPs arrived off-queue while cache-only latch armed; arming grace timer to evaluate the cancel"
+ "NLM: %@ Live primary arrived %.3fs into cache-only attempt (>1s); canceling immediately"
+ "NLM: %@ Live primary arrived %.3fs into cache-only attempt; arming %.3fs grace timer"
+ "NLM: %@ Live update: bringing up missing primary client"
+ "NLM: %@ Live update: bringing up missing secondary client"
+ "NLM: %@ Local IPv4: %s:%u"
+ "NLM: %@ Local IPv6: [%s]:%u"
+ "NLM: %@ Lost advertisement — clearing WiFi/Thread flags"
+ "NLM: %@ Message %u - Dropping stale Thread response (WiFi already won)"
+ "NLM: %@ Message %u - Dropping stale WiFi response (Thread already won)"
+ "NLM: %@ Message %u - Rcvd via Thread (Received response in %.0fms)"
+ "NLM: %@ Message %u - Rcvd via Wi-Fi (Received response in %.0fms)"
+ "NLM: %@ Message %u - Rcvd via Wi-Fi (Received response in %.0fms, updating EstimatedRTT to %.0fms)"
+ "NLM: %@ Message %u - Send via Thread (No response from Wi-Fi, sending over Thread)"
+ "NLM: %@ Message %u - Send via Wi-Fi (Fallback timeout: %.0fms)"
+ "NLM: %@ Message %u - Thread failed (code %ld), Wi-Fi still outstanding"
+ "NLM: %@ Message %u - Thread failed after %.0fms (code %ld)"
+ "NLM: %@ Message %u - Thread failed late (code %ld), WiFi won"
+ "NLM: %@ Message %u - Wi-Fi error, racing over Thread"
+ "NLM: %@ Message %u - Wi-Fi failed (code %ld), Thread still outstanding"
+ "NLM: %@ Message %u - Wi-Fi failed after %.0fms (code %ld)"
+ "NLM: %@ Message %u - Wi-Fi failed late (code %ld), Thread won"
+ "NLM: %@ No WiFi client to register"
+ "NLM: %@ No delegate to publish advertisement state — wifi=%{BOOL}d thread=%{BOOL}d"
+ "NLM: %@ No secured client available for endpoint registration"
+ "NLM: %@ No secured client for WiFi registration"
+ "NLM: %@ No untried secondary addresses available, skipping secondary client creation"
+ "NLM: %@ Now closing primary client"
+ "NLM: %@ Now opening Thread client"
+ "NLM: %@ Only one transport available (WiFi:%@, Thread:%@), skipping registration"
+ "NLM: %@ Open Client after Resolve"
+ "NLM: %@ Opened (WiFi:%@, Thread:%@)"
+ "NLM: %@ Opening WiFi client first, then Thread"
+ "NLM: %@ Opening primary client"
+ "NLM: %@ Pair-verify complete, secured client: %@"
+ "NLM: %@ Pair-verify was Thread, registering WiFi endpoint"
+ "NLM: %@ Pair-verify was WiFi, registering Thread endpoint"
+ "NLM: %@ Primary CoAP client already exists, skipping creation"
+ "NLM: %@ Primary IPs exhausted; no more to try"
+ "NLM: %@ Primary client disconnected (error: %@), continuing with Secondary-only"
+ "NLM: %@ Primary client opened"
+ "NLM: %@ Publishing advertisement state — wifi=%{BOOL}d thread=%{BOOL}d"
+ "NLM: %@ RTT tracking enabled on session"
+ "NLM: %@ Refresh resolved primary address: %{private}s"
+ "NLM: %@ Refresh resolved secondary address: %{private}s"
+ "NLM: %@ Refresh: found Thread address, creating client"
+ "NLM: %@ Refresh: found WiFi address, creating client"
+ "NLM: %@ Refresh: have Thread address, creating client"
+ "NLM: %@ Refresh: have WiFi address, creating client"
+ "NLM: %@ Refresh: primary IPs exhausted; no more to try"
+ "NLM: %@ Refresh: secondary IPs exhausted; no more to try"
+ "NLM: %@ Refresh: trying next primary IP after open failure"
+ "NLM: %@ Refresh: trying next secondary IP after open failure"
+ "NLM: %@ Registering WiFi endpoint via secured Thread client"
+ "NLM: %@ Registering secondary endpoint [%02x%02x:...:%02x%02x]:%u (%zu bytes)"
+ "NLM: %@ Request failed: %@"
+ "NLM: %@ Requesting discovery reconfirm after ICMP port unreachable"
+ "NLM: %@ Requesting discovery reconfirm after failing to open"
+ "NLM: %@ Resolve completed in state %lu (not Opening), ignoring stale resolve"
+ "NLM: %@ Resolve discovered 0 addresses in state %lu (not Opening), ignoring"
+ "NLM: %@ Resolved '%{private}@' but can't print the address..."
+ "NLM: %@ Resolved '%{private}@' to %{private}s (%s, discovered %lu, tried %lu)"
+ "NLM: %@ Secondary CoAP client already exists, skipping creation"
+ "NLM: %@ Secondary IPs exhausted; no more to try"
+ "NLM: %@ Secondary client closed"
+ "NLM: %@ Secondary client disconnected (error: %@), continuing with Primary-only"
+ "NLM: %@ Secondary client opened"
+ "NLM: %@ Secured client (primary) disconnected, transferring to secondary"
+ "NLM: %@ Secured client (secondary) disconnected, transferring to primary"
+ "NLM: %@ Sending endpoint registration via secured client: %@"
+ "NLM: %@ Sending via primary only (secondary not registered) [MID:%u]"
+ "NLM: %@ Successfully registered WiFi endpoint, racing enabled!"
+ "NLM: %@ Successfully registered secondary endpoint"
+ "NLM: %@ Thread client opened during refresh"
+ "NLM: %@ Thread-only connection: creating secondary client only, coapClient will be nil"
+ "NLM: %@ Thread-only mode: closing secondary client"
+ "NLM: %@ Thread-only mode: opening secondary client"
+ "NLM: %@ Thread-only mode: sending request via secondary client [MID:%u]"
+ "NLM: %@ Transport capabilities - WiFi:%@ Thread:%@ KeepAlive:%@"
+ "NLM: %@ Trying next primary IP after open failure"
+ "NLM: %@ Trying next secondary IP after open failure"
+ "NLM: %@ WiFi client opened, registering via secured Thread..."
+ "NLM: %@ _refreshIPAddresses - already have both clients, skipping"
+ "NLM: %@ _refreshIPAddresses - both clients alive, skipping"
+ "NLM: %@ _refreshIPAddresses - bringing up missing clients (needsPrimary=%d, needsSecondary=%d)"
+ "NLM: %@ _refreshIPAddresses - request in flight, deferring"
+ "NLM: %@ _refreshIPAddresses - tearing down dead Thread client"
+ "NLM: %@ _refreshIPAddresses - tearing down dead WiFi client"
+ "NLM: %@ advanceEndpoint: %@ picker exhausted"
+ "NLM: %@ advanceEndpoint: NLM disabled, no iteration"
+ "NLM: %@ advanceEndpoint: close already queued, not iterating"
+ "NLM: %@ advanceEndpoint: failed to open new %@ client: %@"
+ "NLM: %@ advanceEndpoint: no %@ client after build, cannot open"
+ "NLM: %@ advanceEndpoint: no active client to advance from"
+ "NLM: %@ advanceEndpoint: primary picker exhausted, retrying PV on secondary"
+ "NLM: %@ advanceEndpoint: swapping %@ client for fresh client at next IP"
+ "NLM: %@ applyResolverAddresses applied on queue (state=%lu primary=%lu secondary=%lu initialResolveCompleted=%{BOOL}d)"
+ "NLM: %@ getLocalIPv4Endpoint called"
+ "NLM: %@ getLocalIPv6Endpoint called"
+ "NLM: %@ isThreadIPv6Address: %{BOOL}d"
+ "NLM: %@ mergeWithNewTransport - names changed, recycling resolver"
+ "NLM: %@ mergeWithNewTransport - state Open, refreshing IP addresses (resolver browser-owned)"
+ "NLM: %@ mergeWithNewTransport - state is Open, refreshing IP addresses"
+ "NLM: %@ securedClient doesn't match either client, cannot register"
+ "NLM: %@ session->addr_info.local family: %d (AF_INET=%d, AF_INET6=%d)"
+ "NLM: %{public}@ resolver:didUpdateAddresses: cache-only latch armed — forwarding off-queue to bypass Server queue held by pair-verify"
+ "NLM: <Ping id=%lu> received from accessory"
+ "NLM: All transports hit failure threshold; marking accessory unreachable"
+ "NLM: Attached to resolver for deviceID=%{public}@"
+ "NLM: Browser audit pass — active=%lu"
+ "NLM: Configured transport %@ with maxInterval %.1fs"
+ "NLM: Controller forwarding PV-failure deviceID=%{public}@ transport=%lu domain=%{public}@ code=%ld"
+ "NLM: Controller forwarding PV-success deviceID=%{public}@ transport=%lu"
+ "NLM: Controller forwarding Thread advertisement %@"
+ "NLM: Controller forwarding WiFi advertisement %@"
+ "NLM: Controller forwarding heartbeat on transport %ld"
+ "NLM: DNSServiceResolve SRV changed (hostChanged=%d portChanged=%d); rebuilding getaddrinfo pipeline"
+ "NLM: DNSServiceResolve callback err=%d"
+ "NLM: DNSServiceResolve setup failed err=%d"
+ "NLM: Failed to apply RTT sample %.3fs (error %d)\n"
+ "NLM: Heartbeat received for untracked transport %ld"
+ "NLM: Heartbeat received on transport %ld"
+ "NLM: Heartbeat received on transport %ld, connectionState=%ld"
+ "NLM: Heartbeat received on transport %ld, resetting missed flag"
+ "NLM: Heartbeat received while not connected — restoring connectivity"
+ "NLM: Invalid maxInterval for transport %ld"
+ "NLM: Missed heartbeat on transport %@, time since last: %.1fs"
+ "NLM: Missed heartbeat on transport %ld, expected %.1fs, since last %.1fs"
+ "NLM: No free slots in pending request array\n"
+ "NLM: No tracked transports with positive maxInterval — listener idle"
+ "NLM: PV-failure classify deviceID=%{public}@ transport=%lu domain=%{public}@ code=%ld evict=%d"
+ "NLM: PV-success cascade deviceID=%{public}@ transport=%lu"
+ "NLM: PV-success drop — no resolver attached for deviceID=%{public}@"
+ "NLM: Probe already in flight, rejecting new probe"
+ "NLM: Probe-driven recovery failure %lu/%lu for transport %ld: %@"
+ "NLM: Probe-driven recovery succeeded for transport %ld; clearing failure counter"
+ "NLM: Probe-driven recovery succeeded — restoring connectivity (state %lu → Connected)"
+ "NLM: RTT tracking array full (32 pending), evicting oldest for MID=%u\n"
+ "NLM: Re-advertisement (resolver path) deviceID=%{public}@, triggering updateReachability"
+ "NLM: Received Empty CON ping (MID=%d), sending RST"
+ "NLM: Received ping from unknown client"
+ "NLM: Rejecting negative RTT sample: %.3f\n"
+ "NLM: Resetting heartbeat timestamps to now"
+ "NLM: Restarting keep-alive listener"
+ "NLM: SecureTransportBase forwarding heartbeat on transport %ld"
+ "NLM: Send keep-alive probe"
+ "NLM: Sent Empty CON probe, MID=%lu"
+ "NLM: Server torn down before resolver:didUpdateAddresses: block ran on operationQueue for deviceID=%{public}@; dropping update"
+ "NLM: Starting keep-alive listener with %lu transports"
+ "NLM: Stopping keep-alive listener"
+ "NLM: Stopping keep-alive listener (dealloc)"
+ "NLM: Timer fired for transport %@, but heartbeat received %.1fs ago (within %.1fs window) — not a miss"
+ "NLM: Transport %ld destination is unadvertised; closing session"
+ "NLM: Transport deallocated before RTT stats completion [MID:%u]"
+ "NLM: [%{private}@] Discarded probe failure (code %ld) for MID %u, outstanding MID %u"
+ "NLM: dnssd_getaddrinfo error event err=%d"
+ "NLM: dnssd_getaddrinfo_create failed"
+ "NLM: resolver update deviceID=%{public}@ hasPTR=%{public}d primary=%lu secondary=%lu was=%{public}d now=%{public}d"
+ "NLM: tried-key encoder received unsupported address family %u; upstream filter regression?"
+ "NetworkLinkManagement"
+ "No active CoAP session"
+ "No active session"
+ "Not restoring HH2 controller key %@ from the back up list"
+ "Pair Setup completed with err: %d, MFi Cert %@"
+ "Pair-setup after M4, flags %08X productData %@"
+ "Pair-setup: M5 failed, ending pair-setup: %{public}s"
+ "PreferredNetworkUpdated"
+ "Primary"
+ "PropVal"
+ "Q\xd1"
+ "Received ping with message id %i but session has no app data"
+ "Refusing AES-CCM pair-setup: primary resident does not support ECDSA keys (featureFlags=0x%llx)"
+ "Refusing AES-CCM pair-setup: primary resident does not support ECDSA keys (featureFlags=0x%x)"
+ "Refusing AES-CCM pair-setup: primary resident does not support ECDSA keys (features=0x%llx)"
+ "Registry: audit reconciling orphan PTR for deviceID=%{public}@ — recreating resolver from retained serviceName"
+ "Registry: cleaned up resolver for empty+idle deviceID=%{public}@"
+ "Registry: created resolver for deviceID=%{public}@ serviceName='%{private}@'"
+ "Registry: removeResolverForDeviceID no-op for unknown deviceID=%{public}@"
+ "Registry: removed resolver for deviceID=%{public}@"
+ "Registry: updateCachedAddresses no-op for unknown deviceID=%{public}@"
+ "Rejecting cache record for device %{public}@: version type=%{public}@ expected=%ld"
+ "Resolver pipeline factory returned nil"
+ "Resolver pipeline failed"
+ "Resolver timed out before first update"
+ "Resolver: attachDelegate for deviceID=%{public}@ -> %lu delegate(s), snapshot primary=%lu secondary=%lu"
+ "Resolver: cachedIP %{public}@ deviceID=%{public}@ transport=%lu"
+ "Resolver: cachedIPDidUpdate no-op (same pointer) deviceID=%{public}@ transport=%lu"
+ "Resolver: dropping IPv6 address from primary list (IPv4-only policy) for deviceID=%{public}@"
+ "Resolver: fanned out update for deviceID=%{public}@ to %lu delegate(s) (primary=%lu secondary=%lu)"
+ "Resolver: never-delivered health-check restart for deviceID=%{public}@"
+ "Resolver: pipeline delivered fatal error for deviceID=%{public}@ domain=%{public}@ code=%ld marker=%ld"
+ "Resolver: pipeline factory failed for deviceID=%{public}@"
+ "Resolver: serviceName updated for deviceID=%{public}@ to '%{private}@'"
+ "Resolver: torn down pipeline for deviceID=%{public}@"
+ "Retrieved Thread mesh local prefix: %{private}@"
+ "Returning ECDSA local pairing identity for security session: %@, with error: %@"
+ "Secondary"
+ "Secondary(Thread)"
+ "Secure Transport: Ignoring ECDSA pair verify success from a previous open"
+ "Secure Transport: Ignoring ECDSA session failure from a previous open"
+ "Secure Transport: Not closing after ECDSA session failure; transport is owned elsewhere"
+ "Session keep-alive detected missed heartbeats on all transports"
+ "Tearing down session as a result of disconnect with completion call"
+ "Thread mesh local prefix property not found in response"
+ "Timed out, Not handling pending Bonjour for %{public}@, as session restore is active"
+ "Unknown HAPAVCStreamingControlCommand %ld"
+ "Unknown HAPAVCStreamingControlStatus %ld"
+ "Unknown HAPAVCViewerRegistrationOperation %ld"
+ "Unknown HAPMetricEventBluetoothVersionType %ld"
+ "Unknown HAPMetricEventPowerSourcesEnum %ld"
+ "Unknown HAPMetricEventWiFiVersionType %ld"
+ "Unknown HAPSessionKeepAliveTransportType %ld"
+ "Unknown HAPStabilityMetricsBootReasonType %ld"
+ "Unknown HAPStabilityMetricsHardwareFaultType %ld"
+ "Unpair: evicted cache entry deviceID=%{public}@"
+ "Unsupported local address family"
+ "Using Pairing Identity: %{public}@"
+ "[%{public}@] Attempting to derive HDS keys without an active session"
+ "[%{public}@] Disconnect request is not supported for %{public}@"
+ "[%{public}@] Failed to derive HDS keys from foreign pair-verify session: %@"
+ "[%{public}@] Failed to remove the pairing identity backups: %ld"
+ "[%{public}@] Found thread accessory with server ID known = %d paired = %d"
+ "[%{public}@] HAPMetadataCharacteristic %@(%@): description: %@"
+ "[%{public}@] HAPMetadataUnit %@: description: %@"
+ "[%{public}@] HDS key derivation failed (pairedServer=%p controller=%p secureTransport=%p)"
+ "[%{public}@] HDS key derivation failed: no security session on HAP2 secure transport"
+ "[%{public}@] HDS peer address unavailable (pairedServer=%p controller=%p secureTransport=%p coapTransport=%p)"
+ "[%{public}@] Invalid cachedPrimaryData type for device %{public}@"
+ "[%{public}@] Invalid cachedSecondaryData type for device %{public}@"
+ "[%{public}@] Invalid or missing configurationInfo for device %{public}@"
+ "[%{public}@] Legacy WAC accessory Bonjour event - hasPairings %d continuingLegacyPairing: %d"
+ "[%{public}@] Not restoring HH2 controller key %@ from the back up list"
+ "[%{public}@] Pair Setup completed with err: %d, MFi Cert %@"
+ "[%{public}@] Pair-setup after M4, flags %08X productData %@"
+ "[%{public}@] Refusing AES-CCM pair-setup: primary resident does not support ECDSA keys (featureFlags=0x%llx)"
+ "[%{public}@] Refusing AES-CCM pair-setup: primary resident does not support ECDSA keys (featureFlags=0x%x)"
+ "[%{public}@] Refusing AES-CCM pair-setup: primary resident does not support ECDSA keys (features=0x%llx)"
+ "[%{public}@] Rejecting cache record for device %{public}@: version type=%{public}@ expected=%ld"
+ "[%{public}@] Returning ECDSA local pairing identity for security session: %@, with error: %@"
+ "[%{public}@] Tearing down session as a result of disconnect with completion call"
+ "[%{public}@] Timed out, Not handling pending Bonjour for %{public}@, as session restore is active"
+ "[%{public}@] [IP Accessory Server HTTP Client] Failed to get self address %d client ref %p"
+ "[%{public}@] configureKeepAliveListener called -- NOP"
+ "[IP Accessory Server HTTP Client] Failed to get self address %d client ref %p"
+ "adaptiveTimeout"
+ "cachedIPDidUpdate persisted deviceID=%{public}@ transport=%lu op=%{public}@"
+ "cachedPrimaryData"
+ "cachedSecondaryData"
+ "clear"
+ "cleared"
+ "coap-client"
+ "coap_session_create_client"
+ "com.apple.CoreHAP.HAP2.BrowserResolverRegistry.audit"
+ "com.apple.CoreHAP.HAP2ThreadNetworkUtil.events"
+ "com.apple.HomeKit.daemon.Accessory.CHM"
+ "com.apple.HomeKit.daemon.Accessory.CHM.Recovery"
+ "configurationInfo"
+ "configureKeepAliveListener called -- NOP"
+ "deriveSessionKeyWithSalt:info:error: returned nil without error"
+ "deviationRTT"
+ "deviceID=%{public}@ fast-set hasThreadAdvertisement=%{public}d"
+ "deviceID=%{public}@ fast-set hasWiFiAdvertisement=%{public}d"
+ "errorCode=%d"
+ "errorCode=%d hosttarget=%s"
+ "estimatedRTT"
+ "getifaddrs failed: %s"
+ "hap2.resolver.propertyLock.%@"
+ "hasDiscoveryAdvertisement=YES(ptr) deviceID=%{public}@"
+ "hasThreadAdvertisement=YES(ptr) deviceID=%{public}@"
+ "hasWiFiAdvertisement=YES(ptr) deviceID=%{public}@"
+ "honoured"
+ "init(startTime:)"
+ "interfaceName"
+ "invalid"
+ "isThread"
+ "networks"
+ "none"
+ "not honoured"
+ "resolverRegistry"
+ "secondary"
+ "secondary-coap-client"
+ "selectedMaxInterval"
+ "selectedMinInterval"
+ "sessionLossCount"
+ "set"
+ "setIPCache ignored — initialization from cache has already run"
+ "setupEventSubscriptions: CoreThreadRadio framework not available"
+ "supported"
+ "threadConnectivityState"
+ "threadRecoveryAttemptCount"
+ "threadRestartCount"
+ "threadTransportLossCount"
+ "unsupported"
+ "v16@?0@\"NSArray\"8"
+ "v16@?0i8i12"
+ "v24@?0@\"HAP2CoAPClient\"8^{coap_session_t=CCCIII{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}}^{coap_endpoint_t}^{coap_context_t}^vSCi^{coap_queue_t}Q[8C]Q^{coap_pdu_t}QQQQQ*Q*Q^vI{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}IidddIddddCddI[32{?=SdC}]}16"
+ "v24@?0^@8Q16"
+ "v24@?0^{coap_context_t=[6S]^{coap_resource_t}^{coap_resource_t}^{coap_async_state_t}Q^{coap_queue_t}^{coap_endpoint_t}^{coap_session_t}^?^?^?^?^?^?^?^?^?^?^v*Q*QIIIII^v}8^{coap_session_t=CCCIII{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}}^{coap_endpoint_t}^{coap_context_t}^vSCi^{coap_queue_t}Q[8C]Q^{coap_pdu_t}QQQQQ*Q*Q^vI{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}IidddIddddCddI[32{?=SdC}]}16"
+ "v24@?0{shared_ptr<CtrXPC::Event>=^{Event}^{__shared_weak_count}}8"
+ "v28@?0@\"NSData\"8S16@\"NSError\"20"
+ "v32@?0@\"NSData\"8@\"NSString\"16@\"NSError\"24"
+ "version"
+ "wifiConnectivityState"
+ "wifiRecoveryAttemptCount"
+ "wifiRestartCount"
+ "wifiTransportLossCount"
+ "\x8b"
+ "\x91"
+ "\x91\xf0\xf0Q!"
- "!Aq"
- "\"5"
- "%@ '%{private}@' resolves to %lu address(es), %@"
- "%@ Browser fast-set hasDiscoveryAdvertisement=%{public}d"
- "%@ Failed to fetch ECDSA controller key for %@: %@"
- "%@ Failed to fetch ECDSA key for peer %@: %@"
- "&"
- "<HAPAVCViewerRegistrationRequest sessionIdentifier=%@, viewerParticipantID=%@, viewerNegotiationBlob=%@>"
- "<HAPWebRTCOfferOptions SFrameEnabled=%@>"
- "HAPAVCNegotiationStatusBusy"
- "HAPAVCNegotiationStatusUnknownSessionIdentifier"
- "HAPMetadataCharacteristic %@(%@):  description: %@"
- "HAPMetadataUnit %@:  description: %@"
- "Key Bag Pairing Identity to derive ECDSA Key: %@"
- "Legacy WAC accessory Bonjour event - hasPairings %d  continuingLegacyPairing: %d"
- "MFi early-auth: DISMISSED — M4 sent a full token (%ld bytes), not the primed hash; abandoning tap-time validate+roll, validating M4 token"
- "MFi early-auth: M4 hash verified and validate+roll already finished — using its result for M5"
- "Pair Setup completed with err: %d,  MFi Cert %@"
- "Pair-setup M6 bad status %hhu"
- "Pair-setup after M4, flags %08X  productData %@"
- "Pair-setup: M5: Unable to retrieve pairing identity: %s"
- "Q\xc1"
- "Returning ECDSA local pairng identity for security session: %@, with error: %@"
- "Secure Transport PairVerify: Timed out waiting for ECDSA key for peer %@"
- "Secure Transport PairVerify: Timed out waiting for local ECDSA pair-setup identity"
- "Secure Transport PairVerify: Timed out waiting for local pairing identity"
- "Secure Transport PairVerify: Timed out waiting for remote pairing identity"
- "Secure Transport: Finished force closing after ECDSA pair verify failure"
- "Secure Transport: Finished force closing after ECDSA session failure"
- "Timed out,  Not handling pending Bonjour for %{public}@, as session restore is active"
- "Using ECDSA Controller Pairing Identity: %@"
- "Using Pairing Identity: %@"
- "[%{public}@] HAPMetadataCharacteristic %@(%@):  description: %@"
- "[%{public}@] HAPMetadataUnit %@:  description: %@"
- "[%{public}@] Legacy WAC accessory Bonjour event - hasPairings %d  continuingLegacyPairing: %d"
- "[%{public}@] Pair Setup completed with err: %d,  MFi Cert %@"
- "[%{public}@] Pair-setup after M4, flags %08X  productData %@"
- "[%{public}@] Returning ECDSA local pairng identity for security session: %@, with error: %@"
- "[%{public}@] Timed out,  Not handling pending Bonjour for %{public}@, as session restore is active"
- "aborting"
- "trying first address"
- "v24@?0@\"HAP2CoAPClient\"8^{coap_session_t=CCCIII{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}}^{coap_endpoint_t}^{coap_context_t}^vSCi^{coap_queue_t}Q[8C]Q^{coap_pdu_t}QQQQQ*Q*Q^vI{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}Ii}16"
- "v24@?0^{coap_context_t=[6S]^{coap_resource_t}^{coap_resource_t}^{coap_async_state_t}Q^{coap_queue_t}^{coap_endpoint_t}^{coap_session_t}^?^?^?^?^?^?^?^?^?^?^v*Q*QIIIII^v}8^{coap_session_t=CCCIII{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}}^{coap_endpoint_t}^{coap_context_t}^vSCi^{coap_queue_t}Q[8C]Q^{coap_pdu_t}QQQQQ*Q*Q^vI{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}Ii}16"
- "\x81\xf0\xb1!"
- "\x8a"
- "\xd1"
```
