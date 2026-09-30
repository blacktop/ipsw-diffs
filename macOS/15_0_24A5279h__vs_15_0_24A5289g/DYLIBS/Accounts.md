## Accounts

> `/System/Library/Frameworks/Accounts.framework/Versions/A/Accounts`

```diff

-984.0.0.0.0
-  __TEXT.__text: 0x5f55c
+985.0.0.0.0
+  __TEXT.__text: 0x5efd4
   __TEXT.__auth_stubs: 0xb40
-  __TEXT.__objc_methlist: 0x395c
+  __TEXT.__objc_methlist: 0x3964
   __TEXT.__const: 0x190
-  __TEXT.__gcc_except_tab: 0x3f00
-  __TEXT.__cstring: 0x3ab3
-  __TEXT.__oslogstring: 0x53eb
-  __TEXT.__unwind_info: 0x1920
+  __TEXT.__gcc_except_tab: 0x3e7c
+  __TEXT.__cstring: 0x3ae6
+  __TEXT.__oslogstring: 0x5366
+  __TEXT.__unwind_info: 0x1910
   __TEXT.__objc_classname: 0x549
-  __TEXT.__objc_methname: 0x80ef
-  __TEXT.__objc_methtype: 0x155c
+  __TEXT.__objc_methname: 0x80c6
+  __TEXT.__objc_methtype: 0x1529
   __TEXT.__objc_stubs: 0x5ca0
   __DATA_CONST.__got: 0x380
   __DATA_CONST.__const: 0xee0

   __AUTH_CONST.__auth_got: 0x5b0
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x1b00
-  __AUTH_CONST.__cfstring: 0x4740
-  __AUTH_CONST.__objc_const: 0x6440
+  __AUTH_CONST.__cfstring: 0x4760
+  __AUTH_CONST.__objc_const: 0x6420
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0xfa0
   __DATA.__objc_ivar: 0x380
   __DATA.__data: 0x4d8
-  __DATA.__bss: 0x1a8
+  __DATA.__bss: 0x1b0
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /System/Library/PrivateFrameworks/UserManagement.framework/Versions/A/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1851
-  Symbols:   4471
-  CStrings:  635
+  Functions: 1849
+  Symbols:   4469
+  CStrings:  636
 
Symbols:
+ +[ACNotifyAccountCache __enableTestCacheID]
+ GCC_except_table195
+ GCC_except_table201
+ GCC_except_table204
+ GCC_except_table207
+ GCC_except_table212
+ GCC_except_table216
+ GCC_except_table219
+ GCC_except_table222
+ GCC_except_table228
+ GCC_except_table234
+ GCC_except_table244
+ GCC_except_table250
+ GCC_except_table257
+ GCC_except_table262
+ GCC_except_table266
+ GCC_except_table271
+ GCC_except_table274
+ GCC_except_table277
+ GCC_except_table283
+ GCC_except_table287
+ GCC_except_table292
+ GCC_except_table297
+ GCC_except_table304
+ GCC_except_table309
+ GCC_except_table313
+ GCC_except_table316
+ GCC_except_table319
+ GCC_except_table322
+ GCC_except_table325
+ GCC_except_table328
+ GCC_except_table335
+ GCC_except_table340
+ GCC_except_table345
+ GCC_except_table349
+ GCC_except_table352
+ GCC_except_table355
+ GCC_except_table360
+ GCC_except_table364
+ GCC_except_table368
+ GCC_except_table374
+ GCC_except_table379
+ GCC_except_table386
+ GCC_except_table392
+ GCC_except_table396
+ GCC_except_table403
+ GCC_except_table410
+ GCC_except_table416
+ GCC_except_table422
+ GCC_except_table432
+ GCC_except_table436
+ GCC_except_table442
+ GCC_except_table447
+ GCC_except_table453
+ GCC_except_table457
+ GCC_except_table6
+ __59-[ACAccountStore clearAllPermissionsGrantedForAccountType:]_block_invoke.236
+ __65-[ACAccountStore setPermissionGranted:forBundleID:onAccountType:]_block_invoke.231
+ __69-[ACAccountStore requestAccessToAccountsWithType:options:completion:]_block_invoke.219
+ __69-[ACAccountStore requestAccessToAccountsWithType:options:completion:]_block_invoke_2.220
+ ___testCachePrefix
+ __block_literal_global.209
+ _objc_msgSend$accountsWithAccountTypeIdentifierExist:
- -[ACAccountStore updateExistenceCacheOfAccountWithTypeIdentifier:].cold.1
- GCC_except_table191
- GCC_except_table197
- GCC_except_table203
- GCC_except_table206
- GCC_except_table209
- GCC_except_table214
- GCC_except_table218
- GCC_except_table221
- GCC_except_table224
- GCC_except_table230
- GCC_except_table236
- GCC_except_table246
- GCC_except_table252
- GCC_except_table259
- GCC_except_table264
- GCC_except_table268
- GCC_except_table273
- GCC_except_table276
- GCC_except_table279
- GCC_except_table285
- GCC_except_table289
- GCC_except_table294
- GCC_except_table299
- GCC_except_table306
- GCC_except_table311
- GCC_except_table315
- GCC_except_table318
- GCC_except_table321
- GCC_except_table324
- GCC_except_table327
- GCC_except_table330
- GCC_except_table337
- GCC_except_table342
- GCC_except_table347
- GCC_except_table351
- GCC_except_table354
- GCC_except_table357
- GCC_except_table362
- GCC_except_table366
- GCC_except_table370
- GCC_except_table376
- GCC_except_table381
- GCC_except_table388
- GCC_except_table394
- GCC_except_table398
- GCC_except_table405
- GCC_except_table412
- GCC_except_table418
- GCC_except_table424
- GCC_except_table434
- GCC_except_table438
- GCC_except_table444
- GCC_except_table449
- GCC_except_table455
- GCC_except_table459
- GCC_except_table9
- __59-[ACAccountStore clearAllPermissionsGrantedForAccountType:]_block_invoke.238
- __65-[ACAccountStore setPermissionGranted:forBundleID:onAccountType:]_block_invoke.233
- __69-[ACAccountStore requestAccessToAccountsWithType:options:completion:]_block_invoke.221
- __69-[ACAccountStore requestAccessToAccountsWithType:options:completion:]_block_invoke_2.222
- ___66-[ACAccountStore updateExistenceCacheOfAccountWithTypeIdentifier:]_block_invoke
- ___66-[ACAccountStore updateExistenceCacheOfAccountWithTypeIdentifier:]_block_invoke_2
- __block_literal_global.211
- _objc_msgSend$updateExistenceCacheOfAccountWithTypeIdentifier:withHandler:
CStrings:
+ "com.apple.accounts.notify-generation.unit-tests.%!@(MISSING)"

```
