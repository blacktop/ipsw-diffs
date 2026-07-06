## NetworkExtension

> `/System/Library/Frameworks/NetworkExtension.framework/NetworkExtension`

```diff

-  __TEXT.__text: 0x2078fc
-  __TEXT.__objc_methlist: 0xf2e8
-  __TEXT.__const: 0x367c
+  __TEXT.__text: 0x20f6d0
+  __TEXT.__objc_methlist: 0xf4b8
+  __TEXT.__const: 0x36a4
   __TEXT.__swift5_typeref: 0xdda
   __TEXT.__swift5_capture: 0x1010
   __TEXT.__constg_swiftt: 0xc7c

   __TEXT.__swift_as_cont: 0x1f4
   __TEXT.__swift5_fieldmd: 0x680
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__cstring: 0x194c0
-  __TEXT.__oslogstring: 0x24b23
-  __TEXT.__gcc_except_tab: 0x4ff8
-  __TEXT.__unwind_info: 0x5640
-  __TEXT.__eh_frame: 0x2b88
+  __TEXT.__cstring: 0x19606
+  __TEXT.__oslogstring: 0x24c2d
+  __TEXT.__gcc_except_tab: 0x4ff4
+  __TEXT.__unwind_info: 0x56d0
+  __TEXT.__eh_frame: 0x2bc0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x63f0
-  __DATA_CONST.__objc_classlist: 0xb38
+  __DATA_CONST.__const: 0x6448
+  __DATA_CONST.__objc_classlist: 0xb40
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x260
+  __DATA_CONST.__objc_protolist: 0x268
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5338
+  __DATA_CONST.__objc_selrefs: 0x5378
   __DATA_CONST.__objc_protorefs: 0x158
-  __DATA_CONST.__objc_superrefs: 0x720
+  __DATA_CONST.__objc_superrefs: 0x728
   __DATA_CONST.__objc_arraydata: 0x138
   __DATA_CONST.__got: 0x17f0
   __AUTH_CONST.__const: 0x4a00
-  __AUTH_CONST.__cfstring: 0x190a0
-  __AUTH_CONST.__objc_const: 0x23210
+  __AUTH_CONST.__cfstring: 0x19220
+  __AUTH_CONST.__objc_const: 0x233e8
   __AUTH_CONST.__objc_intobj: 0x3a8
   __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x24b0
-  __AUTH.__objc_data: 0x15c8
-  __AUTH.__data: 0xc68
-  __DATA.__objc_ivar: 0x1c3c
-  __DATA.__data: 0x1ef0
-  __DATA.__bss: 0x1668
-  __DATA.__common: 0x188
-  __DATA_DIRTY.__objc_data: 0x6040
-  __DATA_DIRTY.__bss: 0x68
-  __DATA_DIRTY.__common: 0x30
+  __AUTH_CONST.__auth_got: 0x24c0
+  __AUTH.__objc_data: 0x3bc0
+  __AUTH.__data: 0x128
+  __DATA.__objc_ivar: 0x1c48
+  __DATA.__data: 0x1e70
+  __DATA.__bss: 0x1650
+  __DATA.__common: 0x180
+  __DATA_DIRTY.__objc_data: 0x3a98
+  __DATA_DIRTY.__data: 0xc20
+  __DATA_DIRTY.__bss: 0x78
+  __DATA_DIRTY.__common: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8250
-  Symbols:   24151
-  CStrings:  10452
+  Functions: 8302
+  Symbols:   24271
+  CStrings:  10481
 
Sections:
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_protos : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
Symbols:
+ -[NEAOVPN dictionaryRepresentation]
+ -[NEAOVPNException dictionaryRepresentation]
+ -[NEAppPush dictionaryRepresentation]
+ -[NEAppRule dictionaryRepresentation]
+ -[NEConfiguration dictionaryRepresentation]
+ -[NEContentFilter dictionaryRepresentation]
+ -[NEDNSOverHTTPSSettings dictionaryRepresentation]
+ -[NEDNSOverTLSSettings dictionaryRepresentation]
+ -[NEDNSProxy dictionaryRepresentation]
+ -[NEDNSProxyProviderProtocol dictionaryRepresentation]
+ -[NEDNSSettings dictionaryRepresentation]
+ -[NEDNSSettingsBundle dictionaryRepresentation]
+ -[NEEvaluateConnectionRule dictionaryRepresentation]
+ -[NEFilterProviderConfiguration dictionaryRepresentation]
+ -[NEHotspot dictionaryRepresentation]
+ -[NEIKEv2ChildSA unregisterAllInboundTLSSPIs]
+ -[NEIKEv2EncryptionProtocol ipsecEncryptionAlgorithm]
+ -[NEIKEv2Session installIncomingIPsecSAForChildSA:]
+ -[NEIKEv2Session installOutgoingIPsecSAForChildSA:]
+ -[NEIKEv2Session installRekeyedChildSA:inbound:]
+ -[NEIKEv2Session installTLSChildSA:inbound:outbound:]
+ -[NEIKEv2Session startInstallTimersForChildSA:incomingSA:outgoingSA:]
+ -[NEIKEv2Session uninstallOldRekeyedChildSA:]
+ -[NEIKEv2TLSSAInstallationRecord .cxx_destruct]
+ -[NEIKEv2TLSSAInstallationRecord initWithSPI:key:]
+ -[NEIKEv2TLSSAInstallationRecord key]
+ -[NEIKEv2TLSSAInstallationRecord spi]
+ -[NEOnDemandRule dictionaryRepresentation]
+ -[NEOnDemandRuleEvaluateConnection dictionaryRepresentation]
+ -[NEPathController dictionaryRepresentation]
+ -[NEPathRule dictionaryRepresentation]
+ -[NEPerApp dictionaryRepresentation]
+ -[NEPrivateLTENetwork dictionaryRepresentation]
+ -[NEProfileIngestionPayloadInfo dictionaryRepresentation]
+ -[NEProxyServer dictionaryRepresentation]
+ -[NEProxySettings dictionaryRepresentation]
+ -[NERelay dictionaryRepresentation]
+ -[NERelayConfiguration dictionaryRepresentation]
+ -[NETunnelProviderProtocol dictionaryRepresentation]
+ -[NEURLFilterConfiguration dictionaryRepresentation]
+ -[NEUtilConfigurationClient JSONStringForConfiguration:]
+ -[NEUtilConfigurationClient appendConfiguration:toOutputList:useJSON:]
+ -[NEUtilConfigurationClient sanitizeForJSON:]
+ -[NEVPN dictionaryRepresentation]
+ -[NEVPNApp dictionaryRepresentation]
+ -[NEVPNIKEv2SecurityAssociationParameters dictionaryRepresentation]
+ -[NEVPNProtocol dictionaryRepresentation]
+ -[NEVPNProtocolIKEv2 dictionaryRepresentation]
+ -[NEVPNProtocolIPSec dictionaryRepresentation]
+ GCC_except_table100
+ GCC_except_table1041
+ GCC_except_table106
+ GCC_except_table1130
+ GCC_except_table114
+ GCC_except_table1189
+ GCC_except_table1190
+ GCC_except_table1195
+ GCC_except_table1196
+ GCC_except_table1197
+ GCC_except_table133
+ GCC_except_table1365
+ GCC_except_table1366
+ GCC_except_table1369
+ GCC_except_table1371
+ GCC_except_table1372
+ GCC_except_table1373
+ GCC_except_table1374
+ GCC_except_table1377
+ GCC_except_table1383
+ GCC_except_table1388
+ GCC_except_table1402
+ GCC_except_table1413
+ GCC_except_table1414
+ GCC_except_table152
+ GCC_except_table1540
+ GCC_except_table1665
+ GCC_except_table1666
+ GCC_except_table1671
+ GCC_except_table1674
+ GCC_except_table1722
+ GCC_except_table1723
+ GCC_except_table1724
+ GCC_except_table1725
+ GCC_except_table1727
+ GCC_except_table1728
+ GCC_except_table1729
+ GCC_except_table1731
+ GCC_except_table1732
+ GCC_except_table1734
+ GCC_except_table1735
+ GCC_except_table1744
+ GCC_except_table1753
+ GCC_except_table1754
+ GCC_except_table1761
+ GCC_except_table1786
+ GCC_except_table1812
+ GCC_except_table2026
+ GCC_except_table277
+ GCC_except_table2937
+ GCC_except_table3182
+ GCC_except_table3187
+ GCC_except_table3196
+ GCC_except_table3211
+ GCC_except_table3212
+ GCC_except_table3213
+ GCC_except_table3228
+ GCC_except_table3242
+ GCC_except_table3243
+ GCC_except_table3285
+ GCC_except_table3289
+ GCC_except_table3335
+ GCC_except_table3386
+ GCC_except_table3446
+ GCC_except_table3465
+ GCC_except_table3474
+ GCC_except_table3476
+ GCC_except_table3499
+ GCC_except_table3500
+ GCC_except_table3501
+ GCC_except_table3511
+ GCC_except_table3525
+ GCC_except_table3563
+ GCC_except_table3569
+ GCC_except_table3571
+ GCC_except_table3606
+ GCC_except_table3608
+ GCC_except_table3609
+ GCC_except_table3698
+ GCC_except_table3726
+ GCC_except_table3968
+ GCC_except_table3975
+ GCC_except_table3976
+ GCC_except_table3977
+ GCC_except_table3978
+ GCC_except_table3980
+ GCC_except_table402
+ GCC_except_table404
+ GCC_except_table4072
+ GCC_except_table4238
+ GCC_except_table4255
+ GCC_except_table4270
+ GCC_except_table4271
+ GCC_except_table4272
+ GCC_except_table4275
+ GCC_except_table4276
+ GCC_except_table4277
+ GCC_except_table4278
+ GCC_except_table4282
+ GCC_except_table4287
+ GCC_except_table4288
+ GCC_except_table4294
+ GCC_except_table4301
+ GCC_except_table4302
+ GCC_except_table4374
+ GCC_except_table4375
+ GCC_except_table4383
+ GCC_except_table4479
+ GCC_except_table4480
+ GCC_except_table4481
+ GCC_except_table4482
+ GCC_except_table4483
+ GCC_except_table4484
+ GCC_except_table4486
+ GCC_except_table4581
+ GCC_except_table471
+ GCC_except_table4760
+ GCC_except_table4765
+ GCC_except_table4772
+ GCC_except_table4803
+ GCC_except_table4813
+ GCC_except_table4817
+ GCC_except_table4829
+ GCC_except_table4849
+ GCC_except_table4851
+ GCC_except_table4857
+ GCC_except_table4859
+ GCC_except_table4951
+ GCC_except_table5021
+ GCC_except_table5045
+ GCC_except_table5058
+ GCC_except_table5157
+ GCC_except_table5162
+ GCC_except_table5203
+ GCC_except_table5249
+ GCC_except_table5251
+ GCC_except_table5317
+ GCC_except_table5356
+ GCC_except_table5376
+ GCC_except_table5378
+ GCC_except_table5380
+ GCC_except_table5388
+ GCC_except_table5428
+ GCC_except_table5429
+ GCC_except_table5431
+ GCC_except_table5433
+ GCC_except_table5436
+ GCC_except_table5480
+ GCC_except_table5502
+ GCC_except_table5505
+ GCC_except_table5600
+ GCC_except_table5929
+ GCC_except_table5967
+ GCC_except_table5968
+ GCC_except_table5971
+ GCC_except_table6042
+ GCC_except_table6043
+ GCC_except_table6051
+ GCC_except_table6054
+ GCC_except_table6064
+ GCC_except_table6079
+ GCC_except_table6080
+ GCC_except_table6081
+ GCC_except_table6082
+ GCC_except_table6083
+ GCC_except_table6084
+ GCC_except_table6085
+ GCC_except_table6086
+ GCC_except_table6089
+ GCC_except_table6090
+ GCC_except_table6091
+ GCC_except_table6098
+ GCC_except_table6107
+ GCC_except_table6110
+ GCC_except_table6114
+ GCC_except_table6192
+ GCC_except_table6193
+ GCC_except_table6325
+ GCC_except_table6326
+ GCC_except_table6327
+ GCC_except_table6328
+ GCC_except_table6329
+ GCC_except_table633
+ GCC_except_table6330
+ GCC_except_table6331
+ GCC_except_table6332
+ GCC_except_table6333
+ GCC_except_table6334
+ GCC_except_table6335
+ GCC_except_table6336
+ GCC_except_table6337
+ GCC_except_table6338
+ GCC_except_table6339
+ GCC_except_table634
+ GCC_except_table6340
+ GCC_except_table6341
+ GCC_except_table6342
+ GCC_except_table6343
+ GCC_except_table6345
+ GCC_except_table635
+ GCC_except_table6354
+ GCC_except_table6359
+ GCC_except_table636
+ GCC_except_table6360
+ GCC_except_table6361
+ GCC_except_table6366
+ GCC_except_table637
+ GCC_except_table639
+ GCC_except_table6392
+ GCC_except_table645
+ GCC_except_table6471
+ GCC_except_table6472
+ GCC_except_table6473
+ GCC_except_table6474
+ GCC_except_table650
+ GCC_except_table665
+ GCC_except_table666
+ GCC_except_table763
+ GCC_except_table77
+ GCC_except_table830
+ GCC_except_table835
+ GCC_except_table884
+ GCC_except_table889
+ GCC_except_table907
+ GCC_except_table913
+ GCC_except_table914
+ GCC_except_table915
+ GCC_except_table916
+ GCC_except_table944
+ GCC_except_table983
+ GCC_except_table984
+ GCC_except_table985
+ GCC_except_table986
+ GCC_except_table987
+ GCC_except_table988
+ GCC_except_table990
+ GCC_except_table991
+ GCC_except_table992
+ GCC_except_table993
+ _NEHostnameHasMinimumLabels
+ _OBJC_CLASS_$_NEIKEv2TLSSAInstallationRecord
+ _OBJC_CLASS_$_NSISO8601DateFormatter
+ _OBJC_IVAR_$_NEIKEv2ChildSA._registeredInboundTLSSPIs
+ _OBJC_IVAR_$_NEIKEv2TLSSAInstallationRecord._key
+ _OBJC_IVAR_$_NEIKEv2TLSSAInstallationRecord._spi
+ _OBJC_METACLASS_$_NEIKEv2TLSSAInstallationRecord
+ __OBJC_$_INSTANCE_METHODS_NEIKEv2TLSSAInstallationRecord
+ __OBJC_$_INSTANCE_VARIABLES_NEIKEv2TLSSAInstallationRecord
+ __OBJC_$_PROP_LIST_NEIKEv2TLSSAInstallationRecord
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NEDictionaryRepresentable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NEDictionaryRepresentable
+ __OBJC_CLASS_RO_$_NEIKEv2TLSSAInstallationRecord
+ __OBJC_LABEL_PROTOCOL_$_NEDictionaryRepresentable
+ __OBJC_METACLASS_RO_$_NEIKEv2TLSSAInstallationRecord
+ __OBJC_PROTOCOL_$_NEDictionaryRepresentable
+ ___45-[NEUtilConfigurationClient sanitizeForJSON:]_block_invoke
+ ___53-[NEIKEv2Session installTLSChildSA:inbound:outbound:]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e15_v32?0816^B24ls32l8s40l8
+ ___block_descriptor_60_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ ___block_descriptor_68_e8_32s40s48s56bs_e72_v40?0"NSString"8"NSDictionary"16"NEConfiguration"24"NSDictionary"32ls32l8s40l8s48l8s56l8
+ _objc_msgSend$JSONStringForConfiguration:
+ _objc_msgSend$dictionaryRepresentation
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$objCType
+ _objc_msgSend$stringFromDate:timeZone:formatOptions:
+ _objc_msgSend$timeZoneWithAbbreviation:
+ _objc_msgSend$whitespaceCharacterSet
+ _symbolic _____Sg 9CryptoKit8MLKEM768O17OneTimePrivateKeyV
+ _symbolic _____Sg 9CryptoKit9MLKEM1024O17OneTimePrivateKeyV
- -[NEIKEv2Session installRekeyedChildSA:andReturnIPsecSAsToDelete:]
- -[NEIKEv2Session uninstallOldRekeyedChildSA:andDeleteIPsecSAs:]
- GCC_except_table1029
- GCC_except_table104
- GCC_except_table1118
- GCC_except_table112
- GCC_except_table1176
- GCC_except_table1177
- GCC_except_table1182
- GCC_except_table1183
- GCC_except_table1184
- GCC_except_table131
- GCC_except_table1352
- GCC_except_table1353
- GCC_except_table1356
- GCC_except_table1357
- GCC_except_table1358
- GCC_except_table1359
- GCC_except_table1360
- GCC_except_table1361
- GCC_except_table1362
- GCC_except_table1363
- GCC_except_table1364
- GCC_except_table1400
- GCC_except_table1401
- GCC_except_table150
- GCC_except_table1526
- GCC_except_table1651
- GCC_except_table1652
- GCC_except_table1657
- GCC_except_table1660
- GCC_except_table1705
- GCC_except_table1706
- GCC_except_table1707
- GCC_except_table1708
- GCC_except_table1709
- GCC_except_table1710
- GCC_except_table1711
- GCC_except_table1712
- GCC_except_table1713
- GCC_except_table1714
- GCC_except_table1715
- GCC_except_table1716
- GCC_except_table1717
- GCC_except_table1718
- GCC_except_table1739
- GCC_except_table1771
- GCC_except_table1797
- GCC_except_table2009
- GCC_except_table273
- GCC_except_table2919
- GCC_except_table3164
- GCC_except_table3169
- GCC_except_table3175
- GCC_except_table3178
- GCC_except_table3194
- GCC_except_table3195
- GCC_except_table3210
- GCC_except_table3224
- GCC_except_table3225
- GCC_except_table3267
- GCC_except_table3271
- GCC_except_table3317
- GCC_except_table3368
- GCC_except_table3428
- GCC_except_table3447
- GCC_except_table3456
- GCC_except_table3458
- GCC_except_table3477
- GCC_except_table3478
- GCC_except_table3479
- GCC_except_table3490
- GCC_except_table3497
- GCC_except_table3536
- GCC_except_table3542
- GCC_except_table3544
- GCC_except_table3579
- GCC_except_table3581
- GCC_except_table3582
- GCC_except_table3671
- GCC_except_table3699
- GCC_except_table3941
- GCC_except_table3948
- GCC_except_table3949
- GCC_except_table3950
- GCC_except_table3951
- GCC_except_table3953
- GCC_except_table398
- GCC_except_table400
- GCC_except_table4045
- GCC_except_table4210
- GCC_except_table4221
- GCC_except_table4227
- GCC_except_table4242
- GCC_except_table4243
- GCC_except_table4244
- GCC_except_table4245
- GCC_except_table4246
- GCC_except_table4247
- GCC_except_table4248
- GCC_except_table4250
- GCC_except_table4254
- GCC_except_table4259
- GCC_except_table4260
- GCC_except_table4266
- GCC_except_table4346
- GCC_except_table4347
- GCC_except_table4355
- GCC_except_table4448
- GCC_except_table4449
- GCC_except_table4450
- GCC_except_table4451
- GCC_except_table4452
- GCC_except_table4453
- GCC_except_table4455
- GCC_except_table4549
- GCC_except_table467
- GCC_except_table4727
- GCC_except_table4732
- GCC_except_table4739
- GCC_except_table4770
- GCC_except_table4780
- GCC_except_table4784
- GCC_except_table4796
- GCC_except_table4816
- GCC_except_table4818
- GCC_except_table4824
- GCC_except_table4826
- GCC_except_table4918
- GCC_except_table4988
- GCC_except_table4992
- GCC_except_table5012
- GCC_except_table5123
- GCC_except_table5128
- GCC_except_table5169
- GCC_except_table5215
- GCC_except_table5217
- GCC_except_table5281
- GCC_except_table5284
- GCC_except_table5340
- GCC_except_table5342
- GCC_except_table5344
- GCC_except_table5352
- GCC_except_table5391
- GCC_except_table5392
- GCC_except_table5394
- GCC_except_table5396
- GCC_except_table5399
- GCC_except_table5443
- GCC_except_table5465
- GCC_except_table5468
- GCC_except_table5559
- GCC_except_table5886
- GCC_except_table5922
- GCC_except_table5923
- GCC_except_table5926
- GCC_except_table5991
- GCC_except_table5997
- GCC_except_table5998
- GCC_except_table6006
- GCC_except_table6009
- GCC_except_table6019
- GCC_except_table6034
- GCC_except_table6035
- GCC_except_table6037
- GCC_except_table6038
- GCC_except_table6039
- GCC_except_table6040
- GCC_except_table6041
- GCC_except_table6044
- GCC_except_table6045
- GCC_except_table6046
- GCC_except_table6053
- GCC_except_table6062
- GCC_except_table6065
- GCC_except_table6069
- GCC_except_table6146
- GCC_except_table6147
- GCC_except_table626
- GCC_except_table627
- GCC_except_table6277
- GCC_except_table6278
- GCC_except_table6279
- GCC_except_table628
- GCC_except_table6280
- GCC_except_table6281
- GCC_except_table6282
- GCC_except_table6283
- GCC_except_table6284
- GCC_except_table6285
- GCC_except_table6286
- GCC_except_table6287
- GCC_except_table6288
- GCC_except_table6289
- GCC_except_table629
- GCC_except_table6290
- GCC_except_table6291
- GCC_except_table6292
- GCC_except_table6293
- GCC_except_table6294
- GCC_except_table6295
- GCC_except_table6296
- GCC_except_table6297
- GCC_except_table630
- GCC_except_table6306
- GCC_except_table631
- GCC_except_table6311
- GCC_except_table6312
- GCC_except_table6313
- GCC_except_table6318
- GCC_except_table632
- GCC_except_table6421
- GCC_except_table6422
- GCC_except_table6423
- GCC_except_table6424
- GCC_except_table643
- GCC_except_table644
- GCC_except_table659
- GCC_except_table75
- GCC_except_table752
- GCC_except_table819
- GCC_except_table824
- GCC_except_table873
- GCC_except_table878
- GCC_except_table896
- GCC_except_table902
- GCC_except_table903
- GCC_except_table904
- GCC_except_table905
- GCC_except_table933
- GCC_except_table972
- GCC_except_table973
- GCC_except_table974
- GCC_except_table975
- GCC_except_table976
- GCC_except_table977
- GCC_except_table979
- GCC_except_table98
- GCC_except_table980
- GCC_except_table981
- GCC_except_table982
- ___36-[NEIKEv2Session installTLSChildSA:]_block_invoke
- ___block_descriptor_60_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
- ___block_descriptor_60_e8_32s40s48bs_e72_v40?0"NSString"8"NSDictionary"16"NEConfiguration"24"NSDictionary"32ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56s_e36_v16?0"NEIKEv2InformationalPacket"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_76_e8_32s40s48s56s64bs_e5_v8?0ls64l8s32l8s40l8s48l8s56l8
- _symbolic _____Sg 9CryptoKit8MLKEM768O10PrivateKeyV
- _symbolic _____Sg 9CryptoKit9MLKEM1024O10PrivateKeyV
CStrings:
+ "%@ %@ Installing rekeyed IPsec childSA %s %@"
+ "%@ Installing TLS childSA %@ (inbound=%d outbound=%d)"
+ "%@ Missing inbound SPI/key installing TLS childSA %@"
+ "%@ Missing outbound SPI/key installing TLS childSA %@"
+ "%@ Unsupported crypto for childSA %@ (encryption %@, integrity %@)"
+ "%@ failed to find DDM sourced persistent reference for the identity"
+ "%s called with null incomingSA"
+ "-[NEIKEv2Session installRekeyedChildSA:inbound:]"
+ "-[NEIKEv2Session startInstallTimersForChildSA:incomingSA:outgoingSA:]"
+ "-[NEIKEv2Session uninstallOldRekeyedChildSA:]"
+ "-[NEIKEv2TLSSAInstallationRecord initWithSPI:key:]"
+ "Cleartext"
+ "Failed to install rekeyed Child SA inbound"
+ "Failed to install rekeyed Child SA outbound"
+ "Failed to serialize configuration '%@' to JSON"
+ "NoRestriction"
+ "O\t"
+ "RestrictDomains"
+ "UTC"
+ "Unsupported encryption %@ (key length %u)"
+ "isDDMSystemScope"
+ "json"
+ "responder rekeyed child SA last response"
- "%@ Installing TLS childSA %@"
- "%@ No integrity type selected, but encryption %@ is not authenticated"
- "%@ Unsupported %@ key length %u"
- "%@ Unsupported encryption wire type %@"
- "%@ Unsupported integrity type %u"
- "%s called with null sasToDelete"
- "-[NEIKEv2Session installRekeyedChildSA:andReturnIPsecSAsToDelete:]"
- "-[NEIKEv2Session uninstallOldRekeyedChildSA:andDeleteIPsecSAs:]"

```
