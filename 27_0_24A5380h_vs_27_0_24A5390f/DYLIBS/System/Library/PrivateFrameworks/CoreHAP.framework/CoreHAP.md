## CoreHAP

> `/System/Library/PrivateFrameworks/CoreHAP.framework/CoreHAP`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__thread_vars`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-1484.2.0.0.0
-  __TEXT.__text: 0x2ab5a4
-  __TEXT.__objc_methlist: 0x18ad8
-  __TEXT.__const: 0x1230
+1490.2.0.1.1
+  __TEXT.__text: 0x2af29c
+  __TEXT.__objc_methlist: 0x18c98
+  __TEXT.__const: 0x1238
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__constg_swiftt: 0x918
+  __TEXT.__constg_swiftt: 0x960
   __TEXT.__swift5_typeref: 0x3e4
   __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_reflstr: 0x424
-  __TEXT.__swift5_fieldmd: 0x3cc
+  __TEXT.__swift5_reflstr: 0x474
+  __TEXT.__swift5_fieldmd: 0x3f0
   __TEXT.__swift5_assocty: 0xc0
   __TEXT.__swift5_proto: 0x50
   __TEXT.__swift5_types: 0x30
-  __TEXT.__cstring: 0x14599
-  __TEXT.__oslogstring: 0x43aea
-  __TEXT.__swift5_capture: 0x278
-  __TEXT.__gcc_except_tab: 0x5ee8
-  __TEXT.__unwind_info: 0x7768
-  __TEXT.__eh_frame: 0x1000
+  __TEXT.__cstring: 0x146a9
+  __TEXT.__oslogstring: 0x450b2
+  __TEXT.__swift5_capture: 0x288
+  __TEXT.__gcc_except_tab: 0x5f00
+  __TEXT.__unwind_info: 0x77d8
+  __TEXT.__eh_frame: 0x1080
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x59c0
-  __DATA_CONST.__objc_classlist: 0xc18
+  __DATA_CONST.__objc_classlist: 0xc20
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x3b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8218
+  __DATA_CONST.__objc_selrefs: 0x8338
   __DATA_CONST.__objc_protorefs: 0x100
   __DATA_CONST.__objc_superrefs: 0xa68
   __DATA_CONST.__objc_arraydata: 0x200
-  __DATA_CONST.__got: 0x1028
-  __AUTH_CONST.__const: 0x1448
-  __AUTH_CONST.__cfstring: 0x10020
-  __AUTH_CONST.__objc_const: 0x2afd0
+  __DATA_CONST.__got: 0x1030
+  __AUTH_CONST.__const: 0x1498
+  __AUTH_CONST.__cfstring: 0x10080
+  __AUTH_CONST.__objc_const: 0x2b280
   __AUTH_CONST.__objc_intobj: 0x738
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0xc0
-  __AUTH_CONST.__auth_got: 0x1338
-  __AUTH.__objc_data: 0x72e8
-  __AUTH.__data: 0x80
+  __AUTH_CONST.__auth_got: 0x1340
+  __AUTH.__objc_data: 0x73b8
+  __AUTH.__data: 0xb0
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x28
-  __DATA.__objc_ivar: 0x18fc
-  __DATA.__data: 0x2d72
+  __DATA.__objc_ivar: 0x1924
+  __DATA.__data: 0x2da2
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0xee0
   __DATA.__common: 0x8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9807
-  Symbols:   20135
-  CStrings:  7087
+  Functions: 9858
+  Symbols:   20215
+  CStrings:  7178
 
Symbols:
+ -[HAP2Diagnostics notifyOperationTimeoutWithOperationName:]
+ -[HAPAccessoryServerBrowserNFC _logPrewarmTransition:]
+ -[HAPAccessoryServerBrowserNFC _reapPrewarmServerIfNeeded]
+ -[HAPAccessoryServerBrowserNFC _rearmPrewarmAfterFailureEdge]
+ -[HAPAccessoryServerBrowserNFC commitPrewarmDiscovery]
+ -[HAPAccessoryServerBrowserNFC isPrewarming]
+ -[HAPAccessoryServerBrowserNFC prewarmRearmCount]
+ -[HAPAccessoryServerBrowserNFC searching]
+ -[HAPAccessoryServerBrowserNFC setPrewarmRearmCount:]
+ -[HAPAccessoryServerBrowserNFC setPrewarming:]
+ -[HAPAccessoryServerBrowserNFC setSearching:]
+ -[HAPAccessoryServerBrowserNFC startPrewarmDiscoveringNFCAccessoryServer]
+ -[HAPAccessoryServerBrowserNFC stopPrewarmNFCDiscovery]
+ -[HAPAccessoryServerNFC _abandonPreparedPairing]
+ -[HAPAccessoryServerNFC _pairingWorkElapsed]
+ -[HAPAccessoryServerNFC _prepareForPairing]
+ -[HAPAccessoryServerNFC failureReported]
+ -[HAPAccessoryServerNFC isNotCertified]
+ -[HAPAccessoryServerNFC nfcLastStepWorkElapsed]
+ -[HAPAccessoryServerNFC nfcPairingIdleAccumulated]
+ -[HAPAccessoryServerNFC nfcPauseStartTime]
+ -[HAPAccessoryServerNFC pairSetupSessionDidEstablishSessionPendingCommit:]
+ -[HAPAccessoryServerNFC prepareForPairing]
+ -[HAPAccessoryServerNFC preparedPendingCommit]
+ -[HAPAccessoryServerNFC preparingPairing]
+ -[HAPAccessoryServerNFC setFailureReported:]
+ -[HAPAccessoryServerNFC setNfcLastStepWorkElapsed:]
+ -[HAPAccessoryServerNFC setNfcPairingIdleAccumulated:]
+ -[HAPAccessoryServerNFC setNfcPauseStartTime:]
+ -[HAPAccessoryServerNFC setNotCertified:]
+ -[HAPAccessoryServerNFC setPreparedPendingCommit:]
+ -[HAPAccessoryServerNFC setPreparingPairing:]
+ GCC_except_table1059
+ GCC_except_table1061
+ GCC_except_table1167
+ GCC_except_table1172
+ GCC_except_table1174
+ GCC_except_table1187
+ GCC_except_table1199
+ GCC_except_table1201
+ GCC_except_table1203
+ GCC_except_table1205
+ GCC_except_table1331
+ GCC_except_table1335
+ GCC_except_table1337
+ GCC_except_table1539
+ GCC_except_table1749
+ GCC_except_table1751
+ GCC_except_table1756
+ GCC_except_table1764
+ GCC_except_table1770
+ GCC_except_table1772
+ GCC_except_table1776
+ GCC_except_table1782
+ GCC_except_table1784
+ GCC_except_table1786
+ GCC_except_table1788
+ GCC_except_table1807
+ GCC_except_table1815
+ GCC_except_table1822
+ GCC_except_table1830
+ GCC_except_table1834
+ GCC_except_table1872
+ GCC_except_table1991
+ GCC_except_table1995
+ GCC_except_table1996
+ GCC_except_table1998
+ GCC_except_table2000
+ GCC_except_table2012
+ GCC_except_table2017
+ GCC_except_table2021
+ GCC_except_table2024
+ GCC_except_table2026
+ GCC_except_table2029
+ GCC_except_table2046
+ GCC_except_table2056
+ GCC_except_table2058
+ GCC_except_table2060
+ GCC_except_table2065
+ GCC_except_table2068
+ GCC_except_table2070
+ GCC_except_table2073
+ GCC_except_table2080
+ GCC_except_table2082
+ GCC_except_table2085
+ GCC_except_table2088
+ GCC_except_table2090
+ GCC_except_table2092
+ GCC_except_table2100
+ GCC_except_table2108
+ GCC_except_table2152
+ GCC_except_table2157
+ GCC_except_table2175
+ GCC_except_table2176
+ GCC_except_table2177
+ GCC_except_table2179
+ GCC_except_table2180
+ GCC_except_table2181
+ GCC_except_table2183
+ GCC_except_table2184
+ GCC_except_table2206
+ GCC_except_table2210
+ GCC_except_table2218
+ GCC_except_table2384
+ GCC_except_table2391
+ GCC_except_table2399
+ GCC_except_table2403
+ GCC_except_table2408
+ GCC_except_table2413
+ GCC_except_table2425
+ GCC_except_table2427
+ GCC_except_table2528
+ GCC_except_table2536
+ GCC_except_table2537
+ GCC_except_table2539
+ GCC_except_table2540
+ GCC_except_table2541
+ GCC_except_table2556
+ GCC_except_table2570
+ GCC_except_table2650
+ GCC_except_table2662
+ GCC_except_table2723
+ GCC_except_table2731
+ GCC_except_table2742
+ GCC_except_table2756
+ GCC_except_table2759
+ GCC_except_table2764
+ GCC_except_table2772
+ GCC_except_table2778
+ GCC_except_table2780
+ GCC_except_table2790
+ GCC_except_table2813
+ GCC_except_table2819
+ GCC_except_table3024
+ GCC_except_table3075
+ GCC_except_table3091
+ GCC_except_table3093
+ GCC_except_table3134
+ GCC_except_table3149
+ GCC_except_table3150
+ GCC_except_table3153
+ GCC_except_table3159
+ GCC_except_table3166
+ GCC_except_table3169
+ GCC_except_table3174
+ GCC_except_table3179
+ GCC_except_table3184
+ GCC_except_table3223
+ GCC_except_table3240
+ GCC_except_table3243
+ GCC_except_table3248
+ GCC_except_table3250
+ GCC_except_table3266
+ GCC_except_table3280
+ GCC_except_table3282
+ GCC_except_table3286
+ GCC_except_table3294
+ GCC_except_table3302
+ GCC_except_table3366
+ GCC_except_table3373
+ GCC_except_table3375
+ GCC_except_table3376
+ GCC_except_table3399
+ GCC_except_table3419
+ GCC_except_table3647
+ GCC_except_table3714
+ GCC_except_table3715
+ GCC_except_table3719
+ GCC_except_table3722
+ GCC_except_table3724
+ GCC_except_table3725
+ GCC_except_table3728
+ GCC_except_table3730
+ GCC_except_table3737
+ GCC_except_table3750
+ GCC_except_table3761
+ GCC_except_table3762
+ GCC_except_table3764
+ GCC_except_table3766
+ GCC_except_table3769
+ GCC_except_table3772
+ GCC_except_table3774
+ GCC_except_table3777
+ GCC_except_table3780
+ GCC_except_table3792
+ GCC_except_table3794
+ GCC_except_table3798
+ GCC_except_table3802
+ GCC_except_table3806
+ GCC_except_table3832
+ GCC_except_table3855
+ GCC_except_table3861
+ GCC_except_table3865
+ GCC_except_table3869
+ GCC_except_table3871
+ GCC_except_table3874
+ GCC_except_table3876
+ GCC_except_table3885
+ GCC_except_table3887
+ GCC_except_table3968
+ GCC_except_table3969
+ GCC_except_table3970
+ GCC_except_table3971
+ GCC_except_table3972
+ GCC_except_table3973
+ GCC_except_table3974
+ GCC_except_table3975
+ GCC_except_table3976
+ GCC_except_table3977
+ GCC_except_table4020
+ GCC_except_table4047
+ GCC_except_table4157
+ GCC_except_table4164
+ GCC_except_table4206
+ GCC_except_table4210
+ GCC_except_table4213
+ GCC_except_table4219
+ GCC_except_table4222
+ GCC_except_table4225
+ GCC_except_table4228
+ GCC_except_table4231
+ GCC_except_table4234
+ GCC_except_table4239
+ GCC_except_table4252
+ GCC_except_table4257
+ GCC_except_table4261
+ GCC_except_table4263
+ GCC_except_table4266
+ GCC_except_table4277
+ GCC_except_table4285
+ GCC_except_table4289
+ GCC_except_table4296
+ GCC_except_table4300
+ GCC_except_table4318
+ GCC_except_table4320
+ GCC_except_table4322
+ GCC_except_table4323
+ GCC_except_table4326
+ GCC_except_table4335
+ GCC_except_table4337
+ GCC_except_table4343
+ GCC_except_table4348
+ GCC_except_table4359
+ GCC_except_table4370
+ GCC_except_table4372
+ GCC_except_table4381
+ GCC_except_table4383
+ GCC_except_table4385
+ GCC_except_table4651
+ GCC_except_table4657
+ GCC_except_table4674
+ GCC_except_table4678
+ GCC_except_table4695
+ GCC_except_table4701
+ GCC_except_table4714
+ GCC_except_table4728
+ GCC_except_table4732
+ GCC_except_table4845
+ GCC_except_table521
+ GCC_except_table5301
+ GCC_except_table5309
+ GCC_except_table531
+ GCC_except_table5361
+ GCC_except_table5364
+ GCC_except_table5365
+ GCC_except_table5366
+ GCC_except_table5367
+ GCC_except_table545
+ GCC_except_table5517
+ GCC_except_table5518
+ GCC_except_table5519
+ GCC_except_table5520
+ GCC_except_table5521
+ GCC_except_table5527
+ GCC_except_table5528
+ GCC_except_table553
+ GCC_except_table5530
+ GCC_except_table5540
+ GCC_except_table5547
+ GCC_except_table5550
+ GCC_except_table5553
+ GCC_except_table5557
+ GCC_except_table5561
+ GCC_except_table582
+ GCC_except_table589
+ GCC_except_table601
+ GCC_except_table602
+ GCC_except_table604
+ GCC_except_table6047
+ GCC_except_table6048
+ GCC_except_table6067
+ GCC_except_table607
+ GCC_except_table6077
+ GCC_except_table6085
+ GCC_except_table6088
+ GCC_except_table6092
+ GCC_except_table610
+ GCC_except_table620
+ GCC_except_table622
+ GCC_except_table626
+ GCC_except_table636
+ GCC_except_table6361
+ GCC_except_table6365
+ GCC_except_table6410
+ GCC_except_table6414
+ GCC_except_table6416
+ GCC_except_table6418
+ GCC_except_table6620
+ GCC_except_table6630
+ GCC_except_table6631
+ GCC_except_table6632
+ GCC_except_table6633
+ GCC_except_table6639
+ GCC_except_table6655
+ GCC_except_table6690
+ GCC_except_table6691
+ GCC_except_table6692
+ GCC_except_table670
+ GCC_except_table6712
+ GCC_except_table6724
+ GCC_except_table6732
+ GCC_except_table6734
+ GCC_except_table6748
+ GCC_except_table680
+ GCC_except_table688
+ GCC_except_table6971
+ GCC_except_table6989
+ GCC_except_table6992
+ GCC_except_table6995
+ GCC_except_table6996
+ GCC_except_table6998
+ GCC_except_table7028
+ GCC_except_table7050
+ GCC_except_table7054
+ GCC_except_table7063
+ GCC_except_table7067
+ GCC_except_table7071
+ GCC_except_table7075
+ GCC_except_table7079
+ GCC_except_table7087
+ GCC_except_table7089
+ GCC_except_table7091
+ GCC_except_table7130
+ GCC_except_table715
+ GCC_except_table719
+ GCC_except_table722
+ GCC_except_table724
+ GCC_except_table7252
+ GCC_except_table7286
+ GCC_except_table732
+ GCC_except_table7376
+ GCC_except_table7377
+ GCC_except_table7378
+ GCC_except_table7379
+ GCC_except_table7380
+ GCC_except_table7381
+ GCC_except_table7382
+ GCC_except_table7444
+ GCC_except_table745
+ GCC_except_table7454
+ GCC_except_table7455
+ GCC_except_table7467
+ GCC_except_table7486
+ GCC_except_table7489
+ GCC_except_table749
+ GCC_except_table7490
+ GCC_except_table7495
+ GCC_except_table7498
+ GCC_except_table7505
+ GCC_except_table7508
+ GCC_except_table7522
+ GCC_except_table7529
+ GCC_except_table753
+ GCC_except_table7535
+ GCC_except_table7544
+ GCC_except_table7546
+ GCC_except_table7550
+ GCC_except_table7551
+ GCC_except_table7558
+ GCC_except_table7594
+ GCC_except_table7595
+ GCC_except_table7600
+ GCC_except_table7604
+ GCC_except_table7608
+ GCC_except_table7614
+ GCC_except_table7618
+ GCC_except_table7622
+ GCC_except_table7624
+ GCC_except_table7626
+ GCC_except_table763
+ GCC_except_table7630
+ GCC_except_table769
+ GCC_except_table772
+ GCC_except_table7744
+ GCC_except_table7781
+ GCC_except_table7838
+ GCC_except_table784
+ GCC_except_table7841
+ GCC_except_table7845
+ GCC_except_table7851
+ GCC_except_table7858
+ GCC_except_table7859
+ GCC_except_table7875
+ GCC_except_table7879
+ GCC_except_table7880
+ GCC_except_table7881
+ GCC_except_table790
+ GCC_except_table7930
+ GCC_except_table7931
+ GCC_except_table7933
+ GCC_except_table7936
+ GCC_except_table796
+ GCC_except_table7963
+ GCC_except_table7969
+ GCC_except_table797
+ GCC_except_table7989
+ GCC_except_table8007
+ GCC_except_table8008
+ GCC_except_table8009
+ GCC_except_table8023
+ GCC_except_table8024
+ GCC_except_table8040
+ GCC_except_table8050
+ GCC_except_table8057
+ GCC_except_table8062
+ GCC_except_table8068
+ GCC_except_table8080
+ GCC_except_table8086
+ GCC_except_table8095
+ GCC_except_table8101
+ GCC_except_table8102
+ GCC_except_table8106
+ GCC_except_table8108
+ GCC_except_table8114
+ GCC_except_table8135
+ GCC_except_table8137
+ GCC_except_table8138
+ GCC_except_table8164
+ GCC_except_table823
+ GCC_except_table830
+ GCC_except_table8329
+ GCC_except_table837
+ GCC_except_table838
+ GCC_except_table8392
+ GCC_except_table8424
+ GCC_except_table8427
+ GCC_except_table8594
+ GCC_except_table8632
+ GCC_except_table866
+ GCC_except_table8669
+ GCC_except_table8758
+ GCC_except_table8760
+ GCC_except_table8762
+ GCC_except_table8764
+ GCC_except_table8766
+ GCC_except_table8768
+ GCC_except_table8775
+ GCC_except_table8777
+ GCC_except_table8779
+ GCC_except_table8781
+ GCC_except_table8784
+ GCC_except_table8788
+ GCC_except_table8795
+ GCC_except_table8801
+ GCC_except_table8806
+ GCC_except_table8809
+ GCC_except_table8814
+ GCC_except_table8822
+ GCC_except_table8825
+ GCC_except_table8851
+ GCC_except_table8854
+ GCC_except_table8855
+ GCC_except_table889
+ GCC_except_table8894
+ GCC_except_table8895
+ GCC_except_table8896
+ GCC_except_table8898
+ GCC_except_table8899
+ GCC_except_table8901
+ GCC_except_table8902
+ GCC_except_table8903
+ GCC_except_table8905
+ GCC_except_table8906
+ GCC_except_table8908
+ GCC_except_table8912
+ GCC_except_table8913
+ GCC_except_table8917
+ GCC_except_table8968
+ GCC_except_table8975
+ GCC_except_table907
+ GCC_except_table9079
+ GCC_except_table9083
+ GCC_except_table9085
+ GCC_except_table9087
+ GCC_except_table9090
+ GCC_except_table9092
+ GCC_except_table9094
+ GCC_except_table9096
+ GCC_except_table9097
+ GCC_except_table9099
+ GCC_except_table9101
+ GCC_except_table9106
+ GCC_except_table9108
+ GCC_except_table9109
+ GCC_except_table931
+ GCC_except_table935
+ GCC_except_table949
+ GCC_except_table954
+ _OBJC_CLASS_$_CoreHAPHKDF
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._logDescription
+ _OBJC_IVAR_$_HAPAccessoryServerBrowserNFC._prewarmRearmCount
+ _OBJC_IVAR_$_HAPAccessoryServerBrowserNFC._prewarming
+ _OBJC_IVAR_$_HAPAccessoryServerBrowserNFC._searching
+ _OBJC_IVAR_$_HAPAccessoryServerNFC._failureReported
+ _OBJC_IVAR_$_HAPAccessoryServerNFC._nfcLastStepWorkElapsed
+ _OBJC_IVAR_$_HAPAccessoryServerNFC._nfcPairingIdleAccumulated
+ _OBJC_IVAR_$_HAPAccessoryServerNFC._nfcPauseStartTime
+ _OBJC_IVAR_$_HAPAccessoryServerNFC._notCertified
+ _OBJC_IVAR_$_HAPAccessoryServerNFC._preparedPendingCommit
+ _OBJC_IVAR_$_HAPAccessoryServerNFC._preparingPairing
+ _OBJC_METACLASS_$_CoreHAPHKDF
+ __CLASS_METHODS_CoreHAPHKDF
+ __DATA_CoreHAPHKDF
+ __INSTANCE_METHODS_CoreHAPHKDF
+ __METACLASS_DATA_CoreHAPHKDF
+ ___42-[HAPAccessoryServerNFC prepareForPairing]_block_invoke
+ ___43-[HAPAccessoryServerNFC _prepareForPairing]_block_invoke
+ ___54-[HAPAccessoryServerBrowserNFC commitPrewarmDiscovery]_block_invoke
+ ___55-[HAPAccessoryServerBrowserNFC stopPrewarmNFCDiscovery]_block_invoke
+ ___73-[HAPAccessoryServerBrowserNFC startPrewarmDiscoveringNFCAccessoryServer]_block_invoke
+ ___74-[HAPAccessoryServerNFC pairSetupSessionDidEstablishSessionPendingCommit:]_block_invoke
+ ___swift_closure_destructor.181Tm
+ _objc_msgSend$_abandonPreparedPairing
+ _objc_msgSend$_logPrewarmTransition:
+ _objc_msgSend$_pairingWorkElapsed
+ _objc_msgSend$_prepareForPairing
+ _objc_msgSend$_reapPrewarmServerIfNeeded
+ _objc_msgSend$_rearmPrewarmAfterFailureEdge
+ _objc_msgSend$failureReported
+ _objc_msgSend$hap2DiagnosticsDidObserveOperationTimeoutWithOperationName:
+ _objc_msgSend$isPrewarming
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$nfcLastStepWorkElapsed
+ _objc_msgSend$nfcPairingIdleAccumulated
+ _objc_msgSend$nfcPauseStartTime
+ _objc_msgSend$notifyOperationTimeoutWithOperationName:
+ _objc_msgSend$pairSetupSessionDidEstablishSessionPendingCommit:
+ _objc_msgSend$preparingPairing
+ _objc_msgSend$prewarmRearmCount
+ _objc_msgSend$proceedWithCommit
+ _objc_msgSend$searching
+ _objc_msgSend$setFailureReported:
+ _objc_msgSend$setNfcLastStepWorkElapsed:
+ _objc_msgSend$setNfcPairingIdleAccumulated:
+ _objc_msgSend$setNfcPauseStartTime:
+ _objc_msgSend$setPausesBeforeCommit:
+ _objc_msgSend$setPreparedPendingCommit:
+ _objc_msgSend$setPreparingPairing:
+ _objc_msgSend$setPrewarmRearmCount:
+ _objc_msgSend$setPrewarming:
+ _objc_msgSend$setSearching:
+ _objc_retain_x10
- -[HAPAccessoryServerNFC nfcLastStepTime]
- -[HAPAccessoryServerNFC setNfcLastStepTime:]
- GCC_except_table1070
- GCC_except_table1072
- GCC_except_table1178
- GCC_except_table1183
- GCC_except_table1185
- GCC_except_table1198
- GCC_except_table1210
- GCC_except_table1212
- GCC_except_table1214
- GCC_except_table1216
- GCC_except_table1342
- GCC_except_table1346
- GCC_except_table1348
- GCC_except_table1550
- GCC_except_table1760
- GCC_except_table1767
- GCC_except_table1773
- GCC_except_table1775
- GCC_except_table1781
- GCC_except_table1783
- GCC_except_table1787
- GCC_except_table1795
- GCC_except_table1799
- GCC_except_table1804
- GCC_except_table1808
- GCC_except_table1818
- GCC_except_table1833
- GCC_except_table1837
- GCC_except_table1841
- GCC_except_table1845
- GCC_except_table1883
- GCC_except_table2002
- GCC_except_table2006
- GCC_except_table2007
- GCC_except_table2009
- GCC_except_table2011
- GCC_except_table2023
- GCC_except_table2028
- GCC_except_table2032
- GCC_except_table2035
- GCC_except_table2037
- GCC_except_table2040
- GCC_except_table2057
- GCC_except_table2067
- GCC_except_table2069
- GCC_except_table2071
- GCC_except_table2079
- GCC_except_table2081
- GCC_except_table2084
- GCC_except_table2087
- GCC_except_table2091
- GCC_except_table2093
- GCC_except_table2099
- GCC_except_table2101
- GCC_except_table2103
- GCC_except_table2107
- GCC_except_table2111
- GCC_except_table2130
- GCC_except_table2163
- GCC_except_table2168
- GCC_except_table2186
- GCC_except_table2187
- GCC_except_table2188
- GCC_except_table2190
- GCC_except_table2191
- GCC_except_table2192
- GCC_except_table2194
- GCC_except_table2195
- GCC_except_table2217
- GCC_except_table2221
- GCC_except_table2229
- GCC_except_table2402
- GCC_except_table2414
- GCC_except_table2417
- GCC_except_table2430
- GCC_except_table2432
- GCC_except_table2435
- GCC_except_table2436
- GCC_except_table2438
- GCC_except_table2546
- GCC_except_table2547
- GCC_except_table2548
- GCC_except_table2549
- GCC_except_table2550
- GCC_except_table2551
- GCC_except_table2566
- GCC_except_table2580
- GCC_except_table2660
- GCC_except_table2672
- GCC_except_table2877
- GCC_except_table2886
- GCC_except_table2903
- GCC_except_table2937
- GCC_except_table2953
- GCC_except_table2955
- GCC_except_table2967
- GCC_except_table2974
- GCC_except_table2996
- GCC_except_table3010
- GCC_except_table3011
- GCC_except_table3012
- GCC_except_table3021
- GCC_except_table3028
- GCC_except_table3031
- GCC_except_table3036
- GCC_except_table3046
- GCC_except_table3085
- GCC_except_table3102
- GCC_except_table3110
- GCC_except_table3128
- GCC_except_table3142
- GCC_except_table3144
- GCC_except_table3156
- GCC_except_table3164
- GCC_except_table3228
- GCC_except_table3235
- GCC_except_table3237
- GCC_except_table3238
- GCC_except_table3261
- GCC_except_table3281
- GCC_except_table3509
- GCC_except_table3576
- GCC_except_table3577
- GCC_except_table3581
- GCC_except_table3584
- GCC_except_table3586
- GCC_except_table3587
- GCC_except_table3589
- GCC_except_table3590
- GCC_except_table3592
- GCC_except_table3599
- GCC_except_table3609
- GCC_except_table3612
- GCC_except_table3623
- GCC_except_table3624
- GCC_except_table3626
- GCC_except_table3628
- GCC_except_table3631
- GCC_except_table3634
- GCC_except_table3636
- GCC_except_table3639
- GCC_except_table3642
- GCC_except_table3654
- GCC_except_table3656
- GCC_except_table3660
- GCC_except_table3664
- GCC_except_table3668
- GCC_except_table3694
- GCC_except_table3717
- GCC_except_table3723
- GCC_except_table3731
- GCC_except_table3733
- GCC_except_table3736
- GCC_except_table3738
- GCC_except_table3740
- GCC_except_table3748
- GCC_except_table3749
- GCC_except_table3837
- GCC_except_table3845
- GCC_except_table3856
- GCC_except_table3870
- GCC_except_table3873
- GCC_except_table3892
- GCC_except_table3894
- GCC_except_table3904
- GCC_except_table3927
- GCC_except_table3933
- GCC_except_table3982
- GCC_except_table3983
- GCC_except_table3984
- GCC_except_table3985
- GCC_except_table3986
- GCC_except_table3987
- GCC_except_table3988
- GCC_except_table3989
- GCC_except_table3990
- GCC_except_table3991
- GCC_except_table4030
- GCC_except_table4057
- GCC_except_table4167
- GCC_except_table4174
- GCC_except_table4220
- GCC_except_table4223
- GCC_except_table4226
- GCC_except_table4229
- GCC_except_table4232
- GCC_except_table4235
- GCC_except_table4238
- GCC_except_table4241
- GCC_except_table4244
- GCC_except_table4249
- GCC_except_table4262
- GCC_except_table4267
- GCC_except_table4271
- GCC_except_table4273
- GCC_except_table4276
- GCC_except_table4287
- GCC_except_table4305
- GCC_except_table4306
- GCC_except_table4309
- GCC_except_table4310
- GCC_except_table4328
- GCC_except_table4330
- GCC_except_table4333
- GCC_except_table4336
- GCC_except_table4342
- GCC_except_table4347
- GCC_except_table4353
- GCC_except_table4355
- GCC_except_table4358
- GCC_except_table4369
- GCC_except_table4380
- GCC_except_table4382
- GCC_except_table4393
- GCC_except_table4395
- GCC_except_table4401
- GCC_except_table4661
- GCC_except_table4667
- GCC_except_table4684
- GCC_except_table4688
- GCC_except_table4705
- GCC_except_table4711
- GCC_except_table4724
- GCC_except_table4738
- GCC_except_table4742
- GCC_except_table4855
- GCC_except_table5311
- GCC_except_table532
- GCC_except_table5329
- GCC_except_table5371
- GCC_except_table5374
- GCC_except_table5375
- GCC_except_table5376
- GCC_except_table5377
- GCC_except_table542
- GCC_except_table5511
- GCC_except_table5512
- GCC_except_table5513
- GCC_except_table5514
- GCC_except_table5515
- GCC_except_table5522
- GCC_except_table5523
- GCC_except_table5525
- GCC_except_table5532
- GCC_except_table5535
- GCC_except_table5545
- GCC_except_table5548
- GCC_except_table5552
- GCC_except_table5556
- GCC_except_table556
- GCC_except_table564
- GCC_except_table593
- GCC_except_table600
- GCC_except_table6042
- GCC_except_table6043
- GCC_except_table6062
- GCC_except_table6072
- GCC_except_table6075
- GCC_except_table6083
- GCC_except_table6087
- GCC_except_table612
- GCC_except_table613
- GCC_except_table615
- GCC_except_table618
- GCC_except_table621
- GCC_except_table631
- GCC_except_table6356
- GCC_except_table6360
- GCC_except_table637
- GCC_except_table6405
- GCC_except_table6409
- GCC_except_table6411
- GCC_except_table6413
- GCC_except_table644
- GCC_except_table647
- GCC_except_table6615
- GCC_except_table6621
- GCC_except_table6625
- GCC_except_table6627
- GCC_except_table6628
- GCC_except_table6634
- GCC_except_table6650
- GCC_except_table6685
- GCC_except_table6686
- GCC_except_table6687
- GCC_except_table6707
- GCC_except_table6719
- GCC_except_table6722
- GCC_except_table6729
- GCC_except_table6743
- GCC_except_table681
- GCC_except_table691
- GCC_except_table6966
- GCC_except_table6979
- GCC_except_table6987
- GCC_except_table6988
- GCC_except_table699
- GCC_except_table6990
- GCC_except_table6991
- GCC_except_table7023
- GCC_except_table7045
- GCC_except_table7049
- GCC_except_table7053
- GCC_except_table7062
- GCC_except_table7066
- GCC_except_table7070
- GCC_except_table7074
- GCC_except_table7082
- GCC_except_table7084
- GCC_except_table7086
- GCC_except_table7125
- GCC_except_table7234
- GCC_except_table726
- GCC_except_table7266
- GCC_except_table733
- GCC_except_table735
- GCC_except_table7351
- GCC_except_table7352
- GCC_except_table7353
- GCC_except_table7354
- GCC_except_table7355
- GCC_except_table7356
- GCC_except_table7357
- GCC_except_table741
- GCC_except_table7419
- GCC_except_table7429
- GCC_except_table743
- GCC_except_table7430
- GCC_except_table7442
- GCC_except_table7448
- GCC_except_table7461
- GCC_except_table7464
- GCC_except_table7465
- GCC_except_table7470
- GCC_except_table7480
- GCC_except_table7483
- GCC_except_table7497
- GCC_except_table7504
- GCC_except_table7510
- GCC_except_table7519
- GCC_except_table7521
- GCC_except_table7525
- GCC_except_table7526
- GCC_except_table7533
- GCC_except_table7545
- GCC_except_table7554
- GCC_except_table756
- GCC_except_table7569
- GCC_except_table7575
- GCC_except_table7580
- GCC_except_table7583
- GCC_except_table7589
- GCC_except_table7593
- GCC_except_table7597
- GCC_except_table7599
- GCC_except_table760
- GCC_except_table7601
- GCC_except_table7719
- GCC_except_table774
- GCC_except_table7756
- GCC_except_table7813
- GCC_except_table7816
- GCC_except_table7820
- GCC_except_table7826
- GCC_except_table783
- GCC_except_table7833
- GCC_except_table7834
- GCC_except_table7850
- GCC_except_table7854
- GCC_except_table7855
- GCC_except_table7856
- GCC_except_table786
- GCC_except_table7905
- GCC_except_table7906
- GCC_except_table7908
- GCC_except_table7911
- GCC_except_table7938
- GCC_except_table7939
- GCC_except_table7944
- GCC_except_table795
- GCC_except_table7982
- GCC_except_table7983
- GCC_except_table7984
- GCC_except_table7993
- GCC_except_table7998
- GCC_except_table7999
- GCC_except_table8000
- GCC_except_table801
- GCC_except_table8015
- GCC_except_table802
- GCC_except_table8032
- GCC_except_table8037
- GCC_except_table8055
- GCC_except_table8056
- GCC_except_table8061
- GCC_except_table807
- GCC_except_table8070
- GCC_except_table8076
- GCC_except_table8077
- GCC_except_table808
- GCC_except_table8083
- GCC_except_table8085
- GCC_except_table8089
- GCC_except_table8112
- GCC_except_table8113
- GCC_except_table8139
- GCC_except_table8304
- GCC_except_table834
- GCC_except_table8367
- GCC_except_table8399
- GCC_except_table8402
- GCC_except_table841
- GCC_except_table848
- GCC_except_table849
- GCC_except_table8569
- GCC_except_table8607
- GCC_except_table8644
- GCC_except_table8722
- GCC_except_table8724
- GCC_except_table8726
- GCC_except_table8728
- GCC_except_table8730
- GCC_except_table8732
- GCC_except_table8734
- GCC_except_table8737
- GCC_except_table8739
- GCC_except_table8741
- GCC_except_table8743
- GCC_except_table8745
- GCC_except_table8748
- GCC_except_table8750
- GCC_except_table8752
- GCC_except_table8759
- GCC_except_table8765
- GCC_except_table877
- GCC_except_table8778
- GCC_except_table8783
- GCC_except_table8789
- GCC_except_table8815
- GCC_except_table8818
- GCC_except_table8858
- GCC_except_table8859
- GCC_except_table8860
- GCC_except_table8862
- GCC_except_table8863
- GCC_except_table8865
- GCC_except_table8866
- GCC_except_table8867
- GCC_except_table8869
- GCC_except_table8870
- GCC_except_table8872
- GCC_except_table8876
- GCC_except_table8877
- GCC_except_table8881
- GCC_except_table8932
- GCC_except_table8939
- GCC_except_table900
- GCC_except_table9043
- GCC_except_table9047
- GCC_except_table9049
- GCC_except_table9051
- GCC_except_table9054
- GCC_except_table9056
- GCC_except_table9058
- GCC_except_table9060
- GCC_except_table9061
- GCC_except_table9063
- GCC_except_table9065
- GCC_except_table9070
- GCC_except_table9072
- GCC_except_table9073
- GCC_except_table918
- GCC_except_table942
- GCC_except_table946
- GCC_except_table960
- GCC_except_table965
- _OBJC_IVAR_$_HAPAccessoryServerNFC._nfcLastStepTime
- ___swift_closure_destructor.173Tm
- _objc_msgSend$nfcLastStepTime
- _objc_msgSend$setNfcLastStepTime:
CStrings:
+ "AID selected (pre-warm)"
+ "Abandoning pre-warmed pair-setup (non-fatal, pre-consent)"
+ "Adopting already-searching NFC discovery into pre-warm mode"
+ "Cannot pre-warm pair-setup from state %lu"
+ "Commit (resume at M5)"
+ "Committed NFC discovery requested: leaving pre-warm"
+ "Committing pre-warm NFC discovery to a real pairing"
+ "Committing pre-warmed NFC pair-setup (resuming at M5)"
+ "HAP AID selected successfully (pre-warm)"
+ "Ignoring didDetectTag from a stale/replaced NFC reader session"
+ "Ignoring didFailWithError from a stale/replaced NFC reader session: %{public}@"
+ "Ignoring duplicate NFC pair-setup failure (already reported): %@"
+ "Ignoring nfcReaderSessionDidEndUnexpectedly from a stale/replaced NFC reader session: %{public}@"
+ "M4: 32-byte hash but no NDEF token to verify it — prompting uncertified"
+ "M4: prefetched token does not match M4 hash — prompting to add as uncertified"
+ "MFi: delegate accepted not-certified pair; resuming M5 with echoed token"
+ "MFi: delegate accepted not-certified pair; resuming M5 with no software token"
+ "NFC discovery already active and searching; reusing warm session"
+ "NFC pair-setup pre-warmed through M4; awaiting consent to commit (M5/M6)"
+ "NFC reader mode not supported on this device; skipping pre-warm"
+ "NFC tag detected (prewarming=%d)"
+ "No pre-warm tag held; restarting NFC discovery with a fresh detection window for the committed pairing"
+ "Pair-setup paused after M4, pending commit (consent)"
+ "Pre-warm AID selection failed (non-fatal): %@"
+ "Pre-warm NFC discovery already in progress; ignoring duplicate request"
+ "Pre-warm NFC discovery failure (swallowed): %{public}@"
+ "Pre-warm NFC server creation failed; tearing down session and re-arming"
+ "Pre-warm NFC session ended unexpectedly (swallowed): %{public}@"
+ "Pre-warm pair-setup failed before consent (non-fatal): %@"
+ "Pre-warm re-arm cap (%lu) reached; stopping silent NFC discovery"
+ "Pre-warm transition [%{public}s]: prewarming=%d searching=%d rearmCount=%lu/%lu hasReaderSession=%d hasDetectedServer=%d"
+ "Pre-warm: NFC discovery start failed; stopping pre-warm (best-effort): %{public}@"
+ "Pre-warm: reader session unavailable; stopping pre-warm (best-effort)"
+ "Pre-warmed through M4 (awaiting commit)"
+ "Pre-warming NFC pair-setup through M4 (before consent)"
+ "Proceeding with pair-setup commit (M4→M5)"
+ "Re-arming pre-warm NFC discovery (attempt %lu of %lu)"
+ "Reaping stale pre-warm-detected NFC server (connection lost before consent)"
+ "Reusing pre-warm-detected NFC tag for committed pairing"
+ "Secure Transport PairVerify: Timed out waiting for ECDSA key for peer %@"
+ "Secure Transport PairVerify: Timed out waiting for local ECDSA pair-setup identity"
+ "Secure Transport PairVerify: Timed out waiting for local pairing identity"
+ "Secure Transport PairVerify: Timed out waiting for remote pairing identity"
+ "Starting pre-warm NFC discovery (silent, self-rearming on each failure edge, up to %lu re-arms)"
+ "Stopping pre-warm NFC discovery (setup dismissed before consent)"
+ "[%{public}@] Abandoning pre-warmed pair-setup (non-fatal, pre-consent)"
+ "[%{public}@] Adopting already-searching NFC discovery into pre-warm mode"
+ "[%{public}@] Cannot pre-warm pair-setup from state %lu"
+ "[%{public}@] Committed NFC discovery requested: leaving pre-warm"
+ "[%{public}@] Committing pre-warm NFC discovery to a real pairing"
+ "[%{public}@] Committing pre-warmed NFC pair-setup (resuming at M5)"
+ "[%{public}@] HAP AID selected successfully (pre-warm)"
+ "[%{public}@] Ignoring didDetectTag from a stale/replaced NFC reader session"
+ "[%{public}@] Ignoring didFailWithError from a stale/replaced NFC reader session: %{public}@"
+ "[%{public}@] Ignoring duplicate NFC pair-setup failure (already reported): %@"
+ "[%{public}@] Ignoring nfcReaderSessionDidEndUnexpectedly from a stale/replaced NFC reader session: %{public}@"
+ "[%{public}@] NFC discovery already active and searching; reusing warm session"
+ "[%{public}@] NFC pair-setup pre-warmed through M4; awaiting consent to commit (M5/M6)"
+ "[%{public}@] NFC reader mode not supported on this device; skipping pre-warm"
+ "[%{public}@] NFC tag detected (prewarming=%d)"
+ "[%{public}@] No pre-warm tag held; restarting NFC discovery with a fresh detection window for the committed pairing"
+ "[%{public}@] Pre-warm AID selection failed (non-fatal): %@"
+ "[%{public}@] Pre-warm NFC discovery already in progress; ignoring duplicate request"
+ "[%{public}@] Pre-warm NFC discovery failure (swallowed): %{public}@"
+ "[%{public}@] Pre-warm NFC server creation failed; tearing down session and re-arming"
+ "[%{public}@] Pre-warm NFC session ended unexpectedly (swallowed): %{public}@"
+ "[%{public}@] Pre-warm pair-setup failed before consent (non-fatal): %@"
+ "[%{public}@] Pre-warm re-arm cap (%lu) reached; stopping silent NFC discovery"
+ "[%{public}@] Pre-warm transition [%{public}s]: prewarming=%d searching=%d rearmCount=%lu/%lu hasReaderSession=%d hasDetectedServer=%d"
+ "[%{public}@] Pre-warm: NFC discovery start failed; stopping pre-warm (best-effort): %{public}@"
+ "[%{public}@] Pre-warm: reader session unavailable; stopping pre-warm (best-effort)"
+ "[%{public}@] Pre-warming NFC pair-setup through M4 (before consent)"
+ "[%{public}@] Re-arming pre-warm NFC discovery (attempt %lu of %lu)"
+ "[%{public}@] Reaping stale pre-warm-detected NFC server (connection lost before consent)"
+ "[%{public}@] Reusing pre-warm-detected NFC tag for committed pairing"
+ "[%{public}@] Starting pre-warm NFC discovery (silent, self-rearming on each failure edge, up to %lu re-arms)"
+ "[%{public}@] Stopping pre-warm NFC discovery (setup dismissed before consent)"
+ "[%{public}@] [Timing] %{public}@: +%.2fms work (delta %.2fms)"
+ "[%{public}@] [Timing] M1 -> M6 work total: %.2fms"
+ "[%{public}@] [Timing] NFC pairing work total (%{public}@): %.2fms"
+ "[%{public}@] [Timing] Pre-warm started"
+ "[%{public}@] [Timing] Waited %.2fms for consent (idle, excluded from work total)"
+ "[%{public}@] commitPrewarmDiscovery: not pre-warming (already committed or never started); no-op"
+ "[%{public}@] stopPrewarmNFCDiscovery: not pre-warming (already committed or never started); no-op"
+ "[Timing] %{public}@: +%.2fms work (delta %.2fms)"
+ "[Timing] M1 -> M6 work total: %.2fms"
+ "[Timing] NFC pairing work total (%{public}@): %.2fms"
+ "[Timing] Pre-warm started"
+ "[Timing] Waited %.2fms for consent (idle, excluded from work total)"
+ "commit"
+ "commitPrewarmDiscovery: not pre-warming (already committed or never started); no-op"
+ "committedStart"
+ "detectedServerSurfaced"
+ "prewarmFailureSwallowed"
+ "prewarmSessionEndedSwallowed"
+ "readerArmed"
+ "reapedDetectedServer"
+ "startPrewarm"
+ "stopDiscovering"
+ "stopPrewarm"
+ "stopPrewarmNFCDiscovery: not pre-warming (already committed or never started); no-op"
+ "tagDetected"
- "M4: UNEXPECTED — 32-byte MFi token hash with no prefetched NDEF token to verify it; failing pair-setup instead of rolling the hash (would corrupt the accessory's token slot)"
- "M4: prefetched token does not match M4 hash — failing pair-setup"
- "MFi: delegate accepted not-certified pair after roll error; resuming M5 with echoed token"
- "NFC tag detected"
- "[%{public}@] NFC tag detected"
- "[%{public}@] [Timing] %{public}@: +%.2fms (delta %.2fms)"
- "[%{public}@] [Timing] M1 -> M6 total: %.2fms"
- "[%{public}@] [Timing] NFC pairing total (%{public}@): %.2fms"
- "[Timing] %{public}@: +%.2fms (delta %.2fms)"
- "[Timing] M1 -> M6 total: %.2fms"
- "[Timing] NFC pairing total (%{public}@): %.2fms"
```
