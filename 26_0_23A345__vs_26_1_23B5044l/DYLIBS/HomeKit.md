## HomeKit

> `/System/Library/Frameworks/HomeKit.framework/HomeKit`

```diff

-1349.1.3.1.1
-  __TEXT.__text: 0x2c889c
-  __TEXT.__auth_stubs: 0x1b00
-  __TEXT.__objc_methlist: 0x257bc
-  __TEXT.__const: 0x1d0c
+1368.1.0.1.2
+  __TEXT.__text: 0x2d0da0
+  __TEXT.__auth_stubs: 0x1b60
+  __TEXT.__objc_methlist: 0x25b74
+  __TEXT.__const: 0x236c
   __TEXT.__dlopen_cstrs: 0x3a1
-  __TEXT.__cstring: 0x2a512
-  __TEXT.__swift5_typeref: 0xa4c
-  __TEXT.__constg_swiftt: 0x8fc
-  __TEXT.__swift5_reflstr: 0x391
-  __TEXT.__swift5_fieldmd: 0x5d8
-  __TEXT.__swift5_assocty: 0x128
+  __TEXT.__cstring: 0x2a82a
+  __TEXT.__swift5_typeref: 0xbc8
+  __TEXT.__constg_swiftt: 0xa58
+  __TEXT.__swift5_reflstr: 0x3f1
+  __TEXT.__swift5_fieldmd: 0x738
+  __TEXT.__swift5_assocty: 0x148
   __TEXT.__swift5_capture: 0x74
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_protos: 0x20
-  __TEXT.__swift5_proto: 0x168
-  __TEXT.__swift5_types: 0xa4
-  __TEXT.__swift_as_entry: 0x1c
-  __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__oslogstring: 0x2ab9d
+  __TEXT.__swift5_proto: 0x1e0
+  __TEXT.__swift5_types: 0xcc
+  __TEXT.__swift_as_entry: 0x20
+  __TEXT.__swift_as_ret: 0x20
+  __TEXT.__oslogstring: 0x2af25
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__gcc_except_tab: 0x706c
+  __TEXT.__gcc_except_tab: 0x7178
   __TEXT.__ustring: 0x50
-  __TEXT.__unwind_info: 0x9a50
-  __TEXT.__eh_frame: 0xd88
-  __TEXT.__objc_classname: 0x4fc1
-  __TEXT.__objc_methname: 0x48353
-  __TEXT.__objc_methtype: 0x88d8
-  __TEXT.__objc_stubs: 0x25c80
-  __DATA_CONST.__got: 0x1818
-  __DATA_CONST.__const: 0x7e10
-  __DATA_CONST.__objc_classlist: 0x1228
+  __TEXT.__unwind_info: 0x9cc8
+  __TEXT.__eh_frame: 0x10d0
+  __TEXT.__objc_classname: 0x5050
+  __TEXT.__objc_methname: 0x48a62
+  __TEXT.__objc_methtype: 0x893e
+  __TEXT.__objc_stubs: 0x25da0
+  __DATA_CONST.__got: 0x1848
+  __DATA_CONST.__const: 0x7e78
+  __DATA_CONST.__objc_classlist: 0x1248
   __DATA_CONST.__objc_catlist: 0x108
   __DATA_CONST.__objc_protolist: 0x4b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd180
+  __DATA_CONST.__objc_selrefs: 0xd290
   __DATA_CONST.__objc_protorefs: 0xb8
-  __DATA_CONST.__objc_superrefs: 0xf30
+  __DATA_CONST.__objc_superrefs: 0xf50
   __DATA_CONST.__objc_arraydata: 0x1380
-  __AUTH_CONST.__auth_got: 0xd90
-  __AUTH_CONST.__const: 0x2d20
-  __AUTH_CONST.__cfstring: 0x277c0
-  __AUTH_CONST.__objc_const: 0x436b0
+  __AUTH_CONST.__auth_got: 0xdc0
+  __AUTH_CONST.__const: 0x31a8
+  __AUTH_CONST.__cfstring: 0x27ba0
+  __AUTH_CONST.__objc_const: 0x43e80
   __AUTH_CONST.__objc_intobj: 0x7c8
   __AUTH_CONST.__objc_dictobj: 0x848
   __AUTH_CONST.__objc_arrayobj: 0x570
   __AUTH_CONST.__objc_doubleobj: 0x70
-  __AUTH.__objc_data: 0x8348
-  __AUTH.__data: 0x580
-  __DATA.__objc_ivar: 0x2528
-  __DATA.__data: 0x3e18
-  __DATA.__bss: 0x31b0
+  __AUTH.__objc_data: 0x8488
+  __AUTH.__data: 0x6b0
+  __DATA.__objc_ivar: 0x256c
+  __DATA.__data: 0x3f90
+  __DATA.__bss: 0x3fc0
   __DATA.__common: 0x59
   __DATA_DIRTY.__objc_data: 0x33e0
   __DATA_DIRTY.__data: 0x28

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5E5857B7-2036-3A87-85DE-E4A50E25E8BD
-  Functions: 14346
-  Symbols:   44050
-  CStrings:  25661
+  UUID: 628C190A-F6F1-3A92-B97B-8BB024775761
+  Functions: 14562
+  Symbols:   44330
+  CStrings:  25803
 
Symbols:
+ +[CLLocationManager(HomeLocation) hm_locationAuthorizationFromCLAuthorizationStatus:]
+ +[CLLocationManager(HomeLocation) hm_regionStateFromCLRegionState:]
+ +[HMVendorDataStore logCategory]
+ +[HMVendorModelEntry shortDescription]
+ +[HMVendorModelEntry vendorModelEntryFromDictionaryRepresentation:]
+ -[HMAccessorySettingsDataSource _logModifiedAccessorySetting:error:]
+ -[HMCHIPVendorMetadataVendor initWithIdentifier:name:]
+ -[HMHome(PowerAssertionInfo) fetchPowerAssertionInfo:]
+ -[HMHomeManager postHH2UpdateRequiredCarPlayNotificationWithCompletion:]
+ -[HMMediaDestinationController containsSupportedOptions:]
+ -[HMMediaDestinationControllerRequestMessagePayload .cxx_destruct]
+ -[HMMediaDestinationControllerRequestMessagePayload attributeDescriptions]
+ -[HMMediaDestinationControllerRequestMessagePayload destinationIdentifier]
+ -[HMMediaDestinationControllerRequestMessagePayload hash]
+ -[HMMediaDestinationControllerRequestMessagePayload initWithDestination:options:]
+ -[HMMediaDestinationControllerRequestMessagePayload initWithDestinationIdentifier:updateOptions:]
+ -[HMMediaDestinationControllerRequestMessagePayload initWithNoDestination]
+ -[HMMediaDestinationControllerRequestMessagePayload initWithPayload:]
+ -[HMMediaDestinationControllerRequestMessagePayload isEqual:]
+ -[HMMediaDestinationControllerRequestMessagePayload payloadCopy]
+ -[HMMediaDestinationControllerRequestMessagePayload updateOptions]
+ -[HMMediaGroupProtoMediaGroupRole hasSurroundSystem]
+ -[HMMediaGroupProtoMediaGroupRole setSurroundSystem:]
+ -[HMMediaGroupProtoMediaGroupRole surroundSystem]
+ -[HMMediaGroupProtoSurroundSystemRoles .cxx_destruct]
+ -[HMMediaGroupProtoSurroundSystemRoles copyTo:]
+ -[HMMediaGroupProtoSurroundSystemRoles copyWithZone:]
+ -[HMMediaGroupProtoSurroundSystemRoles description]
+ -[HMMediaGroupProtoSurroundSystemRoles dictionaryRepresentation]
+ -[HMMediaGroupProtoSurroundSystemRoles frontLeftDestinationIdentifier]
+ -[HMMediaGroupProtoSurroundSystemRoles frontRightDestinationIdentifier]
+ -[HMMediaGroupProtoSurroundSystemRoles hasFrontLeftDestinationIdentifier]
+ -[HMMediaGroupProtoSurroundSystemRoles hasFrontRightDestinationIdentifier]
+ -[HMMediaGroupProtoSurroundSystemRoles hasRearLeftDestinationIdentifier]
+ -[HMMediaGroupProtoSurroundSystemRoles hasRearRightDestinationIdentifier]
+ -[HMMediaGroupProtoSurroundSystemRoles hash]
+ -[HMMediaGroupProtoSurroundSystemRoles isEqual:]
+ -[HMMediaGroupProtoSurroundSystemRoles mergeFrom:]
+ -[HMMediaGroupProtoSurroundSystemRoles readFrom:]
+ -[HMMediaGroupProtoSurroundSystemRoles rearLeftDestinationIdentifier]
+ -[HMMediaGroupProtoSurroundSystemRoles rearRightDestinationIdentifier]
+ -[HMMediaGroupProtoSurroundSystemRoles setFrontLeftDestinationIdentifier:]
+ -[HMMediaGroupProtoSurroundSystemRoles setFrontRightDestinationIdentifier:]
+ -[HMMediaGroupProtoSurroundSystemRoles setRearLeftDestinationIdentifier:]
+ -[HMMediaGroupProtoSurroundSystemRoles setRearRightDestinationIdentifier:]
+ -[HMMediaGroupProtoSurroundSystemRoles writeTo:]
+ -[HMUserActionPredictionDuetPredictionValue hasLegacyScore]
+ -[HMUserActionPredictionDuetPredictionValue hasMapIsValid]
+ -[HMUserActionPredictionDuetPredictionValue hasModelHasSignificantData]
+ -[HMUserActionPredictionDuetPredictionValue hasReason]
+ -[HMUserActionPredictionDuetPredictionValue legacyScore]
+ -[HMUserActionPredictionDuetPredictionValue mapIsValid]
+ -[HMUserActionPredictionDuetPredictionValue modelHasSignificantData]
+ -[HMUserActionPredictionDuetPredictionValue reason]
+ -[HMUserActionPredictionDuetPredictionValue setHasLegacyScore:]
+ -[HMUserActionPredictionDuetPredictionValue setHasMapIsValid:]
+ -[HMUserActionPredictionDuetPredictionValue setHasModelHasSignificantData:]
+ -[HMUserActionPredictionDuetPredictionValue setLegacyScore:]
+ -[HMUserActionPredictionDuetPredictionValue setMapIsValid:]
+ -[HMUserActionPredictionDuetPredictionValue setModelHasSignificantData:]
+ -[HMUserActionPredictionDuetPredictionValue setReason:]
+ -[HMVendorDataStore .cxx_destruct]
+ -[HMVendorDataStore context]
+ -[HMVendorDataStore fetchVendorModelEntryForManufacturer:model:completion:]
+ -[HMVendorDataStore fetchVendorModelEntryForProductData:completion:]
+ -[HMVendorDataStore initWithContext:]
+ -[HMVendorDataStore init]
+ -[HMVendorDataStore messageTargetUUID]
+ -[HMVendorDataStore setUuid:]
+ -[HMVendorDataStore uuid]
+ -[HMVendorModelEntry .cxx_destruct]
+ -[HMVendorModelEntry appBundleID]
+ -[HMVendorModelEntry appStoreID]
+ -[HMVendorModelEntry attributeDescriptions]
+ -[HMVendorModelEntry copyWithZone:]
+ -[HMVendorModelEntry description]
+ -[HMVendorModelEntry dictionaryRepresentation]
+ -[HMVendorModelEntry firmwareVersion]
+ -[HMVendorModelEntry hash]
+ -[HMVendorModelEntry initWithManufacturer:model:appBundleID:appStoreID:firmwareVersion:productData:productDataAlternates:]
+ -[HMVendorModelEntry isEqual:]
+ -[HMVendorModelEntry manufacturer]
+ -[HMVendorModelEntry model]
+ -[HMVendorModelEntry privateDescription]
+ -[HMVendorModelEntry productDataAlternates]
+ -[HMVendorModelEntry productData]
+ -[HMVendorModelEntry shortDescription]
+ GCC_except_table10006
+ GCC_except_table10026
+ GCC_except_table10027
+ GCC_except_table10028
+ GCC_except_table10069
+ GCC_except_table10071
+ GCC_except_table10168
+ GCC_except_table10172
+ GCC_except_table10189
+ GCC_except_table10191
+ GCC_except_table10197
+ GCC_except_table10201
+ GCC_except_table10204
+ GCC_except_table10211
+ GCC_except_table10215
+ GCC_except_table10221
+ GCC_except_table10233
+ GCC_except_table10236
+ GCC_except_table10244
+ GCC_except_table10245
+ GCC_except_table10247
+ GCC_except_table10249
+ GCC_except_table10251
+ GCC_except_table10263
+ GCC_except_table10273
+ GCC_except_table10489
+ GCC_except_table10538
+ GCC_except_table10543
+ GCC_except_table10547
+ GCC_except_table10555
+ GCC_except_table10603
+ GCC_except_table10606
+ GCC_except_table10607
+ GCC_except_table10954
+ GCC_except_table11002
+ GCC_except_table11015
+ GCC_except_table1120
+ GCC_except_table1124
+ GCC_except_table1131
+ GCC_except_table11384
+ GCC_except_table11386
+ GCC_except_table11388
+ GCC_except_table11389
+ GCC_except_table11419
+ GCC_except_table11421
+ GCC_except_table11424
+ GCC_except_table11431
+ GCC_except_table11432
+ GCC_except_table11433
+ GCC_except_table11541
+ GCC_except_table11542
+ GCC_except_table11568
+ GCC_except_table11570
+ GCC_except_table11574
+ GCC_except_table11575
+ GCC_except_table11623
+ GCC_except_table11649
+ GCC_except_table11662
+ GCC_except_table11746
+ GCC_except_table11747
+ GCC_except_table11748
+ GCC_except_table11749
+ GCC_except_table11750
+ GCC_except_table11751
+ GCC_except_table11752
+ GCC_except_table11753
+ GCC_except_table11754
+ GCC_except_table11755
+ GCC_except_table11756
+ GCC_except_table11757
+ GCC_except_table11758
+ GCC_except_table11759
+ GCC_except_table11760
+ GCC_except_table11761
+ GCC_except_table11784
+ GCC_except_table11811
+ GCC_except_table11921
+ GCC_except_table11922
+ GCC_except_table11990
+ GCC_except_table11992
+ GCC_except_table12000
+ GCC_except_table12011
+ GCC_except_table12013
+ GCC_except_table12018
+ GCC_except_table12019
+ GCC_except_table12020
+ GCC_except_table12225
+ GCC_except_table1223
+ GCC_except_table1232
+ GCC_except_table12425
+ GCC_except_table12428
+ GCC_except_table12433
+ GCC_except_table12437
+ GCC_except_table12443
+ GCC_except_table12448
+ GCC_except_table12450
+ GCC_except_table12455
+ GCC_except_table12456
+ GCC_except_table12458
+ GCC_except_table12540
+ GCC_except_table12542
+ GCC_except_table12561
+ GCC_except_table12562
+ GCC_except_table12563
+ GCC_except_table12564
+ GCC_except_table12569
+ GCC_except_table12583
+ GCC_except_table12589
+ GCC_except_table12592
+ GCC_except_table12594
+ GCC_except_table12672
+ GCC_except_table12680
+ GCC_except_table12681
+ GCC_except_table12686
+ GCC_except_table12692
+ GCC_except_table12694
+ GCC_except_table12696
+ GCC_except_table12698
+ GCC_except_table12700
+ GCC_except_table12702
+ GCC_except_table12704
+ GCC_except_table12837
+ GCC_except_table12893
+ GCC_except_table12894
+ GCC_except_table12895
+ GCC_except_table12896
+ GCC_except_table12906
+ GCC_except_table12907
+ GCC_except_table12931
+ GCC_except_table12932
+ GCC_except_table12988
+ GCC_except_table130
+ GCC_except_table1300
+ GCC_except_table13010
+ GCC_except_table13013
+ GCC_except_table1302
+ GCC_except_table1305
+ GCC_except_table1307
+ GCC_except_table1309
+ GCC_except_table131
+ GCC_except_table13110
+ GCC_except_table1313
+ GCC_except_table13153
+ GCC_except_table13348
+ GCC_except_table13353
+ GCC_except_table13356
+ GCC_except_table13416
+ GCC_except_table13516
+ GCC_except_table13526
+ GCC_except_table13587
+ GCC_except_table13590
+ GCC_except_table13610
+ GCC_except_table13612
+ GCC_except_table13613
+ GCC_except_table1362
+ GCC_except_table1511
+ GCC_except_table1534
+ GCC_except_table1602
+ GCC_except_table1657
+ GCC_except_table1660
+ GCC_except_table1678
+ GCC_except_table1745
+ GCC_except_table1747
+ GCC_except_table1758
+ GCC_except_table1760
+ GCC_except_table1872
+ GCC_except_table1942
+ GCC_except_table1945
+ GCC_except_table2017
+ GCC_except_table2103
+ GCC_except_table2104
+ GCC_except_table2153
+ GCC_except_table2356
+ GCC_except_table2359
+ GCC_except_table2362
+ GCC_except_table2367
+ GCC_except_table2371
+ GCC_except_table2380
+ GCC_except_table2393
+ GCC_except_table2395
+ GCC_except_table2396
+ GCC_except_table2401
+ GCC_except_table2402
+ GCC_except_table2403
+ GCC_except_table2404
+ GCC_except_table2817
+ GCC_except_table2822
+ GCC_except_table2848
+ GCC_except_table2851
+ GCC_except_table2901
+ GCC_except_table2917
+ GCC_except_table2920
+ GCC_except_table2945
+ GCC_except_table2947
+ GCC_except_table2949
+ GCC_except_table2951
+ GCC_except_table3112
+ GCC_except_table3130
+ GCC_except_table3131
+ GCC_except_table3205
+ GCC_except_table3208
+ GCC_except_table3209
+ GCC_except_table3233
+ GCC_except_table3235
+ GCC_except_table3243
+ GCC_except_table3245
+ GCC_except_table3252
+ GCC_except_table3253
+ GCC_except_table3254
+ GCC_except_table3256
+ GCC_except_table3257
+ GCC_except_table3258
+ GCC_except_table3259
+ GCC_except_table3260
+ GCC_except_table3319
+ GCC_except_table3342
+ GCC_except_table3345
+ GCC_except_table3348
+ GCC_except_table3351
+ GCC_except_table3354
+ GCC_except_table3357
+ GCC_except_table3360
+ GCC_except_table3426
+ GCC_except_table3472
+ GCC_except_table3480
+ GCC_except_table3481
+ GCC_except_table3484
+ GCC_except_table3485
+ GCC_except_table3486
+ GCC_except_table3488
+ GCC_except_table3496
+ GCC_except_table3518
+ GCC_except_table3525
+ GCC_except_table3529
+ GCC_except_table3532
+ GCC_except_table3535
+ GCC_except_table3576
+ GCC_except_table3580
+ GCC_except_table3584
+ GCC_except_table3589
+ GCC_except_table3597
+ GCC_except_table3601
+ GCC_except_table3610
+ GCC_except_table3612
+ GCC_except_table3862
+ GCC_except_table3866
+ GCC_except_table3867
+ GCC_except_table3870
+ GCC_except_table3876
+ GCC_except_table3880
+ GCC_except_table3884
+ GCC_except_table3907
+ GCC_except_table3909
+ GCC_except_table3911
+ GCC_except_table3914
+ GCC_except_table3915
+ GCC_except_table3917
+ GCC_except_table3920
+ GCC_except_table4000
+ GCC_except_table4014
+ GCC_except_table4017
+ GCC_except_table4019
+ GCC_except_table4022
+ GCC_except_table4029
+ GCC_except_table4082
+ GCC_except_table4147
+ GCC_except_table4162
+ GCC_except_table4165
+ GCC_except_table4258
+ GCC_except_table4259
+ GCC_except_table4261
+ GCC_except_table4266
+ GCC_except_table4270
+ GCC_except_table4273
+ GCC_except_table4275
+ GCC_except_table4283
+ GCC_except_table4530
+ GCC_except_table4533
+ GCC_except_table4545
+ GCC_except_table4619
+ GCC_except_table4663
+ GCC_except_table4755
+ GCC_except_table4917
+ GCC_except_table4929
+ GCC_except_table4931
+ GCC_except_table4955
+ GCC_except_table4956
+ GCC_except_table4958
+ GCC_except_table5013
+ GCC_except_table5023
+ GCC_except_table5152
+ GCC_except_table5153
+ GCC_except_table5229
+ GCC_except_table5331
+ GCC_except_table5333
+ GCC_except_table5361
+ GCC_except_table5363
+ GCC_except_table538
+ GCC_except_table5381
+ GCC_except_table541
+ GCC_except_table5427
+ GCC_except_table543
+ GCC_except_table549
+ GCC_except_table551
+ GCC_except_table552
+ GCC_except_table5522
+ GCC_except_table5542
+ GCC_except_table5543
+ GCC_except_table5544
+ GCC_except_table5546
+ GCC_except_table5549
+ GCC_except_table5550
+ GCC_except_table5552
+ GCC_except_table5810
+ GCC_except_table5816
+ GCC_except_table5818
+ GCC_except_table5828
+ GCC_except_table5829
+ GCC_except_table6032
+ GCC_except_table6036
+ GCC_except_table6109
+ GCC_except_table6240
+ GCC_except_table6247
+ GCC_except_table6252
+ GCC_except_table6437
+ GCC_except_table6490
+ GCC_except_table6679
+ GCC_except_table6688
+ GCC_except_table6696
+ GCC_except_table6725
+ GCC_except_table6730
+ GCC_except_table6733
+ GCC_except_table6747
+ GCC_except_table6752
+ GCC_except_table6758
+ GCC_except_table6763
+ GCC_except_table6768
+ GCC_except_table6778
+ GCC_except_table6782
+ GCC_except_table6787
+ GCC_except_table6843
+ GCC_except_table6870
+ GCC_except_table6875
+ GCC_except_table6882
+ GCC_except_table6897
+ GCC_except_table6898
+ GCC_except_table6900
+ GCC_except_table6902
+ GCC_except_table6905
+ GCC_except_table6910
+ GCC_except_table6917
+ GCC_except_table6922
+ GCC_except_table6926
+ GCC_except_table6960
+ GCC_except_table7017
+ GCC_except_table7021
+ GCC_except_table7023
+ GCC_except_table7024
+ GCC_except_table710
+ GCC_except_table713
+ GCC_except_table7163
+ GCC_except_table7170
+ GCC_except_table718
+ GCC_except_table721
+ GCC_except_table722
+ GCC_except_table7255
+ GCC_except_table7288
+ GCC_except_table7343
+ GCC_except_table7345
+ GCC_except_table7347
+ GCC_except_table7371
+ GCC_except_table7413
+ GCC_except_table7429
+ GCC_except_table7435
+ GCC_except_table744
+ GCC_except_table7446
+ GCC_except_table7448
+ GCC_except_table7454
+ GCC_except_table7456
+ GCC_except_table7458
+ GCC_except_table7460
+ GCC_except_table7462
+ GCC_except_table7464
+ GCC_except_table7466
+ GCC_except_table7468
+ GCC_except_table7470
+ GCC_except_table7472
+ GCC_except_table7474
+ GCC_except_table7479
+ GCC_except_table7492
+ GCC_except_table7493
+ GCC_except_table7498
+ GCC_except_table7517
+ GCC_except_table7519
+ GCC_except_table7544
+ GCC_except_table7558
+ GCC_except_table7576
+ GCC_except_table761
+ GCC_except_table7756
+ GCC_except_table78
+ GCC_except_table780
+ GCC_except_table80
+ GCC_except_table8019
+ GCC_except_table8062
+ GCC_except_table8122
+ GCC_except_table8238
+ GCC_except_table8241
+ GCC_except_table830
+ GCC_except_table833
+ GCC_except_table8331
+ GCC_except_table834
+ GCC_except_table8350
+ GCC_except_table8360
+ GCC_except_table8496
+ GCC_except_table8505
+ GCC_except_table8518
+ GCC_except_table8525
+ GCC_except_table8564
+ GCC_except_table8594
+ GCC_except_table8596
+ GCC_except_table8598
+ GCC_except_table8600
+ GCC_except_table8607
+ GCC_except_table8613
+ GCC_except_table8617
+ GCC_except_table8627
+ GCC_except_table8633
+ GCC_except_table8719
+ GCC_except_table8721
+ GCC_except_table8731
+ GCC_except_table8733
+ GCC_except_table8735
+ GCC_except_table8737
+ GCC_except_table8739
+ GCC_except_table8745
+ GCC_except_table8749
+ GCC_except_table8762
+ GCC_except_table8764
+ GCC_except_table8766
+ GCC_except_table8768
+ GCC_except_table8787
+ GCC_except_table8944
+ GCC_except_table8946
+ GCC_except_table8947
+ GCC_except_table8948
+ GCC_except_table8950
+ GCC_except_table8952
+ GCC_except_table8953
+ GCC_except_table8954
+ GCC_except_table8989
+ GCC_except_table8992
+ GCC_except_table8993
+ GCC_except_table8996
+ GCC_except_table8999
+ GCC_except_table900
+ GCC_except_table9000
+ GCC_except_table904
+ GCC_except_table9043
+ GCC_except_table9044
+ GCC_except_table9045
+ GCC_except_table905
+ GCC_except_table9052
+ GCC_except_table9053
+ GCC_except_table9055
+ GCC_except_table906
+ GCC_except_table907
+ GCC_except_table9074
+ GCC_except_table908
+ GCC_except_table909
+ GCC_except_table911
+ GCC_except_table913
+ GCC_except_table9146
+ GCC_except_table9147
+ GCC_except_table9148
+ GCC_except_table9185
+ GCC_except_table920
+ GCC_except_table921
+ GCC_except_table9369
+ GCC_except_table9370
+ GCC_except_table9371
+ GCC_except_table9375
+ GCC_except_table9430
+ GCC_except_table9451
+ GCC_except_table9527
+ GCC_except_table9529
+ GCC_except_table9531
+ GCC_except_table9541
+ GCC_except_table9588
+ GCC_except_table9600
+ GCC_except_table9602
+ GCC_except_table9618
+ GCC_except_table9646
+ GCC_except_table9820
+ GCC_except_table9822
+ GCC_except_table9824
+ GCC_except_table9868
+ GCC_except_table9869
+ GCC_except_table9904
+ GCC_except_table9937
+ GCC_except_table9940
+ GCC_except_table9943
+ GCC_except_table9945
+ OBJC_IVAR_$_HMMediaGroupProtoMediaGroupRole._surroundSystem
+ OBJC_IVAR_$_HMMediaGroupProtoSurroundSystemRoles._frontLeftDestinationIdentifier
+ OBJC_IVAR_$_HMMediaGroupProtoSurroundSystemRoles._frontRightDestinationIdentifier
+ OBJC_IVAR_$_HMMediaGroupProtoSurroundSystemRoles._rearLeftDestinationIdentifier
+ OBJC_IVAR_$_HMMediaGroupProtoSurroundSystemRoles._rearRightDestinationIdentifier
+ OBJC_IVAR_$_HMUserActionPredictionDuetPredictionValue._legacyScore
+ OBJC_IVAR_$_HMUserActionPredictionDuetPredictionValue._mapIsValid
+ OBJC_IVAR_$_HMUserActionPredictionDuetPredictionValue._modelHasSignificantData
+ OBJC_IVAR_$_HMUserActionPredictionDuetPredictionValue._reason
+ _CoreAnalyticsLibraryCore.frameworkLibrary.41013
+ _CoreHAPLibraryCore.frameworkLibrary.33293
+ _HMDumpIOPMAssertionBoolKey
+ _HMHomeFetchPowerAssertionsMessage
+ _HMHomeManagerHH2UpdateRequiredCarPlayNotificationMessage
+ _HMHomeManagerHH2UpdateRequiredCarPlayNotificationThresholdExceededKey
+ _HMLocationAuthorizationAsString
+ _HMMediaGroupProtoSurroundSystemRolesReadFrom
+ _HMRegionStateString
+ _IDSFoundationLibraryCore.45323
+ _IDSFoundationLibraryCore.frameworkLibrary.45326
+ _OBJC_CLASS_$_HMMediaDestinationControllerRequestMessagePayload
+ _OBJC_CLASS_$_HMMediaGroupProtoSurroundSystemRoles
+ _OBJC_CLASS_$_HMVendorDataStore
+ _OBJC_CLASS_$_HMVendorModelEntry
+ _OBJC_IVAR_$_HMMediaDestinationControllerRequestMessagePayload._destinationIdentifier
+ _OBJC_IVAR_$_HMMediaDestinationControllerRequestMessagePayload._updateOptions
+ _OBJC_IVAR_$_HMVendorDataStore._context
+ _OBJC_IVAR_$_HMVendorDataStore._uuid
+ _OBJC_IVAR_$_HMVendorModelEntry._appBundleID
+ _OBJC_IVAR_$_HMVendorModelEntry._appStoreID
+ _OBJC_IVAR_$_HMVendorModelEntry._firmwareVersion
+ _OBJC_IVAR_$_HMVendorModelEntry._manufacturer
+ _OBJC_IVAR_$_HMVendorModelEntry._model
+ _OBJC_IVAR_$_HMVendorModelEntry._productData
+ _OBJC_IVAR_$_HMVendorModelEntry._productDataAlternates
+ _OBJC_METACLASS_$_HMMediaDestinationControllerRequestMessagePayload
+ _OBJC_METACLASS_$_HMMediaGroupProtoSurroundSystemRoles
+ _OBJC_METACLASS_$_HMVendorDataStore
+ _OBJC_METACLASS_$_HMVendorModelEntry
+ _UIKitLibrary.45550
+ _UIKitLibraryCore.45546
+ _UIKitLibraryCore.frameworkLibrary.45559
+ __OBJC_$_CLASS_METHODS_HMHome(HomeKit|HomeKit1|AccessCode|WalletInternal|Wallet|Light|ThreadResidentCommissioning|HMAccessory|HMRoom|HMZone|HMServiceGroup|HMUser|HMActionSet|HMTrigger|RemoteAccess|HMSoftwareUpdate|HMMediaProfile|NetworkRouter|HMUserActionPredictions|ThreadManagement|HMHomeHub|PowerAssertionInfo|HomeNetworkInfo|HomeLocationFeedback|MediaGroupReadinessCheck|HomeActivityState|ResidentSelection|HMModernMessaging|HMModernMessagingInternal|Trigger|Climate|SiriEndpointProfilesMessengerFactory|HMActionExecution|Person|Person_Internal|Matter|CHIP|AutomationBuilders|Biome)
+ __OBJC_$_CLASS_METHODS_HMVendorDataStore
+ __OBJC_$_CLASS_METHODS_HMVendorModelEntry
+ __OBJC_$_INSTANCE_METHODS_HMHome(HomeKit|HomeKit1|AccessCode|WalletInternal|Wallet|Light|ThreadResidentCommissioning|HMAccessory|HMRoom|HMZone|HMServiceGroup|HMUser|HMActionSet|HMTrigger|RemoteAccess|HMSoftwareUpdate|HMMediaProfile|NetworkRouter|HMUserActionPredictions|ThreadManagement|HMHomeHub|PowerAssertionInfo|HomeNetworkInfo|HomeLocationFeedback|MediaGroupReadinessCheck|HomeActivityState|ResidentSelection|HMModernMessaging|HMModernMessagingInternal|Trigger|Climate|SiriEndpointProfilesMessengerFactory|HMActionExecution|Person|Person_Internal|Matter|CHIP|AutomationBuilders|Biome)
+ __OBJC_$_INSTANCE_METHODS_HMMediaDestinationControllerRequestMessagePayload
+ __OBJC_$_INSTANCE_METHODS_HMMediaGroupProtoSurroundSystemRoles
+ __OBJC_$_INSTANCE_METHODS_HMVendorDataStore
+ __OBJC_$_INSTANCE_METHODS_HMVendorModelEntry
+ __OBJC_$_INSTANCE_VARIABLES_HMMediaDestinationControllerRequestMessagePayload
+ __OBJC_$_INSTANCE_VARIABLES_HMMediaGroupProtoSurroundSystemRoles
+ __OBJC_$_INSTANCE_VARIABLES_HMVendorDataStore
+ __OBJC_$_INSTANCE_VARIABLES_HMVendorModelEntry
+ __OBJC_$_PROP_LIST_HMApplicationData.13497
+ __OBJC_$_PROP_LIST_HMMediaDestination.20098
+ __OBJC_$_PROP_LIST_HMMediaDestinationControllerRequestMessagePayload
+ __OBJC_$_PROP_LIST_HMMediaGroupProtoSurroundSystemRoles
+ __OBJC_$_PROP_LIST_HMVendorDataStore
+ __OBJC_$_PROP_LIST_HMVendorModelEntry
+ __OBJC_CLASS_PROTOCOLS_$_HMHome(HomeKit|HomeKit1|AccessCode|WalletInternal|Wallet|Light|ThreadResidentCommissioning|HMAccessory|HMRoom|HMZone|HMServiceGroup|HMUser|HMActionSet|HMTrigger|RemoteAccess|HMSoftwareUpdate|HMMediaProfile|NetworkRouter|HMUserActionPredictions|ThreadManagement|HMHomeHub|PowerAssertionInfo|HomeNetworkInfo|HomeLocationFeedback|MediaGroupReadinessCheck|HomeActivityState|ResidentSelection|HMModernMessaging|HMModernMessagingInternal|Trigger|Climate|SiriEndpointProfilesMessengerFactory|HMActionExecution|Person|Person_Internal|Matter|CHIP|AutomationBuilders|Biome)
+ __OBJC_CLASS_PROTOCOLS_$_HMMediaDestinationControllerRequestMessagePayload
+ __OBJC_CLASS_PROTOCOLS_$_HMMediaGroupProtoSurroundSystemRoles
+ __OBJC_CLASS_PROTOCOLS_$_HMVendorDataStore
+ __OBJC_CLASS_PROTOCOLS_$_HMVendorModelEntry
+ __OBJC_CLASS_RO_$_HMMediaDestinationControllerRequestMessagePayload
+ __OBJC_CLASS_RO_$_HMMediaGroupProtoSurroundSystemRoles
+ __OBJC_CLASS_RO_$_HMVendorDataStore
+ __OBJC_CLASS_RO_$_HMVendorModelEntry
+ __OBJC_METACLASS_RO_$_HMMediaDestinationControllerRequestMessagePayload
+ __OBJC_METACLASS_RO_$_HMMediaGroupProtoSurroundSystemRoles
+ __OBJC_METACLASS_RO_$_HMVendorDataStore
+ __OBJC_METACLASS_RO_$_HMVendorModelEntry
+ ___102-[HMHome(HMModernMessaging) unregisterModernMessagingRequestHandlerWithMessageName:completionHandler:]_block_invoke.2285
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.795
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.797
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.801
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.805
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.807
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.800
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.803
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.806
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_3.804
+ ___122-[HMHome(MediaGroupReadinessCheck) performMediaGroupReadinessCheckForAccessory:timeout:setupSessionIdentifier:completion:]_block_invoke.2242
+ ___123-[HMHome(HMModernMessaging) registerModernMessagingRequestHandlerWithMessageName:options:requestHandler:completionHandler:]_block_invoke.2284
+ ___140-[HMHome(HMModernMessaging) sendModernMessagingRequestWithMessageName:destination:requestPayload:options:responseHandler:completionHandler:]_block_invoke.2287
+ ___22-[HMHome _mergeRooms:]_block_invoke.983
+ ___22-[HMHome _mergeRooms:]_block_invoke.986
+ ___22-[HMHome _mergeRooms:]_block_invoke_2.988
+ ___22-[HMHome _mergeRooms:]_block_invoke_3.989
+ ___22-[HMHome _mergeUsers:]_block_invoke.1029
+ ___22-[HMHome _mergeUsers:]_block_invoke.1032
+ ___22-[HMHome _mergeUsers:]_block_invoke_2.1034
+ ___22-[HMHome _mergeUsers:]_block_invoke_3.1035
+ ___22-[HMHome _mergeZones:]_block_invoke.991
+ ___22-[HMHome _mergeZones:]_block_invoke.994
+ ___22-[HMHome _mergeZones:]_block_invoke_2.996
+ ___22-[HMHome _mergeZones:]_block_invoke_3.997
+ ___25-[HMHome _mergeTriggers:]_block_invoke.1025
+ ___25-[HMHome _mergeTriggers:]_block_invoke.1027
+ ___25-[HMXPCClient connection]_block_invoke.82
+ ___25-[HMXPCClient connection]_block_invoke.83
+ ___25-[HMXPCClient connection]_block_invoke.85
+ ___25-[HMXPCClient connection]_block_invoke_2
+ ___27-[HMHome _mergeActionSets:]_block_invoke.1016
+ ___27-[HMHome _mergeActionSets:]_block_invoke.1019
+ ___27-[HMHome _mergeActionSets:]_block_invoke_2.1021
+ ___27-[HMHome _mergeActionSets:]_block_invoke_3.1022
+ ___28-[HMHome _mergeAccessories:]_block_invoke.1002
+ ___28-[HMHome _mergeAccessories:]_block_invoke.1005
+ ___28-[HMHome _mergeAccessories:]_block_invoke.999
+ ___28-[HMHome _mergeAccessories:]_block_invoke_2.1006
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.731
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.735
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.739
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.743
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.745
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.749
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.753
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.765
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.769
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.773
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.777
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.781
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.937
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.946
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.949
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.957
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.960
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.963
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.966
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.968
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.971
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.974
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.977
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.979
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.732
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.736
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.740
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.744
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.746
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.750
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.754
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.766
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.770
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.774
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.778
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.782
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.938
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.947
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.950
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.958
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.961
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.964
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.967
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.970
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.973
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.976
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_3.952
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_4.953
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_5.954
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_6.955
+ ___30-[HMHome _mergeServiceGroups:]_block_invoke.1008
+ ___30-[HMHome _mergeServiceGroups:]_block_invoke.1011
+ ___30-[HMHome _mergeServiceGroups:]_block_invoke_2.1013
+ ___30-[HMHome _mergeServiceGroups:]_block_invoke_3.1014
+ ___32+[HMVendorDataStore logCategory]_block_invoke
+ ___32-[HMHome _mergeResidentDevices:]_block_invoke.1037
+ ___32-[HMHome _mergeResidentDevices:]_block_invoke.1040
+ ___32-[HMHome _mergeResidentDevices:]_block_invoke_2.1042
+ ___32-[HMHome _mergeResidentDevices:]_block_invoke_3.1043
+ ___36-[HMHome _mergeOutgoingInvitations:]_block_invoke.1045
+ ___36-[HMHome _mergeOutgoingInvitations:]_block_invoke.1047
+ ___38-[HMHomeManager _updateDataSyncState:]_block_invoke.537
+ ___39-[HMHome _mergeTriggerOwnedActionSets:]_block_invoke.1023
+ ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.809
+ ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.811
+ ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke.1049
+ ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke.1054
+ ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke_2.1053
+ ___45-[HMXPCClient sendMessage:completionHandler:]_block_invoke.90
+ ___45-[HMXPCClient sendMessage:completionHandler:]_block_invoke.91
+ ___46-[HMHomeManager removeHome:completionHandler:]_block_invoke.650
+ ___47-[HMHomeManager _recomputeAssistantIdentifiers]_block_invoke.719
+ ___51-[HMHomeManager _updatePrimaryHome:notifyDelegate:]_block_invoke.776
+ ___51-[HMHomeManager addHomeWithName:completionHandler:]_block_invoke.646
+ ___52-[HMHome(HMUser) _manageUsersWithCompletionHandler:]_block_invoke.2058
+ ___54-[HMHome(PowerAssertionInfo) fetchPowerAssertionInfo:]_block_invoke
+ ___54-[HMHome(PowerAssertionInfo) fetchPowerAssertionInfo:]_block_invoke.2222
+ ___54-[HMHome(PowerAssertionInfo) fetchPowerAssertionInfo:]_block_invoke_2
+ ___54-[HMHomeManager _refreshBeforeDate:completionHandler:]_block_invoke.632
+ ___54-[HMHomeManager _refreshBeforeDate:completionHandler:]_block_invoke.633
+ ___59-[HMHome(HMModernMessagingInternal) reRegisterHMMMHandlers]_block_invoke.2296
+ ___59-[HMHome(HomeActivityState) fetchCurrentHomeActivityState:]_block_invoke.2249
+ ___62-[HMOutgoingHomeInvitation _mergeWithNewAccessoryInvitations:]_block_invoke.130
+ ___64-[HMHome(HMMediaProfile) updateMediaPassword:completionHandler:]_block_invoke.2136
+ ___64-[HMHome(HomeNetworkInfo) fetchWiFiInfosWithTimeout:completion:]_block_invoke.2227
+ ___64-[HMHome(HomeNetworkInfo) fetchWiFiInfosWithTimeout:completion:]_block_invoke_2.2228
+ ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.737
+ ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.741
+ ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.743
+ ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.745
+ ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke_2.746
+ ___68-[HMVendorDataStore fetchVendorModelEntryForProductData:completion:]_block_invoke
+ ___69-[HMHomeManager addAndSetupAccessoriesWithPayload:completionHandler:]_block_invoke.868
+ ___71-[HMHome(HomeActivityState) changeHomeActivityState:completionHandler:]_block_invoke.2246
+ ___71-[HMHome(HomeNetworkInfo) getPrimaryResidentNetworkInfoWithCompletion:]_block_invoke.2225
+ ___71-[HMHome(HomeNetworkInfo) getPrimaryResidentNetworkInfoWithCompletion:]_block_invoke_2.2226
+ ___72-[HMHomeManager postHH2UpdateRequiredCarPlayNotificationWithCompletion:]_block_invoke
+ ___74-[HMHome(HomeNetworkInfo) fetchNetworkInfosFromTarget:timeout:completion:]_block_invoke.2229
+ ___74-[HMHome(HomeNetworkInfo) fetchNetworkInfosFromTarget:timeout:completion:]_block_invoke_2.2230
+ ___74-[HMHome(Trigger) fetchTriggerNameForTriggerIdentifier:completionHandler:]_block_invoke.2301
+ ___74-[HMHome(Trigger) fetchTriggerNameForTriggerIdentifier:completionHandler:]_block_invoke_2.2302
+ ___74-[HMHomeManager __processSyncResponse:refreshRequested:completionHandler:]_block_invoke.716
+ ___75-[HMHome(HMAccessory) addAndSetupAccessoriesWithPayload:completionHandler:]_block_invoke.1919
+ ___75-[HMVendorDataStore fetchVendorModelEntryForManufacturer:model:completion:]_block_invoke
+ ___78-[HMHome(HomeActivityState) cancelHomeActivityStateHoldWithCompletionHandler:]_block_invoke.2251
+ ___88-[HMHome(HMAccessory) addAccessoryWithAccessorySetupPayload:progress:completionHandler:]_block_invoke.1930
+ ___88-[HMHome(HMAccessory) addAndSetUpNewAccessoriesWithSuggestedRoomName:completionHandler:]_block_invoke.1921
+ ___88-[HMHome(HomeLocationFeedback) retrieveHomeKitLocationForFeedbackWithCompletionHandler:]_block_invoke.2237
+ ___89-[HMHome(NetworkRouter) updateAccessoryNetworkProtectionGroup:protectionMode:completion:]_block_invoke.2191
+ ___Block_byref_object_copy_.16739
+ ___Block_byref_object_copy_.17073
+ ___Block_byref_object_copy_.24685
+ ___Block_byref_object_copy_.27020
+ ___Block_byref_object_copy_.31767
+ ___Block_byref_object_copy_.33390
+ ___Block_byref_object_copy_.35577
+ ___Block_byref_object_copy_.40900
+ ___Block_byref_object_copy_.44353
+ ___Block_byref_object_copy_.64117
+ ___Block_byref_object_copy_.66530
+ ___Block_byref_object_dispose_.16740
+ ___Block_byref_object_dispose_.17074
+ ___Block_byref_object_dispose_.24686
+ ___Block_byref_object_dispose_.27021
+ ___Block_byref_object_dispose_.31768
+ ___Block_byref_object_dispose_.33391
+ ___Block_byref_object_dispose_.35578
+ ___Block_byref_object_dispose_.40901
+ ___Block_byref_object_dispose_.44354
+ ___Block_byref_object_dispose_.64118
+ ___Block_byref_object_dispose_.66531
+ ___CoreAnalyticsLibraryCore_block_invoke.41014
+ ___CoreHAPLibraryCore_block_invoke.33294
+ ___IDSFoundationLibraryCore_block_invoke.45327
+ ___UIKitLibraryCore_block_invoke.45560
+ ___block_literal_global.101.41021
+ ___block_literal_global.101.43204
+ ___block_literal_global.10395
+ ___block_literal_global.10828
+ ___block_literal_global.11099
+ ___block_literal_global.1167
+ ___block_literal_global.11681
+ ___block_literal_global.12.51727
+ ___block_literal_global.12396
+ ___block_literal_global.13429
+ ___block_literal_global.13550
+ ___block_literal_global.14539
+ ___block_literal_global.14680
+ ___block_literal_global.14755
+ ___block_literal_global.15002
+ ___block_literal_global.15375
+ ___block_literal_global.1560
+ ___block_literal_global.15604
+ ___block_literal_global.16186
+ ___block_literal_global.16536
+ ___block_literal_global.16827
+ ___block_literal_global.17.20318
+ ___block_literal_global.17455
+ ___block_literal_global.18663
+ ___block_literal_global.19.16521
+ ___block_literal_global.19194
+ ___block_literal_global.19375
+ ___block_literal_global.1938
+ ___block_literal_global.19508
+ ___block_literal_global.19668
+ ___block_literal_global.20325
+ ___block_literal_global.2055
+ ___block_literal_global.2078
+ ___block_literal_global.20983
+ ___block_literal_global.2133
+ ___block_literal_global.21448
+ ___block_literal_global.22087
+ ___block_literal_global.22454
+ ___block_literal_global.23425
+ ___block_literal_global.235
+ ___block_literal_global.23729
+ ___block_literal_global.24062
+ ___block_literal_global.24723
+ ___block_literal_global.24912
+ ___block_literal_global.25107
+ ___block_literal_global.25634
+ ___block_literal_global.2574
+ ___block_literal_global.25879
+ ___block_literal_global.26249
+ ___block_literal_global.26386
+ ___block_literal_global.26632
+ ___block_literal_global.26877
+ ___block_literal_global.27044
+ ___block_literal_global.27137
+ ___block_literal_global.27868
+ ___block_literal_global.29898
+ ___block_literal_global.30.20307
+ ___block_literal_global.30056
+ ___block_literal_global.30335
+ ___block_literal_global.31614
+ ___block_literal_global.31886
+ ___block_literal_global.32219
+ ___block_literal_global.32481
+ ___block_literal_global.32768
+ ___block_literal_global.32847
+ ___block_literal_global.33.65826
+ ___block_literal_global.33537
+ ___block_literal_global.34037
+ ___block_literal_global.34310
+ ___block_literal_global.35363
+ ___block_literal_global.35600
+ ___block_literal_global.35901
+ ___block_literal_global.37226
+ ___block_literal_global.38205
+ ___block_literal_global.38439
+ ___block_literal_global.38666
+ ___block_literal_global.39061
+ ___block_literal_global.39811
+ ___block_literal_global.4065
+ ___block_literal_global.41008
+ ___block_literal_global.41259
+ ___block_literal_global.41596
+ ___block_literal_global.42258
+ ___block_literal_global.43214
+ ___block_literal_global.43477
+ ___block_literal_global.43743
+ ___block_literal_global.4402
+ ___block_literal_global.44025
+ ___block_literal_global.44245
+ ___block_literal_global.4488
+ ___block_literal_global.45387
+ ___block_literal_global.45478
+ ___block_literal_global.4581
+ ___block_literal_global.46185
+ ___block_literal_global.46377
+ ___block_literal_global.47557
+ ___block_literal_global.47998
+ ___block_literal_global.48323
+ ___block_literal_global.49087
+ ___block_literal_global.49744
+ ___block_literal_global.50102
+ ___block_literal_global.51375
+ ___block_literal_global.51739
+ ___block_literal_global.52023
+ ___block_literal_global.52219
+ ___block_literal_global.523
+ ___block_literal_global.52448
+ ___block_literal_global.53166
+ ___block_literal_global.53286
+ ___block_literal_global.54041
+ ___block_literal_global.54275
+ ___block_literal_global.5441
+ ___block_literal_global.54730
+ ___block_literal_global.54992
+ ___block_literal_global.56070
+ ___block_literal_global.58.38434
+ ___block_literal_global.58351
+ ___block_literal_global.59216
+ ___block_literal_global.6027
+ ___block_literal_global.60503
+ ___block_literal_global.61232
+ ___block_literal_global.61783
+ ___block_literal_global.62093
+ ___block_literal_global.62610
+ ___block_literal_global.62787
+ ___block_literal_global.63176
+ ___block_literal_global.63421
+ ___block_literal_global.6426
+ ___block_literal_global.65230
+ ___block_literal_global.65565
+ ___block_literal_global.6562
+ ___block_literal_global.65832
+ ___block_literal_global.66187
+ ___block_literal_global.66469
+ ___block_literal_global.66825
+ ___block_literal_global.669
+ ___block_literal_global.6789
+ ___block_literal_global.7.24923
+ ___block_literal_global.710
+ ___block_literal_global.7281
+ ___block_literal_global.73.25081
+ ___block_literal_global.758
+ ___block_literal_global.760
+ ___block_literal_global.7645
+ ___block_literal_global.7792
+ ___block_literal_global.8295
+ ___block_literal_global.84.41202
+ ___block_literal_global.8549
+ ___block_literal_global.872
+ ___block_literal_global.9135
+ ___block_literal_global.9378
+ ___block_literal_global.94
+ ___block_literal_global.9776
+ ___getAnalyticsSendEventLazySymbolLoc_block_invoke.41011
+ ___getNSCharacterEncodingDocumentAttributeSymbolLoc_block_invoke.45555
+ ___getNSDocumentTypeDocumentAttributeSymbolLoc_block_invoke.45549
+ ___swift_memcpy40_8
+ _associated conformance So13HMHomeManagerC7HomeKitE06EnergyD0O15ClearAllMessageV15ResponsePayloadV10CodingKeys33_D6F9A83559A5658F48F47635E2FF827BLLOSHACSQ
+ _associated conformance So13HMHomeManagerC7HomeKitE06EnergyD0O15ClearAllMessageV15ResponsePayloadV10CodingKeys33_D6F9A83559A5658F48F47635E2FF827BLLOs0K3KeyACs23CustomStringConvertible
+ _associated conformance So13HMHomeManagerC7HomeKitE06EnergyD0O15ClearAllMessageV15ResponsePayloadV10CodingKeys33_D6F9A83559A5658F48F47635E2FF827BLLOs0K3KeyACs28CustomDebugStringConvertible
+ _associated conformance So13HMHomeManagerC7HomeKitE06EnergyD0O15ClearAllMessageV15ResponsePayloadV7FailureV10CodingKeys33_D6F9A83559A5658F48F47635E2FF827BLLOSHACSQ
+ _associated conformance So13HMHomeManagerC7HomeKitE06EnergyD0O15ClearAllMessageV15ResponsePayloadV7FailureV10CodingKeys33_D6F9A83559A5658F48F47635E2FF827BLLOs0L3KeyACs23CustomStringConvertible
+ _associated conformance So13HMHomeManagerC7HomeKitE06EnergyD0O15ClearAllMessageV15ResponsePayloadV7FailureV10CodingKeys33_D6F9A83559A5658F48F47635E2FF827BLLOs0L3KeyACs28CustomDebugStringConvertible
+ _associated conformance So13HMHomeManagerC7HomeKitE06EnergyD0O15ClearAllMessageV15ResponsePayloadV7FailureV12ErrorDetailsV10CodingKeys33_D6F9A83559A5658F48F47635E2FF827BLLOSHACSQ
+ _associated conformance So13HMHomeManagerC7HomeKitE06EnergyD0O15ClearAllMessageV15ResponsePayloadV7FailureV12ErrorDetailsV10CodingKeys33_D6F9A83559A5658F48F47635E2FF827BLLOs0N3KeyACs23CustomStringConvertible
+ _associated conformance So13HMHomeManagerC7HomeKitE06EnergyD0O15ClearAllMessageV15ResponsePayloadV7FailureV12ErrorDetailsV10CodingKeys33_D6F9A83559A5658F48F47635E2FF827BLLOs0N3KeyACs28CustomDebugStringConvertible
+ _associated conformance So13HMHomeManagerC7HomeKitE06EnergyD0O15ClearAllMessageV15ResponsePayloadV7SuccessV10CodingKeys33_D6F9A83559A5658F48F47635E2FF827BLLOSHACSQ
+ _associated conformance So13HMHomeManagerC7HomeKitE06EnergyD0O15ClearAllMessageV15ResponsePayloadV7SuccessV10CodingKeys33_D6F9A83559A5658F48F47635E2FF827BLLOs0L3KeyACs23CustomStringConvertible
+ _associated conformance So13HMHomeManagerC7HomeKitE06EnergyD0O15ClearAllMessageV15ResponsePayloadV7SuccessV10CodingKeys33_D6F9A83559A5658F48F47635E2FF827BLLOs0L3KeyACs28CustomDebugStringConvertible
+ _associated conformance So13HMHomeManagerC7HomeKitE06EnergyD0O15ClearAllMessageVAC19HMFMessagePrototypeO07RequestH0AC0K7PayloadAiJP_AI0L0
+ _associated conformance So13HMHomeManagerC7HomeKitE06EnergyD0O15ClearAllMessageVAC19HMFMessagePrototypeO07RequestH0AC15ResponsePayloadAiJP_AI0M0
+ _audit_stringCoreAnalytics.41017
+ _audit_stringCoreHAP.33296
+ _audit_stringIDSFoundation.45329
+ _audit_stringUIKit.45562
+ _getAnalyticsSendEventLazySymbolLoc.ptr.41010
+ _getNSCharacterEncodingDocumentAttributeSymbolLoc.ptr.45554
+ _getNSDocumentTypeDocumentAttributeSymbolLoc.ptr.45548
+ _kFetchVendorModelEntryForManufacturerRequestKey
+ _kFetchVendorModelEntryForProductDataRequestKey
+ _kManufacturerKey
+ _kModelKey
+ _kProductDataKey
+ _kVendorModelEntryDictionaryKey
+ _logCategory._hmf_once_t0.14754
+ _logCategory._hmf_once_t0.23728
+ _logCategory._hmf_once_t0.25106
+ _logCategory._hmf_once_t0.32480
+ _logCategory._hmf_once_t0.32846
+ _logCategory._hmf_once_t0.44024
+ _logCategory._hmf_once_t0.46184
+ _logCategory._hmf_once_t0.46376
+ _logCategory._hmf_once_t0.6026
+ _logCategory._hmf_once_t0.63420
+ _logCategory._hmf_once_t1.19507
+ _logCategory._hmf_once_t1.21447
+ _logCategory._hmf_once_t1.41235
+ _logCategory._hmf_once_t1.47556
+ _logCategory._hmf_once_t1.51726
+ _logCategory._hmf_once_t1.53285
+ _logCategory._hmf_once_t1.58350
+ _logCategory._hmf_once_t10.23424
+ _logCategory._hmf_once_t11.13428
+ _logCategory._hmf_once_t11.7644
+ _logCategory._hmf_once_t13.43203
+ _logCategory._hmf_once_t16.31885
+ _logCategory._hmf_once_t16.38438
+ _logCategory._hmf_once_t16.65229
+ _logCategory._hmf_once_t2.24922
+ _logCategory._hmf_once_t2.27043
+ _logCategory._hmf_once_t2.30334
+ _logCategory._hmf_once_t2.34036
+ _logCategory._hmf_once_t20.25646
+ _logCategory._hmf_once_t20.26631
+ _logCategory._hmf_once_t21.62786
+ _logCategory._hmf_once_t24.41595
+ _logCategory._hmf_once_t24.42257
+ _logCategory._hmf_once_t25.26876
+ _logCategory._hmf_once_t25.66186
+ _logCategory._hmf_once_t27.62092
+ _logCategory._hmf_once_t3.54264
+ _logCategory._hmf_once_t3.65825
+ _logCategory._hmf_once_t31.24722
+ _logCategory._hmf_once_t31.54729
+ _logCategory._hmf_once_t31.66824
+ _logCategory._hmf_once_t32.54040
+ _logCategory._hmf_once_t34.20982
+ _logCategory._hmf_once_t365
+ _logCategory._hmf_once_t37.55018
+ _logCategory._hmf_once_t4.15001
+ _logCategory._hmf_once_t4.1571
+ _logCategory._hmf_once_t4.6425
+ _logCategory._hmf_once_t44.26901
+ _logCategory._hmf_once_t45
+ _logCategory._hmf_once_t5.19193
+ _logCategory._hmf_once_t51.43742
+ _logCategory._hmf_once_t6.35362
+ _logCategory._hmf_once_t6.38204
+ _logCategory._hmf_once_t6.44244
+ _logCategory._hmf_once_t6.49743
+ _logCategory._hmf_once_t6.59215
+ _logCategory._hmf_once_t7.53165
+ _logCategory._hmf_once_t8.38665
+ _logCategory._hmf_once_t8.49086
+ _logCategory._hmf_once_t8.52237
+ _logCategory._hmf_once_t9.30055
+ _logCategory._hmf_once_v1.14756
+ _logCategory._hmf_once_v1.23730
+ _logCategory._hmf_once_v1.25108
+ _logCategory._hmf_once_v1.32482
+ _logCategory._hmf_once_v1.32848
+ _logCategory._hmf_once_v1.44026
+ _logCategory._hmf_once_v1.46186
+ _logCategory._hmf_once_v1.46378
+ _logCategory._hmf_once_v1.6028
+ _logCategory._hmf_once_v1.63422
+ _logCategory._hmf_once_v10.30057
+ _logCategory._hmf_once_v11.23426
+ _logCategory._hmf_once_v12.13430
+ _logCategory._hmf_once_v12.7646
+ _logCategory._hmf_once_v14.43205
+ _logCategory._hmf_once_v17.31887
+ _logCategory._hmf_once_v17.38440
+ _logCategory._hmf_once_v17.65231
+ _logCategory._hmf_once_v2.19509
+ _logCategory._hmf_once_v2.21449
+ _logCategory._hmf_once_v2.41236
+ _logCategory._hmf_once_v2.47558
+ _logCategory._hmf_once_v2.51728
+ _logCategory._hmf_once_v2.53287
+ _logCategory._hmf_once_v2.58352
+ _logCategory._hmf_once_v21.25647
+ _logCategory._hmf_once_v21.26633
+ _logCategory._hmf_once_v22.62788
+ _logCategory._hmf_once_v25.41597
+ _logCategory._hmf_once_v25.42259
+ _logCategory._hmf_once_v26.26878
+ _logCategory._hmf_once_v26.66188
+ _logCategory._hmf_once_v28.62094
+ _logCategory._hmf_once_v3.24924
+ _logCategory._hmf_once_v3.27045
+ _logCategory._hmf_once_v3.30336
+ _logCategory._hmf_once_v3.34038
+ _logCategory._hmf_once_v32.24724
+ _logCategory._hmf_once_v32.54731
+ _logCategory._hmf_once_v32.66826
+ _logCategory._hmf_once_v33.54042
+ _logCategory._hmf_once_v35.20984
+ _logCategory._hmf_once_v366
+ _logCategory._hmf_once_v38.55019
+ _logCategory._hmf_once_v4.54265
+ _logCategory._hmf_once_v4.65827
+ _logCategory._hmf_once_v45.26902
+ _logCategory._hmf_once_v46
+ _logCategory._hmf_once_v5.15003
+ _logCategory._hmf_once_v5.1572
+ _logCategory._hmf_once_v5.6427
+ _logCategory._hmf_once_v52.43744
+ _logCategory._hmf_once_v6.19195
+ _logCategory._hmf_once_v7.35364
+ _logCategory._hmf_once_v7.38206
+ _logCategory._hmf_once_v7.44246
+ _logCategory._hmf_once_v7.49745
+ _logCategory._hmf_once_v7.59217
+ _logCategory._hmf_once_v8.53167
+ _logCategory._hmf_once_v9.38667
+ _logCategory._hmf_once_v9.49088
+ _logCategory._hmf_once_v9.52238
+ _objc_msgSend$initWithDestination:options:
+ _objc_msgSend$initWithDestinationIdentifier:updateOptions:
+ _objc_msgSend$initWithManufacturer:model:appBundleID:appStoreID:firmwareVersion:productData:productDataAlternates:
+ _objc_msgSend$initWithNoDestination
+ _objc_msgSend$productData
+ _objc_msgSend$productDataAlternates
+ _objc_msgSend$setFrontLeftDestinationIdentifier:
+ _objc_msgSend$setFrontRightDestinationIdentifier:
+ _objc_msgSend$setRearLeftDestinationIdentifier:
+ _objc_msgSend$setRearRightDestinationIdentifier:
+ _objc_msgSend$setSurroundSystem:
+ _objc_msgSend$updateOptions
+ _objc_msgSend$updateUserInfo:responseHandler:
+ _objc_msgSend$vendorModelEntryFromDictionaryRepresentation:
+ _sharedInstance.onceToken.43213
+ _sharedManager.onceToken.62238
+ _supportedValueClasses.onceToken.52022
+ _supportedValueClasses.onceToken.60466
+ _supportedValueClasses.supportedValueClasses.52024
+ _supportedValueClasses.supportedValueClasses.60467
+ _symbolic SDy__________yyt______pGG 10Foundation4UUIDV s6ResultOsRi_zRi0_zrlE s5ErrorP
+ _symbolic Say_____G So13HMHomeManagerC7HomeKitE06EnergyD0O15ClearAllMessageV15ResponsePayloadV7FailureV
+ _symbolic Say_____G So13HMHomeManagerC7HomeKitE06EnergyD0O15ClearAllMessageV15ResponsePayloadV7SuccessV
+ _symbolic So13HMHomeManagerC
+ _symbolic _____ So13HMHomeManagerC7HomeKitE06EnergyD0O
+ _symbolic _____ So13HMHomeManagerC7HomeKitE06EnergyD0O15ClearAllMessageV
+ _symbolic _____ So13HMHomeManagerC7HomeKitE06EnergyD0O15ClearAllMessageV15ResponsePayloadV
+ _symbolic _____ So13HMHomeManagerC7HomeKitE06EnergyD0O15ClearAllMessageV15ResponsePayloadV10CodingKeys33_D6F9A83559A5658F48F47635E2FF827BLLO
+ _symbolic _____ So13HMHomeManagerC7HomeKitE06EnergyD0O15ClearAllMessageV15ResponsePayloadV7FailureV
+ _symbolic _____ So13HMHomeManagerC7HomeKitE06EnergyD0O15ClearAllMessageV15ResponsePayloadV7FailureV10CodingKeys33_D6F9A83559A5658F48F47635E2FF827BLLO
+ _symbolic _____ So13HMHomeManagerC7HomeKitE06EnergyD0O15ClearAllMessageV15ResponsePayloadV7FailureV12ErrorDetailsV
+ _symbolic _____ So13HMHomeManagerC7HomeKitE06EnergyD0O15ClearAllMessageV15ResponsePayloadV7FailureV12ErrorDetailsV10CodingKeys33_D6F9A83559A5658F48F47635E2FF827BLLO
+ _symbolic _____ So13HMHomeManagerC7HomeKitE06EnergyD0O15ClearAllMessageV15ResponsePayloadV7SuccessV
+ _symbolic _____ So13HMHomeManagerC7HomeKitE06EnergyD0O15ClearAllMessageV15ResponsePayloadV7SuccessV10CodingKeys33_D6F9A83559A5658F48F47635E2FF827BLLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV So13HMHomeManagerC7HomeKitE06EnergyG0O15ClearAllMessageV15ResponsePayloadV10CodingKeys33_D6F9A83559A5658F48F47635E2FF827BLLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV So13HMHomeManagerC7HomeKitE06EnergyG0O15ClearAllMessageV15ResponsePayloadV7FailureV10CodingKeys33_D6F9A83559A5658F48F47635E2FF827BLLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV So13HMHomeManagerC7HomeKitE06EnergyG0O15ClearAllMessageV15ResponsePayloadV7FailureV12ErrorDetailsV10CodingKeys33_D6F9A83559A5658F48F47635E2FF827BLLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV So13HMHomeManagerC7HomeKitE06EnergyG0O15ClearAllMessageV15ResponsePayloadV7SuccessV10CodingKeys33_D6F9A83559A5658F48F47635E2FF827BLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV So13HMHomeManagerC7HomeKitE06EnergyG0O15ClearAllMessageV15ResponsePayloadV10CodingKeys33_D6F9A83559A5658F48F47635E2FF827BLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV So13HMHomeManagerC7HomeKitE06EnergyG0O15ClearAllMessageV15ResponsePayloadV7FailureV10CodingKeys33_D6F9A83559A5658F48F47635E2FF827BLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV So13HMHomeManagerC7HomeKitE06EnergyG0O15ClearAllMessageV15ResponsePayloadV7FailureV12ErrorDetailsV10CodingKeys33_D6F9A83559A5658F48F47635E2FF827BLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV So13HMHomeManagerC7HomeKitE06EnergyG0O15ClearAllMessageV15ResponsePayloadV7SuccessV10CodingKeys33_D6F9A83559A5658F48F47635E2FF827BLLO
+ _symbolic _____y__________yyt______pGG s18_DictionaryStorageC 10Foundation4UUIDV s6ResultOsRi_zRi0_zrlE s5ErrorP
+ _type_layout_string So13HMHomeManagerC7HomeKitE06EnergyD0O15ClearAllMessageV15ResponsePayloadV
+ _type_layout_string So13HMHomeManagerC7HomeKitE06EnergyD0O15ClearAllMessageV15ResponsePayloadV7FailureV12ErrorDetailsV
- +[CLLocationManager(HomeLocation) hm_hmdLocationAuthorizationFromCLAuthorizationStatus:]
- +[CLLocationManager(HomeLocation) hm_hmdRegionStateFromCLRegionState:]
- +[HMMediaDestination payloadForDestination:options:]
- +[HMMediaDestination payloadForNullDestination]
- -[HMCHIPVendorMetadataVendor appBundleID]
- -[HMCHIPVendorMetadataVendor appStoreID]
- -[HMCHIPVendorMetadataVendor initWithIdentifier:name:appStoreID:appBundleID:]
- -[HMCharacteristic setContext:]
- -[HMHome mergeFromNewObjectNoMergeCount:]
- -[HMHomeManager requestLogEventDailySchedulerStatusWithCompletion:]
- -[HMObjectMergeCollection mergeCommonObjectsNoMergeCount]
- GCC_except_table10000
- GCC_except_table10002
- GCC_except_table10004
- GCC_except_table10099
- GCC_except_table10101
- GCC_except_table10105
- GCC_except_table10122
- GCC_except_table10124
- GCC_except_table10130
- GCC_except_table10137
- GCC_except_table10144
- GCC_except_table10148
- GCC_except_table10154
- GCC_except_table10169
- GCC_except_table10177
- GCC_except_table10178
- GCC_except_table10180
- GCC_except_table10182
- GCC_except_table10184
- GCC_except_table10196
- GCC_except_table10206
- GCC_except_table10409
- GCC_except_table10422
- GCC_except_table10471
- GCC_except_table10480
- GCC_except_table10488
- GCC_except_table10536
- GCC_except_table10539
- GCC_except_table10540
- GCC_except_table107
- GCC_except_table108
- GCC_except_table10887
- GCC_except_table1093
- GCC_except_table10935
- GCC_except_table10948
- GCC_except_table1097
- GCC_except_table1104
- GCC_except_table11317
- GCC_except_table11319
- GCC_except_table11321
- GCC_except_table11322
- GCC_except_table11352
- GCC_except_table11354
- GCC_except_table11357
- GCC_except_table11364
- GCC_except_table11365
- GCC_except_table11366
- GCC_except_table11474
- GCC_except_table11475
- GCC_except_table11501
- GCC_except_table11503
- GCC_except_table11507
- GCC_except_table11508
- GCC_except_table11556
- GCC_except_table11582
- GCC_except_table11595
- GCC_except_table11621
- GCC_except_table11625
- GCC_except_table11679
- GCC_except_table11680
- GCC_except_table11681
- GCC_except_table11682
- GCC_except_table11683
- GCC_except_table11684
- GCC_except_table11685
- GCC_except_table11686
- GCC_except_table11687
- GCC_except_table11689
- GCC_except_table11690
- GCC_except_table11691
- GCC_except_table11693
- GCC_except_table11694
- GCC_except_table11717
- GCC_except_table11744
- GCC_except_table11854
- GCC_except_table11855
- GCC_except_table11858
- GCC_except_table11923
- GCC_except_table11933
- GCC_except_table11944
- GCC_except_table11946
- GCC_except_table11951
- GCC_except_table11952
- GCC_except_table11953
- GCC_except_table1196
- GCC_except_table1205
- GCC_except_table12158
- GCC_except_table12358
- GCC_except_table12361
- GCC_except_table12366
- GCC_except_table12370
- GCC_except_table12376
- GCC_except_table12381
- GCC_except_table12383
- GCC_except_table12388
- GCC_except_table12389
- GCC_except_table12391
- GCC_except_table12473
- GCC_except_table12475
- GCC_except_table12494
- GCC_except_table12495
- GCC_except_table12496
- GCC_except_table12497
- GCC_except_table12502
- GCC_except_table12516
- GCC_except_table12522
- GCC_except_table12525
- GCC_except_table12527
- GCC_except_table12605
- GCC_except_table12613
- GCC_except_table12614
- GCC_except_table12619
- GCC_except_table12625
- GCC_except_table12627
- GCC_except_table12629
- GCC_except_table12631
- GCC_except_table12633
- GCC_except_table12635
- GCC_except_table12637
- GCC_except_table1273
- GCC_except_table1275
- GCC_except_table12770
- GCC_except_table1278
- GCC_except_table1280
- GCC_except_table1282
- GCC_except_table12826
- GCC_except_table12827
- GCC_except_table12828
- GCC_except_table12829
- GCC_except_table12839
- GCC_except_table12840
- GCC_except_table1286
- GCC_except_table12864
- GCC_except_table12865
- GCC_except_table12921
- GCC_except_table12943
- GCC_except_table12946
- GCC_except_table13043
- GCC_except_table13086
- GCC_except_table13281
- GCC_except_table13286
- GCC_except_table13289
- GCC_except_table13349
- GCC_except_table1335
- GCC_except_table13434
- GCC_except_table13444
- GCC_except_table13505
- GCC_except_table13508
- GCC_except_table13528
- GCC_except_table13530
- GCC_except_table13531
- GCC_except_table1486
- GCC_except_table1509
- GCC_except_table1577
- GCC_except_table1632
- GCC_except_table1635
- GCC_except_table1653
- GCC_except_table1720
- GCC_except_table1722
- GCC_except_table1815
- GCC_except_table1884
- GCC_except_table1887
- GCC_except_table1959
- GCC_except_table2045
- GCC_except_table2046
- GCC_except_table2095
- GCC_except_table2298
- GCC_except_table2301
- GCC_except_table2304
- GCC_except_table2309
- GCC_except_table2313
- GCC_except_table2322
- GCC_except_table2335
- GCC_except_table2337
- GCC_except_table2338
- GCC_except_table2343
- GCC_except_table2344
- GCC_except_table2345
- GCC_except_table2346
- GCC_except_table2761
- GCC_except_table2766
- GCC_except_table2792
- GCC_except_table2795
- GCC_except_table2808
- GCC_except_table2845
- GCC_except_table2861
- GCC_except_table2889
- GCC_except_table2891
- GCC_except_table2893
- GCC_except_table2895
- GCC_except_table3056
- GCC_except_table3074
- GCC_except_table3075
- GCC_except_table3121
- GCC_except_table3123
- GCC_except_table3147
- GCC_except_table3149
- GCC_except_table3152
- GCC_except_table3153
- GCC_except_table3187
- GCC_except_table3189
- GCC_except_table3196
- GCC_except_table3197
- GCC_except_table3198
- GCC_except_table3200
- GCC_except_table3201
- GCC_except_table3202
- GCC_except_table3204
- GCC_except_table3263
- GCC_except_table3286
- GCC_except_table3289
- GCC_except_table3292
- GCC_except_table3295
- GCC_except_table3298
- GCC_except_table3301
- GCC_except_table3304
- GCC_except_table3369
- GCC_except_table3370
- GCC_except_table3416
- GCC_except_table3423
- GCC_except_table3424
- GCC_except_table3428
- GCC_except_table3429
- GCC_except_table3430
- GCC_except_table3432
- GCC_except_table3440
- GCC_except_table3462
- GCC_except_table3469
- GCC_except_table3473
- GCC_except_table3476
- GCC_except_table3520
- GCC_except_table3524
- GCC_except_table3528
- GCC_except_table3533
- GCC_except_table3541
- GCC_except_table3545
- GCC_except_table3554
- GCC_except_table3556
- GCC_except_table3795
- GCC_except_table3799
- GCC_except_table3803
- GCC_except_table3806
- GCC_except_table3810
- GCC_except_table3811
- GCC_except_table3814
- GCC_except_table3820
- GCC_except_table3824
- GCC_except_table3828
- GCC_except_table3853
- GCC_except_table3858
- GCC_except_table3861
- GCC_except_table3864
- GCC_except_table3944
- GCC_except_table3958
- GCC_except_table3961
- GCC_except_table3963
- GCC_except_table3966
- GCC_except_table3973
- GCC_except_table4026
- GCC_except_table4091
- GCC_except_table4106
- GCC_except_table4109
- GCC_except_table4202
- GCC_except_table4203
- GCC_except_table4205
- GCC_except_table4210
- GCC_except_table4214
- GCC_except_table4217
- GCC_except_table4219
- GCC_except_table4227
- GCC_except_table4474
- GCC_except_table4477
- GCC_except_table4489
- GCC_except_table4563
- GCC_except_table4607
- GCC_except_table4699
- GCC_except_table4861
- GCC_except_table4873
- GCC_except_table4875
- GCC_except_table4899
- GCC_except_table4900
- GCC_except_table4901
- GCC_except_table4902
- GCC_except_table4967
- GCC_except_table5096
- GCC_except_table5097
- GCC_except_table514
- GCC_except_table517
- GCC_except_table5173
- GCC_except_table519
- GCC_except_table525
- GCC_except_table527
- GCC_except_table5275
- GCC_except_table5277
- GCC_except_table528
- GCC_except_table5305
- GCC_except_table5307
- GCC_except_table5325
- GCC_except_table5371
- GCC_except_table5466
- GCC_except_table5486
- GCC_except_table5487
- GCC_except_table5488
- GCC_except_table5490
- GCC_except_table5493
- GCC_except_table5494
- GCC_except_table5496
- GCC_except_table55
- GCC_except_table57
- GCC_except_table5754
- GCC_except_table5760
- GCC_except_table5762
- GCC_except_table5772
- GCC_except_table5773
- GCC_except_table5967
- GCC_except_table5971
- GCC_except_table6044
- GCC_except_table6175
- GCC_except_table6182
- GCC_except_table6187
- GCC_except_table6372
- GCC_except_table6425
- GCC_except_table6617
- GCC_except_table6619
- GCC_except_table6626
- GCC_except_table6634
- GCC_except_table6654
- GCC_except_table6664
- GCC_except_table6667
- GCC_except_table6686
- GCC_except_table6692
- GCC_except_table6697
- GCC_except_table6702
- GCC_except_table6707
- GCC_except_table6712
- GCC_except_table6721
- GCC_except_table6777
- GCC_except_table6785
- GCC_except_table6790
- GCC_except_table6804
- GCC_except_table6809
- GCC_except_table6816
- GCC_except_table6831
- GCC_except_table6832
- GCC_except_table6834
- GCC_except_table6836
- GCC_except_table6844
- GCC_except_table685
- GCC_except_table6860
- GCC_except_table688
- GCC_except_table6894
- GCC_except_table693
- GCC_except_table6951
- GCC_except_table6955
- GCC_except_table6957
- GCC_except_table6958
- GCC_except_table696
- GCC_except_table697
- GCC_except_table7096
- GCC_except_table7103
- GCC_except_table7188
- GCC_except_table719
- GCC_except_table7219
- GCC_except_table7274
- GCC_except_table7276
- GCC_except_table7278
- GCC_except_table7302
- GCC_except_table7330
- GCC_except_table7344
- GCC_except_table736
- GCC_except_table7360
- GCC_except_table7366
- GCC_except_table7377
- GCC_except_table7379
- GCC_except_table7381
- GCC_except_table7383
- GCC_except_table7385
- GCC_except_table7387
- GCC_except_table7389
- GCC_except_table7391
- GCC_except_table7393
- GCC_except_table7395
- GCC_except_table7397
- GCC_except_table7401
- GCC_except_table7403
- GCC_except_table7405
- GCC_except_table7407
- GCC_except_table7412
- GCC_except_table7425
- GCC_except_table7426
- GCC_except_table7431
- GCC_except_table7477
- GCC_except_table7491
- GCC_except_table7509
- GCC_except_table755
- GCC_except_table7689
- GCC_except_table7952
- GCC_except_table7995
- GCC_except_table805
- GCC_except_table8055
- GCC_except_table808
- GCC_except_table809
- GCC_except_table8171
- GCC_except_table8174
- GCC_except_table8264
- GCC_except_table8283
- GCC_except_table8293
- GCC_except_table8429
- GCC_except_table8438
- GCC_except_table8451
- GCC_except_table8458
- GCC_except_table8497
- GCC_except_table8499
- GCC_except_table8527
- GCC_except_table8529
- GCC_except_table8531
- GCC_except_table8533
- GCC_except_table8540
- GCC_except_table8546
- GCC_except_table8550
- GCC_except_table8560
- GCC_except_table8652
- GCC_except_table8654
- GCC_except_table8664
- GCC_except_table8666
- GCC_except_table8668
- GCC_except_table8670
- GCC_except_table8672
- GCC_except_table8678
- GCC_except_table8682
- GCC_except_table8695
- GCC_except_table8697
- GCC_except_table8699
- GCC_except_table8701
- GCC_except_table8720
- GCC_except_table875
- GCC_except_table879
- GCC_except_table880
- GCC_except_table881
- GCC_except_table882
- GCC_except_table883
- GCC_except_table884
- GCC_except_table886
- GCC_except_table8877
- GCC_except_table8879
- GCC_except_table8880
- GCC_except_table8881
- GCC_except_table8883
- GCC_except_table8885
- GCC_except_table8886
- GCC_except_table8887
- GCC_except_table8922
- GCC_except_table8925
- GCC_except_table8926
- GCC_except_table8929
- GCC_except_table893
- GCC_except_table8932
- GCC_except_table8933
- GCC_except_table894
- GCC_except_table8976
- GCC_except_table8977
- GCC_except_table8978
- GCC_except_table8985
- GCC_except_table8986
- GCC_except_table8988
- GCC_except_table9007
- GCC_except_table9079
- GCC_except_table9080
- GCC_except_table9081
- GCC_except_table9118
- GCC_except_table9302
- GCC_except_table9303
- GCC_except_table9304
- GCC_except_table9308
- GCC_except_table9363
- GCC_except_table9384
- GCC_except_table9460
- GCC_except_table9462
- GCC_except_table9464
- GCC_except_table9466
- GCC_except_table9474
- GCC_except_table9521
- GCC_except_table9535
- GCC_except_table9551
- GCC_except_table9579
- GCC_except_table9753
- GCC_except_table9755
- GCC_except_table9757
- GCC_except_table9801
- GCC_except_table9802
- GCC_except_table9837
- GCC_except_table9870
- GCC_except_table9873
- GCC_except_table9876
- GCC_except_table9878
- GCC_except_table9939
- GCC_except_table9959
- GCC_except_table9960
- GCC_except_table9961
- _CoreAnalyticsLibraryCore.frameworkLibrary.40535
- _CoreHAPLibraryCore.frameworkLibrary.32831
- _HMDLocationAuthorizationAsString
- _HMDRegionStateString
- _IDSFoundationLibraryCore.44865
- _IDSFoundationLibraryCore.frameworkLibrary.44868
- _OBJC_IVAR_$_HMCHIPVendorMetadataVendor._appBundleID
- _OBJC_IVAR_$_HMCHIPVendorMetadataVendor._appStoreID
- _OBJC_IVAR_$_HMCharacteristic._context
- _UIKitLibrary.45096
- _UIKitLibraryCore.45092
- _UIKitLibraryCore.frameworkLibrary.45105
- __OBJC_$_CLASS_METHODS_HMHome(HomeKit|HomeKit1|AccessCode|WalletInternal|Wallet|Light|ThreadResidentCommissioning|HMAccessory|HMRoom|HMZone|HMServiceGroup|HMUser|HMActionSet|HMTrigger|RemoteAccess|HMSoftwareUpdate|HMMediaProfile|NetworkRouter|HMUserActionPredictions|ThreadManagement|HMHomeHub|HomeNetworkInfo|HomeLocationFeedback|MediaGroupReadinessCheck|HomeActivityState|ResidentSelection|HMModernMessaging|HMModernMessagingInternal|Trigger|Climate|SiriEndpointProfilesMessengerFactory|HMActionExecution|Person|Person_Internal|Matter|CHIP|AutomationBuilders|Biome)
- __OBJC_$_INSTANCE_METHODS_HMHome(HomeKit|HomeKit1|AccessCode|WalletInternal|Wallet|Light|ThreadResidentCommissioning|HMAccessory|HMRoom|HMZone|HMServiceGroup|HMUser|HMActionSet|HMTrigger|RemoteAccess|HMSoftwareUpdate|HMMediaProfile|NetworkRouter|HMUserActionPredictions|ThreadManagement|HMHomeHub|HomeNetworkInfo|HomeLocationFeedback|MediaGroupReadinessCheck|HomeActivityState|ResidentSelection|HMModernMessaging|HMModernMessagingInternal|Trigger|Climate|SiriEndpointProfilesMessengerFactory|HMActionExecution|Person|Person_Internal|Matter|CHIP|AutomationBuilders|Biome)
- __OBJC_$_PROP_LIST_HMApplicationData.13109
- __OBJC_$_PROP_LIST_HMMediaDestination.265
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HMObjectMerge
- __OBJC_CLASS_PROTOCOLS_$_HMHome(HomeKit|HomeKit1|AccessCode|WalletInternal|Wallet|Light|ThreadResidentCommissioning|HMAccessory|HMRoom|HMZone|HMServiceGroup|HMUser|HMActionSet|HMTrigger|RemoteAccess|HMSoftwareUpdate|HMMediaProfile|NetworkRouter|HMUserActionPredictions|ThreadManagement|HMHomeHub|HomeNetworkInfo|HomeLocationFeedback|MediaGroupReadinessCheck|HomeActivityState|ResidentSelection|HMModernMessaging|HMModernMessagingInternal|Trigger|Climate|SiriEndpointProfilesMessengerFactory|HMActionExecution|Person|Person_Internal|Matter|CHIP|AutomationBuilders|Biome)
- ___102-[HMHome(HMModernMessaging) unregisterModernMessagingRequestHandlerWithMessageName:completionHandler:]_block_invoke.2284
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.786
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.788
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.789
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.792
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.796
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.791
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.794
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.797
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_3.795
- ___122-[HMHome(MediaGroupReadinessCheck) performMediaGroupReadinessCheckForAccessory:timeout:setupSessionIdentifier:completion:]_block_invoke.2239
- ___123-[HMHome(HMModernMessaging) registerModernMessagingRequestHandlerWithMessageName:options:requestHandler:completionHandler:]_block_invoke.2283
- ___140-[HMHome(HMModernMessaging) sendModernMessagingRequestWithMessageName:destination:requestPayload:options:responseHandler:completionHandler:]_block_invoke.2286
- ___22-[HMHome _mergeRooms:]_block_invoke.985
- ___22-[HMHome _mergeRooms:]_block_invoke.987
- ___22-[HMHome _mergeRooms:]_block_invoke_2.989
- ___22-[HMHome _mergeRooms:]_block_invoke_3.990
- ___22-[HMHome _mergeUsers:]_block_invoke.1031
- ___22-[HMHome _mergeUsers:]_block_invoke.1033
- ___22-[HMHome _mergeUsers:]_block_invoke_2.1035
- ___22-[HMHome _mergeUsers:]_block_invoke_3.1036
- ___22-[HMHome _mergeZones:]_block_invoke.993
- ___22-[HMHome _mergeZones:]_block_invoke.995
- ___22-[HMHome _mergeZones:]_block_invoke_2.997
- ___22-[HMHome _mergeZones:]_block_invoke_3.998
- ___25-[HMHome _mergeTriggers:]_block_invoke.1026
- ___25-[HMHome _mergeTriggers:]_block_invoke.1028
- ___25-[HMXPCClient connection]_block_invoke.78
- ___25-[HMXPCClient connection]_block_invoke.79
- ___27-[HMHome _mergeActionSets:]_block_invoke.1018
- ___27-[HMHome _mergeActionSets:]_block_invoke.1020
- ___27-[HMHome _mergeActionSets:]_block_invoke_2.1022
- ___27-[HMHome _mergeActionSets:]_block_invoke_3.1023
- ___28-[HMHome _mergeAccessories:]_block_invoke.1001
- ___28-[HMHome _mergeAccessories:]_block_invoke.1004
- ___28-[HMHome _mergeAccessories:]_block_invoke.1006
- ___28-[HMHome _mergeAccessories:]_block_invoke_2.1007
- ___29-[HMHome mergeFromNewObject:]_block_invoke.732
- ___29-[HMHome mergeFromNewObject:]_block_invoke.736
- ___29-[HMHome mergeFromNewObject:]_block_invoke.740
- ___29-[HMHome mergeFromNewObject:]_block_invoke.744
- ___29-[HMHome mergeFromNewObject:]_block_invoke.746
- ___29-[HMHome mergeFromNewObject:]_block_invoke.750
- ___29-[HMHome mergeFromNewObject:]_block_invoke.754
- ___29-[HMHome mergeFromNewObject:]_block_invoke.766
- ___29-[HMHome mergeFromNewObject:]_block_invoke.770
- ___29-[HMHome mergeFromNewObject:]_block_invoke.774
- ___29-[HMHome mergeFromNewObject:]_block_invoke.778
- ___29-[HMHome mergeFromNewObject:]_block_invoke.782
- ___29-[HMHome mergeFromNewObject:]_block_invoke.938
- ___29-[HMHome mergeFromNewObject:]_block_invoke.947
- ___29-[HMHome mergeFromNewObject:]_block_invoke.950
- ___29-[HMHome mergeFromNewObject:]_block_invoke.958
- ___29-[HMHome mergeFromNewObject:]_block_invoke.961
- ___29-[HMHome mergeFromNewObject:]_block_invoke.964
- ___29-[HMHome mergeFromNewObject:]_block_invoke.967
- ___29-[HMHome mergeFromNewObject:]_block_invoke.969
- ___29-[HMHome mergeFromNewObject:]_block_invoke.972
- ___29-[HMHome mergeFromNewObject:]_block_invoke.975
- ___29-[HMHome mergeFromNewObject:]_block_invoke.978
- ___29-[HMHome mergeFromNewObject:]_block_invoke.981
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.733
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.737
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.741
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.745
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.747
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.751
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.755
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.767
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.771
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.775
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.779
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.783
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.939
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.948
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.951
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.959
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.962
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.965
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.968
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.971
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.974
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.977
- ___29-[HMHome mergeFromNewObject:]_block_invoke_3.953
- ___29-[HMHome mergeFromNewObject:]_block_invoke_4.954
- ___29-[HMHome mergeFromNewObject:]_block_invoke_5.955
- ___29-[HMHome mergeFromNewObject:]_block_invoke_6.956
- ___30-[HMHome _mergeServiceGroups:]_block_invoke.1010
- ___30-[HMHome _mergeServiceGroups:]_block_invoke.1012
- ___30-[HMHome _mergeServiceGroups:]_block_invoke_2.1014
- ___30-[HMHome _mergeServiceGroups:]_block_invoke_3.1015
- ___32-[HMHome _mergeResidentDevices:]_block_invoke.1039
- ___32-[HMHome _mergeResidentDevices:]_block_invoke.1041
- ___32-[HMHome _mergeResidentDevices:]_block_invoke_2.1043
- ___32-[HMHome _mergeResidentDevices:]_block_invoke_3.1044
- ___36-[HMHome _mergeOutgoingInvitations:]_block_invoke.1046
- ___36-[HMHome _mergeOutgoingInvitations:]_block_invoke.1048
- ___38-[HMHomeManager _updateDataSyncState:]_block_invoke.528
- ___39-[HMHome _mergeTriggerOwnedActionSets:]_block_invoke.1024
- ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.800
- ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.802
- ___41-[HMHome mergeFromNewObjectNoMergeCount:]_block_invoke
- ___41-[HMHome mergeFromNewObjectNoMergeCount:]_block_invoke_2
- ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke.1053
- ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke.1055
- ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke_2.1054
- ___45-[HMXPCClient sendMessage:completionHandler:]_block_invoke.87
- ___45-[HMXPCClient sendMessage:completionHandler:]_block_invoke.88
- ___46-[HMHomeManager removeHome:completionHandler:]_block_invoke.641
- ___47-[HMHomeManager _recomputeAssistantIdentifiers]_block_invoke.710
- ___51-[HMHomeManager _updatePrimaryHome:notifyDelegate:]_block_invoke.767
- ___51-[HMHomeManager addHomeWithName:completionHandler:]_block_invoke.637
- ___52-[HMHome(HMUser) _manageUsersWithCompletionHandler:]_block_invoke.2060
- ___54-[HMHomeManager _refreshBeforeDate:completionHandler:]_block_invoke.623
- ___54-[HMHomeManager _refreshBeforeDate:completionHandler:]_block_invoke.624
- ___57-[HMObjectMergeCollection mergeCommonObjectsNoMergeCount]_block_invoke
- ___59-[HMHome(HMModernMessagingInternal) reRegisterHMMMHandlers]_block_invoke.2295
- ___59-[HMHome(HomeActivityState) fetchCurrentHomeActivityState:]_block_invoke.2246
- ___62-[HMOutgoingHomeInvitation _mergeWithNewAccessoryInvitations:]_block_invoke.132
- ___64-[HMHome(HMMediaProfile) updateMediaPassword:completionHandler:]_block_invoke.2138
- ___64-[HMHome(HomeNetworkInfo) fetchWiFiInfosWithTimeout:completion:]_block_invoke.2226
- ___64-[HMHome(HomeNetworkInfo) fetchWiFiInfosWithTimeout:completion:]_block_invoke_2.2227
- ___67-[HMHomeManager requestLogEventDailySchedulerStatusWithCompletion:]_block_invoke
- ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.728
- ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.732
- ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.734
- ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.736
- ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke_2.737
- ___69-[HMHomeManager addAndSetupAccessoriesWithPayload:completionHandler:]_block_invoke.859
- ___71-[HMHome(HomeActivityState) changeHomeActivityState:completionHandler:]_block_invoke.2245
- ___71-[HMHome(HomeNetworkInfo) getPrimaryResidentNetworkInfoWithCompletion:]_block_invoke.2224
- ___71-[HMHome(HomeNetworkInfo) getPrimaryResidentNetworkInfoWithCompletion:]_block_invoke_2.2225
- ___74-[HMHome(HomeNetworkInfo) fetchNetworkInfosFromTarget:timeout:completion:]_block_invoke.2228
- ___74-[HMHome(HomeNetworkInfo) fetchNetworkInfosFromTarget:timeout:completion:]_block_invoke_2.2229
- ___74-[HMHome(Trigger) fetchTriggerNameForTriggerIdentifier:completionHandler:]_block_invoke.2300
- ___74-[HMHome(Trigger) fetchTriggerNameForTriggerIdentifier:completionHandler:]_block_invoke_2.2301
- ___74-[HMHomeManager __processSyncResponse:refreshRequested:completionHandler:]_block_invoke.707
- ___75-[HMHome(HMAccessory) addAndSetupAccessoriesWithPayload:completionHandler:]_block_invoke.1921
- ___78-[HMHome(HomeActivityState) cancelHomeActivityStateHoldWithCompletionHandler:]_block_invoke.2249
- ___88-[HMHome(HMAccessory) addAccessoryWithAccessorySetupPayload:progress:completionHandler:]_block_invoke.1932
- ___88-[HMHome(HMAccessory) addAndSetUpNewAccessoriesWithSuggestedRoomName:completionHandler:]_block_invoke.1923
- ___88-[HMHome(HomeLocationFeedback) retrieveHomeKitLocationForFeedbackWithCompletionHandler:]_block_invoke.2236
- ___89-[HMHome(NetworkRouter) updateAccessoryNetworkProtectionGroup:protectionMode:completion:]_block_invoke.2193
- ___Block_byref_object_copy_.16350
- ___Block_byref_object_copy_.16684
- ___Block_byref_object_copy_.24314
- ___Block_byref_object_copy_.26660
- ___Block_byref_object_copy_.31290
- ___Block_byref_object_copy_.32932
- ___Block_byref_object_copy_.35110
- ___Block_byref_object_copy_.40422
- ___Block_byref_object_copy_.43893
- ___Block_byref_object_copy_.63700
- ___Block_byref_object_copy_.66062
- ___Block_byref_object_dispose_.16351
- ___Block_byref_object_dispose_.16685
- ___Block_byref_object_dispose_.24315
- ___Block_byref_object_dispose_.26661
- ___Block_byref_object_dispose_.31291
- ___Block_byref_object_dispose_.32933
- ___Block_byref_object_dispose_.35111
- ___Block_byref_object_dispose_.40423
- ___Block_byref_object_dispose_.43894
- ___Block_byref_object_dispose_.63701
- ___Block_byref_object_dispose_.66063
- ___CoreAnalyticsLibraryCore_block_invoke.40536
- ___CoreHAPLibraryCore_block_invoke.32832
- ___IDSFoundationLibraryCore_block_invoke.44869
- ___UIKitLibraryCore_block_invoke.45106
- ___block_descriptor_32_e34_v32?0"HMObjectMergePair"8Q16^B24l
- ___block_literal_global.10
- ___block_literal_global.101.40543
- ___block_literal_global.101.42737
- ___block_literal_global.10427
- ___block_literal_global.1061
- ___block_literal_global.10701
- ___block_literal_global.11289
- ___block_literal_global.12.51280
- ___block_literal_global.12003
- ___block_literal_global.13041
- ___block_literal_global.13162
- ___block_literal_global.14143
- ___block_literal_global.14284
- ___block_literal_global.14359
- ___block_literal_global.1453
- ___block_literal_global.14606
- ___block_literal_global.14980
- ___block_literal_global.15208
- ___block_literal_global.15796
- ___block_literal_global.16147
- ___block_literal_global.16436
- ___block_literal_global.17.19927
- ___block_literal_global.17066
- ___block_literal_global.18274
- ___block_literal_global.18810
- ___block_literal_global.18991
- ___block_literal_global.19.16132
- ___block_literal_global.19124
- ___block_literal_global.19283
- ___block_literal_global.1940
- ___block_literal_global.1971
- ___block_literal_global.19934
- ___block_literal_global.2059
- ___block_literal_global.20603
- ___block_literal_global.21068
- ___block_literal_global.2135
- ___block_literal_global.21707
- ___block_literal_global.22074
- ___block_literal_global.23046
- ___block_literal_global.23352
- ___block_literal_global.23686
- ___block_literal_global.24352
- ___block_literal_global.24541
- ___block_literal_global.24739
- ___block_literal_global.2492
- ___block_literal_global.25267
- ___block_literal_global.25511
- ___block_literal_global.25886
- ___block_literal_global.26024
- ___block_literal_global.26271
- ___block_literal_global.26518
- ___block_literal_global.26685
- ___block_literal_global.267
- ___block_literal_global.26778
- ___block_literal_global.27508
- ___block_literal_global.29425
- ___block_literal_global.29584
- ___block_literal_global.29862
- ___block_literal_global.30.19916
- ___block_literal_global.31137
- ___block_literal_global.31408
- ___block_literal_global.31747
- ___block_literal_global.32006
- ___block_literal_global.32292
- ___block_literal_global.32372
- ___block_literal_global.33.65399
- ___block_literal_global.33076
- ___block_literal_global.33572
- ___block_literal_global.33844
- ___block_literal_global.34896
- ___block_literal_global.35133
- ___block_literal_global.35435
- ___block_literal_global.36751
- ___block_literal_global.37724
- ___block_literal_global.37958
- ___block_literal_global.38187
- ___block_literal_global.38583
- ___block_literal_global.39333
- ___block_literal_global.3955
- ___block_literal_global.40530
- ___block_literal_global.40780
- ___block_literal_global.41119
- ___block_literal_global.41785
- ___block_literal_global.42747
- ___block_literal_global.4293
- ___block_literal_global.43011
- ___block_literal_global.43280
- ___block_literal_global.43565
- ___block_literal_global.43785
- ___block_literal_global.4380
- ___block_literal_global.4472
- ___block_literal_global.44930
- ___block_literal_global.45024
- ___block_literal_global.45731
- ___block_literal_global.45923
- ___block_literal_global.47106
- ___block_literal_global.475
- ___block_literal_global.47548
- ___block_literal_global.47874
- ___block_literal_global.48640
- ___block_literal_global.49297
- ___block_literal_global.49655
- ___block_literal_global.50929
- ___block_literal_global.51292
- ___block_literal_global.514
- ___block_literal_global.51576
- ___block_literal_global.51772
- ___block_literal_global.52002
- ___block_literal_global.52719
- ___block_literal_global.52839
- ___block_literal_global.5333
- ___block_literal_global.53594
- ___block_literal_global.53828
- ___block_literal_global.54283
- ___block_literal_global.54544
- ___block_literal_global.55626
- ___block_literal_global.57918
- ___block_literal_global.58.37953
- ___block_literal_global.58782
- ___block_literal_global.5924
- ___block_literal_global.60072
- ___block_literal_global.60803
- ___block_literal_global.61358
- ___block_literal_global.61669
- ___block_literal_global.62186
- ___block_literal_global.62363
- ___block_literal_global.62753
- ___block_literal_global.63001
- ___block_literal_global.6337
- ___block_literal_global.6474
- ___block_literal_global.64802
- ___block_literal_global.65138
- ___block_literal_global.65405
- ___block_literal_global.65763
- ___block_literal_global.66001
- ___block_literal_global.66357
- ___block_literal_global.6704
- ___block_literal_global.7.24552
- ___block_literal_global.701
- ___block_literal_global.7192
- ___block_literal_global.73.24712
- ___block_literal_global.749
- ___block_literal_global.751
- ___block_literal_global.7559
- ___block_literal_global.756
- ___block_literal_global.7891
- ___block_literal_global.8149
- ___block_literal_global.84.40724
- ___block_literal_global.8733
- ___block_literal_global.8973
- ___block_literal_global.9375
- ___block_literal_global.9991
- ___getAnalyticsSendEventLazySymbolLoc_block_invoke.40533
- ___getNSCharacterEncodingDocumentAttributeSymbolLoc_block_invoke.45101
- ___getNSDocumentTypeDocumentAttributeSymbolLoc_block_invoke.45095
- _audit_stringCoreAnalytics.40539
- _audit_stringCoreHAP.32834
- _audit_stringIDSFoundation.44871
- _audit_stringUIKit.45108
- _getAnalyticsSendEventLazySymbolLoc.ptr.40532
- _getNSCharacterEncodingDocumentAttributeSymbolLoc.ptr.45100
- _getNSDocumentTypeDocumentAttributeSymbolLoc.ptr.45094
- _logCategory._hmf_once_t0.14358
- _logCategory._hmf_once_t0.23351
- _logCategory._hmf_once_t0.24738
- _logCategory._hmf_once_t0.32005
- _logCategory._hmf_once_t0.32371
- _logCategory._hmf_once_t0.43564
- _logCategory._hmf_once_t0.45730
- _logCategory._hmf_once_t0.45922
- _logCategory._hmf_once_t0.63000
- _logCategory._hmf_once_t1.19123
- _logCategory._hmf_once_t1.21067
- _logCategory._hmf_once_t1.40756
- _logCategory._hmf_once_t1.47105
- _logCategory._hmf_once_t1.51279
- _logCategory._hmf_once_t1.52838
- _logCategory._hmf_once_t1.57917
- _logCategory._hmf_once_t11.13040
- _logCategory._hmf_once_t13.42736
- _logCategory._hmf_once_t14.62752
- _logCategory._hmf_once_t16.31407
- _logCategory._hmf_once_t16.37957
- _logCategory._hmf_once_t16.64801
- _logCategory._hmf_once_t2.24551
- _logCategory._hmf_once_t2.26684
- _logCategory._hmf_once_t2.29861
- _logCategory._hmf_once_t2.33571
- _logCategory._hmf_once_t20.25279
- _logCategory._hmf_once_t20.26270
- _logCategory._hmf_once_t21.62362
- _logCategory._hmf_once_t24.41118
- _logCategory._hmf_once_t24.41784
- _logCategory._hmf_once_t25.26517
- _logCategory._hmf_once_t25.65762
- _logCategory._hmf_once_t27.61668
- _logCategory._hmf_once_t3.43010
- _logCategory._hmf_once_t3.53817
- _logCategory._hmf_once_t3.65398
- _logCategory._hmf_once_t31.24351
- _logCategory._hmf_once_t31.54282
- _logCategory._hmf_once_t31.66356
- _logCategory._hmf_once_t32.53593
- _logCategory._hmf_once_t34.20602
- _logCategory._hmf_once_t366
- _logCategory._hmf_once_t37.54570
- _logCategory._hmf_once_t4.14605
- _logCategory._hmf_once_t4.1464
- _logCategory._hmf_once_t4.6336
- _logCategory._hmf_once_t44.26540
- _logCategory._hmf_once_t44.32291
- _logCategory._hmf_once_t5.18809
- _logCategory._hmf_once_t51.43279
- _logCategory._hmf_once_t6.34895
- _logCategory._hmf_once_t6.37723
- _logCategory._hmf_once_t6.43784
- _logCategory._hmf_once_t6.49296
- _logCategory._hmf_once_t6.58781
- _logCategory._hmf_once_t7.52718
- _logCategory._hmf_once_t8.38186
- _logCategory._hmf_once_t8.48639
- _logCategory._hmf_once_t8.51790
- _logCategory._hmf_once_t9.29583
- _logCategory._hmf_once_v1.14360
- _logCategory._hmf_once_v1.23353
- _logCategory._hmf_once_v1.24740
- _logCategory._hmf_once_v1.32007
- _logCategory._hmf_once_v1.32373
- _logCategory._hmf_once_v1.43566
- _logCategory._hmf_once_v1.45732
- _logCategory._hmf_once_v1.45924
- _logCategory._hmf_once_v1.63002
- _logCategory._hmf_once_v10.29585
- _logCategory._hmf_once_v12.13042
- _logCategory._hmf_once_v14.42738
- _logCategory._hmf_once_v15.62754
- _logCategory._hmf_once_v17.31409
- _logCategory._hmf_once_v17.37959
- _logCategory._hmf_once_v17.64803
- _logCategory._hmf_once_v2.19125
- _logCategory._hmf_once_v2.21069
- _logCategory._hmf_once_v2.40757
- _logCategory._hmf_once_v2.47107
- _logCategory._hmf_once_v2.51281
- _logCategory._hmf_once_v2.52840
- _logCategory._hmf_once_v2.57919
- _logCategory._hmf_once_v21.25280
- _logCategory._hmf_once_v21.26272
- _logCategory._hmf_once_v22.62364
- _logCategory._hmf_once_v25.41120
- _logCategory._hmf_once_v25.41786
- _logCategory._hmf_once_v26.26519
- _logCategory._hmf_once_v26.65764
- _logCategory._hmf_once_v28.61670
- _logCategory._hmf_once_v3.24553
- _logCategory._hmf_once_v3.26686
- _logCategory._hmf_once_v3.29863
- _logCategory._hmf_once_v3.33573
- _logCategory._hmf_once_v32.24353
- _logCategory._hmf_once_v32.54284
- _logCategory._hmf_once_v32.66358
- _logCategory._hmf_once_v33.53595
- _logCategory._hmf_once_v35.20604
- _logCategory._hmf_once_v367
- _logCategory._hmf_once_v38.54571
- _logCategory._hmf_once_v4.43012
- _logCategory._hmf_once_v4.53818
- _logCategory._hmf_once_v4.65400
- _logCategory._hmf_once_v45.26541
- _logCategory._hmf_once_v45.32293
- _logCategory._hmf_once_v5.14607
- _logCategory._hmf_once_v5.1465
- _logCategory._hmf_once_v5.6338
- _logCategory._hmf_once_v52.43281
- _logCategory._hmf_once_v6.18811
- _logCategory._hmf_once_v7.34897
- _logCategory._hmf_once_v7.37725
- _logCategory._hmf_once_v7.43786
- _logCategory._hmf_once_v7.49298
- _logCategory._hmf_once_v7.58783
- _logCategory._hmf_once_v8.52720
- _logCategory._hmf_once_v9.38188
- _logCategory._hmf_once_v9.48641
- _logCategory._hmf_once_v9.51791
- _objc_msgSend$initWithIdentifier:name:appStoreID:appBundleID:
- _objc_msgSend$mergeCommonObjectsNoMergeCount
- _objc_msgSend$mergeFromNewObjectNoMergeCount:
- _objc_msgSend$payloadForDestination:options:
- _objc_msgSend$payloadForNullDestination
- _sharedInstance.onceToken.42746
- _sharedManager.onceToken.61815
- _supportedValueClasses.onceToken.51575
- _supportedValueClasses.onceToken.60034
- _supportedValueClasses.supportedValueClasses.51577
- _supportedValueClasses.supportedValueClasses.60035
CStrings:
+ "%@%@%@%@%@%@%@%@%@%@"
+ "%{public}@Adapter did receive setting update: accessory: %@ settings (count): %@"
+ "%{public}@Adapter did receive setting update: media system: %@ settings (count): %@"
+ "%{public}@Fetching vendor model entry responded with error: %@"
+ "%{public}@Fetching vendor model entry response payload is invalid"
+ "%{public}@Missing selected language: %@ or available language settings (count): %@"
+ "%{public}@Modified language list (count):%@, error:%@, delegate:%@"
+ "%{public}@No accessory for identifier %@ for biome query for characteristic type %@ service type %@"
+ "%{public}@Notifying client of did receive settings updates for accessory with identifier: %@ settings count: %@ delegate: %@"
+ "%{public}@[HMMediaDestinationControllerRequestMessagePayload] Failed to convert to internal destination for destination: %@"
+ "%{public}@[HMMediaDestinationControllerRequestMessagePayload] Failed to get destination identifier with options: %@ destination: %@"
+ "%{public}@[HMMediaDestinationControllerRequestMessagePayload] Failed to get update options from payload: %@"
+ "%{public}@kFetchVendorModelEntryForManufacturerRequestKey received a response: %@, error: %@"
+ "%{public}@kFetchVendorModelEntryForProductDataRequestKey received a response: %@, error: %@"
+ "%{public}@kFetchVendorModelEntryForProductDataRequestKey response payload is invalid"
+ "%{public}@kFetchVendorModelEntryForProductDataRequestKey was responded with error: %@"
+ "%{public}@vendorModelEntryFromDictionaryRepresentation cannot build object from dictionary %@"
+ "-[HMHome(PowerAssertionInfo) fetchPowerAssertionInfo:]"
+ "-[HMVendorDataStore fetchVendorModelEntryForManufacturer:model:completion:]"
+ "-[HMVendorDataStore fetchVendorModelEntryForProductData:completion:]"
+ "< %@%@%@%@%@>"
+ "@\"HMMediaGroupProtoSurroundSystemRoles\""
+ "Activity history is only supported in HH2 mode"
+ "App Bundle ID"
+ "App Store ID"
+ "Failed to clear EnergyKit data"
+ "Firmware Version"
+ "FirmwareVersion"
+ "HM.FetchPowerAssertionsMessage"
+ "HMHM.homeUpdateRequired"
+ "HMLocationAuthorizationAllowed"
+ "HMLocationAuthorizationNotAllowed"
+ "HMLocationAuthorizationUnknown"
+ "HMMediaDestinationControllerRequestMessagePayload"
+ "HMMediaGroupProtoSurroundSystemRoles"
+ "HMRegionStateInside"
+ "HMRegionStateOutside"
+ "HMRegionStateUnknown"
+ "HMVendorDataStore"
+ "HMVendorModelEntry"
+ "HO"
+ "Homes Only"
+ "IOPMPowerAssertionBoolKey"
+ "Manufacturer"
+ "Model"
+ "PowerAssertionInfo"
+ "Product Data"
+ "Product Data Alternates"
+ "ProductData"
+ "ProductDataAlternates"
+ "T@\"HMMediaGroupProtoSurroundSystemRoles\",&,N,V_surroundSystem"
+ "T@\"NSArray\",R,C,V_productDataAlternates"
+ "T@\"NSString\",&,N,V_frontLeftDestinationIdentifier"
+ "T@\"NSString\",&,N,V_frontRightDestinationIdentifier"
+ "T@\"NSString\",&,N,V_rearLeftDestinationIdentifier"
+ "T@\"NSString\",&,N,V_rearRightDestinationIdentifier"
+ "T@\"NSString\",&,N,V_reason"
+ "T@\"NSString\",R,C,V_firmwareVersion"
+ "T@\"NSString\",R,C,V_manufacturer"
+ "T@\"NSString\",R,C,V_model"
+ "T@\"NSString\",R,C,V_productData"
+ "T@\"NSUUID\",R,C,V_destinationIdentifier"
+ "T@\"_HMContext\",R,N"
+ "TB,N,V_mapIsValid"
+ "TB,N,V_modelHasSignificantData"
+ "TQ,R,V_updateOptions"
+ "Td,N,V_legacyScore"
+ "UAP"
+ "User Action Predictions"
+ "VendorDataStore"
+ "_frontLeftDestinationIdentifier"
+ "_frontRightDestinationIdentifier"
+ "_legacyScore"
+ "_mapIsValid"
+ "_modelHasSignificantData"
+ "_productData"
+ "_productDataAlternates"
+ "_rearLeftDestinationIdentifier"
+ "_rearRightDestinationIdentifier"
+ "_surroundSystem"
+ "_updateOptions"
+ "exceeded"
+ "fetchPowerAssertionInfo:"
+ "fetchVendorModelEntryForManufacturer:model:completion:"
+ "fetchVendorModelEntryForProductData:completion:"
+ "frontLeftDestinationIdentifier"
+ "frontRightDestinationIdentifier"
+ "hasFrontLeftDestinationIdentifier"
+ "hasFrontRightDestinationIdentifier"
+ "hasLegacyScore"
+ "hasMapIsValid"
+ "hasModelHasSignificantData"
+ "hasRearLeftDestinationIdentifier"
+ "hasRearRightDestinationIdentifier"
+ "hasSurroundSystem"
+ "hm_locationAuthorizationFromCLAuthorizationStatus:"
+ "hm_regionStateFromCLRegionState:"
+ "initWithDestination:options:"
+ "initWithDestinationIdentifier:updateOptions:"
+ "initWithManufacturer:model:appBundleID:appStoreID:firmwareVersion:productData:productDataAlternates:"
+ "initWithNoDestination"
+ "kFetchVendorModelEntryForManufacturerRequestKey"
+ "kFetchVendorModelEntryForProductDataRequestKey"
+ "kManufacturerKey"
+ "kModelKey"
+ "kProductDataKey"
+ "kVendorModelEntryDictionaryKey"
+ "legacyScore"
+ "mapIsValid"
+ "modelHasSignificantData"
+ "postHH2UpdateRequiredCarPlayNotificationWithCompletion:"
+ "productData"
+ "productDataAlternates"
+ "rearLeftDestinationIdentifier"
+ "rearRightDestinationIdentifier"
+ "setFrontLeftDestinationIdentifier:"
+ "setFrontRightDestinationIdentifier:"
+ "setHasLegacyScore:"
+ "setHasMapIsValid:"
+ "setHasModelHasSignificantData:"
+ "setLegacyScore:"
+ "setMapIsValid:"
+ "setModelHasSignificantData:"
+ "setRearLeftDestinationIdentifier:"
+ "setRearRightDestinationIdentifier:"
+ "setSurroundSystem:"
+ "surroundSystem"
+ "updateOptions"
+ "updateUserInfo:responseHandler:"
+ "v32@0:8@\"NSDictionary\"16@?<v@?>24"
+ "vendorModelEntryFromDictionaryRepresentation:"
+ "{?=\"legacyScore\"b1\"score\"b1\"predictionType\"b1\"mapIsValid\"b1\"modelHasSignificantData\"b1}"
- "%@%@%@%@%@%@%@%@"
- "%{public}@Adapter did receive setting update: accessory: %@ settings: %@"
- "%{public}@Adapter did receive setting update: media system: %@ settings: %@"
- "%{public}@Failed to convert to internal destination for destination: %@"
- "%{public}@Failed to get destination identifier with options: %@ destination: %@"
- "%{public}@Missing selected language = %@ or available language settings = %@"
- "%{public}@Modified accessory setting:%@, error:%@, delegate:%@"
- "%{public}@Modified media system setting:%@, error:%@, delegate:%@"
- "%{public}@Notifying client of did receive settings updates for accessory with identifier: %@ settings: %@ delegate: %@"
- "-[HMHome mergeFromNewObjectNoMergeCount:]"
- "< %@%@%@%@>"
- "HMDLocationAuthorizationAllowed"
- "HMDLocationAuthorizationNotAllowed"
- "HMDLocationAuthorizationUnknown"
- "HMDRegionStateInside"
- "HMDRegionStateOutside"
- "HMDRegionStateUnknown"
- "Merge-Home-%@-%@"
- "hm_hmdLocationAuthorizationFromCLAuthorizationStatus:"
- "hm_hmdRegionStateFromCLRegionState:"
- "initWithIdentifier:name:appStoreID:appBundleID:"
- "logEventDailySchedulerRequestStatus"
- "mergeCommonObjectsNoMergeCount"
- "mergeFromNewObjectNoMergeCount:"
- "payloadForDestination:options:"
- "payloadForNullDestination"
- "requestLogEventDailySchedulerStatusWithCompletion:"
- "v24@0:8@\"<HMObjectMerge>\"16"
- "{?=\"score\"b1\"predictionType\"b1}"

```
