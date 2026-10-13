## CoreHAP

> `/System/Library/PrivateFrameworks/CoreHAP.framework/CoreHAP`

```diff

-1520.2.3.0.2
-  __TEXT.__text: 0x2ac69c
-  __TEXT.__objc_methlist: 0x195f0
-  __TEXT.__const: 0x13b0
+1520.2.7.1.3
+  __TEXT.__text: 0x2f9040
+  __TEXT.__objc_methlist: 0x1c9d8
+  __TEXT.__const: 0x1818
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__constg_swiftt: 0xa64
-  __TEXT.__swift5_typeref: 0x437
-  __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_reflstr: 0x581
-  __TEXT.__swift5_fieldmd: 0x49c
-  __TEXT.__swift5_assocty: 0xd8
-  __TEXT.__swift5_proto: 0x5c
-  __TEXT.__swift5_types: 0x34
-  __TEXT.__cstring: 0x14b39
-  __TEXT.__oslogstring: 0x46315
+  __TEXT.__constg_swiftt: 0xc20
+  __TEXT.__swift5_typeref: 0x533
+  __TEXT.__swift5_builtin: 0xdc
+  __TEXT.__swift5_reflstr: 0x851
+  __TEXT.__swift5_fieldmd: 0x6a4
+  __TEXT.__swift5_assocty: 0x138
+  __TEXT.__swift5_proto: 0x78
+  __TEXT.__swift5_types: 0x5c
+  __TEXT.__cstring: 0x17714
+  __TEXT.__oslogstring: 0x4b2bb
+  __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_capture: 0x28c
-  __TEXT.__gcc_except_tab: 0x5ef8
-  __TEXT.__unwind_info: 0x8d40
+  __TEXT.__gcc_except_tab: 0x6f8c
+  __TEXT.__unwind_info: 0x9e50
   __TEXT.__eh_frame: 0x1078
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5948
-  __DATA_CONST.__objc_classlist: 0xc68
+  __DATA_CONST.__const: 0x6300
+  __DATA_CONST.__objc_classlist: 0xda0
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x3c0
+  __DATA_CONST.__objc_protolist: 0x3f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x85d8
-  __DATA_CONST.__objc_protorefs: 0x100
-  __DATA_CONST.__objc_superrefs: 0xaa8
+  __DATA_CONST.__objc_selrefs: 0x98f8
+  __DATA_CONST.__objc_protorefs: 0x110
+  __DATA_CONST.__objc_superrefs: 0xbc0
   __DATA_CONST.__objc_arraydata: 0x200
-  __DATA_CONST.__got: 0x1098
-  __AUTH_CONST.__const: 0x1548
-  __AUTH_CONST.__cfstring: 0x10360
-  __AUTH_CONST.__objc_const: 0x2c388
-  __AUTH_CONST.__weak_auth_got: 0x8
-  __AUTH_CONST.__objc_intobj: 0x738
+  __DATA_CONST.__got: 0x11c8
+  __AUTH_CONST.__const: 0x1738
+  __AUTH_CONST.__cfstring: 0x117a0
+  __AUTH_CONST.__objc_const: 0x32290
+  __AUTH_CONST.__weak_auth_got: 0x10
+  __AUTH_CONST.__objc_intobj: 0x750
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0xc0
-  __AUTH_CONST.__auth_got: 0x13a0
-  __AUTH.__objc_data: 0x76f8
-  __AUTH.__data: 0xb0
+  __AUTH_CONST.__auth_got: 0x1448
+  __AUTH.__objc_data: 0x84c0
+  __AUTH.__data: 0x130
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x28
-  __DATA.__objc_ivar: 0x19b4
-  __DATA.__data: 0x2eb2
+  __DATA.__objc_ivar: 0x1e08
+  __DATA.__data: 0x31b8
   __DATA.__crash_info: 0x148
-  __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x1068
+  __DATA.__common: 0x90
+  __DATA_DIRTY.__objc_data: 0x1108
   __DATA_DIRTY.__data: 0x48
-  __DATA_DIRTY.__bss: 0xc8
+  __DATA_DIRTY.__bss: 0xf0
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10054
-  Symbols:   16838
-  CStrings:  7261
+  Functions: 11431
+  Symbols:   18803
+  CStrings:  7784
 
Symbols:
+ +[HAP2AccessoryDeviceIPAddress accessoryDeviceIPAddressWithSerializedData:]
+ +[HAP2AccessoryServerCoordinator(Test) coordinatorForUnitTestsWithBrowser:operationQueue:delegate:]
+ +[HAP2AccessoryServerDiscoveryHAPAccessoryInfo accessoryInfoWithDeviceID:rawDiscoveryInfo:]
+ +[HAP2AccessoryServerIPCacheData dataWithDictionary:deviceID:]
+ +[HAP2AccessoryServerIPCacheData logCategory]
+ +[HAP2SessionKeepAliveConfiguration computeSelectedConfigurationForTransportType:isSleepyEndDevice:supportedMinInterval:supportedMaxInterval:supportedMinRange:]
+ +[HAPBluetoothMetrics parsedFromData:error:]
+ +[HAPBootReasonsMetrics parsedFromData:error:]
+ +[HAPCHMMetrics parsedFromData:error:]
+ +[HAPConnectionHealthMonitor parsedFromData:error:]
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
+ -[HAP2AccessoryAddressLists cachedPrimary]
+ -[HAP2AccessoryAddressLists cachedSecondary]
+ -[HAP2AccessoryAddressLists initWithPrimary:secondary:cachedPrimary:cachedSecondary:]
+ -[HAP2AccessoryAddressLists setCachedPrimary:]
+ -[HAP2AccessoryAddressLists setCachedSecondary:]
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
+ -[HAP2AccessoryDeviceIPAddress debugDescription]
+ -[HAP2AccessoryDeviceIPAddress isIPv6]
+ -[HAP2AccessoryDeviceIPAddress serializedData]
+ -[HAP2AccessoryDeviceIPAddress transportType]
+ -[HAP2AccessoryServer _attachResolverAndForwardToTransport:]
+ -[HAP2AccessoryServer _runLostDiscoveryAdvertisementSideEffectsWithWillSleep:]
+ -[HAP2AccessoryServer _runResolverReactiveWorkWithWas:now:connectionState:]
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
+ -[HAP2AccessoryServerBrowser existingPTRs]
+ -[HAP2AccessoryServerBrowser hasCurrentPTRForDeviceID:]
+ -[HAP2AccessoryServerBrowser hasDiscoveryAdvertisementForAccessoryWithID:]
+ -[HAP2AccessoryServerBrowser hasThreadAdvertisementForAccessoryWithID:]
+ -[HAP2AccessoryServerBrowser hasWiFiAdvertisementForAccessoryWithID:]
+ -[HAP2AccessoryServerBrowser ipCache]
+ -[HAP2AccessoryServerBrowser isInitialCacheRestored]
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
+ -[HAP2AccessoryServerController hasArmedCacheOnlyLatch]
+ -[HAP2AccessoryServerController readLocalEndpointsWithHandler:]
+ -[HAP2AccessoryServerController secureTransport:didChangeThreadAdvertisement:]
+ -[HAP2AccessoryServerController secureTransport:didChangeWiFiAdvertisement:]
+ -[HAP2AccessoryServerController secureTransport:didReceiveHeartbeatOnTransport:]
+ -[HAP2AccessoryServerController secureTransport:pairVerifyDidCompleteOnIPAddress:transportType:]
+ -[HAP2AccessoryServerController secureTransport:pairVerifyDidFailOnIPAddress:transportType:error:]
+ -[HAP2AccessoryServerController secureTransportCurrentResolverSnapshot:]
+ -[HAP2AccessoryServerController sendProbeOnTransport:completion:]
+ -[HAP2AccessoryServerCoordinator initializePairedAccessoryServerFromCachedInfo:]
+ -[HAP2AccessoryServerCoordinator(Test) _test_deliverDiscovery:]
+ -[HAP2AccessoryServerCoordinator(Test) _test_deliverLoss:]
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
+ -[HAPAccessoryServer configureKeepAliveListener:]
+ -[HAPAccessoryServer hasThreadAdvertisement]
+ -[HAPAccessoryServer hasWiFiAdvertisement]
+ -[HAPAccessoryServer lastPairSetupWasSpake2]
+ -[HAPAccessoryServer setHasThreadAdvertisement:]
+ -[HAPAccessoryServer setHasWiFiAdvertisement:]
+ -[HAPAccessoryServer setLastPairSetupWasSpake2:]
+ -[HAPAccessoryServerBrowserHAP2Adapter setIPCache:]
+ -[HAPAccessoryServerHAP2Adapter accessoryServer:didUpdateLocalEndpoints:]
+ -[HAPAccessoryServerHAP2Adapter configureKeepAliveListener:]
+ -[HAPAccessoryServerHAP2Adapter dataStreamPeerAddressWithCompletion:]
+ -[HAPAccessoryServerHAP2Adapter deriveEncryptionForDataStreamWithKeySalt:completionHandler:]
+ -[HAPAccessoryServerHAP2Adapter hasThreadAdvertisement]
+ -[HAPAccessoryServerHAP2Adapter hasWiFiAdvertisement]
+ -[HAPAccessoryServerIP hasWiFiAdvertisement]
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
+ GCC_except_table10019
+ GCC_except_table10097
+ GCC_except_table10099
+ GCC_except_table10101
+ GCC_except_table10103
+ GCC_except_table10105
+ GCC_except_table10107
+ GCC_except_table10109
+ GCC_except_table10115
+ GCC_except_table10117
+ GCC_except_table10120
+ GCC_except_table10122
+ GCC_except_table10124
+ GCC_except_table10131
+ GCC_except_table10137
+ GCC_except_table10142
+ GCC_except_table10145
+ GCC_except_table10150
+ GCC_except_table10155
+ GCC_except_table10158
+ GCC_except_table10161
+ GCC_except_table10187
+ GCC_except_table10190
+ GCC_except_table10191
+ GCC_except_table10230
+ GCC_except_table10231
+ GCC_except_table10232
+ GCC_except_table10234
+ GCC_except_table10235
+ GCC_except_table10237
+ GCC_except_table10238
+ GCC_except_table10239
+ GCC_except_table10241
+ GCC_except_table10242
+ GCC_except_table10244
+ GCC_except_table10248
+ GCC_except_table10249
+ GCC_except_table10253
+ GCC_except_table10304
+ GCC_except_table10311
+ GCC_except_table10419
+ GCC_except_table10421
+ GCC_except_table10423
+ GCC_except_table10426
+ GCC_except_table10428
+ GCC_except_table10430
+ GCC_except_table10432
+ GCC_except_table10433
+ GCC_except_table10440
+ GCC_except_table10442
+ GCC_except_table10443
+ GCC_except_table1131
+ GCC_except_table1133
+ GCC_except_table1200
+ GCC_except_table1202
+ GCC_except_table1204
+ GCC_except_table1206
+ GCC_except_table1746
+ GCC_except_table1751
+ GCC_except_table1753
+ GCC_except_table1767
+ GCC_except_table1779
+ GCC_except_table1783
+ GCC_except_table1785
+ GCC_except_table1915
+ GCC_except_table1919
+ GCC_except_table1921
+ GCC_except_table2123
+ GCC_except_table224
+ GCC_except_table225
+ GCC_except_table226
+ GCC_except_table233
+ GCC_except_table2339
+ GCC_except_table234
+ GCC_except_table2341
+ GCC_except_table2346
+ GCC_except_table2352
+ GCC_except_table2354
+ GCC_except_table2360
+ GCC_except_table2362
+ GCC_except_table2366
+ GCC_except_table2374
+ GCC_except_table2378
+ GCC_except_table2384
+ GCC_except_table2386
+ GCC_except_table2388
+ GCC_except_table2390
+ GCC_except_table2396
+ GCC_except_table240
+ GCC_except_table2400
+ GCC_except_table2408
+ GCC_except_table243
+ GCC_except_table2431
+ GCC_except_table2438
+ GCC_except_table2446
+ GCC_except_table2487
+ GCC_except_table251
+ GCC_except_table253
+ GCC_except_table257
+ GCC_except_table259
+ GCC_except_table2606
+ GCC_except_table2610
+ GCC_except_table2611
+ GCC_except_table2613
+ GCC_except_table2615
+ GCC_except_table2627
+ GCC_except_table2632
+ GCC_except_table2636
+ GCC_except_table2639
+ GCC_except_table2641
+ GCC_except_table2644
+ GCC_except_table2661
+ GCC_except_table2671
+ GCC_except_table2673
+ GCC_except_table2675
+ GCC_except_table268
+ GCC_except_table2680
+ GCC_except_table2683
+ GCC_except_table2685
+ GCC_except_table2688
+ GCC_except_table2691
+ GCC_except_table2695
+ GCC_except_table2697
+ GCC_except_table2700
+ GCC_except_table2703
+ GCC_except_table2705
+ GCC_except_table2707
+ GCC_except_table2711
+ GCC_except_table2715
+ GCC_except_table272
+ GCC_except_table2723
+ GCC_except_table2734
+ GCC_except_table276
+ GCC_except_table2777
+ GCC_except_table2778
+ GCC_except_table2779
+ GCC_except_table278
+ GCC_except_table2781
+ GCC_except_table2782
+ GCC_except_table2783
+ GCC_except_table2785
+ GCC_except_table2789
+ GCC_except_table2790
+ GCC_except_table2816
+ GCC_except_table2820
+ GCC_except_table2824
+ GCC_except_table2988
+ GCC_except_table2995
+ GCC_except_table2999
+ GCC_except_table3003
+ GCC_except_table3007
+ GCC_except_table3010
+ GCC_except_table3012
+ GCC_except_table3014
+ GCC_except_table3023
+ GCC_except_table3025
+ GCC_except_table3028
+ GCC_except_table3029
+ GCC_except_table3031
+ GCC_except_table3132
+ GCC_except_table3140
+ GCC_except_table3141
+ GCC_except_table3142
+ GCC_except_table3143
+ GCC_except_table3144
+ GCC_except_table3145
+ GCC_except_table3160
+ GCC_except_table3174
+ GCC_except_table3254
+ GCC_except_table3266
+ GCC_except_table3471
+ GCC_except_table3480
+ GCC_except_table3497
+ GCC_except_table3531
+ GCC_except_table3547
+ GCC_except_table3549
+ GCC_except_table3561
+ GCC_except_table3568
+ GCC_except_table3590
+ GCC_except_table3604
+ GCC_except_table3605
+ GCC_except_table3609
+ GCC_except_table3615
+ GCC_except_table3622
+ GCC_except_table3625
+ GCC_except_table3640
+ GCC_except_table3680
+ GCC_except_table3697
+ GCC_except_table3700
+ GCC_except_table3705
+ GCC_except_table3707
+ GCC_except_table3723
+ GCC_except_table3737
+ GCC_except_table3739
+ GCC_except_table3743
+ GCC_except_table3751
+ GCC_except_table3759
+ GCC_except_table3823
+ GCC_except_table3830
+ GCC_except_table3832
+ GCC_except_table3833
+ GCC_except_table3876
+ GCC_except_table4104
+ GCC_except_table4179
+ GCC_except_table4186
+ GCC_except_table4190
+ GCC_except_table4192
+ GCC_except_table4194
+ GCC_except_table4196
+ GCC_except_table4200
+ GCC_except_table4203
+ GCC_except_table4209
+ GCC_except_table4220
+ GCC_except_table4222
+ GCC_except_table4223
+ GCC_except_table4225
+ GCC_except_table4228
+ GCC_except_table4230
+ GCC_except_table4231
+ GCC_except_table4233
+ GCC_except_table4234
+ GCC_except_table4236
+ GCC_except_table4267
+ GCC_except_table4270
+ GCC_except_table4272
+ GCC_except_table4275
+ GCC_except_table4279
+ GCC_except_table4281
+ GCC_except_table4284
+ GCC_except_table4287
+ GCC_except_table4299
+ GCC_except_table4301
+ GCC_except_table4305
+ GCC_except_table4309
+ GCC_except_table4313
+ GCC_except_table4318
+ GCC_except_table4331
+ GCC_except_table4350
+ GCC_except_table4373
+ GCC_except_table4379
+ GCC_except_table4383
+ GCC_except_table4389
+ GCC_except_table4392
+ GCC_except_table4394
+ GCC_except_table4396
+ GCC_except_table4403
+ GCC_except_table4404
+ GCC_except_table4405
+ GCC_except_table4406
+ GCC_except_table4407
+ GCC_except_table4410
+ GCC_except_table4412
+ GCC_except_table4498
+ GCC_except_table4499
+ GCC_except_table4500
+ GCC_except_table4501
+ GCC_except_table4502
+ GCC_except_table4503
+ GCC_except_table4504
+ GCC_except_table4505
+ GCC_except_table4506
+ GCC_except_table4507
+ GCC_except_table4508
+ GCC_except_table4509
+ GCC_except_table4510
+ GCC_except_table4511
+ GCC_except_table4512
+ GCC_except_table4551
+ GCC_except_table4578
+ GCC_except_table4669
+ GCC_except_table4671
+ GCC_except_table4673
+ GCC_except_table4708
+ GCC_except_table4719
+ GCC_except_table4740
+ GCC_except_table4748
+ GCC_except_table4759
+ GCC_except_table4773
+ GCC_except_table4776
+ GCC_except_table4781
+ GCC_except_table4789
+ GCC_except_table4797
+ GCC_except_table4799
+ GCC_except_table4810
+ GCC_except_table4843
+ GCC_except_table4846
+ GCC_except_table4847
+ GCC_except_table4853
+ GCC_except_table4855
+ GCC_except_table4861
+ GCC_except_table4862
+ GCC_except_table4867
+ GCC_except_table4868
+ GCC_except_table4874
+ GCC_except_table4883
+ GCC_except_table4884
+ GCC_except_table4885
+ GCC_except_table4886
+ GCC_except_table4887
+ GCC_except_table4888
+ GCC_except_table4889
+ GCC_except_table4895
+ GCC_except_table4902
+ GCC_except_table4906
+ GCC_except_table4907
+ GCC_except_table4921
+ GCC_except_table4937
+ GCC_except_table4954
+ GCC_except_table4955
+ GCC_except_table4957
+ GCC_except_table4958
+ GCC_except_table4961
+ GCC_except_table4962
+ GCC_except_table4977
+ GCC_except_table4992
+ GCC_except_table4999
+ GCC_except_table5019
+ GCC_except_table5029
+ GCC_except_table5031
+ GCC_except_table5097
+ GCC_except_table5101
+ GCC_except_table5102
+ GCC_except_table5104
+ GCC_except_table5106
+ GCC_except_table5109
+ GCC_except_table5112
+ GCC_except_table5115
+ GCC_except_table5118
+ GCC_except_table5121
+ GCC_except_table5124
+ GCC_except_table5127
+ GCC_except_table5130
+ GCC_except_table5135
+ GCC_except_table5148
+ GCC_except_table5153
+ GCC_except_table5157
+ GCC_except_table5159
+ GCC_except_table5162
+ GCC_except_table5174
+ GCC_except_table5182
+ GCC_except_table5186
+ GCC_except_table5192
+ GCC_except_table5193
+ GCC_except_table5196
+ GCC_except_table5197
+ GCC_except_table5215
+ GCC_except_table5217
+ GCC_except_table5219
+ GCC_except_table5220
+ GCC_except_table5223
+ GCC_except_table5229
+ GCC_except_table5232
+ GCC_except_table5234
+ GCC_except_table5241
+ GCC_except_table5243
+ GCC_except_table5245
+ GCC_except_table5248
+ GCC_except_table5259
+ GCC_except_table5270
+ GCC_except_table5272
+ GCC_except_table5283
+ GCC_except_table5285
+ GCC_except_table5287
+ GCC_except_table5293
+ GCC_except_table547
+ GCC_except_table557
+ GCC_except_table5575
+ GCC_except_table5581
+ GCC_except_table5598
+ GCC_except_table5620
+ GCC_except_table5626
+ GCC_except_table5640
+ GCC_except_table5654
+ GCC_except_table5658
+ GCC_except_table571
+ GCC_except_table579
+ GCC_except_table5802
+ GCC_except_table608
+ GCC_except_table615
+ GCC_except_table6260
+ GCC_except_table6269
+ GCC_except_table627
+ GCC_except_table6270
+ GCC_except_table628
+ GCC_except_table6280
+ GCC_except_table6322
+ GCC_except_table6325
+ GCC_except_table6326
+ GCC_except_table6327
+ GCC_except_table6328
+ GCC_except_table633
+ GCC_except_table648
+ GCC_except_table6493
+ GCC_except_table6494
+ GCC_except_table6495
+ GCC_except_table6496
+ GCC_except_table6498
+ GCC_except_table6499
+ GCC_except_table6500
+ GCC_except_table6502
+ GCC_except_table652
+ GCC_except_table6523
+ GCC_except_table6534
+ GCC_except_table6536
+ GCC_except_table6541
+ GCC_except_table6544
+ GCC_except_table6547
+ GCC_except_table6551
+ GCC_except_table6555
+ GCC_except_table659
+ GCC_except_table662
+ GCC_except_table696
+ GCC_except_table706
+ GCC_except_table7106
+ GCC_except_table7107
+ GCC_except_table7126
+ GCC_except_table7136
+ GCC_except_table7139
+ GCC_except_table714
+ GCC_except_table7144
+ GCC_except_table7147
+ GCC_except_table7152
+ GCC_except_table741
+ GCC_except_table7421
+ GCC_except_table7425
+ GCC_except_table745
+ GCC_except_table748
+ GCC_except_table7485
+ GCC_except_table7489
+ GCC_except_table7491
+ GCC_except_table7493
+ GCC_except_table750
+ GCC_except_table756
+ GCC_except_table758
+ GCC_except_table7708
+ GCC_except_table771
+ GCC_except_table7716
+ GCC_except_table7718
+ GCC_except_table7720
+ GCC_except_table7722
+ GCC_except_table7728
+ GCC_except_table7741
+ GCC_except_table775
+ GCC_except_table7759
+ GCC_except_table7765
+ GCC_except_table7779
+ GCC_except_table7783
+ GCC_except_table7790
+ GCC_except_table7796
+ GCC_except_table789
+ GCC_except_table7890
+ GCC_except_table7897
+ GCC_except_table7901
+ GCC_except_table7902
+ GCC_except_table7903
+ GCC_except_table7904
+ GCC_except_table7911
+ GCC_except_table7927
+ GCC_except_table795
+ GCC_except_table7962
+ GCC_except_table7963
+ GCC_except_table7964
+ GCC_except_table798
+ GCC_except_table7984
+ GCC_except_table7996
+ GCC_except_table7999
+ GCC_except_table8004
+ GCC_except_table8006
+ GCC_except_table8020
+ GCC_except_table810
+ GCC_except_table816
+ GCC_except_table817
+ GCC_except_table822
+ GCC_except_table823
+ GCC_except_table8244
+ GCC_except_table8257
+ GCC_except_table8262
+ GCC_except_table8266
+ GCC_except_table8268
+ GCC_except_table8269
+ GCC_except_table8271
+ GCC_except_table8301
+ GCC_except_table8323
+ GCC_except_table8327
+ GCC_except_table8331
+ GCC_except_table8336
+ GCC_except_table8340
+ GCC_except_table8344
+ GCC_except_table8352
+ GCC_except_table8360
+ GCC_except_table8362
+ GCC_except_table8364
+ GCC_except_table8390
+ GCC_except_table8401
+ GCC_except_table8539
+ GCC_except_table8574
+ GCC_except_table858
+ GCC_except_table866
+ GCC_except_table8664
+ GCC_except_table8665
+ GCC_except_table8666
+ GCC_except_table8667
+ GCC_except_table8668
+ GCC_except_table8669
+ GCC_except_table867
+ GCC_except_table8670
+ GCC_except_table8735
+ GCC_except_table8748
+ GCC_except_table8749
+ GCC_except_table8754
+ GCC_except_table8755
+ GCC_except_table8762
+ GCC_except_table8774
+ GCC_except_table8780
+ GCC_except_table8782
+ GCC_except_table8784
+ GCC_except_table8788
+ GCC_except_table8794
+ GCC_except_table8808
+ GCC_except_table8811
+ GCC_except_table8812
+ GCC_except_table8817
+ GCC_except_table8820
+ GCC_except_table8827
+ GCC_except_table8830
+ GCC_except_table8844
+ GCC_except_table8851
+ GCC_except_table8857
+ GCC_except_table8866
+ GCC_except_table8868
+ GCC_except_table8872
+ GCC_except_table8873
+ GCC_except_table8880
+ GCC_except_table8904
+ GCC_except_table8905
+ GCC_except_table8910
+ GCC_except_table8914
+ GCC_except_table8915
+ GCC_except_table8918
+ GCC_except_table8924
+ GCC_except_table8928
+ GCC_except_table8932
+ GCC_except_table8934
+ GCC_except_table8936
+ GCC_except_table8940
+ GCC_except_table895
+ GCC_except_table9059
+ GCC_except_table9096
+ GCC_except_table9154
+ GCC_except_table9157
+ GCC_except_table9164
+ GCC_except_table9170
+ GCC_except_table9177
+ GCC_except_table9178
+ GCC_except_table918
+ GCC_except_table9195
+ GCC_except_table9199
+ GCC_except_table9200
+ GCC_except_table9201
+ GCC_except_table9250
+ GCC_except_table9256
+ GCC_except_table9283
+ GCC_except_table9284
+ GCC_except_table9289
+ GCC_except_table9309
+ GCC_except_table9327
+ GCC_except_table9328
+ GCC_except_table9329
+ GCC_except_table9334
+ GCC_except_table9335
+ GCC_except_table9337
+ GCC_except_table9339
+ GCC_except_table9340
+ GCC_except_table9342
+ GCC_except_table9343
+ GCC_except_table9347
+ GCC_except_table9348
+ GCC_except_table9350
+ GCC_except_table9360
+ GCC_except_table9362
+ GCC_except_table9367
+ GCC_except_table937
+ GCC_except_table9372
+ GCC_except_table9373
+ GCC_except_table9374
+ GCC_except_table9390
+ GCC_except_table9392
+ GCC_except_table9399
+ GCC_except_table9406
+ GCC_except_table9411
+ GCC_except_table9417
+ GCC_except_table9429
+ GCC_except_table9430
+ GCC_except_table9435
+ GCC_except_table9445
+ GCC_except_table9451
+ GCC_except_table9452
+ GCC_except_table9456
+ GCC_except_table9458
+ GCC_except_table9460
+ GCC_except_table9464
+ GCC_except_table9485
+ GCC_except_table9487
+ GCC_except_table9488
+ GCC_except_table9514
+ GCC_except_table961
+ GCC_except_table965
+ GCC_except_table9679
+ GCC_except_table9742
+ GCC_except_table9774
+ GCC_except_table9777
+ GCC_except_table979
+ GCC_except_table984
+ GCC_except_table9944
+ GCC_except_table9982
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
+ _HAPMetricEventBluetoothVersionTypeAsString
+ _HAPMetricEventPowerSourcesBitmaskAsString
+ _HAPMetricEventPowerSourcesEnumAsString
+ _HAPMetricEventThreadFirstRestartConnectivityStateAsString
+ _HAPMetricEventWiFiFirstRestartConnectivityStateAsString
+ _HAPMetricEventWiFiVersionTypeAsString
+ _HAPSessionKeepAliveTransportTypeAsString
+ _HAPStabilityMetricsBootReasonTypeAsString
+ _HAPStabilityMetricsHardwareFaultTypeAsString
+ _NSCocoaErrorDomain
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
+ _OBJC_CLASS_$_HAPAccessoryCHMMetricsLogEvent
+ _OBJC_CLASS_$_HAPAccessoryCHMRecoveryLogEvent
+ _OBJC_CLASS_$_HAPBluetoothMetrics
+ _OBJC_CLASS_$_HAPBootReasonsMetrics
+ _OBJC_CLASS_$_HAPCHMMetrics
+ _OBJC_CLASS_$_HAPConnectionHealthMonitor
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
+ _OBJC_IVAR_$_HAP2AccessoryAddressLists._cachedPrimary
+ _OBJC_IVAR_$_HAP2AccessoryAddressLists._cachedSecondary
+ _OBJC_IVAR_$_HAP2AccessoryAddressResolverPipeline._cancelled
+ _OBJC_IVAR_$_HAP2AccessoryAddressResolverPipeline._errorHandler
+ _OBJC_IVAR_$_HAP2AccessoryAddressResolverPipeline._gai
+ _OBJC_IVAR_$_HAP2AccessoryAddressResolverPipeline._queue
+ _OBJC_IVAR_$_HAP2AccessoryAddressResolverPipeline._resolvedHostname
+ _OBJC_IVAR_$_HAP2AccessoryAddressResolverPipeline._resolvedPort
+ _OBJC_IVAR_$_HAP2AccessoryAddressResolverPipeline._retainedContext
+ _OBJC_IVAR_$_HAP2AccessoryAddressResolverPipeline._serviceRef
+ _OBJC_IVAR_$_HAP2AccessoryAddressResolverPipeline._updateHandler
+ _OBJC_IVAR_$_HAP2AccessoryAddressResolverPipeline._workingSet
+ _OBJC_IVAR_$_HAP2AccessoryAddressResolverPipeline._workingSetCounts
+ _OBJC_IVAR_$_HAP2AccessoryDNSResolver._addresses
+ _OBJC_IVAR_$_HAP2AccessoryDNSResolver._becameEmptyAt
+ _OBJC_IVAR_$_HAP2AccessoryDNSResolver._cacheSubscriber
+ _OBJC_IVAR_$_HAP2AccessoryDNSResolver._cachedPrimaryIP
+ _OBJC_IVAR_$_HAP2AccessoryDNSResolver._cachedSecondaryIP
+ _OBJC_IVAR_$_HAP2AccessoryDNSResolver._delegates
+ _OBJC_IVAR_$_HAP2AccessoryDNSResolver._deviceID
+ _OBJC_IVAR_$_HAP2AccessoryDNSResolver._immediateRetrySpent
+ _OBJC_IVAR_$_HAP2AccessoryDNSResolver._managerQueue
+ _OBJC_IVAR_$_HAP2AccessoryDNSResolver._pipelineCancel
+ _OBJC_IVAR_$_HAP2AccessoryDNSResolver._pipelineFactory
+ _OBJC_IVAR_$_HAP2AccessoryDNSResolver._pipelineStarted
+ _OBJC_IVAR_$_HAP2AccessoryDNSResolver._pipelineTornDown
+ _OBJC_IVAR_$_HAP2AccessoryDNSResolver._propertyLock
+ _OBJC_IVAR_$_HAP2AccessoryDNSResolver._serviceName
+ _OBJC_IVAR_$_HAP2AccessoryDeviceIPAddress._transportType
+ _OBJC_IVAR_$_HAP2AccessoryServer._consecutiveProbeFailures
+ _OBJC_IVAR_$_HAP2AccessoryServer._dnsResolver
+ _OBJC_IVAR_$_HAP2AccessoryServer._hasSeededSinceResolverAttach
+ _OBJC_IVAR_$_HAP2AccessoryServer._hasThreadAdvertisement
+ _OBJC_IVAR_$_HAP2AccessoryServer._hasWiFiAdvertisement
+ _OBJC_IVAR_$_HAP2AccessoryServer._keepAliveListener
+ _OBJC_IVAR_$_HAP2AccessoryServer._lastObservedHasAdvertisement
+ _OBJC_IVAR_$_HAP2AccessoryServerBrowser._auditScheduler
+ _OBJC_IVAR_$_HAP2AccessoryServerBrowser._existingPTRs
+ _OBJC_IVAR_$_HAP2AccessoryServerBrowser._ipCache
+ _OBJC_IVAR_$_HAP2AccessoryServerBrowser._isInitialCacheRestored
+ _OBJC_IVAR_$_HAP2AccessoryServerBrowser._pendingRevalidationPTRs
+ _OBJC_IVAR_$_HAP2AccessoryServerBrowser._resolverRegistry
+ _OBJC_IVAR_$_HAP2AccessoryServerBrowser._revalidationTimer
+ _OBJC_IVAR_$_HAP2AccessoryServerControllerOperation._coapMessageID
+ _OBJC_IVAR_$_HAP2AccessoryServerIPCacheData._cachedPrimaryData
+ _OBJC_IVAR_$_HAP2AccessoryServerIPCacheData._cachedSecondaryData
+ _OBJC_IVAR_$_HAP2AccessoryServerIPCacheData._configurationInfo
+ _OBJC_IVAR_$_HAP2AccessoryServerIPCacheData._deviceID
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportBase._supportsKeepAlive
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportBase._supportsThreadTransport
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportBase._supportsWiFiTransport
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._activeMessageID
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._failoverTimer
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._hasJustCompletedInitialResolve
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._hasPublishedAdvertisementState
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._hasRegisteredEndpoint
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._helloRetryCount
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._helloRetryTimer
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._inFlightRacingLogEvent
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._initialCacheGracePeriodTimer
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._initialConnectionAttemptStartedAt
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._initialResolveCompleted
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._lastCompletedMessageID
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._lastMessageID
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._lastPublishedHasThreadAdvertisement
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._lastPublishedHasWiFiAdvertisement
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._pendingEndpointRegistration
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._pendingIPRefresh
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._primaryEffectiveListIsCacheOnly
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._primaryIPsTriedThisSession
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._primaryOpenInFlight
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._resolveTimeoutTimer
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._resolverCancelBlock
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._resolverRestartTimer
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._secondaryAddressList
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._secondaryCoAPClient
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._secondaryIPsTriedThisSession
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._secondaryOpenInFlight
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._securedClient
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._triedIPsLock
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._tryingInitialCacheOnly
+ _OBJC_IVAR_$_HAP2BrowserResolverRegistry._browser
+ _OBJC_IVAR_$_HAP2BrowserResolverRegistry._managerQueue
+ _OBJC_IVAR_$_HAP2BrowserResolverRegistry._name
+ _OBJC_IVAR_$_HAP2BrowserResolverRegistry._pipelineFactory
+ _OBJC_IVAR_$_HAP2BrowserResolverRegistry._propertyLock
+ _OBJC_IVAR_$_HAP2BrowserResolverRegistry._resolversByDeviceID
+ _OBJC_IVAR_$_HAP2CoAPClient._pendingProbeCompletion
+ _OBJC_IVAR_$_HAP2CoAPClient._pendingProbeMessageID
+ _OBJC_IVAR_$_HAP2SessionKeepAliveConfigurationEntry._maximumInterval
+ _OBJC_IVAR_$_HAP2SessionKeepAliveConfigurationEntry._minimumInterval
+ _OBJC_IVAR_$_HAP2SessionKeepAliveConfigurationEntry._transportType
+ _OBJC_IVAR_$_HAP2SessionKeepAliveListener._dateProvider
+ _OBJC_IVAR_$_HAP2SessionKeepAliveListener._delegateLock
+ _OBJC_IVAR_$_HAP2SessionKeepAliveListener._delegates
+ _OBJC_IVAR_$_HAP2SessionKeepAliveListener._isRunning
+ _OBJC_IVAR_$_HAP2SessionKeepAliveListener._missCheckTimer
+ _OBJC_IVAR_$_HAP2SessionKeepAliveListener._timerProvider
+ _OBJC_IVAR_$_HAP2SessionKeepAliveListener._transportStates
+ _OBJC_IVAR_$_HAP2SessionKeepAliveListener._workQueue
+ _OBJC_IVAR_$_HAP2SessionKeepAliveTransportState._hasMissedHeartbeat
+ _OBJC_IVAR_$_HAP2SessionKeepAliveTransportState._lastHeartbeatTime
+ _OBJC_IVAR_$_HAP2SessionKeepAliveTransportState._maximumInterval
+ _OBJC_IVAR_$_HAP2SessionKeepAliveTransportState._transportType
+ _OBJC_IVAR_$_HAPAccessoryServer._hasThreadAdvertisement
+ _OBJC_IVAR_$_HAPAccessoryServer._hasWiFiAdvertisement
+ _OBJC_IVAR_$_HAPAccessoryServer._lastPairSetupWasSpake2
+ _OBJC_IVAR_$_HAPBluetoothMetrics._bluetoothVersion
+ _OBJC_IVAR_$_HAPBluetoothMetrics._connectionCount
+ _OBJC_IVAR_$_HAPBluetoothMetrics._connectionErrorCount
+ _OBJC_IVAR_$_HAPBluetoothMetrics._connectionStatus
+ _OBJC_IVAR_$_HAPBluetoothMetrics._disconnectionCount
+ _OBJC_IVAR_$_HAPBluetoothMetrics._disconnectionErrorCount
+ _OBJC_IVAR_$_HAPBluetoothMetrics._hwExceptionCount
+ _OBJC_IVAR_$_HAPBluetoothMetrics._overrunCount
+ _OBJC_IVAR_$_HAPBluetoothMetrics._packetRxCount
+ _OBJC_IVAR_$_HAPBluetoothMetrics._packetRxErrorCount
+ _OBJC_IVAR_$_HAPBluetoothMetrics._packetTxCount
+ _OBJC_IVAR_$_HAPBluetoothMetrics._packetTxErrorCount
+ _OBJC_IVAR_$_HAPBluetoothMetrics._rssi
+ _OBJC_IVAR_$_HAPBluetoothMetrics._txPowerLevel
+ _OBJC_IVAR_$_HAPBootReasonsMetrics._brownOutResetBootCount
+ _OBJC_IVAR_$_HAPBootReasonsMetrics._connectivityMonitorBootCount
+ _OBJC_IVAR_$_HAPBootReasonsMetrics._hardwareFaultBootCount
+ _OBJC_IVAR_$_HAPBootReasonsMetrics._hardwareWatchdogResetBootCount
+ _OBJC_IVAR_$_HAPBootReasonsMetrics._heapOverflowBootCount
+ _OBJC_IVAR_$_HAPBootReasonsMetrics._powerOnBootCount
+ _OBJC_IVAR_$_HAPBootReasonsMetrics._softwareExceptionBootCount
+ _OBJC_IVAR_$_HAPBootReasonsMetrics._softwareResetBootCount
+ _OBJC_IVAR_$_HAPBootReasonsMetrics._softwareUpdateCompletedBootCount
+ _OBJC_IVAR_$_HAPBootReasonsMetrics._softwareWatchdogResetBootCount
+ _OBJC_IVAR_$_HAPBootReasonsMetrics._stackOverflowBootCount
+ _OBJC_IVAR_$_HAPBootReasonsMetrics._temperatureLimitBootCount
+ _OBJC_IVAR_$_HAPBootReasonsMetrics._unspecifiedBootCount
+ _OBJC_IVAR_$_HAPCHMMetrics._chmAccessoryRebootCompleted
+ _OBJC_IVAR_$_HAPCHMMetrics._chmAccessoryRebootDurationToRecovery
+ _OBJC_IVAR_$_HAPCHMMetrics._hapSessionLossCount
+ _OBJC_IVAR_$_HAPCHMMetrics._threadFirstRestartCompleted
+ _OBJC_IVAR_$_HAPCHMMetrics._threadFirstRestartConnectivityState
+ _OBJC_IVAR_$_HAPCHMMetrics._threadFirstRestartRecoveryTime
+ _OBJC_IVAR_$_HAPCHMMetrics._threadRecoveryAttemptCount
+ _OBJC_IVAR_$_HAPCHMMetrics._threadRestartCount
+ _OBJC_IVAR_$_HAPCHMMetrics._threadTransportLossCount
+ _OBJC_IVAR_$_HAPCHMMetrics._wifiFirstRestartCompleted
+ _OBJC_IVAR_$_HAPCHMMetrics._wifiFirstRestartConnectivityState
+ _OBJC_IVAR_$_HAPCHMMetrics._wifiFirstRestartRecoveryTime
+ _OBJC_IVAR_$_HAPCHMMetrics._wifiRecoveryAttemptCount
+ _OBJC_IVAR_$_HAPCHMMetrics._wifiRestartCount
+ _OBJC_IVAR_$_HAPCHMMetrics._wifiTransportLossCount
+ _OBJC_IVAR_$_HAPCharacteristicResponseTuple._coapMessageID
+ _OBJC_IVAR_$_HAPConnectionHealthMonitor._deviceRebootDelay
+ _OBJC_IVAR_$_HAPConnectionHealthMonitor._deviceRebootEnable
+ _OBJC_IVAR_$_HAPConnectionHealthMonitor._recoveryStaggerDelay
+ _OBJC_IVAR_$_HAPConnectionHealthMonitor._threadPingTestCount
+ _OBJC_IVAR_$_HAPConnectionHealthMonitor._threadPingTestInterval
+ _OBJC_IVAR_$_HAPConnectionHealthMonitor._threadRecoveryConfiguration
+ _OBJC_IVAR_$_HAPConnectionHealthMonitor._threadRestartMinInterval
+ _OBJC_IVAR_$_HAPConnectionHealthMonitor._wiFiPingTestCount
+ _OBJC_IVAR_$_HAPConnectionHealthMonitor._wiFiPingTestInterval
+ _OBJC_IVAR_$_HAPConnectionHealthMonitor._wiFiRecoveryConfiguration
+ _OBJC_IVAR_$_HAPConnectionHealthMonitor._wiFiRestartMinInterval
+ _OBJC_IVAR_$_HAPErrorCountersMetrics._entries
+ _OBJC_IVAR_$_HAPErrorCountersMetricsEntry._count
+ _OBJC_IVAR_$_HAPErrorCountersMetricsEntry._errorID
+ _OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._abandonedRequestCount
+ _OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._audioOnlyFailureCount
+ _OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._authenticationErrorCount
+ _OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._fragmentFailureCount
+ _OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._fragmentRetriedCount
+ _OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._fragmentSuccessCount
+ _OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._latencyCount1000ms
+ _OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._latencyCount2000ms
+ _OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._latencyCount250ms
+ _OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._latencyCount3750ms
+ _OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._latencyCount500ms
+ _OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._latencyCountOver3750ms
+ _OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._localErrorCount
+ _OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._networkErrorCount
+ _OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._partialSuccessCount
+ _OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._playlistFailureCount
+ _OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._serverReturnedErrorCount
+ _OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._sessionFailureCount
+ _OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._sessionSuccessCount
+ _OBJC_IVAR_$_HAPHKSV3UploadLatencyMetrics._uploadWithoutResidentResponseCount
+ _OBJC_IVAR_$_HAPMetricEventBluetoothVersionTypeWrapper._value
+ _OBJC_IVAR_$_HAPMetricEventPowerSourcesBitmaskWrapper._value
+ _OBJC_IVAR_$_HAPMetricEventPowerSourcesEnumWrapper._value
+ _OBJC_IVAR_$_HAPMetricEventThreadFirstRestartConnectivityStateWrapper._value
+ _OBJC_IVAR_$_HAPMetricEventWiFiFirstRestartConnectivityStateWrapper._value
+ _OBJC_IVAR_$_HAPMetricEventWiFiVersionTypeWrapper._value
+ _OBJC_IVAR_$_HAPPowerMetrics._batteryPercentage
+ _OBJC_IVAR_$_HAPPowerMetrics._currentPowerSource
+ _OBJC_IVAR_$_HAPPowerMetrics._durationOnBatteryPower
+ _OBJC_IVAR_$_HAPPowerMetrics._durationRemainingOnBatteryPower
+ _OBJC_IVAR_$_HAPPowerMetrics._supportedPowerSources
+ _OBJC_IVAR_$_HAPSaturationMetrics._averageCPUUtilization
+ _OBJC_IVAR_$_HAPSaturationMetrics._averageSystemMemoryUtilization
+ _OBJC_IVAR_$_HAPSaturationMetrics._heapHighwaterCount
+ _OBJC_IVAR_$_HAPSaturationMetrics._heapOverflowCount
+ _OBJC_IVAR_$_HAPSaturationMetrics._lastHeapHighwaterTaskName
+ _OBJC_IVAR_$_HAPSaturationMetrics._lastHeapOverflowTaskName
+ _OBJC_IVAR_$_HAPSaturationMetrics._lastProcessCriticalMemoryName
+ _OBJC_IVAR_$_HAPSaturationMetrics._lastStackHighwaterTaskName
+ _OBJC_IVAR_$_HAPSaturationMetrics._lastStackOverflowTaskName
+ _OBJC_IVAR_$_HAPSaturationMetrics._loadAverage
+ _OBJC_IVAR_$_HAPSaturationMetrics._maxTaskReadyQueueSize
+ _OBJC_IVAR_$_HAPSaturationMetrics._nonVolatileMemoryReadCount
+ _OBJC_IVAR_$_HAPSaturationMetrics._nonVolatileMemoryReadErrorCount
+ _OBJC_IVAR_$_HAPSaturationMetrics._nonVolatileMemoryUtilization
+ _OBJC_IVAR_$_HAPSaturationMetrics._nonVolatileMemoryWriteCount
+ _OBJC_IVAR_$_HAPSaturationMetrics._nonVolatileMemoryWriteErrorCount
+ _OBJC_IVAR_$_HAPSaturationMetrics._peakCPUUtilization
+ _OBJC_IVAR_$_HAPSaturationMetrics._peakSystemMemoryUtilization
+ _OBJC_IVAR_$_HAPSaturationMetrics._processCriticalMemoryCount
+ _OBJC_IVAR_$_HAPSaturationMetrics._stackHighwaterCount
+ _OBJC_IVAR_$_HAPSaturationMetrics._stackOverflowCount
+ _OBJC_IVAR_$_HAPSaturationMetrics._systemMemoryPressureCount
+ _OBJC_IVAR_$_HAPSaturationMetrics._taskDeadlineMissCount
+ _OBJC_IVAR_$_HAPSaturationMetrics._totalTasksScheduledCount
+ _OBJC_IVAR_$_HAPSecuritySession._foreignPairVerifySession
+ _OBJC_IVAR_$_HAPSessionKeepAliveTransportTypeWrapper._value
+ _OBJC_IVAR_$_HAPStabilityMetrics._activeHardwareFaults
+ _OBJC_IVAR_$_HAPStabilityMetrics._expectedBootCount
+ _OBJC_IVAR_$_HAPStabilityMetrics._lastBootReason
+ _OBJC_IVAR_$_HAPStabilityMetrics._systemBootCount
+ _OBJC_IVAR_$_HAPStabilityMetrics._systemCrashCount
+ _OBJC_IVAR_$_HAPStabilityMetrics._systemHangCount
+ _OBJC_IVAR_$_HAPStabilityMetrics._systemUptime
+ _OBJC_IVAR_$_HAPStabilityMetricsBootReasonTypeWrapper._value
+ _OBJC_IVAR_$_HAPStabilityMetricsHardwareFaultTypeWrapper._value
+ _OBJC_IVAR_$_HAPTLVPreferredWiFiEntry._PSK
+ _OBJC_IVAR_$_HAPTLVPreferredWiFiEntry._SSID
+ _OBJC_IVAR_$_HAPTLVPreferredWiFiEntry._securityMode
+ _OBJC_IVAR_$_HAPTLVPreferredWiFiList._preferredWiFiList
+ _OBJC_IVAR_$_HAPTLVSelectedSessionKeepAliveConfigurationEntry._maximumInterval
+ _OBJC_IVAR_$_HAPTLVSelectedSessionKeepAliveConfigurationEntry._minimumInterval
+ _OBJC_IVAR_$_HAPTLVSelectedSessionKeepAliveConfigurationEntry._transportType
+ _OBJC_IVAR_$_HAPTLVSelectedSessionKeepAliveConfigurationList._entries
+ _OBJC_IVAR_$_HAPTLVSupportedSessionKeepAliveConfigurationEntry._maximumInterval
+ _OBJC_IVAR_$_HAPTLVSupportedSessionKeepAliveConfigurationEntry._minimumInterval
+ _OBJC_IVAR_$_HAPTLVSupportedSessionKeepAliveConfigurationEntry._minimumRange
+ _OBJC_IVAR_$_HAPTLVSupportedSessionKeepAliveConfigurationEntry._transportType
+ _OBJC_IVAR_$_HAPTLVSupportedSessionKeepAliveConfigurationList._entries
+ _OBJC_IVAR_$_HAPThermalMetrics._averageDeviceTemperature
+ _OBJC_IVAR_$_HAPThermalMetrics._maximumDeviceTemperature
+ _OBJC_IVAR_$_HAPThermalMetrics._minimumDeviceTemperature
+ _OBJC_IVAR_$_HAPThermalMetrics._temperatureLimitViolationCount
+ _OBJC_IVAR_$_HAPThermalMetrics._temperatureLimitViolationDuration
+ _OBJC_IVAR_$_HAPWiFiMetrics._beaconLostCount
+ _OBJC_IVAR_$_HAPWiFiMetrics._beaconRxCount
+ _OBJC_IVAR_$_HAPWiFiMetrics._beaconRxInterval
+ _OBJC_IVAR_$_HAPWiFiMetrics._bssid
+ _OBJC_IVAR_$_HAPWiFiMetrics._channelNumber
+ _OBJC_IVAR_$_HAPWiFiMetrics._connectionStatus
+ _OBJC_IVAR_$_HAPWiFiMetrics._disconnectionCount
+ _OBJC_IVAR_$_HAPWiFiMetrics._disconnectionDuration
+ _OBJC_IVAR_$_HAPWiFiMetrics._gatewayIPv4Address
+ _OBJC_IVAR_$_HAPWiFiMetrics._gatewayIPv6Address
+ _OBJC_IVAR_$_HAPWiFiMetrics._gatewayMacAddress
+ _OBJC_IVAR_$_HAPWiFiMetrics._hwExceptionCount
+ _OBJC_IVAR_$_HAPWiFiMetrics._ipAddressList
+ _OBJC_IVAR_$_HAPWiFiMetrics._packetMulticastRxCount
+ _OBJC_IVAR_$_HAPWiFiMetrics._packetMulticastRxErrorCount
+ _OBJC_IVAR_$_HAPWiFiMetrics._packetMulticastTxCount
+ _OBJC_IVAR_$_HAPWiFiMetrics._packetMulticastTxErrorCount
+ _OBJC_IVAR_$_HAPWiFiMetrics._packetUnicastRxCount
+ _OBJC_IVAR_$_HAPWiFiMetrics._packetUnicastRxErrorCount
+ _OBJC_IVAR_$_HAPWiFiMetrics._packetUnicastTxCount
+ _OBJC_IVAR_$_HAPWiFiMetrics._packetUnicastTxErrorCount
+ _OBJC_IVAR_$_HAPWiFiMetrics._rssi
+ _OBJC_IVAR_$_HAPWiFiMetrics._rxPacketCount
+ _OBJC_IVAR_$_HAPWiFiMetrics._rxPacketErrorCount
+ _OBJC_IVAR_$_HAPWiFiMetrics._subnetMask
+ _OBJC_IVAR_$_HAPWiFiMetrics._txPacketCount
+ _OBJC_IVAR_$_HAPWiFiMetrics._txPacketErrorCount
+ _OBJC_IVAR_$_HAPWiFiMetrics._wifiRestartCount
+ _OBJC_IVAR_$_HAPWiFiMetrics._wifiVersion
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
+ _OBJC_METACLASS_$_HAPAccessoryCHMMetricsLogEvent
+ _OBJC_METACLASS_$_HAPAccessoryCHMRecoveryLogEvent
+ _OBJC_METACLASS_$_HAPBluetoothMetrics
+ _OBJC_METACLASS_$_HAPBootReasonsMetrics
+ _OBJC_METACLASS_$_HAPCHMMetrics
+ _OBJC_METACLASS_$_HAPConnectionHealthMonitor
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
+ __OBJC_$_CLASS_METHODS_HAPBluetoothMetrics
+ __OBJC_$_CLASS_METHODS_HAPBootReasonsMetrics
+ __OBJC_$_CLASS_METHODS_HAPCHMMetrics
+ __OBJC_$_CLASS_METHODS_HAPConnectionHealthMonitor
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
+ __OBJC_$_INSTANCE_METHODS_HAPBluetoothMetrics
+ __OBJC_$_INSTANCE_METHODS_HAPBootReasonsMetrics
+ __OBJC_$_INSTANCE_METHODS_HAPCHMMetrics
+ __OBJC_$_INSTANCE_METHODS_HAPConnectionHealthMonitor
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
+ __OBJC_$_INSTANCE_VARIABLES_HAP2AccessoryAddressResolverPipeline
+ __OBJC_$_INSTANCE_VARIABLES_HAP2AccessoryDNSResolver
+ __OBJC_$_INSTANCE_VARIABLES_HAP2AccessoryServerIPCacheData
+ __OBJC_$_INSTANCE_VARIABLES_HAP2BrowserResolverRegistry
+ __OBJC_$_INSTANCE_VARIABLES_HAP2SessionKeepAliveConfigurationEntry
+ __OBJC_$_INSTANCE_VARIABLES_HAP2SessionKeepAliveListener
+ __OBJC_$_INSTANCE_VARIABLES_HAP2SessionKeepAliveTransportState
+ __OBJC_$_INSTANCE_VARIABLES_HAPBluetoothMetrics
+ __OBJC_$_INSTANCE_VARIABLES_HAPBootReasonsMetrics
+ __OBJC_$_INSTANCE_VARIABLES_HAPCHMMetrics
+ __OBJC_$_INSTANCE_VARIABLES_HAPConnectionHealthMonitor
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
+ __OBJC_$_PROP_LIST_HAPBluetoothMetrics
+ __OBJC_$_PROP_LIST_HAPBootReasonsMetrics
+ __OBJC_$_PROP_LIST_HAPCHMMetrics
+ __OBJC_$_PROP_LIST_HAPConnectionHealthMonitor
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
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HAP2AccessoryServerSecureTransportDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HAP2AccessoryServerTransportDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HAP2AccessoryAddressResolverPipelineFactory
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HAP2AccessoryDNSResolver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HAP2AccessoryDNSResolverCacheSubscriber
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HAP2AccessoryDNSResolverDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HAP2AccessoryDNSResolverPrivate
+ __OBJC_$_PROTOCOL_REFS_HAP2AccessoryAddressResolverPipelineFactory
+ __OBJC_$_PROTOCOL_REFS_HAP2AccessoryDNSResolver
+ __OBJC_$_PROTOCOL_REFS_HAP2AccessoryDNSResolverCacheSubscriber
+ __OBJC_$_PROTOCOL_REFS_HAP2AccessoryDNSResolverDelegate
+ __OBJC_$_PROTOCOL_REFS_HAP2AccessoryDNSResolverPrivate
+ __OBJC_CLASS_PROTOCOLS_$_HAP2AccessoryDNSResolver
+ __OBJC_CLASS_PROTOCOLS_$_HAP2AccessoryServer(Test|Paired|PairedInternal|Unpaired)
+ __OBJC_CLASS_PROTOCOLS_$_HAP2DefaultAccessoryAddressResolverPipelineFactory
+ __OBJC_CLASS_PROTOCOLS_$_HAP2SessionKeepAliveListener
+ __OBJC_CLASS_PROTOCOLS_$_HAPBluetoothMetrics
+ __OBJC_CLASS_PROTOCOLS_$_HAPBootReasonsMetrics
+ __OBJC_CLASS_PROTOCOLS_$_HAPCHMMetrics
+ __OBJC_CLASS_PROTOCOLS_$_HAPConnectionHealthMonitor
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
+ __OBJC_CLASS_RO_$_HAP2AccessoryAddressResolverPipeline
+ __OBJC_CLASS_RO_$_HAP2AccessoryDNSResolver
+ __OBJC_CLASS_RO_$_HAP2AccessoryServerIPCacheData
+ __OBJC_CLASS_RO_$_HAP2BrowserResolverRegistry
+ __OBJC_CLASS_RO_$_HAP2DefaultAccessoryAddressResolverPipelineFactory
+ __OBJC_CLASS_RO_$_HAP2SessionKeepAliveConfiguration
+ __OBJC_CLASS_RO_$_HAP2SessionKeepAliveConfigurationEntry
+ __OBJC_CLASS_RO_$_HAP2SessionKeepAliveListener
+ __OBJC_CLASS_RO_$_HAP2SessionKeepAliveTransportState
+ __OBJC_CLASS_RO_$_HAPBluetoothMetrics
+ __OBJC_CLASS_RO_$_HAPBootReasonsMetrics
+ __OBJC_CLASS_RO_$_HAPCHMMetrics
+ __OBJC_CLASS_RO_$_HAPConnectionHealthMonitor
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
+ __OBJC_METACLASS_RO_$_HAP2AccessoryAddressResolverPipeline
+ __OBJC_METACLASS_RO_$_HAP2AccessoryDNSResolver
+ __OBJC_METACLASS_RO_$_HAP2AccessoryServerIPCacheData
+ __OBJC_METACLASS_RO_$_HAP2BrowserResolverRegistry
+ __OBJC_METACLASS_RO_$_HAP2DefaultAccessoryAddressResolverPipelineFactory
+ __OBJC_METACLASS_RO_$_HAP2SessionKeepAliveConfiguration
+ __OBJC_METACLASS_RO_$_HAP2SessionKeepAliveConfigurationEntry
+ __OBJC_METACLASS_RO_$_HAP2SessionKeepAliveListener
+ __OBJC_METACLASS_RO_$_HAP2SessionKeepAliveTransportState
+ __OBJC_METACLASS_RO_$_HAPBluetoothMetrics
+ __OBJC_METACLASS_RO_$_HAPBootReasonsMetrics
+ __OBJC_METACLASS_RO_$_HAPCHMMetrics
+ __OBJC_METACLASS_RO_$_HAPConnectionHealthMonitor
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
+ __OBJC_PROTOCOL_REFERENCE_$_HAP2AccessoryDNSResolverPrivate
+ __PROPERTIES_HAP2CoAPRequestRacingLogEvent
+ __PROPERTIES_HAPAccessoryCHMMetricsLogEvent
+ __PROPERTIES_HAPAccessoryCHMRecoveryLogEvent
+ __PROTOCOLS_HAPAccessoryCHMMetricsLogEvent
+ __PROTOCOLS_HAPAccessoryCHMRecoveryLogEvent
+ __ZL11_cacheValid
+ __ZL22_cachedMeshLocalPrefix
+ __ZL22_sharedClientOnceToken
+ __ZL24_lastInstalledNCPHandler
+ __ZL30_lastInstalledPreferredHandler
+ __ZNK6CtrXPC5Event7getNameEv
+ __ZnwmSt19__type_descriptor_t
+ ___101-[HAP2AccessoryServerSecureTransportBase transport:pairVerifyDidFailOnIPAddress:transportType:error:]_block_invoke
+ ___107-[HAP2AccessoryServerTransportCoAP _sendRacingRequest:path:method:messageID:primaryClient:secondaryClient:]_block_invoke
+ ___139-[HAP2AccessoryServerTransportCoAP _executeRacingWithRequest:path:method:messageID:primaryClient:secondaryClient:failoverTimeout:rttStats:]_block_invoke
+ ___143-[HAP2DefaultAccessoryAddressResolverPipelineFactory createResolverWithServiceName:serviceType:serviceDomain:queue:updateHandler:errorHandler:]_block_invoke
+ ___145-[HAP2AccessoryServer(PairedInternal) keepAliveListener:didMissHeartbeatOnTransport:expectedInterval:timeSinceLastHeartbeat:allTransportsMissed:]_block_invoke
+ ___145-[HAP2AccessoryServer(PairedInternal) keepAliveListener:didMissHeartbeatOnTransport:expectedInterval:timeSinceLastHeartbeat:allTransportsMissed:]_block_invoke_2
+ ___36-[HAP2SessionKeepAliveListener stop]_block_invoke
+ ___37-[HAP2AccessoryServerBrowser ipCache]_block_invoke
+ ___37-[HAP2SessionKeepAliveListener start]_block_invoke
+ ___39-[HAP2AccessoryDNSResolver serviceName]_block_invoke
+ ___40-[HAP2AccessoryDNSResolver stopPipeline]_block_invoke
+ ___41-[HAP2AccessoryDNSResolver becameEmptyAt]_block_invoke
+ ___41-[HAP2AccessoryDNSResolver startPipeline]_block_invoke
+ ___41-[HAP2AccessoryServerBrowser currentPTRs]_block_invoke
+ ___41-[HAP2AccessoryServerBrowser setIPCache:]_block_invoke
+ ___42-[HAP2CoAPClient sendProbeWithCompletion:]_block_invoke
+ ___42-[HAP2CoAPClient sendProbeWithCompletion:]_block_invoke_2
+ ___42-[HAP2CoAPClient sendProbeWithCompletion:]_block_invoke_3
+ ___43-[HAP2AccessoryDNSResolver attachDelegate:]_block_invoke
+ ___43-[HAP2AccessoryDNSResolver detachDelegate:]_block_invoke
+ ___43-[HAP2AccessoryServer hasWiFiAdvertisement]_block_invoke
+ ___44+[HAP2ThreadNetworkUtil _sharedThreadClient]_block_invoke
+ ___44-[HAP2AccessoryDNSResolver currentAddresses]_block_invoke
+ ___45+[HAP2AccessoryServerIPCacheData logCategory]_block_invoke
+ ___45-[HAP2AccessoryServer hasThreadAdvertisement]_block_invoke
+ ___46-[HAP2AccessoryAddressResolverPipeline cancel]_block_invoke
+ ___46-[HAP2AccessoryDNSResolver updateServiceName:]_block_invoke
+ ___46-[HAP2AccessoryDNSResolver updateServiceName:]_block_invoke_2
+ ___47-[HAP2AccessoryServer setHasWiFiAdvertisement:]_block_invoke
+ ___48+[HAP2ThreadNetworkUtil setupEventSubscriptions]_block_invoke
+ ___48-[HAP2AccessoryServer _setHasWiFiAdvertisement:]_block_invoke
+ ___49-[HAP2AccessoryDNSResolver _startPipelineOnQueue]_block_invoke
+ ___49-[HAP2AccessoryDNSResolver _startPipelineOnQueue]_block_invoke_2
+ ___49-[HAP2AccessoryDNSResolver _startPipelineOnQueue]_block_invoke_3
+ ___49-[HAP2AccessoryServer setHasThreadAdvertisement:]_block_invoke
+ ___49-[HAP2CoAPClient getLocalEndpointWithCompletion:]_block_invoke
+ ___49-[HAP2CoAPClient getLocalEndpointWithCompletion:]_block_invoke_2
+ ___49-[HAP2CoAPClient getLocalEndpointWithCompletion:]_block_invoke_3
+ ___49-[HAP2CoAPClient getLocalEndpointWithCompletion:]_block_invoke_4
+ ___49-[HAP2CoAPClient getLocalEndpointWithCompletion:]_block_invoke_5
+ ___49-[HAP2CoAPClient getRTTStatisticsWithCompletion:]_block_invoke
+ ___49-[HAP2CoAPClient getRTTStatisticsWithCompletion:]_block_invoke_2
+ ___49-[HAP2CoAPClient getRTTStatisticsWithCompletion:]_block_invoke_3
+ ___50-[HAP2AccessoryDNSResolver _handlePipelineUpdate:]_block_invoke
+ ___50-[HAP2AccessoryDNSResolver _handlePipelineUpdate:]_block_invoke_2
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
+ ___58-[HAP2AccessoryServer(Paired) configureKeepAliveListener:]_block_invoke
+ ___58-[HAP2AccessoryServerBrowser _cancelPTRRevalidationWindow]_block_invoke
+ ___58-[HAP2AccessoryServerCoordinator(Test) _test_deliverLoss:]_block_invoke
+ ___58-[HAP2AccessoryServerTransportCoAP _startResolverIfNeeded]_block_invoke
+ ___58-[HAP2AccessoryServerTransportCoAP _startResolverIfNeeded]_block_invoke_2
+ ___59-[HAP2AccessoryServer(Paired) resolver:didUpdateAddresses:]_block_invoke
+ ___59-[HAP2AccessoryServer(Paired) resolver:didUpdateAddresses:]_block_invoke_2
+ ___59-[HAP2AccessoryServerBrowser initWithCoordinators:storage:]_block_invoke_2
+ ___59-[HAP2AccessoryServerTransportCoAP _executeCacheMissCancel]_block_invoke
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
+ ___68-[HAP2AccessoryServerTransportCoAP _resolverDidUpdateWithAddresses:]_block_invoke_2
+ ___68-[HAP2AccessoryServerTransportCoAP _sendMultiTransportRequest:path:]_block_invoke
+ ___69-[HAP2AccessoryAddressResolverPipeline _startGetaddrinfoForHostname:]_block_invoke
+ ___69-[HAP2AccessoryAddressResolverPipeline _startGetaddrinfoForHostname:]_block_invoke_2
+ ___69-[HAP2AccessoryServerTransportCoAP signalPairVerifySuccessToDelegate]_block_invoke
+ ___69-[HAPAccessoryServerHAP2Adapter dataStreamPeerAddressWithCompletion:]_block_invoke
+ ___70-[HAP2AccessoryServerController secureTransport:didChangeState:error:]_block_invoke_4
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
+ ___75-[HAP2BrowserResolverRegistry _performAuditPassOnQueueWithActiveDeviceIDs:]_block_invoke_2
+ ___76-[HAP2AccessoryServerTransportCoAP _armInitialCacheGracePeriodTimerIfNeeded]_block_invoke
+ ___76-[HAP2AccessoryServerTransportCoAP _armInitialCacheGracePeriodTimerIfNeeded]_block_invoke_2
+ ___76-[HAP2AccessoryServerTransportCoAP _openPrimaryClientForRefreshWithAddress:]_block_invoke
+ ___76-[HAP2AccessoryServerTransportCoAP _openPrimaryClientForRefreshWithAddress:]_block_invoke_2
+ ___78-[HAP2AccessoryServerTransportCoAP _openPrimaryClientIteratingWithCompletion:]_block_invoke
+ ___78-[HAP2AccessoryServerTransportCoAP _openPrimaryClientIteratingWithCompletion:]_block_invoke_2
+ ___78-[HAP2AccessoryServerTransportCoAP _openSecondaryClientForRefreshWithAddress:]_block_invoke
+ ___78-[HAP2AccessoryServerTransportCoAP _openSecondaryClientForRefreshWithAddress:]_block_invoke_2
+ ___78-[HAP2AccessoryServerTransportCoAP _sendRegistrationTLVWithAddressBytes:port:]_block_invoke
+ ___79-[HAP2AccessoryServerBrowser(Test) _test_restoreCachedAccessoryServersIfNeeded]_block_invoke
+ ___79-[HAP2AccessoryServerSecureTransportBase transport:didChangeWiFiAdvertisement:]_block_invoke
+ ___79-[HAP2AccessoryServerTransportCoAP signalPairVerifyFailureToDelegateWithError:]_block_invoke
+ ___80-[HAP2AccessoryServerCoordinator initializePairedAccessoryServerFromCachedInfo:]_block_invoke
+ ___80-[HAP2AccessoryServerCoordinator initializePairedAccessoryServerFromCachedInfo:]_block_invoke_2
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
+ ___87-[HAP2AccessoryServerTransportCoAP checkConnectedIPAddressStaleOnTransport:completion:]_block_invoke
+ ___87-[HAP2CoAPClient sendRequestWithMethod:path:payload:messageID:dscpPriority:completion:]_block_invoke
+ ___87-[HAP2CoAPClient sendRequestWithMethod:path:payload:messageID:dscpPriority:completion:]_block_invoke_2
+ ___88-[HAP2AccessoryServerTransportCoAP advanceEndpointAfterPairVerifyFailureWithCompletion:]_block_invoke
+ ___88-[HAP2AccessoryServerTransportCoAP advanceEndpointAfterPairVerifyFailureWithCompletion:]_block_invoke_2
+ ___89-[HAP2AccessoryDNSResolver _applyCachedIP:transportType:notifySubscriber:seedAgingClock:]_block_invoke
+ ___89-[HAP2AccessoryServerTransportCoAP _createDefaultResolverWithUpdateHandler:errorHandler:]_block_invoke
+ ___89-[HAP2AccessoryServerTransportCoAP _openSecondaryClientIteratingIsThreadOnly:completion:]_block_invoke
+ ___89-[HAP2AccessoryServerTransportCoAP _openSecondaryClientIteratingIsThreadOnly:completion:]_block_invoke_2
+ ___90-[HAP2AccessoryServer(PairedInternal) _closeSessionIfConnectedIPAddressStaleForTransport:]_block_invoke
+ ___90-[HAP2AccessoryServer(PairedInternal) _closeSessionIfConnectedIPAddressStaleForTransport:]_block_invoke_2
+ ___90-[HAP2AccessoryServerBrowser noteBonjourAdvertisementUpdatedForDeviceID:rawDiscoveryInfo:]_block_invoke
+ ___90-[HAP2AccessoryServerTransportCoAP _readLocalEndpointForClient:transport:into:completion:]_block_invoke
+ ___90-[HAP2AccessoryServerTransportCoAP _readLocalEndpointForClient:transport:into:completion:]_block_invoke_2
+ ___92-[HAPAccessoryServerHAP2Adapter deriveEncryptionForDataStreamWithKeySalt:completionHandler:]_block_invoke
+ ___93-[HAP2AccessoryServerSecureTransportBase checkConnectedIPAddressStaleOnTransport:completion:]_block_invoke
+ ___94-[HAP2BrowserResolverRegistry updateCachedAddressesForDeviceID:cachedPrimary:cachedSecondary:]_block_invoke
+ ___97-[HAP2CoAPClient _sendRequestWithMethod:path:payload:activity:messageID:dscpPriority:completion:]_block_invoke
+ ___97-[HAP2CoAPClient _sendRequestWithMethod:path:payload:activity:messageID:dscpPriority:completion:]_block_invoke_2
+ ___99-[HAP2AccessoryServerSecureTransportBase transport:pairVerifyDidCompleteOnIPAddress:transportType:]_block_invoke
+ ___block_descriptor_106_e8_32s40s48s56s64r72r80r88r_e28_v24?0"NSData"8"NSError"16ls32l8r64l8s40l8r72l8r80l8r88l8s48l8s56l8
+ ___block_descriptor_122_e8_32s40s48s56s64s72r80r88r96r104w_e28_v24?0"NSData"8"NSError"16lw104l8r72l8s32l8r80l8r88l8s40l8r96l8s48l8s56l8s64l8
+ ___block_descriptor_123_e8_32s40s48s56s64s72s80r88r96r104r112w_e5_v8?0lw112l8s32l8s40l8s48l8s56l8s64l8r80l8r88l8r96l8r104l8s72l8
+ ___block_descriptor_32_e716_v24?0"HAP2CoAPClient"8^{coap_session_t=CCCIII{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}}^{coap_endpoint_t}^{coap_context_t}^vSCi^{coap_queue_t}Q[8C]Q^{coap_pdu_t}QQQQQ*Q*Q^vI{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}IidddIddddCddI[32{?=SdC}]}16l
+ ___block_descriptor_40_e65_v24?0{shared_ptr<CtrXPC::Event>=^{Event}^{__shared_weak_count}}8l
+ ___block_descriptor_40_e8_32bs_e28_v24?0"NSData"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e49_v28?0B8"HAP2AccessorySessionInfo"12"NSError"20ls32l8
+ ___block_descriptor_40_e8_32s_e31_v28?0"NSData"8S16"NSError"20ls32l8
+ ___block_descriptor_40_e8_32w_e11_v16?0i8i12lw32l8
+ ___block_descriptor_40_e8_32w_e12_v24?0^8Q16lw32l8
+ ___block_descriptor_40_e8_32w_e15_v16?0?<v?q>8lw32l8
+ ___block_descriptor_40_e8_32w_e17_v16?0"NSArray"8lw32l8
+ ___block_descriptor_40_e8_32w_e22_v16?0"NSDictionary"8lw32l8
+ ___block_descriptor_42_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e716_v24?0"HAP2CoAPClient"8^{coap_session_t=CCCIII{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}}^{coap_endpoint_t}^{coap_context_t}^vSCi^{coap_queue_t}Q[8C]Q^{coap_pdu_t}QQQQQ*Q*Q^vI{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}IidddIddddCddI[32{?=SdC}]}16l
+ ___block_descriptor_48_e8_32bs40r_e28_v24?0"NSData"8"NSError"16ls32l8r40l8
+ ___block_descriptor_48_e8_32bs40w_e862_v24?0^{coap_context_t=[6S]^{coap_resource_t}^{coap_resource_t}^{coap_async_state_t}Q^{coap_queue_t}^{coap_endpoint_t}^{coap_session_t}^?^?^?^?^?^?^?^?^?^?^v*Q*QIIIII^v}8^{coap_session_t=CCCIII{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}}^{coap_endpoint_t}^{coap_context_t}^vSCi^{coap_queue_t}Q[8C]Q^{coap_pdu_t}QQQQQ*Q*Q^vI{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}IidddIddddCddI[32{?=SdC}]}16lw40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e862_v24?0^{coap_context_t=[6S]^{coap_resource_t}^{coap_resource_t}^{coap_async_state_t}Q^{coap_queue_t}^{coap_endpoint_t}^{coap_session_t}^?^?^?^?^?^?^?^?^?^?^v*Q*QIIIII^v}8^{coap_session_t=CCCIII{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}}^{coap_endpoint_t}^{coap_context_t}^vSCi^{coap_queue_t}Q[8C]Q^{coap_pdu_t}QQQQQ*Q*Q^vI{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}IidddIddddCddI[32{?=SdC}]}16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e28_v32?0"NSOperation"8Q16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32w_e8_v12?0B8lw32l8
+ ___block_descriptor_49_e8_32bs40w_e17_v16?0"NSError"8lw40l8s32l8
+ ___block_descriptor_49_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_50_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_50_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_50_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_51_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_56_e8_32bs40w48w_e5_v8?0ls32l8w40l8w48l8
+ ___block_descriptor_56_e8_32s40bs48w_e5_v8?0lw48l8s40l8s32l8
+ ___block_descriptor_56_e8_32s40r48r_e5_v8?0lr40l8s32l8r48l8
+ ___block_descriptor_56_e8_32s40s48bs_e862_v24?0^{coap_context_t=[6S]^{coap_resource_t}^{coap_resource_t}^{coap_async_state_t}Q^{coap_queue_t}^{coap_endpoint_t}^{coap_session_t}^?^?^?^?^?^?^?^?^?^?^v*Q*QIIIII^v}8^{coap_session_t=CCCIII{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}}^{coap_endpoint_t}^{coap_context_t}^vSCi^{coap_queue_t}Q[8C]Q^{coap_pdu_t}QQQQQ*Q*Q^vI{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}IidddIddddCddI[32{?=SdC}]}16ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e72_"HAP2AccessoryServerIPCacheData"16?0"HAP2AccessoryServerIPCacheData"8ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e17_v16?0"NSError"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48w_e20_v20?0B8"NSError"12lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s_e72_"HAP2AccessoryServerIPCacheData"16?0"HAP2AccessoryServerIPCacheData"8ls32l8s40l8
+ ___block_descriptor_57_e8_32s40bs48w_e5_v8?0lw48l8s40l8s32l8
+ ___block_descriptor_58_e8_32s40n9_8_8_s0_s8_e5_v8?0l
+ ___block_descriptor_58_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_58_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_59_e8_32s40s48s_e17_v16?0"NSError"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32bs40r48r56r_e5_v8?0ls32l8r40l8r48l8r56l8
+ ___block_descriptor_64_e8_32bs40r48w_e5_v8?0lw48l8s32l8r40l8
+ ___block_descriptor_64_e8_32bs40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_64_e8_32s40s48bs_e31_v28?0"NSData"8S16"NSError"20ls32l8s40l8s48l8
+ ___block_descriptor_65_e8_32s40s48bs56w_e20_v20?0B8"NSError"12ls32l8s48l8w56l8s40l8
+ ___block_descriptor_71_e8_32s40s48s_e716_v24?0"HAP2CoAPClient"8^{coap_session_t=CCCIII{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}}^{coap_endpoint_t}^{coap_context_t}^vSCi^{coap_queue_t}Q[8C]Q^{coap_pdu_t}QQQQQ*Q*Q^vI{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}IidddIddddCddI[32{?=SdC}]}16ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e5_v8?0lr56l8s32l8s40l8s48l8r64l8
+ ___block_descriptor_72_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_74_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_74_e8_32s40s48s56s_e28_v24?0"NSData"8"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_75_e8_32s40s48s56s64w_e22_v16?0"NSDictionary"8lw64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_81_e8_32s40s48r56r64r_e5_v8?0ls32l8s40l8r48l8r56l8r64l8
+ ___block_descriptor_82_e8_32s40s48s56w_e5_v8?0lw56l8s32l8s40l8s48l8
+ ___block_descriptor_83_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_83_e8_32s40s48s56s64s72w_e5_v8?0lw72l8s32l8s40l8s48l8s56l8s64l8
+ ___copy_helper_block_e8_40n9_8_8_s0_s8
+ ___destroy_helper_block_e8_40n7_8_s0_s8
+ ___removeDependencyOnCompletion_block_invoke
+ _associated conformance So27HAP2CoAPAccessoryTransportsVs10SetAlgebraSCSQ
+ _associated conformance So27HAP2CoAPAccessoryTransportsVs10SetAlgebraSCs25ExpressibleByArrayLiteral
+ _associated conformance So27HAP2CoAPAccessoryTransportsVs9OptionSetSCSY
+ _associated conformance So27HAP2CoAPAccessoryTransportsVs9OptionSetSCs0F7Algebra
+ _coapPingHandler
+ _coap_session_send_ping
+ _dispatch_activate
+ _dispatch_assert_queue_not$V2
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
+ _logCategory._hmf_once_t8
+ _logCategory._hmf_once_v9
+ _record_pending_message
+ _symbolic $s7CoreHAP39AccessoryMetricsDictionaryRepresentableP
+ _symbolic SS_So8NSObjectCt
+ _symbolic Si
+ _symbolic So11HMMLogEventC
+ _symbolic So7NSErrorCSg
+ _symbolic _____ 10Foundation4UUIDV
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
+ _symbolic _____ySSSo8NSObjectCG s18_DictionaryStorageC
+ _symbolic _____ySS_So8NSObjectCtG s23_ContiguousArrayStorageC
- -[HAP2AccessoryServer(Paired) mergeWithNewlyDiscoveredPairedAccessoryServer:]
- -[HAP2CoAPClient sendRequestWithMethod:path:payload:dscpPriority:completion:]
- GCC_except_table1083
- GCC_except_table1085
- GCC_except_table1191
- GCC_except_table1196
- GCC_except_table1198
- GCC_except_table1212
- GCC_except_table1224
- GCC_except_table1226
- GCC_except_table1228
- GCC_except_table1230
- GCC_except_table1356
- GCC_except_table1360
- GCC_except_table1362
- GCC_except_table1564
- GCC_except_table1774
- GCC_except_table1776
- GCC_except_table1787
- GCC_except_table1789
- GCC_except_table1795
- GCC_except_table1797
- GCC_except_table1801
- GCC_except_table1807
- GCC_except_table1809
- GCC_except_table1811
- GCC_except_table1813
- GCC_except_table1819
- GCC_except_table1823
- GCC_except_table1833
- GCC_except_table1841
- GCC_except_table1848
- GCC_except_table1852
- GCC_except_table1856
- GCC_except_table1860
- GCC_except_table1898
- GCC_except_table2017
- GCC_except_table2021
- GCC_except_table2022
- GCC_except_table2024
- GCC_except_table2026
- GCC_except_table2038
- GCC_except_table2043
- GCC_except_table2047
- GCC_except_table2050
- GCC_except_table2052
- GCC_except_table2055
- GCC_except_table2072
- GCC_except_table2082
- GCC_except_table2084
- GCC_except_table2086
- GCC_except_table2091
- GCC_except_table2094
- GCC_except_table2096
- GCC_except_table2099
- GCC_except_table2102
- GCC_except_table2106
- GCC_except_table2108
- GCC_except_table2111
- GCC_except_table2114
- GCC_except_table2116
- GCC_except_table2118
- GCC_except_table2122
- GCC_except_table2126
- GCC_except_table2134
- GCC_except_table2145
- GCC_except_table2188
- GCC_except_table2189
- GCC_except_table2190
- GCC_except_table2192
- GCC_except_table2193
- GCC_except_table2194
- GCC_except_table2196
- GCC_except_table2200
- GCC_except_table2201
- GCC_except_table2227
- GCC_except_table2231
- GCC_except_table2235
- GCC_except_table228
- GCC_except_table229
- GCC_except_table235
- GCC_except_table236
- GCC_except_table238
- GCC_except_table2399
- GCC_except_table2406
- GCC_except_table2414
- GCC_except_table2418
- GCC_except_table2421
- GCC_except_table2425
- GCC_except_table2428
- GCC_except_table2434
- GCC_except_table2436
- GCC_except_table2439
- GCC_except_table244
- GCC_except_table2440
- GCC_except_table248
- GCC_except_table252
- GCC_except_table2543
- GCC_except_table2551
- GCC_except_table2552
- GCC_except_table2553
- GCC_except_table2554
- GCC_except_table2555
- GCC_except_table2556
- GCC_except_table2571
- GCC_except_table2585
- GCC_except_table263
- GCC_except_table2665
- GCC_except_table267
- GCC_except_table2677
- GCC_except_table2882
- GCC_except_table2891
- GCC_except_table2908
- GCC_except_table2942
- GCC_except_table2958
- GCC_except_table2960
- GCC_except_table2972
- GCC_except_table2979
- GCC_except_table3001
- GCC_except_table3015
- GCC_except_table3016
- GCC_except_table3020
- GCC_except_table3026
- GCC_except_table3033
- GCC_except_table3036
- GCC_except_table3041
- GCC_except_table3046
- GCC_except_table3051
- GCC_except_table3091
- GCC_except_table3108
- GCC_except_table3111
- GCC_except_table3116
- GCC_except_table3118
- GCC_except_table3134
- GCC_except_table3148
- GCC_except_table3150
- GCC_except_table3154
- GCC_except_table3162
- GCC_except_table3170
- GCC_except_table3234
- GCC_except_table3241
- GCC_except_table3243
- GCC_except_table3244
- GCC_except_table3267
- GCC_except_table3287
- GCC_except_table3515
- GCC_except_table3583
- GCC_except_table3584
- GCC_except_table3588
- GCC_except_table3591
- GCC_except_table3593
- GCC_except_table3594
- GCC_except_table3596
- GCC_except_table3597
- GCC_except_table3599
- GCC_except_table3616
- GCC_except_table3619
- GCC_except_table3631
- GCC_except_table3633
- GCC_except_table3638
- GCC_except_table3642
- GCC_except_table3644
- GCC_except_table3647
- GCC_except_table3650
- GCC_except_table3662
- GCC_except_table3664
- GCC_except_table3668
- GCC_except_table3672
- GCC_except_table3676
- GCC_except_table3703
- GCC_except_table3726
- GCC_except_table3732
- GCC_except_table3736
- GCC_except_table3740
- GCC_except_table3742
- GCC_except_table3745
- GCC_except_table3747
- GCC_except_table3749
- GCC_except_table3756
- GCC_except_table3757
- GCC_except_table3758
- GCC_except_table3764
- GCC_except_table3849
- GCC_except_table3850
- GCC_except_table3851
- GCC_except_table3852
- GCC_except_table3853
- GCC_except_table3854
- GCC_except_table3855
- GCC_except_table3857
- GCC_except_table3858
- GCC_except_table3859
- GCC_except_table3860
- GCC_except_table3861
- GCC_except_table3862
- GCC_except_table3863
- GCC_except_table3902
- GCC_except_table3929
- GCC_except_table4039
- GCC_except_table4046
- GCC_except_table4061
- GCC_except_table4069
- GCC_except_table4080
- GCC_except_table4094
- GCC_except_table4097
- GCC_except_table4102
- GCC_except_table4110
- GCC_except_table4116
- GCC_except_table4118
- GCC_except_table4120
- GCC_except_table4130
- GCC_except_table4155
- GCC_except_table4161
- GCC_except_table4247
- GCC_except_table4250
- GCC_except_table4259
- GCC_except_table4262
- GCC_except_table4265
- GCC_except_table4271
- GCC_except_table4276
- GCC_except_table4289
- GCC_except_table4294
- GCC_except_table4298
- GCC_except_table4300
- GCC_except_table4303
- GCC_except_table4314
- GCC_except_table4322
- GCC_except_table4326
- GCC_except_table4332
- GCC_except_table4333
- GCC_except_table4336
- GCC_except_table4337
- GCC_except_table4355
- GCC_except_table4357
- GCC_except_table4359
- GCC_except_table4360
- GCC_except_table4363
- GCC_except_table4369
- GCC_except_table4372
- GCC_except_table4374
- GCC_except_table4380
- GCC_except_table4382
- GCC_except_table4384
- GCC_except_table4398
- GCC_except_table4420
- GCC_except_table4422
- GCC_except_table4424
- GCC_except_table4430
- GCC_except_table4712
- GCC_except_table4718
- GCC_except_table4735
- GCC_except_table4739
- GCC_except_table4757
- GCC_except_table4763
- GCC_except_table4777
- GCC_except_table4791
- GCC_except_table4913
- GCC_except_table531
- GCC_except_table5371
- GCC_except_table5380
- GCC_except_table5390
- GCC_except_table541
- GCC_except_table5432
- GCC_except_table5435
- GCC_except_table5436
- GCC_except_table5437
- GCC_except_table5438
- GCC_except_table555
- GCC_except_table5588
- GCC_except_table5589
- GCC_except_table5590
- GCC_except_table5591
- GCC_except_table5592
- GCC_except_table5593
- GCC_except_table5599
- GCC_except_table5600
- GCC_except_table5609
- GCC_except_table5612
- GCC_except_table5614
- GCC_except_table5619
- GCC_except_table5622
- GCC_except_table5625
- GCC_except_table5629
- GCC_except_table563
- GCC_except_table5633
- GCC_except_table592
- GCC_except_table599
- GCC_except_table611
- GCC_except_table612
- GCC_except_table614
- GCC_except_table617
- GCC_except_table6182
- GCC_except_table6183
- GCC_except_table620
- GCC_except_table6202
- GCC_except_table6212
- GCC_except_table6215
- GCC_except_table6220
- GCC_except_table6223
- GCC_except_table6228
- GCC_except_table632
- GCC_except_table643
- GCC_except_table6501
- GCC_except_table6546
- GCC_except_table6550
- GCC_except_table6552
- GCC_except_table6554
- GCC_except_table6779
- GCC_except_table6786
- GCC_except_table6790
- GCC_except_table6791
- GCC_except_table6792
- GCC_except_table6793
- GCC_except_table6799
- GCC_except_table680
- GCC_except_table6815
- GCC_except_table6850
- GCC_except_table6851
- GCC_except_table6852
- GCC_except_table6872
- GCC_except_table6884
- GCC_except_table6887
- GCC_except_table6892
- GCC_except_table6894
- GCC_except_table690
- GCC_except_table6908
- GCC_except_table698
- GCC_except_table7132
- GCC_except_table7145
- GCC_except_table7150
- GCC_except_table7153
- GCC_except_table7154
- GCC_except_table7156
- GCC_except_table7157
- GCC_except_table7159
- GCC_except_table7189
- GCC_except_table7211
- GCC_except_table7215
- GCC_except_table7219
- GCC_except_table7224
- GCC_except_table7228
- GCC_except_table7232
- GCC_except_table7236
- GCC_except_table7240
- GCC_except_table7248
- GCC_except_table725
- GCC_except_table7250
- GCC_except_table7252
- GCC_except_table7278
- GCC_except_table7289
- GCC_except_table729
- GCC_except_table732
- GCC_except_table734
- GCC_except_table740
- GCC_except_table742
- GCC_except_table7427
- GCC_except_table7462
- GCC_except_table755
- GCC_except_table7552
- GCC_except_table7553
- GCC_except_table7554
- GCC_except_table7555
- GCC_except_table7556
- GCC_except_table7557
- GCC_except_table7558
- GCC_except_table759
- GCC_except_table7622
- GCC_except_table7629
- GCC_except_table763
- GCC_except_table7630
- GCC_except_table7646
- GCC_except_table7647
- GCC_except_table7648
- GCC_except_table7658
- GCC_except_table7664
- GCC_except_table7678
- GCC_except_table7681
- GCC_except_table7682
- GCC_except_table7687
- GCC_except_table7690
- GCC_except_table7697
- GCC_except_table7700
- GCC_except_table7714
- GCC_except_table7721
- GCC_except_table7727
- GCC_except_table773
- GCC_except_table7736
- GCC_except_table7738
- GCC_except_table774
- GCC_except_table7742
- GCC_except_table7743
- GCC_except_table7750
- GCC_except_table7774
- GCC_except_table7775
- GCC_except_table7780
- GCC_except_table7784
- GCC_except_table7785
- GCC_except_table7798
- GCC_except_table7802
- GCC_except_table7804
- GCC_except_table7806
- GCC_except_table7810
- GCC_except_table782
- GCC_except_table785
- GCC_except_table7924
- GCC_except_table794
- GCC_except_table7961
- GCC_except_table800
- GCC_except_table8018
- GCC_except_table8021
- GCC_except_table8028
- GCC_except_table8034
- GCC_except_table8041
- GCC_except_table8042
- GCC_except_table8058
- GCC_except_table8062
- GCC_except_table8063
- GCC_except_table8064
- GCC_except_table807
- GCC_except_table8113
- GCC_except_table8114
- GCC_except_table8116
- GCC_except_table8119
- GCC_except_table8146
- GCC_except_table8147
- GCC_except_table8152
- GCC_except_table8172
- GCC_except_table8190
- GCC_except_table8191
- GCC_except_table8192
- GCC_except_table8201
- GCC_except_table8206
- GCC_except_table8207
- GCC_except_table8208
- GCC_except_table8224
- GCC_except_table8227
- GCC_except_table8234
- GCC_except_table8241
- GCC_except_table8246
- GCC_except_table8252
- GCC_except_table8264
- GCC_except_table8270
- GCC_except_table8279
- GCC_except_table8285
- GCC_except_table8286
- GCC_except_table8290
- GCC_except_table8292
- GCC_except_table8294
- GCC_except_table8298
- GCC_except_table8319
- GCC_except_table8321
- GCC_except_table8322
- GCC_except_table835
- GCC_except_table842
- GCC_except_table850
- GCC_except_table8513
- GCC_except_table8576
- GCC_except_table8608
- GCC_except_table8611
- GCC_except_table8778
- GCC_except_table879
- GCC_except_table8816
- GCC_except_table8853
- GCC_except_table8931
- GCC_except_table8933
- GCC_except_table8935
- GCC_except_table8937
- GCC_except_table8939
- GCC_except_table8941
- GCC_except_table8943
- GCC_except_table8949
- GCC_except_table8951
- GCC_except_table8954
- GCC_except_table8956
- GCC_except_table8958
- GCC_except_table8965
- GCC_except_table8971
- GCC_except_table8976
- GCC_except_table8979
- GCC_except_table8984
- GCC_except_table8989
- GCC_except_table8992
- GCC_except_table8995
- GCC_except_table902
- GCC_except_table9021
- GCC_except_table9024
- GCC_except_table9025
- GCC_except_table9064
- GCC_except_table9065
- GCC_except_table9066
- GCC_except_table9068
- GCC_except_table9069
- GCC_except_table9071
- GCC_except_table9072
- GCC_except_table9073
- GCC_except_table9075
- GCC_except_table9076
- GCC_except_table9078
- GCC_except_table9082
- GCC_except_table9083
- GCC_except_table9087
- GCC_except_table9138
- GCC_except_table9145
- GCC_except_table920
- GCC_except_table9255
- GCC_except_table9258
- GCC_except_table9260
- GCC_except_table9262
- GCC_except_table9264
- GCC_except_table9265
- GCC_except_table9272
- GCC_except_table9274
- GCC_except_table9275
- GCC_except_table944
- GCC_except_table948
- GCC_except_table962
- GCC_except_table967
- __OBJC_$_INSTANCE_METHODS_HAP2AccessoryServer(Paired|PairedInternal|Unpaired)
- __OBJC_$_INSTANCE_METHODS_HAP2AccessoryServerBrowser
- __OBJC_$_INSTANCE_METHODS_HAP2AccessoryServerCoordinator
- __OBJC_CLASS_PROTOCOLS_$_HAP2AccessoryServer(Paired|PairedInternal|Unpaired)
- ___77-[HAP2AccessoryServer(Paired) mergeWithNewlyDiscoveredPairedAccessoryServer:]_block_invoke
- ___77-[HAP2CoAPClient sendRequestWithMethod:path:payload:dscpPriority:completion:]_block_invoke
- ___77-[HAP2CoAPClient sendRequestWithMethod:path:payload:dscpPriority:completion:]_block_invoke_2
- ___87-[HAP2CoAPClient _sendRequestWithMethod:path:payload:activity:dscpPriority:completion:]_block_invoke
- ___87-[HAP2CoAPClient _sendRequestWithMethod:path:payload:activity:dscpPriority:completion:]_block_invoke_2
- ___block_descriptor_48_e693_v24?0"HAP2CoAPClient"8^{coap_session_t=CCCIII{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}}^{coap_endpoint_t}^{coap_context_t}^vSCi^{coap_queue_t}Q[8C]Q^{coap_pdu_t}QQQQQ*Q*Q^vI{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}Ii}16l
- ___block_descriptor_48_e8_32bs40w_e839_v24?0^{coap_context_t=[6S]^{coap_resource_t}^{coap_resource_t}^{coap_async_state_t}Q^{coap_queue_t}^{coap_endpoint_t}^{coap_session_t}^?^?^?^?^?^?^?^?^?^?^v*Q*QIIIII^v}8^{coap_session_t=CCCIII{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}}^{coap_endpoint_t}^{coap_context_t}^vSCi^{coap_queue_t}Q[8C]Q^{coap_pdu_t}QQQQQ*Q*Q^vI{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}Ii}16lw40l8s32l8
- ___block_descriptor_56_e8_32s40bs48w_e5_v8?0lw48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40r48r_e5_v8?0ls32l8r40l8r48l8
- ___block_descriptor_57_e8_32s40bs48w_e5_v8?0lw48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48bs56w_e20_v20?0B8"NSError"12ls32l8s48l8w56l8s40l8
- ___block_descriptor_69_e8_32s40s48s_e693_v24?0"HAP2CoAPClient"8^{coap_session_t=CCCIII{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}}^{coap_endpoint_t}^{coap_context_t}^vSCi^{coap_queue_t}Q[8C]Q^{coap_pdu_t}QQQQQ*Q*Q^vI{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}Ii}16ls32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56r64r_e5_v8?0ls32l8r56l8s40l8r64l8s48l8
- ___block_descriptor_81_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- _logCategory._hmf_once_t78
- _logCategory._hmf_once_v79
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
+ "%@ Resolve completed in state %lu (not Opening), ignoring"
+ "%@ Sending hello from secondary transport"
+ "%@.registry"
+ "%@.registry.propertyLock"
+ "(nil)"
+ "(null)"
+ "00000274-0000-1000-8000-0026BB765291"
+ "00000275-0000-1000-8000-0026BB765291"
+ "3"
+ "<%@: %p primary=%lu secondary=%lu cachedPrimary=%@ cachedSecondary=%@>"
+ "<%s, %@>"
+ "<HAPBluetoothMetrics bluetoothVersion=%@, rssi=%@, txPowerLevel=%@, packetRxCount=%@, packetTxCount=%@, packetRxErrorCount=%@, packetTxErrorCount=%@, overrunCount=%@, connectionStatus=%@, connectionCount=%@, connectionErrorCount=%@, disconnectionCount=%@, disconnectionErrorCount=%@, hwExceptionCount=%@>"
+ "<HAPBootReasonsMetrics unspecifiedBootCount=%@, powerOnBootCount=%@, brownOutResetBootCount=%@, softwareWatchdogResetBootCount=%@, hardwareWatchdogResetBootCount=%@, softwareUpdateCompletedBootCount=%@, softwareResetBootCount=%@, softwareExceptionBootCount=%@, hardwareFaultBootCount=%@, stackOverflowBootCount=%@, heapOverflowBootCount=%@, temperatureLimitBootCount=%@, connectivityMonitorBootCount=%@>"
+ "<HAPCHMMetrics wifiTransportLossCount=%@, wifiRecoveryAttemptCount=%@, wifiRestartCount=%@, wifiFirstRestartRecoveryTime=%@, wifiFirstRestartCompleted=%@, wifiFirstRestartConnectivityState=%@, threadTransportLossCount=%@, threadRecoveryAttemptCount=%@, threadRestartCount=%@, threadFirstRestartRecoveryTime=%@, threadFirstRestartCompleted=%@, threadFirstRestartConnectivityState=%@, hapSessionLossCount=%@, chmAccessoryRebootDurationToRecovery=%@, chmAccessoryRebootCompleted=%@>"
+ "<HAPConnectionHealthMonitor deviceRebootEnable=%@, threadRecoveryConfiguration=%@, wiFiRecoveryConfiguration=%@, recoveryStaggerDelay=%@, deviceRebootDelay=%@, threadPingTestCount=%@, threadPingTestInterval=%@, threadRestartMinInterval=%@, wiFiPingTestCount=%@, wiFiPingTestInterval=%@, wiFiRestartMinInterval=%@>"
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
+ "Created shared CtrClient for CoreHAP"
+ "DNS context already retained"
+ "DNS-SD resolve callback delivered fatal error"
+ "DNS-SD resolver delivered fatal error event"
+ "Failed to create shared CtrClient instance"
+ "Failed to derive HDS keys from foreign pair-verify session: %@"
+ "Failed to start address resolver"
+ "Foreign pair-verify HDS key derivation failed"
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
+ "HAPInternalErrorMarker"
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
+ "IPv4"
+ "IPv6"
+ "Invalid cachedPrimaryData type for device %{public}@"
+ "Invalid cachedSecondaryData type for device %{public}@"
+ "Invalid or missing configurationInfo for device %{public}@"
+ "KeepAlive"
+ "Live resolver completed with empty endpoint set"
+ "Local endpoint is neither AF_INET nor AF_INET6"
+ "Local endpoint is not IPv4"
+ "Local endpoint is not IPv6"
+ "NCP:State"
+ "NLM keep-alive listener active, skipping reachability client"
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
+ "PreferredNetworkUpdated"
+ "Primary"
+ "Q\xd1"
+ "Received ping with message id %i but session has no app data"
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
+ "Secondary"
+ "Secondary(Thread)"
+ "Session keep-alive detected missed heartbeats on all transports"
+ "Unknown HAPMetricEventBluetoothVersionType %ld"
+ "Unknown HAPMetricEventPowerSourcesEnum %ld"
+ "Unknown HAPMetricEventWiFiVersionType %ld"
+ "Unknown HAPSessionKeepAliveTransportType %ld"
+ "Unknown HAPStabilityMetricsBootReasonType %ld"
+ "Unknown HAPStabilityMetricsHardwareFaultType %ld"
+ "Unpair: evicted cache entry deviceID=%{public}@"
+ "Unsupported local address family"
+ "[%{public}@] Attempting to derive HDS keys without an active session"
+ "[%{public}@] Failed to derive HDS keys from foreign pair-verify session: %@"
+ "[%{public}@] HDS key derivation failed (pairedServer=%p controller=%p secureTransport=%p)"
+ "[%{public}@] HDS key derivation failed: no security session on HAP2 secure transport"
+ "[%{public}@] HDS peer address unavailable (pairedServer=%p controller=%p secureTransport=%p coapTransport=%p)"
+ "[%{public}@] Invalid cachedPrimaryData type for device %{public}@"
+ "[%{public}@] Invalid cachedSecondaryData type for device %{public}@"
+ "[%{public}@] Invalid or missing configurationInfo for device %{public}@"
+ "[%{public}@] Rejecting cache record for device %{public}@: version type=%{public}@ expected=%ld"
+ "[%{public}@] configureKeepAliveListener called -- NOP"
+ "adaptiveTimeout"
+ "cachedIPDidUpdate persisted deviceID=%{public}@ transport=%lu op=%{public}@"
+ "cachedPrimaryData"
+ "cachedSecondaryData"
+ "clear"
+ "cleared"
+ "coap-client"
+ "coap_session_create_client"
+ "com.apple.CoreHAP.HAP2.BrowserResolverRegistry.audit"
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
+ "version"
+ "wifiConnectivityState"
+ "wifiRecoveryAttemptCount"
+ "wifiRestartCount"
+ "wifiTransportLossCount"
+ "\x8b"
+ "\x91"
+ "\x91\xf0\xf0Q!"
- "!Aq"
- "%@ '%{private}@' resolves to %lu address(es), %@"
- "<%@: %p primary=%lu secondary=%lu>"
- "Q\xc1"
- "aborting"
- "trying first address"
- "v24@?0@\"HAP2CoAPClient\"8^{coap_session_t=CCCIII{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}}^{coap_endpoint_t}^{coap_context_t}^vSCi^{coap_queue_t}Q[8C]Q^{coap_pdu_t}QQQQQ*Q*Q^vI{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}Ii}16"
- "v24@?0^{coap_context_t=[6S]^{coap_resource_t}^{coap_resource_t}^{coap_async_state_t}Q^{coap_queue_t}^{coap_endpoint_t}^{coap_session_t}^?^?^?^?^?^?^?^?^?^?^v*Q*QIIIII^v}8^{coap_session_t=CCCIII{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}}^{coap_endpoint_t}^{coap_context_t}^vSCi^{coap_queue_t}Q[8C]Q^{coap_pdu_t}QQQQQ*Q*Q^vI{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}Ii}16"
- "\x81\xf0\xf0Q!"
- "\x8a"
- "\xd1"
```
