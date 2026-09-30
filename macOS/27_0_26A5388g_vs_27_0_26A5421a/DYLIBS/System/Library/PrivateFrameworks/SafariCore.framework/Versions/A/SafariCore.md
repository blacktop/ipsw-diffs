## SafariCore

> `/System/Library/PrivateFrameworks/SafariCore.framework/Versions/A/SafariCore`

```diff

-625.1.24.11.2
-  __TEXT.__text: 0x200d24
-  __TEXT.__objc_methlist: 0xd434
-  __TEXT.__const: 0x7a94
-  __TEXT.__gcc_except_tab: 0x7d5c
-  __TEXT.__cstring: 0x17427
+625.1.29.11.25
+  __TEXT.__text: 0x203768
+  __TEXT.__objc_methlist: 0xd51c
+  __TEXT.__const: 0x7c14
+  __TEXT.__gcc_except_tab: 0x7dcc
+  __TEXT.__cstring: 0x17737
   __TEXT.__ustring: 0x2784
-  __TEXT.__oslogstring: 0xe631
+  __TEXT.__oslogstring: 0xe741
   __TEXT.__dlopen_cstrs: 0x157
-  __TEXT.__constg_swiftt: 0x21c4
-  __TEXT.__swift5_typeref: 0x25c2
-  __TEXT.__swift5_reflstr: 0x14db
-  __TEXT.__swift5_fieldmd: 0x196c
-  __TEXT.__swift5_builtin: 0x140
-  __TEXT.__swift5_assocty: 0x608
-  __TEXT.__swift5_proto: 0x4c8
-  __TEXT.__swift5_types: 0x210
+  __TEXT.__constg_swiftt: 0x2214
+  __TEXT.__swift5_typeref: 0x2612
+  __TEXT.__swift5_reflstr: 0x14fb
+  __TEXT.__swift5_fieldmd: 0x19a0
+  __TEXT.__swift5_builtin: 0x154
+  __TEXT.__swift5_assocty: 0x638
+  __TEXT.__swift5_proto: 0x4e0
+  __TEXT.__swift5_types: 0x214
   __TEXT.__swift5_types2: 0x4
   __TEXT.__swift_as_entry: 0x328
   __TEXT.__swift_as_ret: 0x370
   __TEXT.__swift_as_cont: 0x6f0
-  __TEXT.__swift5_capture: 0x142c
+  __TEXT.__swift5_capture: 0x145c
   __TEXT.__swift5_protos: 0x2c
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x9b48
-  __TEXT.__eh_frame: 0xa2a8
+  __TEXT.__unwind_info: 0x9bb8
+  __TEXT.__eh_frame: 0xa2e0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2808
-  __DATA_CONST.__objc_classlist: 0x708
+  __DATA_CONST.__const: 0x2888
+  __DATA_CONST.__objc_classlist: 0x710
   __DATA_CONST.__objc_catlist: 0x160
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7770
+  __DATA_CONST.__objc_selrefs: 0x77f8
   __DATA_CONST.__objc_protorefs: 0xf8
   __DATA_CONST.__objc_superrefs: 0x4c8
   __DATA_CONST.__objc_arraydata: 0x2a98
-  __DATA_CONST.__got: 0x13c0
-  __AUTH_CONST.__const: 0xe748
-  __AUTH_CONST.__cfstring: 0x1b420
-  __AUTH_CONST.__objc_const: 0x16570
+  __DATA_CONST.__got: 0x13d0
+  __AUTH_CONST.__const: 0xe8c0
+  __AUTH_CONST.__cfstring: 0x1b5c0
+  __AUTH_CONST.__objc_const: 0x166e8
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x930
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x588
   __AUTH_CONST.__auth_got: 0x20b8
-  __AUTH.__objc_data: 0x21a0
-  __AUTH.__data: 0xfd8
-  __DATA.__objc_ivar: 0xd2c
-  __DATA.__data: 0x3480
-  __DATA.__bss: 0x9ca0
-  __DATA.__common: 0x78
+  __AUTH.__objc_data: 0x2210
+  __AUTH.__data: 0x1038
+  __DATA.__objc_ivar: 0xd30
+  __DATA.__data: 0x34e0
+  __DATA.__bss: 0x9fa0
+  __DATA.__common: 0x88
   __DATA_DIRTY.__objc_data: 0x2ac0
   __DATA_DIRTY.__data: 0xed8
   __DATA_DIRTY.__bss: 0xe10

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11388
-  Symbols:   15085
-  CStrings:  5317
+  Functions: 11454
+  Symbols:   15131
+  CStrings:  5347
 
Symbols:
+ +[WBSFeatureAvailability _douyinSearchProviderIsAvailble]
+ +[WBSFeatureAvailability isAutomaticPasswordChangeBulkModeEnabled]
+ +[WBSPasswordManagerURL passwordManagerSecurityRecommendationsURLForBreachNotificationForHighPriorityAccount:]
+ -[WBSAnalyticsLogger reportPasswordsActionEvent:isHighPriorityAccount:primaryWarning:passwordChangeMethod:]
+ -[WBSAnalyticsLogger reportPasswordsVolumeEventWithCompromisedPasswordCount:percentOfPasswordsThatAreCompromised:totalPasswordCount:totalPasskeyCount:]
+ -[WBSPasswordWarningManager reportAnalyticsIfNecessary]
+ -[WBSSQLiteStore openAndCheckIntegrity:createIfNeeded:fallBackToMemoryStoreIfError:lockingPolicy:busyTimeout:completionHandler:]
+ -[WBSSavedAccount isEqualForMovingSharedSavedAccountsBackToPersonalKeychainOnGroupExit:withUserNameForAttempt:]
+ GCC_except_table337
+ GCC_except_table343
+ GCC_except_table352
+ GCC_except_table354
+ GCC_except_table359
+ GCC_except_table361
+ GCC_except_table370
+ GCC_except_table373
+ GCC_except_table375
+ GCC_except_table376
+ GCC_except_table398
+ GCC_except_table400
+ GCC_except_table409
+ GCC_except_table410
+ GCC_except_table411
+ GCC_except_table419
+ GCC_except_table425
+ GCC_except_table427
+ GCC_except_table435
+ GCC_except_table447
+ GCC_except_table453
+ GCC_except_table456
+ GCC_except_table468
+ GCC_except_table476
+ GCC_except_table479
+ GCC_except_table481
+ GCC_except_table484
+ GCC_except_table486
+ GCC_except_table493
+ GCC_except_table495
+ GCC_except_table496
+ GCC_except_table498
+ GCC_except_table513
+ GCC_except_table519
+ GCC_except_table538
+ GCC_except_table540
+ OBJC_IVAR_$_WBSSQLiteStore._databaseBusyTimeout
+ _OBJC_CLASS_$_WBSRunLoopCoalescedUpdate
+ _OBJC_METACLASS_$_WBSRunLoopCoalescedUpdate
+ _WBSAutomaticPasswordChangeDeveloperModeEnabledKey
+ _WBSPasswordManagerURLContainsHighPriorityAccountKey
+ _WBSPasswordManagerURLIsForBreachNotificationKey
+ _WBSPasswordsAppPasswordsVolumeAnalyticsEventLastReportedDateKey
+ _WBSTabClusteringPolicyKey
+ __DATA_WBSRunLoopCoalescedUpdate
+ __INSTANCE_METHODS_WBSRunLoopCoalescedUpdate
+ __IVARS_WBSRunLoopCoalescedUpdate
+ __METACLASS_DATA_WBSRunLoopCoalescedUpdate
+ __PROPERTIES_WBSRunLoopCoalescedUpdate
+ ___107-[WBSAnalyticsLogger reportPasswordsActionEvent:isHighPriorityAccount:primaryWarning:passwordChangeMethod:]_block_invoke
+ ___128-[WBSSQLiteStore openAndCheckIntegrity:createIfNeeded:fallBackToMemoryStoreIfError:lockingPolicy:busyTimeout:completionHandler:]_block_invoke
+ ___128-[WBSSQLiteStore openAndCheckIntegrity:createIfNeeded:fallBackToMemoryStoreIfError:lockingPolicy:busyTimeout:completionHandler:]_block_invoke_2
+ ___151-[WBSAnalyticsLogger reportPasswordsVolumeEventWithCompromisedPasswordCount:percentOfPasswordsThatAreCompromised:totalPasswordCount:totalPasskeyCount:]_block_invoke
+ ___66+[WBSFeatureAvailability isAutomaticPasswordChangeBulkModeEnabled]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e25_B16?0"WBSSavedAccount"8l
+ ___block_descriptor_49_e8_32s40s_e49_"NSString"16?0"WBSSavedAccountAdditionalSite"8l
+ ___block_descriptor_57_e19_"NSDictionary"8?0l
+ ___block_descriptor_60_e19_"NSDictionary"8?0l
+ ___block_descriptor_67_ea8_32s40bs_e5_v8?0l
+ _associated conformance So13NSRunLoopModeaSHSCSQ
+ _associated conformance So13NSRunLoopModeas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So13NSRunLoopModeas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _keypath_getTm
+ _objc_msgSend$_douyinSearchProviderIsAvailble
+ _objc_msgSend$block
+ _objc_msgSend$hasScheduledRun
+ _objc_msgSend$initWithRunLoop:modes:block:
+ _objc_msgSend$isAutomaticPasswordChangeBulkModeEnabled
+ _objc_msgSend$isEqualForMovingSharedSavedAccountsBackToPersonalKeychainOnGroupExit:withUserNameForAttempt:
+ _objc_msgSend$modes
+ _objc_msgSend$openAndCheckIntegrity:createIfNeeded:fallBackToMemoryStoreIfError:lockingPolicy:busyTimeout:completionHandler:
+ _objc_msgSend$performIfScheduled
+ _objc_msgSend$performInModes:block:
+ _objc_msgSend$reportPasswordsVolumeEventWithCompromisedPasswordCount:percentOfPasswordsThatAreCompromised:totalPasswordCount:totalPasskeyCount:
+ _objc_msgSend$runLoop
+ _objc_msgSend$setBusyTimeout:
+ _objc_msgSend$setHasScheduledRun:
+ _objc_msgSend$sleepForTimeInterval:
+ _symbolic So25WBSRunLoopCoalescedUpdateCSgXw
+ _symbolic _____ So13NSRunLoopModea
+ _symbolic _____y_____G s23_ContiguousArrayStorageC So13NSRunLoopModea
+ isAutomaticPasswordChangeBulkModeEnabled.isEnabled
+ isAutomaticPasswordChangeBulkModeEnabled.onceToken
- +[WBSFeatureAvailability isRecentSearchesInStartPageEnabled]
- +[WBSPasswordManagerURL passwordManagerSecurityRecommendationsURL]
- -[WBSSavedAccount isEqualForMovingSharedSavedAccountsBackToPersonalKeychainOnGroupExit:]
- GCC_except_table341
- GCC_except_table346
- GCC_except_table347
- GCC_except_table356
- GCC_except_table358
- GCC_except_table367
- GCC_except_table369
- GCC_except_table386
- GCC_except_table388
- GCC_except_table399
- GCC_except_table401
- GCC_except_table406
- GCC_except_table413
- GCC_except_table415
- GCC_except_table423
- GCC_except_table431
- GCC_except_table443
- GCC_except_table448
- GCC_except_table449
- GCC_except_table461
- GCC_except_table462
- GCC_except_table463
- GCC_except_table464
- GCC_except_table472
- GCC_except_table477
- GCC_except_table480
- GCC_except_table483
- GCC_except_table488
- GCC_except_table494
- GCC_except_table497
- GCC_except_table504
- GCC_except_table506
- GCC_except_table507
- _WBSAutoTabClusteringEnabledKey
- ___116-[WBSSQLiteStore openAndCheckIntegrity:createIfNeeded:fallBackToMemoryStoreIfError:lockingPolicy:completionHandler:]_block_invoke
- ___116-[WBSSQLiteStore openAndCheckIntegrity:createIfNeeded:fallBackToMemoryStoreIfError:lockingPolicy:completionHandler:]_block_invoke_2
- ___60+[WBSFeatureAvailability isRecentSearchesInStartPageEnabled]_block_invoke
- ___block_descriptor_40_e8_32s_e49_"NSString"16?0"WBSSavedAccountAdditionalSite"8l
- ___block_descriptor_59_ea8_32s40bs_e5_v8?0l
- _objc_msgSend$isEqualForMovingSharedSavedAccountsBackToPersonalKeychainOnGroupExit:
- isRecentSearchesInStartPageEnabled.isRecentSearchesInStartPageEnabled
- isRecentSearchesInStartPageEnabled.onceToken
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
+ "SafariCore.WBSRunLoopCoalescedUpdate"
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
