## SafariCore

> `/System/Library/PrivateFrameworks/SafariCore.framework/SafariCore`

```diff

-625.1.24.10.1
-  __TEXT.__text: 0x1eb4f8
-  __TEXT.__objc_methlist: 0xd0fc
+625.1.29.10.3
+  __TEXT.__text: 0x1ed4d4
+  __TEXT.__objc_methlist: 0xd134
   __TEXT.__const: 0x7aa4
-  __TEXT.__gcc_except_tab: 0x7758
-  __TEXT.__cstring: 0x16d47
+  __TEXT.__gcc_except_tab: 0x77c8
+  __TEXT.__cstring: 0x17047
   __TEXT.__ustring: 0x2784
-  __TEXT.__oslogstring: 0xe261
+  __TEXT.__oslogstring: 0xe371
   __TEXT.__dlopen_cstrs: 0x157
-  __TEXT.__constg_swiftt: 0x21c4
+  __TEXT.__constg_swiftt: 0x21f4
   __TEXT.__swift5_typeref: 0x25c2
-  __TEXT.__swift5_reflstr: 0x14db
-  __TEXT.__swift5_fieldmd: 0x1978
+  __TEXT.__swift5_reflstr: 0x14fb
+  __TEXT.__swift5_fieldmd: 0x1990
   __TEXT.__swift5_builtin: 0x140
   __TEXT.__swift5_assocty: 0x608
   __TEXT.__swift5_proto: 0x4c8

   __TEXT.__swift5_capture: 0x1490
   __TEXT.__swift5_protos: 0x2c
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x9ae0
-  __TEXT.__eh_frame: 0xa3f8
+  __TEXT.__unwind_info: 0x9b60
+  __TEXT.__eh_frame: 0xa430
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5910
+  __DATA_CONST.__const: 0x59b8
   __DATA_CONST.__objc_classlist: 0x6f8
   __DATA_CONST.__objc_catlist: 0x160
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x75d8
+  __DATA_CONST.__objc_selrefs: 0x7608
   __DATA_CONST.__objc_protorefs: 0xf8
   __DATA_CONST.__objc_superrefs: 0x4c0
   __DATA_CONST.__objc_arraydata: 0x2aa0
-  __DATA_CONST.__got: 0x13a8
-  __AUTH_CONST.__const: 0xb018
-  __AUTH_CONST.__cfstring: 0x1ad60
-  __AUTH_CONST.__objc_const: 0x162c0
+  __DATA_CONST.__got: 0x13b0
+  __AUTH_CONST.__const: 0xb048
+  __AUTH_CONST.__cfstring: 0x1af00
+  __AUTH_CONST.__objc_const: 0x16310
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x930
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x5a0
   __AUTH_CONST.__auth_got: 0x21b0
   __AUTH.__objc_data: 0x2220
-  __AUTH.__data: 0xfd0
-  __DATA.__objc_ivar: 0xd2c
-  __DATA.__data: 0x3540
+  __AUTH.__data: 0x1010
+  __DATA.__objc_ivar: 0xd30
+  __DATA.__data: 0x3560
   __DATA.__bss: 0xa420
-  __DATA.__common: 0x78
+  __DATA.__common: 0x88
   __DATA_DIRTY.__objc_data: 0x2980
   __DATA_DIRTY.__data: 0xdc8
   __DATA_DIRTY.__bss: 0x690

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11211
-  Symbols:   14564
-  CStrings:  5241
+  Functions: 11244
+  Symbols:   14587
+  CStrings:  5271
 
Symbols:
+ +[WBSFeatureAvailability _douyinSearchProviderIsAvailble]
+ +[WBSFeatureAvailability isAutomaticPasswordChangeBulkModeEnabled]
+ +[WBSPasswordManagerURL passwordManagerSecurityRecommendationsURLForBreachNotificationForHighPriorityAccount:]
+ -[WBSAnalyticsLogger reportPasswordsActionEvent:isHighPriorityAccount:primaryWarning:passwordChangeMethod:]
+ -[WBSAnalyticsLogger reportPasswordsVolumeEventWithCompromisedPasswordCount:percentOfPasswordsThatAreCompromised:totalPasswordCount:totalPasskeyCount:]
+ -[WBSPasswordWarningManager reportAnalyticsIfNecessary]
+ -[WBSSQLiteStore openAndCheckIntegrity:createIfNeeded:fallBackToMemoryStoreIfError:lockingPolicy:busyTimeout:completionHandler:]
+ -[WBSSavedAccount isEqualForMovingSharedSavedAccountsBackToPersonalKeychainOnGroupExit:withUserNameForAttempt:]
+ GCC_except_table324
+ GCC_except_table330
+ GCC_except_table339
+ GCC_except_table341
+ GCC_except_table346
+ GCC_except_table348
+ GCC_except_table357
+ GCC_except_table360
+ GCC_except_table362
+ GCC_except_table363
+ GCC_except_table385
+ GCC_except_table387
+ GCC_except_table394
+ GCC_except_table396
+ GCC_except_table406
+ GCC_except_table412
+ GCC_except_table415
+ GCC_except_table427
+ GCC_except_table435
+ GCC_except_table438
+ GCC_except_table440
+ GCC_except_table445
+ GCC_except_table452
+ GCC_except_table454
+ GCC_except_table455
+ GCC_except_table457
+ GCC_except_table464
+ GCC_except_table476
+ GCC_except_table482
+ GCC_except_table501
+ GCC_except_table503
+ _OBJC_IVAR_$_WBSSQLiteStore._databaseBusyTimeout
+ _WBSAutomaticPasswordChangeDeveloperModeEnabledKey
+ _WBSPasswordManagerURLContainsHighPriorityAccountKey
+ _WBSPasswordManagerURLIsForBreachNotificationKey
+ _WBSPasswordsAppPasswordsVolumeAnalyticsEventLastReportedDateKey
+ _WBSTabClusteringPolicyKey
+ ___107-[WBSAnalyticsLogger reportPasswordsActionEvent:isHighPriorityAccount:primaryWarning:passwordChangeMethod:]_block_invoke
+ ___128-[WBSSQLiteStore openAndCheckIntegrity:createIfNeeded:fallBackToMemoryStoreIfError:lockingPolicy:busyTimeout:completionHandler:]_block_invoke
+ ___128-[WBSSQLiteStore openAndCheckIntegrity:createIfNeeded:fallBackToMemoryStoreIfError:lockingPolicy:busyTimeout:completionHandler:]_block_invoke_2
+ ___151-[WBSAnalyticsLogger reportPasswordsVolumeEventWithCompromisedPasswordCount:percentOfPasswordsThatAreCompromised:totalPasswordCount:totalPasskeyCount:]_block_invoke
+ ___66+[WBSFeatureAvailability isAutomaticPasswordChangeBulkModeEnabled]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e25_B16?0"WBSSavedAccount"8ls32l8s40l8
+ ___block_descriptor_49_e8_32s40s_e49_"NSString"16?0"WBSSavedAccountAdditionalSite"8ls32l8s40l8
+ ___block_descriptor_57_e19_"NSDictionary"8?0l
+ ___block_descriptor_60_e19_"NSDictionary"8?0l
+ ___block_descriptor_67_ea8_32s40bs_e5_v8?0ls32l8s40l8
+ _isAutomaticPasswordChangeBulkModeEnabled.isEnabled
+ _isAutomaticPasswordChangeBulkModeEnabled.onceToken
+ _keypath_getTm
+ _objc_msgSend$_douyinSearchProviderIsAvailble
+ _objc_msgSend$isAutomaticPasswordChangeBulkModeEnabled
+ _objc_msgSend$isEqualForMovingSharedSavedAccountsBackToPersonalKeychainOnGroupExit:withUserNameForAttempt:
+ _objc_msgSend$openAndCheckIntegrity:createIfNeeded:fallBackToMemoryStoreIfError:lockingPolicy:busyTimeout:completionHandler:
+ _objc_msgSend$reportPasswordsVolumeEventWithCompromisedPasswordCount:percentOfPasswordsThatAreCompromised:totalPasswordCount:totalPasskeyCount:
+ _objc_msgSend$setBusyTimeout:
+ _objc_msgSend$sleepForTimeInterval:
- +[WBSFeatureAvailability isRecentSearchesInStartPageEnabled]
- +[WBSPasswordManagerURL passwordManagerSecurityRecommendationsURL]
- -[WBSSavedAccount isEqualForMovingSharedSavedAccountsBackToPersonalKeychainOnGroupExit:]
- GCC_except_table327
- GCC_except_table328
- GCC_except_table333
- GCC_except_table334
- GCC_except_table345
- GCC_except_table354
- GCC_except_table356
- GCC_except_table373
- GCC_except_table375
- GCC_except_table386
- GCC_except_table388
- GCC_except_table402
- GCC_except_table407
- GCC_except_table408
- GCC_except_table420
- GCC_except_table421
- GCC_except_table422
- GCC_except_table423
- GCC_except_table431
- GCC_except_table436
- GCC_except_table439
- GCC_except_table442
- GCC_except_table444
- GCC_except_table447
- GCC_except_table453
- GCC_except_table456
- GCC_except_table463
- GCC_except_table465
- GCC_except_table466
- GCC_except_table468
- _WBSAutoTabClusteringEnabledKey
- ___116-[WBSSQLiteStore openAndCheckIntegrity:createIfNeeded:fallBackToMemoryStoreIfError:lockingPolicy:completionHandler:]_block_invoke
- ___116-[WBSSQLiteStore openAndCheckIntegrity:createIfNeeded:fallBackToMemoryStoreIfError:lockingPolicy:completionHandler:]_block_invoke_2
- ___60+[WBSFeatureAvailability isRecentSearchesInStartPageEnabled]_block_invoke
- ___block_descriptor_40_e8_32s_e49_"NSString"16?0"WBSSavedAccountAdditionalSite"8ls32l8
- ___block_descriptor_59_ea8_32s40bs_e5_v8?0ls32l8s40l8
- _isRecentSearchesInStartPageEnabled.isRecentSearchesInStartPageEnabled
- _isRecentSearchesInStartPageEnabled.onceToken
- _objc_msgSend$isEqualForMovingSharedSavedAccountsBackToPersonalKeychainOnGroupExit:
CStrings:
+ "AutomaticPasswordChangeDeveloperModeEnabled"
+ "DidNotFillOneTimeCodeInEntirety"
+ "DidNotReceiveMailOneTimeCode"
+ "DidNotReceiveOneTimeCode"
+ "DidNotReceiveTOTPOneTimeCode"
+ "DidNotReceiveTextMessageOneTimeCode"
+ "DidNotReceiveThirdPartyOneTimeCode"
+ "Failed to begin immediate transaction (busy); retrying: %s"
+ "FinishedWithoutFillingLoginCredentials"
+ "HighPriorityAccount"
+ "InvalidOneTimeCode"
+ "Not reporting invalid compromised password count."
+ "PBANotification"
+ "Refusing to delete session %{public}s written by newer software."
+ "Refusing to update session %{public}s written by newer software."
+ "SignificantChange"
+ "TabClusteringPolicy"
+ "Unable to Fix (Status Text)"
+ "Unable to fix (Status Text)"
+ "WBSPasswordsAppPasswordsVolumeAnalyticsEventLastReportedDateKey"
+ "apc_bulk"
+ "com.apple.Passwords.EngagementActions"
+ "com.apple.Passwords.Volume"
+ "high_priority"
+ "num_compromised_passwords"
+ "password_action"
+ "password_flag"
+ "percent_compromised_passwords"
+ "skippedAccountUUIDs"
+ "total_num_passkeys"
+ "total_num_passwords"
+ "update_method"
- "AutoTabClusteringEnabled"
- "EnableRecentSearchesInStartPage"
```
