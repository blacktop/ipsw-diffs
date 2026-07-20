## WebBookmarks

> `/System/Library/PrivateFrameworks/WebBookmarks.framework/Versions/A/WebBookmarks`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_types`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-625.1.22.11.4
-  __TEXT.__text: 0xb1278
-  __TEXT.__objc_methlist: 0x8934
-  __TEXT.__const: 0x336
-  __TEXT.__gcc_except_tab: 0xc1f8
-  __TEXT.__cstring: 0xf64c
-  __TEXT.__oslogstring: 0xa4bf
+625.1.24.11.2
+  __TEXT.__text: 0xb1cc4
+  __TEXT.__objc_methlist: 0x8964
+  __TEXT.__const: 0x346
+  __TEXT.__gcc_except_tab: 0xc344
+  __TEXT.__cstring: 0xf73a
+  __TEXT.__oslogstring: 0xa54b
   __TEXT.__dlopen_cstrs: 0x50
   __TEXT.__constg_swiftt: 0x60
   __TEXT.__swift5_typeref: 0x9
   __TEXT.__swift5_reflstr: 0x1c
   __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x4760
+  __TEXT.__unwind_info: 0x4788
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5048
+  __DATA_CONST.__objc_selrefs: 0x5068
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0x378
   __DATA_CONST.__got: 0x7e8
   __AUTH_CONST.__const: 0x3970
-  __AUTH_CONST.__cfstring: 0x6320
-  __AUTH_CONST.__objc_const: 0x9ce8
+  __AUTH_CONST.__cfstring: 0x63a0
+  __AUTH_CONST.__objc_const: 0x9d38
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x3c0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x5e8
+  __DATA.__objc_ivar: 0x5f0
   __DATA.__data: 0x1010
   __DATA.__bss: 0x60
   __DATA_DIRTY.__objc_data: 0x1450

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3766
-  Symbols:   8046
-  CStrings:  2068
+  Functions: 3771
+  Symbols:   8063
+  CStrings:  2074
 
Symbols:
+ +[WBBookmarkSyncData _decodedTrimmedBookmarkSyncDataWithContentsOfData:]
+ +[WBBookmarkSyncData containsRecordInContentsOfData:]
+ -[WebBookmarkCollection _mergeDuplicateSpecialFolders]
+ -[WebBookmarkCollection bookmarksPendingFeatureTextBackfill:shouldResetStuckBookmarks:foundBookmarksNeedingBackfill:]
+ -[_WBBookmarkSyncDataForFieldSetupDecoding hasRecord]
+ GCC_except_table319
+ GCC_except_table327
+ GCC_except_table328
+ GCC_except_table336
+ GCC_except_table342
+ GCC_except_table362
+ GCC_except_table372
+ GCC_except_table373
+ GCC_except_table378
+ GCC_except_table383
+ GCC_except_table386
+ GCC_except_table389
+ GCC_except_table394
+ GCC_except_table395
+ GCC_except_table413
+ GCC_except_table418
+ GCC_except_table427
+ GCC_except_table430
+ GCC_except_table431
+ GCC_except_table438
+ GCC_except_table444
+ GCC_except_table445
+ GCC_except_table449
+ GCC_except_table450
+ GCC_except_table463
+ GCC_except_table466
+ GCC_except_table470
+ GCC_except_table471
+ GCC_except_table475
+ GCC_except_table478
+ GCC_except_table484
+ GCC_except_table500
+ GCC_except_table503
+ GCC_except_table507
+ GCC_except_table508
+ GCC_except_table520
+ GCC_except_table521
+ GCC_except_table524
+ GCC_except_table525
+ GCC_except_table542
+ GCC_except_table548
+ GCC_except_table552
+ GCC_except_table553
+ GCC_except_table561
+ GCC_except_table564
+ GCC_except_table567
+ GCC_except_table577
+ GCC_except_table580
+ GCC_except_table583
+ GCC_except_table600
+ GCC_except_table601
+ GCC_except_table608
+ GCC_except_table611
+ GCC_except_table612
+ OBJC_IVAR_$_WebBookmarkCollection._isApplyingInMemoryChanges
+ OBJC_IVAR_$__WBBookmarkSyncDataForFieldSetupDecoding._hasRecord
+ __ZZ54-[WebBookmarkCollection _mergeDuplicateSpecialFolders]E32specialIDsWithCanonicalServerIDs
+ ___54-[WebBookmarkCollection _mergeDuplicateSpecialFolders]_block_invoke
+ _objc_msgSend$_decodedTrimmedBookmarkSyncDataWithContentsOfData:
+ _objc_msgSend$_mergeDuplicateSpecialFolders
+ _objc_msgSend$containsRecordInContentsOfData:
+ _objc_msgSend$hasRecord
+ _objc_msgSend$setHasFetchedFeatureText:
- -[WebBookmarkCollection bookmarksPendingFeatureTextBackfill:]
- GCC_except_table326
- GCC_except_table332
- GCC_except_table338
- GCC_except_table361
- GCC_except_table374
- GCC_except_table375
- GCC_except_table384
- GCC_except_table387
- GCC_except_table390
- GCC_except_table391
- GCC_except_table400
- GCC_except_table401
- GCC_except_table415
- GCC_except_table420
- GCC_except_table429
- GCC_except_table435
- GCC_except_table436
- GCC_except_table440
- GCC_except_table446
- GCC_except_table447
- GCC_except_table455
- GCC_except_table456
- GCC_except_table465
- GCC_except_table468
- GCC_except_table473
- GCC_except_table474
- GCC_except_table479
- GCC_except_table482
- GCC_except_table486
- GCC_except_table504
- GCC_except_table505
- GCC_except_table510
- GCC_except_table511
- GCC_except_table522
- GCC_except_table523
- GCC_except_table529
- GCC_except_table530
- GCC_except_table544
- GCC_except_table550
- GCC_except_table554
- GCC_except_table555
- GCC_except_table563
- GCC_except_table570
- GCC_except_table571
- GCC_except_table579
- GCC_except_table582
- GCC_except_table585
- GCC_except_table606
- GCC_except_table609
- GCC_except_table610
CStrings:
+ "625.1.23"
+ "Merging duplicate special folders left behind by a faulty sync-data reset (rdar://179124635)"
+ "Repairing %zu folder(s) claiming special ID %d"
+ "UPDATE bookmarks SET special_id = 0, editable = 1, deletable = 1 WHERE id = %u"
+ "feature_text IS NULL AND type = 0 AND syncable = 1 AND deleted = 0 AND editable = 1 AND deletable = 1"
+ "special_id = %d AND deleted = 0 ORDER BY id ASC"
```
