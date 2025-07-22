## HomeKitMatter

> `/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter`

```diff

-1340.3.0.0.0
-  __TEXT.__text: 0x13cf08
-  __TEXT.__auth_stubs: 0xa90
-  __TEXT.__objc_methlist: 0xa09c
+1345.1.0.1.1
+  __TEXT.__text: 0x140620
+  __TEXT.__auth_stubs: 0xaa0
+  __TEXT.__objc_methlist: 0xa1fc
   __TEXT.__const: 0x160
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__gcc_except_tab: 0x2cd4
-  __TEXT.__cstring: 0x68df
-  __TEXT.__oslogstring: 0x27c9c
+  __TEXT.__gcc_except_tab: 0x2cf8
+  __TEXT.__cstring: 0x6b59
+  __TEXT.__oslogstring: 0x28231
   __TEXT.__ustring: 0x68
-  __TEXT.__unwind_info: 0x2da8
-  __TEXT.__objc_classname: 0x13d4
-  __TEXT.__objc_methname: 0x24e37
-  __TEXT.__objc_methtype: 0x3a1f
-  __TEXT.__objc_stubs: 0x15e40
-  __DATA_CONST.__got: 0x9a0
-  __DATA_CONST.__const: 0x4690
-  __DATA_CONST.__objc_classlist: 0x408
+  __TEXT.__unwind_info: 0x2e28
+  __TEXT.__objc_classname: 0x142a
+  __TEXT.__objc_methname: 0x256f8
+  __TEXT.__objc_methtype: 0x3b06
+  __TEXT.__objc_stubs: 0x16460
+  __DATA_CONST.__got: 0x9d8
+  __DATA_CONST.__const: 0x47e8
+  __DATA_CONST.__objc_classlist: 0x410
   __DATA_CONST.__objc_catlist: 0x50
-  __DATA_CONST.__objc_protolist: 0x120
+  __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6a18
+  __DATA_CONST.__objc_selrefs: 0x6ba0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x2d0
-  __DATA_CONST.__objc_arraydata: 0x230
-  __AUTH_CONST.__auth_got: 0x558
-  __AUTH_CONST.__const: 0x1000
-  __AUTH_CONST.__cfstring: 0x6a00
-  __AUTH_CONST.__objc_const: 0xef98
-  __AUTH_CONST.__objc_intobj: 0x1728
+  __DATA_CONST.__objc_arraydata: 0x250
+  __AUTH_CONST.__auth_got: 0x560
+  __AUTH_CONST.__const: 0x1040
+  __AUTH_CONST.__cfstring: 0x6b20
+  __AUTH_CONST.__objc_const: 0xf070
+  __AUTH_CONST.__objc_intobj: 0x1770
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x1d10
-  __DATA.__objc_ivar: 0xa7c
-  __DATA.__data: 0xd80
-  __DATA.__bss: 0x438
+  __AUTH.__objc_data: 0x1d60
+  __DATA.__objc_ivar: 0xa80
+  __DATA.__data: 0xde0
+  __DATA.__bss: 0x448
   __DATA_DIRTY.__objc_data: 0xb40
-  __DATA_DIRTY.__bss: 0xa0
+  __DATA_DIRTY.__bss: 0x90
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities
   - /System/Library/PrivateFrameworks/RegulatoryDomain.framework/RegulatoryDomain
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/UARPKit.framework/UARPKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8F307863-98D1-3A37-BED8-1938E8A3B38F
-  Functions: 4150
-  Symbols:   14371
-  CStrings:  9330
+  UUID: 773232F7-FF4F-391C-BCA2-05EFB99FA075
+  Functions: 4192
+  Symbols:   14535
+  CStrings:  9429
 
Symbols:
+ -[HMMTRAccessoryServer _handlePairOnSystemCommissionerFabricStart]
+ -[HMMTRAccessoryServer commissioneeInfo]
+ -[HMMTRAccessoryServer ensureCommissioningID]
+ -[HMMTRAccessoryServer setCommissioneeInfo:]
+ -[HMMTRAccessoryServerBrowser initWithQueue:storeDirectoryURL:dataSource:]
+ -[HMMTRAccessoryServerBrowserDataSourceDefault makeSystemCommissionerPairingManagerWithQueue:browser:]
+ -[HMMTRAccessoryServerBrowserDataSourceDefault makeThreadRadioManagerWithBrowser:]
+ -[HMMTRProtocolMap rawPlistAtKey:]
+ -[HMMTRProtocolMap retrieveHAPToCHIPClusterMapping:]
+ -[HMMTRStorage(Records) setThreadCredentialManagementEnabled:forSystemCommissionerFabricNode:]
+ -[HMMTRStorage(Records) setThreadCredentialManagementEndpoint:forSystemCommissionerFabricNode:]
+ -[HMMTRStorage(Records) threadCredentialManagementEnabledForSystemCommissionerFabricNode:]
+ -[HMMTRStorage(Records) threadCredentialManagementEndpointForSystemCommissionerFabricNode:]
+ -[HMMTRStorage(Records) threadCredentialManagementNodesAndEndpointsForSystemCommissioner]
+ -[HMMTRSystemCommissionerPairingManager _addNetworkToThreadNetworkDirectoryForDevice:endpoint:dataset:]
+ -[HMMTRSystemCommissionerPairingManager _armFailSafeForDevice:expiryLengthSeconds:]
+ -[HMMTRSystemCommissionerPairingManager _commissioningCompleteForDevice:]
+ -[HMMTRSystemCommissionerPairingManager _deviceForSystemCommissionerNode:]
+ -[HMMTRSystemCommissionerPairingManager _donateThreadNetwork:toSystemCommissionerNode:endpoint:]
+ -[HMMTRSystemCommissionerPairingManager _donateThreadNetworksToSystemCommissionerNode:endpoint:]
+ -[HMMTRSystemCommissionerPairingManager _generateThreadOperationalDataset]
+ -[HMMTRSystemCommissionerPairingManager _provisionBorderRouterWithSystemCommissionerNode:endpoint:]
+ -[HMMTRSystemCommissionerPairingManager _retrievePreferredThreadCredentialsWithOptions:]
+ -[HMMTRSystemCommissionerPairingManager _retrieveTHClientPreferredNetworkInternallyOnMdnsAndSig]
+ -[HMMTRSystemCommissionerPairingManager _retrieveThreadCredentialsFromSystemCommissionerNode:endpoint:]
+ -[HMMTRSystemCommissionerPairingManager _setActiveThreadDatasetForDevice:endpoint:dataset:]
+ -[HMMTRSystemCommissionerPairingManager _updateThreadCredentialManagementEnabled:forSystemCommissionerPairingUUID:completionHandler:]
+ -[HMMTRSystemCommissionerPairingManager retrievePreferredThreadCredentialsWithOptions:completionHandler:]
+ -[HMMTRSystemCommissionerPairingManager updateThreadCredentialManagementEnabled:forSystemCommissionerPairingUUID:completionHandler:]
+ GCC_except_table1057
+ GCC_except_table1117
+ GCC_except_table1163
+ GCC_except_table1171
+ GCC_except_table1220
+ GCC_except_table1228
+ GCC_except_table1265
+ GCC_except_table1302
+ GCC_except_table1331
+ GCC_except_table1532
+ GCC_except_table1571
+ GCC_except_table1724
+ GCC_except_table1725
+ GCC_except_table1728
+ GCC_except_table1748
+ GCC_except_table1749
+ GCC_except_table1751
+ GCC_except_table1752
+ GCC_except_table1760
+ GCC_except_table1761
+ GCC_except_table1762
+ GCC_except_table1763
+ GCC_except_table1764
+ GCC_except_table1823
+ GCC_except_table1829
+ GCC_except_table1863
+ GCC_except_table1938
+ GCC_except_table2050
+ GCC_except_table2052
+ GCC_except_table2082
+ GCC_except_table2090
+ GCC_except_table2092
+ GCC_except_table2140
+ GCC_except_table2181
+ GCC_except_table2243
+ GCC_except_table2484
+ GCC_except_table2488
+ GCC_except_table2540
+ GCC_except_table2581
+ GCC_except_table2624
+ GCC_except_table2626
+ GCC_except_table2651
+ GCC_except_table2652
+ GCC_except_table2653
+ GCC_except_table2674
+ GCC_except_table2676
+ GCC_except_table2677
+ GCC_except_table2678
+ GCC_except_table2679
+ GCC_except_table2680
+ GCC_except_table2681
+ GCC_except_table2693
+ GCC_except_table2695
+ GCC_except_table2714
+ GCC_except_table2736
+ GCC_except_table2747
+ GCC_except_table2750
+ GCC_except_table2754
+ GCC_except_table2772
+ GCC_except_table2776
+ GCC_except_table2778
+ GCC_except_table2797
+ GCC_except_table2803
+ GCC_except_table2808
+ GCC_except_table2820
+ GCC_except_table2871
+ GCC_except_table2872
+ GCC_except_table3236
+ GCC_except_table3237
+ GCC_except_table3238
+ GCC_except_table3242
+ GCC_except_table3247
+ GCC_except_table3250
+ GCC_except_table3264
+ GCC_except_table3280
+ GCC_except_table3345
+ GCC_except_table3364
+ GCC_except_table3366
+ GCC_except_table3373
+ GCC_except_table3374
+ GCC_except_table3397
+ GCC_except_table3398
+ GCC_except_table3407
+ GCC_except_table3432
+ GCC_except_table3435
+ GCC_except_table3443
+ GCC_except_table3462
+ GCC_except_table3501
+ GCC_except_table3505
+ GCC_except_table3522
+ GCC_except_table3524
+ GCC_except_table3542
+ GCC_except_table3608
+ GCC_except_table3652
+ GCC_except_table3670
+ GCC_except_table3693
+ GCC_except_table3697
+ GCC_except_table3712
+ GCC_except_table3713
+ GCC_except_table3718
+ GCC_except_table3725
+ GCC_except_table3782
+ GCC_except_table3802
+ GCC_except_table3856
+ GCC_except_table3861
+ GCC_except_table3864
+ GCC_except_table3945
+ GCC_except_table3946
+ GCC_except_table4001
+ GCC_except_table4004
+ GCC_except_table4066
+ GCC_except_table4128
+ GCC_except_table4132
+ GCC_except_table4136
+ GCC_except_table4139
+ GCC_except_table4172
+ GCC_except_table683
+ GCC_except_table687
+ GCC_except_table748
+ GCC_except_table749
+ GCC_except_table750
+ GCC_except_table818
+ GCC_except_table881
+ GCC_except_table885
+ GCC_except_table887
+ GCC_except_table889
+ GCC_except_table891
+ GCC_except_table895
+ GCC_except_table899
+ GCC_except_table902
+ GCC_except_table945
+ GCC_except_table949
+ GCC_except_table951
+ _NSTemporaryDirectory
+ _OBJC_CLASS_$_HMMTRAccessoryServerBrowserDataSourceDefault
+ _OBJC_CLASS_$_MTRClusterGeneralCommissioning
+ _OBJC_CLASS_$_MTRClusterThreadBorderRouterManagement
+ _OBJC_CLASS_$_MTRClusterThreadNetworkDirectory
+ _OBJC_CLASS_$_MTRThreadBorderRouterManagementClusterSetActiveDatasetRequestParams
+ _OBJC_CLASS_$_MTRThreadNetworkDirectoryClusterAddNetworkParams
+ _OBJC_CLASS_$_MTSNetworkCredentialManager
+ _OBJC_CLASS_$_MTSThreadNetworkCredential
+ _OBJC_IVAR_$_HMMTRAccessoryServer._commissioneeInfo
+ _OBJC_IVAR_$_HMMTRProtocolMap._mapData
+ _OBJC_IVAR_$_HMMTRProtocolMap.hapToCHIPClusterMappingArrayOffset
+ _OBJC_METACLASS_$_HMMTRAccessoryServerBrowserDataSourceDefault
+ __OBJC_$_INSTANCE_METHODS_HMMTRAccessoryServerBrowserDataSourceDefault
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HMMTRAccessoryServerBrowserDataSource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMMTRAccessoryServerBrowserDataSource
+ __OBJC_CLASS_PROTOCOLS_$_HMMTRAccessoryServerBrowserDataSourceDefault
+ __OBJC_CLASS_RO_$_HMMTRAccessoryServerBrowserDataSourceDefault
+ __OBJC_LABEL_PROTOCOL_$_HMMTRAccessoryServerBrowserDataSource
+ __OBJC_METACLASS_RO_$_HMMTRAccessoryServerBrowserDataSourceDefault
+ __OBJC_PROTOCOL_$_HMMTRAccessoryServerBrowserDataSource
+ ___101-[HMMTRAccessoryServer updateAccessoryControlToIncludeAdministratorNodes:sharedUserNodes:completion:]_block_invoke.835
+ ___102-[HMMTRAccessoryServer updateAllCharacteristicValuesPostHAPServiceEnumerationForAccessory:completion:]_block_invoke.787
+ ___103-[HMMTRSystemCommissionerPairingManager _retrieveThreadCredentialsFromSystemCommissionerNode:endpoint:]_block_invoke
+ ___105-[HMMTRSystemCommissionerPairingManager retrievePreferredThreadCredentialsWithOptions:completionHandler:]_block_invoke
+ ___107-[HMMTRAccessoryServerBrowser _fetchDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.209
+ ___110-[HMMTRAccessoryServerBrowser removeAllDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.211
+ ___112-[HMMTRAccessoryServer _updateAdditionalCharacteristicsFromCharacteristicUpdate:service:path:completionHandler:]_block_invoke.380
+ ___114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke.911
+ ___114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke.914
+ ___114-[HMMTRProtocolMap _selectedServiceTypeForServiceArray:device:mtrDevice:endpoint:callbackQueue:completionHandler:]_block_invoke.426
+ ___117-[HMMTRAccessoryServer _findSystemCommissionerPairingMatchingSetupPayload:systemCommissionerPairings:pairingManager:]_block_invoke.260
+ ___117-[HMMTRAccessoryServer _findSystemCommissionerPairingMatchingSetupPayload:systemCommissionerPairings:pairingManager:]_block_invoke.261
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.505
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.507
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.509
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.510
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.512
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.514
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.511
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.513
+ ___119-[HMMTRAccessoryServerBrowser removeDevicePairingFabricForSystemCommissionerDeviceWithNodeID:fabric:completionHandler:]_block_invoke.207
+ ___132-[HMMTRSystemCommissionerPairingManager updateThreadCredentialManagementEnabled:forSystemCommissionerPairingUUID:completionHandler:]_block_invoke
+ ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.325
+ ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.326
+ ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.328
+ ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.329
+ ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.330
+ ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.331
+ ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.332
+ ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.333
+ ___278-[HMMTRAccessoryServerBrowser _stageAccessoryServerWithSetupPayload:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:commissioneeInfoHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke.194
+ ___37-[HMMTRAccessoryServer finishPairing]_block_invoke.767
+ ___37-[HMMTRAccessoryServer timerDidFire:]_block_invoke.277
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.643
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.644
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.645
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.647
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.651
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.652
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.653
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.654
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.646
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.655
+ ___40-[HMMTRAccessoryServerBrowser configure]_block_invoke.138
+ ___42-[HMMTRAccessoryServer _setupMatterDevice]_block_invoke.308
+ ___43-[HMMTRAccessoryServer _setupThreadPairing]_block_invoke.466
+ ___43-[HMMTRAccessoryServer _unpair:completion:]_block_invoke.300
+ ___43-[HMMTRAccessoryServer discoverAccessories]_block_invoke.303
+ ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.885
+ ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.887
+ ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.888
+ ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.890
+ ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke_2.886
+ ___45-[HMMTRAccessoryServer stopPairingWithError:]_block_invoke.289
+ ___47-[HMMTRAccessoryServer processAttributeReport:]_block_invoke.974
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.859
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.862
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.864
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke_2.863
+ ___49-[HMMTRAccessoryServerBrowser startBluetoothScan]_block_invoke.364
+ ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.818
+ ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.822
+ ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.823
+ ___51-[HMMTRAccessoryServer device:receivedEventReport:]_block_invoke.975
+ ___52-[HMMTRAccessoryServer populateACLEntriesForPairing]_block_invoke.640
+ ___52-[HMMTRAccessoryServerBrowser _cleanupStagedServers]_block_invoke.315
+ ___53-[HMMTRAccessoryServer _tryPairingUsingMatterSupport]_block_invoke.254
+ ___55-[HMMTRAccessoryServer device:receivedAttributeReport:]_block_invoke.973
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.424
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.425
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.426
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.427
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.428
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.429
+ ___58-[HMMTRProtocolMap _buildEventMapper:characteristicsDict:]_block_invoke.301
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.437
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.438
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.440
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.441
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.442
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.916
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.918
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.922
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.924
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.430
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.431
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.432
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.433
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.434
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.435
+ ___62-[HMMTRAccessoryServerBrowser stopDiscoveringAccessoryServers]_block_invoke.183
+ ___63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.816
+ ___63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.817
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.484
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.485
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.486
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.487
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.488
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.489
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.454
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.455
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.456
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.457
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.458
+ ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.937
+ ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.938
+ ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.939
+ ___64-[HMMTRAccessoryServerBrowser _initializeAndStartBonjourBrowser]_block_invoke.146
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.449
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.450
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.451
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.452
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.453
+ ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.443
+ ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.444
+ ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.445
+ ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.448
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.473
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.474
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.475
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.478
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.482
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.483
+ ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.421
+ ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.422
+ ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.423
+ ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.187
+ ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.189
+ ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.191
+ ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke_2.190
+ ___71-[HMMTRAccessoryServer validateAttestationDeviceInfo:error:completion:]_block_invoke.279
+ ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.407
+ ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.408
+ ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.409
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.467
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.468
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.469
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.471
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.472
+ ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.267
+ ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.268
+ ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.269
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.811
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.812
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.814
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.815
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.788
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.789
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.806
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.807
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.809
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.810
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke_2.802
+ ___73-[HMMTRSystemCommissionerPairingManager _commissioningCompleteForDevice:]_block_invoke
+ ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.869
+ ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.870
+ ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.874
+ ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke_2.876
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.292
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.296
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.297
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.298
+ ___76-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithNodeID:completion:]_block_invoke.192
+ ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.410
+ ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.411
+ ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.412
+ ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.414
+ ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.415
+ ___79-[HMMTRAccessoryServerBrowser _updateAccessoryControlListForServer:completion:]_block_invoke.320
+ ___82-[HMMTRAccessoryServer fetchColorControlClusterForHapAccessory:completionHandler:]_block_invoke.925
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.893
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.894
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.895
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.898
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke_2.897
+ ___82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.158
+ ___82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.160
+ ___82-[HMMTRProtocolMap _buildValueMapper:characteristicsDict:operation:forMTRCluster:]_block_invoke.280
+ ___83-[HMMTRAccessoryServer updateAccessoryControlToRemoveAdministratorNode:completion:]_block_invoke.836
+ ___83-[HMMTRSystemCommissionerPairingManager _armFailSafeForDevice:expiryLengthSeconds:]_block_invoke
+ ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.387
+ ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.389
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.899
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.900
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.901
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.902
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.906
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.907
+ ___86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.940
+ ___86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.941
+ ___88-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:keepAliveOnly:]_block_invoke.356
+ ___88-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:keepAliveOnly:]_block_invoke.357
+ ___88-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:keepAliveOnly:]_block_invoke.358
+ ___88-[HMMTRSystemCommissionerPairingManager _retrievePreferredThreadCredentialsWithOptions:]_block_invoke
+ ___88-[HMMTRSystemCommissionerPairingManager _retrievePreferredThreadCredentialsWithOptions:]_block_invoke.62
+ ___88-[HMMTRSystemCommissionerPairingManager _retrievePreferredThreadCredentialsWithOptions:]_block_invoke_2
+ ___91-[HMMTRProtocolMap servicesForDeviceTypes:device:endpoint:callbackQueue:completionHandler:]_block_invoke.429
+ ___92-[HMMTRAccessoryServer _createFirmwareUpdateServiceWithInstanceID:device:completionHandler:]_block_invoke.780
+ ___92-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fabricUUID:fatalError:]_block_invoke.318
+ ___92-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fabricUUID:fatalError:]_block_invoke.319
+ ___94-[HMMTRAccessoryServer updateAccessoryControlToAdministratorNodes:sharedUserNodes:completion:]_block_invoke.834
+ ___94-[HMMTRAccessoryServerBrowser _handleAddOrUpdateWithDiscriminator:vendorID:productID:overBLE:]_block_invoke.167
+ ___96-[HMMTRProtocolMap servicesOfMTRDevice:forDeviceTypes:endpoint:callbackQueue:completionHandler:]_block_invoke.430
+ ___96-[HMMTRSystemCommissionerPairingManager _donateThreadNetwork:toSystemCommissionerNode:endpoint:]_block_invoke
+ ___96-[HMMTRSystemCommissionerPairingManager _donateThreadNetworksToSystemCommissionerNode:endpoint:]_block_invoke
+ ___96-[HMMTRSystemCommissionerPairingManager _donateThreadNetworksToSystemCommissionerNode:endpoint:]_block_invoke_2
+ ___96-[HMMTRSystemCommissionerPairingManager _retrieveTHClientPreferredNetworkInternallyOnMdnsAndSig]_block_invoke
+ ___97-[HMMTRAccessoryServerBrowser removeAccessoryServer:fromDiscoveredAccessoryServerListWithReason:]_block_invoke.303
+ ___99-[HMMTRAccessoryServer _tryPairingWithOnboardingPayload:systemCommissionerPairings:pairingManager:]_block_invoke.257
+ ___99-[HMMTRAccessoryServer _tryPairingWithOnboardingPayload:systemCommissionerPairings:pairingManager:]_block_invoke.258
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.515
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.516
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.523
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.524
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke_2.519
+ ___99-[HMMTRSystemCommissionerPairingManager _provisionBorderRouterWithSystemCommissionerNode:endpoint:]_block_invoke
+ ___99-[HMMTRSystemCommissionerPairingManager _provisionBorderRouterWithSystemCommissionerNode:endpoint:]_block_invoke_2
+ ___99-[HMMTRSystemCommissionerPairingManager _provisionBorderRouterWithSystemCommissionerNode:endpoint:]_block_invoke_3
+ ___Block_byref_object_copy_.10156
+ ___Block_byref_object_copy_.10902
+ ___Block_byref_object_copy_.11585
+ ___Block_byref_object_copy_.12286
+ ___Block_byref_object_copy_.12451
+ ___Block_byref_object_copy_.1790
+ ___Block_byref_object_copy_.3148
+ ___Block_byref_object_copy_.3432
+ ___Block_byref_object_copy_.4561
+ ___Block_byref_object_copy_.5728
+ ___Block_byref_object_copy_.5883
+ ___Block_byref_object_copy_.7685
+ ___Block_byref_object_copy_.8104
+ ___Block_byref_object_copy_.9204
+ ___Block_byref_object_dispose_.10157
+ ___Block_byref_object_dispose_.10903
+ ___Block_byref_object_dispose_.11586
+ ___Block_byref_object_dispose_.12287
+ ___Block_byref_object_dispose_.12452
+ ___Block_byref_object_dispose_.1791
+ ___Block_byref_object_dispose_.3149
+ ___Block_byref_object_dispose_.3433
+ ___Block_byref_object_dispose_.4562
+ ___Block_byref_object_dispose_.5729
+ ___Block_byref_object_dispose_.5884
+ ___Block_byref_object_dispose_.7686
+ ___Block_byref_object_dispose_.8105
+ ___Block_byref_object_dispose_.9205
+ ___block_descriptor_32_e101_{_HMFFutureBlockOutcome=q}16?0"MTRGeneralCommissioningClusterCommissioningCompleteResponseParams"8l
+ ___block_descriptor_32_e91_{_HMFFutureBlockOutcome=q}16?0"MTRGeneralCommissioningClusterArmFailSafeResponseParams"8l
+ ___block_descriptor_48_e8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e46_v32?0"THCredentials"8"NSUUID"16"NSError"24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e50_{_HMFFutureBlockOutcome=q}16?0"<HMFAlwaysNil>"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e95_{_HMFFutureBlockOutcome=q}16?0"MTRThreadBorderRouterManagementClusterDatasetResponseParams"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e34_{_HMFFutureBlockOutcome=q}16?08ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e49_{_HMFFutureBlockOutcome=q}16?0"THCredentials"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e50_{_HMFFutureBlockOutcome=q}16?0"<HMFAlwaysNil>"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56r_e24_v32?0"NSError"8Q16^B24ls32l8s40l8r56l8s48l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80r_e40_v16?0"HAPCharacteristicResponseTuple"8ls32l8s40l8s48l8r80l8s56l8s64l8s72l8
+ ___block_descriptor_89_e8_32s40s48s56s64bs72r_e29_v24?0"NSArray"8"NSError"16lr72l8s32l8s64l8s40l8s48l8s56l8
+ ___block_literal_global.10029
+ ___block_literal_global.10627
+ ___block_literal_global.109
+ ___block_literal_global.11179
+ ___block_literal_global.11404
+ ___block_literal_global.1142
+ ___block_literal_global.11620
+ ___block_literal_global.11758
+ ___block_literal_global.11888
+ ___block_literal_global.120
+ ___block_literal_global.12106
+ ___block_literal_global.1258
+ ___block_literal_global.1364
+ ___block_literal_global.1441
+ ___block_literal_global.1658
+ ___block_literal_global.1913
+ ___block_literal_global.1967
+ ___block_literal_global.2013
+ ___block_literal_global.208
+ ___block_literal_global.2099
+ ___block_literal_global.2464
+ ___block_literal_global.2604
+ ___block_literal_global.282
+ ___block_literal_global.2909
+ ___block_literal_global.3052
+ ___block_literal_global.3081
+ ___block_literal_global.309
+ ___block_literal_global.312
+ ___block_literal_global.3173
+ ___block_literal_global.3324
+ ___block_literal_global.3516
+ ___block_literal_global.353
+ ___block_literal_global.3685
+ ___block_literal_global.372
+ ___block_literal_global.3809
+ ___block_literal_global.4322
+ ___block_literal_global.4655
+ ___block_literal_global.4947
+ ___block_literal_global.5081
+ ___block_literal_global.5182
+ ___block_literal_global.522
+ ___block_literal_global.544
+ ___block_literal_global.5445
+ ___block_literal_global.5617
+ ___block_literal_global.5866
+ ___block_literal_global.6050
+ ___block_literal_global.611
+ ___block_literal_global.6189
+ ___block_literal_global.6298
+ ___block_literal_global.6332
+ ___block_literal_global.6353
+ ___block_literal_global.6603
+ ___block_literal_global.6616
+ ___block_literal_global.6710
+ ___block_literal_global.6804
+ ___block_literal_global.6898
+ ___block_literal_global.7001
+ ___block_literal_global.7095
+ ___block_literal_global.7234
+ ___block_literal_global.7375
+ ___block_literal_global.7484
+ ___block_literal_global.7555
+ ___block_literal_global.785
+ ___block_literal_global.7887
+ ___block_literal_global.792
+ ___block_literal_global.801
+ ___block_literal_global.805
+ ___block_literal_global.81
+ ___block_literal_global.8115
+ ___block_literal_global.84
+ ___block_literal_global.8449
+ ___block_literal_global.8574
+ ___block_literal_global.86
+ ___block_literal_global.8708
+ ___block_literal_global.871
+ ___block_literal_global.88
+ ___block_literal_global.9238
+ ___block_literal_global.956
+ ___block_literal_global.9636
+ ___block_literal_global.982
+ ___block_literal_global.9955
+ _logCategory._hmf_once_t0.3051
+ _logCategory._hmf_once_t0.5616
+ _logCategory._hmf_once_t0.6331
+ _logCategory._hmf_once_t108
+ _logCategory._hmf_once_t13.3172
+ _logCategory._hmf_once_t13.3515
+ _logCategory._hmf_once_t14.1273
+ _logCategory._hmf_once_t14.6615
+ _logCategory._hmf_once_t14.6709
+ _logCategory._hmf_once_t14.6803
+ _logCategory._hmf_once_t14.7000
+ _logCategory._hmf_once_t14.7094
+ _logCategory._hmf_once_t14.7233
+ _logCategory._hmf_once_t2.10028
+ _logCategory._hmf_once_t2.5181
+ _logCategory._hmf_once_t2.6297
+ _logCategory._hmf_once_t2.7374
+ _logCategory._hmf_once_t20.11757
+ _logCategory._hmf_once_t26.6897
+ _logCategory._hmf_once_t3.1363
+ _logCategory._hmf_once_t3.1440
+ _logCategory._hmf_once_t31.11887
+ _logCategory._hmf_once_t35
+ _logCategory._hmf_once_t4.3684
+ _logCategory._hmf_once_t4.7483
+ _logCategory._hmf_once_t6.2098
+ _logCategory._hmf_once_t68.12313
+ _logCategory._hmf_once_t683
+ _logCategory._hmf_once_t8.11403
+ _logCategory._hmf_once_t8.8573
+ _logCategory._hmf_once_t9.6049
+ _logCategory._hmf_once_v1.3053
+ _logCategory._hmf_once_v1.5618
+ _logCategory._hmf_once_v1.6333
+ _logCategory._hmf_once_v10.6051
+ _logCategory._hmf_once_v109
+ _logCategory._hmf_once_v14.3174
+ _logCategory._hmf_once_v14.3517
+ _logCategory._hmf_once_v15.1274
+ _logCategory._hmf_once_v15.6617
+ _logCategory._hmf_once_v15.6711
+ _logCategory._hmf_once_v15.6805
+ _logCategory._hmf_once_v15.7002
+ _logCategory._hmf_once_v15.7096
+ _logCategory._hmf_once_v15.7235
+ _logCategory._hmf_once_v21.11759
+ _logCategory._hmf_once_v27.6899
+ _logCategory._hmf_once_v3.10030
+ _logCategory._hmf_once_v3.5183
+ _logCategory._hmf_once_v3.6299
+ _logCategory._hmf_once_v3.7376
+ _logCategory._hmf_once_v32.11889
+ _logCategory._hmf_once_v36
+ _logCategory._hmf_once_v4.1365
+ _logCategory._hmf_once_v4.1442
+ _logCategory._hmf_once_v5.3686
+ _logCategory._hmf_once_v5.7485
+ _logCategory._hmf_once_v684
+ _logCategory._hmf_once_v69.12314
+ _logCategory._hmf_once_v7.2100
+ _logCategory._hmf_once_v9.11405
+ _logCategory._hmf_once_v9.8575
+ _objc_msgSend$_addNetworkToThreadNetworkDirectoryForDevice:endpoint:dataset:
+ _objc_msgSend$_armFailSafeForDevice:expiryLengthSeconds:
+ _objc_msgSend$_commissioningCompleteForDevice:
+ _objc_msgSend$_deviceForSystemCommissionerNode:
+ _objc_msgSend$_donateThreadNetwork:toSystemCommissionerNode:endpoint:
+ _objc_msgSend$_donateThreadNetworksToSystemCommissionerNode:endpoint:
+ _objc_msgSend$_generateThreadOperationalDataset
+ _objc_msgSend$_handlePairOnSystemCommissionerFabricStart
+ _objc_msgSend$_provisionBorderRouterWithSystemCommissionerNode:endpoint:
+ _objc_msgSend$_retrievePreferredThreadCredentialsWithOptions:
+ _objc_msgSend$_retrieveTHClientPreferredNetworkInternallyOnMdnsAndSig
+ _objc_msgSend$_retrieveThreadCredentialsFromSystemCommissionerNode:endpoint:
+ _objc_msgSend$_setActiveThreadDatasetForDevice:endpoint:dataset:
+ _objc_msgSend$_updateThreadCredentialManagementEnabled:forSystemCommissionerPairingUUID:completionHandler:
+ _objc_msgSend$addNetworkWithParams:expectedValues:expectedValueInterval:completion:
+ _objc_msgSend$any:
+ _objc_msgSend$armFailSafeWithParams:expectedValues:expectedValueInterval:completion:
+ _objc_msgSend$commissioneeInfo
+ _objc_msgSend$commissioningCompleteWithExpectedValues:expectedValueInterval:completion:
+ _objc_msgSend$dataWithContentsOfFile:options:error:
+ _objc_msgSend$dataset
+ _objc_msgSend$ensureCommissioningID
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$getActiveDatasetRequestWithExpectedValues:expectedValueInterval:completion:
+ _objc_msgSend$hmfAggregatedErrors
+ _objc_msgSend$hmf_appendObject:
+ _objc_msgSend$hmf_objectForKey:forDictionaryAtOffset:
+ _objc_msgSend$hmf_readObjectAtOffset:
+ _objc_msgSend$initWithDataset:borderAgentEUI:
+ _objc_msgSend$initWithUUID:nodeID:vendorID:productID:deviceType:serialNumber:name:setupPayload:threadCredentialManagementEnabled:
+ _objc_msgSend$makeSystemCommissionerPairingManagerWithQueue:browser:
+ _objc_msgSend$makeThreadRadioManagerWithBrowser:
+ _objc_msgSend$rawPlistAtKey:
+ _objc_msgSend$removeItemAtPath:error:
+ _objc_msgSend$retrieveHAPToCHIPClusterMapping:
+ _objc_msgSend$retrievePreferredNetworkInternallyOnMdnsAndSig:
+ _objc_msgSend$rootEndpoint
+ _objc_msgSend$setActiveDataset:
+ _objc_msgSend$setActiveDatasetRequestWithParams:expectedValues:expectedValueInterval:completion:
+ _objc_msgSend$setCommissioneeInfo:
+ _objc_msgSend$setOperationalDataset:
+ _objc_msgSend$setReadEndpointInformation:
+ _objc_msgSend$setThreadCredentialManagementEnabled:forSystemCommissionerFabricNode:
+ _objc_msgSend$setThreadCredentialManagementEndpoint:forSystemCommissionerFabricNode:
+ _objc_msgSend$stringByAppendingPathComponent:
+ _objc_msgSend$threadCredentialManagementEnabledForSystemCommissionerFabricNode:
+ _objc_msgSend$threadCredentialManagementEndpoint:
+ _objc_msgSend$threadCredentialManagementEndpointForSystemCommissionerFabricNode:
+ _objc_msgSend$threadCredentialManagementNodesAndEndpointsForSystemCommissioner
+ _objc_msgSend$timeout:
+ _objc_msgSend$writeToFile:atomically:
- -[HMMTRAccessoryServerBrowser initWithQueue:storeDirectoryURL:]
- -[HMMTRAccessoryServerBrowser setSystemCommissionerPairingManager:]
- -[HMMTRProtocolMap rawPlist]
- -[HMMTRProtocolMap retrieveHAPToCHIPClusterMapping]
- GCC_except_table1052
- GCC_except_table1112
- GCC_except_table1158
- GCC_except_table1166
- GCC_except_table1215
- GCC_except_table1223
- GCC_except_table1260
- GCC_except_table1297
- GCC_except_table1326
- GCC_except_table1527
- GCC_except_table1566
- GCC_except_table1718
- GCC_except_table1719
- GCC_except_table1720
- GCC_except_table1743
- GCC_except_table1744
- GCC_except_table1745
- GCC_except_table1746
- GCC_except_table1747
- GCC_except_table1753
- GCC_except_table1754
- GCC_except_table1756
- GCC_except_table1757
- GCC_except_table1818
- GCC_except_table1824
- GCC_except_table1901
- GCC_except_table2013
- GCC_except_table2015
- GCC_except_table2045
- GCC_except_table2053
- GCC_except_table2055
- GCC_except_table2103
- GCC_except_table2144
- GCC_except_table2206
- GCC_except_table2445
- GCC_except_table2449
- GCC_except_table2501
- GCC_except_table2542
- GCC_except_table2585
- GCC_except_table2587
- GCC_except_table2612
- GCC_except_table2613
- GCC_except_table2614
- GCC_except_table2635
- GCC_except_table2636
- GCC_except_table2637
- GCC_except_table2638
- GCC_except_table2639
- GCC_except_table2640
- GCC_except_table2641
- GCC_except_table2642
- GCC_except_table2654
- GCC_except_table2656
- GCC_except_table2691
- GCC_except_table2697
- GCC_except_table2708
- GCC_except_table2711
- GCC_except_table2715
- GCC_except_table2733
- GCC_except_table2737
- GCC_except_table2739
- GCC_except_table2758
- GCC_except_table2764
- GCC_except_table2782
- GCC_except_table2833
- GCC_except_table2834
- GCC_except_table3196
- GCC_except_table3197
- GCC_except_table3198
- GCC_except_table3202
- GCC_except_table3207
- GCC_except_table3210
- GCC_except_table3224
- GCC_except_table3240
- GCC_except_table3305
- GCC_except_table3324
- GCC_except_table3326
- GCC_except_table3333
- GCC_except_table3334
- GCC_except_table3357
- GCC_except_table3358
- GCC_except_table3367
- GCC_except_table3392
- GCC_except_table3395
- GCC_except_table3403
- GCC_except_table3422
- GCC_except_table3425
- GCC_except_table3461
- GCC_except_table3482
- GCC_except_table3484
- GCC_except_table3502
- GCC_except_table3568
- GCC_except_table3612
- GCC_except_table3630
- GCC_except_table3653
- GCC_except_table3657
- GCC_except_table3672
- GCC_except_table3673
- GCC_except_table3678
- GCC_except_table3685
- GCC_except_table3742
- GCC_except_table3762
- GCC_except_table3816
- GCC_except_table3821
- GCC_except_table3824
- GCC_except_table3903
- GCC_except_table3904
- GCC_except_table3959
- GCC_except_table3962
- GCC_except_table4024
- GCC_except_table4086
- GCC_except_table4090
- GCC_except_table4094
- GCC_except_table4097
- GCC_except_table4130
- GCC_except_table678
- GCC_except_table682
- GCC_except_table743
- GCC_except_table744
- GCC_except_table745
- GCC_except_table813
- GCC_except_table876
- GCC_except_table880
- GCC_except_table882
- GCC_except_table884
- GCC_except_table886
- GCC_except_table890
- GCC_except_table894
- GCC_except_table897
- GCC_except_table940
- GCC_except_table944
- GCC_except_table946
- _OBJC_IVAR_$_HMMTRProtocolMap._hapToCHIPClusterMappingArray
- _OBJC_IVAR_$_HMMTRProtocolMap._rawPlist
- ___101-[HMMTRAccessoryServer updateAccessoryControlToIncludeAdministratorNodes:sharedUserNodes:completion:]_block_invoke.824
- ___102-[HMMTRAccessoryServer updateAllCharacteristicValuesPostHAPServiceEnumerationForAccessory:completion:]_block_invoke.775
- ___107-[HMMTRAccessoryServerBrowser _fetchDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.202
- ___110-[HMMTRAccessoryServerBrowser removeAllDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.204
- ___112-[HMMTRAccessoryServer _updateAdditionalCharacteristicsFromCharacteristicUpdate:service:path:completionHandler:]_block_invoke.377
- ___114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke.900
- ___114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke.903
- ___114-[HMMTRProtocolMap _selectedServiceTypeForServiceArray:device:mtrDevice:endpoint:callbackQueue:completionHandler:]_block_invoke.422
- ___117-[HMMTRAccessoryServer _findSystemCommissionerPairingMatchingSetupPayload:systemCommissionerPairings:pairingManager:]_block_invoke.257
- ___117-[HMMTRAccessoryServer _findSystemCommissionerPairingMatchingSetupPayload:systemCommissionerPairings:pairingManager:]_block_invoke.258
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.498
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.499
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.500
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.501
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.502
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.503
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.505
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.507
- ___119-[HMMTRAccessoryServerBrowser removeDevicePairingFabricForSystemCommissionerDeviceWithNodeID:fabric:completionHandler:]_block_invoke.200
- ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.316
- ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.317
- ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.319
- ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.320
- ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.321
- ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.322
- ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.323
- ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.324
- ___278-[HMMTRAccessoryServerBrowser _stageAccessoryServerWithSetupPayload:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:commissioneeInfoHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke.187
- ___37-[HMMTRAccessoryServer finishPairing]_block_invoke.755
- ___37-[HMMTRAccessoryServer timerDidFire:]_block_invoke.274
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.630
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.631
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.632
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.633
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.635
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.639
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.640
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.641
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.634
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.643
- ___40-[HMMTRAccessoryServerBrowser configure]_block_invoke.131
- ___42-[HMMTRAccessoryServer _setupMatterDevice]_block_invoke.305
- ___43-[HMMTRAccessoryServer _setupThreadPairing]_block_invoke.460
- ___43-[HMMTRAccessoryServer _unpair:completion:]_block_invoke.297
- ___43-[HMMTRAccessoryServer discoverAccessories]_block_invoke.300
- ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.874
- ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.876
- ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.877
- ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.879
- ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke_2.875
- ___45-[HMMTRAccessoryServer stopPairingWithError:]_block_invoke.286
- ___47-[HMMTRAccessoryServer processAttributeReport:]_block_invoke.963
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.848
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.851
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.853
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke_2.852
- ___49-[HMMTRAccessoryServerBrowser startBluetoothScan]_block_invoke.355
- ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.807
- ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.811
- ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.812
- ___51-[HMMTRAccessoryServer device:receivedEventReport:]_block_invoke.964
- ___52-[HMMTRAccessoryServer populateACLEntriesForPairing]_block_invoke.628
- ___52-[HMMTRAccessoryServerBrowser _cleanupStagedServers]_block_invoke.306
- ___53-[HMMTRAccessoryServer _tryPairingUsingMatterSupport]_block_invoke.251
- ___55-[HMMTRAccessoryServer device:receivedAttributeReport:]_block_invoke.962
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.418
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.419
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.420
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.421
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.422
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.423
- ___58-[HMMTRProtocolMap _buildEventMapper:characteristicsDict:]_block_invoke.297
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.430
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.431
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.432
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.434
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.435
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.905
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.907
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.911
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.913
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.424
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.425
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.426
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.427
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.428
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.429
- ___62-[HMMTRAccessoryServerBrowser stopDiscoveringAccessoryServers]_block_invoke.176
- ___63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.805
- ___63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.806
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.478
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.479
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.480
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.481
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.482
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.483
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.448
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.449
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.450
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.451
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.452
- ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.926
- ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.927
- ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.928
- ___64-[HMMTRAccessoryServerBrowser _initializeAndStartBonjourBrowser]_block_invoke.139
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.443
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.444
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.445
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.446
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.447
- ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.437
- ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.438
- ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.439
- ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.442
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.467
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.468
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.469
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.472
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.476
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.477
- ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.410
- ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.415
- ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.417
- ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.177
- ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.180
- ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.182
- ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke_2.183
- ___71-[HMMTRAccessoryServer validateAttestationDeviceInfo:error:completion:]_block_invoke.276
- ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.395
- ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.402
- ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.403
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.461
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.462
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.463
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.465
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.466
- ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.263
- ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.264
- ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.265
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.800
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.801
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.803
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.804
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.776
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.777
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.787
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.795
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.796
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.799
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke_2.791
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.858
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.859
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.863
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke_2.865
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.289
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.290
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.291
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.292
- ___76-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithNodeID:completion:]_block_invoke.185
- ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.404
- ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.405
- ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.406
- ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.408
- ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.409
- ___79-[HMMTRAccessoryServerBrowser _updateAccessoryControlListForServer:completion:]_block_invoke.311
- ___82-[HMMTRAccessoryServer fetchColorControlClusterForHapAccessory:completionHandler:]_block_invoke.914
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.882
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.883
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.884
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.887
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke_2.886
- ___82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.151
- ___82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.153
- ___82-[HMMTRProtocolMap _buildValueMapper:characteristicsDict:operation:forMTRCluster:]_block_invoke.276
- ___83-[HMMTRAccessoryServer updateAccessoryControlToRemoveAdministratorNode:completion:]_block_invoke.825
- ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.381
- ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.383
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.888
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.889
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.890
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.891
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.895
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.896
- ___86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.929
- ___86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.930
- ___88-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:keepAliveOnly:]_block_invoke.347
- ___88-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:keepAliveOnly:]_block_invoke.348
- ___88-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:keepAliveOnly:]_block_invoke.349
- ___91-[HMMTRProtocolMap servicesForDeviceTypes:device:endpoint:callbackQueue:completionHandler:]_block_invoke.425
- ___92-[HMMTRAccessoryServer _createFirmwareUpdateServiceWithInstanceID:device:completionHandler:]_block_invoke.768
- ___92-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fabricUUID:fatalError:]_block_invoke.309
- ___92-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fabricUUID:fatalError:]_block_invoke.310
- ___94-[HMMTRAccessoryServer updateAccessoryControlToAdministratorNodes:sharedUserNodes:completion:]_block_invoke.823
- ___94-[HMMTRAccessoryServerBrowser _handleAddOrUpdateWithDiscriminator:vendorID:productID:overBLE:]_block_invoke.160
- ___96-[HMMTRProtocolMap servicesOfMTRDevice:forDeviceTypes:endpoint:callbackQueue:completionHandler:]_block_invoke.426
- ___97-[HMMTRAccessoryServerBrowser removeAccessoryServer:fromDiscoveredAccessoryServerListWithReason:]_block_invoke.294
- ___99-[HMMTRAccessoryServer _tryPairingWithOnboardingPayload:systemCommissionerPairings:pairingManager:]_block_invoke.254
- ___99-[HMMTRAccessoryServer _tryPairingWithOnboardingPayload:systemCommissionerPairings:pairingManager:]_block_invoke.255
- ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.509
- ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.510
- ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.511
- ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.512
- ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke_2.513
- ___Block_byref_object_copy_.10098
- ___Block_byref_object_copy_.10815
- ___Block_byref_object_copy_.11509
- ___Block_byref_object_copy_.12204
- ___Block_byref_object_copy_.12370
- ___Block_byref_object_copy_.1776
- ___Block_byref_object_copy_.3135
- ___Block_byref_object_copy_.3416
- ___Block_byref_object_copy_.4552
- ___Block_byref_object_copy_.5719
- ___Block_byref_object_copy_.7607
- ___Block_byref_object_copy_.8026
- ___Block_byref_object_copy_.9138
- ___Block_byref_object_dispose_.10099
- ___Block_byref_object_dispose_.10816
- ___Block_byref_object_dispose_.11510
- ___Block_byref_object_dispose_.12205
- ___Block_byref_object_dispose_.12371
- ___Block_byref_object_dispose_.1777
- ___Block_byref_object_dispose_.3136
- ___Block_byref_object_dispose_.3417
- ___Block_byref_object_dispose_.4553
- ___Block_byref_object_dispose_.5720
- ___Block_byref_object_dispose_.7608
- ___Block_byref_object_dispose_.8027
- ___Block_byref_object_dispose_.9139
- ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
- ___block_descriptor_80_e8_32s40s48s56s64s72r_e40_v16?0"HAPCharacteristicResponseTuple"8ls32l8s40l8r72l8s48l8s56l8s64l8
- ___block_descriptor_81_e8_32s40s48s56bs64r_e29_v24?0"NSArray"8"NSError"16lr64l8s32l8s56l8s40l8s48l8
- ___block_literal_global.103
- ___block_literal_global.10551
- ___block_literal_global.11107
- ___block_literal_global.11332
- ___block_literal_global.1134
- ___block_literal_global.114
- ___block_literal_global.11544
- ___block_literal_global.11682
- ___block_literal_global.11812
- ___block_literal_global.12029
- ___block_literal_global.1250
- ___block_literal_global.1356
- ___block_literal_global.1433
- ___block_literal_global.1650
- ___block_literal_global.1899
- ___block_literal_global.1953
- ___block_literal_global.1999
- ___block_literal_global.204
- ___block_literal_global.2085
- ___block_literal_global.2451
- ___block_literal_global.2590
- ___block_literal_global.278
- ___block_literal_global.2896
- ___block_literal_global.300
- ___block_literal_global.303.9095
- ___block_literal_global.3039
- ___block_literal_global.3068
- ___block_literal_global.3160
- ___block_literal_global.3311
- ___block_literal_global.344
- ___block_literal_global.3503
- ___block_literal_global.363
- ___block_literal_global.3675
- ___block_literal_global.3799
- ___block_literal_global.4313
- ___block_literal_global.4646
- ___block_literal_global.4938
- ___block_literal_global.5072
- ___block_literal_global.516
- ___block_literal_global.5173
- ___block_literal_global.540
- ___block_literal_global.5436
- ___block_literal_global.5608
- ___block_literal_global.5846
- ___block_literal_global.5976
- ___block_literal_global.6117
- ___block_literal_global.614
- ___block_literal_global.6226
- ___block_literal_global.6260
- ___block_literal_global.6281
- ___block_literal_global.6531
- ___block_literal_global.6544
- ___block_literal_global.6638
- ___block_literal_global.6732
- ___block_literal_global.6826
- ___block_literal_global.6929
- ___block_literal_global.7023
- ___block_literal_global.7162
- ___block_literal_global.7303
- ___block_literal_global.7408
- ___block_literal_global.7477
- ___block_literal_global.75.9895
- ___block_literal_global.773
- ___block_literal_global.780
- ___block_literal_global.7809
- ___block_literal_global.790
- ___block_literal_global.794
- ___block_literal_global.80
- ___block_literal_global.8037
- ___block_literal_global.8371
- ___block_literal_global.8495
- ___block_literal_global.861
- ___block_literal_global.8629
- ___block_literal_global.9170
- ___block_literal_global.946
- ___block_literal_global.9574
- ___block_literal_global.971
- ___block_literal_global.9894
- ___block_literal_global.9970
- _logCategory._hmf_once_t0.3038
- _logCategory._hmf_once_t0.5607
- _logCategory._hmf_once_t0.6259
- _logCategory._hmf_once_t106
- _logCategory._hmf_once_t13.3159
- _logCategory._hmf_once_t13.3502
- _logCategory._hmf_once_t14.1265
- _logCategory._hmf_once_t14.6543
- _logCategory._hmf_once_t14.6637
- _logCategory._hmf_once_t14.6731
- _logCategory._hmf_once_t14.6928
- _logCategory._hmf_once_t14.7022
- _logCategory._hmf_once_t14.7161
- _logCategory._hmf_once_t15
- _logCategory._hmf_once_t2.5172
- _logCategory._hmf_once_t2.6225
- _logCategory._hmf_once_t2.7302
- _logCategory._hmf_once_t2.9969
- _logCategory._hmf_once_t20.11681
- _logCategory._hmf_once_t26.6825
- _logCategory._hmf_once_t3.1355
- _logCategory._hmf_once_t3.1432
- _logCategory._hmf_once_t31.11811
- _logCategory._hmf_once_t4.3674
- _logCategory._hmf_once_t4.7407
- _logCategory._hmf_once_t6.2084
- _logCategory._hmf_once_t674
- _logCategory._hmf_once_t68.12230
- _logCategory._hmf_once_t8.11331
- _logCategory._hmf_once_t8.8494
- _logCategory._hmf_once_t9.5975
- _logCategory._hmf_once_v1.3040
- _logCategory._hmf_once_v1.5609
- _logCategory._hmf_once_v1.6261
- _logCategory._hmf_once_v10.5977
- _logCategory._hmf_once_v107
- _logCategory._hmf_once_v14.3161
- _logCategory._hmf_once_v14.3504
- _logCategory._hmf_once_v15.1266
- _logCategory._hmf_once_v15.6545
- _logCategory._hmf_once_v15.6639
- _logCategory._hmf_once_v15.6733
- _logCategory._hmf_once_v15.6930
- _logCategory._hmf_once_v15.7024
- _logCategory._hmf_once_v15.7163
- _logCategory._hmf_once_v16
- _logCategory._hmf_once_v21.11683
- _logCategory._hmf_once_v27.6827
- _logCategory._hmf_once_v3.5174
- _logCategory._hmf_once_v3.6227
- _logCategory._hmf_once_v3.7304
- _logCategory._hmf_once_v3.9971
- _logCategory._hmf_once_v32.11813
- _logCategory._hmf_once_v4.1357
- _logCategory._hmf_once_v4.1434
- _logCategory._hmf_once_v5.3676
- _logCategory._hmf_once_v5.7409
- _logCategory._hmf_once_v675
- _logCategory._hmf_once_v69.12231
- _logCategory._hmf_once_v7.2086
- _logCategory._hmf_once_v9.11333
- _logCategory._hmf_once_v9.8496
- _objc_msgSend$initWithUUID:nodeID:vendorID:productID:deviceType:serialNumber:name:setupPayload:
- _objc_msgSend$retrieveHAPToCHIPClusterMapping
CStrings:
+ "!_commissioningID"
+ "%{public}@Accessory is already paired to system commissioner fabric with node ID %@. Completing Apple Home pairing."
+ "%{public}@Assigned System Commissioner pairing UUID %@"
+ "%{public}@Attempting to provision unconfigured Border Router on System Commissioner node %@"
+ "%{public}@Calling didUpdateValuesForCharacteristics for %@ from handling reports %@"
+ "%{public}@Calling didUpdateValuesForCharacteristics for %@ from processing report %@"
+ "%{public}@Calling didUpdateValuesForCharacteristics for %@ from read requests %@"
+ "%{public}@Custom handler ignored report %@ for characteristic %@"
+ "%{public}@Donating Thread network '%@' (%@) to system commissioner node %@"
+ "%{public}@Failed to acquire System Commissioner device controller"
+ "%{public}@Failed to donate Thread credentials to System Commissioner node %@: %@"
+ "%{public}@Failed to mmap Matter protocol mapping data: %@"
+ "%{public}@Failed to remove Matter protocol mapping file: %@"
+ "%{public}@Generated System Commissioner pairing UUID %@"
+ "%{public}@No characteristic found for attribute report: endpoint:%@ cluster:%@ attribute:%@"
+ "%{public}@Successfully donated Thread network '%@' (%@) to Thread Network Directory of system commissioner node %@"
+ "%{public}@Successfully provisioned Border Router on System Commissioner node %@"
+ "%{public}@Successfully retrieved Thread dataset from System Commissioner node %@"
+ "%{public}@Thread Border Router is not configured for System Commissioner node %@"
+ "%{public}@Thread credential management is not supported for System Commissioner pairing with UUID = %@"
+ "%{public}@Updated characteristic %@ from report: %@"
+ "@\"HMMTRSystemCommissionerPairingManager\"32@0:8@\"NSObject<OS_dispatch_queue>\"16@\"HMMTRAccessoryServerBrowser\"24"
+ "@\"HMMTRThreadRadioManager\"24@0:8@\"HMMTRAccessoryServerBrowser\"16"
+ "@\"MTRCommissioneeInfo\""
+ "@32@0:8@16Q24"
+ "CommissioneeInfo must be available"
+ "Failed to generate dataset"
+ "General Commissioning Error %@"
+ "HMD.MTRPlugin.MTS.TCM.ep"
+ "HMD.MTRPlugin.MTS.TCM.on"
+ "HMMTRAccessoryServerBrowserDataSource"
+ "HMMTRAccessoryServerBrowserDataSourceDefault"
+ "MatterHRAPDeviceTypes"
+ "MatterThreadCredentialsRetrievalTimeout"
+ "No MTRDevice"
+ "No dataset available for network"
+ "T@\"MTRCommissioneeInfo\",&,N,V_commissioneeInfo"
+ "T@\"NSDictionary\",R,N"
+ "_addNetworkToThreadNetworkDirectoryForDevice:endpoint:dataset:"
+ "_armFailSafeForDevice:expiryLengthSeconds:"
+ "_commissioneeInfo"
+ "_commissioningCompleteForDevice:"
+ "_deviceForSystemCommissionerNode:"
+ "_donateThreadNetwork:toSystemCommissionerNode:endpoint:"
+ "_donateThreadNetworksToSystemCommissionerNode:endpoint:"
+ "_generateThreadOperationalDataset"
+ "_handlePairOnSystemCommissionerFabricStart"
+ "_mapData"
+ "_provisionBorderRouterWithSystemCommissionerNode:endpoint:"
+ "_retrievePreferredThreadCredentialsWithOptions:"
+ "_retrieveTHClientPreferredNetworkInternallyOnMdnsAndSig"
+ "_retrieveThreadCredentialsFromSystemCommissionerNode:endpoint:"
+ "_setActiveThreadDatasetForDevice:endpoint:dataset:"
+ "_updateThreadCredentialManagementEnabled:forSystemCommissionerPairingUUID:completionHandler:"
+ "addNetworkWithParams:expectedValues:expectedValueInterval:completion:"
+ "any:"
+ "armFailSafeWithParams:expectedValues:expectedValueInterval:completion:"
+ "commissioneeInfo"
+ "commissioningCompleteWithExpectedValues:expectedValueInterval:completion:"
+ "dataWithContentsOfFile:options:error:"
+ "dataset"
+ "ensureCommissioningID"
+ "enumerateObjectsUsingBlock:"
+ "getActiveDatasetRequestWithExpectedValues:expectedValueInterval:completion:"
+ "hapToCHIPClusterMappingArrayOffset"
+ "hmfAggregatedErrors"
+ "hmf_appendObject:"
+ "hmf_objectForKey:forDictionaryAtOffset:"
+ "hmf_readObjectAtOffset:"
+ "initWithDataset:borderAgentEUI:"
+ "initWithQueue:storeDirectoryURL:dataSource:"
+ "initWithUUID:nodeID:vendorID:productID:deviceType:serialNumber:name:setupPayload:threadCredentialManagementEnabled:"
+ "makeSystemCommissionerPairingManagerWithQueue:browser:"
+ "makeThreadRadioManagerWithBrowser:"
+ "rawPlistAtKey:"
+ "removeItemAtPath:error:"
+ "retrieveHAPToCHIPClusterMapping:"
+ "retrievePreferredNetworkInternallyOnMdnsAndSig:"
+ "retrievePreferredThreadCredentialsWithOptions:completionHandler:"
+ "rootEndpoint"
+ "setActiveDataset:"
+ "setActiveDatasetRequestWithParams:expectedValues:expectedValueInterval:completion:"
+ "setCommissioneeInfo:"
+ "setOperationalDataset:"
+ "setReadEndpointInformation:"
+ "setThreadCredentialManagementEnabled:forSystemCommissionerFabricNode:"
+ "setThreadCredentialManagementEndpoint:forSystemCommissionerFabricNode:"
+ "stringByAppendingPathComponent:"
+ "threadCredentialManagementEnabledForSystemCommissionerFabricNode:"
+ "threadCredentialManagementEndpoint:"
+ "threadCredentialManagementEndpointForSystemCommissionerFabricNode:"
+ "threadCredentialManagementNodesAndEndpointsForSystemCommissioner"
+ "timeout:"
+ "updateThreadCredentialManagementEnabled:forSystemCommissionerPairingUUID:completionHandler:"
+ "v32@?0@\"NSError\"8Q16^B24"
+ "v36@0:8B16@20@?28"
+ "writeToFile:atomically:"
+ "{_HMFFutureBlockOutcome=q@}16@?0@\"MTRGeneralCommissioningClusterArmFailSafeResponseParams\"8"
+ "{_HMFFutureBlockOutcome=q@}16@?0@\"MTRGeneralCommissioningClusterCommissioningCompleteResponseParams\"8"
+ "{_HMFFutureBlockOutcome=q@}16@?0@\"MTRThreadBorderRouterManagementClusterDatasetResponseParams\"8"
+ "{_HMFFutureBlockOutcome=q@}16@?0@\"THCredentials\"8"
+ "\xf0\x82\xf0\xf0\xd1\xc1"
- "%{public}@Accessory is already paired to system commissioner fabric. Completing Apple Home pairing."
- "%{public}@Updated characteristic from report: %@"
- "T@\"NSDictionary\",R,N,V_hapToCHIPClusterMappingArray"
- "T@\"NSDictionary\",R,N,V_rawPlist"
- "_hapToCHIPClusterMappingArray"
- "_rawPlist"
- "initWithQueue:storeDirectoryURL:"
- "initWithUUID:nodeID:vendorID:productID:deviceType:serialNumber:name:setupPayload:"
- "rawPlist"
- "retrieveHAPToCHIPClusterMapping"
- "setSystemCommissionerPairingManager:"
- "\xf0\x82\xf0\xf0\xc1\xc1"

```
