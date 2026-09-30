## HomeKitMatter

> `/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter`

```diff

-1349.1.3.1.1
-  __TEXT.__text: 0x140ad0
+1368.1.0.1.2
+  __TEXT.__text: 0x143214
   __TEXT.__auth_stubs: 0xaa0
-  __TEXT.__objc_methlist: 0xa1fc
-  __TEXT.__const: 0x160
+  __TEXT.__objc_methlist: 0xa40c
+  __TEXT.__const: 0x180
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__gcc_except_tab: 0x2cf8
-  __TEXT.__cstring: 0x6b59
-  __TEXT.__oslogstring: 0x28296
+  __TEXT.__gcc_except_tab: 0x2e58
+  __TEXT.__cstring: 0x6c58
+  __TEXT.__oslogstring: 0x28633
   __TEXT.__ustring: 0x68
-  __TEXT.__unwind_info: 0x2e40
-  __TEXT.__objc_classname: 0x142a
-  __TEXT.__objc_methname: 0x25775
-  __TEXT.__objc_methtype: 0x3b1a
-  __TEXT.__objc_stubs: 0x16460
+  __TEXT.__unwind_info: 0x2ef8
+  __TEXT.__objc_classname: 0x143f
+  __TEXT.__objc_methname: 0x25de8
+  __TEXT.__objc_methtype: 0x3b9d
+  __TEXT.__objc_stubs: 0x16620
   __DATA_CONST.__got: 0x9d8
-  __DATA_CONST.__const: 0x48f8
-  __DATA_CONST.__objc_classlist: 0x410
+  __DATA_CONST.__const: 0x49d8
+  __DATA_CONST.__objc_classlist: 0x418
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6ba8
+  __DATA_CONST.__objc_selrefs: 0x6c90
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x2d0
-  __DATA_CONST.__objc_arraydata: 0x250
+  __DATA_CONST.__objc_superrefs: 0x2d8
+  __DATA_CONST.__objc_arraydata: 0x248
   __AUTH_CONST.__auth_got: 0x560
-  __AUTH_CONST.__const: 0x1000
-  __AUTH_CONST.__cfstring: 0x6b20
-  __AUTH_CONST.__objc_const: 0xf070
-  __AUTH_CONST.__objc_intobj: 0x1770
-  __AUTH_CONST.__objc_arrayobj: 0x198
+  __AUTH_CONST.__const: 0x1080
+  __AUTH_CONST.__cfstring: 0x6b40
+  __AUTH_CONST.__objc_const: 0xf410
+  __AUTH_CONST.__objc_intobj: 0x17e8
+  __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x1d60
-  __DATA.__objc_ivar: 0xa80
+  __AUTH.__objc_data: 0x1db0
+  __DATA.__objc_ivar: 0xac0
   __DATA.__data: 0xde0
-  __DATA.__bss: 0x418
+  __DATA.__bss: 0x428
   __DATA_DIRTY.__objc_data: 0xb40
-  __DATA_DIRTY.__bss: 0xc0
+  __DATA_DIRTY.__bss: 0xb0
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/UARPKit.framework/UARPKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 30E3EC99-1797-349B-ACFC-2C2A61667953
-  Functions: 4194
-  Symbols:   14544
-  CStrings:  9431
+  UUID: 1D772111-DE80-375E-B5AF-B0BB6DEA1F68
+  Functions: 4256
+  Symbols:   14722
+  CStrings:  9510
 
Symbols:
+ +[HMMTRUARPAccessory fromUARPSupportedAccessory:]
+ -[HMMTRAccessoryServer _queueOpenPairingWindowWithPINForDuration:completionHandler:]
+ -[HMMTRAccessoryServer _retrieveRootEndpointPartsListWithDevice:completion:]
+ -[HMMTRAccessoryServer commissionCompletePending]
+ -[HMMTRAccessoryServer commissionMetricsReadyHandler]
+ -[HMMTRAccessoryServer rootEndpointPartsList]
+ -[HMMTRAccessoryServer setCommissionCompletePending:]
+ -[HMMTRAccessoryServer setCommissionMetricsReadyHandler:]
+ -[HMMTRAccessoryServer setRootEndpointPartsList:]
+ -[HMMTRAccessoryServer stopPairingWithError:metricsReadyHandler:]
+ -[HMMTRAccessoryServerBrowser _storageDidBecomeAvailable:]
+ -[HMMTRAccessoryServerBrowserDataSourceDefault makeMatterKeypair]
+ -[HMMTRDescriptorClusterManager endpointForClusterID:device:partsList:callbackQueue:completionHandler:]
+ -[HMMTRDescriptorClusterManager fetchHAPCategoryForCHIPDevice:nodeId:server:partsList:callbackQueue:completionHandler:]
+ -[HMMTRHAPService overriddenAsPrimary]
+ -[HMMTRHAPService serviceProperties]
+ -[HMMTRHAPService setOverriddenAsPrimary:]
+ -[HMMTRHAPService setPrimary]
+ -[HMMTRProtocolMap primaryHAPServiceAmongServices:]
+ -[HMMTRProtocolMap rawPlistOffsetForKey:]
+ -[HMMTRSystemCommissionerPairingManager _augmentDatasetWithBorderAgentIDsForDevice:endpoint:dataset:]
+ -[HMMTRSystemCommissionerPairingManager _provisionBorderRouterWithSystemCommissionerNode:endpoint:dataset:]
+ -[HMMTRSystemCommissionerPairingManager _retrievePreferredThreadCredentialsOrCreateWithDataset:]
+ -[HMMTRSystemCommissionerPairingManager retrievePreferredThreadCredentialsOrCreateWithDataset:completionHandler:]
+ -[HMMTRThreadRadioManager startThreadRadioForSystemCommissionerFabricUUID:completion:]
+ -[HMMTRUARPAccessory .cxx_destruct]
+ -[HMMTRUARPAccessory accessoryCategoryNumber]
+ -[HMMTRUARPAccessory accessoryInstallationGuideURL]
+ -[HMMTRUARPAccessory accessoryMarketingName]
+ -[HMMTRUARPAccessory accessoryProductLabel]
+ -[HMMTRUARPAccessory initWithProductNumber:vendorID:productID:vendorName:accessoryCategoryNumber:accessoryMarketingName:accessoryProductLabel:accessoryInstallationGuideURL:]
+ -[HMMTRUARPAccessory productID]
+ -[HMMTRUARPAccessory productNumber]
+ -[HMMTRUARPAccessory vendorID]
+ -[HMMTRUARPAccessory vendorName]
+ -[HMMTRVendorMetadataFileStore _handleCloudMetadataFetchFailure]
+ -[HMMTRVendorMetadataFileStore _handleCloudMetadataFetchSuccess]
+ -[HMMTRVendorMetadataFileStore attemptCloudMetadataFetch]
+ -[HMMTRVendorMetadataFileStore cancelCloudMetadataFetch]
+ -[HMMTRVendorMetadataFileStore fetchInProgress]
+ -[HMMTRVendorMetadataFileStore firstFailureTime]
+ -[HMMTRVendorMetadataFileStore retryCount]
+ -[HMMTRVendorMetadataFileStore retryIntervalOverride]
+ -[HMMTRVendorMetadataFileStore retryQueue]
+ -[HMMTRVendorMetadataFileStore retryTimer]
+ -[HMMTRVendorMetadataFileStore setFetchInProgress:]
+ -[HMMTRVendorMetadataFileStore setFirstFailureTime:]
+ -[HMMTRVendorMetadataFileStore setRetryCount:]
+ -[HMMTRVendorMetadataFileStore setRetryIntervalOverride:]
+ -[HMMTRVendorMetadataFileStore setRetryTimer:]
+ -[HMMTRVendorMetadataFileStore timerDidFire:]
+ GCC_except_table1098
+ GCC_except_table1158
+ GCC_except_table1204
+ GCC_except_table1212
+ GCC_except_table1261
+ GCC_except_table1269
+ GCC_except_table1306
+ GCC_except_table1343
+ GCC_except_table1372
+ GCC_except_table1569
+ GCC_except_table1610
+ GCC_except_table1767
+ GCC_except_table1787
+ GCC_except_table1788
+ GCC_except_table1789
+ GCC_except_table1790
+ GCC_except_table1791
+ GCC_except_table1794
+ GCC_except_table1797
+ GCC_except_table1798
+ GCC_except_table1799
+ GCC_except_table1800
+ GCC_except_table1801
+ GCC_except_table1802
+ GCC_except_table1803
+ GCC_except_table1862
+ GCC_except_table1868
+ GCC_except_table1906
+ GCC_except_table1981
+ GCC_except_table2093
+ GCC_except_table2095
+ GCC_except_table2125
+ GCC_except_table2133
+ GCC_except_table2135
+ GCC_except_table2179
+ GCC_except_table2219
+ GCC_except_table2281
+ GCC_except_table2523
+ GCC_except_table2527
+ GCC_except_table2581
+ GCC_except_table2622
+ GCC_except_table2665
+ GCC_except_table2667
+ GCC_except_table2692
+ GCC_except_table2693
+ GCC_except_table2694
+ GCC_except_table2715
+ GCC_except_table2717
+ GCC_except_table2718
+ GCC_except_table2719
+ GCC_except_table2720
+ GCC_except_table2721
+ GCC_except_table2722
+ GCC_except_table2734
+ GCC_except_table2736
+ GCC_except_table2755
+ GCC_except_table2777
+ GCC_except_table2788
+ GCC_except_table2791
+ GCC_except_table2795
+ GCC_except_table2813
+ GCC_except_table2817
+ GCC_except_table2819
+ GCC_except_table2838
+ GCC_except_table2844
+ GCC_except_table2849
+ GCC_except_table2861
+ GCC_except_table2912
+ GCC_except_table2913
+ GCC_except_table3283
+ GCC_except_table3284
+ GCC_except_table3285
+ GCC_except_table3289
+ GCC_except_table3294
+ GCC_except_table3297
+ GCC_except_table3311
+ GCC_except_table3327
+ GCC_except_table3392
+ GCC_except_table3411
+ GCC_except_table3413
+ GCC_except_table3420
+ GCC_except_table3421
+ GCC_except_table3447
+ GCC_except_table3448
+ GCC_except_table3457
+ GCC_except_table3484
+ GCC_except_table3487
+ GCC_except_table3495
+ GCC_except_table3514
+ GCC_except_table3517
+ GCC_except_table3553
+ GCC_except_table3557
+ GCC_except_table3574
+ GCC_except_table3576
+ GCC_except_table3594
+ GCC_except_table3660
+ GCC_except_table3707
+ GCC_except_table3725
+ GCC_except_table3748
+ GCC_except_table3752
+ GCC_except_table3767
+ GCC_except_table3768
+ GCC_except_table3769
+ GCC_except_table3775
+ GCC_except_table3782
+ GCC_except_table3839
+ GCC_except_table3859
+ GCC_except_table3919
+ GCC_except_table3924
+ GCC_except_table3927
+ GCC_except_table4009
+ GCC_except_table4010
+ GCC_except_table4065
+ GCC_except_table4192
+ GCC_except_table4196
+ GCC_except_table4200
+ GCC_except_table4203
+ GCC_except_table4236
+ GCC_except_table703
+ GCC_except_table710
+ GCC_except_table714
+ GCC_except_table718
+ GCC_except_table720
+ GCC_except_table722
+ GCC_except_table723
+ GCC_except_table785
+ GCC_except_table786
+ GCC_except_table787
+ GCC_except_table859
+ GCC_except_table922
+ GCC_except_table926
+ GCC_except_table928
+ GCC_except_table930
+ GCC_except_table932
+ GCC_except_table936
+ GCC_except_table940
+ GCC_except_table943
+ GCC_except_table986
+ GCC_except_table990
+ GCC_except_table992
+ _OBJC_CLASS_$_HMMTRUARPAccessory
+ _OBJC_CLASS_$_MTRAttributeRequestPath
+ _OBJC_CLASS_$_MTRBaseClusterThreadBorderRouterManagement
+ _OBJC_CLASS_$_MTRBaseClusterThreadNetworkDirectory
+ _OBJC_IVAR_$_HMMTRAccessoryServer._commissionCompletePending
+ _OBJC_IVAR_$_HMMTRAccessoryServer._commissionMetricsReadyHandler
+ _OBJC_IVAR_$_HMMTRAccessoryServer._rootEndpointPartsList
+ _OBJC_IVAR_$_HMMTRHAPService._overriddenAsPrimary
+ _OBJC_IVAR_$_HMMTRUARPAccessory._accessoryCategoryNumber
+ _OBJC_IVAR_$_HMMTRUARPAccessory._accessoryInstallationGuideURL
+ _OBJC_IVAR_$_HMMTRUARPAccessory._accessoryMarketingName
+ _OBJC_IVAR_$_HMMTRUARPAccessory._accessoryProductLabel
+ _OBJC_IVAR_$_HMMTRUARPAccessory._productID
+ _OBJC_IVAR_$_HMMTRUARPAccessory._productNumber
+ _OBJC_IVAR_$_HMMTRUARPAccessory._vendorID
+ _OBJC_IVAR_$_HMMTRUARPAccessory._vendorName
+ _OBJC_IVAR_$_HMMTRVendorMetadataFileStore._fetchInProgress
+ _OBJC_IVAR_$_HMMTRVendorMetadataFileStore._firstFailureTime
+ _OBJC_IVAR_$_HMMTRVendorMetadataFileStore._retryCount
+ _OBJC_IVAR_$_HMMTRVendorMetadataFileStore._retryIntervalOverride
+ _OBJC_IVAR_$_HMMTRVendorMetadataFileStore._retryQueue
+ _OBJC_IVAR_$_HMMTRVendorMetadataFileStore._retryTimer
+ _OBJC_METACLASS_$_HMMTRUARPAccessory
+ __OBJC_$_CLASS_METHODS_HMMTRUARPAccessory
+ __OBJC_$_INSTANCE_METHODS_HMMTRUARPAccessory
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRUARPAccessory
+ __OBJC_$_PROP_LIST_HMMTRUARPAccessory
+ __OBJC_CLASS_RO_$_HMMTRUARPAccessory
+ __OBJC_METACLASS_RO_$_HMMTRUARPAccessory
+ ___101-[HMMTRAccessoryServer updateAccessoryControlToIncludeAdministratorNodes:sharedUserNodes:completion:]_block_invoke.837
+ ___101-[HMMTRSystemCommissionerPairingManager _augmentDatasetWithBorderAgentIDsForDevice:endpoint:dataset:]_block_invoke
+ ___103-[HMMTRDescriptorClusterManager endpointForClusterID:device:partsList:callbackQueue:completionHandler:]_block_invoke
+ ___103-[HMMTRDescriptorClusterManager endpointForClusterID:device:partsList:callbackQueue:completionHandler:]_block_invoke_2
+ ___103-[HMMTRSystemCommissionerPairingManager _retrieveThreadCredentialsFromSystemCommissionerNode:endpoint:]_block_invoke.66
+ ___107-[HMMTRAccessoryServerBrowser _fetchDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.212
+ ___107-[HMMTRSystemCommissionerPairingManager _provisionBorderRouterWithSystemCommissionerNode:endpoint:dataset:]_block_invoke
+ ___107-[HMMTRSystemCommissionerPairingManager _provisionBorderRouterWithSystemCommissionerNode:endpoint:dataset:]_block_invoke.68
+ ___107-[HMMTRSystemCommissionerPairingManager _provisionBorderRouterWithSystemCommissionerNode:endpoint:dataset:]_block_invoke_2
+ ___107-[HMMTRSystemCommissionerPairingManager _provisionBorderRouterWithSystemCommissionerNode:endpoint:dataset:]_block_invoke_3
+ ___109-[HMMTRDescriptorClusterManager fetchHAPCategoryWithMTRDevice:nodeId:server:callbackQueue:completionHandler:]_block_invoke.133
+ ___110-[HMMTRAccessoryServerBrowser removeAllDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.214
+ ___113-[HMMTRSystemCommissionerPairingManager retrievePreferredThreadCredentialsOrCreateWithDataset:completionHandler:]_block_invoke
+ ___114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke.913
+ ___114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke.916
+ ___114-[HMMTRProtocolMap _selectedServiceTypeForServiceArray:device:mtrDevice:endpoint:callbackQueue:completionHandler:]_block_invoke.432
+ ___119-[HMMTRAccessoryServerBrowser removeDevicePairingFabricForSystemCommissionerDeviceWithNodeID:fabric:completionHandler:]_block_invoke.210
+ ___119-[HMMTRDescriptorClusterManager fetchHAPCategoryForCHIPDevice:nodeId:server:partsList:callbackQueue:completionHandler:]_block_invoke
+ ___131-[HMMTRDescriptorClusterManager fetchDeviceTypesForEndpoints:device:endpointDeviceTypes:lastError:callbackQueue:completionHandler:]_block_invoke.350
+ ___134-[HMMTRDescriptorClusterManager fetchDeviceTypesForEndpoints:mtrDevice:endpointDeviceTypes:lastError:callbackQueue:completionHandler:]_block_invoke.351
+ ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.327
+ ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.334
+ ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.335
+ ___198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke.361
+ ___198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke.365
+ ___198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke_2.362
+ ___242-[HMMTRDescriptorClusterManager fetchHAPServicesAtCHIPEndpoint:deviceTopology:endpointDeviceTypes:accessoryInfo:hapToCHIPClusterMappingArray:device:isBridge:bridgeAggregateNodeEndpoint:isComposedDevice:server:callbackQueue:completionHandler:]_block_invoke.325
+ ___278-[HMMTRAccessoryServerBrowser _stageAccessoryServerWithSetupPayload:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:commissioneeInfoHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke.197
+ ___280-[HMMTRDescriptorClusterManager _verifyHAPCharacteristicSupportAtCHIPEndpoint:device:endpointDeviceTypes:callbackQueue:clusterClassToQueryForFeatureMap:hapServicesToCheckForFeatureMap:hapServicesInUse:deviceTopology:bridgeAggregateNodeEndpoint:server:lastError:completionHandler:]_block_invoke.304
+ ___40-[HMMTRAccessoryServerBrowser configure]_block_invoke.141
+ ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.889
+ ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.892
+ ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke_2.888
+ ___45-[HMMTRVendorMetadataFileStore timerDidFire:]_block_invoke
+ ___47-[HMMTRAccessoryServer processAttributeReport:]_block_invoke.976
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.861
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.866
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke_2.865
+ ___50-[HMMTRVendorMetadataFileStore fetchCloudMetadata]_block_invoke
+ ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.819
+ ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.824
+ ___51-[HMMTRAccessoryServer device:receivedEventReport:]_block_invoke.977
+ ___51-[HMMTRProtocolMap primaryHAPServiceAmongServices:]_block_invoke
+ ___51-[HMMTRProtocolMap primaryHAPServiceAmongServices:]_block_invoke_2
+ ___51-[HMMTRProtocolMap primaryHAPServiceAmongServices:]_block_invoke_3
+ ___51-[HMMTRProtocolMap primaryHAPServiceAmongServices:]_block_invoke_4
+ ___51-[HMMTRProtocolMap primaryHAPServiceAmongServices:]_block_invoke_5
+ ___52-[HMMTRAccessoryServerBrowser _cleanupStagedServers]_block_invoke.317
+ ___55-[HMMTRAccessoryServer device:receivedAttributeReport:]_block_invoke.975
+ ___56-[HMMTRVendorMetadataFileStore cancelCloudMetadataFetch]_block_invoke
+ ___57-[HMMTRAccessoryServerBrowser storageDidBecomeAvailable:]_block_invoke
+ ___57-[HMMTRVendorMetadataFileStore attemptCloudMetadataFetch]_block_invoke
+ ___58-[HMMTRProtocolMap _buildEventMapper:characteristicsDict:]_block_invoke.307
+ ___59-[HMMTRHAPEnumerator _serviceLabelIndexMapForDescriptions:]_block_invoke
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.920
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.926
+ ___62-[HMMTRAccessoryServerBrowser stopDiscoveringAccessoryServers]_block_invoke.186
+ ___63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.818
+ ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.940
+ ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.941
+ ___64-[HMMTRAccessoryServerBrowser _initializeAndStartBonjourBrowser]_block_invoke.149
+ ___64-[HMMTRVendorMetadataFileStore _handleCloudMetadataFetchFailure]_block_invoke
+ ___65-[HMMTRAccessoryServer stopPairingWithError:metricsReadyHandler:]_block_invoke
+ ___65-[HMMTRAccessoryServer stopPairingWithError:metricsReadyHandler:]_block_invoke.289
+ ___65-[HMMTRAccessoryServer stopPairingWithError:metricsReadyHandler:]_block_invoke_2
+ ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.190
+ ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.192
+ ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.194
+ ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke_2.193
+ ___71-[HMMTRThreadRadioManager _retryWEDConnectionToAccessoryWithDelayInMs:]_block_invoke.35
+ ___71-[HMMTRThreadRadioManager _retryWEDConnectionToAccessoryWithDelayInMs:]_block_invoke.36
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.816
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke_2.813
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke_3
+ ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.871
+ ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.872
+ ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.876
+ ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke_2.878
+ ___76-[HMMTRAccessoryServer _retrieveRootEndpointPartsListWithDevice:completion:]_block_invoke
+ ___76-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithNodeID:completion:]_block_invoke.195
+ ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke_2
+ ___79-[HMMTRAccessoryServerBrowser _updateAccessoryControlListForServer:completion:]_block_invoke.322
+ ___82-[HMMTRAccessoryServer fetchColorControlClusterForHapAccessory:completionHandler:]_block_invoke.927
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.896
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.897
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.900
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke_2.899
+ ___82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.161
+ ___82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.163
+ ___82-[HMMTRProtocolMap _buildValueMapper:characteristicsDict:operation:forMTRCluster:]_block_invoke.286
+ ___83-[HMMTRAccessoryServer updateAccessoryControlToRemoveAdministratorNode:completion:]_block_invoke.838
+ ___84-[HMMTRAccessoryServer _queueOpenPairingWindowWithPINForDuration:completionHandler:]_block_invoke
+ ___84-[HMMTRAccessoryServer _queueOpenPairingWindowWithPINForDuration:completionHandler:]_block_invoke.410
+ ___84-[HMMTRAccessoryServer _queueOpenPairingWindowWithPINForDuration:completionHandler:]_block_invoke.411
+ ___84-[HMMTRAccessoryServer _queueOpenPairingWindowWithPINForDuration:completionHandler:]_block_invoke.412
+ ___84-[HMMTRAccessoryServer _queueOpenPairingWindowWithPINForDuration:completionHandler:]_block_invoke.414
+ ___84-[HMMTRAccessoryServer _queueOpenPairingWindowWithPINForDuration:completionHandler:]_block_invoke.415
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.903
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.904
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.908
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.909
+ ___86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.942
+ ___86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.943
+ ___86-[HMMTRThreadRadioManager startThreadRadioForSystemCommissionerFabricUUID:completion:]_block_invoke
+ ___86-[HMMTRVendorMetadataFileStore _retrieveVendorMetadataForVendorID:productID:metadata:]_block_invoke
+ ___86-[HMMTRVendorMetadataFileStore _retrieveVendorMetadataForVendorID:productID:metadata:]_block_invoke.82
+ ___91-[HMMTRProtocolMap servicesForDeviceTypes:device:endpoint:callbackQueue:completionHandler:]_block_invoke.435
+ ___92-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fabricUUID:fatalError:]_block_invoke.320
+ ___92-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fabricUUID:fatalError:]_block_invoke.321
+ ___94-[HMMTRAccessoryServer updateAccessoryControlToAdministratorNodes:sharedUserNodes:completion:]_block_invoke.836
+ ___94-[HMMTRAccessoryServerBrowser _handleAddOrUpdateWithDiscriminator:vendorID:productID:overBLE:]_block_invoke.170
+ ___96-[HMMTRDescriptorClusterManager endpointForClusterID:mtrDevice:callbackQueue:completionHandler:]_block_invoke.401
+ ___96-[HMMTRProtocolMap servicesOfMTRDevice:forDeviceTypes:endpoint:callbackQueue:completionHandler:]_block_invoke.436
+ ___96-[HMMTRSystemCommissionerPairingManager _retrievePreferredThreadCredentialsOrCreateWithDataset:]_block_invoke
+ ___96-[HMMTRSystemCommissionerPairingManager _retrievePreferredThreadCredentialsOrCreateWithDataset:]_block_invoke.62
+ ___96-[HMMTRSystemCommissionerPairingManager _retrievePreferredThreadCredentialsOrCreateWithDataset:]_block_invoke_2
+ ___97-[HMMTRAccessoryServer _getCommissioneeNetworkCommissioningClusterEndpointWithDevice:completion:]_block_invoke_2
+ ___97-[HMMTRAccessoryServerBrowser removeAccessoryServer:fromDiscoveredAccessoryServerListWithReason:]_block_invoke.305
+ ___Block_byref_object_copy_.10189
+ ___Block_byref_object_copy_.10952
+ ___Block_byref_object_copy_.11650
+ ___Block_byref_object_copy_.12349
+ ___Block_byref_object_copy_.12513
+ ___Block_byref_object_copy_.1810
+ ___Block_byref_object_copy_.3169
+ ___Block_byref_object_copy_.3457
+ ___Block_byref_object_copy_.4540
+ ___Block_byref_object_copy_.5708
+ ___Block_byref_object_copy_.5859
+ ___Block_byref_object_copy_.7675
+ ___Block_byref_object_copy_.8108
+ ___Block_byref_object_copy_.9232
+ ___Block_byref_object_dispose_.10190
+ ___Block_byref_object_dispose_.10953
+ ___Block_byref_object_dispose_.11651
+ ___Block_byref_object_dispose_.12350
+ ___Block_byref_object_dispose_.12514
+ ___Block_byref_object_dispose_.1811
+ ___Block_byref_object_dispose_.3170
+ ___Block_byref_object_dispose_.3458
+ ___Block_byref_object_dispose_.4541
+ ___Block_byref_object_dispose_.5709
+ ___Block_byref_object_dispose_.5860
+ ___Block_byref_object_dispose_.7676
+ ___Block_byref_object_dispose_.8109
+ ___Block_byref_object_dispose_.9233
+ ___block_descriptor_32_e28_"NSString"16?0"NSString"8l
+ ___block_descriptor_32_e30_"NSString"16?0"HAPService"8l
+ ___block_descriptor_40_e8_32s_e18_B16?0"NSString"8ls32l8
+ ___block_descriptor_48_e8_32bs40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e62_{_HMFFutureBlockOutcome=q}16?0"MTSThreadNetworkCredential"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48w_e5_v8?0ls40l8s32l8w48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e43_{_HMFFutureBlockOutcome=q}16?0"NSError"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56s_e95_{_HMFFutureBlockOutcome=q}16?0"MTRThreadBorderRouterManagementClusterDatasetResponseParams"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_67_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e24_v32?0"NSError"8Q16^B24ls32l8s40l8r64l8s48l8s56l8
+ ___block_literal_global.100
+ ___block_literal_global.10060
+ ___block_literal_global.10655
+ ___block_literal_global.11244
+ ___block_literal_global.11469
+ ___block_literal_global.11684
+ ___block_literal_global.11820
+ ___block_literal_global.11951
+ ___block_literal_global.12169
+ ___block_literal_global.1252
+ ___block_literal_global.1358
+ ___block_literal_global.1443
+ ___block_literal_global.1659
+ ___block_literal_global.1933
+ ___block_literal_global.1987
+ ___block_literal_global.2033
+ ___block_literal_global.2120
+ ___block_literal_global.214
+ ___block_literal_global.2480
+ ___block_literal_global.2628
+ ___block_literal_global.288
+ ___block_literal_global.2930
+ ___block_literal_global.3074
+ ___block_literal_global.3103
+ ___block_literal_global.311
+ ___block_literal_global.314
+ ___block_literal_global.3195
+ ___block_literal_global.3349
+ ___block_literal_global.345
+ ___block_literal_global.353.9096
+ ___block_literal_global.3546
+ ___block_literal_global.3697
+ ___block_literal_global.3821
+ ___block_literal_global.408
+ ___block_literal_global.4308
+ ___block_literal_global.4637
+ ___block_literal_global.489
+ ___block_literal_global.4925
+ ___block_literal_global.5059
+ ___block_literal_global.5160
+ ___block_literal_global.5424
+ ___block_literal_global.554
+ ___block_literal_global.556
+ ___block_literal_global.559
+ ___block_literal_global.5597
+ ___block_literal_global.570
+ ___block_literal_global.5843
+ ___block_literal_global.6031
+ ___block_literal_global.610
+ ___block_literal_global.6171
+ ___block_literal_global.62
+ ___block_literal_global.6280
+ ___block_literal_global.6314
+ ___block_literal_global.6335
+ ___block_literal_global.6585
+ ___block_literal_global.6598
+ ___block_literal_global.6692
+ ___block_literal_global.6786
+ ___block_literal_global.6880
+ ___block_literal_global.6983
+ ___block_literal_global.7077
+ ___block_literal_global.7216
+ ___block_literal_global.7357
+ ___block_literal_global.7463
+ ___block_literal_global.7541
+ ___block_literal_global.7891
+ ___block_literal_global.8119
+ ___block_literal_global.82.9985
+ ___block_literal_global.8451
+ ___block_literal_global.8576
+ ___block_literal_global.8710
+ ___block_literal_global.886
+ ___block_literal_global.9264
+ ___block_literal_global.960
+ ___block_literal_global.9662
+ ___block_literal_global.984
+ ___block_literal_global.9984
+ _attributePathMatches
+ _logCategory._hmf_once_t0.3073
+ _logCategory._hmf_once_t0.5596
+ _logCategory._hmf_once_t0.6313
+ _logCategory._hmf_once_t10.12168
+ _logCategory._hmf_once_t123
+ _logCategory._hmf_once_t13.3194
+ _logCategory._hmf_once_t13.3545
+ _logCategory._hmf_once_t14.1267
+ _logCategory._hmf_once_t14.6597
+ _logCategory._hmf_once_t14.6691
+ _logCategory._hmf_once_t14.6785
+ _logCategory._hmf_once_t14.6982
+ _logCategory._hmf_once_t14.7076
+ _logCategory._hmf_once_t14.7215
+ _logCategory._hmf_once_t199
+ _logCategory._hmf_once_t2.10059
+ _logCategory._hmf_once_t2.5159
+ _logCategory._hmf_once_t2.6279
+ _logCategory._hmf_once_t2.7356
+ _logCategory._hmf_once_t20.11819
+ _logCategory._hmf_once_t26.6879
+ _logCategory._hmf_once_t3.1357
+ _logCategory._hmf_once_t3.1442
+ _logCategory._hmf_once_t31.11950
+ _logCategory._hmf_once_t38
+ _logCategory._hmf_once_t4.3696
+ _logCategory._hmf_once_t4.7462
+ _logCategory._hmf_once_t40.5905
+ _logCategory._hmf_once_t6.2119
+ _logCategory._hmf_once_t68.12373
+ _logCategory._hmf_once_t688
+ _logCategory._hmf_once_t8.11468
+ _logCategory._hmf_once_t8.8575
+ _logCategory._hmf_once_v1.3075
+ _logCategory._hmf_once_v1.5598
+ _logCategory._hmf_once_v1.6315
+ _logCategory._hmf_once_v11.12170
+ _logCategory._hmf_once_v124
+ _logCategory._hmf_once_v14.3196
+ _logCategory._hmf_once_v14.3547
+ _logCategory._hmf_once_v15.1268
+ _logCategory._hmf_once_v15.6599
+ _logCategory._hmf_once_v15.6693
+ _logCategory._hmf_once_v15.6787
+ _logCategory._hmf_once_v15.6984
+ _logCategory._hmf_once_v15.7078
+ _logCategory._hmf_once_v15.7217
+ _logCategory._hmf_once_v200
+ _logCategory._hmf_once_v21.11821
+ _logCategory._hmf_once_v27.6881
+ _logCategory._hmf_once_v3.10061
+ _logCategory._hmf_once_v3.5161
+ _logCategory._hmf_once_v3.6281
+ _logCategory._hmf_once_v3.7358
+ _logCategory._hmf_once_v32.11952
+ _logCategory._hmf_once_v39
+ _logCategory._hmf_once_v4.1359
+ _logCategory._hmf_once_v4.1444
+ _logCategory._hmf_once_v41.5906
+ _logCategory._hmf_once_v5.3698
+ _logCategory._hmf_once_v5.7464
+ _logCategory._hmf_once_v689
+ _logCategory._hmf_once_v69.12374
+ _logCategory._hmf_once_v7.2121
+ _logCategory._hmf_once_v9.11470
+ _logCategory._hmf_once_v9.8577
+ _objc_msgSend$_augmentDatasetWithBorderAgentIDsForDevice:endpoint:dataset:
+ _objc_msgSend$_handleCloudMetadataFetchFailure
+ _objc_msgSend$_handleCloudMetadataFetchSuccess
+ _objc_msgSend$_provisionBorderRouterWithSystemCommissionerNode:endpoint:dataset:
+ _objc_msgSend$_queueOpenPairingWindowWithPINForDuration:completionHandler:
+ _objc_msgSend$_retrievePreferredThreadCredentialsOrCreateWithDataset:
+ _objc_msgSend$_retrieveRootEndpointPartsListWithDevice:completion:
+ _objc_msgSend$_storageDidBecomeAvailable:
+ _objc_msgSend$addNetworkWithParams:completion:
+ _objc_msgSend$attemptCloudMetadataFetch
+ _objc_msgSend$commissionCompletePending
+ _objc_msgSend$commissionMetricsReadyHandler
+ _objc_msgSend$endpointForClusterID:device:partsList:callbackQueue:completionHandler:
+ _objc_msgSend$fetchHAPCategoryForCHIPDevice:nodeId:server:partsList:callbackQueue:completionHandler:
+ _objc_msgSend$fromUARPSupportedAccessory:
+ _objc_msgSend$getActiveDatasetRequestWithCompletion:
+ _objc_msgSend$initWithDataset:borderAgentEUI:borderAgentID:
+ _objc_msgSend$initWithProductNumber:vendorID:productID:vendorName:accessoryCategoryNumber:accessoryMarketingName:accessoryProductLabel:accessoryInstallationGuideURL:
+ _objc_msgSend$makeMatterKeypair
+ _objc_msgSend$overriddenAsPrimary
+ _objc_msgSend$primaryHAPServiceAmongServices:
+ _objc_msgSend$rawPlistOffsetForKey:
+ _objc_msgSend$readAttributeMinSetpointDeadBandWithParams:
+ _objc_msgSend$readAttributePaths:eventPaths:params:queue:completion:
+ _objc_msgSend$requestPathWithEndpointID:clusterID:attributeID:
+ _objc_msgSend$rootEndpointPartsList
+ _objc_msgSend$setActiveDatasetRequestWithParams:completion:
+ _objc_msgSend$setCommissionCompletePending:
+ _objc_msgSend$setCommissionMetricsReadyHandler:
+ _objc_msgSend$setOverriddenAsPrimary:
+ _objc_msgSend$setPrimary
+ _objc_msgSend$setRootEndpointPartsList:
+ _objc_msgSend$startThreadRadioForSystemCommissionerFabricUUID:completion:
+ _objc_msgSend$stopPairingWithError:metricsReadyHandler:
- -[HMMTRDescriptorClusterManager endpointForClusterID:device:callbackQueue:completionHandler:]
- -[HMMTRDescriptorClusterManager fetchEndpointsForDevice:endpointID:callbackQueue:completionHandler:]
- -[HMMTRDescriptorClusterManager fetchHAPCategoryForCHIPDevice:nodeId:server:callbackQueue:completionHandler:]
- -[HMMTRDescriptorClusterManager runBlockForAllEndpointsWithClusterID:device:callbackQueue:block:]
- -[HMMTRSystemCommissionerPairingManager _generateThreadOperationalDataset]
- -[HMMTRSystemCommissionerPairingManager _provisionBorderRouterWithSystemCommissionerNode:endpoint:]
- -[HMMTRSystemCommissionerPairingManager _retrievePreferredThreadCredentialsWithOptions:]
- -[HMMTRSystemCommissionerPairingManager retrievePreferredThreadCredentialsWithOptions:completionHandler:]
- -[HMMTRVendorMetadataVendor appBundleID]
- -[HMMTRVendorMetadataVendor appStoreID]
- -[HMMTRVendorMetadataVendor setAppBundleID:]
- -[HMMTRVendorMetadataVendor setAppStoreID:]
- GCC_except_table1059
- GCC_except_table1119
- GCC_except_table1165
- GCC_except_table1173
- GCC_except_table1222
- GCC_except_table1230
- GCC_except_table1267
- GCC_except_table1304
- GCC_except_table1333
- GCC_except_table1534
- GCC_except_table1573
- GCC_except_table1725
- GCC_except_table1726
- GCC_except_table1727
- GCC_except_table1730
- GCC_except_table1750
- GCC_except_table1751
- GCC_except_table1752
- GCC_except_table1753
- GCC_except_table1754
- GCC_except_table1757
- GCC_except_table1760
- GCC_except_table1761
- GCC_except_table1765
- GCC_except_table1766
- GCC_except_table1825
- GCC_except_table1831
- GCC_except_table1865
- GCC_except_table1940
- GCC_except_table2052
- GCC_except_table2054
- GCC_except_table2084
- GCC_except_table2092
- GCC_except_table2094
- GCC_except_table2142
- GCC_except_table2183
- GCC_except_table2245
- GCC_except_table2486
- GCC_except_table2490
- GCC_except_table2542
- GCC_except_table2583
- GCC_except_table2626
- GCC_except_table2628
- GCC_except_table2653
- GCC_except_table2654
- GCC_except_table2655
- GCC_except_table2676
- GCC_except_table2677
- GCC_except_table2678
- GCC_except_table2679
- GCC_except_table2680
- GCC_except_table2681
- GCC_except_table2682
- GCC_except_table2683
- GCC_except_table2695
- GCC_except_table2697
- GCC_except_table2732
- GCC_except_table2738
- GCC_except_table2749
- GCC_except_table2752
- GCC_except_table2756
- GCC_except_table2774
- GCC_except_table2778
- GCC_except_table2780
- GCC_except_table2799
- GCC_except_table2805
- GCC_except_table2822
- GCC_except_table2873
- GCC_except_table2874
- GCC_except_table3238
- GCC_except_table3239
- GCC_except_table3240
- GCC_except_table3244
- GCC_except_table3249
- GCC_except_table3252
- GCC_except_table3266
- GCC_except_table3282
- GCC_except_table3347
- GCC_except_table3366
- GCC_except_table3368
- GCC_except_table3375
- GCC_except_table3376
- GCC_except_table3399
- GCC_except_table3400
- GCC_except_table3409
- GCC_except_table3434
- GCC_except_table3437
- GCC_except_table3445
- GCC_except_table3464
- GCC_except_table3467
- GCC_except_table3503
- GCC_except_table3507
- GCC_except_table3524
- GCC_except_table3526
- GCC_except_table3544
- GCC_except_table3610
- GCC_except_table3654
- GCC_except_table3672
- GCC_except_table3695
- GCC_except_table3699
- GCC_except_table3714
- GCC_except_table3715
- GCC_except_table3720
- GCC_except_table3727
- GCC_except_table3784
- GCC_except_table3804
- GCC_except_table3858
- GCC_except_table3863
- GCC_except_table3866
- GCC_except_table3947
- GCC_except_table3948
- GCC_except_table4003
- GCC_except_table4006
- GCC_except_table4134
- GCC_except_table4138
- GCC_except_table4141
- GCC_except_table4174
- GCC_except_table685
- GCC_except_table689
- GCC_except_table750
- GCC_except_table751
- GCC_except_table752
- GCC_except_table820
- GCC_except_table883
- GCC_except_table887
- GCC_except_table889
- GCC_except_table891
- GCC_except_table893
- GCC_except_table897
- GCC_except_table901
- GCC_except_table904
- GCC_except_table947
- GCC_except_table951
- GCC_except_table953
- _OBJC_CLASS_$_MTRClusterGeneralCommissioning
- _OBJC_CLASS_$_MTRClusterThreadBorderRouterManagement
- _OBJC_CLASS_$_MTRClusterThreadNetworkDirectory
- _OBJC_IVAR_$_HMMTRVendorMetadataVendor._appBundleID
- _OBJC_IVAR_$_HMMTRVendorMetadataVendor._appStoreID
- ___100-[HMMTRDescriptorClusterManager fetchEndpointsForDevice:endpointID:callbackQueue:completionHandler:]_block_invoke
- ___101-[HMMTRAccessoryServer updateAccessoryControlToIncludeAdministratorNodes:sharedUserNodes:completion:]_block_invoke.835
- ___105-[HMMTRSystemCommissionerPairingManager retrievePreferredThreadCredentialsWithOptions:completionHandler:]_block_invoke
- ___107-[HMMTRAccessoryServerBrowser _fetchDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.209
- ___109-[HMMTRDescriptorClusterManager fetchHAPCategoryForCHIPDevice:nodeId:server:callbackQueue:completionHandler:]_block_invoke
- ___109-[HMMTRDescriptorClusterManager fetchHAPCategoryForCHIPDevice:nodeId:server:callbackQueue:completionHandler:]_block_invoke.127
- ___109-[HMMTRDescriptorClusterManager fetchHAPCategoryWithMTRDevice:nodeId:server:callbackQueue:completionHandler:]_block_invoke.132
- ___110-[HMMTRAccessoryServerBrowser removeAllDevicePairingsForSystemCommissionerDeviceWithNodeID:completionHandler:]_block_invoke.211
- ___114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke.911
- ___114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke.914
- ___114-[HMMTRProtocolMap _selectedServiceTypeForServiceArray:device:mtrDevice:endpoint:callbackQueue:completionHandler:]_block_invoke.426
- ___119-[HMMTRAccessoryServerBrowser removeDevicePairingFabricForSystemCommissionerDeviceWithNodeID:fabric:completionHandler:]_block_invoke.207
- ___131-[HMMTRDescriptorClusterManager fetchDeviceTypesForEndpoints:device:endpointDeviceTypes:lastError:callbackQueue:completionHandler:]_block_invoke.341
- ___134-[HMMTRDescriptorClusterManager fetchDeviceTypesForEndpoints:mtrDevice:endpointDeviceTypes:lastError:callbackQueue:completionHandler:]_block_invoke.342
- ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.325
- ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.326
- ___155-[HMMTRAccessoryServerBrowser finishSystemCommissionerFabricCommissioningWithFabricID:rootCACert:ipk:controllerNodeID:commissioneeNodeID:queue:completion:]_block_invoke.329
- ___198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke.352
- ___198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke.356
- ___198-[HMMTRDescriptorClusterManager fetchHAPServicesForEndpoints:endpointDeviceTypes:device:nodeId:isBridge:bridgeAggregateNodeEndpoint:server:topology:hapAccessoryInfo:callbackQueue:completionHandler:]_block_invoke_2.353
- ___242-[HMMTRDescriptorClusterManager fetchHAPServicesAtCHIPEndpoint:deviceTopology:endpointDeviceTypes:accessoryInfo:hapToCHIPClusterMappingArray:device:isBridge:bridgeAggregateNodeEndpoint:isComposedDevice:server:callbackQueue:completionHandler:]_block_invoke.316
- ___278-[HMMTRAccessoryServerBrowser _stageAccessoryServerWithSetupPayload:deviceCredentialHandler:wifiScanResultsHandler:threadScanResultsHandler:readyToCancelHandler:progressUpdateHandler:commissioneeInfoHandler:scanningNetworks:hasPriorSuccessfulPairing:category:completionHandler:]_block_invoke.194
- ___280-[HMMTRDescriptorClusterManager _verifyHAPCharacteristicSupportAtCHIPEndpoint:device:endpointDeviceTypes:callbackQueue:clusterClassToQueryForFeatureMap:hapServicesToCheckForFeatureMap:hapServicesInUse:deviceTopology:bridgeAggregateNodeEndpoint:server:lastError:completionHandler:]_block_invoke.295
- ___40-[HMMTRAccessoryServerBrowser configure]_block_invoke.138
- ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.885
- ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.888
- ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke_2.886
- ___45-[HMMTRAccessoryServer stopPairingWithError:]_block_invoke
- ___45-[HMMTRAccessoryServer stopPairingWithError:]_block_invoke.289
- ___47-[HMMTRAccessoryServer processAttributeReport:]_block_invoke.974
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.859
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.862
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke_2.863
- ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.818
- ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.822
- ___51-[HMMTRAccessoryServer device:receivedEventReport:]_block_invoke.975
- ___52-[HMMTRAccessoryServerBrowser _cleanupStagedServers]_block_invoke.315
- ___55-[HMMTRAccessoryServer device:receivedAttributeReport:]_block_invoke.973
- ___58-[HMMTRProtocolMap _buildEventMapper:characteristicsDict:]_block_invoke.301
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.916
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.922
- ___62-[HMMTRAccessoryServerBrowser stopDiscoveringAccessoryServers]_block_invoke.183
- ___63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.816
- ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.937
- ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.938
- ___64-[HMMTRAccessoryServerBrowser _initializeAndStartBonjourBrowser]_block_invoke.146
- ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.184
- ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.189
- ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke.191
- ___69-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithIdentifier:]_block_invoke_2.190
- ___71-[HMMTRThreadRadioManager _retryWEDConnectionToAccessoryWithDelayInMs:]_block_invoke.32
- ___71-[HMMTRThreadRadioManager _retryWEDConnectionToAccessoryWithDelayInMs:]_block_invoke.33
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.814
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.869
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.870
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.874
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke_2.876
- ___76-[HMMTRAccessoryServerBrowser discoverAccessoryServerWithNodeID:completion:]_block_invoke.192
- ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.410
- ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.411
- ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.412
- ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.414
- ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.415
- ___79-[HMMTRAccessoryServerBrowser _updateAccessoryControlListForServer:completion:]_block_invoke.320
- ___82-[HMMTRAccessoryServer fetchColorControlClusterForHapAccessory:completionHandler:]_block_invoke.925
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.893
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.894
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.898
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke_2.897
- ___82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.158
- ___82-[HMMTRAccessoryServerBrowser _discriminator:vendorID:productID:CM:fromTXTRecord:]_block_invoke.160
- ___82-[HMMTRProtocolMap _buildValueMapper:characteristicsDict:operation:forMTRCluster:]_block_invoke.280
- ___83-[HMMTRAccessoryServer updateAccessoryControlToRemoveAdministratorNode:completion:]_block_invoke.836
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.899
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.900
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.906
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.907
- ___86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.940
- ___86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.941
- ___88-[HMMTRSystemCommissionerPairingManager _retrievePreferredThreadCredentialsWithOptions:]_block_invoke
- ___88-[HMMTRSystemCommissionerPairingManager _retrievePreferredThreadCredentialsWithOptions:]_block_invoke.62
- ___88-[HMMTRSystemCommissionerPairingManager _retrievePreferredThreadCredentialsWithOptions:]_block_invoke_2
- ___91-[HMMTRProtocolMap servicesForDeviceTypes:device:endpoint:callbackQueue:completionHandler:]_block_invoke.429
- ___92-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fabricUUID:fatalError:]_block_invoke.318
- ___92-[HMMTRAccessoryServerBrowser _createCHIPAccessoryForNodeID:ifPaired:fabricUUID:fatalError:]_block_invoke.319
- ___93-[HMMTRDescriptorClusterManager endpointForClusterID:device:callbackQueue:completionHandler:]_block_invoke
- ___93-[HMMTRDescriptorClusterManager endpointForClusterID:device:callbackQueue:completionHandler:]_block_invoke.391
- ___94-[HMMTRAccessoryServer updateAccessoryControlToAdministratorNodes:sharedUserNodes:completion:]_block_invoke.834
- ___94-[HMMTRAccessoryServerBrowser _handleAddOrUpdateWithDiscriminator:vendorID:productID:overBLE:]_block_invoke.167
- ___96-[HMMTRDescriptorClusterManager endpointForClusterID:mtrDevice:callbackQueue:completionHandler:]_block_invoke.393
- ___96-[HMMTRProtocolMap servicesOfMTRDevice:forDeviceTypes:endpoint:callbackQueue:completionHandler:]_block_invoke.430
- ___97-[HMMTRAccessoryServerBrowser removeAccessoryServer:fromDiscoveredAccessoryServerListWithReason:]_block_invoke.303
- ___97-[HMMTRDescriptorClusterManager runBlockForAllEndpointsWithClusterID:device:callbackQueue:block:]_block_invoke
- ___99-[HMMTRSystemCommissionerPairingManager _provisionBorderRouterWithSystemCommissionerNode:endpoint:]_block_invoke
- ___99-[HMMTRSystemCommissionerPairingManager _provisionBorderRouterWithSystemCommissionerNode:endpoint:]_block_invoke_2
- ___99-[HMMTRSystemCommissionerPairingManager _provisionBorderRouterWithSystemCommissionerNode:endpoint:]_block_invoke_3
- ___Block_byref_object_copy_.10174
- ___Block_byref_object_copy_.10922
- ___Block_byref_object_copy_.11601
- ___Block_byref_object_copy_.12302
- ___Block_byref_object_copy_.12467
- ___Block_byref_object_copy_.1789
- ___Block_byref_object_copy_.3147
- ___Block_byref_object_copy_.3431
- ___Block_byref_object_copy_.4560
- ___Block_byref_object_copy_.5727
- ___Block_byref_object_copy_.5882
- ___Block_byref_object_copy_.7694
- ___Block_byref_object_copy_.8117
- ___Block_byref_object_copy_.9221
- ___Block_byref_object_dispose_.10175
- ___Block_byref_object_dispose_.10923
- ___Block_byref_object_dispose_.11602
- ___Block_byref_object_dispose_.12303
- ___Block_byref_object_dispose_.12468
- ___Block_byref_object_dispose_.1790
- ___Block_byref_object_dispose_.3148
- ___Block_byref_object_dispose_.3432
- ___Block_byref_object_dispose_.4561
- ___Block_byref_object_dispose_.5728
- ___Block_byref_object_dispose_.5883
- ___Block_byref_object_dispose_.7695
- ___Block_byref_object_dispose_.8118
- ___Block_byref_object_dispose_.9222
- ___block_descriptor_48_e8_32s40s_e95_{_HMFFutureBlockOutcome=q}16?0"MTRThreadBorderRouterManagementClusterDatasetResponseParams"8ls32l8s40l8
- ___block_descriptor_56_e8_32s40bs48w_e5_v8?0lw48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e34_{_HMFFutureBlockOutcome=q}16?08ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56r_e24_v32?0"NSError"8Q16^B24ls32l8s40l8r56l8s48l8
- ___block_literal_global.10047
- ___block_literal_global.10645
- ___block_literal_global.11195
- ___block_literal_global.11420
- ___block_literal_global.11636
- ___block_literal_global.11774
- ___block_literal_global.11904
- ___block_literal_global.12122
- ___block_literal_global.1258
- ___block_literal_global.1364
- ___block_literal_global.1441
- ___block_literal_global.1658
- ___block_literal_global.1912
- ___block_literal_global.1966
- ___block_literal_global.2012
- ___block_literal_global.208
- ___block_literal_global.2098
- ___block_literal_global.2463
- ___block_literal_global.2603
- ___block_literal_global.282.11024
- ___block_literal_global.2908
- ___block_literal_global.3051
- ___block_literal_global.3080
- ___block_literal_global.309
- ___block_literal_global.312
- ___block_literal_global.3172
- ___block_literal_global.3323
- ___block_literal_global.336
- ___block_literal_global.3515
- ___block_literal_global.353.9079
- ___block_literal_global.3684
- ___block_literal_global.3808
- ___block_literal_global.400
- ___block_literal_global.4321
- ___block_literal_global.4654
- ___block_literal_global.493
- ___block_literal_global.4946
- ___block_literal_global.5080
- ___block_literal_global.5181
- ___block_literal_global.544
- ___block_literal_global.5444
- ___block_literal_global.5616
- ___block_literal_global.5865
- ___block_literal_global.6049
- ___block_literal_global.611
- ___block_literal_global.6188
- ___block_literal_global.6297
- ___block_literal_global.6331
- ___block_literal_global.6352
- ___block_literal_global.6602
- ___block_literal_global.6615
- ___block_literal_global.6709
- ___block_literal_global.6803
- ___block_literal_global.6897
- ___block_literal_global.7000
- ___block_literal_global.7094
- ___block_literal_global.7233
- ___block_literal_global.7374
- ___block_literal_global.7483
- ___block_literal_global.7554
- ___block_literal_global.7900
- ___block_literal_global.8128
- ___block_literal_global.84
- ___block_literal_global.8462
- ___block_literal_global.8587
- ___block_literal_global.871
- ___block_literal_global.8721
- ___block_literal_global.88
- ___block_literal_global.9255
- ___block_literal_global.956
- ___block_literal_global.9654
- ___block_literal_global.982
- ___block_literal_global.9973
- _logCategory._hmf_once_t0.3050
- _logCategory._hmf_once_t0.5615
- _logCategory._hmf_once_t0.6330
- _logCategory._hmf_once_t108
- _logCategory._hmf_once_t13.3171
- _logCategory._hmf_once_t13.3514
- _logCategory._hmf_once_t14.1273
- _logCategory._hmf_once_t14.6614
- _logCategory._hmf_once_t14.6708
- _logCategory._hmf_once_t14.6802
- _logCategory._hmf_once_t14.6999
- _logCategory._hmf_once_t14.7093
- _logCategory._hmf_once_t14.7232
- _logCategory._hmf_once_t2.10046
- _logCategory._hmf_once_t2.5180
- _logCategory._hmf_once_t2.6296
- _logCategory._hmf_once_t2.7373
- _logCategory._hmf_once_t20.11773
- _logCategory._hmf_once_t202
- _logCategory._hmf_once_t26.6896
- _logCategory._hmf_once_t3.1363
- _logCategory._hmf_once_t3.1440
- _logCategory._hmf_once_t30
- _logCategory._hmf_once_t31.11903
- _logCategory._hmf_once_t35
- _logCategory._hmf_once_t4.3683
- _logCategory._hmf_once_t4.7482
- _logCategory._hmf_once_t6.2097
- _logCategory._hmf_once_t68.12329
- _logCategory._hmf_once_t683
- _logCategory._hmf_once_t8.11419
- _logCategory._hmf_once_t8.8586
- _logCategory._hmf_once_t9.6048
- _logCategory._hmf_once_v1.3052
- _logCategory._hmf_once_v1.5617
- _logCategory._hmf_once_v1.6332
- _logCategory._hmf_once_v10.6050
- _logCategory._hmf_once_v109
- _logCategory._hmf_once_v14.3173
- _logCategory._hmf_once_v14.3516
- _logCategory._hmf_once_v15.1274
- _logCategory._hmf_once_v15.6616
- _logCategory._hmf_once_v15.6710
- _logCategory._hmf_once_v15.6804
- _logCategory._hmf_once_v15.7001
- _logCategory._hmf_once_v15.7095
- _logCategory._hmf_once_v15.7234
- _logCategory._hmf_once_v203
- _logCategory._hmf_once_v21.11775
- _logCategory._hmf_once_v27.6898
- _logCategory._hmf_once_v3.10048
- _logCategory._hmf_once_v3.5182
- _logCategory._hmf_once_v3.6298
- _logCategory._hmf_once_v3.7375
- _logCategory._hmf_once_v31
- _logCategory._hmf_once_v32.11905
- _logCategory._hmf_once_v36
- _logCategory._hmf_once_v4.1365
- _logCategory._hmf_once_v4.1442
- _logCategory._hmf_once_v5.3685
- _logCategory._hmf_once_v5.7484
- _logCategory._hmf_once_v684
- _logCategory._hmf_once_v69.12330
- _logCategory._hmf_once_v7.2099
- _logCategory._hmf_once_v9.11421
- _logCategory._hmf_once_v9.8588
- _objc_msgSend$_generateThreadOperationalDataset
- _objc_msgSend$_provisionBorderRouterWithSystemCommissionerNode:endpoint:
- _objc_msgSend$_retrievePreferredThreadCredentialsWithOptions:
- _objc_msgSend$_runBlockForAllEndpointsWithClusterID:endpoints:device:callbackQueue:finishedRunningAllBlocksPromise:block:
- _objc_msgSend$addNetworkWithParams:expectedValues:expectedValueInterval:completion:
- _objc_msgSend$appBundleID
- _objc_msgSend$appStoreID
- _objc_msgSend$armFailSafeWithParams:expectedValues:expectedValueInterval:completion:
- _objc_msgSend$batchedAccessories
- _objc_msgSend$commissioningCompleteWithExpectedValues:expectedValueInterval:completion:
- _objc_msgSend$endpointForClusterID:device:callbackQueue:completionHandler:
- _objc_msgSend$fetchEndpointsForDevice:endpointID:callbackQueue:completionHandler:
- _objc_msgSend$fetchHAPCategoryForCHIPDevice:nodeId:server:callbackQueue:completionHandler:
- _objc_msgSend$getActiveDatasetRequestWithExpectedValues:expectedValueInterval:completion:
- _objc_msgSend$initWithDataset:borderAgentEUI:
- _objc_msgSend$mtrDeviceStateReported
- _objc_msgSend$setActiveDatasetRequestWithParams:expectedValues:expectedValueInterval:completion:
- _objc_msgSend$setAppBundleID:
- _objc_msgSend$setAppStoreID:
- _objc_msgSend$setBatchedAccessories:
CStrings:
+ "%{public}@Cancelling cloud metadata fetch"
+ "%{public}@Cloud metadata fetch already in progress, skipping duplicate request"
+ "%{public}@Cloud metadata fetch cancelled"
+ "%{public}@Cloud metadata fetch failed, scheduling retry %lu in %.1f seconds"
+ "%{public}@Cloud metadata fetch succeeded, resetting retry state"
+ "%{public}@Commission metrics ready handler was already set when another handler was requested. The second handler is called regardless of metrics readiness."
+ "%{public}@Constructed Service Label service at endpoint %@ of node %@"
+ "%{public}@Failed to read parts list for endpoint 0: %@"
+ "%{public}@Fetching cloud metadata by requesting supported accessories from UARP controller (attempt %lu)"
+ "%{public}@Maximum retry time (%.1f hours) exceeded, giving up on cloud metadata fetch"
+ "%{public}@MinSetpointDeadBand attribute from the %@ cluster endpoint:%@ of node %@ not available"
+ "%{public}@Multiple primary service candidates found: %@"
+ "%{public}@No Endpoints In Use at endpoint 0 of node %@"
+ "%{public}@Retry cancelled - fetch no longer in progress"
+ "%{public}@Saving AbsMaxHeatSetpointLimit attribute as %@ from the %@ cluster for endpoint:%@ of node %@"
+ "%{public}@Saving MinSetpointDeadBand attribute as %@ from the %@ cluster for endpoint:%@ of node %@"
+ "%{public}@Successfully enabled Border Router on System Commissioner node %@"
+ "%{public}@Successfully provisioned Thread credentials on System Commissioner node %@"
+ "%{public}@Successfully retrieved Thread credentials from System Commissioner node %@"
+ "%{public}@Total endpoints In Use at endpoint 0 of node %@: %@"
+ "%{public}@stopPairing requested without metrics ready handler"
+ "%{public}@stopPairing will not wait for metrics submission because commissioning complete callback is not guaranteed"
+ "%{public}@stopPairing will wait for controller:commissioningComplete: callback before removing pairing so that Matter metrics can be propagated"
+ "@\"NSString\"16@?0@\"HAPService\"8"
+ "@\"NSString\"16@?0@\"NSString\"8"
+ "@72@0:8@16S24S28@32Q40@48@56@64"
+ "AlwaysSecondaryHAPServices"
+ "B16@?0@\"NSString\"8"
+ "HMMTRUARPAccessory"
+ "I24@0:8@16"
+ "MinSetpointDeadBand"
+ "PotentialSecondaryHAPServices"
+ "T@\"HMFTimer\",&,V_retryTimer"
+ "T@\"NSArray\",&,N,V_rootEndpointPartsList"
+ "T@\"NSObject<OS_dispatch_queue>\",R,V_retryQueue"
+ "T@\"NSString\",R,N,V_accessoryMarketingName"
+ "T@\"NSString\",R,N,V_accessoryProductLabel"
+ "T@\"NSString\",R,N,V_productNumber"
+ "T@\"NSString\",R,N,V_vendorName"
+ "T@\"NSURL\",R,N,V_accessoryInstallationGuideURL"
+ "T@?,C,N,V_commissionMetricsReadyHandler"
+ "TB,N,V_commissionCompletePending"
+ "TB,N,V_fetchInProgress"
+ "TB,V_overriddenAsPrimary"
+ "TQ,R,N,V_accessoryCategoryNumber"
+ "TQ,V_retryCount"
+ "TS,R,N,V_productID"
+ "TS,R,N,V_vendorID"
+ "Td,N,V_retryIntervalOverride"
+ "Td,V_firstFailureTime"
+ "_accessoryCategoryNumber"
+ "_accessoryInstallationGuideURL"
+ "_accessoryMarketingName"
+ "_accessoryProductLabel"
+ "_augmentDatasetWithBorderAgentIDsForDevice:endpoint:dataset:"
+ "_commissionCompletePending"
+ "_commissionMetricsReadyHandler"
+ "_fetchInProgress"
+ "_firstFailureTime"
+ "_handleCloudMetadataFetchFailure"
+ "_handleCloudMetadataFetchSuccess"
+ "_overriddenAsPrimary"
+ "_productNumber"
+ "_provisionBorderRouterWithSystemCommissionerNode:endpoint:dataset:"
+ "_queueOpenPairingWindowWithPINForDuration:completionHandler:"
+ "_retrievePreferredThreadCredentialsOrCreateWithDataset:"
+ "_retrieveRootEndpointPartsListWithDevice:completion:"
+ "_retryIntervalOverride"
+ "_retryQueue"
+ "_retryTimer"
+ "_rootEndpointPartsList"
+ "_storageDidBecomeAvailable:"
+ "addNetworkWithParams:completion:"
+ "attemptCloudMetadataFetch"
+ "cancelCloudMetadataFetch"
+ "com.apple.homekit.matter.vendor.metadata.retry"
+ "commissionCompletePending"
+ "commissionMetricsReadyHandler"
+ "completion"
+ "device controller unavailable"
+ "endpointForClusterID:device:partsList:callbackQueue:completionHandler:"
+ "fetchHAPCategoryForCHIPDevice:nodeId:server:partsList:callbackQueue:completionHandler:"
+ "fetchInProgress"
+ "firstFailureTime"
+ "fromUARPSupportedAccessory:"
+ "getActiveDatasetRequestWithCompletion:"
+ "handleBDXTransferSessionEndForNodeID:controller:metrics:error:"
+ "initWithDataset:borderAgentEUI:borderAgentID:"
+ "initWithProductNumber:vendorID:productID:vendorName:accessoryCategoryNumber:accessoryMarketingName:accessoryProductLabel:accessoryInstallationGuideURL:"
+ "makeMatterKeypair"
+ "minSetpointDeadBand"
+ "overriddenAsPrimary"
+ "primaryHAPServiceAmongServices:"
+ "rawPlistOffsetForKey:"
+ "readAttributeMinSetpointDeadBandWithParams:"
+ "readAttributePaths:eventPaths:params:queue:completion:"
+ "requestPathWithEndpointID:clusterID:attributeID:"
+ "resultServiceType"
+ "retrievePreferredThreadCredentialsOrCreateWithDataset:completionHandler:"
+ "retryIntervalOverride"
+ "retryQueue"
+ "retryTimer"
+ "rootEndpointPartsList"
+ "serviceProperties"
+ "setActiveDatasetRequestWithParams:completion:"
+ "setCommissionCompletePending:"
+ "setCommissionMetricsReadyHandler:"
+ "setFetchInProgress:"
+ "setFirstFailureTime:"
+ "setOverriddenAsPrimary:"
+ "setPrimary"
+ "setRetryIntervalOverride:"
+ "setRetryTimer:"
+ "setRootEndpointPartsList:"
+ "startThreadRadioForSystemCommissionerFabricUUID:completion:"
+ "stopPairingWithError:metricsReadyHandler:"
+ "v32@0:8^@16@?24"
+ "v48@0:8@\"NSNumber\"16@\"MTRDeviceController\"24@\"MTRMetrics\"32@\"NSError\"40"
+ "{_HMFFutureBlockOutcome=q@}16@?0@\"MTSThreadNetworkCredential\"8"
+ "\xf0\x82\xf0\xf0\xf1\xc1"
- "%{public}@Constructed Service Label service at endpoint %@"
- "%{public}@Could not find metadata on chip device information: %@"
- "%{public}@Examining MTRBaseClusterDescriptor cluster parts list at endpoint %@ to retrieve endpoints in use."
- "%{public}@Failed to get endpoints for device: %@"
- "%{public}@Failed to read parts list. Error: %@"
- "%{public}@Fetching cloud metadata by requesting supported accessories from UARP controller"
- "%{public}@Received supported accessory with unexpected hardwareID: %@"
- "%{public}@Received supported vendor record with unexpected hardwareID: %@"
- "%{public}@Retrieved the following endpoints in use %@"
- "%{public}@Running block on all endpoints with clusterID %@"
- "%{public}@Saving defaultAbsMaxHeatSetpointLimit attribute as %@ from the %@ cluster for endpoint:%@ of node %@"
- "%{public}@Successfully provisioned Border Router on System Commissioner node %@"
- "%{public}@Successfully retrieved Thread dataset from System Commissioner node %@"
- "App Bundle ID"
- "App Store ID"
- "AppBundleID"
- "AppStoreID"
- "Failed to generate dataset"
- "No MTRDevice"
- "T@\"NSString\",C,V_appBundleID"
- "T@\"NSString\",C,V_appStoreID"
- "_appBundleID"
- "_appStoreID"
- "_generateThreadOperationalDataset"
- "_provisionBorderRouterWithSystemCommissionerNode:endpoint:"
- "_retrievePreferredThreadCredentialsWithOptions:"
- "addNetworkWithParams:expectedValues:expectedValueInterval:completion:"
- "appBundleID"
- "appStoreID"
- "armFailSafeWithParams:expectedValues:expectedValueInterval:completion:"
- "commissioningCompleteWithExpectedValues:expectedValueInterval:completion:"
- "endpointForClusterID:device:callbackQueue:completionHandler:"
- "fetchEndpointsForDevice:endpointID:callbackQueue:completionHandler:"
- "fetchHAPCategoryForCHIPDevice:nodeId:server:callbackQueue:completionHandler:"
- "getActiveDatasetRequestWithExpectedValues:expectedValueInterval:completion:"
- "initWithDataset:borderAgentEUI:"
- "retrievePreferredThreadCredentialsWithOptions:completionHandler:"
- "runBlockForAllEndpointsWithClusterID:device:callbackQueue:block:"
- "setActiveDatasetRequestWithParams:expectedValues:expectedValueInterval:completion:"
- "setAppBundleID:"
- "setAppStoreID:"
- "\xf0\x82\xf0\xf0\xd1\xc1"

```
