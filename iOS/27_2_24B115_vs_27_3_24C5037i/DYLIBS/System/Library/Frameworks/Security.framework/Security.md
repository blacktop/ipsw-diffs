## Security

> `/System/Library/Frameworks/Security.framework/Security`

```diff

-62460.40.78.0.0
-  __TEXT.__text: 0x17e210
+62460.60.42.502.1
+  __TEXT.__text: 0x180798
   __TEXT.__lazy_helpers: 0x54
-  __TEXT.__objc_methlist: 0x67cc
-  __TEXT.__const: 0x1b9e8
+  __TEXT.__objc_methlist: 0x693c
+  __TEXT.__const: 0x1ba10
   __TEXT.__dlopen_cstrs: 0xbc
-  __TEXT.__cstring: 0x1965d
-  __TEXT.__gcc_except_tab: 0x7db4
+  __TEXT.__cstring: 0x19c0b
+  __TEXT.__gcc_except_tab: 0x7e7c
   __TEXT.__oslogstring: 0xf8f4
   __TEXT.__ustring: 0x406
   __TEXT.__dof_codesign: 0x1f2c
   __TEXT.__dof_security_: 0x325
-  __TEXT.__unwind_info: 0x72f8
+  __TEXT.__unwind_info: 0x73b0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x15398
-  __DATA_CONST.__objc_classlist: 0x350
+  __DATA_CONST.__const: 0x153f8
+  __DATA_CONST.__objc_classlist: 0x360
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x34d8
+  __DATA_CONST.__objc_selrefs: 0x35e8
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_superrefs: 0x2f0
-  __DATA_CONST.__objc_arraydata: 0x100
-  __DATA_CONST.__got: 0x770
-  __AUTH_CONST.__const: 0x3f80
-  __AUTH_CONST.__cfstring: 0x17a00
-  __AUTH_CONST.__objc_const: 0xa628
+  __DATA_CONST.__objc_superrefs: 0x300
+  __DATA_CONST.__objc_arraydata: 0x158
+  __DATA_CONST.__got: 0x790
+  __AUTH_CONST.__const: 0x3ff8
+  __AUTH_CONST.__cfstring: 0x18000
+  __AUTH_CONST.__objc_const: 0xaa28
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__lazy_load_got: 0x8
-  __AUTH_CONST.__objc_arrayobj: 0x120
+  __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x2000
-  __AUTH.__objc_data: 0x1f90
+  __AUTH_CONST.__auth_got: 0x2010
+  __AUTH.__objc_data: 0x2030
   __AUTH.__data: 0x1488
-  __DATA.__objc_ivar: 0x674
+  __DATA.__objc_ivar: 0x6c0
   __DATA.__data: 0x2180
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x190

   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
-  - /System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices
   - /System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreTime.framework/CoreTime

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/SwiftJOSE.framework/SwiftJOSE
   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /usr/lib/libCoreEntitlements.dylib
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/libcoretls_cfhelpers.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 7143
-  Symbols:   13686
-  CStrings:  5772
+  Functions: 7189
+  Symbols:   13785
+  CStrings:  5836
 
Symbols:
+ +[SecAnalyticsAllowlist currentProcessIsPlatformBinary]
+ +[SecAnalyticsAllowlist sharedAllowlist]
+ +[SecAnalyticsAllowlistFile fileAtURL:kind:platform:error:]
+ -[SecAnalyticsAllowlist .cxx_destruct]
+ -[SecAnalyticsAllowlist contentVersionForKind:]
+ -[SecAnalyticsAllowlist currentFileForKind:]
+ -[SecAnalyticsAllowlist dealloc]
+ -[SecAnalyticsAllowlist entriesForKind:]
+ -[SecAnalyticsAllowlist fileURLForKind:]
+ -[SecAnalyticsAllowlist initWithSystemDirectory:publishedDirectory:]
+ -[SecAnalyticsAllowlist isReportableAppIdentifier:platformBinary:]
+ -[SecAnalyticsAllowlist loadAll]
+ -[SecAnalyticsAllowlist loadKind:]
+ -[SecAnalyticsAllowlist refreshLocked]
+ -[SecAnalyticsAllowlist reportableDomainForHostname:]
+ -[SecAnalyticsAllowlist sourceForKind:]
+ -[SecAnalyticsAllowlistFile containsEntry:]
+ -[SecAnalyticsAllowlistFile contentVersion]
+ -[SecAnalyticsAllowlistFile count]
+ -[SecAnalyticsAllowlistFile dealloc]
+ -[SecAnalyticsAllowlistFile entryAtIndex:]
+ -[SecAnalyticsAllowlistFile initWithBase:size:descriptor:header:]
+ -[SecAnalyticsAllowlistFile isReplaced]
+ -[SecAnalyticsAllowlistFile kind]
+ -[SecAnalyticsAllowlistFile matchDomain:]
+ -[SecAnalyticsAllowlistFile platform]
+ -[SecAnalyticsAllowlistFile verify:]
+ GCC_except_table1438
+ GCC_except_table1444
+ GCC_except_table1447
+ GCC_except_table1450
+ GCC_except_table1453
+ GCC_except_table1456
+ GCC_except_table1459
+ GCC_except_table1462
+ GCC_except_table1937
+ GCC_except_table1942
+ GCC_except_table1946
+ GCC_except_table1984
+ GCC_except_table2022
+ GCC_except_table2028
+ GCC_except_table2033
+ GCC_except_table2123
+ GCC_except_table2141
+ GCC_except_table2267
+ GCC_except_table2271
+ GCC_except_table2279
+ GCC_except_table2295
+ GCC_except_table2303
+ GCC_except_table2304
+ GCC_except_table2311
+ GCC_except_table2316
+ GCC_except_table2322
+ GCC_except_table2328
+ GCC_except_table2333
+ GCC_except_table2371
+ GCC_except_table2376
+ GCC_except_table2426
+ GCC_except_table2427
+ GCC_except_table2695
+ GCC_except_table2715
+ GCC_except_table2718
+ GCC_except_table2723
+ GCC_except_table2724
+ GCC_except_table3064
+ GCC_except_table3093
+ GCC_except_table3157
+ GCC_except_table3160
+ GCC_except_table3167
+ GCC_except_table3170
+ GCC_except_table3277
+ GCC_except_table3297
+ GCC_except_table3300
+ GCC_except_table3304
+ GCC_except_table3307
+ GCC_except_table3580
+ GCC_except_table3636
+ GCC_except_table3652
+ GCC_except_table3660
+ GCC_except_table3667
+ GCC_except_table3679
+ GCC_except_table3725
+ GCC_except_table3745
+ GCC_except_table3749
+ GCC_except_table3764
+ GCC_except_table3777
+ GCC_except_table3778
+ GCC_except_table3883
+ GCC_except_table3886
+ GCC_except_table3954
+ GCC_except_table3960
+ GCC_except_table3961
+ GCC_except_table3985
+ GCC_except_table3986
+ GCC_except_table4457
+ GCC_except_table4461
+ GCC_except_table4467
+ GCC_except_table4480
+ GCC_except_table4484
+ GCC_except_table4485
+ GCC_except_table4496
+ GCC_except_table4509
+ GCC_except_table4511
+ GCC_except_table4518
+ GCC_except_table4524
+ GCC_except_table4528
+ GCC_except_table4537
+ GCC_except_table4540
+ GCC_except_table4543
+ GCC_except_table4545
+ GCC_except_table4549
+ GCC_except_table4552
+ GCC_except_table4557
+ GCC_except_table4560
+ GCC_except_table4562
+ GCC_except_table4566
+ GCC_except_table4569
+ GCC_except_table4572
+ GCC_except_table4645
+ GCC_except_table4661
+ GCC_except_table4662
+ GCC_except_table4688
+ GCC_except_table4691
+ GCC_except_table4695
+ GCC_except_table4700
+ GCC_except_table4716
+ GCC_except_table4717
+ GCC_except_table4718
+ GCC_except_table4719
+ GCC_except_table4720
+ GCC_except_table4721
+ GCC_except_table4722
+ GCC_except_table4723
+ GCC_except_table4794
+ GCC_except_table4806
+ GCC_except_table4810
+ GCC_except_table4921
+ GCC_except_table5045
+ GCC_except_table5046
+ GCC_except_table5052
+ GCC_except_table5057
+ GCC_except_table5059
+ GCC_except_table5061
+ GCC_except_table5063
+ GCC_except_table5065
+ GCC_except_table5067
+ GCC_except_table5069
+ GCC_except_table5198
+ GCC_except_table5201
+ GCC_except_table5203
+ GCC_except_table5205
+ GCC_except_table5208
+ GCC_except_table5211
+ GCC_except_table5213
+ GCC_except_table5425
+ GCC_except_table5427
+ GCC_except_table5944
+ GCC_except_table5953
+ GCC_except_table5955
+ GCC_except_table5957
+ GCC_except_table5959
+ GCC_except_table6094
+ GCC_except_table6100
+ GCC_except_table6113
+ GCC_except_table6118
+ GCC_except_table6120
+ GCC_except_table6129
+ GCC_except_table6131
+ GCC_except_table6132
+ GCC_except_table6138
+ GCC_except_table6140
+ GCC_except_table6144
+ GCC_except_table6145
+ GCC_except_table6146
+ GCC_except_table6147
+ GCC_except_table6148
+ GCC_except_table6171
+ GCC_except_table6173
+ GCC_except_table6200
+ GCC_except_table6201
+ GCC_except_table6202
+ GCC_except_table6203
+ GCC_except_table6217
+ GCC_except_table6218
+ GCC_except_table6219
+ GCC_except_table6234
+ GCC_except_table6236
+ GCC_except_table6239
+ GCC_except_table6240
+ GCC_except_table6241
+ GCC_except_table6242
+ GCC_except_table6259
+ GCC_except_table6266
+ GCC_except_table6267
+ GCC_except_table6269
+ GCC_except_table6272
+ GCC_except_table6274
+ GCC_except_table6277
+ GCC_except_table6278
+ GCC_except_table6292
+ GCC_except_table6298
+ GCC_except_table6325
+ GCC_except_table6330
+ GCC_except_table6343
+ GCC_except_table6358
+ GCC_except_table6361
+ GCC_except_table6362
+ GCC_except_table6363
+ GCC_except_table6367
+ GCC_except_table6368
+ GCC_except_table6369
+ GCC_except_table6370
+ GCC_except_table6372
+ GCC_except_table6378
+ GCC_except_table6379
+ GCC_except_table6380
+ GCC_except_table6381
+ GCC_except_table6383
+ GCC_except_table6386
+ GCC_except_table6387
+ GCC_except_table6393
+ GCC_except_table6400
+ GCC_except_table6401
+ GCC_except_table6402
+ GCC_except_table6403
+ GCC_except_table6406
+ GCC_except_table6411
+ GCC_except_table6419
+ GCC_except_table6420
+ GCC_except_table6434
+ GCC_except_table6437
+ GCC_except_table6444
+ GCC_except_table6445
+ GCC_except_table6453
+ GCC_except_table6461
+ GCC_except_table6468
+ GCC_except_table6470
+ GCC_except_table6471
+ GCC_except_table6473
+ GCC_except_table6474
+ GCC_except_table6481
+ GCC_except_table6484
+ GCC_except_table6485
+ GCC_except_table6486
+ GCC_except_table6489
+ GCC_except_table6494
+ GCC_except_table6498
+ GCC_except_table6500
+ GCC_except_table6536
+ GCC_except_table6537
+ GCC_except_table6538
+ GCC_except_table6541
+ GCC_except_table6542
+ GCC_except_table6543
+ GCC_except_table6545
+ GCC_except_table6547
+ GCC_except_table6548
+ GCC_except_table6549
+ GCC_except_table6550
+ GCC_except_table6552
+ GCC_except_table6553
+ GCC_except_table6554
+ GCC_except_table6555
+ GCC_except_table6556
+ GCC_except_table6557
+ GCC_except_table6558
+ GCC_except_table6559
+ GCC_except_table6561
+ GCC_except_table6562
+ GCC_except_table6563
+ GCC_except_table6564
+ GCC_except_table6565
+ GCC_except_table6566
+ GCC_except_table6567
+ GCC_except_table6568
+ GCC_except_table6569
+ GCC_except_table6570
+ GCC_except_table6571
+ GCC_except_table6572
+ GCC_except_table6573
+ GCC_except_table6576
+ GCC_except_table6606
+ GCC_except_table6621
+ GCC_except_table6624
+ GCC_except_table6625
+ GCC_except_table6627
+ GCC_except_table6628
+ GCC_except_table6631
+ GCC_except_table6632
+ GCC_except_table6636
+ GCC_except_table6639
+ GCC_except_table6640
+ GCC_except_table6641
+ GCC_except_table6657
+ GCC_except_table6662
+ GCC_except_table6666
+ GCC_except_table6672
+ GCC_except_table6675
+ GCC_except_table6680
+ GCC_except_table6683
+ GCC_except_table6684
+ GCC_except_table6688
+ GCC_except_table6689
+ GCC_except_table6690
+ GCC_except_table6698
+ GCC_except_table6713
+ GCC_except_table6714
+ GCC_except_table6725
+ GCC_except_table6732
+ GCC_except_table6737
+ GCC_except_table6740
+ GCC_except_table6748
+ GCC_except_table6750
+ GCC_except_table6768
+ GCC_except_table6769
+ GCC_except_table6770
+ GCC_except_table6773
+ GCC_except_table6782
+ GCC_except_table6791
+ GCC_except_table6792
+ GCC_except_table6795
+ GCC_except_table6798
+ GCC_except_table6800
+ GCC_except_table6807
+ GCC_except_table6810
+ GCC_except_table6811
+ GCC_except_table6812
+ GCC_except_table6813
+ GCC_except_table6817
+ GCC_except_table6818
+ GCC_except_table6830
+ GCC_except_table6832
+ GCC_except_table6833
+ GCC_except_table6836
+ GCC_except_table6839
+ GCC_except_table6840
+ GCC_except_table6842
+ GCC_except_table6847
+ GCC_except_table6860
+ GCC_except_table6862
+ GCC_except_table6868
+ GCC_except_table6870
+ GCC_except_table6872
+ GCC_except_table6873
+ GCC_except_table6877
+ GCC_except_table6881
+ GCC_except_table6896
+ GCC_except_table6897
+ GCC_except_table6902
+ GCC_except_table6922
+ GCC_except_table6931
+ GCC_except_table6933
+ GCC_except_table6935
+ GCC_except_table6938
+ GCC_except_table6941
+ GCC_except_table6945
+ GCC_except_table6950
+ GCC_except_table6951
+ GCC_except_table6954
+ GCC_except_table6957
+ GCC_except_table6964
+ GCC_except_table6969
+ GCC_except_table6970
+ GCC_except_table6980
+ GCC_except_table6985
+ GCC_except_table6989
+ GCC_except_table6990
+ GCC_except_table6992
+ GCC_except_table6995
+ GCC_except_table6998
+ GCC_except_table7001
+ GCC_except_table7002
+ GCC_except_table7004
+ GCC_except_table7005
+ GCC_except_table7006
+ GCC_except_table7007
+ GCC_except_table7008
+ GCC_except_table7009
+ GCC_except_table7011
+ GCC_except_table7012
+ GCC_except_table7017
+ GCC_except_table7020
+ GCC_except_table7023
+ GCC_except_table7024
+ GCC_except_table7039
+ GCC_except_table7040
+ GCC_except_table7045
+ _CreateQWACBindingError
+ _OBJC_CLASS_$_JOSEHeader
+ _OBJC_CLASS_$_JOSEUnverifiedJWS
+ _OBJC_CLASS_$_SecAnalyticsAllowlist
+ _OBJC_CLASS_$_SecAnalyticsAllowlistFile
+ _OBJC_IVAR_$_SecAnalyticsAllowlist._callsSinceReplacedCheck
+ _OBJC_IVAR_$_SecAnalyticsAllowlist._files
+ _OBJC_IVAR_$_SecAnalyticsAllowlist._loaded
+ _OBJC_IVAR_$_SecAnalyticsAllowlist._lock
+ _OBJC_IVAR_$_SecAnalyticsAllowlist._notifyToken
+ _OBJC_IVAR_$_SecAnalyticsAllowlist._publishedDirectory
+ _OBJC_IVAR_$_SecAnalyticsAllowlist._sources
+ _OBJC_IVAR_$_SecAnalyticsAllowlist._systemDirectory
+ _OBJC_IVAR_$_SecAnalyticsAllowlist._urls
+ _OBJC_IVAR_$_SecAnalyticsAllowlistFile._base
+ _OBJC_IVAR_$_SecAnalyticsAllowlistFile._contentVersion
+ _OBJC_IVAR_$_SecAnalyticsAllowlistFile._count
+ _OBJC_IVAR_$_SecAnalyticsAllowlistFile._fd
+ _OBJC_IVAR_$_SecAnalyticsAllowlistFile._kind
+ _OBJC_IVAR_$_SecAnalyticsAllowlistFile._offsets
+ _OBJC_IVAR_$_SecAnalyticsAllowlistFile._platform
+ _OBJC_IVAR_$_SecAnalyticsAllowlistFile._size
+ _OBJC_IVAR_$_SecAnalyticsAllowlistFile._strings
+ _OBJC_IVAR_$_SecAnalyticsAllowlistFile._stringsSize
+ _OBJC_METACLASS_$_SecAnalyticsAllowlist
+ _OBJC_METACLASS_$_SecAnalyticsAllowlistFile
+ _SecAnalyticsAllowlistCodeSignStatusIsPlatformBinary
+ _SecAnalyticsAllowlistCurrentPlatform
+ _SecAnalyticsAllowlistSystemDirectory
+ _SecCertificateCopyPWSPublicKeyIdentifier
+ _SecPolicyCreatePWSMessageKey
+ _SecPolicyCreateQWACTLSBinding
+ _SecTrustCreateAndVerifyQWACTLSBinding
+ _SecTrustCreateAndVerifyQWACTLSBindingInternal
+ _SecTrustCreateAndVerifyQWACTLSBindingWithParameters
+ _ValidateJadesSignature
+ __OBJC_$_CLASS_METHODS_SecAnalyticsAllowlist
+ __OBJC_$_CLASS_METHODS_SecAnalyticsAllowlistFile
+ __OBJC_$_CLASS_PROP_LIST_SecAnalyticsAllowlist
+ __OBJC_$_INSTANCE_METHODS_SecAnalyticsAllowlist
+ __OBJC_$_INSTANCE_METHODS_SecAnalyticsAllowlistFile
+ __OBJC_$_INSTANCE_VARIABLES_SecAnalyticsAllowlist
+ __OBJC_$_INSTANCE_VARIABLES_SecAnalyticsAllowlistFile
+ __OBJC_$_PROP_LIST_SecAnalyticsAllowlistFile
+ __OBJC_CLASS_RO_$_SecAnalyticsAllowlist
+ __OBJC_CLASS_RO_$_SecAnalyticsAllowlistFile
+ __OBJC_METACLASS_RO_$_SecAnalyticsAllowlist
+ __OBJC_METACLASS_RO_$_SecAnalyticsAllowlistFile
+ __SecTrustQWACValidationEnabled.QWACValidationEnabled
+ __SecTrustQWACValidationEnabled.onceToken
+ __SecTrustShowFeatureStatus
+ __ZN8Security14MainMachOImageC2Ev
+ __ZN8Security14MainMachOImageD0Ev
+ __ZN8Security14MainMachOImageD1Ev
+ __ZN8Security9MachOBase12initCommandsEPK12load_command
+ __ZTIN8Security14MainMachOImageE
+ __ZTSN8Security14MainMachOImageE
+ __ZTVN8Security14MainMachOImageE
+ ___40+[SecAnalyticsAllowlist sharedAllowlist]_block_invoke
+ ____SecTrustQWACValidationEnabled_block_invoke
+ _find_entry
+ _has_valid_labels
+ _kSecPolicyApplePWSMessageKey
+ _kSecPolicyAppleQWACTLSBinding
+ _kSecPolicyCheckQWACTLSBinding
+ _kSecQWACTLSBindingErrorDomain
+ _notify_check
+ _objc_terminate
+ _pwsPublicKeyNumber
+ _set_error
+ _sharedAllowlist.once
+ _sharedAllowlist.shared
- GCC_except_table1436
- GCC_except_table1442
- GCC_except_table1445
- GCC_except_table1448
- GCC_except_table1451
- GCC_except_table1454
- GCC_except_table1457
- GCC_except_table1460
- GCC_except_table1925
- GCC_except_table1940
- GCC_except_table1944
- GCC_except_table1982
- GCC_except_table2018
- GCC_except_table2026
- GCC_except_table2031
- GCC_except_table2121
- GCC_except_table2139
- GCC_except_table2265
- GCC_except_table2269
- GCC_except_table2273
- GCC_except_table2291
- GCC_except_table2297
- GCC_except_table2302
- GCC_except_table2309
- GCC_except_table2314
- GCC_except_table2320
- GCC_except_table2324
- GCC_except_table2331
- GCC_except_table2337
- GCC_except_table2372
- GCC_except_table2422
- GCC_except_table2423
- GCC_except_table2693
- GCC_except_table2713
- GCC_except_table2716
- GCC_except_table2721
- GCC_except_table2722
- GCC_except_table3062
- GCC_except_table3091
- GCC_except_table3155
- GCC_except_table3158
- GCC_except_table3165
- GCC_except_table3168
- GCC_except_table3273
- GCC_except_table3295
- GCC_except_table3298
- GCC_except_table3302
- GCC_except_table3305
- GCC_except_table3544
- GCC_except_table3595
- GCC_except_table3600
- GCC_except_table3616
- GCC_except_table3624
- GCC_except_table3643
- GCC_except_table3677
- GCC_except_table3689
- GCC_except_table3705
- GCC_except_table3709
- GCC_except_table3728
- GCC_except_table3742
- GCC_except_table3847
- GCC_except_table3850
- GCC_except_table3913
- GCC_except_table3918
- GCC_except_table3924
- GCC_except_table3925
- GCC_except_table3950
- GCC_except_table4420
- GCC_except_table4424
- GCC_except_table4430
- GCC_except_table4437
- GCC_except_table4443
- GCC_except_table4447
- GCC_except_table4448
- GCC_except_table4459
- GCC_except_table4472
- GCC_except_table4478
- GCC_except_table4481
- GCC_except_table4487
- GCC_except_table4491
- GCC_except_table4500
- GCC_except_table4503
- GCC_except_table4506
- GCC_except_table4508
- GCC_except_table4512
- GCC_except_table4520
- GCC_except_table4523
- GCC_except_table4525
- GCC_except_table4529
- GCC_except_table4532
- GCC_except_table4535
- GCC_except_table4608
- GCC_except_table4621
- GCC_except_table4624
- GCC_except_table4625
- GCC_except_table4647
- GCC_except_table4651
- GCC_except_table4654
- GCC_except_table4663
- GCC_except_table4679
- GCC_except_table4680
- GCC_except_table4681
- GCC_except_table4682
- GCC_except_table4683
- GCC_except_table4685
- GCC_except_table4686
- GCC_except_table4757
- GCC_except_table4769
- GCC_except_table4773
- GCC_except_table4884
- GCC_except_table5008
- GCC_except_table5009
- GCC_except_table5015
- GCC_except_table5020
- GCC_except_table5022
- GCC_except_table5024
- GCC_except_table5026
- GCC_except_table5028
- GCC_except_table5030
- GCC_except_table5032
- GCC_except_table5161
- GCC_except_table5164
- GCC_except_table5166
- GCC_except_table5168
- GCC_except_table5171
- GCC_except_table5174
- GCC_except_table5176
- GCC_except_table5901
- GCC_except_table5910
- GCC_except_table5912
- GCC_except_table5914
- GCC_except_table5916
- GCC_except_table6043
- GCC_except_table6051
- GCC_except_table6057
- GCC_except_table6070
- GCC_except_table6072
- GCC_except_table6075
- GCC_except_table6077
- GCC_except_table6088
- GCC_except_table6089
- GCC_except_table6095
- GCC_except_table6097
- GCC_except_table6101
- GCC_except_table6102
- GCC_except_table6103
- GCC_except_table6104
- GCC_except_table6105
- GCC_except_table6109
- GCC_except_table6110
- GCC_except_table6114
- GCC_except_table6128
- GCC_except_table6130
- GCC_except_table6154
- GCC_except_table6155
- GCC_except_table6159
- GCC_except_table6160
- GCC_except_table6174
- GCC_except_table6175
- GCC_except_table6176
- GCC_except_table6188
- GCC_except_table6191
- GCC_except_table6193
- GCC_except_table6199
- GCC_except_table6213
- GCC_except_table6220
- GCC_except_table6221
- GCC_except_table6223
- GCC_except_table6226
- GCC_except_table6228
- GCC_except_table6232
- GCC_except_table6233
- GCC_except_table6246
- GCC_except_table6249
- GCC_except_table6252
- GCC_except_table6288
- GCC_except_table6297
- GCC_except_table6301
- GCC_except_table6308
- GCC_except_table6309
- GCC_except_table6310
- GCC_except_table6311
- GCC_except_table6312
- GCC_except_table6314
- GCC_except_table6315
- GCC_except_table6316
- GCC_except_table6317
- GCC_except_table6321
- GCC_except_table6322
- GCC_except_table6323
- GCC_except_table6324
- GCC_except_table6326
- GCC_except_table6331
- GCC_except_table6332
- GCC_except_table6333
- GCC_except_table6335
- GCC_except_table6337
- GCC_except_table6340
- GCC_except_table6342
- GCC_except_table6346
- GCC_except_table6353
- GCC_except_table6365
- GCC_except_table6373
- GCC_except_table6374
- GCC_except_table6391
- GCC_except_table6397
- GCC_except_table6398
- GCC_except_table6407
- GCC_except_table6408
- GCC_except_table6415
- GCC_except_table6422
- GCC_except_table6424
- GCC_except_table6425
- GCC_except_table6427
- GCC_except_table6428
- GCC_except_table6435
- GCC_except_table6439
- GCC_except_table6440
- GCC_except_table6447
- GCC_except_table6448
- GCC_except_table6449
- GCC_except_table6452
- GCC_except_table6455
- GCC_except_table6458
- GCC_except_table6460
- GCC_except_table6464
- GCC_except_table6490
- GCC_except_table6491
- GCC_except_table6492
- GCC_except_table6496
- GCC_except_table6497
- GCC_except_table6499
- GCC_except_table6502
- GCC_except_table6503
- GCC_except_table6507
- GCC_except_table6508
- GCC_except_table6509
- GCC_except_table6511
- GCC_except_table6512
- GCC_except_table6513
- GCC_except_table6514
- GCC_except_table6516
- GCC_except_table6517
- GCC_except_table6518
- GCC_except_table6519
- GCC_except_table6520
- GCC_except_table6521
- GCC_except_table6522
- GCC_except_table6523
- GCC_except_table6524
- GCC_except_table6525
- GCC_except_table6526
- GCC_except_table6527
- GCC_except_table6529
- GCC_except_table6530
- GCC_except_table6532
- GCC_except_table6540
- GCC_except_table6574
- GCC_except_table6577
- GCC_except_table6579
- GCC_except_table6580
- GCC_except_table6581
- GCC_except_table6582
- GCC_except_table6583
- GCC_except_table6587
- GCC_except_table6588
- GCC_except_table6590
- GCC_except_table6591
- GCC_except_table6592
- GCC_except_table6593
- GCC_except_table6594
- GCC_except_table6595
- GCC_except_table6596
- GCC_except_table6597
- GCC_except_table6611
- GCC_except_table6614
- GCC_except_table6616
- GCC_except_table6644
- GCC_except_table6648
- GCC_except_table6651
- GCC_except_table6652
- GCC_except_table6667
- GCC_except_table6668
- GCC_except_table6676
- GCC_except_table6678
- GCC_except_table6686
- GCC_except_table6691
- GCC_except_table6700
- GCC_except_table6702
- GCC_except_table6704
- GCC_except_table6712
- GCC_except_table6718
- GCC_except_table6719
- GCC_except_table6723
- GCC_except_table6726
- GCC_except_table6727
- GCC_except_table6735
- GCC_except_table6736
- GCC_except_table6739
- GCC_except_table6741
- GCC_except_table6744
- GCC_except_table6745
- GCC_except_table6747
- GCC_except_table6749
- GCC_except_table6754
- GCC_except_table6755
- GCC_except_table6757
- GCC_except_table6763
- GCC_except_table6766
- GCC_except_table6767
- GCC_except_table6771
- GCC_except_table6776
- GCC_except_table6784
- GCC_except_table6786
- GCC_except_table6794
- GCC_except_table6796
- GCC_except_table6805
- GCC_except_table6814
- GCC_except_table6816
- GCC_except_table6824
- GCC_except_table6825
- GCC_except_table6826
- GCC_except_table6854
- GCC_except_table6856
- GCC_except_table6857
- GCC_except_table6859
- GCC_except_table6876
- GCC_except_table6878
- GCC_except_table6882
- GCC_except_table6885
- GCC_except_table6887
- GCC_except_table6889
- GCC_except_table6892
- GCC_except_table6899
- GCC_except_table6904
- GCC_except_table6906
- GCC_except_table6908
- GCC_except_table6909
- GCC_except_table6910
- GCC_except_table6911
- GCC_except_table6912
- GCC_except_table6914
- GCC_except_table6915
- GCC_except_table6916
- GCC_except_table6918
- GCC_except_table6919
- GCC_except_table6920
- GCC_except_table6923
- GCC_except_table6934
- GCC_except_table6939
- GCC_except_table6943
- GCC_except_table6944
- GCC_except_table6948
- GCC_except_table6953
- GCC_except_table6959
- GCC_except_table6971
- GCC_except_table6977
- GCC_except_table6978
- _SecPolicyCreateQWAC
- __ZN8Security12Architecture5localEv
CStrings:
+ "%s has an invalid size"
+ "%s is not a regular file"
+ "/System/Library/Security/Certificates.bundle"
+ "/private/var/protected/trustd/SharedAssets"
+ "0.4.0.194112.1.6"
+ "0.4.0.194115.1.0"
+ "1.2.840.113635.100.1.133"
+ "1.2.840.113635.100.1.136"
+ "2.5.29.2026.11"
+ "AnalyticsAllowlist_Apps.bin"
+ "AnalyticsAllowlist_Apps_%@.bin"
+ "AnalyticsAllowlist_Domains.bin"
+ "Certificate is not a qualified web certificate for TLS certificate binding"
+ "ES384"
+ "ES512"
+ "PWSMessageKey"
+ "QWACTLSBinding"
+ "RS256"
+ "RS384"
+ "RS512"
+ "TLS-Certificate-Binding-v1"
+ "app identifier"
+ "bad magic"
+ "com.apple.security.analytics-allowlist"
+ "com.apple.security.qwac-tls-binding"
+ "com.apple.trustd.asset-updated"
+ "crit"
+ "domain list must have platform 0"
+ "empty list has strings"
+ "entries cover %u bytes, string area is %u"
+ "entries without strings"
+ "entry %u: not a valid %s"
+ "entry %u: not greater than the entry before it"
+ "entry %u: not terminated inside the string area"
+ "entry %u: offset is %u, expected %u"
+ "exp"
+ "file size does not match header"
+ "fstat %s failed"
+ "iOS"
+ "iat"
+ "invalid crit header"
+ "invalid cty header"
+ "invalid header formats"
+ "invalid header names"
+ "mmap %s failed"
+ "no usable public key"
+ "not a file URL"
+ "open %s failed"
+ "reserved field is not zero"
+ "sigD"
+ "signature verification failed"
+ "string area is not terminated"
+ "string area too large"
+ "tlsTrust is missing hostname"
+ "too many entries"
+ "unable to parse JWS"
+ "unable to parse certificate"
+ "unknown kind requested"
+ "unknown platform"
+ "unsupported format version"
+ "unsupported or incompatible alg"
+ "wrong kind"
+ "wrong platform"
+ "x5t#S256"
```
