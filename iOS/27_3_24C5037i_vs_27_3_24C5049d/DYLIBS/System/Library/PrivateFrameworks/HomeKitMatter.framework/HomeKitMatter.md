## HomeKitMatter

> `/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter`

```diff

-1535.0.0.0.2
-  __TEXT.__text: 0x18a3c0
-  __TEXT.__objc_methlist: 0xb15c
+1535.3.8.0.0
+  __TEXT.__text: 0x18dee8
+  __TEXT.__objc_methlist: 0xb2d4
   __TEXT.__const: 0x2a8
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__gcc_except_tab: 0x3414
-  __TEXT.__cstring: 0x733f
-  __TEXT.__oslogstring: 0x51e35
+  __TEXT.__gcc_except_tab: 0x33e0
+  __TEXT.__cstring: 0x73ea
+  __TEXT.__oslogstring: 0x52f23
   __TEXT.__ustring: 0x68
-  __TEXT.__unwind_info: 0x3ea0
+  __TEXT.__unwind_info: 0x3f60
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4bc8
+  __DATA_CONST.__const: 0x4d80
   __DATA_CONST.__objc_classlist: 0x460
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x73c8
+  __DATA_CONST.__objc_selrefs: 0x74d8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x318
-  __DATA_CONST.__objc_arraydata: 0x250
-  __DATA_CONST.__got: 0xa40
-  __AUTH_CONST.__const: 0x1240
-  __AUTH_CONST.__cfstring: 0x70c0
-  __AUTH_CONST.__objc_const: 0x10788
-  __AUTH_CONST.__objc_intobj: 0x1830
-  __AUTH_CONST.__objc_arrayobj: 0x198
+  __DATA_CONST.__objc_arraydata: 0x260
+  __DATA_CONST.__got: 0xa50
+  __AUTH_CONST.__const: 0x11c0
+  __AUTH_CONST.__cfstring: 0x71a0
+  __AUTH_CONST.__objc_const: 0x10878
+  __AUTH_CONST.__objc_intobj: 0x1908
+  __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1ea0
-  __DATA.__objc_ivar: 0xbc4
+  __DATA.__objc_ivar: 0xbd8
   __DATA.__data: 0xea0
   __DATA_DIRTY.__objc_data: 0xd20
-  __DATA_DIRTY.__bss: 0xb0
+  __DATA_DIRTY.__bss: 0xa0
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/UARPKit.framework/UARPKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4618
-  Symbols:   7543
-  CStrings:  5959
+  Functions: 4680
+  Symbols:   7630
+  CStrings:  6015
 
Symbols:
+ -[HMMTRAccessoryServer _handleAppleLockDoorPositionDetectionEnabledReport:]
+ -[HMMTRAccessoryServer _resumeDayOneFwUpdateIfReadyWithTrigger:]
+ -[HMMTRAccessoryServer dayOneFwUpdateFlagDidClear]
+ -[HMMTRAccessoryServer dayOneResumePending]
+ -[HMMTRAccessoryServer requestDayOneFwUpdateResume]
+ -[HMMTRAccessoryServer setDayOneResumePending:]
+ -[HMMTRAccessoryServerBrowser updateOTAProviderForServer:]
+ -[HMMTRDescriptorClusterManager _isDoorPositionDetectionDisabledForDoorLockAtCHIPEndpoint:device:]
+ -[HMMTRDoorLockClusterAPIRouter appendAliroCredentialsToUsers:flow:completion:]
+ -[HMMTRDoorLockClusterAPIRouter findEvictableEndpointKeyIndexForUserIndex:flow:completion:]
+ -[HMMTRDoorLockClusterAPIRouter getAppleAliroCredentialsWithCredentialType:flow:]
+ -[HMMTRDoorLockClusterAPIRouter getUserWithParams:flow:completion:]
+ -[HMMTRDoorLockClusterAPIRouter sweepAppleAliroCredentialsWithFlow:]
+ -[HMMTRDoorLockClusterAPIRouter walkAppleAliroCredentialsWithCredentialType:flow:visit:]
+ -[HMMTRDoorLockClusterAPIRouter walkAppleAliroCredentialsWithCredentialType:startingAtIndex:flow:visit:]
+ -[HMMTRFirmwareUpdateStatus _dayOneFwUpdateRetryInterval]
+ -[HMMTRFirmwareUpdateStatus _isDayOneFwUpdateFlagSet]
+ -[HMMTRFirmwareUpdateStatus _retryDayOneFwUpdate]
+ -[HMMTRFirmwareUpdateStatus _startDayOneFwUpdateRetryTimer]
+ -[HMMTRFirmwareUpdateStatus _stopDayOneRetryTimer]
+ -[HMMTRFirmwareUpdateStatus _updateIdleResetTimerForDayOneFwUpdate:]
+ -[HMMTRFirmwareUpdateStatus _updateIdleResetTimerWithRegularTimeout]
+ -[HMMTRFirmwareUpdateStatus dayOneFwUpdateFlagDidClear]
+ -[HMMTRFirmwareUpdateStatus dayOneRetryTimer]
+ -[HMMTRFirmwareUpdateStatus setDayOneRetryTimer:]
+ -[HMMTRSyncClusterDoorLock appendAliroCredentialsToUsers:flow:]
+ -[HMMTRSyncClusterDoorLock cacheUserResponse:includesAliroCredentials:]
+ -[HMMTRSyncClusterDoorLock clearEvictableDeviceKeyOfUser:flow:]
+ -[HMMTRSyncClusterDoorLock clearUsers:flow:]
+ -[HMMTRSyncClusterDoorLock ensureAccessoryConnected:countsAsProgress:flow:]
+ -[HMMTRSyncClusterDoorLock ensureAccessoryConnectedForCacheRead:flow:]
+ -[HMMTRSyncClusterDoorLock findHomeUserWithUniqueID:indexStartingAtSlot:assumingTotalNumberOfSlots:availableSlots:usersOfOurFabric:currentFabricIndex:flow:]
+ -[HMMTRSyncClusterDoorLock futureRecordingProgressOfCommand:]
+ -[HMMTRSyncClusterDoorLock knownCurrentFabricIndex]
+ -[HMMTRSyncClusterDoorLock lastOperationProgressUptime]
+ -[HMMTRSyncClusterDoorLock reverifyCachedUser:flow:]
+ -[HMMTRSyncClusterDoorLock setDoorLocked:accessoryUUID:completionHandler:]
+ -[HMMTRSyncClusterDoorLock setKnownCurrentFabricIndex:]
+ -[HMMTRSyncClusterDoorLock setLastOperationProgressUptime:]
+ -[HomeUserSlotResults setUsersOfOurFabric:]
+ -[HomeUserSlotResults usersOfOurFabric]
+ GCC_except_table1008
+ GCC_except_table1012
+ GCC_except_table1014
+ GCC_except_table1016
+ GCC_except_table1018
+ GCC_except_table1022
+ GCC_except_table1025
+ GCC_except_table1088
+ GCC_except_table1092
+ GCC_except_table1094
+ GCC_except_table1219
+ GCC_except_table1279
+ GCC_except_table1325
+ GCC_except_table1333
+ GCC_except_table1384
+ GCC_except_table1392
+ GCC_except_table1429
+ GCC_except_table1467
+ GCC_except_table1494
+ GCC_except_table1691
+ GCC_except_table1732
+ GCC_except_table1886
+ GCC_except_table1888
+ GCC_except_table1912
+ GCC_except_table1913
+ GCC_except_table1914
+ GCC_except_table1915
+ GCC_except_table1918
+ GCC_except_table1921
+ GCC_except_table1922
+ GCC_except_table1923
+ GCC_except_table1925
+ GCC_except_table1926
+ GCC_except_table1938
+ GCC_except_table1940
+ GCC_except_table1941
+ GCC_except_table1942
+ GCC_except_table1950
+ GCC_except_table1955
+ GCC_except_table1958
+ GCC_except_table1960
+ GCC_except_table1962
+ GCC_except_table1963
+ GCC_except_table1965
+ GCC_except_table2032
+ GCC_except_table2038
+ GCC_except_table2076
+ GCC_except_table2159
+ GCC_except_table2277
+ GCC_except_table2310
+ GCC_except_table2319
+ GCC_except_table2321
+ GCC_except_table2370
+ GCC_except_table2409
+ GCC_except_table2433
+ GCC_except_table2499
+ GCC_except_table2789
+ GCC_except_table2791
+ GCC_except_table2793
+ GCC_except_table2797
+ GCC_except_table2858
+ GCC_except_table2899
+ GCC_except_table2948
+ GCC_except_table2950
+ GCC_except_table2981
+ GCC_except_table2982
+ GCC_except_table2983
+ GCC_except_table3005
+ GCC_except_table3006
+ GCC_except_table3007
+ GCC_except_table3008
+ GCC_except_table3009
+ GCC_except_table3010
+ GCC_except_table3011
+ GCC_except_table3012
+ GCC_except_table3022
+ GCC_except_table3024
+ GCC_except_table3036
+ GCC_except_table3055
+ GCC_except_table3071
+ GCC_except_table3077
+ GCC_except_table3090
+ GCC_except_table3093
+ GCC_except_table3097
+ GCC_except_table3112
+ GCC_except_table3119
+ GCC_except_table3121
+ GCC_except_table3151
+ GCC_except_table3160
+ GCC_except_table3165
+ GCC_except_table3177
+ GCC_except_table3232
+ GCC_except_table3649
+ GCC_except_table3674
+ GCC_except_table3675
+ GCC_except_table3676
+ GCC_except_table3680
+ GCC_except_table3685
+ GCC_except_table3688
+ GCC_except_table3704
+ GCC_except_table3719
+ GCC_except_table3788
+ GCC_except_table3796
+ GCC_except_table3805
+ GCC_except_table3806
+ GCC_except_table3839
+ GCC_except_table3848
+ GCC_except_table3852
+ GCC_except_table3886
+ GCC_except_table3889
+ GCC_except_table3897
+ GCC_except_table3919
+ GCC_except_table3923
+ GCC_except_table3962
+ GCC_except_table3964
+ GCC_except_table3966
+ GCC_except_table3985
+ GCC_except_table3987
+ GCC_except_table4005
+ GCC_except_table4088
+ GCC_except_table4178
+ GCC_except_table4182
+ GCC_except_table4197
+ GCC_except_table4198
+ GCC_except_table4199
+ GCC_except_table4205
+ GCC_except_table4212
+ GCC_except_table4217
+ GCC_except_table4272
+ GCC_except_table4294
+ GCC_except_table4340
+ GCC_except_table4345
+ GCC_except_table4348
+ GCC_except_table441
+ GCC_except_table4432
+ GCC_except_table4433
+ GCC_except_table4489
+ GCC_except_table4616
+ GCC_except_table4620
+ GCC_except_table4624
+ GCC_except_table4627
+ GCC_except_table4660
+ GCC_except_table518
+ GCC_except_table556
+ GCC_except_table558
+ GCC_except_table588
+ GCC_except_table592
+ GCC_except_table594
+ GCC_except_table596
+ GCC_except_table768
+ GCC_except_table769
+ GCC_except_table826
+ GCC_except_table827
+ GCC_except_table828
+ GCC_except_table901
+ GCC_except_table943
+ GCC_except_table976
+ _HMMTRAllSettledFailingOnAnyError
+ _HMMTRCredentialIndexOfType
+ _HMMTRDoorLockDlStatusErrorKey
+ _HMMTRDoorLockErrorForSettledResults
+ _HMMTRDoorLockFailedCommandCountErrorKey
+ _HMMTRDoorLockReadCredentialUserTuplesErrorKey
+ _HMMTRDoorLockTotalCommandCountErrorKey
+ _HMMTRErrorForSetCredentialResponse
+ _HMMTRErrorIsLockNotAnswering
+ _HMMTRQueryImageInitiationTypeIsInternalAvailabilityCheck
+ _OBJC_CLASS_$_NAScheduler
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_IVAR_$_HMMTRAccessoryServer._dayOneResumePending
+ _OBJC_IVAR_$_HMMTRFirmwareUpdateStatus._dayOneRetryTimer
+ _OBJC_IVAR_$_HMMTRSyncClusterDoorLock._knownCurrentFabricIndex
+ _OBJC_IVAR_$_HMMTRSyncClusterDoorLock._lastOperationProgressUptime
+ _OBJC_IVAR_$_HomeUserSlotResults._usersOfOurFabric
+ ___104-[HMMTRDoorLockClusterAPIRouter walkAppleAliroCredentialsWithCredentialType:startingAtIndex:flow:visit:]_block_invoke
+ ___121-[HMMTRSyncClusterDoorLock findAllUsersWithCreatorFabricIndex:indexStartingAtSlot:assumingTotalNumberOfSlots:users:flow:]_block_invoke
+ ___156-[HMMTRSyncClusterDoorLock findHomeUserWithUniqueID:indexStartingAtSlot:assumingTotalNumberOfSlots:availableSlots:usersOfOurFabric:currentFabricIndex:flow:]_block_invoke
+ ___39-[HMMTRSyncClusterDoorLock getAllUsers]_block_invoke_2
+ ___40-[HMMTRAccessoryServer setChipDelegate:]_block_invoke
+ ___44-[HMMTRSyncClusterDoorLock clearUsers:flow:]_block_invoke
+ ___47-[HMMTRAnnounceOtaSchedulerTimer timerDidFire:]_block_invoke
+ ___49-[HMMTRFirmwareUpdateStatus _retryDayOneFwUpdate]_block_invoke
+ ___49-[HMMTRFirmwareUpdateStatus _retryDayOneFwUpdate]_block_invoke_2
+ ___49-[HMMTRSyncClusterDoorLock _getUserAtIndex:flow:]_block_invoke
+ ___49-[HMMTRSyncClusterDoorLock _getUserAtIndex:flow:]_block_invoke_2
+ ___51-[HMMTRAccessoryServer requestDayOneFwUpdateResume]_block_invoke
+ ___52-[HMMTRSyncClusterDoorLock reverifyCachedUser:flow:]_block_invoke
+ ___55-[HMMTRFirmwareUpdateStatus dayOneFwUpdateFlagDidClear]_block_invoke
+ ___55-[HMMTRSyncClusterDoorLock getUsersWithUniqueIDs:flow:]_block_invoke_6
+ ___57-[HMMTRSyncClusterDoorLock fetchCurrentFabricIndex_flow:]_block_invoke_3
+ ___58-[HMMTRAccessoryServerBrowser updateOTAProviderForServer:]_block_invoke
+ ___61-[HMMTRSyncClusterDoorLock futureRecordingProgressOfCommand:]_block_invoke
+ ___61-[HMMTRSyncClusterDoorLock futureRecordingProgressOfCommand:]_block_invoke_2
+ ___63-[HMMTRSyncClusterDoorLock appendAliroCredentialsToUsers:flow:]_block_invoke
+ ___63-[HMMTRSyncClusterDoorLock appendAliroCredentialsToUsers:flow:]_block_invoke_2
+ ___63-[HMMTRSyncClusterDoorLock clearEvictableDeviceKeyOfUser:flow:]_block_invoke
+ ___63-[HMMTRSyncClusterDoorLock clearEvictableDeviceKeyOfUser:flow:]_block_invoke_2
+ ___67-[HMMTRDoorLockClusterAPIRouter getUserWithParams:flow:completion:]_block_invoke
+ ___68-[HMMTRDoorLockClusterAPIRouter sweepAppleAliroCredentialsWithFlow:]_block_invoke
+ ___68-[HMMTRFirmwareUpdateStatus _updateIdleResetTimerForDayOneFwUpdate:]_block_invoke
+ ___68-[HMMTRFirmwareUpdateStatus _updateIdleResetTimerWithRegularTimeout]_block_invoke
+ ___68-[HMMTRSyncClusterDoorLock findOrAddUserWithUniqueID:userType:flow:]_block_invoke_2
+ ___74-[HMMTRSyncClusterDoorLock addOrUpdatePinCodeWithValue:forUserIndex:flow:]_block_invoke_3
+ ___74-[HMMTRSyncClusterDoorLock setDoorLocked:accessoryUUID:completionHandler:]_block_invoke
+ ___74-[HMMTRSyncClusterDoorLock setDoorLocked:accessoryUUID:completionHandler:]_block_invoke_2
+ ___75-[HMMTRAccessoryServer _handleAppleLockDoorPositionDetectionEnabledReport:]_block_invoke
+ ___75-[HMMTRSyncClusterDoorLock ensureAccessoryConnected:countsAsProgress:flow:]_block_invoke
+ ___75-[HMMTRSyncClusterDoorLock ensureAccessoryConnected:countsAsProgress:flow:]_block_invoke_2
+ ___75-[HMMTRSyncClusterDoorLock ensureAccessoryConnected:countsAsProgress:flow:]_block_invoke_3
+ ___75-[HMMTRSyncClusterDoorLock ensureAccessoryConnected:countsAsProgress:flow:]_block_invoke_4
+ ___79-[HMMTRDoorLockClusterAPIRouter appendAliroCredentialsToUsers:flow:completion:]_block_invoke
+ ___79-[HMMTRDoorLockClusterAPIRouter appendAliroCredentialsToUsers:flow:completion:]_block_invoke_2
+ ___79-[HMMTRDoorLockClusterAPIRouter appendAliroCredentialsToUsers:flow:completion:]_block_invoke_3
+ ___81-[HMMTRDoorLockClusterAPIRouter getAppleAliroCredentialsWithCredentialType:flow:]_block_invoke
+ ___81-[HMMTRDoorLockClusterAPIRouter getAppleAliroCredentialsWithCredentialType:flow:]_block_invoke_2
+ ___90-[HMMTRSyncClusterDoorLock addOrUpdateIssuerKeyData:forUserUniqueID:isUnifiedAccess:flow:]_block_invoke_2
+ ___90-[HMMTRSyncClusterDoorLock addOrUpdateIssuerKeyData:forUserUniqueID:isUnifiedAccess:flow:]_block_invoke_3
+ ___91-[HMMTRDoorLockClusterAPIRouter findEvictableEndpointKeyIndexForUserIndex:flow:completion:]_block_invoke
+ ___91-[HMMTRDoorLockClusterAPIRouter findEvictableEndpointKeyIndexForUserIndex:flow:completion:]_block_invoke_2
+ ___91-[HMMTRDoorLockClusterAPIRouter findEvictableEndpointKeyIndexForUserIndex:flow:completion:]_block_invoke_3
+ ___92-[HMMTRSyncClusterDoorLock getAllUsersStartingAtSlot:assumingTotalNumberOfSlots:users:flow:]_block_invoke
+ ___98-[HMMTRDescriptorClusterManager _isDoorPositionDetectionDisabledForDoorLockAtCHIPEndpoint:device:]_block_invoke
+ ___HMMTRAllSettledFailingOnAnyError_block_invoke
+ ___HMMTRCredentialIndexOfType_block_invoke
+ ___HMMTRDoorLockErrorForSettledResults_block_invoke
+ ___block_descriptor_32_e27_"NAFuture"16?0"NSArray"8l
+ ___block_descriptor_32_e49_B16?0"MTRDoorLockClusterGetUserResponseParams"8l
+ ___block_descriptor_40_e8_32bs_e45_{_HMFFutureBlockOutcome=q}16?0"HMFFuture"8ls32l8
+ ___block_descriptor_40_e8_32bs_e75_{_HMFFutureBlockOutcome=q}16?0"MTRDoorLockClusterGetUserResponseParams"8ls32l8
+ ___block_descriptor_40_e8_32s_e18_"NAFuture"16?08ls32l8
+ ___block_descriptor_40_e8_32s_e22_B16?0"NSDictionary"8ls32l8
+ ___block_descriptor_48_e8_32bs40r_e8_v16?08ls32l8r40l8
+ ___block_descriptor_48_e8_32s40bs_e16_"HMFFuture"8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e64_B24?0q8"MTRDoorLockClusterGetCredentialStatusResponseParams"16ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e68_v24?0"HMMTRSoftwareUpdateProviderQueryResponseParams"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e64_B24?0q8"MTRDoorLockClusterGetCredentialStatusResponseParams"16ls32l8
+ ___block_descriptor_49_e8_32s40s_e44_{_HMFFutureBlockOutcome=q}16?0"NSString"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e20_v24?08"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e75_{_HMFFutureBlockOutcome=q}16?0"MTRDoorLockClusterGetUserResponseParams"8ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40s48s_e16_"HMFFuture"8?0ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40s48s_e44_{_HMFFutureBlockOutcome=q}16?0"NSNumber"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e22_v16?0"NSDictionary"8ls32l8s40l8s56l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e43_{_HMFFutureBlockOutcome=q}16?0"NSError"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_65_e8_32s40s48s56s_e34_{_HMFFutureBlockOutcome=q}16?08ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48bs_e71_"NAFuture"16?0"MTRDoorLockClusterGetCredentialStatusResponseParams"8ls48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e20_v20?0B8"NSError"12ls64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s_e50_{_HMFFutureBlockOutcome=q}16?0"<HMFAlwaysNil>"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s_e87_{_HMFFutureBlockOutcome=q}16?0"MTRDoorLockClusterGetCredentialStatusResponseParams"8ls32l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e44_{_HMFFutureBlockOutcome=q}16?0"NSNumber"8ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_80_e8_32s40s48s56s64s_e43_{_HMFFutureBlockOutcome=q}16?0"NSError"8ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s_e75_{_HMFFutureBlockOutcome=q}16?0"MTRDoorLockClusterGetUserResponseParams"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_89_e8_32s40s48s56s64s72s80s_e75_{_HMFFutureBlockOutcome=q}16?0"MTRDoorLockClusterGetUserResponseParams"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ _logCategory._hmf_once_t14
+ _logCategory._hmf_once_t1435
+ _logCategory._hmf_once_t357
+ _logCategory._hmf_once_t471
+ _logCategory._hmf_once_t67
+ _logCategory._hmf_once_t796
+ _logCategory._hmf_once_v1436
+ _logCategory._hmf_once_v15
+ _logCategory._hmf_once_v358
+ _logCategory._hmf_once_v472
+ _logCategory._hmf_once_v68
+ _logCategory._hmf_once_v797
- -[HMMTRDoorLockClusterAPIRouter getAppleAliroCredentialsWithCredentialType:startingAtIndex:credentials:flow:]
- -[HMMTRDoorLockClusterAPIRouter getUserWithParams:includeAliroCredentials:temporaryCachedAliroCredentials:flow:completion:]
- -[HMMTRSyncClusterDoorLock __getUserAtIndex:includeAliroCredentials:temporaryCachedAliroCredentials:flow:]
- -[HMMTRSyncClusterDoorLock findAllUsersWithCreatorFabricIndex:indexStartingAtSlot:assumingTotalNumberOfSlots:users:temporaryCachedAliroCredentials:flow:]
- -[HMMTRSyncClusterDoorLock findHomeUserWithUniqueID:indexStartingAtSlot:assumingTotalNumberOfSlots:availableSlots:currentFabricIndex:flow:]
- -[HMMTRSyncClusterDoorLock findHomeUserWithUniqueID:indexStartingAtSlot:assumingTotalNumberOfSlots:availableSlots:currentFabricIndex:temporaryCachedAliroCredentials:flow:]
- -[HMMTRSyncClusterDoorLock getAllUsersStartingAtSlot:assumingTotalNumberOfSlots:users:temporaryCachedAliroCredentials:flow:]
- -[HMMTRSyncClusterDoorLock issuerCredentialForUser:flow:]
- -[HMMTRSyncClusterDoorLock pinCredentialForUser:flow:]
- -[HMMTRSyncClusterDoorLock rfidCredentialForUser:flow:]
- GCC_except_table1059
- GCC_except_table1063
- GCC_except_table1065
- GCC_except_table1188
- GCC_except_table1248
- GCC_except_table1294
- GCC_except_table1302
- GCC_except_table1353
- GCC_except_table1361
- GCC_except_table1398
- GCC_except_table1436
- GCC_except_table1463
- GCC_except_table1660
- GCC_except_table1701
- GCC_except_table1855
- GCC_except_table1856
- GCC_except_table1857
- GCC_except_table1860
- GCC_except_table1880
- GCC_except_table1881
- GCC_except_table1882
- GCC_except_table1883
- GCC_except_table1884
- GCC_except_table1890
- GCC_except_table1892
- GCC_except_table1893
- GCC_except_table1894
- GCC_except_table1895
- GCC_except_table1896
- GCC_except_table1907
- GCC_except_table1909
- GCC_except_table1910
- GCC_except_table1919
- GCC_except_table1929
- GCC_except_table1931
- GCC_except_table1932
- GCC_except_table1934
- GCC_except_table2001
- GCC_except_table2007
- GCC_except_table2045
- GCC_except_table2128
- GCC_except_table2246
- GCC_except_table2248
- GCC_except_table2288
- GCC_except_table2290
- GCC_except_table2339
- GCC_except_table2376
- GCC_except_table2400
- GCC_except_table2466
- GCC_except_table2755
- GCC_except_table2757
- GCC_except_table2759
- GCC_except_table2763
- GCC_except_table2824
- GCC_except_table2865
- GCC_except_table2912
- GCC_except_table2914
- GCC_except_table2945
- GCC_except_table2946
- GCC_except_table2947
- GCC_except_table2969
- GCC_except_table2970
- GCC_except_table2971
- GCC_except_table2972
- GCC_except_table2973
- GCC_except_table2974
- GCC_except_table2975
- GCC_except_table2976
- GCC_except_table2986
- GCC_except_table2988
- GCC_except_table3000
- GCC_except_table3019
- GCC_except_table3035
- GCC_except_table3041
- GCC_except_table3054
- GCC_except_table3057
- GCC_except_table3061
- GCC_except_table3076
- GCC_except_table3079
- GCC_except_table3083
- GCC_except_table3085
- GCC_except_table3124
- GCC_except_table3129
- GCC_except_table3141
- GCC_except_table3193
- GCC_except_table3194
- GCC_except_table3595
- GCC_except_table3620
- GCC_except_table3621
- GCC_except_table3622
- GCC_except_table3626
- GCC_except_table3631
- GCC_except_table3634
- GCC_except_table3650
- GCC_except_table3665
- GCC_except_table3734
- GCC_except_table3742
- GCC_except_table3744
- GCC_except_table3751
- GCC_except_table3752
- GCC_except_table3785
- GCC_except_table3794
- GCC_except_table3832
- GCC_except_table3835
- GCC_except_table3843
- GCC_except_table3865
- GCC_except_table3869
- GCC_except_table3908
- GCC_except_table3910
- GCC_except_table3912
- GCC_except_table3931
- GCC_except_table3933
- GCC_except_table3951
- GCC_except_table4028
- GCC_except_table4075
- GCC_except_table4093
- GCC_except_table4116
- GCC_except_table4120
- GCC_except_table4136
- GCC_except_table4137
- GCC_except_table4143
- GCC_except_table4150
- GCC_except_table4210
- GCC_except_table4232
- GCC_except_table427
- GCC_except_table4278
- GCC_except_table4283
- GCC_except_table4286
- GCC_except_table4370
- GCC_except_table4371
- GCC_except_table4427
- GCC_except_table4430
- GCC_except_table4558
- GCC_except_table4562
- GCC_except_table4565
- GCC_except_table4598
- GCC_except_table504
- GCC_except_table542
- GCC_except_table544
- GCC_except_table574
- GCC_except_table578
- GCC_except_table580
- GCC_except_table582
- GCC_except_table754
- GCC_except_table755
- GCC_except_table812
- GCC_except_table813
- GCC_except_table814
- GCC_except_table887
- GCC_except_table929
- GCC_except_table979
- GCC_except_table983
- GCC_except_table985
- GCC_except_table987
- GCC_except_table989
- GCC_except_table993
- GCC_except_table996
- ___106-[HMMTRSyncClusterDoorLock __getUserAtIndex:includeAliroCredentials:temporaryCachedAliroCredentials:flow:]_block_invoke
- ___106-[HMMTRSyncClusterDoorLock __getUserAtIndex:includeAliroCredentials:temporaryCachedAliroCredentials:flow:]_block_invoke_2
- ___109-[HMMTRDoorLockClusterAPIRouter getAppleAliroCredentialsWithCredentialType:startingAtIndex:credentials:flow:]_block_invoke
- ___123-[HMMTRDoorLockClusterAPIRouter getUserWithParams:includeAliroCredentials:temporaryCachedAliroCredentials:flow:completion:]_block_invoke
- ___123-[HMMTRDoorLockClusterAPIRouter getUserWithParams:includeAliroCredentials:temporaryCachedAliroCredentials:flow:completion:]_block_invoke_2
- ___124-[HMMTRSyncClusterDoorLock getAllUsersStartingAtSlot:assumingTotalNumberOfSlots:users:temporaryCachedAliroCredentials:flow:]_block_invoke
- ___153-[HMMTRSyncClusterDoorLock findAllUsersWithCreatorFabricIndex:indexStartingAtSlot:assumingTotalNumberOfSlots:users:temporaryCachedAliroCredentials:flow:]_block_invoke
- ___171-[HMMTRSyncClusterDoorLock findHomeUserWithUniqueID:indexStartingAtSlot:assumingTotalNumberOfSlots:availableSlots:currentFabricIndex:temporaryCachedAliroCredentials:flow:]_block_invoke
- ___42-[HMMTRSyncClusterDoorLock removeAllUsers]_block_invoke_3
- ___54-[HMMTRSyncClusterDoorLock pinCredentialForUser:flow:]_block_invoke
- ___55-[HMMTRSyncClusterDoorLock rfidCredentialForUser:flow:]_block_invoke
- ___57-[HMMTRSyncClusterDoorLock issuerCredentialForUser:flow:]_block_invoke
- ___58-[HMMTRSyncClusterDoorLock ensureAccessoryConnected:flow:]_block_invoke
- ___58-[HMMTRSyncClusterDoorLock ensureAccessoryConnected:flow:]_block_invoke_2
- ___58-[HMMTRSyncClusterDoorLock ensureAccessoryConnected:flow:]_block_invoke_3
- ___58-[HMMTRSyncClusterDoorLock ensureAccessoryConnected:flow:]_block_invoke_4
- ___72-[HMMTRSyncClusterDoorLock lockDoorWithAccessoryUUID:completionHandler:]_block_invoke
- ___72-[HMMTRSyncClusterDoorLock lockDoorWithAccessoryUUID:completionHandler:]_block_invoke_2
- ___74-[HMMTRSyncClusterDoorLock unlockDoorWithAccessoryUUID:completionHandler:]_block_invoke
- ___74-[HMMTRSyncClusterDoorLock unlockDoorWithAccessoryUUID:completionHandler:]_block_invoke_2
- ___block_descriptor_32_e51_B32?0"MTRDoorLockClusterCredentialStruct"8Q16^B24l
- ___block_descriptor_40_e8_32s_e49_16?0"MTRDoorLockClusterGetUserResponseParams"8ls32l8
- ___block_descriptor_48_e8_32s40s_e60_"HMFFuture"16?0"MTRDoorLockClusterGetUserResponseParams"8ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e20_v24?08"NSError"16ls48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e36_v24?0"<HMFAlwaysNil>"8"NSError"16ls48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e43_{_HMFFutureBlockOutcome=q}16?0"NSError"8ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48bs_e44_{_HMFFutureBlockOutcome=q}16?0"NSString"8ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e45_{_HMFFutureBlockOutcome=q}16?0"HMFFuture"8ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56bs_e44_{_HMFFutureBlockOutcome=q}16?0"NSNumber"8ls32l8s40l8s56l8s48l8
- ___block_descriptor_64_e8_32s40s48s_e87_{_HMFFutureBlockOutcome=q}16?0"MTRDoorLockClusterGetCredentialStatusResponseParams"8ls32l8s40l8s48l8
- ___block_descriptor_65_e8_32s40s48s_e16_"HMFFuture"8?0ls32l8s40l8s48l8
- ___block_descriptor_66_e8_32s40s48s56bs_e61_v24?0"MTRDoorLockClusterGetUserResponseParams"8"NSError"16ls56l8s32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56s64s_e75_{_HMFFutureBlockOutcome=q}16?0"MTRDoorLockClusterGetUserResponseParams"8ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_72_e8_32s40s48s_e71_"NAFuture"16?0"MTRDoorLockClusterGetCredentialStatusResponseParams"8ls32l8s40l8s48l8
- ___block_descriptor_73_e8_32s40s48s56s64bs_e20_v20?0B8"NSError"12ls64l8s32l8s40l8s48l8s56l8
- ___block_descriptor_73_e8_32s40s48s56s64s_e75_{_HMFFutureBlockOutcome=q}16?0"MTRDoorLockClusterGetUserResponseParams"8ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_88_e8_32s40s48s56s64s_e75_{_HMFFutureBlockOutcome=q}16?0"MTRDoorLockClusterGetUserResponseParams"8ls32l8s40l8s48l8s56l8s64l8
- _logCategory._hmf_once_t1422
- _logCategory._hmf_once_t346
- _logCategory._hmf_once_t49
- _logCategory._hmf_once_t492
- _logCategory._hmf_once_t66
- _logCategory._hmf_once_t786
- _logCategory._hmf_once_v1423
- _logCategory._hmf_once_v347
- _logCategory._hmf_once_v493
- _logCategory._hmf_once_v50
- _logCategory._hmf_once_v67
- _logCategory._hmf_once_v787
- _objc_sync_enter
- _objc_sync_exit
CStrings:
+ "%lu of %lu commands failed. First error: %{public}@ %ld"
+ "@\"NAFuture\"16@?0@\"NSArray\"8"
+ "@\"NAFuture\"16@?0@8"
+ "A"
+ "Accessory server is no longer available, skipping OTA provider announcement"
+ "Apple Lock DoorPositionDetectionEnabled changed to %{public}@ on endpoint %{public}@, re-enumerating services"
+ "Apple Lock DoorPositionDetectionEnabled is false for characteristic %@ at endpoint %@ of node %@"
+ "B16@?0@\"NSDictionary\"8"
+ "B24@?0q8@\"MTRDoorLockClusterGetCredentialStatusResponseParams\"16"
+ "Cannot get the status of the software update, announcing OTA provider anyway: %{public}@ (%ld)"
+ "Current device cannot be an OTA provider for node %{public}@ (fabric found: %{public}@)"
+ "Day 1 firmware update flag cleared for accessory server [%{public}@]"
+ "Day 1 firmware update is in progress (%@), postponing the retry for accessory server [%{public}@]"
+ "Day 1 firmware update not resumed, not allowed on this device for node %@ (trigger: %{public}@)"
+ "Day 1 firmware update resume is waiting for the chip delegate for node %@"
+ "Day 1 firmware update resume requested after service enumeration for node %@ (chip delegate attached: %{public}@, OTA state: %{public}@, announce timer set: %{public}@)"
+ "Day 1 firmware update retry skipped, accessory server [%{public}@] is unreachable"
+ "Day 1 firmware update retry skipped, cannot get the status of the update for accessory server [%{public}@], error %{public}@ %ld"
+ "Day 1 firmware update retry skipped, no update available for accessory server [%{public}@]"
+ "DayOneRetryTimer"
+ "Enumeration per Apple Lock DoorPositionDetectionEnabled change complete with error domain: %{public}@ code: %ld"
+ "HMMTRDoorLockDlStatus"
+ "HMMTRDoorLockFailedCommandCount"
+ "HMMTRDoorLockReadCredentialUserTuples"
+ "HMMTRDoorLockTotalCommandCount"
+ "InternalDayOneRetry"
+ "Locking"
+ "OTA announce timer is already set, not updating the OTA provider for node %@"
+ "Resuming the Day 1 firmware update with the OTA announce timer for node %@ (trigger: %{public}@)"
+ "Retrying the Day 1 firmware update for accessory server [%{public}@]"
+ "Server is not enabled. Not updating default OTA provider"
+ "Starting Day 1 firmware update retry timer with delay of %f seconds for accessory server [%{public}@]"
+ "Stop idle reset timer for accessory server [%{public}@]"
+ "The software update is not available, no need to announce OTA provider"
+ "Unlocking"
+ "Update default OTA provider completed for server:%@ with Error: %@."
+ "Update default OTA provider completed for server:%@."
+ "Using DoorPositionDetectionEnabled from endpoint %@ for the DoorLock at endpoint %@ of node %@"
+ "[%{public}@] %lu of %lu commands failed. First error: %{public}@ %ld"
+ "[%{public}@] Accessory server is no longer available, skipping OTA provider announcement"
+ "[%{public}@] Apple Lock DoorPositionDetectionEnabled changed to %{public}@ on endpoint %{public}@, re-enumerating services"
+ "[%{public}@] Apple Lock DoorPositionDetectionEnabled is false for characteristic %@ at endpoint %@ of node %@"
+ "[%{public}@] Cannot get the status of the software update, announcing OTA provider anyway: %{public}@ (%ld)"
+ "[%{public}@] Current device cannot be an OTA provider for node %{public}@ (fabric found: %{public}@)"
+ "[%{public}@] Day 1 firmware update flag cleared for accessory server [%{public}@]"
+ "[%{public}@] Day 1 firmware update is in progress (%@), postponing the retry for accessory server [%{public}@]"
+ "[%{public}@] Day 1 firmware update not resumed, not allowed on this device for node %@ (trigger: %{public}@)"
+ "[%{public}@] Day 1 firmware update resume is waiting for the chip delegate for node %@"
+ "[%{public}@] Day 1 firmware update resume requested after service enumeration for node %@ (chip delegate attached: %{public}@, OTA state: %{public}@, announce timer set: %{public}@)"
+ "[%{public}@] Day 1 firmware update retry skipped, accessory server [%{public}@] is unreachable"
+ "[%{public}@] Day 1 firmware update retry skipped, cannot get the status of the update for accessory server [%{public}@], error %{public}@ %ld"
+ "[%{public}@] Day 1 firmware update retry skipped, no update available for accessory server [%{public}@]"
+ "[%{public}@] Enumeration per Apple Lock DoorPositionDetectionEnabled change complete with error domain: %{public}@ code: %ld"
+ "[%{public}@] OTA announce timer is already set, not updating the OTA provider for node %@"
+ "[%{public}@] Resuming the Day 1 firmware update with the OTA announce timer for node %@ (trigger: %{public}@)"
+ "[%{public}@] Retrying the Day 1 firmware update for accessory server [%{public}@]"
+ "[%{public}@] Server is not enabled. Not updating default OTA provider"
+ "[%{public}@] Starting Day 1 firmware update retry timer with delay of %f seconds for accessory server [%{public}@]"
+ "[%{public}@] Stop idle reset timer for accessory server [%{public}@]"
+ "[%{public}@] The software update is not available, no need to announce OTA provider"
+ "[%{public}@] Update default OTA provider completed for server:%@ with Error: %@."
+ "[%{public}@] Update default OTA provider completed for server:%@."
+ "[%{public}@] Using DoorPositionDetectionEnabled from endpoint %@ for the DoorLock at endpoint %@ of node %@"
+ "[%{public}@] [Flow: %@] Cached user for uniqueID %@ at index %@ is stale on the lock"
+ "[%{public}@] [Flow: %@] Cached user has no issuer key index, reading userIndex: %ld with its credentials"
+ "[%{public}@] [Flow: %@] Calling completion with error: %{public}@ %ld"
+ "[%{public}@] [Flow: %@] Clearing %lu abandoned users that belong to deleted fabrics"
+ "[%{public}@] [Flow: %@] Couldn't read the user of %@ of %lu PINs, first error: %{public}@ %ld"
+ "[%{public}@] [Flow: %@] Dropping credential whose user slot is marked Available. Credential: %@"
+ "[%{public}@] [Flow: %@] Failed to clear credential with error: %{public}@ %ld"
+ "[%{public}@] [Flow: %@] Failed to clear every abandoned user, continuing: %{public}@ %ld"
+ "[%{public}@] [Flow: %@] Failed to read user %@ of a PIN credential, error: %{public}@ %ld"
+ "[%{public}@] [Flow: %@] Failed to verify cached user for userUniqueID %{public}@, walking the lock: %{public}@ %ld"
+ "[%{public}@] [Flow: %@] Found cached user for userUniqueID %@ at index %@, verifying"
+ "[%{public}@] [Flow: %@] Lock reports user %ld has no room for a PIN"
+ "[%{public}@] [NewFlow: %@ {\"Feature\":\"Lock ReadWrite\"}] %s door with accessoryUUID: %@"
+ "[Flow: %@] Cached user for uniqueID %@ at index %@ is stale on the lock"
+ "[Flow: %@] Cached user has no issuer key index, reading userIndex: %ld with its credentials"
+ "[Flow: %@] Calling completion with error: %{public}@ %ld"
+ "[Flow: %@] Clearing %lu abandoned users that belong to deleted fabrics"
+ "[Flow: %@] Couldn't read the user of %@ of %lu PINs, first error: %{public}@ %ld"
+ "[Flow: %@] Dropping credential whose user slot is marked Available. Credential: %@"
+ "[Flow: %@] Failed to clear credential with error: %{public}@ %ld"
+ "[Flow: %@] Failed to clear every abandoned user, continuing: %{public}@ %ld"
+ "[Flow: %@] Failed to read user %@ of a PIN credential, error: %{public}@ %ld"
+ "[Flow: %@] Failed to verify cached user for userUniqueID %{public}@, walking the lock: %{public}@ %ld"
+ "[Flow: %@] Found cached user for userUniqueID %@ at index %@, verifying"
+ "[Flow: %@] Lock reports user %ld has no room for a PIN"
+ "[NewFlow: %@ {\"Feature\":\"Lock ReadWrite\"}] %s door with accessoryUUID: %@"
+ "chip delegate"
+ "enumeration"
+ "hmmtr.dayone.fwupdate.retry.interval"
+ "v16@?0@8"
- "@\"HMFFuture\"16@?0@\"MTRDoorLockClusterGetUserResponseParams\"8"
- "MatteriPhoneOnlyPairingForWatchEnabled"
- "[%{public}@] [Flow: %@] Begin process to re-add AliroCredentialsToUser: %@"
- "[%{public}@] [Flow: %@] Cached user is stale on the lock: %@"
- "[%{public}@] [Flow: %@] Cached user matches identifiers with the lock's current user on index %ld."
- "[%{public}@] [Flow: %@] Calling completion with error: %@"
- "[%{public}@] [Flow: %@] Clear abandoned user: %@ since it belongs to a deleted fabric"
- "[%{public}@] [Flow: %@] Could not find corresponding issuer key index in our cache for userIndex: %ld."
- "[%{public}@] [Flow: %@] Dropping credential that we could not fetch a user for. Credential: %@, Error: %@"
- "[%{public}@] [Flow: %@] Dropping credential that we could not fetch a user for. The user slot was marked Available. Credential: %@"
- "[%{public}@] [Flow: %@] Failed to remove user with index: %@ and uniqueID: %@. Error: %@"
- "[%{public}@] [Flow: %@] Failure to remove all abandoned users with error: %@"
- "[%{public}@] [Flow: %@] Found user on index verify userUniqueID %@"
- "[%{public}@] [Flow: %@] Successfully removed %lu abandoned users"
- "[%{public}@] [Flow: %@] issuerCredentialForUser: %@"
- "[%{public}@] [Flow: %@] pinCredentialForUser: %@"
- "[%{public}@] [NewFlow: %@ {\"Feature\":\"Lock ReadWrite\"}] Locking door with accessoryUUID: %@ completionHandler: %@"
- "[%{public}@] [NewFlow: %@ {\"Feature\":\"Lock ReadWrite\"}] Unlocking door with accessoryUUID: %@ completionHandler: %@"
- "[Flow: %@] Begin process to re-add AliroCredentialsToUser: %@"
- "[Flow: %@] Cached user is stale on the lock: %@"
- "[Flow: %@] Cached user matches identifiers with the lock's current user on index %ld."
- "[Flow: %@] Calling completion with error: %@"
- "[Flow: %@] Clear abandoned user: %@ since it belongs to a deleted fabric"
- "[Flow: %@] Could not find corresponding issuer key index in our cache for userIndex: %ld."
- "[Flow: %@] Dropping credential that we could not fetch a user for. Credential: %@, Error: %@"
- "[Flow: %@] Dropping credential that we could not fetch a user for. The user slot was marked Available. Credential: %@"
- "[Flow: %@] Failed to remove user with index: %@ and uniqueID: %@. Error: %@"
- "[Flow: %@] Failure to remove all abandoned users with error: %@"
- "[Flow: %@] Found user on index verify userUniqueID %@"
- "[Flow: %@] Successfully removed %lu abandoned users"
- "[Flow: %@] issuerCredentialForUser: %@"
- "[Flow: %@] pinCredentialForUser: %@"
- "[NewFlow: %@ {\"Feature\":\"Lock ReadWrite\"}] Locking door with accessoryUUID: %@ completionHandler: %@"
- "[NewFlow: %@ {\"Feature\":\"Lock ReadWrite\"}] Unlocking door with accessoryUUID: %@ completionHandler: %@"
- "aliroCredentials"
- "v24@?0@\"<HMFAlwaysNil>\"8@\"NSError\"16"
- "v24@?0@\"MTRDoorLockClusterGetUserResponseParams\"8@\"NSError\"16"
```
