## HomeKitMatter

> `/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter`

```diff

-1388.4.13.0.0
-  __TEXT.__text: 0x1465a0
-  __TEXT.__auth_stubs: 0xaa0
-  __TEXT.__objc_methlist: 0xa974
-  __TEXT.__const: 0x180
+1418.5.4.0.0
+  __TEXT.__text: 0x150fc8
+  __TEXT.__auth_stubs: 0xa30
+  __TEXT.__objc_methlist: 0xa69c
+  __TEXT.__const: 0x170
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__gcc_except_tab: 0x2d98
-  __TEXT.__cstring: 0x6e78
-  __TEXT.__oslogstring: 0x28d8c
+  __TEXT.__gcc_except_tab: 0x2d40
+  __TEXT.__cstring: 0x6aaa
+  __TEXT.__oslogstring: 0x28ac9
   __TEXT.__ustring: 0x68
-  __TEXT.__unwind_info: 0x2f90
-  __TEXT.__objc_classname: 0x14b2
-  __TEXT.__objc_methname: 0x26951
-  __TEXT.__objc_methtype: 0x3e7a
-  __TEXT.__objc_stubs: 0x16de0
-  __DATA_CONST.__got: 0x9e0
-  __DATA_CONST.__const: 0x48d0
+  __TEXT.__unwind_info: 0x33c8
+  __TEXT.__objc_classname: 0x14b0
+  __TEXT.__objc_methname: 0x25e60
+  __TEXT.__objc_methtype: 0x3e11
+  __TEXT.__objc_stubs: 0x16780
+  __DATA_CONST.__got: 0x9b0
+  __DATA_CONST.__const: 0x4688
   __DATA_CONST.__objc_classlist: 0x438
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6ef8
+  __DATA_CONST.__objc_selrefs: 0x6cf8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x2f8
-  __DATA_CONST.__objc_arraydata: 0x248
-  __AUTH_CONST.__auth_got: 0x560
-  __AUTH_CONST.__const: 0x10e0
-  __AUTH_CONST.__cfstring: 0x6e00
-  __AUTH_CONST.__objc_const: 0xfbe0
-  __AUTH_CONST.__objc_intobj: 0x1818
+  __DATA_CONST.__objc_arraydata: 0x228
+  __AUTH_CONST.__auth_got: 0x528
+  __AUTH_CONST.__const: 0x10a0
+  __AUTH_CONST.__cfstring: 0x6c80
+  __AUTH_CONST.__objc_const: 0xf920
+  __AUTH_CONST.__objc_intobj: 0x16e0
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x1ea0
-  __DATA.__objc_ivar: 0xb20
+  __AUTH.__objc_data: 0x1db0
+  __DATA.__objc_ivar: 0xaf4
   __DATA.__data: 0xde0
-  __DATA.__bss: 0x470
-  __DATA_DIRTY.__objc_data: 0xb90
-  __DATA_DIRTY.__bss: 0xb8
+  __DATA.__bss: 0x440
+  __DATA_DIRTY.__objc_data: 0xc80
+  __DATA_DIRTY.__bss: 0xd8
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/UARPKit.framework/UARPKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 73863858-FBF5-3637-966E-ED9D8D80D2E3
-  Functions: 4357
-  Symbols:   15045
-  CStrings:  9707
+  UUID: 48AB6EA1-24F2-3C5D-995C-5E2BC50D1165
+  Functions: 4269
+  Symbols:   14770
+  CStrings:  9579
 
Symbols:
+ -[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:deviceName:fromTXTRecord:]
+ -[HMMTRAccessoryServerBrowser _handleAddOrUpdateWithDiscriminator:vendorID:productID:deviceName:overBLE:]
+ -[HMMTRAccessoryServerBrowser _handleBonjourAddOrUpdateWithDiscriminator:vendorID:productID:deviceName:]
+ -[HMMTRAccessoryServerBrowser fetchPreferredThreadCredentialsForStagingWithCompletion:]
+ -[HMMTRAccessoryServerFactory vendAccessoryServerWithNodeID:setupCode:discriminator:category:vendorID:productID:serialNumber:firmwareRevision:deviceName:]
+ -[HMMTRAnnounceOtaSchedulerTimer init:server:endpoint:queue:]
+ -[HMMTRVendorMetadataFileStore _convertUARPMetadataToVendor:uarpProductInfoMetadata:vendorID:productID:]
+ -[HMMTRVendorMetadataFileStore _createUARPProductMetadata:productID:]
+ -[HMMTRVendorMetadataFileStore _createUARPVendorMetadata:vendorID:]
+ -[HMMTRVendorMetadataFileStore _generateRecordName:productID:]
+ -[HMMTRVendorMetadataFileStore _isDataInjectionActive]
+ -[HMMTRVendorMetadataFileStore _retrieveVendorMetadataFromInjectedData:productID:metadata:]
+ -[HMMTRVendorMetadataFileStore _retrieveVendorMetadataUsingNewAPIs:productID:]
+ -[HMMTRVendorMetadataFileStore configureMetaDataService]
+ -[HMMTRVendorMetadataFileStore loadTestInjectedMetadata]
+ -[HMMTRVendorMetadataFileStore setUarpController:]
+ GCC_except_table1008
+ GCC_except_table1012
+ GCC_except_table1014
+ GCC_except_table1138
+ GCC_except_table1198
+ GCC_except_table1244
+ GCC_except_table1252
+ GCC_except_table1301
+ GCC_except_table1309
+ GCC_except_table1346
+ GCC_except_table1383
+ GCC_except_table1412
+ GCC_except_table1606
+ GCC_except_table1647
+ GCC_except_table1799
+ GCC_except_table1800
+ GCC_except_table1801
+ GCC_except_table1804
+ GCC_except_table1824
+ GCC_except_table1825
+ GCC_except_table1834
+ GCC_except_table1835
+ GCC_except_table1836
+ GCC_except_table1837
+ GCC_except_table1838
+ GCC_except_table1839
+ GCC_except_table1840
+ GCC_except_table1899
+ GCC_except_table1905
+ GCC_except_table1982
+ GCC_except_table2094
+ GCC_except_table2096
+ GCC_except_table2126
+ GCC_except_table2134
+ GCC_except_table2136
+ GCC_except_table2180
+ GCC_except_table2220
+ GCC_except_table2282
+ GCC_except_table2535
+ GCC_except_table2539
+ GCC_except_table2595
+ GCC_except_table2636
+ GCC_except_table2677
+ GCC_except_table2679
+ GCC_except_table2704
+ GCC_except_table2706
+ GCC_except_table2728
+ GCC_except_table2729
+ GCC_except_table2730
+ GCC_except_table2731
+ GCC_except_table2732
+ GCC_except_table2733
+ GCC_except_table2734
+ GCC_except_table2735
+ GCC_except_table2747
+ GCC_except_table2749
+ GCC_except_table2790
+ GCC_except_table2796
+ GCC_except_table2807
+ GCC_except_table2810
+ GCC_except_table2814
+ GCC_except_table2829
+ GCC_except_table2832
+ GCC_except_table2836
+ GCC_except_table2838
+ GCC_except_table2857
+ GCC_except_table2864
+ GCC_except_table2869
+ GCC_except_table2881
+ GCC_except_table2933
+ GCC_except_table3310
+ GCC_except_table3311
+ GCC_except_table3312
+ GCC_except_table3316
+ GCC_except_table3321
+ GCC_except_table3324
+ GCC_except_table3340
+ GCC_except_table3355
+ GCC_except_table3431
+ GCC_except_table3433
+ GCC_except_table3440
+ GCC_except_table3441
+ GCC_except_table3470
+ GCC_except_table3504
+ GCC_except_table3512
+ GCC_except_table3531
+ GCC_except_table3534
+ GCC_except_table3571
+ GCC_except_table3575
+ GCC_except_table3592
+ GCC_except_table3594
+ GCC_except_table3612
+ GCC_except_table3689
+ GCC_except_table3736
+ GCC_except_table3754
+ GCC_except_table3777
+ GCC_except_table3781
+ GCC_except_table3796
+ GCC_except_table3797
+ GCC_except_table3798
+ GCC_except_table3804
+ GCC_except_table3811
+ GCC_except_table3869
+ GCC_except_table3889
+ GCC_except_table3931
+ GCC_except_table3936
+ GCC_except_table3939
+ GCC_except_table4022
+ GCC_except_table4023
+ GCC_except_table4078
+ GCC_except_table4081
+ GCC_except_table4143
+ GCC_except_table4205
+ GCC_except_table4209
+ GCC_except_table4213
+ GCC_except_table4216
+ GCC_except_table4249
+ GCC_except_table686
+ GCC_except_table687
+ GCC_except_table744
+ GCC_except_table745
+ GCC_except_table746
+ GCC_except_table821
+ GCC_except_table925
+ GCC_except_table929
+ GCC_except_table931
+ GCC_except_table933
+ GCC_except_table935
+ GCC_except_table939
+ GCC_except_table943
+ GCC_except_table946
+ _HMMTRAnnounceOtaTimerInitiatorTypeAsString
+ _OBJC_IVAR_$_HMMTRVendorMetadataFileStore._injectedDataLock
+ _OBJC_IVAR_$_HMMTRVendorMetadataFileStore._uarpLock
+ ___101-[HMMTRAccessoryServer updateAccessoryControlToIncludeAdministratorNodes:sharedUserNodes:completion:]_block_invoke.860
+ ___102-[HMMTRAccessoryServer updateAllCharacteristicValuesPostHAPServiceEnumerationForAccessory:completion:]_block_invoke.808
+ ___105-[HMMTRAccessoryServerBrowser _handleAddOrUpdateWithDiscriminator:vendorID:productID:deviceName:overBLE:]_block_invoke
+ ___105-[HMMTRAccessoryServerBrowser _handleAddOrUpdateWithDiscriminator:vendorID:productID:deviceName:overBLE:]_block_invoke.172
+ ___107-[HMMTRAccessoryServerBrowser _fetchDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.214
+ ___110-[HMMTRAccessoryServerBrowser removeAllDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.216
+ ___114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke.918
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.531
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.532
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.533
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.534
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.538
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.540
+ ___119-[HMMTRAccessoryServerBrowser removeDevicePairingFabricForSystemCommissionerDeviceWithNodeID:fabric:completionHandler:]_block_invoke.212
+ ___131-[HMMTRDescriptorClusterManager fetchDeviceTypesForEndpoints:device:endpointDeviceTypes:lastError:callbackQueue:completionHandler:]_block_invoke.342
+ ___134-[HMMTRDescriptorClusterManager fetchDeviceTypesForEndpoints:mtrDevice:endpointDeviceTypes:lastError:callbackQueue:completionHandler:]_block_invoke.343
+ ___139-[HMMTRAccessoryServer scheduleOrExecuteOTAProviderAnnouncement:initiatorType:immediateAnnouncement:endpoint:delayCounter:isUserTriggered:]_block_invoke.484
+ ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.337
+ ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.338
+ ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.339
+ ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.340
+ ___198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke.353
+ ___198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke.357
+ ___198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke_2.354
+ ___242-[HMMTRDescriptorClusterManager fetchHAPServicesAtCHIPEndpoint:deviceTopology:endpointDeviceTypes:accessoryInfo:hapToCHIPClusterMappingArray:device:isBridge:bridgeAggregateNodeEndpoint:isComposedDevice:server:callbackQueue:completionHandler:]_block_invoke.317
+ ___278-[HMMTRAccessoryServerBrowser _stageAccessoryServerWithSetupPayload:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:commissioneeInfoHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke.199
+ ___280-[HMMTRDescriptorClusterManager _verifyHAPCharacteristicSupportAtCHIPEndpoint:device:endpointDeviceTypes:callbackQueue:clusterClassToQueryForFeatureMap:hapServicesToCheckForFeatureMap:hapServicesInUse:deviceTopology:bridgeAggregateNodeEndpoint:server:lastError:completionHandler:]_block_invoke.296
+ ___37-[HMMTRAccessoryServer finishPairing]_block_invoke.788
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.663
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.664
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.672
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.673
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.667
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.676
+ ___40-[HMMTRAccessoryServerBrowser configure]_block_invoke.141
+ ___43-[HMMTRAccessoryServer _setupThreadPairing]_block_invoke.493
+ ___47-[HMMTRAccessoryServer processAttributeReport:]_block_invoke.987
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.884
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.888
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke_2.887
+ ___49-[HMMTRAccessoryServerBrowser startBluetoothScan]_block_invoke.369
+ ___51-[HMMTRAccessoryServer device:receivedEventReport:]_block_invoke.988
+ ___52-[HMMTRAccessoryServer populateACLEntriesForPairing]_block_invoke.661
+ ___52-[HMMTRAccessoryServerBrowser _cleanupStagedServers]_block_invoke.322
+ ___55-[HMMTRAccessoryServer device:receivedAttributeReport:]_block_invoke.986
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.923
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.925
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.929
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.931
+ ___62-[HMMTRAccessoryServerBrowser stopDiscoveringAccessoryServers]_block_invoke.188
+ ___63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.838
+ ___63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.839
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.511
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.512
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.513
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.514
+ ___64-[HMMTRAccessoryServer _commissioning:complete:abstractMetrics:]_block_invoke.946
+ ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.951
+ ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.952
+ ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.953
+ ___64-[HMMTRAccessoryServerBrowser _initializeAndStartBonjourBrowser]_block_invoke.149
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.500
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.501
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.502
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.510
+ ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.189
+ ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.192
+ ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.194
+ ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.196
+ ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke_2.195
+ ___70-[HMMTRAccessoryServer _onThreadScanResults:commissioning:completion:]_block_invoke.895
+ ___70-[HMMTRAccessoryServer _onThreadScanResults:commissioning:completion:]_block_invoke.896
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.494
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.495
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.496
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.832
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.833
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.836
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.837
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke_2.834
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.809
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.810
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.819
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.827
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.828
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.831
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke_2.823
+ ___76-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithNodeID:completion:]_block_invoke.197
+ ___79-[HMMTRAccessoryServerBrowser _updateAccessoryControlListForServer:completion:]_block_invoke.327
+ ___82-[HMMTRAccessoryServer fetchColorControlClusterForHapAccessory:completionHandler:]_block_invoke.932
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.900
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.901
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.902
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke_2.904
+ ___83-[HMMTRAccessoryServer updateAccessoryControlToRemoveAdministratorNode:completion:]_block_invoke.861
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.906
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.907
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.908
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.913
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.914
+ ___86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.954
+ ___86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.955
+ ___87-[HMMTRAccessoryServerBrowser fetchPreferredThreadCredentialsForStagingWithCompletion:]_block_invoke
+ ___88-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:keepAliveOnly:]_block_invoke.361
+ ___88-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:keepAliveOnly:]_block_invoke.362
+ ___88-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:keepAliveOnly:]_block_invoke.363
+ ___92-[HMMTRAccessoryServer _createFirmwareUpdateServiceWithInstanceID:device:completionHandler:]_block_invoke.801
+ ___92-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fabricUUID:fatalError:]_block_invoke.325
+ ___92-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fabricUUID:fatalError:]_block_invoke.326
+ ___93-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:deviceName:fromTXTRecord:]_block_invoke
+ ___93-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:deviceName:fromTXTRecord:]_block_invoke.161
+ ___93-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:deviceName:fromTXTRecord:]_block_invoke.163
+ ___93-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:deviceName:fromTXTRecord:]_block_invoke.165
+ ___94-[HMMTRAccessoryServer updateAccessoryControlToAdministratorNodes:sharedUserNodes:completion:]_block_invoke.859
+ ___96-[HMMTRDescriptorClusterManager endpointForClusterID:mtrDevice:callbackQueue:completionHandler:]_block_invoke.393
+ ___97-[HMMTRAccessoryServerBrowser removeAccessoryServer:fromDiscoveredAccessoryServerListWithReason:]_block_invoke.310
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.542
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.543
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.544
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.545
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.550
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.551
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke_2.546
+ ___Block_byref_object_copy_.10550
+ ___Block_byref_object_copy_.11223
+ ___Block_byref_object_copy_.11846
+ ___Block_byref_object_copy_.12534
+ ___Block_byref_object_copy_.12698
+ ___Block_byref_object_copy_.1999
+ ___Block_byref_object_copy_.3560
+ ___Block_byref_object_copy_.3849
+ ___Block_byref_object_copy_.4894
+ ___Block_byref_object_copy_.6068
+ ___Block_byref_object_copy_.7968
+ ___Block_byref_object_copy_.8407
+ ___Block_byref_object_copy_.9577
+ ___Block_byref_object_dispose_.10551
+ ___Block_byref_object_dispose_.11224
+ ___Block_byref_object_dispose_.11847
+ ___Block_byref_object_dispose_.12535
+ ___Block_byref_object_dispose_.12699
+ ___Block_byref_object_dispose_.2000
+ ___Block_byref_object_dispose_.3561
+ ___Block_byref_object_dispose_.3850
+ ___Block_byref_object_dispose_.4895
+ ___Block_byref_object_dispose_.6069
+ ___Block_byref_object_dispose_.7969
+ ___Block_byref_object_dispose_.8408
+ ___Block_byref_object_dispose_.9578
+ ___block_descriptor_73_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.10016
+ ___block_literal_global.103
+ ___block_literal_global.10341
+ ___block_literal_global.10417
+ ___block_literal_global.1091
+ ___block_literal_global.11044
+ ___block_literal_global.114
+ ___block_literal_global.11496
+ ___block_literal_global.11666
+ ___block_literal_global.11880
+ ___block_literal_global.12078
+ ___block_literal_global.1209
+ ___block_literal_global.12136
+ ___block_literal_global.12354
+ ___block_literal_global.1314
+ ___block_literal_global.1473
+ ___block_literal_global.1531
+ ___block_literal_global.1625
+ ___block_literal_global.1872
+ ___block_literal_global.2217
+ ___block_literal_global.2272
+ ___block_literal_global.2319
+ ___block_literal_global.2406
+ ___block_literal_global.2766
+ ___block_literal_global.2883
+ ___block_literal_global.3020
+ ___block_literal_global.316
+ ___block_literal_global.319
+ ___block_literal_global.3321
+ ___block_literal_global.337
+ ___block_literal_global.3465
+ ___block_literal_global.3494
+ ___block_literal_global.358.9449
+ ___block_literal_global.3586
+ ___block_literal_global.3741
+ ___block_literal_global.377
+ ___block_literal_global.3937
+ ___block_literal_global.400
+ ___block_literal_global.4071
+ ___block_literal_global.4193
+ ___block_literal_global.4673
+ ___block_literal_global.490
+ ___block_literal_global.4991
+ ___block_literal_global.5279
+ ___block_literal_global.5416
+ ___block_literal_global.547
+ ___block_literal_global.549
+ ___block_literal_global.549.11142
+ ___block_literal_global.5519
+ ___block_literal_global.552
+ ___block_literal_global.563
+ ___block_literal_global.5783
+ ___block_literal_global.5956
+ ___block_literal_global.612
+ ___block_literal_global.6199
+ ___block_literal_global.6327
+ ___block_literal_global.6469
+ ___block_literal_global.65
+ ___block_literal_global.6579
+ ___block_literal_global.6613
+ ___block_literal_global.6634
+ ___block_literal_global.6884
+ ___block_literal_global.6897
+ ___block_literal_global.6991
+ ___block_literal_global.7085
+ ___block_literal_global.7179
+ ___block_literal_global.7282
+ ___block_literal_global.7376
+ ___block_literal_global.75.10342
+ ___block_literal_global.7515
+ ___block_literal_global.7656
+ ___block_literal_global.7758
+ ___block_literal_global.7829
+ ___block_literal_global.80
+ ___block_literal_global.806
+ ___block_literal_global.813
+ ___block_literal_global.8190
+ ___block_literal_global.822
+ ___block_literal_global.826
+ ___block_literal_global.8418
+ ___block_literal_global.857
+ ___block_literal_global.8767
+ ___block_literal_global.8885
+ ___block_literal_global.9016
+ ___block_literal_global.909
+ ___block_literal_global.9609
+ ___block_literal_global.995
+ _logCategory._hmf_once_t0.2271
+ _logCategory._hmf_once_t0.3464
+ _logCategory._hmf_once_t0.5955
+ _logCategory._hmf_once_t0.6612
+ _logCategory._hmf_once_t1.5415
+ _logCategory._hmf_once_t10.1472
+ _logCategory._hmf_once_t12
+ _logCategory._hmf_once_t120
+ _logCategory._hmf_once_t13.3585
+ _logCategory._hmf_once_t13.3936
+ _logCategory._hmf_once_t14.1224
+ _logCategory._hmf_once_t14.6896
+ _logCategory._hmf_once_t14.6990
+ _logCategory._hmf_once_t14.7084
+ _logCategory._hmf_once_t14.7281
+ _logCategory._hmf_once_t14.7375
+ _logCategory._hmf_once_t14.7514
+ _logCategory._hmf_once_t15
+ _logCategory._hmf_once_t196
+ _logCategory._hmf_once_t2.10416
+ _logCategory._hmf_once_t2.5518
+ _logCategory._hmf_once_t2.6578
+ _logCategory._hmf_once_t2.7655
+ _logCategory._hmf_once_t20.12077
+ _logCategory._hmf_once_t26.7178
+ _logCategory._hmf_once_t3.1313
+ _logCategory._hmf_once_t3.1530
+ _logCategory._hmf_once_t3.2882
+ _logCategory._hmf_once_t31.12135
+ _logCategory._hmf_once_t4.4070
+ _logCategory._hmf_once_t6.2405
+ _logCategory._hmf_once_t6.4192
+ _logCategory._hmf_once_t677
+ _logCategory._hmf_once_t70
+ _logCategory._hmf_once_t8.11665
+ _logCategory._hmf_once_v1.2273
+ _logCategory._hmf_once_v1.3466
+ _logCategory._hmf_once_v1.5957
+ _logCategory._hmf_once_v1.6614
+ _logCategory._hmf_once_v11.1474
+ _logCategory._hmf_once_v121
+ _logCategory._hmf_once_v13
+ _logCategory._hmf_once_v14.3587
+ _logCategory._hmf_once_v14.3938
+ _logCategory._hmf_once_v15.1225
+ _logCategory._hmf_once_v15.6898
+ _logCategory._hmf_once_v15.6992
+ _logCategory._hmf_once_v15.7086
+ _logCategory._hmf_once_v15.7283
+ _logCategory._hmf_once_v15.7377
+ _logCategory._hmf_once_v15.7516
+ _logCategory._hmf_once_v16
+ _logCategory._hmf_once_v197
+ _logCategory._hmf_once_v2.5417
+ _logCategory._hmf_once_v21.12079
+ _logCategory._hmf_once_v27.7180
+ _logCategory._hmf_once_v3.10418
+ _logCategory._hmf_once_v3.5520
+ _logCategory._hmf_once_v3.6580
+ _logCategory._hmf_once_v3.7657
+ _logCategory._hmf_once_v32.12137
+ _logCategory._hmf_once_v4.1315
+ _logCategory._hmf_once_v4.1532
+ _logCategory._hmf_once_v4.2884
+ _logCategory._hmf_once_v5.4072
+ _logCategory._hmf_once_v678
+ _logCategory._hmf_once_v7.2407
+ _logCategory._hmf_once_v7.4194
+ _logCategory._hmf_once_v71
+ _logCategory._hmf_once_v9.11667
+ _objc_msgSend$_convertUARPMetadataToVendor:uarpProductInfoMetadata:vendorID:productID:
+ _objc_msgSend$_createUARPProductMetadata:productID:
+ _objc_msgSend$_createUARPVendorMetadata:vendorID:
+ _objc_msgSend$_discriminator:vendorID:productID:CM:deviceName:fromTXTRecord:
+ _objc_msgSend$_generateRecordName:productID:
+ _objc_msgSend$_handleAddOrUpdateWithDiscriminator:vendorID:productID:deviceName:overBLE:
+ _objc_msgSend$_handleBonjourAddOrUpdateWithDiscriminator:vendorID:productID:deviceName:
+ _objc_msgSend$_isDataInjectionActive
+ _objc_msgSend$_retrieveVendorMetadataFromInjectedData:productID:metadata:
+ _objc_msgSend$_retrieveVendorMetadataUsingNewAPIs:productID:
+ _objc_msgSend$accessoryServerBrowser:getThreadNetworkCredentialsForStagingWithCompletion:
+ _objc_msgSend$copyChipMetadataForRecordName:
+ _objc_msgSend$discoveryCapabilities
+ _objc_msgSend$fetchPreferredThreadCredentialsForStagingWithCompletion:
+ _objc_msgSend$init:server:endpoint:queue:
+ _objc_msgSend$initWithUUID:nodeID:vendorID:productID:deviceType:serialNumber:name:setupPayload:
+ _objc_msgSend$loadTestInjectedMetadata
+ _objc_msgSend$setupPasscode
+ _objc_msgSend$subscribeForChipSupportedAccessories
+ _objc_msgSend$vendAccessoryServerWithNodeID:setupCode:discriminator:category:vendorID:productID:serialNumber:firmwareRevision:deviceName:
- +[HMMTRFeatures disableFeatureMatterHRAPDeviceTypesForTests]
- +[HMMTRFeatures disableFeatureMatterRVCForTests]
- +[HMMTRFeatures enableFeatureMatterHRAPDeviceTypesForTests]
- +[HMMTRFeatures enableFeatureMatterRVCForTests]
- +[HMMTRFeatures unsetFeatureMatterHRAPDeviceTypesForTests]
- +[HMMTRFeatures unsetFeatureMatterRVCForTests]
- -[HMMTRAccessoryServer _initializeCredentialManagementForCommissioneeNodeID:storage:]
- -[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]
- -[HMMTRAccessoryServerBrowser _handleAddOrUpdateWithDiscriminator:vendorID:productID:overBLE:]
- -[HMMTRAccessoryServerBrowser _handleBonjourAddOrUpdateWithDiscriminator:vendorID:productID:]
- -[HMMTRAccessoryServerFactory vendAccessoryServerWithNodeID:setupCode:discriminator:category:vendorID:productID:serialNumber:firmwareRevision:]
- -[HMMTRAnnounceOtaSchedulerTimer init:server:nodeID:endpoint:queue:]
- -[HMMTRAnnounceOtaSchedulerTimer nodeID]
- -[HMMTRAnnounceOtaSchedulerTimer setNodeID:]
- -[HMMTRStorage(Records) setThreadCredentialManagementEnabled:forSystemCommissionerFabricNode:]
- -[HMMTRStorage(Records) setThreadCredentialManagementEndpoint:forSystemCommissionerFabricNode:]
- -[HMMTRStorage(Records) threadCredentialManagementEnabledForSystemCommissionerFabricNode:]
- -[HMMTRStorage(Records) threadCredentialManagementEndpointForSystemCommissionerFabricNode:]
- -[HMMTRStorage(Records) threadCredentialManagementNodesAndEndpointsForSystemCommissioner]
- -[HMMTRSystemCommissionerPairingManager _addNetworkToThreadNetworkDirectoryForDevice:endpoint:dataset:]
- -[HMMTRSystemCommissionerPairingManager _armFailSafeForDevice:expiryLengthSeconds:]
- -[HMMTRSystemCommissionerPairingManager _augmentDatasetWithBorderAgentIDsForDevice:endpoint:dataset:]
- -[HMMTRSystemCommissionerPairingManager _commissioningCompleteForDevice:]
- -[HMMTRSystemCommissionerPairingManager _deviceForSystemCommissionerNode:]
- -[HMMTRSystemCommissionerPairingManager _donateThreadNetwork:toSystemCommissionerNode:endpoint:]
- -[HMMTRSystemCommissionerPairingManager _donateThreadNetworksToSystemCommissionerNode:endpoint:]
- -[HMMTRSystemCommissionerPairingManager _provisionBorderRouterWithSystemCommissionerNode:endpoint:dataset:]
- -[HMMTRSystemCommissionerPairingManager _retrievePreferredThreadCredentialsOrCreateWithDataset:]
- -[HMMTRSystemCommissionerPairingManager _retrieveTHClientPreferredNetworkInternallyOnMdnsAndSig]
- -[HMMTRSystemCommissionerPairingManager _retrieveThreadCredentialsFromSystemCommissionerNode:endpoint:]
- -[HMMTRSystemCommissionerPairingManager _setActiveThreadDatasetForDevice:endpoint:dataset:]
- -[HMMTRSystemCommissionerPairingManager _updateThreadCredentialManagementEnabled:forSystemCommissionerPairingUUID:completionHandler:]
- -[HMMTRSystemCommissionerPairingManager retrievePreferredThreadCredentialsOrCreateWithDataset:completionHandler:]
- -[HMMTRSystemCommissionerPairingManager updateThreadCredentialManagementEnabled:forSystemCommissionerPairingUUID:completionHandler:]
- -[HMMTRVendorMetadataFileStore _addProductInfoToMetadata:accessories:]
- -[HMMTRVendorMetadataFileStore _addVendorInfoToMetadata:accessories:]
- -[HMMTRVendorMetadataFileStore _handleCloudMetadataFetchFailure]
- -[HMMTRVendorMetadataFileStore _handleCloudMetadataFetchSuccess]
- -[HMMTRVendorMetadataFileStore _prepopulateCacheForKnownAccessories:]
- -[HMMTRVendorMetadataFileStore _processSupportedAccessories:]
- -[HMMTRVendorMetadataFileStore _retrieveVendorMetadataForVendorID:productID:metadata:]
- -[HMMTRVendorMetadataFileStore _saveMetadata:]
- -[HMMTRVendorMetadataFileStore attemptCloudMetadataFetch]
- -[HMMTRVendorMetadataFileStore batchedAccessories]
- -[HMMTRVendorMetadataFileStore cancelCloudMetadataFetch]
- -[HMMTRVendorMetadataFileStore dclCacheAvailable]
- -[HMMTRVendorMetadataFileStore delegate]
- -[HMMTRVendorMetadataFileStore fetchCloudMetadata]
- -[HMMTRVendorMetadataFileStore fetchInProgress]
- -[HMMTRVendorMetadataFileStore firstFailureTime]
- -[HMMTRVendorMetadataFileStore initWithFileURL:uarpController:fileManager:preferences:]
- -[HMMTRVendorMetadataFileStore logIdentifier]
- -[HMMTRVendorMetadataFileStore metadata]
- -[HMMTRVendorMetadataFileStore overrideMetadata]
- -[HMMTRVendorMetadataFileStore retryCount]
- -[HMMTRVendorMetadataFileStore retryIntervalOverride]
- -[HMMTRVendorMetadataFileStore retryQueue]
- -[HMMTRVendorMetadataFileStore retryTimer]
- -[HMMTRVendorMetadataFileStore sendMessageToAccessory:uarpMsg:error:]
- -[HMMTRVendorMetadataFileStore setBatchedAccessories:]
- -[HMMTRVendorMetadataFileStore setDclCacheAvailable:]
- -[HMMTRVendorMetadataFileStore setDelegate:]
- -[HMMTRVendorMetadataFileStore setFetchInProgress:]
- -[HMMTRVendorMetadataFileStore setFirstFailureTime:]
- -[HMMTRVendorMetadataFileStore setRetryCount:]
- -[HMMTRVendorMetadataFileStore setRetryIntervalOverride:]
- -[HMMTRVendorMetadataFileStore setRetryTimer:]
- -[HMMTRVendorMetadataFileStore staticMetadataFileURL]
- -[HMMTRVendorMetadataFileStore staticMetadata]
- -[HMMTRVendorMetadataFileStore supportedAccessories:forProductGroup:isComplete:]
- -[HMMTRVendorMetadataFileStore timerDidFire:]
- -[HMMTRVendorMetadataFileStore vendorMetadataCache]
- -[HMMTRVendorMetadataVendor invalid]
- -[HMMTRVendorMetadataVendor setInvalid:]
- GCC_except_table1030
- GCC_except_table1034
- GCC_except_table1036
- GCC_except_table1163
- GCC_except_table1223
- GCC_except_table1269
- GCC_except_table1277
- GCC_except_table1326
- GCC_except_table1334
- GCC_except_table1371
- GCC_except_table1408
- GCC_except_table1437
- GCC_except_table1633
- GCC_except_table1674
- GCC_except_table1851
- GCC_except_table1852
- GCC_except_table1853
- GCC_except_table1854
- GCC_except_table1855
- GCC_except_table1858
- GCC_except_table1861
- GCC_except_table1862
- GCC_except_table1863
- GCC_except_table1864
- GCC_except_table1865
- GCC_except_table1866
- GCC_except_table1867
- GCC_except_table1926
- GCC_except_table1932
- GCC_except_table1970
- GCC_except_table2045
- GCC_except_table2157
- GCC_except_table2159
- GCC_except_table2189
- GCC_except_table2197
- GCC_except_table2199
- GCC_except_table2243
- GCC_except_table2283
- GCC_except_table2345
- GCC_except_table2606
- GCC_except_table2610
- GCC_except_table2664
- GCC_except_table2746
- GCC_except_table2748
- GCC_except_table2773
- GCC_except_table2775
- GCC_except_table2797
- GCC_except_table2798
- GCC_except_table2799
- GCC_except_table2800
- GCC_except_table2801
- GCC_except_table2802
- GCC_except_table2803
- GCC_except_table2804
- GCC_except_table2816
- GCC_except_table2818
- GCC_except_table2843
- GCC_except_table2859
- GCC_except_table2865
- GCC_except_table2876
- GCC_except_table2879
- GCC_except_table2883
- GCC_except_table2898
- GCC_except_table2901
- GCC_except_table2905
- GCC_except_table2907
- GCC_except_table2926
- GCC_except_table2937
- GCC_except_table2949
- GCC_except_table3000
- GCC_except_table3001
- GCC_except_table3378
- GCC_except_table3379
- GCC_except_table3380
- GCC_except_table3384
- GCC_except_table3389
- GCC_except_table3392
- GCC_except_table3408
- GCC_except_table3491
- GCC_except_table3499
- GCC_except_table3508
- GCC_except_table3509
- GCC_except_table3538
- GCC_except_table3569
- GCC_except_table3572
- GCC_except_table3580
- GCC_except_table3599
- GCC_except_table3602
- GCC_except_table3640
- GCC_except_table3644
- GCC_except_table3661
- GCC_except_table3663
- GCC_except_table3681
- GCC_except_table3758
- GCC_except_table3805
- GCC_except_table3823
- GCC_except_table3846
- GCC_except_table3850
- GCC_except_table3865
- GCC_except_table3866
- GCC_except_table3867
- GCC_except_table3873
- GCC_except_table3880
- GCC_except_table3938
- GCC_except_table3958
- GCC_except_table4019
- GCC_except_table4024
- GCC_except_table4027
- GCC_except_table4110
- GCC_except_table4111
- GCC_except_table4166
- GCC_except_table4169
- GCC_except_table4231
- GCC_except_table4293
- GCC_except_table4297
- GCC_except_table4301
- GCC_except_table4304
- GCC_except_table4337
- GCC_except_table703
- GCC_except_table710
- GCC_except_table714
- GCC_except_table718
- GCC_except_table720
- GCC_except_table722
- GCC_except_table723
- GCC_except_table785
- GCC_except_table786
- GCC_except_table787
- GCC_except_table903
- GCC_except_table966
- GCC_except_table970
- GCC_except_table972
- GCC_except_table974
- GCC_except_table976
- GCC_except_table980
- GCC_except_table984
- GCC_except_table987
- _HMMTRAnnounceOtaTimerInitatorTypeAsString
- _HMMTRVendorMetadataFileName
- _HM_FEATURE_RVC_DEFAULTS_ENABLED
- _OBJC_CLASS_$_MTRBaseClusterThreadBorderRouterManagement
- _OBJC_CLASS_$_MTRBaseClusterThreadNetworkDirectory
- _OBJC_CLASS_$_MTRThreadBorderRouterManagementClusterSetActiveDatasetRequestParams
- _OBJC_CLASS_$_MTRThreadNetworkDirectoryClusterAddNetworkParams
- _OBJC_CLASS_$_MTSNetworkCredentialManager
- _OBJC_CLASS_$_MTSThreadNetworkCredential
- _OBJC_IVAR_$_HMMTRAnnounceOtaSchedulerTimer._nodeID
- _OBJC_IVAR_$_HMMTRVendorMetadataFileStore._batchedAccessories
- _OBJC_IVAR_$_HMMTRVendorMetadataFileStore._dclCacheAvailable
- _OBJC_IVAR_$_HMMTRVendorMetadataFileStore._delegate
- _OBJC_IVAR_$_HMMTRVendorMetadataFileStore._fetchInProgress
- _OBJC_IVAR_$_HMMTRVendorMetadataFileStore._firstFailureTime
- _OBJC_IVAR_$_HMMTRVendorMetadataFileStore._lock
- _OBJC_IVAR_$_HMMTRVendorMetadataFileStore._retryCount
- _OBJC_IVAR_$_HMMTRVendorMetadataFileStore._retryIntervalOverride
- _OBJC_IVAR_$_HMMTRVendorMetadataFileStore._retryQueue
- _OBJC_IVAR_$_HMMTRVendorMetadataFileStore._retryTimer
- _OBJC_IVAR_$_HMMTRVendorMetadataFileStore._vendorMetadataCache
- _OBJC_IVAR_$_HMMTRVendorMetadataVendor._invalid
- ___101-[HMMTRAccessoryServer updateAccessoryControlToIncludeAdministratorNodes:sharedUserNodes:completion:]_block_invoke.862
- ___101-[HMMTRSystemCommissionerPairingManager _augmentDatasetWithBorderAgentIDsForDevice:endpoint:dataset:]_block_invoke
- ___102-[HMMTRAccessoryServer updateAllCharacteristicValuesPostHAPServiceEnumerationForAccessory:completion:]_block_invoke.810
- ___103-[HMMTRSystemCommissionerPairingManager _retrieveThreadCredentialsFromSystemCommissionerNode:endpoint:]_block_invoke
- ___103-[HMMTRSystemCommissionerPairingManager _retrieveThreadCredentialsFromSystemCommissionerNode:endpoint:]_block_invoke.66
- ___107-[HMMTRAccessoryServerBrowser _fetchDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.213
- ___107-[HMMTRSystemCommissionerPairingManager _provisionBorderRouterWithSystemCommissionerNode:endpoint:dataset:]_block_invoke
- ___107-[HMMTRSystemCommissionerPairingManager _provisionBorderRouterWithSystemCommissionerNode:endpoint:dataset:]_block_invoke.68
- ___107-[HMMTRSystemCommissionerPairingManager _provisionBorderRouterWithSystemCommissionerNode:endpoint:dataset:]_block_invoke_2
- ___107-[HMMTRSystemCommissionerPairingManager _provisionBorderRouterWithSystemCommissionerNode:endpoint:dataset:]_block_invoke_3
- ___110-[HMMTRAccessoryServerBrowser removeAllDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.215
- ___113-[HMMTRSystemCommissionerPairingManager retrievePreferredThreadCredentialsOrCreateWithDataset:completionHandler:]_block_invoke
- ___114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke.924
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.538
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.540
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.543
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.545
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.542
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.544
- ___119-[HMMTRAccessoryServerBrowser removeDevicePairingFabricForSystemCommissionerDeviceWithNodeID:fabric:completionHandler:]_block_invoke.211
- ___131-[HMMTRDescriptorClusterManager fetchDeviceTypesForEndpoints:device:endpointDeviceTypes:lastError:callbackQueue:completionHandler:]_block_invoke.350
- ___132-[HMMTRSystemCommissionerPairingManager updateThreadCredentialManagementEnabled:forSystemCommissionerPairingUUID:completionHandler:]_block_invoke
- ___134-[HMMTRDescriptorClusterManager fetchDeviceTypesForEndpoints:mtrDevice:endpointDeviceTypes:lastError:callbackQueue:completionHandler:]_block_invoke.351
- ___139-[HMMTRAccessoryServer scheduleOrExecuteOTAProviderAnnouncement:initiatorType:immediateAnnouncement:endpoint:delayCounter:isUserTriggered:]_block_invoke.488
- ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.328
- ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.329
- ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.331
- ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.334
- ___198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke.361
- ___198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke.365
- ___198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke_2.362
- ___242-[HMMTRDescriptorClusterManager fetchHAPServicesAtCHIPEndpoint:deviceTopology:endpointDeviceTypes:accessoryInfo:hapToCHIPClusterMappingArray:device:isBridge:bridgeAggregateNodeEndpoint:isComposedDevice:server:callbackQueue:completionHandler:]_block_invoke.325
- ___278-[HMMTRAccessoryServerBrowser _stageAccessoryServerWithSetupPayload:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:commissioneeInfoHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke.198
- ___280-[HMMTRDescriptorClusterManager _verifyHAPCharacteristicSupportAtCHIPEndpoint:device:endpointDeviceTypes:callbackQueue:clusterClassToQueryForFeatureMap:hapServicesToCheckForFeatureMap:hapServicesInUse:deviceTopology:bridgeAggregateNodeEndpoint:server:lastError:completionHandler:]_block_invoke.304
- ___37-[HMMTRAccessoryServer finishPairing]_block_invoke.790
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.667
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.670
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.676
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.677
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.669
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.678
- ___40-[HMMTRAccessoryServerBrowser configure]_block_invoke.142
- ___43-[HMMTRAccessoryServer _setupThreadPairing]_block_invoke.497
- ___45-[HMMTRVendorMetadataFileStore timerDidFire:]_block_invoke
- ___47-[HMMTRAccessoryServer processAttributeReport:]_block_invoke.990
- ___47-[HMMTRAnnounceOtaSchedulerTimer timerDidFire:]_block_invoke
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.889
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.891
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke_2.890
- ___49-[HMMTRAccessoryServerBrowser startBluetoothScan]_block_invoke.365
- ___50-[HMMTRVendorMetadataFileStore fetchCloudMetadata]_block_invoke
- ___51-[HMMTRAccessoryServer device:receivedEventReport:]_block_invoke.991
- ___52-[HMMTRAccessoryServer populateACLEntriesForPairing]_block_invoke.663
- ___52-[HMMTRAccessoryServerBrowser _cleanupStagedServers]_block_invoke.318
- ___55-[HMMTRAccessoryServer device:receivedAttributeReport:]_block_invoke.989
- ___56-[HMMTRVendorMetadataFileStore cancelCloudMetadataFetch]_block_invoke
- ___57-[HMMTRVendorMetadataFileStore attemptCloudMetadataFetch]_block_invoke
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.926
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.928
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.932
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.934
- ___62-[HMMTRAccessoryServerBrowser stopDiscoveringAccessoryServers]_block_invoke.187
- ___63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.840
- ___63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.841
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.517
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.518
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.519
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.520
- ___64-[HMMTRAccessoryServer _commissioning:complete:abstractMetrics:]_block_invoke.949
- ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.954
- ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.955
- ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.956
- ___64-[HMMTRAccessoryServerBrowser _initializeAndStartBonjourBrowser]_block_invoke.150
- ___64-[HMMTRVendorMetadataFileStore _handleCloudMetadataFetchFailure]_block_invoke
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.504
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.506
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.513
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.514
- ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.188
- ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.191
- ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.193
- ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.195
- ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke_2.194
- ___69-[HMMTRVendorMetadataFileStore _prepopulateCacheForKnownAccessories:]_block_invoke
- ___70-[HMMTRAccessoryServer _onThreadScanResults:commissioning:completion:]_block_invoke.898
- ___70-[HMMTRAccessoryServer _onThreadScanResults:commissioning:completion:]_block_invoke.899
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.500
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.502
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.503
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.834
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.835
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.838
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.839
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke_2.836
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.811
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.812
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.821
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.829
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.832
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.833
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke_2.825
- ___73-[HMMTRSystemCommissionerPairingManager _commissioningCompleteForDevice:]_block_invoke
- ___76-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithNodeID:completion:]_block_invoke.196
- ___79-[HMMTRAccessoryServerBrowser _updateAccessoryControlListForServer:completion:]_block_invoke.323
- ___82-[HMMTRAccessoryServer fetchColorControlClusterForHapAccessory:completionHandler:]_block_invoke.935
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.903
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.904
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.908
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke_2.907
- ___82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke
- ___82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.162
- ___82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.164
- ___83-[HMMTRAccessoryServer updateAccessoryControlToRemoveAdministratorNode:completion:]_block_invoke.863
- ___83-[HMMTRSystemCommissionerPairingManager _armFailSafeForDevice:expiryLengthSeconds:]_block_invoke
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.910
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.911
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.912
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.916
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.917
- ___86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.957
- ___86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.958
- ___86-[HMMTRVendorMetadataFileStore _retrieveVendorMetadataForVendorID:productID:metadata:]_block_invoke
- ___86-[HMMTRVendorMetadataFileStore _retrieveVendorMetadataForVendorID:productID:metadata:]_block_invoke.82
- ___88-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:keepAliveOnly:]_block_invoke.357
- ___88-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:keepAliveOnly:]_block_invoke.358
- ___88-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:keepAliveOnly:]_block_invoke.359
- ___92-[HMMTRAccessoryServer _createFirmwareUpdateServiceWithInstanceID:device:completionHandler:]_block_invoke.803
- ___92-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fabricUUID:fatalError:]_block_invoke.321
- ___92-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fabricUUID:fatalError:]_block_invoke.322
- ___94-[HMMTRAccessoryServer updateAccessoryControlToAdministratorNodes:sharedUserNodes:completion:]_block_invoke.861
- ___94-[HMMTRAccessoryServerBrowser _handleAddOrUpdateWithDiscriminator:vendorID:productID:overBLE:]_block_invoke
- ___94-[HMMTRAccessoryServerBrowser _handleAddOrUpdateWithDiscriminator:vendorID:productID:overBLE:]_block_invoke.171
- ___96-[HMMTRDescriptorClusterManager endpointForClusterID:mtrDevice:callbackQueue:completionHandler:]_block_invoke.401
- ___96-[HMMTRSystemCommissionerPairingManager _donateThreadNetwork:toSystemCommissionerNode:endpoint:]_block_invoke
- ___96-[HMMTRSystemCommissionerPairingManager _donateThreadNetworksToSystemCommissionerNode:endpoint:]_block_invoke
- ___96-[HMMTRSystemCommissionerPairingManager _donateThreadNetworksToSystemCommissionerNode:endpoint:]_block_invoke_2
- ___96-[HMMTRSystemCommissionerPairingManager _retrievePreferredThreadCredentialsOrCreateWithDataset:]_block_invoke
- ___96-[HMMTRSystemCommissionerPairingManager _retrievePreferredThreadCredentialsOrCreateWithDataset:]_block_invoke.62
- ___96-[HMMTRSystemCommissionerPairingManager _retrievePreferredThreadCredentialsOrCreateWithDataset:]_block_invoke_2
- ___96-[HMMTRSystemCommissionerPairingManager _retrieveTHClientPreferredNetworkInternallyOnMdnsAndSig]_block_invoke
- ___97-[HMMTRAccessoryServerBrowser removeAccessoryServer:fromDiscoveredAccessoryServerListWithReason:]_block_invoke.306
- ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.546
- ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.547
- ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.548
- ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.549
- ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.554
- ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.555
- ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke_2.550
- ___Block_byref_object_copy_.10666
- ___Block_byref_object_copy_.11431
- ___Block_byref_object_copy_.12059
- ___Block_byref_object_copy_.12763
- ___Block_byref_object_copy_.12930
- ___Block_byref_object_copy_.2067
- ___Block_byref_object_copy_.3554
- ___Block_byref_object_copy_.3842
- ___Block_byref_object_copy_.4921
- ___Block_byref_object_copy_.6092
- ___Block_byref_object_copy_.6243
- ___Block_byref_object_copy_.8059
- ___Block_byref_object_copy_.8492
- ___Block_byref_object_copy_.9701
- ___Block_byref_object_dispose_.10667
- ___Block_byref_object_dispose_.11432
- ___Block_byref_object_dispose_.12060
- ___Block_byref_object_dispose_.12764
- ___Block_byref_object_dispose_.12931
- ___Block_byref_object_dispose_.2068
- ___Block_byref_object_dispose_.3555
- ___Block_byref_object_dispose_.3843
- ___Block_byref_object_dispose_.4922
- ___Block_byref_object_dispose_.6093
- ___Block_byref_object_dispose_.6244
- ___Block_byref_object_dispose_.8060
- ___Block_byref_object_dispose_.8493
- ___Block_byref_object_dispose_.9702
- ___block_descriptor_32_e101_{_HMFFutureBlockOutcome=q}16?0"MTRGeneralCommissioningClusterCommissioningCompleteResponseParams"8l
- ___block_descriptor_32_e91_{_HMFFutureBlockOutcome=q}16?0"MTRGeneralCommissioningClusterArmFailSafeResponseParams"8l
- ___block_descriptor_48_e8_32s40s_e31_v24?0"NSNumber"8"NSNumber"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e46_v32?0"THCredentials"8"NSUUID"16"NSError"24ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e50_{_HMFFutureBlockOutcome=q}16?0"<HMFAlwaysNil>"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e62_{_HMFFutureBlockOutcome=q}16?0"MTSThreadNetworkCredential"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40w_e46_v32?0"THCredentials"8"NSUUID"16"NSError"24lw40l8s32l8
- ___block_descriptor_56_e8_32s40s48s_e49_{_HMFFutureBlockOutcome=q}16?0"THCredentials"8ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e50_{_HMFFutureBlockOutcome=q}16?0"<HMFAlwaysNil>"8ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56s_e43_{_HMFFutureBlockOutcome=q}16?0"NSError"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_64_e8_32s40s48s56s_e50_{_HMFFutureBlockOutcome=q}16?0"<HMFAlwaysNil>"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_64_e8_32s40s48s56s_e95_{_HMFFutureBlockOutcome=q}16?0"MTRThreadBorderRouterManagementClusterDatasetResponseParams"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_65_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_65_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_67_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64r_e24_v32?0"NSError"8Q16^B24ls32l8s40l8r64l8s48l8s56l8
- ___block_literal_global.100
- ___block_literal_global.10137
- ___block_literal_global.10461
- ___block_literal_global.10537
- ___block_literal_global.109
- ___block_literal_global.11157
- ___block_literal_global.1142
- ___block_literal_global.11708
- ___block_literal_global.11878
- ___block_literal_global.120
- ___block_literal_global.12093
- ___block_literal_global.12229
- ___block_literal_global.12361
- ___block_literal_global.1252
- ___block_literal_global.12580
- ___block_literal_global.1358
- ___block_literal_global.1517
- ___block_literal_global.1575
- ___block_literal_global.1668
- ___block_literal_global.1916
- ___block_literal_global.2190
- ___block_literal_global.2245
- ___block_literal_global.2292
- ___block_literal_global.2379
- ___block_literal_global.2739
- ___block_literal_global.2863
- ___block_literal_global.3013
- ___block_literal_global.312
- ___block_literal_global.315
- ___block_literal_global.3315
- ___block_literal_global.345
- ___block_literal_global.3459
- ___block_literal_global.3488
- ___block_literal_global.354
- ___block_literal_global.3580
- ___block_literal_global.373
- ___block_literal_global.3734
- ___block_literal_global.3931
- ___block_literal_global.408
- ___block_literal_global.4082
- ___block_literal_global.4204
- ___block_literal_global.4690
- ___block_literal_global.489
- ___block_literal_global.5018
- ___block_literal_global.5306
- ___block_literal_global.5441
- ___block_literal_global.553
- ___block_literal_global.554
- ___block_literal_global.5543
- ___block_literal_global.556
- ___block_literal_global.559
- ___block_literal_global.570
- ___block_literal_global.5807
- ___block_literal_global.5980
- ___block_literal_global.610
- ___block_literal_global.62
- ___block_literal_global.6227
- ___block_literal_global.6415
- ___block_literal_global.6555
- ___block_literal_global.6664
- ___block_literal_global.6698
- ___block_literal_global.6719
- ___block_literal_global.6969
- ___block_literal_global.6982
- ___block_literal_global.7076
- ___block_literal_global.7170
- ___block_literal_global.7264
- ___block_literal_global.7367
- ___block_literal_global.7461
- ___block_literal_global.7600
- ___block_literal_global.7741
- ___block_literal_global.7847
- ___block_literal_global.7925
- ___block_literal_global.808
- ___block_literal_global.81
- ___block_literal_global.815
- ___block_literal_global.82.10462
- ___block_literal_global.824
- ___block_literal_global.8275
- ___block_literal_global.828
- ___block_literal_global.8503
- ___block_literal_global.86
- ___block_literal_global.8851
- ___block_literal_global.886
- ___block_literal_global.8968
- ___block_literal_global.9104
- ___block_literal_global.960
- ___block_literal_global.9732
- ___block_literal_global.998
- _attributePathMatches
- _isFeatureMatterHRAPDeviceTypesEnabled
- _isFeatureMatterHRAPDeviceTypesEnabledForTests
- _isFeatureMatterRVCEnabled
- _isFeatureMatterRVCEnabledForTests
- _logCategory._hmf_once_t0.2244
- _logCategory._hmf_once_t0.3458
- _logCategory._hmf_once_t0.5979
- _logCategory._hmf_once_t0.6697
- _logCategory._hmf_once_t10.12579
- _logCategory._hmf_once_t10.1516
- _logCategory._hmf_once_t123
- _logCategory._hmf_once_t13.3579
- _logCategory._hmf_once_t13.3930
- _logCategory._hmf_once_t14.1267
- _logCategory._hmf_once_t14.6981
- _logCategory._hmf_once_t14.7075
- _logCategory._hmf_once_t14.7169
- _logCategory._hmf_once_t14.7366
- _logCategory._hmf_once_t14.7460
- _logCategory._hmf_once_t14.7599
- _logCategory._hmf_once_t199
- _logCategory._hmf_once_t2.10536
- _logCategory._hmf_once_t2.5542
- _logCategory._hmf_once_t2.6663
- _logCategory._hmf_once_t2.7740
- _logCategory._hmf_once_t20.12228
- _logCategory._hmf_once_t26.7263
- _logCategory._hmf_once_t3.1357
- _logCategory._hmf_once_t3.1574
- _logCategory._hmf_once_t31.12360
- _logCategory._hmf_once_t38
- _logCategory._hmf_once_t4.4081
- _logCategory._hmf_once_t4.7846
- _logCategory._hmf_once_t40.6289
- _logCategory._hmf_once_t6.2378
- _logCategory._hmf_once_t6.4203
- _logCategory._hmf_once_t678
- _logCategory._hmf_once_t68.12789
- _logCategory._hmf_once_t8.11877
- _logCategory._hmf_once_v1.2246
- _logCategory._hmf_once_v1.3460
- _logCategory._hmf_once_v1.5981
- _logCategory._hmf_once_v1.6699
- _logCategory._hmf_once_v11.12581
- _logCategory._hmf_once_v11.1518
- _logCategory._hmf_once_v124
- _logCategory._hmf_once_v14.3581
- _logCategory._hmf_once_v14.3932
- _logCategory._hmf_once_v15.1268
- _logCategory._hmf_once_v15.6983
- _logCategory._hmf_once_v15.7077
- _logCategory._hmf_once_v15.7171
- _logCategory._hmf_once_v15.7368
- _logCategory._hmf_once_v15.7462
- _logCategory._hmf_once_v15.7601
- _logCategory._hmf_once_v200
- _logCategory._hmf_once_v21.12230
- _logCategory._hmf_once_v27.7265
- _logCategory._hmf_once_v3.10538
- _logCategory._hmf_once_v3.5544
- _logCategory._hmf_once_v3.6665
- _logCategory._hmf_once_v3.7742
- _logCategory._hmf_once_v32.12362
- _logCategory._hmf_once_v39
- _logCategory._hmf_once_v4.1359
- _logCategory._hmf_once_v4.1576
- _logCategory._hmf_once_v41.6290
- _logCategory._hmf_once_v5.4083
- _logCategory._hmf_once_v5.7848
- _logCategory._hmf_once_v679
- _logCategory._hmf_once_v69.12790
- _logCategory._hmf_once_v7.2380
- _logCategory._hmf_once_v7.4205
- _logCategory._hmf_once_v9.11879
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_addNetworkToThreadNetworkDirectoryForDevice:endpoint:dataset:
- _objc_msgSend$_addProductInfoToMetadata:accessories:
- _objc_msgSend$_addVendorInfoToMetadata:accessories:
- _objc_msgSend$_armFailSafeForDevice:expiryLengthSeconds:
- _objc_msgSend$_augmentDatasetWithBorderAgentIDsForDevice:endpoint:dataset:
- _objc_msgSend$_commissioningCompleteForDevice:
- _objc_msgSend$_deviceForSystemCommissionerNode:
- _objc_msgSend$_discriminator:vendorID:productID:CM:fromTXTRecord:
- _objc_msgSend$_donateThreadNetwork:toSystemCommissionerNode:endpoint:
- _objc_msgSend$_donateThreadNetworksToSystemCommissionerNode:endpoint:
- _objc_msgSend$_handleAddOrUpdateWithDiscriminator:vendorID:productID:overBLE:
- _objc_msgSend$_handleBonjourAddOrUpdateWithDiscriminator:vendorID:productID:
- _objc_msgSend$_handleCloudMetadataFetchFailure
- _objc_msgSend$_handleCloudMetadataFetchSuccess
- _objc_msgSend$_initializeCredentialManagementForCommissioneeNodeID:storage:
- _objc_msgSend$_matterCredentialsFromTHCredentials:
- _objc_msgSend$_prepopulateCacheForKnownAccessories:
- _objc_msgSend$_processSupportedAccessories:
- _objc_msgSend$_provisionBorderRouterWithSystemCommissionerNode:endpoint:dataset:
- _objc_msgSend$_retrievePreferredThreadCredentialsOrCreateWithDataset:
- _objc_msgSend$_retrieveTHClientPreferredNetworkInternallyOnMdnsAndSig
- _objc_msgSend$_retrieveThreadCredentialsFromSystemCommissionerNode:endpoint:
- _objc_msgSend$_retrieveVendorMetadataForVendorID:productID:metadata:
- _objc_msgSend$_saveMetadata:
- _objc_msgSend$_setActiveThreadDatasetForDevice:endpoint:dataset:
- _objc_msgSend$_updateThreadCredentialManagementEnabled:forSystemCommissionerPairingUUID:completionHandler:
- _objc_msgSend$addNetworkWithParams:completion:
- _objc_msgSend$any:
- _objc_msgSend$attemptCloudMetadataFetch
- _objc_msgSend$commissioneeInfo
- _objc_msgSend$copyVendorDetailsFromVendor:
- _objc_msgSend$dataset
- _objc_msgSend$dclCacheAvailable
- _objc_msgSend$enumerateObjectsUsingBlock:
- _objc_msgSend$forAllPairedMatterServersFetchVidPid:
- _objc_msgSend$fromUARPSupportedAccessory:
- _objc_msgSend$getActiveDatasetRequestWithCompletion:
- _objc_msgSend$getBatchedSupportedAccessories:assetLocationType:
- _objc_msgSend$hmfAggregatedErrors
- _objc_msgSend$init:server:nodeID:endpoint:queue:
- _objc_msgSend$initWithDataset:borderAgentEUI:borderAgentID:
- _objc_msgSend$initWithFileURL:uarpController:fileManager:preferences:
- _objc_msgSend$initWithUUID:nodeID:vendorID:productID:deviceType:serialNumber:name:setupPayload:threadCredentialManagementEnabled:
- _objc_msgSend$invalid
- _objc_msgSend$matterDeviceTypeID
- _objc_msgSend$overrideMetadata
- _objc_msgSend$readAttributeMinSetpointDeadBandWithParams:
- _objc_msgSend$readAttributePaths:eventPaths:params:queue:completion:
- _objc_msgSend$removeAllGetters
- _objc_msgSend$rendezvousInformation
- _objc_msgSend$retrievePreferredCredentialsInternally:
- _objc_msgSend$retrievePreferredNetworkInternallyOnMdnsAndSig:
- _objc_msgSend$rootEndpoint
- _objc_msgSend$setActiveDataset:
- _objc_msgSend$setActiveDatasetRequestWithParams:completion:
- _objc_msgSend$setDclCacheAvailable:
- _objc_msgSend$setInvalid:
- _objc_msgSend$setOperationalDataset:
- _objc_msgSend$setReadEndpointInformation:
- _objc_msgSend$setThreadCredentialManagementEnabled:forSystemCommissionerFabricNode:
- _objc_msgSend$setThreadCredentialManagementEndpoint:forSystemCommissionerFabricNode:
- _objc_msgSend$staticMetadata
- _objc_msgSend$staticMetadataFileURL
- _objc_msgSend$threadCredentialManagementEnabledForSystemCommissionerFabricNode:
- _objc_msgSend$threadCredentialManagementEndpoint:
- _objc_msgSend$threadCredentialManagementEndpointForSystemCommissionerFabricNode:
- _objc_msgSend$threadCredentialManagementImplicitlyEnabledForDeviceType:
- _objc_msgSend$threadCredentialManagementNodesAndEndpointsForSystemCommissioner
- _objc_msgSend$timeout:
- _objc_msgSend$vendAccessoryServerWithNodeID:setupCode:discriminator:category:vendorID:productID:serialNumber:firmwareRevision:
- _objc_msgSend$vendorMetadataCache
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
CStrings:
+ "%@+%@"
+ "%u-%u"
+ "%u-0000"
+ "%{public}@ productInfo = %@"
+ "%{public}@ vendorInfo = %@"
+ "%{public}@Base file URL is nil, cannot load override metadata"
+ "%{public}@Cannot extract file name from URL: %@"
+ "%{public}@DN value exceeds maximum length of %d bytes, truncating from %zu bytes"
+ "%{public}@Failed to create vendor metadata for vendorID: %d"
+ "%{public}@Failed to decode DN value as UTF-8 string"
+ "%{public}@Failed to generate product record name for vendorID:%u productID:%u"
+ "%{public}@Found UARP product metadata for record: %s uarpProductInfoMetadata: %@"
+ "%{public}@Found UARP vendor metadata for record: %s - Vendor Name: %@"
+ "%{public}@Generated product record name: %s for vendorID: %u productID: %u"
+ "%{public}@Generated vendor record name: %s for vendorID: %u (no valid productID)"
+ "%{public}@Invalid parameters - uarpProductInfoMetadata: %@ productID: %d"
+ "%{public}@Invalid parameters - uarpVendorInfoMetadata: %@ vendorID: %d"
+ "%{public}@Invalid time %02ld:%02ld:%02ld (valid ranges: 00-23:00-59:00-59)"
+ "%{public}@Invalid vendorID: %d - returning nil"
+ "%{public}@Missing DN value in TXT record"
+ "%{public}@Retrieved Thread operational dataset (staging,HAPThreadNetworkMetadata): %@"
+ "%{public}@Retrieved Thread operational dataset (staging,activeOperationalDataSet): %@"
+ "%{public}@Subscribe result: %u"
+ "%{public}@UARP metadata retrieval completed - VendorID: %u, ProductID: %d, metaDataVendor: %@"
+ "%{public}@Using DN from Bonjour TXT record for test device: %@"
+ "%{public}@Vendor metadata override is active for testing - skipping cloud download trigger. Cloud metadata will not be fetched while allowVendorDataOverride flag is enabled."
+ "%{public}@_isDataInjectionActive returns %d"
+ "%{public}@_retrieveVendorMetadataFromInjectedData:%u productID:%d -> failed to create mutable copy of vendor"
+ "%{public}@_retrieveVendorMetadataFromInjectedData:%u productID:%d -> nil metadata provided, returning nil"
+ "%{public}@_retrieveVendorMetadataFromInjectedData:%u productID:%d -> nil vendor, returning nil"
+ "%{public}@_retrieveVendorMetadataFromInjectedData:%u productID:%d -> returning vendor from static metadata"
+ "%{public}@_retrieveVendorMetadataFromInjectedData:%u productID:%d -> returning vendor with product from static metadata, \n vendor = %@"
+ "%{public}@_retrieveVendorMetadataFromInjectedData:%u productID:%d -> vendor is not mutable, cannot add product"
+ "%{public}@_retrieveVendorMetadataFromInjectedData:%u productID:%d -> vendor not found in provided metadata"
+ "%{public}@copyChipMetadataForRecordName: not available in this CoreUARP version"
+ "%{public}@retrieveVendorMetadataForVendorID:nil productID:%d -> nil vendor, returning nil"
+ "%{public}@scheduleOrExecuteOTAProviderAnnouncement is invoked by %@ immediateAnnouncement=%s, delayCounter=%ld, isUserTriggered=%s"
+ "%{public}@subscribeForChipSupportedAccessories: not available in this CoreUARP version"
+ "%{public}@vendAccessoryServerWithNodeID - nodeID: %@, category: %@, vid: %@, pid %@, serial %@, deviceName: %@"
+ "%{public}@vendorInfoRecordName = %s"
+ "<nil>"
+ "<none>"
+ "@48@0:8d16@24@32@40"
+ "AccesoryRequest"
+ "DN"
+ "HMFPreferences.sharedPreferences"
+ "NotifyUpdateRequest"
+ "OtaSchedulerTimer"
+ "RebootRepair"
+ "T@\"NSNumber\",R,D"
+ "T@\"UARPController\",&,N,V_uarpController"
+ "_convertUARPMetadataToVendor:uarpProductInfoMetadata:vendorID:productID:"
+ "_createUARPProductMetadata:productID:"
+ "_createUARPVendorMetadata:vendorID:"
+ "_discriminator:vendorID:productID:CM:deviceName:fromTXTRecord:"
+ "_generateRecordName:productID:"
+ "_handleAddOrUpdateWithDiscriminator:vendorID:productID:deviceName:overBLE:"
+ "_handleBonjourAddOrUpdateWithDiscriminator:vendorID:productID:deviceName:"
+ "_injectedDataLock"
+ "_isDataInjectionActive"
+ "_retrieveVendorMetadataFromInjectedData:productID:metadata:"
+ "_retrieveVendorMetadataUsingNewAPIs:productID:"
+ "_uarpLock"
+ "accessoryServerBrowser:getThreadNetworkCredentialsForStagingWithCompletion:"
+ "configureMetaDataService"
+ "copyChipMetadataForRecordName:"
+ "discoveryCapabilities"
+ "fetchPreferredThreadCredentialsForStagingWithCompletion:"
+ "i64@0:8^@16^@24^@32^@40^@48@56"
+ "init:server:endpoint:queue:"
+ "initWithUUID:nodeID:vendorID:productID:deviceType:serialNumber:name:setupPayload:"
+ "loadTestInjectedMetadata"
+ "setUarpController:"
+ "setupPasscode"
+ "subscribeForChipSupportedAccessories"
+ "v32@0:8@\"HAPAccessoryServerBrowser\"16@?<v@?@\"HAPThreadNetworkMetadata\"@\"NSError\">24"
+ "vendAccessoryServerWithNodeID:setupCode:discriminator:category:vendorID:productID:serialNumber:firmwareRevision:deviceName:"
- "%{public}@Attempting to provision unconfigured Border Router on System Commissioner node %@"
- "%{public}@Cancelling cloud metadata fetch"
- "%{public}@Cloud metadata fetch already in progress, skipping duplicate request"
- "%{public}@Cloud metadata fetch cancelled"
- "%{public}@Cloud metadata fetch failed, scheduling retry %lu in %.1f seconds"
- "%{public}@Cloud metadata fetch succeeded, resetting retry state"
- "%{public}@Donating Thread network '%@' (%@) to system commissioner node %@"
- "%{public}@Failed to acquire System Commissioner device controller"
- "%{public}@Failed to decode local vendor metadata from dictionary representation"
- "%{public}@Failed to decode vendor metadata from dictionary representation"
- "%{public}@Failed to donate Thread credentials to System Commissioner node %@: %@"
- "%{public}@Failed to load local vendor metadata at file URL %@: %@"
- "%{public}@Failed to request supported accessories from UARP controller"
- "%{public}@Failed to write vendor metadata to %@: %@"
- "%{public}@Fetching cloud metadata by requesting supported accessories from UARP controller (attempt %lu)"
- "%{public}@HMMTRAnnounceOtaSchedulerTimer - OTA Announce completed."
- "%{public}@HMMTRAnnounceOtaSchedulerTimer - OTA Announce failed with Error: %@."
- "%{public}@Maximum retry time (%.1f hours) exceeded, giving up on cloud metadata fetch"
- "%{public}@MinSetpointDeadBand attribute from the %@ cluster endpoint:%@ of node %@ not available"
- "%{public}@No DCL data available, defaulting to static metadata"
- "%{public}@No vendor/product information available"
- "%{public}@Processing all supported accessories, number of entries: %lu"
- "%{public}@RVC feature is disabled"
- "%{public}@RVC feature is enabled"
- "%{public}@RVC feature is enabled through profile"
- "%{public}@Received batched supported accessories, number of entries: %lu, isComplete: %@"
- "%{public}@Retrieved Thread operational dataset (staging): %@"
- "%{public}@Retry cancelled - fetch no longer in progress"
- "%{public}@Saving MinSetpointDeadBand attribute as %@ from the %@ cluster for endpoint:%@ of node %@"
- "%{public}@Skipping cloud fetch of metadata because override metadata is active"
- "%{public}@Successfully donated Thread network '%@' (%@) to Thread Network Directory of system commissioner node %@"
- "%{public}@Successfully enabled Border Router on System Commissioner node %@"
- "%{public}@Successfully provisioned Thread credentials on System Commissioner node %@"
- "%{public}@Successfully retrieved Thread credentials from System Commissioner node %@"
- "%{public}@Successfully saved metadata to %@"
- "%{public}@Thread Border Router is not configured for System Commissioner node %@"
- "%{public}@Thread credential management endpoint not found for commissionee %@ with primary device type %@"
- "%{public}@Thread credential management is not supported for System Commissioner pairing with UUID = %@"
- "%{public}@Thread credential management is supported for commissionee %@, auto-enable = %@"
- "%{public}@Unexpected, found %lu batched accessories. Previous batch may not be complete"
- "%{public}@Vendor %@ not found for product record %@"
- "%{public}@retrieveVendorMetadataForVendorID:%@ productID:%@ (newMetadata:%@,vendor(cacheMiss:%@,metadataMiss:%@)) -> returning metadata: %@"
- "%{public}@retrieveVendorMetadataForVendorID:%@ productID:%@ (newMetadata:%@,vendor(cacheMiss:%@,metadataMiss:%@),product(cacheMiss:%@,metadataMiss:%@)) -> returning metadata: %@"
- "%{public}@retrieveVendorMetadataForVendorID:%@ productID:%@ -> nil vendor, returning nil"
- "%{public}@scheduleOrExecuteOTAProviderAnnouncement is invoked by %@ immediateAnnouncement= %@, delayCounter= %ld, isUserTriggered = %@"
- "%{public}@vendAccessoryServerWithNodeID - nodeID: %@, category: %@, vid: %@, pid %@, serial %@"
- "0000"
- "4"
- "@\"<HMMTRVendorMetadataStoreDelegate>\""
- "@\"<HMMTRVendorMetadataStoreDelegate>\"16@0:8"
- "@\"HMMTRVendorMetadata\"16@0:8"
- "@32@0:8@16Q24"
- "@56@0:8d16@24@32@40@48"
- "AccessoryRequestInitiator"
- "Available"
- "CommissioneeInfo must be available"
- "DCL Cache %@"
- "ERROR: Invalid time %02ld:%02ld:%02ld (valid ranges: 00-23:00-59:00-59)"
- "General Commissioning Error %@"
- "HMD.MTRPlugin.MTS.TCM.ep"
- "HMD.MTRPlugin.MTS.TCM.on"
- "Keepalive"
- "MatterHRAPDeviceTypes"
- "MatterThreadCredentialsRetrievalTimeout"
- "MinSetpointDeadBand"
- "No dataset available for network"
- "NotifyUpdateRequestInitiator"
- "RVC"
- "RebootRepairInitiator"
- "T@\"<HMMTRVendorMetadataStoreDelegate>\",W"
- "T@\"<HMMTRVendorMetadataStoreDelegate>\",W,V_delegate"
- "T@\"HMFTimer\",&,V_retryTimer"
- "T@\"HMMTRVendorMetadata\",R,C"
- "T@\"NSCache\",R,N,V_vendorMetadataCache"
- "T@\"NSMutableSet\",&,V_batchedAccessories"
- "T@\"NSObject<OS_dispatch_queue>\",R,V_retryQueue"
- "TB,N,V_fetchInProgress"
- "TB,V_dclCacheAvailable"
- "TB,V_invalid"
- "TQ,V_retryCount"
- "Td,N,V_retryIntervalOverride"
- "Td,V_firstFailureTime"
- "Unavailable"
- "_addNetworkToThreadNetworkDirectoryForDevice:endpoint:dataset:"
- "_addProductInfoToMetadata:accessories:"
- "_addVendorInfoToMetadata:accessories:"
- "_armFailSafeForDevice:expiryLengthSeconds:"
- "_augmentDatasetWithBorderAgentIDsForDevice:endpoint:dataset:"
- "_batchedAccessories"
- "_commissioningCompleteForDevice:"
- "_dclCacheAvailable"
- "_deviceForSystemCommissionerNode:"
- "_discriminator:vendorID:productID:CM:fromTXTRecord:"
- "_donateThreadNetwork:toSystemCommissionerNode:endpoint:"
- "_donateThreadNetworksToSystemCommissionerNode:endpoint:"
- "_fetchInProgress"
- "_firstFailureTime"
- "_handleAddOrUpdateWithDiscriminator:vendorID:productID:overBLE:"
- "_handleBonjourAddOrUpdateWithDiscriminator:vendorID:productID:"
- "_handleCloudMetadataFetchFailure"
- "_handleCloudMetadataFetchSuccess"
- "_initializeCredentialManagementForCommissioneeNodeID:storage:"
- "_prepopulateCacheForKnownAccessories:"
- "_processSupportedAccessories:"
- "_provisionBorderRouterWithSystemCommissionerNode:endpoint:dataset:"
- "_retrievePreferredThreadCredentialsOrCreateWithDataset:"
- "_retrieveTHClientPreferredNetworkInternallyOnMdnsAndSig"
- "_retrieveThreadCredentialsFromSystemCommissionerNode:endpoint:"
- "_retrieveVendorMetadataForVendorID:productID:metadata:"
- "_retryIntervalOverride"
- "_retryQueue"
- "_retryTimer"
- "_saveMetadata:"
- "_setActiveThreadDatasetForDevice:endpoint:dataset:"
- "_updateThreadCredentialManagementEnabled:forSystemCommissionerPairingUUID:completionHandler:"
- "_vendorMetadataCache"
- "addNetworkWithParams:completion:"
- "any:"
- "attemptCloudMetadataFetch"
- "batchedAccessories"
- "cancelCloudMetadataFetch"
- "com.apple.homekit.matter.vendor.metadata.retry"
- "dataset"
- "dclCacheAvailable"
- "device controller unavailable"
- "disableFeatureMatterHRAPDeviceTypesForTests"
- "disableFeatureMatterRVCForTests"
- "enableFeatureMatterHRAPDeviceTypesForTests"
- "enableFeatureMatterRVCForTests"
- "enumerateObjectsUsingBlock:"
- "fetchCloudMetadata"
- "fetchInProgress"
- "firstFailureTime"
- "forAllPairedMatterServersFetchVidPid:"
- "getActiveDatasetRequestWithCompletion:"
- "getBatchedSupportedAccessories:assetLocationType:"
- "hmfAggregatedErrors"
- "i56@0:8^@16^@24^@32^@40@48"
- "init:server:nodeID:endpoint:queue:"
- "initWithDataset:borderAgentEUI:borderAgentID:"
- "initWithFileURL:uarpController:fileManager:preferences:"
- "initWithUUID:nodeID:vendorID:productID:deviceType:serialNumber:name:setupPayload:threadCredentialManagementEnabled:"
- "minSetpointDeadBand"
- "overrideMetadata"
- "readAttributeMinSetpointDeadBandWithParams:"
- "readAttributePaths:eventPaths:params:queue:completion:"
- "rendezvousInformation"
- "retrievePreferredCredentialsInternally:"
- "retrievePreferredNetworkInternallyOnMdnsAndSig:"
- "retrievePreferredThreadCredentialsOrCreateWithDataset:completionHandler:"
- "retryIntervalOverride"
- "retryQueue"
- "retryTimer"
- "rootEndpoint"
- "setActiveDataset:"
- "setActiveDatasetRequestWithParams:completion:"
- "setBatchedAccessories:"
- "setDclCacheAvailable:"
- "setFetchInProgress:"
- "setFirstFailureTime:"
- "setInvalid:"
- "setOperationalDataset:"
- "setReadEndpointInformation:"
- "setRetryIntervalOverride:"
- "setRetryTimer:"
- "setThreadCredentialManagementEnabled:forSystemCommissionerFabricNode:"
- "setThreadCredentialManagementEndpoint:forSystemCommissionerFabricNode:"
- "staticMetadata"
- "staticMetadataFileURL"
- "threadCredentialManagementEnabledForSystemCommissionerFabricNode:"
- "threadCredentialManagementEndpoint:"
- "threadCredentialManagementEndpointForSystemCommissionerFabricNode:"
- "threadCredentialManagementImplicitlyEnabledForDeviceType:"
- "threadCredentialManagementNodesAndEndpointsForSystemCommissioner"
- "timeout:"
- "unsetFeatureMatterHRAPDeviceTypesForTests"
- "unsetFeatureMatterRVCForTests"
- "updateThreadCredentialManagementEnabled:forSystemCommissionerPairingUUID:completionHandler:"
- "v24@0:8@\"<HMMTRVendorMetadataStoreDelegate>\"16"
- "v24@?0@\"NSNumber\"8@\"NSNumber\"16"
- "v32@?0@\"NSError\"8Q16^B24"
- "v32@?0@\"THCredentials\"8@\"NSUUID\"16@\"NSError\"24"
- "v36@0:8B16@20@?28"
- "vendAccessoryServerWithNodeID:setupCode:discriminator:category:vendorID:productID:serialNumber:firmwareRevision:"
- "vendor-metadata"
- "vendor-metadata-local"
- "vendorMetadataCache"
- "{_HMFFutureBlockOutcome=q@}16@?0@\"MTRGeneralCommissioningClusterArmFailSafeResponseParams\"8"
- "{_HMFFutureBlockOutcome=q@}16@?0@\"MTRGeneralCommissioningClusterCommissioningCompleteResponseParams\"8"
- "{_HMFFutureBlockOutcome=q@}16@?0@\"MTRThreadBorderRouterManagementClusterDatasetResponseParams\"8"
- "{_HMFFutureBlockOutcome=q@}16@?0@\"MTSThreadNetworkCredential\"8"
- "{_HMFFutureBlockOutcome=q@}16@?0@\"THCredentials\"8"

```
