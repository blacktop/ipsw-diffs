## ScreenTimeCore

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore`

```diff

-649.0.0.0.0
-  __TEXT.__text: 0xf3a7c
-  __TEXT.__objc_methlist: 0xa140
-  __TEXT.__const: 0x32a8
-  __TEXT.__cstring: 0xa52c
-  __TEXT.__oslogstring: 0xbafa
-  __TEXT.__gcc_except_tab: 0x1b30
-  __TEXT.__swift5_typeref: 0x14cc
-  __TEXT.__constg_swiftt: 0xd0c
+655.0.101.0.0
+  __TEXT.__text: 0xfb294
+  __TEXT.__objc_methlist: 0xa388
+  __TEXT.__const: 0x3458
+  __TEXT.__cstring: 0xa84c
+  __TEXT.__oslogstring: 0xbfea
+  __TEXT.__gcc_except_tab: 0x1b2c
+  __TEXT.__swift5_typeref: 0x1544
+  __TEXT.__constg_swiftt: 0xde8
   __TEXT.__swift5_builtin: 0xf0
-  __TEXT.__swift5_reflstr: 0x7be
-  __TEXT.__swift5_fieldmd: 0x9b4
+  __TEXT.__swift5_reflstr: 0x7de
+  __TEXT.__swift5_fieldmd: 0xa00
   __TEXT.__swift5_assocty: 0x138
-  __TEXT.__swift5_proto: 0x210
-  __TEXT.__swift5_types: 0xe8
-  __TEXT.__swift5_capture: 0xa84
-  __TEXT.__swift5_protos: 0x10
-  __TEXT.__swift_as_entry: 0x158
-  __TEXT.__swift_as_ret: 0x188
-  __TEXT.__swift_as_cont: 0x220
+  __TEXT.__swift5_proto: 0x214
+  __TEXT.__swift5_types: 0xf4
+  __TEXT.__swift5_capture: 0xb08
+  __TEXT.__swift5_protos: 0x14
+  __TEXT.__swift_as_entry: 0x164
+  __TEXT.__swift_as_ret: 0x194
+  __TEXT.__swift_as_cont: 0x228
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x3df8
-  __TEXT.__eh_frame: 0x3d90
+  __TEXT.__unwind_info: 0x3f40
+  __TEXT.__eh_frame: 0x4078
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1d48
-  __DATA_CONST.__objc_classlist: 0x6e0
+  __DATA_CONST.__const: 0x1d98
+  __DATA_CONST.__objc_classlist: 0x6f0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x240
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x53d8
+  __DATA_CONST.__objc_selrefs: 0x54c8
   __DATA_CONST.__objc_protorefs: 0x138
-  __DATA_CONST.__objc_superrefs: 0x4c0
+  __DATA_CONST.__objc_superrefs: 0x4d0
   __DATA_CONST.__objc_arraydata: 0x260
-  __DATA_CONST.__got: 0xe90
-  __AUTH_CONST.__const: 0x3308
-  __AUTH_CONST.__cfstring: 0x97e0
-  __AUTH_CONST.__objc_const: 0x13178
-  __AUTH_CONST.__objc_intobj: 0x180
+  __DATA_CONST.__got: 0xed8
+  __AUTH_CONST.__const: 0x35f8
+  __AUTH_CONST.__cfstring: 0x9a80
+  __AUTH_CONST.__objc_const: 0x13588
+  __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0xf0
-  __AUTH_CONST.__auth_got: 0x1190
-  __AUTH.__objc_data: 0x31a8
+  __AUTH_CONST.__auth_got: 0x1328
+  __AUTH.__objc_data: 0x3248
   __AUTH.__data: 0x500
-  __DATA.__objc_ivar: 0x7bc
-  __DATA.__data: 0x21b0
+  __DATA.__objc_ivar: 0x7e0
+  __DATA.__data: 0x2200
   __DATA.__bss: 0x3f80
   __DATA.__common: 0xd0
-  __DATA_DIRTY.__objc_data: 0x1f18
+  __DATA_DIRTY.__objc_data: 0x1f40
   __DATA_DIRTY.__data: 0x278
   __DATA_DIRTY.__bss: 0x1c0
   __DATA_DIRTY.__common: 0x30

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5840
-  Symbols:   8650
-  CStrings:  2237
+  Functions: 5958
+  Symbols:   8752
+  CStrings:  2279
 
