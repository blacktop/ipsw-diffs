## HomeKit

> `/System/Library/Frameworks/HomeKit.framework/HomeKit`

```diff

-1092.4.10.0.0
-  __TEXT.__text: 0x260414
-  __TEXT.__auth_stubs: 0xcc0
-  __TEXT.__objc_methlist: 0x20154
+1124.5.8.1.1
+  __TEXT.__text: 0x273638
+  __TEXT.__auth_stubs: 0xd20
+  __TEXT.__objc_methlist: 0x1ff74
   __TEXT.__const: 0x290
-  __TEXT.__gcc_except_tab: 0x3fa0
-  __TEXT.__cstring: 0x258bd
-  __TEXT.__oslogstring: 0x24ffc
-  __TEXT.__dlopen_cstrs: 0x3a2
+  __TEXT.__gcc_except_tab: 0x403c
+  __TEXT.__cstring: 0x25b30
+  __TEXT.__oslogstring: 0x256ef
+  __TEXT.__dlopen_cstrs: 0x3ee
   __TEXT.__ustring: 0x50
-  __TEXT.__unwind_info: 0x926c
-  __TEXT.__objc_classname: 0x49a5
-  __TEXT.__objc_methname: 0x3fccf
-  __TEXT.__objc_methtype: 0x77f8
-  __TEXT.__objc_stubs: 0x23480
+  __TEXT.__unwind_info: 0x92b8
+  __TEXT.__objc_classname: 0x49ee
+  __TEXT.__objc_methname: 0x3fead
+  __TEXT.__objc_methtype: 0x7913
+  __TEXT.__objc_stubs: 0x230e0
   __DATA_CONST.__got: 0x3a0
-  __DATA_CONST.__const: 0x6d70
-  __DATA_CONST.__objc_classlist: 0x1068
+  __DATA_CONST.__const: 0x6e78
+  __DATA_CONST.__objc_classlist: 0x1078
   __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x470
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x31a00
-  __DATA_CONST.__objc_selrefs: 0xbcd8
+  __DATA_CONST.__objc_const: 0x31a28
+  __DATA_CONST.__objc_selrefs: 0xbc98
+  __DATA_CONST.__objc_protorefs: 0x98
+  __DATA_CONST.__objc_classrefs: 0x1318
+  __DATA_CONST.__objc_superrefs: 0xdf0
   __DATA_CONST.__objc_arraydata: 0x1330
-  __AUTH_CONST.__cfstring: 0x23500
-  __AUTH_CONST.__objc_const: 0xf188
-  __AUTH_CONST.__const: 0x1960
+  __AUTH_CONST.__cfstring: 0x23820
+  __AUTH_CONST.__objc_const: 0xf1d0
+  __AUTH_CONST.__const: 0x1980
   __AUTH_CONST.__objc_intobj: 0x798
   __AUTH_CONST.__objc_dictobj: 0x848
   __AUTH_CONST.__objc_arrayobj: 0x540
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0x670
-  __AUTH.__objc_data: 0x7bc0
-  __DATA.__objc_protorefs: 0x98
-  __DATA.__objc_classrefs: 0x1308
-  __DATA.__objc_superrefs: 0xdd8
-  __DATA.__objc_ivar: 0x218c
-  __DATA.__data: 0x3618
+  __AUTH_CONST.__auth_got: 0x6a0
+  __AUTH.__objc_data: 0x7c10
+  __DATA.__objc_ivar: 0x2180
+  __DATA.__data: 0x3630
   __DATA.__common: 0x18
-  __DATA.__bss: 0x7f0
-  __DATA_DIRTY.__objc_data: 0x2850
+  __DATA.__bss: 0x818
+  __DATA_DIRTY.__objc_data: 0x28a0
   __DATA_DIRTY.__bss: 0x1d0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 12575
-  Symbols:   40259
-  CStrings:  18579
+  Functions: 12547
+  Symbols:   40214
+  CStrings:  18631
 
Symbols:
+ +[HMAccessory(NetworkRouter) networkRouterStatusFromRouterStatus:wanStatusListData:]
+ +[HMAccessory(NetworkRouter) networkRouterStatusFromWiFiSatelliteStatus:]
+ +[HMAccessory(NetworkRouterInternal) _networkRouterProfilesForAccessoryProfiles:]
+ +[HMAudioAnalysisEventBulletinBoardNotification logCategory]
+ +[HMAudioAnalysisEventBulletinBoardNotification predicateForOptions:]
+ +[HMAudioAnalysisEventBulletinBoardNotification shortDescription]
+ +[HMCameraBulletinBoardSmartNotification logCategory]
+ +[HMCameraBulletinBoardSmartNotification shortDescription]
+ +[HMFObjectCacheHMSettingLanguageValue cachedInstanceForLanguageSettingValue:]
+ +[HMLightProfileNaturalLightingAction actionWithProtoBuf:home:]
+ +[HMNetworkRouterWANStatus parsedFromData:error:]
+ +[HMNetworkRouterWANStatusList parsedFromData:error:]
+ +[HMSoftwareUpdateV2 softwareUpdateFromDescriptor:]
+ -[HMAccessoryDiagnosticInfo softwareUpdate]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo hasSfProblemFlags]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo setHasSfProblemFlags:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo setSfProblemFlags:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo sfProblemFlags]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo StringAsLastKnownControllerHH2Mode:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo StringAsLastKnownControllerSentinelZoneExistence:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasLastKnownControllerHH2Mode]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo hasLastKnownControllerSentinelZoneExistence]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo lastKnownControllerHH2ModeAsString:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo lastKnownControllerHH2Mode]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo lastKnownControllerSentinelZoneExistenceAsString:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo lastKnownControllerSentinelZoneExistence]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasLastKnownControllerHH2Mode:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setHasLastKnownControllerSentinelZoneExistence:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setLastKnownControllerHH2Mode:]
+ -[HMAccessoryDiagnosticInfoProtoSetupInfo setLastKnownControllerSentinelZoneExistence:]
+ -[HMActionSet _removeActionsForAccessory:]
+ -[HMAudioAnalysisEventBulletinBoardNotification __configureWithContext:]
+ -[HMAudioAnalysisEventBulletinBoardNotification attributeDescriptions]
+ -[HMAudioAnalysisEventBulletinBoardNotification description]
+ -[HMAudioAnalysisEventBulletinBoardNotification initWithEnabled:condition:accessoryIdentifier:]
+ -[HMAudioAnalysisEventBulletinBoardNotification logIdentifier]
+ -[HMAudioAnalysisEventBulletinBoardNotification mergeFromNewObject:]
+ -[HMAudioAnalysisEventBulletinBoardNotification privateDescription]
+ -[HMAudioAnalysisEventBulletinBoardNotification shortDescription]
+ -[HMAudioAnalysisEventBulletinBoardNotification uniqueIdentifier]
+ -[HMBulletinBoardNotification initWithEnabled:condition:service:messageTargetUUID:]
+ -[HMCameraBulletinBoardSmartNotification attributeDescriptions]
+ -[HMCameraBulletinBoardSmartNotification initWithEnabled:condition:context:cameraUserSettings:]
+ -[HMCameraBulletinBoardSmartNotification logIdentifier]
+ -[HMCameraBulletinBoardSmartNotification privateDescription]
+ -[HMCameraBulletinBoardSmartNotification shortDescription]
+ -[HMCameraClipManager addObserver:queue:]
+ -[HMCameraClipManager delegateCallersByObservers]
+ -[HMCameraClipManager fetchIsCloudStorageEnabledWithCompletion:]
+ -[HMCameraClipManager setCloudStorageEnabled:completion:]
+ -[HMCameraRecordingEventManager addObserver:queue:]
+ -[HMCameraRecordingEventManager delegateCallersByObservers]
+ -[HMCameraRecordingReachabilityEventManager addObserver:queue:]
+ -[HMCameraRecordingReachabilityEventManager delegateCallersByObservers]
+ -[HMCameraUserSettings createSmartNotificationBulletin]
+ -[HMCharacteristic _updateValue:valueUpdatedDate:]
+ -[HMEventTrigger _removeEventsForAccessory:]
+ -[HMHome _removeActionSetsForAccessory:]
+ -[HMHome _removeEventsForAccessory:]
+ -[HMHome confirmResidentWithCompletion:]
+ -[HMHome setSupportsResidentActionSetStateEvaluation:]
+ -[HMHome supportsResidentActionSetStateEvaluation]
+ -[HMHome updateResidentSelectionVersion:completion:]
+ -[HMHomeManager _didUpdateHomes]
+ -[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]
+ -[HMHomeManager _removeCacheFileAtPath:]
+ -[HMHomeManager _setInitialHomes:]
+ -[HMHomeManager addEphemeralContainerWithName:completion:]
+ -[HMHomeManager deactivateEphemeralContainerWithName:completion:]
+ -[HMHomeManager deleteEphemeralContainerWithName:completion:]
+ -[HMHomeManager isInitialMergeComplete]
+ -[HMHomeManager readCountersForGroup:homeUUIDString:accessoryUUIDString:counter:statistics:datePartition:ephemeralContainerName:completion:]
+ -[HMHomeManager setInitialMergeComplete:]
+ -[HMHomeManager startupEphemeralContainerWithName:completion:]
+ -[HMNetworkRouterWANStatus .cxx_destruct]
+ -[HMNetworkRouterWANStatus copyWithZone:]
+ -[HMNetworkRouterWANStatus description]
+ -[HMNetworkRouterWANStatus identifier]
+ -[HMNetworkRouterWANStatus initWithIdentifier:status:]
+ -[HMNetworkRouterWANStatus init]
+ -[HMNetworkRouterWANStatus isEqual:]
+ -[HMNetworkRouterWANStatus parseFromData:error:]
+ -[HMNetworkRouterWANStatus serializeWithError:]
+ -[HMNetworkRouterWANStatus setIdentifier:]
+ -[HMNetworkRouterWANStatus setStatus:]
+ -[HMNetworkRouterWANStatus status]
+ -[HMNetworkRouterWANStatusList .cxx_destruct]
+ -[HMNetworkRouterWANStatusList copyWithZone:]
+ -[HMNetworkRouterWANStatusList description]
+ -[HMNetworkRouterWANStatusList initWithStatuses:]
+ -[HMNetworkRouterWANStatusList init]
+ -[HMNetworkRouterWANStatusList isEqual:]
+ -[HMNetworkRouterWANStatusList parseFromData:error:]
+ -[HMNetworkRouterWANStatusList serializeWithError:]
+ -[HMNetworkRouterWANStatusList setStatuses:]
+ -[HMNetworkRouterWANStatusList statuses]
+ -[HMProtoResidentCapabilities hasSupportsActivityLoggingOnPrimary]
+ -[HMProtoResidentCapabilities hasSupportsResidentActionSetStateEvaluation]
+ -[HMProtoResidentCapabilities setHasSupportsActivityLoggingOnPrimary:]
+ -[HMProtoResidentCapabilities setHasSupportsResidentActionSetStateEvaluation:]
+ -[HMProtoResidentCapabilities setSupportsActivityLoggingOnPrimary:]
+ -[HMProtoResidentCapabilities setSupportsResidentActionSetStateEvaluation:]
+ -[HMProtoResidentCapabilities supportsActivityLoggingOnPrimary]
+ -[HMProtoResidentCapabilities supportsResidentActionSetStateEvaluation]
+ -[HMResidentCapabilities supportsResidentActionSetStateEvaluation]
+ -[HMResidentDevice IDSDestination]
+ -[HMResidentDevice IDSIdentifier]
+ -[HMResidentDevice deviceIRKData]
+ -[HMResidentDevice setDeviceIRKData:]
+ -[HMResidentDevice setIDSDestination:]
+ -[HMResidentDevice setIDSIdentifier:]
+ -[HMService matterEndpointID]
+ -[HMService setMatterEndpointID:]
+ -[HMService setUserInteractive:]
+ -[HMSettingLanguageValue copyWithZone:]
+ -[HMSoftwareUpdate displayableVersion]
+ -[HMSoftwareUpdate initWithVersion:displayableVersion:downloadSize:state:installDuration:documentationMetadata:releaseDate:]
+ -[NSString(HomeKit) hm_truncatedDisplayableVersionString]
+ -[_HMCameraControl __configureWithContext:]
+ -[_HMCameraProfile _createControlsWithMostRecentSnapshot:]
+ -[_HMCameraProfile snapshotControl]
+ -[_HMCameraProfile streamControl]
+ -[_HMCameraSnapshotControl __configureWithContext:]
+ -[_HMCameraStreamControl __configureWithContext:]
+ GCC_except_table1015
+ GCC_except_table10291
+ GCC_except_table10293
+ GCC_except_table10295
+ GCC_except_table10327
+ GCC_except_table10329
+ GCC_except_table10331
+ GCC_except_table10337
+ GCC_except_table10338
+ GCC_except_table10339
+ GCC_except_table10447
+ GCC_except_table10448
+ GCC_except_table10474
+ GCC_except_table10476
+ GCC_except_table10480
+ GCC_except_table10481
+ GCC_except_table10529
+ GCC_except_table10555
+ GCC_except_table10568
+ GCC_except_table10592
+ GCC_except_table10596
+ GCC_except_table10637
+ GCC_except_table10638
+ GCC_except_table10639
+ GCC_except_table10668
+ GCC_except_table10695
+ GCC_except_table10802
+ GCC_except_table10803
+ GCC_except_table1085
+ GCC_except_table10870
+ GCC_except_table10872
+ GCC_except_table1088
+ GCC_except_table10880
+ GCC_except_table10886
+ GCC_except_table10893
+ GCC_except_table10895
+ GCC_except_table1090
+ GCC_except_table10900
+ GCC_except_table1092
+ GCC_except_table1096
+ GCC_except_table11105
+ GCC_except_table11106
+ GCC_except_table11259
+ GCC_except_table11262
+ GCC_except_table11267
+ GCC_except_table11271
+ GCC_except_table11277
+ GCC_except_table11282
+ GCC_except_table11289
+ GCC_except_table11290
+ GCC_except_table11375
+ GCC_except_table11377
+ GCC_except_table11396
+ GCC_except_table11397
+ GCC_except_table11398
+ GCC_except_table11399
+ GCC_except_table11404
+ GCC_except_table11418
+ GCC_except_table11427
+ GCC_except_table1145
+ GCC_except_table11511
+ GCC_except_table11513
+ GCC_except_table11516
+ GCC_except_table11524
+ GCC_except_table11525
+ GCC_except_table11530
+ GCC_except_table11538
+ GCC_except_table11540
+ GCC_except_table11542
+ GCC_except_table11544
+ GCC_except_table11546
+ GCC_except_table11682
+ GCC_except_table11738
+ GCC_except_table11739
+ GCC_except_table11740
+ GCC_except_table11741
+ GCC_except_table11752
+ GCC_except_table11753
+ GCC_except_table11777
+ GCC_except_table11778
+ GCC_except_table11831
+ GCC_except_table11854
+ GCC_except_table11857
+ GCC_except_table11989
+ GCC_except_table12101
+ GCC_except_table12102
+ GCC_except_table12103
+ GCC_except_table12151
+ GCC_except_table12152
+ GCC_except_table12154
+ GCC_except_table12157
+ GCC_except_table12159
+ GCC_except_table12161
+ GCC_except_table12193
+ GCC_except_table12236
+ GCC_except_table12241
+ GCC_except_table12244
+ GCC_except_table12304
+ GCC_except_table12389
+ GCC_except_table12397
+ GCC_except_table12450
+ GCC_except_table12452
+ GCC_except_table12461
+ GCC_except_table12464
+ GCC_except_table12484
+ GCC_except_table12486
+ GCC_except_table12487
+ GCC_except_table1260
+ GCC_except_table1281
+ GCC_except_table1358
+ GCC_except_table1361
+ GCC_except_table1379
+ GCC_except_table1514
+ GCC_except_table1583
+ GCC_except_table1586
+ GCC_except_table1655
+ GCC_except_table1657
+ GCC_except_table1731
+ GCC_except_table1732
+ GCC_except_table1780
+ GCC_except_table2009
+ GCC_except_table2015
+ GCC_except_table2020
+ GCC_except_table2024
+ GCC_except_table2033
+ GCC_except_table2035
+ GCC_except_table2048
+ GCC_except_table2050
+ GCC_except_table2051
+ GCC_except_table2056
+ GCC_except_table2057
+ GCC_except_table2058
+ GCC_except_table2059
+ GCC_except_table2449
+ GCC_except_table2454
+ GCC_except_table2480
+ GCC_except_table2483
+ GCC_except_table2497
+ GCC_except_table2535
+ GCC_except_table2552
+ GCC_except_table2555
+ GCC_except_table2556
+ GCC_except_table2559
+ GCC_except_table2582
+ GCC_except_table2584
+ GCC_except_table2586
+ GCC_except_table2588
+ GCC_except_table2748
+ GCC_except_table2766
+ GCC_except_table2767
+ GCC_except_table2829
+ GCC_except_table2831
+ GCC_except_table2834
+ GCC_except_table2835
+ GCC_except_table2869
+ GCC_except_table2871
+ GCC_except_table2878
+ GCC_except_table2879
+ GCC_except_table2880
+ GCC_except_table2882
+ GCC_except_table2883
+ GCC_except_table2884
+ GCC_except_table2885
+ GCC_except_table2886
+ GCC_except_table2938
+ GCC_except_table2962
+ GCC_except_table2965
+ GCC_except_table2968
+ GCC_except_table2971
+ GCC_except_table2974
+ GCC_except_table2977
+ GCC_except_table2980
+ GCC_except_table3045
+ GCC_except_table3046
+ GCC_except_table3091
+ GCC_except_table3098
+ GCC_except_table3099
+ GCC_except_table3100
+ GCC_except_table3103
+ GCC_except_table3104
+ GCC_except_table3105
+ GCC_except_table3107
+ GCC_except_table3115
+ GCC_except_table3123
+ GCC_except_table3124
+ GCC_except_table3142
+ GCC_except_table3149
+ GCC_except_table3153
+ GCC_except_table3156
+ GCC_except_table3159
+ GCC_except_table3200
+ GCC_except_table3204
+ GCC_except_table3208
+ GCC_except_table3213
+ GCC_except_table3221
+ GCC_except_table3225
+ GCC_except_table3234
+ GCC_except_table3236
+ GCC_except_table3473
+ GCC_except_table3477
+ GCC_except_table3480
+ GCC_except_table3484
+ GCC_except_table3485
+ GCC_except_table3488
+ GCC_except_table3494
+ GCC_except_table3497
+ GCC_except_table3501
+ GCC_except_table3526
+ GCC_except_table3528
+ GCC_except_table3530
+ GCC_except_table3533
+ GCC_except_table3534
+ GCC_except_table3536
+ GCC_except_table3539
+ GCC_except_table3621
+ GCC_except_table3626
+ GCC_except_table3638
+ GCC_except_table3641
+ GCC_except_table3643
+ GCC_except_table3646
+ GCC_except_table3653
+ GCC_except_table3706
+ GCC_except_table3772
+ GCC_except_table3787
+ GCC_except_table3790
+ GCC_except_table3883
+ GCC_except_table3884
+ GCC_except_table3891
+ GCC_except_table3898
+ GCC_except_table3900
+ GCC_except_table3908
+ GCC_except_table4108
+ GCC_except_table4111
+ GCC_except_table4123
+ GCC_except_table4198
+ GCC_except_table4217
+ GCC_except_table4304
+ GCC_except_table431
+ GCC_except_table436
+ GCC_except_table4407
+ GCC_except_table4412
+ GCC_except_table4413
+ GCC_except_table442
+ GCC_except_table4421
+ GCC_except_table4423
+ GCC_except_table444
+ GCC_except_table4448
+ GCC_except_table4449
+ GCC_except_table4450
+ GCC_except_table446
+ GCC_except_table4511
+ GCC_except_table4521
+ GCC_except_table4586
+ GCC_except_table4588
+ GCC_except_table4590
+ GCC_except_table4632
+ GCC_except_table4633
+ GCC_except_table4705
+ GCC_except_table4792
+ GCC_except_table4793
+ GCC_except_table4799
+ GCC_except_table4801
+ GCC_except_table4830
+ GCC_except_table4832
+ GCC_except_table4851
+ GCC_except_table4897
+ GCC_except_table4947
+ GCC_except_table5033
+ GCC_except_table5053
+ GCC_except_table5054
+ GCC_except_table5055
+ GCC_except_table5057
+ GCC_except_table5061
+ GCC_except_table5063
+ GCC_except_table5277
+ GCC_except_table5283
+ GCC_except_table5285
+ GCC_except_table5295
+ GCC_except_table5296
+ GCC_except_table5543
+ GCC_except_table5651
+ GCC_except_table5657
+ GCC_except_table5664
+ GCC_except_table5669
+ GCC_except_table5752
+ GCC_except_table5758
+ GCC_except_table5760
+ GCC_except_table587
+ GCC_except_table5898
+ GCC_except_table592
+ GCC_except_table595
+ GCC_except_table596
+ GCC_except_table6057
+ GCC_except_table6058
+ GCC_except_table6081
+ GCC_except_table6083
+ GCC_except_table6089
+ GCC_except_table6097
+ GCC_except_table6119
+ GCC_except_table6122
+ GCC_except_table6136
+ GCC_except_table6141
+ GCC_except_table6175
+ GCC_except_table618
+ GCC_except_table6192
+ GCC_except_table6196
+ GCC_except_table6204
+ GCC_except_table6209
+ GCC_except_table6223
+ GCC_except_table6238
+ GCC_except_table6241
+ GCC_except_table6246
+ GCC_except_table6253
+ GCC_except_table6258
+ GCC_except_table6262
+ GCC_except_table6290
+ GCC_except_table6296
+ GCC_except_table6321
+ GCC_except_table6326
+ GCC_except_table6330
+ GCC_except_table635
+ GCC_except_table6359
+ GCC_except_table6361
+ GCC_except_table6362
+ GCC_except_table6497
+ GCC_except_table6503
+ GCC_except_table652
+ GCC_except_table6581
+ GCC_except_table6603
+ GCC_except_table6608
+ GCC_except_table6616
+ GCC_except_table6659
+ GCC_except_table6661
+ GCC_except_table6663
+ GCC_except_table6675
+ GCC_except_table6687
+ GCC_except_table6714
+ GCC_except_table6723
+ GCC_except_table6742
+ GCC_except_table6751
+ GCC_except_table6761
+ GCC_except_table6781
+ GCC_except_table6784
+ GCC_except_table6787
+ GCC_except_table6790
+ GCC_except_table6793
+ GCC_except_table6796
+ GCC_except_table6799
+ GCC_except_table6802
+ GCC_except_table6805
+ GCC_except_table6808
+ GCC_except_table6811
+ GCC_except_table6814
+ GCC_except_table6817
+ GCC_except_table6820
+ GCC_except_table6823
+ GCC_except_table6826
+ GCC_except_table6829
+ GCC_except_table6833
+ GCC_except_table6845
+ GCC_except_table691
+ GCC_except_table694
+ GCC_except_table695
+ GCC_except_table7072
+ GCC_except_table7278
+ GCC_except_table7348
+ GCC_except_table7457
+ GCC_except_table7468
+ GCC_except_table7541
+ GCC_except_table7559
+ GCC_except_table7565
+ GCC_except_table7569
+ GCC_except_table7570
+ GCC_except_table760
+ GCC_except_table763
+ GCC_except_table764
+ GCC_except_table767
+ GCC_except_table769
+ GCC_except_table770
+ GCC_except_table7703
+ GCC_except_table7706
+ GCC_except_table7719
+ GCC_except_table7724
+ GCC_except_table7755
+ GCC_except_table7757
+ GCC_except_table777
+ GCC_except_table7775
+ GCC_except_table778
+ GCC_except_table7783
+ GCC_except_table7785
+ GCC_except_table7787
+ GCC_except_table7789
+ GCC_except_table7796
+ GCC_except_table7802
+ GCC_except_table7806
+ GCC_except_table7807
+ GCC_except_table7816
+ GCC_except_table7872
+ GCC_except_table7874
+ GCC_except_table7882
+ GCC_except_table7884
+ GCC_except_table7886
+ GCC_except_table7888
+ GCC_except_table7890
+ GCC_except_table7896
+ GCC_except_table7900
+ GCC_except_table7912
+ GCC_except_table7914
+ GCC_except_table7916
+ GCC_except_table7918
+ GCC_except_table7937
+ GCC_except_table8089
+ GCC_except_table8091
+ GCC_except_table8095
+ GCC_except_table8096
+ GCC_except_table8097
+ GCC_except_table8136
+ GCC_except_table8143
+ GCC_except_table8144
+ GCC_except_table8188
+ GCC_except_table8189
+ GCC_except_table8190
+ GCC_except_table8198
+ GCC_except_table8200
+ GCC_except_table8262
+ GCC_except_table8263
+ GCC_except_table8264
+ GCC_except_table8301
+ GCC_except_table8483
+ GCC_except_table8484
+ GCC_except_table8485
+ GCC_except_table8489
+ GCC_except_table8544
+ GCC_except_table8565
+ GCC_except_table8636
+ GCC_except_table8642
+ GCC_except_table8644
+ GCC_except_table8646
+ GCC_except_table8648
+ GCC_except_table8656
+ GCC_except_table8706
+ GCC_except_table8708
+ GCC_except_table8733
+ GCC_except_table8761
+ GCC_except_table8919
+ GCC_except_table8971
+ GCC_except_table8978
+ GCC_except_table8983
+ GCC_except_table8988
+ GCC_except_table8992
+ GCC_except_table9011
+ GCC_except_table9013
+ GCC_except_table9043
+ GCC_except_table9063
+ GCC_except_table9064
+ GCC_except_table9065
+ GCC_except_table9102
+ GCC_except_table9103
+ GCC_except_table9107
+ GCC_except_table9109
+ GCC_except_table9111
+ GCC_except_table9170
+ GCC_except_table9200
+ GCC_except_table9202
+ GCC_except_table9204
+ GCC_except_table9206
+ GCC_except_table9208
+ GCC_except_table9214
+ GCC_except_table9216
+ GCC_except_table9222
+ GCC_except_table9229
+ GCC_except_table9236
+ GCC_except_table9240
+ GCC_except_table9246
+ GCC_except_table9255
+ GCC_except_table9263
+ GCC_except_table9264
+ GCC_except_table9277
+ GCC_except_table9287
+ GCC_except_table9491
+ GCC_except_table9504
+ GCC_except_table9553
+ GCC_except_table9554
+ GCC_except_table9556
+ GCC_except_table9560
+ GCC_except_table9624
+ GCC_except_table9627
+ GCC_except_table972
+ GCC_except_table976
+ GCC_except_table983
+ GCC_except_table9939
+ GCC_except_table9978
+ GCC_except_table9991
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo._sfProblemFlags
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._lastKnownControllerHH2Mode
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoSetupInfo._lastKnownControllerSentinelZoneExistence
+ OBJC_IVAR_$_HMProtoResidentCapabilities._supportsActivityLoggingOnPrimary
+ OBJC_IVAR_$_HMProtoResidentCapabilities._supportsResidentActionSetStateEvaluation
+ _CoreAnalyticsLibraryCore.frameworkLibrary.36114
+ _CoreHAPLibrary
+ _CoreHAPLibraryCore.frameworkLibrary.29360
+ _HMAccessoryAudioAnalysisEventBulletinBoardNotificationConditionCodingKey
+ _HMAccessoryAudioAnalysisEventBulletinBoardNotificationEnabledCodingKey
+ _HMAccessoryDisplayableFirmwareVersionCodingKey
+ _HMCameraClipManagerFetchIsCloudStorageEnabledMessage
+ _HMCameraClipManagerMessageKeyIsEnabled
+ _HMCameraClipManagerUpdateCloudStorageMessage
+ _HMCameraSnapshotMostRecentSnapshotUpdatedMessage
+ _HMCharacteristicTypeRouterStatus
+ _HMCharacteristicTypeWANStatusList
+ _HMCharacteristicTypeWiFiSatelliteStatus
+ _HMDaysOfTheWeekForWeekday
+ _HMDaysOfTheWeekToConciseString
+ _HMDeviceSetupFollowupForTVSettingsIdentifier
+ _HMHomeAccessoryAddedMessage
+ _HMHomeKitQAHomeIntegrationBundleIdentifier
+ _HMHomeManagerDataSyncStateToString
+ _HMHomeManagerDeleteHH2EntityMessage
+ _HMHomeManagerDumpStateXPCTransportMessageKey
+ _HMHomeManagerModelIdKey
+ _HMHomeManagerQueryiCloudSwitchStateMessage
+ _HMHomeManagerUpdateiCloudSwitchStateMessage
+ _HMHomeMessageKeyAuthData
+ _HMHomeMessageKeyValue
+ _HMHomeSetResidentSelectionVersionMessage
+ _HMHomeSupportsResidentActionSetStateEvaluationCodingKey
+ _HMHomeUtilBundleIdentifier
+ _HMNetworkRouterWANIdentifierMain
+ _HMResidentDeviceDeviceIRKDataCodingKey
+ _HMServiceConfigurationStateAsString
+ _HMServiceTypeWiFiRouter
+ _HMServiceTypeWiFiSatellite
+ _HMSoftwareUpdateDisplayableVersionCodingKey
+ _IDSFoundationLibraryCore.39694
+ _IDSFoundationLibraryCore.frameworkLibrary.39696
+ _OBJC_CLASS_$_HMFObjectCacheHMSettingLanguageValue
+ _OBJC_CLASS_$_HMNetworkRouterWANStatus
+ _OBJC_CLASS_$_HMNetworkRouterWANStatusList
+ _OBJC_IVAR_$_HMBulletinBoardNotification._messageTargetUUID
+ _OBJC_IVAR_$_HMCameraClipManager._delegateCallersByObservers
+ _OBJC_IVAR_$_HMCameraRecordingEventManager._delegateCallersByObservers
+ _OBJC_IVAR_$_HMCameraRecordingReachabilityEventManager._delegateCallersByObservers
+ _OBJC_IVAR_$_HMHome._supportsResidentActionSetStateEvaluation
+ _OBJC_IVAR_$_HMHomeManager._initialMergeComplete
+ _OBJC_IVAR_$_HMNetworkRouterWANStatus._identifier
+ _OBJC_IVAR_$_HMNetworkRouterWANStatus._status
+ _OBJC_IVAR_$_HMNetworkRouterWANStatusList._statuses
+ _OBJC_IVAR_$_HMResidentDevice._IDSDestination
+ _OBJC_IVAR_$_HMResidentDevice._IDSIdentifier
+ _OBJC_IVAR_$_HMResidentDevice._deviceIRKData
+ _OBJC_IVAR_$_HMService._matterEndpointID
+ _OBJC_IVAR_$_HMSoftwareUpdate._displayableVersion
+ _OBJC_IVAR_$__HMCameraProfile._snapshotControl
+ _OBJC_IVAR_$__HMCameraProfile._streamControl
+ _OBJC_METACLASS_$_HMFObjectCacheHMSettingLanguageValue
+ _OBJC_METACLASS_$_HMNetworkRouterWANStatus
+ _OBJC_METACLASS_$_HMNetworkRouterWANStatusList
+ _TLV8BufferAppend
+ _TLV8BufferFree
+ _TLV8BufferInit
+ _TLV8GetNext
+ _TLV8GetOrCopyCoalesced
+ _UIKitLibrary.39925
+ _UIKitLibraryCore.39921
+ _UIKitLibraryCore.frameworkLibrary.39934
+ __HMErrorFromOSStatus
+ __HMFPreconditionFailureWithFormat
+ __OBJC_$_CLASS_METHODS_HMAccessory(SiriEndpoint|Television|WoL|LightInternal|NetworkRouter|NetworkRouterInternal|Private|PendingConfiguration|CUPeerIdentifier|Shortcuts|Camera|CHIP|NetworkConfiguration|Light|Media)
+ __OBJC_$_CLASS_METHODS_HMFObjectCacheHMSettingLanguageValue
+ __OBJC_$_CLASS_METHODS_HMNetworkRouterWANStatus
+ __OBJC_$_CLASS_METHODS_HMNetworkRouterWANStatusList
+ __OBJC_$_INSTANCE_METHODS_HMAccessory(SiriEndpoint|Television|WoL|LightInternal|NetworkRouter|NetworkRouterInternal|Private|PendingConfiguration|CUPeerIdentifier|Shortcuts|Camera|CHIP|NetworkConfiguration|Light|Media)
+ __OBJC_$_INSTANCE_METHODS_HMNetworkRouterWANStatus
+ __OBJC_$_INSTANCE_METHODS_HMNetworkRouterWANStatusList
+ __OBJC_$_INSTANCE_VARIABLES_HMNetworkRouterWANStatus
+ __OBJC_$_INSTANCE_VARIABLES_HMNetworkRouterWANStatusList
+ __OBJC_$_PROP_LIST_HMAccessoryCapabilities.134
+ __OBJC_$_PROP_LIST_HMActionSetBuilder.149
+ __OBJC_$_PROP_LIST_HMApplicationData.11377
+ __OBJC_$_PROP_LIST_HMCache.100
+ __OBJC_$_PROP_LIST_HMEventTriggerBuilder.215
+ __OBJC_$_PROP_LIST_HMHAPMetadataCategory.89
+ __OBJC_$_PROP_LIST_HMHAPMetadataCharacteristic.59
+ __OBJC_$_PROP_LIST_HMHAPMetadataService.69
+ __OBJC_$_PROP_LIST_HMMediaDestination.265
+ __OBJC_$_PROP_LIST_HMNetworkRouterWANStatus
+ __OBJC_$_PROP_LIST_HMNetworkRouterWANStatusList
+ __OBJC_$_PROP_LIST_HMResidentCapabilities.198
+ __OBJC_$_PROP_LIST_HMTimerTriggerBuilder.201
+ __OBJC_$_PROP_LIST_HMTriggerBuilder.179
+ __OBJC_$_PROP_LIST__HMNetworkConnection.97
+ __OBJC_$_PROP_LIST__HMNetworkPath.59
+ __OBJC_$_PROP_LIST__HMPrivacySettingsProvider.52
+ __OBJC_CLASS_PROTOCOLS_$_HMAudioAnalysisEventBulletinBoardNotification
+ __OBJC_CLASS_PROTOCOLS_$_HMCameraBulletinBoardSmartNotification
+ __OBJC_CLASS_PROTOCOLS_$_HMNetworkRouterWANStatus
+ __OBJC_CLASS_PROTOCOLS_$_HMNetworkRouterWANStatusList
+ __OBJC_CLASS_PROTOCOLS_$_HMSettingLanguageValue
+ __OBJC_CLASS_RO_$_HMFObjectCacheHMSettingLanguageValue
+ __OBJC_CLASS_RO_$_HMNetworkRouterWANStatus
+ __OBJC_CLASS_RO_$_HMNetworkRouterWANStatusList
+ __OBJC_METACLASS_RO_$_HMFObjectCacheHMSettingLanguageValue
+ __OBJC_METACLASS_RO_$_HMNetworkRouterWANStatus
+ __OBJC_METACLASS_RO_$_HMNetworkRouterWANStatusList
+ ___107-[HMCameraRecordingEventManager fetchEventsWithDateInterval:quality:limit:shouldOrderAscending:completion:]_block_invoke.12
+ ___111-[HMCameraRecordingReachabilityEventManager fetchEventsWithDateInterval:limit:shouldOrderAscending:completion:]_block_invoke.68
+ ___111-[HMCameraRecordingReachabilityEventManager fetchEventsWithDateInterval:limit:shouldOrderAscending:completion:]_block_invoke.72
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.777
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.779
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.780
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.783
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.787
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.789
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.782
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.785
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.788
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.790
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_3.786
+ ___140-[HMHomeManager readCountersForGroup:homeUUIDString:accessoryUUIDString:counter:statistics:datePartition:ephemeralContainerName:completion:]_block_invoke
+ ___140-[HMHomeManager readCountersForGroup:homeUUIDString:accessoryUUIDString:counter:statistics:datePartition:ephemeralContainerName:completion:]_block_invoke_2
+ ___22-[HMHome _mergeRooms:]_block_invoke.762
+ ___22-[HMHome _mergeRooms:]_block_invoke.763
+ ___22-[HMHome _mergeRooms:]_block_invoke.765
+ ___22-[HMHome _mergeRooms:]_block_invoke_2.767
+ ___22-[HMHome _mergeRooms:]_block_invoke_3.768
+ ___22-[HMHome _mergeUsers:]_block_invoke.808
+ ___22-[HMHome _mergeUsers:]_block_invoke.809
+ ___22-[HMHome _mergeUsers:]_block_invoke.811
+ ___22-[HMHome _mergeUsers:]_block_invoke_2.813
+ ___22-[HMHome _mergeUsers:]_block_invoke_3.814
+ ___22-[HMHome _mergeZones:]_block_invoke.770
+ ___22-[HMHome _mergeZones:]_block_invoke.771
+ ___22-[HMHome _mergeZones:]_block_invoke.773
+ ___22-[HMHome _mergeZones:]_block_invoke_2.775
+ ___22-[HMHome _mergeZones:]_block_invoke_3.776
+ ___25-[HMHome _mergeTriggers:]_block_invoke.804
+ ___25-[HMHome _mergeTriggers:]_block_invoke.806
+ ___25-[HMXPCClient connection]_block_invoke.77
+ ___25-[HMXPCClient connection]_block_invoke.81
+ ___27-[HMHome _mergeActionSets:]_block_invoke.795
+ ___27-[HMHome _mergeActionSets:]_block_invoke.796
+ ___27-[HMHome _mergeActionSets:]_block_invoke.798
+ ___27-[HMHome _mergeActionSets:]_block_invoke_2.800
+ ___27-[HMHome _mergeActionSets:]_block_invoke_3.801
+ ___28-[HMHome _mergeAccessories:]_block_invoke.778
+ ___28-[HMHome _mergeAccessories:]_block_invoke.779
+ ___28-[HMHome _mergeAccessories:]_block_invoke.781
+ ___28-[HMHome _mergeAccessories:]_block_invoke.782
+ ___28-[HMHome _mergeAccessories:]_block_invoke.784
+ ___28-[HMHome _mergeAccessories:]_block_invoke_2.785
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.547
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.551
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.557
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.561
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.565
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.577
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.581
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.585
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.589
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.741
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.744
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.752
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.755
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.758
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.548
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.552
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.558
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.562
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.566
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.578
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.582
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.586
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.590
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.742
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.745
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.753
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.756
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.759
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_3.747
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_4.748
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_5.749
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_6.750
+ ___29-[HMUser mergeFromNewObject:]_block_invoke.297
+ ___29-[HMUser mergeFromNewObject:]_block_invoke.300
+ ___29-[HMUser mergeFromNewObject:]_block_invoke.302
+ ___29-[HMUser mergeFromNewObject:]_block_invoke.305
+ ___29-[HMUser mergeFromNewObject:]_block_invoke.308
+ ___29-[HMUser mergeFromNewObject:]_block_invoke.311
+ ___29-[HMUser mergeFromNewObject:]_block_invoke.314
+ ___29-[HMUser mergeFromNewObject:]_block_invoke_2.298
+ ___29-[HMUser mergeFromNewObject:]_block_invoke_2.301
+ ___29-[HMUser mergeFromNewObject:]_block_invoke_2.303
+ ___29-[HMUser mergeFromNewObject:]_block_invoke_2.306
+ ___29-[HMUser mergeFromNewObject:]_block_invoke_2.309
+ ___29-[HMUser mergeFromNewObject:]_block_invoke_2.312
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke.1108
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke.1109
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke.1111
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke.1115
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke_2.1113
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke_2.1116
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke_3.1114
+ ___30-[HMAccessory _mergeServices:]_block_invoke.926
+ ___30-[HMAccessory _mergeServices:]_block_invoke.928
+ ___30-[HMHome _mergeServiceGroups:]_block_invoke.787
+ ___30-[HMHome _mergeServiceGroups:]_block_invoke.788
+ ___30-[HMHome _mergeServiceGroups:]_block_invoke.790
+ ___30-[HMHome _mergeServiceGroups:]_block_invoke_2.792
+ ___30-[HMHome _mergeServiceGroups:]_block_invoke_3.793
+ ___32-[HMHome _mergeResidentDevices:]_block_invoke.816
+ ___32-[HMHome _mergeResidentDevices:]_block_invoke.817
+ ___32-[HMHome _mergeResidentDevices:]_block_invoke.819
+ ___32-[HMHome _mergeResidentDevices:]_block_invoke_2.821
+ ___32-[HMHome _mergeResidentDevices:]_block_invoke_3.822
+ ___32-[HMService mergeFromNewObject:]_block_invoke.176
+ ___32-[HMService mergeFromNewObject:]_block_invoke.179
+ ___32-[HMService mergeFromNewObject:]_block_invoke.302
+ ___32-[HMService mergeFromNewObject:]_block_invoke.304
+ ___32-[HMService mergeFromNewObject:]_block_invoke.306
+ ___32-[HMService mergeFromNewObject:]_block_invoke.308
+ ___32-[HMService mergeFromNewObject:]_block_invoke.310
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1084
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1086
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1098
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1099
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1100
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1101
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1103
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1105
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1106
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.930
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.931
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.950
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.953
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.955
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.962
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.966
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1085
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1087
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1092
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1104
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.932
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.951
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.954
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.956
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.963
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.967
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_3.964
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_3.969
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_4.970
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_5.971
+ ___34-[HMHomeManager _setInitialHomes:]_block_invoke
+ ___36-[HMHome _mergeOutgoingInvitations:]_block_invoke.824
+ ___36-[HMHome _mergeOutgoingInvitations:]_block_invoke.826
+ ___37-[HMEventTrigger mergeFromNewObject:]_block_invoke.147
+ ___37-[HMEventTrigger mergeFromNewObject:]_block_invoke.148
+ ___38-[HMHomeManager _updateDataSyncState:]_block_invoke.529
+ ___39-[HMHome _mergeTriggerOwnedActionSets:]_block_invoke.802
+ ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.792
+ ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.794
+ ___39-[HMResidentDevice mergeFromNewObject:]_block_invoke.160
+ ___39-[HMResidentDevice mergeFromNewObject:]_block_invoke_2.161
+ ___39-[HMSoftwareUpdate mergeFromNewObject:]_block_invoke.173
+ ___39-[HMSoftwareUpdate mergeFromNewObject:]_block_invoke.175
+ ___39-[HMSoftwareUpdate mergeFromNewObject:]_block_invoke_2.174
+ ___39-[HMSoftwareUpdate mergeFromNewObject:]_block_invoke_2.176
+ ___40-[HMHome confirmResidentWithCompletion:]_block_invoke
+ ___40-[HMHome confirmResidentWithCompletion:]_block_invoke_2
+ ___40-[HMHome confirmResidentWithCompletion:]_block_invoke_3
+ ___40-[HMSoftwareUpdate requestDocumentation]_block_invoke.161
+ ___41-[HMAccessory _updateHasSymptomsHandler:]_block_invoke.1143
+ ___41-[HMAccessory _updateHasSymptomsHandler:]_block_invoke.1145
+ ___42-[HMActionSet _removeActionsForAccessory:]_block_invoke
+ ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke.828
+ ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke.829
+ ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke.830
+ ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke.831
+ ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke.833
+ ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke_2.832
+ ___43-[HMHome fetchPresenceForUsers:completion:]_block_invoke.842
+ ___43-[HMHome fetchPresenceForUsers:completion:]_block_invoke.844
+ ___44-[HMEventTrigger _removeEventsForAccessory:]_block_invoke
+ ___44-[HMHome _handleAccessoryAddedNotification:]_block_invoke.913
+ ___44-[HMUser _mergeWithNewAccessoryInvitations:]_block_invoke.294
+ ___45-[HMAccessory _handleCharacteristicsUpdated:]_block_invoke.1129
+ ___45-[HMResidentDevice handleRuntimeStateUpdate:]_block_invoke.162
+ ___45-[HMResidentDevice handleRuntimeStateUpdate:]_block_invoke.163
+ ___45-[HMResidentDevice handleRuntimeStateUpdate:]_block_invoke.164
+ ___45-[HMXPCClient sendMessage:completionHandler:]_block_invoke.87
+ ___47-[HMHomeManager _recomputeAssistantIdentifiers]_block_invoke.701
+ ___48-[HMAccessory _deleteSiriHistoryWithCompletion:]_block_invoke.1130
+ ___48-[HMAccessory _deleteSiriHistoryWithCompletion:]_block_invoke.1131
+ ___49-[_HMCameraStreamControl __configureWithContext:]_block_invoke
+ ___50-[HMSoftwareUpdate updateState:completionHandler:]_block_invoke.150
+ ___50-[HMSoftwareUpdate updateState:completionHandler:]_block_invoke.152
+ ___51-[HMHomeManager _updatePrimaryHome:notifyDelegate:]_block_invoke.761
+ ___52-[HMCameraClipManager fetchClipWithUUID:completion:]_block_invoke.157
+ ___52-[HMCameraClipManager fetchClipWithUUID:completion:]_block_invoke.160
+ ___52-[HMHome updateResidentSelectionVersion:completion:]_block_invoke
+ ___52-[HMHome updateResidentSelectionVersion:completion:]_block_invoke_2
+ ___52-[HMHome(HMUser) _manageUsersWithCompletionHandler:]_block_invoke.1728
+ ___52-[HMSoftwareUpdateDocumentationAsset startUnarchive]_block_invoke.127
+ ___53+[HMCameraBulletinBoardSmartNotification logCategory]_block_invoke
+ ___53-[HMMediaProfile mediaProfile:didUpdateMediaSession:]_block_invoke.68
+ ___54-[HMEventTrigger mergeFromNewObjectForBuilderUpdates:]_block_invoke.151
+ ___54-[HMHome _notifyDelegateOfAccessControlUpdateForUser:]_block_invoke.946
+ ___54-[HMHomeManager _refreshBeforeDate:completionHandler:]_block_invoke.623
+ ___54-[HMHomeManager _refreshBeforeDate:completionHandler:]_block_invoke.624
+ ___55-[HMAccessory notifyDelegateOfAppDataUpdateForService:]_block_invoke_2
+ ___57-[HMCameraClipManager setCloudStorageEnabled:completion:]_block_invoke
+ ___58-[HMHomeManager __resolveAccountHandle:completionHandler:]_block_invoke.688
+ ___58-[HMHomeManager addEphemeralContainerWithName:completion:]_block_invoke
+ ___58-[HMHomeManager addEphemeralContainerWithName:completion:]_block_invoke_2
+ ___60+[HMAudioAnalysisEventBulletinBoardNotification logCategory]_block_invoke
+ ___61-[HMHomeManager __removeAccountWithHandle:completionHandler:]_block_invoke.690
+ ___61-[HMHomeManager deleteEphemeralContainerWithName:completion:]_block_invoke
+ ___61-[HMHomeManager deleteEphemeralContainerWithName:completion:]_block_invoke_2
+ ___62-[HMHomeManager startupEphemeralContainerWithName:completion:]_block_invoke
+ ___62-[HMHomeManager startupEphemeralContainerWithName:completion:]_block_invoke_2
+ ___62-[HMOutgoingHomeInvitation _mergeWithNewAccessoryInvitations:]_block_invoke.132
+ ___63-[HMAccessory pairingIdentityWithPrivateKey:completionHandler:]_block_invoke.865
+ ___63-[HMAccessory pairingIdentityWithPrivateKey:completionHandler:]_block_invoke.867
+ ___63-[HMUser updateAnnounceUserSettings:forHome:completionHandler:]_block_invoke.219
+ ___64-[HMCameraClipManager fetchIsCloudStorageEnabledWithCompletion:]_block_invoke
+ ___64-[HMHome(HMMediaProfile) updateMediaPassword:completionHandler:]_block_invoke.1806
+ ___65-[HMHomeManager __removeAccountWithIdentifier:completionHandler:]_block_invoke.689
+ ___65-[HMHomeManager deactivateEphemeralContainerWithName:completion:]_block_invoke
+ ___65-[HMHomeManager deactivateEphemeralContainerWithName:completion:]_block_invoke_2
+ ___66-[HMCameraClipManager fetchHeroFrameURLOfClipWithUUID:completion:]_block_invoke.183
+ ___66-[HMCameraClipManager fetchHeroFrameURLOfClipWithUUID:completion:]_block_invoke.185
+ ___66-[HMCameraClipManager fetchSignificantEventsWithUUIDs:completion:]_block_invoke.200
+ ___66-[HMSoftwareUpdate updateDocumentationMetadata:completionHandler:]_block_invoke.160
+ ___67-[HMHome _addEventTriggerFromResponse:withEventTrigger:completion:]_block_invoke.906
+ ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke
+ ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.719
+ ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.723
+ ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.725
+ ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.727
+ ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke_2
+ ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke_2.728
+ ___69-[HMHomeManager addAndSetupAccessoriesWithPayload:completionHandler:]_block_invoke.845
+ ___71-[HMCameraClipManager fetchClipForSignificantEventWithUUID:completion:]_block_invoke.162
+ ___71-[HMCameraClipManager fetchClipForSignificantEventWithUUID:completion:]_block_invoke.163
+ ___72-[HMCameraClipManager fetchVideoSegmentsAssetContextForClip:completion:]_block_invoke.226
+ ___72-[HMCameraClipManager fetchVideoSegmentsAssetContextForClip:completion:]_block_invoke.227
+ ___72-[HMCameraClipManager fetchVideoSegmentsAssetContextForClip:completion:]_block_invoke.230
+ ___74-[HMHomeManager __processSyncResponse:refreshRequested:completionHandler:]_block_invoke.698
+ ___75-[HMHome(HMAccessory) addAndSetupAccessoriesWithPayload:completionHandler:]_block_invoke.1591
+ ___75-[HMUser updateMediaContentProfileAccessControl:forHome:completionHandler:]_block_invoke.221
+ ___76-[HMCameraClipManager fetchCountOfClipsWithDateInterval:quality:completion:]_block_invoke.173
+ ___76-[HMCameraClipManager fetchCountOfClipsWithDateInterval:quality:completion:]_block_invoke.174
+ ___76-[HMUser updateUserListeningHistoryUpdateControl:forHome:completionHandler:]_block_invoke.223
+ ___77-[HMAudioAnalysisEventBulletinBoardNotification commitWithCompletionHandler:]_block_invoke.20
+ ___77-[HMAudioAnalysisEventBulletinBoardNotification commitWithCompletionHandler:]_block_invoke.22
+ ___78-[HMCameraClipManager fetchFaceCropURLForSignificantEventWithUUID:completion:]_block_invoke.194
+ ___78-[HMCameraClipManager fetchFaceCropURLForSignificantEventWithUUID:completion:]_block_invoke.195
+ ___79-[HMCameraRecordingEventManager fetchCountOfEventsWithDateInterval:completion:]_block_invoke.20
+ ___82-[HMCameraClipManager fetchHeroFrameDataRepresentationForClipWithUUID:completion:]_block_invoke.178
+ ___82-[HMCameraClipManager fetchHeroFrameDataRepresentationForClipWithUUID:completion:]_block_invoke.179
+ ___82-[HMCameraRecordingReachabilityEventManager deleteAllEventsWithCompletionHandler:]_block_invoke.82
+ ___84+[HMAccessory(NetworkRouter) networkRouterStatusFromRouterStatus:wanStatusListData:]_block_invoke
+ ___88-[HMHome(HMAccessory) addAccessoryWithAccessorySetupPayload:progress:completionHandler:]_block_invoke.1602
+ ___88-[HMHome(HMAccessory) addAndSetUpNewAccessoriesWithSuggestedRoomName:completionHandler:]_block_invoke.1593
+ ___88-[HMHome(HomeLocationFeedback) retrieveHomeKitLocationForFeedbackWithCompletionHandler:]_block_invoke.1891
+ ___89-[HMHome(NetworkRouter) updateAccessoryNetworkProtectionGroup:protectionMode:completion:]_block_invoke.1861
+ ___91-[HMCameraRecordingReachabilityEventManager fetchCountOfEventsWithDateInterval:completion:]_block_invoke.81
+ ___93-[HMCameraClipManager fetchFaceCropDataRepresentationForSignificantEventWithUUID:completion:]_block_invoke.189
+ ___93-[HMCameraClipManager fetchFaceCropDataRepresentationForSignificantEventWithUUID:completion:]_block_invoke.190
+ ___93-[HMHomeManager _pingDeviceWithUUID:monitor:secure:restrictToLocalNetwork:completionHandler:]_block_invoke.691
+ ___Block_byref_object_copy_.14411
+ ___Block_byref_object_copy_.14722
+ ___Block_byref_object_copy_.21439
+ ___Block_byref_object_copy_.23537
+ ___Block_byref_object_copy_.27702
+ ___Block_byref_object_copy_.29449
+ ___Block_byref_object_copy_.36001
+ ___Block_byref_object_copy_.38874
+ ___Block_byref_object_copy_.60100
+ ___Block_byref_object_dispose_.14412
+ ___Block_byref_object_dispose_.14723
+ ___Block_byref_object_dispose_.21440
+ ___Block_byref_object_dispose_.23538
+ ___Block_byref_object_dispose_.27703
+ ___Block_byref_object_dispose_.29450
+ ___Block_byref_object_dispose_.36002
+ ___Block_byref_object_dispose_.38875
+ ___Block_byref_object_dispose_.60101
+ ___CoreAnalyticsLibraryCore_block_invoke.36115
+ ___CoreHAPLibraryCore_block_invoke.29361
+ ___IDSFoundationLibraryCore_block_invoke.39697
+ ___UIKitLibraryCore_block_invoke.39935
+ _____HMHomeManagerRegisterForNotifications_block_invoke.1399
+ _____processNextArchivedData_block_invoke.308
+ _____requestFetch_block_invoke.159
+ ___block_descriptor_40_e41_B32?0"HMNetworkRouterWANStatus"8Q16^B24l
+ ___block_descriptor_65_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_literal_global.101.36122
+ ___block_literal_global.10283
+ ___block_literal_global.104
+ ___block_literal_global.1124
+ ___block_literal_global.11310
+ ___block_literal_global.11438
+ ___block_literal_global.1180
+ ___block_literal_global.12.45718
+ ___block_literal_global.121.48665
+ ___block_literal_global.12414
+ ___block_literal_global.12554
+ ___block_literal_global.12626
+ ___block_literal_global.13081
+ ___block_literal_global.13275
+ ___block_literal_global.13840
+ ___block_literal_global.14175
+ ___block_literal_global.14493
+ ___block_literal_global.15089
+ ___block_literal_global.153
+ ___block_literal_global.16
+ ___block_literal_global.1610
+ ___block_literal_global.16191
+ ___block_literal_global.16723
+ ___block_literal_global.16916
+ ___block_literal_global.17.17849
+ ___block_literal_global.17049
+ ___block_literal_global.1716
+ ___block_literal_global.17210
+ ___block_literal_global.177
+ ___block_literal_global.178
+ ___block_literal_global.17856
+ ___block_literal_global.1803
+ ___block_literal_global.18511
+ ___block_literal_global.18916
+ ___block_literal_global.19.14160
+ ___block_literal_global.193
+ ___block_literal_global.19469
+ ___block_literal_global.19808
+ ___block_literal_global.20820
+ ___block_literal_global.212
+ ___block_literal_global.21477
+ ___block_literal_global.21750
+ ___block_literal_global.2177
+ ___block_literal_global.22223
+ ___block_literal_global.22440
+ ___block_literal_global.22773
+ ___block_literal_global.22904
+ ___block_literal_global.23152
+ ___block_literal_global.23402
+ ___block_literal_global.23561
+ ___block_literal_global.23654
+ ___block_literal_global.241
+ ___block_literal_global.249
+ ___block_literal_global.26194
+ ___block_literal_global.26327
+ ___block_literal_global.267
+ ___block_literal_global.26803
+ ___block_literal_global.27562
+ ___block_literal_global.27859
+ ___block_literal_global.28208
+ ___block_literal_global.28412
+ ___block_literal_global.28693
+ ___block_literal_global.28769
+ ___block_literal_global.29658
+ ___block_literal_global.30.17839
+ ___block_literal_global.30.7684
+ ___block_literal_global.30011
+ ___block_literal_global.30283
+ ___block_literal_global.31127
+ ___block_literal_global.31498
+ ___block_literal_global.32589
+ ___block_literal_global.33.59440
+ ___block_literal_global.33504
+ ___block_literal_global.336
+ ___block_literal_global.33736
+ ___block_literal_global.33961
+ ___block_literal_global.34913
+ ___block_literal_global.3544
+ ___block_literal_global.36
+ ___block_literal_global.36109
+ ___block_literal_global.36357
+ ___block_literal_global.36699
+ ___block_literal_global.37329
+ ___block_literal_global.3747
+ ___block_literal_global.38140
+ ___block_literal_global.38267
+ ___block_literal_global.3839
+ ___block_literal_global.38545
+ ___block_literal_global.39758
+ ___block_literal_global.39853
+ ___block_literal_global.40563
+ ___block_literal_global.40753
+ ___block_literal_global.41374
+ ___block_literal_global.42000
+ ___block_literal_global.42441
+ ___block_literal_global.42760
+ ___block_literal_global.43437
+ ___block_literal_global.442
+ ___block_literal_global.44325
+ ___block_literal_global.45439
+ ___block_literal_global.45730
+ ___block_literal_global.45996
+ ___block_literal_global.46191
+ ___block_literal_global.46420
+ ___block_literal_global.47129
+ ___block_literal_global.47249
+ ___block_literal_global.478
+ ___block_literal_global.47983
+ ___block_literal_global.48.46480
+ ___block_literal_global.48419
+ ___block_literal_global.48752
+ ___block_literal_global.49666
+ ___block_literal_global.5019
+ ___block_literal_global.510
+ ___block_literal_global.515
+ ___block_literal_global.52231
+ ___block_literal_global.52939
+ ___block_literal_global.54207
+ ___block_literal_global.5457
+ ___block_literal_global.54890
+ ___block_literal_global.55422
+ ___block_literal_global.55734
+ ___block_literal_global.5591
+ ___block_literal_global.56249
+ ___block_literal_global.56426
+ ___block_literal_global.56792
+ ___block_literal_global.57032
+ ___block_literal_global.58674
+ ___block_literal_global.58842
+ ___block_literal_global.59180
+ ___block_literal_global.59446
+ ___block_literal_global.59808
+ ___block_literal_global.60098
+ ___block_literal_global.60393
+ ___block_literal_global.6137
+ ___block_literal_global.630
+ ___block_literal_global.6621
+ ___block_literal_global.6900
+ ___block_literal_global.73.21728
+ ___block_literal_global.73.36692
+ ___block_literal_global.7351
+ ___block_literal_global.740
+ ___block_literal_global.742
+ ___block_literal_global.7468
+ ___block_literal_global.76.25963
+ ___block_literal_global.7702
+ ___block_literal_global.8165
+ ___block_literal_global.844
+ ___block_literal_global.849
+ ___block_literal_global.86
+ ___block_literal_global.8700
+ ___block_literal_global.8981
+ ___block_literal_global.9
+ ___block_literal_global.911
+ ___block_literal_global.9157
+ ___block_literal_global.9585
+ ___block_literal_global.977
+ ___block_literal_global.979
+ ___block_literal_global.982
+ ___getAnalyticsSendEventLazySymbolLoc_block_invoke.36112
+ ___getHAPTLVUnsignedNumberValueClass_block_invoke
+ ___getHMErrorFromOSStatusSymbolLoc_block_invoke
+ ___getNSCharacterEncodingDocumentAttributeSymbolLoc_block_invoke.39930
+ ___getNSDocumentTypeDocumentAttributeSymbolLoc_block_invoke.39924
+ __dictionaryRepresentationForReportContext
+ __unnamed_array_storage.140
+ __unnamed_array_storage.14428
+ __unnamed_array_storage.222
+ __unnamed_array_storage.226
+ __unnamed_array_storage.22665
+ __unnamed_array_storage.227.26110
+ __unnamed_array_storage.230
+ __unnamed_array_storage.234
+ __unnamed_array_storage.238
+ __unnamed_array_storage.239.26109
+ __unnamed_array_storage.242
+ __unnamed_array_storage.246
+ __unnamed_array_storage.250
+ __unnamed_array_storage.251.26113
+ __unnamed_array_storage.254.26108
+ __unnamed_array_storage.258
+ __unnamed_array_storage.26184
+ __unnamed_array_storage.262
+ __unnamed_array_storage.266
+ __unnamed_array_storage.270
+ __unnamed_array_storage.274
+ __unnamed_array_storage.278
+ __unnamed_array_storage.282
+ __unnamed_array_storage.286
+ __unnamed_array_storage.290
+ __unnamed_array_storage.29359
+ __unnamed_array_storage.294
+ __unnamed_array_storage.298
+ __unnamed_array_storage.302
+ __unnamed_array_storage.306
+ __unnamed_array_storage.310
+ __unnamed_array_storage.311
+ __unnamed_array_storage.317
+ __unnamed_array_storage.318
+ __unnamed_array_storage.330
+ __unnamed_array_storage.334
+ __unnamed_array_storage.338
+ __unnamed_array_storage.342
+ __unnamed_array_storage.346
+ __unnamed_array_storage.350
+ __unnamed_array_storage.354
+ __unnamed_array_storage.358
+ __unnamed_array_storage.362
+ __unnamed_array_storage.366
+ __unnamed_array_storage.370
+ __unnamed_array_storage.374
+ __unnamed_array_storage.378
+ __unnamed_array_storage.382
+ __unnamed_array_storage.386
+ __unnamed_array_storage.390
+ __unnamed_array_storage.394
+ __unnamed_array_storage.398
+ __unnamed_array_storage.402
+ __unnamed_array_storage.406
+ __unnamed_array_storage.410
+ __unnamed_array_storage.414
+ __unnamed_array_storage.418
+ __unnamed_array_storage.419
+ __unnamed_array_storage.54327
+ __unnamed_array_storage.55860
+ __unnamed_array_storage.59296
+ _audit_stringCoreAnalytics.36118
+ _audit_stringCoreHAP.29363
+ _audit_stringIDSFoundation.39699
+ _audit_stringUIKit.39937
+ _cachedInstanceForLanguageSettingValue:.cachedInstances
+ _cachedInstanceForLanguageSettingValue:.lock
+ _getAnalyticsSendEventLazySymbolLoc.ptr.36111
+ _getHAPTLVUnsignedNumberValueClass
+ _getHAPTLVUnsignedNumberValueClass.softClass
+ _getHMErrorFromOSStatusSymbolLoc.ptr
+ _getNSCharacterEncodingDocumentAttributeSymbolLoc.ptr.39929
+ _getNSDocumentTypeDocumentAttributeSymbolLoc.ptr.39923
+ _logCategory._hmf_once_t0.12625
+ _logCategory._hmf_once_t0.21749
+ _logCategory._hmf_once_t0.28411
+ _logCategory._hmf_once_t0.28768
+ _logCategory._hmf_once_t0.40562
+ _logCategory._hmf_once_t0.40752
+ _logCategory._hmf_once_t0.41373
+ _logCategory._hmf_once_t0.57031
+ _logCategory._hmf_once_t1.17048
+ _logCategory._hmf_once_t1.18915
+ _logCategory._hmf_once_t1.36333
+ _logCategory._hmf_once_t1.41999
+ _logCategory._hmf_once_t1.45717
+ _logCategory._hmf_once_t1.47248
+ _logCategory._hmf_once_t1.52230
+ _logCategory._hmf_once_t11
+ _logCategory._hmf_once_t14.56791
+ _logCategory._hmf_once_t16.33735
+ _logCategory._hmf_once_t16.58841
+ _logCategory._hmf_once_t17.38132
+ _logCategory._hmf_once_t19.13301
+ _logCategory._hmf_once_t2.26326
+ _logCategory._hmf_once_t2.30010
+ _logCategory._hmf_once_t20.5590
+ _logCategory._hmf_once_t22.23151
+ _logCategory._hmf_once_t24.36691
+ _logCategory._hmf_once_t25.59807
+ _logCategory._hmf_once_t26.48499
+ _logCategory._hmf_once_t27.47982
+ _logCategory._hmf_once_t27.55733
+ _logCategory._hmf_once_t3.38266
+ _logCategory._hmf_once_t3.59439
+ _logCategory._hmf_once_t31.21476
+ _logCategory._hmf_once_t31.58673
+ _logCategory._hmf_once_t315
+ _logCategory._hmf_once_t33.48775
+ _logCategory._hmf_once_t335
+ _logCategory._hmf_once_t337
+ _logCategory._hmf_once_t34.18510
+ _logCategory._hmf_once_t35.34912
+ _logCategory._hmf_once_t38.7718
+ _logCategory._hmf_once_t4.1191
+ _logCategory._hmf_once_t4.5456
+ _logCategory._hmf_once_t42.54889
+ _logCategory._hmf_once_t5.16722
+ _logCategory._hmf_once_t6.31126
+ _logCategory._hmf_once_t6.33503
+ _logCategory._hmf_once_t6.52938
+ _logCategory._hmf_once_t64.54206
+ _logCategory._hmf_once_t7.23653
+ _logCategory._hmf_once_t7.47128
+ _logCategory._hmf_once_t74
+ _logCategory._hmf_once_t8.33960
+ _logCategory._hmf_once_t8.43436
+ _logCategory._hmf_once_t8.46209
+ _logCategory._hmf_once_v1.12627
+ _logCategory._hmf_once_v1.21751
+ _logCategory._hmf_once_v1.28413
+ _logCategory._hmf_once_v1.28770
+ _logCategory._hmf_once_v1.40564
+ _logCategory._hmf_once_v1.40754
+ _logCategory._hmf_once_v1.41375
+ _logCategory._hmf_once_v1.57033
+ _logCategory._hmf_once_v12
+ _logCategory._hmf_once_v15.56793
+ _logCategory._hmf_once_v17.33737
+ _logCategory._hmf_once_v17.58843
+ _logCategory._hmf_once_v18.38133
+ _logCategory._hmf_once_v2.17050
+ _logCategory._hmf_once_v2.18917
+ _logCategory._hmf_once_v2.36334
+ _logCategory._hmf_once_v2.42001
+ _logCategory._hmf_once_v2.45719
+ _logCategory._hmf_once_v2.47250
+ _logCategory._hmf_once_v2.52232
+ _logCategory._hmf_once_v20.13302
+ _logCategory._hmf_once_v21.5592
+ _logCategory._hmf_once_v23.23153
+ _logCategory._hmf_once_v25.36693
+ _logCategory._hmf_once_v26.59809
+ _logCategory._hmf_once_v27.48500
+ _logCategory._hmf_once_v28.47984
+ _logCategory._hmf_once_v28.55735
+ _logCategory._hmf_once_v3.26328
+ _logCategory._hmf_once_v3.30012
+ _logCategory._hmf_once_v316
+ _logCategory._hmf_once_v32.21478
+ _logCategory._hmf_once_v32.58675
+ _logCategory._hmf_once_v336
+ _logCategory._hmf_once_v338
+ _logCategory._hmf_once_v34.48776
+ _logCategory._hmf_once_v35.18512
+ _logCategory._hmf_once_v36.34914
+ _logCategory._hmf_once_v39.7719
+ _logCategory._hmf_once_v4.38268
+ _logCategory._hmf_once_v4.59441
+ _logCategory._hmf_once_v43.54891
+ _logCategory._hmf_once_v5.1192
+ _logCategory._hmf_once_v5.5458
+ _logCategory._hmf_once_v6.16724
+ _logCategory._hmf_once_v65.54208
+ _logCategory._hmf_once_v7.31128
+ _logCategory._hmf_once_v7.33505
+ _logCategory._hmf_once_v7.52940
+ _logCategory._hmf_once_v75
+ _logCategory._hmf_once_v8.23655
+ _logCategory._hmf_once_v8.47130
+ _logCategory._hmf_once_v9.33962
+ _logCategory._hmf_once_v9.43438
+ _logCategory._hmf_once_v9.46210
+ _objc_msgSend$IDSDestination
+ _objc_msgSend$IDSIdentifier
+ _objc_msgSend$_createControlsWithMostRecentSnapshot:
+ _objc_msgSend$_processHomeConfigurationResponse:refreshRequested:
+ _objc_msgSend$_removeActionSetsForAccessory:
+ _objc_msgSend$_removeActionsForAccessory:
+ _objc_msgSend$_removeCacheFileAtPath:
+ _objc_msgSend$_removeEventsForAccessory:
+ _objc_msgSend$_setInitialHomes:
+ _objc_msgSend$_updateValue:valueUpdatedDate:
+ _objc_msgSend$absoluteURL
+ _objc_msgSend$addObserver:queue:
+ _objc_msgSend$cachedInstanceForLanguageSettingValue:
+ _objc_msgSend$createSmartNotificationBulletin
+ _objc_msgSend$delegateCallersByObservers
+ _objc_msgSend$displayableVersion
+ _objc_msgSend$home:didUpdateSupportsResidentActionSetStateEvaluation:
+ _objc_msgSend$initWithEnabled:condition:accessoryIdentifier:
+ _objc_msgSend$initWithEnabled:condition:context:cameraUserSettings:
+ _objc_msgSend$initWithEnabled:condition:service:messageTargetUUID:
+ _objc_msgSend$initWithIdentifier:status:
+ _objc_msgSend$initWithStatuses:
+ _objc_msgSend$initWithVersion:displayableVersion:downloadSize:state:installDuration:documentationMetadata:releaseDate:
+ _objc_msgSend$isInitialMergeComplete
+ _objc_msgSend$matterEndpointID
+ _objc_msgSend$parseFromData:error:
+ _objc_msgSend$parsedFromData:error:
+ _objc_msgSend$predicateForOptions:
+ _objc_msgSend$serializeWithError:
+ _objc_msgSend$setIDSDestination:
+ _objc_msgSend$setIDSIdentifier:
+ _objc_msgSend$setMatterEndpointID:
+ _objc_msgSend$setStatuses:
+ _objc_msgSend$setSupportsResidentActionSetStateEvaluation:
+ _objc_msgSend$setUserInteractive:
+ _objc_msgSend$shortVersionString
+ _objc_msgSend$softwareUpdateFromDescriptor:
+ _objc_msgSend$statuses
+ _objc_msgSend$supportsResidentActionSetStateEvaluation
+ _sharedInstance.onceToken.38139
+ _sharedManager.onceToken.55877
+ _supportedValueClasses.onceToken.45995
+ _supportedValueClasses.onceToken.54170
+ _supportedValueClasses.supportedValueClasses.45997
+ _supportedValueClasses.supportedValueClasses.54171
+ _unconfigureQueue.onceToken.36698
+ _unconfigureQueue.unconfigureQueue.36700
- +[HMAccessory(NetworkRouter) _networkRouterProfilesForAccessoryProfiles:]
- +[HMBulletinBoardNotificationServiceGroup logCategory]
- +[HMBulletinBoardNotificationServiceGroup supportsSecureCoding]
- +[HMLightProfileNaturalLightingAction actionFromProtoBuf:home:]
- +[HMPBMediaPlaybackAction mediaProfilesType]
- +[HMPBMetadata hapCategoriesType]
- +[HMPBMetadata hapCharacteristicsType]
- +[HMPBMetadata hapServicesType]
- +[HMSymptom symptomWithType:]
- -[HMAccessory _copyFrom:]
- -[HMAccessory _notifyDelegateOfAppDataUpdateForService:]
- -[HMAudioAnalysisEventBulletinBoardNotification __configureWithContext:accessory:]
- -[HMAudioAnalysisEventBulletinBoardNotification initWithBulletinBoardNotification:]
- -[HMAudioAnalysisEventBulletinBoardNotification setAccessoryIdentifier:]
- -[HMBulletinBoardNotification initWithEnabled:condition:]
- -[HMBulletinBoardNotification init]
- -[HMBulletinBoardNotification logID]
- -[HMBulletinBoardNotification notificationServiceGroup]
- -[HMBulletinBoardNotification targetUUID]
- -[HMBulletinBoardNotificationServiceGroup .cxx_destruct]
- -[HMBulletinBoardNotificationServiceGroup __configureWithContext:]
- -[HMBulletinBoardNotificationServiceGroup _callServiceGroupUpdate]
- -[HMBulletinBoardNotificationServiceGroup _findObjects]
- -[HMBulletinBoardNotificationServiceGroup _handleBulletinBoardNotificationServiceGroupUpdateNotification:]
- -[HMBulletinBoardNotificationServiceGroup _registerNotificationHandlers]
- -[HMBulletinBoardNotificationServiceGroup _requestServiceGroup]
- -[HMBulletinBoardNotificationServiceGroup _unconfigureContext]
- -[HMBulletinBoardNotificationServiceGroup _unconfigure]
- -[HMBulletinBoardNotificationServiceGroup associatedServiceUUIDs]
- -[HMBulletinBoardNotificationServiceGroup associatedServices]
- -[HMBulletinBoardNotificationServiceGroup bulletinBoardNotification]
- -[HMBulletinBoardNotificationServiceGroup cameraProfileUUIDs]
- -[HMBulletinBoardNotificationServiceGroup cameraProfiles]
- -[HMBulletinBoardNotificationServiceGroup context]
- -[HMBulletinBoardNotificationServiceGroup encodeWithCoder:]
- -[HMBulletinBoardNotificationServiceGroup handleConfigureNotification:]
- -[HMBulletinBoardNotificationServiceGroup initWithCoder:]
- -[HMBulletinBoardNotificationServiceGroup logID]
- -[HMBulletinBoardNotificationServiceGroup logIdentifier]
- -[HMBulletinBoardNotificationServiceGroup mergeFromNewObject:]
- -[HMBulletinBoardNotificationServiceGroup messageReceiveQueue]
- -[HMBulletinBoardNotificationServiceGroup messageTargetUUID]
- -[HMBulletinBoardNotificationServiceGroup setAssociatedServiceUUIDs:]
- -[HMBulletinBoardNotificationServiceGroup setAssociatedServices:]
- -[HMBulletinBoardNotificationServiceGroup setCameraProfileUUIDs:]
- -[HMBulletinBoardNotificationServiceGroup setCameraProfiles:]
- -[HMBulletinBoardNotificationServiceGroup setContext:]
- -[HMBulletinBoardNotificationServiceGroup targetUUID]
- -[HMBulletinBoardNotificationServiceGroup uniqueIdentifier]
- -[HMCameraBulletinBoardSmartNotification __configureWithContext:cameraUserSettings:]
- -[HMCameraBulletinBoardSmartNotification initWithBulletinBoardNotification:]
- -[HMCameraBulletinBoardSmartNotification targetUUID]
- -[HMCameraClipManager observers]
- -[HMCameraRecordingEventManager observers]
- -[HMCameraRecordingReachabilityEventManager observers]
- -[HMCameraUserSettings smartNotificationBulletinForSettings:]
- -[HMCharacteristic _updateValue:updateTime:messageSentDate:]
- -[HMHome _addIdentifier:bridgeUUID:]
- -[HMHome sendConfigureBulletinNotification]
- -[HMHome setCurrentAccessories:]
- -[HMHome setCurrentActionSets:]
- -[HMHome setCurrentTriggers:]
- -[HMHomeManager _processHomeConfigurationRequest:refreshRequested:]
- -[HMHomeManager _shouldDisplayiCloudSwitchWithCompletionHandler:]
- -[HMHomeManager _updateHomes:]
- -[HMHomeManager addEphemeralContainer:completion:]
- -[HMHomeManager deactivateEphemeralContainer:completion:]
- -[HMHomeManager deleteEphemeralContainer:completion:]
- -[HMHomeManager didUpdateHomes]
- -[HMHomeManager frameworkMergeComplete]
- -[HMHomeManager readCountersForGroup:homeUUIDString:accessoryUUIDString:counter:statistics:datePartition:ephemeralContainer:completion:]
- -[HMHomeManager setDidUpdateHomes:]
- -[HMHomeManager setFrameworkMergeComplete:]
- -[HMHomeManager shouldDisplayiCloudSwitchWithCompletionHandler:]
- -[HMHomeManager startupEphemeralContainer:completion:]
- -[HMMutableReportContext initWithReportDomain:requestInfo:timeout:]
- -[HMPBMediaPlaybackAction actionUUID]
- -[HMPBMediaPlaybackAction clearMediaProfiles]
- -[HMPBMediaPlaybackAction copyTo:]
- -[HMPBMediaPlaybackAction hasActionUUID]
- -[HMPBMediaPlaybackAction hasMediaPlaybackState]
- -[HMPBMediaPlaybackAction hasPlaybackArchive]
- -[HMPBMediaPlaybackAction hasVolume]
- -[HMPBMediaPlaybackAction mediaPlaybackState]
- -[HMPBMediaPlaybackAction mediaProfilesAtIndex:]
- -[HMPBMediaPlaybackAction mediaProfilesCount]
- -[HMPBMediaPlaybackAction mediaProfiles]
- -[HMPBMediaPlaybackAction mergeFrom:]
- -[HMPBMediaPlaybackAction playbackArchive]
- -[HMPBMediaPlaybackAction setActionUUID:]
- -[HMPBMediaPlaybackAction setHasMediaPlaybackState:]
- -[HMPBMediaPlaybackAction setMediaPlaybackState:]
- -[HMPBMediaPlaybackAction setMediaProfiles:]
- -[HMPBMediaPlaybackAction setPlaybackArchive:]
- -[HMPBMediaPlaybackAction setVolume:]
- -[HMPBMediaPlaybackAction volume]
- -[HMPBMetadata clearHapCategories]
- -[HMPBMetadata clearHapCharacteristics]
- -[HMPBMetadata clearHapServices]
- -[HMPBMetadata copyTo:]
- -[HMPBMetadata hapCategoriesAtIndex:]
- -[HMPBMetadata hapCategoriesCount]
- -[HMPBMetadata hapCategories]
- -[HMPBMetadata hapCharacteristicsAtIndex:]
- -[HMPBMetadata hapCharacteristicsCount]
- -[HMPBMetadata hapCharacteristics]
- -[HMPBMetadata hapServicesAtIndex:]
- -[HMPBMetadata hapServicesCount]
- -[HMPBMetadata hapServices]
- -[HMPBMetadata hasVersion]
- -[HMPBMetadata mergeFrom:]
- -[HMPBMetadata setHapCategories:]
- -[HMPBMetadata setHapCharacteristics:]
- -[HMPBMetadata setHapServices:]
- -[HMPBMetadata setHasVersion:]
- -[HMPBMetadata setVersion:]
- -[HMPBMetadata version]
- -[HMPBMetadataCategory catDescription]
- -[HMPBMetadataCategory copyTo:]
- -[HMPBMetadataCategory hasCatDescription]
- -[HMPBMetadataCategory hasIdentifier]
- -[HMPBMetadataCategory hasUuidStr]
- -[HMPBMetadataCategory identifier]
- -[HMPBMetadataCategory mergeFrom:]
- -[HMPBMetadataCategory setCatDescription:]
- -[HMPBMetadataCategory setHasIdentifier:]
- -[HMPBMetadataCategory setIdentifier:]
- -[HMPBMetadataCategory setUuidStr:]
- -[HMPBMetadataCategory uuidStr]
- -[HMPBMetadataCharacteristic chrDescription]
- -[HMPBMetadataCharacteristic copyTo:]
- -[HMPBMetadataCharacteristic hasChrDescription]
- -[HMPBMetadataCharacteristic hasUuidStr]
- -[HMPBMetadataCharacteristic mergeFrom:]
- -[HMPBMetadataCharacteristic setChrDescription:]
- -[HMPBMetadataCharacteristic setUuidStr:]
- -[HMPBMetadataCharacteristic uuidStr]
- -[HMPBMetadataService copyTo:]
- -[HMPBMetadataService hasSvcDescription]
- -[HMPBMetadataService hasUuidStr]
- -[HMPBMetadataService mergeFrom:]
- -[HMPBMetadataService setSvcDescription:]
- -[HMPBMetadataService setUuidStr:]
- -[HMPBMetadataService svcDescription]
- -[HMPBMetadataService uuidStr]
- -[HMResidentDevice accountIdentifier]
- -[HMResidentDevice setAccountIdentifier:]
- -[HMSymptom .cxx_destruct]
- -[HMSymptom localizedTitle]
- -[_HMCameraControl __configureWithContext:home:]
- -[_HMCameraControl _registerNotificationHandlers]
- -[_HMCameraControl home]
- -[_HMCameraControl setHome:]
- -[_HMCameraProfile _createControls:]
- -[_HMCameraProfile snapshotControlInternal]
- -[_HMCameraProfile streamControlInternal]
- -[_HMCameraSnapshotControl __configureWithContext:home:]
- -[_HMCameraSnapshotControl _registerNotificationHandlers]
- -[_HMCameraStreamControl _registerNotificationHandlers]
- GCC_except_table10294
- GCC_except_table10298
- GCC_except_table10299
- GCC_except_table10330
- GCC_except_table10332
- GCC_except_table10334
- GCC_except_table10340
- GCC_except_table10341
- GCC_except_table10342
- GCC_except_table10450
- GCC_except_table10451
- GCC_except_table10477
- GCC_except_table10479
- GCC_except_table10483
- GCC_except_table10484
- GCC_except_table10532
- GCC_except_table10558
- GCC_except_table10571
- GCC_except_table10595
- GCC_except_table10599
- GCC_except_table10652
- GCC_except_table10653
- GCC_except_table10654
- GCC_except_table10671
- GCC_except_table10698
- GCC_except_table1074
- GCC_except_table1076
- GCC_except_table1079
- GCC_except_table10805
- GCC_except_table10809
- GCC_except_table1081
- GCC_except_table1087
- GCC_except_table10871
- GCC_except_table10873
- GCC_except_table10881
- GCC_except_table10888
- GCC_except_table10894
- GCC_except_table10896
- GCC_except_table10903
- GCC_except_table11130
- GCC_except_table11131
- GCC_except_table11287
- GCC_except_table11296
- GCC_except_table11302
- GCC_except_table11307
- GCC_except_table11309
- GCC_except_table11314
- GCC_except_table11315
- GCC_except_table11317
- GCC_except_table1136
- GCC_except_table11400
- GCC_except_table11402
- GCC_except_table11421
- GCC_except_table11422
- GCC_except_table11423
- GCC_except_table11443
- GCC_except_table11449
- GCC_except_table11452
- GCC_except_table11454
- GCC_except_table11534
- GCC_except_table11539
- GCC_except_table11547
- GCC_except_table11553
- GCC_except_table11559
- GCC_except_table11561
- GCC_except_table11563
- GCC_except_table11565
- GCC_except_table11567
- GCC_except_table11569
- GCC_except_table11703
- GCC_except_table11758
- GCC_except_table11759
- GCC_except_table11760
- GCC_except_table11771
- GCC_except_table11772
- GCC_except_table11796
- GCC_except_table11797
- GCC_except_table11851
- GCC_except_table11876
- GCC_except_table11879
- GCC_except_table12011
- GCC_except_table12131
- GCC_except_table12132
- GCC_except_table12133
- GCC_except_table12181
- GCC_except_table12182
- GCC_except_table12184
- GCC_except_table12187
- GCC_except_table12189
- GCC_except_table12191
- GCC_except_table12223
- GCC_except_table12266
- GCC_except_table12271
- GCC_except_table12274
- GCC_except_table12334
- GCC_except_table12419
- GCC_except_table12426
- GCC_except_table12479
- GCC_except_table12481
- GCC_except_table12490
- GCC_except_table12493
- GCC_except_table1251
- GCC_except_table12513
- GCC_except_table12515
- GCC_except_table12516
- GCC_except_table1273
- GCC_except_table1350
- GCC_except_table1353
- GCC_except_table1367
- GCC_except_table1502
- GCC_except_table1571
- GCC_except_table1574
- GCC_except_table1643
- GCC_except_table1645
- GCC_except_table1719
- GCC_except_table1720
- GCC_except_table1768
- GCC_except_table1997
- GCC_except_table2000
- GCC_except_table2003
- GCC_except_table2008
- GCC_except_table2021
- GCC_except_table2023
- GCC_except_table2026
- GCC_except_table2036
- GCC_except_table2039
- GCC_except_table2044
- GCC_except_table2045
- GCC_except_table2046
- GCC_except_table2047
- GCC_except_table2234
- GCC_except_table2236
- GCC_except_table2240
- GCC_except_table2242
- GCC_except_table2244
- GCC_except_table2246
- GCC_except_table2252
- GCC_except_table2475
- GCC_except_table2478
- GCC_except_table2492
- GCC_except_table2524
- GCC_except_table2537
- GCC_except_table2540
- GCC_except_table2541
- GCC_except_table2544
- GCC_except_table2567
- GCC_except_table2569
- GCC_except_table2571
- GCC_except_table2573
- GCC_except_table2733
- GCC_except_table2751
- GCC_except_table2752
- GCC_except_table2808
- GCC_except_table2810
- GCC_except_table2813
- GCC_except_table2814
- GCC_except_table2838
- GCC_except_table2840
- GCC_except_table2848
- GCC_except_table2850
- GCC_except_table2857
- GCC_except_table2858
- GCC_except_table2862
- GCC_except_table2863
- GCC_except_table2864
- GCC_except_table2865
- GCC_except_table2917
- GCC_except_table2941
- GCC_except_table2944
- GCC_except_table2947
- GCC_except_table2950
- GCC_except_table2953
- GCC_except_table2956
- GCC_except_table2959
- GCC_except_table3024
- GCC_except_table3025
- GCC_except_table3069
- GCC_except_table3076
- GCC_except_table3077
- GCC_except_table3078
- GCC_except_table3081
- GCC_except_table3082
- GCC_except_table3083
- GCC_except_table3085
- GCC_except_table3093
- GCC_except_table3101
- GCC_except_table3102
- GCC_except_table3120
- GCC_except_table3127
- GCC_except_table3131
- GCC_except_table3134
- GCC_except_table3137
- GCC_except_table3176
- GCC_except_table3180
- GCC_except_table3184
- GCC_except_table3189
- GCC_except_table3197
- GCC_except_table3201
- GCC_except_table3210
- GCC_except_table3212
- GCC_except_table3444
- GCC_except_table3448
- GCC_except_table3452
- GCC_except_table3455
- GCC_except_table3459
- GCC_except_table3460
- GCC_except_table3463
- GCC_except_table3472
- GCC_except_table3476
- GCC_except_table3500
- GCC_except_table3502
- GCC_except_table3504
- GCC_except_table3507
- GCC_except_table3508
- GCC_except_table3510
- GCC_except_table3513
- GCC_except_table3595
- GCC_except_table3600
- GCC_except_table3612
- GCC_except_table3615
- GCC_except_table3617
- GCC_except_table3620
- GCC_except_table3627
- GCC_except_table3680
- GCC_except_table3746
- GCC_except_table3761
- GCC_except_table3764
- GCC_except_table3878
- GCC_except_table3879
- GCC_except_table3881
- GCC_except_table3890
- GCC_except_table3893
- GCC_except_table3903
- GCC_except_table4102
- GCC_except_table4105
- GCC_except_table4117
- GCC_except_table4189
- GCC_except_table419
- GCC_except_table4208
- GCC_except_table422
- GCC_except_table424
- GCC_except_table4295
- GCC_except_table430
- GCC_except_table432
- GCC_except_table4410
- GCC_except_table4415
- GCC_except_table4416
- GCC_except_table4424
- GCC_except_table4426
- GCC_except_table4452
- GCC_except_table4453
- GCC_except_table4454
- GCC_except_table4514
- GCC_except_table4524
- GCC_except_table4589
- GCC_except_table4591
- GCC_except_table4593
- GCC_except_table4635
- GCC_except_table4636
- GCC_except_table4710
- GCC_except_table4797
- GCC_except_table4798
- GCC_except_table4804
- GCC_except_table4806
- GCC_except_table4835
- GCC_except_table4837
- GCC_except_table4856
- GCC_except_table4902
- GCC_except_table4952
- GCC_except_table5038
- GCC_except_table5058
- GCC_except_table5059
- GCC_except_table5062
- GCC_except_table5065
- GCC_except_table5066
- GCC_except_table5068
- GCC_except_table5274
- GCC_except_table5280
- GCC_except_table5282
- GCC_except_table5292
- GCC_except_table5293
- GCC_except_table5540
- GCC_except_table5649
- GCC_except_table5655
- GCC_except_table5662
- GCC_except_table5667
- GCC_except_table572
- GCC_except_table5743
- GCC_except_table5749
- GCC_except_table575
- GCC_except_table5751
- GCC_except_table580
- GCC_except_table583
- GCC_except_table5888
- GCC_except_table6045
- GCC_except_table6046
- GCC_except_table606
- GCC_except_table6071
- GCC_except_table6073
- GCC_except_table6079
- GCC_except_table6087
- GCC_except_table6102
- GCC_except_table6109
- GCC_except_table6126
- GCC_except_table6131
- GCC_except_table6165
- GCC_except_table6176
- GCC_except_table6182
- GCC_except_table6194
- GCC_except_table6199
- GCC_except_table6213
- GCC_except_table6218
- GCC_except_table6226
- GCC_except_table623
- GCC_except_table6231
- GCC_except_table6243
- GCC_except_table6248
- GCC_except_table6252
- GCC_except_table6280
- GCC_except_table6286
- GCC_except_table6311
- GCC_except_table6316
- GCC_except_table6320
- GCC_except_table6349
- GCC_except_table6353
- GCC_except_table6356
- GCC_except_table640
- GCC_except_table6494
- GCC_except_table6500
- GCC_except_table6580
- GCC_except_table6602
- GCC_except_table6607
- GCC_except_table6615
- GCC_except_table6658
- GCC_except_table6660
- GCC_except_table6662
- GCC_except_table6674
- GCC_except_table6685
- GCC_except_table6711
- GCC_except_table6720
- GCC_except_table6727
- GCC_except_table6748
- GCC_except_table6758
- GCC_except_table6782
- GCC_except_table6785
- GCC_except_table6788
- GCC_except_table679
- GCC_except_table6791
- GCC_except_table6794
- GCC_except_table6797
- GCC_except_table6800
- GCC_except_table6803
- GCC_except_table6806
- GCC_except_table6809
- GCC_except_table6812
- GCC_except_table6815
- GCC_except_table6818
- GCC_except_table682
- GCC_except_table6821
- GCC_except_table6824
- GCC_except_table6827
- GCC_except_table683
- GCC_except_table6830
- GCC_except_table6834
- GCC_except_table6847
- GCC_except_table7068
- GCC_except_table7274
- GCC_except_table7344
- GCC_except_table7447
- GCC_except_table7463
- GCC_except_table748
- GCC_except_table751
- GCC_except_table752
- GCC_except_table753
- GCC_except_table7538
- GCC_except_table754
- GCC_except_table755
- GCC_except_table7556
- GCC_except_table7562
- GCC_except_table7564
- GCC_except_table7566
- GCC_except_table757
- GCC_except_table758
- GCC_except_table7699
- GCC_except_table7702
- GCC_except_table7713
- GCC_except_table7718
- GCC_except_table7752
- GCC_except_table7754
- GCC_except_table7772
- GCC_except_table7780
- GCC_except_table7782
- GCC_except_table7784
- GCC_except_table7786
- GCC_except_table7793
- GCC_except_table7799
- GCC_except_table7801
- GCC_except_table7803
- GCC_except_table7813
- GCC_except_table7824
- GCC_except_table7826
- GCC_except_table7869
- GCC_except_table7871
- GCC_except_table7879
- GCC_except_table7881
- GCC_except_table7883
- GCC_except_table7885
- GCC_except_table7887
- GCC_except_table7893
- GCC_except_table7897
- GCC_except_table7909
- GCC_except_table7911
- GCC_except_table7913
- GCC_except_table7915
- GCC_except_table7934
- GCC_except_table8084
- GCC_except_table8086
- GCC_except_table8088
- GCC_except_table8092
- GCC_except_table8094
- GCC_except_table8130
- GCC_except_table8134
- GCC_except_table8141
- GCC_except_table8185
- GCC_except_table8186
- GCC_except_table8187
- GCC_except_table8194
- GCC_except_table8195
- GCC_except_table8259
- GCC_except_table8260
- GCC_except_table8261
- GCC_except_table8298
- GCC_except_table8480
- GCC_except_table8481
- GCC_except_table8482
- GCC_except_table8486
- GCC_except_table8541
- GCC_except_table8562
- GCC_except_table8633
- GCC_except_table8639
- GCC_except_table8641
- GCC_except_table8643
- GCC_except_table8645
- GCC_except_table8653
- GCC_except_table8702
- GCC_except_table8703
- GCC_except_table8730
- GCC_except_table8758
- GCC_except_table8916
- GCC_except_table8968
- GCC_except_table8975
- GCC_except_table8980
- GCC_except_table8985
- GCC_except_table8989
- GCC_except_table9002
- GCC_except_table9010
- GCC_except_table9040
- GCC_except_table9060
- GCC_except_table9061
- GCC_except_table9062
- GCC_except_table9099
- GCC_except_table9100
- GCC_except_table9104
- GCC_except_table9106
- GCC_except_table9108
- GCC_except_table9167
- GCC_except_table9194
- GCC_except_table9199
- GCC_except_table9201
- GCC_except_table9203
- GCC_except_table9205
- GCC_except_table9211
- GCC_except_table9213
- GCC_except_table9219
- GCC_except_table9223
- GCC_except_table9233
- GCC_except_table9237
- GCC_except_table9243
- GCC_except_table9249
- GCC_except_table9260
- GCC_except_table9261
- GCC_except_table9274
- GCC_except_table9288
- GCC_except_table9499
- GCC_except_table9512
- GCC_except_table9561
- GCC_except_table9562
- GCC_except_table9564
- GCC_except_table9572
- GCC_except_table963
- GCC_except_table9631
- GCC_except_table9632
- GCC_except_table967
- GCC_except_table974
- GCC_except_table9942
- GCC_except_table997
- GCC_except_table9981
- GCC_except_table9994
- _CoreAnalyticsLibraryCore.frameworkLibrary.35957
- _HMDaysOfTheWeekToConsiseString
- _HMHomeEnableExpressForWalletKeyMessageKeyAuthData
- _HMHomeManagerDumpStateXPCMessagesCountersMessageKey
- _IDSFoundationLibraryCore.39527
- _IDSFoundationLibraryCore.frameworkLibrary.39529
- _OBJC_CLASS_$_HMBulletinBoardNotificationServiceGroup
- _OBJC_IVAR_$_HMBulletinBoardNotification._logID
- _OBJC_IVAR_$_HMBulletinBoardNotification._notificationServiceGroup
- _OBJC_IVAR_$_HMBulletinBoardNotification._targetUUID
- _OBJC_IVAR_$_HMBulletinBoardNotificationServiceGroup._associatedServiceUUIDs
- _OBJC_IVAR_$_HMBulletinBoardNotificationServiceGroup._associatedServices
- _OBJC_IVAR_$_HMBulletinBoardNotificationServiceGroup._bulletinBoardNotification
- _OBJC_IVAR_$_HMBulletinBoardNotificationServiceGroup._cameraProfileUUIDs
- _OBJC_IVAR_$_HMBulletinBoardNotificationServiceGroup._cameraProfiles
- _OBJC_IVAR_$_HMBulletinBoardNotificationServiceGroup._context
- _OBJC_IVAR_$_HMBulletinBoardNotificationServiceGroup._lock
- _OBJC_IVAR_$_HMBulletinBoardNotificationServiceGroup._logID
- _OBJC_IVAR_$_HMBulletinBoardNotificationServiceGroup._targetUUID
- _OBJC_IVAR_$_HMBulletinBoardNotificationServiceGroup._uniqueIdentifier
- _OBJC_IVAR_$_HMCameraBulletinBoardSmartNotification._targetUUID
- _OBJC_IVAR_$_HMCameraClipManager._observers
- _OBJC_IVAR_$_HMCameraRecordingEventManager._observers
- _OBJC_IVAR_$_HMCameraRecordingReachabilityEventManager._observers
- _OBJC_IVAR_$_HMHomeManager._didUpdateHomes
- _OBJC_IVAR_$_HMHomeManager._frameworkMergeComplete
- _OBJC_IVAR_$_HMResidentDevice._accountIdentifier
- _OBJC_IVAR_$_HMSymptom._localizedTitle
- _OBJC_IVAR_$__HMCameraControl._home
- _OBJC_IVAR_$__HMCameraProfile._snapshotControlInternal
- _OBJC_IVAR_$__HMCameraProfile._streamControlInternal
- _OBJC_METACLASS_$_HMBulletinBoardNotificationServiceGroup
- _UIKitLibrary.39761
- _UIKitLibraryCore.39755
- _UIKitLibraryCore.frameworkLibrary.39770
- __OBJC_$_CLASS_METHODS_HMAccessory(SiriEndpoint|Television|WoL|LightInternal|NetworkRouter|Private|PendingConfiguration|CUPeerIdentifier|Shortcuts|Camera|CHIP|NetworkConfiguration|Light|Media)
- __OBJC_$_CLASS_METHODS_HMBulletinBoardNotificationServiceGroup
- __OBJC_$_CLASS_METHODS_HMPBMediaPlaybackAction
- __OBJC_$_CLASS_METHODS_HMPBMetadata
- __OBJC_$_CLASS_PROP_LIST_HMBulletinBoardNotificationServiceGroup
- __OBJC_$_INSTANCE_METHODS_HMAccessory(SiriEndpoint|Television|WoL|LightInternal|NetworkRouter|Private|PendingConfiguration|CUPeerIdentifier|Shortcuts|Camera|CHIP|NetworkConfiguration|Light|Media)
- __OBJC_$_INSTANCE_METHODS_HMBulletinBoardNotificationServiceGroup
- __OBJC_$_INSTANCE_VARIABLES_HMBulletinBoardNotificationServiceGroup
- __OBJC_$_PROP_LIST_HMAccessoryCapabilities.133
- __OBJC_$_PROP_LIST_HMActionSetBuilder.148
- __OBJC_$_PROP_LIST_HMApplicationData.11442
- __OBJC_$_PROP_LIST_HMBulletinBoardNotificationServiceGroup
- __OBJC_$_PROP_LIST_HMCache.99
- __OBJC_$_PROP_LIST_HMEventTriggerBuilder.214
- __OBJC_$_PROP_LIST_HMHAPMetadataCategory.88
- __OBJC_$_PROP_LIST_HMHAPMetadataCharacteristic.58
- __OBJC_$_PROP_LIST_HMHAPMetadataService.68
- __OBJC_$_PROP_LIST_HMMediaDestination.264
- __OBJC_$_PROP_LIST_HMPBMediaPlaybackAction
- __OBJC_$_PROP_LIST_HMPBMetadata
- __OBJC_$_PROP_LIST_HMPBMetadataCategory
- __OBJC_$_PROP_LIST_HMPBMetadataCharacteristic
- __OBJC_$_PROP_LIST_HMPBMetadataService
- __OBJC_$_PROP_LIST_HMResidentCapabilities.195
- __OBJC_$_PROP_LIST_HMTimerTriggerBuilder.200
- __OBJC_$_PROP_LIST_HMTriggerBuilder.178
- __OBJC_$_PROP_LIST__HMNetworkConnection.96
- __OBJC_$_PROP_LIST__HMNetworkPath.58
- __OBJC_$_PROP_LIST__HMPrivacySettingsProvider.51
- __OBJC_CLASS_PROTOCOLS_$_HMBulletinBoardNotificationServiceGroup
- __OBJC_CLASS_RO_$_HMBulletinBoardNotificationServiceGroup
- __OBJC_METACLASS_RO_$_HMBulletinBoardNotificationServiceGroup
- ___107-[HMCameraRecordingEventManager fetchEventsWithDateInterval:quality:limit:shouldOrderAscending:completion:]_block_invoke.11
- ___111-[HMCameraRecordingReachabilityEventManager fetchEventsWithDateInterval:limit:shouldOrderAscending:completion:]_block_invoke.67
- ___111-[HMCameraRecordingReachabilityEventManager fetchEventsWithDateInterval:limit:shouldOrderAscending:completion:]_block_invoke.71
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.737
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.739
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.740
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.743
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.747
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.749
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.742
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.745
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.748
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.750
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_3.746
- ___136-[HMHomeManager readCountersForGroup:homeUUIDString:accessoryUUIDString:counter:statistics:datePartition:ephemeralContainer:completion:]_block_invoke
- ___136-[HMHomeManager readCountersForGroup:homeUUIDString:accessoryUUIDString:counter:statistics:datePartition:ephemeralContainer:completion:]_block_invoke_2
- ___22-[HMHome _mergeRooms:]_block_invoke.739
- ___22-[HMHome _mergeRooms:]_block_invoke.740
- ___22-[HMHome _mergeRooms:]_block_invoke.742
- ___22-[HMHome _mergeRooms:]_block_invoke_2.744
- ___22-[HMHome _mergeRooms:]_block_invoke_3.745
- ___22-[HMHome _mergeUsers:]_block_invoke.785
- ___22-[HMHome _mergeUsers:]_block_invoke.786
- ___22-[HMHome _mergeUsers:]_block_invoke.788
- ___22-[HMHome _mergeUsers:]_block_invoke_2.790
- ___22-[HMHome _mergeUsers:]_block_invoke_3.791
- ___22-[HMHome _mergeZones:]_block_invoke.747
- ___22-[HMHome _mergeZones:]_block_invoke.748
- ___22-[HMHome _mergeZones:]_block_invoke.750
- ___22-[HMHome _mergeZones:]_block_invoke_2.752
- ___22-[HMHome _mergeZones:]_block_invoke_3.753
- ___25-[HMHome _mergeTriggers:]_block_invoke.781
- ___25-[HMHome _mergeTriggers:]_block_invoke.783
- ___25-[HMXPCClient connection]_block_invoke.76
- ___25-[HMXPCClient connection]_block_invoke.78
- ___27-[HMHome _mergeActionSets:]_block_invoke.772
- ___27-[HMHome _mergeActionSets:]_block_invoke.773
- ___27-[HMHome _mergeActionSets:]_block_invoke.775
- ___27-[HMHome _mergeActionSets:]_block_invoke_2.777
- ___27-[HMHome _mergeActionSets:]_block_invoke_3.778
- ___28-[HMHome _mergeAccessories:]_block_invoke.755
- ___28-[HMHome _mergeAccessories:]_block_invoke.756
- ___28-[HMHome _mergeAccessories:]_block_invoke.758
- ___28-[HMHome _mergeAccessories:]_block_invoke.759
- ___28-[HMHome _mergeAccessories:]_block_invoke.761
- ___28-[HMHome _mergeAccessories:]_block_invoke_2.762
- ___29-[HMHome mergeFromNewObject:]_block_invoke.525
- ___29-[HMHome mergeFromNewObject:]_block_invoke.529
- ___29-[HMHome mergeFromNewObject:]_block_invoke.533
- ___29-[HMHome mergeFromNewObject:]_block_invoke.535
- ___29-[HMHome mergeFromNewObject:]_block_invoke.539
- ___29-[HMHome mergeFromNewObject:]_block_invoke.559
- ___29-[HMHome mergeFromNewObject:]_block_invoke.563
- ___29-[HMHome mergeFromNewObject:]_block_invoke.567
- ___29-[HMHome mergeFromNewObject:]_block_invoke.709
- ___29-[HMHome mergeFromNewObject:]_block_invoke.718
- ___29-[HMHome mergeFromNewObject:]_block_invoke.721
- ___29-[HMHome mergeFromNewObject:]_block_invoke.729
- ___29-[HMHome mergeFromNewObject:]_block_invoke.735
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.526
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.530
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.534
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.536
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.540
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.560
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.564
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.568
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.710
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.719
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.722
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.730
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.736
- ___29-[HMHome mergeFromNewObject:]_block_invoke_3.724
- ___29-[HMHome mergeFromNewObject:]_block_invoke_4.725
- ___29-[HMHome mergeFromNewObject:]_block_invoke_5.726
- ___29-[HMHome mergeFromNewObject:]_block_invoke_6.727
- ___29-[HMUser mergeFromNewObject:]_block_invoke.296
- ___29-[HMUser mergeFromNewObject:]_block_invoke.299
- ___29-[HMUser mergeFromNewObject:]_block_invoke.301
- ___29-[HMUser mergeFromNewObject:]_block_invoke.304
- ___29-[HMUser mergeFromNewObject:]_block_invoke.307
- ___29-[HMUser mergeFromNewObject:]_block_invoke.310
- ___29-[HMUser mergeFromNewObject:]_block_invoke.313
- ___29-[HMUser mergeFromNewObject:]_block_invoke_2.297
- ___29-[HMUser mergeFromNewObject:]_block_invoke_2.300
- ___29-[HMUser mergeFromNewObject:]_block_invoke_2.302
- ___29-[HMUser mergeFromNewObject:]_block_invoke_2.305
- ___29-[HMUser mergeFromNewObject:]_block_invoke_2.308
- ___29-[HMUser mergeFromNewObject:]_block_invoke_2.311
- ___30-[HMAccessory _mergeProfiles:]_block_invoke.1099
- ___30-[HMAccessory _mergeProfiles:]_block_invoke.1100
- ___30-[HMAccessory _mergeProfiles:]_block_invoke.1102
- ___30-[HMAccessory _mergeProfiles:]_block_invoke.1106
- ___30-[HMAccessory _mergeProfiles:]_block_invoke_2.1104
- ___30-[HMAccessory _mergeProfiles:]_block_invoke_2.1107
- ___30-[HMAccessory _mergeProfiles:]_block_invoke_3.1105
- ___30-[HMAccessory _mergeServices:]_block_invoke.920
- ___30-[HMAccessory _mergeServices:]_block_invoke.922
- ___30-[HMHome _mergeServiceGroups:]_block_invoke.764
- ___30-[HMHome _mergeServiceGroups:]_block_invoke.765
- ___30-[HMHome _mergeServiceGroups:]_block_invoke.767
- ___30-[HMHome _mergeServiceGroups:]_block_invoke_2.769
- ___30-[HMHome _mergeServiceGroups:]_block_invoke_3.770
- ___30-[HMHomeManager _updateHomes:]_block_invoke
- ___32-[HMHome _mergeResidentDevices:]_block_invoke.793
- ___32-[HMHome _mergeResidentDevices:]_block_invoke.794
- ___32-[HMHome _mergeResidentDevices:]_block_invoke.796
- ___32-[HMHome _mergeResidentDevices:]_block_invoke_2.798
- ___32-[HMHome _mergeResidentDevices:]_block_invoke_3.799
- ___32-[HMService mergeFromNewObject:]_block_invoke.161
- ___32-[HMService mergeFromNewObject:]_block_invoke.164
- ___32-[HMService mergeFromNewObject:]_block_invoke_2
- ___32-[HMService mergeFromNewObject:]_block_invoke_3
- ___32-[HMService mergeFromNewObject:]_block_invoke_4
- ___32-[HMService mergeFromNewObject:]_block_invoke_5
- ___32-[HMService mergeFromNewObject:]_block_invoke_6
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1075
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1077
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1079
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1080
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1082
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1085
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1087
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1090
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1092
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.924
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.925
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.929
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.932
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.949
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.954
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1076
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1078
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1083
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1086
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.926
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.930
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.933
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.950
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.955
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_3.951
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_3.956
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_3.961
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_4.962
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_5.963
- ___34-[HMHTMLDocument attributedString]_block_invoke
- ___36-[HMHome _mergeOutgoingInvitations:]_block_invoke.801
- ___36-[HMHome _mergeOutgoingInvitations:]_block_invoke.803
- ___37-[HMEventTrigger mergeFromNewObject:]_block_invoke.144
- ___37-[HMEventTrigger mergeFromNewObject:]_block_invoke.145
- ___38-[HMHomeManager _updateDataSyncState:]_block_invoke.489
- ___39-[HMHome _mergeTriggerOwnedActionSets:]_block_invoke.779
- ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.752
- ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.754
- ___39-[HMResidentDevice mergeFromNewObject:]_block_invoke.148
- ___39-[HMResidentDevice mergeFromNewObject:]_block_invoke_2.149
- ___39-[HMSoftwareUpdate mergeFromNewObject:]_block_invoke.170
- ___39-[HMSoftwareUpdate mergeFromNewObject:]_block_invoke.172
- ___39-[HMSoftwareUpdate mergeFromNewObject:]_block_invoke_2.171
- ___39-[HMSoftwareUpdate mergeFromNewObject:]_block_invoke_2.173
- ___40-[HMSoftwareUpdate requestDocumentation]_block_invoke.158
- ___41-[HMAccessory _updateHasSymptomsHandler:]_block_invoke.1136
- ___41-[HMAccessory _updateHasSymptomsHandler:]_block_invoke.1138
- ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke.805
- ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke.806
- ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke.807
- ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke.808
- ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke.810
- ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke_2.809
- ___43-[HMHome fetchPresenceForUsers:completion:]_block_invoke.819
- ___43-[HMHome fetchPresenceForUsers:completion:]_block_invoke.821
- ___43-[HMHome sendConfigureBulletinNotification]_block_invoke
- ___44-[HMHome _handleAccessoryAddedNotification:]_block_invoke.890
- ___44-[HMUser _mergeWithNewAccessoryInvitations:]_block_invoke.293
- ___45-[HMAccessory _handleCharacteristicsUpdated:]_block_invoke.1120
- ___45-[HMResidentDevice handleRuntimeStateUpdate:]_block_invoke.158
- ___45-[HMResidentDevice handleRuntimeStateUpdate:]_block_invoke.159
- ___45-[HMResidentDevice handleRuntimeStateUpdate:]_block_invoke.160
- ___45-[HMXPCClient sendMessage:completionHandler:]_block_invoke.86
- ___47-[HMHomeManager _recomputeAssistantIdentifiers]_block_invoke.661
- ___48-[HMAccessory _deleteSiriHistoryWithCompletion:]_block_invoke.1121
- ___48-[HMAccessory _deleteSiriHistoryWithCompletion:]_block_invoke.1122
- ___50-[HMHomeManager addEphemeralContainer:completion:]_block_invoke
- ___50-[HMHomeManager addEphemeralContainer:completion:]_block_invoke_2
- ___50-[HMSoftwareUpdate updateState:completionHandler:]_block_invoke.147
- ___50-[HMSoftwareUpdate updateState:completionHandler:]_block_invoke.149
- ___51-[HMHomeManager _updatePrimaryHome:notifyDelegate:]_block_invoke.721
- ___52-[HMCameraClipManager fetchClipWithUUID:completion:]_block_invoke.147
- ___52-[HMCameraClipManager fetchClipWithUUID:completion:]_block_invoke.150
- ___52-[HMHome(HMUser) _manageUsersWithCompletionHandler:]_block_invoke.1702
- ___52-[HMSoftwareUpdateDocumentationAsset startUnarchive]_block_invoke.126
- ___53-[HMHomeManager deleteEphemeralContainer:completion:]_block_invoke
- ___53-[HMHomeManager deleteEphemeralContainer:completion:]_block_invoke_2
- ___53-[HMMediaProfile mediaProfile:didUpdateMediaSession:]_block_invoke.67
- ___54+[HMBulletinBoardNotificationServiceGroup logCategory]_block_invoke
- ___54-[HMEventTrigger mergeFromNewObjectForBuilderUpdates:]_block_invoke.148
- ___54-[HMHome _notifyDelegateOfAccessControlUpdateForUser:]_block_invoke.926
- ___54-[HMHomeManager _refreshBeforeDate:completionHandler:]_block_invoke.582
- ___54-[HMHomeManager _refreshBeforeDate:completionHandler:]_block_invoke.583
- ___54-[HMHomeManager startupEphemeralContainer:completion:]_block_invoke
- ___54-[HMHomeManager startupEphemeralContainer:completion:]_block_invoke_2
- ___55-[_HMCameraStreamControl _registerNotificationHandlers]_block_invoke
- ___56-[HMAccessory _notifyDelegateOfAppDataUpdateForService:]_block_invoke
- ___56-[HMAccessory _notifyDelegateOfAppDataUpdateForService:]_block_invoke_2
- ___57-[HMHomeManager deactivateEphemeralContainer:completion:]_block_invoke
- ___57-[HMHomeManager deactivateEphemeralContainer:completion:]_block_invoke_2
- ___58-[HMHomeManager __resolveAccountHandle:completionHandler:]_block_invoke.648
- ___61-[HMHomeManager __removeAccountWithHandle:completionHandler:]_block_invoke.650
- ___62-[HMOutgoingHomeInvitation _mergeWithNewAccessoryInvitations:]_block_invoke.131
- ___63-[HMAccessory pairingIdentityWithPrivateKey:completionHandler:]_block_invoke.854
- ___63-[HMAccessory pairingIdentityWithPrivateKey:completionHandler:]_block_invoke.856
- ___63-[HMBulletinBoardNotificationServiceGroup _requestServiceGroup]_block_invoke
- ___63-[HMUser updateAnnounceUserSettings:forHome:completionHandler:]_block_invoke.217
- ___64-[HMHome(HMMediaProfile) updateMediaPassword:completionHandler:]_block_invoke.1777
- ___64-[HMHomeManager shouldDisplayiCloudSwitchWithCompletionHandler:]_block_invoke
- ___65-[HMHomeManager __removeAccountWithIdentifier:completionHandler:]_block_invoke.649
- ___65-[HMHomeManager _shouldDisplayiCloudSwitchWithCompletionHandler:]_block_invoke
- ___66-[HMBulletinBoardNotificationServiceGroup _callServiceGroupUpdate]_block_invoke
- ___66-[HMCameraClipManager fetchHeroFrameURLOfClipWithUUID:completion:]_block_invoke.173
- ___66-[HMCameraClipManager fetchHeroFrameURLOfClipWithUUID:completion:]_block_invoke.175
- ___66-[HMCameraClipManager fetchSignificantEventsWithUUIDs:completion:]_block_invoke.190
- ___66-[HMSoftwareUpdate updateDocumentationMetadata:completionHandler:]_block_invoke.157
- ___67-[HMHome _addEventTriggerFromResponse:withEventTrigger:completion:]_block_invoke.883
- ___67-[HMHomeManager _processHomeConfigurationRequest:refreshRequested:]_block_invoke
- ___67-[HMHomeManager _processHomeConfigurationRequest:refreshRequested:]_block_invoke.679
- ___67-[HMHomeManager _processHomeConfigurationRequest:refreshRequested:]_block_invoke.683
- ___67-[HMHomeManager _processHomeConfigurationRequest:refreshRequested:]_block_invoke.685
- ___67-[HMHomeManager _processHomeConfigurationRequest:refreshRequested:]_block_invoke.687
- ___67-[HMHomeManager _processHomeConfigurationRequest:refreshRequested:]_block_invoke_2
- ___67-[HMHomeManager _processHomeConfigurationRequest:refreshRequested:]_block_invoke_2.688
- ___69-[HMHomeManager addAndSetupAccessoriesWithPayload:completionHandler:]_block_invoke.805
- ___71-[HMBulletinBoardNotificationServiceGroup handleConfigureNotification:]_block_invoke
- ___71-[HMCameraClipManager fetchClipForSignificantEventWithUUID:completion:]_block_invoke.152
- ___71-[HMCameraClipManager fetchClipForSignificantEventWithUUID:completion:]_block_invoke.153
- ___72-[HMBulletinBoardNotificationServiceGroup _registerNotificationHandlers]_block_invoke
- ___72-[HMCameraClipManager fetchVideoSegmentsAssetContextForClip:completion:]_block_invoke.216
- ___72-[HMCameraClipManager fetchVideoSegmentsAssetContextForClip:completion:]_block_invoke.217
- ___72-[HMCameraClipManager fetchVideoSegmentsAssetContextForClip:completion:]_block_invoke.220
- ___74-[HMHomeManager __processSyncResponse:refreshRequested:completionHandler:]_block_invoke.658
- ___75-[HMHome(HMAccessory) addAndSetupAccessoriesWithPayload:completionHandler:]_block_invoke.1565
- ___75-[HMUser updateMediaContentProfileAccessControl:forHome:completionHandler:]_block_invoke.219
- ___76-[HMCameraClipManager fetchCountOfClipsWithDateInterval:quality:completion:]_block_invoke.163
- ___76-[HMCameraClipManager fetchCountOfClipsWithDateInterval:quality:completion:]_block_invoke.164
- ___76-[HMUser updateUserListeningHistoryUpdateControl:forHome:completionHandler:]_block_invoke.221
- ___77-[HMAudioAnalysisEventBulletinBoardNotification commitWithCompletionHandler:]_block_invoke.19
- ___77-[HMAudioAnalysisEventBulletinBoardNotification commitWithCompletionHandler:]_block_invoke.21
- ___78-[HMCameraClipManager fetchFaceCropURLForSignificantEventWithUUID:completion:]_block_invoke.184
- ___78-[HMCameraClipManager fetchFaceCropURLForSignificantEventWithUUID:completion:]_block_invoke.185
- ___79-[HMCameraRecordingEventManager fetchCountOfEventsWithDateInterval:completion:]_block_invoke.19
- ___82-[HMCameraClipManager fetchHeroFrameDataRepresentationForClipWithUUID:completion:]_block_invoke.168
- ___82-[HMCameraClipManager fetchHeroFrameDataRepresentationForClipWithUUID:completion:]_block_invoke.169
- ___82-[HMCameraRecordingReachabilityEventManager deleteAllEventsWithCompletionHandler:]_block_invoke.81
- ___88-[HMHome(HMAccessory) addAccessoryWithAccessorySetupPayload:progress:completionHandler:]_block_invoke.1576
- ___88-[HMHome(HMAccessory) addAndSetUpNewAccessoriesWithSuggestedRoomName:completionHandler:]_block_invoke.1567
- ___88-[HMHome(HomeLocationFeedback) retrieveHomeKitLocationForFeedbackWithCompletionHandler:]_block_invoke.1862
- ___89-[HMHome(NetworkRouter) updateAccessoryNetworkProtectionGroup:protectionMode:completion:]_block_invoke.1832
- ___91-[HMCameraRecordingReachabilityEventManager fetchCountOfEventsWithDateInterval:completion:]_block_invoke.79
- ___93-[HMCameraClipManager fetchFaceCropDataRepresentationForSignificantEventWithUUID:completion:]_block_invoke.179
- ___93-[HMCameraClipManager fetchFaceCropDataRepresentationForSignificantEventWithUUID:completion:]_block_invoke.180
- ___93-[HMHomeManager _pingDeviceWithUUID:monitor:secure:restrictToLocalNetwork:completionHandler:]_block_invoke.651
- ___Block_byref_object_copy_.14400
- ___Block_byref_object_copy_.14713
- ___Block_byref_object_copy_.21392
- ___Block_byref_object_copy_.23446
- ___Block_byref_object_copy_.27573
- ___Block_byref_object_copy_.29320
- ___Block_byref_object_copy_.35844
- ___Block_byref_object_copy_.38692
- ___Block_byref_object_copy_.39756
- ___Block_byref_object_copy_.59891
- ___Block_byref_object_dispose_.14401
- ___Block_byref_object_dispose_.14714
- ___Block_byref_object_dispose_.21393
- ___Block_byref_object_dispose_.23447
- ___Block_byref_object_dispose_.27574
- ___Block_byref_object_dispose_.29321
- ___Block_byref_object_dispose_.35845
- ___Block_byref_object_dispose_.38693
- ___Block_byref_object_dispose_.39757
- ___Block_byref_object_dispose_.59892
- ___CoreAnalyticsLibraryCore_block_invoke.35958
- ___HMHomeConfirmResident
- ___IDSFoundationLibraryCore_block_invoke.39530
- ___UIKitLibraryCore_block_invoke.39771
- _____HMHomeConfirmResident_block_invoke
- _____HMHomeConfirmResident_block_invoke_2
- _____HMHomeConfirmResident_block_invoke_3
- _____HMHomeManagerRegisterForNotifications_block_invoke.1364
- _____processNextArchivedData_block_invoke.307
- _____requestFetch_block_invoke.158
- ___block_descriptor_65_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
- ___block_literal_global.101.35965
- ___block_literal_global.103
- ___block_literal_global.10514
- ___block_literal_global.1115
- ___block_literal_global.11503
- ___block_literal_global.1197
- ___block_literal_global.12.45521
- ___block_literal_global.121.48459
- ___block_literal_global.12472
- ___block_literal_global.12619
- ___block_literal_global.13073
- ___block_literal_global.13266
- ___block_literal_global.13833
- ___block_literal_global.14166
- ___block_literal_global.14484
- ___block_literal_global.15
- ___block_literal_global.15078
- ___block_literal_global.1584
- ___block_literal_global.16135
- ___block_literal_global.16666
- ___block_literal_global.16857
- ___block_literal_global.16989
- ___block_literal_global.17.17789
- ___block_literal_global.17151
- ___block_literal_global.1730
- ___block_literal_global.175
- ___block_literal_global.175.16165
- ___block_literal_global.1774
- ___block_literal_global.17796
- ___block_literal_global.18463
- ___block_literal_global.18868
- ___block_literal_global.19.14151
- ___block_literal_global.192
- ___block_literal_global.192.22669
- ___block_literal_global.19419
- ___block_literal_global.19743
- ___block_literal_global.20775
- ___block_literal_global.211
- ___block_literal_global.21430
- ___block_literal_global.21703
- ___block_literal_global.2199
- ___block_literal_global.22175
- ___block_literal_global.22390
- ___block_literal_global.22675
- ___block_literal_global.22810
- ___block_literal_global.23056
- ___block_literal_global.233
- ___block_literal_global.23307
- ___block_literal_global.23470
- ___block_literal_global.23562
- ___block_literal_global.240
- ___block_literal_global.26077
- ___block_literal_global.26212
- ___block_literal_global.266
- ___block_literal_global.26687
- ___block_literal_global.27435
- ___block_literal_global.27730
- ___block_literal_global.28069
- ___block_literal_global.28281
- ___block_literal_global.28559
- ___block_literal_global.28633
- ___block_literal_global.29502
- ___block_literal_global.29858
- ___block_literal_global.30.17779
- ___block_literal_global.30.7694
- ___block_literal_global.30129
- ___block_literal_global.30965
- ___block_literal_global.31333
- ___block_literal_global.32411
- ___block_literal_global.33.59235
- ___block_literal_global.33357
- ___block_literal_global.335
- ___block_literal_global.33588
- ___block_literal_global.33811
- ___block_literal_global.34760
- ___block_literal_global.35952
- ___block_literal_global.36202
- ___block_literal_global.3631
- ___block_literal_global.36538
- ___block_literal_global.37163
- ___block_literal_global.37965
- ___block_literal_global.38090
- ___block_literal_global.3831
- ___block_literal_global.38362
- ___block_literal_global.3922
- ___block_literal_global.39593
- ___block_literal_global.39687
- ___block_literal_global.40396
- ___block_literal_global.40585
- ___block_literal_global.41212
- ___block_literal_global.41838
- ___block_literal_global.42252
- ___block_literal_global.42571
- ___block_literal_global.43246
- ___block_literal_global.44133
- ___block_literal_global.445
- ___block_literal_global.45243
- ___block_literal_global.45533
- ___block_literal_global.45799
- ___block_literal_global.45993
- ___block_literal_global.46221
- ___block_literal_global.46926
- ___block_literal_global.47045
- ___block_literal_global.474
- ___block_literal_global.477
- ___block_literal_global.47776
- ___block_literal_global.479
- ___block_literal_global.48213
- ___block_literal_global.48547
- ___block_literal_global.49460
- ___block_literal_global.5093
- ___block_literal_global.52090
- ___block_literal_global.52793
- ___block_literal_global.54048
- ___block_literal_global.54683
- ___block_literal_global.5489
- ___block_literal_global.55214
- ___block_literal_global.55526
- ___block_literal_global.56023
- ___block_literal_global.56195
- ___block_literal_global.5625
- ___block_literal_global.56583
- ___block_literal_global.56827
- ___block_literal_global.58473
- ___block_literal_global.58639
- ___block_literal_global.58976
- ___block_literal_global.59241
- ___block_literal_global.59601
- ___block_literal_global.59889
- ___block_literal_global.60183
- ___block_literal_global.6143
- ___block_literal_global.632
- ___block_literal_global.6624
- ___block_literal_global.6898
- ___block_literal_global.700
- ___block_literal_global.702
- ___block_literal_global.72
- ___block_literal_global.73.21681
- ___block_literal_global.7359
- ___block_literal_global.7476
- ___block_literal_global.75.36155
- ___block_literal_global.76.25844
- ___block_literal_global.7712
- ___block_literal_global.8
- ___block_literal_global.809
- ___block_literal_global.8168
- ___block_literal_global.84.59903
- ___block_literal_global.863
- ___block_literal_global.8651
- ___block_literal_global.87
- ___block_literal_global.888
- ___block_literal_global.8932
- ___block_literal_global.9109
- ___block_literal_global.9538
- ___block_literal_global.957
- ___block_literal_global.959
- ___block_literal_global.962
- ___block_literal_global.9802
- ___getAnalyticsSendEventLazySymbolLoc_block_invoke.35955
- ___getNSCharacterEncodingDocumentAttributeSymbolLoc_block_invoke.39766
- ___getNSDocumentTypeDocumentAttributeSymbolLoc_block_invoke.39760
- __serializeReportContext
- __unnamed_array_storage.14417
- __unnamed_array_storage.179
- __unnamed_array_storage.219
- __unnamed_array_storage.220
- __unnamed_array_storage.224
- __unnamed_array_storage.22582
- __unnamed_array_storage.227.25991
- __unnamed_array_storage.228
- __unnamed_array_storage.232
- __unnamed_array_storage.236
- __unnamed_array_storage.239.25990
- __unnamed_array_storage.240
- __unnamed_array_storage.244
- __unnamed_array_storage.248
- __unnamed_array_storage.251.25994
- __unnamed_array_storage.252
- __unnamed_array_storage.256
- __unnamed_array_storage.260
- __unnamed_array_storage.26067
- __unnamed_array_storage.264
- __unnamed_array_storage.268
- __unnamed_array_storage.272
- __unnamed_array_storage.276
- __unnamed_array_storage.280
- __unnamed_array_storage.284
- __unnamed_array_storage.288
- __unnamed_array_storage.29199
- __unnamed_array_storage.292
- __unnamed_array_storage.296
- __unnamed_array_storage.300
- __unnamed_array_storage.304
- __unnamed_array_storage.308
- __unnamed_array_storage.314
- __unnamed_array_storage.315
- __unnamed_array_storage.327
- __unnamed_array_storage.328
- __unnamed_array_storage.332
- __unnamed_array_storage.336
- __unnamed_array_storage.340
- __unnamed_array_storage.344
- __unnamed_array_storage.348
- __unnamed_array_storage.352
- __unnamed_array_storage.356
- __unnamed_array_storage.360
- __unnamed_array_storage.364
- __unnamed_array_storage.368
- __unnamed_array_storage.372
- __unnamed_array_storage.376
- __unnamed_array_storage.380
- __unnamed_array_storage.384
- __unnamed_array_storage.388
- __unnamed_array_storage.392
- __unnamed_array_storage.396
- __unnamed_array_storage.400
- __unnamed_array_storage.404
- __unnamed_array_storage.408
- __unnamed_array_storage.412
- __unnamed_array_storage.416
- __unnamed_array_storage.54170
- __unnamed_array_storage.55651
- __unnamed_array_storage.59092
- _audit_stringCoreAnalytics.35961
- _audit_stringIDSFoundation.39532
- _audit_stringUIKit.39773
- _describeDataSyncState
- _describeServiceConfigurationState
- _getAnalyticsSendEventLazySymbolLoc.ptr.35954
- _getNSCharacterEncodingDocumentAttributeSymbolLoc.ptr.39765
- _getNSDocumentTypeDocumentAttributeSymbolLoc.ptr.39759
- _kBulletinBoardNotificationServiceGroupCodingKey
- _kBulletinBoardNotificationServiceGroupRequestKey
- _logCategory._hmf_once_t0.12618
- _logCategory._hmf_once_t0.21702
- _logCategory._hmf_once_t0.28280
- _logCategory._hmf_once_t0.28632
- _logCategory._hmf_once_t0.40395
- _logCategory._hmf_once_t0.40584
- _logCategory._hmf_once_t0.41211
- _logCategory._hmf_once_t0.56826
- _logCategory._hmf_once_t1.16988
- _logCategory._hmf_once_t1.18867
- _logCategory._hmf_once_t1.36178
- _logCategory._hmf_once_t1.41837
- _logCategory._hmf_once_t1.45520
- _logCategory._hmf_once_t1.47044
- _logCategory._hmf_once_t1.52089
- _logCategory._hmf_once_t15.56582
- _logCategory._hmf_once_t16.33587
- _logCategory._hmf_once_t16.58638
- _logCategory._hmf_once_t17.37957
- _logCategory._hmf_once_t19.13292
- _logCategory._hmf_once_t2.26211
- _logCategory._hmf_once_t2.29857
- _logCategory._hmf_once_t20.5624
- _logCategory._hmf_once_t22.23055
- _logCategory._hmf_once_t24.36532
- _logCategory._hmf_once_t25.23306
- _logCategory._hmf_once_t25.59600
- _logCategory._hmf_once_t26.48294
- _logCategory._hmf_once_t27.47775
- _logCategory._hmf_once_t27.55525
- _logCategory._hmf_once_t3.38089
- _logCategory._hmf_once_t3.59234
- _logCategory._hmf_once_t31.21429
- _logCategory._hmf_once_t31.58472
- _logCategory._hmf_once_t310
- _logCategory._hmf_once_t329
- _logCategory._hmf_once_t33.48572
- _logCategory._hmf_once_t339
- _logCategory._hmf_once_t34.14479
- _logCategory._hmf_once_t34.18462
- _logCategory._hmf_once_t35.34759
- _logCategory._hmf_once_t4.1208
- _logCategory._hmf_once_t4.5488
- _logCategory._hmf_once_t40
- _logCategory._hmf_once_t6.30964
- _logCategory._hmf_once_t6.33356
- _logCategory._hmf_once_t6.52792
- _logCategory._hmf_once_t64.54047
- _logCategory._hmf_once_t68
- _logCategory._hmf_once_t7.23561
- _logCategory._hmf_once_t7.46925
- _logCategory._hmf_once_t8.33810
- _logCategory._hmf_once_t8.43245
- _logCategory._hmf_once_t8.46011
- _logCategory._hmf_once_v1.12620
- _logCategory._hmf_once_v1.21704
- _logCategory._hmf_once_v1.28282
- _logCategory._hmf_once_v1.28634
- _logCategory._hmf_once_v1.40397
- _logCategory._hmf_once_v1.40586
- _logCategory._hmf_once_v1.41213
- _logCategory._hmf_once_v1.56828
- _logCategory._hmf_once_v16.56584
- _logCategory._hmf_once_v17.33589
- _logCategory._hmf_once_v17.58640
- _logCategory._hmf_once_v18.37958
- _logCategory._hmf_once_v2.16990
- _logCategory._hmf_once_v2.18869
- _logCategory._hmf_once_v2.36179
- _logCategory._hmf_once_v2.41839
- _logCategory._hmf_once_v2.45522
- _logCategory._hmf_once_v2.47046
- _logCategory._hmf_once_v2.52091
- _logCategory._hmf_once_v20.13293
- _logCategory._hmf_once_v21.5626
- _logCategory._hmf_once_v23.23057
- _logCategory._hmf_once_v25.36533
- _logCategory._hmf_once_v26.23308
- _logCategory._hmf_once_v26.59602
- _logCategory._hmf_once_v27.48295
- _logCategory._hmf_once_v28.47777
- _logCategory._hmf_once_v28.55527
- _logCategory._hmf_once_v3.26213
- _logCategory._hmf_once_v3.29859
- _logCategory._hmf_once_v311
- _logCategory._hmf_once_v32.21431
- _logCategory._hmf_once_v32.58474
- _logCategory._hmf_once_v330
- _logCategory._hmf_once_v34.48573
- _logCategory._hmf_once_v340
- _logCategory._hmf_once_v35.14480
- _logCategory._hmf_once_v35.18464
- _logCategory._hmf_once_v36.34761
- _logCategory._hmf_once_v4.38091
- _logCategory._hmf_once_v4.59236
- _logCategory._hmf_once_v41
- _logCategory._hmf_once_v5.1209
- _logCategory._hmf_once_v5.5490
- _logCategory._hmf_once_v65.54049
- _logCategory._hmf_once_v69
- _logCategory._hmf_once_v7.30966
- _logCategory._hmf_once_v7.33358
- _logCategory._hmf_once_v7.52794
- _logCategory._hmf_once_v8.23563
- _logCategory._hmf_once_v8.46927
- _logCategory._hmf_once_v9.33812
- _logCategory._hmf_once_v9.43247
- _logCategory._hmf_once_v9.46012
- _objc_msgSend$__configureWithContext:cameraUserSettings:
- _objc_msgSend$_addIdentifier:bridgeUUID:
- _objc_msgSend$_callServiceGroupUpdate
- _objc_msgSend$_copyFrom:
- _objc_msgSend$_createControls:
- _objc_msgSend$_findObjects
- _objc_msgSend$_handleBulletinBoardNotificationServiceGroupUpdateNotification:
- _objc_msgSend$_notifyDelegateOfAppDataUpdateForService:
- _objc_msgSend$_processHomeConfigurationRequest:refreshRequested:
- _objc_msgSend$_requestServiceGroup
- _objc_msgSend$_shouldDisplayiCloudSwitchWithCompletionHandler:
- _objc_msgSend$_updateHomes:
- _objc_msgSend$_updateValue:updateTime:messageSentDate:
- _objc_msgSend$accessory:didUpdateBulletinBoardNotificationServiceGroupForService:
- _objc_msgSend$actionFromProtoBuf:home:
- _objc_msgSend$addHapCategories:
- _objc_msgSend$addHapCharacteristics:
- _objc_msgSend$addHapServices:
- _objc_msgSend$addMediaProfiles:
- _objc_msgSend$addObserver:
- _objc_msgSend$associatedServiceUUIDs
- _objc_msgSend$associatedServices
- _objc_msgSend$cameraProfileUUIDs
- _objc_msgSend$cameraProfiles
- _objc_msgSend$clearHapCategories
- _objc_msgSend$clearHapCharacteristics
- _objc_msgSend$clearHapServices
- _objc_msgSend$clearMediaProfiles
- _objc_msgSend$didUpdateHomes
- _objc_msgSend$hapCategories
- _objc_msgSend$hapCategoriesAtIndex:
- _objc_msgSend$hapCategoriesCount
- _objc_msgSend$hapCharacteristics
- _objc_msgSend$hapCharacteristicsAtIndex:
- _objc_msgSend$hapCharacteristicsCount
- _objc_msgSend$hapServices
- _objc_msgSend$hapServicesAtIndex:
- _objc_msgSend$hapServicesCount
- _objc_msgSend$hasPlaybackArchive
- _objc_msgSend$hasVolume
- _objc_msgSend$initWithBulletinBoardNotification:
- _objc_msgSend$initWithEnabled:condition:
- _objc_msgSend$initWithFormat:
- _objc_msgSend$initWithType:
- _objc_msgSend$isSubsetOfSet:
- _objc_msgSend$mediaPlaybackState
- _objc_msgSend$mediaProfilesAtIndex:
- _objc_msgSend$mediaProfilesCount
- _objc_msgSend$notificationServiceGroup
- _objc_msgSend$numberWithUnsignedInt:
- _objc_msgSend$removeObjectsForKeys:
- _objc_msgSend$sendConfigureBulletinNotification
- _objc_msgSend$setAccessoryProfiles:
- _objc_msgSend$setAssociatedServiceUUIDs:
- _objc_msgSend$setAssociatedServices:
- _objc_msgSend$setCameraProfileUUIDs:
- _objc_msgSend$setCameraProfiles:
- _objc_msgSend$setCommissioningID:
- _objc_msgSend$setDeviceIdentifier:
- _objc_msgSend$setDidUpdateHomes:
- _objc_msgSend$setFrameworkMergeComplete:
- _objc_msgSend$setMediaPlaybackState:
- _objc_msgSend$setMediaProfiles:
- _objc_msgSend$setPlaybackArchive:
- _objc_msgSend$smartNotificationBulletin
- _objc_msgSend$smartNotificationBulletinForSettings:
- _objc_msgSend$snapshotControlInternal
- _objc_msgSend$streamControlInternal
- _sharedInstance.onceToken.37964
- _sharedManager.onceToken.55668
- _supportedValueClasses.onceToken.45798
- _supportedValueClasses.onceToken.54013
- _supportedValueClasses.supportedValueClasses.45800
- _supportedValueClasses.supportedValueClasses.54014
- _unconfigureQueue.onceToken.36537
- _unconfigureQueue.unconfigureQueue.36539
CStrings:
+ "\x11\x13\x11C1/\x02G"
+ "\x11\x17\x1f"
+ "\x11\"\x12\x13"
+ "\x12\x12!\x12\""
+ "\x13\x11"
+ "%{public}@%{public}@Failed to fetch is cloud storage enabled: %@"
+ "%{public}@%{public}@Failed to update cloud storage: %@"
+ "%{public}@%{public}@Fetching is cloud storage enabled"
+ "%{public}@%{public}@Setting cloud storage to %@"
+ "%{public}@%{public}@Successfully fetched is cloud storage enabled: %@"
+ "%{public}@%{public}@Successfully set cloud storage to %@"
+ "%{public}@Adding busy status to updated status because home manager generation counter %lu does not match client's value of %lu"
+ "%{public}@Adding queued accessory: %@"
+ "%{public}@Cannot determine network router status because main WAN status TLV has a nil status value: %@"
+ "%{public}@Cannot determine network router status because main WAN status could not be found in WAN status list"
+ "%{public}@Cannot process home configuration response missing generation counter (%@) or metadata version (%@)"
+ "%{public}@Client has registered for didAddAccessory delegate callback : %@, home: %@"
+ "%{public}@Committing audio analysis event bulletin board notification using message %@: %@"
+ "%{public}@Configuring HMAudioAnalysisEventBulletinBoardNotification with context %@"
+ "%{public}@Could not find HMRoom for updated room UUID via merge: %@"
+ "%{public}@Could not find accessory for characteristic updated accessory UUID: %@"
+ "%{public}@Could not find characteristic for characteristic updated characteristic ID: %@"
+ "%{public}@Could not find room with UUID %@ for added accessory"
+ "%{public}@Could not find service for characteristic updated service ID: %@"
+ "%{public}@Could not initialize from decoded service: %@, accessory: %@"
+ "%{public}@Failed to deserialize homes from home configuration data: %@"
+ "%{public}@Failed to parse WAN status list from data %@: %@"
+ "%{public}@Failed to remove cache file %@: %@"
+ "%{public}@Handling accessory added message: %@"
+ "%{public}@Handling multiple characteristic values updated message %@ with payload: %@"
+ "%{public}@Handling status updated message with generation counter: %@, status: %@"
+ "%{public}@KVO reliance on '_didUpdateHomes' is unsupported and will be removed in a future release"
+ "%{public}@Notifying client of accessory did update application data with delegate: %@"
+ "%{public}@Notifying client of did add accessory: %@ delegate: %@, home: %@"
+ "%{public}@Received accessory added message with no accessories list: %@"
+ "%{public}@Received added accessory info with invalid accessoryUUID: %@, accessoryData: %@"
+ "%{public}@Removing home data cache file with version %@ not equal to current version %ld: %@"
+ "%{public}@Removing metadata cache file with version %@ not equal to current version %ld: %@"
+ "%{public}@Skipping adding unarchived accessory %@ because the home already has an existing matching accessory: %@"
+ "%{public}@Status update message payload missing generation counter and/or status number: %@"
+ "%{public}@Updated application data"
+ "%{public}@Updating application data via merge"
+ "%{public}@Updating associated service type via merge to %@"
+ "%{public}@Updating characteristic value from %@ -> %@ with value updated date: %@"
+ "%{public}@Updating configuration state via merge to %@"
+ "%{public}@Updating configured name via merge to %@"
+ "%{public}@Updating default name via merge to %@"
+ "%{public}@Updating is user interactive via merge to %@"
+ "%{public}@Updating last known operating state value and abnormal reasons value via merge to %@ and %@"
+ "%{public}@Updating matter endpoint ID via merge to %@"
+ "%{public}@Updating media display order via merge to %@"
+ "%{public}@Updating media source display order modifiable via merge to %@"
+ "%{public}@Updating media source identifier via merge to %@"
+ "%{public}@Updating name via merge to %@"
+ "%{public}@Updating service subtype via merge to %@"
+ "%{public}@Updating service type via merge to %@"
+ "%{public}@Updating status from %@ -> %@ (initial merge complete: %@)"
+ "%{public}@WAN status TLV has a nil identifier value: %@"
+ "%{public}@supportsResidentActionSetStateEvaluation value updated to %@"
+ "-[HMHome confirmResidentWithCompletion:]"
+ "-[HMHome updateResidentSelectionVersion:completion:]"
+ "-[HMHomeManager addEphemeralContainerWithName:completion:]"
+ "-[HMHomeManager deactivateEphemeralContainerWithName:completion:]"
+ "-[HMHomeManager deleteEphemeralContainerWithName:completion:]"
+ "-[HMHomeManager readCountersForGroup:homeUUIDString:accessoryUUIDString:counter:statistics:datePartition:ephemeralContainerName:completion:]"
+ "-[HMHomeManager startupEphemeralContainerWithName:completion:]"
+ "0000020A-0000-1000-8000-0026BB765291"
+ "0000020E-0000-1000-8000-0026BB765291"
+ "0000020F-0000-1000-8000-0026BB765291"
+ "00000212-0000-1000-8000-0026BB765291"
+ "0000021E-0000-1000-8000-0026BB765291"
+ "1A\x15X%\x15\x17"
+ "1Q"
+ "<HMNetworkRouterWANStatus identifier=%@, status=%@>"
+ "<HMNetworkRouterWANStatusList statuses=%@>"
+ "<Software Update, Version = %@, Displayable Version = %@, State = %@, Download Size = %@, Documentation Metadata = %@, Release Date = %@, Update Type = %@>"
+ "<Unknown symptom type: %ld>"
+ "<Unknown value: %ld>"
+ "<Unknown value: %lu>"
+ "@\"HAPTLVUnsignedNumberValue\""
+ "@28@0:8@16{_HMResidentCapabilitiesStruct=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}24"
+ "@36@0:8B16@20@28"
+ "@44@0:8B16@20@28@36"
+ "@72@0:8@16@24Q32q40d48@56@64"
+ "Asked to set invalid value for recurrenceDays: %ld"
+ "B32@?0@\"HMNetworkRouterWANStatus\"8Q16^B24"
+ "BulletinBoardNotification"
+ "Condition"
+ "Fetching is cloud storage enabled"
+ "HAPTLVUnsignedNumberValue"
+ "HH1State"
+ "HH2State"
+ "HM.SetResidentSelectionVersion"
+ "HM.accessoryAdded"
+ "HM.displayableFirmwareVersion"
+ "HM.displayableVersion"
+ "HM.v"
+ "HMA.audioAnalysisEventBulletinBoardNotificationCondition"
+ "HMA.audioAnalysisEventBulletinBoardNotificationEnabled"
+ "HMCCM.m.ficse"
+ "HMCCM.m.ucs"
+ "HMCMM.mk.ie"
+ "HMCameraSnapshotMostRecentSnapshotUpdatedMessage"
+ "HMErrorFromOSStatus"
+ "HMFObjectCacheHMSettingLanguageValue"
+ "HMHM.deleteHH2Entity"
+ "HMHM.queryiCloudSwitchState"
+ "HMHM.updateiCloudSwitchState"
+ "HMHomeMessageKeyAuthData"
+ "HMHomeSupportsResidentActionSetStateEvaluationCodingKey"
+ "HMNetworkRouterWANStatus"
+ "HMNetworkRouterWANStatusList"
+ "HMResidentDeviceDeviceIRKDataCodingKey"
+ "IDSIdentifier"
+ "NetworkRouterInternal"
+ "Q24@0:8q16"
+ "Q32@0:8q16@24"
+ "StringAsLastKnownControllerHH2Mode:"
+ "StringAsLastKnownControllerSentinelZoneExistence:"
+ "SysDrop AirDrop Event"
+ "SysDrop Cancel Event"
+ "SysDrop Sysdiagnose Event"
+ "T@\"<HMHomeDelegatePrivate>\",R"
+ "T@\"HAPTLVUnsignedNumberValue\",&,N,V_identifier"
+ "T@\"HAPTLVUnsignedNumberValue\",&,N,V_status"
+ "T@\"HMDevice\",&"
+ "T@\"HMMutableArray\",R,N,V_currentAccessories"
+ "T@\"HMMutableArray\",R,N,V_currentActionSets"
+ "T@\"HMMutableArray\",R,N,V_currentTriggers"
+ "T@\"HMSoftwareUpdateV2\",R,C,N"
+ "T@\"NSArray\",?,R,C,N"
+ "T@\"NSData\",R,C,V_deviceIRKData"
+ "T@\"NSMapTable\",R,V_delegateCallersByObservers"
+ "T@\"NSMutableArray\",&,N,V_statuses"
+ "T@\"NSNumber\",R,N,V_matterEndpointID"
+ "T@\"NSObject<OS_dispatch_queue>\",?,R,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",C,V_IDSDestination"
+ "T@\"NSString\",R,C,V_displayableVersion"
+ "T@\"NSUUID\",C,V_IDSIdentifier"
+ "T@\"NSUUID\",R,N,V_messageTargetUUID"
+ "TB,N,GisInitialMergeComplete,V_initialMergeComplete"
+ "TB,N,GisUserInteractive,V_userInteractive"
+ "TB,N,V_supportsActivityLoggingOnPrimary"
+ "TB,N,V_supportsResidentActionSetStateEvaluation"
+ "TQ,N,V_sfProblemFlags"
+ "Ti,N,V_lastKnownControllerHH2Mode"
+ "Ti,N,V_lastKnownControllerSentinelZoneExistence"
+ "T{_HMResidentCapabilitiesStruct=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1},R,N,V_capabilities"
+ "Updating cloud storage"
+ "_IDSDestination"
+ "_IDSIdentifier"
+ "_createControlsWithMostRecentSnapshot:"
+ "_delegateCallersByObservers"
+ "_displayableVersion"
+ "_initialMergeComplete"
+ "_lastKnownControllerHH2Mode"
+ "_lastKnownControllerSentinelZoneExistence"
+ "_matterEndpointID"
+ "_processHomeConfigurationResponse:refreshRequested:"
+ "_removeActionSetsForAccessory:"
+ "_removeActionsForAccessory:"
+ "_removeCacheFileAtPath:"
+ "_removeEventsForAccessory:"
+ "_setInitialHomes:"
+ "_sfProblemFlags"
+ "_statuses"
+ "_supportsActivityLoggingOnPrimary"
+ "_supportsResidentActionSetStateEvaluation"
+ "_updateValue:valueUpdatedDate:"
+ "absoluteURL"
+ "addEphemeralContainerWithName:completion:"
+ "addObserver:queue:"
+ "audio.analysis.bulletin.board"
+ "cachedInstanceForLanguageSettingValue:"
+ "camera.bulletin.board"
+ "com.apple.HomeKit.SetupFollowUp"
+ "com.apple.HomeKitQA.HomeIntegration"
+ "confirmResidentWithCompletion:"
+ "createSmartNotificationBulletin"
+ "deactivateEphemeralContainerWithName:completion:"
+ "delegateCallersByObservers"
+ "deleteEphemeralContainerWithName:completion:"
+ "displayableVersion"
+ "eSimExternal2FAStart"
+ "eSimExternal2FAStop"
+ "ephemeralContainerName"
+ "fetchIsCloudStorageEnabledWithCompletion:"
+ "hasLastKnownControllerHH2Mode"
+ "hasLastKnownControllerSentinelZoneExistence"
+ "hasSfProblemFlags"
+ "hasSupportsActivityLoggingOnPrimary"
+ "hasSupportsResidentActionSetStateEvaluation"
+ "hm_truncatedDisplayableVersionString"
+ "home:didUpdateSupportsResidentActionSetStateEvaluation:"
+ "index.xpc.client.spi.settings"
+ "initWithEnabled:condition:accessoryIdentifier:"
+ "initWithEnabled:condition:context:cameraUserSettings:"
+ "initWithEnabled:condition:service:messageTargetUUID:"
+ "initWithIdentifier:status:"
+ "initWithStatuses:"
+ "initWithVersion:displayableVersion:downloadSize:state:installDuration:documentationMetadata:releaseDate:"
+ "initialMergeComplete"
+ "isInitialMergeComplete"
+ "lastKnownControllerHH2Mode"
+ "lastKnownControllerHH2ModeAsString:"
+ "lastKnownControllerSentinelZoneExistence"
+ "lastKnownControllerSentinelZoneExistenceAsString:"
+ "matterEndpointID"
+ "modelId"
+ "networkRouterStatusFromRouterStatus:wanStatusListData:"
+ "networkRouterStatusFromWiFiSatelliteStatus:"
+ "parseFromData:error:"
+ "parsedFromData:error:"
+ "predicateForOptions:"
+ "readCountersForGroup:homeUUIDString:accessoryUUIDString:counter:statistics:datePartition:ephemeralContainerName:completion:"
+ "serializeWithError:"
+ "serviceMatterEndpointID"
+ "setCloudStorageEnabled:completion:"
+ "setHasLastKnownControllerHH2Mode:"
+ "setHasLastKnownControllerSentinelZoneExistence:"
+ "setHasSfProblemFlags:"
+ "setHasSupportsActivityLoggingOnPrimary:"
+ "setHasSupportsResidentActionSetStateEvaluation:"
+ "setIDSDestination:"
+ "setIDSIdentifier:"
+ "setInitialMergeComplete:"
+ "setLastKnownControllerHH2Mode:"
+ "setLastKnownControllerSentinelZoneExistence:"
+ "setMatterEndpointID:"
+ "setSfProblemFlags:"
+ "setStatuses:"
+ "setSupportsActivityLoggingOnPrimary:"
+ "setSupportsResidentActionSetStateEvaluation:"
+ "setUserInteractive:"
+ "sfProblemFlags"
+ "shortVersionString"
+ "softwareUpdate"
+ "softwareUpdateFromDescriptor:"
+ "startupEphemeralContainerWithName:completion:"
+ "statuses"
+ "supportsActivityLoggingOnPrimary"
+ "supportsResidentActionSetStateEvaluation"
+ "updateResidentSelectionVersion:completion:"
+ "xpcTransport"
+ "{?=\"accessoryAddMSHH2\"b1\"accountSettleWaitMSHH2\"b1\"controllerKeyExchangeMSHH1\"b1\"currentDeviceIDSWaitMSHH2\"b1\"eventRouterFirstEventPushMSHH2\"b1\"eventRouterServerConnectionMSHH2\"b1\"firstCoreDataImportMSHH2\"b1\"homeManagerReadyMSHH2\"b1\"lastKnownStageErrorCode\"b1\"lastKnownStageUnderlyingErrorCode\"b1\"newAccessoryTransferMSHH1\"b1\"pairingIdentityCreationMSHH2\"b1\"primaryResidentElectionMSHH2\"b1\"savedEventState\"b1\"sentinelZoneFetchMSHH1\"b1\"sessionSetupCloseMSHH1\"b1\"sessionSetupOpenMSHH1\"b1\"settingsCreationMSHH2\"b1\"siriReadyMSHH2\"b1\"totalDurationMSHH1\"b1\"totalDurationMSHH2\"b1\"version\"b1\"iCloudAvailableINT\"b1\"iDSAvailableINT\"b1\"lastKnownControllerHH2Mode\"b1\"lastKnownControllerSentinelZoneExistence\"b1\"manateeAvailableINT\"b1\"networkAvailableINT\"b1}"
+ "{?=\"generationTime\"b1\"sfProblemFlags\"b1}"
+ "{?=\"supports5348b248a25f84b0c83e\"b1\"supportsAccessCodes\"b1\"supportsActivityLoggingOnPrimary\"b1\"supportsAnnounce\"b1\"supportsCHIP\"b1\"supportsCameraActivityZones\"b1\"supportsCameraPackageDetection\"b1\"supportsCameraRecording\"b1\"supportsCameraRecordingReachabilityNotifications\"b1\"supportsCameraSignificantEventNotifications\"b1\"supportsCustomMediaApplicationDestination\"b1\"supportsEventLog\"b1\"supportsFaceClassification\"b1\"supportsFirmwareUpdate\"b1\"supportsHomeHub\"b1\"supportsLockNotificationContext\"b1\"supportsMatterTTU\"b1\"supportsMediaActions\"b1\"supportsNaturalLighting\"b1\"supportsResidentActionSetStateEvaluation\"b1\"supportsResidentFirmwareUpdate\"b1\"supportsResidentFirstAccessoryCommunication\"b1\"supportsRouterManagement\"b1\"supportsShortcutActions\"b1\"supportsSiriEndpointSetup\"b1\"supportsThreadBorderRouter\"b1\"supportsThreadNetworkCredentialSharing\"b1\"supportsUnifiedMediaNotifications\"b1\"supportsWakeOnLAN\"b1\"supportsWalletKey\"b1}"
+ "{_HMResidentCapabilitiesStruct=\"supportsCameraRecording\"b1\"supportsRouterManagement\"b1\"supportsShortcutActions\"b1\"supportsMediaActions\"b1\"supportsCameraSignificantEventNotifications\"b1\"supportsFirmwareUpdate\"b1\"supportsResidentFirmwareUpdate\"b1\"supportsCameraActivityZones\"b1\"supportsFaceClassification\"b1\"supportsNaturalLighting\"b1\"supportsCameraRecordingReachabilityNotifications\"b1\"supportsAnnounce\"b1\"supportsWakeOnLAN\"b1\"supportsLockNotificationContext\"b1\"supportsWalletKey\"b1\"supportsCameraPackageDetection\"b1\"supportsAccessCodes\"b1\"supportsCHIP\"b1\"supportsThreadBorderRouter\"b1\"supportsSiriEndpointSetup\"b1\"supportsCustomMediaApplicationDestination\"b1\"supportsUnifiedMediaNotifications\"b1\"supportsHomeHub\"b1\"supportsResidentFirstAccessoryCommunication\"b1\"supportsThreadNetworkCredentialSharing\"b1\"supportsMatterSharedAdminPairing\"b1\"supportsEventLog\"b1\"supportsMatterTTU\"b1\"supportsResidentActionSetStateEvaluation\"b1}"
+ "{_HMResidentCapabilitiesStruct=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}16@0:8"
+ "\x91a"
+ "\x91\xf0\xf0\x11"
+ "\xa1"
+ "\xf0\x93"
- "\x11\x13\x11S1/\x02G"
- "\x11\x16\x1f"
- "\x11!\x11\x13"
- "\x12\x12!\x11\""
- "\x14\x12"
- "\x14\x14"
- "\x1d"
- " condition: %@"
- " enabled: %@"
- "%@ : %@"
- "%{public}@All associated service objects listed in %@ aren't there yet, will check back later. Current services %@"
- "%{public}@All camera profile objects listed in %@ aren't there yet, will check back later. Current cameras %@"
- "%{public}@Calling service notification group update delegate"
- "%{public}@Client has registered for didAddAccessory delegate callback : %@, home: %@, %p"
- "%{public}@Error occurred while unarchiving the keyed archived from daemon: %@"
- "%{public}@Failed to remove home data cache file %@: %@"
- "%{public}@Failed to remove metadata cache file %@: %@"
- "%{public}@Handle status update: Updating status to %@ / Merge complete: %@ / Final Status: %@ / Current Status: %@"
- "%{public}@Handling multiple characteristic values updated message (%@) with multiPartResponse: %@"
- "%{public}@Home %@'s accessories: %@"
- "%{public}@Merging due to associated service value change from %@ to %@"
- "%{public}@Merging due to camera profiles value change from %@ to %@"
- "%{public}@Note's object is not of type UUID"
- "%{public}@Notification is carrying UUID %@, home's UUID %@"
- "%{public}@Notifying client of did add accessory: %@ delegate: %@, home: %@, %p"
- "%{public}@Preserving status flags %lu because home manager generation counter %lu does not match client's value of %lu."
- "%{public}@Received BB notification service group update: %@"
- "%{public}@Removing home data cache file with version %@ lower than current version %ld"
- "%{public}@Removing metadata cache file with version %@ lower than current version %ld"
- "%{public}@Skipping adding unarchived accessory: %@ due to existing accessory: %@"
- "%{public}@Unconfiguring bulletinBoard notification service group"
- "%{public}@Updated current home: nil, Received empty response from sync"
- "%{public}@Updated status to %@, Merge complete: %@, Final Status: %@"
- "%{public}@Updating associated services to %@"
- "%{public}@Updating camera profiles to %@"
- "%{public}@configure HMAudioAnalysisEventBulletinBoardNotification with context %@ and accessory %@"
- "%{public}@handle status updated: generation counter from : %@ -> %@"
- "%{public}@newCameraProfiles %@"
- "%{public}@newServices %@"
- "-[HMBulletinBoardNotificationServiceGroup _requestServiceGroup]"
- "-[HMBulletinBoardNotificationServiceGroup handleConfigureNotification:]"
- "-[HMHome sendConfigureBulletinNotification]"
- "-[HMHomeManager _shouldDisplayiCloudSwitchWithCompletionHandler:]"
- "-[HMHomeManager addEphemeralContainer:completion:]"
- "-[HMHomeManager deactivateEphemeralContainer:completion:]"
- "-[HMHomeManager deleteEphemeralContainer:completion:]"
- "-[HMHomeManager readCountersForGroup:homeUUIDString:accessoryUUIDString:counter:statistics:datePartition:ephemeralContainer:completion:]"
- "-[HMHomeManager shouldDisplayiCloudSwitchWithCompletionHandler:]"
- "-[HMHomeManager startupEphemeralContainer:completion:]"
- "1A\x15X'\x14\x16"
- "<Software Update, Version = %@, State = %@, Download Size = %@, Documentation Metadata = %@, Release Date = %@, Update Type = %@>"
- "<Unknown state>"
- "@\"HMBulletinBoardNotificationServiceGroup\""
- "@28@0:8@16{_HMResidentCapabilitiesStruct=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}24"
- "@28@0:8B16@20"
- "FtswpMzGQrpRXPQGOUFUUG"
- "HAPAuthenticationEnhancement"
- "HAPAuthenticationEnhancementEnabled"
- "HM.BulletinBoardNotificationCameraProfiles"
- "HM.BulletinBoardNotificationServiceGroup"
- "HM.BulletinBoardNotificationServices"
- "HMBulletinBoardNotificationServiceGroup"
- "HMHomeEnableExpressForWalletKeyMessageKeyAuthData"
- "T@\"HMBulletinBoardNotification\",R,W,N,V_bulletinBoardNotification"
- "T@\"HMBulletinBoardNotificationServiceGroup\",R,N,V_notificationServiceGroup"
- "T@\"HMMutableArray\",&,N,V_currentAccessories"
- "T@\"HMMutableArray\",&,N,V_currentTriggers"
- "T@\"NSArray\",&,N,V_associatedServices"
- "T@\"NSArray\",&,N,V_cameraProfiles"
- "T@\"NSData\",&,N,V_playbackArchive"
- "T@\"NSData\",&,N,V_volume"
- "T@\"NSMutableArray\",&,N,V_hapCategories"
- "T@\"NSMutableArray\",&,N,V_hapCharacteristics"
- "T@\"NSMutableArray\",&,N,V_hapServices"
- "T@\"NSMutableArray\",&,N,V_mediaProfiles"
- "T@\"NSObject<OS_dispatch_queue>\",R,N"
- "T@\"NSSet\",&,N,V_associatedServiceUUIDs"
- "T@\"NSSet\",&,N,V_cameraProfileUUIDs"
- "T@\"NSString\",R,C,N,V_logID"
- "T@\"NSUUID\",C,V_accessoryIdentifier"
- "T@\"NSUUID\",R,C,N,V_targetUUID"
- "T@\"_HMCameraSnapshotControl\",R,V_snapshotControlInternal"
- "T@\"_HMCameraStreamControl\",R,V_streamControlInternal"
- "TB,N,V_didUpdateHomes"
- "TB,N,V_frameworkMergeComplete"
- "TB,R,N,GisUserInteractive,V_userInteractive"
- "Ti,N,V_identifier"
- "Ti,N,V_mediaPlaybackState"
- "Ti,N,V_version"
- "T{_HMResidentCapabilitiesStruct=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1},R,N,V_capabilities"
- "Unknown HMSymptomType %tu"
- "UnknownState(%@)"
- "__HMHomeConfirmResident"
- "__configureWithContext:cameraUserSettings:"
- "_addIdentifier:bridgeUUID:"
- "_associatedServiceUUIDs"
- "_associatedServices"
- "_bulletinBoardNotification"
- "_callServiceGroupUpdate"
- "_cameraProfileUUIDs"
- "_cameraProfiles"
- "_copyFrom:"
- "_createControls:"
- "_findObjects"
- "_frameworkMergeComplete"
- "_handleBulletinBoardNotificationServiceGroupUpdateNotification:"
- "_logID"
- "_notificationServiceGroup"
- "_notifyDelegateOfAppDataUpdateForService:"
- "_processHomeConfigurationRequest:refreshRequested:"
- "_requestServiceGroup"
- "_shouldDisplayiCloudSwitchWithCompletionHandler:"
- "_snapshotControlInternal"
- "_streamControlInternal"
- "_targetUUID"
- "_updateHomes:"
- "_updateValue:updateTime:messageSentDate:"
- "accessory:didUpdateBulletinBoardNotificationServiceGroupForService:"
- "actionFromProtoBuf:home:"
- "addEphemeralContainer:completion:"
- "addHapCategories:"
- "addHapCharacteristics:"
- "addHapServices:"
- "addMediaProfiles:"
- "associatedServiceUUIDs"
- "associatedServices"
- "bulletin"
- "bulletin.service.group"
- "cameraProfileUUIDs"
- "clearHapCategories"
- "clearHapCharacteristics"
- "clearHapServices"
- "clearMediaProfiles"
- "deactivateEphemeralContainer:completion:"
- "deleteEphemeralContainer:completion:"
- "didUpdateHomes"
- "ephemeralContainer"
- "frameworkMergeComplete"
- "handleConfigureNotification:"
- "hapCategoriesAtIndex:"
- "hapCategoriesCount"
- "hapCategoriesType"
- "hapCharacteristicsAtIndex:"
- "hapCharacteristicsCount"
- "hapCharacteristicsType"
- "hapServicesAtIndex:"
- "hapServicesCount"
- "hapServicesType"
- "hasCatDescription"
- "hasChrDescription"
- "hasMediaPlaybackState"
- "hasPlaybackArchive"
- "hasSvcDescription"
- "hasUuidStr"
- "initWithBulletinBoardNotification:"
- "initWithEnabled:condition:"
- "initWithFormat:"
- "invalid recurrenceDays"
- "isSubsetOfSet:"
- "kAccessoryAddedNotificationKey"
- "kBulletinBoardNotificationServiceGroupRequestKey"
- "kBulletinBoardNotificationServiceGroupUpdateNotificationKey"
- "kCharacteristicValueUpdateTime"
- "kConfigureBulletinBoardNotification"
- "kMostRecentSnapshotUpdatedNotificationKey"
- "kQueryiCloudSwitchStateRequestKey"
- "kShouldDisplayiCloudSwitchStateRequestKey"
- "kUpdateiCloudSwitchStateRequestKey"
- "logID"
- "mediaProfilesAtIndex:"
- "mediaProfilesCount"
- "mediaProfilesType"
- "notificationServiceGroup"
- "numberWithUnsignedInt:"
- "readCountersForGroup:homeUUIDString:accessoryUUIDString:counter:statistics:datePartition:ephemeralContainer:completion:"
- "removeObjectsForKeys:"
- "sendConfigureBulletinNotification"
- "setAssociatedServiceUUIDs:"
- "setAssociatedServices:"
- "setCameraProfileUUIDs:"
- "setCameraProfiles:"
- "setCurrentAccessories:"
- "setCurrentTriggers:"
- "setDidUpdateHomes:"
- "setFrameworkMergeComplete:"
- "setHapCategories:"
- "setHapCharacteristics:"
- "setHapServices:"
- "setHasIdentifier:"
- "setHasMediaPlaybackState:"
- "setMediaPlaybackState:"
- "shouldDisplayiCloudSwitchWithCompletionHandler:"
- "smartNotificationBulletinForSettings:"
- "snapshotControlInternal"
- "startupEphemeralContainer:completion:"
- "streamControlInternal"
- "symptomWithType:"
- "xpcMessageCounters"
- "{?=\"accessoryAddMSHH2\"b1\"accountSettleWaitMSHH2\"b1\"controllerKeyExchangeMSHH1\"b1\"currentDeviceIDSWaitMSHH2\"b1\"eventRouterFirstEventPushMSHH2\"b1\"eventRouterServerConnectionMSHH2\"b1\"firstCoreDataImportMSHH2\"b1\"homeManagerReadyMSHH2\"b1\"lastKnownStageErrorCode\"b1\"lastKnownStageUnderlyingErrorCode\"b1\"newAccessoryTransferMSHH1\"b1\"pairingIdentityCreationMSHH2\"b1\"primaryResidentElectionMSHH2\"b1\"savedEventState\"b1\"sentinelZoneFetchMSHH1\"b1\"sessionSetupCloseMSHH1\"b1\"sessionSetupOpenMSHH1\"b1\"settingsCreationMSHH2\"b1\"siriReadyMSHH2\"b1\"totalDurationMSHH1\"b1\"totalDurationMSHH2\"b1\"version\"b1\"iCloudAvailableINT\"b1\"iDSAvailableINT\"b1\"manateeAvailableINT\"b1\"networkAvailableINT\"b1}"
- "{?=\"generationTime\"b1}"
- "{?=\"supports5348b248a25f84b0c83e\"b1\"supportsAccessCodes\"b1\"supportsAnnounce\"b1\"supportsCHIP\"b1\"supportsCameraActivityZones\"b1\"supportsCameraPackageDetection\"b1\"supportsCameraRecording\"b1\"supportsCameraRecordingReachabilityNotifications\"b1\"supportsCameraSignificantEventNotifications\"b1\"supportsCustomMediaApplicationDestination\"b1\"supportsEventLog\"b1\"supportsFaceClassification\"b1\"supportsFirmwareUpdate\"b1\"supportsHomeHub\"b1\"supportsLockNotificationContext\"b1\"supportsMatterTTU\"b1\"supportsMediaActions\"b1\"supportsNaturalLighting\"b1\"supportsResidentFirmwareUpdate\"b1\"supportsResidentFirstAccessoryCommunication\"b1\"supportsRouterManagement\"b1\"supportsShortcutActions\"b1\"supportsSiriEndpointSetup\"b1\"supportsThreadBorderRouter\"b1\"supportsThreadNetworkCredentialSharing\"b1\"supportsUnifiedMediaNotifications\"b1\"supportsWakeOnLAN\"b1\"supportsWalletKey\"b1}"
- "{_HMResidentCapabilitiesStruct=\"supportsCameraRecording\"b1\"supportsRouterManagement\"b1\"supportsShortcutActions\"b1\"supportsMediaActions\"b1\"supportsCameraSignificantEventNotifications\"b1\"supportsFirmwareUpdate\"b1\"supportsResidentFirmwareUpdate\"b1\"supportsCameraActivityZones\"b1\"supportsFaceClassification\"b1\"supportsNaturalLighting\"b1\"supportsCameraRecordingReachabilityNotifications\"b1\"supportsAnnounce\"b1\"supportsWakeOnLAN\"b1\"supportsLockNotificationContext\"b1\"supportsWalletKey\"b1\"supportsCameraPackageDetection\"b1\"supportsAccessCodes\"b1\"supportsCHIP\"b1\"supportsThreadBorderRouter\"b1\"supportsSiriEndpointSetup\"b1\"supportsCustomMediaApplicationDestination\"b1\"supportsUnifiedMediaNotifications\"b1\"supportsHomeHub\"b1\"supportsResidentFirstAccessoryCommunication\"b1\"supportsThreadNetworkCredentialSharing\"b1\"supportsMatterSharedAdminPairing\"b1\"supportsEventLog\"b1\"supportsMatterTTU\"b1}"
- "{_HMResidentCapabilitiesStruct=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}16@0:8"
- "\x91Q"
- "\x91\xf0\xf0!"
- "\xb1"
- "\xf0\x83"

```
