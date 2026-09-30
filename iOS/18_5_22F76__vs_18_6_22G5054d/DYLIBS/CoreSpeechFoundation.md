## CoreSpeechFoundation

> `/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/CoreSpeechFoundation`

```diff

-3405.29.3.11.1
-  __TEXT.__text: 0xb4f68
+3406.12.1.0.0
+  __TEXT.__text: 0xb649c
   __TEXT.__auth_stubs: 0x1d90
-  __TEXT.__objc_methlist: 0xba48
+  __TEXT.__objc_methlist: 0xbb60
   __TEXT.__const: 0x7e0
   __TEXT.__dlopen_cstrs: 0x174
   __TEXT.__constg_swiftt: 0x240
   __TEXT.__swift5_typeref: 0x185
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__cstring: 0x13d06
+  __TEXT.__cstring: 0x13f35
   __TEXT.__swift5_fieldmd: 0x128
   __TEXT.__swift5_reflstr: 0x84
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_proto: 0x8
-  __TEXT.__gcc_except_tab: 0x3214
-  __TEXT.__oslogstring: 0xdfe5
-  __TEXT.__unwind_info: 0x3028
+  __TEXT.__gcc_except_tab: 0x32bc
+  __TEXT.__oslogstring: 0xe211
+  __TEXT.__unwind_info: 0x3088
   __TEXT.__eh_frame: 0xe8
-  __TEXT.__objc_classname: 0x1a26
-  __TEXT.__objc_methname: 0x1f9ad
-  __TEXT.__objc_methtype: 0x43b7
-  __TEXT.__objc_stubs: 0x105c0
+  __TEXT.__objc_classname: 0x1a65
+  __TEXT.__objc_methname: 0x1fb21
+  __TEXT.__objc_methtype: 0x4422
+  __TEXT.__objc_stubs: 0x10680
   __DATA_CONST.__got: 0xf20
-  __DATA_CONST.__const: 0x2470
+  __DATA_CONST.__const: 0x24a8
   __DATA_CONST.__objc_classlist: 0x678
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x190
+  __DATA_CONST.__objc_protolist: 0x1a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x67f0
+  __DATA_CONST.__objc_selrefs: 0x6830
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x4e0
   __DATA_CONST.__objc_arraydata: 0x198
   __AUTH_CONST.__auth_got: 0xee0
-  __AUTH_CONST.__const: 0x1570
-  __AUTH_CONST.__cfstring: 0x8a00
-  __AUTH_CONST.__objc_const: 0x12140
+  __AUTH_CONST.__const: 0x15b0
+  __AUTH_CONST.__cfstring: 0x8a20
+  __AUTH_CONST.__objc_const: 0x122a0
   __AUTH_CONST.__objc_dictobj: 0x1e0
   __AUTH_CONST.__objc_intobj: 0x318
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_floatobj: 0x1b0
   __AUTH.__objc_data: 0x500
-  __DATA.__objc_ivar: 0xc00
-  __DATA.__data: 0x12e0
-  __DATA.__bss: 0x8f8
+  __DATA.__objc_ivar: 0xc0c
+  __DATA.__data: 0x13a0
+  __DATA.__bss: 0x910
   __DATA_DIRTY.__objc_data: 0x3c68
   __DATA_DIRTY.__data: 0x2c8
   __DATA_DIRTY.__bss: 0x360

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 673FF75E-0249-3D25-AE7E-8F20630D7B0B
-  Functions: 4482
-  Symbols:   15294
-  CStrings:  9703
+  UUID: 0EEBACA3-4FB7-3F41-8BA1-057C26C5C4C3
+  Functions: 4505
+  Symbols:   15369
+  CStrings:  9746
 
Symbols:
+ +[CSSecureSessionHandler sharedHandler]
+ +[CSSecureSessionHandler siriEnablementSessionAssertionUUID]
+ -[CSAudioProvider secureSessionAssertionUUID]
+ -[CSAudioProvider setSecureSessionAssertionUUID:]
+ -[CSAudioRecorder CSSystemDaemonDisconnected]
+ -[CSLaunchAgentXPCClient activateSecureSession:error:]
+ -[CSLaunchAgentXPCClient duckAudioDeviceWithDeviceID:duckedLevel:rampDuration:]
+ -[CSLaunchAgentXPCClient resetAVVC]
+ -[CSLaunchAgentXPCClient setAlertSoundFromURL:forType:]
+ -[CSSecureSessionHandler .cxx_destruct]
+ -[CSSecureSessionHandler CSAudioServerCrashMonitorDidReceiveServerCrash:]
+ -[CSSecureSessionHandler CSAudioServerCrashMonitorDidReceiveServerRestart:]
+ -[CSSecureSessionHandler CSSiriEnabledMonitor:didReceiveEnabled:]
+ -[CSSecureSessionHandler CSSystemDaemonStateMonitorDidReceiveSysDaemonCrash:]
+ -[CSSecureSessionHandler CSSystemDaemonStateMonitorDidReceiveSysDaemonRestartFromCrash:]
+ -[CSSecureSessionHandler _activateSecureSessionIfNeeded]
+ -[CSSecureSessionHandler _deactivateSecureSessionIfNeeded]
+ -[CSSecureSessionHandler acquireSecureSessionAssertionWithUUID:]
+ -[CSSecureSessionHandler assertionSet]
+ -[CSSecureSessionHandler init]
+ -[CSSecureSessionHandler queue]
+ -[CSSecureSessionHandler releaseAllSecureSessionAssertions]
+ -[CSSecureSessionHandler releaseSecureSessionAssertionWithUUID:]
+ -[CSSecureSessionHandler setAssertionSet:]
+ -[CSSecureSessionHandler setQueue:]
+ -[CSSecureSessionHandler start]
+ -[CSSystemDaemonStateMonitor currentSystemDaemonState]
+ GCC_except_table1213
+ GCC_except_table1242
+ GCC_except_table1331
+ GCC_except_table1333
+ GCC_except_table1334
+ GCC_except_table1336
+ GCC_except_table1337
+ GCC_except_table1338
+ GCC_except_table1352
+ GCC_except_table1745
+ GCC_except_table1746
+ GCC_except_table1747
+ GCC_except_table1748
+ GCC_except_table1749
+ GCC_except_table1760
+ GCC_except_table1766
+ GCC_except_table1773
+ GCC_except_table1775
+ GCC_except_table1776
+ GCC_except_table1789
+ GCC_except_table1794
+ GCC_except_table1879
+ GCC_except_table1884
+ GCC_except_table1956
+ GCC_except_table1965
+ GCC_except_table1997
+ GCC_except_table1998
+ GCC_except_table2000
+ GCC_except_table2001
+ GCC_except_table2007
+ GCC_except_table2016
+ GCC_except_table2023
+ GCC_except_table2066
+ GCC_except_table2137
+ GCC_except_table2247
+ GCC_except_table2282
+ GCC_except_table2420
+ GCC_except_table2495
+ GCC_except_table2506
+ GCC_except_table2508
+ GCC_except_table2513
+ GCC_except_table2515
+ GCC_except_table2528
+ GCC_except_table2535
+ GCC_except_table2537
+ GCC_except_table2555
+ GCC_except_table2576
+ GCC_except_table258
+ GCC_except_table2614
+ GCC_except_table2670
+ GCC_except_table2672
+ GCC_except_table2673
+ GCC_except_table2814
+ GCC_except_table282
+ GCC_except_table2943
+ GCC_except_table2951
+ GCC_except_table2959
+ GCC_except_table2966
+ GCC_except_table2972
+ GCC_except_table2973
+ GCC_except_table2996
+ GCC_except_table301
+ GCC_except_table302
+ GCC_except_table303
+ GCC_except_table304
+ GCC_except_table305
+ GCC_except_table3052
+ GCC_except_table310
+ GCC_except_table3111
+ GCC_except_table3134
+ GCC_except_table3165
+ GCC_except_table3166
+ GCC_except_table3167
+ GCC_except_table3168
+ GCC_except_table3191
+ GCC_except_table3204
+ GCC_except_table3361
+ GCC_except_table3421
+ GCC_except_table3435
+ GCC_except_table3477
+ GCC_except_table3478
+ GCC_except_table3506
+ GCC_except_table3507
+ GCC_except_table3509
+ GCC_except_table3512
+ GCC_except_table3513
+ GCC_except_table3514
+ GCC_except_table3537
+ GCC_except_table3540
+ GCC_except_table3544
+ GCC_except_table3545
+ GCC_except_table3546
+ GCC_except_table3548
+ GCC_except_table3582
+ GCC_except_table3584
+ GCC_except_table3585
+ GCC_except_table3586
+ GCC_except_table3587
+ GCC_except_table3644
+ GCC_except_table365
+ GCC_except_table369
+ GCC_except_table3692
+ GCC_except_table3696
+ GCC_except_table370
+ GCC_except_table371
+ GCC_except_table372
+ GCC_except_table373
+ GCC_except_table3746
+ GCC_except_table3747
+ GCC_except_table3754
+ GCC_except_table3755
+ GCC_except_table3756
+ GCC_except_table3757
+ GCC_except_table3759
+ GCC_except_table3760
+ GCC_except_table3781
+ GCC_except_table3782
+ GCC_except_table3783
+ GCC_except_table3785
+ GCC_except_table3786
+ GCC_except_table3787
+ GCC_except_table3788
+ GCC_except_table3789
+ GCC_except_table3790
+ GCC_except_table3791
+ GCC_except_table3817
+ GCC_except_table3818
+ GCC_except_table3819
+ GCC_except_table3820
+ GCC_except_table3821
+ GCC_except_table3824
+ GCC_except_table3825
+ GCC_except_table3826
+ GCC_except_table3827
+ GCC_except_table3828
+ GCC_except_table3831
+ GCC_except_table3834
+ GCC_except_table3838
+ GCC_except_table3859
+ GCC_except_table3860
+ GCC_except_table3862
+ GCC_except_table3863
+ GCC_except_table3865
+ GCC_except_table3867
+ GCC_except_table3868
+ GCC_except_table3869
+ GCC_except_table3874
+ GCC_except_table3876
+ GCC_except_table3880
+ GCC_except_table3881
+ GCC_except_table3911
+ GCC_except_table3915
+ GCC_except_table4015
+ GCC_except_table4022
+ GCC_except_table4064
+ GCC_except_table4128
+ GCC_except_table4144
+ GCC_except_table4149
+ GCC_except_table4210
+ GCC_except_table4222
+ GCC_except_table4227
+ GCC_except_table4262
+ GCC_except_table4328
+ GCC_except_table457
+ GCC_except_table486
+ GCC_except_table489
+ GCC_except_table494
+ GCC_except_table574
+ GCC_except_table577
+ GCC_except_table580
+ GCC_except_table581
+ GCC_except_table740
+ GCC_except_table747
+ GCC_except_table818
+ GCC_except_table819
+ GCC_except_table841
+ GCC_except_table842
+ GCC_except_table843
+ GCC_except_table847
+ GCC_except_table848
+ GCC_except_table853
+ GCC_except_table854
+ GCC_except_table860
+ GCC_except_table864
+ GCC_except_table873
+ _AudioConverterFillComplexBuffer_BlockInvoke.7127
+ _OBJC_CLASS_$_CSSecureSessionHandler
+ _OBJC_IVAR_$_CSAudioProvider._secureSessionAssertionUUID
+ _OBJC_IVAR_$_CSSecureSessionHandler._assertionSet
+ _OBJC_IVAR_$_CSSecureSessionHandler._queue
+ _OBJC_METACLASS_$_CSSecureSessionHandler
+ __OBJC_$_CLASS_METHODS_CSSecureSessionHandler
+ __OBJC_$_INSTANCE_METHODS_CSSecureSessionHandler
+ __OBJC_$_INSTANCE_VARIABLES_CSSecureSessionHandler
+ __OBJC_$_PROP_LIST_CSSecureSessionHandler
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriEnabledMonitorDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSystemDaemonStateMonitorDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriEnabledMonitorDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSystemDaemonStateMonitorDelegate
+ __OBJC_$_PROTOCOL_REFS_CSSiriEnabledMonitorDelegate
+ __OBJC_$_PROTOCOL_REFS_CSSystemDaemonStateMonitorDelegate
+ __OBJC_CLASS_PROTOCOLS_$_CSSecureSessionHandler
+ __OBJC_CLASS_RO_$_CSSecureSessionHandler
+ __OBJC_LABEL_PROTOCOL_$_CSSiriEnabledMonitorDelegate
+ __OBJC_LABEL_PROTOCOL_$_CSSystemDaemonStateMonitorDelegate
+ __OBJC_METACLASS_RO_$_CSSecureSessionHandler
+ __OBJC_PROTOCOL_$_CSSiriEnabledMonitorDelegate
+ __OBJC_PROTOCOL_$_CSSystemDaemonStateMonitorDelegate
+ ___37-[CSLaunchAgentXPCClient _disconnect]_block_invoke.18
+ ___39+[CSSecureSessionHandler sharedHandler]_block_invoke
+ ___39-[CSAudioRecorder initWithQueue:error:]_block_invoke
+ ___45-[CSAudioRecorder CSSystemDaemonDisconnected]_block_invoke
+ ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.108
+ ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.114
+ ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.119
+ ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.122
+ ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_2.115
+ ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_2.120
+ ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_3.121
+ ___54-[CSSystemDaemonStateMonitor currentSystemDaemonState]_block_invoke
+ ___55-[CSAudioProvider _handleDidStopAudioStreamWithReason:]_block_invoke.107
+ ___55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.102
+ ___55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.99
+ ___55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke_2.100
+ ___57-[CSAudioProvider _didReceiveFinishStartAlertPlaybackAt:]_block_invoke.144
+ ___59-[CSSecureSessionHandler releaseAllSecureSessionAssertions]_block_invoke
+ ___60+[CSSecureSessionHandler siriEnablementSessionAssertionUUID]_block_invoke
+ ___64-[CSSecureSessionHandler acquireSecureSessionAssertionWithUUID:]_block_invoke
+ ___64-[CSSecureSessionHandler releaseSecureSessionAssertionWithUUID:]_block_invoke
+ ___78-[CSAudioProvider playRecordStartingAlertAndResetEndpointerWithAlertOverride:]_block_invoke.134
+ ___Block_byref_object_copy_.11794
+ ___Block_byref_object_copy_.12196
+ ___Block_byref_object_copy_.12483
+ ___Block_byref_object_copy_.12730
+ ___Block_byref_object_copy_.13224
+ ___Block_byref_object_copy_.13758
+ ___Block_byref_object_copy_.13840
+ ___Block_byref_object_copy_.14598
+ ___Block_byref_object_copy_.1491
+ ___Block_byref_object_copy_.2021
+ ___Block_byref_object_copy_.2430
+ ___Block_byref_object_copy_.3156
+ ___Block_byref_object_copy_.4440
+ ___Block_byref_object_copy_.4659
+ ___Block_byref_object_copy_.5489
+ ___Block_byref_object_copy_.5554
+ ___Block_byref_object_copy_.6002
+ ___Block_byref_object_copy_.7715
+ ___Block_byref_object_copy_.7983
+ ___Block_byref_object_copy_.8337
+ ___Block_byref_object_copy_.9096
+ ___Block_byref_object_dispose_.11795
+ ___Block_byref_object_dispose_.12197
+ ___Block_byref_object_dispose_.12484
+ ___Block_byref_object_dispose_.12731
+ ___Block_byref_object_dispose_.13225
+ ___Block_byref_object_dispose_.13759
+ ___Block_byref_object_dispose_.13841
+ ___Block_byref_object_dispose_.14599
+ ___Block_byref_object_dispose_.1492
+ ___Block_byref_object_dispose_.2022
+ ___Block_byref_object_dispose_.2431
+ ___Block_byref_object_dispose_.3157
+ ___Block_byref_object_dispose_.4441
+ ___Block_byref_object_dispose_.4660
+ ___Block_byref_object_dispose_.5490
+ ___Block_byref_object_dispose_.5555
+ ___Block_byref_object_dispose_.6003
+ ___Block_byref_object_dispose_.7716
+ ___Block_byref_object_dispose_.7984
+ ___Block_byref_object_dispose_.8338
+ ___Block_byref_object_dispose_.9097
+ ___block_literal_global.10055
+ ___block_literal_global.1089
+ ___block_literal_global.10906
+ ___block_literal_global.11019
+ ___block_literal_global.11144
+ ___block_literal_global.11260
+ ___block_literal_global.11297
+ ___block_literal_global.11840
+ ___block_literal_global.12304
+ ___block_literal_global.12583
+ ___block_literal_global.12828
+ ___block_literal_global.13134
+ ___block_literal_global.1340
+ ___block_literal_global.13487
+ ___block_literal_global.13589
+ ___block_literal_global.13645
+ ___block_literal_global.1373
+ ___block_literal_global.13782
+ ___block_literal_global.13986
+ ___block_literal_global.1399
+ ___block_literal_global.14080
+ ___block_literal_global.14154
+ ___block_literal_global.1443
+ ___block_literal_global.14430
+ ___block_literal_global.14622
+ ___block_literal_global.1528
+ ___block_literal_global.166.8079
+ ___block_literal_global.177.8073
+ ___block_literal_global.20.12292
+ ___block_literal_global.2038
+ ___block_literal_global.2130
+ ___block_literal_global.2176
+ ___block_literal_global.2215
+ ___block_literal_global.2446
+ ___block_literal_global.253.8025
+ ___block_literal_global.2553
+ ___block_literal_global.26
+ ___block_literal_global.2602
+ ___block_literal_global.27.8191
+ ___block_literal_global.2895
+ ___block_literal_global.3070
+ ___block_literal_global.3176
+ ___block_literal_global.3470
+ ___block_literal_global.3623
+ ___block_literal_global.3886
+ ___block_literal_global.41.8178
+ ___block_literal_global.4467
+ ___block_literal_global.453
+ ___block_literal_global.4627
+ ___block_literal_global.4675
+ ___block_literal_global.5257
+ ___block_literal_global.5341
+ ___block_literal_global.5566
+ ___block_literal_global.6224
+ ___block_literal_global.6369
+ ___block_literal_global.6437
+ ___block_literal_global.6623
+ ___block_literal_global.6639
+ ___block_literal_global.6833
+ ___block_literal_global.6896
+ ___block_literal_global.6956
+ ___block_literal_global.7056
+ ___block_literal_global.7092
+ ___block_literal_global.716
+ ___block_literal_global.7376
+ ___block_literal_global.8204
+ ___block_literal_global.8220
+ ___block_literal_global.848
+ ___block_literal_global.8621
+ ___block_literal_global.8682
+ ___block_literal_global.8831
+ ___block_literal_global.8888
+ ___block_literal_global.91
+ ___block_literal_global.9123
+ ___block_literal_global.9422
+ ___block_literal_global.9552
+ ___block_literal_global.959
+ ___block_literal_global.9658
+ ___block_literal_global.9958
+ __processAudioBuffer:audioStreamHandleId:arrivalTimestampToAudioRecorder:.heartbeat.138
+ _objc_msgSend$CSSystemDaemonDisconnected
+ _objc_msgSend$_activateSecureSessionIfNeeded
+ _objc_msgSend$_deactivateSecureSessionIfNeeded
+ _objc_msgSend$acquireSecureSessionAssertionWithUUID:
+ _objc_msgSend$activateSecureSession:error:
+ _objc_msgSend$isEnabled
+ _objc_msgSend$releaseAllSecureSessionAssertions
+ _objc_msgSend$releaseSecureSessionAssertionWithUUID:
+ _objc_msgSend$resetAVVC
+ _objc_msgSend$siriEnablementSessionAssertionUUID
+ _sharedHandler.onceToken.11839
+ _sharedHandler.sharedHandler.11841
+ _sharedInstance._sharedInstance.10056
+ _sharedInstance._sharedInstance.10907
+ _sharedInstance._sharedInstance.11298
+ _sharedInstance._sharedInstance.13590
+ _sharedInstance._sharedInstance.13646
+ _sharedInstance._sharedInstance.14081
+ _sharedInstance._sharedInstance.14155
+ _sharedInstance._sharedInstance.3887
+ _sharedInstance._sharedInstance.4628
+ _sharedInstance._sharedInstance.5258
+ _sharedInstance._sharedInstance.6225
+ _sharedInstance._sharedInstance.6834
+ _sharedInstance._sharedInstance.7057
+ _sharedInstance._sharedInstance.7377
+ _sharedInstance._sharedInstance.849
+ _sharedInstance._sharedInstance.960
+ _sharedInstance.onceToken.10054
+ _sharedInstance.onceToken.10905
+ _sharedInstance.onceToken.11018
+ _sharedInstance.onceToken.11296
+ _sharedInstance.onceToken.12582
+ _sharedInstance.onceToken.13588
+ _sharedInstance.onceToken.13644
+ _sharedInstance.onceToken.1372
+ _sharedInstance.onceToken.13985
+ _sharedInstance.onceToken.14079
+ _sharedInstance.onceToken.14153
+ _sharedInstance.onceToken.1442
+ _sharedInstance.onceToken.14429
+ _sharedInstance.onceToken.14621
+ _sharedInstance.onceToken.1527
+ _sharedInstance.onceToken.2129
+ _sharedInstance.onceToken.2175
+ _sharedInstance.onceToken.2214
+ _sharedInstance.onceToken.2445
+ _sharedInstance.onceToken.3175
+ _sharedInstance.onceToken.3622
+ _sharedInstance.onceToken.3885
+ _sharedInstance.onceToken.4466
+ _sharedInstance.onceToken.452
+ _sharedInstance.onceToken.4626
+ _sharedInstance.onceToken.4674
+ _sharedInstance.onceToken.5256
+ _sharedInstance.onceToken.6223
+ _sharedInstance.onceToken.6368
+ _sharedInstance.onceToken.6622
+ _sharedInstance.onceToken.6832
+ _sharedInstance.onceToken.7055
+ _sharedInstance.onceToken.7375
+ _sharedInstance.onceToken.8219
+ _sharedInstance.onceToken.847
+ _sharedInstance.onceToken.8681
+ _sharedInstance.onceToken.8887
+ _sharedInstance.onceToken.9421
+ _sharedInstance.onceToken.9551
+ _sharedInstance.onceToken.958
+ _sharedInstance.onceToken.9657
+ _sharedInstance.sharedInstance.11020
+ _sharedInstance.sharedInstance.12584
+ _sharedInstance.sharedInstance.13987
+ _sharedInstance.sharedInstance.14431
+ _sharedInstance.sharedInstance.14623
+ _sharedInstance.sharedInstance.2131
+ _sharedInstance.sharedInstance.2216
+ _sharedInstance.sharedInstance.2447
+ _sharedInstance.sharedInstance.3177
+ _sharedInstance.sharedInstance.3624
+ _sharedInstance.sharedInstance.454
+ _sharedInstance.sharedInstance.4676
+ _sharedInstance.sharedInstance.6370
+ _sharedInstance.sharedInstance.8683
+ _sharedInstance.sharedInstance.8889
+ _sharedInstance.sharedInstance.9553
+ _sharedInstance.sharedInstance.9659
+ _sharedInstance.sharedManager.6624
+ _sharedInstance.sharedManager.8221
+ _sharedLogger.onceToken.13133
+ _sharedLogger.onceToken.2552
+ _sharedLogger.onceToken.6436
+ _sharedLogger.onceToken.6638
+ _sharedLogger.shared.13135
+ _sharedManager.onceToken.13781
+ _sharedMonitor.onceToken.5340
+ _sharedMonitor.sharedMonitor.5342
+ _sharedPreferences.onceToken.8620
+ _siriEnablementSessionAssertionUUID.onceToken
+ _siriEnablementSessionAssertionUUID.siriEnablementSessionAssertionUUID
- +[CSMacUserSessionMonitor sharedInstance]
- -[CSLaunchAgentXPCClient activateSecureSession:]
- -[CSMacUserSessionMonitor _handleSessionActive:]
- -[CSMacUserSessionMonitor _handleSessionResign:]
- -[CSMacUserSessionMonitor _notifySessionActive:]
- -[CSMacUserSessionMonitor _registerUserSessionNotification]
- -[CSMacUserSessionMonitor _startMonitoringWithQueue:]
- -[CSMacUserSessionMonitor _stopMonitoring]
- -[CSMacUserSessionMonitor _unregisterUserSessionNotification]
- -[CSMacUserSessionMonitor init]
- GCC_except_table1221
- GCC_except_table1250
- GCC_except_table1339
- GCC_except_table1342
- GCC_except_table1344
- GCC_except_table1345
- GCC_except_table1346
- GCC_except_table1349
- GCC_except_table1360
- GCC_except_table1754
- GCC_except_table1755
- GCC_except_table1761
- GCC_except_table1764
- GCC_except_table1765
- GCC_except_table1768
- GCC_except_table1774
- GCC_except_table1781
- GCC_except_table1783
- GCC_except_table1784
- GCC_except_table1797
- GCC_except_table1802
- GCC_except_table1887
- GCC_except_table1892
- GCC_except_table1964
- GCC_except_table1973
- GCC_except_table2005
- GCC_except_table2006
- GCC_except_table2008
- GCC_except_table2009
- GCC_except_table2015
- GCC_except_table2024
- GCC_except_table2031
- GCC_except_table2074
- GCC_except_table2143
- GCC_except_table2253
- GCC_except_table2288
- GCC_except_table2428
- GCC_except_table2499
- GCC_except_table2510
- GCC_except_table2512
- GCC_except_table2517
- GCC_except_table2519
- GCC_except_table2532
- GCC_except_table2539
- GCC_except_table2541
- GCC_except_table2559
- GCC_except_table2580
- GCC_except_table2618
- GCC_except_table2674
- GCC_except_table2676
- GCC_except_table2677
- GCC_except_table269
- GCC_except_table2818
- GCC_except_table293
- GCC_except_table2947
- GCC_except_table2955
- GCC_except_table2963
- GCC_except_table2974
- GCC_except_table2976
- GCC_except_table2977
- GCC_except_table3000
- GCC_except_table3060
- GCC_except_table3115
- GCC_except_table312
- GCC_except_table3138
- GCC_except_table314
- GCC_except_table315
- GCC_except_table316
- GCC_except_table3169
- GCC_except_table3170
- GCC_except_table3171
- GCC_except_table3172
- GCC_except_table3195
- GCC_except_table3208
- GCC_except_table321
- GCC_except_table324
- GCC_except_table3341
- GCC_except_table3401
- GCC_except_table3415
- GCC_except_table3457
- GCC_except_table3458
- GCC_except_table3486
- GCC_except_table3487
- GCC_except_table3489
- GCC_except_table3492
- GCC_except_table3493
- GCC_except_table3494
- GCC_except_table3517
- GCC_except_table3520
- GCC_except_table3524
- GCC_except_table3525
- GCC_except_table3526
- GCC_except_table3528
- GCC_except_table3562
- GCC_except_table3564
- GCC_except_table3565
- GCC_except_table3566
- GCC_except_table3567
- GCC_except_table3624
- GCC_except_table3672
- GCC_except_table3676
- GCC_except_table3726
- GCC_except_table3727
- GCC_except_table3734
- GCC_except_table3735
- GCC_except_table3736
- GCC_except_table3737
- GCC_except_table3739
- GCC_except_table3740
- GCC_except_table376
- GCC_except_table3761
- GCC_except_table3763
- GCC_except_table3764
- GCC_except_table3765
- GCC_except_table3766
- GCC_except_table3767
- GCC_except_table3768
- GCC_except_table3769
- GCC_except_table3780
- GCC_except_table3793
- GCC_except_table3794
- GCC_except_table3795
- GCC_except_table3796
- GCC_except_table3797
- GCC_except_table3798
- GCC_except_table380
- GCC_except_table3800
- GCC_except_table3801
- GCC_except_table3802
- GCC_except_table3804
- GCC_except_table3805
- GCC_except_table3808
- GCC_except_table381
- GCC_except_table3811
- GCC_except_table382
- GCC_except_table383
- GCC_except_table3836
- GCC_except_table3837
- GCC_except_table384
- GCC_except_table3840
- GCC_except_table3842
- GCC_except_table3844
- GCC_except_table3845
- GCC_except_table3851
- GCC_except_table3853
- GCC_except_table3857
- GCC_except_table3858
- GCC_except_table3888
- GCC_except_table3892
- GCC_except_table3992
- GCC_except_table3999
- GCC_except_table4041
- GCC_except_table4105
- GCC_except_table4121
- GCC_except_table4126
- GCC_except_table4187
- GCC_except_table4199
- GCC_except_table4204
- GCC_except_table4239
- GCC_except_table4305
- GCC_except_table468
- GCC_except_table497
- GCC_except_table500
- GCC_except_table505
- GCC_except_table585
- GCC_except_table588
- GCC_except_table591
- GCC_except_table592
- GCC_except_table749
- GCC_except_table756
- GCC_except_table827
- GCC_except_table834
- GCC_except_table856
- GCC_except_table857
- GCC_except_table861
- GCC_except_table866
- GCC_except_table867
- GCC_except_table868
- GCC_except_table870
- GCC_except_table871
- GCC_except_table872
- GCC_except_table881
- _AudioConverterFillComplexBuffer_BlockInvoke.7199
- _OBJC_CLASS_$_CSMacUserSessionMonitor
- _OBJC_METACLASS_$_CSMacUserSessionMonitor
- __OBJC_$_CLASS_METHODS_CSMacUserSessionMonitor
- __OBJC_$_INSTANCE_METHODS_CSMacUserSessionMonitor
- __OBJC_CLASS_RO_$_CSMacUserSessionMonitor
- __OBJC_METACLASS_RO_$_CSMacUserSessionMonitor
- ___37-[CSLaunchAgentXPCClient _disconnect]_block_invoke.19
- ___41+[CSMacUserSessionMonitor sharedInstance]_block_invoke
- ___48-[CSMacUserSessionMonitor _notifySessionActive:]_block_invoke
- ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.107
- ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.113
- ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.118
- ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.121
- ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_2.114
- ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_2.119
- ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_3.120
- ___55-[CSAudioProvider _handleDidStopAudioStreamWithReason:]_block_invoke.105
- ___55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.101
- ___55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.93
- ___55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke_2.99
- ___57-[CSAudioProvider _didReceiveFinishStartAlertPlaybackAt:]_block_invoke.143
- ___78-[CSAudioProvider playRecordStartingAlertAndResetEndpointerWithAlertOverride:]_block_invoke.133
- ___Block_byref_object_copy_.11747
- ___Block_byref_object_copy_.12139
- ___Block_byref_object_copy_.12417
- ___Block_byref_object_copy_.12665
- ___Block_byref_object_copy_.13157
- ___Block_byref_object_copy_.13692
- ___Block_byref_object_copy_.13774
- ___Block_byref_object_copy_.14534
- ___Block_byref_object_copy_.1525
- ___Block_byref_object_copy_.2066
- ___Block_byref_object_copy_.2484
- ___Block_byref_object_copy_.3213
- ___Block_byref_object_copy_.4512
- ___Block_byref_object_copy_.4731
- ___Block_byref_object_copy_.5561
- ___Block_byref_object_copy_.5626
- ___Block_byref_object_copy_.6074
- ___Block_byref_object_copy_.7790
- ___Block_byref_object_copy_.8066
- ___Block_byref_object_copy_.8426
- ___Block_byref_object_copy_.9184
- ___Block_byref_object_dispose_.11748
- ___Block_byref_object_dispose_.12140
- ___Block_byref_object_dispose_.12418
- ___Block_byref_object_dispose_.12666
- ___Block_byref_object_dispose_.13158
- ___Block_byref_object_dispose_.13693
- ___Block_byref_object_dispose_.13775
- ___Block_byref_object_dispose_.14535
- ___Block_byref_object_dispose_.1526
- ___Block_byref_object_dispose_.2067
- ___Block_byref_object_dispose_.2485
- ___Block_byref_object_dispose_.3214
- ___Block_byref_object_dispose_.4513
- ___Block_byref_object_dispose_.4732
- ___Block_byref_object_dispose_.5562
- ___Block_byref_object_dispose_.5627
- ___Block_byref_object_dispose_.6075
- ___Block_byref_object_dispose_.7791
- ___Block_byref_object_dispose_.8067
- ___Block_byref_object_dispose_.8427
- ___Block_byref_object_dispose_.9185
- ___block_literal_global.10012
- ___block_literal_global.10862
- ___block_literal_global.10975
- ___block_literal_global.11100
- ___block_literal_global.11215
- ___block_literal_global.1123
- ___block_literal_global.11252
- ___block_literal_global.11792
- ___block_literal_global.12234
- ___block_literal_global.12518
- ___block_literal_global.12761
- ___block_literal_global.13067
- ___block_literal_global.13421
- ___block_literal_global.13523
- ___block_literal_global.13579
- ___block_literal_global.13716
- ___block_literal_global.1374
- ___block_literal_global.13920
- ___block_literal_global.14014
- ___block_literal_global.1407
- ___block_literal_global.14088
- ___block_literal_global.1433
- ___block_literal_global.14366
- ___block_literal_global.14558
- ___block_literal_global.1477
- ___block_literal_global.1562
- ___block_literal_global.166.8164
- ___block_literal_global.177.8158
- ___block_literal_global.2045
- ___block_literal_global.21
- ___block_literal_global.2173
- ___block_literal_global.2219
- ___block_literal_global.2258
- ___block_literal_global.2500
- ___block_literal_global.253.8109
- ___block_literal_global.2605
- ___block_literal_global.2654
- ___block_literal_global.27.8280
- ___block_literal_global.2952
- ___block_literal_global.3127
- ___block_literal_global.3233
- ___block_literal_global.3529
- ___block_literal_global.3682
- ___block_literal_global.3939
- ___block_literal_global.41.8267
- ___block_literal_global.425
- ___block_literal_global.4539
- ___block_literal_global.4699
- ___block_literal_global.4747
- ___block_literal_global.485
- ___block_literal_global.5329
- ___block_literal_global.5413
- ___block_literal_global.5638
- ___block_literal_global.6296
- ___block_literal_global.6441
- ___block_literal_global.6509
- ___block_literal_global.6695
- ___block_literal_global.6711
- ___block_literal_global.6905
- ___block_literal_global.6968
- ___block_literal_global.7028
- ___block_literal_global.7128
- ___block_literal_global.7164
- ___block_literal_global.7448
- ___block_literal_global.751
- ___block_literal_global.8293
- ___block_literal_global.8309
- ___block_literal_global.8710
- ___block_literal_global.8771
- ___block_literal_global.883
- ___block_literal_global.8919
- ___block_literal_global.8976
- ___block_literal_global.9211
- ___block_literal_global.9510
- ___block_literal_global.9640
- ___block_literal_global.9746
- ___block_literal_global.993
- __processAudioBuffer:audioStreamHandleId:arrivalTimestampToAudioRecorder:.heartbeat.134
- _objc_msgSend$_notifySessionActive:
- _objc_msgSend$_registerUserSessionNotification
- _objc_msgSend$_unregisterUserSessionNotification
- _objc_msgSend$macUserSessionMonitor:sessionActive:
- _sharedInstance._sharedInstance.10013
- _sharedInstance._sharedInstance.10863
- _sharedInstance._sharedInstance.11253
- _sharedInstance._sharedInstance.13524
- _sharedInstance._sharedInstance.13580
- _sharedInstance._sharedInstance.14015
- _sharedInstance._sharedInstance.14089
- _sharedInstance._sharedInstance.3940
- _sharedInstance._sharedInstance.4700
- _sharedInstance._sharedInstance.5330
- _sharedInstance._sharedInstance.6297
- _sharedInstance._sharedInstance.6906
- _sharedInstance._sharedInstance.7129
- _sharedInstance._sharedInstance.7449
- _sharedInstance._sharedInstance.884
- _sharedInstance._sharedInstance.994
- _sharedInstance.onceToken.10011
- _sharedInstance.onceToken.10861
- _sharedInstance.onceToken.10974
- _sharedInstance.onceToken.11251
- _sharedInstance.onceToken.12517
- _sharedInstance.onceToken.13522
- _sharedInstance.onceToken.13578
- _sharedInstance.onceToken.13919
- _sharedInstance.onceToken.14013
- _sharedInstance.onceToken.1406
- _sharedInstance.onceToken.14087
- _sharedInstance.onceToken.14365
- _sharedInstance.onceToken.14557
- _sharedInstance.onceToken.1476
- _sharedInstance.onceToken.1561
- _sharedInstance.onceToken.2172
- _sharedInstance.onceToken.2218
- _sharedInstance.onceToken.2257
- _sharedInstance.onceToken.2499
- _sharedInstance.onceToken.3232
- _sharedInstance.onceToken.3681
- _sharedInstance.onceToken.3938
- _sharedInstance.onceToken.424
- _sharedInstance.onceToken.4538
- _sharedInstance.onceToken.4698
- _sharedInstance.onceToken.4746
- _sharedInstance.onceToken.484
- _sharedInstance.onceToken.5328
- _sharedInstance.onceToken.6295
- _sharedInstance.onceToken.6440
- _sharedInstance.onceToken.6694
- _sharedInstance.onceToken.6904
- _sharedInstance.onceToken.7127
- _sharedInstance.onceToken.7447
- _sharedInstance.onceToken.8308
- _sharedInstance.onceToken.8770
- _sharedInstance.onceToken.882
- _sharedInstance.onceToken.8975
- _sharedInstance.onceToken.9509
- _sharedInstance.onceToken.9639
- _sharedInstance.onceToken.9745
- _sharedInstance.onceToken.992
- _sharedInstance.sharedInstance.10976
- _sharedInstance.sharedInstance.12519
- _sharedInstance.sharedInstance.13921
- _sharedInstance.sharedInstance.14367
- _sharedInstance.sharedInstance.14559
- _sharedInstance.sharedInstance.2174
- _sharedInstance.sharedInstance.2259
- _sharedInstance.sharedInstance.2501
- _sharedInstance.sharedInstance.3234
- _sharedInstance.sharedInstance.3683
- _sharedInstance.sharedInstance.426
- _sharedInstance.sharedInstance.4748
- _sharedInstance.sharedInstance.486
- _sharedInstance.sharedInstance.6442
- _sharedInstance.sharedInstance.8772
- _sharedInstance.sharedInstance.8977
- _sharedInstance.sharedInstance.9641
- _sharedInstance.sharedInstance.9747
- _sharedInstance.sharedManager.6696
- _sharedInstance.sharedManager.8310
- _sharedLogger.onceToken.13066
- _sharedLogger.onceToken.2604
- _sharedLogger.onceToken.6508
- _sharedLogger.onceToken.6710
- _sharedLogger.shared.13068
- _sharedManager.onceToken.13715
- _sharedMonitor.onceToken.5412
- _sharedMonitor.sharedMonitor.5414
- _sharedPreferences.onceToken.8709
CStrings:
+ "%s Acquire Secure Session Assertion with UUID: %@"
+ "%s Calling AVVTC %@ secure session under system daemon took: %f"
+ "%s Cannot acquire secure session assertion when current user is inactive"
+ "%s Release Secure Session Assertion with UUID: %@"
+ "%s SetAlertURL is failed with error: %@"
+ "%s Successfully activated secure session? %@, err: %@"
+ "%s Successfully deactivated secure session? %@, err: %@"
+ "%s UUID is nil"
+ "%s alert URL is nil"
+ "%s alertURL: %@, forType: %d"
+ "%s releasing All the secureAssertions when audio server daemons crash"
+ "%s releasing All the secureAssertions when system daemon crashes"
+ "-[CSLaunchAgentXPCClient activateSecureSession:error:]"
+ "-[CSLaunchAgentXPCClient resetAVVC]"
+ "-[CSLaunchAgentXPCClient setAlertSoundFromURL:forType:]"
+ "-[CSSecureSessionHandler CSAudioServerCrashMonitorDidReceiveServerCrash:]"
+ "-[CSSecureSessionHandler CSSystemDaemonStateMonitorDidReceiveSysDaemonCrash:]"
+ "-[CSSecureSessionHandler _activateSecureSessionIfNeeded]"
+ "-[CSSecureSessionHandler _deactivateSecureSessionIfNeeded]"
+ "-[CSSecureSessionHandler acquireSecureSessionAssertionWithUUID:]_block_invoke"
+ "-[CSSecureSessionHandler releaseSecureSessionAssertionWithUUID:]_block_invoke"
+ "B28@0:8B16^@20"
+ "CSSecureSessionHandler"
+ "CSSiriEnabledMonitorDelegate"
+ "CSSystemDaemonDisconnected"
+ "CSSystemDaemonStateMonitorDelegate"
+ "Secure Session Handler Queue"
+ "T@\"NSMutableSet\",&,N,V_assertionSet"
+ "T@\"NSUUID\",&,N,V_secureSessionAssertionUUID"
+ "_activateSecureSessionIfNeeded"
+ "_assertionSet"
+ "_deactivateSecureSessionIfNeeded"
+ "_secureSessionAssertionUUID"
+ "acquireSecureSessionAssertionWithUUID:"
+ "activate"
+ "activateSecureSession:error:"
+ "alertURL"
+ "assertionSet"
+ "audioDeviceID"
+ "currentSystemDaemonState"
+ "deactivate"
+ "duckAudioDeviceWithDeviceID:duckedLevel:rampDuration:"
+ "duckLevel"
+ "rampDuration"
+ "releaseAllSecureSessionAssertions"
+ "releaseSecureSessionAssertionWithUUID:"
+ "resetAVVC"
+ "secureSessionAssertionUUID"
+ "setAssertionSet:"
+ "setSecureSessionAssertionUUID:"
+ "siriEnablementSessionAssertionUUID"
+ "v24@0:8@\"CSSystemDaemonStateMonitor\"16"
+ "v28@0:8@\"CSSiriEnabledMonitor\"16B24"
+ "v28@0:8I16f20f24"
- "%s Notify Mac User session %@"
- "-[CSLaunchAgentXPCClient activateSecureSession:]"
- "-[CSMacUserSessionMonitor _notifySessionActive:]"
- "CSMacUserSessionMonitor"
- "_handleSessionActive:"
- "_handleSessionResign:"
- "_notifySessionActive:"
- "_registerUserSessionNotification"
- "_unregisterUserSessionNotification"
- "activateSecureSession:"
- "inactive"
- "macUserSessionMonitor:sessionActive:"

```
