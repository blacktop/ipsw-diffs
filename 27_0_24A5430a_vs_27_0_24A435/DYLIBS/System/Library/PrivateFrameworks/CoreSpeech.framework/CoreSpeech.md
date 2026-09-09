## CoreSpeech

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech`

```diff

 3600.70.47.11.1
-  __TEXT.__text: 0x149fb4
+  __TEXT.__text: 0x14d1ec
   __TEXT.__lazy_helpers: 0x54
-  __TEXT.__objc_methlist: 0x14cac
+  __TEXT.__objc_methlist: 0x1508c
   __TEXT.__const: 0x42c
   __TEXT.__dlopen_cstrs: 0x1e0
-  __TEXT.__gcc_except_tab: 0x3170
-  __TEXT.__cstring: 0x289f4
-  __TEXT.__oslogstring: 0x1fe04
-  __TEXT.__unwind_info: 0x4f70
+  __TEXT.__gcc_except_tab: 0x3230
+  __TEXT.__cstring: 0x28ec2
+  __TEXT.__oslogstring: 0x20308
+  __TEXT.__unwind_info: 0x5010
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x4258
-  __DATA_CONST.__objc_classlist: 0x840
+  __DATA_CONST.__objc_classlist: 0x868
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x4e8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0xada8
+  __DATA_CONST.__objc_selrefs: 0xaea8
   __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA_CONST.__objc_superrefs: 0x678
+  __DATA_CONST.__objc_superrefs: 0x6a0
   __DATA_CONST.__objc_arraydata: 0x3e8
-  __DATA_CONST.__got: 0x1b28
-  __AUTH_CONST.__const: 0x1e40
-  __AUTH_CONST.__cfstring: 0x9680
-  __AUTH_CONST.__objc_const: 0x20cb8
+  __DATA_CONST.__got: 0x1b40
+  __AUTH_CONST.__const: 0x1f60
+  __AUTH_CONST.__cfstring: 0x96c0
+  __AUTH_CONST.__objc_const: 0x21458
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__lazy_load_got: 0x8
   __AUTH_CONST.__objc_intobj: 0x9a8

   __AUTH_CONST.__objc_floatobj: 0x4f0
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__auth_got: 0xda8
-  __AUTH.__objc_data: 0x3b10
-  __DATA.__objc_ivar: 0x1944
+  __AUTH.__objc_data: 0x3ca0
+  __DATA.__objc_ivar: 0x1998
   __DATA.__data: 0x3a74
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x1770

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8091
-  Symbols:   17809
-  CStrings:  5580
+  Functions: 8197
+  Symbols:   17978
+  CStrings:  5613
 
