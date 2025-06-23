## CoreHAP

> `/System/Library/PrivateFrameworks/CoreHAP.framework/CoreHAP`

```diff

-1323.0.6.0.1
-  __TEXT.__text: 0x1a6ac4
-  __TEXT.__auth_stubs: 0x15b0
-  __TEXT.__objc_methlist: 0x138c8
+1334.0.0.0.1
+  __TEXT.__text: 0x1a8f00
+  __TEXT.__auth_stubs: 0x15c0
+  __TEXT.__objc_methlist: 0x13990
   __TEXT.__const: 0x700
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__gcc_except_tab: 0x62f0
-  __TEXT.__cstring: 0x10a1e
-  __TEXT.__oslogstring: 0x1ff5a
-  __TEXT.__unwind_info: 0x5d38
-  __TEXT.__objc_classname: 0x2df8
-  __TEXT.__objc_methname: 0x268b3
-  __TEXT.__objc_methtype: 0x8fb9
-  __TEXT.__objc_stubs: 0x187c0
-  __DATA_CONST.__got: 0xa68
-  __DATA_CONST.__const: 0x5070
-  __DATA_CONST.__objc_classlist: 0x960
+  __TEXT.__gcc_except_tab: 0x63b4
+  __TEXT.__cstring: 0x10ae0
+  __TEXT.__oslogstring: 0x20320
+  __TEXT.__unwind_info: 0x5d98
+  __TEXT.__objc_classname: 0x2e43
+  __TEXT.__objc_methname: 0x26a8f
+  __TEXT.__objc_methtype: 0x9054
+  __TEXT.__objc_stubs: 0x188e0
+  __DATA_CONST.__got: 0xa78
+  __DATA_CONST.__const: 0x5078
+  __DATA_CONST.__objc_classlist: 0x968
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x338
+  __DATA_CONST.__objc_protolist: 0x340
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6f30
+  __DATA_CONST.__objc_selrefs: 0x6f80
   __DATA_CONST.__objc_protorefs: 0xc0
-  __DATA_CONST.__objc_superrefs: 0x7e0
+  __DATA_CONST.__objc_superrefs: 0x7e8
   __DATA_CONST.__objc_arraydata: 0x208
-  __AUTH_CONST.__auth_got: 0xae8
+  __AUTH_CONST.__auth_got: 0xaf0
   __AUTH_CONST.__const: 0x800
-  __AUTH_CONST.__cfstring: 0xdb20
-  __AUTH_CONST.__objc_const: 0x220d0
+  __AUTH_CONST.__cfstring: 0xdbe0
+  __AUTH_CONST.__objc_const: 0x22338
   __AUTH_CONST.__objc_intobj: 0x6c0
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0xd8
-  __AUTH.__objc_data: 0x4dd0
-  __DATA.__objc_ivar: 0x14f4
-  __DATA.__data: 0x26c2
+  __AUTH.__objc_data: 0x4e20
+  __DATA.__objc_ivar: 0x1508
+  __DATA.__data: 0x2722
   __DATA.__bss: 0x499
   __DATA_DIRTY.__objc_data: 0xff0
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: AFAED248-15CF-3B34-B17A-D9779977E15C
-  Functions: 7481
-  Symbols:   24356
-  CStrings:  12891
+  UUID: C04A3111-2977-3F77-A463-09064F8CA1B4
+  Functions: 7509
+  Symbols:   24437
+  CStrings:  12938
 
Symbols:
+ -[HAP2AccessoryServer(Unpaired) pairWithDelegate:pairingRequest:]
+ -[HAP2AccessoryServerController currentLocalPairingIdentity]
+ -[HAP2AccessoryServerController keyBag]
+ -[HAP2AccessoryServerPairingDriver pairAccessory:pairingRequest:delegate:]
+ -[HAP2AccessoryServerPairingDriver pairingRequest]
+ -[HAP2AccessoryServerPairingDriver setPairingRequest:]
+ -[HAP2CoAPIOThread initWithQualityOfService:delegate:dateProvider:]
+ -[HAPAccessory readCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]
+ -[HAPAccessory readValueForCharacteristic:timeout:expiry:completionQueue:completionHandler:]
+ -[HAPAccessory writeCharacteristicValue:timeout:expiry:completionQueue:completionHandler:]
+ -[HAPAccessory writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]
+ -[HAPAccessoryServer readCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]
+ -[HAPAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]
+ -[HAPAccessoryServerHAP2Adapter readCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]
+ -[HAPAccessoryServerHAP2Adapter writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]
+ -[HAPAccessoryServerIP _handlePrepareWriteResponseObject:type:prepareIdentifier:httpStatus:error:requestTuples:timeout:expiry:queue:originalCompletion:completion:]
+ -[HAPAccessoryServerIP _handleReadECONNRESETError:readCharacteristics:responses:timeout:expiry:queue:completionHandler:]
+ -[HAPAccessoryServerIP _handleWriteECONNResetError:writeRequests:responses:timeout:expiry:queue:completionHandler:]
+ -[HAPAccessoryServerIP _insertReadCharacteristicValues:timeout:expiry:queue:completionHandler:]
+ -[HAPAccessoryServerIP _insertWriteCharacteristicValues:timeout:expiry:queue:withCompletionHandler:]
+ -[HAPAccessoryServerIP _performExecuteWriteValues:prepareIdentifier:timeout:expiry:queue:completionHandler:]
+ -[HAPAccessoryServerIP _performTimedWriteValues:timeout:expiry:queue:completionHandler:]
+ -[HAPAccessoryServerIP _performWriteValues:timeout:expiry:queue:completionHandler:]
+ -[HAPAccessoryServerIP _queueReadCharacteristicValues:timeout:expiry:queue:completionHandler:]
+ -[HAPAccessoryServerIP _queueWriteCharacteristicValues:timeout:expiry:queue:withCompletionHandler:]
+ -[HAPAccessoryServerIP _queuedReadOperationBlock:timeout:expiry:queue:completionHandler:]
+ -[HAPAccessoryServerIP _queuedWriteOperationBlock:timeout:expiry:queue:completionHandler:]
+ -[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]
+ -[HAPAccessoryServerIP _writeCharacteristicValues:timeout:expiry:queue:completionHandler:]
+ -[HAPAccessoryServerIP readCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]
+ -[HAPAccessoryServerIP remainingTTLForExpiry:]
+ -[HAPAccessoryServerIP writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]
+ -[HAPKeyBag(AccessoryUtils) associateControllerIdentifier:error:]
+ -[HAPKeyBag(AccessoryUtils) shouldRetryPVDueToAuthenticationError:]
+ -[HAPMetricsDispatcher submitLogEvent:error:]
+ -[HAPMetricsPowerManagementLogEvent .cxx_destruct]
+ -[HAPMetricsPowerManagementLogEvent accessoryIdentifier]
+ -[HAPMetricsPowerManagementLogEvent coreAnalyticsEventDictionary]
+ -[HAPMetricsPowerManagementLogEvent coreAnalyticsEventName]
+ -[HAPMetricsPowerManagementLogEvent coreAnalyticsEventOptions]
+ -[HAPMetricsPowerManagementLogEvent description]
+ -[HAPMetricsPowerManagementLogEvent initForHAPAccessory:withLogType:]
+ -[HAPMetricsPowerManagementLogEvent initForSuspendedAccessory:]
+ -[HAPMetricsPowerManagementLogEvent logType]
+ -[_HAPAccessoryServerBTLE100 readCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]
+ -[_HAPAccessoryServerBTLE100 writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]
+ -[_HAPAccessoryServerBTLE200 readCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]
+ -[_HAPAccessoryServerBTLE200 writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]
+ GCC_except_table1049
+ GCC_except_table1053
+ GCC_except_table1066
+ GCC_except_table1071
+ GCC_except_table1080
+ GCC_except_table1082
+ GCC_except_table1084
+ GCC_except_table1086
+ GCC_except_table1212
+ GCC_except_table1216
+ GCC_except_table1218
+ GCC_except_table1430
+ GCC_except_table1636
+ GCC_except_table1639
+ GCC_except_table1647
+ GCC_except_table1649
+ GCC_except_table1655
+ GCC_except_table1657
+ GCC_except_table1661
+ GCC_except_table1667
+ GCC_except_table1672
+ GCC_except_table1676
+ GCC_except_table1686
+ GCC_except_table1701
+ GCC_except_table1705
+ GCC_except_table1709
+ GCC_except_table1713
+ GCC_except_table1715
+ GCC_except_table1868
+ GCC_except_table1869
+ GCC_except_table1871
+ GCC_except_table1873
+ GCC_except_table1882
+ GCC_except_table1888
+ GCC_except_table1891
+ GCC_except_table1893
+ GCC_except_table1896
+ GCC_except_table1916
+ GCC_except_table1918
+ GCC_except_table1927
+ GCC_except_table1931
+ GCC_except_table1933
+ GCC_except_table1939
+ GCC_except_table1941
+ GCC_except_table1943
+ GCC_except_table1947
+ GCC_except_table1951
+ GCC_except_table1959
+ GCC_except_table1970
+ GCC_except_table200
+ GCC_except_table2008
+ GCC_except_table2014
+ GCC_except_table207
+ GCC_except_table209
+ GCC_except_table212
+ GCC_except_table215
+ GCC_except_table217
+ GCC_except_table2192
+ GCC_except_table2198
+ GCC_except_table220
+ GCC_except_table2204
+ GCC_except_table2207
+ GCC_except_table2210
+ GCC_except_table2213
+ GCC_except_table2225
+ GCC_except_table2226
+ GCC_except_table2228
+ GCC_except_table223
+ GCC_except_table225
+ GCC_except_table2324
+ GCC_except_table2332
+ GCC_except_table2333
+ GCC_except_table2334
+ GCC_except_table2335
+ GCC_except_table2336
+ GCC_except_table2337
+ GCC_except_table234
+ GCC_except_table2352
+ GCC_except_table2366
+ GCC_except_table238
+ GCC_except_table2446
+ GCC_except_table2458
+ GCC_except_table2484
+ GCC_except_table2492
+ GCC_except_table2503
+ GCC_except_table2517
+ GCC_except_table2520
+ GCC_except_table2525
+ GCC_except_table2533
+ GCC_except_table2539
+ GCC_except_table2541
+ GCC_except_table2715
+ GCC_except_table2765
+ GCC_except_table2781
+ GCC_except_table2784
+ GCC_except_table2798
+ GCC_except_table2806
+ GCC_except_table2821
+ GCC_except_table2833
+ GCC_except_table2834
+ GCC_except_table2836
+ GCC_except_table2849
+ GCC_except_table2852
+ GCC_except_table2857
+ GCC_except_table2913
+ GCC_except_table2921
+ GCC_except_table2923
+ GCC_except_table2937
+ GCC_except_table2951
+ GCC_except_table2953
+ GCC_except_table2957
+ GCC_except_table2965
+ GCC_except_table2973
+ GCC_except_table3022
+ GCC_except_table3030
+ GCC_except_table3032
+ GCC_except_table3033
+ GCC_except_table3056
+ GCC_except_table3300
+ GCC_except_table3364
+ GCC_except_table3369
+ GCC_except_table3372
+ GCC_except_table3374
+ GCC_except_table3375
+ GCC_except_table3377
+ GCC_except_table3378
+ GCC_except_table3387
+ GCC_except_table3397
+ GCC_except_table3400
+ GCC_except_table3411
+ GCC_except_table3414
+ GCC_except_table3416
+ GCC_except_table3419
+ GCC_except_table3422
+ GCC_except_table3424
+ GCC_except_table3427
+ GCC_except_table3430
+ GCC_except_table3442
+ GCC_except_table3444
+ GCC_except_table3448
+ GCC_except_table3452
+ GCC_except_table3456
+ GCC_except_table3482
+ GCC_except_table3507
+ GCC_except_table3509
+ GCC_except_table3511
+ GCC_except_table3593
+ GCC_except_table3594
+ GCC_except_table3595
+ GCC_except_table3596
+ GCC_except_table3597
+ GCC_except_table3598
+ GCC_except_table3599
+ GCC_except_table3636
+ GCC_except_table3662
+ GCC_except_table3760
+ GCC_except_table3782
+ GCC_except_table3785
+ GCC_except_table3788
+ GCC_except_table3791
+ GCC_except_table3794
+ GCC_except_table3797
+ GCC_except_table3800
+ GCC_except_table3803
+ GCC_except_table3806
+ GCC_except_table3811
+ GCC_except_table3821
+ GCC_except_table3824
+ GCC_except_table3835
+ GCC_except_table3843
+ GCC_except_table3847
+ GCC_except_table3855
+ GCC_except_table3859
+ GCC_except_table3860
+ GCC_except_table3878
+ GCC_except_table3882
+ GCC_except_table3883
+ GCC_except_table3892
+ GCC_except_table3895
+ GCC_except_table3903
+ GCC_except_table3905
+ GCC_except_table3908
+ GCC_except_table3920
+ GCC_except_table3931
+ GCC_except_table3933
+ GCC_except_table3948
+ GCC_except_table405
+ GCC_except_table421
+ GCC_except_table4214
+ GCC_except_table4231
+ GCC_except_table4235
+ GCC_except_table4258
+ GCC_except_table4271
+ GCC_except_table4285
+ GCC_except_table4289
+ GCC_except_table429
+ GCC_except_table4402
+ GCC_except_table4482
+ GCC_except_table4490
+ GCC_except_table4500
+ GCC_except_table4540
+ GCC_except_table4541
+ GCC_except_table4542
+ GCC_except_table4543
+ GCC_except_table459
+ GCC_except_table4641
+ GCC_except_table4642
+ GCC_except_table4643
+ GCC_except_table4644
+ GCC_except_table4645
+ GCC_except_table4652
+ GCC_except_table4653
+ GCC_except_table4655
+ GCC_except_table4662
+ GCC_except_table4665
+ GCC_except_table4667
+ GCC_except_table467
+ GCC_except_table4675
+ GCC_except_table4678
+ GCC_except_table4682
+ GCC_except_table4686
+ GCC_except_table4715
+ GCC_except_table4716
+ GCC_except_table4735
+ GCC_except_table4745
+ GCC_except_table4748
+ GCC_except_table4753
+ GCC_except_table4756
+ GCC_except_table482
+ GCC_except_table484
+ GCC_except_table487
+ GCC_except_table490
+ GCC_except_table502
+ GCC_except_table5020
+ GCC_except_table5024
+ GCC_except_table506
+ GCC_except_table5062
+ GCC_except_table5064
+ GCC_except_table5066
+ GCC_except_table509
+ GCC_except_table516
+ GCC_except_table522
+ GCC_except_table5232
+ GCC_except_table5238
+ GCC_except_table5242
+ GCC_except_table5243
+ GCC_except_table5244
+ GCC_except_table5245
+ GCC_except_table5251
+ GCC_except_table5285
+ GCC_except_table5286
+ GCC_except_table5287
+ GCC_except_table5319
+ GCC_except_table5322
+ GCC_except_table5327
+ GCC_except_table5329
+ GCC_except_table5343
+ GCC_except_table547
+ GCC_except_table5545
+ GCC_except_table5557
+ GCC_except_table5562
+ GCC_except_table5565
+ GCC_except_table5566
+ GCC_except_table5568
+ GCC_except_table5569
+ GCC_except_table557
+ GCC_except_table5571
+ GCC_except_table5601
+ GCC_except_table5623
+ GCC_except_table5627
+ GCC_except_table5631
+ GCC_except_table5636
+ GCC_except_table564
+ GCC_except_table5640
+ GCC_except_table5644
+ GCC_except_table5648
+ GCC_except_table5652
+ GCC_except_table5660
+ GCC_except_table5662
+ GCC_except_table5664
+ GCC_except_table5724
+ GCC_except_table5725
+ GCC_except_table5726
+ GCC_except_table5727
+ GCC_except_table5728
+ GCC_except_table5791
+ GCC_except_table5792
+ GCC_except_table5804
+ GCC_except_table5823
+ GCC_except_table5826
+ GCC_except_table5827
+ GCC_except_table5832
+ GCC_except_table5835
+ GCC_except_table5845
+ GCC_except_table5859
+ GCC_except_table5872
+ GCC_except_table5881
+ GCC_except_table5883
+ GCC_except_table5887
+ GCC_except_table5904
+ GCC_except_table5906
+ GCC_except_table591
+ GCC_except_table5915
+ GCC_except_table5930
+ GCC_except_table5936
+ GCC_except_table5940
+ GCC_except_table5941
+ GCC_except_table5944
+ GCC_except_table595
+ GCC_except_table5950
+ GCC_except_table5954
+ GCC_except_table5958
+ GCC_except_table5960
+ GCC_except_table5962
+ GCC_except_table5966
+ GCC_except_table600
+ GCC_except_table608
+ GCC_except_table6117
+ GCC_except_table6173
+ GCC_except_table6176
+ GCC_except_table6180
+ GCC_except_table6186
+ GCC_except_table6193
+ GCC_except_table6194
+ GCC_except_table621
+ GCC_except_table6210
+ GCC_except_table6214
+ GCC_except_table6215
+ GCC_except_table6216
+ GCC_except_table625
+ GCC_except_table6265
+ GCC_except_table6266
+ GCC_except_table6268
+ GCC_except_table629
+ GCC_except_table6299
+ GCC_except_table6300
+ GCC_except_table6305
+ GCC_except_table6325
+ GCC_except_table6342
+ GCC_except_table6343
+ GCC_except_table6344
+ GCC_except_table6352
+ GCC_except_table6357
+ GCC_except_table6358
+ GCC_except_table6359
+ GCC_except_table6376
+ GCC_except_table6382
+ GCC_except_table6388
+ GCC_except_table639
+ GCC_except_table640
+ GCC_except_table6400
+ GCC_except_table6401
+ GCC_except_table6415
+ GCC_except_table6421
+ GCC_except_table6422
+ GCC_except_table6426
+ GCC_except_table6434
+ GCC_except_table6438
+ GCC_except_table6444
+ GCC_except_table645
+ GCC_except_table6465
+ GCC_except_table6467
+ GCC_except_table6468
+ GCC_except_table648
+ GCC_except_table6494
+ GCC_except_table651
+ GCC_except_table660
+ GCC_except_table6658
+ GCC_except_table666
+ GCC_except_table667
+ GCC_except_table672
+ GCC_except_table6721
+ GCC_except_table673
+ GCC_except_table6753
+ GCC_except_table6756
+ GCC_except_table6920
+ GCC_except_table6983
+ GCC_except_table699
+ GCC_except_table7047
+ GCC_except_table7053
+ GCC_except_table706
+ GCC_except_table7099
+ GCC_except_table7103
+ GCC_except_table7105
+ GCC_except_table7107
+ GCC_except_table7109
+ GCC_except_table7111
+ GCC_except_table7113
+ GCC_except_table7115
+ GCC_except_table7117
+ GCC_except_table7119
+ GCC_except_table7122
+ GCC_except_table7124
+ GCC_except_table7126
+ GCC_except_table7129
+ GCC_except_table713
+ GCC_except_table714
+ GCC_except_table7155
+ GCC_except_table7158
+ GCC_except_table7159
+ GCC_except_table7198
+ GCC_except_table7199
+ GCC_except_table7200
+ GCC_except_table7202
+ GCC_except_table7203
+ GCC_except_table7205
+ GCC_except_table7206
+ GCC_except_table7207
+ GCC_except_table7209
+ GCC_except_table7210
+ GCC_except_table7212
+ GCC_except_table7216
+ GCC_except_table7217
+ GCC_except_table7221
+ GCC_except_table7269
+ GCC_except_table7276
+ GCC_except_table7370
+ GCC_except_table7386
+ GCC_except_table7388
+ GCC_except_table7390
+ GCC_except_table7393
+ GCC_except_table7395
+ GCC_except_table7397
+ GCC_except_table7399
+ GCC_except_table7400
+ GCC_except_table7402
+ GCC_except_table7406
+ GCC_except_table7411
+ GCC_except_table748
+ GCC_except_table771
+ GCC_except_table790
+ GCC_except_table814
+ GCC_except_table818
+ GCC_except_table837
+ GCC_except_table941
+ GCC_except_table943
+ _HMFUptime
+ _OBJC_CLASS_$_HAPMetricsPowerManagementLogEvent
+ _OBJC_CLASS_$_HMFDate
+ _OBJC_IVAR_$_HAP2AccessoryServerController._keyBag
+ _OBJC_IVAR_$_HAP2AccessoryServerPairingDriver._pairingRequest
+ _OBJC_IVAR_$_HAP2CoAPIOThread._dateProvider
+ _OBJC_IVAR_$_HAPMetricsPowerManagementLogEvent._accessoryIdentifier
+ _OBJC_IVAR_$_HAPMetricsPowerManagementLogEvent._logType
+ _OBJC_METACLASS_$_HAPMetricsPowerManagementLogEvent
+ __CopyPairingIdentityDelegateCallback_f.15174
+ __CopyPairingIdentityDelegateCallback_f.21902
+ __CopyPairingIdentityDelegateCallback_f.2816
+ __FindPairedPeerDelegateCallback_f.2815
+ __OBJC_$_INSTANCE_METHODS_HAPKeyBag(AccessoryUtils)
+ __OBJC_$_INSTANCE_METHODS_HAPMetricsPowerManagementLogEvent
+ __OBJC_$_INSTANCE_VARIABLES_HAPMetricsPowerManagementLogEvent
+ __OBJC_$_PROP_LIST_HAP2AccessoryServerBrowser.400
+ __OBJC_$_PROP_LIST_HAP2AccessoryServerPairingDriver.268
+ __OBJC_$_PROP_LIST_HAPMetricsPowerManagementLogEvent
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HMMLogEventSubmitting
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMMLogEventSubmitting
+ __OBJC_$_PROTOCOL_REFS_HMMLogEventSubmitting
+ __OBJC_CLASS_PROTOCOLS_$_HAPMetricsDispatcher
+ __OBJC_CLASS_PROTOCOLS_$_HAPMetricsPowerManagementLogEvent
+ __OBJC_CLASS_RO_$_HAPMetricsPowerManagementLogEvent
+ __OBJC_LABEL_PROTOCOL_$_HMMLogEventSubmitting
+ __OBJC_METACLASS_RO_$_HAPMetricsPowerManagementLogEvent
+ __OBJC_PROTOCOL_$_HMMLogEventSubmitting
+ __PairSetupPromptForSetupCodeDelegateCallback_f.21904
+ __SavePairedPeerDelegateCallback_f.15173
+ __SavePairedPeerDelegateCallback_f.21899
+ ___104-[_HAPAccessoryServerBTLE100 readCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke
+ ___104-[_HAPAccessoryServerBTLE100 readCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.166
+ ___104-[_HAPAccessoryServerBTLE200 readCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke
+ ___104-[_HAPAccessoryServerBTLE200 readCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.381
+ ___104-[_HAPAccessoryServerBTLE200 readCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke_2
+ ___105-[_HAPAccessoryServerBTLE100 writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke
+ ___105-[_HAPAccessoryServerBTLE200 writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke
+ ___105-[_HAPAccessoryServerBTLE200 writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.439
+ ___105-[_HAPAccessoryServerBTLE200 writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.440
+ ___105-[_HAPAccessoryServerBTLE200 writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.441
+ ___107-[HAPAccessoryServerHAP2Adapter readCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke
+ ___108-[HAPAccessoryServerHAP2Adapter writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke
+ ___108-[HAPAccessoryServerIP _performExecuteWriteValues:prepareIdentifier:timeout:expiry:queue:completionHandler:]_block_invoke
+ ___108-[HAPAccessoryServerIP _performExecuteWriteValues:prepareIdentifier:timeout:expiry:queue:completionHandler:]_block_invoke.282
+ ___108-[HAPAccessoryServerIP _performExecuteWriteValues:prepareIdentifier:timeout:expiry:queue:completionHandler:]_block_invoke_2
+ ___108-[HAPAccessoryServerIP _performExecuteWriteValues:prepareIdentifier:timeout:expiry:queue:completionHandler:]_block_invoke_3
+ ___108-[HAPAccessoryServerIP _performExecuteWriteValues:prepareIdentifier:timeout:expiry:queue:completionHandler:]_block_invoke_4
+ ___115-[HAPAccessoryServerIP _handleWriteECONNResetError:writeRequests:responses:timeout:expiry:queue:completionHandler:]_block_invoke
+ ___115-[HAPAccessoryServerIP _handleWriteECONNResetError:writeRequests:responses:timeout:expiry:queue:completionHandler:]_block_invoke.264
+ ___115-[HAPAccessoryServerIP _handleWriteECONNResetError:writeRequests:responses:timeout:expiry:queue:completionHandler:]_block_invoke_2
+ ___120-[HAPAccessoryServerIP _handleReadECONNRESETError:readCharacteristics:responses:timeout:expiry:queue:completionHandler:]_block_invoke
+ ___120-[HAPAccessoryServerIP _handleReadECONNRESETError:readCharacteristics:responses:timeout:expiry:queue:completionHandler:]_block_invoke.208
+ ___120-[HAPAccessoryServerIP _handleReadECONNRESETError:readCharacteristics:responses:timeout:expiry:queue:completionHandler:]_block_invoke_2
+ ___39-[HAP2AccessoryServerController keyBag]_block_invoke
+ ___41-[HAPAccessoryServerIP getAccessoryInfo:]_block_invoke.520
+ ___43-[HAP2AccessoryServerController setKeyBag:]_block_invoke
+ ___47-[HAPAccessoryServerIP identifyWithCompletion:]_block_invoke.649
+ ___49-[HAPAccessoryServerIP authSession:authComplete:]_block_invoke.566
+ ___50-[HAP2AccessoryServerPairingDriver pairingRequest]_block_invoke
+ ___50-[HAPAccessoryServerIP networkMonitorIsReachable:]_block_invoke.515
+ ___52-[HAP2AccessoryServer(Paired) unpairWithCompletion:]_block_invoke.64
+ ___52-[HAP2AccessoryServer(Paired) unpairWithCompletion:]_block_invoke.65
+ ___53-[HAPAccessoryServerHAP2Adapter _printMissingValues:]_block_invoke.230
+ ___53-[HAPAccessoryServerHAP2Adapter _printMissingValues:]_block_invoke.238
+ ___53-[HAPAccessoryServerIP setPairVerifyCompletionBlock:]_block_invoke.421
+ ___54-[HAP2AccessoryServer(Paired) _getSleepIntervalValue:]_block_invoke.252
+ ___54-[HAP2AccessoryServerPairingDriver setPairingRequest:]_block_invoke
+ ___55-[HAPAccessoryServerIP authSession:validateUUID:token:]_block_invoke.556
+ ___55-[HAPAccessoryServerIP authSession:validateUUID:token:]_block_invoke.561
+ ___56-[HAP2AccessoryServer(Paired) removePairing:completion:]_block_invoke.69
+ ___56-[HAP2AccessoryServer(Paired) removePairing:completion:]_block_invoke.70
+ ___57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke.550
+ ___57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke_2.554
+ ___59-[HAP2AccessoryServer(Paired) updateAccessoriesWithReason:]_block_invoke.80
+ ___59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke.478
+ ___59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke_2.479
+ ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.456
+ ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.461
+ ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.462
+ ___60-[HAPAccessoryServerIP _validatePairingAuthMethod:activity:]_block_invoke.534
+ ___64-[HAP2AccessoryServer(Paired) _pollAccessoryOnQueueWithOptions:]_block_invoke.267
+ ___64-[HAP2AccessoryServer(Paired) _pollAccessoryOnQueueWithOptions:]_block_invoke.268
+ ___64-[HAP2AccessoryServer(Paired) _pollAccessoryOnQueueWithOptions:]_block_invoke_2.272
+ ___64-[HAPAccessoryServerIP httpClientDidCloseConnectionDueToServer:]_block_invoke.424
+ ___65-[HAP2AccessoryServer(Unpaired) pairWithDelegate:pairingRequest:]_block_invoke
+ ___65-[HAPAccessoryServerIP _continuePairingAfterAuthPromptWithRetry:]_block_invoke.470
+ ___74-[HAP2AccessoryServerPairingDriver pairAccessory:pairingRequest:delegate:]_block_invoke
+ ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke.605
+ ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke.607
+ ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.606
+ ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.608
+ ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1278
+ ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1279
+ ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1281
+ ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke_2.1280
+ ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke_2.1282
+ ___82-[HAPAccessoryServerHAP2Adapter accessoryServer:doesRequirePermission:completion:]_block_invoke.262
+ ___83-[HAPAccessoryServerIP _performWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke
+ ___83-[HAPAccessoryServerIP _performWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke.265
+ ___83-[HAPAccessoryServerIP _performWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke.273
+ ___83-[HAPAccessoryServerIP _performWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke_2
+ ___83-[HAPAccessoryServerIP _performWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke_2.274
+ ___83-[HAPAccessoryServerIP _performWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke_3
+ ___83-[HAPAccessoryServerIP _performWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke_4
+ ___85-[HAPAccessoryServerIP _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.342
+ ___88-[HAPAccessoryServerIP _performTimedWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke
+ ___88-[HAPAccessoryServerIP _performTimedWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke.275
+ ___88-[HAPAccessoryServerIP _performTimedWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke.276
+ ___88-[HAPAccessoryServerIP _performTimedWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke_2
+ ___88-[HAPAccessoryServerIP _performTimedWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke_2.277
+ ___88-[HAPAccessoryServerIP _performTimedWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke_3
+ ___88-[HAPAccessoryServerIP _performTimedWriteValues:timeout:expiry:queue:completionHandler:]_block_invoke_4
+ ___88-[HAPAccessoryServerIP _startAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.580
+ ___89-[HAPAccessoryServerIP _queuedReadOperationBlock:timeout:expiry:queue:completionHandler:]_block_invoke
+ ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke
+ ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.209
+ ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.214
+ ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.223
+ ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.233
+ ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke_2
+ ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke_2.234
+ ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke_3
+ ___89-[HAPAccessoryServerIP _readCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke_4
+ ___90-[HAPAccessory readCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke
+ ___90-[HAPAccessory readCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.115
+ ___90-[HAPAccessory readCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.116
+ ___90-[HAPAccessory readCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.117
+ ___90-[HAPAccessory writeCharacteristicValue:timeout:expiry:completionQueue:completionHandler:]_block_invoke
+ ___90-[HAPAccessory writeCharacteristicValue:timeout:expiry:completionQueue:completionHandler:]_block_invoke.121
+ ___90-[HAPAccessory writeCharacteristicValue:timeout:expiry:completionQueue:completionHandler:]_block_invoke.122
+ ___90-[HAPAccessory writeCharacteristicValue:timeout:expiry:completionQueue:completionHandler:]_block_invoke.123
+ ___90-[HAPAccessory writeCharacteristicValue:timeout:expiry:completionQueue:completionHandler:]_block_invoke_2
+ ___90-[HAPAccessoryServerIP _queuedWriteOperationBlock:timeout:expiry:queue:completionHandler:]_block_invoke
+ ___90-[HAPAccessoryServerIP _writeCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke
+ ___90-[HAPAccessoryServerIP _writeCharacteristicValues:timeout:expiry:queue:completionHandler:]_block_invoke.253
+ ___91-[HAPAccessory writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke
+ ___91-[HAPAccessory writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.133
+ ___91-[HAPAccessory writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.134
+ ___91-[HAPAccessory writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.135
+ ___92-[HAPAccessory readValueForCharacteristic:timeout:expiry:completionQueue:completionHandler:]_block_invoke
+ ___92-[HAPAccessory readValueForCharacteristic:timeout:expiry:completionQueue:completionHandler:]_block_invoke.90
+ ___92-[HAPAccessory readValueForCharacteristic:timeout:expiry:completionQueue:completionHandler:]_block_invoke.94
+ ___92-[HAPAccessory readValueForCharacteristic:timeout:expiry:completionQueue:completionHandler:]_block_invoke.98
+ ___92-[HAPAccessory readValueForCharacteristic:timeout:expiry:completionQueue:completionHandler:]_block_invoke_2
+ ___93-[HAPAccessoryServerHAP2Adapter enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.189
+ ___94-[HAPAccessoryServerHAP2Adapter _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.197
+ ___94-[HAPAccessoryServerHAP2Adapter _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke_2.198
+ ___97-[HAP2AccessoryServer(Paired) _readValuesForCharacteristics:timeout:options:activity:completion:]_block_invoke.239
+ ___97-[HAP2AccessoryServer(Paired) _readValuesForCharacteristics:timeout:options:activity:completion:]_block_invoke_2.240
+ ___97-[HAP2AccessoryServer(Paired) _readValuesForCharacteristics:timeout:options:activity:completion:]_block_invoke_3.241
+ ___98-[HAPAccessoryServerIP readCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke
+ ___98-[HAPAccessoryServerIP readCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke_2
+ ___98-[HAPAccessoryServerIP readCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke_3
+ ___99-[HAPAccessoryServerIP writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke
+ ___99-[HAPAccessoryServerIP writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.252
+ ___Block_byref_object_copy_.10638
+ ___Block_byref_object_copy_.10935
+ ___Block_byref_object_copy_.11754
+ ___Block_byref_object_copy_.11951
+ ___Block_byref_object_copy_.13018
+ ___Block_byref_object_copy_.13829
+ ___Block_byref_object_copy_.14057
+ ___Block_byref_object_copy_.15084
+ ___Block_byref_object_copy_.17208
+ ___Block_byref_object_copy_.17426
+ ___Block_byref_object_copy_.18413
+ ___Block_byref_object_copy_.19029
+ ___Block_byref_object_copy_.20127
+ ___Block_byref_object_copy_.20934
+ ___Block_byref_object_copy_.2101
+ ___Block_byref_object_copy_.25039
+ ___Block_byref_object_copy_.25205
+ ___Block_byref_object_copy_.2764
+ ___Block_byref_object_copy_.382
+ ___Block_byref_object_copy_.4333
+ ___Block_byref_object_copy_.5206
+ ___Block_byref_object_copy_.5471
+ ___Block_byref_object_copy_.5923
+ ___Block_byref_object_copy_.6551
+ ___Block_byref_object_copy_.6734
+ ___Block_byref_object_copy_.750
+ ___Block_byref_object_copy_.7545
+ ___Block_byref_object_copy_.9049
+ ___Block_byref_object_copy_.9371
+ ___Block_byref_object_copy_.9575
+ ___Block_byref_object_dispose_.10639
+ ___Block_byref_object_dispose_.10936
+ ___Block_byref_object_dispose_.11755
+ ___Block_byref_object_dispose_.11952
+ ___Block_byref_object_dispose_.13019
+ ___Block_byref_object_dispose_.13830
+ ___Block_byref_object_dispose_.14058
+ ___Block_byref_object_dispose_.15085
+ ___Block_byref_object_dispose_.17209
+ ___Block_byref_object_dispose_.17427
+ ___Block_byref_object_dispose_.18414
+ ___Block_byref_object_dispose_.19030
+ ___Block_byref_object_dispose_.20128
+ ___Block_byref_object_dispose_.20935
+ ___Block_byref_object_dispose_.2102
+ ___Block_byref_object_dispose_.25040
+ ___Block_byref_object_dispose_.25206
+ ___Block_byref_object_dispose_.2765
+ ___Block_byref_object_dispose_.383
+ ___Block_byref_object_dispose_.4334
+ ___Block_byref_object_dispose_.5207
+ ___Block_byref_object_dispose_.5472
+ ___Block_byref_object_dispose_.5924
+ ___Block_byref_object_dispose_.6552
+ ___Block_byref_object_dispose_.6735
+ ___Block_byref_object_dispose_.751
+ ___Block_byref_object_dispose_.7546
+ ___Block_byref_object_dispose_.9050
+ ___Block_byref_object_dispose_.9372
+ ___Block_byref_object_dispose_.9576
+ ___block_descriptor_104_e8_32s40s48s56s64bs72bs80w88w_e5_v8?0lw80l8w88l8s32l8s40l8s48l8s64l8s56l8s72l8
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80bs88bs_e5_v8?0ls32l8s40l8s48l8s56l8s80l8s64l8s72l8s88l8
+ ___block_descriptor_112_e8_32s40s48s56s64s72bs80bs88w96w_e5_v8?0lw88l8w96l8s32l8s40l8s48l8s72l8s56l8s64l8s80l8
+ ___block_descriptor_112_e8_32s40s48s56s64s72s80bs88bs96w_e5_v8?0lw96l8s32l8s40l8s48l8s56l8s80l8s64l8s72l8s88l8
+ ___block_descriptor_56_e8_32s40r48r_e40_v24?0"HAPPairingIdentity"8"NSError"16lr40l8r48l8s32l8
+ ___block_descriptor_64_e8_32s40s48s56s_e23_"<HAP2Cancelable>"8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56bs64w_e17_v16?0"NSError"8lw64l8s32l8s40l8s56l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56bs64w_e26_v36?08Q16i24"NSError"28lw64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56bs64w_e29_v24?0"NSArray"8"NSError"16lw64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_96_e8_32s40s48s56s64bs72w80w_e26_v36?08Q16i24"NSError"28lw72l8w80l8s32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.10307
+ ___block_literal_global.10990
+ ___block_literal_global.11750
+ ___block_literal_global.12123
+ ___block_literal_global.1298
+ ___block_literal_global.13288
+ ___block_literal_global.1335
+ ___block_literal_global.15198
+ ___block_literal_global.15627
+ ___block_literal_global.16934
+ ___block_literal_global.17217
+ ___block_literal_global.18602
+ ___block_literal_global.19871
+ ___block_literal_global.2006
+ ___block_literal_global.20149
+ ___block_literal_global.20601
+ ___block_literal_global.21559
+ ___block_literal_global.219
+ ___block_literal_global.223
+ ___block_literal_global.226
+ ___block_literal_global.22889
+ ___block_literal_global.23224
+ ___block_literal_global.244
+ ___block_literal_global.24812
+ ___block_literal_global.25425
+ ___block_literal_global.2834
+ ___block_literal_global.3780
+ ___block_literal_global.5293
+ ___block_literal_global.5467
+ ___block_literal_global.6020
+ ___block_literal_global.6563
+ ___block_literal_global.6709
+ ___block_literal_global.7815
+ ___block_literal_global.813
+ ___block_literal_global.8717
+ ___block_literal_global.9140
+ ___block_literal_global.9690
+ _hkConfig.21543
+ _logCategory._hmf_once_t426
+ _logCategory._hmf_once_t55
+ _logCategory._hmf_once_v427
+ _logCategory._hmf_once_v56
+ _objc_msgSend$_handlePrepareWriteResponseObject:type:prepareIdentifier:httpStatus:error:requestTuples:timeout:expiry:queue:originalCompletion:completion:
+ _objc_msgSend$_handleReadECONNRESETError:readCharacteristics:responses:timeout:expiry:queue:completionHandler:
+ _objc_msgSend$_handleWriteECONNResetError:writeRequests:responses:timeout:expiry:queue:completionHandler:
+ _objc_msgSend$_insertReadCharacteristicValues:timeout:expiry:queue:completionHandler:
+ _objc_msgSend$_insertWriteCharacteristicValues:timeout:expiry:queue:withCompletionHandler:
+ _objc_msgSend$_performExecuteWriteValues:prepareIdentifier:timeout:expiry:queue:completionHandler:
+ _objc_msgSend$_performTimedWriteValues:timeout:expiry:queue:completionHandler:
+ _objc_msgSend$_performWriteValues:timeout:expiry:queue:completionHandler:
+ _objc_msgSend$_queueReadCharacteristicValues:timeout:expiry:queue:completionHandler:
+ _objc_msgSend$_queueWriteCharacteristicValues:timeout:expiry:queue:withCompletionHandler:
+ _objc_msgSend$_queuedReadOperationBlock:timeout:expiry:queue:completionHandler:
+ _objc_msgSend$_queuedWriteOperationBlock:timeout:expiry:queue:completionHandler:
+ _objc_msgSend$_readCharacteristicValues:timeout:expiry:queue:completionHandler:
+ _objc_msgSend$_writeCharacteristicValues:timeout:expiry:queue:completionHandler:
+ _objc_msgSend$associateControllerIdentifier:error:
+ _objc_msgSend$currentLocalPairingIdentity
+ _objc_msgSend$initForHAPAccessory:withLogType:
+ _objc_msgSend$initForSuspendedAccessory:
+ _objc_msgSend$initWithQualityOfService:delegate:dateProvider:
+ _objc_msgSend$keyBagForIdentifier:
+ _objc_msgSend$logType
+ _objc_msgSend$now
+ _objc_msgSend$pairAccessory:pairingRequest:delegate:
+ _objc_msgSend$pairWithDelegate:pairingRequest:
+ _objc_msgSend$readCharacteristicValues:timeout:expiry:completionQueue:completionHandler:
+ _objc_msgSend$readValueForCharacteristic:timeout:expiry:completionQueue:completionHandler:
+ _objc_msgSend$remainingTTLForExpiry:
+ _objc_msgSend$submitLogEvent:error:
+ _objc_msgSend$writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:
+ _sharedInstance.onceToken.15626
- -[HAP2AccessoryServer(Unpaired) pairWithDelegate:]
- -[HAP2AccessoryServerPairingDriver pairAccessory:delegate:]
- -[HAPAccessory readCharacteristicValues:timeout:completionQueue:completionHandler:]
- -[HAPAccessory readValueForCharacteristic:timeout:completionQueue:completionHandler:]
- -[HAPAccessory writeCharacteristicValue:timeout:completionQueue:completionHandler:]
- -[HAPAccessory writeCharacteristicValues:timeout:completionQueue:completionHandler:]
- -[HAPAccessoryServer readCharacteristicValues:timeout:completionQueue:completionHandler:]
- -[HAPAccessoryServer writeCharacteristicValues:timeout:completionQueue:completionHandler:]
- -[HAPAccessoryServerHAP2Adapter currentIdentity]
- -[HAPAccessoryServerHAP2Adapter readCharacteristicValues:timeout:completionQueue:completionHandler:]
- -[HAPAccessoryServerHAP2Adapter writeCharacteristicValues:timeout:completionQueue:completionHandler:]
- -[HAPAccessoryServerIP _handlePrepareWriteResponseObject:type:prepareIdentifier:httpStatus:error:requestTuples:timeout:queue:originalCompletion:completion:]
- -[HAPAccessoryServerIP _handleReadECONNRESETError:readCharacteristics:responses:timeout:queue:completionHandler:]
- -[HAPAccessoryServerIP _handleWriteECONNResetError:writeRequests:responses:timeout:queue:completionHandler:]
- -[HAPAccessoryServerIP _insertReadCharacteristicValues:timeout:queue:completionHandler:]
- -[HAPAccessoryServerIP _insertWriteCharacteristicValues:timeout:queue:withCompletionHandler:]
- -[HAPAccessoryServerIP _performExecuteWriteValues:prepareIdentifier:timeout:queue:completionHandler:]
- -[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]
- -[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]
- -[HAPAccessoryServerIP _queueReadCharacteristicValues:timeout:queue:completionHandler:]
- -[HAPAccessoryServerIP _queueWriteCharacteristicValues:timeout:queue:withCompletionHandler:]
- -[HAPAccessoryServerIP _queuedReadOperationBlock:timeout:queue:completionHandler:]
- -[HAPAccessoryServerIP _queuedWriteOperationBlock:timeout:queue:completionHandler:]
- -[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]
- -[HAPAccessoryServerIP _writeCharacteristicValues:timeout:queue:completionHandler:]
- -[HAPAccessoryServerIP readCharacteristicValues:timeout:completionQueue:completionHandler:]
- -[HAPAccessoryServerIP writeCharacteristicValues:timeout:completionQueue:completionHandler:]
- -[_HAPAccessoryServerBTLE100 readCharacteristicValues:timeout:completionQueue:completionHandler:]
- -[_HAPAccessoryServerBTLE100 writeCharacteristicValues:timeout:completionQueue:completionHandler:]
- -[_HAPAccessoryServerBTLE200 readCharacteristicValues:timeout:completionQueue:completionHandler:]
- -[_HAPAccessoryServerBTLE200 writeCharacteristicValues:timeout:completionQueue:completionHandler:]
- GCC_except_table1042
- GCC_except_table1046
- GCC_except_table1059
- GCC_except_table1064
- GCC_except_table1073
- GCC_except_table1075
- GCC_except_table1077
- GCC_except_table1079
- GCC_except_table1205
- GCC_except_table1209
- GCC_except_table1211
- GCC_except_table1423
- GCC_except_table1629
- GCC_except_table1632
- GCC_except_table1640
- GCC_except_table1642
- GCC_except_table1648
- GCC_except_table1650
- GCC_except_table1654
- GCC_except_table1658
- GCC_except_table1660
- GCC_except_table1669
- GCC_except_table1679
- GCC_except_table1687
- GCC_except_table1698
- GCC_except_table1702
- GCC_except_table1706
- GCC_except_table1708
- GCC_except_table1857
- GCC_except_table1861
- GCC_except_table1862
- GCC_except_table1866
- GCC_except_table1875
- GCC_except_table1877
- GCC_except_table1881
- GCC_except_table1886
- GCC_except_table1889
- GCC_except_table1906
- GCC_except_table1909
- GCC_except_table1911
- GCC_except_table1917
- GCC_except_table1926
- GCC_except_table1929
- GCC_except_table1932
- GCC_except_table1934
- GCC_except_table1940
- GCC_except_table1944
- GCC_except_table1952
- GCC_except_table1963
- GCC_except_table198
- GCC_except_table2001
- GCC_except_table2007
- GCC_except_table205
- GCC_except_table208
- GCC_except_table211
- GCC_except_table214
- GCC_except_table216
- GCC_except_table2178
- GCC_except_table218
- GCC_except_table2191
- GCC_except_table2197
- GCC_except_table2200
- GCC_except_table2203
- GCC_except_table2206
- GCC_except_table2212
- GCC_except_table2214
- GCC_except_table2218
- GCC_except_table222
- GCC_except_table224
- GCC_except_table2317
- GCC_except_table2325
- GCC_except_table2326
- GCC_except_table2327
- GCC_except_table2328
- GCC_except_table2329
- GCC_except_table233
- GCC_except_table2330
- GCC_except_table2345
- GCC_except_table2359
- GCC_except_table237
- GCC_except_table2439
- GCC_except_table2451
- GCC_except_table2477
- GCC_except_table2485
- GCC_except_table2496
- GCC_except_table2510
- GCC_except_table2513
- GCC_except_table2518
- GCC_except_table2526
- GCC_except_table2532
- GCC_except_table2534
- GCC_except_table2708
- GCC_except_table2758
- GCC_except_table2774
- GCC_except_table2777
- GCC_except_table2791
- GCC_except_table2792
- GCC_except_table2814
- GCC_except_table2826
- GCC_except_table2827
- GCC_except_table2829
- GCC_except_table2835
- GCC_except_table2845
- GCC_except_table2850
- GCC_except_table2906
- GCC_except_table2909
- GCC_except_table2914
- GCC_except_table2930
- GCC_except_table2944
- GCC_except_table2946
- GCC_except_table2950
- GCC_except_table2958
- GCC_except_table2966
- GCC_except_table3015
- GCC_except_table3023
- GCC_except_table3025
- GCC_except_table3026
- GCC_except_table3049
- GCC_except_table3293
- GCC_except_table3357
- GCC_except_table3358
- GCC_except_table3362
- GCC_except_table3367
- GCC_except_table3368
- GCC_except_table3370
- GCC_except_table3371
- GCC_except_table3373
- GCC_except_table3390
- GCC_except_table3393
- GCC_except_table3404
- GCC_except_table3405
- GCC_except_table3407
- GCC_except_table3409
- GCC_except_table3415
- GCC_except_table3417
- GCC_except_table3420
- GCC_except_table3423
- GCC_except_table3435
- GCC_except_table3437
- GCC_except_table3441
- GCC_except_table3445
- GCC_except_table3449
- GCC_except_table3475
- GCC_except_table3493
- GCC_except_table3497
- GCC_except_table3502
- GCC_except_table3579
- GCC_except_table3580
- GCC_except_table3581
- GCC_except_table3582
- GCC_except_table3583
- GCC_except_table3584
- GCC_except_table3585
- GCC_except_table3629
- GCC_except_table3655
- GCC_except_table3746
- GCC_except_table3771
- GCC_except_table3775
- GCC_except_table3781
- GCC_except_table3784
- GCC_except_table3787
- GCC_except_table3790
- GCC_except_table3793
- GCC_except_table3796
- GCC_except_table3799
- GCC_except_table3804
- GCC_except_table3815
- GCC_except_table3818
- GCC_except_table3829
- GCC_except_table3837
- GCC_except_table3841
- GCC_except_table3848
- GCC_except_table3849
- GCC_except_table3853
- GCC_except_table3872
- GCC_except_table3874
- GCC_except_table3876
- GCC_except_table3877
- GCC_except_table3889
- GCC_except_table3891
- GCC_except_table3899
- GCC_except_table3902
- GCC_except_table3914
- GCC_except_table3925
- GCC_except_table3927
- GCC_except_table3936
- GCC_except_table404
- GCC_except_table420
- GCC_except_table4202
- GCC_except_table4225
- GCC_except_table4229
- GCC_except_table4246
- GCC_except_table4265
- GCC_except_table4279
- GCC_except_table428
- GCC_except_table4283
- GCC_except_table4396
- GCC_except_table4476
- GCC_except_table4484
- GCC_except_table4494
- GCC_except_table4531
- GCC_except_table4534
- GCC_except_table4535
- GCC_except_table4536
- GCC_except_table458
- GCC_except_table4635
- GCC_except_table4636
- GCC_except_table4637
- GCC_except_table4638
- GCC_except_table4639
- GCC_except_table4640
- GCC_except_table4647
- GCC_except_table4649
- GCC_except_table4656
- GCC_except_table4659
- GCC_except_table466
- GCC_except_table4661
- GCC_except_table4666
- GCC_except_table4669
- GCC_except_table4676
- GCC_except_table4680
- GCC_except_table4709
- GCC_except_table4710
- GCC_except_table4729
- GCC_except_table4739
- GCC_except_table4742
- GCC_except_table4747
- GCC_except_table4750
- GCC_except_table480
- GCC_except_table483
- GCC_except_table486
- GCC_except_table489
- GCC_except_table501
- GCC_except_table5014
- GCC_except_table5018
- GCC_except_table505
- GCC_except_table5052
- GCC_except_table5056
- GCC_except_table5060
- GCC_except_table508
- GCC_except_table515
- GCC_except_table521
- GCC_except_table5217
- GCC_except_table5223
- GCC_except_table5227
- GCC_except_table5228
- GCC_except_table5229
- GCC_except_table5230
- GCC_except_table5236
- GCC_except_table5270
- GCC_except_table5271
- GCC_except_table5272
- GCC_except_table5292
- GCC_except_table5304
- GCC_except_table5312
- GCC_except_table5314
- GCC_except_table5328
- GCC_except_table546
- GCC_except_table5530
- GCC_except_table5542
- GCC_except_table5547
- GCC_except_table5550
- GCC_except_table5551
- GCC_except_table5553
- GCC_except_table5554
- GCC_except_table5556
- GCC_except_table556
- GCC_except_table5586
- GCC_except_table5608
- GCC_except_table5612
- GCC_except_table5616
- GCC_except_table5621
- GCC_except_table5625
- GCC_except_table5629
- GCC_except_table563
- GCC_except_table5633
- GCC_except_table5637
- GCC_except_table5645
- GCC_except_table5647
- GCC_except_table5649
- GCC_except_table5709
- GCC_except_table5710
- GCC_except_table5711
- GCC_except_table5712
- GCC_except_table5713
- GCC_except_table5772
- GCC_except_table5773
- GCC_except_table5793
- GCC_except_table5806
- GCC_except_table5809
- GCC_except_table5815
- GCC_except_table5818
- GCC_except_table5825
- GCC_except_table5828
- GCC_except_table5849
- GCC_except_table5855
- GCC_except_table5864
- GCC_except_table5870
- GCC_except_table5871
- GCC_except_table5886
- GCC_except_table5896
- GCC_except_table590
- GCC_except_table5911
- GCC_except_table5912
- GCC_except_table5917
- GCC_except_table5921
- GCC_except_table5922
- GCC_except_table5925
- GCC_except_table5935
- GCC_except_table5937
- GCC_except_table5939
- GCC_except_table594
- GCC_except_table5943
- GCC_except_table596
- GCC_except_table604
- GCC_except_table6090
- GCC_except_table6146
- GCC_except_table6149
- GCC_except_table6153
- GCC_except_table6159
- GCC_except_table6166
- GCC_except_table6167
- GCC_except_table618
- GCC_except_table6183
- GCC_except_table6187
- GCC_except_table6188
- GCC_except_table6189
- GCC_except_table622
- GCC_except_table6237
- GCC_except_table6238
- GCC_except_table6240
- GCC_except_table6243
- GCC_except_table626
- GCC_except_table6272
- GCC_except_table6277
- GCC_except_table6297
- GCC_except_table6314
- GCC_except_table6315
- GCC_except_table6316
- GCC_except_table6324
- GCC_except_table6329
- GCC_except_table6330
- GCC_except_table6331
- GCC_except_table6345
- GCC_except_table6348
- GCC_except_table635
- GCC_except_table6354
- GCC_except_table636
- GCC_except_table6360
- GCC_except_table6372
- GCC_except_table6378
- GCC_except_table6387
- GCC_except_table6393
- GCC_except_table6394
- GCC_except_table6398
- GCC_except_table641
- GCC_except_table6410
- GCC_except_table6412
- GCC_except_table6416
- GCC_except_table6437
- GCC_except_table6439
- GCC_except_table644
- GCC_except_table6466
- GCC_except_table647
- GCC_except_table652
- GCC_except_table662
- GCC_except_table663
- GCC_except_table6630
- GCC_except_table668
- GCC_except_table669
- GCC_except_table6693
- GCC_except_table6725
- GCC_except_table6728
- GCC_except_table6892
- GCC_except_table695
- GCC_except_table6955
- GCC_except_table7019
- GCC_except_table702
- GCC_except_table7025
- GCC_except_table7071
- GCC_except_table7073
- GCC_except_table7075
- GCC_except_table7077
- GCC_except_table7079
- GCC_except_table7081
- GCC_except_table7083
- GCC_except_table7085
- GCC_except_table7087
- GCC_except_table7089
- GCC_except_table709
- GCC_except_table7091
- GCC_except_table7094
- GCC_except_table7096
- GCC_except_table7098
- GCC_except_table710
- GCC_except_table7127
- GCC_except_table7130
- GCC_except_table7131
- GCC_except_table7170
- GCC_except_table7171
- GCC_except_table7172
- GCC_except_table7174
- GCC_except_table7175
- GCC_except_table7177
- GCC_except_table7178
- GCC_except_table7179
- GCC_except_table7181
- GCC_except_table7182
- GCC_except_table7184
- GCC_except_table7188
- GCC_except_table7189
- GCC_except_table7193
- GCC_except_table7241
- GCC_except_table7248
- GCC_except_table7342
- GCC_except_table7358
- GCC_except_table7360
- GCC_except_table7362
- GCC_except_table7365
- GCC_except_table7367
- GCC_except_table7369
- GCC_except_table7371
- GCC_except_table7372
- GCC_except_table7374
- GCC_except_table7378
- GCC_except_table7383
- GCC_except_table744
- GCC_except_table767
- GCC_except_table785
- GCC_except_table809
- GCC_except_table813
- GCC_except_table827
- GCC_except_table934
- GCC_except_table936
- __CopyPairingIdentityDelegateCallback_f.15065
- __CopyPairingIdentityDelegateCallback_f.21655
- __CopyPairingIdentityDelegateCallback_f.2732
- __FindPairedPeerDelegateCallback_f.2731
- __OBJC_$_INSTANCE_METHODS_HAPKeyBag
- __OBJC_$_PROP_LIST_HAP2AccessoryServerBrowser.406
- __OBJC_$_PROP_LIST_HAP2AccessoryServerDelegate
- __PairSetupPromptForSetupCodeDelegateCallback_f.21657
- __SavePairedPeerDelegateCallback_f.15063
- __SavePairedPeerDelegateCallback_f.21652
- ___100-[HAPAccessoryServerHAP2Adapter readCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke
- ___101-[HAPAccessoryServerHAP2Adapter writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke
- ___101-[HAPAccessoryServerIP _performExecuteWriteValues:prepareIdentifier:timeout:queue:completionHandler:]_block_invoke
- ___101-[HAPAccessoryServerIP _performExecuteWriteValues:prepareIdentifier:timeout:queue:completionHandler:]_block_invoke_2
- ___101-[HAPAccessoryServerIP _performExecuteWriteValues:prepareIdentifier:timeout:queue:completionHandler:]_block_invoke_3
- ___101-[HAPAccessoryServerIP _performExecuteWriteValues:prepareIdentifier:timeout:queue:completionHandler:]_block_invoke_4
- ___108-[HAPAccessoryServerIP _handleWriteECONNResetError:writeRequests:responses:timeout:queue:completionHandler:]_block_invoke
- ___108-[HAPAccessoryServerIP _handleWriteECONNResetError:writeRequests:responses:timeout:queue:completionHandler:]_block_invoke.261
- ___113-[HAPAccessoryServerIP _handleReadECONNRESETError:readCharacteristics:responses:timeout:queue:completionHandler:]_block_invoke
- ___113-[HAPAccessoryServerIP _handleReadECONNRESETError:readCharacteristics:responses:timeout:queue:completionHandler:]_block_invoke.208
- ___41-[HAPAccessoryServerIP getAccessoryInfo:]_block_invoke.516
- ___47-[HAPAccessoryServerIP identifyWithCompletion:]_block_invoke.645
- ___49-[HAPAccessoryServerIP authSession:authComplete:]_block_invoke.562
- ___50-[HAP2AccessoryServer(Unpaired) pairWithDelegate:]_block_invoke
- ___50-[HAPAccessoryServerIP networkMonitorIsReachable:]_block_invoke.511
- ___52-[HAP2AccessoryServer(Paired) unpairWithCompletion:]_block_invoke.77
- ___52-[HAP2AccessoryServer(Paired) unpairWithCompletion:]_block_invoke.78
- ___53-[HAPAccessoryServerHAP2Adapter _printMissingValues:]_block_invoke.229
- ___53-[HAPAccessoryServerHAP2Adapter _printMissingValues:]_block_invoke.237
- ___53-[HAPAccessoryServerIP setPairVerifyCompletionBlock:]_block_invoke.417
- ___54-[HAP2AccessoryServer(Paired) _getSleepIntervalValue:]_block_invoke.265
- ___55-[HAPAccessoryServerIP authSession:validateUUID:token:]_block_invoke.552
- ___55-[HAPAccessoryServerIP authSession:validateUUID:token:]_block_invoke.557
- ___56-[HAP2AccessoryServer(Paired) removePairing:completion:]_block_invoke.82
- ___56-[HAP2AccessoryServer(Paired) removePairing:completion:]_block_invoke.83
- ___57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke.546
- ___57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke_2.550
- ___59-[HAP2AccessoryServer(Paired) updateAccessoriesWithReason:]_block_invoke.93
- ___59-[HAP2AccessoryServerPairingDriver pairAccessory:delegate:]_block_invoke
- ___59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke.474
- ___59-[HAPAccessoryServerIP _handlePairSetupCompletionWithData:]_block_invoke_2.475
- ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.452
- ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.457
- ___59-[HAPAccessoryServerIP _pairSetupStartWithConsentRequired:]_block_invoke.458
- ___60-[HAPAccessoryServerIP _validatePairingAuthMethod:activity:]_block_invoke.530
- ___64-[HAP2AccessoryServer(Paired) _pollAccessoryOnQueueWithOptions:]_block_invoke.280
- ___64-[HAP2AccessoryServer(Paired) _pollAccessoryOnQueueWithOptions:]_block_invoke.281
- ___64-[HAP2AccessoryServer(Paired) _pollAccessoryOnQueueWithOptions:]_block_invoke_2.285
- ___64-[HAPAccessoryServerIP httpClientDidCloseConnectionDueToServer:]_block_invoke.420
- ___65-[HAPAccessoryServerIP _continuePairingAfterAuthPromptWithRetry:]_block_invoke.466
- ___76-[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]_block_invoke
- ___76-[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]_block_invoke.262
- ___76-[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]_block_invoke.270
- ___76-[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]_block_invoke_2
- ___76-[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]_block_invoke_2.271
- ___76-[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]_block_invoke_3
- ___76-[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]_block_invoke_4
- ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke.601
- ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke.603
- ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.602
- ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.604
- ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1273
- ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1274
- ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1276
- ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke_2.1275
- ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke_2.1277
- ___81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke
- ___81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke.272
- ___81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke.273
- ___81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke_2
- ___81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke_2.274
- ___81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke_3
- ___81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke_4
- ___82-[HAPAccessoryServerHAP2Adapter accessoryServer:doesRequirePermission:completion:]_block_invoke.261
- ___82-[HAPAccessoryServerIP _queuedReadOperationBlock:timeout:queue:completionHandler:]_block_invoke
- ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke
- ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.209
- ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.214
- ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.223
- ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.230
- ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke_2
- ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke_2.231
- ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke_3
- ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke_4
- ___83-[HAPAccessory readCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke
- ___83-[HAPAccessory readCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.111
- ___83-[HAPAccessory readCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.112
- ___83-[HAPAccessory writeCharacteristicValue:timeout:completionQueue:completionHandler:]_block_invoke
- ___83-[HAPAccessory writeCharacteristicValue:timeout:completionQueue:completionHandler:]_block_invoke.116
- ___83-[HAPAccessory writeCharacteristicValue:timeout:completionQueue:completionHandler:]_block_invoke.117
- ___83-[HAPAccessory writeCharacteristicValue:timeout:completionQueue:completionHandler:]_block_invoke_2
- ___83-[HAPAccessoryServerIP _queuedWriteOperationBlock:timeout:queue:completionHandler:]_block_invoke
- ___83-[HAPAccessoryServerIP _writeCharacteristicValues:timeout:queue:completionHandler:]_block_invoke
- ___83-[HAPAccessoryServerIP _writeCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.250
- ___84-[HAPAccessory writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke
- ___84-[HAPAccessory writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.127
- ___84-[HAPAccessory writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.128
- ___85-[HAPAccessory readValueForCharacteristic:timeout:completionQueue:completionHandler:]_block_invoke
- ___85-[HAPAccessory readValueForCharacteristic:timeout:completionQueue:completionHandler:]_block_invoke.90
- ___85-[HAPAccessory readValueForCharacteristic:timeout:completionQueue:completionHandler:]_block_invoke.94
- ___85-[HAPAccessory readValueForCharacteristic:timeout:completionQueue:completionHandler:]_block_invoke_2
- ___85-[HAPAccessoryServerIP _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.334
- ___88-[HAPAccessoryServerIP _startAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.576
- ___91-[HAPAccessoryServerIP readCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke
- ___91-[HAPAccessoryServerIP readCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke_2
- ___91-[HAPAccessoryServerIP readCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke_3
- ___92-[HAPAccessoryServerIP writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke
- ___92-[HAPAccessoryServerIP writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.249
- ___93-[HAPAccessoryServerHAP2Adapter enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.188
- ___94-[HAPAccessoryServerHAP2Adapter _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.196
- ___94-[HAPAccessoryServerHAP2Adapter _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke_2.197
- ___97-[HAP2AccessoryServer(Paired) _readValuesForCharacteristics:timeout:options:activity:completion:]_block_invoke.252
- ___97-[HAP2AccessoryServer(Paired) _readValuesForCharacteristics:timeout:options:activity:completion:]_block_invoke_2.253
- ___97-[HAP2AccessoryServer(Paired) _readValuesForCharacteristics:timeout:options:activity:completion:]_block_invoke_3.254
- ___97-[_HAPAccessoryServerBTLE100 readCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke
- ___97-[_HAPAccessoryServerBTLE100 readCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.166
- ___97-[_HAPAccessoryServerBTLE200 readCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke
- ___97-[_HAPAccessoryServerBTLE200 readCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.381
- ___97-[_HAPAccessoryServerBTLE200 readCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke_2
- ___98-[_HAPAccessoryServerBTLE100 writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke
- ___98-[_HAPAccessoryServerBTLE200 writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke
- ___98-[_HAPAccessoryServerBTLE200 writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.439
- ___98-[_HAPAccessoryServerBTLE200 writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.440
- ___98-[_HAPAccessoryServerBTLE200 writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.441
- ___Block_byref_object_copy_.10528
- ___Block_byref_object_copy_.10816
- ___Block_byref_object_copy_.11652
- ___Block_byref_object_copy_.11849
- ___Block_byref_object_copy_.12910
- ___Block_byref_object_copy_.13712
- ___Block_byref_object_copy_.13940
- ___Block_byref_object_copy_.14974
- ___Block_byref_object_copy_.16985
- ___Block_byref_object_copy_.17200
- ___Block_byref_object_copy_.18189
- ___Block_byref_object_copy_.18792
- ___Block_byref_object_copy_.19881
- ___Block_byref_object_copy_.2020
- ___Block_byref_object_copy_.20686
- ___Block_byref_object_copy_.24811
- ___Block_byref_object_copy_.24977
- ___Block_byref_object_copy_.2680
- ___Block_byref_object_copy_.336
- ___Block_byref_object_copy_.4239
- ___Block_byref_object_copy_.5106
- ___Block_byref_object_copy_.5370
- ___Block_byref_object_copy_.5821
- ___Block_byref_object_copy_.6456
- ___Block_byref_object_copy_.6636
- ___Block_byref_object_copy_.690
- ___Block_byref_object_copy_.7429
- ___Block_byref_object_copy_.8948
- ___Block_byref_object_copy_.9265
- ___Block_byref_object_copy_.9469
- ___Block_byref_object_dispose_.10529
- ___Block_byref_object_dispose_.10817
- ___Block_byref_object_dispose_.11653
- ___Block_byref_object_dispose_.11850
- ___Block_byref_object_dispose_.12911
- ___Block_byref_object_dispose_.13713
- ___Block_byref_object_dispose_.13941
- ___Block_byref_object_dispose_.14975
- ___Block_byref_object_dispose_.16986
- ___Block_byref_object_dispose_.17201
- ___Block_byref_object_dispose_.18190
- ___Block_byref_object_dispose_.18793
- ___Block_byref_object_dispose_.19882
- ___Block_byref_object_dispose_.2021
- ___Block_byref_object_dispose_.20687
- ___Block_byref_object_dispose_.24812
- ___Block_byref_object_dispose_.24978
- ___Block_byref_object_dispose_.2681
- ___Block_byref_object_dispose_.337
- ___Block_byref_object_dispose_.4240
- ___Block_byref_object_dispose_.5107
- ___Block_byref_object_dispose_.5371
- ___Block_byref_object_dispose_.5822
- ___Block_byref_object_dispose_.6457
- ___Block_byref_object_dispose_.6637
- ___Block_byref_object_dispose_.691
- ___Block_byref_object_dispose_.7430
- ___Block_byref_object_dispose_.8949
- ___Block_byref_object_dispose_.9266
- ___Block_byref_object_dispose_.9470
- ___block_descriptor_104_e8_32s40s48s56s64bs72bs80w88w_e5_v8?0lw80l8w88l8s32l8s40l8s64l8s48l8s56l8s72l8
- ___block_descriptor_104_e8_32s40s48s56s64s72bs80bs88w_e5_v8?0lw88l8s32l8s40l8s48l8s72l8s56l8s64l8s80l8
- ___block_descriptor_56_e8_32s40r48r_e40_v24?0"HAPPairingIdentity"8"NSError"16ls32l8r40l8r48l8
- ___block_descriptor_56_e8_32s40s48s_e23_"<HAP2Cancelable>"8?0ls32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48bs56w_e17_v16?0"NSError"8lw56l8s32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48bs56w_e26_v36?08Q16i24"NSError"28lw56l8s32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48bs56w_e29_v24?0"NSArray"8"NSError"16lw56l8s32l8s40l8s48l8
- ___block_descriptor_88_e8_32s40s48s56bs64w72w_e26_v36?08Q16i24"NSError"28lw64l8w72l8s32l8s40l8s48l8s56l8
- ___block_descriptor_96_e8_32s40s48s56bs64bs72w80w_e5_v8?0lw72l8w80l8s32l8s40l8s56l8s48l8s64l8
- ___block_descriptor_96_e8_32s40s48s56s64s72bs80bs_e5_v8?0ls32l8s40l8s48l8s72l8s56l8s64l8s80l8
- ___block_literal_global.10198
- ___block_literal_global.10874
- ___block_literal_global.11648
- ___block_literal_global.12016
- ___block_literal_global.1293
- ___block_literal_global.13180
- ___block_literal_global.1330
- ___block_literal_global.15089
- ___block_literal_global.15519
- ___block_literal_global.16719
- ___block_literal_global.16994
- ___block_literal_global.18373
- ___block_literal_global.1925
- ___block_literal_global.19628
- ___block_literal_global.19903
- ___block_literal_global.20345
- ___block_literal_global.21312
- ___block_literal_global.218
- ___block_literal_global.222
- ___block_literal_global.225
- ___block_literal_global.22647
- ___block_literal_global.22982
- ___block_literal_global.243
- ___block_literal_global.24584
- ___block_literal_global.25198
- ___block_literal_global.2750
- ___block_literal_global.3692
- ___block_literal_global.5190
- ___block_literal_global.5366
- ___block_literal_global.5920
- ___block_literal_global.6468
- ___block_literal_global.6613
- ___block_literal_global.759
- ___block_literal_global.7686
- ___block_literal_global.8596
- ___block_literal_global.9033
- ___block_literal_global.9580
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_CoreHAP
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_CoreHAP
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_CoreHAP
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_CoreHAP
- _hkConfig.21296
- _logCategory._hmf_once_t418
- _logCategory._hmf_once_t47
- _logCategory._hmf_once_v419
- _logCategory._hmf_once_v48
- _objc_msgSend$_handlePrepareWriteResponseObject:type:prepareIdentifier:httpStatus:error:requestTuples:timeout:queue:originalCompletion:completion:
- _objc_msgSend$_handleReadECONNRESETError:readCharacteristics:responses:timeout:queue:completionHandler:
- _objc_msgSend$_handleWriteECONNResetError:writeRequests:responses:timeout:queue:completionHandler:
- _objc_msgSend$_insertReadCharacteristicValues:timeout:queue:completionHandler:
- _objc_msgSend$_insertWriteCharacteristicValues:timeout:queue:withCompletionHandler:
- _objc_msgSend$_performExecuteWriteValues:prepareIdentifier:timeout:queue:completionHandler:
- _objc_msgSend$_performTimedWriteValues:timeout:queue:completionHandler:
- _objc_msgSend$_performWriteValues:timeout:queue:completionHandler:
- _objc_msgSend$_queueReadCharacteristicValues:timeout:queue:completionHandler:
- _objc_msgSend$_queueWriteCharacteristicValues:timeout:queue:withCompletionHandler:
- _objc_msgSend$_queuedReadOperationBlock:timeout:queue:completionHandler:
- _objc_msgSend$_queuedWriteOperationBlock:timeout:queue:completionHandler:
- _objc_msgSend$_readCharacteristicValues:timeout:queue:completionHandler:
- _objc_msgSend$_writeCharacteristicValues:timeout:queue:completionHandler:
- _objc_msgSend$disassociateAccessoryWithControllerKeyUsingAccessoryIdentifier:
- _objc_msgSend$pairAccessory:delegate:
- _objc_msgSend$pairWithDelegate:
- _objc_msgSend$readCharacteristicValues:timeout:completionQueue:completionHandler:
- _objc_msgSend$readValueForCharacteristic:timeout:completionQueue:completionHandler:
- _objc_msgSend$writeCharacteristicValues:timeout:completionQueue:completionHandler:
- _sharedInstance.onceToken.15518
CStrings:
+ "\"5"
+ "%{public}@Controller key %@ is already associated for accessory %@"
+ "%{public}@CoreHAP received request after expiry"
+ "%{public}@Drop read operation due to TTL expiry"
+ "%{public}@Drop timed write operation due to TTL expiry"
+ "%{public}@Drop write operation due to TTL expiry"
+ "%{public}@Remaining TTL for read characteristic value request: %0.4f sec"
+ "%{public}@Remaining TTL for read multiple characteristic values request: %0.4f sec"
+ "%{public}@Remaining TTL for read operation: %0.4f sec"
+ "%{public}@Remaining TTL for timed write operation: %0.4f sec"
+ "%{public}@Remaining TTL for write characteristic value request: %0.4f sec"
+ "%{public}@Remaining TTL for write multiple characteristic values request: %0.4f sec"
+ "%{public}@Remaining TTL for write operation: %0.4f sec"
+ "%{public}@Unable to associate controller identifier with accessory identifier: %@"
+ "%{public}@Unable to associate controller key: %@"
+ "%{public}@Unable to establish relationsihp between accessory and controller key: %@"
+ "<none>"
+ "@\"<HAP2Cancelable>\"32@0:8@\"<HAP2UnpairedAccessoryServerPairDelegate>\"16@\"HAPAccessoryPairingRequest\"24"
+ "@\"<HAP2Cancelable>\"40@0:8@\"<HAP2UnpairedAccessoryServer>\"16@\"HAPAccessoryPairingRequest\"24@\"<HAP2AccessoryServerPairingDriverDelegate>\"32"
+ "@\"<HMFDateProvider>\""
+ "@32@0:8@16q24"
+ "@?56@0:8@16d24@32@40@?48"
+ "A"
+ "AccessoryUtils"
+ "HAPMetricsPowerManagementLogEvent"
+ "HAPMetricsPowerManagementLogEvent - Accessory Identifier: %@, Log Type: %ld"
+ "HMMLogEventSubmitting"
+ "Request TTL expired at CoreHAP"
+ "T@\"HAPAccessoryPairingRequest\",R,N"
+ "T@\"HAPPairingIdentity\",R,N"
+ "TTL already expired."
+ "Tq,R,N,V_logType"
+ "_dateProvider"
+ "_handlePrepareWriteResponseObject:type:prepareIdentifier:httpStatus:error:requestTuples:timeout:expiry:queue:originalCompletion:completion:"
+ "_handleReadECONNRESETError:readCharacteristics:responses:timeout:expiry:queue:completionHandler:"
+ "_handleWriteECONNResetError:writeRequests:responses:timeout:expiry:queue:completionHandler:"
+ "_insertReadCharacteristicValues:timeout:expiry:queue:completionHandler:"
+ "_insertWriteCharacteristicValues:timeout:expiry:queue:withCompletionHandler:"
+ "_logType"
+ "_performExecuteWriteValues:prepareIdentifier:timeout:expiry:queue:completionHandler:"
+ "_performTimedWriteValues:timeout:expiry:queue:completionHandler:"
+ "_performWriteValues:timeout:expiry:queue:completionHandler:"
+ "_queueReadCharacteristicValues:timeout:expiry:queue:completionHandler:"
+ "_queueWriteCharacteristicValues:timeout:expiry:queue:withCompletionHandler:"
+ "_queuedReadOperationBlock:timeout:expiry:queue:completionHandler:"
+ "_queuedWriteOperationBlock:timeout:expiry:queue:completionHandler:"
+ "_readCharacteristicValues:timeout:expiry:queue:completionHandler:"
+ "_writeCharacteristicValues:timeout:expiry:queue:completionHandler:"
+ "associateControllerIdentifier:error:"
+ "com.apple.homekit.corehap.powermanagement.logevent"
+ "currentLocalPairingIdentity"
+ "initForHAPAccessory:withLogType:"
+ "initForSuspendedAccessory:"
+ "initWithQualityOfService:delegate:dateProvider:"
+ "keyBagForIdentifier:"
+ "logType"
+ "now"
+ "pairAccessory:pairingRequest:delegate:"
+ "pairWithDelegate:pairingRequest:"
+ "readCharacteristicValues:timeout:expiry:completionQueue:completionHandler:"
+ "readValueForCharacteristic:timeout:expiry:completionQueue:completionHandler:"
+ "remainingTTLForExpiry:"
+ "submitLogEvent:error:"
+ "v100@0:8@16Q24@32i40@44@52d60@68@76@?84@?92"
+ "v24@0:8@\"HMMLogEvent\"16"
+ "v32@0:8@\"HMMLogEvent\"16@\"NSError\"24"
+ "v56@0:8@16d24@32@40@?48"
+ "v64@0:8@16@24d32@40@48@?56"
+ "v72@0:8@16@24@32d40@48@56@?64"
+ "writeCharacteristicValue:timeout:expiry:completionQueue:completionHandler:"
+ "writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:"
- "\"4"
- "@\"<HAP2Cancelable>\"24@0:8@\"<HAP2UnpairedAccessoryServerPairDelegate>\"16"
- "@\"<HAP2Cancelable>\"32@0:8@\"<HAP2UnpairedAccessoryServer>\"16@\"<HAP2AccessoryServerPairingDriverDelegate>\"24"
- "@?48@0:8@16d24@32@?40"
- "B24@0:8@\"NSError\"16"
- "T@\"HAPAccessoryPairingRequest\",R"
- "_handlePrepareWriteResponseObject:type:prepareIdentifier:httpStatus:error:requestTuples:timeout:queue:originalCompletion:completion:"
- "_handleReadECONNRESETError:readCharacteristics:responses:timeout:queue:completionHandler:"
- "_handleWriteECONNResetError:writeRequests:responses:timeout:queue:completionHandler:"
- "_insertReadCharacteristicValues:timeout:queue:completionHandler:"
- "_insertWriteCharacteristicValues:timeout:queue:withCompletionHandler:"
- "_performExecuteWriteValues:prepareIdentifier:timeout:queue:completionHandler:"
- "_performTimedWriteValues:timeout:queue:completionHandler:"
- "_performWriteValues:timeout:queue:completionHandler:"
- "_queueReadCharacteristicValues:timeout:queue:completionHandler:"
- "_queueWriteCharacteristicValues:timeout:queue:withCompletionHandler:"
- "_queuedReadOperationBlock:timeout:queue:completionHandler:"
- "_queuedWriteOperationBlock:timeout:queue:completionHandler:"
- "_readCharacteristicValues:timeout:queue:completionHandler:"
- "_writeCharacteristicValues:timeout:queue:completionHandler:"
- "pairAccessory:delegate:"
- "pairWithDelegate:"
- "rA"
- "readCharacteristicValues:timeout:completionQueue:completionHandler:"
- "readValueForCharacteristic:timeout:completionQueue:completionHandler:"
- "v24@0:8@\"NSData\"16"
- "v56@0:8@16@24d32@40@?48"
- "v64@0:8@16@24@32d40@48@?56"
- "v92@0:8@16Q24@32i40@44@52d60@68@?76@?84"
- "writeCharacteristicValue:timeout:completionQueue:completionHandler:"
- "writeCharacteristicValues:timeout:completionQueue:completionHandler:"

```
