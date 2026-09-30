## CoreHAP

> `/System/Library/PrivateFrameworks/CoreHAP.framework/Versions/A/CoreHAP`

```diff

-1241.4.11.0.0
-  __TEXT.__text: 0x1bfdf4
-  __TEXT.__auth_stubs: 0x1190
-  __TEXT.__objc_methlist: 0x113dc
+1278.5.13.4.2
+  __TEXT.__text: 0x1c0290
+  __TEXT.__auth_stubs: 0x11a0
+  __TEXT.__objc_methlist: 0x13130
   __TEXT.__const: 0x6d0
-  __TEXT.__gcc_except_tab: 0x5b48
-  __TEXT.__cstring: 0xfad8
-  __TEXT.__oslogstring: 0x1db2f
-  __TEXT.__unwind_info: 0x5d48
+  __TEXT.__gcc_except_tab: 0x5b64
+  __TEXT.__cstring: 0x104c8
+  __TEXT.__oslogstring: 0x1dd90
+  __TEXT.__unwind_info: 0x5aa0
   __TEXT.__objc_classname: 0x2d51
-  __TEXT.__objc_methname: 0x25190
-  __TEXT.__objc_methtype: 0x8cec
-  __TEXT.__objc_stubs: 0x17420
-  __DATA_CONST.__got: 0xa00
-  __DATA_CONST.__const: 0x1cd0
+  __TEXT.__objc_methname: 0x2541f
+  __TEXT.__objc_methtype: 0x8d3b
+  __TEXT.__objc_stubs: 0x175a0
+  __DATA_CONST.__got: 0xa08
+  __DATA_CONST.__const: 0x1cc0
   __DATA_CONST.__objc_classlist: 0x940
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x320
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x69d0
+  __DATA_CONST.__objc_selrefs: 0x6b50
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x7c0
   __DATA_CONST.__objc_arraydata: 0x208
-  __AUTH_CONST.__auth_got: 0x8d8
+  __AUTH_CONST.__auth_got: 0x8e0
   __AUTH_CONST.__const: 0x4290
-  __AUTH_CONST.__cfstring: 0xcf60
-  __AUTH_CONST.__objc_const: 0x24720
-  __AUTH_CONST.__objc_intobj: 0x4e0
+  __AUTH_CONST.__cfstring: 0xd4c0
+  __AUTH_CONST.__objc_const: 0x214a8
+  __AUTH_CONST.__objc_intobj: 0x510
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH.__objc_data: 0x5460
-  __DATA.__objc_ivar: 0x1430
-  __DATA.__data: 0x25a2
+  __DATA.__objc_ivar: 0x1438
+  __DATA.__data: 0x25aa
   __DATA.__bss: 0x401
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x820

   - /System/Library/PrivateFrameworks/HomeKitFeatures.framework/Versions/A/HomeKitFeatures
   - /System/Library/PrivateFrameworks/HomeKitMetrics.framework/Versions/A/HomeKitMetrics
   - /System/Library/PrivateFrameworks/MobileBluetooth.framework/Versions/A/MobileBluetooth
+  - /System/Library/PrivateFrameworks/MobileStoreDemoCore.framework/Versions/A/MobileStoreDemoCore
   - /System/Library/PrivateFrameworks/WirelessProximity.framework/Versions/A/WirelessProximity
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2418C68E-21E3-323A-ABBB-3D860A325FB7
-  Functions: 7411
-  Symbols:   16388
-  CStrings:  12291
+  UUID: 61397D4A-98D2-38C9-B80E-C3E841F46132
+  Functions: 7351
+  Symbols:   16427
+  CStrings:  12408
 
Symbols:
+ +[HAPAccessoryServerIP setUseDeferredResolutionStrategy:]
+ +[HAPAccessoryServerIP useDeferredResolutionStrategy]
+ +[HAPSystemKeychainStore serializeDictionary:options:]
+ +[HAPSystemKeychainStore serializeImmutableDictionary:]
+ +[NSError(HAPError) _userInfoWithDescription:reason:suggestion:underlyingError:marker:]
+ +[NSError(HAPError) hapErrorWithCode:description:reason:suggestion:underlyingError:marker:]
+ +[NSError(HAPError) hapErrorWithCode:marker:]
+ +[NSError(HAPError) hapHMErrorWithCode:description:reason:suggestion:underlyingError:marker:]
+ -[HAP2AccessoryServerController setAccessoryCache:]
+ -[HAPAccessoryServerIP _populateSocketUpdateType]
+ -[HAPAccessoryServerIP _socketUpdateTypeForCachedSocketInfo:newSocketInfo:]
+ -[HAPAccessoryServerIP checkIfSuspendedAccesoryRediscovered]
+ -[HAPAccessoryServerIP currentSocketUpdateType]
+ -[HAPAccessoryServerIP setCheckIfSuspendedAccesoryRediscovered:]
+ -[HAPAccessoryServerIP setCurrentSocketUpdateType:]
+ -[HAPCoreUtilsHTTPClient getClientID]
+ -[HAPHTTPClient clientID]
+ -[HAPSuspendedAccessoryIP logIdentifier]
+ -[HAPSystemKeychainStore addKeychainItem:error:]
+ GCC_except_table1063
+ GCC_except_table1069
+ GCC_except_table1082
+ GCC_except_table1087
+ GCC_except_table1098
+ GCC_except_table1100
+ GCC_except_table1102
+ GCC_except_table1104
+ GCC_except_table1230
+ GCC_except_table1236
+ GCC_except_table1238
+ GCC_except_table1450
+ GCC_except_table1656
+ GCC_except_table1659
+ GCC_except_table1667
+ GCC_except_table1669
+ GCC_except_table1675
+ GCC_except_table1677
+ GCC_except_table1681
+ GCC_except_table1685
+ GCC_except_table1692
+ GCC_except_table1696
+ GCC_except_table1706
+ GCC_except_table1714
+ GCC_except_table1721
+ GCC_except_table1729
+ GCC_except_table1734
+ GCC_except_table1736
+ GCC_except_table1885
+ GCC_except_table1890
+ GCC_except_table1891
+ GCC_except_table1906
+ GCC_except_table1910
+ GCC_except_table1913
+ GCC_except_table1915
+ GCC_except_table1918
+ GCC_except_table1940
+ GCC_except_table1946
+ GCC_except_table1949
+ GCC_except_table1953
+ GCC_except_table1955
+ GCC_except_table1958
+ GCC_except_table1963
+ GCC_except_table1965
+ GCC_except_table1967
+ GCC_except_table1971
+ GCC_except_table1977
+ GCC_except_table1985
+ GCC_except_table1998
+ GCC_except_table2036
+ GCC_except_table2044
+ GCC_except_table2252
+ GCC_except_table2253
+ GCC_except_table2254
+ GCC_except_table2255
+ GCC_except_table2256
+ GCC_except_table2257
+ GCC_except_table2273
+ GCC_except_table2287
+ GCC_except_table2376
+ GCC_except_table2401
+ GCC_except_table2409
+ GCC_except_table2420
+ GCC_except_table2434
+ GCC_except_table2437
+ GCC_except_table2442
+ GCC_except_table2450
+ GCC_except_table2456
+ GCC_except_table2458
+ GCC_except_table2632
+ GCC_except_table2683
+ GCC_except_table2699
+ GCC_except_table2702
+ GCC_except_table2716
+ GCC_except_table2717
+ GCC_except_table2724
+ GCC_except_table2752
+ GCC_except_table2754
+ GCC_except_table2763
+ GCC_except_table2770
+ GCC_except_table2773
+ GCC_except_table2778
+ GCC_except_table2835
+ GCC_except_table2838
+ GCC_except_table2843
+ GCC_except_table2845
+ GCC_except_table2859
+ GCC_except_table2875
+ GCC_except_table2877
+ GCC_except_table2881
+ GCC_except_table2891
+ GCC_except_table2899
+ GCC_except_table2948
+ GCC_except_table2956
+ GCC_except_table2958
+ GCC_except_table2959
+ GCC_except_table2982
+ GCC_except_table3226
+ GCC_except_table3293
+ GCC_except_table3296
+ GCC_except_table3299
+ GCC_except_table3303
+ GCC_except_table3304
+ GCC_except_table3306
+ GCC_except_table3313
+ GCC_except_table3326
+ GCC_except_table3337
+ GCC_except_table3340
+ GCC_except_table3342
+ GCC_except_table3345
+ GCC_except_table3348
+ GCC_except_table3350
+ GCC_except_table3356
+ GCC_except_table3368
+ GCC_except_table3370
+ GCC_except_table3374
+ GCC_except_table3378
+ GCC_except_table3382
+ GCC_except_table3408
+ GCC_except_table3426
+ GCC_except_table3430
+ GCC_except_table3433
+ GCC_except_table3435
+ GCC_except_table3437
+ GCC_except_table3571
+ GCC_except_table3658
+ GCC_except_table3683
+ GCC_except_table3696
+ GCC_except_table3699
+ GCC_except_table3702
+ GCC_except_table3705
+ GCC_except_table3708
+ GCC_except_table3711
+ GCC_except_table3716
+ GCC_except_table3727
+ GCC_except_table3730
+ GCC_except_table3741
+ GCC_except_table3749
+ GCC_except_table3756
+ GCC_except_table3763
+ GCC_except_table3764
+ GCC_except_table3768
+ GCC_except_table3787
+ GCC_except_table3789
+ GCC_except_table3791
+ GCC_except_table3792
+ GCC_except_table3795
+ GCC_except_table3801
+ GCC_except_table3804
+ GCC_except_table3806
+ GCC_except_table3812
+ GCC_except_table3814
+ GCC_except_table3817
+ GCC_except_table3829
+ GCC_except_table3840
+ GCC_except_table3842
+ GCC_except_table3851
+ GCC_except_table3857
+ GCC_except_table4117
+ GCC_except_table4123
+ GCC_except_table4140
+ GCC_except_table4144
+ GCC_except_table4161
+ GCC_except_table4169
+ GCC_except_table417
+ GCC_except_table4196
+ GCC_except_table4200
+ GCC_except_table4308
+ GCC_except_table4372
+ GCC_except_table438
+ GCC_except_table4380
+ GCC_except_table4391
+ GCC_except_table4428
+ GCC_except_table4431
+ GCC_except_table4432
+ GCC_except_table4433
+ GCC_except_table4434
+ GCC_except_table451
+ GCC_except_table4514
+ GCC_except_table4515
+ GCC_except_table4517
+ GCC_except_table4518
+ GCC_except_table4525
+ GCC_except_table4528
+ GCC_except_table4535
+ GCC_except_table4538
+ GCC_except_table4545
+ GCC_except_table4548
+ GCC_except_table4551
+ GCC_except_table4555
+ GCC_except_table4559
+ GCC_except_table4588
+ GCC_except_table4608
+ GCC_except_table4618
+ GCC_except_table4621
+ GCC_except_table4626
+ GCC_except_table4629
+ GCC_except_table487
+ GCC_except_table4891
+ GCC_except_table4895
+ GCC_except_table4929
+ GCC_except_table4933
+ GCC_except_table4935
+ GCC_except_table4937
+ GCC_except_table501
+ GCC_except_table504
+ GCC_except_table507
+ GCC_except_table510
+ GCC_except_table5100
+ GCC_except_table5104
+ GCC_except_table5105
+ GCC_except_table5106
+ GCC_except_table5107
+ GCC_except_table5113
+ GCC_except_table5147
+ GCC_except_table5148
+ GCC_except_table5149
+ GCC_except_table5169
+ GCC_except_table5181
+ GCC_except_table5184
+ GCC_except_table5189
+ GCC_except_table5191
+ GCC_except_table5205
+ GCC_except_table526
+ GCC_except_table531
+ GCC_except_table534
+ GCC_except_table541
+ GCC_except_table5418
+ GCC_except_table5430
+ GCC_except_table5435
+ GCC_except_table5438
+ GCC_except_table5439
+ GCC_except_table5441
+ GCC_except_table5442
+ GCC_except_table5444
+ GCC_except_table547
+ GCC_except_table5474
+ GCC_except_table5496
+ GCC_except_table5500
+ GCC_except_table5504
+ GCC_except_table5509
+ GCC_except_table5513
+ GCC_except_table5517
+ GCC_except_table5521
+ GCC_except_table5525
+ GCC_except_table5533
+ GCC_except_table5535
+ GCC_except_table5539
+ GCC_except_table5601
+ GCC_except_table5602
+ GCC_except_table5603
+ GCC_except_table5604
+ GCC_except_table5662
+ GCC_except_table5663
+ GCC_except_table5683
+ GCC_except_table570
+ GCC_except_table5700
+ GCC_except_table5705
+ GCC_except_table5708
+ GCC_except_table5715
+ GCC_except_table5718
+ GCC_except_table5732
+ GCC_except_table5739
+ GCC_except_table5745
+ GCC_except_table5754
+ GCC_except_table5756
+ GCC_except_table5762
+ GCC_except_table5763
+ GCC_except_table5778
+ GCC_except_table5780
+ GCC_except_table5788
+ GCC_except_table580
+ GCC_except_table5804
+ GCC_except_table5813
+ GCC_except_table5814
+ GCC_except_table5817
+ GCC_except_table5823
+ GCC_except_table5827
+ GCC_except_table5829
+ GCC_except_table5831
+ GCC_except_table5835
+ GCC_except_table587
+ GCC_except_table5980
+ GCC_except_table6039
+ GCC_except_table6043
+ GCC_except_table6049
+ GCC_except_table6056
+ GCC_except_table6073
+ GCC_except_table6077
+ GCC_except_table6078
+ GCC_except_table6079
+ GCC_except_table6127
+ GCC_except_table6128
+ GCC_except_table6130
+ GCC_except_table6133
+ GCC_except_table6161
+ GCC_except_table6162
+ GCC_except_table6187
+ GCC_except_table6204
+ GCC_except_table6205
+ GCC_except_table6206
+ GCC_except_table6214
+ GCC_except_table6219
+ GCC_except_table622
+ GCC_except_table6220
+ GCC_except_table6221
+ GCC_except_table6235
+ GCC_except_table6238
+ GCC_except_table624
+ GCC_except_table6244
+ GCC_except_table6250
+ GCC_except_table6262
+ GCC_except_table6263
+ GCC_except_table6268
+ GCC_except_table6277
+ GCC_except_table6285
+ GCC_except_table6286
+ GCC_except_table6290
+ GCC_except_table6298
+ GCC_except_table6302
+ GCC_except_table6304
+ GCC_except_table6308
+ GCC_except_table6329
+ GCC_except_table6331
+ GCC_except_table6332
+ GCC_except_table634
+ GCC_except_table6358
+ GCC_except_table636
+ GCC_except_table650
+ GCC_except_table6522
+ GCC_except_table6585
+ GCC_except_table660
+ GCC_except_table6617
+ GCC_except_table6620
+ GCC_except_table671
+ GCC_except_table672
+ GCC_except_table677
+ GCC_except_table6784
+ GCC_except_table680
+ GCC_except_table683
+ GCC_except_table6847
+ GCC_except_table6910
+ GCC_except_table6916
+ GCC_except_table692
+ GCC_except_table6963
+ GCC_except_table6965
+ GCC_except_table6967
+ GCC_except_table6969
+ GCC_except_table6973
+ GCC_except_table6975
+ GCC_except_table6977
+ GCC_except_table6979
+ GCC_except_table6981
+ GCC_except_table6984
+ GCC_except_table6986
+ GCC_except_table6988
+ GCC_except_table6991
+ GCC_except_table7017
+ GCC_except_table702
+ GCC_except_table703
+ GCC_except_table7040
+ GCC_except_table7041
+ GCC_except_table7042
+ GCC_except_table7044
+ GCC_except_table7045
+ GCC_except_table7047
+ GCC_except_table7048
+ GCC_except_table7049
+ GCC_except_table7051
+ GCC_except_table7052
+ GCC_except_table7054
+ GCC_except_table7058
+ GCC_except_table7059
+ GCC_except_table7063
+ GCC_except_table7111
+ GCC_except_table7118
+ GCC_except_table7230
+ GCC_except_table7232
+ GCC_except_table7235
+ GCC_except_table7237
+ GCC_except_table7239
+ GCC_except_table7241
+ GCC_except_table7242
+ GCC_except_table7244
+ GCC_except_table7248
+ GCC_except_table7253
+ GCC_except_table729
+ GCC_except_table736
+ GCC_except_table743
+ GCC_except_table744
+ GCC_except_table763
+ GCC_except_table785
+ GCC_except_table805
+ GCC_except_table829
+ GCC_except_table833
+ GCC_except_table847
+ GCC_except_table852
+ GCC_except_table954
+ GCC_except_table956
+ OBJC_IVAR_$_HAPAccessoryServerIP._checkIfSuspendedAccesoryRediscovered
+ OBJC_IVAR_$_HAPAccessoryServerIP._currentSocketUpdateType
+ _CopyPairingIdentityDelegateCallback_f.14533
+ _CopyPairingIdentityDelegateCallback_f.21200
+ _CopyPairingIdentityDelegateCallback_f.2749
+ _FindPairedPeerDelegateCallback_f.2748
+ _HAPErrorCodeFromHAPBLEStatusErrorCode
+ _HMMInternalErrorMarkerKey
+ _HTTPClientGetClientID
+ _OBJC_$_PROP_LIST_HAP2AccessoryServerBrowser.418
+ _OBJC_$_PROP_LIST_HAP2CoAPClient.245
+ _PairSetupPromptForSetupCodeDelegateCallback_f.21202
+ _SavePairedPeerDelegateCallback_f.14532
+ _SavePairedPeerDelegateCallback_f.21197
+ __102-[HAPAccessoryServerHAP2Adapter _writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.236
+ __108-[HAPAccessoryServerIP _handleWriteECONNResetError:writeRequests:responses:timeout:queue:completionHandler:]_block_invoke.283
+ __113-[HAPAccessoryServerIP _handleReadECONNRESETError:readCharacteristics:responses:timeout:queue:completionHandler:]_block_invoke.216
+ __117-[HAPHTTPClient _sendHTTPRequestToURL:withMethod:requestObject:serializationType:timeout:activity:completionHandler:]_block_invoke.43
+ __41-[HAPAccessoryServerIP getAccessoryInfo:]_block_invoke.548
+ __45-[HAPAccessoryServerIP _pairSetupContinueWAC]_block_invoke.123
+ __45-[HAPAccessoryServerIP stopPairingWithError:]_block_invoke.166
+ __46-[HAP2AccessoryServerBrowser _stopDiscovering]_block_invoke.118
+ __47-[HAPAccessoryServerIP identifyWithCompletion:]_block_invoke.683
+ __48-[HAPAccessoryServerIP startPairingWithRequest:]_block_invoke.162
+ __49-[HAPAccessoryServerIP _continuePairingAfterWAC:]_block_invoke.125
+ __49-[HAPAccessoryServerIP _continuePairingAfterWAC:]_block_invoke.130
+ __49-[HAPAccessoryServerIP authSession:authComplete:]_block_invoke.590
+ __50-[HAPAccessoryServerIP networkMonitorIsReachable:]_block_invoke.543
+ __53-[HAPAccessoryServerHAP2Adapter _printMissingValues:]_block_invoke.245
+ __53-[HAPAccessoryServerHAP2Adapter _printMissingValues:]_block_invoke.255
+ __53-[HAPAccessoryServerIP setPairVerifyCompletionBlock:]_block_invoke.450
+ __54-[HAP2AccessoryServer(Paired) _getSleepIntervalValue:]_block_invoke.316
+ __54-[HAP2AccessoryServerTransportCoAP _sendRequest:path:]_block_invoke.101
+ __56-[HAP2AccessoryServerTransportBase _closeWithOperation:]_block_invoke.43
+ __56-[HAP2AccessoryServerTransportBase _closeWithOperation:]_block_invoke.44
+ __57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke.580
+ __57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke_2.584
+ __59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke.502
+ __59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke.508
+ __59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke_2.509
+ __59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.482
+ __59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.485
+ __60-[HAPAccessoryServerIP _validatePairingAuthMethod:activity:]_block_invoke.562
+ __62-[HAP2AccessoryServerTransportBase _sendRequestWithOperation:]_block_invoke.39
+ __64-[HAP2AccessoryServer(Paired) _pollAccessoryOnQueueWithOptions:]_block_invoke.331
+ __64-[HAP2AccessoryServer(Paired) _pollAccessoryOnQueueWithOptions:]_block_invoke.338
+ __64-[HAP2AccessoryServer(Paired) _pollAccessoryOnQueueWithOptions:]_block_invoke.339
+ __65-[HAPAccessoryServerIP _continuePairingAfterAuthPromptWithRetry:]_block_invoke.493
+ __66-[HAPSystemKeychainStore _allAccessoryPairingKeysIncludingHH2Key:]_block_invoke.374
+ __72-[HAP2CoAPClient _ioThreadDidFailToSendMessageInSession:message:reason:]_block_invoke.93
+ __76-[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]_block_invoke.284
+ __76-[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]_block_invoke.292
+ __76-[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]_block_invoke_2.293
+ __76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke.637
+ __76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke.639
+ __76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.638
+ __76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.640
+ __76-[HAPSystemKeychainStore allKeychainItemsForType:identifier:syncable:error:]_block_invoke.324
+ __79-[HAPAccessoryServerIP _queueListPairingWithCompletionQueue:completionHandler:]_block_invoke.188
+ __79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1297
+ __79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1298
+ __79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1302
+ __79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke_2.1299
+ __80-[HAP2AccessoryServer(Paired) enableNotificationsForCharacteristics:completion:]_block_invoke.140
+ __80-[HAP2AccessoryServer(Paired) enableNotificationsForCharacteristics:completion:]_block_invoke_2.141
+ __80-[HAP2AccessoryServer(Paired) writeValuesForCharacteristics:timeout:completion:]_block_invoke.122
+ __80-[HAP2AccessoryServer(Paired) writeValuesForCharacteristics:timeout:completion:]_block_invoke_2.123
+ __81-[HAPAccessoryServerIP _establishSecureSessionAndRemovePairing:queue:completion:]_block_invoke.618
+ __81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke.296
+ __81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke.297
+ __81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke.298
+ __81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke_2.299
+ __82-[HAP2AccessoryServer(Paired) _handleDiscoveredAccessories:withCompletionHandler:]_block_invoke.264
+ __82-[HAP2AccessoryServer(Paired) _handleDiscoveredAccessories:withCompletionHandler:]_block_invoke.266
+ __82-[HAPAccessoryServerHAP2Adapter accessoryServer:doesRequirePermission:completion:]_block_invoke.292
+ __82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.219
+ __82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.225
+ __82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.231
+ __82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.239
+ __82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.248
+ __82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke_2.249
+ __83-[HAPAccessoryServerIP _writeCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.272
+ __85-[HAPAccessoryServerIP _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.361
+ __85-[HAPAccessoryServerIP _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.365
+ __86-[HAPAccessoryServerIP _establishSecureConnectionAndFetchAttributeDatabaseWithReason:]_block_invoke.160
+ __87-[HAPAccessoryServerBrowserIP _handleConnectionUpdateWithBonjourDeviceInfo:socketInfo:]_block_invoke.66
+ __88-[HAPAccessoryServerIP _queueAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.187
+ __88-[HAPAccessoryServerIP _startAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.604
+ __90-[HAPAccessoryServerIP _queueEnableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.190
+ __92-[HAPAccessoryServerIP writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.269
+ __93-[HAPAccessoryServerHAP2Adapter _hap2CharacteristicTuplesForHAPCharacteristics:tuples:error:]_block_invoke.267
+ __94-[HAPAccessoryServerHAP2Adapter _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.198
+ __94-[HAPAccessoryServerHAP2Adapter _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke_2.199
+ __97-[HAP2AccessoryServer(Paired) _readValuesForCharacteristics:timeout:options:activity:completion:]_block_invoke.287
+ __97-[HAP2AccessoryServer(Paired) _readValuesForCharacteristics:timeout:options:activity:completion:]_block_invoke_2.288
+ __97-[HAP2AccessoryServer(Paired) _readValuesForCharacteristics:timeout:options:activity:completion:]_block_invoke_3.289
+ __Block_byref_object_copy_.10169
+ __Block_byref_object_copy_.10454
+ __Block_byref_object_copy_.11282
+ __Block_byref_object_copy_.11481
+ __Block_byref_object_copy_.12464
+ __Block_byref_object_copy_.13170
+ __Block_byref_object_copy_.13401
+ __Block_byref_object_copy_.14438
+ __Block_byref_object_copy_.16568
+ __Block_byref_object_copy_.16789
+ __Block_byref_object_copy_.17772
+ __Block_byref_object_copy_.18372
+ __Block_byref_object_copy_.19442
+ __Block_byref_object_copy_.2025
+ __Block_byref_object_copy_.20255
+ __Block_byref_object_copy_.24106
+ __Block_byref_object_copy_.24275
+ __Block_byref_object_copy_.2697
+ __Block_byref_object_copy_.4267
+ __Block_byref_object_copy_.5129
+ __Block_byref_object_copy_.5402
+ __Block_byref_object_copy_.6183
+ __Block_byref_object_copy_.6362
+ __Block_byref_object_copy_.7120
+ __Block_byref_object_copy_.713
+ __Block_byref_object_copy_.8640
+ __Block_byref_object_copy_.8953
+ __Block_byref_object_copy_.9155
+ __Block_byref_object_dispose_.10170
+ __Block_byref_object_dispose_.10455
+ __Block_byref_object_dispose_.11283
+ __Block_byref_object_dispose_.11482
+ __Block_byref_object_dispose_.12465
+ __Block_byref_object_dispose_.13171
+ __Block_byref_object_dispose_.13402
+ __Block_byref_object_dispose_.14439
+ __Block_byref_object_dispose_.16569
+ __Block_byref_object_dispose_.16790
+ __Block_byref_object_dispose_.17773
+ __Block_byref_object_dispose_.18373
+ __Block_byref_object_dispose_.19443
+ __Block_byref_object_dispose_.20256
+ __Block_byref_object_dispose_.2026
+ __Block_byref_object_dispose_.24107
+ __Block_byref_object_dispose_.24276
+ __Block_byref_object_dispose_.2698
+ __Block_byref_object_dispose_.4268
+ __Block_byref_object_dispose_.5130
+ __Block_byref_object_dispose_.5403
+ __Block_byref_object_dispose_.6184
+ __Block_byref_object_dispose_.6363
+ __Block_byref_object_dispose_.7121
+ __Block_byref_object_dispose_.714
+ __Block_byref_object_dispose_.8641
+ __Block_byref_object_dispose_.8954
+ __Block_byref_object_dispose_.9156
+ __OBJC_$_CLASS_PROP_LIST_HAPAccessoryServerIP
+ ___48-[HAPSystemKeychainStore addKeychainItem:error:]_block_invoke
+ ___block_descriptor_48_e8_32bs40r_e197_v16?0^{HTTPMessagePrivate={__CFRuntimeBase=QAQ}^{HTTPMessagePrivate}{?=[8192c]Q*Q*Qi*Q{?=*Q*Q*Q*Q*Q*Q*Q***Q*Q}*Qi*QCQCi}CiC*QQQ[1000C]*^{?}*Q[2{iovec=^vQ}]^{iovec}iQiii^v^v^v^v^v^v^?^??iCq*iQI*}8l
+ __block_literal_global.10527
+ __block_literal_global.11278
+ __block_literal_global.11659
+ __block_literal_global.12734
+ __block_literal_global.1320
+ __block_literal_global.1357
+ __block_literal_global.14555
+ __block_literal_global.14983
+ __block_literal_global.16175
+ __block_literal_global.16583
+ __block_literal_global.17951
+ __block_literal_global.19188
+ __block_literal_global.1938
+ __block_literal_global.19466
+ __block_literal_global.199
+ __block_literal_global.19931
+ __block_literal_global.20862
+ __block_literal_global.22191
+ __block_literal_global.22516
+ __block_literal_global.230
+ __block_literal_global.238
+ __block_literal_global.23879
+ __block_literal_global.241
+ __block_literal_global.24497
+ __block_literal_global.256
+ __block_literal_global.2767
+ __block_literal_global.320
+ __block_literal_global.3717
+ __block_literal_global.408
+ __block_literal_global.469
+ __block_literal_global.5213
+ __block_literal_global.5396
+ __block_literal_global.6196
+ __block_literal_global.6336
+ __block_literal_global.7431
+ __block_literal_global.799
+ __block_literal_global.8336
+ __block_literal_global.8719
+ __block_literal_global.9266
+ __block_literal_global.9842
+ __useDeferredResolutionStrategy
+ _objc_msgSend$_populateSocketUpdateType
+ _objc_msgSend$_socketUpdateTypeForCachedSocketInfo:newSocketInfo:
+ _objc_msgSend$_userInfoWithDescription:reason:suggestion:underlyingError:marker:
+ _objc_msgSend$cachedSocketInfo
+ _objc_msgSend$checkIfSuspendedAccesoryRediscovered
+ _objc_msgSend$clientID
+ _objc_msgSend$getClientID
+ _objc_msgSend$hapErrorWithCode:description:reason:suggestion:underlyingError:marker:
+ _objc_msgSend$hapErrorWithCode:marker:
+ _objc_msgSend$hapHMErrorWithCode:description:reason:suggestion:underlyingError:marker:
+ _objc_msgSend$isOwnerPairing
+ _objc_msgSend$serializeDictionary:options:
+ _objc_msgSend$setCheckIfSuspendedAccesoryRediscovered:
+ _objc_msgSend$setCurrentSocketUpdateType:
+ _objc_msgSend$useDeferredResolutionStrategy
+ hkConfig.20846
+ logCategory._hmf_once_t23
+ logCategory._hmf_once_t35
+ logCategory._hmf_once_t391
+ logCategory._hmf_once_v24
+ logCategory._hmf_once_v36
+ logCategory._hmf_once_v392
+ sharedInstance.onceToken.14982
- +[HAPSystemKeychainStore serializeDictionary:]
- +[NSError(HAPError) _userInfoWithDescription:reason:suggestion:underlyingError:]
- GCC_except_table1054
- GCC_except_table1060
- GCC_except_table1073
- GCC_except_table1078
- GCC_except_table1089
- GCC_except_table1091
- GCC_except_table1093
- GCC_except_table1095
- GCC_except_table1221
- GCC_except_table1227
- GCC_except_table1229
- GCC_except_table1441
- GCC_except_table1647
- GCC_except_table1650
- GCC_except_table1658
- GCC_except_table1660
- GCC_except_table1666
- GCC_except_table1668
- GCC_except_table1672
- GCC_except_table1676
- GCC_except_table1678
- GCC_except_table1683
- GCC_except_table1697
- GCC_except_table1705
- GCC_except_table1712
- GCC_except_table1716
- GCC_except_table1720
- GCC_except_table1727
- GCC_except_table1876
- GCC_except_table1879
- GCC_except_table1882
- GCC_except_table1884
- GCC_except_table1899
- GCC_except_table1902
- GCC_except_table1907
- GCC_except_table1924
- GCC_except_table1927
- GCC_except_table1929
- GCC_except_table1931
- GCC_except_table1944
- GCC_except_table1947
- GCC_except_table1952
- GCC_except_table1954
- GCC_except_table1956
- GCC_except_table1960
- GCC_except_table1966
- GCC_except_table1974
- GCC_except_table1987
- GCC_except_table2024
- GCC_except_table2032
- GCC_except_table2232
- GCC_except_table2240
- GCC_except_table2241
- GCC_except_table2242
- GCC_except_table2243
- GCC_except_table2245
- GCC_except_table2261
- GCC_except_table2275
- GCC_except_table2352
- GCC_except_table2389
- GCC_except_table2397
- GCC_except_table2408
- GCC_except_table2422
- GCC_except_table2425
- GCC_except_table2430
- GCC_except_table2438
- GCC_except_table2444
- GCC_except_table2446
- GCC_except_table2620
- GCC_except_table2671
- GCC_except_table2687
- GCC_except_table2690
- GCC_except_table2704
- GCC_except_table2705
- GCC_except_table2712
- GCC_except_table2727
- GCC_except_table2740
- GCC_except_table2742
- GCC_except_table2758
- GCC_except_table2761
- GCC_except_table2766
- GCC_except_table2823
- GCC_except_table2826
- GCC_except_table2831
- GCC_except_table2833
- GCC_except_table2847
- GCC_except_table2863
- GCC_except_table2865
- GCC_except_table2869
- GCC_except_table2879
- GCC_except_table2887
- GCC_except_table2936
- GCC_except_table2944
- GCC_except_table2946
- GCC_except_table2947
- GCC_except_table2970
- GCC_except_table3214
- GCC_except_table3273
- GCC_except_table3274
- GCC_except_table3278
- GCC_except_table3281
- GCC_except_table3283
- GCC_except_table3284
- GCC_except_table3291
- GCC_except_table3308
- GCC_except_table3311
- GCC_except_table3322
- GCC_except_table3325
- GCC_except_table3327
- GCC_except_table3330
- GCC_except_table3333
- GCC_except_table3335
- GCC_except_table3341
- GCC_except_table3355
- GCC_except_table3359
- GCC_except_table3363
- GCC_except_table3367
- GCC_except_table3393
- GCC_except_table3411
- GCC_except_table3415
- GCC_except_table3418
- GCC_except_table3420
- GCC_except_table3422
- GCC_except_table3554
- GCC_except_table3640
- GCC_except_table3647
- GCC_except_table3669
- GCC_except_table3672
- GCC_except_table3675
- GCC_except_table3678
- GCC_except_table3681
- GCC_except_table3684
- GCC_except_table3698
- GCC_except_table3709
- GCC_except_table3712
- GCC_except_table3723
- GCC_except_table3731
- GCC_except_table3738
- GCC_except_table3745
- GCC_except_table3746
- GCC_except_table3750
- GCC_except_table3751
- GCC_except_table3771
- GCC_except_table3773
- GCC_except_table3774
- GCC_except_table3777
- GCC_except_table3783
- GCC_except_table3786
- GCC_except_table3788
- GCC_except_table3794
- GCC_except_table3796
- GCC_except_table3799
- GCC_except_table3811
- GCC_except_table3822
- GCC_except_table3824
- GCC_except_table3833
- GCC_except_table3839
- GCC_except_table4099
- GCC_except_table4105
- GCC_except_table4122
- GCC_except_table4126
- GCC_except_table4143
- GCC_except_table415
- GCC_except_table4151
- GCC_except_table4164
- GCC_except_table4178
- GCC_except_table4290
- GCC_except_table4354
- GCC_except_table436
- GCC_except_table4362
- GCC_except_table4373
- GCC_except_table4409
- GCC_except_table4412
- GCC_except_table4413
- GCC_except_table4414
- GCC_except_table4415
- GCC_except_table449
- GCC_except_table4495
- GCC_except_table4496
- GCC_except_table4497
- GCC_except_table4498
- GCC_except_table4499
- GCC_except_table4500
- GCC_except_table4506
- GCC_except_table4507
- GCC_except_table4509
- GCC_except_table4521
- GCC_except_table4529
- GCC_except_table4532
- GCC_except_table4536
- GCC_except_table4569
- GCC_except_table4570
- GCC_except_table4599
- GCC_except_table4602
- GCC_except_table4607
- GCC_except_table4610
- GCC_except_table485
- GCC_except_table4872
- GCC_except_table4876
- GCC_except_table4910
- GCC_except_table4914
- GCC_except_table4916
- GCC_except_table4918
- GCC_except_table499
- GCC_except_table500
- GCC_except_table505
- GCC_except_table5075
- GCC_except_table508
- GCC_except_table5081
- GCC_except_table5085
- GCC_except_table5086
- GCC_except_table5087
- GCC_except_table5088
- GCC_except_table5128
- GCC_except_table5129
- GCC_except_table5130
- GCC_except_table5150
- GCC_except_table5162
- GCC_except_table5165
- GCC_except_table5170
- GCC_except_table5172
- GCC_except_table5186
- GCC_except_table524
- GCC_except_table529
- GCC_except_table532
- GCC_except_table539
- GCC_except_table5399
- GCC_except_table5411
- GCC_except_table5416
- GCC_except_table5419
- GCC_except_table5420
- GCC_except_table5422
- GCC_except_table5423
- GCC_except_table5425
- GCC_except_table545
- GCC_except_table5455
- GCC_except_table5477
- GCC_except_table5481
- GCC_except_table5485
- GCC_except_table5490
- GCC_except_table5494
- GCC_except_table5498
- GCC_except_table5502
- GCC_except_table5506
- GCC_except_table5514
- GCC_except_table5516
- GCC_except_table5520
- GCC_except_table5582
- GCC_except_table5583
- GCC_except_table5584
- GCC_except_table5585
- GCC_except_table5643
- GCC_except_table5644
- GCC_except_table5658
- GCC_except_table566
- GCC_except_table5664
- GCC_except_table5680
- GCC_except_table5681
- GCC_except_table5686
- GCC_except_table5689
- GCC_except_table5713
- GCC_except_table5720
- GCC_except_table5726
- GCC_except_table5735
- GCC_except_table5737
- GCC_except_table5743
- GCC_except_table5744
- GCC_except_table5758
- GCC_except_table576
- GCC_except_table5760
- GCC_except_table5768
- GCC_except_table5783
- GCC_except_table5784
- GCC_except_table5789
- GCC_except_table5793
- GCC_except_table5794
- GCC_except_table5797
- GCC_except_table5807
- GCC_except_table5811
- GCC_except_table5815
- GCC_except_table583
- GCC_except_table5960
- GCC_except_table6016
- GCC_except_table6019
- GCC_except_table6023
- GCC_except_table6029
- GCC_except_table6037
- GCC_except_table6053
- GCC_except_table6058
- GCC_except_table6059
- GCC_except_table6107
- GCC_except_table6108
- GCC_except_table6110
- GCC_except_table6113
- GCC_except_table612
- GCC_except_table6141
- GCC_except_table6142
- GCC_except_table6147
- GCC_except_table618
- GCC_except_table6184
- GCC_except_table6185
- GCC_except_table6186
- GCC_except_table6194
- GCC_except_table6199
- GCC_except_table6200
- GCC_except_table6201
- GCC_except_table6215
- GCC_except_table6218
- GCC_except_table6224
- GCC_except_table6230
- GCC_except_table6242
- GCC_except_table6243
- GCC_except_table6248
- GCC_except_table6257
- GCC_except_table6265
- GCC_except_table6266
- GCC_except_table6270
- GCC_except_table6278
- GCC_except_table6282
- GCC_except_table6284
- GCC_except_table6288
- GCC_except_table630
- GCC_except_table6309
- GCC_except_table6311
- GCC_except_table6312
- GCC_except_table632
- GCC_except_table6338
- GCC_except_table646
- GCC_except_table6502
- GCC_except_table652
- GCC_except_table6565
- GCC_except_table6597
- GCC_except_table6600
- GCC_except_table667
- GCC_except_table668
- GCC_except_table673
- GCC_except_table676
- GCC_except_table6764
- GCC_except_table679
- GCC_except_table6827
- GCC_except_table684
- GCC_except_table6890
- GCC_except_table6896
- GCC_except_table694
- GCC_except_table6941
- GCC_except_table6943
- GCC_except_table6945
- GCC_except_table6947
- GCC_except_table6949
- GCC_except_table6951
- GCC_except_table6953
- GCC_except_table6955
- GCC_except_table6957
- GCC_except_table6959
- GCC_except_table6964
- GCC_except_table6966
- GCC_except_table6968
- GCC_except_table699
- GCC_except_table6997
- GCC_except_table7000
- GCC_except_table7001
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
- GCC_except_table7192
- GCC_except_table7208
- GCC_except_table7210
- GCC_except_table7215
- GCC_except_table7217
- GCC_except_table7219
- GCC_except_table7221
- GCC_except_table7222
- GCC_except_table7224
- GCC_except_table7233
- GCC_except_table725
- GCC_except_table732
- GCC_except_table739
- GCC_except_table740
- GCC_except_table759
- GCC_except_table781
- GCC_except_table799
- GCC_except_table823
- GCC_except_table827
- GCC_except_table839
- GCC_except_table844
- GCC_except_table945
- GCC_except_table947
- _CopyPairingIdentityDelegateCallback_f.14476
- _CopyPairingIdentityDelegateCallback_f.21111
- _CopyPairingIdentityDelegateCallback_f.2731
- _FindPairedPeerDelegateCallback_f.2730
- _OBJC_$_PROP_LIST_HAP2AccessoryServerBrowser.412
- _OBJC_$_PROP_LIST_HAP2CoAPClient.242
- _PairSetupPromptForSetupCodeDelegateCallback_f.21113
- _SavePairedPeerDelegateCallback_f.14475
- _SavePairedPeerDelegateCallback_f.21107
- __102-[HAPAccessoryServerHAP2Adapter _writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.227
- __108-[HAPAccessoryServerIP _handleWriteECONNResetError:writeRequests:responses:timeout:queue:completionHandler:]_block_invoke.272
- __113-[HAPAccessoryServerIP _handleReadECONNRESETError:readCharacteristics:responses:timeout:queue:completionHandler:]_block_invoke.207
- __117-[HAPHTTPClient _sendHTTPRequestToURL:withMethod:requestObject:serializationType:timeout:activity:completionHandler:]_block_invoke.40
- __41-[HAPAccessoryServerIP getAccessoryInfo:]_block_invoke.540
- __45-[HAPAccessoryServerIP _pairSetupContinueWAC]_block_invoke.120
- __45-[HAPAccessoryServerIP stopPairingWithError:]_block_invoke.157
- __46-[HAP2AccessoryServerBrowser _stopDiscovering]_block_invoke.112
- __47-[HAPAccessoryServerIP identifyWithCompletion:]_block_invoke.674
- __48-[HAPAccessoryServerIP startPairingWithRequest:]_block_invoke.153
- __49-[HAPAccessoryServerIP _continuePairingAfterWAC:]_block_invoke.122
- __49-[HAPAccessoryServerIP _continuePairingAfterWAC:]_block_invoke.127
- __49-[HAPAccessoryServerIP authSession:authComplete:]_block_invoke.579
- __50-[HAPAccessoryServerIP networkMonitorIsReachable:]_block_invoke.535
- __53-[HAPAccessoryServerHAP2Adapter _printMissingValues:]_block_invoke.236
- __53-[HAPAccessoryServerHAP2Adapter _printMissingValues:]_block_invoke.246
- __53-[HAPAccessoryServerIP setPairVerifyCompletionBlock:]_block_invoke.442
- __54-[HAP2AccessoryServer(Paired) _getSleepIntervalValue:]_block_invoke.280
- __54-[HAP2AccessoryServerTransportCoAP _sendRequest:path:]_block_invoke.95
- __56-[HAP2AccessoryServerTransportBase _closeWithOperation:]_block_invoke.37
- __56-[HAP2AccessoryServerTransportBase _closeWithOperation:]_block_invoke.38
- __57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke.569
- __57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke_2.573
- __59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke.494
- __59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke.500
- __59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke_2.501
- __59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.469
- __59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.474
- __60-[HAPAccessoryServerIP _validatePairingAuthMethod:activity:]_block_invoke.551
- __62-[HAP2AccessoryServerTransportBase _sendRequestWithOperation:]_block_invoke.33
- __64-[HAP2AccessoryServer(Paired) _pollAccessoryOnQueueWithOptions:]_block_invoke.295
- __64-[HAP2AccessoryServer(Paired) _pollAccessoryOnQueueWithOptions:]_block_invoke.302
- __64-[HAP2AccessoryServer(Paired) _pollAccessoryOnQueueWithOptions:]_block_invoke.303
- __65-[HAPAccessoryServerIP _continuePairingAfterAuthPromptWithRetry:]_block_invoke.485
- __66-[HAPSystemKeychainStore _allAccessoryPairingKeysIncludingHH2Key:]_block_invoke.352
- __72-[HAP2CoAPClient _ioThreadDidFailToSendMessageInSession:message:reason:]_block_invoke.90
- __76-[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]_block_invoke.273
- __76-[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]_block_invoke.281
- __76-[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]_block_invoke_2.282
- __76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke.628
- __76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke.630
- __76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.629
- __76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.631
- __76-[HAPSystemKeychainStore allKeychainItemsForType:identifier:syncable:error:]_block_invoke.320
- __79-[HAPAccessoryServerIP _queueListPairingWithCompletionQueue:completionHandler:]_block_invoke.179
- __79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1271
- __79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1272
- __79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1276
- __79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke_2.1273
- __80-[HAP2AccessoryServer(Paired) enableNotificationsForCharacteristics:completion:]_block_invoke.122
- __80-[HAP2AccessoryServer(Paired) enableNotificationsForCharacteristics:completion:]_block_invoke_2.123
- __80-[HAP2AccessoryServer(Paired) writeValuesForCharacteristics:timeout:completion:]_block_invoke.110
- __80-[HAP2AccessoryServer(Paired) writeValuesForCharacteristics:timeout:completion:]_block_invoke_2.111
- __81-[HAPAccessoryServerIP _establishSecureSessionAndRemovePairing:queue:completion:]_block_invoke.609
- __81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke.285
- __81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke.286
- __81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke.287
- __81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke_2.288
- __82-[HAP2AccessoryServer(Paired) _handleDiscoveredAccessories:withCompletionHandler:]_block_invoke.234
- __82-[HAP2AccessoryServer(Paired) _handleDiscoveredAccessories:withCompletionHandler:]_block_invoke.236
- __82-[HAPAccessoryServerHAP2Adapter accessoryServer:doesRequirePermission:completion:]_block_invoke.277
- __82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.208
- __82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.214
- __82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.220
- __82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.228
- __82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.237
- __82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke_2.238
- __83-[HAPAccessoryServerIP _writeCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.261
- __85-[HAPAccessoryServerIP _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.347
- __85-[HAPAccessoryServerIP _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.351
- __86-[HAPAccessoryServerIP _establishSecureConnectionAndFetchAttributeDatabaseWithReason:]_block_invoke.151
- __88-[HAPAccessoryServerIP _queueAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.178
- __88-[HAPAccessoryServerIP _startAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.595
- __90-[HAPAccessoryServerIP _queueEnableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.181
- __92-[HAPAccessoryServerIP writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.258
- __93-[HAPAccessoryServerHAP2Adapter _hap2CharacteristicTuplesForHAPCharacteristics:tuples:error:]_block_invoke.252
- __94-[HAPAccessoryServerHAP2Adapter _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.192
- __94-[HAPAccessoryServerHAP2Adapter _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke_2.193
- __97-[HAP2AccessoryServer(Paired) _readValuesForCharacteristics:timeout:options:activity:completion:]_block_invoke.251
- __97-[HAP2AccessoryServer(Paired) _readValuesForCharacteristics:timeout:options:activity:completion:]_block_invoke_2.252
- __97-[HAP2AccessoryServer(Paired) _readValuesForCharacteristics:timeout:options:activity:completion:]_block_invoke_3.253
- __Block_byref_object_copy_.10131
- __Block_byref_object_copy_.10413
- __Block_byref_object_copy_.11236
- __Block_byref_object_copy_.11435
- __Block_byref_object_copy_.12418
- __Block_byref_object_copy_.13123
- __Block_byref_object_copy_.13355
- __Block_byref_object_copy_.14391
- __Block_byref_object_copy_.16519
- __Block_byref_object_copy_.16738
- __Block_byref_object_copy_.17713
- __Block_byref_object_copy_.18321
- __Block_byref_object_copy_.19394
- __Block_byref_object_copy_.2004
- __Block_byref_object_copy_.20193
- __Block_byref_object_copy_.24012
- __Block_byref_object_copy_.24181
- __Block_byref_object_copy_.2679
- __Block_byref_object_copy_.4249
- __Block_byref_object_copy_.5125
- __Block_byref_object_copy_.5381
- __Block_byref_object_copy_.6177
- __Block_byref_object_copy_.6356
- __Block_byref_object_copy_.709
- __Block_byref_object_copy_.7111
- __Block_byref_object_copy_.8623
- __Block_byref_object_copy_.8933
- __Block_byref_object_copy_.9135
- __Block_byref_object_dispose_.10132
- __Block_byref_object_dispose_.10414
- __Block_byref_object_dispose_.11237
- __Block_byref_object_dispose_.11436
- __Block_byref_object_dispose_.12419
- __Block_byref_object_dispose_.13124
- __Block_byref_object_dispose_.13356
- __Block_byref_object_dispose_.14392
- __Block_byref_object_dispose_.16520
- __Block_byref_object_dispose_.16739
- __Block_byref_object_dispose_.17714
- __Block_byref_object_dispose_.18322
- __Block_byref_object_dispose_.19395
- __Block_byref_object_dispose_.2005
- __Block_byref_object_dispose_.20194
- __Block_byref_object_dispose_.24013
- __Block_byref_object_dispose_.24182
- __Block_byref_object_dispose_.2680
- __Block_byref_object_dispose_.4250
- __Block_byref_object_dispose_.5126
- __Block_byref_object_dispose_.5382
- __Block_byref_object_dispose_.6178
- __Block_byref_object_dispose_.6357
- __Block_byref_object_dispose_.710
- __Block_byref_object_dispose_.7112
- __Block_byref_object_dispose_.8624
- __Block_byref_object_dispose_.8934
- __Block_byref_object_dispose_.9136
- ___block_descriptor_48_e8_32bs40r_e196_v16?0^{HTTPMessagePrivate={__CFRuntimeBase=QAQ}^{HTTPMessagePrivate}{?=[8192c]Q*Q*Qi*Q{?=*Q*Q*Q*Q*Q*Q*Q***Q*Q}*Qi*QCQCi}CiC*QQQ[1000C]*^{?}*Q[2{iovec=^vQ}]^{iovec}iQiii^v^v^v^v^v^v^?^??iCq*iQI}8l
- __block_literal_global.10481
- __block_literal_global.11232
- __block_literal_global.11613
- __block_literal_global.12685
- __block_literal_global.1294
- __block_literal_global.1331
- __block_literal_global.14498
- __block_literal_global.14930
- __block_literal_global.16125
- __block_literal_global.16534
- __block_literal_global.17901
- __block_literal_global.190
- __block_literal_global.19140
- __block_literal_global.1916
- __block_literal_global.19418
- __block_literal_global.19866
- __block_literal_global.20776
- __block_literal_global.221
- __block_literal_global.22101
- __block_literal_global.22427
- __block_literal_global.229
- __block_literal_global.232
- __block_literal_global.23785
- __block_literal_global.24404
- __block_literal_global.250
- __block_literal_global.2749
- __block_literal_global.316
- __block_literal_global.3699
- __block_literal_global.386
- __block_literal_global.466
- __block_literal_global.5198
- __block_literal_global.5375
- __block_literal_global.6189
- __block_literal_global.6328
- __block_literal_global.7425
- __block_literal_global.798
- __block_literal_global.8325
- __block_literal_global.8702
- __block_literal_global.9245
- __block_literal_global.9815
- _objc_msgSend$_userInfoWithDescription:reason:suggestion:underlyingError:
- _objc_msgSend$initWithVersionString:
- _objc_msgSend$serializeDictionary:
- hkConfig.20760
- logCategory._hmf_once_t22
- logCategory._hmf_once_t33
- logCategory._hmf_once_t388
- logCategory._hmf_once_v23
- logCategory._hmf_once_v34
- logCategory._hmf_once_v389
- sharedInstance.onceToken.14929
CStrings:
+ "    Rediscovered Paired Accessory Server: %@"
+ "%@\x1e%@"
+ "%@ Canceling connection idle timer of: %fs"
+ "%@ Failed to parse protocol version from string: %@"
+ "%{public}@Canceling connection idle timer of: %0.3fs"
+ "%{public}@Completed pair-verify and caching socket info: %@:%@"
+ "%{public}@Creating socket connection using both IP and DNS Name: %@ ... %@ with output string: %@"
+ "%{public}@Received Bonjour event - canceling timer"
+ "%{public}@Received a Bonjour Add for an already discovered paired IP accessory server %{public}@ wacAccessory:%{public}@ with new BonjourDevice info: %@"
+ "%{public}@Sending GET request to '%{public}@' (info: %@:%@ ... CID 0x%x)"
+ "%{public}@Sending POST request to '%@' (info: %@:%@ ... CID 0x%x)"
+ "%{public}@Sending PUT request to '%{public}@' with body %{public}@ (info: %@:%@ ... CID 0x%x)"
+ "%{public}@[HAP HTTP Client] Setting destination to %@:%@ with CID 0x%x"
+ "%{public}@pending bonjour remove event for suspended accessory server: %{public}@ with suspendedState %lu"
+ "%{public}@pending bonjour remove event for suspended accessory server: %{public}@ with wake number %lu"
+ "/AppleInternal/Library/BuildRoots/846c37f3-0935-11f0-8504-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/HomeKit/Sources/CoreHAP/Accessories/HAPSuspendedAccessory.m"
+ "/AppleInternal/Library/BuildRoots/846c37f3-0935-11f0-8504-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/HomeKit/Sources/CoreHAP/HAP2/HAPAdapter/HAPAccessoryServerHAP2Adapter.m"
+ "/AppleInternal/Library/BuildRoots/846c37f3-0935-11f0-8504-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/HomeKit/Sources/CoreHAP/HAP2/Pairing/HAP2AccessoryServerPairingDriver.m"
+ "/AppleInternal/Library/BuildRoots/846c37f3-0935-11f0-8504-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/HomeKit/Sources/CoreHAP/HAPHTTPClient.m"
+ "/AppleInternal/Library/BuildRoots/846c37f3-0935-11f0-8504-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/HomeKit/Sources/CoreHAP/Servers/HAPAccessoryServerIP.m"
+ "/AppleInternal/Library/BuildRoots/846c37f3-0935-11f0-8504-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/HomeKit/Sources/CoreHAP/Servers/_HAPAccessoryServerBTLE200.m"
+ "@32@0:8q16q24"
+ "@56@0:8@16@24@32@40q48"
+ "@64@0:8q16@24@32@40@48q56"
+ "Accessory server transport no longer open after sending request"
+ "Attempting to create HDS keys without an active session"
+ "Base class HAPAccessoryServer does not implement validatePairingAuthMethod"
+ "COAP Response Code: %ldd"
+ "Cannot disable notifications on unpaired accessory server"
+ "Cannot enable notifications on unpaired accessory server"
+ "Cannot get characteristics while unpaired"
+ "Cannot read characteristics on unpaired accessory server"
+ "Cannot update notification configuration while unpaired"
+ "Cannot write characteristics on unpaired accessory server"
+ "DEMO"
+ "Failed to handle request because httpClient has been deallocated"
+ "HAP2 Accessory server state != HAP2AccessoryServerTransportStateOpen during completion handler of sendRequest"
+ "HAP2 CoAP failed due to HAP2CoAPIOConsumerFailureReasonNotDeliverable"
+ "HAP2AccessoryServer cannot send request when transport not open"
+ "HAP2AccessoryServer.isPaired is false during _readValuesForCharacteristics"
+ "HAP2AccessoryServer.isPaired is false during disableNotificationsForCharacteristics"
+ "HAP2AccessoryServer.isPaired is false during enableNotificationsForCharacteristics"
+ "HAP2AccessoryServer.isPaired is false during writeValuesForCharacteristics"
+ "HAP2AccessoryServerTransport state != HAP2AccessoryServerTransportStateOpen when calling sendRequestWithOperation"
+ "HAP2AccessoryServerTransportCoAP discovered 0 addresses during call to _resolveAddress"
+ "HAPAccessoryServerHAP2Adapter has nil pairedServer during _enableEvents:forCharacteristics"
+ "HAPAccessoryServerHAP2Adapter.pairedServer is nil during _hap2CharacteristicTuplesForHAPCharacteristics"
+ "HAPAccessoryServerIP._pairingSession nil during createKeysForDataStream"
+ "Lost discovery advertisement while accessory was reporting reachable"
+ "Lost paired accessory server"
+ "Lost unpaired accessory server"
+ "No advertisement"
+ "Not sending auth challenge request because the accessory doesn't claim to support it"
+ "On demand connections are enabled and the accessory is marked as reachable but lacks an advertisement"
+ "Owner Pairing"
+ "Received txtRecord that has a bad value for key '%@' ('%@'): %@"
+ "Resolved no addresses"
+ "TB"
+ "TB,N,V_checkIfSuspendedAccesoryRediscovered"
+ "TI,R,N"
+ "Tq,N,V_currentSocketUpdateType"
+ "[inKeychainItem.accessGroup isEqual:kWillowKeychainAccessGroup]"
+ "_checkIfSuspendedAccesoryRediscovered"
+ "_currentSocketUpdateType"
+ "_populateSocketUpdateType"
+ "_socketUpdateTypeForCachedSocketInfo:newSocketInfo:"
+ "_userInfoWithDescription:reason:suggestion:underlyingError:marker:"
+ "addKeychainItem:error:"
+ "checkIfSuspendedAccesoryRediscovered"
+ "clientID"
+ "currentSocketUpdateType"
+ "decryptData:additionalAuthenticatedData not supported on HAP2AccessoryServerSecureTransportBase"
+ "encryptData:additionalAuthenticatedData not supported on HAP2AccessoryServerSecureTransportBase"
+ "getClientID"
+ "hapErrorWithCode:description:reason:suggestion:underlyingError:marker:"
+ "hapErrorWithCode:marker:"
+ "hapHMErrorWithCode:description:reason:suggestion:underlyingError:marker:"
+ "i24@0:8^{HTTPMessagePrivate={__CFRuntimeBase=QAQ}^{HTTPMessagePrivate}{?=[8192c]Q*Q*Qi*Q{?=*Q*Q*Q*Q*Q*Q*Q***Q*Q}*Qi*QCQCi}CiC*QQQ[1000C]*^{?}*Q[2{iovec=^vQ}]^{iovec}iQiii^v^v^v^v^v^v^?^?@?iCq*iQI*}16"
+ "inKeychainItem.accessGroup"
+ "inKeychainItem.account"
+ "inKeychainItem.creationDate"
+ "inKeychainItem.type"
+ "inKeychainItem.viewHint"
+ "lost discovery advertisement"
+ "mtr2"
+ "mtrS"
+ "nfcA"
+ "q32@0:8@16@24"
+ "serializeDictionary:options:"
+ "serializeImmutableDictionary:"
+ "setCheckIfSuspendedAccesoryRediscovered:"
+ "setCurrentSocketUpdateType:"
+ "setUseDeferredResolutionStrategy:"
+ "useDeferredResolutionStrategy"
+ "v16@?0^{HTTPMessagePrivate={__CFRuntimeBase=QAQ}^{HTTPMessagePrivate}{?=[8192c]Q*Q*Qi*Q{?=*Q*Q*Q*Q*Q*Q*Q***Q*Q}*Qi*QCQCi}CiC*QQQ[1000C]*^{?}*Q[2{iovec=^vQ}]^{iovec}iQiii^v^v^v^v^v^v^?^?@?iCq*iQI*}8"
+ "v32@0:8^{HTTPMessagePrivate={__CFRuntimeBase=QAQ}^{HTTPMessagePrivate}{?=[8192c]Q*Q*Qi*Q{?=*Q*Q*Q*Q*Q*Q*Q***Q*Q}*Qi*QCQCi}CiC*QQQ[1000C]*^{?}*Q[2{iovec=^vQ}]^{iovec}iQiii^v^v^v^v^v^v^?^?@?iCq*iQI*}16@?24"
+ "validatePairingAuthMethod not supported on HAPAccessoryServerHAP2Adapter"
+ "\xf0\xb1"
- "%@ Failed to parse protocol version: %@"
- "%@ Suspending connection idle timer of: %fs"
- "%{public}@Received Bonjour event - suspending timer"
- "%{public}@Sending GET request to '%{public}@'"
- "%{public}@Sending POST request to '%@'"
- "%{public}@Sending PUT request to '%{public}@' with body %{public}@"
- "%{public}@Suspending connection idle timer of: %0.3fs"
- "%{public}@[HAP HTTP Client] Setting destination to %@:%@"
- "%{public}@pending bonjour remove event for suspended accessory server: %{public}@"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/HomeKit/Sources/CoreHAP/Accessories/HAPSuspendedAccessory.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/HomeKit/Sources/CoreHAP/HAP2/HAPAdapter/HAPAccessoryServerHAP2Adapter.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/HomeKit/Sources/CoreHAP/HAP2/Pairing/HAP2AccessoryServerPairingDriver.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/HomeKit/Sources/CoreHAP/HAPHTTPClient.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/HomeKit/Sources/CoreHAP/Servers/HAPAccessoryServerIP.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/HomeKit/Sources/CoreHAP/Servers/_HAPAccessoryServerBTLE200.m"
- "1.1"
- "_userInfoWithDescription:reason:suggestion:underlyingError:"
- "i24@0:8^{HTTPMessagePrivate={__CFRuntimeBase=QAQ}^{HTTPMessagePrivate}{?=[8192c]Q*Q*Qi*Q{?=*Q*Q*Q*Q*Q*Q*Q***Q*Q}*Qi*QCQCi}CiC*QQQ[1000C]*^{?}*Q[2{iovec=^vQ}]^{iovec}iQiii^v^v^v^v^v^v^?^?@?iCq*iQI}16"
- "inKeychainItem.platformReference"
- "initWithVersionString:"
- "serializeDictionary:"
- "v16@?0^{HTTPMessagePrivate={__CFRuntimeBase=QAQ}^{HTTPMessagePrivate}{?=[8192c]Q*Q*Qi*Q{?=*Q*Q*Q*Q*Q*Q*Q***Q*Q}*Qi*QCQCi}CiC*QQQ[1000C]*^{?}*Q[2{iovec=^vQ}]^{iovec}iQiii^v^v^v^v^v^v^?^?@?iCq*iQI}8"
- "v32@0:8^{HTTPMessagePrivate={__CFRuntimeBase=QAQ}^{HTTPMessagePrivate}{?=[8192c]Q*Q*Qi*Q{?=*Q*Q*Q*Q*Q*Q*Q***Q*Q}*Qi*QCQCi}CiC*QQQ[1000C]*^{?}*Q[2{iovec=^vQ}]^{iovec}iQiii^v^v^v^v^v^v^?^?@?iCq*iQI}16@?24"
- "\xf0\xa1"

```
