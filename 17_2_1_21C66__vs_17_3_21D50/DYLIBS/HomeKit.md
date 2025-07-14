## HomeKit

> `/System/Library/Frameworks/HomeKit.framework/HomeKit`

```diff

-1092.3.10.1.2
-  __TEXT.__text: 0x261674
+1092.4.10.0.0
+  __TEXT.__text: 0x260414
   __TEXT.__auth_stubs: 0xcc0
-  __TEXT.__objc_methlist: 0x201c4
+  __TEXT.__objc_methlist: 0x20154
   __TEXT.__const: 0x290
-  __TEXT.__gcc_except_tab: 0x3fc0
-  __TEXT.__cstring: 0x25866
-  __TEXT.__oslogstring: 0x25183
+  __TEXT.__gcc_except_tab: 0x3fa0
+  __TEXT.__cstring: 0x258bd
+  __TEXT.__oslogstring: 0x24ffc
   __TEXT.__dlopen_cstrs: 0x3a2
   __TEXT.__ustring: 0x50
-  __TEXT.__unwind_info: 0x92a0
+  __TEXT.__unwind_info: 0x926c
   __TEXT.__objc_classname: 0x49a5
-  __TEXT.__objc_methname: 0x3fd0f
+  __TEXT.__objc_methname: 0x3fccf
   __TEXT.__objc_methtype: 0x77f8
-  __TEXT.__objc_stubs: 0x234a0
+  __TEXT.__objc_stubs: 0x23480
   __DATA_CONST.__got: 0x3a0
-  __DATA_CONST.__const: 0x6d68
+  __DATA_CONST.__const: 0x6d70
   __DATA_CONST.__objc_classlist: 0x1068
   __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x470
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x319f8
-  __DATA_CONST.__objc_selrefs: 0xbd08
+  __DATA_CONST.__objc_const: 0x31a00
+  __DATA_CONST.__objc_selrefs: 0xbcd8
   __DATA_CONST.__objc_arraydata: 0x1330
   __AUTH_CONST.__cfstring: 0x23500
   __AUTH_CONST.__objc_const: 0xf188
-  __AUTH_CONST.__const: 0x1920
+  __AUTH_CONST.__const: 0x1960
   __AUTH_CONST.__objc_intobj: 0x798
   __AUTH_CONST.__objc_dictobj: 0x848
   __AUTH_CONST.__objc_arrayobj: 0x540

   __DATA.__objc_protorefs: 0x98
   __DATA.__objc_classrefs: 0x1308
   __DATA.__objc_superrefs: 0xdd8
-  __DATA.__objc_ivar: 0x2188
-  __DATA.__data: 0x3608
+  __DATA.__objc_ivar: 0x218c
+  __DATA.__data: 0x3618
   __DATA.__common: 0x18
-  __DATA.__bss: 0x800
+  __DATA.__bss: 0x7f0
   __DATA_DIRTY.__objc_data: 0x2850
   __DATA_DIRTY.__bss: 0x1d0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2DD64732-A41F-3410-8404-4C7ED7FEEF4B
-  Functions: 12583
-  Symbols:   40278
-  CStrings:  23107
+  UUID: 57031298-2262-31F1-87F1-285D547D6ABA
+  Functions: 12575
+  Symbols:   40259
+  CStrings:  23099
 
Symbols:
+ +[HMSymptomsHandler symptomsHandlerUUIDFromAccessoryUUID:]
+ -[HMAccessory _createSymptomsHandler]
+ -[HMAccessory _updateHasSymptomsHandler:]
+ -[HMAccessory hasSymptomsHandler]
+ -[HMAccessory setHasSymptomsHandler:]
+ -[HMSymptomsHandler _handleSymptomStateUpdatedMessage:]
+ -[HMSymptomsHandler _subscribe]
+ -[HMSymptomsHandler _unsubscribe]
+ -[HMSymptomsHandler configure]
+ -[HMSymptomsHandler dealloc]
+ -[HMSymptomsHandler fixSessionFactory]
+ -[HMSymptomsHandler initWithAccessory:]
+ -[HMSymptomsHandler initWithUUID:context:logIdentifier:]
+ -[HMSymptomsHandler setFixSessionFactory:]
+ GCC_except_table1006
+ GCC_except_table10294
+ GCC_except_table10296
+ GCC_except_table10298
+ GCC_except_table10299
+ GCC_except_table10330
+ GCC_except_table10332
+ GCC_except_table10334
+ GCC_except_table10341
+ GCC_except_table10450
+ GCC_except_table10451
+ GCC_except_table10477
+ GCC_except_table10479
+ GCC_except_table10483
+ GCC_except_table10484
+ GCC_except_table10532
+ GCC_except_table10558
+ GCC_except_table10571
+ GCC_except_table10595
+ GCC_except_table10599
+ GCC_except_table10640
+ GCC_except_table10641
+ GCC_except_table10642
+ GCC_except_table10643
+ GCC_except_table10644
+ GCC_except_table10645
+ GCC_except_table10646
+ GCC_except_table10647
+ GCC_except_table10671
+ GCC_except_table10698
+ GCC_except_table1074
+ GCC_except_table1076
+ GCC_except_table1079
+ GCC_except_table10805
+ GCC_except_table10806
+ GCC_except_table10809
+ GCC_except_table1081
+ GCC_except_table10871
+ GCC_except_table10873
+ GCC_except_table10887
+ GCC_except_table10888
+ GCC_except_table10894
+ GCC_except_table10901
+ GCC_except_table10903
+ GCC_except_table11130
+ GCC_except_table11131
+ GCC_except_table11284
+ GCC_except_table11287
+ GCC_except_table11296
+ GCC_except_table11302
+ GCC_except_table11307
+ GCC_except_table11309
+ GCC_except_table11314
+ GCC_except_table1136
+ GCC_except_table11400
+ GCC_except_table11402
+ GCC_except_table11421
+ GCC_except_table11422
+ GCC_except_table11423
+ GCC_except_table11424
+ GCC_except_table11443
+ GCC_except_table11449
+ GCC_except_table11452
+ GCC_except_table11454
+ GCC_except_table11534
+ GCC_except_table11536
+ GCC_except_table11539
+ GCC_except_table11548
+ GCC_except_table11553
+ GCC_except_table11559
+ GCC_except_table11563
+ GCC_except_table11565
+ GCC_except_table11703
+ GCC_except_table11758
+ GCC_except_table11759
+ GCC_except_table11760
+ GCC_except_table11771
+ GCC_except_table11772
+ GCC_except_table11796
+ GCC_except_table11797
+ GCC_except_table11851
+ GCC_except_table11876
+ GCC_except_table11879
+ GCC_except_table12011
+ GCC_except_table12131
+ GCC_except_table12132
+ GCC_except_table12133
+ GCC_except_table12181
+ GCC_except_table12182
+ GCC_except_table12184
+ GCC_except_table12187
+ GCC_except_table12191
+ GCC_except_table12223
+ GCC_except_table12266
+ GCC_except_table12271
+ GCC_except_table12334
+ GCC_except_table12419
+ GCC_except_table12426
+ GCC_except_table12479
+ GCC_except_table12481
+ GCC_except_table12490
+ GCC_except_table12493
+ GCC_except_table1251
+ GCC_except_table12513
+ GCC_except_table12515
+ GCC_except_table12516
+ GCC_except_table1273
+ GCC_except_table1350
+ GCC_except_table1353
+ GCC_except_table1367
+ GCC_except_table1502
+ GCC_except_table1571
+ GCC_except_table1574
+ GCC_except_table1643
+ GCC_except_table1645
+ GCC_except_table1719
+ GCC_except_table1720
+ GCC_except_table1768
+ GCC_except_table1997
+ GCC_except_table2000
+ GCC_except_table2003
+ GCC_except_table2008
+ GCC_except_table2021
+ GCC_except_table2023
+ GCC_except_table2026
+ GCC_except_table2036
+ GCC_except_table2038
+ GCC_except_table2039
+ GCC_except_table2044
+ GCC_except_table2045
+ GCC_except_table2046
+ GCC_except_table2047
+ GCC_except_table2234
+ GCC_except_table2236
+ GCC_except_table2242
+ GCC_except_table2252
+ GCC_except_table2475
+ GCC_except_table2478
+ GCC_except_table2492
+ GCC_except_table2524
+ GCC_except_table2537
+ GCC_except_table2540
+ GCC_except_table2567
+ GCC_except_table2569
+ GCC_except_table2733
+ GCC_except_table2751
+ GCC_except_table2752
+ GCC_except_table2808
+ GCC_except_table2810
+ GCC_except_table2813
+ GCC_except_table2838
+ GCC_except_table2840
+ GCC_except_table2848
+ GCC_except_table2850
+ GCC_except_table2857
+ GCC_except_table2858
+ GCC_except_table2859
+ GCC_except_table2864
+ GCC_except_table2917
+ GCC_except_table2941
+ GCC_except_table2944
+ GCC_except_table2947
+ GCC_except_table2950
+ GCC_except_table2953
+ GCC_except_table2956
+ GCC_except_table2959
+ GCC_except_table3024
+ GCC_except_table3025
+ GCC_except_table3069
+ GCC_except_table3076
+ GCC_except_table3077
+ GCC_except_table3078
+ GCC_except_table3083
+ GCC_except_table3093
+ GCC_except_table3101
+ GCC_except_table3102
+ GCC_except_table3120
+ GCC_except_table3127
+ GCC_except_table3134
+ GCC_except_table3137
+ GCC_except_table3176
+ GCC_except_table3189
+ GCC_except_table3197
+ GCC_except_table3210
+ GCC_except_table3212
+ GCC_except_table3444
+ GCC_except_table3455
+ GCC_except_table3460
+ GCC_except_table3469
+ GCC_except_table3472
+ GCC_except_table3500
+ GCC_except_table3502
+ GCC_except_table3507
+ GCC_except_table3510
+ GCC_except_table3513
+ GCC_except_table3595
+ GCC_except_table3600
+ GCC_except_table3612
+ GCC_except_table3615
+ GCC_except_table3617
+ GCC_except_table3620
+ GCC_except_table3627
+ GCC_except_table3680
+ GCC_except_table3746
+ GCC_except_table3761
+ GCC_except_table3764
+ GCC_except_table3878
+ GCC_except_table3879
+ GCC_except_table3881
+ GCC_except_table3886
+ GCC_except_table3893
+ GCC_except_table3895
+ GCC_except_table3903
+ GCC_except_table4102
+ GCC_except_table4105
+ GCC_except_table4117
+ GCC_except_table4189
+ GCC_except_table4208
+ GCC_except_table4295
+ GCC_except_table4410
+ GCC_except_table4415
+ GCC_except_table4416
+ GCC_except_table4424
+ GCC_except_table4426
+ GCC_except_table4451
+ GCC_except_table4452
+ GCC_except_table4453
+ GCC_except_table4454
+ GCC_except_table4514
+ GCC_except_table4524
+ GCC_except_table4589
+ GCC_except_table4591
+ GCC_except_table4635
+ GCC_except_table4636
+ GCC_except_table4710
+ GCC_except_table4797
+ GCC_except_table4798
+ GCC_except_table4806
+ GCC_except_table4835
+ GCC_except_table4837
+ GCC_except_table4856
+ GCC_except_table4902
+ GCC_except_table4952
+ GCC_except_table5038
+ GCC_except_table5058
+ GCC_except_table5059
+ GCC_except_table5060
+ GCC_except_table5062
+ GCC_except_table5068
+ GCC_except_table5274
+ GCC_except_table5280
+ GCC_except_table5282
+ GCC_except_table5292
+ GCC_except_table5293
+ GCC_except_table5540
+ GCC_except_table5649
+ GCC_except_table5655
+ GCC_except_table5667
+ GCC_except_table5743
+ GCC_except_table5749
+ GCC_except_table5751
+ GCC_except_table5888
+ GCC_except_table6045
+ GCC_except_table6046
+ GCC_except_table6071
+ GCC_except_table6073
+ GCC_except_table6079
+ GCC_except_table6087
+ GCC_except_table6102
+ GCC_except_table6112
+ GCC_except_table6126
+ GCC_except_table6131
+ GCC_except_table6165
+ GCC_except_table6176
+ GCC_except_table6182
+ GCC_except_table6186
+ GCC_except_table6194
+ GCC_except_table6199
+ GCC_except_table6213
+ GCC_except_table6218
+ GCC_except_table6226
+ GCC_except_table6228
+ GCC_except_table6231
+ GCC_except_table6236
+ GCC_except_table6248
+ GCC_except_table6252
+ GCC_except_table6280
+ GCC_except_table6286
+ GCC_except_table6311
+ GCC_except_table6316
+ GCC_except_table6320
+ GCC_except_table6349
+ GCC_except_table6353
+ GCC_except_table6355
+ GCC_except_table6494
+ GCC_except_table6500
+ GCC_except_table6580
+ GCC_except_table6602
+ GCC_except_table6607
+ GCC_except_table6615
+ GCC_except_table6658
+ GCC_except_table6660
+ GCC_except_table6662
+ GCC_except_table6674
+ GCC_except_table6685
+ GCC_except_table6711
+ GCC_except_table6720
+ GCC_except_table6730
+ GCC_except_table6733
+ GCC_except_table6736
+ GCC_except_table6739
+ GCC_except_table6748
+ GCC_except_table6758
+ GCC_except_table6782
+ GCC_except_table6785
+ GCC_except_table6788
+ GCC_except_table6791
+ GCC_except_table6794
+ GCC_except_table6797
+ GCC_except_table6800
+ GCC_except_table6803
+ GCC_except_table6806
+ GCC_except_table6809
+ GCC_except_table6812
+ GCC_except_table6815
+ GCC_except_table6818
+ GCC_except_table6821
+ GCC_except_table6824
+ GCC_except_table6827
+ GCC_except_table6830
+ GCC_except_table6846
+ GCC_except_table6847
+ GCC_except_table6855
+ GCC_except_table6872
+ GCC_except_table6874
+ GCC_except_table6899
+ GCC_except_table6913
+ GCC_except_table6915
+ GCC_except_table6935
+ GCC_except_table6939
+ GCC_except_table7068
+ GCC_except_table7274
+ GCC_except_table7344
+ GCC_except_table7447
+ GCC_except_table7463
+ GCC_except_table7538
+ GCC_except_table7556
+ GCC_except_table7564
+ GCC_except_table7566
+ GCC_except_table7567
+ GCC_except_table7699
+ GCC_except_table7702
+ GCC_except_table7713
+ GCC_except_table7716
+ GCC_except_table7752
+ GCC_except_table7754
+ GCC_except_table7772
+ GCC_except_table7780
+ GCC_except_table7782
+ GCC_except_table7784
+ GCC_except_table7786
+ GCC_except_table7793
+ GCC_except_table7799
+ GCC_except_table7801
+ GCC_except_table7803
+ GCC_except_table7813
+ GCC_except_table7824
+ GCC_except_table7826
+ GCC_except_table7869
+ GCC_except_table7871
+ GCC_except_table7881
+ GCC_except_table7883
+ GCC_except_table7885
+ GCC_except_table7897
+ GCC_except_table7909
+ GCC_except_table7911
+ GCC_except_table7913
+ GCC_except_table7915
+ GCC_except_table7934
+ GCC_except_table8084
+ GCC_except_table8086
+ GCC_except_table8087
+ GCC_except_table8088
+ GCC_except_table8090
+ GCC_except_table8093
+ GCC_except_table8130
+ GCC_except_table8133
+ GCC_except_table8134
+ GCC_except_table8137
+ GCC_except_table8140
+ GCC_except_table8185
+ GCC_except_table8186
+ GCC_except_table8187
+ GCC_except_table8197
+ GCC_except_table8259
+ GCC_except_table8260
+ GCC_except_table8261
+ GCC_except_table8298
+ GCC_except_table8480
+ GCC_except_table8481
+ GCC_except_table8482
+ GCC_except_table8486
+ GCC_except_table8541
+ GCC_except_table8562
+ GCC_except_table8633
+ GCC_except_table8639
+ GCC_except_table8643
+ GCC_except_table8645
+ GCC_except_table8702
+ GCC_except_table8703
+ GCC_except_table8705
+ GCC_except_table8730
+ GCC_except_table8758
+ GCC_except_table8916
+ GCC_except_table8968
+ GCC_except_table8975
+ GCC_except_table8980
+ GCC_except_table8985
+ GCC_except_table8989
+ GCC_except_table9002
+ GCC_except_table9005
+ GCC_except_table9008
+ GCC_except_table9040
+ GCC_except_table9060
+ GCC_except_table9061
+ GCC_except_table9062
+ GCC_except_table9099
+ GCC_except_table9100
+ GCC_except_table9104
+ GCC_except_table9106
+ GCC_except_table9167
+ GCC_except_table9194
+ GCC_except_table9197
+ GCC_except_table9199
+ GCC_except_table9201
+ GCC_except_table9203
+ GCC_except_table9223
+ GCC_except_table9226
+ GCC_except_table9233
+ GCC_except_table9237
+ GCC_except_table9243
+ GCC_except_table9249
+ GCC_except_table9252
+ GCC_except_table9261
+ GCC_except_table9274
+ GCC_except_table9288
+ GCC_except_table9499
+ GCC_except_table9512
+ GCC_except_table9561
+ GCC_except_table9562
+ GCC_except_table9564
+ GCC_except_table9568
+ GCC_except_table9628
+ GCC_except_table963
+ GCC_except_table9631
+ GCC_except_table9632
+ GCC_except_table974
+ GCC_except_table9942
+ GCC_except_table997
+ GCC_except_table9981
+ GCC_except_table9994
+ _CoreAnalyticsLibraryCore.frameworkLibrary.35957
+ _HMAccessoryHasSymptomsHandlerCodingKey
+ _HMSymptomsHandlerInitiateFixMessage
+ _HMSymptomsHandlerSubscribeMessage
+ _HMSymptomsHandlerSymptomStateUpdatedMessage
+ _HMSymptomsHandlerSymptomsMessageKey
+ _HMSymptomsHandlerUnsubscribeMessage
+ _IDSFoundationLibraryCore.39527
+ _IDSFoundationLibraryCore.frameworkLibrary.39529
+ _OBJC_IVAR_$_HMAccessory._hasSymptomsHandler
+ _OBJC_IVAR_$_HMSymptomsHandler._fixSessionFactory
+ _UIKitLibrary.39761
+ _UIKitLibraryCore.39755
+ _UIKitLibraryCore.frameworkLibrary.39770
+ __OBJC_$_PROP_LIST_HMApplicationData.11442
+ ___29-[HMAccessory initWithCoder:]_block_invoke
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke.1099
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke.1100
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke.1102
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke_2.1104
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke_2.1107
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke_3.1105
+ ___30-[HMAccessory _mergeServices:]_block_invoke.920
+ ___30-[HMAccessory _mergeServices:]_block_invoke.922
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1075
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1077
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1079
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1080
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1082
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1087
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1089
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1090
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1092
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.924
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.925
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.929
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.932
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.949
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.954
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.958
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1076
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1078
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1083
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1086
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1095
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.926
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.930
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.933
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.950
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.955
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.959
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_3.951
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_3.956
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_3.961
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_4.962
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_5.963
+ ___41-[HMAccessory _updateHasSymptomsHandler:]_block_invoke
+ ___41-[HMAccessory _updateHasSymptomsHandler:]_block_invoke.1136
+ ___41-[HMAccessory _updateHasSymptomsHandler:]_block_invoke.1138
+ ___41-[HMAccessory _updateHasSymptomsHandler:]_block_invoke_2
+ ___45-[HMAccessory _handleCharacteristicsUpdated:]_block_invoke.1120
+ ___48-[HMAccessory _deleteSiriHistoryWithCompletion:]_block_invoke.1121
+ ___48-[HMAccessory _deleteSiriHistoryWithCompletion:]_block_invoke.1122
+ ___56-[HMSymptomsHandler initWithUUID:context:logIdentifier:]_block_invoke
+ ___63-[HMAccessory pairingIdentityWithPrivateKey:completionHandler:]_block_invoke.854
+ ___63-[HMAccessory pairingIdentityWithPrivateKey:completionHandler:]_block_invoke.856
+ ___Block_byref_object_copy_.14400
+ ___Block_byref_object_copy_.14713
+ ___Block_byref_object_copy_.21392
+ ___Block_byref_object_copy_.23446
+ ___Block_byref_object_copy_.27573
+ ___Block_byref_object_copy_.29320
+ ___Block_byref_object_copy_.35844
+ ___Block_byref_object_copy_.38692
+ ___Block_byref_object_copy_.39756
+ ___Block_byref_object_copy_.59891
+ ___Block_byref_object_dispose_.14401
+ ___Block_byref_object_dispose_.14714
+ ___Block_byref_object_dispose_.21393
+ ___Block_byref_object_dispose_.23447
+ ___Block_byref_object_dispose_.27574
+ ___Block_byref_object_dispose_.29321
+ ___Block_byref_object_dispose_.35845
+ ___Block_byref_object_dispose_.38693
+ ___Block_byref_object_dispose_.39757
+ ___Block_byref_object_dispose_.59892
+ ___CoreAnalyticsLibraryCore_block_invoke.35958
+ ___IDSFoundationLibraryCore_block_invoke.39530
+ ___UIKitLibraryCore_block_invoke.39771
+ ___block_descriptor_32_e66_"HMSymptomFixSession"32?0"HMSymptom"8"NSUUID"16"_HMContext"24l
+ ___block_literal_global.101.35965
+ ___block_literal_global.10514
+ ___block_literal_global.1115
+ ___block_literal_global.11503
+ ___block_literal_global.12.45521
+ ___block_literal_global.121.48459
+ ___block_literal_global.12472
+ ___block_literal_global.12619
+ ___block_literal_global.13073
+ ___block_literal_global.13266
+ ___block_literal_global.13833
+ ___block_literal_global.14166
+ ___block_literal_global.14484
+ ___block_literal_global.15078
+ ___block_literal_global.16135
+ ___block_literal_global.16666
+ ___block_literal_global.16857
+ ___block_literal_global.16989
+ ___block_literal_global.17.17789
+ ___block_literal_global.17151
+ ___block_literal_global.175.16165
+ ___block_literal_global.17796
+ ___block_literal_global.18463
+ ___block_literal_global.18868
+ ___block_literal_global.19.14151
+ ___block_literal_global.192.22669
+ ___block_literal_global.19419
+ ___block_literal_global.19743
+ ___block_literal_global.20775
+ ___block_literal_global.21430
+ ___block_literal_global.21703
+ ___block_literal_global.22175
+ ___block_literal_global.22390
+ ___block_literal_global.22675
+ ___block_literal_global.22810
+ ___block_literal_global.23056
+ ___block_literal_global.23307
+ ___block_literal_global.23470
+ ___block_literal_global.23562
+ ___block_literal_global.26077
+ ___block_literal_global.26212
+ ___block_literal_global.26687
+ ___block_literal_global.27435
+ ___block_literal_global.27730
+ ___block_literal_global.28069
+ ___block_literal_global.28281
+ ___block_literal_global.28559
+ ___block_literal_global.28633
+ ___block_literal_global.29502
+ ___block_literal_global.29858
+ ___block_literal_global.30.17779
+ ___block_literal_global.30.7694
+ ___block_literal_global.30129
+ ___block_literal_global.30965
+ ___block_literal_global.31333
+ ___block_literal_global.32411
+ ___block_literal_global.33.59235
+ ___block_literal_global.33357
+ ___block_literal_global.33588
+ ___block_literal_global.33811
+ ___block_literal_global.34760
+ ___block_literal_global.35952
+ ___block_literal_global.36202
+ ___block_literal_global.3631
+ ___block_literal_global.36538
+ ___block_literal_global.37163
+ ___block_literal_global.37965
+ ___block_literal_global.38090
+ ___block_literal_global.3831
+ ___block_literal_global.38362
+ ___block_literal_global.3922
+ ___block_literal_global.39593
+ ___block_literal_global.39687
+ ___block_literal_global.40396
+ ___block_literal_global.40585
+ ___block_literal_global.41212
+ ___block_literal_global.41838
+ ___block_literal_global.42252
+ ___block_literal_global.42571
+ ___block_literal_global.43246
+ ___block_literal_global.44133
+ ___block_literal_global.45243
+ ___block_literal_global.45533
+ ___block_literal_global.45799
+ ___block_literal_global.45993
+ ___block_literal_global.46221
+ ___block_literal_global.46926
+ ___block_literal_global.47045
+ ___block_literal_global.47776
+ ___block_literal_global.48213
+ ___block_literal_global.48547
+ ___block_literal_global.49460
+ ___block_literal_global.5093
+ ___block_literal_global.52090
+ ___block_literal_global.52793
+ ___block_literal_global.53
+ ___block_literal_global.54048
+ ___block_literal_global.54683
+ ___block_literal_global.5489
+ ___block_literal_global.55214
+ ___block_literal_global.55526
+ ___block_literal_global.56023
+ ___block_literal_global.56195
+ ___block_literal_global.5625
+ ___block_literal_global.56583
+ ___block_literal_global.56827
+ ___block_literal_global.58473
+ ___block_literal_global.58639
+ ___block_literal_global.58976
+ ___block_literal_global.59241
+ ___block_literal_global.59601
+ ___block_literal_global.59889
+ ___block_literal_global.60183
+ ___block_literal_global.6143
+ ___block_literal_global.6624
+ ___block_literal_global.6898
+ ___block_literal_global.73.21681
+ ___block_literal_global.7359
+ ___block_literal_global.7476
+ ___block_literal_global.75.36155
+ ___block_literal_global.76.25844
+ ___block_literal_global.7712
+ ___block_literal_global.8168
+ ___block_literal_global.84.59903
+ ___block_literal_global.8651
+ ___block_literal_global.8932
+ ___block_literal_global.9109
+ ___block_literal_global.9538
+ ___block_literal_global.9802
+ ___getAnalyticsSendEventLazySymbolLoc_block_invoke.35955
+ ___getNSCharacterEncodingDocumentAttributeSymbolLoc_block_invoke.39766
+ ___getNSDocumentTypeDocumentAttributeSymbolLoc_block_invoke.39760
+ __unnamed_array_storage.14417
+ __unnamed_array_storage.22582
+ __unnamed_array_storage.227.25991
+ __unnamed_array_storage.239.25990
+ __unnamed_array_storage.251.25994
+ __unnamed_array_storage.26067
+ __unnamed_array_storage.29199
+ __unnamed_array_storage.54170
+ __unnamed_array_storage.55651
+ __unnamed_array_storage.59092
+ _audit_stringCoreAnalytics.35961
+ _audit_stringIDSFoundation.39532
+ _audit_stringUIKit.39773
+ _getAnalyticsSendEventLazySymbolLoc.ptr.35954
+ _getNSCharacterEncodingDocumentAttributeSymbolLoc.ptr.39765
+ _getNSDocumentTypeDocumentAttributeSymbolLoc.ptr.39759
+ _logCategory._hmf_once_t0.12618
+ _logCategory._hmf_once_t0.21702
+ _logCategory._hmf_once_t0.28280
+ _logCategory._hmf_once_t0.28632
+ _logCategory._hmf_once_t0.40395
+ _logCategory._hmf_once_t0.40584
+ _logCategory._hmf_once_t0.41211
+ _logCategory._hmf_once_t0.56826
+ _logCategory._hmf_once_t1.16988
+ _logCategory._hmf_once_t1.18867
+ _logCategory._hmf_once_t1.36178
+ _logCategory._hmf_once_t1.41837
+ _logCategory._hmf_once_t1.45520
+ _logCategory._hmf_once_t1.47044
+ _logCategory._hmf_once_t1.52089
+ _logCategory._hmf_once_t15.56582
+ _logCategory._hmf_once_t16.33587
+ _logCategory._hmf_once_t16.58638
+ _logCategory._hmf_once_t17.37957
+ _logCategory._hmf_once_t19.13292
+ _logCategory._hmf_once_t2.26211
+ _logCategory._hmf_once_t2.29857
+ _logCategory._hmf_once_t20.5624
+ _logCategory._hmf_once_t22.23055
+ _logCategory._hmf_once_t24.36532
+ _logCategory._hmf_once_t25.23306
+ _logCategory._hmf_once_t25.59600
+ _logCategory._hmf_once_t26.48294
+ _logCategory._hmf_once_t27.47775
+ _logCategory._hmf_once_t27.55525
+ _logCategory._hmf_once_t3.38089
+ _logCategory._hmf_once_t3.59234
+ _logCategory._hmf_once_t31.21429
+ _logCategory._hmf_once_t31.58472
+ _logCategory._hmf_once_t310
+ _logCategory._hmf_once_t33.48572
+ _logCategory._hmf_once_t34.14479
+ _logCategory._hmf_once_t34.18462
+ _logCategory._hmf_once_t35.34759
+ _logCategory._hmf_once_t394
+ _logCategory._hmf_once_t4.5488
+ _logCategory._hmf_once_t51
+ _logCategory._hmf_once_t6.30964
+ _logCategory._hmf_once_t6.33356
+ _logCategory._hmf_once_t6.52792
+ _logCategory._hmf_once_t64.54047
+ _logCategory._hmf_once_t7.23561
+ _logCategory._hmf_once_t7.46925
+ _logCategory._hmf_once_t8.33810
+ _logCategory._hmf_once_t8.43245
+ _logCategory._hmf_once_t8.46011
+ _logCategory._hmf_once_v1.12620
+ _logCategory._hmf_once_v1.21704
+ _logCategory._hmf_once_v1.28282
+ _logCategory._hmf_once_v1.28634
+ _logCategory._hmf_once_v1.40397
+ _logCategory._hmf_once_v1.40586
+ _logCategory._hmf_once_v1.41213
+ _logCategory._hmf_once_v1.56828
+ _logCategory._hmf_once_v16.56584
+ _logCategory._hmf_once_v17.33589
+ _logCategory._hmf_once_v17.58640
+ _logCategory._hmf_once_v18.37958
+ _logCategory._hmf_once_v2.16990
+ _logCategory._hmf_once_v2.18869
+ _logCategory._hmf_once_v2.36179
+ _logCategory._hmf_once_v2.41839
+ _logCategory._hmf_once_v2.45522
+ _logCategory._hmf_once_v2.47046
+ _logCategory._hmf_once_v2.52091
+ _logCategory._hmf_once_v20.13293
+ _logCategory._hmf_once_v21.5626
+ _logCategory._hmf_once_v23.23057
+ _logCategory._hmf_once_v25.36533
+ _logCategory._hmf_once_v26.23308
+ _logCategory._hmf_once_v26.59602
+ _logCategory._hmf_once_v27.48295
+ _logCategory._hmf_once_v28.47777
+ _logCategory._hmf_once_v28.55527
+ _logCategory._hmf_once_v3.26213
+ _logCategory._hmf_once_v3.29859
+ _logCategory._hmf_once_v311
+ _logCategory._hmf_once_v32.21431
+ _logCategory._hmf_once_v32.58474
+ _logCategory._hmf_once_v34.48573
+ _logCategory._hmf_once_v35.14480
+ _logCategory._hmf_once_v35.18464
+ _logCategory._hmf_once_v36.34761
+ _logCategory._hmf_once_v395
+ _logCategory._hmf_once_v4.38091
+ _logCategory._hmf_once_v4.59236
+ _logCategory._hmf_once_v5.5490
+ _logCategory._hmf_once_v52
+ _logCategory._hmf_once_v65.54049
+ _logCategory._hmf_once_v7.30966
+ _logCategory._hmf_once_v7.33358
+ _logCategory._hmf_once_v7.52794
+ _logCategory._hmf_once_v8.23563
+ _logCategory._hmf_once_v8.46927
+ _logCategory._hmf_once_v9.33812
+ _logCategory._hmf_once_v9.43247
+ _logCategory._hmf_once_v9.46012
+ _objc_msgSend$_createSymptomsHandler
+ _objc_msgSend$_updateHasSymptomsHandler:
+ _objc_msgSend$fixSessionFactory
+ _objc_msgSend$hasSymptomsHandler
+ _objc_msgSend$initWithUUID:context:logIdentifier:
+ _objc_msgSend$setHasSymptomsHandler:
+ _objc_msgSend$symptomsHandlerUUIDFromAccessoryUUID:
+ _sharedInstance.onceToken.37964
+ _sharedManager.onceToken.55668
+ _supportedValueClasses.onceToken.45798
+ _supportedValueClasses.onceToken.54013
+ _supportedValueClasses.supportedValueClasses.45800
+ _supportedValueClasses.supportedValueClasses.54014
+ _unconfigureQueue.onceToken.36537
+ _unconfigureQueue.unconfigureQueue.36539
- +[HMSymptom archive:]
- +[HMSymptom archiveSymptomDict:]
- +[HMSymptom unarchive:]
- +[HMSymptom unarchiveSymptomDict:]
- +[HMSymptomsHandler supportsSecureCoding]
- -[HMAccessory __updateSymptomsHandler:]
- -[HMAccessory _handleControlTargetsUpdatedMessage:]
- -[HMAccessory _handleSymptomsHandlerUpdatedMessage:]
- -[HMAccessory _notifyClientsOfSymptomsHandlerAddedOrRemoved:]
- -[HMAccessory addControlTargetUUIDs:]
- -[HMAccessory removeControlTargetUUIDs:]
- -[HMAccessory resetControlTargetUUIDs]
- -[HMSymptomsHandler __configureWithContext:]
- -[HMSymptomsHandler _handleSFDeviceIdentifierUpdated:]
- -[HMSymptomsHandler _handleSymptomsUpdated:]
- -[HMSymptomsHandler _registerForMessages]
- -[HMSymptomsHandler _unconfigureContext]
- -[HMSymptomsHandler _unconfigure]
- -[HMSymptomsHandler encodeWithCoder:]
- -[HMSymptomsHandler initWithCoder:]
- -[HMSymptomsHandler initWithUUID:logIdentifier:]
- -[HMSymptomsHandler mergeFromNewObject:]
- -[HMSymptomsHandler uniqueIdentifier]
- GCC_except_table10002
- GCC_except_table1001
- GCC_except_table1010
- GCC_except_table10302
- GCC_except_table10304
- GCC_except_table10306
- GCC_except_table10307
- GCC_except_table10338
- GCC_except_table10348
- GCC_except_table10349
- GCC_except_table10350
- GCC_except_table10458
- GCC_except_table10459
- GCC_except_table10485
- GCC_except_table10487
- GCC_except_table10491
- GCC_except_table10492
- GCC_except_table10540
- GCC_except_table10566
- GCC_except_table10579
- GCC_except_table10603
- GCC_except_table10607
- GCC_except_table10655
- GCC_except_table10656
- GCC_except_table10657
- GCC_except_table10658
- GCC_except_table10659
- GCC_except_table10660
- GCC_except_table10661
- GCC_except_table10662
- GCC_except_table10679
- GCC_except_table10706
- GCC_except_table1078
- GCC_except_table1080
- GCC_except_table10813
- GCC_except_table10814
- GCC_except_table10817
- GCC_except_table1085
- GCC_except_table10879
- GCC_except_table10889
- GCC_except_table10895
- GCC_except_table10904
- GCC_except_table10909
- GCC_except_table1091
- GCC_except_table10910
- GCC_except_table10911
- GCC_except_table11138
- GCC_except_table11139
- GCC_except_table11295
- GCC_except_table11300
- GCC_except_table11304
- GCC_except_table11310
- GCC_except_table11322
- GCC_except_table11323
- GCC_except_table11325
- GCC_except_table1140
- GCC_except_table11408
- GCC_except_table11410
- GCC_except_table11430
- GCC_except_table11431
- GCC_except_table11432
- GCC_except_table11437
- GCC_except_table11451
- GCC_except_table11457
- GCC_except_table11460
- GCC_except_table11462
- GCC_except_table11542
- GCC_except_table11544
- GCC_except_table11555
- GCC_except_table11556
- GCC_except_table11571
- GCC_except_table11573
- GCC_except_table11575
- GCC_except_table11577
- GCC_except_table11711
- GCC_except_table11766
- GCC_except_table11767
- GCC_except_table11768
- GCC_except_table11779
- GCC_except_table11780
- GCC_except_table11804
- GCC_except_table11805
- GCC_except_table11859
- GCC_except_table11884
- GCC_except_table11887
- GCC_except_table12019
- GCC_except_table12139
- GCC_except_table12140
- GCC_except_table12141
- GCC_except_table12190
- GCC_except_table12192
- GCC_except_table12195
- GCC_except_table12197
- GCC_except_table12199
- GCC_except_table12231
- GCC_except_table12279
- GCC_except_table12282
- GCC_except_table12342
- GCC_except_table12427
- GCC_except_table12434
- GCC_except_table12487
- GCC_except_table12489
- GCC_except_table12498
- GCC_except_table12501
- GCC_except_table12521
- GCC_except_table12523
- GCC_except_table12524
- GCC_except_table1255
- GCC_except_table1277
- GCC_except_table1354
- GCC_except_table1357
- GCC_except_table1371
- GCC_except_table1506
- GCC_except_table1575
- GCC_except_table1578
- GCC_except_table1647
- GCC_except_table1649
- GCC_except_table1723
- GCC_except_table1724
- GCC_except_table1772
- GCC_except_table2001
- GCC_except_table2004
- GCC_except_table2007
- GCC_except_table2016
- GCC_except_table2025
- GCC_except_table2027
- GCC_except_table2030
- GCC_except_table2040
- GCC_except_table2042
- GCC_except_table2043
- GCC_except_table2048
- GCC_except_table2049
- GCC_except_table2050
- GCC_except_table2051
- GCC_except_table2238
- GCC_except_table2248
- GCC_except_table2250
- GCC_except_table2256
- GCC_except_table2479
- GCC_except_table2482
- GCC_except_table2496
- GCC_except_table2528
- GCC_except_table2545
- GCC_except_table2548
- GCC_except_table2575
- GCC_except_table2577
- GCC_except_table2737
- GCC_except_table2755
- GCC_except_table2756
- GCC_except_table2812
- GCC_except_table2817
- GCC_except_table2818
- GCC_except_table2842
- GCC_except_table2844
- GCC_except_table2852
- GCC_except_table2854
- GCC_except_table2866
- GCC_except_table2867
- GCC_except_table2868
- GCC_except_table2869
- GCC_except_table2921
- GCC_except_table2945
- GCC_except_table2948
- GCC_except_table2951
- GCC_except_table2954
- GCC_except_table2957
- GCC_except_table2960
- GCC_except_table2963
- GCC_except_table3028
- GCC_except_table3029
- GCC_except_table3073
- GCC_except_table3080
- GCC_except_table3086
- GCC_except_table3087
- GCC_except_table3089
- GCC_except_table3097
- GCC_except_table3105
- GCC_except_table3106
- GCC_except_table3124
- GCC_except_table3135
- GCC_except_table3138
- GCC_except_table3141
- GCC_except_table3188
- GCC_except_table3193
- GCC_except_table3205
- GCC_except_table3214
- GCC_except_table3216
- GCC_except_table3456
- GCC_except_table3464
- GCC_except_table3467
- GCC_except_table3473
- GCC_except_table3480
- GCC_except_table3506
- GCC_except_table3511
- GCC_except_table3512
- GCC_except_table3514
- GCC_except_table3517
- GCC_except_table3599
- GCC_except_table3604
- GCC_except_table3616
- GCC_except_table3619
- GCC_except_table3621
- GCC_except_table3624
- GCC_except_table3631
- GCC_except_table3684
- GCC_except_table3750
- GCC_except_table3765
- GCC_except_table3768
- GCC_except_table3882
- GCC_except_table3883
- GCC_except_table3885
- GCC_except_table3894
- GCC_except_table3897
- GCC_except_table3899
- GCC_except_table3907
- GCC_except_table4106
- GCC_except_table4109
- GCC_except_table4121
- GCC_except_table4193
- GCC_except_table4212
- GCC_except_table4299
- GCC_except_table4414
- GCC_except_table4419
- GCC_except_table4420
- GCC_except_table4428
- GCC_except_table4430
- GCC_except_table4455
- GCC_except_table4456
- GCC_except_table4457
- GCC_except_table4458
- GCC_except_table4518
- GCC_except_table4528
- GCC_except_table4595
- GCC_except_table4597
- GCC_except_table4639
- GCC_except_table4642
- GCC_except_table4643
- GCC_except_table4717
- GCC_except_table4805
- GCC_except_table4811
- GCC_except_table4813
- GCC_except_table4842
- GCC_except_table4844
- GCC_except_table4863
- GCC_except_table4909
- GCC_except_table4959
- GCC_except_table5045
- GCC_except_table5067
- GCC_except_table5069
- GCC_except_table5072
- GCC_except_table5073
- GCC_except_table5075
- GCC_except_table5281
- GCC_except_table5287
- GCC_except_table5289
- GCC_except_table5299
- GCC_except_table5300
- GCC_except_table5547
- GCC_except_table5656
- GCC_except_table5669
- GCC_except_table5674
- GCC_except_table5750
- GCC_except_table5756
- GCC_except_table5758
- GCC_except_table5895
- GCC_except_table6052
- GCC_except_table6053
- GCC_except_table6078
- GCC_except_table6080
- GCC_except_table6086
- GCC_except_table6094
- GCC_except_table6116
- GCC_except_table6119
- GCC_except_table6133
- GCC_except_table6138
- GCC_except_table6172
- GCC_except_table6183
- GCC_except_table6189
- GCC_except_table6193
- GCC_except_table6201
- GCC_except_table6206
- GCC_except_table6220
- GCC_except_table6225
- GCC_except_table6233
- GCC_except_table6235
- GCC_except_table6238
- GCC_except_table6250
- GCC_except_table6255
- GCC_except_table6259
- GCC_except_table6287
- GCC_except_table6293
- GCC_except_table6318
- GCC_except_table6323
- GCC_except_table6327
- GCC_except_table6360
- GCC_except_table6362
- GCC_except_table6363
- GCC_except_table6501
- GCC_except_table6507
- GCC_except_table6587
- GCC_except_table6609
- GCC_except_table6614
- GCC_except_table6622
- GCC_except_table6665
- GCC_except_table6667
- GCC_except_table6669
- GCC_except_table6681
- GCC_except_table6692
- GCC_except_table6718
- GCC_except_table6734
- GCC_except_table6737
- GCC_except_table6740
- GCC_except_table6743
- GCC_except_table6746
- GCC_except_table6755
- GCC_except_table6765
- GCC_except_table6789
- GCC_except_table6792
- GCC_except_table6795
- GCC_except_table6798
- GCC_except_table6801
- GCC_except_table6804
- GCC_except_table6807
- GCC_except_table6810
- GCC_except_table6813
- GCC_except_table6816
- GCC_except_table6819
- GCC_except_table6822
- GCC_except_table6825
- GCC_except_table6828
- GCC_except_table6831
- GCC_except_table6837
- GCC_except_table6841
- GCC_except_table6853
- GCC_except_table6854
- GCC_except_table6862
- GCC_except_table6879
- GCC_except_table6881
- GCC_except_table6906
- GCC_except_table6920
- GCC_except_table6922
- GCC_except_table6942
- GCC_except_table6946
- GCC_except_table7075
- GCC_except_table7281
- GCC_except_table7351
- GCC_except_table7457
- GCC_except_table7468
- GCC_except_table7544
- GCC_except_table7568
- GCC_except_table7570
- GCC_except_table7572
- GCC_except_table7573
- GCC_except_table7704
- GCC_except_table7707
- GCC_except_table7723
- GCC_except_table7726
- GCC_except_table7757
- GCC_except_table7759
- GCC_except_table7777
- GCC_except_table7785
- GCC_except_table7787
- GCC_except_table7789
- GCC_except_table7791
- GCC_except_table7798
- GCC_except_table7806
- GCC_except_table7808
- GCC_except_table7809
- GCC_except_table7819
- GCC_except_table7820
- GCC_except_table7821
- GCC_except_table7832
- GCC_except_table7834
- GCC_except_table7877
- GCC_except_table7889
- GCC_except_table7891
- GCC_except_table7895
- GCC_except_table7901
- GCC_except_table7905
- GCC_except_table7917
- GCC_except_table7919
- GCC_except_table7921
- GCC_except_table7923
- GCC_except_table7942
- GCC_except_table8095
- GCC_except_table8096
- GCC_except_table8098
- GCC_except_table8100
- GCC_except_table8101
- GCC_except_table8102
- GCC_except_table8138
- GCC_except_table8142
- GCC_except_table8145
- GCC_except_table8148
- GCC_except_table8149
- GCC_except_table8193
- GCC_except_table8202
- GCC_except_table8203
- GCC_except_table8205
- GCC_except_table8267
- GCC_except_table8268
- GCC_except_table8269
- GCC_except_table8306
- GCC_except_table8488
- GCC_except_table8489
- GCC_except_table8490
- GCC_except_table8494
- GCC_except_table8549
- GCC_except_table8570
- GCC_except_table8647
- GCC_except_table8649
- GCC_except_table8651
- GCC_except_table8661
- GCC_except_table8710
- GCC_except_table8711
- GCC_except_table8713
- GCC_except_table8738
- GCC_except_table8766
- GCC_except_table8924
- GCC_except_table8983
- GCC_except_table8988
- GCC_except_table8993
- GCC_except_table8997
- GCC_except_table9013
- GCC_except_table9016
- GCC_except_table9018
- GCC_except_table9048
- GCC_except_table9068
- GCC_except_table9069
- GCC_except_table9070
- GCC_except_table9107
- GCC_except_table9112
- GCC_except_table9114
- GCC_except_table9116
- GCC_except_table9175
- GCC_except_table9202
- GCC_except_table9207
- GCC_except_table9209
- GCC_except_table9221
- GCC_except_table9227
- GCC_except_table9231
- GCC_except_table9234
- GCC_except_table9241
- GCC_except_table9245
- GCC_except_table9251
- GCC_except_table9257
- GCC_except_table9268
- GCC_except_table9269
- GCC_except_table9282
- GCC_except_table9296
- GCC_except_table9507
- GCC_except_table9520
- GCC_except_table9569
- GCC_except_table9570
- GCC_except_table9576
- GCC_except_table9580
- GCC_except_table9636
- GCC_except_table9639
- GCC_except_table9640
- GCC_except_table971
- GCC_except_table978
- GCC_except_table9950
- GCC_except_table9989
- _CoreAnalyticsLibraryCore.frameworkLibrary.35973
- _HMAccessoryControlTargetsMessageKey
- _HMAccessoryControlTargetsUpdatedMessage
- _HMAccessorySymptomsHandlerUpdatedMessage
- _HMSymptomsHandlerCodingKey
- _HMSymptomsHandlerFixErrorMessage
- _HMSymptomsHandlerSFDeviceIdentifierCodingKey
- _HMSymptomsHandlerSFDeviceIdentifierUpdatedMessage
- _HMSymptomsHandlerSymptomsUpdatedMessage
- _IDSFoundationLibraryCore.39539
- _IDSFoundationLibraryCore.frameworkLibrary.39541
- _OBJC_IVAR_$_HMSymptomsHandler._uniqueIdentifier
- _UIKitLibrary.39773
- _UIKitLibraryCore.39767
- _UIKitLibraryCore.frameworkLibrary.39782
- __OBJC_$_CLASS_PROP_LIST_HMSymptomsHandler
- __OBJC_$_PROP_LIST_HMApplicationData.11455
- ___30-[HMAccessory _mergeProfiles:]_block_invoke.1105
- ___30-[HMAccessory _mergeProfiles:]_block_invoke.1108
- ___30-[HMAccessory _mergeProfiles:]_block_invoke.1112
- ___30-[HMAccessory _mergeProfiles:]_block_invoke_2.1110
- ___30-[HMAccessory _mergeProfiles:]_block_invoke_2.1113
- ___30-[HMAccessory _mergeProfiles:]_block_invoke_3.1111
- ___30-[HMAccessory _mergeServices:]_block_invoke.926
- ___30-[HMAccessory _mergeServices:]_block_invoke.928
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1081
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1083
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1086
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1093
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1095
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1098
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1100
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1102
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1103
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.930
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.931
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.950
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.953
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.955
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.960
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.964
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1082
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1084
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1089
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1092
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1101
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.932
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.951
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.954
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.956
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.961
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.965
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_3.957
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_3.962
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_3.967
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_4.968
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_5.969
- ___39-[HMAccessory __updateSymptomsHandler:]_block_invoke
- ___40-[HMSymptomsHandler mergeFromNewObject:]_block_invoke
- ___40-[HMSymptomsHandler mergeFromNewObject:]_block_invoke.37
- ___45-[HMAccessory _handleCharacteristicsUpdated:]_block_invoke.1124
- ___48-[HMAccessory _deleteSiriHistoryWithCompletion:]_block_invoke.1125
- ___48-[HMAccessory _deleteSiriHistoryWithCompletion:]_block_invoke.1126
- ___61-[HMAccessory _notifyClientsOfSymptomsHandlerAddedOrRemoved:]_block_invoke
- ___61-[HMAccessory _notifyClientsOfSymptomsHandlerAddedOrRemoved:]_block_invoke.1140
- ___63-[HMAccessory pairingIdentityWithPrivateKey:completionHandler:]_block_invoke.860
- ___63-[HMAccessory pairingIdentityWithPrivateKey:completionHandler:]_block_invoke.862
- ___Block_byref_object_copy_.14413
- ___Block_byref_object_copy_.14726
- ___Block_byref_object_copy_.21405
- ___Block_byref_object_copy_.23476
- ___Block_byref_object_copy_.27603
- ___Block_byref_object_copy_.29351
- ___Block_byref_object_copy_.35860
- ___Block_byref_object_copy_.38707
- ___Block_byref_object_copy_.39768
- ___Block_byref_object_copy_.59879
- ___Block_byref_object_dispose_.14414
- ___Block_byref_object_dispose_.14727
- ___Block_byref_object_dispose_.21406
- ___Block_byref_object_dispose_.23477
- ___Block_byref_object_dispose_.27604
- ___Block_byref_object_dispose_.29352
- ___Block_byref_object_dispose_.35861
- ___Block_byref_object_dispose_.38708
- ___Block_byref_object_dispose_.39769
- ___Block_byref_object_dispose_.59880
- ___CoreAnalyticsLibraryCore_block_invoke.35974
- ___IDSFoundationLibraryCore_block_invoke.39542
- ___UIKitLibraryCore_block_invoke.39783
- ___block_literal_global.101.35981
- ___block_literal_global.10527
- ___block_literal_global.11516
- ___block_literal_global.12.45532
- ___block_literal_global.121.48471
- ___block_literal_global.12485
- ___block_literal_global.12632
- ___block_literal_global.13086
- ___block_literal_global.13279
- ___block_literal_global.13846
- ___block_literal_global.14179
- ___block_literal_global.14497
- ___block_literal_global.15091
- ___block_literal_global.16148
- ___block_literal_global.16679
- ___block_literal_global.16870
- ___block_literal_global.17.17802
- ___block_literal_global.17002
- ___block_literal_global.17164
- ___block_literal_global.175.16178
- ___block_literal_global.17809
- ___block_literal_global.18476
- ___block_literal_global.18881
- ___block_literal_global.19.14164
- ___block_literal_global.192.22699
- ___block_literal_global.19432
- ___block_literal_global.19756
- ___block_literal_global.20788
- ___block_literal_global.21443
- ___block_literal_global.21716
- ___block_literal_global.22201
- ___block_literal_global.22420
- ___block_literal_global.22705
- ___block_literal_global.22840
- ___block_literal_global.23086
- ___block_literal_global.23337
- ___block_literal_global.23500
- ___block_literal_global.23592
- ___block_literal_global.26107
- ___block_literal_global.26242
- ___block_literal_global.26717
- ___block_literal_global.27465
- ___block_literal_global.27761
- ___block_literal_global.28100
- ___block_literal_global.28312
- ___block_literal_global.28590
- ___block_literal_global.28664
- ___block_literal_global.29533
- ___block_literal_global.29889
- ___block_literal_global.30.17792
- ___block_literal_global.30.7709
- ___block_literal_global.30160
- ___block_literal_global.30996
- ___block_literal_global.31364
- ___block_literal_global.32547
- ___block_literal_global.33.59223
- ___block_literal_global.33373
- ___block_literal_global.33604
- ___block_literal_global.33827
- ___block_literal_global.34776
- ___block_literal_global.35968
- ___block_literal_global.36218
- ___block_literal_global.3646
- ___block_literal_global.36554
- ___block_literal_global.37179
- ___block_literal_global.37981
- ___block_literal_global.38106
- ___block_literal_global.38378
- ___block_literal_global.3846
- ___block_literal_global.3937
- ___block_literal_global.39605
- ___block_literal_global.39699
- ___block_literal_global.40408
- ___block_literal_global.40597
- ___block_literal_global.41224
- ___block_literal_global.41850
- ___block_literal_global.42264
- ___block_literal_global.42583
- ___block_literal_global.43258
- ___block_literal_global.44144
- ___block_literal_global.45254
- ___block_literal_global.45544
- ___block_literal_global.45810
- ___block_literal_global.46004
- ___block_literal_global.46233
- ___block_literal_global.46938
- ___block_literal_global.47057
- ___block_literal_global.47788
- ___block_literal_global.48225
- ___block_literal_global.48559
- ___block_literal_global.49472
- ___block_literal_global.5108
- ___block_literal_global.52078
- ___block_literal_global.52781
- ___block_literal_global.54037
- ___block_literal_global.54671
- ___block_literal_global.5504
- ___block_literal_global.55202
- ___block_literal_global.55514
- ___block_literal_global.56011
- ___block_literal_global.56183
- ___block_literal_global.5640
- ___block_literal_global.56571
- ___block_literal_global.56815
- ___block_literal_global.58461
- ___block_literal_global.58627
- ___block_literal_global.58964
- ___block_literal_global.59229
- ___block_literal_global.59589
- ___block_literal_global.59877
- ___block_literal_global.60171
- ___block_literal_global.6158
- ___block_literal_global.6639
- ___block_literal_global.6913
- ___block_literal_global.73.21694
- ___block_literal_global.7374
- ___block_literal_global.7491
- ___block_literal_global.75.36171
- ___block_literal_global.76.25874
- ___block_literal_global.7727
- ___block_literal_global.8183
- ___block_literal_global.84.59891
- ___block_literal_global.8666
- ___block_literal_global.8947
- ___block_literal_global.9124
- ___block_literal_global.9552
- ___block_literal_global.9815
- ___getAnalyticsSendEventLazySymbolLoc_block_invoke.35971
- ___getNSCharacterEncodingDocumentAttributeSymbolLoc_block_invoke.39778
- ___getNSDocumentTypeDocumentAttributeSymbolLoc_block_invoke.39772
- __unnamed_array_storage.14430
- __unnamed_array_storage.22612
- __unnamed_array_storage.227.26021
- __unnamed_array_storage.239.26020
- __unnamed_array_storage.251.26024
- __unnamed_array_storage.26097
- __unnamed_array_storage.29230
- __unnamed_array_storage.54159
- __unnamed_array_storage.55639
- __unnamed_array_storage.59080
- _audit_stringCoreAnalytics.35977
- _audit_stringIDSFoundation.39544
- _audit_stringUIKit.39785
- _getAnalyticsSendEventLazySymbolLoc.ptr.35970
- _getNSCharacterEncodingDocumentAttributeSymbolLoc.ptr.39777
- _getNSDocumentTypeDocumentAttributeSymbolLoc.ptr.39771
- _kSymptomsCodingKey
- _logCategory._hmf_once_t0.12631
- _logCategory._hmf_once_t0.21715
- _logCategory._hmf_once_t0.28311
- _logCategory._hmf_once_t0.28663
- _logCategory._hmf_once_t0.40407
- _logCategory._hmf_once_t0.40596
- _logCategory._hmf_once_t0.41223
- _logCategory._hmf_once_t0.56814
- _logCategory._hmf_once_t1.17001
- _logCategory._hmf_once_t1.18880
- _logCategory._hmf_once_t1.36194
- _logCategory._hmf_once_t1.41849
- _logCategory._hmf_once_t1.45531
- _logCategory._hmf_once_t1.47056
- _logCategory._hmf_once_t1.52077
- _logCategory._hmf_once_t15.56570
- _logCategory._hmf_once_t16.33603
- _logCategory._hmf_once_t16.58626
- _logCategory._hmf_once_t17.37973
- _logCategory._hmf_once_t19.13305
- _logCategory._hmf_once_t2.26241
- _logCategory._hmf_once_t2.29888
- _logCategory._hmf_once_t20.5639
- _logCategory._hmf_once_t22.23085
- _logCategory._hmf_once_t24.36548
- _logCategory._hmf_once_t25.23336
- _logCategory._hmf_once_t25.59588
- _logCategory._hmf_once_t26.48306
- _logCategory._hmf_once_t27.47787
- _logCategory._hmf_once_t27.55513
- _logCategory._hmf_once_t3.38105
- _logCategory._hmf_once_t3.59222
- _logCategory._hmf_once_t31.21442
- _logCategory._hmf_once_t31.58460
- _logCategory._hmf_once_t313
- _logCategory._hmf_once_t33.48584
- _logCategory._hmf_once_t34.14492
- _logCategory._hmf_once_t34.18475
- _logCategory._hmf_once_t35.34775
- _logCategory._hmf_once_t393
- _logCategory._hmf_once_t4.5503
- _logCategory._hmf_once_t50
- _logCategory._hmf_once_t6.30995
- _logCategory._hmf_once_t6.33372
- _logCategory._hmf_once_t6.52780
- _logCategory._hmf_once_t64.54036
- _logCategory._hmf_once_t7.23591
- _logCategory._hmf_once_t7.46937
- _logCategory._hmf_once_t8.33826
- _logCategory._hmf_once_t8.43257
- _logCategory._hmf_once_t8.46022
- _logCategory._hmf_once_v1.12633
- _logCategory._hmf_once_v1.21717
- _logCategory._hmf_once_v1.28313
- _logCategory._hmf_once_v1.28665
- _logCategory._hmf_once_v1.40409
- _logCategory._hmf_once_v1.40598
- _logCategory._hmf_once_v1.41225
- _logCategory._hmf_once_v1.56816
- _logCategory._hmf_once_v16.56572
- _logCategory._hmf_once_v17.33605
- _logCategory._hmf_once_v17.58628
- _logCategory._hmf_once_v18.37974
- _logCategory._hmf_once_v2.17003
- _logCategory._hmf_once_v2.18882
- _logCategory._hmf_once_v2.36195
- _logCategory._hmf_once_v2.41851
- _logCategory._hmf_once_v2.45533
- _logCategory._hmf_once_v2.47058
- _logCategory._hmf_once_v2.52079
- _logCategory._hmf_once_v20.13306
- _logCategory._hmf_once_v21.5641
- _logCategory._hmf_once_v23.23087
- _logCategory._hmf_once_v25.36549
- _logCategory._hmf_once_v26.23338
- _logCategory._hmf_once_v26.59590
- _logCategory._hmf_once_v27.48307
- _logCategory._hmf_once_v28.47789
- _logCategory._hmf_once_v28.55515
- _logCategory._hmf_once_v3.26243
- _logCategory._hmf_once_v3.29890
- _logCategory._hmf_once_v314
- _logCategory._hmf_once_v32.21444
- _logCategory._hmf_once_v32.58462
- _logCategory._hmf_once_v34.48585
- _logCategory._hmf_once_v35.14493
- _logCategory._hmf_once_v35.18477
- _logCategory._hmf_once_v36.34777
- _logCategory._hmf_once_v394
- _logCategory._hmf_once_v4.38107
- _logCategory._hmf_once_v4.59224
- _logCategory._hmf_once_v5.5505
- _logCategory._hmf_once_v51
- _logCategory._hmf_once_v65.54038
- _logCategory._hmf_once_v7.30997
- _logCategory._hmf_once_v7.33374
- _logCategory._hmf_once_v7.52782
- _logCategory._hmf_once_v8.23593
- _logCategory._hmf_once_v8.46939
- _logCategory._hmf_once_v9.33828
- _logCategory._hmf_once_v9.43259
- _logCategory._hmf_once_v9.46023
- _objc_msgSend$__updateSymptomsHandler:
- _objc_msgSend$_notifyClientsOfSymptomsHandlerAddedOrRemoved:
- _objc_msgSend$_registerForMessages
- _objc_msgSend$addControlTargetUUIDs:
- _objc_msgSend$initWithUUID:logIdentifier:
- _objc_msgSend$removeControlTargetUUIDs:
- _objc_msgSend$setDidReceiveAccountInfo:
- _objc_msgSend$unarchive:
- _sharedInstance.onceToken.37980
- _sharedManager.onceToken.55656
- _supportedValueClasses.onceToken.45809
- _supportedValueClasses.onceToken.54001
- _supportedValueClasses.supportedValueClasses.45811
- _supportedValueClasses.supportedValueClasses.54002
- _unconfigureQueue.onceToken.36553
- _unconfigureQueue.unconfigureQueue.36555
CStrings:
+ "\x11\x16"
+ "%{public}@Notifying client of added symptoms handler"
+ "%{public}@Notifying client of removed symptoms handler"
+ "%{public}@Received %@ message so updating SFDevice identifier from %@ to %@"
+ "%{public}@Received %@ message so updating symptoms from %@ to %@"
+ "%{public}@Subscribing to symptoms changes with message: %@"
+ "%{public}@Unsubscribing from symptoms changes with message: %@"
+ "@\"HMSymptomFixSession\"32@?0@\"HMSymptom\"8@\"NSUUID\"16@\"_HMContext\"24"
+ "DA8F18EC-6C7D-4631-9B5B-615977C21A44"
+ "HM.hasSymptomsHandler"
+ "HMS.type"
+ "HMSM.initiateFix"
+ "HMSM.subscribe"
+ "HMSM.symptomStateUpdated"
+ "HMSM.symptoms"
+ "HMSM.unsubscribe"
+ "T@\"HMMutableArray\",R,V_currentSymptoms"
+ "T@\"HMSymptomsHandler\",&,V_symptomsHandler"
+ "T@?,C,V_fixSessionFactory"
+ "TB,V_hasSymptomsHandler"
+ "_createSymptomsHandler"
+ "_fixSessionFactory"
+ "_handleSymptomStateUpdatedMessage:"
+ "_hasSymptomsHandler"
+ "_updateHasSymptomsHandler:"
+ "fixSessionFactory"
+ "hasSymptomsHandler"
+ "initWithUUID:context:logIdentifier:"
+ "setFixSessionFactory:"
+ "setHasSymptomsHandler:"
+ "symptomsHandlerUUIDFromAccessoryUUID:"
- "\x12\x15"
- "%{public}@Cannot initialize from decoded uuid: %@"
- "%{public}@Failed to unarchive symptoms from archive data: %@"
- "%{public}@Failed to unarchive symptoms handler from symptoms handler data: %@"
- "%{public}@Failed to unarchive symtoms from archive data: %@"
- "%{public}@Notifying client of symptoms handler addition"
- "%{public}@Notifying client of symptoms handler removal"
- "%{public}@Received message-%@, updating SFDevice identifier from %@ to %@"
- "%{public}@Received message-%@, updating symptoms from %@ to %@"
- "%{public}@Symptoms handler in new home data is nil"
- "%{public}@Unable to look up target accessory with UUID %@"
- "%{public}@Unconfiguring symptomsHandler"
- "%{public}@Updating SF device identifier for merge from %@ to %@"
- "%{public}@Updating symptoms for merge from %@ to %@"
- "HM.Symptoms"
- "HM.symptomsHandler"
- "HMCT.updated"
- "HMSH.updated"
- "HMSM.fixError"
- "HMSM.sfDeviceIdentifierUpdated"
- "HMSM.symptomsUpdated"
- "T@\"HMMutableArray\",R,N,V_currentSymptoms"
- "T@\"HMSymptomsHandler\",C,V_symptomsHandler"
- "__updateSymptomsHandler:"
- "_handleControlTargetsUpdatedMessage:"
- "_handleSFDeviceIdentifierUpdated:"
- "_handleSymptomsHandlerUpdatedMessage:"
- "_handleSymptomsUpdated:"
- "_notifyClientsOfSymptomsHandlerAddedOrRemoved:"
- "_registerForMessages"
- "addControlTargetUUIDs:"
- "archive:"
- "archiveSymptomDict:"
- "initWithUUID:logIdentifier:"
- "removeControlTargetUUIDs:"
- "resetControlTargetUUIDs"
- "symptom.type"
- "unarchive:"
- "unarchiveSymptomDict:"

```
