## CoreHAP

> `/System/Library/PrivateFrameworks/CoreHAP.framework/Versions/A/CoreHAP`

```diff

-1493.1.5.4.1
-  __TEXT.__text: 0x2a9a7c
-  __TEXT.__objc_methlist: 0x17d80
-  __TEXT.__const: 0x11c8
-  __TEXT.__constg_swiftt: 0x960
-  __TEXT.__swift5_typeref: 0x3e4
+1514.0.0.0.1
+  __TEXT.__text: 0x2af1d4
+  __TEXT.__objc_methlist: 0x18410
+  __TEXT.__const: 0x1330
+  __TEXT.__constg_swiftt: 0xa64
+  __TEXT.__swift5_typeref: 0x437
   __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_reflstr: 0x474
-  __TEXT.__swift5_fieldmd: 0x3f0
-  __TEXT.__swift5_assocty: 0xc0
-  __TEXT.__swift5_proto: 0x50
-  __TEXT.__swift5_types: 0x30
-  __TEXT.__cstring: 0x13d35
-  __TEXT.__oslogstring: 0x3d570
-  __TEXT.__swift5_capture: 0x288
-  __TEXT.__gcc_except_tab: 0x5890
-  __TEXT.__unwind_info: 0x86c8
+  __TEXT.__swift5_reflstr: 0x581
+  __TEXT.__swift5_fieldmd: 0x49c
+  __TEXT.__swift5_assocty: 0xd8
+  __TEXT.__swift5_proto: 0x5c
+  __TEXT.__swift5_types: 0x34
+  __TEXT.__cstring: 0x140df
+  __TEXT.__oslogstring: 0x3dea4
+  __TEXT.__swift5_capture: 0x28c
+  __TEXT.__gcc_except_tab: 0x586c
+  __TEXT.__unwind_info: 0x8810
   __TEXT.__eh_frame: 0x1080
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2148
-  __DATA_CONST.__objc_classlist: 0xbf8
+  __DATA_CONST.__const: 0x2170
+  __DATA_CONST.__objc_classlist: 0xc28
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x390
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7c28
+  __DATA_CONST.__objc_selrefs: 0x7df0
   __DATA_CONST.__objc_protorefs: 0x100
-  __DATA_CONST.__objc_superrefs: 0xa40
+  __DATA_CONST.__objc_superrefs: 0xa70
   __DATA_CONST.__objc_arraydata: 0x200
-  __DATA_CONST.__got: 0xfb8
-  __AUTH_CONST.__const: 0x5468
-  __AUTH_CONST.__cfstring: 0xf7a0
-  __AUTH_CONST.__objc_const: 0x29fc8
+  __DATA_CONST.__got: 0x1008
+  __AUTH_CONST.__const: 0x53f8
+  __AUTH_CONST.__cfstring: 0xfa00
+  __AUTH_CONST.__objc_const: 0x2abb0
+  __AUTH_CONST.__weak_auth_got: 0x8
   __AUTH_CONST.__objc_intobj: 0x588
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0xc0
-  __AUTH_CONST.__auth_got: 0x10b0
-  __AUTH.__objc_data: 0x7228
+  __AUTH_CONST.__auth_got: 0x1110
+  __AUTH.__objc_data: 0x7518
   __AUTH.__data: 0xb0
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x28
-  __DATA.__objc_ivar: 0x17fc
-  __DATA.__data: 0x2c22
+  __DATA.__objc_ivar: 0x1870
+  __DATA.__data: 0x2c72
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0xfc8
   __DATA_DIRTY.__data: 0x40
-  __DATA_DIRTY.__bss: 0x88
+  __DATA_DIRTY.__bss: 0x78
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9510
-  Symbols:   19560
-  CStrings:  6554
+  Functions: 9652
+  Symbols:   19793
+  CStrings:  6604
 
Symbols:
+ +[HAP2ThreadNetworkUtil _eventQueue]
+ +[HAP2ThreadNetworkUtil _fetchMeshLocalPrefixFromXPC]
+ +[HAP2ThreadNetworkUtil _setSharedThreadClient:]
+ +[HAP2ThreadNetworkUtil forceRefreshMeshLocalPrefix]
+ +[HAP2ThreadNetworkUtil isNetworkLinkManagementEnabled]
+ +[HAP2ThreadNetworkUtil setupEventSubscriptions]
+ +[HAPAVCStreamingControlCommandWrapper parsedFromData:error:]
+ +[HAPAVCStreamingControlRequest parsedFromData:error:]
+ +[HAPAVCStreamingControlResponse parsedFromData:error:]
+ +[HAPAVCStreamingControlStatusWrapper parsedFromData:error:]
+ +[HAPAVCViewerRegistrationOperationWrapper parsedFromData:error:]
+ -[HAP2AccessoryAddressLists .cxx_destruct]
+ -[HAP2AccessoryAddressLists description]
+ -[HAP2AccessoryAddressLists initWithPrimary:secondary:]
+ -[HAP2AccessoryAddressLists isEmpty]
+ -[HAP2AccessoryAddressLists primary]
+ -[HAP2AccessoryAddressLists secondary]
+ -[HAP2AccessoryAddressLists setPrimary:]
+ -[HAP2AccessoryAddressLists setSecondary:]
+ -[HAP2AccessoryDeviceIPAddress copyWithZone:]
+ -[HAP2AccessoryDeviceIPAddress hash]
+ -[HAP2AccessoryDeviceIPAddress isEqual:]
+ -[HAP2AccessoryServer _controllerUnchecked]
+ -[HAP2AccessoryServer _setHasDiscoveryAdvertisementLockOnly:]
+ -[HAP2AccessoryServer(Paired) closeSessionWithCompletion:]
+ -[HAP2AccessoryServer(Unpaired) localPairingIdentityForPairingDriver:error:]
+ -[HAP2AccessoryServer(Unpaired) pairingDriver:saveRemoteECDSAPairingKey:forAccessoryIdentifier:error:]
+ -[HAP2AccessoryServer(Unpaired) pairingDriver:saveRemotePairingIdentity:error:]
+ -[HAP2AccessoryServerBrowser dealloc]
+ -[HAP2AccessoryServerBrowser localPairingIdentityForDeviceID:error:]
+ -[HAP2AccessoryServerController closeSessionWithCompletion:]
+ -[HAP2AccessoryServerController forceSessionExpired]
+ -[HAP2AccessoryServerController isReadingAttributeDatabase]
+ -[HAP2AccessoryServerController localPairingIdentityForSecureTransport:error:]
+ -[HAP2AccessoryServerController secureTransport:ecdsaLongTermPublicKeyForPeerWithIdentifier:error:]
+ -[HAP2AccessoryServerController secureTransport:localPairingIdentityForECDSAKeyPairSetupSession:error:]
+ -[HAP2AccessoryServerController secureTransport:remotePairingIdentityForDeviceID:error:]
+ -[HAP2AccessoryServerController setUnitTest_useHH2:]
+ -[HAP2AccessoryServerCoordinator _didDiscoverAccessory:fromMDNSEvent:completion:]
+ -[HAP2AccessoryServerDiscoveryBonjour lastKnownAccessoryInfoByServiceKey]
+ -[HAP2AccessoryServerTransportCoAP addressResolverFactory]
+ -[HAP2AccessoryServerTransportCoAP setAddressResolverFactory:]
+ -[HAP2SerializedOperationQueue _applyCallerQoSToOperations:]
+ -[HAP2SerializedOperationQueue addConcurrentBlock:qos:]
+ -[HAPAVCStreamingControlCommandWrapper copyWithZone:]
+ -[HAPAVCStreamingControlCommandWrapper description]
+ -[HAPAVCStreamingControlCommandWrapper initWithValue:]
+ -[HAPAVCStreamingControlCommandWrapper init]
+ -[HAPAVCStreamingControlCommandWrapper isEqual:]
+ -[HAPAVCStreamingControlCommandWrapper parseFromData:error:]
+ -[HAPAVCStreamingControlCommandWrapper serializeWithError:]
+ -[HAPAVCStreamingControlCommandWrapper setValue:]
+ -[HAPAVCStreamingControlCommandWrapper value]
+ -[HAPAVCStreamingControlRequest .cxx_destruct]
+ -[HAPAVCStreamingControlRequest command]
+ -[HAPAVCStreamingControlRequest copyWithZone:]
+ -[HAPAVCStreamingControlRequest description]
+ -[HAPAVCStreamingControlRequest initWithSessionIdentifier:command:]
+ -[HAPAVCStreamingControlRequest init]
+ -[HAPAVCStreamingControlRequest isEqual:]
+ -[HAPAVCStreamingControlRequest parseFromData:error:]
+ -[HAPAVCStreamingControlRequest serializeWithError:]
+ -[HAPAVCStreamingControlRequest sessionIdentifier]
+ -[HAPAVCStreamingControlRequest setCommand:]
+ -[HAPAVCStreamingControlRequest setSessionIdentifier:]
+ -[HAPAVCStreamingControlResponse .cxx_destruct]
+ -[HAPAVCStreamingControlResponse copyWithZone:]
+ -[HAPAVCStreamingControlResponse description]
+ -[HAPAVCStreamingControlResponse initWithSessionIdentifier:status:]
+ -[HAPAVCStreamingControlResponse init]
+ -[HAPAVCStreamingControlResponse isEqual:]
+ -[HAPAVCStreamingControlResponse parseFromData:error:]
+ -[HAPAVCStreamingControlResponse serializeWithError:]
+ -[HAPAVCStreamingControlResponse sessionIdentifier]
+ -[HAPAVCStreamingControlResponse setSessionIdentifier:]
+ -[HAPAVCStreamingControlResponse setStatus:]
+ -[HAPAVCStreamingControlResponse status]
+ -[HAPAVCStreamingControlStatusWrapper copyWithZone:]
+ -[HAPAVCStreamingControlStatusWrapper description]
+ -[HAPAVCStreamingControlStatusWrapper initWithValue:]
+ -[HAPAVCStreamingControlStatusWrapper init]
+ -[HAPAVCStreamingControlStatusWrapper isEqual:]
+ -[HAPAVCStreamingControlStatusWrapper parseFromData:error:]
+ -[HAPAVCStreamingControlStatusWrapper serializeWithError:]
+ -[HAPAVCStreamingControlStatusWrapper setValue:]
+ -[HAPAVCStreamingControlStatusWrapper value]
+ -[HAPAVCViewerRegistrationOperationWrapper copyWithZone:]
+ -[HAPAVCViewerRegistrationOperationWrapper description]
+ -[HAPAVCViewerRegistrationOperationWrapper initWithValue:]
+ -[HAPAVCViewerRegistrationOperationWrapper init]
+ -[HAPAVCViewerRegistrationOperationWrapper isEqual:]
+ -[HAPAVCViewerRegistrationOperationWrapper parseFromData:error:]
+ -[HAPAVCViewerRegistrationOperationWrapper serializeWithError:]
+ -[HAPAVCViewerRegistrationOperationWrapper setValue:]
+ -[HAPAVCViewerRegistrationOperationWrapper value]
+ -[HAPAVCViewerRegistrationRequest initWithSessionIdentifier:viewerParticipantID:viewerNegotiationBlob:operation:]
+ -[HAPAVCViewerRegistrationRequest operation]
+ -[HAPAVCViewerRegistrationRequest setOperation:]
+ -[HAPAccessoryInfo hasAssignedProductPlan]
+ -[HAPAccessoryPairingRequest init]
+ -[HAPAccessoryPairingRequest setShouldAllowECDSAKeyPairSetup:]
+ -[HAPAccessoryPairingRequest shouldAllowECDSAKeyPairSetup]
+ -[HAPAccessoryServer disconnectWithCompletion:]
+ -[HAPAccessoryServer pairSetupLastError]
+ -[HAPAccessoryServer pairSetupM1ToM4Completed]
+ -[HAPAccessoryServer pairSetupM1ToM4DurationMS]
+ -[HAPAccessoryServer pairSetupM1ToM4Error]
+ -[HAPAccessoryServer pairSetupM5ToM6Completed]
+ -[HAPAccessoryServer pairSetupM5ToM6DurationMS]
+ -[HAPAccessoryServer pairSetupM5ToM6Error]
+ -[HAPAccessoryServer pairSetupWorkDurationMS]
+ -[HAPAccessoryServer setPairSetupLastError:]
+ -[HAPAccessoryServer setPairSetupM1ToM4Completed:]
+ -[HAPAccessoryServer setPairSetupM1ToM4DurationMS:]
+ -[HAPAccessoryServer setPairSetupM1ToM4Error:]
+ -[HAPAccessoryServer setPairSetupM5ToM6Completed:]
+ -[HAPAccessoryServer setPairSetupM5ToM6DurationMS:]
+ -[HAPAccessoryServer setPairSetupM5ToM6Error:]
+ -[HAPAccessoryServer setPairSetupWorkDurationMS:]
+ -[HAPAccessoryServer setTokenAuthCompleted:]
+ -[HAPAccessoryServer setTokenAuthDurationMS:]
+ -[HAPAccessoryServer setTokenAuthError:]
+ -[HAPAccessoryServer tokenAuthCompleted]
+ -[HAPAccessoryServer tokenAuthDurationMS]
+ -[HAPAccessoryServer tokenAuthError]
+ -[HAPAccessoryServerBrowser hasWiFiAdvertisementForHAP2AccessoryServerIdentifier:]
+ -[HAPAccessoryServerBrowser isThreadAccessoryDiscoveredWithAccessoryServerIdentifier:]
+ -[HAPAccessoryServerBrowserHAP2Adapter hasWiFiAdvertisementForHAP2AccessoryServerIdentifier:]
+ -[HAPAccessoryServerBrowserHAP2Adapter isThreadAccessoryDiscoveredWithAccessoryServerIdentifier:]
+ -[HAPAccessoryServerHAP2Adapter disconnectWithCompletion:]
+ -[HAPAccessoryServerIP disconnectWithCompletion:]
+ -[HAPAccessoryServerIP selfAddress]
+ -[HAPCoreUtilsHTTPClient getSelfAddress:maxLength:outLength:]
+ -[HAPHTTPClient selfAddress]
+ -[HAPKeyBag cachedAccessoryKeyType]
+ -[HAPKeyBag setCachedAccessoryKeyType:]
+ -[HAPWebRTCOfferOptions SFrameConfiguration]
+ -[HAPWebRTCOfferOptions initWithSFrameEnabled:SFrameConfiguration:]
+ -[HAPWebRTCOfferOptions setSFrameConfiguration:]
+ -[_HAPAccessoryServerBTLE200 _ecdsaKeyPairSetupRefusalError]
+ GCC_except_table1000
+ GCC_except_table1105
+ GCC_except_table1107
+ GCC_except_table1213
+ GCC_except_table1218
+ GCC_except_table1235
+ GCC_except_table1249
+ GCC_except_table1251
+ GCC_except_table1253
+ GCC_except_table1255
+ GCC_except_table1381
+ GCC_except_table1387
+ GCC_except_table1389
+ GCC_except_table1591
+ GCC_except_table18
+ GCC_except_table1808
+ GCC_except_table1814
+ GCC_except_table1816
+ GCC_except_table1822
+ GCC_except_table1824
+ GCC_except_table1828
+ GCC_except_table1834
+ GCC_except_table1838
+ GCC_except_table1840
+ GCC_except_table1850
+ GCC_except_table1860
+ GCC_except_table1868
+ GCC_except_table1875
+ GCC_except_table1879
+ GCC_except_table1883
+ GCC_except_table1888
+ GCC_except_table1926
+ GCC_except_table2045
+ GCC_except_table2050
+ GCC_except_table2051
+ GCC_except_table2055
+ GCC_except_table2076
+ GCC_except_table2079
+ GCC_except_table2081
+ GCC_except_table2086
+ GCC_except_table2115
+ GCC_except_table2117
+ GCC_except_table2122
+ GCC_except_table2127
+ GCC_except_table2130
+ GCC_except_table2139
+ GCC_except_table2142
+ GCC_except_table2149
+ GCC_except_table2151
+ GCC_except_table2161
+ GCC_except_table2169
+ GCC_except_table2182
+ GCC_except_table2233
+ GCC_except_table2236
+ GCC_except_table2237
+ GCC_except_table2239
+ GCC_except_table2240
+ GCC_except_table2268
+ GCC_except_table236
+ GCC_except_table237
+ GCC_except_table247
+ GCC_except_table2472
+ GCC_except_table248
+ GCC_except_table2480
+ GCC_except_table2501
+ GCC_except_table251
+ GCC_except_table2515
+ GCC_except_table254
+ GCC_except_table2595
+ GCC_except_table2607
+ GCC_except_table261
+ GCC_except_table267
+ GCC_except_table268
+ GCC_except_table271
+ GCC_except_table275
+ GCC_except_table2811
+ GCC_except_table2820
+ GCC_except_table2838
+ GCC_except_table284
+ GCC_except_table2872
+ GCC_except_table2888
+ GCC_except_table2890
+ GCC_except_table290
+ GCC_except_table2902
+ GCC_except_table2909
+ GCC_except_table2931
+ GCC_except_table2945
+ GCC_except_table2946
+ GCC_except_table2947
+ GCC_except_table2950
+ GCC_except_table2959
+ GCC_except_table2966
+ GCC_except_table2969
+ GCC_except_table2974
+ GCC_except_table2979
+ GCC_except_table2984
+ GCC_except_table3025
+ GCC_except_table3042
+ GCC_except_table3045
+ GCC_except_table3050
+ GCC_except_table3068
+ GCC_except_table3084
+ GCC_except_table3086
+ GCC_except_table3090
+ GCC_except_table3098
+ GCC_except_table3106
+ GCC_except_table3170
+ GCC_except_table3177
+ GCC_except_table3179
+ GCC_except_table3180
+ GCC_except_table3203
+ GCC_except_table3223
+ GCC_except_table3451
+ GCC_except_table3518
+ GCC_except_table3519
+ GCC_except_table3523
+ GCC_except_table3526
+ GCC_except_table3528
+ GCC_except_table3529
+ GCC_except_table3533
+ GCC_except_table3534
+ GCC_except_table3536
+ GCC_except_table3543
+ GCC_except_table3553
+ GCC_except_table3556
+ GCC_except_table3567
+ GCC_except_table3568
+ GCC_except_table3570
+ GCC_except_table3572
+ GCC_except_table3575
+ GCC_except_table3579
+ GCC_except_table3581
+ GCC_except_table3584
+ GCC_except_table3587
+ GCC_except_table3601
+ GCC_except_table3605
+ GCC_except_table3609
+ GCC_except_table3613
+ GCC_except_table3640
+ GCC_except_table3663
+ GCC_except_table3669
+ GCC_except_table3673
+ GCC_except_table3679
+ GCC_except_table3686
+ GCC_except_table3693
+ GCC_except_table3694
+ GCC_except_table3695
+ GCC_except_table3782
+ GCC_except_table3783
+ GCC_except_table3784
+ GCC_except_table3785
+ GCC_except_table3787
+ GCC_except_table3788
+ GCC_except_table3789
+ GCC_except_table3790
+ GCC_except_table3791
+ GCC_except_table3792
+ GCC_except_table3793
+ GCC_except_table3794
+ GCC_except_table3795
+ GCC_except_table3796
+ GCC_except_table3849
+ GCC_except_table3954
+ GCC_except_table3961
+ GCC_except_table4003
+ GCC_except_table4007
+ GCC_except_table4010
+ GCC_except_table4013
+ GCC_except_table4016
+ GCC_except_table4019
+ GCC_except_table4022
+ GCC_except_table4025
+ GCC_except_table4028
+ GCC_except_table4031
+ GCC_except_table4036
+ GCC_except_table4049
+ GCC_except_table4054
+ GCC_except_table4058
+ GCC_except_table4060
+ GCC_except_table4063
+ GCC_except_table4074
+ GCC_except_table4082
+ GCC_except_table4095
+ GCC_except_table4099
+ GCC_except_table41
+ GCC_except_table4100
+ GCC_except_table4118
+ GCC_except_table4120
+ GCC_except_table4122
+ GCC_except_table4123
+ GCC_except_table4126
+ GCC_except_table4132
+ GCC_except_table4135
+ GCC_except_table4137
+ GCC_except_table4143
+ GCC_except_table4147
+ GCC_except_table4150
+ GCC_except_table4161
+ GCC_except_table4172
+ GCC_except_table4174
+ GCC_except_table4183
+ GCC_except_table4185
+ GCC_except_table4187
+ GCC_except_table4453
+ GCC_except_table4459
+ GCC_except_table4476
+ GCC_except_table4480
+ GCC_except_table4498
+ GCC_except_table4504
+ GCC_except_table4518
+ GCC_except_table4532
+ GCC_except_table4536
+ GCC_except_table4649
+ GCC_except_table5107
+ GCC_except_table5116
+ GCC_except_table5127
+ GCC_except_table5169
+ GCC_except_table5172
+ GCC_except_table5173
+ GCC_except_table5174
+ GCC_except_table5175
+ GCC_except_table5258
+ GCC_except_table5259
+ GCC_except_table5260
+ GCC_except_table5261
+ GCC_except_table5262
+ GCC_except_table5263
+ GCC_except_table5269
+ GCC_except_table5270
+ GCC_except_table5272
+ GCC_except_table5279
+ GCC_except_table5282
+ GCC_except_table5284
+ GCC_except_table5289
+ GCC_except_table5292
+ GCC_except_table5295
+ GCC_except_table555
+ GCC_except_table566
+ GCC_except_table582
+ GCC_except_table5852
+ GCC_except_table5853
+ GCC_except_table5872
+ GCC_except_table5882
+ GCC_except_table5885
+ GCC_except_table5890
+ GCC_except_table5893
+ GCC_except_table5898
+ GCC_except_table5923
+ GCC_except_table5931
+ GCC_except_table594
+ GCC_except_table5942
+ GCC_except_table5964
+ GCC_except_table5972
+ GCC_except_table5978
+ GCC_except_table5980
+ GCC_except_table5990
+ GCC_except_table6015
+ GCC_except_table6021
+ GCC_except_table628
+ GCC_except_table6320
+ GCC_except_table6324
+ GCC_except_table6369
+ GCC_except_table6373
+ GCC_except_table6375
+ GCC_except_table6377
+ GCC_except_table640
+ GCC_except_table641
+ GCC_except_table643
+ GCC_except_table646
+ GCC_except_table649
+ GCC_except_table6601
+ GCC_except_table6608
+ GCC_except_table6612
+ GCC_except_table6613
+ GCC_except_table6614
+ GCC_except_table6615
+ GCC_except_table6621
+ GCC_except_table663
+ GCC_except_table6637
+ GCC_except_table667
+ GCC_except_table6673
+ GCC_except_table6674
+ GCC_except_table6675
+ GCC_except_table6695
+ GCC_except_table6707
+ GCC_except_table6710
+ GCC_except_table6715
+ GCC_except_table6717
+ GCC_except_table6731
+ GCC_except_table678
+ GCC_except_table681
+ GCC_except_table6966
+ GCC_except_table6979
+ GCC_except_table6984
+ GCC_except_table6987
+ GCC_except_table6988
+ GCC_except_table6990
+ GCC_except_table6991
+ GCC_except_table6993
+ GCC_except_table7023
+ GCC_except_table7047
+ GCC_except_table7051
+ GCC_except_table7055
+ GCC_except_table7060
+ GCC_except_table7064
+ GCC_except_table7068
+ GCC_except_table7072
+ GCC_except_table7076
+ GCC_except_table7084
+ GCC_except_table7086
+ GCC_except_table7090
+ GCC_except_table7154
+ GCC_except_table7155
+ GCC_except_table7156
+ GCC_except_table7157
+ GCC_except_table7158
+ GCC_except_table7159
+ GCC_except_table7160
+ GCC_except_table7224
+ GCC_except_table7231
+ GCC_except_table7232
+ GCC_except_table7248
+ GCC_except_table7249
+ GCC_except_table725
+ GCC_except_table7250
+ GCC_except_table7266
+ GCC_except_table7280
+ GCC_except_table7284
+ GCC_except_table7292
+ GCC_except_table7299
+ GCC_except_table7302
+ GCC_except_table7316
+ GCC_except_table7323
+ GCC_except_table7329
+ GCC_except_table733
+ GCC_except_table7338
+ GCC_except_table7340
+ GCC_except_table7346
+ GCC_except_table7347
+ GCC_except_table7354
+ GCC_except_table7378
+ GCC_except_table7379
+ GCC_except_table7384
+ GCC_except_table7388
+ GCC_except_table7389
+ GCC_except_table7392
+ GCC_except_table7398
+ GCC_except_table7402
+ GCC_except_table7406
+ GCC_except_table7408
+ GCC_except_table7410
+ GCC_except_table7414
+ GCC_except_table7528
+ GCC_except_table7565
+ GCC_except_table760
+ GCC_except_table7622
+ GCC_except_table7625
+ GCC_except_table7638
+ GCC_except_table764
+ GCC_except_table7645
+ GCC_except_table7646
+ GCC_except_table7662
+ GCC_except_table7666
+ GCC_except_table7667
+ GCC_except_table7668
+ GCC_except_table767
+ GCC_except_table769
+ GCC_except_table7717
+ GCC_except_table7720
+ GCC_except_table7723
+ GCC_except_table7750
+ GCC_except_table7751
+ GCC_except_table7756
+ GCC_except_table7794
+ GCC_except_table7795
+ GCC_except_table7796
+ GCC_except_table781
+ GCC_except_table7810
+ GCC_except_table7811
+ GCC_except_table7812
+ GCC_except_table7828
+ GCC_except_table783
+ GCC_except_table7831
+ GCC_except_table7838
+ GCC_except_table7845
+ GCC_except_table7850
+ GCC_except_table7856
+ GCC_except_table7868
+ GCC_except_table7869
+ GCC_except_table7874
+ GCC_except_table7883
+ GCC_except_table7891
+ GCC_except_table7892
+ GCC_except_table7896
+ GCC_except_table7898
+ GCC_except_table7900
+ GCC_except_table7904
+ GCC_except_table7925
+ GCC_except_table7927
+ GCC_except_table7928
+ GCC_except_table7954
+ GCC_except_table808
+ GCC_except_table8119
+ GCC_except_table812
+ GCC_except_table8182
+ GCC_except_table8214
+ GCC_except_table8217
+ GCC_except_table823
+ GCC_except_table824
+ GCC_except_table829
+ GCC_except_table832
+ GCC_except_table835
+ GCC_except_table8384
+ GCC_except_table8422
+ GCC_except_table8459
+ GCC_except_table850
+ GCC_except_table854
+ GCC_except_table855
+ GCC_except_table8552
+ GCC_except_table8556
+ GCC_except_table8566
+ GCC_except_table8568
+ GCC_except_table8571
+ GCC_except_table8573
+ GCC_except_table8575
+ GCC_except_table8584
+ GCC_except_table8590
+ GCC_except_table8595
+ GCC_except_table8598
+ GCC_except_table8603
+ GCC_except_table8608
+ GCC_except_table8611
+ GCC_except_table8614
+ GCC_except_table8640
+ GCC_except_table8643
+ GCC_except_table8644
+ GCC_except_table8663
+ GCC_except_table8664
+ GCC_except_table8665
+ GCC_except_table8667
+ GCC_except_table8668
+ GCC_except_table8670
+ GCC_except_table8671
+ GCC_except_table8672
+ GCC_except_table8674
+ GCC_except_table8675
+ GCC_except_table8677
+ GCC_except_table8681
+ GCC_except_table8682
+ GCC_except_table8686
+ GCC_except_table883
+ GCC_except_table8850
+ GCC_except_table8852
+ GCC_except_table8854
+ GCC_except_table8857
+ GCC_except_table8859
+ GCC_except_table8861
+ GCC_except_table8863
+ GCC_except_table8864
+ GCC_except_table8871
+ GCC_except_table8873
+ GCC_except_table8874
+ GCC_except_table890
+ GCC_except_table898
+ GCC_except_table899
+ GCC_except_table915
+ GCC_except_table937
+ GCC_except_table95
+ GCC_except_table955
+ GCC_except_table977
+ GCC_except_table981
+ GCC_except_table995
+ OBJC_IVAR_$_HAP2AccessoryAddressLists._primary
+ OBJC_IVAR_$_HAP2AccessoryAddressLists._secondary
+ OBJC_IVAR_$_HAP2AccessoryServerController._lastAnnouncedSessionNumber
+ OBJC_IVAR_$_HAP2AccessoryServerController._unitTest_useHH2
+ OBJC_IVAR_$_HAP2AccessoryServerDiscoveryBonjour._lastKnownAccessoryInfoByServiceKey
+ OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._addressResolverFactory
+ OBJC_IVAR_$_HAP2AccessoryServerTransportCoAP._sendRequestQoS
+ OBJC_IVAR_$_HAPAVCStreamingControlCommandWrapper._value
+ OBJC_IVAR_$_HAPAVCStreamingControlRequest._command
+ OBJC_IVAR_$_HAPAVCStreamingControlRequest._sessionIdentifier
+ OBJC_IVAR_$_HAPAVCStreamingControlResponse._sessionIdentifier
+ OBJC_IVAR_$_HAPAVCStreamingControlResponse._status
+ OBJC_IVAR_$_HAPAVCStreamingControlStatusWrapper._value
+ OBJC_IVAR_$_HAPAVCViewerRegistrationOperationWrapper._value
+ OBJC_IVAR_$_HAPAVCViewerRegistrationRequest._operation
+ OBJC_IVAR_$_HAPAccessoryPairingRequest._shouldAllowECDSAKeyPairSetup
+ OBJC_IVAR_$_HAPAccessoryServer._pairSetupLastError
+ OBJC_IVAR_$_HAPAccessoryServer._pairSetupM1ToM4Completed
+ OBJC_IVAR_$_HAPAccessoryServer._pairSetupM1ToM4DurationMS
+ OBJC_IVAR_$_HAPAccessoryServer._pairSetupM1ToM4Error
+ OBJC_IVAR_$_HAPAccessoryServer._pairSetupM5ToM6Completed
+ OBJC_IVAR_$_HAPAccessoryServer._pairSetupM5ToM6DurationMS
+ OBJC_IVAR_$_HAPAccessoryServer._pairSetupM5ToM6Error
+ OBJC_IVAR_$_HAPAccessoryServer._pairSetupWorkDurationMS
+ OBJC_IVAR_$_HAPAccessoryServer._tokenAuthCompleted
+ OBJC_IVAR_$_HAPAccessoryServer._tokenAuthDurationMS
+ OBJC_IVAR_$_HAPAccessoryServer._tokenAuthError
+ OBJC_IVAR_$_HAPKeyBag._cachedAccessoryKeyType
+ OBJC_IVAR_$_HAPWebRTCOfferOptions._SFrameConfiguration
+ _HAPAVCStreamingControlCommandAsString
+ _HAPAVCStreamingControlStatusAsString
+ _HAPAVCViewerRegistrationOperationAsString
+ _HAPErrorAlreadyPairedPeerIdentifierKey
+ _HTTPClientGetSelfAddress
+ _OBJC_CLASS_$_HAP2AccessoryAddressLists
+ _OBJC_CLASS_$_HAPAVCStreamingControlCommandWrapper
+ _OBJC_CLASS_$_HAPAVCStreamingControlRequest
+ _OBJC_CLASS_$_HAPAVCStreamingControlResponse
+ _OBJC_CLASS_$_HAPAVCStreamingControlStatusWrapper
+ _OBJC_CLASS_$_HAPAVCViewerRegistrationOperationWrapper
+ _OBJC_METACLASS_$_HAP2AccessoryAddressLists
+ _OBJC_METACLASS_$_HAPAVCStreamingControlCommandWrapper
+ _OBJC_METACLASS_$_HAPAVCStreamingControlRequest
+ _OBJC_METACLASS_$_HAPAVCStreamingControlResponse
+ _OBJC_METACLASS_$_HAPAVCStreamingControlStatusWrapper
+ _OBJC_METACLASS_$_HAPAVCViewerRegistrationOperationWrapper
+ __60-[HAP2AccessoryServerController closeSessionWithCompletion:]_block_invoke
+ __81-[HAP2AccessoryServerCoordinator _didDiscoverAccessory:fromMDNSEvent:completion:]_block_invoke
+ __OBJC_$_CLASS_METHODS_HAPAVCStreamingControlCommandWrapper
+ __OBJC_$_CLASS_METHODS_HAPAVCStreamingControlRequest
+ __OBJC_$_CLASS_METHODS_HAPAVCStreamingControlResponse
+ __OBJC_$_CLASS_METHODS_HAPAVCStreamingControlStatusWrapper
+ __OBJC_$_CLASS_METHODS_HAPAVCViewerRegistrationOperationWrapper
+ __OBJC_$_INSTANCE_METHODS_HAP2AccessoryAddressLists
+ __OBJC_$_INSTANCE_METHODS_HAPAVCStreamingControlCommandWrapper
+ __OBJC_$_INSTANCE_METHODS_HAPAVCStreamingControlRequest
+ __OBJC_$_INSTANCE_METHODS_HAPAVCStreamingControlResponse
+ __OBJC_$_INSTANCE_METHODS_HAPAVCStreamingControlStatusWrapper
+ __OBJC_$_INSTANCE_METHODS_HAPAVCViewerRegistrationOperationWrapper
+ __OBJC_$_INSTANCE_VARIABLES_HAP2AccessoryAddressLists
+ __OBJC_$_INSTANCE_VARIABLES_HAPAVCStreamingControlCommandWrapper
+ __OBJC_$_INSTANCE_VARIABLES_HAPAVCStreamingControlRequest
+ __OBJC_$_INSTANCE_VARIABLES_HAPAVCStreamingControlResponse
+ __OBJC_$_INSTANCE_VARIABLES_HAPAVCStreamingControlStatusWrapper
+ __OBJC_$_INSTANCE_VARIABLES_HAPAVCViewerRegistrationOperationWrapper
+ __OBJC_$_PROP_LIST_HAP2AccessoryAddressLists
+ __OBJC_$_PROP_LIST_HAPAVCStreamingControlCommandWrapper
+ __OBJC_$_PROP_LIST_HAPAVCStreamingControlRequest
+ __OBJC_$_PROP_LIST_HAPAVCStreamingControlResponse
+ __OBJC_$_PROP_LIST_HAPAVCStreamingControlStatusWrapper
+ __OBJC_$_PROP_LIST_HAPAVCViewerRegistrationOperationWrapper
+ __OBJC_CLASS_PROTOCOLS_$_HAP2AccessoryDeviceIPAddress
+ __OBJC_CLASS_PROTOCOLS_$_HAPAVCStreamingControlCommandWrapper
+ __OBJC_CLASS_PROTOCOLS_$_HAPAVCStreamingControlRequest
+ __OBJC_CLASS_PROTOCOLS_$_HAPAVCStreamingControlResponse
+ __OBJC_CLASS_PROTOCOLS_$_HAPAVCStreamingControlStatusWrapper
+ __OBJC_CLASS_PROTOCOLS_$_HAPAVCViewerRegistrationOperationWrapper
+ __OBJC_CLASS_RO_$_HAP2AccessoryAddressLists
+ __OBJC_CLASS_RO_$_HAPAVCStreamingControlCommandWrapper
+ __OBJC_CLASS_RO_$_HAPAVCStreamingControlRequest
+ __OBJC_CLASS_RO_$_HAPAVCStreamingControlResponse
+ __OBJC_CLASS_RO_$_HAPAVCStreamingControlStatusWrapper
+ __OBJC_CLASS_RO_$_HAPAVCViewerRegistrationOperationWrapper
+ __OBJC_METACLASS_RO_$_HAP2AccessoryAddressLists
+ __OBJC_METACLASS_RO_$_HAPAVCStreamingControlCommandWrapper
+ __OBJC_METACLASS_RO_$_HAPAVCStreamingControlRequest
+ __OBJC_METACLASS_RO_$_HAPAVCStreamingControlResponse
+ __OBJC_METACLASS_RO_$_HAPAVCStreamingControlStatusWrapper
+ __OBJC_METACLASS_RO_$_HAPAVCViewerRegistrationOperationWrapper
+ __ZL10_cacheLock
+ __ZL11_eventQueue
+ __ZL11_generation
+ __ZL19_sharedThreadClient
+ __ZL20_eventQueueOnceToken
+ __ZdlPv
+ ___36+[HAP2ThreadNetworkUtil _eventQueue]_block_invoke
+ ___49-[HAPAccessoryServerIP disconnectWithCompletion:]_block_invoke
+ ___58-[HAP2AccessoryServer(Paired) closeSessionWithCompletion:]_block_invoke
+ ___58-[HAPAccessoryServerHAP2Adapter disconnectWithCompletion:]_block_invoke
+ ___60-[HAP2AccessoryServerController closeSessionWithCompletion:]_block_invoke
+ ___60-[HAP2SerializedOperationQueue _applyCallerQoSToOperations:]_block_invoke
+ ___61-[HAP2AccessoryServer _setHasDiscoveryAdvertisementLockOnly:]_block_invoke
+ ___70-[HAP2AccessoryServerController _announceReestablishedSessionIfNeeded]_block_invoke
+ ___78-[HAPAccessoryServerBrowserHAP2Adapter discoverAccessoryServerWithIdentifier:]_block_invoke_3
+ ___78-[HAPAccessoryServerBrowserHAP2Adapter discoverAccessoryServerWithIdentifier:]_block_invoke_4
+ ___81-[HAP2AccessoryServerCoordinator _didDiscoverAccessory:fromMDNSEvent:completion:]_block_invoke
+ ___97-[HAPAccessoryServerBrowserHAP2Adapter isThreadAccessoryDiscoveredWithAccessoryServerIdentifier:]_block_invoke
+ ___block_descriptor_40_e28_v32?0"NSOperation"8Q16^B24l
+ ___block_descriptor_40_e8_32bs_e41_v32?0"NSData"8"NSString"16"NSError"24l
+ ___block_descriptor_56_e8_32s40r48r_e69_v32?0"HAP2AccessoryServerDiscoveryBonjourBrowseResultTuple"8Q16^B24l
+ __swift_closure_destructor.198Tm
+ __xpc_type_dictionary
+ __xpc_type_string
+ _associated conformance 7CoreHAP17PairSetupTLVErrorOSHAASQ
+ _dispatch_queue_attr_make_with_qos_class
+ _objc_msgSend$ECDSAKeyForAccessoryName:error:
+ _objc_msgSend$_applyCallerQoSToOperations:
+ _objc_msgSend$_didDiscoverAccessory:fromMDNSEvent:completion:
+ _objc_msgSend$_ecdsaKeyPairSetupRefusalError
+ _objc_msgSend$_setHasDiscoveryAdvertisementLockOnly:
+ _objc_msgSend$_sharedThreadClient
+ _objc_msgSend$addConcurrentBlock:qos:
+ _objc_msgSend$broadcast
+ _objc_msgSend$cachedAccessoryKeyType
+ _objc_msgSend$closeSessionWithCompletion:
+ _objc_msgSend$controllerKeyForDeviceId:error:
+ _objc_msgSend$controllerKeyForECDSAKeyAccessory:error:
+ _objc_msgSend$disconnectWithCompletion:
+ _objc_msgSend$forceSessionExpired
+ _objc_msgSend$getProperty:output:
+ _objc_msgSend$getSelfAddress:maxLength:outLength:
+ _objc_msgSend$initWithSFrameEnabled:SFrameConfiguration:
+ _objc_msgSend$initWithSessionIdentifier:viewerParticipantID:viewerNegotiationBlob:operation:
+ _objc_msgSend$isKnownToSystemCommissioner
+ _objc_msgSend$lastKnownAccessoryInfoByServiceKey
+ _objc_msgSend$localPairingIdentityForDeviceID:error:
+ _objc_msgSend$localPairingIdentityForPairingDriver:error:
+ _objc_msgSend$localPairingIdentityForSecureTransport:error:
+ _objc_msgSend$pairingDriver:saveRemoteECDSAPairingKey:forAccessoryIdentifier:error:
+ _objc_msgSend$pairingDriver:saveRemotePairingIdentity:error:
+ _objc_msgSend$primary
+ _objc_msgSend$publicKeyForIdentifier:error:
+ _objc_msgSend$saveECDSAKey:forAccessoryName:error:
+ _objc_msgSend$savePublicKey:forIdentifier:error:
+ _objc_msgSend$secondary
+ _objc_msgSend$secureTransport:ecdsaLongTermPublicKeyForPeerWithIdentifier:error:
+ _objc_msgSend$secureTransport:localPairingIdentityForECDSAKeyPairSetupSession:error:
+ _objc_msgSend$secureTransport:remotePairingIdentityForDeviceID:error:
+ _objc_msgSend$selfAddress
+ _objc_msgSend$setCachedAccessoryKeyType:
+ _objc_msgSend$setShouldAllowECDSAKeyPairSetup:
+ _objc_msgSend$shouldAllowECDSAKeyPairSetup
+ _os_unfair_lock_lock
+ _serviceKeyForBrowseResult
+ _swift_deallocClassInstance
+ _symbolic _____ 7CoreHAP17PairSetupTLVErrorO
+ _symbolic _____Sg 10Foundation4DateV
+ _symbolic _____Sg6rolled_______pSg5errorAB9echoTokentSg 10Foundation4DataV s5ErrorP
+ _symbolic _____y______pG s23_ContiguousArrayStorageC s7CVarArgP
+ _xpc_dictionary_create
+ _xpc_dictionary_get_value
+ _xpc_get_type
+ _xpc_string_get_string_ptr
+ logCategory._hmf_once_t111
+ logCategory._hmf_once_t20
+ logCategory._hmf_once_t280
+ logCategory._hmf_once_t49
+ logCategory._hmf_once_t86
+ logCategory._hmf_once_t866
+ logCategory._hmf_once_t903
+ logCategory._hmf_once_t99
+ logCategory._hmf_once_v100
+ logCategory._hmf_once_v112
+ logCategory._hmf_once_v21
+ logCategory._hmf_once_v281
+ logCategory._hmf_once_v50
+ logCategory._hmf_once_v867
+ logCategory._hmf_once_v87
+ logCategory._hmf_once_v904
- -[HAP2AccessoryServer _browserFastSetHasDiscoveryAdvertisement:]
- -[HAP2AccessoryServer(Unpaired) pairingDriver:didRequestLocalPairingIdentityWithCompletion:]
- -[HAP2AccessoryServer(Unpaired) pairingDriver:didSaveRemoteECDSAPairingKey:forAccessoryIdentifier:completion:]
- -[HAP2AccessoryServer(Unpaired) pairingDriver:didSaveRemotePairingIdentity:completion:]
- -[HAP2AccessoryServerController secureTransport:needsECDSALongTermPublicKeyForPeerWithIdentifier:completion:]
- -[HAP2AccessoryServerController secureTransport:needsLocalPairingIdentityForECDSAKeyPairSetupSession:completion:]
- -[HAP2AccessoryServerController secureTransport:needsLocalPairingIdentityWithCompletion:]
- -[HAP2AccessoryServerController secureTransport:needsRemotePairingIdentityForDeviceID:completion:]
- -[HAP2AccessoryServerCoordinator _didDiscoverAccessory:completion:]
- -[HAPAVCViewerRegistrationRequest initWithSessionIdentifier:viewerParticipantID:viewerNegotiationBlob:]
- -[HAPWebRTCOfferOptions initWithSFrameEnabled:]
- GCC_except_table1092
- GCC_except_table1094
- GCC_except_table1200
- GCC_except_table1205
- GCC_except_table1209
- GCC_except_table1236
- GCC_except_table1238
- GCC_except_table1240
- GCC_except_table1242
- GCC_except_table1368
- GCC_except_table1374
- GCC_except_table1376
- GCC_except_table1578
- GCC_except_table16
- GCC_except_table1788
- GCC_except_table1790
- GCC_except_table1795
- GCC_except_table1809
- GCC_except_table1811
- GCC_except_table1815
- GCC_except_table1821
- GCC_except_table1823
- GCC_except_table1825
- GCC_except_table1827
- GCC_except_table1832
- GCC_except_table1854
- GCC_except_table1861
- GCC_except_table1865
- GCC_except_table1869
- GCC_except_table1874
- GCC_except_table1912
- GCC_except_table2031
- GCC_except_table2036
- GCC_except_table2037
- GCC_except_table2039
- GCC_except_table2041
- GCC_except_table2058
- GCC_except_table2062
- GCC_except_table2065
- GCC_except_table2089
- GCC_except_table2099
- GCC_except_table2101
- GCC_except_table2108
- GCC_except_table2111
- GCC_except_table2116
- GCC_except_table2119
- GCC_except_table2123
- GCC_except_table2128
- GCC_except_table2135
- GCC_except_table2141
- GCC_except_table2168
- GCC_except_table2201
- GCC_except_table2208
- GCC_except_table2226
- GCC_except_table2227
- GCC_except_table2228
- GCC_except_table2230
- GCC_except_table2234
- GCC_except_table2257
- GCC_except_table2261
- GCC_except_table2269
- GCC_except_table234
- GCC_except_table235
- GCC_except_table245
- GCC_except_table246
- GCC_except_table2473
- GCC_except_table2486
- GCC_except_table249
- GCC_except_table2502
- GCC_except_table2516
- GCC_except_table252
- GCC_except_table259
- GCC_except_table2596
- GCC_except_table2608
- GCC_except_table263
- GCC_except_table266
- GCC_except_table2668
- GCC_except_table2676
- GCC_except_table2687
- GCC_except_table269
- GCC_except_table2701
- GCC_except_table2704
- GCC_except_table2709
- GCC_except_table2718
- GCC_except_table2724
- GCC_except_table2726
- GCC_except_table273
- GCC_except_table2736
- GCC_except_table2759
- GCC_except_table2765
- GCC_except_table282
- GCC_except_table288
- GCC_except_table2961
- GCC_except_table2970
- GCC_except_table2988
- GCC_except_table3022
- GCC_except_table3038
- GCC_except_table3040
- GCC_except_table3059
- GCC_except_table3081
- GCC_except_table3095
- GCC_except_table3096
- GCC_except_table3097
- GCC_except_table3100
- GCC_except_table3108
- GCC_except_table3115
- GCC_except_table3118
- GCC_except_table3123
- GCC_except_table3128
- GCC_except_table3133
- GCC_except_table3173
- GCC_except_table3190
- GCC_except_table3193
- GCC_except_table3198
- GCC_except_table3200
- GCC_except_table3216
- GCC_except_table3232
- GCC_except_table3234
- GCC_except_table3238
- GCC_except_table3246
- GCC_except_table3254
- GCC_except_table3318
- GCC_except_table3325
- GCC_except_table3327
- GCC_except_table3328
- GCC_except_table3351
- GCC_except_table3371
- GCC_except_table3666
- GCC_except_table3667
- GCC_except_table3671
- GCC_except_table3674
- GCC_except_table3676
- GCC_except_table3681
- GCC_except_table3691
- GCC_except_table3704
- GCC_except_table3715
- GCC_except_table3716
- GCC_except_table3718
- GCC_except_table3720
- GCC_except_table3723
- GCC_except_table3726
- GCC_except_table3728
- GCC_except_table3731
- GCC_except_table3734
- GCC_except_table3746
- GCC_except_table3748
- GCC_except_table3752
- GCC_except_table3756
- GCC_except_table3760
- GCC_except_table3809
- GCC_except_table3815
- GCC_except_table3819
- GCC_except_table3823
- GCC_except_table3825
- GCC_except_table3828
- GCC_except_table3830
- GCC_except_table3832
- GCC_except_table3839
- GCC_except_table3840
- GCC_except_table3841
- GCC_except_table39
- GCC_except_table3918
- GCC_except_table3919
- GCC_except_table3920
- GCC_except_table3921
- GCC_except_table3922
- GCC_except_table3923
- GCC_except_table3924
- GCC_except_table3925
- GCC_except_table3926
- GCC_except_table3927
- GCC_except_table3928
- GCC_except_table3929
- GCC_except_table3930
- GCC_except_table3931
- GCC_except_table3984
- GCC_except_table4138
- GCC_except_table4142
- GCC_except_table4148
- GCC_except_table4151
- GCC_except_table4154
- GCC_except_table4157
- GCC_except_table4160
- GCC_except_table4163
- GCC_except_table4166
- GCC_except_table4171
- GCC_except_table4184
- GCC_except_table4189
- GCC_except_table4195
- GCC_except_table4198
- GCC_except_table4209
- GCC_except_table4217
- GCC_except_table4224
- GCC_except_table4230
- GCC_except_table4231
- GCC_except_table4234
- GCC_except_table4235
- GCC_except_table4253
- GCC_except_table4255
- GCC_except_table4257
- GCC_except_table4258
- GCC_except_table4261
- GCC_except_table4267
- GCC_except_table4270
- GCC_except_table4272
- GCC_except_table4278
- GCC_except_table4280
- GCC_except_table4283
- GCC_except_table4294
- GCC_except_table4305
- GCC_except_table4307
- GCC_except_table4316
- GCC_except_table4318
- GCC_except_table4320
- GCC_except_table4326
- GCC_except_table4586
- GCC_except_table4592
- GCC_except_table4609
- GCC_except_table4613
- GCC_except_table4630
- GCC_except_table4638
- GCC_except_table4651
- GCC_except_table4665
- GCC_except_table4669
- GCC_except_table4782
- GCC_except_table5238
- GCC_except_table5246
- GCC_except_table5257
- GCC_except_table5302
- GCC_except_table5304
- GCC_except_table5305
- GCC_except_table5387
- GCC_except_table5388
- GCC_except_table5389
- GCC_except_table5390
- GCC_except_table5391
- GCC_except_table5392
- GCC_except_table5398
- GCC_except_table5399
- GCC_except_table5401
- GCC_except_table5408
- GCC_except_table5411
- GCC_except_table5413
- GCC_except_table5418
- GCC_except_table5421
- GCC_except_table5424
- GCC_except_table5428
- GCC_except_table5432
- GCC_except_table545
- GCC_except_table556
- GCC_except_table572
- GCC_except_table584
- GCC_except_table5918
- GCC_except_table5919
- GCC_except_table5938
- GCC_except_table5948
- GCC_except_table5951
- GCC_except_table618
- GCC_except_table6230
- GCC_except_table6234
- GCC_except_table6279
- GCC_except_table6283
- GCC_except_table6285
- GCC_except_table6287
- GCC_except_table630
- GCC_except_table631
- GCC_except_table633
- GCC_except_table636
- GCC_except_table639
- GCC_except_table6489
- GCC_except_table6495
- GCC_except_table6499
- GCC_except_table6500
- GCC_except_table6501
- GCC_except_table6502
- GCC_except_table6508
- GCC_except_table6524
- GCC_except_table653
- GCC_except_table6560
- GCC_except_table6561
- GCC_except_table6562
- GCC_except_table657
- GCC_except_table6582
- GCC_except_table6594
- GCC_except_table6597
- GCC_except_table6602
- GCC_except_table6604
- GCC_except_table661
- GCC_except_table6618
- GCC_except_table668
- GCC_except_table6853
- GCC_except_table6866
- GCC_except_table6871
- GCC_except_table6874
- GCC_except_table6875
- GCC_except_table6877
- GCC_except_table6878
- GCC_except_table6880
- GCC_except_table6910
- GCC_except_table6932
- GCC_except_table6936
- GCC_except_table6940
- GCC_except_table6945
- GCC_except_table6949
- GCC_except_table6953
- GCC_except_table6957
- GCC_except_table6961
- GCC_except_table6969
- GCC_except_table6971
- GCC_except_table6975
- GCC_except_table7039
- GCC_except_table7040
- GCC_except_table7041
- GCC_except_table7042
- GCC_except_table7043
- GCC_except_table7044
- GCC_except_table7045
- GCC_except_table705
- GCC_except_table7107
- GCC_except_table7117
- GCC_except_table7118
- GCC_except_table7133
- GCC_except_table7134
- GCC_except_table7142
- GCC_except_table7148
- GCC_except_table7161
- GCC_except_table7164
- GCC_except_table7165
- GCC_except_table7170
- GCC_except_table7173
- GCC_except_table7180
- GCC_except_table7183
- GCC_except_table7197
- GCC_except_table7204
- GCC_except_table7210
- GCC_except_table7219
- GCC_except_table7221
- GCC_except_table7227
- GCC_except_table7228
- GCC_except_table723
- GCC_except_table7235
- GCC_except_table7259
- GCC_except_table7265
- GCC_except_table7269
- GCC_except_table7270
- GCC_except_table7273
- GCC_except_table7279
- GCC_except_table7287
- GCC_except_table7291
- GCC_except_table7295
- GCC_except_table7409
- GCC_except_table7446
- GCC_except_table750
- GCC_except_table7503
- GCC_except_table7506
- GCC_except_table7513
- GCC_except_table7519
- GCC_except_table7526
- GCC_except_table7527
- GCC_except_table754
- GCC_except_table7543
- GCC_except_table7547
- GCC_except_table7548
- GCC_except_table7549
- GCC_except_table757
- GCC_except_table759
- GCC_except_table7598
- GCC_except_table7599
- GCC_except_table7601
- GCC_except_table7604
- GCC_except_table7631
- GCC_except_table7637
- GCC_except_table7657
- GCC_except_table7675
- GCC_except_table7676
- GCC_except_table7677
- GCC_except_table7686
- GCC_except_table7691
- GCC_except_table7692
- GCC_except_table7693
- GCC_except_table7708
- GCC_except_table771
- GCC_except_table7711
- GCC_except_table7725
- GCC_except_table773
- GCC_except_table7730
- GCC_except_table7736
- GCC_except_table7748
- GCC_except_table7749
- GCC_except_table7754
- GCC_except_table7763
- GCC_except_table7771
- GCC_except_table7772
- GCC_except_table7778
- GCC_except_table7780
- GCC_except_table7784
- GCC_except_table7807
- GCC_except_table7808
- GCC_except_table7834
- GCC_except_table792
- GCC_except_table798
- GCC_except_table7999
- GCC_except_table8062
- GCC_except_table8094
- GCC_except_table8097
- GCC_except_table813
- GCC_except_table814
- GCC_except_table819
- GCC_except_table822
- GCC_except_table825
- GCC_except_table8264
- GCC_except_table830
- GCC_except_table8302
- GCC_except_table8339
- GCC_except_table834
- GCC_except_table8428
- GCC_except_table8430
- GCC_except_table8432
- GCC_except_table8434
- GCC_except_table8436
- GCC_except_table8438
- GCC_except_table8440
- GCC_except_table8443
- GCC_except_table8445
- GCC_except_table8447
- GCC_except_table8449
- GCC_except_table845
- GCC_except_table8451
- GCC_except_table8454
- GCC_except_table8456
- GCC_except_table8458
- GCC_except_table8467
- GCC_except_table8473
- GCC_except_table8478
- GCC_except_table8481
- GCC_except_table8486
- GCC_except_table8491
- GCC_except_table8494
- GCC_except_table8497
- GCC_except_table8523
- GCC_except_table8526
- GCC_except_table8527
- GCC_except_table8546
- GCC_except_table8547
- GCC_except_table8551
- GCC_except_table8553
- GCC_except_table8555
- GCC_except_table8557
- GCC_except_table8564
- GCC_except_table8565
- GCC_except_table8569
- GCC_except_table8620
- GCC_except_table8627
- GCC_except_table871
- GCC_except_table8731
- GCC_except_table8735
- GCC_except_table8739
- GCC_except_table8742
- GCC_except_table8746
- GCC_except_table8748
- GCC_except_table8749
- GCC_except_table8751
- GCC_except_table8753
- GCC_except_table8758
- GCC_except_table8760
- GCC_except_table8761
- GCC_except_table878
- GCC_except_table885
- GCC_except_table886
- GCC_except_table902
- GCC_except_table924
- GCC_except_table93
- GCC_except_table942
- GCC_except_table964
- GCC_except_table968
- GCC_except_table982
- GCC_except_table987
- __111-[HAP2AccessoryServerSecureTransportPairVerify securitySession:didReceiveLocalPairingIdentityRequestWithError:]_block_invoke
- __124-[HAP2AccessoryServerSecureTransportPairVerify securitySession:didReceiveRequestForPeerPairingIdentityWithIdentifier:error:]_block_invoke
- __45-[HAP2AccessoryServerController closeSession]_block_invoke
- __67-[HAP2AccessoryServerCoordinator _didDiscoverAccessory:completion:]_block_invoke
- __78-[HAPAccessoryServerBrowserHAP2Adapter discoverAccessoryServerWithIdentifier:]_block_invoke
- __78-[HAPAccessoryServerBrowserHAP2Adapter discoverAccessoryServerWithIdentifier:]_block_invoke_2
- __91-[HAP2AccessoryServerSecureTransportPairVerify ecdsaLongTermPublicKeyOfPeerWithIdentifier:]_block_invoke
- ___105-[HAP2AccessoryServerSecureTransportPairVerify localPairingIdentityOfECDSAKeyPairSetupSession:withError:]_block_invoke
- ___105-[HAP2AccessoryServerSecureTransportPairVerify localPairingIdentityOfECDSAKeyPairSetupSession:withError:]_block_invoke_2
- ___109-[HAP2AccessoryServerController secureTransport:needsECDSALongTermPublicKeyForPeerWithIdentifier:completion:]_block_invoke
- ___110-[HAP2AccessoryServer(Unpaired) pairingDriver:didSaveRemoteECDSAPairingKey:forAccessoryIdentifier:completion:]_block_invoke
- ___111-[HAP2AccessoryServerSecureTransportPairVerify securitySession:didReceiveLocalPairingIdentityRequestWithError:]_block_invoke
- ___111-[HAP2AccessoryServerSecureTransportPairVerify securitySession:didReceiveLocalPairingIdentityRequestWithError:]_block_invoke_2
- ___113-[HAP2AccessoryServerController secureTransport:needsLocalPairingIdentityForECDSAKeyPairSetupSession:completion:]_block_invoke
- ___117-[HAP2AccessoryServerPairingDriverPairSetupWorkItem pairSetupSession:didReceiveLocalPairingIdentityRequestWithError:]_block_invoke
- ___118-[HAP2AccessoryServerPairingDriverPairSetupWorkItem pairSetupSession:didPairWithPeerIdentifier:ecdsaPairingKey:error:]_block_invoke
- ___124-[HAP2AccessoryServerSecureTransportPairVerify securitySession:didReceiveRequestForPeerPairingIdentityWithIdentifier:error:]_block_invoke
- ___124-[HAP2AccessoryServerSecureTransportPairVerify securitySession:didReceiveRequestForPeerPairingIdentityWithIdentifier:error:]_block_invoke_2
- ___43-[HAP2AccessoryServer(Paired) closeSession]_block_invoke
- ___45-[HAP2AccessoryServerController closeSession]_block_invoke
- ___64-[HAP2AccessoryServer _browserFastSetHasDiscoveryAdvertisement:]_block_invoke
- ___67-[HAP2AccessoryServerCoordinator _didDiscoverAccessory:completion:]_block_invoke
- ___87-[HAP2AccessoryServer(Unpaired) pairingDriver:didSaveRemotePairingIdentity:completion:]_block_invoke
- ___91-[HAP2AccessoryServerSecureTransportPairVerify ecdsaLongTermPublicKeyOfPeerWithIdentifier:]_block_invoke
- ___91-[HAP2AccessoryServerSecureTransportPairVerify ecdsaLongTermPublicKeyOfPeerWithIdentifier:]_block_invoke_2
- ___92-[HAP2AccessoryServer(Unpaired) pairingDriver:didRequestLocalPairingIdentityWithCompletion:]_block_invoke
- ___92-[HAP2AccessoryServerPairingDriverPairSetupWorkItem pairSetupSession:didPairWithPeer:error:]_block_invoke
- ___98-[HAP2AccessoryServerController secureTransport:needsRemotePairingIdentityForDeviceID:completion:]_block_invoke
- ___block_descriptor_40_e8_32bs_e28_v24?0"NSData"8"NSError"16l
- ___block_descriptor_48_e8_32r40r_e69_v32?0"HAP2AccessoryServerDiscoveryBonjourBrowseResultTuple"8Q16^B24l
- ___block_descriptor_48_e8_32s40bs_e40_v24?0"HAPPairingIdentity"8"NSError"16l
- ___block_descriptor_48_e8_32s40r_e17_v16?0"NSError"8l
- ___block_descriptor_56_e8_32s40r48r_e28_v24?0"NSData"8"NSError"16l
- ___block_descriptor_56_e8_32s40r48r_e40_v24?0"HAPPairingIdentity"8"NSError"16l
- ___block_descriptor_56_e8_32s40s48bs_e40_v24?0"HAPECDSAPairingKey"8"NSError"16l
- ___block_descriptor_80_e8_32s40s48s56s64r72r_e5_v8?0l
- ___copy_helper_block_e8_32s40s48s56s64r72r
- ___destroy_helper_block_e8_32s40s48s56s64r72r
- __swift_closure_destructor.181Tm
- _objc_msgSend$_browserFastSetHasDiscoveryAdvertisement:
- _objc_msgSend$_didDiscoverAccessory:completion:
- _objc_msgSend$fetchControllerKeyForECDSAKeyAccessory:completion:
- _objc_msgSend$fetchKeysForIdentifiers:completion:
- _objc_msgSend$initWithSFrameEnabled:
- _objc_msgSend$initWithSessionIdentifier:viewerParticipantID:viewerNegotiationBlob:
- _objc_msgSend$pairingDriver:didRequestLocalPairingIdentityWithCompletion:
- _objc_msgSend$pairingDriver:didSaveRemoteECDSAPairingKey:forAccessoryIdentifier:completion:
- _objc_msgSend$pairingDriver:didSaveRemotePairingIdentity:completion:
- _objc_msgSend$saveECDSAKey:forAccessoryName:completion:
- _objc_msgSend$savePublicKey:forAccessoryWithID:completion:
- _objc_msgSend$secureTransport:needsECDSALongTermPublicKeyForPeerWithIdentifier:completion:
- _objc_msgSend$secureTransport:needsLocalPairingIdentityForECDSAKeyPairSetupSession:completion:
- _objc_msgSend$secureTransport:needsLocalPairingIdentityWithCompletion:
- _objc_msgSend$secureTransport:needsRemotePairingIdentityForDeviceID:completion:
- logCategory._hmf_once_t13
- logCategory._hmf_once_t267
- logCategory._hmf_once_t47
- logCategory._hmf_once_t69
- logCategory._hmf_once_t79
- logCategory._hmf_once_t83
- logCategory._hmf_once_t856
- logCategory._hmf_once_t98
- logCategory._hmf_once_v14
- logCategory._hmf_once_v268
- logCategory._hmf_once_v48
- logCategory._hmf_once_v70
- logCategory._hmf_once_v80
- logCategory._hmf_once_v84
- logCategory._hmf_once_v857
- logCategory._hmf_once_v99
CStrings:
+ "%@ Lock-only-set hasDiscoveryAdvertisement=%{public}d"
+ "%@ Not announcing re-established session (readingAttributeDatabase=%@, accessories=%lu)"
+ "%@ Session %lu already announced, skipping re-establish"
+ "%s|%s|%s"
+ "(none)"
+ "(unprintable)"
+ ", Should Allow ECDSA Key Pair Setup: %@"
+ "000000-0000"
+ ": "
+ "<%@: %p primary=%lu secondary=%lu>"
+ "<HAPAVCStreamingControlCommandWrapper value=%@>"
+ "<HAPAVCStreamingControlRequest sessionIdentifier=%@, command=%@>"
+ "<HAPAVCStreamingControlResponse sessionIdentifier=%@, status=%@>"
+ "<HAPAVCStreamingControlStatusWrapper value=%@>"
+ "<HAPAVCViewerRegistrationOperationWrapper value=%@>"
+ "<HAPAVCViewerRegistrationRequest sessionIdentifier=%@, viewerParticipantID=%@, viewerNegotiationBlob=%@, operation=%@>"
+ "<HAPWebRTCOfferOptions SFrameEnabled=%@, SFrameConfiguration=%@>"
+ "B5"
+ "CoreThreadRadio framework not available"
+ "Disconnect request is not supported for %{public}@"
+ "Failed to create XPC dictionary"
+ "Failed to get Thread mesh local prefix: empty string"
+ "Failed to get Thread mesh local prefix: invalid XPC response type"
+ "Failed to get Thread mesh local prefix: property value is not a string"
+ "Found thread accessory with server ID known = %d paired = %d"
+ "HAPAVCStreamingControlCommandEnd"
+ "HAPAVCStreamingControlStatusError"
+ "HAPAVCStreamingControlStatusSuccess"
+ "HAPAVCStreamingControlStatusUnknownSessionIdentifier"
+ "HAPAVCViewerRegistrationOperationDeregister"
+ "HAPAVCViewerRegistrationOperationRegister"
+ "HAPAVCViewerRegistrationStatusUnknownParticipant"
+ "HAPErrorAlreadyPairedPeerIdentifierKey"
+ "HAPMetadataCharacteristic %@(%@): description: %@"
+ "HAPMetadataUnit %@: description: %@"
+ "IPv6:MeshLocalPrefix"
+ "Legacy WAC accessory Bonjour event - hasPairings %d continuingLegacyPairing: %d"
+ "M%hhu: accessory rejected pair-setup with error %llu (%{public}s) — failing with HAP error %ld"
+ "M5: owner additional-pairing info unavailable, failing pair-setup: %{public}s"
+ "MFi early-auth: DISMISSED — the tap-time validate+roll does not cover M4's full token (%ld bytes); abandoning it and validating the M4 token"
+ "MFi early-auth: M4 echoed the tap-time token and its validate+roll already finished — using its result for M5"
+ "MFi early-auth: M4 echoed the tap-time token but its validate+roll is still in flight — M5 will continue when it returns"
+ "MFi early-auth: M4 hash verified and validate+roll already finished — resolving M5 from its result"
+ "MFi early-auth: the adopted validate+roll returned nothing usable; validating M4's echoed token instead"
+ "MFi early-auth: the tap-time validate+roll has nothing usable for M4's echoed token; validating it instead"
+ "MFi pre-consent roll: consuming the result that arrived during the consent wait"
+ "MFi pre-consent roll: finished after %{public}sms, before consent; parking its result until commit"
+ "MFi pre-consent roll: still in flight at consent after %{public}sms; M5 will continue when it returns"
+ "MFi pre-consent roll: validating M4's token during the consent wait, off the on-tag critical path"
+ "MFi validate+roll resolved after teardown — discarding"
+ "NLM-ADDR %@ _setIpAddress: %{private}s -> %{private}s"
+ "Pair Setup completed with err: %d, MFi Cert %@"
+ "Pair-setup after M4, flags %08X productData %@"
+ "Pair-setup: M5 failed, ending pair-setup: %{public}s"
+ "PropVal"
+ "Refusing AES-CCM pair-setup: primary resident does not support ECDSA keys (featureFlags=0x%llx)"
+ "Refusing AES-CCM pair-setup: primary resident does not support ECDSA keys (featureFlags=0x%x)"
+ "Refusing AES-CCM pair-setup: primary resident does not support ECDSA keys (features=0x%llx)"
+ "Retrieved Thread mesh local prefix: %{private}@"
+ "Returning ECDSA local pairing identity for security session: %@, with error: %@"
+ "Tearing down session as a result of disconnect with completion call"
+ "Thread mesh local prefix property not found in response"
+ "Timed out, Not handling pending Bonjour for %{public}@, as session restore is active"
+ "Unknown HAPAVCStreamingControlCommand %ld"
+ "Unknown HAPAVCStreamingControlStatus %ld"
+ "Unknown HAPAVCViewerRegistrationOperation %ld"
+ "Using Pairing Identity: %{public}@"
+ "[%{public}@] Disconnect request is not supported for %{public}@"
+ "[%{public}@] Found thread accessory with server ID known = %d paired = %d"
+ "[%{public}@] HAPMetadataCharacteristic %@(%@): description: %@"
+ "[%{public}@] HAPMetadataUnit %@: description: %@"
+ "[%{public}@] Legacy WAC accessory Bonjour event - hasPairings %d continuingLegacyPairing: %d"
+ "[%{public}@] Pair Setup completed with err: %d, MFi Cert %@"
+ "[%{public}@] Pair-setup after M4, flags %08X productData %@"
+ "[%{public}@] Refusing AES-CCM pair-setup: primary resident does not support ECDSA keys (featureFlags=0x%llx)"
+ "[%{public}@] Refusing AES-CCM pair-setup: primary resident does not support ECDSA keys (featureFlags=0x%x)"
+ "[%{public}@] Refusing AES-CCM pair-setup: primary resident does not support ECDSA keys (features=0x%llx)"
+ "[%{public}@] Returning ECDSA local pairing identity for security session: %@, with error: %@"
+ "[%{public}@] Tearing down session as a result of disconnect with completion call"
+ "[%{public}@] Timed out, Not handling pending Bonjour for %{public}@, as session restore is active"
+ "[%{public}@] [IP Accessory Server HTTP Client] Failed to get self address %d client ref %p"
+ "[IP Accessory Server HTTP Client] Failed to get self address %d client ref %p"
+ "com.apple.CoreHAP.HAP2ThreadNetworkUtil.events"
+ "v32@?0@\"NSData\"8@\"NSString\"16@\"NSError\"24"
+ "\x81\xf0\xf0A!"
- "\"5"
- "%@ Browser fast-set hasDiscoveryAdvertisement=%{public}d"
- "%@ Failed to fetch ECDSA controller key for %@: %@"
- "%@ Failed to fetch ECDSA key for peer %@: %@"
- "&"
- "<HAPAVCViewerRegistrationRequest sessionIdentifier=%@, viewerParticipantID=%@, viewerNegotiationBlob=%@>"
- "<HAPWebRTCOfferOptions SFrameEnabled=%@>"
- "HAPAVCNegotiationStatusBusy"
- "HAPAVCNegotiationStatusUnknownSessionIdentifier"
- "HAPMetadataCharacteristic %@(%@):  description: %@"
- "HAPMetadataUnit %@:  description: %@"
- "Key Bag Pairing Identity to derive ECDSA Key: %@"
- "Legacy WAC accessory Bonjour event - hasPairings %d  continuingLegacyPairing: %d"
- "MFi early-auth: DISMISSED — M4 sent a full token (%ld bytes), not the primed hash; abandoning tap-time validate+roll, validating M4 token"
- "MFi early-auth: M4 hash verified and validate+roll already finished — using its result for M5"
- "Pair Setup completed with err: %d,  MFi Cert %@"
- "Pair-setup M6 bad status %hhu"
- "Pair-setup after M4, flags %08X  productData %@"
- "Pair-setup: M5: Unable to retrieve pairing identity: %s"
- "Returning ECDSA local pairng identity for security session: %@, with error: %@"
- "Secure Transport PairVerify: Timed out waiting for ECDSA key for peer %@"
- "Secure Transport PairVerify: Timed out waiting for local ECDSA pair-setup identity"
- "Secure Transport PairVerify: Timed out waiting for local pairing identity"
- "Secure Transport PairVerify: Timed out waiting for remote pairing identity"
- "Timed out,  Not handling pending Bonjour for %{public}@, as session restore is active"
- "Using ECDSA Controller Pairing Identity: %@"
- "Using Pairing Identity: %@"
- "[%{public}@] HAPMetadataCharacteristic %@(%@):  description: %@"
- "[%{public}@] HAPMetadataUnit %@:  description: %@"
- "[%{public}@] Legacy WAC accessory Bonjour event - hasPairings %d  continuingLegacyPairing: %d"
- "[%{public}@] Pair Setup completed with err: %d,  MFi Cert %@"
- "[%{public}@] Pair-setup after M4, flags %08X  productData %@"
- "[%{public}@] Returning ECDSA local pairng identity for security session: %@, with error: %@"
- "[%{public}@] Timed out,  Not handling pending Bonjour for %{public}@, as session restore is active"
- "\x81\xf0\xb1!"
```
