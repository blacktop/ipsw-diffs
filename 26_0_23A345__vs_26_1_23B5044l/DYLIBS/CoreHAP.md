## CoreHAP

> `/System/Library/PrivateFrameworks/CoreHAP.framework/CoreHAP`

```diff

-1349.1.3.1.1
-  __TEXT.__text: 0x1a8a20
+1368.1.0.1.2
+  __TEXT.__text: 0x1aaf74
   __TEXT.__auth_stubs: 0x1570
-  __TEXT.__objc_methlist: 0x13860
+  __TEXT.__objc_methlist: 0x13a38
   __TEXT.__const: 0x710
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__gcc_except_tab: 0x63b4
-  __TEXT.__cstring: 0x11066
-  __TEXT.__oslogstring: 0x200d1
-  __TEXT.__unwind_info: 0x5d70
-  __TEXT.__objc_classname: 0x2e07
-  __TEXT.__objc_methname: 0x267b1
-  __TEXT.__objc_methtype: 0x8fd0
-  __TEXT.__objc_stubs: 0x186a0
-  __DATA_CONST.__got: 0xa58
-  __DATA_CONST.__const: 0x50b8
-  __DATA_CONST.__objc_classlist: 0x958
+  __TEXT.__gcc_except_tab: 0x63e8
+  __TEXT.__cstring: 0x1121b
+  __TEXT.__oslogstring: 0x202ad
+  __TEXT.__unwind_info: 0x5dd8
+  __TEXT.__objc_classname: 0x2e26
+  __TEXT.__objc_methname: 0x26bcc
+  __TEXT.__objc_methtype: 0x9003
+  __TEXT.__objc_stubs: 0x189c0
+  __DATA_CONST.__got: 0xa60
+  __DATA_CONST.__const: 0x5130
+  __DATA_CONST.__objc_classlist: 0x960
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x338
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6ef0
+  __DATA_CONST.__objc_selrefs: 0x6fb8
   __DATA_CONST.__objc_protorefs: 0xc0
-  __DATA_CONST.__objc_superrefs: 0x7d8
+  __DATA_CONST.__objc_superrefs: 0x7e0
   __DATA_CONST.__objc_arraydata: 0x208
   __AUTH_CONST.__auth_got: 0xac8
-  __AUTH_CONST.__const: 0x7e0
-  __AUTH_CONST.__cfstring: 0xdd20
-  __AUTH_CONST.__objc_const: 0x220b8
+  __AUTH_CONST.__const: 0x800
+  __AUTH_CONST.__cfstring: 0xde40
+  __AUTH_CONST.__objc_const: 0x22268
   __AUTH_CONST.__objc_intobj: 0x6c0
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0xd8
-  __AUTH.__objc_data: 0x4e20
-  __DATA.__objc_ivar: 0x14f0
+  __AUTH.__objc_data: 0x4e70
+  __DATA.__objc_ivar: 0x1504
   __DATA.__data: 0x26c2
-  __DATA.__bss: 0x479
+  __DATA.__bss: 0x499
   __DATA_DIRTY.__objc_data: 0xf50
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0xc8
+  __DATA_DIRTY.__bss: 0xb8
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: A85D03F2-B52F-330B-9A74-077FBC1E8B87
-  Functions: 7484
-  Symbols:   24326
-  CStrings:  12937
+  UUID: F813E315-3662-320C-BD1E-878A02223616
+  Functions: 7532
+  Symbols:   24466
+  CStrings:  13003
 
Symbols:
+ +[HAPAccessoryServerIPCacheData logCategory]
+ -[HAPAccessoryServerBrowserIP _doStartDiscoveringAccessoryServers]
+ -[HAPAccessoryServerBrowserIP _prePopulateBrowserFromCacheWithCompletion:]
+ -[HAPAccessoryServerBrowserIP cache]
+ -[HAPAccessoryServerBrowserIP initWithQueue:cache:]
+ -[HAPAccessoryServerBrowserIP isInitialCacheRestored]
+ -[HAPAccessoryServerBrowserIP setIsInitialCacheRestored:]
+ -[HAPAccessoryServerBrowserIP updateCacheForDeviceID:ipData:]
+ -[HAPAccessoryServerIP _updateCacheForDevice:socketInfo:bonjour:]
+ -[HAPAccessoryServerIPCacheData .cxx_destruct]
+ -[HAPAccessoryServerIPCacheData bonjourDeviceInfo]
+ -[HAPAccessoryServerIPCacheData debugDescription]
+ -[HAPAccessoryServerIPCacheData dictionaryRepresentation]
+ -[HAPAccessoryServerIPCacheData initFromDictionary:]
+ -[HAPAccessoryServerIPCacheData initWithCachedIp:bonjourRecord:]
+ -[HAPAccessoryServerIPCacheData setBonjourDeviceInfo:]
+ -[HAPAccessoryServerIPCacheData setSocketInfo:]
+ -[HAPAccessoryServerIPCacheData socketInfo]
+ -[HAPHTTPClient clientRequestIdentifier]
+ -[HAPHTTPClient requestCounter]
+ -[HAPHTTPClient setRequestCounter:]
+ -[HAPHTTPClient setUniqueClientIdentifier:]
+ -[HAPHTTPClient uniqueClientIdentifier]
+ -[HAPMetadata hapCharacteristicMapOffset]
+ -[HAPMetadata hapCharacteristicShortUUIDToNameMapOffset]
+ -[HAPMetadata hapPropertyMapOffset]
+ -[HAPMetadata hapServiceBTLEShortUUIDToNameMapOffset]
+ -[HAPMetadata hapServiceMapOffset]
+ -[HAPMetadata hapServiceShortUUIDToNameMapOffset]
+ -[HAPMetadata hapSupportsAuthDataSetOffset]
+ -[HAPMetadata hapUnitMapOffset]
+ -[HAPMetadata indexDictionary:keyPath:]
+ -[HAPMetadata init]
+ -[HAPMetadata metadata]
+ -[HAPMetadata parseCharacteristicMetadata:withName:]
+ -[HAPMetadata parseCharacteristicServiceTupleMetadata:withCharacteristicName:]
+ -[HAPMetadata parsePropertyMetadata:withType:]
+ -[HAPMetadata parseServiceMetadata:withName:]
+ -[HAPMetadata parseUnitMetadata:withName:]
+ -[HAPMetadata setHapCharacteristicMapOffset:]
+ -[HAPMetadata setHapCharacteristicShortUUIDToNameMapOffset:]
+ -[HAPMetadata setHapPropertyMapOffset:]
+ -[HAPMetadata setHapServiceBTLEShortUUIDToNameMapOffset:]
+ -[HAPMetadata setHapServiceMapOffset:]
+ -[HAPMetadata setHapServiceShortUUIDToNameMapOffset:]
+ -[HAPMetadata setHapSupportsAuthDataSetOffset:]
+ -[HAPMetadata setHapUnitMapOffset:]
+ -[HAPMetadata setMetadata:]
+ -[HAPMetadataCharacteristic hash]
+ -[HAPMetadataCharacteristic isEqual:]
+ -[HAPMetadataCharacteristicValue hash]
+ -[HAPMetadataCharacteristicValue isEqual:]
+ -[HAPMetadataProperty hash]
+ -[HAPMetadataProperty isEqual:]
+ -[HAPMetadataService hash]
+ -[HAPMetadataService isEqual:]
+ -[HAPMetadataUnit hash]
+ -[HAPMetadataUnit isEqual:]
+ GCC_except_table1053
+ GCC_except_table1057
+ GCC_except_table1070
+ GCC_except_table1075
+ GCC_except_table1084
+ GCC_except_table1086
+ GCC_except_table1088
+ GCC_except_table1090
+ GCC_except_table1216
+ GCC_except_table1220
+ GCC_except_table1222
+ GCC_except_table1435
+ GCC_except_table1641
+ GCC_except_table1644
+ GCC_except_table1652
+ GCC_except_table1654
+ GCC_except_table1660
+ GCC_except_table1662
+ GCC_except_table1666
+ GCC_except_table1670
+ GCC_except_table1672
+ GCC_except_table1677
+ GCC_except_table1681
+ GCC_except_table1691
+ GCC_except_table1699
+ GCC_except_table1706
+ GCC_except_table1710
+ GCC_except_table1714
+ GCC_except_table1718
+ GCC_except_table1720
+ GCC_except_table1869
+ GCC_except_table1874
+ GCC_except_table1876
+ GCC_except_table1878
+ GCC_except_table1887
+ GCC_except_table1889
+ GCC_except_table1893
+ GCC_except_table1896
+ GCC_except_table1898
+ GCC_except_table1901
+ GCC_except_table1918
+ GCC_except_table1921
+ GCC_except_table1923
+ GCC_except_table1925
+ GCC_except_table1929
+ GCC_except_table1932
+ GCC_except_table1936
+ GCC_except_table1938
+ GCC_except_table1941
+ GCC_except_table1944
+ GCC_except_table1946
+ GCC_except_table1948
+ GCC_except_table1952
+ GCC_except_table1956
+ GCC_except_table1964
+ GCC_except_table1975
+ GCC_except_table2013
+ GCC_except_table2019
+ GCC_except_table2190
+ GCC_except_table2197
+ GCC_except_table2203
+ GCC_except_table2209
+ GCC_except_table2212
+ GCC_except_table2215
+ GCC_except_table2218
+ GCC_except_table2224
+ GCC_except_table2226
+ GCC_except_table2231
+ GCC_except_table2233
+ GCC_except_table2329
+ GCC_except_table2342
+ GCC_except_table2357
+ GCC_except_table2371
+ GCC_except_table2451
+ GCC_except_table2463
+ GCC_except_table2489
+ GCC_except_table2497
+ GCC_except_table2508
+ GCC_except_table2522
+ GCC_except_table2525
+ GCC_except_table2530
+ GCC_except_table2538
+ GCC_except_table2544
+ GCC_except_table2546
+ GCC_except_table2720
+ GCC_except_table2770
+ GCC_except_table2786
+ GCC_except_table2789
+ GCC_except_table2804
+ GCC_except_table2811
+ GCC_except_table2826
+ GCC_except_table2839
+ GCC_except_table2841
+ GCC_except_table2847
+ GCC_except_table2854
+ GCC_except_table2857
+ GCC_except_table2862
+ GCC_except_table2918
+ GCC_except_table2921
+ GCC_except_table2926
+ GCC_except_table2928
+ GCC_except_table2942
+ GCC_except_table2956
+ GCC_except_table2958
+ GCC_except_table2962
+ GCC_except_table2970
+ GCC_except_table2978
+ GCC_except_table3027
+ GCC_except_table3035
+ GCC_except_table3038
+ GCC_except_table3061
+ GCC_except_table3305
+ GCC_except_table3370
+ GCC_except_table3374
+ GCC_except_table3377
+ GCC_except_table3380
+ GCC_except_table3383
+ GCC_except_table3385
+ GCC_except_table3392
+ GCC_except_table3402
+ GCC_except_table3405
+ GCC_except_table3417
+ GCC_except_table3419
+ GCC_except_table3421
+ GCC_except_table3424
+ GCC_except_table3427
+ GCC_except_table3429
+ GCC_except_table3432
+ GCC_except_table3435
+ GCC_except_table3447
+ GCC_except_table3449
+ GCC_except_table3453
+ GCC_except_table3457
+ GCC_except_table3461
+ GCC_except_table3487
+ GCC_except_table3505
+ GCC_except_table3509
+ GCC_except_table3512
+ GCC_except_table3514
+ GCC_except_table3516
+ GCC_except_table3604
+ GCC_except_table3644
+ GCC_except_table3670
+ GCC_except_table3770
+ GCC_except_table3777
+ GCC_except_table3799
+ GCC_except_table3802
+ GCC_except_table3805
+ GCC_except_table3808
+ GCC_except_table3811
+ GCC_except_table3814
+ GCC_except_table3817
+ GCC_except_table3820
+ GCC_except_table3823
+ GCC_except_table3838
+ GCC_except_table3841
+ GCC_except_table3852
+ GCC_except_table3860
+ GCC_except_table3871
+ GCC_except_table3872
+ GCC_except_table3876
+ GCC_except_table3877
+ GCC_except_table3895
+ GCC_except_table3897
+ GCC_except_table3900
+ GCC_except_table3903
+ GCC_except_table3914
+ GCC_except_table3920
+ GCC_except_table3922
+ GCC_except_table3925
+ GCC_except_table3948
+ GCC_except_table3950
+ GCC_except_table3959
+ GCC_except_table3965
+ GCC_except_table4225
+ GCC_except_table4231
+ GCC_except_table4248
+ GCC_except_table4252
+ GCC_except_table4269
+ GCC_except_table4288
+ GCC_except_table4302
+ GCC_except_table4306
+ GCC_except_table4419
+ GCC_except_table4483
+ GCC_except_table4491
+ GCC_except_table4501
+ GCC_except_table4543
+ GCC_except_table4546
+ GCC_except_table4547
+ GCC_except_table4548
+ GCC_except_table4549
+ GCC_except_table4631
+ GCC_except_table4632
+ GCC_except_table4633
+ GCC_except_table4635
+ GCC_except_table4636
+ GCC_except_table4642
+ GCC_except_table4643
+ GCC_except_table4645
+ GCC_except_table4652
+ GCC_except_table4655
+ GCC_except_table4657
+ GCC_except_table4662
+ GCC_except_table4665
+ GCC_except_table4668
+ GCC_except_table4672
+ GCC_except_table4676
+ GCC_except_table4705
+ GCC_except_table4706
+ GCC_except_table4735
+ GCC_except_table4738
+ GCC_except_table4743
+ GCC_except_table4746
+ GCC_except_table5010
+ GCC_except_table5014
+ GCC_except_table5059
+ GCC_except_table5063
+ GCC_except_table5065
+ GCC_except_table5067
+ GCC_except_table5234
+ GCC_except_table5240
+ GCC_except_table5244
+ GCC_except_table5245
+ GCC_except_table5246
+ GCC_except_table5247
+ GCC_except_table5253
+ GCC_except_table5287
+ GCC_except_table5288
+ GCC_except_table5289
+ GCC_except_table5309
+ GCC_except_table5321
+ GCC_except_table5324
+ GCC_except_table5329
+ GCC_except_table5331
+ GCC_except_table5345
+ GCC_except_table5566
+ GCC_except_table5578
+ GCC_except_table5583
+ GCC_except_table5586
+ GCC_except_table5587
+ GCC_except_table5589
+ GCC_except_table5590
+ GCC_except_table5592
+ GCC_except_table5622
+ GCC_except_table5644
+ GCC_except_table5648
+ GCC_except_table5652
+ GCC_except_table5657
+ GCC_except_table5661
+ GCC_except_table5665
+ GCC_except_table5669
+ GCC_except_table5673
+ GCC_except_table5681
+ GCC_except_table5683
+ GCC_except_table5685
+ GCC_except_table5745
+ GCC_except_table5746
+ GCC_except_table5747
+ GCC_except_table5748
+ GCC_except_table5749
+ GCC_except_table5812
+ GCC_except_table5813
+ GCC_except_table5825
+ GCC_except_table5831
+ GCC_except_table5844
+ GCC_except_table5847
+ GCC_except_table5848
+ GCC_except_table5853
+ GCC_except_table5863
+ GCC_except_table5866
+ GCC_except_table5880
+ GCC_except_table5887
+ GCC_except_table5893
+ GCC_except_table5902
+ GCC_except_table5908
+ GCC_except_table5925
+ GCC_except_table5936
+ GCC_except_table5951
+ GCC_except_table5952
+ GCC_except_table5957
+ GCC_except_table5961
+ GCC_except_table5962
+ GCC_except_table5965
+ GCC_except_table5971
+ GCC_except_table5975
+ GCC_except_table5979
+ GCC_except_table5981
+ GCC_except_table5983
+ GCC_except_table5987
+ GCC_except_table6139
+ GCC_except_table6195
+ GCC_except_table6198
+ GCC_except_table6202
+ GCC_except_table6208
+ GCC_except_table6215
+ GCC_except_table6216
+ GCC_except_table6232
+ GCC_except_table6236
+ GCC_except_table6237
+ GCC_except_table6238
+ GCC_except_table6287
+ GCC_except_table6288
+ GCC_except_table6290
+ GCC_except_table6293
+ GCC_except_table6320
+ GCC_except_table6321
+ GCC_except_table6326
+ GCC_except_table6363
+ GCC_except_table6364
+ GCC_except_table6365
+ GCC_except_table6378
+ GCC_except_table6380
+ GCC_except_table6397
+ GCC_except_table6403
+ GCC_except_table6409
+ GCC_except_table6421
+ GCC_except_table6422
+ GCC_except_table6427
+ GCC_except_table6436
+ GCC_except_table6442
+ GCC_except_table6443
+ GCC_except_table6447
+ GCC_except_table6455
+ GCC_except_table6459
+ GCC_except_table6461
+ GCC_except_table6465
+ GCC_except_table6486
+ GCC_except_table6488
+ GCC_except_table6489
+ GCC_except_table6515
+ GCC_except_table6679
+ GCC_except_table6742
+ GCC_except_table6774
+ GCC_except_table6777
+ GCC_except_table6943
+ GCC_except_table7006
+ GCC_except_table7070
+ GCC_except_table710
+ GCC_except_table7122
+ GCC_except_table7124
+ GCC_except_table7126
+ GCC_except_table7128
+ GCC_except_table7132
+ GCC_except_table7136
+ GCC_except_table7138
+ GCC_except_table7140
+ GCC_except_table7142
+ GCC_except_table7145
+ GCC_except_table7147
+ GCC_except_table7149
+ GCC_except_table7152
+ GCC_except_table718
+ GCC_except_table7221
+ GCC_except_table7222
+ GCC_except_table7223
+ GCC_except_table7225
+ GCC_except_table7226
+ GCC_except_table7228
+ GCC_except_table7229
+ GCC_except_table7230
+ GCC_except_table7232
+ GCC_except_table7233
+ GCC_except_table7235
+ GCC_except_table7239
+ GCC_except_table7240
+ GCC_except_table7292
+ GCC_except_table7299
+ GCC_except_table7393
+ GCC_except_table7409
+ GCC_except_table7411
+ GCC_except_table7413
+ GCC_except_table7416
+ GCC_except_table7418
+ GCC_except_table7420
+ GCC_except_table7422
+ GCC_except_table7423
+ GCC_except_table7425
+ GCC_except_table7429
+ GCC_except_table7434
+ GCC_except_table752
+ GCC_except_table775
+ GCC_except_table794
+ GCC_except_table818
+ GCC_except_table822
+ GCC_except_table836
+ GCC_except_table841
+ GCC_except_table945
+ GCC_except_table947
+ _OBJC_CLASS_$_HAPAccessoryServerIPCacheData
+ _OBJC_IVAR_$_HAPAccessoryServerBrowserIP._cache
+ _OBJC_IVAR_$_HAPAccessoryServerBrowserIP._isInitialCacheRestored
+ _OBJC_IVAR_$_HAPAccessoryServerIPCacheData._bonjourDeviceInfo
+ _OBJC_IVAR_$_HAPAccessoryServerIPCacheData._socketInfo
+ _OBJC_IVAR_$_HAPHTTPClient._requestCounter
+ _OBJC_IVAR_$_HAPHTTPClient._uniqueClientIdentifier
+ _OBJC_IVAR_$_HAPMetadata._hapCharacteristicMapOffset
+ _OBJC_IVAR_$_HAPMetadata._hapCharacteristicShortUUIDToNameMapOffset
+ _OBJC_IVAR_$_HAPMetadata._hapPropertyMapOffset
+ _OBJC_IVAR_$_HAPMetadata._hapServiceBTLEShortUUIDToNameMapOffset
+ _OBJC_IVAR_$_HAPMetadata._hapServiceMapOffset
+ _OBJC_IVAR_$_HAPMetadata._hapServiceShortUUIDToNameMapOffset
+ _OBJC_IVAR_$_HAPMetadata._hapSupportsAuthDataSetOffset
+ _OBJC_IVAR_$_HAPMetadata._hapUnitMapOffset
+ _OBJC_IVAR_$_HAPMetadata._metadata
+ _OBJC_METACLASS_$_HAPAccessoryServerIPCacheData
+ __CopyPairingIdentityDelegateCallback_f.15205
+ __CopyPairingIdentityDelegateCallback_f.21966
+ __CopyPairingIdentityDelegateCallback_f.2810
+ __FindPairedPeerDelegateCallback_f.2809
+ __OBJC_$_CLASS_METHODS_HAPAccessoryServerIPCacheData
+ __OBJC_$_INSTANCE_METHODS_HAPAccessoryServerIPCacheData
+ __OBJC_$_INSTANCE_VARIABLES_HAPAccessoryServerIPCacheData
+ __OBJC_$_PROP_LIST_HAPAccessoryServerIPCacheData
+ __OBJC_CLASS_RO_$_HAPAccessoryServerIPCacheData
+ __OBJC_METACLASS_RO_$_HAPAccessoryServerIPCacheData
+ __PairSetupPromptForSetupCodeDelegateCallback_f.21968
+ __SavePairedPeerDelegateCallback_f.15196
+ __SavePairedPeerDelegateCallback_f.21963
+ ___104-[_HAPAccessoryServerBTLE200 readCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.383
+ ___105-[_HAPAccessoryServerBTLE200 writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.442
+ ___105-[_HAPAccessoryServerBTLE200 writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.443
+ ___106-[_HAPAccessoryServerBTLE200 removePairingForCurrentControllerOnQueue:completion:serverPairingCompletion:]_block_invoke.735
+ ___106-[_HAPAccessoryServerBTLE200 removePairingForCurrentControllerOnQueue:completion:serverPairingCompletion:]_block_invoke.736
+ ___108-[HAPAccessoryServerIP _performExecuteWriteValues:prepareIdentifier:timeout:expiry:queue:completionHandler:]_block_invoke.283
+ ___108-[HAPAccessoryServerIP _performExecuteWriteValues:prepareIdentifier:timeout:expiry:queue:completionHandler:]_block_invoke.284
+ ___115-[HAPAccessoryServerIP _handleWriteECONNResetError:writeRequests:responses:timeout:expiry:queue:completionHandler:]_block_invoke.265
+ ___120-[HAPAccessoryServerIP _handleReadECONNRESETError:readCharacteristics:responses:timeout:expiry:queue:completionHandler:]_block_invoke.209
+ ___26-[HAPMetadata hapServices]_block_invoke
+ ___28-[HAPMetadata hapProperties]_block_invoke
+ ___28-[HAPMetadata hapValueUnits]_block_invoke
+ ___33-[HAPMetadata hapCharacteristics]_block_invoke
+ ___40-[HAPMetadata hapSupportsAuthDataTuples]_block_invoke
+ ___41-[HAPAccessoryServerIP getAccessoryInfo:]_block_invoke.524
+ ___44+[HAPAccessoryServerIPCacheData logCategory]_block_invoke
+ ___45-[HAPAccessoryServerIP stopPairingWithError:]_block_invoke.164
+ ___47-[HAPAccessoryServerIP identifyWithCompletion:]_block_invoke.653
+ ___48-[HAPAccessoryServerIP startPairingWithRequest:]_block_invoke.162
+ ___49-[HAPAccessoryServerIP authSession:authComplete:]_block_invoke.570
+ ___50-[HAPAccessoryServerIP networkMonitorIsReachable:]_block_invoke.519
+ ___50-[_HAPAccessoryServerBTLE200 _checkForAuthPrompt:]_block_invoke.635
+ ___50-[_HAPAccessoryServerBTLE200 _checkForAuthPrompt:]_block_invoke.642
+ ___50-[_HAPAccessoryServerBTLE200 _checkForAuthPrompt:]_block_invoke.646
+ ___50-[_HAPAccessoryServerBTLE200 isReadyForOperation:]_block_invoke.834
+ ___53-[HAPAccessoryServerIP setPairVerifyCompletionBlock:]_block_invoke.423
+ ___53-[_HAPAccessoryServerBTLE200 identifyWithCompletion:]_block_invoke.758
+ ___53-[_HAPAccessoryServerBTLE200 identifyWithCompletion:]_block_invoke.765
+ ___54-[_HAPAccessoryServerBTLE200 startPairingWithRequest:]_block_invoke.624
+ ___55-[HAPAccessoryServerIP authSession:validateUUID:token:]_block_invoke.560
+ ___55-[HAPAccessoryServerIP authSession:validateUUID:token:]_block_invoke.565
+ ___55-[_HAPAccessoryServerBTLE200 authSession:authComplete:]_block_invoke.994
+ ___57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke.554
+ ___57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke_2.558
+ ___59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke.482
+ ___59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke_2.483
+ ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.460
+ ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.465
+ ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.466
+ ___59-[_HAPAccessoryServerBTLE200 peripheral:didModifyServices:]_block_invoke.959
+ ___60-[HAPAccessoryServerIP _validatePairingAuthMethod:activity:]_block_invoke.538
+ ___60-[_HAPAccessoryServerBTLE200 continuePairingAfterAuthPrompt]_block_invoke.665
+ ___63-[HAPAccessoryServerBrowserIP startDiscoveringAccessoryServers]_block_invoke_2
+ ___63-[HAPAccessoryServerBrowserIP startDiscoveringAccessoryServers]_block_invoke_3
+ ___63-[_HAPAccessoryServerBTLE200 authSession:sendAuthExchangeData:]_block_invoke.987
+ ___63-[_HAPAccessoryServerBTLE200 authSession:sendAuthExchangeData:]_block_invoke_2.990
+ ___64-[_HAPAccessoryServerBTLE200 securitySession:didCloseWithError:]_block_invoke.1012
+ ___65-[HAPAccessoryServerBrowserIP wacBrowser:didFindHAPWACAccessory:]_block_invoke.74
+ ___65-[HAPAccessoryServerIP _continuePairingAfterAuthPromptWithRetry:]_block_invoke.474
+ ___65-[HAPAccessoryServerIP _httpClientDidCloseConnectionDueToServer:]_block_invoke.428
+ ___66-[HAPAccessoryServerBrowserIP _doStartDiscoveringAccessoryServers]_block_invoke
+ ___66-[_HAPAccessoryServerBTLE200 _discoverWithType:completionHandler:]_block_invoke.213
+ ___66-[_HAPAccessoryServerBTLE200 _discoverWithType:completionHandler:]_block_invoke.214
+ ___66-[_HAPAccessoryServerBTLE200 _handlePairSetupSessionExchangeData:]_block_invoke.680
+ ___67-[HAPAccessoryServerBrowserIP wacBrowser:didRemoveHAPWACAccessory:]_block_invoke.75
+ ___67-[_HAPAccessoryServerBTLE200 _reallySendRequest:completionHandler:]_block_invoke.779
+ ___71-[_HAPAccessoryServerBTLE200 _getPairingFeaturesWithCompletionHandler:]_block_invoke.655
+ ___74-[HAPAccessoryServerBrowserIP _prePopulateBrowserFromCacheWithCompletion:]_block_invoke
+ ___74-[HAPAccessoryServerBrowserIP _prePopulateBrowserFromCacheWithCompletion:]_block_invoke_2
+ ___74-[HAPAccessoryServerBrowserIP _prePopulateBrowserFromCacheWithCompletion:]_block_invoke_3
+ ___75-[_HAPAccessoryServerBTLE200 addPairing:completionQueue:completionHandler:]_block_invoke.702
+ ___75-[_HAPAccessoryServerBTLE200 addPairing:completionQueue:completionHandler:]_block_invoke.709
+ ___75-[_HAPAccessoryServerBTLE200 addPairing:completionQueue:completionHandler:]_block_invoke.713
+ ___75-[_HAPAccessoryServerBTLE200 addPairing:completionQueue:completionHandler:]_block_invoke_2.717
+ ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke.611
+ ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.612
+ ___76-[_HAPAccessoryServerBTLE200 _sendRequest:shouldPrioritize:responseHandler:]_block_invoke.770
+ ___76-[_HAPAccessoryServerBTLE200 discoverAccessoriesAndReadCharacteristicTypes:]_block_invoke.200
+ ___76-[_HAPAccessoryServerBTLE200 discoverAccessoriesAndReadCharacteristicTypes:]_block_invoke_2.204
+ ___76-[_HAPAccessoryServerBTLE200 discoverAccessoriesAndReadCharacteristicTypes:]_block_invoke_3.205
+ ___77-[_HAPAccessoryServerBTLE200 handleDisconnectionWithError:completionHandler:]_block_invoke.843
+ ___77-[_HAPAccessoryServerBTLE200 handleDisconnectionWithError:completionHandler:]_block_invoke.848
+ ___78-[_HAPAccessoryServerBTLE200 removePairing:completionQueue:completionHandler:]_block_invoke.719
+ ___78-[_HAPAccessoryServerBTLE200 removePairing:completionQueue:completionHandler:]_block_invoke.726
+ ___78-[_HAPAccessoryServerBTLE200 removePairing:completionQueue:completionHandler:]_block_invoke.730
+ ___78-[_HAPAccessoryServerBTLE200 removePairing:completionQueue:completionHandler:]_block_invoke_2.734
+ ___79-[HAPAccessoryServerIP _queueListPairingWithCompletionQueue:completionHandler:]_block_invoke.186
+ ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1285
+ ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1287
+ ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke_2.1286
+ ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke_2.1288
+ ___79-[_HAPAccessoryServerBTLE200 generateBroadcastKey:queue:withCompletionHandler:]_block_invoke.855
+ ___80-[_HAPAccessoryServerBTLE200 _generateBroadcastKey:queue:withCompletionHandler:]_block_invoke.865
+ ___80-[_HAPAccessoryServerBTLE200 _readCharacteristicValues:queue:completionHandler:]_block_invoke.393
+ ___80-[_HAPAccessoryServerBTLE200 _readCharacteristicValues:queue:completionHandler:]_block_invoke.394
+ ___80-[_HAPAccessoryServerBTLE200 _removePairingOfAccessoryServerCancelledMidPairing]_block_invoke.193
+ ___80-[_HAPAccessoryServerBTLE200 listPairingsWithCompletionQueue:completionHandler:]_block_invoke.737
+ ___80-[_HAPAccessoryServerBTLE200 listPairingsWithCompletionQueue:completionHandler:]_block_invoke.738
+ ___80-[_HAPAccessoryServerBTLE200 listPairingsWithCompletionQueue:completionHandler:]_block_invoke.745
+ ___83-[HAPAccessoryServerBrowserIP wacBrowser:didFindUnconfiguredPairedHAPWACAccessory:]_block_invoke.78
+ ___83-[HAPAccessoryServerIP _performWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke.266
+ ___83-[HAPAccessoryServerIP _performWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke.274
+ ___83-[HAPAccessoryServerIP _performWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke_2.275
+ ___84-[_HAPAccessoryServerBTLE200 _configureCharacteristics:queue:withCompletionHandler:]_block_invoke.607
+ ___84-[_HAPAccessoryServerBTLE200 _configureCharacteristics:queue:withCompletionHandler:]_block_invoke.608
+ ___85-[HAPAccessoryServerIP _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.340
+ ___85-[HAPAccessoryServerIP _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.344
+ ___86-[HAPAccessoryServerIP _establishSecureConnectionAndFetchAttributeDatabaseWithReason:]_block_invoke.160
+ ___88-[HAPAccessoryServerIP _performTimedWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke.277
+ ___88-[HAPAccessoryServerIP _performTimedWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke_2.278
+ ___88-[HAPAccessoryServerIP _queueAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.185
+ ___88-[HAPAccessoryServerIP _startAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.584
+ ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.210
+ ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.215
+ ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.224
+ ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.234
+ ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke_2.235
+ ___89-[_HAPAccessoryServerBTLE200 _enableEvent:forCharacteristic:withCompletionHandler:queue:]_block_invoke.569
+ ___89-[_HAPAccessoryServerBTLE200 _enableEvent:forCharacteristic:withCompletionHandler:queue:]_block_invoke.570
+ ___90-[HAPAccessoryServerIP _queueEnableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.187
+ ___90-[HAPAccessoryServerIP _writeCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.254
+ ___91-[_HAPAccessoryServerBTLE200 _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.549
+ ___91-[_HAPAccessoryServerBTLE200 _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.550
+ ___91-[_HAPAccessoryServerBTLE200 _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.554
+ ___91-[_HAPAccessoryServerBTLE200 _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.555
+ ___91-[_HAPAccessoryServerBTLE200 _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.562
+ ___99-[HAPAccessoryServerIP writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.253
+ ___Block_byref_object_copy_.10722
+ ___Block_byref_object_copy_.11021
+ ___Block_byref_object_copy_.11841
+ ___Block_byref_object_copy_.12038
+ ___Block_byref_object_copy_.13039
+ ___Block_byref_object_copy_.13800
+ ___Block_byref_object_copy_.14027
+ ___Block_byref_object_copy_.15106
+ ___Block_byref_object_copy_.17262
+ ___Block_byref_object_copy_.17482
+ ___Block_byref_object_copy_.18468
+ ___Block_byref_object_copy_.19076
+ ___Block_byref_object_copy_.20180
+ ___Block_byref_object_copy_.2091
+ ___Block_byref_object_copy_.20997
+ ___Block_byref_object_copy_.25107
+ ___Block_byref_object_copy_.25273
+ ___Block_byref_object_copy_.2760
+ ___Block_byref_object_copy_.374
+ ___Block_byref_object_copy_.4322
+ ___Block_byref_object_copy_.5207
+ ___Block_byref_object_copy_.5467
+ ___Block_byref_object_copy_.5927
+ ___Block_byref_object_copy_.6553
+ ___Block_byref_object_copy_.6734
+ ___Block_byref_object_copy_.742
+ ___Block_byref_object_copy_.7552
+ ___Block_byref_object_copy_.9123
+ ___Block_byref_object_copy_.9445
+ ___Block_byref_object_copy_.9649
+ ___Block_byref_object_dispose_.10723
+ ___Block_byref_object_dispose_.11022
+ ___Block_byref_object_dispose_.11842
+ ___Block_byref_object_dispose_.12039
+ ___Block_byref_object_dispose_.13040
+ ___Block_byref_object_dispose_.13801
+ ___Block_byref_object_dispose_.14028
+ ___Block_byref_object_dispose_.15107
+ ___Block_byref_object_dispose_.17263
+ ___Block_byref_object_dispose_.17483
+ ___Block_byref_object_dispose_.18469
+ ___Block_byref_object_dispose_.19077
+ ___Block_byref_object_dispose_.20181
+ ___Block_byref_object_dispose_.2092
+ ___Block_byref_object_dispose_.20998
+ ___Block_byref_object_dispose_.25108
+ ___Block_byref_object_dispose_.25274
+ ___Block_byref_object_dispose_.2761
+ ___Block_byref_object_dispose_.375
+ ___Block_byref_object_dispose_.4323
+ ___Block_byref_object_dispose_.5208
+ ___Block_byref_object_dispose_.5468
+ ___Block_byref_object_dispose_.5928
+ ___Block_byref_object_dispose_.6554
+ ___Block_byref_object_dispose_.6735
+ ___Block_byref_object_dispose_.743
+ ___Block_byref_object_dispose_.7553
+ ___Block_byref_object_dispose_.9124
+ ___Block_byref_object_dispose_.9446
+ ___Block_byref_object_dispose_.9650
+ ___block_descriptor_40_e8_32s_e56_v32?0"NSString"8"HAPAccessoryServerIPCacheData"16^B24ls32l8
+ ___block_descriptor_48_e8_32s40s_e34_v32?0"NSString"8"NSArray"16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e39_v32?0"NSString"8"NSDictionary"16^B24ls32l8s40l8
+ ___block_literal_global.1021
+ ___block_literal_global.10396
+ ___block_literal_global.11083
+ ___block_literal_global.11837
+ ___block_literal_global.12209
+ ___block_literal_global.1304
+ ___block_literal_global.13338
+ ___block_literal_global.1341
+ ___block_literal_global.14921
+ ___block_literal_global.1513
+ ___block_literal_global.15229
+ ___block_literal_global.15661
+ ___block_literal_global.17005
+ ___block_literal_global.17272
+ ___block_literal_global.18653
+ ___block_literal_global.194
+ ___block_literal_global.19922
+ ___block_literal_global.1996
+ ___block_literal_global.20202
+ ___block_literal_global.20668
+ ___block_literal_global.21622
+ ___block_literal_global.22957
+ ___block_literal_global.23293
+ ___block_literal_global.24881
+ ___block_literal_global.25493
+ ___block_literal_global.2825
+ ___block_literal_global.3774
+ ___block_literal_global.386.7623
+ ___block_literal_global.5289
+ ___block_literal_global.5463
+ ___block_literal_global.6025
+ ___block_literal_global.6565
+ ___block_literal_global.6709
+ ___block_literal_global.7865
+ ___block_literal_global.800
+ ___block_literal_global.836
+ ___block_literal_global.8798
+ ___block_literal_global.9215
+ ___block_literal_global.9763
+ _hkConfig.21606
+ _logCategory._hmf_once_t2
+ _logCategory._hmf_once_t25
+ _logCategory._hmf_once_t35
+ _logCategory._hmf_once_t42
+ _logCategory._hmf_once_t431
+ _logCategory._hmf_once_t55
+ _logCategory._hmf_once_v26
+ _logCategory._hmf_once_v3
+ _logCategory._hmf_once_v36
+ _logCategory._hmf_once_v43
+ _logCategory._hmf_once_v432
+ _logCategory._hmf_once_v56
+ _objc_msgSend$_doStartDiscoveringAccessoryServers
+ _objc_msgSend$_prePopulateBrowserFromCacheWithCompletion:
+ _objc_msgSend$_updateCacheForDevice:socketInfo:bonjour:
+ _objc_msgSend$cache
+ _objc_msgSend$clientRequestIdentifier
+ _objc_msgSend$deleteDataForDevice:
+ _objc_msgSend$dictionaryRepresentation
+ _objc_msgSend$hapCharacteristicFromName:
+ _objc_msgSend$hapCharacteristicMapOffset
+ _objc_msgSend$hapCharacteristicShortUUIDToNameMapOffset
+ _objc_msgSend$hapPropertyMapOffset
+ _objc_msgSend$hapServiceBTLEShortUUIDToNameMapOffset
+ _objc_msgSend$hapServiceFromName:
+ _objc_msgSend$hapServiceMapOffset
+ _objc_msgSend$hapServiceShortUUIDToNameMapOffset
+ _objc_msgSend$hapSupportsAuthDataSetOffset
+ _objc_msgSend$hapSupportsAuthDataTuples
+ _objc_msgSend$hapUnitMapOffset
+ _objc_msgSend$hmf_appendObject:
+ _objc_msgSend$hmf_copyAsMemoryMappedData
+ _objc_msgSend$hmf_objectForKey:forDictionaryAtOffset:
+ _objc_msgSend$hmf_readObjectAtOffset:
+ _objc_msgSend$indexDictionary:keyPath:
+ _objc_msgSend$initWithCachedIp:bonjourRecord:
+ _objc_msgSend$initWithDictionary:
+ _objc_msgSend$isInitialCacheRestored
+ _objc_msgSend$parseCharacteristicMetadata:withName:
+ _objc_msgSend$parseCharacteristicServiceTupleMetadata:withCharacteristicName:
+ _objc_msgSend$parsePropertyMetadata:withType:
+ _objc_msgSend$parseServiceMetadata:withName:
+ _objc_msgSend$parseUnitMetadata:withName:
+ _objc_msgSend$requestCounter
+ _objc_msgSend$retrieveCachedData:
+ _objc_msgSend$saveData:forDevice:
+ _objc_msgSend$setHapCharacteristicMapOffset:
+ _objc_msgSend$setHapCharacteristicShortUUIDToNameMapOffset:
+ _objc_msgSend$setHapPropertyMapOffset:
+ _objc_msgSend$setHapServiceBTLEShortUUIDToNameMapOffset:
+ _objc_msgSend$setHapServiceMapOffset:
+ _objc_msgSend$setHapServiceShortUUIDToNameMapOffset:
+ _objc_msgSend$setHapSupportsAuthDataSetOffset:
+ _objc_msgSend$setHapUnitMapOffset:
+ _objc_msgSend$setIsInitialCacheRestored:
+ _objc_msgSend$setRequestCounter:
+ _objc_msgSend$setUniqueClientIdentifier:
+ _objc_msgSend$socketInfo
+ _objc_msgSend$uniqueClientIdentifier
+ _objc_msgSend$updateCacheForDeviceID:ipData:
+ _objc_msgSend$valueForKeyPath:
+ _sharedInstance.onceToken.15660
- -[HAPMetadata hapCharacteristicMap]
- -[HAPMetadata hapCharacteristicNameTypeMap]
- -[HAPMetadata hapPropertyMap]
- -[HAPMetadata hapServiceMap]
- -[HAPMetadata hapServiceNameTypeMap]
- -[HAPMetadata hapSupportsAuthDataSet]
- -[HAPMetadata hapUnitMap]
- -[HAPMetadata initWithServices:characteristics:units:properties:addAuthDataTuples:hapBaseUUIDSuffix:]
- -[HAPMetadata parseProperties:]
- -[HAPMetadata parseServices:]
- -[HAPMetadata parseUnits:]
- -[HAPMetadata parsedUUIDs]
- -[HAPMetadata setHapCharacteristicMap:]
- -[HAPMetadata setHapCharacteristicNameTypeMap:]
- -[HAPMetadata setHapPropertyMap:]
- -[HAPMetadata setHapServiceMap:]
- -[HAPMetadata setHapServiceNameTypeMap:]
- -[HAPMetadata setHapSupportsAuthDataSet:]
- -[HAPMetadata setHapUnitMap:]
- -[HAPMetadata setParsedUUIDs:]
- -[HAPMetadata updateRawPlist]
- GCC_except_table1052
- GCC_except_table1056
- GCC_except_table1069
- GCC_except_table1074
- GCC_except_table1083
- GCC_except_table1085
- GCC_except_table1087
- GCC_except_table1089
- GCC_except_table1215
- GCC_except_table1219
- GCC_except_table1221
- GCC_except_table1434
- GCC_except_table1640
- GCC_except_table1643
- GCC_except_table1651
- GCC_except_table1653
- GCC_except_table1659
- GCC_except_table1661
- GCC_except_table1665
- GCC_except_table1669
- GCC_except_table1671
- GCC_except_table1676
- GCC_except_table1680
- GCC_except_table1690
- GCC_except_table1698
- GCC_except_table1705
- GCC_except_table1709
- GCC_except_table1713
- GCC_except_table1717
- GCC_except_table1719
- GCC_except_table1868
- GCC_except_table1872
- GCC_except_table1875
- GCC_except_table1877
- GCC_except_table1886
- GCC_except_table1888
- GCC_except_table1892
- GCC_except_table1895
- GCC_except_table1897
- GCC_except_table1900
- GCC_except_table1917
- GCC_except_table1920
- GCC_except_table1922
- GCC_except_table1924
- GCC_except_table1928
- GCC_except_table1931
- GCC_except_table1935
- GCC_except_table1937
- GCC_except_table1940
- GCC_except_table1943
- GCC_except_table1945
- GCC_except_table1947
- GCC_except_table1951
- GCC_except_table1955
- GCC_except_table1963
- GCC_except_table1974
- GCC_except_table2012
- GCC_except_table2018
- GCC_except_table2189
- GCC_except_table2196
- GCC_except_table2202
- GCC_except_table2208
- GCC_except_table2211
- GCC_except_table2214
- GCC_except_table2217
- GCC_except_table2223
- GCC_except_table2225
- GCC_except_table2229
- GCC_except_table2232
- GCC_except_table2328
- GCC_except_table2336
- GCC_except_table2356
- GCC_except_table2370
- GCC_except_table2450
- GCC_except_table2462
- GCC_except_table2488
- GCC_except_table2496
- GCC_except_table2507
- GCC_except_table2521
- GCC_except_table2524
- GCC_except_table2529
- GCC_except_table2537
- GCC_except_table2543
- GCC_except_table2545
- GCC_except_table2719
- GCC_except_table2769
- GCC_except_table2785
- GCC_except_table2788
- GCC_except_table2802
- GCC_except_table2810
- GCC_except_table2825
- GCC_except_table2837
- GCC_except_table2840
- GCC_except_table2846
- GCC_except_table2853
- GCC_except_table2856
- GCC_except_table2861
- GCC_except_table2917
- GCC_except_table2920
- GCC_except_table2925
- GCC_except_table2927
- GCC_except_table2941
- GCC_except_table2955
- GCC_except_table2957
- GCC_except_table2961
- GCC_except_table2969
- GCC_except_table2977
- GCC_except_table3026
- GCC_except_table3034
- GCC_except_table3036
- GCC_except_table3060
- GCC_except_table3304
- GCC_except_table3368
- GCC_except_table3373
- GCC_except_table3376
- GCC_except_table3378
- GCC_except_table3381
- GCC_except_table3384
- GCC_except_table3391
- GCC_except_table3401
- GCC_except_table3404
- GCC_except_table3415
- GCC_except_table3418
- GCC_except_table3420
- GCC_except_table3423
- GCC_except_table3426
- GCC_except_table3428
- GCC_except_table3431
- GCC_except_table3434
- GCC_except_table3446
- GCC_except_table3448
- GCC_except_table3452
- GCC_except_table3456
- GCC_except_table3460
- GCC_except_table3486
- GCC_except_table3504
- GCC_except_table3508
- GCC_except_table3511
- GCC_except_table3513
- GCC_except_table3515
- GCC_except_table3590
- GCC_except_table3640
- GCC_except_table3666
- GCC_except_table3757
- GCC_except_table3764
- GCC_except_table3782
- GCC_except_table3786
- GCC_except_table3789
- GCC_except_table3792
- GCC_except_table3798
- GCC_except_table3801
- GCC_except_table3804
- GCC_except_table3807
- GCC_except_table3810
- GCC_except_table3815
- GCC_except_table3825
- GCC_except_table3839
- GCC_except_table3847
- GCC_except_table3851
- GCC_except_table3858
- GCC_except_table3859
- GCC_except_table3863
- GCC_except_table3882
- GCC_except_table3884
- GCC_except_table3886
- GCC_except_table3887
- GCC_except_table3890
- GCC_except_table3896
- GCC_except_table3901
- GCC_except_table3907
- GCC_except_table3924
- GCC_except_table3935
- GCC_except_table3946
- GCC_except_table3952
- GCC_except_table4212
- GCC_except_table4218
- GCC_except_table4235
- GCC_except_table4239
- GCC_except_table4256
- GCC_except_table4262
- GCC_except_table4289
- GCC_except_table4293
- GCC_except_table4406
- GCC_except_table4470
- GCC_except_table4478
- GCC_except_table4488
- GCC_except_table4525
- GCC_except_table4528
- GCC_except_table4529
- GCC_except_table4530
- GCC_except_table4531
- GCC_except_table4613
- GCC_except_table4614
- GCC_except_table4615
- GCC_except_table4616
- GCC_except_table4617
- GCC_except_table4618
- GCC_except_table4624
- GCC_except_table4625
- GCC_except_table4627
- GCC_except_table4637
- GCC_except_table4639
- GCC_except_table4644
- GCC_except_table4647
- GCC_except_table4650
- GCC_except_table4654
- GCC_except_table4658
- GCC_except_table4687
- GCC_except_table4688
- GCC_except_table4707
- GCC_except_table4717
- GCC_except_table4720
- GCC_except_table4728
- GCC_except_table4992
- GCC_except_table4996
- GCC_except_table5030
- GCC_except_table5034
- GCC_except_table5036
- GCC_except_table5038
- GCC_except_table5205
- GCC_except_table5211
- GCC_except_table5215
- GCC_except_table5216
- GCC_except_table5217
- GCC_except_table5218
- GCC_except_table5224
- GCC_except_table5258
- GCC_except_table5259
- GCC_except_table5260
- GCC_except_table5280
- GCC_except_table5292
- GCC_except_table5295
- GCC_except_table5300
- GCC_except_table5302
- GCC_except_table5316
- GCC_except_table5518
- GCC_except_table5530
- GCC_except_table5535
- GCC_except_table5538
- GCC_except_table5539
- GCC_except_table5541
- GCC_except_table5542
- GCC_except_table5544
- GCC_except_table5574
- GCC_except_table5596
- GCC_except_table5600
- GCC_except_table5604
- GCC_except_table5609
- GCC_except_table5613
- GCC_except_table5617
- GCC_except_table5621
- GCC_except_table5625
- GCC_except_table5633
- GCC_except_table5635
- GCC_except_table5637
- GCC_except_table5697
- GCC_except_table5698
- GCC_except_table5699
- GCC_except_table5700
- GCC_except_table5701
- GCC_except_table5760
- GCC_except_table5764
- GCC_except_table5765
- GCC_except_table5777
- GCC_except_table5783
- GCC_except_table5796
- GCC_except_table5799
- GCC_except_table5800
- GCC_except_table5805
- GCC_except_table5815
- GCC_except_table5818
- GCC_except_table5832
- GCC_except_table5839
- GCC_except_table5845
- GCC_except_table5854
- GCC_except_table5860
- GCC_except_table5861
- GCC_except_table5877
- GCC_except_table5879
- GCC_except_table5888
- GCC_except_table5903
- GCC_except_table5913
- GCC_except_table5914
- GCC_except_table5917
- GCC_except_table5923
- GCC_except_table5931
- GCC_except_table5933
- GCC_except_table5935
- GCC_except_table5939
- GCC_except_table6091
- GCC_except_table6147
- GCC_except_table6150
- GCC_except_table6154
- GCC_except_table6160
- GCC_except_table6167
- GCC_except_table6168
- GCC_except_table6184
- GCC_except_table6188
- GCC_except_table6189
- GCC_except_table6190
- GCC_except_table6239
- GCC_except_table6240
- GCC_except_table6242
- GCC_except_table6245
- GCC_except_table6272
- GCC_except_table6273
- GCC_except_table6278
- GCC_except_table6298
- GCC_except_table6315
- GCC_except_table6316
- GCC_except_table6317
- GCC_except_table6325
- GCC_except_table6330
- GCC_except_table6331
- GCC_except_table6332
- GCC_except_table6349
- GCC_except_table6355
- GCC_except_table6361
- GCC_except_table6374
- GCC_except_table6388
- GCC_except_table6395
- GCC_except_table6399
- GCC_except_table6407
- GCC_except_table6411
- GCC_except_table6413
- GCC_except_table6417
- GCC_except_table6438
- GCC_except_table6440
- GCC_except_table6441
- GCC_except_table6467
- GCC_except_table6631
- GCC_except_table6694
- GCC_except_table6726
- GCC_except_table6729
- GCC_except_table6895
- GCC_except_table6958
- GCC_except_table7022
- GCC_except_table7028
- GCC_except_table7074
- GCC_except_table7078
- GCC_except_table7080
- GCC_except_table7082
- GCC_except_table7084
- GCC_except_table7086
- GCC_except_table7088
- GCC_except_table709
- GCC_except_table7090
- GCC_except_table7092
- GCC_except_table7094
- GCC_except_table7097
- GCC_except_table7099
- GCC_except_table7101
- GCC_except_table7104
- GCC_except_table7133
- GCC_except_table716
- GCC_except_table7173
- GCC_except_table7174
- GCC_except_table7175
- GCC_except_table7177
- GCC_except_table7180
- GCC_except_table7184
- GCC_except_table7185
- GCC_except_table7187
- GCC_except_table7191
- GCC_except_table7192
- GCC_except_table7196
- GCC_except_table7251
- GCC_except_table7345
- GCC_except_table7361
- GCC_except_table7363
- GCC_except_table7365
- GCC_except_table7368
- GCC_except_table7370
- GCC_except_table7372
- GCC_except_table7374
- GCC_except_table7375
- GCC_except_table7377
- GCC_except_table7381
- GCC_except_table7386
- GCC_except_table751
- GCC_except_table774
- GCC_except_table793
- GCC_except_table817
- GCC_except_table821
- GCC_except_table835
- GCC_except_table840
- GCC_except_table944
- GCC_except_table946
- _OBJC_IVAR_$_HAPMetadata._hapCharacteristicMap
- _OBJC_IVAR_$_HAPMetadata._hapCharacteristicNameTypeMap
- _OBJC_IVAR_$_HAPMetadata._hapPropertyMap
- _OBJC_IVAR_$_HAPMetadata._hapServiceMap
- _OBJC_IVAR_$_HAPMetadata._hapServiceNameTypeMap
- _OBJC_IVAR_$_HAPMetadata._hapSupportsAuthDataSet
- _OBJC_IVAR_$_HAPMetadata._hapUnitMap
- _OBJC_IVAR_$_HAPMetadata._parsedUUIDs
- _OBJC_IVAR_$_HAPMetadata._rawPlist
- _OBJC_IVAR_$_HAPMetadataTuple._index
- __CopyPairingIdentityDelegateCallback_f.15028
- __CopyPairingIdentityDelegateCallback_f.21810
- __CopyPairingIdentityDelegateCallback_f.2828
- __FindPairedPeerDelegateCallback_f.2827
- __PairSetupPromptForSetupCodeDelegateCallback_f.21812
- __SavePairedPeerDelegateCallback_f.15027
- __SavePairedPeerDelegateCallback_f.21806
- ___104-[_HAPAccessoryServerBTLE200 readCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.381
- ___105-[_HAPAccessoryServerBTLE200 writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.439
- ___105-[_HAPAccessoryServerBTLE200 writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.440
- ___106-[_HAPAccessoryServerBTLE200 removePairingForCurrentControllerOnQueue:completion:serverPairingCompletion:]_block_invoke.733
- ___106-[_HAPAccessoryServerBTLE200 removePairingForCurrentControllerOnQueue:completion:serverPairingCompletion:]_block_invoke.734
- ___108-[HAPAccessoryServerIP _performExecuteWriteValues:prepareIdentifier:timeout:expiry:queue:completionHandler:]_block_invoke.282
- ___108-[HAPAccessoryServerIP _performExecuteWriteValues:prepareIdentifier:timeout:expiry:queue:completionHandler:]_block_invoke_4
- ___115-[HAPAccessoryServerIP _handleWriteECONNResetError:writeRequests:responses:timeout:expiry:queue:completionHandler:]_block_invoke.264
- ___120-[HAPAccessoryServerIP _handleReadECONNRESETError:readCharacteristics:responses:timeout:expiry:queue:completionHandler:]_block_invoke.208
- ___41-[HAPAccessoryServerIP getAccessoryInfo:]_block_invoke.522
- ___45-[HAPAccessoryServerIP stopPairingWithError:]_block_invoke.163
- ___47-[HAPAccessoryServerIP identifyWithCompletion:]_block_invoke.651
- ___48-[HAPAccessoryServerIP startPairingWithRequest:]_block_invoke.161
- ___49-[HAPAccessoryServerIP authSession:authComplete:]_block_invoke.568
- ___50-[HAPAccessoryServerIP networkMonitorIsReachable:]_block_invoke.517
- ___50-[_HAPAccessoryServerBTLE200 _checkForAuthPrompt:]_block_invoke.633
- ___50-[_HAPAccessoryServerBTLE200 _checkForAuthPrompt:]_block_invoke.640
- ___50-[_HAPAccessoryServerBTLE200 _checkForAuthPrompt:]_block_invoke.644
- ___50-[_HAPAccessoryServerBTLE200 isReadyForOperation:]_block_invoke.832
- ___53-[HAPAccessoryServerIP setPairVerifyCompletionBlock:]_block_invoke.421
- ___53-[_HAPAccessoryServerBTLE200 identifyWithCompletion:]_block_invoke.756
- ___53-[_HAPAccessoryServerBTLE200 identifyWithCompletion:]_block_invoke.763
- ___54-[_HAPAccessoryServerBTLE200 startPairingWithRequest:]_block_invoke.622
- ___55-[HAPAccessoryServerIP authSession:validateUUID:token:]_block_invoke.558
- ___55-[HAPAccessoryServerIP authSession:validateUUID:token:]_block_invoke.563
- ___55-[_HAPAccessoryServerBTLE200 authSession:authComplete:]_block_invoke.992
- ___57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke.552
- ___57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke_2.556
- ___59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke.480
- ___59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke_2.481
- ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.458
- ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.463
- ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.464
- ___59-[_HAPAccessoryServerBTLE200 peripheral:didModifyServices:]_block_invoke.957
- ___60-[HAPAccessoryServerIP _validatePairingAuthMethod:activity:]_block_invoke.536
- ___60-[_HAPAccessoryServerBTLE200 continuePairingAfterAuthPrompt]_block_invoke.663
- ___63-[HAPAccessoryServerBrowserIP startDiscoveringAccessoryServers]_block_invoke.45
- ___63-[_HAPAccessoryServerBTLE200 authSession:sendAuthExchangeData:]_block_invoke.985
- ___63-[_HAPAccessoryServerBTLE200 authSession:sendAuthExchangeData:]_block_invoke_2.988
- ___64-[_HAPAccessoryServerBTLE200 securitySession:didCloseWithError:]_block_invoke.1010
- ___65-[HAPAccessoryServerBrowserIP wacBrowser:didFindHAPWACAccessory:]_block_invoke.72
- ___65-[HAPAccessoryServerIP _continuePairingAfterAuthPromptWithRetry:]_block_invoke.472
- ___65-[HAPAccessoryServerIP _httpClientDidCloseConnectionDueToServer:]_block_invoke.426
- ___66-[_HAPAccessoryServerBTLE200 _discoverWithType:completionHandler:]_block_invoke.211
- ___66-[_HAPAccessoryServerBTLE200 _discoverWithType:completionHandler:]_block_invoke.212
- ___66-[_HAPAccessoryServerBTLE200 _handlePairSetupSessionExchangeData:]_block_invoke.678
- ___67-[HAPAccessoryServerBrowserIP wacBrowser:didRemoveHAPWACAccessory:]_block_invoke.73
- ___67-[_HAPAccessoryServerBTLE200 _reallySendRequest:completionHandler:]_block_invoke.777
- ___71-[_HAPAccessoryServerBTLE200 _getPairingFeaturesWithCompletionHandler:]_block_invoke.653
- ___75-[_HAPAccessoryServerBTLE200 addPairing:completionQueue:completionHandler:]_block_invoke.700
- ___75-[_HAPAccessoryServerBTLE200 addPairing:completionQueue:completionHandler:]_block_invoke.707
- ___75-[_HAPAccessoryServerBTLE200 addPairing:completionQueue:completionHandler:]_block_invoke.711
- ___75-[_HAPAccessoryServerBTLE200 addPairing:completionQueue:completionHandler:]_block_invoke_2.715
- ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke.607
- ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.608
- ___76-[_HAPAccessoryServerBTLE200 _sendRequest:shouldPrioritize:responseHandler:]_block_invoke.768
- ___76-[_HAPAccessoryServerBTLE200 discoverAccessoriesAndReadCharacteristicTypes:]_block_invoke.198
- ___76-[_HAPAccessoryServerBTLE200 discoverAccessoriesAndReadCharacteristicTypes:]_block_invoke_2.202
- ___76-[_HAPAccessoryServerBTLE200 discoverAccessoriesAndReadCharacteristicTypes:]_block_invoke_3.203
- ___77-[_HAPAccessoryServerBTLE200 handleDisconnectionWithError:completionHandler:]_block_invoke.841
- ___77-[_HAPAccessoryServerBTLE200 handleDisconnectionWithError:completionHandler:]_block_invoke.846
- ___78-[_HAPAccessoryServerBTLE200 removePairing:completionQueue:completionHandler:]_block_invoke.717
- ___78-[_HAPAccessoryServerBTLE200 removePairing:completionQueue:completionHandler:]_block_invoke.724
- ___78-[_HAPAccessoryServerBTLE200 removePairing:completionQueue:completionHandler:]_block_invoke.728
- ___78-[_HAPAccessoryServerBTLE200 removePairing:completionQueue:completionHandler:]_block_invoke_2.732
- ___79-[HAPAccessoryServerIP _queueListPairingWithCompletionQueue:completionHandler:]_block_invoke.185
- ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1281
- ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1282
- ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke_2.1283
- ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke_2.1285
- ___79-[_HAPAccessoryServerBTLE200 generateBroadcastKey:queue:withCompletionHandler:]_block_invoke.853
- ___80-[_HAPAccessoryServerBTLE200 _generateBroadcastKey:queue:withCompletionHandler:]_block_invoke.863
- ___80-[_HAPAccessoryServerBTLE200 _readCharacteristicValues:queue:completionHandler:]_block_invoke.391
- ___80-[_HAPAccessoryServerBTLE200 _readCharacteristicValues:queue:completionHandler:]_block_invoke.392
- ___80-[_HAPAccessoryServerBTLE200 _removePairingOfAccessoryServerCancelledMidPairing]_block_invoke.191
- ___80-[_HAPAccessoryServerBTLE200 listPairingsWithCompletionQueue:completionHandler:]_block_invoke.735
- ___80-[_HAPAccessoryServerBTLE200 listPairingsWithCompletionQueue:completionHandler:]_block_invoke.736
- ___80-[_HAPAccessoryServerBTLE200 listPairingsWithCompletionQueue:completionHandler:]_block_invoke.743
- ___83-[HAPAccessoryServerBrowserIP wacBrowser:didFindUnconfiguredPairedHAPWACAccessory:]_block_invoke.76
- ___83-[HAPAccessoryServerIP _performWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke.265
- ___83-[HAPAccessoryServerIP _performWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke.273
- ___83-[HAPAccessoryServerIP _performWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke_2.274
- ___84-[_HAPAccessoryServerBTLE200 _configureCharacteristics:queue:withCompletionHandler:]_block_invoke.605
- ___84-[_HAPAccessoryServerBTLE200 _configureCharacteristics:queue:withCompletionHandler:]_block_invoke.606
- ___85-[HAPAccessoryServerIP _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.338
- ___85-[HAPAccessoryServerIP _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.342
- ___86-[HAPAccessoryServerIP _establishSecureConnectionAndFetchAttributeDatabaseWithReason:]_block_invoke.159
- ___88-[HAPAccessoryServerIP _performTimedWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke.275
- ___88-[HAPAccessoryServerIP _performTimedWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke_2.277
- ___88-[HAPAccessoryServerIP _queueAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.184
- ___88-[HAPAccessoryServerIP _startAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.582
- ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.209
- ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.214
- ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.223
- ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.233
- ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke_2.234
- ___89-[_HAPAccessoryServerBTLE200 _enableEvent:forCharacteristic:withCompletionHandler:queue:]_block_invoke.567
- ___89-[_HAPAccessoryServerBTLE200 _enableEvent:forCharacteristic:withCompletionHandler:queue:]_block_invoke.568
- ___90-[HAPAccessoryServerIP _queueEnableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.186
- ___90-[HAPAccessoryServerIP _writeCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.253
- ___91-[_HAPAccessoryServerBTLE200 _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.547
- ___91-[_HAPAccessoryServerBTLE200 _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.548
- ___91-[_HAPAccessoryServerBTLE200 _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.551
- ___91-[_HAPAccessoryServerBTLE200 _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.552
- ___91-[_HAPAccessoryServerBTLE200 _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.560
- ___99-[HAPAccessoryServerIP writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.252
- ___Block_byref_object_copy_.10631
- ___Block_byref_object_copy_.10929
- ___Block_byref_object_copy_.11749
- ___Block_byref_object_copy_.11946
- ___Block_byref_object_copy_.12947
- ___Block_byref_object_copy_.13684
- ___Block_byref_object_copy_.13912
- ___Block_byref_object_copy_.14938
- ___Block_byref_object_copy_.17108
- ___Block_byref_object_copy_.17327
- ___Block_byref_object_copy_.18314
- ___Block_byref_object_copy_.18930
- ___Block_byref_object_copy_.20032
- ___Block_byref_object_copy_.20842
- ___Block_byref_object_copy_.2116
- ___Block_byref_object_copy_.24952
- ___Block_byref_object_copy_.25118
- ___Block_byref_object_copy_.2779
- ___Block_byref_object_copy_.382
- ___Block_byref_object_copy_.4352
- ___Block_byref_object_copy_.5226
- ___Block_byref_object_copy_.5492
- ___Block_byref_object_copy_.5944
- ___Block_byref_object_copy_.6571
- ___Block_byref_object_copy_.6754
- ___Block_byref_object_copy_.752
- ___Block_byref_object_copy_.7547
- ___Block_byref_object_copy_.9042
- ___Block_byref_object_copy_.9364
- ___Block_byref_object_copy_.9568
- ___Block_byref_object_dispose_.10632
- ___Block_byref_object_dispose_.10930
- ___Block_byref_object_dispose_.11750
- ___Block_byref_object_dispose_.11947
- ___Block_byref_object_dispose_.12948
- ___Block_byref_object_dispose_.13685
- ___Block_byref_object_dispose_.13913
- ___Block_byref_object_dispose_.14939
- ___Block_byref_object_dispose_.17109
- ___Block_byref_object_dispose_.17328
- ___Block_byref_object_dispose_.18315
- ___Block_byref_object_dispose_.18931
- ___Block_byref_object_dispose_.20033
- ___Block_byref_object_dispose_.20843
- ___Block_byref_object_dispose_.2117
- ___Block_byref_object_dispose_.24953
- ___Block_byref_object_dispose_.25119
- ___Block_byref_object_dispose_.2780
- ___Block_byref_object_dispose_.383
- ___Block_byref_object_dispose_.4353
- ___Block_byref_object_dispose_.5227
- ___Block_byref_object_dispose_.5493
- ___Block_byref_object_dispose_.5945
- ___Block_byref_object_dispose_.6572
- ___Block_byref_object_dispose_.6755
- ___Block_byref_object_dispose_.753
- ___Block_byref_object_dispose_.7548
- ___Block_byref_object_dispose_.9043
- ___Block_byref_object_dispose_.9365
- ___Block_byref_object_dispose_.9569
- ___block_literal_global.1019
- ___block_literal_global.10300
- ___block_literal_global.10985
- ___block_literal_global.11745
- ___block_literal_global.12118
- ___block_literal_global.1301
- ___block_literal_global.13217
- ___block_literal_global.1338
- ___block_literal_global.15052
- ___block_literal_global.1511
- ___block_literal_global.15481
- ___block_literal_global.16843
- ___block_literal_global.17118
- ___block_literal_global.18503
- ___block_literal_global.193
- ___block_literal_global.19775
- ___block_literal_global.20054
- ___block_literal_global.2021
- ___block_literal_global.20509
- ___block_literal_global.21467
- ___block_literal_global.22802
- ___block_literal_global.23137
- ___block_literal_global.24725
- ___block_literal_global.25338
- ___block_literal_global.2846
- ___block_literal_global.3799
- ___block_literal_global.384
- ___block_literal_global.5313
- ___block_literal_global.5488
- ___block_literal_global.6041
- ___block_literal_global.6583
- ___block_literal_global.6729
- ___block_literal_global.7807
- ___block_literal_global.814
- ___block_literal_global.834
- ___block_literal_global.8710
- ___block_literal_global.9133
- ___block_literal_global.9682
- _hkConfig.21451
- _logCategory._hmf_once_t24
- _logCategory._hmf_once_t34
- _logCategory._hmf_once_t40
- _logCategory._hmf_once_t426
- _logCategory._hmf_once_t51
- _logCategory._hmf_once_v25
- _logCategory._hmf_once_v35
- _logCategory._hmf_once_v41
- _logCategory._hmf_once_v427
- _logCategory._hmf_once_v52
- _objc_msgSend$hapCharacteristicMap
- _objc_msgSend$hapCharacteristicNameTypeMap
- _objc_msgSend$hapPropertyMap
- _objc_msgSend$hapServiceMap
- _objc_msgSend$hapServiceNameTypeMap
- _objc_msgSend$hapSupportsAuthDataSet
- _objc_msgSend$hapUnitMap
- _objc_msgSend$hmf_firstObjectWithValue:forKeyPath:
- _objc_msgSend$index
- _objc_msgSend$parseCharacteristicServiceTuples:
- _objc_msgSend$parseCharacteristics:
- _objc_msgSend$parseProperties:
- _objc_msgSend$parseServices:
- _objc_msgSend$parseUnits:
- _objc_msgSend$parsedUUIDs
- _objc_msgSend$setHapCharacteristicMap:
- _objc_msgSend$setHapCharacteristicNameTypeMap:
- _objc_msgSend$setHapPropertyMap:
- _objc_msgSend$setHapServiceMap:
- _objc_msgSend$setHapServiceNameTypeMap:
- _objc_msgSend$setHapSupportsAuthDataSet:
- _objc_msgSend$setHapUnitMap:
- _objc_msgSend$setParsedUUIDs:
- _objc_msgSend$updateRawPlist
- _sharedInstance.onceToken.15480
CStrings:
+ "%04X"
+ "%04lX"
+ "%s     SO_TRAFFIC_CLASS: %d\n"
+ "%{public}@Accessory server died"
+ "%{public}@Cannot save cache for nil deviceID"
+ "%{public}@Could not init socket info for device %@ from dictionary %@"
+ "%{public}@Device id changed during pair setup: %@, %@"
+ "%{public}@Error during _PairingShowSetupCode_f, object is not a HAPSRPPairSetupSession: %@"
+ "%{public}@Error during _SavePairedPeerDelegateCallback_f with peerIdentifier: %@, peerPublicKeyData: %@, session: %@"
+ "%{public}@Error during _performExecuteWriteValues: inPrepareIdentifier is nil"
+ "%{public}@Error during open security session: the delegate is missing"
+ "%{public}@Failed to parse HAP property %@ bitPosition %@ description %@"
+ "%{public}@Failed to parse HAP unit %@ description %@"
+ "%{public}@Ignoring cache entry with null fields"
+ "%{public}@Invalid HTTP Request Method: %ud"
+ "%{public}@Invalid input dictionary %@"
+ "%{public}@Missing Bonjour Info with dnsName: %@, hasBonjourDeviceInfo: %@"
+ "%{public}@No cached IP addresses"
+ "%{public}@Pre-populate browser with cached IP Addresses"
+ "%{public}@Request to save cache with nil bonjour info ignored %@"
+ "%{public}@Retrieve data %@ for device %@"
+ "%{public}@Sending GET request to '%{public}@' (info: %@:%@ ... CID %@)"
+ "%{public}@Sending POST request to '%@' (info: %@:%@ ... CID %@)"
+ "%{public}@Sending PUT request to '%{public}@' with body %{public}@ (info: %@:%@ ... CID %@)"
+ "0000"
+ "0x%@%@"
+ "@\"<HAPAccessoryServerIPCache>\""
+ "@44@0:8@16@24S32@36"
+ "@56@0:8@16@24@32S40@44B52"
+ "@64@0:8@16@24@32@40S48B52@56"
+ "@68@0:8@16@24@32@40S48B52B56@60"
+ "AccessoryServerIPCache"
+ "Also setting SO_TRAFFIC_CLASS to %d (mapped from DSCP %d)\n"
+ "Could not get next control message header for AQM.\n"
+ "D"
+ "Failed to create characteristic with type, %@, characteristic instance ID, %@, properties, %hu"
+ "Failed to create characteristic with type, %@, characteristic instance ID, %@, properties, %hu, metadata, %@"
+ "HAPAccessoryServerIPCacheData"
+ "HAPAccessoryServerIPCacheData: socketInfo %@, bonjour %@"
+ "Setting IPV6_TCLASS to 0x%x (DSCP %d)\n"
+ "Setting IP_TOS to 0x%x (DSCP %d)\n"
+ "T@\"<HAPAccessoryServerIPCache>\",R,N,V_cache"
+ "T@\"NSArray\",&,N,V_mandatoryCharacteristics"
+ "T@\"NSArray\",&,N,V_optionalCharacteristics"
+ "T@\"NSData\",&,N,V_metadata"
+ "T@\"NSDictionary\",&,N,V_socketInfo"
+ "T@\"NSString\",C,N,V_uniqueClientIdentifier"
+ "TB,N,V_isInitialCacheRestored"
+ "TI,N,V_hapCharacteristicMapOffset"
+ "TI,N,V_hapCharacteristicShortUUIDToNameMapOffset"
+ "TI,N,V_hapPropertyMapOffset"
+ "TI,N,V_hapServiceBTLEShortUUIDToNameMapOffset"
+ "TI,N,V_hapServiceMapOffset"
+ "TI,N,V_hapServiceShortUUIDToNameMapOffset"
+ "TI,N,V_hapSupportsAuthDataSetOffset"
+ "TI,N,V_hapUnitMapOffset"
+ "TQ,N,V_requestCounter"
+ "TS,N,V_characteristicProperties"
+ "TS,N,V_properties"
+ "TS,R,N,V_characteristicProperties"
+ "Unsupported address family for DSCP/AQM. Sending without it.\n"
+ "_doStartDiscoveringAccessoryServers"
+ "_hapCharacteristicMapOffset"
+ "_hapCharacteristicShortUUIDToNameMapOffset"
+ "_hapPropertyMapOffset"
+ "_hapServiceBTLEShortUUIDToNameMapOffset"
+ "_hapServiceMapOffset"
+ "_hapServiceShortUUIDToNameMapOffset"
+ "_hapSupportsAuthDataSetOffset"
+ "_hapUnitMapOffset"
+ "_isInitialCacheRestored"
+ "_prePopulateBrowserFromCacheWithCompletion:"
+ "_requestCounter"
+ "_socketInfo"
+ "_uniqueClientIdentifier"
+ "_updateCacheForDevice:socketInfo:bonjour:"
+ "cache"
+ "clientRequestIdentifier"
+ "deleteDataForDevice:"
+ "hapCharacteristicMapOffset"
+ "hapCharacteristicShortUUIDToNameMapOffset"
+ "hapPropertyMapOffset"
+ "hapServiceBTLEShortUUIDToNameMapOffset"
+ "hapServiceMapOffset"
+ "hapServiceShortUUIDToNameMapOffset"
+ "hapSupportsAuthDataSetOffset"
+ "hapUnitMapOffset"
+ "hmf_appendObject:"
+ "hmf_copyAsMemoryMappedData"
+ "hmf_objectForKey:forDictionaryAtOffset:"
+ "hmf_readObjectAtOffset:"
+ "indexDictionary:keyPath:"
+ "initFromDictionary:"
+ "initWithCachedIp:bonjourRecord:"
+ "initWithQueue:cache:"
+ "isInitialCacheRestored"
+ "nil"
+ "nonnil"
+ "parseCharacteristicMetadata:withName:"
+ "parseCharacteristicServiceTupleMetadata:withCharacteristicName:"
+ "parsePropertyMetadata:withType:"
+ "parseServiceMetadata:withName:"
+ "parseUnitMetadata:withName:"
+ "requestCounter"
+ "retrieveCachedData:"
+ "saveData:forDevice:"
+ "setHapCharacteristicMapOffset:"
+ "setHapCharacteristicShortUUIDToNameMapOffset:"
+ "setHapPropertyMapOffset:"
+ "setHapServiceBTLEShortUUIDToNameMapOffset:"
+ "setHapServiceMapOffset:"
+ "setHapServiceShortUUIDToNameMapOffset:"
+ "setHapSupportsAuthDataSetOffset:"
+ "setHapUnitMapOffset:"
+ "setIsInitialCacheRestored:"
+ "setRequestCounter:"
+ "setSocketInfo:"
+ "setUniqueClientIdentifier:"
+ "socketInfo"
+ "uniqueClientIdentifier"
+ "updateCacheForDeviceID:ipData:"
+ "v32@?0@\"NSString\"8@\"HAPAccessoryServerIPCacheData\"16^B24"
+ "v32@?0@\"NSString\"8@\"NSArray\"16^B24"
+ "v32@?0@\"NSString\"8@\"NSDictionary\"16^B24"
+ "valueForKeyPath:"
+ "\x81"
- "\f"
- "%{public}@Failed to parse HAP addAuthData tuples: %@"
- "%{public}@Failed to parse HAP characteristics: %@"
- "%{public}@Failed to parse HAP properties: %@"
- "%{public}@Failed to parse HAP property %@  bitPosition %@ description %@"
- "%{public}@Failed to parse HAP services: %@"
- "%{public}@Failed to parse HAP unit %@  description %@"
- "%{public}@Failed to parse HAP units: %@"
- "%{public}@No HAP characteristics"
- "%{public}@Sending GET request to '%{public}@' (info: %@:%@ ... CID 0x%X)"
- "%{public}@Sending POST request to '%@' (info: %@:%@ ... CID 0x%X)"
- "%{public}@Sending PUT request to '%{public}@' with body %{public}@ (info: %@:%@ ... CID 0x%X)"
- "%{public}@characteristic %@: UUID %@ is already defined in the metadata"
- "%{public}@service %@: BTLE UUID %@ is already defined in the metadata"
- "%{public}@service %@: UUID %@ is already defined in the metadata"
- "@60@0:8@16@24@32Q40@48B56"
- "@68@0:8@16@24@32@40Q48B56@60"
- "@72@0:8@16@24@32@40Q48B56B60@64"
- "AF_INET: Setting IP_TOS to 0x%x (DSCP %d)\n"
- "Failed to create characteristic with type, %@, characteristic instance ID, %@, properties, %tu"
- "Failed to create characteristic with type, %@, characteristic instance ID, %@, properties, %tu, metadata, %@"
- "T@\"NSDictionary\",&,N,V_hapCharacteristicMap"
- "T@\"NSDictionary\",&,N,V_hapCharacteristicNameTypeMap"
- "T@\"NSDictionary\",&,N,V_hapPropertyMap"
- "T@\"NSDictionary\",&,N,V_hapServiceMap"
- "T@\"NSDictionary\",&,N,V_hapServiceNameTypeMap"
- "T@\"NSDictionary\",&,N,V_hapUnitMap"
- "T@\"NSDictionary\",R,N,V_rawPlist"
- "T@\"NSMutableArray\",&,N,V_parsedUUIDs"
- "T@\"NSSet\",&,N,V_hapSupportsAuthDataSet"
- "T@\"NSSet\",&,N,V_mandatoryCharacteristics"
- "T@\"NSSet\",&,N,V_optionalCharacteristics"
- "T@\"NSString\",R,N,V_index"
- "TQ,N,V_characteristicProperties"
- "TQ,N,V_properties"
- "TQ,R,N,V_characteristicProperties"
- "Unsupported address family for DSCP. Sending without it.\n"
- "_hapCharacteristicMap"
- "_hapCharacteristicNameTypeMap"
- "_hapPropertyMap"
- "_hapServiceMap"
- "_hapServiceNameTypeMap"
- "_hapSupportsAuthDataSet"
- "_hapUnitMap"
- "_index"
- "_parsedUUIDs"
- "_rawPlist"
- "hapCharacteristicMap"
- "hapCharacteristicNameTypeMap"
- "hapPropertyMap"
- "hapServiceMap"
- "hapServiceNameTypeMap"
- "hapSupportsAuthDataSet"
- "hapUnitMap"
- "hmf_firstObjectWithValue:forKeyPath:"
- "initWithServices:characteristics:units:properties:addAuthDataTuples:hapBaseUUIDSuffix:"
- "parseProperties:"
- "parseServices:"
- "parseUnits:"
- "parsedUUIDs"
- "setHapCharacteristicMap:"
- "setHapCharacteristicNameTypeMap:"
- "setHapPropertyMap:"
- "setHapServiceMap:"
- "setHapServiceNameTypeMap:"
- "setHapSupportsAuthDataSet:"
- "setHapUnitMap:"
- "setParsedUUIDs:"
- "updateRawPlist"

```
