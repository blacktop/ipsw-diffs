## CoreHAP

> `/System/Library/PrivateFrameworks/CoreHAP.framework/CoreHAP`

```diff

-1054.1.7.1.4
-  __TEXT.__text: 0x195ba4
+1076.2.8.1.1
+  __TEXT.__text: 0x196d5c
   __TEXT.__auth_stubs: 0x1550
-  __TEXT.__objc_methlist: 0x11444
+  __TEXT.__objc_methlist: 0x11534
   __TEXT.__const: 0x5e0
-  __TEXT.__gcc_except_tab: 0x45e4
-  __TEXT.__cstring: 0xfbf0
-  __TEXT.__oslogstring: 0x1ed7c
+  __TEXT.__gcc_except_tab: 0x4784
+  __TEXT.__cstring: 0xfcf5
+  __TEXT.__oslogstring: 0x1f0ac
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__unwind_info: 0x5bb8
-  __TEXT.__objc_classname: 0x2d7c
-  __TEXT.__objc_methname: 0x25470
-  __TEXT.__objc_methtype: 0x8d49
-  __TEXT.__objc_stubs: 0x17bc0
+  __TEXT.__unwind_info: 0x5bf0
+  __TEXT.__objc_classname: 0x2dce
+  __TEXT.__objc_methname: 0x25610
+  __TEXT.__objc_methtype: 0x8d75
+  __TEXT.__objc_stubs: 0x17c60
   __DATA_CONST.__got: 0x2d0
-  __DATA_CONST.__const: 0x5300
-  __DATA_CONST.__objc_classlist: 0x940
+  __DATA_CONST.__const: 0x5318
+  __DATA_CONST.__objc_classlist: 0x950
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x330
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1ba50
-  __DATA_CONST.__objc_selrefs: 0x6a48
+  __DATA_CONST.__objc_const: 0x1bd00
+  __DATA_CONST.__objc_selrefs: 0x6a90
   __DATA_CONST.__objc_arraydata: 0x208
-  __AUTH_CONST.__cfstring: 0xd140
+  __AUTH_CONST.__cfstring: 0xd200
   __AUTH_CONST.__const: 0x7c0
-  __AUTH_CONST.__objc_const: 0x8f08
+  __AUTH_CONST.__objc_const: 0x8f98
   __AUTH_CONST.__objc_intobj: 0x660
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__auth_got: 0xab8
-  __AUTH.__objc_data: 0x50a0
+  __AUTH.__objc_data: 0x5140
   __DATA.__objc_protorefs: 0xc0
-  __DATA.__objc_classrefs: 0xaa8
-  __DATA.__objc_superrefs: 0x7c8
-  __DATA.__objc_ivar: 0x1458
+  __DATA.__objc_classrefs: 0xab8
+  __DATA.__objc_superrefs: 0x7d8
+  __DATA.__objc_ivar: 0x1474
   __DATA.__data: 0x266a
   __DATA.__bss: 0x4b1
   __DATA_DIRTY.__objc_data: 0xbe0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5B16C854-95F1-342D-8390-B1E91162B610
-  Functions: 7356
-  Symbols:   23813
-  CStrings:  12505
+  UUID: 89B14CE8-649E-3A24-A887-879180B2D9C8
+  Functions: 7375
+  Symbols:   23878
+  CStrings:  12551
 
Symbols:
+ -[HAPAccessoryServerIP bonjourRemoveEvent]
+ -[HAPAccessoryServerIP ipConnectionStatistics]
+ -[HAPAccessoryServerIP setIpConnectionStatistics:]
+ -[HAPAccessoryServerIPConnectionStatistics .cxx_destruct]
+ -[HAPAccessoryServerIPConnectionStatistics accessoryServerIPEvent:]
+ -[HAPAccessoryServerIPConnectionStatistics accessory]
+ -[HAPAccessoryServerIPConnectionStatistics generateBonjourRemoveMetric]
+ -[HAPAccessoryServerIPConnectionStatistics initWithAccessory:]
+ -[HAPAccessoryServerIPConnectionStatistics metricTriggered]
+ -[HAPAccessoryServerIPConnectionStatistics sessionRestoreActive]
+ -[HAPAccessoryServerIPConnectionStatistics state]
+ -[HAPMetricsBonjourIncorrrectStateLogEvent .cxx_destruct]
+ -[HAPMetricsBonjourIncorrrectStateLogEvent coreAnalyticsEventDictionary]
+ -[HAPMetricsBonjourIncorrrectStateLogEvent coreAnalyticsEventName]
+ -[HAPMetricsBonjourIncorrrectStateLogEvent coreAnalyticsEventOptions]
+ -[HAPMetricsBonjourIncorrrectStateLogEvent deviceID]
+ -[HAPMetricsBonjourIncorrrectStateLogEvent initWithDeviceID:]
+ -[HAPMetricsBonjourIncorrrectStateLogEvent setDeviceID:]
+ GCC_except_table1006
+ GCC_except_table1010
+ GCC_except_table1023
+ GCC_except_table1028
+ GCC_except_table1037
+ GCC_except_table1039
+ GCC_except_table1041
+ GCC_except_table1043
+ GCC_except_table1169
+ GCC_except_table1173
+ GCC_except_table1175
+ GCC_except_table1559
+ GCC_except_table1567
+ GCC_except_table1569
+ GCC_except_table1575
+ GCC_except_table1577
+ GCC_except_table1581
+ GCC_except_table1585
+ GCC_except_table1587
+ GCC_except_table1592
+ GCC_except_table1596
+ GCC_except_table1606
+ GCC_except_table1614
+ GCC_except_table1621
+ GCC_except_table1625
+ GCC_except_table1629
+ GCC_except_table1633
+ GCC_except_table1635
+ GCC_except_table1782
+ GCC_except_table1784
+ GCC_except_table1786
+ GCC_except_table1795
+ GCC_except_table1797
+ GCC_except_table1804
+ GCC_except_table1809
+ GCC_except_table1829
+ GCC_except_table1831
+ GCC_except_table1833
+ GCC_except_table1840
+ GCC_except_table1844
+ GCC_except_table1852
+ GCC_except_table1854
+ GCC_except_table1856
+ GCC_except_table1860
+ GCC_except_table1864
+ GCC_except_table1872
+ GCC_except_table1883
+ GCC_except_table1920
+ GCC_except_table1926
+ GCC_except_table2097
+ GCC_except_table2126
+ GCC_except_table2237
+ GCC_except_table2248
+ GCC_except_table2249
+ GCC_except_table2250
+ GCC_except_table2265
+ GCC_except_table2279
+ GCC_except_table2354
+ GCC_except_table2366
+ GCC_except_table2392
+ GCC_except_table2400
+ GCC_except_table2411
+ GCC_except_table2428
+ GCC_except_table2433
+ GCC_except_table2441
+ GCC_except_table2447
+ GCC_except_table2449
+ GCC_except_table2630
+ GCC_except_table2699
+ GCC_except_table2721
+ GCC_except_table2736
+ GCC_except_table2748
+ GCC_except_table2749
+ GCC_except_table2764
+ GCC_except_table2767
+ GCC_except_table2772
+ GCC_except_table2831
+ GCC_except_table2836
+ GCC_except_table2838
+ GCC_except_table2852
+ GCC_except_table2866
+ GCC_except_table2868
+ GCC_except_table2872
+ GCC_except_table2880
+ GCC_except_table2888
+ GCC_except_table2945
+ GCC_except_table2947
+ GCC_except_table2948
+ GCC_except_table2971
+ GCC_except_table3199
+ GCC_except_table3263
+ GCC_except_table3266
+ GCC_except_table3268
+ GCC_except_table3269
+ GCC_except_table3272
+ GCC_except_table3274
+ GCC_except_table3291
+ GCC_except_table3294
+ GCC_except_table3305
+ GCC_except_table3310
+ GCC_except_table3313
+ GCC_except_table3316
+ GCC_except_table3318
+ GCC_except_table3321
+ GCC_except_table3324
+ GCC_except_table3338
+ GCC_except_table3342
+ GCC_except_table3346
+ GCC_except_table3350
+ GCC_except_table3376
+ GCC_except_table3394
+ GCC_except_table3398
+ GCC_except_table3401
+ GCC_except_table3403
+ GCC_except_table3405
+ GCC_except_table3520
+ GCC_except_table3545
+ GCC_except_table3632
+ GCC_except_table3639
+ GCC_except_table3661
+ GCC_except_table3664
+ GCC_except_table3667
+ GCC_except_table3670
+ GCC_except_table3673
+ GCC_except_table3676
+ GCC_except_table3679
+ GCC_except_table3682
+ GCC_except_table3685
+ GCC_except_table3690
+ GCC_except_table3701
+ GCC_except_table3704
+ GCC_except_table3715
+ GCC_except_table3723
+ GCC_except_table3727
+ GCC_except_table3734
+ GCC_except_table3735
+ GCC_except_table3739
+ GCC_except_table3740
+ GCC_except_table3758
+ GCC_except_table3760
+ GCC_except_table3763
+ GCC_except_table3766
+ GCC_except_table3772
+ GCC_except_table3777
+ GCC_except_table3783
+ GCC_except_table3785
+ GCC_except_table3788
+ GCC_except_table3800
+ GCC_except_table3811
+ GCC_except_table3813
+ GCC_except_table3822
+ GCC_except_table3828
+ GCC_except_table384
+ GCC_except_table400
+ GCC_except_table408
+ GCC_except_table4088
+ GCC_except_table4094
+ GCC_except_table4111
+ GCC_except_table4115
+ GCC_except_table4132
+ GCC_except_table4138
+ GCC_except_table4151
+ GCC_except_table4165
+ GCC_except_table4169
+ GCC_except_table4272
+ GCC_except_table4352
+ GCC_except_table4370
+ GCC_except_table438
+ GCC_except_table4404
+ GCC_except_table4407
+ GCC_except_table4408
+ GCC_except_table4409
+ GCC_except_table4410
+ GCC_except_table445
+ GCC_except_table4501
+ GCC_except_table4504
+ GCC_except_table4506
+ GCC_except_table4513
+ GCC_except_table4527
+ GCC_except_table4535
+ GCC_except_table4538
+ GCC_except_table4542
+ GCC_except_table4546
+ GCC_except_table4575
+ GCC_except_table4576
+ GCC_except_table459
+ GCC_except_table4605
+ GCC_except_table4608
+ GCC_except_table4613
+ GCC_except_table4616
+ GCC_except_table462
+ GCC_except_table465
+ GCC_except_table468
+ GCC_except_table480
+ GCC_except_table486
+ GCC_except_table4877
+ GCC_except_table4881
+ GCC_except_table4915
+ GCC_except_table4919
+ GCC_except_table4921
+ GCC_except_table4923
+ GCC_except_table493
+ GCC_except_table499
+ GCC_except_table5082
+ GCC_except_table5086
+ GCC_except_table5087
+ GCC_except_table5088
+ GCC_except_table5089
+ GCC_except_table5095
+ GCC_except_table5129
+ GCC_except_table5130
+ GCC_except_table5131
+ GCC_except_table5149
+ GCC_except_table5164
+ GCC_except_table5169
+ GCC_except_table517
+ GCC_except_table5171
+ GCC_except_table5185
+ GCC_except_table527
+ GCC_except_table534
+ GCC_except_table5384
+ GCC_except_table5396
+ GCC_except_table5401
+ GCC_except_table5404
+ GCC_except_table5405
+ GCC_except_table5407
+ GCC_except_table5408
+ GCC_except_table5410
+ GCC_except_table5440
+ GCC_except_table5462
+ GCC_except_table5466
+ GCC_except_table5470
+ GCC_except_table5475
+ GCC_except_table5479
+ GCC_except_table5483
+ GCC_except_table5487
+ GCC_except_table5499
+ GCC_except_table5501
+ GCC_except_table5503
+ GCC_except_table5541
+ GCC_except_table5568
+ GCC_except_table5569
+ GCC_except_table5570
+ GCC_except_table5571
+ GCC_except_table561
+ GCC_except_table5629
+ GCC_except_table5630
+ GCC_except_table5644
+ GCC_except_table5650
+ GCC_except_table5663
+ GCC_except_table5666
+ GCC_except_table5672
+ GCC_except_table5675
+ GCC_except_table5682
+ GCC_except_table5685
+ GCC_except_table569
+ GCC_except_table5699
+ GCC_except_table5706
+ GCC_except_table5712
+ GCC_except_table5721
+ GCC_except_table5723
+ GCC_except_table5727
+ GCC_except_table5728
+ GCC_except_table5742
+ GCC_except_table5744
+ GCC_except_table5752
+ GCC_except_table5767
+ GCC_except_table5768
+ GCC_except_table577
+ GCC_except_table5778
+ GCC_except_table5787
+ GCC_except_table5791
+ GCC_except_table5793
+ GCC_except_table5795
+ GCC_except_table5799
+ GCC_except_table589
+ GCC_except_table593
+ GCC_except_table5944
+ GCC_except_table597
+ GCC_except_table5998
+ GCC_except_table6005
+ GCC_except_table6011
+ GCC_except_table6018
+ GCC_except_table6019
+ GCC_except_table6035
+ GCC_except_table6039
+ GCC_except_table6040
+ GCC_except_table6041
+ GCC_except_table606
+ GCC_except_table607
+ GCC_except_table6089
+ GCC_except_table6090
+ GCC_except_table6092
+ GCC_except_table6095
+ GCC_except_table612
+ GCC_except_table6125
+ GCC_except_table6126
+ GCC_except_table615
+ GCC_except_table6166
+ GCC_except_table6167
+ GCC_except_table6168
+ GCC_except_table6176
+ GCC_except_table618
+ GCC_except_table6181
+ GCC_except_table6183
+ GCC_except_table6197
+ GCC_except_table6200
+ GCC_except_table6224
+ GCC_except_table6225
+ GCC_except_table623
+ GCC_except_table6230
+ GCC_except_table6239
+ GCC_except_table6245
+ GCC_except_table6258
+ GCC_except_table6262
+ GCC_except_table6264
+ GCC_except_table6268
+ GCC_except_table627
+ GCC_except_table6289
+ GCC_except_table6291
+ GCC_except_table6292
+ GCC_except_table6318
+ GCC_except_table633
+ GCC_except_table634
+ GCC_except_table639
+ GCC_except_table640
+ GCC_except_table6482
+ GCC_except_table6545
+ GCC_except_table6577
+ GCC_except_table6580
+ GCC_except_table666
+ GCC_except_table6744
+ GCC_except_table677
+ GCC_except_table678
+ GCC_except_table6807
+ GCC_except_table6870
+ GCC_except_table6876
+ GCC_except_table6925
+ GCC_except_table6927
+ GCC_except_table6929
+ GCC_except_table6931
+ GCC_except_table6935
+ GCC_except_table6937
+ GCC_except_table6939
+ GCC_except_table6941
+ GCC_except_table6944
+ GCC_except_table6946
+ GCC_except_table6948
+ GCC_except_table6951
+ GCC_except_table6977
+ GCC_except_table6980
+ GCC_except_table6981
+ GCC_except_table7022
+ GCC_except_table7024
+ GCC_except_table7027
+ GCC_except_table7028
+ GCC_except_table7029
+ GCC_except_table7031
+ GCC_except_table7032
+ GCC_except_table7034
+ GCC_except_table7038
+ GCC_except_table7039
+ GCC_except_table7043
+ GCC_except_table7091
+ GCC_except_table7098
+ GCC_except_table712
+ GCC_except_table7208
+ GCC_except_table7212
+ GCC_except_table7217
+ GCC_except_table7219
+ GCC_except_table7221
+ GCC_except_table7222
+ GCC_except_table7224
+ GCC_except_table7228
+ GCC_except_table7233
+ GCC_except_table735
+ GCC_except_table754
+ GCC_except_table778
+ GCC_except_table782
+ GCC_except_table793
+ GCC_except_table798
+ GCC_except_table898
+ GCC_except_table900
+ _OBJC_CLASS_$_HAPAccessoryServerIPConnectionStatistics
+ _OBJC_CLASS_$_HAPMetricsBonjourIncorrrectStateLogEvent
+ _OBJC_IVAR_$_HAPAccessoryServerIP._ipConnectionStatistics
+ _OBJC_IVAR_$_HAPAccessoryServerIPConnectionStatistics._accessory
+ _OBJC_IVAR_$_HAPAccessoryServerIPConnectionStatistics._lock
+ _OBJC_IVAR_$_HAPAccessoryServerIPConnectionStatistics._metricTriggered
+ _OBJC_IVAR_$_HAPAccessoryServerIPConnectionStatistics._sessionRestoreActive
+ _OBJC_IVAR_$_HAPAccessoryServerIPConnectionStatistics._state
+ _OBJC_IVAR_$_HAPMetricsBonjourIncorrrectStateLogEvent._deviceID
+ _OBJC_METACLASS_$_HAPAccessoryServerIPConnectionStatistics
+ _OBJC_METACLASS_$_HAPMetricsBonjourIncorrrectStateLogEvent
+ __CopyPairingIdentityDelegateCallback_f.14559
+ __CopyPairingIdentityDelegateCallback_f.21087
+ __CopyPairingIdentityDelegateCallback_f.2711
+ __FindPairedPeerDelegateCallback_f.2710
+ __OBJC_$_CLASS_PROP_LIST_HAPMetricsBonjourIncorrrectStateLogEvent
+ __OBJC_$_INSTANCE_METHODS_HAPAccessoryServerIPConnectionStatistics
+ __OBJC_$_INSTANCE_METHODS_HAPMetricsBonjourIncorrrectStateLogEvent
+ __OBJC_$_INSTANCE_VARIABLES_HAPAccessoryServerIPConnectionStatistics
+ __OBJC_$_INSTANCE_VARIABLES_HAPMetricsBonjourIncorrrectStateLogEvent
+ __OBJC_$_PROP_LIST_HAPAccessoryServerIPConnectionStatistics
+ __OBJC_$_PROP_LIST_HAPMetricsBonjourIncorrrectStateLogEvent
+ __OBJC_CLASS_PROTOCOLS_$_HAPMetricsBonjourIncorrrectStateLogEvent
+ __OBJC_CLASS_RO_$_HAPAccessoryServerIPConnectionStatistics
+ __OBJC_CLASS_RO_$_HAPMetricsBonjourIncorrrectStateLogEvent
+ __OBJC_METACLASS_RO_$_HAPAccessoryServerIPConnectionStatistics
+ __OBJC_METACLASS_RO_$_HAPMetricsBonjourIncorrrectStateLogEvent
+ __PairSetupPromptForSetupCodeDelegateCallback_f.21089
+ __SavePairedPeerDelegateCallback_f.14558
+ __SavePairedPeerDelegateCallback_f.21083
+ ___108-[HAPAccessoryServerIP _handleWriteECONNResetError:writeRequests:responses:timeout:queue:completionHandler:]_block_invoke.247
+ ___113-[HAPAccessoryServerIP _handleReadECONNRESETError:readCharacteristics:responses:timeout:queue:completionHandler:]_block_invoke.194
+ ___41-[HAPAccessoryServerIP getAccessoryInfo:]_block_invoke.476
+ ___44-[HAPAccessoryServerIP _pairVerifyStartWAC:]_block_invoke.111
+ ___45-[HAPAccessoryServerIP _pairSetupContinueWAC]_block_invoke.109
+ ___45-[HAPAccessoryServerIP stopPairingWithError:]_block_invoke.149
+ ___47-[HAPAccessoryServerIP identifyWithCompletion:]_block_invoke.609
+ ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.113
+ ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.116
+ ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.118
+ ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke_2.114
+ ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke_2.117
+ ___48-[HAPAccessoryServerIP startPairingWithRequest:]_block_invoke.147
+ ___49-[HAPAccessoryServerIP _continuePairingAfterWAC:]_block_invoke.119
+ ___49-[HAPAccessoryServerIP _continuePairingAfterWAC:]_block_invoke.124
+ ___49-[HAPAccessoryServerIP authSession:authComplete:]_block_invoke.526
+ ___50-[HAPAccessoryServerIP networkMonitorIsReachable:]_block_invoke.471
+ ___53-[HAPAccessoryServerIP setPairVerifyCompletionBlock:]_block_invoke.405
+ ___55-[HAPAccessoryServerIP authSession:validateUUID:token:]_block_invoke.516
+ ___55-[HAPAccessoryServerIP authSession:validateUUID:token:]_block_invoke.521
+ ___57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke.511
+ ___57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke_2.515
+ ___59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke.440
+ ___59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke_2.441
+ ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.418
+ ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.424
+ ___60-[HAPAccessoryServerIP _validatePairingAuthMethod:activity:]_block_invoke.495
+ ___65-[HAPAccessoryServerIP _continuePairingAfterAuthPromptWithRetry:]_block_invoke.432
+ ___76-[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]_block_invoke.248
+ ___76-[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]_block_invoke_2.256
+ ___76-[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]_block_invoke_3.257
+ ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke.568
+ ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke.570
+ ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.569
+ ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.571
+ ___79-[HAPAccessoryServerIP _queueListPairingWithCompletionQueue:completionHandler:]_block_invoke.171
+ ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1168
+ ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1169
+ ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke_2.1170
+ ___81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke.258
+ ___81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke_2.259
+ ___81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke_3.260
+ ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.195
+ ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.200
+ ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.209
+ ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke_2.216
+ ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke_3.217
+ ___83-[HAPAccessoryServerIP _writeCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.236
+ ___85-[HAPAccessoryServerIP _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.317
+ ___85-[HAPAccessoryServerIP _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.321
+ ___86-[HAPAccessoryServerIP _establishSecureConnectionAndFetchAttributeDatabaseWithReason:]_block_invoke.145
+ ___88-[HAPAccessoryServerIP _queueAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.170
+ ___88-[HAPAccessoryServerIP _startAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.540
+ ___90-[HAPAccessoryServerIP _queueEnableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.172
+ ___92-[HAPAccessoryServerIP writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.235
+ ___Block_byref_object_copy_.10106
+ ___Block_byref_object_copy_.10410
+ ___Block_byref_object_copy_.11226
+ ___Block_byref_object_copy_.11423
+ ___Block_byref_object_copy_.12446
+ ___Block_byref_object_copy_.13206
+ ___Block_byref_object_copy_.13432
+ ___Block_byref_object_copy_.14466
+ ___Block_byref_object_copy_.16429
+ ___Block_byref_object_copy_.16645
+ ___Block_byref_object_copy_.17660
+ ___Block_byref_object_copy_.18243
+ ___Block_byref_object_copy_.19324
+ ___Block_byref_object_copy_.1983
+ ___Block_byref_object_copy_.20147
+ ___Block_byref_object_copy_.24207
+ ___Block_byref_object_copy_.24372
+ ___Block_byref_object_copy_.2659
+ ___Block_byref_object_copy_.4046
+ ___Block_byref_object_copy_.4862
+ ___Block_byref_object_copy_.5096
+ ___Block_byref_object_copy_.5542
+ ___Block_byref_object_copy_.6176
+ ___Block_byref_object_copy_.6358
+ ___Block_byref_object_copy_.679
+ ___Block_byref_object_copy_.7210
+ ___Block_byref_object_copy_.8593
+ ___Block_byref_object_copy_.8904
+ ___Block_byref_object_copy_.9108
+ ___Block_byref_object_dispose_.10107
+ ___Block_byref_object_dispose_.10411
+ ___Block_byref_object_dispose_.11227
+ ___Block_byref_object_dispose_.11424
+ ___Block_byref_object_dispose_.12447
+ ___Block_byref_object_dispose_.13207
+ ___Block_byref_object_dispose_.13433
+ ___Block_byref_object_dispose_.14467
+ ___Block_byref_object_dispose_.16430
+ ___Block_byref_object_dispose_.16646
+ ___Block_byref_object_dispose_.17661
+ ___Block_byref_object_dispose_.18244
+ ___Block_byref_object_dispose_.19325
+ ___Block_byref_object_dispose_.1984
+ ___Block_byref_object_dispose_.20148
+ ___Block_byref_object_dispose_.24208
+ ___Block_byref_object_dispose_.24373
+ ___Block_byref_object_dispose_.2660
+ ___Block_byref_object_dispose_.4047
+ ___Block_byref_object_dispose_.4863
+ ___Block_byref_object_dispose_.5097
+ ___Block_byref_object_dispose_.5543
+ ___Block_byref_object_dispose_.6177
+ ___Block_byref_object_dispose_.6359
+ ___Block_byref_object_dispose_.680
+ ___Block_byref_object_dispose_.7211
+ ___Block_byref_object_dispose_.8594
+ ___Block_byref_object_dispose_.8905
+ ___Block_byref_object_dispose_.9109
+ ___block_literal_global.10463
+ ___block_literal_global.11222
+ ___block_literal_global.11590
+ ___block_literal_global.1186
+ ___block_literal_global.1223
+ ___block_literal_global.12692
+ ___block_literal_global.14583
+ ___block_literal_global.15010
+ ___block_literal_global.16156
+ ___block_literal_global.16438
+ ___block_literal_global.17822
+ ___block_literal_global.179
+ ___block_literal_global.1895
+ ___block_literal_global.19069
+ ___block_literal_global.19345
+ ___block_literal_global.19808
+ ___block_literal_global.20730
+ ___block_literal_global.22071
+ ___block_literal_global.22393
+ ___block_literal_global.23981
+ ___block_literal_global.24594
+ ___block_literal_global.2726
+ ___block_literal_global.4924
+ ___block_literal_global.5092
+ ___block_literal_global.5635
+ ___block_literal_global.6187
+ ___block_literal_global.6332
+ ___block_literal_global.7467
+ ___block_literal_global.759
+ ___block_literal_global.8299
+ ___block_literal_global.8677
+ ___block_literal_global.9218
+ ___block_literal_global.9792
+ __unnamed_array_storage.14595
+ __unnamed_array_storage.15617
+ __unnamed_array_storage.16160
+ __unnamed_array_storage.20651
+ _hkConfig.20714
+ _objc_msgSend$accessoryServerIPEvent:
+ _objc_msgSend$bonjourRemoveEvent
+ _objc_msgSend$generateBonjourRemoveMetric
+ _objc_msgSend$initWithDeviceID:
+ _objc_msgSend$ipConnectionStatistics
+ _sharedInstance.onceToken.15009
- GCC_except_table1003
- GCC_except_table1007
- GCC_except_table1020
- GCC_except_table1025
- GCC_except_table1034
- GCC_except_table1036
- GCC_except_table1038
- GCC_except_table1040
- GCC_except_table1166
- GCC_except_table1170
- GCC_except_table1172
- GCC_except_table1553
- GCC_except_table1564
- GCC_except_table1566
- GCC_except_table1572
- GCC_except_table1574
- GCC_except_table1578
- GCC_except_table1582
- GCC_except_table1584
- GCC_except_table1589
- GCC_except_table1593
- GCC_except_table1603
- GCC_except_table1611
- GCC_except_table1618
- GCC_except_table1622
- GCC_except_table1626
- GCC_except_table1630
- GCC_except_table1632
- GCC_except_table1776
- GCC_except_table1781
- GCC_except_table1783
- GCC_except_table1792
- GCC_except_table1794
- GCC_except_table1798
- GCC_except_table1803
- GCC_except_table1823
- GCC_except_table1828
- GCC_except_table1830
- GCC_except_table1834
- GCC_except_table1841
- GCC_except_table1843
- GCC_except_table1851
- GCC_except_table1853
- GCC_except_table1857
- GCC_except_table1861
- GCC_except_table1869
- GCC_except_table1880
- GCC_except_table1917
- GCC_except_table1923
- GCC_except_table2094
- GCC_except_table2123
- GCC_except_table2234
- GCC_except_table2242
- GCC_except_table2243
- GCC_except_table2244
- GCC_except_table2262
- GCC_except_table2276
- GCC_except_table2351
- GCC_except_table2363
- GCC_except_table2389
- GCC_except_table2397
- GCC_except_table2408
- GCC_except_table2422
- GCC_except_table2430
- GCC_except_table2438
- GCC_except_table2444
- GCC_except_table2446
- GCC_except_table2620
- GCC_except_table2689
- GCC_except_table2711
- GCC_except_table2726
- GCC_except_table2738
- GCC_except_table2739
- GCC_except_table2747
- GCC_except_table2754
- GCC_except_table2762
- GCC_except_table2818
- GCC_except_table2821
- GCC_except_table2826
- GCC_except_table2842
- GCC_except_table2856
- GCC_except_table2858
- GCC_except_table2862
- GCC_except_table2870
- GCC_except_table2878
- GCC_except_table2927
- GCC_except_table2935
- GCC_except_table2938
- GCC_except_table2961
- GCC_except_table3189
- GCC_except_table3248
- GCC_except_table3249
- GCC_except_table3253
- GCC_except_table3256
- GCC_except_table3261
- GCC_except_table3262
- GCC_except_table3264
- GCC_except_table3284
- GCC_except_table3295
- GCC_except_table3296
- GCC_except_table3298
- GCC_except_table3300
- GCC_except_table3303
- GCC_except_table3311
- GCC_except_table3314
- GCC_except_table3326
- GCC_except_table3328
- GCC_except_table3332
- GCC_except_table3340
- GCC_except_table3366
- GCC_except_table3384
- GCC_except_table3388
- GCC_except_table3391
- GCC_except_table3393
- GCC_except_table3395
- GCC_except_table3510
- GCC_except_table3535
- GCC_except_table3622
- GCC_except_table3629
- GCC_except_table3647
- GCC_except_table3651
- GCC_except_table3654
- GCC_except_table3660
- GCC_except_table3663
- GCC_except_table3666
- GCC_except_table3669
- GCC_except_table3672
- GCC_except_table3675
- GCC_except_table3680
- GCC_except_table3691
- GCC_except_table3694
- GCC_except_table3705
- GCC_except_table3713
- GCC_except_table3717
- GCC_except_table3724
- GCC_except_table3725
- GCC_except_table3729
- GCC_except_table3730
- GCC_except_table3748
- GCC_except_table3750
- GCC_except_table3752
- GCC_except_table3753
- GCC_except_table3756
- GCC_except_table3765
- GCC_except_table3767
- GCC_except_table3773
- GCC_except_table3778
- GCC_except_table3790
- GCC_except_table3801
- GCC_except_table3803
- GCC_except_table3812
- GCC_except_table3818
- GCC_except_table382
- GCC_except_table398
- GCC_except_table406
- GCC_except_table4078
- GCC_except_table4084
- GCC_except_table4101
- GCC_except_table4105
- GCC_except_table4122
- GCC_except_table4128
- GCC_except_table4141
- GCC_except_table4155
- GCC_except_table4159
- GCC_except_table4262
- GCC_except_table4342
- GCC_except_table4350
- GCC_except_table436
- GCC_except_table4394
- GCC_except_table4397
- GCC_except_table4398
- GCC_except_table4399
- GCC_except_table4400
- GCC_except_table443
- GCC_except_table4491
- GCC_except_table4492
- GCC_except_table4493
- GCC_except_table4494
- GCC_except_table4495
- GCC_except_table4496
- GCC_except_table4517
- GCC_except_table4528
- GCC_except_table4536
- GCC_except_table4565
- GCC_except_table4566
- GCC_except_table457
- GCC_except_table458
- GCC_except_table4585
- GCC_except_table4598
- GCC_except_table4603
- GCC_except_table4606
- GCC_except_table463
- GCC_except_table466
- GCC_except_table478
- GCC_except_table482
- GCC_except_table4867
- GCC_except_table4871
- GCC_except_table4905
- GCC_except_table4909
- GCC_except_table491
- GCC_except_table4911
- GCC_except_table4913
- GCC_except_table497
- GCC_except_table5066
- GCC_except_table5072
- GCC_except_table5077
- GCC_except_table5078
- GCC_except_table5079
- GCC_except_table5085
- GCC_except_table5119
- GCC_except_table5120
- GCC_except_table5121
- GCC_except_table5139
- GCC_except_table515
- GCC_except_table5151
- GCC_except_table5154
- GCC_except_table5159
- GCC_except_table5175
- GCC_except_table525
- GCC_except_table532
- GCC_except_table5374
- GCC_except_table5386
- GCC_except_table5391
- GCC_except_table5394
- GCC_except_table5395
- GCC_except_table5397
- GCC_except_table5398
- GCC_except_table5400
- GCC_except_table5430
- GCC_except_table5452
- GCC_except_table5456
- GCC_except_table5460
- GCC_except_table5465
- GCC_except_table5469
- GCC_except_table5473
- GCC_except_table5477
- GCC_except_table5481
- GCC_except_table5489
- GCC_except_table5493
- GCC_except_table5550
- GCC_except_table5551
- GCC_except_table5552
- GCC_except_table5553
- GCC_except_table559
- GCC_except_table5611
- GCC_except_table5612
- GCC_except_table5626
- GCC_except_table563
- GCC_except_table5632
- GCC_except_table5645
- GCC_except_table5648
- GCC_except_table5649
- GCC_except_table5654
- GCC_except_table5657
- GCC_except_table5664
- GCC_except_table5681
- GCC_except_table5688
- GCC_except_table5694
- GCC_except_table5703
- GCC_except_table5705
- GCC_except_table5709
- GCC_except_table5710
- GCC_except_table5724
- GCC_except_table5726
- GCC_except_table573
- GCC_except_table5734
- GCC_except_table5749
- GCC_except_table5750
- GCC_except_table5755
- GCC_except_table5759
- GCC_except_table5760
- GCC_except_table5763
- GCC_except_table5769
- GCC_except_table5775
- GCC_except_table587
- GCC_except_table591
- GCC_except_table5926
- GCC_except_table595
- GCC_except_table5980
- GCC_except_table5983
- GCC_except_table5987
- GCC_except_table5993
- GCC_except_table6000
- GCC_except_table6017
- GCC_except_table6021
- GCC_except_table6022
- GCC_except_table6023
- GCC_except_table604
- GCC_except_table605
- GCC_except_table6071
- GCC_except_table6072
- GCC_except_table6074
- GCC_except_table6077
- GCC_except_table610
- GCC_except_table6107
- GCC_except_table6108
- GCC_except_table6113
- GCC_except_table613
- GCC_except_table6148
- GCC_except_table6150
- GCC_except_table6158
- GCC_except_table616
- GCC_except_table6163
- GCC_except_table6164
- GCC_except_table6165
- GCC_except_table6179
- GCC_except_table6188
- GCC_except_table6194
- GCC_except_table6207
- GCC_except_table621
- GCC_except_table6221
- GCC_except_table6227
- GCC_except_table6228
- GCC_except_table6232
- GCC_except_table6240
- GCC_except_table6244
- GCC_except_table625
- GCC_except_table6271
- GCC_except_table6273
- GCC_except_table6274
- GCC_except_table6300
- GCC_except_table631
- GCC_except_table632
- GCC_except_table637
- GCC_except_table638
- GCC_except_table6464
- GCC_except_table6527
- GCC_except_table6559
- GCC_except_table6562
- GCC_except_table664
- GCC_except_table6726
- GCC_except_table675
- GCC_except_table676
- GCC_except_table6789
- GCC_except_table6852
- GCC_except_table6858
- GCC_except_table6903
- GCC_except_table6905
- GCC_except_table6907
- GCC_except_table6909
- GCC_except_table6911
- GCC_except_table6913
- GCC_except_table6915
- GCC_except_table6917
- GCC_except_table6919
- GCC_except_table6926
- GCC_except_table6928
- GCC_except_table6930
- GCC_except_table6959
- GCC_except_table6962
- GCC_except_table6963
- GCC_except_table7002
- GCC_except_table7003
- GCC_except_table7004
- GCC_except_table7006
- GCC_except_table7007
- GCC_except_table7009
- GCC_except_table7010
- GCC_except_table7011
- GCC_except_table7013
- GCC_except_table7014
- GCC_except_table7016
- GCC_except_table7073
- GCC_except_table7080
- GCC_except_table710
- GCC_except_table7174
- GCC_except_table7190
- GCC_except_table7194
- GCC_except_table7197
- GCC_except_table7199
- GCC_except_table7201
- GCC_except_table7203
- GCC_except_table7204
- GCC_except_table7206
- GCC_except_table733
- GCC_except_table751
- GCC_except_table775
- GCC_except_table779
- GCC_except_table790
- GCC_except_table795
- GCC_except_table895
- GCC_except_table897
- __CopyPairingIdentityDelegateCallback_f.14401
- __CopyPairingIdentityDelegateCallback_f.20856
- __CopyPairingIdentityDelegateCallback_f.2624
- __FindPairedPeerDelegateCallback_f.2623
- __PairSetupPromptForSetupCodeDelegateCallback_f.20858
- __SavePairedPeerDelegateCallback_f.14400
- __SavePairedPeerDelegateCallback_f.20852
- ___108-[HAPAccessoryServerIP _handleWriteECONNResetError:writeRequests:responses:timeout:queue:completionHandler:]_block_invoke.246
- ___113-[HAPAccessoryServerIP _handleReadECONNRESETError:readCharacteristics:responses:timeout:queue:completionHandler:]_block_invoke.193
- ___41-[HAPAccessoryServerIP getAccessoryInfo:]_block_invoke.475
- ___44-[HAPAccessoryServerIP _pairVerifyStartWAC:]_block_invoke.110
- ___45-[HAPAccessoryServerIP _pairSetupContinueWAC]_block_invoke.108
- ___45-[HAPAccessoryServerIP stopPairingWithError:]_block_invoke.148
- ___47-[HAPAccessoryServerIP identifyWithCompletion:]_block_invoke.608
- ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.111
- ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.114
- ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.117
- ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke_2.113
- ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke_2.116
- ___48-[HAPAccessoryServerIP startPairingWithRequest:]_block_invoke.146
- ___49-[HAPAccessoryServerIP _continuePairingAfterWAC:]_block_invoke.118
- ___49-[HAPAccessoryServerIP _continuePairingAfterWAC:]_block_invoke.123
- ___49-[HAPAccessoryServerIP authSession:authComplete:]_block_invoke.525
- ___50-[HAPAccessoryServerIP networkMonitorIsReachable:]_block_invoke.470
- ___53-[HAPAccessoryServerIP setPairVerifyCompletionBlock:]_block_invoke.404
- ___55-[HAPAccessoryServerIP authSession:validateUUID:token:]_block_invoke.515
- ___55-[HAPAccessoryServerIP authSession:validateUUID:token:]_block_invoke.520
- ___57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke.510
- ___57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke_2.514
- ___59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke.439
- ___59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke_2.440
- ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.417
- ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.422
- ___60-[HAPAccessoryServerIP _validatePairingAuthMethod:activity:]_block_invoke.494
- ___65-[HAPAccessoryServerIP _continuePairingAfterAuthPromptWithRetry:]_block_invoke.431
- ___76-[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]_block_invoke.247
- ___76-[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]_block_invoke_2.255
- ___76-[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]_block_invoke_3.256
- ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke.567
- ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke.569
- ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.568
- ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.570
- ___79-[HAPAccessoryServerIP _queueListPairingWithCompletionQueue:completionHandler:]_block_invoke.170
- ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1160
- ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1161
- ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke_2.1162
- ___81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke.257
- ___81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke_2.258
- ___81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke_3.259
- ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.194
- ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.199
- ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.208
- ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke_2.215
- ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke_3.216
- ___83-[HAPAccessoryServerIP _writeCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.235
- ___85-[HAPAccessoryServerIP _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.316
- ___85-[HAPAccessoryServerIP _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.320
- ___86-[HAPAccessoryServerIP _establishSecureConnectionAndFetchAttributeDatabaseWithReason:]_block_invoke.144
- ___88-[HAPAccessoryServerIP _queueAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.169
- ___88-[HAPAccessoryServerIP _startAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.539
- ___90-[HAPAccessoryServerIP _queueEnableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.171
- ___92-[HAPAccessoryServerIP writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.234
- ___Block_byref_object_copy_.10262
- ___Block_byref_object_copy_.11081
- ___Block_byref_object_copy_.11278
- ___Block_byref_object_copy_.12297
- ___Block_byref_object_copy_.13057
- ___Block_byref_object_copy_.13283
- ___Block_byref_object_copy_.14309
- ___Block_byref_object_copy_.16267
- ___Block_byref_object_copy_.16483
- ___Block_byref_object_copy_.17427
- ___Block_byref_object_copy_.18022
- ___Block_byref_object_copy_.1893
- ___Block_byref_object_copy_.19102
- ___Block_byref_object_copy_.19921
- ___Block_byref_object_copy_.23973
- ___Block_byref_object_copy_.24138
- ___Block_byref_object_copy_.2571
- ___Block_byref_object_copy_.3960
- ___Block_byref_object_copy_.4783
- ___Block_byref_object_copy_.5020
- ___Block_byref_object_copy_.5464
- ___Block_byref_object_copy_.6097
- ___Block_byref_object_copy_.6279
- ___Block_byref_object_copy_.677
- ___Block_byref_object_copy_.7035
- ___Block_byref_object_copy_.8446
- ___Block_byref_object_copy_.8757
- ___Block_byref_object_copy_.8960
- ___Block_byref_object_copy_.9958
- ___Block_byref_object_dispose_.10263
- ___Block_byref_object_dispose_.11082
- ___Block_byref_object_dispose_.11279
- ___Block_byref_object_dispose_.12298
- ___Block_byref_object_dispose_.13058
- ___Block_byref_object_dispose_.13284
- ___Block_byref_object_dispose_.14310
- ___Block_byref_object_dispose_.16268
- ___Block_byref_object_dispose_.16484
- ___Block_byref_object_dispose_.17428
- ___Block_byref_object_dispose_.18023
- ___Block_byref_object_dispose_.1894
- ___Block_byref_object_dispose_.19103
- ___Block_byref_object_dispose_.19922
- ___Block_byref_object_dispose_.23974
- ___Block_byref_object_dispose_.24139
- ___Block_byref_object_dispose_.2572
- ___Block_byref_object_dispose_.3961
- ___Block_byref_object_dispose_.4784
- ___Block_byref_object_dispose_.5021
- ___Block_byref_object_dispose_.5465
- ___Block_byref_object_dispose_.6098
- ___Block_byref_object_dispose_.6280
- ___Block_byref_object_dispose_.678
- ___Block_byref_object_dispose_.7036
- ___Block_byref_object_dispose_.8447
- ___Block_byref_object_dispose_.8758
- ___Block_byref_object_dispose_.8961
- ___Block_byref_object_dispose_.9959
- ___block_literal_global.10314
- ___block_literal_global.11077
- ___block_literal_global.11444
- ___block_literal_global.1178
- ___block_literal_global.1215
- ___block_literal_global.12543
- ___block_literal_global.14425
- ___block_literal_global.14852
- ___block_literal_global.15995
- ___block_literal_global.16276
- ___block_literal_global.17602
- ___block_literal_global.178
- ___block_literal_global.1805
- ___block_literal_global.18847
- ___block_literal_global.19124
- ___block_literal_global.19584
- ___block_literal_global.20500
- ___block_literal_global.21836
- ___block_literal_global.22159
- ___block_literal_global.23747
- ___block_literal_global.24360
- ___block_literal_global.2642
- ___block_literal_global.4847
- ___block_literal_global.5016
- ___block_literal_global.5556
- ___block_literal_global.6108
- ___block_literal_global.6253
- ___block_literal_global.7299
- ___block_literal_global.740
- ___block_literal_global.8127
- ___block_literal_global.8530
- ___block_literal_global.9070
- ___block_literal_global.9644
- __unnamed_array_storage.14437
- __unnamed_array_storage.15458
- __unnamed_array_storage.15999
- __unnamed_array_storage.20421
- _hkConfig.20484
- _sharedInstance.onceToken.14851
CStrings:
+ "%{public}@%@ IP Connection BonjourAdd"
+ "%{public}@%@ IP Connection BonjourRemoved"
+ "%{public}@%@ IP Connection BonjourUndiscovered"
+ "%{public}@%@ IP Connection Connected"
+ "%{public}@%@ IP Connection Connection Failed"
+ "%{public}@%@ IP Connection ConnectionTerminated"
+ "%{public}@%@ IP Connection Session Restore Deregistration"
+ "%{public}@%@ IP Connection Session Restore Registration"
+ "%{public}@%@ IP Connection Successful Transaction"
+ "%{public}@%@ IP Connection bonjour submitting metric"
+ "%{public}@%@ updating discovery state from %@ to %@"
+ "%{public}@*** failed to build reachability notify dictionary -- invalid accessory or identifier %@"
+ "%{public}@*** transitioning to invalid state %@ while connected"
+ "%{public}@Cannot generate bonjour metric as accessory server is nil"
+ "%{public}@Will not update state as accessory server is nil"
+ "@\"HAPAccessoryServerIPConnectionStatistics\""
+ "HAPAccessoryServerIPConnectionStatistics"
+ "HAPAccessoryServerIPDiscoveryState_Connected"
+ "HAPAccessoryServerIPDiscoveryState_DisconnectionPending"
+ "HAPAccessoryServerIPDiscoveryState_Discovered"
+ "HAPAccessoryServerIPDiscoveryState_Undiscovered"
+ "HAPMetricsBonjourIncorrrectStateLogEvent"
+ "T@\"HAPAccessoryServer\",R,W,N,V_accessory"
+ "T@\"HAPAccessoryServerIPConnectionStatistics\",&,N,V_ipConnectionStatistics"
+ "T@\"NSString\",&,N,V_deviceID"
+ "TB,R,V_metricTriggered"
+ "TB,R,V_sessionRestoreActive"
+ "Tq,R,V_state"
+ "_ipConnectionStatistics"
+ "_metricTriggered"
+ "accessoryID_STRING"
+ "accessoryServerIPEvent:"
+ "bonjourRemoveEvent"
+ "com.apple.HomeKit.daemon.bonjourIncorrectState"
+ "generateBonjourRemoveMetric"
+ "initWithDeviceID:"
+ "ipConnectionStatistics"
+ "metricTriggered"
+ "setDeviceID:"
+ "setIpConnectionStatistics:"
+ "\x83\"\x12]\x12"
- "\x83\"\x12]\x11"

```
