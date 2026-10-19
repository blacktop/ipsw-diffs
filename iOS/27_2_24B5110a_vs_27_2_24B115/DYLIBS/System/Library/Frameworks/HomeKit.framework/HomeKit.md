## HomeKit

> `/System/Library/Frameworks/HomeKit.framework/HomeKit`

```diff

 1520.2.7.1.3
-  __TEXT.__text: 0x48426c
-  __TEXT.__objc_methlist: 0x298e4
-  __TEXT.__const: 0x12f18
+  __TEXT.__text: 0x48e3c0
+  __TEXT.__objc_methlist: 0x2a0fc
+  __TEXT.__const: 0x12f28
   __TEXT.__dlopen_cstrs: 0x403
   __TEXT.__swift5_typeref: 0x484d
-  __TEXT.__cstring: 0x32cda
+  __TEXT.__cstring: 0x334a7
   __TEXT.__constg_swiftt: 0x4048
   __TEXT.__swift5_reflstr: 0x2cce
   __TEXT.__swift5_fieldmd: 0x3c0c

   __TEXT.__swift_as_entry: 0x2c8
   __TEXT.__swift_as_ret: 0x320
   __TEXT.__swift_as_cont: 0x698
-  __TEXT.__oslogstring: 0x5ab42
+  __TEXT.__oslogstring: 0x5ba22
   __TEXT.__swift5_mpenum: 0x20
   __TEXT.__gcc_except_tab: 0x6948
   __TEXT.__ustring: 0x50
-  __TEXT.__unwind_info: 0x13758
-  __TEXT.__eh_frame: 0xd934
+  __TEXT.__unwind_info: 0x13998
+  __TEXT.__eh_frame: 0xd96c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x95c8
-  __DATA_CONST.__objc_classlist: 0x13f8
+  __DATA_CONST.__const: 0x9660
+  __DATA_CONST.__objc_classlist: 0x1420
   __DATA_CONST.__objc_catlist: 0x108
   __DATA_CONST.__objc_protolist: 0x570
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xea10
+  __DATA_CONST.__objc_selrefs: 0xec48
   __DATA_CONST.__objc_protorefs: 0x110
-  __DATA_CONST.__objc_superrefs: 0x1000
+  __DATA_CONST.__objc_superrefs: 0x1020
   __DATA_CONST.__objc_arraydata: 0x1508
-  __DATA_CONST.__got: 0x20c8
-  __AUTH_CONST.__const: 0xbc50
-  __AUTH_CONST.__cfstring: 0x2d120
-  __AUTH_CONST.__objc_const: 0x4b808
+  __DATA_CONST.__got: 0x20f0
+  __AUTH_CONST.__const: 0xbcd0
+  __AUTH_CONST.__cfstring: 0x2d7a0
+  __AUTH_CONST.__objc_const: 0x4c350
   __AUTH_CONST.__objc_intobj: 0x9f0
   __AUTH_CONST.__objc_dictobj: 0x848
   __AUTH_CONST.__objc_arrayobj: 0x630
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__auth_got: 0x1fd0
-  __AUTH.__objc_data: 0x9600
+  __AUTH.__objc_data: 0x9790
   __AUTH.__data: 0x3ef8
-  __DATA.__objc_ivar: 0x2954
+  __DATA.__objc_ivar: 0x29b4
   __DATA.__data: 0x7cc0
   __DATA.__common: 0x1a0
   __DATA_DIRTY.__objc_data: 0x36a0
-  __DATA_DIRTY.__data: 0x1a8
+  __DATA_DIRTY.__data: 0x198
   __DATA_DIRTY.__bss: 0x2c0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 22318
-  Symbols:   29042
-  CStrings:  13066
+  Functions: 22499
+  Symbols:   29263
+  CStrings:  13165
 
Symbols:
+ +[HMCurrentMediaGroupProvider _participantRoleForSurroundSystem:destinationIdentifier:]
+ +[HMSurroundSystem derivedDestinationIdentifierForGroupIdentifier:]
+ +[HMSurroundSystem roomNameSentinel]
+ +[HMSurroundSystem supportsSecureCoding]
+ +[HMSurroundSystemConfigurationRequest logCategory]
+ +[HMSurroundSystemConfigurationRequest messageName]
+ +[HMSurroundSystemConfigurationRequest shortDescription]
+ +[HMSurroundSystemConfigurationRequestPayload logCategory]
+ +[HMSurroundSystemUpdateRolesRequest logCategory]
+ +[HMSurroundSystemUpdateRolesRequest shortDescription]
+ -[HMAccessory accessoryWithAudioDestinationIdentifier:]
+ -[HMAccessory mediaDestinationController:didGetUpdateDestinationRequestWithSurroundSystemDestination:completionHandler:]
+ -[HMAccessory setSupportsSurroundSystemFrontRoleCapability:]
+ -[HMAccessory setSupportsSurroundSystemRearRoleCapability:]
+ -[HMAccessory supportsSurroundSystemFrontRoleCapability]
+ -[HMAccessory supportsSurroundSystemFrontRole]
+ -[HMAccessory supportsSurroundSystemRearRoleCapability]
+ -[HMAccessory supportsSurroundSystemRearRole]
+ -[HMAccessoryCapabilities supportsAudioDestinationSurroundSystemFrontRole]
+ -[HMAccessoryCapabilities supportsAudioDestinationSurroundSystemRearRole]
+ -[HMAccessoryCapabilities supportsHomeTheaterSourceSurroundSystem]
+ -[HMCurrentMediaGroupProvider _mergeWithCurrentAppleTVAccessory:surroundSystemDestination:home:]
+ -[HMCurrentMediaGroupProvider _mergeWithCurrentHomePodAccessory:surroundSystem:home:]
+ -[HMCurrentMediaGroupProvider _notifyClientOfCurrentMediaGroupWithCurrentAccessory:surroundSystem:sourceAccessory:home:]
+ -[HMHome accessoryWithAudioDestinationControllerIdentifier:]
+ -[HMHome mediaGroupsController:sourceAccessoryForSurroundSystem:]
+ -[HMMediaDestination containsSurroundSystemFrontRoleSupportedOptions]
+ -[HMMediaDestination containsSurroundSystemRearRoleSupportedOptions]
+ -[HMMediaDestinationController supportsSurroundSystemDestinations]
+ -[HMMediaDestinationController updateToSurroundSystemDestination:completionHandler:]
+ -[HMMediaGroup surroundSystem]
+ -[HMMediaGroupDestination supportsSurroundSystemFrontRole]
+ -[HMMediaGroupDestination supportsSurroundSystemRearRole]
+ -[HMMediaGroupsController homeTheaterSystemForSurroundSystem:]
+ -[HMMediaGroupsController updateSurroundSystemRolesWithRequest:completion:]
+ -[HMMediaSystem supportsSurroundSystemFrontRole]
+ -[HMMediaSystem supportsSurroundSystemRearRole]
+ -[HMMutableSurroundSystem copyWithZone:]
+ -[HMProtoAccessoryCapabilities(UnobfuscatedAliases) setSupportsAudioDestinationSurroundSystemFrontRole:]
+ -[HMProtoAccessoryCapabilities(UnobfuscatedAliases) setSupportsAudioDestinationSurroundSystemRearRole:]
+ -[HMProtoAccessoryCapabilities(UnobfuscatedAliases) setSupportsHomeTheaterSourceSurroundSystem:]
+ -[HMProtoAccessoryCapabilities(UnobfuscatedAliases) supportsAudioDestinationSurroundSystemFrontRole]
+ -[HMProtoAccessoryCapabilities(UnobfuscatedAliases) supportsAudioDestinationSurroundSystemRearRole]
+ -[HMProtoAccessoryCapabilities(UnobfuscatedAliases) supportsHomeTheaterSourceSurroundSystem]
+ -[HMResidentCapabilities supportsSurroundConfiguration]
+ -[HMResidentDevice setSupportsSurroundConfiguration:]
+ -[HMResidentDevice supportsSurroundConfiguration]
+ -[HMSurroundSystem .cxx_destruct]
+ -[HMSurroundSystem destinationIdentifiers]
+ -[HMSurroundSystem destinationUniqueIdentifiers]
+ -[HMSurroundSystem encodeToProtoBufferData]
+ -[HMSurroundSystem encodeWithCoder:]
+ -[HMSurroundSystem frontLeftDestinationIdentifier]
+ -[HMSurroundSystem frontRightDestinationIdentifier]
+ -[HMSurroundSystem hash]
+ -[HMSurroundSystem hmf_appendAttributeDescriptionsToString:options:]
+ -[HMSurroundSystem initWithCoder:]
+ -[HMSurroundSystem initWithIdentifier:parentIdentifier:associatedGroupIdentifier:frontLeftDestinationIdentifier:frontRightDestinationIdentifier:rearLeftDestinationIdentifier:rearRightDestinationIdentifier:]
+ -[HMSurroundSystem initWithIdentifier:parentIdentifier:name:defaultName:associatedGroupIdentifier:frontLeftDestinationIdentifier:frontRightDestinationIdentifier:rearLeftDestinationIdentifier:rearRightDestinationIdentifier:]
+ -[HMSurroundSystem initWithProtoBufferData:]
+ -[HMSurroundSystem isEqual:]
+ -[HMSurroundSystem metricType]
+ -[HMSurroundSystem mutableCopyWithZone:]
+ -[HMSurroundSystem rearLeftDestinationIdentifier]
+ -[HMSurroundSystem rearRightDestinationIdentifier]
+ -[HMSurroundSystem setFrontLeftDestinationIdentifier:]
+ -[HMSurroundSystem setFrontRightDestinationIdentifier:]
+ -[HMSurroundSystem setRearLeftDestinationIdentifier:]
+ -[HMSurroundSystem setRearRightDestinationIdentifier:]
+ -[HMSurroundSystem shortDescription]
+ -[HMSurroundSystemConfigurationRequest .cxx_destruct]
+ -[HMSurroundSystemConfigurationRequest accessoriesInWrongRoom]
+ -[HMSurroundSystemConfigurationRequest description]
+ -[HMSurroundSystemConfigurationRequest frontLeftAccessoryUUID]
+ -[HMSurroundSystemConfigurationRequest frontLeftAccessory]
+ -[HMSurroundSystemConfigurationRequest frontRightAccessoryUUID]
+ -[HMSurroundSystemConfigurationRequest frontRightAccessory]
+ -[HMSurroundSystemConfigurationRequest hash]
+ -[HMSurroundSystemConfigurationRequest hmf_appendAttributeDescriptionsToString:options:]
+ -[HMSurroundSystemConfigurationRequest identifier]
+ -[HMSurroundSystemConfigurationRequest initWithIdentifier:sourceAccessory:frontLeftAccessory:frontRightAccessory:rearLeftAccessory:rearRightAccessory:]
+ -[HMSurroundSystemConfigurationRequest initWithSourceAccessory:frontLeftAccessory:frontRightAccessory:rearLeftAccessory:rearRightAccessory:]
+ -[HMSurroundSystemConfigurationRequest isEqual:]
+ -[HMSurroundSystemConfigurationRequest isUniqueAccessories]
+ -[HMSurroundSystemConfigurationRequest isValidAllFrontConfiguration]
+ -[HMSurroundSystemConfigurationRequest isValidAllRearConfiguration]
+ -[HMSurroundSystemConfigurationRequest isValidConfiguration]
+ -[HMSurroundSystemConfigurationRequest isValidHomePodConfiguration]
+ -[HMSurroundSystemConfigurationRequest isValidMixConfiguration]
+ -[HMSurroundSystemConfigurationRequest isValidSourceAccessory]
+ -[HMSurroundSystemConfigurationRequest messageName]
+ -[HMSurroundSystemConfigurationRequest metricType]
+ -[HMSurroundSystemConfigurationRequest payload]
+ -[HMSurroundSystemConfigurationRequest privateDescription]
+ -[HMSurroundSystemConfigurationRequest rearLeftAccessoryUUID]
+ -[HMSurroundSystemConfigurationRequest rearLeftAccessory]
+ -[HMSurroundSystemConfigurationRequest rearRightAccessoryUUID]
+ -[HMSurroundSystemConfigurationRequest rearRightAccessory]
+ -[HMSurroundSystemConfigurationRequest setFrontLeftAccessory:]
+ -[HMSurroundSystemConfigurationRequest setFrontRightAccessory:]
+ -[HMSurroundSystemConfigurationRequest setRearLeftAccessory:]
+ -[HMSurroundSystemConfigurationRequest setRearRightAccessory:]
+ -[HMSurroundSystemConfigurationRequest setSourceAccessory:]
+ -[HMSurroundSystemConfigurationRequest shortDescription]
+ -[HMSurroundSystemConfigurationRequest sourceAccessoryUUID]
+ -[HMSurroundSystemConfigurationRequest sourceAccessory]
+ -[HMSurroundSystemConfigurationRequestPayload .cxx_destruct]
+ -[HMSurroundSystemConfigurationRequestPayload frontLeftAccessoryUUID]
+ -[HMSurroundSystemConfigurationRequestPayload frontRightAccessoryUUID]
+ -[HMSurroundSystemConfigurationRequestPayload hash]
+ -[HMSurroundSystemConfigurationRequestPayload hmf_appendAttributeDescriptionsToString:options:]
+ -[HMSurroundSystemConfigurationRequestPayload identifier]
+ -[HMSurroundSystemConfigurationRequestPayload initWithIdentifier:sourceAccessoryUUID:frontLeftAccessoryUUID:frontRightAccessoryUUID:rearLeftAccessoryUUID:rearRightAccessoryUUID:]
+ -[HMSurroundSystemConfigurationRequestPayload initWithPayload:]
+ -[HMSurroundSystemConfigurationRequestPayload isEqual:]
+ -[HMSurroundSystemConfigurationRequestPayload payloadCopy]
+ -[HMSurroundSystemConfigurationRequestPayload rearLeftAccessoryUUID]
+ -[HMSurroundSystemConfigurationRequestPayload rearRightAccessoryUUID]
+ -[HMSurroundSystemConfigurationRequestPayload sourceAccessoryUUID]
+ -[HMSurroundSystemUpdateRolesRequest .cxx_destruct]
+ -[HMSurroundSystemUpdateRolesRequest configurationRequestWithSourceAccessory:]
+ -[HMSurroundSystemUpdateRolesRequest description]
+ -[HMSurroundSystemUpdateRolesRequest frontLeftAccessoryUUID]
+ -[HMSurroundSystemUpdateRolesRequest frontLeftAccessory]
+ -[HMSurroundSystemUpdateRolesRequest frontRightAccessoryUUID]
+ -[HMSurroundSystemUpdateRolesRequest frontRightAccessory]
+ -[HMSurroundSystemUpdateRolesRequest hash]
+ -[HMSurroundSystemUpdateRolesRequest hmf_appendAttributeDescriptionsToString:options:]
+ -[HMSurroundSystemUpdateRolesRequest initWithSurroundSystem:frontLeftAccessory:frontRightAccessory:rearLeftAccessory:rearRightAccessory:]
+ -[HMSurroundSystemUpdateRolesRequest isEqual:]
+ -[HMSurroundSystemUpdateRolesRequest isUniqueAccessories]
+ -[HMSurroundSystemUpdateRolesRequest isValidAllFrontConfiguration]
+ -[HMSurroundSystemUpdateRolesRequest isValidAllRearConfiguration]
+ -[HMSurroundSystemUpdateRolesRequest isValidHomePodConfiguration]
+ -[HMSurroundSystemUpdateRolesRequest isValidMixConfiguration]
+ -[HMSurroundSystemUpdateRolesRequest isValidRequest]
+ -[HMSurroundSystemUpdateRolesRequest privateDescription]
+ -[HMSurroundSystemUpdateRolesRequest rearLeftAccessoryUUID]
+ -[HMSurroundSystemUpdateRolesRequest rearLeftAccessory]
+ -[HMSurroundSystemUpdateRolesRequest rearRightAccessoryUUID]
+ -[HMSurroundSystemUpdateRolesRequest rearRightAccessory]
+ -[HMSurroundSystemUpdateRolesRequest shortDescription]
+ -[HMSurroundSystemUpdateRolesRequest surroundSystemIdentifier]
+ -[HMSurroundSystemUpdateRolesRequest surroundSystem]
+ GCC_except_table10000
+ GCC_except_table10001
+ GCC_except_table10044
+ GCC_except_table10045
+ GCC_except_table10046
+ GCC_except_table10053
+ GCC_except_table10054
+ GCC_except_table10056
+ GCC_except_table10075
+ GCC_except_table10144
+ GCC_except_table10145
+ GCC_except_table10146
+ GCC_except_table10179
+ GCC_except_table10188
+ GCC_except_table10202
+ GCC_except_table10273
+ GCC_except_table10303
+ GCC_except_table10304
+ GCC_except_table10305
+ GCC_except_table10307
+ GCC_except_table10310
+ GCC_except_table10311
+ GCC_except_table10317
+ GCC_except_table10466
+ GCC_except_table10467
+ GCC_except_table10468
+ GCC_except_table10472
+ GCC_except_table10527
+ GCC_except_table10548
+ GCC_except_table10629
+ GCC_except_table10631
+ GCC_except_table10633
+ GCC_except_table10635
+ GCC_except_table10643
+ GCC_except_table10693
+ GCC_except_table10705
+ GCC_except_table10707
+ GCC_except_table10723
+ GCC_except_table10752
+ GCC_except_table10941
+ GCC_except_table10942
+ GCC_except_table10977
+ GCC_except_table11010
+ GCC_except_table11013
+ GCC_except_table11016
+ GCC_except_table11018
+ GCC_except_table11084
+ GCC_except_table11104
+ GCC_except_table11105
+ GCC_except_table11106
+ GCC_except_table11145
+ GCC_except_table11147
+ GCC_except_table11149
+ GCC_except_table11214
+ GCC_except_table11246
+ GCC_except_table11248
+ GCC_except_table11252
+ GCC_except_table11269
+ GCC_except_table11271
+ GCC_except_table11277
+ GCC_except_table11281
+ GCC_except_table11284
+ GCC_except_table11291
+ GCC_except_table11295
+ GCC_except_table11301
+ GCC_except_table11313
+ GCC_except_table11316
+ GCC_except_table11324
+ GCC_except_table11325
+ GCC_except_table11327
+ GCC_except_table11329
+ GCC_except_table11331
+ GCC_except_table11351
+ GCC_except_table11361
+ GCC_except_table11577
+ GCC_except_table11590
+ GCC_except_table11649
+ GCC_except_table11652
+ GCC_except_table11654
+ GCC_except_table11667
+ GCC_except_table11668
+ GCC_except_table11736
+ GCC_except_table11739
+ GCC_except_table11740
+ GCC_except_table12087
+ GCC_except_table12125
+ GCC_except_table12138
+ GCC_except_table12534
+ GCC_except_table12535
+ GCC_except_table12537
+ GCC_except_table12538
+ GCC_except_table12548
+ GCC_except_table12572
+ GCC_except_table12573
+ GCC_except_table12576
+ GCC_except_table12579
+ GCC_except_table12588
+ GCC_except_table12589
+ GCC_except_table12590
+ GCC_except_table12687
+ GCC_except_table12713
+ GCC_except_table12715
+ GCC_except_table12719
+ GCC_except_table12720
+ GCC_except_table12768
+ GCC_except_table12794
+ GCC_except_table12807
+ GCC_except_table12833
+ GCC_except_table12837
+ GCC_except_table12886
+ GCC_except_table12887
+ GCC_except_table12888
+ GCC_except_table12889
+ GCC_except_table12890
+ GCC_except_table12891
+ GCC_except_table12892
+ GCC_except_table12893
+ GCC_except_table12894
+ GCC_except_table12895
+ GCC_except_table12896
+ GCC_except_table12897
+ GCC_except_table12898
+ GCC_except_table12899
+ GCC_except_table12900
+ GCC_except_table12901
+ GCC_except_table12924
+ GCC_except_table12951
+ GCC_except_table13061
+ GCC_except_table13062
+ GCC_except_table13065
+ GCC_except_table13131
+ GCC_except_table13133
+ GCC_except_table13141
+ GCC_except_table13152
+ GCC_except_table13154
+ GCC_except_table13159
+ GCC_except_table13160
+ GCC_except_table13161
+ GCC_except_table13385
+ GCC_except_table13586
+ GCC_except_table13594
+ GCC_except_table13604
+ GCC_except_table13609
+ GCC_except_table13611
+ GCC_except_table13616
+ GCC_except_table13617
+ GCC_except_table13619
+ GCC_except_table13701
+ GCC_except_table13703
+ GCC_except_table13722
+ GCC_except_table13723
+ GCC_except_table13724
+ GCC_except_table13725
+ GCC_except_table13730
+ GCC_except_table13744
+ GCC_except_table13750
+ GCC_except_table13753
+ GCC_except_table13755
+ GCC_except_table13833
+ GCC_except_table13841
+ GCC_except_table13842
+ GCC_except_table13847
+ GCC_except_table13853
+ GCC_except_table13855
+ GCC_except_table13857
+ GCC_except_table13859
+ GCC_except_table13861
+ GCC_except_table13863
+ GCC_except_table13865
+ GCC_except_table13998
+ GCC_except_table14054
+ GCC_except_table14055
+ GCC_except_table14056
+ GCC_except_table14057
+ GCC_except_table14067
+ GCC_except_table14068
+ GCC_except_table14092
+ GCC_except_table14093
+ GCC_except_table14169
+ GCC_except_table14191
+ GCC_except_table14194
+ GCC_except_table14342
+ GCC_except_table14539
+ GCC_except_table14545
+ GCC_except_table14548
+ GCC_except_table14613
+ GCC_except_table14648
+ GCC_except_table14654
+ GCC_except_table14658
+ GCC_except_table14659
+ GCC_except_table14664
+ GCC_except_table14667
+ GCC_except_table14668
+ GCC_except_table14669
+ GCC_except_table14670
+ GCC_except_table14671
+ GCC_except_table14672
+ GCC_except_table14679
+ GCC_except_table14821
+ GCC_except_table14917
+ GCC_except_table14966
+ GCC_except_table14968
+ GCC_except_table14970
+ GCC_except_table15017
+ GCC_except_table15020
+ GCC_except_table15041
+ GCC_except_table15043
+ GCC_except_table15044
+ GCC_except_table1537
+ GCC_except_table1563
+ GCC_except_table1631
+ GCC_except_table1706
+ GCC_except_table1709
+ GCC_except_table1727
+ GCC_except_table1795
+ GCC_except_table1797
+ GCC_except_table1808
+ GCC_except_table1810
+ GCC_except_table1949
+ GCC_except_table2005
+ GCC_except_table2008
+ GCC_except_table2082
+ GCC_except_table2169
+ GCC_except_table2170
+ GCC_except_table2219
+ GCC_except_table2506
+ GCC_except_table2512
+ GCC_except_table2517
+ GCC_except_table2521
+ GCC_except_table2530
+ GCC_except_table2551
+ GCC_except_table2552
+ GCC_except_table2553
+ GCC_except_table2554
+ GCC_except_table3125
+ GCC_except_table3130
+ GCC_except_table3156
+ GCC_except_table3159
+ GCC_except_table3172
+ GCC_except_table3209
+ GCC_except_table3225
+ GCC_except_table3228
+ GCC_except_table3254
+ GCC_except_table3256
+ GCC_except_table3258
+ GCC_except_table3260
+ GCC_except_table3407
+ GCC_except_table3410
+ GCC_except_table3418
+ GCC_except_table3419
+ GCC_except_table3447
+ GCC_except_table3474
+ GCC_except_table3475
+ GCC_except_table3522
+ GCC_except_table3524
+ GCC_except_table3549
+ GCC_except_table3551
+ GCC_except_table3554
+ GCC_except_table3555
+ GCC_except_table3579
+ GCC_except_table3581
+ GCC_except_table3598
+ GCC_except_table3599
+ GCC_except_table3600
+ GCC_except_table3602
+ GCC_except_table3603
+ GCC_except_table3604
+ GCC_except_table3605
+ GCC_except_table3606
+ GCC_except_table3689
+ GCC_except_table3712
+ GCC_except_table3715
+ GCC_except_table3718
+ GCC_except_table3721
+ GCC_except_table3724
+ GCC_except_table3727
+ GCC_except_table3730
+ GCC_except_table3795
+ GCC_except_table3796
+ GCC_except_table3849
+ GCC_except_table3850
+ GCC_except_table3851
+ GCC_except_table3854
+ GCC_except_table3855
+ GCC_except_table3856
+ GCC_except_table3858
+ GCC_except_table3866
+ GCC_except_table3895
+ GCC_except_table3899
+ GCC_except_table3902
+ GCC_except_table3905
+ GCC_except_table3946
+ GCC_except_table3950
+ GCC_except_table3954
+ GCC_except_table3959
+ GCC_except_table3967
+ GCC_except_table3971
+ GCC_except_table3980
+ GCC_except_table3982
+ GCC_except_table4226
+ GCC_except_table4230
+ GCC_except_table4234
+ GCC_except_table4242
+ GCC_except_table4251
+ GCC_except_table4255
+ GCC_except_table4259
+ GCC_except_table4288
+ GCC_except_table4290
+ GCC_except_table4292
+ GCC_except_table4295
+ GCC_except_table4296
+ GCC_except_table4298
+ GCC_except_table4301
+ GCC_except_table4376
+ GCC_except_table4390
+ GCC_except_table4393
+ GCC_except_table4395
+ GCC_except_table4398
+ GCC_except_table4405
+ GCC_except_table4460
+ GCC_except_table4527
+ GCC_except_table4542
+ GCC_except_table4545
+ GCC_except_table4637
+ GCC_except_table4638
+ GCC_except_table4645
+ GCC_except_table4649
+ GCC_except_table4652
+ GCC_except_table4654
+ GCC_except_table4662
+ GCC_except_table4927
+ GCC_except_table4930
+ GCC_except_table4942
+ GCC_except_table5018
+ GCC_except_table5064
+ GCC_except_table5157
+ GCC_except_table5352
+ GCC_except_table5364
+ GCC_except_table5391
+ GCC_except_table5392
+ GCC_except_table5393
+ GCC_except_table5394
+ GCC_except_table5449
+ GCC_except_table5459
+ GCC_except_table5619
+ GCC_except_table5620
+ GCC_except_table5839
+ GCC_except_table5846
+ GCC_except_table5851
+ GCC_except_table6051
+ GCC_except_table6111
+ GCC_except_table6317
+ GCC_except_table6319
+ GCC_except_table6334
+ GCC_except_table6355
+ GCC_except_table6366
+ GCC_except_table6371
+ GCC_except_table6374
+ GCC_except_table6388
+ GCC_except_table6393
+ GCC_except_table6404
+ GCC_except_table6409
+ GCC_except_table6414
+ GCC_except_table6419
+ GCC_except_table6423
+ GCC_except_table6428
+ GCC_except_table6479
+ GCC_except_table6483
+ GCC_except_table6491
+ GCC_except_table6496
+ GCC_except_table6515
+ GCC_except_table6539
+ GCC_except_table6541
+ GCC_except_table6543
+ GCC_except_table6546
+ GCC_except_table6551
+ GCC_except_table6558
+ GCC_except_table6563
+ GCC_except_table6567
+ GCC_except_table6604
+ GCC_except_table6658
+ GCC_except_table6667
+ GCC_except_table6710
+ GCC_except_table6712
+ GCC_except_table6727
+ GCC_except_table6852
+ GCC_except_table6854
+ GCC_except_table6872
+ GCC_except_table6918
+ GCC_except_table7013
+ GCC_except_table7033
+ GCC_except_table7034
+ GCC_except_table7035
+ GCC_except_table7037
+ GCC_except_table7040
+ GCC_except_table7041
+ GCC_except_table7043
+ GCC_except_table7392
+ GCC_except_table7398
+ GCC_except_table7400
+ GCC_except_table7410
+ GCC_except_table7411
+ GCC_except_table7616
+ GCC_except_table7703
+ GCC_except_table7728
+ GCC_except_table7732
+ GCC_except_table7734
+ GCC_except_table7735
+ GCC_except_table7942
+ GCC_except_table7945
+ GCC_except_table8044
+ GCC_except_table8063
+ GCC_except_table8073
+ GCC_except_table8228
+ GCC_except_table8237
+ GCC_except_table8250
+ GCC_except_table8257
+ GCC_except_table8296
+ GCC_except_table8298
+ GCC_except_table8333
+ GCC_except_table8335
+ GCC_except_table8337
+ GCC_except_table8339
+ GCC_except_table8346
+ GCC_except_table8354
+ GCC_except_table8364
+ GCC_except_table8376
+ GCC_except_table8382
+ GCC_except_table8474
+ GCC_except_table8483
+ GCC_except_table8485
+ GCC_except_table8495
+ GCC_except_table8497
+ GCC_except_table8499
+ GCC_except_table8501
+ GCC_except_table8503
+ GCC_except_table8509
+ GCC_except_table8513
+ GCC_except_table8526
+ GCC_except_table8528
+ GCC_except_table8530
+ GCC_except_table8532
+ GCC_except_table8559
+ GCC_except_table8589
+ GCC_except_table8676
+ GCC_except_table8683
+ GCC_except_table8804
+ GCC_except_table8859
+ GCC_except_table8863
+ GCC_except_table8915
+ GCC_except_table8927
+ GCC_except_table8953
+ GCC_except_table8959
+ GCC_except_table8970
+ GCC_except_table8972
+ GCC_except_table8974
+ GCC_except_table8976
+ GCC_except_table8978
+ GCC_except_table8980
+ GCC_except_table8982
+ GCC_except_table8984
+ GCC_except_table8986
+ GCC_except_table8988
+ GCC_except_table8990
+ GCC_except_table8992
+ GCC_except_table8994
+ GCC_except_table8999
+ GCC_except_table9013
+ GCC_except_table9014
+ GCC_except_table9037
+ GCC_except_table9039
+ GCC_except_table9064
+ GCC_except_table9077
+ GCC_except_table9095
+ GCC_except_table9274
+ GCC_except_table9625
+ GCC_except_table9668
+ GCC_except_table9761
+ GCC_except_table9770
+ GCC_except_table9945
+ GCC_except_table9947
+ GCC_except_table9948
+ GCC_except_table9949
+ GCC_except_table9951
+ GCC_except_table9953
+ GCC_except_table9954
+ GCC_except_table9955
+ GCC_except_table9990
+ GCC_except_table9997
+ _HMAccessorySupportsSurroundSystemFrontRoleCodingKey
+ _HMAccessorySupportsSurroundSystemRearRoleCodingKey
+ _HMResidentDeviceSupportsSurroundConfigurationCodingKey
+ _OBJC_CLASS_$_HMMutableSurroundSystem
+ _OBJC_CLASS_$_HMSurroundSystem
+ _OBJC_CLASS_$_HMSurroundSystemConfigurationRequest
+ _OBJC_CLASS_$_HMSurroundSystemConfigurationRequestPayload
+ _OBJC_CLASS_$_HMSurroundSystemUpdateRolesRequest
+ _OBJC_IVAR_$_HMAccessory._supportsSurroundSystemFrontRoleCapability
+ _OBJC_IVAR_$_HMAccessory._supportsSurroundSystemRearRoleCapability
+ _OBJC_IVAR_$_HMResidentDevice._supportsSurroundConfiguration
+ _OBJC_IVAR_$_HMSurroundSystem._frontLeftDestinationIdentifier
+ _OBJC_IVAR_$_HMSurroundSystem._frontRightDestinationIdentifier
+ _OBJC_IVAR_$_HMSurroundSystem._rearLeftDestinationIdentifier
+ _OBJC_IVAR_$_HMSurroundSystem._rearRightDestinationIdentifier
+ _OBJC_IVAR_$_HMSurroundSystemConfigurationRequest._frontLeftAccessory
+ _OBJC_IVAR_$_HMSurroundSystemConfigurationRequest._frontRightAccessory
+ _OBJC_IVAR_$_HMSurroundSystemConfigurationRequest._identifier
+ _OBJC_IVAR_$_HMSurroundSystemConfigurationRequest._rearLeftAccessory
+ _OBJC_IVAR_$_HMSurroundSystemConfigurationRequest._rearRightAccessory
+ _OBJC_IVAR_$_HMSurroundSystemConfigurationRequest._sourceAccessory
+ _OBJC_IVAR_$_HMSurroundSystemConfigurationRequestPayload._frontLeftAccessoryUUID
+ _OBJC_IVAR_$_HMSurroundSystemConfigurationRequestPayload._frontRightAccessoryUUID
+ _OBJC_IVAR_$_HMSurroundSystemConfigurationRequestPayload._identifier
+ _OBJC_IVAR_$_HMSurroundSystemConfigurationRequestPayload._rearLeftAccessoryUUID
+ _OBJC_IVAR_$_HMSurroundSystemConfigurationRequestPayload._rearRightAccessoryUUID
+ _OBJC_IVAR_$_HMSurroundSystemConfigurationRequestPayload._sourceAccessoryUUID
+ _OBJC_IVAR_$_HMSurroundSystemUpdateRolesRequest._frontLeftAccessory
+ _OBJC_IVAR_$_HMSurroundSystemUpdateRolesRequest._frontRightAccessory
+ _OBJC_IVAR_$_HMSurroundSystemUpdateRolesRequest._rearLeftAccessory
+ _OBJC_IVAR_$_HMSurroundSystemUpdateRolesRequest._rearRightAccessory
+ _OBJC_IVAR_$_HMSurroundSystemUpdateRolesRequest._surroundSystem
+ _OBJC_METACLASS_$_HMMutableSurroundSystem
+ _OBJC_METACLASS_$_HMSurroundSystem
+ _OBJC_METACLASS_$_HMSurroundSystemConfigurationRequest
+ _OBJC_METACLASS_$_HMSurroundSystemConfigurationRequestPayload
+ _OBJC_METACLASS_$_HMSurroundSystemUpdateRolesRequest
+ __OBJC_$_CLASS_METHODS_HMSurroundSystem
+ __OBJC_$_CLASS_METHODS_HMSurroundSystemConfigurationRequest
+ __OBJC_$_CLASS_METHODS_HMSurroundSystemConfigurationRequestPayload
+ __OBJC_$_CLASS_METHODS_HMSurroundSystemUpdateRolesRequest
+ __OBJC_$_CLASS_PROP_LIST_HMSurroundSystem
+ __OBJC_$_INSTANCE_METHODS_HMMutableSurroundSystem
+ __OBJC_$_INSTANCE_METHODS_HMProtoAccessoryCapabilities(UnobfuscatedAliases)
+ __OBJC_$_INSTANCE_METHODS_HMSurroundSystem
+ __OBJC_$_INSTANCE_METHODS_HMSurroundSystemConfigurationRequest
+ __OBJC_$_INSTANCE_METHODS_HMSurroundSystemConfigurationRequestPayload
+ __OBJC_$_INSTANCE_METHODS_HMSurroundSystemUpdateRolesRequest
+ __OBJC_$_INSTANCE_VARIABLES_HMSurroundSystem
+ __OBJC_$_INSTANCE_VARIABLES_HMSurroundSystemConfigurationRequest
+ __OBJC_$_INSTANCE_VARIABLES_HMSurroundSystemConfigurationRequestPayload
+ __OBJC_$_INSTANCE_VARIABLES_HMSurroundSystemUpdateRolesRequest
+ __OBJC_$_PROP_LIST_HMMutableSurroundSystem
+ __OBJC_$_PROP_LIST_HMSurroundSystem
+ __OBJC_$_PROP_LIST_HMSurroundSystemConfigurationRequest
+ __OBJC_$_PROP_LIST_HMSurroundSystemConfigurationRequestPayload
+ __OBJC_$_PROP_LIST_HMSurroundSystemUpdateRolesRequest
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HMMediaDestinationControllerInternalDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMMediaDestinationControllerInternalDelegate
+ __OBJC_CLASS_PROTOCOLS_$_HMSurroundSystemConfigurationRequest
+ __OBJC_CLASS_PROTOCOLS_$_HMSurroundSystemConfigurationRequestPayload
+ __OBJC_CLASS_PROTOCOLS_$_HMSurroundSystemUpdateRolesRequest
+ __OBJC_CLASS_RO_$_HMMutableSurroundSystem
+ __OBJC_CLASS_RO_$_HMSurroundSystem
+ __OBJC_CLASS_RO_$_HMSurroundSystemConfigurationRequest
+ __OBJC_CLASS_RO_$_HMSurroundSystemConfigurationRequestPayload
+ __OBJC_CLASS_RO_$_HMSurroundSystemUpdateRolesRequest
+ __OBJC_METACLASS_RO_$_HMMutableSurroundSystem
+ __OBJC_METACLASS_RO_$_HMSurroundSystem
+ __OBJC_METACLASS_RO_$_HMSurroundSystemConfigurationRequest
+ __OBJC_METACLASS_RO_$_HMSurroundSystemConfigurationRequestPayload
+ __OBJC_METACLASS_RO_$_HMSurroundSystemUpdateRolesRequest
+ ___120-[HMAccessory mediaDestinationController:didGetUpdateDestinationRequestWithSurroundSystemDestination:completionHandler:]_block_invoke
+ ___120-[HMCurrentMediaGroupProvider _notifyClientOfCurrentMediaGroupWithCurrentAccessory:surroundSystem:sourceAccessory:home:]_block_invoke
+ ___120-[HMCurrentMediaGroupProvider _notifyClientOfCurrentMediaGroupWithCurrentAccessory:surroundSystem:sourceAccessory:home:]_block_invoke_2
+ ___48-[HMSurroundSystem destinationUniqueIdentifiers]_block_invoke
+ ___49+[HMSurroundSystemUpdateRolesRequest logCategory]_block_invoke
+ ___51+[HMSurroundSystemConfigurationRequest logCategory]_block_invoke
+ ___55-[HMAccessory accessoryWithAudioDestinationIdentifier:]_block_invoke
+ ___58+[HMSurroundSystemConfigurationRequestPayload logCategory]_block_invoke
+ ___60-[HMHome accessoryWithAudioDestinationControllerIdentifier:]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e43_"HMMediaGroupParticipant"16?0"NSString"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e30_v24?0"NSString"8"NSError"16ls32l8s40l8s48l8
+ _logCategory._hmf_once_t75
+ _logCategory._hmf_once_t781
+ _logCategory._hmf_once_t842
+ _logCategory._hmf_once_t92
+ _logCategory._hmf_once_v76
+ _logCategory._hmf_once_v782
+ _logCategory._hmf_once_v843
+ _logCategory._hmf_once_v93
- GCC_except_table10027
- GCC_except_table10036
- GCC_except_table10050
- GCC_except_table10120
- GCC_except_table10149
- GCC_except_table10150
- GCC_except_table10151
- GCC_except_table10153
- GCC_except_table10156
- GCC_except_table10157
- GCC_except_table10163
- GCC_except_table10312
- GCC_except_table10313
- GCC_except_table10314
- GCC_except_table10318
- GCC_except_table10373
- GCC_except_table10394
- GCC_except_table10474
- GCC_except_table10476
- GCC_except_table10478
- GCC_except_table10480
- GCC_except_table10488
- GCC_except_table10538
- GCC_except_table10550
- GCC_except_table10552
- GCC_except_table10568
- GCC_except_table10597
- GCC_except_table10786
- GCC_except_table10787
- GCC_except_table10822
- GCC_except_table10855
- GCC_except_table10858
- GCC_except_table10861
- GCC_except_table10863
- GCC_except_table10929
- GCC_except_table10949
- GCC_except_table10950
- GCC_except_table10951
- GCC_except_table10990
- GCC_except_table10992
- GCC_except_table10994
- GCC_except_table11059
- GCC_except_table11091
- GCC_except_table11093
- GCC_except_table11097
- GCC_except_table11114
- GCC_except_table11116
- GCC_except_table11122
- GCC_except_table11126
- GCC_except_table11129
- GCC_except_table11136
- GCC_except_table11140
- GCC_except_table11146
- GCC_except_table11158
- GCC_except_table11161
- GCC_except_table11169
- GCC_except_table11170
- GCC_except_table11172
- GCC_except_table11174
- GCC_except_table11176
- GCC_except_table11196
- GCC_except_table11206
- GCC_except_table11422
- GCC_except_table11435
- GCC_except_table11494
- GCC_except_table11497
- GCC_except_table11499
- GCC_except_table11512
- GCC_except_table11513
- GCC_except_table11581
- GCC_except_table11584
- GCC_except_table11585
- GCC_except_table11932
- GCC_except_table11970
- GCC_except_table11983
- GCC_except_table12379
- GCC_except_table12380
- GCC_except_table12382
- GCC_except_table12383
- GCC_except_table12393
- GCC_except_table12417
- GCC_except_table12418
- GCC_except_table12421
- GCC_except_table12424
- GCC_except_table12433
- GCC_except_table12434
- GCC_except_table12435
- GCC_except_table12532
- GCC_except_table12558
- GCC_except_table12560
- GCC_except_table12564
- GCC_except_table12565
- GCC_except_table12613
- GCC_except_table12639
- GCC_except_table12652
- GCC_except_table12678
- GCC_except_table12682
- GCC_except_table12731
- GCC_except_table12732
- GCC_except_table12733
- GCC_except_table12734
- GCC_except_table12735
- GCC_except_table12736
- GCC_except_table12737
- GCC_except_table12738
- GCC_except_table12739
- GCC_except_table12740
- GCC_except_table12741
- GCC_except_table12742
- GCC_except_table12743
- GCC_except_table12744
- GCC_except_table12745
- GCC_except_table12746
- GCC_except_table12769
- GCC_except_table12796
- GCC_except_table12906
- GCC_except_table12907
- GCC_except_table12910
- GCC_except_table12976
- GCC_except_table12978
- GCC_except_table12986
- GCC_except_table12997
- GCC_except_table12999
- GCC_except_table13004
- GCC_except_table13005
- GCC_except_table13006
- GCC_except_table13230
- GCC_except_table13431
- GCC_except_table13434
- GCC_except_table13439
- GCC_except_table13443
- GCC_except_table13449
- GCC_except_table13454
- GCC_except_table13456
- GCC_except_table13461
- GCC_except_table13462
- GCC_except_table13464
- GCC_except_table13546
- GCC_except_table13548
- GCC_except_table13567
- GCC_except_table13568
- GCC_except_table13569
- GCC_except_table13570
- GCC_except_table13575
- GCC_except_table13595
- GCC_except_table13600
- GCC_except_table13678
- GCC_except_table13686
- GCC_except_table13687
- GCC_except_table13692
- GCC_except_table13698
- GCC_except_table13700
- GCC_except_table13702
- GCC_except_table13704
- GCC_except_table13706
- GCC_except_table13708
- GCC_except_table13710
- GCC_except_table13843
- GCC_except_table13899
- GCC_except_table13900
- GCC_except_table13901
- GCC_except_table13902
- GCC_except_table13912
- GCC_except_table13913
- GCC_except_table13937
- GCC_except_table13938
- GCC_except_table14014
- GCC_except_table14036
- GCC_except_table14039
- GCC_except_table14187
- GCC_except_table14384
- GCC_except_table14390
- GCC_except_table14393
- GCC_except_table14458
- GCC_except_table14493
- GCC_except_table14499
- GCC_except_table14503
- GCC_except_table14504
- GCC_except_table14509
- GCC_except_table14511
- GCC_except_table14512
- GCC_except_table14513
- GCC_except_table14514
- GCC_except_table14515
- GCC_except_table14516
- GCC_except_table14517
- GCC_except_table14524
- GCC_except_table14656
- GCC_except_table14762
- GCC_except_table14813
- GCC_except_table14815
- GCC_except_table14862
- GCC_except_table14865
- GCC_except_table14886
- GCC_except_table14888
- GCC_except_table14889
- GCC_except_table1535
- GCC_except_table1561
- GCC_except_table1629
- GCC_except_table1700
- GCC_except_table1703
- GCC_except_table1721
- GCC_except_table1789
- GCC_except_table1791
- GCC_except_table1802
- GCC_except_table1804
- GCC_except_table1943
- GCC_except_table1997
- GCC_except_table2000
- GCC_except_table2074
- GCC_except_table2161
- GCC_except_table2162
- GCC_except_table2211
- GCC_except_table2498
- GCC_except_table2501
- GCC_except_table2504
- GCC_except_table2513
- GCC_except_table2522
- GCC_except_table2535
- GCC_except_table2537
- GCC_except_table2538
- GCC_except_table2544
- GCC_except_table3111
- GCC_except_table3116
- GCC_except_table3142
- GCC_except_table3145
- GCC_except_table3158
- GCC_except_table3195
- GCC_except_table3211
- GCC_except_table3214
- GCC_except_table3240
- GCC_except_table3242
- GCC_except_table3244
- GCC_except_table3246
- GCC_except_table3393
- GCC_except_table3396
- GCC_except_table3404
- GCC_except_table3405
- GCC_except_table3433
- GCC_except_table3460
- GCC_except_table3461
- GCC_except_table3508
- GCC_except_table3510
- GCC_except_table3535
- GCC_except_table3537
- GCC_except_table3540
- GCC_except_table3541
- GCC_except_table3565
- GCC_except_table3567
- GCC_except_table3575
- GCC_except_table3577
- GCC_except_table3584
- GCC_except_table3585
- GCC_except_table3586
- GCC_except_table3588
- GCC_except_table3590
- GCC_except_table3592
- GCC_except_table3675
- GCC_except_table3698
- GCC_except_table3701
- GCC_except_table3704
- GCC_except_table3707
- GCC_except_table3710
- GCC_except_table3713
- GCC_except_table3716
- GCC_except_table3781
- GCC_except_table3782
- GCC_except_table3828
- GCC_except_table3835
- GCC_except_table3836
- GCC_except_table3837
- GCC_except_table3840
- GCC_except_table3841
- GCC_except_table3844
- GCC_except_table3852
- GCC_except_table3874
- GCC_except_table3881
- GCC_except_table3885
- GCC_except_table3891
- GCC_except_table3932
- GCC_except_table3936
- GCC_except_table3940
- GCC_except_table3945
- GCC_except_table3953
- GCC_except_table3957
- GCC_except_table3966
- GCC_except_table3968
- GCC_except_table4212
- GCC_except_table4216
- GCC_except_table4220
- GCC_except_table4223
- GCC_except_table4227
- GCC_except_table4228
- GCC_except_table4231
- GCC_except_table4268
- GCC_except_table4270
- GCC_except_table4272
- GCC_except_table4275
- GCC_except_table4276
- GCC_except_table4278
- GCC_except_table4281
- GCC_except_table4356
- GCC_except_table4370
- GCC_except_table4373
- GCC_except_table4375
- GCC_except_table4378
- GCC_except_table4385
- GCC_except_table4440
- GCC_except_table4505
- GCC_except_table4520
- GCC_except_table4523
- GCC_except_table4615
- GCC_except_table4616
- GCC_except_table4618
- GCC_except_table4623
- GCC_except_table4627
- GCC_except_table4630
- GCC_except_table4632
- GCC_except_table4901
- GCC_except_table4904
- GCC_except_table4916
- GCC_except_table4992
- GCC_except_table5038
- GCC_except_table5131
- GCC_except_table5326
- GCC_except_table5338
- GCC_except_table5340
- GCC_except_table5365
- GCC_except_table5367
- GCC_except_table5368
- GCC_except_table5423
- GCC_except_table5433
- GCC_except_table5593
- GCC_except_table5594
- GCC_except_table5810
- GCC_except_table5817
- GCC_except_table5822
- GCC_except_table6022
- GCC_except_table6082
- GCC_except_table6288
- GCC_except_table6290
- GCC_except_table6297
- GCC_except_table6305
- GCC_except_table6337
- GCC_except_table6342
- GCC_except_table6345
- GCC_except_table6359
- GCC_except_table6364
- GCC_except_table6370
- GCC_except_table6375
- GCC_except_table6380
- GCC_except_table6385
- GCC_except_table6390
- GCC_except_table6394
- GCC_except_table6450
- GCC_except_table6454
- GCC_except_table6462
- GCC_except_table6467
- GCC_except_table6481
- GCC_except_table6486
- GCC_except_table6493
- GCC_except_table6509
- GCC_except_table6512
- GCC_except_table6514
- GCC_except_table6517
- GCC_except_table6529
- GCC_except_table6534
- GCC_except_table6575
- GCC_except_table6629
- GCC_except_table6638
- GCC_except_table6681
- GCC_except_table6683
- GCC_except_table6698
- GCC_except_table6740
- GCC_except_table6742
- GCC_except_table6760
- GCC_except_table6806
- GCC_except_table6901
- GCC_except_table6921
- GCC_except_table6922
- GCC_except_table6923
- GCC_except_table6925
- GCC_except_table6928
- GCC_except_table6929
- GCC_except_table6931
- GCC_except_table7278
- GCC_except_table7284
- GCC_except_table7286
- GCC_except_table7296
- GCC_except_table7297
- GCC_except_table7502
- GCC_except_table7506
- GCC_except_table7589
- GCC_except_table7614
- GCC_except_table7618
- GCC_except_table7621
- GCC_except_table7828
- GCC_except_table7831
- GCC_except_table7924
- GCC_except_table7943
- GCC_except_table7953
- GCC_except_table8108
- GCC_except_table8117
- GCC_except_table8130
- GCC_except_table8137
- GCC_except_table8176
- GCC_except_table8178
- GCC_except_table8213
- GCC_except_table8215
- GCC_except_table8217
- GCC_except_table8219
- GCC_except_table8226
- GCC_except_table8234
- GCC_except_table8244
- GCC_except_table8256
- GCC_except_table8262
- GCC_except_table8350
- GCC_except_table8359
- GCC_except_table8361
- GCC_except_table8371
- GCC_except_table8373
- GCC_except_table8375
- GCC_except_table8377
- GCC_except_table8379
- GCC_except_table8385
- GCC_except_table8389
- GCC_except_table8402
- GCC_except_table8404
- GCC_except_table8406
- GCC_except_table8408
- GCC_except_table8435
- GCC_except_table8465
- GCC_except_table8524
- GCC_except_table8531
- GCC_except_table8652
- GCC_except_table8707
- GCC_except_table8709
- GCC_except_table8711
- GCC_except_table8733
- GCC_except_table8763
- GCC_except_table8775
- GCC_except_table8801
- GCC_except_table8807
- GCC_except_table8818
- GCC_except_table8820
- GCC_except_table8822
- GCC_except_table8824
- GCC_except_table8826
- GCC_except_table8828
- GCC_except_table8830
- GCC_except_table8832
- GCC_except_table8834
- GCC_except_table8836
- GCC_except_table8838
- GCC_except_table8840
- GCC_except_table8842
- GCC_except_table8847
- GCC_except_table8862
- GCC_except_table8887
- GCC_except_table8912
- GCC_except_table8925
- GCC_except_table8943
- GCC_except_table9122
- GCC_except_table9473
- GCC_except_table9516
- GCC_except_table9609
- GCC_except_table9618
- GCC_except_table9793
- GCC_except_table9795
- GCC_except_table9796
- GCC_except_table9797
- GCC_except_table9799
- GCC_except_table9801
- GCC_except_table9802
- GCC_except_table9803
- GCC_except_table9838
- GCC_except_table9841
- GCC_except_table9842
- GCC_except_table9845
- GCC_except_table9848
- GCC_except_table9849
- GCC_except_table9892
- GCC_except_table9893
- GCC_except_table9894
- GCC_except_table9901
- GCC_except_table9902
- GCC_except_table9904
- GCC_except_table9923
- GCC_except_table9992
- __OBJC_$_INSTANCE_METHODS_HMProtoAccessoryCapabilities
- __OBJC_$_PROP_LIST_HMProtoAccessoryCapabilities
- _logCategory._hmf_once_t105
- _logCategory._hmf_once_t22
- _logCategory._hmf_once_t71
- _logCategory._hmf_once_t777
- _logCategory._hmf_once_t830
- _logCategory._hmf_once_t87
- _logCategory._hmf_once_v106
- _logCategory._hmf_once_v23
- _logCategory._hmf_once_v72
- _logCategory._hmf_once_v778
- _logCategory._hmf_once_v831
- _logCategory._hmf_once_v88
CStrings:
+ ", frontLeftAccessoryUUID: %@"
+ ", frontLeftDestinationIdentifier: %@"
+ ", frontRightAccessoryUUID: %@"
+ ", frontRightDestinationIdentifier: %@"
+ ", isValid: %@"
+ ", needsRoomChangeCount: %@"
+ ", rearLeftAccessoryUUID: %@"
+ ", rearLeftDestinationIdentifier: %@"
+ ", rearRightAccessoryUUID: %@"
+ ", rearRightDestinationIdentifier: %@"
+ ", sourceAccessoryUUID: %@"
+ ", surroundSystemIdentifier: %@"
+ "73C81D06-E21A-4614-93C9-038DC106F5E3"
+ "<Merge> Notifying client of updated supportsSurroundConfiguration value: %@"
+ "<Merge> Updating supportsSurroundConfiguration from %@ to %@"
+ "<SS %@ n:%@ L:%@ R:%@ l:%@ r:%@>"
+ "@\"HMMediaGroupParticipant\"16@?0@\"NSString\"8"
+ "Configured surround system: %@"
+ "Failed to configure surround system destination: %@ due to no home for controller: %@"
+ "Failed to configure surround system destination: %@ due to no surround system in groups controller: %@"
+ "Failed to configure surround system: %@ due to unresolved role accessories front left: %@ front right: %@ rear left: %@ rear right: %@"
+ "Failed to configure surround system: %@ with error domain: %@ code: %@"
+ "Failed to get source accessory due to no accessory with destination controller: %@"
+ "Failed to get source accessory due to no home theater group for surround system: %@"
+ "Failed to merge surround system home theater due to invalid participant count: %@"
+ "Failed to merge surround system home theater due to no surround system for destination: %@ in groups controller: %@"
+ "Failed to merge with surround system due to no destination controller for surround system: %@ destination: %@"
+ "Failed to parse surround system payload: %@"
+ "Failed to update surround system roles due to no source accessory for group: %@ from data source: %@"
+ "Failed to update to surround system destination: %@ due to no internal delegate"
+ "HM.ac.supportsSurroundSystemFrontRole"
+ "HM.ac.supportsSurroundSystemRearRole"
+ "HMCurrentMediaGroupTypeHomeTheaterSurroundSystem"
+ "HMMediaDestinationSurroundSystem"
+ "HMMediaGroupParticipantRoleSurroundSystemFrontLeft"
+ "HMMediaGroupParticipantRoleSurroundSystemFrontRight"
+ "HMMediaGroupParticipantRoleSurroundSystemRearLeft"
+ "HMMediaGroupParticipantRoleSurroundSystemRearRight"
+ "HMResidentDeviceSupportsSurroundConfigurationCodingKey"
+ "HMSurroundSystemAssociatedGroupIdentifierCodingKey"
+ "HMSurroundSystemConfigurationRequest"
+ "HMSurroundSystemDataRoomNameSentinel"
+ "HMSurroundSystemDefaultNameCodingKey"
+ "HMSurroundSystemFrontLeftAccessoryUUID"
+ "HMSurroundSystemFrontLeftDestinationIdentifierCodingKey"
+ "HMSurroundSystemFrontRightAccessoryUUID"
+ "HMSurroundSystemFrontRightDestinationIdentifierCodingKey"
+ "HMSurroundSystemIdentifier"
+ "HMSurroundSystemIdentifierCodingKey"
+ "HMSurroundSystemNameCodingKey"
+ "HMSurroundSystemParentIdentifierCodingKey"
+ "HMSurroundSystemRearLeftAccessoryUUID"
+ "HMSurroundSystemRearLeftDestinationIdentifierCodingKey"
+ "HMSurroundSystemRearRightAccessoryUUID"
+ "HMSurroundSystemRearRightDestinationIdentifierCodingKey"
+ "HMSurroundSystemSourceAccessoryUUID"
+ "Handing update destination request for surround system destination: %@ to internal delegate: %@"
+ "Handling did get update destination request with surround system destination: %@ controller: %@"
+ "HomeTheaterSurround"
+ "Media.Group.SurroundSystem.ConfigurationRequest"
+ "Media.Group.SurroundSystem.ConfigurationRequest.Payload"
+ "Media.Group.SurroundSystem.UpdateRolesRequest"
+ "SF "
+ "SR "
+ "SS "
+ "Updating supports Surround System front role capability to %@"
+ "Updating supports Surround System rear role capability to %@"
+ "Updating surround system roles with request: %@ for group: %@"
+ "[%{public}@] <Merge> Notifying client of updated supportsSurroundConfiguration value: %@"
+ "[%{public}@] <Merge> Updating supportsSurroundConfiguration from %@ to %@"
+ "[%{public}@] Configured surround system: %@"
+ "[%{public}@] Failed to configure surround system destination: %@ due to no home for controller: %@"
+ "[%{public}@] Failed to configure surround system destination: %@ due to no surround system in groups controller: %@"
+ "[%{public}@] Failed to configure surround system: %@ due to unresolved role accessories front left: %@ front right: %@ rear left: %@ rear right: %@"
+ "[%{public}@] Failed to configure surround system: %@ with error domain: %@ code: %@"
+ "[%{public}@] Failed to get source accessory due to no accessory with destination controller: %@"
+ "[%{public}@] Failed to get source accessory due to no home theater group for surround system: %@"
+ "[%{public}@] Failed to merge surround system home theater due to invalid participant count: %@"
+ "[%{public}@] Failed to merge surround system home theater due to no surround system for destination: %@ in groups controller: %@"
+ "[%{public}@] Failed to merge with surround system due to no destination controller for surround system: %@ destination: %@"
+ "[%{public}@] Failed to parse surround system payload: %@"
+ "[%{public}@] Failed to update surround system roles due to no source accessory for group: %@ from data source: %@"
+ "[%{public}@] Failed to update to surround system destination: %@ due to no internal delegate"
+ "[%{public}@] Handing update destination request for surround system destination: %@ to internal delegate: %@"
+ "[%{public}@] Handling did get update destination request with surround system destination: %@ controller: %@"
+ "[%{public}@] Updating supports Surround System front role capability to %@"
+ "[%{public}@] Updating supports Surround System rear role capability to %@"
+ "[%{public}@] Updating surround system roles with request: %@ for group: %@"
+ "[%{public}@] [HMSurroundSystem] Failed to decode event data: %@"
+ "[%{public}@] [HMSurroundSystem] Failed to derive destination unique identifier: %@"
+ "[HMSurroundSystem] Failed to decode event data: %@"
+ "[HMSurroundSystem] Failed to derive destination unique identifier: %@"
+ "frontLeftAccessory is required"
+ "frontRightAccessory is required"
+ "rearLeftAccessory is required"
+ "rearRightAccessory is required"
+ "sourceAccessory is required"
+ "surroundSystem is required"
+ "v24@?0@\"NSString\"8@\"NSError\"16"
```
