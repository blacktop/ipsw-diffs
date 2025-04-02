## HomeKitMatter

> `/System/Library/PrivateFrameworks/HomeKitMatter.framework/Versions/A/HomeKitMatter`

```diff

-1278.5.13.4.2
-  __TEXT.__text: 0x14c63c
+1278.6.20.0.1
+  __TEXT.__text: 0x14f428
   __TEXT.__auth_stubs: 0x820
-  __TEXT.__objc_methlist: 0x9acc
+  __TEXT.__objc_methlist: 0x9bd4
   __TEXT.__const: 0x150
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__gcc_except_tab: 0x2aa0
-  __TEXT.__cstring: 0x5fbb
-  __TEXT.__oslogstring: 0x236b8
+  __TEXT.__gcc_except_tab: 0x2b60
+  __TEXT.__cstring: 0x6066
+  __TEXT.__oslogstring: 0x23d59
   __TEXT.__ustring: 0x68
-  __TEXT.__unwind_info: 0x2c88
-  __TEXT.__objc_classname: 0x1338
-  __TEXT.__objc_methname: 0x23078
-  __TEXT.__objc_methtype: 0x377b
-  __TEXT.__objc_stubs: 0x148c0
+  __TEXT.__unwind_info: 0x2d08
+  __TEXT.__objc_classname: 0x133c
+  __TEXT.__objc_methname: 0x235c3
+  __TEXT.__objc_methtype: 0x37f0
+  __TEXT.__objc_stubs: 0x14c40
   __DATA_CONST.__got: 0x920
   __DATA_CONST.__const: 0xb10
   __DATA_CONST.__objc_classlist: 0x3e8
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x64a0
+  __DATA_CONST.__objc_selrefs: 0x6580
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x2c8
   __DATA_CONST.__objc_arraydata: 0x220
   __AUTH_CONST.__auth_got: 0x420
-  __AUTH_CONST.__const: 0x4fc0
+  __AUTH_CONST.__const: 0x5200
   __AUTH_CONST.__cfstring: 0x6580
-  __AUTH_CONST.__objc_const: 0xe9e0
+  __AUTH_CONST.__objc_const: 0xea38
   __AUTH_CONST.__objc_intobj: 0x15a8
   __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x2710
-  __DATA.__objc_ivar: 0xa58
+  __DATA.__objc_ivar: 0xa5c
   __DATA.__data: 0xd80
   __DATA.__bss: 0x498
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4116
-  Symbols:   9865
-  CStrings:  8024
+  Functions: 4147
+  Symbols:   9940
+  CStrings:  8085
 
Symbols:
+ -[HMMTRAccessoryServer _notifyDelegateOfAccessoryMatchingCommissioningDiscriminatorDiscovered]
+ -[HMMTRAccessoryServer _notifyDelegateOfMatterAccessoryVendorID:productID:deviceType:]
+ -[HMMTRAccessoryServer _notifyDelegateOfSupportedLinkLayerTypes:]
+ -[HMMTRAccessoryServer accessoryWithSameDiscriminatorDiscovered]
+ -[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]
+ -[HMMTRAccessoryServer currentDeviceTypeFromDCL]
+ -[HMMTRAccessoryServer isLocallyDiscoveredAndMatchesDiscriminatorOfSetupPayload:]
+ -[HMMTRAccessoryServer notifyDelegateOfAccessoryMatchingCommissioningDiscriminatorDiscovered]
+ -[HMMTRAccessoryServerBrowser _cleanUpMTRDevicesWithFabricUUID:]
+ -[HMMTRAccessoryServerBrowser _updatePairingMetricsUponAccessoryDiscovery]
+ -[HMMTRAccessoryServerBrowser announceOtaProviderForNodeID:isRetry:]
+ -[HMMTRAccessoryServerBrowser handleHomeAddedAccessoryWithNodeID:fabricUUID:]
+ -[HMMTRAccessoryServerBrowser handleHomeRemovedAccessoryWithNodeID:fabricUUID:]
+ -[HMMTRAccessoryServerBrowser locallyDiscoveredAccessoryServerMatchesDiscriminatorOfSetupPayload:]
+ -[HMMTRFirmwareUpdateStatus incrementOtaAnnounceDelayCounter]
+ -[HMMTRFirmwareUpdateStatus otaAnnounceDelayCounter]
+ -[HMMTRFirmwareUpdateStatus resetOtaAnnounceDelayCounter]
+ -[HMMTRFirmwareUpdateStatus setOtaAnnounceDelayCounter:]
+ -[HMMTRSoftwareUpdateProvider notifyUpdateRequestedForNodeID:isUserTriggered:isRetry:]
+ -[HMMTRSyncClusterDoorLock fetchAvailableCredentialSlotsWithLimit:forCredentialType:flow:]
+ -[HMMTRSyncClusterDoorLock fetchAvailableUserSlotsWithLimit:flow:]
+ -[HMMTRSyncClusterDoorLock getAllUsersStartingAtSlot:assumingTotalNumberOfSlots:users:temporaryCachedAliroCredentials:flow:]
+ -[HMMTRSyncClusterDoorLock isUserSlotAvailableForUserResponse:]
+ -[HMMTRSyncClusterDoorLock totalNumberOfAliroDeviceKeyCredentialsSupportedWithFlow:]
+ -[HMMTRSyncClusterDoorLock totalNumberOfAliroIssuerKeyCredentialsSupportedWithFlow:]
+ -[HMMTRSyncClusterDoorLock totalNumberOfCredentialSlotsSupportedForCredentialType:flow:]
+ GCC_except_table1016
+ GCC_except_table1087
+ GCC_except_table1134
+ GCC_except_table1138
+ GCC_except_table1145
+ GCC_except_table1177
+ GCC_except_table1203
+ GCC_except_table1211
+ GCC_except_table1248
+ GCC_except_table1285
+ GCC_except_table1504
+ GCC_except_table1545
+ GCC_except_table1695
+ GCC_except_table1696
+ GCC_except_table1717
+ GCC_except_table1718
+ GCC_except_table1719
+ GCC_except_table1720
+ GCC_except_table1721
+ GCC_except_table1724
+ GCC_except_table1727
+ GCC_except_table1728
+ GCC_except_table1729
+ GCC_except_table1730
+ GCC_except_table1731
+ GCC_except_table1732
+ GCC_except_table1733
+ GCC_except_table1792
+ GCC_except_table1800
+ GCC_except_table1877
+ GCC_except_table2000
+ GCC_except_table2027
+ GCC_except_table2060
+ GCC_except_table2070
+ GCC_except_table2072
+ GCC_except_table2121
+ GCC_except_table2170
+ GCC_except_table2238
+ GCC_except_table2488
+ GCC_except_table2494
+ GCC_except_table2543
+ GCC_except_table2553
+ GCC_except_table2586
+ GCC_except_table2624
+ GCC_except_table2626
+ GCC_except_table2671
+ GCC_except_table2672
+ GCC_except_table2673
+ GCC_except_table2674
+ GCC_except_table2675
+ GCC_except_table2676
+ GCC_except_table2677
+ GCC_except_table2691
+ GCC_except_table2725
+ GCC_except_table2731
+ GCC_except_table2744
+ GCC_except_table2747
+ GCC_except_table2751
+ GCC_except_table2763
+ GCC_except_table2767
+ GCC_except_table2769
+ GCC_except_table2788
+ GCC_except_table2794
+ GCC_except_table2801
+ GCC_except_table2814
+ GCC_except_table2867
+ GCC_except_table2868
+ GCC_except_table3228
+ GCC_except_table3230
+ GCC_except_table3233
+ GCC_except_table3239
+ GCC_except_table3242
+ GCC_except_table3256
+ GCC_except_table3272
+ GCC_except_table3333
+ GCC_except_table3334
+ GCC_except_table3359
+ GCC_except_table3360
+ GCC_except_table3396
+ GCC_except_table3404
+ GCC_except_table3423
+ GCC_except_table3426
+ GCC_except_table3464
+ GCC_except_table3468
+ GCC_except_table3484
+ GCC_except_table3486
+ GCC_except_table3509
+ GCC_except_table3569
+ GCC_except_table3613
+ GCC_except_table3630
+ GCC_except_table3656
+ GCC_except_table3662
+ GCC_except_table3677
+ GCC_except_table3678
+ GCC_except_table3683
+ GCC_except_table3690
+ GCC_except_table3730
+ GCC_except_table3750
+ GCC_except_table3803
+ GCC_except_table3808
+ GCC_except_table3811
+ GCC_except_table3889
+ GCC_except_table3890
+ GCC_except_table3947
+ GCC_except_table3950
+ GCC_except_table4064
+ GCC_except_table4069
+ GCC_except_table4075
+ GCC_except_table4079
+ GCC_except_table4103
+ GCC_except_table4126
+ GCC_except_table430
+ GCC_except_table497
+ GCC_except_table664
+ GCC_except_table667
+ GCC_except_table727
+ GCC_except_table728
+ GCC_except_table729
+ GCC_except_table769
+ GCC_except_table834
+ GCC_except_table840
+ GCC_except_table842
+ GCC_except_table844
+ GCC_except_table846
+ GCC_except_table850
+ GCC_except_table854
+ GCC_except_table859
+ GCC_except_table902
+ GCC_except_table908
+ GCC_except_table910
+ OBJC_IVAR_$_HMMTRFirmwareUpdateStatus._otaAnnounceDelayCounter
+ __101-[HMMTRAccessoryServer updateAccessoryControlToIncludeAdministratorNodes:sharedUserNodes:completion:]_block_invoke.881
+ __102-[HMMTRSyncClusterDoorLock updateSchedulesForUserIndex:withWeekDaySchedules:andYearDaySchedules:flow:]_block_invoke.388
+ __105-[HMMTRSyncClusterDoorLock updateSchedulesOfScheduleType:withRequestedSchedules:forUserAtUserIndex:flow:]_block_invoke.471
+ __107-[HMMTRSyncClusterDoorLock setScheduleOfScheduleType:withSchedule:atScheduleIndex:forUserAtUserIndex:flow:]_block_invoke.525
+ __113-[HMMTRAttestationStatus deviceAttestationCompletedForController:opaqueDeviceHandle:attestationDeviceInfo:error:]_block_invoke.12
+ __113-[HMMTRAttestationStatus deviceAttestationCompletedForController:opaqueDeviceHandle:attestationDeviceInfo:error:]_block_invoke.15
+ __113-[HMMTRAttestationStatus deviceAttestationCompletedForController:opaqueDeviceHandle:attestationDeviceInfo:error:]_block_invoke.16
+ __113-[HMMTRAttestationStatus deviceAttestationCompletedForController:opaqueDeviceHandle:attestationDeviceInfo:error:]_block_invoke.23
+ __113-[HMMTRSyncClusterDoorLock findOperationOrderForModifyingWeekDaySchedules:andYearDaySchedules:forUserIndex:flow:]_block_invoke.467
+ __114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke.940
+ __114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke.943
+ __125-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:withWeekDaySchedules:andYearDaySchedules:requireFullScheduleAudit:flow:]_block_invoke.376
+ __125-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:withWeekDaySchedules:andYearDaySchedules:requireFullScheduleAudit:flow:]_block_invoke.377
+ __125-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:withWeekDaySchedules:andYearDaySchedules:requireFullScheduleAudit:flow:]_block_invoke.380
+ __125-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:withWeekDaySchedules:andYearDaySchedules:requireFullScheduleAudit:flow:]_block_invoke.383
+ __37-[HMMTRAccessoryServer finishPairing]_block_invoke.800
+ __39-[HMMTRSyncClusterDoorLock getAllUsers]_block_invoke.370
+ __42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke.270
+ __42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke.275
+ __42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke.279
+ __42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke.289
+ __42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke_2.282
+ __47-[HMMTRAccessoryServer processAttributeReport:]_block_invoke.1024
+ __51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.853
+ __51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.857
+ __51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.860
+ __51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.861
+ __51-[HMMTRAccessoryServer device:receivedEventReport:]_block_invoke.1025
+ __54-[HMMTRSyncClusterDoorLock removePinCodeForUserIndex:]_block_invoke.305
+ __55-[HMMTRAccessoryServer device:receivedAttributeReport:]_block_invoke.1021
+ __58-[HMMTRSyncClusterDoorLock addOrUpdateReaderKeyData:flow:]_block_invoke.325
+ __59-[HMMTRSyncClusterDoorLock readSchedulesForUserIndex:flow:]_block_invoke.389
+ __60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.950
+ __60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.954
+ __60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.959
+ __62-[HMMTRSyncClusterDoorLock readAliroSupportedVersionWithFlow:]_block_invoke.392
+ __62-[HMMTRSyncClusterDoorLock readAliroSupportedVersionWithFlow:]_block_invoke.393
+ __63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.851
+ __63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.852
+ __64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.974
+ __64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.975
+ __64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.976
+ __66-[HMMTRSyncClusterDoorLock fetchAvailableUserSlotsWithLimit:flow:]_block_invoke.449
+ __67-[HMMTRSyncClusterDoorLock _addOrUpdateIssuerKeyData:forUser:flow:]_block_invoke.341
+ __67-[HMMTRSyncClusterDoorLock _addOrUpdateIssuerKeyData:forUser:flow:]_block_invoke.347
+ __67-[HMMTRSyncClusterDoorLock _addOrUpdateIssuerKeyData:forUser:flow:]_block_invoke.350
+ __67-[HMMTRSyncClusterDoorLock _addOrUpdateIssuerKeyData:forUser:flow:]_block_invoke.356
+ __67-[HMMTRSyncClusterDoorLock _addOrUpdateIssuerKeyData:forUser:flow:]_block_invoke_2.351
+ __68-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:userType:flow:]_block_invoke.435
+ __68-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:userType:flow:]_block_invoke.437
+ __69-[HMMTRSyncClusterDoorLock addOrUpdatePinCodeWithValue:forUserIndex:]_block_invoke.295
+ __73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.845
+ __73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.849
+ __73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.850
+ __73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.826
+ __73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.827
+ __73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.838
+ __73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.842
+ __73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.843
+ __74-[HMMTRSyncClusterDoorLock addOrUpdateIssuerKeyData:forUserUniqueID:flow:]_block_invoke.361
+ __74-[HMMTRSyncClusterDoorLock addOrUpdateIssuerKeyData:forUserUniqueID:flow:]_block_invoke.362
+ __74-[HMMTRSyncClusterDoorLock addOrUpdateIssuerKeyData:forUserUniqueID:flow:]_block_invoke.363
+ __75+[HMMTRSyncClusterDoorLock validateFutureResults:ofClass:areNullable:flow:]_block_invoke.422
+ __79-[HMMTRAccessoryServer updateAllCharacteristicValuesPostHAPServiceEnumeration:]_block_invoke.825
+ __79-[HMMTRSyncClusterDoorLock clearAllUsersWithDeletedCreatorFabricIndexWithFlow:]_block_invoke.319
+ __79-[HMMTRSyncClusterDoorLock clearAllUsersWithDeletedCreatorFabricIndexWithFlow:]_block_invoke_2.320
+ __80-[HMMTRSyncClusterDoorLock addDeviceCredentialKeyData:ofType:forUserIndex:flow:]_block_invoke.336
+ __82-[HMMTRAccessoryServer fetchColorControlClusterForHapAccessory:completionHandler:]_block_invoke.960
+ __82-[HMMTRAccessoryServer fetchColorControlClusterForHapAccessory:completionHandler:]_block_invoke.962
+ __83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke.910
+ __83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke.911
+ __83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke.912
+ __83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke.915
+ __83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke.924
+ __83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke.925
+ __83-[HMMTRAccessoryServer updateAccessoryControlToRemoveAdministratorNode:completion:]_block_invoke.884
+ __83-[HMMTRSyncClusterDoorLock addIssuerKeyData:forUserIndex:isUnifiedAccess:withFlow:]_block_invoke.331
+ __84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.926
+ __84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.927
+ __84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.928
+ __84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.935
+ __84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.936
+ __86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.977
+ __86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.978
+ __86-[HMMTRSyncClusterDoorLock addPinCredentialAtIndex:withValue:forUserAtUserIndex:flow:]_block_invoke.502
+ __89-[HMMTRSyncClusterDoorLock updatePinCredentialAtIndex:withValue:forUserAtUserIndex:flow:]_block_invoke.503
+ __90-[HMMTRSyncClusterDoorLock addNewUsersWithUserUniqueIDs:withCorrespondingIssuerKeys:flow:]_block_invoke.242
+ __90-[HMMTRSyncClusterDoorLock addNewUsersWithUserUniqueIDs:withCorrespondingIssuerKeys:flow:]_block_invoke_2.243
+ __90-[HMMTRSyncClusterDoorLock addNewUsersWithUserUniqueIDs:withCorrespondingIssuerKeys:flow:]_block_invoke_3.244
+ __90-[HMMTRSyncClusterDoorLock fetchAvailableCredentialSlotsWithLimit:forCredentialType:flow:]_block_invoke.443
+ __92-[HMMTRAccessoryServer _createFirmwareUpdateServiceWithInstanceID:device:completionHandler:]_block_invoke.815
+ __94-[HMMTRAccessoryServer updateAccessoryControlToAdministratorNodes:sharedUserNodes:completion:]_block_invoke.878
+ __94-[HMMTRSyncClusterDoorLock getScheduleOfScheduleType:atScheduleIndex:forUserAtUserIndex:flow:]_block_invoke.534
+ __94-[HMMTRSyncClusterDoorLock getScheduleOfScheduleType:atScheduleIndex:forUserAtUserIndex:flow:]_block_invoke_2.539
+ __96-[HMMTRSyncClusterDoorLock addCredentialData:forCredentialType:atIndex:forUserAtUserIndex:flow:]_block_invoke.506
+ __96-[HMMTRSyncClusterDoorLock clearScheduleOfScheduleType:atScheduleIndex:forUserAtUserIndex:flow:]_block_invoke.524
+ __99-[HMMTRSyncClusterDoorLock updateCredentialData:forCredentialType:atIndex:forUserAtUserIndex:flow:]_block_invoke.511
+ __Block_byref_object_copy_.10461
+ __Block_byref_object_copy_.11147
+ __Block_byref_object_copy_.11812
+ __Block_byref_object_copy_.12003
+ __Block_byref_object_copy_.1498
+ __Block_byref_object_copy_.2844
+ __Block_byref_object_copy_.2990
+ __Block_byref_object_copy_.3153
+ __Block_byref_object_copy_.4136
+ __Block_byref_object_copy_.5300
+ __Block_byref_object_copy_.6947
+ __Block_byref_object_copy_.7270
+ __Block_byref_object_copy_.7654
+ __Block_byref_object_copy_.8745
+ __Block_byref_object_copy_.9737
+ __Block_byref_object_dispose_.10462
+ __Block_byref_object_dispose_.11148
+ __Block_byref_object_dispose_.11813
+ __Block_byref_object_dispose_.12004
+ __Block_byref_object_dispose_.1499
+ __Block_byref_object_dispose_.2845
+ __Block_byref_object_dispose_.2991
+ __Block_byref_object_dispose_.3154
+ __Block_byref_object_dispose_.4137
+ __Block_byref_object_dispose_.5301
+ __Block_byref_object_dispose_.6948
+ __Block_byref_object_dispose_.7271
+ __Block_byref_object_dispose_.7655
+ __Block_byref_object_dispose_.8746
+ __Block_byref_object_dispose_.9738
+ ___114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke
+ ___114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke_2
+ ___124-[HMMTRSyncClusterDoorLock getAllUsersStartingAtSlot:assumingTotalNumberOfSlots:users:temporaryCachedAliroCredentials:flow:]_block_invoke
+ ___60-[HMMTRAccessoryServerBrowser handleHomeDeletionWithFabric:]_block_invoke_2
+ ___66-[HMMTRSyncClusterDoorLock fetchAvailableUserSlotsWithLimit:flow:]_block_invoke
+ ___66-[HMMTRSyncClusterDoorLock fetchAvailableUserSlotsWithLimit:flow:]_block_invoke_2
+ ___68-[HMMTRAccessoryServerBrowser announceOtaProviderForNodeID:isRetry:]_block_invoke
+ ___77-[HMMTRAccessoryServerBrowser handleHomeAddedAccessoryWithNodeID:fabricUUID:]_block_invoke
+ ___79-[HMMTRAccessoryServerBrowser handleHomeRemovedAccessoryWithNodeID:fabricUUID:]_block_invoke
+ ___84-[HMMTRSyncClusterDoorLock totalNumberOfAliroDeviceKeyCredentialsSupportedWithFlow:]_block_invoke
+ ___84-[HMMTRSyncClusterDoorLock totalNumberOfAliroIssuerKeyCredentialsSupportedWithFlow:]_block_invoke
+ ___86-[HMMTRSoftwareUpdateProvider notifyUpdateRequestedForNodeID:isUserTriggered:isRetry:]_block_invoke
+ ___90-[HMMTRSyncClusterDoorLock addNewUsersWithUserUniqueIDs:withCorrespondingIssuerKeys:flow:]_block_invoke_3
+ ___90-[HMMTRSyncClusterDoorLock fetchAvailableCredentialSlotsWithLimit:forCredentialType:flow:]_block_invoke
+ ___block_descriptor_40_e8_32s_e56_v32?0"MTRDoorLockClusterGetUserResponseParams"8Q16^B24l
+ ___block_descriptor_56_e8_32s40s48bs_e45_v28?0"HMMTRAccessoryServer"8B16"NSError"20l
+ ___block_descriptor_56_e8_32s40s_e45_v28?0"HMMTRAccessoryServer"8B16"NSError"20l
+ ___block_descriptor_57_e8_32s40s48s_e17_v16?0"NSError"8l
+ ___block_descriptor_64_e8_32s40s48bs56w_e20_v20?0B8"NSError"12l
+ ___block_descriptor_64_e8_32s40s48s56s_e43_{_HMFFutureBlockOutcome=q}16?0"NSArray"8l
+ ___block_descriptor_64_e8_32s40s48s_e41_{_HMFFutureBlockOutcome=q}16?0"NSSet"8l
+ ___block_descriptor_64_e8_32s40s48s_e43_{_HMFFutureBlockOutcome=q}16?0"NSArray"8l
+ ___block_descriptor_64_e8_32s40s_e44_{_HMFFutureBlockOutcome=q}16?0"NSNumber"8l
+ ___block_descriptor_65_e8_32s40s48bs56w_e20_v20?0B8"NSError"12l
+ ___block_descriptor_72_e8_32s40s48s56bs64bs_e17_v16?0"NSError"8l
+ ___block_descriptor_72_e8_32s40s48s56bs_e17_v16?0"NSError"8l
+ ___block_descriptor_72_e8_32s40s48s56s64s_e43_{_HMFFutureBlockOutcome=q}16?0"NSArray"8l
+ ___block_descriptor_80_e8_32s40s48s56s64bs72bs_e5_v8?0l
+ ___block_descriptor_80_e8_32s40s48s56s64s72r_e25_v32?0"NSNumber"8Q16^B24l
+ ___block_descriptor_80_e8_32s40s48s_e87_{_HMFFutureBlockOutcome=q}16?0"MTRDoorLockClusterGetCredentialStatusResponseParams"8l
+ ___block_descriptor_88_e8_32s40s48s56s64s72s_e34_{_HMFFutureBlockOutcome=q}16?08l
+ ___copy_helper_block_e8_32s40s48s56s64b72b
+ __block_literal_global.10198
+ __block_literal_global.1033
+ __block_literal_global.1056
+ __block_literal_global.10732
+ __block_literal_global.10967
+ __block_literal_global.11192
+ __block_literal_global.1133
+ __block_literal_global.11335
+ __block_literal_global.11449
+ __block_literal_global.11856
+ __block_literal_global.1343
+ __block_literal_global.1610
+ __block_literal_global.1662
+ __block_literal_global.1709
+ __block_literal_global.1797
+ __block_literal_global.2149
+ __block_literal_global.2293
+ __block_literal_global.2598
+ __block_literal_global.2748
+ __block_literal_global.2777
+ __block_literal_global.281
+ __block_literal_global.285
+ __block_literal_global.2874
+ __block_literal_global.298
+ __block_literal_global.3050
+ __block_literal_global.311
+ __block_literal_global.322
+ __block_literal_global.3238
+ __block_literal_global.3370
+ __block_literal_global.3481
+ __block_literal_global.349
+ __block_literal_global.353
+ __block_literal_global.358
+ __block_literal_global.361
+ __block_literal_global.365
+ __block_literal_global.391
+ __block_literal_global.405
+ __block_literal_global.4232
+ __block_literal_global.426
+ __block_literal_global.430
+ __block_literal_global.4520
+ __block_literal_global.46.9527
+ __block_literal_global.4655
+ __block_literal_global.4757
+ __block_literal_global.480
+ __block_literal_global.5015
+ __block_literal_global.5189
+ __block_literal_global.529
+ __block_literal_global.537
+ __block_literal_global.541
+ __block_literal_global.5429
+ __block_literal_global.544
+ __block_literal_global.549
+ __block_literal_global.5558
+ __block_literal_global.5793
+ __block_literal_global.5827
+ __block_literal_global.5849
+ __block_literal_global.6106
+ __block_literal_global.6118
+ __block_literal_global.6212
+ __block_literal_global.6308
+ __block_literal_global.6403
+ __block_literal_global.6511
+ __block_literal_global.6606
+ __block_literal_global.6702
+ __block_literal_global.682
+ __block_literal_global.6847
+ __block_literal_global.6995
+ __block_literal_global.7102
+ __block_literal_global.7181
+ __block_literal_global.7477
+ __block_literal_global.7666
+ __block_literal_global.780
+ __block_literal_global.7994
+ __block_literal_global.8122
+ __block_literal_global.82.9528
+ __block_literal_global.822
+ __block_literal_global.830
+ __block_literal_global.8769
+ __block_literal_global.9204
+ __block_literal_global.9526
+ __block_literal_global.9604
+ __block_literal_global.964
+ _objc_msgSend$_cleanUpMTRDevicesWithFabricUUID:
+ _objc_msgSend$_notifyDelegateOfAccessoryMatchingCommissioningDiscriminatorDiscovered
+ _objc_msgSend$_notifyDelegateOfMatterAccessoryVendorID:productID:deviceType:
+ _objc_msgSend$_notifyDelegateOfSupportedLinkLayerTypes:
+ _objc_msgSend$_updatePairingMetricsUponAccessoryDiscovery
+ _objc_msgSend$accessoryWithSameDiscriminatorDiscovered
+ _objc_msgSend$announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:
+ _objc_msgSend$announceOtaProviderForNodeID:isRetry:
+ _objc_msgSend$currentDeviceTypeFromDCL
+ _objc_msgSend$fetchAvailableCredentialSlotsWithLimit:forCredentialType:flow:
+ _objc_msgSend$fetchAvailableUserSlotsWithLimit:flow:
+ _objc_msgSend$forgetDeviceWithNodeID:
+ _objc_msgSend$getAllUsersStartingAtSlot:assumingTotalNumberOfSlots:users:temporaryCachedAliroCredentials:flow:
+ _objc_msgSend$hapIPErrorWithCode:marker:
+ _objc_msgSend$incrementOtaAnnounceDelayCounter
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$isLocallyDiscoveredAndMatchesDiscriminatorOfSetupPayload:
+ _objc_msgSend$isUserSlotAvailableForUserResponse:
+ _objc_msgSend$locallyDiscoveredAccessoryServerMatchesDiscriminatorOfSetupPayload:
+ _objc_msgSend$na_safeAddObject:
+ _objc_msgSend$nodesWithStoredData
+ _objc_msgSend$notifyDelegateOfAccessoryMatchingCommissioningDiscriminatorDiscovered
+ _objc_msgSend$notifyMatterAccessoryMatchingCommissioningDiscriminatorDiscovered
+ _objc_msgSend$notifyMatterAccessoryVendorID:productID:deviceType:
+ _objc_msgSend$notifySupportedLinkLayerTypes:
+ _objc_msgSend$numberOfAliroDeviceKeyCredentialsSupportedWithFlow:completion:
+ _objc_msgSend$otaAnnounceDelayCounter
+ _objc_msgSend$resetOtaAnnounceDelayCounter
+ _objc_msgSend$setOtaAnnounceDelayCounter:
+ _objc_msgSend$totalNumberOfAliroDeviceKeyCredentialsSupportedWithFlow:
+ _objc_msgSend$totalNumberOfAliroIssuerKeyCredentialsSupportedWithFlow:
+ _objc_msgSend$totalNumberOfCredentialSlotsSupportedForCredentialType:flow:
+ logCategory._hmf_once_t0.1661
+ logCategory._hmf_once_t0.2747
+ logCategory._hmf_once_t0.5188
+ logCategory._hmf_once_t0.5826
+ logCategory._hmf_once_t1.4654
+ logCategory._hmf_once_t10.6994
+ logCategory._hmf_once_t13.2873
+ logCategory._hmf_once_t13.3237
+ logCategory._hmf_once_t2.4756
+ logCategory._hmf_once_t2.5792
+ logCategory._hmf_once_t2.6846
+ logCategory._hmf_once_t2.9603
+ logCategory._hmf_once_t20.11334
+ logCategory._hmf_once_t22.6211
+ logCategory._hmf_once_t22.6307
+ logCategory._hmf_once_t22.6605
+ logCategory._hmf_once_t22.6701
+ logCategory._hmf_once_t22.7993
+ logCategory._hmf_once_t273
+ logCategory._hmf_once_t3.1055
+ logCategory._hmf_once_t349
+ logCategory._hmf_once_t4.3369
+ logCategory._hmf_once_t4.7101
+ logCategory._hmf_once_t40.7665
+ logCategory._hmf_once_t571
+ logCategory._hmf_once_t6.1708
+ logCategory._hmf_once_t6.1796
+ logCategory._hmf_once_t8.10966
+ logCategory._hmf_once_t9.5557
+ logCategory._hmf_once_v1.1663
+ logCategory._hmf_once_v1.2749
+ logCategory._hmf_once_v1.5190
+ logCategory._hmf_once_v1.5828
+ logCategory._hmf_once_v10.5559
+ logCategory._hmf_once_v11.6996
+ logCategory._hmf_once_v14.2875
+ logCategory._hmf_once_v14.3239
+ logCategory._hmf_once_v2.4656
+ logCategory._hmf_once_v21.11336
+ logCategory._hmf_once_v23.6213
+ logCategory._hmf_once_v23.6309
+ logCategory._hmf_once_v23.6607
+ logCategory._hmf_once_v23.6703
+ logCategory._hmf_once_v23.7995
+ logCategory._hmf_once_v274
+ logCategory._hmf_once_v3.4758
+ logCategory._hmf_once_v3.5794
+ logCategory._hmf_once_v3.6848
+ logCategory._hmf_once_v3.9605
+ logCategory._hmf_once_v350
+ logCategory._hmf_once_v4.1057
+ logCategory._hmf_once_v41.7667
+ logCategory._hmf_once_v5.3371
+ logCategory._hmf_once_v5.7103
+ logCategory._hmf_once_v572
+ logCategory._hmf_once_v7.1710
+ logCategory._hmf_once_v7.1798
+ logCategory._hmf_once_v9.10968
- -[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:completionHandler:]
- -[HMMTRAccessoryServerBrowser announceOtaProviderForNodeID:]
- -[HMMTRAccessoryServerBrowser handleHomeAddedAccessoryWithNodeID:fabric:]
- -[HMMTRAccessoryServerBrowser handleHomeRemovedAccessoryWithNodeID:]
- -[HMMTRSoftwareUpdateProvider notifyUpdateRequestedForNodeID:isUserTriggered:]
- -[HMMTRSyncClusterDoorLock addNewUsersWithUserUniqueIDs:withCorrespondingIssuerKeys:withIncrementor:forCredentialSlot:flow:]
- GCC_except_table1066
- GCC_except_table1113
- GCC_except_table1117
- GCC_except_table1124
- GCC_except_table1158
- GCC_except_table1184
- GCC_except_table1192
- GCC_except_table1229
- GCC_except_table1266
- GCC_except_table1485
- GCC_except_table1526
- GCC_except_table1676
- GCC_except_table1677
- GCC_except_table1679
- GCC_except_table1699
- GCC_except_table1700
- GCC_except_table1701
- GCC_except_table1702
- GCC_except_table1705
- GCC_except_table1708
- GCC_except_table1709
- GCC_except_table1710
- GCC_except_table1711
- GCC_except_table1712
- GCC_except_table1713
- GCC_except_table1714
- GCC_except_table1773
- GCC_except_table1781
- GCC_except_table1858
- GCC_except_table1981
- GCC_except_table2008
- GCC_except_table2041
- GCC_except_table2051
- GCC_except_table2053
- GCC_except_table2102
- GCC_except_table2151
- GCC_except_table2219
- GCC_except_table2469
- GCC_except_table2475
- GCC_except_table2523
- GCC_except_table2533
- GCC_except_table2566
- GCC_except_table2604
- GCC_except_table2606
- GCC_except_table2629
- GCC_except_table2630
- GCC_except_table2631
- GCC_except_table2649
- GCC_except_table2653
- GCC_except_table2654
- GCC_except_table2655
- GCC_except_table2656
- GCC_except_table2668
- GCC_except_table2704
- GCC_except_table2723
- GCC_except_table2726
- GCC_except_table2730
- GCC_except_table2742
- GCC_except_table2746
- GCC_except_table2748
- GCC_except_table2765
- GCC_except_table2771
- GCC_except_table2778
- GCC_except_table2791
- GCC_except_table2844
- GCC_except_table2845
- GCC_except_table3201
- GCC_except_table3202
- GCC_except_table3203
- GCC_except_table3206
- GCC_except_table3212
- GCC_except_table3215
- GCC_except_table3245
- GCC_except_table3304
- GCC_except_table3305
- GCC_except_table3330
- GCC_except_table3331
- GCC_except_table3367
- GCC_except_table3375
- GCC_except_table3394
- GCC_except_table3397
- GCC_except_table3435
- GCC_except_table3439
- GCC_except_table3455
- GCC_except_table3457
- GCC_except_table3480
- GCC_except_table3540
- GCC_except_table3584
- GCC_except_table3601
- GCC_except_table3627
- GCC_except_table3633
- GCC_except_table3648
- GCC_except_table3649
- GCC_except_table3654
- GCC_except_table3661
- GCC_except_table3700
- GCC_except_table3720
- GCC_except_table3773
- GCC_except_table3778
- GCC_except_table3781
- GCC_except_table3916
- GCC_except_table3919
- GCC_except_table4033
- GCC_except_table4038
- GCC_except_table4044
- GCC_except_table4048
- GCC_except_table4072
- GCC_except_table4095
- GCC_except_table480
- GCC_except_table647
- GCC_except_table650
- GCC_except_table710
- GCC_except_table711
- GCC_except_table712
- GCC_except_table752
- GCC_except_table813
- GCC_except_table819
- GCC_except_table821
- GCC_except_table823
- GCC_except_table825
- GCC_except_table829
- GCC_except_table833
- GCC_except_table838
- GCC_except_table881
- GCC_except_table887
- GCC_except_table889
- GCC_except_table995
- __101-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:completionHandler:]_block_invoke.934
- __101-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:completionHandler:]_block_invoke.937
- __101-[HMMTRAccessoryServer updateAccessoryControlToIncludeAdministratorNodes:sharedUserNodes:completion:]_block_invoke.875
- __102-[HMMTRSyncClusterDoorLock updateSchedulesForUserIndex:withWeekDaySchedules:andYearDaySchedules:flow:]_block_invoke.379
- __105-[HMMTRSyncClusterDoorLock updateSchedulesOfScheduleType:withRequestedSchedules:forUserAtUserIndex:flow:]_block_invoke.455
- __107-[HMMTRSyncClusterDoorLock setScheduleOfScheduleType:withSchedule:atScheduleIndex:forUserAtUserIndex:flow:]_block_invoke.508
- __113-[HMMTRAttestationStatus deviceAttestationCompletedForController:opaqueDeviceHandle:attestationDeviceInfo:error:]_block_invoke.11
- __113-[HMMTRAttestationStatus deviceAttestationCompletedForController:opaqueDeviceHandle:attestationDeviceInfo:error:]_block_invoke.14
- __113-[HMMTRAttestationStatus deviceAttestationCompletedForController:opaqueDeviceHandle:attestationDeviceInfo:error:]_block_invoke.18
- __113-[HMMTRAttestationStatus deviceAttestationCompletedForController:opaqueDeviceHandle:attestationDeviceInfo:error:]_block_invoke.22
- __113-[HMMTRSyncClusterDoorLock findOperationOrderForModifyingWeekDaySchedules:andYearDaySchedules:forUserIndex:flow:]_block_invoke.451
- __124-[HMMTRSyncClusterDoorLock addNewUsersWithUserUniqueIDs:withCorrespondingIssuerKeys:withIncrementor:forCredentialSlot:flow:]_block_invoke.422
- __125-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:withWeekDaySchedules:andYearDaySchedules:requireFullScheduleAudit:flow:]_block_invoke.366
- __125-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:withWeekDaySchedules:andYearDaySchedules:requireFullScheduleAudit:flow:]_block_invoke.367
- __125-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:withWeekDaySchedules:andYearDaySchedules:requireFullScheduleAudit:flow:]_block_invoke.371
- __125-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:withWeekDaySchedules:andYearDaySchedules:requireFullScheduleAudit:flow:]_block_invoke.374
- __37-[HMMTRAccessoryServer finishPairing]_block_invoke.794
- __39-[HMMTRSyncClusterDoorLock getAllUsers]_block_invoke.360
- __42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke.256
- __42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke.264
- __42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke.268
- __42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke.278
- __42-[HMMTRSyncClusterDoorLock getAllPinCodes]_block_invoke_2.271
- __47-[HMMTRAccessoryServer processAttributeReport:]_block_invoke.1016
- __51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.847
- __51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.851
- __51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.854
- __51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.855
- __51-[HMMTRAccessoryServer device:receivedEventReport:]_block_invoke.1017
- __54-[HMMTRSyncClusterDoorLock removePinCodeForUserIndex:]_block_invoke.295
- __55-[HMMTRAccessoryServer device:receivedAttributeReport:]_block_invoke.1013
- __58-[HMMTRSyncClusterDoorLock addOrUpdateReaderKeyData:flow:]_block_invoke.315
- __59-[HMMTRSyncClusterDoorLock readSchedulesForUserIndex:flow:]_block_invoke.380
- __60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.938
- __60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.942
- __60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.951
- __62-[HMMTRSyncClusterDoorLock readAliroSupportedVersionWithFlow:]_block_invoke.383
- __62-[HMMTRSyncClusterDoorLock readAliroSupportedVersionWithFlow:]_block_invoke.384
- __63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.845
- __63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.846
- __64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.966
- __64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.967
- __64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.968
- __67-[HMMTRSyncClusterDoorLock _addOrUpdateIssuerKeyData:forUser:flow:]_block_invoke.331
- __67-[HMMTRSyncClusterDoorLock _addOrUpdateIssuerKeyData:forUser:flow:]_block_invoke.337
- __67-[HMMTRSyncClusterDoorLock _addOrUpdateIssuerKeyData:forUser:flow:]_block_invoke.340
- __67-[HMMTRSyncClusterDoorLock _addOrUpdateIssuerKeyData:forUser:flow:]_block_invoke.346
- __67-[HMMTRSyncClusterDoorLock _addOrUpdateIssuerKeyData:forUser:flow:]_block_invoke_2.341
- __68-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:userType:flow:]_block_invoke.430
- __68-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:userType:flow:]_block_invoke.432
- __69-[HMMTRSyncClusterDoorLock addOrUpdatePinCodeWithValue:forUserIndex:]_block_invoke.284
- __73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.838
- __73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.839
- __73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.843
- __73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.820
- __73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.821
- __73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.831
- __73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.832
- __73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.836
- __74-[HMMTRSyncClusterDoorLock addOrUpdateIssuerKeyData:forUserUniqueID:flow:]_block_invoke.353
- __74-[HMMTRSyncClusterDoorLock addOrUpdateIssuerKeyData:forUserUniqueID:flow:]_block_invoke.354
- __74-[HMMTRSyncClusterDoorLock addOrUpdateIssuerKeyData:forUserUniqueID:flow:]_block_invoke.355
- __75+[HMMTRSyncClusterDoorLock validateFutureResults:ofClass:areNullable:flow:]_block_invoke.413
- __79-[HMMTRAccessoryServer updateAllCharacteristicValuesPostHAPServiceEnumeration:]_block_invoke.819
- __79-[HMMTRSyncClusterDoorLock clearAllUsersWithDeletedCreatorFabricIndexWithFlow:]_block_invoke.309
- __79-[HMMTRSyncClusterDoorLock clearAllUsersWithDeletedCreatorFabricIndexWithFlow:]_block_invoke_2.310
- __80-[HMMTRSyncClusterDoorLock addDeviceCredentialKeyData:ofType:forUserIndex:flow:]_block_invoke.326
- __82-[HMMTRAccessoryServer fetchColorControlClusterForHapAccessory:completionHandler:]_block_invoke.952
- __82-[HMMTRAccessoryServer fetchColorControlClusterForHapAccessory:completionHandler:]_block_invoke.954
- __83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke.904
- __83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke.905
- __83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke.906
- __83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke.909
- __83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke.918
- __83-[HMMTRAccessoryServer generateStateCaptureInformationForReason:completionHandler:]_block_invoke.919
- __83-[HMMTRAccessoryServer updateAccessoryControlToRemoveAdministratorNode:completion:]_block_invoke.878
- __83-[HMMTRSyncClusterDoorLock addIssuerKeyData:forUserIndex:isUnifiedAccess:withFlow:]_block_invoke.321
- __84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.920
- __84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.921
- __84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.922
- __84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.923
- __84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.930
- __86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.969
- __86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.970
- __86-[HMMTRSyncClusterDoorLock addPinCredentialAtIndex:withValue:forUserAtUserIndex:flow:]_block_invoke.487
- __89-[HMMTRSyncClusterDoorLock updatePinCredentialAtIndex:withValue:forUserAtUserIndex:flow:]_block_invoke.488
- __90-[HMMTRSyncClusterDoorLock addNewUsersWithUserUniqueIDs:withCorrespondingIssuerKeys:flow:]_block_invoke.420
- __90-[HMMTRSyncClusterDoorLock addNewUsersWithUserUniqueIDs:withCorrespondingIssuerKeys:flow:]_block_invoke.421
- __92-[HMMTRAccessoryServer _createFirmwareUpdateServiceWithInstanceID:device:completionHandler:]_block_invoke.809
- __94-[HMMTRAccessoryServer updateAccessoryControlToAdministratorNodes:sharedUserNodes:completion:]_block_invoke.872
- __94-[HMMTRSyncClusterDoorLock getScheduleOfScheduleType:atScheduleIndex:forUserAtUserIndex:flow:]_block_invoke.517
- __94-[HMMTRSyncClusterDoorLock getScheduleOfScheduleType:atScheduleIndex:forUserAtUserIndex:flow:]_block_invoke_2.522
- __96-[HMMTRSyncClusterDoorLock addCredentialData:forCredentialType:atIndex:forUserAtUserIndex:flow:]_block_invoke.491
- __96-[HMMTRSyncClusterDoorLock clearScheduleOfScheduleType:atScheduleIndex:forUserAtUserIndex:flow:]_block_invoke.507
- __99-[HMMTRSyncClusterDoorLock updateCredentialData:forCredentialType:atIndex:forUserAtUserIndex:flow:]_block_invoke.496
- __Block_byref_object_copy_.10413
- __Block_byref_object_copy_.11088
- __Block_byref_object_copy_.11753
- __Block_byref_object_copy_.11944
- __Block_byref_object_copy_.2826
- __Block_byref_object_copy_.2968
- __Block_byref_object_copy_.3131
- __Block_byref_object_copy_.4116
- __Block_byref_object_copy_.5280
- __Block_byref_object_copy_.6927
- __Block_byref_object_copy_.7249
- __Block_byref_object_copy_.7632
- __Block_byref_object_copy_.8710
- __Block_byref_object_copy_.9694
- __Block_byref_object_dispose_.10414
- __Block_byref_object_dispose_.11089
- __Block_byref_object_dispose_.11754
- __Block_byref_object_dispose_.11945
- __Block_byref_object_dispose_.2827
- __Block_byref_object_dispose_.2969
- __Block_byref_object_dispose_.3132
- __Block_byref_object_dispose_.4117
- __Block_byref_object_dispose_.5281
- __Block_byref_object_dispose_.6928
- __Block_byref_object_dispose_.7250
- __Block_byref_object_dispose_.7633
- __Block_byref_object_dispose_.8711
- __Block_byref_object_dispose_.9695
- ___101-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:completionHandler:]_block_invoke
- ___101-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:completionHandler:]_block_invoke_2
- ___124-[HMMTRSyncClusterDoorLock addNewUsersWithUserUniqueIDs:withCorrespondingIssuerKeys:withIncrementor:forCredentialSlot:flow:]_block_invoke
- ___60-[HMMTRAccessoryServerBrowser announceOtaProviderForNodeID:]_block_invoke
- ___68-[HMMTRAccessoryServerBrowser handleHomeRemovedAccessoryWithNodeID:]_block_invoke
- ___73-[HMMTRAccessoryServerBrowser handleHomeAddedAccessoryWithNodeID:fabric:]_block_invoke
- ___78-[HMMTRSoftwareUpdateProvider notifyUpdateRequestedForNodeID:isUserTriggered:]_block_invoke
- ___92-[HMMTRSyncClusterDoorLock getAllUsersStartingAtSlot:assumingTotalNumberOfSlots:users:flow:]_block_invoke
- ___block_descriptor_56_e8_32s40s_e20_v20?0B8"NSError"12l
- ___block_descriptor_57_e8_32s40s48bs_e20_v20?0B8"NSError"12l
- ___block_descriptor_72_e8_32s40s48s56bs64bs_e5_v8?0l
- ___block_descriptor_72_e8_32s40s48s56s_e81_{_HMFFutureBlockOutcome=q}16?0"MTRDoorLockClusterSetCredentialResponseParams"8l
- ___block_descriptor_80_e8_32s40s48s56s64s_e87_{_HMFFutureBlockOutcome=q}16?0"MTRDoorLockClusterGetCredentialStatusResponseParams"8l
- __block_literal_global.10152
- __block_literal_global.1025
- __block_literal_global.1058
- __block_literal_global.10683
- __block_literal_global.10908
- __block_literal_global.11133
- __block_literal_global.11276
- __block_literal_global.1135
- __block_literal_global.11390
- __block_literal_global.11797
- __block_literal_global.1336
- __block_literal_global.1596
- __block_literal_global.1648
- __block_literal_global.1695
- __block_literal_global.1783
- __block_literal_global.2132
- __block_literal_global.2276
- __block_literal_global.2580
- __block_literal_global.270.10518
- __block_literal_global.2730
- __block_literal_global.274
- __block_literal_global.2759
- __block_literal_global.2854
- __block_literal_global.288
- __block_literal_global.301
- __block_literal_global.3028
- __block_literal_global.312
- __block_literal_global.3217
- __block_literal_global.333
- __block_literal_global.3349
- __block_literal_global.339
- __block_literal_global.3460
- __block_literal_global.348
- __block_literal_global.357
- __block_literal_global.362
- __block_literal_global.382
- __block_literal_global.396
- __block_literal_global.410
- __block_literal_global.417
- __block_literal_global.4212
- __block_literal_global.4500
- __block_literal_global.46.9494
- __block_literal_global.4635
- __block_literal_global.464
- __block_literal_global.4737
- __block_literal_global.4995
- __block_literal_global.512
- __block_literal_global.5169
- __block_literal_global.520
- __block_literal_global.524
- __block_literal_global.527
- __block_literal_global.532.9857
- __block_literal_global.5409
- __block_literal_global.5538
- __block_literal_global.5773
- __block_literal_global.5807
- __block_literal_global.5829
- __block_literal_global.6086
- __block_literal_global.6098
- __block_literal_global.6192
- __block_literal_global.6288
- __block_literal_global.6383
- __block_literal_global.6491
- __block_literal_global.6586
- __block_literal_global.6682
- __block_literal_global.6827
- __block_literal_global.686
- __block_literal_global.6975
- __block_literal_global.7082
- __block_literal_global.7161
- __block_literal_global.7455
- __block_literal_global.7644
- __block_literal_global.782
- __block_literal_global.7972
- __block_literal_global.8100
- __block_literal_global.816
- __block_literal_global.82.9495
- __block_literal_global.824
- __block_literal_global.8734
- __block_literal_global.9170
- __block_literal_global.9493
- __block_literal_global.9571
- __block_literal_global.966
- _objc_msgSend$addNewUsersWithUserUniqueIDs:withCorrespondingIssuerKeys:withIncrementor:forCredentialSlot:flow:
- _objc_msgSend$announceOtaProvider:providerEndpoint:immediateAnnouncement:completionHandler:
- _objc_msgSend$announceOtaProviderForNodeID:
- _objc_msgSend$updateUserUniqueIDForUserIndex:userUniqueID:flow:
- logCategory._hmf_once_t0.1647
- logCategory._hmf_once_t0.2729
- logCategory._hmf_once_t0.5168
- logCategory._hmf_once_t0.5806
- logCategory._hmf_once_t1.4634
- logCategory._hmf_once_t10.6974
- logCategory._hmf_once_t13.2853
- logCategory._hmf_once_t13.3216
- logCategory._hmf_once_t2.4736
- logCategory._hmf_once_t2.5772
- logCategory._hmf_once_t2.6826
- logCategory._hmf_once_t2.9570
- logCategory._hmf_once_t20.11275
- logCategory._hmf_once_t22.6191
- logCategory._hmf_once_t22.6287
- logCategory._hmf_once_t22.6585
- logCategory._hmf_once_t22.6681
- logCategory._hmf_once_t22.7971
- logCategory._hmf_once_t265
- logCategory._hmf_once_t3.1057
- logCategory._hmf_once_t346
- logCategory._hmf_once_t4.3348
- logCategory._hmf_once_t4.7081
- logCategory._hmf_once_t40.7643
- logCategory._hmf_once_t560
- logCategory._hmf_once_t6.1694
- logCategory._hmf_once_t6.1782
- logCategory._hmf_once_t8.10907
- logCategory._hmf_once_t9.5537
- logCategory._hmf_once_v1.1649
- logCategory._hmf_once_v1.2731
- logCategory._hmf_once_v1.5170
- logCategory._hmf_once_v1.5808
- logCategory._hmf_once_v10.5539
- logCategory._hmf_once_v11.6976
- logCategory._hmf_once_v14.2855
- logCategory._hmf_once_v14.3218
- logCategory._hmf_once_v2.4636
- logCategory._hmf_once_v21.11277
- logCategory._hmf_once_v23.6193
- logCategory._hmf_once_v23.6289
- logCategory._hmf_once_v23.6587
- logCategory._hmf_once_v23.6683
- logCategory._hmf_once_v23.7973
- logCategory._hmf_once_v266
- logCategory._hmf_once_v3.4738
- logCategory._hmf_once_v3.5774
- logCategory._hmf_once_v3.6828
- logCategory._hmf_once_v3.9572
- logCategory._hmf_once_v347
- logCategory._hmf_once_v4.1059
- logCategory._hmf_once_v41.7645
- logCategory._hmf_once_v5.3350
- logCategory._hmf_once_v5.7083
- logCategory._hmf_once_v561
- logCategory._hmf_once_v7.1696
- logCategory._hmf_once_v7.1784
- logCategory._hmf_once_v9.10909
CStrings:
+ "\x02\x12"
+ "\x11A"
+ "\"\x11\x11"
+ "%{public}@Accessory server already purged by the time user responded"
+ "%{public}@Accessory server purged by the time user responded"
+ "%{public}@Accessory server was purged by the time device attestation completed"
+ "%{public}@Cleaning up stale MTRDevices"
+ "%{public}@Locally discovered server %@ matches the discriminator %@ (short %@)"
+ "%{public}@Notifying delegate of accessory vendor ID %@, product ID %@, device type %@"
+ "%{public}@Notifying matter accessory matching commissioning discriminator discovered"
+ "%{public}@Notifying supported link layer types: %@"
+ "%{public}@Removing unpaired node %@ from fabric %@ controller %@"
+ "%{public}@[Flow: %@] Credential exists at slot %ld for credentialType %ld"
+ "%{public}@[Flow: %@] Exhausted full occupied user sweep: %@"
+ "%{public}@[Flow: %@] Exhausted search for occupied credentials with result %@"
+ "%{public}@[Flow: %@] No user uniqueIDS and corresponding issuer keys to add"
+ "%{public}@[Flow: %@] Number of users with credentials: %ld are more than what is available on the lock: %lu"
+ "%{public}@[Flow: %@] Number of users with credentials: %ld are more than what the lock supports: %@"
+ "%{public}@[Flow: %@] Number of users: %ld are more than what the lock supports: %@"
+ "%{public}@[Flow: %@] Number of users: %ld are more than what the lock supports: %lu"
+ "%{public}@[Flow: %@] availableUserSlots: %@ | availableCredentialSlots %@"
+ "%{public}@[Flow: %@] findAllOccupiedCredentialSlotsForCredentialType: %ld startingAtSlot: %ld assumingTotalNumberOfSlots: %ld"
+ "%{public}@accessoryWithSameDiscriminatorDiscovered -> NO as setupPayload is missing"
+ "%{public}@accessoryWithSameDiscriminatorDiscovered -> YES as server was locally discovered"
+ "%{public}@announceOtaProvider for %@, immediateAnnouncement: %@, delayCounter: %lu"
+ "%{public}@isLocallyDiscoveredAndMatchesDiscriminatorOfSetupPayload compares short discriminator %@ against its own %@"
+ "%{public}@isLocallyDiscoveredAndMatchesDiscriminatorOfSetupPayload failed to match discriminator %@ against its own %@"
+ "%{public}@isLocallyDiscoveredAndMatchesDiscriminatorOfSetupPayload matched discriminator %@ against server's own"
+ "@56@0:8q16q24@32@40@48"
+ "@56@0:8q16q24q32@40@48"
+ "T@\"HMMTRAccessoryServer\",W,N,V_accessoryServer"
+ "TB,R,D,N"
+ "TQ,N,V_otaAnnounceDelayCounter"
+ "_cleanUpMTRDevicesWithFabricUUID:"
+ "_notifyDelegateOfAccessoryMatchingCommissioningDiscriminatorDiscovered"
+ "_notifyDelegateOfMatterAccessoryVendorID:productID:deviceType:"
+ "_notifyDelegateOfSupportedLinkLayerTypes:"
+ "_otaAnnounceDelayCounter"
+ "_updatePairingMetricsUponAccessoryDiscovery"
+ "accessoryWithSameDiscriminatorDiscovered"
+ "announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:"
+ "announceOtaProviderForNodeID:isRetry:"
+ "currentDeviceTypeFromDCL"
+ "fetchAvailableCredentialSlotsWithLimit:forCredentialType:flow:"
+ "fetchAvailableUserSlotsWithLimit:flow:"
+ "forgetDeviceWithNodeID:"
+ "getAllUsersStartingAtSlot:assumingTotalNumberOfSlots:users:temporaryCachedAliroCredentials:flow:"
+ "handleHomeAddedAccessoryWithNodeID:fabricUUID:"
+ "handleHomeRemovedAccessoryWithNodeID:fabricUUID:"
+ "hapIPErrorWithCode:marker:"
+ "incrementOtaAnnounceDelayCounter"
+ "initWithCapacity:"
+ "isLocallyDiscoveredAndMatchesDiscriminatorOfSetupPayload:"
+ "isUserSlotAvailableForUserResponse:"
+ "locallyDiscoveredAccessoryServerMatchesDiscriminatorOfSetupPayload:"
+ "na_safeAddObject:"
+ "nodesWithStoredData"
+ "notifyDelegateOfAccessoryMatchingCommissioningDiscriminatorDiscovered"
+ "notifyMatterAccessoryMatchingCommissioningDiscriminatorDiscovered"
+ "notifyMatterAccessoryVendorID:productID:deviceType:"
+ "notifySupportedLinkLayerTypes:"
+ "notifyUpdateRequestedForNodeID:isUserTriggered:isRetry:"
+ "otaAnnounceDelayCounter"
+ "resetOtaAnnounceDelayCounter"
+ "setOtaAnnounceDelayCounter:"
+ "totalNumberOfAliroDeviceKeyCredentialsSupportedWithFlow:"
+ "totalNumberOfAliroIssuerKeyCredentialsSupportedWithFlow:"
+ "totalNumberOfCredentialSlotsSupportedForCredentialType:flow:"
+ "v24@0:8@\"NSNumber\"16"
+ "v28@?0@\"HMMTRAccessoryServer\"8B16@\"NSError\"20"
+ "v32@?0@\"MTRDoorLockClusterGetUserResponseParams\"8Q16^B24"
+ "v32@?0@\"NSNumber\"8Q16^B24"
+ "v40@0:8@\"NSNumber\"16@\"NSNumber\"24@\"NSNumber\"32"
+ "v52@0:8@16@24B32q36@?44"
+ "{_HMFFutureBlockOutcome=q@}16@?0@\"NSSet\"8"
- "\x111"
- "#\x11"
- "%{public}@[Flow: %@] Adding issuerKey: %@ to userUniqueID: %@ toCredentialSlot: %ld"
- "%{public}@[Flow: %@] Credential slot resources have been exhausted"
- "%{public}@[Flow: %@] Error while reading number of aliro issuer key credentials supported: %@"
- "%{public}@[Flow: %@] userIndex is nil when trying to add credential to new user. Possible firmware issue."
- "%{public}@announceOtaProvider for %@"
- "addNewUsersWithUserUniqueIDs:withCorrespondingIssuerKeys:withIncrementor:forCredentialSlot:flow:"
- "announceOtaProvider:providerEndpoint:immediateAnnouncement:completionHandler:"
- "announceOtaProviderForNodeID:"
- "handleHomeAddedAccessoryWithNodeID:fabric:"
- "handleHomeRemovedAccessoryWithNodeID:"
- "notifyUpdateRequestedForNodeID:isUserTriggered:"
- "v44@0:8@16@24B32@?36"

```
