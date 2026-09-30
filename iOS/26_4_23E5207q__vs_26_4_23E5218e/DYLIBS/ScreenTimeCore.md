## ScreenTimeCore

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore`

```diff

-605.4.13.0.0
-  __TEXT.__text: 0xc2928
+605.4.16.0.0
+  __TEXT.__text: 0xc3d88
   __TEXT.__auth_stubs: 0x1630
-  __TEXT.__objc_methlist: 0x91b8
+  __TEXT.__objc_methlist: 0x92d8
   __TEXT.__const: 0x2410
-  __TEXT.__cstring: 0x9a5c
-  __TEXT.__oslogstring: 0x9d9f
+  __TEXT.__cstring: 0x9bcc
+  __TEXT.__oslogstring: 0x9faf
   __TEXT.__gcc_except_tab: 0x1c34
   __TEXT.__constg_swiftt: 0x8d0
   __TEXT.__swift5_typeref: 0xbb2

   __TEXT.__swift_as_ret: 0x64
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x3038
+  __TEXT.__unwind_info: 0x3068
   __TEXT.__eh_frame: 0x16e0
-  __TEXT.__objc_classname: 0x1e20
-  __TEXT.__objc_methname: 0x18bb0
-  __TEXT.__objc_methtype: 0x2af1
-  __TEXT.__objc_stubs: 0xdf60
-  __DATA_CONST.__got: 0xbe8
-  __DATA_CONST.__const: 0x1b68
-  __DATA_CONST.__objc_classlist: 0x650
+  __TEXT.__objc_classname: 0x1e50
+  __TEXT.__objc_methname: 0x18fd0
+  __TEXT.__objc_methtype: 0x2b21
+  __TEXT.__objc_stubs: 0xe0e0
+  __DATA_CONST.__got: 0xbf0
+  __DATA_CONST.__const: 0x1b60
+  __DATA_CONST.__objc_classlist: 0x658
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x1e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4e30
+  __DATA_CONST.__objc_selrefs: 0x4ec8
   __DATA_CONST.__objc_protorefs: 0x110
-  __DATA_CONST.__objc_superrefs: 0x498
+  __DATA_CONST.__objc_superrefs: 0x4a8
   __DATA_CONST.__objc_arraydata: 0x260
   __AUTH_CONST.__auth_got: 0xb28
-  __AUTH_CONST.__const: 0x1d70
-  __AUTH_CONST.__cfstring: 0x9120
-  __AUTH_CONST.__objc_const: 0x11778
+  __AUTH_CONST.__const: 0x1d50
+  __AUTH_CONST.__cfstring: 0x9320
+  __AUTH_CONST.__objc_const: 0x11918
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0xf0
-  __AUTH.__objc_data: 0x3348
+  __AUTH.__objc_data: 0x3398
   __AUTH.__data: 0x340
-  __DATA.__objc_ivar: 0x708
+  __DATA.__objc_ivar: 0x718
   __DATA.__data: 0x1b08
-  __DATA.__bss: 0x36e0
+  __DATA.__bss: 0x36d0
   __DATA.__common: 0x68
   __DATA_DIRTY.__objc_data: 0x1418
   __DATA_DIRTY.__data: 0xb8

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 97BA381B-8EF9-318C-88BD-15306A83A711
-  Functions: 4736
-  Symbols:   12491
-  CStrings:  7220
+  UUID: 424CA5D8-9186-3439-9A05-4726864522AA
+  Functions: 4765
+  Symbols:   12559
+  CStrings:  7287
 
