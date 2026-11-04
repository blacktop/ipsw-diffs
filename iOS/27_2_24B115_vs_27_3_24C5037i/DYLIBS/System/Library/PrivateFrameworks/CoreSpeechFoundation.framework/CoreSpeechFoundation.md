## CoreSpeechFoundation

> `/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/CoreSpeechFoundation`

```diff

-3605.32.1.0.0
-  __TEXT.__text: 0xcc0d4
-  __TEXT.__objc_methlist: 0xdd20
+3610.11.1.0.0
+  __TEXT.__text: 0xcfbac
+  __TEXT.__objc_methlist: 0xe100
   __TEXT.__const: 0x1078
   __TEXT.__dlopen_cstrs: 0x24a
   __TEXT.__constg_swiftt: 0x2cc
   __TEXT.__swift5_typeref: 0x1dc
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_types: 0x30
-  __TEXT.__cstring: 0x16dbe
+  __TEXT.__cstring: 0x17563
   __TEXT.__swift5_reflstr: 0x278
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_fieldmd: 0x250
   __TEXT.__swift5_proto: 0x74
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__gcc_except_tab: 0x3e08
-  __TEXT.__oslogstring: 0x120ca
-  __TEXT.__unwind_info: 0x4b70
+  __TEXT.__gcc_except_tab: 0x3e84
+  __TEXT.__oslogstring: 0x12d4c
+  __TEXT.__unwind_info: 0x4c88
   __TEXT.__eh_frame: 0x270
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2958
-  __DATA_CONST.__objc_classlist: 0x758
+  __DATA_CONST.__const: 0x29f0
+  __DATA_CONST.__objc_classlist: 0x778
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x228
+  __DATA_CONST.__objc_protolist: 0x230
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x18
-  __DATA_CONST.__objc_selrefs: 0x76d0
+  __DATA_CONST.__objc_selrefs: 0x78a8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x578
+  __DATA_CONST.__objc_superrefs: 0x590
   __DATA_CONST.__objc_arraydata: 0x1c8
-  __DATA_CONST.__got: 0x1048
-  __AUTH_CONST.__const: 0x1b80
-  __AUTH_CONST.__cfstring: 0x9d20
-  __AUTH_CONST.__objc_const: 0x152f0
+  __DATA_CONST.__got: 0x1068
+  __AUTH_CONST.__const: 0x1be0
+  __AUTH_CONST.__cfstring: 0x9f60
+  __AUTH_CONST.__objc_const: 0x15920
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_dictobj: 0x1e0
-  __AUTH_CONST.__objc_intobj: 0x4e0
+  __AUTH_CONST.__objc_intobj: 0x4f8
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_floatobj: 0x1a0
-  __AUTH_CONST.__auth_got: 0xfc8
-  __AUTH.__objc_data: 0x218
-  __DATA.__objc_ivar: 0xde4
-  __DATA.__data: 0x1a60
+  __AUTH_CONST.__auth_got: 0xfe8
+  __AUTH.__objc_data: 0x358
+  __DATA.__objc_ivar: 0xe44
+  __DATA.__data: 0x1ac0
   __DATA_DIRTY.__objc_data: 0x4810
   __DATA_DIRTY.__data: 0x2e8
   __DATA_DIRTY.__bss: 0x668

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5329
-  Symbols:   9989
-  CStrings:  3836
+  Functions: 5410
+  Symbols:   10136
+  CStrings:  3923
 
Symbols:
+ +[CSCompanionRuntimeThresholdKeys _originatingPlatformForSelfPlatform:servingPlatform:]
+ +[CSCompanionRuntimeThresholdKeys devicePrefixForPlatform:]
+ +[CSCompanionRuntimeThresholdKeys micSourceForRecordRoute:]
+ +[CSCompanionRuntimeThresholdKeys overrideKeyForSelfPlatform:servingPlatform:recordRoute:]
+ +[CSCompanionRuntimeThresholdKeys sectionKeysForSelfPlatform:servingPlatform:recordRoute:]
+ +[CSLinwoodEnabledAndAvailableMonitor sharedInstance]
+ +[CSRequestMutex CSRequestMutexOwnerDescription:]
+ +[CSRequestMutex CSRequestMutexOwnerShortName:]
+ +[CSRequestMutexController CSRequestMutexControllerResourceTypeDescription:]
+ +[CSRequestMutexController DefaultHoldTimeInMillisForResourceTypeDescription:]
+ +[CSRequestMutexController MaxHoldTimeInMillisForResourceTypeDescription:]
+ +[CSRequestMutexController sharedInstance]
+ +[CSUtils isDeviceSelectionParticipating]
+ +[CSUtils isDeviceSelectionShadowModeEnabled]
+ +[CSUtils isRequestLockEnforcingSingleTenancyEnabled]
+ +[CSUtils shouldExcludeBSSChannelsFromVoiceTrigger]
+ +[CSUtils supportMindPalaceAmbient]
+ +[CSUtils supportsVoiceTriggerAssetChannelSelection]
+ +[CSVoiceTriggerFirstPassConfigDecoder _processingChannelsBitSetWithoutBSS:]
+ +[CSVoiceTriggerFirstPassConfigDecoder decodeConfigFrom:shouldExcludeBSSChannels:]
+ +[CSVoiceTriggerFirstPassConfigDecoder decodeConfigFrom:shouldExcludeBSSChannels:isLinwoodEnabledAndAvailable:]
+ -[CSAudioPowerProvider _deactivateLocked]
+ -[CSAudioStartStreamOption serverAudioSentByClient]
+ -[CSAudioStartStreamOption setServerAudioSentByClient:]
+ -[CSFPreferences deviceSelectionTriggerAudioSliceMs]
+ -[CSFPreferences selfTapGainOverride]
+ -[CSFPreferences spectralMeterNormalizationEnabledOverride]
+ -[CSLinwoodEnabledAndAvailableMonitor _checkLinwoodEnabledAndAvailable]
+ -[CSLinwoodEnabledAndAvailableMonitor _didReceiveSiriCapabilitiesChanged]
+ -[CSLinwoodEnabledAndAvailableMonitor _notifyObserver:withEnabledAndAvailable:]
+ -[CSLinwoodEnabledAndAvailableMonitor _startMonitoringWithQueue:]
+ -[CSLinwoodEnabledAndAvailableMonitor _stopMonitoring]
+ -[CSLinwoodEnabledAndAvailableMonitor init]
+ -[CSLinwoodEnabledAndAvailableMonitor isEnabledAndAvailable]
+ -[CSRequestMutex .cxx_destruct]
+ -[CSRequestMutex _armAutoReleaseForOwner:generation:holdTimeInMillis:]
+ -[CSRequestMutex _clearOwnerLocked]
+ -[CSRequestMutex _notifyOwnerDidChangeFrom:to:]
+ -[CSRequestMutex _tryAcquireForOwner:client:requestId:holdTimeInMillis:]
+ -[CSRequestMutex initWithSingleTenancyEnforced:]
+ -[CSRequestMutex init]
+ -[CSRequestMutex ownerRequestId]
+ -[CSRequestMutex registerObserver:]
+ -[CSRequestMutex releaseAllForRemoteClient:]
+ -[CSRequestMutex releaseForOwner:requestId:]
+ -[CSRequestMutex releaseForRemoteClient:requestId:isCompanionRequest:]
+ -[CSRequestMutex releaseForRequestId:]
+ -[CSRequestMutex requestMutexOwner]
+ -[CSRequestMutex tryAcquireForCompanionWithRequestId:holdTimeInMillis:]
+ -[CSRequestMutex tryAcquireForLocalWithRequestId:holdTimeInMillis:]
+ -[CSRequestMutex tryAcquireForOwner:requestId:holdTimeInMillis:]
+ -[CSRequestMutex tryAcquireForRemoteClient:requestId:isCompanionRequest:holdTimeInMillis:]
+ -[CSRequestMutex unregisterObserver:]
+ -[CSRequestMutexController .cxx_destruct]
+ -[CSRequestMutexController _aggregateOwnersRuntimeType]
+ -[CSRequestMutexController _areAllResourcesAvailableToAcquireByOwner:resourceType:]
+ -[CSRequestMutexController _publishAggregateOwnerIfChanged]
+ -[CSRequestMutexController _resourceOwnerDescription]
+ -[CSRequestMutexController areAllResourcesAvailableToAcquireByOwner:resourceType:]
+ -[CSRequestMutexController dealloc]
+ -[CSRequestMutexController initWithSingleTenancyEnforced:]
+ -[CSRequestMutexController init]
+ -[CSRequestMutexController registerObserver:]
+ -[CSRequestMutexController releaseAllForRemoteClient:]
+ -[CSRequestMutexController releaseForOwner:requestId:resourceType:]
+ -[CSRequestMutexController releaseForRemoteClient:requestId:isCompanionRequest:resourceType:]
+ -[CSRequestMutexController releaseForRequestId:resourceType:]
+ -[CSRequestMutexController releaseIfHeldForRequestId:resourceType:]
+ -[CSRequestMutexController requestMutexOwnerDidChange:]
+ -[CSRequestMutexController tryAcquireForCompanionWithRequestId:resourceType:]
+ -[CSRequestMutexController tryAcquireForLocalWithRequestId:resourceType:]
+ -[CSRequestMutexController tryAcquireForOwner:requestId:resourceType:]
+ -[CSRequestMutexController tryAcquireForRemoteClient:requestId:isCompanionRequest:resourceType:holdTimeInMillis:]
+ -[CSRequestMutexController unregisterObserver:]
+ -[CSVoiceTriggerSecondPassConfig allowedChannelsBitsetLinwood]
+ -[CSVoiceTriggerSecondPassConfig allowedChannelsBitset]
+ -[CSVoiceTriggerSecondPassConfig initWithPreTriggerAudioTime:prependingAudioTime:trailingAudioTime:resourcePath:configPathNDAPI:useRecognizerCombination:configPathRecognizer:useKeywordSpotting:phraseConfigs:wearerDetectionConfig:quasarCheckerResultCutOffCount:useTimeBasedTriggerLength:allowedChannelsBitset:allowedChannelsBitsetLinwood:]
+ GCC_except_table1376
+ GCC_except_table1407
+ GCC_except_table1490
+ GCC_except_table1494
+ GCC_except_table1495
+ GCC_except_table1496
+ GCC_except_table1498
+ GCC_except_table1499
+ GCC_except_table1502
+ GCC_except_table1510
+ GCC_except_table1519
+ GCC_except_table1521
+ GCC_except_table1522
+ GCC_except_table1525
+ GCC_except_table1526
+ GCC_except_table1527
+ GCC_except_table1529
+ GCC_except_table1533
+ GCC_except_table1545
+ GCC_except_table1940
+ GCC_except_table1942
+ GCC_except_table1943
+ GCC_except_table1944
+ GCC_except_table1948
+ GCC_except_table1951
+ GCC_except_table1952
+ GCC_except_table1960
+ GCC_except_table1967
+ GCC_except_table1969
+ GCC_except_table1970
+ GCC_except_table1985
+ GCC_except_table1991
+ GCC_except_table2079
+ GCC_except_table2084
+ GCC_except_table2149
+ GCC_except_table2161
+ GCC_except_table2203
+ GCC_except_table2204
+ GCC_except_table2206
+ GCC_except_table2207
+ GCC_except_table2213
+ GCC_except_table2224
+ GCC_except_table2231
+ GCC_except_table2274
+ GCC_except_table2292
+ GCC_except_table2373
+ GCC_except_table2485
+ GCC_except_table2520
+ GCC_except_table2691
+ GCC_except_table2695
+ GCC_except_table2774
+ GCC_except_table2785
+ GCC_except_table2787
+ GCC_except_table2794
+ GCC_except_table2807
+ GCC_except_table2814
+ GCC_except_table2816
+ GCC_except_table2834
+ GCC_except_table2855
+ GCC_except_table2902
+ GCC_except_table2906
+ GCC_except_table2959
+ GCC_except_table2961
+ GCC_except_table2962
+ GCC_except_table3130
+ GCC_except_table3271
+ GCC_except_table3279
+ GCC_except_table3297
+ GCC_except_table3301
+ GCC_except_table3303
+ GCC_except_table3304
+ GCC_except_table3340
+ GCC_except_table3346
+ GCC_except_table3410
+ GCC_except_table3414
+ GCC_except_table3469
+ GCC_except_table3481
+ GCC_except_table3485
+ GCC_except_table3492
+ GCC_except_table3504
+ GCC_except_table3528
+ GCC_except_table3529
+ GCC_except_table3530
+ GCC_except_table3531
+ GCC_except_table3556
+ GCC_except_table3569
+ GCC_except_table3761
+ GCC_except_table3821
+ GCC_except_table3877
+ GCC_except_table3878
+ GCC_except_table3907
+ GCC_except_table3908
+ GCC_except_table3910
+ GCC_except_table3914
+ GCC_except_table3915
+ GCC_except_table3938
+ GCC_except_table3940
+ GCC_except_table3945
+ GCC_except_table3946
+ GCC_except_table3947
+ GCC_except_table3955
+ GCC_except_table3981
+ GCC_except_table4028
+ GCC_except_table4048
+ GCC_except_table4049
+ GCC_except_table4050
+ GCC_except_table4051
+ GCC_except_table4061
+ GCC_except_table4152
+ GCC_except_table4164
+ GCC_except_table4165
+ GCC_except_table4176
+ GCC_except_table4181
+ GCC_except_table4182
+ GCC_except_table4185
+ GCC_except_table4186
+ GCC_except_table4192
+ GCC_except_table4193
+ GCC_except_table4195
+ GCC_except_table4197
+ GCC_except_table4198
+ GCC_except_table4200
+ GCC_except_table4201
+ GCC_except_table4204
+ GCC_except_table4205
+ GCC_except_table4209
+ GCC_except_table4210
+ GCC_except_table4212
+ GCC_except_table4213
+ GCC_except_table4214
+ GCC_except_table4216
+ GCC_except_table4217
+ GCC_except_table4219
+ GCC_except_table4220
+ GCC_except_table4221
+ GCC_except_table4222
+ GCC_except_table4250
+ GCC_except_table4300
+ GCC_except_table4304
+ GCC_except_table4363
+ GCC_except_table4364
+ GCC_except_table4365
+ GCC_except_table4366
+ GCC_except_table4368
+ GCC_except_table4369
+ GCC_except_table4393
+ GCC_except_table4400
+ GCC_except_table4402
+ GCC_except_table4415
+ GCC_except_table4424
+ GCC_except_table4426
+ GCC_except_table4427
+ GCC_except_table4428
+ GCC_except_table4429
+ GCC_except_table4430
+ GCC_except_table4431
+ GCC_except_table4434
+ GCC_except_table4437
+ GCC_except_table4439
+ GCC_except_table4443
+ GCC_except_table4445
+ GCC_except_table4446
+ GCC_except_table4448
+ GCC_except_table4450
+ GCC_except_table4452
+ GCC_except_table4461
+ GCC_except_table4474
+ GCC_except_table4475
+ GCC_except_table4477
+ GCC_except_table4478
+ GCC_except_table4480
+ GCC_except_table4482
+ GCC_except_table4483
+ GCC_except_table4489
+ GCC_except_table4491
+ GCC_except_table4495
+ GCC_except_table4496
+ GCC_except_table4526
+ GCC_except_table4665
+ GCC_except_table4672
+ GCC_except_table4755
+ GCC_except_table4843
+ GCC_except_table4899
+ GCC_except_table4900
+ GCC_except_table4901
+ GCC_except_table4903
+ GCC_except_table4904
+ GCC_except_table4905
+ GCC_except_table4906
+ GCC_except_table4907
+ GCC_except_table4909
+ GCC_except_table4911
+ GCC_except_table4912
+ GCC_except_table4914
+ GCC_except_table4916
+ GCC_except_table4917
+ GCC_except_table4919
+ GCC_except_table4955
+ GCC_except_table5021
+ GCC_except_table5026
+ GCC_except_table5067
+ GCC_except_table5133
+ GCC_except_table545
+ GCC_except_table582
+ GCC_except_table585
+ GCC_except_table590
+ GCC_except_table608
+ GCC_except_table676
+ GCC_except_table680
+ GCC_except_table687
+ GCC_except_table850
+ GCC_except_table857
+ GCC_except_table920
+ GCC_except_table921
+ GCC_except_table928
+ GCC_except_table944
+ GCC_except_table945
+ GCC_except_table952
+ GCC_except_table956
+ GCC_except_table957
+ GCC_except_table961
+ GCC_except_table965
+ GCC_except_table966
+ GCC_except_table980
+ _AFDeviceSelectionParticipating
+ _AFIsLinwoodEnabledAndAvailable
+ _OBJC_CLASS_$_CSCompanionRuntimeThresholdKeys
+ _OBJC_CLASS_$_CSLinwoodEnabledAndAvailableMonitor
+ _OBJC_CLASS_$_CSRequestMutex
+ _OBJC_CLASS_$_CSRequestMutexController
+ _OBJC_IVAR_$_CSAudioPowerProvider._cachedSpectralNormalizationEnabledOverride
+ _OBJC_IVAR_$_CSAudioPowerProvider._deactivateLock
+ _OBJC_IVAR_$_CSAudioPowerProvider._selfTapGain
+ _OBJC_IVAR_$_CSAudioPowerProvider._selfTapScratchBuffer
+ _OBJC_IVAR_$_CSAudioPowerProvider._selfTapScratchCapacity
+ _OBJC_IVAR_$_CSAudioPowerProvider._unconfiguredPowerMeterDropHeartbeat
+ _OBJC_IVAR_$_CSAudioStartStreamOption._serverAudioSentByClient
+ _OBJC_IVAR_$_CSLinwoodEnabledAndAvailableMonitor._isLinwoodEnabledAndAvailable
+ _OBJC_IVAR_$_CSRequestMutex._autoReleaseQueue
+ _OBJC_IVAR_$_CSRequestMutex._generation
+ _OBJC_IVAR_$_CSRequestMutex._lock
+ _OBJC_IVAR_$_CSRequestMutex._observers
+ _OBJC_IVAR_$_CSRequestMutex._ownersRequestId
+ _OBJC_IVAR_$_CSRequestMutex._ownersRuntimeType
+ _OBJC_IVAR_$_CSRequestMutex._ownersXPCConnectionId
+ _OBJC_IVAR_$_CSRequestMutex._singleTenancyEnforced
+ _OBJC_IVAR_$_CSRequestMutexController._lock
+ _OBJC_IVAR_$_CSRequestMutexController._observerNotificationQueue
+ _OBJC_IVAR_$_CSRequestMutexController._observers
+ _OBJC_IVAR_$_CSRequestMutexController._publishedOwnersRuntimeType
+ _OBJC_IVAR_$_CSRequestMutexController._requestMutexes
+ _OBJC_IVAR_$_CSRequestMutexController._singleTenancyEnforced
+ _OBJC_IVAR_$_CSVoiceTriggerSecondPassConfig._allowedChannelsBitset
+ _OBJC_IVAR_$_CSVoiceTriggerSecondPassConfig._allowedChannelsBitsetLinwood
+ _OBJC_METACLASS_$_CSCompanionRuntimeThresholdKeys
+ _OBJC_METACLASS_$_CSLinwoodEnabledAndAvailableMonitor
+ _OBJC_METACLASS_$_CSRequestMutex
+ _OBJC_METACLASS_$_CSRequestMutexController
+ __OBJC_$_CLASS_METHODS_CSCompanionRuntimeThresholdKeys
+ __OBJC_$_CLASS_METHODS_CSLinwoodEnabledAndAvailableMonitor
+ __OBJC_$_CLASS_METHODS_CSRequestMutex
+ __OBJC_$_CLASS_METHODS_CSRequestMutexController
+ __OBJC_$_INSTANCE_METHODS_CSLinwoodEnabledAndAvailableMonitor
+ __OBJC_$_INSTANCE_METHODS_CSRequestMutex
+ __OBJC_$_INSTANCE_METHODS_CSRequestMutexController
+ __OBJC_$_INSTANCE_VARIABLES_CSLinwoodEnabledAndAvailableMonitor
+ __OBJC_$_INSTANCE_VARIABLES_CSRequestMutex
+ __OBJC_$_INSTANCE_VARIABLES_CSRequestMutexController
+ __OBJC_$_PROP_LIST_CSRequestMutex
+ __OBJC_$_PROP_LIST_CSRequestMutexController
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSRequestMutexObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSRequestMutexObserver
+ __OBJC_$_PROTOCOL_REFS_CSRequestMutexObserver
+ __OBJC_CLASS_PROTOCOLS_$_CSRequestMutexController
+ __OBJC_CLASS_RO_$_CSCompanionRuntimeThresholdKeys
+ __OBJC_CLASS_RO_$_CSLinwoodEnabledAndAvailableMonitor
+ __OBJC_CLASS_RO_$_CSRequestMutex
+ __OBJC_CLASS_RO_$_CSRequestMutexController
+ __OBJC_LABEL_PROTOCOL_$_CSRequestMutexObserver
+ __OBJC_METACLASS_RO_$_CSCompanionRuntimeThresholdKeys
+ __OBJC_METACLASS_RO_$_CSLinwoodEnabledAndAvailableMonitor
+ __OBJC_METACLASS_RO_$_CSRequestMutex
+ __OBJC_METACLASS_RO_$_CSRequestMutexController
+ __OBJC_PROTOCOL_$_CSRequestMutexObserver
+ ___42+[CSRequestMutexController sharedInstance]_block_invoke
+ ___52-[CSFPreferences deviceSelectionTriggerAudioSliceMs]_block_invoke
+ ___53+[CSLinwoodEnabledAndAvailableMonitor sharedInstance]_block_invoke
+ ___53+[CSUtils isRequestLockEnforcingSingleTenancyEnabled]_block_invoke
+ ___55-[CSRequestMutexController requestMutexOwnerDidChange:]_block_invoke
+ ___70-[CSRequestMutex _armAutoReleaseForOwner:generation:holdTimeInMillis:]_block_invoke
+ ___73-[CSLinwoodEnabledAndAvailableMonitor _didReceiveSiriCapabilitiesChanged]_block_invoke
+ ___block_descriptor_100_e100_i28?0r^{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}8I16r^{AudioBufferList=I[1{AudioBuffer=II^v}]}20l
+ ___block_descriptor_57_e8_32s_e5_v8?0ls32l8
+ __siriCapabilitiesDidChange
+ _deviceSelectionTriggerAudioSliceMs.durationMs
+ _deviceSelectionTriggerAudioSliceMs.onceToken
+ _isRequestLockEnforcingSingleTenancyEnabled.onceToken
+ _isRequestLockEnforcingSingleTenancyEnabled.result
+ _kAFSiriCapabilitiesDidChangeNotification
+ _os_unfair_recursive_lock_lock_with_options
+ _os_unfair_recursive_lock_unlock
- +[CSUtils isDeviceSelectionEnabled]
- -[CSFPreferences deviceSelectionShazamDuration]
- -[CSVoiceTriggerSecondPassConfig initWithPreTriggerAudioTime:prependingAudioTime:trailingAudioTime:resourcePath:configPathNDAPI:useRecognizerCombination:configPathRecognizer:useKeywordSpotting:phraseConfigs:wearerDetectionConfig:quasarCheckerResultCutOffCount:useTimeBasedTriggerLength:]
- GCC_except_table1363
- GCC_except_table1394
- GCC_except_table1477
- GCC_except_table1481
- GCC_except_table1482
- GCC_except_table1483
- GCC_except_table1484
- GCC_except_table1485
- GCC_except_table1486
- GCC_except_table1487
- GCC_except_table1488
- GCC_except_table1489
- GCC_except_table1506
- GCC_except_table1508
- GCC_except_table1509
- GCC_except_table1512
- GCC_except_table1516
- GCC_except_table1520
- GCC_except_table1532
- GCC_except_table1927
- GCC_except_table1928
- GCC_except_table1929
- GCC_except_table1930
- GCC_except_table1931
- GCC_except_table1935
- GCC_except_table1938
- GCC_except_table1939
- GCC_except_table1947
- GCC_except_table1956
- GCC_except_table1957
- GCC_except_table1972
- GCC_except_table1978
- GCC_except_table2066
- GCC_except_table2071
- GCC_except_table2134
- GCC_except_table2146
- GCC_except_table2188
- GCC_except_table2189
- GCC_except_table2191
- GCC_except_table2192
- GCC_except_table2198
- GCC_except_table2209
- GCC_except_table2216
- GCC_except_table2259
- GCC_except_table2277
- GCC_except_table2358
- GCC_except_table2470
- GCC_except_table2505
- GCC_except_table2676
- GCC_except_table2680
- GCC_except_table2759
- GCC_except_table2770
- GCC_except_table2772
- GCC_except_table2777
- GCC_except_table2779
- GCC_except_table2799
- GCC_except_table2801
- GCC_except_table2819
- GCC_except_table2840
- GCC_except_table2887
- GCC_except_table2891
- GCC_except_table2944
- GCC_except_table2946
- GCC_except_table2947
- GCC_except_table3113
- GCC_except_table3254
- GCC_except_table3262
- GCC_except_table3270
- GCC_except_table3280
- GCC_except_table3284
- GCC_except_table3286
- GCC_except_table3323
- GCC_except_table3329
- GCC_except_table3390
- GCC_except_table3394
- GCC_except_table3449
- GCC_except_table3461
- GCC_except_table3465
- GCC_except_table3472
- GCC_except_table3484
- GCC_except_table3508
- GCC_except_table3509
- GCC_except_table3510
- GCC_except_table3511
- GCC_except_table3536
- GCC_except_table3549
- GCC_except_table3719
- GCC_except_table3779
- GCC_except_table3793
- GCC_except_table3836
- GCC_except_table3865
- GCC_except_table3866
- GCC_except_table3868
- GCC_except_table3871
- GCC_except_table3872
- GCC_except_table3873
- GCC_except_table3896
- GCC_except_table3898
- GCC_except_table3903
- GCC_except_table3904
- GCC_except_table3905
- GCC_except_table3939
- GCC_except_table3965
- GCC_except_table3986
- GCC_except_table4006
- GCC_except_table4008
- GCC_except_table4009
- GCC_except_table4019
- GCC_except_table4110
- GCC_except_table4111
- GCC_except_table4120
- GCC_except_table4122
- GCC_except_table4123
- GCC_except_table4124
- GCC_except_table4125
- GCC_except_table4128
- GCC_except_table4129
- GCC_except_table4132
- GCC_except_table4133
- GCC_except_table4134
- GCC_except_table4135
- GCC_except_table4136
- GCC_except_table4137
- GCC_except_table4138
- GCC_except_table4139
- GCC_except_table4140
- GCC_except_table4143
- GCC_except_table4144
- GCC_except_table4150
- GCC_except_table4151
- GCC_except_table4155
- GCC_except_table4156
- GCC_except_table4158
- GCC_except_table4159
- GCC_except_table4163
- GCC_except_table4168
- GCC_except_table4172
- GCC_except_table4258
- GCC_except_table4262
- GCC_except_table4313
- GCC_except_table4314
- GCC_except_table4321
- GCC_except_table4322
- GCC_except_table4323
- GCC_except_table4324
- GCC_except_table4326
- GCC_except_table4327
- GCC_except_table4348
- GCC_except_table4350
- GCC_except_table4351
- GCC_except_table4352
- GCC_except_table4354
- GCC_except_table4357
- GCC_except_table4358
- GCC_except_table4359
- GCC_except_table4360
- GCC_except_table4361
- GCC_except_table4373
- GCC_except_table4382
- GCC_except_table4384
- GCC_except_table4385
- GCC_except_table4386
- GCC_except_table4387
- GCC_except_table4388
- GCC_except_table4389
- GCC_except_table4395
- GCC_except_table4404
- GCC_except_table4406
- GCC_except_table4408
- GCC_except_table4410
- GCC_except_table4412
- GCC_except_table4419
- GCC_except_table4433
- GCC_except_table4435
- GCC_except_table4442
- GCC_except_table4447
- GCC_except_table4449
- GCC_except_table4453
- GCC_except_table4596
- GCC_except_table4603
- GCC_except_table4686
- GCC_except_table4753
- GCC_except_table4763
- GCC_except_table4819
- GCC_except_table4820
- GCC_except_table4821
- GCC_except_table4823
- GCC_except_table4824
- GCC_except_table4825
- GCC_except_table4826
- GCC_except_table4827
- GCC_except_table4828
- GCC_except_table4830
- GCC_except_table4831
- GCC_except_table4835
- GCC_except_table4836
- GCC_except_table4838
- GCC_except_table4874
- GCC_except_table4940
- GCC_except_table4945
- GCC_except_table4986
- GCC_except_table5052
- GCC_except_table543
- GCC_except_table580
- GCC_except_table583
- GCC_except_table588
- GCC_except_table606
- GCC_except_table674
- GCC_except_table678
- GCC_except_table683
- GCC_except_table848
- GCC_except_table855
- GCC_except_table918
- GCC_except_table919
- GCC_except_table926
- GCC_except_table941
- GCC_except_table942
- GCC_except_table947
- GCC_except_table948
- GCC_except_table954
- GCC_except_table958
- GCC_except_table959
- GCC_except_table963
- GCC_except_table978
- ___47-[CSFPreferences deviceSelectionShazamDuration]_block_invoke
- ___block_descriptor_80_e100_i28?0r^{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}8I16r^{AudioBufferList=I[1{AudioBuffer=II^v}]}20l
- _deviceSelectionShazamDuration.atoaDuration
- _deviceSelectionShazamDuration.onceToken
CStrings:
+ "#5\xb1B"
+ "%s #requestLock aggregate owner changed from %s to %s, notifying %lu observer(s)"
+ "%s #requestLock hold of %ld ms for %s expiry superseded, no-op"
+ "%s #requestLock hold of %ld ms for %s request %@ expired: the request that took the hold over never released it, owner now is none"
+ "%s #requestLock hold of %ld ms for %s request %@ expired: the reserving client never started a request, owner now is none"
+ "%s #requestLock lock owner changed but aggregate owner unchanged: %s, %@"
+ "%s #requestLock owner changed from %s to %s, notifying %lu observer(s)"
+ "%s #requestLock releaseAllForRemoteClient: remote client went away holding %s ownership, owner now is none"
+ "%s #requestLock releaseForOwner: %s, requestId: %@, resource: %s, %@"
+ "%s #requestLock releaseForOwner: no-op for %@, nobody holds the mutex"
+ "%s #requestLock releaseForOwner: no-op for %s request %@, %s holds the mutex for %@"
+ "%s #requestLock releaseForOwner: released %s ownership held by %@, released by %@, owner now is none"
+ "%s #requestLock releaseForRemoteClient: %s, requestId: %@, resource: %s, %@"
+ "%s #requestLock releaseForRemoteClient: no-op, remote client does not hold %s ownership for %@ (held for %@)"
+ "%s #requestLock releaseForRemoteClient: released %s ownership held for %@, owner now is none"
+ "%s #requestLock releaseForRequestId: no-op for %@, nobody holds the mutex"
+ "%s #requestLock releaseForRequestId: released %s ownership held by %@, released by %@, owner now is none"
+ "%s #requestLock releaseForRequestId: requestId: %@, resource: %s, %@"
+ "%s #requestLock releaseIfHeldForRequestId: requestId: %@, resource: %s, held for it: %d, %@"
+ "%s #requestLock resource %s is unavailable to owner %s b/c resource %s is already held by %s."
+ "%s #requestLock resources disagree on owner: %s and %s both hold one, reporting %s"
+ "%s #requestLock tryAcquire called when feature, RequestLockEnforcingSingleTenancyEnabled, not enabled"
+ "%s #requestLock tryAcquire for %s request %@: acquired (previous owner: %s for %@, holdTimeInMillis: %ld, remote client: %d)"
+ "%s #requestLock tryAcquire for %s request %@: blocked, %s currently owns the mutex for %@"
+ "%s #requestLock tryAcquireForOwner: %s, requestId: %@, resource: %s, succeeded: %i, %@"
+ "%s #requestLock tryAcquireForRemoteClient: %s, requestId: %@, resource: %s, succeeded: %i, %@"
+ "%s #requestLock tryAcquireForRemoteClient: rejected, no xpcConnectionId supplied"
+ "%s Failed to allocate SelfTap gain scratch buffer; falling back to unity gain"
+ "%s Ignoring asset processingChannelsBitset=0x%{public}llx, using 0x%{public}llx"
+ "%s Ignoring invalid selfTapGainOverride %.3f; using unity gain"
+ "%s Linwood enabled and available changed to %{public}@"
+ "%s Linwood is enabled and available, processingChannelsBitset=0x%{public}llx"
+ "%s Moving-window normalization %{public}s by override for route '%{public}@'"
+ "%s Power meter is not configured yet, dropping audio chunk, heartbeat = %llu"
+ "%s Second pass allowedChannelsBitset=0x%{public}llx, allowedChannelsBitset_linwood=0x%{public}llx"
+ "%s Secure sensor not allowed within %{public}.0fms, last status = %{public}d"
+ "%s SelfTap gain override applied: %.3fx (%.2f dB)"
+ "%s Start monitoring: Linwood enabled and available, Linwood is %{public}@"
+ "%s Stop monitoring: Linwood enabled and available"
+ "+[CSVoiceTriggerFirstPassConfigDecoder decodeConfigFrom:shouldExcludeBSSChannels:isLinwoodEnabledAndAvailable:]"
+ "-[CSAudioPowerProvider _deactivateLocked]"
+ "-[CSLinwoodEnabledAndAvailableMonitor _didReceiveSiriCapabilitiesChanged]"
+ "-[CSLinwoodEnabledAndAvailableMonitor _startMonitoringWithQueue:]"
+ "-[CSLinwoodEnabledAndAvailableMonitor _stopMonitoring]"
+ "-[CSRequestMutex _armAutoReleaseForOwner:generation:holdTimeInMillis:]_block_invoke"
+ "-[CSRequestMutex _notifyOwnerDidChangeFrom:to:]"
+ "-[CSRequestMutex _tryAcquireForOwner:client:requestId:holdTimeInMillis:]"
+ "-[CSRequestMutex releaseAllForRemoteClient:]"
+ "-[CSRequestMutex releaseForOwner:requestId:]"
+ "-[CSRequestMutex releaseForRemoteClient:requestId:isCompanionRequest:]"
+ "-[CSRequestMutex releaseForRequestId:]"
+ "-[CSRequestMutex tryAcquireForRemoteClient:requestId:isCompanionRequest:holdTimeInMillis:]"
+ "-[CSRequestMutexController _aggregateOwnersRuntimeType]"
+ "-[CSRequestMutexController _areAllResourcesAvailableToAcquireByOwner:resourceType:]"
+ "-[CSRequestMutexController _publishAggregateOwnerIfChanged]"
+ "-[CSRequestMutexController releaseForOwner:requestId:resourceType:]"
+ "-[CSRequestMutexController releaseForRemoteClient:requestId:isCompanionRequest:resourceType:]"
+ "-[CSRequestMutexController releaseForRequestId:resourceType:]"
+ "-[CSRequestMutexController releaseIfHeldForRequestId:resourceType:]"
+ "-[CSRequestMutexController tryAcquireForOwner:requestId:resourceType:]"
+ "-[CSRequestMutexController tryAcquireForRemoteClient:requestId:isCompanionRequest:resourceType:holdTimeInMillis:]"
+ "BluetoothDoAP"
+ "BuiltIn"
+ "CSRequestMutex.autoRelease"
+ "CSRequestMutexController.observerNotification"
+ "Device Selection Trigger Audio Slice Ms"
+ "[serverAudioSentByClient = %@]"
+ "allowedChannelsBitset"
+ "allowedChannelsBitset_linwood"
+ "appletv"
+ "audio"
+ "audioaccessory"
+ "companion"
+ "enabled and available"
+ "homeaccessory"
+ "ipad"
+ "iphone"
+ "local"
+ "none"
+ "not enabled or not available"
+ "override_selftap_gain"
+ "processingChannelsBitset_linwood"
+ "request_lock"
+ "resourceOwners: (%c, %c, %c)"
+ "serverAudioSentByClient"
+ "spectral_meter_normalization_enabled"
+ "support_mindpalace_ambient"
+ "unspecified"
+ "vision"
+ "watch"
- "+[CSVoiceTriggerFirstPassConfigDecoder decodeConfigFrom:]"
- "-[CSAudioPowerProvider deactivate]"
- "Device Selection Shazam Duration"
```