Symbols:
+ -[CSAlwaysOnProcessorEnabledWatchExclave .cxx_destruct]
+ -[CSAlwaysOnProcessorEnabledWatchExclave _addConditons]
+ -[CSAlwaysOnProcessorEnabledWatchExclave _handlePowerStateChange:]
+ -[CSAlwaysOnProcessorEnabledWatchExclave _subscribeToMonitors]
+ -[CSAlwaysOnProcessorEnabledWatchExclave init]
+ -[CSAlwaysOnProcessorEnabledWatchExclave queue]
+ -[CSAlwaysOnProcessorEnabledWatchExclave setQueue:]
+ -[CSAlwaysOnProcessorEnabledWatchExclave setSleepModeMonitor:]
+ -[CSAlwaysOnProcessorEnabledWatchExclave setWristStateMonitor:]
+ -[CSAlwaysOnProcessorEnabledWatchExclave sleepModeMonitor]
+ -[CSAlwaysOnProcessorEnabledWatchExclave wristStateMonitor]
+ -[CSRaiseToSpeakEnabledPolicyWatchExclave _addListeningEnabledConditions]
+ -[CSRaiseToSpeakEnabledPolicyWatchExclave _subscribeEventMonitors]
+ -[CSRaiseToSpeakEnabledPolicyWatchExclave init]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch .cxx_destruct]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch _addVoiceTriggerAPModeSuspendConditions]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch _handleClientRecordStateDidChange:eventUUID:]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch _handlePowerStateChange:]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch _isAudioRouteIneligibleForAP]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch _isHearstRoutedWithNoPhoneCall]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch _isInPhoneCallStateWithHeadset]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch _isSpeechDetectionDevicePresent]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch _subscribeEventMonitors]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch attSiriStateMonitor]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch audioRouteChangeMonitor]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch audiostreamActivityMonitor]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch batteryMonitor]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch builtinSpeakerStateMonitor]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch commandControlStreamEventMonitor]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch init]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch isSiriClientConsideredAsRecord]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch pendingRecordingStopUUID]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch phoneCallStateMonitor]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch phraseSpotterEnabledMonitor]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch playbackVolumeStatusMonitor]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch setAttSiriStateMonitor:]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch setAudioRouteChangeMonitor:]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch setAudiostreamActivityMonitor:]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch setBatteryMonitor:]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch setBuiltinSpeakerStateMonitor:]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch setCommandControlStreamEventMonitor:]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch setIsSiriClientConsideredAsRecord:]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch setPendingRecordingStopUUID:]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch setPhoneCallStateMonitor:]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch setPhraseSpotterEnabledMonitor:]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch setPlaybackVolumeStatusMonitor:]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch setSiriAssertionMonitor:]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch setSiriClientBehaviorMonitor:]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch setSleepModeMonitor:]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch setSpeechDetectionDevicePresentMonitor:]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch setWristStateMonitor:]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch siriAssertionMonitor]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch siriClientBehaviorMonitor:didChangedRecordState:withEventUUID:withContext:]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch siriClientBehaviorMonitor:didStartStreamWithContext:successfully:option:withEventUUID:]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch siriClientBehaviorMonitor:didStopStream:withEventUUID:]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch siriClientBehaviorMonitor:willStartStreamWithContext:option:]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch siriClientBehaviorMonitor:willStopStream:reason:]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch siriClientBehaviorMonitor]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch sleepModeMonitor]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch speechDetectionDevicePresentMonitor]
+ -[CSVoiceTriggerAPModeSuspendPolicyWatch wristStateMonitor]
+ -[CSVoiceTriggerActivationPolicyExclaveWatch .cxx_destruct]
+ -[CSVoiceTriggerActivationPolicyExclaveWatch CSAudioRouteChangeMonitor:didReceiveAudioRouteChangeEvent:]
+ -[CSVoiceTriggerActivationPolicyExclaveWatch CSVoiceTriggerXPCServiceProxy:bypassPhraseSpotter:]
+ -[CSVoiceTriggerActivationPolicyExclaveWatch CSVoiceTriggerXPCServiceProxy:bypassRaiseToSpeak:]
+ -[CSVoiceTriggerActivationPolicyExclaveWatch _addConditons]
+ -[CSVoiceTriggerActivationPolicyExclaveWatch _isExternalPhraseSpotterRunning:]
+ -[CSVoiceTriggerActivationPolicyExclaveWatch _subscribeToMonitors]
+ -[CSVoiceTriggerActivationPolicyExclaveWatch init]
+ -[CSVoiceTriggerActivationPolicyExclaveWatch queue]
+ -[CSVoiceTriggerActivationPolicyExclaveWatch setQueue:]
+ -[CSVoiceTriggerActivationPolicyExclaveWatch siriClientBehaviorMonitor:didStartStreamWithContext:successfully:option:withEventUUID:]
+ -[CSVoiceTriggerActivationPolicyExclaveWatch siriClientBehaviorMonitor:didStopStream:withEventUUID:]
+ -[CSVoiceTriggerActivationPolicyExclaveWatch siriClientBehaviorMonitor:willStartStreamWithContext:option:]
+ -[CSVoiceTriggerActivationPolicyExclaveWatch siriClientBehaviorMonitor:willStopStream:reason:]
+ -[CSVoiceTriggerEnabledPolicyWatchExclave _addListeningEnabledConditions]
+ -[CSVoiceTriggerEnabledPolicyWatchExclave _subscribeEventMonitors]
+ -[CSVoiceTriggerEnabledPolicyWatchExclave init]
+ GCC_except_table1562
+ GCC_except_table1617
+ GCC_except_table1641
+ GCC_except_table1645
+ GCC_except_table1661
+ GCC_except_table1664
+ GCC_except_table1694
+ GCC_except_table1792
+ GCC_except_table1794
+ GCC_except_table1796
+ GCC_except_table1802
+ GCC_except_table1862
+ GCC_except_table1888
+ GCC_except_table1894
+ GCC_except_table1975
+ GCC_except_table1995
+ GCC_except_table2111
+ GCC_except_table2260
+ GCC_except_table2290
+ GCC_except_table2293
+ GCC_except_table2296
+ GCC_except_table2301
+ GCC_except_table2313
+ GCC_except_table2318
+ GCC_except_table2321
+ GCC_except_table2413
+ GCC_except_table2419
+ GCC_except_table2459
+ GCC_except_table2462
+ GCC_except_table2466
+ GCC_except_table2484
+ GCC_except_table2517
+ GCC_except_table2679
+ GCC_except_table2691
+ GCC_except_table2722
+ GCC_except_table2758
+ GCC_except_table2792
+ GCC_except_table2793
+ GCC_except_table2794
+ GCC_except_table2795
+ GCC_except_table2796
+ GCC_except_table2800
+ GCC_except_table2803
+ GCC_except_table2806
+ GCC_except_table2807
+ GCC_except_table2810
+ GCC_except_table2811
+ GCC_except_table2820
+ GCC_except_table2826
+ GCC_except_table2828
+ GCC_except_table2829
+ GCC_except_table2899
+ GCC_except_table3165
+ GCC_except_table3243
+ GCC_except_table3280
+ GCC_except_table3313
+ GCC_except_table3316
+ GCC_except_table3319
+ GCC_except_table3350
+ GCC_except_table3410
+ GCC_except_table3642
+ GCC_except_table3668
+ GCC_except_table3731
+ GCC_except_table3733
+ GCC_except_table3751
+ GCC_except_table3755
+ GCC_except_table3757
+ GCC_except_table3759
+ GCC_except_table3763
+ GCC_except_table3774
+ GCC_except_table3777
+ GCC_except_table3783
+ GCC_except_table3785
+ GCC_except_table3787
+ GCC_except_table3789
+ GCC_except_table3791
+ GCC_except_table3793
+ GCC_except_table3794
+ GCC_except_table3795
+ GCC_except_table3796
+ GCC_except_table3798
+ GCC_except_table3799
+ GCC_except_table3800
+ GCC_except_table3803
+ GCC_except_table3804
+ GCC_except_table3805
+ GCC_except_table3806
+ GCC_except_table3807
+ GCC_except_table3808
+ GCC_except_table3809
+ GCC_except_table3811
+ GCC_except_table3812
+ GCC_except_table3820
+ GCC_except_table3825
+ GCC_except_table3826
+ GCC_except_table3827
+ GCC_except_table3828
+ GCC_except_table3969
+ GCC_except_table3993
+ GCC_except_table4059
+ GCC_except_table4075
+ GCC_except_table4096
+ GCC_except_table4188
+ GCC_except_table4440
+ GCC_except_table4511
+ GCC_except_table4512
+ GCC_except_table4516
+ GCC_except_table4519
+ GCC_except_table4523
+ GCC_except_table4548
+ GCC_except_table4601
+ GCC_except_table4607
+ GCC_except_table4677
+ GCC_except_table4881
+ GCC_except_table4888
+ GCC_except_table4895
+ GCC_except_table4901
+ GCC_except_table4984
+ GCC_except_table5144
+ GCC_except_table5154
+ GCC_except_table5178
+ GCC_except_table5198
+ GCC_except_table5295
+ GCC_except_table5322
+ GCC_except_table5330
+ GCC_except_table5332
+ GCC_except_table5336
+ GCC_except_table5338
+ GCC_except_table5349
+ GCC_except_table5350
+ GCC_except_table5355
+ GCC_except_table5362
+ GCC_except_table5367
+ GCC_except_table5369
+ GCC_except_table5371
+ GCC_except_table5373
+ GCC_except_table5374
+ GCC_except_table5375
+ GCC_except_table5376
+ GCC_except_table5378
+ GCC_except_table5379
+ GCC_except_table5380
+ GCC_except_table5381
+ GCC_except_table5382
+ GCC_except_table5384
+ GCC_except_table5385
+ GCC_except_table5386
+ GCC_except_table5388
+ GCC_except_table5403
+ GCC_except_table5434
+ GCC_except_table5491
+ GCC_except_table5495
+ GCC_except_table5549
+ GCC_except_table5579
+ GCC_except_table5582
+ GCC_except_table5672
+ GCC_except_table5686
+ GCC_except_table5693
+ GCC_except_table5705
+ GCC_except_table5709
+ GCC_except_table5719
+ GCC_except_table5948
+ GCC_except_table5981
+ GCC_except_table5986
+ GCC_except_table6023
+ GCC_except_table6032
+ GCC_except_table6062
+ GCC_except_table6130
+ GCC_except_table6272
+ GCC_except_table6375
+ GCC_except_table6383
+ GCC_except_table6403
+ GCC_except_table6408
+ GCC_except_table6514
+ GCC_except_table6569
+ GCC_except_table6649
+ GCC_except_table6671
+ GCC_except_table6672
+ GCC_except_table6682
+ GCC_except_table6683
+ GCC_except_table6695
+ GCC_except_table6726
+ GCC_except_table6737
+ GCC_except_table6742
+ GCC_except_table6747
+ GCC_except_table6775
+ GCC_except_table6847
+ GCC_except_table6859
+ GCC_except_table6882
+ GCC_except_table6893
+ GCC_except_table6896
+ GCC_except_table6919
+ GCC_except_table6931
+ GCC_except_table6978
+ GCC_except_table7226
+ GCC_except_table7262
+ GCC_except_table7335
+ GCC_except_table7389
+ GCC_except_table7412
+ GCC_except_table7453
+ GCC_except_table7464
+ GCC_except_table7608
+ GCC_except_table7616
+ GCC_except_table7732
+ GCC_except_table7733
+ GCC_except_table7734
+ GCC_except_table7735
+ GCC_except_table7736
+ GCC_except_table7741
+ GCC_except_table7804
+ GCC_except_table7850
+ GCC_except_table7858
+ GCC_except_table7864
+ GCC_except_table7889
+ GCC_except_table7895
+ GCC_except_table7901
+ GCC_except_table8039
+ _NSProcessInfoPowerStateDidChangeNotification
+ _OBJC_CLASS_$_CSAlwaysOnProcessorEnabledWatchExclave
+ _OBJC_CLASS_$_CSRaiseToSpeakEnabledPolicyWatchExclave
+ _OBJC_CLASS_$_CSVoiceTriggerAPModeSuspendPolicyWatch
+ _OBJC_CLASS_$_CSVoiceTriggerActivationPolicyExclaveWatch
+ _OBJC_CLASS_$_CSVoiceTriggerEnabledPolicyWatchExclave
+ _OBJC_IVAR_$_CSAlwaysOnProcessorEnabledWatchExclave._queue
+ _OBJC_IVAR_$_CSAlwaysOnProcessorEnabledWatchExclave._sleepModeMonitor
+ _OBJC_IVAR_$_CSAlwaysOnProcessorEnabledWatchExclave._wristStateMonitor
+ _OBJC_IVAR_$_CSVoiceTriggerAPModeSuspendPolicyWatch._attSiriStateMonitor
+ _OBJC_IVAR_$_CSVoiceTriggerAPModeSuspendPolicyWatch._audioRouteChangeMonitor
+ _OBJC_IVAR_$_CSVoiceTriggerAPModeSuspendPolicyWatch._audiostreamActivityMonitor
+ _OBJC_IVAR_$_CSVoiceTriggerAPModeSuspendPolicyWatch._batteryMonitor
+ _OBJC_IVAR_$_CSVoiceTriggerAPModeSuspendPolicyWatch._builtinSpeakerStateMonitor
+ _OBJC_IVAR_$_CSVoiceTriggerAPModeSuspendPolicyWatch._commandControlStreamEventMonitor
+ _OBJC_IVAR_$_CSVoiceTriggerAPModeSuspendPolicyWatch._isSiriClientConsideredAsRecord
+ _OBJC_IVAR_$_CSVoiceTriggerAPModeSuspendPolicyWatch._pendingRecordingStopUUID
+ _OBJC_IVAR_$_CSVoiceTriggerAPModeSuspendPolicyWatch._phoneCallStateMonitor
+ _OBJC_IVAR_$_CSVoiceTriggerAPModeSuspendPolicyWatch._phraseSpotterEnabledMonitor
+ _OBJC_IVAR_$_CSVoiceTriggerAPModeSuspendPolicyWatch._playbackVolumeStatusMonitor
+ _OBJC_IVAR_$_CSVoiceTriggerAPModeSuspendPolicyWatch._recordStateQueue
+ _OBJC_IVAR_$_CSVoiceTriggerAPModeSuspendPolicyWatch._siriAssertionMonitor
+ _OBJC_IVAR_$_CSVoiceTriggerAPModeSuspendPolicyWatch._siriClientBehaviorMonitor
+ _OBJC_IVAR_$_CSVoiceTriggerAPModeSuspendPolicyWatch._sleepModeMonitor
+ _OBJC_IVAR_$_CSVoiceTriggerAPModeSuspendPolicyWatch._speechDetectionDevicePresentMonitor
+ _OBJC_IVAR_$_CSVoiceTriggerAPModeSuspendPolicyWatch._wristStateMonitor
+ _OBJC_IVAR_$_CSVoiceTriggerActivationPolicyExclaveWatch._queue
+ _OBJC_METACLASS_$_CSAlwaysOnProcessorEnabledWatchExclave
+ _OBJC_METACLASS_$_CSRaiseToSpeakEnabledPolicyWatchExclave
+ _OBJC_METACLASS_$_CSVoiceTriggerAPModeSuspendPolicyWatch
+ _OBJC_METACLASS_$_CSVoiceTriggerActivationPolicyExclaveWatch
+ _OBJC_METACLASS_$_CSVoiceTriggerEnabledPolicyWatchExclave
+ __OBJC_$_INSTANCE_METHODS_CSAlwaysOnProcessorEnabledWatchExclave
+ __OBJC_$_INSTANCE_METHODS_CSRaiseToSpeakEnabledPolicyWatchExclave
+ __OBJC_$_INSTANCE_METHODS_CSVoiceTriggerAPModeSuspendPolicyWatch
+ __OBJC_$_INSTANCE_METHODS_CSVoiceTriggerActivationPolicyExclaveWatch
+ __OBJC_$_INSTANCE_METHODS_CSVoiceTriggerEnabledPolicyWatchExclave
+ __OBJC_$_INSTANCE_VARIABLES_CSAlwaysOnProcessorEnabledWatchExclave
+ __OBJC_$_INSTANCE_VARIABLES_CSVoiceTriggerAPModeSuspendPolicyWatch
+ __OBJC_$_INSTANCE_VARIABLES_CSVoiceTriggerActivationPolicyExclaveWatch
+ __OBJC_$_PROP_LIST_CSAlwaysOnProcessorEnabledWatchExclave
+ __OBJC_$_PROP_LIST_CSVoiceTriggerAPModeSuspendPolicyWatch
+ __OBJC_$_PROP_LIST_CSVoiceTriggerActivationPolicyExclaveWatch
+ __OBJC_CLASS_PROTOCOLS_$_CSVoiceTriggerAPModeSuspendPolicyWatch
+ __OBJC_CLASS_PROTOCOLS_$_CSVoiceTriggerActivationPolicyExclaveWatch
+ __OBJC_CLASS_RO_$_CSAlwaysOnProcessorEnabledWatchExclave
+ __OBJC_CLASS_RO_$_CSRaiseToSpeakEnabledPolicyWatchExclave
+ __OBJC_CLASS_RO_$_CSVoiceTriggerAPModeSuspendPolicyWatch
+ __OBJC_CLASS_RO_$_CSVoiceTriggerActivationPolicyExclaveWatch
+ __OBJC_CLASS_RO_$_CSVoiceTriggerEnabledPolicyWatchExclave
+ __OBJC_METACLASS_RO_$_CSAlwaysOnProcessorEnabledWatchExclave
+ __OBJC_METACLASS_RO_$_CSRaiseToSpeakEnabledPolicyWatchExclave
+ __OBJC_METACLASS_RO_$_CSVoiceTriggerAPModeSuspendPolicyWatch
+ __OBJC_METACLASS_RO_$_CSVoiceTriggerActivationPolicyExclaveWatch
+ __OBJC_METACLASS_RO_$_CSVoiceTriggerEnabledPolicyWatchExclave
+ ___100-[CSVoiceTriggerActivationPolicyExclaveWatch siriClientBehaviorMonitor:didStopStream:withEventUUID:]_block_invoke
+ ___104-[CSVoiceTriggerActivationPolicyExclaveWatch CSAudioRouteChangeMonitor:didReceiveAudioRouteChangeEvent:]_block_invoke
+ ___116-[CSVoiceTriggerAPModeSuspendPolicyWatch siriClientBehaviorMonitor:didChangedRecordState:withEventUUID:withContext:]_block_invoke
+ ___132-[CSVoiceTriggerActivationPolicyExclaveWatch siriClientBehaviorMonitor:didStartStreamWithContext:successfully:option:withEventUUID:]_block_invoke
+ ___55-[CSAlwaysOnProcessorEnabledWatchExclave _addConditons]_block_invoke
+ ___59-[CSVoiceTriggerActivationPolicyExclaveWatch _addConditons]_block_invoke
+ ___73-[CSRaiseToSpeakEnabledPolicyWatchExclave _addListeningEnabledConditions]_block_invoke
+ ___73-[CSVoiceTriggerEnabledPolicyWatchExclave _addListeningEnabledConditions]_block_invoke
+ ___81-[CSVoiceTriggerAPModeSuspendPolicyWatch _addVoiceTriggerAPModeSuspendConditions]_block_invoke
+ ___81-[CSVoiceTriggerAPModeSuspendPolicyWatch _addVoiceTriggerAPModeSuspendConditions]_block_invoke_2
+ ___86-[CSVoiceTriggerAPModeSuspendPolicyWatch _handleClientRecordStateDidChange:eventUUID:]_block_invoke
+ ___96-[CSVoiceTriggerActivationPolicyExclaveWatch CSVoiceTriggerXPCServiceProxy:bypassPhraseSpotter:]_block_invoke
+ _objc_msgSend$_addConditons
+ _objc_msgSend$_isExternalPhraseSpotterRunning:
+ _objc_msgSend$_isHearstRoutedWithNoPhoneCall
+ _objc_msgSend$_isInPhoneCallStateWithHeadset
+ _objc_msgSend$_subscribeToMonitors
+ _objc_msgSend$attSiriStateMonitor
+ _objc_msgSend$audiostreamActivityMonitor
+ _objc_msgSend$builtinSpeakerStateMonitor
+ _objc_msgSend$bypassPhraseSpotter
+ _objc_msgSend$commandControlStreamEventMonitor
+ _objc_msgSend$forceAPModeNonExclaveWatch
+ _objc_msgSend$isLowPowerModeEnabled
+ _objc_msgSend$isSiriClientConsideredAsRecord
+ _objc_msgSend$phraseSpotterEnabledMonitor
+ _objc_msgSend$playbackVolumeStatusMonitor
+ _objc_msgSend$setIsSiriClientConsideredAsRecord:
+ _objc_msgSend$siriAssertionMonitor
+ _objc_msgSend$siriClientBehaviorMonitor
+ _objc_msgSend$sleepModeMonitor
+ _objc_msgSend$wristState
+ _objc_msgSend$wristStateMonitor
- GCC_except_table1558
- GCC_except_table1582
- GCC_except_table1586
- GCC_except_table1602
- GCC_except_table1605
- GCC_except_table1635
- GCC_except_table1733
- GCC_except_table1735
- GCC_except_table1737
- GCC_except_table1743
- GCC_except_table1803
- GCC_except_table1829
- GCC_except_table1835
- GCC_except_table1916
- GCC_except_table1936
- GCC_except_table2052
- GCC_except_table2201
- GCC_except_table2231
- GCC_except_table2234
- GCC_except_table2237
- GCC_except_table2242
- GCC_except_table2254
- GCC_except_table2259
- GCC_except_table2262
- GCC_except_table2354
- GCC_except_table2360
- GCC_except_table2400
- GCC_except_table2403
- GCC_except_table2407
- GCC_except_table2425
- GCC_except_table2458
- GCC_except_table2561
- GCC_except_table2632
- GCC_except_table2663
- GCC_except_table2688
- GCC_except_table2699
- GCC_except_table2733
- GCC_except_table2734
- GCC_except_table2735
- GCC_except_table2736
- GCC_except_table2737
- GCC_except_table2741
- GCC_except_table2744
- GCC_except_table2748
- GCC_except_table2751
- GCC_except_table2752
- GCC_except_table2761
- GCC_except_table2767
- GCC_except_table2769
- GCC_except_table2770
- GCC_except_table2840
- GCC_except_table3106
- GCC_except_table3184
- GCC_except_table3221
- GCC_except_table3232
- GCC_except_table3254
- GCC_except_table3257
- GCC_except_table3260
- GCC_except_table3351
- GCC_except_table3583
- GCC_except_table3609
- GCC_except_table3637
- GCC_except_table3671
- GCC_except_table3672
- GCC_except_table3674
- GCC_except_table3676
- GCC_except_table3692
- GCC_except_table3694
- GCC_except_table3698
- GCC_except_table3700
- GCC_except_table3702
- GCC_except_table3704
- GCC_except_table3707
- GCC_except_table3715
- GCC_except_table3718
- GCC_except_table3724
- GCC_except_table3726
- GCC_except_table3728
- GCC_except_table3732
- GCC_except_table3734
- GCC_except_table3736
- GCC_except_table3737
- GCC_except_table3739
- GCC_except_table3740
- GCC_except_table3741
- GCC_except_table3744
- GCC_except_table3745
- GCC_except_table3746
- GCC_except_table3747
- GCC_except_table3748
- GCC_except_table3749
- GCC_except_table3750
- GCC_except_table3752
- GCC_except_table3767
- GCC_except_table3768
- GCC_except_table3769
- GCC_except_table3904
- GCC_except_table3928
- GCC_except_table3994
- GCC_except_table4010
- GCC_except_table4031
- GCC_except_table4123
- GCC_except_table4375
- GCC_except_table4442
- GCC_except_table4443
- GCC_except_table4447
- GCC_except_table4450
- GCC_except_table4454
- GCC_except_table4479
- GCC_except_table4532
- GCC_except_table4538
- GCC_except_table4608
- GCC_except_table4812
- GCC_except_table4819
- GCC_except_table4826
- GCC_except_table4832
- GCC_except_table4915
- GCC_except_table5075
- GCC_except_table5085
- GCC_except_table5109
- GCC_except_table5129
- GCC_except_table5212
- GCC_except_table5226
- GCC_except_table5235
- GCC_except_table5242
- GCC_except_table5248
- GCC_except_table5250
- GCC_except_table5253
- GCC_except_table5261
- GCC_except_table5263
- GCC_except_table5267
- GCC_except_table5269
- GCC_except_table5280
- GCC_except_table5286
- GCC_except_table5293
- GCC_except_table5298
- GCC_except_table5300
- GCC_except_table5302
- GCC_except_table5305
- GCC_except_table5306
- GCC_except_table5307
- GCC_except_table5309
- GCC_except_table5310
- GCC_except_table5312
- GCC_except_table5313
- GCC_except_table5315
- GCC_except_table5316
- GCC_except_table5334
- GCC_except_table5408
- GCC_except_table5412
- GCC_except_table5466
- GCC_except_table5496
- GCC_except_table5499
- GCC_except_table5589
- GCC_except_table5603
- GCC_except_table5610
- GCC_except_table5622
- GCC_except_table5626
- GCC_except_table5636
- GCC_except_table5865
- GCC_except_table5898
- GCC_except_table5903
- GCC_except_table5940
- GCC_except_table5949
- GCC_except_table5979
- GCC_except_table6047
- GCC_except_table6189
- GCC_except_table6292
- GCC_except_table6300
- GCC_except_table6320
- GCC_except_table6325
- GCC_except_table6431
- GCC_except_table6486
- GCC_except_table6566
- GCC_except_table6588
- GCC_except_table6589
- GCC_except_table6599
- GCC_except_table6600
- GCC_except_table6612
- GCC_except_table6643
- GCC_except_table6654
- GCC_except_table6659
- GCC_except_table6664
- GCC_except_table6692
- GCC_except_table6764
- GCC_except_table6776
- GCC_except_table6799
- GCC_except_table6810
- GCC_except_table6813
- GCC_except_table6836
- GCC_except_table6848
- GCC_except_table7120
- GCC_except_table7156
- GCC_except_table7229
- GCC_except_table7283
- GCC_except_table7306
- GCC_except_table7347
- GCC_except_table7358
- GCC_except_table7502
- GCC_except_table7510
- GCC_except_table7626
- GCC_except_table7627
- GCC_except_table7628
- GCC_except_table7629
- GCC_except_table7630
- GCC_except_table7635
- GCC_except_table7698
- GCC_except_table7744
- GCC_except_table7752
- GCC_except_table7758
- GCC_except_table7783
- GCC_except_table7789
- GCC_except_table7795
- GCC_except_table7933
CStrings:
+ "%s Built-in voice triggered, can stay in AOP mode"
+ "%s Disabling VoiceTrigger on AOP as since LowPowerMode is enabled"
+ "%s Disabling VoiceTrigger on AOP as since SleepMode is enabled"
+ "%s Disabling VoiceTrigger on AOP as the watch is off wrist"
+ "%s Display is off, remain in AOP mode so all triggers are gated"
+ "%s External phrase spotter running, ignore AOP trigger notification"
+ "%s ForceAPModeNonExclaveWatch=YES, forcing listening enabled (AP mode always on)"
+ "%s Phrase spotter is disabled, ignore Siri AP/AOP activation"
+ "%s RTS on watch cannot be turned on since there is another non eligible app recording and we are not in a connected or outgoing call"
+ "%s Received Hearst event %{public}ld"
+ "%s Turn on AP mode since LPM enabled with backlight ON"
+ "%s Turn on AP mode since Sleep Mode is enabled with backLight ON"
+ "%s Turn on AP mode since watch is off wrist and back light is on"
+ "%s VAD is not present (%d) or Hearst routed without phone call (%d)"
+ "%s VoiceTrigger on watch cannot be turned on since HS is disabled"
+ "%s VoiceTrigger on watch cannot be turned on since system shell is not started"
+ "%s VoiceTrigger on watch cannot be turned on since there is another non eligible app recording and we are not in a connected or outgoing call"
+ "%s phraseSpotter bypassed, ignore AOP/AP trigger notification"
+ "-[CSAlwaysOnProcessorEnabledWatchExclave _addConditons]_block_invoke"
+ "-[CSRaiseToSpeakEnabledPolicyWatchExclave _addListeningEnabledConditions]_block_invoke"
+ "-[CSVoiceTriggerAPModeSuspendPolicyWatch _addVoiceTriggerAPModeSuspendConditions]_block_invoke"
+ "-[CSVoiceTriggerAPModeSuspendPolicyWatch _addVoiceTriggerAPModeSuspendConditions]_block_invoke_2"
+ "-[CSVoiceTriggerAPModeSuspendPolicyWatch _handleClientRecordStateDidChange:eventUUID:]"
+ "-[CSVoiceTriggerAPModeSuspendPolicyWatch _handleClientRecordStateDidChange:eventUUID:]_block_invoke"
+ "-[CSVoiceTriggerAPModeSuspendPolicyWatch _isAudioRouteIneligibleForAP]"
+ "-[CSVoiceTriggerAPModeSuspendPolicyWatch _isSpeechDetectionDevicePresent]"
+ "-[CSVoiceTriggerActivationPolicyExclaveWatch CSAudioRouteChangeMonitor:didReceiveAudioRouteChangeEvent:]_block_invoke"
+ "-[CSVoiceTriggerActivationPolicyExclaveWatch _addConditons]_block_invoke"
+ "-[CSVoiceTriggerActivationPolicyExclaveWatch _isExternalPhraseSpotterRunning:]"
+ "-[CSVoiceTriggerEnabledPolicyWatchExclave _addListeningEnabledConditions]_block_invoke"
+ "CSVoiceTriggerAPModeSuspendPolicyWatch RecordState queue"
+ "com.apple.corespeech.CSAOPActivationEventHandlingPolicyWatch.queue"
+ "com.apple.corespeech.CSAlwaysOnProcessorEnabledExcalveWatch.queue"
```
