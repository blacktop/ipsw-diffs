## CoreHAP

> `/System/Library/PrivateFrameworks/CoreHAP.framework/CoreHAP`

```diff

-  __TEXT.__text: 0x291238
-  __TEXT.__objc_methlist: 0x187d0
-  __TEXT.__const: 0x1220
+  __TEXT.__text: 0x2ab5a4
+  __TEXT.__objc_methlist: 0x18ad8
+  __TEXT.__const: 0x1230
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__constg_swiftt: 0x8c8
-  __TEXT.__swift5_typeref: 0x38e
+  __TEXT.__constg_swiftt: 0x918
+  __TEXT.__swift5_typeref: 0x3e4
   __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_reflstr: 0x404
-  __TEXT.__swift5_fieldmd: 0x3c0
+  __TEXT.__swift5_reflstr: 0x424
+  __TEXT.__swift5_fieldmd: 0x3cc
   __TEXT.__swift5_assocty: 0xc0
   __TEXT.__swift5_proto: 0x50
   __TEXT.__swift5_types: 0x30
-  __TEXT.__cstring: 0x14327
-  __TEXT.__oslogstring: 0x434f1
-  __TEXT.__swift5_capture: 0x204
-  __TEXT.__gcc_except_tab: 0x5e50
-  __TEXT.__unwind_info: 0x7580
-  __TEXT.__eh_frame: 0xd38
+  __TEXT.__cstring: 0x14599
+  __TEXT.__oslogstring: 0x43aea
+  __TEXT.__swift5_capture: 0x278
+  __TEXT.__gcc_except_tab: 0x5ee8
+  __TEXT.__unwind_info: 0x7768
+  __TEXT.__eh_frame: 0x1000
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5900
-  __DATA_CONST.__objc_classlist: 0xc00
+  __DATA_CONST.__const: 0x59c0
+  __DATA_CONST.__objc_classlist: 0xc18
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x3b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8070
+  __DATA_CONST.__objc_selrefs: 0x8218
   __DATA_CONST.__objc_protorefs: 0x100
-  __DATA_CONST.__objc_superrefs: 0xa50
+  __DATA_CONST.__objc_superrefs: 0xa68
   __DATA_CONST.__objc_arraydata: 0x200
-  __DATA_CONST.__got: 0xfc0
-  __AUTH_CONST.__const: 0x1298
-  __AUTH_CONST.__cfstring: 0xffc0
-  __AUTH_CONST.__objc_const: 0x2aae0
+  __DATA_CONST.__got: 0x1028
+  __AUTH_CONST.__const: 0x1448
+  __AUTH_CONST.__cfstring: 0x10020
+  __AUTH_CONST.__objc_const: 0x2afd0
   __AUTH_CONST.__objc_intobj: 0x738
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0xc0
-  __AUTH_CONST.__auth_got: 0x12d8
-  __AUTH.__objc_data: 0x71c8
-  __AUTH.__data: 0xb0
+  __AUTH_CONST.__auth_got: 0x1338
+  __AUTH.__objc_data: 0x72e8
+  __AUTH.__data: 0x80
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x28
-  __DATA.__objc_ivar: 0x18c4
-  __DATA.__data: 0x2d42
+  __DATA.__objc_ivar: 0x18fc
+  __DATA.__data: 0x2d72
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xf20
+  __DATA.__bss: 0xee0
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0xfa0
-  __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x58
+  __DATA_DIRTY.__objc_data: 0xfc8
+  __DATA_DIRTY.__data: 0x48
+  __DATA_DIRTY.__bss: 0xa8
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9663
-  Symbols:   29537
-  CStrings:  9115
+  Functions: 9807
+  Symbols:   29809
+  CStrings:  9150
 
Sections:
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_floatobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__thread_vars : content changed
Symbols:
+ +[HAP2Diagnostics sharedDiagnostics]
+ -[HAP2AccessoryServer _browserFastSetHasDiscoveryAdvertisement:]
+ -[HAP2AsynchronousOperation enqueueMachTime]
+ -[HAP2AsynchronousOperation executeStartMachTime]
+ -[HAP2AsynchronousOperation owningQueue]
+ -[HAP2AsynchronousOperation reportStallSnapshotIfNeeded:waitLatency:]
+ -[HAP2AsynchronousOperation setEnqueueMachTime:]
+ -[HAP2AsynchronousOperation setExecuteStartMachTime:]
+ -[HAP2AsynchronousOperation setOwningQueue:]
+ -[HAP2AsynchronousOperation setUnfinishedDependencyCount:]
+ -[HAP2AsynchronousOperation stallSnapshotForWaitLatency:]
+ -[HAP2AsynchronousOperation unfinishedDependencyCount]
+ -[HAP2Diagnostics .cxx_destruct]
+ -[HAP2Diagnostics notifyOperationQueueStallWithSnapshot:]
+ -[HAP2Diagnostics observer]
+ -[HAP2Diagnostics setObserver:]
+ -[HAP2SerializedOperationQueue _stampDiagnosticsOnOperations:]
+ -[HAPAccessoryServerBrowserIP maximumNumberOfPairVerifiesAllowed]
+ -[HAPAccessoryServerNFC _isTransientKeychainError:]
+ -[HAPAccessoryServerNFC _normalizeNFCPairSetupError:]
+ -[HAPAccessoryServerNFC pairSetupSession:promptUncertifiedForMFiRollError:completionHandler:]
+ -[HAPAdditionalWifiData .cxx_destruct]
+ -[HAPAdditionalWifiData bssid]
+ -[HAPAdditionalWifiData channelNumber]
+ -[HAPAdditionalWifiData copyWithZone:]
+ -[HAPAdditionalWifiData initWithOperatingClass:channelNumber:bssid:]
+ -[HAPAdditionalWifiData init]
+ -[HAPAdditionalWifiData operatingClass]
+ -[HAPAdditionalWifiData setBssid:]
+ -[HAPAdditionalWifiData setChannelNumber:]
+ -[HAPAdditionalWifiData setOperatingClass:]
+ -[HAPMetricsDispatcher _evictExpiredRacingRendezvousAtUptime:orphanedHandlers:]
+ -[HAPMetricsDispatcher _isExpiredRendezvous:atUptime:]
+ -[HAPMetricsDispatcher _matchedRacingHandlerForRendezvous:forIdentifier:messageID:]
+ -[HAPMetricsDispatcher _racingKeyForIdentifier:messageID:]
+ -[HAPMetricsDispatcher _racingRendezvousForIdentifier:messageID:atUptime:orphanedHandlers:]
+ -[HAPMetricsDispatcher _updateRacingRendezvousForIdentifier:messageID:withBlock:]
+ -[HAPMetricsDispatcher awaitRacingResultForAccessoryIdentifier:messageID:handler:]
+ -[HAPMetricsDispatcher deliverRacingResult:forAccessoryIdentifier:messageID:]
+ -[HAPMetricsDispatcher init]
+ -[HAPMetricsDispatcher lastRacingSweepUptime]
+ -[HAPMetricsDispatcher racingRendezvousByKey]
+ -[HAPMetricsDispatcher setLastRacingSweepUptime:]
+ -[HAPMetricsDispatcher setRacingRendezvousByKey:]
+ -[HAPMetricsDispatcher setUptimeProvider:]
+ -[HAPMetricsDispatcher uptimeProvider]
+ -[HAPMetricsRacingRendezvous .cxx_destruct]
+ -[HAPMetricsRacingRendezvous handler]
+ -[HAPMetricsRacingRendezvous initWithInsertUptime:]
+ -[HAPMetricsRacingRendezvous insertUptime]
+ -[HAPMetricsRacingRendezvous racingResult]
+ -[HAPMetricsRacingRendezvous setHandler:]
+ -[HAPMetricsRacingRendezvous setRacingResult:]
+ -[HAPSystemKeychainStore ecdsaPairingKeyExistsForAccessoryName:]
+ GCC_except_table1070
+ GCC_except_table1072
+ GCC_except_table1183
+ GCC_except_table1185
+ GCC_except_table1198
+ GCC_except_table1210
+ GCC_except_table1212
+ GCC_except_table1214
+ GCC_except_table1216
+ GCC_except_table1342
+ GCC_except_table1346
+ GCC_except_table1348
+ GCC_except_table1550
+ GCC_except_table1762
+ GCC_except_table1767
+ GCC_except_table1773
+ GCC_except_table1775
+ GCC_except_table1781
+ GCC_except_table1787
+ GCC_except_table1795
+ GCC_except_table1797
+ GCC_except_table1799
+ GCC_except_table1804
+ GCC_except_table1818
+ GCC_except_table1826
+ GCC_except_table1833
+ GCC_except_table1837
+ GCC_except_table1841
+ GCC_except_table1845
+ GCC_except_table1883
+ GCC_except_table2002
+ GCC_except_table2006
+ GCC_except_table2009
+ GCC_except_table2011
+ GCC_except_table2023
+ GCC_except_table2028
+ GCC_except_table2035
+ GCC_except_table2037
+ GCC_except_table2040
+ GCC_except_table2067
+ GCC_except_table2071
+ GCC_except_table2079
+ GCC_except_table2081
+ GCC_except_table2087
+ GCC_except_table2091
+ GCC_except_table2093
+ GCC_except_table2096
+ GCC_except_table2099
+ GCC_except_table2101
+ GCC_except_table2107
+ GCC_except_table2111
+ GCC_except_table2119
+ GCC_except_table2130
+ GCC_except_table2186
+ GCC_except_table2187
+ GCC_except_table2188
+ GCC_except_table2191
+ GCC_except_table2192
+ GCC_except_table2195
+ GCC_except_table2217
+ GCC_except_table2221
+ GCC_except_table2229
+ GCC_except_table226
+ GCC_except_table227
+ GCC_except_table233
+ GCC_except_table236
+ GCC_except_table239
+ GCC_except_table2395
+ GCC_except_table2402
+ GCC_except_table2406
+ GCC_except_table2410
+ GCC_except_table2414
+ GCC_except_table2417
+ GCC_except_table2419
+ GCC_except_table242
+ GCC_except_table2421
+ GCC_except_table2424
+ GCC_except_table2430
+ GCC_except_table2432
+ GCC_except_table2435
+ GCC_except_table2436
+ GCC_except_table2438
+ GCC_except_table244
+ GCC_except_table246
+ GCC_except_table247
+ GCC_except_table250
+ GCC_except_table252
+ GCC_except_table2538
+ GCC_except_table2546
+ GCC_except_table2548
+ GCC_except_table2549
+ GCC_except_table2550
+ GCC_except_table2551
+ GCC_except_table2566
+ GCC_except_table2580
+ GCC_except_table261
+ GCC_except_table265
+ GCC_except_table2660
+ GCC_except_table2672
+ GCC_except_table2877
+ GCC_except_table2886
+ GCC_except_table2903
+ GCC_except_table2937
+ GCC_except_table2953
+ GCC_except_table2955
+ GCC_except_table2967
+ GCC_except_table2974
+ GCC_except_table2996
+ GCC_except_table3010
+ GCC_except_table3011
+ GCC_except_table3012
+ GCC_except_table3015
+ GCC_except_table3021
+ GCC_except_table3028
+ GCC_except_table3031
+ GCC_except_table3036
+ GCC_except_table3041
+ GCC_except_table3046
+ GCC_except_table3102
+ GCC_except_table3105
+ GCC_except_table3110
+ GCC_except_table3112
+ GCC_except_table3128
+ GCC_except_table3142
+ GCC_except_table3148
+ GCC_except_table3156
+ GCC_except_table3164
+ GCC_except_table3228
+ GCC_except_table3235
+ GCC_except_table3237
+ GCC_except_table3238
+ GCC_except_table3261
+ GCC_except_table3281
+ GCC_except_table3509
+ GCC_except_table3576
+ GCC_except_table3577
+ GCC_except_table3581
+ GCC_except_table3584
+ GCC_except_table3586
+ GCC_except_table3587
+ GCC_except_table3589
+ GCC_except_table3590
+ GCC_except_table3592
+ GCC_except_table3599
+ GCC_except_table3609
+ GCC_except_table3612
+ GCC_except_table3624
+ GCC_except_table3634
+ GCC_except_table3636
+ GCC_except_table3639
+ GCC_except_table3642
+ GCC_except_table3654
+ GCC_except_table3656
+ GCC_except_table3660
+ GCC_except_table3664
+ GCC_except_table3668
+ GCC_except_table3694
+ GCC_except_table3717
+ GCC_except_table3723
+ GCC_except_table3727
+ GCC_except_table3731
+ GCC_except_table3736
+ GCC_except_table3738
+ GCC_except_table3740
+ GCC_except_table3747
+ GCC_except_table3748
+ GCC_except_table3749
+ GCC_except_table3837
+ GCC_except_table3845
+ GCC_except_table3870
+ GCC_except_table3873
+ GCC_except_table3878
+ GCC_except_table3886
+ GCC_except_table3892
+ GCC_except_table3894
+ GCC_except_table3927
+ GCC_except_table3933
+ GCC_except_table3978
+ GCC_except_table3979
+ GCC_except_table3980
+ GCC_except_table3981
+ GCC_except_table3982
+ GCC_except_table3983
+ GCC_except_table3984
+ GCC_except_table3985
+ GCC_except_table3986
+ GCC_except_table3987
+ GCC_except_table3988
+ GCC_except_table3989
+ GCC_except_table3990
+ GCC_except_table3991
+ GCC_except_table4030
+ GCC_except_table4057
+ GCC_except_table4167
+ GCC_except_table4174
+ GCC_except_table4220
+ GCC_except_table4223
+ GCC_except_table4226
+ GCC_except_table4235
+ GCC_except_table4238
+ GCC_except_table4241
+ GCC_except_table4244
+ GCC_except_table4249
+ GCC_except_table4262
+ GCC_except_table4271
+ GCC_except_table4273
+ GCC_except_table4276
+ GCC_except_table4287
+ GCC_except_table4295
+ GCC_except_table4299
+ GCC_except_table4305
+ GCC_except_table4306
+ GCC_except_table4309
+ GCC_except_table4310
+ GCC_except_table4328
+ GCC_except_table4330
+ GCC_except_table4332
+ GCC_except_table4333
+ GCC_except_table4336
+ GCC_except_table4342
+ GCC_except_table4345
+ GCC_except_table4347
+ GCC_except_table4353
+ GCC_except_table4355
+ GCC_except_table4358
+ GCC_except_table4369
+ GCC_except_table4380
+ GCC_except_table4382
+ GCC_except_table4391
+ GCC_except_table4393
+ GCC_except_table4395
+ GCC_except_table4401
+ GCC_except_table4661
+ GCC_except_table4667
+ GCC_except_table4684
+ GCC_except_table4688
+ GCC_except_table4705
+ GCC_except_table4711
+ GCC_except_table4724
+ GCC_except_table4738
+ GCC_except_table4742
+ GCC_except_table4855
+ GCC_except_table5311
+ GCC_except_table5319
+ GCC_except_table532
+ GCC_except_table5329
+ GCC_except_table5371
+ GCC_except_table5374
+ GCC_except_table5375
+ GCC_except_table5376
+ GCC_except_table5377
+ GCC_except_table542
+ GCC_except_table5511
+ GCC_except_table5512
+ GCC_except_table5513
+ GCC_except_table5514
+ GCC_except_table5515
+ GCC_except_table5516
+ GCC_except_table5522
+ GCC_except_table5523
+ GCC_except_table5525
+ GCC_except_table5532
+ GCC_except_table5535
+ GCC_except_table5537
+ GCC_except_table5542
+ GCC_except_table5545
+ GCC_except_table5548
+ GCC_except_table5552
+ GCC_except_table5556
+ GCC_except_table556
+ GCC_except_table564
+ GCC_except_table600
+ GCC_except_table6042
+ GCC_except_table6043
+ GCC_except_table6062
+ GCC_except_table6072
+ GCC_except_table6075
+ GCC_except_table6080
+ GCC_except_table6083
+ GCC_except_table6087
+ GCC_except_table612
+ GCC_except_table613
+ GCC_except_table615
+ GCC_except_table618
+ GCC_except_table621
+ GCC_except_table631
+ GCC_except_table633
+ GCC_except_table6356
+ GCC_except_table6360
+ GCC_except_table637
+ GCC_except_table6405
+ GCC_except_table6409
+ GCC_except_table6411
+ GCC_except_table6413
+ GCC_except_table644
+ GCC_except_table647
+ GCC_except_table6615
+ GCC_except_table6621
+ GCC_except_table6625
+ GCC_except_table6626
+ GCC_except_table6627
+ GCC_except_table6628
+ GCC_except_table6634
+ GCC_except_table6650
+ GCC_except_table6685
+ GCC_except_table6686
+ GCC_except_table6687
+ GCC_except_table6707
+ GCC_except_table6719
+ GCC_except_table6722
+ GCC_except_table6727
+ GCC_except_table6729
+ GCC_except_table6743
+ GCC_except_table681
+ GCC_except_table691
+ GCC_except_table6966
+ GCC_except_table6979
+ GCC_except_table6984
+ GCC_except_table6988
+ GCC_except_table699
+ GCC_except_table6990
+ GCC_except_table6991
+ GCC_except_table6993
+ GCC_except_table7023
+ GCC_except_table7045
+ GCC_except_table7049
+ GCC_except_table7053
+ GCC_except_table7058
+ GCC_except_table7062
+ GCC_except_table7066
+ GCC_except_table7070
+ GCC_except_table7074
+ GCC_except_table7082
+ GCC_except_table7084
+ GCC_except_table7086
+ GCC_except_table7125
+ GCC_except_table7234
+ GCC_except_table7266
+ GCC_except_table730
+ GCC_except_table733
+ GCC_except_table735
+ GCC_except_table7351
+ GCC_except_table7352
+ GCC_except_table7354
+ GCC_except_table7355
+ GCC_except_table7356
+ GCC_except_table7357
+ GCC_except_table741
+ GCC_except_table7419
+ GCC_except_table7429
+ GCC_except_table743
+ GCC_except_table7430
+ GCC_except_table7442
+ GCC_except_table7448
+ GCC_except_table7464
+ GCC_except_table7465
+ GCC_except_table7470
+ GCC_except_table7473
+ GCC_except_table7480
+ GCC_except_table7483
+ GCC_except_table7497
+ GCC_except_table7504
+ GCC_except_table7510
+ GCC_except_table7519
+ GCC_except_table7521
+ GCC_except_table7525
+ GCC_except_table7526
+ GCC_except_table7533
+ GCC_except_table7545
+ GCC_except_table7554
+ GCC_except_table756
+ GCC_except_table7569
+ GCC_except_table7570
+ GCC_except_table7575
+ GCC_except_table7579
+ GCC_except_table7580
+ GCC_except_table7583
+ GCC_except_table7589
+ GCC_except_table7593
+ GCC_except_table7597
+ GCC_except_table7599
+ GCC_except_table760
+ GCC_except_table7601
+ GCC_except_table7605
+ GCC_except_table7719
+ GCC_except_table774
+ GCC_except_table775
+ GCC_except_table7756
+ GCC_except_table780
+ GCC_except_table7813
+ GCC_except_table7816
+ GCC_except_table7820
+ GCC_except_table7826
+ GCC_except_table783
+ GCC_except_table7833
+ GCC_except_table7834
+ GCC_except_table7854
+ GCC_except_table786
+ GCC_except_table7905
+ GCC_except_table7906
+ GCC_except_table7908
+ GCC_except_table791
+ GCC_except_table7911
+ GCC_except_table7939
+ GCC_except_table7944
+ GCC_except_table795
+ GCC_except_table7964
+ GCC_except_table7982
+ GCC_except_table7983
+ GCC_except_table7984
+ GCC_except_table7993
+ GCC_except_table7998
+ GCC_except_table7999
+ GCC_except_table8000
+ GCC_except_table801
+ GCC_except_table8015
+ GCC_except_table8018
+ GCC_except_table802
+ GCC_except_table8025
+ GCC_except_table8032
+ GCC_except_table8037
+ GCC_except_table8043
+ GCC_except_table8055
+ GCC_except_table8056
+ GCC_except_table8061
+ GCC_except_table807
+ GCC_except_table8070
+ GCC_except_table8076
+ GCC_except_table8077
+ GCC_except_table808
+ GCC_except_table8081
+ GCC_except_table8083
+ GCC_except_table8085
+ GCC_except_table8089
+ GCC_except_table8110
+ GCC_except_table8112
+ GCC_except_table8113
+ GCC_except_table8139
+ GCC_except_table8304
+ GCC_except_table834
+ GCC_except_table8367
+ GCC_except_table8399
+ GCC_except_table8402
+ GCC_except_table841
+ GCC_except_table848
+ GCC_except_table849
+ GCC_except_table8569
+ GCC_except_table86
+ GCC_except_table8607
+ GCC_except_table8644
+ GCC_except_table8722
+ GCC_except_table8724
+ GCC_except_table8728
+ GCC_except_table8730
+ GCC_except_table8732
+ GCC_except_table8734
+ GCC_except_table8737
+ GCC_except_table8739
+ GCC_except_table8741
+ GCC_except_table8743
+ GCC_except_table8745
+ GCC_except_table8748
+ GCC_except_table8750
+ GCC_except_table8752
+ GCC_except_table8759
+ GCC_except_table8765
+ GCC_except_table877
+ GCC_except_table8783
+ GCC_except_table8786
+ GCC_except_table8815
+ GCC_except_table8818
+ GCC_except_table8819
+ GCC_except_table8858
+ GCC_except_table8859
+ GCC_except_table8860
+ GCC_except_table8862
+ GCC_except_table8863
+ GCC_except_table8865
+ GCC_except_table8866
+ GCC_except_table8867
+ GCC_except_table8869
+ GCC_except_table8870
+ GCC_except_table8872
+ GCC_except_table8876
+ GCC_except_table8877
+ GCC_except_table8881
+ GCC_except_table8932
+ GCC_except_table8939
+ GCC_except_table900
+ GCC_except_table9043
+ GCC_except_table9047
+ GCC_except_table9049
+ GCC_except_table9051
+ GCC_except_table9054
+ GCC_except_table9056
+ GCC_except_table9058
+ GCC_except_table9060
+ GCC_except_table9061
+ GCC_except_table9063
+ GCC_except_table9065
+ GCC_except_table9070
+ GCC_except_table9072
+ GCC_except_table9073
+ GCC_except_table918
+ GCC_except_table942
+ GCC_except_table946
+ GCC_except_table960
+ GCC_except_table965
+ _HAP2OperationSecondsSinceMachTime
+ _HMFQualityOfServiceClassToString
+ _HMFQualityOfServiceToString
+ _OBJC_CLASS_$_HAP2Diagnostics
+ _OBJC_CLASS_$_HAPAdditionalWifiData
+ _OBJC_CLASS_$_HAPMetricsRacingRendezvous
+ _OBJC_IVAR_$_HAP2AsynchronousOperation._enqueueMachTime
+ _OBJC_IVAR_$_HAP2AsynchronousOperation._executeStartMachTime
+ _OBJC_IVAR_$_HAP2AsynchronousOperation._owningQueue
+ _OBJC_IVAR_$_HAP2AsynchronousOperation._unfinishedDependencyCount
+ _OBJC_IVAR_$_HAP2Diagnostics._observer
+ _OBJC_IVAR_$_HAPAccessoryServerBrowserIP._maximumNumberOfPairVerifiesAllowed
+ _OBJC_IVAR_$_HAPAdditionalWifiData._bssid
+ _OBJC_IVAR_$_HAPAdditionalWifiData._channelNumber
+ _OBJC_IVAR_$_HAPAdditionalWifiData._operatingClass
+ _OBJC_IVAR_$_HAPMetricsDispatcher._lastRacingSweepUptime
+ _OBJC_IVAR_$_HAPMetricsDispatcher._racingRendezvousByKey
+ _OBJC_IVAR_$_HAPMetricsDispatcher._uptimeProvider
+ _OBJC_IVAR_$_HAPMetricsRacingRendezvous._handler
+ _OBJC_IVAR_$_HAPMetricsRacingRendezvous._insertUptime
+ _OBJC_IVAR_$_HAPMetricsRacingRendezvous._racingResult
+ _OBJC_METACLASS_$_HAP2Diagnostics
+ _OBJC_METACLASS_$_HAPAdditionalWifiData
+ _OBJC_METACLASS_$_HAPMetricsRacingRendezvous
+ __OBJC_$_CLASS_METHODS_HAP2Diagnostics
+ __OBJC_$_CLASS_PROP_LIST_HAP2Diagnostics
+ __OBJC_$_INSTANCE_METHODS_HAP2Diagnostics
+ __OBJC_$_INSTANCE_METHODS_HAPAdditionalWifiData
+ __OBJC_$_INSTANCE_METHODS_HAPMetricsRacingRendezvous
+ __OBJC_$_INSTANCE_VARIABLES_HAP2Diagnostics
+ __OBJC_$_INSTANCE_VARIABLES_HAPAdditionalWifiData
+ __OBJC_$_INSTANCE_VARIABLES_HAPMetricsRacingRendezvous
+ __OBJC_$_PROP_LIST_HAP2Diagnostics
+ __OBJC_$_PROP_LIST_HAPAdditionalWifiData
+ __OBJC_$_PROP_LIST_HAPMetricsRacingRendezvous
+ __OBJC_CLASS_PROTOCOLS_$_HAPAdditionalWifiData
+ __OBJC_CLASS_RO_$_HAP2Diagnostics
+ __OBJC_CLASS_RO_$_HAPAdditionalWifiData
+ __OBJC_CLASS_RO_$_HAPMetricsRacingRendezvous
+ __OBJC_METACLASS_RO_$_HAP2Diagnostics
+ __OBJC_METACLASS_RO_$_HAPAdditionalWifiData
+ __OBJC_METACLASS_RO_$_HAPMetricsRacingRendezvous
+ ___28-[HAPMetricsDispatcher init]_block_invoke
+ ___36+[HAP2Diagnostics sharedDiagnostics]_block_invoke
+ ___44-[HAP2AsynchronousOperation enqueueMachTime]_block_invoke
+ ___48-[HAP2AsynchronousOperation setEnqueueMachTime:]_block_invoke
+ ___49-[HAP2AsynchronousOperation executeStartMachTime]_block_invoke
+ ___53-[HAP2AsynchronousOperation setExecuteStartMachTime:]_block_invoke
+ ___54-[HAP2AsynchronousOperation unfinishedDependencyCount]_block_invoke
+ ___58-[HAP2AsynchronousOperation setUnfinishedDependencyCount:]_block_invoke
+ ___62-[HAP2SerializedOperationQueue _stampDiagnosticsOnOperations:]_block_invoke
+ ___64-[HAP2AccessoryServer _browserFastSetHasDiscoveryAdvertisement:]_block_invoke
+ ___64-[HAPSystemKeychainStore ecdsaPairingKeyExistsForAccessoryName:]_block_invoke
+ ___77-[HAPMetricsDispatcher deliverRacingResult:forAccessoryIdentifier:messageID:]_block_invoke
+ ___79-[HAPMetricsDispatcher _evictExpiredRacingRendezvousAtUptime:orphanedHandlers:]_block_invoke
+ ___82-[HAPMetricsDispatcher awaitRacingResultForAccessoryIdentifier:messageID:handler:]_block_invoke
+ ___83-[HAPMetricsDispatcher _matchedRacingHandlerForRendezvous:forIdentifier:messageID:]_block_invoke
+ ___93-[HAPAccessoryServerNFC pairSetupSession:promptUncertifiedForMFiRollError:completionHandler:]_block_invoke
+ ___block_descriptor_32_e5_d8?0l
+ ___block_descriptor_40_e8_32bs_e36_v16?0"HAPMetricsRacingRendezvous"8ls32l8
+ ___block_descriptor_40_e8_32bs_e67_v40?0"NSData"8"NSString"16"HAPAdditionalWifiData"24"NSError"32ls32l8
+ ___block_descriptor_40_e8_32s_e36_v16?0"HAPMetricsRacingRendezvous"8ls32l8
+ ___block_descriptor_48_e8_32s_e28_v32?0"NSOperation"8Q16^B24ls32l8
+ ___block_descriptor_48_e8_32s_e53_B32?0"NSString"8"HAPMetricsRacingRendezvous"16^B24ls32l8
+ ___swift_closure_destructor.173Tm
+ __apduRejectedErrorWithSW
+ _logCategory._hmf_once_t856
+ _logCategory._hmf_once_v857
+ _mach_continuous_time
+ _mach_timebase_info
+ _objc_msgSend$_browserFastSetHasDiscoveryAdvertisement:
+ _objc_msgSend$_evictExpiredRacingRendezvousAtUptime:orphanedHandlers:
+ _objc_msgSend$_isExpiredRendezvous:atUptime:
+ _objc_msgSend$_isTransientKeychainError:
+ _objc_msgSend$_matchedRacingHandlerForRendezvous:forIdentifier:messageID:
+ _objc_msgSend$_normalizeNFCPairSetupError:
+ _objc_msgSend$_racingKeyForIdentifier:messageID:
+ _objc_msgSend$_racingRendezvousForIdentifier:messageID:atUptime:orphanedHandlers:
+ _objc_msgSend$_stampDiagnosticsOnOperations:
+ _objc_msgSend$_updateRacingRendezvousForIdentifier:messageID:withBlock:
+ _objc_msgSend$accessoryServer:promptUncertifiedForMFiRollError:completionHandler:
+ _objc_msgSend$channelNumber
+ _objc_msgSend$ecdsaPairingKeyExistsForAccessoryName:
+ _objc_msgSend$enqueueMachTime
+ _objc_msgSend$executeStartMachTime
+ _objc_msgSend$hap2DiagnosticsDidObserveOperationQueueStallWithSnapshot:
+ _objc_msgSend$initWithInsertUptime:
+ _objc_msgSend$initWithOperatingClass:channelNumber:bssid:
+ _objc_msgSend$insertUptime
+ _objc_msgSend$keysOfEntriesPassingTest:
+ _objc_msgSend$lastRacingSweepUptime
+ _objc_msgSend$maxConcurrentOperationCount
+ _objc_msgSend$notifyOperationQueueStallWithSnapshot:
+ _objc_msgSend$observer
+ _objc_msgSend$operatingClass
+ _objc_msgSend$owningQueue
+ _objc_msgSend$pairSetupSession:promptUncertifiedForMFiRollError:completionHandler:
+ _objc_msgSend$qualityOfService
+ _objc_msgSend$racingRendezvousByKey
+ _objc_msgSend$racingResult
+ _objc_msgSend$removeObjectsForKeys:
+ _objc_msgSend$reportStallSnapshotIfNeeded:waitLatency:
+ _objc_msgSend$setEnqueueMachTime:
+ _objc_msgSend$setExecuteStartMachTime:
+ _objc_msgSend$setLastRacingSweepUptime:
+ _objc_msgSend$setOwningQueue:
+ _objc_msgSend$setRacingResult:
+ _objc_msgSend$setUnfinishedDependencyCount:
+ _objc_msgSend$sharedDiagnostics
+ _objc_msgSend$stallSnapshotForWaitLatency:
+ _objc_msgSend$unfinishedDependencyCount
+ _objc_msgSend$uptimeProvider
+ _objc_sync_enter
+ _objc_sync_exit
+ _qos_class_self
+ _sharedDiagnostics.onceToken
+ _sharedDiagnostics.sharedDiagnostics
+ _symbolic So21HAPAdditionalWifiDataCSg
+ _symbolic _____SgXwz_Xx 7CoreHAP24HAPSpakePairSetupSessionC
+ _symbolic ______p s5ErrorP
+ _symbolic _____ySiG s11_SetStorageC
+ _symbolic _____ySiG s23_ContiguousArrayStorageC
+ _symbolic _____ySnySiGG s23_ContiguousArrayStorageC
- -[HAPAccessoryServerBrowserIP maximumNumberOfPairVeifiesAllowed]
- GCC_except_table1032
- GCC_except_table1034
- GCC_except_table1140
- GCC_except_table1145
- GCC_except_table1147
- GCC_except_table1160
- GCC_except_table1172
- GCC_except_table1174
- GCC_except_table1176
- GCC_except_table1304
- GCC_except_table1308
- GCC_except_table1310
- GCC_except_table1527
- GCC_except_table1737
- GCC_except_table1739
- GCC_except_table1744
- GCC_except_table1750
- GCC_except_table1752
- GCC_except_table1758
- GCC_except_table1764
- GCC_except_table1768
- GCC_except_table1770
- GCC_except_table1772
- GCC_except_table1774
- GCC_except_table1779
- GCC_except_table1801
- GCC_except_table1812
- GCC_except_table1816
- GCC_except_table1820
- GCC_except_table1858
- GCC_except_table1977
- GCC_except_table1981
- GCC_except_table1982
- GCC_except_table1984
- GCC_except_table1986
- GCC_except_table199
- GCC_except_table1998
- GCC_except_table200
- GCC_except_table2003
- GCC_except_table2010
- GCC_except_table2012
- GCC_except_table2015
- GCC_except_table2042
- GCC_except_table2044
- GCC_except_table2046
- GCC_except_table2051
- GCC_except_table2054
- GCC_except_table206
- GCC_except_table2060
- GCC_except_table2064
- GCC_except_table2066
- GCC_except_table207
- GCC_except_table2072
- GCC_except_table2074
- GCC_except_table2080
- GCC_except_table209
- GCC_except_table2092
- GCC_except_table212
- GCC_except_table2136
- GCC_except_table2141
- GCC_except_table215
- GCC_except_table2159
- GCC_except_table2160
- GCC_except_table2161
- GCC_except_table2164
- GCC_except_table2165
- GCC_except_table2167
- GCC_except_table217
- GCC_except_table219
- GCC_except_table220
- GCC_except_table2202
- GCC_except_table223
- GCC_except_table225
- GCC_except_table2368
- GCC_except_table2375
- GCC_except_table2379
- GCC_except_table238
- GCC_except_table2383
- GCC_except_table2387
- GCC_except_table2390
- GCC_except_table2392
- GCC_except_table2394
- GCC_except_table2397
- GCC_except_table2403
- GCC_except_table2405
- GCC_except_table2408
- GCC_except_table2409
- GCC_except_table2411
- GCC_except_table2505
- GCC_except_table2513
- GCC_except_table2514
- GCC_except_table2515
- GCC_except_table2516
- GCC_except_table2517
- GCC_except_table2518
- GCC_except_table2533
- GCC_except_table2627
- GCC_except_table2639
- GCC_except_table2665
- GCC_except_table2673
- GCC_except_table2684
- GCC_except_table2698
- GCC_except_table2701
- GCC_except_table2706
- GCC_except_table2714
- GCC_except_table2720
- GCC_except_table2722
- GCC_except_table2916
- GCC_except_table2925
- GCC_except_table2942
- GCC_except_table2976
- GCC_except_table2992
- GCC_except_table2994
- GCC_except_table3006
- GCC_except_table3013
- GCC_except_table3035
- GCC_except_table3049
- GCC_except_table3050
- GCC_except_table3051
- GCC_except_table3054
- GCC_except_table3060
- GCC_except_table3067
- GCC_except_table3070
- GCC_except_table3075
- GCC_except_table3080
- GCC_except_table3124
- GCC_except_table3141
- GCC_except_table3149
- GCC_except_table3151
- GCC_except_table3167
- GCC_except_table3181
- GCC_except_table3183
- GCC_except_table3187
- GCC_except_table3195
- GCC_except_table3203
- GCC_except_table3267
- GCC_except_table3274
- GCC_except_table3276
- GCC_except_table3277
- GCC_except_table3300
- GCC_except_table3320
- GCC_except_table3548
- GCC_except_table3615
- GCC_except_table3616
- GCC_except_table3620
- GCC_except_table3625
- GCC_except_table3629
- GCC_except_table3638
- GCC_except_table3648
- GCC_except_table3651
- GCC_except_table3662
- GCC_except_table3663
- GCC_except_table3665
- GCC_except_table3667
- GCC_except_table3670
- GCC_except_table3673
- GCC_except_table3675
- GCC_except_table3678
- GCC_except_table3681
- GCC_except_table3693
- GCC_except_table3695
- GCC_except_table3699
- GCC_except_table3703
- GCC_except_table3707
- GCC_except_table3751
- GCC_except_table3755
- GCC_except_table3758
- GCC_except_table3760
- GCC_except_table3762
- GCC_except_table3769
- GCC_except_table3770
- GCC_except_table3771
- GCC_except_table3852
- GCC_except_table3853
- GCC_except_table3854
- GCC_except_table3855
- GCC_except_table3857
- GCC_except_table3858
- GCC_except_table3859
- GCC_except_table3860
- GCC_except_table3861
- GCC_except_table3862
- GCC_except_table3863
- GCC_except_table3864
- GCC_except_table3865
- GCC_except_table3931
- GCC_except_table4041
- GCC_except_table4048
- GCC_except_table4090
- GCC_except_table4094
- GCC_except_table4097
- GCC_except_table4100
- GCC_except_table4103
- GCC_except_table4106
- GCC_except_table4109
- GCC_except_table4112
- GCC_except_table4115
- GCC_except_table4118
- GCC_except_table4123
- GCC_except_table4136
- GCC_except_table4141
- GCC_except_table4145
- GCC_except_table4147
- GCC_except_table4150
- GCC_except_table4161
- GCC_except_table4169
- GCC_except_table4173
- GCC_except_table4179
- GCC_except_table4180
- GCC_except_table4183
- GCC_except_table4184
- GCC_except_table4202
- GCC_except_table4204
- GCC_except_table4206
- GCC_except_table4207
- GCC_except_table4210
- GCC_except_table4219
- GCC_except_table4221
- GCC_except_table4227
- GCC_except_table4243
- GCC_except_table4254
- GCC_except_table4256
- GCC_except_table4265
- GCC_except_table4269
- GCC_except_table4275
- GCC_except_table4535
- GCC_except_table4541
- GCC_except_table4558
- GCC_except_table4562
- GCC_except_table4579
- GCC_except_table4585
- GCC_except_table4598
- GCC_except_table4612
- GCC_except_table4616
- GCC_except_table4729
- GCC_except_table494
- GCC_except_table504
- GCC_except_table518
- GCC_except_table5183
- GCC_except_table5191
- GCC_except_table5201
- GCC_except_table5243
- GCC_except_table5246
- GCC_except_table5247
- GCC_except_table5248
- GCC_except_table5249
- GCC_except_table526
- GCC_except_table5383
- GCC_except_table5384
- GCC_except_table5385
- GCC_except_table5386
- GCC_except_table5387
- GCC_except_table5388
- GCC_except_table5394
- GCC_except_table5395
- GCC_except_table5397
- GCC_except_table5404
- GCC_except_table5407
- GCC_except_table5409
- GCC_except_table5414
- GCC_except_table5417
- GCC_except_table5420
- GCC_except_table5424
- GCC_except_table5428
- GCC_except_table555
- GCC_except_table562
- GCC_except_table574
- GCC_except_table575
- GCC_except_table577
- GCC_except_table580
- GCC_except_table583
- GCC_except_table5914
- GCC_except_table5915
- GCC_except_table5934
- GCC_except_table5944
- GCC_except_table5947
- GCC_except_table595
- GCC_except_table5952
- GCC_except_table5955
- GCC_except_table5959
- GCC_except_table599
- GCC_except_table606
- GCC_except_table609
- GCC_except_table6228
- GCC_except_table6232
- GCC_except_table6277
- GCC_except_table6281
- GCC_except_table6283
- GCC_except_table6285
- GCC_except_table643
- GCC_except_table6477
- GCC_except_table6483
- GCC_except_table6487
- GCC_except_table6488
- GCC_except_table6489
- GCC_except_table6490
- GCC_except_table6496
- GCC_except_table6512
- GCC_except_table653
- GCC_except_table6547
- GCC_except_table6548
- GCC_except_table6549
- GCC_except_table6569
- GCC_except_table6581
- GCC_except_table6584
- GCC_except_table6589
- GCC_except_table6591
- GCC_except_table6605
- GCC_except_table661
- GCC_except_table6828
- GCC_except_table6841
- GCC_except_table6846
- GCC_except_table6849
- GCC_except_table6850
- GCC_except_table6852
- GCC_except_table6853
- GCC_except_table6855
- GCC_except_table688
- GCC_except_table6885
- GCC_except_table6907
- GCC_except_table6911
- GCC_except_table6915
- GCC_except_table692
- GCC_except_table6920
- GCC_except_table6924
- GCC_except_table6928
- GCC_except_table6932
- GCC_except_table6936
- GCC_except_table6944
- GCC_except_table6946
- GCC_except_table6948
- GCC_except_table695
- GCC_except_table697
- GCC_except_table703
- GCC_except_table705
- GCC_except_table7092
- GCC_except_table7122
- GCC_except_table718
- GCC_except_table7207
- GCC_except_table7208
- GCC_except_table7209
- GCC_except_table7210
- GCC_except_table7211
- GCC_except_table7212
- GCC_except_table7213
- GCC_except_table722
- GCC_except_table7275
- GCC_except_table7285
- GCC_except_table7286
- GCC_except_table7298
- GCC_except_table7304
- GCC_except_table7317
- GCC_except_table7320
- GCC_except_table7321
- GCC_except_table7326
- GCC_except_table7329
- GCC_except_table7336
- GCC_except_table7339
- GCC_except_table736
- GCC_except_table7360
- GCC_except_table7366
- GCC_except_table737
- GCC_except_table7375
- GCC_except_table7377
- GCC_except_table7381
- GCC_except_table7382
- GCC_except_table7389
- GCC_except_table7401
- GCC_except_table7410
- GCC_except_table742
- GCC_except_table7425
- GCC_except_table7426
- GCC_except_table7431
- GCC_except_table7435
- GCC_except_table7436
- GCC_except_table7439
- GCC_except_table7445
- GCC_except_table7449
- GCC_except_table745
- GCC_except_table7453
- GCC_except_table7455
- GCC_except_table7457
- GCC_except_table748
- GCC_except_table753
- GCC_except_table757
- GCC_except_table7576
- GCC_except_table7613
- GCC_except_table763
- GCC_except_table7670
- GCC_except_table7673
- GCC_except_table7677
- GCC_except_table7683
- GCC_except_table769
- GCC_except_table7690
- GCC_except_table7691
- GCC_except_table770
- GCC_except_table7707
- GCC_except_table7711
- GCC_except_table7712
- GCC_except_table7713
- GCC_except_table7762
- GCC_except_table7763
- GCC_except_table7765
- GCC_except_table7768
- GCC_except_table7795
- GCC_except_table7796
- GCC_except_table7801
- GCC_except_table7821
- GCC_except_table7839
- GCC_except_table7840
- GCC_except_table7841
- GCC_except_table7857
- GCC_except_table7872
- GCC_except_table7875
- GCC_except_table7882
- GCC_except_table7889
- GCC_except_table7894
- GCC_except_table7900
- GCC_except_table7912
- GCC_except_table7913
- GCC_except_table7918
- GCC_except_table7927
- GCC_except_table7933
- GCC_except_table7934
- GCC_except_table7940
- GCC_except_table7942
- GCC_except_table7946
- GCC_except_table796
- GCC_except_table7967
- GCC_except_table7969
- GCC_except_table7970
- GCC_except_table7996
- GCC_except_table803
- GCC_except_table810
- GCC_except_table811
- GCC_except_table8161
- GCC_except_table8224
- GCC_except_table8256
- GCC_except_table8259
- GCC_except_table839
- GCC_except_table8426
- GCC_except_table8464
- GCC_except_table8501
- GCC_except_table8576
- GCC_except_table8582
- GCC_except_table862
- GCC_except_table8630
- GCC_except_table8632
- GCC_except_table8634
- GCC_except_table8636
- GCC_except_table8638
- GCC_except_table8640
- GCC_except_table8642
- GCC_except_table8645
- GCC_except_table8647
- GCC_except_table8649
- GCC_except_table8651
- GCC_except_table8653
- GCC_except_table8656
- GCC_except_table8658
- GCC_except_table8660
- GCC_except_table8667
- GCC_except_table8673
- GCC_except_table8678
- GCC_except_table8681
- GCC_except_table8686
- GCC_except_table8691
- GCC_except_table8694
- GCC_except_table8697
- GCC_except_table8723
- GCC_except_table8727
- GCC_except_table8766
- GCC_except_table8767
- GCC_except_table8768
- GCC_except_table8771
- GCC_except_table8774
- GCC_except_table8775
- GCC_except_table8777
- GCC_except_table8780
- GCC_except_table8784
- GCC_except_table8785
- GCC_except_table880
- GCC_except_table8840
- GCC_except_table8847
- GCC_except_table8952
- GCC_except_table8971
- GCC_except_table8975
- GCC_except_table8977
- GCC_except_table8979
- GCC_except_table8982
- GCC_except_table8984
- GCC_except_table8986
- GCC_except_table8988
- GCC_except_table8989
- GCC_except_table8991
- GCC_except_table8993
- GCC_except_table8998
- GCC_except_table9000
- GCC_except_table9001
- GCC_except_table904
- GCC_except_table908
- GCC_except_table922
- GCC_except_table927
- _OBJC_IVAR_$_HAPAccessoryServerBrowserIP._maximumNumberOfPairVeifiesAllowed
- ___72-[HAPAccessoryServerHAP2Adapter accessoryServer:didFinishAuthWithError:]_block_invoke_2
- ___84-[HAPAccessoryServerHAP2Adapter accessoryServer:doesRequireSetupCodeWithCompletion:]_block_invoke_2
- ___86-[HAPAccessoryServerHAP2Adapter accessoryServer:validatePairingCert:model:completion:]_block_invoke_2
- ___90-[HAPAccessoryServerHAP2Adapter accessoryServer:confirmSoftwareAuthUUID:token:completion:]_block_invoke_2
- ___95-[HAPAccessoryServerHAP2Adapter accessoryServer:authenticateSoftwareAuthUUID:token:completion:]_block_invoke_2
- ___97-[HAPAccessoryServerHAP2Adapter accessoryServer:validateSoftwareAuthUUID:token:model:completion:]_block_invoke_2
- ___98-[HAPAccessoryServerHAP2Adapter accessoryServer:didRejectSetupCodeWithBackoffInterval:completion:]_block_invoke_2
- ___block_descriptor_40_e8_32bs_e41_v32?0"NSData"8"NSString"16"NSError"24ls32l8
- _logCategory._hmf_once_t854
- _logCategory._hmf_once_v855
- _swift_willThrowTypedImpl
CStrings:
+ "%@ Browser fast-set hasDiscoveryAdvertisement=%{public}d"
+ "%@/%u"
+ "%@@%.2fs"
+ "%{public}@"
+ "AES-CCM auth tag length must be one of "
+ "AES-CCM nonce length must be 7–13 bytes (got "
+ "AES-CCM-128 decryption failed"
+ "AES-CCM-128 decryption requires a "
+ "AES-CCM-128 decryption requires non-empty key, nonce, AAD, ciphertext, and auth tag"
+ "AdditionalWifiDataProxPairing"
+ "B32@?0@\"NSString\"8@\"HAPMetricsRacingRendezvous\"16^B24"
+ "Background ECDSA pairing key save hit a transient keychain error, retrying once"
+ "Background persist of ECDSA pairing key FAILED after announcing success (lostDuplicateRace=%{public}@, domain=%{public}@, code=%ld); accessory will need to re-pair"
+ "Delegate does not support promptUncertifiedForMFiRollError; failing pair-setup"
+ "ECDSA pairing key already exists for peer; reporting already-paired"
+ "HAP2 stall: op '%@' waited=%.2fs unfinishedDeps=%lu executing=%lu queued=%lu suspended=%d maxConcurrent=%ld runQoS=%@ reqQoS=%@ queueQoS=%@ longestRunning=[%@]"
+ "HK ECDSA Privacy v1 BPK"
+ "Including AdditionalWifiData in M5 encrypted data (%ld bytes)"
+ "Injected prefetched MFi token (%ld bytes); starting validate+roll"
+ "Injecting prefetched MFi token into SPAKE2+ session"
+ "MFi: delegate accepted not-certified pair after roll error; resuming M5 with echoed token"
+ "MFi: delegate declined not-certified pair; propagating original error"
+ "MFi: prompt resolved after teardown — discarding"
+ "NFC pair-setup failed"
+ "Not resuming a pending bulk operation while one is already current"
+ "SPAKE2+ session asking delegate whether to prompt user after MFi roll error: %{public}@/%ld"
+ "Stashing prefetched MFi token (%lu bytes)"
+ "[%{public}@] Background ECDSA pairing key save hit a transient keychain error, retrying once"
+ "[%{public}@] Background persist of ECDSA pairing key FAILED after announcing success (lostDuplicateRace=%{public}@, domain=%{public}@, code=%ld); accessory will need to re-pair"
+ "[%{public}@] Delegate does not support promptUncertifiedForMFiRollError; failing pair-setup"
+ "[%{public}@] ECDSA pairing key already exists for peer; reporting already-paired"
+ "[%{public}@] Injecting prefetched MFi token into SPAKE2+ session"
+ "[%{public}@] Not resuming a pending bulk operation while one is already current"
+ "[%{public}@] SPAKE2+ session asking delegate whether to prompt user after MFi roll error: %{public}@/%ld"
+ "[%{public}@] Stashing prefetched MFi token (%lu bytes)"
+ "[%{public}@] [Timing] NFC duplicate existence-check: %.2fms"
+ "[%{public}@] [Timing] Pair-setup(NFC+keysave) complete (background): %.2fms"
+ "[Timing] NFC duplicate existence-check: %.2fms"
+ "[Timing] Pair-setup(NFC+keysave) complete (background): %.2fms"
+ "d8@?0"
+ "v16@?0@\"HAPMetricsRacingRendezvous\"8"
+ "v40@?0@\"NSData\"8@\"NSString\"16@\"HAPAdditionalWifiData\"24@\"NSError\"32"
- "Failed to save ECDSA pairing key to keystore: %@"
- "Injected prefetched MFi token (%ld bytes); starting parallel validate+roll"
- "Injecting prefetched MFi token into SPAKE2+ session for parallel validate+roll"
- "Pair-setup(NFC+keysave) complete"
- "Stashing prefetched MFi token (%lu bytes) for parallel validate+roll"
- "[%{public}@] Failed to save ECDSA pairing key to keystore: %@"
- "[%{public}@] Injecting prefetched MFi token into SPAKE2+ session for parallel validate+roll"
- "[%{public}@] Stashing prefetched MFi token (%lu bytes) for parallel validate+roll"
- "p256NistKdfCmacAes128Sha256 not yet supported"
- "v32@?0@\"NSData\"8@\"NSString\"16@\"NSError\"24"

```
