## HomeKit

> `/System/Library/Frameworks/HomeKit.framework/HomeKit`

```diff

-1535.0.0.0.2
-  __TEXT.__text: 0x498058
-  __TEXT.__objc_methlist: 0x2a734
-  __TEXT.__const: 0x12cd8
+1535.3.8.0.0
+  __TEXT.__text: 0x4a268c
+  __TEXT.__objc_methlist: 0x2ab1c
+  __TEXT.__const: 0x130c8
   __TEXT.__dlopen_cstrs: 0x44f
-  __TEXT.__swift5_typeref: 0x45fe
-  __TEXT.__cstring: 0x33bc8
-  __TEXT.__constg_swiftt: 0x4010
-  __TEXT.__swift5_reflstr: 0x2de0
-  __TEXT.__swift5_fieldmd: 0x3cec
+  __TEXT.__swift5_typeref: 0x478e
+  __TEXT.__cstring: 0x340ff
+  __TEXT.__constg_swiftt: 0x4124
+  __TEXT.__swift5_reflstr: 0x2e74
+  __TEXT.__swift5_fieldmd: 0x3dc8
   __TEXT.__swift5_builtin: 0xc8
-  __TEXT.__swift5_assocty: 0x9b8
-  __TEXT.__swift5_capture: 0xb08
+  __TEXT.__swift5_assocty: 0x9d8
+  __TEXT.__swift5_capture: 0xb48
   __TEXT.__swift5_protos: 0x4c
-  __TEXT.__swift5_proto: 0xf88
-  __TEXT.__swift5_types: 0x514
-  __TEXT.__swift_as_entry: 0x2e0
-  __TEXT.__swift_as_ret: 0x338
-  __TEXT.__swift_as_cont: 0x6f0
-  __TEXT.__oslogstring: 0x5c5e8
+  __TEXT.__swift5_proto: 0xfd0
+  __TEXT.__swift5_types: 0x530
+  __TEXT.__swift_as_entry: 0x2e8
+  __TEXT.__swift_as_ret: 0x340
+  __TEXT.__swift_as_cont: 0x6fc
+  __TEXT.__oslogstring: 0x5cf3a
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__gcc_except_tab: 0x6a5c
-  __TEXT.__ustring: 0x50
-  __TEXT.__unwind_info: 0x13d18
-  __TEXT.__eh_frame: 0xddd0
+  __TEXT.__gcc_except_tab: 0x6b6c
+  __TEXT.__ustring: 0x54
+  __TEXT.__unwind_info: 0x14528
+  __TEXT.__eh_frame: 0xe254
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x97a0
-  __DATA_CONST.__objc_classlist: 0x1448
+  __DATA_CONST.__const: 0x9870
+  __DATA_CONST.__objc_classlist: 0x1468
   __DATA_CONST.__objc_catlist: 0x108
-  __DATA_CONST.__objc_protolist: 0x570
+  __DATA_CONST.__objc_protolist: 0x578
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xee10
+  __DATA_CONST.__objc_selrefs: 0xefd8
   __DATA_CONST.__objc_protorefs: 0x110
-  __DATA_CONST.__objc_superrefs: 0x1048
+  __DATA_CONST.__objc_superrefs: 0x1058
   __DATA_CONST.__objc_arraydata: 0x14c0
-  __DATA_CONST.__got: 0x2110
-  __AUTH_CONST.__const: 0xbac8
-  __AUTH_CONST.__cfstring: 0x2dcc0
-  __AUTH_CONST.__objc_const: 0x4cda8
+  __DATA_CONST.__got: 0x2118
+  __AUTH_CONST.__const: 0xbe08
+  __AUTH_CONST.__cfstring: 0x2e060
+  __AUTH_CONST.__objc_const: 0x4d4a0
   __AUTH_CONST.__objc_intobj: 0x9f0
   __AUTH_CONST.__objc_dictobj: 0x848
   __AUTH_CONST.__objc_arrayobj: 0x618
   __AUTH_CONST.__objc_doubleobj: 0x70
-  __AUTH_CONST.__auth_got: 0x1fd0
-  __AUTH.__objc_data: 0x9918
-  __AUTH.__data: 0x41e8
-  __DATA.__objc_ivar: 0x2a28
-  __DATA.__data: 0x7bf8
+  __AUTH_CONST.__auth_got: 0x1fd8
+  __AUTH.__objc_data: 0x9a28
+  __AUTH.__data: 0x4380
+  __DATA.__objc_ivar: 0x2a4c
+  __DATA.__data: 0x7da0
   __DATA.__common: 0x1b0
   __DATA_DIRTY.__objc_data: 0x36a0
   __DATA_DIRTY.__data: 0x1b0
-  __DATA_DIRTY.__bss: 0x2b0
+  __DATA_DIRTY.__bss: 0x2a0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/ActivityKit.framework/ActivityKit

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 22686
-  Symbols:   29480
-  CStrings:  13252
+  Functions: 22888
+  Symbols:   29638
+  CStrings:  13321
 
Symbols:
+ +[HMPredicateUtilities validatePredicateShape:options:rejectionReason:]
+ +[HMPredicateUtilities validateStoredPredicate:]
+ +[HMUnrecognizedUserParentalControlSettings(Foundation) supportsSecureCoding]
+ -[HMAccessory defaultGroupNameForMediaDestinationController:]
+ -[HMHome _updateUnrecognizedUserSettingNamed:value:completion:]
+ -[HMHome setUnrecognizedUserSettings:]
+ -[HMHome stagedHomeTheaterRenamesForMediaGroupsController:]
+ -[HMHome unrecognizedUserSettings]
+ -[HMHome updateUnrecognizedUserAllowExplicitContent:completion:]
+ -[HMHome updateUnrecognizedUserBroadWorldKnowledgeAllowed:completion:]
+ -[HMHome updateUnrecognizedUserMathAssistanceAllowed:completion:]
+ -[HMHome updateUnrecognizedUserSafariEnabled:completion:]
+ -[HMHome updateUnrecognizedUserSensitiveTopicsAllowed:completion:]
+ -[HMHome updateUnrecognizedUserWebContentFilter:completion:]
+ -[HMHome updateUnrecognizedUserWritingAssistanceAllowed:completion:]
+ -[HMMediaDestinationController configureLastNotifiedGroupName]
+ -[HMMediaDestinationController lastNotifiedGroupName]
+ -[HMMediaDestinationController locallyStageDestination:]
+ -[HMMediaDestinationController locallyStageGroupName:]
+ -[HMMediaDestinationController setLastNotifiedGroupName:]
+ -[HMMediaGroupStageHomeTheaterRename .cxx_destruct]
+ -[HMMediaGroupStageHomeTheaterRename description]
+ -[HMMediaGroupStageHomeTheaterRename destinationControllerIdentifier]
+ -[HMMediaGroupStageHomeTheaterRename groupName]
+ -[HMMediaGroupStageHomeTheaterRename hash]
+ -[HMMediaGroupStageHomeTheaterRename hmf_appendAttributeDescriptionsToString:options:]
+ -[HMMediaGroupStageHomeTheaterRename initWithDestinationControllerIdentifier:groupName:defaultName:]
+ -[HMMediaGroupStageHomeTheaterRename isDefaultName]
+ -[HMMediaGroupStageHomeTheaterRename isEqual:]
+ -[HMMediaGroupStagingManager extendTimerToTimeInterval:]
+ -[HMMediaGroupStagingManager locallyStageDestination:forDestinationController:]
+ -[HMMediaGroupStagingManager locallyStageGroupName:defaultName:forDestinationControllerIdentifier:]
+ -[HMMediaGroupStagingManager notifyDestinationControllerGroupNameWithIdentifiers:]
+ -[HMMediaGroupStagingManager notifyDestinationControllersWithDestinationControllerIdentifiers:]
+ -[HMMediaGroupStagingManager stagedDestinationControllerDataIdentifiers]
+ -[HMMediaGroupStagingManager stagedGroupNameForDestinationControllerIdentifier:]
+ -[HMMediaGroupStagingManager stagedHomeTheaterRenames]
+ -[HMMediaGroupsController stagedHomeTheaterRenames]
+ -[HMPredicateShapeVisitor .cxx_destruct]
+ -[HMPredicateShapeVisitor initWithOptions:]
+ -[HMPredicateShapeVisitor isAllowedConstant:depth:]
+ -[HMPredicateShapeVisitor isAllowedFunction:operand:argumentCount:]
+ -[HMPredicateShapeVisitor isAllowedKeyPath:]
+ -[HMPredicateShapeVisitor rejectionReasonForPredicate:]
+ -[HMPredicateShapeVisitor visitPredicate:]
+ -[HMPredicateShapeVisitor visitPredicateExpression:]
+ -[HMPredicateShapeVisitor visitPredicateOperator:]
+ -[HMUnrecognizedUserParentalControlSettings(Foundation) copyWithZone:]
+ -[HMUnrecognizedUserParentalControlSettings(Foundation) description]
+ -[HMUnrecognizedUserParentalControlSettings(Foundation) encodeWithCoder:]
+ -[HMUnrecognizedUserParentalControlSettings(Foundation) hash]
+ -[HMUnrecognizedUserParentalControlSettings(Foundation) initWithCoder:]
+ -[HMUnrecognizedUserParentalControlSettings(Foundation) init]
+ -[HMUnrecognizedUserParentalControlSettings(Foundation) isEqual:]
+ GCC_except_table10011
+ GCC_except_table10070
+ GCC_except_table10073
+ GCC_except_table10075
+ GCC_except_table10088
+ GCC_except_table10089
+ GCC_except_table10157
+ GCC_except_table10161
+ GCC_except_table10508
+ GCC_except_table10546
+ GCC_except_table10559
+ GCC_except_table10912
+ GCC_except_table10922
+ GCC_except_table11018
+ GCC_except_table11111
+ GCC_except_table11112
+ GCC_except_table11114
+ GCC_except_table11115
+ GCC_except_table11125
+ GCC_except_table11149
+ GCC_except_table11150
+ GCC_except_table11153
+ GCC_except_table11156
+ GCC_except_table11165
+ GCC_except_table11166
+ GCC_except_table11167
+ GCC_except_table11264
+ GCC_except_table11290
+ GCC_except_table11292
+ GCC_except_table11296
+ GCC_except_table11297
+ GCC_except_table11345
+ GCC_except_table11371
+ GCC_except_table11384
+ GCC_except_table11414
+ GCC_except_table11418
+ GCC_except_table11467
+ GCC_except_table11468
+ GCC_except_table11469
+ GCC_except_table11470
+ GCC_except_table11471
+ GCC_except_table11472
+ GCC_except_table11473
+ GCC_except_table11474
+ GCC_except_table11475
+ GCC_except_table11476
+ GCC_except_table11477
+ GCC_except_table11478
+ GCC_except_table11479
+ GCC_except_table11480
+ GCC_except_table11481
+ GCC_except_table11482
+ GCC_except_table11505
+ GCC_except_table11532
+ GCC_except_table11642
+ GCC_except_table11643
+ GCC_except_table11646
+ GCC_except_table1171
+ GCC_except_table11712
+ GCC_except_table11714
+ GCC_except_table11733
+ GCC_except_table11735
+ GCC_except_table11741
+ GCC_except_table11742
+ GCC_except_table1175
+ GCC_except_table1182
+ GCC_except_table12035
+ GCC_except_table12247
+ GCC_except_table12303
+ GCC_except_table12314
+ GCC_except_table12520
+ GCC_except_table12522
+ GCC_except_table12529
+ GCC_except_table12537
+ GCC_except_table12558
+ GCC_except_table12569
+ GCC_except_table1257
+ GCC_except_table12574
+ GCC_except_table12577
+ GCC_except_table12591
+ GCC_except_table12596
+ GCC_except_table12602
+ GCC_except_table12607
+ GCC_except_table12612
+ GCC_except_table12617
+ GCC_except_table12622
+ GCC_except_table12626
+ GCC_except_table12631
+ GCC_except_table1266
+ GCC_except_table12682
+ GCC_except_table12686
+ GCC_except_table12694
+ GCC_except_table12699
+ GCC_except_table12713
+ GCC_except_table12718
+ GCC_except_table12725
+ GCC_except_table12741
+ GCC_except_table12742
+ GCC_except_table12744
+ GCC_except_table12746
+ GCC_except_table12749
+ GCC_except_table12754
+ GCC_except_table12761
+ GCC_except_table12766
+ GCC_except_table12770
+ GCC_except_table12807
+ GCC_except_table12861
+ GCC_except_table12870
+ GCC_except_table12878
+ GCC_except_table13001
+ GCC_except_table13004
+ GCC_except_table13106
+ GCC_except_table13125
+ GCC_except_table13135
+ GCC_except_table13292
+ GCC_except_table13295
+ GCC_except_table13304
+ GCC_except_table13317
+ GCC_except_table13324
+ GCC_except_table1334
+ GCC_except_table1336
+ GCC_except_table1339
+ GCC_except_table13402
+ GCC_except_table13404
+ GCC_except_table13406
+ GCC_except_table1341
+ GCC_except_table13413
+ GCC_except_table13421
+ GCC_except_table1343
+ GCC_except_table13431
+ GCC_except_table13443
+ GCC_except_table13449
+ GCC_except_table13452
+ GCC_except_table1347
+ GCC_except_table13545
+ GCC_except_table13554
+ GCC_except_table13556
+ GCC_except_table13566
+ GCC_except_table13568
+ GCC_except_table13570
+ GCC_except_table13572
+ GCC_except_table13574
+ GCC_except_table13580
+ GCC_except_table13584
+ GCC_except_table13597
+ GCC_except_table13599
+ GCC_except_table13601
+ GCC_except_table13603
+ GCC_except_table13631
+ GCC_except_table13661
+ GCC_except_table13746
+ GCC_except_table13947
+ GCC_except_table13950
+ GCC_except_table13955
+ GCC_except_table13959
+ GCC_except_table13970
+ GCC_except_table13972
+ GCC_except_table13977
+ GCC_except_table13978
+ GCC_except_table13980
+ GCC_except_table14062
+ GCC_except_table14064
+ GCC_except_table14083
+ GCC_except_table14084
+ GCC_except_table14085
+ GCC_except_table14086
+ GCC_except_table14091
+ GCC_except_table14105
+ GCC_except_table14111
+ GCC_except_table14114
+ GCC_except_table14116
+ GCC_except_table14162
+ GCC_except_table14194
+ GCC_except_table14204
+ GCC_except_table14205
+ GCC_except_table14210
+ GCC_except_table14216
+ GCC_except_table14220
+ GCC_except_table14222
+ GCC_except_table14224
+ GCC_except_table14228
+ GCC_except_table14361
+ GCC_except_table14417
+ GCC_except_table14418
+ GCC_except_table14420
+ GCC_except_table14430
+ GCC_except_table14431
+ GCC_except_table14455
+ GCC_except_table14532
+ GCC_except_table14554
+ GCC_except_table14557
+ GCC_except_table14705
+ GCC_except_table14902
+ GCC_except_table14908
+ GCC_except_table14911
+ GCC_except_table14976
+ GCC_except_table15011
+ GCC_except_table15017
+ GCC_except_table15022
+ GCC_except_table15023
+ GCC_except_table15025
+ GCC_except_table15026
+ GCC_except_table15029
+ GCC_except_table15030
+ GCC_except_table15031
+ GCC_except_table15032
+ GCC_except_table15033
+ GCC_except_table15034
+ GCC_except_table15035
+ GCC_except_table15036
+ GCC_except_table15037
+ GCC_except_table15038
+ GCC_except_table15039
+ GCC_except_table15040
+ GCC_except_table15041
+ GCC_except_table15042
+ GCC_except_table15043
+ GCC_except_table15053
+ GCC_except_table15060
+ GCC_except_table15064
+ GCC_except_table15067
+ GCC_except_table15219
+ GCC_except_table15222
+ GCC_except_table15243
+ GCC_except_table15245
+ GCC_except_table15246
+ GCC_except_table1538
+ GCC_except_table1564
+ GCC_except_table1632
+ GCC_except_table1707
+ GCC_except_table1710
+ GCC_except_table1728
+ GCC_except_table1796
+ GCC_except_table1798
+ GCC_except_table1809
+ GCC_except_table1811
+ GCC_except_table1952
+ GCC_except_table2011
+ GCC_except_table2014
+ GCC_except_table2088
+ GCC_except_table2175
+ GCC_except_table2176
+ GCC_except_table2225
+ GCC_except_table2528
+ GCC_except_table2531
+ GCC_except_table2534
+ GCC_except_table2539
+ GCC_except_table2543
+ GCC_except_table2552
+ GCC_except_table2565
+ GCC_except_table2567
+ GCC_except_table2568
+ GCC_except_table2573
+ GCC_except_table2574
+ GCC_except_table2575
+ GCC_except_table2576
+ GCC_except_table3169
+ GCC_except_table3174
+ GCC_except_table3199
+ GCC_except_table3201
+ GCC_except_table3235
+ GCC_except_table3238
+ GCC_except_table3251
+ GCC_except_table3288
+ GCC_except_table3333
+ GCC_except_table3336
+ GCC_except_table3362
+ GCC_except_table3364
+ GCC_except_table3366
+ GCC_except_table3368
+ GCC_except_table3515
+ GCC_except_table3518
+ GCC_except_table3526
+ GCC_except_table3527
+ GCC_except_table3555
+ GCC_except_table3582
+ GCC_except_table3583
+ GCC_except_table3630
+ GCC_except_table3632
+ GCC_except_table3657
+ GCC_except_table3659
+ GCC_except_table3662
+ GCC_except_table3663
+ GCC_except_table3687
+ GCC_except_table3689
+ GCC_except_table3697
+ GCC_except_table3699
+ GCC_except_table3706
+ GCC_except_table3707
+ GCC_except_table3708
+ GCC_except_table3710
+ GCC_except_table3711
+ GCC_except_table3712
+ GCC_except_table3713
+ GCC_except_table3714
+ GCC_except_table3797
+ GCC_except_table3820
+ GCC_except_table3823
+ GCC_except_table3826
+ GCC_except_table3829
+ GCC_except_table3832
+ GCC_except_table3835
+ GCC_except_table3838
+ GCC_except_table3903
+ GCC_except_table3904
+ GCC_except_table3950
+ GCC_except_table3957
+ GCC_except_table3958
+ GCC_except_table3959
+ GCC_except_table3962
+ GCC_except_table3964
+ GCC_except_table3966
+ GCC_except_table3974
+ GCC_except_table3996
+ GCC_except_table4003
+ GCC_except_table4007
+ GCC_except_table4010
+ GCC_except_table4013
+ GCC_except_table4055
+ GCC_except_table4059
+ GCC_except_table4063
+ GCC_except_table4068
+ GCC_except_table4076
+ GCC_except_table4089
+ GCC_except_table4091
+ GCC_except_table4335
+ GCC_except_table4339
+ GCC_except_table4343
+ GCC_except_table4350
+ GCC_except_table4351
+ GCC_except_table4354
+ GCC_except_table4360
+ GCC_except_table4364
+ GCC_except_table4368
+ GCC_except_table4397
+ GCC_except_table4399
+ GCC_except_table4401
+ GCC_except_table4404
+ GCC_except_table4405
+ GCC_except_table4407
+ GCC_except_table4410
+ GCC_except_table4485
+ GCC_except_table4499
+ GCC_except_table4502
+ GCC_except_table4504
+ GCC_except_table4507
+ GCC_except_table4514
+ GCC_except_table4569
+ GCC_except_table4636
+ GCC_except_table4651
+ GCC_except_table4654
+ GCC_except_table4746
+ GCC_except_table4747
+ GCC_except_table4749
+ GCC_except_table4754
+ GCC_except_table4758
+ GCC_except_table4761
+ GCC_except_table4763
+ GCC_except_table5038
+ GCC_except_table5041
+ GCC_except_table5053
+ GCC_except_table5129
+ GCC_except_table5175
+ GCC_except_table5465
+ GCC_except_table5477
+ GCC_except_table5479
+ GCC_except_table5504
+ GCC_except_table5505
+ GCC_except_table5506
+ GCC_except_table5507
+ GCC_except_table5562
+ GCC_except_table5572
+ GCC_except_table5734
+ GCC_except_table5735
+ GCC_except_table5847
+ GCC_except_table5849
+ GCC_except_table5864
+ GCC_except_table5989
+ GCC_except_table5991
+ GCC_except_table6009
+ GCC_except_table6055
+ GCC_except_table6150
+ GCC_except_table6170
+ GCC_except_table6171
+ GCC_except_table6172
+ GCC_except_table6174
+ GCC_except_table6177
+ GCC_except_table6178
+ GCC_except_table6180
+ GCC_except_table6538
+ GCC_except_table6544
+ GCC_except_table6546
+ GCC_except_table6556
+ GCC_except_table6557
+ GCC_except_table6764
+ GCC_except_table6768
+ GCC_except_table6851
+ GCC_except_table6876
+ GCC_except_table6880
+ GCC_except_table6882
+ GCC_except_table6883
+ GCC_except_table7050
+ GCC_except_table7057
+ GCC_except_table7178
+ GCC_except_table7233
+ GCC_except_table7235
+ GCC_except_table7237
+ GCC_except_table7259
+ GCC_except_table7289
+ GCC_except_table7301
+ GCC_except_table7327
+ GCC_except_table7333
+ GCC_except_table7344
+ GCC_except_table7346
+ GCC_except_table7348
+ GCC_except_table7350
+ GCC_except_table7352
+ GCC_except_table7354
+ GCC_except_table7356
+ GCC_except_table7358
+ GCC_except_table7360
+ GCC_except_table7362
+ GCC_except_table7364
+ GCC_except_table7366
+ GCC_except_table7368
+ GCC_except_table7373
+ GCC_except_table7387
+ GCC_except_table7388
+ GCC_except_table7411
+ GCC_except_table7413
+ GCC_except_table7438
+ GCC_except_table744
+ GCC_except_table7451
+ GCC_except_table7469
+ GCC_except_table747
+ GCC_except_table752
+ GCC_except_table755
+ GCC_except_table756
+ GCC_except_table7700
+ GCC_except_table7702
+ GCC_except_table7704
+ GCC_except_table778
+ GCC_except_table795
+ GCC_except_table8040
+ GCC_except_table8083
+ GCC_except_table814
+ GCC_except_table8176
+ GCC_except_table8185
+ GCC_except_table8360
+ GCC_except_table8362
+ GCC_except_table8363
+ GCC_except_table8364
+ GCC_except_table8366
+ GCC_except_table8368
+ GCC_except_table8369
+ GCC_except_table8370
+ GCC_except_table8405
+ GCC_except_table8408
+ GCC_except_table8409
+ GCC_except_table8412
+ GCC_except_table8415
+ GCC_except_table8459
+ GCC_except_table8460
+ GCC_except_table8461
+ GCC_except_table8468
+ GCC_except_table8469
+ GCC_except_table8471
+ GCC_except_table8490
+ GCC_except_table8559
+ GCC_except_table8560
+ GCC_except_table8561
+ GCC_except_table8594
+ GCC_except_table8603
+ GCC_except_table8617
+ GCC_except_table8688
+ GCC_except_table8718
+ GCC_except_table8719
+ GCC_except_table8720
+ GCC_except_table8722
+ GCC_except_table8725
+ GCC_except_table8726
+ GCC_except_table8734
+ GCC_except_table878
+ GCC_except_table881
+ GCC_except_table882
+ GCC_except_table8886
+ GCC_except_table8887
+ GCC_except_table8888
+ GCC_except_table8892
+ GCC_except_table8947
+ GCC_except_table8968
+ GCC_except_table9050
+ GCC_except_table9052
+ GCC_except_table9054
+ GCC_except_table9056
+ GCC_except_table9064
+ GCC_except_table9114
+ GCC_except_table9126
+ GCC_except_table9128
+ GCC_except_table9144
+ GCC_except_table9173
+ GCC_except_table9362
+ GCC_except_table9363
+ GCC_except_table9398
+ GCC_except_table9431
+ GCC_except_table9434
+ GCC_except_table9437
+ GCC_except_table9439
+ GCC_except_table948
+ GCC_except_table9505
+ GCC_except_table9525
+ GCC_except_table9526
+ GCC_except_table9527
+ GCC_except_table953
+ GCC_except_table954
+ GCC_except_table955
+ GCC_except_table956
+ GCC_except_table9566
+ GCC_except_table9568
+ GCC_except_table957
+ GCC_except_table9570
+ GCC_except_table958
+ GCC_except_table960
+ GCC_except_table962
+ GCC_except_table9635
+ GCC_except_table9667
+ GCC_except_table9669
+ GCC_except_table9673
+ GCC_except_table969
+ GCC_except_table9690
+ GCC_except_table9692
+ GCC_except_table9698
+ GCC_except_table970
+ GCC_except_table9702
+ GCC_except_table9705
+ GCC_except_table9712
+ GCC_except_table9716
+ GCC_except_table9722
+ GCC_except_table9734
+ GCC_except_table9737
+ GCC_except_table9745
+ GCC_except_table9746
+ GCC_except_table9748
+ GCC_except_table9750
+ GCC_except_table9752
+ GCC_except_table9772
+ GCC_except_table9782
+ GCC_except_table9998
+ _HMHomeSetUnrecognizedUserSettingRequestKey
+ _HMHomeUnrecognizedUserAllowExplicitContentSettingName
+ _HMHomeUnrecognizedUserBroadWorldKnowledgeAllowedSettingName
+ _HMHomeUnrecognizedUserMathAssistanceAllowedSettingName
+ _HMHomeUnrecognizedUserSafariEnabledSettingName
+ _HMHomeUnrecognizedUserSensitiveTopicsAllowedSettingName
+ _HMHomeUnrecognizedUserSettingNameKey
+ _HMHomeUnrecognizedUserSettingValueKey
+ _HMHomeUnrecognizedUserSettingsCodingKey
+ _HMHomeUnrecognizedUserWebContentFilterSettingName
+ _HMHomeUnrecognizedUserWritingAssistanceAllowedSettingName
+ _HMPredicateContainsClientFormConstants
+ _HMPredicateLeafCount
+ _HMPredicateNestingExceedsCap
+ _OBJC_CLASS_$_HMMediaGroupStageHomeTheaterRename
+ _OBJC_CLASS_$_HMPredicateShapeVisitor
+ _OBJC_CLASS_$_HMUnrecognizedUserParentalControlSettings
+ _OBJC_IVAR_$_HMHome._unrecognizedUserSettings
+ _OBJC_IVAR_$_HMMediaDestinationController._lastNotifiedGroupName
+ _OBJC_IVAR_$_HMMediaGroupStageHomeTheaterRename._defaultName
+ _OBJC_IVAR_$_HMMediaGroupStageHomeTheaterRename._destinationControllerIdentifier
+ _OBJC_IVAR_$_HMMediaGroupStageHomeTheaterRename._groupName
+ _OBJC_IVAR_$_HMMediaGroupStagingManager._stagedHomeTheaterRenamesByIdentifier
+ _OBJC_IVAR_$_HMMediaGroupStagingManager._timerDeadline
+ _OBJC_IVAR_$_HMPredicateShapeVisitor._options
+ _OBJC_IVAR_$_HMPredicateShapeVisitor._rejectionReason
+ _OBJC_METACLASS_$_HMMediaGroupStageHomeTheaterRename
+ _OBJC_METACLASS_$_HMPredicateShapeVisitor
+ _OBJC_METACLASS_$_HMUnrecognizedUserParentalControlSettings
+ __DATA_HMUnrecognizedUserParentalControlSettings
+ __DATA__TtCE7HomeKitCSo41HMUnrecognizedUserParentalControlSettingsP33_364673852D08779EE22D469B707141C67Storage
+ __IVARS_HMUnrecognizedUserParentalControlSettings
+ __IVARS__TtCE7HomeKitCSo41HMUnrecognizedUserParentalControlSettingsP33_364673852D08779EE22D469B707141C67Storage
+ __METACLASS_DATA_HMUnrecognizedUserParentalControlSettings
+ __METACLASS_DATA__TtCE7HomeKitCSo41HMUnrecognizedUserParentalControlSettingsP33_364673852D08779EE22D469B707141C67Storage
+ __OBJC_$_CLASS_METHODS_HMAccessory(HomeKit|DynamicAccessorySettingsAdapter|Identifier|SwiftExtensions|HomeKit1|SiriEndpoint|Television|ErrorStatus|LightInternal|HMDoorbellChimeProfile|NetworkRouter|Shortcuts|Camera|CameraInternal|CHIP|NetworkConfiguration|Climate|PendingConfiguration|Private|CUPeerIdentifier|Diagnostics|ThreadManagement|Light|Media)
+ __OBJC_$_CLASS_METHODS_HMUnrecognizedUserParentalControlSettings(Foundation)
+ __OBJC_$_INSTANCE_METHODS_HMAccessory(HomeKit|DynamicAccessorySettingsAdapter|Identifier|SwiftExtensions|HomeKit1|SiriEndpoint|Television|ErrorStatus|LightInternal|HMDoorbellChimeProfile|NetworkRouter|Shortcuts|Camera|CameraInternal|CHIP|NetworkConfiguration|Climate|PendingConfiguration|Private|CUPeerIdentifier|Diagnostics|ThreadManagement|Light|Media)
+ __OBJC_$_INSTANCE_METHODS_HMClientConnection(HomeKit)
+ __OBJC_$_INSTANCE_METHODS_HMMediaGroupStageHomeTheaterRename
+ __OBJC_$_INSTANCE_METHODS_HMPredicateShapeVisitor
+ __OBJC_$_INSTANCE_METHODS_HMUnrecognizedUserParentalControlSettings(Foundation)
+ __OBJC_$_INSTANCE_VARIABLES_HMMediaGroupStageHomeTheaterRename
+ __OBJC_$_INSTANCE_VARIABLES_HMPredicateShapeVisitor
+ __OBJC_$_PROP_LIST_HMMediaGroupStageHomeTheaterRename
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSPredicateVisitor
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSPredicateVisitor
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSPredicateVisitor
+ __OBJC_CLASS_PROTOCOLS_$_HMPredicateShapeVisitor
+ __OBJC_CLASS_PROTOCOLS_$_HMUnrecognizedUserParentalControlSettings(Foundation)
+ __OBJC_CLASS_RO_$_HMMediaGroupStageHomeTheaterRename
+ __OBJC_CLASS_RO_$_HMPredicateShapeVisitor
+ __OBJC_LABEL_PROTOCOL_$_NSPredicateVisitor
+ __OBJC_METACLASS_RO_$_HMMediaGroupStageHomeTheaterRename
+ __OBJC_METACLASS_RO_$_HMPredicateShapeVisitor
+ __OBJC_PROTOCOL_$_NSPredicateVisitor
+ __PROPERTIES_HMUnrecognizedUserParentalControlSettings
+ ___41-[HMMediaGroupsController deriveGroupMap]_block_invoke_4
+ ___61-[HMUnrecognizedUserParentalControlSettings(Foundation) hash]_block_invoke
+ ___63-[HMHome _updateUnrecognizedUserSettingNamed:value:completion:]_block_invoke
+ ___82-[HMMediaGroupStagingManager notifyDestinationControllerGroupNameWithIdentifiers:]_block_invoke
+ ___95-[HMMediaGroupStagingManager notifyDestinationControllersWithDestinationControllerIdentifiers:]_block_invoke
+ ___block_descriptor_40_e8_32r_e35_v32?0"NSString"8"NSNumber"16^B24lr32l8
+ ___block_descriptor_40_e8_32s_e44_v16?0"HMMediaGroupStageHomeTheaterRename"8ls32l8
+ ___block_descriptor_48_e8_32s40s_e16_v16?0"NSUUID"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s64l8s48l8s56l8
+ ___swift_closure_destructor.109Tm
+ ___swift_closure_destructor.34Tm
+ _associated conformance So18HMClientConnectionC7HomeKitE31GetSceneUnsecuringStatesRequestV15ResponsePayloadV10CodingKeys33_D8E2A7EA01489BED7C91F0A5B4305D9BLLOSHACSQ
+ _associated conformance So18HMClientConnectionC7HomeKitE31GetSceneUnsecuringStatesRequestV15ResponsePayloadV10CodingKeys33_D8E2A7EA01489BED7C91F0A5B4305D9BLLOs0L3KeyACs23CustomStringConvertible
+ _associated conformance So18HMClientConnectionC7HomeKitE31GetSceneUnsecuringStatesRequestV15ResponsePayloadV10CodingKeys33_D8E2A7EA01489BED7C91F0A5B4305D9BLLOs0L3KeyACs28CustomDebugStringConvertible
+ _associated conformance So18HMClientConnectionC7HomeKitE31GetSceneUnsecuringStatesRequestV15ResponsePayloadV4ItemV10CodingKeys33_D8E2A7EA01489BED7C91F0A5B4305D9BLLOSHACSQ
+ _associated conformance So18HMClientConnectionC7HomeKitE31GetSceneUnsecuringStatesRequestV15ResponsePayloadV4ItemV10CodingKeys33_D8E2A7EA01489BED7C91F0A5B4305D9BLLOs0M3KeyACs23CustomStringConvertible
+ _associated conformance So18HMClientConnectionC7HomeKitE31GetSceneUnsecuringStatesRequestV15ResponsePayloadV4ItemV10CodingKeys33_D8E2A7EA01489BED7C91F0A5B4305D9BLLOs0M3KeyACs28CustomDebugStringConvertible
+ _associated conformance So18HMClientConnectionC7HomeKitE31GetSceneUnsecuringStatesRequestVAC19HMFMessagePrototypeO0I7MessageAC0I7PayloadAgHP_AG0M0
+ _associated conformance So18HMClientConnectionC7HomeKitE31GetSceneUnsecuringStatesRequestVAC19HMFMessagePrototypeO0I7MessageAC15ResponsePayloadAgHP_AG0N0
+ _logCategory._hmf_once_t100
+ _logCategory._hmf_once_t17
+ _logCategory._hmf_once_t569
+ _logCategory._hmf_once_t785
+ _logCategory._hmf_once_t85
+ _logCategory._hmf_once_t870
+ _logCategory._hmf_once_v101
+ _logCategory._hmf_once_v18
+ _logCategory._hmf_once_v570
+ _logCategory._hmf_once_v786
+ _logCategory._hmf_once_v86
+ _logCategory._hmf_once_v871
+ _symbolic SDySSSo8NSNumberCG
+ _symbolic SS_So8NSNumberCt
+ _symbolic Say_____G So18HMClientConnectionC7HomeKitE31GetSceneUnsecuringStatesRequestV15ResponsePayloadV4ItemV
+ _symbolic So12NSDictionaryCSgSo7NSErrorCSgIeyByy_
+ _symbolic So41HMUnrecognizedUserParentalControlSettingsC
+ _symbolic So7NSArrayC
+ _symbolic _____ So18HMClientConnectionC7HomeKitE31GetSceneUnsecuringStatesRequestV
+ _symbolic _____ So18HMClientConnectionC7HomeKitE31GetSceneUnsecuringStatesRequestV0I7PayloadV
+ _symbolic _____ So18HMClientConnectionC7HomeKitE31GetSceneUnsecuringStatesRequestV15ResponsePayloadV
+ _symbolic _____ So18HMClientConnectionC7HomeKitE31GetSceneUnsecuringStatesRequestV15ResponsePayloadV10CodingKeys33_D8E2A7EA01489BED7C91F0A5B4305D9BLLO
+ _symbolic _____ So18HMClientConnectionC7HomeKitE31GetSceneUnsecuringStatesRequestV15ResponsePayloadV4ItemV
+ _symbolic _____ So18HMClientConnectionC7HomeKitE31GetSceneUnsecuringStatesRequestV15ResponsePayloadV4ItemV10CodingKeys33_D8E2A7EA01489BED7C91F0A5B4305D9BLLO
+ _symbolic _____ So41HMUnrecognizedUserParentalControlSettingsC7HomeKitE7Storage33_364673852D08779EE22D469B707141C6LLC
+ _symbolic ______Sbt 10Foundation4UUIDV
+ _symbolic _____ySSSo8NSNumberCG s18_DictionaryStorageC
+ _symbolic _____ySS_So8NSNumberCtG s23_ContiguousArrayStorageC
+ _symbolic _____y_____G s22KeyedDecodingContainerV So18HMClientConnectionC7HomeKitE31GetSceneUnsecuringStatesRequestV15ResponsePayloadV10CodingKeys33_D8E2A7EA01489BED7C91F0A5B4305D9BLLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV So18HMClientConnectionC7HomeKitE31GetSceneUnsecuringStatesRequestV15ResponsePayloadV4ItemV10CodingKeys33_D8E2A7EA01489BED7C91F0A5B4305D9BLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV So18HMClientConnectionC7HomeKitE31GetSceneUnsecuringStatesRequestV15ResponsePayloadV10CodingKeys33_D8E2A7EA01489BED7C91F0A5B4305D9BLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV So18HMClientConnectionC7HomeKitE31GetSceneUnsecuringStatesRequestV15ResponsePayloadV4ItemV10CodingKeys33_D8E2A7EA01489BED7C91F0A5B4305D9BLLO
+ _symbolic _____y_____SbG s18_DictionaryStorageC 10Foundation4UUIDV
+ _symbolic _____y______SbtG s23_ContiguousArrayStorageC 10Foundation4UUIDV
+ _type_layout_string So18HMClientConnectionC7HomeKitE31GetSceneUnsecuringStatesRequestV0I7PayloadV
- GCC_except_table10091
- GCC_except_table10092
- GCC_except_table1010
- GCC_except_table10127
- GCC_except_table1013
- GCC_except_table10163
- GCC_except_table10166
- GCC_except_table10168
- GCC_except_table1022
- GCC_except_table10234
- GCC_except_table10254
- GCC_except_table10255
- GCC_except_table10256
- GCC_except_table10295
- GCC_except_table10297
- GCC_except_table10299
- GCC_except_table1035
- GCC_except_table10364
- GCC_except_table10396
- GCC_except_table10398
- GCC_except_table10402
- GCC_except_table10419
- GCC_except_table1042
- GCC_except_table10421
- GCC_except_table10427
- GCC_except_table10431
- GCC_except_table10434
- GCC_except_table10441
- GCC_except_table10445
- GCC_except_table10451
- GCC_except_table10463
- GCC_except_table10466
- GCC_except_table10474
- GCC_except_table10475
- GCC_except_table10477
- GCC_except_table10479
- GCC_except_table10481
- GCC_except_table10501
- GCC_except_table10511
- GCC_except_table10727
- GCC_except_table10740
- GCC_except_table10799
- GCC_except_table10802
- GCC_except_table10804
- GCC_except_table1081
- GCC_except_table10817
- GCC_except_table10818
- GCC_except_table1083
- GCC_except_table10886
- GCC_except_table10889
- GCC_except_table10890
- GCC_except_table1118
- GCC_except_table1120
- GCC_except_table1122
- GCC_except_table11237
- GCC_except_table1124
- GCC_except_table11275
- GCC_except_table11288
- GCC_except_table1131
- GCC_except_table1139
- GCC_except_table1149
- GCC_except_table1161
- GCC_except_table1167
- GCC_except_table11684
- GCC_except_table11685
- GCC_except_table11687
- GCC_except_table11688
- GCC_except_table11698
- GCC_except_table1170
- GCC_except_table11723
- GCC_except_table11726
- GCC_except_table11729
- GCC_except_table11738
- GCC_except_table11739
- GCC_except_table11837
- GCC_except_table11863
- GCC_except_table11865
- GCC_except_table11869
- GCC_except_table11870
- GCC_except_table11918
- GCC_except_table11944
- GCC_except_table11957
- GCC_except_table11983
- GCC_except_table11987
- GCC_except_table12036
- GCC_except_table12037
- GCC_except_table12038
- GCC_except_table12039
- GCC_except_table12040
- GCC_except_table12041
- GCC_except_table12043
- GCC_except_table12044
- GCC_except_table12045
- GCC_except_table12046
- GCC_except_table12048
- GCC_except_table12049
- GCC_except_table12050
- GCC_except_table12051
- GCC_except_table12074
- GCC_except_table12101
- GCC_except_table12211
- GCC_except_table12212
- GCC_except_table12215
- GCC_except_table12281
- GCC_except_table12283
- GCC_except_table12291
- GCC_except_table12304
- GCC_except_table12309
- GCC_except_table12310
- GCC_except_table12311
- GCC_except_table12535
- GCC_except_table1263
- GCC_except_table12653
- GCC_except_table12663
- GCC_except_table1272
- GCC_except_table1274
- GCC_except_table12759
- GCC_except_table1284
- GCC_except_table1286
- GCC_except_table1288
- GCC_except_table12892
- GCC_except_table12895
- GCC_except_table1290
- GCC_except_table12900
- GCC_except_table12904
- GCC_except_table12910
- GCC_except_table12915
- GCC_except_table12917
- GCC_except_table1292
- GCC_except_table12922
- GCC_except_table12923
- GCC_except_table12925
- GCC_except_table1298
- GCC_except_table13007
- GCC_except_table13009
- GCC_except_table1302
- GCC_except_table13028
- GCC_except_table13029
- GCC_except_table13030
- GCC_except_table13031
- GCC_except_table13036
- GCC_except_table13050
- GCC_except_table13056
- GCC_except_table13059
- GCC_except_table13061
- GCC_except_table13107
- GCC_except_table13139
- GCC_except_table13149
- GCC_except_table1315
- GCC_except_table13150
- GCC_except_table13155
- GCC_except_table13161
- GCC_except_table13163
- GCC_except_table13165
- GCC_except_table13167
- GCC_except_table13169
- GCC_except_table1317
- GCC_except_table13171
- GCC_except_table13173
- GCC_except_table1319
- GCC_except_table1321
- GCC_except_table13306
- GCC_except_table13362
- GCC_except_table13364
- GCC_except_table13375
- GCC_except_table13376
- GCC_except_table13401
- GCC_except_table13477
- GCC_except_table1349
- GCC_except_table13499
- GCC_except_table13502
- GCC_except_table13520
- GCC_except_table13522
- GCC_except_table13524
- GCC_except_table13697
- GCC_except_table13704
- GCC_except_table13709
- GCC_except_table1379
- GCC_except_table13909
- GCC_except_table14169
- GCC_except_table14171
- GCC_except_table14178
- GCC_except_table14186
- GCC_except_table14207
- GCC_except_table14223
- GCC_except_table14240
- GCC_except_table14245
- GCC_except_table14251
- GCC_except_table14256
- GCC_except_table14261
- GCC_except_table14266
- GCC_except_table14271
- GCC_except_table14275
- GCC_except_table14280
- GCC_except_table14331
- GCC_except_table14335
- GCC_except_table14343
- GCC_except_table14348
- GCC_except_table14362
- GCC_except_table14367
- GCC_except_table14374
- GCC_except_table14390
- GCC_except_table14391
- GCC_except_table14393
- GCC_except_table14395
- GCC_except_table14398
- GCC_except_table14403
- GCC_except_table14410
- GCC_except_table14415
- GCC_except_table14510
- GCC_except_table14519
- GCC_except_table14660
- GCC_except_table14857
- GCC_except_table14863
- GCC_except_table14866
- GCC_except_table14931
- GCC_except_table14966
- GCC_except_table14972
- GCC_except_table14977
- GCC_except_table14978
- GCC_except_table14983
- GCC_except_table14985
- GCC_except_table14986
- GCC_except_table14987
- GCC_except_table14988
- GCC_except_table14989
- GCC_except_table14990
- GCC_except_table14991
- GCC_except_table14992
- GCC_except_table14999
- GCC_except_table15006
- GCC_except_table15010
- GCC_except_table15013
- GCC_except_table15156
- GCC_except_table15159
- GCC_except_table15180
- GCC_except_table15182
- GCC_except_table15183
- GCC_except_table1540
- GCC_except_table1543
- GCC_except_table1548
- GCC_except_table1551
- GCC_except_table1552
- GCC_except_table1574
- GCC_except_table1591
- GCC_except_table1610
- GCC_except_table1660
- GCC_except_table1663
- GCC_except_table1664
- GCC_except_table1730
- GCC_except_table1735
- GCC_except_table1736
- GCC_except_table1737
- GCC_except_table1738
- GCC_except_table1739
- GCC_except_table1740
- GCC_except_table1742
- GCC_except_table1744
- GCC_except_table1751
- GCC_except_table1752
- GCC_except_table1953
- GCC_except_table1957
- GCC_except_table1964
- GCC_except_table2039
- GCC_except_table2048
- GCC_except_table2116
- GCC_except_table2118
- GCC_except_table2121
- GCC_except_table2123
- GCC_except_table2125
- GCC_except_table2129
- GCC_except_table2320
- GCC_except_table2346
- GCC_except_table2414
- GCC_except_table2489
- GCC_except_table2492
- GCC_except_table2510
- GCC_except_table2578
- GCC_except_table2580
- GCC_except_table2591
- GCC_except_table2593
- GCC_except_table2732
- GCC_except_table2788
- GCC_except_table2791
- GCC_except_table2865
- GCC_except_table2952
- GCC_except_table2953
- GCC_except_table3002
- GCC_except_table3292
- GCC_except_table3295
- GCC_except_table3298
- GCC_except_table3303
- GCC_except_table3307
- GCC_except_table3329
- GCC_except_table3331
- GCC_except_table3332
- GCC_except_table3337
- GCC_except_table3338
- GCC_except_table3339
- GCC_except_table3340
- GCC_except_table3933
- GCC_except_table3938
- GCC_except_table3965
- GCC_except_table3999
- GCC_except_table4002
- GCC_except_table4015
- GCC_except_table4052
- GCC_except_table4097
- GCC_except_table4100
- GCC_except_table4126
- GCC_except_table4128
- GCC_except_table4130
- GCC_except_table4132
- GCC_except_table4279
- GCC_except_table4282
- GCC_except_table4290
- GCC_except_table4291
- GCC_except_table4319
- GCC_except_table4347
- GCC_except_table4394
- GCC_except_table4396
- GCC_except_table4421
- GCC_except_table4423
- GCC_except_table4426
- GCC_except_table4427
- GCC_except_table4451
- GCC_except_table4453
- GCC_except_table4461
- GCC_except_table4463
- GCC_except_table4470
- GCC_except_table4471
- GCC_except_table4472
- GCC_except_table4474
- GCC_except_table4475
- GCC_except_table4476
- GCC_except_table4477
- GCC_except_table4478
- GCC_except_table4561
- GCC_except_table4584
- GCC_except_table4587
- GCC_except_table4590
- GCC_except_table4593
- GCC_except_table4596
- GCC_except_table4599
- GCC_except_table4602
- GCC_except_table4667
- GCC_except_table4668
- GCC_except_table4714
- GCC_except_table4721
- GCC_except_table4722
- GCC_except_table4723
- GCC_except_table4726
- GCC_except_table4727
- GCC_except_table4728
- GCC_except_table4730
- GCC_except_table4738
- GCC_except_table4760
- GCC_except_table4767
- GCC_except_table4774
- GCC_except_table4777
- GCC_except_table4819
- GCC_except_table4823
- GCC_except_table4827
- GCC_except_table4832
- GCC_except_table4840
- GCC_except_table4844
- GCC_except_table4853
- GCC_except_table4855
- GCC_except_table5099
- GCC_except_table5103
- GCC_except_table5107
- GCC_except_table5110
- GCC_except_table5114
- GCC_except_table5115
- GCC_except_table5118
- GCC_except_table5124
- GCC_except_table5128
- GCC_except_table5132
- GCC_except_table5161
- GCC_except_table5163
- GCC_except_table5165
- GCC_except_table5168
- GCC_except_table5169
- GCC_except_table5171
- GCC_except_table5174
- GCC_except_table5249
- GCC_except_table5263
- GCC_except_table5266
- GCC_except_table5271
- GCC_except_table5278
- GCC_except_table5333
- GCC_except_table5400
- GCC_except_table5415
- GCC_except_table5418
- GCC_except_table5510
- GCC_except_table5511
- GCC_except_table5513
- GCC_except_table5518
- GCC_except_table5522
- GCC_except_table5525
- GCC_except_table5527
- GCC_except_table5535
- GCC_except_table5802
- GCC_except_table5805
- GCC_except_table5817
- GCC_except_table5893
- GCC_except_table5939
- GCC_except_table6032
- GCC_except_table6229
- GCC_except_table6241
- GCC_except_table6243
- GCC_except_table6268
- GCC_except_table6269
- GCC_except_table6270
- GCC_except_table6271
- GCC_except_table6330
- GCC_except_table6340
- GCC_except_table6502
- GCC_except_table6503
- GCC_except_table6615
- GCC_except_table6617
- GCC_except_table6632
- GCC_except_table6757
- GCC_except_table6759
- GCC_except_table6777
- GCC_except_table6823
- GCC_except_table6918
- GCC_except_table6938
- GCC_except_table6939
- GCC_except_table6940
- GCC_except_table6942
- GCC_except_table6945
- GCC_except_table6946
- GCC_except_table6948
- GCC_except_table720
- GCC_except_table723
- GCC_except_table7306
- GCC_except_table7312
- GCC_except_table7314
- GCC_except_table7324
- GCC_except_table7325
- GCC_except_table7532
- GCC_except_table7536
- GCC_except_table7619
- GCC_except_table7644
- GCC_except_table7650
- GCC_except_table7651
- GCC_except_table7818
- GCC_except_table7825
- GCC_except_table7946
- GCC_except_table8001
- GCC_except_table8003
- GCC_except_table8005
- GCC_except_table8027
- GCC_except_table8057
- GCC_except_table8069
- GCC_except_table8095
- GCC_except_table8101
- GCC_except_table8112
- GCC_except_table8114
- GCC_except_table8116
- GCC_except_table8118
- GCC_except_table8120
- GCC_except_table8122
- GCC_except_table8124
- GCC_except_table8126
- GCC_except_table8128
- GCC_except_table8130
- GCC_except_table8132
- GCC_except_table8134
- GCC_except_table8136
- GCC_except_table8141
- GCC_except_table8155
- GCC_except_table8156
- GCC_except_table8179
- GCC_except_table8181
- GCC_except_table8206
- GCC_except_table8219
- GCC_except_table8237
- GCC_except_table824
- GCC_except_table843
- GCC_except_table853
- GCC_except_table8771
- GCC_except_table8814
- GCC_except_table8907
- GCC_except_table8916
- GCC_except_table9091
- GCC_except_table9093
- GCC_except_table9094
- GCC_except_table9095
- GCC_except_table9097
- GCC_except_table9099
- GCC_except_table9100
- GCC_except_table9101
- GCC_except_table9136
- GCC_except_table9139
- GCC_except_table9140
- GCC_except_table9143
- GCC_except_table9146
- GCC_except_table9147
- GCC_except_table9190
- GCC_except_table9191
- GCC_except_table9192
- GCC_except_table9199
- GCC_except_table9200
- GCC_except_table9202
- GCC_except_table9221
- GCC_except_table9290
- GCC_except_table9291
- GCC_except_table9292
- GCC_except_table9325
- GCC_except_table9334
- GCC_except_table9348
- GCC_except_table9419
- GCC_except_table9449
- GCC_except_table9450
- GCC_except_table9451
- GCC_except_table9453
- GCC_except_table9456
- GCC_except_table9457
- GCC_except_table9464
- GCC_except_table9615
- GCC_except_table9616
- GCC_except_table9617
- GCC_except_table9621
- GCC_except_table9676
- GCC_except_table9697
- GCC_except_table9779
- GCC_except_table9781
- GCC_except_table9783
- GCC_except_table9785
- GCC_except_table9793
- GCC_except_table9843
- GCC_except_table9855
- GCC_except_table9857
- GCC_except_table9873
- GCC_except_table9902
- __OBJC_$_CLASS_METHODS_HMAccessory(Identifier|SwiftExtensions|HomeKit|HomeKit1|DynamicAccessorySettingsAdapter|PendingConfiguration|Private|CUPeerIdentifier|Diagnostics|ThreadManagement|SiriEndpoint|Television|ErrorStatus|LightInternal|HMDoorbellChimeProfile|NetworkRouter|Shortcuts|Camera|CameraInternal|CHIP|NetworkConfiguration|Climate|Light|Media)
- __OBJC_$_INSTANCE_METHODS_HMAccessory(Identifier|SwiftExtensions|HomeKit|HomeKit1|DynamicAccessorySettingsAdapter|PendingConfiguration|Private|CUPeerIdentifier|Diagnostics|ThreadManagement|SiriEndpoint|Television|ErrorStatus|LightInternal|HMDoorbellChimeProfile|NetworkRouter|Shortcuts|Camera|CameraInternal|CHIP|NetworkConfiguration|Climate|Light|Media)
- __OBJC_$_INSTANCE_METHODS_HMClientConnection
- ___88-[HMMediaGroupStagingManager notifyDestinationControllersWithDestinationControllerData:]_block_invoke_2
- ___block_descriptor_56_e8_32s40bs_e5_v8?0ls40l8s32l8
- ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls56l8s32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___swift_closure_destructor.121Tm
- _logCategory._hmf_once_t562
- _logCategory._hmf_once_t75
- _logCategory._hmf_once_t765
- _logCategory._hmf_once_t78
- _logCategory._hmf_once_t863
- _logCategory._hmf_once_t94
- _logCategory._hmf_once_v563
- _logCategory._hmf_once_v76
- _logCategory._hmf_once_v766
- _logCategory._hmf_once_v79
- _logCategory._hmf_once_v864
- _logCategory._hmf_once_v95
CStrings:
+ ", defaultName: %@"
+ ", stagedGroupNames: %@"
+ "-[HMHome _updateUnrecognizedUserSettingNamed:value:completion:]"
+ "-[HMHome updateUnrecognizedUserWebContentFilter:completion:]"
+ "21"
+ "<%@: %@>"
+ "Configuring last notified group name: %{private}@"
+ "Could not find scene identifiers in the message payload"
+ "Failed to get default group name due to no room for controller: %@"
+ "Failed to get destination controller from data source for group name identifier: %@"
+ "Failed to get staged home theater renames due to no data source"
+ "Failed to stage destination due to invalid destination identifier: %@"
+ "Failed to stage destination due to no staging manager"
+ "Failed to stage group name due to no default group name"
+ "Failed to stage group name due to no staging manager"
+ "Fetching unsecuring states for %ld scene identifiers"
+ "Finished fetching %ld scene unsecuring states"
+ "HM.getSceneUnsecuringStates"
+ "HMHomeSetUnrecognizedUserSettingRequestKey"
+ "HMHomeUnrecognizedUserSettingNameKey"
+ "HMHomeUnrecognizedUserSettingValueKey"
+ "HMHomeUnrecognizedUserSettingsCodingKey"
+ "HMUnrecognizedUserParentalControlSettingsValuesCodingKey"
+ "HomeKit_Private.HMUnrecognizedUserParentalControlSettings"
+ "Sending set request for setting %{public}@ for unrecognized people"
+ "Set request for setting %{public}@ for unrecognized people failed, error domain %{public}@ code %ld"
+ "Setting %{public}@ for unrecognized people is already set to the same value, skipping request"
+ "Settings for unrecognized people updated"
+ "Skipping notifying of update group name due to matching group name: %{private}@"
+ "Staging destination locally for controller: %@ destination: %@"
+ "Staging group name: %{private}@ locally for controller: %{public}@"
+ "[%{public}@] Configuring last notified group name: %{private}@"
+ "[%{public}@] Failed to get default group name due to no room for controller: %@"
+ "[%{public}@] Failed to get destination controller from data source for group name identifier: %@"
+ "[%{public}@] Failed to get staged home theater renames due to no data source"
+ "[%{public}@] Failed to stage destination due to invalid destination identifier: %@"
+ "[%{public}@] Failed to stage destination due to no staging manager"
+ "[%{public}@] Failed to stage group name due to no default group name"
+ "[%{public}@] Failed to stage group name due to no staging manager"
+ "[%{public}@] Sending set request for setting %{public}@ for unrecognized people"
+ "[%{public}@] Set request for setting %{public}@ for unrecognized people failed, error domain %{public}@ code %ld"
+ "[%{public}@] Setting %{public}@ for unrecognized people is already set to the same value, skipping request"
+ "[%{public}@] Settings for unrecognized people updated"
+ "[%{public}@] Skipping notifying of update group name due to matching group name: %{private}@"
+ "[%{public}@] Staging destination locally for controller: %@ destination: %@"
+ "[%{public}@] Staging group name: %{private}@ locally for controller: %{public}@"
+ "_NSPredicateUtilities"
+ "compound predicates are nested deeper than %d levels"
+ "constant value contains a disallowed type: %@"
+ "containsUnsecuringAction"
+ "controller"
+ "expression '%@' is not recognized"
+ "expression type not allowed: %@"
+ "function '%@' is not allowed"
+ "keyPath '%@' is not allowed"
+ "operator '%@' is not allowed"
+ "operator '%@' is not recognized"
+ "operator '%@' is not used by HomeKit predicates"
+ "predicate could not be archived: %@"
+ "predicate too large (%lu bytes, limit %d)"
+ "sceneIdentifierListKey"
+ "unrecognizedUserAllowExplicitContent"
+ "unrecognizedUserBroadWorldKnowledgeAllowed"
+ "unrecognizedUserMathAssistanceAllowed"
+ "unrecognizedUserSafariEnabled"
+ "unrecognizedUserSensitiveTopicsAllowed"
+ "unrecognizedUserWebContentFilter"
+ "unrecognizedUserWritingAssistanceAllowed"
+ "v16@?0@\"HMMediaGroupStageHomeTheaterRename\"8"
+ "v32@?0@\"NSString\"8@\"NSNumber\"16^B24"
+ "\xa1\xf0\xf0\xd1"
+ "…"
- "2!"
- "\xa1\xf0\xf0\xc1"
- "\xe1!"
```
