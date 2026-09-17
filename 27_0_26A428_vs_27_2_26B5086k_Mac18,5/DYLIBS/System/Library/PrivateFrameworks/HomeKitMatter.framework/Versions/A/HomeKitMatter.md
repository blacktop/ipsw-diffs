## HomeKitMatter

> `/System/Library/PrivateFrameworks/HomeKitMatter.framework/Versions/A/HomeKitMatter`

```diff

-1493.1.5.4.1
-  __TEXT.__text: 0x18b090
-  __TEXT.__objc_methlist: 0xabf4
-  __TEXT.__const: 0x280
+1514.0.0.0.1
+  __TEXT.__text: 0x18e048
+  __TEXT.__objc_methlist: 0xace4
+  __TEXT.__const: 0x290
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__gcc_except_tab: 0x3070
-  __TEXT.__cstring: 0x6b01
-  __TEXT.__oslogstring: 0x4b788
+  __TEXT.__gcc_except_tab: 0x30e4
+  __TEXT.__cstring: 0x6bf4
+  __TEXT.__oslogstring: 0x4c512
   __TEXT.__ustring: 0x68
-  __TEXT.__unwind_info: 0x3cc8
+  __TEXT.__unwind_info: 0x3d20
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xb78
+  __DATA_CONST.__const: 0xba0
   __DATA_CONST.__objc_classlist: 0x458
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6e50
+  __DATA_CONST.__objc_selrefs: 0x6f10
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x310
   __DATA_CONST.__objc_arraydata: 0x240
   __DATA_CONST.__got: 0x970
-  __AUTH_CONST.__const: 0x56d0
-  __AUTH_CONST.__cfstring: 0x6ba0
-  __AUTH_CONST.__objc_const: 0x102c8
+  __AUTH_CONST.__const: 0x5700
+  __AUTH_CONST.__cfstring: 0x6c40
+  __AUTH_CONST.__objc_const: 0x103c0
   __AUTH_CONST.__objc_intobj: 0x16b0
   __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1e50
-  __DATA.__objc_ivar: 0xb70
+  __DATA.__objc_ivar: 0xb84
   __DATA.__data: 0xea0
   __DATA_DIRTY.__objc_data: 0xd20
   __DATA_DIRTY.__bss: 0xa0

   - /System/Library/PrivateFrameworks/UARPKit.framework/Versions/A/UARPKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4509
-  Symbols:   10330
-  CStrings:  5536
+  Functions: 4538
+  Symbols:   10392
+  CStrings:  5581
 
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
+ GCC_except_table1676
+ GCC_except_table1719
+ GCC_except_table1874
+ GCC_except_table1875
+ GCC_except_table1878
+ GCC_except_table1901
+ GCC_except_table1902
+ GCC_except_table1905
+ GCC_except_table1913
+ GCC_except_table1914
+ GCC_except_table1973
+ GCC_except_table1979
+ GCC_except_table2067
+ GCC_except_table2183
+ GCC_except_table2185
+ GCC_except_table2215
+ GCC_except_table2225
+ GCC_except_table2227
+ GCC_except_table2283
+ GCC_except_table2329
+ GCC_except_table2354
+ GCC_except_table2425
+ GCC_except_table2712
+ GCC_except_table2714
+ GCC_except_table2716
+ GCC_except_table2720
+ GCC_except_table2781
+ GCC_except_table2814
+ GCC_except_table2860
+ GCC_except_table2862
+ GCC_except_table2893
+ GCC_except_table2894
+ GCC_except_table2895
+ GCC_except_table2919
+ GCC_except_table2920
+ GCC_except_table2921
+ GCC_except_table2922
+ GCC_except_table2923
+ GCC_except_table2924
+ GCC_except_table2934
+ GCC_except_table2936
+ GCC_except_table2947
+ GCC_except_table2968
+ GCC_except_table2989
+ GCC_except_table3004
+ GCC_except_table3007
+ GCC_except_table3011
+ GCC_except_table3026
+ GCC_except_table3033
+ GCC_except_table3035
+ GCC_except_table3063
+ GCC_except_table3072
+ GCC_except_table3077
+ GCC_except_table3089
+ GCC_except_table3142
+ GCC_except_table3143
+ GCC_except_table3533
+ GCC_except_table3559
+ GCC_except_table3561
+ GCC_except_table3565
+ GCC_except_table3571
+ GCC_except_table3574
+ GCC_except_table3590
+ GCC_except_table3605
+ GCC_except_table3674
+ GCC_except_table3675
+ GCC_except_table3708
+ GCC_except_table3717
+ GCC_except_table3721
+ GCC_except_table3755
+ GCC_except_table3759
+ GCC_except_table3767
+ GCC_except_table3789
+ GCC_except_table3793
+ GCC_except_table3836
+ GCC_except_table3838
+ GCC_except_table3840
+ GCC_except_table3859
+ GCC_except_table3861
+ GCC_except_table3882
+ GCC_except_table3959
+ GCC_except_table4006
+ GCC_except_table4026
+ GCC_except_table4049
+ GCC_except_table4068
+ GCC_except_table4069
+ GCC_except_table4070
+ GCC_except_table4076
+ GCC_except_table4083
+ GCC_except_table4088
+ GCC_except_table4125
+ GCC_except_table4147
+ GCC_except_table4189
+ GCC_except_table4195
+ GCC_except_table4198
+ GCC_except_table4284
+ GCC_except_table4285
+ GCC_except_table4343
+ GCC_except_table4346
+ GCC_except_table4410
+ GCC_except_table4470
+ GCC_except_table4474
+ GCC_except_table4480
+ GCC_except_table4484
+ GCC_except_table4518
+ OBJC_IVAR_$_HMMTRAccessoryServer._finalizeRetryAttempt
+ OBJC_IVAR_$_HMMTRAccessoryServer._finalizeRetryTimer
+ OBJC_IVAR_$_HMMTRAccessoryServer._pendingReenumerationCompletionHandlers
+ OBJC_IVAR_$_HMMTRAccessoryServer._pendingServiceReenumeration
+ OBJC_IVAR_$_HMMTRThreadRadioManager._eMACAddressOfPairingAccessory
+ _HMMTRAccessoryServerDeferredMatterCommissioningErrorKey
+ _HMMTRAccessoryServerDeferredMatterCommissioningNodeIDKey
+ _HMMTRAccessoryServerDidBeginDeferredMatterCommissioningNotification
+ _HMMTRAccessoryServerDidFailDeferredMatterCommissioningNotification
+ __118-[HMMTRAccessoryServerBrowser fetchPreferredThreadCredentialsUsingFabricUUID:systemCommissionerFabric:withCompletion:]_block_invoke
+ __54-[HMMTRAccessoryServer _persistThreadWEDInfoToStorage]_block_invoke
+ ___118-[HMMTRAccessoryServerBrowser fetchPreferredThreadCredentialsUsingFabricUUID:systemCommissionerFabric:withCompletion:]_block_invoke
+ ___139-[HMMTRAccessoryServer scheduleOrExecuteOTAProviderAnnouncement:initiatorType:immediateAnnouncement:endpoint:delayCounter:isUserTriggered:]_block_invoke_2
+ ___39-[HMMTRAccessoryServer _endPairingMode]_block_invoke
+ ___46-[HMMTRAccessoryServer _resumeFinalizePairing]_block_invoke
+ ___53-[HMMTRAccessoryServer _enqueueResumeFinalizeAttempt]_block_invoke
+ ___54-[HMMTRAccessoryServer _persistThreadWEDInfoToStorage]_block_invoke
+ ___80-[HMMTRAccessoryServer resumeFinalizeForCommissionedAccessoryWithOnboardingURL:]_block_invoke
+ ___block_descriptor_57_e8_32s40s48bs_e46_v24?0"HAPThreadNetworkMetadata"8"NSError"16l
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
+ defaultFeatures._hmf_once_t9
+ defaultFeatures._hmf_once_v10
+ logCategory._hmf_once_t117
+ logCategory._hmf_once_t1301
+ logCategory._hmf_once_t136
+ logCategory._hmf_once_t180
+ logCategory._hmf_once_t24
+ logCategory._hmf_once_t32
+ logCategory._hmf_once_t346
+ logCategory._hmf_once_t492
+ logCategory._hmf_once_t50
+ logCategory._hmf_once_t761
+ logCategory._hmf_once_v118
+ logCategory._hmf_once_v1302
+ logCategory._hmf_once_v137
+ logCategory._hmf_once_v181
+ logCategory._hmf_once_v25
+ logCategory._hmf_once_v33
+ logCategory._hmf_once_v347
+ logCategory._hmf_once_v493
+ logCategory._hmf_once_v51
+ logCategory._hmf_once_v762
- +[HMMTRProtocolMap mapTargetAirPuriferState:]
- -[HMMTRAccessoryServer _readCharacteristicValueFromCacheAfterConfirmingBridgedAccessroyReachabilityWithCharacteristic:responseHandler:]
- -[HMMTRAccessoryServer removeNode:withPrivilge:fromExistingAclEntries:]
- -[HMMTRProtocolMap isRequiresOptionalMatterAttributeForCharacteristic:]
- GCC_except_table1674
- GCC_except_table1717
- GCC_except_table1871
- GCC_except_table1872
- GCC_except_table1876
- GCC_except_table1896
- GCC_except_table1897
- GCC_except_table1903
- GCC_except_table1906
- GCC_except_table1907
- GCC_except_table1971
- GCC_except_table1977
- GCC_except_table2065
- GCC_except_table2180
- GCC_except_table2182
- GCC_except_table2212
- GCC_except_table2222
- GCC_except_table2224
- GCC_except_table2280
- GCC_except_table2326
- GCC_except_table2351
- GCC_except_table2422
- GCC_except_table2709
- GCC_except_table2711
- GCC_except_table2713
- GCC_except_table2717
- GCC_except_table2775
- GCC_except_table2808
- GCC_except_table2854
- GCC_except_table2856
- GCC_except_table2887
- GCC_except_table2888
- GCC_except_table2889
- GCC_except_table2911
- GCC_except_table2912
- GCC_except_table2913
- GCC_except_table2914
- GCC_except_table2915
- GCC_except_table2916
- GCC_except_table2928
- GCC_except_table2930
- GCC_except_table2941
- GCC_except_table2962
- GCC_except_table2977
- GCC_except_table2998
- GCC_except_table3001
- GCC_except_table3005
- GCC_except_table3020
- GCC_except_table3023
- GCC_except_table3027
- GCC_except_table3056
- GCC_except_table3065
- GCC_except_table3070
- GCC_except_table3082
- GCC_except_table3135
- GCC_except_table3136
- GCC_except_table3519
- GCC_except_table3545
- GCC_except_table3546
- GCC_except_table3547
- GCC_except_table3551
- GCC_except_table3557
- GCC_except_table3576
- GCC_except_table3591
- GCC_except_table3660
- GCC_except_table3661
- GCC_except_table3690
- GCC_except_table3697
- GCC_except_table3729
- GCC_except_table3733
- GCC_except_table3741
- GCC_except_table3761
- GCC_except_table3764
- GCC_except_table3806
- GCC_except_table3808
- GCC_except_table3810
- GCC_except_table3829
- GCC_except_table3831
- GCC_except_table3852
- GCC_except_table3929
- GCC_except_table3976
- GCC_except_table3996
- GCC_except_table4019
- GCC_except_table4023
- GCC_except_table4038
- GCC_except_table4039
- GCC_except_table4040
- GCC_except_table4046
- GCC_except_table4058
- GCC_except_table4095
- GCC_except_table4117
- GCC_except_table4160
- GCC_except_table4166
- GCC_except_table4169
- GCC_except_table4255
- GCC_except_table4256
- GCC_except_table4314
- GCC_except_table4317
- GCC_except_table4381
- GCC_except_table4441
- GCC_except_table4445
- GCC_except_table4451
- GCC_except_table4455
- GCC_except_table4489
- __139-[HMMTRAccessoryServer scheduleOrExecuteOTAProviderAnnouncement:initiatorType:immediateAnnouncement:endpoint:delayCounter:isUserTriggered:]_block_invoke
- _objc_msgSend$_readCharacteristicValueFromCacheAfterConfirmingBridgedAccessroyReachabilityWithCharacteristic:responseHandler:
- _objc_msgSend$accessoryIsUserConfigurationReadyForNodeID:fabricUUID:
- _objc_msgSend$isRequiresOptionalMatterAttributeForCharacteristic:
- _objc_msgSend$mapTargetAirPuriferState:
- _objc_msgSend$removeNode:withPrivilge:fromExistingAclEntries:
- defaultFeatures._hmf_once_t2
- defaultFeatures._hmf_once_v3
- logCategory._hmf_once_t111
- logCategory._hmf_once_t119
- logCategory._hmf_once_t1243
- logCategory._hmf_once_t178
- logCategory._hmf_once_t18
- logCategory._hmf_once_t29
- logCategory._hmf_once_t345
- logCategory._hmf_once_t491
- logCategory._hmf_once_t724
- logCategory._hmf_once_v112
- logCategory._hmf_once_v120
- logCategory._hmf_once_v1244
- logCategory._hmf_once_v179
- logCategory._hmf_once_v19
- logCategory._hmf_once_v30
- logCategory._hmf_once_v346
- logCategory._hmf_once_v492
- logCategory._hmf_once_v725
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
+ "Power state changed - state = %lu, goingToSleep: %@"
+ "Read color control attribute colorCapabilities supportsColorTempFeature: %@ accessoryRange: [%@ : %@] allowedRange: [%@ : %@]"
+ "Resuming finalize (attempt %lu)"
+ "Resuming finalize for already-commissioned deferred Matter accessory with onboarding URL %{private}@"
+ "Scheduling finalize retry #%lu in %.0f seconds"
+ "Skipping resume finalize: accessory server is disabled, has no controller, or the browser has died"
+ "Target Position reported null; falling back to Current Position"
+ "Thread StopAccessoryPairing completed, error domain: %{public}@ code: %ld"
+ "Thread credential fabric %{public}@ does not match current browser fabric %{public}@"
+ "Tracking fabric with active clients for resumption for fabricUUID: %@"
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
+ "[%{public}@] Power state changed - state = %lu, goingToSleep: %@"
+ "[%{public}@] Read color control attribute colorCapabilities supportsColorTempFeature: %@ accessoryRange: [%@ : %@] allowedRange: [%@ : %@]"
+ "[%{public}@] Resuming finalize (attempt %lu)"
+ "[%{public}@] Resuming finalize for already-commissioned deferred Matter accessory with onboarding URL %{private}@"
+ "[%{public}@] Scheduling finalize retry #%lu in %.0f seconds"
+ "[%{public}@] Skipping resume finalize: accessory server is disabled, has no controller, or the browser has died"
+ "[%{public}@] Target Position reported null; falling back to Current Position"
+ "[%{public}@] Thread StopAccessoryPairing completed, error domain: %{public}@ code: %ld"
+ "[%{public}@] Thread credential fabric %{public}@ does not match current browser fabric %{public}@"
+ "[%{public}@] Tracking fabric with active clients for resumption for fabricUUID: %@"
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
- "Power state state changed - state = %lu, goingToSleep: %@"
- "Read color control attribute colorCapabilities supportsColorTempFeature: %@ accessoryRange: [%@ : %@]  allowedRange: [%@ : %@]"
- "RequiresOptionalMatterAttribute"
- "Thread StopAccessoryPairing completed, error: %@"
- "Tracking frabic with active clients for resumption for fabricUUID: %@"
- "[%{public}@] Accessory for nodeID %@ is not user configuration ready; skipping"
- "[%{public}@] Connecting pending fabric fabric: %@"
- "[%{public}@] Element data data array missing from array type %@"
- "[%{public}@] FATAL Error: Failed to generate ooperational cert for fabric ID %@. error: %@"
- "[%{public}@] No %@ cluster in any endpoints %@."
- "[%{public}@] No endpoints available for diagnostic clusters for HAPAccessory: %@"
- "[%{public}@] Notifying matter petric pairing step %@"
- "[%{public}@] Optional characteristic %@ on endpoint %@ of node %@ requires an additional Optional Matter attribute check"
- "[%{public}@] Power state state changed - state = %lu, goingToSleep: %@"
- "[%{public}@] Read color control attribute colorCapabilities supportsColorTempFeature: %@ accessoryRange: [%@ : %@]  allowedRange: [%@ : %@]"
- "[%{public}@] Thread StopAccessoryPairing completed, error: %@"
- "[%{public}@] Tracking frabic with active clients for resumption for fabricUUID: %@"
- "[%{public}@] _connectPendingFabricConnectionsForTargetFabricUUIDID for - %@"
- "[%{public}@] verifyHAPCharacteristicSupportWithRequiredAttributeValuesAtCHIPEndpoint shortCharacteristicKey = %@, clusterClassName = %@,  hapServicesToCheckForRequiredAttributeValues = %@, hapCharacteristicsToCheckForRequiredAttributeValues = %@, curHAPCharacteristicAttributesToCheck = %@"
- "_connectPendingFabricConnectionsForTargetFabricUUIDID for - %@"
- "verifyHAPCharacteristicSupportWithRequiredAttributeValuesAtCHIPEndpoint shortCharacteristicKey = %@, clusterClassName = %@,  hapServicesToCheckForRequiredAttributeValues = %@, hapCharacteristicsToCheckForRequiredAttributeValues = %@, curHAPCharacteristicAttributesToCheck = %@"
- "\xf0\xd2\xf0\xf0\xf01\xf0a"
```
