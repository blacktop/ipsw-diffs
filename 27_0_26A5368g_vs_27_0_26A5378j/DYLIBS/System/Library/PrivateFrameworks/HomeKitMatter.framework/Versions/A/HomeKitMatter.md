## HomeKitMatter

> `/System/Library/PrivateFrameworks/HomeKitMatter.framework/Versions/A/HomeKitMatter`

```diff

-  __TEXT.__text: 0x18cbdc
-  __TEXT.__objc_methlist: 0xa7dc
+  __TEXT.__text: 0x1869f0
+  __TEXT.__objc_methlist: 0xa6ec
   __TEXT.__const: 0x250
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__gcc_except_tab: 0x3068
-  __TEXT.__cstring: 0x6c98
-  __TEXT.__oslogstring: 0x4ad55
+  __TEXT.__gcc_except_tab: 0x2f44
+  __TEXT.__cstring: 0x6924
+  __TEXT.__oslogstring: 0x49912
   __TEXT.__ustring: 0x68
-  __TEXT.__unwind_info: 0x2fc0
+  __TEXT.__unwind_info: 0x2f70
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xc50
-  __DATA_CONST.__objc_classlist: 0x438
+  __DATA_CONST.__const: 0xb78
+  __DATA_CONST.__objc_classlist: 0x430
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6ce8
+  __DATA_CONST.__objc_selrefs: 0x6b50
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x2f8
-  __DATA_CONST.__objc_arraydata: 0x248
-  __DATA_CONST.__got: 0x958
+  __DATA_CONST.__objc_superrefs: 0x2f0
+  __DATA_CONST.__objc_arraydata: 0x240
+  __DATA_CONST.__got: 0x938
   __AUTH_CONST.__const: 0x55d0
-  __AUTH_CONST.__cfstring: 0x6da0
-  __AUTH_CONST.__objc_const: 0xfb30
-  __AUTH_CONST.__objc_intobj: 0x16f8
-  __AUTH_CONST.__objc_arrayobj: 0x180
+  __AUTH_CONST.__cfstring: 0x6960
+  __AUTH_CONST.__objc_const: 0xf9b8
+  __AUTH_CONST.__objc_intobj: 0x16b0
+  __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x1db0
-  __DATA.__objc_ivar: 0xb10
+  __AUTH.__objc_data: 0x1d60
+  __DATA.__objc_ivar: 0xafc
   __DATA.__data: 0xe40
-  __DATA.__bss: 0x4a8
+  __DATA.__bss: 0x478
   __DATA_DIRTY.__objc_data: 0xc80
-  __DATA_DIRTY.__bss: 0x88
+  __DATA_DIRTY.__bss: 0xb8
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /System/Library/PrivateFrameworks/UARPKit.framework/Versions/A/UARPKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4417
-  Symbols:   10592
-  CStrings:  6412
+  Functions: 4395
+  Symbols:   10481
+  CStrings:  6258
 
Sections:
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ -[HMMTRAccessoryServer startBusyImageResponseTimer:timeInterval:requestParams:queue:]
+ -[HMMTRAccessoryServer startOtaProviderSchedulerTimer:queue:]
+ -[HMMTRAccessoryServerBrowser _cancelBonjourBrowser]
+ -[HMMTRAccessoryServerBrowser _filterAccessoryServersUnpairedFromStorageAmongServers:completion:]
+ -[HMMTRAccessoryServerBrowser _reconcileBonjourBrowser]
+ -[HMMTRAccessoryServerBrowser preWarmCommissioningSession]
+ -[HMMTRAccessoryServerBrowserDataSourceDefault makeAttestationDataStoreWithURL:]
+ -[HMMTRAnnounceOtaSchedulerTimer init:server:queue:]
+ -[HMMTROTAAnnounceTimer initWithServer:nodeId:queue:]
+ -[HMMTRQueryImageResponseBusyTimer initWithServer:softwareUpdateProvider:timeInterval:requestParams:queue:]
+ GCC_except_table1021
+ GCC_except_table1027
+ GCC_except_table1029
+ GCC_except_table1151
+ GCC_except_table1219
+ GCC_except_table1265
+ GCC_except_table1273
+ GCC_except_table1324
+ GCC_except_table1332
+ GCC_except_table1369
+ GCC_except_table1406
+ GCC_except_table1433
+ GCC_except_table1629
+ GCC_except_table1672
+ GCC_except_table1826
+ GCC_except_table1827
+ GCC_except_table1828
+ GCC_except_table1831
+ GCC_except_table1851
+ GCC_except_table1852
+ GCC_except_table1853
+ GCC_except_table1858
+ GCC_except_table1861
+ GCC_except_table1862
+ GCC_except_table1863
+ GCC_except_table1864
+ GCC_except_table1865
+ GCC_except_table1866
+ GCC_except_table1867
+ GCC_except_table1926
+ GCC_except_table1934
+ GCC_except_table2022
+ GCC_except_table2137
+ GCC_except_table2139
+ GCC_except_table2169
+ GCC_except_table2179
+ GCC_except_table2181
+ GCC_except_table2237
+ GCC_except_table2283
+ GCC_except_table2308
+ GCC_except_table2379
+ GCC_except_table2649
+ GCC_except_table2653
+ GCC_except_table2711
+ GCC_except_table2744
+ GCC_except_table2789
+ GCC_except_table2791
+ GCC_except_table2822
+ GCC_except_table2823
+ GCC_except_table2824
+ GCC_except_table2847
+ GCC_except_table2848
+ GCC_except_table2849
+ GCC_except_table2850
+ GCC_except_table2851
+ GCC_except_table2852
+ GCC_except_table2853
+ GCC_except_table2863
+ GCC_except_table2865
+ GCC_except_table2876
+ GCC_except_table2896
+ GCC_except_table2911
+ GCC_except_table2917
+ GCC_except_table2932
+ GCC_except_table2935
+ GCC_except_table2963
+ GCC_except_table2982
+ GCC_except_table2991
+ GCC_except_table2996
+ GCC_except_table3008
+ GCC_except_table3061
+ GCC_except_table3062
+ GCC_except_table3442
+ GCC_except_table3443
+ GCC_except_table3444
+ GCC_except_table3448
+ GCC_except_table3454
+ GCC_except_table3457
+ GCC_except_table3473
+ GCC_except_table3488
+ GCC_except_table3556
+ GCC_except_table3557
+ GCC_except_table3586
+ GCC_except_table3617
+ GCC_except_table3621
+ GCC_except_table3629
+ GCC_except_table3648
+ GCC_except_table3651
+ GCC_except_table3693
+ GCC_except_table3695
+ GCC_except_table3697
+ GCC_except_table3739
+ GCC_except_table3816
+ GCC_except_table3863
+ GCC_except_table3883
+ GCC_except_table3907
+ GCC_except_table3911
+ GCC_except_table3926
+ GCC_except_table3927
+ GCC_except_table3928
+ GCC_except_table3934
+ GCC_except_table3941
+ GCC_except_table3982
+ GCC_except_table4047
+ GCC_except_table4053
+ GCC_except_table4056
+ GCC_except_table4142
+ GCC_except_table4143
+ GCC_except_table4200
+ GCC_except_table4203
+ GCC_except_table4267
+ GCC_except_table4327
+ GCC_except_table4333
+ GCC_except_table4337
+ GCC_except_table4341
+ GCC_except_table4375
+ GCC_except_table848
+ GCC_except_table890
+ GCC_except_table941
+ GCC_except_table947
+ GCC_except_table949
+ GCC_except_table951
+ GCC_except_table953
+ _HMMTRShouldSelectCategory
+ __85-[HMMTRAccessoryServerBrowser _updateDiscoveredAccessoryServersWithNodes:fabricUUID:]_block_invoke
+ ___97-[HMMTRAccessoryServerBrowser _filterAccessoryServersUnpairedFromStorageAmongServers:completion:]_block_invoke
+ ___97-[HMMTRAccessoryServerBrowser _filterAccessoryServersUnpairedFromStorageAmongServers:completion:]_block_invoke_2
+ ___block_descriptor_56_e8_32s40s48s_e17_v16?0"NSArray"8l
+ _kDefaultOtaProviderEndpoint
+ _objc_msgSend$_cancelBonjourBrowser
+ _objc_msgSend$_filterAccessoryServersUnpairedFromStorageAmongServers:completion:
+ _objc_msgSend$_reconcileBonjourBrowser
+ _objc_msgSend$init:server:queue:
+ _objc_msgSend$initWithServer:softwareUpdateProvider:timeInterval:requestParams:queue:
+ _objc_msgSend$makeAttestationDataStoreWithURL:
+ _objc_msgSend$startOtaProviderSchedulerTimer:queue:
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
- GCC_except_table1045
- GCC_except_table1051
- GCC_except_table1053
- GCC_except_table1177
- GCC_except_table1245
- GCC_except_table1291
- GCC_except_table1299
- GCC_except_table1350
- GCC_except_table1358
- GCC_except_table1395
- GCC_except_table1432
- GCC_except_table1461
- GCC_except_table1657
- GCC_except_table1700
- GCC_except_table1856
- GCC_except_table1859
- GCC_except_table1879
- GCC_except_table1880
- GCC_except_table1881
- GCC_except_table1882
- GCC_except_table1883
- GCC_except_table1886
- GCC_except_table1889
- GCC_except_table1890
- GCC_except_table1891
- GCC_except_table1892
- GCC_except_table1893
- GCC_except_table1894
- GCC_except_table1895
- GCC_except_table1954
- GCC_except_table1962
- GCC_except_table2050
- GCC_except_table2165
- GCC_except_table2167
- GCC_except_table2197
- GCC_except_table2207
- GCC_except_table2209
- GCC_except_table2265
- GCC_except_table2311
- GCC_except_table2335
- GCC_except_table2406
- GCC_except_table2675
- GCC_except_table2679
- GCC_except_table2737
- GCC_except_table2770
- GCC_except_table2811
- GCC_except_table2813
- GCC_except_table2844
- GCC_except_table2845
- GCC_except_table2868
- GCC_except_table2869
- GCC_except_table2870
- GCC_except_table2871
- GCC_except_table2872
- GCC_except_table2873
- GCC_except_table2874
- GCC_except_table2875
- GCC_except_table2885
- GCC_except_table2887
- GCC_except_table2898
- GCC_except_table2918
- GCC_except_table2933
- GCC_except_table2976
- GCC_except_table2979
- GCC_except_table2983
- GCC_except_table2985
- GCC_except_table3004
- GCC_except_table3011
- GCC_except_table3016
- GCC_except_table3028
- GCC_except_table3081
- GCC_except_table3082
- GCC_except_table3464
- GCC_except_table3465
- GCC_except_table3466
- GCC_except_table3470
- GCC_except_table3476
- GCC_except_table3479
- GCC_except_table3495
- GCC_except_table3510
- GCC_except_table3579
- GCC_except_table3580
- GCC_except_table3609
- GCC_except_table3640
- GCC_except_table3644
- GCC_except_table3652
- GCC_except_table3671
- GCC_except_table3674
- GCC_except_table3720
- GCC_except_table3738
- GCC_except_table3740
- GCC_except_table3761
- GCC_except_table3838
- GCC_except_table3885
- GCC_except_table3905
- GCC_except_table3929
- GCC_except_table3933
- GCC_except_table3948
- GCC_except_table3949
- GCC_except_table3950
- GCC_except_table3956
- GCC_except_table3963
- GCC_except_table4026
- GCC_except_table4069
- GCC_except_table4075
- GCC_except_table4078
- GCC_except_table4164
- GCC_except_table4165
- GCC_except_table4222
- GCC_except_table4225
- GCC_except_table4289
- GCC_except_table4349
- GCC_except_table4355
- GCC_except_table4359
- GCC_except_table4363
- GCC_except_table4397
- GCC_except_table850
- GCC_except_table892
- GCC_except_table963
- GCC_except_table965
- GCC_except_table967
- GCC_except_table969
- GCC_except_table973
- GCC_except_table977
- GCC_except_table982
- OBJC_IVAR_$_HMMTRAccessoryServer._diagnosticsEventDelegate
- OBJC_IVAR_$_HMMTRAccessoryServerDiagnosticsEvent._values
- OBJC_IVAR_$_HMMTRAnnounceOtaSchedulerTimer._endpoint
- OBJC_IVAR_$_HMMTROTAAnnounceTimer._endpoint
- OBJC_IVAR_$_HMMTRQueryImageResponseBusyTimer._endpoint
- _MTREventNumberKey
- _MTREventSystemUpTimeKey
- _OBJC_CLASS_$_HMMTRAccessoryServerDiagnosticsEvent
- _OBJC_CLASS_$_NSLocale
- _OBJC_METACLASS_$_HMMTRAccessoryServerDiagnosticsEvent
- __82-[HMMTRAccessoryServer(Diagnostics) resetWiFiNetworkDiagnosticsCountForAccessory:]_block_invoke
- __84-[HMMTRAccessoryServer(Diagnostics) resetThreadNetworkDiagnosticsCountForAccessory:]_block_invoke
- __OBJC_$_INSTANCE_METHODS_HMMTRAccessoryServerDiagnosticsEvent
- __OBJC_$_INSTANCE_VARIABLES_HMMTRAccessoryServerDiagnosticsEvent
- __OBJC_$_PROP_LIST_HMMTRAccessoryServerDiagnosticsEvent
- __OBJC_CLASS_RO_$_HMMTRAccessoryServerDiagnosticsEvent
- __OBJC_METACLASS_RO_$_HMMTRAccessoryServerDiagnosticsEvent
- ___68-[HMMTRAccessoryServer(Diagnostics) collectDiagnosticsForAccessory:]_block_invoke
- ___78-[HMMTRAccessoryServer(Diagnostics) _readPastEventsFromAccessory:forClusters:]_block_invoke
- ___82-[HMMTRAccessoryServer(Diagnostics) resetWiFiNetworkDiagnosticsCountForAccessory:]_block_invoke
- ___84-[HMMTRAccessoryServer(Diagnostics) resetThreadNetworkDiagnosticsCountForAccessory:]_block_invoke
- ___block_descriptor_72_e8_32s40s48s56s64r_e29_v24?0"NSArray"8"NSError"16l
- ___copy_helper_block_e8_32s40s48s56s64r
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
- logCategory._hmf_once_t20
- logCategory._hmf_once_v21
CStrings:
+ "Timer already deallocated, skipping completion handler"
+ "[%{public}@] Timer already deallocated, skipping completion handler"
- "%@ [Event no. %@, UpTime %@] Thread connection status %@"
- "%@ [Event no. %@, UpTime %@] WiFi Association Failure event with cause %@, status %@"
- "%@ [Event no. %@, UpTime %@] WiFi Connection Status event with status %@"
- "%@ [Event no. %@, UpTime %@] WiFi Disconnection event with reason %@"
- "Calling delegate to handle diagnostics event: %@ for accessory: %@"
- "Cluster"
- "Collecting accessory diagnostics for %@"
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

```
