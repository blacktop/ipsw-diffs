## SafariCore

> `/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore`

```diff

-624.2.1.10.1
-  __TEXT.__text: 0x14dce0
+624.2.2.10.1
+  __TEXT.__text: 0x14e2e0
   __TEXT.__auth_stubs: 0x3310
-  __TEXT.__objc_methlist: 0xbf44
+  __TEXT.__objc_methlist: 0xbf6c
   __TEXT.__const: 0x3570
-  __TEXT.__gcc_except_tab: 0x7054
-  __TEXT.__cstring: 0x130b5
+  __TEXT.__gcc_except_tab: 0x709c
+  __TEXT.__cstring: 0x130e5
   __TEXT.__ustring: 0x2826
-  __TEXT.__oslogstring: 0xb073
+  __TEXT.__oslogstring: 0xb163
   __TEXT.__dlopen_cstrs: 0x157
   __TEXT.__swift5_typeref: 0x10d1
   __TEXT.__constg_swiftt: 0xb7c

   __TEXT.__swift_as_ret: 0xf4
   __TEXT.__swift5_capture: 0x70c
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x69f8
+  __TEXT.__unwind_info: 0x6a28
   __TEXT.__eh_frame: 0x3a00
   __TEXT.__objc_classname: 0x1de5
-  __TEXT.__objc_methname: 0x260e5
+  __TEXT.__objc_methname: 0x261d5
   __TEXT.__objc_methtype: 0x46aa
-  __TEXT.__objc_stubs: 0x12bc0
+  __TEXT.__objc_stubs: 0x12c20
   __DATA_CONST.__got: 0xea0
-  __DATA_CONST.__const: 0x5230
+  __DATA_CONST.__const: 0x5258
   __DATA_CONST.__objc_classlist: 0x610
   __DATA_CONST.__objc_catlist: 0x160
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6df0
+  __DATA_CONST.__objc_selrefs: 0x6e10
   __DATA_CONST.__objc_protorefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0x4a0
   __DATA_CONST.__objc_arraydata: 0x2a20
   __AUTH_CONST.__auth_got: 0x19a0
   __AUTH_CONST.__const: 0x6c08
-  __AUTH_CONST.__cfstring: 0x19b80
-  __AUTH_CONST.__objc_const: 0x13a88
+  __AUTH_CONST.__cfstring: 0x19ba0
+  __AUTH_CONST.__objc_const: 0x13ac8
   __AUTH_CONST.__objc_intobj: 0x870
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x5a0
   __AUTH.__objc_data: 0x2710
   __AUTH.__data: 0x660
-  __DATA.__objc_ivar: 0xc6c
+  __DATA.__objc_ivar: 0xc74
   __DATA.__data: 0x1a58
   __DATA.__bss: 0x5190
   __DATA.__common: 0x30

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C600C369-642F-33CD-B16C-BB8E60D0D9F5
-  Functions: 8001
-  Symbols:   21371
-  CStrings:  13316
+  UUID: 940B704D-007A-3438-AC4E-C35D77FEE513
+  Functions: 8010
+  Symbols:   21397
+  CStrings:  13327
 
Symbols:
+ -[NSFileManager(SafariNSFileManagerExtras) safari_ensureDirectoryExists:].cold.3
+ -[WBSAnalyticsLogger didVisitWebpageWithPerFormUsageDictionary:webpageLocale:]
+ -[WBSSavedAccountStore _fetchSignInWithAppleAccountsWithCoalescing]
+ -[WBSSavedAccountStore _scheduleSignInWithAppleFetchForDate:]
+ -[WBSSavedAccountStore _scheduleSignInWithAppleFetchForDate:].cold.1
+ GCC_except_table173
+ GCC_except_table284
+ GCC_except_table291
+ GCC_except_table326
+ GCC_except_table333
+ GCC_except_table344
+ GCC_except_table347
+ GCC_except_table348
+ GCC_except_table372
+ GCC_except_table381
+ GCC_except_table387
+ GCC_except_table391
+ GCC_except_table396
+ GCC_except_table397
+ GCC_except_table400
+ GCC_except_table411
+ GCC_except_table414
+ GCC_except_table415
+ GCC_except_table419
+ GCC_except_table422
+ GCC_except_table425
+ GCC_except_table430
+ GCC_except_table436
+ GCC_except_table439
+ GCC_except_table442
+ GCC_except_table445
+ GCC_except_table454
+ GCC_except_table458
+ GCC_except_table459
+ _OBJC_IVAR_$_WBSSavedAccountStore._lastSignInWithAppleFetchTimestamp
+ _OBJC_IVAR_$_WBSSavedAccountStore._signInWithAppleFetchTimer
+ ___112-[WBSSavedAccountStore canSaveUser:password:forProtectionSpace:highLevelDomain:notes:customTitle:groupID:error:]_block_invoke.314
+ ___126-[WBSSavedAccountStore _cleanUpSharedSavedAccountsWithUnknownOriginalContributorParticipantIDsIfNecessaryFromRecentlyDeleted:]_block_invoke.339
+ ___145-[WBSSavedAccountStore _moveSavedAccountsOriginallyContributedByCurrentUserToPersonalKeychainFromGroupIDOnInternalQueue:isForAlreadyExitedGroup:]_block_invoke.369
+ ___145-[WBSSavedAccountStore _moveSavedAccountsOriginallyContributedByCurrentUserToPersonalKeychainFromGroupIDOnInternalQueue:isForAlreadyExitedGroup:]_block_invoke_2.370
+ ___147-[WBSSavedAccountStore _getSavedAccountMatchesFromSavedAccountTreeMatchesOnInternalQueue:withCriteria:mergingAutoFillPasskeys:nearbyDeviceOptions:]_block_invoke.419
+ ___53-[WBSSavedAccountStore _fetchSignInWithAppleAccounts]_block_invoke.237
+ ___53-[WBSSavedAccountStore _fetchSignInWithAppleAccounts]_block_invoke.237.cold.1
+ ___53-[WBSSavedAccountStore _fetchSignInWithAppleAccounts]_block_invoke.238
+ ___61-[WBSSavedAccountStore _scheduleSignInWithAppleFetchForDate:]_block_invoke
+ ___61-[WBSSavedAccountStore _scheduleSignInWithAppleFetchForDate:]_block_invoke_2
+ ___65-[WBSSavedAccountStore _signInWithApplePushNotificationReceived:]_block_invoke
+ ___66-[WBSSavedAccountStore _performCleanupForExitedGroupsIfNecessary:]_block_invoke.377
+ ___66-[WBSSavedAccountStore _performCleanupForExitedGroupsIfNecessary:]_block_invoke.381
+ ___69-[WBSSavedAccountStore _performRecentlyDeletedMaintenanceIfNecessary]_block_invoke.350
+ ___74-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:completionHandler:]_block_invoke.351
+ ___74-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:completionHandler:]_block_invoke.351.cold.1
+ ___74-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:completionHandler:]_block_invoke.355
+ ___74-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:completionHandler:]_block_invoke_2.357
+ ___78-[WBSAnalyticsLogger didVisitWebpageWithPerFormUsageDictionary:webpageLocale:]_block_invoke
+ ___86-[WBSSavedAccountStore _ensureNoRecentlyDeletedSavedAccountsConflictWithSavedAccount:]_block_invoke.390
+ ___86-[WBSSavedAccountStore _moveContributedSavedAccountsBackToPersonalKeychainIfNecessary]_block_invoke.376
+ ___88-[WBSSavedAccountStore _updateCachedSignInWithAppleAccountsOnInternalQueueWithAccounts:]_block_invoke.244
+ ___95-[WBSSavedAccountStore _changeSavedAccountWithRequestOnInternalQueue:performPostUpdateActions:]_block_invoke.280
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSTimer"8ls32l8
+ ___block_literal_global.1010
+ ___block_literal_global.1012
+ ___block_literal_global.1046
+ ___block_literal_global.1112
+ ___block_literal_global.1270
+ ___block_literal_global.1272
+ ___block_literal_global.1277
+ ___block_literal_global.1279
+ ___block_literal_global.1281
+ ___block_literal_global.1283
+ ___block_literal_global.1285
+ ___block_literal_global.1287
+ ___block_literal_global.1289
+ ___block_literal_global.1291
+ ___block_literal_global.1293
+ ___block_literal_global.1295
+ ___block_literal_global.1297
+ ___block_literal_global.1299
+ ___block_literal_global.1363
+ ___block_literal_global.1365
+ ___block_literal_global.1367
+ ___block_literal_global.1369
+ ___block_literal_global.1371
+ ___block_literal_global.1373
+ ___block_literal_global.241
+ ___block_literal_global.257
+ ___block_literal_global.265
+ ___block_literal_global.272
+ ___block_literal_global.305
+ ___block_literal_global.307
+ ___block_literal_global.323
+ ___block_literal_global.329
+ ___block_literal_global.335
+ ___block_literal_global.338
+ ___block_literal_global.359
+ ___block_literal_global.364
+ ___block_literal_global.380
+ ___block_literal_global.428
+ ___block_literal_global.644
+ ___block_literal_global.780
+ ___block_literal_global.785
+ ___block_literal_global.800
+ ___block_literal_global.812
+ ___block_literal_global.821
+ ___block_literal_global.830
+ ___block_literal_global.855
+ ___block_literal_global.885
+ ___block_literal_global.924
+ ___block_literal_global.968
+ _objc_msgSend$_fetchSignInWithAppleAccountsWithCoalescing
+ _objc_msgSend$_scheduleSignInWithAppleFetchForDate:
+ _objc_msgSend$initWithFireDate:interval:repeats:block:
- GCC_except_table123
- GCC_except_table126
- GCC_except_table279
- GCC_except_table286
- GCC_except_table330
- GCC_except_table341
- GCC_except_table346
- GCC_except_table360
- GCC_except_table373
- GCC_except_table382
- GCC_except_table384
- GCC_except_table395
- GCC_except_table398
- GCC_except_table407
- GCC_except_table408
- GCC_except_table413
- GCC_except_table416
- GCC_except_table417
- GCC_except_table421
- GCC_except_table424
- GCC_except_table429
- GCC_except_table434
- GCC_except_table438
- GCC_except_table443
- GCC_except_table447
- GCC_except_table448
- GCC_except_table456
- ___112-[WBSSavedAccountStore canSaveUser:password:forProtectionSpace:highLevelDomain:notes:customTitle:groupID:error:]_block_invoke.311
- ___126-[WBSSavedAccountStore _cleanUpSharedSavedAccountsWithUnknownOriginalContributorParticipantIDsIfNecessaryFromRecentlyDeleted:]_block_invoke.337
- ___145-[WBSSavedAccountStore _moveSavedAccountsOriginallyContributedByCurrentUserToPersonalKeychainFromGroupIDOnInternalQueue:isForAlreadyExitedGroup:]_block_invoke.367
- ___145-[WBSSavedAccountStore _moveSavedAccountsOriginallyContributedByCurrentUserToPersonalKeychainFromGroupIDOnInternalQueue:isForAlreadyExitedGroup:]_block_invoke_2.368
- ___147-[WBSSavedAccountStore _getSavedAccountMatchesFromSavedAccountTreeMatchesOnInternalQueue:withCriteria:mergingAutoFillPasskeys:nearbyDeviceOptions:]_block_invoke.417
- ___53-[WBSSavedAccountStore _fetchSignInWithAppleAccounts]_block_invoke.234
- ___53-[WBSSavedAccountStore _fetchSignInWithAppleAccounts]_block_invoke.234.cold.1
- ___53-[WBSSavedAccountStore _fetchSignInWithAppleAccounts]_block_invoke.235
- ___66-[WBSSavedAccountStore _performCleanupForExitedGroupsIfNecessary:]_block_invoke.375
- ___66-[WBSSavedAccountStore _performCleanupForExitedGroupsIfNecessary:]_block_invoke.379
- ___69-[WBSSavedAccountStore _performRecentlyDeletedMaintenanceIfNecessary]_block_invoke.348
- ___74-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:completionHandler:]_block_invoke.349
- ___74-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:completionHandler:]_block_invoke.349.cold.1
- ___74-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:completionHandler:]_block_invoke.353
- ___74-[WBSSavedAccountStore _moveSavedAccount:toGroupWithID:completionHandler:]_block_invoke_2.355
- ___86-[WBSSavedAccountStore _ensureNoRecentlyDeletedSavedAccountsConflictWithSavedAccount:]_block_invoke.388
- ___86-[WBSSavedAccountStore _moveContributedSavedAccountsBackToPersonalKeychainIfNecessary]_block_invoke.374
- ___88-[WBSSavedAccountStore _updateCachedSignInWithAppleAccountsOnInternalQueueWithAccounts:]_block_invoke.241
- ___95-[WBSSavedAccountStore _changeSavedAccountWithRequestOnInternalQueue:performPostUpdateActions:]_block_invoke.277
- ___block_literal_global.1007
- ___block_literal_global.1009
- ___block_literal_global.1043
- ___block_literal_global.1109
- ___block_literal_global.1267
- ___block_literal_global.1269
- ___block_literal_global.1274
- ___block_literal_global.1276
- ___block_literal_global.1278
- ___block_literal_global.1280
- ___block_literal_global.1282
- ___block_literal_global.1284
- ___block_literal_global.1286
- ___block_literal_global.1288
- ___block_literal_global.1290
- ___block_literal_global.1292
- ___block_literal_global.1294
- ___block_literal_global.1296
- ___block_literal_global.1360
- ___block_literal_global.1362
- ___block_literal_global.1364
- ___block_literal_global.1366
- ___block_literal_global.1368
- ___block_literal_global.1370
- ___block_literal_global.238
- ___block_literal_global.250
- ___block_literal_global.254
- ___block_literal_global.262
- ___block_literal_global.266
- ___block_literal_global.302
- ___block_literal_global.304
- ___block_literal_global.320
- ___block_literal_global.326
- ___block_literal_global.370
- ___block_literal_global.415
- ___block_literal_global.641
- ___block_literal_global.777
- ___block_literal_global.782
- ___block_literal_global.797
- ___block_literal_global.809
- ___block_literal_global.818
- ___block_literal_global.827
- ___block_literal_global.852
- ___block_literal_global.879
- ___block_literal_global.921
- ___block_literal_global.956
CStrings:
+ "Couldn't ensure directory exists: directory URL is nil"
+ "Scheduled Sign in with Apple accounts fetch for %@"
+ "_fetchSignInWithAppleAccountsWithCoalescing"
+ "_lastSignInWithAppleFetchTimestamp"
+ "_scheduleSignInWithAppleFetchForDate should not be called with a nil date, call _fetchSignInWithAppleAccounts directly instead"
+ "_scheduleSignInWithAppleFetchForDate:"
+ "_signInWithAppleFetchTimer"
+ "com.apple.Safari.AutoFill.AutoFillUsageForPageVisit"
+ "didVisitWebpageWithPerFormUsageDictionary:webpageLocale:"
+ "initWithFireDate:interval:repeats:block:"

```
