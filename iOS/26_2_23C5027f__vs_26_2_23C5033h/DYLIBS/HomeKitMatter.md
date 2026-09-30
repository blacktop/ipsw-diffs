## HomeKitMatter

> `/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter`

```diff

-1388.3.1.0.2
-  __TEXT.__text: 0x1440cc
+1388.3.4.0.0
+  __TEXT.__text: 0x146378
   __TEXT.__auth_stubs: 0xaa0
-  __TEXT.__objc_methlist: 0xa714
+  __TEXT.__objc_methlist: 0xa964
   __TEXT.__const: 0x180
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__gcc_except_tab: 0x2d84
-  __TEXT.__cstring: 0x6c24
-  __TEXT.__oslogstring: 0x28654
+  __TEXT.__gcc_except_tab: 0x2d98
+  __TEXT.__cstring: 0x6e77
+  __TEXT.__oslogstring: 0x28d8c
   __TEXT.__ustring: 0x68
-  __TEXT.__unwind_info: 0x2f28
-  __TEXT.__objc_classname: 0x1474
-  __TEXT.__objc_methname: 0x2634c
-  __TEXT.__objc_methtype: 0x3db6
-  __TEXT.__objc_stubs: 0x168c0
-  __DATA_CONST.__got: 0x9d0
-  __DATA_CONST.__const: 0x4860
-  __DATA_CONST.__objc_classlist: 0x428
+  __TEXT.__unwind_info: 0x2f90
+  __TEXT.__objc_classname: 0x14b2
+  __TEXT.__objc_methname: 0x26944
+  __TEXT.__objc_methtype: 0x3e7a
+  __TEXT.__objc_stubs: 0x16dc0
+  __DATA_CONST.__got: 0x9e0
+  __DATA_CONST.__const: 0x48d0
+  __DATA_CONST.__objc_classlist: 0x438
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6da0
+  __DATA_CONST.__objc_selrefs: 0x6ef0
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x2e8
+  __DATA_CONST.__objc_superrefs: 0x2f8
   __DATA_CONST.__objc_arraydata: 0x248
   __AUTH_CONST.__auth_got: 0x560
-  __AUTH_CONST.__const: 0x10c0
-  __AUTH_CONST.__cfstring: 0x6c20
-  __AUTH_CONST.__objc_const: 0xf838
+  __AUTH_CONST.__const: 0x10e0
+  __AUTH_CONST.__cfstring: 0x6e00
+  __AUTH_CONST.__objc_const: 0xfbe0
   __AUTH_CONST.__objc_intobj: 0x1818
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x1e00
-  __DATA.__objc_ivar: 0xaf4
+  __AUTH.__objc_data: 0x1ea0
+  __DATA.__objc_ivar: 0xb20
   __DATA.__data: 0xde0
-  __DATA.__bss: 0x438
+  __DATA.__bss: 0x470
   __DATA_DIRTY.__objc_data: 0xb90
-  __DATA_DIRTY.__bss: 0xc8
+  __DATA_DIRTY.__bss: 0xb8
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/UARPKit.framework/UARPKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 23F440C2-DD73-3C1B-83CB-A6A1BC3C8CB7
-  Functions: 4307
-  Symbols:   14869
-  CStrings:  9584
+  UUID: 33E19332-B787-3434-830C-76A15C293C54
+  Functions: 4356
+  Symbols:   15042
+  CStrings:  9706
 
Symbols:
+ +[HMMTRAnnounceOtaSchedulerTimer logCategory]
+ -[HMMTRAccessoryServer _cleanupAnnounceOtaProviderSchedulerTimer]
+ -[HMMTRAccessoryServer activeAnnounceOtaSchedulerTimer]
+ -[HMMTRAccessoryServer announceOtaQueue]
+ -[HMMTRAccessoryServer hasOtaProviderSchedulerTimer]
+ -[HMMTRAccessoryServer matchedSetupPayload]
+ -[HMMTRAccessoryServer scheduleOrExecuteOTAProviderAnnouncement:initiatorType:immediateAnnouncement:endpoint:delayCounter:isUserTriggered:]
+ -[HMMTRAccessoryServer setActiveAnnounceOtaSchedulerTimer:]
+ -[HMMTRAccessoryServer setMatchedSetupPayload:]
+ -[HMMTRAccessoryServer startOtaProviderSchedulerTimer:endpoint:queue:]
+ -[HMMTRAccessoryServer stopOtaProviderSchedulerTimer]
+ -[HMMTRAccessoryServerBrowser announceOtaProviderForNodeID:isRetry:isUserTriggered:timeZone:]
+ -[HMMTRAnnounceOtaScheduler .cxx_destruct]
+ -[HMMTRAnnounceOtaScheduler _currentTimeComponents]
+ -[HMMTRAnnounceOtaScheduler _getSoftwareInstallingWindowBeginHour]
+ -[HMMTRAnnounceOtaScheduler _getSoftwareInstallingWindowBeginMinute]
+ -[HMMTRAnnounceOtaScheduler _getSoftwareInstallingWindowBeginSecond]
+ -[HMMTRAnnounceOtaScheduler _getSoftwareInstallingWindowEndHour]
+ -[HMMTRAnnounceOtaScheduler _getSoftwareInstallingWindowEndMinute]
+ -[HMMTRAnnounceOtaScheduler _getSoftwareInstallingWindowEndSecond]
+ -[HMMTRAnnounceOtaScheduler _homeCalendar]
+ -[HMMTRAnnounceOtaScheduler _isWithinUpdateTimeWindowForComponents:windowBegin:windowEnd:]
+ -[HMMTRAnnounceOtaScheduler _secondsSinceMidnightForHour:minute:second:]
+ -[HMMTRAnnounceOtaScheduler _secondsUntilInstallationWindowBeginForComponents:targetDateTime:]
+ -[HMMTRAnnounceOtaScheduler calendar]
+ -[HMMTRAnnounceOtaScheduler homeTimeZone]
+ -[HMMTRAnnounceOtaScheduler init:]
+ -[HMMTRAnnounceOtaScheduler isWithinUpdateTimeWindow]
+ -[HMMTRAnnounceOtaScheduler secondsUntilInstallationWindowBegin]
+ -[HMMTRAnnounceOtaScheduler setCalendar:]
+ -[HMMTRAnnounceOtaSchedulerTimer .cxx_destruct]
+ -[HMMTRAnnounceOtaSchedulerTimer endpoint]
+ -[HMMTRAnnounceOtaSchedulerTimer init:server:nodeID:endpoint:queue:]
+ -[HMMTRAnnounceOtaSchedulerTimer logIdentifier]
+ -[HMMTRAnnounceOtaSchedulerTimer nodeID]
+ -[HMMTRAnnounceOtaSchedulerTimer queue]
+ -[HMMTRAnnounceOtaSchedulerTimer server]
+ -[HMMTRAnnounceOtaSchedulerTimer setEndpoint:]
+ -[HMMTRAnnounceOtaSchedulerTimer setNodeID:]
+ -[HMMTRAnnounceOtaSchedulerTimer setQueue:]
+ -[HMMTRAnnounceOtaSchedulerTimer setServer:]
+ -[HMMTRAnnounceOtaSchedulerTimer setTimeInterval:]
+ -[HMMTRAnnounceOtaSchedulerTimer setUpdateTimer:]
+ -[HMMTRAnnounceOtaSchedulerTimer start]
+ -[HMMTRAnnounceOtaSchedulerTimer stop]
+ -[HMMTRAnnounceOtaSchedulerTimer timeInterval]
+ -[HMMTRAnnounceOtaSchedulerTimer timerDidFire:]
+ -[HMMTRAnnounceOtaSchedulerTimer updateTimer]
+ -[HMMTRSoftwareUpdateProvider notifyUpdateRequestedForNodeID:isUserTriggered:isRetry:timeZone:]
+ GCC_except_table1029
+ GCC_except_table1033
+ GCC_except_table1035
+ GCC_except_table1162
+ GCC_except_table1222
+ GCC_except_table1268
+ GCC_except_table1276
+ GCC_except_table1325
+ GCC_except_table1333
+ GCC_except_table1370
+ GCC_except_table1407
+ GCC_except_table1436
+ GCC_except_table1632
+ GCC_except_table1673
+ GCC_except_table1825
+ GCC_except_table1826
+ GCC_except_table1827
+ GCC_except_table1830
+ GCC_except_table1850
+ GCC_except_table1851
+ GCC_except_table1852
+ GCC_except_table1853
+ GCC_except_table1854
+ GCC_except_table1857
+ GCC_except_table1860
+ GCC_except_table1861
+ GCC_except_table1862
+ GCC_except_table1863
+ GCC_except_table1864
+ GCC_except_table1865
+ GCC_except_table1866
+ GCC_except_table1925
+ GCC_except_table1931
+ GCC_except_table1969
+ GCC_except_table2044
+ GCC_except_table2156
+ GCC_except_table2158
+ GCC_except_table2188
+ GCC_except_table2196
+ GCC_except_table2198
+ GCC_except_table2242
+ GCC_except_table2282
+ GCC_except_table2344
+ GCC_except_table2611
+ GCC_except_table2615
+ GCC_except_table2669
+ GCC_except_table2710
+ GCC_except_table2751
+ GCC_except_table2753
+ GCC_except_table2778
+ GCC_except_table2779
+ GCC_except_table2780
+ GCC_except_table2802
+ GCC_except_table2803
+ GCC_except_table2804
+ GCC_except_table2805
+ GCC_except_table2807
+ GCC_except_table2808
+ GCC_except_table2809
+ GCC_except_table2821
+ GCC_except_table2823
+ GCC_except_table2858
+ GCC_except_table2875
+ GCC_except_table2878
+ GCC_except_table2882
+ GCC_except_table2897
+ GCC_except_table2904
+ GCC_except_table2906
+ GCC_except_table2925
+ GCC_except_table2931
+ GCC_except_table2936
+ GCC_except_table2948
+ GCC_except_table2999
+ GCC_except_table3000
+ GCC_except_table3377
+ GCC_except_table3378
+ GCC_except_table3379
+ GCC_except_table3383
+ GCC_except_table3388
+ GCC_except_table3391
+ GCC_except_table3407
+ GCC_except_table3422
+ GCC_except_table3490
+ GCC_except_table3498
+ GCC_except_table3500
+ GCC_except_table3507
+ GCC_except_table3508
+ GCC_except_table3568
+ GCC_except_table3571
+ GCC_except_table3579
+ GCC_except_table3598
+ GCC_except_table3639
+ GCC_except_table3643
+ GCC_except_table3660
+ GCC_except_table3662
+ GCC_except_table3680
+ GCC_except_table3757
+ GCC_except_table3804
+ GCC_except_table3822
+ GCC_except_table3845
+ GCC_except_table3849
+ GCC_except_table3864
+ GCC_except_table3865
+ GCC_except_table3866
+ GCC_except_table3872
+ GCC_except_table3879
+ GCC_except_table3937
+ GCC_except_table3957
+ GCC_except_table4018
+ GCC_except_table4023
+ GCC_except_table4026
+ GCC_except_table4109
+ GCC_except_table4110
+ GCC_except_table4165
+ GCC_except_table4168
+ GCC_except_table4230
+ GCC_except_table4292
+ GCC_except_table4296
+ GCC_except_table4300
+ GCC_except_table4303
+ GCC_except_table4336
+ GCC_except_table902
+ GCC_except_table965
+ GCC_except_table969
+ GCC_except_table971
+ GCC_except_table973
+ GCC_except_table975
+ GCC_except_table979
+ GCC_except_table983
+ GCC_except_table986
+ _HMMTRAnnounceOtaTimerInitatorTypeAsString
+ _OBJC_CLASS_$_HMMTRAnnounceOtaScheduler
+ _OBJC_CLASS_$_HMMTRAnnounceOtaSchedulerTimer
+ _OBJC_CLASS_$_NSDateComponents
+ _OBJC_IVAR_$_HMMTRAccessoryServer._activeAnnounceOtaSchedulerTimer
+ _OBJC_IVAR_$_HMMTRAccessoryServer._announceOtaQueue
+ _OBJC_IVAR_$_HMMTRAccessoryServer._matchedSetupPayload
+ _OBJC_IVAR_$_HMMTRAnnounceOtaScheduler._calendar
+ _OBJC_IVAR_$_HMMTRAnnounceOtaScheduler._homeTimeZone
+ _OBJC_IVAR_$_HMMTRAnnounceOtaSchedulerTimer._endpoint
+ _OBJC_IVAR_$_HMMTRAnnounceOtaSchedulerTimer._nodeID
+ _OBJC_IVAR_$_HMMTRAnnounceOtaSchedulerTimer._queue
+ _OBJC_IVAR_$_HMMTRAnnounceOtaSchedulerTimer._server
+ _OBJC_IVAR_$_HMMTRAnnounceOtaSchedulerTimer._timeInterval
+ _OBJC_IVAR_$_HMMTRAnnounceOtaSchedulerTimer._updateTimer
+ _OBJC_METACLASS_$_HMMTRAnnounceOtaScheduler
+ _OBJC_METACLASS_$_HMMTRAnnounceOtaSchedulerTimer
+ __OBJC_$_CLASS_METHODS_HMMTRAnnounceOtaSchedulerTimer
+ __OBJC_$_INSTANCE_METHODS_HMMTRAnnounceOtaScheduler
+ __OBJC_$_INSTANCE_METHODS_HMMTRAnnounceOtaSchedulerTimer
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRAnnounceOtaScheduler
+ __OBJC_$_INSTANCE_VARIABLES_HMMTRAnnounceOtaSchedulerTimer
+ __OBJC_$_PROP_LIST_HMMTRAnnounceOtaScheduler
+ __OBJC_$_PROP_LIST_HMMTRAnnounceOtaSchedulerTimer
+ __OBJC_CLASS_PROTOCOLS_$_HMMTRAnnounceOtaSchedulerTimer
+ __OBJC_CLASS_RO_$_HMMTRAnnounceOtaScheduler
+ __OBJC_CLASS_RO_$_HMMTRAnnounceOtaSchedulerTimer
+ __OBJC_METACLASS_RO_$_HMMTRAnnounceOtaScheduler
+ __OBJC_METACLASS_RO_$_HMMTRAnnounceOtaSchedulerTimer
+ ___101-[HMMTRAccessoryServer updateAccessoryControlToIncludeAdministratorNodes:sharedUserNodes:completion:]_block_invoke.862
+ ___102-[HMMTRAccessoryServer updateAllCharacteristicValuesPostHAPServiceEnumerationForAccessory:completion:]_block_invoke.810
+ ___112-[HMMTRAccessoryServer _updateAdditionalCharacteristicsFromCharacteristicUpdate:service:path:completionHandler:]_block_invoke.401
+ ___114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke.921
+ ___114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke.924
+ ___117-[HMMTRAccessoryServer _findSystemCommissionerPairingMatchingSetupPayload:systemCommissionerPairings:pairingManager:]_block_invoke.281
+ ___117-[HMMTRAccessoryServer _findSystemCommissionerPairingMatchingSetupPayload:systemCommissionerPairings:pairingManager:]_block_invoke.282
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.535
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.536
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.537
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.538
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.539
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.540
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.541
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.543
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.545
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.542
+ ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.544
+ ___139-[HMMTRAccessoryServer scheduleOrExecuteOTAProviderAnnouncement:initiatorType:immediateAnnouncement:endpoint:delayCounter:isUserTriggered:]_block_invoke
+ ___139-[HMMTRAccessoryServer scheduleOrExecuteOTAProviderAnnouncement:initiatorType:immediateAnnouncement:endpoint:delayCounter:isUserTriggered:]_block_invoke.488
+ ___37-[HMMTRAccessoryServer finishPairing]_block_invoke.790
+ ___37-[HMMTRAccessoryServer timerDidFire:]_block_invoke.298
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.665
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.666
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.667
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.668
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.670
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.674
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.675
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.676
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.677
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.669
+ ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.678
+ ___42-[HMMTRAccessoryServer _setupMatterDevice]_block_invoke.329
+ ___43-[HMMTRAccessoryServer _setupThreadPairing]_block_invoke.497
+ ___43-[HMMTRAccessoryServer _unpair:completion:]_block_invoke.321
+ ___43-[HMMTRAccessoryServer discoverAccessories]_block_invoke.324
+ ___45+[HMMTRAnnounceOtaSchedulerTimer logCategory]_block_invoke
+ ___47-[HMMTRAccessoryServer processAttributeReport:]_block_invoke.990
+ ___47-[HMMTRAnnounceOtaSchedulerTimer timerDidFire:]_block_invoke
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.886
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.889
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.891
+ ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke_2.890
+ ___51-[HMMTRAccessoryServer device:receivedEventReport:]_block_invoke.991
+ ___52-[HMMTRAccessoryServer populateACLEntriesForPairing]_block_invoke.663
+ ___53-[HMMTRAccessoryServer _tryPairingUsingMatterSupport]_block_invoke.275
+ ___55-[HMMTRAccessoryServer device:receivedAttributeReport:]_block_invoke.989
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.445
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.446
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.447
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.448
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.449
+ ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.450
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.457
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.458
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.459
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.461
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.462
+ ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.463
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.926
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.928
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.932
+ ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.934
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.451
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.452
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.453
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.454
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.455
+ ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.456
+ ___63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.840
+ ___63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.841
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.515
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.516
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.517
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.518
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.519
+ ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.520
+ ___64-[HMMTRAccessoryServer _commissioning:complete:abstractMetrics:]_block_invoke.949
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.475
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.476
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.477
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.478
+ ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.479
+ ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.954
+ ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.955
+ ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.956
+ ___65-[HMMTRAccessoryServer stopPairingWithError:metricsReadyHandler:]_block_invoke.310
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.470
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.471
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.472
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.473
+ ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.474
+ ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.464
+ ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.465
+ ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.466
+ ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.469
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.504
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.505
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.506
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.509
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.513
+ ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.514
+ ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.437
+ ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.442
+ ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.443
+ ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.444
+ ___70-[HMMTRAccessoryServer _onThreadScanResults:commissioning:completion:]_block_invoke.898
+ ___70-[HMMTRAccessoryServer _onThreadScanResults:commissioning:completion:]_block_invoke.899
+ ___71-[HMMTRAccessoryServer validateAttestationDeviceInfo:error:completion:]_block_invoke.300
+ ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.422
+ ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.428
+ ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.429
+ ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.430
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.498
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.499
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.500
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.502
+ ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.503
+ ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.287
+ ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.288
+ ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.289
+ ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.290
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.834
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.835
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.838
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.839
+ ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke_2.836
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.812
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.821
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.829
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.830
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.832
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.833
+ ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke_2.825
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.313
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.314
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.315
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.317
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.318
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.316
+ ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.319
+ ___82-[HMMTRAccessoryServer fetchColorControlClusterForHapAccessory:completionHandler:]_block_invoke.935
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.903
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.904
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.905
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.908
+ ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke_2.907
+ ___83-[HMMTRAccessoryServer updateAccessoryControlToRemoveAdministratorNode:completion:]_block_invoke.863
+ ___84-[HMMTRAccessoryServer _queueOpenPairingWindowWithPINForDuration:completionHandler:]_block_invoke.431
+ ___84-[HMMTRAccessoryServer _queueOpenPairingWindowWithPINForDuration:completionHandler:]_block_invoke.432
+ ___84-[HMMTRAccessoryServer _queueOpenPairingWindowWithPINForDuration:completionHandler:]_block_invoke.433
+ ___84-[HMMTRAccessoryServer _queueOpenPairingWindowWithPINForDuration:completionHandler:]_block_invoke.435
+ ___84-[HMMTRAccessoryServer _queueOpenPairingWindowWithPINForDuration:completionHandler:]_block_invoke.436
+ ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.408
+ ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.410
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.909
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.910
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.911
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.912
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.916
+ ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.917
+ ___86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.957
+ ___86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.958
+ ___92-[HMMTRAccessoryServer _createFirmwareUpdateServiceWithInstanceID:device:completionHandler:]_block_invoke.803
+ ___94-[HMMTRAccessoryServer updateAccessoryControlToAdministratorNodes:sharedUserNodes:completion:]_block_invoke.861
+ ___95-[HMMTRSoftwareUpdateProvider notifyUpdateRequestedForNodeID:isUserTriggered:isRetry:timeZone:]_block_invoke
+ ___99-[HMMTRAccessoryServer _tryPairingWithOnboardingPayload:systemCommissionerPairings:pairingManager:]_block_invoke.278
+ ___99-[HMMTRAccessoryServer _tryPairingWithOnboardingPayload:systemCommissionerPairings:pairingManager:]_block_invoke.279
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.546
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.547
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.548
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.549
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.554
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.555
+ ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke_2.550
+ ___Block_byref_object_copy_.10661
+ ___Block_byref_object_copy_.11420
+ ___Block_byref_object_copy_.12047
+ ___Block_byref_object_copy_.12751
+ ___Block_byref_object_copy_.12918
+ ___Block_byref_object_copy_.2066
+ ___Block_byref_object_copy_.3553
+ ___Block_byref_object_copy_.3841
+ ___Block_byref_object_copy_.4920
+ ___Block_byref_object_copy_.6090
+ ___Block_byref_object_copy_.6241
+ ___Block_byref_object_copy_.8057
+ ___Block_byref_object_copy_.8490
+ ___Block_byref_object_copy_.9700
+ ___Block_byref_object_dispose_.10662
+ ___Block_byref_object_dispose_.11421
+ ___Block_byref_object_dispose_.12048
+ ___Block_byref_object_dispose_.12752
+ ___Block_byref_object_dispose_.12919
+ ___Block_byref_object_dispose_.2067
+ ___Block_byref_object_dispose_.3554
+ ___Block_byref_object_dispose_.3842
+ ___Block_byref_object_dispose_.4921
+ ___Block_byref_object_dispose_.6091
+ ___Block_byref_object_dispose_.6242
+ ___Block_byref_object_dispose_.8058
+ ___Block_byref_object_dispose_.8491
+ ___Block_byref_object_dispose_.9701
+ ___block_descriptor_48_e8_32s40w_e68_v24?0"HMMTRSoftwareUpdateProviderQueryResponseParams"8"NSError"16lw40l8s32l8
+ ___block_descriptor_65_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_66_e8_32s40s48s56s_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8
+ ___block_literal_global.10136
+ ___block_literal_global.10460
+ ___block_literal_global.10536
+ ___block_literal_global.11149
+ ___block_literal_global.11866
+ ___block_literal_global.12081
+ ___block_literal_global.12217
+ ___block_literal_global.12349
+ ___block_literal_global.12568
+ ___block_literal_global.1575
+ ___block_literal_global.1667
+ ___block_literal_global.1915
+ ___block_literal_global.2189
+ ___block_literal_global.2244
+ ___block_literal_global.2291
+ ___block_literal_global.2378
+ ___block_literal_global.2738
+ ___block_literal_global.2862
+ ___block_literal_global.3012
+ ___block_literal_global.3314
+ ___block_literal_global.3458
+ ___block_literal_global.3487
+ ___block_literal_global.3579
+ ___block_literal_global.3733
+ ___block_literal_global.3930
+ ___block_literal_global.4081
+ ___block_literal_global.4203
+ ___block_literal_global.4689
+ ___block_literal_global.5017
+ ___block_literal_global.5305
+ ___block_literal_global.5439
+ ___block_literal_global.553
+ ___block_literal_global.5541
+ ___block_literal_global.5805
+ ___block_literal_global.5978
+ ___block_literal_global.6225
+ ___block_literal_global.6413
+ ___block_literal_global.6553
+ ___block_literal_global.6662
+ ___block_literal_global.6696
+ ___block_literal_global.6717
+ ___block_literal_global.6967
+ ___block_literal_global.6980
+ ___block_literal_global.7074
+ ___block_literal_global.7168
+ ___block_literal_global.7262
+ ___block_literal_global.7365
+ ___block_literal_global.7459
+ ___block_literal_global.7598
+ ___block_literal_global.7739
+ ___block_literal_global.7845
+ ___block_literal_global.7923
+ ___block_literal_global.808
+ ___block_literal_global.815
+ ___block_literal_global.82.10461
+ ___block_literal_global.824
+ ___block_literal_global.8273
+ ___block_literal_global.828
+ ___block_literal_global.8501
+ ___block_literal_global.8849
+ ___block_literal_global.8966
+ ___block_literal_global.9102
+ ___block_literal_global.9731
+ ___block_literal_global.998
+ __windowBeginSeconds
+ __windowBoundariesInitialized
+ __windowEndSeconds
+ _logCategory._hmf_once_t0.2243
+ _logCategory._hmf_once_t0.3457
+ _logCategory._hmf_once_t0.5977
+ _logCategory._hmf_once_t0.6695
+ _logCategory._hmf_once_t10.12567
+ _logCategory._hmf_once_t10.1516
+ _logCategory._hmf_once_t13.3578
+ _logCategory._hmf_once_t13.3929
+ _logCategory._hmf_once_t14.6979
+ _logCategory._hmf_once_t14.7073
+ _logCategory._hmf_once_t14.7167
+ _logCategory._hmf_once_t14.7364
+ _logCategory._hmf_once_t14.7458
+ _logCategory._hmf_once_t14.7597
+ _logCategory._hmf_once_t2.10535
+ _logCategory._hmf_once_t2.5540
+ _logCategory._hmf_once_t2.6661
+ _logCategory._hmf_once_t2.7738
+ _logCategory._hmf_once_t20.12216
+ _logCategory._hmf_once_t26.7261
+ _logCategory._hmf_once_t3.1574
+ _logCategory._hmf_once_t31.12348
+ _logCategory._hmf_once_t368
+ _logCategory._hmf_once_t4.4080
+ _logCategory._hmf_once_t4.7844
+ _logCategory._hmf_once_t40.6287
+ _logCategory._hmf_once_t5
+ _logCategory._hmf_once_t6.2377
+ _logCategory._hmf_once_t6.4202
+ _logCategory._hmf_once_t678
+ _logCategory._hmf_once_t68.12777
+ _logCategory._hmf_once_t8.11865
+ _logCategory._hmf_once_v1.2245
+ _logCategory._hmf_once_v1.3459
+ _logCategory._hmf_once_v1.5979
+ _logCategory._hmf_once_v1.6697
+ _logCategory._hmf_once_v11.12569
+ _logCategory._hmf_once_v11.1518
+ _logCategory._hmf_once_v14.3580
+ _logCategory._hmf_once_v14.3931
+ _logCategory._hmf_once_v15.6981
+ _logCategory._hmf_once_v15.7075
+ _logCategory._hmf_once_v15.7169
+ _logCategory._hmf_once_v15.7366
+ _logCategory._hmf_once_v15.7460
+ _logCategory._hmf_once_v15.7599
+ _logCategory._hmf_once_v21.12218
+ _logCategory._hmf_once_v27.7263
+ _logCategory._hmf_once_v3.10537
+ _logCategory._hmf_once_v3.5542
+ _logCategory._hmf_once_v3.6663
+ _logCategory._hmf_once_v3.7740
+ _logCategory._hmf_once_v32.12350
+ _logCategory._hmf_once_v369
+ _logCategory._hmf_once_v4.1576
+ _logCategory._hmf_once_v41.6288
+ _logCategory._hmf_once_v5.4082
+ _logCategory._hmf_once_v5.7846
+ _logCategory._hmf_once_v6
+ _logCategory._hmf_once_v679
+ _logCategory._hmf_once_v69.12778
+ _logCategory._hmf_once_v7.2379
+ _logCategory._hmf_once_v7.4204
+ _logCategory._hmf_once_v9.11867
+ _objc_msgSend$_cleanupAnnounceOtaProviderSchedulerTimer
+ _objc_msgSend$_currentTimeComponents
+ _objc_msgSend$_getSoftwareInstallingWindowBeginHour
+ _objc_msgSend$_getSoftwareInstallingWindowBeginMinute
+ _objc_msgSend$_getSoftwareInstallingWindowBeginSecond
+ _objc_msgSend$_getSoftwareInstallingWindowEndHour
+ _objc_msgSend$_getSoftwareInstallingWindowEndMinute
+ _objc_msgSend$_getSoftwareInstallingWindowEndSecond
+ _objc_msgSend$_homeCalendar
+ _objc_msgSend$_isWithinUpdateTimeWindowForComponents:windowBegin:windowEnd:
+ _objc_msgSend$_secondsSinceMidnightForHour:minute:second:
+ _objc_msgSend$_secondsUntilInstallationWindowBeginForComponents:targetDateTime:
+ _objc_msgSend$activeAnnounceOtaSchedulerTimer
+ _objc_msgSend$announceOtaProviderForNodeID:isRetry:isUserTriggered:timeZone:
+ _objc_msgSend$announceOtaQueue
+ _objc_msgSend$calendar
+ _objc_msgSend$currentCalendar
+ _objc_msgSend$dateByAddingUnit:value:toDate:options:
+ _objc_msgSend$day
+ _objc_msgSend$hasOtaProviderSchedulerTimer
+ _objc_msgSend$homeTimeZone
+ _objc_msgSend$hour
+ _objc_msgSend$init:
+ _objc_msgSend$init:server:nodeID:endpoint:queue:
+ _objc_msgSend$isWithinUpdateTimeWindow
+ _objc_msgSend$matchedPayload
+ _objc_msgSend$matchedSetupPayload
+ _objc_msgSend$minute
+ _objc_msgSend$month
+ _objc_msgSend$scheduleOrExecuteOTAProviderAnnouncement:initiatorType:immediateAnnouncement:endpoint:delayCounter:isUserTriggered:
+ _objc_msgSend$second
+ _objc_msgSend$secondsUntilInstallationWindowBegin
+ _objc_msgSend$setActiveAnnounceOtaSchedulerTimer:
+ _objc_msgSend$setDay:
+ _objc_msgSend$setMatchedSetupPayload:
+ _objc_msgSend$setMonth:
+ _objc_msgSend$setYear:
+ _objc_msgSend$startOtaProviderSchedulerTimer:endpoint:queue:
+ _objc_msgSend$stopOtaProviderSchedulerTimer
+ _objc_msgSend$systemTimeZone
+ _objc_msgSend$year
- -[HMMTRAccessoryServerBrowser announceOtaProviderForNodeID:isRetry:]
- -[HMMTRSoftwareUpdateProvider notifyUpdateRequestedForNodeID:isUserTriggered:isRetry:]
- GCC_except_table1030
- GCC_except_table1034
- GCC_except_table1036
- GCC_except_table1142
- GCC_except_table1202
- GCC_except_table1248
- GCC_except_table1256
- GCC_except_table1305
- GCC_except_table1313
- GCC_except_table1350
- GCC_except_table1387
- GCC_except_table1416
- GCC_except_table1613
- GCC_except_table1654
- GCC_except_table1806
- GCC_except_table1807
- GCC_except_table1808
- GCC_except_table1811
- GCC_except_table1831
- GCC_except_table1832
- GCC_except_table1833
- GCC_except_table1834
- GCC_except_table1835
- GCC_except_table1838
- GCC_except_table1841
- GCC_except_table1842
- GCC_except_table1843
- GCC_except_table1844
- GCC_except_table1845
- GCC_except_table1846
- GCC_except_table1847
- GCC_except_table1906
- GCC_except_table1912
- GCC_except_table1950
- GCC_except_table2025
- GCC_except_table2137
- GCC_except_table2139
- GCC_except_table2169
- GCC_except_table2177
- GCC_except_table2179
- GCC_except_table2223
- GCC_except_table2263
- GCC_except_table2325
- GCC_except_table2574
- GCC_except_table2578
- GCC_except_table2632
- GCC_except_table2673
- GCC_except_table2715
- GCC_except_table2717
- GCC_except_table2742
- GCC_except_table2743
- GCC_except_table2744
- GCC_except_table2766
- GCC_except_table2767
- GCC_except_table2768
- GCC_except_table2769
- GCC_except_table2770
- GCC_except_table2771
- GCC_except_table2772
- GCC_except_table2773
- GCC_except_table2785
- GCC_except_table2787
- GCC_except_table2822
- GCC_except_table2828
- GCC_except_table2839
- GCC_except_table2846
- GCC_except_table2861
- GCC_except_table2868
- GCC_except_table2870
- GCC_except_table2889
- GCC_except_table2895
- GCC_except_table2912
- GCC_except_table2963
- GCC_except_table2964
- GCC_except_table3336
- GCC_except_table3337
- GCC_except_table3338
- GCC_except_table3342
- GCC_except_table3347
- GCC_except_table3350
- GCC_except_table3365
- GCC_except_table3380
- GCC_except_table3448
- GCC_except_table3456
- GCC_except_table3458
- GCC_except_table3465
- GCC_except_table3466
- GCC_except_table3495
- GCC_except_table3526
- GCC_except_table3529
- GCC_except_table3556
- GCC_except_table3559
- GCC_except_table3597
- GCC_except_table3618
- GCC_except_table3620
- GCC_except_table3638
- GCC_except_table3708
- GCC_except_table3755
- GCC_except_table3773
- GCC_except_table3796
- GCC_except_table3800
- GCC_except_table3815
- GCC_except_table3816
- GCC_except_table3817
- GCC_except_table3823
- GCC_except_table3830
- GCC_except_table3888
- GCC_except_table3908
- GCC_except_table3969
- GCC_except_table3974
- GCC_except_table3977
- GCC_except_table4060
- GCC_except_table4061
- GCC_except_table4116
- GCC_except_table4119
- GCC_except_table4181
- GCC_except_table4243
- GCC_except_table4247
- GCC_except_table4251
- GCC_except_table4254
- GCC_except_table4287
- GCC_except_table903
- GCC_except_table966
- GCC_except_table970
- GCC_except_table972
- GCC_except_table974
- GCC_except_table976
- GCC_except_table980
- GCC_except_table984
- GCC_except_table987
- ___101-[HMMTRAccessoryServer updateAccessoryControlToIncludeAdministratorNodes:sharedUserNodes:completion:]_block_invoke.843
- ___102-[HMMTRAccessoryServer updateAllCharacteristicValuesPostHAPServiceEnumerationForAccessory:completion:]_block_invoke.791
- ___112-[HMMTRAccessoryServer _updateAdditionalCharacteristicsFromCharacteristicUpdate:service:path:completionHandler:]_block_invoke.385
- ___114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke.902
- ___114-[HMMTRAccessoryServer announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:]_block_invoke.905
- ___117-[HMMTRAccessoryServer _findSystemCommissionerPairingMatchingSetupPayload:systemCommissionerPairings:pairingManager:]_block_invoke.265
- ___117-[HMMTRAccessoryServer _findSystemCommissionerPairingMatchingSetupPayload:systemCommissionerPairings:pairingManager:]_block_invoke.266
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.510
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.511
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.512
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.513
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.514
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.515
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.516
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.518
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke.520
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.517
- ___119-[HMMTRAccessoryServer _readCharacteristicValues:timeout:skipCache:sendNotification:completionQueue:completionHandler:]_block_invoke_2.519
- ___37-[HMMTRAccessoryServer finishPairing]_block_invoke.771
- ___37-[HMMTRAccessoryServer timerDidFire:]_block_invoke.282
- ___38-[HMMTROTAAnnounceTimer timerDidFire:]_block_invoke.9
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.646
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.647
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.648
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.649
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.651
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.655
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.656
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.657
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke.658
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.650
- ___40-[HMMTRAccessoryServer _finalizePairing]_block_invoke_2.659
- ___42-[HMMTRAccessoryServer _setupMatterDevice]_block_invoke.313
- ___43-[HMMTRAccessoryServer _setupThreadPairing]_block_invoke.472
- ___43-[HMMTRAccessoryServer _unpair:completion:]_block_invoke.305
- ___43-[HMMTRAccessoryServer discoverAccessories]_block_invoke.308
- ___47-[HMMTRAccessoryServer processAttributeReport:]_block_invoke.971
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.867
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.870
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke.872
- ___49-[HMMTRAccessoryServer _prepareThreadCredentials]_block_invoke_2.871
- ___49-[HMMTRQueryImageResponseBusyTimer timerDidFire:]_block_invoke.4
- ___51-[HMMTRAccessoryServer device:receivedEventReport:]_block_invoke.972
- ___52-[HMMTRAccessoryServer populateACLEntriesForPairing]_block_invoke.644
- ___53-[HMMTRAccessoryServer _tryPairingUsingMatterSupport]_block_invoke.259
- ___55-[HMMTRAccessoryServer device:receivedAttributeReport:]_block_invoke.970
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.429
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.430
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.431
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.432
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.433
- ___56-[HMMTRAccessoryServer removePairing:completionHandler:]_block_invoke.434
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.441
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.442
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.443
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.445
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.446
- ___59-[HMMTRAccessoryServer fetchPairingsWithCompletionHandler:]_block_invoke.447
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.907
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.909
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.913
- ___60-[HMMTRAccessoryServer createDoorLockClusterObjectWithFlow:]_block_invoke.915
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.435
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.436
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.437
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.438
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.439
- ___60-[HMMTRAccessoryServer updateFabricLabel:completionHandler:]_block_invoke.440
- ___63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.821
- ___63-[HMMTRAccessoryServer _handlePairingFailureWithError:context:]_block_invoke.822
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.490
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.491
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.492
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.493
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.494
- ___63-[HMMTRAccessoryServer removeAllPairingsWithCompletionHandler:]_block_invoke.495
- ___64-[HMMTRAccessoryServer _commissioning:complete:abstractMetrics:]_block_invoke.930
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.459
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.460
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.461
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.462
- ___64-[HMMTRAccessoryServer _fetchSerialNumberWithCompletionHandler:]_block_invoke.463
- ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.935
- ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.936
- ___64-[HMMTRAccessoryServer refreshThreadCapabilitiesWithCompletion:]_block_invoke.937
- ___65-[HMMTRAccessoryServer stopPairingWithError:metricsReadyHandler:]_block_invoke.294
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.454
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.455
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.456
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.457
- ___66-[HMMTRAccessoryServer _fetchCurrentPairingWithCompletionHandler:]_block_invoke.458
- ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.448
- ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.449
- ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.450
- ___68-[HMMTRAccessoryServer fetchLastKnownPairingsWithCompletionHandler:]_block_invoke.453
- ___68-[HMMTRAccessoryServerBrowser announceOtaProviderForNodeID:isRetry:]_block_invoke
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.479
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.480
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.481
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.484
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.488
- ___69-[HMMTRAccessoryServer fetchExtendedMACAddressFromDevice:completion:]_block_invoke.489
- ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.421
- ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.426
- ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.427
- ___69-[HMMTRAccessoryServer readPairingWindowStatusWithCompletionHandler:]_block_invoke.428
- ___70-[HMMTRAccessoryServer _onThreadScanResults:commissioning:completion:]_block_invoke.879
- ___70-[HMMTRAccessoryServer _onThreadScanResults:commissioning:completion:]_block_invoke.880
- ___71-[HMMTRAccessoryServer validateAttestationDeviceInfo:error:completion:]_block_invoke.284
- ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.406
- ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.412
- ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.413
- ___72-[HMMTRAccessoryServer _openPairingWindowForDuration:completionHandler:]_block_invoke.414
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.473
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.474
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.475
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.477
- ___72-[HMMTRAccessoryServer fetchWEDSupportInformationFromDevice:completion:]_block_invoke.478
- ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.271
- ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.272
- ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.273
- ___72-[HMMTRAccessoryServer queueAccessoryOperation:highPriority:completion:]_block_invoke.274
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.815
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.816
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.819
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke.820
- ___73-[HMMTRAccessoryServer _buildHAPCategoriesFromCHIPWithCompletionHandler:]_block_invoke_2.817
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.792
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.793
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.802
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.810
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.813
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke.814
- ___73-[HMMTRAccessoryServer _rebuildHAPServicesFromCHIPWithCompletionHandler:]_block_invoke_2.806
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.297
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.298
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.299
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.301
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke.302
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.300
- ___76-[HMMTRAccessoryServer removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.303
- ___82-[HMMTRAccessoryServer fetchColorControlClusterForHapAccessory:completionHandler:]_block_invoke.916
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.884
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.885
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.886
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke.889
- ___82-[HMMTRAccessoryServer generateAccessoryConfigurationForReason:completionHandler:]_block_invoke_2.888
- ___83-[HMMTRAccessoryServer updateAccessoryControlToRemoveAdministratorNode:completion:]_block_invoke.844
- ___84-[HMMTRAccessoryServer _queueOpenPairingWindowWithPINForDuration:completionHandler:]_block_invoke.415
- ___84-[HMMTRAccessoryServer _queueOpenPairingWindowWithPINForDuration:completionHandler:]_block_invoke.416
- ___84-[HMMTRAccessoryServer _queueOpenPairingWindowWithPINForDuration:completionHandler:]_block_invoke.417
- ___84-[HMMTRAccessoryServer _queueOpenPairingWindowWithPINForDuration:completionHandler:]_block_invoke.419
- ___84-[HMMTRAccessoryServer _queueOpenPairingWindowWithPINForDuration:completionHandler:]_block_invoke.420
- ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.392
- ___84-[HMMTRAccessoryServer _updatedCharacteristicsForAttributeReport:completionHandler:]_block_invoke.394
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.890
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.891
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.892
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.893
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.897
- ___84-[HMMTRAccessoryServer updateDefaultOtaProvider:providerEndpoint:completionHandler:]_block_invoke.898
- ___86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.938
- ___86-[HMMTRAccessoryServer _fetchAdditionalThreadNetworkInformationFromDevice:completion:]_block_invoke.939
- ___86-[HMMTRSoftwareUpdateProvider notifyUpdateRequestedForNodeID:isUserTriggered:isRetry:]_block_invoke
- ___92-[HMMTRAccessoryServer _createFirmwareUpdateServiceWithInstanceID:device:completionHandler:]_block_invoke.784
- ___94-[HMMTRAccessoryServer updateAccessoryControlToAdministratorNodes:sharedUserNodes:completion:]_block_invoke.842
- ___99-[HMMTRAccessoryServer _tryPairingWithOnboardingPayload:systemCommissionerPairings:pairingManager:]_block_invoke.262
- ___99-[HMMTRAccessoryServer _tryPairingWithOnboardingPayload:systemCommissionerPairings:pairingManager:]_block_invoke.263
- ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.521
- ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.522
- ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.523
- ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.524
- ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.529
- ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke.530
- ___99-[HMMTRAccessoryServer writeCharacteristicValues:timeout:expiry:completionQueue:completionHandler:]_block_invoke_2.525
- ___Block_byref_object_copy_.10450
- ___Block_byref_object_copy_.11225
- ___Block_byref_object_copy_.11877
- ___Block_byref_object_copy_.12581
- ___Block_byref_object_copy_.12748
- ___Block_byref_object_copy_.2063
- ___Block_byref_object_copy_.3423
- ___Block_byref_object_copy_.3711
- ___Block_byref_object_copy_.4792
- ___Block_byref_object_copy_.5962
- ___Block_byref_object_copy_.6113
- ___Block_byref_object_copy_.7929
- ___Block_byref_object_copy_.8362
- ___Block_byref_object_copy_.9486
- ___Block_byref_object_dispose_.10451
- ___Block_byref_object_dispose_.11226
- ___Block_byref_object_dispose_.11878
- ___Block_byref_object_dispose_.12582
- ___Block_byref_object_dispose_.12749
- ___Block_byref_object_dispose_.2064
- ___Block_byref_object_dispose_.3424
- ___Block_byref_object_dispose_.3712
- ___Block_byref_object_dispose_.4793
- ___Block_byref_object_dispose_.5963
- ___Block_byref_object_dispose_.6114
- ___Block_byref_object_dispose_.7930
- ___Block_byref_object_dispose_.8363
- ___Block_byref_object_dispose_.9487
- ___block_descriptor_57_e8_32s40s48s_e17_v16?0"NSError"8ls32l8s40l8s48l8
- ___block_literal_global.10245
- ___block_literal_global.10321
- ___block_literal_global.10931
- ___block_literal_global.11526
- ___block_literal_global.11911
- ___block_literal_global.12047
- ___block_literal_global.12179
- ___block_literal_global.12398
- ___block_literal_global.1573
- ___block_literal_global.1665
- ___block_literal_global.1912
- ___block_literal_global.2187
- ___block_literal_global.2242
- ___block_literal_global.2289
- ___block_literal_global.2376
- ___block_literal_global.2737
- ___block_literal_global.2885
- ___block_literal_global.3183
- ___block_literal_global.3328
- ___block_literal_global.3357
- ___block_literal_global.3449
- ___block_literal_global.3603
- ___block_literal_global.3800
- ___block_literal_global.3951
- ___block_literal_global.4074
- ___block_literal_global.4561
- ___block_literal_global.4889
- ___block_literal_global.5177
- ___block_literal_global.528
- ___block_literal_global.5311
- ___block_literal_global.5413
- ___block_literal_global.5677
- ___block_literal_global.5850
- ___block_literal_global.6097
- ___block_literal_global.6285
- ___block_literal_global.6425
- ___block_literal_global.6534
- ___block_literal_global.6568
- ___block_literal_global.6589
- ___block_literal_global.6839
- ___block_literal_global.6852
- ___block_literal_global.6946
- ___block_literal_global.7040
- ___block_literal_global.7134
- ___block_literal_global.7237
- ___block_literal_global.7331
- ___block_literal_global.7470
- ___block_literal_global.7611
- ___block_literal_global.7717
- ___block_literal_global.7795
- ___block_literal_global.789
- ___block_literal_global.796
- ___block_literal_global.805
- ___block_literal_global.809
- ___block_literal_global.8145
- ___block_literal_global.82.10246
- ___block_literal_global.8373
- ___block_literal_global.8722
- ___block_literal_global.8840
- ___block_literal_global.8976
- ___block_literal_global.9517
- ___block_literal_global.979
- ___block_literal_global.9922
- _logCategory._hmf_once_t0.2241
- _logCategory._hmf_once_t0.3327
- _logCategory._hmf_once_t0.5849
- _logCategory._hmf_once_t0.6567
- _logCategory._hmf_once_t10.12397
- _logCategory._hmf_once_t11.3182
- _logCategory._hmf_once_t13.3448
- _logCategory._hmf_once_t13.3799
- _logCategory._hmf_once_t14.6851
- _logCategory._hmf_once_t14.6945
- _logCategory._hmf_once_t14.7039
- _logCategory._hmf_once_t14.7236
- _logCategory._hmf_once_t14.7330
- _logCategory._hmf_once_t14.7469
- _logCategory._hmf_once_t2.10320
- _logCategory._hmf_once_t2.5412
- _logCategory._hmf_once_t2.6533
- _logCategory._hmf_once_t2.7610
- _logCategory._hmf_once_t20.12046
- _logCategory._hmf_once_t26.7133
- _logCategory._hmf_once_t3.1572
- _logCategory._hmf_once_t31.12178
- _logCategory._hmf_once_t370
- _logCategory._hmf_once_t4.3950
- _logCategory._hmf_once_t4.7716
- _logCategory._hmf_once_t40.6159
- _logCategory._hmf_once_t6.2375
- _logCategory._hmf_once_t670
- _logCategory._hmf_once_t68.12607
- _logCategory._hmf_once_t8.11695
- _logCategory._hmf_once_t8.8839
- _logCategory._hmf_once_v1.2243
- _logCategory._hmf_once_v1.3329
- _logCategory._hmf_once_v1.5851
- _logCategory._hmf_once_v1.6569
- _logCategory._hmf_once_v11.12399
- _logCategory._hmf_once_v12.3184
- _logCategory._hmf_once_v14.3450
- _logCategory._hmf_once_v14.3801
- _logCategory._hmf_once_v15.6853
- _logCategory._hmf_once_v15.6947
- _logCategory._hmf_once_v15.7041
- _logCategory._hmf_once_v15.7238
- _logCategory._hmf_once_v15.7332
- _logCategory._hmf_once_v15.7471
- _logCategory._hmf_once_v21.12048
- _logCategory._hmf_once_v27.7135
- _logCategory._hmf_once_v3.10322
- _logCategory._hmf_once_v3.5414
- _logCategory._hmf_once_v3.6535
- _logCategory._hmf_once_v3.7612
- _logCategory._hmf_once_v32.12180
- _logCategory._hmf_once_v371
- _logCategory._hmf_once_v4.1574
- _logCategory._hmf_once_v41.6160
- _logCategory._hmf_once_v5.3952
- _logCategory._hmf_once_v5.7718
- _logCategory._hmf_once_v671
- _logCategory._hmf_once_v69.12608
- _logCategory._hmf_once_v7.2377
- _logCategory._hmf_once_v9.11697
- _logCategory._hmf_once_v9.8841
- _objc_msgSend$announceOtaProviderForNodeID:isRetry:
CStrings:
+ "%{public}@%@ - using device timezone as fallback"
+ "%{public}@Captured matched setup payload from commissioning operation"
+ "%{public}@Cleaning up announce ota Timer for nodeID: %@ during accessory server dealloc"
+ "%{public}@Current time %02ld:%02ld:%02ld %s within installation window %02ld:%02ld:%02ld - %02ld:%02ld:%02ld"
+ "%{public}@Failed to create current date from components"
+ "%{public}@Failed to create target installation date"
+ "%{public}@Failed to create target installation date for tomorrow"
+ "%{public}@Failed to initialize calendar - invalid home timezone configuration"
+ "%{public}@HMMTRAnnounceOtaScheduler is instantiated with self.homeTimeZone = %@"
+ "%{public}@HMMTRAnnounceOtaSchedulerTimer - OTA Announce completed."
+ "%{public}@HMMTRAnnounceOtaSchedulerTimer - OTA Announce failed with Error: %@."
+ "%{public}@HMMTRAnnounceOtaSchedulerTimer timer expired"
+ "%{public}@Ignoring timer callback for stopped/replaced timer"
+ "%{public}@Invalid negative time interval: %f - cannot start timer"
+ "%{public}@No setup payload to store for System Commissioner node %@"
+ "%{public}@Server is no longer available"
+ "%{public}@Starting AnnounceOtaProviderSchedulerTimer, with delay of %ld hours, %ld minutes, %ld seconds (total: %0.2f seconds)"
+ "%{public}@Stopping AnnounceOtaProviderSchedulerTimer: %@"
+ "%{public}@Storing setup payload for System Commissioner node %@: %@"
+ "%{public}@Time conversion failed - cannot determine update window"
+ "%{public}@Using matched setup payload from commissioning operation for node %@: %@"
+ "%{public}@Using onboardingSetupPayloadString for node %@ (no matched setup payload available): %@"
+ "%{public}@Using original setupPayloadString for node %@ (no matched setup payload available): %@"
+ "%{public}@Window boundaries not initialized properly"
+ "%{public}@announceOtaProvider for %@, immediateAnnouncement: %@, delayCounter: %lu providerNodeId: %@"
+ "%{public}@scheduleOrExecuteOTAProviderAnnouncement is invoked by %@ immediateAnnouncement= %@, delayCounter= %ld, isUserTriggered = %@"
+ "%{public}@there is an active timer, no need for a new one"
+ "@\"HMMTRAnnounceOtaSchedulerTimer\""
+ "@\"NSCalendar\""
+ "@\"NSTimeZone\""
+ "@56@0:8d16@24@32@40@48"
+ "AccesoryRequestInitiator"
+ "B40@0:8@16q24q32"
+ "ERROR: Invalid time %02ld:%02ld:%02ld (valid ranges: 00-23:00-59:00-59)"
+ "HMMTRAnnounceOtaScheduler"
+ "HMMTRAnnounceOtaSchedulerTimer"
+ "HMMTRAnnounceOtaSchedulerTimer for [%@]"
+ "IS"
+ "NotifyUpdateRequestInitiator"
+ "QueryImageBusyResponseTimer"
+ "RebootRepairInitiator"
+ "T@\"HMMTRAnnounceOtaSchedulerTimer\",&,V_activeAnnounceOtaSchedulerTimer"
+ "T@\"MTRSetupPayload\",&,N,V_matchedSetupPayload"
+ "T@\"NSCalendar\",&,V_calendar"
+ "T@\"NSObject<OS_dispatch_queue>\",R,V_announceOtaQueue"
+ "T@\"NSTimeZone\",R,N,V_homeTimeZone"
+ "Td,N,V_timeInterval"
+ "Unknown (%lu)"
+ "_activeAnnounceOtaSchedulerTimer"
+ "_announceOtaQueue"
+ "_calendar"
+ "_cleanupAnnounceOtaProviderSchedulerTimer"
+ "_currentTimeComponents"
+ "_getSoftwareInstallingWindowBeginHour"
+ "_getSoftwareInstallingWindowBeginMinute"
+ "_getSoftwareInstallingWindowBeginSecond"
+ "_getSoftwareInstallingWindowEndHour"
+ "_getSoftwareInstallingWindowEndMinute"
+ "_getSoftwareInstallingWindowEndSecond"
+ "_homeCalendar"
+ "_homeTimeZone"
+ "_isWithinUpdateTimeWindowForComponents:windowBegin:windowEnd:"
+ "_matchedSetupPayload"
+ "_secondsSinceMidnightForHour:minute:second:"
+ "_secondsUntilInstallationWindowBeginForComponents:targetDateTime:"
+ "_timeInterval"
+ "activeAnnounceOtaSchedulerTimer"
+ "announceOtaProviderForNodeID:isRetry:isUserTriggered:timeZone:"
+ "announceOtaQueue"
+ "calendar"
+ "com.apple.homekit.matter.ota-scheduler-timer-management"
+ "currentCalendar"
+ "d32@0:8@16@24"
+ "dateByAddingUnit:value:toDate:options:"
+ "day"
+ "hasOtaProviderSchedulerTimer"
+ "hmmtr.software.install.window.begin.hour"
+ "hmmtr.software.install.window.begin.minute"
+ "hmmtr.software.install.window.begin.second"
+ "hmmtr.software.install.window.end.hour"
+ "hmmtr.software.install.window.end.minute"
+ "hmmtr.software.install.window.end.second"
+ "homeTimeZone"
+ "homeTimeZone is nil"
+ "hour"
+ "init:"
+ "init:server:nodeID:endpoint:queue:"
+ "is NOT"
+ "isWithinUpdateTimeWindow"
+ "matchedPayload"
+ "matchedSetupPayload"
+ "minute"
+ "month"
+ "notifyUpdateRequestedForNodeID:isUserTriggered:isRetry:timeZone:"
+ "q40@0:8q16q24q32"
+ "scheduleOrExecuteOTAProviderAnnouncement:initiatorType:immediateAnnouncement:endpoint:delayCounter:isUserTriggered:"
+ "second"
+ "secondsUntilInstallationWindowBegin"
+ "setActiveAnnounceOtaSchedulerTimer:"
+ "setCalendar:"
+ "setDay:"
+ "setMatchedSetupPayload:"
+ "setMonth:"
+ "setTimeInterval:"
+ "setYear:"
+ "startOtaProviderSchedulerTimer:endpoint:queue:"
+ "stopOtaProviderSchedulerTimer"
+ "systemTimeZone"
+ "v40@0:8@16B24B28@32"
+ "v40@0:8d16@24@32"
+ "v56@0:8@16Q24B32@36q44B52"
+ "year"
- "%{public}@OTA Announce completed for server: %@"
- "%{public}@OTA Announce failed for server %@: %@"
- "%{public}@announceOtaProvider for %@, immediateAnnouncement: %@, delayCounter: %lu"
- "announceOtaProviderForNodeID:isRetry:"
- "notifyUpdateRequestedForNodeID:isUserTriggered:isRetry:"
- "\xf0\x92\xf0\xf0\xf1\xc1"

```
