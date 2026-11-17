## CoreUtils

> `/System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils`

```diff

-920.2.0.0.0
-  __TEXT.__text: 0x1155cc
-  __TEXT.__objc_methlist: 0xa118
-  __TEXT.__cstring: 0x1d8de
+920.6.0.0.0
+  __TEXT.__text: 0x115f28
+  __TEXT.__objc_methlist: 0xa160
+  __TEXT.__cstring: 0x1da97
   __TEXT.__const: 0x229c
   __TEXT.__gcc_except_tab: 0x1bcc
   __TEXT.__oslogstring: 0x4a72
-  __TEXT.__unwind_info: 0x49c8
+  __TEXT.__unwind_info: 0x4a00
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2a58
+  __DATA_CONST.__const: 0x2a80
   __DATA_CONST.__objc_classlist: 0x350
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x51e0
+  __DATA_CONST.__objc_selrefs: 0x5200
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x240
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__got: 0x6c8
   __AUTH_CONST.__const: 0x28a8
   __AUTH_CONST.__cfstring: 0x45c0
-  __AUTH_CONST.__objc_const: 0x13cc0
+  __AUTH_CONST.__objc_const: 0x13d18
   __AUTH_CONST.__objc_intobj: 0x258
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x1870
   __AUTH.__objc_data: 0x2030
   __AUTH.__data: 0xa00
-  __DATA.__objc_ivar: 0x1514
+  __DATA.__objc_ivar: 0x151c
   __DATA.__data: 0x2f50
   __DATA.__common: 0x2a
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0x88
-  __DATA_DIRTY.__bss: 0x201
+  __DATA_DIRTY.__bss: 0x1c9
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 5821
-  Symbols:   10246
-  CStrings:  4870
+  Functions: 5835
+  Symbols:   10261
+  CStrings:  4883
 
Symbols:
+ -[CUHomeKitManager homeManagerDidUpdateCurrentHome:]
+ -[CUHomeKitManager homeManagerDidUpdatePrimaryHome:]
+ -[CUUserNotificationSession _addRequestWithResultBlock:error:]
+ -[CUUserNotificationSession mockPostCount]
+ -[CUUserNotificationSession repost]
+ GCC_except_table2293
+ GCC_except_table2294
+ GCC_except_table2317
+ GCC_except_table2362
+ GCC_except_table2446
+ GCC_except_table2470
+ GCC_except_table2511
+ GCC_except_table2579
+ GCC_except_table2581
+ GCC_except_table2582
+ GCC_except_table2584
+ GCC_except_table2593
+ GCC_except_table2596
+ GCC_except_table2599
+ GCC_except_table2602
+ GCC_except_table2609
+ GCC_except_table2612
+ GCC_except_table2626
+ GCC_except_table2687
+ GCC_except_table3021
+ GCC_except_table3022
+ GCC_except_table3110
+ GCC_except_table3132
+ GCC_except_table3170
+ GCC_except_table3217
+ GCC_except_table3218
+ GCC_except_table3220
+ GCC_except_table3242
+ GCC_except_table3250
+ GCC_except_table3255
+ GCC_except_table3261
+ GCC_except_table3534
+ GCC_except_table3590
+ GCC_except_table3964
+ GCC_except_table4012
+ GCC_except_table4284
+ GCC_except_table4342
+ GCC_except_table4349
+ GCC_except_table4357
+ GCC_except_table4472
+ GCC_except_table4499
+ GCC_except_table4500
+ GCC_except_table4562
+ GCC_except_table4566
+ GCC_except_table4568
+ GCC_except_table4570
+ GCC_except_table4593
+ GCC_except_table4668
+ GCC_except_table4669
+ GCC_except_table4670
+ GCC_except_table4672
+ GCC_except_table4674
+ GCC_except_table4676
+ GCC_except_table4678
+ GCC_except_table4682
+ GCC_except_table4684
+ GCC_except_table4696
+ GCC_except_table4705
+ GCC_except_table4709
+ GCC_except_table4710
+ GCC_except_table4712
+ GCC_except_table4713
+ GCC_except_table4714
+ GCC_except_table4719
+ GCC_except_table4728
+ GCC_except_table4742
+ GCC_except_table4746
+ GCC_except_table4748
+ GCC_except_table4749
+ GCC_except_table4750
+ GCC_except_table4751
+ GCC_except_table4752
+ GCC_except_table4754
+ GCC_except_table4755
+ GCC_except_table4756
+ GCC_except_table4758
+ GCC_except_table5306
+ GCC_except_table5319
+ GCC_except_table5388
+ GCC_except_table5392
+ GCC_except_table5397
+ GCC_except_table5417
+ GCC_except_table5428
+ GCC_except_table5678
+ GCC_except_table5691
+ _OBJC_IVAR_$_CUHomeKitManager._bestUserID
+ _OBJC_IVAR_$_CUUserNotificationSession._mockPostCount
+ __PairingResetThrottleBucket
+ __PairingThrottleDelayLocked
+ __SetupServerSetupCodeVerified
+ ___35-[CUUserNotificationSession repost]_block_invoke
+ ___35-[CUUserNotificationSession repost]_block_invoke_2
+ ___35-[CUUserNotificationSession repost]_block_invoke_3
+ ___52-[CUHomeKitManager homeManagerDidUpdateCurrentHome:]_block_invoke
+ ___52-[CUHomeKitManager homeManagerDidUpdatePrimaryHome:]_block_invoke
+ ___62-[CUUserNotificationSession _addRequestWithResultBlock:error:]_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls40l8s32l8
+ _gPairingThrottle
- GCC_except_table2289
- GCC_except_table2290
- GCC_except_table2313
- GCC_except_table2358
- GCC_except_table2442
- GCC_except_table2466
- GCC_except_table2503
- GCC_except_table2574
- GCC_except_table2575
- GCC_except_table2577
- GCC_except_table2580
- GCC_except_table2585
- GCC_except_table2592
- GCC_except_table2595
- GCC_except_table2598
- GCC_except_table2605
- GCC_except_table2608
- GCC_except_table2622
- GCC_except_table2683
- GCC_except_table3017
- GCC_except_table3018
- GCC_except_table3106
- GCC_except_table3128
- GCC_except_table3162
- GCC_except_table3210
- GCC_except_table3213
- GCC_except_table3216
- GCC_except_table3238
- GCC_except_table3246
- GCC_except_table3251
- GCC_except_table3257
- GCC_except_table3530
- GCC_except_table3586
- GCC_except_table3960
- GCC_except_table4008
- GCC_except_table4273
- GCC_except_table4331
- GCC_except_table4338
- GCC_except_table4346
- GCC_except_table4461
- GCC_except_table4488
- GCC_except_table4489
- GCC_except_table4551
- GCC_except_table4555
- GCC_except_table4557
- GCC_except_table4559
- GCC_except_table4582
- GCC_except_table4656
- GCC_except_table4657
- GCC_except_table4658
- GCC_except_table4659
- GCC_except_table4661
- GCC_except_table4663
- GCC_except_table4665
- GCC_except_table4671
- GCC_except_table4673
- GCC_except_table4685
- GCC_except_table4692
- GCC_except_table4694
- GCC_except_table4695
- GCC_except_table4697
- GCC_except_table4698
- GCC_except_table4699
- GCC_except_table4701
- GCC_except_table4702
- GCC_except_table4704
- GCC_except_table4707
- GCC_except_table4721
- GCC_except_table4722
- GCC_except_table4723
- GCC_except_table4724
- GCC_except_table4725
- GCC_except_table4727
- GCC_except_table4730
- GCC_except_table4731
- GCC_except_table4739
- GCC_except_table5295
- GCC_except_table5308
- GCC_except_table5377
- GCC_except_table5381
- GCC_except_table5386
- GCC_except_table5405
- GCC_except_table5414
- GCC_except_table5663
- GCC_except_table5664
- _gPairingThrottleCounter
- _gPairingThrottleNextTicks
- _gPairingTries
CStrings:
+ "### Repost failed: %{error}\n"
+ "-[CUHomeKitManager homeManagerDidUpdateCurrentHome:]_block_invoke"
+ "-[CUHomeKitManager homeManagerDidUpdatePrimaryHome:]_block_invoke"
+ "-[CUUserNotificationSession _addRequestWithResultBlock:error:]"
+ "-[CUUserNotificationSession repost]_block_invoke"
+ "-[CUUserNotificationSession repost]_block_invoke_3"
+ "Best user changed: %@ -> %@"
+ "Failed"
+ "HomeManagerDidUpdateCurrentHome"
+ "HomeManagerDidUpdatePrimaryHome"
+ "Repost ignored: %s\n"
+ "Repost: %@\n"
+ "Reposted: %@, %{error}\n"
+ "Succeeded"
- "-[CUUserNotificationSession _runRequestAddStart:]"
```
