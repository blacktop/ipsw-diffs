## HomeKitMatter

> `/System/Library/PrivateFrameworks/HomeKitMatter.framework/Versions/A/HomeKitMatter`

```diff

-1493.1.5.4.1
-  __TEXT.__text: 0x18f1a8
-  __TEXT.__objc_methlist: 0xabf4
-  __TEXT.__const: 0x280
+1520.2.7.4.1
+  __TEXT.__text: 0x19c36c
+  __TEXT.__objc_methlist: 0xafac
+  __TEXT.__const: 0x2b0
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__gcc_except_tab: 0x3070
-  __TEXT.__cstring: 0x6b01
-  __TEXT.__oslogstring: 0x4b788
+  __TEXT.__gcc_except_tab: 0x3454
+  __TEXT.__cstring: 0x6f3b
+  __TEXT.__oslogstring: 0x4de25
   __TEXT.__ustring: 0x68
-  __TEXT.__unwind_info: 0x30f8
+  __TEXT.__unwind_info: 0x32b0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xb78
-  __DATA_CONST.__objc_classlist: 0x458
+  __DATA_CONST.__const: 0xc28
+  __DATA_CONST.__objc_classlist: 0x460
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6e50
+  __DATA_CONST.__objc_selrefs: 0x7138
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x310
-  __DATA_CONST.__objc_arraydata: 0x240
-  __DATA_CONST.__got: 0x970
-  __AUTH_CONST.__const: 0x56d0
-  __AUTH_CONST.__cfstring: 0x6ba0
-  __AUTH_CONST.__objc_const: 0x102c8
-  __AUTH_CONST.__objc_intobj: 0x16b0
-  __AUTH_CONST.__objc_arrayobj: 0x168
+  __DATA_CONST.__objc_superrefs: 0x318
+  __DATA_CONST.__objc_arraydata: 0x250
+  __DATA_CONST.__got: 0x9c8
+  __AUTH_CONST.__const: 0x5a00
+  __AUTH_CONST.__cfstring: 0x6f20
+  __AUTH_CONST.__objc_const: 0x10770
+  __AUTH_CONST.__objc_intobj: 0x17a0
+  __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x1e50
-  __DATA.__objc_ivar: 0xb70
+  __AUTH.__objc_data: 0x1ea0
+  __DATA.__objc_ivar: 0xbc4
   __DATA.__data: 0xea0
-  __DATA.__bss: 0x498
+  __DATA.__bss: 0x4c8
   __DATA_DIRTY.__objc_data: 0xd20
   __DATA_DIRTY.__bss: 0xa0
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth

   - /System/Library/PrivateFrameworks/UARPKit.framework/Versions/A/UARPKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4509
-  Symbols:   10330
-  CStrings:  5536
+  Functions: 4648
+  Symbols:   10618
+  CStrings:  5715
 
Symbols:
+ +[HMMTRAsyncMutex logCategory]
+ +[HMMTRFeatures disableDemoModeSuppressDPSForTests]
+ +[HMMTRFeatures disableFeatureLockDPSForTests]
+ +[HMMTRFeatures enableDemoModeSuppressDPSForTests]
+ +[HMMTRFeatures enableFeatureLockDPSForTests]
+ +[HMMTRFeatures unsetDemoModeSuppressDPSForTests]
+ +[HMMTRFeatures unsetFeatureLockDPSForTests]
+ +[HMMTRMultiFabricDataStoreQuery v2FabricDataItemPreferenceComparator]
+ +[HMMTRProtocolMap mapTargetAirPurifierState:]
+ -[HMMTRAccessoryServer _deviceStorageDataSourceForCurrentNode]
+ -[HMMTRAccessoryServer _endPairingMode]
+ -[HMMTRAccessoryServer _enqueueResumeFinalizeAttempt]
+ -[HMMTRAccessoryServer _invalidateFinalizeRetry]
+ -[HMMTRAccessoryServer _persistThreadWEDInfoToStorage]
+ -[HMMTRAccessoryServer _readCharacteristicValueFromCacheAfterConfirmingBridgedAccessoryReachabilityWithCharacteristic:responseHandler:]
+ -[HMMTRAccessoryServer _resumeFinalizePairing]
+ -[HMMTRAccessoryServer _scheduleFinalizeRetry]
+ -[HMMTRAccessoryServer connectivityMonitorClusterFactory]
+ -[HMMTRAccessoryServer finalizeRetryAttempt]
+ -[HMMTRAccessoryServer finalizeRetryTimer]
+ -[HMMTRAccessoryServer generalCommissioningClusterFactory]
+ -[HMMTRAccessoryServer networkCommissioningClusterFactory]
+ -[HMMTRAccessoryServer pendingReenumerationCompletionHandlers]
+ -[HMMTRAccessoryServer pendingServiceReenumeration]
+ -[HMMTRAccessoryServer removeClusterIDForCharacteristic:endpointID:]
+ -[HMMTRAccessoryServer removeNode:withPrivilege:fromExistingAclEntries:]
+ -[HMMTRAccessoryServer resumeFinalizeForCommissionedAccessoryWithOnboardingURL:]
+ -[HMMTRAccessoryServer setConnectivityMonitorClusterFactory:]
+ -[HMMTRAccessoryServer setFinalizeRetryAttempt:]
+ -[HMMTRAccessoryServer setFinalizeRetryTimer:]
+ -[HMMTRAccessoryServer setGeneralCommissioningClusterFactory:]
+ -[HMMTRAccessoryServer setNetworkCommissioningClusterFactory:]
+ -[HMMTRAccessoryServer setPendingServiceReenumeration:]
+ -[HMMTRAccessoryServer(Diagnostics) supportsEnhancedMetricsForAccessory:]
+ -[HMMTRAccessoryServer(NetworkRepair) _addThreadNetwork:dataset:completion:]
+ -[HMMTRAccessoryServer(NetworkRepair) _addWiFiNetworks:networks:completion:]
+ -[HMMTRAccessoryServer(NetworkRepair) _armFailSafeWithCluster:completion:]
+ -[HMMTRAccessoryServer(NetworkRepair) _commissioningCompleteWithCluster:completion:]
+ -[HMMTRAccessoryServer(NetworkRepair) _connectThreadNetwork:networkID:completion:]
+ -[HMMTRAccessoryServer(NetworkRepair) _createGeneralCommissioningCluster]
+ -[HMMTRAccessoryServer(NetworkRepair) _createThreadNetworkCommissioningCluster]
+ -[HMMTRAccessoryServer(NetworkRepair) _createWiFiNetworkCommissioningCluster]
+ -[HMMTRAccessoryServer(NetworkRepair) _disarmFailSafeWithCluster:completion:]
+ -[HMMTRAccessoryServer(NetworkRepair) _extractThreadExtendedPANIDFromNetworksAttribute:]
+ -[HMMTRAccessoryServer(NetworkRepair) _extractWiFiSSIDsFromNetworksAttribute:]
+ -[HMMTRAccessoryServer(NetworkRepair) _findAllNetworkCommissioningEndpoints]
+ -[HMMTRAccessoryServer(NetworkRepair) _findNetworkCommissioningEndpointForInterfaceType:]
+ -[HMMTRAccessoryServer(NetworkRepair) _handleAtCapacityWiFiRepair:deviceSSIDs:preferredNetworks:maxNetworks:completion:]
+ -[HMMTRAccessoryServer(NetworkRepair) _hasDualNetworkCommissioningClusters]
+ -[HMMTRAccessoryServer(NetworkRepair) _removeWiFiNetwork:ssid:completion:]
+ -[HMMTRAccessoryServer(NetworkRepair) _reorderWiFiNetworks:networks:completion:]
+ -[HMMTRAccessoryServer(NetworkRepair) hasDualNetworkCommissioningClusters]
+ -[HMMTRAccessoryServer(NetworkRepair) repairThreadNetworkWithCompletion:completion:]
+ -[HMMTRAccessoryServer(NetworkRepair) repairWiFiNetworkWithCompletion:completion:]
+ -[HMMTRAccessoryServerBrowser _makeAccessoryServerFactory]
+ -[HMMTRAccessoryServerBrowser _updateDiscoveredAccessoryServersWithNodes:fabricUUID:completion:]
+ -[HMMTRAccessoryServerBrowser discoveredAccessoryServersAsyncMutex]
+ -[HMMTRAccessoryServerBrowser fetchPreferredThreadCredentialsUsingFabricUUID:systemCommissionerFabric:withCompletion:]
+ -[HMMTRAccessoryServerBrowser hasPresentCommissionableNodeMatchingOnboardingURL:]
+ -[HMMTRAccessoryServerBrowser updateDiscoveredAccessoryServersWithNodes:fabricUUID:completion:]
+ -[HMMTRAccessoryServerBrowser workQueueFactory]
+ -[HMMTRAccessoryServerFactory workQueueFactory]
+ -[HMMTRAsyncMutex .cxx_destruct]
+ -[HMMTRAsyncMutex initWithQueue:]
+ -[HMMTRAsyncMutex lockWithCompletion:]
+ -[HMMTRAsyncMutex locked]
+ -[HMMTRAsyncMutex pendingCompletions]
+ -[HMMTRAsyncMutex queue]
+ -[HMMTRAsyncMutex setLocked:]
+ -[HMMTRAsyncMutex unlock]
+ -[HMMTRControllerFactory workQueueFactory]
+ -[HMMTRControllerFactoryStorage initWithWorkQueueFactory:]
+ -[HMMTRControllerFactoryStorage workQueueFactory]
+ -[HMMTRDescriptorClusterManager workQueueFactory]
+ -[HMMTRExclusiveServerActionQueue workQueueFactory]
+ -[HMMTRFirmwareUpdateStatus workQueueFactory]
+ -[HMMTRSyncClusterThermostat readAttributePluginCurrentRelativeHumidityWithParams:]
+ -[HMMTRSyncClusterThermostat updatedValuePluginCurrentRelativeHumidityForAttributeReport:responseHandler:]
+ -[HMMTRSyncClusterWindowCovering _targetPositionDictionary:fallingBackToCurrentPositionLift:params:]
+ -[HMMTRSystemCommissionerControllerParams workQueueFactory]
+ -[HMMTRThreadRadioManager eMACAddressOfPairingAccessory]
+ -[HMMTRThreadRadioManager setEMACAddressOfPairingAccessory:]
+ -[HMMTRThreadRadioManager workQueueFactory]
+ GCC_except_table1003
+ GCC_except_table1007
+ GCC_except_table1009
+ GCC_except_table1011
+ GCC_except_table1013
+ GCC_except_table1017
+ GCC_except_table1020
+ GCC_except_table1083
+ GCC_except_table1089
+ GCC_except_table1091
+ GCC_except_table1213
+ GCC_except_table1281
+ GCC_except_table1327
+ GCC_except_table1335
+ GCC_except_table1388
+ GCC_except_table1396
+ GCC_except_table1433
+ GCC_except_table1471
+ GCC_except_table1498
+ GCC_except_table1697
+ GCC_except_table1740
+ GCC_except_table1894
+ GCC_except_table1895
+ GCC_except_table1919
+ GCC_except_table1920
+ GCC_except_table1921
+ GCC_except_table1922
+ GCC_except_table1923
+ GCC_except_table1926
+ GCC_except_table1929
+ GCC_except_table1930
+ GCC_except_table1931
+ GCC_except_table1932
+ GCC_except_table1933
+ GCC_except_table1934
+ GCC_except_table1935
+ GCC_except_table1946
+ GCC_except_table1949
+ GCC_except_table1950
+ GCC_except_table1951
+ GCC_except_table1961
+ GCC_except_table1970
+ GCC_except_table1979
+ GCC_except_table1981
+ GCC_except_table1982
+ GCC_except_table1984
+ GCC_except_table2053
+ GCC_except_table2059
+ GCC_except_table2147
+ GCC_except_table2265
+ GCC_except_table2267
+ GCC_except_table2298
+ GCC_except_table2309
+ GCC_except_table2311
+ GCC_except_table2367
+ GCC_except_table2413
+ GCC_except_table2438
+ GCC_except_table2510
+ GCC_except_table2810
+ GCC_except_table2812
+ GCC_except_table2816
+ GCC_except_table2877
+ GCC_except_table2910
+ GCC_except_table2957
+ GCC_except_table2959
+ GCC_except_table2990
+ GCC_except_table2991
+ GCC_except_table2992
+ GCC_except_table3014
+ GCC_except_table3015
+ GCC_except_table3016
+ GCC_except_table3017
+ GCC_except_table3018
+ GCC_except_table3019
+ GCC_except_table3021
+ GCC_except_table3031
+ GCC_except_table3033
+ GCC_except_table3045
+ GCC_except_table3066
+ GCC_except_table3081
+ GCC_except_table3087
+ GCC_except_table3102
+ GCC_except_table3105
+ GCC_except_table3109
+ GCC_except_table3124
+ GCC_except_table3127
+ GCC_except_table3131
+ GCC_except_table3133
+ GCC_except_table3163
+ GCC_except_table3172
+ GCC_except_table3177
+ GCC_except_table3189
+ GCC_except_table3243
+ GCC_except_table3244
+ GCC_except_table3640
+ GCC_except_table3665
+ GCC_except_table3666
+ GCC_except_table3667
+ GCC_except_table3671
+ GCC_except_table3677
+ GCC_except_table3680
+ GCC_except_table3696
+ GCC_except_table3711
+ GCC_except_table3780
+ GCC_except_table3781
+ GCC_except_table3814
+ GCC_except_table3823
+ GCC_except_table3827
+ GCC_except_table3861
+ GCC_except_table3865
+ GCC_except_table3873
+ GCC_except_table3895
+ GCC_except_table3899
+ GCC_except_table3942
+ GCC_except_table3944
+ GCC_except_table3946
+ GCC_except_table3965
+ GCC_except_table3967
+ GCC_except_table3988
+ GCC_except_table4065
+ GCC_except_table4112
+ GCC_except_table4132
+ GCC_except_table4155
+ GCC_except_table4159
+ GCC_except_table4174
+ GCC_except_table4175
+ GCC_except_table4176
+ GCC_except_table4182
+ GCC_except_table4189
+ GCC_except_table4194
+ GCC_except_table4231
+ GCC_except_table4253
+ GCC_except_table4299
+ GCC_except_table4305
+ GCC_except_table4308
+ GCC_except_table4394
+ GCC_except_table4395
+ GCC_except_table4453
+ GCC_except_table4456
+ GCC_except_table4520
+ GCC_except_table4580
+ GCC_except_table4584
+ GCC_except_table4590
+ GCC_except_table4594
+ GCC_except_table4628
+ GCC_except_table594
+ GCC_except_table600
+ GCC_except_table602
+ GCC_except_table606
+ GCC_except_table776
+ GCC_except_table777
+ GCC_except_table834
+ GCC_except_table835
+ GCC_except_table836
+ GCC_except_table909
+ GCC_except_table951
+ OBJC_IVAR_$_HMMTRAccessoryServer._connectivityMonitorClusterFactory
+ OBJC_IVAR_$_HMMTRAccessoryServer._finalizeRetryAttempt
+ OBJC_IVAR_$_HMMTRAccessoryServer._finalizeRetryTimer
+ OBJC_IVAR_$_HMMTRAccessoryServer._generalCommissioningClusterFactory
+ OBJC_IVAR_$_HMMTRAccessoryServer._networkCommissioningClusterFactory
+ OBJC_IVAR_$_HMMTRAccessoryServer._pendingReenumerationCompletionHandlers
+ OBJC_IVAR_$_HMMTRAccessoryServer._pendingServiceReenumeration
+ OBJC_IVAR_$_HMMTRAccessoryServerBrowser._discoveredAccessoryServersAsyncMutex
+ OBJC_IVAR_$_HMMTRAccessoryServerBrowser._workQueueFactory
+ OBJC_IVAR_$_HMMTRAccessoryServerFactory._workQueueFactory
+ OBJC_IVAR_$_HMMTRAsyncMutex._locked
+ OBJC_IVAR_$_HMMTRAsyncMutex._pendingCompletions
+ OBJC_IVAR_$_HMMTRAsyncMutex._queue
+ OBJC_IVAR_$_HMMTRControllerFactory._workQueueFactory
+ OBJC_IVAR_$_HMMTRControllerFactoryStorage._workQueueFactory
+ OBJC_IVAR_$_HMMTRDescriptorClusterManager._workQueueFactory
+ OBJC_IVAR_$_HMMTRExclusiveServerActionQueue._workQueueFactory
+ OBJC_IVAR_$_HMMTRFirmwareUpdateStatus._workQueueFactory
+ OBJC_IVAR_$_HMMTRSystemCommissionerControllerParams._workQueueFactory
+ OBJC_IVAR_$_HMMTRThreadRadioManager._eMACAddressOfPairingAccessory
+ OBJC_IVAR_$_HMMTRThreadRadioManager._workQueueFactory
+ _AppleExtensionNeedsAdditionalConfigurationAttribute
+ _HAPWorkQueueFactoryOrDefault
+ _HMErrorDomain
+ _HMMTRAccessoryServerDeferredMatterCommissioningErrorKey
+ _HMMTRAccessoryServerDeferredMatterCommissioningNodeIDKey
+ _HMMTRAccessoryServerDidBeginDeferredMatterCommissioningNotification
+ _HMMTRAccessoryServerDidFailDeferredMatterCommissioningNotification
+ _HMMTRIsSecondPartyProduct
+ _OBJC_CLASS_$_HMHomeManager
+ _OBJC_CLASS_$_HMMTRAsyncMutex
+ _OBJC_CLASS_$_MTRClusterAppleAccessoryConnectivityMonitor
+ _OBJC_CLASS_$_MTRNetworkCommissioningClusterAddOrUpdateThreadNetworkParams
+ _OBJC_CLASS_$_MTRNetworkCommissioningClusterAddOrUpdateWiFiNetworkParams
+ _OBJC_CLASS_$_MTRNetworkCommissioningClusterConnectNetworkParams
+ _OBJC_CLASS_$_MTRNetworkCommissioningClusterRemoveNetworkParams
+ _OBJC_CLASS_$_MTRNetworkCommissioningClusterReorderNetworkParams
+ _OBJC_CLASS_$_MTRThreadOperationalDataset
+ _OBJC_METACLASS_$_HMMTRAsyncMutex
+ __118-[HMMTRAccessoryServerBrowser fetchPreferredThreadCredentialsUsingFabricUUID:systemCommissionerFabric:withCompletion:]_block_invoke
+ __120-[HMMTRAccessoryServer(NetworkRepair) _handleAtCapacityWiFiRepair:deviceSSIDs:preferredNetworks:maxNetworks:completion:]_block_invoke
+ __177-[HMMTRAccessoryServerBrowser setOperationalFabricData:operationalCertIssuer:storageDataSource:allTargetFabricUUIDs:entityIdentifier:accessoryServerNodeIDs:forTargetFabricUUID:]_block_invoke
+ __49-[HMMTRAccessoryServer initWithKeystore:browser:]_block_invoke
+ __54-[HMMTRAccessoryServer _persistThreadWEDInfoToStorage]_block_invoke
+ __76-[HMMTRAccessoryServer(NetworkRepair) _addWiFiNetworks:networks:completion:]_block_invoke
+ __80-[HMMTRAccessoryServer(NetworkRepair) _reorderWiFiNetworks:networks:completion:]_block_invoke
+ __82-[HMMTRAccessoryServer(NetworkRepair) repairWiFiNetworkWithCompletion:completion:]_block_invoke
+ __83-[HMMTRAccessoryServerBrowser invalidateAllDiscoveredServersWithReason:completion:]_block_invoke
+ __84-[HMMTRAccessoryServer(NetworkRepair) repairThreadNetworkWithCompletion:completion:]_block_invoke
+ __96-[HMMTRAccessoryServerBrowser _updateDiscoveredAccessoryServersWithNodes:fabricUUID:completion:]_block_invoke
+ __OBJC_$_CLASS_METHODS_HMMTRAsyncMutex
+ __OBJC_$_INSTANCE_METHODS_HMMTRAccessoryServer(HAPAccessory|RemoteAccess|Diagnostics|DiagnosticsInternal|SystemCommissionerPairing|NetworkRepair)
+ __OBJC_$_INSTANCE_METHODS_HMMTRAsyncMutex
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRAsyncMutex
+ __OBJC_$_PROP_LIST_HMMTRAsyncMutex
+ __OBJC_CLASS_RO_$_HMMTRAsyncMutex
+ __OBJC_METACLASS_RO_$_HMMTRAsyncMutex
+ ___118-[HMMTRAccessoryServerBrowser fetchPreferredThreadCredentialsUsingFabricUUID:systemCommissionerFabric:withCompletion:]_block_invoke
+ ___120-[HMMTRAccessoryServer(NetworkRepair) _handleAtCapacityWiFiRepair:deviceSSIDs:preferredNetworks:maxNetworks:completion:]_block_invoke
+ ___139-[HMMTRAccessoryServer scheduleOrExecuteOTAProviderAnnouncement:initiatorType:immediateAnnouncement:endpoint:delayCounter:isUserTriggered:]_block_invoke_2
+ ___177-[HMMTRAccessoryServerBrowser setOperationalFabricData:operationalCertIssuer:storageDataSource:allTargetFabricUUIDs:entityIdentifier:accessoryServerNodeIDs:forTargetFabricUUID:]_block_invoke_2
+ ___25-[HMMTRAsyncMutex unlock]_block_invoke
+ ___30+[HMMTRAsyncMutex logCategory]_block_invoke
+ ___38-[HMMTRAsyncMutex lockWithCompletion:]_block_invoke
+ ___39-[HMMTRAccessoryServer _endPairingMode]_block_invoke
+ ___46-[HMMTRAccessoryServer _resumeFinalizePairing]_block_invoke
+ ___49-[HMMTRAccessoryServer initWithKeystore:browser:]_block_invoke_2
+ ___49-[HMMTRAccessoryServer initWithKeystore:browser:]_block_invoke_3
+ ___53-[HMMTRAccessoryServer _enqueueResumeFinalizeAttempt]_block_invoke
+ ___54-[HMMTRAccessoryServer _persistThreadWEDInfoToStorage]_block_invoke
+ ___70+[HMMTRMultiFabricDataStoreQuery v2FabricDataItemPreferenceComparator]_block_invoke
+ ___73-[HMMTRAccessoryServer(Diagnostics) supportsEnhancedMetricsForAccessory:]_block_invoke
+ ___74-[HMMTRAccessoryServer(NetworkRepair) _armFailSafeWithCluster:completion:]_block_invoke
+ ___74-[HMMTRAccessoryServer(NetworkRepair) _removeWiFiNetwork:ssid:completion:]_block_invoke
+ ___76-[HMMTRAccessoryServer(NetworkRepair) _addThreadNetwork:dataset:completion:]_block_invoke
+ ___76-[HMMTRAccessoryServer(NetworkRepair) _addWiFiNetworks:networks:completion:]_block_invoke
+ ___77-[HMMTRAccessoryServer(NetworkRepair) _disarmFailSafeWithCluster:completion:]_block_invoke
+ ___80-[HMMTRAccessoryServer resumeFinalizeForCommissionedAccessoryWithOnboardingURL:]_block_invoke
+ ___80-[HMMTRAccessoryServer(NetworkRepair) _reorderWiFiNetworks:networks:completion:]_block_invoke
+ ___82-[HMMTRAccessoryServer(NetworkRepair) _connectThreadNetwork:networkID:completion:]_block_invoke
+ ___82-[HMMTRAccessoryServer(NetworkRepair) repairWiFiNetworkWithCompletion:completion:]_block_invoke
+ ___82-[HMMTRAccessoryServer(NetworkRepair) repairWiFiNetworkWithCompletion:completion:]_block_invoke_2
+ ___84-[HMMTRAccessoryServer(NetworkRepair) _commissioningCompleteWithCluster:completion:]_block_invoke
+ ___84-[HMMTRAccessoryServer(NetworkRepair) repairThreadNetworkWithCompletion:completion:]_block_invoke
+ ___84-[HMMTRAccessoryServer(NetworkRepair) repairThreadNetworkWithCompletion:completion:]_block_invoke_2
+ ___84-[HMMTRAccessoryServer(NetworkRepair) repairThreadNetworkWithCompletion:completion:]_block_invoke_3
+ ___84-[HMMTRAccessoryServer(NetworkRepair) repairThreadNetworkWithCompletion:completion:]_block_invoke_4
+ ___84-[HMMTRAccessoryServer(NetworkRepair) repairThreadNetworkWithCompletion:completion:]_block_invoke_5
+ ___95-[HMMTRAccessoryServerBrowser updateDiscoveredAccessoryServersWithNodes:fabricUUID:completion:]_block_invoke
+ ___96-[HMMTRAccessoryServerBrowser _updateDiscoveredAccessoryServersWithNodes:fabricUUID:completion:]_block_invoke
+ ___block_descriptor_104_e8_32s40s48s56s64s72bs80bs88w_e17_v16?0"NSError"8l
+ ___block_descriptor_32_e111_q24?0"<HMMTRMultiFabricDataStoreQueryV2FabricDataItem>"8"<HMMTRMultiFabricDataStoreQueryV2FabricDataItem>"16l
+ ___block_descriptor_32_e65_"MTRClusterNetworkCommissioning"24?0"HMMTRAccessoryServer"8Q16l
+ ___block_descriptor_32_e66_"MTRBaseClusterGeneralCommissioning"16?0"HMMTRAccessoryServer"8l
+ ___block_descriptor_32_e88_"MTRClusterAppleAccessoryConnectivityMonitor"24?0"HMMTRAccessoryServer"8"NSNumber"16l
+ ___block_descriptor_40_e8_32bs_e79_v24?0"MTRNetworkCommissioningClusterNetworkConfigResponseParams"8"NSError"16l
+ ___block_descriptor_48_e8_32bs40w_e79_v24?0"MTRNetworkCommissioningClusterNetworkConfigResponseParams"8"NSError"16l
+ ___block_descriptor_48_e8_32s40bs_e80_v24?0"MTRNetworkCommissioningClusterConnectNetworkResponseParams"8"NSError"16l
+ ___block_descriptor_48_e8_32s40bs_e87_v24?0"MTRGeneralCommissioningClusterCommissioningCompleteResponseParams"8"NSError"16l
+ ___block_descriptor_56_e8_32bs40r48r_e5_v8?0l
+ ___block_descriptor_56_e8_32bs40r48w_e5_v8?0l
+ ___block_descriptor_56_e8_32s40bs48w_e17_v16?0"NSError"8l
+ ___block_descriptor_57_e8_32s40s48bs_e46_v24?0"HAPThreadNetworkMetadata"8"NSError"16l
+ ___block_descriptor_64_e8_32s40s48bs56w_e17_v16?0"NSError"8l
+ ___block_descriptor_72_e8_32s40s48r56r64w_e79_v24?0"MTRNetworkCommissioningClusterNetworkConfigResponseParams"8"NSError"16l
+ ___block_descriptor_72_e8_32s40s48s56bs64w_e17_v16?0"NSError"8l
+ ___block_descriptor_80_e8_32s40s48r56r64r72w_e79_v24?0"MTRNetworkCommissioningClusterNetworkConfigResponseParams"8"NSError"16l
+ ___block_descriptor_80_e8_32s40s48s56s64bs72w_e17_v16?0"NSError"8l
+ ___copy_helper_block_e8_32b40r48r
+ ___copy_helper_block_e8_32s40s48r56r64r72w
+ ___copy_helper_block_e8_32s40s48r56r64w
+ ___copy_helper_block_e8_32s40s48s56s64b72w
+ ___copy_helper_block_e8_32s40s48s56s64s72b80b88w
+ ___destroy_helper_block_e8_32s40s48r56r64r72w
+ ___destroy_helper_block_e8_32s40s48r56r64w
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s88w
+ ___destroy_helper_block_e8_32s40s48s56s64s72w
+ ___suppressDpsForDemoMode_block_invoke
+ __dispatch_main_q
+ _isFeatureLockDPSEnabled
+ _isFeatureLockDPSEnabledForTests
+ _isFeatureNetworkLinkManagementEnabled
+ _objc_msgSend$_addThreadNetwork:dataset:completion:
+ _objc_msgSend$_addWiFiNetworks:networks:completion:
+ _objc_msgSend$_armFailSafeWithCluster:completion:
+ _objc_msgSend$_commissioningCompleteWithCluster:completion:
+ _objc_msgSend$_connectThreadNetwork:networkID:completion:
+ _objc_msgSend$_createGeneralCommissioningCluster
+ _objc_msgSend$_createThreadNetworkCommissioningCluster
+ _objc_msgSend$_createWiFiNetworkCommissioningCluster
+ _objc_msgSend$_deviceStorageDataSourceForCurrentNode
+ _objc_msgSend$_disarmFailSafeWithCluster:completion:
+ _objc_msgSend$_endPairingMode
+ _objc_msgSend$_enqueueResumeFinalizeAttempt
+ _objc_msgSend$_extractThreadExtendedPANIDFromNetworksAttribute:
+ _objc_msgSend$_extractWiFiSSIDsFromNetworksAttribute:
+ _objc_msgSend$_findAllNetworkCommissioningEndpoints
+ _objc_msgSend$_findNetworkCommissioningEndpointForInterfaceType:
+ _objc_msgSend$_handleAtCapacityWiFiRepair:deviceSSIDs:preferredNetworks:maxNetworks:completion:
+ _objc_msgSend$_hasDualNetworkCommissioningClusters
+ _objc_msgSend$_invalidateFinalizeRetry
+ _objc_msgSend$_makeAccessoryServerFactory
+ _objc_msgSend$_persistThreadWEDInfoToStorage
+ _objc_msgSend$_readCharacteristicValueFromCacheAfterConfirmingBridgedAccessoryReachabilityWithCharacteristic:responseHandler:
+ _objc_msgSend$_removeWiFiNetwork:ssid:completion:
+ _objc_msgSend$_reorderWiFiNetworks:networks:completion:
+ _objc_msgSend$_resumeFinalizePairing
+ _objc_msgSend$_scheduleFinalizeRetry
+ _objc_msgSend$_targetPositionDictionary:fallingBackToCurrentPositionLift:params:
+ _objc_msgSend$_updateDiscoveredAccessoryServersWithNodes:fabricUUID:completion:
+ _objc_msgSend$accessoryNeedsFinalizeResumeForNodeID:fabricUUID:
+ _objc_msgSend$accessoryNetworkCommissioningStateIsReadyForNodeID:fabricUUID:
+ _objc_msgSend$accessoryServerBrowser:getThreadNetworkCredentialsForFabricUUID:requireFullNetworkAttributes:withCompletion:
+ _objc_msgSend$addOrUpdateThreadNetworkWithParams:expectedValues:expectedValueInterval:completionHandler:
+ _objc_msgSend$addOrUpdateWiFiNetworkWithParams:expectedValues:expectedValueInterval:completionHandler:
+ _objc_msgSend$allowsDeferredMatterCommissioningOnThisControllerDevice
+ _objc_msgSend$arrayByAddingObject:
+ _objc_msgSend$connectNetworkWithParams:expectedValues:expectedValueInterval:completion:
+ _objc_msgSend$demoModeStatus
+ _objc_msgSend$discoveredAccessoryServersAsyncMutex
+ _objc_msgSend$eMACAddressOfPairingAccessory
+ _objc_msgSend$extendedPANID
+ _objc_msgSend$finalizeRetryAttempt
+ _objc_msgSend$finalizeRetryTimer
+ _objc_msgSend$generalCommissioningClusterFactory
+ _objc_msgSend$hmf_hexadecimalRepresentation
+ _objc_msgSend$initWithData:
+ _objc_msgSend$initWithWorkQueueFactory:
+ _objc_msgSend$isEnabled
+ _objc_msgSend$lockWithCompletion:
+ _objc_msgSend$locked
+ _objc_msgSend$mapTargetAirPurifierState:
+ _objc_msgSend$markHomeMatterFabricCommissioningDoneWithCompletion:
+ _objc_msgSend$networkCommissioningClusterFactory
+ _objc_msgSend$networkingStatus
+ _objc_msgSend$newQueueWithLabel:attributes:
+ _objc_msgSend$newQueueWithLabel:attributes:target:
+ _objc_msgSend$pendingCompletions
+ _objc_msgSend$pendingReenumerationCompletionHandlers
+ _objc_msgSend$pendingServiceReenumeration
+ _objc_msgSend$readAttributeMaxNetworksWithParams:
+ _objc_msgSend$readAttributePluginCurrentRelativeHumidityWithParams:
+ _objc_msgSend$removeClusterIDForCharacteristic:endpointID:
+ _objc_msgSend$removeNetworkWithParams:expectedValues:expectedValueInterval:completion:
+ _objc_msgSend$removeNode:withPrivilege:fromExistingAclEntries:
+ _objc_msgSend$reorderNetworkWithParams:expectedValues:expectedValueInterval:completion:
+ _objc_msgSend$resetCachedProtocolMapForTesting
+ _objc_msgSend$resumeFinalizeForCommissionedAccessoryWithOnboardingURL:
+ _objc_msgSend$setEMACAddressOfPairingAccessory:
+ _objc_msgSend$setFinalizeRetryAttempt:
+ _objc_msgSend$setFinalizeRetryTimer:
+ _objc_msgSend$setLocked:
+ _objc_msgSend$setNetworkID:
+ _objc_msgSend$setNetworkIndex:
+ _objc_msgSend$setOperationalDataset:
+ _objc_msgSend$setPendingServiceReenumeration:
+ _objc_msgSend$setSsid:
+ _objc_msgSend$shouldBypassOtaTimeWindowFirstTimePairing:
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$subarrayWithRange:
+ _objc_msgSend$suppressDPS
+ _objc_msgSend$unlock
+ _objc_msgSend$updateDiscoveredAccessoryServersWithNodes:fabricUUID:completion:
+ _objc_msgSend$v2FabricDataItemPreferenceComparator
+ _objc_msgSend$workQueueFactory
+ _secondPartyProducts
+ _suppressDpsForDemoMode
+ _suppressDpsForDemoModeForTests
+ defaultFeatures._hmf_once_t9
+ defaultFeatures._hmf_once_v10
+ logCategory._hmf_once_t117
+ logCategory._hmf_once_t1301
+ logCategory._hmf_once_t136
+ logCategory._hmf_once_t180
+ logCategory._hmf_once_t210
+ logCategory._hmf_once_t24
+ logCategory._hmf_once_t32
+ logCategory._hmf_once_t346
+ logCategory._hmf_once_t492
+ logCategory._hmf_once_t50
+ logCategory._hmf_once_t761
+ logCategory._hmf_once_v118
+ logCategory._hmf_once_v1302
+ logCategory._hmf_once_v137
+ logCategory._hmf_once_v181
+ logCategory._hmf_once_v211
+ logCategory._hmf_once_v25
+ logCategory._hmf_once_v33
+ logCategory._hmf_once_v347
+ logCategory._hmf_once_v493
+ logCategory._hmf_once_v51
+ logCategory._hmf_once_v762
+ suppressDpsForDemoMode.onceToken
+ suppressDpsForDemoMode.suppressed
- +[HMMTRProtocolMap mapTargetAirPuriferState:]
- -[HMMTRAccessoryServer _readCharacteristicValueFromCacheAfterConfirmingBridgedAccessroyReachabilityWithCharacteristic:responseHandler:]
- -[HMMTRAccessoryServer removeNode:withPrivilge:fromExistingAclEntries:]
- -[HMMTRAccessoryServerBrowser _updateDiscoveredAccessoryServersWithNodes:fabricUUID:]
- -[HMMTRProtocolMap isRequiresOptionalMatterAttributeForCharacteristic:]
- GCC_except_table1002
- GCC_except_table1066
- GCC_except_table1072
- GCC_except_table1074
- GCC_except_table1196
- GCC_except_table1264
- GCC_except_table1310
- GCC_except_table1318
- GCC_except_table1369
- GCC_except_table1377
- GCC_except_table1414
- GCC_except_table1451
- GCC_except_table1478
- GCC_except_table1674
- GCC_except_table1717
- GCC_except_table1871
- GCC_except_table1872
- GCC_except_table1873
- GCC_except_table1876
- GCC_except_table1897
- GCC_except_table1898
- GCC_except_table1900
- GCC_except_table1903
- GCC_except_table1906
- GCC_except_table1907
- GCC_except_table1908
- GCC_except_table1909
- GCC_except_table1910
- GCC_except_table1911
- GCC_except_table1912
- GCC_except_table1971
- GCC_except_table2065
- GCC_except_table2180
- GCC_except_table2182
- GCC_except_table2212
- GCC_except_table2222
- GCC_except_table2224
- GCC_except_table2280
- GCC_except_table2326
- GCC_except_table2351
- GCC_except_table2422
- GCC_except_table2709
- GCC_except_table2711
- GCC_except_table2713
- GCC_except_table2717
- GCC_except_table2775
- GCC_except_table2854
- GCC_except_table2856
- GCC_except_table2887
- GCC_except_table2888
- GCC_except_table2889
- GCC_except_table2911
- GCC_except_table2912
- GCC_except_table2913
- GCC_except_table2914
- GCC_except_table2915
- GCC_except_table2916
- GCC_except_table2917
- GCC_except_table2918
- GCC_except_table2928
- GCC_except_table2930
- GCC_except_table2941
- GCC_except_table2962
- GCC_except_table2977
- GCC_except_table2983
- GCC_except_table2998
- GCC_except_table3001
- GCC_except_table3005
- GCC_except_table3023
- GCC_except_table3027
- GCC_except_table3029
- GCC_except_table3056
- GCC_except_table3065
- GCC_except_table3070
- GCC_except_table3082
- GCC_except_table3135
- GCC_except_table3136
- GCC_except_table3519
- GCC_except_table3545
- GCC_except_table3546
- GCC_except_table3547
- GCC_except_table3551
- GCC_except_table3557
- GCC_except_table3560
- GCC_except_table3576
- GCC_except_table3591
- GCC_except_table3660
- GCC_except_table3661
- GCC_except_table3690
- GCC_except_table3697
- GCC_except_table3729
- GCC_except_table3733
- GCC_except_table3741
- GCC_except_table3761
- GCC_except_table3764
- GCC_except_table3806
- GCC_except_table3808
- GCC_except_table3810
- GCC_except_table3829
- GCC_except_table3831
- GCC_except_table3852
- GCC_except_table3929
- GCC_except_table3976
- GCC_except_table3996
- GCC_except_table4019
- GCC_except_table4023
- GCC_except_table4038
- GCC_except_table4039
- GCC_except_table4040
- GCC_except_table4046
- GCC_except_table4053
- GCC_except_table4058
- GCC_except_table4095
- GCC_except_table4117
- GCC_except_table4160
- GCC_except_table4166
- GCC_except_table4169
- GCC_except_table4255
- GCC_except_table4256
- GCC_except_table4314
- GCC_except_table4317
- GCC_except_table4381
- GCC_except_table4441
- GCC_except_table4445
- GCC_except_table4451
- GCC_except_table4455
- GCC_except_table4489
- GCC_except_table593
- GCC_except_table599
- GCC_except_table601
- GCC_except_table605
- GCC_except_table762
- GCC_except_table763
- GCC_except_table820
- GCC_except_table821
- GCC_except_table822
- GCC_except_table895
- GCC_except_table937
- GCC_except_table988
- GCC_except_table992
- GCC_except_table994
- GCC_except_table996
- GCC_except_table998
- __139-[HMMTRAccessoryServer scheduleOrExecuteOTAProviderAnnouncement:initiatorType:immediateAnnouncement:endpoint:delayCounter:isUserTriggered:]_block_invoke
- __85-[HMMTRAccessoryServerBrowser _updateDiscoveredAccessoryServersWithNodes:fabricUUID:]_block_invoke
- __OBJC_$_INSTANCE_METHODS_HMMTRAccessoryServer(HAPAccessory|RemoteAccess|Diagnostics|DiagnosticsInternal|SystemCommissionerPairing)
- __OBJC_$_PROP_LIST_HMMTRAccessoryServer
- ___84-[HMMTRAccessoryServerBrowser updateDiscoveredAccessoryServersWithNodes:fabricUUID:]_block_invoke
- ___85-[HMMTRAccessoryServerBrowser _updateDiscoveredAccessoryServersWithNodes:fabricUUID:]_block_invoke
- ___block_descriptor_56_e8_32s40s48s_e17_v16?0"NSArray"8l
- _dispatch_queue_create_with_target$V2
- _objc_msgSend$_readCharacteristicValueFromCacheAfterConfirmingBridgedAccessroyReachabilityWithCharacteristic:responseHandler:
- _objc_msgSend$_updateDiscoveredAccessoryServersWithNodes:fabricUUID:
- _objc_msgSend$accessoryIsUserConfigurationReadyForNodeID:fabricUUID:
- _objc_msgSend$isRequiresOptionalMatterAttributeForCharacteristic:
- _objc_msgSend$mapTargetAirPuriferState:
- _objc_msgSend$removeNode:withPrivilge:fromExistingAclEntries:
- _objc_msgSend$updateDiscoveredAccessoryServersWithNodes:fabricUUID:
- defaultFeatures._hmf_once_t2
- defaultFeatures._hmf_once_v3
- logCategory._hmf_once_t111
- logCategory._hmf_once_t119
- logCategory._hmf_once_t1243
- logCategory._hmf_once_t178
- logCategory._hmf_once_t18
- logCategory._hmf_once_t208
- logCategory._hmf_once_t29
- logCategory._hmf_once_t345
- logCategory._hmf_once_t491
- logCategory._hmf_once_t724
- logCategory._hmf_once_v112
- logCategory._hmf_once_v120
- logCategory._hmf_once_v1244
- logCategory._hmf_once_v179
- logCategory._hmf_once_v19
- logCategory._hmf_once_v209
- logCategory._hmf_once_v30
- logCategory._hmf_once_v346
- logCategory._hmf_once_v492
- logCategory._hmf_once_v725
CStrings:
+ "0000007A-0000-1000-8000-0026BB765291"
+ "101"
+ "45"
+ "<unknown>"
+ "@\"MTRBaseClusterGeneralCommissioning\"16@?0@\"HMMTRAccessoryServer\"8"
+ "@\"MTRClusterAppleAccessoryConnectivityMonitor\"24@?0@\"HMMTRAccessoryServer\"8@\"NSNumber\"16"
+ "@\"MTRClusterNetworkCommissioning\"24@?0@\"HMMTRAccessoryServer\"8Q16"
+ "Accessory for nodeID %@ is not network-commissioning-ready; skipping"
+ "Cannot parse Matter onboarding payload for commissionable-node presence check: %{public}@"
+ "Commissionable-node powered check: discriminator=%{public}@ vendorID=%{public}@ productID=%{public}@ matchingNodePresent=%{public}d (%lu present)"
+ "Connecting pending fabric: %@"
+ "Deferred Matter commissioning not allowed on this controller device; leaving nodeID %@ pending"
+ "Deferred service re-enumeration complete with error domain: %{public}@ code: %ld"
+ "Delegate does not support fabric-scoped Thread credential retrieval"
+ "Door State"
+ "Door Tampered"
+ "Element data array missing from array type %@"
+ "FATAL Error: Failed to generate operational cert for fabric ID %@. error: %@"
+ "Failed to fetch Preferred Thread Credentials from owner, error domain: %{public}@ code: %ld"
+ "Failed to persist HomeMatterFabricCommissioningDone state, error domain: %{public}@ code: %ld"
+ "Failed to persist WED support from commissionee info: %@"
+ "Failed to persist eMAC from commissionee info: %@"
+ "Finalize already complete; skipping resume and releasing exclusive slot"
+ "Finalize failed after Matter commissioning completed; scheduling finalize retry with backoff"
+ "Finalize retry already scheduled; not stacking another"
+ "Finalize retry timer fired; enqueuing resume attempt"
+ "Firmware update connection attempt for an accessory with nodeID %@, error = %@"
+ "FirstTimePairing"
+ "HMMTRAccessoryServerDeferredMatterCommissioningErrorKey"
+ "HMMTRAccessoryServerDeferredMatterCommissioningNodeIDKey"
+ "HMMTRAccessoryServerDidBeginDeferredMatterCommissioningNotification"
+ "HMMTRAccessoryServerDidFailDeferredMatterCommissioningNotification"
+ "Lock acquired"
+ "Lock handed to next waiter (pending=%lu)"
+ "Lock is held; queued waiter (pending=%lu)"
+ "Lock released"
+ "LockDPS"
+ "MTRBaseClusterDoorLock"
+ "Network Repair: ArmFailSafe failed: %@"
+ "Network Repair: ArmFailSafe returned error code: %@"
+ "Network Repair: Arming fail-safe (60s)"
+ "Network Repair: CommissioningComplete failed: %@"
+ "Network Repair: CommissioningComplete returned error code: %@"
+ "Network Repair: CommissioningComplete succeeded"
+ "Network Repair: Device has dual NetworkCommissioning clusters: %@ (WiFi: %@, Thread: %@)"
+ "Network Repair: Disarm fail-safe failed: %@"
+ "Network Repair: Disarm fail-safe returned error code: %@"
+ "Network Repair: Disarming fail-safe (rollback)"
+ "Network Repair: Fail-safe armed"
+ "Network Repair: Failed to read parts list from root endpoint"
+ "Network Repair: Found NetworkCommissioning cluster at endpoint %@ with FeatureMap 0x%lx"
+ "Network Repair: No Matter device available"
+ "Network Repair: No NetworkCommissioning cluster found for interface type 0x%lx"
+ "Network Repair: Sending CommissioningComplete"
+ "NetworkLinkManagement"
+ "No %{public}@ cluster in any of %lu endpoints"
+ "No device storage data source; cannot persist WED info for nodeID %@"
+ "No endpoints available for diagnostic clusters for accessory %{public}@ %{private}@"
+ "Node %@ completed Matter fabric commissioning but not finalize; resuming finalize"
+ "PSK"
+ "Power state changed - state = %lu, goingToSleep: %@"
+ "ProxPairing"
+ "Read color control attribute colorCapabilities supportsColorTempFeature: %@ accessoryRange: [%@ : %@] allowedRange: [%@ : %@]"
+ "Refusing to commission vendor %@ product %@: pairing this accessory is not supported"
+ "RequiresPassword"
+ "Resuming finalize (attempt %lu)"
+ "Resuming finalize for already-commissioned deferred Matter accessory with onboarding URL %{private}@"
+ "SSID"
+ "Scheduling finalize retry #%lu in %.0f seconds"
+ "Skipping resume finalize: accessory server is disabled, has no controller, or the browser has died"
+ "Target Position reported null; falling back to Current Position"
+ "Thread Repair: AddOrUpdateThreadNetwork failed: %@"
+ "Thread Repair: AddOrUpdateThreadNetwork returned status: %@"
+ "Thread Repair: ConnectNetwork failed: %@"
+ "Thread Repair: ConnectNetwork returned status: %@"
+ "Thread Repair: ConnectNetwork with Extended PAN ID: %@"
+ "Thread Repair: Device already on home's Thread network"
+ "Thread Repair: Extended PAN ID mismatch, updating credentials"
+ "Thread Repair: Failed to extract Extended PAN ID from dataset"
+ "Thread Repair: Feature not enabled"
+ "Thread Repair: Found Thread network with Extended PAN ID: %@"
+ "Thread Repair: No Thread network on device, adding home network"
+ "Thread Repair: No operational dataset provided, skipping repair"
+ "Thread Repair: Successfully connected to Thread network"
+ "Thread Repair: Successfully updated Thread network"
+ "Thread StopAccessoryPairing completed, error domain: %{public}@ code: %ld"
+ "Thread credential fabric %{public}@ does not match current browser fabric %{public}@"
+ "Topology is nil"
+ "Tracking fabric with active clients for resumption for fabricUUID: %@"
+ "Unlock called while not locked; ignoring"
+ "WiFi Repair: AddOrUpdateWiFiNetwork failed for '%@': %@"
+ "WiFi Repair: Added network '%@'"
+ "WiFi Repair: Adding %lu missing network(s)"
+ "WiFi Repair: All preferred networks already on device, reordering"
+ "WiFi Repair: At capacity (%lu/%@), removing '%@' to add '%@'"
+ "WiFi Repair: At capacity (%lu/%@), updating %lu existing home network(s)"
+ "WiFi Repair: Capacity limited - adding %lu of %lu missing networks"
+ "WiFi Repair: Device WiFi capacity: %lu current, %@ max"
+ "WiFi Repair: Device at capacity and no primary network available"
+ "WiFi Repair: Failed to add networks: %@"
+ "WiFi Repair: Failed to read MaxNetworks attribute"
+ "WiFi Repair: Failed to remove '%@': %@"
+ "WiFi Repair: Feature not enabled"
+ "WiFi Repair: Found %lu network(s) on device: %@"
+ "WiFi Repair: No preferred networks provided, skipping repair"
+ "WiFi Repair: Reading device network capacity and current networks"
+ "WiFi Repair: ReorderNetwork failed for '%@': %@"
+ "WiFi Repair: Reordering had %lu failures, continuing"
+ "WiFi repair failed: unable to add home network"
+ "WiFi repair failed: unable to remove existing network"
+ "[%{public}@] Accessory for nodeID %@ is not network-commissioning-ready; skipping"
+ "[%{public}@] Cannot parse Matter onboarding payload for commissionable-node presence check: %{public}@"
+ "[%{public}@] Commissionable-node powered check: discriminator=%{public}@ vendorID=%{public}@ productID=%{public}@ matchingNodePresent=%{public}d (%lu present)"
+ "[%{public}@] Connecting pending fabric: %@"
+ "[%{public}@] Deferred Matter commissioning not allowed on this controller device; leaving nodeID %@ pending"
+ "[%{public}@] Deferred service re-enumeration complete with error domain: %{public}@ code: %ld"
+ "[%{public}@] Delegate does not support fabric-scoped Thread credential retrieval"
+ "[%{public}@] Element data array missing from array type %@"
+ "[%{public}@] FATAL Error: Failed to generate operational cert for fabric ID %@. error: %@"
+ "[%{public}@] Failed to fetch Preferred Thread Credentials from owner, error domain: %{public}@ code: %ld"
+ "[%{public}@] Failed to persist HomeMatterFabricCommissioningDone state, error domain: %{public}@ code: %ld"
+ "[%{public}@] Failed to persist WED support from commissionee info: %@"
+ "[%{public}@] Failed to persist eMAC from commissionee info: %@"
+ "[%{public}@] Finalize already complete; skipping resume and releasing exclusive slot"
+ "[%{public}@] Finalize failed after Matter commissioning completed; scheduling finalize retry with backoff"
+ "[%{public}@] Finalize retry already scheduled; not stacking another"
+ "[%{public}@] Finalize retry timer fired; enqueuing resume attempt"
+ "[%{public}@] Firmware update connection attempt for an accessory with nodeID %@, error = %@"
+ "[%{public}@] Lock acquired"
+ "[%{public}@] Lock handed to next waiter (pending=%lu)"
+ "[%{public}@] Lock is held; queued waiter (pending=%lu)"
+ "[%{public}@] Lock released"
+ "[%{public}@] Network Repair: ArmFailSafe failed: %@"
+ "[%{public}@] Network Repair: ArmFailSafe returned error code: %@"
+ "[%{public}@] Network Repair: Arming fail-safe (60s)"
+ "[%{public}@] Network Repair: CommissioningComplete failed: %@"
+ "[%{public}@] Network Repair: CommissioningComplete returned error code: %@"
+ "[%{public}@] Network Repair: CommissioningComplete succeeded"
+ "[%{public}@] Network Repair: Device has dual NetworkCommissioning clusters: %@ (WiFi: %@, Thread: %@)"
+ "[%{public}@] Network Repair: Disarm fail-safe failed: %@"
+ "[%{public}@] Network Repair: Disarm fail-safe returned error code: %@"
+ "[%{public}@] Network Repair: Disarming fail-safe (rollback)"
+ "[%{public}@] Network Repair: Fail-safe armed"
+ "[%{public}@] Network Repair: Failed to read parts list from root endpoint"
+ "[%{public}@] Network Repair: Found NetworkCommissioning cluster at endpoint %@ with FeatureMap 0x%lx"
+ "[%{public}@] Network Repair: No Matter device available"
+ "[%{public}@] Network Repair: No NetworkCommissioning cluster found for interface type 0x%lx"
+ "[%{public}@] Network Repair: Sending CommissioningComplete"
+ "[%{public}@] No %{public}@ cluster in any of %lu endpoints"
+ "[%{public}@] No device storage data source; cannot persist WED info for nodeID %@"
+ "[%{public}@] No endpoints available for diagnostic clusters for accessory %{public}@ %{private}@"
+ "[%{public}@] Node %@ completed Matter fabric commissioning but not finalize; resuming finalize"
+ "[%{public}@] Power state changed - state = %lu, goingToSleep: %@"
+ "[%{public}@] Read color control attribute colorCapabilities supportsColorTempFeature: %@ accessoryRange: [%@ : %@] allowedRange: [%@ : %@]"
+ "[%{public}@] Refusing to commission vendor %@ product %@: pairing this accessory is not supported"
+ "[%{public}@] Resuming finalize (attempt %lu)"
+ "[%{public}@] Resuming finalize for already-commissioned deferred Matter accessory with onboarding URL %{private}@"
+ "[%{public}@] Scheduling finalize retry #%lu in %.0f seconds"
+ "[%{public}@] Skipping resume finalize: accessory server is disabled, has no controller, or the browser has died"
+ "[%{public}@] Target Position reported null; falling back to Current Position"
+ "[%{public}@] Thread Repair: AddOrUpdateThreadNetwork failed: %@"
+ "[%{public}@] Thread Repair: AddOrUpdateThreadNetwork returned status: %@"
+ "[%{public}@] Thread Repair: ConnectNetwork failed: %@"
+ "[%{public}@] Thread Repair: ConnectNetwork returned status: %@"
+ "[%{public}@] Thread Repair: ConnectNetwork with Extended PAN ID: %@"
+ "[%{public}@] Thread Repair: Device already on home's Thread network"
+ "[%{public}@] Thread Repair: Extended PAN ID mismatch, updating credentials"
+ "[%{public}@] Thread Repair: Failed to extract Extended PAN ID from dataset"
+ "[%{public}@] Thread Repair: Feature not enabled"
+ "[%{public}@] Thread Repair: Found Thread network with Extended PAN ID: %@"
+ "[%{public}@] Thread Repair: No Thread network on device, adding home network"
+ "[%{public}@] Thread Repair: No operational dataset provided, skipping repair"
+ "[%{public}@] Thread Repair: Successfully connected to Thread network"
+ "[%{public}@] Thread Repair: Successfully updated Thread network"
+ "[%{public}@] Thread StopAccessoryPairing completed, error domain: %{public}@ code: %ld"
+ "[%{public}@] Thread credential fabric %{public}@ does not match current browser fabric %{public}@"
+ "[%{public}@] Topology is nil"
+ "[%{public}@] Tracking fabric with active clients for resumption for fabricUUID: %@"
+ "[%{public}@] Unlock called while not locked; ignoring"
+ "[%{public}@] WiFi Repair: AddOrUpdateWiFiNetwork failed for '%@': %@"
+ "[%{public}@] WiFi Repair: Added network '%@'"
+ "[%{public}@] WiFi Repair: Adding %lu missing network(s)"
+ "[%{public}@] WiFi Repair: All preferred networks already on device, reordering"
+ "[%{public}@] WiFi Repair: At capacity (%lu/%@), removing '%@' to add '%@'"
+ "[%{public}@] WiFi Repair: At capacity (%lu/%@), updating %lu existing home network(s)"
+ "[%{public}@] WiFi Repair: Capacity limited - adding %lu of %lu missing networks"
+ "[%{public}@] WiFi Repair: Device WiFi capacity: %lu current, %@ max"
+ "[%{public}@] WiFi Repair: Device at capacity and no primary network available"
+ "[%{public}@] WiFi Repair: Failed to add networks: %@"
+ "[%{public}@] WiFi Repair: Failed to read MaxNetworks attribute"
+ "[%{public}@] WiFi Repair: Failed to remove '%@': %@"
+ "[%{public}@] WiFi Repair: Feature not enabled"
+ "[%{public}@] WiFi Repair: Found %lu network(s) on device: %@"
+ "[%{public}@] WiFi Repair: No preferred networks provided, skipping repair"
+ "[%{public}@] WiFi Repair: Reading device network capacity and current networks"
+ "[%{public}@] WiFi Repair: ReorderNetwork failed for '%@': %@"
+ "[%{public}@] WiFi Repair: Reordering had %lu failures, continuing"
+ "[%{public}@] _connectPendingFabricConnectionsForTargetFabricUUID for - %@"
+ "[%{public}@] resumeFinalizeForCommissionedAccessoryWithOnboardingURL called but already resuming; ignoring"
+ "[%{public}@] verifyHAPCharacteristicSupportWithRequiredAttributeValuesAtCHIPEndpoint shortCharacteristicKey = %@, clusterClassName = %@, hapServicesToCheckForRequiredAttributeValues = %@, hapCharacteristicsToCheckForRequiredAttributeValues = %@, curHAPCharacteristicAttributesToCheck = %@"
+ "_connectPendingFabricConnectionsForTargetFabricUUID for - %@"
+ "hmmtr.asyncmutex"
+ "maxNetworks"
+ "networkingStatus"
+ "q24@?0@\"<HMMTRMultiFabricDataStoreQueryV2FabricDataItem>\"8@\"<HMMTRMultiFabricDataStoreQueryV2FabricDataItem>\"16"
+ "readAttributeDoorStateWithCompletion:"
+ "resumeFinalizeForCommissionedAccessoryWithOnboardingURL called but already resuming; ignoring"
+ "v24@?0@\"MTRNetworkCommissioningClusterConnectNetworkResponseParams\"8@\"NSError\"16"
+ "v24@?0@\"MTRNetworkCommissioningClusterNetworkConfigResponseParams\"8@\"NSError\"16"
+ "verifyHAPCharacteristicSupportWithRequiredAttributeValuesAtCHIPEndpoint shortCharacteristicKey = %@, clusterClassName = %@, hapServicesToCheckForRequiredAttributeValues = %@, hapCharacteristicsToCheckForRequiredAttributeValues = %@, curHAPCharacteristicAttributesToCheck = %@"
+ "\xf0\xd2\xf0\xf0\xf0A\xf0\xb1"
- "Accessory for nodeID %@ is not user configuration ready; skipping"
- "Connecting pending fabric fabric: %@"
- "Element data data array missing from array type %@"
- "FATAL Error: Failed to generate ooperational cert for fabric ID %@. error: %@"
- "Firmware update connection attempt for a accessory with nodeID %@, error = %@"
- "No %@ cluster in any endpoints %@."
- "No endpoints available for diagnostic clusters for HAPAccessory: %@"
- "Notifying matter petric pairing step %@"
- "Optional characteristic %@ on endpoint %@ of node %@ requires an additional Optional Matter attribute check"
- "Power state state changed - state = %lu, goingToSleep: %@"
- "Read color control attribute colorCapabilities supportsColorTempFeature: %@ accessoryRange: [%@ : %@]  allowedRange: [%@ : %@]"
- "RequiresOptionalMatterAttribute"
- "Thread StopAccessoryPairing completed, error: %@"
- "Tracking frabic with active clients for resumption for fabricUUID: %@"
- "[%{public}@] Accessory for nodeID %@ is not user configuration ready; skipping"
- "[%{public}@] Connecting pending fabric fabric: %@"
- "[%{public}@] Element data data array missing from array type %@"
- "[%{public}@] FATAL Error: Failed to generate ooperational cert for fabric ID %@. error: %@"
- "[%{public}@] Firmware update connection attempt for a accessory with nodeID %@, error = %@"
- "[%{public}@] No %@ cluster in any endpoints %@."
- "[%{public}@] No endpoints available for diagnostic clusters for HAPAccessory: %@"
- "[%{public}@] Notifying matter petric pairing step %@"
- "[%{public}@] Optional characteristic %@ on endpoint %@ of node %@ requires an additional Optional Matter attribute check"
- "[%{public}@] Power state state changed - state = %lu, goingToSleep: %@"
- "[%{public}@] Read color control attribute colorCapabilities supportsColorTempFeature: %@ accessoryRange: [%@ : %@]  allowedRange: [%@ : %@]"
- "[%{public}@] Thread StopAccessoryPairing completed, error: %@"
- "[%{public}@] Tracking frabic with active clients for resumption for fabricUUID: %@"
- "[%{public}@] _connectPendingFabricConnectionsForTargetFabricUUIDID for - %@"
- "[%{public}@] verifyHAPCharacteristicSupportWithRequiredAttributeValuesAtCHIPEndpoint shortCharacteristicKey = %@, clusterClassName = %@,  hapServicesToCheckForRequiredAttributeValues = %@, hapCharacteristicsToCheckForRequiredAttributeValues = %@, curHAPCharacteristicAttributesToCheck = %@"
- "_connectPendingFabricConnectionsForTargetFabricUUIDID for - %@"
- "verifyHAPCharacteristicSupportWithRequiredAttributeValuesAtCHIPEndpoint shortCharacteristicKey = %@, clusterClassName = %@,  hapServicesToCheckForRequiredAttributeValues = %@, hapCharacteristicsToCheckForRequiredAttributeValues = %@, curHAPCharacteristicAttributesToCheck = %@"
- "\xf0\xd2\xf0\xf0\xf01\xf0a"
```
