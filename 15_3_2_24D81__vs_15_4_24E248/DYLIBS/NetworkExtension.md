## NetworkExtension

> `/System/Library/Frameworks/NetworkExtension.framework/Versions/A/NetworkExtension`

```diff

-2063.80.10.0.0
-  __TEXT.__text: 0x1eca9c
-  __TEXT.__auth_stubs: 0x3c10
-  __TEXT.__objc_methlist: 0xd63c
-  __TEXT.__cstring: 0x1788f
+2063.101.3.0.0
+  __TEXT.__text: 0x1ed9ac
+  __TEXT.__auth_stubs: 0x3be0
+  __TEXT.__objc_methlist: 0xe61c
+  __TEXT.__const: 0x2478
+  __TEXT.__cstring: 0x17a2b
   __TEXT.__swift5_typeref: 0x332
-  __TEXT.__const: 0x2428
   __TEXT.__constg_swiftt: 0x540
   __TEXT.__swift5_reflstr: 0xa4
   __TEXT.__swift5_fieldmd: 0x228

   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_types: 0x48
   __TEXT.__swift5_capture: 0x140
+  __TEXT.__swift_as_entry: 0xc
+  __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__gcc_except_tab: 0x54cc
-  __TEXT.__oslogstring: 0x2157c
-  __TEXT.__unwind_info: 0x4530
+  __TEXT.__gcc_except_tab: 0x5570
+  __TEXT.__oslogstring: 0x216b3
+  __TEXT.__unwind_info: 0x4480
   __TEXT.__eh_frame: 0x598
-  __TEXT.__objc_classname: 0x23b7
-  __TEXT.__objc_methname: 0x19382
-  __TEXT.__objc_methtype: 0x3677
-  __TEXT.__objc_stubs: 0xf800
-  __DATA_CONST.__got: 0x1578
-  __DATA_CONST.__const: 0x2e58
-  __DATA_CONST.__objc_classlist: 0xa58
+  __TEXT.__objc_classname: 0x23dc
+  __TEXT.__objc_methname: 0x195ed
+  __TEXT.__objc_methtype: 0x366c
+  __TEXT.__objc_stubs: 0xf900
+  __DATA_CONST.__got: 0x1568
+  __DATA_CONST.__const: 0x2f90
+  __DATA_CONST.__objc_classlist: 0xa60
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x200
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4ca0
+  __DATA_CONST.__objc_selrefs: 0x4dd0
   __DATA_CONST.__objc_protorefs: 0x108
-  __DATA_CONST.__objc_superrefs: 0x6e8
+  __DATA_CONST.__objc_superrefs: 0x6f0
   __DATA_CONST.__objc_arraydata: 0x128
-  __AUTH_CONST.__auth_got: 0x1e18
+  __AUTH_CONST.__auth_got: 0x1e00
   __AUTH_CONST.__const: 0x43e8
-  __AUTH_CONST.__cfstring: 0x171e0
-  __AUTH_CONST.__objc_const: 0x21ff0
+  __AUTH_CONST.__cfstring: 0x17320
+  __AUTH_CONST.__objc_const: 0x20760
   __AUTH_CONST.__objc_intobj: 0x3c0
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x6de0
+  __AUTH.__objc_data: 0x6e30
   __AUTH.__data: 0x1d8
-  __DATA.__objc_ivar: 0x1a50
+  __DATA.__objc_ivar: 0x1a60
   __DATA.__data: 0x1a50
-  __DATA.__common: 0x198
   __DATA.__bss: 0xbc0
+  __DATA.__common: 0x198
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/CryptoKit.framework/Versions/A/CryptoKit

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 9B05C4CB-F9B2-3C39-98A7-A3B74AAF688B
-  Functions: 6682
-  Symbols:   15682
-  CStrings:  15101
+  UUID: F913842A-2104-3357-ABCE-CC66C2789445
+  Functions: 6643
+  Symbols:   15768
+  CStrings:  15156
 
Symbols:
+ +[NEIKEv2Crypto createHMACFromDataVector:key:prfProtocol:]
+ +[NEIKEv2IKESA createAuthenticationDataForSharedSecret:octetVector:prfProtocol:]
+ +[NERelayConfiguration fqdnOverlap:otherRelay:]
+ -[NEIKEv2GSPM createLocalSignedOctetVector]
+ -[NEIKEv2GSPM createRemoteSignedOctetVector]
+ -[NEIKEv2IKESA clearPostAuthenticationData]
+ -[NEIKEv2IKESA createAuthenticationDataForSharedSecret:octetVector:]
+ -[NEIKEv2IKESA createInitiatorSignedOctetVectorUsingPrimeKey:]
+ -[NEIKEv2IKESA createIntAuthOctetVector]
+ -[NEIKEv2IKESA createLocalSignedOctetVectorUsingPrimeKey:]
+ -[NEIKEv2IKESA createRemoteSignedOctetVectorUsingPrimeKey:]
+ -[NEIKEv2IKESA createResponderSignedOctetVectorUsingPrimeKey:]
+ -[NEIKEv2IntegrityProtocol macLength]
+ -[NEIKEv2IntermediatePacket authenticatedDataVector]
+ -[NEIKEv2PRFProtocol ccHMAC]
+ -[NEIKEv2SecurityContextCBCPlusHMAC checkIncomingHMACForPayloadData:authenticatedHeaders:]
+ -[NENetworkAgentSessionFileHandle .cxx_destruct]
+ -[NENetworkAgentSessionFileHandle description]
+ -[NENetworkAgentSessionFileHandle initWithNetworkAgentSession:]
+ -[NENetworkAgentSessionFileHandle initWithNetworkAgentSession:name:]
+ -[NENetworkAgentSessionFileHandle name]
+ -[NENetworkAgentSessionFileHandle type]
+ -[NERelayConfiguration excludedFQDNs]
+ -[NERelayConfiguration internalExcludedDomains]
+ -[NERelayConfiguration internalMatchDomains]
+ -[NERelayConfiguration isUIToggleEnabled]
+ -[NERelayConfiguration matchFQDNs]
+ -[NERelayConfiguration onDemandRules:overlapWithOtherRules:]
+ -[NERelayConfiguration setExcludedFQDNs:]
+ -[NERelayConfiguration setInternalExcludedDomains:]
+ -[NERelayConfiguration setInternalMatchDomains:]
+ -[NERelayConfiguration setMatchFQDNs:]
+ -[NERelayConfiguration setUiToggleEnabled:]
+ -[NERelayManager excludedFQDNs]
+ -[NERelayManager isUIToggleEnabled]
+ -[NERelayManager matchFQDNs]
+ -[NERelayManager setExcludedFQDNs:]
+ -[NERelayManager setMatchFQDNs:]
+ -[NERelayManager setUIToggleEnabled:]
+ GCC_except_table1058
+ GCC_except_table1120
+ GCC_except_table1121
+ GCC_except_table1122
+ GCC_except_table1295
+ GCC_except_table1296
+ GCC_except_table1297
+ GCC_except_table1298
+ GCC_except_table1299
+ GCC_except_table1311
+ GCC_except_table1312
+ GCC_except_table1325
+ GCC_except_table1336
+ GCC_except_table1337
+ GCC_except_table1465
+ GCC_except_table1591
+ GCC_except_table1596
+ GCC_except_table1599
+ GCC_except_table1658
+ GCC_except_table1659
+ GCC_except_table1660
+ GCC_except_table1661
+ GCC_except_table1663
+ GCC_except_table1668
+ GCC_except_table1672
+ GCC_except_table1675
+ GCC_except_table1683
+ GCC_except_table1684
+ GCC_except_table1691
+ GCC_except_table1721
+ GCC_except_table1749
+ GCC_except_table2801
+ GCC_except_table2811
+ GCC_except_table3050
+ GCC_except_table3055
+ GCC_except_table3061
+ GCC_except_table3064
+ GCC_except_table3081
+ GCC_except_table3082
+ GCC_except_table3083
+ GCC_except_table3097
+ GCC_except_table3107
+ GCC_except_table3108
+ GCC_except_table3191
+ GCC_except_table3239
+ GCC_except_table3289
+ GCC_except_table3303
+ GCC_except_table3312
+ GCC_except_table3314
+ GCC_except_table3331
+ GCC_except_table3332
+ GCC_except_table3333
+ GCC_except_table3349
+ GCC_except_table3391
+ GCC_except_table3399
+ GCC_except_table3401
+ GCC_except_table3436
+ GCC_except_table3438
+ GCC_except_table3439
+ GCC_except_table3530
+ GCC_except_table3554
+ GCC_except_table3793
+ GCC_except_table3818
+ GCC_except_table3819
+ GCC_except_table3820
+ GCC_except_table3821
+ GCC_except_table3823
+ GCC_except_table3906
+ GCC_except_table3966
+ GCC_except_table3973
+ GCC_except_table4110
+ GCC_except_table4111
+ GCC_except_table4112
+ GCC_except_table4114
+ GCC_except_table4115
+ GCC_except_table4116
+ GCC_except_table4117
+ GCC_except_table4118
+ GCC_except_table4122
+ GCC_except_table4127
+ GCC_except_table4128
+ GCC_except_table4134
+ GCC_except_table4141
+ GCC_except_table4142
+ GCC_except_table4214
+ GCC_except_table4215
+ GCC_except_table4223
+ GCC_except_table4317
+ GCC_except_table4318
+ GCC_except_table4319
+ GCC_except_table4320
+ GCC_except_table4321
+ GCC_except_table4322
+ GCC_except_table4324
+ GCC_except_table4405
+ GCC_except_table4575
+ GCC_except_table4585
+ GCC_except_table4589
+ GCC_except_table4602
+ GCC_except_table4622
+ GCC_except_table4624
+ GCC_except_table4630
+ GCC_except_table4632
+ GCC_except_table4726
+ GCC_except_table4795
+ GCC_except_table4815
+ GCC_except_table4829
+ GCC_except_table4927
+ GCC_except_table4932
+ GCC_except_table4976
+ GCC_except_table5022
+ GCC_except_table5024
+ GCC_except_table5086
+ GCC_except_table5089
+ GCC_except_table5127
+ GCC_except_table5147
+ GCC_except_table5149
+ GCC_except_table5151
+ GCC_except_table5162
+ GCC_except_table5201
+ GCC_except_table5202
+ GCC_except_table5204
+ GCC_except_table5206
+ GCC_except_table5209
+ GCC_except_table5274
+ GCC_except_table5277
+ GCC_except_table5349
+ GCC_except_table5675
+ GCC_except_table5689
+ GCC_except_table5690
+ GCC_except_table5693
+ GCC_except_table5746
+ GCC_except_table5752
+ GCC_except_table5753
+ GCC_except_table5762
+ GCC_except_table5771
+ GCC_except_table5786
+ GCC_except_table5787
+ GCC_except_table5788
+ GCC_except_table5789
+ GCC_except_table5790
+ GCC_except_table5791
+ GCC_except_table5793
+ GCC_except_table5796
+ GCC_except_table5797
+ GCC_except_table5800
+ GCC_except_table5806
+ GCC_except_table5815
+ GCC_except_table5818
+ GCC_except_table5822
+ GCC_except_table5900
+ GCC_except_table5901
+ GCC_except_table6025
+ GCC_except_table6026
+ GCC_except_table6027
+ GCC_except_table6031
+ GCC_except_table6032
+ GCC_except_table6033
+ GCC_except_table6034
+ GCC_except_table6036
+ GCC_except_table6037
+ GCC_except_table6038
+ GCC_except_table6039
+ GCC_except_table6040
+ GCC_except_table6041
+ GCC_except_table6042
+ GCC_except_table6043
+ GCC_except_table6052
+ GCC_except_table6057
+ GCC_except_table6058
+ GCC_except_table6059
+ GCC_except_table6064
+ GCC_except_table6090
+ GCC_except_table6169
+ GCC_except_table6170
+ GCC_except_table6171
+ GCC_except_table6172
+ GCC_except_table915
+ GCC_except_table917
+ GCC_except_table919
+ GCC_except_table920
+ GCC_except_table922
+ GCC_except_table924
+ GCC_except_table965
+ OBJC_IVAR_$_NEIKEv2IntermediatePacket._authenticatedDataVector
+ OBJC_IVAR_$_NENetworkAgentSessionFileHandle._name
+ OBJC_IVAR_$_NERelayConfiguration._excludedFQDNs
+ OBJC_IVAR_$_NERelayConfiguration._internalExcludedDomains
+ OBJC_IVAR_$_NERelayConfiguration._internalMatchDomains
+ OBJC_IVAR_$_NERelayConfiguration._matchFQDNs
+ OBJC_IVAR_$_NERelayConfiguration._uiToggleEnabled
+ _CCHmacInit
+ _CFDictionaryGetValueIfPresent
+ _NEAddSensitiveDataToDictionary
+ _NEIPSecDBCopyValueIfPresent
+ _NEIPSecDBCreateMutableDictionary
+ _OBJC_CLASS_$_NENetworkAgentSessionFileHandle
+ _OBJC_METACLASS_$_NENetworkAgentSessionFileHandle
+ __Block_byref_object_copy_.12318
+ __Block_byref_object_copy_.14712
+ __Block_byref_object_copy_.17061
+ __Block_byref_object_copy_.21151
+ __Block_byref_object_copy_.22207
+ __Block_byref_object_copy_.23426
+ __Block_byref_object_copy_.24106
+ __Block_byref_object_copy_.26540
+ __Block_byref_object_copy_.27681
+ __Block_byref_object_copy_.6944
+ __Block_byref_object_copy_.9495
+ __Block_byref_object_dispose_.12319
+ __Block_byref_object_dispose_.14713
+ __Block_byref_object_dispose_.17062
+ __Block_byref_object_dispose_.21152
+ __Block_byref_object_dispose_.22208
+ __Block_byref_object_dispose_.23427
+ __Block_byref_object_dispose_.24107
+ __Block_byref_object_dispose_.26541
+ __Block_byref_object_dispose_.27682
+ __Block_byref_object_dispose_.6945
+ __Block_byref_object_dispose_.9496
+ __NEIPSecDBUpdateSA_block_invoke.121
+ __OBJC_$_INSTANCE_METHODS_NENetworkAgentSessionFileHandle
+ __OBJC_$_INSTANCE_VARIABLES_NENetworkAgentSessionFileHandle
+ __OBJC_$_PROP_LIST_NENetworkAgentSessionFileHandle
+ __OBJC_CLASS_RO_$_NENetworkAgentSessionFileHandle
+ __OBJC_METACLASS_RO_$_NENetworkAgentSessionFileHandle
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ __block_descriptor_tmp.11
+ __block_descriptor_tmp.117
+ __block_descriptor_tmp.124
+ __block_descriptor_tmp.15
+ __block_descriptor_tmp.19328
+ __block_descriptor_tmp.22908
+ __block_descriptor_tmp.24957
+ __block_descriptor_tmp.25570
+ __block_literal_global.10.15181
+ __block_literal_global.10.9159
+ __block_literal_global.12602
+ __block_literal_global.12977
+ __block_literal_global.13860
+ __block_literal_global.14.21673
+ __block_literal_global.14.25184
+ __block_literal_global.14041
+ __block_literal_global.14714
+ __block_literal_global.15183
+ __block_literal_global.15745
+ __block_literal_global.15987
+ __block_literal_global.16675
+ __block_literal_global.17069
+ __block_literal_global.17504
+ __block_literal_global.17640
+ __block_literal_global.17947
+ __block_literal_global.19.13873
+ __block_literal_global.19.17631
+ __block_literal_global.19254
+ __block_literal_global.19895
+ __block_literal_global.20162
+ __block_literal_global.21242
+ __block_literal_global.21678
+ __block_literal_global.22.13874
+ __block_literal_global.22.17637
+ __block_literal_global.22073
+ __block_literal_global.22824
+ __block_literal_global.22906
+ __block_literal_global.23371
+ __block_literal_global.23511
+ __block_literal_global.23621
+ __block_literal_global.23655
+ __block_literal_global.23848
+ __block_literal_global.24893
+ __block_literal_global.24955
+ __block_literal_global.25188
+ __block_literal_global.25293
+ __block_literal_global.25676
+ __block_literal_global.26076
+ __block_literal_global.26252
+ __block_literal_global.26506
+ __block_literal_global.27060
+ __block_literal_global.27702
+ __block_literal_global.28.26544
+ __block_literal_global.28.5604
+ __block_literal_global.3453
+ __block_literal_global.3732
+ __block_literal_global.3814
+ __block_literal_global.4.13863
+ __block_literal_global.4225
+ __block_literal_global.4311
+ __block_literal_global.4676
+ __block_literal_global.4976
+ __block_literal_global.5625
+ __block_literal_global.63.19890
+ __block_literal_global.63.4971
+ __block_literal_global.69.3727
+ __block_literal_global.69.3809
+ __block_literal_global.6974
+ __block_literal_global.7.24883
+ __block_literal_global.7196
+ __block_literal_global.72.25288
+ __block_literal_global.7380
+ __block_literal_global.75.4220
+ __block_literal_global.75.4306
+ __block_literal_global.7794
+ __block_literal_global.9157
+ __oidQCCompliance
+ __oidQCDisclosures
+ __oidQCEuRetentionPeriod
+ __oidQCLimitValue
+ __oidQCStatements
+ __oidQCSyntaxv1
+ __oidQCSyntaxv2
+ __oidQCType
+ __oidQCTypeEseal
+ __oidQCTypeEsign
+ __oidQCTypeWeb
+ __oidSemanticsIdEidasLegal
+ __oidSemanticsIdEidasNatural
+ __oidSemanticsIdLegal
+ __oidSemanticsIdNatural
+ _cc_clear
+ _extensionAuxiliaryHostProtocol.protocol.19891
+ _extensionAuxiliaryHostProtocol.protocol.23656
+ _extensionAuxiliaryHostProtocol.protocol.25289
+ _extensionAuxiliaryHostProtocol.protocol.3728
+ _extensionAuxiliaryHostProtocol.protocol.3810
+ _extensionAuxiliaryHostProtocol.protocol.4221
+ _extensionAuxiliaryHostProtocol.protocol.4307
+ _extensionAuxiliaryHostProtocol.protocol.4673
+ _extensionAuxiliaryHostProtocol.protocol.4972
+ _extensionAuxiliaryHostProtocol.protocolInit.19889
+ _extensionAuxiliaryHostProtocol.protocolInit.23654
+ _extensionAuxiliaryHostProtocol.protocolInit.25287
+ _extensionAuxiliaryHostProtocol.protocolInit.3726
+ _extensionAuxiliaryHostProtocol.protocolInit.3808
+ _extensionAuxiliaryHostProtocol.protocolInit.4219
+ _extensionAuxiliaryHostProtocol.protocolInit.4305
+ _extensionAuxiliaryHostProtocol.protocolInit.4672
+ _extensionAuxiliaryHostProtocol.protocolInit.4970
+ _extensionAuxiliaryVendorProtocol.protocol.19896
+ _extensionAuxiliaryVendorProtocol.protocol.25294
+ _extensionAuxiliaryVendorProtocol.protocol.3733
+ _extensionAuxiliaryVendorProtocol.protocol.3815
+ _extensionAuxiliaryVendorProtocol.protocol.4226
+ _extensionAuxiliaryVendorProtocol.protocol.4312
+ _extensionAuxiliaryVendorProtocol.protocol.4677
+ _extensionAuxiliaryVendorProtocol.protocol.4977
+ _extensionAuxiliaryVendorProtocol.protocolInit.19894
+ _extensionAuxiliaryVendorProtocol.protocolInit.25292
+ _extensionAuxiliaryVendorProtocol.protocolInit.3731
+ _extensionAuxiliaryVendorProtocol.protocolInit.3813
+ _extensionAuxiliaryVendorProtocol.protocolInit.4224
+ _extensionAuxiliaryVendorProtocol.protocolInit.4310
+ _extensionAuxiliaryVendorProtocol.protocolInit.4675
+ _extensionAuxiliaryVendorProtocol.protocolInit.4975
+ _kNEExcludedFQDNsPayloadKey
+ _kNEMatchFQDNsPayloadKey
+ _objc_msgSend$dupSessionFileDescriptor
+ _objc_msgSend$excludedFQDNs
+ _objc_msgSend$initWithNetworkAgentSession:name:
+ _objc_msgSend$isUIToggleEnabled
+ _objc_msgSend$matchFQDNs
+ _objc_msgSend$setExcludedFQDNs:
+ _objc_msgSend$setMatchFQDNs:
+ _objc_msgSend$setUiToggleEnabled:
+ _oidQCCompliance
+ _oidQCDisclosures
+ _oidQCEuRetentionPeriod
+ _oidQCLimitValue
+ _oidQCStatements
+ _oidQCSyntaxv1
+ _oidQCSyntaxv2
+ _oidQCType
+ _oidQCTypeEseal
+ _oidQCTypeEsign
+ _oidQCTypeWeb
+ _oidSemanticsIdEidasLegal
+ _oidSemanticsIdEidasNatural
+ _oidSemanticsIdLegal
+ _oidSemanticsIdNatural
+ _trimStars
+ block_copy_helper.56
+ block_descriptor.58
+ block_destroy_helper.57
+ convert_error_to_string.24099
+ driverInterface.driverInterface.16676
+ driverInterface.driverInterface.20159
+ driverInterface.driverInterface.21674
+ driverInterface.driverInterface.7374
+ driverInterface.onceToken.16674
+ driverInterface.onceToken.20158
+ driverInterface.onceToken.21672
+ driverInterface.onceToken.7373
+ g_noAppFilter.27655
+ globalConfigurationManager.gChangeQueue.17635
+ globalConfigurationManager.gChangeQueue.5623
+ globalConfigurationManager.gConfigurationManager.17632
+ globalConfigurationManager.gConfigurationManager.5621
+ globalConfigurationManager.onceToken.17630
+ globalConfigurationManager.onceToken.5620
+ initGlobals.onceToken.15986
+ isA_CFArray.25388
+ loadedManagers.loadedManagers.26504
+ loadedManagers.loadedManagers.27658
+ loadedManagers.managers_init.26503
+ loadedManagers.managers_init.27657
+ managerInterface.managerInterface.20163
+ managerInterface.managerInterface.21679
+ managerInterface.onceToken.20161
+ managerInterface.onceToken.21677
+ sharedManager.g_manager.7197
+ sharedManager.g_manager.7795
+ sharedManager.init_manager.7195
+ sharedManager.init_manager.7793
+ sharedManager.onceToken.17639
+ sharedManager.onceToken.27701
+ sharedManager.onceToken.5624
- +[NEIKEv2IKESA createAuthenticationDataForSharedSecret:octets:prfProtocol:]
- -[NEIKEv2GSPM createLocalSignedOctets]
- -[NEIKEv2GSPM createRemoteSignedOctets]
- -[NEIKEv2IKESA clearAuthenticationSecrets]
- -[NEIKEv2IKESA copyCertSigningKey]
- -[NEIKEv2IKESA createAuthenticationDataForSharedSecret:octets:]
- -[NEIKEv2IKESA createInitiatorSignedOctetsUsingPrimeKey:]
- -[NEIKEv2IKESA createIntAuthOctets]
- -[NEIKEv2IKESA createResponderSignedOctetsUsingPrimeKey:]
- -[NEIKEv2IntegrityProtocol digestLength]
- -[NEIKEv2IntermediatePacket authenticatedData]
- -[NEIKEv2PacketTunnelProvider stopObserving]
- -[NEIKEv2SecurityContextCBCPlusHMAC computeIncomingHMACUsingContext:authenticatedHeaders:payloadData:]
- -[NEIKEv2SecurityContextCBCPlusHMAC computeOutgoingHMACUsingContext:payloadData:]
- GCC_except_table1052
- GCC_except_table1108
- GCC_except_table1109
- GCC_except_table1116
- GCC_except_table1282
- GCC_except_table1283
- GCC_except_table1286
- GCC_except_table1287
- GCC_except_table1290
- GCC_except_table1291
- GCC_except_table1305
- GCC_except_table1319
- GCC_except_table1330
- GCC_except_table1331
- GCC_except_table1459
- GCC_except_table1584
- GCC_except_table1585
- GCC_except_table1593
- GCC_except_table1645
- GCC_except_table1646
- GCC_except_table1647
- GCC_except_table1648
- GCC_except_table1649
- GCC_except_table1650
- GCC_except_table1666
- GCC_except_table1669
- GCC_except_table1677
- GCC_except_table1678
- GCC_except_table1685
- GCC_except_table1715
- GCC_except_table1743
- GCC_except_table2793
- GCC_except_table2803
- GCC_except_table3042
- GCC_except_table3047
- GCC_except_table3053
- GCC_except_table3056
- GCC_except_table3074
- GCC_except_table3075
- GCC_except_table3076
- GCC_except_table3090
- GCC_except_table3100
- GCC_except_table3101
- GCC_except_table3184
- GCC_except_table3232
- GCC_except_table3282
- GCC_except_table3296
- GCC_except_table3305
- GCC_except_table3307
- GCC_except_table3324
- GCC_except_table3325
- GCC_except_table3326
- GCC_except_table3342
- GCC_except_table3384
- GCC_except_table3392
- GCC_except_table3394
- GCC_except_table3429
- GCC_except_table3431
- GCC_except_table3432
- GCC_except_table3521
- GCC_except_table3545
- GCC_except_table3784
- GCC_except_table3809
- GCC_except_table3810
- GCC_except_table3811
- GCC_except_table3812
- GCC_except_table3814
- GCC_except_table3897
- GCC_except_table3945
- GCC_except_table3952
- GCC_except_table4053
- GCC_except_table4068
- GCC_except_table4090
- GCC_except_table4091
- GCC_except_table4092
- GCC_except_table4093
- GCC_except_table4094
- GCC_except_table4096
- GCC_except_table4097
- GCC_except_table4101
- GCC_except_table4106
- GCC_except_table4107
- GCC_except_table4120
- GCC_except_table4121
- GCC_except_table4193
- GCC_except_table4194
- GCC_except_table4202
- GCC_except_table4296
- GCC_except_table4297
- GCC_except_table4298
- GCC_except_table4299
- GCC_except_table4300
- GCC_except_table4301
- GCC_except_table4303
- GCC_except_table4384
- GCC_except_table4554
- GCC_except_table4564
- GCC_except_table4568
- GCC_except_table4581
- GCC_except_table4601
- GCC_except_table4603
- GCC_except_table4609
- GCC_except_table4611
- GCC_except_table4705
- GCC_except_table4774
- GCC_except_table4794
- GCC_except_table4808
- GCC_except_table4906
- GCC_except_table4911
- GCC_except_table4955
- GCC_except_table5001
- GCC_except_table5003
- GCC_except_table5065
- GCC_except_table5068
- GCC_except_table5106
- GCC_except_table5126
- GCC_except_table5128
- GCC_except_table5130
- GCC_except_table5141
- GCC_except_table5180
- GCC_except_table5181
- GCC_except_table5183
- GCC_except_table5185
- GCC_except_table5188
- GCC_except_table5232
- GCC_except_table5256
- GCC_except_table5328
- GCC_except_table5652
- GCC_except_table5666
- GCC_except_table5667
- GCC_except_table5670
- GCC_except_table5723
- GCC_except_table5729
- GCC_except_table5730
- GCC_except_table5739
- GCC_except_table5742
- GCC_except_table5748
- GCC_except_table5763
- GCC_except_table5764
- GCC_except_table5766
- GCC_except_table5767
- GCC_except_table5768
- GCC_except_table5769
- GCC_except_table5770
- GCC_except_table5773
- GCC_except_table5774
- GCC_except_table5777
- GCC_except_table5783
- GCC_except_table5795
- GCC_except_table5799
- GCC_except_table5877
- GCC_except_table5878
- GCC_except_table6002
- GCC_except_table6003
- GCC_except_table6004
- GCC_except_table6005
- GCC_except_table6006
- GCC_except_table6007
- GCC_except_table6008
- GCC_except_table6009
- GCC_except_table6010
- GCC_except_table6011
- GCC_except_table6012
- GCC_except_table6013
- GCC_except_table6014
- GCC_except_table6023
- GCC_except_table6061
- GCC_except_table6140
- GCC_except_table6141
- GCC_except_table6142
- GCC_except_table6143
- GCC_except_table909
- GCC_except_table910
- GCC_except_table911
- GCC_except_table912
- GCC_except_table913
- GCC_except_table914
- GCC_except_table959
- OBJC_IVAR_$_NEIKEv2IntermediatePacket._internalAuthenticatedData
- OBJC_IVAR_$_NERelayConfiguration._excludedDomains
- OBJC_IVAR_$_NERelayConfiguration._matchDomains
- _CCHmac
- _CCHmacClone
- _CCHmacCreate
- _CCHmacDestroy
- _CCHmacOutputSizeFromRef
- __Block_byref_object_copy_.12308
- __Block_byref_object_copy_.14698
- __Block_byref_object_copy_.16999
- __Block_byref_object_copy_.21052
- __Block_byref_object_copy_.22109
- __Block_byref_object_copy_.23327
- __Block_byref_object_copy_.24007
- __Block_byref_object_copy_.26453
- __Block_byref_object_copy_.27584
- __Block_byref_object_copy_.6930
- __Block_byref_object_copy_.9486
- __Block_byref_object_dispose_.12309
- __Block_byref_object_dispose_.14699
- __Block_byref_object_dispose_.17000
- __Block_byref_object_dispose_.21053
- __Block_byref_object_dispose_.22110
- __Block_byref_object_dispose_.23328
- __Block_byref_object_dispose_.24008
- __Block_byref_object_dispose_.26454
- __Block_byref_object_dispose_.27585
- __Block_byref_object_dispose_.6931
- __Block_byref_object_dispose_.9487
- __NEIPSecDBUpdateSA_block_invoke.124
- __block_descriptor_tmp.123
- __block_descriptor_tmp.130
- __block_descriptor_tmp.14
- __block_descriptor_tmp.18.24940
- __block_descriptor_tmp.19271
- __block_descriptor_tmp.22809
- __block_descriptor_tmp.24876
- __block_descriptor_tmp.25484
- __block_literal_global.10.15167
- __block_literal_global.10.9147
- __block_literal_global.12593
- __block_literal_global.12967
- __block_literal_global.13849
- __block_literal_global.14.21575
- __block_literal_global.14.25103
- __block_literal_global.14030
- __block_literal_global.14700
- __block_literal_global.15169
- __block_literal_global.15729
- __block_literal_global.15971
- __block_literal_global.16659
- __block_literal_global.17007
- __block_literal_global.17446
- __block_literal_global.17581
- __block_literal_global.17889
- __block_literal_global.19.13862
- __block_literal_global.19.17572
- __block_literal_global.19197
- __block_literal_global.19839
- __block_literal_global.20107
- __block_literal_global.21144
- __block_literal_global.21580
- __block_literal_global.21975
- __block_literal_global.22.13863
- __block_literal_global.22.17578
- __block_literal_global.22725
- __block_literal_global.22807
- __block_literal_global.23272
- __block_literal_global.23412
- __block_literal_global.23522
- __block_literal_global.23556
- __block_literal_global.23749
- __block_literal_global.24810
- __block_literal_global.24874
- __block_literal_global.25107
- __block_literal_global.25207
- __block_literal_global.25590
- __block_literal_global.25990
- __block_literal_global.26166
- __block_literal_global.26420
- __block_literal_global.26973
- __block_literal_global.27605
- __block_literal_global.28.26457
- __block_literal_global.28.5602
- __block_literal_global.3450
- __block_literal_global.3728
- __block_literal_global.3810
- __block_literal_global.4.13852
- __block_literal_global.4221
- __block_literal_global.4307
- __block_literal_global.4671
- __block_literal_global.4970
- __block_literal_global.5623
- __block_literal_global.63.19834
- __block_literal_global.63.4965
- __block_literal_global.69.3723
- __block_literal_global.69.3805
- __block_literal_global.6961
- __block_literal_global.7.24800
- __block_literal_global.7183
- __block_literal_global.72.25202
- __block_literal_global.7369
- __block_literal_global.75.4216
- __block_literal_global.75.4302
- __block_literal_global.7783
- __block_literal_global.9145
- _extensionAuxiliaryHostProtocol.protocol.19835
- _extensionAuxiliaryHostProtocol.protocol.23557
- _extensionAuxiliaryHostProtocol.protocol.25203
- _extensionAuxiliaryHostProtocol.protocol.3724
- _extensionAuxiliaryHostProtocol.protocol.3806
- _extensionAuxiliaryHostProtocol.protocol.4217
- _extensionAuxiliaryHostProtocol.protocol.4303
- _extensionAuxiliaryHostProtocol.protocol.4668
- _extensionAuxiliaryHostProtocol.protocol.4966
- _extensionAuxiliaryHostProtocol.protocolInit.19833
- _extensionAuxiliaryHostProtocol.protocolInit.23555
- _extensionAuxiliaryHostProtocol.protocolInit.25201
- _extensionAuxiliaryHostProtocol.protocolInit.3722
- _extensionAuxiliaryHostProtocol.protocolInit.3804
- _extensionAuxiliaryHostProtocol.protocolInit.4215
- _extensionAuxiliaryHostProtocol.protocolInit.4301
- _extensionAuxiliaryHostProtocol.protocolInit.4667
- _extensionAuxiliaryHostProtocol.protocolInit.4964
- _extensionAuxiliaryVendorProtocol.protocol.19840
- _extensionAuxiliaryVendorProtocol.protocol.25208
- _extensionAuxiliaryVendorProtocol.protocol.3729
- _extensionAuxiliaryVendorProtocol.protocol.3811
- _extensionAuxiliaryVendorProtocol.protocol.4222
- _extensionAuxiliaryVendorProtocol.protocol.4308
- _extensionAuxiliaryVendorProtocol.protocol.4672
- _extensionAuxiliaryVendorProtocol.protocol.4971
- _extensionAuxiliaryVendorProtocol.protocolInit.19838
- _extensionAuxiliaryVendorProtocol.protocolInit.25206
- _extensionAuxiliaryVendorProtocol.protocolInit.3727
- _extensionAuxiliaryVendorProtocol.protocolInit.3809
- _extensionAuxiliaryVendorProtocol.protocolInit.4220
- _extensionAuxiliaryVendorProtocol.protocolInit.4306
- _extensionAuxiliaryVendorProtocol.protocolInit.4670
- _extensionAuxiliaryVendorProtocol.protocolInit.4969
- _kCFBooleanFalse
- _swift_isUniquelyReferenced_nonNull_native
- block_copy_helper.32
- block_descriptor.34
- block_destroy_helper.33
- convert_error_to_string.24000
- driverInterface.driverInterface.16660
- driverInterface.driverInterface.20104
- driverInterface.driverInterface.21576
- driverInterface.driverInterface.7363
- driverInterface.onceToken.16658
- driverInterface.onceToken.20103
- driverInterface.onceToken.21574
- driverInterface.onceToken.7362
- g_noAppFilter.27558
- globalConfigurationManager.gChangeQueue.17576
- globalConfigurationManager.gChangeQueue.5621
- globalConfigurationManager.gConfigurationManager.17573
- globalConfigurationManager.gConfigurationManager.5619
- globalConfigurationManager.onceToken.17571
- globalConfigurationManager.onceToken.5618
- initGlobals.onceToken.15970
- isA_CFArray.25302
- loadedManagers.loadedManagers.26418
- loadedManagers.loadedManagers.27561
- loadedManagers.managers_init.26417
- loadedManagers.managers_init.27560
- managerInterface.managerInterface.20108
- managerInterface.managerInterface.21581
- managerInterface.onceToken.20106
- managerInterface.onceToken.21579
- sharedManager.g_manager.7184
- sharedManager.g_manager.7784
- sharedManager.init_manager.7182
- sharedManager.init_manager.7782
- sharedManager.onceToken.17580
- sharedManager.onceToken.27604
- sharedManager.onceToken.5622
CStrings:
+ "%s called with null dataVector"
+ "%s called with null direction"
+ "%s called with null mutableSAData"
+ "%s called with null packet.authenticatedDataVector"
+ "%s called with null remoteSignedOctetVector"
+ "%s called with null saData"
+ "%s called with null self.gspmHandler.sessionKey"
+ "%s%s:%s "
+ "+[NEIKEv2Crypto createHMACFromDataVector:key:prfProtocol:]"
+ "+[NEIKEv2IKESA(Crypto) createAuthenticationDataForSharedSecret:octetVector:prfProtocol:]"
+ "-[NEIKEv2GSPM createLocalSignedOctetVector]"
+ "-[NEIKEv2GSPM createRemoteSignedOctetVector]"
+ "-[NEIKEv2IKESA(Crypto) createAuthenticationDataForSharedSecret:octetVector:]"
+ "-[NEIKEv2IKESA(Crypto) createInitiatorSignedOctetVectorUsingPrimeKey:]"
+ "-[NEIKEv2IKESA(Crypto) createIntAuthOctetVector]"
+ "-[NEIKEv2IKESA(Crypto) createResponderSignedOctetVectorUsingPrimeKey:]"
+ "-[NEIKEv2IntermediatePacket authenticatedDataVector]"
+ "ExcludedFQDNs"
+ "Failed to create responder identifier payload for GSPM"
+ "Failed to get Initiator ID data for %@"
+ "Failed to get Responder ID data for %@"
+ "Invalid DoH hostname"
+ "Invalid excluded FQDN"
+ "Invalid match FQDN"
+ "MatchFQDNs"
+ "NEIPSecDBCreateMutableDictionary"
+ "NEIPSecDBFilloutBasicSAInfo"
+ "NENetworkAgentSessionFileHandle"
+ "Network Agent Session socket (%d) %@"
+ "T@\"NSArray\",&,V_internalExcludedDomains"
+ "T@\"NSArray\",&,V_internalMatchDomains"
+ "T@\"NSArray\",C,V_excludedFQDNs"
+ "T@\"NSArray\",C,V_matchFQDNs"
+ "TB,GisUIToggleEnabled"
+ "TB,GisUIToggleEnabled,V_uiToggleEnabled"
+ "Unnecessary excludes when matching only FQDNs"
+ "[NEIKEv2Crypto createHMACFromDataVector:key:prfProtocol:] failed"
+ "[NEIKEv2Crypto createIntAuthOctetVector] failed"
+ "[self createLocalSignedOctetVectorUsingPrimeKey:] failed"
+ "[self createRemoteSignedOctetVectorUsingPrimeKey:] failed"
+ "_authenticatedDataVector"
+ "_excludedFQDNs"
+ "_internalExcludedDomains"
+ "_internalMatchDomains"
+ "_matchFQDNs"
+ "_uiToggleEnabled"
+ "createInitiatorSignedOctetVector(GSPM) failed"
+ "createInitiatorSignedOctetVectorUsingPrimeKey failed"
+ "createInitiatorSignedOctetVectorUsingPrimeKey: failed"
+ "createResponderSignedOctetVector(GSPM) failed"
+ "createResponderSignedOctetVectorUsingPrimeKey failed"
+ "createResponderSignedOctetVectorUsingPrimeKey: failed"
+ "dupSessionFileDescriptor"
+ "excludedFQDNs"
+ "fqdn"
+ "initWithNetworkAgentSession:"
+ "initWithNetworkAgentSession:name:"
+ "internalExcludedDomains"
+ "internalMatchDomains"
+ "isUIToggleEnabled"
+ "matchFQDNs"
+ "sensitiveDataWithBytes:length:%zu failed"
+ "setExcludedFQDNs:"
+ "setInternalExcludedDomains:"
+ "setInternalMatchDomains:"
+ "setMatchFQDNs:"
+ "setUIToggleEnabled:"
+ "setUiToggleEnabled:"
+ "uiToggleEnabled"
- "%s called with null packet.authenticatedData"
- "%s called with null self.gspmHandler"
- "%sdomain:%s "
- "+[NEIKEv2IKESA(Crypto) createAuthenticationDataForSharedSecret:octets:prfProtocol:]"
- "-[NEIKEv2GSPM createLocalSignedOctets]"
- "-[NEIKEv2GSPM createRemoteSignedOctets]"
- "-[NEIKEv2IKESA(Crypto) createAuthenticationDataForSharedSecret:octets:]"
- "-[NEIKEv2IKESA(Crypto) createInitiatorSignedOctetsUsingPrimeKey:]"
- "-[NEIKEv2IKESA(Crypto) createIntAuthOctets]"
- "-[NEIKEv2IKESA(Crypto) createResponderSignedOctetsUsingPrimeKey:]"
- "-[NEIKEv2IntermediatePacket authenticatedData]"
- "CCHmacClone failed"
- "CCHmacCreate failed"
- "GSPM.sessionKey failed"
- "PRF length %u != HMAC output size %zu"
- "[NEIKEv2Crypto createIntAuthOctets] failed"
- "[NESensitiveData mutableSensitiveDataWithMaxCapacity:%zu] failed"
- "[self createRemoteSignedOctetsUsingPrimeKey:] failed"
- "^{?=[96I]}"
- "_internalAuthenticatedData"
- "creatInitiatorSignedOctets(GSPM) failed"
- "createInitiatorSignedOctets failed"
- "createInitiatorSignedOctetsUsingPrimeKey: failed"
- "createResponderSignedOctets failed"
- "createResponderSignedOctets(GSPM) failed"
- "createResponderSignedOctetsUsingPrimeKey: failed"
- "saData is NULL"

```
