## CoreHAP

> `/System/Library/PrivateFrameworks/CoreHAP.framework/Versions/A/CoreHAP`

```diff

-1490.2.0.0.0
-  __TEXT.__text: 0x21625c
-  __TEXT.__objc_methlist: 0x17010
-  __TEXT.__const: 0x7e0
-  __TEXT.__gcc_except_tab: 0x5600
-  __TEXT.__cstring: 0x135e5
-  __TEXT.__oslogstring: 0x3909f
-  __TEXT.__unwind_info: 0x6938
+1493.1.5.4.1
+  __TEXT.__text: 0x2b51a4
+  __TEXT.__objc_methlist: 0x17d80
+  __TEXT.__const: 0x11c8
+  __TEXT.__constg_swiftt: 0x960
+  __TEXT.__swift5_typeref: 0x3e4
+  __TEXT.__swift5_builtin: 0x50
+  __TEXT.__swift5_reflstr: 0x474
+  __TEXT.__swift5_fieldmd: 0x3f0
+  __TEXT.__swift5_assocty: 0xc0
+  __TEXT.__swift5_proto: 0x50
+  __TEXT.__swift5_types: 0x30
+  __TEXT.__cstring: 0x13d35
+  __TEXT.__oslogstring: 0x3d570
+  __TEXT.__swift5_capture: 0x288
+  __TEXT.__gcc_except_tab: 0x5890
+  __TEXT.__unwind_info: 0x7330
+  __TEXT.__eh_frame: 0x1080
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2110
-  __DATA_CONST.__objc_classlist: 0xba8
+  __DATA_CONST.__const: 0x2148
+  __DATA_CONST.__objc_classlist: 0xbf8
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x338
+  __DATA_CONST.__objc_protolist: 0x390
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7888
-  __DATA_CONST.__objc_protorefs: 0xc0
-  __DATA_CONST.__objc_superrefs: 0xa20
+  __DATA_CONST.__objc_selrefs: 0x7c28
+  __DATA_CONST.__objc_protorefs: 0x100
+  __DATA_CONST.__objc_superrefs: 0xa40
   __DATA_CONST.__objc_arraydata: 0x200
-  __DATA_CONST.__got: 0xd88
-  __AUTH_CONST.__const: 0x4500
-  __AUTH_CONST.__cfstring: 0xf5c0
-  __AUTH_CONST.__objc_const: 0x28c78
-  __AUTH_CONST.__objc_intobj: 0x570
+  __DATA_CONST.__got: 0xfb8
+  __AUTH_CONST.__const: 0x5468
+  __AUTH_CONST.__cfstring: 0xf7a0
+  __AUTH_CONST.__objc_const: 0x29fc8
+  __AUTH_CONST.__objc_intobj: 0x588
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0xc0
-  __AUTH_CONST.__auth_got: 0x980
-  __AUTH.__objc_data: 0x64f0
+  __AUTH_CONST.__auth_got: 0x10b0
+  __AUTH.__objc_data: 0x7228
+  __AUTH.__data: 0xb0
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x28
-  __DATA.__objc_ivar: 0x17ac
-  __DATA.__data: 0x26c2
+  __DATA.__objc_ivar: 0x17fc
+  __DATA.__data: 0x2c22
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x388
-  __DATA_DIRTY.__objc_data: 0xfa0
-  __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x78
+  __DATA.__bss: 0xd80
+  __DATA.__common: 0x8
+  __DATA_DIRTY.__objc_data: 0xfc8
+  __DATA_DIRTY.__data: 0x40
+  __DATA_DIRTY.__bss: 0x88
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libdns_services.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8639
-  Symbols:   18916
-  CStrings:  6205
+  Functions: 9510
+  Symbols:   19560
+  CStrings:  6554
 
Symbols:
+ +[HAPECDSAConversion ecdsaPrivateKeyFrom352bitRandomData:error:]
+ +[HAPECDSAPairingKey supportsSecureCoding]
+ +[HAPPairingUtilities createAddPairingRequestForPairing:error:]
+ -[HAP2AccessoryServer _handleDiscoveredRemovedAccessories:]
+ -[HAP2AccessoryServer removedAccessoryECDSAKey]
+ -[HAP2AccessoryServer setRemovedAccessoryECDSAKey:]
+ -[HAP2AccessoryServer(Unpaired) getPairingsWithRemovedAccessoryECDSAKey:completion:]
+ -[HAP2AccessoryServer(Unpaired) pairingDriver:didSaveRemoteECDSAPairingKey:forAccessoryIdentifier:completion:]
+ -[HAP2AccessoryServer(Unpaired) pairingDriver:requestPairVerifyTLKWithCompletion:]
+ -[HAP2AccessoryServer(Unpaired) removeUnpairedAccessoryPairing:ecdsaAccessoryKey:completion:]
+ -[HAP2AccessoryServer(Unpaired) updateRemovedAccessoriesWithReason:ecdsaAccessoryKey:completion:]
+ -[HAP2AccessoryServerController operationQueue]
+ -[HAP2AccessoryServerController secureTransport:checkECDSACapabilityWithCompletion:]
+ -[HAP2AccessoryServerController secureTransport:needsECDSALongTermPublicKeyForPeerWithIdentifier:completion:]
+ -[HAP2AccessoryServerController secureTransport:needsLocalPairingIdentityForECDSAKeyPairSetupSession:completion:]
+ -[HAP2AccessoryServerController secureTransport:needsNetworkConfigurationForPairSetupSession:completion:]
+ -[HAP2AccessoryServerController secureTransport:needsPairVerifyTLKsWithCompletion:]
+ -[HAP2AccessoryServerController secureTransport:needsSetupCodeForPairSetupSession:completion:]
+ -[HAP2AccessoryServerPairingDriverPairSetupWorkItem pairSetupSession:didPairWithPeerIdentifier:ecdsaPairingKey:error:]
+ -[HAP2AccessoryServerPairingDriverPairSetupWorkItem pairSetupSession:didReceiveAdditionalPairingRequestWithPairingIdentifier:ecdsaPublicKey:error:]
+ -[HAP2AccessoryServerPairingDriverPairSetupWorkItem pairSetupSession:didReceiveThreadNetworkConfigurationTLVRequestWithCompletionHandler:]
+ -[HAP2AccessoryServerPairingDriverPairSetupWorkItem pairSetupSession:didReceiveWiFiNetworkConfigurationTLVRequestWithCompletionHandler:]
+ -[HAP2AccessoryServerSecureTransportPairVerify _attemptECDSAKeyPairVerify]
+ -[HAP2AccessoryServerSecureTransportPairVerify _createECDSAKeyPairVerifySession]
+ -[HAP2AccessoryServerSecureTransportPairVerify _createSecuritySessionFromECDSASession]
+ -[HAP2AccessoryServerSecureTransportPairVerify _handleECDSASessionFailure:]
+ -[HAP2AccessoryServerSecureTransportPairVerify ecdsaKeyPairVerifySession]
+ -[HAP2AccessoryServerSecureTransportPairVerify ecdsaKeySecuritySessionOpen]
+ -[HAP2AccessoryServerSecureTransportPairVerify ecdsaLongTermPublicKeyOfPeerWithIdentifier:]
+ -[HAP2AccessoryServerSecureTransportPairVerify localPairingIdentityOfECDSAKeyPairSetupSession:withError:]
+ -[HAP2AccessoryServerSecureTransportPairVerify pairSetupSession:didPairWithPeer:error:]
+ -[HAP2AccessoryServerSecureTransportPairVerify pairSetupSession:didReceiveLocalPairingIdentityRequestWithError:]
+ -[HAP2AccessoryServerSecureTransportPairVerify pairSetupSession:didReceiveSetupExchangeData:]
+ -[HAP2AccessoryServerSecureTransportPairVerify pairSetupSession:didStopWithError:]
+ -[HAP2AccessoryServerSecureTransportPairVerify setEcdsaKeyPairVerifySession:]
+ -[HAP2AccessoryServerSecureTransportPairVerify setEcdsaKeySecuritySessionOpen:]
+ -[HAPAccessoryServer associateAccessoryWithControllerKey:usingAccessoryECDSAPairingKey:]
+ -[HAPAccessoryServer associateAccessoryWithControllerKeyUsingAccessoryECDSAPairingKey:]
+ -[HAPAccessoryServer enableRemovedAccessoryKey:ecdsaAccessoryKey:completionQueue:completion:]
+ -[HAPAccessoryServer removePairingsWithRemovedAccessoryKey:ecdsaAccessoryKey:queue:completion:]
+ -[HAPAccessoryServer removedAccessoryECDSAKey]
+ -[HAPAccessoryServer setRemovedAccessoryECDSAKey:]
+ -[HAPAccessoryServerHAP2Adapter accessoryServer:requestPairVerifyTLKWithCompletion:]
+ -[HAPAccessoryServerHAP2Adapter enableRemovedAccessoryKey:ecdsaAccessoryKey:completionQueue:completion:]
+ -[HAPAccessoryServerIP _ensurePairingSessionIsInitializedWithType:completion:]
+ -[HAPAccessoryServerIP _pairingCompletedWithError:]
+ -[HAPAccessoryServerIP _queueAddPairingForPairing:queue:completion:]
+ -[HAPAccessoryServerIP _startAddPairingForPairing:queue:completion:]
+ -[HAPAccessoryServerIP ecdsaLongTermPublicKeyOfPeerWithIdentifier:]
+ -[HAPAccessoryServerIP hasECDSAKeySession]
+ -[HAPAccessoryServerIP httpResponseHandler]
+ -[HAPAccessoryServerIP localPairingIdentityOfECDSAKeyPairSetupSession:withError:]
+ -[HAPAccessoryServerIP pairSetupSession:didPairWithPeer:error:]
+ -[HAPAccessoryServerIP pairSetupSession:didPairWithPeerIdentifier:ecdsaPairingKey:error:]
+ -[HAPAccessoryServerIP pairSetupSession:didReceiveAdditionalPairingRequestWithPairingIdentifier:ecdsaPublicKey:error:]
+ -[HAPAccessoryServerIP pairSetupSession:didReceiveBackoffRequestWithTimeInterval:]
+ -[HAPAccessoryServerIP pairSetupSession:didReceiveLocalPairingIdentityRequestWithError:]
+ -[HAPAccessoryServerIP pairSetupSession:didReceiveProductData:]
+ -[HAPAccessoryServerIP pairSetupSession:didReceiveSetupCodeRequestWithCompletionHandler:]
+ -[HAPAccessoryServerIP pairSetupSession:didReceiveSetupExchangeData:]
+ -[HAPAccessoryServerIP pairSetupSession:didReceiveThreadNetworkConfigurationTLVRequestWithCompletionHandler:]
+ -[HAPAccessoryServerIP pairSetupSession:didReceiveWiFiNetworkConfigurationTLVRequestWithCompletionHandler:]
+ -[HAPAccessoryServerIP pairSetupSession:didStopWithError:]
+ -[HAPAccessoryServerIP pairSetupSessionDidReceiveInvalidSetupCode:]
+ -[HAPAccessoryServerIP pairSetupSession]
+ -[HAPAccessoryServerIP pairVerifySession]
+ -[HAPAccessoryServerIP setHttpResponseHandler:]
+ -[HAPAccessoryServerIP setPairSetupSession:]
+ -[HAPAccessoryServerIP setPairVerifySession:]
+ -[HAPAccessoryServerIP setSetupCodeCompletionHandler:]
+ -[HAPAccessoryServerIP setupCodeCompletionHandler]
+ -[HAPAdditionalWifiData .cxx_destruct]
+ -[HAPAdditionalWifiData bssid]
+ -[HAPAdditionalWifiData channelNumber]
+ -[HAPAdditionalWifiData copyWithZone:]
+ -[HAPAdditionalWifiData initWithOperatingClass:channelNumber:bssid:]
+ -[HAPAdditionalWifiData init]
+ -[HAPAdditionalWifiData operatingClass]
+ -[HAPAdditionalWifiData setBssid:]
+ -[HAPAdditionalWifiData setChannelNumber:]
+ -[HAPAdditionalWifiData setOperatingClass:]
+ -[HAPECDSAPairingKey .cxx_destruct]
+ -[HAPECDSAPairingKey copyWithZone:]
+ -[HAPECDSAPairingKey data]
+ -[HAPECDSAPairingKey encodeWithCoder:]
+ -[HAPECDSAPairingKey hash]
+ -[HAPECDSAPairingKey hmf_appendAttributeDescriptionsToString:options:]
+ -[HAPECDSAPairingKey initWithCoder:]
+ -[HAPECDSAPairingKey initWithPairingKeyType:data:]
+ -[HAPECDSAPairingKey isEqual:]
+ -[HAPECDSAPairingKey keyType]
+ -[HAPKeyBag(AccessoryUtils) associateECDSAKeyAccessoryControllerIdentifier:error:]
+ -[HAPMetadataTuple hmf_fastEncodedSize]
+ -[HAPPairing .cxx_destruct]
+ -[HAPPairing ecdsaPairing]
+ -[HAPPairing ed25519PairingIdentity]
+ -[HAPPairing initWithECDSAPairing:]
+ -[HAPPairing initWithEd25519PairingIdentity:]
+ -[HAPPairingECDSAKey .cxx_destruct]
+ -[HAPPairingECDSAKey identifier]
+ -[HAPPairingECDSAKey initWithIdentifier:publicKey:permissions:]
+ -[HAPPairingECDSAKey permissions]
+ -[HAPPairingECDSAKey publicKey]
+ -[HAPPairingIdentity ecdsaPublicKey]
+ -[HAPSecuritySession _handleSetupExchangeCompleteWithForeignPairVerifySession:]
+ -[HAPSecuritySession handleSetupExchangeCompleteWithForeignPairVerifySession:]
+ -[HAPSystemKeychainStore _getControllerPublicKey:secretKey:keyPair:username:allowCreation:forECDSAKeyAccessory:error:]
+ -[HAPSystemKeychainStore _getECDSAPairingKey:registeredWithHomeKit:forAccessoryName:]
+ -[HAPSystemKeychainStore _saveECDSAPairingKey:forAccessoryName:]
+ -[HAPSystemKeychainStore cloneRemovedAccessoryECDSAKeyForName:iCloudIdentifier:error:]
+ -[HAPSystemKeychainStore createHH2ControllerKey:secretKey:keyPair:ecdsaPrivateKey:ecdsaPublicKey:username:]
+ -[HAPSystemKeychainStore deleteDeferredMatterOnboardingPayloadForAccessoryUUID:error:]
+ -[HAPSystemKeychainStore deleteRemovedAccessoryECDSAKeyForName:error:]
+ -[HAPSystemKeychainStore ecdsaPairingKeyExistsForAccessoryName:]
+ -[HAPSystemKeychainStore establishRelationshipBetweenControllerKeyAndAccessoryECDSAPairingKey:accessoryPairingIdentifier:controllerKeyIdentifier:error:]
+ -[HAPSystemKeychainStore getAssociatedControllerKeyForECDSAKeyAccessory:]
+ -[HAPSystemKeychainStore getControllerPublicKey:secretKey:username:allowCreation:forECDSAKeyAccessory:error:]
+ -[HAPSystemKeychainStore getHH2ControllerECDSAPublicKeyWithIdentifier:]
+ -[HAPSystemKeychainStore getOrCreateHH2ControllerKey:secretKey:keyPair:ecdsaPrivateKey:ecdsaPublicKey:username:]
+ -[HAPSystemKeychainStore readControllerPairingKeyForECDSAKeyAccessory:error:]
+ -[HAPSystemKeychainStore readDeferredMatterOnboardingPayloadForAccessoryUUID:error:]
+ -[HAPSystemKeychainStore readECDSAKeyForRemovedAccessoryName:iCloudIdentifier:error:]
+ -[HAPSystemKeychainStore readECDSAPairingKeyForAccessoryName:registeredWithHomeKit:error:]
+ -[HAPSystemKeychainStore saveDeferredMatterOnboardingPayload:forAccessoryUUID:error:]
+ -[HAPSystemKeychainStore saveECDSAPairingKey:forAccessoryName:error:]
+ -[_HAPAccessoryServerBTLE200 ecdsaKeyPairVerifySession]
+ -[_HAPAccessoryServerBTLE200 ecdsaKeySecuritySessionOpen]
+ -[_HAPAccessoryServerBTLE200 ecdsaLongTermPublicKeyOfPeerWithIdentifier:]
+ -[_HAPAccessoryServerBTLE200 enableRemovedAccessoryKey:ecdsaAccessoryKey:completionQueue:completion:]
+ -[_HAPAccessoryServerBTLE200 localPairingIdentityOfECDSAKeyPairSetupSession:withError:]
+ -[_HAPAccessoryServerBTLE200 pairSetupSession:didPairWithPeerIdentifier:ecdsaPairingKey:error:]
+ -[_HAPAccessoryServerBTLE200 pairSetupSession:didReceiveAdditionalPairingRequestWithPairingIdentifier:ecdsaPublicKey:error:]
+ -[_HAPAccessoryServerBTLE200 pairSetupSession:didReceiveThreadNetworkConfigurationTLVRequestWithCompletionHandler:]
+ -[_HAPAccessoryServerBTLE200 pairSetupSession:didReceiveWiFiNetworkConfigurationTLVRequestWithCompletionHandler:]
+ -[_HAPAccessoryServerBTLE200 setEcdsaKeyPairVerifySession:]
+ -[_HAPAccessoryServerBTLE200 setEcdsaKeySecuritySessionOpen:]
+ GCC_except_table1092
+ GCC_except_table1094
+ GCC_except_table1200
+ GCC_except_table1205
+ GCC_except_table1209
+ GCC_except_table1222
+ GCC_except_table1236
+ GCC_except_table1238
+ GCC_except_table1240
+ GCC_except_table1242
+ GCC_except_table1368
+ GCC_except_table1374
+ GCC_except_table1376
+ GCC_except_table1578
+ GCC_except_table1788
+ GCC_except_table1790
+ GCC_except_table1795
+ GCC_except_table1801
+ GCC_except_table1803
+ GCC_except_table1809
+ GCC_except_table1811
+ GCC_except_table1815
+ GCC_except_table1821
+ GCC_except_table1823
+ GCC_except_table1825
+ GCC_except_table1827
+ GCC_except_table1832
+ GCC_except_table1836
+ GCC_except_table1846
+ GCC_except_table1854
+ GCC_except_table1861
+ GCC_except_table1865
+ GCC_except_table1869
+ GCC_except_table1874
+ GCC_except_table1912
+ GCC_except_table2036
+ GCC_except_table2037
+ GCC_except_table2041
+ GCC_except_table2053
+ GCC_except_table2062
+ GCC_except_table2065
+ GCC_except_table2067
+ GCC_except_table2072
+ GCC_except_table2089
+ GCC_except_table2099
+ GCC_except_table2101
+ GCC_except_table2103
+ GCC_except_table2108
+ GCC_except_table2111
+ GCC_except_table2113
+ GCC_except_table2116
+ GCC_except_table2123
+ GCC_except_table2125
+ GCC_except_table2128
+ GCC_except_table2133
+ GCC_except_table2135
+ GCC_except_table2137
+ GCC_except_table2147
+ GCC_except_table2155
+ GCC_except_table2168
+ GCC_except_table2201
+ GCC_except_table2208
+ GCC_except_table2226
+ GCC_except_table2227
+ GCC_except_table2228
+ GCC_except_table2230
+ GCC_except_table2231
+ GCC_except_table2232
+ GCC_except_table2234
+ GCC_except_table2235
+ GCC_except_table2257
+ GCC_except_table2261
+ GCC_except_table2269
+ GCC_except_table2473
+ GCC_except_table2481
+ GCC_except_table2482
+ GCC_except_table2483
+ GCC_except_table2485
+ GCC_except_table2486
+ GCC_except_table2502
+ GCC_except_table2516
+ GCC_except_table2596
+ GCC_except_table2608
+ GCC_except_table2668
+ GCC_except_table2676
+ GCC_except_table2687
+ GCC_except_table2701
+ GCC_except_table2704
+ GCC_except_table2709
+ GCC_except_table2718
+ GCC_except_table2724
+ GCC_except_table2726
+ GCC_except_table2736
+ GCC_except_table2759
+ GCC_except_table2765
+ GCC_except_table2970
+ GCC_except_table2988
+ GCC_except_table3022
+ GCC_except_table3038
+ GCC_except_table3040
+ GCC_except_table3052
+ GCC_except_table3059
+ GCC_except_table3081
+ GCC_except_table3095
+ GCC_except_table3097
+ GCC_except_table3100
+ GCC_except_table3108
+ GCC_except_table3115
+ GCC_except_table3118
+ GCC_except_table3123
+ GCC_except_table3128
+ GCC_except_table3133
+ GCC_except_table3173
+ GCC_except_table3190
+ GCC_except_table3193
+ GCC_except_table3198
+ GCC_except_table3200
+ GCC_except_table3216
+ GCC_except_table3232
+ GCC_except_table3234
+ GCC_except_table3238
+ GCC_except_table3246
+ GCC_except_table3254
+ GCC_except_table3318
+ GCC_except_table3325
+ GCC_except_table3327
+ GCC_except_table3328
+ GCC_except_table3351
+ GCC_except_table3371
+ GCC_except_table3599
+ GCC_except_table3666
+ GCC_except_table3671
+ GCC_except_table3674
+ GCC_except_table3676
+ GCC_except_table3682
+ GCC_except_table3684
+ GCC_except_table3691
+ GCC_except_table3701
+ GCC_except_table3704
+ GCC_except_table3715
+ GCC_except_table3716
+ GCC_except_table3718
+ GCC_except_table3720
+ GCC_except_table3723
+ GCC_except_table3726
+ GCC_except_table3728
+ GCC_except_table3731
+ GCC_except_table3734
+ GCC_except_table3746
+ GCC_except_table3748
+ GCC_except_table3752
+ GCC_except_table3756
+ GCC_except_table3760
+ GCC_except_table3809
+ GCC_except_table3815
+ GCC_except_table3819
+ GCC_except_table3823
+ GCC_except_table3825
+ GCC_except_table3828
+ GCC_except_table3830
+ GCC_except_table3832
+ GCC_except_table3839
+ GCC_except_table3840
+ GCC_except_table3841
+ GCC_except_table3918
+ GCC_except_table3919
+ GCC_except_table3920
+ GCC_except_table3921
+ GCC_except_table3922
+ GCC_except_table3923
+ GCC_except_table3924
+ GCC_except_table3925
+ GCC_except_table3926
+ GCC_except_table3927
+ GCC_except_table3928
+ GCC_except_table3929
+ GCC_except_table3930
+ GCC_except_table3931
+ GCC_except_table3984
+ GCC_except_table4089
+ GCC_except_table4138
+ GCC_except_table4142
+ GCC_except_table4145
+ GCC_except_table4151
+ GCC_except_table4154
+ GCC_except_table4160
+ GCC_except_table4163
+ GCC_except_table4166
+ GCC_except_table4171
+ GCC_except_table4184
+ GCC_except_table4189
+ GCC_except_table4193
+ GCC_except_table4195
+ GCC_except_table4198
+ GCC_except_table4209
+ GCC_except_table4217
+ GCC_except_table4224
+ GCC_except_table4230
+ GCC_except_table4231
+ GCC_except_table4234
+ GCC_except_table4235
+ GCC_except_table4253
+ GCC_except_table4255
+ GCC_except_table4257
+ GCC_except_table4258
+ GCC_except_table4261
+ GCC_except_table4267
+ GCC_except_table4270
+ GCC_except_table4272
+ GCC_except_table4278
+ GCC_except_table4280
+ GCC_except_table4283
+ GCC_except_table4294
+ GCC_except_table4305
+ GCC_except_table4307
+ GCC_except_table4316
+ GCC_except_table4318
+ GCC_except_table4320
+ GCC_except_table4326
+ GCC_except_table4586
+ GCC_except_table4592
+ GCC_except_table4609
+ GCC_except_table4613
+ GCC_except_table4630
+ GCC_except_table4638
+ GCC_except_table4651
+ GCC_except_table4665
+ GCC_except_table4669
+ GCC_except_table4782
+ GCC_except_table5238
+ GCC_except_table5246
+ GCC_except_table5257
+ GCC_except_table5299
+ GCC_except_table5302
+ GCC_except_table5303
+ GCC_except_table5304
+ GCC_except_table5305
+ GCC_except_table5387
+ GCC_except_table5388
+ GCC_except_table5389
+ GCC_except_table5390
+ GCC_except_table5391
+ GCC_except_table5392
+ GCC_except_table5398
+ GCC_except_table5399
+ GCC_except_table5401
+ GCC_except_table5408
+ GCC_except_table5411
+ GCC_except_table5413
+ GCC_except_table5418
+ GCC_except_table5421
+ GCC_except_table5424
+ GCC_except_table5428
+ GCC_except_table5432
+ GCC_except_table545
+ GCC_except_table556
+ GCC_except_table572
+ GCC_except_table584
+ GCC_except_table5918
+ GCC_except_table5919
+ GCC_except_table5938
+ GCC_except_table5948
+ GCC_except_table5951
+ GCC_except_table5956
+ GCC_except_table5959
+ GCC_except_table6230
+ GCC_except_table6234
+ GCC_except_table6279
+ GCC_except_table6283
+ GCC_except_table6285
+ GCC_except_table6287
+ GCC_except_table630
+ GCC_except_table631
+ GCC_except_table633
+ GCC_except_table636
+ GCC_except_table639
+ GCC_except_table6489
+ GCC_except_table6495
+ GCC_except_table6499
+ GCC_except_table6500
+ GCC_except_table6501
+ GCC_except_table6502
+ GCC_except_table6508
+ GCC_except_table6524
+ GCC_except_table653
+ GCC_except_table6560
+ GCC_except_table6561
+ GCC_except_table6562
+ GCC_except_table657
+ GCC_except_table6582
+ GCC_except_table6594
+ GCC_except_table6597
+ GCC_except_table6602
+ GCC_except_table6604
+ GCC_except_table661
+ GCC_except_table6618
+ GCC_except_table671
+ GCC_except_table6853
+ GCC_except_table6871
+ GCC_except_table6874
+ GCC_except_table6875
+ GCC_except_table6877
+ GCC_except_table6878
+ GCC_except_table6880
+ GCC_except_table6910
+ GCC_except_table6936
+ GCC_except_table6940
+ GCC_except_table6949
+ GCC_except_table6953
+ GCC_except_table6957
+ GCC_except_table6961
+ GCC_except_table6969
+ GCC_except_table6971
+ GCC_except_table6975
+ GCC_except_table7039
+ GCC_except_table7040
+ GCC_except_table7041
+ GCC_except_table7042
+ GCC_except_table7043
+ GCC_except_table7044
+ GCC_except_table7045
+ GCC_except_table705
+ GCC_except_table7107
+ GCC_except_table7117
+ GCC_except_table7118
+ GCC_except_table7133
+ GCC_except_table7134
+ GCC_except_table7142
+ GCC_except_table7148
+ GCC_except_table715
+ GCC_except_table7161
+ GCC_except_table7164
+ GCC_except_table7165
+ GCC_except_table7170
+ GCC_except_table7173
+ GCC_except_table7180
+ GCC_except_table7183
+ GCC_except_table7197
+ GCC_except_table7204
+ GCC_except_table7210
+ GCC_except_table7219
+ GCC_except_table7221
+ GCC_except_table7227
+ GCC_except_table7228
+ GCC_except_table7235
+ GCC_except_table7259
+ GCC_except_table7260
+ GCC_except_table7265
+ GCC_except_table7269
+ GCC_except_table7270
+ GCC_except_table7273
+ GCC_except_table7279
+ GCC_except_table7283
+ GCC_except_table7287
+ GCC_except_table7289
+ GCC_except_table7291
+ GCC_except_table7295
+ GCC_except_table7446
+ GCC_except_table7506
+ GCC_except_table7513
+ GCC_except_table7526
+ GCC_except_table7527
+ GCC_except_table7543
+ GCC_except_table7548
+ GCC_except_table7549
+ GCC_except_table757
+ GCC_except_table759
+ GCC_except_table7598
+ GCC_except_table7599
+ GCC_except_table7601
+ GCC_except_table7604
+ GCC_except_table7631
+ GCC_except_table7632
+ GCC_except_table7637
+ GCC_except_table7657
+ GCC_except_table7675
+ GCC_except_table7676
+ GCC_except_table7677
+ GCC_except_table7686
+ GCC_except_table7691
+ GCC_except_table7692
+ GCC_except_table7693
+ GCC_except_table7708
+ GCC_except_table7711
+ GCC_except_table7718
+ GCC_except_table7725
+ GCC_except_table773
+ GCC_except_table7730
+ GCC_except_table7736
+ GCC_except_table7748
+ GCC_except_table7749
+ GCC_except_table7754
+ GCC_except_table7763
+ GCC_except_table7771
+ GCC_except_table7772
+ GCC_except_table7776
+ GCC_except_table7778
+ GCC_except_table7780
+ GCC_except_table7784
+ GCC_except_table7805
+ GCC_except_table7807
+ GCC_except_table7808
+ GCC_except_table7834
+ GCC_except_table798
+ GCC_except_table7999
+ GCC_except_table802
+ GCC_except_table8062
+ GCC_except_table8094
+ GCC_except_table8097
+ GCC_except_table813
+ GCC_except_table814
+ GCC_except_table819
+ GCC_except_table822
+ GCC_except_table825
+ GCC_except_table8264
+ GCC_except_table8302
+ GCC_except_table834
+ GCC_except_table840
+ GCC_except_table8428
+ GCC_except_table8430
+ GCC_except_table8432
+ GCC_except_table8434
+ GCC_except_table8436
+ GCC_except_table8438
+ GCC_except_table844
+ GCC_except_table8440
+ GCC_except_table8443
+ GCC_except_table8445
+ GCC_except_table8447
+ GCC_except_table8449
+ GCC_except_table845
+ GCC_except_table8451
+ GCC_except_table8454
+ GCC_except_table8456
+ GCC_except_table8458
+ GCC_except_table8467
+ GCC_except_table8473
+ GCC_except_table8478
+ GCC_except_table8481
+ GCC_except_table8486
+ GCC_except_table8491
+ GCC_except_table8494
+ GCC_except_table8497
+ GCC_except_table8527
+ GCC_except_table8546
+ GCC_except_table8547
+ GCC_except_table8548
+ GCC_except_table8550
+ GCC_except_table8551
+ GCC_except_table8553
+ GCC_except_table8554
+ GCC_except_table8555
+ GCC_except_table8557
+ GCC_except_table8558
+ GCC_except_table8560
+ GCC_except_table8564
+ GCC_except_table8565
+ GCC_except_table8569
+ GCC_except_table8620
+ GCC_except_table8627
+ GCC_except_table871
+ GCC_except_table8731
+ GCC_except_table8735
+ GCC_except_table8737
+ GCC_except_table8739
+ GCC_except_table8742
+ GCC_except_table8744
+ GCC_except_table8746
+ GCC_except_table8748
+ GCC_except_table8749
+ GCC_except_table8751
+ GCC_except_table8753
+ GCC_except_table8758
+ GCC_except_table8760
+ GCC_except_table8761
+ GCC_except_table878
+ GCC_except_table885
+ GCC_except_table886
+ GCC_except_table902
+ GCC_except_table924
+ GCC_except_table942
+ GCC_except_table964
+ GCC_except_table968
+ GCC_except_table982
+ GCC_except_table987
+ OBJC_IVAR_$_HAP2AccessoryServer._removedAccessoryECDSAKey
+ OBJC_IVAR_$_HAP2AccessoryServerSecureTransportPairVerify._ecdsaKeyPairVerifySession
+ OBJC_IVAR_$_HAP2AccessoryServerSecureTransportPairVerify._ecdsaKeySecuritySessionOpen
+ OBJC_IVAR_$_HAPAccessoryServer._removedAccessoryECDSAKey
+ OBJC_IVAR_$_HAPAccessoryServerIP._httpResponseHandler
+ OBJC_IVAR_$_HAPAccessoryServerIP._pairSetupSession
+ OBJC_IVAR_$_HAPAccessoryServerIP._pairVerifySession
+ OBJC_IVAR_$_HAPAccessoryServerIP._setupCodeCompletionHandler
+ OBJC_IVAR_$_HAPAdditionalWifiData._bssid
+ OBJC_IVAR_$_HAPAdditionalWifiData._channelNumber
+ OBJC_IVAR_$_HAPAdditionalWifiData._operatingClass
+ OBJC_IVAR_$_HAPECDSAPairingKey._data
+ OBJC_IVAR_$_HAPECDSAPairingKey._keyType
+ OBJC_IVAR_$_HAPPairing._ecdsaPairing
+ OBJC_IVAR_$_HAPPairing._ed25519PairingIdentity
+ OBJC_IVAR_$_HAPPairingECDSAKey._identifier
+ OBJC_IVAR_$_HAPPairingECDSAKey._permissions
+ OBJC_IVAR_$_HAPPairingECDSAKey._publicKey
+ OBJC_IVAR_$__HAPAccessoryServerBTLE200._ecdsaKeyPairVerifySession
+ OBJC_IVAR_$__HAPAccessoryServerBTLE200._ecdsaKeySecuritySessionOpen
+ _CFPreferencesCopyAppValue
+ _OBJC_CLASS_$_CoreHAPHKDF
+ _OBJC_CLASS_$_HAPAdditionalWifiData
+ _OBJC_CLASS_$_HAPECDSAConversion
+ _OBJC_CLASS_$_HAPECDSAKeyPairVerifySession
+ _OBJC_CLASS_$_HAPECDSAPairingKey
+ _OBJC_CLASS_$_HAPPairing
+ _OBJC_CLASS_$_HAPPairingECDSAKey
+ _OBJC_CLASS_$_HAPSpakePairSetupSession
+ _OBJC_CLASS_$_NSCondition
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_CLASS_$__TtC7CoreHAP24HAPSpakePairSetupSession
+ _OBJC_CLASS_$__TtC7CoreHAP28HAPECDSAKeyPairVerifySession
+ _OBJC_METACLASS_$_CoreHAPHKDF
+ _OBJC_METACLASS_$_HAPAdditionalWifiData
+ _OBJC_METACLASS_$_HAPECDSAConversion
+ _OBJC_METACLASS_$_HAPECDSAKeyPairVerifySession
+ _OBJC_METACLASS_$_HAPECDSAPairingKey
+ _OBJC_METACLASS_$_HAPPairing
+ _OBJC_METACLASS_$_HAPPairingECDSAKey
+ _OBJC_METACLASS_$_HAPSpakePairSetupSession
+ _OBJC_METACLASS_$__TtC7CoreHAP24HAPSpakePairSetupSession
+ _OBJC_METACLASS_$__TtC7CoreHAP28HAPECDSAKeyPairVerifySession
+ _PROTOCOLS_HAPECDSAKeyPairVerifySession
+ _PROTOCOLS_HAPSpakePairSetupSession
+ _PROTOCOLS__TtC7CoreHAP24HAPSpakePairSetupSession
+ _PROTOCOLS__TtC7CoreHAP28HAPECDSAKeyPairVerifySession
+ __101-[_HAPAccessoryServerBTLE200 enableRemovedAccessoryKey:ecdsaAccessoryKey:completionQueue:completion:]_block_invoke
+ __104-[HAPAccessoryServerHAP2Adapter enableRemovedAccessoryKey:ecdsaAccessoryKey:completionQueue:completion:]_block_invoke
+ __40-[HAP2CoAPIOThread _unregisterConsumer:]_block_invoke
+ __50-[HAPAccessoryServerIP _pairVerifyStartWithRetry:]_block_invoke
+ __53-[_HAPAccessoryServerBTLE200 _establishSecureSession]_block_invoke
+ __53-[_HAPAccessoryServerBTLE200 _establishSecureSession]_block_invoke_2
+ __53-[_HAPAccessoryServerBTLE200 _establishSecureSession]_block_invoke_3
+ __64-[_HAPAccessoryServerBTLE200 pairSetupSession:didStopWithError:]_block_invoke
+ __65-[HAPAccessoryServerIP _continuePairingAfterAuthPromptWithRetry:]_block_invoke
+ __68-[HAPAccessoryServerIP _queueAddPairingForPairing:queue:completion:]_block_invoke
+ __68-[HAPAccessoryServerIP _startAddPairingForPairing:queue:completion:]_block_invoke
+ __75-[_HAPAccessoryServerBTLE200 pairSetupSession:didReceiveSetupExchangeData:]_block_invoke
+ __78-[HAPAccessoryServerBrowserHAP2Adapter discoverAccessoryServerWithIdentifier:]_block_invoke
+ __78-[HAPAccessoryServerBrowserHAP2Adapter discoverAccessoryServerWithIdentifier:]_block_invoke_2
+ __78-[HAPAccessoryServerIP _ensurePairingSessionIsInitializedWithType:completion:]_block_invoke
+ __78-[HAPAccessoryServerIP _ensurePairingSessionIsInitializedWithType:completion:]_block_invoke_2
+ __78-[HAPAccessoryServerIP _ensurePairingSessionIsInitializedWithType:completion:]_block_invoke_3
+ __82-[HAP2AccessoryServerSecureTransportPairVerify pairSetupSession:didStopWithError:]_block_invoke
+ __91-[HAP2AccessoryServerSecureTransportPairVerify ecdsaLongTermPublicKeyOfPeerWithIdentifier:]_block_invoke
+ __93-[HAP2AccessoryServer(Unpaired) removeUnpairedAccessoryPairing:ecdsaAccessoryKey:completion:]_block_invoke
+ __95-[HAPAccessoryServer removePairingsWithRemovedAccessoryKey:ecdsaAccessoryKey:queue:completion:]_block_invoke
+ __95-[HAPAccessoryServer removePairingsWithRemovedAccessoryKey:ecdsaAccessoryKey:queue:completion:]_block_invoke_2
+ __97-[HAP2AccessoryServer(Unpaired) updateRemovedAccessoriesWithReason:ecdsaAccessoryKey:completion:]_block_invoke
+ __Block_copy
+ __Block_release
+ __CLASS_METHODS_CoreHAPHKDF
+ __CLASS_METHODS_HAPECDSAKeyPairVerifySession
+ __CLASS_METHODS__TtC7CoreHAP28HAPECDSAKeyPairVerifySession
+ __DATA_CoreHAPHKDF
+ __DATA_HAPECDSAKeyPairVerifySession
+ __DATA_HAPSpakePairSetupSession
+ __DATA__TtC7CoreHAP24HAPSpakePairSetupSession
+ __DATA__TtC7CoreHAP28HAPECDSAKeyPairVerifySession
+ __INSTANCE_METHODS_CoreHAPHKDF
+ __INSTANCE_METHODS_HAPECDSAKeyPairVerifySession
+ __INSTANCE_METHODS_HAPSpakePairSetupSession
+ __INSTANCE_METHODS__TtC7CoreHAP24HAPSpakePairSetupSession
+ __INSTANCE_METHODS__TtC7CoreHAP28HAPECDSAKeyPairVerifySession
+ __IVARS_HAPECDSAKeyPairVerifySession
+ __IVARS_HAPSpakePairSetupSession
+ __IVARS__TtC7CoreHAP24HAPSpakePairSetupSession
+ __IVARS__TtC7CoreHAP28HAPECDSAKeyPairVerifySession
+ __METACLASS_DATA_CoreHAPHKDF
+ __METACLASS_DATA_HAPECDSAKeyPairVerifySession
+ __METACLASS_DATA_HAPSpakePairSetupSession
+ __METACLASS_DATA__TtC7CoreHAP24HAPSpakePairSetupSession
+ __METACLASS_DATA__TtC7CoreHAP28HAPECDSAKeyPairVerifySession
+ __OBJC_$_CLASS_METHODS_HAPECDSAConversion
+ __OBJC_$_CLASS_METHODS_HAPECDSAPairingKey
+ __OBJC_$_CLASS_PROP_LIST_HAPECDSAPairingKey
+ __OBJC_$_INSTANCE_METHODS_HAPAdditionalWifiData
+ __OBJC_$_INSTANCE_METHODS_HAPECDSAPairingKey
+ __OBJC_$_INSTANCE_METHODS_HAPPairing
+ __OBJC_$_INSTANCE_METHODS_HAPPairingECDSAKey
+ __OBJC_$_INSTANCE_VARIABLES_HAPAdditionalWifiData
+ __OBJC_$_INSTANCE_VARIABLES_HAPECDSAPairingKey
+ __OBJC_$_INSTANCE_VARIABLES_HAPPairing
+ __OBJC_$_INSTANCE_VARIABLES_HAPPairingECDSAKey
+ __OBJC_$_PROP_LIST_HAPAdditionalWifiData
+ __OBJC_$_PROP_LIST_HAPECDSAPairingKey
+ __OBJC_$_PROP_LIST_HAPPairing
+ __OBJC_$_PROP_LIST_HAPPairingECDSAKey
+ __OBJC_$_PROP_LIST_HMFFastEncodable
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HAPECDSAKeyPairVerifySessionDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HAPPairVerifySession
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HAPSpakePairSetupSessionDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HAPSpakePairSetupSessionDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HMFFastEncodable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HAPECDSAKeyPairVerifySessionDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HAPPairVerifySession
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HAPSpakePairSetupSessionDelegate
+ __OBJC_$_PROTOCOL_REFS_HAPECDSAKeyPairVerifySessionDelegate
+ __OBJC_$_PROTOCOL_REFS_HAPPairVerifySession
+ __OBJC_$_PROTOCOL_REFS_HAPSpakePairSetupSessionDelegate
+ __OBJC_CLASS_PROTOCOLS_$_HAPAdditionalWifiData
+ __OBJC_CLASS_PROTOCOLS_$_HAPECDSAPairingKey
+ __OBJC_CLASS_RO_$_HAPAdditionalWifiData
+ __OBJC_CLASS_RO_$_HAPECDSAConversion
+ __OBJC_CLASS_RO_$_HAPECDSAPairingKey
+ __OBJC_CLASS_RO_$_HAPPairing
+ __OBJC_CLASS_RO_$_HAPPairingECDSAKey
+ __OBJC_LABEL_PROTOCOL_$_HAPECDSAKeyPairVerifySessionDelegate
+ __OBJC_LABEL_PROTOCOL_$_HAPPairVerifySession
+ __OBJC_LABEL_PROTOCOL_$_HAPSpakePairSetupSessionDelegate
+ __OBJC_METACLASS_RO_$_HAPAdditionalWifiData
+ __OBJC_METACLASS_RO_$_HAPECDSAConversion
+ __OBJC_METACLASS_RO_$_HAPECDSAPairingKey
+ __OBJC_METACLASS_RO_$_HAPPairing
+ __OBJC_METACLASS_RO_$_HAPPairingECDSAKey
+ __OBJC_PROTOCOL_$_HAPECDSAKeyPairVerifySessionDelegate
+ __OBJC_PROTOCOL_$_HAPPairVerifySession
+ __OBJC_PROTOCOL_$_HAPSpakePairSetupSessionDelegate
+ __PROPERTIES_HAPECDSAKeyPairVerifySession
+ __PROPERTIES_HAPSpakePairSetupSession
+ __PROPERTIES__TtC7CoreHAP28HAPECDSAKeyPairVerifySession
+ __PROTOCOLS_HAPECDSAKeyPairVerifySession
+ __PROTOCOLS_HAPSpakePairSetupSession
+ __PROTOCOLS__TtC7CoreHAP24HAPSpakePairSetupSession
+ __PROTOCOLS__TtC7CoreHAP28HAPECDSAKeyPairVerifySession
+ ___101-[_HAPAccessoryServerBTLE200 enableRemovedAccessoryKey:ecdsaAccessoryKey:completionQueue:completion:]_block_invoke
+ ___104-[HAPAccessoryServerHAP2Adapter enableRemovedAccessoryKey:ecdsaAccessoryKey:completionQueue:completion:]_block_invoke
+ ___105-[HAP2AccessoryServerSecureTransportPairVerify localPairingIdentityOfECDSAKeyPairSetupSession:withError:]_block_invoke
+ ___105-[HAP2AccessoryServerSecureTransportPairVerify localPairingIdentityOfECDSAKeyPairSetupSession:withError:]_block_invoke_2
+ ___107-[HAPAccessoryServerIP pairSetupSession:didReceiveWiFiNetworkConfigurationTLVRequestWithCompletionHandler:]_block_invoke
+ ___107-[HAPAccessoryServerIP pairSetupSession:didReceiveWiFiNetworkConfigurationTLVRequestWithCompletionHandler:]_block_invoke_2
+ ___107-[HAPAccessoryServerIP pairSetupSession:didReceiveWiFiNetworkConfigurationTLVRequestWithCompletionHandler:]_block_invoke_3
+ ___109-[HAP2AccessoryServerController secureTransport:needsECDSALongTermPublicKeyForPeerWithIdentifier:completion:]_block_invoke
+ ___109-[HAPAccessoryServerIP pairSetupSession:didReceiveThreadNetworkConfigurationTLVRequestWithCompletionHandler:]_block_invoke
+ ___109-[HAPAccessoryServerIP pairSetupSession:didReceiveThreadNetworkConfigurationTLVRequestWithCompletionHandler:]_block_invoke_2
+ ___109-[HAPAccessoryServerIP pairSetupSession:didReceiveThreadNetworkConfigurationTLVRequestWithCompletionHandler:]_block_invoke_3
+ ___110-[HAP2AccessoryServer(Unpaired) pairingDriver:didSaveRemoteECDSAPairingKey:forAccessoryIdentifier:completion:]_block_invoke
+ ___113-[HAP2AccessoryServerController secureTransport:needsLocalPairingIdentityForECDSAKeyPairSetupSession:completion:]_block_invoke
+ ___113-[_HAPAccessoryServerBTLE200 pairSetupSession:didReceiveWiFiNetworkConfigurationTLVRequestWithCompletionHandler:]_block_invoke
+ ___113-[_HAPAccessoryServerBTLE200 pairSetupSession:didReceiveWiFiNetworkConfigurationTLVRequestWithCompletionHandler:]_block_invoke_2
+ ___115-[_HAPAccessoryServerBTLE200 pairSetupSession:didReceiveThreadNetworkConfigurationTLVRequestWithCompletionHandler:]_block_invoke
+ ___115-[_HAPAccessoryServerBTLE200 pairSetupSession:didReceiveThreadNetworkConfigurationTLVRequestWithCompletionHandler:]_block_invoke_2
+ ___118-[HAP2AccessoryServerPairingDriverPairSetupWorkItem pairSetupSession:didPairWithPeerIdentifier:ecdsaPairingKey:error:]_block_invoke
+ ___40-[HAP2CoAPIOThread _unregisterConsumer:]_block_invoke_2
+ ___53-[_HAPAccessoryServerBTLE200 _establishSecureSession]_block_invoke
+ ___53-[_HAPAccessoryServerBTLE200 _establishSecureSession]_block_invoke_2
+ ___53-[_HAPAccessoryServerBTLE200 _establishSecureSession]_block_invoke_3
+ ___58-[HAPAccessoryServerIP pairSetupSession:didStopWithError:]_block_invoke
+ ___63-[HAPAccessoryServerIP pairSetupSession:didReceiveProductData:]_block_invoke
+ ___64-[HAPSystemKeychainStore ecdsaPairingKeyExistsForAccessoryName:]_block_invoke
+ ___65-[_HAPAccessoryServerBTLE200 _obtainPairVerifyTLKWithCompletion:]_block_invoke
+ ___65-[_HAPAccessoryServerBTLE200 _obtainPairVerifyTLKWithCompletion:]_block_invoke_2
+ ___65-[_HAPAccessoryServerBTLE200 _obtainPairVerifyTLKWithCompletion:]_block_invoke_3
+ ___67-[HAPAccessoryServerIP pairSetupSessionDidReceiveInvalidSetupCode:]_block_invoke
+ ___68-[HAPAccessoryServerIP _queueAddPairingForPairing:queue:completion:]_block_invoke
+ ___68-[HAPAccessoryServerIP _startAddPairingForPairing:queue:completion:]_block_invoke
+ ___69-[HAPAccessoryServerIP pairSetupSession:didReceiveSetupExchangeData:]_block_invoke
+ ___69-[HAPSystemKeychainStore saveECDSAPairingKey:forAccessoryName:error:]_block_invoke
+ ___73-[HAP2AccessoryServerPairingDriverPairSetupWorkItem runForPairingDriver:]_block_invoke
+ ___73-[HAP2AccessoryServerPairingDriverPairSetupWorkItem runForPairingDriver:]_block_invoke_2
+ ___74-[HAP2AccessoryServerSecureTransportPairVerify _attemptECDSAKeyPairVerify]_block_invoke
+ ___74-[HAP2AccessoryServerSecureTransportPairVerify _attemptECDSAKeyPairVerify]_block_invoke_2
+ ___74-[HAP2AccessoryServerSecureTransportPairVerify _attemptECDSAKeyPairVerify]_block_invoke_3
+ ___75-[HAP2AccessoryServerSecureTransportPairVerify _handleECDSASessionFailure:]_block_invoke
+ ___75-[HAP2AccessoryServerSecureTransportPairVerify _handleECDSASessionFailure:]_block_invoke_2
+ ___75-[HAP2AccessoryServerSecureTransportPairVerify _handleECDSASessionFailure:]_block_invoke_3
+ ___75-[HAP2AccessoryServerSecureTransportPairVerify _handleECDSASessionFailure:]_block_invoke_4
+ ___75-[_HAPAccessoryServerBTLE100 addPairing:completionQueue:completionHandler:]_block_invoke_2
+ ___78-[HAPAccessoryServerIP _ensurePairingSessionIsInitializedWithType:completion:]_block_invoke
+ ___78-[HAPAccessoryServerIP _ensurePairingSessionIsInitializedWithType:completion:]_block_invoke_2
+ ___78-[HAPAccessoryServerIP _ensurePairingSessionIsInitializedWithType:completion:]_block_invoke_3
+ ___78-[HAPSecuritySession handleSetupExchangeCompleteWithForeignPairVerifySession:]_block_invoke
+ ___79-[HAPSecuritySession _handleSetupExchangeCompleteWithForeignPairVerifySession:]_block_invoke
+ ___80-[HAP2AccessoryServerSecureTransportPairVerify _createECDSAKeyPairVerifySession]_block_invoke
+ ___80-[HAP2AccessoryServerSecureTransportPairVerify _createECDSAKeyPairVerifySession]_block_invoke_2
+ ___80-[HAP2AccessoryServerSecureTransportPairVerify _createECDSAKeyPairVerifySession]_block_invoke_3
+ ___81-[HAPAccessoryServerIP _establishSecureSessionAndRemovePairing:queue:completion:]_block_invoke_3
+ ___82-[HAP2AccessoryServerSecureTransportPairVerify pairSetupSession:didStopWithError:]_block_invoke
+ ___82-[HAP2AccessoryServerSecureTransportPairVerify pairSetupSession:didStopWithError:]_block_invoke_2
+ ___82-[HAP2AccessoryServerSecureTransportPairVerify pairSetupSession:didStopWithError:]_block_invoke_3
+ ___82-[HAP2AccessoryServerSecureTransportPairVerify pairSetupSession:didStopWithError:]_block_invoke_4
+ ___82-[HAPAccessoryServerIP pairSetupSession:didReceiveBackoffRequestWithTimeInterval:]_block_invoke
+ ___84-[HAP2AccessoryServer(Unpaired) getPairingsWithRemovedAccessoryECDSAKey:completion:]_block_invoke
+ ___84-[HAP2AccessoryServer(Unpaired) getPairingsWithRemovedAccessoryECDSAKey:completion:]_block_invoke_2
+ ___84-[HAP2AccessoryServerController secureTransport:checkECDSACapabilityWithCompletion:]_block_invoke
+ ___84-[HAPAccessoryServerHAP2Adapter accessoryServer:requestPairVerifyTLKWithCompletion:]_block_invoke
+ ___89-[HAPAccessoryServerIP pairSetupSession:didReceiveSetupCodeRequestWithCompletionHandler:]_block_invoke
+ ___90-[HAPSystemKeychainStore readECDSAPairingKeyForAccessoryName:registeredWithHomeKit:error:]_block_invoke
+ ___91-[HAP2AccessoryServerSecureTransportPairVerify ecdsaLongTermPublicKeyOfPeerWithIdentifier:]_block_invoke
+ ___91-[HAP2AccessoryServerSecureTransportPairVerify ecdsaLongTermPublicKeyOfPeerWithIdentifier:]_block_invoke_2
+ ___93-[HAP2AccessoryServer(Unpaired) removeUnpairedAccessoryPairing:ecdsaAccessoryKey:completion:]_block_invoke
+ ___93-[HAP2AccessoryServer(Unpaired) removeUnpairedAccessoryPairing:ecdsaAccessoryKey:completion:]_block_invoke_2
+ ___93-[HAP2AccessoryServerSecureTransportPairVerify pairSetupSession:didReceiveSetupExchangeData:]_block_invoke
+ ___93-[HAPAccessoryServer enableRemovedAccessoryKey:ecdsaAccessoryKey:completionQueue:completion:]_block_invoke
+ ___95-[HAPAccessoryServer removePairingsWithRemovedAccessoryKey:ecdsaAccessoryKey:queue:completion:]_block_invoke
+ ___95-[HAPAccessoryServer removePairingsWithRemovedAccessoryKey:ecdsaAccessoryKey:queue:completion:]_block_invoke_2
+ ___95-[HAPAccessoryServer removePairingsWithRemovedAccessoryKey:ecdsaAccessoryKey:queue:completion:]_block_invoke_3
+ ___97-[HAP2AccessoryServer(Unpaired) updateRemovedAccessoriesWithReason:ecdsaAccessoryKey:completion:]_block_invoke
+ ___97-[HAP2AccessoryServer(Unpaired) updateRemovedAccessoriesWithReason:ecdsaAccessoryKey:completion:]_block_invoke_2
+ ___97-[HAP2AccessoryServer(Unpaired) updateRemovedAccessoriesWithReason:ecdsaAccessoryKey:completion:]_block_invoke_3
+ ___block_descriptor_40_e8_32bs_e28_v24?0"NSData"8"NSError"16l
+ ___block_descriptor_40_e8_32bs_e67_v40?0"NSData"8"NSString"16"HAPAdditionalWifiData"24"NSError"32l
+ ___block_descriptor_40_e8_32s_e43_B32?0"HAP2CoAPIOThreadQueueEntry"8Q16^B24l
+ ___block_descriptor_40_e8_32s_e8_v12?0i8l
+ ___block_descriptor_48_e8_32s40bs_e40_v24?0"HAPECDSAPairingKey"8"NSError"16l
+ ___block_descriptor_48_e8_32s40bs_e40_v24?0"HAPPairingIdentity"8"NSError"16l
+ ___block_descriptor_48_e8_32s40bs_e8_v12?0i8l
+ ___block_descriptor_48_e8_32s40w_e20_v20?0B8"NSError"12l
+ ___block_descriptor_48_e8_32s40w_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_49_e8_32s40w_e5_v8?0l
+ ___block_descriptor_56_e8_32s40r48r_e28_v24?0"NSData"8"NSError"16l
+ ___block_descriptor_56_e8_32s40s48bs_e40_v24?0"HAPECDSAPairingKey"8"NSError"16l
+ ___block_descriptor_56_e8_32s40s48s_e68_v32?0"HAPSecuritySessionDelegateAdditionalDerivedKeyTuple"8Q16^B24l
+ ___block_descriptor_56_e8_32s40w_e28_v24?0"NSData"8"NSError"16l
+ ___block_descriptor_60_e8_32s40bs_e28_v24?0"NSData"8"NSError"16l
+ ___block_descriptor_60_e8_32s40bs_e5_v8?0l
+ ___block_descriptor_68_e8_32s40s48bs_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e17_v16?0"NSError"8l
+ ___swift__destructor
+ ___swift_allocate_value_buffer
+ ___swift_closure_destructor
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_destroy_boxed_opaque_existential_0Tm
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ ___swift_memcpy16_8
+ ___swift_memcpy1_1
+ ___swift_memcpy8_8
+ ___swift_noop_void_return
+ ___swift_project_boxed_opaque_existential_1
+ ___swift_project_value_buffer
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_CoreHAP
+ __swift__destructor
+ __swift_closure_destructor
+ __swift_closure_destructor.181Tm
+ __swift_stdlib_bridgeErrorToNSError
+ __swift_stdlib_malloc_size
+ __swift_stdlib_reportUnimplementedInitializer
+ _associated conformance 7CoreHAP20PairSetupCipherSuite33_FFB3B66732484B0775DD4AE3FA14FD0DLLOSHAASQ
+ _associated conformance 7CoreHAP24HAPSpakePairSetupSessionC0dE5StateOSHAASQ
+ _associated conformance 7CoreHAP24HAPSpakePairSetupSessionC21MFiTokenPrefetchState33_FFB3B66732484B0775DD4AE3FA14FD0DLLOSHAASQ
+ _associated conformance 7CoreHAP24HAPSpakePairSetupSessionC7KDFMode33_FFB3B66732484B0775DD4AE3FA14FD0DLLOSHAASQ
+ _associated conformance So15HAPFeatureFlagsVs10SetAlgebraSCSQ
+ _associated conformance So15HAPFeatureFlagsVs10SetAlgebraSCs25ExpressibleByArrayLiteral
+ _associated conformance So15HAPFeatureFlagsVs9OptionSetSCSY
+ _associated conformance So15HAPFeatureFlagsVs9OptionSetSCs0D7Algebra
+ _block_copy_helper
+ _block_descriptor
+ _block_destroy_helper
+ _ccaes_cbc_encrypt_mode
+ _ccaes_ccm_decrypt_mode
+ _ccaes_ccm_encrypt_mode
+ _ccccm_one_shot_decrypt
+ _ccccm_one_shot_encrypt
+ _ccchacha20poly1305_decrypt_oneshot
+ _ccchacha20poly1305_encrypt_oneshot
+ _ccchacha20poly1305_info
+ _ccec_cp_256
+ _ccec_generate_key_deterministic
+ _ccec_x963_export
+ _cced25519_sign
+ _cced25519_verify
+ _ccnistkdf_ctr_cmac
+ _ccrng
+ _ccsha512_di
+ _cczp_bitlen
+ _flat unique So19HAPPairSetupSession_p
+ _flat unique So27HAPPairSetupSessionDelegate_p
+ _flat unique So32HAPSpakePairSetupSessionDelegate_p
+ _flat unique So36HAPECDSAKeyPairVerifySessionDelegate_p
+ _get_enum_tag_for_layout_string 10Foundation4DataV15_RepresentationO
+ _get_enum_tag_for_layout_string 7CoreHAP24HAPSpakePairSetupSessionC20CredentialFetchState33_FFB3B66732484B0775DD4AE3FA14FD0DLLO
+ _kCFPreferencesCurrentApplication
+ _malloc_size
+ _memmove
+ _memset
+ _objc_allocWithZone
+ _objc_msgSend$_attemptECDSAKeyPairVerify
+ _objc_msgSend$_createECDSAKeyPairVerifySession
+ _objc_msgSend$_createSecuritySessionFromECDSASession
+ _objc_msgSend$_ensurePairingSessionIsInitializedWithType:completion:
+ _objc_msgSend$_getControllerPublicKey:secretKey:keyPair:username:allowCreation:forECDSAKeyAccessory:error:
+ _objc_msgSend$_getECDSAPairingKey:registeredWithHomeKit:forAccessoryName:
+ _objc_msgSend$_handleECDSASessionFailure:
+ _objc_msgSend$_handleSetupExchangeCompleteWithForeignPairVerifySession:
+ _objc_msgSend$_queueAddPairingForPairing:queue:completion:
+ _objc_msgSend$_saveECDSAPairingKey:forAccessoryName:
+ _objc_msgSend$_startAddPairingForPairing:queue:completion:
+ _objc_msgSend$accessoryServer:didRequestHomeThreadNetworkCredentialsWithCompletion:
+ _objc_msgSend$accessoryServer:didRequestHomeWiFiNetworkCredentialsWithCompletion:
+ _objc_msgSend$accessoryServer:requestPairVerifyTLKWithCompletion:
+ _objc_msgSend$accessoryServer:requestPairVerifyTLKsWithCompletion:
+ _objc_msgSend$associateAccessoryWithControllerKey:usingAccessoryECDSAPairingKey:
+ _objc_msgSend$associateAccessoryWithControllerKeyUsingAccessoryECDSAPairingKey:
+ _objc_msgSend$associateECDSAKeyAccessoryControllerIdentifier:error:
+ _objc_msgSend$channelNumber
+ _objc_msgSend$createAddPairingRequestForPairing:error:
+ _objc_msgSend$deriveSessionKeyWithSalt:info:error:
+ _objc_msgSend$ecdsaKeyPairVerifySession
+ _objc_msgSend$ecdsaLongTermPublicKeyOfPeerWithIdentifier:
+ _objc_msgSend$ecdsaPairing
+ _objc_msgSend$ecdsaPrivateKeyFrom352bitRandomData:error:
+ _objc_msgSend$ecdsaPrivateKeyFromEd25519PrivateKey:error:
+ _objc_msgSend$ecdsaPublicKey
+ _objc_msgSend$ecdsaPublicKeyFromEd25519PrivateKey:error:
+ _objc_msgSend$ed25519PairingIdentity
+ _objc_msgSend$enableRemovedAccessoryKey:ecdsaAccessoryKey:completionQueue:completion:
+ _objc_msgSend$establishRelationshipBetweenControllerKeyAndAccessoryECDSAPairingKey:accessoryPairingIdentifier:controllerKeyIdentifier:error:
+ _objc_msgSend$fetchControllerKeyForECDSAKeyAccessory:completion:
+ _objc_msgSend$fetchECDSAKeyForAccessoryName:completion:
+ _objc_msgSend$fetchPairVerifyTLKsForAccessoryName:completion:
+ _objc_msgSend$getAssociatedControllerKeyForECDSAKeyAccessory:
+ _objc_msgSend$getHH2ControllerKeyWithIdentifier:
+ _objc_msgSend$getOrCreateHH2ControllerKey:secretKey:keyPair:username:
+ _objc_msgSend$getPairingsWithRemovedAccessoryECDSAKey:completion:
+ _objc_msgSend$handleSetupExchangeCompleteWithForeignPairVerifySession:
+ _objc_msgSend$hmf_fastEncodedSize
+ _objc_msgSend$hmf_fastEncodedSizeForObject:
+ _objc_msgSend$httpResponseHandler
+ _objc_msgSend$indexesOfObjectsPassingTest:
+ _objc_msgSend$initWithDelegate:pairVerifyTLKs:
+ _objc_msgSend$initWithECDSAPairing:
+ _objc_msgSend$initWithEd25519PairingIdentity:
+ _objc_msgSend$initWithIdentifier:publicKey:permissions:
+ _objc_msgSend$initWithOperatingClass:channelNumber:bssid:
+ _objc_msgSend$initWithPairingKeyType:data:
+ _objc_msgSend$initWithRole:pairSetupType:featureFlags:delegate:pairVerifyTLK:
+ _objc_msgSend$keyType
+ _objc_msgSend$localPairingIdentityOfECDSAKeyPairSetupSession:withError:
+ _objc_msgSend$objectsAtIndexes:
+ _objc_msgSend$openTransportWithResume:completion:
+ _objc_msgSend$operatingClass
+ _objc_msgSend$pairSetupSession:confirmMFiTokenWithUUID:newToken:
+ _objc_msgSend$pairSetupSession:didPairWithPeerIdentifier:ecdsaPairingKey:error:
+ _objc_msgSend$pairSetupSession:didReceiveAdditionalPairingRequestWithPairingIdentifier:ecdsaPublicKey:error:
+ _objc_msgSend$pairSetupSession:didReceiveThreadNetworkConfigurationTLVRequestWithCompletionHandler:
+ _objc_msgSend$pairSetupSession:didReceiveWiFiNetworkConfigurationTLVRequestWithCompletionHandler:
+ _objc_msgSend$pairSetupSession:promptUncertifiedForMFiRollError:completionHandler:
+ _objc_msgSend$pairSetupSession:validateAndRollMFiTokenWithUUID:token:completionHandler:
+ _objc_msgSend$pairSetupSessionDidEstablishSessionPendingCommit:
+ _objc_msgSend$pairVerifySession
+ _objc_msgSend$pairingDriver:didSaveRemoteECDSAPairingKey:forAccessoryIdentifier:completion:
+ _objc_msgSend$pairingDriver:requestPairVerifyTLKWithCompletion:
+ _objc_msgSend$readControllerPairingKeyForECDSAKeyAccessory:error:
+ _objc_msgSend$readECDSAPairingKeyForAccessoryName:registeredWithHomeKit:error:
+ _objc_msgSend$removePairingsWithRemovedAccessoryKey:ecdsaAccessoryKey:queue:completion:
+ _objc_msgSend$removeUnpairedAccessoryPairing:ecdsaAccessoryKey:completion:
+ _objc_msgSend$removedAccessoryECDSAKey
+ _objc_msgSend$saveECDSAKey:forAccessoryName:completion:
+ _objc_msgSend$saveECDSAPairingKey:forAccessoryName:error:
+ _objc_msgSend$secureTransport:checkECDSACapabilityWithCompletion:
+ _objc_msgSend$secureTransport:needsECDSALongTermPublicKeyForPeerWithIdentifier:completion:
+ _objc_msgSend$secureTransport:needsLocalPairingIdentityForECDSAKeyPairSetupSession:completion:
+ _objc_msgSend$secureTransport:needsPairVerifyTLKsWithCompletion:
+ _objc_msgSend$sessionInternal
+ _objc_msgSend$sessionReadKeyWithError:
+ _objc_msgSend$sessionWriteKeyWithError:
+ _objc_msgSend$setEcdsaKeyPairVerifySession:
+ _objc_msgSend$setEcdsaKeySecuritySessionOpen:
+ _objc_msgSend$setHttpResponseHandler:
+ _objc_msgSend$setPairVerifySession:
+ _objc_msgSend$setRemovedAccessoryECDSAKey:
+ _objc_msgSend$updateKeychainItem:createIfNeeded:error:
+ _objc_msgSend$updateRemovedAccessoriesWithReason:ecdsaAccessoryKey:completion:
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain
+ _swift_bridgeObjectRetain_n
+ _swift_coroFrameAlloc
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_deallocObject
+ _swift_deletedMethodError
+ _swift_dynamicCast
+ _swift_dynamicCastClass
+ _swift_endAccess
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getErrorValue
+ _swift_getForeignTypeMetadata
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getSingletonMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_initStackObject
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_isaMask
+ _swift_lookUpClassMethod
+ _swift_once
+ _swift_release
+ _swift_release_n
+ _swift_retain
+ _swift_retain_n
+ _swift_setDeallocating
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRelease_n
+ _swift_unknownObjectRetain
+ _swift_unknownObjectWeakAssign
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
+ _swift_updateClassMetadata2
+ _swift_willThrow
+ _symbolic $sSY
+ _symbolic $ss10SetAlgebraP
+ _symbolic $ss25ExpressibleByArrayLiteralP
+ _symbolic $ss9OptionSetP
+ _symbolic SS
+ _symbolic SSIego_
+ _symbolic SSSg
+ _symbolic SS_ypt
+ _symbolic Say_____G 8Dispatch0A13WorkItemFlagsV
+ _symbolic Say_____G So17OS_dispatch_queueC8DispatchE10AttributesV
+ _symbolic Say_____GSg 10Foundation4DataV
+ _symbolic Sb
+ _symbolic SiIegd_
+ _symbolic SiIegr_
+ _symbolic So11NSConditionC
+ _symbolic So17OS_dispatch_queueC
+ _symbolic So21HAPAdditionalWifiDataCSg
+ _symbolic So28HAPECDSAKeyPairVerifySessionCSgXw
+ _symbolic So6NSLockC
+ _symbolic So8NSObjectC
+ _symbolic So8NSObjectCSg
+ _symbolic Su
+ _symbolic _____ 10Foundation4DataV
+ _symbolic _____ 7CoreHAP17HAPPairSetupNonceV
+ _symbolic _____ 7CoreHAP20PairSetupCipherSuite33_FFB3B66732484B0775DD4AE3FA14FD0DLLO
+ _symbolic _____ 7CoreHAP24HAPSpakePairSetupSessionC
+ _symbolic _____ 7CoreHAP24HAPSpakePairSetupSessionC0dE5StateO
+ _symbolic _____ 7CoreHAP24HAPSpakePairSetupSessionC20CredentialFetchState33_FFB3B66732484B0775DD4AE3FA14FD0DLLO
+ _symbolic _____ 7CoreHAP24HAPSpakePairSetupSessionC21MFiTokenPrefetchState33_FFB3B66732484B0775DD4AE3FA14FD0DLLO
+ _symbolic _____ 7CoreHAP24HAPSpakePairSetupSessionC7KDFMode33_FFB3B66732484B0775DD4AE3FA14FD0DLLO
+ _symbolic _____ 7CoreHAP28HAPECDSAKeyPairVerifySessionC
+ _symbolic _____ So15HAPFeatureFlagsV
+ _symbolic _____ So23HAPPairSetupSessionRoleV
+ _symbolic _____ So31HAPAccessoryServerPairSetupTypeV
+ _symbolic _____ So33HAPECDSAKeyPairVerifySessionStateV
+ _symbolic _____ s5Int32V
+ _symbolic _____ s5UInt8V
+ _symbolic _____ s6UInt32V
+ _symbolic _____ s6UInt64V
+ _symbolic _____Iegd_ s5Int32V
+ _symbolic _____Iegr_ s5Int32V
+ _symbolic _____Sg 10Foundation4DataV
+ _symbolic _____Sg 16CryptoKitPrivate12SymmetricKeyV
+ _symbolic _____Sg 16CryptoKitPrivate6SPAKE2O6ProverV
+ _symbolic _____Sg 7CoreHAP20PairSetupCipherSuite33_FFB3B66732484B0775DD4AE3FA14FD0DLLO
+ _symbolic _____Sg 9CryptoKit03ChaC4PolyO5NonceV
+ _symbolic _____Sg 9CryptoKit10Curve25519O12KeyAgreementO06PublicD0V
+ _symbolic _____Sg 9CryptoKit10Curve25519O12KeyAgreementO07PrivateD0V
+ _symbolic _____Sg 9CryptoKit12SharedSecretV
+ _symbolic _____Sg 9CryptoKit4P256O7SigningO10PrivateKeyV
+ _symbolic _____SgXw 7CoreHAP24HAPSpakePairSetupSessionC
+ _symbolic _____SgXwz_Xx 7CoreHAP24HAPSpakePairSetupSessionC
+ _symbolic _____Sg_ABt 16CryptoKitPrivate12SymmetricKeyV
+ _symbolic ___________pSgXw So36HAPECDSAKeyPairVerifySessionDelegateP So012HAPPairSetupdE0P
+ _symbolic ______p 10Foundation15ContiguousBytesP
+ _symbolic ______p s5ErrorP
+ _symbolic ______pSg s5ErrorP
+ _symbolic ______pSg5error_t s5ErrorP
+ _symbolic ______pSgXw So19HAPPairSetupSessionP
+ _symbolic ______pSgXw So32HAPSpakePairSetupSessionDelegateP
+ _symbolic _____ySS_yptG s23_ContiguousArrayStorageC
+ _symbolic _____ySSypG s18_DictionaryStorageC
+ _symbolic _____ySiG s11_SetStorageC
+ _symbolic _____ySiG s23_ContiguousArrayStorageC
+ _symbolic _____ySnySiGG s23_ContiguousArrayStorageC
+ _symbolic _____y_____AB_G s12Zip2SequenceV8IteratorV 10Foundation4DataV
+ _symbolic _____y_____G 9CryptoKit24HashedAuthenticationCodeV AA6SHA256V
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic _____yySpy_____Gz_SpySo8NSObjectCSgGSgzSpyypGSgztcG s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic ytSg
+ _type_layout_string 7CoreHAP17HAPPairSetupNonceV
+ _type_layout_string 7CoreHAP24HAPSpakePairSetupSessionC20CredentialFetchState33_FFB3B66732484B0775DD4AE3FA14FD0DLLO
+ _type_layout_string So15HAPFeatureFlagsV
+ block_copy_helper
+ block_descriptor
+ block_destroy_helper
+ logCategory._hmf_once_t214
+ logCategory._hmf_once_t69
+ logCategory._hmf_once_t856
+ logCategory._hmf_once_v215
+ logCategory._hmf_once_v70
+ logCategory._hmf_once_v857
- +[HAPPairingUtilities createAddPairingRequestForPairingIdentity:error:]
- -[HAPAccessoryServerBrowser isThreadAccessoryDiscoveredWithAccessoryServerIdentifier:]
- -[HAPAccessoryServerBrowserHAP2Adapter isThreadAccessoryDiscoveredWithAccessoryServerIdentifier:]
- -[HAPAccessoryServerIP _ensurePairingSessionIsInitializedWithType:]
- -[HAPAccessoryServerIP _queueAddPairingWithIdentifier:publicKey:admin:queue:completion:]
- -[HAPAccessoryServerIP _startAddPairingWithIdentifier:publicKey:admin:queue:completion:]
- GCC_except_table1043
- GCC_except_table1045
- GCC_except_table1151
- GCC_except_table1156
- GCC_except_table1160
- GCC_except_table1173
- GCC_except_table1187
- GCC_except_table1189
- GCC_except_table1191
- GCC_except_table1193
- GCC_except_table1319
- GCC_except_table1325
- GCC_except_table1327
- GCC_except_table1525
- GCC_except_table1733
- GCC_except_table1735
- GCC_except_table1740
- GCC_except_table1746
- GCC_except_table1748
- GCC_except_table1754
- GCC_except_table1756
- GCC_except_table1760
- GCC_except_table1766
- GCC_except_table1768
- GCC_except_table1770
- GCC_except_table1772
- GCC_except_table1777
- GCC_except_table1781
- GCC_except_table1791
- GCC_except_table1799
- GCC_except_table1806
- GCC_except_table1810
- GCC_except_table1814
- GCC_except_table1819
- GCC_except_table1857
- GCC_except_table1972
- GCC_except_table1977
- GCC_except_table1978
- GCC_except_table1980
- GCC_except_table1982
- GCC_except_table1991
- GCC_except_table1993
- GCC_except_table1997
- GCC_except_table2000
- GCC_except_table2002
- GCC_except_table2007
- GCC_except_table2024
- GCC_except_table2033
- GCC_except_table2035
- GCC_except_table2042
- GCC_except_table2046
- GCC_except_table2048
- GCC_except_table2051
- GCC_except_table2056
- GCC_except_table2060
- GCC_except_table2064
- GCC_except_table2070
- GCC_except_table2078
- GCC_except_table2091
- GCC_except_table2118
- GCC_except_table2149
- GCC_except_table2157
- GCC_except_table2361
- GCC_except_table2369
- GCC_except_table2370
- GCC_except_table2371
- GCC_except_table2372
- GCC_except_table2373
- GCC_except_table2374
- GCC_except_table2390
- GCC_except_table2404
- GCC_except_table2496
- GCC_except_table2556
- GCC_except_table2564
- GCC_except_table2575
- GCC_except_table2589
- GCC_except_table2592
- GCC_except_table2597
- GCC_except_table2606
- GCC_except_table2612
- GCC_except_table2614
- GCC_except_table2624
- GCC_except_table2647
- GCC_except_table2653
- GCC_except_table2835
- GCC_except_table2844
- GCC_except_table2894
- GCC_except_table2910
- GCC_except_table2912
- GCC_except_table2924
- GCC_except_table2931
- GCC_except_table2947
- GCC_except_table2962
- GCC_except_table2963
- GCC_except_table2966
- GCC_except_table2974
- GCC_except_table2981
- GCC_except_table2984
- GCC_except_table2989
- GCC_except_table2994
- GCC_except_table3034
- GCC_except_table3048
- GCC_except_table3051
- GCC_except_table3056
- GCC_except_table3058
- GCC_except_table3074
- GCC_except_table3090
- GCC_except_table3092
- GCC_except_table3104
- GCC_except_table3112
- GCC_except_table3176
- GCC_except_table3183
- GCC_except_table3185
- GCC_except_table3186
- GCC_except_table3209
- GCC_except_table3229
- GCC_except_table3457
- GCC_except_table3524
- GCC_except_table3525
- GCC_except_table3529
- GCC_except_table3532
- GCC_except_table3534
- GCC_except_table3535
- GCC_except_table3539
- GCC_except_table3540
- GCC_except_table3542
- GCC_except_table3549
- GCC_except_table3559
- GCC_except_table3562
- GCC_except_table3573
- GCC_except_table3574
- GCC_except_table3576
- GCC_except_table3578
- GCC_except_table3581
- GCC_except_table3584
- GCC_except_table3586
- GCC_except_table3589
- GCC_except_table3592
- GCC_except_table3604
- GCC_except_table3606
- GCC_except_table3610
- GCC_except_table3614
- GCC_except_table3618
- GCC_except_table3644
- GCC_except_table3673
- GCC_except_table3683
- GCC_except_table3686
- GCC_except_table3688
- GCC_except_table3690
- GCC_except_table3697
- GCC_except_table3698
- GCC_except_table3699
- GCC_except_table3776
- GCC_except_table3777
- GCC_except_table3778
- GCC_except_table3779
- GCC_except_table3780
- GCC_except_table3781
- GCC_except_table3782
- GCC_except_table3783
- GCC_except_table3784
- GCC_except_table3785
- GCC_except_table3787
- GCC_except_table3788
- GCC_except_table3789
- GCC_except_table3842
- GCC_except_table3937
- GCC_except_table3944
- GCC_except_table3986
- GCC_except_table3990
- GCC_except_table3993
- GCC_except_table3996
- GCC_except_table3999
- GCC_except_table4002
- GCC_except_table4005
- GCC_except_table4008
- GCC_except_table4011
- GCC_except_table4014
- GCC_except_table4019
- GCC_except_table4030
- GCC_except_table4034
- GCC_except_table4036
- GCC_except_table4039
- GCC_except_table4050
- GCC_except_table4058
- GCC_except_table4065
- GCC_except_table4071
- GCC_except_table4072
- GCC_except_table4075
- GCC_except_table4076
- GCC_except_table4094
- GCC_except_table4098
- GCC_except_table4099
- GCC_except_table4102
- GCC_except_table4108
- GCC_except_table4111
- GCC_except_table4113
- GCC_except_table4119
- GCC_except_table4121
- GCC_except_table4124
- GCC_except_table4135
- GCC_except_table4146
- GCC_except_table4159
- GCC_except_table4161
- GCC_except_table4167
- GCC_except_table4427
- GCC_except_table4433
- GCC_except_table4450
- GCC_except_table4454
- GCC_except_table4471
- GCC_except_table4479
- GCC_except_table4492
- GCC_except_table4506
- GCC_except_table4510
- GCC_except_table4623
- GCC_except_table507
- GCC_except_table5079
- GCC_except_table5087
- GCC_except_table5098
- GCC_except_table5140
- GCC_except_table5143
- GCC_except_table5144
- GCC_except_table5145
- GCC_except_table5146
- GCC_except_table521
- GCC_except_table5228
- GCC_except_table5229
- GCC_except_table5230
- GCC_except_table5231
- GCC_except_table5232
- GCC_except_table5233
- GCC_except_table5239
- GCC_except_table5240
- GCC_except_table5242
- GCC_except_table5249
- GCC_except_table5252
- GCC_except_table5254
- GCC_except_table5259
- GCC_except_table5262
- GCC_except_table5265
- GCC_except_table5269
- GCC_except_table5273
- GCC_except_table537
- GCC_except_table549
- GCC_except_table5759
- GCC_except_table5760
- GCC_except_table5779
- GCC_except_table5789
- GCC_except_table5792
- GCC_except_table5797
- GCC_except_table5800
- GCC_except_table5804
- GCC_except_table583
- GCC_except_table595
- GCC_except_table596
- GCC_except_table598
- GCC_except_table601
- GCC_except_table604
- GCC_except_table6073
- GCC_except_table6077
- GCC_except_table6122
- GCC_except_table6126
- GCC_except_table6128
- GCC_except_table6130
- GCC_except_table622
- GCC_except_table625
- GCC_except_table6318
- GCC_except_table632
- GCC_except_table6324
- GCC_except_table6328
- GCC_except_table6329
- GCC_except_table6330
- GCC_except_table6331
- GCC_except_table6337
- GCC_except_table635
- GCC_except_table6353
- GCC_except_table6386
- GCC_except_table6387
- GCC_except_table6388
- GCC_except_table6408
- GCC_except_table6420
- GCC_except_table6423
- GCC_except_table6428
- GCC_except_table6430
- GCC_except_table6444
- GCC_except_table658
- GCC_except_table6678
- GCC_except_table6691
- GCC_except_table6696
- GCC_except_table6699
- GCC_except_table6700
- GCC_except_table6702
- GCC_except_table6703
- GCC_except_table6705
- GCC_except_table6735
- GCC_except_table675
- GCC_except_table6757
- GCC_except_table6761
- GCC_except_table6765
- GCC_except_table6770
- GCC_except_table6774
- GCC_except_table6778
- GCC_except_table6782
- GCC_except_table6786
- GCC_except_table6794
- GCC_except_table6796
- GCC_except_table6800
- GCC_except_table6863
- GCC_except_table6864
- GCC_except_table6865
- GCC_except_table6867
- GCC_except_table6868
- GCC_except_table6869
- GCC_except_table6928
- GCC_except_table6933
- GCC_except_table6951
- GCC_except_table6964
- GCC_except_table6967
- GCC_except_table6968
- GCC_except_table6973
- GCC_except_table6976
- GCC_except_table6983
- GCC_except_table6986
- GCC_except_table7000
- GCC_except_table7007
- GCC_except_table7013
- GCC_except_table702
- GCC_except_table7022
- GCC_except_table7024
- GCC_except_table7030
- GCC_except_table7031
- GCC_except_table7038
- GCC_except_table7050
- GCC_except_table7059
- GCC_except_table706
- GCC_except_table7074
- GCC_except_table7075
- GCC_except_table7080
- GCC_except_table7084
- GCC_except_table7085
- GCC_except_table7088
- GCC_except_table709
- GCC_except_table7094
- GCC_except_table7098
- GCC_except_table7102
- GCC_except_table7104
- GCC_except_table7106
- GCC_except_table711
- GCC_except_table7110
- GCC_except_table7224
- GCC_except_table725
- GCC_except_table7261
- GCC_except_table7317
- GCC_except_table7320
- GCC_except_table7324
- GCC_except_table7330
- GCC_except_table7337
- GCC_except_table7338
- GCC_except_table7354
- GCC_except_table7358
- GCC_except_table7359
- GCC_except_table7360
- GCC_except_table7410
- GCC_except_table7412
- GCC_except_table7415
- GCC_except_table744
- GCC_except_table7442
- GCC_except_table7443
- GCC_except_table7448
- GCC_except_table7468
- GCC_except_table7486
- GCC_except_table7487
- GCC_except_table7488
- GCC_except_table7497
- GCC_except_table7502
- GCC_except_table7504
- GCC_except_table7522
- GCC_except_table7529
- GCC_except_table7536
- GCC_except_table7541
- GCC_except_table7559
- GCC_except_table7560
- GCC_except_table7565
- GCC_except_table7574
- GCC_except_table7582
- GCC_except_table7583
- GCC_except_table7587
- GCC_except_table7589
- GCC_except_table7591
- GCC_except_table7595
- GCC_except_table7616
- GCC_except_table7618
- GCC_except_table7619
- GCC_except_table7645
- GCC_except_table765
- GCC_except_table766
- GCC_except_table774
- GCC_except_table777
- GCC_except_table7809
- GCC_except_table782
- GCC_except_table786
- GCC_except_table7872
- GCC_except_table7904
- GCC_except_table7907
- GCC_except_table796
- GCC_except_table797
- GCC_except_table8074
- GCC_except_table8112
- GCC_except_table8149
- GCC_except_table8227
- GCC_except_table8229
- GCC_except_table823
- GCC_except_table8231
- GCC_except_table8233
- GCC_except_table8235
- GCC_except_table8237
- GCC_except_table8239
- GCC_except_table8241
- GCC_except_table8243
- GCC_except_table8245
- GCC_except_table8247
- GCC_except_table8250
- GCC_except_table8252
- GCC_except_table8254
- GCC_except_table8262
- GCC_except_table8268
- GCC_except_table8273
- GCC_except_table8276
- GCC_except_table8279
- GCC_except_table8305
- GCC_except_table8308
- GCC_except_table8309
- GCC_except_table8328
- GCC_except_table8329
- GCC_except_table8330
- GCC_except_table8332
- GCC_except_table8333
- GCC_except_table8335
- GCC_except_table8336
- GCC_except_table8337
- GCC_except_table8340
- GCC_except_table8342
- GCC_except_table8346
- GCC_except_table8347
- GCC_except_table8351
- GCC_except_table837
- GCC_except_table838
- GCC_except_table8402
- GCC_except_table8409
- GCC_except_table8510
- GCC_except_table8512
- GCC_except_table8514
- GCC_except_table8517
- GCC_except_table8519
- GCC_except_table8521
- GCC_except_table8524
- GCC_except_table8530
- GCC_except_table8535
- GCC_except_table854
- GCC_except_table876
- GCC_except_table894
- GCC_except_table916
- GCC_except_table920
- GCC_except_table934
- GCC_except_table939
- __77-[HAPAccessoryServer removePairingsWithRemovedAccessoryKey:queue:completion:]_block_invoke
- __77-[HAPAccessoryServer removePairingsWithRemovedAccessoryKey:queue:completion:]_block_invoke_2
- __81-[HAPAccessoryServerIP _establishSecureSessionAndRemovePairing:queue:completion:]_block_invoke
- __88-[HAPAccessoryServerIP _queueAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke
- __88-[HAPAccessoryServerIP _startAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke
- ___77-[HAPAccessoryServer removePairingsWithRemovedAccessoryKey:queue:completion:]_block_invoke
- ___77-[HAPAccessoryServer removePairingsWithRemovedAccessoryKey:queue:completion:]_block_invoke_2
- ___77-[HAPAccessoryServer removePairingsWithRemovedAccessoryKey:queue:completion:]_block_invoke_3
- ___78-[HAPAccessoryServerBrowserHAP2Adapter discoverAccessoryServerWithIdentifier:]_block_invoke_3
- ___78-[HAPAccessoryServerBrowserHAP2Adapter discoverAccessoryServerWithIdentifier:]_block_invoke_4
- ___88-[HAPAccessoryServerIP _queueAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke
- ___88-[HAPAccessoryServerIP _startAddPairingWithIdentifier:publicKey:admin:queue:completion:]_block_invoke
- ___97-[HAPAccessoryServerBrowserHAP2Adapter isThreadAccessoryDiscoveredWithAccessoryServerIdentifier:]_block_invoke
- ___block_descriptor_73_e8_32s40s48s56bs64w_e17_v16?0"NSError"8l
- _objc_msgSend$_queueAddPairingWithIdentifier:publicKey:admin:queue:completion:
- _objc_msgSend$_startAddPairingWithIdentifier:publicKey:admin:queue:completion:
- _objc_msgSend$addPairingRequestWithIdentity:error:
- _objc_msgSend$createAddPairingRequestForPairingIdentity:error:
- _objc_msgSend$enableRemovedAccessoryKey:completionQueue:completion:
- _objc_msgSend$isKnownToSystemCommissioner
- logCategory._hmf_once_t164
- logCategory._hmf_once_t59
- logCategory._hmf_once_t790
- logCategory._hmf_once_t804
- logCategory._hmf_once_v165
- logCategory._hmf_once_v60
- logCategory._hmf_once_v791
- logCategory._hmf_once_v805
CStrings:
+ "%@ Couldn't serialize add pairing request TLVs: %@"
+ "%@ ECDSA capability check requested"
+ "%@ ECDSA key found for accessory %@"
+ "%@ Failed to fetch ECDSA controller key for %@: %@"
+ "%@ Failed to fetch ECDSA key for peer %@: %@"
+ "%@ Network configuration request received for pair setup session"
+ "%@ No ECDSA key found for accessory %@: %@"
+ "%@ No accessory server for ECDSA key lookup"
+ "%@ No accessory server for ECDSA local pairing identity"
+ "%@ No accessory server for pair-verify TLKs lookup"
+ "%@ No storage for ECDSA key lookup"
+ "%@ No storage for ECDSA local pairing identity"
+ "%@ No storage for pair-verify TLKs lookup"
+ "%@ Setup code request received for pair setup session"
+ ", Hash: %@"
+ "AES-CCM auth tag length must be one of "
+ "AES-CCM decryption failed with error: %d"
+ "AES-CCM encryption failed with error: %d"
+ "AES-CCM nonce length must be 7–13 bytes (got "
+ "AES-CCM-128 decryption failed"
+ "AES-CCM-128 decryption requires a "
+ "AES-CCM-128 decryption requires non-empty key, nonce, AAD, ciphertext, and auth tag"
+ "AES-CMAC KDF failed with error: %d"
+ "Accessory identifier mismatches. Received: %@"
+ "Additional pairing info available for M5"
+ "Additional pairing request received"
+ "AdditionalWifiDataProxPairing"
+ "An ECDSA secure session is already either being established or established"
+ "B32@?0@\"HAP2CoAPIOThreadQueueEntry\"8Q16^B24"
+ "ChaCha20-Poly1305"
+ "Cloned removed ECDSA accessory key %@ with error %u"
+ "Coap IO reclaimed %lu in-flight + %lu queued slot(s) on unregister (%lu/%lu now in use)"
+ "Coap IO sliding window now full (%lu slots in use), %lu message(s) still queued"
+ "Coap IO slot allocated: %lu/%lu in use, %lu queued"
+ "Coap IO slot(s) released x%lu on completion: %lu/%lu in use, %lu queued"
+ "CoreHAP.HAPECDSAKeyPairVerifySession"
+ "CoreHAP.HAPSpakePairSetupSession"
+ "CoreHAP_Private.HAPECDSAKeyPairVerifySessionObjCWrapper"
+ "CoreHAP_Private.HAPSpakePairSetupSessionObjCWrapper"
+ "Could not retrieve peer long term key from pairing identifier %s"
+ "Decrypted M2 proof data didn't include required TLVs"
+ "Deferred Matter Onboarding Payload: "
+ "Delegate not available to create encrypted proof"
+ "Deriving session keys from foreign session"
+ "ECC P-256"
+ "ECC P-256 pairing key data must be 64 bytes long"
+ "ECC P-256 signature verification failed: %s"
+ "ECDSA key pair verify session did stop with error: %@"
+ "ECDSA public key derivation failed: %@"
+ "ECDSA public key keychain item deserialization failed: %@"
+ "ECDSA signature created for encrypted proof"
+ "ECDSA signature verification failed"
+ "Ed25519 sign failed with error: %d"
+ "Encoding %{private}@ failed"
+ "Encrypted data too short (%ld bytes)"
+ "Establish relationship between ECDSA public key Accessory : [%@] & controller key : [%@]"
+ "Exchange data received in invalid state: %hhu"
+ "Exchange in state %s failed with error: %@"
+ "Failed to allocate memory to export ECDSA private key"
+ "Failed to append encrypted data TLV: %s"
+ "Failed to derive ECDSA private key from random data with ccec status %lu"
+ "Failed to derive ECDSA private key: %@"
+ "Failed to derive ECDSA public key: %@"
+ "Failed to derive additional key '%@' from foreign session with error: %@"
+ "Failed to derive broadcast key from foreign session with error: %@"
+ "Failed to export ECDSA private key generated from random data with ccec status %lu"
+ "Failed to fetch peer LTPK: %@"
+ "Failed to get input key from foreign session with error: %@"
+ "Failed to get output key from foreign session with error: %@"
+ "Failed to retrieve TLKs for ECDSA pair-verify: %@"
+ "Failed to retrieve read key from pair verify session: %@"
+ "Failed to retrieve write key from pair verify session: %@"
+ "Failed to save accessory's identifier and ECDSA public key to the keystore with error: %@"
+ "Failed to serialize accessory ECDSA public key"
+ "Failed to serialize pairing key '%{private}@' for accessory %@ - error %ld"
+ "Got HAP setup code: %s"
+ "HAP P-256 Key From Ed25519 Key"
+ "HAP.keyType"
+ "HAPSpakePairSetupSession initialized with featureFlags: 0x%s, using %s encryption"
+ "HK ECDSA Privacy IPK"
+ "HK ECDSA Privacy v1 BPK"
+ "HK ECDSA Privacy v1 IPK"
+ "HK ECDSA Privacy v1 TLK"
+ "HomeKit accessory that has been paired with ECDSA key with this account."
+ "HomeKit-Pair-Setup"
+ "HomeKit-Pair-Setup-HomeKit-Pair-Setup-HomeKit-Pair-Setup"
+ "HomeKit-Pairing-Info"
+ "HomeKit-Pairing-Salt"
+ "HomeKit-Verifier"
+ "Identifier TLV could not be added to proof"
+ "Identifier could not be encrypted for proof"
+ "Ignoring prefetched MFi token injection (token empty or uuid not 16 bytes)"
+ "Including AdditionalWifiData in M5 encrypted data (%ld bytes)"
+ "Including TLK TLV in M5 encrypted data"
+ "Including Thread credentials in M5 encrypted data"
+ "Including WiFi country code in M5 encrypted data"
+ "Including WiFi credentials in M5 encrypted data"
+ "Including additional pairing TLV in M5 encrypted data"
+ "Injected prefetched MFi token (%ld bytes); starting validate+roll"
+ "Invalid number of keychain items(%tu) for removed ECDSA accessory '%@'"
+ "Key Bag Pairing Identity to derive ECDSA Key: %@"
+ "Keys not available for computing shared secret"
+ "Keys not available to create encrypted proof"
+ "Local pairing identity available to create encrypted proof"
+ "Local pairing identity does not have private key to create encrypted proof"
+ "Looking for associated controller key for ECDSA key accessory : [%@]"
+ "M2 IPK-based session key derivation with %ld TLK(s)"
+ "M2 TLK decryption succeeded"
+ "M2 TLK derivation failed, trying next"
+ "M2 decryption succeeded"
+ "M2 keys available"
+ "M2 no TLK produced a valid session key"
+ "M2 peer public key OK"
+ "M2 shared secret computed"
+ "M2: Setup Code does not match"
+ "M2: Using hashed setup code"
+ "M2: Using repeated setup code"
+ "M2: cipherSuite %llu (%{public}s)"
+ "M2: extraFlags 0x%s"
+ "M2: flags 0x%s"
+ "M2: no cipherSuite advertised; defaulting to legacy (suite 0)"
+ "M2: unknown cipherSuite raw value %llu"
+ "M4: 32-byte hash but no NDEF token to verify it — prompting uncertified"
+ "M4: Accessory using %{public}s KDF"
+ "M4: Accessory using CMAC-CTR KDF (detected via trial-decrypt)"
+ "M4: prefetched token does not match M4 hash — prompting to add as uncertified"
+ "M4: received mfiToken (%ld bytes), uuid (%ld bytes)"
+ "M4: requesting MFi token validate+roll"
+ "M5 credentials snapshot: wifi=%{public}s, thread=%{public}s"
+ "M5: %{public}s mfiToken (%ld bytes)"
+ "M5: LTPK identifier=%{public}s ecdsaPublicKey=%{public}s"
+ "M5: no rolled token and nothing to echo"
+ "M5: no rolled token — echoing token (%ld bytes)"
+ "M5: no rolled/echo token and only the 32-byte M4 hash remains — failing rather than transmitting it"
+ "M5: public key x963Representation: %{public}s"
+ "M5: using rolled MFi token (%ld bytes)"
+ "M6: confirming rolled MFi token"
+ "MFi early-auth: DISMISSED — M4 sent a full token (%ld bytes), not the primed hash; abandoning tap-time validate+roll, validating M4 token"
+ "MFi early-auth: INTERRUPTED — abandoning validate+roll still in flight (state inProgress → cancelled)"
+ "MFi early-auth: M4 hash VERIFIED against tap-time NDEF token — early auth accepted; consuming validate+roll for M5"
+ "MFi early-auth: M4 hash verified and validate+roll already finished — using its result for M5"
+ "MFi early-auth: M4 hash verified but validate+roll still in flight — M5 will continue when it returns"
+ "MFi early-auth: M4 was waiting on the validate+roll — driving M5 now"
+ "MFi early-auth: cancel requested (state %{public}s → cancelled)"
+ "MFi early-auth: delegate did not handle validate+roll — completing with no rolled token"
+ "MFi early-auth: discarding already-finished validate+roll (state completed → cancelled)"
+ "MFi early-auth: state notStarted → inProgress (validate+roll started for tap-time NDEF token, %ld bytes)"
+ "MFi early-auth: validate+roll FAILED (state inProgress → completed): %s"
+ "MFi early-auth: validate+roll finished (state inProgress → completed) — no rolled token returned"
+ "MFi early-auth: validate+roll finished (state inProgress → completed) — rolled token ready (%ld bytes)"
+ "MFi early-auth: validate+roll in unexpected state at M4 (hash verified) — failing pair-setup"
+ "MFi early-auth: validate+roll returned after it was abandoned at M4 — discarding result"
+ "MFi token roll completed but session no longer in M5 — discarding"
+ "MFi token validate/roll failed: %s"
+ "MFi: delegate accepted not-certified pair; resuming M5 with echoed token"
+ "MFi: delegate accepted not-certified pair; resuming M5 with no software token"
+ "MFi: delegate declined not-certified pair; propagating original error"
+ "MFi: prompt resolved after teardown — discarding"
+ "NFC"
+ "Neither Ed25519 key nor ECDSA key is available for the accessory to establish a secure session"
+ "No IDS Date provider to set time for cloned removed ECDSA accessory key"
+ "No additional pairing info (current user may be owner)"
+ "Pair Setup session stopped with error: %@"
+ "Pair Verify session completed"
+ "Pair Verify session stopped with error: %@"
+ "Pair verify TLK not available - failing pair setup"
+ "Pair-Setup-Accessory-Sign"
+ "Pair-Setup-Controller-Sign"
+ "Pair-Setup-Encrypt"
+ "Pair-Verify-Encrypt-Info"
+ "Pair-Verify-Encrypt-Salt"
+ "Pair-setup M6 bad status %hhu"
+ "Pair-setup M6 invalid encrypted data length: %ld"
+ "Pair-setup M6 pairing complete!"
+ "Pair-setup TLK required but not provided for AES-CCM accessory"
+ "Pair-setup failed: %s"
+ "Pair-setup initializing using SPAKE2+"
+ "Pair-setup paused after M4, pending commit (consent)"
+ "Pair-setup: M1"
+ "Pair-setup: M2"
+ "Pair-setup: M3"
+ "Pair-setup: M4"
+ "Pair-setup: M5"
+ "Pair-setup: M5: Unable to retrieve pairing identity: %s"
+ "Pair-setup: M6"
+ "Pair-verify TLKs required but not provided"
+ "Pair-verify aborted with no accessory public key"
+ "Pair-verify completion handling failed: %d"
+ "Pair-verify initializing using ECC NIST P-256"
+ "Pair-verify using Ed25519 key with length %lu"
+ "Pair-verify using removed accessory ECDSA key"
+ "Pair-verify using removed accessory ECDSA key without TLKs"
+ "Pair-verify using removed accessory Ed25519 key"
+ "Pair-verify: M1"
+ "Pair-verify: M2"
+ "Pair-verify: M3"
+ "Pair-verify: M4"
+ "Pairing identifier in M2 could not be decoded"
+ "Pairing.ECDSAPairVerify"
+ "Per-accessory deferred Matter onboarding payload"
+ "Pre-warming Thread credentials during M1"
+ "Pre-warming WiFi credentials during M1"
+ "Prefetched MFi token already injected; ignoring"
+ "Proceeding with pair-setup commit (M4→M5)"
+ "Progressing pair verify using pairVerifySession"
+ "Progressing pairing using pairSetupSession"
+ "Providing local pairing identity for ECDSA pair-verify: identifier=%{public}s ecdsaPublicKey=%{public}s"
+ "ProxPairing"
+ "Received M2 encrypted data didn't include required TLVs"
+ "Received M4 error %llu"
+ "Received invalid state M%llu message"
+ "Received public key of unexpected size %ld"
+ "Removed ECDSA public key keychain item deserialization failed: %@"
+ "Removed HomeKit Accessory ECDSA key which used to be paired with this account."
+ "Removed HomeKit ECDSA Accessory"
+ "Removing ECC NIST P-256 key pairing from accessory"
+ "Removing pairing from accessory using removed ECDSA key"
+ "Request for local pairing identity for ECDSA key accessory"
+ "Request to save ECDSA pairing key for peer: %@"
+ "Request to save ECDSA public key of pairing peer: %@"
+ "Returning ECDSA local pairng identity for security session: %@, with error: %@"
+ "Saving key requested with invalid arguments, key %{private}@, name %@"
+ "Secure Transport PairVerify: Timed out waiting for ECDSA key for peer %@"
+ "Secure Transport PairVerify: Timed out waiting for local ECDSA pair-setup identity"
+ "Secure Transport PairVerify: Unexpected didPairWithPeer call - this is for pair-setup, not pair-verify"
+ "Secure Transport PairVerify: Unexpected local pairing identity request - this is for pair-setup, not pair-verify"
+ "Secure Transport: Checking ECDSA capability"
+ "Secure Transport: Creating ECDSA key pair verify session"
+ "Secure Transport: Delegate doesn't support ECDSA capability check - using standard session"
+ "Secure Transport: ECDSA capability check failed (%@) - using standard session"
+ "Secure Transport: ECDSA key available - creating ECDSA session"
+ "Secure Transport: ECDSA pair verify session completed successfully"
+ "Secure Transport: ECDSA pair verify session failed: %@"
+ "Secure Transport: ECDSA session failure: %@"
+ "Secure Transport: Failed to fetch ECDSA key for peer %@: %@"
+ "Secure Transport: Failed to fetch pair-verify TLKs: %@"
+ "Secure Transport: Finished force closing after ECDSA pair verify failure"
+ "Secure Transport: Finished force closing after ECDSA session failure"
+ "Secure Transport: No ECDSA key available - using standard session"
+ "Secure Transport: No ECDSA session to create security session from"
+ "Secure Transport: No delegate for ECDSA capability check"
+ "Secure Transport: No delegate for ECDSA key lookup"
+ "Secure Transport: No delegate for pair-verify IPKs lookup"
+ "Session deallocating with network credential fetch in progress (wifi=%{bool}d, thread=%{bool}d)"
+ "Session no longer active, discarding Thread credentials"
+ "Session no longer active, discarding WiFi credentials"
+ "Shared secret derived"
+ "SharedAdminProxPairing"
+ "Signature TLV could not be added to proof"
+ "Skipping TLK with invalid length %ld"
+ "Skipping network credential pre-warming - accessory does not support AES-CCM"
+ "Split setup key derivation failed: %s"
+ "Starting Pair-setup"
+ "Stopping Pair-setup"
+ "TLK data available for M5"
+ "Thread credential delegate method not implemented - skipping"
+ "Thread credential fetch already in progress or completed"
+ "Thread credential fetch completed but no credentials available"
+ "Thread credential fetch failed: %s"
+ "Thread credentials pre-warmed successfully"
+ "Thread network configuration TLV request received"
+ "Unable to associate accessory %@ (Ed25519 error: %@, ECDSA error: %@)"
+ "Unable to create Spake2+ prover: %s"
+ "Unable to decrypt product data string (%s)!"
+ "Unable to establish relationship between accessory and controller key (ECDSA): %@"
+ "Unable to fetch accessory ECDSA public key for accessory with error: %@"
+ "Unable to retrieve Spake2+ shared key: %s"
+ "Unable to retrieve pair-setup identifier from accessory server!"
+ "Unable to retrieve shared secret key!"
+ "Unable to save the accessory public key inside KeyChain: %{private}@"
+ "Unable to verify confirmV and generate shared secret: %s"
+ "Unable to verify peer key: %s"
+ "Unknown pairing key type %lu"
+ "Using ECDSA Controller Pairing Identity: %@"
+ "We haven't exchanged public key with the accessory to remove pairing"
+ "WiFi credential delegate method not implemented - skipping"
+ "WiFi credential fetch already in progress or completed"
+ "WiFi credential fetch completed but no credentials available"
+ "WiFi credential fetch failed: %s"
+ "WiFi credentials pre-warmed successfully"
+ "WiFi network configuration TLV request received"
+ "Wrapper not available to create encrypted proof"
+ "[%{public}@] Accessory identifier mismatches. Received: %@"
+ "[%{public}@] An ECDSA secure session is already either being established or established"
+ "[%{public}@] Cloned removed ECDSA accessory key %@ with error %u"
+ "[%{public}@] Deriving session keys from foreign session"
+ "[%{public}@] ECC P-256 pairing key data must be 64 bytes long"
+ "[%{public}@] ECDSA key pair verify session did stop with error: %@"
+ "[%{public}@] ECDSA public key derivation failed: %@"
+ "[%{public}@] ECDSA public key keychain item deserialization failed: %@"
+ "[%{public}@] Encoding %{private}@ failed"
+ "[%{public}@] Establish relationship between ECDSA public key Accessory : [%@] & controller key : [%@]"
+ "[%{public}@] Failed to allocate memory to export ECDSA private key"
+ "[%{public}@] Failed to derive ECDSA private key from random data with ccec status %lu"
+ "[%{public}@] Failed to derive ECDSA private key: %@"
+ "[%{public}@] Failed to derive ECDSA public key: %@"
+ "[%{public}@] Failed to derive additional key '%@' from foreign session with error: %@"
+ "[%{public}@] Failed to derive broadcast key from foreign session with error: %@"
+ "[%{public}@] Failed to export ECDSA private key generated from random data with ccec status %lu"
+ "[%{public}@] Failed to fetch peer LTPK: %@"
+ "[%{public}@] Failed to get input key from foreign session with error: %@"
+ "[%{public}@] Failed to get output key from foreign session with error: %@"
+ "[%{public}@] Failed to retrieve TLKs for ECDSA pair-verify: %@"
+ "[%{public}@] Failed to retrieve read key from pair verify session: %@"
+ "[%{public}@] Failed to retrieve write key from pair verify session: %@"
+ "[%{public}@] Failed to save accessory's identifier and ECDSA public key to the keystore with error: %@"
+ "[%{public}@] Failed to serialize accessory ECDSA public key"
+ "[%{public}@] Failed to serialize pairing key '%{private}@' for accessory %@ - error %ld"
+ "[%{public}@] Invalid number of keychain items(%tu) for removed ECDSA accessory '%@'"
+ "[%{public}@] Looking for associated controller key for ECDSA key accessory : [%@]"
+ "[%{public}@] Neither Ed25519 key nor ECDSA key is available for the accessory to establish a secure session"
+ "[%{public}@] No IDS Date provider to set time for cloned removed ECDSA accessory key"
+ "[%{public}@] Pair Setup session stopped with error: %@"
+ "[%{public}@] Pair Verify session completed"
+ "[%{public}@] Pair Verify session stopped with error: %@"
+ "[%{public}@] Pair-setup initializing using SPAKE2+"
+ "[%{public}@] Pair-verify aborted with no accessory public key"
+ "[%{public}@] Pair-verify completion handling failed: %d"
+ "[%{public}@] Pair-verify initializing using ECC NIST P-256"
+ "[%{public}@] Pair-verify using Ed25519 key with length %lu"
+ "[%{public}@] Pair-verify using removed accessory ECDSA key"
+ "[%{public}@] Pair-verify using removed accessory ECDSA key without TLKs"
+ "[%{public}@] Pair-verify using removed accessory Ed25519 key"
+ "[%{public}@] Progressing pair verify using pairVerifySession"
+ "[%{public}@] Progressing pairing using pairSetupSession"
+ "[%{public}@] Removed ECDSA public key keychain item deserialization failed: %@"
+ "[%{public}@] Removing ECC NIST P-256 key pairing from accessory"
+ "[%{public}@] Removing pairing from accessory using removed ECDSA key"
+ "[%{public}@] Request for local pairing identity for ECDSA key accessory"
+ "[%{public}@] Request to save ECDSA public key of pairing peer: %@"
+ "[%{public}@] Returning ECDSA local pairng identity for security session: %@, with error: %@"
+ "[%{public}@] Saving key requested with invalid arguments, key %{private}@, name %@"
+ "[%{public}@] Unable to associate accessory %@ (Ed25519 error: %@, ECDSA error: %@)"
+ "[%{public}@] Unable to establish relationship between accessory and controller key (ECDSA): %@"
+ "[%{public}@] Unable to fetch accessory ECDSA public key for accessory with error: %@"
+ "[%{public}@] Unable to save the accessory public key inside KeyChain: %{private}@"
+ "[%{public}@] Unknown pairing key type %lu"
+ "[%{public}@] We haven't exchanged public key with the accessory to remove pairing"
+ "accessoryPairingIdentifier"
+ "accessoryPairingKey"
+ "accessoryUUID"
+ "com.apple.CoreHAP.HAPSpakePairSetupSession"
+ "data.length == 44"
+ "ecdsaPairingKey.data.length == HAPECCP256PublicKeyBytes"
+ "hapE"
+ "hapF"
+ "init()"
+ "mtOU"
+ "p256NistKdfCmacAes128Sha256 not yet supported"
+ "payload"
+ "sizeof dummyKeyBytes == HMFPairingKeyLength"
+ "v24@?0@\"HAPECDSAPairingKey\"8@\"NSError\"16"
+ "v40@?0@\"NSData\"8@\"NSString\"16@\"HAPAdditionalWifiData\"24@\"NSError\"32"
+ "\xf0\xd1"
- "Found thread accessory with server ID known = %d paired = %d"
- "Unable to associate accessory %@ (Ed25519 error: %@)"
- "[%{public}@] Found thread accessory with server ID known = %d paired = %d"
- "[%{public}@] Unable to associate accessory %@ (Ed25519 error: %@)"
- "\xf0\xc1"
```