Symbols:
+ +[STBlueprint appExceptionsDeclarationForUser:usingCache:]
+ +[STBlueprint appExceptionsDeclarationForUser:usingCache:].cold.1
+ +[STBlueprint appExceptionsDeclarationForUser:usingCache:].cold.2
+ +[STBlueprint appExceptionsDeclarationForUser:usingCache:].cold.3
+ +[STBlueprintConfiguration _recoverSiteWhiteListItemFromDictionary:]
+ +[STBlueprintConfiguration _recoverSiteWhiteListItemsFromArray:]
+ +[STBlueprintConfiguration logWebContentFilterDiagnostics:]
+ +[STBlueprintConfiguration logWebContentFilterDiagnostics:].cold.1
+ +[STBlueprintConfiguration logWebContentFilterDiagnostics:].cold.2
+ +[STCoreUser(UnmodeledProperties) keyPathsForValuesAffectingIsThirdPartyReplacingAppAndWebsiteActivity]
+ -[STBlueprintConfiguration _logSiteWhiteListStructureForRecovery:]
+ -[STBlueprintConfiguration _updatePayloadWithRecoveredConfiguration:]
+ -[STBlueprintConfiguration _updatePayloadWithRecoveredConfiguration:].cold.1
+ -[STBlueprintConfiguration attemptWebContentFilterRecovery]
+ -[STBlueprintConfiguration attemptWebContentFilterRecovery].cold.1
+ -[STBlueprintConfiguration attemptWebContentFilterRecovery].cold.2
+ -[STBlueprintConfiguration attemptWebContentFilterRecovery].cold.3
+ -[STCoreUser(UnmodeledInternal) setIsThirdPartyReplacingAppAndWebsiteActivity:]
+ -[STCoreUser(UnmodeledProperties) isThirdPartyReplacingAppAndWebsiteActivity]
+ -[STManagementState disableAppAndWebsiteActivityDueToThirdPartyAppWithCompletionHandler:]
+ -[STManagementState isAppAndWebsiteActivityEnabledWithCompletionHandler:]
+ -[STRegulatoryAllowedAppsPolicy appsRatingFooterInfo]
+ -[STRegulatoryAllowedAppsPolicy init]
+ -[STRegulatoryAllowedAppsPolicy setAppsRatingFooterInfo:]
+ -[STRegulatoryContentPrivacyRestrictionsPolicy .cxx_destruct]
+ -[STRegulatoryContentPrivacyRestrictionsPolicy guardianSignInReason]
+ -[STRegulatoryContentPrivacyRestrictionsPolicy init]
+ -[STRegulatoryContentPrivacyRestrictionsPolicy setGuardianSignInReason:]
+ -[STRegulatoryContentPrivacyRestrictionsPolicy setTopLevelRestrictionsForcedToEnabled:]
+ -[STRegulatoryContentPrivacyRestrictionsPolicy topLevelRestrictionsForcedToEnabled]
+ -[STRegulatoryPolicy contentRestrictions]
+ -[STRegulatoryPolicy setContentRestrictions:]
+ GCC_except_table102
+ GCC_except_table131
+ GCC_except_table134
+ GCC_except_table143
+ GCC_except_table152
+ GCC_except_table66
+ GCC_except_table99
+ _OBJC_CLASS_$_STRegulatoryContentPrivacyRestrictionsPolicy
+ _OBJC_IVAR_$_STRegulatoryAllowedAppsPolicy._appsRatingFooterInfo
+ _OBJC_IVAR_$_STRegulatoryContentPrivacyRestrictionsPolicy._guardianSignInReason
+ _OBJC_IVAR_$_STRegulatoryContentPrivacyRestrictionsPolicy._topLevelRestrictionsForcedToEnabled
+ _OBJC_IVAR_$_STRegulatoryPolicy._contentRestrictions
+ _OBJC_METACLASS_$_STRegulatoryContentPrivacyRestrictionsPolicy
+ __OBJC_$_INSTANCE_METHODS_STRegulatoryContentPrivacyRestrictionsPolicy
+ __OBJC_$_INSTANCE_VARIABLES_STRegulatoryContentPrivacyRestrictionsPolicy
+ __OBJC_$_PROP_LIST_STRegulatoryContentPrivacyRestrictionsPolicy
+ __OBJC_CLASS_RO_$_STRegulatoryContentPrivacyRestrictionsPolicy
+ __OBJC_METACLASS_RO_$_STRegulatoryContentPrivacyRestrictionsPolicy
+ ___73-[STManagementState isAppAndWebsiteActivityEnabledWithCompletionHandler:]_block_invoke
+ ___73-[STManagementState isAppAndWebsiteActivityEnabledWithCompletionHandler:]_block_invoke_2
+ ___89-[STManagementState disableAppAndWebsiteActivityDueToThirdPartyAppWithCompletionHandler:]_block_invoke
+ ___89-[STManagementState disableAppAndWebsiteActivityDueToThirdPartyAppWithCompletionHandler:]_block_invoke_2
+ _objc_msgSend$_logSiteWhiteListStructureForRecovery:
+ _objc_msgSend$_recoverSiteWhiteListItemFromDictionary:
+ _objc_msgSend$_recoverSiteWhiteListItemsFromArray:
+ _objc_msgSend$_updatePayloadWithRecoveredConfiguration:
+ _objc_msgSend$buildWithIdentifier:withRestrictWeb:withUseContentFilter:withWhiteListEnabled:withSiteWhiteList:withFilterWhiteList:withFilterBlackList:
+ _objc_msgSend$disableAppAndWebsiteActivityDueToThirdPartyAppWithCompletionHandler:
+ _objc_msgSend$isAppAndWebsiteActivityEnabledWithCompletionHandler:
+ _objc_msgSend$isThirdPartyReplacingAppAndWebsiteActivity
+ _objc_msgSend$loadPayload:error:
+ _objc_msgSend$logWebContentFilterDiagnostics:
+ _objc_msgSend$setAppsRatingFooterInfo:
+ _objc_msgSend$setContentRestrictions:
+ _objc_msgSend$setIsThirdPartyReplacingAppAndWebsiteActivity:
- +[STBlueprint _buildConfigurationsByDeclarationIdentifierFromBlueprint:error:].cold.3
- +[STBlueprint _buildConfigurationsByDeclarationIdentifierFromBlueprint:error:].cold.4
- +[STBlueprint appExceptionsDeclarationForBlueprint:usingCache:]
- +[STBlueprint appExceptionsDeclarationForBlueprint:usingCache:].cold.1
- +[STBlueprint appExceptionsDeclarationForBlueprint:usingCache:].cold.2
- +[STBlueprint appExceptionsDeclarationForBlueprint:usingCache:].cold.3
- +[STBlueprint appExceptionsDeclarationForBlueprint:usingCache:].cold.4
- GCC_except_table125
- GCC_except_table128
- GCC_except_table137
- GCC_except_table140
- _OUTLINED_FUNCTION_13
- ___78+[STBlueprint _buildConfigurationsByDeclarationIdentifierFromBlueprint:error:]_block_invoke
- ___78+[STBlueprint _buildConfigurationsByDeclarationIdentifierFromBlueprint:error:]_block_invoke.cold.1
- __buildConfigurationsByDeclarationIdentifierFromBlueprint:error:.exceptionsDeclarationCache
- __buildConfigurationsByDeclarationIdentifierFromBlueprint:error:.onceToken
- __swift_FORCE_LOAD_$_swiftCoreImage
- __swift_FORCE_LOAD_$_swiftCoreImage_$_ScreenTimeCore
- _objc_msgSend$appExceptionsDeclarationForBlueprint:usingCache:
CStrings:
+ "@\"STRegulatoryContentPrivacyRestrictionsPolicy\""
+ "Address"
+ "PageTitle"
+ "Payload"
+ "STRegulatoryContentPrivacyRestrictionsPolicy"
+ "Successfully recovered webcontentfilter configuration"
+ "T@\"STRegulatoryContentPrivacyRestrictionsPolicy\",&,V_contentRestrictions"
+ "T@\"STUIPolicyMessageInfo\",&,V_appsRatingFooterInfo"
+ "TB,V_topLevelRestrictionsForcedToEnabled"
+ "_appsRatingFooterInfo"
+ "_contentRestrictions"
+ "_logSiteWhiteListStructureForRecovery:"
+ "_recoverSiteWhiteListItemFromDictionary:"
+ "_recoverSiteWhiteListItemsFromArray:"
+ "_topLevelRestrictionsForcedToEnabled"
+ "_updatePayloadWithRecoveredConfiguration:"
+ "appExceptionsDeclarationForUser:usingCache:"
+ "appsRatingFooterInfo"
+ "attemptWebContentFilterRecovery"
+ "buildWithIdentifier:withRestrictWeb:withUseContentFilter:withWhiteListEnabled:withSiteWhiteList:withFilterWhiteList:withFilterBlackList:"
+ "cloudSettings.isThirdPartyReplacingAppAndWebsiteActivity"
+ "contentRestrictions"
+ "disableAppAndWebsiteActivityDueToThirdPartyAppWithCompletionHandler:"
+ "familySettings.isThirdPartyReplacingAppAndWebsiteActivity"
+ "filterBlackList"
+ "filterWhiteList"
+ "isAppAndWebsiteActivityEnabledWithCompletionHandler:"
+ "isThirdPartyReplacingAppAndWebsiteActivity"
+ "keyPathsForValuesAffectingIsThirdPartyReplacingAppAndWebsiteActivity"
+ "loadPayload:error:"
+ "localSettings.isThirdPartyReplacingAppAndWebsiteActivity"
+ "logWebContentFilterDiagnostics:"
+ "pageTitle"
+ "payloadAddress"
+ "payloadPageTitle"
+ "restrictWeb"
+ "setAppsRatingFooterInfo:"
+ "setContentRestrictions:"
+ "setIsThirdPartyReplacingAppAndWebsiteActivity:"
+ "setTopLevelRestrictionsForcedToEnabled:"
+ "siteWhiteList"
+ "topLevelRestrictionsForcedToEnabled"
+ "useContentFilter"
+ "webcontentfilter recovery: failed to build recovered configuration"
+ "webcontentfilter recovery: failed to parse plist: %{public}@"
+ "webcontentfilter recovery: failed to serialize recovered config: %{public}@"
+ "webcontentfilter recovery: no Payload in plist"
+ "webcontentfilter recovery: recovered %lu of %lu siteWhiteList items"
+ "webcontentfilter recovery: siteWhiteList class=%{public}@, count=%lu"
+ "webcontentfilter recovery: siteWhiteList[0] class=%{public}@"
+ "webcontentfilter recovery: siteWhiteList[0] class=%{public}@, keys=%{public}@"
+ "webcontentfilter recovery: updated payload with recovered configuration"
+ "webcontentfilter serialization diagnostic: siteWhiteList class=%{public}@, count=%lu"
+ "webcontentfilter serialization diagnostic: siteWhiteList[0] class=%{public}@"
+ "whiteListEnabled"
- "CEMSystemAppExceptionsDeclaration is in blueprint configurations already. This is not expected:%@"
- "Creating app exceptions cache. Did ScreenTimeAgent restart?"
- "Not a restriction blueprint. CEMSystemAppExceptionsDeclaration won't be included."
- "Processing app exceptions for restriction blueprint %@"
- "appExceptionsDeclarationForBlueprint:usingCache:"

```
