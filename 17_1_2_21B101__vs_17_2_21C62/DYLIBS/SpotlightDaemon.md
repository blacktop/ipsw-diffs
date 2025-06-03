## SpotlightDaemon

> `/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon`

```diff

-2274.0.3.0.0
-  __TEXT.__text: 0x70f88
+2274.8.2.0.0
+  __TEXT.__text: 0x710d4
   __TEXT.__auth_stubs: 0x1770
-  __TEXT.__objc_methlist: 0x2ed0
+  __TEXT.__objc_methlist: 0x2ee0
   __TEXT.__const: 0x1e0
-  __TEXT.__cstring: 0x506c
-  __TEXT.__gcc_except_tab: 0x26ac
-  __TEXT.__oslogstring: 0x602f
+  __TEXT.__cstring: 0x5055
+  __TEXT.__gcc_except_tab: 0x26b8
+  __TEXT.__oslogstring: 0x60b4
   __TEXT.__unwind_info: 0x19c4
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x409
-  __TEXT.__objc_methname: 0xa334
-  __TEXT.__objc_methtype: 0x1b5a
-  __TEXT.__objc_stubs: 0x8300
+  __TEXT.__objc_methname: 0xa24e
+  __TEXT.__objc_methtype: 0x1ba6
+  __TEXT.__objc_stubs: 0x82e0
   __DATA_CONST.__got: 0x428
-  __DATA_CONST.__const: 0x2cc0
+  __DATA_CONST.__const: 0x2ce8
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4290
-  __DATA_CONST.__objc_selrefs: 0x25b0
+  __DATA_CONST.__objc_const: 0x4260
+  __DATA_CONST.__objc_selrefs: 0x25a8
   __DATA_CONST.__objc_arraydata: 0x168
   __AUTH_CONST.__const: 0xaa0
   __AUTH_CONST.__cfstring: 0x3c40

   __DATA.__objc_protorefs: 0x8
   __DATA.__objc_classrefs: 0x370
   __DATA.__objc_superrefs: 0xd0
-  __DATA.__objc_ivar: 0x36c
+  __DATA.__objc_ivar: 0x368
   __DATA.__data: 0x3d8
   __DATA.__thread_ptrs: 0x8
   __DATA.__bss: 0x1a9

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 744DE98F-F401-3F94-B8FE-D571CA57D416
+  UUID: 5E87A635-5A56-3AAF-8F59-05E0AD99C72D
   Functions: 2036
-  Symbols:   6961
-  CStrings:  3773
+  Symbols:   6960
+  CStrings:  3772
 
Symbols:
+ -[MDSearchableIndexService entitledAttributes]
+ -[MDSearchableIndexService fetchAttributes:protectionClass:bundleID:identifiers:userCtx:flags:qos:reply:completionHandler:]
+ -[MDSearchableIndexService setEntitledAttributes:]
+ -[SDConnectionConfiguration entitledAttributes]
+ -[SPConcreteCoreSpotlightIndexer fetchAttributes:bundleID:identifiers:userCtx:flags:completion:]
+ -[SPConcreteCoreSpotlightIndexer fetchAttributes:bundleID:identifiers:userCtx:flags:completionHandler:]
+ -[SPCoreSpotlightIndexer fetchAttributes:protectionClass:bundleID:identifiers:userCtx:flags:qos:completionHandler:]
+ -[SPCoreSpotlightIndexer fetchAttributesForProtectionClass:attributes:bundleID:identifiers:userCtx:flags:completion:]
+ GCC_except_table266
+ GCC_except_table276
+ GCC_except_table301
+ GCC_except_table312
+ GCC_except_table322
+ GCC_except_table352
+ GCC_except_table360
+ GCC_except_table374
+ GCC_except_table392
+ GCC_except_table435
+ GCC_except_table490
+ GCC_except_table524
+ GCC_except_table533
+ GCC_except_table539
+ GCC_except_table563
+ GCC_except_table572
+ GCC_except_table593
+ GCC_except_table629
+ GCC_except_table656
+ GCC_except_table660
+ GCC_except_table667
+ GCC_except_table674
+ GCC_except_table680
+ GCC_except_table683
+ GCC_except_table691
+ GCC_except_table700
+ GCC_except_table705
+ GCC_except_table710
+ GCC_except_table715
+ GCC_except_table721
+ GCC_except_table727
+ GCC_except_table762
+ GCC_except_table764
+ GCC_except_table769
+ _OBJC_IVAR_$_MDSearchableIndexService._entitledAttributes
+ _OBJC_IVAR_$_SDConnectionConfiguration._entitledAttributes
+ ___103-[SPConcreteCoreSpotlightIndexer fetchAttributes:bundleID:identifiers:userCtx:flags:completionHandler:]_block_invoke
+ ___115-[SPCoreSpotlightIndexer fetchAttributes:protectionClass:bundleID:identifiers:userCtx:flags:qos:completionHandler:]_block_invoke
+ ___117-[SPCoreSpotlightIndexer fetchAttributesForProtectionClass:attributes:bundleID:identifiers:userCtx:flags:completion:]_block_invoke
+ ___123-[MDSearchableIndexService fetchAttributes:protectionClass:bundleID:identifiers:userCtx:flags:qos:reply:completionHandler:]_block_invoke
+ ___28-[CSSearchAgent startQuery:]_block_invoke.138
+ ___28-[CSSearchAgent startQuery:]_block_invoke.142
+ ___28-[CSSearchAgent startQuery:]_block_invoke.147
+ ___28-[CSSearchAgent startQuery:]_block_invoke.152
+ ___28-[CSSearchAgent startQuery:]_block_invoke_2.145
+ ___28-[CSSearchAgent startQuery:]_block_invoke_2.149
+ ___28-[CSSearchAgent startQuery:]_block_invoke_2.149.cold.1
+ ___28-[CSSearchAgent startQuery:]_block_invoke_2.149.cold.2
+ ___96-[SPConcreteCoreSpotlightIndexer fetchAttributes:bundleID:identifiers:userCtx:flags:completion:]_block_invoke
+ ___block_descriptor_84_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.2382
+ ___block_literal_global.2384
+ ___block_literal_global.2448
+ ___block_literal_global.2455
+ ___processItemsForImport_block_invoke.2402
+ __unnamed_array_storage.2389
+ __unnamed_array_storage.2393
+ __unnamed_array_storage.2445
+ _objc_msgSend$arrayWithObjects:
+ _objc_msgSend$decimalDigitCharacterSet
+ _objc_msgSend$entitledAttributes
+ _objc_msgSend$fetchAttributes:bundleID:identifiers:userCtx:flags:completion:
+ _objc_msgSend$fetchAttributes:bundleID:identifiers:userCtx:flags:completionHandler:
+ _objc_msgSend$fetchAttributes:protectionClass:bundleID:identifiers:userCtx:flags:qos:completionHandler:
+ _objc_msgSend$fetchAttributes:protectionClass:bundleID:identifiers:userCtx:flags:qos:reply:completionHandler:
+ _objc_msgSend$fetchAttributesForProtectionClass:attributes:bundleID:identifiers:userCtx:flags:completion:
+ _objc_msgSend$setEntitledAttributes:
- -[MDSearchableIndexService fetchAttributes:protectionClass:bundleID:identifiers:includeParents:qos:reply:completionHandler:]
- -[SDConnectionConfiguration allowDocumentUnderstandingEntitledAttributes]
- -[SDConnectionConfiguration allowPhotosEntitledAttributes]
- -[SDConnectionConfiguration allowSpotlightEntitledAttributes]
- -[SPConcreteCoreSpotlightIndexer fetchAttributes:bundleID:identifiers:includeParents:completion:]
- -[SPConcreteCoreSpotlightIndexer fetchAttributes:bundleID:identifiers:includeParents:completionHandler:]
- -[SPCoreSpotlightIndexer fetchAttributes:protectionClass:bundleID:identifiers:includeParents:qos:completionHandler:]
- GCC_except_table268
- GCC_except_table278
- GCC_except_table302
- GCC_except_table313
- GCC_except_table325
- GCC_except_table353
- GCC_except_table361
- GCC_except_table375
- GCC_except_table394
- GCC_except_table438
- GCC_except_table491
- GCC_except_table525
- GCC_except_table534
- GCC_except_table540
- GCC_except_table565
- GCC_except_table573
- GCC_except_table594
- GCC_except_table630
- GCC_except_table657
- GCC_except_table662
- GCC_except_table670
- GCC_except_table675
- GCC_except_table681
- GCC_except_table684
- GCC_except_table692
- GCC_except_table701
- GCC_except_table706
- GCC_except_table711
- GCC_except_table716
- GCC_except_table722
- GCC_except_table728
- GCC_except_table763
- GCC_except_table765
- GCC_except_table770
- _OBJC_IVAR_$_SDConnectionConfiguration._allowDocumentUnderstandingEntitledAttributes
- _OBJC_IVAR_$_SDConnectionConfiguration._allowPhotosEntitledAttributes
- _OBJC_IVAR_$_SDConnectionConfiguration._allowSpotlightEntitledAttributes
- ___103-[SPCoreSpotlightIndexer fetchAttributesForProtectionClass:attributes:bundleID:identifiers:completion:]_block_invoke
- ___104-[SPConcreteCoreSpotlightIndexer fetchAttributes:bundleID:identifiers:includeParents:completionHandler:]_block_invoke
- ___116-[SPCoreSpotlightIndexer fetchAttributes:protectionClass:bundleID:identifiers:includeParents:qos:completionHandler:]_block_invoke
- ___124-[MDSearchableIndexService fetchAttributes:protectionClass:bundleID:identifiers:includeParents:qos:reply:completionHandler:]_block_invoke
- ___28-[CSSearchAgent startQuery:]_block_invoke.137
- ___28-[CSSearchAgent startQuery:]_block_invoke.141
- ___28-[CSSearchAgent startQuery:]_block_invoke.146
- ___28-[CSSearchAgent startQuery:]_block_invoke.151
- ___28-[CSSearchAgent startQuery:]_block_invoke_2.144
- ___28-[CSSearchAgent startQuery:]_block_invoke_2.148
- ___28-[CSSearchAgent startQuery:]_block_invoke_2.148.cold.1
- ___28-[CSSearchAgent startQuery:]_block_invoke_2.148.cold.2
- ___45-[SPConcreteCoreSpotlightIndexer resumeIndex]_block_invoke_2
- ___97-[SPConcreteCoreSpotlightIndexer fetchAttributes:bundleID:identifiers:includeParents:completion:]_block_invoke
- ___block_literal_global.2379
- ___block_literal_global.2381
- ___block_literal_global.2445
- ___block_literal_global.2452
- ___processItemsForImport_block_invoke.2399
- __unnamed_array_storage.2386
- __unnamed_array_storage.2390
- __unnamed_array_storage.2442
- _objc_msgSend$allowDocumentUnderstandingEntitledAttributes
- _objc_msgSend$allowPhotosEntitledAttributes
- _objc_msgSend$allowSpotlightEntitledAttributes
- _objc_msgSend$fetchAttributes:bundleID:identifiers:includeParents:completion:
- _objc_msgSend$fetchAttributes:bundleID:identifiers:includeParents:completionHandler:
- _objc_msgSend$fetchAttributes:protectionClass:bundleID:identifiers:includeParents:qos:completionHandler:
- _objc_msgSend$fetchAttributes:protectionClass:bundleID:identifiers:includeParents:qos:reply:completionHandler:
- _objc_msgSend$setAllowDocumentUnderstandingEntitledAttributes:
- _objc_msgSend$setAllowPhotosEntitledAttributes:
- _objc_msgSend$setAllowSpotlightEntitledAttributes:
CStrings:
+ "Cannot delete in deleteItemsForEnumerator because index is null"
+ "Cannot delete in deleteItemsForEnumerator because index is read-only"
+ "Ti,N,V_entitledAttributes"
+ "Ti,R,N,V_entitledAttributes"
+ "_entitledAttributes"
+ "arrayWithObjects:"
+ "decimalDigitCharacterSet"
+ "entitledAttributes"
+ "fetchAttributes:bundleID:identifiers:userCtx:flags:completion:"
+ "fetchAttributes:bundleID:identifiers:userCtx:flags:completionHandler:"
+ "fetchAttributes:protectionClass:bundleID:identifiers:userCtx:flags:qos:completionHandler:"
+ "fetchAttributes:protectionClass:bundleID:identifiers:userCtx:flags:qos:reply:completionHandler:"
+ "fetchAttributesForProtectionClass:attributes:bundleID:identifiers:userCtx:flags:completion:"
+ "setEntitledAttributes:"
+ "v60@0:8@16@24@32@40i48@?52"
+ "v68@0:8@16@24@32@40@48i56@?60"
+ "v72@0:8@\"NSArray\"16@\"NSString\"24@\"NSString\"32@\"NSObject\"40@\"NSObject\"48I56I60@?<v@?@@\"NSError\">64"
+ "v72@0:8@16@24@32@40@48I56I60@?64"
+ "v80@0:8@16@24@32@40@48I56I60@64@?72"
- "SpotlightSodiumRanking"
- "TB,R,N,V_allowDocumentUnderstandingEntitledAttributes"
- "TB,R,N,V_allowPhotosEntitledAttributes"
- "TB,R,N,V_allowSpotlightEntitledAttributes"
- "_allowDocumentUnderstandingEntitledAttributes"
- "_allowPhotosEntitledAttributes"
- "_allowSpotlightEntitledAttributes"
- "allowDocumentUnderstandingEntitledAttributes"
- "allowPhotosEntitledAttributes"
- "allowSpotlightEntitledAttributes"
- "fetchAttributes:bundleID:identifiers:includeParents:completion:"
- "fetchAttributes:bundleID:identifiers:includeParents:completionHandler:"
- "fetchAttributes:protectionClass:bundleID:identifiers:includeParents:qos:completionHandler:"
- "fetchAttributes:protectionClass:bundleID:identifiers:includeParents:qos:reply:completionHandler:"
- "setAllowDocumentUnderstandingEntitledAttributes:"
- "setAllowPhotosEntitledAttributes:"
- "setAllowSpotlightEntitledAttributes:"
- "v64@0:8@\"NSArray\"16@\"NSString\"24@\"NSString\"32@\"NSObject\"40B48I52@?<v@?@@\"NSError\">56"
- "v64@0:8@16@24@32@40B48I52@?56"
- "v72@0:8@16@24@32@40B48I52@56@?64"

```
