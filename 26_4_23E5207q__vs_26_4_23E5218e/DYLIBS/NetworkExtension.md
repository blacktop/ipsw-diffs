## NetworkExtension

> `/System/Library/Frameworks/NetworkExtension.framework/NetworkExtension`

```diff

-2226.100.24.0.0
-  __TEXT.__text: 0x2088fc
-  __TEXT.__auth_stubs: 0x44f0
-  __TEXT.__objc_methlist: 0xee98
-  __TEXT.__const: 0x3494
-  __TEXT.__cstring: 0x1856b
+2226.100.30.0.1
+  __TEXT.__text: 0x20af18
+  __TEXT.__auth_stubs: 0x4500
+  __TEXT.__objc_methlist: 0xeff0
+  __TEXT.__const: 0x34a4
+  __TEXT.__cstring: 0x186f9
   __TEXT.__constg_swiftt: 0xc1c
   __TEXT.__swift5_typeref: 0xdd3
-  __TEXT.__swift5_reflstr: 0x465
+  __TEXT.__swift5_reflstr: 0x464
   __TEXT.__swift5_fieldmd: 0x5a8
   __TEXT.__swift5_builtin: 0x8c
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_proto: 0x60
   __TEXT.__swift5_types: 0x90
   __TEXT.__swift5_capture: 0xd58
-  __TEXT.__oslogstring: 0x233d6
+  __TEXT.__oslogstring: 0x23c5c
   __TEXT.__swift_as_entry: 0xe4
   __TEXT.__swift_as_ret: 0x104
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__gcc_except_tab: 0x5a3c
-  __TEXT.__unwind_info: 0x54f0
-  __TEXT.__eh_frame: 0x2928
-  __TEXT.__objc_classname: 0x2f6f
-  __TEXT.__objc_methname: 0x1b047
-  __TEXT.__objc_methtype: 0x4031
-  __TEXT.__objc_stubs: 0x10600
-  __DATA_CONST.__got: 0x1728
+  __TEXT.__gcc_except_tab: 0x5ad0
+  __TEXT.__unwind_info: 0x5510
+  __TEXT.__eh_frame: 0x2900
+  __TEXT.__objc_classname: 0x2fc2
+  __TEXT.__objc_methname: 0x1b1f7
+  __TEXT.__objc_methtype: 0x4132
+  __TEXT.__objc_stubs: 0x10720
+  __DATA_CONST.__got: 0x1740
   __DATA_CONST.__const: 0x5a78
-  __DATA_CONST.__objc_classlist: 0xb28
+  __DATA_CONST.__objc_classlist: 0xb40
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x268
+  __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x51a8
+  __DATA_CONST.__objc_selrefs: 0x51f8
   __DATA_CONST.__objc_protorefs: 0x158
-  __DATA_CONST.__objc_superrefs: 0x708
+  __DATA_CONST.__objc_superrefs: 0x718
   __DATA_CONST.__objc_arraydata: 0x138
-  __AUTH_CONST.__auth_got: 0x2288
-  __AUTH_CONST.__const: 0x3e58
-  __AUTH_CONST.__cfstring: 0x17fc0
-  __AUTH_CONST.__objc_const: 0x22938
+  __AUTH_CONST.__auth_got: 0x2290
+  __AUTH_CONST.__const: 0x3e98
+  __AUTH_CONST.__cfstring: 0x18180
+  __AUTH_CONST.__objc_const: 0x22c40
   __AUTH_CONST.__objc_intobj: 0x390
   __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x1528
+  __AUTH.__objc_data: 0x1618
   __AUTH.__data: 0xd90
-  __DATA.__objc_ivar: 0x1b78
-  __DATA.__data: 0x1fa8
-  __DATA.__bss: 0x1488
+  __DATA.__objc_ivar: 0x1b98
+  __DATA.__data: 0x2008
+  __DATA.__bss: 0x1498
   __DATA.__common: 0x190
   __DATA_DIRTY.__objc_data: 0x6040
   __DATA_DIRTY.__bss: 0xf0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D0905FA4-CF33-349D-9C3B-6C10973E5A3C
-  Functions: 7898
-  Symbols:   22887
-  CStrings:  15828
+  UUID: 0C2FE64D-7763-31C3-A584-8FD7A68D0AFF
+  Functions: 7920
+  Symbols:   22980
+  CStrings:  15922
 
Symbols:
+ +[NEGuardProxyManager sharedManager]
+ -[NEFlowDivertFileHandle initFlowDivertControlSocketWithParams:isGuardProxy:order:]
+ -[NEFlowDivertFileHandle initGuardProxyFlowDivertControlSocket]
+ -[NEGuardProxy .cxx_destruct]
+ -[NEGuardProxy init]
+ -[NEGuardProxy startWithOptions:completionHandler:]
+ -[NEGuardProxy stop]
+ -[NEGuardProxyManager .cxx_destruct]
+ -[NEGuardProxyManager container:didFailWithError:]
+ -[NEGuardProxyManager container:didRequestFlowDivertControlSocketWithCompletionHandler:]
+ -[NEGuardProxyManager container:didSetTunnelConfiguration:completionHandler:]
+ -[NEGuardProxyManager container:didStartWithError:]
+ -[NEGuardProxyManager init]
+ -[NEGuardProxyManager start]
+ -[NEGuardProxyManager stopWithCompletionHandler:]
+ -[NEGuardProxyProvider handleNewFlow:]
+ -[NEGuardProxyProvider startProxyWithOptions:completionHandler:]
+ -[NEGuardProxyProvider stopProxyWithReason:completionHandler:]
+ -[NEPvDConfiguration proxyPolicyRuleCount]
+ -[NEPvDFetcher initWithDelegate:queue:url:identityRef:additionalHTTPHeaders:cachedPvDConfig:]
+ -[NEPvDFetcher scheduleNextFetchForExpiration:]
+ -[NEPvDFetcher setQueue:]
+ -[NERelayConfiguration cachedPvDConfig]
+ -[NERelayConfiguration setCachedPvDConfig:]
+ GCC_except_table1032
+ GCC_except_table1095
+ GCC_except_table1096
+ GCC_except_table1097
+ GCC_except_table1272
+ GCC_except_table1273
+ GCC_except_table1274
+ GCC_except_table1275
+ GCC_except_table1276
+ GCC_except_table1288
+ GCC_except_table1289
+ GCC_except_table1302
+ GCC_except_table131
+ GCC_except_table1313
+ GCC_except_table1314
+ GCC_except_table1439
+ GCC_except_table150
+ GCC_except_table1600
+ GCC_except_table1601
+ GCC_except_table1606
+ GCC_except_table1609
+ GCC_except_table1654
+ GCC_except_table1655
+ GCC_except_table1656
+ GCC_except_table1657
+ GCC_except_table1658
+ GCC_except_table1659
+ GCC_except_table1660
+ GCC_except_table1661
+ GCC_except_table1662
+ GCC_except_table1663
+ GCC_except_table1664
+ GCC_except_table1665
+ GCC_except_table1666
+ GCC_except_table1667
+ GCC_except_table1668
+ GCC_except_table1673
+ GCC_except_table1677
+ GCC_except_table1680
+ GCC_except_table1686
+ GCC_except_table1687
+ GCC_except_table1694
+ GCC_except_table1718
+ GCC_except_table1744
+ GCC_except_table1956
+ GCC_except_table271
+ GCC_except_table2862
+ GCC_except_table2872
+ GCC_except_table3106
+ GCC_except_table3111
+ GCC_except_table3117
+ GCC_except_table3120
+ GCC_except_table3135
+ GCC_except_table3136
+ GCC_except_table3137
+ GCC_except_table3152
+ GCC_except_table3166
+ GCC_except_table3209
+ GCC_except_table3213
+ GCC_except_table3259
+ GCC_except_table3310
+ GCC_except_table3371
+ GCC_except_table3390
+ GCC_except_table3399
+ GCC_except_table3401
+ GCC_except_table3420
+ GCC_except_table3421
+ GCC_except_table3422
+ GCC_except_table3433
+ GCC_except_table3440
+ GCC_except_table3479
+ GCC_except_table3485
+ GCC_except_table3487
+ GCC_except_table3522
+ GCC_except_table3524
+ GCC_except_table3525
+ GCC_except_table3614
+ GCC_except_table3641
+ GCC_except_table3883
+ GCC_except_table3890
+ GCC_except_table3891
+ GCC_except_table3892
+ GCC_except_table3893
+ GCC_except_table3895
+ GCC_except_table396
+ GCC_except_table398
+ GCC_except_table3986
+ GCC_except_table4154
+ GCC_except_table4165
+ GCC_except_table4186
+ GCC_except_table4187
+ GCC_except_table4188
+ GCC_except_table4189
+ GCC_except_table4190
+ GCC_except_table4191
+ GCC_except_table4192
+ GCC_except_table4193
+ GCC_except_table4194
+ GCC_except_table4198
+ GCC_except_table4203
+ GCC_except_table4204
+ GCC_except_table4210
+ GCC_except_table4217
+ GCC_except_table4218
+ GCC_except_table4290
+ GCC_except_table4291
+ GCC_except_table4299
+ GCC_except_table4392
+ GCC_except_table4393
+ GCC_except_table4394
+ GCC_except_table4395
+ GCC_except_table4396
+ GCC_except_table4397
+ GCC_except_table4399
+ GCC_except_table4481
+ GCC_except_table4624
+ GCC_except_table4628
+ GCC_except_table465
+ GCC_except_table4672
+ GCC_except_table4676
+ GCC_except_table4688
+ GCC_except_table4708
+ GCC_except_table4710
+ GCC_except_table4716
+ GCC_except_table4718
+ GCC_except_table4810
+ GCC_except_table4879
+ GCC_except_table4900
+ GCC_except_table4913
+ GCC_except_table5010
+ GCC_except_table5015
+ GCC_except_table5056
+ GCC_except_table5102
+ GCC_except_table5104
+ GCC_except_table5168
+ GCC_except_table5171
+ GCC_except_table5207
+ GCC_except_table5227
+ GCC_except_table5229
+ GCC_except_table5231
+ GCC_except_table5239
+ GCC_except_table5278
+ GCC_except_table5279
+ GCC_except_table5281
+ GCC_except_table5283
+ GCC_except_table5286
+ GCC_except_table5332
+ GCC_except_table5354
+ GCC_except_table5357
+ GCC_except_table5433
+ GCC_except_table548
+ GCC_except_table549
+ GCC_except_table550
+ GCC_except_table551
+ GCC_except_table552
+ GCC_except_table563
+ GCC_except_table564
+ GCC_except_table571
+ GCC_except_table5760
+ GCC_except_table578
+ GCC_except_table579
+ GCC_except_table5796
+ GCC_except_table5797
+ GCC_except_table5800
+ GCC_except_table5865
+ GCC_except_table5871
+ GCC_except_table5872
+ GCC_except_table5880
+ GCC_except_table5908
+ GCC_except_table5909
+ GCC_except_table5910
+ GCC_except_table5912
+ GCC_except_table5913
+ GCC_except_table5915
+ GCC_except_table5919
+ GCC_except_table5920
+ GCC_except_table5927
+ GCC_except_table5936
+ GCC_except_table5939
+ GCC_except_table5943
+ GCC_except_table6020
+ GCC_except_table6021
+ GCC_except_table6150
+ GCC_except_table6151
+ GCC_except_table6152
+ GCC_except_table6153
+ GCC_except_table6155
+ GCC_except_table6156
+ GCC_except_table6157
+ GCC_except_table6158
+ GCC_except_table6162
+ GCC_except_table6163
+ GCC_except_table6164
+ GCC_except_table6165
+ GCC_except_table6167
+ GCC_except_table6168
+ GCC_except_table6169
+ GCC_except_table6170
+ GCC_except_table6179
+ GCC_except_table6184
+ GCC_except_table6185
+ GCC_except_table6186
+ GCC_except_table6191
+ GCC_except_table6217
+ GCC_except_table6294
+ GCC_except_table6295
+ GCC_except_table6296
+ GCC_except_table6297
+ GCC_except_table670
+ GCC_except_table742
+ GCC_except_table796
+ GCC_except_table814
+ GCC_except_table820
+ GCC_except_table821
+ GCC_except_table822
+ GCC_except_table823
+ GCC_except_table851
+ GCC_except_table890
+ GCC_except_table895
+ GCC_except_table897
+ GCC_except_table898
+ GCC_except_table899
+ GCC_except_table900
+ GCC_except_table943
+ _NEFlowDirectorSetCFILVerdictCallback
+ _OBJC_CLASS_$_NEGuardProxy
+ _OBJC_CLASS_$_NEGuardProxyManager
+ _OBJC_CLASS_$_NEGuardProxyProvider
+ _OBJC_IVAR_$_NEAppProxyFlow._guard_proxy_completion_handler
+ _OBJC_IVAR_$_NEAppProxyProviderContainer._guardProxyFlows
+ _OBJC_IVAR_$_NEGuardProxy._flowDivertControlHandle
+ _OBJC_IVAR_$_NEGuardProxy._policyIDs
+ _OBJC_IVAR_$_NEGuardProxy._session
+ _OBJC_IVAR_$_NEGuardProxy._started
+ _OBJC_IVAR_$_NEGuardProxyManager._guardProxy
+ _OBJC_IVAR_$_NERelayConfiguration._cachedPvDConfig
+ _OBJC_METACLASS_$_NEGuardProxy
+ _OBJC_METACLASS_$_NEGuardProxyManager
+ _OBJC_METACLASS_$_NEGuardProxyProvider
+ __OBJC_$_CLASS_METHODS_NEGuardProxyManager
+ __OBJC_$_INSTANCE_METHODS_NEGuardProxy
+ __OBJC_$_INSTANCE_METHODS_NEGuardProxyManager
+ __OBJC_$_INSTANCE_METHODS_NEGuardProxyProvider
+ __OBJC_$_INSTANCE_VARIABLES_NEGuardProxy
+ __OBJC_$_INSTANCE_VARIABLES_NEGuardProxyManager
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NEAppProxyProviderContainerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NEAppProxyProviderContainerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_NEGuardProxyManager
+ __OBJC_CLASS_RO_$_NEGuardProxy
+ __OBJC_CLASS_RO_$_NEGuardProxyManager
+ __OBJC_CLASS_RO_$_NEGuardProxyProvider
+ __OBJC_LABEL_PROTOCOL_$_NEAppProxyProviderContainerDelegate
+ __OBJC_METACLASS_RO_$_NEGuardProxy
+ __OBJC_METACLASS_RO_$_NEGuardProxyManager
+ __OBJC_METACLASS_RO_$_NEGuardProxyProvider
+ __OBJC_PROTOCOL_$_NEAppProxyProviderContainerDelegate
+ ___28-[NEGuardProxyManager start]_block_invoke
+ ___36+[NEGuardProxyManager sharedManager]_block_invoke
+ ___57-[NERelayManager saveToPreferencesWithCompletionHandler:]_block_invoke.75
+ ___61-[NERelayManager removeFromPreferencesWithCompletionHandler:]_block_invoke.74
+ ___65-[NEAppProxyProviderContainer setInitialFlowDivertControlSocket:]_block_invoke.10
+ ___65-[NEAppProxyProviderContainer setInitialFlowDivertControlSocket:]_block_invoke_2.12
+ ___93-[NEPvDFetcher initWithDelegate:queue:url:identityRef:additionalHTTPHeaders:cachedPvDConfig:]_block_invoke
+ ___Block_byref_object_copy_.12748
+ ___Block_byref_object_copy_.15201
+ ___Block_byref_object_copy_.171
+ ___Block_byref_object_copy_.20595
+ ___Block_byref_object_copy_.21863
+ ___Block_byref_object_copy_.22912
+ ___Block_byref_object_copy_.24051
+ ___Block_byref_object_copy_.24769
+ ___Block_byref_object_copy_.27424
+ ___Block_byref_object_copy_.28598
+ ___Block_byref_object_copy_.7096
+ ___Block_byref_object_copy_.9671
+ ___Block_byref_object_dispose_.12749
+ ___Block_byref_object_dispose_.15202
+ ___Block_byref_object_dispose_.172
+ ___Block_byref_object_dispose_.20596
+ ___Block_byref_object_dispose_.21864
+ ___Block_byref_object_dispose_.22913
+ ___Block_byref_object_dispose_.24052
+ ___Block_byref_object_dispose_.24770
+ ___Block_byref_object_dispose_.27425
+ ___Block_byref_object_dispose_.28599
+ ___Block_byref_object_dispose_.7097
+ ___Block_byref_object_dispose_.9672
+ ___block_descriptor_tmp.19801
+ ___block_descriptor_tmp.23604
+ ___block_descriptor_tmp.25650
+ ___block_descriptor_tmp.26256
+ ___block_literal_global.10.15795
+ ___block_literal_global.10.9335
+ ___block_literal_global.10280
+ ___block_literal_global.1130
+ ___block_literal_global.13033
+ ___block_literal_global.13405
+ ___block_literal_global.14.22375
+ ___block_literal_global.14366
+ ___block_literal_global.14531
+ ___block_literal_global.1472
+ ___block_literal_global.15.25880
+ ___block_literal_global.15203
+ ___block_literal_global.15797
+ ___block_literal_global.16382
+ ___block_literal_global.16625
+ ___block_literal_global.17.14379
+ ___block_literal_global.17.18095
+ ___block_literal_global.17113
+ ___block_literal_global.17970
+ ___block_literal_global.18104
+ ___block_literal_global.18409
+ ___block_literal_global.1884
+ ___block_literal_global.19710
+ ___block_literal_global.20.18101
+ ___block_literal_global.20385
+ ___block_literal_global.2086
+ ___block_literal_global.20899
+ ___block_literal_global.21960
+ ___block_literal_global.2230
+ ___block_literal_global.22380
+ ___block_literal_global.2249
+ ___block_literal_global.22777
+ ___block_literal_global.2346
+ ___block_literal_global.23518
+ ___block_literal_global.23602
+ ___block_literal_global.24154
+ ___block_literal_global.24266
+ ___block_literal_global.24309
+ ___block_literal_global.24504
+ ___block_literal_global.24686
+ ___block_literal_global.2506
+ ___block_literal_global.25597
+ ___block_literal_global.25648
+ ___block_literal_global.25884
+ ___block_literal_global.25979
+ ___block_literal_global.2624
+ ___block_literal_global.26362
+ ___block_literal_global.26917
+ ___block_literal_global.27005
+ ___block_literal_global.27152
+ ___block_literal_global.27390
+ ___block_literal_global.27936
+ ___block_literal_global.28.27428
+ ___block_literal_global.2823
+ ___block_literal_global.28650
+ ___block_literal_global.2968
+ ___block_literal_global.3091
+ ___block_literal_global.3183
+ ___block_literal_global.3457
+ ___block_literal_global.3729
+ ___block_literal_global.3810
+ ___block_literal_global.4.14369
+ ___block_literal_global.4238
+ ___block_literal_global.4324
+ ___block_literal_global.4698
+ ___block_literal_global.4998
+ ___block_literal_global.5
+ ___block_literal_global.5644
+ ___block_literal_global.63.20380
+ ___block_literal_global.63.3178
+ ___block_literal_global.63.4993
+ ___block_literal_global.69.2081
+ ___block_literal_global.69.3724
+ ___block_literal_global.69.3805
+ ___block_literal_global.7.25588
+ ___block_literal_global.7125
+ ___block_literal_global.73.25974
+ ___block_literal_global.7353
+ ___block_literal_global.75.4233
+ ___block_literal_global.75.4319
+ ___block_literal_global.7540
+ ___block_literal_global.7963
+ ___block_literal_global.8087
+ ___block_literal_global.9333
+ __extensionAuxiliaryHostProtocol.protocol.20381
+ __extensionAuxiliaryHostProtocol.protocol.2082
+ __extensionAuxiliaryHostProtocol.protocol.24310
+ __extensionAuxiliaryHostProtocol.protocol.2503
+ __extensionAuxiliaryHostProtocol.protocol.25975
+ __extensionAuxiliaryHostProtocol.protocol.2621
+ __extensionAuxiliaryHostProtocol.protocol.2820
+ __extensionAuxiliaryHostProtocol.protocol.2965
+ __extensionAuxiliaryHostProtocol.protocol.3088
+ __extensionAuxiliaryHostProtocol.protocol.3179
+ __extensionAuxiliaryHostProtocol.protocol.3725
+ __extensionAuxiliaryHostProtocol.protocol.3806
+ __extensionAuxiliaryHostProtocol.protocol.4234
+ __extensionAuxiliaryHostProtocol.protocol.4320
+ __extensionAuxiliaryHostProtocol.protocol.4695
+ __extensionAuxiliaryHostProtocol.protocol.4994
+ __extensionAuxiliaryHostProtocol.protocolInit.20379
+ __extensionAuxiliaryHostProtocol.protocolInit.2080
+ __extensionAuxiliaryHostProtocol.protocolInit.24308
+ __extensionAuxiliaryHostProtocol.protocolInit.2502
+ __extensionAuxiliaryHostProtocol.protocolInit.25973
+ __extensionAuxiliaryHostProtocol.protocolInit.2620
+ __extensionAuxiliaryHostProtocol.protocolInit.2819
+ __extensionAuxiliaryHostProtocol.protocolInit.2964
+ __extensionAuxiliaryHostProtocol.protocolInit.3087
+ __extensionAuxiliaryHostProtocol.protocolInit.3177
+ __extensionAuxiliaryHostProtocol.protocolInit.3723
+ __extensionAuxiliaryHostProtocol.protocolInit.3804
+ __extensionAuxiliaryHostProtocol.protocolInit.4232
+ __extensionAuxiliaryHostProtocol.protocolInit.4318
+ __extensionAuxiliaryHostProtocol.protocolInit.4694
+ __extensionAuxiliaryHostProtocol.protocolInit.4992
+ __extensionAuxiliaryVendorProtocol.protocol.20386
+ __extensionAuxiliaryVendorProtocol.protocol.2087
+ __extensionAuxiliaryVendorProtocol.protocol.2250
+ __extensionAuxiliaryVendorProtocol.protocol.2347
+ __extensionAuxiliaryVendorProtocol.protocol.2507
+ __extensionAuxiliaryVendorProtocol.protocol.25980
+ __extensionAuxiliaryVendorProtocol.protocol.2625
+ __extensionAuxiliaryVendorProtocol.protocol.2824
+ __extensionAuxiliaryVendorProtocol.protocol.2969
+ __extensionAuxiliaryVendorProtocol.protocol.3092
+ __extensionAuxiliaryVendorProtocol.protocol.3184
+ __extensionAuxiliaryVendorProtocol.protocol.3730
+ __extensionAuxiliaryVendorProtocol.protocol.3811
+ __extensionAuxiliaryVendorProtocol.protocol.4239
+ __extensionAuxiliaryVendorProtocol.protocol.4325
+ __extensionAuxiliaryVendorProtocol.protocol.4699
+ __extensionAuxiliaryVendorProtocol.protocol.4999
+ __extensionAuxiliaryVendorProtocol.protocolInit.20384
+ __extensionAuxiliaryVendorProtocol.protocolInit.2085
+ __extensionAuxiliaryVendorProtocol.protocolInit.2248
+ __extensionAuxiliaryVendorProtocol.protocolInit.2345
+ __extensionAuxiliaryVendorProtocol.protocolInit.2505
+ __extensionAuxiliaryVendorProtocol.protocolInit.25978
+ __extensionAuxiliaryVendorProtocol.protocolInit.2623
+ __extensionAuxiliaryVendorProtocol.protocolInit.2822
+ __extensionAuxiliaryVendorProtocol.protocolInit.2967
+ __extensionAuxiliaryVendorProtocol.protocolInit.3090
+ __extensionAuxiliaryVendorProtocol.protocolInit.3182
+ __extensionAuxiliaryVendorProtocol.protocolInit.3728
+ __extensionAuxiliaryVendorProtocol.protocolInit.3809
+ __extensionAuxiliaryVendorProtocol.protocolInit.4237
+ __extensionAuxiliaryVendorProtocol.protocolInit.4323
+ __extensionAuxiliaryVendorProtocol.protocolInit.4697
+ __extensionAuxiliaryVendorProtocol.protocolInit.4997
+ _block_copy_helper.76
+ _block_copy_helper.84
+ _block_copy_helper.90
+ _block_descriptor.78
+ _block_descriptor.86
+ _block_descriptor.92
+ _block_destroy_helper.77
+ _block_destroy_helper.85
+ _block_destroy_helper.91
+ _convert_error_to_string.24764
+ _driverInterface.driverInterface.10277
+ _driverInterface.driverInterface.17114
+ _driverInterface.driverInterface.20896
+ _driverInterface.driverInterface.22376
+ _driverInterface.driverInterface.7533
+ _driverInterface.onceToken.10276
+ _driverInterface.onceToken.17112
+ _driverInterface.onceToken.20895
+ _driverInterface.onceToken.22374
+ _driverInterface.onceToken.7532
+ _g_noAppFilter.28572
+ _globalConfigurationManager.gChangeQueue.18099
+ _globalConfigurationManager.gChangeQueue.5642
+ _globalConfigurationManager.gConfigurationManager.18096
+ _globalConfigurationManager.gConfigurationManager.5640
+ _globalConfigurationManager.onceToken.18094
+ _globalConfigurationManager.onceToken.5639
+ _initGlobals.onceToken.16624
+ _loadedManagers.loadedManagers.27388
+ _loadedManagers.loadedManagers.28575
+ _loadedManagers.managers_init.27387
+ _loadedManagers.managers_init.28574
+ _managerInterface.managerInterface.10281
+ _managerInterface.managerInterface.20900
+ _managerInterface.managerInterface.22381
+ _managerInterface.onceToken.10279
+ _managerInterface.onceToken.20898
+ _managerInterface.onceToken.22379
+ _objc_msgSend$allowsUnsafeSocketAccess
+ _objc_msgSend$bundleWithIdentifier:
+ _objc_msgSend$cachedPvDConfig
+ _objc_msgSend$dataWithJSONObject:options:error:
+ _objc_msgSend$initFlowDivertControlSocketWithParams:isGuardProxy:order:
+ _objc_msgSend$initGuardProxyFlowDivertControlSocket
+ _objc_msgSend$initWithDelegate:providerClass:
+ _objc_msgSend$isInbound
+ _objc_msgSend$localizedStringForKey:value:table:
+ _objc_msgSend$setCachedPvDConfig:
+ _objectdestroy.20Tm
+ _objectdestroy.94Tm
+ _objectdestroyTm
+ _sharedManager.g_manager.27006
+ _sharedManager.g_manager.7354
+ _sharedManager.g_manager.7964
+ _sharedManager.init_manager.7352
+ _sharedManager.init_manager.7962
+ _sharedManager.onceToken.18103
+ _sharedManager.onceToken.27004
+ _sharedManager.onceToken.28649
+ _sharedManager.onceToken.5643
- -[NEFlowDivertFileHandle initFlowDivertControlSocketWithParams:order:]
- -[NEPvDFetcher initWithDelegate:queue:url:identityRef:additionalHTTPHeaders:]
- GCC_except_table1026
- GCC_except_table1083
- GCC_except_table1084
- GCC_except_table1091
- GCC_except_table1259
- GCC_except_table1260
- GCC_except_table1263
- GCC_except_table1264
- GCC_except_table1267
- GCC_except_table1268
- GCC_except_table1282
- GCC_except_table1296
- GCC_except_table130
- GCC_except_table1307
- GCC_except_table1308
- GCC_except_table1433
- GCC_except_table149
- GCC_except_table1558
- GCC_except_table1559
- GCC_except_table1564
- GCC_except_table1567
- GCC_except_table1612
- GCC_except_table1613
- GCC_except_table1614
- GCC_except_table1615
- GCC_except_table1616
- GCC_except_table1617
- GCC_except_table1618
- GCC_except_table1619
- GCC_except_table1620
- GCC_except_table1621
- GCC_except_table1622
- GCC_except_table1623
- GCC_except_table1624
- GCC_except_table1625
- GCC_except_table1626
- GCC_except_table1631
- GCC_except_table1635
- GCC_except_table1638
- GCC_except_table1644
- GCC_except_table1645
- GCC_except_table1652
- GCC_except_table1676
- GCC_except_table1702
- GCC_except_table1914
- GCC_except_table270
- GCC_except_table2820
- GCC_except_table2830
- GCC_except_table3064
- GCC_except_table3069
- GCC_except_table3075
- GCC_except_table3078
- GCC_except_table3093
- GCC_except_table3094
- GCC_except_table3095
- GCC_except_table3110
- GCC_except_table3124
- GCC_except_table3125
- GCC_except_table3171
- GCC_except_table3217
- GCC_except_table3268
- GCC_except_table3329
- GCC_except_table3348
- GCC_except_table3357
- GCC_except_table3359
- GCC_except_table3378
- GCC_except_table3379
- GCC_except_table3380
- GCC_except_table3391
- GCC_except_table3398
- GCC_except_table3437
- GCC_except_table3443
- GCC_except_table3445
- GCC_except_table3480
- GCC_except_table3482
- GCC_except_table3483
- GCC_except_table3572
- GCC_except_table3599
- GCC_except_table3838
- GCC_except_table3845
- GCC_except_table3846
- GCC_except_table3847
- GCC_except_table3848
- GCC_except_table3850
- GCC_except_table3941
- GCC_except_table395
- GCC_except_table397
- GCC_except_table4107
- GCC_except_table4118
- GCC_except_table4124
- GCC_except_table4139
- GCC_except_table4140
- GCC_except_table4141
- GCC_except_table4142
- GCC_except_table4143
- GCC_except_table4144
- GCC_except_table4145
- GCC_except_table4146
- GCC_except_table4147
- GCC_except_table4151
- GCC_except_table4156
- GCC_except_table4157
- GCC_except_table4163
- GCC_except_table4170
- GCC_except_table4243
- GCC_except_table4244
- GCC_except_table4252
- GCC_except_table4345
- GCC_except_table4346
- GCC_except_table4347
- GCC_except_table4348
- GCC_except_table4349
- GCC_except_table4350
- GCC_except_table4352
- GCC_except_table4434
- GCC_except_table4610
- GCC_except_table4612
- GCC_except_table464
- GCC_except_table4648
- GCC_except_table4658
- GCC_except_table4674
- GCC_except_table4694
- GCC_except_table4696
- GCC_except_table4702
- GCC_except_table4704
- GCC_except_table4796
- GCC_except_table4865
- GCC_except_table4886
- GCC_except_table4899
- GCC_except_table4996
- GCC_except_table5001
- GCC_except_table5042
- GCC_except_table5088
- GCC_except_table5090
- GCC_except_table5154
- GCC_except_table5157
- GCC_except_table5193
- GCC_except_table5213
- GCC_except_table5215
- GCC_except_table5217
- GCC_except_table5225
- GCC_except_table5264
- GCC_except_table5265
- GCC_except_table5267
- GCC_except_table5269
- GCC_except_table5272
- GCC_except_table5316
- GCC_except_table5338
- GCC_except_table5341
- GCC_except_table541
- GCC_except_table5417
- GCC_except_table542
- GCC_except_table543
- GCC_except_table544
- GCC_except_table545
- GCC_except_table553
- GCC_except_table559
- GCC_except_table566
- GCC_except_table573
- GCC_except_table574
- GCC_except_table5746
- GCC_except_table5782
- GCC_except_table5783
- GCC_except_table5786
- GCC_except_table5840
- GCC_except_table5846
- GCC_except_table5847
- GCC_except_table5855
- GCC_except_table5858
- GCC_except_table5868
- GCC_except_table5884
- GCC_except_table5885
- GCC_except_table5886
- GCC_except_table5887
- GCC_except_table5888
- GCC_except_table5889
- GCC_except_table5890
- GCC_except_table5894
- GCC_except_table5895
- GCC_except_table5902
- GCC_except_table5995
- GCC_except_table5996
- GCC_except_table6125
- GCC_except_table6126
- GCC_except_table6127
- GCC_except_table6128
- GCC_except_table6129
- GCC_except_table6130
- GCC_except_table6131
- GCC_except_table6132
- GCC_except_table6133
- GCC_except_table6134
- GCC_except_table6135
- GCC_except_table6136
- GCC_except_table6137
- GCC_except_table6138
- GCC_except_table6139
- GCC_except_table6140
- GCC_except_table6141
- GCC_except_table6142
- GCC_except_table6143
- GCC_except_table6144
- GCC_except_table6145
- GCC_except_table6192
- GCC_except_table6269
- GCC_except_table6270
- GCC_except_table6271
- GCC_except_table6272
- GCC_except_table665
- GCC_except_table732
- GCC_except_table786
- GCC_except_table809
- GCC_except_table815
- GCC_except_table816
- GCC_except_table817
- GCC_except_table818
- GCC_except_table846
- GCC_except_table884
- GCC_except_table885
- GCC_except_table886
- GCC_except_table887
- GCC_except_table888
- GCC_except_table889
- GCC_except_table937
- ___57-[NERelayManager saveToPreferencesWithCompletionHandler:]_block_invoke.42
- ___61-[NERelayManager removeFromPreferencesWithCompletionHandler:]_block_invoke.41
- ___65-[NEAppProxyProviderContainer setInitialFlowDivertControlSocket:]_block_invoke.7
- ___77-[NEPvDFetcher initWithDelegate:queue:url:identityRef:additionalHTTPHeaders:]_block_invoke
- ___Block_byref_object_copy_.12496
- ___Block_byref_object_copy_.14946
- ___Block_byref_object_copy_.170
- ___Block_byref_object_copy_.20472
- ___Block_byref_object_copy_.21748
- ___Block_byref_object_copy_.22796
- ___Block_byref_object_copy_.23937
- ___Block_byref_object_copy_.24640
- ___Block_byref_object_copy_.27260
- ___Block_byref_object_copy_.28435
- ___Block_byref_object_copy_.6848
- ___Block_byref_object_copy_.9420
- ___Block_byref_object_dispose_.12497
- ___Block_byref_object_dispose_.14947
- ___Block_byref_object_dispose_.171
- ___Block_byref_object_dispose_.20473
- ___Block_byref_object_dispose_.21749
- ___Block_byref_object_dispose_.22797
- ___Block_byref_object_dispose_.23938
- ___Block_byref_object_dispose_.24641
- ___Block_byref_object_dispose_.27261
- ___Block_byref_object_dispose_.28436
- ___Block_byref_object_dispose_.6849
- ___Block_byref_object_dispose_.9421
- ___block_descriptor_tmp.19513
- ___block_descriptor_tmp.23490
- ___block_descriptor_tmp.25523
- ___block_descriptor_tmp.26138
- ___block_literal_global.10.15540
- ___block_literal_global.10.9084
- ___block_literal_global.10029
- ___block_literal_global.1129
- ___block_literal_global.12780
- ___block_literal_global.13152
- ___block_literal_global.14.22259
- ___block_literal_global.14112
- ___block_literal_global.1422
- ___block_literal_global.14277
- ___block_literal_global.14948
- ___block_literal_global.15.25753
- ___block_literal_global.15542
- ___block_literal_global.16105
- ___block_literal_global.16348
- ___block_literal_global.16836
- ___block_literal_global.17.14125
- ___block_literal_global.17.17805
- ___block_literal_global.17680
- ___block_literal_global.17814
- ___block_literal_global.18122
- ___block_literal_global.1831
- ___block_literal_global.19422
- ___block_literal_global.20.17811
- ___block_literal_global.20279
- ___block_literal_global.2030
- ___block_literal_global.20787
- ___block_literal_global.2173
- ___block_literal_global.21845
- ___block_literal_global.2192
- ___block_literal_global.22264
- ___block_literal_global.22661
- ___block_literal_global.2289
- ___block_literal_global.23404
- ___block_literal_global.23488
- ___block_literal_global.24040
- ___block_literal_global.24152
- ___block_literal_global.24186
- ___block_literal_global.24380
- ___block_literal_global.2449
- ___block_literal_global.24562
- ___block_literal_global.25470
- ___block_literal_global.25521
- ___block_literal_global.2567
- ___block_literal_global.25757
- ___block_literal_global.25861
- ___block_literal_global.26244
- ___block_literal_global.26799
- ___block_literal_global.26988
- ___block_literal_global.27226
- ___block_literal_global.2767
- ___block_literal_global.27772
- ___block_literal_global.28.27264
- ___block_literal_global.28454
- ___block_literal_global.2911
- ___block_literal_global.3034
- ___block_literal_global.3126
- ___block_literal_global.3399
- ___block_literal_global.3672
- ___block_literal_global.3753
- ___block_literal_global.4.14115
- ___block_literal_global.4181
- ___block_literal_global.4267
- ___block_literal_global.4641
- ___block_literal_global.4942
- ___block_literal_global.5581
- ___block_literal_global.63.20274
- ___block_literal_global.63.3121
- ___block_literal_global.63.4937
- ___block_literal_global.6877
- ___block_literal_global.69.2025
- ___block_literal_global.69.3667
- ___block_literal_global.69.3748
- ___block_literal_global.7.25461
- ___block_literal_global.7105
- ___block_literal_global.7292
- ___block_literal_global.73.25856
- ___block_literal_global.75.4176
- ___block_literal_global.75.4262
- ___block_literal_global.7711
- ___block_literal_global.7835
- ___block_literal_global.9082
- __extensionAuxiliaryHostProtocol.protocol.2026
- __extensionAuxiliaryHostProtocol.protocol.20275
- __extensionAuxiliaryHostProtocol.protocol.24187
- __extensionAuxiliaryHostProtocol.protocol.2446
- __extensionAuxiliaryHostProtocol.protocol.2564
- __extensionAuxiliaryHostProtocol.protocol.25857
- __extensionAuxiliaryHostProtocol.protocol.2764
- __extensionAuxiliaryHostProtocol.protocol.2908
- __extensionAuxiliaryHostProtocol.protocol.3031
- __extensionAuxiliaryHostProtocol.protocol.3122
- __extensionAuxiliaryHostProtocol.protocol.3668
- __extensionAuxiliaryHostProtocol.protocol.3749
- __extensionAuxiliaryHostProtocol.protocol.4177
- __extensionAuxiliaryHostProtocol.protocol.4263
- __extensionAuxiliaryHostProtocol.protocol.4638
- __extensionAuxiliaryHostProtocol.protocol.4938
- __extensionAuxiliaryHostProtocol.protocolInit.2024
- __extensionAuxiliaryHostProtocol.protocolInit.20273
- __extensionAuxiliaryHostProtocol.protocolInit.24185
- __extensionAuxiliaryHostProtocol.protocolInit.2445
- __extensionAuxiliaryHostProtocol.protocolInit.2563
- __extensionAuxiliaryHostProtocol.protocolInit.25855
- __extensionAuxiliaryHostProtocol.protocolInit.2763
- __extensionAuxiliaryHostProtocol.protocolInit.2907
- __extensionAuxiliaryHostProtocol.protocolInit.3030
- __extensionAuxiliaryHostProtocol.protocolInit.3120
- __extensionAuxiliaryHostProtocol.protocolInit.3666
- __extensionAuxiliaryHostProtocol.protocolInit.3747
- __extensionAuxiliaryHostProtocol.protocolInit.4175
- __extensionAuxiliaryHostProtocol.protocolInit.4261
- __extensionAuxiliaryHostProtocol.protocolInit.4637
- __extensionAuxiliaryHostProtocol.protocolInit.4936
- __extensionAuxiliaryVendorProtocol.protocol.20280
- __extensionAuxiliaryVendorProtocol.protocol.2031
- __extensionAuxiliaryVendorProtocol.protocol.2193
- __extensionAuxiliaryVendorProtocol.protocol.2290
- __extensionAuxiliaryVendorProtocol.protocol.2450
- __extensionAuxiliaryVendorProtocol.protocol.2568
- __extensionAuxiliaryVendorProtocol.protocol.25862
- __extensionAuxiliaryVendorProtocol.protocol.2768
- __extensionAuxiliaryVendorProtocol.protocol.2912
- __extensionAuxiliaryVendorProtocol.protocol.3035
- __extensionAuxiliaryVendorProtocol.protocol.3127
- __extensionAuxiliaryVendorProtocol.protocol.3673
- __extensionAuxiliaryVendorProtocol.protocol.3754
- __extensionAuxiliaryVendorProtocol.protocol.4182
- __extensionAuxiliaryVendorProtocol.protocol.4268
- __extensionAuxiliaryVendorProtocol.protocol.4642
- __extensionAuxiliaryVendorProtocol.protocol.4943
- __extensionAuxiliaryVendorProtocol.protocolInit.20278
- __extensionAuxiliaryVendorProtocol.protocolInit.2029
- __extensionAuxiliaryVendorProtocol.protocolInit.2191
- __extensionAuxiliaryVendorProtocol.protocolInit.2288
- __extensionAuxiliaryVendorProtocol.protocolInit.2448
- __extensionAuxiliaryVendorProtocol.protocolInit.2566
- __extensionAuxiliaryVendorProtocol.protocolInit.25860
- __extensionAuxiliaryVendorProtocol.protocolInit.2766
- __extensionAuxiliaryVendorProtocol.protocolInit.2910
- __extensionAuxiliaryVendorProtocol.protocolInit.3033
- __extensionAuxiliaryVendorProtocol.protocolInit.3125
- __extensionAuxiliaryVendorProtocol.protocolInit.3671
- __extensionAuxiliaryVendorProtocol.protocolInit.3752
- __extensionAuxiliaryVendorProtocol.protocolInit.4180
- __extensionAuxiliaryVendorProtocol.protocolInit.4266
- __extensionAuxiliaryVendorProtocol.protocolInit.4640
- __extensionAuxiliaryVendorProtocol.protocolInit.4941
- _block_copy_helper.23
- _block_copy_helper.36
- _block_copy_helper.59
- _block_copy_helper.65
- _block_copy_helper.85
- _block_descriptor.25
- _block_descriptor.38
- _block_descriptor.61
- _block_descriptor.67
- _block_descriptor.87
- _block_destroy_helper.24
- _block_destroy_helper.37
- _block_destroy_helper.60
- _block_destroy_helper.66
- _block_destroy_helper.86
- _convert_error_to_string.24635
- _driverInterface.driverInterface.10026
- _driverInterface.driverInterface.16837
- _driverInterface.driverInterface.20784
- _driverInterface.driverInterface.22260
- _driverInterface.driverInterface.7285
- _driverInterface.onceToken.10025
- _driverInterface.onceToken.16835
- _driverInterface.onceToken.20783
- _driverInterface.onceToken.22258
- _driverInterface.onceToken.7284
- _g_noAppFilter.28409
- _globalConfigurationManager.gChangeQueue.17809
- _globalConfigurationManager.gChangeQueue.5579
- _globalConfigurationManager.gConfigurationManager.17806
- _globalConfigurationManager.gConfigurationManager.5577
- _globalConfigurationManager.onceToken.17804
- _globalConfigurationManager.onceToken.5576
- _initGlobals.onceToken.16347
- _loadedManagers.loadedManagers.27224
- _loadedManagers.loadedManagers.28412
- _loadedManagers.managers_init.27223
- _loadedManagers.managers_init.28411
- _managerInterface.managerInterface.10030
- _managerInterface.managerInterface.20788
- _managerInterface.managerInterface.22265
- _managerInterface.onceToken.10028
- _managerInterface.onceToken.20786
- _managerInterface.onceToken.22263
- _objc_msgSend$initFlowDivertControlSocketWithParams:order:
- _objectdestroy.27Tm
- _objectdestroy.31Tm
- _objectdestroy.40Tm
- _objectdestroy.44Tm
- _sharedManager.g_manager.7106
- _sharedManager.g_manager.7712
- _sharedManager.init_manager.7104
- _sharedManager.init_manager.7710
- _sharedManager.onceToken.17813
- _sharedManager.onceToken.28453
- _sharedManager.onceToken.5580
CStrings:
+ "%@ NEGuardProxy has already been started, ignoring the start request"
+ "%@: NEGuardProxy failed to remove policies from session %@"
+ "%@: NEGuardProxy failed to remove policy with id: %zu from session %@"
+ "%@: NEGuardProxy flowDivertControlHandle: %d"
+ "%@: NEGuardProxy has stopped and removed all policies."
+ "%@: NEGuardProxy starting with options: %@."
+ "%@: NEGuardProxy stopping."
+ "%@: NEGuardProxy unable to add filter policy to the policy session %@"
+ "%@: NEGuardProxy unable to add skip policy to the policy session %@"
+ "%@: NEGuardProxy unable to apply policies to the policy session %@"
+ "%@: NEGuardProxy unable to apply remove all policies to the policy session %@"
+ "%@: NEGuardProxy: Creating a new flow divert control socket"
+ "%@: NEGuardProxy: Creating a new policy session"
+ "%@: NEGuardProxy: Failed to create a flow divert control socket"
+ "%@: NEGuardProxyProvider didFailWithError called with: %@"
+ "%@: NEGuardProxyProvider failed to start with error: %@"
+ "%@: NEGuardProxyProvider started successfully"
+ "%@: NEGuardProxyProvider: handleCFILVerdict: (%@)"
+ "%@: NEGuardProxyProvider: handleNewFlow: (%@)"
+ "%@: NEGuardProxyProvider: handleNewFlowAsync: (%@)"
+ "%@: NEGuardProxyProvider: starting with options %@"
+ "%@: NEGuardProxyProvider: stopping with reason %ld"
+ "%@: No control socket to qualify flow"
+ "%@: Write operation on the control socket failed while qualifying flow (%s)"
+ "%@: failed to init, providerClass is not a NEGuardProxyProvider or a subclass of NEAppProxyProvider"
+ "%@: flowDivertCFILVerdict called for non GuardProxyProvider"
+ "%@: flowDivertCFILVerdict didn't find the flow: %u."
+ "%@: flowDivertCFILVerdict is called."
+ "%@: handleNewFlowAsync with %@ and flow_id: %u"
+ "%@: no flow found for flow qualification"
+ "%@: qualifying flow"
+ "%sclient-flags:0x%x"
+ "-[NEPvDFetcher initWithDelegate:queue:url:identityRef:additionalHTTPHeaders:cachedPvDConfig:]"
+ "@\"NEGuardProxy\""
+ "@28@0:8B16B20i24"
+ "@64@0:8@16@24@32^{__SecIdentity=}40@48@56"
+ "CachedPvD"
+ "Guard proxy is already running. Skipping start sequence."
+ "NEAppProxyProviderContainerDelegate"
+ "NEGuardProxy"
+ "NEGuardProxy stopped (%@)"
+ "NEGuardProxyManager"
+ "NEGuardProxyManager: sharedManager called"
+ "NEGuardProxyManager: start called"
+ "NEGuardProxyManager: stopping guard proxy manager."
+ "NEGuardProxyProvider"
+ "RELAY_ERROR_CERTIFICATE_EXPIRED"
+ "RELAY_ERROR_CERTIFICATE_INVALID"
+ "RELAY_ERROR_CERTIFICATE_MISSING"
+ "RELAY_ERROR_DNS_FAILED"
+ "RELAY_ERROR_OTHER"
+ "RELAY_ERROR_PVD_CONFIGURATION_TRUNCATED"
+ "RELAY_ERROR_SERVER_CERTIFICATE_EXPIRED"
+ "RELAY_ERROR_SERVER_CERTIFICATE_INVALID"
+ "RELAY_ERROR_SERVER_DISCONNECTED"
+ "RELAY_ERROR_SERVER_UNREACHABLE"
+ "Restored cached PvD configuration, expires in %lu seconds"
+ "Restored expired cached PvD configuration (expired %lu seconds ago), fetching fresh config"
+ "Scheduling PvD fetch in %lu mins"
+ "Setting up guard proxy"
+ "T@\"NSDictionary\",&,V_cachedPvDConfig"
+ "_cachedPvDConfig"
+ "_flowDivertControlHandle"
+ "_guardProxy"
+ "_guardProxyFlows"
+ "_guard_proxy_completion_handler"
+ "_policyIDs"
+ "bundleWithIdentifier:"
+ "cachedPvDConfig"
+ "com.apple.NetworkExtension"
+ "container:didFailWithError:"
+ "container:didSetTunnelConfiguration:completionHandler:"
+ "dataWithJSONObject:options:error:"
+ "didFailWithError with error: %@"
+ "didStartWithError called with: %@"
+ "domains"
+ "initFlowDivertControlSocketWithParams() flow_divert adding FLOW_DIVERT_TLV_GUARD_PROXY_CTL_UNIT"
+ "initFlowDivertControlSocketWithParams:isGuardProxy:order:"
+ "initGuardProxyFlowDivertControlSocket"
+ "initWithDelegate:queue:url:identityRef:additionalHTTPHeaders:cachedPvDConfig:"
+ "localizedStringForKey:value:table:"
+ "proxyPolicyRuleCount"
+ "setCachedPvDConfig:"
+ "stopWithCompletionHandler:"
+ "subnets"
+ "v32@0:8@\"NEAppProxyProviderContainer\"16@\"NSError\"24"
+ "v32@0:8@\"NEAppProxyProviderContainer\"16@?<v@?@\"NSFileHandle\">24"
+ "v40@0:8@\"NEAppProxyProviderContainer\"16@\"NETunnelNetworkSettings\"24@?<v@?@\"NSError\">32"
- "%@: failed to init, providerClass is not subclass of NEAppProxyProvider"
- "%sclient-flags:%u"
- "-[NEPvDFetcher initWithDelegate:queue:url:identityRef:additionalHTTPHeaders:]"
- "@24@0:8B16i20"
- "@56@0:8@16@24@32^{__SecIdentity=}40@48"
- "Fetching new PvD %@ in %lu mins"
- "initFlowDivertControlSocketWithParams:order:"
- "initWithDelegate:queue:url:identityRef:additionalHTTPHeaders:"

```
