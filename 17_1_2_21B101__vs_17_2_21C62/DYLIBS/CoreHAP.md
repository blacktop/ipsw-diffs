## CoreHAP

> `/System/Library/PrivateFrameworks/CoreHAP.framework/CoreHAP`

```diff

-1076.2.8.1.1
-  __TEXT.__text: 0x196d5c
-  __TEXT.__auth_stubs: 0x1550
-  __TEXT.__objc_methlist: 0x11534
+1092.3.10.1.2
+  __TEXT.__text: 0x1982ac
+  __TEXT.__auth_stubs: 0x1560
+  __TEXT.__objc_methlist: 0x116c4
   __TEXT.__const: 0x5e0
   __TEXT.__gcc_except_tab: 0x4784
-  __TEXT.__cstring: 0xfcf5
-  __TEXT.__oslogstring: 0x1f0ac
+  __TEXT.__cstring: 0xfdc3
+  __TEXT.__oslogstring: 0x1f2e5
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__unwind_info: 0x5bf0
-  __TEXT.__objc_classname: 0x2dce
-  __TEXT.__objc_methname: 0x25610
-  __TEXT.__objc_methtype: 0x8d75
-  __TEXT.__objc_stubs: 0x17c60
+  __TEXT.__unwind_info: 0x5c40
+  __TEXT.__objc_classname: 0x2dfa
+  __TEXT.__objc_methname: 0x25bea
+  __TEXT.__objc_methtype: 0x8e8d
+  __TEXT.__objc_stubs: 0x17e60
   __DATA_CONST.__got: 0x2d0
-  __DATA_CONST.__const: 0x5318
-  __DATA_CONST.__objc_classlist: 0x950
+  __DATA_CONST.__const: 0x5330
+  __DATA_CONST.__objc_classlist: 0x960
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x330
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1bd00
-  __DATA_CONST.__objc_selrefs: 0x6a90
+  __DATA_CONST.__objc_const: 0x1c000
+  __DATA_CONST.__objc_selrefs: 0x6b68
   __DATA_CONST.__objc_arraydata: 0x208
-  __AUTH_CONST.__cfstring: 0xd200
+  __AUTH_CONST.__cfstring: 0xd360
   __AUTH_CONST.__const: 0x7c0
-  __AUTH_CONST.__objc_const: 0x8f98
+  __AUTH_CONST.__objc_const: 0x9028
   __AUTH_CONST.__objc_intobj: 0x660
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0xd8
-  __AUTH_CONST.__auth_got: 0xab8
-  __AUTH.__objc_data: 0x5140
+  __AUTH_CONST.__auth_got: 0xac0
+  __AUTH.__objc_data: 0x51e0
   __DATA.__objc_protorefs: 0xc0
-  __DATA.__objc_classrefs: 0xab8
-  __DATA.__objc_superrefs: 0x7d8
-  __DATA.__objc_ivar: 0x1474
-  __DATA.__data: 0x266a
+  __DATA.__objc_classrefs: 0xac8
+  __DATA.__objc_superrefs: 0x7e8
+  __DATA.__objc_ivar: 0x14a0
+  __DATA.__data: 0x267a
   __DATA.__bss: 0x4b1
   __DATA_DIRTY.__objc_data: 0xbe0
   __DATA_DIRTY.__common: 0x20
-  __DATA_DIRTY.__bss: 0xa0
+  __DATA_DIRTY.__bss: 0x90
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 89B14CE8-649E-3A24-A887-879180B2D9C8
-  Functions: 7375
-  Symbols:   23878
-  CStrings:  12551
+  UUID: 4E75B652-DD2D-3C54-9F54-6AFDDAF0BCD9
+  Functions: 7412
+  Symbols:   23991
+  CStrings:  12639
 
Symbols:
+ -[HAPAccessory linkLayerType]
+ -[HAPAccessory setLinkLayerType:]
+ -[HAPAccessoryServerBookkeeping connectionMethod]
+ -[HAPAccessoryServerBookkeeping initWithDiscoveryMethod:]
+ -[HAPAccessoryServerBookkeeping initialDiscoveryMethod]
+ -[HAPAccessoryServerBookkeeping lastDiscoveryMethod]
+ -[HAPAccessoryServerBookkeeping setConnectionMethod:]
+ -[HAPAccessoryServerBookkeeping setLastDiscoveryMethod:]
+ -[HAPAccessoryServerBrowserBTLE updateScanInBackground:]
+ -[HAPAccessoryServerBrowserIP _handleConnectionUpdateWithBonjourDeviceInfo:socketInfo:]
+ -[HAPAccessoryServerBrowserIP handleConnectionUpdateWithBonjourDeviceInfo:socketInfo:]
+ -[HAPAccessoryServerBrowserIP serverIdentifierToSkipBonjourUpdate]
+ -[HAPAccessoryServerBrowserIP setServerIdentifierToSkipBonjourUpdate:]
+ -[HAPAccessoryServerIP _updateWithBonjourDeviceInfo:socketInfo:]
+ -[HAPAccessoryServerIP currentSocketInfo]
+ -[HAPAccessoryServerIP discoveryBookkeeping]
+ -[HAPAccessoryServerIP initWithBonjourDeviceInfo:keyStore:browser:discoveryMethod:]
+ -[HAPAccessoryServerIP initWithKeyStore:browser:discoveryMethod:]
+ -[HAPAccessoryServerIP pendingConnectionSocketInfo]
+ -[HAPAccessoryServerIP setDiscoveryBookkeeping:]
+ -[HAPAccessoryServerIP setPendingConnectionSocketInfo:]
+ -[HAPAccessoryServerIP updateWithBonjourDeviceInfo:socketInfo:]
+ -[HAPHTTPClient getHttpClientPeerAddress:]
+ -[HAPHTTPClient initWithSocketInfo:eventsEnabled:queue:wakeAddress:]
+ -[HAPHTTPClient peerSocketInfo]
+ -[HAPHTTPClient pendingConnectionSocketInfo]
+ -[HAPSocketInfo .cxx_destruct]
+ -[HAPSocketInfo dictionaryRepresentation]
+ -[HAPSocketInfo initWithDictionary:]
+ -[HAPSocketInfo initWithIPAddressString:port:]
+ -[HAPSocketInfo initWithSocket:]
+ -[HAPSocketInfo ipAddressString]
+ -[HAPSocketInfo port]
+ -[HAPThreadNetworkMetadata initWithActiveOperationalDataSet:]
+ GCC_except_table1013
+ GCC_except_table1017
+ GCC_except_table1030
+ GCC_except_table1035
+ GCC_except_table1044
+ GCC_except_table1046
+ GCC_except_table1048
+ GCC_except_table1050
+ GCC_except_table1176
+ GCC_except_table1180
+ GCC_except_table1182
+ GCC_except_table1564
+ GCC_except_table1583
+ GCC_except_table1589
+ GCC_except_table1593
+ GCC_except_table1595
+ GCC_except_table1600
+ GCC_except_table1604
+ GCC_except_table1622
+ GCC_except_table1637
+ GCC_except_table1641
+ GCC_except_table1643
+ GCC_except_table1798
+ GCC_except_table1800
+ GCC_except_table1802
+ GCC_except_table1811
+ GCC_except_table1813
+ GCC_except_table1817
+ GCC_except_table1820
+ GCC_except_table1822
+ GCC_except_table1825
+ GCC_except_table1842
+ GCC_except_table1845
+ GCC_except_table1847
+ GCC_except_table1853
+ GCC_except_table1862
+ GCC_except_table1865
+ GCC_except_table1868
+ GCC_except_table1870
+ GCC_except_table1876
+ GCC_except_table1880
+ GCC_except_table1888
+ GCC_except_table1899
+ GCC_except_table1936
+ GCC_except_table1942
+ GCC_except_table2113
+ GCC_except_table2142
+ GCC_except_table2253
+ GCC_except_table2261
+ GCC_except_table2262
+ GCC_except_table2263
+ GCC_except_table2264
+ GCC_except_table2266
+ GCC_except_table2281
+ GCC_except_table2295
+ GCC_except_table2372
+ GCC_except_table2384
+ GCC_except_table2410
+ GCC_except_table2418
+ GCC_except_table2429
+ GCC_except_table2443
+ GCC_except_table2446
+ GCC_except_table2451
+ GCC_except_table2459
+ GCC_except_table2465
+ GCC_except_table2467
+ GCC_except_table2648
+ GCC_except_table2717
+ GCC_except_table2739
+ GCC_except_table2754
+ GCC_except_table2766
+ GCC_except_table2775
+ GCC_except_table2782
+ GCC_except_table2785
+ GCC_except_table2790
+ GCC_except_table2846
+ GCC_except_table2849
+ GCC_except_table2854
+ GCC_except_table2856
+ GCC_except_table2870
+ GCC_except_table2884
+ GCC_except_table2886
+ GCC_except_table2890
+ GCC_except_table2898
+ GCC_except_table2906
+ GCC_except_table2955
+ GCC_except_table2963
+ GCC_except_table2965
+ GCC_except_table2966
+ GCC_except_table2989
+ GCC_except_table3224
+ GCC_except_table3283
+ GCC_except_table3284
+ GCC_except_table3288
+ GCC_except_table3293
+ GCC_except_table3296
+ GCC_except_table3297
+ GCC_except_table3299
+ GCC_except_table3319
+ GCC_except_table3330
+ GCC_except_table3331
+ GCC_except_table3333
+ GCC_except_table3335
+ GCC_except_table3341
+ GCC_except_table3343
+ GCC_except_table3349
+ GCC_except_table3361
+ GCC_except_table3363
+ GCC_except_table3367
+ GCC_except_table3371
+ GCC_except_table3375
+ GCC_except_table3419
+ GCC_except_table3423
+ GCC_except_table3426
+ GCC_except_table3428
+ GCC_except_table3430
+ GCC_except_table3548
+ GCC_except_table3573
+ GCC_except_table3663
+ GCC_except_table3688
+ GCC_except_table3692
+ GCC_except_table3695
+ GCC_except_table3698
+ GCC_except_table3707
+ GCC_except_table3710
+ GCC_except_table3713
+ GCC_except_table3716
+ GCC_except_table3721
+ GCC_except_table3732
+ GCC_except_table3746
+ GCC_except_table3754
+ GCC_except_table3765
+ GCC_except_table3770
+ GCC_except_table3771
+ GCC_except_table3789
+ GCC_except_table3791
+ GCC_except_table3793
+ GCC_except_table3794
+ GCC_except_table3797
+ GCC_except_table3803
+ GCC_except_table3806
+ GCC_except_table3808
+ GCC_except_table3814
+ GCC_except_table3816
+ GCC_except_table3819
+ GCC_except_table3831
+ GCC_except_table3842
+ GCC_except_table3844
+ GCC_except_table3853
+ GCC_except_table3859
+ GCC_except_table387
+ GCC_except_table403
+ GCC_except_table411
+ GCC_except_table4119
+ GCC_except_table4125
+ GCC_except_table4142
+ GCC_except_table4146
+ GCC_except_table4163
+ GCC_except_table4182
+ GCC_except_table4196
+ GCC_except_table4200
+ GCC_except_table4303
+ GCC_except_table4383
+ GCC_except_table4391
+ GCC_except_table4401
+ GCC_except_table441
+ GCC_except_table4437
+ GCC_except_table4440
+ GCC_except_table4441
+ GCC_except_table4442
+ GCC_except_table4443
+ GCC_except_table448
+ GCC_except_table4536
+ GCC_except_table4537
+ GCC_except_table4539
+ GCC_except_table4540
+ GCC_except_table4541
+ GCC_except_table4547
+ GCC_except_table4548
+ GCC_except_table4550
+ GCC_except_table4557
+ GCC_except_table4560
+ GCC_except_table4562
+ GCC_except_table4567
+ GCC_except_table4570
+ GCC_except_table4573
+ GCC_except_table4577
+ GCC_except_table4581
+ GCC_except_table4610
+ GCC_except_table4611
+ GCC_except_table463
+ GCC_except_table4630
+ GCC_except_table4640
+ GCC_except_table4643
+ GCC_except_table4648
+ GCC_except_table4651
+ GCC_except_table471
+ GCC_except_table483
+ GCC_except_table487
+ GCC_except_table489
+ GCC_except_table4912
+ GCC_except_table4916
+ GCC_except_table4950
+ GCC_except_table4954
+ GCC_except_table4956
+ GCC_except_table4958
+ GCC_except_table496
+ GCC_except_table502
+ GCC_except_table5111
+ GCC_except_table5117
+ GCC_except_table5121
+ GCC_except_table5122
+ GCC_except_table5123
+ GCC_except_table5124
+ GCC_except_table5165
+ GCC_except_table5166
+ GCC_except_table5184
+ GCC_except_table5196
+ GCC_except_table5199
+ GCC_except_table520
+ GCC_except_table5204
+ GCC_except_table5206
+ GCC_except_table5220
+ GCC_except_table530
+ GCC_except_table537
+ GCC_except_table5419
+ GCC_except_table5431
+ GCC_except_table5436
+ GCC_except_table5439
+ GCC_except_table5442
+ GCC_except_table5443
+ GCC_except_table5445
+ GCC_except_table5497
+ GCC_except_table5505
+ GCC_except_table5510
+ GCC_except_table5514
+ GCC_except_table5518
+ GCC_except_table5522
+ GCC_except_table5526
+ GCC_except_table5534
+ GCC_except_table5536
+ GCC_except_table5538
+ GCC_except_table5576
+ GCC_except_table5603
+ GCC_except_table5604
+ GCC_except_table5605
+ GCC_except_table5606
+ GCC_except_table564
+ GCC_except_table5664
+ GCC_except_table5665
+ GCC_except_table5679
+ GCC_except_table568
+ GCC_except_table5698
+ GCC_except_table570
+ GCC_except_table5701
+ GCC_except_table5702
+ GCC_except_table5707
+ GCC_except_table5710
+ GCC_except_table5717
+ GCC_except_table572
+ GCC_except_table5720
+ GCC_except_table5734
+ GCC_except_table5741
+ GCC_except_table5747
+ GCC_except_table5756
+ GCC_except_table5758
+ GCC_except_table5762
+ GCC_except_table5763
+ GCC_except_table5779
+ GCC_except_table578
+ GCC_except_table580
+ GCC_except_table5802
+ GCC_except_table5803
+ GCC_except_table5808
+ GCC_except_table5812
+ GCC_except_table5813
+ GCC_except_table5816
+ GCC_except_table5822
+ GCC_except_table5826
+ GCC_except_table5828
+ GCC_except_table5830
+ GCC_except_table5834
+ GCC_except_table592
+ GCC_except_table596
+ GCC_except_table5979
+ GCC_except_table600
+ GCC_except_table6038
+ GCC_except_table6042
+ GCC_except_table6048
+ GCC_except_table6055
+ GCC_except_table6056
+ GCC_except_table6072
+ GCC_except_table6076
+ GCC_except_table6077
+ GCC_except_table6078
+ GCC_except_table609
+ GCC_except_table610
+ GCC_except_table6127
+ GCC_except_table6129
+ GCC_except_table6132
+ GCC_except_table6160
+ GCC_except_table6161
+ GCC_except_table6186
+ GCC_except_table6203
+ GCC_except_table6204
+ GCC_except_table6205
+ GCC_except_table621
+ GCC_except_table6213
+ GCC_except_table6218
+ GCC_except_table6219
+ GCC_except_table6220
+ GCC_except_table6234
+ GCC_except_table6237
+ GCC_except_table6243
+ GCC_except_table6249
+ GCC_except_table626
+ GCC_except_table6261
+ GCC_except_table6267
+ GCC_except_table6276
+ GCC_except_table6282
+ GCC_except_table6283
+ GCC_except_table6287
+ GCC_except_table6295
+ GCC_except_table6299
+ GCC_except_table630
+ GCC_except_table6301
+ GCC_except_table6305
+ GCC_except_table6326
+ GCC_except_table6328
+ GCC_except_table6329
+ GCC_except_table6355
+ GCC_except_table636
+ GCC_except_table637
+ GCC_except_table642
+ GCC_except_table643
+ GCC_except_table6519
+ GCC_except_table6582
+ GCC_except_table6614
+ GCC_except_table6617
+ GCC_except_table669
+ GCC_except_table6781
+ GCC_except_table682
+ GCC_except_table683
+ GCC_except_table6844
+ GCC_except_table6907
+ GCC_except_table6913
+ GCC_except_table6958
+ GCC_except_table6960
+ GCC_except_table6962
+ GCC_except_table6964
+ GCC_except_table6966
+ GCC_except_table6968
+ GCC_except_table6970
+ GCC_except_table6972
+ GCC_except_table6974
+ GCC_except_table6976
+ GCC_except_table6978
+ GCC_except_table6983
+ GCC_except_table6985
+ GCC_except_table6988
+ GCC_except_table7014
+ GCC_except_table7017
+ GCC_except_table7018
+ GCC_except_table7057
+ GCC_except_table7058
+ GCC_except_table7059
+ GCC_except_table7061
+ GCC_except_table7062
+ GCC_except_table7064
+ GCC_except_table7065
+ GCC_except_table7066
+ GCC_except_table7068
+ GCC_except_table7069
+ GCC_except_table7071
+ GCC_except_table7075
+ GCC_except_table7076
+ GCC_except_table7080
+ GCC_except_table7128
+ GCC_except_table7135
+ GCC_except_table717
+ GCC_except_table7229
+ GCC_except_table7245
+ GCC_except_table7247
+ GCC_except_table7249
+ GCC_except_table7252
+ GCC_except_table7254
+ GCC_except_table7256
+ GCC_except_table7258
+ GCC_except_table7259
+ GCC_except_table7261
+ GCC_except_table7265
+ GCC_except_table7270
+ GCC_except_table740
+ GCC_except_table759
+ GCC_except_table783
+ GCC_except_table787
+ GCC_except_table799
+ GCC_except_table804
+ GCC_except_table905
+ GCC_except_table907
+ _HAPAccessoryServerConnectionMethodToString
+ _HAPAccessoryServerDiscoveryMethod
+ _HAPAccessoryServerDiscoveryMethodToString
+ _OBJC_CLASS_$_HAPAccessoryServerBookkeeping
+ _OBJC_CLASS_$_HAPSocketInfo
+ _OBJC_IVAR_$_HAPAccessory._linkLayerType
+ _OBJC_IVAR_$_HAPAccessoryServerBookkeeping._connectionMethod
+ _OBJC_IVAR_$_HAPAccessoryServerBookkeeping._initialDiscoveryMethod
+ _OBJC_IVAR_$_HAPAccessoryServerBookkeeping._lastDiscoveryMethod
+ _OBJC_IVAR_$_HAPAccessoryServerBrowserIP._serverIdentifierToSkipBonjourUpdate
+ _OBJC_IVAR_$_HAPAccessoryServerIP._discoveryBookkeeping
+ _OBJC_IVAR_$_HAPAccessoryServerIP._pendingConnectionSocketInfo
+ _OBJC_IVAR_$_HAPHTTPClient._peerAddress
+ _OBJC_IVAR_$_HAPHTTPClient._pendingConnectionSocketInfo
+ _OBJC_IVAR_$_HAPSocketInfo._ipAddressString
+ _OBJC_IVAR_$_HAPSocketInfo._port
+ _OBJC_METACLASS_$_HAPAccessoryServerBookkeeping
+ _OBJC_METACLASS_$_HAPSocketInfo
+ _SockAddrGetPort
+ __CopyPairingIdentityDelegateCallback_f.14689
+ __CopyPairingIdentityDelegateCallback_f.21183
+ __CopyPairingIdentityDelegateCallback_f.2656
+ __FindPairedPeerDelegateCallback_f.2655
+ __OBJC_$_INSTANCE_METHODS_HAPAccessoryServerBookkeeping
+ __OBJC_$_INSTANCE_METHODS_HAPSocketInfo
+ __OBJC_$_INSTANCE_VARIABLES_HAPAccessoryServerBookkeeping
+ __OBJC_$_INSTANCE_VARIABLES_HAPSocketInfo
+ __OBJC_$_PROP_LIST_HAPAccessoryServerBookkeeping
+ __OBJC_$_PROP_LIST_HAPSocketInfo
+ __OBJC_CLASS_RO_$_HAPAccessoryServerBookkeeping
+ __OBJC_CLASS_RO_$_HAPSocketInfo
+ __OBJC_METACLASS_RO_$_HAPAccessoryServerBookkeeping
+ __OBJC_METACLASS_RO_$_HAPSocketInfo
+ __PairSetupPromptForSetupCodeDelegateCallback_f.21185
+ __SavePairedPeerDelegateCallback_f.14688
+ __SavePairedPeerDelegateCallback_f.21179
+ ___103-[_HAPAccessoryServerBTLE100 _handlePairingsReadForCharacteristic:readError:removing:queue:completion:]_block_invoke.336
+ ___108-[HAPAccessoryServerIP _handleWriteECONNResetError:writeRequests:responses:timeout:queue:completionHandler:]_block_invoke.248
+ ___113-[HAPAccessoryServerIP _handleReadECONNRESETError:readCharacteristics:responses:timeout:queue:completionHandler:]_block_invoke.195
+ ___41-[HAPAccessoryServerIP getAccessoryInfo:]_block_invoke.477
+ ___44-[HAPAccessoryServerIP _pairVerifyStartWAC:]_block_invoke.112
+ ___45-[HAPAccessoryServerIP _pairSetupContinueWAC]_block_invoke.110
+ ___45-[HAPAccessoryServerIP stopPairingWithError:]_block_invoke.150
+ ___45-[_HAPAccessoryServerBTLE100 _pairSetupStart]_block_invoke.321
+ ___47-[HAPAccessoryServerIP identifyWithCompletion:]_block_invoke.613
+ ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.114
+ ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.117
+ ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.119
+ ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke_2.115
+ ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke_2.118
+ ___48-[HAPAccessoryServerIP startPairingWithRequest:]_block_invoke.148
+ ___49-[HAPAccessoryServerIP _continuePairingAfterWAC:]_block_invoke.120
+ ___49-[HAPAccessoryServerIP _continuePairingAfterWAC:]_block_invoke.125
+ ___49-[HAPAccessoryServerIP authSession:authComplete:]_block_invoke.527
+ ___50-[HAPAccessoryServerIP networkMonitorIsReachable:]_block_invoke.472
+ ___53-[HAPAccessoryServerIP setPairVerifyCompletionBlock:]_block_invoke.406
+ ___55-[HAPAccessoryServerIP authSession:validateUUID:token:]_block_invoke.517
+ ___55-[HAPAccessoryServerIP authSession:validateUUID:token:]_block_invoke.522
+ ___55-[_HAPAccessoryServerBTLE200 authSession:authComplete:]_block_invoke.992
+ ___56-[HAPAccessoryServerBrowserBTLE updateScanInBackground:]_block_invoke
+ ___57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke.512
+ ___57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke_2.516
+ ___59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke.441
+ ___59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke_2.442
+ ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.419
+ ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.425
+ ___59-[_HAPAccessoryServerBTLE200 peripheral:didModifyServices:]_block_invoke.957
+ ___60-[HAPAccessoryServerIP _validatePairingAuthMethod:activity:]_block_invoke.496
+ ___63-[HAPAccessoryServerBrowserIP startDiscoveringAccessoryServers]_block_invoke.42
+ ___63-[HAPAccessoryServerIP updateWithBonjourDeviceInfo:socketInfo:]_block_invoke
+ ___63-[HAPAccessoryServerIP updateWithBonjourDeviceInfo:socketInfo:]_block_invoke_2
+ ___63-[HAPAccessoryServerIP updateWithBonjourDeviceInfo:socketInfo:]_block_invoke_3
+ ___63-[_HAPAccessoryServerBTLE100 _handlePairSetupExchangeWithData:]_block_invoke.322
+ ___63-[_HAPAccessoryServerBTLE200 authSession:sendAuthExchangeData:]_block_invoke.985
+ ___63-[_HAPAccessoryServerBTLE200 authSession:sendAuthExchangeData:]_block_invoke_2.988
+ ___64-[HAPAccessoryServerIP _updateWithBonjourDeviceInfo:socketInfo:]_block_invoke
+ ___64-[_HAPAccessoryServerBTLE200 securitySession:didCloseWithError:]_block_invoke.1010
+ ___65-[HAPAccessoryServerBrowserIP wacBrowser:didFindHAPWACAccessory:]_block_invoke.69
+ ___65-[HAPAccessoryServerIP _continuePairingAfterAuthPromptWithRetry:]_block_invoke.433
+ ___67-[HAPAccessoryServerBrowserIP wacBrowser:didRemoveHAPWACAccessory:]_block_invoke.70
+ ___75-[_HAPAccessoryServerBTLE100 peripheral:didUpdateValueForDescriptor:error:]_block_invoke.317
+ ___76-[HAPAccessoryServerBrowserIP unitTest_handleBonjourBrowserEvent:eventInfo:]_block_invoke
+ ___76-[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]_block_invoke.249
+ ___76-[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]_block_invoke_2.257
+ ___76-[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]_block_invoke_3.258
+ ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke.569
+ ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke.571
+ ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.570
+ ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.572
+ ___79-[HAPAccessoryServerIP _queueListPairingWithCompletionQueue:completionHandler:]_block_invoke.172
+ ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1190
+ ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1191
+ ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke_2.1192
+ ___81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke.259
+ ___81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke_2.260
+ ___81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke_3.261
+ ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.196
+ ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.201
+ ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.210
+ ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke_2.217
+ ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke_3.218
+ ___82-[_HAPAccessoryServerBTLE100 removePairingForCurrentControllerOnQueue:completion:]_block_invoke.344
+ ___82-[_HAPAccessoryServerBTLE100 removePairingForCurrentControllerOnQueue:completion:]_block_invoke.345
+ ___83-[HAPAccessoryServerBrowserIP wacBrowser:didFindUnconfiguredPairedHAPWACAccessory:]_block_invoke.73
+ ___83-[HAPAccessoryServerIP _writeCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.237
+ ___85-[HAPAccessoryServerIP _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.318
+ ___85-[HAPAccessoryServerIP _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.322
+ ___86-[HAPAccessoryServerBrowserIP handleConnectionUpdateWithBonjourDeviceInfo:socketInfo:]_block_invoke
+ ___86-[HAPAccessoryServerIP _establishSecureConnectionAndFetchAttributeDatabaseWithReason:]_block_invoke.146
+ ___86-[_HAPAccessoryServerBTLE100 _removePairingWithIdentifier:publicKey:queue:completion:]_block_invoke.343
+ ___87-[HAPAccessoryServerBrowserIP _handleConnectionUpdateWithBonjourDeviceInfo:socketInfo:]_block_invoke
+ ___88-[HAPAccessoryServerIP _queueAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.171
+ ___88-[HAPAccessoryServerIP _startAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.541
+ ___89-[_HAPAccessoryServerBTLE100 _addPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.333
+ ___90-[HAPAccessoryServerIP _queueEnableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.173
+ ___92-[HAPAccessoryServerIP writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.236
+ ___Block_byref_object_copy_.10225
+ ___Block_byref_object_copy_.10530
+ ___Block_byref_object_copy_.11343
+ ___Block_byref_object_copy_.11540
+ ___Block_byref_object_copy_.12562
+ ___Block_byref_object_copy_.13334
+ ___Block_byref_object_copy_.13561
+ ___Block_byref_object_copy_.14595
+ ___Block_byref_object_copy_.16544
+ ___Block_byref_object_copy_.16760
+ ___Block_byref_object_copy_.17774
+ ___Block_byref_object_copy_.18357
+ ___Block_byref_object_copy_.1922
+ ___Block_byref_object_copy_.19437
+ ___Block_byref_object_copy_.20261
+ ___Block_byref_object_copy_.24307
+ ___Block_byref_object_copy_.24472
+ ___Block_byref_object_copy_.2605
+ ___Block_byref_object_copy_.3996
+ ___Block_byref_object_copy_.4853
+ ___Block_byref_object_copy_.5091
+ ___Block_byref_object_copy_.5535
+ ___Block_byref_object_copy_.6195
+ ___Block_byref_object_copy_.6377
+ ___Block_byref_object_copy_.678
+ ___Block_byref_object_copy_.7233
+ ___Block_byref_object_copy_.8694
+ ___Block_byref_object_copy_.9008
+ ___Block_byref_object_copy_.9211
+ ___Block_byref_object_dispose_.10226
+ ___Block_byref_object_dispose_.10531
+ ___Block_byref_object_dispose_.11344
+ ___Block_byref_object_dispose_.11541
+ ___Block_byref_object_dispose_.12563
+ ___Block_byref_object_dispose_.13335
+ ___Block_byref_object_dispose_.13562
+ ___Block_byref_object_dispose_.14596
+ ___Block_byref_object_dispose_.16545
+ ___Block_byref_object_dispose_.16761
+ ___Block_byref_object_dispose_.17775
+ ___Block_byref_object_dispose_.18358
+ ___Block_byref_object_dispose_.1923
+ ___Block_byref_object_dispose_.19438
+ ___Block_byref_object_dispose_.20262
+ ___Block_byref_object_dispose_.24308
+ ___Block_byref_object_dispose_.24473
+ ___Block_byref_object_dispose_.2606
+ ___Block_byref_object_dispose_.3997
+ ___Block_byref_object_dispose_.4854
+ ___Block_byref_object_dispose_.5092
+ ___Block_byref_object_dispose_.5536
+ ___Block_byref_object_dispose_.6196
+ ___Block_byref_object_dispose_.6378
+ ___Block_byref_object_dispose_.679
+ ___Block_byref_object_dispose_.7234
+ ___Block_byref_object_dispose_.8695
+ ___Block_byref_object_dispose_.9009
+ ___Block_byref_object_dispose_.9212
+ ___block_literal_global.1019
+ ___block_literal_global.10581
+ ___block_literal_global.11339
+ ___block_literal_global.11708
+ ___block_literal_global.1208
+ ___block_literal_global.1245
+ ___block_literal_global.12823
+ ___block_literal_global.14713
+ ___block_literal_global.1511
+ ___block_literal_global.15140
+ ___block_literal_global.16280
+ ___block_literal_global.16553
+ ___block_literal_global.17936
+ ___block_literal_global.180
+ ___block_literal_global.1831
+ ___block_literal_global.19182
+ ___block_literal_global.19459
+ ___block_literal_global.19924
+ ___block_literal_global.20837
+ ___block_literal_global.22171
+ ___block_literal_global.22493
+ ___block_literal_global.24081
+ ___block_literal_global.24695
+ ___block_literal_global.2671
+ ___block_literal_global.4916
+ ___block_literal_global.5087
+ ___block_literal_global.5647
+ ___block_literal_global.6206
+ ___block_literal_global.6351
+ ___block_literal_global.740
+ ___block_literal_global.7495
+ ___block_literal_global.8380
+ ___block_literal_global.8778
+ ___block_literal_global.9321
+ ___block_literal_global.9910
+ __unnamed_array_storage.14725
+ __unnamed_array_storage.15744
+ __unnamed_array_storage.16284
+ __unnamed_array_storage.20758
+ _hkConfig.20821
+ _logCategory._hmf_once_t22
+ _logCategory._hmf_once_t399
+ _logCategory._hmf_once_t47
+ _logCategory._hmf_once_t49
+ _logCategory._hmf_once_v23
+ _logCategory._hmf_once_v400
+ _logCategory._hmf_once_v48
+ _logCategory._hmf_once_v50
+ _objc_msgSend$_handleConnectionUpdateWithBonjourDeviceInfo:socketInfo:
+ _objc_msgSend$_updateWithBonjourDeviceInfo:socketInfo:
+ _objc_msgSend$accessoryServer:didUpdateConnectionState:linkLayerType:bookkeeping:withError:
+ _objc_msgSend$discoveryBookkeeping
+ _objc_msgSend$getHttpClientPeerAddress:
+ _objc_msgSend$initWithBonjourDeviceInfo:keyStore:browser:discoveryMethod:
+ _objc_msgSend$initWithDiscoveryMethod:
+ _objc_msgSend$initWithIPAddressString:port:
+ _objc_msgSend$initWithKeyStore:browser:discoveryMethod:
+ _objc_msgSend$initWithSocket:
+ _objc_msgSend$initWithSocketInfo:eventsEnabled:queue:wakeAddress:
+ _objc_msgSend$ipAddressString
+ _objc_msgSend$peerSocketInfo
+ _objc_msgSend$pendingConnectionSocketInfo
+ _objc_msgSend$serverIdentifierToSkipBonjourUpdate
+ _objc_msgSend$setConnectionMethod:
+ _objc_msgSend$setLastDiscoveryMethod:
+ _objc_msgSend$setPendingConnectionSocketInfo:
+ _objc_msgSend$setScanInBackground:
+ _objc_msgSend$updateWithBonjourDeviceInfo:socketInfo:
+ _sharedInstance.onceToken.15139
- -[HAPAccessoryServerIP _updateWithBonjourDeviceInfo:]
- -[HAPAccessoryServerIP initWithBonjourDeviceInfo:keyStore:browser:]
- -[HAPAccessoryServerIP updateWithBonjourDeviceInfo:]
- GCC_except_table1006
- GCC_except_table1010
- GCC_except_table1023
- GCC_except_table1028
- GCC_except_table1037
- GCC_except_table1039
- GCC_except_table1041
- GCC_except_table1043
- GCC_except_table1169
- GCC_except_table1173
- GCC_except_table1175
- GCC_except_table1556
- GCC_except_table1559
- GCC_except_table1569
- GCC_except_table1581
- GCC_except_table1587
- GCC_except_table1592
- GCC_except_table1596
- GCC_except_table1606
- GCC_except_table1621
- GCC_except_table1625
- GCC_except_table1635
- GCC_except_table1779
- GCC_except_table1782
- GCC_except_table1784
- GCC_except_table1786
- GCC_except_table1797
- GCC_except_table1801
- GCC_except_table1804
- GCC_except_table1806
- GCC_except_table1809
- GCC_except_table1826
- GCC_except_table1829
- GCC_except_table1831
- GCC_except_table1833
- GCC_except_table1837
- GCC_except_table1840
- GCC_except_table1844
- GCC_except_table1846
- GCC_except_table1852
- GCC_except_table1854
- GCC_except_table1864
- GCC_except_table1883
- GCC_except_table1920
- GCC_except_table1926
- GCC_except_table2097
- GCC_except_table2126
- GCC_except_table2237
- GCC_except_table2245
- GCC_except_table2246
- GCC_except_table2247
- GCC_except_table2248
- GCC_except_table2249
- GCC_except_table2250
- GCC_except_table2279
- GCC_except_table2354
- GCC_except_table2366
- GCC_except_table2392
- GCC_except_table2400
- GCC_except_table2411
- GCC_except_table2425
- GCC_except_table2428
- GCC_except_table2433
- GCC_except_table2441
- GCC_except_table2447
- GCC_except_table2449
- GCC_except_table2630
- GCC_except_table2699
- GCC_except_table2721
- GCC_except_table2736
- GCC_except_table2748
- GCC_except_table2749
- GCC_except_table2757
- GCC_except_table2764
- GCC_except_table2772
- GCC_except_table2828
- GCC_except_table2831
- GCC_except_table2836
- GCC_except_table2838
- GCC_except_table2852
- GCC_except_table2866
- GCC_except_table2868
- GCC_except_table2872
- GCC_except_table2880
- GCC_except_table2888
- GCC_except_table2937
- GCC_except_table2945
- GCC_except_table2947
- GCC_except_table2948
- GCC_except_table2971
- GCC_except_table3199
- GCC_except_table3258
- GCC_except_table3259
- GCC_except_table3263
- GCC_except_table3266
- GCC_except_table3268
- GCC_except_table3269
- GCC_except_table3271
- GCC_except_table3272
- GCC_except_table3274
- GCC_except_table3281
- GCC_except_table3305
- GCC_except_table3308
- GCC_except_table3310
- GCC_except_table3313
- GCC_except_table3318
- GCC_except_table3321
- GCC_except_table3324
- GCC_except_table3336
- GCC_except_table3342
- GCC_except_table3350
- GCC_except_table3376
- GCC_except_table3394
- GCC_except_table3398
- GCC_except_table3403
- GCC_except_table3405
- GCC_except_table3520
- GCC_except_table3545
- GCC_except_table3632
- GCC_except_table3639
- GCC_except_table3657
- GCC_except_table3661
- GCC_except_table3664
- GCC_except_table3667
- GCC_except_table3673
- GCC_except_table3676
- GCC_except_table3679
- GCC_except_table3682
- GCC_except_table3685
- GCC_except_table3690
- GCC_except_table3715
- GCC_except_table3723
- GCC_except_table3727
- GCC_except_table3734
- GCC_except_table3739
- GCC_except_table3740
- GCC_except_table3760
- GCC_except_table3762
- GCC_except_table3763
- GCC_except_table3772
- GCC_except_table3775
- GCC_except_table3777
- GCC_except_table3783
- GCC_except_table3785
- GCC_except_table3788
- GCC_except_table3800
- GCC_except_table3811
- GCC_except_table3813
- GCC_except_table3822
- GCC_except_table3828
- GCC_except_table384
- GCC_except_table400
- GCC_except_table408
- GCC_except_table4088
- GCC_except_table4094
- GCC_except_table4111
- GCC_except_table4115
- GCC_except_table4132
- GCC_except_table4138
- GCC_except_table4151
- GCC_except_table4165
- GCC_except_table4272
- GCC_except_table4352
- GCC_except_table4360
- GCC_except_table4370
- GCC_except_table438
- GCC_except_table4404
- GCC_except_table4407
- GCC_except_table4408
- GCC_except_table4409
- GCC_except_table4410
- GCC_except_table445
- GCC_except_table4501
- GCC_except_table4502
- GCC_except_table4503
- GCC_except_table4504
- GCC_except_table4505
- GCC_except_table4506
- GCC_except_table4512
- GCC_except_table4513
- GCC_except_table4515
- GCC_except_table4522
- GCC_except_table4525
- GCC_except_table4527
- GCC_except_table4532
- GCC_except_table4535
- GCC_except_table4542
- GCC_except_table4546
- GCC_except_table4575
- GCC_except_table4576
- GCC_except_table459
- GCC_except_table4595
- GCC_except_table460
- GCC_except_table4605
- GCC_except_table4608
- GCC_except_table4613
- GCC_except_table4616
- GCC_except_table480
- GCC_except_table484
- GCC_except_table486
- GCC_except_table4877
- GCC_except_table4881
- GCC_except_table4915
- GCC_except_table4919
- GCC_except_table4921
- GCC_except_table4923
- GCC_except_table493
- GCC_except_table499
- GCC_except_table5076
- GCC_except_table5082
- GCC_except_table5086
- GCC_except_table5087
- GCC_except_table5088
- GCC_except_table5089
- GCC_except_table5095
- GCC_except_table5129
- GCC_except_table5131
- GCC_except_table5149
- GCC_except_table5161
- GCC_except_table5169
- GCC_except_table517
- GCC_except_table5171
- GCC_except_table5185
- GCC_except_table527
- GCC_except_table534
- GCC_except_table5384
- GCC_except_table5396
- GCC_except_table5401
- GCC_except_table5404
- GCC_except_table5405
- GCC_except_table5407
- GCC_except_table5408
- GCC_except_table5410
- GCC_except_table5462
- GCC_except_table5466
- GCC_except_table5470
- GCC_except_table5479
- GCC_except_table5483
- GCC_except_table5487
- GCC_except_table5491
- GCC_except_table5499
- GCC_except_table5503
- GCC_except_table5541
- GCC_except_table5568
- GCC_except_table5569
- GCC_except_table5570
- GCC_except_table5571
- GCC_except_table561
- GCC_except_table5629
- GCC_except_table5630
- GCC_except_table5644
- GCC_except_table565
- GCC_except_table5650
- GCC_except_table5663
- GCC_except_table5666
- GCC_except_table5667
- GCC_except_table567
- GCC_except_table5672
- GCC_except_table5675
- GCC_except_table5682
- GCC_except_table569
- GCC_except_table5699
- GCC_except_table5706
- GCC_except_table5712
- GCC_except_table5721
- GCC_except_table5723
- GCC_except_table5727
- GCC_except_table5728
- GCC_except_table5742
- GCC_except_table5744
- GCC_except_table575
- GCC_except_table5752
- GCC_except_table5767
- GCC_except_table5768
- GCC_except_table577
- GCC_except_table5773
- GCC_except_table5778
- GCC_except_table5781
- GCC_except_table5791
- GCC_except_table5793
- GCC_except_table5795
- GCC_except_table5799
- GCC_except_table589
- GCC_except_table593
- GCC_except_table5944
- GCC_except_table597
- GCC_except_table5998
- GCC_except_table6001
- GCC_except_table6005
- GCC_except_table6011
- GCC_except_table6018
- GCC_except_table6019
- GCC_except_table6039
- GCC_except_table6040
- GCC_except_table6041
- GCC_except_table606
- GCC_except_table607
- GCC_except_table6089
- GCC_except_table6090
- GCC_except_table6092
- GCC_except_table6095
- GCC_except_table612
- GCC_except_table6125
- GCC_except_table6131
- GCC_except_table6149
- GCC_except_table6167
- GCC_except_table6168
- GCC_except_table6176
- GCC_except_table6181
- GCC_except_table6182
- GCC_except_table6183
- GCC_except_table6197
- GCC_except_table6200
- GCC_except_table6206
- GCC_except_table6212
- GCC_except_table6224
- GCC_except_table6225
- GCC_except_table623
- GCC_except_table6230
- GCC_except_table6239
- GCC_except_table6245
- GCC_except_table6246
- GCC_except_table6250
- GCC_except_table6258
- GCC_except_table6264
- GCC_except_table6268
- GCC_except_table627
- GCC_except_table6289
- GCC_except_table6291
- GCC_except_table6292
- GCC_except_table6318
- GCC_except_table633
- GCC_except_table634
- GCC_except_table639
- GCC_except_table640
- GCC_except_table6482
- GCC_except_table6545
- GCC_except_table6577
- GCC_except_table6580
- GCC_except_table666
- GCC_except_table6744
- GCC_except_table677
- GCC_except_table678
- GCC_except_table6807
- GCC_except_table6870
- GCC_except_table6876
- GCC_except_table6921
- GCC_except_table6923
- GCC_except_table6925
- GCC_except_table6927
- GCC_except_table6929
- GCC_except_table6931
- GCC_except_table6933
- GCC_except_table6935
- GCC_except_table6937
- GCC_except_table6939
- GCC_except_table6941
- GCC_except_table6944
- GCC_except_table6946
- GCC_except_table6948
- GCC_except_table6951
- GCC_except_table6977
- GCC_except_table6980
- GCC_except_table7020
- GCC_except_table7021
- GCC_except_table7022
- GCC_except_table7024
- GCC_except_table7025
- GCC_except_table7027
- GCC_except_table7028
- GCC_except_table7029
- GCC_except_table7031
- GCC_except_table7032
- GCC_except_table7034
- GCC_except_table7038
- GCC_except_table7039
- GCC_except_table7043
- GCC_except_table7091
- GCC_except_table7098
- GCC_except_table712
- GCC_except_table7192
- GCC_except_table7208
- GCC_except_table7210
- GCC_except_table7212
- GCC_except_table7215
- GCC_except_table7217
- GCC_except_table7219
- GCC_except_table7221
- GCC_except_table7222
- GCC_except_table7224
- GCC_except_table7228
- GCC_except_table7233
- GCC_except_table735
- GCC_except_table754
- GCC_except_table778
- GCC_except_table782
- GCC_except_table793
- GCC_except_table798
- GCC_except_table898
- GCC_except_table900
- __CopyPairingIdentityDelegateCallback_f.14559
- __CopyPairingIdentityDelegateCallback_f.21087
- __CopyPairingIdentityDelegateCallback_f.2711
- __FindPairedPeerDelegateCallback_f.2710
- __PairSetupPromptForSetupCodeDelegateCallback_f.21089
- __SavePairedPeerDelegateCallback_f.14558
- __SavePairedPeerDelegateCallback_f.21083
- ___103-[_HAPAccessoryServerBTLE100 _handlePairingsReadForCharacteristic:readError:removing:queue:completion:]_block_invoke.333
- ___108-[HAPAccessoryServerIP _handleWriteECONNResetError:writeRequests:responses:timeout:queue:completionHandler:]_block_invoke.247
- ___113-[HAPAccessoryServerIP _handleReadECONNRESETError:readCharacteristics:responses:timeout:queue:completionHandler:]_block_invoke.194
- ___41-[HAPAccessoryServerIP getAccessoryInfo:]_block_invoke.476
- ___44-[HAPAccessoryServerIP _pairVerifyStartWAC:]_block_invoke.111
- ___45-[HAPAccessoryServerIP _pairSetupContinueWAC]_block_invoke.109
- ___45-[HAPAccessoryServerIP stopPairingWithError:]_block_invoke.149
- ___45-[_HAPAccessoryServerBTLE100 _pairSetupStart]_block_invoke.318
- ___47-[HAPAccessoryServerIP identifyWithCompletion:]_block_invoke.609
- ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.112
- ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.115
- ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.118
- ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke_2.114
- ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke_2.117
- ___48-[HAPAccessoryServerIP startPairingWithRequest:]_block_invoke.147
- ___49-[HAPAccessoryServerIP _continuePairingAfterWAC:]_block_invoke.119
- ___49-[HAPAccessoryServerIP _continuePairingAfterWAC:]_block_invoke.124
- ___49-[HAPAccessoryServerIP authSession:authComplete:]_block_invoke.526
- ___50-[HAPAccessoryServerIP networkMonitorIsReachable:]_block_invoke.471
- ___52-[HAPAccessoryServerIP updateWithBonjourDeviceInfo:]_block_invoke
- ___52-[HAPAccessoryServerIP updateWithBonjourDeviceInfo:]_block_invoke_2
- ___52-[HAPAccessoryServerIP updateWithBonjourDeviceInfo:]_block_invoke_3
- ___53-[HAPAccessoryServerIP _updateWithBonjourDeviceInfo:]_block_invoke
- ___53-[HAPAccessoryServerIP setPairVerifyCompletionBlock:]_block_invoke.405
- ___55-[HAPAccessoryServerIP authSession:validateUUID:token:]_block_invoke.516
- ___55-[HAPAccessoryServerIP authSession:validateUUID:token:]_block_invoke.521
- ___55-[_HAPAccessoryServerBTLE200 authSession:authComplete:]_block_invoke.989
- ___57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke.511
- ___57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke_2.515
- ___59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke.440
- ___59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke_2.441
- ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.418
- ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.423
- ___59-[_HAPAccessoryServerBTLE200 peripheral:didModifyServices:]_block_invoke.954
- ___60-[HAPAccessoryServerIP _validatePairingAuthMethod:activity:]_block_invoke.495
- ___63-[HAPAccessoryServerBrowserIP startDiscoveringAccessoryServers]_block_invoke.38
- ___63-[_HAPAccessoryServerBTLE100 _handlePairSetupExchangeWithData:]_block_invoke.319
- ___63-[_HAPAccessoryServerBTLE200 authSession:sendAuthExchangeData:]_block_invoke.982
- ___63-[_HAPAccessoryServerBTLE200 authSession:sendAuthExchangeData:]_block_invoke_2.985
- ___64-[_HAPAccessoryServerBTLE200 securitySession:didCloseWithError:]_block_invoke.1007
- ___65-[HAPAccessoryServerBrowserIP wacBrowser:didFindHAPWACAccessory:]_block_invoke.65
- ___65-[HAPAccessoryServerIP _continuePairingAfterAuthPromptWithRetry:]_block_invoke.432
- ___67-[HAPAccessoryServerBrowserIP wacBrowser:didRemoveHAPWACAccessory:]_block_invoke.66
- ___70-[HAPAccessoryServerBrowserIP _handleBonjourAddOrUpdateWithEventInfo:]_block_invoke
- ___75-[_HAPAccessoryServerBTLE100 peripheral:didUpdateValueForDescriptor:error:]_block_invoke.314
- ___76-[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]_block_invoke.248
- ___76-[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]_block_invoke_2.256
- ___76-[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]_block_invoke_3.257
- ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke.568
- ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke.570
- ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.569
- ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.571
- ___79-[HAPAccessoryServerIP _queueListPairingWithCompletionQueue:completionHandler:]_block_invoke.171
- ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1168
- ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1169
- ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke_2.1170
- ___81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke.258
- ___81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke_2.259
- ___81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke_3.260
- ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.195
- ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.200
- ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.209
- ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke_2.216
- ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke_3.217
- ___82-[_HAPAccessoryServerBTLE100 removePairingForCurrentControllerOnQueue:completion:]_block_invoke.341
- ___82-[_HAPAccessoryServerBTLE100 removePairingForCurrentControllerOnQueue:completion:]_block_invoke.342
- ___83-[HAPAccessoryServerBrowserIP wacBrowser:didFindUnconfiguredPairedHAPWACAccessory:]_block_invoke.69
- ___83-[HAPAccessoryServerIP _writeCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.236
- ___85-[HAPAccessoryServerIP _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.317
- ___85-[HAPAccessoryServerIP _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.321
- ___86-[HAPAccessoryServerIP _establishSecureConnectionAndFetchAttributeDatabaseWithReason:]_block_invoke.145
- ___86-[_HAPAccessoryServerBTLE100 _removePairingWithIdentifier:publicKey:queue:completion:]_block_invoke.340
- ___88-[HAPAccessoryServerIP _queueAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.170
- ___88-[HAPAccessoryServerIP _startAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.540
- ___89-[_HAPAccessoryServerBTLE100 _addPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.330
- ___90-[HAPAccessoryServerIP _queueEnableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.172
- ___92-[HAPAccessoryServerIP writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.235
- ___Block_byref_object_copy_.10106
- ___Block_byref_object_copy_.10410
- ___Block_byref_object_copy_.11226
- ___Block_byref_object_copy_.11423
- ___Block_byref_object_copy_.12446
- ___Block_byref_object_copy_.13206
- ___Block_byref_object_copy_.13432
- ___Block_byref_object_copy_.14466
- ___Block_byref_object_copy_.16429
- ___Block_byref_object_copy_.16645
- ___Block_byref_object_copy_.17660
- ___Block_byref_object_copy_.18243
- ___Block_byref_object_copy_.19324
- ___Block_byref_object_copy_.1983
- ___Block_byref_object_copy_.20147
- ___Block_byref_object_copy_.24207
- ___Block_byref_object_copy_.24372
- ___Block_byref_object_copy_.2659
- ___Block_byref_object_copy_.4046
- ___Block_byref_object_copy_.4862
- ___Block_byref_object_copy_.5096
- ___Block_byref_object_copy_.5542
- ___Block_byref_object_copy_.6176
- ___Block_byref_object_copy_.6358
- ___Block_byref_object_copy_.679
- ___Block_byref_object_copy_.7210
- ___Block_byref_object_copy_.8593
- ___Block_byref_object_copy_.8904
- ___Block_byref_object_copy_.9108
- ___Block_byref_object_dispose_.10107
- ___Block_byref_object_dispose_.10411
- ___Block_byref_object_dispose_.11227
- ___Block_byref_object_dispose_.11424
- ___Block_byref_object_dispose_.12447
- ___Block_byref_object_dispose_.13207
- ___Block_byref_object_dispose_.13433
- ___Block_byref_object_dispose_.14467
- ___Block_byref_object_dispose_.16430
- ___Block_byref_object_dispose_.16646
- ___Block_byref_object_dispose_.17661
- ___Block_byref_object_dispose_.18244
- ___Block_byref_object_dispose_.19325
- ___Block_byref_object_dispose_.1984
- ___Block_byref_object_dispose_.20148
- ___Block_byref_object_dispose_.24208
- ___Block_byref_object_dispose_.24373
- ___Block_byref_object_dispose_.2660
- ___Block_byref_object_dispose_.4047
- ___Block_byref_object_dispose_.4863
- ___Block_byref_object_dispose_.5097
- ___Block_byref_object_dispose_.5543
- ___Block_byref_object_dispose_.6177
- ___Block_byref_object_dispose_.6359
- ___Block_byref_object_dispose_.680
- ___Block_byref_object_dispose_.7211
- ___Block_byref_object_dispose_.8594
- ___Block_byref_object_dispose_.8905
- ___Block_byref_object_dispose_.9109
- ___block_literal_global.1016
- ___block_literal_global.10463
- ___block_literal_global.11222
- ___block_literal_global.11590
- ___block_literal_global.1186
- ___block_literal_global.1223
- ___block_literal_global.12692
- ___block_literal_global.14583
- ___block_literal_global.15010
- ___block_literal_global.1508
- ___block_literal_global.16156
- ___block_literal_global.16438
- ___block_literal_global.17822
- ___block_literal_global.179
- ___block_literal_global.1895
- ___block_literal_global.19069
- ___block_literal_global.19345
- ___block_literal_global.19808
- ___block_literal_global.20730
- ___block_literal_global.22071
- ___block_literal_global.22393
- ___block_literal_global.23981
- ___block_literal_global.24594
- ___block_literal_global.2726
- ___block_literal_global.4924
- ___block_literal_global.5092
- ___block_literal_global.5635
- ___block_literal_global.6187
- ___block_literal_global.6332
- ___block_literal_global.7467
- ___block_literal_global.759
- ___block_literal_global.8299
- ___block_literal_global.8677
- ___block_literal_global.9218
- ___block_literal_global.9792
- __unnamed_array_storage.14595
- __unnamed_array_storage.15617
- __unnamed_array_storage.16160
- __unnamed_array_storage.20651
- _hkConfig.20714
- _logCategory._hmf_once_t21
- _logCategory._hmf_once_t397
- _logCategory._hmf_once_t44
- _logCategory._hmf_once_t45
- _logCategory._hmf_once_v22
- _logCategory._hmf_once_v398
- _logCategory._hmf_once_v45
- _logCategory._hmf_once_v46
- _objc_msgSend$_updateWithBonjourDeviceInfo:
- _objc_msgSend$initWithBonjourDeviceInfo:keyStore:browser:
- _objc_msgSend$initWithKeyStore:browser:
- _objc_msgSend$updateWithBonjourDeviceInfo:
- _sharedInstance.onceToken.15009
CStrings:
+ "\x01\x11\x13B"
+ "\x11\x17"
+ "%{public}@*** Skipping bonjour add for %@.  Remove HAPServerIPBrowserSkipBonjourUpdateForIdentifier from preferences to clear"
+ "%{public}@Could not initialize socket info from dictionary: %@"
+ "%{public}@Creating socket connection using ipAddress %@"
+ "%{public}@Failed to initialize HAPSocketInfo: failed to obtain socket address string: %d"
+ "%{public}@Failed to initialize HAPSocketInfo: invalid socket address family: %d"
+ "%{public}@Saving socket info"
+ "%{public}@Saving socket info for newly discovered server %@"
+ "%{public}@Skipping bonjour updates for server with identifier: %@"
+ "@\"HAPAccessoryServerBookkeeping\""
+ "@\"HAPSocketInfo\""
+ "@\"HMFNetAddress\""
+ "@24@0:8r^{sockaddr_storage=CC[6c]q[112c]}16"
+ "@44@0:8@16B24@28@36"
+ "Bonjour Update"
+ "DNS Name"
+ "HAPAccessoryServerBookkeeping"
+ "HAPServerIPBrowserServerIdentifierToSkipBonjourUpdates"
+ "HAPSocketInfo"
+ "HAPSocketInfoIPAddressString"
+ "HAPSocketInfoPort"
+ "IP Address"
+ "Keystore"
+ "No Connection"
+ "Simulated Bonjour Update"
+ "T@\"HAPAccessoryServerBookkeeping\",&,N,V_discoveryBookkeeping"
+ "T@\"HAPSocketInfo\",&,N,V_pendingConnectionSocketInfo"
+ "T@\"HAPSocketInfo\",R,N"
+ "T@\"HAPSocketInfo\",R,N,V_pendingConnectionSocketInfo"
+ "T@\"HMFNetAddress\",R,N,V_peerAddress"
+ "T@\"NSDictionary\",R,C"
+ "T@\"NSNumber\",R,N,V_port"
+ "T@\"NSString\",&,N,V_serverIdentifierToSkipBonjourUpdate"
+ "T@\"NSString\",R,N,V_ipAddressString"
+ "TB,V_scanInBackground"
+ "TQ,N,V_connectionMethod"
+ "TQ,N,V_lastDiscoveryMethod"
+ "TQ,R,N,V_initialDiscoveryMethod"
+ "Tq,N,V_linkLayerType"
+ "WAC"
+ "_connectionMethod"
+ "_discoveryBookkeeping"
+ "_handleConnectionUpdateWithBonjourDeviceInfo:socketInfo:"
+ "_initialDiscoveryMethod"
+ "_ipAddressString"
+ "_lastDiscoveryMethod"
+ "_peerAddress"
+ "_pendingConnectionSocketInfo"
+ "_serverIdentifierToSkipBonjourUpdate"
+ "_updateWithBonjourDeviceInfo:socketInfo:"
+ "accessoryServer:didUpdateConnectionState:linkLayerType:bookkeeping:withError:"
+ "connectionMethod"
+ "currentSocketInfo"
+ "dictionaryRepresentation"
+ "discoveryBookkeeping"
+ "dns:%@(%tu)%@"
+ "e*"
+ "getHttpClientPeerAddress:"
+ "handleConnectionUpdateWithBonjourDeviceInfo:socketInfo:"
+ "i24@0:8^{sockaddr_storage=CC[6c]q[112c]}16"
+ "initWithActiveOperationalDataSet:"
+ "initWithBonjourDeviceInfo:keyStore:browser:discoveryMethod:"
+ "initWithDiscoveryMethod:"
+ "initWithIPAddressString:port:"
+ "initWithKeyStore:browser:discoveryMethod:"
+ "initWithSocket:"
+ "initWithSocketInfo:eventsEnabled:queue:wakeAddress:"
+ "initialDiscoveryMethod"
+ "ip:%@(%tu)%@"
+ "ipAddressString"
+ "lastDiscoveryMethod"
+ "peerSocketInfo"
+ "pendingConnectionSocketInfo"
+ "serverIdentifierToSkipBonjourUpdate"
+ "setConnectionMethod:"
+ "setDiscoveryBookkeeping:"
+ "setLastDiscoveryMethod:"
+ "setLinkLayerType:"
+ "setPendingConnectionSocketInfo:"
+ "setServerIdentifierToSkipBonjourUpdate:"
+ "t"
+ "updateScanInBackground:"
+ "updateWithBonjourDeviceInfo:socketInfo:"
+ "v52@0:8@\"HAPAccessoryServer\"16B24q28@\"HAPAccessoryServerBookkeeping\"36@\"NSError\"44"
+ "v52@0:8@16B24q28@36@44"
+ "\x83\"\x14]\x12"
+ "\xf0\x91"
- "\x01\x11\x12A"
- "\x11\x16"
- "%@(%tu)%@"
- "TB,N,V_scanInBackground"
- "U*"
- "_updateWithBonjourDeviceInfo:"
- "initWithBonjourDeviceInfo:keyStore:browser:"
- "updateWithBonjourDeviceInfo:"
- "\x83\"\x12]\x12"
- "\xf0q"

```
