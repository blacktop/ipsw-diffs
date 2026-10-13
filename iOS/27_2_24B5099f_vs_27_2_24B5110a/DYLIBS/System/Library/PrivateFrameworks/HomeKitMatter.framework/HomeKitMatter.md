## HomeKitMatter

> `/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter`

```diff

-1520.2.3.0.2
-  __TEXT.__text: 0x1815fc
-  __TEXT.__objc_methlist: 0xaf1c
+1520.2.7.1.3
+  __TEXT.__text: 0x1896c0
+  __TEXT.__objc_methlist: 0xb0cc
   __TEXT.__const: 0x2c8
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__gcc_except_tab: 0x30b0
-  __TEXT.__cstring: 0x704f
-  __TEXT.__oslogstring: 0x50502
+  __TEXT.__gcc_except_tab: 0x3414
+  __TEXT.__cstring: 0x730a
+  __TEXT.__oslogstring: 0x51beb
   __TEXT.__ustring: 0x68
-  __TEXT.__unwind_info: 0x3d28
+  __TEXT.__unwind_info: 0x3e88
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4938
+  __DATA_CONST.__const: 0x4ba8
   __DATA_CONST.__objc_classlist: 0x460
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x71c8
+  __DATA_CONST.__objc_selrefs: 0x7360
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x318
-  __DATA_CONST.__objc_arraydata: 0x240
-  __DATA_CONST.__got: 0xa08
-  __AUTH_CONST.__const: 0x1180
-  __AUTH_CONST.__cfstring: 0x6ee0
-  __AUTH_CONST.__objc_const: 0x10640
-  __AUTH_CONST.__objc_intobj: 0x1740
-  __AUTH_CONST.__objc_arrayobj: 0x168
+  __DATA_CONST.__objc_arraydata: 0x250
+  __DATA_CONST.__got: 0xa48
+  __AUTH_CONST.__const: 0x1200
+  __AUTH_CONST.__cfstring: 0x70a0
+  __AUTH_CONST.__objc_const: 0x106e0
+  __AUTH_CONST.__objc_intobj: 0x1830
+  __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1ea0
-  __DATA.__objc_ivar: 0xbac
+  __DATA.__objc_ivar: 0xbb8
   __DATA.__data: 0xea0
   __DATA_DIRTY.__objc_data: 0xd20
   __DATA_DIRTY.__bss: 0xb0

   - /System/Library/PrivateFrameworks/UARPKit.framework/UARPKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4537
-  Symbols:   7430
-  CStrings:  5832
+  Functions: 4607
+  Symbols:   7533
+  CStrings:  5951
 
Symbols:
+ +[HMMTRFeatures disableDemoModeSuppressDPSForTests]
+ +[HMMTRFeatures disableFeatureLockDPSForTests]
+ +[HMMTRFeatures enableDemoModeSuppressDPSForTests]
+ +[HMMTRFeatures enableFeatureLockDPSForTests]
+ +[HMMTRFeatures unsetDemoModeSuppressDPSForTests]
+ +[HMMTRFeatures unsetFeatureLockDPSForTests]
+ -[HMMTRAccessoryServer connectivityMonitorClusterFactory]
+ -[HMMTRAccessoryServer generalCommissioningClusterFactory]
+ -[HMMTRAccessoryServer networkCommissioningClusterFactory]
+ -[HMMTRAccessoryServer removeClusterIDForCharacteristic:endpointID:]
+ -[HMMTRAccessoryServer setConnectivityMonitorClusterFactory:]
+ -[HMMTRAccessoryServer setGeneralCommissioningClusterFactory:]
+ -[HMMTRAccessoryServer setNetworkCommissioningClusterFactory:]
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
+ -[HMMTRSyncClusterThermostat readAttributePluginCurrentRelativeHumidityWithParams:]
+ -[HMMTRSyncClusterThermostat updatedValuePluginCurrentRelativeHumidityForAttributeReport:responseHandler:]
+ GCC_except_table1058
+ GCC_except_table1064
+ GCC_except_table1186
+ GCC_except_table1246
+ GCC_except_table1292
+ GCC_except_table1300
+ GCC_except_table1351
+ GCC_except_table1359
+ GCC_except_table1396
+ GCC_except_table1434
+ GCC_except_table1461
+ GCC_except_table1658
+ GCC_except_table1699
+ GCC_except_table1852
+ GCC_except_table1853
+ GCC_except_table1856
+ GCC_except_table1879
+ GCC_except_table1880
+ GCC_except_table1883
+ GCC_except_table1891
+ GCC_except_table1892
+ GCC_except_table1903
+ GCC_except_table1905
+ GCC_except_table1906
+ GCC_except_table1907
+ GCC_except_table1915
+ GCC_except_table1920
+ GCC_except_table1923
+ GCC_except_table1925
+ GCC_except_table1927
+ GCC_except_table1928
+ GCC_except_table1930
+ GCC_except_table1997
+ GCC_except_table2003
+ GCC_except_table2041
+ GCC_except_table2124
+ GCC_except_table2242
+ GCC_except_table2244
+ GCC_except_table2275
+ GCC_except_table2284
+ GCC_except_table2286
+ GCC_except_table2335
+ GCC_except_table2372
+ GCC_except_table2396
+ GCC_except_table2462
+ GCC_except_table2751
+ GCC_except_table2753
+ GCC_except_table2755
+ GCC_except_table2759
+ GCC_except_table2820
+ GCC_except_table2861
+ GCC_except_table2941
+ GCC_except_table2942
+ GCC_except_table2943
+ GCC_except_table2965
+ GCC_except_table2966
+ GCC_except_table2967
+ GCC_except_table2968
+ GCC_except_table2969
+ GCC_except_table2970
+ GCC_except_table2972
+ GCC_except_table2982
+ GCC_except_table2984
+ GCC_except_table2996
+ GCC_except_table3031
+ GCC_except_table3037
+ GCC_except_table3050
+ GCC_except_table3053
+ GCC_except_table3057
+ GCC_except_table3072
+ GCC_except_table3075
+ GCC_except_table3079
+ GCC_except_table3081
+ GCC_except_table3111
+ GCC_except_table3120
+ GCC_except_table3125
+ GCC_except_table3137
+ GCC_except_table3189
+ GCC_except_table3190
+ GCC_except_table3586
+ GCC_except_table3611
+ GCC_except_table3612
+ GCC_except_table3613
+ GCC_except_table3617
+ GCC_except_table3622
+ GCC_except_table3625
+ GCC_except_table3641
+ GCC_except_table3656
+ GCC_except_table3725
+ GCC_except_table3733
+ GCC_except_table3735
+ GCC_except_table3742
+ GCC_except_table3743
+ GCC_except_table3776
+ GCC_except_table3785
+ GCC_except_table3789
+ GCC_except_table3823
+ GCC_except_table3826
+ GCC_except_table3834
+ GCC_except_table3860
+ GCC_except_table3899
+ GCC_except_table3901
+ GCC_except_table3903
+ GCC_except_table3920
+ GCC_except_table3922
+ GCC_except_table3940
+ GCC_except_table4017
+ GCC_except_table4064
+ GCC_except_table4082
+ GCC_except_table4105
+ GCC_except_table4109
+ GCC_except_table4124
+ GCC_except_table4125
+ GCC_except_table4126
+ GCC_except_table4132
+ GCC_except_table4139
+ GCC_except_table4144
+ GCC_except_table4199
+ GCC_except_table4221
+ GCC_except_table4267
+ GCC_except_table4272
+ GCC_except_table4275
+ GCC_except_table4359
+ GCC_except_table4360
+ GCC_except_table4416
+ GCC_except_table4419
+ GCC_except_table4543
+ GCC_except_table4547
+ GCC_except_table4551
+ GCC_except_table4554
+ GCC_except_table4587
+ GCC_except_table995
+ _AppleExtensionNeedsAdditionalConfigurationAttribute
+ _OBJC_CLASS_$_HMHomeManager
+ _OBJC_CLASS_$_MTRClusterAppleAccessoryConnectivityMonitor
+ _OBJC_CLASS_$_MTRNetworkCommissioningClusterAddOrUpdateThreadNetworkParams
+ _OBJC_CLASS_$_MTRNetworkCommissioningClusterAddOrUpdateWiFiNetworkParams
+ _OBJC_CLASS_$_MTRNetworkCommissioningClusterConnectNetworkParams
+ _OBJC_CLASS_$_MTRNetworkCommissioningClusterRemoveNetworkParams
+ _OBJC_CLASS_$_MTRNetworkCommissioningClusterReorderNetworkParams
+ _OBJC_IVAR_$_HMMTRAccessoryServer._connectivityMonitorClusterFactory
+ _OBJC_IVAR_$_HMMTRAccessoryServer._generalCommissioningClusterFactory
+ _OBJC_IVAR_$_HMMTRAccessoryServer._networkCommissioningClusterFactory
+ __OBJC_$_INSTANCE_METHODS_HMMTRAccessoryServer(HAPAccessory|RemoteAccess|Diagnostics|DiagnosticsInternal|SystemCommissionerPairing|NetworkRepair)
+ ___120-[HMMTRAccessoryServer(NetworkRepair) _handleAtCapacityWiFiRepair:deviceSSIDs:preferredNetworks:maxNetworks:completion:]_block_invoke
+ ___49-[HMMTRAccessoryServer initWithKeystore:browser:]_block_invoke_2
+ ___49-[HMMTRAccessoryServer initWithKeystore:browser:]_block_invoke_3
+ ___73-[HMMTRAccessoryServer(Diagnostics) supportsEnhancedMetricsForAccessory:]_block_invoke
+ ___74-[HMMTRAccessoryServer(NetworkRepair) _armFailSafeWithCluster:completion:]_block_invoke
+ ___74-[HMMTRAccessoryServer(NetworkRepair) _removeWiFiNetwork:ssid:completion:]_block_invoke
+ ___76-[HMMTRAccessoryServer(NetworkRepair) _addThreadNetwork:dataset:completion:]_block_invoke
+ ___76-[HMMTRAccessoryServer(NetworkRepair) _addWiFiNetworks:networks:completion:]_block_invoke
+ ___77-[HMMTRAccessoryServer(NetworkRepair) _disarmFailSafeWithCluster:completion:]_block_invoke
+ ___80-[HMMTRAccessoryServer(NetworkRepair) _reorderWiFiNetworks:networks:completion:]_block_invoke
+ ___82-[HMMTRAccessoryServer(NetworkRepair) _connectThreadNetwork:networkID:completion:]_block_invoke
+ ___82-[HMMTRAccessoryServer(NetworkRepair) repairWiFiNetworkWithCompletion:completion:]_block_invoke
+ ___82-[HMMTRAccessoryServer(NetworkRepair) repairWiFiNetworkWithCompletion:completion:]_block_invoke_2
+ ___82-[HMMTRAccessoryServer(NetworkRepair) repairWiFiNetworkWithCompletion:completion:]_block_invoke_3
+ ___84-[HMMTRAccessoryServer(NetworkRepair) _commissioningCompleteWithCluster:completion:]_block_invoke
+ ___84-[HMMTRAccessoryServer(NetworkRepair) repairThreadNetworkWithCompletion:completion:]_block_invoke
+ ___84-[HMMTRAccessoryServer(NetworkRepair) repairThreadNetworkWithCompletion:completion:]_block_invoke_2
+ ___84-[HMMTRAccessoryServer(NetworkRepair) repairThreadNetworkWithCompletion:completion:]_block_invoke_3
+ ___84-[HMMTRAccessoryServer(NetworkRepair) repairThreadNetworkWithCompletion:completion:]_block_invoke_4
+ ___84-[HMMTRAccessoryServer(NetworkRepair) repairThreadNetworkWithCompletion:completion:]_block_invoke_5
+ ___block_descriptor_104_e8_32s40s48s56s64s72bs80bs88w_e17_v16?0"NSError"8lw88l8s72l8s32l8s40l8s48l8s56l8s80l8s64l8
+ ___block_descriptor_32_e65_"MTRClusterNetworkCommissioning"24?0"HMMTRAccessoryServer"8Q16l
+ ___block_descriptor_32_e66_"MTRBaseClusterGeneralCommissioning"16?0"HMMTRAccessoryServer"8l
+ ___block_descriptor_32_e88_"MTRClusterAppleAccessoryConnectivityMonitor"24?0"HMMTRAccessoryServer"8"NSNumber"16l
+ ___block_descriptor_40_e8_32bs_e79_v24?0"MTRNetworkCommissioningClusterNetworkConfigResponseParams"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32bs40w_e79_v24?0"MTRNetworkCommissioningClusterNetworkConfigResponseParams"8"NSError"16lw40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e80_v24?0"MTRNetworkCommissioningClusterConnectNetworkResponseParams"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e87_v24?0"MTRGeneralCommissioningClusterCommissioningCompleteResponseParams"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32bs40r48r_e5_v8?0ls32l8r40l8r48l8
+ ___block_descriptor_56_e8_32bs40r48w_e5_v8?0lw48l8r40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48w_e17_v16?0"NSError"8lw48l8s40l8s32l8
+ ___block_descriptor_64_e8_32s40s48bs56w_e17_v16?0"NSError"8lw56l8s48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48r56r64w_e79_v24?0"MTRNetworkCommissioningClusterNetworkConfigResponseParams"8"NSError"16lw64l8r48l8r56l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56bs64w_e17_v16?0"NSError"8lw64l8s56l8s32l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48r56r64r72w_e79_v24?0"MTRNetworkCommissioningClusterNetworkConfigResponseParams"8"NSError"16lw72l8r48l8r56l8s32l8r64l8s40l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs72w_e17_v16?0"NSError"8lw72l8s64l8s32l8s40l8s48l8s56l8
+ ___suppressDpsForDemoMode_block_invoke
+ __dispatch_main_q
+ _isFeatureLockDPSEnabled
+ _isFeatureLockDPSEnabledForTests
+ _isFeatureNetworkLinkManagementEnabled
+ _logCategory._hmf_once_t210
+ _logCategory._hmf_once_v211
+ _suppressDpsForDemoMode
+ _suppressDpsForDemoMode.onceToken
+ _suppressDpsForDemoMode.suppressed
+ _suppressDpsForDemoModeForTests
- GCC_except_table1056
- GCC_except_table1060
- GCC_except_table1184
- GCC_except_table1244
- GCC_except_table1290
- GCC_except_table1298
- GCC_except_table1349
- GCC_except_table1357
- GCC_except_table1394
- GCC_except_table1432
- GCC_except_table1459
- GCC_except_table1656
- GCC_except_table1697
- GCC_except_table1849
- GCC_except_table1850
- GCC_except_table1854
- GCC_except_table1874
- GCC_except_table1875
- GCC_except_table1881
- GCC_except_table1884
- GCC_except_table1885
- GCC_except_table1949
- GCC_except_table1955
- GCC_except_table1993
- GCC_except_table2076
- GCC_except_table2192
- GCC_except_table2194
- GCC_except_table2225
- GCC_except_table2234
- GCC_except_table2236
- GCC_except_table2285
- GCC_except_table2322
- GCC_except_table2346
- GCC_except_table2412
- GCC_except_table2691
- GCC_except_table2693
- GCC_except_table2695
- GCC_except_table2699
- GCC_except_table2760
- GCC_except_table2801
- GCC_except_table2848
- GCC_except_table2850
- GCC_except_table2881
- GCC_except_table2882
- GCC_except_table2883
- GCC_except_table2905
- GCC_except_table2906
- GCC_except_table2907
- GCC_except_table2909
- GCC_except_table2911
- GCC_except_table2912
- GCC_except_table2922
- GCC_except_table2924
- GCC_except_table2936
- GCC_except_table2955
- GCC_except_table2977
- GCC_except_table2990
- GCC_except_table2993
- GCC_except_table2997
- GCC_except_table3012
- GCC_except_table3019
- GCC_except_table3021
- GCC_except_table3051
- GCC_except_table3060
- GCC_except_table3065
- GCC_except_table3077
- GCC_except_table3129
- GCC_except_table3130
- GCC_except_table3520
- GCC_except_table3545
- GCC_except_table3546
- GCC_except_table3547
- GCC_except_table3551
- GCC_except_table3556
- GCC_except_table3559
- GCC_except_table3575
- GCC_except_table3590
- GCC_except_table3659
- GCC_except_table3667
- GCC_except_table3669
- GCC_except_table3676
- GCC_except_table3677
- GCC_except_table3710
- GCC_except_table3719
- GCC_except_table3723
- GCC_except_table3757
- GCC_except_table3760
- GCC_except_table3768
- GCC_except_table3790
- GCC_except_table3794
- GCC_except_table3833
- GCC_except_table3835
- GCC_except_table3837
- GCC_except_table3854
- GCC_except_table3874
- GCC_except_table3951
- GCC_except_table3998
- GCC_except_table4016
- GCC_except_table4039
- GCC_except_table4043
- GCC_except_table4058
- GCC_except_table4059
- GCC_except_table4060
- GCC_except_table4066
- GCC_except_table4073
- GCC_except_table4078
- GCC_except_table4133
- GCC_except_table4155
- GCC_except_table4197
- GCC_except_table4202
- GCC_except_table4205
- GCC_except_table4289
- GCC_except_table4290
- GCC_except_table4346
- GCC_except_table4349
- GCC_except_table4411
- GCC_except_table4473
- GCC_except_table4477
- GCC_except_table4484
- GCC_except_table4517
- __OBJC_$_INSTANCE_METHODS_HMMTRAccessoryServer(HAPAccessory|RemoteAccess|Diagnostics|DiagnosticsInternal|SystemCommissionerPairing)
- __OBJC_$_PROP_LIST_HMMTRAccessoryServer
- _logCategory._hmf_once_t208
- _logCategory._hmf_once_v209
CStrings:
+ "0000007A-0000-1000-8000-0026BB765291"
+ "101"
+ "45"
+ "@\"MTRBaseClusterGeneralCommissioning\"16@?0@\"HMMTRAccessoryServer\"8"
+ "@\"MTRClusterAppleAccessoryConnectivityMonitor\"24@?0@\"HMMTRAccessoryServer\"8@\"NSNumber\"16"
+ "@\"MTRClusterNetworkCommissioning\"24@?0@\"HMMTRAccessoryServer\"8Q16"
+ "Door State"
+ "Door Tampered"
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
+ "PSK"
+ "RequiresPassword"
+ "SSID"
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
+ "Topology is nil"
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
+ "[%{public}@] Topology is nil"
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
+ "maxNetworks"
+ "networkingStatus"
+ "readAttributeDoorStateWithCompletion:"
+ "v24@?0@\"MTRNetworkCommissioningClusterConnectNetworkResponseParams\"8@\"NSError\"16"
+ "v24@?0@\"MTRNetworkCommissioningClusterNetworkConfigResponseParams\"8@\"NSError\"16"
+ "\xf0\xd2\xf0\xf0\xf0A\xf0\xb1"
- "\xf0\xd2\xf0\xf0\xf0A\xf0\x81"
```
