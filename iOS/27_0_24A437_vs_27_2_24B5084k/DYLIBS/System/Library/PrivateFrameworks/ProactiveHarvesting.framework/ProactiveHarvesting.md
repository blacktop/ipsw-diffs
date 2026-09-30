## ProactiveHarvesting

> `/System/Library/PrivateFrameworks/ProactiveHarvesting.framework/ProactiveHarvesting`

```diff

-1346.0.1.0.0
-  __TEXT.__text: 0x3b2b4
-  __TEXT.__objc_methlist: 0x7b94
-  __TEXT.__const: 0x19c
-  __TEXT.__gcc_except_tab: 0x844
-  __TEXT.__cstring: 0x2556
-  __TEXT.__oslogstring: 0x44f7
-  __TEXT.__unwind_info: 0x2cb8
+1351.0.0.0.0
+  __TEXT.__text: 0x3bf18
+  __TEXT.__objc_methlist: 0x7bb4
+  __TEXT.__const: 0x1a4
+  __TEXT.__gcc_except_tab: 0x860
+  __TEXT.__cstring: 0x2592
+  __TEXT.__oslogstring: 0x47e2
+  __TEXT.__unwind_info: 0x2cd8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x13d8
+  __DATA_CONST.__const: 0x1448
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5528
+  __DATA_CONST.__objc_selrefs: 0x5538
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x118
   __DATA_CONST.__objc_arraydata: 0x18
-  __DATA_CONST.__got: 0x520
-  __AUTH_CONST.__const: 0x5c0
+  __DATA_CONST.__got: 0x528
+  __AUTH_CONST.__const: 0x580
   __AUTH_CONST.__cfstring: 0x2880
-  __AUTH_CONST.__objc_const: 0x40b8
+  __AUTH_CONST.__objc_const: 0x40d8
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x548
+  __AUTH_CONST.__auth_got: 0x560
   __AUTH.__objc_data: 0x280
   __AUTH.__data: 0x100
-  __DATA.__objc_ivar: 0x2c4
+  __DATA.__objc_ivar: 0x2c8
   __DATA.__data: 0x480
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0xd70
-  __DATA_DIRTY.__bss: 0x140
+  __DATA_DIRTY.__bss: 0x118
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler
   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
+  - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 2809
-  Symbols:   4547
-  CStrings:  675
+  Functions: 2817
+  Symbols:   4565
+  CStrings:  685
 
Symbols:
+ +[HVConsumerCoordinator maxContentAgeForDataSource:]
+ +[HVHarvestEligibility _admitContentByAgeWithCreationDate:maxContentAge:bundleId:itemId:eligibleExceptForAge:]
+ +[HVHarvestEligibility supportedFirstPartyItemEligibleBlock]
+ -[HVConsumerCoordinator maxContentAgeForDataSource:]
+ -[HVConsumerCoordinator registerMaxContentAge:oneDataSource:]
+ GCC_except_table156
+ GCC_except_table166
+ GCC_except_table169
+ GCC_except_table173
+ GCC_except_table244
+ GCC_except_table2714
+ GCC_except_table2739
+ GCC_except_table2742
+ GCC_except_table275
+ GCC_except_table320
+ GCC_except_table324
+ GCC_except_table326
+ GCC_except_table338
+ GCC_except_table411
+ GCC_except_table415
+ GCC_except_table422
+ GCC_except_table434
+ GCC_except_table455
+ GCC_except_table459
+ GCC_except_table464
+ GCC_except_table471
+ GCC_except_table485
+ GCC_except_table489
+ GCC_except_table490
+ GCC_except_table492
+ GCC_except_table497
+ GCC_except_table500
+ GCC_except_table505
+ GCC_except_table507
+ GCC_except_table517
+ GCC_except_table533
+ GCC_except_table616
+ GCC_except_table618
+ GCC_except_table620
+ GCC_except_table622
+ GCC_except_table663
+ GCC_except_table693
+ OBJC_IVAR_$_HVConsumerCoordinatorGuardedData._maxContentAgeByDataSource
+ _CFAbsoluteTimeGetCurrent
+ _TCCAccessCopyBundleIdentifiersDisabledForService
+ ___52-[HVConsumerCoordinator maxContentAgeForDataSource:]_block_invoke
+ ___61-[HVConsumerCoordinator registerMaxContentAge:oneDataSource:]_block_invoke
+ ___block_descriptor_40_e71_"HVEligibilityCheckResult"24?0?<"CSSearchableItem"?>8"NSString"16l
+ ___block_descriptor_40_e8_32bs_e8_v12?0i8ls32l8
+ ___block_descriptor_52_e8_32s40r_e42_v16?0"HVConsumerCoordinatorGuardedData"8ls32l8r40l8
+ __migrateIfNeededWithCompletion:._pasOnceToken13
+ __os_feature_enabled_impl
+ _dispatch_get_global_queue
+ _kTCCServiceSiriAccess
+ _objc_msgSend$maxContentAgeForDataSource:
+ _sharedInstance._pasOnceToken4
- GCC_except_table155
- GCC_except_table165
- GCC_except_table168
- GCC_except_table172
- GCC_except_table243
- GCC_except_table2706
- GCC_except_table2731
- GCC_except_table2734
- GCC_except_table309
- GCC_except_table315
- GCC_except_table321
- GCC_except_table332
- GCC_except_table403
- GCC_except_table405
- GCC_except_table416
- GCC_except_table428
- GCC_except_table447
- GCC_except_table449
- GCC_except_table458
- GCC_except_table465
- GCC_except_table479
- GCC_except_table483
- GCC_except_table484
- GCC_except_table486
- GCC_except_table491
- GCC_except_table493
- GCC_except_table494
- GCC_except_table501
- GCC_except_table511
- GCC_except_table527
- GCC_except_table594
- GCC_except_table598
- GCC_except_table600
- GCC_except_table604
- GCC_except_table655
- GCC_except_table685
- __migrateIfNeededWithCompletion:._pasOnceToken12
- _objc_retain_x28
CStrings:
+ "AppExclusions"
+ "HVConsumerCoordinator: _consumeAllContentFromOneDataSource<%{public}@>: dropped %tu over-age items via drain-time guard"
+ "HVConsumerCoordinator: _consumeOneContentFromOneDataSource: age gate fail-open for %@ dataSource %{public}@ (absoluteTimestamp=%f, now=%f)"
+ "HVConsumerCoordinator: _consumeOneContentFromOneDataSource: dropping over-age content %@ from bundle %@ dataSource %{public}@ (age=%.0fs, window=%.0fs)"
+ "HVConsumerCoordinator: registerMaxContentAge: %f oneDataSource: %{public}@ (stored: %f)"
+ "HVContentAdmission failed to register TCC access change handler."
+ "HVHarvestEligibility: age gate fail-open for item %@ from bundle %@ (contentCreationDate=%@)"
+ "HVHarvestEligibility: age gate rejecting item %@ from bundle %@ (age=%.0fs, window=%.0fs)"
+ "IntelligenceFlow"
+ "com.apple.tcc.access.changed"
```
