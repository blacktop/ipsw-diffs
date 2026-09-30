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
- `__TEXT.__swift5_types`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-534.0.0.0.0
-  __TEXT.__text: 0xb68dc
-  __TEXT.__objc_methlist: 0x91ac
+536.0.0.0.0
+  __TEXT.__text: 0xb81cc
+  __TEXT.__objc_methlist: 0x929c
   __TEXT.__const: 0x7e4
   __TEXT.__dlopen_cstrs: 0x85c
-  __TEXT.__cstring: 0x609b
+  __TEXT.__cstring: 0x6096
   __TEXT.__swift5_typeref: 0x2a5
   __TEXT.__swift5_capture: 0x1d8
   __TEXT.__constg_swiftt: 0x1a0

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__oslogstring: 0xf1e3
-  __TEXT.__gcc_except_tab: 0x2858
-  __TEXT.__unwind_info: 0x2c30
+  __TEXT.__oslogstring: 0xf724
+  __TEXT.__gcc_except_tab: 0x28ac
+  __TEXT.__unwind_info: 0x2c78
   __TEXT.__eh_frame: 0x70
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3710
+  __DATA_CONST.__const: 0x3768
   __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5508
+  __DATA_CONST.__objc_selrefs: 0x55a8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x3f0
-  __DATA_CONST.__got: 0x768
-  __AUTH_CONST.__const: 0x1618
-  __AUTH_CONST.__cfstring: 0x5d40
-  __AUTH_CONST.__objc_const: 0xbdf0
+  __DATA_CONST.__got: 0x778
+  __AUTH_CONST.__const: 0x1638
+  __AUTH_CONST.__cfstring: 0x5d20
+  __AUTH_CONST.__objc_const: 0xbf28
   __AUTH_CONST.__objc_intobj: 0xa50
   __AUTH_CONST.__objc_dictobj: 0x410
   __AUTH_CONST.__objc_arrayobj: 0x1e0

   __AUTH_CONST.__auth_got: 0xbb0
   __AUTH.__objc_data: 0x11d8
   __AUTH.__data: 0xa8
-  __DATA.__objc_ivar: 0x9f4
+  __DATA.__objc_ivar: 0xa08
   __DATA.__data: 0xf80
-  __DATA.__bss: 0x7e0
+  __DATA.__bss: 0x828
   __DATA_DIRTY.__objc_data: 0x5a8
   __DATA_DIRTY.__data: 0xc8
-  __DATA_DIRTY.__bss: 0x110
+  __DATA_DIRTY.__bss: 0xd0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AVRouting.framework/AVRouting

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4064
-  Symbols:   8533
-  CStrings:  2071
+  Functions: 4093
+  Symbols:   8587
+  CStrings:  2089
 
