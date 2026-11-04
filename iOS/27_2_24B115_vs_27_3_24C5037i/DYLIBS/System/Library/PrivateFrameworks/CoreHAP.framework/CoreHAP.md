## CoreHAP

> `/System/Library/PrivateFrameworks/CoreHAP.framework/CoreHAP`

```diff

-1520.2.7.1.3
-  __TEXT.__text: 0x2f9040
-  __TEXT.__objc_methlist: 0x1c9d8
-  __TEXT.__const: 0x1818
+1535.0.0.0.2
+  __TEXT.__text: 0x30f7e8
+  __TEXT.__objc_methlist: 0x1d1a8
+  __TEXT.__const: 0x1aa8
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__constg_swiftt: 0xc20
-  __TEXT.__swift5_typeref: 0x533
-  __TEXT.__swift5_builtin: 0xdc
-  __TEXT.__swift5_reflstr: 0x851
-  __TEXT.__swift5_fieldmd: 0x6a4
-  __TEXT.__swift5_assocty: 0x138
-  __TEXT.__swift5_proto: 0x78
-  __TEXT.__swift5_types: 0x5c
-  __TEXT.__cstring: 0x17714
-  __TEXT.__oslogstring: 0x4b2bb
+  __TEXT.__constg_swiftt: 0xd6c
+  __TEXT.__swift5_typeref: 0x567
+  __TEXT.__swift5_reflstr: 0x927
+  __TEXT.__swift5_fieldmd: 0x748
+  __TEXT.__swift5_builtin: 0xf0
+  __TEXT.__swift5_assocty: 0x198
+  __TEXT.__swift5_proto: 0x8c
+  __TEXT.__swift5_types: 0x64
+  __TEXT.__cstring: 0x19245
+  __TEXT.__oslogstring: 0x4cebb
+  __TEXT.__swift5_capture: 0x2c0
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__swift5_capture: 0x28c
-  __TEXT.__gcc_except_tab: 0x6f8c
-  __TEXT.__unwind_info: 0x9e50
-  __TEXT.__eh_frame: 0x1078
+  __TEXT.__gcc_except_tab: 0x71a0
+  __TEXT.__unwind_info: 0xa260
+  __TEXT.__eh_frame: 0x10e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6300
-  __DATA_CONST.__objc_classlist: 0xda0
-  __DATA_CONST.__objc_catlist: 0x30
+  __DATA_CONST.__const: 0x6868
+  __DATA_CONST.__objc_classlist: 0xdd8
+  __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x3f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x98f8
+  __DATA_CONST.__objc_selrefs: 0x9b30
   __DATA_CONST.__objc_protorefs: 0x110
-  __DATA_CONST.__objc_superrefs: 0xbc0
+  __DATA_CONST.__objc_superrefs: 0xc00
   __DATA_CONST.__objc_arraydata: 0x200
-  __DATA_CONST.__got: 0x11c8
-  __AUTH_CONST.__const: 0x1738
-  __AUTH_CONST.__cfstring: 0x117a0
-  __AUTH_CONST.__objc_const: 0x32290
+  __DATA_CONST.__got: 0x1208
+  __AUTH_CONST.__const: 0x1b00
+  __AUTH_CONST.__cfstring: 0x11b60
+  __AUTH_CONST.__objc_const: 0x32ff0
   __AUTH_CONST.__weak_auth_got: 0x10
-  __AUTH_CONST.__objc_intobj: 0x750
+  __AUTH_CONST.__objc_intobj: 0x780
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0xc0
-  __AUTH_CONST.__auth_got: 0x1448
-  __AUTH.__objc_data: 0x84c0
-  __AUTH.__data: 0x130
+  __AUTH_CONST.__auth_got: 0x14a0
+  __AUTH.__objc_data: 0x8830
+  __AUTH.__data: 0x138
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x28
-  __DATA.__objc_ivar: 0x1e08
-  __DATA.__data: 0x31b8
+  __DATA.__objc_ivar: 0x1e7c
+  __DATA.__data: 0x3250
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x90
   __DATA_DIRTY.__objc_data: 0x1108

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11431
-  Symbols:   18803
-  CStrings:  7784
+  Functions: 11695
+  Symbols:   19180
+  CStrings:  8059
 
Symbols:
+ +[HAPCharacteristicResponseTuple responseTupleForNullValueOfCharacteristic:]
+ +[HAPErrorEntry parsedFromData:error:]
+ +[HAPErrorStatus parsedFromData:error:]
+ +[HAPErrorStatusCodeWrapper parsedFromData:error:]
+ +[HAPIPAddressVersionWrapper parsedFromData:error:]
+ +[HAPTLVSessionTransportEndpointAddress parsedFromData:error:]
+ +[HAPTLVSessionTransportEndpointEntry parsedFromData:error:]
+ +[HAPTLVSessionTransportEndpointList parsedFromData:error:]
+ -[HAP2AccessoryDNSResolver _beginRetryLadderOnQueue]
+ -[HAP2AccessoryDNSResolver _clearPendingRetryRungOnQueue]
+ -[HAP2AccessoryDNSResolver _fireRetryRungOnQueueWithGeneration:]
+ -[HAP2AccessoryDNSResolver _scheduleNextRetryRungOnQueue]
+ -[HAP2AccessoryServer _cancelAccessoryDiscoveryRetry]
+ -[HAP2AccessoryServer _isKeepAliveActive]
+ -[HAP2AccessoryServer _startConfirming]
+ -[HAP2AccessoryServer accessoryDiscoveryRetryTimer]
+ -[HAP2AccessoryServer failedDiscoveryRetryCount]
+ -[HAP2AccessoryServer setAccessoryDiscoveryRetryTimer:]
+ -[HAP2AccessoryServer setFailedDiscoveryRetryCount:]
+ -[HAP2AccessoryServer(Paired) didChangeLocalEndpoints]
+ -[HAP2AccessoryServer(Paired) didRegisterTransportEndpoints:]
+ -[HAP2AccessoryServer(Paired) notifyReestablishedSecureSession]
+ -[HAP2AccessoryServer(Paired) readLocalEndpointsWithHandler:]
+ -[HAP2AccessoryServer(Paired) timerDidFire:]
+ -[HAP2AccessoryServerController closeClientOnTransport:completion:]
+ -[HAP2AccessoryServerController didRegisterTransportEndpoints:]
+ -[HAP2AccessoryServerController secureTransportDidChangeLocalEndpoints:]
+ -[HAP2AccessoryServerPairingDriverSoftwareAuthWorkItem _restoreTransportDelegate]
+ -[HAP2AccessoryServerPairingDriverSoftwareAuthWorkItem finishWithError:]
+ -[HAP2AccessoryServerPairingDriverSoftwareAuthWorkItem previousTransportDelegate]
+ -[HAP2AccessoryServerPairingDriverSoftwareAuthWorkItem setPreviousTransportDelegate:]
+ -[HAP2AccessoryServerPairingDriverSoftwareAuthWorkItem setTakenOverTransport:]
+ -[HAP2AccessoryServerPairingDriverSoftwareAuthWorkItem setTakeoverTransportDelegate:]
+ -[HAP2AccessoryServerPairingDriverSoftwareAuthWorkItem takenOverTransport]
+ -[HAP2AccessoryServerPairingDriverSoftwareAuthWorkItem takeoverTransportDelegate]
+ -[HAP2AccessoryServerSecureTransportBase closeClientOnTransport:completion:]
+ -[HAP2AccessoryServerSecureTransportBase didRegisterTransportEndpoints:]
+ -[HAP2AccessoryServerSecureTransportBase setSupportsSessionTransportEndpointList:]
+ -[HAP2AccessoryServerSecureTransportBase transportDidChangeLocalEndpoints:]
+ -[HAP2AccessoryServerTransportBase setSupportsSessionTransportEndpointList:]
+ -[HAP2AccessoryServerTransportBase supportsSessionTransportEndpointList]
+ -[HAP2AccessoryServerTransportCoAP _applyResolverAddressesOffQueue:]
+ -[HAP2AccessoryServerTransportCoAP _claimResolveTimeoutTimerExpecting:]
+ -[HAP2AccessoryServerTransportCoAP _enableRacingOnClient:transportType:]
+ -[HAP2AccessoryServerTransportCoAP _maybeApplyOffQueueWhileAwaitingInitialResolve:]
+ -[HAP2AccessoryServerTransportCoAP _notifyLocalEndpointsChanged]
+ -[HAP2AccessoryServerTransportCoAP _probeAcceptedLinkOnClient:transportType:attemptsLeft:]
+ -[HAP2AccessoryServerTransportCoAP _unsecuredClientWithTransportType:]
+ -[HAP2AccessoryServerTransportCoAP acceptedLinkProbeRetryInterval]
+ -[HAP2AccessoryServerTransportCoAP closeClientOnTransport:completion:]
+ -[HAP2AccessoryServerTransportCoAP didRegisterTransportEndpoints:]
+ -[HAP2AccessoryServerTransportCoAP setAcceptedLinkProbeRetryInterval:]
+ -[HAPAccessoryPairingRequest bestEffortNetworkCredentials]
+ -[HAPAccessoryPairingRequest requiredNetworkCredentials]
+ -[HAPAccessoryPairingRequest setBestEffortNetworkCredentials:]
+ -[HAPAccessoryPairingRequest setRequiredNetworkCredentials:]
+ -[HAPAccessoryServer didRegisterTransportEndpoints:]
+ -[HAPAccessoryServer readLocalEndpointsWithCompletion:]
+ -[HAPAccessoryServerBrowser pairSetupSession:pairSetupType:features:pairVerifyTLK:pairingRequest:error:]
+ -[HAPAccessoryServerBrowserNFC _reapDetectedServerIfNeeded:]
+ -[HAPAccessoryServerBrowserNFC _scheduleBusyRearmAfterDelay]
+ -[HAPAccessoryServerBrowserNFC _scheduleBusyRetry]
+ -[HAPAccessoryServerBrowserNFC busyRetryPending]
+ -[HAPAccessoryServerBrowserNFC committedBusyRetryCount]
+ -[HAPAccessoryServerBrowserNFC nfcServerDidStartPairing:]
+ -[HAPAccessoryServerBrowserNFC pairingServer]
+ -[HAPAccessoryServerBrowserNFC setBusyRetryPending:]
+ -[HAPAccessoryServerBrowserNFC setCommittedBusyRetryCount:]
+ -[HAPAccessoryServerBrowserNFC setPairingServer:]
+ -[HAPAccessoryServerHAP2Adapter accessoryServer:didUpdateLocalEndpoints:registeredEndpoints:]
+ -[HAPAccessoryServerHAP2Adapter accessoryServerReestablishedSecureSession:]
+ -[HAPAccessoryServerHAP2Adapter didRegisterTransportEndpoints:]
+ -[HAPAccessoryServerHAP2Adapter readLocalEndpointsWithCompletion:]
+ -[HAPAccessoryServerNFC _alreadyPairedErrorForPeer:marker:]
+ -[HAPAccessoryServerNFC _finishPairingWithPeerIdentifier:pairingKey:controllerIdentity:]
+ -[HAPAccessoryServerNFC _fireProxMetricBeginPhase:]
+ -[HAPAccessoryServerNFC _fireProxMetricEndPhase:completed:error:]
+ -[HAPAccessoryServerNFC _resumePairingWithPeerIdentifier:pairingKey:controllerIdentity:proceed:]
+ -[HAPAccessoryServerNFC isTagSessionOver]
+ -[HAPAccessoryServerNFC nfcM5SendTime]
+ -[HAPAccessoryServerNFC nfcReachedM6]
+ -[HAPAccessoryServerNFC noteReaderSessionEnded]
+ -[HAPAccessoryServerNFC pairVerifyTLKForPairSetupSession:]
+ -[HAPAccessoryServerNFC prepareForReuseWithReaderSession:]
+ -[HAPAccessoryServerNFC proxPairingMetricDelegateQueue]
+ -[HAPAccessoryServerNFC proxPairingMetricDelegate]
+ -[HAPAccessoryServerNFC setNfcM5SendTime:]
+ -[HAPAccessoryServerNFC setNfcReachedM6:]
+ -[HAPAccessoryServerNFC setProxPairingMetricDelegate:]
+ -[HAPAccessoryServerNFC setProxPairingMetricDelegateQueue:]
+ -[HAPCameraBufferActivityCommandRequest initWithStart:duration:activity:reason:]
+ -[HAPCameraBufferActivityCommandRequest reason]
+ -[HAPCameraBufferActivityCommandRequest setReason:]
+ -[HAPCameraVideoStreamCapabilities initWithIdentifier:quality:width:height:framesPerSecond:averageBitrate:peakBitrate:keyFrameInterval:videoCodec:]
+ -[HAPCameraVideoStreamCapabilities keyFrameInterval]
+ -[HAPCameraVideoStreamCapabilities setKeyFrameInterval:]
+ -[HAPCameraVideoStreamCapabilities setVideoCodec:]
+ -[HAPCameraVideoStreamCapabilities videoCodec]
+ -[HAPCharacteristicResponseTuple setValueIsNull:]
+ -[HAPCharacteristicResponseTuple valueIsNull]
+ -[HAPErrorEntry .cxx_destruct]
+ -[HAPErrorEntry copyWithZone:]
+ -[HAPErrorEntry description]
+ -[HAPErrorEntry errorCode]
+ -[HAPErrorEntry initWithErrorCode:manufacturerErrorInfo:]
+ -[HAPErrorEntry init]
+ -[HAPErrorEntry isEqual:]
+ -[HAPErrorEntry manufacturerErrorInfo]
+ -[HAPErrorEntry parseFromData:error:]
+ -[HAPErrorEntry serializeWithError:]
+ -[HAPErrorEntry setErrorCode:]
+ -[HAPErrorEntry setManufacturerErrorInfo:]
+ -[HAPErrorStatus .cxx_destruct]
+ -[HAPErrorStatus copyWithZone:]
+ -[HAPErrorStatus description]
+ -[HAPErrorStatus errorEntry]
+ -[HAPErrorStatus initWithErrorEntry:]
+ -[HAPErrorStatus init]
+ -[HAPErrorStatus isEqual:]
+ -[HAPErrorStatus parseFromData:error:]
+ -[HAPErrorStatus serializeWithError:]
+ -[HAPErrorStatus setErrorEntry:]
+ -[HAPErrorStatusCodeWrapper copyWithZone:]
+ -[HAPErrorStatusCodeWrapper description]
+ -[HAPErrorStatusCodeWrapper initWithValue:]
+ -[HAPErrorStatusCodeWrapper init]
+ -[HAPErrorStatusCodeWrapper isEqual:]
+ -[HAPErrorStatusCodeWrapper parseFromData:error:]
+ -[HAPErrorStatusCodeWrapper serializeWithError:]
+ -[HAPErrorStatusCodeWrapper setValue:]
+ -[HAPErrorStatusCodeWrapper value]
+ -[HAPIPAddressVersionWrapper copyWithZone:]
+ -[HAPIPAddressVersionWrapper description]
+ -[HAPIPAddressVersionWrapper initWithValue:]
+ -[HAPIPAddressVersionWrapper init]
+ -[HAPIPAddressVersionWrapper isEqual:]
+ -[HAPIPAddressVersionWrapper parseFromData:error:]
+ -[HAPIPAddressVersionWrapper serializeWithError:]
+ -[HAPIPAddressVersionWrapper setValue:]
+ -[HAPIPAddressVersionWrapper value]
+ -[HAPTLVSessionTransportEndpointAddress .cxx_destruct]
+ -[HAPTLVSessionTransportEndpointAddress IPAddressVersion]
+ -[HAPTLVSessionTransportEndpointAddress IPAddress]
+ -[HAPTLVSessionTransportEndpointAddress copyWithZone:]
+ -[HAPTLVSessionTransportEndpointAddress description]
+ -[HAPTLVSessionTransportEndpointAddress initWithIPAddressVersion:IPAddress:port:]
+ -[HAPTLVSessionTransportEndpointAddress init]
+ -[HAPTLVSessionTransportEndpointAddress isEqual:]
+ -[HAPTLVSessionTransportEndpointAddress parseFromData:error:]
+ -[HAPTLVSessionTransportEndpointAddress port]
+ -[HAPTLVSessionTransportEndpointAddress serializeWithError:]
+ -[HAPTLVSessionTransportEndpointAddress setIPAddress:]
+ -[HAPTLVSessionTransportEndpointAddress setIPAddressVersion:]
+ -[HAPTLVSessionTransportEndpointAddress setPort:]
+ -[HAPTLVSessionTransportEndpointEntry .cxx_destruct]
+ -[HAPTLVSessionTransportEndpointEntry copyWithZone:]
+ -[HAPTLVSessionTransportEndpointEntry description]
+ -[HAPTLVSessionTransportEndpointEntry endpointAddress]
+ -[HAPTLVSessionTransportEndpointEntry initWithTransportType:endpointAddress:]
+ -[HAPTLVSessionTransportEndpointEntry init]
+ -[HAPTLVSessionTransportEndpointEntry isEqual:]
+ -[HAPTLVSessionTransportEndpointEntry parseFromData:error:]
+ -[HAPTLVSessionTransportEndpointEntry serializeWithError:]
+ -[HAPTLVSessionTransportEndpointEntry setEndpointAddress:]
+ -[HAPTLVSessionTransportEndpointEntry setTransportType:]
+ -[HAPTLVSessionTransportEndpointEntry transportType]
+ -[HAPTLVSessionTransportEndpointList .cxx_destruct]
+ -[HAPTLVSessionTransportEndpointList copyWithZone:]
+ -[HAPTLVSessionTransportEndpointList description]
+ -[HAPTLVSessionTransportEndpointList entries]
+ -[HAPTLVSessionTransportEndpointList initWithEntries:]
+ -[HAPTLVSessionTransportEndpointList init]
+ -[HAPTLVSessionTransportEndpointList isEqual:]
+ -[HAPTLVSessionTransportEndpointList parseFromData:error:]
+ -[HAPTLVSessionTransportEndpointList serializeWithError:]
+ -[HAPTLVSessionTransportEndpointList setEntries:]
+ -[_HAPAccessoryServerBTLE200 _notifyDelegatesOfSecureSessionEstablished]
+ GCC_except_table1001
+ GCC_except_table1003
+ GCC_except_table10036
+ GCC_except_table1007
+ GCC_except_table10073
+ GCC_except_table1014
+ GCC_except_table1017
+ GCC_except_table10201
+ GCC_except_table10203
+ GCC_except_table10205
+ GCC_except_table10207
+ GCC_except_table10209
+ GCC_except_table10211
+ GCC_except_table10213
+ GCC_except_table10219
+ GCC_except_table10221
+ GCC_except_table10224
+ GCC_except_table10226
+ GCC_except_table10228
+ GCC_except_table10246
+ GCC_except_table10254
+ GCC_except_table10259
+ GCC_except_table10262
+ GCC_except_table10265
+ GCC_except_table10291
+ GCC_except_table10294
+ GCC_except_table10295
+ GCC_except_table10339
+ GCC_except_table10340
+ GCC_except_table10341
+ GCC_except_table10343
+ GCC_except_table10344
+ GCC_except_table10346
+ GCC_except_table10347
+ GCC_except_table10348
+ GCC_except_table10350
+ GCC_except_table10351
+ GCC_except_table10353
+ GCC_except_table10357
+ GCC_except_table10358
+ GCC_except_table10364
+ GCC_except_table10416
+ GCC_except_table1051
+ GCC_except_table10599
+ GCC_except_table10601
+ GCC_except_table10603
+ GCC_except_table10606
+ GCC_except_table10608
+ GCC_except_table1061
+ GCC_except_table10610
+ GCC_except_table10612
+ GCC_except_table10613
+ GCC_except_table10620
+ GCC_except_table10622
+ GCC_except_table10623
+ GCC_except_table1069
+ GCC_except_table1096
+ GCC_except_table1100
+ GCC_except_table1103
+ GCC_except_table1105
+ GCC_except_table1111
+ GCC_except_table1113
+ GCC_except_table1126
+ GCC_except_table1130
+ GCC_except_table1134
+ GCC_except_table1144
+ GCC_except_table1145
+ GCC_except_table1150
+ GCC_except_table1153
+ GCC_except_table1156
+ GCC_except_table1161
+ GCC_except_table1165
+ GCC_except_table1171
+ GCC_except_table1172
+ GCC_except_table1177
+ GCC_except_table1178
+ GCC_except_table1213
+ GCC_except_table1221
+ GCC_except_table1222
+ GCC_except_table1250
+ GCC_except_table1273
+ GCC_except_table1292
+ GCC_except_table1316
+ GCC_except_table1320
+ GCC_except_table1334
+ GCC_except_table1339
+ GCC_except_table1444
+ GCC_except_table1446
+ GCC_except_table2004
+ GCC_except_table2009
+ GCC_except_table2011
+ GCC_except_table2025
+ GCC_except_table2037
+ GCC_except_table2039
+ GCC_except_table2041
+ GCC_except_table2043
+ GCC_except_table2173
+ GCC_except_table2177
+ GCC_except_table2179
+ GCC_except_table2381
+ GCC_except_table2601
+ GCC_except_table2603
+ GCC_except_table2608
+ GCC_except_table2614
+ GCC_except_table2616
+ GCC_except_table2622
+ GCC_except_table2624
+ GCC_except_table2628
+ GCC_except_table2640
+ GCC_except_table2646
+ GCC_except_table2648
+ GCC_except_table2650
+ GCC_except_table2652
+ GCC_except_table2658
+ GCC_except_table2662
+ GCC_except_table2670
+ GCC_except_table2672
+ GCC_except_table2693
+ GCC_except_table2704
+ GCC_except_table2708
+ GCC_except_table2749
+ GCC_except_table2865
+ GCC_except_table2869
+ GCC_except_table2870
+ GCC_except_table2872
+ GCC_except_table2874
+ GCC_except_table2886
+ GCC_except_table2891
+ GCC_except_table2895
+ GCC_except_table2898
+ GCC_except_table2900
+ GCC_except_table2903
+ GCC_except_table2920
+ GCC_except_table2930
+ GCC_except_table2932
+ GCC_except_table2934
+ GCC_except_table2939
+ GCC_except_table2942
+ GCC_except_table2944
+ GCC_except_table2947
+ GCC_except_table2950
+ GCC_except_table2954
+ GCC_except_table2956
+ GCC_except_table2959
+ GCC_except_table2962
+ GCC_except_table2964
+ GCC_except_table2966
+ GCC_except_table2970
+ GCC_except_table2974
+ GCC_except_table2982
+ GCC_except_table2993
+ GCC_except_table3035
+ GCC_except_table3036
+ GCC_except_table3037
+ GCC_except_table3039
+ GCC_except_table3040
+ GCC_except_table3041
+ GCC_except_table3043
+ GCC_except_table3047
+ GCC_except_table3048
+ GCC_except_table3074
+ GCC_except_table3078
+ GCC_except_table3082
+ GCC_except_table3246
+ GCC_except_table3253
+ GCC_except_table3257
+ GCC_except_table3261
+ GCC_except_table3265
+ GCC_except_table3268
+ GCC_except_table3270
+ GCC_except_table3272
+ GCC_except_table3275
+ GCC_except_table3281
+ GCC_except_table3283
+ GCC_except_table3286
+ GCC_except_table3287
+ GCC_except_table3289
+ GCC_except_table333
+ GCC_except_table3390
+ GCC_except_table3398
+ GCC_except_table3399
+ GCC_except_table3400
+ GCC_except_table3401
+ GCC_except_table3402
+ GCC_except_table3403
+ GCC_except_table341
+ GCC_except_table3418
+ GCC_except_table3432
+ GCC_except_table3512
+ GCC_except_table352
+ GCC_except_table3524
+ GCC_except_table366
+ GCC_except_table369
+ GCC_except_table3731
+ GCC_except_table374
+ GCC_except_table3740
+ GCC_except_table3757
+ GCC_except_table3791
+ GCC_except_table3807
+ GCC_except_table3809
+ GCC_except_table382
+ GCC_except_table3821
+ GCC_except_table3828
+ GCC_except_table3850
+ GCC_except_table3864
+ GCC_except_table3865
+ GCC_except_table3866
+ GCC_except_table3869
+ GCC_except_table3875
+ GCC_except_table388
+ GCC_except_table3882
+ GCC_except_table3885
+ GCC_except_table3890
+ GCC_except_table3895
+ GCC_except_table390
+ GCC_except_table3900
+ GCC_except_table392
+ GCC_except_table3940
+ GCC_except_table3957
+ GCC_except_table3960
+ GCC_except_table3965
+ GCC_except_table3967
+ GCC_except_table3983
+ GCC_except_table3998
+ GCC_except_table4000
+ GCC_except_table4004
+ GCC_except_table4012
+ GCC_except_table4020
+ GCC_except_table403
+ GCC_except_table4084
+ GCC_except_table4091
+ GCC_except_table4093
+ GCC_except_table4094
+ GCC_except_table4117
+ GCC_except_table4137
+ GCC_except_table436
+ GCC_except_table4366
+ GCC_except_table4441
+ GCC_except_table4448
+ GCC_except_table4452
+ GCC_except_table4454
+ GCC_except_table4456
+ GCC_except_table4458
+ GCC_except_table4462
+ GCC_except_table4465
+ GCC_except_table4471
+ GCC_except_table4482
+ GCC_except_table4484
+ GCC_except_table4485
+ GCC_except_table4487
+ GCC_except_table4490
+ GCC_except_table4492
+ GCC_except_table4493
+ GCC_except_table4495
+ GCC_except_table4496
+ GCC_except_table450
+ GCC_except_table451
+ GCC_except_table4515
+ GCC_except_table4518
+ GCC_except_table4529
+ GCC_except_table4530
+ GCC_except_table4532
+ GCC_except_table4534
+ GCC_except_table4537
+ GCC_except_table4541
+ GCC_except_table4543
+ GCC_except_table4546
+ GCC_except_table4549
+ GCC_except_table4561
+ GCC_except_table4563
+ GCC_except_table4567
+ GCC_except_table4571
+ GCC_except_table4575
+ GCC_except_table458
+ GCC_except_table4580
+ GCC_except_table4593
+ GCC_except_table460
+ GCC_except_table4612
+ GCC_except_table462
+ GCC_except_table463
+ GCC_except_table4635
+ GCC_except_table4641
+ GCC_except_table4645
+ GCC_except_table4649
+ GCC_except_table4651
+ GCC_except_table4654
+ GCC_except_table4656
+ GCC_except_table4658
+ GCC_except_table4665
+ GCC_except_table4666
+ GCC_except_table4667
+ GCC_except_table4668
+ GCC_except_table4672
+ GCC_except_table4674
+ GCC_except_table468
+ GCC_except_table4764
+ GCC_except_table4765
+ GCC_except_table4766
+ GCC_except_table4767
+ GCC_except_table4768
+ GCC_except_table4769
+ GCC_except_table4770
+ GCC_except_table4771
+ GCC_except_table4772
+ GCC_except_table4774
+ GCC_except_table4775
+ GCC_except_table4777
+ GCC_except_table4778
+ GCC_except_table4817
+ GCC_except_table4844
+ GCC_except_table485
+ GCC_except_table487
+ GCC_except_table493
+ GCC_except_table4935
+ GCC_except_table4939
+ GCC_except_table494
+ GCC_except_table4941
+ GCC_except_table4943
+ GCC_except_table4980
+ GCC_except_table499
+ GCC_except_table500
+ GCC_except_table5034
+ GCC_except_table5038
+ GCC_except_table5039
+ GCC_except_table5041
+ GCC_except_table5043
+ GCC_except_table5046
+ GCC_except_table5049
+ GCC_except_table5052
+ GCC_except_table5055
+ GCC_except_table5058
+ GCC_except_table506
+ GCC_except_table5061
+ GCC_except_table5064
+ GCC_except_table5067
+ GCC_except_table5072
+ GCC_except_table5085
+ GCC_except_table5090
+ GCC_except_table5094
+ GCC_except_table5096
+ GCC_except_table5099
+ GCC_except_table5113
+ GCC_except_table5125
+ GCC_except_table5131
+ GCC_except_table5132
+ GCC_except_table5136
+ GCC_except_table515
+ GCC_except_table5154
+ GCC_except_table5156
+ GCC_except_table5158
+ GCC_except_table516
+ GCC_except_table5168
+ GCC_except_table517
+ GCC_except_table5171
+ GCC_except_table5173
+ GCC_except_table518
+ GCC_except_table5184
+ GCC_except_table5189
+ GCC_except_table519
+ GCC_except_table520
+ GCC_except_table5200
+ GCC_except_table521
+ GCC_except_table5211
+ GCC_except_table5213
+ GCC_except_table5224
+ GCC_except_table5226
+ GCC_except_table5228
+ GCC_except_table524
+ GCC_except_table530
+ GCC_except_table534
+ GCC_except_table535
+ GCC_except_table543
+ GCC_except_table5516
+ GCC_except_table5522
+ GCC_except_table5539
+ GCC_except_table5543
+ GCC_except_table5561
+ GCC_except_table5567
+ GCC_except_table559
+ GCC_except_table5595
+ GCC_except_table5599
+ GCC_except_table5717
+ GCC_except_table580
+ GCC_except_table581
+ GCC_except_table583
+ GCC_except_table584
+ GCC_except_table587
+ GCC_except_table588
+ GCC_except_table603
+ GCC_except_table6040
+ GCC_except_table6042
+ GCC_except_table6044
+ GCC_except_table6046
+ GCC_except_table606
+ GCC_except_table613
+ GCC_except_table616
+ GCC_except_table6236
+ GCC_except_table6245
+ GCC_except_table6246
+ GCC_except_table6256
+ GCC_except_table6298
+ GCC_except_table6301
+ GCC_except_table6302
+ GCC_except_table6303
+ GCC_except_table6304
+ GCC_except_table631
+ GCC_except_table641
+ GCC_except_table643
+ GCC_except_table6481
+ GCC_except_table6482
+ GCC_except_table6483
+ GCC_except_table6484
+ GCC_except_table6485
+ GCC_except_table6486
+ GCC_except_table6487
+ GCC_except_table6488
+ GCC_except_table6490
+ GCC_except_table6511
+ GCC_except_table6522
+ GCC_except_table6524
+ GCC_except_table6529
+ GCC_except_table6532
+ GCC_except_table6535
+ GCC_except_table6539
+ GCC_except_table6543
+ GCC_except_table7094
+ GCC_except_table7095
+ GCC_except_table7114
+ GCC_except_table7124
+ GCC_except_table7127
+ GCC_except_table7132
+ GCC_except_table7135
+ GCC_except_table7140
+ GCC_except_table7409
+ GCC_except_table7413
+ GCC_except_table7473
+ GCC_except_table7477
+ GCC_except_table7479
+ GCC_except_table7481
+ GCC_except_table7657
+ GCC_except_table7665
+ GCC_except_table7667
+ GCC_except_table7669
+ GCC_except_table7671
+ GCC_except_table7677
+ GCC_except_table7690
+ GCC_except_table7709
+ GCC_except_table7734
+ GCC_except_table7738
+ GCC_except_table7743
+ GCC_except_table7745
+ GCC_except_table7749
+ GCC_except_table7751
+ GCC_except_table7827
+ GCC_except_table7834
+ GCC_except_table7838
+ GCC_except_table7839
+ GCC_except_table7840
+ GCC_except_table7841
+ GCC_except_table7850
+ GCC_except_table7866
+ GCC_except_table7923
+ GCC_except_table7935
+ GCC_except_table7938
+ GCC_except_table7943
+ GCC_except_table7945
+ GCC_except_table7959
+ GCC_except_table8225
+ GCC_except_table8238
+ GCC_except_table8243
+ GCC_except_table8246
+ GCC_except_table8247
+ GCC_except_table8249
+ GCC_except_table8250
+ GCC_except_table8252
+ GCC_except_table8282
+ GCC_except_table8304
+ GCC_except_table8308
+ GCC_except_table8312
+ GCC_except_table8317
+ GCC_except_table8321
+ GCC_except_table8325
+ GCC_except_table8329
+ GCC_except_table8333
+ GCC_except_table8341
+ GCC_except_table8343
+ GCC_except_table8345
+ GCC_except_table8371
+ GCC_except_table8382
+ GCC_except_table8529
+ GCC_except_table8533
+ GCC_except_table8569
+ GCC_except_table8671
+ GCC_except_table8736
+ GCC_except_table8750
+ GCC_except_table8751
+ GCC_except_table8756
+ GCC_except_table8757
+ GCC_except_table8764
+ GCC_except_table8776
+ GCC_except_table8786
+ GCC_except_table8789
+ GCC_except_table8791
+ GCC_except_table8795
+ GCC_except_table8801
+ GCC_except_table8815
+ GCC_except_table8818
+ GCC_except_table8819
+ GCC_except_table8824
+ GCC_except_table8834
+ GCC_except_table8837
+ GCC_except_table8858
+ GCC_except_table8864
+ GCC_except_table8875
+ GCC_except_table8879
+ GCC_except_table8887
+ GCC_except_table8911
+ GCC_except_table8912
+ GCC_except_table8917
+ GCC_except_table8921
+ GCC_except_table8922
+ GCC_except_table8925
+ GCC_except_table8931
+ GCC_except_table8935
+ GCC_except_table8939
+ GCC_except_table8941
+ GCC_except_table8943
+ GCC_except_table8947
+ GCC_except_table903
+ GCC_except_table9101
+ GCC_except_table913
+ GCC_except_table9138
+ GCC_except_table9196
+ GCC_except_table9206
+ GCC_except_table9212
+ GCC_except_table9219
+ GCC_except_table9220
+ GCC_except_table9236
+ GCC_except_table9240
+ GCC_except_table9241
+ GCC_except_table9242
+ GCC_except_table927
+ GCC_except_table9291
+ GCC_except_table9292
+ GCC_except_table9294
+ GCC_except_table9297
+ GCC_except_table9324
+ GCC_except_table9325
+ GCC_except_table9330
+ GCC_except_table935
+ GCC_except_table9368
+ GCC_except_table9369
+ GCC_except_table9370
+ GCC_except_table9375
+ GCC_except_table9376
+ GCC_except_table9377
+ GCC_except_table9380
+ GCC_except_table9383
+ GCC_except_table9384
+ GCC_except_table9388
+ GCC_except_table9389
+ GCC_except_table9391
+ GCC_except_table9400
+ GCC_except_table9403
+ GCC_except_table9408
+ GCC_except_table9410
+ GCC_except_table9413
+ GCC_except_table9422
+ GCC_except_table9423
+ GCC_except_table9424
+ GCC_except_table9440
+ GCC_except_table9442
+ GCC_except_table9459
+ GCC_except_table9470
+ GCC_except_table9476
+ GCC_except_table9489
+ GCC_except_table9494
+ GCC_except_table9506
+ GCC_except_table9507
+ GCC_except_table9510
+ GCC_except_table9512
+ GCC_except_table9518
+ GCC_except_table9539
+ GCC_except_table9541
+ GCC_except_table9542
+ GCC_except_table9568
+ GCC_except_table964
+ GCC_except_table970
+ GCC_except_table9733
+ GCC_except_table9796
+ GCC_except_table982
+ GCC_except_table9828
+ GCC_except_table983
+ GCC_except_table9831
+ GCC_except_table985
+ GCC_except_table988
+ GCC_except_table991
+ GCC_except_table9998
+ _HAP2ResolverDNSSDCode
+ _HAPCharacteristicUUID_ErrorStatus
+ _HAPErrorStatusCodeAsString
+ _HAPIPAddressVersionAsString
+ _HAPNFCIsReaderBusyError
+ _HAPTLVParseLimitedLengthContiguousTLVs
+ _OBJC_CLASS_$_HAPErrorEntry
+ _OBJC_CLASS_$_HAPErrorStatus
+ _OBJC_CLASS_$_HAPErrorStatusCodeWrapper
+ _OBJC_CLASS_$_HAPIPAddressVersionWrapper
+ _OBJC_CLASS_$_HAPTLVSessionTransportEndpointAddress
+ _OBJC_CLASS_$_HAPTLVSessionTransportEndpointEntry
+ _OBJC_CLASS_$_HAPTLVSessionTransportEndpointList
+ _OBJC_CLASS_$_HMFExponentialBackoffTimer
+ _OBJC_CLASS_$_HMFSystemDefaultNetworkPathMonitor
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_IVAR_$_HAP2AccessoryDNSResolver._everDelivered
+ _OBJC_IVAR_$_HAP2AccessoryDNSResolver._isSubscribed
+ _OBJC_IVAR_$_HAP2AccessoryDNSResolver._retryGeneration
+ _OBJC_IVAR_$_HAP2AccessoryDNSResolver._retryPending
+ _OBJC_IVAR_$_HAP2AccessoryDNSResolver._retryRung
+ _OBJC_IVAR_$_HAP2AccessoryDNSResolver._stopped
+ _OBJC_IVAR_$_HAP2AccessoryServer._accessoryDiscoveryRetryTimer
+ _OBJC_IVAR_$_HAP2AccessoryServer._failedDiscoveryRetryCount
+ _OBJC_IVAR_$_HAP2AccessoryServerPairingDriverSoftwareAuthWorkItem._previousTransportDelegate
+ _OBJC_IVAR_$_HAP2AccessoryServerPairingDriverSoftwareAuthWorkItem._takenOverTransport
+ _OBJC_IVAR_$_HAP2AccessoryServerPairingDriverSoftwareAuthWorkItem._takeoverTransportDelegate
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportBase._supportsSessionTransportEndpointList
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._acceptedLinkProbeRetryInterval
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._registeredTransportEndpoints
+ _OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._resolveTimeoutClaimLock
+ _OBJC_IVAR_$_HAPAccessoryPairingRequest._bestEffortNetworkCredentials
+ _OBJC_IVAR_$_HAPAccessoryPairingRequest._requiredNetworkCredentials
+ _OBJC_IVAR_$_HAPAccessoryServerBrowserNFC._busyRetryPending
+ _OBJC_IVAR_$_HAPAccessoryServerBrowserNFC._committedBusyRetryCount
+ _OBJC_IVAR_$_HAPAccessoryServerBrowserNFC._pairingServer
+ _OBJC_IVAR_$_HAPAccessoryServerNFC._nfcM5SendTime
+ _OBJC_IVAR_$_HAPAccessoryServerNFC._nfcReachedM6
+ _OBJC_IVAR_$_HAPAccessoryServerNFC._nfcStateLock
+ _OBJC_IVAR_$_HAPAccessoryServerNFC._proxPairingMetricDelegate
+ _OBJC_IVAR_$_HAPAccessoryServerNFC._proxPairingMetricDelegateQueue
+ _OBJC_IVAR_$_HAPCameraBufferActivityCommandRequest._reason
+ _OBJC_IVAR_$_HAPCameraVideoStreamCapabilities._keyFrameInterval
+ _OBJC_IVAR_$_HAPCameraVideoStreamCapabilities._videoCodec
+ _OBJC_IVAR_$_HAPCharacteristicResponseTuple._valueIsNull
+ _OBJC_IVAR_$_HAPErrorEntry._errorCode
+ _OBJC_IVAR_$_HAPErrorEntry._manufacturerErrorInfo
+ _OBJC_IVAR_$_HAPErrorStatus._errorEntry
+ _OBJC_IVAR_$_HAPErrorStatusCodeWrapper._value
+ _OBJC_IVAR_$_HAPIPAddressVersionWrapper._value
+ _OBJC_IVAR_$_HAPTLVSessionTransportEndpointAddress._IPAddress
+ _OBJC_IVAR_$_HAPTLVSessionTransportEndpointAddress._IPAddressVersion
+ _OBJC_IVAR_$_HAPTLVSessionTransportEndpointAddress._port
+ _OBJC_IVAR_$_HAPTLVSessionTransportEndpointEntry._endpointAddress
+ _OBJC_IVAR_$_HAPTLVSessionTransportEndpointEntry._transportType
+ _OBJC_IVAR_$_HAPTLVSessionTransportEndpointList._entries
+ _OBJC_METACLASS_$_HAPErrorEntry
+ _OBJC_METACLASS_$_HAPErrorStatus
+ _OBJC_METACLASS_$_HAPErrorStatusCodeWrapper
+ _OBJC_METACLASS_$_HAPIPAddressVersionWrapper
+ _OBJC_METACLASS_$_HAPTLVSessionTransportEndpointAddress
+ _OBJC_METACLASS_$_HAPTLVSessionTransportEndpointEntry
+ _OBJC_METACLASS_$_HAPTLVSessionTransportEndpointList
+ __OBJC_$_CLASS_METHODS_HAPErrorEntry
+ __OBJC_$_CLASS_METHODS_HAPErrorStatus
+ __OBJC_$_CLASS_METHODS_HAPErrorStatusCodeWrapper
+ __OBJC_$_CLASS_METHODS_HAPIPAddressVersionWrapper
+ __OBJC_$_CLASS_METHODS_HAPTLVSessionTransportEndpointAddress
+ __OBJC_$_CLASS_METHODS_HAPTLVSessionTransportEndpointEntry
+ __OBJC_$_CLASS_METHODS_HAPTLVSessionTransportEndpointList
+ __OBJC_$_INSTANCE_METHODS_HAPErrorEntry
+ __OBJC_$_INSTANCE_METHODS_HAPErrorStatus
+ __OBJC_$_INSTANCE_METHODS_HAPErrorStatusCodeWrapper
+ __OBJC_$_INSTANCE_METHODS_HAPIPAddressVersionWrapper
+ __OBJC_$_INSTANCE_METHODS_HAPTLVSessionTransportEndpointAddress
+ __OBJC_$_INSTANCE_METHODS_HAPTLVSessionTransportEndpointEntry
+ __OBJC_$_INSTANCE_METHODS_HAPTLVSessionTransportEndpointList
+ __OBJC_$_INSTANCE_VARIABLES_HAPErrorEntry
+ __OBJC_$_INSTANCE_VARIABLES_HAPErrorStatus
+ __OBJC_$_INSTANCE_VARIABLES_HAPErrorStatusCodeWrapper
+ __OBJC_$_INSTANCE_VARIABLES_HAPIPAddressVersionWrapper
+ __OBJC_$_INSTANCE_VARIABLES_HAPTLVSessionTransportEndpointAddress
+ __OBJC_$_INSTANCE_VARIABLES_HAPTLVSessionTransportEndpointEntry
+ __OBJC_$_INSTANCE_VARIABLES_HAPTLVSessionTransportEndpointList
+ __OBJC_$_PROP_LIST_HAPErrorEntry
+ __OBJC_$_PROP_LIST_HAPErrorStatus
+ __OBJC_$_PROP_LIST_HAPErrorStatusCodeWrapper
+ __OBJC_$_PROP_LIST_HAPIPAddressVersionWrapper
+ __OBJC_$_PROP_LIST_HAPTLVSessionTransportEndpointAddress
+ __OBJC_$_PROP_LIST_HAPTLVSessionTransportEndpointEntry
+ __OBJC_$_PROP_LIST_HAPTLVSessionTransportEndpointList
+ __OBJC_CLASS_PROTOCOLS_$_HAPErrorEntry
+ __OBJC_CLASS_PROTOCOLS_$_HAPErrorStatus
+ __OBJC_CLASS_PROTOCOLS_$_HAPErrorStatusCodeWrapper
+ __OBJC_CLASS_PROTOCOLS_$_HAPIPAddressVersionWrapper
+ __OBJC_CLASS_PROTOCOLS_$_HAPTLVSessionTransportEndpointAddress
+ __OBJC_CLASS_PROTOCOLS_$_HAPTLVSessionTransportEndpointEntry
+ __OBJC_CLASS_PROTOCOLS_$_HAPTLVSessionTransportEndpointList
+ __OBJC_CLASS_RO_$_HAPErrorEntry
+ __OBJC_CLASS_RO_$_HAPErrorStatus
+ __OBJC_CLASS_RO_$_HAPErrorStatusCodeWrapper
+ __OBJC_CLASS_RO_$_HAPIPAddressVersionWrapper
+ __OBJC_CLASS_RO_$_HAPTLVSessionTransportEndpointAddress
+ __OBJC_CLASS_RO_$_HAPTLVSessionTransportEndpointEntry
+ __OBJC_CLASS_RO_$_HAPTLVSessionTransportEndpointList
+ __OBJC_METACLASS_RO_$_HAPErrorEntry
+ __OBJC_METACLASS_RO_$_HAPErrorStatus
+ __OBJC_METACLASS_RO_$_HAPErrorStatusCodeWrapper
+ __OBJC_METACLASS_RO_$_HAPIPAddressVersionWrapper
+ __OBJC_METACLASS_RO_$_HAPTLVSessionTransportEndpointAddress
+ __OBJC_METACLASS_RO_$_HAPTLVSessionTransportEndpointEntry
+ __OBJC_METACLASS_RO_$_HAPTLVSessionTransportEndpointList
+ ___44-[HAP2AccessoryServer(Paired) timerDidFire:]_block_invoke
+ ___47-[HAPAccessoryServerNFC noteReaderSessionEnded]_block_invoke
+ ___51-[HAPAccessoryServerNFC _fireProxMetricBeginPhase:]_block_invoke
+ ___54-[HAP2AccessoryServer(Paired) didChangeLocalEndpoints]_block_invoke
+ ___54-[HAP2AccessoryServer(Paired) didChangeLocalEndpoints]_block_invoke_2
+ ___57-[HAP2AccessoryDNSResolver _scheduleNextRetryRungOnQueue]_block_invoke
+ ___57-[HAPAccessoryServerBrowserNFC nfcServerDidStartPairing:]_block_invoke
+ ___58-[HAPAccessoryServerNFC pairVerifyTLKForPairSetupSession:]_block_invoke
+ ___58-[HAPAccessoryServerNFC prepareForReuseWithReaderSession:]_block_invoke
+ ___60-[HAPAccessoryServerBrowserNFC _scheduleBusyRearmAfterDelay]_block_invoke
+ ___61-[HAP2AccessoryServer(Paired) didRegisterTransportEndpoints:]_block_invoke
+ ___61-[HAP2AccessoryServer(Paired) readLocalEndpointsWithHandler:]_block_invoke
+ ___63-[HAP2AccessoryServer(Paired) notifyReestablishedSecureSession]_block_invoke
+ ___63-[HAP2AccessoryServerController didRegisterTransportEndpoints:]_block_invoke
+ ___65-[HAPAccessoryServerNFC _fireProxMetricEndPhase:completed:error:]_block_invoke
+ ___66-[HAP2AccessoryServerTransportCoAP didRegisterTransportEndpoints:]_block_invoke
+ ___67-[HAP2AccessoryServerController closeClientOnTransport:completion:]_block_invoke
+ ___67-[HAP2AccessoryServerController closeClientOnTransport:completion:]_block_invoke_2
+ ___70-[HAP2AccessoryServerTransportCoAP closeClientOnTransport:completion:]_block_invoke
+ ___72-[HAP2AccessoryServerSecureTransportBase didRegisterTransportEndpoints:]_block_invoke
+ ___72-[_HAPAccessoryServerBTLE200 _notifyDelegatesOfSecureSessionEstablished]_block_invoke
+ ___75-[HAP2AccessoryServerSecureTransportBase transportDidChangeLocalEndpoints:]_block_invoke
+ ___75-[HAPAccessoryServerHAP2Adapter accessoryServerReestablishedSecureSession:]_block_invoke
+ ___76-[HAP2AccessoryServerSecureTransportBase closeClientOnTransport:completion:]_block_invoke
+ ___88-[HAPAccessoryServerNFC _finishPairingWithPeerIdentifier:pairingKey:controllerIdentity:]_block_invoke
+ ___90-[HAP2AccessoryServerTransportCoAP _probeAcceptedLinkOnClient:transportType:attemptsLeft:]_block_invoke
+ ___90-[HAP2AccessoryServerTransportCoAP _probeAcceptedLinkOnClient:transportType:attemptsLeft:]_block_invoke_2
+ ___90-[HAPAccessoryServerNFC pairSetupSession:didPairWithPeerIdentifier:ecdsaPairingKey:error:]_block_invoke_2
+ ___90-[HAPAccessoryServerNFC pairSetupSession:didPairWithPeerIdentifier:ecdsaPairingKey:error:]_block_invoke_3
+ ___block_descriptor_32_e1275_v24?0"HAP2CoAPClient"8^{coap_session_t=iiiIQQQ{coap_addr_hash_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{coap_sockaddr_un=C[27c]})}Si}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{coap_sockaddr_un=C[27c]})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{coap_sockaddr_un=C[27c]})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{coap_sockaddr_un=C[27c]})}[3{?=^?^?^?^?}]}^{coap_endpoint_t}^{coap_context_t}^vSCCi^{coap_queue_t}^{coap_lg_xmit_t}^{coap_lg_crcv_t}^{coap_lg_srcv_t}Q[8C]Q^{coap_pdu_t}QQQQQ{coap_dtls_cpsk_t=CCC[5C]^?^v*{coap_dtls_cpsk_info_t={coap_bin_const_t=Q*}{coap_bin_const_t=Q*}}}^{coap_bin_const_t}^{coap_bin_const_t}^{coap_bin_const_t}^v{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}SS{coap_fixed_point_t=SS}IIiIICCCCCCCCCCiIQ^{coap_bin_const_t}^{coap_bin_const_t}iii^{coap_bin_const_t}dddIddddCddI[32{?=SdC}]}16l
+ ___block_descriptor_40_e8_32w_e39_v24?0"NSDictionary"8"NSDictionary"16lw32l8
+ ___block_descriptor_48_e1275_v24?0"HAP2CoAPClient"8^{coap_session_t=iiiIQQQ{coap_addr_hash_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{coap_sockaddr_un=C[27c]})}Si}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{coap_sockaddr_un=C[27c]})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{coap_sockaddr_un=C[27c]})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{coap_sockaddr_un=C[27c]})}[3{?=^?^?^?^?}]}^{coap_endpoint_t}^{coap_context_t}^vSCCi^{coap_queue_t}^{coap_lg_xmit_t}^{coap_lg_crcv_t}^{coap_lg_srcv_t}Q[8C]Q^{coap_pdu_t}QQQQQ{coap_dtls_cpsk_t=CCC[5C]^?^v*{coap_dtls_cpsk_info_t={coap_bin_const_t=Q*}{coap_bin_const_t=Q*}}}^{coap_bin_const_t}^{coap_bin_const_t}^{coap_bin_const_t}^v{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}SS{coap_fixed_point_t=SS}IIiIICCCCCCCCCCiIQ^{coap_bin_const_t}^{coap_bin_const_t}iii^{coap_bin_const_t}dddIddddCddI[32{?=SdC}]}16l
+ ___block_descriptor_48_e8_32bs40r_e8_v16?0q8ls32l8r40l8
+ ___block_descriptor_48_e8_32bs40w_e1638_v24?0^{coap_context_t={coap_opt_filter_t=S[2S][6C]}^{coap_resource_t}^{coap_resource_t}^{coap_resource_t}^?Q^{coap_queue_t}^{coap_endpoint_t}^{coap_session_t}^?^?^?^?^?^?^vI^?^?^?^?^v{coap_dtls_spsk_t=CC[6C]^?^v^?^v{coap_dtls_spsk_info_t={coap_bin_const_t=Q*}{coap_bin_const_t=Q*}}}IIIIIIQ^{coap_cache_entry_t}^SQ^vI{fd_set=[32i]}{fd_set=[32i]}{fd_set=[32i]}[64^{coap_socket_t}]ICCCCI}8^{coap_session_t=iiiIQQQ{coap_addr_hash_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{coap_sockaddr_un=C[27c]})}Si}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{coap_sockaddr_un=C[27c]})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{coap_sockaddr_un=C[27c]})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{coap_sockaddr_un=C[27c]})}[3{?=^?^?^?^?}]}^{coap_endpoint_t}^{coap_context_t}^vSCCi^{coap_queue_t}^{coap_lg_xmit_t}^{coap_lg_crcv_t}^{coap_lg_srcv_t}Q[8C]Q^{coap_pdu_t}QQQQQ{coap_dtls_cpsk_t=CCC[5C]^?^v*{coap_dtls_cpsk_info_t={coap_bin_const_t=Q*}{coap_bin_const_t=Q*}}}^{coap_bin_const_t}^{coap_bin_const_t}^{coap_bin_const_t}^v{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}SS{coap_fixed_point_t=SS}IIiIICCCCCCCCCCiIQ^{coap_bin_const_t}^{coap_bin_const_t}iii^{coap_bin_const_t}dddIddddCddI[32{?=SdC}]}16lw40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e1638_v24?0^{coap_context_t={coap_opt_filter_t=S[2S][6C]}^{coap_resource_t}^{coap_resource_t}^{coap_resource_t}^?Q^{coap_queue_t}^{coap_endpoint_t}^{coap_session_t}^?^?^?^?^?^?^vI^?^?^?^?^v{coap_dtls_spsk_t=CC[6C]^?^v^?^v{coap_dtls_spsk_info_t={coap_bin_const_t=Q*}{coap_bin_const_t=Q*}}}IIIIIIQ^{coap_cache_entry_t}^SQ^vI{fd_set=[32i]}{fd_set=[32i]}{fd_set=[32i]}[64^{coap_socket_t}]ICCCCI}8^{coap_session_t=iiiIQQQ{coap_addr_hash_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{coap_sockaddr_un=C[27c]})}Si}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{coap_sockaddr_un=C[27c]})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{coap_sockaddr_un=C[27c]})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{coap_sockaddr_un=C[27c]})}[3{?=^?^?^?^?}]}^{coap_endpoint_t}^{coap_context_t}^vSCCi^{coap_queue_t}^{coap_lg_xmit_t}^{coap_lg_crcv_t}^{coap_lg_srcv_t}Q[8C]Q^{coap_pdu_t}QQQQQ{coap_dtls_cpsk_t=CCC[5C]^?^v*{coap_dtls_cpsk_info_t={coap_bin_const_t=Q*}{coap_bin_const_t=Q*}}}^{coap_bin_const_t}^{coap_bin_const_t}^{coap_bin_const_t}^v{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}SS{coap_fixed_point_t=SS}IIiIICCCCCCCCCCiIQ^{coap_bin_const_t}^{coap_bin_const_t}iii^{coap_bin_const_t}dddIddddCddI[32{?=SdC}]}16ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_56_e8_32s40s48bs_e1638_v24?0^{coap_context_t={coap_opt_filter_t=S[2S][6C]}^{coap_resource_t}^{coap_resource_t}^{coap_resource_t}^?Q^{coap_queue_t}^{coap_endpoint_t}^{coap_session_t}^?^?^?^?^?^?^vI^?^?^?^?^v{coap_dtls_spsk_t=CC[6C]^?^v^?^v{coap_dtls_spsk_info_t={coap_bin_const_t=Q*}{coap_bin_const_t=Q*}}}IIIIIIQ^{coap_cache_entry_t}^SQ^vI{fd_set=[32i]}{fd_set=[32i]}{fd_set=[32i]}[64^{coap_socket_t}]ICCCCI}8^{coap_session_t=iiiIQQQ{coap_addr_hash_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{coap_sockaddr_un=C[27c]})}Si}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{coap_sockaddr_un=C[27c]})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{coap_sockaddr_un=C[27c]})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{coap_sockaddr_un=C[27c]})}[3{?=^?^?^?^?}]}^{coap_endpoint_t}^{coap_context_t}^vSCCi^{coap_queue_t}^{coap_lg_xmit_t}^{coap_lg_crcv_t}^{coap_lg_srcv_t}Q[8C]Q^{coap_pdu_t}QQQQQ{coap_dtls_cpsk_t=CCC[5C]^?^v*{coap_dtls_cpsk_info_t={coap_bin_const_t=Q*}{coap_bin_const_t=Q*}}}^{coap_bin_const_t}^{coap_bin_const_t}^{coap_bin_const_t}^v{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}SS{coap_fixed_point_t=SS}IIiIICCCCCCCCCCiIQ^{coap_bin_const_t}^{coap_bin_const_t}iii^{coap_bin_const_t}dddIddddCddI[32{?=SdC}]}16ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32w40w_e8_v16?0q8lw32l8w40l8
+ ___block_descriptor_57_e8_32bs40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_64_e8_32bs40w48w_e5_v8?0lw40l8w48l8s32l8
+ ___block_descriptor_64_e8_32bs40w48w_e8_v12?0B8lw40l8w48l8s32l8
+ ___block_descriptor_64_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_64_e8_32w40w_e5_v8?0lw32l8w40l8
+ ___block_descriptor_65_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_68_e8_32s40s48bs_e28_v24?0"NSData"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_71_e8_32s40s48s_e1275_v24?0"HAP2CoAPClient"8^{coap_session_t=iiiIQQQ{coap_addr_hash_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{coap_sockaddr_un=C[27c]})}Si}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{coap_sockaddr_un=C[27c]})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{coap_sockaddr_un=C[27c]})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{coap_sockaddr_un=C[27c]})}[3{?=^?^?^?^?}]}^{coap_endpoint_t}^{coap_context_t}^vSCCi^{coap_queue_t}^{coap_lg_xmit_t}^{coap_lg_crcv_t}^{coap_lg_srcv_t}Q[8C]Q^{coap_pdu_t}QQQQQ{coap_dtls_cpsk_t=CCC[5C]^?^v*{coap_dtls_cpsk_info_t={coap_bin_const_t=Q*}{coap_bin_const_t=Q*}}}^{coap_bin_const_t}^{coap_bin_const_t}^{coap_bin_const_t}^v{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}SS{coap_fixed_point_t=SS}IIiIICCCCCCCCCCiIQ^{coap_bin_const_t}^{coap_bin_const_t}iii^{coap_bin_const_t}dddIddddCddI[32{?=SdC}]}16ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40bs48bs56r64w_e5_v8?0lw64l8s40l8r56l8s32l8s48l8
+ ___block_descriptor_72_e8_32s40s48bs56r64w_e5_v8?0lw64l8s48l8s32l8s40l8r56l8
+ ___block_descriptor_72_e8_32s40s48s56w_e5_v8?0lw56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48w_e5_v8?0ls32l8w48l8s40l8
+ ___block_descriptor_76_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56r64r72r_e39_v32?0"<HAP2AccessoryPrivate>"8Q16^B24lr56l8s32l8s40l8r64l8s48l8r72l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e8_v12?0B8ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_81_e8_32s40s48s56s64s72s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_88_e8_32s40s48s56w_e28_v24?0"NSData"8"NSError"16ls32l8s40l8w56l8s48l8
+ ___swift_closure_destructor.242Tm
+ ___swift_memcpy24_8
+ _arc4random_uniform
+ _associated conformance So25HAPNetworkCredentialTypesVs10SetAlgebraSCSQ
+ _associated conformance So25HAPNetworkCredentialTypesVs10SetAlgebraSCs25ExpressibleByArrayLiteral
+ _associated conformance So25HAPNetworkCredentialTypesVs9OptionSetSCSY
+ _associated conformance So25HAPNetworkCredentialTypesVs9OptionSetSCs0E7Algebra
+ _b_ipv4
+ _bcst_cnt
+ _cache_ignore_options
+ _check_freshness
+ _check_token_size
+ _cid_track_counter
+ _coap_add_block_b_data
+ _coap_add_data
+ _coap_add_data_large_internal
+ _coap_add_option_internal
+ _coap_address_equals
+ _coap_block_build_body
+ _coap_block_check_lg_xmit_timeouts
+ _coap_block_delete_lg_crcv
+ _coap_block_delete_lg_srcv
+ _coap_block_delete_lg_xmit
+ _coap_block_new_lg_crcv
+ _coap_cache_derive_key_w_ignore
+ _coap_cancel_observe_lkd
+ _coap_check_code_lg_xmit
+ _coap_check_send_need_lg_crcv
+ _coap_check_update_token
+ _coap_client_delay_first
+ _coap_delete_cache_entry
+ _coap_delete_node_lkd
+ _coap_delete_observer_internal
+ _coap_delete_observer_request
+ _coap_digest_update
+ _coap_dtls_close
+ _coap_dtls_establish
+ _coap_dtls_send
+ _coap_encode_var_safe8
+ _coap_endpoint_str
+ _coap_find_lg_xmit_response
+ _coap_find_lg_xmit_response.empty
+ _coap_find_observer_cache_key
+ _coap_get_block_b
+ _coap_get_data_large
+ _coap_get_query
+ _coap_get_resource_from_uri_path_lkd
+ _coap_get_uri_path.hex
+ _coap_handle_event_lkd
+ _coap_handle_request_put_block
+ _coap_handle_request_send_block
+ _coap_handle_response_get_block
+ _coap_insert_option
+ _coap_io_process_with_fds_lkd
+ _coap_is_bcast
+ _coap_is_mcast
+ _coap_layers_coap
+ _coap_netif_close
+ _coap_netif_dgrm_write
+ _coap_notify_observers
+ _coap_opt_encode
+ _coap_option_check_repeatable
+ _coap_pdu_duplicate_lkd
+ _coap_pdu_parse_opt.outbuf
+ _coap_pdu_parse_opt_base
+ _coap_pdu_parse_opt_csm
+ _coap_print_ip_addr
+ _coap_print_wellknown_lkd
+ _coap_print_wellknown_lkd._rt_attributes
+ _coap_prng_default
+ _coap_remove_option
+ _coap_send_ack_lkd
+ _coap_send_internal
+ _coap_send_message_type_lkd
+ _coap_send_test_extended_token
+ _coap_session_apply_rtt_sample
+ _coap_session_disconnected_lkd
+ _coap_session_establish
+ _coap_session_max_pdu_size_lkd
+ _coap_session_release_lkd
+ _coap_session_send_ping_lkd
+ _coap_session_set_ack_timeout
+ _coap_session_set_max_retransmit
+ _coap_socket_connect_udp
+ _coap_socket_recv
+ _coap_split_uri_sub
+ _coap_startup.well_known
+ _coap_update_option
+ _coap_update_token
+ _coap_uri_scheme
+ _fls
+ _flsll
+ _free_wellknown_response
+ _hnd_get_wellknown_lkd
+ _is_unescaped_in_path
+ _kAccessoryDiscoveryRetryMaximumFailures
+ _kHAP2DNSSDErrorDomain
+ _kHAP2ResolverRetryLadder
+ _last_refresh
+ _localtime_r
+ _logCategory._hmf_once_t940
+ _logCategory._hmf_once_v941
+ _messageIsPing
+ _msg_code_string
+ _next_option_safe
+ _objc_release_x4
+ _random
+ _resource_uri_wellknown
+ _setup_block_b
+ _srandom
+ _strchr
+ _strcpy
+ _strstr
+ _symbolic Sd
+ _symbolic SdSg
+ _symbolic _____ 7CoreHAP24HAPSpakePairSetupSessionC8ParkedM533_FFB3B66732484B0775DD4AE3FA14FD0DLLV
+ _symbolic _____ So25HAPNetworkCredentialTypesV
+ _symbolic _____Sg 7CoreHAP24HAPSpakePairSetupSessionC8ParkedM533_FFB3B66732484B0775DD4AE3FA14FD0DLLV
+ _symbolic _____Sg So25HAPNetworkCredentialTypesV
+ _track_echo
+ _track_fetch_observe
+ _type_layout_string 7CoreHAP24HAPSpakePairSetupSessionC8ParkedM533_FFB3B66732484B0775DD4AE3FA14FD0DLLV
+ _type_layout_string So29HAPCHMThreadConnectivityStateV
+ _update_received_blocks
+ _write_char
- -[HAP2AccessoryServer _runLostDiscoveryAdvertisementSideEffectsWithWillSleep:]
- -[HAPAccessoryServer pairSetupM1ToM4Completed]
- -[HAPAccessoryServer pairSetupM1ToM4DurationMS]
- -[HAPAccessoryServer pairSetupM1ToM4Error]
- -[HAPAccessoryServer pairSetupM5ToM6Completed]
- -[HAPAccessoryServer pairSetupM5ToM6DurationMS]
- -[HAPAccessoryServer pairSetupM5ToM6Error]
- -[HAPAccessoryServer setPairSetupM1ToM4Completed:]
- -[HAPAccessoryServer setPairSetupM1ToM4DurationMS:]
- -[HAPAccessoryServer setPairSetupM1ToM4Error:]
- -[HAPAccessoryServer setPairSetupM5ToM6Completed:]
- -[HAPAccessoryServer setPairSetupM5ToM6DurationMS:]
- -[HAPAccessoryServer setPairSetupM5ToM6Error:]
- -[HAPAccessoryServer setTokenAuthCompleted:]
- -[HAPAccessoryServer setTokenAuthDurationMS:]
- -[HAPAccessoryServer setTokenAuthError:]
- -[HAPAccessoryServer tokenAuthCompleted]
- -[HAPAccessoryServer tokenAuthDurationMS]
- -[HAPAccessoryServer tokenAuthError]
- -[HAPAccessoryServerBrowser pairSetupSession:pairSetupType:features:pairVerifyTLK:error:]
- -[HAPAccessoryServerBrowserNFC _reapPrewarmServerIfNeeded]
- -[HAPAccessoryServerHAP2Adapter accessoryServer:didUpdateLocalEndpoints:]
- -[HAPAccessoryServerIP ensureNetworkMonitor]
- -[HAPAccessoryServerIP networkMonitor]
- -[HAPAccessoryServerNFC _captureProxPairSetupPhaseTimingsAsOf:pairSetupReachedM6:phaseError:]
- -[HAPAccessoryServerNFC _resetProxPairSetupPhaseOutputs]
- -[HAPAccessoryServerNFC _resetTokenAuthOutputs]
- -[HAPCameraBufferActivityCommandRequest initWithStart:duration:activity:]
- -[HAPCameraVideoStreamCapabilities initWithIdentifier:quality:width:height:framesPerSecond:averageBitrate:peakBitrate:]
- -[HAPSystemKeychainStore allLegacyAccessoryPairingKeys]
- -[HAPSystemKeychainStore deletePairingKeysForAccessory:error:]
- -[HAPSystemKeychainStore readAccessoryPairingKeyForAccessory:error:]
- -[HMFPairingIdentity(HAPKeyStore) isControllerKey]
- GCC_except_table10019
- GCC_except_table10097
- GCC_except_table10099
- GCC_except_table10101
- GCC_except_table10103
- GCC_except_table10105
- GCC_except_table10107
- GCC_except_table10109
- GCC_except_table10115
- GCC_except_table10117
- GCC_except_table10120
- GCC_except_table10122
- GCC_except_table10124
- GCC_except_table10131
- GCC_except_table10137
- GCC_except_table10142
- GCC_except_table10145
- GCC_except_table10150
- GCC_except_table10155
- GCC_except_table10158
- GCC_except_table10161
- GCC_except_table10187
- GCC_except_table10190
- GCC_except_table10191
- GCC_except_table10230
- GCC_except_table10231
- GCC_except_table10232
- GCC_except_table10234
- GCC_except_table10237
- GCC_except_table10238
- GCC_except_table10239
- GCC_except_table10242
- GCC_except_table10244
- GCC_except_table10248
- GCC_except_table10253
- GCC_except_table10304
- GCC_except_table10311
- GCC_except_table10419
- GCC_except_table10421
- GCC_except_table10426
- GCC_except_table10428
- GCC_except_table10430
- GCC_except_table10432
- GCC_except_table10433
- GCC_except_table10440
- GCC_except_table10442
- GCC_except_table10443
- GCC_except_table1131
- GCC_except_table1133
- GCC_except_table1200
- GCC_except_table1202
- GCC_except_table1204
- GCC_except_table1746
- GCC_except_table1751
- GCC_except_table1753
- GCC_except_table1767
- GCC_except_table1779
- GCC_except_table1781
- GCC_except_table1783
- GCC_except_table1785
- GCC_except_table1915
- GCC_except_table1919
- GCC_except_table1921
- GCC_except_table2123
- GCC_except_table2339
- GCC_except_table2341
- GCC_except_table2346
- GCC_except_table2352
- GCC_except_table2354
- GCC_except_table2360
- GCC_except_table2362
- GCC_except_table2366
- GCC_except_table2374
- GCC_except_table2378
- GCC_except_table2384
- GCC_except_table2386
- GCC_except_table2388
- GCC_except_table2390
- GCC_except_table2396
- GCC_except_table2400
- GCC_except_table2408
- GCC_except_table2410
- GCC_except_table2423
- GCC_except_table2431
- GCC_except_table2438
- GCC_except_table2442
- GCC_except_table2446
- GCC_except_table2487
- GCC_except_table2606
- GCC_except_table2610
- GCC_except_table2611
- GCC_except_table2613
- GCC_except_table2615
- GCC_except_table2627
- GCC_except_table2632
- GCC_except_table2639
- GCC_except_table2641
- GCC_except_table2644
- GCC_except_table2661
- GCC_except_table2671
- GCC_except_table2673
- GCC_except_table2675
- GCC_except_table2680
- GCC_except_table2683
- GCC_except_table2688
- GCC_except_table2691
- GCC_except_table2695
- GCC_except_table2697
- GCC_except_table2703
- GCC_except_table2705
- GCC_except_table2707
- GCC_except_table2711
- GCC_except_table2715
- GCC_except_table2723
- GCC_except_table2734
- GCC_except_table2777
- GCC_except_table2778
- GCC_except_table2779
- GCC_except_table2781
- GCC_except_table2782
- GCC_except_table2783
- GCC_except_table2785
- GCC_except_table2789
- GCC_except_table2790
- GCC_except_table2816
- GCC_except_table2820
- GCC_except_table2824
- GCC_except_table2988
- GCC_except_table2995
- GCC_except_table2999
- GCC_except_table3003
- GCC_except_table3007
- GCC_except_table3010
- GCC_except_table3012
- GCC_except_table3014
- GCC_except_table3017
- GCC_except_table3023
- GCC_except_table3025
- GCC_except_table3028
- GCC_except_table3029
- GCC_except_table3031
- GCC_except_table3132
- GCC_except_table3140
- GCC_except_table3141
- GCC_except_table3142
- GCC_except_table3143
- GCC_except_table3144
- GCC_except_table3145
- GCC_except_table3160
- GCC_except_table3174
- GCC_except_table3254
- GCC_except_table3266
- GCC_except_table3471
- GCC_except_table3480
- GCC_except_table3497
- GCC_except_table3531
- GCC_except_table3547
- GCC_except_table3549
- GCC_except_table3561
- GCC_except_table3568
- GCC_except_table3590
- GCC_except_table3604
- GCC_except_table3605
- GCC_except_table3606
- GCC_except_table3609
- GCC_except_table3615
- GCC_except_table3622
- GCC_except_table3625
- GCC_except_table3630
- GCC_except_table3635
- GCC_except_table3640
- GCC_except_table3680
- GCC_except_table3697
- GCC_except_table3700
- GCC_except_table3705
- GCC_except_table3707
- GCC_except_table3723
- GCC_except_table3737
- GCC_except_table3739
- GCC_except_table3743
- GCC_except_table3751
- GCC_except_table3759
- GCC_except_table3823
- GCC_except_table3830
- GCC_except_table3832
- GCC_except_table3833
- GCC_except_table3856
- GCC_except_table3876
- GCC_except_table4104
- GCC_except_table4179
- GCC_except_table4186
- GCC_except_table4190
- GCC_except_table4192
- GCC_except_table4194
- GCC_except_table4196
- GCC_except_table4200
- GCC_except_table4203
- GCC_except_table4209
- GCC_except_table4220
- GCC_except_table4222
- GCC_except_table4223
- GCC_except_table4225
- GCC_except_table4228
- GCC_except_table4230
- GCC_except_table4231
- GCC_except_table4233
- GCC_except_table4234
- GCC_except_table4236
- GCC_except_table4243
- GCC_except_table4253
- GCC_except_table4256
- GCC_except_table4267
- GCC_except_table4268
- GCC_except_table4270
- GCC_except_table4272
- GCC_except_table4275
- GCC_except_table4279
- GCC_except_table4281
- GCC_except_table4284
- GCC_except_table4287
- GCC_except_table4299
- GCC_except_table4301
- GCC_except_table4305
- GCC_except_table4309
- GCC_except_table4313
- GCC_except_table4318
- GCC_except_table4331
- GCC_except_table4350
- GCC_except_table4373
- GCC_except_table4379
- GCC_except_table4383
- GCC_except_table4387
- GCC_except_table4389
- GCC_except_table4392
- GCC_except_table4394
- GCC_except_table4396
- GCC_except_table4403
- GCC_except_table4404
- GCC_except_table4405
- GCC_except_table4406
- GCC_except_table4407
- GCC_except_table4409
- GCC_except_table4410
- GCC_except_table4411
- GCC_except_table4412
- GCC_except_table4499
- GCC_except_table4500
- GCC_except_table4501
- GCC_except_table4502
- GCC_except_table4503
- GCC_except_table4504
- GCC_except_table4506
- GCC_except_table4507
- GCC_except_table4508
- GCC_except_table4509
- GCC_except_table4510
- GCC_except_table4511
- GCC_except_table4512
- GCC_except_table4551
- GCC_except_table4578
- GCC_except_table4708
- GCC_except_table4719
- GCC_except_table4740
- GCC_except_table4748
- GCC_except_table4759
- GCC_except_table4781
- GCC_except_table4789
- GCC_except_table4795
- GCC_except_table4797
- GCC_except_table4799
- GCC_except_table4810
- GCC_except_table4843
- GCC_except_table4846
- GCC_except_table4847
- GCC_except_table4853
- GCC_except_table4855
- GCC_except_table4861
- GCC_except_table4862
- GCC_except_table4867
- GCC_except_table4868
- GCC_except_table4874
- GCC_except_table4883
- GCC_except_table4884
- GCC_except_table4885
- GCC_except_table4886
- GCC_except_table4887
- GCC_except_table4888
- GCC_except_table4889
- GCC_except_table4895
- GCC_except_table4902
- GCC_except_table4906
- GCC_except_table4907
- GCC_except_table4921
- GCC_except_table4954
- GCC_except_table4955
- GCC_except_table4957
- GCC_except_table4958
- GCC_except_table4961
- GCC_except_table4962
- GCC_except_table4977
- GCC_except_table4999
- GCC_except_table5019
- GCC_except_table5029
- GCC_except_table5031
- GCC_except_table5097
- GCC_except_table5101
- GCC_except_table5102
- GCC_except_table5104
- GCC_except_table5106
- GCC_except_table5109
- GCC_except_table5112
- GCC_except_table5115
- GCC_except_table5118
- GCC_except_table5124
- GCC_except_table5127
- GCC_except_table5130
- GCC_except_table5148
- GCC_except_table5153
- GCC_except_table5157
- GCC_except_table5174
- GCC_except_table5192
- GCC_except_table5193
- GCC_except_table5196
- GCC_except_table5197
- GCC_except_table5215
- GCC_except_table5217
- GCC_except_table5219
- GCC_except_table5220
- GCC_except_table5223
- GCC_except_table5229
- GCC_except_table5232
- GCC_except_table5241
- GCC_except_table5243
- GCC_except_table5245
- GCC_except_table5248
- GCC_except_table5259
- GCC_except_table5270
- GCC_except_table5272
- GCC_except_table5283
- GCC_except_table5285
- GCC_except_table5287
- GCC_except_table5293
- GCC_except_table547
- GCC_except_table557
- GCC_except_table5575
- GCC_except_table5598
- GCC_except_table5602
- GCC_except_table5620
- GCC_except_table5626
- GCC_except_table5640
- GCC_except_table5654
- GCC_except_table5658
- GCC_except_table571
- GCC_except_table579
- GCC_except_table5802
- GCC_except_table608
- GCC_except_table615
- GCC_except_table6260
- GCC_except_table6269
- GCC_except_table627
- GCC_except_table6270
- GCC_except_table628
- GCC_except_table6280
- GCC_except_table630
- GCC_except_table6322
- GCC_except_table6325
- GCC_except_table6326
- GCC_except_table6327
- GCC_except_table6328
- GCC_except_table633
- GCC_except_table636
- GCC_except_table646
- GCC_except_table648
- GCC_except_table6493
- GCC_except_table6494
- GCC_except_table6495
- GCC_except_table6496
- GCC_except_table6497
- GCC_except_table6498
- GCC_except_table6499
- GCC_except_table6500
- GCC_except_table6502
- GCC_except_table652
- GCC_except_table6523
- GCC_except_table6534
- GCC_except_table6536
- GCC_except_table6541
- GCC_except_table6544
- GCC_except_table6547
- GCC_except_table6551
- GCC_except_table6555
- GCC_except_table659
- GCC_except_table662
- GCC_except_table696
- GCC_except_table706
- GCC_except_table7106
- GCC_except_table7107
- GCC_except_table7126
- GCC_except_table7136
- GCC_except_table7139
- GCC_except_table714
- GCC_except_table7144
- GCC_except_table7147
- GCC_except_table7152
- GCC_except_table741
- GCC_except_table7421
- GCC_except_table7425
- GCC_except_table745
- GCC_except_table748
- GCC_except_table7485
- GCC_except_table7489
- GCC_except_table7491
- GCC_except_table7493
- GCC_except_table750
- GCC_except_table756
- GCC_except_table758
- GCC_except_table7708
- GCC_except_table771
- GCC_except_table7716
- GCC_except_table7718
- GCC_except_table7722
- GCC_except_table7728
- GCC_except_table7741
- GCC_except_table775
- GCC_except_table7759
- GCC_except_table7765
- GCC_except_table7779
- GCC_except_table7783
- GCC_except_table7788
- GCC_except_table779
- GCC_except_table7790
- GCC_except_table7794
- GCC_except_table7796
- GCC_except_table789
- GCC_except_table7890
- GCC_except_table7897
- GCC_except_table790
- GCC_except_table7904
- GCC_except_table7911
- GCC_except_table7927
- GCC_except_table795
- GCC_except_table7962
- GCC_except_table7963
- GCC_except_table7964
- GCC_except_table798
- GCC_except_table7984
- GCC_except_table7996
- GCC_except_table7999
- GCC_except_table8004
- GCC_except_table8006
- GCC_except_table801
- GCC_except_table8020
- GCC_except_table806
- GCC_except_table810
- GCC_except_table816
- GCC_except_table817
- GCC_except_table822
- GCC_except_table823
- GCC_except_table8244
- GCC_except_table8257
- GCC_except_table8262
- GCC_except_table8265
- GCC_except_table8266
- GCC_except_table8268
- GCC_except_table8269
- GCC_except_table8271
- GCC_except_table8301
- GCC_except_table8323
- GCC_except_table8327
- GCC_except_table8331
- GCC_except_table8336
- GCC_except_table8340
- GCC_except_table8344
- GCC_except_table8348
- GCC_except_table8352
- GCC_except_table8360
- GCC_except_table8362
- GCC_except_table8364
- GCC_except_table8390
- GCC_except_table8401
- GCC_except_table851
- GCC_except_table8539
- GCC_except_table8574
- GCC_except_table858
- GCC_except_table866
- GCC_except_table8664
- GCC_except_table867
- GCC_except_table8735
- GCC_except_table8748
- GCC_except_table8749
- GCC_except_table8754
- GCC_except_table8755
- GCC_except_table8762
- GCC_except_table8774
- GCC_except_table8780
- GCC_except_table8788
- GCC_except_table8794
- GCC_except_table8808
- GCC_except_table8811
- GCC_except_table8812
- GCC_except_table8817
- GCC_except_table8820
- GCC_except_table8830
- GCC_except_table8844
- GCC_except_table8857
- GCC_except_table8866
- GCC_except_table8868
- GCC_except_table8872
- GCC_except_table8904
- GCC_except_table8905
- GCC_except_table8910
- GCC_except_table8914
- GCC_except_table8915
- GCC_except_table8918
- GCC_except_table8924
- GCC_except_table8928
- GCC_except_table8932
- GCC_except_table8934
- GCC_except_table8936
- GCC_except_table8940
- GCC_except_table895
- GCC_except_table9059
- GCC_except_table9096
- GCC_except_table9154
- GCC_except_table9157
- GCC_except_table9164
- GCC_except_table9170
- GCC_except_table9177
- GCC_except_table9178
- GCC_except_table918
- GCC_except_table9195
- GCC_except_table9200
- GCC_except_table9201
- GCC_except_table9250
- GCC_except_table9251
- GCC_except_table9253
- GCC_except_table9256
- GCC_except_table9283
- GCC_except_table9284
- GCC_except_table9289
- GCC_except_table9309
- GCC_except_table9327
- GCC_except_table9328
- GCC_except_table9329
- GCC_except_table9334
- GCC_except_table9335
- GCC_except_table9337
- GCC_except_table9339
- GCC_except_table9340
- GCC_except_table9342
- GCC_except_table9343
- GCC_except_table9347
- GCC_except_table9348
- GCC_except_table9360
- GCC_except_table9362
- GCC_except_table9367
- GCC_except_table937
- GCC_except_table9372
- GCC_except_table9373
- GCC_except_table9374
- GCC_except_table9390
- GCC_except_table9392
- GCC_except_table9411
- GCC_except_table9429
- GCC_except_table9430
- GCC_except_table9435
- GCC_except_table9452
- GCC_except_table9456
- GCC_except_table9458
- GCC_except_table9460
- GCC_except_table9485
- GCC_except_table9487
- GCC_except_table961
- GCC_except_table965
- GCC_except_table9679
- GCC_except_table9742
- GCC_except_table9774
- GCC_except_table9777
- GCC_except_table979
- GCC_except_table984
- GCC_except_table9944
- GCC_except_table9982
- _OBJC_CLASS_$_HMFNetMonitor
- _OBJC_CLASS_$_NSCondition
- _OBJC_IVAR_$_HAP2AccessoryDNSResolver._immediateRetrySpent
- _OBJC_IVAR_$_HAPAccessoryServer._pairSetupM1ToM4Completed
- _OBJC_IVAR_$_HAPAccessoryServer._pairSetupM1ToM4DurationMS
- _OBJC_IVAR_$_HAPAccessoryServer._pairSetupM1ToM4Error
- _OBJC_IVAR_$_HAPAccessoryServer._pairSetupM5ToM6Completed
- _OBJC_IVAR_$_HAPAccessoryServer._pairSetupM5ToM6DurationMS
- _OBJC_IVAR_$_HAPAccessoryServer._pairSetupM5ToM6Error
- _OBJC_IVAR_$_HAPAccessoryServer._tokenAuthCompleted
- _OBJC_IVAR_$_HAPAccessoryServer._tokenAuthDurationMS
- _OBJC_IVAR_$_HAPAccessoryServer._tokenAuthError
- _OBJC_IVAR_$_HAPAccessoryServerIP._networkMonitor
- __OBJC_$_CATEGORY_HMFPairingIdentity_$_HAPKeyStore
- __OBJC_$_CATEGORY_INSTANCE_METHODS_HMFPairingIdentity_$_HAPKeyStore
- __OBJC_$_PROP_LIST_HMFPairingIdentity_$_HAPKeyStore
- ___43-[HAPAccessoryServerNFC _startHAPPairSetup]_block_invoke
- ___43-[HAPAccessoryServerNFC _startHAPPairSetup]_block_invoke_2
- ___43-[HAPAccessoryServerNFC _startHAPPairSetup]_block_invoke_3
- ___50-[HAP2AccessoryDNSResolver _handlePipelineUpdate:]_block_invoke_2
- ___66-[HAP2AccessoryServerTransportCoAP readLocalEndpointsWithHandler:]_block_invoke_2
- ___66-[HAP2AccessoryServerTransportCoAP readLocalEndpointsWithHandler:]_block_invoke_3
- ___82-[HAP2AccessoryServer(Paired) _handleDiscoveredAccessories:withCompletionHandler:]_block_invoke_3
- ___83-[HAP2AccessoryServer(PairedInternal) keepAliveListenerDidCompleteIPPortPairCheck:]_block_invoke
- ___83-[HAP2AccessoryServer(PairedInternal) keepAliveListenerDidCompleteIPPortPairCheck:]_block_invoke_2
- ___block_descriptor_32_e716_v24?0"HAP2CoAPClient"8^{coap_session_t=CCCIII{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}}^{coap_endpoint_t}^{coap_context_t}^vSCi^{coap_queue_t}Q[8C]Q^{coap_pdu_t}QQQQQ*Q*Q^vI{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}IidddIddddCddI[32{?=SdC}]}16l
- ___block_descriptor_40_e8_32w_e22_v16?0"NSDictionary"8lw32l8
- ___block_descriptor_48_e716_v24?0"HAP2CoAPClient"8^{coap_session_t=CCCIII{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}}^{coap_endpoint_t}^{coap_context_t}^vSCi^{coap_queue_t}Q[8C]Q^{coap_pdu_t}QQQQQ*Q*Q^vI{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}IidddIddddCddI[32{?=SdC}]}16l
- ___block_descriptor_48_e8_32bs40w_e862_v24?0^{coap_context_t=[6S]^{coap_resource_t}^{coap_resource_t}^{coap_async_state_t}Q^{coap_queue_t}^{coap_endpoint_t}^{coap_session_t}^?^?^?^?^?^?^?^?^?^?^v*Q*QIIIII^v}8^{coap_session_t=CCCIII{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}}^{coap_endpoint_t}^{coap_context_t}^vSCi^{coap_queue_t}Q[8C]Q^{coap_pdu_t}QQQQQ*Q*Q^vI{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}IidddIddddCddI[32{?=SdC}]}16lw40l8s32l8
- ___block_descriptor_48_e8_32s40bs_e862_v24?0^{coap_context_t=[6S]^{coap_resource_t}^{coap_resource_t}^{coap_async_state_t}Q^{coap_queue_t}^{coap_endpoint_t}^{coap_session_t}^?^?^?^?^?^?^?^?^?^?^v*Q*QIIIII^v}8^{coap_session_t=CCCIII{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}}^{coap_endpoint_t}^{coap_context_t}^vSCi^{coap_queue_t}Q[8C]Q^{coap_pdu_t}QQQQQ*Q*Q^vI{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}IidddIddddCddI[32{?=SdC}]}16ls32l8s40l8
- ___block_descriptor_48_e8_32w_e8_v12?0B8lw32l8
- ___block_descriptor_56_e8_32s40s48bs_e862_v24?0^{coap_context_t=[6S]^{coap_resource_t}^{coap_resource_t}^{coap_async_state_t}Q^{coap_queue_t}^{coap_endpoint_t}^{coap_session_t}^?^?^?^?^?^?^?^?^?^?^v*Q*QIIIII^v}8^{coap_session_t=CCCIII{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}}^{coap_endpoint_t}^{coap_context_t}^vSCi^{coap_queue_t}Q[8C]Q^{coap_pdu_t}QQQQQ*Q*Q^vI{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}IidddIddddCddI[32{?=SdC}]}16ls32l8s48l8s40l8
- ___block_descriptor_60_e8_32s40bs_e28_v24?0"NSData"8"NSError"16ls32l8s40l8
- ___block_descriptor_60_e8_32s40bs_e5_v8?0ls32l8s40l8
- ___block_descriptor_71_e8_32s40s48s_e716_v24?0"HAP2CoAPClient"8^{coap_session_t=CCCIII{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}}^{coap_endpoint_t}^{coap_context_t}^vSCi^{coap_queue_t}Q[8C]Q^{coap_pdu_t}QQQQQ*Q*Q^vI{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}IidddIddddCddI[32{?=SdC}]}16ls32l8s40l8s48l8
- ___swift_closure_destructor.198Tm
- _accept
- _arc4random_buf
- _coapNetworkRead
- _coap_add_data_after
- _coap_add_option
- _coap_cancel_session_messages
- _coap_delete_node
- _coap_get_block
- _coap_get_context_server_hint
- _coap_get_context_server_psk
- _coap_get_data
- _coap_get_log_level
- _coap_get_resource_from_uri_path
- _coap_get_session_client_psk
- _coap_handle_event
- _coap_network_read
- _coap_network_send
- _coap_pdu_parse_header
- _coap_pdu_parse_header_size
- _coap_pdu_parse_opt
- _coap_print_wellknown
- _coap_print_wellknown._rt_attributes
- _coap_send
- _coap_send_message_type
- _coap_session_disconnected
- _coap_session_max_pdu_size
- _coap_session_release
- _coap_session_send_csm
- _coap_session_send_ping
- _coap_session_write
- _coap_set_log_level
- _coap_touch_observer
- _coap_wellknown_response
- _getsockopt
- _logCategory._hmf_once_t938
- _logCategory._hmf_once_v939
- _no_response
- _perror
- _symbolic So11NSConditionC
- _type_layout_string So15HAPFeatureFlagsV
CStrings:
+ "   %s: mid=0x%04x: mcast response delayed for %u.%03u secs\n"
+ "   %s: mid=0x%04x: response dropped\n"
+ "!1"
+ "!Aq\xa1"
+ "%.*s "
+ "%.*s URI scheme unknown\n"
+ "%@ Backoff timer fired with no attribute database — requesting another read"
+ "%@ Failed to merge discovered services for accessory %lu"
+ "%@ Giving up on attribute database read after %lu attempts"
+ "%@ HDS-over-TCP peer selected: %s from %s thread=%{BOOL}d (%{private}@)"
+ "%@ Ignoring request to identify an already paired accessory"
+ "%@ NLM Probe: Transport %lu not yet accepted; not probing"
+ "%@ NLM keep-alive listener active with an attribute database, skipping reachability client"
+ "%@ NLM: Cannot hand over registered transport endpoints, transport missing or unsupported"
+ "%@ Scheduling attribute database re-read after failed discovery"
+ "%s\n"
+ "%s:%d"
+ "%skc=0x"
+ "%skid=0x"
+ "%spIV=0x"
+ "%u/%c/BERT"
+ "%u/%c/BERT(%zu)"
+ "%{private}@ Restored the transport delegate"
+ "(resource_param.length + 1) <= query_filter->length"
+ "*  %s: netif: failed to read %zd bytes (%s)\n"
+ "*  %s: netif: failed to read %zd bytes (%s) state %d\n"
+ "*  %s: netif: failed to send %zd bytes (%s) state %d\n"
+ "*  %s: netif: recv %4zd bytes\n"
+ "*  %s: netif: sent %4zd bytes\n"
+ "*  %s: netif: sent %4zd of %4zd bytes\n"
+ "**  %s: mid=0x%04x: already in-use - dropped\n"
+ "** %s: coap_add_data_large: COAP_BLOCK_USE_LIBCOAP not enabled\n"
+ "** %s: coap_cancel_observe: COAP_BLOCK_USE_LIBCOAP not enabled\n"
+ "** %s: coap_socket_recv: %s\n"
+ "** %s: coap_socket_recv: ICMP: %s\n"
+ "** %s: large body receive internal issue\n"
+ "** %s: lg_crcv %p initialized - stateless token xxxx%012llx\n"
+ "** %s: lg_crcv %p released\n"
+ "** %s: lg_srcv %p initialized\n"
+ "** %s: lg_srcv %p released\n"
+ "** %s: lg_xmit %p initialized\n"
+ "** %s: lg_xmit %p released\n"
+ "** %s: mid=0x%04x: added to retransmit queue (%ums)\n"
+ "** %s: mid=0x%04x: delayed\n"
+ "** %s: mid=0x%04x: give up after %d attempts\n"
+ "** %s: mid=0x%04x: mcast delayed transmission\n"
+ "** %s: mid=0x%04x: not transmitted after disconnect\n"
+ "** %s: mid=0x%04x: removed (1)\n"
+ "** %s: mid=0x%04x: removed (2)\n"
+ "** %s: mid=0x%04x: removed (3)\n"
+ "** %s: mid=0x%04x: removed (4)\n"
+ "** %s: mid=0x%04x: removed (6)\n"
+ "** %s: mid=0x%04x: retransmission #%d (next %ums)\n"
+ "** %s: mid=0x%04x: transmitted after delay\n"
+ "** %s: timeout waiting for CSM response\n"
+ "** %s: timeout waiting for first response\n"
+ "***%s: CID: New Client Session\n"
+ "***%s: CID: Old Client Session\n"
+ "***%s: session %p: closed\n"
+ "***%s: session %p: created outgoing session\n"
+ "***%s: session %p: duplicate - already exists\n"
+ "***%s: session %p: new incoming session\n"
+ "***%s: session ICMP issue (%s)\n"
+ "***%s: session ack_random_factor set to %u.%03u\n"
+ "***%s: session ack_timeout set to %u.%03u\n"
+ "***%s: session disconnected (%s)\n"
+ "***%s: session max_retransmit set to %u\n"
+ "***EVENT: %s\n"
+ "*opt == COAP_PAYLOAD_START"
+ "*optp"
+ ".%03u"
+ ".well-known/core: truncating data length to %zu from %zu\n"
+ "00000279-0000-1000-8000-0026BB765291"
+ "00000330-0000-1000-8000-0026BB765291"
+ "<HAPCameraBufferActivityCommandRequest start=%@, duration=%@, activity=%@, reason=%@>"
+ "<HAPCameraVideoStreamCapabilities identifier=%@, quality=%@, width=%@, height=%@, framesPerSecond=%@, averageBitrate=%@, peakBitrate=%@, keyFrameInterval=%@, videoCodec=%@>"
+ "<HAPErrorEntry errorCode=%@, manufacturerErrorInfo=%@>"
+ "<HAPErrorStatus errorEntry=%@>"
+ "<HAPErrorStatusCodeWrapper value=%@>"
+ "<HAPIPAddressVersionWrapper value=%@>"
+ "<HAPTLVSessionTransportEndpointAddress IPAddressVersion=%@, IPAddress=%@, port=%@>"
+ "<HAPTLVSessionTransportEndpointEntry transportType=%@, endpointAddress=%@>"
+ "<HAPTLVSessionTransportEndpointList entries=%@>"
+ "<libcoap> Unhandled log level (%u) for message: %{private}s"
+ "A pairing is in flight on the detected NFC server; keeping its reader session"
+ "Accessory is already in a home and could not be replaced; reporting already-paired"
+ "Alrt"
+ "Bad Response"
+ "Block-Wise-Transfer"
+ "COAP_EVENT_BAD_PACKET"
+ "COAP_EVENT_KEEPALIVE_FAILURE"
+ "COAP_EVENT_MSG_RETRANSMITTED"
+ "COAP_EVENT_OSCORE_DECODE_ERROR"
+ "COAP_EVENT_OSCORE_DECRYPTION_FAILURE"
+ "COAP_EVENT_OSCORE_INTERNAL_ERROR"
+ "COAP_EVENT_OSCORE_NOT_ENABLED"
+ "COAP_EVENT_OSCORE_NO_PROTECTED_PAYLOAD"
+ "COAP_EVENT_OSCORE_NO_SECURITY"
+ "COAP_EVENT_PARTIAL_BLOCK"
+ "COAP_EVENT_SERVER_SESSION_DEL"
+ "COAP_EVENT_SERVER_SESSION_NEW"
+ "COAP_EVENT_SESSION_CLOSED"
+ "COAP_EVENT_SESSION_CONNECTED"
+ "COAP_EVENT_SESSION_FAILED"
+ "COAP_EVENT_WS_CLOSED"
+ "COAP_EVENT_WS_CONNECTED"
+ "COAP_EVENT_WS_PACKET_SIZE"
+ "COAP_EVENT_XMIT_BLOCK_FAIL"
+ "COAP_NACK_BAD_RESPONSE"
+ "COAP_NACK_ICMP_ISSUE"
+ "COAP_NACK_NOT_DELIVERABLE"
+ "COAP_NACK_RST"
+ "COAP_NACK_TLS_FAILED"
+ "COAP_NACK_TLS_LAYER_FAILED"
+ "COAP_NACK_TOO_MANY_RETRIES"
+ "COAP_NACK_WS_FAILED"
+ "COAP_NACK_WS_LAYER_FAILED"
+ "Changing blocksize during request invalid"
+ "Client app version of updated PDU\n"
+ "Client app version of updated PDU (3)\n"
+ "Conflict"
+ "Content-Format mismatch"
+ "Content-Format option mismatch\n"
+ "Crit"
+ "DTLS"
+ "Data body updated during receipt - new request started\n"
+ "Debg"
+ "Deferring network credential fetch until commit"
+ "Delegate does not support accessoryServer:pairVerifyTLKWithError:"
+ "Dropping exchange data from a pair-setup session that is no longer current"
+ "Dropping existing-accessory check result after pair-setup teardown"
+ "Duplicate request with mid=0x%04x - not processed\n"
+ "Echo"
+ "Emrg"
+ "Err "
+ "Extended Token requested size support not available\n"
+ "Extended Token support available\n"
+ "Extended Token support not available\n"
+ "Extended-Token-Length"
+ "Failed to drain wakeup pipe: %d"
+ "Failed to remove existing pairing key with error domain=%{public}@, code=%ld"
+ "Failed to run coap_io_process_with_fds"
+ "Failed to update keychain item to set invisible with error: %@"
+ "Failed to update keychain item to set invisible with error: %d"
+ "Failed to update token\n"
+ "Failing HAP Browser instantiation - nil delegate"
+ "Fetching Thread credentials for M5"
+ "Fetching WiFi credentials for M5"
+ "HAP2DNSSDErrorDomain"
+ "HAPErrorStatusCodeAudioFailure"
+ "HAPErrorStatusCodeBulbFailure"
+ "HAPErrorStatusCodeCalibrationError"
+ "HAPErrorStatusCodeConnectivityFailure"
+ "HAPErrorStatusCodeCoolingFailure"
+ "HAPErrorStatusCodeDeviceDamaged"
+ "HAPErrorStatusCodeDeviceOverheating"
+ "HAPErrorStatusCodeExcessiveBatteryDrain"
+ "HAPErrorStatusCodeFreezeRisk"
+ "HAPErrorStatusCodeHeatingFailure"
+ "HAPErrorStatusCodeJammed"
+ "HAPErrorStatusCodePowerInstability"
+ "HAPErrorStatusCodeSafetyTemperatureExceeded"
+ "HAPErrorStatusCodeSensorFailure"
+ "HAPErrorStatusCodeSuddenTemperatureChange"
+ "HAPIPAddressVersionIPv4"
+ "HAPIPAddressVersionIPv6"
+ "Hop Limit Reached"
+ "Hop-Limit"
+ "Ignoring pending-commit notice from a pair-setup session that is no longer current"
+ "Ignoring re-arm request; a pairing attempt is still in flight"
+ "Ignoring stop from a pair-setup session that is no longer current (%{public}@ %ld)"
+ "Illegal block requested (%d > last = %zu)\n"
+ "Info"
+ "Invalid Hop Limit\n"
+ "Invalid multicast packet received RFC7252 8.1\n"
+ "M4: accessory presented no MFi software token — prompting uncertified"
+ "M5 network credentials: threadRequired=%{bool,public}d threadBestEffort=%{bool,public}d wifiRequired=%{bool,public}d wifi=%{public}s thread=%{public}s waited=%{public}ldms fetchAge=%{public}ldms -> %{public}s"
+ "M5 network-credential gate changed after the fetches started"
+ "M5 waiting up to %{public}ldms for network credentials"
+ "M5: owner ECDSA public key is not a valid P-256 raw key (%ld bytes), failing pair-setup"
+ "Memory issue"
+ "Missing block 0"
+ "Missing interim block"
+ "NFC server finished pairing; releasing its claim on the reader session"
+ "NFC server started pairing; its reader session is now in use"
+ "NLM: %@ Accepted list does not hold the current link on transport %ld"
+ "NLM: %@ Accessory accepted the link on transport %ld, racing enabled"
+ "NLM: %@ Disconnected link is no longer held by the transport; ignoring"
+ "NLM: %@ Failed to close client for transport %ld: %@"
+ "NLM: %@ Live address arrived while awaiting initial resolve; applying inline instead of behind the deadlocked open operation"
+ "NLM: %@ No live %{public}s address to reopen on"
+ "NLM: %@ Probe on the accepted link on transport %ld failed: %ld (%lu attempt(s) left)"
+ "NLM: %@ Registered endpoints arrived with no second link to accept"
+ "NLM: %@ Secured client disconnected and the accessory never acknowledged the other link, tearing down transport to re-verify"
+ "NLM: %@ Secured over Thread, WiFi not acknowledged: sending request via secondary client [MID:%u]"
+ "NLM: %@ Stale link on transport %ld: client %{BOOL}d, secured %{public}s, other %{BOOL}d connected %{BOOL}d registered %{BOOL}d, endpoint list %{BOOL}d, supports WiFi %{BOOL}d Thread %{BOOL}d"
+ "NLM: %@ Transport capabilities - WiFi:%@ Thread:%@ KeepAlive:%@ EndpointList:%@"
+ "NLM: %@ applyResolverAddresses dropped empty delivery"
+ "NLM: %@ session local address family: %d (AF_INET=%d, AF_INET6=%d)"
+ "NLM: Close transport client"
+ "NLM: Connectivity restored with no attribute database — updating accessories"
+ "NLM: Received Empty CON ping (MID=%d)"
+ "NLM: Transport %ld controller was replaced before the close-client answer; dropping the decision"
+ "NLM: Transport %ld controller was replaced before the stale answer; dropping the decision"
+ "NLM: Transport %ld destination is unadvertised; rebuilding the link, keeping the session"
+ "NLM: Transport %ld destination is unadvertised; transport not open, leaving the session"
+ "NLM: Transport %ld unknown close-client result %ld; closing session"
+ "No delegate to check for an existing accessory; reporting already-paired"
+ "Not all blocks have ETag option\n"
+ "Note"
+ "OSC "
+ "Observe PDU presented to app.\n"
+ "Option Block2 has invalid set M bit - cleared\n"
+ "Option number %d is not defined as repeatable\n"
+ "Option number %d is not defined as repeatable - dropped\n"
+ "Oscore"
+ "PDU presented by app\n"
+ "PDU presented by app.\n"
+ "PDU presented to app.\n"
+ "Pair verify TLK not available on demand - failing pair setup"
+ "Pair verify TLK unavailable: %@"
+ "Pair-setup ended during the TLK request; not creating its session"
+ "Pair-setup stopped while M5 waited for network credentials; not sending M5"
+ "Pair-setup stopped while M5 was being assembled; not sending M5"
+ "Pair-setup: session wrapper released before M5; not sending M5"
+ "Pre-warm NFC reader arm refused as busy; pacing the re-arm by %.0fms"
+ "Pre-warm transition [%{public}s]: prewarming=%d searching=%d rearmCount=%lu/%lu hasReaderSession=%d hasDetectedServer=%d pairingInFlight=%d busyRetry=%lu/%lu"
+ "Pre-warmed pair-setup committed without a pairing request; M5 won't wait for credentials"
+ "Proxy loop detected '%s'\n"
+ "Proxy return has bad hop limit count '%zu'\n"
+ "Proxy-%s code %d.%02d handler not supported\n"
+ "Proxy-%s support not configured\n"
+ "Proxy-Scheme requires Uri-Host\n"
+ "Proxy-URI not decodable\n"
+ "Q-Block1"
+ "Q-Block2"
+ "Re-arming for another pairing attempt on a re-detected tag (from state %lu)"
+ "Reader session torn down while holding a tag; no longer claiming one"
+ "Reaping stale detected NFC server (%{public}s)"
+ "Received nack for message id %i with reason %d but no matching sent message, ignoring"
+ "Reliable: type != CON\n"
+ "Replaced option Q-Block1 with Block1\n"
+ "Replaced option Q-Block2 with Block2\n"
+ "Request-Tag"
+ "Resolver: abandoning retry ladder at rung %lu on stop for deviceID=%{public}@"
+ "Resolver: audit found unsubscribed resolver for deviceID=%{public}@ (pipelineStarted=%d tornDown=%d); starting retry ladder"
+ "Resolver: first delivery for deviceID=%{public}@ (primary=%lu secondary=%lu)"
+ "Resolver: pipeline arm FAILED for deviceID=%{public}@ serviceName='%{private}@' (factory returned nil; not subscribed)"
+ "Resolver: pipeline armed for deviceID=%{public}@ serviceName='%{private}@' (subscribed; rung=%lu everDelivered=%d)"
+ "Resolver: pipeline delivered error for deviceID=%{public}@ domain=%{public}@ code=%ld dnssd=%{public}@ marker=%ld voidsSubscription=%d"
+ "Resolver: retry ladder exhausted for deviceID=%{public}@ after %lu attempts; deferring to audit"
+ "Resolver: retry rung firing for deviceID=%{public}@ (attempt %lu)"
+ "Resolver: scheduling retry rung %lu/%lu in %.2fs for deviceID=%{public}@"
+ "Reusing NFC accessory server %@ for the re-detected tag"
+ "SPAKE2+ session requested pair verify TLK"
+ "Scheme"
+ "Server app version of updated PDU\n"
+ "Size of large buffer restricted to 0x%lx bytes\n"
+ "Skipping Thread credential fetch - neither required nor best-effort"
+ "Skipping network credential fetch - accessory does not support AES-CCM"
+ "Skipping the busy retry; NFC discovery was stopped or already restarted"
+ "TCP "
+ "TLS "
+ "Tag detected while a pairing is in flight; keeping the pairing server"
+ "Testing for Extended Token support\n"
+ "Thread credentials required for pair-setup are unavailable"
+ "Timed out waiting for Thread credential pre-warm before M5"
+ "Token reused - see https://rfc-editor.org/rfc/rfc9175.html#section-4.2\n"
+ "Too Many Requests"
+ "Too many missing blocks"
+ "Tuple change for CID failed\n"
+ "UDP "
+ "Unknown HAPErrorStatusCode %ld"
+ "Unknown HAPIPAddressVersion %ld"
+ "Unknown nack reason %d, treating as not deliverable"
+ "Unprocessable"
+ "Unsupported URI type %d\n"
+ "Uri"
+ "WS  "
+ "WSS "
+ "Wakeup pipe closed unexpectedly"
+ "Warn"
+ "WebSocket: type != CON\n"
+ "Wi-Fi credentials required for pair-setup are unavailable"
+ "[%s]:%d"
+ "[%{public}@] A pairing is in flight on the detected NFC server; keeping its reader session"
+ "[%{public}@] Accessory is already in a home and could not be replaced; reporting already-paired"
+ "[%{public}@] Delegate does not support accessoryServer:pairVerifyTLKWithError:"
+ "[%{public}@] Dropping exchange data from a pair-setup session that is no longer current"
+ "[%{public}@] Dropping existing-accessory check result after pair-setup teardown"
+ "[%{public}@] Failed to remove existing pairing key with error domain=%{public}@, code=%ld"
+ "[%{public}@] Failed to update keychain item to set invisible with error: %@"
+ "[%{public}@] Failed to update keychain item to set invisible with error: %d"
+ "[%{public}@] Failing HAP Browser instantiation - nil delegate"
+ "[%{public}@] Ignoring pending-commit notice from a pair-setup session that is no longer current"
+ "[%{public}@] Ignoring re-arm request; a pairing attempt is still in flight"
+ "[%{public}@] Ignoring stop from a pair-setup session that is no longer current (%{public}@ %ld)"
+ "[%{public}@] NFC server finished pairing; releasing its claim on the reader session"
+ "[%{public}@] NFC server started pairing; its reader session is now in use"
+ "[%{public}@] No delegate to check for an existing accessory; reporting already-paired"
+ "[%{public}@] Pair verify TLK unavailable: %@"
+ "[%{public}@] Pair-setup ended during the TLK request; not creating its session"
+ "[%{public}@] Pre-warm NFC reader arm refused as busy; pacing the re-arm by %.0fms"
+ "[%{public}@] Pre-warm transition [%{public}s]: prewarming=%d searching=%d rearmCount=%lu/%lu hasReaderSession=%d hasDetectedServer=%d pairingInFlight=%d busyRetry=%lu/%lu"
+ "[%{public}@] Re-arming for another pairing attempt on a re-detected tag (from state %lu)"
+ "[%{public}@] Reader session torn down while holding a tag; no longer claiming one"
+ "[%{public}@] Reaping stale detected NFC server (%{public}s)"
+ "[%{public}@] Reusing NFC accessory server %@ for the re-detected tag"
+ "[%{public}@] SPAKE2+ session requested pair verify TLK"
+ "[%{public}@] Skipping the busy retry; NFC discovery was stopped or already restarted"
+ "[%{public}@] Tag detected while a pairing is in flight; keeping the pairing server"
+ "[%{public}@] [Timing] NFC existing-accessory check: %.2fms"
+ "[%{public}@] didRegisterTransportEndpoints called -- NOP"
+ "[%{public}@] nfcd refused the NFC reader arm as busy; retrying in %.0fms (attempt %lu of %lu)"
+ "[%{public}@] nfcd still refuses the NFC reader as busy after %lu retries; giving up"
+ "[Timing] NFC existing-accessory check: %.2fms"
+ "application/ace+cbor"
+ "application/coap-group+json"
+ "application/cwt"
+ "application/dots+cbor"
+ "application/missing-blocks+cbor-seq"
+ "application/oscore"
+ "application/rdf+xml"
+ "block: Oversized packet - reduced to %u from %zu\n"
+ "block: Oversized packet - reduced to %zu from %zu\n"
+ "block: Undersized packet - expected %u, got %zu\n"
+ "block: Undersized packet chunk %u got %zu\n"
+ "buf"
+ "c"
+ "cache_entry"
+ "call custom handler for resource '%*.*s' (3)\n"
+ "call custom handler for resource '%*.*s' (4)\n"
+ "call handler for pseudo resource '%*.*s' (3)\n"
+ "cannot send response for mid=0x%04x\n"
+ "coap"
+ "coap+tcp"
+ "coap+tcp URI scheme not supported in this version of libcoap\n"
+ "coap+ws"
+ "coap+ws URI scheme not supported in this version of libcoap\n"
+ "coap_add_data: PDU already contains data\n"
+ "coap_add_data_large: PDU already contains data\n"
+ "coap_add_data_large_internal"
+ "coap_add_option_internal"
+ "coap_add_optlist_pdu: PDU already contains data\n"
+ "coap_add_resource_lkd"
+ "coap_add_token: Insufficient space for token. Token ignored\n"
+ "coap_add_token: Token size too large. PDU ignored\n"
+ "coap_add_token: Token size too large. Token ignored\n"
+ "coap_address.c"
+ "coap_block.c"
+ "coap_block_new_lg_crcv"
+ "coap_cache.c"
+ "coap_client_delay_first"
+ "coap_client_delay_first: timeout\n"
+ "coap_delete_cache_entry"
+ "coap_delete_observers"
+ "coap_dispatch: Received invalid PDU code (%d.%02d)\n"
+ "coap_dtls_hello: ContentType Connection-IS dropped\n"
+ "coap_encode.c"
+ "coap_encode_var_safe"
+ "coap_encode_var_safe8"
+ "coap_find_observer_cache_key"
+ "coap_free_endpoint_lkd"
+ "coap_get_data_large"
+ "coap_handle_dgram: UDP version not supported\n"
+ "coap_insert_option"
+ "coap_io_prepare_io_lkd"
+ "coap_is_bcst: Cannot determine any broadcast addresses\n"
+ "coap_is_bcst: Insufficient space for broadcast addresses\n"
+ "coap_net.c"
+ "coap_netif.c"
+ "coap_netif_dgrm_write"
+ "coap_new_string"
+ "coap_option.c"
+ "coap_pdu.c"
+ "coap_pdu_init"
+ "coap_pdu_parse: %d.%02d: offset %u malformed option\n"
+ "coap_pdu_parse: %d.%02d: offset %u option %u has bad length %u\n"
+ "coap_pdu_parse_opt"
+ "coap_print_ip_addr: inet_ntop\n"
+ "coap_print_wellknown_lkd"
+ "coap_remove_option"
+ "coap_resource.c"
+ "coap_send: Invalid PDU code (%d.%02d)\n"
+ "coap_send: PDU dropped as token too long (%zu > %u)\n"
+ "coap_send: Socket closed\n"
+ "coap_send: Using coap_cancel_observe() to do OBSERVE cancellation\n"
+ "coap_session_release_lkd"
+ "coap_socket_connect_udp: connect: %s (%d)\n"
+ "coap_socket_connect_udp: local address family != remote address family\n"
+ "coap_socket_connect_udp: setsockopt SO_BROADCAST: %s\n"
+ "coap_socket_connect_udp: unsupported sa_family %d\n"
+ "coap_socket_recv: %s\n"
+ "coap_socket_send: %s\n"
+ "coap_startup() should be called before any other coap_*() functions are called\n"
+ "coap_str.c"
+ "coap_write_block_b_opt"
+ "coaps"
+ "coaps URI scheme not supported in this version of libcoap\n"
+ "coaps+tcp"
+ "coaps+tcp URI scheme not supported in this version of libcoap\n"
+ "coaps+ws"
+ "coaps+ws URI scheme not supported in this version of libcoap\n"
+ "code <= 0xff"
+ "connection lost before consent"
+ "could not create response PDU\n"
+ "create new subscription %p key 0x%02x%02x%02x%02x\n"
+ "detectedServerReused"
+ "didRegisterTransportEndpoints called -- NOP"
+ "dropped ACK with request code (%d.%02d)\n"
+ "dropped client"
+ "found Block option, block is BERT, block nr. %u (%zu)\n"
+ "found Block option, block is BERT, block nr. %u, M %d\n"
+ "found Block option, block size is %u, block nr. %u\n"
+ "found Block option, block size is %u, block nr. %u, M %d\n"
+ "got RST for mid=0x%04x\n"
+ "handle_request: Invalid PDU response code (%d.%02d)\n"
+ "hnd_get_wellknown_lkd"
+ "http"
+ "https"
+ "ignoring request to change Block size from %u to %u\n"
+ "ignoring request to increase Block size, (%u > %u)\n"
+ "ignoring request to increase Block size, next block is not aligned on requested block size boundary. (%zu x %u mod %u = %zu != 0)\n"
+ "len <= (size_t)wkc_len"
+ "mcast delay: insufficient memory\n"
+ "mid >= 0 && mid <= 0xffff"
+ "n <= length"
+ "new Block size is %u, block number %u completed\n"
+ "next_option != NULL"
+ "nfcd refused the NFC reader arm as busy; retrying in %.0fms (attempt %lu of %lu)"
+ "nfcd still refuses the NFC reader as busy after %lu retries; giving up"
+ "not enough space, even the smallest block does not fit (1)\n"
+ "not enough space, even the smallest block does not fit (2)\n"
+ "not enough space, even the smallest block does not fit (3)\n"
+ "observe: unexpected action %d\n"
+ "option != NULL"
+ "other link"
+ "pdu->data"
+ "pdu->hdr_size == 2"
+ "removed subscription %p with token '%s' key 0x%02x%02x%02x%02x\n"
+ "replaced by a tag with a different setup payload"
+ "resource->context == NULL"
+ "resource->subscribers"
+ "s->ref > 1"
+ "serverFinishedPairing"
+ "serverStartedPairing"
+ "session->ref == 1"
+ "setup_block_b"
+ "size+1 != 0"
+ "stale link"
+ "start <= total"
+ "type <= 0x3"
+ "v16@?0q8"
+ "v24@?0@\"HAP2CoAPClient\"8^{coap_session_t=iiiIQQQ{coap_addr_hash_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{coap_sockaddr_un=C[27c]})}Si}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{coap_sockaddr_un=C[27c]})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{coap_sockaddr_un=C[27c]})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{coap_sockaddr_un=C[27c]})}[3{?=^?^?^?^?}]}^{coap_endpoint_t}^{coap_context_t}^vSCCi^{coap_queue_t}^{coap_lg_xmit_t}^{coap_lg_crcv_t}^{coap_lg_srcv_t}Q[8C]Q^{coap_pdu_t}QQQQQ{coap_dtls_cpsk_t=CCC[5C]^?^v*{coap_dtls_cpsk_info_t={coap_bin_const_t=Q*}{coap_bin_const_t=Q*}}}^{coap_bin_const_t}^{coap_bin_const_t}^{coap_bin_const_t}^v{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}SS{coap_fixed_point_t=SS}IIiIICCCCCCCCCCiIQ^{coap_bin_const_t}^{coap_bin_const_t}iii^{coap_bin_const_t}dddIddddCddI[32{?=SdC}]}16"
+ "v24@?0^{coap_context_t={coap_opt_filter_t=S[2S][6C]}^{coap_resource_t}^{coap_resource_t}^{coap_resource_t}^?Q^{coap_queue_t}^{coap_endpoint_t}^{coap_session_t}^?^?^?^?^?^?^vI^?^?^?^?^v{coap_dtls_spsk_t=CC[6C]^?^v^?^v{coap_dtls_spsk_info_t={coap_bin_const_t=Q*}{coap_bin_const_t=Q*}}}IIIIIIQ^{coap_cache_entry_t}^SQ^vI{fd_set=[32i]}{fd_set=[32i]}{fd_set=[32i]}[64^{coap_socket_t}]ICCCCI}8^{coap_session_t=iiiIQQQ{coap_addr_hash_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{coap_sockaddr_un=C[27c]})}Si}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{coap_sockaddr_un=C[27c]})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{coap_sockaddr_un=C[27c]})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{coap_sockaddr_un=C[27c]})}[3{?=^?^?^?^?}]}^{coap_endpoint_t}^{coap_context_t}^vSCCi^{coap_queue_t}^{coap_lg_xmit_t}^{coap_lg_crcv_t}^{coap_lg_srcv_t}Q[8C]Q^{coap_pdu_t}QQQQQ{coap_dtls_cpsk_t=CCC[5C]^?^v*{coap_dtls_cpsk_info_t={coap_bin_const_t=Q*}{coap_bin_const_t=Q*}}}^{coap_bin_const_t}^{coap_bin_const_t}^{coap_bin_const_t}^v{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}SS{coap_fixed_point_t=SS}IIiIICCCCCCCCCCiIQ^{coap_bin_const_t}^{coap_bin_const_t}iii^{coap_bin_const_t}dddIddddCddI[32{?=SdC}]}16"
+ "v:Reliable c:%s {"
+ "v:WebSocket c:%s {"
+ "\x81\xf0\xe1!"
+ "\xf01\xf0A"
- " DTLS"
- " NONE"
- " TCP "
- " TLS "
- " UDP "
- "!Aq\x81"
- "%@ HDS-over-TCP peer selected: %s from %s (%{private}@)"
- "%s     IPV6_PKTINFO: ifindex=%d, addr=%s\n"
- "%s     IPV6_TCLASS: 0x%02x (DSCP 0x%02x)\n"
- "%s     IP_PKTINFO: ifindex=%d, ipi_spec_dst=%s, ipi_addr=%s\n"
- "%s     IP_TOS: 0x%02x (DSCP 0x%02x)\n"
- "%s     SO_TRAFFIC_CLASS: %d\n"
- "%s   No control messages.\n"
- "%s   cmsg: level=%d, type=%d, len=%u\n"
- "%s   iov[%d]: base=%p, len=%zu\n"
- "%s --- End msghdr Info ---\n"
- "%s --- msghdr Info ---\n"
- "%s msg_controllen: %u\n"
- "%s msg_flags: 0x%x ["
- "%s msg_iovlen: %d\n"
- "%s msg_name: AF_INET %s:%d (len %d)\n"
- "%s msg_name: AF_INET6 %s:%d (len %d)\n"
- "%s msg_name: NULL (len %d)\n"
- "%s msg_name: Unknown Family %d (len %d)\n"
- "'%s'"
- "(resource_param.length + 1) <= coap_opt_length(query_filter)"
- "*   %s: failed to send %zd bytes\n"
- "*  %s: failed to send %zd bytes\n"
- "*  %s: read error\n"
- "*  %s: received %zd bytes\n"
- "*  %s: sent %zd bytes\n"
- "**  %s: tid=%d: already in-use - dropped\n"
- "** %s: tid=%d: added to retransmit queue (%ums)\n"
- "** %s: tid=%d: delayed\n"
- "** %s: tid=%d: give up after %d attempts\n"
- "** %s: tid=%d: not transmitted after disconnect\n"
- "** %s: tid=%d: removed\n"
- "** %s: tid=%d: retransmission #%d\n"
- "** %s: tid=%d: transmitted after delay\n"
- "** removed observer %s\n"
- "***%s: new incoming session\n"
- "***%s: new outgoing session\n"
- "***%s: sending CSM\n"
- "***%s: session ack_random_factor set to %d.%03d\n"
- "***%s: session closed\n"
- "***%s: session disconnected (reason %d)\n"
- "***EVENT: 0x%04x\n"
- ":%d"
- "<HAPCameraBufferActivityCommandRequest start=%@, duration=%@, activity=%@>"
- "<HAPCameraVideoStreamCapabilities identifier=%@, quality=%@, width=%@, height=%@, framesPerSecond=%@, averageBitrate=%@, peakBitrate=%@>"
- "<libcoap> Unknown log level (%u) for message: %{private}s"
- "Also setting SO_TRAFFIC_CLASS to %d (mapped from DSCP %d)\n"
- "Block-wise-Transfer"
- "CIPH"
- "COAP_PROTO_RELIABLE(session->proto)"
- "Chosen sock->fd = %d, flags = %d\n"
- "Coap Network Read"
- "Coap_write timeout %u, requested time %u"
- "Could not get next control message header for AQM.\n"
- "Delegate does not support requestPairVerifyTLKWithCompletion: - cannot proceed with NFC pair-setup"
- "ECDSA pairing key already exists for peer; reporting already-paired"
- "Failed to run coap_run_once"
- "Failed to updated keychain item to set invisible with error: %@"
- "Failed to updated keychain item to set invisible with error: %d"
- "Failing HAP Browser instantioation - nil delegate"
- "ICMP port unreachable; failing this session's queued messages now"
- "Invalid socket file descriptor (fd = -1).\n"
- "MSG_CTRUNC "
- "MSG_TRUNC "
- "NLM keep-alive listener active, skipping reachability client"
- "NLM: %@ Transport capabilities - WiFi:%@ Thread:%@ KeepAlive:%@"
- "NLM: %@ session->addr_info.local family: %d (AF_INET=%d, AF_INET6=%d)"
- "NLM: Received Empty CON ping (MID=%d), sending RST"
- "Pipe closed unexpectedly"
- "Pre-warm transition [%{public}s]: prewarming=%d searching=%d rearmCount=%lu/%lu hasReaderSession=%d hasDetectedServer=%d"
- "Pre-warming Thread credentials during M1"
- "Pre-warming WiFi credentials during M1"
- "Reaping stale pre-warm-detected NFC server (connection lost before consent)"
- "Resolver pipeline factory returned nil"
- "Resolver: never-delivered health-check restart for deviceID=%{public}@"
- "Resolver: pipeline delivered fatal error for deviceID=%{public}@ domain=%{public}@ code=%ld marker=%ld"
- "Resolver: pipeline factory failed for deviceID=%{public}@"
- "Setting IPV6_TCLASS to 0x%x (DSCP %d)\n"
- "Setting IP_TOS to 0x%x (DSCP %d)\n"
- "Skipping network credential pre-warming - accessory does not support AES-CCM"
- "TLK not available for NFC pair-setup"
- "TX: "
- "Unsupported address family for DSCP/AQM. Sending without it.\n"
- "Using connected socket path (msg_name=NULL).\n"
- "Using unconnected socket path (msg_name set).\n"
- "[%{public}@] Delegate does not support requestPairVerifyTLKWithCompletion: - cannot proceed with NFC pair-setup"
- "[%{public}@] ECDSA pairing key already exists for peer; reporting already-paired"
- "[%{public}@] Failed to updated keychain item to set invisible with error: %@"
- "[%{public}@] Failed to updated keychain item to set invisible with error: %d"
- "[%{public}@] Failing HAP Browser instantioation - nil delegate"
- "[%{public}@] Pre-warm transition [%{public}s]: prewarming=%d searching=%d rearmCount=%lu/%lu hasReaderSession=%d hasDetectedServer=%d"
- "[%{public}@] Reaping stale pre-warm-detected NFC server (connection lost before consent)"
- "[%{public}@] [Timing] NFC duplicate existence-check: %.2fms"
- "[Timing] NFC duplicate existence-check: %.2fms"
- "]\n"
- "address.c"
- "block.c"
- "call custom handler for resource '%*.*s'\n"
- "cannot generate response\r\n"
- "cannot send response for message %d\n"
- "cannot send response for transaction %d\n"
- "cannot send response for transaction %u\n"
- "coap_encode_var_safe(buf, sizeof(buf), COAP_MEDIATYPE_APPLICATION_LINK_FORMAT) == 1"
- "coap_free_endpoint"
- "coap_get_data"
- "coap_network_read"
- "coap_network_read: %s\n"
- "coap_network_read: unreachable\n"
- "coap_network_send"
- "coap_network_send: %s\n"
- "coap_pdu_parse: missing payload start code\n"
- "coap_pdu_parse_header_size"
- "coap_pdu_parse_header_size(proto, data) <= length"
- "coap_pdu_parse_size"
- "coap_print_wellknown"
- "coap_send_pdu_dscp"
- "coap_send_pdu_dscp failed: %s (%d)\n"
- "coap_send_pdu_dscp: Session state = %d\n"
- "coap_session_release"
- "coap_session_send"
- "coap_session_send_csm"
- "coap_socket_accept_tcp: accept: %s\n"
- "coap_socket_accept_tcp: getsockname: %s\n"
- "coap_socket_accept_tcp: ioctl FIONBIO: %s\n"
- "coap_socket_connect_tcp1: bind: %s\n"
- "coap_socket_connect_tcp1: connect: %s\n"
- "coap_socket_connect_tcp1: getpeername: %s\n"
- "coap_socket_connect_tcp1: getsockname: %s\n"
- "coap_socket_connect_tcp1: ioctl FIONBIO: %s\n"
- "coap_socket_connect_tcp1: setsockopt IPV6_V6ONLY: %s\n"
- "coap_socket_connect_tcp1: setsockopt SO_REUSEADDR: %s\n"
- "coap_socket_connect_tcp1: socket: %s\n"
- "coap_socket_connect_tcp1: unsupported sa_family\n"
- "coap_socket_connect_tcp: getpeername: %s\n"
- "coap_socket_connect_tcp: getsockname: %s\n"
- "coap_socket_connect_udp: connect: %s\n"
- "coap_socket_connect_udp: unsupported sa_family\n"
- "coap_socket_finish_connect_tcp: connect failed: %s\n"
- "coap_socket_finish_connect_tcp: getsockopt: %s\n"
- "coap_socket_read: recv: %s\n"
- "coap_socket_write: send: %s\n"
- "coap_wellknown_response"
- "coap_wellknown_response: cannot add Block2 option\n"
- "coap_wellknown_response: cannot add token\n"
- "coap_wellknown_response: cannot create PDU\n"
- "coap_wellknown_response: coap_add_data failed\n"
- "coap_wellknown_response: insufficient storage space\n"
- "coap_wellknown_response: message to small even for szx == 0\n"
- "coap_wellknown_response: undefined resource\n"
- "coap_write_block_opt"
- "create block\n"
- "create default response for %s\n"
- "create new subscription\n"
- "get_wkc_len: coap_print_wellknown() returned %zu\n"
- "got RST for message %d\n"
- "handle_request"
- "have wellknown response %p\n"
- "insufficient space for block option\n"
- "method not allowed for .well-known/core\n"
- "net.c"
- "no_response"
- "not enough space, even the smallest block does not fit"
- "option.c"
- "packet"
- "pdu->data == NULL"
- "pdu->max_hdr_size >= 2"
- "pdu->max_hdr_size >= 3"
- "pdu->max_hdr_size >= 6"
- "pdu->used_size >= pdu->token_length"
- "pdu.c"
- "proto == COAP_PROTO_TCP || proto == COAP_PROTO_TLS"
- "removed observer tid %s\n"
- "resource.c"
- "resp->used_size <= resp->max_size"
- "response == NULL"
- "sock"
- "v24@?0@\"HAP2CoAPClient\"8^{coap_session_t=CCCIII{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}}^{coap_endpoint_t}^{coap_context_t}^vSCi^{coap_queue_t}Q[8C]Q^{coap_pdu_t}QQQQQ*Q*Q^vI{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}IidddIddddCddI[32{?=SdC}]}16"
- "v24@?0^{coap_context_t=[6S]^{coap_resource_t}^{coap_resource_t}^{coap_async_state_t}Q^{coap_queue_t}^{coap_endpoint_t}^{coap_session_t}^?^?^?^?^?^?^?^?^?^?^v*Q*QIIIII^v}8^{coap_session_t=CCCIII{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{UT_hash_handle=^{UT_hash_table}^v^v^{UT_hash_handle}^{UT_hash_handle}^vII}{coap_addr_tuple_t={coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}}i{coap_socket_t=iS^{coap_session_t}^{coap_endpoint_t}}^{coap_endpoint_t}^{coap_context_t}^vSCi^{coap_queue_t}Q[8C]Q^{coap_pdu_t}QQQQQ*Q*Q^vI{coap_fixed_point_t=SS}{coap_fixed_point_t=SS}IidddIddddCddI[32{?=SdC}]}16"
- "\x91\xf0\xf0Q!"
```
