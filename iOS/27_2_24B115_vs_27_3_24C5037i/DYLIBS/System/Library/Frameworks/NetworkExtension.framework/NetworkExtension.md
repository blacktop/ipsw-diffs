## NetworkExtension

> `/System/Library/Frameworks/NetworkExtension.framework/NetworkExtension`

```diff

-2365.40.3.0.2
-  __TEXT.__text: 0x20a618
-  __TEXT.__objc_methlist: 0xf578
+2365.60.12.0.0
+  __TEXT.__text: 0x20b4b8
+  __TEXT.__objc_methlist: 0xf5a8
   __TEXT.__const: 0x36b4
   __TEXT.__swift5_typeref: 0xdf0
   __TEXT.__swift5_capture: 0x1038

   __TEXT.__swift_as_cont: 0x1f4
   __TEXT.__swift5_fieldmd: 0x680
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__cstring: 0x197c9
-  __TEXT.__oslogstring: 0x24eff
+  __TEXT.__cstring: 0x197e6
+  __TEXT.__oslogstring: 0x24f83
   __TEXT.__gcc_except_tab: 0x5008
-  __TEXT.__unwind_info: 0x6ae0
+  __TEXT.__unwind_info: 0x6af0
   __TEXT.__eh_frame: 0x2bd0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x268
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x53e8
+  __DATA_CONST.__objc_selrefs: 0x5400
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x728
   __DATA_CONST.__objc_arraydata: 0x138
   __DATA_CONST.__got: 0x17f8
   __AUTH_CONST.__const: 0x4aa0
-  __AUTH_CONST.__cfstring: 0x19480
-  __AUTH_CONST.__objc_const: 0x23450
+  __AUTH_CONST.__cfstring: 0x194e0
+  __AUTH_CONST.__objc_const: 0x23470
   __AUTH_CONST.__objc_intobj: 0x3d8
   __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x24b8
-  __DATA.__objc_ivar: 0x1c50
+  __DATA.__objc_ivar: 0x1c54
   __DATA.__data: 0x640
   __DATA.__common: 0x190
   __DATA_DIRTY.__objc_data: 0x7658

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8335
-  Symbols:   14432
-  CStrings:  7247
+  Functions: 8340
+  Symbols:   14438
+  CStrings:  7252
 
Symbols:
+ +[NEPolicyResult scopeSocketToInterfaceNameWithFlags:flags:]
+ +[NEPolicyResult tunnelIPToInterfaceNameWithFlags:secondaryResultType:flags:]
+ -[NEAppRule setMatchSigningIdentifier:]
+ -[NEPathController updateAppRulesForUID:]
+ -[NEPolicyResult appendInterfaceNameAndResultFlagsToData:]
+ GCC_except_table1002
+ GCC_except_table1007
+ GCC_except_table1056
+ GCC_except_table1145
+ GCC_except_table1205
+ GCC_except_table1212
+ GCC_except_table1381
+ GCC_except_table1392
+ GCC_except_table1398
+ GCC_except_table1404
+ GCC_except_table1417
+ GCC_except_table1429
+ GCC_except_table1555
+ GCC_except_table1681
+ GCC_except_table1686
+ GCC_except_table1689
+ GCC_except_table1750
+ GCC_except_table1755
+ GCC_except_table1759
+ GCC_except_table1762
+ GCC_except_table1769
+ GCC_except_table1776
+ GCC_except_table1801
+ GCC_except_table1827
+ GCC_except_table2041
+ GCC_except_table279
+ GCC_except_table2953
+ GCC_except_table3198
+ GCC_except_table3203
+ GCC_except_table3209
+ GCC_except_table3212
+ GCC_except_table3229
+ GCC_except_table3244
+ GCC_except_table3259
+ GCC_except_table3301
+ GCC_except_table3305
+ GCC_except_table3351
+ GCC_except_table3402
+ GCC_except_table3462
+ GCC_except_table3481
+ GCC_except_table3490
+ GCC_except_table3492
+ GCC_except_table3517
+ GCC_except_table3527
+ GCC_except_table3541
+ GCC_except_table3579
+ GCC_except_table3585
+ GCC_except_table3587
+ GCC_except_table3622
+ GCC_except_table3625
+ GCC_except_table3714
+ GCC_except_table3742
+ GCC_except_table3984
+ GCC_except_table3994
+ GCC_except_table3996
+ GCC_except_table4088
+ GCC_except_table409
+ GCC_except_table411
+ GCC_except_table4255
+ GCC_except_table4266
+ GCC_except_table4272
+ GCC_except_table4295
+ GCC_except_table4299
+ GCC_except_table4305
+ GCC_except_table4311
+ GCC_except_table4319
+ GCC_except_table4392
+ GCC_except_table4400
+ GCC_except_table4501
+ GCC_except_table4503
+ GCC_except_table4600
+ GCC_except_table477
+ GCC_except_table4782
+ GCC_except_table4787
+ GCC_except_table4794
+ GCC_except_table4825
+ GCC_except_table4835
+ GCC_except_table4839
+ GCC_except_table4851
+ GCC_except_table4873
+ GCC_except_table4881
+ GCC_except_table4974
+ GCC_except_table5046
+ GCC_except_table5066
+ GCC_except_table5070
+ GCC_except_table5083
+ GCC_except_table5187
+ GCC_except_table5228
+ GCC_except_table5274
+ GCC_except_table5276
+ GCC_except_table5342
+ GCC_except_table5345
+ GCC_except_table5381
+ GCC_except_table5401
+ GCC_except_table5403
+ GCC_except_table5405
+ GCC_except_table5413
+ GCC_except_table5454
+ GCC_except_table5458
+ GCC_except_table5461
+ GCC_except_table5505
+ GCC_except_table5527
+ GCC_except_table5530
+ GCC_except_table5625
+ GCC_except_table5956
+ GCC_except_table5995
+ GCC_except_table5996
+ GCC_except_table5999
+ GCC_except_table6064
+ GCC_except_table6070
+ GCC_except_table6071
+ GCC_except_table6079
+ GCC_except_table6082
+ GCC_except_table6092
+ GCC_except_table6110
+ GCC_except_table6111
+ GCC_except_table6117
+ GCC_except_table6118
+ GCC_except_table6119
+ GCC_except_table6126
+ GCC_except_table6135
+ GCC_except_table6138
+ GCC_except_table6142
+ GCC_except_table6220
+ GCC_except_table6221
+ GCC_except_table6369
+ GCC_except_table6370
+ GCC_except_table6371
+ GCC_except_table6372
+ GCC_except_table6373
+ GCC_except_table6387
+ GCC_except_table6388
+ GCC_except_table6394
+ GCC_except_table6420
+ GCC_except_table6499
+ GCC_except_table6500
+ GCC_except_table6501
+ GCC_except_table6502
+ GCC_except_table653
+ GCC_except_table659
+ GCC_except_table665
+ GCC_except_table672
+ GCC_except_table680
+ GCC_except_table777
+ GCC_except_table844
+ GCC_except_table849
+ GCC_except_table898
+ GCC_except_table903
+ GCC_except_table921
+ GCC_except_table930
+ GCC_except_table958
+ _OBJC_IVAR_$_NEPolicyResult._resultFlags
- GCC_except_table1003
- GCC_except_table1055
- GCC_except_table1144
- GCC_except_table1203
- GCC_except_table1209
- GCC_except_table1379
- GCC_except_table1383
- GCC_except_table1397
- GCC_except_table1402
- GCC_except_table1416
- GCC_except_table1427
- GCC_except_table1554
- GCC_except_table1679
- GCC_except_table1685
- GCC_except_table1688
- GCC_except_table1733
- GCC_except_table1754
- GCC_except_table1758
- GCC_except_table1761
- GCC_except_table1767
- GCC_except_table1775
- GCC_except_table1800
- GCC_except_table1826
- GCC_except_table2040
- GCC_except_table278
- GCC_except_table2952
- GCC_except_table3197
- GCC_except_table3202
- GCC_except_table3208
- GCC_except_table3211
- GCC_except_table3226
- GCC_except_table3243
- GCC_except_table3257
- GCC_except_table3300
- GCC_except_table3304
- GCC_except_table3350
- GCC_except_table3401
- GCC_except_table3461
- GCC_except_table3480
- GCC_except_table3489
- GCC_except_table3491
- GCC_except_table3514
- GCC_except_table3526
- GCC_except_table3540
- GCC_except_table3578
- GCC_except_table3584
- GCC_except_table3586
- GCC_except_table3621
- GCC_except_table3623
- GCC_except_table3713
- GCC_except_table3741
- GCC_except_table3983
- GCC_except_table3990
- GCC_except_table3995
- GCC_except_table408
- GCC_except_table4087
- GCC_except_table410
- GCC_except_table4254
- GCC_except_table4265
- GCC_except_table4271
- GCC_except_table4286
- GCC_except_table4298
- GCC_except_table4303
- GCC_except_table4310
- GCC_except_table4317
- GCC_except_table4390
- GCC_except_table4399
- GCC_except_table4495
- GCC_except_table4502
- GCC_except_table4598
- GCC_except_table476
- GCC_except_table4780
- GCC_except_table4785
- GCC_except_table4792
- GCC_except_table4823
- GCC_except_table4833
- GCC_except_table4837
- GCC_except_table4849
- GCC_except_table4869
- GCC_except_table4877
- GCC_except_table4971
- GCC_except_table5041
- GCC_except_table5061
- GCC_except_table5065
- GCC_except_table5078
- GCC_except_table5177
- GCC_except_table5223
- GCC_except_table5269
- GCC_except_table5271
- GCC_except_table5337
- GCC_except_table5340
- GCC_except_table5376
- GCC_except_table5396
- GCC_except_table5398
- GCC_except_table5400
- GCC_except_table5408
- GCC_except_table5448
- GCC_except_table5449
- GCC_except_table5451
- GCC_except_table5500
- GCC_except_table5522
- GCC_except_table5525
- GCC_except_table5620
- GCC_except_table5951
- GCC_except_table5990
- GCC_except_table5991
- GCC_except_table5994
- GCC_except_table6059
- GCC_except_table6065
- GCC_except_table6066
- GCC_except_table6074
- GCC_except_table6077
- GCC_except_table6087
- GCC_except_table6102
- GCC_except_table6103
- GCC_except_table6104
- GCC_except_table6105
- GCC_except_table6106
- GCC_except_table6121
- GCC_except_table6130
- GCC_except_table6133
- GCC_except_table6137
- GCC_except_table6215
- GCC_except_table6216
- GCC_except_table6348
- GCC_except_table6349
- GCC_except_table6350
- GCC_except_table6351
- GCC_except_table6352
- GCC_except_table6377
- GCC_except_table6383
- GCC_except_table6384
- GCC_except_table6415
- GCC_except_table646
- GCC_except_table6494
- GCC_except_table6495
- GCC_except_table6496
- GCC_except_table6497
- GCC_except_table658
- GCC_except_table663
- GCC_except_table671
- GCC_except_table678
- GCC_except_table776
- GCC_except_table843
- GCC_except_table848
- GCC_except_table897
- GCC_except_table902
- GCC_except_table920
- GCC_except_table926
- GCC_except_table957
- GCC_except_table996
Functions:
~ -[NEPolicySession addPolicy:storeLocally:] : 6092 -> 6004
+ -[NEAppRule setMatchSigningIdentifier:]
~ -[NEConfiguration configurePluginWithPayload:pluginType:payloadType:vpnType:] : 3824 -> 4420
~ ___59-[NEAppPushManager saveToPreferencesWithCompletionHandler:]_block_invoke.38 : 332 -> 388
+ -[NEPathController updateAppRulesForUID:]
~ -[NEDeclarationInstaller dictionaryForVPNConfiguration:] : 6032 -> 7324
+ +[NEPolicyResult scopeSocketToInterfaceNameWithFlags:flags:]
+ +[NEPolicyResult tunnelIPToInterfaceNameWithFlags:secondaryResultType:flags:]
~ -[NEPolicyResult descriptionWithIndent:options:] : 408 -> 440
+ -[NEPolicyResult appendInterfaceNameAndResultFlagsToData:]
~ -[NEUtilConfigurationClient setDNSProxyWithParameters:errorStr:] : 276 -> 356
~ -[NEUtilConfigurationClient setAppPushParameters:errorStr:] : 456 -> 544
CStrings:
+ "%@ configurePluginWithPayload: unsupported or incomplete authentication, type %@, user name %@, password %@."
+ "%@ dictionaryForVPNConfiguration unsupported protocol type %ld"
+ "%@ found DDM sourced persistent reference [%@] for the password"
+ "Adding %lu plugin path rules"
+ "e"
+ "missing"
+ "present"
+ "result-flags"
- "%@ configurePluginWithPayload: unsupported authen type %@."
- "%@ dictionaryForVPNConfiguration failed to find protocol object for ipsec"
- "U"
```