Symbols:
+ -[AXHearingAidDevice releaseBatteryServices]
+ -[AXHearingAidDeviceController pairingInfoRemovedErrorTimeStamp]
+ -[AXHearingAidDeviceController setPairingInfoRemovedErrorTimeStamp:]
+ -[HUAccessoryManager getRouteSupportingHeadphoneAccommodationsActivatingConnectedHeadphonesIfNeededWithCompletion:]
+ -[HUAccessoryManager prefEQTempDisabledByIdentifier]
+ -[HUAccessoryManager prefEQTempDisabledDesiredByIdentifier]
+ -[HUAccessoryManager prefEQTempDisabledInFlightIdentifiers]
+ -[HUAccessoryManager sendPrefEQTempDisabledForIdentifier:]
+ -[HUAccessoryManager setPrefEQTempDisabledByIdentifier:]
+ -[HUAccessoryManager setPrefEQTempDisabledDesiredByIdentifier:]
+ -[HUAccessoryManager setPrefEQTempDisabledInFlightIdentifiers:]
+ -[HUAudioRoutesManager hasNotifiedRouteState]
+ -[HUAudioRoutesManager selectHeadphoneRoute]
+ -[HUAudioRoutesManager setHasNotifiedRouteState:]
+ -[HUAudioRoutesState hash]
+ -[HUAudioRoutesState isEqual:]
+ -[HUAudioRoutesState isEqualToRoutesState:]
+ -[HUHearingAidSettings updatePairedDevicePublicPreferences:]
+ -[HULiveListenController muteMixerOutputInAudioQueue]
+ -[HULiveListenController muteMixerOutput]
+ GCC_except_table1020
+ GCC_except_table1028
+ GCC_except_table1030
+ GCC_except_table1038
+ GCC_except_table1042
+ GCC_except_table1050
+ GCC_except_table1058
+ GCC_except_table1061
+ GCC_except_table1068
+ GCC_except_table1071
+ GCC_except_table1072
+ GCC_except_table1084
+ GCC_except_table1095
+ GCC_except_table1097
+ GCC_except_table1126
+ GCC_except_table1134
+ GCC_except_table1141
+ GCC_except_table1145
+ GCC_except_table1147
+ GCC_except_table1152
+ GCC_except_table1156
+ GCC_except_table1158
+ GCC_except_table1180
+ GCC_except_table1181
+ GCC_except_table1202
+ GCC_except_table1206
+ GCC_except_table1265
+ GCC_except_table1283
+ GCC_except_table1287
+ GCC_except_table1447
+ GCC_except_table1455
+ GCC_except_table1478
+ GCC_except_table1515
+ GCC_except_table1521
+ GCC_except_table1557
+ GCC_except_table1562
+ GCC_except_table1563
+ GCC_except_table1569
+ GCC_except_table1571
+ GCC_except_table1585
+ GCC_except_table1637
+ GCC_except_table1662
+ GCC_except_table1670
+ GCC_except_table1678
+ GCC_except_table1682
+ GCC_except_table1702
+ GCC_except_table1804
+ GCC_except_table1823
+ GCC_except_table1848
+ GCC_except_table1854
+ GCC_except_table1933
+ GCC_except_table1951
+ GCC_except_table1959
+ GCC_except_table1960
+ GCC_except_table1964
+ GCC_except_table1971
+ GCC_except_table1977
+ GCC_except_table1980
+ GCC_except_table2011
+ GCC_except_table2017
+ GCC_except_table2024
+ GCC_except_table2094
+ GCC_except_table2097
+ GCC_except_table2118
+ GCC_except_table2119
+ GCC_except_table2121
+ GCC_except_table2122
+ GCC_except_table2124
+ GCC_except_table2125
+ GCC_except_table2126
+ GCC_except_table2127
+ GCC_except_table2130
+ GCC_except_table2134
+ GCC_except_table2140
+ GCC_except_table2150
+ GCC_except_table2155
+ GCC_except_table2157
+ GCC_except_table2159
+ GCC_except_table2161
+ GCC_except_table2163
+ GCC_except_table2165
+ GCC_except_table2186
+ GCC_except_table2187
+ GCC_except_table2199
+ GCC_except_table2201
+ GCC_except_table2204
+ GCC_except_table2208
+ GCC_except_table2224
+ GCC_except_table2225
+ GCC_except_table2232
+ GCC_except_table2246
+ GCC_except_table2254
+ GCC_except_table2269
+ GCC_except_table2271
+ GCC_except_table2446
+ GCC_except_table2459
+ GCC_except_table2486
+ GCC_except_table2602
+ GCC_except_table2628
+ GCC_except_table2635
+ GCC_except_table2689
+ GCC_except_table2691
+ GCC_except_table2692
+ GCC_except_table2697
+ GCC_except_table2698
+ GCC_except_table2699
+ GCC_except_table2700
+ GCC_except_table2701
+ GCC_except_table2705
+ GCC_except_table2744
+ GCC_except_table2749
+ GCC_except_table2756
+ GCC_except_table2764
+ GCC_except_table2769
+ GCC_except_table2771
+ GCC_except_table2780
+ GCC_except_table2784
+ GCC_except_table2886
+ GCC_except_table2908
+ GCC_except_table2940
+ GCC_except_table2968
+ GCC_except_table3105
+ GCC_except_table3135
+ GCC_except_table3156
+ GCC_except_table3165
+ GCC_except_table3174
+ GCC_except_table3183
+ GCC_except_table3186
+ GCC_except_table3188
+ GCC_except_table3244
+ GCC_except_table3271
+ GCC_except_table3342
+ GCC_except_table3358
+ GCC_except_table3370
+ GCC_except_table3373
+ GCC_except_table3385
+ GCC_except_table3393
+ GCC_except_table3400
+ GCC_except_table3403
+ GCC_except_table3413
+ GCC_except_table3423
+ GCC_except_table3426
+ GCC_except_table3435
+ GCC_except_table3438
+ GCC_except_table3440
+ GCC_except_table3465
+ GCC_except_table3528
+ GCC_except_table3534
+ GCC_except_table3538
+ GCC_except_table3607
+ GCC_except_table3609
+ GCC_except_table3652
+ GCC_except_table3689
+ GCC_except_table3764
+ GCC_except_table3782
+ GCC_except_table3785
+ GCC_except_table3795
+ GCC_except_table903
+ GCC_except_table911
+ GCC_except_table914
+ GCC_except_table922
+ GCC_except_table925
+ GCC_except_table927
+ GCC_except_table930
+ GCC_except_table945
+ GCC_except_table949
+ GCC_except_table952
+ GCC_except_table956
+ GCC_except_table984
+ _AVSystemController_HighestArbitrationPriorityForTipiDidChangeNotification
+ _AVSystemController_HighestArbitrationPriorityForTipi_BundleID
+ _OBJC_IVAR_$_AXHearingAidDeviceController._pairingInfoRemovedErrorTimeStamp
+ _OBJC_IVAR_$_HUAccessoryManager._prefEQTempDisabledByIdentifier
+ _OBJC_IVAR_$_HUAccessoryManager._prefEQTempDisabledDesiredByIdentifier
+ _OBJC_IVAR_$_HUAccessoryManager._prefEQTempDisabledInFlightIdentifiers
+ _OBJC_IVAR_$_HUAudioRoutesManager._hasNotifiedRouteState
+ ___115-[HUAccessoryManager getRouteSupportingHeadphoneAccommodationsActivatingConnectedHeadphonesIfNeededWithCompletion:]_block_invoke
+ ___115-[HUAccessoryManager getRouteSupportingHeadphoneAccommodationsActivatingConnectedHeadphonesIfNeededWithCompletion:]_block_invoke_2
+ ___115-[HUAccessoryManager getRouteSupportingHeadphoneAccommodationsActivatingConnectedHeadphonesIfNeededWithCompletion:]_block_invoke_3
+ ___41-[HULiveListenController muteMixerOutput]_block_invoke
+ ___44-[HUAudioRoutesManager selectHeadphoneRoute]_block_invoke
+ ___58-[HUAccessoryManager sendPrefEQTempDisabledForIdentifier:]_block_invoke
+ ___58-[HUAccessoryManager sendPrefEQTempDisabledForIdentifier:]_block_invoke_2
+ ___84-[AXHearingAidDeviceController processConnectionFailForPairingInfoRemovedForDevice:]_block_invoke_2
+ ___block_descriptor_48_e8_32s40bs_e44_v44?0"NSDictionary"8Q16"NSString"24B32Q36ls40l8s32l8
+ ___block_descriptor_56_e8_32s40s48w_e17_v16?0"NSError"8lw48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e5_v8?0lr56l8s48l8s32l8s40l8
+ _objc_msgSend$hasNotifiedRouteState
+ _objc_msgSend$isEqualToNumber:
+ _objc_msgSend$isEqualToRoutesState:
+ _objc_msgSend$muteMixerOutput
+ _objc_msgSend$muteMixerOutputInAudioQueue
+ _objc_msgSend$numberWithUnsignedLong:
+ _objc_msgSend$pairingInfoRemovedErrorTimeStamp
+ _objc_msgSend$releaseBatteryServices
+ _objc_msgSend$selectHeadphoneRoute
+ _objc_msgSend$sendPrefEQTempDisabledForIdentifier:
+ _objc_msgSend$setHasNotifiedRouteState:
+ _objc_msgSend$setPairingInfoRemovedErrorTimeStamp:
+ _objc_msgSend$setPrefEQTempDisabledByIdentifier:
+ _objc_msgSend$setPrefEQTempDisabledDesiredByIdentifier:
+ _objc_msgSend$setPrefEQTempDisabledInFlightIdentifiers:
+ _objc_msgSend$updatePairedDevicePublicPreferences:
- GCC_except_table1013
- GCC_except_table1017
- GCC_except_table1021
- GCC_except_table1029
- GCC_except_table1033
- GCC_except_table1041
- GCC_except_table1049
- GCC_except_table1052
- GCC_except_table1059
- GCC_except_table1062
- GCC_except_table1063
- GCC_except_table1066
- GCC_except_table1079
- GCC_except_table1086
- GCC_except_table1117
- GCC_except_table1125
- GCC_except_table1127
- GCC_except_table1132
- GCC_except_table1138
- GCC_except_table1142
- GCC_except_table1144
- GCC_except_table1166
- GCC_except_table1167
- GCC_except_table1188
- GCC_except_table1192
- GCC_except_table1251
- GCC_except_table1269
- GCC_except_table1273
- GCC_except_table1433
- GCC_except_table1441
- GCC_except_table1464
- GCC_except_table1500
- GCC_except_table1506
- GCC_except_table1539
- GCC_except_table1542
- GCC_except_table1547
- GCC_except_table1548
- GCC_except_table1555
- GCC_except_table1556
- GCC_except_table1622
- GCC_except_table1647
- GCC_except_table1655
- GCC_except_table1663
- GCC_except_table1667
- GCC_except_table1672
- GCC_except_table1789
- GCC_except_table1808
- GCC_except_table1833
- GCC_except_table1839
- GCC_except_table1903
- GCC_except_table1936
- GCC_except_table1944
- GCC_except_table1945
- GCC_except_table1949
- GCC_except_table1956
- GCC_except_table1962
- GCC_except_table1965
- GCC_except_table1996
- GCC_except_table2002
- GCC_except_table2009
- GCC_except_table2077
- GCC_except_table2080
- GCC_except_table2087
- GCC_except_table2101
- GCC_except_table2102
- GCC_except_table2103
- GCC_except_table2105
- GCC_except_table2106
- GCC_except_table2107
- GCC_except_table2108
- GCC_except_table2109
- GCC_except_table2110
- GCC_except_table2113
- GCC_except_table2115
- GCC_except_table2117
- GCC_except_table2139
- GCC_except_table2141
- GCC_except_table2143
- GCC_except_table2145
- GCC_except_table2147
- GCC_except_table2167
- GCC_except_table2168
- GCC_except_table2169
- GCC_except_table2180
- GCC_except_table2182
- GCC_except_table2189
- GCC_except_table2205
- GCC_except_table2206
- GCC_except_table2213
- GCC_except_table2227
- GCC_except_table2235
- GCC_except_table2250
- GCC_except_table2252
- GCC_except_table2427
- GCC_except_table2440
- GCC_except_table2467
- GCC_except_table2583
- GCC_except_table2609
- GCC_except_table2616
- GCC_except_table2670
- GCC_except_table2672
- GCC_except_table2673
- GCC_except_table2678
- GCC_except_table2679
- GCC_except_table2680
- GCC_except_table2681
- GCC_except_table2682
- GCC_except_table2686
- GCC_except_table2725
- GCC_except_table2730
- GCC_except_table2737
- GCC_except_table2745
- GCC_except_table2750
- GCC_except_table2752
- GCC_except_table2761
- GCC_except_table2765
- GCC_except_table2860
- GCC_except_table2882
- GCC_except_table2914
- GCC_except_table2942
- GCC_except_table3079
- GCC_except_table3109
- GCC_except_table3130
- GCC_except_table3131
- GCC_except_table3139
- GCC_except_table3148
- GCC_except_table3160
- GCC_except_table3162
- GCC_except_table3215
- GCC_except_table3242
- GCC_except_table3312
- GCC_except_table3313
- GCC_except_table3329
- GCC_except_table3335
- GCC_except_table3344
- GCC_except_table3356
- GCC_except_table3371
- GCC_except_table3374
- GCC_except_table3382
- GCC_except_table3384
- GCC_except_table3394
- GCC_except_table3397
- GCC_except_table3406
- GCC_except_table3409
- GCC_except_table3436
- GCC_except_table3499
- GCC_except_table3505
- GCC_except_table3509
- GCC_except_table3578
- GCC_except_table3580
- GCC_except_table3623
- GCC_except_table3660
- GCC_except_table3735
- GCC_except_table3753
- GCC_except_table3756
- GCC_except_table3766
- GCC_except_table902
- GCC_except_table910
- GCC_except_table913
- GCC_except_table921
- GCC_except_table924
- GCC_except_table926
- GCC_except_table929
- GCC_except_table944
- GCC_except_table948
- GCC_except_table951
- GCC_except_table955
- GCC_except_table983
- ___block_descriptor_33_e17_v16?0"NSError"8l
CStrings:
+ "AccessoryManager: Active route is speaker but supported headphones %@ are connected - switching route for Headphone Accommodations"
+ "AccessoryManager: Route is not nil %@"
+ "AudioRoutesManager: audioRoutesDidChange, route state unchanged — skipping redundant listener notification"
+ "HearingAidDevice: Created power source for %@"
+ "HearingAidDevice: Released power source for %@"
+ "HearingAidDevice: Released power source for Left"
+ "HearingAidDevice: Released power source for Right"
+ "HearingAidDeviceController: Clearing old pairing info removed time stamp: %@"
+ "HearingAidDeviceController: Ignoring pairing info removed event, last control message time stamp: %@"
+ "HearingAidsSettings: Clear HearingSetDevicePairedEars, ears from iCloud: %@"
+ "HearingAidsSettings: Save HearingSetDevicePairedEars: %@"
+ "LiveListenController: Deactivated audio session: %@, error: %@"
+ "LiveListenController: Early mute mixer"
+ "LiveListenController: Route changed, isListening = %d"
+ "LiveListenController: Route changed, selected route: LL = [%d->%d], HA = [%d->%d]"
+ "LiveListenController: Route lost to speaker while listening — stopping Live Listen immediately"
+ "LiveListenController: Will stop LiveListen with audio session: %@"
+ "setPrefEQTempDisabled: skipping send for device %{public}@, already set to %d"
+ "setPrefEQTempDisabled: skipping send for device %{public}@, change already in flight"
- "State"
```
