## CoreUtils

> `/System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils`

```diff

-900.58.0.0.0
-  __TEXT.__text: 0x11bb7c
-  __TEXT.__objc_methlist: 0xa328
-  __TEXT.__cstring: 0x1e3fc
+910.21.0.0.0
+  __TEXT.__text: 0x11d000
+  __TEXT.__objc_methlist: 0xa3a0
+  __TEXT.__cstring: 0x1e5c5
   __TEXT.__const: 0x22dc
-  __TEXT.__gcc_except_tab: 0x1ac8
-  __TEXT.__oslogstring: 0x48bd
-  __TEXT.__unwind_info: 0x48f0
+  __TEXT.__gcc_except_tab: 0x1af4
+  __TEXT.__oslogstring: 0x48fa
+  __TEXT.__unwind_info: 0x4980
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1510
+  __DATA_CONST.__const: 0x1550
   __DATA_CONST.__objc_classlist: 0x350
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5368
+  __DATA_CONST.__objc_selrefs: 0x53e8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x240
   __DATA_CONST.__objc_arraydata: 0x8
-  __DATA_CONST.__got: 0x678
-  __AUTH_CONST.__const: 0x40e8
-  __AUTH_CONST.__cfstring: 0x4020
-  __AUTH_CONST.__objc_const: 0x13ea8
+  __DATA_CONST.__got: 0x680
+  __AUTH_CONST.__const: 0x4198
+  __AUTH_CONST.__cfstring: 0x4060
+  __AUTH_CONST.__objc_const: 0x13ed8
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x15c0
+  __AUTH_CONST.__auth_got: 0x15d8
   __AUTH.__objc_data: 0x1e28
   __AUTH.__data: 0xa18
   __DATA.__objc_ivar: 0x1540

   __DATA.__common: 0x2a
   __DATA_DIRTY.__objc_data: 0x2f8
   __DATA_DIRTY.__data: 0xa8
-  __DATA_DIRTY.__bss: 0x2a0
+  __DATA_DIRTY.__bss: 0x268
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 5827
-  Symbols:   11663
-  CStrings:  4880
+  Functions: 5854
+  Symbols:   11707
+  CStrings:  4894
 
Symbols:
+ +[CUFile deletePath:dispatchQueue:completionHandler:]
+ +[CUFile deletePath:error:]
+ +[CUFile renameWithOldPath:newPath:dispatchQueue:completionHandler:]
+ +[CUFile renameWithOldPath:newPath:error:]
+ +[CUFile validatedFilename:error:]
+ +[CUOPACK encodeObjectAsDispatchData:flags:error:]
+ -[CUSystemMonitor systemNameSync]
+ GCC_except_table1329
+ GCC_except_table1336
+ GCC_except_table1337
+ GCC_except_table1340
+ GCC_except_table1387
+ GCC_except_table1388
+ GCC_except_table1419
+ GCC_except_table1422
+ GCC_except_table1428
+ GCC_except_table1433
+ GCC_except_table1436
+ GCC_except_table1486
+ GCC_except_table1487
+ GCC_except_table2033
+ GCC_except_table2073
+ GCC_except_table2105
+ GCC_except_table2321
+ GCC_except_table2322
+ GCC_except_table2345
+ GCC_except_table2391
+ GCC_except_table2475
+ GCC_except_table2499
+ GCC_except_table2536
+ GCC_except_table2540
+ GCC_except_table2607
+ GCC_except_table2608
+ GCC_except_table2610
+ GCC_except_table2611
+ GCC_except_table2613
+ GCC_except_table2618
+ GCC_except_table2625
+ GCC_except_table2628
+ GCC_except_table2631
+ GCC_except_table2638
+ GCC_except_table2641
+ GCC_except_table2655
+ GCC_except_table2716
+ GCC_except_table3048
+ GCC_except_table3049
+ GCC_except_table3108
+ GCC_except_table3179
+ GCC_except_table3183
+ GCC_except_table3227
+ GCC_except_table3230
+ GCC_except_table3231
+ GCC_except_table3233
+ GCC_except_table3263
+ GCC_except_table3268
+ GCC_except_table3274
+ GCC_except_table3539
+ GCC_except_table3589
+ GCC_except_table3978
+ GCC_except_table4026
+ GCC_except_table4351
+ GCC_except_table4359
+ GCC_except_table4367
+ GCC_except_table4482
+ GCC_except_table4509
+ GCC_except_table4510
+ GCC_except_table4574
+ GCC_except_table4578
+ GCC_except_table4580
+ GCC_except_table4582
+ GCC_except_table4605
+ GCC_except_table4679
+ GCC_except_table4680
+ GCC_except_table4681
+ GCC_except_table4682
+ GCC_except_table4684
+ GCC_except_table4686
+ GCC_except_table4690
+ GCC_except_table4694
+ GCC_except_table4696
+ GCC_except_table4708
+ GCC_except_table4715
+ GCC_except_table4717
+ GCC_except_table4718
+ GCC_except_table4720
+ GCC_except_table4724
+ GCC_except_table4726
+ GCC_except_table4727
+ GCC_except_table4748
+ GCC_except_table4752
+ GCC_except_table4755
+ GCC_except_table4756
+ GCC_except_table4757
+ GCC_except_table4758
+ GCC_except_table4759
+ GCC_except_table4760
+ GCC_except_table4761
+ GCC_except_table4762
+ GCC_except_table4763
+ GCC_except_table4764
+ GCC_except_table4765
+ GCC_except_table4766
+ GCC_except_table4767
+ GCC_except_table4769
+ GCC_except_table4770
+ GCC_except_table4771
+ GCC_except_table4773
+ GCC_except_table5325
+ GCC_except_table5338
+ GCC_except_table5407
+ GCC_except_table5411
+ GCC_except_table5416
+ GCC_except_table5435
+ GCC_except_table5444
+ GCC_except_table5693
+ GCC_except_table5694
+ GCC_except_table5707
+ GCC_except_table669
+ GCC_except_table770
+ GCC_except_table785
+ GCC_except_table787
+ GCC_except_table790
+ GCC_except_table992
+ _CFDataSetLength
+ _OPACKEncoderCreateDispatchData
+ __BonjourAdvertiserApplyString
+ __GlobalInitialize
+ __OPACKEncodeRoot
+ __OPACKEncoderDispatchDataCallback
+ __OPACKEncoderDispatchDataFlushScratch
+ __PairingSessionLimitPeerInfo
+ ___53+[CUFile deletePath:dispatchQueue:completionHandler:]_block_invoke
+ ___68+[CUFile renameWithOldPath:newPath:dispatchQueue:completionHandler:]_block_invoke
+ ___BonjourAdvertiserSetDomain_block_invoke
+ ___BonjourAdvertiserSetFlags_block_invoke
+ ___BonjourAdvertiserSetInterfaceIndex_block_invoke
+ ___BonjourAdvertiserSetInterfaceName_block_invoke
+ ___BonjourAdvertiserSetName_block_invoke
+ ___BonjourAdvertiserSetP2P_block_invoke
+ ___BonjourAdvertiserSetPort_block_invoke
+ ___BonjourAdvertiserSetServiceType_block_invoke
+ ___BonjourAdvertiserSetTXTRecord_block_invoke
+ ___BonjourAdvertiserSetTrafficFlags_block_invoke
+ ____BonjourAdvertiserApplyString_block_invoke
+ ____OPACKEncoderDispatchDataCallback_block_invoke
+ ___block_descriptor_32_e142_v24?0^{BonjourAdvertiserPrivate={__CFRuntimeBase=QAQ}^{LogCategory}^{_DNSServiceRef_t}I^{__CFData}?^{__CFString}qIQC*QI[17c]*Ci**SCI}8*16l
+ ___block_descriptor_41_e5_v8?0l
+ ___block_descriptor_57_e8_32b_e5_v8?0l
+ __dispatch_data_empty
+ _dispatch_data_create
+ _dispatch_data_create_concat
+ _gGlobalInitOnce
+ _objc_msgSend$characterAtIndex:
+ _objc_msgSend$deletePath:error:
+ _objc_msgSend$fetchAuthKitAccountWithAltDSID:error:
+ _objc_msgSend$removeItemAtPath:error:
+ _objc_msgSend$renameWithOldPath:newPath:error:
+ _objc_msgSend$setNeedsUserInteractivePriority:
+ _objc_msgSend$subarrayWithRange:
+ _objc_msgSend$substringFromIndex:
- GCC_except_table1317
- GCC_except_table1324
- GCC_except_table1325
- GCC_except_table1328
- GCC_except_table1375
- GCC_except_table1376
- GCC_except_table1407
- GCC_except_table1410
- GCC_except_table1416
- GCC_except_table1421
- GCC_except_table1424
- GCC_except_table1474
- GCC_except_table1475
- GCC_except_table2014
- GCC_except_table2054
- GCC_except_table2086
- GCC_except_table2302
- GCC_except_table2303
- GCC_except_table2326
- GCC_except_table2372
- GCC_except_table2456
- GCC_except_table2480
- GCC_except_table2517
- GCC_except_table2521
- GCC_except_table2588
- GCC_except_table2589
- GCC_except_table2591
- GCC_except_table2592
- GCC_except_table2594
- GCC_except_table2599
- GCC_except_table2603
- GCC_except_table2606
- GCC_except_table2609
- GCC_except_table2612
- GCC_except_table2619
- GCC_except_table2636
- GCC_except_table2697
- GCC_except_table3029
- GCC_except_table3030
- GCC_except_table3089
- GCC_except_table3160
- GCC_except_table3164
- GCC_except_table3208
- GCC_except_table3211
- GCC_except_table3212
- GCC_except_table3214
- GCC_except_table3236
- GCC_except_table3244
- GCC_except_table3249
- GCC_except_table3520
- GCC_except_table3570
- GCC_except_table3958
- GCC_except_table4006
- GCC_except_table4331
- GCC_except_table4339
- GCC_except_table4347
- GCC_except_table4462
- GCC_except_table4489
- GCC_except_table4490
- GCC_except_table4554
- GCC_except_table4558
- GCC_except_table4560
- GCC_except_table4562
- GCC_except_table4585
- GCC_except_table4659
- GCC_except_table4660
- GCC_except_table4661
- GCC_except_table4662
- GCC_except_table4664
- GCC_except_table4666
- GCC_except_table4668
- GCC_except_table4670
- GCC_except_table4674
- GCC_except_table4676
- GCC_except_table4695
- GCC_except_table4697
- GCC_except_table4698
- GCC_except_table4700
- GCC_except_table4701
- GCC_except_table4702
- GCC_except_table4704
- GCC_except_table4705
- GCC_except_table4706
- GCC_except_table4707
- GCC_except_table4709
- GCC_except_table4710
- GCC_except_table4711
- GCC_except_table4719
- GCC_except_table4728
- GCC_except_table4732
- GCC_except_table4733
- GCC_except_table4735
- GCC_except_table4736
- GCC_except_table4737
- GCC_except_table4738
- GCC_except_table4740
- GCC_except_table4743
- GCC_except_table4744
- GCC_except_table4746
- GCC_except_table4747
- GCC_except_table5381
- GCC_except_table5385
- GCC_except_table5390
- GCC_except_table5408
- GCC_except_table5417
- GCC_except_table5666
- GCC_except_table5667
- GCC_except_table5680
- GCC_except_table657
- GCC_except_table758
- GCC_except_table773
- GCC_except_table775
- GCC_except_table778
- GCC_except_table980
- __GlobalEnsureInitialized
- _objc_msgSend$authKitAccountWithAltDSID:error:
CStrings:
+ "### Clear TXT record failed: %#m\n"
+ "### Limit excessive MAC addresses: count=%d, max=%d"
+ "### Limit excessive MAC addresses: peer=%@, count=%d, max=%d"
+ ".."
+ "Bad new path"
+ "Bad old path"
+ "Empty filename: %@"
+ "Evicting stale TXT record for %s.%s%s%%%u: %#{txt}"
+ "Remove failed: path=%@"
+ "Rename failed: %@ -> %@"
+ "Unsafe filename: %@"
+ "macAddrs"
+ "v24@?0^{BonjourAdvertiserPrivate={__CFRuntimeBase=QAQ}^{LogCategory}@^{_DNSServiceRef_t}I^{__CFData}@?^{__CFString}q@I@QC*QI[17c]*Ci**SCI}8*16"
+ "void _PairingSessionLimitPeerInfo(PairingSessionRef)"
```
