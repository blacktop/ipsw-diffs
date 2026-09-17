## HomeKit

> `/System/Library/PrivateFrameworks/HomeKit.framework/Versions/A/HomeKit`

```diff

-1493.1.5.4.1
-  __TEXT.__text: 0x3e20f8
-  __TEXT.__objc_methlist: 0x281ec
-  __TEXT.__const: 0x6818
+1514.0.0.0.1
+  __TEXT.__text: 0x3f6240
+  __TEXT.__objc_methlist: 0x28764
+  __TEXT.__const: 0x7578
   __TEXT.__dlopen_cstrs: 0x3bb
-  __TEXT.__swift5_typeref: 0x1fe8
-  __TEXT.__cstring: 0x2eddf
-  __TEXT.__constg_swiftt: 0x1c98
-  __TEXT.__swift5_reflstr: 0x1195
-  __TEXT.__swift5_fieldmd: 0x1474
+  __TEXT.__swift5_typeref: 0x231a
+  __TEXT.__cstring: 0x2fb49
+  __TEXT.__constg_swiftt: 0x1fb4
+  __TEXT.__swift5_reflstr: 0x1535
+  __TEXT.__swift5_fieldmd: 0x18e4
   __TEXT.__swift5_builtin: 0xa0
-  __TEXT.__swift5_assocty: 0x368
-  __TEXT.__swift5_capture: 0x9a4
+  __TEXT.__swift5_assocty: 0x3a8
+  __TEXT.__swift5_capture: 0x970
   __TEXT.__swift5_protos: 0x38
-  __TEXT.__swift5_proto: 0x4d0
-  __TEXT.__swift5_types: 0x1c4
-  __TEXT.__swift_as_entry: 0x1e8
-  __TEXT.__swift_as_ret: 0x22c
-  __TEXT.__swift_as_cont: 0x434
-  __TEXT.__oslogstring: 0x55954
+  __TEXT.__swift5_proto: 0x57c
+  __TEXT.__swift5_types: 0x214
+  __TEXT.__swift_as_entry: 0x1fc
+  __TEXT.__swift_as_ret: 0x240
+  __TEXT.__swift_as_cont: 0x444
+  __TEXT.__oslogstring: 0x56517
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__gcc_except_tab: 0x67a0
+  __TEXT.__gcc_except_tab: 0x67a4
   __TEXT.__ustring: 0x50
-  __TEXT.__unwind_info: 0xf070
-  __TEXT.__eh_frame: 0x7a18
+  __TEXT.__unwind_info: 0xf5c8
+  __TEXT.__eh_frame: 0x8050
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5978
+  __DATA_CONST.__const: 0x5ac8
   __DATA_CONST.__objc_classlist: 0x1338
   __DATA_CONST.__objc_catlist: 0x108
   __DATA_CONST.__objc_protolist: 0x558
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe000
+  __DATA_CONST.__objc_selrefs: 0xe2a0
   __DATA_CONST.__objc_protorefs: 0x110
   __DATA_CONST.__objc_superrefs: 0xf90
   __DATA_CONST.__objc_arraydata: 0x13f0
-  __DATA_CONST.__got: 0x1dd8
-  __AUTH_CONST.__const: 0x9e18
-  __AUTH_CONST.__cfstring: 0x2b340
-  __AUTH_CONST.__objc_const: 0x482b0
+  __DATA_CONST.__got: 0x1e30
+  __AUTH_CONST.__const: 0xa4c0
+  __AUTH_CONST.__cfstring: 0x2bd60
+  __AUTH_CONST.__objc_const: 0x48af8
   __AUTH_CONST.__objc_intobj: 0x9a8
   __AUTH_CONST.__objc_dictobj: 0x848
   __AUTH_CONST.__objc_arrayobj: 0x5d0
   __AUTH_CONST.__objc_doubleobj: 0x70
-  __AUTH_CONST.__auth_got: 0x1830
+  __AUTH_CONST.__auth_got: 0x18d8
   __AUTH.__objc_data: 0x8e00
-  __AUTH.__data: 0x17a8
-  __DATA.__objc_ivar: 0x27a4
-  __DATA.__data: 0x51f0
+  __AUTH.__data: 0x1a78
+  __DATA.__objc_ivar: 0x2814
+  __DATA.__data: 0x54e0
   __DATA.__common: 0x90
-  __DATA_DIRTY.__objc_data: 0x36f0
-  __DATA_DIRTY.__data: 0x80
-  __DATA_DIRTY.__bss: 0x218
+  __DATA_DIRTY.__objc_data: 0x36f8
+  __DATA_DIRTY.__data: 0x130
+  __DATA_DIRTY.__bss: 0x208
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /System/Library/PrivateFrameworks/StreamingZip.framework/Versions/A/StreamingZip
   - /System/Library/PrivateFrameworks/TCC.framework/Versions/A/TCC
+  - /System/Library/PrivateFrameworks/ToolKit.framework/Versions/A/ToolKit
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
+  - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 17435
-  Symbols:   32364
-  CStrings:  12192
+  Functions: 17857
+  Symbols:   32689
+  CStrings:  12348
 
Symbols:
+ +[HMAccessory(CameraInternal) _cameraProfilesForAccessoryProfiles:]
+ +[HMCoreAnalyticsMetricEventDispatcher logCategory]
+ +[HMMediaDestinationControllerData defaultGroupName]
+ +[HMRoom shortDescription]
+ +[HMSoftwareUpdateDocumentationAsset needsNotificationForState:]
+ -[HMAccessory colorCode]
+ -[HMAccessory fetchShouldSkipFirmwareUpdateApplyPolicyWithCompletionHandler:]
+ -[HMAccessory notifyDelegateUpdatedSupportsRTAPATAudioUsingContext:]
+ -[HMAccessory setColorCode:]
+ -[HMAccessory setShouldSkipFirmwareUpdateApplyPolicy:completionHandler:]
+ -[HMAccessory setSupportsRegulatoryErase:]
+ -[HMAccessory setUserConfigurationReady:]
+ -[HMAccessory supportsRegulatoryErase]
+ -[HMAccessory(Private) notifyPostPairingSetupCompleteWithCompletionHandler:]
+ -[HMAccessoryCapabilities supportsAudioDestinationMediaSystemVirtualHomePod]
+ -[HMAccessoryCapabilities supportsAudioDestinationVirtualHomeTheater]
+ -[HMAccessoryCapabilities supportsHomeTheaterNaming]
+ -[HMAccessoryCapabilities supportsRegulatoryErase]
+ -[HMAccessoryDiagnosticsMetadata captureDate]
+ -[HMAccessoryDiagnosticsMetadata initWithSnapshotPath:urlParameters:privacyPolicyURL:uploadDestination:consentVersion:uploadType:captureDate:isCachedSnapshot:]
+ -[HMAccessoryDiagnosticsMetadata isCachedSnapshot]
+ -[HMAccessoryDiagnosticsOptions captureWhenAvailable]
+ -[HMAccessoryDiagnosticsOptions setCaptureWhenAvailable:]
+ -[HMAccessoryDiagnosticsOptions setTransferDeadline:]
+ -[HMAccessoryDiagnosticsOptions transferDeadline]
+ -[HMAccessorySetupManager notifyProxControlDismissed]
+ -[HMAccessorySetupManager notifyProxControlInteraction]
+ -[HMAccessorySetupManager simulateNFCTapWithSetupURLStrings:completionHandler:]
+ -[HMCameraClipVideoHLSPlaylistGenerator _hlsPlaylistEncryptionMethodName]
+ -[HMCameraClipVideoHLSPlaylistGenerator _playlistTargetDuration]
+ -[HMCameraClipVideoHLSPlaylistGenerator encryptionScheme]
+ -[HMCameraClipVideoHLSPlaylistGenerator isClipComplete]
+ -[HMCameraClipVideoHLSPlaylistGenerator isFinished]
+ -[HMCameraClipVideoHLSPlaylistGenerator maxDataSegmentDuration]
+ -[HMCameraClipVideoHLSPlaylistGenerator segmentsString]
+ -[HMCameraClipVideoHLSPlaylistGenerator setFinished:]
+ -[HMCameraClipVideoHLSPlaylistGenerator setMaxDataSegmentDuration:]
+ -[HMCameraClipVideoHLSPlaylistGenerator targetFragmentDuration]
+ -[HMCoreAnalyticsMetricEvent hmf_appendAttributeDescriptionsToString:options:]
+ -[HMDemoModeStatus disableRealCameraContent]
+ -[HMDemoModeStatus setDisableRealCameraContent:]
+ -[HMDemoModeStatus setSuppressDPS:]
+ -[HMDemoModeStatus setThermostatPreset:]
+ -[HMDemoModeStatus suppressDPS]
+ -[HMDemoModeStatus thermostatPreset]
+ -[HMFMessage(HMXPC) hm_xpcTimeoutDate]
+ -[HMFMutableMessage(HMXPC) hm_setXPCTimeoutDate:]
+ -[HMHome _handleAccessoryUserConfigurationReadyMessage:]
+ -[HMHome(HMAccessory) _removeAccessory:regulatoryEraseRequired:completionHandler:]
+ -[HMHome(HMAccessory) removeAccessory:regulatoryEraseRequired:completionHandler:]
+ -[HMHomeManager _accessoryUUIDsForClientDelegation:]
+ -[HMHomeManager _failClientDelegationRequestWithCode:completion:]
+ -[HMHomeManager _sendClientDelegationMessageWithName:accessoryUUIDs:auditToken:completion:]
+ -[HMHomeManager delegateAccessories:toProcessWithAuditToken:completionHandler:]
+ -[HMHomeManager isDelegatedOnly]
+ -[HMHomeManager isRegulatoryEraseRequiredForLastRemovedCurrentAccessory]
+ -[HMHomeManager revokeAccessories:fromProcessWithAuditToken:completionHandler:]
+ -[HMHomeManager revokeAllAccessoriesFromProcessWithAuditToken:completionHandler:]
+ -[HMHomeManager(DemoMode) setDemoModeDisableRealCameraContent:]
+ -[HMHomeManager(DemoMode) setDemoModeSuppressDPS:]
+ -[HMHomeManager(DemoMode) setDemoModeThermostatPreset:]
+ -[HMHomeTheaterSystem initWithIdentifier:parentIdentifier:name:defaultName:audioDestinationIdentifier:audioDestinationType:]
+ -[HMMediaDestinationController groupName]
+ -[HMMediaDestinationController initWithControllerData:supportsHomeTheaterNaming:]
+ -[HMMediaDestinationController notifyDidUpdateGroupName]
+ -[HMMediaDestinationController notifyDidUpdateSupportedOptions]
+ -[HMMediaDestinationController setSupportsHomeTheaterNaming:]
+ -[HMMediaDestinationController supportsHomeTheaterNaming]
+ -[HMMediaDestinationController updateGroupName:completionHandler:]
+ -[HMMediaDestinationControllerData groupName]
+ -[HMMediaDestinationControllerData initWithIdentifier:parentIdentifier:destinationIdentifier:supportedOptions:availableDestinationIdentifiers:rawGroupName:]
+ -[HMMediaDestinationControllerData isDefaultName]
+ -[HMMediaDestinationControllerData rawGroupName]
+ -[HMMediaDestinationControllerData setRawGroupName:]
+ -[HMMediaGroupProtoMediaDestinationControllerData groupName]
+ -[HMMediaGroupProtoMediaDestinationControllerData hasGroupName]
+ -[HMMediaGroupProtoMediaDestinationControllerData setGroupName:]
+ -[HMMediaGroupStagingManager cancelTimer:]
+ -[HMMediaGroupStagingManager clientHasMediaGroupsEnabled]
+ -[HMMediaGroupStagingManager configureWithMessageDispatcher:clientHasMediaGroupsEnabled:]
+ -[HMMediaGroupStagingManager metricContext]
+ -[HMMediaGroupStagingManager notifyDestinationControllersWithDestinationControllerData:]
+ -[HMMediaGroupStagingManager resetMetricCountsIfNeeded]
+ -[HMMediaGroupStagingManager setClientHasMediaGroupsEnabled:]
+ -[HMMediaGroupStagingManager stageGroups:destinations:destinationControllersData:removedGroupIdentifiers:]
+ -[HMMediaGroupStagingManager stagedDestinationControllerData]
+ -[HMMediaGroupStagingManager startMetricWithMetricType:]
+ -[HMMediaGroupStagingManager stopMetricWithResult:]
+ -[HMProtoAccessoryCapabilities hasSupportsAudioDestinationMediaSystemVirtualHomePod]
+ -[HMProtoAccessoryCapabilities hasSupportsAudioDestinationVirtualHomeTheater]
+ -[HMProtoAccessoryCapabilities hasSupportsHomeTheaterNaming]
+ -[HMProtoAccessoryCapabilities setHasSupportsAudioDestinationMediaSystemVirtualHomePod:]
+ -[HMProtoAccessoryCapabilities setHasSupportsAudioDestinationVirtualHomeTheater:]
+ -[HMProtoAccessoryCapabilities setHasSupportsHomeTheaterNaming:]
+ -[HMProtoAccessoryCapabilities setSupportsAudioDestinationMediaSystemVirtualHomePod:]
+ -[HMProtoAccessoryCapabilities setSupportsAudioDestinationVirtualHomeTheater:]
+ -[HMProtoAccessoryCapabilities setSupportsHomeTheaterNaming:]
+ -[HMProtoAccessoryCapabilities supportsAudioDestinationMediaSystemVirtualHomePod]
+ -[HMProtoAccessoryCapabilities supportsAudioDestinationVirtualHomeTheater]
+ -[HMProtoAccessoryCapabilities supportsHomeTheaterNaming]
+ -[HMProtoResidentCapabilities hasSupports3826361c217c]
+ -[HMProtoResidentCapabilities hasSupportsECDSAKey]
+ -[HMProtoResidentCapabilities setHasSupports3826361c217c:]
+ -[HMProtoResidentCapabilities setHasSupportsECDSAKey:]
+ -[HMProtoResidentCapabilities setSupports3826361c217c:]
+ -[HMProtoResidentCapabilities setSupportsECDSAKey:]
+ -[HMProtoResidentCapabilities supports3826361c217c]
+ -[HMProtoResidentCapabilities supportsECDSAKey]
+ -[HMResidentCapabilities supportsECDSAKey]
+ -[HMRoom description]
+ -[HMRoom hmf_appendAttributeDescriptionsToString:options:]
+ -[HMRoom privateDescription]
+ -[HMRoom shortDescription]
+ -[HMSetupAccessoryDescription proxPairingCardLaunchSessionID]
+ -[HMSetupAccessoryDescription proxPairingMetricsSessionID]
+ -[HMSetupAccessoryDescription setProxPairingCardLaunchSessionID:]
+ -[HMSetupAccessoryDescription setProxPairingMetricsSessionID:]
+ -[HMSetupAccessoryPayload colorCode]
+ -[HMSetupAccessoryPayload setColorCode:]
+ -[HMSoftwareUpdateDocumentationAsset documentationForState:]
+ -[HMSoftwareUpdateDocumentationAsset invalidateCache]
+ -[HMSoftwareUpdateDocumentationAsset queue]
+ -[HMSoftwareUpdateDocumentationManager completeCompletions:documentation:]
+ -[HMSoftwareUpdateDocumentationManager documentationAsset:didTransitionToState:documentation:error:]
+ -[HMSoftwareUpdateDocumentationManager drainCompletionsForAsset:]
+ -[HMSoftwareUpdateDocumentationManager failCompletions:error:]
+ -[HMSoftwareUpdateDocumentationManager failCompletionsForAsset:error:]
+ -[HMXPCClientDataSource homeDataAuthorizationStatus]
+ -[HMXPCMessageTransportConfiguration alternativeEntitlements]
+ -[HMXPCMessageTransportConfiguration setAlternativeEntitlements:]
+ -[NSError(HMError) isNotSignedIntoiCloudError]
+ GCC_except_table10018
+ GCC_except_table10020
+ GCC_except_table10022
+ GCC_except_table10087
+ GCC_except_table10119
+ GCC_except_table10121
+ GCC_except_table10125
+ GCC_except_table10142
+ GCC_except_table10144
+ GCC_except_table10150
+ GCC_except_table10154
+ GCC_except_table10157
+ GCC_except_table10164
+ GCC_except_table10174
+ GCC_except_table10186
+ GCC_except_table10189
+ GCC_except_table10197
+ GCC_except_table10198
+ GCC_except_table10200
+ GCC_except_table10202
+ GCC_except_table10204
+ GCC_except_table10224
+ GCC_except_table10234
+ GCC_except_table10434
+ GCC_except_table10447
+ GCC_except_table10488
+ GCC_except_table10491
+ GCC_except_table10493
+ GCC_except_table10506
+ GCC_except_table10507
+ GCC_except_table10575
+ GCC_except_table10578
+ GCC_except_table10579
+ GCC_except_table10926
+ GCC_except_table10964
+ GCC_except_table10977
+ GCC_except_table11339
+ GCC_except_table11340
+ GCC_except_table11342
+ GCC_except_table11343
+ GCC_except_table11353
+ GCC_except_table11377
+ GCC_except_table11378
+ GCC_except_table11381
+ GCC_except_table11384
+ GCC_except_table11393
+ GCC_except_table11394
+ GCC_except_table11395
+ GCC_except_table11492
+ GCC_except_table11650
+ GCC_except_table11657
+ GCC_except_table11662
+ GCC_except_table1167
+ GCC_except_table1171
+ GCC_except_table1178
+ GCC_except_table11856
+ GCC_except_table11904
+ GCC_except_table12104
+ GCC_except_table12106
+ GCC_except_table12113
+ GCC_except_table12121
+ GCC_except_table12142
+ GCC_except_table12153
+ GCC_except_table12158
+ GCC_except_table12175
+ GCC_except_table12180
+ GCC_except_table12186
+ GCC_except_table12191
+ GCC_except_table12196
+ GCC_except_table12201
+ GCC_except_table12206
+ GCC_except_table12210
+ GCC_except_table12215
+ GCC_except_table12262
+ GCC_except_table12266
+ GCC_except_table12281
+ GCC_except_table12295
+ GCC_except_table12300
+ GCC_except_table12307
+ GCC_except_table12324
+ GCC_except_table12325
+ GCC_except_table12327
+ GCC_except_table12329
+ GCC_except_table12332
+ GCC_except_table12337
+ GCC_except_table12344
+ GCC_except_table12349
+ GCC_except_table12353
+ GCC_except_table12391
+ GCC_except_table12437
+ GCC_except_table12446
+ GCC_except_table12453
+ GCC_except_table12455
+ GCC_except_table12459
+ GCC_except_table12460
+ GCC_except_table12534
+ GCC_except_table12547
+ GCC_except_table1255
+ GCC_except_table12577
+ GCC_except_table12626
+ GCC_except_table12627
+ GCC_except_table12628
+ GCC_except_table12629
+ GCC_except_table12630
+ GCC_except_table12631
+ GCC_except_table12632
+ GCC_except_table12633
+ GCC_except_table12634
+ GCC_except_table12635
+ GCC_except_table12636
+ GCC_except_table12637
+ GCC_except_table12638
+ GCC_except_table12639
+ GCC_except_table1264
+ GCC_except_table12640
+ GCC_except_table12641
+ GCC_except_table12664
+ GCC_except_table12691
+ GCC_except_table12801
+ GCC_except_table12802
+ GCC_except_table12805
+ GCC_except_table12871
+ GCC_except_table12873
+ GCC_except_table12881
+ GCC_except_table12892
+ GCC_except_table12894
+ GCC_except_table12899
+ GCC_except_table12900
+ GCC_except_table12901
+ GCC_except_table13125
+ GCC_except_table13326
+ GCC_except_table13329
+ GCC_except_table13334
+ GCC_except_table13338
+ GCC_except_table1334
+ GCC_except_table13351
+ GCC_except_table13353
+ GCC_except_table13358
+ GCC_except_table13359
+ GCC_except_table13361
+ GCC_except_table1339
+ GCC_except_table1341
+ GCC_except_table1343
+ GCC_except_table13443
+ GCC_except_table13445
+ GCC_except_table13464
+ GCC_except_table13467
+ GCC_except_table1347
+ GCC_except_table13472
+ GCC_except_table13486
+ GCC_except_table13492
+ GCC_except_table13495
+ GCC_except_table13499
+ GCC_except_table13577
+ GCC_except_table13585
+ GCC_except_table13586
+ GCC_except_table13591
+ GCC_except_table13597
+ GCC_except_table13599
+ GCC_except_table13601
+ GCC_except_table13603
+ GCC_except_table13605
+ GCC_except_table13607
+ GCC_except_table13609
+ GCC_except_table13742
+ GCC_except_table13798
+ GCC_except_table13799
+ GCC_except_table13800
+ GCC_except_table13801
+ GCC_except_table13811
+ GCC_except_table13812
+ GCC_except_table13836
+ GCC_except_table13837
+ GCC_except_table13911
+ GCC_except_table13933
+ GCC_except_table13936
+ GCC_except_table14082
+ GCC_except_table14258
+ GCC_except_table14317
+ GCC_except_table14352
+ GCC_except_table14358
+ GCC_except_table14362
+ GCC_except_table14363
+ GCC_except_table14368
+ GCC_except_table14370
+ GCC_except_table14371
+ GCC_except_table14372
+ GCC_except_table14373
+ GCC_except_table14374
+ GCC_except_table14375
+ GCC_except_table14376
+ GCC_except_table14383
+ GCC_except_table14522
+ GCC_except_table14525
+ GCC_except_table14545
+ GCC_except_table14547
+ GCC_except_table14548
+ GCC_except_table1513
+ GCC_except_table1539
+ GCC_except_table1605
+ GCC_except_table1676
+ GCC_except_table1681
+ GCC_except_table1699
+ GCC_except_table1767
+ GCC_except_table1769
+ GCC_except_table1780
+ GCC_except_table1782
+ GCC_except_table1920
+ GCC_except_table1974
+ GCC_except_table1977
+ GCC_except_table2051
+ GCC_except_table2138
+ GCC_except_table2139
+ GCC_except_table2192
+ GCC_except_table2471
+ GCC_except_table2474
+ GCC_except_table2479
+ GCC_except_table2505
+ GCC_except_table2507
+ GCC_except_table2508
+ GCC_except_table2513
+ GCC_except_table2514
+ GCC_except_table2515
+ GCC_except_table2516
+ GCC_except_table2532
+ GCC_except_table2542
+ GCC_except_table2638
+ GCC_except_table2977
+ GCC_except_table2979
+ GCC_except_table3280
+ GCC_except_table3285
+ GCC_except_table3311
+ GCC_except_table3314
+ GCC_except_table3327
+ GCC_except_table3359
+ GCC_except_table3362
+ GCC_except_table3388
+ GCC_except_table3390
+ GCC_except_table3392
+ GCC_except_table3394
+ GCC_except_table3541
+ GCC_except_table3544
+ GCC_except_table3552
+ GCC_except_table3553
+ GCC_except_table3574
+ GCC_except_table3601
+ GCC_except_table3660
+ GCC_except_table3662
+ GCC_except_table3665
+ GCC_except_table3666
+ GCC_except_table3692
+ GCC_except_table3694
+ GCC_except_table3702
+ GCC_except_table3704
+ GCC_except_table3711
+ GCC_except_table3712
+ GCC_except_table3713
+ GCC_except_table3715
+ GCC_except_table3716
+ GCC_except_table3717
+ GCC_except_table3718
+ GCC_except_table3719
+ GCC_except_table3802
+ GCC_except_table3825
+ GCC_except_table3828
+ GCC_except_table3831
+ GCC_except_table3834
+ GCC_except_table3840
+ GCC_except_table3843
+ GCC_except_table3908
+ GCC_except_table3909
+ GCC_except_table3955
+ GCC_except_table3962
+ GCC_except_table3963
+ GCC_except_table3964
+ GCC_except_table3967
+ GCC_except_table3968
+ GCC_except_table3969
+ GCC_except_table3971
+ GCC_except_table3979
+ GCC_except_table4001
+ GCC_except_table4010
+ GCC_except_table4014
+ GCC_except_table4017
+ GCC_except_table4020
+ GCC_except_table4061
+ GCC_except_table4065
+ GCC_except_table4069
+ GCC_except_table4074
+ GCC_except_table4082
+ GCC_except_table4086
+ GCC_except_table4095
+ GCC_except_table4097
+ GCC_except_table4341
+ GCC_except_table4346
+ GCC_except_table4350
+ GCC_except_table4353
+ GCC_except_table4357
+ GCC_except_table4358
+ GCC_except_table4363
+ GCC_except_table4369
+ GCC_except_table4373
+ GCC_except_table4377
+ GCC_except_table4400
+ GCC_except_table4402
+ GCC_except_table4404
+ GCC_except_table4407
+ GCC_except_table4408
+ GCC_except_table4410
+ GCC_except_table4413
+ GCC_except_table4488
+ GCC_except_table4502
+ GCC_except_table4505
+ GCC_except_table4507
+ GCC_except_table4510
+ GCC_except_table4517
+ GCC_except_table4572
+ GCC_except_table4637
+ GCC_except_table4652
+ GCC_except_table4655
+ GCC_except_table4747
+ GCC_except_table4748
+ GCC_except_table4752
+ GCC_except_table4757
+ GCC_except_table4761
+ GCC_except_table4764
+ GCC_except_table4766
+ GCC_except_table4774
+ GCC_except_table5025
+ GCC_except_table5028
+ GCC_except_table5040
+ GCC_except_table5116
+ GCC_except_table5162
+ GCC_except_table5255
+ GCC_except_table5450
+ GCC_except_table5464
+ GCC_except_table5489
+ GCC_except_table5490
+ GCC_except_table5491
+ GCC_except_table5492
+ GCC_except_table5547
+ GCC_except_table5562
+ GCC_except_table5828
+ GCC_except_table5830
+ GCC_except_table5845
+ GCC_except_table5883
+ GCC_except_table5885
+ GCC_except_table5903
+ GCC_except_table5949
+ GCC_except_table6044
+ GCC_except_table6064
+ GCC_except_table6065
+ GCC_except_table6066
+ GCC_except_table6068
+ GCC_except_table6071
+ GCC_except_table6072
+ GCC_except_table6074
+ GCC_except_table6408
+ GCC_except_table6414
+ GCC_except_table6416
+ GCC_except_table6426
+ GCC_except_table6427
+ GCC_except_table6632
+ GCC_except_table6636
+ GCC_except_table6734
+ GCC_except_table6741
+ GCC_except_table6889
+ GCC_except_table7006
+ GCC_except_table7061
+ GCC_except_table7063
+ GCC_except_table7065
+ GCC_except_table7087
+ GCC_except_table7117
+ GCC_except_table7129
+ GCC_except_table7154
+ GCC_except_table7160
+ GCC_except_table7171
+ GCC_except_table7173
+ GCC_except_table7175
+ GCC_except_table7177
+ GCC_except_table7179
+ GCC_except_table7181
+ GCC_except_table7183
+ GCC_except_table7185
+ GCC_except_table7187
+ GCC_except_table7189
+ GCC_except_table7191
+ GCC_except_table7193
+ GCC_except_table7195
+ GCC_except_table7200
+ GCC_except_table7214
+ GCC_except_table7215
+ GCC_except_table7240
+ GCC_except_table7242
+ GCC_except_table7267
+ GCC_except_table7280
+ GCC_except_table7298
+ GCC_except_table7477
+ GCC_except_table7828
+ GCC_except_table7871
+ GCC_except_table7964
+ GCC_except_table7973
+ GCC_except_table8131
+ GCC_except_table8134
+ GCC_except_table8226
+ GCC_except_table8245
+ GCC_except_table8255
+ GCC_except_table8397
+ GCC_except_table8406
+ GCC_except_table8419
+ GCC_except_table8426
+ GCC_except_table8465
+ GCC_except_table8467
+ GCC_except_table8502
+ GCC_except_table8504
+ GCC_except_table8506
+ GCC_except_table8508
+ GCC_except_table8515
+ GCC_except_table8523
+ GCC_except_table8529
+ GCC_except_table8539
+ GCC_except_table8545
+ GCC_except_table8624
+ GCC_except_table8633
+ GCC_except_table8635
+ GCC_except_table8645
+ GCC_except_table8647
+ GCC_except_table8649
+ GCC_except_table8651
+ GCC_except_table8653
+ GCC_except_table8659
+ GCC_except_table8663
+ GCC_except_table8676
+ GCC_except_table8680
+ GCC_except_table8682
+ GCC_except_table8869
+ GCC_except_table8871
+ GCC_except_table8872
+ GCC_except_table8873
+ GCC_except_table8875
+ GCC_except_table8877
+ GCC_except_table8878
+ GCC_except_table8879
+ GCC_except_table8914
+ GCC_except_table8917
+ GCC_except_table8918
+ GCC_except_table8921
+ GCC_except_table8924
+ GCC_except_table8925
+ GCC_except_table8968
+ GCC_except_table8969
+ GCC_except_table8970
+ GCC_except_table8977
+ GCC_except_table8978
+ GCC_except_table8980
+ GCC_except_table8999
+ GCC_except_table9068
+ GCC_except_table9069
+ GCC_except_table9070
+ GCC_except_table9109
+ GCC_except_table9123
+ GCC_except_table9191
+ GCC_except_table9219
+ GCC_except_table9220
+ GCC_except_table9221
+ GCC_except_table9223
+ GCC_except_table9226
+ GCC_except_table9227
+ GCC_except_table9233
+ GCC_except_table9382
+ GCC_except_table9383
+ GCC_except_table9384
+ GCC_except_table9388
+ GCC_except_table9443
+ GCC_except_table9466
+ GCC_except_table950
+ GCC_except_table952
+ GCC_except_table9546
+ GCC_except_table9548
+ GCC_except_table9550
+ GCC_except_table9552
+ GCC_except_table9560
+ GCC_except_table958
+ GCC_except_table9610
+ GCC_except_table9622
+ GCC_except_table9624
+ GCC_except_table966
+ GCC_except_table9814
+ GCC_except_table9815
+ GCC_except_table9850
+ GCC_except_table9883
+ GCC_except_table9886
+ GCC_except_table9889
+ GCC_except_table9891
+ GCC_except_table9957
+ GCC_except_table9977
+ GCC_except_table9978
+ GCC_except_table9979
+ OBJC_IVAR_$_HMAccessory._colorCode
+ OBJC_IVAR_$_HMAccessory._supportsRegulatoryErase
+ OBJC_IVAR_$_HMAccessory._userConfigurationReady
+ OBJC_IVAR_$_HMAccessoryDiagnosticsMetadata._captureDate
+ OBJC_IVAR_$_HMAccessoryDiagnosticsMetadata._isCachedSnapshot
+ OBJC_IVAR_$_HMAccessoryDiagnosticsOptions._captureWhenAvailable
+ OBJC_IVAR_$_HMAccessoryDiagnosticsOptions._transferDeadline
+ OBJC_IVAR_$_HMCameraClipVideoHLSPlaylistGenerator._clipComplete
+ OBJC_IVAR_$_HMCameraClipVideoHLSPlaylistGenerator._encryptionScheme
+ OBJC_IVAR_$_HMCameraClipVideoHLSPlaylistGenerator._finished
+ OBJC_IVAR_$_HMCameraClipVideoHLSPlaylistGenerator._maxDataSegmentDuration
+ OBJC_IVAR_$_HMCameraClipVideoHLSPlaylistGenerator._segmentsString
+ OBJC_IVAR_$_HMCameraClipVideoHLSPlaylistGenerator._targetFragmentDuration
+ OBJC_IVAR_$_HMDemoModeStatus._disableRealCameraContent
+ OBJC_IVAR_$_HMDemoModeStatus._suppressDPS
+ OBJC_IVAR_$_HMDemoModeStatus._thermostatPreset
+ OBJC_IVAR_$_HMHomeManager._isRegulatoryEraseRequiredForLastRemovedCurrentAccessory
+ OBJC_IVAR_$_HMMediaDestinationController._supportsHomeTheaterNaming
+ OBJC_IVAR_$_HMMediaDestinationControllerData._rawGroupName
+ OBJC_IVAR_$_HMMediaGroupProtoMediaDestinationControllerData._groupName
+ OBJC_IVAR_$_HMMediaGroupStagingManager._clientHasMediaGroupsEnabled
+ OBJC_IVAR_$_HMMediaGroupStagingManager._metricContext
+ OBJC_IVAR_$_HMProtoAccessoryCapabilities._supportsAudioDestinationMediaSystemVirtualHomePod
+ OBJC_IVAR_$_HMProtoAccessoryCapabilities._supportsAudioDestinationVirtualHomeTheater
+ OBJC_IVAR_$_HMProtoAccessoryCapabilities._supportsHomeTheaterNaming
+ OBJC_IVAR_$_HMProtoResidentCapabilities._supports3826361c217c
+ OBJC_IVAR_$_HMProtoResidentCapabilities._supportsECDSAKey
+ OBJC_IVAR_$_HMSetupAccessoryDescription._proxPairingCardLaunchSessionID
+ OBJC_IVAR_$_HMSetupAccessoryDescription._proxPairingMetricsSessionID
+ OBJC_IVAR_$_HMSetupAccessoryPayload._colorCode
+ OBJC_IVAR_$_HMXPCMessageTransportConfiguration._alternativeEntitlements
+ _HMAccessoryColorCodeCodingKey
+ _HMAccessoryFetchShouldSkipFirmwareUpdateApplyPolicyMessage
+ _HMAccessoryPostPairingSetupCompleteMessage
+ _HMAccessoryRegulatoryEraseRequiredKey
+ _HMAccessorySetShouldSkipFirmwareUpdateApplyPolicyMessage
+ _HMAccessorySetupManagerMessageKeyNFCSetupURLStrings
+ _HMAccessorySetupManagerMessageKeyProxControlErrorCode
+ _HMAccessorySetupManagerMessageKeyProxControlErrorDetails
+ _HMAccessorySetupManagerProxAssetPrimaryVideoKey
+ _HMAccessorySetupManagerProxControlDismissedMessage
+ _HMAccessorySetupManagerProxControlErrorDetailsRequestedMessage
+ _HMAccessorySetupManagerProxControlInteractionMessage
+ _HMAccessoryShouldSkipFirmwareUpdateApplyPolicyMessageKey
+ _HMAccessorySupportsHomeTheaterNamingCodingKey
+ _HMAccessorySupportsRegulatoryEraseCodingKey
+ _HMAccessoryUserConfigurationReadyCodingKey
+ _HMCharacteristicTypeAVCStreamingControl
+ _HMCharacteristicTypeDewarp
+ _HMDemoModeDisableRealCameraContentKey
+ _HMDemoModeSuppressDPSKey
+ _HMDemoModeThermostatPresetKey
+ _HMErrorRetryableAfterReconnectUserInfoKey
+ _HMFUptime
+ _HMHomeAccessoryUserConfigurationReadyMessage
+ _HMHomeCaptionPlanCountCodingKey
+ _HMHomeCaptionPlanTierCodingKey
+ _HMHomeDidUpdateCaptionPlanMessage
+ _HMHomeFetchCaptionPlanMessage
+ _HMHomeManagerClientDelegationAccessoryUUIDsKey
+ _HMHomeManagerClientDelegationAuditTokenKey
+ _HMHomeManagerDelegateAccessoriesMessage
+ _HMHomeManagerLastRemovedCurrentAccessoryRegulatoryEraseRequiredCodingKey
+ _HMHomeManagerRevokeAccessoriesMessage
+ _HMHomeManagerRevokeAllAccessoriesMessage
+ _HMMediaDestinationControllerGroupNamePayloadKey
+ _HMMediaDestinationControllerUpdateGroupNameRequestMessage
+ _HMServiceTypeCameraSensorOperatingMode
+ __106-[HMMediaGroupStagingManager stageGroups:destinations:destinationControllersData:removedGroupIdentifiers:]_block_invoke
+ __34-[HMAccessory mergeFromNewObject:]_block_invoke_7
+ __34-[HMAccessory mergeFromNewObject:]_block_invoke_8
+ __77-[HMAccessory fetchShouldSkipFirmwareUpdateApplyPolicyWithCompletionHandler:]_block_invoke
+ __77-[HMAccessory fetchShouldSkipFirmwareUpdateApplyPolicyWithCompletionHandler:]_block_invoke_2
+ __OBJC_$_CLASS_METHODS_HMAccessory(HomeKit|DynamicAccessorySettingsAdapter|SwiftExtensions|SiriEndpoint|Television|LightInternal|HMDoorbellChimeProfile|NetworkRouter|PendingConfiguration|Private|CUPeerIdentifier|Diagnostics|Shortcuts|Camera|CameraInternal|CHIP|NetworkConfiguration|Climate|Light|Media)
+ __OBJC_$_CLASS_METHODS_HMCoreAnalyticsMetricEventDispatcher
+ __OBJC_$_CLASS_METHODS_HMHome(HomeKit|CaptionPlanSwift|HomeKit1|HomeKit2|HomeKit3|SwiftExtensions|AccessCode|WalletInternal|Wallet|Light|MediaGroupSettingsControllerFactory|ThreadResidentCommissioning|SiriEndpointProfilesMessengerFactory|HMActionExecution|Person|Person_Internal|Matter|CHIP|HMAccessory|HMRoom|HMZone|HMServiceGroup|HMUser|HMActionSet|HMTrigger|RemoteAccess|HMSoftwareUpdate|HMMediaProfile|NetworkRouter|HMUserActionPredictions|ThreadManagement|HMHomeHub|PowerAssertionInfo|HomeNetworkInfo|HomeLocationFeedback|MediaGroupReadinessCheck|HomeActivityState|ResidentSelection|HMModernMessaging|HMModernMessagingInternal|Trigger|Biome|Climate|AutomationBuilders)
+ __OBJC_$_INSTANCE_METHODS_HMAccessory(HomeKit|DynamicAccessorySettingsAdapter|SwiftExtensions|SiriEndpoint|Television|LightInternal|HMDoorbellChimeProfile|NetworkRouter|PendingConfiguration|Private|CUPeerIdentifier|Diagnostics|Shortcuts|Camera|CameraInternal|CHIP|NetworkConfiguration|Climate|Light|Media)
+ __OBJC_$_INSTANCE_METHODS_HMEventTrigger(SwiftExtensions|HMEventTriggerBuilder)
+ __OBJC_$_INSTANCE_METHODS_HMHome(HomeKit|CaptionPlanSwift|HomeKit1|HomeKit2|HomeKit3|SwiftExtensions|AccessCode|WalletInternal|Wallet|Light|MediaGroupSettingsControllerFactory|ThreadResidentCommissioning|SiriEndpointProfilesMessengerFactory|HMActionExecution|Person|Person_Internal|Matter|CHIP|HMAccessory|HMRoom|HMZone|HMServiceGroup|HMUser|HMActionSet|HMTrigger|RemoteAccess|HMSoftwareUpdate|HMMediaProfile|NetworkRouter|HMUserActionPredictions|ThreadManagement|HMHomeHub|PowerAssertionInfo|HomeNetworkInfo|HomeLocationFeedback|MediaGroupReadinessCheck|HomeActivityState|ResidentSelection|HMModernMessaging|HMModernMessagingInternal|Trigger|Biome|Climate|AutomationBuilders)
+ __OBJC_$_PROP_LIST_HMCoreAnalyticsMetricEventDispatcher
+ __OBJC_CLASS_PROTOCOLS_$_HMCoreAnalyticsMetricEventDispatcher
+ __OBJC_CLASS_PROTOCOLS_$_HMHome(HomeKit|CaptionPlanSwift|HomeKit1|HomeKit2|HomeKit3|SwiftExtensions|AccessCode|WalletInternal|Wallet|Light|MediaGroupSettingsControllerFactory|ThreadResidentCommissioning|SiriEndpointProfilesMessengerFactory|HMActionExecution|Person|Person_Internal|Matter|CHIP|HMAccessory|HMRoom|HMZone|HMServiceGroup|HMUser|HMActionSet|HMTrigger|RemoteAccess|HMSoftwareUpdate|HMMediaProfile|NetworkRouter|HMUserActionPredictions|ThreadManagement|HMHomeHub|PowerAssertionInfo|HomeNetworkInfo|HomeLocationFeedback|MediaGroupReadinessCheck|HomeActivityState|ResidentSelection|HMModernMessaging|HMModernMessagingInternal|Trigger|Biome|Climate|AutomationBuilders)
+ ___106-[HMMediaGroupStagingManager stageGroups:destinations:destinationControllersData:removedGroupIdentifiers:]_block_invoke
+ ___51+[HMCoreAnalyticsMetricEventDispatcher logCategory]_block_invoke
+ ___51-[HMMediaDestinationController mergeFromNewObject:]_block_invoke_3
+ ___51-[HMMediaDestinationController mergeFromNewObject:]_block_invoke_4
+ ___53-[HMSoftwareUpdateDocumentationAsset invalidateCache]_block_invoke
+ ___56-[HMMediaDestinationController notifyDidUpdateGroupName]_block_invoke
+ ___62-[HMSoftwareUpdateDocumentationManager failCompletions:error:]_block_invoke
+ ___63-[HMMediaDestinationController notifyDidUpdateSupportedOptions]_block_invoke
+ ___63-[HMSoftwareUpdateDocumentationAsset cancelUnarchiveWithError:]_block_invoke
+ ___66-[HMMediaDestinationController updateGroupName:completionHandler:]_block_invoke
+ ___68-[HMAccessory notifyDelegateUpdatedSupportsRTAPATAudioUsingContext:]_block_invoke
+ ___68-[HMAccessory notifyDelegateUpdatedSupportsRTAPATAudioUsingContext:]_block_invoke_2
+ ___68-[HMSoftwareUpdateDocumentationManager removeDocumentationMetadata:]_block_invoke
+ ___72-[HMAccessory setShouldSkipFirmwareUpdateApplyPolicy:completionHandler:]_block_invoke
+ ___74-[HMSoftwareUpdateDocumentationManager completeCompletions:documentation:]_block_invoke
+ ___76-[HMAccessory(Private) notifyPostPairingSetupCompleteWithCompletionHandler:]_block_invoke
+ ___77-[HMAccessory fetchShouldSkipFirmwareUpdateApplyPolicyWithCompletionHandler:]_block_invoke
+ ___77-[HMAccessory fetchShouldSkipFirmwareUpdateApplyPolicyWithCompletionHandler:]_block_invoke_2
+ ___79-[HMAccessorySetupManager simulateNFCTapWithSetupURLStrings:completionHandler:]_block_invoke
+ ___81-[HMHome(HMAccessory) removeAccessory:regulatoryEraseRequired:completionHandler:]_block_invoke
+ ___82-[HMHome(HMAccessory) _removeAccessory:regulatoryEraseRequired:completionHandler:]_block_invoke
+ ___88-[HMMediaGroupStagingManager notifyDestinationControllersWithDestinationControllerData:]_block_invoke
+ ___88-[HMMediaGroupStagingManager notifyDestinationControllersWithDestinationControllerData:]_block_invoke_2
+ ___block_descriptor_32_e50_"NSUUID"16?0"HMMediaDestinationControllerData"8l
+ ___swift_memcpy176_8
+ ___swift_memcpy224_8
+ __swift_FORCE_LOAD_$_swiftIntents
+ __swift_FORCE_LOAD_$_swiftIntents_$_HomeKit
+ _associated conformance 7HomeKit30AccessoryHealthSnapshotMessageOAA19HMFMessagePrototypeO07RequestF0AA0I7PayloadAeFP_AE0J0
+ _associated conformance 7HomeKit30AccessoryHealthSnapshotMessageOAA19HMFMessagePrototypeO07RequestF0AA15ResponsePayloadAeFP_AE0K0
+ _associated conformance So18HMClientConnectionC7HomeKitE07HydrateC15EntitiesRequestV0G7PayloadV10CodingKeys33_CDC1F0A71EBD15EE416B075C79B451BCLLOSHACSQ
+ _associated conformance So18HMClientConnectionC7HomeKitE07HydrateC15EntitiesRequestV0G7PayloadV10CodingKeys33_CDC1F0A71EBD15EE416B075C79B451BCLLOs0I3KeyACs23CustomStringConvertible
+ _associated conformance So18HMClientConnectionC7HomeKitE07HydrateC15EntitiesRequestV0G7PayloadV10CodingKeys33_CDC1F0A71EBD15EE416B075C79B451BCLLOs0I3KeyACs28CustomDebugStringConvertible
+ _associated conformance So18HMClientConnectionC7HomeKitE07HydrateC15EntitiesRequestV15ResponsePayloadV10CodingKeys33_CDC1F0A71EBD15EE416B075C79B451BCLLOSHACSQ
+ _associated conformance So18HMClientConnectionC7HomeKitE07HydrateC15EntitiesRequestV15ResponsePayloadV10CodingKeys33_CDC1F0A71EBD15EE416B075C79B451BCLLOs0J3KeyACs23CustomStringConvertible
+ _associated conformance So18HMClientConnectionC7HomeKitE07HydrateC15EntitiesRequestV15ResponsePayloadV10CodingKeys33_CDC1F0A71EBD15EE416B075C79B451BCLLOs0J3KeyACs28CustomDebugStringConvertible
+ _associated conformance So18HMClientConnectionC7HomeKitE07HydrateC15EntitiesRequestVAC19HMFMessagePrototypeO0G7MessageAC0G7PayloadAgHP_AG0K0
+ _associated conformance So18HMClientConnectionC7HomeKitE07HydrateC15EntitiesRequestVAC19HMFMessagePrototypeO0G7MessageAC15ResponsePayloadAgHP_AG0L0
+ _associated conformance So18HMClientConnectionC7HomeKitE08HydratedC6EntityV0F9ReferenceV10CodingKeys33_F18E7B87BB31449A79B57FA3A7933904LLOSHACSQ
+ _associated conformance So18HMClientConnectionC7HomeKitE08HydratedC6EntityV0F9ReferenceV10CodingKeys33_F18E7B87BB31449A79B57FA3A7933904LLOs0H3KeyACs23CustomStringConvertible
+ _associated conformance So18HMClientConnectionC7HomeKitE08HydratedC6EntityV0F9ReferenceV10CodingKeys33_F18E7B87BB31449A79B57FA3A7933904LLOs0H3KeyACs28CustomDebugStringConvertible
+ _associated conformance So18HMClientConnectionC7HomeKitE08HydratedC6EntityV10CodingKeys33_F18E7B87BB31449A79B57FA3A7933904LLOSHACSQ
+ _associated conformance So18HMClientConnectionC7HomeKitE08HydratedC6EntityV10CodingKeys33_F18E7B87BB31449A79B57FA3A7933904LLOs0G3KeyACs23CustomStringConvertible
+ _associated conformance So18HMClientConnectionC7HomeKitE08HydratedC6EntityV10CodingKeys33_F18E7B87BB31449A79B57FA3A7933904LLOs0G3KeyACs28CustomDebugStringConvertible
+ _associated conformance So18HMClientConnectionC7HomeKitE20HydrationRequestItemV10CodingKeys33_CDC1F0A71EBD15EE416B075C79B451BCLLOSHACSQ
+ _associated conformance So18HMClientConnectionC7HomeKitE20HydrationRequestItemV10CodingKeys33_CDC1F0A71EBD15EE416B075C79B451BCLLOs0H3KeyACs23CustomStringConvertible
+ _associated conformance So18HMClientConnectionC7HomeKitE20HydrationRequestItemV10CodingKeys33_CDC1F0A71EBD15EE416B075C79B451BCLLOs0H3KeyACs28CustomDebugStringConvertible
+ _kAccessoryReprovisionStateKey
+ _objc_msgSend$_accessoryUUIDsForClientDelegation:
+ _objc_msgSend$_failClientDelegationRequestWithCode:completion:
+ _objc_msgSend$_hlsPlaylistEncryptionMethodName
+ _objc_msgSend$_playlistTargetDuration
+ _objc_msgSend$_removeAccessory:regulatoryEraseRequired:completionHandler:
+ _objc_msgSend$_sendClientDelegationMessageWithName:accessoryUUIDs:auditToken:completion:
+ _objc_msgSend$accessory:didUpdateMatterNodeID:
+ _objc_msgSend$accessoryDidUpdateSupportsRTAPATAudio:
+ _objc_msgSend$accessoryDidUpdateSupportsRegulatoryErase:
+ _objc_msgSend$alternativeEntitlements
+ _objc_msgSend$cancelTimer:
+ _objc_msgSend$clientHasMediaGroupsEnabled
+ _objc_msgSend$colorCode
+ _objc_msgSend$completeCompletions:documentation:
+ _objc_msgSend$configureCaptionPlanObservation
+ _objc_msgSend$configureWithMessageDispatcher:clientHasMediaGroupsEnabled:
+ _objc_msgSend$defaultGroupName
+ _objc_msgSend$didUpdateSupportedOptionsForMediaDestinationController:
+ _objc_msgSend$documentationAsset:didTransitionToState:documentation:error:
+ _objc_msgSend$documentationForState:
+ _objc_msgSend$drainCompletionsForAsset:
+ _objc_msgSend$encryptionScheme
+ _objc_msgSend$failCompletions:error:
+ _objc_msgSend$failCompletionsForAsset:error:
+ _objc_msgSend$hasGroupName
+ _objc_msgSend$hm_setXPCTimeoutDate:
+ _objc_msgSend$homeManager:didRemoveCurrentAccessoryWithRegulatoryEraseRequired:
+ _objc_msgSend$initWithControllerData:supportsHomeTheaterNaming:
+ _objc_msgSend$initWithIdentifier:parentIdentifier:destinationIdentifier:supportedOptions:availableDestinationIdentifiers:rawGroupName:
+ _objc_msgSend$initWithIdentifier:parentIdentifier:name:defaultName:audioDestinationIdentifier:audioDestinationType:
+ _objc_msgSend$initWithSnapshotPath:urlParameters:privacyPolicyURL:uploadDestination:consentVersion:uploadType:captureDate:isCachedSnapshot:
+ _objc_msgSend$invalidateCache
+ _objc_msgSend$isCachedSnapshot
+ _objc_msgSend$isClipComplete
+ _objc_msgSend$isRegulatoryEraseRequiredForLastRemovedCurrentAccessory
+ _objc_msgSend$maxDataSegmentDuration
+ _objc_msgSend$mediaDestinationController:didUpdateGroupName:
+ _objc_msgSend$metricContext
+ _objc_msgSend$needsNotificationForState:
+ _objc_msgSend$notifyDelegateUpdatedSupportsRTAPATAudioUsingContext:
+ _objc_msgSend$notifyDestinationControllersWithDestinationControllerData:
+ _objc_msgSend$notifyDidUpdateGroupName
+ _objc_msgSend$notifyDidUpdateSupportedOptions
+ _objc_msgSend$proxPairingCardLaunchSessionID
+ _objc_msgSend$proxPairingMetricsSessionID
+ _objc_msgSend$rawGroupName
+ _objc_msgSend$resetMetricCountsIfNeeded
+ _objc_msgSend$segmentsString
+ _objc_msgSend$setAlternativeEntitlements:
+ _objc_msgSend$setClientHasMediaGroupsEnabled:
+ _objc_msgSend$setColorCode:
+ _objc_msgSend$setDisableRealCameraContent:
+ _objc_msgSend$setGroupName:
+ _objc_msgSend$setMaxDataSegmentDuration:
+ _objc_msgSend$setProxPairingCardLaunchSessionID:
+ _objc_msgSend$setProxPairingMetricsSessionID:
+ _objc_msgSend$setSupportsAudioDestinationMediaSystemVirtualHomePod:
+ _objc_msgSend$setSupportsAudioDestinationVirtualHomeTheater:
+ _objc_msgSend$setSupportsECDSAKey:
+ _objc_msgSend$setSupportsHomeTheaterNaming:
+ _objc_msgSend$setSupportsRegulatoryErase:
+ _objc_msgSend$setSuppressDPS:
+ _objc_msgSend$setThermostatPreset:
+ _objc_msgSend$setUserConfigurationReady:
+ _objc_msgSend$stageGroups:destinations:destinationControllersData:removedGroupIdentifiers:
+ _objc_msgSend$stagedDestinationControllerData
+ _objc_msgSend$startMetricWithMetricType:
+ _objc_msgSend$stopMetricWithResult:
+ _objc_msgSend$supportsAudioDestinationMediaSystemVirtualHomePod
+ _objc_msgSend$supportsAudioDestinationVirtualHomeTheater
+ _objc_msgSend$supportsECDSAKey
+ _objc_msgSend$supportsHomeTheaterNaming
+ _objc_msgSend$supportsRegulatoryErase
+ _objc_msgSend$swiftEventForTriggerType:dictionary:home:
+ _objc_msgSend$transferDeadline
+ _symbolic SDySSSiG
+ _symbolic SS16bundleIdentifier_SS8typeNamet
+ _symbolic SS______t 7ToolKit10TypedValueO
+ _symbolic SaySDySSypGG
+ _symbolic Say_____G 7HomeKit23AccessoryHealthSnapshotV10ErrorCountV
+ _symbolic Say_____G 7HomeKit24IdentifiedHealthSnapshotV
+ _symbolic Say_____G So18HMClientConnectionC7HomeKitE08HydratedC6EntityV
+ _symbolic Say_____G So18HMClientConnectionC7HomeKitE08HydratedC6EntityV0F9ReferenceV
+ _symbolic Say_____G So18HMClientConnectionC7HomeKitE20HydrationRequestItemV
+ _symbolic ScSy_____G So6HMHomeC7HomeKitE11CaptionPlanO
+ _symbolic Si5count_t
+ _symbolic So7NSErrorCSg
+ _symbolic _____ 7HomeKit18AccessoryHealthSPIV
+ _symbolic _____ 7HomeKit23AccessoryHealthSnapshotV
+ _symbolic _____ 7HomeKit23AccessoryHealthSnapshotV10ErrorCountV
+ _symbolic _____ 7HomeKit24IdentifiedHealthSnapshotV
+ _symbolic _____ 7HomeKit30AccessoryHealthSnapshotMessageO
+ _symbolic _____ 7HomeKit30AccessoryHealthSnapshotMessageO14RequestPayloadV
+ _symbolic _____ 7HomeKit30AccessoryHealthSnapshotMessageO15ResponsePayloadV
+ _symbolic _____ So18HMClientConnectionC7HomeKitE07HydrateC15EntitiesRequestV
+ _symbolic _____ So18HMClientConnectionC7HomeKitE07HydrateC15EntitiesRequestV0G7PayloadV
+ _symbolic _____ So18HMClientConnectionC7HomeKitE07HydrateC15EntitiesRequestV0G7PayloadV10CodingKeys33_CDC1F0A71EBD15EE416B075C79B451BCLLO
+ _symbolic _____ So18HMClientConnectionC7HomeKitE07HydrateC15EntitiesRequestV15ResponsePayloadV
+ _symbolic _____ So18HMClientConnectionC7HomeKitE07HydrateC15EntitiesRequestV15ResponsePayloadV10CodingKeys33_CDC1F0A71EBD15EE416B075C79B451BCLLO
+ _symbolic _____ So18HMClientConnectionC7HomeKitE08HydratedC6EntityV
+ _symbolic _____ So18HMClientConnectionC7HomeKitE08HydratedC6EntityV0F9ReferenceV
+ _symbolic _____ So18HMClientConnectionC7HomeKitE08HydratedC6EntityV0F9ReferenceV10CodingKeys33_F18E7B87BB31449A79B57FA3A7933904LLO
+ _symbolic _____ So18HMClientConnectionC7HomeKitE08HydratedC6EntityV10CodingKeys33_F18E7B87BB31449A79B57FA3A7933904LLO
+ _symbolic _____ So18HMClientConnectionC7HomeKitE14SchemaTypeNameO
+ _symbolic _____ So18HMClientConnectionC7HomeKitE20HydrationRequestItemV
+ _symbolic _____ So18HMClientConnectionC7HomeKitE20HydrationRequestItemV10CodingKeys33_CDC1F0A71EBD15EE416B075C79B451BCLLO
+ _symbolic _____ So6HMHomeC7HomeKitE11CaptionPlanO
+ _symbolic _____Sg 7ToolKit21DisplayRepresentationV
+ _symbolic _____Sg 7ToolKit21DisplayRepresentationV15PluginModelDataV
+ _symbolic _____Sg 7ToolKit21DisplayRepresentationV5ImageO
+ _symbolic _____Sg So18HMClientConnectionC7HomeKitE08HydratedC6EntityV0F9ReferenceV
+ _symbolic ___________t 10Foundation4UUIDV 7ToolKit10TypedValueO06EntityF0V
+ _symbolic ______pSgIeghg_Sg s5ErrorP
+ _symbolic _____ySDySSypGG s23_ContiguousArrayStorageC
+ _symbolic _____ySSSiG s18_DictionaryStorageC
+ _symbolic _____ySS_____G s18_DictionaryStorageC 7ToolKit10TypedValueO
+ _symbolic _____ySS______tG s23_ContiguousArrayStorageC 7ToolKit10TypedValueO
+ _symbolic _____y_____G 15Synchronization5_CellVAARi_zrlE So6HMHomeC7HomeKitE15SwiftExtensionsC5StateV
+ _symbolic _____y_____G s22KeyedDecodingContainerV So18HMClientConnectionC7HomeKitE07HydrateF15EntitiesRequestV0J7PayloadV10CodingKeys33_CDC1F0A71EBD15EE416B075C79B451BCLLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV So18HMClientConnectionC7HomeKitE07HydrateF15EntitiesRequestV15ResponsePayloadV10CodingKeys33_CDC1F0A71EBD15EE416B075C79B451BCLLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV So18HMClientConnectionC7HomeKitE08HydratedF6EntityV0I9ReferenceV10CodingKeys33_F18E7B87BB31449A79B57FA3A7933904LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV So18HMClientConnectionC7HomeKitE08HydratedF6EntityV10CodingKeys33_F18E7B87BB31449A79B57FA3A7933904LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV So18HMClientConnectionC7HomeKitE20HydrationRequestItemV10CodingKeys33_CDC1F0A71EBD15EE416B075C79B451BCLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV So18HMClientConnectionC7HomeKitE07HydrateF15EntitiesRequestV0J7PayloadV10CodingKeys33_CDC1F0A71EBD15EE416B075C79B451BCLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV So18HMClientConnectionC7HomeKitE07HydrateF15EntitiesRequestV15ResponsePayloadV10CodingKeys33_CDC1F0A71EBD15EE416B075C79B451BCLLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV So18HMClientConnectionC7HomeKitE08HydratedF6EntityV0I9ReferenceV10CodingKeys33_F18E7B87BB31449A79B57FA3A7933904LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV So18HMClientConnectionC7HomeKitE08HydratedF6EntityV10CodingKeys33_F18E7B87BB31449A79B57FA3A7933904LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV So18HMClientConnectionC7HomeKitE20HydrationRequestItemV10CodingKeys33_CDC1F0A71EBD15EE416B075C79B451BCLLO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 7HomeKit23AccessoryHealthSnapshotV10ErrorCountV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 7HomeKit24IdentifiedHealthSnapshotV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 7ToolKit10TypedValueO
+ _symbolic _____y______G ScS12ContinuationV So6HMHomeC7HomeKitE11CaptionPlanO
+ _symbolic _____y______GSg ScS12ContinuationV So6HMHomeC7HomeKitE11CaptionPlanO
+ _symbolic _____y_______G ScS12ContinuationV11YieldResultO So6HMHomeC7HomeKitE11CaptionPlanO
+ _symbolic _____y_______G ScS12ContinuationV15BufferingPolicyO So6HMHomeC7HomeKitE11CaptionPlanO
+ _symbolic _____y_______GSg ScS12ContinuationV11YieldResultO So6HMHomeC7HomeKitE11CaptionPlanO
+ _symbolic _____y__________G s18_DictionaryStorageC 10Foundation4UUIDV 7ToolKit10TypedValueO06EntityH0V
+ _type_layout_string 7HomeKit18AccessoryHealthSPIV
+ _type_layout_string 7HomeKit23AccessoryHealthSnapshotV
+ _type_layout_string 7HomeKit23AccessoryHealthSnapshotV10ErrorCountV
+ _type_layout_string 7HomeKit24IdentifiedHealthSnapshotV
+ _type_layout_string 7HomeKit30AccessoryHealthSnapshotMessageO15ResponsePayloadV
+ _type_layout_string So18HMClientConnectionC7HomeKitE07HydrateC15EntitiesRequestV0G7PayloadV
+ allowedTargetValueClassesForShortcuts._hmf_once_t36
+ allowedTargetValueClassesForShortcuts._hmf_once_v37
+ get_witness_table ScSySo6HMHomeC7HomeKitE11CaptionPlanOGSciHPyHC
+ logCategory._hmf_once_t105
+ logCategory._hmf_once_t107
+ logCategory._hmf_once_t119
+ logCategory._hmf_once_t123
+ logCategory._hmf_once_t133
+ logCategory._hmf_once_t145
+ logCategory._hmf_once_t152
+ logCategory._hmf_once_t20
+ logCategory._hmf_once_t219
+ logCategory._hmf_once_t243
+ logCategory._hmf_once_t28
+ logCategory._hmf_once_t31
+ logCategory._hmf_once_t40
+ logCategory._hmf_once_t41
+ logCategory._hmf_once_t45
+ logCategory._hmf_once_t48
+ logCategory._hmf_once_t50
+ logCategory._hmf_once_t51
+ logCategory._hmf_once_t547
+ logCategory._hmf_once_t58
+ logCategory._hmf_once_t61
+ logCategory._hmf_once_t706
+ logCategory._hmf_once_t71
+ logCategory._hmf_once_t72
+ logCategory._hmf_once_t780
+ logCategory._hmf_once_t80
+ logCategory._hmf_once_t81
+ logCategory._hmf_once_t89
+ logCategory._hmf_once_t94
+ logCategory._hmf_once_v106
+ logCategory._hmf_once_v108
+ logCategory._hmf_once_v120
+ logCategory._hmf_once_v124
+ logCategory._hmf_once_v134
+ logCategory._hmf_once_v146
+ logCategory._hmf_once_v153
+ logCategory._hmf_once_v21
+ logCategory._hmf_once_v220
+ logCategory._hmf_once_v244
+ logCategory._hmf_once_v29
+ logCategory._hmf_once_v32
+ logCategory._hmf_once_v41
+ logCategory._hmf_once_v42
+ logCategory._hmf_once_v46
+ logCategory._hmf_once_v49
+ logCategory._hmf_once_v51
+ logCategory._hmf_once_v52
+ logCategory._hmf_once_v548
+ logCategory._hmf_once_v59
+ logCategory._hmf_once_v62
+ logCategory._hmf_once_v707
+ logCategory._hmf_once_v72
+ logCategory._hmf_once_v73
+ logCategory._hmf_once_v781
+ logCategory._hmf_once_v81
+ logCategory._hmf_once_v82
+ logCategory._hmf_once_v90
+ logCategory._hmf_once_v95
- +[HMAccessory(Camera) _cameraProfilesForAccessoryProfiles:]
- +[HMCameraClipVideoHLSPlaylistGenerator _hlsPlaylistEncryptionMethodNameForScheme:]
- -[HMAccessory _notifyCameraProfileVisibilityChangedForCharacteristic:value:previousValue:]
- -[HMAccessorySetupManager simulateNFCTapWithSetupURLString:completionHandler:]
- -[HMCameraClipVideoHLSPlaylistGenerator hlsPlaylistString]
- -[HMHome(Wallet) fetchWalleKeyExpressEnablementConflictingPassDescription:]
- -[HMHomeTheaterSystem initWithIdentifier:parentIdentifier:name:audioDestinationIdentifier:audioDestinationType:]
- -[HMMediaDestinationController initWithControllerData:]
- -[HMMediaGroupStagingManager clearStagedDestinationControllerDataForIdentifier:]
- -[HMMediaGroupStagingManager clearStagedDestinationControllerData]
- -[HMMediaGroupStagingManager clearStagedDestinationForIdentifier:]
- -[HMMediaGroupStagingManager clearStagedDestinations]
- -[HMMediaGroupStagingManager clearStagedGroupForIdentifier:]
- -[HMMediaGroupStagingManager clearStagedGroups]
- -[HMMediaGroupStagingManager clearStagedRemovedGroupIdentifiers]
- -[HMMediaGroupStagingManager configureWithMessageDispatcher:]
- -[HMMediaGroupStagingManager metricStartTime]
- -[HMMediaGroupStagingManager metricType]
- -[HMMediaGroupStagingManager setMetricStartTime:]
- -[HMMediaGroupStagingManager setMetricType:]
- -[HMMediaGroupStagingManager stageDestinationControllersData:]
- -[HMMediaGroupStagingManager stageDestinations:]
- -[HMMediaGroupStagingManager stageGroups:]
- -[HMMediaGroupStagingManager stageRemovedGroupIdentifiers:]
- -[HMSetupAccessoryPayload initWithVersion1LegacyPayloadData:value:length:payloadBytes:reserved:setupPayloadURL:outError:]
- -[HMSoftwareUpdateDocumentationAsset documentationIsCached]
- -[HMSoftwareUpdateDocumentationAsset stateNeedsNotification]
- -[HMSoftwareUpdateDocumentationManager didUpdateDocumentationAssetState:]
- GCC_except_table10003
- GCC_except_table10004
- GCC_except_table10005
- GCC_except_table10007
- GCC_except_table10010
- GCC_except_table10011
- GCC_except_table10017
- GCC_except_table10166
- GCC_except_table10167
- GCC_except_table10172
- GCC_except_table10227
- GCC_except_table10250
- GCC_except_table10330
- GCC_except_table10332
- GCC_except_table10334
- GCC_except_table10336
- GCC_except_table10344
- GCC_except_table10391
- GCC_except_table10403
- GCC_except_table10405
- GCC_except_table10595
- GCC_except_table10596
- GCC_except_table10631
- GCC_except_table10664
- GCC_except_table10667
- GCC_except_table10670
- GCC_except_table10672
- GCC_except_table10751
- GCC_except_table10771
- GCC_except_table10772
- GCC_except_table10773
- GCC_except_table10812
- GCC_except_table10814
- GCC_except_table10816
- GCC_except_table10881
- GCC_except_table10913
- GCC_except_table10915
- GCC_except_table10919
- GCC_except_table10936
- GCC_except_table10938
- GCC_except_table10944
- GCC_except_table10948
- GCC_except_table10951
- GCC_except_table10958
- GCC_except_table10962
- GCC_except_table10968
- GCC_except_table10980
- GCC_except_table10983
- GCC_except_table10991
- GCC_except_table10992
- GCC_except_table10994
- GCC_except_table10996
- GCC_except_table10998
- GCC_except_table11018
- GCC_except_table11028
- GCC_except_table11231
- GCC_except_table11244
- GCC_except_table11277
- GCC_except_table11280
- GCC_except_table11282
- GCC_except_table11295
- GCC_except_table11296
- GCC_except_table11364
- GCC_except_table11367
- GCC_except_table11368
- GCC_except_table1164
- GCC_except_table1168
- GCC_except_table11715
- GCC_except_table1175
- GCC_except_table11753
- GCC_except_table11766
- GCC_except_table12122
- GCC_except_table12124
- GCC_except_table12126
- GCC_except_table12127
- GCC_except_table12137
- GCC_except_table12162
- GCC_except_table12165
- GCC_except_table12168
- GCC_except_table12177
- GCC_except_table12178
- GCC_except_table12179
- GCC_except_table12302
- GCC_except_table12304
- GCC_except_table12308
- GCC_except_table12309
- GCC_except_table12357
- GCC_except_table12383
- GCC_except_table12396
- GCC_except_table12422
- GCC_except_table12426
- GCC_except_table12477
- GCC_except_table12479
- GCC_except_table12509
- GCC_except_table12510
- GCC_except_table12511
- GCC_except_table12512
- GCC_except_table12513
- GCC_except_table12514
- GCC_except_table12515
- GCC_except_table12516
- GCC_except_table12517
- GCC_except_table12518
- GCC_except_table12519
- GCC_except_table1252
- GCC_except_table12520
- GCC_except_table12521
- GCC_except_table12522
- GCC_except_table12523
- GCC_except_table12546
- GCC_except_table1261
- GCC_except_table12683
- GCC_except_table12684
- GCC_except_table12687
- GCC_except_table12753
- GCC_except_table12755
- GCC_except_table12763
- GCC_except_table12774
- GCC_except_table12776
- GCC_except_table12781
- GCC_except_table12782
- GCC_except_table12783
- GCC_except_table13005
- GCC_except_table13206
- GCC_except_table13209
- GCC_except_table13214
- GCC_except_table13218
- GCC_except_table13226
- GCC_except_table13231
- GCC_except_table13233
- GCC_except_table13238
- GCC_except_table13239
- GCC_except_table13241
- GCC_except_table1331
- GCC_except_table13323
- GCC_except_table13325
- GCC_except_table1333
- GCC_except_table13344
- GCC_except_table13345
- GCC_except_table13347
- GCC_except_table13352
- GCC_except_table13366
- GCC_except_table13372
- GCC_except_table13375
- GCC_except_table13379
- GCC_except_table1338
- GCC_except_table1340
- GCC_except_table1344
- GCC_except_table13457
- GCC_except_table13471
- GCC_except_table13477
- GCC_except_table13479
- GCC_except_table13481
- GCC_except_table13483
- GCC_except_table13485
- GCC_except_table13487
- GCC_except_table13489
- GCC_except_table13622
- GCC_except_table13678
- GCC_except_table13679
- GCC_except_table13680
- GCC_except_table13681
- GCC_except_table13691
- GCC_except_table13692
- GCC_except_table13716
- GCC_except_table13717
- GCC_except_table13791
- GCC_except_table13813
- GCC_except_table13816
- GCC_except_table13961
- GCC_except_table14131
- GCC_except_table14136
- GCC_except_table14139
- GCC_except_table14192
- GCC_except_table14225
- GCC_except_table14230
- GCC_except_table14231
- GCC_except_table14232
- GCC_except_table14233
- GCC_except_table14235
- GCC_except_table14244
- GCC_except_table14246
- GCC_except_table14248
- GCC_except_table14253
- GCC_except_table14254
- GCC_except_table14255
- GCC_except_table14256
- GCC_except_table14257
- GCC_except_table14259
- GCC_except_table14263
- GCC_except_table14265
- GCC_except_table14401
- GCC_except_table14404
- GCC_except_table14424
- GCC_except_table14426
- GCC_except_table14427
- GCC_except_table1510
- GCC_except_table1536
- GCC_except_table1602
- GCC_except_table1673
- GCC_except_table1678
- GCC_except_table1696
- GCC_except_table1764
- GCC_except_table1766
- GCC_except_table1777
- GCC_except_table1779
- GCC_except_table1908
- GCC_except_table1960
- GCC_except_table1963
- GCC_except_table2037
- GCC_except_table2126
- GCC_except_table2127
- GCC_except_table2176
- GCC_except_table2444
- GCC_except_table2447
- GCC_except_table2450
- GCC_except_table2455
- GCC_except_table2459
- GCC_except_table2481
- GCC_except_table2484
- GCC_except_table2489
- GCC_except_table2490
- GCC_except_table2491
- GCC_except_table3048
- GCC_except_table3053
- GCC_except_table3079
- GCC_except_table3082
- GCC_except_table3095
- GCC_except_table3127
- GCC_except_table3130
- GCC_except_table3156
- GCC_except_table3158
- GCC_except_table3160
- GCC_except_table3162
- GCC_except_table3309
- GCC_except_table3312
- GCC_except_table3320
- GCC_except_table3321
- GCC_except_table3342
- GCC_except_table3369
- GCC_except_table3370
- GCC_except_table3428
- GCC_except_table3430
- GCC_except_table3433
- GCC_except_table3434
- GCC_except_table3460
- GCC_except_table3462
- GCC_except_table3470
- GCC_except_table3472
- GCC_except_table3479
- GCC_except_table3480
- GCC_except_table3481
- GCC_except_table3483
- GCC_except_table3484
- GCC_except_table3485
- GCC_except_table3486
- GCC_except_table3487
- GCC_except_table3570
- GCC_except_table3593
- GCC_except_table3596
- GCC_except_table3599
- GCC_except_table3605
- GCC_except_table3608
- GCC_except_table3611
- GCC_except_table3676
- GCC_except_table3677
- GCC_except_table3723
- GCC_except_table3730
- GCC_except_table3731
- GCC_except_table3732
- GCC_except_table3735
- GCC_except_table3736
- GCC_except_table3737
- GCC_except_table3739
- GCC_except_table3747
- GCC_except_table3769
- GCC_except_table3778
- GCC_except_table3782
- GCC_except_table3785
- GCC_except_table3788
- GCC_except_table3829
- GCC_except_table3833
- GCC_except_table3842
- GCC_except_table3850
- GCC_except_table3854
- GCC_except_table3863
- GCC_except_table3865
- GCC_except_table4104
- GCC_except_table4109
- GCC_except_table4113
- GCC_except_table4116
- GCC_except_table4120
- GCC_except_table4121
- GCC_except_table4126
- GCC_except_table4132
- GCC_except_table4136
- GCC_except_table4140
- GCC_except_table4163
- GCC_except_table4165
- GCC_except_table4167
- GCC_except_table4170
- GCC_except_table4171
- GCC_except_table4173
- GCC_except_table4176
- GCC_except_table4251
- GCC_except_table4265
- GCC_except_table4268
- GCC_except_table4270
- GCC_except_table4273
- GCC_except_table4280
- GCC_except_table4419
- GCC_except_table4426
- GCC_except_table4431
- GCC_except_table4624
- GCC_except_table4672
- GCC_except_table4872
- GCC_except_table4874
- GCC_except_table4881
- GCC_except_table4889
- GCC_except_table4910
- GCC_except_table4921
- GCC_except_table4926
- GCC_except_table4929
- GCC_except_table4943
- GCC_except_table4948
- GCC_except_table4954
- GCC_except_table4959
- GCC_except_table4964
- GCC_except_table4969
- GCC_except_table4974
- GCC_except_table4978
- GCC_except_table4983
- GCC_except_table5030
- GCC_except_table5034
- GCC_except_table5044
- GCC_except_table5049
- GCC_except_table5063
- GCC_except_table5068
- GCC_except_table5075
- GCC_except_table5092
- GCC_except_table5093
- GCC_except_table5095
- GCC_except_table5097
- GCC_except_table5100
- GCC_except_table5105
- GCC_except_table5112
- GCC_except_table5117
- GCC_except_table5121
- GCC_except_table5157
- GCC_except_table5204
- GCC_except_table5215
- GCC_except_table5269
- GCC_except_table5334
- GCC_except_table5349
- GCC_except_table5352
- GCC_except_table5444
- GCC_except_table5445
- GCC_except_table5448
- GCC_except_table5453
- GCC_except_table5457
- GCC_except_table5460
- GCC_except_table5470
- GCC_except_table5716
- GCC_except_table5719
- GCC_except_table5731
- GCC_except_table5807
- GCC_except_table5851
- GCC_except_table5944
- GCC_except_table6208
- GCC_except_table6211
- GCC_except_table6303
- GCC_except_table6322
- GCC_except_table6332
- GCC_except_table6468
- GCC_except_table6477
- GCC_except_table6490
- GCC_except_table6497
- GCC_except_table6536
- GCC_except_table6538
- GCC_except_table6566
- GCC_except_table6568
- GCC_except_table6570
- GCC_except_table6572
- GCC_except_table6579
- GCC_except_table6585
- GCC_except_table6591
- GCC_except_table6601
- GCC_except_table6607
- GCC_except_table6684
- GCC_except_table6693
- GCC_except_table6695
- GCC_except_table6705
- GCC_except_table6707
- GCC_except_table6709
- GCC_except_table6711
- GCC_except_table6713
- GCC_except_table6719
- GCC_except_table6723
- GCC_except_table6736
- GCC_except_table6742
- GCC_except_table6761
- GCC_except_table6791
- GCC_except_table6840
- GCC_except_table6852
- GCC_except_table6854
- GCC_except_table6878
- GCC_except_table6879
- GCC_except_table6881
- GCC_except_table6936
- GCC_except_table6949
- GCC_except_table7209
- GCC_except_table7211
- GCC_except_table7226
- GCC_except_table7264
- GCC_except_table7266
- GCC_except_table7284
- GCC_except_table7330
- GCC_except_table7425
- GCC_except_table7445
- GCC_except_table7446
- GCC_except_table7447
- GCC_except_table7449
- GCC_except_table7452
- GCC_except_table7453
- GCC_except_table7455
- GCC_except_table7781
- GCC_except_table7787
- GCC_except_table7789
- GCC_except_table7799
- GCC_except_table7800
- GCC_except_table7875
- GCC_except_table7885
- GCC_except_table7981
- GCC_except_table8160
- GCC_except_table8164
- GCC_except_table8262
- GCC_except_table8266
- GCC_except_table8268
- GCC_except_table8269
- GCC_except_table8408
- GCC_except_table8417
- GCC_except_table8533
- GCC_except_table8588
- GCC_except_table8590
- GCC_except_table8592
- GCC_except_table8614
- GCC_except_table8642
- GCC_except_table8654
- GCC_except_table8672
- GCC_except_table8689
- GCC_except_table8691
- GCC_except_table8693
- GCC_except_table8695
- GCC_except_table8697
- GCC_except_table8699
- GCC_except_table8701
- GCC_except_table8705
- GCC_except_table8707
- GCC_except_table8709
- GCC_except_table8711
- GCC_except_table8713
- GCC_except_table8718
- GCC_except_table8732
- GCC_except_table8758
- GCC_except_table8760
- GCC_except_table8785
- GCC_except_table8798
- GCC_except_table8816
- GCC_except_table8995
- GCC_except_table9334
- GCC_except_table9377
- GCC_except_table944
- GCC_except_table9470
- GCC_except_table9479
- GCC_except_table951
- GCC_except_table957
- GCC_except_table964
- GCC_except_table9654
- GCC_except_table9656
- GCC_except_table9657
- GCC_except_table9658
- GCC_except_table9660
- GCC_except_table9662
- GCC_except_table9663
- GCC_except_table9664
- GCC_except_table9699
- GCC_except_table9702
- GCC_except_table9703
- GCC_except_table9706
- GCC_except_table9709
- GCC_except_table9710
- GCC_except_table9753
- GCC_except_table9754
- GCC_except_table9755
- GCC_except_table9762
- GCC_except_table9763
- GCC_except_table9765
- GCC_except_table9784
- GCC_except_table9853
- GCC_except_table9854
- GCC_except_table9855
- GCC_except_table9893
- GCC_except_table9907
- GCC_except_table9975
- OBJC_IVAR_$_HMCameraClipVideoHLSPlaylistGenerator._hlsPlaylistString
- OBJC_IVAR_$_HMMediaGroupStagingManager._metricStartTime
- OBJC_IVAR_$_HMMediaGroupStagingManager._metricType
- _HMAccessorySetupManagerMessageKeyNFCSetupURLString
- __70-[_HMContext(Convenience) sendMessage:target:payload:responseHandler:]_block_invoke
- __70-[_HMContext(Convenience) sendMessage:target:payload:responseHandler:]_block_invoke_2
- __OBJC_$_CLASS_METHODS_HMAccessory(HomeKit|DynamicAccessorySettingsAdapter|SwiftExtensions|SiriEndpoint|Television|LightInternal|HMDoorbellChimeProfile|NetworkRouter|PendingConfiguration|Private|CUPeerIdentifier|Diagnostics|Shortcuts|Camera|CHIP|NetworkConfiguration|Climate|Light|Media)
- __OBJC_$_CLASS_METHODS_HMCameraClipVideoHLSPlaylistGenerator
- __OBJC_$_CLASS_METHODS_HMHome(HomeKit|HomeKit1|SwiftExtensions|HomeKit2|AccessCode|WalletInternal|Wallet|Light|HMAccessory|HMRoom|HMZone|HMServiceGroup|HMUser|HMActionSet|HMTrigger|RemoteAccess|HMSoftwareUpdate|HMMediaProfile|NetworkRouter|HMUserActionPredictions|ThreadManagement|HMHomeHub|PowerAssertionInfo|HomeNetworkInfo|HomeLocationFeedback|MediaGroupReadinessCheck|HomeActivityState|ResidentSelection|HMModernMessaging|HMModernMessagingInternal|Trigger|Biome|Climate|MediaGroupSettingsControllerFactory|ThreadResidentCommissioning|SiriEndpointProfilesMessengerFactory|HMActionExecution|Person|Person_Internal|Matter|CHIP|AutomationBuilders)
- __OBJC_$_INSTANCE_METHODS_HMAccessory(HomeKit|DynamicAccessorySettingsAdapter|SwiftExtensions|SiriEndpoint|Television|LightInternal|HMDoorbellChimeProfile|NetworkRouter|PendingConfiguration|Private|CUPeerIdentifier|Diagnostics|Shortcuts|Camera|CHIP|NetworkConfiguration|Climate|Light|Media)
- __OBJC_$_INSTANCE_METHODS_HMEventTrigger(HMEventTriggerBuilder)
- __OBJC_$_INSTANCE_METHODS_HMHome(HomeKit|HomeKit1|SwiftExtensions|HomeKit2|AccessCode|WalletInternal|Wallet|Light|HMAccessory|HMRoom|HMZone|HMServiceGroup|HMUser|HMActionSet|HMTrigger|RemoteAccess|HMSoftwareUpdate|HMMediaProfile|NetworkRouter|HMUserActionPredictions|ThreadManagement|HMHomeHub|PowerAssertionInfo|HomeNetworkInfo|HomeLocationFeedback|MediaGroupReadinessCheck|HomeActivityState|ResidentSelection|HMModernMessaging|HMModernMessagingInternal|Trigger|Biome|Climate|MediaGroupSettingsControllerFactory|ThreadResidentCommissioning|SiriEndpointProfilesMessengerFactory|HMActionExecution|Person|Person_Internal|Matter|CHIP|AutomationBuilders)
- __OBJC_CLASS_PROTOCOLS_$_HMHome(HomeKit|HomeKit1|SwiftExtensions|HomeKit2|AccessCode|WalletInternal|Wallet|Light|HMAccessory|HMRoom|HMZone|HMServiceGroup|HMUser|HMActionSet|HMTrigger|RemoteAccess|HMSoftwareUpdate|HMMediaProfile|NetworkRouter|HMUserActionPredictions|ThreadManagement|HMHomeHub|PowerAssertionInfo|HomeNetworkInfo|HomeLocationFeedback|MediaGroupReadinessCheck|HomeActivityState|ResidentSelection|HMModernMessaging|HMModernMessagingInternal|Trigger|Biome|Climate|MediaGroupSettingsControllerFactory|ThreadResidentCommissioning|SiriEndpointProfilesMessengerFactory|HMActionExecution|Person|Person_Internal|Matter|CHIP|AutomationBuilders)
- ___42-[HMMediaGroupStagingManager stageGroups:]_block_invoke
- ___47-[HMMediaGroupStagingManager clearStagedGroups]_block_invoke
- ___48-[HMMediaGroupStagingManager stageDestinations:]_block_invoke
- ___53-[HMMediaGroupStagingManager clearStagedDestinations]_block_invoke
- ___58-[HMHome(HMAccessory) _removeAccessory:completionHandler:]_block_invoke
- ___62-[HMMediaGroupStagingManager stageDestinationControllersData:]_block_invoke
- ___66-[HMMediaGroupStagingManager clearStagedDestinationControllerData]_block_invoke
- ___70-[HMHomeManager(DemoMode) exportDemoAccessoriesWithCompletionHandler:]_block_invoke_2
- ___70-[_HMContext(Convenience) sendMessage:target:payload:responseHandler:]_block_invoke
- ___70-[_HMContext(Convenience) sendMessage:target:payload:responseHandler:]_block_invoke_2
- ___73-[HMSoftwareUpdateDocumentationManager addAssetAndCompletion:completion:]_block_invoke
- ___73-[HMSoftwareUpdateDocumentationManager didUpdateDocumentationAssetState:]_block_invoke
- ___75-[HMHome(Wallet) fetchWalleKeyExpressEnablementConflictingPassDescription:]_block_invoke
- ___78-[HMAccessorySetupManager simulateNFCTapWithSetupURLString:completionHandler:]_block_invoke
- ___90-[HMAccessory _notifyCameraProfileVisibilityChangedForCharacteristic:value:previousValue:]_block_invoke
- _kAccessoryReprovisonStateKey
- _objc_msgSend$_hlsPlaylistEncryptionMethodNameForScheme:
- _objc_msgSend$_notifyCameraProfileVisibilityChangedForCharacteristic:value:previousValue:
- _objc_msgSend$clearStagedDestinationControllerData
- _objc_msgSend$clearStagedDestinationControllerDataForIdentifier:
- _objc_msgSend$clearStagedDestinationForIdentifier:
- _objc_msgSend$clearStagedDestinations
- _objc_msgSend$clearStagedGroupForIdentifier:
- _objc_msgSend$clearStagedGroups
- _objc_msgSend$clearStagedRemovedGroupIdentifiers
- _objc_msgSend$configureWithMessageDispatcher:
- _objc_msgSend$didUpdateDocumentationAssetState:
- _objc_msgSend$documentationIsCached
- _objc_msgSend$hlsPlaylistString
- _objc_msgSend$initWithControllerData:
- _objc_msgSend$initWithIdentifier:parentIdentifier:destinationIdentifier:supportedOptions:availableDestinationIdentifiers:
- _objc_msgSend$initWithIdentifier:parentIdentifier:name:audioDestinationIdentifier:audioDestinationType:
- _objc_msgSend$initWithSnapshotPath:urlParameters:privacyPolicyURL:uploadDestination:consentVersion:uploadType:
- _objc_msgSend$initWithVersion1LegacyPayloadData:value:length:payloadBytes:reserved:setupPayloadURL:outError:
- _objc_msgSend$metricStartTime
- _objc_msgSend$setMetricStartTime:
- _objc_msgSend$setMetricType:
- _objc_msgSend$stageDestinationControllersData:
- _objc_msgSend$stageDestinations:
- _objc_msgSend$stageGroups:
- _objc_msgSend$stageRemovedGroupIdentifiers:
- _objc_msgSend$stateNeedsNotification
- _objc_msgSend$systemUptime
- _symbolic So7NSErrorCSgIeyBy_
- _symbolic ______pSgIegg_Sg s5ErrorP
- allowedTargetValueClassesForShortcuts._hmf_once_t29
- allowedTargetValueClassesForShortcuts._hmf_once_v30
- logCategory._hmf_once_t112
- logCategory._hmf_once_t114
- logCategory._hmf_once_t13
- logCategory._hmf_once_t136
- logCategory._hmf_once_t144
- logCategory._hmf_once_t17
- logCategory._hmf_once_t179
- logCategory._hmf_once_t23
- logCategory._hmf_once_t234
- logCategory._hmf_once_t25
- logCategory._hmf_once_t35
- logCategory._hmf_once_t37
- logCategory._hmf_once_t486
- logCategory._hmf_once_t54
- logCategory._hmf_once_t55
- logCategory._hmf_once_t562
- logCategory._hmf_once_t59
- logCategory._hmf_once_t64
- logCategory._hmf_once_t643
- logCategory._hmf_once_t78
- logCategory._hmf_once_t86
- logCategory._hmf_once_t88
- logCategory._hmf_once_t97
- logCategory._hmf_once_v113
- logCategory._hmf_once_v115
- logCategory._hmf_once_v137
- logCategory._hmf_once_v14
- logCategory._hmf_once_v145
- logCategory._hmf_once_v18
- logCategory._hmf_once_v180
- logCategory._hmf_once_v235
- logCategory._hmf_once_v24
- logCategory._hmf_once_v26
- logCategory._hmf_once_v36
- logCategory._hmf_once_v38
- logCategory._hmf_once_v487
- logCategory._hmf_once_v55
- logCategory._hmf_once_v56
- logCategory._hmf_once_v563
- logCategory._hmf_once_v60
- logCategory._hmf_once_v644
- logCategory._hmf_once_v65
- logCategory._hmf_once_v79
- logCategory._hmf_once_v87
- logCategory._hmf_once_v89
- logCategory._hmf_once_v98
CStrings:
+ "#EXT-X-TARGETDURATION:%llu\n"
+ "%@%@%@%@%@%@%@%@%@%@%@%@"
+ "%s Dropping malformed caption plan update"
+ ", %@: %@"
+ ", Alternative Entitlements: %@"
+ ", Color Code: %@"
+ ", captureDate: %@"
+ ", groupName: %@"
+ ", isCachedSnapshot: %@"
+ ", supportsHomeTheaterNaming: %@"
+ "-[HMAccessory fetchShouldSkipFirmwareUpdateApplyPolicyWithCompletionHandler:]"
+ "-[HMAccessory setShouldSkipFirmwareUpdateApplyPolicy:completionHandler:]"
+ "-[HMAccessory(Private) notifyPostPairingSetupCompleteWithCompletionHandler:]"
+ "-[HMAccessorySetupManager simulateNFCTapWithSetupURLStrings:completionHandler:]"
+ "-[HMHome(HMAccessory) _removeAccessory:regulatoryEraseRequired:completionHandler:]"
+ "-[HMHome(HMAccessory) removeAccessory:regulatoryEraseRequired:completionHandler:]"
+ "-[HMHomeManager _failClientDelegationRequestWithCode:completion:]"
+ "-[HMHomeManager _sendClientDelegationMessageWithName:accessoryUUIDs:auditToken:completion:]"
+ "-[HMHomeManager delegateAccessories:toProcessWithAuditToken:completionHandler:]"
+ "-[HMHomeManager revokeAccessories:fromProcessWithAuditToken:completionHandler:]"
+ "00008035-0000-1000-8000-0026BB765291"
+ "0000805F-0000-1000-8000-0026BB765291"
+ "00008088-0000-1000-8000-0026BB765291"
+ "7A3E1B9C-42D6-4F8A-B5E1-C9D7F2A68034"
+ "@\"NSUUID\"16@?0@\"HMMediaDestinationControllerData\"8"
+ "Asset is cached but has no documentation"
+ "Asset transitioned to state: %ld"
+ "BackingStoreV5RemovalHomeKitAPI"
+ "CAMERA_BUFFER_MGMT_SVC"
+ "CAMERA_CAPABILITIES_SVC"
+ "CAMERA_CLIENT_CERTIFICATE_MGMT_SVC"
+ "CAMERA_GLOBAL_OPERATING_MODE_SVC"
+ "CAMERA_KEY_MGMT_SVC"
+ "CAMERA_MOTION_ZONES_SVC"
+ "CAMERA_MULTI_TIER_RTP_STREAM_MGMT_SVC"
+ "CAMERA_PRIVACY_ZONES_SVC"
+ "CAMERA_SENSOR_OPERATING_MODE_SVC"
+ "CAMERA_WEBRTC_STREAM_MGMT_SVC"
+ "Calibration Status updated to HMAccessoryCalibrationStatusComplete"
+ "Calibration Status updated to HMAccessoryCalibrationStatusInProgress"
+ "Calling completions with cached documentation"
+ "Calling did update group name: %{private}@ for delegate: %@"
+ "Calling did update supported options: %@ for delegate: %@"
+ "Client delegation request rejected: an accessory has no UUID"
+ "Configuring with message dispatcher: %@, clientHasMediaGroupsEnabled: %@"
+ "CoreAnalytics.Metric.Event.Dispatcher"
+ "Failed to create unarchiver for accessory from %{public}@ with error: %{public}@"
+ "Failed to notify client of updated group name due to no delegate caller given by context: %@"
+ "Failed to notify client of updated supported options due to no delegate caller given by context: %@"
+ "Failed to unarchive accessory from %{public}@: %@"
+ "Failed to update group name due to no message dispatcher given by context: %@"
+ "Failed to update video resolution quality: %@"
+ "Finished hydrating %ld entities in %s"
+ "HKD"
+ "HKDG"
+ "HM.accessoryUserConfigurationReady"
+ "HM.colorCode"
+ "HMA.diagnostics.ck.cached"
+ "HMA.diagnostics.ck.cd"
+ "HMA.diagnostics.ck.cwa"
+ "HMA.diagnostics.ck.td"
+ "HMA.regulatoryEraseRequired"
+ "HMA.supportsRegulatoryErase"
+ "HMA.userConfigurationReady"
+ "HMASM.m.proxControlDismissed"
+ "HMASM.m.proxControlErrorDetailsRequested"
+ "HMASM.m.proxControlInteraction"
+ "HMASM.mk.nfcSetupURLStrings"
+ "HMASM.mk.proxControlErrorCode"
+ "HMASM.mk.proxControlErrorDetails"
+ "HMASM.pa.primaryVideo"
+ "HMAccessoryFetchShouldSkipFirmwareUpdateApplyPolicyMessage"
+ "HMAccessoryPostPairingSetupCompleteMessage"
+ "HMAccessorySetShouldSkipFirmwareUpdateApplyPolicyMessage"
+ "HMAccessoryShouldSkipFirmwareUpdateApplyPolicyMessageKey"
+ "HMAccessorySupportsHomeTheaterNamingCodingKey"
+ "HMErrorRetryableAfterReconnect"
+ "HMHM.d.at"
+ "HMHM.d.auuids"
+ "HMHM.da"
+ "HMHM.dr"
+ "HMHM.dra"
+ "HMHM.isRegulatoryEraseRequiredForLastRemovedCurrentAccessory"
+ "HMHome.CaptionPlan"
+ "HMHomeCaptionPlanCountCodingKey"
+ "HMHomeCaptionPlanTierCodingKey"
+ "HMHomeDidUpdateCaptionPlanMessage"
+ "HMHomeFetchCaptionPlanMessage"
+ "HMHomeTheaterSystemDefaultNameCodingKey"
+ "HMMediaDestinationControllerGroupNameCodingKey"
+ "HMMediaDestinationControllerGroupNamePayloadKey"
+ "HMMediaDestinationControllerUpdateGroupNameRequestMessage"
+ "HMXPCMessageHeaderKeyXPCTimeoutDate"
+ "HOME_THEATER"
+ "Handling accessory user configuration ready message: %{public}@"
+ "Home Theater"
+ "HomeDeviceEntity"
+ "HomeMatterFabricDone"
+ "Hydrating %ld entities"
+ "Invalidating cache"
+ "Merging new media destination controller group name: %{private}@"
+ "Merging supports home theater naming: %@"
+ "Missing accessory data from %{public}@"
+ "Nil message dispatcher"
+ "No asset is tracked for the metadata"
+ "No existing accessory with UUID: %{public}@"
+ "Not fetching missing wallet keys for accessory: %@, supportsCHIP: %@, supportsWalletKey: %@"
+ "Not invalidating cache in state: %@"
+ "Notifying client of updated matterNodeID: %@"
+ "Notifying client of updated supportsRTAPATAudio: %@"
+ "Notifying client that current accessory was removed with regulatoryEraseRequired: %@."
+ "ProxPairing"
+ "RegulatoryEraseOnObliteration"
+ "Sending update group name message"
+ "Setup interrupted, awaiting accessory re-tap"
+ "SetupPayload: V1 claims a color code but is only %tu characters, treating as absent"
+ "SetupPayload: V1 color code %llu is reserved, treating as absent"
+ "SetupPayload: V1 color code is not base36 encoded, treating as absent"
+ "SetupPayload: V1 is %tu characters but the color code bit is clear, ignoring trailing characters"
+ "SetupPayload: V1 parsed - paired:%d NFC:%d SetupID:%@ PN:%@ PG:%@ DeviceID:%@ ColorCode:%@"
+ "TargetLocationEntity"
+ "TargetLocationType"
+ "The completion parameter is required"
+ "The data could not be read from the file."
+ "Update group name message responded with error: %@"
+ "Update group name message succeeded"
+ "Updating matterNodeID from %@ to %@"
+ "Updating supportsRegulatoryErase from %@ to %@"
+ "VHT "
+ "VMS "
+ "[%@] Failed to localize default group name for key: %@"
+ "[%{public}@] Asset is cached but has no documentation"
+ "[%{public}@] Asset transitioned to state: %ld"
+ "[%{public}@] Calibration Status updated to HMAccessoryCalibrationStatusComplete"
+ "[%{public}@] Calibration Status updated to HMAccessoryCalibrationStatusInProgress"
+ "[%{public}@] Calling completions with cached documentation"
+ "[%{public}@] Calling did update group name: %{private}@ for delegate: %@"
+ "[%{public}@] Calling did update supported options: %@ for delegate: %@"
+ "[%{public}@] Client delegation request rejected: an accessory has no UUID"
+ "[%{public}@] Configuring with message dispatcher: %@, clientHasMediaGroupsEnabled: %@"
+ "[%{public}@] Failed to create unarchiver for accessory from %{public}@ with error: %{public}@"
+ "[%{public}@] Failed to notify client of updated group name due to no delegate caller given by context: %@"
+ "[%{public}@] Failed to notify client of updated supported options due to no delegate caller given by context: %@"
+ "[%{public}@] Failed to unarchive accessory from %{public}@: %@"
+ "[%{public}@] Failed to update group name due to no message dispatcher given by context: %@"
+ "[%{public}@] Failed to update video resolution quality: %@"
+ "[%{public}@] Handling accessory user configuration ready message: %{public}@"
+ "[%{public}@] Invalidating cache"
+ "[%{public}@] Merging new media destination controller group name: %{private}@"
+ "[%{public}@] Merging supports home theater naming: %@"
+ "[%{public}@] Missing accessory data from %{public}@"
+ "[%{public}@] No asset is tracked for the metadata"
+ "[%{public}@] No existing accessory with UUID: %{public}@"
+ "[%{public}@] Not fetching missing wallet keys for accessory: %@, supportsCHIP: %@, supportsWalletKey: %@"
+ "[%{public}@] Not invalidating cache in state: %@"
+ "[%{public}@] Notifying client of updated matterNodeID: %@"
+ "[%{public}@] Notifying client of updated supportsRTAPATAudio: %@"
+ "[%{public}@] Notifying client that current accessory was removed with regulatoryEraseRequired: %@."
+ "[%{public}@] Sending update group name message"
+ "[%{public}@] SetupPayload: V1 claims a color code but is only %tu characters, treating as absent"
+ "[%{public}@] SetupPayload: V1 color code %llu is reserved, treating as absent"
+ "[%{public}@] SetupPayload: V1 color code is not base36 encoded, treating as absent"
+ "[%{public}@] SetupPayload: V1 is %tu characters but the color code bit is clear, ignoring trailing characters"
+ "[%{public}@] SetupPayload: V1 parsed - paired:%d NFC:%d SetupID:%@ PN:%@ PG:%@ DeviceID:%@ ColorCode:%@"
+ "[%{public}@] Simulating NFC tap for %lu setup URL(s)"
+ "[%{public}@] The completion parameter is required"
+ "[%{public}@] Update group name message responded with error: %@"
+ "[%{public}@] Update group name message succeeded"
+ "[%{public}@] Updating matterNodeID from %@ to %@"
+ "[%{public}@] Updating supportsRegulatoryErase from %@ to %@"
+ "[%{public}@] [%@] Failed to localize default group name for key: %@"
+ "[%{public}@] [%{public}@] Simulating NFC tap for %lu setup URL(s)"
+ "[%{public}@] diagnostics transfer completed successfully"
+ "[%{public}@] diagnostics transfer metadata: %{private}@"
+ "[%{public}@] fetchShouldSkipFirmwareUpdateApplyPolicy"
+ "[%{public}@] fetchShouldSkipFirmwareUpdateApplyPolicy: %@"
+ "[%{public}@] fetchShouldSkipFirmwareUpdateApplyPolicy: response payload missing value"
+ "[%{public}@] notifyPostPairingSetupComplete"
+ "[%{public}@] setShouldSkipFirmwareUpdateApplyPolicy: %@"
+ "attemptCount"
+ "availableonAssetServer"
+ "cameraProfileUniqueIdentifier"
+ "colorCode"
+ "currentDiscoverabilityStateDuration"
+ "currentReachabilityStateDuration"
+ "currentSessionStateDuration"
+ "diagnostics transfer completed successfully"
+ "diagnostics transfer metadata: %{private}@"
+ "disableRealCameraContentForDemoV2"
+ "disconnectionErrors"
+ "discoverabilityLosses"
+ "discoverableDuration"
+ "establishmentErrors"
+ "failedCount"
+ "fetchAccessoryHealth"
+ "fetchShouldSkipFirmwareUpdateApplyPolicy"
+ "fetchShouldSkipFirmwareUpdateApplyPolicy: %@"
+ "fetchShouldSkipFirmwareUpdateApplyPolicy: response payload missing value"
+ "hasActiveSession"
+ "hm.hydrateHomeEntitiesRequest"
+ "lastDisconnectionError"
+ "lastEstablishmentError"
+ "no-bundle-id"
+ "notifyPostPairingSetupComplete"
+ "previousResult"
+ "proxPairingCardLaunchSessionID"
+ "proxPairingMetricsSessionID"
+ "reachabilityLosses"
+ "reachableDuration"
+ "setShouldSkipFirmwareUpdateApplyPolicy: %@"
+ "setupURLStrings"
+ "supports3826361c217c"
+ "supportsAudioDestinationMediaSystemVirtualHomePod"
+ "supportsAudioDestinationVirtualHomeTheater"
+ "supportsECDSAKey"
+ "supportsHomeTheaterNaming"
+ "suppressDpsForDemoV2"
+ "thermostatPresetForDemoV2"
+ "user_defined_type"
+ "\xd1"
+ "\xe12"
- "#EXT-X-TARGETDURATION:%u\n"
- "%@%@%@%@%@%@%@%@%@%@"
- "-[HMAccessorySetupManager simulateNFCTapWithSetupURLString:completionHandler:]"
- "-[HMHome(HMAccessory) _removeAccessory:completionHandler:]"
- "-[HMHome(Wallet) fetchWalleKeyExpressEnablementConflictingPassDescription:]"
- "BackingStoreV5Removal"
- "Calibration Status updated to  HMAccessoryCalibrationStatusComplete"
- "Calibration Status updated to  HMAccessoryCalibrationStatusInProgress"
- "Calling completion with cached documentation: %@"
- "Cleared staged destination controller data for identifier: %@"
- "Cleared staged destination for identifier: %@"
- "Cleared staged group for identifier: %@"
- "Configuring with message dispatcher: %@"
- "Failed to update video resoluiton quality: %@"
- "Fetching description of the conflicting pass..."
- "Got error while fetching participant participant: %@"
- "HMASM.mk.nfcSetupURLString"
- "Home did not sync staged data before timeout, firing staging results failure metric"
- "Home synced staged data in %ld ms, firing staging results metric"
- "In didUpdateDocumentationAssetState"
- "Not fetching missing wallet keys for accessory accessory: %@, supportsCHIP: %@, supportsWalletKey: %@"
- "SetupPayload: V1 failed to decode suffix with EUI64: %@"
- "SetupPayload: V1 legacy payload (length %tu)"
- "SetupPayload: V1 parsed - SetupID:%@ PN:%@ PG:%@"
- "SetupPayload: V1 parsed - paired:%d NFC:%d SetupID:%@ PN:%@ PG:%@ DeviceID:%@"
- "SetupPayload: V1 parsed with EUI64 - PN:%@ PG:%@ EUI:%@"
- "SetupPayload: V1 payload too short for EUI64 - expected %tu, got %tu"
- "Staging destination controller data: %@"
- "Staging destinations: %@"
- "Staging groups: %@"
- "Staging removed group identifiers: %@"
- "The  data could not be read from the file."
- "[%{public}@] Calibration Status updated to  HMAccessoryCalibrationStatusComplete"
- "[%{public}@] Calibration Status updated to  HMAccessoryCalibrationStatusInProgress"
- "[%{public}@] Calling completion with cached documentation: %@"
- "[%{public}@] Cleared staged destination controller data for identifier: %@"
- "[%{public}@] Cleared staged destination for identifier: %@"
- "[%{public}@] Cleared staged group for identifier: %@"
- "[%{public}@] Configuring with message dispatcher: %@"
- "[%{public}@] Failed to update video resoluiton quality: %@"
- "[%{public}@] Fetching description of the conflicting pass..."
- "[%{public}@] Home did not sync staged data before timeout, firing staging results failure metric"
- "[%{public}@] Home synced staged data in %ld ms, firing staging results metric"
- "[%{public}@] In didUpdateDocumentationAssetState"
- "[%{public}@] Not fetching missing wallet keys for accessory accessory: %@, supportsCHIP: %@, supportsWalletKey: %@"
- "[%{public}@] SetupPayload: V1 failed to decode suffix with EUI64: %@"
- "[%{public}@] SetupPayload: V1 legacy payload (length %tu)"
- "[%{public}@] SetupPayload: V1 parsed - SetupID:%@ PN:%@ PG:%@"
- "[%{public}@] SetupPayload: V1 parsed - paired:%d NFC:%d SetupID:%@ PN:%@ PG:%@ DeviceID:%@"
- "[%{public}@] SetupPayload: V1 parsed with EUI64 - PN:%@ PG:%@ EUI:%@"
- "[%{public}@] SetupPayload: V1 payload too short for EUI64 - expected %tu, got %tu"
- "[%{public}@] Simulating NFC tap for setup URL: %@"
- "[%{public}@] Staging destination controller data: %@"
- "[%{public}@] Staging destinations: %@"
- "[%{public}@] Staging groups: %@"
- "[%{public}@] Staging removed group identifiers: %@"
- "[%{public}@] [%{public}@] Simulating NFC tap for setup URL: %@"
- "[%{public}@] diagnostics transfer completed successfully with metadata: %@"
- "diagnostics transfer completed successfully with metadata: %@"
- "fetchUpdates(for:)"
- "importCameraRecording(fileURL:zoneName:clipUUIDSuffix:startDate:)"
- "send(_:payload:destination:headers:userInfo:messageUUID:qualityOfService:)"
- "setupURLString"
- "updateLocation(_:source:)"
- "\xd12"
```
