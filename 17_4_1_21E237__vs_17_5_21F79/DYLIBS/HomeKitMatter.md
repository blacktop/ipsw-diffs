## HomeKitMatter

> `/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter`

```diff

-1124.5.8.1.1
-  __TEXT.__text: 0xf7778
-  __TEXT.__auth_stubs: 0x970
-  __TEXT.__objc_methlist: 0x6fc8
+1124.6.30.0.1
+  __TEXT.__text: 0xfacd4
+  __TEXT.__auth_stubs: 0x9d0
+  __TEXT.__objc_methlist: 0x70f0
   __TEXT.__const: 0xb8
-  __TEXT.__gcc_except_tab: 0x15b0
-  __TEXT.__cstring: 0x4725
-  __TEXT.__oslogstring: 0x20517
+  __TEXT.__gcc_except_tab: 0x15c8
+  __TEXT.__cstring: 0x4f14
+  __TEXT.__oslogstring: 0x209ac
   __TEXT.__ustring: 0x68
-  __TEXT.__unwind_info: 0x22c4
-  __TEXT.__objc_classname: 0xcc5
-  __TEXT.__objc_methname: 0x1bc78
-  __TEXT.__objc_methtype: 0x253a
-  __TEXT.__objc_stubs: 0x117c0
+  __TEXT.__dlopen_cstrs: 0x58
+  __TEXT.__unwind_info: 0x2324
+  __TEXT.__objc_classname: 0xdb6
+  __TEXT.__objc_methname: 0x1c642
+  __TEXT.__objc_methtype: 0x2fa2
+  __TEXT.__objc_stubs: 0x11a40
   __DATA_CONST.__got: 0x1b8
-  __DATA_CONST.__const: 0x3828
-  __DATA_CONST.__objc_classlist: 0x308
+  __DATA_CONST.__const: 0x3a28
+  __DATA_CONST.__objc_classlist: 0x310
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0xb8
+  __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x9500
-  __DATA_CONST.__objc_selrefs: 0x50c0
-  __DATA_CONST.__objc_classrefs: 0x708
-  __DATA_CONST.__objc_superrefs: 0x240
-  __DATA_CONST.__objc_arraydata: 0x1f0
-  __AUTH_CONST.__objc_const: 0x2a78
-  __AUTH_CONST.__cfstring: 0x4f80
-  __AUTH_CONST.__const: 0x860
-  __AUTH_CONST.__objc_intobj: 0x10f8
-  __AUTH_CONST.__objc_arrayobj: 0x150
+  __DATA_CONST.__objc_const: 0x9d60
+  __DATA_CONST.__objc_selrefs: 0x5148
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x718
+  __DATA_CONST.__objc_superrefs: 0x250
+  __DATA_CONST.__objc_arraydata: 0x220
+  __AUTH_CONST.__objc_const: 0x2b08
+  __AUTH_CONST.__cfstring: 0x5480
+  __AUTH_CONST.__const: 0x8a0
+  __AUTH_CONST.__objc_intobj: 0x1140
+  __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x4c8
+  __AUTH_CONST.__objc_dictobj: 0x50
+  __AUTH_CONST.__auth_got: 0x4f8
   __AUTH.__objc_data: 0x1680
-  __DATA.__objc_ivar: 0x7f8
-  __DATA.__data: 0x8a0
-  __DATA.__bss: 0x2b8
-  __DATA_DIRTY.__objc_data: 0x7d0
-  __DATA_DIRTY.__bss: 0xa0
+  __DATA.__objc_ivar: 0x814
+  __DATA.__data: 0xaa0
+  __DATA.__bss: 0x2d8
+  __DATA_DIRTY.__objc_data: 0x820
+  __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/HomeKit.framework/HomeKit
   - /System/Library/Frameworks/Matter.framework/Matter
   - /System/Library/Frameworks/MatterSupport.framework/MatterSupport
   - /System/Library/Frameworks/Network.framework/Network

   - /System/Library/PrivateFrameworks/HomeKitMetrics.framework/HomeKitMetrics
   - /System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities
   - /System/Library/PrivateFrameworks/RegulatoryDomain.framework/RegulatoryDomain
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3210
-  Symbols:   11136
-  CStrings:  6668
+  Functions: 3245
+  Symbols:   11297
+  CStrings:  6845
 
Symbols:
+ +[HMMTRAccessoryPairingEndContext hapContextWithStep:error:]
+ +[HMMTRAccessoryPairingEndContext hmmtrContextWithCancelledError:]
+ +[HMMTRAccessoryPairingEndContext hmmtrContextWithStep:error:]
+ +[HMMTRAccessoryPairingEndContext mtrContextWithStep:error:]
+ +[HMMTRAccessoryPairingEndContext otherContextWithStep:error:]
+ +[HMMTRUserAuthorizationForPairing logCategory]
+ -[HMMTRAccessoryPairingEndContext .cxx_destruct]
+ -[HMMTRAccessoryPairingEndContext attributeDescriptions]
+ -[HMMTRAccessoryPairingEndContext error]
+ -[HMMTRAccessoryPairingEndContext initWithStep:error:sourceErrorDomain:]
+ -[HMMTRAccessoryPairingEndContext sourceErrorDomain]
+ -[HMMTRAccessoryPairingEndContext step]
+ -[HMMTRAccessoryServer _handlePairingFailureWithError:context:]
+ -[HMMTRAccessoryServer _notifyDelegateOfPairingStep:]
+ -[HMMTRAccessoryServer _pairingComplete:context:]
+ -[HMMTRAccessoryServer _startPairingWithError:pairingEndContext:]
+ -[HMMTRAccessoryServer _startPairingWithReadyToCancelHandler:error:pairingEndContext:]
+ -[HMMTRAccessoryServer abortStagingWithError:context:]
+ -[HMMTRAccessoryServer controller:commissioningComplete:nodeID:metrics:]
+ -[HMMTRAccessoryServer controller:commissioningSessionEstablishmentDone:]
+ -[HMMTRAccessoryServer controller:statusUpdate:]
+ -[HMMTRAccessoryServerBrowser _notifyDelegateOfPairingStep:]
+ -[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]
+ -[HMMTRAccessoryServerBrowser userAuthorizationForPairing]
+ -[HMMTRAttestationStatus _requestUserPermissionForBridgeAccessory:completionHandler:]
+ -[HMMTRAttestationStatus setUserAuthorizationDelegate:]
+ -[HMMTRAttestationStatus userAuthorizationDelegate]
+ -[HMMTRUIDialogPresenter requestUserPermissionForBridgeAccessory:completionHandler:]
+ -[HMMTRUserAuthorizationForPairing .cxx_destruct]
+ -[HMMTRUserAuthorizationForPairing initWithUiDialogPresenter:]
+ -[HMMTRUserAuthorizationForPairing requestUserPermissionForBridgeAccessory:completionHandler:]
+ -[HMMTRUserAuthorizationForPairing setUiDialogPresenter:]
+ -[HMMTRUserAuthorizationForPairing uiDialogPresenter]
+ -[HMMTRVendorMetadataFileStore _processSupportedAccessories:]
+ -[HMMTRVendorMetadataFileStore batchedAccessories]
+ -[HMMTRVendorMetadataFileStore setBatchedAccessories:]
+ -[HMMTRVendorMetadataFileStore supportedAccessories:forProductGroup:isComplete:]
+ GCC_except_table1016
+ GCC_except_table1144
+ GCC_except_table1145
+ GCC_except_table1165
+ GCC_except_table1166
+ GCC_except_table1167
+ GCC_except_table1170
+ GCC_except_table1172
+ GCC_except_table1173
+ GCC_except_table1174
+ GCC_except_table1175
+ GCC_except_table1176
+ GCC_except_table1177
+ GCC_except_table1178
+ GCC_except_table1229
+ GCC_except_table1235
+ GCC_except_table1335
+ GCC_except_table1358
+ GCC_except_table1387
+ GCC_except_table1392
+ GCC_except_table1425
+ GCC_except_table1451
+ GCC_except_table1468
+ GCC_except_table1516
+ GCC_except_table1686
+ GCC_except_table1690
+ GCC_except_table1741
+ GCC_except_table1798
+ GCC_except_table1843
+ GCC_except_table1864
+ GCC_except_table1865
+ GCC_except_table1876
+ GCC_except_table1877
+ GCC_except_table1878
+ GCC_except_table1879
+ GCC_except_table1880
+ GCC_except_table1881
+ GCC_except_table1882
+ GCC_except_table1889
+ GCC_except_table1891
+ GCC_except_table1895
+ GCC_except_table1913
+ GCC_except_table1927
+ GCC_except_table1933
+ GCC_except_table1944
+ GCC_except_table1946
+ GCC_except_table1954
+ GCC_except_table1970
+ GCC_except_table1976
+ GCC_except_table1983
+ GCC_except_table2072
+ GCC_except_table2334
+ GCC_except_table2339
+ GCC_except_table2342
+ GCC_except_table2352
+ GCC_except_table2416
+ GCC_except_table2431
+ GCC_except_table2433
+ GCC_except_table2440
+ GCC_except_table2441
+ GCC_except_table2466
+ GCC_except_table2467
+ GCC_except_table2501
+ GCC_except_table2540
+ GCC_except_table2573
+ GCC_except_table2577
+ GCC_except_table2593
+ GCC_except_table2594
+ GCC_except_table2620
+ GCC_except_table2687
+ GCC_except_table2723
+ GCC_except_table2731
+ GCC_except_table2746
+ GCC_except_table2780
+ GCC_except_table2781
+ GCC_except_table2786
+ GCC_except_table2794
+ GCC_except_table2912
+ GCC_except_table2917
+ GCC_except_table3019
+ GCC_except_table3022
+ GCC_except_table3158
+ GCC_except_table3166
+ GCC_except_table3169
+ GCC_except_table3197
+ GCC_except_table3219
+ GCC_except_table461
+ GCC_except_table462
+ GCC_except_table463
+ GCC_except_table494
+ GCC_except_table496
+ GCC_except_table550
+ GCC_except_table554
+ GCC_except_table556
+ GCC_except_table558
+ GCC_except_table560
+ GCC_except_table563
+ GCC_except_table629
+ GCC_except_table663
+ GCC_except_table721
+ GCC_except_table768
+ GCC_except_table776
+ GCC_except_table802
+ GCC_except_table832
+ _CoreAnalyticsLibraryCore.frameworkLibrary
+ _HMMTRAccessoryPairingStepAsString
+ _OBJC_CLASS_$_HMMTRAccessoryPairingEndContext
+ _OBJC_CLASS_$_HMMTRUserAuthorizationForPairing
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_IVAR_$_HMMTRAccessoryPairingEndContext._error
+ _OBJC_IVAR_$_HMMTRAccessoryPairingEndContext._sourceErrorDomain
+ _OBJC_IVAR_$_HMMTRAccessoryPairingEndContext._step
+ _OBJC_IVAR_$_HMMTRAccessoryServerBrowser._userAuthorizationForPairing
+ _OBJC_IVAR_$_HMMTRAttestationStatus._userAuthorizationDelegate
+ _OBJC_IVAR_$_HMMTRUserAuthorizationForPairing._uiDialogPresenter
+ _OBJC_IVAR_$_HMMTRVendorMetadataFileStore._batchedAccessories
+ _OBJC_METACLASS_$_HMMTRAccessoryPairingEndContext
+ _OBJC_METACLASS_$_HMMTRUserAuthorizationForPairing
+ __OBJC_$_CLASS_METHODS_HMMTRAccessoryPairingEndContext
+ __OBJC_$_CLASS_METHODS_HMMTRUserAuthorizationForPairing
+ __OBJC_$_INSTANCE_METHODS_HMMTRAccessoryPairingEndContext
+ __OBJC_$_INSTANCE_METHODS_HMMTRUserAuthorizationForPairing
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRAccessoryPairingEndContext
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRUserAuthorizationForPairing
+ __OBJC_$_PROP_LIST_HMMTRAccessoryPairingEndContext
+ __OBJC_$_PROP_LIST_HMMTRUserAuthorizationForPairing
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HAPAccessoryServerBrowserDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HAPAccessoryServerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HMMTRHAPAccessoryServerBrowserPairingDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HMMTRHAPAccessoryServerPairingDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HMMTRUserAuthorizationForPairingDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HAPAccessoryServerBrowserDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HAPAccessoryServerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_MTRDeviceControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HAPAccessoryServerBrowserDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HAPAccessoryServerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMMTRHAPAccessoryServerBrowserPairingDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMMTRHAPAccessoryServerPairingDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMMTRUserAuthorizationForPairingDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTRDeviceControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_HAPAccessoryServerBrowserDelegate
+ __OBJC_$_PROTOCOL_REFS_HAPAccessoryServerDelegate
+ __OBJC_$_PROTOCOL_REFS_HMMTRHAPAccessoryServerBrowserPairingDelegate
+ __OBJC_$_PROTOCOL_REFS_HMMTRHAPAccessoryServerPairingDelegate
+ __OBJC_$_PROTOCOL_REFS_HMMTRUserAuthorizationForPairingDelegate
+ __OBJC_$_PROTOCOL_REFS_MTRDeviceControllerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_HMMTRUserAuthorizationForPairing
+ __OBJC_CLASS_RO_$_HMMTRAccessoryPairingEndContext
+ __OBJC_CLASS_RO_$_HMMTRUserAuthorizationForPairing
+ __OBJC_LABEL_PROTOCOL_$_HAPAccessoryServerBrowserDelegate
+ __OBJC_LABEL_PROTOCOL_$_HAPAccessoryServerDelegate
+ __OBJC_LABEL_PROTOCOL_$_HMMTRHAPAccessoryServerBrowserPairingDelegate
+ __OBJC_LABEL_PROTOCOL_$_HMMTRHAPAccessoryServerPairingDelegate
+ __OBJC_LABEL_PROTOCOL_$_HMMTRUserAuthorizationForPairingDelegate
+ __OBJC_LABEL_PROTOCOL_$_MTRDeviceControllerDelegate
+ __OBJC_METACLASS_RO_$_HMMTRAccessoryPairingEndContext
+ __OBJC_METACLASS_RO_$_HMMTRUserAuthorizationForPairing
+ __OBJC_PROTOCOL_$_HAPAccessoryServerBrowserDelegate
+ __OBJC_PROTOCOL_$_HAPAccessoryServerDelegate
+ __OBJC_PROTOCOL_$_HMMTRHAPAccessoryServerBrowserPairingDelegate
+ __OBJC_PROTOCOL_$_HMMTRHAPAccessoryServerPairingDelegate
+ __OBJC_PROTOCOL_$_HMMTRUserAuthorizationForPairingDelegate
+ __OBJC_PROTOCOL_$_MTRDeviceControllerDelegate
+ __OBJC_PROTOCOL_REFERENCE_$_HMMTRHAPAccessoryServerBrowserPairingDelegate
+ __OBJC_PROTOCOL_REFERENCE_$_HMMTRHAPAccessoryServerPairingDelegate
+ ___100-[HMMTRAccessoryServer _endpointForOTARequestorWithTopology:device:callbackQueue:completionHandler:]_block_invoke.735
+ ___101-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:completionHandler:]_block_invoke.867
+ ___101-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:completionHandler:]_block_invoke.870
+ ___101-[HMMTRAccessoryServer updateAccessoryControlToIncludeAdministratorNodes:sharedUserNodes:completion:]_block_invoke.793
+ ___105-[HMMTRAccessoryServerBrowser prepareForPairingWithSetupPayload:fabric:fabricID:owner:completionHandler:]_block_invoke.172
+ ___107-[HMMTRAccessoryServerBrowser _fetchDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.140
+ ___110-[HMMTRAccessoryServerBrowser removeAllDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.142
+ ___113-[HMMTRAttestationStatus deviceAttestationCompletedForController:opaqueDeviceHandle:attestationDeviceInfo:error:]_block_invoke.10
+ ___113-[HMMTRAttestationStatus deviceAttestationCompletedForController:opaqueDeviceHandle:attestationDeviceInfo:error:]_block_invoke.11
+ ___113-[HMMTRAttestationStatus deviceAttestationCompletedForController:opaqueDeviceHandle:attestationDeviceInfo:error:]_block_invoke.13
+ ___113-[HMMTRAttestationStatus deviceAttestationCompletedForController:opaqueDeviceHandle:attestationDeviceInfo:error:]_block_invoke.6
+ ___113-[HMMTRAttestationStatus deviceAttestationCompletedForController:opaqueDeviceHandle:attestationDeviceInfo:error:]_block_invoke.9
+ ___116-[HMMTRAccessoryServerBrowser fetchCommissioningCertificatesForAccessoryWithOperationalPublicKey:completionHandler:]_block_invoke.199
+ ___117-[HMMTRAccessoryServer _findSystemCommissionerPairingMatchingSetupPayload:systemCommissionerPairings:pairingManager:]_block_invoke.235
+ ___117-[HMMTRAccessoryServer _findSystemCommissionerPairingMatchingSetupPayload:systemCommissionerPairings:pairingManager:]_block_invoke.236
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.487
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.488
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.489
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.490
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.493
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.491
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_3.492
+ ___119-[HMMTRAccessoryServerBrowser removeDevicePairingFabricForSystemCommissionerDeviceWithNodeID:fabric:completionHandler:]_block_invoke.138
+ ___133-[HMMTRAccessoryServerBrowser fetchCertificatesForSharedUserWithAccessoryNodeID:sharedUserType:publicKey:fabricID:completionHandler:]_block_invoke.190
+ ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke
+ ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.177
+ ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.180
+ ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.182
+ ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.183
+ ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.184
+ ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.185
+ ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.186
+ ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.187
+ ___254-[HMMTRAccessoryServerBrowser _stageAccessoryServerWithSetupPayload:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke.124
+ ___37-[HMMTRAccessoryServer finishPairing]_block_invoke.690
+ ___37-[HMMTRAccessoryServer timerDidFire:]_block_invoke.256
+ ___38-[HMMTRAccessoryServer setupReporting]_block_invoke.298
+ ___38-[HMMTRAccessoryServer setupReporting]_block_invoke.299
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.586
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.587
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.588
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.589
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.590
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.591
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.592
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.593
+ ___42-[HMMTRAccessoryServer setupThreadPairing]_block_invoke.449
+ ___43-[HMMTRAccessoryServer _unpair:completion:]_block_invoke.285
+ ___43-[HMMTRAccessoryServer _unpair:completion:]_block_invoke_2.288
+ ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.842
+ ___45-[HMMTRAccessoryServer enumerateHAPServices:]_block_invoke.747
+ ___45-[HMMTRAccessoryServer enumerateHAPServices:]_block_invoke.754
+ ___45-[HMMTRAccessoryServer stopPairingWithError:]_block_invoke.274
+ ___47+[HMMTRUserAuthorizationForPairing logCategory]_block_invoke
+ ___47-[HMMTRAccessoryServer processAttributeReport:]_block_invoke.923
+ ___48-[HMMTRAccessoryServer startPairingWithRequest:]_block_invoke.261
+ ___48-[HMMTRAccessoryServer startPairingWithRequest:]_block_invoke.262
+ ___48-[HMMTRAccessoryServer startPairingWithRequest:]_block_invoke_2.263
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.817
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.821
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke_2.820
+ ___49-[HMMTRAccessoryServer fetchColorControlCluster:]_block_invoke.878
+ ___49-[HMMTRAccessoryServer fetchColorControlCluster:]_block_invoke.879
+ ___49-[HMMTRAccessoryServer fetchColorControlCluster:]_block_invoke.880
+ ___49-[HMMTRAccessoryServerBrowser _deleteOldPairings]_block_invoke.170
+ ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.773
+ ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.777
+ ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.778
+ ___51-[HMMTRAccessoryServer device:receivedEventReport:]_block_invoke.924
+ ___52-[HMMTRAccessoryServerBrowser _cleanupStagedServers]_block_invoke.158
+ ___53-[HMMTRAccessoryServer _tryPairingUsingMatterSupport]_block_invoke.230
+ ___54-[HMMTRAccessoryServer abortStagingWithError:context:]_block_invoke
+ ___55-[HMMTRAccessoryServer _pairOnSystemCommissionerFabric]_block_invoke.691
+ ___55-[HMMTRAccessoryServer _pairOnSystemCommissionerFabric]_block_invoke.696
+ ___55-[HMMTRAccessoryServer device:receivedAttributeReport:]_block_invoke.922
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.413
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.414
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.415
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.416
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.417
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.423
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.424
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.425
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.427
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.428
+ ___59-[HMMTRAccessoryServerBrowser _preWarmCommissioningSession]_block_invoke.306
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.871
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.873
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.875
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.876
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.418
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.419
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.420
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.421
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.422
+ ___62-[HMMTRAccessoryServerBrowser stopDiscoveringAccessoryServers]_block_invoke.117
+ ___63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke
+ ___63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.771
+ ___63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.772
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.466
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.467
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.468
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.469
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.472
+ ___63-[HMMTRAccessoryServerBrowser startDiscoveringAccessoryServers]_block_invoke.114
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.433
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.434
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.435
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.436
+ ___64-[HMMTRAccessoryServerBrowser _initializeAndStartBonjourBrowser]_block_invoke.92
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.429
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.430
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.431
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.432
+ ___66-[HMMTRAccessoryServer _handlePartsListChanged:storage:endpoints:]_block_invoke.306
+ ___66-[HMMTRAccessoryServerBrowser storageDidUpdateData:isLocalChange:]_block_invoke.297
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.455
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.456
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.457
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.461
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.465
+ ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.411
+ ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.412
+ ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.119
+ ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.122
+ ___71-[HMMTRAccessoryServer validateAttestationDeviceInfo:error:completion:]_block_invoke.258
+ ___71-[HMMTRAccessoryServerBrowser createNewFabricDataForFabric:completion:]_block_invoke.168
+ ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.398
+ ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.399
+ ___72-[HMMTRAccessoryServer controller:commissioningComplete:nodeID:metrics:]_block_invoke
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.437
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.438
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.439
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.441
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.443
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.444
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.445
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.446
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.447
+ ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.448
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.450
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.451
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.452
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.453
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.454
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.767
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.768
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.770
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke_2.769
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.755
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.756
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.763
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.764
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.766
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke_2.757
+ ___73-[HMMTRAccessoryServerBrowser createNewFabricDataForFabricID:completion:]_block_invoke.166
+ ___73-[HMMTRAccessoryServerBrowser handleResidentReachabilityChangeForFabric:]_block_invoke.299
+ ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.826
+ ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.827
+ ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.831
+ ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke_2.833
+ ___74-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:]_block_invoke.300
+ ___74-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:]_block_invoke.301
+ ___74-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:]_block_invoke.302
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.277
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.278
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.279
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.280
+ ___79-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationWithCompletion:]_block_invoke.888
+ ___79-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationWithCompletion:]_block_invoke.889
+ ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.400
+ ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.401
+ ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.402
+ ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.404
+ ___79-[HMMTRAccessoryServerBrowser _updateAccessoryControlListForServer:completion:]_block_invoke.164
+ ___81-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fatalError:]_block_invoke.163
+ ___82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.103
+ ___82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.105
+ ___83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke.846
+ ___83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke.847
+ ___83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke.848
+ ___83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke.849
+ ___83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke.854
+ ___83-[HMMTRAccessoryServer updateAccessoryControlToRemoveAdministratorNode:completion:]_block_invoke.794
+ ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.363
+ ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.364
+ ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.366
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.855
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.856
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.857
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.858
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.861
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.862
+ ___84-[HMMTRUIDialogPresenter requestUserPermissionForBridgeAccessory:completionHandler:]_block_invoke
+ ___84-[HMMTRUIDialogPresenter requestUserPermissionForBridgeAccessory:completionHandler:]_block_invoke_2
+ ___85-[HMMTRAttestationStatus _requestUserPermissionForBridgeAccessory:completionHandler:]_block_invoke
+ ___86-[HMMTRAccessoryServer _startPairingWithReadyToCancelHandler:error:pairingEndContext:]_block_invoke
+ ___90-[HMMTRAccessoryServer _startLocallyDiscoveredAccessoryServerPairingWithRequest:fabricID:]_block_invoke.265
+ ___90-[HMMTRAccessoryServer _startLocallyDiscoveredAccessoryServerPairingWithRequest:fabricID:]_block_invoke.266
+ ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.495
+ ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.496
+ ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.497
+ ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.498
+ ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.500
+ ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke_2.499
+ ___93-[HMMTRAccessoryServerBrowser updateAccessoryACLAndGetNOCFromResidentForSharedUserForFabric:]_block_invoke.298
+ ___94-[HMMTRAccessoryServer updateAccessoryControlToAdministratorNodes:sharedUserNodes:completion:]_block_invoke.792
+ ___94-[HMMTRAccessoryServerBrowser _handleAddOrUpdateWithDiscriminator:vendorID:productID:overBLE:]_block_invoke.111
+ ___94-[HMMTRUserAuthorizationForPairing requestUserPermissionForBridgeAccessory:completionHandler:]_block_invoke
+ ___95-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:operationQueuePriority:completion:]_block_invoke.242
+ ___95-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:operationQueuePriority:completion:]_block_invoke.243
+ ___95-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:operationQueuePriority:completion:]_block_invoke.245
+ ___99-[HMMTRAccessoryServer _tryPairingWithOnboardingPayload:systemCommissionerPairings:pairingManager:]_block_invoke.233
+ ___Block_byref_object_copy_.2196
+ ___Block_byref_object_copy_.2478
+ ___Block_byref_object_copy_.3398
+ ___Block_byref_object_copy_.4318
+ ___Block_byref_object_copy_.4918
+ ___Block_byref_object_copy_.5226
+ ___Block_byref_object_copy_.5584
+ ___Block_byref_object_copy_.6136
+ ___Block_byref_object_copy_.6609
+ ___Block_byref_object_copy_.7100
+ ___Block_byref_object_copy_.7775
+ ___Block_byref_object_copy_.8326
+ ___Block_byref_object_copy_.9005
+ ___Block_byref_object_copy_.9215
+ ___Block_byref_object_dispose_.2197
+ ___Block_byref_object_dispose_.2479
+ ___Block_byref_object_dispose_.3399
+ ___Block_byref_object_dispose_.4319
+ ___Block_byref_object_dispose_.4919
+ ___Block_byref_object_dispose_.5227
+ ___Block_byref_object_dispose_.5585
+ ___Block_byref_object_dispose_.6137
+ ___Block_byref_object_dispose_.6610
+ ___Block_byref_object_dispose_.7101
+ ___Block_byref_object_dispose_.7776
+ ___Block_byref_object_dispose_.8327
+ ___Block_byref_object_dispose_.9006
+ ___Block_byref_object_dispose_.9216
+ ___CoreAnalyticsLibraryCore_block_invoke
+ ___block_descriptor_32_e30_v16?0"HMMTRAccessoryServer"8l
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32bs_e78_v24?0"MTRNetworkCommissioningClusterScanNetworksResponseParams"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_40_e8_32s_e114_v32?0"MTRNetworkCommissioningClusterScanNetworksResponseParams"8"NSError"16"HMMTRAccessoryPairingEndContext"24ls32l8
+ ___block_descriptor_40_e8_32s_e26_"NSMutableDictionary"8?0ls32l8
+ ___block_descriptor_48_e8_32s40bs_e20_v20?0B8"NSError"12ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e65_v32?0"NSArray"8"NSError"16"HMMTRAccessoryPairingEndContext"24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e65_v32?0"NSArray"8"NSError"16"HMMTRAccessoryPairingEndContext"24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e84_v32?0"MTRCommissioningParameters"8"NSError"16"HMMTRAccessoryPairingEndContext"24ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48r_e5_v8?0ls40l8s32l8r48l8
+ ___block_descriptor_56_e8_32s40s_e20_v20?0B8"NSError"12ls32l8s40l8
+ ___block_descriptor_57_e8_32s40s48bs_e20_v20?0B8"NSError"12ls32l8s48l8s40l8
+ ___block_descriptor_64_e8_32s40bs48r56r_e5_v8?0ls32l8r48l8r56l8s40l8
+ ___block_descriptor_64_e8_32s40s48r56r_e17_v16?0"NSError"8ls32l8r48l8r56l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e65_v32?0"NSArray"8"NSError"16"HMMTRAccessoryPairingEndContext"24ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e87_v24?0"MTRGeneralCommissioningClusterCommissioningCompleteResponseParams"8"NSError"16ls32l8s40l8s48l8s64l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e66_v32?0"NSString"8"NSError"16"HMMTRAccessoryPairingEndContext"24ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.1001
+ ___block_literal_global.1077
+ ___block_literal_global.1233
+ ___block_literal_global.141
+ ___block_literal_global.1475
+ ___block_literal_global.150
+ ___block_literal_global.1646
+ ___block_literal_global.1814
+ ___block_literal_global.1933
+ ___block_literal_global.2151
+ ___block_literal_global.2216
+ ___block_literal_global.230.7863
+ ___block_literal_global.2371
+ ___block_literal_global.2547
+ ___block_literal_global.264
+ ___block_literal_global.2700
+ ___block_literal_global.2810
+ ___block_literal_global.296
+ ___block_literal_global.317
+ ___block_literal_global.328
+ ___block_literal_global.3451
+ ___block_literal_global.3711
+ ___block_literal_global.3846
+ ___block_literal_global.4076
+ ___block_literal_global.4452
+ ___block_literal_global.4601
+ ___block_literal_global.4613
+ ___block_literal_global.466
+ ___block_literal_global.471
+ ___block_literal_global.4828
+ ___block_literal_global.4962
+ ___block_literal_global.5073
+ ___block_literal_global.5126
+ ___block_literal_global.5400
+ ___block_literal_global.5595
+ ___block_literal_global.585
+ ___block_literal_global.6174
+ ___block_literal_global.6392
+ ___block_literal_global.6572
+ ___block_literal_global.670
+ ___block_literal_global.6985
+ ___block_literal_global.7410
+ ___block_literal_global.746
+ ___block_literal_global.750
+ ___block_literal_global.753
+ ___block_literal_global.759
+ ___block_literal_global.765
+ ___block_literal_global.8013
+ ___block_literal_global.8229
+ ___block_literal_global.8360
+ ___block_literal_global.8500
+ ___block_literal_global.8609
+ ___block_literal_global.906
+ ___block_literal_global.9081
+ ___block_literal_global.937
+ ___getAnalyticsSendEventLazySymbolLoc_block_invoke
+ ___submitMatterMetrics_block_invoke
+ ___submitMatterMetrics_block_invoke.2
+ ___submitMatterMetrics_block_invoke_2
+ __sl_dlopen
+ __unnamed_array_storage.12
+ __unnamed_array_storage.13
+ __unnamed_array_storage.1376
+ __unnamed_array_storage.1792
+ __unnamed_array_storage.2360
+ __unnamed_array_storage.4816
+ __unnamed_array_storage.5156
+ __unnamed_array_storage.6086
+ __unnamed_array_storage.7
+ __unnamed_array_storage.7808
+ _abort_report_np
+ _audit_stringCoreAnalytics
+ _dispatch_queue_attr_make_with_qos_class
+ _dlerror
+ _dlsym
+ _free
+ _getAnalyticsSendEventLazySymbolLoc.ptr
+ _logCategory._hmf_once_t15.4451
+ _logCategory._hmf_once_t15.8608
+ _logCategory._hmf_once_t2.3845
+ _logCategory._hmf_once_t2.4600
+ _logCategory._hmf_once_t2.4827
+ _logCategory._hmf_once_t2.6984
+ _logCategory._hmf_once_t24.2604
+ _logCategory._hmf_once_t3.1000
+ _logCategory._hmf_once_t3.1076
+ _logCategory._hmf_once_t364
+ _logCategory._hmf_once_t4.5072
+ _logCategory._hmf_once_t51.3450
+ _logCategory._hmf_once_t594
+ _logCategory._hmf_once_t6.2215
+ _logCategory._hmf_once_t8.6571
+ _logCategory._hmf_once_t8.8228
+ _logCategory._hmf_once_t9.905
+ _logCategory._hmf_once_v10.907
+ _logCategory._hmf_once_v16.4453
+ _logCategory._hmf_once_v16.8610
+ _logCategory._hmf_once_v25.2605
+ _logCategory._hmf_once_v3.3847
+ _logCategory._hmf_once_v3.4602
+ _logCategory._hmf_once_v3.4829
+ _logCategory._hmf_once_v3.6986
+ _logCategory._hmf_once_v365
+ _logCategory._hmf_once_v4.1002
+ _logCategory._hmf_once_v4.1078
+ _logCategory._hmf_once_v5.5074
+ _logCategory._hmf_once_v52.3452
+ _logCategory._hmf_once_v595
+ _logCategory._hmf_once_v7.2217
+ _logCategory._hmf_once_v9.6573
+ _logCategory._hmf_once_v9.8230
+ _objc_msgSend$_handlePairingFailureWithError:context:
+ _objc_msgSend$_notifyDelegateOfPairingStep:
+ _objc_msgSend$_pairingComplete:context:
+ _objc_msgSend$_processSupportedAccessories:
+ _objc_msgSend$_requestUserPermissionForBridgeAccessory:completionHandler:
+ _objc_msgSend$_startPairingWithError:pairingEndContext:
+ _objc_msgSend$_startPairingWithReadyToCancelHandler:error:pairingEndContext:
+ _objc_msgSend$abortStagingWithError:context:
+ _objc_msgSend$accessoryServer:didStopPairingWithError:matterPairingEndContext:
+ _objc_msgSend$batchedAccessories
+ _objc_msgSend$conformsToProtocol:
+ _objc_msgSend$finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:
+ _objc_msgSend$getBatchedSupportedAccessories:assetLocationType:
+ _objc_msgSend$hapContextWithStep:error:
+ _objc_msgSend$hmmtrContextWithCancelledError:
+ _objc_msgSend$hmmtrContextWithStep:error:
+ _objc_msgSend$hmmtr_isMatterError
+ _objc_msgSend$initWithStep:error:sourceErrorDomain:
+ _objc_msgSend$initWithUiDialogPresenter:
+ _objc_msgSend$metricDataForKey:
+ _objc_msgSend$mtrContextWithStep:error:
+ _objc_msgSend$notifyMatterAccessoryPairingStep:
+ _objc_msgSend$otherContextWithStep:error:
+ _objc_msgSend$requestUserPermissionForBridgeAccessory:completionHandler:
+ _objc_msgSend$requestUserPermissionForBridgeAccessory:withContext:queue:completionHandler:
+ _objc_msgSend$setBatchedAccessories:
+ _objc_msgSend$setDeviceControllerDelegate:queue:
+ _objc_msgSend$setUserAuthorizationDelegate:
+ _objc_msgSend$sourceErrorDomain
+ _objc_msgSend$step
+ _objc_msgSend$userAuthorizationDelegate
+ _submitMatterMetrics.metricsQueue
+ _submitMatterMetrics.onceToken
- +[HMMTRDoorLock logCategory]
- -[HMMTRAccessoryServer _handlePairingFailureWithError:]
- -[HMMTRAccessoryServer _pairingComplete:]
- -[HMMTRAccessoryServer _startPairingWithError:]
- -[HMMTRAccessoryServer _startPairingWithReadyToCancelHandler:error:]
- -[HMMTRAccessoryServer abortStagingWithError:]
- -[HMMTRAccessoryServer onCommissioningComplete:]
- -[HMMTRAccessoryServer onPairingComplete:]
- -[HMMTRAccessoryServer onPairingDeleted:]
- -[HMMTRAccessoryServer onStatusUpdate:]
- -[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]
- -[HMMTRDoorLock readAttributeLockTargetStateWithCompletionHandler:]
- -[HMMTRSyncClusterDoorLock readAttributeLockTargetStateWithParams:]
- -[HMMTRVendorMetadataFileStore supportedAccessories:forProductGroup:]
- GCC_except_table1002
- GCC_except_table1130
- GCC_except_table1131
- GCC_except_table1149
- GCC_except_table1150
- GCC_except_table1151
- GCC_except_table1152
- GCC_except_table1153
- GCC_except_table1156
- GCC_except_table1158
- GCC_except_table1159
- GCC_except_table1160
- GCC_except_table1161
- GCC_except_table1162
- GCC_except_table1212
- GCC_except_table1218
- GCC_except_table1310
- GCC_except_table1333
- GCC_except_table1362
- GCC_except_table1395
- GCC_except_table1421
- GCC_except_table1438
- GCC_except_table1486
- GCC_except_table1659
- GCC_except_table1663
- GCC_except_table1714
- GCC_except_table1770
- GCC_except_table1815
- GCC_except_table1835
- GCC_except_table1836
- GCC_except_table1837
- GCC_except_table1848
- GCC_except_table1849
- GCC_except_table1850
- GCC_except_table1851
- GCC_except_table1852
- GCC_except_table1853
- GCC_except_table1854
- GCC_except_table1861
- GCC_except_table1867
- GCC_except_table1885
- GCC_except_table1899
- GCC_except_table1905
- GCC_except_table1916
- GCC_except_table1918
- GCC_except_table1926
- GCC_except_table1942
- GCC_except_table1948
- GCC_except_table1955
- GCC_except_table2044
- GCC_except_table2305
- GCC_except_table2310
- GCC_except_table2313
- GCC_except_table2323
- GCC_except_table2388
- GCC_except_table2402
- GCC_except_table2404
- GCC_except_table2411
- GCC_except_table2412
- GCC_except_table2437
- GCC_except_table2438
- GCC_except_table2472
- GCC_except_table2511
- GCC_except_table2544
- GCC_except_table2548
- GCC_except_table2564
- GCC_except_table2565
- GCC_except_table2591
- GCC_except_table2658
- GCC_except_table2694
- GCC_except_table2702
- GCC_except_table2717
- GCC_except_table2736
- GCC_except_table2751
- GCC_except_table2752
- GCC_except_table2757
- GCC_except_table2883
- GCC_except_table2888
- GCC_except_table2984
- GCC_except_table2987
- GCC_except_table3123
- GCC_except_table3127
- GCC_except_table3131
- GCC_except_table3134
- GCC_except_table3184
- GCC_except_table447
- GCC_except_table448
- GCC_except_table449
- GCC_except_table480
- GCC_except_table482
- GCC_except_table536
- GCC_except_table540
- GCC_except_table542
- GCC_except_table544
- GCC_except_table546
- GCC_except_table549
- GCC_except_table615
- GCC_except_table649
- GCC_except_table707
- GCC_except_table754
- GCC_except_table762
- GCC_except_table788
- GCC_except_table818
- _OBJC_CLASS_$_HMMTRDoorLock
- _OBJC_METACLASS_$_HMMTRDoorLock
- _OBJC_METACLASS_$_MTRBaseClusterDoorLock
- __OBJC_$_CLASS_METHODS_HMMTRDoorLock
- __OBJC_$_INSTANCE_METHODS_HMMTRDoorLock
- __OBJC_$_PROP_LIST_HMMTRDoorLock
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_MTRDevicePairingDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_MTRDevicePairingDelegate
- __OBJC_$_PROTOCOL_REFS_MTRDevicePairingDelegate
- __OBJC_CLASS_PROTOCOLS_$_HMMTRDoorLock
- __OBJC_CLASS_RO_$_HMMTRDoorLock
- __OBJC_LABEL_PROTOCOL_$_MTRDevicePairingDelegate
- __OBJC_METACLASS_RO_$_HMMTRDoorLock
- __OBJC_PROTOCOL_$_MTRDevicePairingDelegate
- ___100-[HMMTRAccessoryServer _endpointForOTARequestorWithTopology:device:callbackQueue:completionHandler:]_block_invoke.634
- ___101-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:completionHandler:]_block_invoke.764
- ___101-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:completionHandler:]_block_invoke.767
- ___101-[HMMTRAccessoryServer updateAccessoryControlToIncludeAdministratorNodes:sharedUserNodes:completion:]_block_invoke.692
- ___105-[HMMTRAccessoryServerBrowser prepareForPairingWithSetupPayload:fabric:fabricID:owner:completionHandler:]_block_invoke.170
- ___107-[HMMTRAccessoryServerBrowser _fetchDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.139
- ___110-[HMMTRAccessoryServerBrowser removeAllDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.141
- ___113-[HMMTRAttestationStatus deviceAttestationCompletedForController:opaqueDeviceHandle:attestationDeviceInfo:error:]_block_invoke.1
- ___113-[HMMTRAttestationStatus deviceAttestationCompletedForController:opaqueDeviceHandle:attestationDeviceInfo:error:]_block_invoke.4
- ___113-[HMMTRAttestationStatus deviceAttestationCompletedForController:opaqueDeviceHandle:attestationDeviceInfo:error:]_block_invoke.7
- ___116-[HMMTRAccessoryServerBrowser fetchCommissioningCertificatesForAccessoryWithOperationalPublicKey:completionHandler:]_block_invoke.196
- ___117-[HMMTRAccessoryServer _findSystemCommissionerPairingMatchingSetupPayload:systemCommissionerPairings:pairingManager:]_block_invoke.231
- ___117-[HMMTRAccessoryServer _findSystemCommissionerPairingMatchingSetupPayload:systemCommissionerPairings:pairingManager:]_block_invoke.232
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.480
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.481
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.482
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.483
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.486
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.484
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_3.485
- ___119-[HMMTRAccessoryServerBrowser removeDevicePairingFabricForSystemCommissionerDeviceWithNodeID:fabric:completionHandler:]_block_invoke.137
- ___133-[HMMTRAccessoryServerBrowser fetchCertificatesForSharedUserWithAccessoryNodeID:sharedUserType:publicKey:fabricID:completionHandler:]_block_invoke.187
- ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke
- ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.176
- ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.178
- ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.180
- ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.181
- ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.182
- ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.183
- ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.184
- ___154-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:]_block_invoke.185
- ___254-[HMMTRAccessoryServerBrowser _stageAccessoryServerWithSetupPayload:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke.123
- ___28+[HMMTRDoorLock logCategory]_block_invoke
- ___37-[HMMTRAccessoryServer finishPairing]_block_invoke.590
- ___37-[HMMTRAccessoryServer timerDidFire:]_block_invoke.252
- ___38-[HMMTRAccessoryServer setupReporting]_block_invoke.289
- ___38-[HMMTRAccessoryServer setupReporting]_block_invoke.291
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.575
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.579
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.580
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.581
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.583
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.584
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.585
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.586
- ___42-[HMMTRAccessoryServer setupThreadPairing]_block_invoke.442
- ___43-[HMMTRAccessoryServer _unpair:completion:]_block_invoke.281
- ___43-[HMMTRAccessoryServer _unpair:completion:]_block_invoke_2.284
- ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.739
- ___45-[HMMTRAccessoryServer enumerateHAPServices:]_block_invoke.646
- ___45-[HMMTRAccessoryServer enumerateHAPServices:]_block_invoke.653
- ___45-[HMMTRAccessoryServer stopPairingWithError:]_block_invoke.270
- ___46-[HMMTRAccessoryServer abortStagingWithError:]_block_invoke
- ___47-[HMMTRAccessoryServer processAttributeReport:]_block_invoke.821
- ___48-[HMMTRAccessoryServer onCommissioningComplete:]_block_invoke
- ___48-[HMMTRAccessoryServer startPairingWithRequest:]_block_invoke.257
- ___48-[HMMTRAccessoryServer startPairingWithRequest:]_block_invoke.258
- ___48-[HMMTRAccessoryServer startPairingWithRequest:]_block_invoke_2.259
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.716
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.720
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke_2.719
- ___49-[HMMTRAccessoryServer fetchColorControlCluster:]_block_invoke.775
- ___49-[HMMTRAccessoryServer fetchColorControlCluster:]_block_invoke.776
- ___49-[HMMTRAccessoryServer fetchColorControlCluster:]_block_invoke.777
- ___49-[HMMTRAccessoryServerBrowser _deleteOldPairings]_block_invoke.169
- ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.672
- ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.676
- ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.677
- ___51-[HMMTRAccessoryServer device:receivedEventReport:]_block_invoke.822
- ___52-[HMMTRAccessoryServerBrowser _cleanupStagedServers]_block_invoke.156
- ___53-[HMMTRAccessoryServer _tryPairingUsingMatterSupport]_block_invoke.226
- ___55-[HMMTRAccessoryServer _handlePairingFailureWithError:]_block_invoke
- ___55-[HMMTRAccessoryServer _handlePairingFailureWithError:]_block_invoke.670
- ___55-[HMMTRAccessoryServer _handlePairingFailureWithError:]_block_invoke.671
- ___55-[HMMTRAccessoryServer _pairOnSystemCommissionerFabric]_block_invoke.591
- ___55-[HMMTRAccessoryServer _pairOnSystemCommissionerFabric]_block_invoke.596
- ___55-[HMMTRAccessoryServer device:receivedAttributeReport:]_block_invoke.820
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.407
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.408
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.409
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.410
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.411
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.417
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.418
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.419
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.420
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.421
- ___59-[HMMTRAccessoryServerBrowser _preWarmCommissioningSession]_block_invoke.219
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.768
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.770
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.772
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.773
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.412
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.413
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.414
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.415
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.416
- ___62-[HMMTRAccessoryServerBrowser stopDiscoveringAccessoryServers]_block_invoke.116
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.459
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.460
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.461
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.462
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.465
- ___63-[HMMTRAccessoryServerBrowser startDiscoveringAccessoryServers]_block_invoke.113
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.426
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.427
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.428
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.429
- ___64-[HMMTRAccessoryServerBrowser _initializeAndStartBonjourBrowser]_block_invoke.91
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.422
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.423
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.424
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.425
- ___66-[HMMTRAccessoryServer _handlePartsListChanged:storage:endpoints:]_block_invoke.300
- ___66-[HMMTRAccessoryServerBrowser storageDidUpdateData:isLocalChange:]_block_invoke.210
- ___67-[HMMTRDoorLock readAttributeLockTargetStateWithCompletionHandler:]_block_invoke
- ___68-[HMMTRAccessoryServer _startPairingWithReadyToCancelHandler:error:]_block_invoke
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.448
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.449
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.450
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.451
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.454
- ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.399
- ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.406
- ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.117
- ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.121
- ___71-[HMMTRAccessoryServer validateAttestationDeviceInfo:error:completion:]_block_invoke.254
- ___71-[HMMTRAccessoryServerBrowser createNewFabricDataForFabric:completion:]_block_invoke.166
- ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.387
- ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.392
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.430
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.431
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.432
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.434
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionNumberWithCompletionHandler:]_block_invoke.436
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.437
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.438
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.439
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.440
- ___72-[HMMTRAccessoryServer fetchSoftwareVersionStringWithCompletionHandler:]_block_invoke.441
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.443
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.444
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.445
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.446
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.447
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.666
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.667
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.669
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke_2.668
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.654
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.655
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.662
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.663
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.665
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke_2.656
- ___73-[HMMTRAccessoryServerBrowser createNewFabricDataForFabricID:completion:]_block_invoke.164
- ___73-[HMMTRAccessoryServerBrowser handleResidentReachabilityChangeForFabric:]_block_invoke.212
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.725
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.726
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.730
- ___74-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:]_block_invoke.213
- ___74-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:]_block_invoke.214
- ___74-[HMMTRAccessoryServerBrowser handleUpdateNotificationsEnabled:forFabric:]_block_invoke.215
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.273
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.274
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.275
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.276
- ___79-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationWithCompletion:]_block_invoke.785
- ___79-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationWithCompletion:]_block_invoke.786
- ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.394
- ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.395
- ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.396
- ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.398
- ___79-[HMMTRAccessoryServerBrowser _updateAccessoryControlListForServer:completion:]_block_invoke.163
- ___81-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fatalError:]_block_invoke.161
- ___82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.102
- ___82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.104
- ___83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke.743
- ___83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke.744
- ___83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke.745
- ___83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke.746
- ___83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke.751
- ___83-[HMMTRAccessoryServer updateAccessoryControlToRemoveAdministratorNode:completion:]_block_invoke.693
- ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.357
- ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.358
- ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.360
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.752
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.753
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.754
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.755
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.758
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.759
- ___90-[HMMTRAccessoryServer _startLocallyDiscoveredAccessoryServerPairingWithRequest:fabricID:]_block_invoke.261
- ___90-[HMMTRAccessoryServer _startLocallyDiscoveredAccessoryServerPairingWithRequest:fabricID:]_block_invoke.262
- ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.488
- ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.489
- ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.490
- ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.491
- ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.493
- ___92-[HMMTRAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke_2.492
- ___93-[HMMTRAccessoryServerBrowser updateAccessoryACLAndGetNOCFromResidentForSharedUserForFabric:]_block_invoke.211
- ___94-[HMMTRAccessoryServer updateAccessoryControlToAdministratorNodes:sharedUserNodes:completion:]_block_invoke.691
- ___94-[HMMTRAccessoryServerBrowser _handleAddOrUpdateWithDiscriminator:vendorID:productID:overBLE:]_block_invoke.110
- ___95-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:operationQueuePriority:completion:]_block_invoke.237
- ___95-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:operationQueuePriority:completion:]_block_invoke.238
- ___95-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:operationQueuePriority:completion:]_block_invoke.239
- ___99-[HMMTRAccessoryServer _tryPairingWithOnboardingPayload:systemCommissionerPairings:pairingManager:]_block_invoke.229
- ___Block_byref_object_copy_.2084
- ___Block_byref_object_copy_.2363
- ___Block_byref_object_copy_.3272
- ___Block_byref_object_copy_.4182
- ___Block_byref_object_copy_.4674
- ___Block_byref_object_copy_.4949
- ___Block_byref_object_copy_.5308
- ___Block_byref_object_copy_.5937
- ___Block_byref_object_copy_.6411
- ___Block_byref_object_copy_.6873
- ___Block_byref_object_copy_.7528
- ___Block_byref_object_copy_.8050
- ___Block_byref_object_copy_.8731
- ___Block_byref_object_copy_.8943
- ___Block_byref_object_dispose_.2085
- ___Block_byref_object_dispose_.2364
- ___Block_byref_object_dispose_.3273
- ___Block_byref_object_dispose_.4183
- ___Block_byref_object_dispose_.4675
- ___Block_byref_object_dispose_.4950
- ___Block_byref_object_dispose_.5309
- ___Block_byref_object_dispose_.5938
- ___Block_byref_object_dispose_.6412
- ___Block_byref_object_dispose_.6874
- ___Block_byref_object_dispose_.7529
- ___Block_byref_object_dispose_.8051
- ___Block_byref_object_dispose_.8732
- ___Block_byref_object_dispose_.8944
- ___block_descriptor_40_e8_32s_e30_v16?0"HMMTRAccessoryServer"8ls32l8
- ___block_descriptor_40_e8_32s_e78_v24?0"MTRNetworkCommissioningClusterScanNetworksResponseParams"8"NSError"16ls32l8
- ___block_descriptor_48_e8_32s40s_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e48_v24?0"MTRCommissioningParameters"8"NSError"16ls32l8s40l8
- ___block_descriptor_56_e8_32s40bs48r_e5_v8?0ls32l8r48l8s40l8
- ___block_descriptor_56_e8_32s40s48r_e17_v16?0"NSError"8lr48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s56l8s48l8
- ___block_descriptor_64_e8_32s40s48s56bs_e87_v24?0"MTRGeneralCommissioningClusterCommissioningCompleteResponseParams"8"NSError"16ls32l8s40l8s56l8s48l8
- ___block_descriptor_64_e8_32s40s48s_e20_v20?0B8"NSError"12ls32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56s64s_e30_v24?0"NSString"8"NSError"16ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.1143
- ___block_literal_global.120
- ___block_literal_global.1365
- ___block_literal_global.149
- ___block_literal_global.1532
- ___block_literal_global.1701
- ___block_literal_global.1822
- ___block_literal_global.2039
- ___block_literal_global.2104
- ___block_literal_global.2257
- ___block_literal_global.230.7616
- ___block_literal_global.231
- ___block_literal_global.240
- ___block_literal_global.2431
- ___block_literal_global.2582
- ___block_literal_global.2692
- ___block_literal_global.295.5123
- ___block_literal_global.3325
- ___block_literal_global.3582
- ___block_literal_global.3716
- ___block_literal_global.391
- ___block_literal_global.3943
- ___block_literal_global.4315
- ___block_literal_global.4462
- ___block_literal_global.4474
- ___block_literal_global.464
- ___block_literal_global.4718
- ___block_literal_global.4829
- ___block_literal_global.5124
- ___block_literal_global.5319
- ___block_literal_global.5680
- ___block_literal_global.578
- ___block_literal_global.582
- ___block_literal_global.5973
- ___block_literal_global.6194
- ___block_literal_global.6374
- ___block_literal_global.645
- ___block_literal_global.649
- ___block_literal_global.652
- ___block_literal_global.658
- ___block_literal_global.676
- ___block_literal_global.6787
- ___block_literal_global.7185
- ___block_literal_global.7758
- ___block_literal_global.7953
- ___block_literal_global.8084
- ___block_literal_global.8227
- ___block_literal_global.823
- ___block_literal_global.8333
- ___block_literal_global.835
- ___block_literal_global.8809
- ___block_literal_global.916
- ___block_literal_global.991
- __unnamed_array_storage.1266
- __unnamed_array_storage.1679
- __unnamed_array_storage.2245
- __unnamed_array_storage.5885
- __unnamed_array_storage.7560
- _logCategory._hmf_once_t1.5679
- _logCategory._hmf_once_t14
- _logCategory._hmf_once_t15.8332
- _logCategory._hmf_once_t2.3715
- _logCategory._hmf_once_t2.4461
- _logCategory._hmf_once_t2.6786
- _logCategory._hmf_once_t24.2486
- _logCategory._hmf_once_t3.915
- _logCategory._hmf_once_t3.990
- _logCategory._hmf_once_t362
- _logCategory._hmf_once_t4.4828
- _logCategory._hmf_once_t51.3324
- _logCategory._hmf_once_t583
- _logCategory._hmf_once_t6.2103
- _logCategory._hmf_once_t8.6373
- _logCategory._hmf_once_t8.7952
- _logCategory._hmf_once_t9.822
- _logCategory._hmf_once_v10.824
- _logCategory._hmf_once_v15
- _logCategory._hmf_once_v16.8334
- _logCategory._hmf_once_v2.5681
- _logCategory._hmf_once_v25.2487
- _logCategory._hmf_once_v3.3717
- _logCategory._hmf_once_v3.4463
- _logCategory._hmf_once_v3.6788
- _logCategory._hmf_once_v363
- _logCategory._hmf_once_v4.917
- _logCategory._hmf_once_v4.992
- _logCategory._hmf_once_v5.4830
- _logCategory._hmf_once_v52.3326
- _logCategory._hmf_once_v584
- _logCategory._hmf_once_v7.2105
- _logCategory._hmf_once_v9.6375
- _logCategory._hmf_once_v9.7954
- _objc_msgSend$_handlePairingFailureWithError:
- _objc_msgSend$_pairingComplete:
- _objc_msgSend$_startPairingWithError:
- _objc_msgSend$_startPairingWithReadyToCancelHandler:error:
- _objc_msgSend$abortStagingWithError:
- _objc_msgSend$accessoryServer:didStopPairingWithError:
- _objc_msgSend$finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:
- _objc_msgSend$getSupportedAccessories:assetLocationType:
- _objc_msgSend$readAttributeLockStateWithCompletionHandler:
- _objc_msgSend$readAttributeLockStateWithParams:
- _objc_msgSend$setPairingDelegate:queue:
CStrings:
+ "\x02)\x14\x11\x18\x1f"
+ "%s"
+ "%{public}@Accessory server has prior successful pairing, skipping user permission dialog for unauthorized accessory"
+ "%{public}@CHIP Accessory pairing failed: %@, %@"
+ "%{public}@Cleaning up state due to pairing failure %@"
+ "%{public}@Continue commisioning."
+ "%{public}@Device commisioning was rejected."
+ "%{public}@HMMTRAttestationStatus: _requestUserPermissionForBridgeAccessory"
+ "%{public}@HMMTRAttestationStatus: _requestUserPermissionForBridgeAccessory - calling delegate"
+ "%{public}@HMMTRAttestationStatus: _requestUserPermissionForBridgeAccessory - delegate set"
+ "%{public}@No vendor/product information available"
+ "%{public}@Notifying matter petric pairing step %@"
+ "%{public}@Processing all supported accessories, number of entries: %lu"
+ "%{public}@Received batched supported accessories, number of entries: %lu, isComplete: %@"
+ "%{public}@Setting linkLayerType to Thread"
+ "%{public}@Setting linkLayerType to WiFi"
+ "%{public}@Submission of Matter metric event '%@' was: %@"
+ "%{public}@Submitting Matter metric after commissioning complete: %@"
+ "%{public}@Submitting Matter metric event '%@' to CA with %lu entries: %@ "
+ "%{public}@Unable to find delegate confirming to HAPAccessoryServerMTRDelegatePrivate"
+ "%{public}@Unable to find delegate confirming to HMMTRHAPAccessoryServerPairingDelegate"
+ "%{public}@Unexpected, found %lu batched accessories. Previous batch may not be complete"
+ "%{public}@Unexpected, got an error response for user permission for bridge accessory. Fail pairing."
+ "%{public}@Unexpected, got an error response for user permission for unauthorized accessory. Fail pairing."
+ "%{public}@User Authorization delegate is not set"
+ "%{public}@User selection for bridge accessory. Should cancel : %s"
+ "."
+ "@\"HMMTRUserAuthorizationForPairing\""
+ "@\"NSMutableDictionary\"8@?0"
+ "@32@0:8Q16@24"
+ "AnalyticsSendEventLazy"
+ "B24@0:8q16"
+ "Error"
+ "HAPAccessoryServerBrowserDelegate"
+ "HAPAccessoryServerDelegate"
+ "HMMTRAccessoryPairingEndContext"
+ "HMMTRAccessoryPairingStep_AddingNodeIDToAccessControlList"
+ "HMMTRAccessoryPairingStep_BuildingHAPCategoryFromCHIP"
+ "HMMTRAccessoryPairingStep_BuildingHAPServicesAndCharacteristicsFromCHIP"
+ "HMMTRAccessoryPairingStep_CASESanityCheck"
+ "HMMTRAccessoryPairingStep_Commissioning"
+ "HMMTRAccessoryPairingStep_FetchingCurrentPairingInformation"
+ "HMMTRAccessoryPairingStep_GettingNetworkRequirement"
+ "HMMTRAccessoryPairingStep_InternalStateAndInputValidation"
+ "HMMTRAccessoryPairingStep_None"
+ "HMMTRAccessoryPairingStep_RequestingThreadCredentials"
+ "HMMTRAccessoryPairingStep_RequestingWifiCredentials"
+ "HMMTRAccessoryPairingStep_SavingAccessoryPublicKey"
+ "HMMTRAccessoryPairingStep_SetupCommissioningSession"
+ "HMMTRAccessoryPairingStep_SystemCommissionerPairing_AddingNOC"
+ "HMMTRAccessoryPairingStep_SystemCommissionerPairing_AddingRootCertificate"
+ "HMMTRAccessoryPairingStep_SystemCommissionerPairing_ArmingFailSafe"
+ "HMMTRAccessoryPairingStep_SystemCommissionerPairing_CSRRequest"
+ "HMMTRAccessoryPairingStep_SystemCommissionerPairing_Completing"
+ "HMMTRAccessoryPairingStep_SystemCommissionerPairing_ConnectingToCommissionee"
+ "HMMTRAccessoryPairingStep_SystemCommissionerPairing_CreatingNewSystemCommissionerFabric"
+ "HMMTRAccessoryPairingStep_SystemCommissionerPairing_FetchingRootCertificate"
+ "HMMTRAccessoryPairingStep_SystemCommissionerPairing_Start"
+ "HMMTRAccessoryPairingStep_SystemCommissionerPairing_UpdatingMatterStorage"
+ "HMMTRErrorDomain"
+ "HMMTRHAPAccessoryServerBrowserPairingDelegate"
+ "HMMTRHAPAccessoryServerPairingDelegate"
+ "HMMTRUserAuthorizationForPairing"
+ "HMMTRUserAuthorizationForPairingDelegate"
+ "MTRDeviceControllerDelegate"
+ "SourceErrorDomain"
+ "Step"
+ "T@\"HMMTRUserAuthorizationForPairing\",R,N,V_userAuthorizationForPairing"
+ "T@\"NSError\",R,N,V_error"
+ "T@\"NSMutableSet\",&,V_batchedAccessories"
+ "T@\"NSNumber\",R,N,V_step"
+ "T@\"NSString\",R,N,V_sourceErrorDomain"
+ "T@,&,N,V_userAuthorizationDelegate"
+ "Undefined HMMTRAccessoryPairingStep %tu"
+ "_"
+ "_batchedAccessories"
+ "_error"
+ "_handlePairingFailureWithError:context:"
+ "_notifyDelegateOfPairingStep:"
+ "_pairingComplete:context:"
+ "_processSupportedAccessories:"
+ "_requestUserPermissionForBridgeAccessory:completionHandler:"
+ "_sourceErrorDomain"
+ "_startPairingWithError:pairingEndContext:"
+ "_startPairingWithReadyToCancelHandler:error:pairingEndContext:"
+ "_step"
+ "_userAuthorizationDelegate"
+ "_userAuthorizationForPairing"
+ "abortStagingWithError:context:"
+ "accessoryServer:authenticateUUID:token:"
+ "accessoryServer:confirmUUID:token:"
+ "accessoryServer:didDisconnectWithError:"
+ "accessoryServer:didFinishAuth:"
+ "accessoryServer:didReceiveBadPasswordThrottleAttemptsWithDelay:"
+ "accessoryServer:didStopPairingWithError:matterPairingEndContext:"
+ "accessoryServer:didUpdateCategory:"
+ "accessoryServer:didUpdateConnectionState:linkLayerType:bookkeeping:withError:"
+ "accessoryServer:didUpdateConnectionState:sessionInfo:linkLayerType:withError:"
+ "accessoryServer:didUpdateHasPairings:"
+ "accessoryServer:didUpdateName:"
+ "accessoryServer:didUpdateWakeNumber:"
+ "accessoryServer:requestUserPermission:accessoryInfo:error:"
+ "accessoryServer:validateCert:model:"
+ "accessoryServer:validateUUID:token:model:"
+ "accessoryServerBrowser:accessoryServer:didUpdateValuesForCharacteristics:stateNumber:broadcast:"
+ "accessoryServerBrowser:didChangeReachability:forAccessoryServerWithIdentifier:"
+ "accessoryServerBrowser:didFindAccessoryServerForReprovisioning:"
+ "accessoryServerBrowser:didFindAccessoryServerNeedingReprovisioning:error:"
+ "accessoryServerBrowser:didFinishWACForAccessoryWithIdentifier:error:"
+ "accessoryServerBrowser:getCacheForAccessoryWithIdentifier:withCompletion:"
+ "accessoryServerBrowser:removeCacheForAccessoryWithIdentifier:"
+ "accessoryServerBrowser:saveCache:serverIdentifier:"
+ "accessoryServerDidUpdateStateNumber:"
+ "accessoryServerNeedsOwnershipToken:"
+ "batchedAccessories"
+ "com.apple.matter.metrics"
+ "com.apple.matter.pairing-event"
+ "controller:commissioningComplete:"
+ "controller:commissioningComplete:nodeID:"
+ "controller:commissioningComplete:nodeID:metrics:"
+ "controller:commissioningSessionEstablishmentDone:"
+ "controller:readCommissioningInfo:"
+ "controller:statusUpdate:"
+ "deviceCachePrimed:"
+ "error response for user permission for bridge accessory"
+ "finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:"
+ "getBatchedSupportedAccessories:assetLocationType:"
+ "hapContextWithStep:error:"
+ "hmmtr.pairing.userAuthorization"
+ "hmmtrContextWithCancelledError:"
+ "hmmtrContextWithStep:error:"
+ "info"
+ "initWithStep:error:sourceErrorDomain:"
+ "initWithUiDialogPresenter:"
+ "isServerLinkTypeBrowseable:"
+ "metricDataForKey:"
+ "mtrContextWithStep:error:"
+ "no"
+ "notifyMatterAccessoryPairingStep:"
+ "otherContextWithStep:error:"
+ "requestUserPermissionForBridgeAccessory:completionHandler:"
+ "requestUserPermissionForBridgeAccessory:withContext:queue:completionHandler:"
+ "setBatchedAccessories:"
+ "setDeviceControllerDelegate:queue:"
+ "setUserAuthorizationDelegate:"
+ "softlink:o:path:/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics"
+ "sourceErrorDomain"
+ "step"
+ "supportedAccessories:forProductGroup:isComplete:"
+ "user rejected permission for bridge accessory"
+ "userAuthorizationDelegate"
+ "userAuthorizationForPairing"
+ "v24@0:8@\"HAPAccessoryServer\"16"
+ "v28@0:8@\"HAPAccessoryServer\"16B24"
+ "v32@0:8@\"HAPAccessoryServer\"16@\"NSError\"24"
+ "v32@0:8@\"HAPAccessoryServer\"16@\"NSNumber\"24"
+ "v32@0:8@\"HAPAccessoryServer\"16@\"NSString\"24"
+ "v32@0:8@\"HAPAccessoryServer\"16Q24"
+ "v32@0:8@\"HAPAccessoryServer\"16q24"
+ "v32@0:8@\"HAPAccessoryServerBrowser\"16@\"HAPAccessoryServer\"24"
+ "v32@0:8@\"HAPAccessoryServerBrowser\"16@\"NSError\"24"
+ "v32@0:8@\"HAPAccessoryServerBrowser\"16@\"NSString\"24"
+ "v32@0:8@\"HMMTRAccessoryServer\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"MTRDeviceController\"16@\"MTRProductIdentity\"24"
+ "v32@0:8@\"MTRDeviceController\"16@\"NSError\"24"
+ "v32@0:8@\"MTRDeviceController\"16q24"
+ "v32@0:8^@16^@24"
+ "v32@?0@\"MTRCommissioningParameters\"8@\"NSError\"16@\"HMMTRAccessoryPairingEndContext\"24"
+ "v32@?0@\"MTRNetworkCommissioningClusterScanNetworksResponseParams\"8@\"NSError\"16@\"HMMTRAccessoryPairingEndContext\"24"
+ "v32@?0@\"NSArray\"8@\"NSError\"16@\"HMMTRAccessoryPairingEndContext\"24"
+ "v32@?0@\"NSString\"8@\"NSError\"16@\"HMMTRAccessoryPairingEndContext\"24"
+ "v36@0:8@\"HAPAccessoryServerBrowser\"16B24@\"NSString\"28"
+ "v36@0:8@\"NSSet\"16@\"UARPProductGroup\"24B32"
+ "v36@0:8@16B24@28"
+ "v40@0:8@\"HAPAccessoryServer\"16@\"NSData\"24@\"NSString\"32"
+ "v40@0:8@\"HAPAccessoryServer\"16@\"NSUUID\"24@\"NSData\"32"
+ "v40@0:8@\"HAPAccessoryServerBrowser\"16@\"HAPAccessoryServer\"24@\"NSError\"32"
+ "v40@0:8@\"HAPAccessoryServerBrowser\"16@\"HMMTRCachedFabricCertificateData\"24@\"NSNumber\"32"
+ "v40@0:8@\"HAPAccessoryServerBrowser\"16@\"NSData\"24@\"NSString\"32"
+ "v40@0:8@\"HAPAccessoryServerBrowser\"16@\"NSNumber\"24@?<v@?@\"HMMTRCachedFabricCertificateData\">32"
+ "v40@0:8@\"HAPAccessoryServerBrowser\"16@\"NSString\"24@\"NSError\"32"
+ "v40@0:8@\"HAPAccessoryServerBrowser\"16@\"NSString\"24@?<v@?@\"HAPThreadNetworkMetadata\"@\"NSError\">32"
+ "v40@0:8@\"HAPAccessoryServerBrowser\"16@\"NSString\"24@?<v@?@\"NSData\">32"
+ "v40@0:8@\"HMMTRAccessoryServer\"16@\"NSError\"24@\"HMMTRAccessoryPairingEndContext\"32"
+ "v40@0:8@\"MTRDeviceController\"16@\"NSError\"24@\"NSNumber\"32"
+ "v40@0:8@?16^@24^@32"
+ "v44@0:8@\"HAPAccessoryServer\"16@\"NSArray\"24@\"NSNumber\"32B40"
+ "v44@0:8@\"HAPAccessoryServer\"16B24q28@\"NSError\"36"
+ "v44@0:8@\"HAPAccessoryServerBrowser\"16@\"HAPAccessoryServer\"24B32@\"NSNumber\"36"
+ "v44@0:8@16@24B32@36"
+ "v44@0:8@16B24q28@36"
+ "v48@0:8@\"HAPAccessoryServer\"16@\"NSArray\"24@\"HMFOSTransaction\"32@\"NSError\"40"
+ "v48@0:8@\"HAPAccessoryServer\"16@\"NSUUID\"24@\"NSData\"32@\"NSString\"40"
+ "v48@0:8@\"HAPAccessoryServer\"16q24@\"HAPAccessoryInfo\"32@\"NSError\"40"
+ "v48@0:8@\"HAPAccessoryServerBrowser\"16@\"NSNumber\"24@\"NSData\"32@?<v@?@\"NSData\"@\"NSData\"@\"NSNumber\"@\"NSData\"@\"NSError\">40"
+ "v48@0:8@\"MTRDeviceController\"16@\"NSError\"24@\"NSNumber\"32@\"MTRMetrics\"40"
+ "v48@0:8@16q24@32@40"
+ "v52@0:8@\"HAPAccessoryServer\"16B24@\"HAP2AccessorySessionInfo\"28q36@\"NSError\"44"
+ "v52@0:8@\"HAPAccessoryServer\"16B24q28@\"HAPAccessoryServerBookkeeping\"36@\"NSError\"44"
+ "v52@0:8@\"HAPAccessoryServerBrowser\"16@\"HAPAccessoryServer\"24@\"NSArray\"32@\"NSNumber\"40B48"
+ "v52@0:8@16@24@32@40B48"
+ "v52@0:8@16B24@28q36@44"
+ "v52@0:8@16B24q28@36@44"
+ "v56@0:8@\"HAPAccessoryServerBrowser\"16@\"NSNumber\"24@\"NSNumber\"32@\"NSData\"40@?<v@?@\"NSData\"@\"NSData\"@\"NSNumber\"@\"NSData\"@\"NSError\">48"
+ "yes"
+ "\xd1A"
- "\x02(\x14\x11\x18\x1f"
- "%{public}@Accessory server has prior successful pairing, skipping user permission dialog"
- "%{public}@CHIP Accessory pairing deleted. NodeID:%@ Error:%@ "
- "%{public}@CHIP Accessory pairing failed: %@"
- "%{public}@Cleaning up state due to pairing failure"
- "%{public}@Failed to fetch vendor/product information for product group: %@"
- "%{public}@Read Lock State %@, error: %@"
- "%{public}@Received supported accessories for product group: %@"
- "%{public}@Unexpected, got an error response for user permission. Fail pairing."
- "HMMTRDoorLock"
- "MTRDevicePairingDelegate"
- "_handlePairingFailureWithError:"
- "_pairingComplete:"
- "_startPairingWithError:"
- "_startPairingWithReadyToCancelHandler:error:"
- "abortStagingWithError:"
- "finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissoneeNodeID:queue:completion:"
- "getSupportedAccessories:assetLocationType:"
- "onCommissioningComplete:"
- "onPairingComplete:"
- "onPairingDeleted:"
- "onStatusUpdate:"
- "readAttributeLockStateWithCompletionHandler:"
- "readAttributeLockStateWithParams:"
- "readAttributeLockTargetStateWithCompletionHandler:"
- "readAttributeLockTargetStateWithParams:"
- "setPairingDelegate:queue:"
- "v24@0:8@\"NSError\"16"
- "v24@0:8^@16"
- "v24@?0@\"MTRCommissioningParameters\"8@\"NSError\"16"
- "v32@0:8@?16^@24"
- "\xc1A"

```
