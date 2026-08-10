## HearingUtilities

> `/System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-536.0.0.0.0
-  __TEXT.__text: 0xb81cc
-  __TEXT.__objc_methlist: 0x929c
+539.1.0.0.0
+  __TEXT.__text: 0xb9a80
+  __TEXT.__objc_methlist: 0x93e4
   __TEXT.__const: 0x7e4
   __TEXT.__dlopen_cstrs: 0x85c
-  __TEXT.__cstring: 0x6096
+  __TEXT.__cstring: 0x60b7
   __TEXT.__swift5_typeref: 0x2a5
   __TEXT.__swift5_capture: 0x1d8
   __TEXT.__constg_swiftt: 0x1a0

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__oslogstring: 0xf724
-  __TEXT.__gcc_except_tab: 0x28ac
-  __TEXT.__unwind_info: 0x2c78
+  __TEXT.__oslogstring: 0xfd57
+  __TEXT.__gcc_except_tab: 0x2900
+  __TEXT.__unwind_info: 0x2cd8
   __TEXT.__eh_frame: 0x70
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3768
+  __DATA_CONST.__const: 0x37e8
   __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x55a8
+  __DATA_CONST.__objc_selrefs: 0x5688
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x3f0
   __DATA_CONST.__got: 0x778
   __AUTH_CONST.__const: 0x1638
-  __AUTH_CONST.__cfstring: 0x5d20
-  __AUTH_CONST.__objc_const: 0xbf28
-  __AUTH_CONST.__objc_intobj: 0xa50
+  __AUTH_CONST.__cfstring: 0x5d60
+  __AUTH_CONST.__objc_const: 0xc078
+  __AUTH_CONST.__objc_intobj: 0xa68
   __AUTH_CONST.__objc_dictobj: 0x410
   __AUTH_CONST.__objc_arrayobj: 0x1e0
   __AUTH_CONST.__objc_doubleobj: 0x1870
   __AUTH_CONST.__auth_got: 0xbb0
   __AUTH.__objc_data: 0x11d8
   __AUTH.__data: 0xa8
-  __DATA.__objc_ivar: 0xa08
+  __DATA.__objc_ivar: 0xa24
   __DATA.__data: 0xf80
-  __DATA.__bss: 0x828
+  __DATA.__bss: 0x820
   __DATA_DIRTY.__objc_data: 0x5a8
   __DATA_DIRTY.__data: 0xc8
   __DATA_DIRTY.__bss: 0xd0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4093
-  Symbols:   8587
-  CStrings:  2089
+  Functions: 4130
+  Symbols:   8658
+  CStrings:  2109
 
Symbols:
+ +[AXHearingAidDevice releaseLeftPowerSourceID:andRightPowerSourceID:]
+ +[HUWidgetReloadHelper reloadAllWidgets]
+ -[AXHAController notifiedPeersOfDiscovery]
+ -[AXHAController setNotifiedPeersOfDiscovery:]
+ -[AXHearingAidDevice reconcileMicrophoneMuteFromVolumes]
+ -[AXHearingAidDevice releaseBatteryServicesOnBluetoothQueue]
+ -[AXHearingAidDevice updateInputTagsAfterPairing]
+ -[AXHearingAidDeviceController bluetoothCentralQueue]
+ -[HUAudioRoutesManager attemptPauseAudioPlaybackWithRemainingAttempts:completion:]
+ -[HUAudioRoutesManager audioSessionWasInterrupted:]
+ -[HUNearbyDevice isInOnboarding]
+ -[HUNearbyDevice setIsInOnboarding:]
+ -[HUNearbyHearingAidController attemptReloadingHearingDeviceProperties]
+ -[HUNearbyHearingAidController checkPeerStateAfterTimeOut:]
+ -[HUNearbyHearingAidController handlePeerDiscoveryEndedFromDevice:]
+ -[HUNearbyHearingAidController handlePeerDiscoveryStartedFromDevice:]
+ -[HUNearbyHearingAidController needsReloadingHearingDeviceProperties]
+ -[HUNearbyHearingAidController notifyConnectedPeerOfDiscoveryReason:]
+ -[HUNearbyHearingAidController notifyPeersDiscoveryEnded]
+ -[HUNearbyHearingAidController notifyPeersDiscoveryStarted]
+ -[HUNearbyHearingAidController propertyLoadRetryCount]
+ -[HUNearbyHearingAidController propertyLoadRetryTimer]
+ -[HUNearbyHearingAidController reloadHearingDevicePropertiesIfNeeded]
+ -[HUNearbyHearingAidController setPropertyLoadRetryCount:]
+ -[HUNearbyHearingAidController setPropertyLoadRetryTimer:]
+ -[HUNoiseController bufferExposureSampleWithSPL:startDate:endDate:]
+ -[HUNoiseController exposureBufferStartDate]
+ -[HUNoiseController exposureBuffer]
+ -[HUNoiseController flushExposureBufferToHealth]
+ -[HUNoiseController lastArtifactsDetectedSampleDate]
+ -[HUNoiseController setExposureBuffer:]
+ -[HUNoiseController setExposureBufferStartDate:]
+ -[HUNoiseController setLastArtifactsDetectedSampleDate:]
+ GCC_except_table1006
+ GCC_except_table1046
+ GCC_except_table1052
+ GCC_except_table1060
+ GCC_except_table1064
+ GCC_except_table1080
+ GCC_except_table1083
+ GCC_except_table1090
+ GCC_except_table1093
+ GCC_except_table1094
+ GCC_except_table1106
+ GCC_except_table1110
+ GCC_except_table1117
+ GCC_except_table1119
+ GCC_except_table1148
+ GCC_except_table1163
+ GCC_except_table1167
+ GCC_except_table1169
+ GCC_except_table1174
+ GCC_except_table1178
+ GCC_except_table1203
+ GCC_except_table1224
+ GCC_except_table1228
+ GCC_except_table1289
+ GCC_except_table1307
+ GCC_except_table1311
+ GCC_except_table1471
+ GCC_except_table1479
+ GCC_except_table1502
+ GCC_except_table1539
+ GCC_except_table1545
+ GCC_except_table1580
+ GCC_except_table1583
+ GCC_except_table1588
+ GCC_except_table1589
+ GCC_except_table1595
+ GCC_except_table1596
+ GCC_except_table1597
+ GCC_except_table1611
+ GCC_except_table1663
+ GCC_except_table1688
+ GCC_except_table1696
+ GCC_except_table1704
+ GCC_except_table1708
+ GCC_except_table1713
+ GCC_except_table1728
+ GCC_except_table1830
+ GCC_except_table1849
+ GCC_except_table1874
+ GCC_except_table1880
+ GCC_except_table1944
+ GCC_except_table1985
+ GCC_except_table1986
+ GCC_except_table1990
+ GCC_except_table1997
+ GCC_except_table2003
+ GCC_except_table2006
+ GCC_except_table2037
+ GCC_except_table2043
+ GCC_except_table2050
+ GCC_except_table2144
+ GCC_except_table2145
+ GCC_except_table2146
+ GCC_except_table2147
+ GCC_except_table2148
+ GCC_except_table2149
+ GCC_except_table2151
+ GCC_except_table2152
+ GCC_except_table2153
+ GCC_except_table2156
+ GCC_except_table2158
+ GCC_except_table2160
+ GCC_except_table2166
+ GCC_except_table2176
+ GCC_except_table2181
+ GCC_except_table2183
+ GCC_except_table2189
+ GCC_except_table2191
+ GCC_except_table2211
+ GCC_except_table2212
+ GCC_except_table2213
+ GCC_except_table2227
+ GCC_except_table2230
+ GCC_except_table2235
+ GCC_except_table2251
+ GCC_except_table2252
+ GCC_except_table2259
+ GCC_except_table2273
+ GCC_except_table2281
+ GCC_except_table2296
+ GCC_except_table2298
+ GCC_except_table2473
+ GCC_except_table2513
+ GCC_except_table2629
+ GCC_except_table2655
+ GCC_except_table2662
+ GCC_except_table2716
+ GCC_except_table2718
+ GCC_except_table2719
+ GCC_except_table2724
+ GCC_except_table2725
+ GCC_except_table2726
+ GCC_except_table2727
+ GCC_except_table2728
+ GCC_except_table2732
+ GCC_except_table2776
+ GCC_except_table2783
+ GCC_except_table2791
+ GCC_except_table2796
+ GCC_except_table2798
+ GCC_except_table2807
+ GCC_except_table2811
+ GCC_except_table2913
+ GCC_except_table2935
+ GCC_except_table2967
+ GCC_except_table2995
+ GCC_except_table3132
+ GCC_except_table3162
+ GCC_except_table3184
+ GCC_except_table3192
+ GCC_except_table3201
+ GCC_except_table3210
+ GCC_except_table3213
+ GCC_except_table3215
+ GCC_except_table3298
+ GCC_except_table3375
+ GCC_except_table3376
+ GCC_except_table3391
+ GCC_except_table3397
+ GCC_except_table3406
+ GCC_except_table3418
+ GCC_except_table3433
+ GCC_except_table3437
+ GCC_except_table3446
+ GCC_except_table3448
+ GCC_except_table3458
+ GCC_except_table3461
+ GCC_except_table3470
+ GCC_except_table3473
+ GCC_except_table3475
+ GCC_except_table3500
+ GCC_except_table3563
+ GCC_except_table3569
+ GCC_except_table3573
+ GCC_except_table362
+ GCC_except_table3644
+ GCC_except_table3646
+ GCC_except_table3726
+ GCC_except_table378
+ GCC_except_table3801
+ GCC_except_table3819
+ GCC_except_table3822
+ GCC_except_table3832
+ GCC_except_table415
+ GCC_except_table439
+ GCC_except_table588
+ GCC_except_table591
+ GCC_except_table592
+ GCC_except_table600
+ GCC_except_table604
+ GCC_except_table616
+ GCC_except_table629
+ GCC_except_table848
+ GCC_except_table902
+ GCC_except_table923
+ GCC_except_table931
+ GCC_except_table934
+ GCC_except_table942
+ GCC_except_table947
+ GCC_except_table950
+ GCC_except_table965
+ GCC_except_table969
+ GCC_except_table972
+ GCC_except_table976
+ _AVAudioSessionInterruptionNotification
+ _AVAudioSessionInterruptionTypeKey
+ _AXHearingPerformPowerSourceTeardown
+ _OBJC_IVAR_$_AXHAController._notifiedPeersOfDiscovery
+ _OBJC_IVAR_$_HUNearbyDevice._isInOnboarding
+ _OBJC_IVAR_$_HUNearbyHearingAidController._propertyLoadRetryCount
+ _OBJC_IVAR_$_HUNearbyHearingAidController._propertyLoadRetryTimer
+ _OBJC_IVAR_$_HUNoiseController._exposureBuffer
+ _OBJC_IVAR_$_HUNoiseController._exposureBufferStartDate
+ _OBJC_IVAR_$_HUNoiseController._lastArtifactsDetectedSampleDate
+ ___29-[AXHearingAidDevice dealloc]_block_invoke
+ ___40+[HUWidgetReloadHelper reloadAllWidgets]_block_invoke
+ ___40-[HUNoiseController _stopADAMDReceiving]_block_invoke
+ ___44-[AXHearingAidDevice releaseBatteryServices]_block_invoke
+ ___48-[HUNoiseController flushExposureBufferToHealth]_block_invoke
+ ___51-[HUAudioRoutesManager audioSessionWasInterrupted:]_block_invoke
+ ___59-[HUNearbyHearingAidController checkPeerStateAfterTimeOut:]_block_invoke
+ ___69-[HUNearbyHearingAidController notifyConnectedPeerOfDiscoveryReason:]_block_invoke
+ ___71-[HUNearbyHearingAidController attemptReloadingHearingDeviceProperties]_block_invoke
+ ___82-[HUAudioRoutesManager attemptPauseAudioPlaybackWithRemainingAttempts:completion:]_block_invoke
+ ___82-[HUAudioRoutesManager attemptPauseAudioPlaybackWithRemainingAttempts:completion:]_block_invoke_2
+ ___block_descriptor_48_e5_v8?0l
+ ___block_descriptor_56_e8_32s40bs_e23_v20?0I8^{__CFArray=}12ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e8_v12?0I8ls40l8s32l8
+ _objc_msgSend$attemptPauseAudioPlaybackWithRemainingAttempts:completion:
+ _objc_msgSend$attemptReloadingHearingDeviceProperties
+ _objc_msgSend$bluetoothCentralQueue
+ _objc_msgSend$bufferExposureSampleWithSPL:startDate:endDate:
+ _objc_msgSend$checkPeerStateAfterTimeOut:
+ _objc_msgSend$exposureBuffer
+ _objc_msgSend$exposureBufferStartDate
+ _objc_msgSend$flushExposureBufferToHealth
+ _objc_msgSend$handlePeerDiscoveryEndedFromDevice:
+ _objc_msgSend$handlePeerDiscoveryStartedFromDevice:
+ _objc_msgSend$isInOnboarding
+ _objc_msgSend$lastArtifactsDetectedSampleDate
+ _objc_msgSend$needsReloadingHearingDeviceProperties
+ _objc_msgSend$notifiedPeersOfDiscovery
+ _objc_msgSend$notifyConnectedPeerOfDiscoveryReason:
+ _objc_msgSend$notifyPeersDiscoveryEnded
+ _objc_msgSend$notifyPeersDiscoveryStarted
+ _objc_msgSend$processCanUseBluetooth
+ _objc_msgSend$propertyLoadRetryCount
+ _objc_msgSend$propertyLoadRetryTimer
+ _objc_msgSend$reconcileMicrophoneMuteFromVolumes
+ _objc_msgSend$releaseBatteryServicesOnBluetoothQueue
+ _objc_msgSend$releaseLeftPowerSourceID:andRightPowerSourceID:
+ _objc_msgSend$reloadAllWidgets
+ _objc_msgSend$reloadHearingDevicePropertiesIfNeeded
+ _objc_msgSend$setExposureBufferStartDate:
+ _objc_msgSend$setIsInOnboarding:
+ _objc_msgSend$setLastArtifactsDetectedSampleDate:
+ _objc_msgSend$setNotifiedPeersOfDiscovery:
+ _objc_msgSend$setPropertyLoadRetryCount:
+ _objc_msgSend$updateInputTagsAfterPairing
- -[HUAudioRoutesManager audioSessionDidBecomeInactive:]
- -[HUAudioRoutesManager audioSessionResumptionRecommended:]
- -[HUHearingAidSettings syncMicrophoneMutedForLeftVolume:rightVolume:]
- -[HUNearbyHearingAidController checkPeerStateAfterTimeOut]
- -[HUNoiseController writeExposureToHKWithSPL:startDate:andEndDate:]
- GCC_except_table1020
- GCC_except_table1024
- GCC_except_table1028
- GCC_except_table1030
- GCC_except_table1038
- GCC_except_table1058
- GCC_except_table1061
- GCC_except_table1068
- GCC_except_table1071
- GCC_except_table1075
- GCC_except_table1084
- GCC_except_table1088
- GCC_except_table1095
- GCC_except_table1126
- GCC_except_table1134
- GCC_except_table1136
- GCC_except_table1141
- GCC_except_table1145
- GCC_except_table1147
- GCC_except_table1152
- GCC_except_table1181
- GCC_except_table1206
- GCC_except_table1265
- GCC_except_table1283
- GCC_except_table1287
- GCC_except_table1447
- GCC_except_table1455
- GCC_except_table1478
- GCC_except_table1515
- GCC_except_table1521
- GCC_except_table1554
- GCC_except_table1557
- GCC_except_table1562
- GCC_except_table1563
- GCC_except_table1569
- GCC_except_table1570
- GCC_except_table1571
- GCC_except_table1585
- GCC_except_table1637
- GCC_except_table1662
- GCC_except_table1670
- GCC_except_table1678
- GCC_except_table1682
- GCC_except_table1687
- GCC_except_table1702
- GCC_except_table1804
- GCC_except_table1823
- GCC_except_table1848
- GCC_except_table1854
- GCC_except_table1918
- GCC_except_table1933
- GCC_except_table1951
- GCC_except_table1960
- GCC_except_table1964
- GCC_except_table1971
- GCC_except_table1980
- GCC_except_table2011
- GCC_except_table2017
- GCC_except_table2024
- GCC_except_table2094
- GCC_except_table2097
- GCC_except_table2104
- GCC_except_table2118
- GCC_except_table2119
- GCC_except_table2121
- GCC_except_table2122
- GCC_except_table2124
- GCC_except_table2125
- GCC_except_table2126
- GCC_except_table2127
- GCC_except_table2132
- GCC_except_table2134
- GCC_except_table2137
- GCC_except_table2140
- GCC_except_table2155
- GCC_except_table2157
- GCC_except_table2159
- GCC_except_table2161
- GCC_except_table2165
- GCC_except_table2186
- GCC_except_table2199
- GCC_except_table2201
- GCC_except_table2204
- GCC_except_table2208
- GCC_except_table2224
- GCC_except_table2232
- GCC_except_table2246
- GCC_except_table2254
- GCC_except_table2269
- GCC_except_table2271
- GCC_except_table2446
- GCC_except_table2459
- GCC_except_table2602
- GCC_except_table2628
- GCC_except_table2635
- GCC_except_table2689
- GCC_except_table2691
- GCC_except_table2692
- GCC_except_table2697
- GCC_except_table2698
- GCC_except_table2699
- GCC_except_table2700
- GCC_except_table2701
- GCC_except_table2705
- GCC_except_table2744
- GCC_except_table2749
- GCC_except_table2756
- GCC_except_table2764
- GCC_except_table2769
- GCC_except_table2780
- GCC_except_table2784
- GCC_except_table2886
- GCC_except_table2908
- GCC_except_table2940
- GCC_except_table2968
- GCC_except_table3105
- GCC_except_table3135
- GCC_except_table3156
- GCC_except_table3157
- GCC_except_table3165
- GCC_except_table3174
- GCC_except_table3186
- GCC_except_table3188
- GCC_except_table3244
- GCC_except_table3341
- GCC_except_table3342
- GCC_except_table3358
- GCC_except_table3364
- GCC_except_table3370
- GCC_except_table3373
- GCC_except_table3385
- GCC_except_table3393
- GCC_except_table3400
- GCC_except_table3411
- GCC_except_table3413
- GCC_except_table3423
- GCC_except_table3435
- GCC_except_table3438
- GCC_except_table3440
- GCC_except_table3465
- GCC_except_table3528
- GCC_except_table3534
- GCC_except_table3538
- GCC_except_table3607
- GCC_except_table3609
- GCC_except_table3652
- GCC_except_table368
- GCC_except_table3764
- GCC_except_table3782
- GCC_except_table3785
- GCC_except_table3795
- GCC_except_table405
- GCC_except_table429
- GCC_except_table574
- GCC_except_table577
- GCC_except_table578
- GCC_except_table586
- GCC_except_table590
- GCC_except_table602
- GCC_except_table615
- GCC_except_table834
- GCC_except_table887
- GCC_except_table903
- GCC_except_table911
- GCC_except_table914
- GCC_except_table922
- GCC_except_table925
- GCC_except_table927
- GCC_except_table930
- GCC_except_table949
- GCC_except_table952
- GCC_except_table956
- GCC_except_table984
- _AVAudioSessionDidBecomeInactiveNotification
- _AVAudioSessionResumptionRecommendationNotification
- ___26-[HUAccessoryManager init]_block_invoke_3
- ___53-[HUNoiseController processMeasurement:withMetadata:]_block_invoke_3
- ___54-[HUAudioRoutesManager audioSessionDidBecomeInactive:]_block_invoke
- ___57-[HUAudioRoutesManager pauseAudioPlaybackWithCompletion:]_block_invoke_3
- ___58-[HUAudioRoutesManager audioSessionResumptionRecommended:]_block_invoke
- ___58-[HUNearbyHearingAidController checkPeerStateAfterTimeOut]_block_invoke
- ___67-[HUNoiseController writeExposureToHKWithSPL:startDate:andEndDate:]_block_invoke
- ___block_descriptor_65_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- _objc_msgSend$checkPeerStateAfterTimeOut
- _objc_msgSend$removePendingNoiseSamplesWithinDateInterval:
- _objc_msgSend$syncMicrophoneMutedForLeftVolume:rightVolume:
- _objc_msgSend$writeExposureToHKWithSPL:startDate:andEndDate:
CStrings:
+ "Artifacts detected, removing %lu pending noise samples"
+ "Audio still playing after %ld pause attempts, giving up"
+ "Did not receive artifacts detected event within timeout (%@). Update artifacts detected state to 0"
+ "Did not receive artifacts detected event within timer timeout. Update artifacts detected state to 0"
+ "Didn't Start handoff for a reason: %@"
+ "Discovery: notify all peers to release connection for reason %@"
+ "Discovery: peer %@ ended onboarding, finishing handoff and updating state"
+ "Discovery: peer %@ started onboarding, releasing connection if needed and backing off"
+ "DiscoveryEnded"
+ "DiscoveryStarted"
+ "HAController: Adjust Independently preference changed to %d, reloading hearing aid widgets"
+ "HUAccessoryManager: Bluetooth not authorized, skipping CoreBluetooth initialization"
+ "HearingAidDevice: Input tags changed for %@ peripheral(s), resetting connection"
+ "HearingAidDevice: Input tags unchanged, skipping connection reset"
+ "HearingAidDevice: Pairing completed while connected, re-tagging input and resetting connection to renegotiate codec for %@"
+ "NearbyHearingAidController: Hearing device properties loaded, stopping reload retries after %@ attempt(s)"
+ "NearbyHearingAidController: No more attempts for reloading hearing device properties"
+ "NearbyHearingAidController: No need for reloading hearing device properties"
+ "NearbyHearingAidController: Reloading hearing device properties, attempt %@ of %@"
+ "NearbyHearingAidController: Starting peerTimer for Peer state check, Peer in onboarding %d"
+ "NearbyHearingAidController: Stopping reloading hearing device properties after %@ attempt(s)"
+ "NearbyHearingAidController: Will try reloading hearing device properties after %@ secs"
+ "Paused audio playback %@, attempts remaining %ld"
+ "Relinquish connection for reason: %@ to peer: %@"
+ "Shouldn't relinquish connection for reason: %@ to peer: %@"
+ "Skipping exposure sample with invalid date range: %@ - %@"
+ "Update measurements enabled state from %d to %d"
- "Couldn't Start handoff for a reason: %@"
- "HearingAidDevice: Updated Input tags, resetting connection"
- "Invalid classification date range: %@ - %@"
- "Invalid exposure date range: %@ - %@"
- "NearbyHearingAidController: Starting peerTimer for Peer state"
- "Paused audio playback %@"
- "relinquishConnectionForReason: %@ to peer: %@"
```
