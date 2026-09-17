## ProactiveHarvesting

> `/System/Library/PrivateFrameworks/ProactiveHarvesting.framework/Versions/A/ProactiveHarvesting`

```diff

-1345.0.3.0.0
-  __TEXT.__text: 0x3dfdc
-  __TEXT.__objc_methlist: 0x7b94
-  __TEXT.__const: 0x1a4
-  __TEXT.__gcc_except_tab: 0x868
-  __TEXT.__cstring: 0x2448
-  __TEXT.__oslogstring: 0x455c
-  __TEXT.__unwind_info: 0x2d30
+1351.0.0.0.0
+  __TEXT.__text: 0x3ecf0
+  __TEXT.__objc_methlist: 0x7bb4
+  __TEXT.__const: 0x1ac
+  __TEXT.__gcc_except_tab: 0x884
+  __TEXT.__cstring: 0x2484
+  __TEXT.__oslogstring: 0x4847
+  __TEXT.__unwind_info: 0x2d58
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x528
+  __DATA_CONST.__const: 0x548
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5548
+  __DATA_CONST.__objc_selrefs: 0x5558
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x118
   __DATA_CONST.__objc_arraydata: 0x18
-  __DATA_CONST.__got: 0x518
-  __AUTH_CONST.__const: 0x1790
+  __DATA_CONST.__got: 0x520
+  __AUTH_CONST.__const: 0x17b0
   __AUTH_CONST.__cfstring: 0x2780
-  __AUTH_CONST.__objc_const: 0x40b8
+  __AUTH_CONST.__objc_const: 0x40d8
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x460
+  __AUTH_CONST.__auth_got: 0x480
   __AUTH.__objc_data: 0x280
   __AUTH.__data: 0x100
-  __DATA.__objc_ivar: 0x2c4
+  __DATA.__objc_ivar: 0x2c8
   __DATA.__data: 0x480
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0xd70
-  __DATA_DIRTY.__bss: 0x120
+  __DATA_DIRTY.__bss: 0x118
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/Versions/A/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/Versions/A/ProactiveSupport
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SetupAssistantFramework.framework/Versions/A/SetupAssistantFramework
+  - /System/Library/PrivateFrameworks/TCC.framework/Versions/A/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 2853
-  Symbols:   4579
-  CStrings:  668
+  Functions: 2861
+  Symbols:   4598
+  CStrings:  678
 
Symbols:
+ +[HVConsumerCoordinator maxContentAgeForDataSource:]
+ +[HVHarvestEligibility _admitContentByAgeWithCreationDate:maxContentAge:bundleId:itemId:eligibleExceptForAge:]
+ +[HVHarvestEligibility supportedFirstPartyItemEligibleBlock]
+ -[HVConsumerCoordinator maxContentAgeForDataSource:]
+ -[HVConsumerCoordinator registerMaxContentAge:oneDataSource:]
+ GCC_except_table162
+ GCC_except_table174
+ GCC_except_table187
+ GCC_except_table190
+ GCC_except_table194
+ GCC_except_table265
+ GCC_except_table2756
+ GCC_except_table2781
+ GCC_except_table2785
+ GCC_except_table296
+ GCC_except_table335
+ GCC_except_table342
+ GCC_except_table343
+ GCC_except_table351
+ GCC_except_table353
+ GCC_except_table365
+ GCC_except_table442
+ GCC_except_table446
+ GCC_except_table453
+ GCC_except_table467
+ GCC_except_table487
+ GCC_except_table490
+ GCC_except_table498
+ GCC_except_table503
+ GCC_except_table510
+ GCC_except_table524
+ GCC_except_table528
+ GCC_except_table529
+ GCC_except_table537
+ GCC_except_table540
+ GCC_except_table545
+ GCC_except_table547
+ GCC_except_table559
+ GCC_except_table575
+ GCC_except_table658
+ GCC_except_table660
+ GCC_except_table662
+ GCC_except_table664
+ GCC_except_table705
+ GCC_except_table735
+ OBJC_IVAR_$_HVConsumerCoordinatorGuardedData._maxContentAgeByDataSource
+ _CFAbsoluteTimeGetCurrent
+ _TCCAccessCopyBundleIdentifiersDisabledForService
+ ___52-[HVConsumerCoordinator maxContentAgeForDataSource:]_block_invoke
+ ___61-[HVConsumerCoordinator registerMaxContentAge:oneDataSource:]_block_invoke
+ ___block_descriptor_40_e71_"HVEligibilityCheckResult"24?0?<"CSSearchableItem"?>8"NSString"16l
+ ___block_descriptor_40_e8_32bs_e8_v12?0i8l
+ ___block_descriptor_52_e8_32s40r_e42_v16?0"HVConsumerCoordinatorGuardedData"8l
+ __os_feature_enabled_impl
+ _dispatch_get_global_queue
+ _kTCCServiceSiriAccess
+ _migrateIfNeededWithCompletion:._pasOnceToken13
+ _objc_msgSend$maxContentAgeForDataSource:
+ sharedInstance._pasOnceToken4
- GCC_except_table161
- GCC_except_table173
- GCC_except_table185
- GCC_except_table188
- GCC_except_table192
- GCC_except_table264
- GCC_except_table2748
- GCC_except_table2773
- GCC_except_table2777
- GCC_except_table330
- GCC_except_table337
- GCC_except_table338
- GCC_except_table346
- GCC_except_table348
- GCC_except_table359
- GCC_except_table430
- GCC_except_table440
- GCC_except_table447
- GCC_except_table461
- GCC_except_table481
- GCC_except_table484
- GCC_except_table492
- GCC_except_table497
- GCC_except_table504
- GCC_except_table518
- GCC_except_table522
- GCC_except_table523
- GCC_except_table525
- GCC_except_table533
- GCC_except_table534
- GCC_except_table541
- GCC_except_table553
- GCC_except_table569
- GCC_except_table636
- GCC_except_table640
- GCC_except_table642
- GCC_except_table646
- GCC_except_table697
- GCC_except_table727
- _migrateIfNeededWithCompletion:._pasOnceToken12
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
