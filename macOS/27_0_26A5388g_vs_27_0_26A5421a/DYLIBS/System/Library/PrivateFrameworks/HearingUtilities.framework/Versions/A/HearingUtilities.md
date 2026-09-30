## HearingUtilities

> `/System/Library/PrivateFrameworks/HearingUtilities.framework/Versions/A/HearingUtilities`

```diff

-536.0.0.0.0
-  __TEXT.__text: 0x8fe00
-  __TEXT.__objc_methlist: 0x6fac
+539.0.1.0.0
+  __TEXT.__text: 0x911b0
+  __TEXT.__objc_methlist: 0x7094
   __TEXT.__const: 0x6b4
   __TEXT.__dlopen_cstrs: 0x3ed
   __TEXT.__constg_swiftt: 0x110

   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_fieldmd: 0xd4
-  __TEXT.__cstring: 0x4b8a
+  __TEXT.__cstring: 0x4bab
   __TEXT.__swift5_capture: 0x1a8
-  __TEXT.__oslogstring: 0xcd4b
-  __TEXT.__gcc_except_tab: 0x1cdc
-  __TEXT.__unwind_info: 0x2118
+  __TEXT.__oslogstring: 0xd20b
+  __TEXT.__gcc_except_tab: 0x1d0c
+  __TEXT.__unwind_info: 0x2158
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xa68
+  __DATA_CONST.__const: 0xa98
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4158
+  __DATA_CONST.__objc_selrefs: 0x4200
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0x2a0
   __DATA_CONST.__got: 0x580
-  __AUTH_CONST.__const: 0x3d50
-  __AUTH_CONST.__cfstring: 0x4800
-  __AUTH_CONST.__objc_const: 0x8fc8
-  __AUTH_CONST.__objc_intobj: 0x648
+  __AUTH_CONST.__const: 0x3dc0
+  __AUTH_CONST.__cfstring: 0x4840
+  __AUTH_CONST.__objc_const: 0x9088
+  __AUTH_CONST.__objc_intobj: 0x660
   __AUTH_CONST.__objc_dictobj: 0x280
   __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x850
   __AUTH.__objc_data: 0x640
   __AUTH.__data: 0x58
-  __DATA.__objc_ivar: 0x788
+  __DATA.__objc_ivar: 0x798
   __DATA.__data: 0xb60
-  __DATA.__bss: 0x4d8
+  __DATA.__bss: 0x4e0
   __DATA_DIRTY.__objc_data: 0xaf8
   __DATA_DIRTY.__data: 0xc8
-  __DATA_DIRTY.__bss: 0x140
+  __DATA_DIRTY.__bss: 0x138
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3149
-  Symbols:   6567
-  CStrings:  1654
+  Functions: 3174
+  Symbols:   6622
+  CStrings:  1670
 
Symbols:
+ +[AXHearingAidDevice releaseLeftPowerSourceID:andRightPowerSourceID:]
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
+ GCC_except_table1002
+ GCC_except_table1003
+ GCC_except_table1006
+ GCC_except_table1015
+ GCC_except_table1019
+ GCC_except_table1026
+ GCC_except_table1029
+ GCC_except_table1060
+ GCC_except_table1069
+ GCC_except_table1071
+ GCC_except_table1076
+ GCC_except_table1080
+ GCC_except_table1082
+ GCC_except_table1088
+ GCC_except_table1094
+ GCC_except_table1096
+ GCC_except_table1119
+ GCC_except_table1141
+ GCC_except_table1145
+ GCC_except_table1210
+ GCC_except_table1357
+ GCC_except_table1401
+ GCC_except_table1428
+ GCC_except_table1431
+ GCC_except_table1437
+ GCC_except_table1446
+ GCC_except_table1447
+ GCC_except_table1458
+ GCC_except_table1510
+ GCC_except_table1539
+ GCC_except_table1547
+ GCC_except_table1555
+ GCC_except_table1559
+ GCC_except_table1564
+ GCC_except_table1579
+ GCC_except_table1612
+ GCC_except_table1627
+ GCC_except_table1654
+ GCC_except_table1658
+ GCC_except_table1667
+ GCC_except_table1675
+ GCC_except_table1755
+ GCC_except_table1781
+ GCC_except_table1782
+ GCC_except_table1783
+ GCC_except_table1784
+ GCC_except_table1785
+ GCC_except_table1786
+ GCC_except_table1787
+ GCC_except_table1788
+ GCC_except_table1789
+ GCC_except_table1792
+ GCC_except_table1794
+ GCC_except_table1796
+ GCC_except_table1802
+ GCC_except_table1812
+ GCC_except_table1817
+ GCC_except_table1819
+ GCC_except_table1821
+ GCC_except_table1823
+ GCC_except_table1847
+ GCC_except_table1849
+ GCC_except_table1861
+ GCC_except_table1863
+ GCC_except_table1866
+ GCC_except_table1871
+ GCC_except_table1887
+ GCC_except_table1888
+ GCC_except_table1895
+ GCC_except_table1917
+ GCC_except_table1932
+ GCC_except_table1934
+ GCC_except_table2112
+ GCC_except_table2125
+ GCC_except_table2152
+ GCC_except_table2200
+ GCC_except_table2207
+ GCC_except_table2262
+ GCC_except_table2264
+ GCC_except_table2267
+ GCC_except_table2272
+ GCC_except_table2273
+ GCC_except_table2274
+ GCC_except_table2275
+ GCC_except_table2276
+ GCC_except_table2280
+ GCC_except_table2309
+ GCC_except_table2320
+ GCC_except_table2328
+ GCC_except_table2333
+ GCC_except_table2334
+ GCC_except_table2335
+ GCC_except_table2440
+ GCC_except_table2481
+ GCC_except_table2508
+ GCC_except_table2647
+ GCC_except_table2694
+ GCC_except_table2695
+ GCC_except_table2703
+ GCC_except_table2712
+ GCC_except_table2721
+ GCC_except_table2724
+ GCC_except_table2786
+ GCC_except_table2792
+ GCC_except_table2796
+ GCC_except_table2871
+ GCC_except_table2904
+ GCC_except_table294
+ GCC_except_table312
+ GCC_except_table352
+ GCC_except_table378
+ GCC_except_table486
+ GCC_except_table490
+ GCC_except_table491
+ GCC_except_table499
+ GCC_except_table503
+ GCC_except_table515
+ GCC_except_table526
+ GCC_except_table746
+ GCC_except_table802
+ GCC_except_table822
+ GCC_except_table830
+ GCC_except_table835
+ GCC_except_table847
+ GCC_except_table850
+ GCC_except_table852
+ GCC_except_table870
+ GCC_except_table874
+ GCC_except_table877
+ GCC_except_table883
+ GCC_except_table913
+ GCC_except_table949
+ GCC_except_table953
+ GCC_except_table957
+ GCC_except_table959
+ GCC_except_table969
+ GCC_except_table973
+ GCC_except_table989
+ GCC_except_table992
+ GCC_except_table999
+ OBJC_IVAR_$_AXHAController._notifiedPeersOfDiscovery
+ OBJC_IVAR_$_HUNearbyDevice._isInOnboarding
+ OBJC_IVAR_$_HUNearbyHearingAidController._propertyLoadRetryCount
+ OBJC_IVAR_$_HUNearbyHearingAidController._propertyLoadRetryTimer
+ _AVAudioSessionInterruptionNotification
+ _AVAudioSessionInterruptionTypeKey
+ __82-[HUAudioRoutesManager attemptPauseAudioPlaybackWithRemainingAttempts:completion:]_block_invoke
+ ___29-[AXHearingAidDevice dealloc]_block_invoke
+ ___44-[AXHearingAidDevice releaseBatteryServices]_block_invoke
+ ___51-[HUAudioRoutesManager audioSessionWasInterrupted:]_block_invoke
+ ___59-[HUNearbyHearingAidController checkPeerStateAfterTimeOut:]_block_invoke
+ ___69-[HUNearbyHearingAidController notifyConnectedPeerOfDiscoveryReason:]_block_invoke
+ ___71-[HUNearbyHearingAidController attemptReloadingHearingDeviceProperties]_block_invoke
+ ___82-[HUAudioRoutesManager attemptPauseAudioPlaybackWithRemainingAttempts:completion:]_block_invoke
+ ___82-[HUAudioRoutesManager attemptPauseAudioPlaybackWithRemainingAttempts:completion:]_block_invoke_2
+ ___block_descriptor_48_e5_v8?0l
+ ___block_descriptor_56_e8_32s40bs_e23_v20?0I8^{__CFArray=}12l
+ ___block_descriptor_56_e8_32s40bs_e5_v8?0l
+ ___block_descriptor_56_e8_32s40bs_e8_v12?0I8l
+ _objc_msgSend$attemptPauseAudioPlaybackWithRemainingAttempts:completion:
+ _objc_msgSend$attemptReloadingHearingDeviceProperties
+ _objc_msgSend$bluetoothCentralQueue
+ _objc_msgSend$checkPeerStateAfterTimeOut:
+ _objc_msgSend$handlePeerDiscoveryEndedFromDevice:
+ _objc_msgSend$handlePeerDiscoveryStartedFromDevice:
+ _objc_msgSend$isInOnboarding
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
+ _objc_msgSend$reloadHearingDevicePropertiesIfNeeded
+ _objc_msgSend$setIsInOnboarding:
+ _objc_msgSend$setNotifiedPeersOfDiscovery:
+ _objc_msgSend$setPropertyLoadRetryCount:
+ _objc_msgSend$updateInputTagsAfterPairing
+ _objc_msgSend$userInfo
- -[HUAudioRoutesManager audioSessionDidBecomeInactive:]
- -[HUAudioRoutesManager audioSessionResumptionRecommended:]
- -[HUHearingAidSettings syncMicrophoneMutedForLeftVolume:rightVolume:]
- -[HUNearbyHearingAidController checkPeerStateAfterTimeOut]
- GCC_except_table1005
- GCC_except_table1008
- GCC_except_table1039
- GCC_except_table1048
- GCC_except_table1050
- GCC_except_table1055
- GCC_except_table1059
- GCC_except_table1061
- GCC_except_table1067
- GCC_except_table1073
- GCC_except_table1075
- GCC_except_table1098
- GCC_except_table1099
- GCC_except_table1124
- GCC_except_table1187
- GCC_except_table1335
- GCC_except_table1379
- GCC_except_table1406
- GCC_except_table1409
- GCC_except_table1414
- GCC_except_table1415
- GCC_except_table1424
- GCC_except_table1425
- GCC_except_table1488
- GCC_except_table1517
- GCC_except_table1525
- GCC_except_table1533
- GCC_except_table1537
- GCC_except_table1542
- GCC_except_table1557
- GCC_except_table1590
- GCC_except_table1605
- GCC_except_table1623
- GCC_except_table1631
- GCC_except_table1632
- GCC_except_table1636
- GCC_except_table1733
- GCC_except_table1736
- GCC_except_table1744
- GCC_except_table1759
- GCC_except_table1760
- GCC_except_table1761
- GCC_except_table1762
- GCC_except_table1763
- GCC_except_table1764
- GCC_except_table1765
- GCC_except_table1767
- GCC_except_table1770
- GCC_except_table1772
- GCC_except_table1774
- GCC_except_table1777
- GCC_except_table1790
- GCC_except_table1795
- GCC_except_table1797
- GCC_except_table1801
- GCC_except_table1803
- GCC_except_table1805
- GCC_except_table1826
- GCC_except_table1839
- GCC_except_table1841
- GCC_except_table1844
- GCC_except_table1864
- GCC_except_table1865
- GCC_except_table1872
- GCC_except_table1886
- GCC_except_table1894
- GCC_except_table1911
- GCC_except_table2089
- GCC_except_table2102
- GCC_except_table2129
- GCC_except_table2177
- GCC_except_table2184
- GCC_except_table2239
- GCC_except_table2241
- GCC_except_table2244
- GCC_except_table2249
- GCC_except_table2250
- GCC_except_table2251
- GCC_except_table2252
- GCC_except_table2253
- GCC_except_table2257
- GCC_except_table2286
- GCC_except_table2288
- GCC_except_table2297
- GCC_except_table2305
- GCC_except_table2310
- GCC_except_table2312
- GCC_except_table2417
- GCC_except_table2458
- GCC_except_table2485
- GCC_except_table2624
- GCC_except_table2671
- GCC_except_table2672
- GCC_except_table2680
- GCC_except_table2689
- GCC_except_table2698
- GCC_except_table2701
- GCC_except_table2763
- GCC_except_table2769
- GCC_except_table2773
- GCC_except_table2846
- GCC_except_table2879
- GCC_except_table300
- GCC_except_table340
- GCC_except_table366
- GCC_except_table472
- GCC_except_table476
- GCC_except_table477
- GCC_except_table485
- GCC_except_table489
- GCC_except_table501
- GCC_except_table512
- GCC_except_table732
- GCC_except_table787
- GCC_except_table803
- GCC_except_table811
- GCC_except_table816
- GCC_except_table828
- GCC_except_table831
- GCC_except_table833
- GCC_except_table836
- GCC_except_table851
- GCC_except_table858
- GCC_except_table864
- GCC_except_table892
- GCC_except_table928
- GCC_except_table932
- GCC_except_table936
- GCC_except_table938
- GCC_except_table948
- GCC_except_table952
- GCC_except_table960
- GCC_except_table968
- GCC_except_table971
- GCC_except_table978
- GCC_except_table982
- GCC_except_table985
- GCC_except_table994
- GCC_except_table998
- _AVAudioSessionDidBecomeInactiveNotification
- _AVAudioSessionResumptionRecommendationNotification
- __57-[HUAudioRoutesManager pauseAudioPlaybackWithCompletion:]_block_invoke
- ___54-[HUAudioRoutesManager audioSessionDidBecomeInactive:]_block_invoke
- ___57-[HUAudioRoutesManager pauseAudioPlaybackWithCompletion:]_block_invoke_3
- ___58-[HUAudioRoutesManager audioSessionResumptionRecommended:]_block_invoke
- ___58-[HUNearbyHearingAidController checkPeerStateAfterTimeOut]_block_invoke
- _objc_msgSend$checkPeerStateAfterTimeOut
- _objc_msgSend$syncMicrophoneMutedForLeftVolume:rightVolume:
CStrings:
+ "Audio still playing after %ld pause attempts, giving up"
+ "Didn't Start handoff for a reason: %@"
+ "Discovery: notify all peers to release connection for reason %@"
+ "Discovery: peer %@ ended onboarding, finishing handoff and updating state"
+ "Discovery: peer %@ started onboarding, releasing connection if needed and backing off"
+ "DiscoveryEnded"
+ "DiscoveryStarted"
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
- "Couldn't Start handoff for a reason: %@"
- "HearingAidDevice: Updated Input tags, resetting connection"
- "NearbyHearingAidController: Starting peerTimer for Peer state"
- "Paused audio playback %@"
- "relinquishConnectionForReason: %@ to peer: %@"
```
