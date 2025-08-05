## CoreServices

> `/System/Library/Frameworks/CoreServices.framework/CoreServices`

```diff

-1439.0.0.0.0
-  __TEXT.__text: 0x1a5ea8
-  __TEXT.__auth_stubs: 0x2fe0
+1441.3.0.0.0
+  __TEXT.__text: 0x1a6428
+  __TEXT.__auth_stubs: 0x3060
   __TEXT.__delay_stubs: 0x2c
   __TEXT.__delay_helper: 0x16c
-  __TEXT.__objc_methlist: 0xcb1c
+  __TEXT.__objc_methlist: 0xcb54
   __TEXT.__const: 0x910
-  __TEXT.__cstring: 0x240c6
-  __TEXT.__oslogstring: 0x130f8
-  __TEXT.__gcc_except_tab: 0x268ec
+  __TEXT.__cstring: 0x241e6
+  __TEXT.__oslogstring: 0x13114
+  __TEXT.__gcc_except_tab: 0x26918
   __TEXT.__ustring: 0x23c
   __TEXT.__unwind_info: 0xaea8
   __TEXT.__eh_frame: 0x60
   __TEXT.__objc_classname: 0x1e43
-  __TEXT.__objc_methname: 0x1cba9
-  __TEXT.__objc_methtype: 0x9f38
-  __TEXT.__objc_stubs: 0x101c0
+  __TEXT.__objc_methname: 0x1cc40
+  __TEXT.__objc_methtype: 0x9f57
+  __TEXT.__objc_stubs: 0x10220
   __DATA_CONST.__got: 0xa78
-  __DATA_CONST.__const: 0x6ba8
+  __DATA_CONST.__const: 0x6c00
   __DATA_CONST.__objc_classlist: 0x698
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5df8
+  __DATA_CONST.__objc_selrefs: 0x5e18
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x550
   __DATA_CONST.__objc_arraydata: 0x180
-  __AUTH_CONST.__auth_got: 0x1810
-  __AUTH_CONST.__const: 0x35c0
-  __AUTH_CONST.__cfstring: 0x167a0
-  __AUTH_CONST.__objc_const: 0x12bd0
+  __AUTH_CONST.__auth_got: 0x1850
+  __AUTH_CONST.__const: 0x3588
+  __AUTH_CONST.__cfstring: 0x16820
+  __AUTH_CONST.__objc_const: 0x12be0
   __AUTH_CONST.__objc_intobj: 0x810
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x120
-  __AUTH.__objc_data: 0x2ad0
+  __AUTH.__objc_data: 0x2a80
   __AUTH.__data: 0x318
-  __DATA.__objc_ivar: 0xa70
+  __DATA.__objc_ivar: 0xa6c
   __DATA.__data: 0x1260
   __DATA.__bss: 0xe78
   __DATA.__common: 0x40
-  __DATA_DIRTY.__objc_data: 0x1720
+  __DATA_DIRTY.__objc_data: 0x1770
   __DATA_DIRTY.__data: 0x50
   __DATA_DIRTY.__crash_info: 0x148
   __DATA_DIRTY.__bss: 0x8c8

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: E6E2A9ED-4A2A-394A-A017-172A53898CC8
-  Functions: 8545
-  Symbols:   27776
-  CStrings:  13503
+  UUID: 6FAC58DA-7B8F-3272-A512-FFB6C5D826F6
+  Functions: 8553
+  Symbols:   27802
+  CStrings:  13516
 
Symbols:
+ -[LSApplicationRecord(InfoPlistRarities) serializedPlaceholderPath]
+ -[LSApplicationRestrictionsManager reasonForApplicationRestriction:checkFlags:stateProvider:]
+ -[LSApplicationWorkspace(DefaultApps) setPreferenceForNoHandlerForCategory:completionHandler:]
+ -[LSClaimBindingConfiguration honorPreferenceForNoHandler]
+ -[LSClaimBindingConfiguration setHonorPreferenceForNoHandler:]
+ -[_LSApplicationState restrictionReasonWithStateProvider:]
+ -[_LSApplicationState restrictionReason]
+ GCC_except_table165
+ GCC_except_table192
+ GCC_except_table260
+ GCC_except_table269
+ GCC_except_table271
+ GCC_except_table273
+ GCC_except_table276
+ GCC_except_table283
+ GCC_except_table288
+ GCC_except_table291
+ GCC_except_table303
+ GCC_except_table310
+ GCC_except_table312
+ GCC_except_table322
+ GCC_except_table328
+ GCC_except_table341
+ GCC_except_table344
+ GCC_except_table350
+ GCC_except_table355
+ GCC_except_table358
+ GCC_except_table365
+ GCC_except_table371
+ GCC_except_table374
+ GCC_except_table380
+ GCC_except_table384
+ GCC_except_table387
+ GCC_except_table400
+ GCC_except_table403
+ GCC_except_table407
+ GCC_except_table433
+ GCC_except_table439
+ GCC_except_table443
+ GCC_except_table449
+ GCC_except_table453
+ GCC_except_table454
+ GCC_except_table467
+ GCC_except_table486
+ GCC_except_table487
+ GCC_except_table490
+ GCC_except_table495
+ GCC_except_table496
+ __LSApplicationRestrictionsManagerReasonForApplicationRestriction
+ __LSNoHandlerIdentifier
+ __ZN14LaunchServices17BindingEvaluationL16addStrongBindingERNS0_5StateE
+ ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.643
+ ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.643.cold.1
+ ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.644
+ ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.644.cold.1
+ ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.644.cold.2
+ ___59-[_LSDModifyClient removeAllHandlersWithCompletionHandler:]_block_invoke_2
+ ___59-[_LSDModifyClient requestLSDExitSafely:completionHandler:]_block_invoke.308
+ ___59-[_LSDModifyClient requestLSDExitSafely:completionHandler:]_block_invoke.311
+ ___59-[_LSDModifyClient requestLSDExitSafely:completionHandler:]_block_invoke.314
+ ___68-[LSApplicationWorkspaceRemoteObserver applicationInstallsDidStart:]_block_invoke.757
+ ___75-[_LSDModifyClient unregisterApplicationsAtMountPoint:operationUUID:reply:]_block_invoke.253
+ ___78-[LSApplicationRecord(AlternateIcons) setAlternateIconName:completionHandler:]_block_invoke.635
+ ___78-[LSApplicationRecord(AlternateIcons) setAlternateIconName:completionHandler:]_block_invoke.635.cold.1
+ ___84-[_LSDModifyClient setPreferenceValue:forKey:forApplicationAtURL:completionHandler:]_block_invoke.288
+ ___94-[LSApplicationWorkspace(DefaultApps) setPreferenceForNoHandlerForCategory:completionHandler:]_block_invoke
+ ___98-[_LSDModifyClient performUpdateOfPersonasOfBundleIDs:toPersonaUniqueStrings:operationUUID:reply:]_block_invoke.307
+ ___Block_byref_object_copy_.1012
+ ___Block_byref_object_copy_.1194
+ ___Block_byref_object_copy_.162
+ ___Block_byref_object_copy_.165
+ ___Block_byref_object_copy_.387
+ ___Block_byref_object_copy_.42
+ ___Block_byref_object_copy_.688
+ ___Block_byref_object_copy_.76
+ ___Block_byref_object_dispose_.1013
+ ___Block_byref_object_dispose_.1195
+ ___Block_byref_object_dispose_.163
+ ___Block_byref_object_dispose_.166
+ ___Block_byref_object_dispose_.388
+ ___Block_byref_object_dispose_.43
+ ___Block_byref_object_dispose_.689
+ ___Block_byref_object_dispose_.77
+ ____LSHandlerPrefRemoveAllWithBundleID_block_invoke.66
+ ____LSHandlerPrefRemoveAllWithBundleID_block_invoke.70
+ ____LSHandlerPrefRemoveAllWithBundleID_block_invoke.70.cold.1
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.940
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.940.cold.1
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.944.cold.1
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.946
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.947
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke_2.945
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke_2.949
+ ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke_2.949.cold.1
+ ____LSServer_SyncWithMobileInstallation_block_invoke.1014
+ ____LSServer_SyncWithMobileInstallation_block_invoke_2.1015
+ ____ZN13LSHandlerPref4SaveEP11_LSDatabase_block_invoke.59
+ ____ZN14LaunchServices12PrefsStorage15setValueForNodeEP8NSStringP6FSNodeP11objc_objectPU15__autoreleasingP7NSError_block_invoke.103
+ ____ZN14LaunchServices12PrefsStorage7_updateEv_block_invoke.79
+ ____ZN14LaunchServices12PrefsStorage7_updateEv_block_invoke.79.cold.1
+ ___block_descriptor_104_ea8_32r40r48r56r64r72r80r88r96rc_e42_v24?0"LSDBExecutionContext"8"NSError"16lr32l8r40l8r48l8r56l8r64l8r72l8r80l8r88l8r96l8
+ ___block_descriptor_48_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_72_ea8_32r40r48r56r64rc_e5_v8?0lr32l8r40l8r48l8r56l8r64l8
+ ___block_literal_global.1099
+ ___block_literal_global.1122
+ ___block_literal_global.1149
+ ___block_literal_global.1151
+ ___block_literal_global.1162
+ ___block_literal_global.253
+ ___block_literal_global.255
+ ___block_literal_global.313
+ ___block_literal_global.316
+ ___block_literal_global.334
+ ___block_literal_global.632
+ ___block_literal_global.919
+ ___block_literal_global.947
+ ___block_literal_global.98
+ ___block_literal_global.986
+ _audit_token_to_asid
+ _audit_token_to_auid
+ _audit_token_to_egid
+ _audit_token_to_euid
+ _audit_token_to_pidversion
+ _audit_token_to_rgid
+ _audit_token_to_ruid
+ _computeApplicationRestrictionReasonWithMCStateProvider
+ _dispatch_workloop_create_inactive
+ _dispatch_workloop_set_autorelease_frequency
+ _objc_msgSend$bindableWithTypeIdentifier:
+ _objc_msgSend$honorPreferenceForNoHandler
+ _objc_msgSend$initWithConfiguration:error:
+ _objc_msgSend$restrictionReasonWithStateProvider:
+ _objc_msgSend$setHonorPreferenceForNoHandler:
- -[_LSDClient(Private) handleXPCInvocation:isReply:].cold.1
- -[_LSDClient(Private) initWithXPCConnection:queue:]
- GCC_except_table118
- GCC_except_table152
- GCC_except_table186
- GCC_except_table256
- GCC_except_table268
- GCC_except_table270
- GCC_except_table272
- GCC_except_table275
- GCC_except_table278
- GCC_except_table286
- GCC_except_table289
- GCC_except_table300
- GCC_except_table305
- GCC_except_table309
- GCC_except_table311
- GCC_except_table321
- GCC_except_table325
- GCC_except_table340
- GCC_except_table343
- GCC_except_table349
- GCC_except_table353
- GCC_except_table356
- GCC_except_table363
- GCC_except_table368
- GCC_except_table373
- GCC_except_table375
- GCC_except_table381
- GCC_except_table385
- GCC_except_table399
- GCC_except_table402
- GCC_except_table406
- GCC_except_table431
- GCC_except_table437
- GCC_except_table441
- GCC_except_table445
- GCC_except_table451
- GCC_except_table452
- GCC_except_table465
- GCC_except_table484
- GCC_except_table485
- GCC_except_table488
- GCC_except_table491
- GCC_except_table494
- _OBJC_IVAR_$__LSDClient._queue
- __LSServer_MakeServiceFloorBlock
- ___51-[_LSDClient(Private) handleXPCInvocation:isReply:]_block_invoke
- ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.641
- ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.641.cold.1
- ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.642
- ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.642.cold.1
- ___56-[LSApplicationRecord(AlternateIcons) alternateIconName]_block_invoke.642.cold.2
- ___59-[_LSDModifyClient removeAllHandlersWithCompletionHandler:]_block_invoke.203
- ___59-[_LSDModifyClient requestLSDExitSafely:completionHandler:]_block_invoke.303
- ___59-[_LSDModifyClient requestLSDExitSafely:completionHandler:]_block_invoke.306
- ___59-[_LSDModifyClient requestLSDExitSafely:completionHandler:]_block_invoke.309
- ___68-[LSApplicationWorkspaceRemoteObserver applicationInstallsDidStart:]_block_invoke.754
- ___75-[_LSDModifyClient unregisterApplicationsAtMountPoint:operationUUID:reply:]_block_invoke.243
- ___78-[LSApplicationRecord(AlternateIcons) setAlternateIconName:completionHandler:]_block_invoke.633
- ___78-[LSApplicationRecord(AlternateIcons) setAlternateIconName:completionHandler:]_block_invoke.633.cold.1
- ___84-[_LSDModifyClient setPreferenceValue:forKey:forApplicationAtURL:completionHandler:]_block_invoke.283
- ___98-[_LSDModifyClient performUpdateOfPersonasOfBundleIDs:toPersonaUniqueStrings:operationUUID:reply:]_block_invoke.302
- ___Block_byref_object_copy_.1009
- ___Block_byref_object_copy_.1191
- ___Block_byref_object_copy_.382
- ___Block_byref_object_copy_.39
- ___Block_byref_object_copy_.686
- ___Block_byref_object_copy_.73
- ___Block_byref_object_dispose_.1010
- ___Block_byref_object_dispose_.1192
- ___Block_byref_object_dispose_.383
- ___Block_byref_object_dispose_.40
- ___Block_byref_object_dispose_.687
- ___Block_byref_object_dispose_.74
- ____LSHandlerPrefRemoveAllWithBundleID_block_invoke.63
- ____LSHandlerPrefRemoveAllWithBundleID_block_invoke.67
- ____LSHandlerPrefRemoveAllWithBundleID_block_invoke.67.cold.1
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.937
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.937.cold.1
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.941
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.941.cold.1
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke.943
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke_2.939
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke_2.946
- ____LSServer_LSEnumerateAndRegisterAllBundles_block_invoke_2.946.cold.1
- ____LSServer_SyncWithMobileInstallation_block_invoke.1011
- ____LSServer_SyncWithMobileInstallation_block_invoke_2.1012
- ____ZN13LSHandlerPref4SaveEP11_LSDatabase_block_invoke.56
- ____ZN14LaunchServices12PrefsStorage15setValueForNodeEP8NSStringP6FSNodeP11objc_objectPU15__autoreleasingP7NSError_block_invoke.100
- ____ZN14LaunchServices12PrefsStorage7_updateEv_block_invoke.76
- ____ZN14LaunchServices12PrefsStorage7_updateEv_block_invoke.76.cold.1
- ___block_descriptor_121_ea8_32s40s48s56s64s72s80s88s96bs104r112c30_ZTS10CFReleaserIPK9__CFArrayE_e42_v24?0"LSDBExecutionContext"8"NSError"16l
- ___block_descriptor_88_ea8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s80l8s40l8s48l8s56l8s64l8s72l8
- ___block_literal_global.1096
- ___block_literal_global.1119
- ___block_literal_global.1146
- ___block_literal_global.1148
- ___block_literal_global.1159
- ___block_literal_global.247
- ___block_literal_global.249
- ___block_literal_global.305
- ___block_literal_global.308
- ___block_literal_global.311
- ___block_literal_global.329
- ___block_literal_global.630
- ___block_literal_global.916
- ___block_literal_global.945
- ___block_literal_global.95
- ___block_literal_global.984
- ___copy_helper_block_ea8_112c30_ZTS10CFReleaserIPK9__CFArrayE
- ___destroy_helper_block_ea8_112c30_ZTS10CFReleaserIPK9__CFArrayE
- _computeIsApplicationRestrictedWithMCStateProvider
- _objc_msgSend$initWithXPCConnection:queue:
- _objc_msgSend$retainArguments
- _qos_class_self
CStrings:
+ "-[LSApplicationWorkspace(DefaultApps) setPreferenceForNoHandlerForCategory:completionHandler:]_block_invoke"
+ "-[_LSDModifyClient registerItemInfo:alias:diskImageAlias:bundleURL:installationPlist:completionHandler:]"
+ "[pid:%d/%d uid:%d/%d gid:%d/%d %d/%d]"
+ "checkForExfiltrationRisk: Checking if token %{public}@ is allowed to map the LS database or is a platform binary."
+ "com.apple.coreservices.nohandler$BF6A2FC2-EAE7-4116-BEF3-495EAA007C85"
+ "honorPreferenceForNoHandler"
+ "restrictionReason"
+ "restrictionReasonWithStateProvider:"
+ "serializedPlaceholderPath"
+ "setHonorPreferenceForNoHandler:"
+ "setPreferenceForNoHandlerForCategory:completionHandler:"
+ "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /Library/Caches/com.apple.xbs/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1416:63)]"
+ "still checking for any strong binding preference"
+ "user prefers no handler for : %@ %@"
+ "{?=\"allowWildcardClaims\"b1\"ignoreStrongBindingPreferences\"b1\"ignoreWeakBindingPreferences\"b1\"requireOpenInPlace\"b1\"honorPreferenceForNoHandler\"b1}"
- "-[_LSDModifyClient registerItemInfo:alias:diskImageAlias:bundleURL:installationPlist:completionHandler:]_block_invoke"
- "Failed to create dispatch_block_t for XPC message -[%{public}s %{public}s], aborting."
- "initWithXPCConnection:queue:"
- "retainArguments"
- "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /Library/Caches/com.apple.xbs/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1413:63)]"
- "{?=\"allowWildcardClaims\"b1\"ignoreStrongBindingPreferences\"b1\"ignoreWeakBindingPreferences\"b1\"requireOpenInPlace\"b1}"

```
