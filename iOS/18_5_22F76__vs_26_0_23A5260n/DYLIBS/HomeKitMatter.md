## HomeKitMatter

> `/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter`

```diff

-1278.6.31.1.1
-  __TEXT.__text: 0x133d90
+1323.0.6.0.1
+  __TEXT.__text: 0x13699c
   __TEXT.__auth_stubs: 0xa40
-  __TEXT.__objc_methlist: 0x9ccc
-  __TEXT.__const: 0x158
+  __TEXT.__objc_methlist: 0x9e6c
+  __TEXT.__const: 0x168
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__gcc_except_tab: 0x2b5c
-  __TEXT.__cstring: 0x6014
-  __TEXT.__oslogstring: 0x25e34
+  __TEXT.__gcc_except_tab: 0x2b10
+  __TEXT.__cstring: 0x6287
+  __TEXT.__oslogstring: 0x2665c
   __TEXT.__ustring: 0x68
-  __TEXT.__unwind_info: 0x2cc8
-  __TEXT.__objc_classname: 0x133b
-  __TEXT.__objc_methname: 0x23e0d
-  __TEXT.__objc_methtype: 0x3859
-  __TEXT.__objc_stubs: 0x15820
-  __DATA_CONST.__got: 0x998
-  __DATA_CONST.__const: 0x4530
-  __DATA_CONST.__objc_classlist: 0x3e8
+  __TEXT.__unwind_info: 0x2d28
+  __TEXT.__objc_classname: 0x137b
+  __TEXT.__objc_methname: 0x245b0
+  __TEXT.__objc_methtype: 0x394c
+  __TEXT.__objc_stubs: 0x159e0
+  __DATA_CONST.__got: 0x9a0
+  __DATA_CONST.__const: 0x4580
+  __DATA_CONST.__objc_classlist: 0x3f8
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x67a8
+  __DATA_CONST.__objc_selrefs: 0x68c0
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x2c8
+  __DATA_CONST.__objc_superrefs: 0x2d0
   __DATA_CONST.__objc_arraydata: 0x228
   __AUTH_CONST.__auth_got: 0x530
-  __AUTH_CONST.__const: 0xec0
-  __AUTH_CONST.__cfstring: 0x6440
-  __AUTH_CONST.__objc_const: 0xe9c0
-  __AUTH_CONST.__objc_intobj: 0x15d8
+  __AUTH_CONST.__const: 0xf40
+  __AUTH_CONST.__cfstring: 0x6580
+  __AUTH_CONST.__objc_const: 0xec68
+  __AUTH_CONST.__objc_intobj: 0x1638
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x1db0
-  __DATA.__objc_ivar: 0xa50
+  __AUTH.__objc_data: 0x1c70
+  __DATA.__objc_ivar: 0xa5c
   __DATA.__data: 0xd80
-  __DATA.__bss: 0x408
-  __DATA_DIRTY.__objc_data: 0x960
-  __DATA_DIRTY.__bss: 0x90
+  __DATA.__bss: 0x418
+  __DATA_DIRTY.__objc_data: 0xb40
+  __DATA_DIRTY.__bss: 0xb0
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AF3E330C-826C-3E5E-824A-95211C3E3FA8
-  Functions: 4085
-  Symbols:   14111
-  CStrings:  9023
+  UUID: B6A42461-DCF0-3E66-A454-8B9E371FA47F
+  Functions: 4114
+  Symbols:   14218
+  CStrings:  9113
 
Symbols:
+ +[HMMTRAccessoryServer _convertPairingFailureError:]
+ +[HMMTRCommissioningSessionHandler logCategory]
+ +[HMMTRProtocolMap mapSensorFaultToStatusActive:]
+ +[HMMTRStorageEventDispatcher logCategory]
+ +[HMMTRStorageEventDispatcher shortDescription]
+ +[HMMTRSyncClusterSmokeCOAlarm logCategory]
+ -[HMMTRAccessoryServer _controller:commissioningAndPairedNodeRecoveryComplete:nodeID:abstractMetrics:]
+ -[HMMTRAccessoryServer _isAllowedForRawEventDictionaryHandling:]
+ -[HMMTRAccessoryServer _setupPayloadForLastCommissioning]
+ -[HMMTRAccessoryServer _setupThreadPairing]
+ -[HMMTRAccessoryServer controller:commissioneeHasReceivedNetworkCredentials:]
+ -[HMMTRAccessoryServer controller:readCommissioneeInfo:]
+ -[HMMTRAccessoryServer handleAttestationComplete]
+ -[HMMTRAccessoryServer handleCommissioneeHasReceivedNetworkCredentials]
+ -[HMMTRAccessoryServer readSpecificationVersionWithCompletionHandler:]
+ -[HMMTRAccessoryServer setSetupPayloadForPairingUsingMatterSupport:]
+ -[HMMTRAccessoryServer setStageCommissioneeInfoHandler:]
+ -[HMMTRAccessoryServer setupPayloadForPairingUsingMatterSupport]
+ -[HMMTRAccessoryServer stageCommissioneeInfoHandler]
+ -[HMMTRAccessoryServer startStagedPairingWithDeviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:commissioneeInfoHandler:scanningNetworks:completion:]
+ -[HMMTRAccessoryServerBrowser _addDiscoveredAccessoryServerWithNodeID:fabricUUID:]
+ -[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fabricUUID:fatalError:]
+ -[HMMTRAccessoryServerBrowser _createSystemCommissionerCHIPAccessoryForNodeID:]
+ -[HMMTRAccessoryServerBrowser _deleteOldPairingsForFabricUUID:]
+ -[HMMTRAccessoryServerBrowser _isDevicePaired:fabricUUID:]
+ -[HMMTRAccessoryServerBrowser _setUpBrowserTargetFabricIfNotFabricUUID:rediscoverAccessories:]
+ -[HMMTRAccessoryServerBrowser _setUpBrowserTargetFabricUUID:]
+ -[HMMTRAccessoryServerBrowser _setUpUpdatedBrowserTargetFabricUUID:]
+ -[HMMTRAccessoryServerBrowser _setUpUpdatedBrowserTargetFabricUUID:rediscoverAccessories:]
+ -[HMMTRAccessoryServerBrowser _setUpUpdatedBrowserTargetFabricUUID:rediscoverAccessories:overrideAccessoryControlAllowed:]
+ -[HMMTRAccessoryServerBrowser _stageAccessoryServerWithSetupPayload:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:commissioneeInfoHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:]
+ -[HMMTRAccessoryServerBrowser _startDiscoveringAccessoryServersWithNoResponseToDelegate]
+ -[HMMTRAccessoryServerBrowser _updateDiscoveredAccessoryServersWithNodes:fabricUUID:]
+ -[HMMTRAccessoryServerBrowser controllerWrapperForFabricUUID:]
+ -[HMMTRAccessoryServerBrowser deviceControllerForFabricUUID:]
+ -[HMMTRAccessoryServerBrowser discoveringAccessoryServersRequested]
+ -[HMMTRAccessoryServerBrowser handleHomeAddedAccessoryWithNodeID:fabricUUID:localControl:]
+ -[HMMTRAccessoryServerBrowser handleHomeDeletionWithFabricUUID:]
+ -[HMMTRAccessoryServerBrowser isCurrentDeviceAllowedAccessoryControlDespiteReachableResidentForFabricUUID:]
+ -[HMMTRAccessoryServerBrowser notifyDiscoveredAccessoryServer:]
+ -[HMMTRAccessoryServerBrowser setDiscoveringAccessoryServersRequested:]
+ -[HMMTRAccessoryServerBrowser setOperationalFabricData:operationalCertIssuer:storageDataSource:allTargetFabricUUIDs:entityIdentifier:accessoryServerNodeIDs:forTargetFabricUUID:]
+ -[HMMTRAccessoryServerBrowser setUpBrowserTargetFabricAndRediscoverAccessoriesForHomeFabricUUID:]
+ -[HMMTRAccessoryServerBrowser setUpBrowserTargetFabricUUID:]
+ -[HMMTRAccessoryServerBrowser setUpBrowserTargetFabricUUID:completion:]
+ -[HMMTRAccessoryServerBrowser setUpBrowserTargetFabricWithoutRediscoveringAccessoriesForHomeFabricUUID:]
+ -[HMMTRAccessoryServerBrowser stageAccessoryServerWithSetupPayload:fabricID:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:commissioneeInfoHandler:scanningNetworks:completionHandler:]
+ -[HMMTRAccessoryServerBrowser startDiscoveringAccessoryServersWithNoResponseToDelegate]
+ -[HMMTRAccessoryServerBrowser storageForFabricUUID:sharedAdmin:]
+ -[HMMTRAccessoryServerBrowser storageForSystemCommissioner]
+ -[HMMTRAccessoryServerBrowser updateDiscoveredAccessoryServersWithNodes:fabricUUID:]
+ -[HMMTRCommissioningSessionHandler .cxx_destruct]
+ -[HMMTRCommissioningSessionHandler allPairedNodeIDs]
+ -[HMMTRCommissioningSessionHandler clientQueue]
+ -[HMMTRCommissioningSessionHandler completionHandler]
+ -[HMMTRCommissioningSessionHandler controller:commissioningSessionEstablishmentDone:]
+ -[HMMTRCommissioningSessionHandler controllerParametersToRemove]
+ -[HMMTRCommissioningSessionHandler establishSessionToRemoveFabricWithDeviceController:forControllerParameters:setupPayload:nodeID:allPairedNodeIDs:completion:]
+ -[HMMTRCommissioningSessionHandler initWithClientQueue:]
+ -[HMMTRCommissioningSessionHandler logIdentifier]
+ -[HMMTRCommissioningSessionHandler nodeID]
+ -[HMMTRCommissioningSessionHandler readFabricsFromDeviceBeingCommissionedWithController:completion:]
+ -[HMMTRCommissioningSessionHandler removeFabricFromDeviceBeingCommissionedWithController:fabricIndex:completion:]
+ -[HMMTRCommissioningSessionHandler setAllPairedNodeIDs:]
+ -[HMMTRCommissioningSessionHandler setCompletionHandler:]
+ -[HMMTRCommissioningSessionHandler setControllerParametersToRemove:]
+ -[HMMTRCommissioningSessionHandler setNodeID:]
+ -[HMMTRCommissioningSessionHandler setUpCommissioningSessionWithDeviceController:payload:newNodeID:error:]
+ -[HMMTRFabricData fabricID]
+ -[HMMTRFabricData initWithRootPublicKey:fabricID:ipk:residentNodeID:rootKeyPair:rootCert:residentOperationalKeyPair:residentOperationalCert:]
+ -[HMMTRFabricData residentOperationalCert]
+ -[HMMTRFabricData residentOperationalKeyPair]
+ -[HMMTRFabricData rootKeyPair]
+ -[HMMTRFabricData rootPublicKey]
+ -[HMMTRStorage clearStaleItems]
+ -[HMMTRStorage initWithQueue:dataSource:systemCommissionerFabric:fabricUUID:sharedAdmin:]
+ -[HMMTRStorageEventDispatcher .cxx_destruct]
+ -[HMMTRStorageEventDispatcher _handleUpdatedDataWithIsLocalChange:]
+ -[HMMTRStorageEventDispatcher caseAuthenticatedTagsUpdated]
+ -[HMMTRStorageEventDispatcher dataSource]
+ -[HMMTRStorageEventDispatcher delegate]
+ -[HMMTRStorageEventDispatcher fabricDataSource]
+ -[HMMTRStorageEventDispatcher fabricID]
+ -[HMMTRStorageEventDispatcher fabricUUID]
+ -[HMMTRStorageEventDispatcher handlePrimaryResidentDataReady]
+ -[HMMTRStorageEventDispatcher handleUpdatedCurrentFabricIndex]
+ -[HMMTRStorageEventDispatcher handleUpdatedDataForFabricIndex:isLocalChange:]
+ -[HMMTRStorageEventDispatcher handleUpdatedDataForFabricIndex:nodeID:isLocalChange:]
+ -[HMMTRStorageEventDispatcher handleUpdatedDataWithIsLocalChange:]
+ -[HMMTRStorageEventDispatcher initWithQueue:]
+ -[HMMTRStorageEventDispatcher logIdentifier]
+ -[HMMTRStorageEventDispatcher setCaseAuthenticatedTagsUpdated:]
+ -[HMMTRStorageEventDispatcher setDataSource:]
+ -[HMMTRStorageEventDispatcher setDelegate:]
+ -[HMMTRStorageEventDispatcher setFabricDataSource:]
+ -[HMMTRStorageEventDispatcher workQueue]
+ -[HMMTRSyncClusterSmokeCOAlarm readAttributePluginStatusActiveWithParams:]
+ -[HMMTRSyncClusterSmokeCOAlarm updatedValuePluginStatusActiveForAttributeReport:responseHandler:]
+ -[HMMTRThreadRadioManager _connectToAccessoryWithExtendedMACAddress:forRetry:completion:]
+ -[HMMTRThreadRadioManager connectToWEDAccessory:completion:]
+ -[HMMTRThreadRadioManager disconnectFromWEDAccessory:completion:]
+ -[HMMTRThreadRadioManager setWedAccessoryServer:]
+ -[HMMTRThreadRadioManager wedAccessoryServer]
+ -[HMMTRVendorMetadataFileStore dclCacheAvailable]
+ -[HMMTRVendorMetadataFileStore logIdentifier]
+ -[HMMTRVendorMetadataFileStore setDclCacheAvailable:]
+ GCC_except_table1010
+ GCC_except_table1070
+ GCC_except_table1116
+ GCC_except_table1124
+ GCC_except_table1173
+ GCC_except_table1181
+ GCC_except_table1218
+ GCC_except_table1255
+ GCC_except_table1480
+ GCC_except_table1519
+ GCC_except_table1669
+ GCC_except_table1670
+ GCC_except_table1691
+ GCC_except_table1692
+ GCC_except_table1693
+ GCC_except_table1694
+ GCC_except_table1695
+ GCC_except_table1698
+ GCC_except_table1701
+ GCC_except_table1702
+ GCC_except_table1703
+ GCC_except_table1704
+ GCC_except_table1705
+ GCC_except_table1706
+ GCC_except_table1707
+ GCC_except_table1766
+ GCC_except_table1772
+ GCC_except_table1849
+ GCC_except_table1970
+ GCC_except_table1997
+ GCC_except_table2026
+ GCC_except_table2034
+ GCC_except_table2036
+ GCC_except_table2083
+ GCC_except_table2123
+ GCC_except_table2185
+ GCC_except_table2424
+ GCC_except_table2428
+ GCC_except_table2480
+ GCC_except_table2521
+ GCC_except_table2564
+ GCC_except_table2566
+ GCC_except_table2611
+ GCC_except_table2613
+ GCC_except_table2614
+ GCC_except_table2615
+ GCC_except_table2616
+ GCC_except_table2617
+ GCC_except_table2618
+ GCC_except_table2630
+ GCC_except_table2632
+ GCC_except_table2651
+ GCC_except_table2673
+ GCC_except_table2684
+ GCC_except_table2691
+ GCC_except_table2706
+ GCC_except_table2709
+ GCC_except_table2713
+ GCC_except_table2715
+ GCC_except_table2740
+ GCC_except_table2745
+ GCC_except_table2757
+ GCC_except_table2808
+ GCC_except_table2809
+ GCC_except_table3169
+ GCC_except_table3170
+ GCC_except_table3171
+ GCC_except_table3180
+ GCC_except_table3183
+ GCC_except_table3197
+ GCC_except_table3213
+ GCC_except_table3279
+ GCC_except_table3294
+ GCC_except_table3296
+ GCC_except_table3304
+ GCC_except_table3327
+ GCC_except_table3328
+ GCC_except_table3337
+ GCC_except_table3360
+ GCC_except_table3363
+ GCC_except_table3371
+ GCC_except_table3390
+ GCC_except_table3393
+ GCC_except_table3429
+ GCC_except_table3433
+ GCC_except_table3449
+ GCC_except_table3451
+ GCC_except_table3469
+ GCC_except_table3532
+ GCC_except_table3576
+ GCC_except_table3618
+ GCC_except_table3622
+ GCC_except_table3637
+ GCC_except_table3638
+ GCC_except_table3643
+ GCC_except_table3650
+ GCC_except_table3708
+ GCC_except_table3728
+ GCC_except_table3782
+ GCC_except_table3787
+ GCC_except_table3790
+ GCC_except_table3867
+ GCC_except_table3868
+ GCC_except_table3923
+ GCC_except_table3926
+ GCC_except_table3988
+ GCC_except_table403
+ GCC_except_table4050
+ GCC_except_table4054
+ GCC_except_table4058
+ GCC_except_table4061
+ GCC_except_table4094
+ GCC_except_table470
+ GCC_except_table640
+ GCC_except_table643
+ GCC_except_table703
+ GCC_except_table704
+ GCC_except_table705
+ GCC_except_table771
+ GCC_except_table834
+ GCC_except_table838
+ GCC_except_table842
+ GCC_except_table844
+ GCC_except_table848
+ GCC_except_table852
+ GCC_except_table855
+ GCC_except_table898
+ GCC_except_table902
+ GCC_except_table904
+ _HMMTRAppleAlvaradoGuidanceConsumerClusterReducePeriodEventID
+ _HMMTRAppleAlvaradoThermostatClusterID
+ _HMMTRThermostatClusterAppleActivePresetChangedEventID
+ _OBJC_CLASS_$_HMMTRCommissioningSessionHandler
+ _OBJC_CLASS_$_HMMTRStorageEventDispatcher
+ _OBJC_CLASS_$_HMMTRSyncClusterSmokeCOAlarm
+ _OBJC_CLASS_$_MTRClusterSmokeCOAlarm
+ _OBJC_IVAR_$_HMMTRAccessoryServer._setupPayloadForPairingUsingMatterSupport
+ _OBJC_IVAR_$_HMMTRAccessoryServer._stageCommissioneeInfoHandler
+ _OBJC_IVAR_$_HMMTRAccessoryServerBrowser._discoveringAccessoryServersRequested
+ _OBJC_IVAR_$_HMMTRCommissioningSessionHandler._allPairedNodeIDs
+ _OBJC_IVAR_$_HMMTRCommissioningSessionHandler._clientQueue
+ _OBJC_IVAR_$_HMMTRCommissioningSessionHandler._completionHandler
+ _OBJC_IVAR_$_HMMTRCommissioningSessionHandler._controllerParametersToRemove
+ _OBJC_IVAR_$_HMMTRCommissioningSessionHandler._nodeID
+ _OBJC_IVAR_$_HMMTRFabricData._fabricID
+ _OBJC_IVAR_$_HMMTRFabricData._residentOperationalCert
+ _OBJC_IVAR_$_HMMTRFabricData._residentOperationalKeyPair
+ _OBJC_IVAR_$_HMMTRFabricData._rootKeyPair
+ _OBJC_IVAR_$_HMMTRFabricData._rootPublicKey
+ _OBJC_IVAR_$_HMMTRStorageEventDispatcher._caseAuthenticatedTagsUpdated
+ _OBJC_IVAR_$_HMMTRStorageEventDispatcher._dataSource
+ _OBJC_IVAR_$_HMMTRStorageEventDispatcher._delegate
+ _OBJC_IVAR_$_HMMTRStorageEventDispatcher._fabricDataSource
+ _OBJC_IVAR_$_HMMTRStorageEventDispatcher._fabricID
+ _OBJC_IVAR_$_HMMTRStorageEventDispatcher._fabricUUID
+ _OBJC_IVAR_$_HMMTRStorageEventDispatcher._lock
+ _OBJC_IVAR_$_HMMTRStorageEventDispatcher._workQueue
+ _OBJC_IVAR_$_HMMTRThreadRadioManager._wedAccessoryServer
+ _OBJC_IVAR_$_HMMTRVendorMetadataFileStore._dclCacheAvailable
+ _OBJC_METACLASS_$_HMMTRCommissioningSessionHandler
+ _OBJC_METACLASS_$_HMMTRStorageEventDispatcher
+ _OBJC_METACLASS_$_HMMTRSyncClusterSmokeCOAlarm
+ _OBJC_METACLASS_$_MTRClusterSmokeCOAlarm
+ __OBJC_$_CLASS_METHODS_HMMTRCommissioningSessionHandler
+ __OBJC_$_CLASS_METHODS_HMMTRStorageEventDispatcher
+ __OBJC_$_CLASS_METHODS_HMMTRSyncClusterSmokeCOAlarm
+ __OBJC_$_INSTANCE_METHODS_HMMTRCommissioningSessionHandler
+ __OBJC_$_INSTANCE_METHODS_HMMTRStorageEventDispatcher
+ __OBJC_$_INSTANCE_METHODS_HMMTRSyncClusterSmokeCOAlarm
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRCommissioningSessionHandler
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRStorageEventDispatcher
+ __OBJC_$_PROP_LIST_HMMTRCommissioningSessionHandler
+ __OBJC_$_PROP_LIST_HMMTRStorageEventDispatcher
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HMMTRHAPAccessoryServerPairingDelegate
+ __OBJC_CLASS_PROTOCOLS_$_HMMTRCommissioningSessionHandler
+ __OBJC_CLASS_PROTOCOLS_$_HMMTRStorageEventDispatcher
+ __OBJC_CLASS_RO_$_HMMTRCommissioningSessionHandler
+ __OBJC_CLASS_RO_$_HMMTRStorageEventDispatcher
+ __OBJC_CLASS_RO_$_HMMTRSyncClusterSmokeCOAlarm
+ __OBJC_METACLASS_RO_$_HMMTRCommissioningSessionHandler
+ __OBJC_METACLASS_RO_$_HMMTRStorageEventDispatcher
+ __OBJC_METACLASS_RO_$_HMMTRSyncClusterSmokeCOAlarm
+ ___101-[HMMTRAccessoryServer updateAccessoryControlToIncludeAdministratorNodes:sharedUserNodes:completion:]_block_invoke.794
+ ___102-[HMMTRAccessoryServer updateAllCharacteristicValuesPostHAPServiceEnumerationForAccessory:completion:]_block_invoke.753
+ ___104-[HMMTRAccessoryServerBrowser setUpBrowserTargetFabricWithoutRediscoveringAccessoriesForHomeFabricUUID:]_block_invoke
+ ___107-[HMMTRAccessoryServerBrowser _fetchDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.198
+ ___110-[HMMTRAccessoryServerBrowser removeAllDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.200
+ ___111-[HMMTRThreadRadioManager _startAccessoryPairingWithExtendedMACAddress:isWedDevice:accessoryServer:completion:]_block_invoke.22
+ ___113-[HMMTRCommissioningSessionHandler removeFabricFromDeviceBeingCommissionedWithController:fabricIndex:completion:]_block_invoke
+ ___114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke.866
+ ___114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke.869
+ ___114-[HMMTRProtocolMap _selectedServiceTypeForServiceArray:device:mtrDevice:endpoint:callbackQueue:completionHandler:]_block_invoke.411
+ ___117-[HMMTRAccessoryServer _findSystemCommissionerPairingMatchingSetupPayload:systemCommissionerPairings:pairingManager:]_block_invoke.257
+ ___117-[HMMTRAccessoryServer _findSystemCommissionerPairingMatchingSetupPayload:systemCommissionerPairings:pairingManager:]_block_invoke.258
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.483
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.484
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.485
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.487
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_3.488
+ ___119-[HMMTRAccessoryServerBrowser removeDevicePairingFabricForSystemCommissionerDeviceWithNodeID:fabric:completionHandler:]_block_invoke.196
+ ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.310
+ ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.317
+ ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.318
+ ___159-[HMMTRCommissioningSessionHandler establishSessionToRemoveFabricWithDeviceController:forControllerParameters:setupPayload:nodeID:allPairedNodeIDs:completion:]_block_invoke
+ ___177-[HMMTRAccessoryServerBrowser setOperationalFabricData:operationalCertIssuer:storageDataSource:allTargetFabricUUIDs:entityIdentifier:accessoryServerNodeIDs:forTargetFabricUUID:]_block_invoke
+ ___213-[HMMTRAccessoryServer startStagedPairingWithDeviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:commissioneeInfoHandler:scanningNetworks:completion:]_block_invoke
+ ___251-[HMMTRAccessoryServerBrowser stageAccessoryServerWithSetupPayload:fabricID:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:commissioneeInfoHandler:scanningNetworks:completionHandler:]_block_invoke
+ ___278-[HMMTRAccessoryServerBrowser _stageAccessoryServerWithSetupPayload:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:commissioneeInfoHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke
+ ___278-[HMMTRAccessoryServerBrowser _stageAccessoryServerWithSetupPayload:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:commissioneeInfoHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke.183
+ ___278-[HMMTRAccessoryServerBrowser _stageAccessoryServerWithSetupPayload:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:commissioneeInfoHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke_2
+ ___31-[HMMTRStorage clearStaleItems]_block_invoke
+ ___37-[HMMTRAccessoryServer finishPairing]_block_invoke.733
+ ___37-[HMMTRAccessoryServer timerDidFire:]_block_invoke.277
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.611
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.612
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.613
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.614
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.616
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.620
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.621
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.622
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.623
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.615
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.624
+ ___40-[HMMTRStorage _removeAllDataSourceData]_block_invoke.121
+ ___42+[HMMTRStorageEventDispatcher logCategory]_block_invoke
+ ___42-[HMMTRAccessoryServer _setupMatterDevice]_block_invoke.307
+ ___42-[HMMTRAccessoryServer _setupMatterDevice]_block_invoke.309
+ ___43+[HMMTRSyncClusterSmokeCOAlarm logCategory]_block_invoke
+ ___43-[HMMTRAccessoryServer _setupThreadPairing]_block_invoke
+ ___43-[HMMTRAccessoryServer _setupThreadPairing]_block_invoke.445
+ ___43-[HMMTRAccessoryServer _unpair:completion:]_block_invoke.300
+ ___43-[HMMTRAccessoryServer discoverAccessories]_block_invoke.303
+ ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.844
+ ___45-[HMMTRAccessoryServer stopPairingWithError:]_block_invoke.289
+ ___45-[HMMTRStorage _syncSetDataSourceDictionary:]_block_invoke.122
+ ___47+[HMMTRCommissioningSessionHandler logCategory]_block_invoke
+ ___47-[HMMTRAccessoryServer processAttributeReport:]_block_invoke.930
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.818
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.821
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.823
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke_2.822
+ ___49-[HMMTRAccessoryServerBrowser startBluetoothScan]_block_invoke.349
+ ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.777
+ ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.781
+ ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.782
+ ___51-[HMMTRAccessoryServer device:receivedEventReport:]_block_invoke.931
+ ___51-[HMMTRStorage syncDataSourceDictionary:forFabric:]_block_invoke.123
+ ___52-[HMMTRAccessoryServer populateACLEntriesForPairing]_block_invoke.609
+ ___52-[HMMTRAccessoryServerBrowser _cleanupStagedServers]_block_invoke.300
+ ___53-[HMMTRAccessoryServer _tryPairingUsingMatterSupport]_block_invoke.251
+ ___55-[HMMTRAccessoryServer device:receivedAttributeReport:]_block_invoke.929
+ ___56-[HMMTRAccessoryServer controller:readCommissioneeInfo:]_block_invoke
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.403
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.404
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.405
+ ___56-[HMMTRStorage _syncSetDataSourceValuesWithError:block:]_block_invoke.118
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.415
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.416
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.417
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.421
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.871
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.873
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.877
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.879
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.409
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.410
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.411
+ ___60-[HMMTRAccessoryServerBrowser setUpBrowserTargetFabricUUID:]_block_invoke
+ ___61-[HMMTRAccessoryServerBrowser deviceControllerForFabricUUID:]_block_invoke
+ ___62-[HMMTRAccessoryServerBrowser stopDiscoveringAccessoryServers]_block_invoke.172
+ ___62-[HMMTRStorageEventDispatcher handleUpdatedCurrentFabricIndex]_block_invoke
+ ___63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.775
+ ___63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.776
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.463
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.464
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.465
+ ___63-[HMMTRAccessoryServerBrowser _deleteOldPairingsForFabricUUID:]_block_invoke
+ ___63-[HMMTRAccessoryServerBrowser notifyDiscoveredAccessoryServer:]_block_invoke
+ ___63-[HMMTRAccessoryServerBrowser notifyDiscoveredAccessoryServer:]_block_invoke_2
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.433
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.434
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.435
+ ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.893
+ ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.894
+ ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.895
+ ___64-[HMMTRAccessoryServerBrowser handleHomeDeletionWithFabricUUID:]_block_invoke
+ ___64-[HMMTRAccessoryServerBrowser handleHomeDeletionWithFabricUUID:]_block_invoke_2
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.428
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.429
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.430
+ ___66-[HMMTRStorageEventDispatcher handleUpdatedDataWithIsLocalChange:]_block_invoke
+ ___67-[HMMTRStorageEventDispatcher _handleUpdatedDataWithIsLocalChange:]_block_invoke
+ ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.422
+ ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.423
+ ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.424
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.452
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.453
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.454
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.461
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.462
+ ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.395
+ ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.400
+ ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.401
+ ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.402
+ ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.173
+ ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.176
+ ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.178
+ ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.180
+ ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke_2.179
+ ___69-[HMMTRColorControl stopMoveToColorTemperatureCommandWithCompletion:]_block_invoke_2
+ ___70-[HMMTRAccessoryServer readSpecificationVersionWithCompletionHandler:]_block_invoke
+ ___71-[HMMTRAccessoryServer validateAttestationDeviceInfo:error:completion:]_block_invoke.279
+ ___71-[HMMTRAccessoryServerBrowser setUpBrowserTargetFabricUUID:completion:]_block_invoke
+ ___71-[HMMTRThreadRadioManager _retryWEDConnectionToAccessoryWithDelayInMs:]_block_invoke.32
+ ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.380
+ ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.386
+ ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.387
+ ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.388
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.446
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.447
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.448
+ ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.263
+ ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.264
+ ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.265
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.770
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.771
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.773
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.774
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.754
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.755
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.765
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.766
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.768
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.769
+ ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.828
+ ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.829
+ ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.833
+ ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke_2.835
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.292
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.293
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.294
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.295
+ ___76-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithNodeID:completion:]_block_invoke.181
+ ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.389
+ ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.390
+ ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.391
+ ___79-[HMMTRAccessoryServerBrowser _updateAccessoryControlListForServer:completion:]_block_invoke.305
+ ___79-[HMMTRThreadRadioManager connectToAccessoryWithExtendedMACAddress:completion:]_block_invoke
+ ___81-[HMMTRAccessoryServer _controller:commissioningComplete:nodeID:abstractMetrics:]_block_invoke
+ ___82-[HMMTRAccessoryServer fetchColorControlClusterForHapAccessory:completionHandler:]_block_invoke.880
+ ___82-[HMMTRAccessoryServer fetchColorControlClusterForHapAccessory:completionHandler:]_block_invoke.882
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.848
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.849
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.850
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.853
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke_2.852
+ ___83-[HMMTRAccessoryServer updateAccessoryControlToRemoveAdministratorNode:completion:]_block_invoke.795
+ ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.366
+ ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.368
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.854
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.855
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.856
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.857
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.861
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.862
+ ___84-[HMMTRAccessoryServerBrowser updateDiscoveredAccessoryServersWithNodes:fabricUUID:]_block_invoke
+ ___85-[HMMTRAccessoryServerBrowser _updateDiscoveredAccessoryServersWithNodes:fabricUUID:]_block_invoke
+ ___85-[HMMTRCommissioningSessionHandler controller:commissioningSessionEstablishmentDone:]_block_invoke
+ ___85-[HMMTRCommissioningSessionHandler controller:commissioningSessionEstablishmentDone:]_block_invoke.11
+ ___85-[HMMTRCommissioningSessionHandler controller:commissioningSessionEstablishmentDone:]_block_invoke.8
+ ___85-[HMMTRCommissioningSessionHandler controller:commissioningSessionEstablishmentDone:]_block_invoke_2
+ ___85-[HMMTRCommissioningSessionHandler controller:commissioningSessionEstablishmentDone:]_block_invoke_2.12
+ ___86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.896
+ ___86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.897
+ ___87-[HMMTRAccessoryServerBrowser startDiscoveringAccessoryServersWithNoResponseToDelegate]_block_invoke
+ ___88-[HMMTRAccessoryServerBrowser _startDiscoveringAccessoryServersWithNoResponseToDelegate]_block_invoke
+ ___88-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:keepAliveOnly:]_block_invoke.341
+ ___88-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:keepAliveOnly:]_block_invoke.342
+ ___88-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:keepAliveOnly:]_block_invoke.343
+ ___89-[HMMTRThreadRadioManager _connectToAccessoryWithExtendedMACAddress:forRetry:completion:]_block_invoke
+ ___89-[HMMTRThreadRadioManager _connectToAccessoryWithExtendedMACAddress:forRetry:completion:]_block_invoke_2
+ ___89-[HMMTRThreadRadioManager _connectToAccessoryWithExtendedMACAddress:forRetry:completion:]_block_invoke_3
+ ___90-[HMMTRAccessoryServerBrowser handleHomeAddedAccessoryWithNodeID:fabricUUID:localControl:]_block_invoke
+ ___91-[HMMTRProtocolMap servicesForDeviceTypes:device:endpoint:callbackQueue:completionHandler:]_block_invoke.414
+ ___92-[HMMTRAccessoryServer _createFirmwareUpdateServiceWithInstanceID:device:completionHandler:]_block_invoke.746
+ ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.493
+ ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.494
+ ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.495
+ ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke_2.497
+ ___92-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fabricUUID:fatalError:]_block_invoke
+ ___92-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fabricUUID:fatalError:]_block_invoke.303
+ ___92-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fabricUUID:fatalError:]_block_invoke.304
+ ___94-[HMMTRAccessoryServer updateAccessoryControlToAdministratorNodes:sharedUserNodes:completion:]_block_invoke.793
+ ___96-[HMMTRProtocolMap servicesOfMTRDevice:forDeviceTypes:endpoint:callbackQueue:completionHandler:]_block_invoke.415
+ ___97-[HMMTRAccessoryServerBrowser setUpBrowserTargetFabricAndRediscoverAccessoriesForHomeFabricUUID:]_block_invoke
+ ___99-[HMMTRAccessoryServer _tryPairingWithOnboardingPayload:systemCommissionerPairings:pairingManager:]_block_invoke.254
+ ___99-[HMMTRAccessoryServer _tryPairingWithOnboardingPayload:systemCommissionerPairings:pairingManager:]_block_invoke.255
+ ___Block_byref_object_copy_.10592
+ ___Block_byref_object_copy_.11263
+ ___Block_byref_object_copy_.11961
+ ___Block_byref_object_copy_.12127
+ ___Block_byref_object_copy_.1553
+ ___Block_byref_object_copy_.2907
+ ___Block_byref_object_copy_.3186
+ ___Block_byref_object_copy_.4274
+ ___Block_byref_object_copy_.5430
+ ___Block_byref_object_copy_.7071
+ ___Block_byref_object_copy_.7417
+ ___Block_byref_object_copy_.7837
+ ___Block_byref_object_copy_.8927
+ ___Block_byref_object_copy_.9879
+ ___Block_byref_object_dispose_.10593
+ ___Block_byref_object_dispose_.11264
+ ___Block_byref_object_dispose_.11962
+ ___Block_byref_object_dispose_.12128
+ ___Block_byref_object_dispose_.1554
+ ___Block_byref_object_dispose_.2908
+ ___Block_byref_object_dispose_.3187
+ ___Block_byref_object_dispose_.4275
+ ___Block_byref_object_dispose_.5431
+ ___Block_byref_object_dispose_.7072
+ ___Block_byref_object_dispose_.7418
+ ___Block_byref_object_dispose_.7838
+ ___Block_byref_object_dispose_.8928
+ ___Block_byref_object_dispose_.9880
+ ___block_descriptor_105_e8_32s40s48bs56bs64bs72bs80bs88bs96bs_e45_v28?0B8"HMMTRAccessoryServer"12"NSError"20ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_105_e8_32s40s48bs56bs64bs72bs80bs88bs96bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_121_e8_32s40s48s56s64bs72bs80bs88bs96bs104bs112bs_e5_v8?0ls32l8s40l8s48l8s64l8s56l8s72l8s80l8s88l8s96l8s104l8s112l8
+ ___block_descriptor_32_e74_"NSNumber"16?0"MTROperationalCredentialsClusterFabricDescriptorStruct"8l
+ ___block_descriptor_40_e8_32bs_e42_v24?0"HMMTRAccessoryServer"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e64_B16?0"MTROperationalCredentialsClusterFabricDescriptorStruct"8ls32l8
+ ___block_descriptor_48_e8_32s40s_e30_B16?0"HMMTRAccessoryServer"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e46_v24?0"HAPThreadNetworkMetadata"8"NSError"16ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e71_v24?0"MTROperationalCredentialsClusterNOCResponseParams"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_97_e8_32s40bs48bs56bs64bs72bs80bs88bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_literal_global.1026
+ ___block_literal_global.10331
+ ___block_literal_global.10859
+ ___block_literal_global.11084
+ ___block_literal_global.1130
+ ___block_literal_global.11300
+ ___block_literal_global.11437
+ ___block_literal_global.11570
+ ___block_literal_global.11788
+ ___block_literal_global.1208
+ ___block_literal_global.132
+ ___block_literal_global.14
+ ___block_literal_global.1421
+ ___block_literal_global.149
+ ___block_literal_global.1674
+ ___block_literal_global.1726
+ ___block_literal_global.1772
+ ___block_literal_global.1860
+ ___block_literal_global.22
+ ___block_literal_global.2222
+ ___block_literal_global.2362
+ ___block_literal_global.245
+ ___block_literal_global.2668
+ ___block_literal_global.2811
+ ___block_literal_global.2840
+ ___block_literal_global.2932
+ ___block_literal_global.3085
+ ___block_literal_global.315
+ ___block_literal_global.3279
+ ___block_literal_global.338
+ ___block_literal_global.3421
+ ___block_literal_global.3532
+ ___block_literal_global.357
+ ___block_literal_global.4037
+ ___block_literal_global.412
+ ___block_literal_global.4365
+ ___block_literal_global.46.9679
+ ___block_literal_global.4654
+ ___block_literal_global.4788
+ ___block_literal_global.485
+ ___block_literal_global.4889
+ ___block_literal_global.5147
+ ___block_literal_global.5319
+ ___block_literal_global.5556
+ ___block_literal_global.5686
+ ___block_literal_global.5922
+ ___block_literal_global.5956
+ ___block_literal_global.5977
+ ___block_literal_global.6227
+ ___block_literal_global.6239
+ ___block_literal_global.6335
+ ___block_literal_global.6432
+ ___block_literal_global.651
+ ___block_literal_global.6528
+ ___block_literal_global.6636
+ ___block_literal_global.6733
+ ___block_literal_global.6830
+ ___block_literal_global.6974
+ ___block_literal_global.7113
+ ___block_literal_global.7223
+ ___block_literal_global.7294
+ ___block_literal_global.743
+ ___block_literal_global.75.9680
+ ___block_literal_global.751
+ ___block_literal_global.758
+ ___block_literal_global.7621
+ ___block_literal_global.7848
+ ___block_literal_global.8179
+ ___block_literal_global.8302
+ ___block_literal_global.84
+ ___block_literal_global.8434
+ ___block_literal_global.8957
+ ___block_literal_global.909
+ ___block_literal_global.9359
+ ___block_literal_global.938
+ ___block_literal_global.9678
+ ___block_literal_global.9757
+ ___isHH2Enabled_block_invoke
+ _isHH2Enabled
+ _isHH2Enabled.hh2Enabled
+ _isHH2Enabled.onceToken
+ _logCategory._hmf_once_t0.2810
+ _logCategory._hmf_once_t0.5318
+ _logCategory._hmf_once_t0.5955
+ _logCategory._hmf_once_t10.11787
+ _logCategory._hmf_once_t13.2931
+ _logCategory._hmf_once_t13.3278
+ _logCategory._hmf_once_t14
+ _logCategory._hmf_once_t18
+ _logCategory._hmf_once_t2.4888
+ _logCategory._hmf_once_t2.5921
+ _logCategory._hmf_once_t2.6973
+ _logCategory._hmf_once_t2.9756
+ _logCategory._hmf_once_t20.11436
+ _logCategory._hmf_once_t23.6334
+ _logCategory._hmf_once_t23.6431
+ _logCategory._hmf_once_t23.6635
+ _logCategory._hmf_once_t23.6732
+ _logCategory._hmf_once_t23.6829
+ _logCategory._hmf_once_t26.1420
+ _logCategory._hmf_once_t3.1129
+ _logCategory._hmf_once_t3.1207
+ _logCategory._hmf_once_t31.11569
+ _logCategory._hmf_once_t356
+ _logCategory._hmf_once_t4.3420
+ _logCategory._hmf_once_t4.7222
+ _logCategory._hmf_once_t6.1771
+ _logCategory._hmf_once_t6.1859
+ _logCategory._hmf_once_t663
+ _logCategory._hmf_once_t8.11083
+ _logCategory._hmf_once_t87.10833
+ _logCategory._hmf_once_t9.5685
+ _logCategory._hmf_once_v1.2812
+ _logCategory._hmf_once_v1.5320
+ _logCategory._hmf_once_v1.5957
+ _logCategory._hmf_once_v10.5687
+ _logCategory._hmf_once_v11.11789
+ _logCategory._hmf_once_v14.2933
+ _logCategory._hmf_once_v14.3280
+ _logCategory._hmf_once_v15
+ _logCategory._hmf_once_v19
+ _logCategory._hmf_once_v21.11438
+ _logCategory._hmf_once_v24.6336
+ _logCategory._hmf_once_v24.6433
+ _logCategory._hmf_once_v24.6637
+ _logCategory._hmf_once_v24.6734
+ _logCategory._hmf_once_v24.6831
+ _logCategory._hmf_once_v27.1422
+ _logCategory._hmf_once_v3.4890
+ _logCategory._hmf_once_v3.5923
+ _logCategory._hmf_once_v3.6975
+ _logCategory._hmf_once_v3.9758
+ _logCategory._hmf_once_v32.11571
+ _logCategory._hmf_once_v357
+ _logCategory._hmf_once_v4.1131
+ _logCategory._hmf_once_v4.1209
+ _logCategory._hmf_once_v5.3422
+ _logCategory._hmf_once_v5.7224
+ _logCategory._hmf_once_v664
+ _logCategory._hmf_once_v7.1773
+ _logCategory._hmf_once_v7.1861
+ _logCategory._hmf_once_v88.10834
+ _logCategory._hmf_once_v9.11085
+ _objc_msgSend$_addDiscoveredAccessoryServerWithNodeID:fabricUUID:
+ _objc_msgSend$_connectToAccessoryWithExtendedMACAddress:forRetry:completion:
+ _objc_msgSend$_controller:commissioningAndPairedNodeRecoveryComplete:nodeID:abstractMetrics:
+ _objc_msgSend$_convertPairingFailureError:
+ _objc_msgSend$_createCHIPAccessoryForNodeID:ifPaired:fabricUUID:fatalError:
+ _objc_msgSend$_createSystemCommissionerCHIPAccessoryForNodeID:
+ _objc_msgSend$_deleteOldPairingsForFabricUUID:
+ _objc_msgSend$_isAllowedForRawEventDictionaryHandling:
+ _objc_msgSend$_isDevicePaired:fabricUUID:
+ _objc_msgSend$_setUpBrowserTargetFabricIfNotFabricUUID:rediscoverAccessories:
+ _objc_msgSend$_setUpBrowserTargetFabricUUID:
+ _objc_msgSend$_setUpUpdatedBrowserTargetFabricUUID:
+ _objc_msgSend$_setUpUpdatedBrowserTargetFabricUUID:rediscoverAccessories:
+ _objc_msgSend$_setUpUpdatedBrowserTargetFabricUUID:rediscoverAccessories:overrideAccessoryControlAllowed:
+ _objc_msgSend$_setupPayloadForLastCommissioning
+ _objc_msgSend$_setupThreadPairing
+ _objc_msgSend$_stageAccessoryServerWithSetupPayload:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:commissioneeInfoHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:
+ _objc_msgSend$_startDiscoveringAccessoryServersWithNoResponseToDelegate
+ _objc_msgSend$_updateDiscoveredAccessoryServersWithNodes:fabricUUID:
+ _objc_msgSend$accessoryServer:didReadCommissioneeInfo:
+ _objc_msgSend$allPairedNodeIDs
+ _objc_msgSend$bundlePath
+ _objc_msgSend$clearOperationalFabricDataForTargetFabricUUID:
+ _objc_msgSend$clearStaleItems
+ _objc_msgSend$completionHandler
+ _objc_msgSend$connectToWEDAccessory:completion:
+ _objc_msgSend$containsString:
+ _objc_msgSend$controllerParametersToRemove
+ _objc_msgSend$controllerWrapperForFabricUUID:
+ _objc_msgSend$dclCacheAvailable
+ _objc_msgSend$deviceBeingCommissionedWithNodeID:error:
+ _objc_msgSend$deviceControllerForFabricUUID:
+ _objc_msgSend$disconnectFromWEDAccessory:completion:
+ _objc_msgSend$discoveringAccessoryServersRequested
+ _objc_msgSend$establishSessionToRemoveFabricWithDeviceController:forControllerParameters:setupPayload:nodeID:allPairedNodeIDs:completion:
+ _objc_msgSend$handleAttestationComplete
+ _objc_msgSend$handleCommissioneeHasReceivedNetworkCredentials
+ _objc_msgSend$handleRawEventReportDictionary:flow:hapAccessory:
+ _objc_msgSend$hmf_enumerateWithAutoreleasePoolUsingBlock:
+ _objc_msgSend$initWithClientQueue:
+ _objc_msgSend$initWithQueue:dataSource:systemCommissionerFabric:fabricUUID:sharedAdmin:
+ _objc_msgSend$isCurrentDeviceAllowedAccessoryControlDespiteReachableResidentForFabricUUID:
+ _objc_msgSend$mapSensorFaultToStatusActive:
+ _objc_msgSend$notifyDiscoveredAccessoryServer:
+ _objc_msgSend$readAttributeEndOfServiceAlertWithParams:
+ _objc_msgSend$readAttributeFabricsWithParams:completion:
+ _objc_msgSend$readAttributeHardwareFaultAlertWithParams:
+ _objc_msgSend$readAttributeSpecificationVersionWithParams:
+ _objc_msgSend$readFabricsFromDeviceBeingCommissionedWithController:completion:
+ _objc_msgSend$removeFabricFromDeviceBeingCommissionedWithController:fabricIndex:completion:
+ _objc_msgSend$removeFabricWithParams:completion:
+ _objc_msgSend$setAllPairedNodeIDs:
+ _objc_msgSend$setCompletionHandler:
+ _objc_msgSend$setControllerParametersToRemove:
+ _objc_msgSend$setDclCacheAvailable:
+ _objc_msgSend$setDiscoveringAccessoryServersRequested:
+ _objc_msgSend$setSetupPayloadForPairingUsingMatterSupport:
+ _objc_msgSend$setStageCommissioneeInfoHandler:
+ _objc_msgSend$setUpBrowserTargetFabricAndRediscoverAccessoriesForHomeFabricUUID:
+ _objc_msgSend$setUpBrowserTargetFabricUUID:
+ _objc_msgSend$setUpBrowserTargetFabricUUID:completion:
+ _objc_msgSend$setUpCommissioningSessionWithDeviceController:payload:newNodeID:error:
+ _objc_msgSend$setWedAccessoryServer:
+ _objc_msgSend$setupPayloadForPairingUsingMatterSupport
+ _objc_msgSend$stageAccessoryServerWithSetupPayload:fabricID:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:commissioneeInfoHandler:scanningNetworks:completionHandler:
+ _objc_msgSend$stageCommissioneeInfoHandler
+ _objc_msgSend$startDiscoveringAccessoryServersWithNoResponseToDelegate
+ _objc_msgSend$startStagedPairingWithDeviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:commissioneeInfoHandler:scanningNetworks:completion:
+ _objc_msgSend$statusCode
+ _objc_msgSend$storageForFabricUUID:sharedAdmin:
+ _objc_msgSend$storageForSystemCommissioner
+ _objc_msgSend$updateDiscoveredAccessoryServersWithNodes:fabricUUID:
+ _objc_msgSend$wedAccessoryServer
- +[HMMTRFabricData logCategory]
- -[HMMTRAccessoryServer _removeSharedAdminControllerNodeIDFromACLWithCompletion:]
- -[HMMTRAccessoryServer _restoreCommissioneeInfoBeforeNextPairingAttempt]
- -[HMMTRAccessoryServer originalPairingAttemptOperationalCert]
- -[HMMTRAccessoryServer originalPairingAttemptRootCert]
- -[HMMTRAccessoryServer setOriginalPairingAttemptOperationalCert:]
- -[HMMTRAccessoryServer setOriginalPairingAttemptRootCert:]
- -[HMMTRAccessoryServer setStorage:]
- -[HMMTRAccessoryServer setupThreadPairing]
- -[HMMTRAccessoryServer startStagedPairingWithDeviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:scanningNetworks:completion:]
- -[HMMTRAccessoryServer storage]
- -[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:]
- -[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fatalError:]
- -[HMMTRAccessoryServerBrowser _currentHomeFabricDeviceController]
- -[HMMTRAccessoryServerBrowser _deleteOldPairings]
- -[HMMTRAccessoryServerBrowser _isDevicePaired:]
- -[HMMTRAccessoryServerBrowser _setupStorageStateForHomeFabricUUID:]
- -[HMMTRAccessoryServerBrowser _setupStorageStateForUpdatedHomeFabricUUID:]
- -[HMMTRAccessoryServerBrowser _setupStorageStateForUpdatedHomeFabricUUID:rediscoverAccessories:]
- -[HMMTRAccessoryServerBrowser _setupStorageStateForUpdatedHomeFabricUUID:rediscoverAccessories:overrideAccessoryControlAllowed:]
- -[HMMTRAccessoryServerBrowser _setupStorageStateIfNotFabricUUID:rediscoverAccessories:]
- -[HMMTRAccessoryServerBrowser _stageAccessoryServerWithSetupPayload:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:]
- -[HMMTRAccessoryServerBrowser appleHomeTargetFabricUUIDWithID:]
- -[HMMTRAccessoryServerBrowser currentHomeFabricDeviceControllerWrapper]
- -[HMMTRAccessoryServerBrowser deviceController]
- -[HMMTRAccessoryServerBrowser getNumberOfAccessoryServersForFabricUUID:completion:]
- -[HMMTRAccessoryServerBrowser handleHomeAddedAccessoryWithNodeID:fabricUUID:]
- -[HMMTRAccessoryServerBrowser handleHomeDeletionWithFabric:]
- -[HMMTRAccessoryServerBrowser isSystemCommissionerMode]
- -[HMMTRAccessoryServerBrowser matterStorageItems]
- -[HMMTRAccessoryServerBrowser pendingMatterStackRestart]
- -[HMMTRAccessoryServerBrowser setMatterStorageItems:]
- -[HMMTRAccessoryServerBrowser setOperationalFabricData:operationalCertIssuer:storageDataSource:allTargetFabricUUIDs:entityIdentifier:forTargetFabricUUID:]
- -[HMMTRAccessoryServerBrowser setPendingMatterStackRestart:]
- -[HMMTRAccessoryServerBrowser setSystemCommissionerMode:]
- -[HMMTRAccessoryServerBrowser setupStorageStateAndRediscoverAccessoriesForHomeFabricUUID:]
- -[HMMTRAccessoryServerBrowser setupStorageStateForHomeFabricUUID:]
- -[HMMTRAccessoryServerBrowser setupStorageStateForHomeFabricUUID:completion:]
- -[HMMTRAccessoryServerBrowser setupStorageStateWithoutRediscoveringAccessoriesForHomeFabricUUID:]
- -[HMMTRAccessoryServerBrowser stageAccessoryServerWithSetupPayload:fabricID:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:scanningNetworks:completionHandler:]
- -[HMMTRAccessoryServerBrowser systemCommissionerMode]
- -[HMMTRFabric fabricData]
- -[HMMTRFabricControllerStore cachedWrapperWithFabricID:]
- -[HMMTRFabricData attributeDescriptions]
- -[HMMTRFabricData fabric]
- -[HMMTRFabricData initWithFabric:]
- -[HMMTRFabricData logIdentifier]
- -[HMMTRFabricData setFabric:]
- -[HMMTRFabricData setIpk:]
- -[HMMTRFabricData setResidentNodeID:]
- -[HMMTRFabricData setRootCert:]
- -[HMMTRFabricDataSnapshot .cxx_destruct]
- -[HMMTRFabricDataSnapshot fabricID]
- -[HMMTRFabricDataSnapshot initWithRootPublicKey:fabricID:ipk:residentNodeID:rootKeyPair:rootCert:residentOperationalKeyPair:residentOperationalCert:]
- -[HMMTRFabricDataSnapshot ipk]
- -[HMMTRFabricDataSnapshot residentNodeID]
- -[HMMTRFabricDataSnapshot residentOperationalCert]
- -[HMMTRFabricDataSnapshot residentOperationalKeyPair]
- -[HMMTRFabricDataSnapshot rootCert]
- -[HMMTRFabricDataSnapshot rootKeyPair]
- -[HMMTRFabricDataSnapshot rootPublicKey]
- -[HMMTRStorage _handlePerFabricStorageMaybeAvailable:]
- -[HMMTRStorage _handleUpdatedDataWithIsLocalChange:]
- -[HMMTRStorage _nodeIDFromOperationalX509Certificate:]
- -[HMMTRStorage delegate]
- -[HMMTRStorage handlePrimaryResidentDataReady]
- -[HMMTRStorage handleUpdatedCurrentFabricIndex]
- -[HMMTRStorage handleUpdatedDataForFabricIndex:isLocalChange:]
- -[HMMTRStorage handleUpdatedDataForFabricIndex:nodeID:isLocalChange:]
- -[HMMTRStorage handleUpdatedDataWithIsLocalChange:]
- -[HMMTRStorage initWithQueue:]
- -[HMMTRStorage ipkForCurrentFabric]
- -[HMMTRStorage isFabricCreationInProgress]
- -[HMMTRStorage legacyNodeIDForCurrentFabric]
- -[HMMTRStorage legacyNodeIDForTargetFabricUUID:]
- -[HMMTRStorage operationalCert]
- -[HMMTRStorage prepareStorageForTargetFabricUUID:]
- -[HMMTRStorage prepareStorageForTargetFabricUUID:forInitialSetup:]
- -[HMMTRStorage rootCertForCurrentFabric]
- -[HMMTRStorage rootCert]
- -[HMMTRStorage setDelegate:]
- -[HMMTRStorage setFabricCreationInProgress:]
- -[HMMTRStorage setFabricID:]
- -[HMMTRStorage setFabricUUID:]
- -[HMMTRStorage setOperationalCert:]
- -[HMMTRStorage setRootCert:]
- -[HMMTRStorage setSharedAdmin:]
- -[HMMTRStorage setSystemCommissionerFabric:]
- -[HMMTRThreadRadioManager connectToAccessoryWithExtendedMACAddress:forRetry:completion:]
- GCC_except_table1055
- GCC_except_table1102
- GCC_except_table1106
- GCC_except_table1113
- GCC_except_table1162
- GCC_except_table1170
- GCC_except_table1207
- GCC_except_table1244
- GCC_except_table1463
- GCC_except_table1502
- GCC_except_table1650
- GCC_except_table1651
- GCC_except_table1653
- GCC_except_table1673
- GCC_except_table1674
- GCC_except_table1675
- GCC_except_table1676
- GCC_except_table1679
- GCC_except_table1682
- GCC_except_table1683
- GCC_except_table1684
- GCC_except_table1685
- GCC_except_table1686
- GCC_except_table1687
- GCC_except_table1688
- GCC_except_table1747
- GCC_except_table1753
- GCC_except_table1830
- GCC_except_table1951
- GCC_except_table1977
- GCC_except_table2006
- GCC_except_table2014
- GCC_except_table2016
- GCC_except_table2063
- GCC_except_table2103
- GCC_except_table2165
- GCC_except_table2405
- GCC_except_table2409
- GCC_except_table2458
- GCC_except_table2466
- GCC_except_table2507
- GCC_except_table2545
- GCC_except_table2547
- GCC_except_table2571
- GCC_except_table2572
- GCC_except_table2573
- GCC_except_table2594
- GCC_except_table2595
- GCC_except_table2596
- GCC_except_table2597
- GCC_except_table2598
- GCC_except_table2610
- GCC_except_table2631
- GCC_except_table2647
- GCC_except_table2653
- GCC_except_table2664
- GCC_except_table2671
- GCC_except_table2683
- GCC_except_table2689
- GCC_except_table2708
- GCC_except_table2714
- GCC_except_table2721
- GCC_except_table2785
- GCC_except_table2786
- GCC_except_table3148
- GCC_except_table3149
- GCC_except_table3150
- GCC_except_table3153
- GCC_except_table3158
- GCC_except_table3161
- GCC_except_table3191
- GCC_except_table3252
- GCC_except_table3267
- GCC_except_table3269
- GCC_except_table3276
- GCC_except_table3277
- GCC_except_table3302
- GCC_except_table3335
- GCC_except_table3338
- GCC_except_table3346
- GCC_except_table3365
- GCC_except_table3368
- GCC_except_table3404
- GCC_except_table3408
- GCC_except_table3424
- GCC_except_table3426
- GCC_except_table3444
- GCC_except_table3503
- GCC_except_table3547
- GCC_except_table3564
- GCC_except_table3589
- GCC_except_table3608
- GCC_except_table3609
- GCC_except_table3614
- GCC_except_table3621
- GCC_except_table3679
- GCC_except_table3699
- GCC_except_table3752
- GCC_except_table3757
- GCC_except_table3760
- GCC_except_table3836
- GCC_except_table3837
- GCC_except_table3892
- GCC_except_table3895
- GCC_except_table4008
- GCC_except_table4012
- GCC_except_table4016
- GCC_except_table4019
- GCC_except_table4042
- GCC_except_table4065
- GCC_except_table417
- GCC_except_table484
- GCC_except_table651
- GCC_except_table654
- GCC_except_table714
- GCC_except_table715
- GCC_except_table716
- GCC_except_table756
- GCC_except_table819
- GCC_except_table823
- GCC_except_table825
- GCC_except_table827
- GCC_except_table829
- GCC_except_table833
- GCC_except_table837
- GCC_except_table883
- GCC_except_table887
- GCC_except_table889
- GCC_except_table995
- _OBJC_CLASS_$_HMMTRFabricDataSnapshot
- _OBJC_IVAR_$_HMMTRAccessoryServer._originalPairingAttemptOperationalCert
- _OBJC_IVAR_$_HMMTRAccessoryServer._originalPairingAttemptRootCert
- _OBJC_IVAR_$_HMMTRAccessoryServer._storage
- _OBJC_IVAR_$_HMMTRAccessoryServerBrowser._matterStorageItems
- _OBJC_IVAR_$_HMMTRAccessoryServerBrowser._pendingMatterStackRestart
- _OBJC_IVAR_$_HMMTRAccessoryServerBrowser._systemCommissionerMode
- _OBJC_IVAR_$_HMMTRFabric._fabricData
- _OBJC_IVAR_$_HMMTRFabricData._fabric
- _OBJC_IVAR_$_HMMTRFabricDataSnapshot._fabricID
- _OBJC_IVAR_$_HMMTRFabricDataSnapshot._ipk
- _OBJC_IVAR_$_HMMTRFabricDataSnapshot._residentNodeID
- _OBJC_IVAR_$_HMMTRFabricDataSnapshot._residentOperationalCert
- _OBJC_IVAR_$_HMMTRFabricDataSnapshot._residentOperationalKeyPair
- _OBJC_IVAR_$_HMMTRFabricDataSnapshot._rootCert
- _OBJC_IVAR_$_HMMTRFabricDataSnapshot._rootKeyPair
- _OBJC_IVAR_$_HMMTRFabricDataSnapshot._rootPublicKey
- _OBJC_IVAR_$_HMMTRStorage._delegate
- _OBJC_IVAR_$_HMMTRStorage._fabricCreationInProgress
- _OBJC_IVAR_$_HMMTRStorage._operationalCert
- _OBJC_IVAR_$_HMMTRStorage._rootCert
- _OBJC_METACLASS_$_HMMTRFabricDataSnapshot
- __OBJC_$_CLASS_METHODS_HMMTRFabricData
- __OBJC_$_INSTANCE_METHODS_HMMTRFabricDataSnapshot
- __OBJC_$_INSTANCE_VARIABLES_HMMTRFabricDataSnapshot
- __OBJC_$_PROP_LIST_HMMTRFabricDataSnapshot
- __OBJC_CLASS_RO_$_HMMTRFabricDataSnapshot
- __OBJC_METACLASS_RO_$_HMMTRFabricDataSnapshot
- ___101-[HMMTRAccessoryServer updateAccessoryControlToIncludeAdministratorNodes:sharedUserNodes:completion:]_block_invoke.771
- ___102-[HMMTRAccessoryServer updateAllCharacteristicValuesPostHAPServiceEnumerationForAccessory:completion:]_block_invoke.730
- ___107-[HMMTRAccessoryServerBrowser _fetchDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.197
- ___110-[HMMTRAccessoryServerBrowser removeAllDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.199
- ___111-[HMMTRThreadRadioManager _startAccessoryPairingWithExtendedMACAddress:isWedDevice:accessoryServer:completion:]_block_invoke.23
- ___114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke.843
- ___114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke.846
- ___114-[HMMTRProtocolMap _selectedServiceTypeForServiceArray:device:mtrDevice:endpoint:callbackQueue:completionHandler:]_block_invoke.408
- ___117-[HMMTRAccessoryServer _findSystemCommissionerPairingMatchingSetupPayload:systemCommissionerPairings:pairingManager:]_block_invoke.260
- ___117-[HMMTRAccessoryServer _findSystemCommissionerPairingMatchingSetupPayload:systemCommissionerPairings:pairingManager:]_block_invoke.261
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.487
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.488
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.495
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.493
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_3.494
- ___119-[HMMTRAccessoryServerBrowser removeDevicePairingFabricForSystemCommissionerDeviceWithNodeID:fabric:completionHandler:]_block_invoke.195
- ___154-[HMMTRAccessoryServerBrowser setOperationalFabricData:operationalCertIssuer:storageDataSource:allTargetFabricUUIDs:entityIdentifier:forTargetFabricUUID:]_block_invoke
- ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.308
- ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.309
- ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.312
- ___189-[HMMTRAccessoryServer startStagedPairingWithDeviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:scanningNetworks:completion:]_block_invoke
- ___227-[HMMTRAccessoryServerBrowser stageAccessoryServerWithSetupPayload:fabricID:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:scanningNetworks:completionHandler:]_block_invoke
- ___254-[HMMTRAccessoryServerBrowser _stageAccessoryServerWithSetupPayload:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke
- ___254-[HMMTRAccessoryServerBrowser _stageAccessoryServerWithSetupPayload:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke.182
- ___254-[HMMTRAccessoryServerBrowser _stageAccessoryServerWithSetupPayload:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke_2
- ___30+[HMMTRFabricData logCategory]_block_invoke
- ___37-[HMMTRAccessoryServer finishPairing]_block_invoke.710
- ___37-[HMMTRAccessoryServer timerDidFire:]_block_invoke.280
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.590
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.591
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.592
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.593
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.595
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.599
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.600
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.601
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.602
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.594
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.603
- ___40-[HMMTRStorage _removeAllDataSourceData]_block_invoke.16
- ___42-[HMMTRAccessoryServer _setupMatterDevice]_block_invoke.310
- ___42-[HMMTRAccessoryServer _setupMatterDevice]_block_invoke.312
- ___42-[HMMTRAccessoryServer setupThreadPairing]_block_invoke
- ___42-[HMMTRAccessoryServer setupThreadPairing]_block_invoke.448
- ___43-[HMMTRAccessoryServer _unpair:completion:]_block_invoke.303
- ___43-[HMMTRAccessoryServer discoverAccessories]_block_invoke.306
- ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.821
- ___45-[HMMTRAccessoryServer stopPairingWithError:]_block_invoke.292
- ___45-[HMMTRStorage _syncSetDataSourceDictionary:]_block_invoke.17
- ___47-[HMMTRAccessoryServer processAttributeReport:]_block_invoke.905
- ___47-[HMMTRAccessoryServerBrowser deviceController]_block_invoke
- ___47-[HMMTRStorage handleUpdatedCurrentFabricIndex]_block_invoke
- ___47-[HMMTRStorage handleUpdatedCurrentFabricIndex]_block_invoke.8
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.795
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.798
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.800
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke_2.799
- ___49-[HMMTRAccessoryServerBrowser _deleteOldPairings]_block_invoke
- ___49-[HMMTRAccessoryServerBrowser startBluetoothScan]_block_invoke.353
- ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.754
- ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.758
- ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.759
- ___51-[HMMTRAccessoryServer device:receivedEventReport:]_block_invoke.906
- ___51-[HMMTRStorage handleUpdatedDataWithIsLocalChange:]_block_invoke
- ___51-[HMMTRStorage syncDataSourceDictionary:forFabric:]_block_invoke.18
- ___52-[HMMTRAccessoryServer populateACLEntriesForPairing]_block_invoke.588
- ___52-[HMMTRAccessoryServerBrowser _cleanupStagedServers]_block_invoke.299
- ___52-[HMMTRStorage _handleUpdatedDataWithIsLocalChange:]_block_invoke
- ___53-[HMMTRAccessoryServer _tryPairingUsingMatterSupport]_block_invoke.254
- ___55-[HMMTRAccessoryServer device:receivedAttributeReport:]_block_invoke.904
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.409
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.410
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.411
- ___56-[HMMTRFabricControllerStore cachedWrapperWithFabricID:]_block_invoke
- ___56-[HMMTRFabricControllerStore cachedWrapperWithFabricID:]_block_invoke_2
- ___56-[HMMTRStorage _syncSetDataSourceValuesWithError:block:]_block_invoke.13
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.418
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.422
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.423
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.424
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.848
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.850
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.854
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.856
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.415
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.416
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.417
- ___60-[HMMTRAccessoryServerBrowser handleHomeDeletionWithFabric:]_block_invoke
- ___60-[HMMTRAccessoryServerBrowser handleHomeDeletionWithFabric:]_block_invoke_2
- ___62-[HMMTRAccessoryServerBrowser stopDiscoveringAccessoryServers]_block_invoke.171
- ___63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.752
- ___63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.753
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.469
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.470
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.471
- ___63-[HMMTRAccessoryServerBrowser startDiscoveringAccessoryServers]_block_invoke.168
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.438
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.439
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.440
- ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.868
- ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.869
- ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.870
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.433
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.434
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.435
- ___66-[HMMTRAccessoryServerBrowser setupStorageStateForHomeFabricUUID:]_block_invoke
- ___66-[HMMTRAccessoryServerBrowser storageDidUpdateData:isLocalChange:]_block_invoke
- ___66-[HMMTRAccessoryServerBrowser storageDidUpdateData:isLocalChange:]_block_invoke.339
- ___66-[HMMTRAccessoryServerBrowser storageDidUpdateData:isLocalChange:]_block_invoke.340
- ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.425
- ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.426
- ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.430
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.455
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.456
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.460
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.464
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.465
- ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.398
- ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.403
- ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.404
- ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.405
- ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.172
- ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.175
- ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.177
- ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.179
- ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke_2.178
- ___71-[HMMTRAccessoryServer validateAttestationDeviceInfo:error:completion:]_block_invoke.282
- ___71-[HMMTRThreadRadioManager _retryWEDConnectionToAccessoryWithDelayInMs:]_block_invoke.34
- ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.383
- ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.389
- ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.390
- ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.391
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.449
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.453
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.454
- ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.267
- ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.268
- ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.269
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.747
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.748
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.750
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.751
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.731
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.732
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.742
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.743
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.745
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.746
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.805
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.806
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.810
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke_2.812
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.295
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.299
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.300
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.301
- ___76-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithNodeID:completion:]_block_invoke.180
- ___77-[HMMTRAccessoryServerBrowser handleHomeAddedAccessoryWithNodeID:fabricUUID:]_block_invoke
- ___77-[HMMTRAccessoryServerBrowser setupStorageStateForHomeFabricUUID:completion:]_block_invoke
- ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.392
- ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.396
- ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.397
- ___79-[HMMTRAccessoryServerBrowser _updateAccessoryControlListForServer:completion:]_block_invoke.303
- ___80-[HMMTRAccessoryServer _removeSharedAdminControllerNodeIDFromACLWithCompletion:]_block_invoke
- ___81-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fatalError:]_block_invoke
- ___81-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fatalError:]_block_invoke.301
- ___81-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fatalError:]_block_invoke.302
- ___82-[HMMTRAccessoryServer fetchColorControlClusterForHapAccessory:completionHandler:]_block_invoke.857
- ___82-[HMMTRAccessoryServer fetchColorControlClusterForHapAccessory:completionHandler:]_block_invoke.859
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.825
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.826
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.827
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.830
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke_2.829
- ___83-[HMMTRAccessoryServer updateAccessoryControlToRemoveAdministratorNode:completion:]_block_invoke.772
- ___83-[HMMTRAccessoryServerBrowser getNumberOfAccessoryServersForFabricUUID:completion:]_block_invoke
- ___83-[HMMTRAccessoryServerBrowser getNumberOfAccessoryServersForFabricUUID:completion:]_block_invoke_2
- ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.369
- ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.371
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.831
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.832
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.833
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.834
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.838
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.839
- ___86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.871
- ___86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.872
- ___88-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:keepAliveOnly:]_block_invoke.344
- ___88-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:keepAliveOnly:]_block_invoke.345
- ___88-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:keepAliveOnly:]_block_invoke.346
- ___88-[HMMTRThreadRadioManager connectToAccessoryWithExtendedMACAddress:forRetry:completion:]_block_invoke
- ___88-[HMMTRThreadRadioManager connectToAccessoryWithExtendedMACAddress:forRetry:completion:]_block_invoke.20
- ___88-[HMMTRThreadRadioManager connectToAccessoryWithExtendedMACAddress:forRetry:completion:]_block_invoke_2
- ___88-[HMMTRThreadRadioManager connectToAccessoryWithExtendedMACAddress:forRetry:completion:]_block_invoke_3
- ___90-[HMMTRAccessoryServerBrowser setupStorageStateAndRediscoverAccessoriesForHomeFabricUUID:]_block_invoke
- ___91-[HMMTRProtocolMap servicesForDeviceTypes:device:endpoint:callbackQueue:completionHandler:]_block_invoke.411
- ___92-[HMMTRAccessoryServer _createFirmwareUpdateServiceWithInstanceID:device:completionHandler:]_block_invoke.723
- ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.497
- ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.501
- ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.502
- ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke_2.500
- ___94-[HMMTRAccessoryServer updateAccessoryControlToAdministratorNodes:sharedUserNodes:completion:]_block_invoke.770
- ___96-[HMMTRProtocolMap servicesOfMTRDevice:forDeviceTypes:endpoint:callbackQueue:completionHandler:]_block_invoke.412
- ___97-[HMMTRAccessoryServerBrowser setupStorageStateWithoutRediscoveringAccessoriesForHomeFabricUUID:]_block_invoke
- ___99-[HMMTRAccessoryServer _tryPairingWithOnboardingPayload:systemCommissionerPairings:pairingManager:]_block_invoke.257
- ___99-[HMMTRAccessoryServer _tryPairingWithOnboardingPayload:systemCommissionerPairings:pairingManager:]_block_invoke.258
- ___Block_byref_object_copy_.10442
- ___Block_byref_object_copy_.11120
- ___Block_byref_object_copy_.11801
- ___Block_byref_object_copy_.11998
- ___Block_byref_object_copy_.1467
- ___Block_byref_object_copy_.2816
- ___Block_byref_object_copy_.3096
- ___Block_byref_object_copy_.4116
- ___Block_byref_object_copy_.5269
- ___Block_byref_object_copy_.6917
- ___Block_byref_object_copy_.7268
- ___Block_byref_object_copy_.7688
- ___Block_byref_object_copy_.8772
- ___Block_byref_object_copy_.9722
- ___Block_byref_object_dispose_.10443
- ___Block_byref_object_dispose_.11121
- ___Block_byref_object_dispose_.11802
- ___Block_byref_object_dispose_.11999
- ___Block_byref_object_dispose_.1468
- ___Block_byref_object_dispose_.2817
- ___Block_byref_object_dispose_.3097
- ___Block_byref_object_dispose_.4117
- ___Block_byref_object_dispose_.5270
- ___Block_byref_object_dispose_.6918
- ___Block_byref_object_dispose_.7269
- ___Block_byref_object_dispose_.7689
- ___Block_byref_object_dispose_.8773
- ___Block_byref_object_dispose_.9723
- ___block_descriptor_113_e8_32s40s48s56s64bs72bs80bs88bs96bs104bs_e5_v8?0ls32l8s40l8s48l8s64l8s56l8s72l8s80l8s88l8s96l8s104l8
- ___block_descriptor_32_e40_B16?0"<HMMTRFabricStorageDataSource>"8l
- ___block_descriptor_40_e8_32s_e30_B16?0"HMMTRAccessoryServer"8ls32l8
- ___block_descriptor_40_e8_32s_e32_B16?0"HMMTRControllerWrapper"8ls32l8
- ___block_descriptor_40_e8_32s_e8_v16?0Q8ls32l8
- ___block_descriptor_48_e8_32s40bs_e46_v24?0"HAPThreadNetworkMetadata"8"NSError"16ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e43_{_HMFFutureBlockOutcome=q}16?0"NSArray"8ls32l8s40l8s48l8
- ___block_descriptor_89_e8_32s40bs48bs56bs64bs72bs80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_descriptor_97_e8_32s40s48bs56bs64bs72bs80bs88bs_e45_v28?0B8"HMMTRAccessoryServer"12"NSError"20ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
- ___block_descriptor_97_e8_32s40s48bs56bs64bs72bs80bs88bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
- ___block_literal_global.10181
- ___block_literal_global.1056
- ___block_literal_global.10719
- ___block_literal_global.10942
- ___block_literal_global.11157
- ___block_literal_global.11301
- ___block_literal_global.1134
- ___block_literal_global.11416
- ___block_literal_global.11849
- ___block_literal_global.1341
- ___block_literal_global.156
- ___block_literal_global.1581
- ___block_literal_global.1633
- ___block_literal_global.1680
- ___block_literal_global.17
- ___block_literal_global.1768
- ___block_literal_global.2123
- ___block_literal_global.2265
- ___block_literal_global.2569
- ___block_literal_global.2719
- ___block_literal_global.2748
- ___block_literal_global.2842
- ___block_literal_global.287
- ___block_literal_global.2994
- ___block_literal_global.3189
- ___block_literal_global.3322
- ___block_literal_global.336
- ___block_literal_global.342
- ___block_literal_global.3433
- ___block_literal_global.359
- ___block_literal_global.361.8959
- ___block_literal_global.4206
- ___block_literal_global.4494
- ___block_literal_global.46.9523
- ___block_literal_global.462
- ___block_literal_global.4627
- ___block_literal_global.4728
- ___block_literal_global.482
- ___block_literal_global.4987
- ___block_literal_global.5158
- ___block_literal_global.5395
- ___block_literal_global.5524
- ___block_literal_global.5759
- ___block_literal_global.5793
- ___block_literal_global.5814
- ___block_literal_global.6072
- ___block_literal_global.6084
- ___block_literal_global.6179
- ___block_literal_global.6276
- ___block_literal_global.6372
- ___block_literal_global.6482
- ___block_literal_global.6579
- ___block_literal_global.6676
- ___block_literal_global.6820
- ___block_literal_global.684
- ___block_literal_global.6959
- ___block_literal_global.7068
- ___block_literal_global.7147
- ___block_literal_global.728
- ___block_literal_global.735
- ___block_literal_global.7472
- ___block_literal_global.75.9524
- ___block_literal_global.7699
- ___block_literal_global.780
- ___block_literal_global.8030
- ___block_literal_global.8153
- ___block_literal_global.8803
- ___block_literal_global.913
- ___block_literal_global.9202
- ___block_literal_global.9522
- ___block_literal_global.9599
- ___block_literal_global.964
- ___block_literal_global.99
- _logCategory._hmf_once_t0.1632
- _logCategory._hmf_once_t0.2718
- _logCategory._hmf_once_t0.5157
- _logCategory._hmf_once_t0.5792
- _logCategory._hmf_once_t13.2841
- _logCategory._hmf_once_t13.3188
- _logCategory._hmf_once_t2.4727
- _logCategory._hmf_once_t2.5758
- _logCategory._hmf_once_t2.6819
- _logCategory._hmf_once_t2.9598
- _logCategory._hmf_once_t20.11300
- _logCategory._hmf_once_t23.6178
- _logCategory._hmf_once_t23.6275
- _logCategory._hmf_once_t23.6481
- _logCategory._hmf_once_t23.6578
- _logCategory._hmf_once_t23.6675
- _logCategory._hmf_once_t25
- _logCategory._hmf_once_t3.1055
- _logCategory._hmf_once_t3.1133
- _logCategory._hmf_once_t31.11415
- _logCategory._hmf_once_t363
- _logCategory._hmf_once_t4.3321
- _logCategory._hmf_once_t4.7067
- _logCategory._hmf_once_t6.1679
- _logCategory._hmf_once_t6.1767
- _logCategory._hmf_once_t651
- _logCategory._hmf_once_t8.10941
- _logCategory._hmf_once_t81
- _logCategory._hmf_once_t9.5523
- _logCategory._hmf_once_v1.1634
- _logCategory._hmf_once_v1.2720
- _logCategory._hmf_once_v1.5159
- _logCategory._hmf_once_v1.5794
- _logCategory._hmf_once_v10.5525
- _logCategory._hmf_once_v14.2843
- _logCategory._hmf_once_v14.3190
- _logCategory._hmf_once_v21.11302
- _logCategory._hmf_once_v24.6180
- _logCategory._hmf_once_v24.6277
- _logCategory._hmf_once_v24.6483
- _logCategory._hmf_once_v24.6580
- _logCategory._hmf_once_v24.6677
- _logCategory._hmf_once_v26
- _logCategory._hmf_once_v3.4729
- _logCategory._hmf_once_v3.5760
- _logCategory._hmf_once_v3.6821
- _logCategory._hmf_once_v3.9600
- _logCategory._hmf_once_v32.11417
- _logCategory._hmf_once_v364
- _logCategory._hmf_once_v4.1057
- _logCategory._hmf_once_v4.1135
- _logCategory._hmf_once_v5.3323
- _logCategory._hmf_once_v5.7069
- _logCategory._hmf_once_v652
- _logCategory._hmf_once_v7.1681
- _logCategory._hmf_once_v7.1769
- _logCategory._hmf_once_v82
- _logCategory._hmf_once_v9.10943
- _objc_msgSend$_createCHIPAccessoryForNodeID:
- _objc_msgSend$_createCHIPAccessoryForNodeID:ifPaired:fatalError:
- _objc_msgSend$_currentHomeFabricDeviceController
- _objc_msgSend$_deleteOldPairings
- _objc_msgSend$_handlePerFabricStorageMaybeAvailable:
- _objc_msgSend$_isDevicePaired:
- _objc_msgSend$_nodeIDFromOperationalX509Certificate:
- _objc_msgSend$_restoreCommissioneeInfoBeforeNextPairingAttempt
- _objc_msgSend$_setupStorageStateForHomeFabricUUID:
- _objc_msgSend$_setupStorageStateForUpdatedHomeFabricUUID:
- _objc_msgSend$_setupStorageStateForUpdatedHomeFabricUUID:rediscoverAccessories:
- _objc_msgSend$_setupStorageStateForUpdatedHomeFabricUUID:rediscoverAccessories:overrideAccessoryControlAllowed:
- _objc_msgSend$_setupStorageStateIfNotFabricUUID:rediscoverAccessories:
- _objc_msgSend$_stageAccessoryServerWithSetupPayload:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:
- _objc_msgSend$appleHomeTargetFabricUUIDWithID:
- _objc_msgSend$cachedWrapperWithFabricID:
- _objc_msgSend$connectToAccessoryWithExtendedMACAddress:forRetry:completion:
- _objc_msgSend$currentHomeFabricDeviceControllerWrapper
- _objc_msgSend$didUpdateMatterItems:oldStorage:
- _objc_msgSend$endLocalStorageModeByPersistingAppleFabricData
- _objc_msgSend$enumerateObjectsUsingBlock:
- _objc_msgSend$getNumberOfAccessoryServersForFabricUUID:completion:
- _objc_msgSend$invalidate
- _objc_msgSend$ipkForTargetFabricUUID:forPairing:
- _objc_msgSend$isFabricCreationInProgress
- _objc_msgSend$isSystemCommissionerMode
- _objc_msgSend$legacyNodeIDForCurrentFabric
- _objc_msgSend$legacyNodeIDForTargetFabricUUID:
- _objc_msgSend$matterItemsFromDictionary:
- _objc_msgSend$matterStorageItems
- _objc_msgSend$originalPairingAttemptOperationalCert
- _objc_msgSend$originalPairingAttemptRootCert
- _objc_msgSend$ownerIPK
- _objc_msgSend$pendingMatterStackRestart
- _objc_msgSend$prepareStorageForTargetFabricUUID:
- _objc_msgSend$prepareStorageForTargetFabricUUID:forInitialSetup:
- _objc_msgSend$reloadOperationalFabricData
- _objc_msgSend$restartCount
- _objc_msgSend$setMatterStorageItems:
- _objc_msgSend$setOperationalCert:
- _objc_msgSend$setOriginalPairingAttemptOperationalCert:
- _objc_msgSend$setOriginalPairingAttemptRootCert:
- _objc_msgSend$setOwnerIPK:
- _objc_msgSend$setOwnerNodeID:
- _objc_msgSend$setPendingMatterStackRestart:
- _objc_msgSend$setRestartCount:
- _objc_msgSend$setRootCert:
- _objc_msgSend$setSharedAdmin:
- _objc_msgSend$setSystemCommissionerFabric:
- _objc_msgSend$setSystemCommissionerMode:
- _objc_msgSend$setSystemCommissionerNocSigner:
- _objc_msgSend$setupStorageStateAndRediscoverAccessoriesForHomeFabricUUID:
- _objc_msgSend$setupStorageStateForHomeFabricUUID:
- _objc_msgSend$setupStorageStateForHomeFabricUUID:completion:
- _objc_msgSend$setupThreadPairing
- _objc_msgSend$stageAccessoryServerWithSetupPayload:fabricID:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:scanningNetworks:completionHandler:
- _objc_msgSend$startDiscoveringAccessoryServers
- _objc_msgSend$startStagedPairingWithDeviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:scanningNetworks:completion:
- _objc_msgSend$updateAccessoryControlToRemoveAdministratorNode:completion:
CStrings:
+ "%{public}@Accessory conflicting fabric could not be removed. Failing the pairing"
+ "%{public}@Accessory is in fact paired with node ID %@"
+ "%{public}@Accessory with node ID %@ was added to home with fabric %@, for local control: %@"
+ "%{public}@An error occurred while trying to read EndOfService Alert attribute"
+ "%{public}@An error occurred while trying to read Hardware Fault Alert attribute"
+ "%{public}@Cannot set nil target fabric UUID"
+ "%{public}@Constructed at endpoint %@ a bridged accessory %@"
+ "%{public}@Device wasn't obtained to read fabrics: %@"
+ "%{public}@Device wasn't obtained to remove fabric: %@"
+ "%{public}@EndOfService Alert was read with unexpected class type %@"
+ "%{public}@EndOfService Alert was read with unexpected value %@"
+ "%{public}@Established commissioning session with error %@"
+ "%{public}@Establishing commissioning session to remove fabric"
+ "%{public}@Failed to fetch pairings from device with error: %@"
+ "%{public}@Failed to remove fabric index %@ with error %@"
+ "%{public}@Failed to remove fabric index %@ with status code %@: %@"
+ "%{public}@Failed to set up commissioning session with error: %@"
+ "%{public}@Fetched specification number version data: %@"
+ "%{public}@Handling custom event: %@"
+ "%{public}@Hardware Fault Alert was read with unexpected class type %@"
+ "%{public}@HomeKit Matter is Running in %@ mode"
+ "%{public}@Ignoring setOperationalFabricData call because storage data source is not configured yet"
+ "%{public}@Matter CommissioneeInfo has been read"
+ "%{public}@More than one match was found unexpectedly: %@"
+ "%{public}@No DCL data available, defaulting to static metadata"
+ "%{public}@No Matter device available to read specification version"
+ "%{public}@No match from fetched pairings"
+ "%{public}@No system commissioner pairing manager is available. Retrying pairing directly."
+ "%{public}@Node %@ is removed in a race, server shall not be created while updating discovered accessory servers"
+ "%{public}@Paired CHIP Accessory server %@ matches setupID %@ (isPaired/hasPairings: %@/%@) but will be ignored when searched without identifier"
+ "%{public}@Persisting HomeKitMatter Data for Accessory: %@, system commissioner mode: %@"
+ "%{public}@Received request for staging"
+ "%{public}@Removing the conflicting fabric from the accessory"
+ "%{public}@Retrieved pairings %@, error: %@"
+ "%{public}@Retrying commissioning after removing conflicting fabric"
+ "%{public}@Set up new accessory server: %@"
+ "%{public}@Setting up target Fabric UUID = %@"
+ "%{public}@Starting browse for accessory servers"
+ "%{public}@Successfully removed fabric index %@"
+ "%{public}@There must have been an existing server for node %@, fabric %@"
+ "%{public}@Unknown action to perform after establishing commissioning session"
+ "%{public}@Updating CATs (admin %@, user %@) for FabricID (browser's fabric %@, server's %@"
+ "%{public}@Updating discovered accessory servers for fabric %@ with paired nodes: %@"
+ "%{public}@Updating software version number from %@ to %@"
+ "%{public}@Write Occupied Heating/Cooling Setpoint (sync): Active value was received with unexpected class type %@"
+ "%{public}@Write Occupied Heating/Cooling Setpoint (sync): Control Sequence was read with unexpected class type %@"
+ "%{public}@Write Occupied Heating/Cooling Setpoint (sync): System Mode was read with unexpected class type %@"
+ "%{public}@Write Occupied Heating/Cooling Setpoint (sync): Target Setpoint was received with unexpected class type %@"
+ "%{public}@Write Occupied Heating/Cooling Setpoint (sync): Target State was received with unexpected class type %@"
+ "%{public}@[NewFlow: %@] HMMTRAccessoryServer Handling custom event report=%@"
+ "%{public}@_setupThreadPairing emac %@, isWED=%@"
+ "%{public}@setupThreadPairing - On network commissioning"
+ "%{public}@setupThreadPairing - Waiting for accessory to receive network credentials"
+ "%{public}@setupThreadPairingAfterNetworkCredentials - Network credentials sent to accessory"
+ "%{public}@setupThreadPairingAfterNetworkCredentials - Unexpected state - received commissioneeHasReceivedNetworkCredentials even though accessory was already on-network"
+ "-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fabricUUID:fatalError:]_block_invoke"
+ "00000075-0000-1000-8000-0026BB765291"
+ "4"
+ "@\"HMMTRStorageEventDispatcher\""
+ "@\"MTRSetupPayload\""
+ "@\"NSNumber\"16@?0@\"MTROperationalCredentialsClusterFabricDescriptorStruct\"8"
+ "@44@0:8Q16B24@28^@36"
+ "@48@0:8@16@24B32@36B44"
+ "Available"
+ "B16@?0@\"MTROperationalCredentialsClusterFabricDescriptorStruct\"8"
+ "B24@0:8@\"HMMTRFabricData\"16"
+ "B32@0:8Q16@24"
+ "B48@0:8@16@24@32^@40"
+ "DCL Cache %@"
+ "HAPAccessoryServerPairingProgressStateAddingSystemCommissioner"
+ "HAPAccessoryServerPairingProgressStateAddingWifiCredentialsDone"
+ "HAPAccessoryServerPairingProgressStateAddingWifiCredentialsFailed"
+ "HAPAccessoryServerPairingProgressStateAddingWifiCredentialsStart"
+ "HAPAccessoryServerPairingProgressStateCommissioningStart"
+ "HAPAccessoryServerPairingProgressStateMatterPairingWindowOpeningWithPasscode"
+ "HAPAccessoryServerPairingProgressStateNetworkScanStart"
+ "HAPAccessoryServerPairingProgressStateThreadCredentialsStart"
+ "HH1"
+ "HH2"
+ "HMDHomeManager"
+ "HMMTRCommissioningSessionHandler"
+ "HMMTRStorageEventDispatcher"
+ "HMMTRSyncClusterSmokeCOAlarm"
+ "HomeKitDaemonLegacy.framework"
+ "T@\"HMMTRAccessoryServer\",W,N,V_wedAccessoryServer"
+ "T@\"HMMTRControllerParameters\",&,V_controllerParametersToRemove"
+ "T@\"HMMTRStorageEventDispatcher\",R,N,V_storage"
+ "T@\"MTRSetupPayload\",&,N,V_setupPayloadForPairingUsingMatterSupport"
+ "T@\"NSArray\",R,C,D,N"
+ "T@\"NSArray\",R,C,N"
+ "T@\"NSNumber\",&,V_nodeID"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_clientQueue"
+ "T@\"NSSet\",&,V_allPairedNodeIDs"
+ "T@\"NSUUID\",R,V_fabricUUID"
+ "T@?,C,N,V_stageCommissioneeInfoHandler"
+ "T@?,C,V_completionHandler"
+ "TB,N,V_caseAuthenticatedTagsUpdated"
+ "TB,R,GisSharedAdmin,V_sharedAdmin"
+ "TB,V_dclCacheAvailable"
+ "TB,V_discoveringAccessoryServersRequested"
+ "Unavailable"
+ "_addDiscoveredAccessoryServerWithNodeID:fabricUUID:"
+ "_allPairedNodeIDs"
+ "_caseAuthenticatedTagsUpdated"
+ "_completionHandler"
+ "_connectToAccessoryWithExtendedMACAddress:forRetry:completion:"
+ "_controller:commissioningAndPairedNodeRecoveryComplete:nodeID:abstractMetrics:"
+ "_controllerParametersToRemove"
+ "_convertPairingFailureError:"
+ "_createCHIPAccessoryForNodeID:ifPaired:fabricUUID:fatalError:"
+ "_createSystemCommissionerCHIPAccessoryForNodeID:"
+ "_dclCacheAvailable"
+ "_deleteOldPairingsForFabricUUID:"
+ "_discoveringAccessoryServersRequested"
+ "_isAllowedForRawEventDictionaryHandling:"
+ "_isDevicePaired:fabricUUID:"
+ "_setUpBrowserTargetFabricIfNotFabricUUID:rediscoverAccessories:"
+ "_setUpBrowserTargetFabricUUID:"
+ "_setUpUpdatedBrowserTargetFabricUUID:"
+ "_setUpUpdatedBrowserTargetFabricUUID:rediscoverAccessories:"
+ "_setUpUpdatedBrowserTargetFabricUUID:rediscoverAccessories:overrideAccessoryControlAllowed:"
+ "_setupPayloadForLastCommissioning"
+ "_setupPayloadForPairingUsingMatterSupport"
+ "_setupThreadPairing"
+ "_stageAccessoryServerWithSetupPayload:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:commissioneeInfoHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:"
+ "_stageCommissioneeInfoHandler"
+ "_startDiscoveringAccessoryServersWithNoResponseToDelegate"
+ "_updateDiscoveredAccessoryServersWithNodes:fabricUUID:"
+ "_wedAccessoryServer"
+ "accessoryServer:didReadCommissioneeInfo:"
+ "allPairedNodeIDs"
+ "bundlePath"
+ "caseAuthenticatedTagsUpdated"
+ "clearStaleItems"
+ "completionHandler"
+ "connectToWEDAccessory:completion:"
+ "containsString:"
+ "controllerParametersToRemove"
+ "controllerWrapperForFabricUUID:"
+ "dclCacheAvailable"
+ "deviceBeingCommissionedWithNodeID:error:"
+ "deviceControllerForFabricUUID:"
+ "disconnectFromWEDAccessory:completion:"
+ "discoveringAccessoryServersRequested"
+ "establishSessionToRemoveFabricWithDeviceController:forControllerParameters:setupPayload:nodeID:allPairedNodeIDs:completion:"
+ "handleAttestationComplete"
+ "handleCommissioneeHasReceivedNetworkCredentials"
+ "handleHomeAddedAccessoryWithNodeID:fabricUUID:localControl:"
+ "handleHomeDeletionWithFabricUUID:"
+ "handleRawEventReportDictionary:flow:hapAccessory:"
+ "hmf_enumerateWithAutoreleasePoolUsingBlock:"
+ "hmmtr.cs.handler"
+ "hmmtr.storage.event.dispatcher"
+ "hmmtr.syncsmokecoalarm"
+ "initWithClientQueue:"
+ "initWithQueue:dataSource:systemCommissionerFabric:fabricUUID:sharedAdmin:"
+ "isCurrentDeviceAllowedAccessoryControlDespiteReachableResidentForFabricUUID:"
+ "mapSensorFaultToStatusActive:"
+ "notifyDiscoveredAccessoryServer:"
+ "queryCompleteForAccessory:boardID:error:"
+ "queryCompleteForAccessory:chipID:error:"
+ "queryCompleteForAccessory:chipRevision:error:"
+ "queryCompleteForAccessory:ecid:error:"
+ "queryCompleteForAccessory:enableMixMatch:error:"
+ "queryCompleteForAccessory:epoch:error:"
+ "queryCompleteForAccessory:liveNonce:error:"
+ "queryCompleteForAccessory:manifestPrefix:error:"
+ "queryCompleteForAccessory:nonceHash:error:"
+ "queryCompleteForAccessory:nonceSeed:error:"
+ "queryCompleteForAccessory:productionMode:error:"
+ "queryCompleteForAccessory:securityDomain:error:"
+ "queryCompleteForAccessory:securityMode:error:"
+ "readAttributeEndOfServiceAlertWithParams:"
+ "readAttributeFabricsWithParams:completion:"
+ "readAttributeHardwareFaultAlertWithParams:"
+ "readAttributePluginStatusActiveWithParams:"
+ "readAttributeSpecificationVersionWithParams:"
+ "readFabricsFromDeviceBeingCommissionedWithController:completion:"
+ "readSpecificationVersionWithCompletionHandler:"
+ "removeFabricFromDeviceBeingCommissionedWithController:fabricIndex:completion:"
+ "removeFabricWithParams:completion:"
+ "setAllPairedNodeIDs:"
+ "setCaseAuthenticatedTagsUpdated:"
+ "setCompletionHandler:"
+ "setControllerParametersToRemove:"
+ "setDclCacheAvailable:"
+ "setDiscoveringAccessoryServersRequested:"
+ "setOperationalFabricData:operationalCertIssuer:storageDataSource:allTargetFabricUUIDs:entityIdentifier:accessoryServerNodeIDs:forTargetFabricUUID:"
+ "setSetupPayloadForPairingUsingMatterSupport:"
+ "setStageCommissioneeInfoHandler:"
+ "setUpBrowserTargetFabricAndRediscoverAccessoriesForHomeFabricUUID:"
+ "setUpBrowserTargetFabricUUID:"
+ "setUpBrowserTargetFabricUUID:completion:"
+ "setUpBrowserTargetFabricWithoutRediscoveringAccessoriesForHomeFabricUUID:"
+ "setUpCommissioningSessionWithDeviceController:payload:newNodeID:error:"
+ "setWedAccessoryServer:"
+ "setupPayloadForPairingUsingMatterSupport"
+ "stageAccessoryServerWithSetupPayload:fabricID:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:commissioneeInfoHandler:scanningNetworks:completionHandler:"
+ "stageCommissioneeInfoHandler"
+ "startDiscoveringAccessoryServersWithNoResponseToDelegate"
+ "startStagedPairingWithDeviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:commissioneeInfoHandler:scanningNetworks:completion:"
+ "statusCode"
+ "storageForFabricUUID:sharedAdmin:"
+ "storageForSystemCommissioner"
+ "updateDiscoveredAccessoryServersWithNodes:fabricUUID:"
+ "updatedValuePluginStatusActiveForAttributeReport:responseHandler:"
+ "v24@0:8@\"<HMMTRStorageDataSource>\"16"
+ "v28@0:8@\"HMMTRStorageEventDispatcher\"16B24"
+ "v32@0:8@\"HMMTRAccessoryServer\"16@\"MTRCommissioneeInfo\"24"
+ "v36@0:8@\"UARPAccessory\"16B24@\"NSError\"28"
+ "v40@0:8@\"UARPAccessory\"16@\"NSData\"24@\"NSError\"32"
+ "v40@0:8@\"UARPAccessory\"16Q24@\"NSError\"32"
+ "v76@0:8@?16@?24@?32@?40@?48@?56B64@?68"
+ "v92@0:8@16@24@?32@?40@?48@?56@?64@?72B80@?84"
+ "v96@0:8@16@?24@?32@?40@?48@?56@?64B72B76@80@?88"
+ "wedAccessoryServer"
+ "\xf0\x82\xf0\xf0\xc1\xc1"
- "!Q"
- "%{public}@Accessory with node ID %@ was added to home with fabric %@"
- "%{public}@All nodes to add back after reloading Matter stack: %@"
- "%{public}@CHIP Storage updated. All nodes to add: %@"
- "%{public}@Changing System Commissioner Mode from %@ to %@"
- "%{public}@Constructed bridge accessory %@"
- "%{public}@Current Matter stack is running for fabric %@ and therefore request to handle pairing on fabric %@ cannot be processed"
- "%{public}@Expecting fabric ID to be present"
- "%{public}@Fabric data source not available; failed to get legacy node ID for fabric %@"
- "%{public}@Fabric storage is not available"
- "%{public}@Ignoring updated fabric index notification until fabric creation is successful"
- "%{public}@Invalidating all local servers to force reload them..."
- "%{public}@Matter device controller is unexpectedly inactive when storage is updated"
- "%{public}@Matter stack restart is pending. Deferring re-enumeration"
- "%{public}@No paired devices found. Not restarting matter stack"
- "%{public}@No system commissioner pairing managager is available. Retrying pairing directly."
- "%{public}@Persisting HomeKitMatter Data for Accessory: %@, shared admin: %@, system commissioner mode: %@"
- "%{public}@Received request for staging. Enabling system commissioner mode"
- "%{public}@Removing shared admin controller device's node ID from ACL"
- "%{public}@Setting up storage state for Target Fabric UUID = %@"
- "%{public}@Shutting down the stack"
- "%{public}@Some Matter Items updated in storage, reload the matter stack..."
- "%{public}@Staging is complete. Disabling system commissioner mode"
- "%{public}@Storage has a node that is not yet discovered: %@"
- "%{public}@Storage state cannot be setup without target fabric UUID"
- "%{public}@Storage update handling was deferred - count down %lu"
- "%{public}@Updating CATs (admin %@, user %@) for FabricID (browser's fabric %@, server's %@, storage's %@"
- "%{public}@Updating software version number from from %@ to %@"
- "-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fatalError:]_block_invoke"
- "@\"HMMTRFabricDataSnapshot\""
- "@36@0:8Q16B24^@28"
- "B16@?0@\"HMMTRControllerWrapper\"8"
- "B24@0:8@\"HMMTRFabricDataSnapshot\"16"
- "B24@0:8Q16"
- "Fabric Data"
- "HMMTRFabricDataSnapshot"
- "T@\"HMMTRFabricDataSnapshot\",R,N,V_fabricData"
- "T@\"HMMTRStorage\",R,W,N,V_storage"
- "T@\"HMMTRStorage\",W,N,V_storage"
- "T@\"MTRDeviceController\",R,D"
- "T@\"NSArray\",C,D,N"
- "T@\"NSArray\",C,N"
- "T@\"NSData\",&,N,V_ipk"
- "T@\"NSData\",&,N,V_operationalCert"
- "T@\"NSData\",&,N,V_originalPairingAttemptOperationalCert"
- "T@\"NSData\",&,N,V_originalPairingAttemptRootCert"
- "T@\"NSData\",&,N,V_rootCert"
- "T@\"NSDictionary\",&,V_matterStorageItems"
- "T@\"NSNumber\",&,N,V_residentNodeID"
- "T@\"NSNumber\",&,V_fabricID"
- "TB,GisFabricCreationInProgress,V_fabricCreationInProgress"
- "TB,GisSharedAdmin,V_sharedAdmin"
- "TB,GisSystemCommissionerFabric,V_systemCommissionerFabric"
- "TB,R,GisSystemCommissionerMode,V_systemCommissionerMode"
- "TB,V_pendingMatterStackRestart"
- "_createCHIPAccessoryForNodeID:"
- "_createCHIPAccessoryForNodeID:ifPaired:fatalError:"
- "_currentHomeFabricDeviceController"
- "_deleteOldPairings"
- "_fabricCreationInProgress"
- "_handlePerFabricStorageMaybeAvailable:"
- "_isDevicePaired:"
- "_matterStorageItems"
- "_nodeIDFromOperationalX509Certificate:"
- "_originalPairingAttemptOperationalCert"
- "_originalPairingAttemptRootCert"
- "_pendingMatterStackRestart"
- "_removeSharedAdminControllerNodeIDFromACLWithCompletion:"
- "_restoreCommissioneeInfoBeforeNextPairingAttempt"
- "_setupStorageStateForHomeFabricUUID:"
- "_setupStorageStateForUpdatedHomeFabricUUID:"
- "_setupStorageStateForUpdatedHomeFabricUUID:rediscoverAccessories:"
- "_setupStorageStateForUpdatedHomeFabricUUID:rediscoverAccessories:overrideAccessoryControlAllowed:"
- "_setupStorageStateIfNotFabricUUID:rediscoverAccessories:"
- "_stageAccessoryServerWithSetupPayload:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:"
- "_systemCommissionerMode"
- "appleHomeTargetFabricUUIDWithID:"
- "cachedWrapperWithFabricID:"
- "com.apple.homed"
- "connectToAccessoryWithExtendedMACAddress:forRetry:completion:"
- "controlSequenceNumber"
- "currentHomeFabricDeviceControllerWrapper"
- "enumerateObjectsUsingBlock:"
- "fabricCreationInProgress"
- "getNumberOfAccessoryServersForFabricUUID:completion:"
- "handleHomeAddedAccessoryWithNodeID:fabricUUID:"
- "handleHomeDeletionWithFabric:"
- "hmmtr.fabricData"
- "hmmtrAccessoryPairingDiscoveredOverBLE"
- "invalidate"
- "ipkForCurrentFabric"
- "isFabricCreationInProgress"
- "isHH2Enabled"
- "isSystemCommissionerMode"
- "legacyNodeIDForCurrentFabric"
- "legacyNodeIDForTargetFabricUUID:"
- "matterStorageItems"
- "originalPairingAttemptOperationalCert"
- "originalPairingAttemptRootCert"
- "pendingMatterStackRestart"
- "prepareStorageForTargetFabricUUID:"
- "prepareStorageForTargetFabricUUID:forInitialSetup:"
- "reloadOperationalFabricData"
- "rootCertForCurrentFabric"
- "setFabricCreationInProgress:"
- "setFabricDataItems:"
- "setMatterStorageItems:"
- "setOperationalCert:"
- "setOperationalFabricData:operationalCertIssuer:storageDataSource:allTargetFabricUUIDs:entityIdentifier:forTargetFabricUUID:"
- "setOriginalPairingAttemptOperationalCert:"
- "setOriginalPairingAttemptRootCert:"
- "setPendingMatterStackRestart:"
- "setResidentNodeID:"
- "setRootCert:"
- "setSharedAdmin:"
- "setStorage:"
- "setSystemCommissionerFabric:"
- "setSystemCommissionerMode:"
- "setupStorageStateAndRediscoverAccessoriesForHomeFabricUUID:"
- "setupStorageStateForHomeFabricUUID:"
- "setupStorageStateForHomeFabricUUID:completion:"
- "setupStorageStateWithoutRediscoveringAccessoriesForHomeFabricUUID:"
- "setupThreadPairing"
- "stageAccessoryServerWithSetupPayload:fabricID:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:scanningNetworks:completionHandler:"
- "startStagedPairingWithDeviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:scanningNetworks:completion:"
- "systemCommissionerMode"
- "systemModeNumber"
- "targetHeaterCoolerStateValue"
- "targetSetpointNumber"
- "v16@?0Q8"
- "v24@0:8@\"HMMTRStorage\"16"
- "v24@0:8@\"NSArray\"16"
- "v28@0:8@\"HMMTRStorage\"16B24"
- "v32@0:8@\"NSUUID\"16@?<v@?Q>24"
- "v68@0:8@?16@?24@?32@?40@?48B56@?60"
- "v84@0:8@16@24@?32@?40@?48@?56@?64B72@?76"
- "v88@0:8@16@?24@?32@?40@?48@?56B64B68@72@?80"
- "\xf0\x82\xc1\xf0\xf1\xc1"

```
