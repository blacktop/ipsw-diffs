## CoreHAP

> `/System/Library/PrivateFrameworks/CoreHAP.framework/CoreHAP`

```diff

-1092.4.10.0.0
-  __TEXT.__text: 0x1982ac
-  __TEXT.__auth_stubs: 0x1560
-  __TEXT.__objc_methlist: 0x116c4
+1124.5.8.1.1
+  __TEXT.__text: 0x1a25e8
+  __TEXT.__auth_stubs: 0x1550
+  __TEXT.__objc_methlist: 0x1194c
   __TEXT.__const: 0x5e0
-  __TEXT.__gcc_except_tab: 0x4784
-  __TEXT.__cstring: 0xfdc3
-  __TEXT.__oslogstring: 0x1f2e5
+  __TEXT.__gcc_except_tab: 0x4898
+  __TEXT.__cstring: 0xfe2c
+  __TEXT.__oslogstring: 0x1f7e9
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__unwind_info: 0x5c40
-  __TEXT.__objc_classname: 0x2dfa
-  __TEXT.__objc_methname: 0x25bea
-  __TEXT.__objc_methtype: 0x8e8d
-  __TEXT.__objc_stubs: 0x17e60
+  __TEXT.__unwind_info: 0x5d90
+  __TEXT.__objc_classname: 0x2e1c
+  __TEXT.__objc_methname: 0x262ce
+  __TEXT.__objc_methtype: 0x8ec2
+  __TEXT.__objc_stubs: 0x18240
   __DATA_CONST.__got: 0x2d0
-  __DATA_CONST.__const: 0x5330
-  __DATA_CONST.__objc_classlist: 0x960
+  __DATA_CONST.__const: 0x53a8
+  __DATA_CONST.__objc_classlist: 0x968
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x330
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1c000
-  __DATA_CONST.__objc_selrefs: 0x6b68
+  __DATA_CONST.__objc_const: 0x1c350
+  __DATA_CONST.__objc_selrefs: 0x6ca0
+  __DATA_CONST.__objc_protorefs: 0xc0
+  __DATA_CONST.__objc_classrefs: 0xad0
+  __DATA_CONST.__objc_superrefs: 0x7f0
   __DATA_CONST.__objc_arraydata: 0x208
-  __AUTH_CONST.__cfstring: 0xd360
-  __AUTH_CONST.__const: 0x7c0
-  __AUTH_CONST.__objc_const: 0x9028
-  __AUTH_CONST.__objc_intobj: 0x660
+  __AUTH_CONST.__cfstring: 0xd3e0
+  __AUTH_CONST.__const: 0x7e0
+  __AUTH_CONST.__objc_const: 0x90b8
+  __AUTH_CONST.__objc_intobj: 0x678
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0xd8
-  __AUTH_CONST.__auth_got: 0xac0
-  __AUTH.__objc_data: 0x51e0
-  __DATA.__objc_protorefs: 0xc0
-  __DATA.__objc_classrefs: 0xac8
-  __DATA.__objc_superrefs: 0x7e8
-  __DATA.__objc_ivar: 0x14a0
+  __AUTH_CONST.__auth_got: 0xab8
+  __AUTH.__objc_data: 0x5230
+  __DATA.__objc_ivar: 0x14dc
   __DATA.__data: 0x267a
   __DATA.__bss: 0x4b1
   __DATA_DIRTY.__objc_data: 0xbe0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 93A3DBB6-199A-37F1-AA45-532CDA8F791C
-  Functions: 7412
-  Symbols:   23991
-  CStrings:  12639
+  UUID: EE4FB855-4EC7-3B46-BD99-175D25DB4EFE
+  Functions: 7474
+  Symbols:   24174
+  CStrings:  12742
 
Symbols:
+ +[HAPMetadata currentMetadataHook]
+ +[HAPSocketInfo shortDescription]
+ -[HAPAccessoryServer metric_pairVerifyConnectionEstablishedBy]
+ -[HAPAccessoryServer requestWaitForResidentToSignalAccessorySetup]
+ -[HAPAccessoryServer setMetric_pairVerifyConnectionEstablishedBy:]
+ -[HAPAccessoryServerBrowserIP _doBonjourRemoveWithServer:]
+ -[HAPAccessoryServerBrowserIP maximumNumberOfPairVeifiesAllowed]
+ -[HAPAccessoryServerBrowserIP maximumPairVerifyFailureCount]
+ -[HAPAccessoryServerIP _incrementPairVerifyFailureCount]
+ -[HAPAccessoryServerIP _pollAccessory]
+ -[HAPAccessoryServerIP _startReachabilityEventTimer]
+ -[HAPAccessoryServerIP cachedSocketInfo]
+ -[HAPAccessoryServerIP consecutivePairVerifyFailures]
+ -[HAPAccessoryServerIP nameResolutionCompletionBlocks]
+ -[HAPAccessoryServerIP nameResolver]
+ -[HAPAccessoryServerIP resetPairVerifyFailureCount]
+ -[HAPAccessoryServerIP setCachedSocketInfo:]
+ -[HAPAccessoryServerIP setConsecutivePairVerifyFailures:]
+ -[HAPAccessoryServerIP setNameResolutionCompletionBlocks:]
+ -[HAPAccessoryServerIP setNameResolver:]
+ -[HAPAccessoryServerIP(NameResolution) _cancelNameResolution]
+ -[HAPAccessoryServerIP(NameResolution) _doResolveWithCompletion:]
+ -[HAPMetricsPairVerifyEvent connectionEstablishedUsing]
+ -[HAPMetricsPairVerifyEvent initWithAccessory:forLinkType:durationInMS:reason:connectionEstablishedUsing:pvError:]
+ -[HAPNameResolver .cxx_destruct]
+ -[HAPNameResolver _doCompletionWithErrorCode:socketInfo:state:]
+ -[HAPNameResolver _doCompletionWithErrorCode:state:]
+ -[HAPNameResolver _doCompletionWithSocketInfo:]
+ -[HAPNameResolver cancelTimer]
+ -[HAPNameResolver completion]
+ -[HAPNameResolver connection]
+ -[HAPNameResolver domain]
+ -[HAPNameResolver initWithDeviceName:serviceType:domain:workQueue:]
+ -[HAPNameResolver invalidate]
+ -[HAPNameResolver name]
+ -[HAPNameResolver nwConnnectionStart]
+ -[HAPNameResolver nwCreateConnection]
+ -[HAPNameResolver resolutionState]
+ -[HAPNameResolver resolveTCPNameWithTimeoutInSeconds:completion:]
+ -[HAPNameResolver serviceType]
+ -[HAPNameResolver setCompletion:]
+ -[HAPNameResolver setConnection:]
+ -[HAPNameResolver setDomain:]
+ -[HAPNameResolver setName:]
+ -[HAPNameResolver setResolutionState:]
+ -[HAPNameResolver setServiceType:]
+ -[HAPNameResolver setStateChangedHandler]
+ -[HAPNameResolver setTimer:]
+ -[HAPNameResolver setWorkQueue:]
+ -[HAPNameResolver startTimerWithTimeoutInSeconds:]
+ -[HAPNameResolver timerDidFire:]
+ -[HAPNameResolver timer]
+ -[HAPNameResolver workQueue]
+ -[HAPSocketInfo hash]
+ -[HAPSocketInfo isEqual:]
+ -[HAPSocketInfo shortDescription]
+ GCC_except_table1025
+ GCC_except_table1029
+ GCC_except_table1042
+ GCC_except_table1047
+ GCC_except_table1056
+ GCC_except_table1058
+ GCC_except_table1060
+ GCC_except_table1062
+ GCC_except_table1188
+ GCC_except_table1192
+ GCC_except_table1194
+ GCC_except_table1405
+ GCC_except_table1609
+ GCC_except_table1612
+ GCC_except_table1620
+ GCC_except_table1628
+ GCC_except_table1630
+ GCC_except_table1634
+ GCC_except_table1638
+ GCC_except_table1640
+ GCC_except_table1645
+ GCC_except_table1649
+ GCC_except_table1659
+ GCC_except_table1667
+ GCC_except_table1674
+ GCC_except_table1678
+ GCC_except_table1682
+ GCC_except_table1686
+ GCC_except_table1688
+ GCC_except_table1840
+ GCC_except_table1843
+ GCC_except_table1858
+ GCC_except_table1867
+ GCC_except_table1887
+ GCC_except_table1890
+ GCC_except_table1892
+ GCC_except_table1894
+ GCC_except_table1898
+ GCC_except_table1901
+ GCC_except_table1905
+ GCC_except_table1907
+ GCC_except_table1910
+ GCC_except_table1913
+ GCC_except_table1915
+ GCC_except_table1917
+ GCC_except_table1921
+ GCC_except_table1925
+ GCC_except_table1933
+ GCC_except_table1944
+ GCC_except_table1981
+ GCC_except_table1987
+ GCC_except_table2158
+ GCC_except_table2187
+ GCC_except_table2298
+ GCC_except_table2306
+ GCC_except_table2307
+ GCC_except_table2308
+ GCC_except_table2309
+ GCC_except_table2310
+ GCC_except_table2311
+ GCC_except_table2326
+ GCC_except_table2340
+ GCC_except_table2417
+ GCC_except_table2455
+ GCC_except_table2463
+ GCC_except_table2474
+ GCC_except_table2488
+ GCC_except_table2491
+ GCC_except_table2496
+ GCC_except_table2504
+ GCC_except_table2510
+ GCC_except_table2512
+ GCC_except_table2693
+ GCC_except_table2759
+ GCC_except_table2762
+ GCC_except_table2784
+ GCC_except_table2799
+ GCC_except_table2811
+ GCC_except_table2812
+ GCC_except_table2820
+ GCC_except_table2827
+ GCC_except_table2830
+ GCC_except_table2835
+ GCC_except_table2891
+ GCC_except_table2894
+ GCC_except_table2899
+ GCC_except_table2901
+ GCC_except_table2915
+ GCC_except_table2929
+ GCC_except_table2931
+ GCC_except_table2935
+ GCC_except_table2943
+ GCC_except_table2951
+ GCC_except_table3000
+ GCC_except_table3008
+ GCC_except_table3010
+ GCC_except_table3011
+ GCC_except_table3034
+ GCC_except_table3273
+ GCC_except_table3332
+ GCC_except_table3337
+ GCC_except_table3340
+ GCC_except_table3342
+ GCC_except_table3345
+ GCC_except_table3348
+ GCC_except_table3355
+ GCC_except_table3365
+ GCC_except_table3368
+ GCC_except_table3379
+ GCC_except_table3380
+ GCC_except_table3382
+ GCC_except_table3384
+ GCC_except_table3387
+ GCC_except_table3390
+ GCC_except_table3392
+ GCC_except_table3395
+ GCC_except_table3398
+ GCC_except_table3410
+ GCC_except_table3412
+ GCC_except_table3416
+ GCC_except_table3420
+ GCC_except_table3424
+ GCC_except_table3450
+ GCC_except_table3468
+ GCC_except_table3472
+ GCC_except_table3475
+ GCC_except_table3477
+ GCC_except_table3479
+ GCC_except_table3598
+ GCC_except_table3624
+ GCC_except_table3715
+ GCC_except_table3722
+ GCC_except_table3740
+ GCC_except_table3744
+ GCC_except_table3747
+ GCC_except_table3750
+ GCC_except_table3753
+ GCC_except_table3756
+ GCC_except_table3759
+ GCC_except_table3762
+ GCC_except_table3768
+ GCC_except_table3773
+ GCC_except_table3784
+ GCC_except_table3787
+ GCC_except_table3798
+ GCC_except_table3810
+ GCC_except_table3817
+ GCC_except_table3818
+ GCC_except_table3822
+ GCC_except_table3823
+ GCC_except_table3841
+ GCC_except_table3843
+ GCC_except_table3845
+ GCC_except_table3846
+ GCC_except_table3849
+ GCC_except_table3855
+ GCC_except_table3858
+ GCC_except_table3860
+ GCC_except_table3866
+ GCC_except_table3868
+ GCC_except_table3871
+ GCC_except_table3883
+ GCC_except_table3894
+ GCC_except_table3896
+ GCC_except_table3905
+ GCC_except_table3911
+ GCC_except_table397
+ GCC_except_table413
+ GCC_except_table4171
+ GCC_except_table4177
+ GCC_except_table4194
+ GCC_except_table4198
+ GCC_except_table421
+ GCC_except_table4215
+ GCC_except_table4221
+ GCC_except_table4234
+ GCC_except_table4248
+ GCC_except_table4252
+ GCC_except_table4355
+ GCC_except_table4435
+ GCC_except_table4453
+ GCC_except_table4489
+ GCC_except_table4492
+ GCC_except_table4493
+ GCC_except_table4494
+ GCC_except_table4495
+ GCC_except_table451
+ GCC_except_table458
+ GCC_except_table4588
+ GCC_except_table4589
+ GCC_except_table4590
+ GCC_except_table4591
+ GCC_except_table4592
+ GCC_except_table4593
+ GCC_except_table4599
+ GCC_except_table4600
+ GCC_except_table4602
+ GCC_except_table4609
+ GCC_except_table4612
+ GCC_except_table4614
+ GCC_except_table4619
+ GCC_except_table4622
+ GCC_except_table4625
+ GCC_except_table4629
+ GCC_except_table4633
+ GCC_except_table4662
+ GCC_except_table4663
+ GCC_except_table4682
+ GCC_except_table4692
+ GCC_except_table4695
+ GCC_except_table4700
+ GCC_except_table4703
+ GCC_except_table472
+ GCC_except_table473
+ GCC_except_table475
+ GCC_except_table478
+ GCC_except_table481
+ GCC_except_table493
+ GCC_except_table4965
+ GCC_except_table4969
+ GCC_except_table497
+ GCC_except_table499
+ GCC_except_table5003
+ GCC_except_table5007
+ GCC_except_table5009
+ GCC_except_table5011
+ GCC_except_table506
+ GCC_except_table512
+ GCC_except_table5172
+ GCC_except_table5176
+ GCC_except_table5177
+ GCC_except_table5178
+ GCC_except_table5179
+ GCC_except_table5185
+ GCC_except_table5219
+ GCC_except_table5221
+ GCC_except_table5239
+ GCC_except_table5251
+ GCC_except_table5254
+ GCC_except_table5259
+ GCC_except_table5261
+ GCC_except_table5275
+ GCC_except_table540
+ GCC_except_table547
+ GCC_except_table5476
+ GCC_except_table5488
+ GCC_except_table5493
+ GCC_except_table5496
+ GCC_except_table5499
+ GCC_except_table5500
+ GCC_except_table5502
+ GCC_except_table5532
+ GCC_except_table5554
+ GCC_except_table5558
+ GCC_except_table5562
+ GCC_except_table5567
+ GCC_except_table5571
+ GCC_except_table5575
+ GCC_except_table5579
+ GCC_except_table5583
+ GCC_except_table5591
+ GCC_except_table5593
+ GCC_except_table5595
+ GCC_except_table5637
+ GCC_except_table5666
+ GCC_except_table5667
+ GCC_except_table5725
+ GCC_except_table5726
+ GCC_except_table574
+ GCC_except_table5740
+ GCC_except_table5746
+ GCC_except_table5759
+ GCC_except_table5768
+ GCC_except_table5771
+ GCC_except_table5778
+ GCC_except_table5781
+ GCC_except_table5795
+ GCC_except_table5817
+ GCC_except_table5819
+ GCC_except_table582
+ GCC_except_table5823
+ GCC_except_table5824
+ GCC_except_table5838
+ GCC_except_table5840
+ GCC_except_table5848
+ GCC_except_table5863
+ GCC_except_table5864
+ GCC_except_table5869
+ GCC_except_table5873
+ GCC_except_table5874
+ GCC_except_table5877
+ GCC_except_table588
+ GCC_except_table5883
+ GCC_except_table5887
+ GCC_except_table5889
+ GCC_except_table5891
+ GCC_except_table5895
+ GCC_except_table590
+ GCC_except_table602
+ GCC_except_table6040
+ GCC_except_table606
+ GCC_except_table6096
+ GCC_except_table6099
+ GCC_except_table6103
+ GCC_except_table6109
+ GCC_except_table6116
+ GCC_except_table6117
+ GCC_except_table6133
+ GCC_except_table6137
+ GCC_except_table6138
+ GCC_except_table6139
+ GCC_except_table6187
+ GCC_except_table6188
+ GCC_except_table619
+ GCC_except_table6190
+ GCC_except_table6193
+ GCC_except_table620
+ GCC_except_table6221
+ GCC_except_table6222
+ GCC_except_table6227
+ GCC_except_table6247
+ GCC_except_table625
+ GCC_except_table6264
+ GCC_except_table6265
+ GCC_except_table6266
+ GCC_except_table6274
+ GCC_except_table6279
+ GCC_except_table628
+ GCC_except_table6280
+ GCC_except_table6281
+ GCC_except_table6298
+ GCC_except_table6304
+ GCC_except_table631
+ GCC_except_table6310
+ GCC_except_table6322
+ GCC_except_table6323
+ GCC_except_table6337
+ GCC_except_table6343
+ GCC_except_table6344
+ GCC_except_table6348
+ GCC_except_table6356
+ GCC_except_table6360
+ GCC_except_table6362
+ GCC_except_table6366
+ GCC_except_table6387
+ GCC_except_table6389
+ GCC_except_table6390
+ GCC_except_table640
+ GCC_except_table6416
+ GCC_except_table646
+ GCC_except_table647
+ GCC_except_table652
+ GCC_except_table653
+ GCC_except_table6580
+ GCC_except_table6643
+ GCC_except_table6675
+ GCC_except_table6678
+ GCC_except_table679
+ GCC_except_table6842
+ GCC_except_table6905
+ GCC_except_table693
+ GCC_except_table694
+ GCC_except_table7019
+ GCC_except_table7021
+ GCC_except_table7023
+ GCC_except_table7025
+ GCC_except_table7027
+ GCC_except_table7029
+ GCC_except_table7031
+ GCC_except_table7033
+ GCC_except_table7035
+ GCC_except_table7037
+ GCC_except_table7039
+ GCC_except_table7042
+ GCC_except_table7044
+ GCC_except_table7046
+ GCC_except_table7049
+ GCC_except_table7078
+ GCC_except_table7079
+ GCC_except_table7118
+ GCC_except_table7119
+ GCC_except_table7120
+ GCC_except_table7122
+ GCC_except_table7123
+ GCC_except_table7125
+ GCC_except_table7126
+ GCC_except_table7127
+ GCC_except_table7129
+ GCC_except_table7130
+ GCC_except_table7132
+ GCC_except_table7136
+ GCC_except_table7137
+ GCC_except_table7141
+ GCC_except_table7189
+ GCC_except_table7196
+ GCC_except_table728
+ GCC_except_table7290
+ GCC_except_table7306
+ GCC_except_table7308
+ GCC_except_table7310
+ GCC_except_table7313
+ GCC_except_table7315
+ GCC_except_table7317
+ GCC_except_table7319
+ GCC_except_table7320
+ GCC_except_table7322
+ GCC_except_table7326
+ GCC_except_table7331
+ GCC_except_table751
+ GCC_except_table771
+ GCC_except_table795
+ GCC_except_table811
+ GCC_except_table816
+ GCC_except_table917
+ GCC_except_table919
+ _OBJC_CLASS_$_HAPNameResolver
+ _OBJC_IVAR_$_HAPAccessoryServer._metric_pairVerifyConnectionEstablishedBy
+ _OBJC_IVAR_$_HAPAccessoryServerBrowserIP._maximumNumberOfPairVeifiesAllowed
+ _OBJC_IVAR_$_HAPAccessoryServerIP._cachedSocketInfo
+ _OBJC_IVAR_$_HAPAccessoryServerIP._consecutivePairVerifyFailures
+ _OBJC_IVAR_$_HAPAccessoryServerIP._nameResolutionCompletionBlocks
+ _OBJC_IVAR_$_HAPAccessoryServerIP._nameResolver
+ _OBJC_IVAR_$_HAPMetricsPairVerifyEvent._connectionEstablishedUsing
+ _OBJC_IVAR_$_HAPNameResolver._completion
+ _OBJC_IVAR_$_HAPNameResolver._connection
+ _OBJC_IVAR_$_HAPNameResolver._domain
+ _OBJC_IVAR_$_HAPNameResolver._lock
+ _OBJC_IVAR_$_HAPNameResolver._name
+ _OBJC_IVAR_$_HAPNameResolver._resolutionState
+ _OBJC_IVAR_$_HAPNameResolver._serviceType
+ _OBJC_IVAR_$_HAPNameResolver._timer
+ _OBJC_IVAR_$_HAPNameResolver._workQueue
+ _OBJC_METACLASS_$_HAPNameResolver
+ __CopyPairingIdentityDelegateCallback_f.14937
+ __CopyPairingIdentityDelegateCallback_f.21488
+ __CopyPairingIdentityDelegateCallback_f.2710
+ __FindPairedPeerDelegateCallback_f.2709
+ __OBJC_$_CLASS_METHODS_HAPAccessoryServerIP(HTTPActivity|SessionRestore|Metrics|NameResolution)
+ __OBJC_$_CLASS_METHODS_HAPSocketInfo
+ __OBJC_$_CLASS_PROP_LIST_HAPMetadata
+ __OBJC_$_INSTANCE_METHODS_HAPAccessoryServerIP(HTTPActivity|SessionRestore|Metrics|NameResolution)
+ __OBJC_$_INSTANCE_METHODS_HAPNameResolver
+ __OBJC_$_INSTANCE_VARIABLES_HAPNameResolver
+ __OBJC_$_PROP_LIST_HAP2Accessory.289
+ __OBJC_$_PROP_LIST_HAP2AccessoryServerBrowser.399
+ __OBJC_$_PROP_LIST_HAP2AccessoryServerCoordinator.182
+ __OBJC_$_PROP_LIST_HAP2AccessoryServerMetadata.103
+ __OBJC_$_PROP_LIST_HAP2CoAPClient.224
+ __OBJC_$_PROP_LIST_HAP2EncodedCharacteristicEvent.70
+ __OBJC_$_PROP_LIST_HAP2EncodedCharacteristicResponse.58
+ __OBJC_$_PROP_LIST_HAP2EncodedEnableNotificationResponse.67
+ __OBJC_$_PROP_LIST_HAPAccessoryReachabilityClient.201
+ __OBJC_$_PROP_LIST_HAPAccessoryReachabilityProfile.98
+ __OBJC_$_PROP_LIST_HAPNameResolver
+ __OBJC_CLASS_PROTOCOLS_$_HAPNameResolver
+ __OBJC_CLASS_RO_$_HAPNameResolver
+ __OBJC_METACLASS_RO_$_HAPNameResolver
+ __PairSetupPromptForSetupCodeDelegateCallback_f.21490
+ __SavePairedPeerDelegateCallback_f.14936
+ __SavePairedPeerDelegateCallback_f.21483
+ ___103-[_HAPAccessoryServerBTLE100 _handlePairingsReadForCharacteristic:readError:removing:queue:completion:]_block_invoke.337
+ ___108-[HAP2AccessoryServerController _removePairingCompletionWithIdentity:cleanupLocalData:operation:completion:]_block_invoke.268
+ ___108-[HAPAccessoryServerIP _handleWriteECONNResetError:writeRequests:responses:timeout:queue:completionHandler:]_block_invoke.250
+ ___113-[HAPAccessoryServerIP _handleReadECONNRESETError:readCharacteristics:responses:timeout:queue:completionHandler:]_block_invoke.197
+ ___29-[HAPNameResolver invalidate]_block_invoke
+ ___37-[HAPNameResolver nwCreateConnection]_block_invoke
+ ___41-[HAPAccessoryServerIP getAccessoryInfo:]_block_invoke.486
+ ___41-[HAPNameResolver setStateChangedHandler]_block_invoke
+ ___44-[HAPAccessoryServerIP _pairVerifyStartWAC:]_block_invoke.114
+ ___44-[HAPAccessoryServerIP setCachedSocketInfo:]_block_invoke
+ ___45-[HAP2AccessoryServerController closeSession]_block_invoke.286
+ ___45-[HAP2AccessoryServerController closeSession]_block_invoke.290
+ ___45-[HAPAccessoryServerIP _pairSetupContinueWAC]_block_invoke.112
+ ___45-[HAPAccessoryServerIP stopPairingWithError:]_block_invoke.152
+ ___45-[_HAPAccessoryServerBTLE100 _pairSetupStart]_block_invoke.322
+ ___47-[HAPAccessoryServerIP identifyWithCompletion:]_block_invoke.614
+ ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.115
+ ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.118
+ ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.121
+ ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke_2.117
+ ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke_2.120
+ ___48-[HAPAccessoryServerIP startPairingWithRequest:]_block_invoke.150
+ ___49-[HAPAccessoryServerIP _continuePairingAfterWAC:]_block_invoke.122
+ ___49-[HAPAccessoryServerIP _continuePairingAfterWAC:]_block_invoke.127
+ ___49-[HAPAccessoryServerIP authSession:authComplete:]_block_invoke.528
+ ___50-[HAPAccessoryServerIP networkMonitorIsReachable:]_block_invoke.481
+ ___52-[HAP2AccessoryServer(Paired) unpairWithCompletion:]_block_invoke.77
+ ___53-[HAPAccessoryServerHAP2Adapter _printMissingValues:]_block_invoke.220
+ ___53-[HAPAccessoryServerHAP2Adapter _printMissingValues:]_block_invoke.228
+ ___53-[HAPAccessoryServerIP setPairVerifyCompletionBlock:]_block_invoke.409
+ ___54-[HAP2AccessoryServer(Paired) _getSleepIntervalValue:]_block_invoke.228
+ ___55-[HAP2AccessoryServerController addPairing:completion:]_block_invoke.272
+ ___55-[HAPAccessoryServerIP authSession:validateUUID:token:]_block_invoke.518
+ ___55-[HAPAccessoryServerIP authSession:validateUUID:token:]_block_invoke.523
+ ___55-[_HAPAccessoryServerBTLE200 authSession:authComplete:]_block_invoke.993
+ ___56-[HAP2AccessoryServer(Paired) removePairing:completion:]_block_invoke.82
+ ___56-[HAP2AccessoryServerController _scheduleRestartSession]_block_invoke.362
+ ___57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke.513
+ ___57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke_2.517
+ ___59-[HAP2AccessoryServer(Paired) updateAccessoriesWithReason:]_block_invoke.92
+ ___59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke.450
+ ___59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke_2.451
+ ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.428
+ ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.433
+ ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.434
+ ___59-[_HAPAccessoryServerBTLE200 peripheral:didModifyServices:]_block_invoke.958
+ ___60-[HAPAccessoryServerIP _validatePairingAuthMethod:activity:]_block_invoke.497
+ ___63-[HAPAccessoryServerBrowserIP startDiscoveringAccessoryServers]_block_invoke.45
+ ___63-[_HAPAccessoryServerBTLE100 _handlePairSetupExchangeWithData:]_block_invoke.323
+ ___63-[_HAPAccessoryServerBTLE200 authSession:sendAuthExchangeData:]_block_invoke.986
+ ___63-[_HAPAccessoryServerBTLE200 authSession:sendAuthExchangeData:]_block_invoke_2.989
+ ___64-[HAP2AccessoryServer(Paired) _pollAccessoryOnQueueWithOptions:]_block_invoke.244
+ ___64-[HAP2AccessoryServer(Paired) _pollAccessoryOnQueueWithOptions:]_block_invoke_2.248
+ ___64-[HAP2AccessoryServerController unpairedIdentifyWithCompletion:]_block_invoke.282
+ ___64-[HAPAccessoryServerIP _updateWithBonjourDeviceInfo:socketInfo:]_block_invoke.90
+ ___64-[_HAPAccessoryServerBTLE200 securitySession:didCloseWithError:]_block_invoke.1011
+ ___65-[HAPAccessoryServerBrowserIP wacBrowser:didFindHAPWACAccessory:]_block_invoke.72
+ ___65-[HAPAccessoryServerIP _continuePairingAfterAuthPromptWithRetry:]_block_invoke.442
+ ___65-[HAPAccessoryServerIP(NameResolution) _doResolveWithCompletion:]_block_invoke
+ ___65-[HAPAccessoryServerIP(NameResolution) _doResolveWithCompletion:]_block_invoke.13
+ ___65-[HAPNameResolver resolveTCPNameWithTimeoutInSeconds:completion:]_block_invoke
+ ___66-[HAPSystemKeychainStore _allAccessoryPairingKeysIncludingHH2Key:]_block_invoke.334
+ ___67-[HAPAccessoryServerBrowserIP wacBrowser:didRemoveHAPWACAccessory:]_block_invoke.73
+ ___72-[HAP2AccessoryServerController _disableAllCharacteristicsNotification:]_block_invoke.331
+ ___72-[HAP2AccessoryServerController _disableAllCharacteristicsNotification:]_block_invoke_2.332
+ ___75-[HAP2AccessoryServerController _getPairingsCharacteristicForServer:error:]_block_invoke.262
+ ___75-[_HAPAccessoryServerBTLE100 peripheral:didUpdateValueForDescriptor:error:]_block_invoke.318
+ ___76-[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]_block_invoke.251
+ ___76-[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]_block_invoke_2.259
+ ___76-[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]_block_invoke_3.260
+ ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke.570
+ ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke.572
+ ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.571
+ ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.573
+ ___76-[HAPSystemKeychainStore allKeychainItemsForType:identifier:syncable:error:]_block_invoke.306
+ ___77-[HAP2AccessoryServerController _handleAttributeDatabaseResponse:completion:]_block_invoke.200
+ ___79-[HAPAccessoryServerIP _queueListPairingWithCompletionQueue:completionHandler:]_block_invoke.174
+ ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1211
+ ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1212
+ ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke_2.1213
+ ___80-[HAP2AccessoryServerController _callCharacteristicCompletion:operations:error:]_block_invoke.358
+ ___80-[HAP2AccessoryServerController _callCharacteristicCompletion:operations:error:]_block_invoke.361
+ ___81-[HAP2AccessoryServerEncodingThread groupingsForWriteRequestsForCharacteristics:]_block_invoke.52
+ ___81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke.261
+ ___81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke_2.262
+ ___81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke_3.263
+ ___82-[HAPAccessoryServerHAP2Adapter accessoryServer:doesRequirePermission:completion:]_block_invoke.246
+ ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.198
+ ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.203
+ ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.212
+ ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke_2.219
+ ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke_3.220
+ ___82-[_HAPAccessoryServerBTLE100 removePairingForCurrentControllerOnQueue:completion:]_block_invoke.346
+ ___83-[HAPAccessoryServerBrowserIP wacBrowser:didFindUnconfiguredPairedHAPWACAccessory:]_block_invoke.76
+ ___83-[HAPAccessoryServerIP _writeCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.239
+ ___85-[HAPAccessoryServerIP _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.320
+ ___85-[HAPAccessoryServerIP _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.324
+ ___86-[HAPAccessoryServerIP _establishSecureConnectionAndFetchAttributeDatabaseWithReason:]_block_invoke.148
+ ___86-[_HAPAccessoryServerBTLE100 _removePairingWithIdentifier:publicKey:queue:completion:]_block_invoke.344
+ ___88-[HAPAccessoryServerIP _queueAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.173
+ ___88-[HAPAccessoryServerIP _startAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.542
+ ___89-[_HAPAccessoryServerBTLE100 _addPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.334
+ ___90-[HAP2AccessoryServerController enableNotificationsForCharacteristics:options:completion:]_block_invoke.226
+ ___90-[HAP2AccessoryServerController enableNotificationsForCharacteristics:options:completion:]_block_invoke.228
+ ___90-[HAP2AccessoryServerController enableNotificationsForCharacteristics:options:completion:]_block_invoke.239
+ ___90-[HAP2AccessoryServerController enableNotificationsForCharacteristics:options:completion:]_block_invoke.243
+ ___90-[HAP2AccessoryServerController enableNotificationsForCharacteristics:options:completion:]_block_invoke.248
+ ___90-[HAP2AccessoryServerController enableNotificationsForCharacteristics:options:completion:]_block_invoke_2.249
+ ___90-[HAP2AccessoryServerController writeValuesForCharacteristics:timeout:options:completion:]_block_invoke.224
+ ___90-[HAPAccessoryServerIP _queueEnableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.175
+ ___91-[HAP2AccessoryServerController disableNotificationsForCharacteristics:options:completion:]_block_invoke.250
+ ___91-[HAP2AccessoryServerController disableNotificationsForCharacteristics:options:completion:]_block_invoke.255
+ ___92-[HAPAccessoryServerIP writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.238
+ ___93-[HAP2AccessoryServerEncodingThread _parseCharacteristicResponsesWithBodyData:request:error:]_block_invoke.55
+ ___93-[HAPAccessoryServerHAP2Adapter enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.188
+ ___94-[HAP2AccessoryServerController _createOperationsToReadCharacteristics:timeout:options:error:]_block_invoke.219
+ ___94-[HAPAccessoryServerHAP2Adapter _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.190
+ ___94-[HAPAccessoryServerHAP2Adapter _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke_2.191
+ ___97-[HAP2AccessoryServer(Paired) _readValuesForCharacteristics:timeout:options:activity:completion:]_block_invoke.215
+ ___97-[HAP2AccessoryServer(Paired) _readValuesForCharacteristics:timeout:options:activity:completion:]_block_invoke_2.216
+ ___97-[HAP2AccessoryServer(Paired) _readValuesForCharacteristics:timeout:options:activity:completion:]_block_invoke_3.217
+ ___Block_byref_object_copy_.10463
+ ___Block_byref_object_copy_.10774
+ ___Block_byref_object_copy_.11590
+ ___Block_byref_object_copy_.11788
+ ___Block_byref_object_copy_.12815
+ ___Block_byref_object_copy_.13571
+ ___Block_byref_object_copy_.13801
+ ___Block_byref_object_copy_.14842
+ ___Block_byref_object_copy_.16797
+ ___Block_byref_object_copy_.17009
+ ___Block_byref_object_copy_.18059
+ ___Block_byref_object_copy_.18659
+ ___Block_byref_object_copy_.19741
+ ___Block_byref_object_copy_.1989
+ ___Block_byref_object_copy_.20564
+ ___Block_byref_object_copy_.24625
+ ___Block_byref_object_copy_.24791
+ ___Block_byref_object_copy_.2659
+ ___Block_byref_object_copy_.336
+ ___Block_byref_object_copy_.4215
+ ___Block_byref_object_copy_.5080
+ ___Block_byref_object_copy_.5312
+ ___Block_byref_object_copy_.5763
+ ___Block_byref_object_copy_.6426
+ ___Block_byref_object_copy_.6612
+ ___Block_byref_object_copy_.691
+ ___Block_byref_object_copy_.7471
+ ___Block_byref_object_copy_.8912
+ ___Block_byref_object_copy_.9226
+ ___Block_byref_object_copy_.9430
+ ___Block_byref_object_dispose_.10464
+ ___Block_byref_object_dispose_.10775
+ ___Block_byref_object_dispose_.11591
+ ___Block_byref_object_dispose_.11789
+ ___Block_byref_object_dispose_.12816
+ ___Block_byref_object_dispose_.13572
+ ___Block_byref_object_dispose_.13802
+ ___Block_byref_object_dispose_.14843
+ ___Block_byref_object_dispose_.16798
+ ___Block_byref_object_dispose_.17010
+ ___Block_byref_object_dispose_.18060
+ ___Block_byref_object_dispose_.18660
+ ___Block_byref_object_dispose_.19742
+ ___Block_byref_object_dispose_.1990
+ ___Block_byref_object_dispose_.20565
+ ___Block_byref_object_dispose_.24626
+ ___Block_byref_object_dispose_.24792
+ ___Block_byref_object_dispose_.2660
+ ___Block_byref_object_dispose_.337
+ ___Block_byref_object_dispose_.4216
+ ___Block_byref_object_dispose_.5081
+ ___Block_byref_object_dispose_.5313
+ ___Block_byref_object_dispose_.5764
+ ___Block_byref_object_dispose_.6427
+ ___Block_byref_object_dispose_.6613
+ ___Block_byref_object_dispose_.692
+ ___Block_byref_object_dispose_.7472
+ ___Block_byref_object_dispose_.8913
+ ___Block_byref_object_dispose_.9227
+ ___Block_byref_object_dispose_.9431
+ ___block_descriptor_40_e8_32s_e35_v24?0"NSError"8"HAPSocketInfo"16ls32l8
+ ___block_descriptor_40_e8_32w_e34_v20?0i8"NSObject<OS_nw_error>"12lw32l8
+ ___block_descriptor_45_e8_32s_e35_v24?0"NSError"8"HAPSocketInfo"16ls32l8
+ ___block_literal_global.10144
+ ___block_literal_global.1020
+ ___block_literal_global.10828
+ ___block_literal_global.11586
+ ___block_literal_global.11956
+ ___block_literal_global.1229
+ ___block_literal_global.1266
+ ___block_literal_global.13075
+ ___block_literal_global.14952
+ ___block_literal_global.1512
+ ___block_literal_global.15377
+ ___block_literal_global.16540
+ ___block_literal_global.16806
+ ___block_literal_global.182
+ ___block_literal_global.18238
+ ___block_literal_global.1893
+ ___block_literal_global.19488
+ ___block_literal_global.19764
+ ___block_literal_global.20224
+ ___block_literal_global.203
+ ___block_literal_global.209
+ ___block_literal_global.21142
+ ___block_literal_global.213
+ ___block_literal_global.216
+ ___block_literal_global.22482
+ ___block_literal_global.22807
+ ___block_literal_global.233
+ ___block_literal_global.237
+ ___block_literal_global.242
+ ___block_literal_global.24398
+ ___block_literal_global.25013
+ ___block_literal_global.260
+ ___block_literal_global.2728
+ ___block_literal_global.302
+ ___block_literal_global.32
+ ___block_literal_global.364
+ ___block_literal_global.3647
+ ___block_literal_global.373
+ ___block_literal_global.375
+ ___block_literal_global.377
+ ___block_literal_global.379
+ ___block_literal_global.381
+ ___block_literal_global.383
+ ___block_literal_global.464
+ ___block_literal_global.5147
+ ___block_literal_global.5308
+ ___block_literal_global.5878
+ ___block_literal_global.6437
+ ___block_literal_global.6585
+ ___block_literal_global.737
+ ___block_literal_global.7737
+ ___block_literal_global.8603
+ ___block_literal_global.88
+ ___block_literal_global.8995
+ ___block_literal_global.9539
+ ___txtRecordDictionaryForNetworkTxtRecordData_block_invoke.198
+ __unnamed_array_storage.14961
+ __unnamed_array_storage.15992
+ __unnamed_array_storage.16544
+ __unnamed_array_storage.21063
+ __unnamed_array_storage.299
+ __unnamed_array_storage.329
+ __unnamed_array_storage.332
+ __unnamed_array_storage.340
+ _hkConfig.21126
+ _logCategory._hmf_once_t404
+ _logCategory._hmf_once_t50
+ _logCategory._hmf_once_v405
+ _logCategory._hmf_once_v51
+ _nw_parameters_create_secure_tcp
+ _objc_msgSend$_cancelNameResolution
+ _objc_msgSend$_doBonjourRemoveWithServer:
+ _objc_msgSend$_doCompletionWithErrorCode:socketInfo:state:
+ _objc_msgSend$_doCompletionWithErrorCode:state:
+ _objc_msgSend$_doCompletionWithSocketInfo:
+ _objc_msgSend$_incrementPairVerifyFailureCount
+ _objc_msgSend$_pollAccessory
+ _objc_msgSend$_startReachabilityEventTimer
+ _objc_msgSend$cancelTimer
+ _objc_msgSend$connection
+ _objc_msgSend$connectionEstablishedUsing
+ _objc_msgSend$initWithAccessory:forLinkType:durationInMS:reason:connectionEstablishedUsing:pvError:
+ _objc_msgSend$initWithDeviceName:serviceType:domain:workQueue:
+ _objc_msgSend$isMemberOfClass:
+ _objc_msgSend$maximumPairVerifyFailureCount
+ _objc_msgSend$metric_pairVerifyConnectionEstablishedBy
+ _objc_msgSend$nameResolutionCompletionBlocks
+ _objc_msgSend$nameResolver
+ _objc_msgSend$nwConnnectionStart
+ _objc_msgSend$nwCreateConnection
+ _objc_msgSend$resetPairVerifyFailureCount
+ _objc_msgSend$resolutionState
+ _objc_msgSend$resolveTCPNameWithTimeoutInSeconds:completion:
+ _objc_msgSend$setCachedSocketInfo:
+ _objc_msgSend$setCompletion:
+ _objc_msgSend$setConnection:
+ _objc_msgSend$setMetric_pairVerifyConnectionEstablishedBy:
+ _objc_msgSend$setNameResolutionCompletionBlocks:
+ _objc_msgSend$setNameResolver:
+ _objc_msgSend$setResolutionState:
+ _objc_msgSend$setStateChangedHandler
+ _objc_msgSend$setTimer:
+ _objc_msgSend$startTimerWithTimeoutInSeconds:
+ _objc_msgSend$timer
+ _sharedInstance.onceToken.15376
- -[HAPAccessoryServerIP pendingConnectionSocketInfo]
- -[HAPAccessoryServerIP setPendingConnectionSocketInfo:]
- -[HAPMetricsPairVerifyEvent initWithAccessory:forLinkType:durationInMS:reason:pvError:]
- GCC_except_table1013
- GCC_except_table1017
- GCC_except_table1030
- GCC_except_table1035
- GCC_except_table1044
- GCC_except_table1046
- GCC_except_table1048
- GCC_except_table1050
- GCC_except_table1176
- GCC_except_table1180
- GCC_except_table1182
- GCC_except_table1564
- GCC_except_table1567
- GCC_except_table1575
- GCC_except_table1577
- GCC_except_table1583
- GCC_except_table1585
- GCC_except_table1589
- GCC_except_table1593
- GCC_except_table1595
- GCC_except_table1600
- GCC_except_table1604
- GCC_except_table1614
- GCC_except_table1629
- GCC_except_table1633
- GCC_except_table1637
- GCC_except_table1641
- GCC_except_table1643
- GCC_except_table1795
- GCC_except_table1798
- GCC_except_table1800
- GCC_except_table1802
- GCC_except_table1811
- GCC_except_table1813
- GCC_except_table1817
- GCC_except_table1820
- GCC_except_table1822
- GCC_except_table1825
- GCC_except_table1842
- GCC_except_table1849
- GCC_except_table1853
- GCC_except_table1860
- GCC_except_table1868
- GCC_except_table1872
- GCC_except_table1876
- GCC_except_table1880
- GCC_except_table1888
- GCC_except_table1899
- GCC_except_table1936
- GCC_except_table1942
- GCC_except_table2113
- GCC_except_table2142
- GCC_except_table2253
- GCC_except_table2261
- GCC_except_table2262
- GCC_except_table2263
- GCC_except_table2264
- GCC_except_table2265
- GCC_except_table2266
- GCC_except_table2281
- GCC_except_table2295
- GCC_except_table2372
- GCC_except_table2384
- GCC_except_table2410
- GCC_except_table2418
- GCC_except_table2443
- GCC_except_table2446
- GCC_except_table2451
- GCC_except_table2459
- GCC_except_table2465
- GCC_except_table2467
- GCC_except_table2648
- GCC_except_table2717
- GCC_except_table2739
- GCC_except_table2754
- GCC_except_table2766
- GCC_except_table2767
- GCC_except_table2775
- GCC_except_table2782
- GCC_except_table2785
- GCC_except_table2790
- GCC_except_table2846
- GCC_except_table2849
- GCC_except_table2854
- GCC_except_table2856
- GCC_except_table2870
- GCC_except_table2884
- GCC_except_table2886
- GCC_except_table2890
- GCC_except_table2898
- GCC_except_table2906
- GCC_except_table2955
- GCC_except_table2963
- GCC_except_table2965
- GCC_except_table2966
- GCC_except_table2989
- GCC_except_table3224
- GCC_except_table3283
- GCC_except_table3284
- GCC_except_table3288
- GCC_except_table3291
- GCC_except_table3293
- GCC_except_table3294
- GCC_except_table3296
- GCC_except_table3297
- GCC_except_table3299
- GCC_except_table3306
- GCC_except_table3316
- GCC_except_table3319
- GCC_except_table3330
- GCC_except_table3331
- GCC_except_table3335
- GCC_except_table3338
- GCC_except_table3341
- GCC_except_table3349
- GCC_except_table3361
- GCC_except_table3363
- GCC_except_table3367
- GCC_except_table3371
- GCC_except_table3375
- GCC_except_table3401
- GCC_except_table3419
- GCC_except_table3423
- GCC_except_table3426
- GCC_except_table3428
- GCC_except_table3430
- GCC_except_table3548
- GCC_except_table3573
- GCC_except_table3663
- GCC_except_table3670
- GCC_except_table3688
- GCC_except_table3692
- GCC_except_table3695
- GCC_except_table3698
- GCC_except_table3701
- GCC_except_table3704
- GCC_except_table3707
- GCC_except_table3710
- GCC_except_table3713
- GCC_except_table3716
- GCC_except_table3721
- GCC_except_table3732
- GCC_except_table3735
- GCC_except_table3746
- GCC_except_table3754
- GCC_except_table3758
- GCC_except_table3766
- GCC_except_table3770
- GCC_except_table3771
- GCC_except_table3789
- GCC_except_table3791
- GCC_except_table3793
- GCC_except_table3794
- GCC_except_table3797
- GCC_except_table3803
- GCC_except_table3808
- GCC_except_table3814
- GCC_except_table3816
- GCC_except_table3819
- GCC_except_table3831
- GCC_except_table3842
- GCC_except_table3844
- GCC_except_table3853
- GCC_except_table3859
- GCC_except_table387
- GCC_except_table403
- GCC_except_table411
- GCC_except_table4119
- GCC_except_table4125
- GCC_except_table4142
- GCC_except_table4146
- GCC_except_table4163
- GCC_except_table4169
- GCC_except_table4182
- GCC_except_table4196
- GCC_except_table4200
- GCC_except_table4303
- GCC_except_table4383
- GCC_except_table4391
- GCC_except_table4401
- GCC_except_table441
- GCC_except_table4437
- GCC_except_table4440
- GCC_except_table4441
- GCC_except_table4442
- GCC_except_table448
- GCC_except_table4536
- GCC_except_table4537
- GCC_except_table4538
- GCC_except_table4539
- GCC_except_table4540
- GCC_except_table4541
- GCC_except_table4547
- GCC_except_table4548
- GCC_except_table4550
- GCC_except_table4557
- GCC_except_table4560
- GCC_except_table4562
- GCC_except_table4567
- GCC_except_table4570
- GCC_except_table4573
- GCC_except_table4577
- GCC_except_table4581
- GCC_except_table4610
- GCC_except_table4611
- GCC_except_table462
- GCC_except_table463
- GCC_except_table4630
- GCC_except_table4640
- GCC_except_table4643
- GCC_except_table4648
- GCC_except_table465
- GCC_except_table4651
- GCC_except_table468
- GCC_except_table471
- GCC_except_table483
- GCC_except_table487
- GCC_except_table489
- GCC_except_table4912
- GCC_except_table4916
- GCC_except_table4950
- GCC_except_table4954
- GCC_except_table4956
- GCC_except_table4958
- GCC_except_table496
- GCC_except_table502
- GCC_except_table5111
- GCC_except_table5117
- GCC_except_table5121
- GCC_except_table5122
- GCC_except_table5123
- GCC_except_table5124
- GCC_except_table5130
- GCC_except_table5164
- GCC_except_table5165
- GCC_except_table5184
- GCC_except_table5196
- GCC_except_table5199
- GCC_except_table520
- GCC_except_table5204
- GCC_except_table5206
- GCC_except_table537
- GCC_except_table5419
- GCC_except_table5431
- GCC_except_table5436
- GCC_except_table5439
- GCC_except_table5440
- GCC_except_table5442
- GCC_except_table5443
- GCC_except_table5445
- GCC_except_table5475
- GCC_except_table5501
- GCC_except_table5505
- GCC_except_table5510
- GCC_except_table5514
- GCC_except_table5518
- GCC_except_table5522
- GCC_except_table5526
- GCC_except_table5534
- GCC_except_table5536
- GCC_except_table5538
- GCC_except_table5576
- GCC_except_table5603
- GCC_except_table5604
- GCC_except_table5605
- GCC_except_table5606
- GCC_except_table564
- GCC_except_table5679
- GCC_except_table568
- GCC_except_table5685
- GCC_except_table5698
- GCC_except_table570
- GCC_except_table5701
- GCC_except_table5702
- GCC_except_table5707
- GCC_except_table5710
- GCC_except_table5717
- GCC_except_table572
- GCC_except_table5720
- GCC_except_table5734
- GCC_except_table5741
- GCC_except_table5747
- GCC_except_table5756
- GCC_except_table5758
- GCC_except_table5777
- GCC_except_table5779
- GCC_except_table5787
- GCC_except_table5803
- GCC_except_table5812
- GCC_except_table5813
- GCC_except_table5816
- GCC_except_table5822
- GCC_except_table5826
- GCC_except_table5828
- GCC_except_table5830
- GCC_except_table5834
- GCC_except_table592
- GCC_except_table596
- GCC_except_table5979
- GCC_except_table600
- GCC_except_table6035
- GCC_except_table6038
- GCC_except_table6042
- GCC_except_table6048
- GCC_except_table6055
- GCC_except_table6056
- GCC_except_table6072
- GCC_except_table6076
- GCC_except_table6077
- GCC_except_table6078
- GCC_except_table609
- GCC_except_table6126
- GCC_except_table6127
- GCC_except_table6129
- GCC_except_table6132
- GCC_except_table615
- GCC_except_table6160
- GCC_except_table6161
- GCC_except_table6166
- GCC_except_table618
- GCC_except_table6186
- GCC_except_table6203
- GCC_except_table6204
- GCC_except_table6205
- GCC_except_table621
- GCC_except_table6213
- GCC_except_table6218
- GCC_except_table6219
- GCC_except_table6220
- GCC_except_table6234
- GCC_except_table6237
- GCC_except_table6243
- GCC_except_table6249
- GCC_except_table626
- GCC_except_table6261
- GCC_except_table6262
- GCC_except_table6267
- GCC_except_table6276
- GCC_except_table6282
- GCC_except_table6283
- GCC_except_table6287
- GCC_except_table6299
- GCC_except_table630
- GCC_except_table6301
- GCC_except_table6305
- GCC_except_table6326
- GCC_except_table6329
- GCC_except_table6355
- GCC_except_table637
- GCC_except_table642
- GCC_except_table643
- GCC_except_table6519
- GCC_except_table6582
- GCC_except_table6614
- GCC_except_table6617
- GCC_except_table669
- GCC_except_table6781
- GCC_except_table682
- GCC_except_table683
- GCC_except_table6844
- GCC_except_table6907
- GCC_except_table6913
- GCC_except_table6958
- GCC_except_table6960
- GCC_except_table6962
- GCC_except_table6964
- GCC_except_table6966
- GCC_except_table6970
- GCC_except_table6972
- GCC_except_table6976
- GCC_except_table6978
- GCC_except_table6981
- GCC_except_table6983
- GCC_except_table6985
- GCC_except_table6988
- GCC_except_table7014
- GCC_except_table7017
- GCC_except_table7018
- GCC_except_table7057
- GCC_except_table7058
- GCC_except_table7059
- GCC_except_table7061
- GCC_except_table7062
- GCC_except_table7064
- GCC_except_table7065
- GCC_except_table7066
- GCC_except_table7068
- GCC_except_table7069
- GCC_except_table7071
- GCC_except_table7076
- GCC_except_table7080
- GCC_except_table7128
- GCC_except_table7135
- GCC_except_table717
- GCC_except_table7229
- GCC_except_table7245
- GCC_except_table7247
- GCC_except_table7249
- GCC_except_table7252
- GCC_except_table7254
- GCC_except_table7256
- GCC_except_table7258
- GCC_except_table7259
- GCC_except_table7261
- GCC_except_table7265
- GCC_except_table7270
- GCC_except_table740
- GCC_except_table759
- GCC_except_table783
- GCC_except_table787
- GCC_except_table804
- GCC_except_table905
- GCC_except_table907
- _CFPreferencesGetAppBooleanValue
- _OBJC_IVAR_$_HAPAccessoryServerIP._pendingConnectionSocketInfo
- __CopyPairingIdentityDelegateCallback_f.14689
- __CopyPairingIdentityDelegateCallback_f.21183
- __CopyPairingIdentityDelegateCallback_f.2656
- __FindPairedPeerDelegateCallback_f.2655
- __OBJC_$_CLASS_METHODS_HAPAccessoryServerIP(HTTPActivity|SessionRestore|Metrics)
- __OBJC_$_INSTANCE_METHODS_HAPAccessoryServerIP(HTTPActivity|SessionRestore|Metrics)
- __OBJC_$_PROP_LIST_HAP2Accessory.288
- __OBJC_$_PROP_LIST_HAP2AccessoryServerBrowser.398
- __OBJC_$_PROP_LIST_HAP2AccessoryServerCoordinator.181
- __OBJC_$_PROP_LIST_HAP2AccessoryServerMetadata.102
- __OBJC_$_PROP_LIST_HAP2CoAPClient.223
- __OBJC_$_PROP_LIST_HAP2EncodedCharacteristicEvent.69
- __OBJC_$_PROP_LIST_HAP2EncodedCharacteristicResponse.57
- __OBJC_$_PROP_LIST_HAP2EncodedEnableNotificationResponse.66
- __OBJC_$_PROP_LIST_HAPAccessoryReachabilityClient.200
- __OBJC_$_PROP_LIST_HAPAccessoryReachabilityProfile.97
- __PairSetupPromptForSetupCodeDelegateCallback_f.21185
- __SavePairedPeerDelegateCallback_f.14688
- __SavePairedPeerDelegateCallback_f.21179
- ___103-[_HAPAccessoryServerBTLE100 _handlePairingsReadForCharacteristic:readError:removing:queue:completion:]_block_invoke.336
- ___108-[HAP2AccessoryServerController _removePairingCompletionWithIdentity:cleanupLocalData:operation:completion:]_block_invoke.267
- ___108-[HAPAccessoryServerIP _handleWriteECONNResetError:writeRequests:responses:timeout:queue:completionHandler:]_block_invoke.248
- ___113-[HAPAccessoryServerIP _handleReadECONNRESETError:readCharacteristics:responses:timeout:queue:completionHandler:]_block_invoke.195
- ___41-[HAPAccessoryServerIP getAccessoryInfo:]_block_invoke.477
- ___44-[HAPAccessoryServerIP _pairVerifyStartWAC:]_block_invoke.112
- ___45-[HAP2AccessoryServerController closeSession]_block_invoke.285
- ___45-[HAP2AccessoryServerController closeSession]_block_invoke.289
- ___45-[HAPAccessoryServerIP _pairSetupContinueWAC]_block_invoke.110
- ___45-[HAPAccessoryServerIP stopPairingWithError:]_block_invoke.150
- ___45-[_HAPAccessoryServerBTLE100 _pairSetupStart]_block_invoke.321
- ___47-[HAPAccessoryServerIP identifyWithCompletion:]_block_invoke.613
- ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.113
- ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.114
- ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.117
- ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke_2.115
- ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke_2.118
- ___48-[HAPAccessoryServerIP startPairingWithRequest:]_block_invoke.148
- ___49-[HAPAccessoryServerIP _continuePairingAfterWAC:]_block_invoke.120
- ___49-[HAPAccessoryServerIP _continuePairingAfterWAC:]_block_invoke.125
- ___49-[HAPAccessoryServerIP authSession:authComplete:]_block_invoke.527
- ___50-[HAPAccessoryServerIP networkMonitorIsReachable:]_block_invoke.472
- ___52-[HAP2AccessoryServer(Paired) unpairWithCompletion:]_block_invoke.75
- ___53-[HAPAccessoryServerHAP2Adapter _printMissingValues:]_block_invoke.219
- ___53-[HAPAccessoryServerHAP2Adapter _printMissingValues:]_block_invoke.227
- ___53-[HAPAccessoryServerIP setPairVerifyCompletionBlock:]_block_invoke.406
- ___54-[HAP2AccessoryServer(Paired) _getSleepIntervalValue:]_block_invoke.227
- ___55-[HAP2AccessoryServerController addPairing:completion:]_block_invoke.271
- ___55-[HAPAccessoryServerIP authSession:validateUUID:token:]_block_invoke.517
- ___55-[HAPAccessoryServerIP authSession:validateUUID:token:]_block_invoke.522
- ___55-[_HAPAccessoryServerBTLE200 authSession:authComplete:]_block_invoke.992
- ___56-[HAP2AccessoryServer(Paired) removePairing:completion:]_block_invoke.80
- ___56-[HAP2AccessoryServerController _scheduleRestartSession]_block_invoke.361
- ___57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke.512
- ___57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke_2.516
- ___59-[HAP2AccessoryServer(Paired) updateAccessoriesWithReason:]_block_invoke.91
- ___59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke.441
- ___59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke_2.442
- ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.419
- ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.424
- ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.425
- ___59-[_HAPAccessoryServerBTLE200 peripheral:didModifyServices:]_block_invoke.957
- ___60-[HAPAccessoryServerIP _validatePairingAuthMethod:activity:]_block_invoke.496
- ___63-[HAPAccessoryServerBrowserIP startDiscoveringAccessoryServers]_block_invoke.42
- ___63-[_HAPAccessoryServerBTLE100 _handlePairSetupExchangeWithData:]_block_invoke.322
- ___63-[_HAPAccessoryServerBTLE200 authSession:sendAuthExchangeData:]_block_invoke.985
- ___63-[_HAPAccessoryServerBTLE200 authSession:sendAuthExchangeData:]_block_invoke_2.988
- ___64-[HAP2AccessoryServer(Paired) _pollAccessoryOnQueueWithOptions:]_block_invoke.242
- ___64-[HAP2AccessoryServer(Paired) _pollAccessoryOnQueueWithOptions:]_block_invoke_2.247
- ___64-[HAP2AccessoryServerController unpairedIdentifyWithCompletion:]_block_invoke.281
- ___64-[_HAPAccessoryServerBTLE200 securitySession:didCloseWithError:]_block_invoke.1010
- ___65-[HAPAccessoryServerBrowserIP wacBrowser:didFindHAPWACAccessory:]_block_invoke.69
- ___65-[HAPAccessoryServerIP _continuePairingAfterAuthPromptWithRetry:]_block_invoke.433
- ___66-[HAPSystemKeychainStore _allAccessoryPairingKeysIncludingHH2Key:]_block_invoke.333
- ___67-[HAPAccessoryServerBrowserIP wacBrowser:didRemoveHAPWACAccessory:]_block_invoke.70
- ___72-[HAP2AccessoryServerController _disableAllCharacteristicsNotification:]_block_invoke.330
- ___72-[HAP2AccessoryServerController _disableAllCharacteristicsNotification:]_block_invoke_2.331
- ___75-[HAP2AccessoryServerController _getPairingsCharacteristicForServer:error:]_block_invoke.261
- ___75-[_HAPAccessoryServerBTLE100 peripheral:didUpdateValueForDescriptor:error:]_block_invoke.317
- ___76-[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]_block_invoke.249
- ___76-[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]_block_invoke_2.257
- ___76-[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]_block_invoke_3.258
- ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke.569
- ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke.571
- ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.570
- ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.572
- ___76-[HAPSystemKeychainStore allKeychainItemsForType:identifier:syncable:error:]_block_invoke.305
- ___77-[HAP2AccessoryServerController _handleAttributeDatabaseResponse:completion:]_block_invoke.199
- ___79-[HAPAccessoryServerIP _queueListPairingWithCompletionQueue:completionHandler:]_block_invoke.172
- ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1190
- ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1191
- ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke_2.1192
- ___80-[HAP2AccessoryServerController _callCharacteristicCompletion:operations:error:]_block_invoke.357
- ___80-[HAP2AccessoryServerController _callCharacteristicCompletion:operations:error:]_block_invoke.359
- ___81-[HAP2AccessoryServerEncodingThread groupingsForWriteRequestsForCharacteristics:]_block_invoke.51
- ___81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke.259
- ___81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke_2.260
- ___81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke_3.261
- ___82-[HAPAccessoryServerHAP2Adapter accessoryServer:doesRequirePermission:completion:]_block_invoke.245
- ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.196
- ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.201
- ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.210
- ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke_2.217
- ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke_3.218
- ___82-[_HAPAccessoryServerBTLE100 removePairingForCurrentControllerOnQueue:completion:]_block_invoke.344
- ___83-[HAPAccessoryServerBrowserIP wacBrowser:didFindUnconfiguredPairedHAPWACAccessory:]_block_invoke.73
- ___83-[HAPAccessoryServerIP _writeCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.237
- ___85-[HAPAccessoryServerIP _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.318
- ___85-[HAPAccessoryServerIP _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.322
- ___86-[HAPAccessoryServerIP _establishSecureConnectionAndFetchAttributeDatabaseWithReason:]_block_invoke.146
- ___86-[_HAPAccessoryServerBTLE100 _removePairingWithIdentifier:publicKey:queue:completion:]_block_invoke.343
- ___88-[HAPAccessoryServerIP _queueAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.171
- ___88-[HAPAccessoryServerIP _startAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.541
- ___89-[_HAPAccessoryServerBTLE100 _addPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.333
- ___90-[HAP2AccessoryServerController enableNotificationsForCharacteristics:options:completion:]_block_invoke.225
- ___90-[HAP2AccessoryServerController enableNotificationsForCharacteristics:options:completion:]_block_invoke.227
- ___90-[HAP2AccessoryServerController enableNotificationsForCharacteristics:options:completion:]_block_invoke.238
- ___90-[HAP2AccessoryServerController enableNotificationsForCharacteristics:options:completion:]_block_invoke.242
- ___90-[HAP2AccessoryServerController enableNotificationsForCharacteristics:options:completion:]_block_invoke.247
- ___90-[HAP2AccessoryServerController enableNotificationsForCharacteristics:options:completion:]_block_invoke_2.248
- ___90-[HAP2AccessoryServerController writeValuesForCharacteristics:timeout:options:completion:]_block_invoke.223
- ___90-[HAPAccessoryServerIP _queueEnableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.173
- ___91-[HAP2AccessoryServerController disableNotificationsForCharacteristics:options:completion:]_block_invoke.249
- ___91-[HAP2AccessoryServerController disableNotificationsForCharacteristics:options:completion:]_block_invoke.254
- ___92-[HAPAccessoryServerIP writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.236
- ___93-[HAP2AccessoryServerEncodingThread _parseCharacteristicResponsesWithBodyData:request:error:]_block_invoke.54
- ___93-[HAPAccessoryServerHAP2Adapter enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.187
- ___94-[HAP2AccessoryServerController _createOperationsToReadCharacteristics:timeout:options:error:]_block_invoke.218
- ___94-[HAPAccessoryServerHAP2Adapter _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.189
- ___94-[HAPAccessoryServerHAP2Adapter _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke_2.190
- ___97-[HAP2AccessoryServer(Paired) _readValuesForCharacteristics:timeout:options:activity:completion:]_block_invoke.214
- ___97-[HAP2AccessoryServer(Paired) _readValuesForCharacteristics:timeout:options:activity:completion:]_block_invoke_2.215
- ___97-[HAP2AccessoryServer(Paired) _readValuesForCharacteristics:timeout:options:activity:completion:]_block_invoke_3.216
- ___Block_byref_object_copy_.10225
- ___Block_byref_object_copy_.10530
- ___Block_byref_object_copy_.11343
- ___Block_byref_object_copy_.11540
- ___Block_byref_object_copy_.12562
- ___Block_byref_object_copy_.13334
- ___Block_byref_object_copy_.13561
- ___Block_byref_object_copy_.14595
- ___Block_byref_object_copy_.16544
- ___Block_byref_object_copy_.16760
- ___Block_byref_object_copy_.17774
- ___Block_byref_object_copy_.18357
- ___Block_byref_object_copy_.1922
- ___Block_byref_object_copy_.19437
- ___Block_byref_object_copy_.20261
- ___Block_byref_object_copy_.24307
- ___Block_byref_object_copy_.24472
- ___Block_byref_object_copy_.2605
- ___Block_byref_object_copy_.323
- ___Block_byref_object_copy_.3996
- ___Block_byref_object_copy_.4853
- ___Block_byref_object_copy_.5091
- ___Block_byref_object_copy_.5535
- ___Block_byref_object_copy_.6195
- ___Block_byref_object_copy_.6377
- ___Block_byref_object_copy_.678
- ___Block_byref_object_copy_.7233
- ___Block_byref_object_copy_.8694
- ___Block_byref_object_copy_.9008
- ___Block_byref_object_copy_.9211
- ___Block_byref_object_dispose_.10226
- ___Block_byref_object_dispose_.10531
- ___Block_byref_object_dispose_.11344
- ___Block_byref_object_dispose_.11541
- ___Block_byref_object_dispose_.12563
- ___Block_byref_object_dispose_.13335
- ___Block_byref_object_dispose_.13562
- ___Block_byref_object_dispose_.14596
- ___Block_byref_object_dispose_.16545
- ___Block_byref_object_dispose_.16761
- ___Block_byref_object_dispose_.17775
- ___Block_byref_object_dispose_.18358
- ___Block_byref_object_dispose_.1923
- ___Block_byref_object_dispose_.19438
- ___Block_byref_object_dispose_.20262
- ___Block_byref_object_dispose_.24308
- ___Block_byref_object_dispose_.24473
- ___Block_byref_object_dispose_.2606
- ___Block_byref_object_dispose_.324
- ___Block_byref_object_dispose_.3997
- ___Block_byref_object_dispose_.4854
- ___Block_byref_object_dispose_.5092
- ___Block_byref_object_dispose_.5536
- ___Block_byref_object_dispose_.6196
- ___Block_byref_object_dispose_.6378
- ___Block_byref_object_dispose_.679
- ___Block_byref_object_dispose_.7234
- ___Block_byref_object_dispose_.8695
- ___Block_byref_object_dispose_.9009
- ___Block_byref_object_dispose_.9212
- ___block_literal_global.1019
- ___block_literal_global.10581
- ___block_literal_global.11339
- ___block_literal_global.11708
- ___block_literal_global.1208
- ___block_literal_global.1245
- ___block_literal_global.12823
- ___block_literal_global.14713
- ___block_literal_global.1511
- ___block_literal_global.15140
- ___block_literal_global.16280
- ___block_literal_global.16553
- ___block_literal_global.17936
- ___block_literal_global.180
- ___block_literal_global.1831
- ___block_literal_global.19182
- ___block_literal_global.19459
- ___block_literal_global.19924
- ___block_literal_global.202
- ___block_literal_global.208
- ___block_literal_global.20837
- ___block_literal_global.212
- ___block_literal_global.215
- ___block_literal_global.22171
- ___block_literal_global.22493
- ___block_literal_global.232
- ___block_literal_global.236
- ___block_literal_global.24081
- ___block_literal_global.241
- ___block_literal_global.24695
- ___block_literal_global.259
- ___block_literal_global.2671
- ___block_literal_global.301
- ___block_literal_global.33
- ___block_literal_global.363
- ___block_literal_global.372
- ___block_literal_global.374
- ___block_literal_global.376
- ___block_literal_global.378
- ___block_literal_global.380
- ___block_literal_global.382
- ___block_literal_global.463
- ___block_literal_global.4916
- ___block_literal_global.5087
- ___block_literal_global.5647
- ___block_literal_global.6206
- ___block_literal_global.6351
- ___block_literal_global.740
- ___block_literal_global.7495
- ___block_literal_global.8380
- ___block_literal_global.87
- ___block_literal_global.8778
- ___block_literal_global.9321
- ___block_literal_global.9910
- ___txtRecordDictionaryForNetworkTxtRecordData_block_invoke.197
- __os_feature_enabled_impl
- __unnamed_array_storage.14725
- __unnamed_array_storage.15744
- __unnamed_array_storage.16284
- __unnamed_array_storage.20758
- __unnamed_array_storage.298
- __unnamed_array_storage.328
- __unnamed_array_storage.331
- __unnamed_array_storage.339
- _hkConfig.20821
- _logCategory._hmf_once_t399
- _logCategory._hmf_once_t49
- _logCategory._hmf_once_v400
- _logCategory._hmf_once_v50
- _objc_msgSend$initWithAccessory:forLinkType:durationInMS:reason:pvError:
- _objc_msgSend$initWithSocketInfo:eventsEnabled:queue:wakeAddress:
- _objc_msgSend$setPendingConnectionSocketInfo:
- _sharedInstance.onceToken.15139
CStrings:
+ "\x02A\"\x11\x141\x16$\x12\""
+ "%@ %@/%@"
+ "%{public}@*** No completion block provided for name resolution"
+ "%{public}@*** RESET Called"
+ "%{public}@*** clearing socket info"
+ "%{public}@Authenticated: %d"
+ "%{public}@Bonjour reconfirm failed %d"
+ "%{public}@Cancelling active name resolution"
+ "%{public}@attempt to initiate name resolution on stale object"
+ "%{public}@name resolution already in progress.  Queueing completion routine"
+ "%{public}@name resolution completed for %@ error %@"
+ "%{public}@name resolution failed"
+ "%{public}@name resolution time out for %@"
+ "%{public}@name resolution timed out for %@"
+ "%{public}@no completion routine for name resolution"
+ "%{public}@nw_connection Address resolved:  %s   port: %d for %@"
+ "%{public}@nw_connection sock addr to string failed: %d %@"
+ "%{public}@nw_connection state changed %@ %d error %@"
+ "%{public}@nw_connection_create failed for %@ %@ %@"
+ "%{public}@nw_connection_create with %@ %@ %@"
+ "%{public}@nw_connection_state cancelled %@"
+ "%{public}@nw_connection_state failed %@"
+ "%{public}@nw_connection_state invalid %@"
+ "%{public}@nw_connection_state preparing %@"
+ "%{public}@nw_connection_state ready %@"
+ "%{public}@nw_connection_state waiting %@"
+ "%{public}@resetting IP info as a result of maximum pair verify failures reached"
+ "%{public}@saving updated socket info"
+ "%{public}@starting name resolution for %@ with timeout of %@"
+ "%{public}@updating cached socket info from %@ to %@"
+ "'"
+ "@\"HAPNameResolver\""
+ "@64@0:8@16@24Q32@40@48@56"
+ "HAPMaximumConsecutiveIPPairVerifyFailures"
+ "HAPMetricsPairVerifyEvent - Accessory Identifier: %@, linkType: %@, duration: %lu ms, reason: %@, connection Established: %@ error: %@"
+ "HAPNameResolver"
+ "HAPServerIPServerNameResolutionTimeoutSeconds"
+ "NameResolution"
+ "T@\"HAPNameResolver\",&,N,V_nameResolver"
+ "T@\"HAPSocketInfo\",&,N,V_cachedSocketInfo"
+ "T@\"HMFTimer\",&,N,V_timer"
+ "T@\"NSArray\",?,R,C,N"
+ "T@\"NSMutableArray\",&,N,V_nameResolutionCompletionBlocks"
+ "T@\"NSObject<OS_nw_connection>\",&,N,V_connection"
+ "T@\"NSString\",&,N,V_domain"
+ "T@\"NSString\",&,N,V_metric_pairVerifyConnectionEstablishedBy"
+ "T@\"NSString\",&,N,V_serviceType"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",?,R,C,N"
+ "T@\"NSString\",R,N,V_connectionEstablishedUsing"
+ "T@\"NSUUID\",?,R,N"
+ "T@?,C"
+ "T@?,C,N,V_completion"
+ "TB,?,R"
+ "TQ,N,V_consecutivePairVerifyFailures"
+ "TQ,R,N,V_maximumNumberOfPairVeifiesAllowed"
+ "TQ,R,V_resolutionState"
+ "_cachedSocketInfo"
+ "_cancelNameResolution"
+ "_connectionEstablishedUsing"
+ "_consecutivePairVerifyFailures"
+ "_doBonjourRemoveWithServer:"
+ "_doCompletionWithErrorCode:socketInfo:state:"
+ "_doCompletionWithErrorCode:state:"
+ "_doCompletionWithSocketInfo:"
+ "_doResolveWithCompletion:"
+ "_incrementPairVerifyFailureCount"
+ "_maximumNumberOfPairVeifiesAllowed"
+ "_metric_pairVerifyConnectionEstablishedBy"
+ "_nameResolutionCompletionBlocks"
+ "_nameResolver"
+ "_pollAccessory"
+ "_resolutionState"
+ "_startReachabilityEventTimer"
+ "cachedSocketInfo"
+ "cancelTimer"
+ "connection"
+ "connectionEstablishedUsing"
+ "consecutivePairVerifyFailures"
+ "currentMetadataHook"
+ "initWithAccessory:forLinkType:durationInMS:reason:connectionEstablishedUsing:pvError:"
+ "initWithDeviceName:serviceType:domain:workQueue:"
+ "maximumNumberOfPairVeifiesAllowed"
+ "maximumPairVerifyFailureCount"
+ "metric_pairVerifyConnectionEstablishedBy"
+ "nameResolutionCompletionBlocks"
+ "nameResolver"
+ "nwConnnectionStart"
+ "nwCreateConnection"
+ "requestWaitForResidentToSignalAccessorySetup"
+ "resetPairVerifyFailureCount"
+ "resolutionState"
+ "resolveTCPNameWithTimeoutInSeconds:completion:"
+ "setCachedSocketInfo:"
+ "setCompletion:"
+ "setConnection:"
+ "setConsecutivePairVerifyFailures:"
+ "setMetric_pairVerifyConnectionEstablishedBy:"
+ "setNameResolutionCompletionBlocks:"
+ "setNameResolver:"
+ "setResolutionState:"
+ "setStateChangedHandler"
+ "setTimer:"
+ "startTimerWithTimeoutInSeconds:"
+ "timer"
+ "v24@?0@\"NSError\"8@\"HAPSocketInfo\"16"
+ "v32@0:8q16Q24"
+ "v40@0:8q16@24Q32"
+ "\x83\"\x13\x11]\x14"
+ "\xf0\xa1"
- "\x02A\"\x11\x141\x16$\x12!"
- "%{public}@Updating the accessory's name from: '%@' to '%@'"
- "@56@0:8@16@24Q32@40@48"
- "HAPAuthenticationEnhancement"
- "HAPAuthenticationEnhancementEnabled"
- "HAPMetricsPairVerifyEvent - Accessory Identifier: %@, linkType: %@, duration: %lu ms, reason: %@, error: %@"
- "Home"
- "T@\"HAPSocketInfo\",&,N,V_pendingConnectionSocketInfo"
- "T@\"NSUUID\",R,N"
- "com.apple.homed"
- "initWithAccessory:forLinkType:durationInMS:reason:pvError:"
- "setPendingConnectionSocketInfo:"
- "\x83\"\x14]\x12"
- "\xf0\x91"

```
