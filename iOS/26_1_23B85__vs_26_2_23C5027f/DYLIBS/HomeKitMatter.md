## HomeKitMatter

> `/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter`

```diff

-1371.2.9.0.0
-  __TEXT.__text: 0x143214
+1388.3.1.0.2
+  __TEXT.__text: 0x1440cc
   __TEXT.__auth_stubs: 0xaa0
-  __TEXT.__objc_methlist: 0xa40c
+  __TEXT.__objc_methlist: 0xa714
   __TEXT.__const: 0x180
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__gcc_except_tab: 0x2e58
-  __TEXT.__cstring: 0x6c58
-  __TEXT.__oslogstring: 0x28633
+  __TEXT.__gcc_except_tab: 0x2d84
+  __TEXT.__cstring: 0x6c24
+  __TEXT.__oslogstring: 0x28654
   __TEXT.__ustring: 0x68
-  __TEXT.__unwind_info: 0x2ef8
-  __TEXT.__objc_classname: 0x143f
-  __TEXT.__objc_methname: 0x25de8
-  __TEXT.__objc_methtype: 0x3b9d
-  __TEXT.__objc_stubs: 0x16620
-  __DATA_CONST.__got: 0x9d8
-  __DATA_CONST.__const: 0x49d8
-  __DATA_CONST.__objc_classlist: 0x418
+  __TEXT.__unwind_info: 0x2f28
+  __TEXT.__objc_classname: 0x1474
+  __TEXT.__objc_methname: 0x2634c
+  __TEXT.__objc_methtype: 0x3db6
+  __TEXT.__objc_stubs: 0x168c0
+  __DATA_CONST.__got: 0x9d0
+  __DATA_CONST.__const: 0x4860
+  __DATA_CONST.__objc_classlist: 0x428
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6c90
+  __DATA_CONST.__objc_selrefs: 0x6da0
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x2d8
+  __DATA_CONST.__objc_superrefs: 0x2e8
   __DATA_CONST.__objc_arraydata: 0x248
   __AUTH_CONST.__auth_got: 0x560
-  __AUTH_CONST.__const: 0x1080
-  __AUTH_CONST.__cfstring: 0x6b40
-  __AUTH_CONST.__objc_const: 0xf410
-  __AUTH_CONST.__objc_intobj: 0x17e8
+  __AUTH_CONST.__const: 0x10c0
+  __AUTH_CONST.__cfstring: 0x6c20
+  __AUTH_CONST.__objc_const: 0xf838
+  __AUTH_CONST.__objc_intobj: 0x1818
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x1d60
-  __DATA.__objc_ivar: 0xac0
+  __AUTH.__objc_data: 0x1e00
+  __DATA.__objc_ivar: 0xaf4
   __DATA.__data: 0xde0
-  __DATA.__bss: 0x408
+  __DATA.__bss: 0x438
   __DATA_DIRTY.__objc_data: 0xb90
-  __DATA_DIRTY.__bss: 0xd0
+  __DATA_DIRTY.__bss: 0xc8
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/UARPKit.framework/UARPKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7B9AC063-4F74-39C7-A032-AAAAE61D06C4
-  Functions: 4256
-  Symbols:   14722
-  CStrings:  9510
+  UUID: 23F440C2-DD73-3C1B-83CB-A6A1BC3C8CB7
+  Functions: 4307
+  Symbols:   14869
+  CStrings:  9584
 
Symbols:
+ +[HMMTRAccessoryServer shouldRetryPairingWithCommissioningSessionEstablishmentError:]
+ +[HMMTRFeatures disableFeatureMatterHRAPDeviceTypesForTests]
+ +[HMMTRFeatures enableFeatureMatterHRAPDeviceTypesForTests]
+ +[HMMTRFeatures unsetFeatureMatterHRAPDeviceTypesForTests]
+ +[HMMTRProtocolMap resetCachedProtocolMapForTesting]
+ +[HMMTRQueryImageResponseBusyTimer logCategory]
+ +[HMMTRWEDPollingTimer logCategory]
+ -[HMMTRAccessoryServer _cleanupMatterSoftwareUpdateBusyTimer]
+ -[HMMTRAccessoryServer _collectThreadNetworkCredentials:completion:]
+ -[HMMTRAccessoryServer _collectWiFiNetworkCredentials:completion:]
+ -[HMMTRAccessoryServer _commissioning:complete:abstractMetrics:]
+ -[HMMTRAccessoryServer _commissioningAndPairedNodeRecoveryComplete:abstractMetrics:]
+ -[HMMTRAccessoryServer _computeSetupPayloadString]
+ -[HMMTRAccessoryServer _createCommissioningOperationWithParameters:setupPayload:]
+ -[HMMTRAccessoryServer _initializeCredentialManagementForCommissioneeNodeID:storage:]
+ -[HMMTRAccessoryServer _onThreadScanResults:commissioning:completion:]
+ -[HMMTRAccessoryServer _onWiFiScanResults:completion:]
+ -[HMMTRAccessoryServer _parametersForNewCommissioning]
+ -[HMMTRAccessoryServer _startNewCommissioningWithPayload:]
+ -[HMMTRAccessoryServer _syncAbortStagingWithError:context:]
+ -[HMMTRAccessoryServer _threadScanRequired]
+ -[HMMTRAccessoryServer _wifiScanRequired]
+ -[HMMTRAccessoryServer busyImageResponseTimer]
+ -[HMMTRAccessoryServer commissioning:completedDeviceAttestation:error:completion:]
+ -[HMMTRAccessoryServer commissioning:failedWithError:metrics:]
+ -[HMMTRAccessoryServer commissioning:needsThreadCredentialsWithScanResults:error:completion:]
+ -[HMMTRAccessoryServer commissioning:needsWiFiCredentialsWithScanResults:error:completion:]
+ -[HMMTRAccessoryServer commissioning:readCommissioneeInfo:]
+ -[HMMTRAccessoryServer commissioning:succeededForNodeID:metrics:]
+ -[HMMTRAccessoryServer commissioningProvisionedNetworkCredentials:]
+ -[HMMTRAccessoryServer commissioningStartingNetworkScan:]
+ -[HMMTRAccessoryServer currentCommissioning]
+ -[HMMTRAccessoryServer dispatchedNetworkScanEnd]
+ -[HMMTRAccessoryServer hasBusyImageResponseTimer]
+ -[HMMTRAccessoryServer resetBusyImageResponseCounter]
+ -[HMMTRAccessoryServer setBusyImageResponseTimer:]
+ -[HMMTRAccessoryServer setCurrentCommissioning:]
+ -[HMMTRAccessoryServer setDispatchedNetworkScanEnd:]
+ -[HMMTRAccessoryServer startBusyImageResponseTimer:timeInterval:endpoint:requestParams:queue:]
+ -[HMMTRAccessoryServer stopBusyImageResponseTimer]
+ -[HMMTRAccessoryServerBrowser _isWedPollingAllowed]
+ -[HMMTRAccessoryServerBrowser _pollWedAccessories]
+ -[HMMTRAccessoryServerBrowser setWedPollingTimer:]
+ -[HMMTRAccessoryServerBrowser wedPollingTimer]
+ -[HMMTRAttestationStatus accessoryServer:completedDeviceAttestation:error:completion:]
+ -[HMMTRAttestationStatus populateAttestationParameters:]
+ -[HMMTRQueryImageResponseBusyTimer .cxx_destruct]
+ -[HMMTRQueryImageResponseBusyTimer endpoint]
+ -[HMMTRQueryImageResponseBusyTimer initWithServer:softwareUpdateProvider:timeInterval:endpoint:requestParams:queue:]
+ -[HMMTRQueryImageResponseBusyTimer logIdentifier]
+ -[HMMTRQueryImageResponseBusyTimer queue]
+ -[HMMTRQueryImageResponseBusyTimer requestParams]
+ -[HMMTRQueryImageResponseBusyTimer server]
+ -[HMMTRQueryImageResponseBusyTimer setEndpoint:]
+ -[HMMTRQueryImageResponseBusyTimer setQueue:]
+ -[HMMTRQueryImageResponseBusyTimer setRequestParams:]
+ -[HMMTRQueryImageResponseBusyTimer setServer:]
+ -[HMMTRQueryImageResponseBusyTimer setSoftwareUpdateProvider:]
+ -[HMMTRQueryImageResponseBusyTimer setUpdateTimer:]
+ -[HMMTRQueryImageResponseBusyTimer softwareUpdateProvider]
+ -[HMMTRQueryImageResponseBusyTimer start]
+ -[HMMTRQueryImageResponseBusyTimer stop]
+ -[HMMTRQueryImageResponseBusyTimer timerDidFire:]
+ -[HMMTRQueryImageResponseBusyTimer updateTimer]
+ -[HMMTRSoftwareUpdateProvider triggerQueryImageWithPairing:initiationType:requestParams:completionHandler:]
+ -[HMMTRThreadRadioManager _connectToAccessoryWithExtendedMACAddress:asRetry:completion:]
+ -[HMMTRWEDPollingTimer .cxx_destruct]
+ -[HMMTRWEDPollingTimer _scheduleNextPolling]
+ -[HMMTRWEDPollingTimer attemptCount]
+ -[HMMTRWEDPollingTimer browser]
+ -[HMMTRWEDPollingTimer dealloc]
+ -[HMMTRWEDPollingTimer initWithBrowser:queue:]
+ -[HMMTRWEDPollingTimer logIdentifier]
+ -[HMMTRWEDPollingTimer pollingActive]
+ -[HMMTRWEDPollingTimer pollingTimer]
+ -[HMMTRWEDPollingTimer queue]
+ -[HMMTRWEDPollingTimer setAttemptCount:]
+ -[HMMTRWEDPollingTimer setBrowser:]
+ -[HMMTRWEDPollingTimer setPollingActive:]
+ -[HMMTRWEDPollingTimer setPollingTimer:]
+ -[HMMTRWEDPollingTimer setQueue:]
+ -[HMMTRWEDPollingTimer startPolling]
+ -[HMMTRWEDPollingTimer stopPolling]
+ -[HMMTRWEDPollingTimer timerDidFire:]
+ GCC_except_table1030
+ GCC_except_table1034
+ GCC_except_table1036
+ GCC_except_table1142
+ GCC_except_table1202
+ GCC_except_table1248
+ GCC_except_table1256
+ GCC_except_table1305
+ GCC_except_table1313
+ GCC_except_table1350
+ GCC_except_table1387
+ GCC_except_table1416
+ GCC_except_table1613
+ GCC_except_table1654
+ GCC_except_table1806
+ GCC_except_table1807
+ GCC_except_table1808
+ GCC_except_table1811
+ GCC_except_table1831
+ GCC_except_table1832
+ GCC_except_table1833
+ GCC_except_table1834
+ GCC_except_table1835
+ GCC_except_table1838
+ GCC_except_table1841
+ GCC_except_table1842
+ GCC_except_table1843
+ GCC_except_table1844
+ GCC_except_table1845
+ GCC_except_table1846
+ GCC_except_table1847
+ GCC_except_table1912
+ GCC_except_table1950
+ GCC_except_table2025
+ GCC_except_table2137
+ GCC_except_table2139
+ GCC_except_table2169
+ GCC_except_table2177
+ GCC_except_table2223
+ GCC_except_table2263
+ GCC_except_table2325
+ GCC_except_table2574
+ GCC_except_table2578
+ GCC_except_table2632
+ GCC_except_table2673
+ GCC_except_table2742
+ GCC_except_table2743
+ GCC_except_table2744
+ GCC_except_table2766
+ GCC_except_table2767
+ GCC_except_table2768
+ GCC_except_table2769
+ GCC_except_table2770
+ GCC_except_table2772
+ GCC_except_table2773
+ GCC_except_table2785
+ GCC_except_table2787
+ GCC_except_table2806
+ GCC_except_table2822
+ GCC_except_table2828
+ GCC_except_table2839
+ GCC_except_table2842
+ GCC_except_table2846
+ GCC_except_table2864
+ GCC_except_table2868
+ GCC_except_table2870
+ GCC_except_table2889
+ GCC_except_table2895
+ GCC_except_table2900
+ GCC_except_table2963
+ GCC_except_table2964
+ GCC_except_table3336
+ GCC_except_table3337
+ GCC_except_table3338
+ GCC_except_table3342
+ GCC_except_table3347
+ GCC_except_table3350
+ GCC_except_table3365
+ GCC_except_table3380
+ GCC_except_table3456
+ GCC_except_table3458
+ GCC_except_table3465
+ GCC_except_table3466
+ GCC_except_table3526
+ GCC_except_table3529
+ GCC_except_table3537
+ GCC_except_table3556
+ GCC_except_table3559
+ GCC_except_table3597
+ GCC_except_table3601
+ GCC_except_table3618
+ GCC_except_table3620
+ GCC_except_table3638
+ GCC_except_table3708
+ GCC_except_table3755
+ GCC_except_table3773
+ GCC_except_table3796
+ GCC_except_table3800
+ GCC_except_table3815
+ GCC_except_table3816
+ GCC_except_table3817
+ GCC_except_table3823
+ GCC_except_table3830
+ GCC_except_table3888
+ GCC_except_table3908
+ GCC_except_table3969
+ GCC_except_table3974
+ GCC_except_table3977
+ GCC_except_table4060
+ GCC_except_table4061
+ GCC_except_table4116
+ GCC_except_table4119
+ GCC_except_table4181
+ GCC_except_table4243
+ GCC_except_table4247
+ GCC_except_table4251
+ GCC_except_table4254
+ GCC_except_table4287
+ GCC_except_table862
+ GCC_except_table903
+ GCC_except_table966
+ GCC_except_table970
+ GCC_except_table972
+ GCC_except_table974
+ GCC_except_table976
+ GCC_except_table980
+ GCC_except_table984
+ GCC_except_table987
+ _HMMTRQueryImageInitiationTypeAsString
+ _OBJC_CLASS_$_HMMTRQueryImageResponseBusyTimer
+ _OBJC_CLASS_$_HMMTRWEDPollingTimer
+ _OBJC_CLASS_$_MTRCommissioningOperation
+ _OBJC_IVAR_$_HMMTRAccessoryServer._busyImageResponseTimer
+ _OBJC_IVAR_$_HMMTRAccessoryServer._currentCommissioning
+ _OBJC_IVAR_$_HMMTRAccessoryServer._dispatchedNetworkScanEnd
+ _OBJC_IVAR_$_HMMTRAccessoryServerBrowser._wedPollingTimer
+ _OBJC_IVAR_$_HMMTRQueryImageResponseBusyTimer._endpoint
+ _OBJC_IVAR_$_HMMTRQueryImageResponseBusyTimer._queue
+ _OBJC_IVAR_$_HMMTRQueryImageResponseBusyTimer._requestParams
+ _OBJC_IVAR_$_HMMTRQueryImageResponseBusyTimer._server
+ _OBJC_IVAR_$_HMMTRQueryImageResponseBusyTimer._softwareUpdateProvider
+ _OBJC_IVAR_$_HMMTRQueryImageResponseBusyTimer._updateTimer
+ _OBJC_IVAR_$_HMMTRWEDPollingTimer._attemptCount
+ _OBJC_IVAR_$_HMMTRWEDPollingTimer._browser
+ _OBJC_IVAR_$_HMMTRWEDPollingTimer._pollingActive
+ _OBJC_IVAR_$_HMMTRWEDPollingTimer._pollingTimer
+ _OBJC_IVAR_$_HMMTRWEDPollingTimer._queue
+ _OBJC_METACLASS_$_HMMTRQueryImageResponseBusyTimer
+ _OBJC_METACLASS_$_HMMTRWEDPollingTimer
+ __OBJC_$_CLASS_METHODS_HMMTRQueryImageResponseBusyTimer
+ __OBJC_$_CLASS_METHODS_HMMTRWEDPollingTimer
+ __OBJC_$_INSTANCE_METHODS_HMMTRQueryImageResponseBusyTimer
+ __OBJC_$_INSTANCE_METHODS_HMMTRWEDPollingTimer
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRQueryImageResponseBusyTimer
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRWEDPollingTimer
+ __OBJC_$_PROP_LIST_HMMTRQueryImageResponseBusyTimer
+ __OBJC_$_PROP_LIST_HMMTRWEDPollingTimer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTRCommissioningDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_MTRCommissioningDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTRCommissioningDelegate
+ __OBJC_$_PROTOCOL_REFS_MTRCommissioningDelegate
+ __OBJC_CLASS_PROTOCOLS_$_HMMTRQueryImageResponseBusyTimer
+ __OBJC_CLASS_PROTOCOLS_$_HMMTRWEDPollingTimer
+ __OBJC_CLASS_RO_$_HMMTRQueryImageResponseBusyTimer
+ __OBJC_CLASS_RO_$_HMMTRWEDPollingTimer
+ __OBJC_LABEL_PROTOCOL_$_MTRCommissioningDelegate
+ __OBJC_METACLASS_RO_$_HMMTRQueryImageResponseBusyTimer
+ __OBJC_METACLASS_RO_$_HMMTRWEDPollingTimer
+ __OBJC_PROTOCOL_$_MTRCommissioningDelegate
+ ___101-[HMMTRAccessoryServer updateAccessoryControlToIncludeAdministratorNodes:sharedUserNodes:completion:]_block_invoke.843
+ ___102-[HMMTRAccessoryServer updateAllCharacteristicValuesPostHAPServiceEnumerationForAccessory:completion:]_block_invoke.791
+ ___107-[HMMTRAccessoryServerBrowser _fetchDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.213
+ ___107-[HMMTRSoftwareUpdateProvider triggerQueryImageWithPairing:initiationType:requestParams:completionHandler:]_block_invoke
+ ___110-[HMMTRAccessoryServerBrowser removeAllDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.215
+ ___112-[HMMTRAccessoryServer _updateAdditionalCharacteristicsFromCharacteristicUpdate:service:path:completionHandler:]_block_invoke.385
+ ___114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke.902
+ ___114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke.905
+ ___117-[HMMTRAccessoryServer _findSystemCommissionerPairingMatchingSetupPayload:systemCommissionerPairings:pairingManager:]_block_invoke.265
+ ___117-[HMMTRAccessoryServer _findSystemCommissionerPairingMatchingSetupPayload:systemCommissionerPairings:pairingManager:]_block_invoke.266
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.511
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.513
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.515
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.516
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.518
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.520
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.517
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.519
+ ___119-[HMMTRAccessoryServerBrowser removeDevicePairingFabricForSystemCommissionerDeviceWithNodeID:fabric:completionHandler:]_block_invoke.211
+ ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.329
+ ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.336
+ ___278-[HMMTRAccessoryServerBrowser _stageAccessoryServerWithSetupPayload:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:commissioneeInfoHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke.198
+ ___35+[HMMTRWEDPollingTimer logCategory]_block_invoke
+ ___35-[HMMTRWEDPollingTimer stopPolling]_block_invoke
+ ___36-[HMMTRWEDPollingTimer startPolling]_block_invoke
+ ___37-[HMMTRAccessoryServer finishPairing]_block_invoke.771
+ ___37-[HMMTRAccessoryServer timerDidFire:]_block_invoke.282
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.646
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.648
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.649
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.655
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.656
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.657
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.658
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.650
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.659
+ ___40-[HMMTRAccessoryServerBrowser configure]_block_invoke.142
+ ___42-[HMMTRAccessoryServer _setupMatterDevice]_block_invoke.313
+ ___43-[HMMTRAccessoryServer _setupThreadPairing]_block_invoke.472
+ ___43-[HMMTRAccessoryServer _unpair:completion:]_block_invoke.305
+ ___43-[HMMTRAccessoryServer discoverAccessories]_block_invoke.308
+ ___47+[HMMTRQueryImageResponseBusyTimer logCategory]_block_invoke
+ ___47-[HMMTRAccessoryServer processAttributeReport:]_block_invoke.971
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.867
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.870
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.872
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke_2.871
+ ___49-[HMMTRAccessoryServerBrowser startBluetoothScan]_block_invoke.365
+ ___49-[HMMTRQueryImageResponseBusyTimer timerDidFire:]_block_invoke
+ ___49-[HMMTRQueryImageResponseBusyTimer timerDidFire:]_block_invoke.4
+ ___50-[HMMTRAccessoryServerBrowser _pollWedAccessories]_block_invoke
+ ___51-[HMMTRAccessoryServer device:receivedEventReport:]_block_invoke.972
+ ___52-[HMMTRAccessoryServer populateACLEntriesForPairing]_block_invoke.644
+ ___52-[HMMTRAccessoryServerBrowser _cleanupStagedServers]_block_invoke.318
+ ___53-[HMMTRAccessoryServer _tryPairingUsingMatterSupport]_block_invoke.259
+ ___54-[HMMTRAccessoryServer _onWiFiScanResults:completion:]_block_invoke
+ ___54-[HMMTRAccessoryServer _onWiFiScanResults:completion:]_block_invoke_2
+ ___55-[HMMTRAccessoryServer device:receivedAttributeReport:]_block_invoke.970
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.430
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.431
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.432
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.433
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.434
+ ___59-[HMMTRAccessoryServer commissioning:readCommissioneeInfo:]_block_invoke
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.443
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.445
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.446
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.447
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.907
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.909
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.913
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.915
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.436
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.437
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.438
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.439
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.440
+ ___62-[HMMTRAccessoryServerBrowser stopDiscoveringAccessoryServers]_block_invoke.187
+ ___63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.821
+ ___63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.822
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.490
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.491
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.492
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.493
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.494
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.495
+ ___64-[HMMTRAccessoryServer _commissioning:complete:abstractMetrics:]_block_invoke
+ ___64-[HMMTRAccessoryServer _commissioning:complete:abstractMetrics:]_block_invoke.930
+ ___64-[HMMTRAccessoryServer _commissioning:complete:abstractMetrics:]_block_invoke_2
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.459
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.460
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.461
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.462
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.463
+ ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.935
+ ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.936
+ ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.937
+ ___64-[HMMTRAccessoryServerBrowser _initializeAndStartBonjourBrowser]_block_invoke.150
+ ___65-[HMMTRAccessoryServer stopPairingWithError:metricsReadyHandler:]_block_invoke.294
+ ___66-[HMMTRAccessoryServer _collectWiFiNetworkCredentials:completion:]_block_invoke
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.454
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.455
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.456
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.457
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.458
+ ___68-[HMMTRAccessoryServer _collectThreadNetworkCredentials:completion:]_block_invoke
+ ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.449
+ ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.450
+ ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.453
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.479
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.480
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.481
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.484
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.488
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.489
+ ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.426
+ ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.427
+ ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.428
+ ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.188
+ ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.191
+ ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.193
+ ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.195
+ ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke_2.194
+ ___70-[HMMTRAccessoryServer _onThreadScanResults:commissioning:completion:]_block_invoke
+ ___70-[HMMTRAccessoryServer _onThreadScanResults:commissioning:completion:]_block_invoke.879
+ ___70-[HMMTRAccessoryServer _onThreadScanResults:commissioning:completion:]_block_invoke.880
+ ___70-[HMMTRAccessoryServer _onThreadScanResults:commissioning:completion:]_block_invoke_2
+ ___71-[HMMTRAccessoryServer validateAttestationDeviceInfo:error:completion:]_block_invoke.284
+ ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.406
+ ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.412
+ ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.413
+ ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.414
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.473
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.474
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.475
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.477
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.478
+ ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.271
+ ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.272
+ ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.273
+ ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.274
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.819
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.820
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke_2.817
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.792
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.793
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.802
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.811
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.813
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.814
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke_2.806
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.298
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.299
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.301
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.302
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.300
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.303
+ ___76-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithNodeID:completion:]_block_invoke.196
+ ___79-[HMMTRAccessoryServerBrowser _updateAccessoryControlListForServer:completion:]_block_invoke.323
+ ___82-[HMMTRAccessoryServer fetchColorControlClusterForHapAccessory:completionHandler:]_block_invoke.916
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.884
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.885
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.886
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.889
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke_2.888
+ ___82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.162
+ ___82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.164
+ ___83-[HMMTRAccessoryServer updateAccessoryControlToRemoveAdministratorNode:completion:]_block_invoke.844
+ ___84-[HMMTRAccessoryServer _queueOpenPairingWindowWithPINForDuration:completionHandler:]_block_invoke.416
+ ___84-[HMMTRAccessoryServer _queueOpenPairingWindowWithPINForDuration:completionHandler:]_block_invoke.417
+ ___84-[HMMTRAccessoryServer _queueOpenPairingWindowWithPINForDuration:completionHandler:]_block_invoke.419
+ ___84-[HMMTRAccessoryServer _queueOpenPairingWindowWithPINForDuration:completionHandler:]_block_invoke.420
+ ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.392
+ ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.394
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.890
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.891
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.892
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.893
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.897
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.898
+ ___86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.938
+ ___86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.939
+ ___86-[HMMTRAttestationStatus accessoryServer:completedDeviceAttestation:error:completion:]_block_invoke
+ ___86-[HMMTRAttestationStatus accessoryServer:completedDeviceAttestation:error:completion:]_block_invoke.12
+ ___86-[HMMTRAttestationStatus accessoryServer:completedDeviceAttestation:error:completion:]_block_invoke.14
+ ___86-[HMMTRAttestationStatus accessoryServer:completedDeviceAttestation:error:completion:]_block_invoke.15
+ ___86-[HMMTRAttestationStatus accessoryServer:completedDeviceAttestation:error:completion:]_block_invoke.16
+ ___86-[HMMTRAttestationStatus accessoryServer:completedDeviceAttestation:error:completion:]_block_invoke.18
+ ___86-[HMMTRAttestationStatus accessoryServer:completedDeviceAttestation:error:completion:]_block_invoke.9
+ ___86-[HMMTRAttestationStatus accessoryServer:completedDeviceAttestation:error:completion:]_block_invoke_2
+ ___88-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:keepAliveOnly:]_block_invoke.359
+ ___88-[HMMTRThreadRadioManager _connectToAccessoryWithExtendedMACAddress:asRetry:completion:]_block_invoke
+ ___88-[HMMTRThreadRadioManager _connectToAccessoryWithExtendedMACAddress:asRetry:completion:]_block_invoke_2
+ ___88-[HMMTRThreadRadioManager _connectToAccessoryWithExtendedMACAddress:asRetry:completion:]_block_invoke_3
+ ___92-[HMMTRAccessoryServer _createFirmwareUpdateServiceWithInstanceID:device:completionHandler:]_block_invoke.784
+ ___92-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fabricUUID:fatalError:]_block_invoke.322
+ ___94-[HMMTRAccessoryServer updateAccessoryControlToAdministratorNodes:sharedUserNodes:completion:]_block_invoke.842
+ ___94-[HMMTRAccessoryServerBrowser _handleAddOrUpdateWithDiscriminator:vendorID:productID:overBLE:]_block_invoke.171
+ ___97-[HMMTRAccessoryServerBrowser removeAccessoryServer:fromDiscoveredAccessoryServerListWithReason:]_block_invoke.306
+ ___99-[HMMTRAccessoryServer _tryPairingWithOnboardingPayload:systemCommissionerPairings:pairingManager:]_block_invoke.262
+ ___99-[HMMTRAccessoryServer _tryPairingWithOnboardingPayload:systemCommissionerPairings:pairingManager:]_block_invoke.263
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.521
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.522
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.529
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.530
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke_2.525
+ ___Block_byref_object_copy_.10450
+ ___Block_byref_object_copy_.11225
+ ___Block_byref_object_copy_.11877
+ ___Block_byref_object_copy_.12581
+ ___Block_byref_object_copy_.12748
+ ___Block_byref_object_copy_.2063
+ ___Block_byref_object_copy_.3423
+ ___Block_byref_object_copy_.3711
+ ___Block_byref_object_copy_.4792
+ ___Block_byref_object_copy_.5962
+ ___Block_byref_object_copy_.6113
+ ___Block_byref_object_copy_.7929
+ ___Block_byref_object_copy_.8362
+ ___Block_byref_object_copy_.9486
+ ___Block_byref_object_dispose_.10451
+ ___Block_byref_object_dispose_.11226
+ ___Block_byref_object_dispose_.11878
+ ___Block_byref_object_dispose_.12582
+ ___Block_byref_object_dispose_.12749
+ ___Block_byref_object_dispose_.2064
+ ___Block_byref_object_dispose_.3424
+ ___Block_byref_object_dispose_.3712
+ ___Block_byref_object_dispose_.4793
+ ___Block_byref_object_dispose_.5963
+ ___Block_byref_object_dispose_.6114
+ ___Block_byref_object_dispose_.7930
+ ___Block_byref_object_dispose_.8363
+ ___Block_byref_object_dispose_.9487
+ ___block_descriptor_48_e8_32s40bs_e35_v16?0"MTSWiFiNetworkAssociation"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e37_v16?0"MTSThreadNetworkAssociation"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e77_v24?0"MTRGeneralCommissioningClusterArmFailSafeResponseParams"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e84_v32?0"MTRCommissioningParameters"8"NSError"16"HMMTRAccessoryPairingEndContext"24ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs56w_e35_v24?0"THCredentials"8"NSError"16lw56l8s32l8s48l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
+ ___block_literal_global.10245
+ ___block_literal_global.10321
+ ___block_literal_global.10931
+ ___block_literal_global.11526
+ ___block_literal_global.11696
+ ___block_literal_global.11911
+ ___block_literal_global.12047
+ ___block_literal_global.12179
+ ___block_literal_global.12398
+ ___block_literal_global.1517
+ ___block_literal_global.1573
+ ___block_literal_global.1665
+ ___block_literal_global.1912
+ ___block_literal_global.2187
+ ___block_literal_global.2242
+ ___block_literal_global.2289
+ ___block_literal_global.2376
+ ___block_literal_global.2737
+ ___block_literal_global.2885
+ ___block_literal_global.312
+ ___block_literal_global.315
+ ___block_literal_global.3183
+ ___block_literal_global.3328
+ ___block_literal_global.3357
+ ___block_literal_global.3449
+ ___block_literal_global.354
+ ___block_literal_global.3603
+ ___block_literal_global.373
+ ___block_literal_global.3800
+ ___block_literal_global.3951
+ ___block_literal_global.4074
+ ___block_literal_global.4561
+ ___block_literal_global.4889
+ ___block_literal_global.5177
+ ___block_literal_global.528
+ ___block_literal_global.5311
+ ___block_literal_global.5413
+ ___block_literal_global.5677
+ ___block_literal_global.5850
+ ___block_literal_global.6097
+ ___block_literal_global.6285
+ ___block_literal_global.6425
+ ___block_literal_global.6534
+ ___block_literal_global.6568
+ ___block_literal_global.6589
+ ___block_literal_global.6839
+ ___block_literal_global.6852
+ ___block_literal_global.6946
+ ___block_literal_global.7040
+ ___block_literal_global.7134
+ ___block_literal_global.7237
+ ___block_literal_global.7331
+ ___block_literal_global.7470
+ ___block_literal_global.7611
+ ___block_literal_global.7717
+ ___block_literal_global.7795
+ ___block_literal_global.789
+ ___block_literal_global.796
+ ___block_literal_global.809
+ ___block_literal_global.8145
+ ___block_literal_global.82.10246
+ ___block_literal_global.8373
+ ___block_literal_global.8722
+ ___block_literal_global.8840
+ ___block_literal_global.8976
+ ___block_literal_global.9517
+ ___block_literal_global.979
+ ___block_literal_global.9922
+ _isFeatureMatterHRAPDeviceTypesEnabled
+ _isFeatureMatterHRAPDeviceTypesEnabledForTests
+ _logCategory._hmf_once_t0.2241
+ _logCategory._hmf_once_t0.3327
+ _logCategory._hmf_once_t0.5849
+ _logCategory._hmf_once_t0.6567
+ _logCategory._hmf_once_t10.12397
+ _logCategory._hmf_once_t11.3182
+ _logCategory._hmf_once_t13.3448
+ _logCategory._hmf_once_t13.3799
+ _logCategory._hmf_once_t14.6851
+ _logCategory._hmf_once_t14.6945
+ _logCategory._hmf_once_t14.7039
+ _logCategory._hmf_once_t14.7236
+ _logCategory._hmf_once_t14.7330
+ _logCategory._hmf_once_t14.7469
+ _logCategory._hmf_once_t2.10320
+ _logCategory._hmf_once_t2.5412
+ _logCategory._hmf_once_t2.6533
+ _logCategory._hmf_once_t2.7610
+ _logCategory._hmf_once_t20.12046
+ _logCategory._hmf_once_t26.7133
+ _logCategory._hmf_once_t3.1572
+ _logCategory._hmf_once_t31.12178
+ _logCategory._hmf_once_t4.3950
+ _logCategory._hmf_once_t4.7716
+ _logCategory._hmf_once_t40.6159
+ _logCategory._hmf_once_t6.2375
+ _logCategory._hmf_once_t670
+ _logCategory._hmf_once_t68.12607
+ _logCategory._hmf_once_t8.11695
+ _logCategory._hmf_once_t8.8839
+ _logCategory._hmf_once_v1.2243
+ _logCategory._hmf_once_v1.3329
+ _logCategory._hmf_once_v1.5851
+ _logCategory._hmf_once_v1.6569
+ _logCategory._hmf_once_v11.12399
+ _logCategory._hmf_once_v12.3184
+ _logCategory._hmf_once_v14.3450
+ _logCategory._hmf_once_v14.3801
+ _logCategory._hmf_once_v15.6853
+ _logCategory._hmf_once_v15.6947
+ _logCategory._hmf_once_v15.7041
+ _logCategory._hmf_once_v15.7238
+ _logCategory._hmf_once_v15.7332
+ _logCategory._hmf_once_v15.7471
+ _logCategory._hmf_once_v21.12048
+ _logCategory._hmf_once_v27.7135
+ _logCategory._hmf_once_v3.10322
+ _logCategory._hmf_once_v3.5414
+ _logCategory._hmf_once_v3.6535
+ _logCategory._hmf_once_v3.7612
+ _logCategory._hmf_once_v32.12180
+ _logCategory._hmf_once_v4.1574
+ _logCategory._hmf_once_v41.6160
+ _logCategory._hmf_once_v5.3952
+ _logCategory._hmf_once_v5.7718
+ _logCategory._hmf_once_v671
+ _logCategory._hmf_once_v69.12608
+ _logCategory._hmf_once_v7.2377
+ _logCategory._hmf_once_v9.11697
+ _logCategory._hmf_once_v9.8841
+ _objc_msgSend$_cleanupMatterSoftwareUpdateBusyTimer
+ _objc_msgSend$_collectThreadNetworkCredentials:completion:
+ _objc_msgSend$_collectWiFiNetworkCredentials:completion:
+ _objc_msgSend$_commissioning:complete:abstractMetrics:
+ _objc_msgSend$_commissioningAndPairedNodeRecoveryComplete:abstractMetrics:
+ _objc_msgSend$_computeSetupPayloadString
+ _objc_msgSend$_connectToAccessoryWithExtendedMACAddress:asRetry:completion:
+ _objc_msgSend$_createCommissioningOperationWithParameters:setupPayload:
+ _objc_msgSend$_initializeCredentialManagementForCommissioneeNodeID:storage:
+ _objc_msgSend$_isWedPollingAllowed
+ _objc_msgSend$_onThreadScanResults:commissioning:completion:
+ _objc_msgSend$_onWiFiScanResults:completion:
+ _objc_msgSend$_parametersForNewCommissioning
+ _objc_msgSend$_pollWedAccessories
+ _objc_msgSend$_scheduleNextPolling
+ _objc_msgSend$_startNewCommissioningWithPayload:
+ _objc_msgSend$_syncAbortStagingWithError:context:
+ _objc_msgSend$_threadScanRequired
+ _objc_msgSend$_wifiScanRequired
+ _objc_msgSend$accessoryServer:completedDeviceAttestation:error:completion:
+ _objc_msgSend$attemptCount
+ _objc_msgSend$attributes
+ _objc_msgSend$busyImageResponseTimer
+ _objc_msgSend$cancelCommissioningForNodeID:error:
+ _objc_msgSend$currentCommissioning
+ _objc_msgSend$dispatchedNetworkScanEnd
+ _objc_msgSend$hasBusyImageResponseTimer
+ _objc_msgSend$initWithBrowser:queue:
+ _objc_msgSend$initWithParameters:setupPayload:delegate:queue:
+ _objc_msgSend$initWithServer:softwareUpdateProvider:timeInterval:endpoint:requestParams:queue:
+ _objc_msgSend$matterDeviceTypeID
+ _objc_msgSend$pollingActive
+ _objc_msgSend$pollingTimer
+ _objc_msgSend$populateAttestationParameters:
+ _objc_msgSend$qrCodeString
+ _objc_msgSend$queryImageWithPairing:requestParams:queue:initiationType:completionHandler:
+ _objc_msgSend$requestParams
+ _objc_msgSend$resetBusyImageResponseCounter
+ _objc_msgSend$setAttemptCount:
+ _objc_msgSend$setBusyImageResponseTimer:
+ _objc_msgSend$setCurrentCommissioning:
+ _objc_msgSend$setDispatchedNetworkScanEnd:
+ _objc_msgSend$setExtraAttributesToRead:
+ _objc_msgSend$setForceThreadScan:
+ _objc_msgSend$setForceWiFiScan:
+ _objc_msgSend$setPollingActive:
+ _objc_msgSend$setPollingTimer:
+ _objc_msgSend$shouldRetryPairingWithCommissioningSessionEstablishmentError:
+ _objc_msgSend$startPolling
+ _objc_msgSend$startWithController:
+ _objc_msgSend$stopBusyImageResponseTimer
+ _objc_msgSend$stopPolling
+ _objc_msgSend$threadCredentialManagementImplicitlyEnabledForDeviceType:
+ _objc_msgSend$triggerQueryImageWithPairing:initiationType:requestParams:completionHandler:
+ _objc_msgSend$wedPollingTimer
+ _objc_msgSend$wifiCredentials
+ _objc_msgSend$wifiSSID
+ _onceToken
- -[HMMTRAccessoryServer _collectNetworkCredentials:]
- -[HMMTRAccessoryServer _commissionWithParams:]
- -[HMMTRAccessoryServer _continueNetworkProvisioning]
- -[HMMTRAccessoryServer _controller:commissioningAndPairedNodeRecoveryComplete:nodeID:abstractMetrics:]
- -[HMMTRAccessoryServer _controller:commissioningComplete:nodeID:abstractMetrics:]
- -[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationWithCompletion:]
- -[HMMTRAccessoryServer _getCommissioneeHasActiveNetworkWithNetworkCommissioningCluster:completion:]
- -[HMMTRAccessoryServer _getCommissioneeNetworkCommissioningClusterEndpointWithDevice:completion:]
- -[HMMTRAccessoryServer _onNetworkScanResults:]
- -[HMMTRAccessoryServer _onThreadScanResults:]
- -[HMMTRAccessoryServer _onWiFiScanResults:]
- -[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]
- -[HMMTRAccessoryServer commissionCompletePending]
- -[HMMTRAccessoryServer commissioneeNetworks]
- -[HMMTRAccessoryServer controller:commissioneeHasReceivedNetworkCredentials:]
- -[HMMTRAccessoryServer controller:commissioningComplete:nodeID:metrics:]
- -[HMMTRAccessoryServer controller:commissioningSessionEstablishmentDone:]
- -[HMMTRAccessoryServer controller:readCommissioneeInfo:]
- -[HMMTRAccessoryServer controller:statusUpdate:]
- -[HMMTRAccessoryServer setCommissionCompletePending:]
- -[HMMTRAccessoryServer setCommissioneeNetworks:]
- -[HMMTRAccessoryServerBrowser _getRandomFabricId]
- -[HMMTRAccessoryServerBrowser _pollWedAccessoriesIfAllowed]
- -[HMMTRAttestationStatus deviceAttestationCompletedForController:opaqueDeviceHandle:attestationDeviceInfo:error:]
- -[HMMTRAttestationStatus populateDelegate:]
- -[HMMTRSoftwareUpdateProvider triggerQueryImageWithPairing:accessoryInitiated:requestParams:completionHandler:]
- -[HMMTRThreadRadioManager _connectToAccessoryWithExtendedMACAddress:forRetry:completion:]
- GCC_except_table1098
- GCC_except_table1158
- GCC_except_table1204
- GCC_except_table1212
- GCC_except_table1261
- GCC_except_table1269
- GCC_except_table1306
- GCC_except_table1343
- GCC_except_table1372
- GCC_except_table1569
- GCC_except_table1610
- GCC_except_table1762
- GCC_except_table1763
- GCC_except_table1764
- GCC_except_table1767
- GCC_except_table1787
- GCC_except_table1788
- GCC_except_table1789
- GCC_except_table1790
- GCC_except_table1791
- GCC_except_table1794
- GCC_except_table1797
- GCC_except_table1798
- GCC_except_table1799
- GCC_except_table1800
- GCC_except_table1801
- GCC_except_table1802
- GCC_except_table1803
- GCC_except_table1862
- GCC_except_table1868
- GCC_except_table1981
- GCC_except_table2093
- GCC_except_table2095
- GCC_except_table2125
- GCC_except_table2133
- GCC_except_table2135
- GCC_except_table2219
- GCC_except_table2281
- GCC_except_table2523
- GCC_except_table2527
- GCC_except_table2581
- GCC_except_table2622
- GCC_except_table2665
- GCC_except_table2667
- GCC_except_table2692
- GCC_except_table2693
- GCC_except_table2694
- GCC_except_table2716
- GCC_except_table2718
- GCC_except_table2719
- GCC_except_table2720
- GCC_except_table2721
- GCC_except_table2722
- GCC_except_table2734
- GCC_except_table2736
- GCC_except_table2755
- GCC_except_table2777
- GCC_except_table2788
- GCC_except_table2791
- GCC_except_table2795
- GCC_except_table2810
- GCC_except_table2813
- GCC_except_table2817
- GCC_except_table2819
- GCC_except_table2838
- GCC_except_table2844
- GCC_except_table2849
- GCC_except_table2913
- GCC_except_table3283
- GCC_except_table3284
- GCC_except_table3285
- GCC_except_table3289
- GCC_except_table3294
- GCC_except_table3297
- GCC_except_table3311
- GCC_except_table3327
- GCC_except_table3392
- GCC_except_table3411
- GCC_except_table3413
- GCC_except_table3420
- GCC_except_table3421
- GCC_except_table3447
- GCC_except_table3457
- GCC_except_table3484
- GCC_except_table3487
- GCC_except_table3514
- GCC_except_table3517
- GCC_except_table3553
- GCC_except_table3557
- GCC_except_table3574
- GCC_except_table3576
- GCC_except_table3594
- GCC_except_table3660
- GCC_except_table3707
- GCC_except_table3725
- GCC_except_table3748
- GCC_except_table3752
- GCC_except_table3767
- GCC_except_table3768
- GCC_except_table3769
- GCC_except_table3775
- GCC_except_table3782
- GCC_except_table3839
- GCC_except_table3859
- GCC_except_table3919
- GCC_except_table3924
- GCC_except_table3927
- GCC_except_table4009
- GCC_except_table4010
- GCC_except_table4065
- GCC_except_table4068
- GCC_except_table4130
- GCC_except_table4192
- GCC_except_table4196
- GCC_except_table4200
- GCC_except_table4203
- GCC_except_table4236
- GCC_except_table859
- GCC_except_table922
- GCC_except_table926
- GCC_except_table928
- GCC_except_table930
- GCC_except_table932
- GCC_except_table936
- GCC_except_table940
- GCC_except_table943
- GCC_except_table986
- GCC_except_table990
- GCC_except_table992
- _OBJC_CLASS_$_MTRBaseClusterNetworkCommissioning
- _OBJC_CLASS_$_MTRNetworkCommissioningClusterScanNetworksParams
- _OBJC_IVAR_$_HMMTRAccessoryServer._commissionCompletePending
- _OBJC_IVAR_$_HMMTRAccessoryServer._commissioneeNetworks
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_MTRDeviceAttestationDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_MTRDeviceAttestationDelegate
- __OBJC_$_PROTOCOL_REFS_MTRDeviceAttestationDelegate
- __OBJC_CLASS_PROTOCOLS_$_HMMTRAttestationStatus
- __OBJC_LABEL_PROTOCOL_$_MTRDeviceAttestationDelegate
- __OBJC_PROTOCOL_$_MTRDeviceAttestationDelegate
- ___101-[HMMTRAccessoryServer updateAccessoryControlToIncludeAdministratorNodes:sharedUserNodes:completion:]_block_invoke.837
- ___102-[HMMTRAccessoryServer updateAllCharacteristicValuesPostHAPServiceEnumerationForAccessory:completion:]_block_invoke.787
- ___107-[HMMTRAccessoryServerBrowser _fetchDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.212
- ___110-[HMMTRAccessoryServerBrowser removeAllDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.214
- ___111-[HMMTRSoftwareUpdateProvider triggerQueryImageWithPairing:accessoryInitiated:requestParams:completionHandler:]_block_invoke
- ___112-[HMMTRAccessoryServer _updateAdditionalCharacteristicsFromCharacteristicUpdate:service:path:completionHandler:]_block_invoke.380
- ___113-[HMMTRAttestationStatus deviceAttestationCompletedForController:opaqueDeviceHandle:attestationDeviceInfo:error:]_block_invoke
- ___113-[HMMTRAttestationStatus deviceAttestationCompletedForController:opaqueDeviceHandle:attestationDeviceInfo:error:]_block_invoke.11
- ___113-[HMMTRAttestationStatus deviceAttestationCompletedForController:opaqueDeviceHandle:attestationDeviceInfo:error:]_block_invoke.14
- ___113-[HMMTRAttestationStatus deviceAttestationCompletedForController:opaqueDeviceHandle:attestationDeviceInfo:error:]_block_invoke.15
- ___113-[HMMTRAttestationStatus deviceAttestationCompletedForController:opaqueDeviceHandle:attestationDeviceInfo:error:]_block_invoke.16
- ___113-[HMMTRAttestationStatus deviceAttestationCompletedForController:opaqueDeviceHandle:attestationDeviceInfo:error:]_block_invoke.18
- ___113-[HMMTRAttestationStatus deviceAttestationCompletedForController:opaqueDeviceHandle:attestationDeviceInfo:error:]_block_invoke.9
- ___113-[HMMTRAttestationStatus deviceAttestationCompletedForController:opaqueDeviceHandle:attestationDeviceInfo:error:]_block_invoke_2
- ___114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke.913
- ___114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke.916
- ___117-[HMMTRAccessoryServer _findSystemCommissionerPairingMatchingSetupPayload:systemCommissionerPairings:pairingManager:]_block_invoke.260
- ___117-[HMMTRAccessoryServer _findSystemCommissionerPairingMatchingSetupPayload:systemCommissionerPairings:pairingManager:]_block_invoke.261
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.504
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.505
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.506
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.507
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.508
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.509
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.511
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.513
- ___119-[HMMTRAccessoryServerBrowser removeDevicePairingFabricForSystemCommissionerDeviceWithNodeID:fabric:completionHandler:]_block_invoke.210
- ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.327
- ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.330
- ___278-[HMMTRAccessoryServerBrowser _stageAccessoryServerWithSetupPayload:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:commissioneeInfoHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke.197
- ___37-[HMMTRAccessoryServer finishPairing]_block_invoke.767
- ___37-[HMMTRAccessoryServer timerDidFire:]_block_invoke.277
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.642
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.643
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.644
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.645
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.652
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.653
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.654
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.646
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.655
- ___40-[HMMTRAccessoryServerBrowser configure]_block_invoke.141
- ___42-[HMMTRAccessoryServer _setupMatterDevice]_block_invoke.308
- ___43-[HMMTRAccessoryServer _onWiFiScanResults:]_block_invoke
- ___43-[HMMTRAccessoryServer _onWiFiScanResults:]_block_invoke_2
- ___43-[HMMTRAccessoryServer _setupThreadPairing]_block_invoke.466
- ___43-[HMMTRAccessoryServer _unpair:completion:]_block_invoke.300
- ___43-[HMMTRAccessoryServer discoverAccessories]_block_invoke.303
- ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke
- ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.887
- ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.889
- ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.890
- ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.892
- ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke_2
- ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke_2.888
- ___47-[HMMTRAccessoryServer processAttributeReport:]_block_invoke.976
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.861
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.864
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.866
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke_2.865
- ___49-[HMMTRAccessoryServerBrowser startBluetoothScan]_block_invoke.364
- ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke
- ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.819
- ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.823
- ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.824
- ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke_2
- ___51-[HMMTRAccessoryServer device:receivedEventReport:]_block_invoke.977
- ___52-[HMMTRAccessoryServer _continueNetworkProvisioning]_block_invoke
- ___52-[HMMTRAccessoryServer populateACLEntriesForPairing]_block_invoke.640
- ___52-[HMMTRAccessoryServerBrowser _cleanupStagedServers]_block_invoke.317
- ___53-[HMMTRAccessoryServer _tryPairingUsingMatterSupport]_block_invoke.254
- ___55-[HMMTRAccessoryServer device:receivedAttributeReport:]_block_invoke.975
- ___56-[HMMTRAccessoryServer controller:readCommissioneeInfo:]_block_invoke
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.424
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.425
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.426
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.427
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.428
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.436
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.437
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.438
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.440
- ___59-[HMMTRAccessoryServerBrowser _pollWedAccessoriesIfAllowed]_block_invoke
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.918
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.920
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.924
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.926
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.430
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.431
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.432
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.433
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.434
- ___62-[HMMTRAccessoryServerBrowser stopDiscoveringAccessoryServers]_block_invoke.186
- ___63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.817
- ___63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.818
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.484
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.485
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.486
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.487
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.488
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.489
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.454
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.455
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.456
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.457
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.458
- ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.939
- ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.940
- ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.941
- ___64-[HMMTRAccessoryServerBrowser _initializeAndStartBonjourBrowser]_block_invoke.149
- ___65-[HMMTRAccessoryServer stopPairingWithError:metricsReadyHandler:]_block_invoke.289
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.449
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.450
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.451
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.452
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.453
- ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.443
- ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.444
- ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.445
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.473
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.474
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.475
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.478
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.482
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.483
- ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.416
- ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.422
- ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.423
- ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.187
- ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.190
- ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.192
- ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.194
- ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke_2.193
- ___71-[HMMTRAccessoryServer validateAttestationDeviceInfo:error:completion:]_block_invoke.279
- ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.401
- ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.407
- ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.408
- ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.409
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.467
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.468
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.469
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.471
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.472
- ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.266
- ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.267
- ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.268
- ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.269
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.811
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.812
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke_2.813
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.788
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.789
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.798
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.806
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.807
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.809
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke_2.802
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.871
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.872
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.876
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke_2
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke_2.878
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.292
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.293
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.294
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.296
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.295
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.298
- ___76-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithNodeID:completion:]_block_invoke.195
- ___79-[HMMTRAccessoryServerBrowser _updateAccessoryControlListForServer:completion:]_block_invoke.322
- ___81-[HMMTRAccessoryServer _controller:commissioningComplete:nodeID:abstractMetrics:]_block_invoke
- ___82-[HMMTRAccessoryServer fetchColorControlClusterForHapAccessory:completionHandler:]_block_invoke.927
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.895
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.896
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.897
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.900
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke_2.899
- ___82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.161
- ___82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.163
- ___83-[HMMTRAccessoryServer updateAccessoryControlToRemoveAdministratorNode:completion:]_block_invoke.838
- ___84-[HMMTRAccessoryServer _queueOpenPairingWindowWithPINForDuration:completionHandler:]_block_invoke.410
- ___84-[HMMTRAccessoryServer _queueOpenPairingWindowWithPINForDuration:completionHandler:]_block_invoke.411
- ___84-[HMMTRAccessoryServer _queueOpenPairingWindowWithPINForDuration:completionHandler:]_block_invoke.412
- ___84-[HMMTRAccessoryServer _queueOpenPairingWindowWithPINForDuration:completionHandler:]_block_invoke.414
- ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.387
- ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.389
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.901
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.902
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.903
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.904
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.908
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.909
- ___86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.942
- ___86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.943
- ___88-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:keepAliveOnly:]_block_invoke.356
- ___89-[HMMTRThreadRadioManager _connectToAccessoryWithExtendedMACAddress:forRetry:completion:]_block_invoke
- ___89-[HMMTRThreadRadioManager _connectToAccessoryWithExtendedMACAddress:forRetry:completion:]_block_invoke_2
- ___89-[HMMTRThreadRadioManager _connectToAccessoryWithExtendedMACAddress:forRetry:completion:]_block_invoke_3
- ___92-[HMMTRAccessoryServer _createFirmwareUpdateServiceWithInstanceID:device:completionHandler:]_block_invoke.780
- ___92-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fabricUUID:fatalError:]_block_invoke.320
- ___94-[HMMTRAccessoryServer updateAccessoryControlToAdministratorNodes:sharedUserNodes:completion:]_block_invoke.836
- ___94-[HMMTRAccessoryServerBrowser _handleAddOrUpdateWithDiscriminator:vendorID:productID:overBLE:]_block_invoke.170
- ___97-[HMMTRAccessoryServer _getCommissioneeNetworkCommissioningClusterEndpointWithDevice:completion:]_block_invoke
- ___97-[HMMTRAccessoryServer _getCommissioneeNetworkCommissioningClusterEndpointWithDevice:completion:]_block_invoke_2
- ___97-[HMMTRAccessoryServerBrowser removeAccessoryServer:fromDiscoveredAccessoryServerListWithReason:]_block_invoke.305
- ___99-[HMMTRAccessoryServer _getCommissioneeHasActiveNetworkWithNetworkCommissioningCluster:completion:]_block_invoke
- ___99-[HMMTRAccessoryServer _tryPairingWithOnboardingPayload:systemCommissionerPairings:pairingManager:]_block_invoke.257
- ___99-[HMMTRAccessoryServer _tryPairingWithOnboardingPayload:systemCommissionerPairings:pairingManager:]_block_invoke.258
- ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.515
- ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.516
- ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.517
- ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.518
- ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke_2.519
- ___Block_byref_object_copy_.10189
- ___Block_byref_object_copy_.10952
- ___Block_byref_object_copy_.11650
- ___Block_byref_object_copy_.12349
- ___Block_byref_object_copy_.12513
- ___Block_byref_object_copy_.1810
- ___Block_byref_object_copy_.3169
- ___Block_byref_object_copy_.3457
- ___Block_byref_object_copy_.4540
- ___Block_byref_object_copy_.5708
- ___Block_byref_object_copy_.5859
- ___Block_byref_object_copy_.7675
- ___Block_byref_object_copy_.8108
- ___Block_byref_object_copy_.9232
- ___Block_byref_object_dispose_.10190
- ___Block_byref_object_dispose_.10953
- ___Block_byref_object_dispose_.11651
- ___Block_byref_object_dispose_.12350
- ___Block_byref_object_dispose_.12514
- ___Block_byref_object_dispose_.1811
- ___Block_byref_object_dispose_.3170
- ___Block_byref_object_dispose_.3458
- ___Block_byref_object_dispose_.4541
- ___Block_byref_object_dispose_.5709
- ___Block_byref_object_dispose_.5860
- ___Block_byref_object_dispose_.7676
- ___Block_byref_object_dispose_.8109
- ___Block_byref_object_dispose_.9233
- ___block_descriptor_40_e8_32bs_e78_v24?0"MTRNetworkCommissioningClusterScanNetworksResponseParams"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32s_e114_v32?0"MTRNetworkCommissioningClusterScanNetworksResponseParams"8"NSError"16"HMMTRAccessoryPairingEndContext"24ls32l8
- ___block_descriptor_40_e8_32s_e35_v16?0"MTSWiFiNetworkAssociation"8ls32l8
- ___block_descriptor_40_e8_32s_e37_v16?0"MTSThreadNetworkAssociation"8ls32l8
- ___block_descriptor_48_e8_32s40s_e84_v32?0"MTRCommissioningParameters"8"NSError"16"HMMTRAccessoryPairingEndContext"24ls32l8s40l8
- ___block_descriptor_56_e8_32s40s_e45_v28?0"HMMTRAccessoryServer"8B16"NSError"20ls32l8s40l8
- ___block_descriptor_57_e8_32s40bs48bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s56l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0ls32l8s40l8r56l8s48l8
- ___block_descriptor_65_e8_32s40s48s56bs_e30_v24?0"NSNumber"8"NSError"16ls32l8s56l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48bs56r64w_e30_v24?0"NSNumber"8"NSError"16lw64l8r56l8s48l8s32l8s40l8
- ___block_descriptor_72_e8_32s40s48r56r64w_e35_v24?0"THCredentials"8"NSError"16lw64l8s32l8r48l8r56l8s40l8
- ___block_descriptor_72_e8_32s40s48r56r64w_e5_v8?0lw64l8r48l8s32l8r56l8s40l8
- ___block_descriptor_72_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_80_e8_32s40s48s56s64r72r_e5_v8?0ls32l8s40l8s48l8r64l8r72l8s56l8
- ___block_descriptor_81_e8_32s40s48s56s64bs72w_e20_v20?0B8"NSError"12ls32l8s40l8w72l8s64l8s48l8s56l8
- ___block_literal_global.10060
- ___block_literal_global.10655
- ___block_literal_global.11244
- ___block_literal_global.11469
- ___block_literal_global.11684
- ___block_literal_global.11820
- ___block_literal_global.11951
- ___block_literal_global.12169
- ___block_literal_global.1443
- ___block_literal_global.1659
- ___block_literal_global.1933
- ___block_literal_global.1987
- ___block_literal_global.2033
- ___block_literal_global.2120
- ___block_literal_global.2480
- ___block_literal_global.2628
- ___block_literal_global.2930
- ___block_literal_global.3074
- ___block_literal_global.3103
- ___block_literal_global.311
- ___block_literal_global.314
- ___block_literal_global.3195
- ___block_literal_global.3349
- ___block_literal_global.353.9096
- ___block_literal_global.3546
- ___block_literal_global.3697
- ___block_literal_global.372
- ___block_literal_global.3821
- ___block_literal_global.4308
- ___block_literal_global.4637
- ___block_literal_global.4925
- ___block_literal_global.5059
- ___block_literal_global.5160
- ___block_literal_global.522
- ___block_literal_global.5424
- ___block_literal_global.5597
- ___block_literal_global.5843
- ___block_literal_global.6031
- ___block_literal_global.6171
- ___block_literal_global.6280
- ___block_literal_global.6314
- ___block_literal_global.6335
- ___block_literal_global.6585
- ___block_literal_global.6598
- ___block_literal_global.6692
- ___block_literal_global.6786
- ___block_literal_global.6880
- ___block_literal_global.6983
- ___block_literal_global.7077
- ___block_literal_global.7216
- ___block_literal_global.7357
- ___block_literal_global.7463
- ___block_literal_global.7541
- ___block_literal_global.785
- ___block_literal_global.7891
- ___block_literal_global.792
- ___block_literal_global.801
- ___block_literal_global.8119
- ___block_literal_global.82.9985
- ___block_literal_global.8451
- ___block_literal_global.8576
- ___block_literal_global.8710
- ___block_literal_global.9264
- ___block_literal_global.9662
- ___block_literal_global.984
- ___block_literal_global.9984
- _logCategory._hmf_once_t0.3073
- _logCategory._hmf_once_t0.5596
- _logCategory._hmf_once_t0.6313
- _logCategory._hmf_once_t10.12168
- _logCategory._hmf_once_t13.3194
- _logCategory._hmf_once_t13.3545
- _logCategory._hmf_once_t14.6597
- _logCategory._hmf_once_t14.6691
- _logCategory._hmf_once_t14.6785
- _logCategory._hmf_once_t14.6982
- _logCategory._hmf_once_t14.7076
- _logCategory._hmf_once_t14.7215
- _logCategory._hmf_once_t2.10059
- _logCategory._hmf_once_t2.5159
- _logCategory._hmf_once_t2.6279
- _logCategory._hmf_once_t2.7356
- _logCategory._hmf_once_t20.11819
- _logCategory._hmf_once_t26.6879
- _logCategory._hmf_once_t3.1442
- _logCategory._hmf_once_t31.11950
- _logCategory._hmf_once_t4.3696
- _logCategory._hmf_once_t4.7462
- _logCategory._hmf_once_t40.5905
- _logCategory._hmf_once_t6.2119
- _logCategory._hmf_once_t68.12373
- _logCategory._hmf_once_t688
- _logCategory._hmf_once_t8.11468
- _logCategory._hmf_once_t8.8575
- _logCategory._hmf_once_v1.3075
- _logCategory._hmf_once_v1.5598
- _logCategory._hmf_once_v1.6315
- _logCategory._hmf_once_v11.12170
- _logCategory._hmf_once_v14.3196
- _logCategory._hmf_once_v14.3547
- _logCategory._hmf_once_v15.6599
- _logCategory._hmf_once_v15.6693
- _logCategory._hmf_once_v15.6787
- _logCategory._hmf_once_v15.6984
- _logCategory._hmf_once_v15.7078
- _logCategory._hmf_once_v15.7217
- _logCategory._hmf_once_v21.11821
- _logCategory._hmf_once_v27.6881
- _logCategory._hmf_once_v3.10061
- _logCategory._hmf_once_v3.5161
- _logCategory._hmf_once_v3.6281
- _logCategory._hmf_once_v3.7358
- _logCategory._hmf_once_v32.11952
- _logCategory._hmf_once_v4.1444
- _logCategory._hmf_once_v41.5906
- _logCategory._hmf_once_v5.3698
- _logCategory._hmf_once_v5.7464
- _logCategory._hmf_once_v689
- _logCategory._hmf_once_v69.12374
- _logCategory._hmf_once_v7.2121
- _logCategory._hmf_once_v9.11470
- _logCategory._hmf_once_v9.8577
- _objc_msgSend$_collectNetworkCredentials:
- _objc_msgSend$_commissionWithParams:
- _objc_msgSend$_connectToAccessoryWithExtendedMACAddress:forRetry:completion:
- _objc_msgSend$_continueNetworkProvisioning
- _objc_msgSend$_controller:commissioningAndPairedNodeRecoveryComplete:nodeID:abstractMetrics:
- _objc_msgSend$_controller:commissioningComplete:nodeID:abstractMetrics:
- _objc_msgSend$_fetchAdditionalThreadNetworkInformationWithCompletion:
- _objc_msgSend$_getCommissioneeHasActiveNetworkWithNetworkCommissioningCluster:completion:
- _objc_msgSend$_getCommissioneeNetworkCommissioningClusterEndpointWithDevice:completion:
- _objc_msgSend$_onNetworkScanResults:
- _objc_msgSend$_onThreadScanResults:
- _objc_msgSend$_onWiFiScanResults:
- _objc_msgSend$_pollWedAccessoriesIfAllowed
- _objc_msgSend$_requestAccessoryNetworkScanWithCompletionHandler:
- _objc_msgSend$allFabricIDs
- _objc_msgSend$commissionCompletePending
- _objc_msgSend$commissionDevice:commissioningParams:error:
- _objc_msgSend$commissioneeNetworkCommissioningClusterEndpoint
- _objc_msgSend$commissioneeNetworks
- _objc_msgSend$continueCommissioningDevice:ignoreAttestationFailure:error:
- _objc_msgSend$endpointForClusterID:device:partsList:callbackQueue:completionHandler:
- _objc_msgSend$getDeviceBeingCommissioned:error:
- _objc_msgSend$populateDelegate:
- _objc_msgSend$queryImageWithPairing:requestParams:queue:accessoryInitiated:completionHandler:
- _objc_msgSend$readAttributeNetworksWithCompletion:
- _objc_msgSend$readAttributeScanMaxTimeSecondsWithCompletionHandler:
- _objc_msgSend$scanNetworksWithParams:completionHandler:
- _objc_msgSend$sessionTransportType
- _objc_msgSend$setCommissionCompletePending:
- _objc_msgSend$setCommissioneeNetworkCommissioningClusterEndpoint:
- _objc_msgSend$setCommissioneeNetworks:
- _objc_msgSend$setDeviceAttestationDelegate:
- _objc_msgSend$setServerSideProcessingTimeout:
- _objc_msgSend$stopDevicePairing:error:
- _objc_msgSend$threadScanResults
- _objc_msgSend$triggerQueryImageWithPairing:accessoryInitiated:requestParams:completionHandler:
- _protocolMap.onceToken
CStrings:
+ "%{public}@Attempt to disarm failsafe resulted in: %@, %@"
+ "%{public}@Cleaning up Matter software update busy timer for nodeID: %@ during accessory server dealloc"
+ "%{public}@Concatenated QR codes are not enabled.  Failing pairing for %@ without trying with MatterSupport"
+ "%{public}@Concatenated QR codes are not enabled: %@"
+ "%{public}@Could not shut down existing PASE session so we can do a new commissioning.  Failing the pairing"
+ "%{public}@Determining Thread credentials for accessory."
+ "%{public}@Determining WiFi credentials for accessory."
+ "%{public}@Device attestation failed and the error should not be ignored"
+ "%{public}@Falling back to pairing directly, not via MatterSupport, for concatenated QR code"
+ "%{public}@Ignoring timer callback for stopped/replaced timer for accessory server [%@]"
+ "%{public}@Invalid Network Commissioning feature map value: %@"
+ "%{public}@Invalid WED support value: %@"
+ "%{public}@Query image request initiated by: %@"
+ "%{public}@Reset query image busy response counter to 0"
+ "%{public}@Scheduling WED polling in %.1f seconds (attempt %lu)"
+ "%{public}@Software update became BUSY for accessory server [%@] after busy timer expired, retrying with backOff delay"
+ "%{public}@Software update became NotAvailable for accessory server [%@] after busy timer expired, No Need to Send NotAvailable Response"
+ "%{public}@Software update became available after busy timer expired, announcing OTA provider to initiate update for accessory server = [%@]"
+ "%{public}@Start queryimage busy response timeout for accessory server [%@]"
+ "%{public}@Starting WED polling timer"
+ "%{public}@Starting busy timer for nodeID: %@ with %0.2f second delay"
+ "%{public}@Stop queryimage busy response timeout for accessory server [%@]"
+ "%{public}@Stopping WED polling timer"
+ "%{public}@Stopping busy timer for nodeID: %@"
+ "%{public}@Thread credential management endpoint not found for commissionee %@ with primary device type %@"
+ "%{public}@Thread credential management is supported for commissionee %@, auto-enable = %@"
+ "%{public}@Thread scan failed: %@"
+ "%{public}@Unhandled software update status: %@ for accessory server [%@]"
+ "%{public}@Updating delay with exponential backoff to %.0f seconds busyImageResponseCounter = %lu"
+ "%{public}@WED polling already active, rescheduling next attempt"
+ "%{public}@WED polling attempt cancelled"
+ "%{public}@WED polling exceeded maximum attempts (%lu), stopping"
+ "%{public}@WED polling not active, not scheduling"
+ "%{public}@WED polling not allowed, not scheduling"
+ "%{public}@WED polling timer fired"
+ "%{public}@Wi-Fi scan failed: %@"
+ "%{public}@queryimage busy response timer expired for accessory server [%@]"
+ "%{public}@stopPairing will not wait for metrics submission because there was no commissioning to stop, so we will not get a callback with metrics."
+ "*"
+ "@\"HMMTRQueryImageResponseBusyTimer\""
+ "@\"HMMTRSoftwareUpdateProviderQueryImageRequestParams\""
+ "@\"HMMTRWEDPollingTimer\""
+ "@\"MTRCommissioningOperation\""
+ "@64@0:8@16@24d32@40@48@56"
+ "AccessoryInitiated"
+ "HMMTRQueryImageResponseBusyTimer"
+ "HMMTRWEDPollingTimer"
+ "InternalBusyTimer"
+ "InternalRebootPair"
+ "MTRCommissioningDelegate"
+ "MatterConcatenatedQRCodes"
+ "T@\"HMFTimer\",&,N,V_pollingTimer"
+ "T@\"HMFTimer\",&,V_updateTimer"
+ "T@\"HMMTRAccessoryServer\",W,V_server"
+ "T@\"HMMTRQueryImageResponseBusyTimer\",&,N,V_busyImageResponseTimer"
+ "T@\"HMMTRSoftwareUpdateProvider\",W,V_softwareUpdateProvider"
+ "T@\"HMMTRSoftwareUpdateProviderQueryImageRequestParams\",&,V_requestParams"
+ "T@\"HMMTRWEDPollingTimer\",&,N,V_wedPollingTimer"
+ "T@\"MTRCommissioningOperation\",&,N,V_currentCommissioning"
+ "T@\"NSMutableDictionary\",&,V_vendorsByVendorID"
+ "TB,N,V_dispatchedNetworkScanEnd"
+ "TB,N,V_pollingActive"
+ "TQ,N,V_attemptCount"
+ "Unknown(%lu)"
+ "_attemptCount"
+ "_busyImageResponseTimer"
+ "_cleanupMatterSoftwareUpdateBusyTimer"
+ "_collectThreadNetworkCredentials:completion:"
+ "_collectWiFiNetworkCredentials:completion:"
+ "_commissioning:complete:abstractMetrics:"
+ "_commissioningAndPairedNodeRecoveryComplete:abstractMetrics:"
+ "_computeSetupPayloadString"
+ "_connectToAccessoryWithExtendedMACAddress:asRetry:completion:"
+ "_createCommissioningOperationWithParameters:setupPayload:"
+ "_currentCommissioning"
+ "_dispatchedNetworkScanEnd"
+ "_initializeCredentialManagementForCommissioneeNodeID:storage:"
+ "_isWedPollingAllowed"
+ "_onThreadScanResults:commissioning:completion:"
+ "_onWiFiScanResults:completion:"
+ "_parametersForNewCommissioning"
+ "_pollWedAccessories"
+ "_pollingActive"
+ "_pollingTimer"
+ "_requestParams"
+ "_scheduleNextPolling"
+ "_startNewCommissioningWithPayload:"
+ "_syncAbortStagingWithError:context:"
+ "_threadScanRequired"
+ "_wedPollingTimer"
+ "_wifiScanRequired"
+ "accessoryServer:completedDeviceAttestation:error:completion:"
+ "attemptCount"
+ "attributes"
+ "busyImageResponseTimer"
+ "cancelCommissioningForNodeID:error:"
+ "commissioning:completedDeviceAttestation:error:completion:"
+ "commissioning:failedWithError:metrics:"
+ "commissioning:needsThreadCredentialsWithScanResults:error:completion:"
+ "commissioning:needsWiFiCredentialsWithScanResults:error:completion:"
+ "commissioning:readCommissioneeInfo:"
+ "commissioning:succeededForNodeID:metrics:"
+ "commissioningProvisionedNetworkCredentials:"
+ "commissioningStartingNetworkScan:"
+ "currentCommissioning"
+ "disableFeatureMatterHRAPDeviceTypesForTests"
+ "dispatchedNetworkScanEnd"
+ "enableFeatureMatterHRAPDeviceTypesForTests"
+ "hasBusyImageResponseTimer"
+ "hmmtr.queryImage.busyResponse.timer"
+ "hmmtr.wed.polling.timer"
+ "initWithBrowser:queue:"
+ "initWithParameters:setupPayload:delegate:queue:"
+ "initWithServer:softwareUpdateProvider:timeInterval:endpoint:requestParams:queue:"
+ "pollingActive"
+ "pollingTimer"
+ "populateAttestationParameters:"
+ "qrCodeString"
+ "queryImageWithPairing:requestParams:queue:initiationType:completionHandler:"
+ "requestParams"
+ "resetBusyImageResponseCounter"
+ "resetCachedProtocolMapForTesting"
+ "setAttemptCount:"
+ "setBusyImageResponseTimer:"
+ "setCurrentCommissioning:"
+ "setDispatchedNetworkScanEnd:"
+ "setExtraAttributesToRead:"
+ "setForceThreadScan:"
+ "setForceWiFiScan:"
+ "setPollingActive:"
+ "setPollingTimer:"
+ "setRequestParams:"
+ "setSoftwareUpdateProvider:"
+ "setWedPollingTimer:"
+ "shouldRetryPairingWithCommissioningSessionEstablishmentError:"
+ "startBusyImageResponseTimer:timeInterval:endpoint:requestParams:queue:"
+ "startPolling"
+ "startWithController:"
+ "stopBusyImageResponseTimer"
+ "stopPolling"
+ "threadCredentialManagementImplicitlyEnabledForDeviceType:"
+ "triggerQueryImageWithPairing:initiationType:requestParams:completionHandler:"
+ "unsetFeatureMatterHRAPDeviceTypesForTests"
+ "v24@0:8@\"MTRCommissioningOperation\"16"
+ "v32@0:8@\"MTRCommissioningOperation\"16@\"MTRCommissioneeInfo\"24"
+ "v40@0:8@\"MTRCommissioningOperation\"16@\"NSError\"24@\"MTRMetrics\"32"
+ "v40@0:8@\"MTRCommissioningOperation\"16@\"NSNumber\"24@\"MTRMetrics\"32"
+ "v48@0:8@\"MTRCommissioningOperation\"16@\"MTRDeviceAttestationDeviceInfo\"24@\"NSError\"32@?<v@?>40"
+ "v48@0:8@\"MTRCommissioningOperation\"16@\"NSArray\"24@\"NSError\"32@?<v@?@\"NSData\">40"
+ "v48@0:8@\"MTRCommissioningOperation\"16@\"NSArray\"24@\"NSError\"32@?<v@?@\"NSData\"@\"NSData\">40"
+ "v48@0:8@16Q24@32@?40"
+ "v56@0:8@16d24@32@40@48"
+ "wedPollingTimer"
+ "wifiCredentials"
+ "wifiSSID"
+ "\xf0\x92\xf0\xf0\xf1\xc1"
- "%{public}@Accessory NetworkCommissioning cluster feature map has unsupported value: %@"
- "%{public}@CHIP Accessory failed to stop Pairing with Error: %@"
- "%{public}@CHIP Accessory pairing failed before network provisioning: %@"
- "%{public}@CHIP Accessory ready for network provisioning"
- "%{public}@Checking what network technology is supported for the accessory."
- "%{public}@Commissionee already has a commissioned network. Skip network scanning."
- "%{public}@Commissionee over BLE: %@, has active network: %@"
- "%{public}@Commissionee was already network commissioned. Skip network commissioning parameters."
- "%{public}@Commissioning failed: %@"
- "%{public}@Continue commissioning device failed: %@"
- "%{public}@Couldn't get device being commissioned for network scanning: %@"
- "%{public}@Couldn't get network commissioning cluster features for scanning: %@"
- "%{public}@Couldn't get scan max time from device: %@"
- "%{public}@Error setup commissioning session %@, context %@"
- "%{public}@Failed to check supported network technologies for server, but commissionee was already network commissioned. Ignoring error and continuing with pairing. Error: %@"
- "%{public}@Failed to check supported network technologies for server. Error: %@..."
- "%{public}@Failed to fetch additional Thread network information - aborting pairing: %@"
- "%{public}@Failed to query endpoints for network commissioning cluster : %@"
- "%{public}@Failed to read networks attribute from commissionee: %@"
- "%{public}@Found network commissioning cluster at endpoint: %@"
- "%{public}@Ignoring unexpected call to pairing complete"
- "%{public}@Neither WiFi nor Thread scan results present in scan response"
- "%{public}@Network commissioning cluster feature (featureMap: %@) doesn't require scanning for current request. Returning empty scan results."
- "%{public}@Network commissioning cluster init failed for scanning"
- "%{public}@Network commissioning cluster not found for scanning: %@. Returning empty scan results."
- "%{public}@Network commissioning cluster not found. Proceeding with on-network commissioning"
- "%{public}@Network scanning was not requested by upper layer. Returning empty scan results for %s."
- "%{public}@No Matter device controller available to commission"
- "%{public}@Requesting to commission device(%@)."
- "%{public}@Scanned networks: %@"
- "%{public}@Sending scan network command with timeout: %@"
- "%{public}@Setting linkLayerType to Thread"
- "%{public}@Setting linkLayerType to WiFi"
- "%{public}@Updating delay with exponential backoff to %.0f seconds"
- "%{public}@not reading thread network prerequisites"
- "%{public}@stopPairing will not wait for metrics submission because commissioning complete callback is not guaranteed"
- "%{public}@triggerQueryImageWithPairing method is called and accessoryInitiated is %d"
- "MTRDeviceAttestationDelegate"
- "T@\"NSArray\",&,N,V_commissioneeNetworks"
- "T@\"NSDictionary\",C,V_vendorsByVendorID"
- "TB,N,V_commissionCompletePending"
- "WiFi"
- "_collectNetworkCredentials:"
- "_commissionCompletePending"
- "_commissionWithParams:"
- "_commissioneeNetworks"
- "_connectToAccessoryWithExtendedMACAddress:forRetry:completion:"
- "_continueNetworkProvisioning"
- "_controller:commissioningAndPairedNodeRecoveryComplete:nodeID:abstractMetrics:"
- "_controller:commissioningComplete:nodeID:abstractMetrics:"
- "_fetchAdditionalThreadNetworkInformationWithCompletion:"
- "_getCommissioneeHasActiveNetworkWithNetworkCommissioningCluster:completion:"
- "_getCommissioneeNetworkCommissioningClusterEndpointWithDevice:completion:"
- "_getRandomFabricId"
- "_onNetworkScanResults:"
- "_onThreadScanResults:"
- "_onWiFiScanResults:"
- "_pollWedAccessoriesIfAllowed"
- "_requestAccessoryNetworkScanWithCompletionHandler:"
- "allFabricIDs"
- "commissionCompletePending"
- "commissionDevice:commissioningParams:error:"
- "commissioneeNetworks"
- "continueCommissioningDevice:ignoreAttestationFailure:error:"
- "deviceAttestation:completedForDevice:attestationDeviceInfo:error:"
- "deviceAttestation:failedForDevice:error:"
- "deviceAttestationCompletedForController:opaqueDeviceHandle:attestationDeviceInfo:error:"
- "deviceAttestationFailedForController:opaqueDeviceHandle:error:"
- "getDeviceBeingCommissioned:error:"
- "populateDelegate:"
- "queryImageWithPairing:requestParams:queue:accessoryInitiated:completionHandler:"
- "readAttributeNetworksWithCompletion:"
- "readAttributeScanMaxTimeSecondsWithCompletionHandler:"
- "scanNetworksWithParams:completionHandler:"
- "scanResponse.threadScanResults"
- "sessionTransportType"
- "setCommissionCompletePending:"
- "setCommissioneeNetworks:"
- "setDeviceAttestationDelegate:"
- "setServerSideProcessingTimeout:"
- "stopDevicePairing:error:"
- "threadScanResults"
- "triggerQueryImageWithPairing:accessoryInitiated:requestParams:completionHandler:"
- "v24@?0@\"MTRNetworkCommissioningClusterScanNetworksResponseParams\"8@\"NSError\"16"
- "v32@?0@\"MTRNetworkCommissioningClusterScanNetworksResponseParams\"8@\"NSError\"16@\"HMMTRAccessoryPairingEndContext\"24"
- "v40@0:8@\"MTRDeviceController\"16^v24@\"NSError\"32"
- "v40@0:8@16^v24@32"
- "v48@0:8@\"MTRDeviceController\"16^v24@\"MTRDeviceAttestationDeviceInfo\"32@\"NSError\"40"
- "v48@0:8@16^v24@32@40"
- "\xf0\x82\xf0\xf0\xf1\xc1"

```
