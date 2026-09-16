## HomeKitMatter

> `/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter`

```diff

-1493.1.5.1.1
-  __TEXT.__text: 0x17d6bc
-  __TEXT.__objc_methlist: 0xad0c
-  __TEXT.__const: 0x298
+1514.0.0.0.1
+  __TEXT.__text: 0x1803f0
+  __TEXT.__objc_methlist: 0xadfc
+  __TEXT.__const: 0x2a8
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__gcc_except_tab: 0x302c
-  __TEXT.__cstring: 0x6ed0
-  __TEXT.__oslogstring: 0x4f542
+  __TEXT.__gcc_except_tab: 0x30a8
+  __TEXT.__cstring: 0x6fc3
+  __TEXT.__oslogstring: 0x502d8
   __TEXT.__ustring: 0x68
-  __TEXT.__unwind_info: 0x3c88
+  __TEXT.__unwind_info: 0x3ce0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x48f0
+  __DATA_CONST.__const: 0x4940
   __DATA_CONST.__objc_classlist: 0x458
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7098
+  __DATA_CONST.__objc_selrefs: 0x7158
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x310
   __DATA_CONST.__objc_arraydata: 0x240
   __DATA_CONST.__got: 0x9f8
   __AUTH_CONST.__const: 0x1140
-  __AUTH_CONST.__cfstring: 0x6d20
-  __AUTH_CONST.__objc_const: 0x10238
+  __AUTH_CONST.__cfstring: 0x6dc0
+  __AUTH_CONST.__objc_const: 0x10330
   __AUTH_CONST.__objc_intobj: 0x1740
   __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1e50
-  __DATA.__objc_ivar: 0xb64
+  __DATA.__objc_ivar: 0xb78
   __DATA.__data: 0xea0
   __DATA_DIRTY.__objc_data: 0xd20
-  __DATA_DIRTY.__bss: 0xc0
+  __DATA_DIRTY.__bss: 0xa0
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/UARPKit.framework/UARPKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4477
-  Symbols:   10307
-  CStrings:  5772
+  Functions: 4506
+  Symbols:   10370
+  CStrings:  5817
 
Symbols:
+ +[HMMTRProtocolMap mapTargetAirPurifierState:]
+ -[HMMTRAccessoryServer _deviceStorageDataSourceForCurrentNode]
+ -[HMMTRAccessoryServer _endPairingMode]
+ -[HMMTRAccessoryServer _enqueueResumeFinalizeAttempt]
+ -[HMMTRAccessoryServer _invalidateFinalizeRetry]
+ -[HMMTRAccessoryServer _persistThreadWEDInfoToStorage]
+ -[HMMTRAccessoryServer _readCharacteristicValueFromCacheAfterConfirmingBridgedAccessoryReachabilityWithCharacteristic:responseHandler:]
+ -[HMMTRAccessoryServer _resumeFinalizePairing]
+ -[HMMTRAccessoryServer _scheduleFinalizeRetry]
+ -[HMMTRAccessoryServer finalizeRetryAttempt]
+ -[HMMTRAccessoryServer finalizeRetryTimer]
+ -[HMMTRAccessoryServer pendingReenumerationCompletionHandlers]
+ -[HMMTRAccessoryServer pendingServiceReenumeration]
+ -[HMMTRAccessoryServer removeNode:withPrivilege:fromExistingAclEntries:]
+ -[HMMTRAccessoryServer resumeFinalizeForCommissionedAccessoryWithOnboardingURL:]
+ -[HMMTRAccessoryServer setFinalizeRetryAttempt:]
+ -[HMMTRAccessoryServer setFinalizeRetryTimer:]
+ -[HMMTRAccessoryServer setPendingServiceReenumeration:]
+ -[HMMTRAccessoryServerBrowser fetchPreferredThreadCredentialsUsingFabricUUID:systemCommissionerFabric:withCompletion:]
+ -[HMMTRAccessoryServerBrowser hasPresentCommissionableNodeMatchingOnboardingURL:]
+ -[HMMTRSyncClusterWindowCovering _targetPositionDictionary:fallingBackToCurrentPositionLift:params:]
+ -[HMMTRThreadRadioManager eMACAddressOfPairingAccessory]
+ -[HMMTRThreadRadioManager setEMACAddressOfPairingAccessory:]
+ GCC_except_table1637
+ GCC_except_table1678
+ GCC_except_table1831
+ GCC_except_table1832
+ GCC_except_table1835
+ GCC_except_table1858
+ GCC_except_table1859
+ GCC_except_table1862
+ GCC_except_table1870
+ GCC_except_table1871
+ GCC_except_table1930
+ GCC_except_table1936
+ GCC_except_table1974
+ GCC_except_table2057
+ GCC_except_table2171
+ GCC_except_table2173
+ GCC_except_table2203
+ GCC_except_table2211
+ GCC_except_table2213
+ GCC_except_table2262
+ GCC_except_table2299
+ GCC_except_table2323
+ GCC_except_table2388
+ GCC_except_table2665
+ GCC_except_table2667
+ GCC_except_table2669
+ GCC_except_table2673
+ GCC_except_table2734
+ GCC_except_table2775
+ GCC_except_table2821
+ GCC_except_table2823
+ GCC_except_table2854
+ GCC_except_table2855
+ GCC_except_table2856
+ GCC_except_table2880
+ GCC_except_table2881
+ GCC_except_table2882
+ GCC_except_table2883
+ GCC_except_table2884
+ GCC_except_table2885
+ GCC_except_table2895
+ GCC_except_table2897
+ GCC_except_table2908
+ GCC_except_table2927
+ GCC_except_table2949
+ GCC_except_table2962
+ GCC_except_table2965
+ GCC_except_table2969
+ GCC_except_table2984
+ GCC_except_table2991
+ GCC_except_table2993
+ GCC_except_table3021
+ GCC_except_table3030
+ GCC_except_table3035
+ GCC_except_table3047
+ GCC_except_table3098
+ GCC_except_table3099
+ GCC_except_table3489
+ GCC_except_table3515
+ GCC_except_table3516
+ GCC_except_table3520
+ GCC_except_table3525
+ GCC_except_table3528
+ GCC_except_table3544
+ GCC_except_table3559
+ GCC_except_table3628
+ GCC_except_table3636
+ GCC_except_table3638
+ GCC_except_table3645
+ GCC_except_table3646
+ GCC_except_table3679
+ GCC_except_table3688
+ GCC_except_table3692
+ GCC_except_table3726
+ GCC_except_table3729
+ GCC_except_table3737
+ GCC_except_table3759
+ GCC_except_table3763
+ GCC_except_table3802
+ GCC_except_table3804
+ GCC_except_table3806
+ GCC_except_table3823
+ GCC_except_table3825
+ GCC_except_table3843
+ GCC_except_table3920
+ GCC_except_table3967
+ GCC_except_table3985
+ GCC_except_table4008
+ GCC_except_table4027
+ GCC_except_table4028
+ GCC_except_table4029
+ GCC_except_table4035
+ GCC_except_table4042
+ GCC_except_table4047
+ GCC_except_table4102
+ GCC_except_table4124
+ GCC_except_table4166
+ GCC_except_table4171
+ GCC_except_table4174
+ GCC_except_table4258
+ GCC_except_table4259
+ GCC_except_table4315
+ GCC_except_table4318
+ GCC_except_table4380
+ GCC_except_table4442
+ GCC_except_table4446
+ GCC_except_table4450
+ GCC_except_table4453
+ GCC_except_table4486
+ _HMMTRAccessoryServerDeferredMatterCommissioningErrorKey
+ _HMMTRAccessoryServerDeferredMatterCommissioningNodeIDKey
+ _HMMTRAccessoryServerDidBeginDeferredMatterCommissioningNotification
+ _HMMTRAccessoryServerDidFailDeferredMatterCommissioningNotification
+ _OBJC_IVAR_$_HMMTRAccessoryServer._finalizeRetryAttempt
+ _OBJC_IVAR_$_HMMTRAccessoryServer._finalizeRetryTimer
+ _OBJC_IVAR_$_HMMTRAccessoryServer._pendingReenumerationCompletionHandlers
+ _OBJC_IVAR_$_HMMTRAccessoryServer._pendingServiceReenumeration
+ _OBJC_IVAR_$_HMMTRThreadRadioManager._eMACAddressOfPairingAccessory
+ ___118-[HMMTRAccessoryServerBrowser fetchPreferredThreadCredentialsUsingFabricUUID:systemCommissionerFabric:withCompletion:]_block_invoke
+ ___139-[HMMTRAccessoryServer scheduleOrExecuteOTAProviderAnnouncement:initiatorType:immediateAnnouncement:endpoint:delayCounter:isUserTriggered:]_block_invoke_2
+ ___39-[HMMTRAccessoryServer _endPairingMode]_block_invoke
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_3
+ ___46-[HMMTRAccessoryServer _resumeFinalizePairing]_block_invoke
+ ___53-[HMMTRAccessoryServer _enqueueResumeFinalizeAttempt]_block_invoke
+ ___54-[HMMTRAccessoryServer _persistThreadWEDInfoToStorage]_block_invoke
+ ___80-[HMMTRAccessoryServer resumeFinalizeForCommissionedAccessoryWithOnboardingURL:]_block_invoke
+ ___block_descriptor_57_e8_32s40s48bs_e46_v24?0"HAPThreadNetworkMetadata"8"NSError"16ls32l8s48l8s40l8
+ ___block_descriptor_57_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ _defaultFeatures._hmf_once_t9
+ _defaultFeatures._hmf_once_v10
+ _logCategory._hmf_once_t135
+ _logCategory._hmf_once_t136
+ _logCategory._hmf_once_t1419
+ _logCategory._hmf_once_t180
+ _logCategory._hmf_once_t24
+ _logCategory._hmf_once_t32
+ _logCategory._hmf_once_t346
+ _logCategory._hmf_once_t492
+ _logCategory._hmf_once_t50
+ _logCategory._hmf_once_t786
+ _logCategory._hmf_once_v136
+ _logCategory._hmf_once_v137
+ _logCategory._hmf_once_v1420
+ _logCategory._hmf_once_v181
+ _logCategory._hmf_once_v25
+ _logCategory._hmf_once_v33
+ _logCategory._hmf_once_v347
+ _logCategory._hmf_once_v493
+ _logCategory._hmf_once_v51
+ _logCategory._hmf_once_v787
+ _objc_msgSend$_deviceStorageDataSourceForCurrentNode
+ _objc_msgSend$_endPairingMode
+ _objc_msgSend$_enqueueResumeFinalizeAttempt
+ _objc_msgSend$_invalidateFinalizeRetry
+ _objc_msgSend$_persistThreadWEDInfoToStorage
+ _objc_msgSend$_readCharacteristicValueFromCacheAfterConfirmingBridgedAccessoryReachabilityWithCharacteristic:responseHandler:
+ _objc_msgSend$_resumeFinalizePairing
+ _objc_msgSend$_scheduleFinalizeRetry
+ _objc_msgSend$_targetPositionDictionary:fallingBackToCurrentPositionLift:params:
+ _objc_msgSend$accessoryNeedsFinalizeResumeForNodeID:fabricUUID:
+ _objc_msgSend$accessoryNetworkCommissioningStateIsReadyForNodeID:fabricUUID:
+ _objc_msgSend$accessoryServerBrowser:getThreadNetworkCredentialsForFabricUUID:requireFullNetworkAttributes:withCompletion:
+ _objc_msgSend$allowsDeferredMatterCommissioningOnThisControllerDevice
+ _objc_msgSend$eMACAddressOfPairingAccessory
+ _objc_msgSend$fetchPreferredThreadCredentialsUsingFabricUUID:systemCommissionerFabric:withCompletion:
+ _objc_msgSend$finalizeRetryAttempt
+ _objc_msgSend$finalizeRetryTimer
+ _objc_msgSend$mapTargetAirPurifierState:
+ _objc_msgSend$markHomeMatterFabricCommissioningDoneWithCompletion:
+ _objc_msgSend$pendingReenumerationCompletionHandlers
+ _objc_msgSend$pendingServiceReenumeration
+ _objc_msgSend$removeNode:withPrivilege:fromExistingAclEntries:
+ _objc_msgSend$resumeFinalizeForCommissionedAccessoryWithOnboardingURL:
+ _objc_msgSend$setEMACAddressOfPairingAccessory:
+ _objc_msgSend$setFinalizeRetryAttempt:
+ _objc_msgSend$setFinalizeRetryTimer:
+ _objc_msgSend$setPendingServiceReenumeration:
+ _objc_msgSend$shouldBypassOtaTimeWindowFirstTimePairing:
- +[HMMTRProtocolMap mapTargetAirPuriferState:]
- -[HMMTRAccessoryServer _readCharacteristicValueFromCacheAfterConfirmingBridgedAccessroyReachabilityWithCharacteristic:responseHandler:]
- -[HMMTRAccessoryServer removeNode:withPrivilge:fromExistingAclEntries:]
- -[HMMTRProtocolMap isRequiresOptionalMatterAttributeForCharacteristic:]
- GCC_except_table1635
- GCC_except_table1676
- GCC_except_table1828
- GCC_except_table1829
- GCC_except_table1833
- GCC_except_table1853
- GCC_except_table1854
- GCC_except_table1860
- GCC_except_table1863
- GCC_except_table1864
- GCC_except_table1928
- GCC_except_table1934
- GCC_except_table1972
- GCC_except_table2055
- GCC_except_table2168
- GCC_except_table2170
- GCC_except_table2200
- GCC_except_table2208
- GCC_except_table2210
- GCC_except_table2259
- GCC_except_table2296
- GCC_except_table2320
- GCC_except_table2385
- GCC_except_table2662
- GCC_except_table2664
- GCC_except_table2666
- GCC_except_table2670
- GCC_except_table2728
- GCC_except_table2769
- GCC_except_table2815
- GCC_except_table2817
- GCC_except_table2848
- GCC_except_table2849
- GCC_except_table2850
- GCC_except_table2872
- GCC_except_table2873
- GCC_except_table2874
- GCC_except_table2875
- GCC_except_table2876
- GCC_except_table2877
- GCC_except_table2889
- GCC_except_table2891
- GCC_except_table2902
- GCC_except_table2921
- GCC_except_table2937
- GCC_except_table2956
- GCC_except_table2959
- GCC_except_table2963
- GCC_except_table2978
- GCC_except_table2981
- GCC_except_table2985
- GCC_except_table3014
- GCC_except_table3023
- GCC_except_table3028
- GCC_except_table3040
- GCC_except_table3091
- GCC_except_table3092
- GCC_except_table3475
- GCC_except_table3500
- GCC_except_table3501
- GCC_except_table3502
- GCC_except_table3506
- GCC_except_table3511
- GCC_except_table3530
- GCC_except_table3545
- GCC_except_table3614
- GCC_except_table3622
- GCC_except_table3624
- GCC_except_table3631
- GCC_except_table3632
- GCC_except_table3661
- GCC_except_table3668
- GCC_except_table3700
- GCC_except_table3703
- GCC_except_table3711
- GCC_except_table3731
- GCC_except_table3734
- GCC_except_table3772
- GCC_except_table3774
- GCC_except_table3776
- GCC_except_table3793
- GCC_except_table3795
- GCC_except_table3813
- GCC_except_table3890
- GCC_except_table3937
- GCC_except_table3955
- GCC_except_table3978
- GCC_except_table3982
- GCC_except_table3997
- GCC_except_table3998
- GCC_except_table3999
- GCC_except_table4005
- GCC_except_table4017
- GCC_except_table4072
- GCC_except_table4094
- GCC_except_table4137
- GCC_except_table4142
- GCC_except_table4145
- GCC_except_table4229
- GCC_except_table4230
- GCC_except_table4286
- GCC_except_table4289
- GCC_except_table4351
- GCC_except_table4413
- GCC_except_table4417
- GCC_except_table4421
- GCC_except_table4424
- GCC_except_table4457
- ___block_descriptor_57_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- _defaultFeatures._hmf_once_t2
- _defaultFeatures._hmf_once_v3
- _logCategory._hmf_once_t119
- _logCategory._hmf_once_t129
- _logCategory._hmf_once_t1361
- _logCategory._hmf_once_t178
- _logCategory._hmf_once_t18
- _logCategory._hmf_once_t29
- _logCategory._hmf_once_t345
- _logCategory._hmf_once_t491
- _logCategory._hmf_once_t749
- _logCategory._hmf_once_v120
- _logCategory._hmf_once_v130
- _logCategory._hmf_once_v1362
- _logCategory._hmf_once_v179
- _logCategory._hmf_once_v19
- _logCategory._hmf_once_v30
- _logCategory._hmf_once_v346
- _logCategory._hmf_once_v492
- _logCategory._hmf_once_v750
- _objc_msgSend$_readCharacteristicValueFromCacheAfterConfirmingBridgedAccessroyReachabilityWithCharacteristic:responseHandler:
- _objc_msgSend$accessoryIsUserConfigurationReadyForNodeID:fabricUUID:
- _objc_msgSend$isRequiresOptionalMatterAttributeForCharacteristic:
- _objc_msgSend$mapTargetAirPuriferState:
- _objc_msgSend$removeNode:withPrivilge:fromExistingAclEntries:
CStrings:
+ "<unknown>"
+ "Accessory for nodeID %@ is not network-commissioning-ready; skipping"
+ "Cannot parse Matter onboarding payload for commissionable-node presence check: %{public}@"
+ "Commissionable-node powered check: discriminator=%{public}@ vendorID=%{public}@ productID=%{public}@ matchingNodePresent=%{public}d (%lu present)"
+ "Connecting pending fabric: %@"
+ "Deferred Matter commissioning not allowed on this controller device; leaving nodeID %@ pending"
+ "Deferred service re-enumeration complete with error domain: %{public}@ code: %ld"
+ "Delegate does not support fabric-scoped Thread credential retrieval"
+ "Element data array missing from array type %@"
+ "FATAL Error: Failed to generate operational cert for fabric ID %@. error: %@"
+ "Failed to fetch Preferred Thread Credentials from owner, error domain: %{public}@ code: %ld"
+ "Failed to persist HomeMatterFabricCommissioningDone state, error domain: %{public}@ code: %ld"
+ "Failed to persist WED support from commissionee info: %@"
+ "Failed to persist eMAC from commissionee info: %@"
+ "Finalize already complete; skipping resume and releasing exclusive slot"
+ "Finalize failed after Matter commissioning completed; scheduling finalize retry with backoff"
+ "Finalize retry already scheduled; not stacking another"
+ "Finalize retry timer fired; enqueuing resume attempt"
+ "FirstTimePairing"
+ "HMMTRAccessoryServerDeferredMatterCommissioningErrorKey"
+ "HMMTRAccessoryServerDeferredMatterCommissioningNodeIDKey"
+ "HMMTRAccessoryServerDidBeginDeferredMatterCommissioningNotification"
+ "HMMTRAccessoryServerDidFailDeferredMatterCommissioningNotification"
+ "No %{public}@ cluster in any of %lu endpoints"
+ "No device storage data source; cannot persist WED info for nodeID %@"
+ "No endpoints available for diagnostic clusters for accessory %{public}@ %{private}@"
+ "Node %@ completed Matter fabric commissioning but not finalize; resuming finalize"
+ "Read color control attribute colorCapabilities supportsColorTempFeature: %@ accessoryRange: [%@ : %@] allowedRange: [%@ : %@]"
+ "Resuming finalize (attempt %lu)"
+ "Resuming finalize for already-commissioned deferred Matter accessory with onboarding URL %{private}@"
+ "Scheduling finalize retry #%lu in %.0f seconds"
+ "Skipping resume finalize: accessory server is disabled, has no controller, or the browser has died"
+ "Target Position reported null; falling back to Current Position"
+ "Thread StopAccessoryPairing completed, error domain: %{public}@ code: %ld"
+ "Thread credential fabric %{public}@ does not match current browser fabric %{public}@"
+ "[%{public}@] Accessory for nodeID %@ is not network-commissioning-ready; skipping"
+ "[%{public}@] Cannot parse Matter onboarding payload for commissionable-node presence check: %{public}@"
+ "[%{public}@] Commissionable-node powered check: discriminator=%{public}@ vendorID=%{public}@ productID=%{public}@ matchingNodePresent=%{public}d (%lu present)"
+ "[%{public}@] Connecting pending fabric: %@"
+ "[%{public}@] Deferred Matter commissioning not allowed on this controller device; leaving nodeID %@ pending"
+ "[%{public}@] Deferred service re-enumeration complete with error domain: %{public}@ code: %ld"
+ "[%{public}@] Delegate does not support fabric-scoped Thread credential retrieval"
+ "[%{public}@] Element data array missing from array type %@"
+ "[%{public}@] FATAL Error: Failed to generate operational cert for fabric ID %@. error: %@"
+ "[%{public}@] Failed to fetch Preferred Thread Credentials from owner, error domain: %{public}@ code: %ld"
+ "[%{public}@] Failed to persist HomeMatterFabricCommissioningDone state, error domain: %{public}@ code: %ld"
+ "[%{public}@] Failed to persist WED support from commissionee info: %@"
+ "[%{public}@] Failed to persist eMAC from commissionee info: %@"
+ "[%{public}@] Finalize already complete; skipping resume and releasing exclusive slot"
+ "[%{public}@] Finalize failed after Matter commissioning completed; scheduling finalize retry with backoff"
+ "[%{public}@] Finalize retry already scheduled; not stacking another"
+ "[%{public}@] Finalize retry timer fired; enqueuing resume attempt"
+ "[%{public}@] No %{public}@ cluster in any of %lu endpoints"
+ "[%{public}@] No device storage data source; cannot persist WED info for nodeID %@"
+ "[%{public}@] No endpoints available for diagnostic clusters for accessory %{public}@ %{private}@"
+ "[%{public}@] Node %@ completed Matter fabric commissioning but not finalize; resuming finalize"
+ "[%{public}@] Read color control attribute colorCapabilities supportsColorTempFeature: %@ accessoryRange: [%@ : %@] allowedRange: [%@ : %@]"
+ "[%{public}@] Resuming finalize (attempt %lu)"
+ "[%{public}@] Resuming finalize for already-commissioned deferred Matter accessory with onboarding URL %{private}@"
+ "[%{public}@] Scheduling finalize retry #%lu in %.0f seconds"
+ "[%{public}@] Skipping resume finalize: accessory server is disabled, has no controller, or the browser has died"
+ "[%{public}@] Target Position reported null; falling back to Current Position"
+ "[%{public}@] Thread StopAccessoryPairing completed, error domain: %{public}@ code: %ld"
+ "[%{public}@] Thread credential fabric %{public}@ does not match current browser fabric %{public}@"
+ "[%{public}@] _connectPendingFabricConnectionsForTargetFabricUUID for - %@"
+ "[%{public}@] resumeFinalizeForCommissionedAccessoryWithOnboardingURL called but already resuming; ignoring"
+ "[%{public}@] verifyHAPCharacteristicSupportWithRequiredAttributeValuesAtCHIPEndpoint shortCharacteristicKey = %@, clusterClassName = %@, hapServicesToCheckForRequiredAttributeValues = %@, hapCharacteristicsToCheckForRequiredAttributeValues = %@, curHAPCharacteristicAttributesToCheck = %@"
+ "_connectPendingFabricConnectionsForTargetFabricUUID for - %@"
+ "resumeFinalizeForCommissionedAccessoryWithOnboardingURL called but already resuming; ignoring"
+ "verifyHAPCharacteristicSupportWithRequiredAttributeValuesAtCHIPEndpoint shortCharacteristicKey = %@, clusterClassName = %@, hapServicesToCheckForRequiredAttributeValues = %@, hapCharacteristicsToCheckForRequiredAttributeValues = %@, curHAPCharacteristicAttributesToCheck = %@"
+ "\xf0\xd2\xf0\xf0\xf0A\xf0\x81"
- "Accessory for nodeID %@ is not user configuration ready; skipping"
- "Connecting pending fabric fabric: %@"
- "Element data data array missing from array type %@"
- "FATAL Error: Failed to generate ooperational cert for fabric ID %@. error: %@"
- "No %@ cluster in any endpoints %@."
- "No endpoints available for diagnostic clusters for HAPAccessory: %@"
- "Notifying matter petric pairing step %@"
- "Optional characteristic %@ on endpoint %@ of node %@ requires an additional Optional Matter attribute check"
- "Read color control attribute colorCapabilities supportsColorTempFeature: %@ accessoryRange: [%@ : %@]  allowedRange: [%@ : %@]"
- "RequiresOptionalMatterAttribute"
- "Thread StopAccessoryPairing completed, error: %@"
- "[%{public}@] Accessory for nodeID %@ is not user configuration ready; skipping"
- "[%{public}@] Connecting pending fabric fabric: %@"
- "[%{public}@] Element data data array missing from array type %@"
- "[%{public}@] FATAL Error: Failed to generate ooperational cert for fabric ID %@. error: %@"
- "[%{public}@] No %@ cluster in any endpoints %@."
- "[%{public}@] No endpoints available for diagnostic clusters for HAPAccessory: %@"
- "[%{public}@] Notifying matter petric pairing step %@"
- "[%{public}@] Optional characteristic %@ on endpoint %@ of node %@ requires an additional Optional Matter attribute check"
- "[%{public}@] Read color control attribute colorCapabilities supportsColorTempFeature: %@ accessoryRange: [%@ : %@]  allowedRange: [%@ : %@]"
- "[%{public}@] Thread StopAccessoryPairing completed, error: %@"
- "[%{public}@] _connectPendingFabricConnectionsForTargetFabricUUIDID for - %@"
- "[%{public}@] verifyHAPCharacteristicSupportWithRequiredAttributeValuesAtCHIPEndpoint shortCharacteristicKey = %@, clusterClassName = %@,  hapServicesToCheckForRequiredAttributeValues = %@, hapCharacteristicsToCheckForRequiredAttributeValues = %@, curHAPCharacteristicAttributesToCheck = %@"
- "_connectPendingFabricConnectionsForTargetFabricUUIDID for - %@"
- "verifyHAPCharacteristicSupportWithRequiredAttributeValuesAtCHIPEndpoint shortCharacteristicKey = %@, clusterClassName = %@,  hapServicesToCheckForRequiredAttributeValues = %@, hapCharacteristicsToCheckForRequiredAttributeValues = %@, curHAPCharacteristicAttributesToCheck = %@"
- "\xf0\xd2\xf0\xf0\xf01\xf0a"
```
