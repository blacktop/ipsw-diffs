## HomeKitMatter

> `/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter`

```diff

-1334.0.0.0.1
-  __TEXT.__text: 0x13bb64
-  __TEXT.__auth_stubs: 0xa40
-  __TEXT.__objc_methlist: 0x9f94
+1340.3.0.0.0
+  __TEXT.__text: 0x13cf08
+  __TEXT.__auth_stubs: 0xa90
+  __TEXT.__objc_methlist: 0xa09c
   __TEXT.__const: 0x160
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__gcc_except_tab: 0x2b88
-  __TEXT.__cstring: 0x684b
-  __TEXT.__oslogstring: 0x279f9
+  __TEXT.__gcc_except_tab: 0x2cd4
+  __TEXT.__cstring: 0x68df
+  __TEXT.__oslogstring: 0x27c9c
   __TEXT.__ustring: 0x68
-  __TEXT.__unwind_info: 0x2d60
-  __TEXT.__objc_classname: 0x13be
-  __TEXT.__objc_methname: 0x24ae7
-  __TEXT.__objc_methtype: 0x3997
-  __TEXT.__objc_stubs: 0x15ca0
-  __DATA_CONST.__got: 0x998
-  __DATA_CONST.__const: 0x4658
-  __DATA_CONST.__objc_classlist: 0x400
+  __TEXT.__unwind_info: 0x2da8
+  __TEXT.__objc_classname: 0x13d4
+  __TEXT.__objc_methname: 0x24e37
+  __TEXT.__objc_methtype: 0x3a1f
+  __TEXT.__objc_stubs: 0x15e40
+  __DATA_CONST.__got: 0x9a0
+  __DATA_CONST.__const: 0x4690
+  __DATA_CONST.__objc_classlist: 0x408
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6988
+  __DATA_CONST.__objc_selrefs: 0x6a18
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x2c8
+  __DATA_CONST.__objc_superrefs: 0x2d0
   __DATA_CONST.__objc_arraydata: 0x230
-  __AUTH_CONST.__auth_got: 0x530
-  __AUTH_CONST.__const: 0xfa0
+  __AUTH_CONST.__auth_got: 0x558
+  __AUTH_CONST.__const: 0x1000
   __AUTH_CONST.__cfstring: 0x6a00
-  __AUTH_CONST.__objc_const: 0xeda8
+  __AUTH_CONST.__objc_const: 0xef98
   __AUTH_CONST.__objc_intobj: 0x1728
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x1cc0
-  __DATA.__objc_ivar: 0xa60
+  __AUTH.__objc_data: 0x1d10
+  __DATA.__objc_ivar: 0xa7c
   __DATA.__data: 0xd80
-  __DATA.__bss: 0x428
+  __DATA.__bss: 0x438
   __DATA_DIRTY.__objc_data: 0xb40
-  __DATA_DIRTY.__bss: 0xb0
+  __DATA_DIRTY.__bss: 0xa0
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4B89A236-08E3-37B6-829D-430F8C7F97FA
-  Functions: 4126
-  Symbols:   14284
-  CStrings:  9281
+  UUID: 8F307863-98D1-3A37-BED8-1938E8A3B38F
+  Functions: 4150
+  Symbols:   14371
+  CStrings:  9330
 
Symbols:
+ -[HMMTRAccessoryServer busyImageResponseCounter]
+ -[HMMTRAccessoryServer handleBusyImageResponseCounter]
+ -[HMMTRAccessoryServer handleNotAvailableImageResponseCounter]
+ -[HMMTRAccessoryServer notAvailableImageResponseCounter]
+ -[HMMTRAccessoryServer resetNonAvailableCounters]
+ -[HMMTRAccessoryServer setBusyImageResponseCounter:]
+ -[HMMTRAccessoryServer setNotAvailableImageResponseCounter:]
+ -[HMMTRFabricConnectionRequest abortAllLowPriorityOperationsWithReason:]
+ -[HMMTRFabricConnectionRequest hasOnlyQueuedLowPriorityRequests]
+ -[HMMTRFabricConnectionRequest notifyOperationsCompleted:]
+ -[HMMTRFabricConnectionRequest setHasOnlyQueuedLowPriorityRequests:]
+ -[HMMTRTimeBasedCounter _startNewCountingPeriod:]
+ -[HMMTRTimeBasedCounter count]
+ -[HMMTRTimeBasedCounter incrementOrReset]
+ -[HMMTRTimeBasedCounter initTimeBasedCounter:]
+ -[HMMTRTimeBasedCounter resetTimeBasedCounter]
+ -[HMMTRTimeBasedCounter setCount:]
+ -[HMMTRTimeBasedCounter setStartTime:]
+ -[HMMTRTimeBasedCounter setThreshold:]
+ -[HMMTRTimeBasedCounter startTime]
+ -[HMMTRTimeBasedCounter threshold]
+ GCC_except_table1718
+ GCC_except_table1720
+ GCC_except_table1723
+ GCC_except_table1744
+ GCC_except_table1745
+ GCC_except_table1747
+ GCC_except_table1756
+ GCC_except_table1757
+ GCC_except_table1758
+ GCC_except_table1759
+ GCC_except_table1818
+ GCC_except_table1824
+ GCC_except_table1901
+ GCC_except_table2013
+ GCC_except_table2015
+ GCC_except_table2045
+ GCC_except_table2053
+ GCC_except_table2055
+ GCC_except_table2103
+ GCC_except_table2144
+ GCC_except_table2206
+ GCC_except_table2445
+ GCC_except_table2449
+ GCC_except_table2501
+ GCC_except_table2542
+ GCC_except_table2585
+ GCC_except_table2587
+ GCC_except_table2612
+ GCC_except_table2613
+ GCC_except_table2614
+ GCC_except_table2635
+ GCC_except_table2636
+ GCC_except_table2637
+ GCC_except_table2638
+ GCC_except_table2639
+ GCC_except_table2641
+ GCC_except_table2654
+ GCC_except_table2656
+ GCC_except_table2675
+ GCC_except_table2691
+ GCC_except_table2708
+ GCC_except_table2711
+ GCC_except_table2715
+ GCC_except_table2730
+ GCC_except_table2733
+ GCC_except_table2737
+ GCC_except_table2739
+ GCC_except_table2758
+ GCC_except_table2764
+ GCC_except_table2769
+ GCC_except_table2782
+ GCC_except_table2833
+ GCC_except_table2834
+ GCC_except_table3196
+ GCC_except_table3197
+ GCC_except_table3198
+ GCC_except_table3202
+ GCC_except_table3207
+ GCC_except_table3210
+ GCC_except_table3224
+ GCC_except_table3240
+ GCC_except_table3305
+ GCC_except_table3324
+ GCC_except_table3326
+ GCC_except_table3333
+ GCC_except_table3334
+ GCC_except_table3357
+ GCC_except_table3358
+ GCC_except_table3367
+ GCC_except_table3392
+ GCC_except_table3395
+ GCC_except_table3403
+ GCC_except_table3422
+ GCC_except_table3425
+ GCC_except_table3465
+ GCC_except_table3482
+ GCC_except_table3484
+ GCC_except_table3502
+ GCC_except_table3568
+ GCC_except_table3612
+ GCC_except_table3630
+ GCC_except_table3653
+ GCC_except_table3657
+ GCC_except_table3672
+ GCC_except_table3673
+ GCC_except_table3678
+ GCC_except_table3685
+ GCC_except_table3742
+ GCC_except_table3762
+ GCC_except_table3816
+ GCC_except_table3821
+ GCC_except_table3824
+ GCC_except_table3903
+ GCC_except_table3904
+ GCC_except_table3959
+ GCC_except_table3962
+ GCC_except_table4024
+ GCC_except_table4086
+ GCC_except_table4090
+ GCC_except_table4094
+ GCC_except_table4097
+ GCC_except_table4130
+ _HMFUptime
+ _OBJC_CLASS_$_HMMTRTimeBasedCounter
+ _OBJC_IVAR_$_HMMTRAccessoryServer._busyImageResponseCounter
+ _OBJC_IVAR_$_HMMTRAccessoryServer._notAvailableImageResponseCounter
+ _OBJC_IVAR_$_HMMTRFabricConnectionRequest._hasOnlyQueuedLowPriorityRequests
+ _OBJC_IVAR_$_HMMTRTimeBasedCounter._count
+ _OBJC_IVAR_$_HMMTRTimeBasedCounter._startTime
+ _OBJC_IVAR_$_HMMTRTimeBasedCounter._threshold
+ _OBJC_IVAR_$_HMMTRTimeBasedCounter._timeBasedCounterlock
+ _OBJC_METACLASS_$_HMMTRTimeBasedCounter
+ __OBJC_$_INSTANCE_METHODS_HMMTRTimeBasedCounter
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRTimeBasedCounter
+ __OBJC_$_PROP_LIST_HMMTRTimeBasedCounter
+ __OBJC_CLASS_RO_$_HMMTRTimeBasedCounter
+ __OBJC_METACLASS_RO_$_HMMTRTimeBasedCounter
+ ___101-[HMMTRAccessoryServer updateAccessoryControlToIncludeAdministratorNodes:sharedUserNodes:completion:]_block_invoke.824
+ ___102-[HMMTRAccessoryServer updateAllCharacteristicValuesPostHAPServiceEnumerationForAccessory:completion:]_block_invoke.775
+ ___112-[HMMTRAccessoryServer _updateAdditionalCharacteristicsFromCharacteristicUpdate:service:path:completionHandler:]_block_invoke.377
+ ___114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke.900
+ ___114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke.903
+ ___117-[HMMTRAccessoryServer _findSystemCommissionerPairingMatchingSetupPayload:systemCommissionerPairings:pairingManager:]_block_invoke.258
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.501
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.502
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.504
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.508
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.503
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.505
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.507
+ ___37-[HMMTRAccessoryServer finishPairing]_block_invoke.755
+ ___37-[HMMTRAccessoryServer timerDidFire:]_block_invoke.274
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.631
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.632
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.633
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.639
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.640
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.641
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.642
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.634
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.643
+ ___42-[HMMTRAccessoryServer _setupMatterDevice]_block_invoke.305
+ ___43-[HMMTRAccessoryServer _setupThreadPairing]_block_invoke.460
+ ___43-[HMMTRAccessoryServer _unpair:completion:]_block_invoke.297
+ ___43-[HMMTRAccessoryServer discoverAccessories]_block_invoke.300
+ ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.874
+ ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.876
+ ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.877
+ ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.879
+ ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke_2.875
+ ___45-[HMMTRAccessoryServer stopPairingWithError:]_block_invoke.286
+ ___47-[HMMTRAccessoryServer processAttributeReport:]_block_invoke.963
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.848
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.851
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.853
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke_2.852
+ ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.807
+ ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.811
+ ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.812
+ ___51-[HMMTRAccessoryServer device:receivedEventReport:]_block_invoke.964
+ ___52-[HMMTRAccessoryServer populateACLEntriesForPairing]_block_invoke.628
+ ___53-[HMMTRAccessoryServer _tryPairingUsingMatterSupport]_block_invoke.251
+ ___55-[HMMTRAccessoryServer device:receivedAttributeReport:]_block_invoke.962
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.423
+ ___58-[HMMTRFabricConnectionRequest notifyOperationsCompleted:]_block_invoke
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.432
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.436
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.905
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.907
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.911
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.913
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.429
+ ___63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.805
+ ___63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.806
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.483
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.452
+ ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.926
+ ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.927
+ ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.928
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.447
+ ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.439
+ ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.442
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.469
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.472
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.477
+ ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.410
+ ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.417
+ ___71-[HMMTRAccessoryServer validateAttestationDeviceInfo:error:completion:]_block_invoke.276
+ ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.395
+ ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.403
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.463
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.466
+ ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.266
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.800
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.801
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.803
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.804
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.776
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.777
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.787
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.795
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.796
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.798
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.799
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke_2.791
+ ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.858
+ ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.859
+ ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.863
+ ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke_2.865
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.291
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.294
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.292
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.295
+ ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.406
+ ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.409
+ ___82-[HMMTRAccessoryServer fetchColorControlClusterForHapAccessory:completionHandler:]_block_invoke.914
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.882
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.883
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.884
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.887
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke_2.886
+ ___83-[HMMTRAccessoryServer updateAccessoryControlToRemoveAdministratorNode:completion:]_block_invoke.825
+ ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.381
+ ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.383
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.888
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.889
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.890
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.891
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.895
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.896
+ ___86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.929
+ ___86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.930
+ ___92-[HMMTRAccessoryServer _createFirmwareUpdateServiceWithInstanceID:device:completionHandler:]_block_invoke.768
+ ___94-[HMMTRAccessoryServer updateAccessoryControlToAdministratorNodes:sharedUserNodes:completion:]_block_invoke.823
+ ___99-[HMMTRAccessoryServer _tryPairingWithOnboardingPayload:systemCommissionerPairings:pairingManager:]_block_invoke.255
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.511
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.517
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.518
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke_2.513
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke_3
+ ___Block_byref_object_copy_.10098
+ ___Block_byref_object_copy_.10815
+ ___Block_byref_object_copy_.11509
+ ___Block_byref_object_copy_.12204
+ ___Block_byref_object_copy_.12370
+ ___Block_byref_object_copy_.5719
+ ___Block_byref_object_copy_.7607
+ ___Block_byref_object_copy_.8026
+ ___Block_byref_object_copy_.9138
+ ___Block_byref_object_dispose_.10099
+ ___Block_byref_object_dispose_.10816
+ ___Block_byref_object_dispose_.11510
+ ___Block_byref_object_dispose_.12205
+ ___Block_byref_object_dispose_.12371
+ ___Block_byref_object_dispose_.5720
+ ___Block_byref_object_dispose_.7608
+ ___Block_byref_object_dispose_.8027
+ ___Block_byref_object_dispose_.9139
+ ___block_descriptor_122_e8_32s40s48s56s64s72s80bs88r96r104r_e5_v8?0lr88l8s32l8s40l8r96l8s48l8r104l8s56l8s64l8s80l8s72l8
+ ___block_descriptor_32_e26_"NSArray"16?0"NSArray"8l
+ ___block_descriptor_32_e36_16?0"HMMTRHAPServiceDescription"8l
+ ___block_descriptor_32_e83_q24?0"HAPCharacteristicWriteRequestTuple"8"HAPCharacteristicWriteRequestTuple"16l
+ ___block_descriptor_72_e8_32s40s48r56r_e40_v16?0"HAPCharacteristicResponseTuple"8ls32l8r48l8r56l8s40l8
+ ___block_descriptor_72_e8_32s40s48r56r_e5_v8?0lr48l8r56l8s32l8s40l8
+ ___block_descriptor_81_e8_32s40s48s56bs64r_e29_v24?0"NSArray"8"NSError"16lr64l8s32l8s56l8s40l8s48l8
+ ___block_literal_global.10551
+ ___block_literal_global.11107
+ ___block_literal_global.11332
+ ___block_literal_global.11544
+ ___block_literal_global.11682
+ ___block_literal_global.11812
+ ___block_literal_global.12029
+ ___block_literal_global.303.9095
+ ___block_literal_global.516
+ ___block_literal_global.5436
+ ___block_literal_global.5608
+ ___block_literal_global.5846
+ ___block_literal_global.5976
+ ___block_literal_global.6117
+ ___block_literal_global.6226
+ ___block_literal_global.6260
+ ___block_literal_global.6281
+ ___block_literal_global.6531
+ ___block_literal_global.6544
+ ___block_literal_global.6638
+ ___block_literal_global.6732
+ ___block_literal_global.6826
+ ___block_literal_global.6929
+ ___block_literal_global.7023
+ ___block_literal_global.7162
+ ___block_literal_global.7303
+ ___block_literal_global.7408
+ ___block_literal_global.7477
+ ___block_literal_global.75.9895
+ ___block_literal_global.773
+ ___block_literal_global.780
+ ___block_literal_global.7809
+ ___block_literal_global.790
+ ___block_literal_global.794
+ ___block_literal_global.8037
+ ___block_literal_global.8371
+ ___block_literal_global.8495
+ ___block_literal_global.8629
+ ___block_literal_global.9170
+ ___block_literal_global.9574
+ ___block_literal_global.971
+ ___block_literal_global.9894
+ ___block_literal_global.9970
+ _exp2
+ _logCategory._hmf_once_t0.5607
+ _logCategory._hmf_once_t0.6259
+ _logCategory._hmf_once_t14.6543
+ _logCategory._hmf_once_t14.6637
+ _logCategory._hmf_once_t14.6731
+ _logCategory._hmf_once_t14.6928
+ _logCategory._hmf_once_t14.7022
+ _logCategory._hmf_once_t14.7161
+ _logCategory._hmf_once_t2.6225
+ _logCategory._hmf_once_t2.7302
+ _logCategory._hmf_once_t2.9969
+ _logCategory._hmf_once_t20.11681
+ _logCategory._hmf_once_t26.6825
+ _logCategory._hmf_once_t31.11811
+ _logCategory._hmf_once_t4.7407
+ _logCategory._hmf_once_t674
+ _logCategory._hmf_once_t68.12230
+ _logCategory._hmf_once_t8.11331
+ _logCategory._hmf_once_t8.8494
+ _logCategory._hmf_once_t9.5975
+ _logCategory._hmf_once_v1.5609
+ _logCategory._hmf_once_v1.6261
+ _logCategory._hmf_once_v10.5977
+ _logCategory._hmf_once_v15.6545
+ _logCategory._hmf_once_v15.6639
+ _logCategory._hmf_once_v15.6733
+ _logCategory._hmf_once_v15.6930
+ _logCategory._hmf_once_v15.7024
+ _logCategory._hmf_once_v15.7163
+ _logCategory._hmf_once_v21.11683
+ _logCategory._hmf_once_v27.6827
+ _logCategory._hmf_once_v3.6227
+ _logCategory._hmf_once_v3.7304
+ _logCategory._hmf_once_v3.9971
+ _logCategory._hmf_once_v32.11813
+ _logCategory._hmf_once_v5.7409
+ _logCategory._hmf_once_v675
+ _logCategory._hmf_once_v69.12231
+ _logCategory._hmf_once_v9.11333
+ _logCategory._hmf_once_v9.8496
+ _objc_msgSend$_startNewCountingPeriod:
+ _objc_msgSend$abortAllLowPriorityOperationsWithReason:
+ _objc_msgSend$busyImageResponseCounter
+ _objc_msgSend$hasOnlyQueuedLowPriorityRequests
+ _objc_msgSend$incrementOrReset
+ _objc_msgSend$initTimeBasedCounter:
+ _objc_msgSend$notAvailableImageResponseCounter
+ _objc_msgSend$notifyOperationsCompleted:
+ _objc_msgSend$resetTimeBasedCounter
+ _objc_msgSend$setBusyImageResponseCounter:
+ _objc_msgSend$setCount:
+ _objc_msgSend$setHasOnlyQueuedLowPriorityRequests:
+ _objc_msgSend$threshold
+ _os_unfair_lock_assert_owner
+ _os_unfair_recursive_lock_lock_with_options
+ _os_unfair_recursive_lock_unlock
- GCC_except_table1716
- GCC_except_table1717
- GCC_except_table1739
- GCC_except_table1740
- GCC_except_table1741
- GCC_except_table1742
- GCC_except_table1749
- GCC_except_table1751
- GCC_except_table1752
- GCC_except_table1814
- GCC_except_table1820
- GCC_except_table1897
- GCC_except_table2031
- GCC_except_table2039
- GCC_except_table2041
- GCC_except_table2089
- GCC_except_table2130
- GCC_except_table2192
- GCC_except_table2431
- GCC_except_table2435
- GCC_except_table2487
- GCC_except_table2528
- GCC_except_table2571
- GCC_except_table2573
- GCC_except_table2598
- GCC_except_table2599
- GCC_except_table2600
- GCC_except_table2621
- GCC_except_table2622
- GCC_except_table2623
- GCC_except_table2624
- GCC_except_table2625
- GCC_except_table2626
- GCC_except_table2627
- GCC_except_table2628
- GCC_except_table2661
- GCC_except_table2677
- GCC_except_table2683
- GCC_except_table2694
- GCC_except_table2701
- GCC_except_table2716
- GCC_except_table2719
- GCC_except_table2723
- GCC_except_table2725
- GCC_except_table2744
- GCC_except_table2750
- GCC_except_table2755
- GCC_except_table2768
- GCC_except_table2819
- GCC_except_table2820
- GCC_except_table3178
- GCC_except_table3179
- GCC_except_table3180
- GCC_except_table3184
- GCC_except_table3189
- GCC_except_table3192
- GCC_except_table3206
- GCC_except_table3222
- GCC_except_table3287
- GCC_except_table3306
- GCC_except_table3308
- GCC_except_table3315
- GCC_except_table3316
- GCC_except_table3339
- GCC_except_table3340
- GCC_except_table3349
- GCC_except_table3372
- GCC_except_table3375
- GCC_except_table3383
- GCC_except_table3402
- GCC_except_table3405
- GCC_except_table3441
- GCC_except_table3445
- GCC_except_table3463
- GCC_except_table3481
- GCC_except_table3544
- GCC_except_table3588
- GCC_except_table3606
- GCC_except_table3629
- GCC_except_table3633
- GCC_except_table3648
- GCC_except_table3649
- GCC_except_table3654
- GCC_except_table3661
- GCC_except_table3718
- GCC_except_table3738
- GCC_except_table3792
- GCC_except_table3797
- GCC_except_table3800
- GCC_except_table3879
- GCC_except_table3880
- GCC_except_table3935
- GCC_except_table3938
- GCC_except_table4000
- GCC_except_table4062
- GCC_except_table4066
- GCC_except_table4070
- GCC_except_table4073
- GCC_except_table4106
- __OBJC_$_PROP_LIST_HMMTROperationalCertificateIssuer
- ___101-[HMMTRAccessoryServer updateAccessoryControlToIncludeAdministratorNodes:sharedUserNodes:completion:]_block_invoke.811
- ___102-[HMMTRAccessoryServer updateAllCharacteristicValuesPostHAPServiceEnumerationForAccessory:completion:]_block_invoke.770
- ___112-[HMMTRAccessoryServer _updateAdditionalCharacteristicsFromCharacteristicUpdate:service:path:completionHandler:]_block_invoke.376
- ___114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke.887
- ___114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke.890
- ___117-[HMMTRAccessoryServer _findSystemCommissionerPairingMatchingSetupPayload:systemCommissionerPairings:pairingManager:]_block_invoke.256
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.497
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.503
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.501
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.504
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_3.502
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_3.505
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_4
- ___37-[HMMTRAccessoryServer finishPairing]_block_invoke.750
- ___37-[HMMTRAccessoryServer timerDidFire:]_block_invoke.273
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.625
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.626
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.627
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.628
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.634
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.636
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.637
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.629
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.638
- ___42-[HMMTRAccessoryServer _setupMatterDevice]_block_invoke.304
- ___43-[HMMTRAccessoryServer _setupThreadPairing]_block_invoke.459
- ___43-[HMMTRAccessoryServer _unpair:completion:]_block_invoke.296
- ___43-[HMMTRAccessoryServer discoverAccessories]_block_invoke.299
- ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.861
- ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.863
- ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.864
- ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke.866
- ___45-[HMMTRAccessoryServer _onThreadScanResults:]_block_invoke_2.862
- ___45-[HMMTRAccessoryServer stopPairingWithError:]_block_invoke.285
- ___47-[HMMTRAccessoryServer processAttributeReport:]_block_invoke.950
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.835
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.838
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.840
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke_2.839
- ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.794
- ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.798
- ___51-[HMMTRAccessoryServer _collectNetworkCredentials:]_block_invoke.799
- ___51-[HMMTRAccessoryServer device:receivedEventReport:]_block_invoke.951
- ___52-[HMMTRAccessoryServer populateACLEntriesForPairing]_block_invoke.623
- ___53-[HMMTRAccessoryServer _tryPairingUsingMatterSupport]_block_invoke.250
- ___55-[HMMTRAccessoryServer device:receivedAttributeReport:]_block_invoke.949
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.417
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.429
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.433
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.892
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.894
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.898
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.900
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.423
- ___61-[HMMTRFabricConnectionRequest abortAllOperationsWithReason:]_block_invoke
- ___63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.792
- ___63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.793
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.477
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.447
- ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.913
- ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.914
- ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.915
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.442
- ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.436
- ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.441
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.466
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.471
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.475
- ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.409
- ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.414
- ___71-[HMMTRAccessoryServer validateAttestationDeviceInfo:error:completion:]_block_invoke.275
- ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.394
- ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.400
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.460
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.464
- ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.262
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.787
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.788
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.790
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.791
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.771
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.772
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.782
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.783
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.785
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.786
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.845
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.846
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke.850
- ___74-[HMMTRAccessoryServer _requestAccessoryNetworkScanWithCompletionHandler:]_block_invoke_2.852
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.288
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.292
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.291
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.294
- ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.403
- ___79-[HMMTRAccessoryServer _openPairingWindowWithPINForDuration:completionHandler:]_block_invoke.407
- ___82-[HMMTRAccessoryServer fetchColorControlClusterForHapAccessory:completionHandler:]_block_invoke.901
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.869
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.870
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.871
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.874
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke_2.873
- ___83-[HMMTRAccessoryServer updateAccessoryControlToRemoveAdministratorNode:completion:]_block_invoke.812
- ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.380
- ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.382
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.875
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.876
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.877
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.878
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.882
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.883
- ___86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.916
- ___86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.917
- ___92-[HMMTRAccessoryServer _createFirmwareUpdateServiceWithInstanceID:device:completionHandler:]_block_invoke.763
- ___94-[HMMTRAccessoryServer updateAccessoryControlToAdministratorNodes:sharedUserNodes:completion:]_block_invoke.810
- ___99-[HMMTRAccessoryServer _tryPairingWithOnboardingPayload:systemCommissionerPairings:pairingManager:]_block_invoke.253
- ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.507
- ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.508
- ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.513
- ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke_2.511
- ___Block_byref_object_copy_.10045
- ___Block_byref_object_copy_.10788
- ___Block_byref_object_copy_.11480
- ___Block_byref_object_copy_.12174
- ___Block_byref_object_copy_.12338
- ___Block_byref_object_copy_.5713
- ___Block_byref_object_copy_.7556
- ___Block_byref_object_copy_.7975
- ___Block_byref_object_copy_.9085
- ___Block_byref_object_dispose_.10046
- ___Block_byref_object_dispose_.10789
- ___Block_byref_object_dispose_.11481
- ___Block_byref_object_dispose_.12175
- ___Block_byref_object_dispose_.12339
- ___Block_byref_object_dispose_.5714
- ___Block_byref_object_dispose_.7557
- ___Block_byref_object_dispose_.7976
- ___Block_byref_object_dispose_.9086
- ___block_descriptor_138_e8_32s40s48s56s64s72s80bs88r96r104r112r120r_e5_v8?0lr88l8s32l8s40l8r96l8r104l8s48l8r112l8s56l8r120l8s64l8s80l8s72l8
- ___block_descriptor_56_e8_32bs40r48r_e5_v8?0ls32l8r40l8r48l8
- ___block_descriptor_64_e8_32s40r48r56r_e40_v16?0"HAPCharacteristicResponseTuple"8lr40l8r48l8r56l8s32l8
- ___block_descriptor_73_e8_32s40s48s56bs64r_e29_v24?0"NSArray"8"NSError"16lr64l8s32l8s56l8s40l8s48l8
- ___block_descriptor_80_e8_32s40s48r56r64r72r_e5_v8?0lr48l8r56l8s32l8r64l8r72l8s40l8
- ___block_literal_global.10526
- ___block_literal_global.11078
- ___block_literal_global.11303
- ___block_literal_global.11515
- ___block_literal_global.11653
- ___block_literal_global.11782
- ___block_literal_global.11999
- ___block_literal_global.303.9042
- ___block_literal_global.5430
- ___block_literal_global.5602
- ___block_literal_global.5840
- ___block_literal_global.5970
- ___block_literal_global.6111
- ___block_literal_global.6220
- ___block_literal_global.6254
- ___block_literal_global.6275
- ___block_literal_global.6525
- ___block_literal_global.6538
- ___block_literal_global.6632
- ___block_literal_global.6726
- ___block_literal_global.6820
- ___block_literal_global.6923
- ___block_literal_global.7017
- ___block_literal_global.7111
- ___block_literal_global.7252
- ___block_literal_global.7357
- ___block_literal_global.7426
- ___block_literal_global.75.9842
- ___block_literal_global.768
- ___block_literal_global.775
- ___block_literal_global.7758
- ___block_literal_global.7986
- ___block_literal_global.8319
- ___block_literal_global.8443
- ___block_literal_global.8576
- ___block_literal_global.9117
- ___block_literal_global.9521
- ___block_literal_global.958
- ___block_literal_global.9841
- ___block_literal_global.9917
- _logCategory._hmf_once_t0.5601
- _logCategory._hmf_once_t0.6253
- _logCategory._hmf_once_t14.6537
- _logCategory._hmf_once_t14.6631
- _logCategory._hmf_once_t14.6725
- _logCategory._hmf_once_t14.6922
- _logCategory._hmf_once_t14.7016
- _logCategory._hmf_once_t14.7110
- _logCategory._hmf_once_t2.6219
- _logCategory._hmf_once_t2.7251
- _logCategory._hmf_once_t2.9916
- _logCategory._hmf_once_t20.11652
- _logCategory._hmf_once_t26.6819
- _logCategory._hmf_once_t31.11781
- _logCategory._hmf_once_t4.7356
- _logCategory._hmf_once_t65
- _logCategory._hmf_once_t671
- _logCategory._hmf_once_t8.11302
- _logCategory._hmf_once_t8.8442
- _logCategory._hmf_once_t9.5969
- _logCategory._hmf_once_v1.5603
- _logCategory._hmf_once_v1.6255
- _logCategory._hmf_once_v10.5971
- _logCategory._hmf_once_v15.6539
- _logCategory._hmf_once_v15.6633
- _logCategory._hmf_once_v15.6727
- _logCategory._hmf_once_v15.6924
- _logCategory._hmf_once_v15.7018
- _logCategory._hmf_once_v15.7112
- _logCategory._hmf_once_v21.11654
- _logCategory._hmf_once_v27.6821
- _logCategory._hmf_once_v3.6221
- _logCategory._hmf_once_v3.7253
- _logCategory._hmf_once_v3.9918
- _logCategory._hmf_once_v32.11783
- _logCategory._hmf_once_v5.7358
- _logCategory._hmf_once_v66
- _logCategory._hmf_once_v672
- _logCategory._hmf_once_v9.11304
- _logCategory._hmf_once_v9.8444
CStrings:
+ "%{public}@Cache read didn't succeed for all requests (%lu)"
+ "%{public}@Counter =  %ld, reached its max (%ld) in last %llu hours"
+ "%{public}@Counter incremented to %ld"
+ "%{public}@Counter manually reset"
+ "%{public}@Counter reset due to timeout"
+ "%{public}@First use: Counter started at %f"
+ "%{public}@Updating delay with exponential backoff to %.0f seconds"
+ "%{public}@abortAllLowPriorityOperationsWithReason for fabric: %@ - fabricRequests is not low priority only, letting idle timer expire normally"
+ "%{public}@abortAllLowPriorityOperationsWithReason for fabric: %@ - marking as complete, only had low priority requests"
+ "%{public}@readCharacteristicValueFromCache(%lu) response: %@"
+ "%{public}@readCharacteristicValues(%lu) response:%@, error:%@"
+ "@\"HMMTRTimeBasedCounter\""
+ "@\"NSArray\"16@?0@\"NSArray\"8"
+ "@16@?0@\"HMMTRHAPServiceDescription\"8"
+ "B24@0:8d16"
+ "HMMTRTimeBasedCounter"
+ "T@\"<HMMTROperationalCertificateIssuerRemoteDelegate>\",R"
+ "T@\"HMMTRTimeBasedCounter\",&,V_notAvailableImageResponseCounter"
+ "T@,R,W,N,V_context"
+ "TB,V_hasOnlyQueuedLowPriorityRequests"
+ "TQ,N,V_count"
+ "TQ,N,V_threshold"
+ "TQ,V_busyImageResponseCounter"
+ "Td,N,V_startTime"
+ "_busyImageResponseCounter"
+ "_count"
+ "_hasOnlyQueuedLowPriorityRequests"
+ "_notAvailableImageResponseCounter"
+ "_startNewCountingPeriod:"
+ "_threshold"
+ "_timeBasedCounterlock"
+ "abortAllLowPriorityOperationsWithReason:"
+ "busyImageResponseCounter"
+ "d"
+ "handleBusyImageResponseCounter"
+ "handleNotAvailableImageResponseCounter"
+ "hasOnlyQueuedLowPriorityRequests"
+ "incrementOrReset"
+ "initTimeBasedCounter:"
+ "notAvailableImageResponseCounter"
+ "notifyOperationsCompleted:"
+ "q24@?0@\"HAPCharacteristicWriteRequestTuple\"8@\"HAPCharacteristicWriteRequestTuple\"16"
+ "resetNonAvailableCounters"
+ "resetTimeBasedCounter"
+ "setBusyImageResponseCounter:"
+ "setCount:"
+ "setHasOnlyQueuedLowPriorityRequests:"
+ "setNotAvailableImageResponseCounter:"
+ "setThreshold:"
+ "threshold"
+ "{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}"
+ "\xf0\x82\xf0\xf0\xc1\xc1"
- "%{public}@Cache read didn't succeed for all requests."
- "T@,R,N,V_context"
- "\xf0\x82\xf0\xf0\xa1\xc1"

```
