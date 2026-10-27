## WebBookmarks

> `/System/Library/PrivateFrameworks/WebBookmarks.framework/Versions/A/WebBookmarks`

```diff

-625.1.29.11.28
-  __TEXT.__text: 0xfc588
-  __TEXT.__objc_methlist: 0x8b80
+625.2.8.11.9
+  __TEXT.__text: 0xfd08c
+  __TEXT.__objc_methlist: 0x8bd0
   __TEXT.__const: 0x2058
-  __TEXT.__gcc_except_tab: 0xc388
-  __TEXT.__cstring: 0xfb30
-  __TEXT.__oslogstring: 0xb9ec
+  __TEXT.__gcc_except_tab: 0xc484
+  __TEXT.__cstring: 0xfbe0
+  __TEXT.__oslogstring: 0xbc9c
   __TEXT.__dlopen_cstrs: 0x50
   __TEXT.__constg_swiftt: 0xadc
   __TEXT.__swift5_typeref: 0xf5e

   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_assocty: 0xa0
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0x59d8
+  __TEXT.__unwind_info: 0x5a08
   __TEXT.__eh_frame: 0x3d18
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x50d0
+  __DATA_CONST.__objc_selrefs: 0x50f8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x378
   __DATA_CONST.__got: 0x9f0
   __AUTH_CONST.__const: 0x5668
-  __AUTH_CONST.__cfstring: 0x63e0
-  __AUTH_CONST.__objc_const: 0xa610
+  __AUTH_CONST.__cfstring: 0x6420
+  __AUTH_CONST.__objc_const: 0xa630
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x3c0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0xd98
   __AUTH_CONST.__auth_ptr: 0x440
-  __AUTH.__objc_data: 0x2a8
-  __AUTH.__data: 0x460
-  __DATA.__objc_ivar: 0x5fc
-  __DATA.__data: 0x1a78
-  __DATA.__bss: 0x1ce0
-  __DATA_DIRTY.__objc_data: 0x1450
-  __DATA_DIRTY.__data: 0xc8
-  __DATA_DIRTY.__bss: 0x1d8
+  __AUTH.__objc_data: 0x1d8
+  __AUTH.__data: 0xd8
+  __DATA.__objc_ivar: 0x600
+  __DATA.__data: 0x1a60
+  __DATA.__bss: 0x1cc0
+  __DATA_DIRTY.__objc_data: 0x1520
+  __DATA_DIRTY.__data: 0x468
+  __DATA_DIRTY.__bss: 0x1f8
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5001
-  Symbols:   8567
-  CStrings:  2173
+  Functions: 5010
+  Symbols:   8579
+  CStrings:  2183
 
Symbols:
+ -[WBTabCollection localTabGroupWithUUID:]
+ -[WBTabGroupManager localTabGroupWithUUID:]
+ -[WBWindowState initWithUUID:localTabGroup:sceneID:]
+ -[WebBookmarkCollection _shouldWaitForLockForVersionUpgradeMigrations]
+ -[WebBookmarkCollection _tryPerformDatabaseUpdatesWithApplyInMemoryChanges:secureDelete:shouldWaitForLock:updates:]
+ -[WebBookmarkTabCollection _localTabGroupWithUUID:]
+ GCC_except_table116
+ GCC_except_table132
+ GCC_except_table204
+ GCC_except_table243
+ GCC_except_table324
+ GCC_except_table326
+ GCC_except_table332
+ GCC_except_table338
+ GCC_except_table361
+ GCC_except_table374
+ GCC_except_table375
+ GCC_except_table380
+ GCC_except_table382
+ GCC_except_table384
+ GCC_except_table396
+ GCC_except_table397
+ GCC_except_table398
+ GCC_except_table415
+ GCC_except_table420
+ GCC_except_table429
+ GCC_except_table433
+ GCC_except_table434
+ GCC_except_table441
+ GCC_except_table447
+ GCC_except_table448
+ GCC_except_table452
+ GCC_except_table453
+ GCC_except_table454
+ GCC_except_table468
+ GCC_except_table475
+ GCC_except_table476
+ GCC_except_table477
+ GCC_except_table482
+ GCC_except_table489
+ GCC_except_table505
+ GCC_except_table507
+ GCC_except_table512
+ GCC_except_table513
+ GCC_except_table514
+ GCC_except_table525
+ GCC_except_table526
+ GCC_except_table530
+ GCC_except_table531
+ GCC_except_table547
+ GCC_except_table553
+ GCC_except_table557
+ GCC_except_table558
+ GCC_except_table566
+ GCC_except_table571
+ GCC_except_table573
+ GCC_except_table582
+ GCC_except_table605
+ GCC_except_table606
+ GCC_except_table607
+ GCC_except_table617
+ GCC_except_table618
+ GCC_except_table619
+ OBJC_IVAR_$_WebBookmarkCollection._didRequestDatabaseInterrupt
+ _WBBoundedTransactionLockWaitMilliseconds
+ _WBDatabaseBusyTimeoutMilliseconds
+ _ZN12WebBookmarks26BookmarkSQLReadTransactionC2EP7sqlite3PKNSt3__16atomicIbEE
+ _ZN12WebBookmarks27BookmarkSQLWriteTransactionC2EP7sqlite3NS0_17ShouldWaitForLockEPKNSt3__16atomicIbEE
+ __ZN12WebBookmarks26BookmarkSQLReadTransactionC1EP7sqlite3PKNSt3__16atomicIbEE
+ __ZN12WebBookmarks26BookmarkSQLReadTransactionC2EP7sqlite3PKNSt3__16atomicIbEE
+ __ZN12WebBookmarks27BookmarkSQLWriteTransactionC1EP7sqlite3NS0_17ShouldWaitForLockEPKNSt3__16atomicIbEE
+ __ZN12WebBookmarks27BookmarkSQLWriteTransactionC2EP7sqlite3NS0_17ShouldWaitForLockEPKNSt3__16atomicIbEE
+ ___111-[WebBookmarkCollection _updateDatabaseIfNewerVersion:wasLaunchedForSyncStringKey:upgradeSelector:versionType:]_block_invoke_2
+ ___115-[WebBookmarkCollection _tryPerformDatabaseUpdatesWithApplyInMemoryChanges:secureDelete:shouldWaitForLock:updates:]_block_invoke
+ ___41-[WBTabCollection localTabGroupWithUUID:]_block_invoke
+ _objc_msgSend$_localTabGroupWithUUID:
+ _objc_msgSend$_shouldWaitForLockForVersionUpgradeMigrations
+ _objc_msgSend$_tryPerformDatabaseUpdatesWithApplyInMemoryChanges:secureDelete:shouldWaitForLock:updates:
+ _objc_msgSend$safari_isSafariFamilyBundleIdentifier:
- GCC_except_table117
- GCC_except_table209
- GCC_except_table249
- GCC_except_table267
- GCC_except_table276
- GCC_except_table281
- GCC_except_table290
- GCC_except_table292
- GCC_except_table302
- GCC_except_table327
- GCC_except_table329
- GCC_except_table334
- GCC_except_table363
- GCC_except_table364
- GCC_except_table377
- GCC_except_table378
- GCC_except_table383
- GCC_except_table393
- GCC_except_table394
- GCC_except_table402
- GCC_except_table403
- GCC_except_table404
- GCC_except_table418
- GCC_except_table423
- GCC_except_table438
- GCC_except_table439
- GCC_except_table440
- GCC_except_table444
- GCC_except_table450
- GCC_except_table451
- GCC_except_table460
- GCC_except_table461
- GCC_except_table462
- GCC_except_table474
- GCC_except_table478
- GCC_except_table479
- GCC_except_table486
- GCC_except_table488
- GCC_except_table492
- GCC_except_table510
- GCC_except_table511
- GCC_except_table515
- GCC_except_table516
- GCC_except_table517
- GCC_except_table528
- GCC_except_table534
- GCC_except_table535
- GCC_except_table536
- GCC_except_table550
- GCC_except_table556
- GCC_except_table560
- GCC_except_table561
- GCC_except_table575
- GCC_except_table576
- GCC_except_table577
- GCC_except_table591
- GCC_except_table611
- GCC_except_table615
- GCC_except_table616
- _ZN12WebBookmarks26BookmarkSQLReadTransactionC2EP7sqlite3
- _ZN12WebBookmarks27BookmarkSQLWriteTransactionC2EP7sqlite3
- __43-[WBTabGroupManager insertUnnamedTabGroup:]_block_invoke
- __ZN12WebBookmarks26BookmarkSQLReadTransactionC1EP7sqlite3
- __ZN12WebBookmarks26BookmarkSQLReadTransactionC2EP7sqlite3
- __ZN12WebBookmarks27BookmarkSQLWriteTransactionC1EP7sqlite3
- __ZN12WebBookmarks27BookmarkSQLWriteTransactionC2EP7sqlite3
- ___97-[WebBookmarkCollection performDatabaseUpdatesWithTransaction:applyInMemoryChanges:secureDelete:]_block_invoke
CStrings:
+ "Abandoning a freshly opened write transaction; interrupted for suspension."
+ "Deferring the %{public}@ upgrade; another process already holds the database write lock."
+ "Deferring the %{public}@ upgrade; interrupted for suspension."
+ "Failed to check whether tab group %d is claimed by an open window"
+ "Not opening a write transaction; the database was interrupted for suspension."
+ "Rolling back a write transaction interrupted for suspension, reverting %zu bookmark state changes"
+ "SELECT 1 FROM windows WHERE date_closed IS NULL AND (local_tab_group_id = %d OR private_tab_group_id = %d)"
+ "WebBookmarks could not start a bounded-wait immediate transaction. Result code was: %d"
+ "WebBookmarks did not start a deferred transaction; interrupted for suspension. Result code was: %d"
+ "WebBookmarks did not start an immediate transaction; interrupted for suspension. Result code was: %d"
```
