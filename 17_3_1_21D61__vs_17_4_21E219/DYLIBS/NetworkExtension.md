## NetworkExtension

> `/System/Library/Frameworks/NetworkExtension.framework/NetworkExtension`

```diff

-1838.80.4.0.0
-  __TEXT.__text: 0x198b8c
-  __TEXT.__auth_stubs: 0x3490
-  __TEXT.__objc_methlist: 0xca14
-  __TEXT.__const: 0x1c58
-  __TEXT.__cstring: 0x14105
+1838.102.2.0.0
+  __TEXT.__text: 0x198f74
+  __TEXT.__auth_stubs: 0x34e0
+  __TEXT.__objc_methlist: 0xca7c
+  __TEXT.__const: 0x2018
+  __TEXT.__cstring: 0x14215
   __TEXT.__constg_swiftt: 0x100
   __TEXT.__swift5_typeref: 0x49
   __TEXT.__swift5_reflstr: 0x35

   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x14
-  __TEXT.__gcc_except_tab: 0x399c
-  __TEXT.__oslogstring: 0x1cfff
-  __TEXT.__unwind_info: 0x4024
+  __TEXT.__gcc_except_tab: 0x39a0
+  __TEXT.__oslogstring: 0x1cf39
+  __TEXT.__unwind_info: 0x4014
   __TEXT.__eh_frame: 0x120
   __TEXT.__objc_classname: 0x21fc
-  __TEXT.__objc_methname: 0x17903
+  __TEXT.__objc_methname: 0x17ab1
   __TEXT.__objc_methtype: 0x3356
-  __TEXT.__objc_stubs: 0xe6a0
+  __TEXT.__objc_stubs: 0xe760
   __DATA_CONST.__got: 0xa00
-  __DATA_CONST.__const: 0x52b8
+  __DATA_CONST.__const: 0x52e8
   __DATA_CONST.__objc_classlist: 0x9a8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x17bd0
-  __DATA_CONST.__objc_selrefs: 0x4790
-  __DATA_CONST.__objc_arraydata: 0x100
-  __AUTH_CONST.__const: 0xd18
+  __DATA_CONST.__objc_const: 0x17ca0
+  __DATA_CONST.__objc_selrefs: 0x47c0
+  __DATA_CONST.__objc_protorefs: 0xf0
+  __DATA_CONST.__objc_classrefs: 0x9e0
+  __DATA_CONST.__objc_superrefs: 0x6c0
+  __DATA_CONST.__objc_arraydata: 0x118
+  __AUTH_CONST.__const: 0xdb8
   __AUTH_CONST.__auth_ptr: 0x58
   __AUTH_CONST.__objc_const: 0x48
-  __AUTH_CONST.__cfstring: 0x15440
+  __AUTH_CONST.__cfstring: 0x15660
   __AUTH_CONST.__objc_intobj: 0x3c0
-  __AUTH_CONST.__objc_arrayobj: 0xf0
+  __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x1a58
+  __AUTH_CONST.__auth_got: 0x1a80
   __AUTH.__objc_data: 0x0
-  __DATA.__objc_protorefs: 0xf0
-  __DATA.__objc_classrefs: 0x9e0
-  __DATA.__objc_superrefs: 0x6c0
-  __DATA.__objc_ivar: 0x1904
+  __DATA.__objc_ivar: 0x1918
   __DATA.__data: 0x16e8
   __DATA.__common: 0x158
   __DATA.__bss: 0x998
-  __DATA_DIRTY.__const: 0x400
+  __DATA_DIRTY.__const: 0x360
   __DATA_DIRTY.__objc_const: 0x8898
   __DATA_DIRTY.__objc_data: 0x6130
   __DATA_DIRTY.__data: 0x28

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 6024
-  Symbols:   20230
-  CStrings:  11236
+  Functions: 6022
+  Symbols:   20270
+  CStrings:  11266
 
Symbols:
+ +[NEPolicyCondition scopedInterfaceFlags:eflags:xflags:]
+ -[NEAppProxyProvider fetchFlowStatesWithCompletionHandler:]
+ -[NEConfiguration usesPolicyBasedRouting]
+ -[NEIKEv2ChildSAProposal matchesLocalProposal:checkDHGroup:]
+ -[NEIKEv2DHKeys createSharedSecretForRemotePublicKey:ecdhKey:dhContext:]
+ -[NEIKEv2DeleteChildContext .cxx_destruct]
+ -[NEIKEv2IKESAProposal matchesLocalProposal:]
+ -[NEIKEv2PRFProtocol digest]
+ -[NEIKEv2Session removeChild:withReason:]
+ -[NEVPNConnectivityManager setUsesPolicyBasedRouting:]
+ -[NEVPNConnectivityManager usesPolicyBasedRouting]
+ -[NEVPNProtocol excludeDeviceCommunication]
+ -[NEVPNProtocol setExcludeDeviceCommunication:]
+ -[NSMutableString(NEPrettyPrint) appendPrettyHex:withName:andIndent:options:]
+ GCC_except_table102
+ GCC_except_table1038
+ GCC_except_table1039
+ GCC_except_table1044
+ GCC_except_table1045
+ GCC_except_table110
+ GCC_except_table1203
+ GCC_except_table1204
+ GCC_except_table1205
+ GCC_except_table1206
+ GCC_except_table1212
+ GCC_except_table1217
+ GCC_except_table1218
+ GCC_except_table1231
+ GCC_except_table1242
+ GCC_except_table1243
+ GCC_except_table128
+ GCC_except_table1368
+ GCC_except_table146
+ GCC_except_table1493
+ GCC_except_table1494
+ GCC_except_table1499
+ GCC_except_table1502
+ GCC_except_table1556
+ GCC_except_table1557
+ GCC_except_table1558
+ GCC_except_table1559
+ GCC_except_table1568
+ GCC_except_table1575
+ GCC_except_table1576
+ GCC_except_table1583
+ GCC_except_table1589
+ GCC_except_table1609
+ GCC_except_table1635
+ GCC_except_table2337
+ GCC_except_table248
+ GCC_except_table3050
+ GCC_except_table3061
+ GCC_except_table3075
+ GCC_except_table3076
+ GCC_except_table3093
+ GCC_except_table3134
+ GCC_except_table3140
+ GCC_except_table3174
+ GCC_except_table3175
+ GCC_except_table3260
+ GCC_except_table3282
+ GCC_except_table3517
+ GCC_except_table3523
+ GCC_except_table3526
+ GCC_except_table3611
+ GCC_except_table371
+ GCC_except_table3757
+ GCC_except_table3768
+ GCC_except_table3774
+ GCC_except_table3794
+ GCC_except_table3795
+ GCC_except_table3796
+ GCC_except_table3801
+ GCC_except_table3806
+ GCC_except_table3807
+ GCC_except_table3813
+ GCC_except_table3820
+ GCC_except_table3821
+ GCC_except_table3893
+ GCC_except_table3894
+ GCC_except_table3902
+ GCC_except_table3997
+ GCC_except_table3999
+ GCC_except_table4000
+ GCC_except_table4002
+ GCC_except_table4082
+ GCC_except_table4249
+ GCC_except_table4263
+ GCC_except_table4275
+ GCC_except_table4295
+ GCC_except_table4297
+ GCC_except_table4303
+ GCC_except_table4305
+ GCC_except_table438
+ GCC_except_table4394
+ GCC_except_table4461
+ GCC_except_table4482
+ GCC_except_table4495
+ GCC_except_table4597
+ GCC_except_table4638
+ GCC_except_table4684
+ GCC_except_table4686
+ GCC_except_table4782
+ GCC_except_table4802
+ GCC_except_table4804
+ GCC_except_table4806
+ GCC_except_table4813
+ GCC_except_table4853
+ GCC_except_table4857
+ GCC_except_table4860
+ GCC_except_table4902
+ GCC_except_table4923
+ GCC_except_table4926
+ GCC_except_table4996
+ GCC_except_table518
+ GCC_except_table519
+ GCC_except_table525
+ GCC_except_table530
+ GCC_except_table531
+ GCC_except_table5315
+ GCC_except_table5327
+ GCC_except_table5328
+ GCC_except_table5331
+ GCC_except_table538
+ GCC_except_table5383
+ GCC_except_table5389
+ GCC_except_table5390
+ GCC_except_table5399
+ GCC_except_table5402
+ GCC_except_table5408
+ GCC_except_table5426
+ GCC_except_table5427
+ GCC_except_table5433
+ GCC_except_table5434
+ GCC_except_table5435
+ GCC_except_table5442
+ GCC_except_table545
+ GCC_except_table5451
+ GCC_except_table5454
+ GCC_except_table5458
+ GCC_except_table546
+ GCC_except_table5533
+ GCC_except_table5534
+ GCC_except_table5646
+ GCC_except_table5647
+ GCC_except_table5648
+ GCC_except_table5649
+ GCC_except_table5650
+ GCC_except_table5651
+ GCC_except_table5652
+ GCC_except_table5666
+ GCC_except_table5667
+ GCC_except_table5668
+ GCC_except_table5694
+ GCC_except_table5771
+ GCC_except_table5772
+ GCC_except_table5773
+ GCC_except_table5774
+ GCC_except_table634
+ GCC_except_table701
+ GCC_except_table706
+ GCC_except_table755
+ GCC_except_table760
+ GCC_except_table778
+ GCC_except_table784
+ GCC_except_table785
+ GCC_except_table786
+ GCC_except_table787
+ GCC_except_table815
+ GCC_except_table848
+ GCC_except_table850
+ GCC_except_table853
+ GCC_except_table855
+ GCC_except_table896
+ GCC_except_table96
+ GCC_except_table984
+ _CCDeriveKey
+ _CCHKDFExpand
+ _CCKDFParametersCreateHkdf
+ _CCKDFParametersDestroy
+ _DERAlgorithmIdItemSpecs
+ _DERNumAlgorithmIdItemSpecs
+ _DERNumRSAKeyPairItemSpecs
+ _DERNumRSAPrivKeyCRTItemSpecs
+ _DERNumRSAPubKeyAppleItemSpecs
+ _DERNumRSAPubKeyPKCS1ItemSpecs
+ _DERNumSubjPubKeyInfoItemSpecs
+ _DERRSAKeyPairItemSpecs
+ _DERRSAPrivKeyCRTItemSpecs
+ _DERRSAPubKeyAppleItemSpecs
+ _DERRSAPubKeyPKCS1ItemSpecs
+ _DERSubjPubKeyInfoItemSpecs
+ _NEDNSProxyMapError
+ _NEFlowDirectorFetchFlowStates
+ _NEIKEv2ASN1AlgorithmIdECDSA256
+ _NEIKEv2ASN1AlgorithmIdECDSA384
+ _NEIKEv2ASN1AlgorithmIdECDSA512
+ _NEIKEv2ASN1AlgorithmIdED25519
+ _NEIKEv2ASN1AlgorithmIdED25519NonStandard
+ _NEIKEv2ASN1AlgorithmIdED448
+ _NEIKEv2ASN1AlgorithmIdRSAPKCS256
+ _NEIKEv2ASN1AlgorithmIdRSAPKCS384
+ _NEIKEv2ASN1AlgorithmIdRSAPKCS512
+ _NEIKEv2ASN1AlgorithmIdRSAPSS256
+ _NEIKEv2ASN1AlgorithmIdRSAPSS384
+ _NEIKEv2ASN1AlgorithmIdRSAPSS512
+ _NEIKEv2ASN1CheckForNULLItem
+ _NEIKEv2ASN1DecodeIntegerItem
+ _NEIKEv2ASN1RSAMGF1OID
+ _NEIKEv2ASN1RSAMGF1OIDBytes
+ _NEIKEv2ASN1RSAPSSAlgoParamItemSpecs
+ _OBJC_IVAR_$_NEIKEv2ChildSAProposal._noESNTransformPresent
+ _OBJC_IVAR_$_NEIKEv2ChildSAProposal._unsupportedTransformTypePresent
+ _OBJC_IVAR_$_NEIKEv2DeleteChildContext._reasonError
+ _OBJC_IVAR_$_NEIKEv2IKESAProposal._unsupportedTransformTypePresent
+ _OBJC_IVAR_$_NEPolicyCondition._interfaceEflags
+ _OBJC_IVAR_$_NEPolicyCondition._interfaceFlags
+ _OBJC_IVAR_$_NEPolicyCondition._interfaceXflags
+ _OBJC_IVAR_$_NEVPNConnectivityManager._usesPolicyBasedRouting
+ _OBJC_IVAR_$_NEVPNProtocol._excludeDeviceCommunication
+ ___101-[NEProviderAppConfigurationClient handleCommand:forConfigWithName:withParameters:completionHandler:]_block_invoke.154
+ ___101-[NEProviderAppConfigurationClient handleCommand:forConfigWithName:withParameters:completionHandler:]_block_invoke.189
+ ___101-[NEProviderAppConfigurationClient handleCommand:forConfigWithName:withParameters:completionHandler:]_block_invoke_2.161
+ ___101-[NEProviderAppConfigurationClient handleCommand:forConfigWithName:withParameters:completionHandler:]_block_invoke_2.193
+ ___101-[NEProviderAppConfigurationClient handleCommand:forConfigWithName:withParameters:completionHandler:]_block_invoke_3.194
+ ___114-[NEFilterDataExtensionProviderContext handleDataCompleteForFlow:direction:reply:controlSocket:completionHandler:]_block_invoke.135
+ ___41-[NEIKEv2Session removeChild:withReason:]_block_invoke
+ ___49-[NEVPNConnectivityManager refreshConfigurations]_block_invoke.51
+ ___56-[NEIKEv2Listener createListenerWithParameters:attempt:]_block_invoke.5
+ ___56-[NEIKEv2Listener createListenerWithParameters:attempt:]_block_invoke.7
+ ___75-[NEExtensionAppProxyProviderContext fetchFlowStatesWithCompletionHandler:]_block_invoke
+ ___75-[NEFilterDataExtensionProviderContext setupSocketSourceWithControlSocket:]_block_invoke.124
+ ___76-[NEFilterDataExtensionProviderContext updateFlow:withVerdict:forDirection:]_block_invoke.119
+ ___92-[NEFilterDataExtensionProviderContext handleNewFlow:reply:controlSocket:completionHandler:]_block_invoke.127
+ ___92-[NEFilterDataExtensionProviderContext handleNewFlow:reply:controlSocket:completionHandler:]_block_invoke_2.128
+ ___94-[NEUtilConfigurationClient handleCommand:forConfigWithName:withParameters:completionHandler:]_block_invoke.926
+ ___94-[NEUtilConfigurationClient handleCommand:forConfigWithName:withParameters:completionHandler:]_block_invoke.963
+ ___94-[NEUtilConfigurationClient handleCommand:forConfigWithName:withParameters:completionHandler:]_block_invoke_2.934
+ ___94-[NEUtilConfigurationClient handleCommand:forConfigWithName:withParameters:completionHandler:]_block_invoke_3.951
+ ___Block_byref_object_copy_.11463
+ ___Block_byref_object_copy_.13861
+ ___Block_byref_object_copy_.147
+ ___Block_byref_object_copy_.19770
+ ___Block_byref_object_copy_.20817
+ ___Block_byref_object_copy_.21948
+ ___Block_byref_object_copy_.221
+ ___Block_byref_object_copy_.22598
+ ___Block_byref_object_copy_.24900
+ ___Block_byref_object_copy_.6819
+ ___Block_byref_object_dispose_.11464
+ ___Block_byref_object_dispose_.13862
+ ___Block_byref_object_dispose_.148
+ ___Block_byref_object_dispose_.19771
+ ___Block_byref_object_dispose_.20818
+ ___Block_byref_object_dispose_.21949
+ ___Block_byref_object_dispose_.222
+ ___Block_byref_object_dispose_.22599
+ ___Block_byref_object_dispose_.24901
+ ___Block_byref_object_dispose_.6820
+ ___block_descriptor_144_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s_e19_"NSDictionary"8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8s128l8s136l8
+ ___block_descriptor_40_e8_32bs_e20_v16?0^{__CFArray=}8ls32l8
+ ___block_descriptor_72_e8_32s40r48r56r64r_e5_v8?0ls32l8r40l8r48l8r56l8r64l8
+ ___block_descriptor_80_e8_32s40s48s56r64r72r_e8_v12?0i8ls32l8r56l8r64l8r72l8s40l8s48l8
+ ___block_descriptor_tmp.18.23423
+ ___block_descriptor_tmp.18093
+ ___block_descriptor_tmp.21508
+ ___block_descriptor_tmp.23359
+ ___block_descriptor_tmp.23947
+ ___block_descriptor_tmp.57
+ ___block_literal_global.10.14266
+ ___block_literal_global.10.8968
+ ___block_literal_global.1126
+ ___block_literal_global.11751
+ ___block_literal_global.12.23581
+ ___block_literal_global.12123
+ ___block_literal_global.13008
+ ___block_literal_global.13171
+ ___block_literal_global.13863
+ ___block_literal_global.14.20281
+ ___block_literal_global.1410
+ ___block_literal_global.14268
+ ___block_literal_global.14819
+ ___block_literal_global.15058
+ ___block_literal_global.15546
+ ___block_literal_global.16303
+ ___block_literal_global.16437
+ ___block_literal_global.16739
+ ___block_literal_global.17.13020
+ ___block_literal_global.17.16428
+ ___block_literal_global.18019
+ ___block_literal_global.1807
+ ___block_literal_global.18668
+ ___block_literal_global.18932
+ ___block_literal_global.19867
+ ___block_literal_global.20.16434
+ ___block_literal_global.2010
+ ___block_literal_global.20286
+ ___block_literal_global.20682
+ ___block_literal_global.21435
+ ___block_literal_global.21506
+ ___block_literal_global.2154
+ ___block_literal_global.2172
+ ___block_literal_global.22048
+ ___block_literal_global.22159
+ ___block_literal_global.22193
+ ___block_literal_global.22374
+ ___block_literal_global.2272
+ ___block_literal_global.23307
+ ___block_literal_global.23357
+ ___block_literal_global.23585
+ ___block_literal_global.23674
+ ___block_literal_global.24053
+ ___block_literal_global.2433
+ ___block_literal_global.24445
+ ___block_literal_global.24618
+ ___block_literal_global.24868
+ ___block_literal_global.25397
+ ___block_literal_global.2549
+ ___block_literal_global.25966
+ ___block_literal_global.2752
+ ___block_literal_global.28.24904
+ ___block_literal_global.2894
+ ___block_literal_global.3015
+ ___block_literal_global.3107
+ ___block_literal_global.3377
+ ___block_literal_global.3655
+ ___block_literal_global.3737
+ ___block_literal_global.4.13011
+ ___block_literal_global.4154
+ ___block_literal_global.4240
+ ___block_literal_global.4601
+ ___block_literal_global.4901
+ ___block_literal_global.63
+ ___block_literal_global.63.18663
+ ___block_literal_global.63.3102
+ ___block_literal_global.63.4896
+ ___block_literal_global.66
+ ___block_literal_global.6821
+ ___block_literal_global.69
+ ___block_literal_global.69.2005
+ ___block_literal_global.69.3650
+ ___block_literal_global.69.3732
+ ___block_literal_global.7.23299
+ ___block_literal_global.7046
+ ___block_literal_global.72
+ ___block_literal_global.72.23669
+ ___block_literal_global.7232
+ ___block_literal_global.75
+ ___block_literal_global.75.4149
+ ___block_literal_global.75.4235
+ ___block_literal_global.7683
+ ___block_literal_global.77
+ ___block_literal_global.7788
+ ___block_literal_global.8966
+ __extensionAuxiliaryHostProtocol.protocol.18664
+ __extensionAuxiliaryHostProtocol.protocol.2006
+ __extensionAuxiliaryHostProtocol.protocol.22194
+ __extensionAuxiliaryHostProtocol.protocol.23670
+ __extensionAuxiliaryHostProtocol.protocol.2430
+ __extensionAuxiliaryHostProtocol.protocol.2546
+ __extensionAuxiliaryHostProtocol.protocol.2749
+ __extensionAuxiliaryHostProtocol.protocol.2891
+ __extensionAuxiliaryHostProtocol.protocol.3012
+ __extensionAuxiliaryHostProtocol.protocol.3103
+ __extensionAuxiliaryHostProtocol.protocol.3651
+ __extensionAuxiliaryHostProtocol.protocol.3733
+ __extensionAuxiliaryHostProtocol.protocol.4150
+ __extensionAuxiliaryHostProtocol.protocol.4236
+ __extensionAuxiliaryHostProtocol.protocol.4598
+ __extensionAuxiliaryHostProtocol.protocol.4897
+ __extensionAuxiliaryHostProtocol.protocolInit.18662
+ __extensionAuxiliaryHostProtocol.protocolInit.2004
+ __extensionAuxiliaryHostProtocol.protocolInit.22192
+ __extensionAuxiliaryHostProtocol.protocolInit.23668
+ __extensionAuxiliaryHostProtocol.protocolInit.2429
+ __extensionAuxiliaryHostProtocol.protocolInit.2545
+ __extensionAuxiliaryHostProtocol.protocolInit.2748
+ __extensionAuxiliaryHostProtocol.protocolInit.2890
+ __extensionAuxiliaryHostProtocol.protocolInit.3011
+ __extensionAuxiliaryHostProtocol.protocolInit.3101
+ __extensionAuxiliaryHostProtocol.protocolInit.3649
+ __extensionAuxiliaryHostProtocol.protocolInit.3731
+ __extensionAuxiliaryHostProtocol.protocolInit.4148
+ __extensionAuxiliaryHostProtocol.protocolInit.4234
+ __extensionAuxiliaryHostProtocol.protocolInit.4597
+ __extensionAuxiliaryHostProtocol.protocolInit.4895
+ __extensionAuxiliaryVendorProtocol.protocol.18669
+ __extensionAuxiliaryVendorProtocol.protocol.2011
+ __extensionAuxiliaryVendorProtocol.protocol.2173
+ __extensionAuxiliaryVendorProtocol.protocol.2273
+ __extensionAuxiliaryVendorProtocol.protocol.23675
+ __extensionAuxiliaryVendorProtocol.protocol.2434
+ __extensionAuxiliaryVendorProtocol.protocol.2550
+ __extensionAuxiliaryVendorProtocol.protocol.2753
+ __extensionAuxiliaryVendorProtocol.protocol.2895
+ __extensionAuxiliaryVendorProtocol.protocol.3016
+ __extensionAuxiliaryVendorProtocol.protocol.3108
+ __extensionAuxiliaryVendorProtocol.protocol.3656
+ __extensionAuxiliaryVendorProtocol.protocol.3738
+ __extensionAuxiliaryVendorProtocol.protocol.4155
+ __extensionAuxiliaryVendorProtocol.protocol.4241
+ __extensionAuxiliaryVendorProtocol.protocol.4602
+ __extensionAuxiliaryVendorProtocol.protocol.4902
+ __extensionAuxiliaryVendorProtocol.protocolInit.18667
+ __extensionAuxiliaryVendorProtocol.protocolInit.2009
+ __extensionAuxiliaryVendorProtocol.protocolInit.2171
+ __extensionAuxiliaryVendorProtocol.protocolInit.2271
+ __extensionAuxiliaryVendorProtocol.protocolInit.23673
+ __extensionAuxiliaryVendorProtocol.protocolInit.2432
+ __extensionAuxiliaryVendorProtocol.protocolInit.2548
+ __extensionAuxiliaryVendorProtocol.protocolInit.2751
+ __extensionAuxiliaryVendorProtocol.protocolInit.2893
+ __extensionAuxiliaryVendorProtocol.protocolInit.3014
+ __extensionAuxiliaryVendorProtocol.protocolInit.3106
+ __extensionAuxiliaryVendorProtocol.protocolInit.3654
+ __extensionAuxiliaryVendorProtocol.protocolInit.3736
+ __extensionAuxiliaryVendorProtocol.protocolInit.4153
+ __extensionAuxiliaryVendorProtocol.protocolInit.4239
+ __extensionAuxiliaryVendorProtocol.protocolInit.4600
+ __extensionAuxiliaryVendorProtocol.protocolInit.4900
+ __unnamed_array_storage.106
+ __unnamed_array_storage.19871
+ __unnamed_array_storage.20830
+ __unnamed_array_storage.219
+ __unnamed_array_storage.26673
+ _convert_error_to_string.22593
+ _createSharedSecretForRemotePublicKey:ecdhKey:dhContext:.type
+ _driverInterface.driverInterface.15547
+ _driverInterface.driverInterface.18929
+ _driverInterface.driverInterface.20282
+ _driverInterface.driverInterface.7226
+ _driverInterface.onceToken.15545
+ _driverInterface.onceToken.18928
+ _driverInterface.onceToken.20280
+ _driverInterface.onceToken.7225
+ _g_noAppFilter.25930
+ _globalConfigurationManager.gChangeQueue.16432
+ _globalConfigurationManager.gConfigurationManager.16429
+ _globalConfigurationManager.onceToken.16427
+ _initGlobals.onceToken.15057
+ _kNEExcludeDeviceCommunication
+ _loadedManagers.loadedManagers.24866
+ _loadedManagers.loadedManagers.25933
+ _loadedManagers.managers_init.24865
+ _loadedManagers.managers_init.25932
+ _managerInterface.managerInterface.18933
+ _managerInterface.managerInterface.20287
+ _managerInterface.onceToken.18931
+ _managerInterface.onceToken.20285
+ _objc_msgSend$appendPrettyHex:withName:andIndent:options:
+ _objc_msgSend$excludeDeviceCommunication
+ _objc_msgSend$ikeInterfaceName
+ _objc_msgSend$scopedInterfaceFlags:eflags:xflags:
+ _objc_msgSend$setExcludeDeviceCommunication:
+ _objc_msgSend$setUsesPolicyBasedRouting:
+ _objc_msgSend$usesPolicyBasedRouting
+ _sharedManager.g_manager.7047
+ _sharedManager.g_manager.7684
+ _sharedManager.init_manager.7045
+ _sharedManager.init_manager.7682
+ _sharedManager.onceToken.16436
+ _sharedManager.onceToken.25965
- +[NEIKEv2Crypto createPRFPlusFromData:key:prfAlgorithm:outputLength:]
- -[NEIKEv2AuthenticationProtocol isPKCS]
- -[NEIKEv2ChildSA responderSendIntegrityKey]
- -[NEIKEv2ChildSA setResponderSendIntegrityKey:]
- -[NEIKEv2ChildSAProposal matchesProposal:checkDHGroup:]
- -[NEIKEv2DHKeys createSharedSecretForRemotePublicKey:publicKeySize:ecdhKey:dhContext:]
- -[NEIKEv2IKESAProposal matchesProposal:]
- GCC_except_table101
- GCC_except_table1034
- GCC_except_table1035
- GCC_except_table1040
- GCC_except_table1041
- GCC_except_table109
- GCC_except_table1192
- GCC_except_table1193
- GCC_except_table1198
- GCC_except_table1199
- GCC_except_table1208
- GCC_except_table1213
- GCC_except_table1214
- GCC_except_table1227
- GCC_except_table1238
- GCC_except_table1239
- GCC_except_table127
- GCC_except_table1364
- GCC_except_table145
- GCC_except_table1489
- GCC_except_table1490
- GCC_except_table1495
- GCC_except_table1498
- GCC_except_table1543
- GCC_except_table1544
- GCC_except_table1545
- GCC_except_table1546
- GCC_except_table1560
- GCC_except_table1571
- GCC_except_table1572
- GCC_except_table1579
- GCC_except_table1585
- GCC_except_table1605
- GCC_except_table1631
- GCC_except_table2336
- GCC_except_table246
- GCC_except_table3048
- GCC_except_table3059
- GCC_except_table3072
- GCC_except_table3073
- GCC_except_table3091
- GCC_except_table3132
- GCC_except_table3138
- GCC_except_table3170
- GCC_except_table3173
- GCC_except_table3258
- GCC_except_table3280
- GCC_except_table3515
- GCC_except_table3521
- GCC_except_table3522
- GCC_except_table3609
- GCC_except_table367
- GCC_except_table3753
- GCC_except_table3764
- GCC_except_table3770
- GCC_except_table3785
- GCC_except_table3786
- GCC_except_table3787
- GCC_except_table3788
- GCC_except_table3802
- GCC_except_table3803
- GCC_except_table3809
- GCC_except_table3816
- GCC_except_table3817
- GCC_except_table3889
- GCC_except_table3890
- GCC_except_table3898
- GCC_except_table3991
- GCC_except_table3992
- GCC_except_table3993
- GCC_except_table3994
- GCC_except_table4078
- GCC_except_table4245
- GCC_except_table4255
- GCC_except_table4271
- GCC_except_table4291
- GCC_except_table4293
- GCC_except_table4299
- GCC_except_table4301
- GCC_except_table436
- GCC_except_table4389
- GCC_except_table4456
- GCC_except_table4477
- GCC_except_table4490
- GCC_except_table4587
- GCC_except_table4633
- GCC_except_table4679
- GCC_except_table4681
- GCC_except_table4777
- GCC_except_table4797
- GCC_except_table4799
- GCC_except_table4801
- GCC_except_table4808
- GCC_except_table4847
- GCC_except_table4848
- GCC_except_table4850
- GCC_except_table4897
- GCC_except_table4918
- GCC_except_table4921
- GCC_except_table4991
- GCC_except_table511
- GCC_except_table512
- GCC_except_table522
- GCC_except_table527
- GCC_except_table528
- GCC_except_table5310
- GCC_except_table5322
- GCC_except_table5323
- GCC_except_table5326
- GCC_except_table535
- GCC_except_table5378
- GCC_except_table5384
- GCC_except_table5385
- GCC_except_table5394
- GCC_except_table5397
- GCC_except_table5403
- GCC_except_table5418
- GCC_except_table5419
- GCC_except_table542
- GCC_except_table5420
- GCC_except_table5421
- GCC_except_table5422
- GCC_except_table543
- GCC_except_table5437
- GCC_except_table5446
- GCC_except_table5449
- GCC_except_table5453
- GCC_except_table5526
- GCC_except_table5527
- GCC_except_table5633
- GCC_except_table5634
- GCC_except_table5635
- GCC_except_table5636
- GCC_except_table5637
- GCC_except_table5638
- GCC_except_table5639
- GCC_except_table5654
- GCC_except_table5659
- GCC_except_table5660
- GCC_except_table5687
- GCC_except_table5764
- GCC_except_table5765
- GCC_except_table5766
- GCC_except_table5767
- GCC_except_table631
- GCC_except_table697
- GCC_except_table702
- GCC_except_table751
- GCC_except_table756
- GCC_except_table774
- GCC_except_table780
- GCC_except_table781
- GCC_except_table782
- GCC_except_table783
- GCC_except_table811
- GCC_except_table842
- GCC_except_table843
- GCC_except_table844
- GCC_except_table845
- GCC_except_table892
- GCC_except_table95
- GCC_except_table980
- _DERContentLengthOfEncodedSequence
- _DEREncodeItem
- _DEREncodeItemSized
- _DEREncodeLength
- _DEREncodeLengthSized
- _DEREncodeSequence
- _DEREncodeSequenceFromObject
- _DEREncodeTag
- _DERLengthOfEncodedSequence
- _DERLengthOfEncodedSequenceFromObject
- _DERLengthOfItem
- _DERLengthOfLength
- _NEIKEv2CheckForNULLDERItem
- _NEIKEv2DERAlgorithmIdItemSpecs
- _NEIKEv2DERNumAlgorithmIdItemSpecs
- _NEIKEv2DecodeIntegerDERItem
- _NEIKEv2DigitalSignatureOIDED25519NonStandard
- _NEIKEv2EncodeAlgorithmId
- _NEIKEv2RSAPSSAlgorithmParametersItemSpecs
- _NEIKEv2RSAPSSIDMGF1OID
- _NEIKEv2RSAPSSIDMGF1OIDBytes
- _OBJC_IVAR_$_NEIKEv2ChildSA._dhPublicKeySize
- _OBJC_IVAR_$_NEIKEv2DHKeys._publicKeySize
- _OBJC_IVAR_$_NEIKEv2IKESA._dhPublicKeySize
- _OBJC_IVAR_$_NEIKEv2IKESA._sKeySeed
- ___101-[NEProviderAppConfigurationClient handleCommand:forConfigWithName:withParameters:completionHandler:]_block_invoke.153
- ___101-[NEProviderAppConfigurationClient handleCommand:forConfigWithName:withParameters:completionHandler:]_block_invoke.188
- ___101-[NEProviderAppConfigurationClient handleCommand:forConfigWithName:withParameters:completionHandler:]_block_invoke_2.160
- ___101-[NEProviderAppConfigurationClient handleCommand:forConfigWithName:withParameters:completionHandler:]_block_invoke_2.192
- ___101-[NEProviderAppConfigurationClient handleCommand:forConfigWithName:withParameters:completionHandler:]_block_invoke_3.193
- ___114-[NEFilterDataExtensionProviderContext handleDataCompleteForFlow:direction:reply:controlSocket:completionHandler:]_block_invoke.134
- ___30-[NEIKEv2Session removeChild:]_block_invoke
- ___49-[NEVPNConnectivityManager refreshConfigurations]_block_invoke.49
- ___56-[NEIKEv2Listener createListenerWithParameters:attempt:]_block_invoke.6
- ___56-[NEIKEv2Listener createListenerWithParameters:attempt:]_block_invoke.8
- ___75-[NEFilterDataExtensionProviderContext setupSocketSourceWithControlSocket:]_block_invoke.123
- ___76-[NEFilterDataExtensionProviderContext updateFlow:withVerdict:forDirection:]_block_invoke.118
- ___92-[NEFilterDataExtensionProviderContext handleNewFlow:reply:controlSocket:completionHandler:]_block_invoke.126
- ___92-[NEFilterDataExtensionProviderContext handleNewFlow:reply:controlSocket:completionHandler:]_block_invoke_2.127
- ___94-[NEUtilConfigurationClient handleCommand:forConfigWithName:withParameters:completionHandler:]_block_invoke.920
- ___94-[NEUtilConfigurationClient handleCommand:forConfigWithName:withParameters:completionHandler:]_block_invoke.957
- ___94-[NEUtilConfigurationClient handleCommand:forConfigWithName:withParameters:completionHandler:]_block_invoke_2.928
- ___94-[NEUtilConfigurationClient handleCommand:forConfigWithName:withParameters:completionHandler:]_block_invoke_3.945
- ___Block_byref_object_copy_.11491
- ___Block_byref_object_copy_.13887
- ___Block_byref_object_copy_.141
- ___Block_byref_object_copy_.19874
- ___Block_byref_object_copy_.20909
- ___Block_byref_object_copy_.218
- ___Block_byref_object_copy_.22041
- ___Block_byref_object_copy_.22687
- ___Block_byref_object_copy_.24980
- ___Block_byref_object_copy_.6822
- ___Block_byref_object_dispose_.11492
- ___Block_byref_object_dispose_.13888
- ___Block_byref_object_dispose_.142
- ___Block_byref_object_dispose_.19875
- ___Block_byref_object_dispose_.20910
- ___Block_byref_object_dispose_.219
- ___Block_byref_object_dispose_.22042
- ___Block_byref_object_dispose_.22688
- ___Block_byref_object_dispose_.24981
- ___Block_byref_object_dispose_.6823
- ___block_descriptor_128_e8_32s40s48s56s64s72s80s88s96s104s112s120s_e19_"NSDictionary"8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8
- ___block_descriptor_64_e8_32s40r48r56r_e5_v8?0ls32l8r40l8r48l8r56l8
- ___block_descriptor_72_e8_32s40s48s56r64r_e8_v12?0i8ls32l8r56l8r64l8s40l8s48l8
- ___block_descriptor_tmp.18.23504
- ___block_descriptor_tmp.18110
- ___block_descriptor_tmp.21602
- ___block_descriptor_tmp.23440
- ___block_descriptor_tmp.24029
- ___block_descriptor_tmp.54
- ___block_literal_global.10.14282
- ___block_literal_global.10.8989
- ___block_literal_global.1147
- ___block_literal_global.11782
- ___block_literal_global.12.23662
- ___block_literal_global.12152
- ___block_literal_global.13040
- ___block_literal_global.13203
- ___block_literal_global.13889
- ___block_literal_global.14.20384
- ___block_literal_global.1424
- ___block_literal_global.14284
- ___block_literal_global.14850
- ___block_literal_global.15089
- ___block_literal_global.15572
- ___block_literal_global.16323
- ___block_literal_global.16458
- ___block_literal_global.16761
- ___block_literal_global.17.13052
- ___block_literal_global.17.16449
- ___block_literal_global.18036
- ___block_literal_global.1822
- ___block_literal_global.18673
- ___block_literal_global.18936
- ___block_literal_global.19971
- ___block_literal_global.20.16455
- ___block_literal_global.2020
- ___block_literal_global.20389
- ___block_literal_global.20784
- ___block_literal_global.21529
- ___block_literal_global.21600
- ___block_literal_global.2163
- ___block_literal_global.2181
- ___block_literal_global.22142
- ___block_literal_global.22253
- ___block_literal_global.22287
- ___block_literal_global.22467
- ___block_literal_global.2280
- ___block_literal_global.23385
- ___block_literal_global.23438
- ___block_literal_global.23666
- ___block_literal_global.23754
- ___block_literal_global.24135
- ___block_literal_global.2437
- ___block_literal_global.24526
- ___block_literal_global.24698
- ___block_literal_global.24948
- ___block_literal_global.25469
- ___block_literal_global.2552
- ___block_literal_global.26034
- ___block_literal_global.2754
- ___block_literal_global.28.24984
- ___block_literal_global.2899
- ___block_literal_global.3020
- ___block_literal_global.3113
- ___block_literal_global.3380
- ___block_literal_global.3656
- ___block_literal_global.3738
- ___block_literal_global.4.13043
- ___block_literal_global.4160
- ___block_literal_global.4246
- ___block_literal_global.4606
- ___block_literal_global.4903
- ___block_literal_global.61
- ___block_literal_global.62.18668
- ___block_literal_global.62.3108
- ___block_literal_global.62.4898
- ___block_literal_global.65.23922
- ___block_literal_global.68
- ___block_literal_global.68.2015
- ___block_literal_global.68.3651
- ___block_literal_global.68.3733
- ___block_literal_global.6824
- ___block_literal_global.7.23376
- ___block_literal_global.70
- ___block_literal_global.7043
- ___block_literal_global.71.23749
- ___block_literal_global.7228
- ___block_literal_global.74
- ___block_literal_global.74.4155
- ___block_literal_global.74.4241
- ___block_literal_global.76
- ___block_literal_global.7670
- ___block_literal_global.7775
- ___block_literal_global.8987
- __extensionAuxiliaryHostProtocol.protocol.18669
- __extensionAuxiliaryHostProtocol.protocol.2016
- __extensionAuxiliaryHostProtocol.protocol.22288
- __extensionAuxiliaryHostProtocol.protocol.23750
- __extensionAuxiliaryHostProtocol.protocol.2434
- __extensionAuxiliaryHostProtocol.protocol.2549
- __extensionAuxiliaryHostProtocol.protocol.2751
- __extensionAuxiliaryHostProtocol.protocol.2896
- __extensionAuxiliaryHostProtocol.protocol.3017
- __extensionAuxiliaryHostProtocol.protocol.3109
- __extensionAuxiliaryHostProtocol.protocol.3652
- __extensionAuxiliaryHostProtocol.protocol.3734
- __extensionAuxiliaryHostProtocol.protocol.4156
- __extensionAuxiliaryHostProtocol.protocol.4242
- __extensionAuxiliaryHostProtocol.protocol.4603
- __extensionAuxiliaryHostProtocol.protocol.4899
- __extensionAuxiliaryHostProtocol.protocolInit.18667
- __extensionAuxiliaryHostProtocol.protocolInit.2014
- __extensionAuxiliaryHostProtocol.protocolInit.22286
- __extensionAuxiliaryHostProtocol.protocolInit.23748
- __extensionAuxiliaryHostProtocol.protocolInit.2433
- __extensionAuxiliaryHostProtocol.protocolInit.2548
- __extensionAuxiliaryHostProtocol.protocolInit.2750
- __extensionAuxiliaryHostProtocol.protocolInit.2895
- __extensionAuxiliaryHostProtocol.protocolInit.3016
- __extensionAuxiliaryHostProtocol.protocolInit.3107
- __extensionAuxiliaryHostProtocol.protocolInit.3650
- __extensionAuxiliaryHostProtocol.protocolInit.3732
- __extensionAuxiliaryHostProtocol.protocolInit.4154
- __extensionAuxiliaryHostProtocol.protocolInit.4240
- __extensionAuxiliaryHostProtocol.protocolInit.4602
- __extensionAuxiliaryHostProtocol.protocolInit.4897
- __extensionAuxiliaryVendorProtocol.protocol.18674
- __extensionAuxiliaryVendorProtocol.protocol.2021
- __extensionAuxiliaryVendorProtocol.protocol.2182
- __extensionAuxiliaryVendorProtocol.protocol.2281
- __extensionAuxiliaryVendorProtocol.protocol.23755
- __extensionAuxiliaryVendorProtocol.protocol.2438
- __extensionAuxiliaryVendorProtocol.protocol.2553
- __extensionAuxiliaryVendorProtocol.protocol.2755
- __extensionAuxiliaryVendorProtocol.protocol.2900
- __extensionAuxiliaryVendorProtocol.protocol.3021
- __extensionAuxiliaryVendorProtocol.protocol.3114
- __extensionAuxiliaryVendorProtocol.protocol.3657
- __extensionAuxiliaryVendorProtocol.protocol.3739
- __extensionAuxiliaryVendorProtocol.protocol.4161
- __extensionAuxiliaryVendorProtocol.protocol.4247
- __extensionAuxiliaryVendorProtocol.protocol.4607
- __extensionAuxiliaryVendorProtocol.protocol.4904
- __extensionAuxiliaryVendorProtocol.protocolInit.18672
- __extensionAuxiliaryVendorProtocol.protocolInit.2019
- __extensionAuxiliaryVendorProtocol.protocolInit.2180
- __extensionAuxiliaryVendorProtocol.protocolInit.2279
- __extensionAuxiliaryVendorProtocol.protocolInit.23753
- __extensionAuxiliaryVendorProtocol.protocolInit.2436
- __extensionAuxiliaryVendorProtocol.protocolInit.2551
- __extensionAuxiliaryVendorProtocol.protocolInit.2753
- __extensionAuxiliaryVendorProtocol.protocolInit.2898
- __extensionAuxiliaryVendorProtocol.protocolInit.3019
- __extensionAuxiliaryVendorProtocol.protocolInit.3112
- __extensionAuxiliaryVendorProtocol.protocolInit.3655
- __extensionAuxiliaryVendorProtocol.protocolInit.3737
- __extensionAuxiliaryVendorProtocol.protocolInit.4159
- __extensionAuxiliaryVendorProtocol.protocolInit.4245
- __extensionAuxiliaryVendorProtocol.protocolInit.4605
- __extensionAuxiliaryVendorProtocol.protocolInit.4902
- __unnamed_array_storage.19975
- __unnamed_array_storage.20923
- __unnamed_array_storage.218
- __unnamed_array_storage.26742
- _convert_error_to_string.22684
- _copyDigitalSignatureAlgorithmIdentifierForAuth:.NEIKEv2ASN1NullPayload
- _createSharedSecretForRemotePublicKey:publicKeySize:ecdhKey:dhContext:.type
- _driverInterface.driverInterface.15573
- _driverInterface.driverInterface.18933
- _driverInterface.driverInterface.20385
- _driverInterface.driverInterface.7222
- _driverInterface.onceToken.15571
- _driverInterface.onceToken.18932
- _driverInterface.onceToken.20383
- _driverInterface.onceToken.7221
- _g_noAppFilter.25997
- _globalConfigurationManager.gChangeQueue.16453
- _globalConfigurationManager.gConfigurationManager.16450
- _globalConfigurationManager.onceToken.16448
- _initGlobals.onceToken.15088
- _loadedManagers.loadedManagers.24946
- _loadedManagers.loadedManagers.26000
- _loadedManagers.managers_init.24945
- _loadedManagers.managers_init.25999
- _managerInterface.managerInterface.18937
- _managerInterface.managerInterface.20390
- _managerInterface.onceToken.18935
- _managerInterface.onceToken.20388
- _objc_msgSend$resetBytesInRange:
- _sharedManager.g_manager.7044
- _sharedManager.g_manager.7671
- _sharedManager.init_manager.7042
- _sharedManager.init_manager.7669
- _sharedManager.onceToken.16457
- _sharedManager.onceToken.26033
CStrings:
+ "\n%*s%@ = %llX"
+ "%@: stopping tunnel since Child disconnected %@"
+ "%s called with null localProposal"
+ "%s called with null localProposal.dhProtocols"
+ "%s called with null localProposal.encryptionProtocols"
+ "%s called with null localProposal.prfProtocols"
+ "%s called with null rekey.skD"
+ "-[NEIKEv2ChildSAProposal matchesLocalProposal:checkDHGroup:]"
+ "-[NEIKEv2DHKeys createSharedSecretForRemotePublicKey:ecdhKey:dhContext:]"
+ "-[NEIKEv2IKESA(Crypto) generateAllValuesForRekey:]"
+ "-[NEIKEv2IKESAProposal matchesLocalProposal:]"
+ "2\x17\x12\x12\x1f\x02\x12\x1f\x03\x11"
+ "AppleConnect IKEv2 Client"
+ "BoundInterfaceFlags"
+ "CCDeriveKey failed %d"
+ "CCHKDFExpand failed %d"
+ "CCKDFParametersCreateHkdf failed %d"
+ "Calculated sKeySeed derivatives"
+ "Compute MODP DH %zu result"
+ "Computed MODP DH %zu result"
+ "DeviceCommunication"
+ "ExcludeDeviceCommunication"
+ "Failed to compute MODP DH %zu value: %d"
+ "Failed to create MODP DH %zu context: %d"
+ "Failed to generate MODP DH %zu key pair: %d"
+ "Found unsupported transform type %u in Child SA proposal"
+ "Found unsupported transform type %u in IKE SA proposal"
+ "G\x12\x1a"
+ "Generated MODP DH %zu key"
+ "IdleTimeout"
+ "Ignoring ESN transform found in IKE SA proposal"
+ "Incorrect RSA-PSS MaskGenAlgorithm.OID"
+ "InterfaceEflags"
+ "InterfaceFlags"
+ "InterfaceXflags"
+ "LocalNonceSize"
+ "Max MODP DH %zu key length (%zu) is greater than prime length (%zu)"
+ "Not matching proposal missing No ESN transform"
+ "Not matching proposal with unsupported transform type"
+ "Peer MODP DH %zu key length (%zu) is not equal to prime length (%zu)"
+ "RemoteNonceSize"
+ "Service must be: AirPlay, AirPrint, AirDrop, VoiceMail, CellularServices or DeviceCommunication"
+ "T@\"NSString\",?,R,C"
+ "TB,?,N"
+ "TB,?,N,GisNetworkProvider"
+ "TB,?,N,GisNexusProvider"
+ "TB,?,N,GisNexusProvider,VnexusProvider"
+ "TB,?,N,GisSpecificUseOnly"
+ "TB,?,N,VsupportsBrowseRequests"
+ "TB,N,V_usesPolicyBasedRouting"
+ "TB,V_excludeDeviceCommunication"
+ "Unexpected non-NULL HashAlgorithm parameters"
+ "Unexpected non-NULL RSA-PSS MaskGenAlgorithm.HashAlgorithm parameters"
+ "VPN connectivity state is now %@, visibility state is now %ld%{public}s, %s policy-based routing"
+ "_excludeDeviceCommunication"
+ "_interfaceEflags"
+ "_interfaceFlags"
+ "_interfaceXflags"
+ "_noESNTransformPresent"
+ "_reasonError"
+ "_unsupportedTransformTypePresent"
+ "_usesPolicyBasedRouting"
+ "appendPrettyHex:withName:andIndent:options:"
+ "delete child with id %u, reason %@"
+ "does not use"
+ "eflags"
+ "exclude-device-communication"
+ "excludeDeviceCommunication"
+ "fetchFlowStatesWithCompletionHandler:"
+ "flags"
+ "scoped-interface-flags"
+ "scoped-interface-flags: %X, eflags %X, xflags %X"
+ "scopedInterfaceFlags:eflags:xflags:"
+ "setExcludeDeviceCommunication:"
+ "setUsesPolicyBasedRouting:"
+ "uses"
+ "usesPolicyBasedRouting"
+ "v16@?0^{__CFArray=}8"
+ "\x9b"
+ "\xf0\xf0q\xf0a\x12"
- "%@: stopping tunnel since Child disconnected %ld"
- "%s called with null authData"
- "%s called with null proposal.dhProtocols"
- "%s called with null proposal.encryptionProtocols"
- "%s called with null proposal.prfProtocols"
- "%s called with null self.sKeySeed"
- "+[NEIKEv2Crypto createPRFPlusFromData:key:prfAlgorithm:outputLength:]"
- "-[NEIKEv2ChildSAProposal matchesProposal:checkDHGroup:]"
- "-[NEIKEv2DHKeys createSharedSecretForRemotePublicKey:publicKeySize:ecdhKey:dhContext:]"
- "-[NEIKEv2IKESA(Crypto) calculateSKEYSEEDDerivativesForRekey:]"
- "-[NEIKEv2IKESA(Crypto) calculateSKEYSEEDForRekey:]"
- "-[NEIKEv2IKESAProposal matchesProposal:]"
- "2\x17\x12\x12/\x03\x12\x1f\x03\x11"
- "Compute MODP DH result"
- "Connectivity state is now %@, visibility state is now %ld%{public}s"
- "Failed DH public key size check"
- "Failed to calculate ASN.1 payload size, error %d"
- "Failed to calculate parameters payload size for authentication protocol %@, error %d"
- "Failed to compute DH value: %d"
- "Failed to create DH context: %d"
- "Failed to encode ASN.1 payload, error %d"
- "Failed to encode HashAlgorithm for authentication protocol %@"
- "Failed to encode MaskGenAlgorithm for authentication protocol %@"
- "Failed to encode algorithm identifier for authentication protocol %@"
- "Failed to encode parameters payload for authentication protocol %@, error %d"
- "Failed to generate DH key pair: %d"
- "G\x12*"
- "Generated MODP key len %zu"
- "Incorrect RSA-PSS MaskGenAlgorithm.OID, error %d"
- "Invalid public DH information was generated"
- "Service must be: AirPlay, AirPrint, AirDrop, VoiceMail, or CellularServices"
- "TB,N,GisNetworkProvider"
- "TB,N,GisNexusProvider"
- "TB,N,GisNexusProvider,VnexusProvider"
- "TB,N,GisSpecificUseOnly"
- "TB,N,VsupportsBrowseRequests"
- "Unexpected non-NULL HashAlgorithm parameters, error %d"
- "Unexpected non-NULL RSA-PSS MaskGenAlgorithm.HashAlgorithm parameters, error %d"
- "[NEIKEv2Crypto createPRFPlusFromData:] failed"
- "[NESensitiveData mutableSensitiveDataWithMaxCapacity:%u] failed"
- "_dhPublicKeySize"
- "_publicKeySize"
- "_sKeySeed"
- "calculated sKeySeed derivatives"
- "delete child with id %u"
- "derivatives.length != totalDerivativesLength"
- "derivatives.length(%zu) != totalDerivativesLength(%u)"
- "resetBytesInRange:"
- "sKeySeed is nil"
- "\x8b"
- "\xf0\xf0\x91\xf0a\x12"

```