Symbols:
+ +[STCoreOrganizationSettings keyPathsForValuesAffectingContentPrivacyAccessibilityAskRestriction]
+ +[STCoreUser(UnmodeledInternal) keyPathsForValuesAffectingContentPrivacyAccessibilityAskRestriction]
+ +[STLocations migrationJournal]
+ +[STLocations migrationUpdatesJournal]
+ +[STMigrationDetailsCoreAnalyticsEvent description]
+ +[STMigrationStatusCoreAnalyticsEvent description]
+ -[STCoreOrganizationSettings contentPrivacyAccessibilityAskRestriction]
+ -[STCoreOrganizationSettings setContentPrivacyAccessibilityAskRestriction:]
+ -[STCoreUser(UnmodeledInternal) contentPrivacyAccessibilityAskRestriction]
+ -[STCoreUser(UnmodeledInternal) setContentPrivacyAccessibilityAskRestriction:]
+ -[STManagementState isEurekaEnabled]
+ -[STManagementState recordMigrationUpdateForAltDSID:update:completionHandler:]
+ -[STMigrationDetailsCoreAnalyticsEvent childAccounts]
+ -[STMigrationDetailsCoreAnalyticsEvent initWithChildAccounts:migrationOutcome:migrationSelection:migrationType:]
+ -[STMigrationDetailsCoreAnalyticsEvent migrationOutcome]
+ -[STMigrationDetailsCoreAnalyticsEvent migrationSelection]
+ -[STMigrationDetailsCoreAnalyticsEvent migrationType]
+ -[STMigrationDetailsCoreAnalyticsEvent name]
+ -[STMigrationDetailsCoreAnalyticsEvent payload]
+ -[STMigrationStatusCoreAnalyticsEvent familyAccountType]
+ -[STMigrationStatusCoreAnalyticsEvent familyAccount]
+ -[STMigrationStatusCoreAnalyticsEvent initWithFamilyAccount:familyAccountType:migrationEligible:migrationStatus:]
+ -[STMigrationStatusCoreAnalyticsEvent migrationEligible]
+ -[STMigrationStatusCoreAnalyticsEvent migrationStatus]
+ -[STMigrationStatusCoreAnalyticsEvent name]
+ -[STMigrationStatusCoreAnalyticsEvent payload]
+ -[STRegulatoryIntelligenceSiriPolicy allowedSiriVersionFooterHidden]
+ -[STRegulatoryIntelligenceSiriPolicy setAllowedSiriVersionFooterHidden:]
+ -[STRegulatoryIntelligenceSiriPolicy setSiriAIIsHidden:]
+ -[STRegulatoryIntelligenceSiriPolicy siriAIIsHidden]
+ GCC_except_table102
+ GCC_except_table126
+ GCC_except_table129
+ GCC_except_table132
+ GCC_except_table135
+ GCC_except_table147
+ GCC_except_table150
+ GCC_except_table197
+ GCC_except_table210
+ GCC_except_table213
+ GCC_except_table219
+ GCC_except_table50
+ GCC_except_table61
+ GCC_except_table71
+ _OBJC_CLASS_$_STMigrationDetailsCoreAnalyticsEvent
+ _OBJC_CLASS_$_STMigrationStatusCoreAnalyticsEvent
+ _OBJC_IVAR_$_STMigrationDetailsCoreAnalyticsEvent._childAccounts
+ _OBJC_IVAR_$_STMigrationDetailsCoreAnalyticsEvent._migrationOutcome
+ _OBJC_IVAR_$_STMigrationDetailsCoreAnalyticsEvent._migrationSelection
+ _OBJC_IVAR_$_STMigrationDetailsCoreAnalyticsEvent._migrationType
+ _OBJC_IVAR_$_STMigrationStatusCoreAnalyticsEvent._familyAccount
+ _OBJC_IVAR_$_STMigrationStatusCoreAnalyticsEvent._familyAccountType
+ _OBJC_IVAR_$_STMigrationStatusCoreAnalyticsEvent._migrationEligible
+ _OBJC_IVAR_$_STMigrationStatusCoreAnalyticsEvent._migrationStatus
+ _OBJC_IVAR_$_STRegulatoryIntelligenceSiriPolicy._allowedSiriVersionFooterHidden
+ _OBJC_IVAR_$_STRegulatoryIntelligenceSiriPolicy._siriAIIsHidden
+ _OBJC_METACLASS_$_STMigrationDetailsCoreAnalyticsEvent
+ _OBJC_METACLASS_$_STMigrationStatusCoreAnalyticsEvent
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_9
+ __OBJC_$_CLASS_METHODS_STMigrationDetailsCoreAnalyticsEvent
+ __OBJC_$_CLASS_METHODS_STMigrationStatusCoreAnalyticsEvent
+ __OBJC_$_INSTANCE_METHODS_STMigrationDetailsCoreAnalyticsEvent
+ __OBJC_$_INSTANCE_METHODS_STMigrationStatusCoreAnalyticsEvent
+ __OBJC_$_INSTANCE_VARIABLES_STMigrationDetailsCoreAnalyticsEvent
+ __OBJC_$_INSTANCE_VARIABLES_STMigrationStatusCoreAnalyticsEvent
+ __OBJC_$_PROP_LIST_STMigrationDetailsCoreAnalyticsEvent
+ __OBJC_$_PROP_LIST_STMigrationStatusCoreAnalyticsEvent
+ __OBJC_CLASS_PROTOCOLS_$_STMigrationDetailsCoreAnalyticsEvent
+ __OBJC_CLASS_PROTOCOLS_$_STMigrationStatusCoreAnalyticsEvent
+ __OBJC_CLASS_RO_$_STMigrationDetailsCoreAnalyticsEvent
+ __OBJC_CLASS_RO_$_STMigrationStatusCoreAnalyticsEvent
+ __OBJC_METACLASS_RO_$_STMigrationDetailsCoreAnalyticsEvent
+ __OBJC_METACLASS_RO_$_STMigrationStatusCoreAnalyticsEvent
+ ___78-[STManagementState recordMigrationUpdateForAltDSID:update:completionHandler:]_block_invoke
+ ___78-[STManagementState recordMigrationUpdateForAltDSID:update:completionHandler:]_block_invoke_2
+ ___79-[STManagementState saveExpressIntroductionSettingsDefaults:completionHandler:]_block_invoke_3
+ ___83-[STManagementState isLocationSharingModificationAllowedForDSID:completionHandler:]_block_invoke_3
+ ___85-[STManagementState setLocationSharingModificationAllowed:forDSID:completionHandler:]_block_invoke_3
+ ___block_descriptor_57_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_58_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s40l8s48l8
+ ___swift_closure_destructor.129Tm
+ ___swift_closure_destructor.32Tm
+ ___swift_closure_destructor.36Tm
+ _objc_msgSend$URLByAppendingPathComponent:
+ _objc_msgSend$allowChangesToShareMyLocationForDSID:completion:
+ _objc_msgSend$applyExpressIntroductionSettingsDefaults:error:
+ _objc_msgSend$childAccounts
+ _objc_msgSend$communicationSafetyHasStrictPolicy
+ _objc_msgSend$communicationSafetyIsEnabled
+ _objc_msgSend$contentPrivacyAccessibilityAskRestriction
+ _objc_msgSend$contentRestrictionsHasStrictPolicy
+ _objc_msgSend$contentRestrictionsIsEnabled
+ _objc_msgSend$contentRestrictionsValueByKey
+ _objc_msgSend$familyAccount
+ _objc_msgSend$familyAccountType
+ _objc_msgSend$isEurekaEnabled
+ _objc_msgSend$migrationEligible
+ _objc_msgSend$migrationOutcome
+ _objc_msgSend$migrationSelection
+ _objc_msgSend$migrationStatus
+ _objc_msgSend$migrationType
+ _objc_msgSend$recordMigrationUpdateForAltDSID:update:completionHandler:
+ _objc_msgSend$restrictionsImmutableCopy
+ _objc_msgSend$restrictionsWithIsEnabled:valueByAgePresetKey:
+ _objc_msgSend$screenDistanceHasStrictPolicy
+ _objc_msgSend$screenDistanceIsEnabled
+ _objc_msgSend$setAllowChangesToShareMyLocation:forDSID:completion:
+ _objc_msgSend$setAllowedSiriVersionFooterHidden:
+ _objc_msgSend$setCommunicationSafetyEnabled:error:
+ _objc_msgSend$setContentPrivacyAccessibilityAskRestriction:
+ _objc_msgSend$setSiriAIIsHidden:
+ _objc_msgSend$setWebFilterState:error:
+ _symbolic $s14ScreenTimeCore019ExpressIntroductionaB16SettingsApplyingP
+ _symbolic _____ 14ScreenTimeCore0aB30SettingsRestrictionsTranslatorO
+ _symbolic _____ 14ScreenTimeCore0aB32SettingsServiceClientTranslationO
+ _symbolic _____ 14ScreenTimeCore37ExpressIntroductionSettingsTranslatorO
+ _symbolic _____Sg 26ScreenTimeSettingsServices0abC0C14WebPermissionsV19BrowserFilterPolicyO
+ _symbolic _____Sg 26ScreenTimeSettingsServices0abC0C16PermissionPolicyO
+ _symbolic _____Sg 26ScreenTimeSettingsServices0abC0C19ContentRestrictionsV08ExplicitE6PolicyO
+ _symbolic _____Sg 26ScreenTimeSettingsServices0abC0C19ContentRestrictionsV16EnablementPolicyO
+ _symbolic _____Sg 26ScreenTimeSettingsServices0abC0C19ContentRestrictionsV17RatingRestrictionV
+ _symbolic _____Sg 26ScreenTimeSettingsServices0abC0C9WebDomainV
- -[STCoreUser .cxx_destruct]
- GCC_except_table100
- GCC_except_table124
- GCC_except_table127
- GCC_except_table130
- GCC_except_table133
- GCC_except_table142
- GCC_except_table145
- GCC_except_table188
- GCC_except_table191
- GCC_except_table203
- GCC_except_table209
- GCC_except_table49
- GCC_except_table60
- GCC_except_table66
- _OBJC_IVAR_$_STCoreUser._familyMemberType
- __OBJC_$_INSTANCE_VARIABLES_STCoreUser
- ___60-[STManagementState setScreenTimeEnabled:completionHandler:]_block_invoke_3
- ___swift_closure_destructor.26Tm
- ___swift_closure_destructor.30Tm
- _symbolic _____Sg 10Foundation3URLV
CStrings:
+ "%s: Applying Express Introduction defaults to New Screen Time"
+ "%s: Unknown STWebFilterState %lu, falling back to the most-restrictive askToBrowse"
+ "%s: autoFilterEdited mapped to safeBrowsing (plain Limit Adult Websites); this enum-only SPI carries no list data, so any existing allow/block lists are left unchanged"
+ "%s: could not resolve web domain, failing open"
+ "Accessibility Ask: STOrganizationSettingsRestrictionUtility (inContext) returning isAllowed = %{bool}d"
+ "Accessibility Ask: STOrganizationSettingsRestrictionUtility returning isAllowed = %{bool}d"
+ "Accessibility Ask: STOrganizationSettingsRestrictionUtility saved isAllowed = %{bool}d"
+ "Accessibility Ask: unknown family age range; derived restriction value Allow"
+ "Accessibility Ask: user is adult in family; derived restriction value Allow"
+ "Accessibility Ask: user is child (U13) in family; derived restriction value DontAllow"
+ "Accessibility Ask: user is not in a family; derived restriction value Allow"
+ "Accessibility Ask: user is teen (U18) in family; derived restriction value DontAllow"
+ "Best-effort %{public}s stack write failed during setScreenTimeEnabled double-write: %{public}@"
+ "Could not resolve web domain for identifier: %{private}s"
+ "Invalid Accessibility Ask restriction value found in UserDefaults; returning Allow"
+ "MigrationDetails"
+ "MigrationJournal.jsonl"
+ "MigrationStatus"
+ "MigrationUpdatesJournal.jsonl"
+ "STAutomaticAccessibilityAskSetKey_"
+ "applyExpressIntroductionSettingsDefaults(_:)"
+ "browserFilterPolicy(for:)"
+ "childAccounts"
+ "childAccountsModified"
+ "childAccountsReviewed"
+ "cloudSettings.contentPrivacyAccessibilityAskRestriction"
+ "com.apple.ScreenTime.MigrationDetails"
+ "com.apple.ScreenTime.MigrationStatus"
+ "contentPrivacyAccessibilityAskRestriction"
+ "eureka_server_ramp"
+ "familyAccount"
+ "familyAccountType"
+ "familySettings.contentPrivacyAccessibilityAskRestriction"
+ "legacy"
+ "localSettings.contentPrivacyAccessibilityAskRestriction"
+ "migrationEligible"
+ "migrationOutcome"
+ "migrationSelection"
+ "migrationStatus"
+ "migrationType"
+ "new"
+ "setCommunicationSafetyEnabled(_:)"
+ "setWebFilterState(_:)"
+ "trackId"
- "%s: could not form URL for web domain, failing open"
- "Failed to create URL for domain: %{private}s"
```
