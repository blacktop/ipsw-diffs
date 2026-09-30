## CoreHAP

> `/System/Library/PrivateFrameworks/CoreHAP.framework/CoreHAP`

```diff

-1418.5.15.0.0
-  __TEXT.__text: 0x1e7330
+1418.6.12.0.0
+  __TEXT.__text: 0x1e71c0
   __TEXT.__auth_stubs: 0x1590
-  __TEXT.__objc_methlist: 0x162f0
+  __TEXT.__objc_methlist: 0x16348
   __TEXT.__const: 0x770
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__gcc_except_tab: 0x67f0
+  __TEXT.__gcc_except_tab: 0x6800
   __TEXT.__cstring: 0x128d5
-  __TEXT.__oslogstring: 0x210fd
-  __TEXT.__unwind_info: 0x74e0
-  __TEXT.__objc_classname: 0x3444
-  __TEXT.__objc_methname: 0x28f83
-  __TEXT.__objc_methtype: 0x9512
-  __TEXT.__objc_stubs: 0x1a180
+  __TEXT.__oslogstring: 0x2114b
+  __TEXT.__unwind_info: 0x74d8
+  __TEXT.__objc_classname: 0x3446
+  __TEXT.__objc_methname: 0x29080
+  __TEXT.__objc_methtype: 0x9538
+  __TEXT.__objc_stubs: 0x1a220
   __DATA_CONST.__got: 0xcf8
   __DATA_CONST.__const: 0x5448
   __DATA_CONST.__objc_classlist: 0xb10
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x348
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7628
+  __DATA_CONST.__objc_selrefs: 0x7660
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x980
   __DATA_CONST.__objc_arraydata: 0x208
   __AUTH_CONST.__auth_got: 0xae0
   __AUTH_CONST.__const: 0x7e0
   __AUTH_CONST.__cfstring: 0xede0
-  __AUTH_CONST.__objc_const: 0x27260
+  __AUTH_CONST.__objc_const: 0x27328
   __AUTH_CONST.__objc_intobj: 0x6f0
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH.__objc_data: 0x5f50
-  __DATA.__objc_ivar: 0x1704
+  __DATA.__objc_ivar: 0x1710
   __DATA.__data: 0x2782
   __DATA.__bss: 0x4c9
   __DATA_DIRTY.__objc_data: 0xf50

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E0F56146-69EC-3AE4-8211-2BA60E2670C0
-  Functions: 8356
-  Symbols:   26945
-  CStrings:  13751
+  UUID: F3AD385C-07FC-3576-9751-4C5D3BDD9518
+  Functions: 8359
+  Symbols:   26959
+  CStrings:  13768
 
Symbols:
+ -[HAPAccessoryServerIP setWacTeardownInProgress:]
+ -[HAPAccessoryServerIP wacTeardownInProgress]
+ -[HAPSuspendedAccessoryIP initWithName:identifier:wakeTuples:queue:shouldWake:]
+ -[HAPSuspendedAccessoryIP setShouldWake:]
+ -[HAPSuspendedAccessoryIP shouldWake]
+ -[HAPWACAccessoryClient joinAccessoryNetworkWithCompletion:joinContext:]
+ -[HAPWACAccessoryClient joinContext]
+ -[HAPWACAccessoryClient setJoinContext:]
+ GCC_except_table1097
+ GCC_except_table1101
+ GCC_except_table1114
+ GCC_except_table1119
+ GCC_except_table1128
+ GCC_except_table1130
+ GCC_except_table1132
+ GCC_except_table1134
+ GCC_except_table1260
+ GCC_except_table1264
+ GCC_except_table1266
+ GCC_except_table1479
+ GCC_except_table1687
+ GCC_except_table1689
+ GCC_except_table1694
+ GCC_except_table1700
+ GCC_except_table1702
+ GCC_except_table1708
+ GCC_except_table1710
+ GCC_except_table1714
+ GCC_except_table1718
+ GCC_except_table1720
+ GCC_except_table1725
+ GCC_except_table1729
+ GCC_except_table1739
+ GCC_except_table1747
+ GCC_except_table1754
+ GCC_except_table1758
+ GCC_except_table1762
+ GCC_except_table1766
+ GCC_except_table1802
+ GCC_except_table1922
+ GCC_except_table1926
+ GCC_except_table1929
+ GCC_except_table1931
+ GCC_except_table1941
+ GCC_except_table1943
+ GCC_except_table1947
+ GCC_except_table1950
+ GCC_except_table1952
+ GCC_except_table1955
+ GCC_except_table1972
+ GCC_except_table1979
+ GCC_except_table1981
+ GCC_except_table1983
+ GCC_except_table1987
+ GCC_except_table1990
+ GCC_except_table1994
+ GCC_except_table1996
+ GCC_except_table1999
+ GCC_except_table2002
+ GCC_except_table2004
+ GCC_except_table2006
+ GCC_except_table2010
+ GCC_except_table2014
+ GCC_except_table2022
+ GCC_except_table2033
+ GCC_except_table2077
+ GCC_except_table2083
+ GCC_except_table2252
+ GCC_except_table2259
+ GCC_except_table2265
+ GCC_except_table2269
+ GCC_except_table2273
+ GCC_except_table2276
+ GCC_except_table2279
+ GCC_except_table2281
+ GCC_except_table2284
+ GCC_except_table2290
+ GCC_except_table2292
+ GCC_except_table2297
+ GCC_except_table2299
+ GCC_except_table2395
+ GCC_except_table2408
+ GCC_except_table2423
+ GCC_except_table2437
+ GCC_except_table2517
+ GCC_except_table2529
+ GCC_except_table2555
+ GCC_except_table2563
+ GCC_except_table2574
+ GCC_except_table2588
+ GCC_except_table2591
+ GCC_except_table2596
+ GCC_except_table2604
+ GCC_except_table2610
+ GCC_except_table2612
+ GCC_except_table2787
+ GCC_except_table2837
+ GCC_except_table2853
+ GCC_except_table2856
+ GCC_except_table2871
+ GCC_except_table2878
+ GCC_except_table2893
+ GCC_except_table2906
+ GCC_except_table2908
+ GCC_except_table2914
+ GCC_except_table2921
+ GCC_except_table2924
+ GCC_except_table2929
+ GCC_except_table2934
+ GCC_except_table2990
+ GCC_except_table2993
+ GCC_except_table2998
+ GCC_except_table3000
+ GCC_except_table3014
+ GCC_except_table3028
+ GCC_except_table3030
+ GCC_except_table3034
+ GCC_except_table3042
+ GCC_except_table3050
+ GCC_except_table3099
+ GCC_except_table3107
+ GCC_except_table3110
+ GCC_except_table3133
+ GCC_except_table3377
+ GCC_except_table3444
+ GCC_except_table3448
+ GCC_except_table3451
+ GCC_except_table3454
+ GCC_except_table3457
+ GCC_except_table3459
+ GCC_except_table3466
+ GCC_except_table3476
+ GCC_except_table3479
+ GCC_except_table3491
+ GCC_except_table3493
+ GCC_except_table3495
+ GCC_except_table3498
+ GCC_except_table3501
+ GCC_except_table3503
+ GCC_except_table3506
+ GCC_except_table3509
+ GCC_except_table3521
+ GCC_except_table3523
+ GCC_except_table3527
+ GCC_except_table3531
+ GCC_except_table3535
+ GCC_except_table3561
+ GCC_except_table3579
+ GCC_except_table3583
+ GCC_except_table3586
+ GCC_except_table3588
+ GCC_except_table3590
+ GCC_except_table3599
+ GCC_except_table3691
+ GCC_except_table3692
+ GCC_except_table3693
+ GCC_except_table3730
+ GCC_except_table3756
+ GCC_except_table3847
+ GCC_except_table3854
+ GCC_except_table3896
+ GCC_except_table3924
+ GCC_except_table3929
+ GCC_except_table3940
+ GCC_except_table3944
+ GCC_except_table3949
+ GCC_except_table3960
+ GCC_except_table3968
+ GCC_except_table3972
+ GCC_except_table3979
+ GCC_except_table3980
+ GCC_except_table3984
+ GCC_except_table3985
+ GCC_except_table4003
+ GCC_except_table4007
+ GCC_except_table4011
+ GCC_except_table4020
+ GCC_except_table4022
+ GCC_except_table4028
+ GCC_except_table4033
+ GCC_except_table4045
+ GCC_except_table4056
+ GCC_except_table4058
+ GCC_except_table4067
+ GCC_except_table4073
+ GCC_except_table4333
+ GCC_except_table4339
+ GCC_except_table4356
+ GCC_except_table4360
+ GCC_except_table4377
+ GCC_except_table4383
+ GCC_except_table4396
+ GCC_except_table4410
+ GCC_except_table4414
+ GCC_except_table445
+ GCC_except_table4527
+ GCC_except_table455
+ GCC_except_table469
+ GCC_except_table477
+ GCC_except_table4935
+ GCC_except_table4943
+ GCC_except_table4953
+ GCC_except_table4999
+ GCC_except_table5000
+ GCC_except_table5001
+ GCC_except_table507
+ GCC_except_table5086
+ GCC_except_table5087
+ GCC_except_table5088
+ GCC_except_table5095
+ GCC_except_table5097
+ GCC_except_table5107
+ GCC_except_table5109
+ GCC_except_table5120
+ GCC_except_table5124
+ GCC_except_table5128
+ GCC_except_table515
+ GCC_except_table529
+ GCC_except_table532
+ GCC_except_table535
+ GCC_except_table538
+ GCC_except_table5475
+ GCC_except_table5476
+ GCC_except_table5495
+ GCC_except_table550
+ GCC_except_table5508
+ GCC_except_table5516
+ GCC_except_table554
+ GCC_except_table557
+ GCC_except_table564
+ GCC_except_table570
+ GCC_except_table5781
+ GCC_except_table5785
+ GCC_except_table5819
+ GCC_except_table5823
+ GCC_except_table5825
+ GCC_except_table5827
+ GCC_except_table598
+ GCC_except_table5996
+ GCC_except_table6002
+ GCC_except_table6007
+ GCC_except_table6008
+ GCC_except_table6009
+ GCC_except_table6015
+ GCC_except_table6031
+ GCC_except_table6063
+ GCC_except_table6064
+ GCC_except_table6065
+ GCC_except_table608
+ GCC_except_table6085
+ GCC_except_table6100
+ GCC_except_table6105
+ GCC_except_table6107
+ GCC_except_table6121
+ GCC_except_table615
+ GCC_except_table6344
+ GCC_except_table6357
+ GCC_except_table6369
+ GCC_except_table6371
+ GCC_except_table6401
+ GCC_except_table642
+ GCC_except_table6423
+ GCC_except_table6427
+ GCC_except_table6431
+ GCC_except_table6436
+ GCC_except_table6440
+ GCC_except_table6444
+ GCC_except_table6448
+ GCC_except_table6452
+ GCC_except_table646
+ GCC_except_table6460
+ GCC_except_table6462
+ GCC_except_table6464
+ GCC_except_table651
+ GCC_except_table6530
+ GCC_except_table6531
+ GCC_except_table6532
+ GCC_except_table659
+ GCC_except_table6590
+ GCC_except_table6594
+ GCC_except_table6595
+ GCC_except_table6607
+ GCC_except_table6613
+ GCC_except_table6629
+ GCC_except_table6630
+ GCC_except_table6638
+ GCC_except_table6648
+ GCC_except_table6662
+ GCC_except_table6669
+ GCC_except_table6675
+ GCC_except_table6684
+ GCC_except_table6686
+ GCC_except_table6690
+ GCC_except_table6691
+ GCC_except_table6708
+ GCC_except_table6710
+ GCC_except_table6719
+ GCC_except_table672
+ GCC_except_table6734
+ GCC_except_table6735
+ GCC_except_table6740
+ GCC_except_table6744
+ GCC_except_table6748
+ GCC_except_table6754
+ GCC_except_table6758
+ GCC_except_table676
+ GCC_except_table6762
+ GCC_except_table6764
+ GCC_except_table6766
+ GCC_except_table6770
+ GCC_except_table680
+ GCC_except_table6885
+ GCC_except_table690
+ GCC_except_table691
+ GCC_except_table6922
+ GCC_except_table696
+ GCC_except_table6981
+ GCC_except_table6985
+ GCC_except_table699
+ GCC_except_table6991
+ GCC_except_table6998
+ GCC_except_table6999
+ GCC_except_table7015
+ GCC_except_table7019
+ GCC_except_table702
+ GCC_except_table7020
+ GCC_except_table7021
+ GCC_except_table707
+ GCC_except_table7071
+ GCC_except_table7076
+ GCC_except_table7103
+ GCC_except_table7104
+ GCC_except_table7109
+ GCC_except_table711
+ GCC_except_table7129
+ GCC_except_table7146
+ GCC_except_table7147
+ GCC_except_table7148
+ GCC_except_table7157
+ GCC_except_table7162
+ GCC_except_table7163
+ GCC_except_table7164
+ GCC_except_table717
+ GCC_except_table718
+ GCC_except_table7182
+ GCC_except_table7189
+ GCC_except_table7196
+ GCC_except_table7201
+ GCC_except_table7207
+ GCC_except_table7219
+ GCC_except_table7220
+ GCC_except_table7225
+ GCC_except_table723
+ GCC_except_table7234
+ GCC_except_table724
+ GCC_except_table7240
+ GCC_except_table7241
+ GCC_except_table7245
+ GCC_except_table7247
+ GCC_except_table7249
+ GCC_except_table7253
+ GCC_except_table7276
+ GCC_except_table7277
+ GCC_except_table7303
+ GCC_except_table7467
+ GCC_except_table751
+ GCC_except_table7530
+ GCC_except_table7565
+ GCC_except_table758
+ GCC_except_table765
+ GCC_except_table766
+ GCC_except_table7731
+ GCC_except_table7770
+ GCC_except_table7807
+ GCC_except_table7871
+ GCC_except_table7877
+ GCC_except_table7923
+ GCC_except_table7925
+ GCC_except_table7927
+ GCC_except_table7929
+ GCC_except_table7931
+ GCC_except_table7933
+ GCC_except_table7935
+ GCC_except_table7937
+ GCC_except_table7939
+ GCC_except_table7941
+ GCC_except_table7946
+ GCC_except_table7948
+ GCC_except_table7950
+ GCC_except_table7956
+ GCC_except_table7962
+ GCC_except_table797
+ GCC_except_table7973
+ GCC_except_table8002
+ GCC_except_table8003
+ GCC_except_table8042
+ GCC_except_table8049
+ GCC_except_table8054
+ GCC_except_table8056
+ GCC_except_table8060
+ GCC_except_table8061
+ GCC_except_table8065
+ GCC_except_table8113
+ GCC_except_table8120
+ GCC_except_table820
+ GCC_except_table8214
+ GCC_except_table8230
+ GCC_except_table8232
+ GCC_except_table8237
+ GCC_except_table8239
+ GCC_except_table8244
+ GCC_except_table8246
+ GCC_except_table8250
+ GCC_except_table8255
+ GCC_except_table839
+ GCC_except_table863
+ GCC_except_table867
+ GCC_except_table881
+ GCC_except_table886
+ GCC_except_table989
+ GCC_except_table991
+ _OBJC_IVAR_$_HAPAccessoryServerIP._wacTeardownInProgress
+ _OBJC_IVAR_$_HAPSuspendedAccessoryIP._shouldWake
+ _OBJC_IVAR_$_HAPWACAccessoryClient._joinContext
+ __CopyPairingIdentityDelegateCallback_f.17285
+ __CopyPairingIdentityDelegateCallback_f.24261
+ __PairSetupPromptForSetupCodeDelegateCallback_f.24263
+ __SavePairedPeerDelegateCallback_f.17277
+ __SavePairedPeerDelegateCallback_f.24257
+ ___108-[HAPAccessoryServerIP _performExecuteWriteValues:prepareIdentifier:timeout:expiry:queue:completionHandler:]_block_invoke.245
+ ___108-[HAPAccessoryServerIP _performExecuteWriteValues:prepareIdentifier:timeout:expiry:queue:completionHandler:]_block_invoke.246
+ ___115-[HAPAccessoryServerIP _handleWriteECONNResetError:writeRequests:responses:timeout:expiry:queue:completionHandler:]_block_invoke.227
+ ___120-[HAPAccessoryServerIP _handleReadECONNRESETError:readCharacteristics:responses:timeout:expiry:queue:completionHandler:]_block_invoke.183
+ ___41-[HAPAccessoryServerIP getAccessoryInfo:]_block_invoke.477
+ ___45-[HAPAccessoryServerIP stopPairingWithError:]_block_invoke.144
+ ___47-[HAPAccessoryServerIP identifyWithCompletion:]_block_invoke.595
+ ___48-[HAPAccessoryServerIP startPairingWithRequest:]_block_invoke.142
+ ___49-[HAPAccessoryServerIP _continuePairingAfterWAC:]_block_invoke.111
+ ___49-[HAPAccessoryServerIP _continuePairingAfterWAC:]_block_invoke.116
+ ___49-[HAPAccessoryServerIP authSession:authComplete:]_block_invoke.520
+ ___50-[HAPAccessoryServerIP networkMonitorIsReachable:]_block_invoke.472
+ ___53-[HAPAccessoryServerIP setPairVerifyCompletionBlock:]_block_invoke.376
+ ___55-[HAPAccessoryServerIP authSession:validateUUID:token:]_block_invoke.510
+ ___55-[HAPAccessoryServerIP authSession:validateUUID:token:]_block_invoke.515
+ ___57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke.504
+ ___57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke_2.508
+ ___59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke.435
+ ___59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke_2.436
+ ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.413
+ ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.418
+ ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.419
+ ___60-[HAPAccessoryServerIP _validatePairingAuthMethod:activity:]_block_invoke.488
+ ___65-[HAPAccessoryServerIP _continuePairingAfterAuthPromptWithRetry:]_block_invoke.427
+ ___65-[HAPAccessoryServerIP _httpClientDidCloseConnectionDueToServer:]_block_invoke.381
+ ___72-[HAPWACAccessoryClient joinAccessoryNetworkWithCompletion:joinContext:]_block_invoke
+ ___72-[HAPWACAccessoryClient joinAccessoryNetworkWithCompletion:joinContext:]_block_invoke.78
+ ___72-[HAPWACAccessoryClient joinAccessoryNetworkWithCompletion:joinContext:]_block_invoke.79
+ ___72-[HAPWACAccessoryClient joinAccessoryNetworkWithCompletion:joinContext:]_block_invoke_2
+ ___72-[HAPWACAccessoryClient joinAccessoryNetworkWithCompletion:joinContext:]_block_invoke_3
+ ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke.553
+ ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke.555
+ ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.554
+ ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.556
+ ___79-[HAPAccessoryServerIP _queueListPairingWithCompletionQueue:completionHandler:]_block_invoke.166
+ ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1232
+ ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1235
+ ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke_2.1236
+ ___83-[HAPAccessoryServerIP _performWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke.228
+ ___83-[HAPAccessoryServerIP _performWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke.236
+ ___83-[HAPAccessoryServerIP _performWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke_2.237
+ ___85-[HAPAccessoryServerIP _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.302
+ ___85-[HAPAccessoryServerIP _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.303
+ ___86-[HAPAccessoryServerIP _establishSecureConnectionAndFetchAttributeDatabaseWithReason:]_block_invoke.140
+ ___88-[HAPAccessoryServerIP _performTimedWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke.238
+ ___88-[HAPAccessoryServerIP _performTimedWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke.239
+ ___88-[HAPAccessoryServerIP _performTimedWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke_2.240
+ ___88-[HAPAccessoryServerIP _queueAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.165
+ ___88-[HAPAccessoryServerIP _startAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.531
+ ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.184
+ ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.186
+ ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.195
+ ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.205
+ ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke_2.206
+ ___90-[HAPAccessoryServerIP _queueEnableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.167
+ ___90-[HAPAccessoryServerIP _writeCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.225
+ ___99-[HAPAccessoryServerIP writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.224
+ ___Block_byref_object_copy_.11097
+ ___Block_byref_object_copy_.11500
+ ___Block_byref_object_copy_.12329
+ ___Block_byref_object_copy_.12526
+ ___Block_byref_object_copy_.14434
+ ___Block_byref_object_copy_.15185
+ ___Block_byref_object_copy_.15976
+ ___Block_byref_object_copy_.17189
+ ___Block_byref_object_copy_.18547
+ ___Block_byref_object_copy_.19458
+ ___Block_byref_object_copy_.19679
+ ___Block_byref_object_copy_.20684
+ ___Block_byref_object_copy_.21302
+ ___Block_byref_object_copy_.22423
+ ___Block_byref_object_copy_.23249
+ ___Block_byref_object_copy_.2343
+ ___Block_byref_object_copy_.26258
+ ___Block_byref_object_copy_.27538
+ ___Block_byref_object_copy_.27705
+ ___Block_byref_object_copy_.5478
+ ___Block_byref_object_copy_.5766
+ ___Block_byref_object_copy_.6194
+ ___Block_byref_object_copy_.6834
+ ___Block_byref_object_copy_.7018
+ ___Block_byref_object_copy_.7816
+ ___Block_byref_object_copy_.851
+ ___Block_byref_object_copy_.9416
+ ___Block_byref_object_copy_.9761
+ ___Block_byref_object_copy_.9965
+ ___Block_byref_object_dispose_.11098
+ ___Block_byref_object_dispose_.11501
+ ___Block_byref_object_dispose_.12330
+ ___Block_byref_object_dispose_.12527
+ ___Block_byref_object_dispose_.14435
+ ___Block_byref_object_dispose_.15186
+ ___Block_byref_object_dispose_.15977
+ ___Block_byref_object_dispose_.17190
+ ___Block_byref_object_dispose_.18548
+ ___Block_byref_object_dispose_.19459
+ ___Block_byref_object_dispose_.19680
+ ___Block_byref_object_dispose_.20685
+ ___Block_byref_object_dispose_.21303
+ ___Block_byref_object_dispose_.22424
+ ___Block_byref_object_dispose_.23250
+ ___Block_byref_object_dispose_.2344
+ ___Block_byref_object_dispose_.26259
+ ___Block_byref_object_dispose_.27539
+ ___Block_byref_object_dispose_.27706
+ ___Block_byref_object_dispose_.5479
+ ___Block_byref_object_dispose_.5767
+ ___Block_byref_object_dispose_.6195
+ ___Block_byref_object_dispose_.6835
+ ___Block_byref_object_dispose_.7019
+ ___Block_byref_object_dispose_.7817
+ ___Block_byref_object_dispose_.852
+ ___Block_byref_object_dispose_.9417
+ ___Block_byref_object_dispose_.9762
+ ___Block_byref_object_dispose_.9966
+ ___block_literal_global.10120
+ ___block_literal_global.10766
+ ___block_literal_global.11554
+ ___block_literal_global.12325
+ ___block_literal_global.1252
+ ___block_literal_global.12695
+ ___block_literal_global.1289
+ ___block_literal_global.14722
+ ___block_literal_global.17306
+ ___block_literal_global.174
+ ___block_literal_global.17733
+ ___block_literal_global.19111
+ ___block_literal_global.19468
+ ___block_literal_global.20842
+ ___block_literal_global.22166
+ ___block_literal_global.22445
+ ___block_literal_global.2249
+ ___block_literal_global.22901
+ ___block_literal_global.23852
+ ___block_literal_global.25291
+ ___block_literal_global.25631
+ ___block_literal_global.27311
+ ___block_literal_global.27934
+ ___block_literal_global.5561
+ ___block_literal_global.5762
+ ___block_literal_global.6315
+ ___block_literal_global.6845
+ ___block_literal_global.6992
+ ___block_literal_global.8128
+ ___block_literal_global.9040
+ ___block_literal_global.9517
+ ___block_literal_global.956
+ _hkConfig.23836
+ _logCategory._hmf_once_t2
+ _logCategory._hmf_once_t435
+ _logCategory._hmf_once_v3
+ _logCategory._hmf_once_v436
+ _objc_msgSend$joinAccessoryNetworkWithCompletion:joinContext:
+ _objc_msgSend$joinContext
+ _objc_msgSend$setJoinContext:
+ _objc_msgSend$setWacTeardownInProgress:
+ _objc_msgSend$shouldWake
+ _objc_msgSend$wacTeardownInProgress
+ _sharedInstance.onceToken.17732
- -[HAPSuspendedAccessoryIP initWithName:identifier:wakeTuples:queue:]
- -[HAPWACAccessoryClient joinAccessoryNetworkWithCompletion:]
- GCC_except_table1098
- GCC_except_table1102
- GCC_except_table1115
- GCC_except_table1120
- GCC_except_table1129
- GCC_except_table1131
- GCC_except_table1133
- GCC_except_table1135
- GCC_except_table1261
- GCC_except_table1265
- GCC_except_table1267
- GCC_except_table1480
- GCC_except_table1688
- GCC_except_table1690
- GCC_except_table1695
- GCC_except_table1701
- GCC_except_table1703
- GCC_except_table1709
- GCC_except_table1711
- GCC_except_table1715
- GCC_except_table1719
- GCC_except_table1721
- GCC_except_table1726
- GCC_except_table1730
- GCC_except_table1740
- GCC_except_table1748
- GCC_except_table1755
- GCC_except_table1759
- GCC_except_table1763
- GCC_except_table1767
- GCC_except_table1803
- GCC_except_table1923
- GCC_except_table1928
- GCC_except_table1930
- GCC_except_table1932
- GCC_except_table1942
- GCC_except_table1944
- GCC_except_table1948
- GCC_except_table1951
- GCC_except_table1953
- GCC_except_table1956
- GCC_except_table1973
- GCC_except_table1980
- GCC_except_table1982
- GCC_except_table1984
- GCC_except_table1988
- GCC_except_table1991
- GCC_except_table1995
- GCC_except_table1997
- GCC_except_table2000
- GCC_except_table2003
- GCC_except_table2005
- GCC_except_table2007
- GCC_except_table2011
- GCC_except_table2015
- GCC_except_table2023
- GCC_except_table2034
- GCC_except_table2078
- GCC_except_table2084
- GCC_except_table2251
- GCC_except_table2258
- GCC_except_table2264
- GCC_except_table2268
- GCC_except_table2272
- GCC_except_table2275
- GCC_except_table2278
- GCC_except_table2280
- GCC_except_table2283
- GCC_except_table2289
- GCC_except_table2291
- GCC_except_table2295
- GCC_except_table2298
- GCC_except_table2394
- GCC_except_table2402
- GCC_except_table2422
- GCC_except_table2436
- GCC_except_table2516
- GCC_except_table2528
- GCC_except_table2554
- GCC_except_table2562
- GCC_except_table2573
- GCC_except_table2587
- GCC_except_table2590
- GCC_except_table2595
- GCC_except_table2603
- GCC_except_table2609
- GCC_except_table2611
- GCC_except_table2786
- GCC_except_table2836
- GCC_except_table2852
- GCC_except_table2855
- GCC_except_table2869
- GCC_except_table2877
- GCC_except_table2892
- GCC_except_table2904
- GCC_except_table2907
- GCC_except_table2913
- GCC_except_table2920
- GCC_except_table2923
- GCC_except_table2928
- GCC_except_table2933
- GCC_except_table2989
- GCC_except_table2992
- GCC_except_table2997
- GCC_except_table2999
- GCC_except_table3013
- GCC_except_table3027
- GCC_except_table3029
- GCC_except_table3033
- GCC_except_table3041
- GCC_except_table3049
- GCC_except_table3098
- GCC_except_table3106
- GCC_except_table3108
- GCC_except_table3132
- GCC_except_table3376
- GCC_except_table3442
- GCC_except_table3447
- GCC_except_table3450
- GCC_except_table3452
- GCC_except_table3455
- GCC_except_table3458
- GCC_except_table3465
- GCC_except_table3475
- GCC_except_table3478
- GCC_except_table3489
- GCC_except_table3492
- GCC_except_table3494
- GCC_except_table3497
- GCC_except_table3500
- GCC_except_table3502
- GCC_except_table3505
- GCC_except_table3508
- GCC_except_table3520
- GCC_except_table3522
- GCC_except_table3526
- GCC_except_table3530
- GCC_except_table3534
- GCC_except_table3560
- GCC_except_table3578
- GCC_except_table3582
- GCC_except_table3585
- GCC_except_table3587
- GCC_except_table3589
- GCC_except_table3596
- GCC_except_table3677
- GCC_except_table3678
- GCC_except_table3679
- GCC_except_table3727
- GCC_except_table3753
- GCC_except_table3844
- GCC_except_table3851
- GCC_except_table3893
- GCC_except_table3897
- GCC_except_table3926
- GCC_except_table3937
- GCC_except_table3941
- GCC_except_table3943
- GCC_except_table3957
- GCC_except_table3965
- GCC_except_table3969
- GCC_except_table3976
- GCC_except_table3977
- GCC_except_table3981
- GCC_except_table3982
- GCC_except_table4000
- GCC_except_table4002
- GCC_except_table4004
- GCC_except_table4014
- GCC_except_table4019
- GCC_except_table4025
- GCC_except_table4027
- GCC_except_table4042
- GCC_except_table4053
- GCC_except_table4055
- GCC_except_table4064
- GCC_except_table4070
- GCC_except_table4330
- GCC_except_table4336
- GCC_except_table4353
- GCC_except_table4357
- GCC_except_table4374
- GCC_except_table4380
- GCC_except_table4393
- GCC_except_table4407
- GCC_except_table4411
- GCC_except_table443
- GCC_except_table4524
- GCC_except_table453
- GCC_except_table467
- GCC_except_table475
- GCC_except_table4932
- GCC_except_table4940
- GCC_except_table4950
- GCC_except_table4992
- GCC_except_table4996
- GCC_except_table4997
- GCC_except_table505
- GCC_except_table5080
- GCC_except_table5081
- GCC_except_table5082
- GCC_except_table5091
- GCC_except_table5092
- GCC_except_table5101
- GCC_except_table5106
- GCC_except_table5111
- GCC_except_table5121
- GCC_except_table5125
- GCC_except_table513
- GCC_except_table527
- GCC_except_table528
- GCC_except_table533
- GCC_except_table536
- GCC_except_table5472
- GCC_except_table5473
- GCC_except_table548
- GCC_except_table5492
- GCC_except_table5502
- GCC_except_table5510
- GCC_except_table552
- GCC_except_table555
- GCC_except_table562
- GCC_except_table568
- GCC_except_table5778
- GCC_except_table5782
- GCC_except_table5816
- GCC_except_table5820
- GCC_except_table5822
- GCC_except_table5824
- GCC_except_table596
- GCC_except_table5993
- GCC_except_table5999
- GCC_except_table6003
- GCC_except_table6004
- GCC_except_table6005
- GCC_except_table6012
- GCC_except_table6028
- GCC_except_table606
- GCC_except_table6060
- GCC_except_table6061
- GCC_except_table6062
- GCC_except_table6082
- GCC_except_table6094
- GCC_except_table6102
- GCC_except_table6104
- GCC_except_table6118
- GCC_except_table613
- GCC_except_table6341
- GCC_except_table6354
- GCC_except_table6359
- GCC_except_table6363
- GCC_except_table6398
- GCC_except_table640
- GCC_except_table6420
- GCC_except_table6424
- GCC_except_table6428
- GCC_except_table6433
- GCC_except_table6437
- GCC_except_table644
- GCC_except_table6441
- GCC_except_table6445
- GCC_except_table6449
- GCC_except_table6457
- GCC_except_table6459
- GCC_except_table6461
- GCC_except_table647
- GCC_except_table6523
- GCC_except_table6524
- GCC_except_table6525
- GCC_except_table655
- GCC_except_table6587
- GCC_except_table6591
- GCC_except_table6592
- GCC_except_table6604
- GCC_except_table6610
- GCC_except_table6623
- GCC_except_table6627
- GCC_except_table6632
- GCC_except_table6642
- GCC_except_table6659
- GCC_except_table6666
- GCC_except_table6672
- GCC_except_table6681
- GCC_except_table6683
- GCC_except_table6687
- GCC_except_table6688
- GCC_except_table670
- GCC_except_table6705
- GCC_except_table6707
- GCC_except_table6716
- GCC_except_table6731
- GCC_except_table6732
- GCC_except_table6737
- GCC_except_table674
- GCC_except_table6741
- GCC_except_table6742
- GCC_except_table6751
- GCC_except_table6755
- GCC_except_table6759
- GCC_except_table6761
- GCC_except_table6763
- GCC_except_table6767
- GCC_except_table678
- GCC_except_table688
- GCC_except_table6882
- GCC_except_table689
- GCC_except_table6919
- GCC_except_table694
- GCC_except_table697
- GCC_except_table6975
- GCC_except_table6982
- GCC_except_table6988
- GCC_except_table6995
- GCC_except_table6996
- GCC_except_table700
- GCC_except_table7012
- GCC_except_table7016
- GCC_except_table7017
- GCC_except_table7018
- GCC_except_table705
- GCC_except_table7067
- GCC_except_table7068
- GCC_except_table709
- GCC_except_table7100
- GCC_except_table7101
- GCC_except_table7106
- GCC_except_table7126
- GCC_except_table7143
- GCC_except_table7144
- GCC_except_table7145
- GCC_except_table715
- GCC_except_table7154
- GCC_except_table7159
- GCC_except_table716
- GCC_except_table7160
- GCC_except_table7161
- GCC_except_table7176
- GCC_except_table7186
- GCC_except_table7193
- GCC_except_table7198
- GCC_except_table7204
- GCC_except_table721
- GCC_except_table7216
- GCC_except_table7217
- GCC_except_table722
- GCC_except_table7222
- GCC_except_table7231
- GCC_except_table7237
- GCC_except_table7238
- GCC_except_table7242
- GCC_except_table7244
- GCC_except_table7246
- GCC_except_table7250
- GCC_except_table7271
- GCC_except_table7273
- GCC_except_table7300
- GCC_except_table7464
- GCC_except_table749
- GCC_except_table7527
- GCC_except_table7559
- GCC_except_table756
- GCC_except_table763
- GCC_except_table764
- GCC_except_table7728
- GCC_except_table7767
- GCC_except_table7804
- GCC_except_table7868
- GCC_except_table7874
- GCC_except_table7920
- GCC_except_table7922
- GCC_except_table7924
- GCC_except_table7926
- GCC_except_table7928
- GCC_except_table7930
- GCC_except_table7932
- GCC_except_table7934
- GCC_except_table7936
- GCC_except_table7938
- GCC_except_table7940
- GCC_except_table7945
- GCC_except_table7947
- GCC_except_table7953
- GCC_except_table7959
- GCC_except_table7964
- GCC_except_table798
- GCC_except_table7996
- GCC_except_table8000
- GCC_except_table8039
- GCC_except_table8040
- GCC_except_table8041
- GCC_except_table8048
- GCC_except_table8057
- GCC_except_table8058
- GCC_except_table8062
- GCC_except_table8110
- GCC_except_table8117
- GCC_except_table821
- GCC_except_table8211
- GCC_except_table8227
- GCC_except_table8229
- GCC_except_table8231
- GCC_except_table8236
- GCC_except_table8238
- GCC_except_table8240
- GCC_except_table8247
- GCC_except_table8252
- GCC_except_table840
- GCC_except_table864
- GCC_except_table868
- GCC_except_table882
- GCC_except_table887
- GCC_except_table990
- GCC_except_table992
- __CopyPairingIdentityDelegateCallback_f.17290
- __CopyPairingIdentityDelegateCallback_f.24253
- __PairSetupPromptForSetupCodeDelegateCallback_f.24255
- __SavePairedPeerDelegateCallback_f.17282
- __SavePairedPeerDelegateCallback_f.24249
- ___108-[HAPAccessoryServerIP _performExecuteWriteValues:prepareIdentifier:timeout:expiry:queue:completionHandler:]_block_invoke.248
- ___108-[HAPAccessoryServerIP _performExecuteWriteValues:prepareIdentifier:timeout:expiry:queue:completionHandler:]_block_invoke.249
- ___115-[HAPAccessoryServerIP _handleWriteECONNResetError:writeRequests:responses:timeout:expiry:queue:completionHandler:]_block_invoke.230
- ___120-[HAPAccessoryServerIP _handleReadECONNRESETError:readCharacteristics:responses:timeout:expiry:queue:completionHandler:]_block_invoke.186
- ___41-[HAPAccessoryServerIP getAccessoryInfo:]_block_invoke.480
- ___45-[HAPAccessoryServerIP stopPairingWithError:]_block_invoke.147
- ___47-[HAPAccessoryServerIP identifyWithCompletion:]_block_invoke.598
- ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.111
- ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.113
- ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke_2.112
- ___48-[HAPAccessoryServerIP startPairingWithRequest:]_block_invoke.145
- ___49-[HAPAccessoryServerIP _continuePairingAfterWAC:]_block_invoke.114
- ___49-[HAPAccessoryServerIP _continuePairingAfterWAC:]_block_invoke.119
- ___49-[HAPAccessoryServerIP authSession:authComplete:]_block_invoke.523
- ___50-[HAPAccessoryServerIP networkMonitorIsReachable:]_block_invoke.475
- ___53-[HAPAccessoryServerIP setPairVerifyCompletionBlock:]_block_invoke.379
- ___55-[HAPAccessoryServerIP authSession:validateUUID:token:]_block_invoke.513
- ___55-[HAPAccessoryServerIP authSession:validateUUID:token:]_block_invoke.518
- ___57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke.507
- ___57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke_2.511
- ___59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke.438
- ___59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke_2.439
- ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.416
- ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.421
- ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.422
- ___60-[HAPAccessoryServerIP _validatePairingAuthMethod:activity:]_block_invoke.491
- ___60-[HAPWACAccessoryClient joinAccessoryNetworkWithCompletion:]_block_invoke
- ___60-[HAPWACAccessoryClient joinAccessoryNetworkWithCompletion:]_block_invoke.78
- ___60-[HAPWACAccessoryClient joinAccessoryNetworkWithCompletion:]_block_invoke.79
- ___60-[HAPWACAccessoryClient joinAccessoryNetworkWithCompletion:]_block_invoke_2
- ___60-[HAPWACAccessoryClient joinAccessoryNetworkWithCompletion:]_block_invoke_3
- ___65-[HAPAccessoryServerIP _continuePairingAfterAuthPromptWithRetry:]_block_invoke.430
- ___65-[HAPAccessoryServerIP _httpClientDidCloseConnectionDueToServer:]_block_invoke.384
- ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke.556
- ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke.558
- ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.557
- ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.559
- ___79-[HAPAccessoryServerIP _queueListPairingWithCompletionQueue:completionHandler:]_block_invoke.169
- ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1230
- ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1231
- ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke_2.1232
- ___83-[HAPAccessoryServerIP _performWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke.231
- ___83-[HAPAccessoryServerIP _performWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke.239
- ___83-[HAPAccessoryServerIP _performWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke_2.240
- ___85-[HAPAccessoryServerIP _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.305
- ___85-[HAPAccessoryServerIP _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.306
- ___86-[HAPAccessoryServerIP _establishSecureConnectionAndFetchAttributeDatabaseWithReason:]_block_invoke.143
- ___88-[HAPAccessoryServerIP _performTimedWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke.241
- ___88-[HAPAccessoryServerIP _performTimedWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke.242
- ___88-[HAPAccessoryServerIP _performTimedWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke_2.243
- ___88-[HAPAccessoryServerIP _queueAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.168
- ___88-[HAPAccessoryServerIP _startAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.534
- ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.187
- ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.189
- ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.198
- ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.208
- ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke_2.209
- ___90-[HAPAccessoryServerIP _queueEnableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.170
- ___90-[HAPAccessoryServerIP _writeCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.228
- ___99-[HAPAccessoryServerIP writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.227
- ___Block_byref_object_copy_.11107
- ___Block_byref_object_copy_.11506
- ___Block_byref_object_copy_.12338
- ___Block_byref_object_copy_.12535
- ___Block_byref_object_copy_.14447
- ___Block_byref_object_copy_.15199
- ___Block_byref_object_copy_.15989
- ___Block_byref_object_copy_.17194
- ___Block_byref_object_copy_.18550
- ___Block_byref_object_copy_.19448
- ___Block_byref_object_copy_.19668
- ___Block_byref_object_copy_.20672
- ___Block_byref_object_copy_.21287
- ___Block_byref_object_copy_.22412
- ___Block_byref_object_copy_.23237
- ___Block_byref_object_copy_.2342
- ___Block_byref_object_copy_.26249
- ___Block_byref_object_copy_.27529
- ___Block_byref_object_copy_.27696
- ___Block_byref_object_copy_.5491
- ___Block_byref_object_copy_.5785
- ___Block_byref_object_copy_.6213
- ___Block_byref_object_copy_.6854
- ___Block_byref_object_copy_.7039
- ___Block_byref_object_copy_.7840
- ___Block_byref_object_copy_.854
- ___Block_byref_object_copy_.9438
- ___Block_byref_object_copy_.9781
- ___Block_byref_object_copy_.9985
- ___Block_byref_object_dispose_.11108
- ___Block_byref_object_dispose_.11507
- ___Block_byref_object_dispose_.12339
- ___Block_byref_object_dispose_.12536
- ___Block_byref_object_dispose_.14448
- ___Block_byref_object_dispose_.15200
- ___Block_byref_object_dispose_.15990
- ___Block_byref_object_dispose_.17195
- ___Block_byref_object_dispose_.18551
- ___Block_byref_object_dispose_.19449
- ___Block_byref_object_dispose_.19669
- ___Block_byref_object_dispose_.20673
- ___Block_byref_object_dispose_.21288
- ___Block_byref_object_dispose_.22413
- ___Block_byref_object_dispose_.23238
- ___Block_byref_object_dispose_.2343
- ___Block_byref_object_dispose_.26250
- ___Block_byref_object_dispose_.27530
- ___Block_byref_object_dispose_.27697
- ___Block_byref_object_dispose_.5492
- ___Block_byref_object_dispose_.5786
- ___Block_byref_object_dispose_.6214
- ___Block_byref_object_dispose_.6855
- ___Block_byref_object_dispose_.7040
- ___Block_byref_object_dispose_.7841
- ___Block_byref_object_dispose_.855
- ___Block_byref_object_dispose_.9439
- ___Block_byref_object_dispose_.9782
- ___Block_byref_object_dispose_.9986
- ___block_literal_global.10130
- ___block_literal_global.10776
- ___block_literal_global.11562
- ___block_literal_global.12334
- ___block_literal_global.1250
- ___block_literal_global.12706
- ___block_literal_global.1287
- ___block_literal_global.14736
- ___block_literal_global.17311
- ___block_literal_global.177
- ___block_literal_global.17738
- ___block_literal_global.19101
- ___block_literal_global.19458
- ___block_literal_global.20826
- ___block_literal_global.22155
- ___block_literal_global.22434
- ___block_literal_global.2248
- ___block_literal_global.22890
- ___block_literal_global.23842
- ___block_literal_global.25284
- ___block_literal_global.25623
- ___block_literal_global.27302
- ___block_literal_global.27925
- ___block_literal_global.5579
- ___block_literal_global.5781
- ___block_literal_global.6334
- ___block_literal_global.6865
- ___block_literal_global.7013
- ___block_literal_global.8157
- ___block_literal_global.905
- ___block_literal_global.9067
- ___block_literal_global.9537
- _hkConfig.23826
- _logCategory._hmf_once_t1
- _logCategory._hmf_once_t436
- _logCategory._hmf_once_v2
- _logCategory._hmf_once_v437
- _objc_msgSend$joinAccessoryNetworkWithCompletion:
- _sharedInstance.onceToken.17737
CStrings:
+ "\""
+ "%{public}@Failed to join network, reporting error code: %ld"
+ "%{public}@Skipping wake for suspended accessory: '%@' (shouldWake is NO)"
+ "%{public}@Unhandled state: %tu, reporting auth failure"
+ "%{public}@tearDownWAC - already in progress, skipping"
+ "@32@0:8@?16Q24"
+ "@52@0:8@16@24@32@40B48"
+ "TB,N,V_shouldWake"
+ "TB,N,V_wacTeardownInProgress"
+ "TQ,N,V_joinContext"
+ "_joinContext"
+ "_shouldWake"
+ "_wacTeardownInProgress"
+ "accessoryUUID"
+ "initWithName:identifier:wakeTuples:queue:shouldWake:"
+ "joinAccessoryNetworkWithCompletion:joinContext:"
+ "joinContext"
+ "setJoinContext:"
+ "setShouldWake:"
+ "setWacTeardownInProgress:"
+ "shouldWake"
+ "wacTeardownInProgress"
- "%{public}@Failed to join network, reporting connection failure"
- "%{public}@Retrying to join accessory network due to error: %{public}@"
- "%{public}@Unhandled state: %tu"
- "initWithName:identifier:wakeTuples:queue:"
- "joinAccessoryNetworkWithCompletion:"

```
