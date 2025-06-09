## CoreHAP

> `/System/Library/PrivateFrameworks/CoreHAP.framework/CoreHAP`

```diff

-1278.6.31.1.1
-  __TEXT.__text: 0x1a50c8
-  __TEXT.__auth_stubs: 0x1590
-  __TEXT.__objc_methlist: 0x13740
-  __TEXT.__const: 0x6f0
+1323.0.6.0.1
+  __TEXT.__text: 0x1a6ac4
+  __TEXT.__auth_stubs: 0x15b0
+  __TEXT.__objc_methlist: 0x138c8
+  __TEXT.__const: 0x700
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__gcc_except_tab: 0x6238
-  __TEXT.__cstring: 0x10937
-  __TEXT.__oslogstring: 0x1fc02
-  __TEXT.__unwind_info: 0x5c48
-  __TEXT.__objc_classname: 0x2ddd
-  __TEXT.__objc_methname: 0x2655f
-  __TEXT.__objc_methtype: 0x8f76
-  __TEXT.__objc_stubs: 0x18500
+  __TEXT.__gcc_except_tab: 0x62f0
+  __TEXT.__cstring: 0x10a1e
+  __TEXT.__oslogstring: 0x1ff5a
+  __TEXT.__unwind_info: 0x5d38
+  __TEXT.__objc_classname: 0x2df8
+  __TEXT.__objc_methname: 0x268b3
+  __TEXT.__objc_methtype: 0x8fb9
+  __TEXT.__objc_stubs: 0x187c0
   __DATA_CONST.__got: 0xa68
-  __DATA_CONST.__const: 0x4ff0
+  __DATA_CONST.__const: 0x5070
   __DATA_CONST.__objc_classlist: 0x960
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x330
+  __DATA_CONST.__objc_protolist: 0x338
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6e90
+  __DATA_CONST.__objc_selrefs: 0x6f30
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x7e0
   __DATA_CONST.__objc_arraydata: 0x208
-  __AUTH_CONST.__auth_got: 0xad8
+  __AUTH_CONST.__auth_got: 0xae8
   __AUTH_CONST.__const: 0x800
-  __AUTH_CONST.__cfstring: 0xda20
-  __AUTH_CONST.__objc_const: 0x21f20
+  __AUTH_CONST.__cfstring: 0xdb20
+  __AUTH_CONST.__objc_const: 0x220d0
   __AUTH_CONST.__objc_intobj: 0x6c0
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0xd8
-  __AUTH.__objc_data: 0x4e70
-  __DATA.__objc_ivar: 0x14d8
-  __DATA.__data: 0x266a
-  __DATA.__bss: 0x4a9
-  __DATA_DIRTY.__objc_data: 0xf50
-  __DATA_DIRTY.__bss: 0xb8
+  __AUTH.__objc_data: 0x4dd0
+  __DATA.__objc_ivar: 0x14f4
+  __DATA.__data: 0x26c2
+  __DATA.__bss: 0x499
+  __DATA_DIRTY.__objc_data: 0xff0
+  __DATA_DIRTY.__data: 0x8
+  __DATA_DIRTY.__bss: 0xc8
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Network.framework/Network

   - /System/Library/PrivateFrameworks/CloudServices.framework/CloudServices
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
+  - /System/Library/PrivateFrameworks/CryptoKitPrivate.framework/CryptoKitPrivate
   - /System/Library/PrivateFrameworks/EasyConfig.framework/EasyConfig
   - /System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation
   - /System/Library/PrivateFrameworks/HomeKitFeatures.framework/HomeKitFeatures

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/WirelessProximity.framework/WirelessProximity
   - /usr/lib/libSystem.B.dylib
-  - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F7487F3B-7EF9-3D78-B0C6-65B6D76CC6F9
-  Functions: 7458
-  Symbols:   24232
-  CStrings:  12829
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: AFAED248-15CF-3B34-B17A-D9779977E15C
+  Functions: 7481
+  Symbols:   24356
+  CStrings:  12891
 
Symbols:
+ +[HAP2AccessoryServerTransportCoAP sortAddressList:]
+ +[HAPHTTPClient dnsNameForHTTPHeaderFromDNSNames:]
+ +[HAPSRPPairSetupSession initialize]
+ +[HAPSRPPairSetupSession isValidSetupCode:]
+ +[HAPSRPPairSetupSession logCategory]
+ -[HAP2AccessoryDeviceIPAddress description]
+ -[HAPAccessory setSuspendCapable:]
+ -[HAPAccessory suspendCapable]
+ -[HAPAccessoryServerBrowser pairSetupSession:pairSetupType:features:]
+ -[HAPAccessoryServerBrowser removeRecentlySeenPairedPeripheralWithIdentifier:]
+ -[HAPAccessoryServerBrowserBTLE _removeRecentlySeenPairedPeripheralWithIdentifier:]
+ -[HAPAccessoryServerBrowserBTLE removeRecentlySeenPairedPeripheralWithIdentifier:]
+ -[HAPAccessoryServerIP currentPairVerifyError]
+ -[HAPAccessoryServerIP ensureNetworkMonitor]
+ -[HAPAccessoryServerIP httpClient:didStartConnectingToNetAddress:]
+ -[HAPAccessoryServerIP setCurrentPairVerifyError:]
+ -[HAPAccessoryServerIP setTriedConnectingToIPv4Address:]
+ -[HAPAccessoryServerIP setTriedConnectingToIPv6Address:]
+ -[HAPAccessoryServerIP triedConnectingToIPv4Address]
+ -[HAPAccessoryServerIP triedConnectingToIPv6Address]
+ -[HAPCoreUtilsHTTPClient isInvalidated]
+ -[HAPCoreUtilsHTTPClient setConnectionProgressHandler:context:]
+ -[HAPCoreUtilsHTTPClient setContext:]
+ -[HAPCoreUtilsHTTPClient setIsInvalidated:]
+ -[HAPMetricsPairVerifyEvent triedConnectingToIPv4Address]
+ -[HAPMetricsPairVerifyEvent triedConnectingToIPv6Address]
+ -[HAPSRPPairSetupSession .cxx_destruct]
+ -[HAPSRPPairSetupSession _handleBackoffExpiration]
+ -[HAPSRPPairSetupSession _handleLocalPairingIdentityRequestWithStatus:]
+ -[HAPSRPPairSetupSession _handlePairSetupExchangeComplete]
+ -[HAPSRPPairSetupSession _handleProductData:]
+ -[HAPSRPPairSetupSession _initializeServer]
+ -[HAPSRPPairSetupSession _initializeSession]
+ -[HAPSRPPairSetupSession _initiateClientPairSetupExchange]
+ -[HAPSRPPairSetupSession _invalidate]
+ -[HAPSRPPairSetupSession _processSetupCode:error:]
+ -[HAPSRPPairSetupSession _processSetupExchangeData:error:]
+ -[HAPSRPPairSetupSession _showSetupCodeWithError:]
+ -[HAPSRPPairSetupSession _stopWithError:]
+ -[HAPSRPPairSetupSession backoffTimer]
+ -[HAPSRPPairSetupSession certificate]
+ -[HAPSRPPairSetupSession clientQueue]
+ -[HAPSRPPairSetupSession dealloc]
+ -[HAPSRPPairSetupSession debugDescription]
+ -[HAPSRPPairSetupSession decryptData:additionalAuthenticatedData:error:]
+ -[HAPSRPPairSetupSession delegate]
+ -[HAPSRPPairSetupSession descriptionWithPointer:]
+ -[HAPSRPPairSetupSession description]
+ -[HAPSRPPairSetupSession encryptData:additionalAuthenticatedData:error:]
+ -[HAPSRPPairSetupSession generateSessionKeys]
+ -[HAPSRPPairSetupSession getCertificate]
+ -[HAPSRPPairSetupSession handleBackoffRequestWithTimeout:]
+ -[HAPSRPPairSetupSession handleInvalidSetupCodeAndRestart:]
+ -[HAPSRPPairSetupSession handleSavePeerRequestWithPeerIdentity:error:]
+ -[HAPSRPPairSetupSession handleSetupCodeRequest]
+ -[HAPSRPPairSetupSession initWithRole:pairSetupType:delegate:]
+ -[HAPSRPPairSetupSession init]
+ -[HAPSRPPairSetupSession isHandlingInvalidSetupCode]
+ -[HAPSRPPairSetupSession isSecureSession]
+ -[HAPSRPPairSetupSession logIdentifier]
+ -[HAPSRPPairSetupSession pairSetupType]
+ -[HAPSRPPairSetupSession pairingSession]
+ -[HAPSRPPairSetupSession receivedSetupExchangeData:error:]
+ -[HAPSRPPairSetupSession role]
+ -[HAPSRPPairSetupSession sessionReadKey]
+ -[HAPSRPPairSetupSession sessionReadNonce]
+ -[HAPSRPPairSetupSession sessionWriteKey]
+ -[HAPSRPPairSetupSession sessionWriteNonce]
+ -[HAPSRPPairSetupSession setBackoffTimer:]
+ -[HAPSRPPairSetupSession setCertificate:]
+ -[HAPSRPPairSetupSession setHandlingInvalidSetupCode:]
+ -[HAPSRPPairSetupSession setPairSetupType:]
+ -[HAPSRPPairSetupSession setSessionReadKey:]
+ -[HAPSRPPairSetupSession setSessionReadNonce:]
+ -[HAPSRPPairSetupSession setSessionWriteKey:]
+ -[HAPSRPPairSetupSession setSessionWriteNonce:]
+ -[HAPSRPPairSetupSession setState:]
+ -[HAPSRPPairSetupSession shortDescription]
+ -[HAPSRPPairSetupSession start]
+ -[HAPSRPPairSetupSession state]
+ -[HAPSRPPairSetupSession stopWithError:]
+ -[HAPSRPPairSetupSession stop]
+ -[HAPSRPPairSetupSession timerDidFire:]
+ -[NSError(HAPError) isHAPOperationDelayed]
+ GCC_except_table1042
+ GCC_except_table1046
+ GCC_except_table1059
+ GCC_except_table1064
+ GCC_except_table1073
+ GCC_except_table1075
+ GCC_except_table1077
+ GCC_except_table1079
+ GCC_except_table1205
+ GCC_except_table1209
+ GCC_except_table1211
+ GCC_except_table1423
+ GCC_except_table1629
+ GCC_except_table1632
+ GCC_except_table1640
+ GCC_except_table1642
+ GCC_except_table1648
+ GCC_except_table1650
+ GCC_except_table1654
+ GCC_except_table1660
+ GCC_except_table1665
+ GCC_except_table1669
+ GCC_except_table1679
+ GCC_except_table1694
+ GCC_except_table1698
+ GCC_except_table1702
+ GCC_except_table1706
+ GCC_except_table1708
+ GCC_except_table1861
+ GCC_except_table1862
+ GCC_except_table1864
+ GCC_except_table1866
+ GCC_except_table1875
+ GCC_except_table1881
+ GCC_except_table1884
+ GCC_except_table1886
+ GCC_except_table1889
+ GCC_except_table1909
+ GCC_except_table1911
+ GCC_except_table1920
+ GCC_except_table1924
+ GCC_except_table1926
+ GCC_except_table1932
+ GCC_except_table1934
+ GCC_except_table1936
+ GCC_except_table1940
+ GCC_except_table1944
+ GCC_except_table1952
+ GCC_except_table1963
+ GCC_except_table2001
+ GCC_except_table2007
+ GCC_except_table2185
+ GCC_except_table2191
+ GCC_except_table2197
+ GCC_except_table2200
+ GCC_except_table2203
+ GCC_except_table2206
+ GCC_except_table2218
+ GCC_except_table2219
+ GCC_except_table2221
+ GCC_except_table2317
+ GCC_except_table2325
+ GCC_except_table2326
+ GCC_except_table2327
+ GCC_except_table2328
+ GCC_except_table2329
+ GCC_except_table2330
+ GCC_except_table2345
+ GCC_except_table2359
+ GCC_except_table2439
+ GCC_except_table2451
+ GCC_except_table2477
+ GCC_except_table2485
+ GCC_except_table2496
+ GCC_except_table2510
+ GCC_except_table2513
+ GCC_except_table2518
+ GCC_except_table2526
+ GCC_except_table2532
+ GCC_except_table2534
+ GCC_except_table2708
+ GCC_except_table2758
+ GCC_except_table2774
+ GCC_except_table2777
+ GCC_except_table2791
+ GCC_except_table2792
+ GCC_except_table2799
+ GCC_except_table2814
+ GCC_except_table2826
+ GCC_except_table2827
+ GCC_except_table2829
+ GCC_except_table2842
+ GCC_except_table2845
+ GCC_except_table2850
+ GCC_except_table2909
+ GCC_except_table2914
+ GCC_except_table2916
+ GCC_except_table2930
+ GCC_except_table2944
+ GCC_except_table2946
+ GCC_except_table2950
+ GCC_except_table2958
+ GCC_except_table2966
+ GCC_except_table3023
+ GCC_except_table3025
+ GCC_except_table3026
+ GCC_except_table3049
+ GCC_except_table3293
+ GCC_except_table3358
+ GCC_except_table3365
+ GCC_except_table3367
+ GCC_except_table3368
+ GCC_except_table3370
+ GCC_except_table3371
+ GCC_except_table3373
+ GCC_except_table3380
+ GCC_except_table3390
+ GCC_except_table3405
+ GCC_except_table3407
+ GCC_except_table3415
+ GCC_except_table3417
+ GCC_except_table3420
+ GCC_except_table3423
+ GCC_except_table3435
+ GCC_except_table3437
+ GCC_except_table3441
+ GCC_except_table3445
+ GCC_except_table3449
+ GCC_except_table3475
+ GCC_except_table3497
+ GCC_except_table3500
+ GCC_except_table3502
+ GCC_except_table3504
+ GCC_except_table3579
+ GCC_except_table3580
+ GCC_except_table3581
+ GCC_except_table3582
+ GCC_except_table3583
+ GCC_except_table3584
+ GCC_except_table3585
+ GCC_except_table3586
+ GCC_except_table3587
+ GCC_except_table3588
+ GCC_except_table3589
+ GCC_except_table3590
+ GCC_except_table3591
+ GCC_except_table3592
+ GCC_except_table3629
+ GCC_except_table3655
+ GCC_except_table3746
+ GCC_except_table3753
+ GCC_except_table3771
+ GCC_except_table3775
+ GCC_except_table3778
+ GCC_except_table3781
+ GCC_except_table3784
+ GCC_except_table3787
+ GCC_except_table3793
+ GCC_except_table3796
+ GCC_except_table3799
+ GCC_except_table3818
+ GCC_except_table3829
+ GCC_except_table3837
+ GCC_except_table3841
+ GCC_except_table3848
+ GCC_except_table3849
+ GCC_except_table3853
+ GCC_except_table3854
+ GCC_except_table3874
+ GCC_except_table3876
+ GCC_except_table3880
+ GCC_except_table3886
+ GCC_except_table3889
+ GCC_except_table3891
+ GCC_except_table3897
+ GCC_except_table3899
+ GCC_except_table3902
+ GCC_except_table3914
+ GCC_except_table3925
+ GCC_except_table3927
+ GCC_except_table3936
+ GCC_except_table3942
+ GCC_except_table404
+ GCC_except_table420
+ GCC_except_table4202
+ GCC_except_table4208
+ GCC_except_table4225
+ GCC_except_table4229
+ GCC_except_table4246
+ GCC_except_table4252
+ GCC_except_table4279
+ GCC_except_table428
+ GCC_except_table4283
+ GCC_except_table4396
+ GCC_except_table4476
+ GCC_except_table4484
+ GCC_except_table4494
+ GCC_except_table4531
+ GCC_except_table4534
+ GCC_except_table4535
+ GCC_except_table4536
+ GCC_except_table4537
+ GCC_except_table458
+ GCC_except_table4635
+ GCC_except_table4636
+ GCC_except_table4637
+ GCC_except_table4638
+ GCC_except_table4639
+ GCC_except_table4646
+ GCC_except_table4647
+ GCC_except_table4649
+ GCC_except_table4659
+ GCC_except_table466
+ GCC_except_table4661
+ GCC_except_table4666
+ GCC_except_table4669
+ GCC_except_table4672
+ GCC_except_table4676
+ GCC_except_table4680
+ GCC_except_table4709
+ GCC_except_table4710
+ GCC_except_table4729
+ GCC_except_table4739
+ GCC_except_table4742
+ GCC_except_table4747
+ GCC_except_table4750
+ GCC_except_table480
+ GCC_except_table481
+ GCC_except_table483
+ GCC_except_table486
+ GCC_except_table489
+ GCC_except_table5014
+ GCC_except_table5018
+ GCC_except_table505
+ GCC_except_table5052
+ GCC_except_table5056
+ GCC_except_table5058
+ GCC_except_table5060
+ GCC_except_table515
+ GCC_except_table521
+ GCC_except_table5217
+ GCC_except_table5223
+ GCC_except_table5227
+ GCC_except_table5228
+ GCC_except_table5229
+ GCC_except_table5230
+ GCC_except_table5236
+ GCC_except_table5270
+ GCC_except_table5271
+ GCC_except_table5272
+ GCC_except_table5292
+ GCC_except_table5304
+ GCC_except_table5307
+ GCC_except_table5312
+ GCC_except_table5314
+ GCC_except_table5328
+ GCC_except_table546
+ GCC_except_table5530
+ GCC_except_table5542
+ GCC_except_table5547
+ GCC_except_table5550
+ GCC_except_table5551
+ GCC_except_table5553
+ GCC_except_table5554
+ GCC_except_table5556
+ GCC_except_table556
+ GCC_except_table5586
+ GCC_except_table5608
+ GCC_except_table5612
+ GCC_except_table5616
+ GCC_except_table5621
+ GCC_except_table5625
+ GCC_except_table563
+ GCC_except_table5633
+ GCC_except_table5637
+ GCC_except_table5645
+ GCC_except_table5647
+ GCC_except_table5649
+ GCC_except_table5709
+ GCC_except_table5710
+ GCC_except_table5711
+ GCC_except_table5712
+ GCC_except_table5713
+ GCC_except_table5772
+ GCC_except_table5787
+ GCC_except_table5793
+ GCC_except_table5806
+ GCC_except_table5809
+ GCC_except_table5810
+ GCC_except_table5815
+ GCC_except_table5818
+ GCC_except_table5825
+ GCC_except_table5828
+ GCC_except_table5842
+ GCC_except_table5849
+ GCC_except_table5855
+ GCC_except_table5864
+ GCC_except_table5870
+ GCC_except_table5871
+ GCC_except_table5886
+ GCC_except_table5888
+ GCC_except_table5896
+ GCC_except_table590
+ GCC_except_table5912
+ GCC_except_table5921
+ GCC_except_table5922
+ GCC_except_table5925
+ GCC_except_table5931
+ GCC_except_table5935
+ GCC_except_table5937
+ GCC_except_table5939
+ GCC_except_table594
+ GCC_except_table5943
+ GCC_except_table596
+ GCC_except_table598
+ GCC_except_table604
+ GCC_except_table606
+ GCC_except_table6090
+ GCC_except_table6146
+ GCC_except_table6149
+ GCC_except_table6153
+ GCC_except_table6159
+ GCC_except_table618
+ GCC_except_table6183
+ GCC_except_table6187
+ GCC_except_table6188
+ GCC_except_table6189
+ GCC_except_table622
+ GCC_except_table6237
+ GCC_except_table6238
+ GCC_except_table6240
+ GCC_except_table6243
+ GCC_except_table6271
+ GCC_except_table6272
+ GCC_except_table6277
+ GCC_except_table6297
+ GCC_except_table6314
+ GCC_except_table6315
+ GCC_except_table6316
+ GCC_except_table6324
+ GCC_except_table6329
+ GCC_except_table6330
+ GCC_except_table6331
+ GCC_except_table6345
+ GCC_except_table6348
+ GCC_except_table6354
+ GCC_except_table636
+ GCC_except_table6360
+ GCC_except_table6373
+ GCC_except_table6378
+ GCC_except_table6387
+ GCC_except_table6393
+ GCC_except_table6398
+ GCC_except_table6406
+ GCC_except_table641
+ GCC_except_table6410
+ GCC_except_table6412
+ GCC_except_table6416
+ GCC_except_table6437
+ GCC_except_table6439
+ GCC_except_table644
+ GCC_except_table6440
+ GCC_except_table6466
+ GCC_except_table652
+ GCC_except_table656
+ GCC_except_table662
+ GCC_except_table663
+ GCC_except_table6630
+ GCC_except_table668
+ GCC_except_table669
+ GCC_except_table6693
+ GCC_except_table6725
+ GCC_except_table6728
+ GCC_except_table6892
+ GCC_except_table695
+ GCC_except_table6955
+ GCC_except_table7019
+ GCC_except_table702
+ GCC_except_table7025
+ GCC_except_table7077
+ GCC_except_table7079
+ GCC_except_table7081
+ GCC_except_table7083
+ GCC_except_table7085
+ GCC_except_table7087
+ GCC_except_table7089
+ GCC_except_table709
+ GCC_except_table7091
+ GCC_except_table7094
+ GCC_except_table7096
+ GCC_except_table7098
+ GCC_except_table710
+ GCC_except_table7101
+ GCC_except_table7127
+ GCC_except_table7130
+ GCC_except_table7131
+ GCC_except_table7171
+ GCC_except_table7172
+ GCC_except_table7174
+ GCC_except_table7175
+ GCC_except_table7177
+ GCC_except_table7178
+ GCC_except_table7179
+ GCC_except_table7181
+ GCC_except_table7182
+ GCC_except_table7184
+ GCC_except_table7188
+ GCC_except_table7189
+ GCC_except_table7193
+ GCC_except_table7241
+ GCC_except_table7248
+ GCC_except_table7358
+ GCC_except_table7362
+ GCC_except_table7365
+ GCC_except_table7367
+ GCC_except_table7369
+ GCC_except_table7371
+ GCC_except_table7372
+ GCC_except_table7374
+ GCC_except_table7378
+ GCC_except_table7383
+ GCC_except_table744
+ GCC_except_table767
+ GCC_except_table785
+ GCC_except_table809
+ GCC_except_table813
+ GCC_except_table827
+ GCC_except_table832
+ GCC_except_table934
+ GCC_except_table936
+ _BonjourDevice_CopyDNSNames
+ _ConvertFromHAPIPStatusErrorCode
+ _HAPCharacteristicUUID_MatterFirmwareUpdateStatus
+ _HTTPClientSetClientContext
+ _HTTPClientSetConnectionProgressHandler
+ _OBJC_CLASS_$_HAPSRPPairSetupSession
+ _OBJC_IVAR_$_HAPAccessory._suspendCapable
+ _OBJC_IVAR_$_HAPAccessoryServerIP._currentPairVerifyError
+ _OBJC_IVAR_$_HAPAccessoryServerIP._triedConnectingToIPv4Address
+ _OBJC_IVAR_$_HAPAccessoryServerIP._triedConnectingToIPv6Address
+ _OBJC_IVAR_$_HAPCoreUtilsHTTPClient._isInvalidated
+ _OBJC_IVAR_$_HAPCoreUtilsHTTPClient._lock
+ _OBJC_IVAR_$_HAPMetricsPairVerifyEvent._triedConnectingToIPv4Address
+ _OBJC_IVAR_$_HAPMetricsPairVerifyEvent._triedConnectingToIPv6Address
+ _OBJC_IVAR_$_HAPSRPPairSetupSession._backoffTimer
+ _OBJC_IVAR_$_HAPSRPPairSetupSession._certificate
+ _OBJC_IVAR_$_HAPSRPPairSetupSession._clientQueue
+ _OBJC_IVAR_$_HAPSRPPairSetupSession._delegate
+ _OBJC_IVAR_$_HAPSRPPairSetupSession._handlingInvalidSetupCode
+ _OBJC_IVAR_$_HAPSRPPairSetupSession._pairSetupType
+ _OBJC_IVAR_$_HAPSRPPairSetupSession._pairingSession
+ _OBJC_IVAR_$_HAPSRPPairSetupSession._role
+ _OBJC_IVAR_$_HAPSRPPairSetupSession._sessionReadKey
+ _OBJC_IVAR_$_HAPSRPPairSetupSession._sessionReadNonce
+ _OBJC_IVAR_$_HAPSRPPairSetupSession._sessionWriteKey
+ _OBJC_IVAR_$_HAPSRPPairSetupSession._sessionWriteNonce
+ _OBJC_IVAR_$_HAPSRPPairSetupSession._state
+ _OBJC_METACLASS_$_HAPSRPPairSetupSession
+ __CopyPairingIdentityDelegateCallback_f.15065
+ __CopyPairingIdentityDelegateCallback_f.21655
+ __CopyPairingIdentityDelegateCallback_f.2732
+ __FindPairedPeerDelegateCallback_f.2731
+ __HandleConnectionProgress
+ __OBJC_$_CLASS_METHODS_HAP2AccessoryServerTransportCoAP
+ __OBJC_$_CLASS_METHODS_HAPSRPPairSetupSession
+ __OBJC_$_INSTANCE_METHODS_HAPSRPPairSetupSession
+ __OBJC_$_INSTANCE_VARIABLES_HAPSRPPairSetupSession
+ __OBJC_$_PROP_LIST_HAPCoreUtilsHTTPClient
+ __OBJC_$_PROP_LIST_HAPSRPPairSetupSession
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HAPPairSetupSession
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HAPPairSetupSession
+ __OBJC_$_PROTOCOL_REFS_HAPPairSetupSession
+ __OBJC_CLASS_PROTOCOLS_$_HAPSRPPairSetupSession
+ __OBJC_CLASS_RO_$_HAPSRPPairSetupSession
+ __OBJC_LABEL_PROTOCOL_$_HAPPairSetupSession
+ __OBJC_METACLASS_RO_$_HAPSRPPairSetupSession
+ __OBJC_PROTOCOL_$_HAPPairSetupSession
+ __PairSetupPromptForSetupCodeDelegateCallback_f.21657
+ __SavePairedPeerDelegateCallback_f.15063
+ __SavePairedPeerDelegateCallback_f.21652
+ ___106-[_HAPAccessoryServerBTLE200 removePairingForCurrentControllerOnQueue:completion:serverPairingCompletion:]_block_invoke.733
+ ___108-[HAPAccessoryServerIP _handleWriteECONNResetError:writeRequests:responses:timeout:queue:completionHandler:]_block_invoke.261
+ ___113-[HAPAccessoryServerIP _handleReadECONNRESETError:readCharacteristics:responses:timeout:queue:completionHandler:]_block_invoke.208
+ ___31-[HAPSRPPairSetupSession start]_block_invoke
+ ___37+[HAPSRPPairSetupSession logCategory]_block_invoke
+ ___40-[HAPSRPPairSetupSession getCertificate]_block_invoke
+ ___40-[HAPSRPPairSetupSession stopWithError:]_block_invoke
+ ___41-[HAPAccessoryServerIP getAccessoryInfo:]_block_invoke.516
+ ___41-[HAPSRPPairSetupSession isSecureSession]_block_invoke
+ ___44-[HAPAccessoryServerIP _pairVerifyStartWAC:]_block_invoke.119
+ ___45-[HAPAccessoryServerIP _pairSetupContinueWAC]_block_invoke.117
+ ___45-[HAPAccessoryServerIP stopPairingWithError:]_block_invoke.163
+ ___45-[HAPSRPPairSetupSession generateSessionKeys]_block_invoke
+ ___47-[HAPAccessoryServerIP identifyWithCompletion:]_block_invoke.645
+ ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.120
+ ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.121
+ ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.123
+ ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.126
+ ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke_2.122
+ ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke_2.125
+ ___48-[HAPAccessoryServerIP startPairingWithRequest:]_block_invoke.161
+ ___48-[HAPSRPPairSetupSession handleSetupCodeRequest]_block_invoke
+ ___48-[HAPSRPPairSetupSession handleSetupCodeRequest]_block_invoke_2
+ ___48-[HAPSRPPairSetupSession handleSetupCodeRequest]_block_invoke_3
+ ___49-[HAPAccessoryServerIP _continuePairingAfterWAC:]_block_invoke.127
+ ___49-[HAPAccessoryServerIP _continuePairingAfterWAC:]_block_invoke.132
+ ___49-[HAPAccessoryServerIP authSession:authComplete:]_block_invoke.562
+ ___50-[HAPAccessoryServerIP networkMonitorIsReachable:]_block_invoke.511
+ ___50-[_HAPAccessoryServerBTLE200 isReadyForOperation:]_block_invoke.832
+ ___51-[HAP2AccessoryServerTransportCoAP _resolveAddress]_block_invoke_2.59
+ ___52+[HAP2AccessoryServerTransportCoAP sortAddressList:]_block_invoke
+ ___53-[HAPAccessoryServerIP setPairVerifyCompletionBlock:]_block_invoke.417
+ ___53-[_HAPAccessoryServerBTLE200 identifyWithCompletion:]_block_invoke.756
+ ___53-[_HAPAccessoryServerBTLE200 identifyWithCompletion:]_block_invoke.763
+ ___55-[HAPAccessoryServerIP authSession:validateUUID:token:]_block_invoke.552
+ ___55-[HAPAccessoryServerIP authSession:validateUUID:token:]_block_invoke.557
+ ___55-[_HAPAccessoryServerBTLE200 authSession:authComplete:]_block_invoke.992
+ ___57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke.546
+ ___57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke_2.550
+ ___58-[HAPSRPPairSetupSession handleBackoffRequestWithTimeout:]_block_invoke
+ ___58-[HAPSRPPairSetupSession receivedSetupExchangeData:error:]_block_invoke
+ ___59-[HAPSRPPairSetupSession handleInvalidSetupCodeAndRestart:]_block_invoke
+ ___59-[_HAPAccessoryServerBTLE200 peripheral:didModifyServices:]_block_invoke.957
+ ___60-[HAPAccessoryServerIP _validatePairingAuthMethod:activity:]_block_invoke.530
+ ___60-[_HAPAccessoryServerBTLE200 continuePairingAfterAuthPrompt]_block_invoke.663
+ ___63-[_HAPAccessoryServerBTLE200 authSession:sendAuthExchangeData:]_block_invoke.985
+ ___63-[_HAPAccessoryServerBTLE200 authSession:sendAuthExchangeData:]_block_invoke_2.988
+ ___64-[HAPAccessoryServerIP httpClientDidCloseConnectionDueToServer:]_block_invoke.420
+ ___64-[_HAPAccessoryServerBTLE200 securitySession:didCloseWithError:]_block_invoke.1010
+ ___65-[HAPAccessoryServerBrowserIP wacBrowser:didFindHAPWACAccessory:]_block_invoke.72
+ ___66-[_HAPAccessoryServerBTLE200 _handlePairSetupSessionExchangeData:]_block_invoke.678
+ ___67-[HAPAccessoryServerBrowserIP wacBrowser:didRemoveHAPWACAccessory:]_block_invoke.73
+ ___67-[_HAPAccessoryServerBTLE200 _reallySendRequest:completionHandler:]_block_invoke.777
+ ___72-[HAPSRPPairSetupSession decryptData:additionalAuthenticatedData:error:]_block_invoke
+ ___72-[HAPSRPPairSetupSession encryptData:additionalAuthenticatedData:error:]_block_invoke
+ ___75-[_HAPAccessoryServerBTLE200 addPairing:completionQueue:completionHandler:]_block_invoke.700
+ ___75-[_HAPAccessoryServerBTLE200 addPairing:completionQueue:completionHandler:]_block_invoke.707
+ ___75-[_HAPAccessoryServerBTLE200 addPairing:completionQueue:completionHandler:]_block_invoke.711
+ ___75-[_HAPAccessoryServerBTLE200 addPairing:completionQueue:completionHandler:]_block_invoke_2.715
+ ___76-[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]_block_invoke.262
+ ___76-[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]_block_invoke.270
+ ___76-[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]_block_invoke_2.271
+ ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke.601
+ ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke.603
+ ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.602
+ ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.604
+ ___76-[_HAPAccessoryServerBTLE200 _sendRequest:shouldPrioritize:responseHandler:]_block_invoke.768
+ ___77-[_HAPAccessoryServerBTLE200 handleDisconnectionWithError:completionHandler:]_block_invoke.841
+ ___77-[_HAPAccessoryServerBTLE200 handleDisconnectionWithError:completionHandler:]_block_invoke.846
+ ___78-[_HAPAccessoryServerBTLE200 removePairing:completionQueue:completionHandler:]_block_invoke.717
+ ___78-[_HAPAccessoryServerBTLE200 removePairing:completionQueue:completionHandler:]_block_invoke.724
+ ___78-[_HAPAccessoryServerBTLE200 removePairing:completionQueue:completionHandler:]_block_invoke.728
+ ___78-[_HAPAccessoryServerBTLE200 removePairing:completionQueue:completionHandler:]_block_invoke_2.732
+ ___79-[HAPAccessoryServerIP _queueListPairingWithCompletionQueue:completionHandler:]_block_invoke.185
+ ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1273
+ ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1274
+ ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1276
+ ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke_2.1275
+ ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke_2.1277
+ ___79-[_HAPAccessoryServerBTLE200 generateBroadcastKey:queue:withCompletionHandler:]_block_invoke.853
+ ___80-[_HAPAccessoryServerBTLE200 _generateBroadcastKey:queue:withCompletionHandler:]_block_invoke.863
+ ___80-[_HAPAccessoryServerBTLE200 listPairingsWithCompletionQueue:completionHandler:]_block_invoke.735
+ ___80-[_HAPAccessoryServerBTLE200 listPairingsWithCompletionQueue:completionHandler:]_block_invoke.743
+ ___81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke.272
+ ___81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke.273
+ ___81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke_2.274
+ ___82-[HAPAccessoryServerBrowserBTLE removeRecentlySeenPairedPeripheralWithIdentifier:]_block_invoke
+ ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.209
+ ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.214
+ ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.223
+ ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.230
+ ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke_2.231
+ ___83-[HAPAccessory readCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.111
+ ___83-[HAPAccessory readCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.112
+ ___83-[HAPAccessory writeCharacteristicValue:timeout:completionQueue:completionHandler:]_block_invoke.116
+ ___83-[HAPAccessory writeCharacteristicValue:timeout:completionQueue:completionHandler:]_block_invoke.117
+ ___83-[HAPAccessoryServerBrowserIP wacBrowser:didFindUnconfiguredPairedHAPWACAccessory:]_block_invoke.76
+ ___83-[HAPAccessoryServerIP _writeCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.250
+ ___84-[HAPAccessory writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.127
+ ___84-[HAPAccessory writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.128
+ ___85-[HAPAccessory readValueForCharacteristic:timeout:completionQueue:completionHandler:]_block_invoke.90
+ ___85-[HAPAccessory readValueForCharacteristic:timeout:completionQueue:completionHandler:]_block_invoke.94
+ ___85-[HAPAccessoryServerIP _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.334
+ ___86-[HAPAccessoryServerIP _establishSecureConnectionAndFetchAttributeDatabaseWithReason:]_block_invoke.159
+ ___88-[HAPAccessoryServerIP _queueAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.184
+ ___88-[HAPAccessoryServerIP _startAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.576
+ ___90-[HAPAccessoryServerIP _queueEnableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.186
+ ___92-[HAPAccessoryServerIP writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.249
+ ___Block_byref_object_copy_.10528
+ ___Block_byref_object_copy_.10816
+ ___Block_byref_object_copy_.11652
+ ___Block_byref_object_copy_.11849
+ ___Block_byref_object_copy_.12910
+ ___Block_byref_object_copy_.13712
+ ___Block_byref_object_copy_.13940
+ ___Block_byref_object_copy_.14974
+ ___Block_byref_object_copy_.16985
+ ___Block_byref_object_copy_.17200
+ ___Block_byref_object_copy_.18189
+ ___Block_byref_object_copy_.18792
+ ___Block_byref_object_copy_.19881
+ ___Block_byref_object_copy_.2020
+ ___Block_byref_object_copy_.20686
+ ___Block_byref_object_copy_.24811
+ ___Block_byref_object_copy_.24977
+ ___Block_byref_object_copy_.2680
+ ___Block_byref_object_copy_.4239
+ ___Block_byref_object_copy_.5106
+ ___Block_byref_object_copy_.5370
+ ___Block_byref_object_copy_.5821
+ ___Block_byref_object_copy_.6456
+ ___Block_byref_object_copy_.6636
+ ___Block_byref_object_copy_.690
+ ___Block_byref_object_copy_.7429
+ ___Block_byref_object_copy_.8948
+ ___Block_byref_object_copy_.9265
+ ___Block_byref_object_copy_.9469
+ ___Block_byref_object_dispose_.10529
+ ___Block_byref_object_dispose_.10817
+ ___Block_byref_object_dispose_.11653
+ ___Block_byref_object_dispose_.11850
+ ___Block_byref_object_dispose_.12911
+ ___Block_byref_object_dispose_.13713
+ ___Block_byref_object_dispose_.13941
+ ___Block_byref_object_dispose_.14975
+ ___Block_byref_object_dispose_.16986
+ ___Block_byref_object_dispose_.17201
+ ___Block_byref_object_dispose_.18190
+ ___Block_byref_object_dispose_.18793
+ ___Block_byref_object_dispose_.19882
+ ___Block_byref_object_dispose_.2021
+ ___Block_byref_object_dispose_.20687
+ ___Block_byref_object_dispose_.24812
+ ___Block_byref_object_dispose_.24978
+ ___Block_byref_object_dispose_.2681
+ ___Block_byref_object_dispose_.4240
+ ___Block_byref_object_dispose_.5107
+ ___Block_byref_object_dispose_.5371
+ ___Block_byref_object_dispose_.5822
+ ___Block_byref_object_dispose_.6457
+ ___Block_byref_object_dispose_.6637
+ ___Block_byref_object_dispose_.691
+ ___Block_byref_object_dispose_.7430
+ ___Block_byref_object_dispose_.8949
+ ___Block_byref_object_dispose_.9266
+ ___Block_byref_object_dispose_.9470
+ ___block_descriptor_104_e8_32s40s48s56s64bs72bs80w88w_e5_v8?0lw80l8w88l8s32l8s40l8s64l8s48l8s56l8s72l8
+ ___block_descriptor_104_e8_32s40s48s56s64s72bs80bs88w_e5_v8?0lw88l8s32l8s40l8s48l8s72l8s56l8s64l8s80l8
+ ___block_descriptor_120_e8_32s40s48s56r64r72r80r88r_e5_v8?0ls32l8r56l8s40l8r64l8r72l8r80l8s48l8r88l8
+ ___block_descriptor_49_e8_32s40s_e39_v24?0"HAPCharacteristic"8"NSError"16ls32l8s40l8
+ ___block_descriptor_96_e8_32s40s48s56bs64bs72w80w_e5_v8?0lw72l8w80l8s32l8s40l8s56l8s48l8s64l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72bs80bs_e5_v8?0ls32l8s40l8s48l8s72l8s56l8s64l8s80l8
+ ___block_literal_global.1019
+ ___block_literal_global.10198
+ ___block_literal_global.10874
+ ___block_literal_global.11648
+ ___block_literal_global.12016
+ ___block_literal_global.1293
+ ___block_literal_global.13180
+ ___block_literal_global.1330
+ ___block_literal_global.15089
+ ___block_literal_global.1511
+ ___block_literal_global.15519
+ ___block_literal_global.16719
+ ___block_literal_global.16994
+ ___block_literal_global.18373
+ ___block_literal_global.1925
+ ___block_literal_global.193
+ ___block_literal_global.19628
+ ___block_literal_global.19903
+ ___block_literal_global.20345
+ ___block_literal_global.21312
+ ___block_literal_global.22647
+ ___block_literal_global.22982
+ ___block_literal_global.24584
+ ___block_literal_global.25198
+ ___block_literal_global.2750
+ ___block_literal_global.3692
+ ___block_literal_global.5190
+ ___block_literal_global.5366
+ ___block_literal_global.5920
+ ___block_literal_global.63
+ ___block_literal_global.6468
+ ___block_literal_global.6613
+ ___block_literal_global.759
+ ___block_literal_global.7686
+ ___block_literal_global.834
+ ___block_literal_global.8596
+ ___block_literal_global.9033
+ ___block_literal_global.9580
+ ___swift_reflection_version
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_CoreHAP
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_CoreHAP
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_CoreHAP
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_CoreHAP
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_CoreHAP
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_CoreHAP
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_CoreHAP
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_CoreHAP
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_CoreHAP
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_CoreHAP
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_CoreHAP
+ _hkConfig.21296
+ _logCategory._hmf_once_t141
+ _logCategory._hmf_once_t24
+ _logCategory._hmf_once_t333
+ _logCategory._hmf_once_t418
+ _logCategory._hmf_once_t51
+ _logCategory._hmf_once_v142
+ _logCategory._hmf_once_v25
+ _logCategory._hmf_once_v334
+ _logCategory._hmf_once_v419
+ _logCategory._hmf_once_v52
+ _objc_msgSend$_removeRecentlySeenPairedPeripheralWithIdentifier:
+ _objc_msgSend$address
+ _objc_msgSend$addressFamily
+ _objc_msgSend$currentPairVerifyError
+ _objc_msgSend$dnsNameForHTTPHeaderFromDNSNames:
+ _objc_msgSend$ensureNetworkMonitor
+ _objc_msgSend$hmf_enumerateWithAutoreleasePoolUsingBlock:
+ _objc_msgSend$hmf_isEqualToUUID:
+ _objc_msgSend$httpClient:didStartConnectingToNetAddress:
+ _objc_msgSend$initWithBytesNoCopy:length:encoding:freeWhenDone:
+ _objc_msgSend$isHAPOperationDelayed
+ _objc_msgSend$isInvalidated
+ _objc_msgSend$isSeenOnBonjour
+ _objc_msgSend$pairSetupSession:pairSetupType:features:
+ _objc_msgSend$removeRecentlySeenPairedPeripheralWithIdentifier:
+ _objc_msgSend$setConnectionProgressHandler:context:
+ _objc_msgSend$setContext:
+ _objc_msgSend$setCurrentPairVerifyError:
+ _objc_msgSend$setIsInvalidated:
+ _objc_msgSend$setTriedConnectingToIPv4Address:
+ _objc_msgSend$setTriedConnectingToIPv6Address:
+ _objc_msgSend$sortAddressList:
+ _objc_msgSend$suspendCapable
+ _objc_msgSend$triedConnectingToIPv4Address
+ _objc_msgSend$triedConnectingToIPv6Address
+ _sharedInstance.onceToken.15518
- +[HAPPairSetupSession initialize]
- +[HAPPairSetupSession isValidSetupCode:]
- +[HAPPairSetupSession logCategory]
- -[HAP2AccessoryDeviceIPAddress getAddressPtr]
- -[HAPAccessoryServerIP checkIfSuspendedAccesoryRediscovered]
- -[HAPAccessoryServerIP setCheckIfSuspendedAccesoryRediscovered:]
- -[HAPPairSetupSession .cxx_destruct]
- -[HAPPairSetupSession _handleBackoffExpiration]
- -[HAPPairSetupSession _handleLocalPairingIdentityRequestWithStatus:]
- -[HAPPairSetupSession _handlePairSetupExchangeComplete]
- -[HAPPairSetupSession _handleProductData:]
- -[HAPPairSetupSession _initializeServer]
- -[HAPPairSetupSession _initializeSession]
- -[HAPPairSetupSession _initiateClientPairSetupExchange]
- -[HAPPairSetupSession _invalidate]
- -[HAPPairSetupSession _processSetupCode:error:]
- -[HAPPairSetupSession _processSetupExchangeData:error:]
- -[HAPPairSetupSession _showSetupCodeWithError:]
- -[HAPPairSetupSession _stopWithError:]
- -[HAPPairSetupSession backoffTimer]
- -[HAPPairSetupSession certificate]
- -[HAPPairSetupSession clientQueue]
- -[HAPPairSetupSession dealloc]
- -[HAPPairSetupSession debugDescription]
- -[HAPPairSetupSession decryptData:additionalAuthenticatedData:error:]
- -[HAPPairSetupSession delegate]
- -[HAPPairSetupSession descriptionWithPointer:]
- -[HAPPairSetupSession description]
- -[HAPPairSetupSession encryptData:additionalAuthenticatedData:error:]
- -[HAPPairSetupSession generateSessionKeys]
- -[HAPPairSetupSession getCertificate]
- -[HAPPairSetupSession handleBackoffRequestWithTimeout:]
- -[HAPPairSetupSession handleInvalidSetupCodeAndRestart:]
- -[HAPPairSetupSession handleSavePeerRequestWithPeerIdentity:error:]
- -[HAPPairSetupSession handleSetupCodeRequest]
- -[HAPPairSetupSession initWithRole:pairSetupType:delegate:]
- -[HAPPairSetupSession init]
- -[HAPPairSetupSession isHandlingInvalidSetupCode]
- -[HAPPairSetupSession isSecureSession]
- -[HAPPairSetupSession logIdentifier]
- -[HAPPairSetupSession pairSetupType]
- -[HAPPairSetupSession pairingSession]
- -[HAPPairSetupSession receivedSetupExchangeData:error:]
- -[HAPPairSetupSession role]
- -[HAPPairSetupSession sessionReadKey]
- -[HAPPairSetupSession sessionReadNonce]
- -[HAPPairSetupSession sessionWriteKey]
- -[HAPPairSetupSession sessionWriteNonce]
- -[HAPPairSetupSession setBackoffTimer:]
- -[HAPPairSetupSession setCertificate:]
- -[HAPPairSetupSession setHandlingInvalidSetupCode:]
- -[HAPPairSetupSession setPairSetupType:]
- -[HAPPairSetupSession setSessionReadKey:]
- -[HAPPairSetupSession setSessionReadNonce:]
- -[HAPPairSetupSession setSessionWriteKey:]
- -[HAPPairSetupSession setSessionWriteNonce:]
- -[HAPPairSetupSession setState:]
- -[HAPPairSetupSession shortDescription]
- -[HAPPairSetupSession start]
- -[HAPPairSetupSession state]
- -[HAPPairSetupSession stopWithError:]
- -[HAPPairSetupSession stop]
- -[HAPPairSetupSession timerDidFire:]
- GCC_except_table1035
- GCC_except_table1039
- GCC_except_table1052
- GCC_except_table1057
- GCC_except_table1066
- GCC_except_table1068
- GCC_except_table1070
- GCC_except_table1072
- GCC_except_table1198
- GCC_except_table1202
- GCC_except_table1204
- GCC_except_table1416
- GCC_except_table1622
- GCC_except_table1625
- GCC_except_table1633
- GCC_except_table1635
- GCC_except_table1641
- GCC_except_table1643
- GCC_except_table1647
- GCC_except_table1651
- GCC_except_table1653
- GCC_except_table1662
- GCC_except_table1672
- GCC_except_table1680
- GCC_except_table1691
- GCC_except_table1695
- GCC_except_table1699
- GCC_except_table1701
- GCC_except_table1850
- GCC_except_table1854
- GCC_except_table1855
- GCC_except_table1859
- GCC_except_table1868
- GCC_except_table1870
- GCC_except_table1874
- GCC_except_table1879
- GCC_except_table1882
- GCC_except_table1899
- GCC_except_table1902
- GCC_except_table1904
- GCC_except_table1910
- GCC_except_table1919
- GCC_except_table1922
- GCC_except_table1925
- GCC_except_table1927
- GCC_except_table1933
- GCC_except_table1937
- GCC_except_table1945
- GCC_except_table1956
- GCC_except_table1994
- GCC_except_table2000
- GCC_except_table2171
- GCC_except_table2184
- GCC_except_table2190
- GCC_except_table2193
- GCC_except_table2196
- GCC_except_table2199
- GCC_except_table2205
- GCC_except_table2207
- GCC_except_table2211
- GCC_except_table2310
- GCC_except_table2318
- GCC_except_table2319
- GCC_except_table2320
- GCC_except_table2321
- GCC_except_table2322
- GCC_except_table2323
- GCC_except_table2338
- GCC_except_table2352
- GCC_except_table2429
- GCC_except_table2441
- GCC_except_table2467
- GCC_except_table2475
- GCC_except_table2486
- GCC_except_table2500
- GCC_except_table2503
- GCC_except_table2508
- GCC_except_table2516
- GCC_except_table2522
- GCC_except_table2524
- GCC_except_table2698
- GCC_except_table2748
- GCC_except_table2764
- GCC_except_table2767
- GCC_except_table2781
- GCC_except_table2782
- GCC_except_table2789
- GCC_except_table2804
- GCC_except_table2816
- GCC_except_table2817
- GCC_except_table2819
- GCC_except_table2825
- GCC_except_table2832
- GCC_except_table2840
- GCC_except_table2896
- GCC_except_table2899
- GCC_except_table2904
- GCC_except_table2920
- GCC_except_table2934
- GCC_except_table2936
- GCC_except_table2940
- GCC_except_table2948
- GCC_except_table2956
- GCC_except_table3005
- GCC_except_table3013
- GCC_except_table3016
- GCC_except_table3039
- GCC_except_table3283
- GCC_except_table3346
- GCC_except_table3347
- GCC_except_table3351
- GCC_except_table3354
- GCC_except_table3356
- GCC_except_table3359
- GCC_except_table3360
- GCC_except_table3369
- GCC_except_table3379
- GCC_except_table3382
- GCC_except_table3394
- GCC_except_table3396
- GCC_except_table3398
- GCC_except_table3401
- GCC_except_table3406
- GCC_except_table3424
- GCC_except_table3426
- GCC_except_table3430
- GCC_except_table3434
- GCC_except_table3438
- GCC_except_table3464
- GCC_except_table3482
- GCC_except_table3486
- GCC_except_table3489
- GCC_except_table3491
- GCC_except_table3614
- GCC_except_table3640
- GCC_except_table3732
- GCC_except_table3739
- GCC_except_table3757
- GCC_except_table3761
- GCC_except_table3764
- GCC_except_table3767
- GCC_except_table3770
- GCC_except_table3773
- GCC_except_table3776
- GCC_except_table3779
- GCC_except_table3782
- GCC_except_table3785
- GCC_except_table3801
- GCC_except_table3823
- GCC_except_table3827
- GCC_except_table3834
- GCC_except_table3835
- GCC_except_table3839
- GCC_except_table3840
- GCC_except_table3858
- GCC_except_table3860
- GCC_except_table3862
- GCC_except_table3863
- GCC_except_table3866
- GCC_except_table3875
- GCC_except_table3883
- GCC_except_table3885
- GCC_except_table3888
- GCC_except_table3900
- GCC_except_table3911
- GCC_except_table3913
- GCC_except_table3922
- GCC_except_table3928
- GCC_except_table398
- GCC_except_table414
- GCC_except_table4188
- GCC_except_table4194
- GCC_except_table4211
- GCC_except_table4215
- GCC_except_table422
- GCC_except_table4232
- GCC_except_table4238
- GCC_except_table4251
- GCC_except_table4269
- GCC_except_table4382
- GCC_except_table4462
- GCC_except_table4470
- GCC_except_table4480
- GCC_except_table4517
- GCC_except_table452
- GCC_except_table4520
- GCC_except_table4521
- GCC_except_table4522
- GCC_except_table4523
- GCC_except_table459
- GCC_except_table4619
- GCC_except_table4620
- GCC_except_table4621
- GCC_except_table4622
- GCC_except_table4623
- GCC_except_table4624
- GCC_except_table4630
- GCC_except_table4631
- GCC_except_table4633
- GCC_except_table4643
- GCC_except_table4645
- GCC_except_table4650
- GCC_except_table4653
- GCC_except_table4660
- GCC_except_table4664
- GCC_except_table4693
- GCC_except_table4694
- GCC_except_table4713
- GCC_except_table4723
- GCC_except_table4726
- GCC_except_table473
- GCC_except_table4731
- GCC_except_table4734
- GCC_except_table474
- GCC_except_table476
- GCC_except_table479
- GCC_except_table482
- GCC_except_table494
- GCC_except_table498
- GCC_except_table4996
- GCC_except_table5000
- GCC_except_table5034
- GCC_except_table5038
- GCC_except_table5040
- GCC_except_table5042
- GCC_except_table514
- GCC_except_table5199
- GCC_except_table5205
- GCC_except_table5209
- GCC_except_table5210
- GCC_except_table5211
- GCC_except_table5212
- GCC_except_table5218
- GCC_except_table5252
- GCC_except_table5253
- GCC_except_table5254
- GCC_except_table5274
- GCC_except_table5286
- GCC_except_table5289
- GCC_except_table5294
- GCC_except_table5296
- GCC_except_table5310
- GCC_except_table537
- GCC_except_table547
- GCC_except_table5512
- GCC_except_table5524
- GCC_except_table5529
- GCC_except_table5532
- GCC_except_table5533
- GCC_except_table5535
- GCC_except_table5536
- GCC_except_table5538
- GCC_except_table554
- GCC_except_table5568
- GCC_except_table5590
- GCC_except_table5594
- GCC_except_table5598
- GCC_except_table5603
- GCC_except_table5607
- GCC_except_table5611
- GCC_except_table5615
- GCC_except_table5619
- GCC_except_table5627
- GCC_except_table5631
- GCC_except_table5691
- GCC_except_table5692
- GCC_except_table5693
- GCC_except_table5694
- GCC_except_table5752
- GCC_except_table5753
- GCC_except_table5767
- GCC_except_table5786
- GCC_except_table5789
- GCC_except_table5790
- GCC_except_table5795
- GCC_except_table5798
- GCC_except_table5805
- GCC_except_table5808
- GCC_except_table581
- GCC_except_table5822
- GCC_except_table5829
- GCC_except_table5835
- GCC_except_table5844
- GCC_except_table5846
- GCC_except_table585
- GCC_except_table5850
- GCC_except_table5851
- GCC_except_table5868
- GCC_except_table587
- GCC_except_table5876
- GCC_except_table589
- GCC_except_table5891
- GCC_except_table5892
- GCC_except_table5897
- GCC_except_table5901
- GCC_except_table5902
- GCC_except_table5905
- GCC_except_table5915
- GCC_except_table5919
- GCC_except_table5923
- GCC_except_table595
- GCC_except_table597
- GCC_except_table6068
- GCC_except_table609
- GCC_except_table6124
- GCC_except_table6127
- GCC_except_table613
- GCC_except_table6131
- GCC_except_table6137
- GCC_except_table6144
- GCC_except_table6145
- GCC_except_table6161
- GCC_except_table6165
- GCC_except_table617
- GCC_except_table6215
- GCC_except_table6216
- GCC_except_table6218
- GCC_except_table6221
- GCC_except_table6249
- GCC_except_table6250
- GCC_except_table6255
- GCC_except_table627
- GCC_except_table6275
- GCC_except_table6292
- GCC_except_table6293
- GCC_except_table6294
- GCC_except_table6302
- GCC_except_table6307
- GCC_except_table6308
- GCC_except_table6309
- GCC_except_table632
- GCC_except_table6323
- GCC_except_table6326
- GCC_except_table6332
- GCC_except_table6338
- GCC_except_table6350
- GCC_except_table6351
- GCC_except_table6356
- GCC_except_table6365
- GCC_except_table6371
- GCC_except_table6376
- GCC_except_table638
- GCC_except_table6384
- GCC_except_table6388
- GCC_except_table6390
- GCC_except_table6415
- GCC_except_table6417
- GCC_except_table6418
- GCC_except_table643
- GCC_except_table6444
- GCC_except_table653
- GCC_except_table654
- GCC_except_table659
- GCC_except_table660
- GCC_except_table6608
- GCC_except_table6671
- GCC_except_table6703
- GCC_except_table6706
- GCC_except_table686
- GCC_except_table6870
- GCC_except_table693
- GCC_except_table6933
- GCC_except_table6997
- GCC_except_table700
- GCC_except_table7003
- GCC_except_table701
- GCC_except_table7048
- GCC_except_table7050
- GCC_except_table7052
- GCC_except_table7054
- GCC_except_table7056
- GCC_except_table7058
- GCC_except_table7060
- GCC_except_table7062
- GCC_except_table7064
- GCC_except_table7066
- GCC_except_table7068
- GCC_except_table7078
- GCC_except_table7104
- GCC_except_table7107
- GCC_except_table7108
- GCC_except_table7147
- GCC_except_table7148
- GCC_except_table7149
- GCC_except_table7151
- GCC_except_table7152
- GCC_except_table7154
- GCC_except_table7155
- GCC_except_table7156
- GCC_except_table7158
- GCC_except_table7159
- GCC_except_table7161
- GCC_except_table7165
- GCC_except_table7166
- GCC_except_table7218
- GCC_except_table7225
- GCC_except_table7319
- GCC_except_table7335
- GCC_except_table7337
- GCC_except_table7339
- GCC_except_table7344
- GCC_except_table7346
- GCC_except_table7348
- GCC_except_table7349
- GCC_except_table735
- GCC_except_table7351
- GCC_except_table7355
- GCC_except_table758
- GCC_except_table778
- GCC_except_table802
- GCC_except_table806
- GCC_except_table820
- GCC_except_table825
- GCC_except_table927
- GCC_except_table929
- _BonjourDevice_GetDNSName
- _HMErrorFromHAPIPStatusErrorCode
- _OBJC_CLASS_$_HAPPairSetupSession
- _OBJC_IVAR_$_HAPAccessoryServerIP._checkIfSuspendedAccesoryRediscovered
- _OBJC_IVAR_$_HAPPairSetupSession._backoffTimer
- _OBJC_IVAR_$_HAPPairSetupSession._certificate
- _OBJC_IVAR_$_HAPPairSetupSession._clientQueue
- _OBJC_IVAR_$_HAPPairSetupSession._delegate
- _OBJC_IVAR_$_HAPPairSetupSession._handlingInvalidSetupCode
- _OBJC_IVAR_$_HAPPairSetupSession._pairSetupType
- _OBJC_IVAR_$_HAPPairSetupSession._pairingSession
- _OBJC_IVAR_$_HAPPairSetupSession._role
- _OBJC_IVAR_$_HAPPairSetupSession._sessionReadKey
- _OBJC_IVAR_$_HAPPairSetupSession._sessionReadNonce
- _OBJC_IVAR_$_HAPPairSetupSession._sessionWriteKey
- _OBJC_IVAR_$_HAPPairSetupSession._sessionWriteNonce
- _OBJC_IVAR_$_HAPPairSetupSession._state
- _OBJC_METACLASS_$_HAPPairSetupSession
- __CopyPairingIdentityDelegateCallback_f.14973
- __CopyPairingIdentityDelegateCallback_f.21540
- __CopyPairingIdentityDelegateCallback_f.2710
- __FindPairedPeerDelegateCallback_f.2709
- __OBJC_$_CLASS_METHODS_HAPPairSetupSession
- __OBJC_$_INSTANCE_METHODS_HAPPairSetupSession
- __OBJC_$_INSTANCE_VARIABLES_HAPPairSetupSession
- __OBJC_$_PROP_LIST_HAPPairSetupSession
- __OBJC_CLASS_PROTOCOLS_$_HAPPairSetupSession
- __OBJC_CLASS_RO_$_HAPPairSetupSession
- __OBJC_METACLASS_RO_$_HAPPairSetupSession
- __PairSetupPromptForSetupCodeDelegateCallback_f.21542
- __SavePairedPeerDelegateCallback_f.14972
- __SavePairedPeerDelegateCallback_f.21535
- ___106-[_HAPAccessoryServerBTLE200 removePairingForCurrentControllerOnQueue:completion:serverPairingCompletion:]_block_invoke.735
- ___108-[HAPAccessoryServerIP _handleWriteECONNResetError:writeRequests:responses:timeout:queue:completionHandler:]_block_invoke.265
- ___113-[HAPAccessoryServerIP _handleReadECONNRESETError:readCharacteristics:responses:timeout:queue:completionHandler:]_block_invoke.212
- ___28-[HAPPairSetupSession start]_block_invoke
- ___34+[HAPPairSetupSession logCategory]_block_invoke
- ___37-[HAPPairSetupSession getCertificate]_block_invoke
- ___37-[HAPPairSetupSession stopWithError:]_block_invoke
- ___38-[HAPPairSetupSession isSecureSession]_block_invoke
- ___41-[HAPAccessoryServerIP getAccessoryInfo:]_block_invoke.510
- ___42-[HAPPairSetupSession generateSessionKeys]_block_invoke
- ___44-[HAPAccessoryServerIP _pairVerifyStartWAC:]_block_invoke.123
- ___45-[HAPAccessoryServerIP _pairSetupContinueWAC]_block_invoke.121
- ___45-[HAPAccessoryServerIP stopPairingWithError:]_block_invoke.167
- ___45-[HAPPairSetupSession handleSetupCodeRequest]_block_invoke
- ___45-[HAPPairSetupSession handleSetupCodeRequest]_block_invoke_2
- ___45-[HAPPairSetupSession handleSetupCodeRequest]_block_invoke_3
- ___47-[HAPAccessoryServerIP identifyWithCompletion:]_block_invoke.641
- ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.125
- ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.127
- ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.128
- ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke.130
- ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke_2.126
- ___48-[HAPAccessoryServerIP _continuePairingUsingWAC]_block_invoke_2.129
- ___48-[HAPAccessoryServerIP startPairingWithRequest:]_block_invoke.165
- ___49-[HAPAccessoryServerIP _continuePairingAfterWAC:]_block_invoke.131
- ___49-[HAPAccessoryServerIP _continuePairingAfterWAC:]_block_invoke.136
- ___49-[HAPAccessoryServerIP authSession:authComplete:]_block_invoke.555
- ___50-[HAPAccessoryServerIP networkMonitorIsReachable:]_block_invoke.505
- ___50-[_HAPAccessoryServerBTLE200 isReadyForOperation:]_block_invoke.833
- ___51-[HAP2AccessoryServerTransportCoAP _resolveAddress]_block_invoke_2.56
- ___51-[HAP2AccessoryServerTransportCoAP _resolveAddress]_block_invoke_3
- ___53-[HAPAccessoryServerIP setPairVerifyCompletionBlock:]_block_invoke.421
- ___53-[_HAPAccessoryServerBTLE200 identifyWithCompletion:]_block_invoke.757
- ___53-[_HAPAccessoryServerBTLE200 identifyWithCompletion:]_block_invoke.764
- ___55-[HAPAccessoryServerIP authSession:validateUUID:token:]_block_invoke.545
- ___55-[HAPAccessoryServerIP authSession:validateUUID:token:]_block_invoke.550
- ___55-[HAPPairSetupSession handleBackoffRequestWithTimeout:]_block_invoke
- ___55-[HAPPairSetupSession receivedSetupExchangeData:error:]_block_invoke
- ___55-[_HAPAccessoryServerBTLE200 authSession:authComplete:]_block_invoke.993
- ___56-[HAPPairSetupSession handleInvalidSetupCodeAndRestart:]_block_invoke
- ___57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke.540
- ___57-[HAPAccessoryServerIP authSession:sendAuthExchangeData:]_block_invoke_2.544
- ___59-[_HAPAccessoryServerBTLE200 peripheral:didModifyServices:]_block_invoke.958
- ___60-[HAPAccessoryServerIP _validatePairingAuthMethod:activity:]_block_invoke.524
- ___60-[_HAPAccessoryServerBTLE200 continuePairingAfterAuthPrompt]_block_invoke.664
- ___63-[_HAPAccessoryServerBTLE200 authSession:sendAuthExchangeData:]_block_invoke.986
- ___63-[_HAPAccessoryServerBTLE200 authSession:sendAuthExchangeData:]_block_invoke_2.989
- ___64-[_HAPAccessoryServerBTLE200 securitySession:didCloseWithError:]_block_invoke.1011
- ___65-[HAPAccessoryServerBrowserIP wacBrowser:didFindHAPWACAccessory:]_block_invoke.73
- ___66-[_HAPAccessoryServerBTLE200 _handlePairSetupSessionExchangeData:]_block_invoke.679
- ___67-[HAPAccessoryServerBrowserIP wacBrowser:didRemoveHAPWACAccessory:]_block_invoke.74
- ___67-[_HAPAccessoryServerBTLE200 _reallySendRequest:completionHandler:]_block_invoke.778
- ___69-[HAPPairSetupSession decryptData:additionalAuthenticatedData:error:]_block_invoke
- ___69-[HAPPairSetupSession encryptData:additionalAuthenticatedData:error:]_block_invoke
- ___75-[_HAPAccessoryServerBTLE200 addPairing:completionQueue:completionHandler:]_block_invoke.701
- ___75-[_HAPAccessoryServerBTLE200 addPairing:completionQueue:completionHandler:]_block_invoke.708
- ___75-[_HAPAccessoryServerBTLE200 addPairing:completionQueue:completionHandler:]_block_invoke.712
- ___75-[_HAPAccessoryServerBTLE200 addPairing:completionQueue:completionHandler:]_block_invoke_2.716
- ___76-[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]_block_invoke.266
- ___76-[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]_block_invoke_2.274
- ___76-[HAPAccessoryServerIP _performWriteValues:timeout:queue:completionHandler:]_block_invoke_3.275
- ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke.597
- ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke.599
- ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.598
- ___76-[HAPAccessoryServerIP removePairingForCurrentControllerOnQueue:completion:]_block_invoke_2.600
- ___76-[_HAPAccessoryServerBTLE200 _sendRequest:shouldPrioritize:responseHandler:]_block_invoke.769
- ___77-[_HAPAccessoryServerBTLE200 handleDisconnectionWithError:completionHandler:]_block_invoke.842
- ___77-[_HAPAccessoryServerBTLE200 handleDisconnectionWithError:completionHandler:]_block_invoke.847
- ___78-[_HAPAccessoryServerBTLE200 removePairing:completionQueue:completionHandler:]_block_invoke.718
- ___78-[_HAPAccessoryServerBTLE200 removePairing:completionQueue:completionHandler:]_block_invoke.725
- ___78-[_HAPAccessoryServerBTLE200 removePairing:completionQueue:completionHandler:]_block_invoke.729
- ___78-[_HAPAccessoryServerBTLE200 removePairing:completionQueue:completionHandler:]_block_invoke_2.733
- ___79-[HAPAccessoryServerIP _queueListPairingWithCompletionQueue:completionHandler:]_block_invoke.189
- ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1255
- ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke.1256
- ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke_2.1257
- ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke_3
- ___79-[HAPAccessoryServerIP(HTTPActivity) _requestResource:queue:completionHandler:]_block_invoke_4
- ___79-[_HAPAccessoryServerBTLE200 generateBroadcastKey:queue:withCompletionHandler:]_block_invoke.854
- ___80-[_HAPAccessoryServerBTLE200 _generateBroadcastKey:queue:withCompletionHandler:]_block_invoke.864
- ___80-[_HAPAccessoryServerBTLE200 listPairingsWithCompletionQueue:completionHandler:]_block_invoke.737
- ___80-[_HAPAccessoryServerBTLE200 listPairingsWithCompletionQueue:completionHandler:]_block_invoke.744
- ___81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke.276
- ___81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke_2.277
- ___81-[HAPAccessoryServerIP _performTimedWriteValues:timeout:queue:completionHandler:]_block_invoke_3.278
- ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.213
- ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.218
- ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.227
- ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke_2.234
- ___82-[HAPAccessoryServerIP _readCharacteristicValues:timeout:queue:completionHandler:]_block_invoke_3.235
- ___83-[HAPAccessory readCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.105
- ___83-[HAPAccessory readCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.106
- ___83-[HAPAccessory writeCharacteristicValue:timeout:completionQueue:completionHandler:]_block_invoke.110
- ___83-[HAPAccessory writeCharacteristicValue:timeout:completionQueue:completionHandler:]_block_invoke.111
- ___83-[HAPAccessoryServerBrowserIP wacBrowser:didFindUnconfiguredPairedHAPWACAccessory:]_block_invoke.77
- ___83-[HAPAccessoryServerIP _writeCharacteristicValues:timeout:queue:completionHandler:]_block_invoke.254
- ___84-[HAPAccessory writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.121
- ___84-[HAPAccessory writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.122
- ___85-[HAPAccessory readValueForCharacteristic:timeout:completionQueue:completionHandler:]_block_invoke.84
- ___85-[HAPAccessory readValueForCharacteristic:timeout:completionQueue:completionHandler:]_block_invoke.88
- ___85-[HAPAccessoryServerIP _enableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.342
- ___86-[HAPAccessoryServerIP _establishSecureConnectionAndFetchAttributeDatabaseWithReason:]_block_invoke.163
- ___87-[HAPAccessoryServerBrowserIP _handleConnectionUpdateWithBonjourDeviceInfo:socketInfo:]_block_invoke.64
- ___88-[HAPAccessoryServerIP _queueAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.188
- ___88-[HAPAccessoryServerIP _startAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke.569
- ___90-[HAPAccessoryServerIP _queueEnableEvents:forCharacteristics:withCompletionHandler:queue:]_block_invoke.190
- ___92-[HAPAccessoryServerIP writeCharacteristicValues:timeout:completionQueue:completionHandler:]_block_invoke.253
- ___Block_byref_object_copy_.10487
- ___Block_byref_object_copy_.10767
- ___Block_byref_object_copy_.11590
- ___Block_byref_object_copy_.11787
- ___Block_byref_object_copy_.12851
- ___Block_byref_object_copy_.13647
- ___Block_byref_object_copy_.13875
- ___Block_byref_object_copy_.14884
- ___Block_byref_object_copy_.16874
- ___Block_byref_object_copy_.17086
- ___Block_byref_object_copy_.18073
- ___Block_byref_object_copy_.18675
- ___Block_byref_object_copy_.19762
- ___Block_byref_object_copy_.1992
- ___Block_byref_object_copy_.20568
- ___Block_byref_object_copy_.24691
- ___Block_byref_object_copy_.24856
- ___Block_byref_object_copy_.2658
- ___Block_byref_object_copy_.4214
- ___Block_byref_object_copy_.5078
- ___Block_byref_object_copy_.5338
- ___Block_byref_object_copy_.5791
- ___Block_byref_object_copy_.6435
- ___Block_byref_object_copy_.6614
- ___Block_byref_object_copy_.687
- ___Block_byref_object_copy_.7409
- ___Block_byref_object_copy_.8936
- ___Block_byref_object_copy_.9251
- ___Block_byref_object_copy_.9446
- ___Block_byref_object_dispose_.10488
- ___Block_byref_object_dispose_.10768
- ___Block_byref_object_dispose_.11591
- ___Block_byref_object_dispose_.11788
- ___Block_byref_object_dispose_.12852
- ___Block_byref_object_dispose_.13648
- ___Block_byref_object_dispose_.13876
- ___Block_byref_object_dispose_.14885
- ___Block_byref_object_dispose_.16875
- ___Block_byref_object_dispose_.17087
- ___Block_byref_object_dispose_.18074
- ___Block_byref_object_dispose_.18676
- ___Block_byref_object_dispose_.19763
- ___Block_byref_object_dispose_.1993
- ___Block_byref_object_dispose_.20569
- ___Block_byref_object_dispose_.24692
- ___Block_byref_object_dispose_.24857
- ___Block_byref_object_dispose_.2659
- ___Block_byref_object_dispose_.4215
- ___Block_byref_object_dispose_.5079
- ___Block_byref_object_dispose_.5339
- ___Block_byref_object_dispose_.5792
- ___Block_byref_object_dispose_.6436
- ___Block_byref_object_dispose_.6615
- ___Block_byref_object_dispose_.688
- ___Block_byref_object_dispose_.7410
- ___Block_byref_object_dispose_.8937
- ___Block_byref_object_dispose_.9252
- ___Block_byref_object_dispose_.9447
- ___block_descriptor_57_e8_32s40s48s_e39_v24?0"HAPCharacteristic"8"NSError"16ls32l8s40l8s48l8
- ___block_descriptor_80_e8_32s40s48bs56w64w_e5_v8?0lw56l8w64l8s32l8s40l8s48l8
- ___block_descriptor_88_e8_32s40s48s56bs64w72w_e5_v8?0lw64l8w72l8s32l8s40l8s48l8s56l8
- ___block_descriptor_88_e8_32s40s48s56s64bs72w_e5_v8?0lw72l8s32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_96_e8_32s40s48s56r64r_e5_v8?0ls32l8r56l8s40l8s48l8r64l8
- ___block_literal_global.10159
- ___block_literal_global.1020
- ___block_literal_global.10822
- ___block_literal_global.11586
- ___block_literal_global.11958
- ___block_literal_global.1273
- ___block_literal_global.1310
- ___block_literal_global.13126
- ___block_literal_global.14989
- ___block_literal_global.1512
- ___block_literal_global.15413
- ___block_literal_global.16609
- ___block_literal_global.16883
- ___block_literal_global.18255
- ___block_literal_global.1897
- ___block_literal_global.19509
- ___block_literal_global.197
- ___block_literal_global.19786
- ___block_literal_global.20234
- ___block_literal_global.21192
- ___block_literal_global.22530
- ___block_literal_global.22864
- ___block_literal_global.24464
- ___block_literal_global.25078
- ___block_literal_global.2725
- ___block_literal_global.3669
- ___block_literal_global.5161
- ___block_literal_global.5334
- ___block_literal_global.55
- ___block_literal_global.5894
- ___block_literal_global.6446
- ___block_literal_global.6591
- ___block_literal_global.7663
- ___block_literal_global.769
- ___block_literal_global.835
- ___block_literal_global.8563
- ___block_literal_global.9020
- ___block_literal_global.9555
- _hkConfig.21176
- _logCategory._hmf_once_t140
- _logCategory._hmf_once_t23
- _logCategory._hmf_once_t332
- _logCategory._hmf_once_t412
- _logCategory._hmf_once_t52
- _logCategory._hmf_once_v141
- _logCategory._hmf_once_v24
- _logCategory._hmf_once_v333
- _logCategory._hmf_once_v413
- _logCategory._hmf_once_v53
- _objc_msgSend$checkIfSuspendedAccesoryRediscovered
- _objc_msgSend$getAddressPtr
- _objc_msgSend$setCheckIfSuspendedAccesoryRediscovered:
- _sharedInstance.onceToken.15412
CStrings:
+ "%c"
+ "%{public}@CopyDNSNames failed with error: %d"
+ "%{public}@Failed to initialize string with dns name: %s"
+ "%{public}@Failed to request resource because the accessory sent an invalid response with HTTP Status Code '%{public}d %{public}s' and a %{public}@ body: %{public}@"
+ "%{public}@Network is available"
+ "%{public}@Network is unavailable"
+ "%{public}@Removed recently seen paired peripheral with identifier %{public}@"
+ "%{public}@Resource request returned HTTP client error: %@"
+ "%{public}@Saving accessory cache with identifier: %@"
+ "%{public}@Secure session has been lost since this operation was staged. Canceling operation and re-queueing read."
+ "%{public}@Secure session has been lost since this operation was staged. Canceling operation and re-queueing timed write."
+ "%{public}@Secure session has been lost since this operation was staged. Canceling operation and re-queueing write."
+ "%{public}@Unknown Phase in HandleConnectionProgress: %d"
+ "%{public}@Unknown address family in net address: %@, %lu"
+ "%{public}@Updating peripheral [%@] keychain:\n peripheralIdentifier from %{public}@ to %{public}@,\n protocolVersion from %lu to %lu,\n resumeSessionID from %llu to %llu."
+ "%{public}@[LPM] Suspend Capable Accessory: Disconnected -> Entering suspended mode"
+ "%{public}@[LPM] Suspend Capable Accessory: Unexpected disconnect"
+ "00000221-0000-1000-8000-0026BB765291"
+ "00000251-0000-1000-8000-0026BB765291"
+ "0000026E-0000-1000-8000-0026BB765291"
+ "<%s>"
+ "@\"<HAPPairSetupSession>\""
+ "@\"HAPPairSetupSessionServerInfo\"24@0:8@\"<HAPPairSetupSession>\"16"
+ "@\"HAPPairingIdentity\"32@0:8@\"<HAPPairSetupSession>\"16^@24"
+ "@\"HAPSRPPairSetupSession\""
+ "@\"HAPSRPPairSetupSession\"16@0:8"
+ "@\"NSString\"32@0:8@\"<HAPPairSetupSession>\"16^@24"
+ "@36@0:8@16Q24C32"
+ "Accessory reported an internal timeout"
+ "B32@0:8@\"<HAPPairSetupSession>\"16d24"
+ "B40@0:8@\"<HAPPairSetupSession>\"16@\"HAPPairingIdentity\"24^@32"
+ "HAPSRPPairSetupSession"
+ "Num IP Addresses: %lu, Num IP Addresses Tried: %lu, Num Bonjour Names: %lu, IP Address: %@, Service Name: %@ Resolve Attempt: %@"
+ "T@\"<HAPPairSetupSession>\",&,V_pairSetupSession"
+ "T@\"HAPSRPPairSetupSession\",&,N"
+ "T@\"HAPSRPPairSetupSession\",&,N,V_pairingSession"
+ "T@\"NSError\",C,N,V_currentPairVerifyError"
+ "TB,N,V_isInvalidated"
+ "TB,N,V_suspendCapable"
+ "TB,N,V_triedConnectingToIPv4Address"
+ "TB,N,V_triedConnectingToIPv6Address"
+ "TB,R,N,V_triedConnectingToIPv4Address"
+ "TB,R,N,V_triedConnectingToIPv6Address"
+ "T^{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})},R,N"
+ "Unable to send Pair Verify request"
+ "Unable to send initial Pair Verify request"
+ "_currentPairVerifyError"
+ "_isInvalidated"
+ "_removeRecentlySeenPairedPeripheralWithIdentifier:"
+ "_suspendCapable"
+ "_triedConnectingToIPv4Address"
+ "_triedConnectingToIPv6Address"
+ "addressFamily"
+ "currentPairVerifyError"
+ "dnsNameForHTTPHeaderFromDNSNames:"
+ "ensureNetworkMonitor"
+ "hmf_enumerateWithAutoreleasePoolUsingBlock:"
+ "hmf_isEqualToUUID:"
+ "httpClient:didStartConnectingToNetAddress:"
+ "initWithBytesNoCopy:length:encoding:freeWhenDone:"
+ "isHAPOperationDelayed"
+ "pairSetupSession:pairSetupType:features:"
+ "removeRecentlySeenPairedPeripheralWithIdentifier:"
+ "setConnectionProgressHandler:context:"
+ "setContext:"
+ "setCurrentPairVerifyError:"
+ "setIsInvalidated:"
+ "setSuspendCapable:"
+ "setTriedConnectingToIPv4Address:"
+ "setTriedConnectingToIPv6Address:"
+ "sortAddressList:"
+ "suspendCapable"
+ "triedConnectingOverIPv4"
+ "triedConnectingOverIPv6"
+ "triedConnectingToIPv4Address"
+ "triedConnectingToIPv6Address"
+ "v24@0:8@\"<HAPPairSetupSession>\"16"
+ "v24@0:8@\"HAPSRPPairSetupSession\"16"
+ "v32@0:8@\"<HAPPairSetupSession>\"16@\"NSData\"24"
+ "v32@0:8@\"<HAPPairSetupSession>\"16@\"NSError\"24"
+ "v32@0:8@\"<HAPPairSetupSession>\"16@\"NSString\"24"
+ "v32@0:8@\"<HAPPairSetupSession>\"16@?<v@?@\"NSString\"@\"NSError\">24"
+ "v32@0:8@\"HAPHTTPClient\"16@\"HMFNetAddress\"24"
+ "v32@0:8@\"NSData\"16@\"NSError\"24"
+ "v32@0:8^?16^v24"
+ "\xf0\xc1"
- "    Rediscovered Paired Accessory Server: %@"
- "%@ %@ %@"
- "%{public}@Disconnected -> Entering suspended mode"
- "%{public}@Image snapshot returned HTTP client error: %@"
- "%{public}@Network is available, resuming all streams"
- "%{public}@Network is unavailable, suspending all streams"
- "%{public}@Received a Bonjour Add for an already discovered paired IP accessory server %{public}@ wacAccessory:%{public}@ with new BonjourDevice info: %@"
- "%{public}@Updating peripheral [%@] keychain with resumeSessionID: %llu"
- "@\"HAPPairSetupSession\""
- "@\"HAPPairSetupSession\"16@0:8"
- "@\"HAPPairSetupSessionServerInfo\"24@0:8@\"HAPPairSetupSession\"16"
- "@\"HAPPairingIdentity\"32@0:8@\"HAPPairSetupSession\"16^@24"
- "@\"NSString\"32@0:8@\"HAPPairSetupSession\"16^@24"
- "B32@0:8@\"HAPPairSetupSession\"16d24"
- "B40@0:8@\"HAPPairSetupSession\"16@\"HAPPairingIdentity\"24^@32"
- "Num IP Addresses: %lu, Num IP Addresses Tried: %lu, Num Bonjour Names: %lu, IP Address: %@, Service Name: %@ Resolve Attmpt: %@"
- "T@\"HAPPairSetupSession\",&,N"
- "T@\"HAPPairSetupSession\",&,N,V_pairSetupSession"
- "T@\"HAPPairSetupSession\",&,N,V_pairingSession"
- "TB,N,V_checkIfSuspendedAccesoryRediscovered"
- "T{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})},R,N,V_address"
- "_checkIfSuspendedAccesoryRediscovered"
- "checkIfSuspendedAccesoryRediscovered"
- "getAddressPtr"
- "setCheckIfSuspendedAccesoryRediscovered:"
- "v24@0:8@\"HAPPairSetupSession\"16"
- "v32@0:8@\"HAPPairSetupSession\"16@\"NSData\"24"
- "v32@0:8@\"HAPPairSetupSession\"16@\"NSError\"24"
- "v32@0:8@\"HAPPairSetupSession\"16@\"NSString\"24"
- "v32@0:8@\"HAPPairSetupSession\"16@?<v@?@\"NSString\"@\"NSError\">24"
- "{coap_address_t=I(?={sockaddr=CC[14c]}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})}16@0:8"
- "\xf0\xb1"

```
