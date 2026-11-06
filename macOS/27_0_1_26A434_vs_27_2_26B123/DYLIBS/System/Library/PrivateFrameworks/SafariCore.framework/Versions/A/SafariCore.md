## SafariCore

> `/System/Library/PrivateFrameworks/SafariCore.framework/Versions/A/SafariCore`

```diff

-625.1.29.11.28
-  __TEXT.__text: 0x203b3c
-  __TEXT.__objc_methlist: 0xd514
-  __TEXT.__const: 0x7c14
-  __TEXT.__gcc_except_tab: 0x7dcc
-  __TEXT.__cstring: 0x17737
+625.2.8.11.9
+  __TEXT.__text: 0x20be9c
+  __TEXT.__objc_methlist: 0xd694
+  __TEXT.__const: 0x7d64
+  __TEXT.__gcc_except_tab: 0x7f38
+  __TEXT.__cstring: 0x17897
   __TEXT.__ustring: 0x2784
-  __TEXT.__oslogstring: 0xe741
+  __TEXT.__oslogstring: 0xea91
   __TEXT.__dlopen_cstrs: 0x157
-  __TEXT.__constg_swiftt: 0x2214
-  __TEXT.__swift5_typeref: 0x2612
-  __TEXT.__swift5_reflstr: 0x14fb
-  __TEXT.__swift5_fieldmd: 0x19a0
-  __TEXT.__swift5_builtin: 0x154
+  __TEXT.__constg_swiftt: 0x2380
+  __TEXT.__swift5_typeref: 0x2706
+  __TEXT.__swift5_reflstr: 0x156b
+  __TEXT.__swift5_fieldmd: 0x1a24
+  __TEXT.__swift5_builtin: 0x17c
   __TEXT.__swift5_assocty: 0x638
   __TEXT.__swift5_proto: 0x4e0
-  __TEXT.__swift5_types: 0x214
+  __TEXT.__swift5_types: 0x224
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__swift_as_entry: 0x328
-  __TEXT.__swift_as_ret: 0x370
+  __TEXT.__swift_as_entry: 0x324
+  __TEXT.__swift_as_ret: 0x36c
   __TEXT.__swift_as_cont: 0x6f0
-  __TEXT.__swift5_capture: 0x145c
-  __TEXT.__swift5_protos: 0x2c
+  __TEXT.__swift5_capture: 0x14e8
+  __TEXT.__swift5_protos: 0x30
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x9bc0
-  __TEXT.__eh_frame: 0xa2e0
+  __TEXT.__unwind_info: 0x9d88
+  __TEXT.__eh_frame: 0xa310
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2888
-  __DATA_CONST.__objc_classlist: 0x710
+  __DATA_CONST.__const: 0x28e0
+  __DATA_CONST.__objc_classlist: 0x718
   __DATA_CONST.__objc_catlist: 0x160
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x77f8
+  __DATA_CONST.__objc_selrefs: 0x78b8
   __DATA_CONST.__objc_protorefs: 0xf8
   __DATA_CONST.__objc_superrefs: 0x4c8
   __DATA_CONST.__objc_arraydata: 0x2a98
-  __DATA_CONST.__got: 0x13d0
-  __AUTH_CONST.__const: 0xe8c0
-  __AUTH_CONST.__cfstring: 0x1b5c0
-  __AUTH_CONST.__objc_const: 0x166e0
+  __DATA_CONST.__got: 0x13e0
+  __AUTH_CONST.__const: 0xed18
+  __AUTH_CONST.__cfstring: 0x1b640
+  __AUTH_CONST.__objc_const: 0x168a0
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x930
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x588
   __AUTH_CONST.__auth_got: 0x20c0
-  __AUTH_CONST.__auth_ptr: 0x9d0
-  __AUTH.__objc_data: 0x2210
-  __AUTH.__data: 0x1038
-  __DATA.__objc_ivar: 0xd30
-  __DATA.__data: 0x34e0
-  __DATA.__bss: 0x9fa0
-  __DATA.__common: 0x88
-  __DATA_DIRTY.__objc_data: 0x2ac0
-  __DATA_DIRTY.__data: 0xed8
+  __AUTH_CONST.__auth_ptr: 0x9d8
+  __AUTH.__objc_data: 0x808
+  __AUTH.__data: 0x2f0
+  __DATA.__objc_ivar: 0xd34
+  __DATA.__data: 0x35c0
+  __DATA.__bss: 0x9fb0
+  __DATA.__common: 0xa8
+  __DATA_DIRTY.__objc_data: 0x45e0
+  __DATA_DIRTY.__data: 0x1c78
   __DATA_DIRTY.__bss: 0xe10
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11456
-  Symbols:   15128
-  CStrings:  5347
+  Functions: 11601
+  Symbols:   15242
+  CStrings:  5365
 
Symbols:
+ +[NSURLSessionConfiguration(SafariCoreExtras) safari_persistentStateSessionConfiguration]
+ +[WBSFeatureAvailability automaticPasswordChangeShouldAlwaysRecommend]
+ +[WBSFeatureAvailability isAutomaticPasswordChangeTestFestModeEnabled]
+ +[WBSFeatureAvailability isNotifyMeWhenJitterEnabled]
+ +[WBSFeatureAvailability setAutomaticPasswordChangeTestFestModeEnabled:]
+ +[WBSSavedAccount isDebugAccountForAutomaticPasswordChangeForDomain:]
+ +[WBSSavedAccount isUUIDHighLevelDomain:]
+ -[NSURLProtectionSpace(SafariCoreExtras) safari_getAllowsCredentialSavingWithCompletionHandler:]
+ -[WBSAnalyticsLogger didDetectSearchEngineBannerWithLinkToApp:wasUserLoggedIn:pageLoadSource:]
+ -[WBSFileVaultRecoveryKeyListenerProxy _synchronousRemoteObjectProxyWithErrorHandler:]
+ -[WBSFileVaultRecoveryKeyListenerProxy deleteRecoveryKeyForVolumeID:serialNumber:error:]
+ -[WBSFileVaultRecoveryKeyListenerProxy recoveryKeyForVolumeID:serialNumber:error:]
+ -[WBSFileVaultRecoveryKeyListenerProxy recoveryKeysForSerialNumber:error:]
+ -[WBSFileVaultRecoveryKeyListenerProxy saveRecoveryKeyWithRequest:error:]
+ -[WBSPasswordWarningManager _getAllWarningsOnWorkQueueForcingUpdate:]
+ -[WBSPasswordWarningTopFraudTargets emailProviderFraudTargets]
+ -[WBSPasswordWarningTopFraudTargets initWithHighPriorityTargets:targets:financialTargets:emailProviderFraudTargets:]
+ -[WBSSavedAccount _adoptSidecarDataFromSavedAccount:]
+ -[WBSSavedAccountStore _logSavedAccountsWithTOTPGeneratorsOnlyInPasskeySidecars:]
+ -[WBSSavedAccountStore _savedAccountConflictingWithSavedAccountOnInternalQueue:afterUpdatingUsername:password:]
+ -[WBSSavedAccountStore canSaveUser:password:forProtectionSpace:highLevelDomain:notes:customTitle:groupID:completionHandler:]
+ -[WBSSavedAccountStore canSaveUser:password:forUserTypedSite:notes:customTitle:groupID:completionHandler:]
+ -[WBSSavedAccountTreeMatch pruneFileVaultRecoveryKeyTrees]
+ GCC_except_table109
+ GCC_except_table123
+ GCC_except_table129
+ GCC_except_table132
+ GCC_except_table139
+ GCC_except_table142
+ GCC_except_table144
+ GCC_except_table147
+ GCC_except_table149
+ GCC_except_table151
+ GCC_except_table153
+ GCC_except_table155
+ GCC_except_table161
+ GCC_except_table163
+ GCC_except_table165
+ GCC_except_table167
+ GCC_except_table169
+ GCC_except_table171
+ GCC_except_table173
+ GCC_except_table175
+ GCC_except_table177
+ GCC_except_table183
+ GCC_except_table185
+ GCC_except_table187
+ GCC_except_table189
+ GCC_except_table191
+ GCC_except_table197
+ GCC_except_table199
+ GCC_except_table201
+ GCC_except_table205
+ GCC_except_table207
+ GCC_except_table209
+ GCC_except_table211
+ GCC_except_table213
+ GCC_except_table215
+ GCC_except_table217
+ GCC_except_table221
+ GCC_except_table223
+ GCC_except_table229
+ GCC_except_table230
+ GCC_except_table233
+ GCC_except_table235
+ GCC_except_table237
+ GCC_except_table239
+ GCC_except_table242
+ GCC_except_table244
+ GCC_except_table247
+ GCC_except_table250
+ GCC_except_table252
+ GCC_except_table255
+ GCC_except_table257
+ GCC_except_table260
+ GCC_except_table264
+ GCC_except_table269
+ GCC_except_table271
+ GCC_except_table273
+ GCC_except_table274
+ GCC_except_table278
+ GCC_except_table283
+ GCC_except_table288
+ GCC_except_table291
+ GCC_except_table293
+ GCC_except_table295
+ GCC_except_table298
+ GCC_except_table301
+ GCC_except_table304
+ GCC_except_table310
+ GCC_except_table334
+ GCC_except_table336
+ GCC_except_table338
+ GCC_except_table346
+ GCC_except_table356
+ GCC_except_table358
+ GCC_except_table363
+ GCC_except_table365
+ GCC_except_table367
+ GCC_except_table369
+ GCC_except_table374
+ GCC_except_table377
+ GCC_except_table391
+ GCC_except_table393
+ GCC_except_table395
+ GCC_except_table397
+ GCC_except_table399
+ GCC_except_table401
+ GCC_except_table404
+ GCC_except_table406
+ GCC_except_table408
+ GCC_except_table412
+ GCC_except_table418
+ GCC_except_table420
+ GCC_except_table422
+ GCC_except_table426
+ GCC_except_table428
+ GCC_except_table436
+ GCC_except_table448
+ GCC_except_table457
+ GCC_except_table464
+ GCC_except_table469
+ GCC_except_table472
+ GCC_except_table477
+ GCC_except_table480
+ GCC_except_table483
+ GCC_except_table488
+ GCC_except_table494
+ GCC_except_table497
+ GCC_except_table499
+ GCC_except_table502
+ GCC_except_table506
+ GCC_except_table517
+ GCC_except_table521
+ GCC_except_table523
+ GCC_except_table525
+ GCC_except_table527
+ GCC_except_table529
+ GCC_except_table531
+ GCC_except_table533
+ GCC_except_table535
+ GCC_except_table537
+ GCC_except_table539
+ GCC_except_table541
+ GCC_except_table78
+ GCC_except_table90
+ OBJC_IVAR_$_WBSPasswordWarningTopFraudTargets._emailProviderFraudTargets
+ WBSOSLogSearchFeatureAvailability
+ WBSOSLogSearchFeatureAvailability.log
+ WBSOSLogSearchFeatureAvailability.onceToken
+ _OBJC_CLASS_$_WBSGuidedBrowsingNavigationEvent
+ _OBJC_METACLASS_$_WBSGuidedBrowsingNavigationEvent
+ _PROTOCOLS_WBSGuidedBrowsingNavigationEvent
+ _WBSAutomaticPasswordChangeDebugLogAutoFilledDataKey
+ _WBSDebugNotifyMeWhenJitterEnabledKey
+ _WBSOSLogSearchFeatureAvailability
+ _WBSTimeUntilNextTwiceDailyAnalyticsReportForKey
+ __124-[WBSSavedAccountStore canSaveUser:password:forProtectionSpace:highLevelDomain:notes:customTitle:groupID:completionHandler:]_block_invoke
+ __69-[WBSPasswordWarningManager _getAllWarningsOnWorkQueueForcingUpdate:]_block_invoke
+ __69-[WBSPasswordWarningManager _getAllWarningsOnWorkQueueForcingUpdate:]_block_invoke_2
+ __73-[WBSFileVaultRecoveryKeyListenerProxy saveRecoveryKeyWithRequest:error:]_block_invoke
+ __73-[WBSFileVaultRecoveryKeyListenerProxy saveRecoveryKeyWithRequest:error:]_block_invoke_2
+ __74-[WBSFileVaultRecoveryKeyListenerProxy recoveryKeysForSerialNumber:error:]_block_invoke
+ __74-[WBSFileVaultRecoveryKeyListenerProxy recoveryKeysForSerialNumber:error:]_block_invoke_2
+ __82-[WBSFileVaultRecoveryKeyListenerProxy recoveryKeyForVolumeID:serialNumber:error:]_block_invoke
+ __82-[WBSFileVaultRecoveryKeyListenerProxy recoveryKeyForVolumeID:serialNumber:error:]_block_invoke_2
+ __86-[WBSFileVaultRecoveryKeyListenerProxy _synchronousRemoteObjectProxyWithErrorHandler:]_block_invoke
+ __88-[WBSFileVaultRecoveryKeyListenerProxy deleteRecoveryKeyForVolumeID:serialNumber:error:]_block_invoke
+ __88-[WBSFileVaultRecoveryKeyListenerProxy deleteRecoveryKeyForVolumeID:serialNumber:error:]_block_invoke_2
+ __CLASS_METHODS_WBSGuidedBrowsingNavigationEvent
+ __CLASS_PROPERTIES_WBSGuidedBrowsingNavigationEvent
+ __DATA_WBSGuidedBrowsingNavigationEvent
+ __INSTANCE_METHODS_WBSGuidedBrowsingNavigationEvent
+ __IVARS_WBSGuidedBrowsingNavigationEvent
+ __IVARS__TtCE10SafariCoreV15Synchronization5MutexP33_5EB6CF0E21105A7FACDF3B64E2151CBD10SendingBox
+ __METACLASS_DATA_WBSGuidedBrowsingNavigationEvent
+ __OBJC_$_INSTANCE_METHODS_WBSAnalyticsLogger(ForegroundReturnAnalyticsLogger)
+ __OBJC_$_INSTANCE_METHODS_WBSSavedAccountChangeRequest(SafariCore)
+ __PROPERTIES_WBSGuidedBrowsingNavigationEvent
+ __PROTOCOLS_WBSGuidedBrowsingNavigationEvent
+ __ZL30configureCommonSessionSettingsP25NSURLSessionConfiguration
+ ___111-[WBSSavedAccountStore _savedAccountConflictingWithSavedAccountOnInternalQueue:afterUpdatingUsername:password:]_block_invoke
+ ___124-[WBSSavedAccountStore canSaveUser:password:forProtectionSpace:highLevelDomain:notes:customTitle:groupID:completionHandler:]_block_invoke
+ ___49-[WBSSavedAccount lastUsedDateForSite:inContext:]_block_invoke
+ ___58-[WBSSavedAccountTreeMatch pruneFileVaultRecoveryKeyTrees]_block_invoke
+ ___69-[WBSPasswordWarningManager _getAllWarningsOnWorkQueueForcingUpdate:]_block_invoke
+ ___69-[WBSPasswordWarningManager _getAllWarningsOnWorkQueueForcingUpdate:]_block_invoke_2
+ ___73-[WBSFileVaultRecoveryKeyListenerProxy saveRecoveryKeyWithRequest:error:]_block_invoke
+ ___73-[WBSFileVaultRecoveryKeyListenerProxy saveRecoveryKeyWithRequest:error:]_block_invoke_2
+ ___74-[WBSFileVaultRecoveryKeyListenerProxy recoveryKeysForSerialNumber:error:]_block_invoke
+ ___74-[WBSFileVaultRecoveryKeyListenerProxy recoveryKeysForSerialNumber:error:]_block_invoke_2
+ ___81-[WBSSavedAccountStore _logSavedAccountsWithTOTPGeneratorsOnlyInPasskeySidecars:]_block_invoke
+ ___81-[WBSSavedAccountStore _logSavedAccountsWithTOTPGeneratorsOnlyInPasskeySidecars:]_block_invoke_2
+ ___82-[WBSFileVaultRecoveryKeyListenerProxy recoveryKeyForVolumeID:serialNumber:error:]_block_invoke
+ ___82-[WBSFileVaultRecoveryKeyListenerProxy recoveryKeyForVolumeID:serialNumber:error:]_block_invoke_2
+ ___86-[WBSFileVaultRecoveryKeyListenerProxy _synchronousRemoteObjectProxyWithErrorHandler:]_block_invoke
+ ___88-[WBSFileVaultRecoveryKeyListenerProxy deleteRecoveryKeyForVolumeID:serialNumber:error:]_block_invoke
+ ___88-[WBSFileVaultRecoveryKeyListenerProxy deleteRecoveryKeyForVolumeID:serialNumber:error:]_block_invoke_2
+ ___94-[WBSAnalyticsLogger didDetectSearchEngineBannerWithLinkToApp:wasUserLoggedIn:pageLoadSource:]_block_invoke
+ ___94-[WBSSavedAccountStore canSaveUser:password:forUserTypedSite:notes:customTitle:groupID:error:]_block_invoke
+ ___96-[NSURLProtectionSpace(SafariCoreExtras) safari_getAllowsCredentialSavingWithCompletionHandler:]_block_invoke
+ ___96-[NSURLProtectionSpace(SafariCoreExtras) safari_getAllowsCredentialSavingWithCompletionHandler:]_block_invoke_2
+ ___WBSOSLogSearchFeatureAvailability_block_invoke
+ ___block_descriptor_32_e30_B16?0"WBSSavedAccountMatch"8l
+ ___block_descriptor_32_e32_B32?0"WBSSavedAccount"8Q16^B24l
+ ___block_descriptor_40_e8_32bs_e36_v16?0"WBSSavedAccountMatchResult"8l
+ ___block_descriptor_40_e8_32r_e49_v32?0q8"<WBSSavedAccountSidecarInternal>"16^B24l
+ ___block_descriptor_41_e8_32s_e46_v32?0"NSString"8"NSMutableDictionary"16^B24l
+ ___block_descriptor_48_e8_32r40r_e17_v16?0"NSError"8l
+ ___block_descriptor_48_e8_32s40r_e8_v12?0B8l
+ ___block_descriptor_56_e8_32r40r48r_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_56_e8_32r40r48r_e45_v24?0"WBSFileVaultRecoveryKey"8"NSError"16l
+ ___block_descriptor_56_e8_32s40r48r_e20_v20?0B8"NSError"12l
+ ___block_descriptor_56_e8_32s40r_e17_v16?0"NSError"8l
+ ___block_descriptor_56_e8_32s40s48r_e46_v32?0"NSString"8"NSMutableDictionary"16^B24l
+ ___block_descriptor_73_e8_32s40s48s56s64r_e42_v32?0"NSString"8"WBSSavedAccount"16^B24l
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80s88bs_e5_v8?0l
+ ___copy_helper_block_e8_32r40r48r
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88b
+ ___destroy_helper_block_e8_32r40r48r
+ ___unnamed_2
+ __swift_closure_destructor.125Tm
+ __swift_closure_destructor.244Tm
+ __swift_closure_destructor.254Tm
+ __swift_closure_destructor.409Tm
+ __swift_closure_destructor.467Tm
+ __swift_closure_destructor.54Tm
+ __swift_closure_destructor.583Tm
+ __swift_closure_destructor.58Tm
+ _automaticPasswordChangeTestFestModeEnabled
+ _finalizeSyncResult
+ _objc_msgSend$_adoptSidecarDataFromSavedAccount:
+ _objc_msgSend$_getAllWarningsOnWorkQueueForcingUpdate:
+ _objc_msgSend$_logSavedAccountsWithTOTPGeneratorsOnlyInPasskeySidecars:
+ _objc_msgSend$_savedAccountConflictingWithSavedAccountOnInternalQueue:afterUpdatingUsername:password:
+ _objc_msgSend$_savedAccountDidAdoptSidecarDataFromConflictingSavedAccount:
+ _objc_msgSend$_synchronousRemoteObjectProxyWithErrorHandler:
+ _objc_msgSend$automaticPasswordChangeShouldAlwaysRecommend
+ _objc_msgSend$canSaveUser:password:forProtectionSpace:highLevelDomain:notes:customTitle:groupID:completionHandler:
+ _objc_msgSend$canSaveUser:password:forUserTypedSite:notes:customTitle:groupID:completionHandler:
+ _objc_msgSend$currentURLChanged:inTabWithUUID:
+ _objc_msgSend$defaultSessionConfiguration
+ _objc_msgSend$emailProviderFraudTargets
+ _objc_msgSend$initWithHighPriorityTargets:targets:financialTargets:emailProviderFraudTargets:
+ _objc_msgSend$isAutomaticPasswordChangeTestFestModeEnabled
+ _objc_msgSend$isDebugAccountForAutomaticPasswordChangeForDomain:
+ _objc_msgSend$isUUIDHighLevelDomain:
+ _objc_msgSend$pruneFileVaultRecoveryKeyTrees
+ _objc_msgSend$reportNavigationEvent:inTabWithUUID:
+ _objc_msgSend$safari_getAllowsCredentialSavingWithCompletionHandler:
+ _objc_msgSend$setConnectionCodeSigningRequirement:
+ _objc_msgSend$set_sourceApplicationBundleIdentifier:
+ _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
+ _symbolic $s10SafariCore45WBSAutomaticPasswordChangeCompletionReportingP
+ _symbolic SS_So8NSObjectCt
+ _symbolic Shy_____G 10Foundation4UUIDV
+ _symbolic _____ 10SafariCore32WBSGuidedBrowsingNavigationEventC
+ _symbolic _____ 15Synchronization5MutexV10SafariCoreE10SendingBox33_5EB6CF0E21105A7FACDF3B64E2151CBDLLC
+ _symbolic _____ So35WBSAnalyticsForegroundReturnOutcomeV
+ _symbolic _____ So43WBSAnalyticsForegroundReturnAwayDurationBinV
+ _symbolic _____SgXwz_Xx 10SafariCore27WBSGuidedBrowsingControllerC
+ _symbolic ______pIeghg_ 10SafariCore39WBSGuidedBrowsingUIRegistrationProtocolP
+ _symbolic _____m 10SafariCore32WBSGuidedBrowsingNavigationEventC
+ _symbolic _____ySSSo8NSObjectCG s18_DictionaryStorageC
+ _symbolic _____ySS_So8NSObjectCtG s23_ContiguousArrayStorageC
+ _symbolic _____ySbG 15Synchronization6AtomicV
+ _symbolic _____yShy_____GG 15Synchronization5MutexVAARi_zrlE 10Foundation4UUIDV
+ _symbolic _____ySo15NSXPCConnectionCSgG 15Synchronization5MutexVAARi_zrlE
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 10Foundation4UUIDV
+ _symbolic _____yxG 15Synchronization5MutexVAARi_zrlE
- +[WBSFeatureAvailability isAllowFavoritesInFrequentlyVisitedEnabled]
- +[WBSFeatureAvailability isAllowLogOnURLsInFrequentlyVisitedEnabled]
- +[WBSFeatureAvailability isDropOutliersInFrequentlyVisitedEnabled]
- -[WBSAnalyticsLogger didDetectSearchEngineBannerWithLinkToApp:wasUserLoggedIn:]
- -[WBSPasswordWarningTopFraudTargets initWithHighPriorityTargets:targets:financialTargets:]
- -[WBSWellKnownChangePasswordURLFallbackController didFinishLoad]
- GCC_except_table104
- GCC_except_table124
- GCC_except_table128
- GCC_except_table134
- GCC_except_table137
- GCC_except_table146
- GCC_except_table148
- GCC_except_table150
- GCC_except_table152
- GCC_except_table154
- GCC_except_table156
- GCC_except_table166
- GCC_except_table168
- GCC_except_table170
- GCC_except_table172
- GCC_except_table174
- GCC_except_table176
- GCC_except_table182
- GCC_except_table184
- GCC_except_table186
- GCC_except_table188
- GCC_except_table190
- GCC_except_table194
- GCC_except_table198
- GCC_except_table200
- GCC_except_table202
- GCC_except_table204
- GCC_except_table206
- GCC_except_table210
- GCC_except_table214
- GCC_except_table216
- GCC_except_table220
- GCC_except_table222
- GCC_except_table224
- GCC_except_table232
- GCC_except_table234
- GCC_except_table236
- GCC_except_table238
- GCC_except_table240
- GCC_except_table243
- GCC_except_table246
- GCC_except_table249
- GCC_except_table251
- GCC_except_table253
- GCC_except_table254
- GCC_except_table256
- GCC_except_table259
- GCC_except_table262
- GCC_except_table265
- GCC_except_table270
- GCC_except_table272
- GCC_except_table276
- GCC_except_table279
- GCC_except_table284
- GCC_except_table290
- GCC_except_table292
- GCC_except_table294
- GCC_except_table297
- GCC_except_table300
- GCC_except_table303
- GCC_except_table309
- GCC_except_table333
- GCC_except_table335
- GCC_except_table337
- GCC_except_table339
- GCC_except_table343
- GCC_except_table348
- GCC_except_table357
- GCC_except_table359
- GCC_except_table364
- GCC_except_table366
- GCC_except_table368
- GCC_except_table370
- GCC_except_table375
- GCC_except_table384
- GCC_except_table390
- GCC_except_table392
- GCC_except_table394
- GCC_except_table398
- GCC_except_table400
- GCC_except_table403
- GCC_except_table405
- GCC_except_table407
- GCC_except_table409
- GCC_except_table417
- GCC_except_table419
- GCC_except_table421
- GCC_except_table425
- GCC_except_table427
- GCC_except_table435
- GCC_except_table447
- GCC_except_table452
- GCC_except_table456
- GCC_except_table459
- GCC_except_table465
- GCC_except_table470
- GCC_except_table474
- GCC_except_table478
- GCC_except_table481
- GCC_except_table484
- GCC_except_table486
- GCC_except_table489
- GCC_except_table491
- GCC_except_table495
- GCC_except_table498
- GCC_except_table501
- GCC_except_table505
- GCC_except_table508
- GCC_except_table518
- GCC_except_table522
- GCC_except_table524
- GCC_except_table526
- GCC_except_table528
- GCC_except_table530
- GCC_except_table532
- GCC_except_table534
- GCC_except_table536
- GCC_except_table538
- GCC_except_table540
- GCC_except_table58
- GCC_except_table72
- GCC_except_table79
- GCC_except_table83
- GCC_except_table87
- _WBSEnableDropOutliersInFrequentlyVisitedKey
- _WBSFrequentlyVisitedSitesAllowLogonURLsPreferenceKey
- _WBSFrequentlyVisitedSitesAllowSitesFromFavoritesPreferenceKey
- __112-[WBSSavedAccountStore canSaveUser:password:forProtectionSpace:highLevelDomain:notes:customTitle:groupID:error:]_block_invoke
- __75-[WBSPasswordWarningManager getAllWarningsForcingUpdate:completionHandler:]_block_invoke_2
- __OBJC_$_CLASS_PROP_LIST_NSURLSessionConfiguration_$_SafariCoreExtras
- __OBJC_$_INSTANCE_METHODS_WBSAnalyticsLogger
- __OBJC_$_INSTANCE_METHODS_WBSSavedAccountChangeRequest
- ___75-[WBSPasswordWarningManager getAllWarningsForcingUpdate:completionHandler:]_block_invoke_2
- ___75-[WBSPasswordWarningManager getAllWarningsForcingUpdate:completionHandler:]_block_invoke_3
- ___79-[WBSAnalyticsLogger didDetectSearchEngineBannerWithLinkToApp:wasUserLoggedIn:]_block_invoke
- ___block_descriptor_104_e8_32s40s48s56s64s72s80s88r96r_e5_v8?0l
- ___block_descriptor_48_e8_32s40s_e46_v32?0"NSString"8"NSMutableDictionary"16^B24l
- ___copy_helper_block_e8_32s40s48s56s64s72s80s88r96r
- ___destroy_helper_block_e8_32s40s48s56s64s72s80s88r96r
- __swift_closure_destructor.238Tm
- __swift_closure_destructor.248Tm
- __swift_closure_destructor.403Tm
- __swift_closure_destructor.461Tm
- __swift_closure_destructor.53Tm
- __swift_closure_destructor.577Tm
- __swift_closure_destructor.57Tm
- _objc_msgSend$initWithHighPriorityTargets:targets:financialTargets:
- _objc_msgSend$safari_isAppleSigned
- _symbolic So15NSXPCConnectionC
- _symbolic _____y_____G s23_ContiguousArrayStorageC 10SafariCore26WBSLocalizedPluralVariableV
CStrings:
+ "(null)"
+ "-[WBSSavedAccountStore canSaveUser:password:forUserTypedSite:notes:customTitle:groupID:error:]"
+ "AuthenticationServicesAgent connection failed in %{public}@: %{public}@"
+ "Connected to broker"
+ "Error reporting navigation state to broker: %{public}s"
+ "Exceeded %.2f sec timeout while checking wheather credential saving is allowed for %{sensitive}@"
+ "Expired %.2f timeout waiting for canSaveUser:password: call to resolve"
+ "Expired %.2f timeout waiting for canSaveUser:password:forProtectionSpace: to complete"
+ "Expired timeout waiting for canSaveUser:password:forProtectionSpace: to complete"
+ "Failed to acquire synchronous remote object proxy."
+ "Found %lu saved account(s) with a TOTP generator in a passkey sidecar but not in a password sidecar"
+ "Found saved account for '%{sensitive}@' on %{sensitive}@ that will conflict with saved account for '%{sensitive}@' after updating username"
+ "Guided browser connection dropped during teardown; not reconnecting"
+ "No reply from AuthenticationServicesAgent."
+ "PMAutomaticPasswordChangeDebugLogAutoFilledData"
+ "SafariCore.WBSGuidedBrowsingNavigationEvent"
+ "SearchFeatureAvailability"
+ "Synchronous remote proxy object error handler invoked with error: %{public}@"
+ "Unable to decode target URL for navigation event"
+ "WBSDebugNotifyMeWhenJitterEnabled"
+ "WBSGuidedBrowsingNavigationEvent { targetURL (hash) = "
+ "com.apple.Safari.Foreground.DidResolveOutcome"
+ "currentURLChanged"
+ "emailProviderFraudTargets"
+ "pageLoadSource"
+ "reportNavigationEvent"
+ "v24@?0@\"WBSFileVaultRecoveryKey\"8@\"NSError\"16"
- "EnableDropOutliersInFrequentlyVisited"
- "FrequentlyVisitedSitesAllowLogonURLs"
- "FrequentlyVisitedSitesAllowSitesFromFavorites"
- "Incoming connection from %{private}s is not Apple-signed, rejecting"
- "New strong password has been saved for %ld"
- "New strong passwords have been saved for %ld"
- "New strong passwords have been saved for %ld out of %ld accounts."
- "strongPasswordsMessage"
- "wasUserLoggedIn"
```
