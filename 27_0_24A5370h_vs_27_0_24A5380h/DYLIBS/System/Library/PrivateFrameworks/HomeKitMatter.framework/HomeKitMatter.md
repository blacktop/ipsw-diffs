## HomeKitMatter

> `/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter`

```diff

-  __TEXT.__text: 0x186be8
-  __TEXT.__objc_methlist: 0xadc4
+  __TEXT.__text: 0x1815cc
+  __TEXT.__objc_methlist: 0xad0c
   __TEXT.__const: 0x298
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__gcc_except_tab: 0x3150
-  __TEXT.__cstring: 0x7103
-  __TEXT.__oslogstring: 0x508b3
+  __TEXT.__gcc_except_tab: 0x302c
+  __TEXT.__cstring: 0x6e9e
+  __TEXT.__oslogstring: 0x4f5a5
   __TEXT.__ustring: 0x68
-  __TEXT.__unwind_info: 0x3178
+  __TEXT.__unwind_info: 0x3140
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x49c8
+  __DATA_CONST.__const: 0x48f0
   __DATA_CONST.__objc_classlist: 0x458
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x71f0
+  __DATA_CONST.__objc_selrefs: 0x7098
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x318
-  __DATA_CONST.__objc_arraydata: 0x248
-  __DATA_CONST.__got: 0xa08
+  __DATA_CONST.__objc_superrefs: 0x310
+  __DATA_CONST.__objc_arraydata: 0x240
+  __DATA_CONST.__got: 0x9f8
   __AUTH_CONST.__const: 0x1140
-  __AUTH_CONST.__cfstring: 0x7060
-  __AUTH_CONST.__objc_const: 0x10318
-  __AUTH_CONST.__objc_intobj: 0x1788
-  __AUTH_CONST.__objc_arrayobj: 0x180
+  __AUTH_CONST.__cfstring: 0x6ce0
+  __AUTH_CONST.__objc_const: 0x10238
+  __AUTH_CONST.__objc_intobj: 0x1740
+  __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x1ef0
-  __DATA.__objc_ivar: 0xb78
+  __AUTH.__objc_data: 0x1e50
+  __DATA.__objc_ivar: 0xb64
   __DATA.__data: 0xea0
-  __DATA.__bss: 0x4c8
-  __DATA_DIRTY.__objc_data: 0xc80
-  __DATA_DIRTY.__bss: 0x88
+  __DATA.__bss: 0x478
+  __DATA_DIRTY.__objc_data: 0xd20
+  __DATA_DIRTY.__bss: 0xd8
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/UARPKit.framework/UARPKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4494
-  Symbols:   15495
-  CStrings:  6783
+  Functions: 4477
+  Symbols:   15383
+  CStrings:  6643
 
Sections:
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __DATA.__data : content changed
Symbols:
+ +[HMMTRBeaconProtectionKey bpkFromMatterFabricRawIPK:compressedFabricId:error:]
+ +[HMMTRBeaconProtectionKey compressedFabricIdFromRootPublicKey:fabricID:error:]
+ -[HMMTRAccessoryServer startBusyImageResponseTimer:timeInterval:requestParams:queue:]
+ -[HMMTRAccessoryServer startOtaProviderSchedulerTimer:queue:]
+ -[HMMTRAccessoryServerBrowser _cancelBonjourBrowser]
+ -[HMMTRAccessoryServerBrowser _filterAccessoryServersUnpairedFromStorageAmongServers:completion:]
+ -[HMMTRAccessoryServerBrowser _reconcileBonjourBrowser]
+ -[HMMTRAccessoryServerBrowser preWarmCommissioningSession]
+ -[HMMTRAccessoryServerBrowser replayPresentCommissionableNodeDiscriminatorsToServer:]
+ -[HMMTRAccessoryServerBrowserDataSourceDefault makeAttestationDataStoreWithURL:]
+ -[HMMTRAnnounceOtaSchedulerTimer init:server:queue:]
+ -[HMMTROTAAnnounceTimer initWithServer:nodeId:queue:]
+ -[HMMTRQueryImageResponseBusyTimer initWithServer:softwareUpdateProvider:timeInterval:requestParams:queue:]
+ GCC_except_table1041
+ GCC_except_table1045
+ GCC_except_table1047
+ GCC_except_table1169
+ GCC_except_table1229
+ GCC_except_table1275
+ GCC_except_table1283
+ GCC_except_table1332
+ GCC_except_table1340
+ GCC_except_table1377
+ GCC_except_table1414
+ GCC_except_table1441
+ GCC_except_table1635
+ GCC_except_table1676
+ GCC_except_table1828
+ GCC_except_table1829
+ GCC_except_table1830
+ GCC_except_table1833
+ GCC_except_table1855
+ GCC_except_table1856
+ GCC_except_table1860
+ GCC_except_table1863
+ GCC_except_table1864
+ GCC_except_table1865
+ GCC_except_table1866
+ GCC_except_table1867
+ GCC_except_table1868
+ GCC_except_table1869
+ GCC_except_table1928
+ GCC_except_table1934
+ GCC_except_table1972
+ GCC_except_table2055
+ GCC_except_table2168
+ GCC_except_table2170
+ GCC_except_table2200
+ GCC_except_table2208
+ GCC_except_table2210
+ GCC_except_table2259
+ GCC_except_table2296
+ GCC_except_table2385
+ GCC_except_table2662
+ GCC_except_table2664
+ GCC_except_table2666
+ GCC_except_table2670
+ GCC_except_table2728
+ GCC_except_table2769
+ GCC_except_table2815
+ GCC_except_table2817
+ GCC_except_table2848
+ GCC_except_table2849
+ GCC_except_table2850
+ GCC_except_table2872
+ GCC_except_table2873
+ GCC_except_table2874
+ GCC_except_table2875
+ GCC_except_table2876
+ GCC_except_table2877
+ GCC_except_table2878
+ GCC_except_table2879
+ GCC_except_table2889
+ GCC_except_table2902
+ GCC_except_table2921
+ GCC_except_table2937
+ GCC_except_table2943
+ GCC_except_table2956
+ GCC_except_table2959
+ GCC_except_table2963
+ GCC_except_table2978
+ GCC_except_table2985
+ GCC_except_table2987
+ GCC_except_table3014
+ GCC_except_table3023
+ GCC_except_table3028
+ GCC_except_table3040
+ GCC_except_table3091
+ GCC_except_table3092
+ GCC_except_table3475
+ GCC_except_table3500
+ GCC_except_table3501
+ GCC_except_table3502
+ GCC_except_table3506
+ GCC_except_table3511
+ GCC_except_table3514
+ GCC_except_table3545
+ GCC_except_table3614
+ GCC_except_table3622
+ GCC_except_table3624
+ GCC_except_table3632
+ GCC_except_table3661
+ GCC_except_table3668
+ GCC_except_table3700
+ GCC_except_table3703
+ GCC_except_table3711
+ GCC_except_table3731
+ GCC_except_table3734
+ GCC_except_table3772
+ GCC_except_table3774
+ GCC_except_table3776
+ GCC_except_table3795
+ GCC_except_table3813
+ GCC_except_table3890
+ GCC_except_table3937
+ GCC_except_table3955
+ GCC_except_table3978
+ GCC_except_table3982
+ GCC_except_table3997
+ GCC_except_table3998
+ GCC_except_table4005
+ GCC_except_table4012
+ GCC_except_table4017
+ GCC_except_table4072
+ GCC_except_table4094
+ GCC_except_table4137
+ GCC_except_table4142
+ GCC_except_table4145
+ GCC_except_table4229
+ GCC_except_table4230
+ GCC_except_table4286
+ GCC_except_table4289
+ GCC_except_table4351
+ GCC_except_table4413
+ GCC_except_table4417
+ GCC_except_table4421
+ GCC_except_table4424
+ GCC_except_table4457
+ GCC_except_table872
+ GCC_except_table963
+ GCC_except_table967
+ GCC_except_table969
+ GCC_except_table971
+ GCC_except_table973
+ _HMMTRShouldSelectCategory
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_HAPECDSAKeyPairVerifySession
+ _OBJC_CLASS_$_HMMTRBeaconProtectionKey
+ _OBJC_METACLASS_$_HMMTRBeaconProtectionKey
+ __OBJC_$_CLASS_METHODS_HMMTRBeaconProtectionKey
+ __OBJC_CLASS_RO_$_HMMTRBeaconProtectionKey
+ __OBJC_METACLASS_RO_$_HMMTRBeaconProtectionKey
+ ___85-[HMMTRAccessoryServerBrowser _updateDiscoveredAccessoryServersWithNodes:fabricUUID:]_block_invoke_2
+ ___85-[HMMTRAccessoryServerBrowser replayPresentCommissionableNodeDiscriminatorsToServer:]_block_invoke
+ ___97-[HMMTRAccessoryServerBrowser _filterAccessoryServersUnpairedFromStorageAmongServers:completion:]_block_invoke
+ ___97-[HMMTRAccessoryServerBrowser _filterAccessoryServersUnpairedFromStorageAmongServers:completion:]_block_invoke_2
+ ___block_descriptor_56_e8_32s40s48s_e17_v16?0"NSArray"8ls32l8s40l8s48l8
+ _kDefaultOtaProviderEndpoint
+ _logCategory._hmf_once_t1361
+ _logCategory._hmf_once_v1362
+ _objc_msgSend$_cancelBonjourBrowser
+ _objc_msgSend$_filterAccessoryServersUnpairedFromStorageAmongServers:completion:
+ _objc_msgSend$_reconcileBonjourBrowser
+ _objc_msgSend$bpkFromTLK:error:
+ _objc_msgSend$hkdfSHA256DeriveKeyFromIKM:salt:info:outputByteCount:error:
+ _objc_msgSend$init:server:queue:
+ _objc_msgSend$initWithServer:softwareUpdateProvider:timeInterval:requestParams:queue:
+ _objc_msgSend$makeAttestationDataStoreWithURL:
+ _objc_msgSend$replayPresentCommissionableNodeDiscriminatorsToServer:
+ _objc_msgSend$startOtaProviderSchedulerTimer:queue:
+ _objc_msgSend$subdataWithRange:
+ _objc_msgSend$tlkFromIKM:error:
- -[HMMTRAccessoryServer diagnosticsEventDelegate]
- -[HMMTRAccessoryServer setDiagnosticsEventDelegate:]
- -[HMMTRAccessoryServer setDiagnosticsEventHandler:]
- -[HMMTRAccessoryServer startBusyImageResponseTimer:timeInterval:endpoint:requestParams:queue:]
- -[HMMTRAccessoryServer startOtaProviderSchedulerTimer:endpoint:queue:]
- -[HMMTRAccessoryServer(Diagnostics) _processEvent:]
- -[HMMTRAccessoryServer(Diagnostics) _readPastEventsFromAccessory:forClusters:]
- -[HMMTRAccessoryServer(Diagnostics) collectDiagnosticsForAccessory:]
- -[HMMTRAccessoryServer(Diagnostics) errorCountOfThreadNetworkDiagnostics:]
- -[HMMTRAccessoryServer(Diagnostics) errorCountOfWiFiNetworkDiagnostics:]
- -[HMMTRAccessoryServer(Diagnostics) packetCountOfThreadNetworkDiagnostics:]
- -[HMMTRAccessoryServer(Diagnostics) packetCountOfWiFiNetworkDiagnostics:]
- -[HMMTRAccessoryServer(Diagnostics) readPastDiagnosticEventsFromAccessory:fromEventNumber:]
- -[HMMTRAccessoryServer(Diagnostics) resetThreadNetworkDiagnosticsCountForAccessory:]
- -[HMMTRAccessoryServer(Diagnostics) resetWiFiNetworkDiagnosticsCountForAccessory:]
- -[HMMTRAccessoryServer(DiagnosticsInternal) _handleDiagnosticsEvent:]
- -[HMMTRAccessoryServerBrowser _preWarmCommissioningSession]
- -[HMMTRAccessoryServerDiagnosticsEvent .cxx_destruct]
- -[HMMTRAccessoryServerDiagnosticsEvent initWithValues:]
- -[HMMTRAccessoryServerDiagnosticsEvent values]
- -[HMMTRAnnounceOtaSchedulerTimer endpoint]
- -[HMMTRAnnounceOtaSchedulerTimer init:server:endpoint:queue:]
- -[HMMTRAnnounceOtaSchedulerTimer setEndpoint:]
- -[HMMTROTAAnnounceTimer endpoint]
- -[HMMTROTAAnnounceTimer initWithServer:nodeId:endpoint:queue:]
- -[HMMTROTAAnnounceTimer setEndpoint:]
- -[HMMTRQueryImageResponseBusyTimer endpoint]
- -[HMMTRQueryImageResponseBusyTimer initWithServer:softwareUpdateProvider:timeInterval:endpoint:requestParams:queue:]
- -[HMMTRQueryImageResponseBusyTimer setEndpoint:]
- GCC_except_table1061
- GCC_except_table1065
- GCC_except_table1067
- GCC_except_table1191
- GCC_except_table1251
- GCC_except_table1297
- GCC_except_table1305
- GCC_except_table1354
- GCC_except_table1362
- GCC_except_table1399
- GCC_except_table1436
- GCC_except_table1465
- GCC_except_table1659
- GCC_except_table1700
- GCC_except_table1852
- GCC_except_table1877
- GCC_except_table1878
- GCC_except_table1879
- GCC_except_table1880
- GCC_except_table1881
- GCC_except_table1884
- GCC_except_table1887
- GCC_except_table1888
- GCC_except_table1889
- GCC_except_table1890
- GCC_except_table1891
- GCC_except_table1892
- GCC_except_table1893
- GCC_except_table1952
- GCC_except_table1958
- GCC_except_table1996
- GCC_except_table2079
- GCC_except_table2192
- GCC_except_table2194
- GCC_except_table2224
- GCC_except_table2232
- GCC_except_table2234
- GCC_except_table2283
- GCC_except_table2343
- GCC_except_table2408
- GCC_except_table2684
- GCC_except_table2686
- GCC_except_table2688
- GCC_except_table2692
- GCC_except_table2750
- GCC_except_table2791
- GCC_except_table2833
- GCC_except_table2835
- GCC_except_table2866
- GCC_except_table2867
- GCC_except_table2868
- GCC_except_table2890
- GCC_except_table2892
- GCC_except_table2893
- GCC_except_table2894
- GCC_except_table2895
- GCC_except_table2896
- GCC_except_table2897
- GCC_except_table2907
- GCC_except_table2909
- GCC_except_table2920
- GCC_except_table2939
- GCC_except_table2955
- GCC_except_table2961
- GCC_except_table2974
- GCC_except_table2977
- GCC_except_table2996
- GCC_except_table2999
- GCC_except_table3003
- GCC_except_table3005
- GCC_except_table3030
- GCC_except_table3037
- GCC_except_table3042
- GCC_except_table3054
- GCC_except_table3105
- GCC_except_table3106
- GCC_except_table3491
- GCC_except_table3516
- GCC_except_table3517
- GCC_except_table3518
- GCC_except_table3522
- GCC_except_table3527
- GCC_except_table3546
- GCC_except_table3561
- GCC_except_table3639
- GCC_except_table3641
- GCC_except_table3648
- GCC_except_table3649
- GCC_except_table3678
- GCC_except_table3685
- GCC_except_table3717
- GCC_except_table3720
- GCC_except_table3728
- GCC_except_table3748
- GCC_except_table3751
- GCC_except_table3789
- GCC_except_table3791
- GCC_except_table3810
- GCC_except_table3812
- GCC_except_table3830
- GCC_except_table3907
- GCC_except_table3954
- GCC_except_table3972
- GCC_except_table3995
- GCC_except_table4014
- GCC_except_table4015
- GCC_except_table4016
- GCC_except_table4022
- GCC_except_table4029
- GCC_except_table4034
- GCC_except_table4089
- GCC_except_table4111
- GCC_except_table4154
- GCC_except_table4159
- GCC_except_table4162
- GCC_except_table4246
- GCC_except_table4247
- GCC_except_table4303
- GCC_except_table4306
- GCC_except_table4368
- GCC_except_table4430
- GCC_except_table4434
- GCC_except_table4438
- GCC_except_table4441
- GCC_except_table4474
- GCC_except_table874
- GCC_except_table981
- GCC_except_table983
- GCC_except_table985
- GCC_except_table987
- GCC_except_table991
- GCC_except_table995
- GCC_except_table998
- _MTREventNumberKey
- _MTREventSystemUpTimeKey
- _OBJC_CLASS_$_HMMTRAccessoryServerDiagnosticsEvent
- _OBJC_CLASS_$_NSLocale
- _OBJC_IVAR_$_HMMTRAccessoryServer._diagnosticsEventDelegate
- _OBJC_IVAR_$_HMMTRAccessoryServerDiagnosticsEvent._values
- _OBJC_IVAR_$_HMMTRAnnounceOtaSchedulerTimer._endpoint
- _OBJC_IVAR_$_HMMTROTAAnnounceTimer._endpoint
- _OBJC_IVAR_$_HMMTRQueryImageResponseBusyTimer._endpoint
- _OBJC_METACLASS_$_HMMTRAccessoryServerDiagnosticsEvent
- __OBJC_$_INSTANCE_METHODS_HMMTRAccessoryServerDiagnosticsEvent
- __OBJC_$_INSTANCE_VARIABLES_HMMTRAccessoryServerDiagnosticsEvent
- __OBJC_$_PROP_LIST_HMMTRAccessoryServerDiagnosticsEvent
- __OBJC_CLASS_RO_$_HMMTRAccessoryServerDiagnosticsEvent
- __OBJC_METACLASS_RO_$_HMMTRAccessoryServerDiagnosticsEvent
- ___68-[HMMTRAccessoryServer(Diagnostics) collectDiagnosticsForAccessory:]_block_invoke
- ___78-[HMMTRAccessoryServer(Diagnostics) _readPastEventsFromAccessory:forClusters:]_block_invoke
- ___82-[HMMTRAccessoryServer(Diagnostics) resetWiFiNetworkDiagnosticsCountForAccessory:]_block_invoke
- ___84-[HMMTRAccessoryServer(Diagnostics) resetThreadNetworkDiagnosticsCountForAccessory:]_block_invoke
- ___block_descriptor_72_e8_32s40s48s56s64r_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s48l8r64l8s56l8
- _kHMMTRAccessoryServerDiagnosticsKeyGeneralBootReason
- _kHMMTRAccessoryServerDiagnosticsKeyGeneralDiagnosticsSupported
- _kHMMTRAccessoryServerDiagnosticsKeyGeneralRebootCount
- _kHMMTRAccessoryServerDiagnosticsKeyGeneralTotalOperationalHours
- _kHMMTRAccessoryServerDiagnosticsKeyGeneralUpTime
- _kHMMTRAccessoryServerDiagnosticsKeyThreadNetworkChannelNumber
- _kHMMTRAccessoryServerDiagnosticsKeyThreadNetworkConnectionStatus
- _kHMMTRAccessoryServerDiagnosticsKeyThreadNetworkDiagnosticsFeatureMap
- _kHMMTRAccessoryServerDiagnosticsKeyThreadNetworkErrorCount
- _kHMMTRAccessoryServerDiagnosticsKeyThreadNetworkOverrunCount
- _kHMMTRAccessoryServerDiagnosticsKeyThreadNetworkPacketCount
- _kHMMTRAccessoryServerDiagnosticsKeyThreadNetworkPacketRxBroadcastCount
- _kHMMTRAccessoryServerDiagnosticsKeyThreadNetworkPacketRxUnicastCount
- _kHMMTRAccessoryServerDiagnosticsKeyThreadNetworkPacketTxBroadcastCount
- _kHMMTRAccessoryServerDiagnosticsKeyThreadNetworkPacketTxUnicastCount
- _kHMMTRAccessoryServerDiagnosticsKeyWiFiNetworkAssociationFailure
- _kHMMTRAccessoryServerDiagnosticsKeyWiFiNetworkBeaconLostCount
- _kHMMTRAccessoryServerDiagnosticsKeyWiFiNetworkBeaconRxCount
- _kHMMTRAccessoryServerDiagnosticsKeyWiFiNetworkChannelNumber
- _kHMMTRAccessoryServerDiagnosticsKeyWiFiNetworkConnectionStatus
- _kHMMTRAccessoryServerDiagnosticsKeyWiFiNetworkDiagnosticsFeatureMap
- _kHMMTRAccessoryServerDiagnosticsKeyWiFiNetworkErrorCount
- _kHMMTRAccessoryServerDiagnosticsKeyWiFiNetworkPacketCount
- _kHMMTRAccessoryServerDiagnosticsKeyWiFiNetworkPacketRxMulticastCount
- _kHMMTRAccessoryServerDiagnosticsKeyWiFiNetworkPacketRxUnicastCount
- _kHMMTRAccessoryServerDiagnosticsKeyWiFiNetworkPacketTxMulticastCount
- _kHMMTRAccessoryServerDiagnosticsKeyWiFiNetworkPacketTxUnicastCount
- _kHMMTRAccessoryServerDiagnosticsLastRebootTime
- _logCategory._hmf_once_t1359
- _logCategory._hmf_once_t20
- _logCategory._hmf_once_v1360
- _logCategory._hmf_once_v21
- _objc_msgSend$_handleDiagnosticsEvent:
- _objc_msgSend$_preWarmCommissioningSession
- _objc_msgSend$_processEvent:
- _objc_msgSend$_readPastEventsFromAccessory:forClusters:
- _objc_msgSend$addTimeInterval:
- _objc_msgSend$diagnosticsEventDelegate
- _objc_msgSend$errorCountOfThreadNetworkDiagnostics:
- _objc_msgSend$errorCountOfWiFiNetworkDiagnostics:
- _objc_msgSend$handleDiagnosticsEvents:forAccessory:
- _objc_msgSend$init:server:endpoint:queue:
- _objc_msgSend$initWithServer:softwareUpdateProvider:timeInterval:endpoint:requestParams:queue:
- _objc_msgSend$initWithValues:
- _objc_msgSend$localeWithLocaleIdentifier:
- _objc_msgSend$packetCountOfThreadNetworkDiagnostics:
- _objc_msgSend$packetCountOfWiFiNetworkDiagnostics:
- _objc_msgSend$readAttributeBeaconLostCountWithParams:
- _objc_msgSend$readAttributeBeaconRxCountWithParams:
- _objc_msgSend$readAttributeBootReasonWithParams:
- _objc_msgSend$readAttributeChannelNumberWithParams:
- _objc_msgSend$readAttributeChannelWithParams:
- _objc_msgSend$readAttributeOverrunCountWithParams:
- _objc_msgSend$readAttributePacketMulticastRxCountWithParams:
- _objc_msgSend$readAttributePacketMulticastTxCountWithParams:
- _objc_msgSend$readAttributePacketUnicastRxCountWithParams:
- _objc_msgSend$readAttributePacketUnicastTxCountWithParams:
- _objc_msgSend$readAttributeRebootCountWithParams:
- _objc_msgSend$readAttributeRxBroadcastCountWithParams:
- _objc_msgSend$readAttributeRxErrFcsCountWithParams:
- _objc_msgSend$readAttributeRxErrInvalidSrcAddrCountWithParams:
- _objc_msgSend$readAttributeRxErrNoFrameCountWithParams:
- _objc_msgSend$readAttributeRxErrOtherCountWithParams:
- _objc_msgSend$readAttributeRxErrSecCountWithParams:
- _objc_msgSend$readAttributeRxErrUnknownNeighborCountWithParams:
- _objc_msgSend$readAttributeRxTotalCountWithParams:
- _objc_msgSend$readAttributeRxUnicastCountWithParams:
- _objc_msgSend$readAttributeTotalOperationalHoursWithParams:
- _objc_msgSend$readAttributeTxBroadcastCountWithParams:
- _objc_msgSend$readAttributeTxDirectMaxRetryExpiryCountWithParams:
- _objc_msgSend$readAttributeTxErrAbortCountWithParams:
- _objc_msgSend$readAttributeTxErrBusyChannelCountWithParams:
- _objc_msgSend$readAttributeTxErrCcaCountWithParams:
- _objc_msgSend$readAttributeTxIndirectMaxRetryExpiryCountWithParams:
- _objc_msgSend$readAttributeTxTotalCountWithParams:
- _objc_msgSend$readAttributeTxUnicastCountWithParams:
- _objc_msgSend$readAttributeUpTimeWithParams:
- _objc_msgSend$readEventsWithEndpointID:clusterID:eventID:params:queue:completion:
- _objc_msgSend$resetCountsWithExpectedValues:expectedValueInterval:completion:
- _objc_msgSend$setDiagnosticsEventDelegate:
- _objc_msgSend$setLocale:
- _objc_msgSend$setMinEventNumber:
- _objc_msgSend$startOtaProviderSchedulerTimer:endpoint:queue:
- _objc_msgSend$timeZoneForSecondsFromGMT:
CStrings:
+ "CompressedFabric"
+ "Deferred Matter commissioning attempt failed; replaying present commissionable nodes to retry"
+ "GroupKey v1.0"
+ "HMMTRBeaconProtectionKeyErrorDomain"
+ "Matter raw IPK must be 16 bytes (got %lu)"
+ "NFC deferred setup already completed system-commissioner pairing (commissioningID set); treating repeat attempt as success without re-pairing"
+ "Timer already deallocated, skipping completion handler"
+ "[%{public}@] Deferred Matter commissioning attempt failed; replaying present commissionable nodes to retry"
+ "[%{public}@] NFC deferred setup already completed system-commissioner pairing (commissioningID set); treating repeat attempt as success without re-pairing"
+ "[%{public}@] Timer already deallocated, skipping completion handler"
+ "compressedFabricId must be 8 bytes (got %lu)"
+ "rootPublicKey must be a 65-byte uncompressed P-256 point (leading 0x04 + X || Y) or a 64-byte X || Y; got %lu bytes"
+ "\xf0\xd2\xf0\xf0\xf01\xf0a"
- "%@ [Event no. %@, UpTime %@] Thread connection status %@"
- "%@ [Event no. %@, UpTime %@] WiFi Association Failure event with cause %@, status %@"
- "%@ [Event no. %@, UpTime %@] WiFi Connection Status event with status %@"
- "%@ [Event no. %@, UpTime %@] WiFi Disconnection event with reason %@"
- "Calling delegate to handle diagnostics event: %@ for accessory: %@"
- "Cluster"
- "Collecting accessory diagnostics for %@"
- "Deferred Matter commissioning attempt failed; will retry on the next matching discovery"
- "Diagnostic event did not find any destination accessory: %@"
- "Event"
- "EventNumber"
- "GeneralDiagnostics - BootReason: %@"
- "GeneralDiagnostics - RebootCount: %@"
- "GeneralDiagnostics - TotalOperationalHours: %@"
- "GeneralDiagnostics - UpTime: %@"
- "Reset ThreadNetworkDiagnostics counters with error: %@"
- "Reset WiFiNetworkDiagnostics counters with error: %@"
- "Resetting ThreadNetworkDiagnostics counters"
- "Resetting WiFiNetworkDiagnostics counters"
- "ThreadNetworkDiagnostics - ChannelNumber: %@"
- "ThreadNetworkDiagnostics - ErrorCount: %@"
- "ThreadNetworkDiagnostics - FeatureMap: %@"
- "ThreadNetworkDiagnostics - OverrunCount: %@"
- "ThreadNetworkDiagnostics - PacketCount: %@"
- "ThreadNetworkDiagnostics - RxBroadcastCount: %@"
- "ThreadNetworkDiagnostics - RxUnicastCount: %@"
- "ThreadNetworkDiagnostics - TxBroadcastCount: %@"
- "ThreadNetworkDiagnostics - TxUnicastCount: %@"
- "ThreadNetworkDiagnostics ConnectionStatus event data has unexpected structure: %@"
- "ThreadNetworkDiagnostics ConnectionStatus event data type is unexpected: %@"
- "UpTime"
- "WiFiNetworkDiagnostics - BeaconLostCount: %@"
- "WiFiNetworkDiagnostics - BeaconRxCount: %@"
- "WiFiNetworkDiagnostics - ChannelNumber: %@"
- "WiFiNetworkDiagnostics - ErrorCount: %@"
- "WiFiNetworkDiagnostics - FeatureMap: %@"
- "WiFiNetworkDiagnostics - PacketCount: %@"
- "WiFiNetworkDiagnostics - PacketRxMulticastCount: %@"
- "WiFiNetworkDiagnostics - PacketRxUnicastCount: %@"
- "WiFiNetworkDiagnostics - PacketTxMulticastCount: %@"
- "WiFiNetworkDiagnostics - PacketTxUnicastCount: %@"
- "WiFiNetworkDiagnostics AssociationFailure event data has unexpected structure: %@"
- "WiFiNetworkDiagnostics AssociationFailure event data type is unexpected: %@"
- "WiFiNetworkDiagnostics ConnectionStatus event data has unexpected structure: %@"
- "WiFiNetworkDiagnostics ConnectionStatus event data type is unexpected: %@"
- "WiFiNetworkDiagnostics Disconnection event data has unexpected structure: %@"
- "WiFiNetworkDiagnostics Disconnection event data type is unexpected: %@"
- "[%@] Read diagnostic events for cluster ID 0x%lX, error: %@"
- "[%@] Received diagnostic event %@"
- "[%{public}@] %@ [Event no. %@, UpTime %@] Thread connection status %@"
- "[%{public}@] %@ [Event no. %@, UpTime %@] WiFi Association Failure event with cause %@, status %@"
- "[%{public}@] %@ [Event no. %@, UpTime %@] WiFi Connection Status event with status %@"
- "[%{public}@] %@ [Event no. %@, UpTime %@] WiFi Disconnection event with reason %@"
- "[%{public}@] Calling delegate to handle diagnostics event: %@ for accessory: %@"
- "[%{public}@] Collecting accessory diagnostics for %@"
- "[%{public}@] Deferred Matter commissioning attempt failed; will retry on the next matching discovery"
- "[%{public}@] Diagnostic event did not find any destination accessory: %@"
- "[%{public}@] GeneralDiagnostics - BootReason: %@"
- "[%{public}@] GeneralDiagnostics - RebootCount: %@"
- "[%{public}@] GeneralDiagnostics - TotalOperationalHours: %@"
- "[%{public}@] GeneralDiagnostics - UpTime: %@"
- "[%{public}@] Reset ThreadNetworkDiagnostics counters with error: %@"
- "[%{public}@] Reset WiFiNetworkDiagnostics counters with error: %@"
- "[%{public}@] Resetting ThreadNetworkDiagnostics counters"
- "[%{public}@] Resetting WiFiNetworkDiagnostics counters"
- "[%{public}@] ThreadNetworkDiagnostics - ChannelNumber: %@"
- "[%{public}@] ThreadNetworkDiagnostics - ErrorCount: %@"
- "[%{public}@] ThreadNetworkDiagnostics - FeatureMap: %@"
- "[%{public}@] ThreadNetworkDiagnostics - OverrunCount: %@"
- "[%{public}@] ThreadNetworkDiagnostics - PacketCount: %@"
- "[%{public}@] ThreadNetworkDiagnostics - RxBroadcastCount: %@"
- "[%{public}@] ThreadNetworkDiagnostics - RxUnicastCount: %@"
- "[%{public}@] ThreadNetworkDiagnostics - TxBroadcastCount: %@"
- "[%{public}@] ThreadNetworkDiagnostics - TxUnicastCount: %@"
- "[%{public}@] ThreadNetworkDiagnostics ConnectionStatus event data has unexpected structure: %@"
- "[%{public}@] ThreadNetworkDiagnostics ConnectionStatus event data type is unexpected: %@"
- "[%{public}@] WiFiNetworkDiagnostics - BeaconLostCount: %@"
- "[%{public}@] WiFiNetworkDiagnostics - BeaconRxCount: %@"
- "[%{public}@] WiFiNetworkDiagnostics - ChannelNumber: %@"
- "[%{public}@] WiFiNetworkDiagnostics - ErrorCount: %@"
- "[%{public}@] WiFiNetworkDiagnostics - FeatureMap: %@"
- "[%{public}@] WiFiNetworkDiagnostics - PacketCount: %@"
- "[%{public}@] WiFiNetworkDiagnostics - PacketRxMulticastCount: %@"
- "[%{public}@] WiFiNetworkDiagnostics - PacketRxUnicastCount: %@"
- "[%{public}@] WiFiNetworkDiagnostics - PacketTxMulticastCount: %@"
- "[%{public}@] WiFiNetworkDiagnostics - PacketTxUnicastCount: %@"
- "[%{public}@] WiFiNetworkDiagnostics AssociationFailure event data has unexpected structure: %@"
- "[%{public}@] WiFiNetworkDiagnostics AssociationFailure event data type is unexpected: %@"
- "[%{public}@] WiFiNetworkDiagnostics ConnectionStatus event data has unexpected structure: %@"
- "[%{public}@] WiFiNetworkDiagnostics ConnectionStatus event data type is unexpected: %@"
- "[%{public}@] WiFiNetworkDiagnostics Disconnection event data has unexpected structure: %@"
- "[%{public}@] WiFiNetworkDiagnostics Disconnection event data type is unexpected: %@"
- "[%{public}@] [%@] Read diagnostic events for cluster ID 0x%lX, error: %@"
- "[%{public}@] [%@] Received diagnostic event %@"
- "en_US_POSIX"
- "general_BootReason"
- "general_DiagnosticsSupported"
- "general_LastRebootTime"
- "general_RebootCount"
- "general_TotalOperationalHours"
- "general_UpTime"
- "threadNetwork_ChannelNumber"
- "threadNetwork_ConnectionStatus"
- "threadNetwork_DiagnosticsFeatureMap"
- "threadNetwork_ErrorCount"
- "threadNetwork_OverrunCount"
- "threadNetwork_PacketCount"
- "threadNetwork_PacketRxBroadcastCount"
- "threadNetwork_PacketRxUnicastCount"
- "threadNetwork_PacketTxBroadcastCount"
- "threadNetwork_PacketTxUnicastCount"
- "wifiNetwork_AssociationFailure"
- "wifiNetwork_BeaconLostCount"
- "wifiNetwork_BeaconRxCount"
- "wifiNetwork_ChannelNumber"
- "wifiNetwork_ConnectionStatus"
- "wifiNetwork_DiagnosticsFeatureMap"
- "wifiNetwork_ErrorCount"
- "wifiNetwork_PacketCount"
- "wifiNetwork_PacketRxMulticastCount"
- "wifiNetwork_PacketRxUnicastCount"
- "wifiNetwork_PacketTxMulticastCount"
- "wifiNetwork_PacketTxUnicastCount"
- "yyyy-MM-dd' 'HH:mm:ss-ZZZZZ"
- "\xf0\xd2\xf0\xf0\xf01с"

```
