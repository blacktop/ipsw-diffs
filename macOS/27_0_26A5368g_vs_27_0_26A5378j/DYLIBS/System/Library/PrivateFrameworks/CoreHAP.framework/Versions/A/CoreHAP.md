## CoreHAP

> `/System/Library/PrivateFrameworks/CoreHAP.framework/Versions/A/CoreHAP`

```diff

-  __TEXT.__text: 0x213270
-  __TEXT.__objc_methlist: 0x16e08
+  __TEXT.__text: 0x2159e0
+  __TEXT.__objc_methlist: 0x17000
   __TEXT.__const: 0x7e0
-  __TEXT.__gcc_except_tab: 0x5568
-  __TEXT.__cstring: 0x134d2
-  __TEXT.__oslogstring: 0x38f33
-  __TEXT.__unwind_info: 0x6870
+  __TEXT.__gcc_except_tab: 0x55f0
+  __TEXT.__cstring: 0x135e5
+  __TEXT.__oslogstring: 0x3900a
+  __TEXT.__unwind_info: 0x6938
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x20f0
-  __DATA_CONST.__objc_classlist: 0xb98
+  __DATA_CONST.__const: 0x2110
+  __DATA_CONST.__objc_classlist: 0xba8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x338
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7740
+  __DATA_CONST.__objc_selrefs: 0x7878
   __DATA_CONST.__objc_protorefs: 0xc0
-  __DATA_CONST.__objc_superrefs: 0xa10
+  __DATA_CONST.__objc_superrefs: 0xa20
   __DATA_CONST.__objc_arraydata: 0x200
-  __DATA_CONST.__got: 0xd30
-  __AUTH_CONST.__const: 0x4400
-  __AUTH_CONST.__cfstring: 0xf560
-  __AUTH_CONST.__objc_const: 0x288e8
+  __DATA_CONST.__got: 0xd88
+  __AUTH_CONST.__const: 0x4500
+  __AUTH_CONST.__cfstring: 0xf5c0
+  __AUTH_CONST.__objc_const: 0x28c58
   __AUTH_CONST.__objc_intobj: 0x570
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0xc0
-  __AUTH_CONST.__auth_got: 0x948
-  __AUTH.__objc_data: 0x6450
+  __AUTH_CONST.__auth_got: 0x980
+  __AUTH.__objc_data: 0x64f0
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x28
-  __DATA.__objc_ivar: 0x177c
+  __DATA.__objc_ivar: 0x17a8
   __DATA.__data: 0x26c2
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x398
+  __DATA.__bss: 0x388
   __DATA_DIRTY.__objc_data: 0xfa0
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x58
+  __DATA_DIRTY.__bss: 0x78
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8584
-  Symbols:   19009
-  CStrings:  8163
+  Functions: 8638
+  Symbols:   19144
+  CStrings:  8176
 
Sections:
~ __TEXT.__const : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_floatobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__thread_vars : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
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
+ GCC_except_table1054
+ GCC_except_table1056
+ GCC_except_table1167
+ GCC_except_table1171
+ GCC_except_table1184
+ GCC_except_table1198
+ GCC_except_table1200
+ GCC_except_table1202
+ GCC_except_table1204
+ GCC_except_table1330
+ GCC_except_table1336
+ GCC_except_table1338
+ GCC_except_table1536
+ GCC_except_table1746
+ GCC_except_table1751
+ GCC_except_table1757
+ GCC_except_table1759
+ GCC_except_table1765
+ GCC_except_table1771
+ GCC_except_table1779
+ GCC_except_table1781
+ GCC_except_table1783
+ GCC_except_table1788
+ GCC_except_table1802
+ GCC_except_table1810
+ GCC_except_table1817
+ GCC_except_table1821
+ GCC_except_table1825
+ GCC_except_table1830
+ GCC_except_table1868
+ GCC_except_table1989
+ GCC_except_table1991
+ GCC_except_table2002
+ GCC_except_table2004
+ GCC_except_table2008
+ GCC_except_table2011
+ GCC_except_table2013
+ GCC_except_table2018
+ GCC_except_table2035
+ GCC_except_table2053
+ GCC_except_table2057
+ GCC_except_table2059
+ GCC_except_table2062
+ GCC_except_table2067
+ GCC_except_table2069
+ GCC_except_table2071
+ GCC_except_table2075
+ GCC_except_table2081
+ GCC_except_table2089
+ GCC_except_table2102
+ GCC_except_table2129
+ GCC_except_table2130
+ GCC_except_table2152
+ GCC_except_table2160
+ GCC_except_table2168
+ GCC_except_table235
+ GCC_except_table2371
+ GCC_except_table2379
+ GCC_except_table2380
+ GCC_except_table2381
+ GCC_except_table2382
+ GCC_except_table2384
+ GCC_except_table2400
+ GCC_except_table2414
+ GCC_except_table245
+ GCC_except_table246
+ GCC_except_table249
+ GCC_except_table2494
+ GCC_except_table2506
+ GCC_except_table252
+ GCC_except_table263
+ GCC_except_table265
+ GCC_except_table266
+ GCC_except_table269
+ GCC_except_table2696
+ GCC_except_table2705
+ GCC_except_table273
+ GCC_except_table2755
+ GCC_except_table2771
+ GCC_except_table2773
+ GCC_except_table2785
+ GCC_except_table2792
+ GCC_except_table2808
+ GCC_except_table282
+ GCC_except_table2822
+ GCC_except_table2823
+ GCC_except_table2824
+ GCC_except_table2836
+ GCC_except_table2843
+ GCC_except_table2846
+ GCC_except_table2851
+ GCC_except_table2856
+ GCC_except_table288
+ GCC_except_table2896
+ GCC_except_table2910
+ GCC_except_table2913
+ GCC_except_table2918
+ GCC_except_table2920
+ GCC_except_table2936
+ GCC_except_table2952
+ GCC_except_table2958
+ GCC_except_table2966
+ GCC_except_table2974
+ GCC_except_table3038
+ GCC_except_table3045
+ GCC_except_table3047
+ GCC_except_table3048
+ GCC_except_table3071
+ GCC_except_table3091
+ GCC_except_table3319
+ GCC_except_table3386
+ GCC_except_table3387
+ GCC_except_table3391
+ GCC_except_table3394
+ GCC_except_table3396
+ GCC_except_table3397
+ GCC_except_table3401
+ GCC_except_table3402
+ GCC_except_table3404
+ GCC_except_table3411
+ GCC_except_table3421
+ GCC_except_table3424
+ GCC_except_table3436
+ GCC_except_table3440
+ GCC_except_table3446
+ GCC_except_table3448
+ GCC_except_table3451
+ GCC_except_table3454
+ GCC_except_table3466
+ GCC_except_table3468
+ GCC_except_table3472
+ GCC_except_table3480
+ GCC_except_table3506
+ GCC_except_table3529
+ GCC_except_table3535
+ GCC_except_table3539
+ GCC_except_table3543
+ GCC_except_table3545
+ GCC_except_table3548
+ GCC_except_table3550
+ GCC_except_table3552
+ GCC_except_table3559
+ GCC_except_table3560
+ GCC_except_table3561
+ GCC_except_table3645
+ GCC_except_table3653
+ GCC_except_table3678
+ GCC_except_table3681
+ GCC_except_table3686
+ GCC_except_table3694
+ GCC_except_table3700
+ GCC_except_table3702
+ GCC_except_table3712
+ GCC_except_table3735
+ GCC_except_table3741
+ GCC_except_table3786
+ GCC_except_table3787
+ GCC_except_table3788
+ GCC_except_table3789
+ GCC_except_table3790
+ GCC_except_table3791
+ GCC_except_table3792
+ GCC_except_table3793
+ GCC_except_table3794
+ GCC_except_table3795
+ GCC_except_table3796
+ GCC_except_table3797
+ GCC_except_table3798
+ GCC_except_table3799
+ GCC_except_table3852
+ GCC_except_table3947
+ GCC_except_table3954
+ GCC_except_table3996
+ GCC_except_table4000
+ GCC_except_table4003
+ GCC_except_table4006
+ GCC_except_table4009
+ GCC_except_table4012
+ GCC_except_table4015
+ GCC_except_table4018
+ GCC_except_table4024
+ GCC_except_table4029
+ GCC_except_table4040
+ GCC_except_table4044
+ GCC_except_table4046
+ GCC_except_table4049
+ GCC_except_table4060
+ GCC_except_table4068
+ GCC_except_table4075
+ GCC_except_table4081
+ GCC_except_table4082
+ GCC_except_table4085
+ GCC_except_table4086
+ GCC_except_table4104
+ GCC_except_table4106
+ GCC_except_table4108
+ GCC_except_table4109
+ GCC_except_table4112
+ GCC_except_table4118
+ GCC_except_table4121
+ GCC_except_table4123
+ GCC_except_table4129
+ GCC_except_table4131
+ GCC_except_table4134
+ GCC_except_table4145
+ GCC_except_table4156
+ GCC_except_table4158
+ GCC_except_table4167
+ GCC_except_table4169
+ GCC_except_table4171
+ GCC_except_table4177
+ GCC_except_table4437
+ GCC_except_table4443
+ GCC_except_table4460
+ GCC_except_table4464
+ GCC_except_table4481
+ GCC_except_table4489
+ GCC_except_table4502
+ GCC_except_table4516
+ GCC_except_table4520
+ GCC_except_table4633
+ GCC_except_table5089
+ GCC_except_table5097
+ GCC_except_table5108
+ GCC_except_table5150
+ GCC_except_table5154
+ GCC_except_table5155
+ GCC_except_table5156
+ GCC_except_table518
+ GCC_except_table5238
+ GCC_except_table5239
+ GCC_except_table5240
+ GCC_except_table5241
+ GCC_except_table5242
+ GCC_except_table5243
+ GCC_except_table5249
+ GCC_except_table5250
+ GCC_except_table5252
+ GCC_except_table5259
+ GCC_except_table5262
+ GCC_except_table5264
+ GCC_except_table5269
+ GCC_except_table5272
+ GCC_except_table5275
+ GCC_except_table5279
+ GCC_except_table5283
+ GCC_except_table532
+ GCC_except_table548
+ GCC_except_table560
+ GCC_except_table5769
+ GCC_except_table5770
+ GCC_except_table5789
+ GCC_except_table5799
+ GCC_except_table5802
+ GCC_except_table5807
+ GCC_except_table5810
+ GCC_except_table5814
+ GCC_except_table594
+ GCC_except_table606
+ GCC_except_table607
+ GCC_except_table6083
+ GCC_except_table6087
+ GCC_except_table609
+ GCC_except_table612
+ GCC_except_table6132
+ GCC_except_table6136
+ GCC_except_table6138
+ GCC_except_table6140
+ GCC_except_table615
+ GCC_except_table629
+ GCC_except_table633
+ GCC_except_table6334
+ GCC_except_table6338
+ GCC_except_table6339
+ GCC_except_table6340
+ GCC_except_table6341
+ GCC_except_table6347
+ GCC_except_table636
+ GCC_except_table6363
+ GCC_except_table6396
+ GCC_except_table6397
+ GCC_except_table6398
+ GCC_except_table6418
+ GCC_except_table643
+ GCC_except_table6430
+ GCC_except_table6433
+ GCC_except_table6438
+ GCC_except_table6440
+ GCC_except_table6454
+ GCC_except_table646
+ GCC_except_table6688
+ GCC_except_table669
+ GCC_except_table6701
+ GCC_except_table6706
+ GCC_except_table6709
+ GCC_except_table6710
+ GCC_except_table6712
+ GCC_except_table6713
+ GCC_except_table6715
+ GCC_except_table6745
+ GCC_except_table6767
+ GCC_except_table6771
+ GCC_except_table6775
+ GCC_except_table6780
+ GCC_except_table6784
+ GCC_except_table6788
+ GCC_except_table6792
+ GCC_except_table6796
+ GCC_except_table6804
+ GCC_except_table6806
+ GCC_except_table6810
+ GCC_except_table686
+ GCC_except_table6873
+ GCC_except_table6874
+ GCC_except_table6875
+ GCC_except_table6876
+ GCC_except_table6877
+ GCC_except_table6878
+ GCC_except_table6879
+ GCC_except_table6938
+ GCC_except_table6942
+ GCC_except_table6955
+ GCC_except_table6961
+ GCC_except_table6974
+ GCC_except_table6977
+ GCC_except_table6983
+ GCC_except_table6993
+ GCC_except_table6996
+ GCC_except_table7010
+ GCC_except_table7017
+ GCC_except_table7023
+ GCC_except_table7032
+ GCC_except_table7034
+ GCC_except_table7040
+ GCC_except_table7041
+ GCC_except_table7048
+ GCC_except_table7060
+ GCC_except_table7069
+ GCC_except_table7084
+ GCC_except_table7085
+ GCC_except_table7090
+ GCC_except_table7094
+ GCC_except_table7095
+ GCC_except_table7098
+ GCC_except_table7104
+ GCC_except_table7108
+ GCC_except_table7112
+ GCC_except_table7114
+ GCC_except_table7116
+ GCC_except_table7120
+ GCC_except_table713
+ GCC_except_table720
+ GCC_except_table722
+ GCC_except_table7234
+ GCC_except_table7271
+ GCC_except_table7330
+ GCC_except_table7334
+ GCC_except_table734
+ GCC_except_table7340
+ GCC_except_table7347
+ GCC_except_table7348
+ GCC_except_table736
+ GCC_except_table7364
+ GCC_except_table7368
+ GCC_except_table7369
+ GCC_except_table7370
+ GCC_except_table7419
+ GCC_except_table7420
+ GCC_except_table7422
+ GCC_except_table7425
+ GCC_except_table7452
+ GCC_except_table7453
+ GCC_except_table7458
+ GCC_except_table7478
+ GCC_except_table7496
+ GCC_except_table7497
+ GCC_except_table7498
+ GCC_except_table7507
+ GCC_except_table7512
+ GCC_except_table7513
+ GCC_except_table7514
+ GCC_except_table7529
+ GCC_except_table7532
+ GCC_except_table7539
+ GCC_except_table7546
+ GCC_except_table7551
+ GCC_except_table7557
+ GCC_except_table7569
+ GCC_except_table7570
+ GCC_except_table7575
+ GCC_except_table7584
+ GCC_except_table7592
+ GCC_except_table7593
+ GCC_except_table7597
+ GCC_except_table7599
+ GCC_except_table7601
+ GCC_except_table7605
+ GCC_except_table761
+ GCC_except_table7626
+ GCC_except_table7628
+ GCC_except_table7629
+ GCC_except_table7655
+ GCC_except_table776
+ GCC_except_table777
+ GCC_except_table7819
+ GCC_except_table782
+ GCC_except_table785
+ GCC_except_table788
+ GCC_except_table7882
+ GCC_except_table7914
+ GCC_except_table7917
+ GCC_except_table793
+ GCC_except_table797
+ GCC_except_table807
+ GCC_except_table808
+ GCC_except_table8084
+ GCC_except_table8122
+ GCC_except_table8159
+ GCC_except_table8226
+ GCC_except_table8228
+ GCC_except_table8232
+ GCC_except_table8236
+ GCC_except_table8238
+ GCC_except_table8240
+ GCC_except_table8242
+ GCC_except_table8244
+ GCC_except_table8246
+ GCC_except_table8249
+ GCC_except_table8251
+ GCC_except_table8275
+ GCC_except_table8278
+ GCC_except_table8304
+ GCC_except_table8307
+ GCC_except_table8308
+ GCC_except_table8328
+ GCC_except_table8329
+ GCC_except_table8331
+ GCC_except_table8332
+ GCC_except_table8335
+ GCC_except_table8336
+ GCC_except_table8338
+ GCC_except_table8339
+ GCC_except_table834
+ GCC_except_table8341
+ GCC_except_table8345
+ GCC_except_table8346
+ GCC_except_table8350
+ GCC_except_table8401
+ GCC_except_table8408
+ GCC_except_table841
+ GCC_except_table848
+ GCC_except_table8509
+ GCC_except_table8511
+ GCC_except_table8513
+ GCC_except_table8516
+ GCC_except_table8518
+ GCC_except_table8520
+ GCC_except_table8522
+ GCC_except_table8523
+ GCC_except_table8525
+ GCC_except_table8529
+ GCC_except_table8534
+ GCC_except_table865
+ GCC_except_table887
+ GCC_except_table905
+ GCC_except_table927
+ GCC_except_table93
+ GCC_except_table931
+ GCC_except_table945
+ GCC_except_table950
+ OBJC_IVAR_$_HAP2AsynchronousOperation._enqueueMachTime
+ OBJC_IVAR_$_HAP2AsynchronousOperation._executeStartMachTime
+ OBJC_IVAR_$_HAP2AsynchronousOperation._owningQueue
+ OBJC_IVAR_$_HAP2AsynchronousOperation._unfinishedDependencyCount
+ OBJC_IVAR_$_HAP2Diagnostics._observer
+ OBJC_IVAR_$_HAPAccessoryServerBrowserIP._maximumNumberOfPairVerifiesAllowed
+ OBJC_IVAR_$_HAPMetricsDispatcher._lastRacingSweepUptime
+ OBJC_IVAR_$_HAPMetricsDispatcher._racingRendezvousByKey
+ OBJC_IVAR_$_HAPMetricsDispatcher._uptimeProvider
+ OBJC_IVAR_$_HAPMetricsRacingRendezvous._handler
+ OBJC_IVAR_$_HAPMetricsRacingRendezvous._insertUptime
+ OBJC_IVAR_$_HAPMetricsRacingRendezvous._racingResult
+ _HAP2OperationSecondsSinceMachTime
+ _HMFQualityOfServiceClassToString
+ _HMFQualityOfServiceToString
+ _OBJC_CLASS_$_HAP2Diagnostics
+ _OBJC_CLASS_$_HAPMetricsRacingRendezvous
+ _OBJC_METACLASS_$_HAP2Diagnostics
+ _OBJC_METACLASS_$_HAPMetricsRacingRendezvous
+ __72-[HAPAccessoryServerHAP2Adapter accessoryServer:didFinishAuthWithError:]_block_invoke
+ __84-[HAPAccessoryServerHAP2Adapter accessoryServer:doesRequireSetupCodeWithCompletion:]_block_invoke
+ __86-[HAPAccessoryServerHAP2Adapter accessoryServer:validatePairingCert:model:completion:]_block_invoke
+ __90-[HAPAccessoryServerHAP2Adapter accessoryServer:confirmSoftwareAuthUUID:token:completion:]_block_invoke
+ __95-[HAPAccessoryServerHAP2Adapter accessoryServer:authenticateSoftwareAuthUUID:token:completion:]_block_invoke
+ __97-[HAPAccessoryServerHAP2Adapter accessoryServer:validateSoftwareAuthUUID:token:model:completion:]_block_invoke
+ __98-[HAPAccessoryServerHAP2Adapter accessoryServer:didRejectSetupCodeWithBackoffInterval:completion:]_block_invoke
+ __OBJC_$_CLASS_METHODS_HAP2Diagnostics
+ __OBJC_$_CLASS_PROP_LIST_HAP2Diagnostics
+ __OBJC_$_INSTANCE_METHODS_HAP2Diagnostics
+ __OBJC_$_INSTANCE_METHODS_HAPMetricsRacingRendezvous
+ __OBJC_$_INSTANCE_VARIABLES_HAP2Diagnostics
+ __OBJC_$_INSTANCE_VARIABLES_HAPMetricsRacingRendezvous
+ __OBJC_$_PROP_LIST_HAP2Diagnostics
+ __OBJC_$_PROP_LIST_HAPMetricsRacingRendezvous
+ __OBJC_CLASS_RO_$_HAP2Diagnostics
+ __OBJC_CLASS_RO_$_HAPMetricsRacingRendezvous
+ __OBJC_METACLASS_RO_$_HAP2Diagnostics
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
+ ___77-[HAPMetricsDispatcher deliverRacingResult:forAccessoryIdentifier:messageID:]_block_invoke
+ ___79-[HAPMetricsDispatcher _evictExpiredRacingRendezvousAtUptime:orphanedHandlers:]_block_invoke
+ ___82-[HAPMetricsDispatcher awaitRacingResultForAccessoryIdentifier:messageID:handler:]_block_invoke
+ ___83-[HAPMetricsDispatcher _matchedRacingHandlerForRendezvous:forIdentifier:messageID:]_block_invoke
+ ___block_descriptor_32_e5_d8?0l
+ ___block_descriptor_40_e8_32bs_e36_v16?0"HAPMetricsRacingRendezvous"8l
+ ___block_descriptor_40_e8_32s_e36_v16?0"HAPMetricsRacingRendezvous"8l
+ ___block_descriptor_48_e8_32s_e28_v32?0"NSOperation"8Q16^B24l
+ ___block_descriptor_48_e8_32s_e53_B32?0"NSString"8"HAPMetricsRacingRendezvous"16^B24l
+ _mach_continuous_time
+ _mach_timebase_info
+ _objc_msgSend$_browserFastSetHasDiscoveryAdvertisement:
+ _objc_msgSend$_evictExpiredRacingRendezvousAtUptime:orphanedHandlers:
+ _objc_msgSend$_isExpiredRendezvous:atUptime:
+ _objc_msgSend$_matchedRacingHandlerForRendezvous:forIdentifier:messageID:
+ _objc_msgSend$_racingKeyForIdentifier:messageID:
+ _objc_msgSend$_racingRendezvousForIdentifier:messageID:atUptime:orphanedHandlers:
+ _objc_msgSend$_stampDiagnosticsOnOperations:
+ _objc_msgSend$_updateRacingRendezvousForIdentifier:messageID:withBlock:
+ _objc_msgSend$enqueueMachTime
+ _objc_msgSend$executeStartMachTime
+ _objc_msgSend$hap2DiagnosticsDidObserveOperationQueueStallWithSnapshot:
+ _objc_msgSend$initWithInsertUptime:
+ _objc_msgSend$insertUptime
+ _objc_msgSend$keysOfEntriesPassingTest:
+ _objc_msgSend$lastRacingSweepUptime
+ _objc_msgSend$maxConcurrentOperationCount
+ _objc_msgSend$notifyOperationQueueStallWithSnapshot:
+ _objc_msgSend$observer
+ _objc_msgSend$owningQueue
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
+ logCategory._hmf_once_t804
+ logCategory._hmf_once_v805
+ sharedDiagnostics.onceToken
+ sharedDiagnostics.sharedDiagnostics
- -[HAPAccessoryServerBrowserIP maximumNumberOfPairVeifiesAllowed]
- GCC_except_table1016
- GCC_except_table1018
- GCC_except_table1124
- GCC_except_table1129
- GCC_except_table1133
- GCC_except_table1146
- GCC_except_table1160
- GCC_except_table1164
- GCC_except_table1166
- GCC_except_table1292
- GCC_except_table1298
- GCC_except_table1300
- GCC_except_table1513
- GCC_except_table1721
- GCC_except_table1723
- GCC_except_table1728
- GCC_except_table1734
- GCC_except_table1736
- GCC_except_table1742
- GCC_except_table1748
- GCC_except_table1752
- GCC_except_table1754
- GCC_except_table1756
- GCC_except_table1758
- GCC_except_table1763
- GCC_except_table1785
- GCC_except_table1796
- GCC_except_table1800
- GCC_except_table1805
- GCC_except_table1843
- GCC_except_table1958
- GCC_except_table1963
- GCC_except_table1964
- GCC_except_table1966
- GCC_except_table1968
- GCC_except_table1977
- GCC_except_table1979
- GCC_except_table1986
- GCC_except_table2010
- GCC_except_table2017
- GCC_except_table2019
- GCC_except_table2021
- GCC_except_table2025
- GCC_except_table2028
- GCC_except_table2032
- GCC_except_table2034
- GCC_except_table2037
- GCC_except_table205
- GCC_except_table2056
- GCC_except_table206
- GCC_except_table2064
- GCC_except_table2077
- GCC_except_table2104
- GCC_except_table2105
- GCC_except_table2127
- GCC_except_table2135
- GCC_except_table2143
- GCC_except_table216
- GCC_except_table217
- GCC_except_table220
- GCC_except_table223
- GCC_except_table230
- GCC_except_table2340
- GCC_except_table2348
- GCC_except_table2349
- GCC_except_table2350
- GCC_except_table2351
- GCC_except_table2352
- GCC_except_table2353
- GCC_except_table236
- GCC_except_table2369
- GCC_except_table237
- GCC_except_table240
- GCC_except_table244
- GCC_except_table2463
- GCC_except_table2475
- GCC_except_table2500
- GCC_except_table2508
- GCC_except_table2519
- GCC_except_table253
- GCC_except_table2533
- GCC_except_table2536
- GCC_except_table2541
- GCC_except_table2550
- GCC_except_table2556
- GCC_except_table2558
- GCC_except_table2738
- GCC_except_table2747
- GCC_except_table2797
- GCC_except_table2813
- GCC_except_table2815
- GCC_except_table2834
- GCC_except_table2850
- GCC_except_table2864
- GCC_except_table2865
- GCC_except_table2866
- GCC_except_table2869
- GCC_except_table2877
- GCC_except_table2884
- GCC_except_table2887
- GCC_except_table2892
- GCC_except_table2897
- GCC_except_table2937
- GCC_except_table2951
- GCC_except_table2959
- GCC_except_table2961
- GCC_except_table2977
- GCC_except_table2993
- GCC_except_table2995
- GCC_except_table2999
- GCC_except_table3007
- GCC_except_table3015
- GCC_except_table3079
- GCC_except_table3086
- GCC_except_table3088
- GCC_except_table3089
- GCC_except_table3112
- GCC_except_table3132
- GCC_except_table3360
- GCC_except_table3427
- GCC_except_table3428
- GCC_except_table3432
- GCC_except_table3437
- GCC_except_table3442
- GCC_except_table3445
- GCC_except_table3452
- GCC_except_table3462
- GCC_except_table3465
- GCC_except_table3477
- GCC_except_table3479
- GCC_except_table3481
- GCC_except_table3484
- GCC_except_table3487
- GCC_except_table3489
- GCC_except_table3492
- GCC_except_table3495
- GCC_except_table3507
- GCC_except_table3509
- GCC_except_table3513
- GCC_except_table3517
- GCC_except_table3521
- GCC_except_table3547
- GCC_except_table3565
- GCC_except_table3569
- GCC_except_table3572
- GCC_except_table3574
- GCC_except_table3576
- GCC_except_table3583
- GCC_except_table3584
- GCC_except_table3585
- GCC_except_table3662
- GCC_except_table3663
- GCC_except_table3665
- GCC_except_table3666
- GCC_except_table3667
- GCC_except_table3668
- GCC_except_table3669
- GCC_except_table3670
- GCC_except_table3671
- GCC_except_table3672
- GCC_except_table3673
- GCC_except_table3674
- GCC_except_table3675
- GCC_except_table3728
- GCC_except_table3823
- GCC_except_table3830
- GCC_except_table3872
- GCC_except_table3876
- GCC_except_table3879
- GCC_except_table3882
- GCC_except_table3885
- GCC_except_table3888
- GCC_except_table3891
- GCC_except_table3894
- GCC_except_table3897
- GCC_except_table3900
- GCC_except_table3905
- GCC_except_table3916
- GCC_except_table3920
- GCC_except_table3922
- GCC_except_table3925
- GCC_except_table3936
- GCC_except_table3944
- GCC_except_table3951
- GCC_except_table3957
- GCC_except_table3958
- GCC_except_table3961
- GCC_except_table3962
- GCC_except_table3980
- GCC_except_table3982
- GCC_except_table3984
- GCC_except_table3985
- GCC_except_table3988
- GCC_except_table3994
- GCC_except_table3997
- GCC_except_table3999
- GCC_except_table4005
- GCC_except_table4007
- GCC_except_table4010
- GCC_except_table4032
- GCC_except_table4034
- GCC_except_table4043
- GCC_except_table4045
- GCC_except_table4047
- GCC_except_table4053
- GCC_except_table4313
- GCC_except_table4319
- GCC_except_table4336
- GCC_except_table4340
- GCC_except_table4357
- GCC_except_table4365
- GCC_except_table4378
- GCC_except_table4392
- GCC_except_table4396
- GCC_except_table4509
- GCC_except_table478
- GCC_except_table493
- GCC_except_table4963
- GCC_except_table4971
- GCC_except_table4982
- GCC_except_table5024
- GCC_except_table5027
- GCC_except_table5028
- GCC_except_table5029
- GCC_except_table5030
- GCC_except_table509
- GCC_except_table5112
- GCC_except_table5113
- GCC_except_table5114
- GCC_except_table5115
- GCC_except_table5116
- GCC_except_table5117
- GCC_except_table5123
- GCC_except_table5124
- GCC_except_table5126
- GCC_except_table5133
- GCC_except_table5136
- GCC_except_table5138
- GCC_except_table5143
- GCC_except_table5146
- GCC_except_table5149
- GCC_except_table5157
- GCC_except_table522
- GCC_except_table556
- GCC_except_table5643
- GCC_except_table5644
- GCC_except_table5663
- GCC_except_table5673
- GCC_except_table5676
- GCC_except_table568
- GCC_except_table5681
- GCC_except_table5684
- GCC_except_table5688
- GCC_except_table569
- GCC_except_table571
- GCC_except_table574
- GCC_except_table577
- GCC_except_table591
- GCC_except_table595
- GCC_except_table5957
- GCC_except_table5961
- GCC_except_table598
- GCC_except_table6006
- GCC_except_table6010
- GCC_except_table6012
- GCC_except_table6014
- GCC_except_table605
- GCC_except_table608
- GCC_except_table6202
- GCC_except_table6208
- GCC_except_table6212
- GCC_except_table6213
- GCC_except_table6214
- GCC_except_table6215
- GCC_except_table6221
- GCC_except_table6237
- GCC_except_table6270
- GCC_except_table6271
- GCC_except_table6272
- GCC_except_table6292
- GCC_except_table6304
- GCC_except_table6307
- GCC_except_table631
- GCC_except_table6312
- GCC_except_table6314
- GCC_except_table641
- GCC_except_table648
- GCC_except_table6562
- GCC_except_table6575
- GCC_except_table6580
- GCC_except_table6583
- GCC_except_table6584
- GCC_except_table6586
- GCC_except_table6587
- GCC_except_table6589
- GCC_except_table6619
- GCC_except_table6641
- GCC_except_table6645
- GCC_except_table6649
- GCC_except_table6654
- GCC_except_table6658
- GCC_except_table6662
- GCC_except_table6666
- GCC_except_table6670
- GCC_except_table6678
- GCC_except_table6680
- GCC_except_table6684
- GCC_except_table6747
- GCC_except_table6748
- GCC_except_table6749
- GCC_except_table675
- GCC_except_table6750
- GCC_except_table6751
- GCC_except_table6752
- GCC_except_table6753
- GCC_except_table6812
- GCC_except_table6816
- GCC_except_table6817
- GCC_except_table682
- GCC_except_table6829
- GCC_except_table6835
- GCC_except_table684
- GCC_except_table6848
- GCC_except_table6851
- GCC_except_table6852
- GCC_except_table6857
- GCC_except_table6860
- GCC_except_table6867
- GCC_except_table6870
- GCC_except_table6884
- GCC_except_table6891
- GCC_except_table6897
- GCC_except_table6906
- GCC_except_table6908
- GCC_except_table6914
- GCC_except_table6915
- GCC_except_table6922
- GCC_except_table6934
- GCC_except_table6958
- GCC_except_table6959
- GCC_except_table696
- GCC_except_table6964
- GCC_except_table6968
- GCC_except_table6969
- GCC_except_table6972
- GCC_except_table698
- GCC_except_table6982
- GCC_except_table6988
- GCC_except_table6990
- GCC_except_table6994
- GCC_except_table7109
- GCC_except_table7146
- GCC_except_table7202
- GCC_except_table7205
- GCC_except_table7209
- GCC_except_table7215
- GCC_except_table7222
- GCC_except_table7223
- GCC_except_table723
- GCC_except_table7239
- GCC_except_table7243
- GCC_except_table7244
- GCC_except_table7245
- GCC_except_table727
- GCC_except_table7294
- GCC_except_table7295
- GCC_except_table7297
- GCC_except_table7300
- GCC_except_table7328
- GCC_except_table7333
- GCC_except_table7353
- GCC_except_table7371
- GCC_except_table7372
- GCC_except_table7373
- GCC_except_table738
- GCC_except_table7382
- GCC_except_table7387
- GCC_except_table7388
- GCC_except_table7389
- GCC_except_table739
- GCC_except_table7404
- GCC_except_table7407
- GCC_except_table7414
- GCC_except_table7421
- GCC_except_table7426
- GCC_except_table7432
- GCC_except_table744
- GCC_except_table7444
- GCC_except_table7445
- GCC_except_table7450
- GCC_except_table7459
- GCC_except_table7467
- GCC_except_table7468
- GCC_except_table747
- GCC_except_table7472
- GCC_except_table7474
- GCC_except_table7476
- GCC_except_table7480
- GCC_except_table750
- GCC_except_table7501
- GCC_except_table7503
- GCC_except_table7504
- GCC_except_table7530
- GCC_except_table759
- GCC_except_table769
- GCC_except_table7694
- GCC_except_table770
- GCC_except_table7757
- GCC_except_table7789
- GCC_except_table7792
- GCC_except_table7959
- GCC_except_table796
- GCC_except_table7997
- GCC_except_table8034
- GCC_except_table8098
- GCC_except_table810
- GCC_except_table8104
- GCC_except_table811
- GCC_except_table8152
- GCC_except_table8154
- GCC_except_table8156
- GCC_except_table8158
- GCC_except_table8160
- GCC_except_table8162
- GCC_except_table8164
- GCC_except_table8166
- GCC_except_table8168
- GCC_except_table8170
- GCC_except_table8172
- GCC_except_table8175
- GCC_except_table8177
- GCC_except_table8179
- GCC_except_table8187
- GCC_except_table8193
- GCC_except_table8198
- GCC_except_table8201
- GCC_except_table8204
- GCC_except_table8233
- GCC_except_table8254
- GCC_except_table8255
- GCC_except_table8257
- GCC_except_table8258
- GCC_except_table8260
- GCC_except_table8262
- GCC_except_table8264
- GCC_except_table8265
- GCC_except_table827
- GCC_except_table8271
- GCC_except_table8276
- GCC_except_table8439
- GCC_except_table8455
- GCC_except_table8457
- GCC_except_table8459
- GCC_except_table8462
- GCC_except_table8464
- GCC_except_table8466
- GCC_except_table8468
- GCC_except_table8469
- GCC_except_table8471
- GCC_except_table8475
- GCC_except_table8480
- GCC_except_table867
- GCC_except_table889
- GCC_except_table893
- GCC_except_table907
- GCC_except_table912
- OBJC_IVAR_$_HAPAccessoryServerBrowserIP._maximumNumberOfPairVeifiesAllowed
- ___72-[HAPAccessoryServerHAP2Adapter accessoryServer:didFinishAuthWithError:]_block_invoke_2
- ___84-[HAPAccessoryServerHAP2Adapter accessoryServer:doesRequireSetupCodeWithCompletion:]_block_invoke_2
- ___86-[HAPAccessoryServerHAP2Adapter accessoryServer:validatePairingCert:model:completion:]_block_invoke_2
- ___90-[HAPAccessoryServerHAP2Adapter accessoryServer:confirmSoftwareAuthUUID:token:completion:]_block_invoke_2
- ___95-[HAPAccessoryServerHAP2Adapter accessoryServer:authenticateSoftwareAuthUUID:token:completion:]_block_invoke_2
- ___97-[HAPAccessoryServerHAP2Adapter accessoryServer:validateSoftwareAuthUUID:token:model:completion:]_block_invoke_2
- ___98-[HAPAccessoryServerHAP2Adapter accessoryServer:didRejectSetupCodeWithBackoffInterval:completion:]_block_invoke_2
- logCategory._hmf_once_t802
- logCategory._hmf_once_v803
CStrings:
+ "%@ Browser fast-set hasDiscoveryAdvertisement=%{public}d"
+ "%@/%u"
+ "%@@%.2fs"
+ "%{public}@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Rtwm5p/Sources/HomeKit/Sources/CoreHAP/HAP2/HAPAdapter/HAPAccessoryServerHAP2Adapter.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Rtwm5p/Sources/HomeKit/Sources/CoreHAP/HAP2/Pairing/HAP2AccessoryServerPairingDriver.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Rtwm5p/Sources/HomeKit/Sources/CoreHAP/HAPHTTPClient.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Rtwm5p/Sources/HomeKit/Sources/CoreHAP/Servers/HAPAccessoryServerIP.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Rtwm5p/Sources/HomeKit/Sources/CoreHAP/Servers/_HAPAccessoryServerBTLE200.m"
+ "B32@?0@\"NSString\"8@\"HAPMetricsRacingRendezvous\"16^B24"
+ "HAP2 stall: op '%@' waited=%.2fs unfinishedDeps=%lu executing=%lu queued=%lu suspended=%d maxConcurrent=%ld runQoS=%@ reqQoS=%@ queueQoS=%@ longestRunning=[%@]"
+ "Not resuming a pending bulk operation while one is already current"
+ "[%{public}@] Not resuming a pending bulk operation while one is already current"
+ "d8@?0"
+ "v16@?0@\"HAPMetricsRacingRendezvous\"8"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iiizLX/Sources/HomeKit/Sources/CoreHAP/HAP2/HAPAdapter/HAPAccessoryServerHAP2Adapter.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iiizLX/Sources/HomeKit/Sources/CoreHAP/HAP2/Pairing/HAP2AccessoryServerPairingDriver.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iiizLX/Sources/HomeKit/Sources/CoreHAP/HAPHTTPClient.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iiizLX/Sources/HomeKit/Sources/CoreHAP/Servers/HAPAccessoryServerIP.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.iiizLX/Sources/HomeKit/Sources/CoreHAP/Servers/_HAPAccessoryServerBTLE200.m"

```
