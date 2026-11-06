## CoreUtils

> `/System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils`

```diff

-900.58.0.0.0
-  __TEXT.__text: 0x11f6d8
-  __TEXT.__objc_methlist: 0xa328
-  __TEXT.__cstring: 0x1e3fc
+910.31.0.0.0
+  __TEXT.__text: 0x1210f0
+  __TEXT.__objc_methlist: 0xa408
+  __TEXT.__cstring: 0x1e5e3
   __TEXT.__const: 0x22dc
-  __TEXT.__gcc_except_tab: 0x1ac8
-  __TEXT.__oslogstring: 0x48bd
-  __TEXT.__unwind_info: 0x3910
+  __TEXT.__gcc_except_tab: 0x1af4
+  __TEXT.__oslogstring: 0x4978
+  __TEXT.__unwind_info: 0x3998
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1510
+  __DATA_CONST.__const: 0x1560
   __DATA_CONST.__objc_classlist: 0x350
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5368
+  __DATA_CONST.__objc_selrefs: 0x5428
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x240
   __DATA_CONST.__objc_arraydata: 0x8
-  __DATA_CONST.__got: 0x678
-  __AUTH_CONST.__const: 0x40e8
-  __AUTH_CONST.__cfstring: 0x4020
-  __AUTH_CONST.__objc_const: 0x13ea8
+  __DATA_CONST.__got: 0x680
+  __AUTH_CONST.__const: 0x4198
+  __AUTH_CONST.__cfstring: 0x40a0
+  __AUTH_CONST.__objc_const: 0x13f28
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x15c0
+  __AUTH_CONST.__auth_got: 0x15d8
   __AUTH_CONST.__auth_ptr: 0x0
   __AUTH.__objc_data: 0x1e28
   __AUTH.__data: 0xa18
-  __DATA.__objc_ivar: 0x1540
+  __DATA.__objc_ivar: 0x1544
   __DATA.__data: 0x2f50
-  __DATA.__bss: 0x1190
+  __DATA.__bss: 0x11d0
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
+  Functions: 5859
+  Symbols:   11715
+  CStrings:  4898
 
Symbols:
+ +[CUFile deletePath:dispatchQueue:completionHandler:]
+ +[CUFile deletePath:error:]
+ +[CUFile renameWithOldPath:newPath:dispatchQueue:completionHandler:]
+ +[CUFile renameWithOldPath:newPath:error:]
+ +[CUFile validatedFilename:error:]
+ +[CUOPACK encodeObjectAsDispatchData:flags:error:]
+ -[CUNANDataSession _scheduleWFAStopTimeout]
+ -[CUNANDataSession _scheduleWFAStop]
+ -[CUPairingSession appInfoPostAuth]
+ -[CUPairingSession setAppInfoPostAuth:]
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
+ GCC_except_table2324
+ GCC_except_table2325
+ GCC_except_table2348
+ GCC_except_table2394
+ GCC_except_table2478
+ GCC_except_table2502
+ GCC_except_table2539
+ GCC_except_table2543
+ GCC_except_table2610
+ GCC_except_table2611
+ GCC_except_table2613
+ GCC_except_table2614
+ GCC_except_table2616
+ GCC_except_table2621
+ GCC_except_table2625
+ GCC_except_table2628
+ GCC_except_table2631
+ GCC_except_table2634
+ GCC_except_table2641
+ GCC_except_table2644
+ GCC_except_table2658
+ GCC_except_table2719
+ GCC_except_table3053
+ GCC_except_table3054
+ GCC_except_table3113
+ GCC_except_table3184
+ GCC_except_table3188
+ GCC_except_table3232
+ GCC_except_table3235
+ GCC_except_table3238
+ GCC_except_table3260
+ GCC_except_table3268
+ GCC_except_table3273
+ GCC_except_table3279
+ GCC_except_table3544
+ GCC_except_table3594
+ GCC_except_table3983
+ GCC_except_table4031
+ GCC_except_table4356
+ GCC_except_table4364
+ GCC_except_table4372
+ GCC_except_table4487
+ GCC_except_table4514
+ GCC_except_table4515
+ GCC_except_table4579
+ GCC_except_table4583
+ GCC_except_table4587
+ GCC_except_table4610
+ GCC_except_table4684
+ GCC_except_table4685
+ GCC_except_table4686
+ GCC_except_table4687
+ GCC_except_table4689
+ GCC_except_table4691
+ GCC_except_table4693
+ GCC_except_table4699
+ GCC_except_table4713
+ GCC_except_table4720
+ GCC_except_table4723
+ GCC_except_table4726
+ GCC_except_table4727
+ GCC_except_table4734
+ GCC_except_table4754
+ GCC_except_table4755
+ GCC_except_table4756
+ GCC_except_table4757
+ GCC_except_table4758
+ GCC_except_table4760
+ GCC_except_table4761
+ GCC_except_table4762
+ GCC_except_table4763
+ GCC_except_table4764
+ GCC_except_table4765
+ GCC_except_table4766
+ GCC_except_table4767
+ GCC_except_table4768
+ GCC_except_table4769
+ GCC_except_table4770
+ GCC_except_table4771
+ GCC_except_table4772
+ GCC_except_table4774
+ GCC_except_table4775
+ GCC_except_table4776
+ GCC_except_table4778
+ GCC_except_table5330
+ GCC_except_table5343
+ GCC_except_table5412
+ GCC_except_table5416
+ GCC_except_table5421
+ GCC_except_table5440
+ GCC_except_table5449
+ GCC_except_table5698
+ GCC_except_table5699
+ GCC_except_table5712
+ GCC_except_table669
+ GCC_except_table770
+ GCC_except_table785
+ GCC_except_table787
+ GCC_except_table790
+ GCC_except_table992
+ OBJC_IVAR_$_CUPairingSession._appInfoPostAuth
+ _CFDataSetLength
+ _OPACKEncoderCreateDispatchData
+ __BonjourAdvertiserApplyString
+ __GlobalInitialize
+ __OPACKEncodeRoot
+ __OPACKEncoderDispatchDataCallback
+ __OPACKEncoderDispatchDataFlushScratch
+ __PairingSessionLimitPeerInfo
+ ___36-[CUNANDataSession _scheduleWFAStop]_block_invoke
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
+ _objc_msgSend$_scheduleWFAStop
+ _objc_msgSend$_scheduleWFAStopTimeout
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
- GCC_except_table2622
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
- GCC_except_table3244
- GCC_except_table3249
- GCC_except_table3255
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
- GCC_except_table4688
- GCC_except_table4697
- GCC_except_table4698
- GCC_except_table4700
- GCC_except_table4702
- GCC_except_table4704
- GCC_except_table4705
- GCC_except_table4706
- GCC_except_table4707
- GCC_except_table4709
- GCC_except_table4710
- GCC_except_table4711
- GCC_except_table4719
- GCC_except_table4721
- GCC_except_table4728
- GCC_except_table4733
- GCC_except_table4737
- GCC_except_table4738
- GCC_except_table4739
- GCC_except_table4740
- GCC_except_table4741
- GCC_except_table4742
- GCC_except_table4743
- GCC_except_table4745
- GCC_except_table4749
- GCC_except_table4751
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
+ "### WFA DataSession stop timeout: %d seconds, id=%@"
+ ".."
+ "Bad new path"
+ "Bad old path"
+ "Empty filename: %@"
+ "Evicting stale TXT record for %s.%s%s%%%u: %#{txt}"
+ "HomeAccessory"
+ "Remove failed: path=%@"
+ "Rename failed: %@ -> %@"
+ "Unsafe filename: %@"
+ "[%llu] MeDevice unchanged: fml=<%@>, ids=<%@>, name='%@', isThisDevice=%s"
+ "appInfoPostAuth"
+ "macAddrs"
+ "v24@?0^{BonjourAdvertiserPrivate={__CFRuntimeBase=QAQ}^{LogCategory}@^{_DNSServiceRef_t}I^{__CFData}@?^{__CFString}q@I@QC*QI[17c]*Ci**SCI}8*16"
+ "void _PairingSessionLimitPeerInfo(PairingSessionRef)"
```
