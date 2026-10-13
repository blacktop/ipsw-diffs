## WebBookmarks

> `/System/Library/PrivateFrameworks/WebBookmarks.framework/WebBookmarks`

```diff

-625.2.7.1.0
-  __TEXT.__text: 0xea7b4
-  __TEXT.__objc_methlist: 0x8bc8
+625.2.8.10.4
+  __TEXT.__text: 0xeba1c
+  __TEXT.__objc_methlist: 0x8c88
   __TEXT.__const: 0x2058
-  __TEXT.__gcc_except_tab: 0xc46c
-  __TEXT.__cstring: 0x10210
+  __TEXT.__gcc_except_tab: 0xc674
+  __TEXT.__cstring: 0x102e0
   __TEXT.__oslogstring: 0xb63c
   __TEXT.__dlopen_cstrs: 0xb2
   __TEXT.__constg_swiftt: 0xadc

   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_assocty: 0xa0
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0x6a10
+  __TEXT.__unwind_info: 0x6af8
   __TEXT.__eh_frame: 0x3d68
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3280
+  __DATA_CONST.__const: 0x3328
   __DATA_CONST.__objc_classlist: 0x260
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5158
+  __DATA_CONST.__objc_selrefs: 0x51a8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1f0
   __DATA_CONST.__objc_arraydata: 0x370
-  __DATA_CONST.__got: 0xa20
+  __DATA_CONST.__got: 0xa28
   __AUTH_CONST.__const: 0x2be8
-  __AUTH_CONST.__cfstring: 0x6540
-  __AUTH_CONST.__objc_const: 0xa848
+  __AUTH_CONST.__cfstring: 0x65c0
+  __AUTH_CONST.__objc_const: 0xa8a8
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x3c0
   __AUTH_CONST.__objc_dictobj: 0x50

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4948
-  Symbols:   6611
-  CStrings:  2198
+  Functions: 4973
+  Symbols:   6642
+  CStrings:  2203
 
Symbols:
+ -[WBBookmarkDBAccess item:isDescendantOfFolderWithType:]
+ -[WBTabCollection deletePebblePinnedSuggestions]
+ -[WBTabCollection migratePebblePinnedSuggestionsToBookmarkCollection:]
+ -[WBTabCollection pebblePinnedSuggestionsFolderIDIfExists]
+ -[WBTabCollection pebblePinnedSuggestionsFolder]
+ -[WBTabCollection pebblePinnedSuggestions]
+ -[WebBookmarkCollection _specialIDOfBookmarkWithID:]
+ -[WebBookmarkCollection doesBookmark:haveAncestorWithSpecialID:]
+ -[WebBookmarkCollection enumerateBookmarks:andReadingListItems:andPinnedSuggestions:matchingString:usingBlock:]
+ -[WebBookmarkCollection firstPebblePinnedSuggestionWithURLMatchingString:]
+ -[WebBookmarkCollection isBookmarkPebblePinnedSuggestion:]
+ -[WebBookmarkCollection migratePebblePinnedSuggestionsToBookmarkCollection:]
+ -[WebBookmarkCollection pebblePinnedSuggestionsFolder]
+ -[WebBookmarkCollection pebblePinnedSuggestions]
+ -[WebBookmarkReadonlyCollection enumerateBookmarks:andReadingListItems:andPinnedSuggestions:matchingString:usingBlock:]
+ -[WebBookmarkReadonlyCollection isBookmarkPebblePinnedSuggestion:]
+ GCC_except_table137
+ GCC_except_table167
+ GCC_except_table186
+ GCC_except_table205
+ GCC_except_table236
+ GCC_except_table246
+ GCC_except_table265
+ GCC_except_table277
+ GCC_except_table288
+ GCC_except_table305
+ GCC_except_table311
+ GCC_except_table317
+ GCC_except_table321
+ GCC_except_table330
+ GCC_except_table333
+ GCC_except_table334
+ GCC_except_table336
+ GCC_except_table348
+ GCC_except_table353
+ GCC_except_table366
+ GCC_except_table376
+ GCC_except_table377
+ GCC_except_table382
+ GCC_except_table386
+ GCC_except_table387
+ GCC_except_table390
+ GCC_except_table392
+ GCC_except_table398
+ GCC_except_table413
+ GCC_except_table418
+ GCC_except_table427
+ GCC_except_table430
+ GCC_except_table431
+ GCC_except_table432
+ GCC_except_table433
+ GCC_except_table435
+ GCC_except_table445
+ GCC_except_table450
+ GCC_except_table451
+ GCC_except_table454
+ GCC_except_table455
+ GCC_except_table456
+ GCC_except_table470
+ GCC_except_table474
+ GCC_except_table475
+ GCC_except_table476
+ GCC_except_table479
+ GCC_except_table484
+ GCC_except_table504
+ GCC_except_table506
+ GCC_except_table507
+ GCC_except_table522
+ GCC_except_table523
+ GCC_except_table526
+ GCC_except_table527
+ GCC_except_table528
+ GCC_except_table544
+ GCC_except_table553
+ GCC_except_table554
+ GCC_except_table564
+ GCC_except_table566
+ GCC_except_table567
+ GCC_except_table568
+ GCC_except_table576
+ GCC_except_table579
+ GCC_except_table582
+ GCC_except_table597
+ GCC_except_table598
+ GCC_except_table599
+ GCC_except_table600
+ GCC_except_table601
+ GCC_except_table602
+ GCC_except_table617
+ GCC_except_table618
+ GCC_except_table619
+ _BookmarksPebblePinnedSuggestionsSpecialID
+ _CKBAFolderTypeForBookmark
+ _WBSCloudBookmarkListRecordNamePinnedSuggestions
+ ___119-[WebBookmarkReadonlyCollection enumerateBookmarks:andReadingListItems:andPinnedSuggestions:matchingString:usingBlock:]_block_invoke
+ ___42-[WBTabCollection pebblePinnedSuggestions]_block_invoke
+ ___42-[WBTabCollection pebblePinnedSuggestions]_block_invoke_2
+ ___48-[WBTabCollection deletePebblePinnedSuggestions]_block_invoke
+ ___48-[WBTabCollection deletePebblePinnedSuggestions]_block_invoke_2
+ ___48-[WBTabCollection pebblePinnedSuggestionsFolder]_block_invoke
+ ___48-[WBTabCollection pebblePinnedSuggestionsFolder]_block_invoke_2
+ ___58-[WBTabCollection pebblePinnedSuggestionsFolderIDIfExists]_block_invoke
+ ___58-[WBTabCollection pebblePinnedSuggestionsFolderIDIfExists]_block_invoke_2
+ ___66-[WebBookmarkReadonlyCollection isBookmarkPebblePinnedSuggestion:]_block_invoke
+ ___70-[WBTabCollection migratePebblePinnedSuggestionsToBookmarkCollection:]_block_invoke
+ ___block_descriptor_40_ea8_32s_e14_"NSArray"8?0ls32l8
+ ___block_descriptor_40_ea8_32s_e18_"WebBookmark"8?0ls32l8
+ ___block_descriptor_40_ea8_32s_e5_i8?0ls32l8
+ ___block_descriptor_59_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- -[WebBookmarkCollection enumerateBookmarks:andReadingListItems:matchingString:usingBlock:]
- -[WebBookmarkReadonlyCollection enumerateBookmarks:andReadingListItems:matchingString:usingBlock:]
- GCC_except_table111
- GCC_except_table113
- GCC_except_table183
- GCC_except_table22
- GCC_except_table229
- GCC_except_table233
- GCC_except_table234
- GCC_except_table238
- GCC_except_table250
- GCC_except_table255
- GCC_except_table260
- GCC_except_table267
- GCC_except_table268
- GCC_except_table292
- GCC_except_table293
- GCC_except_table312
- GCC_except_table324
- GCC_except_table332
- GCC_except_table337
- GCC_except_table340
- GCC_except_table341
- GCC_except_table343
- GCC_except_table349
- GCC_except_table355
- GCC_except_table360
- GCC_except_table373
- GCC_except_table383
- GCC_except_table391
- GCC_except_table394
- GCC_except_table396
- GCC_except_table397
- GCC_except_table400
- GCC_except_table405
- GCC_except_table406
- GCC_except_table420
- GCC_except_table425
- GCC_except_table437
- GCC_except_table438
- GCC_except_table440
- GCC_except_table441
- GCC_except_table442
- GCC_except_table458
- GCC_except_table459
- GCC_except_table460
- GCC_except_table461
- GCC_except_table462
- GCC_except_table463
- GCC_except_table464
- GCC_except_table477
- GCC_except_table483
- GCC_except_table486
- GCC_except_table489
- GCC_except_table491
- GCC_except_table495
- GCC_except_table513
- GCC_except_table514
- GCC_except_table518
- GCC_except_table533
- GCC_except_table534
- GCC_except_table535
- GCC_except_table536
- GCC_except_table537
- GCC_except_table551
- GCC_except_table560
- GCC_except_table561
- GCC_except_table571
- GCC_except_table573
- GCC_except_table574
- GCC_except_table575
- GCC_except_table583
- GCC_except_table586
- GCC_except_table589
- GCC_except_table611
- GCC_except_table612
- ___98-[WebBookmarkReadonlyCollection enumerateBookmarks:andReadingListItems:matchingString:usingBlock:]_block_invoke
- ___block_descriptor_58_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
CStrings:
+ " AND parent NOT IN (SELECT id FROM bookmarks WHERE special_id = %ld)"
+ "AND parent NOT IN (SELECT id FROM bookmarks WHERE special_id = %ld)"
+ "Pinned Suggestions"
+ "SELECT special_id FROM bookmarks WHERE id = %d"
+ "i8@?0"
```
