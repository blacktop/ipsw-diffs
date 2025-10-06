## CoreSuggestions

> `/System/Library/PrivateFrameworks/CoreSuggestions.framework/CoreSuggestions`

```diff

-1226.0.1.0.0
-  __TEXT.__text: 0x80720
+1226.2.2.1.0
+  __TEXT.__text: 0x80ba4
   __TEXT.__auth_stubs: 0xd40
-  __TEXT.__objc_methlist: 0x81a4
+  __TEXT.__objc_methlist: 0x81bc
   __TEXT.__const: 0x7e0
   __TEXT.__gcc_except_tab: 0x6ac
   __TEXT.__cstring: 0x7677
   __TEXT.__oslogstring: 0x20f1
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x20a0
+  __TEXT.__unwind_info: 0x20b4
   __TEXT.__objc_classname: 0x1341
-  __TEXT.__objc_methname: 0x10d52
-  __TEXT.__objc_methtype: 0x50fe
-  __TEXT.__objc_stubs: 0x9140
+  __TEXT.__objc_methname: 0x10dd4
+  __TEXT.__objc_methtype: 0x51a5
+  __TEXT.__objc_stubs: 0x9160
   __DATA_CONST.__got: 0x150
   __DATA_CONST.__const: 0x2770
   __DATA_CONST.__objc_classlist: 0x4a8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xc0c8
-  __DATA_CONST.__objc_selrefs: 0x3c70
-  __DATA_CONST.__objc_arraydata: 0x250
+  __DATA_CONST.__objc_const: 0xc108
+  __DATA_CONST.__objc_selrefs: 0x3c80
+  __DATA_CONST.__objc_arraydata: 0x260
   __AUTH_CONST.__cfstring: 0x9f60
   __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__const: 0x2e0
-  __AUTH_CONST.__objc_dictobj: 0xc8
+  __AUTH_CONST.__const: 0x300
+  __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x30

   __DATA.__objc_superrefs: 0x438
   __DATA.__objc_ivar: 0x820
   __DATA.__data: 0x10a8
-  __DATA.__bss: 0x120
-  __DATA_DIRTY.__const: 0x2c0
+  __DATA.__bss: 0x130
+  __DATA_DIRTY.__const: 0x2a0
   __DATA_DIRTY.__objc_const: 0x3d28
   __DATA_DIRTY.__objc_data: 0x2e90
   __DATA_DIRTY.__data: 0x110
-  __DATA_DIRTY.__bss: 0x2e0
+  __DATA_DIRTY.__bss: 0x2d0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A7A1252A-40E9-3861-959C-025D54E2B0E3
-  Functions: 3190
-  Symbols:   10376
-  CStrings:  6190
+  UUID: 222C2013-5EEB-3F51-B4B7-7DB9F2FDF6AE
+  Functions: 3194
+  Symbols:   10387
+  CStrings:  6196
 
Symbols:
+ -[SGSuggestionsService suggestionsFromSearchableItem:options:processingType:error:]
+ -[SGSuggestionsService suggestionsFromSearchableItem:options:processingType:withCompletion:]
+ GCC_except_table1369
+ GCC_except_table1455
+ GCC_except_table1458
+ GCC_except_table1460
+ GCC_except_table1785
+ GCC_except_table2206
+ GCC_except_table2231
+ GCC_except_table2233
+ GCC_except_table2269
+ GCC_except_table2322
+ GCC_except_table2689
+ GCC_except_table3074
+ GCC_except_table3091
+ GCC_except_table3098
+ GCC_except_table3112
+ ___110-[SGSuggestionsService namesForDetail:limitTo:prependMaybe:onlySignificant:supportsInfoLookup:withCompletion:]_block_invoke.562
+ ___110-[SGSuggestionsService namesForDetail:limitTo:prependMaybe:onlySignificant:supportsInfoLookup:withCompletion:]_block_invoke.563
+ ___110-[SGSuggestionsService namesForDetail:limitTo:prependMaybe:onlySignificant:supportsInfoLookup:withCompletion:]_block_invoke.582
+ ___39+[SGSuggestionsService prepareForQuery]_block_invoke.443
+ ___43-[SGSuggestionsService cacheSnapshotFuture]_block_invoke.548
+ ___43-[SGSuggestionsService cacheSnapshotFuture]_block_invoke.549
+ ___43-[SGSuggestionsService cacheSnapshotFuture]_block_invoke.554
+ ___83-[SGSuggestionsService suggestionsFromSearchableItem:options:processingType:error:]_block_invoke
+ ___83-[SGSuggestionsService suggestionsFromSearchableItem:options:processingType:error:]_block_invoke_2
+ ___92-[SGSuggestionsService suggestionsFromSearchableItem:options:processingType:withCompletion:]_block_invoke
+ ___Block_byref_object_copy_.2193
+ ___Block_byref_object_copy_.3145
+ ___Block_byref_object_copy_.5283
+ ___Block_byref_object_copy_.5806
+ ___Block_byref_object_copy_.6202
+ ___Block_byref_object_copy_.9445
+ ___Block_byref_object_copy_.9555
+ ___Block_byref_object_dispose_.2194
+ ___Block_byref_object_dispose_.3146
+ ___Block_byref_object_dispose_.5284
+ ___Block_byref_object_dispose_.5807
+ ___Block_byref_object_dispose_.6203
+ ___Block_byref_object_dispose_.9446
+ ___Block_byref_object_dispose_.9556
+ ___block_descriptor_64_e8_32s40s_e25_v16?0?<v?"NSError">8ls32l8s40l8
+ ___block_literal_global.14.8706
+ ___block_literal_global.17.8709
+ ___block_literal_global.2150
+ ___block_literal_global.23.8715
+ ___block_literal_global.330
+ ___block_literal_global.412
+ ___block_literal_global.4942
+ ___block_literal_global.5288
+ ___block_literal_global.5574
+ ___block_literal_global.565
+ ___block_literal_global.570
+ ___block_literal_global.5793
+ ___block_literal_global.651
+ ___block_literal_global.6569
+ ___block_literal_global.7082
+ ___block_literal_global.7746
+ ___block_literal_global.8693
+ ___block_literal_global.9014
+ ___block_literal_global.9484
+ ___block_literal_global.9565
+ ___block_literal_global.96.9015
+ ___block_literal_global.9807
+ __entitlements_block_invoke._onceToken.568
+ __entitlements_block_invoke._pasExprOnceResult.567
+ __unnamed_array_storage.408
+ __unnamed_array_storage.409
+ __unnamed_array_storage.415
+ __unnamed_array_storage.416
+ __unnamed_array_storage.428
+ __unnamed_array_storage.429
+ __unnamed_array_storage.516
+ __unnamed_array_storage.520
+ __unnamed_array_storage.521
+ __unnamed_array_storage.524
+ __unnamed_array_storage.525
+ __unnamed_array_storage.7877
+ _objc_msgSend$suggestionsFromSearchableItem:options:processingType:withCompletion:
- GCC_except_table1364
- GCC_except_table1451
- GCC_except_table1454
- GCC_except_table1456
- GCC_except_table1781
- GCC_except_table2202
- GCC_except_table2227
- GCC_except_table2229
- GCC_except_table2265
- GCC_except_table2318
- GCC_except_table2685
- GCC_except_table3070
- GCC_except_table3087
- GCC_except_table3094
- GCC_except_table3108
- ___110-[SGSuggestionsService namesForDetail:limitTo:prependMaybe:onlySignificant:supportsInfoLookup:withCompletion:]_block_invoke.555
- ___110-[SGSuggestionsService namesForDetail:limitTo:prependMaybe:onlySignificant:supportsInfoLookup:withCompletion:]_block_invoke.556
- ___110-[SGSuggestionsService namesForDetail:limitTo:prependMaybe:onlySignificant:supportsInfoLookup:withCompletion:]_block_invoke.575
- ___39+[SGSuggestionsService prepareForQuery]_block_invoke.440
- ___43-[SGSuggestionsService cacheSnapshotFuture]_block_invoke.541
- ___43-[SGSuggestionsService cacheSnapshotFuture]_block_invoke.542
- ___43-[SGSuggestionsService cacheSnapshotFuture]_block_invoke.547
- ___84-[SGSuggestionsService dissectAttachmentsFromSearchableItem:options:withCompletion:]_block_invoke_2
- ___Block_byref_object_copy_.2199
- ___Block_byref_object_copy_.3174
- ___Block_byref_object_copy_.5322
- ___Block_byref_object_copy_.5836
- ___Block_byref_object_copy_.6232
- ___Block_byref_object_copy_.9480
- ___Block_byref_object_copy_.9590
- ___Block_byref_object_dispose_.2200
- ___Block_byref_object_dispose_.3175
- ___Block_byref_object_dispose_.5323
- ___Block_byref_object_dispose_.5837
- ___Block_byref_object_dispose_.6233
- ___Block_byref_object_dispose_.9481
- ___Block_byref_object_dispose_.9591
- ___block_descriptor_64_e8_32s40s48bs_e23_v16?0"SGXPCResponse"8ls32l8s40l8s48l8
- ___block_literal_global.14.8741
- ___block_literal_global.17.8744
- ___block_literal_global.2154
- ___block_literal_global.23.8750
- ___block_literal_global.327
- ___block_literal_global.409
- ___block_literal_global.4969
- ___block_literal_global.5325
- ___block_literal_global.558
- ___block_literal_global.5603
- ___block_literal_global.563
- ___block_literal_global.5823
- ___block_literal_global.644
- ___block_literal_global.6599
- ___block_literal_global.7112
- ___block_literal_global.7778
- ___block_literal_global.8728
- ___block_literal_global.9049
- ___block_literal_global.9519
- ___block_literal_global.96.9050
- ___block_literal_global.9600
- ___block_literal_global.9840
- __entitlements_block_invoke._onceToken.561
- __entitlements_block_invoke._pasExprOnceResult.560
- __unnamed_array_storage.405
- __unnamed_array_storage.406
- __unnamed_array_storage.412
- __unnamed_array_storage.413
- __unnamed_array_storage.425
- __unnamed_array_storage.426
- __unnamed_array_storage.513
- __unnamed_array_storage.514
- __unnamed_array_storage.518
- __unnamed_array_storage.7909
CStrings:
+ "@48@0:8@16Q24Q32^@40"
+ "suggestionsFromSearchableItem:options:processingType:error:"
+ "suggestionsFromSearchableItem:options:processingType:withCompletion:"
+ "v48@0:8@\"CSSearchableItem\"16Q24Q32@?<v@?@\"NSArray\"@\"NSError\">40"
+ "v48@0:8@\"CSSearchableItem\"16Q24Q32@?<v@?@\"SGXPCResponse1\">40"
+ "v48@0:8@16Q24Q32@?40"

```
