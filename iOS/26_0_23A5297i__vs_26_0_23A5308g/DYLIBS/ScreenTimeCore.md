## ScreenTimeCore

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore`

```diff

-591.100.0.0.0
-  __TEXT.__text: 0xb5ee0
+601.0.0.0.0
+  __TEXT.__text: 0xb61d0
   __TEXT.__auth_stubs: 0x1570
-  __TEXT.__objc_methlist: 0x8770
-  __TEXT.__const: 0x1dd0
-  __TEXT.__cstring: 0xa138
-  __TEXT.__oslogstring: 0x9a9c
-  __TEXT.__gcc_except_tab: 0x1ce0
+  __TEXT.__objc_methlist: 0x8858
+  __TEXT.__const: 0x1df0
+  __TEXT.__cstring: 0xa318
+  __TEXT.__oslogstring: 0x9bac
+  __TEXT.__gcc_except_tab: 0x1d00
   __TEXT.__constg_swiftt: 0x844
   __TEXT.__swift5_typeref: 0xa52
   __TEXT.__swift5_builtin: 0x78

   __TEXT.__swift_as_ret: 0x18
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x2b98
+  __TEXT.__unwind_info: 0x2bb8
   __TEXT.__eh_frame: 0xcf8
-  __TEXT.__objc_classname: 0x182a
-  __TEXT.__objc_methname: 0x16331
-  __TEXT.__objc_methtype: 0x2407
-  __TEXT.__objc_stubs: 0xd460
-  __DATA_CONST.__got: 0xb48
-  __DATA_CONST.__const: 0x1a00
+  __TEXT.__objc_classname: 0x1835
+  __TEXT.__objc_methname: 0x164f3
+  __TEXT.__objc_methtype: 0x23ff
+  __TEXT.__objc_stubs: 0xd580
+  __DATA_CONST.__got: 0xb50
+  __DATA_CONST.__const: 0x1a50
   __DATA_CONST.__objc_classlist: 0x5e0
-  __DATA_CONST.__objc_catlist: 0x18
+  __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x1d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4930
+  __DATA_CONST.__objc_selrefs: 0x4978
   __DATA_CONST.__objc_protorefs: 0x108
   __DATA_CONST.__objc_superrefs: 0x458
   __DATA_CONST.__objc_arraydata: 0x250
   __AUTH_CONST.__auth_got: 0xac8
-  __AUTH_CONST.__const: 0x1718
-  __AUTH_CONST.__cfstring: 0x88c0
-  __AUTH_CONST.__objc_const: 0xff68
-  __AUTH_CONST.__objc_intobj: 0x168
+  __AUTH_CONST.__const: 0x1770
+  __AUTH_CONST.__cfstring: 0x8940
+  __AUTH_CONST.__objc_const: 0x10070
+  __AUTH_CONST.__objc_intobj: 0x138
+  __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH.__objc_data: 0x2fb8
+  __AUTH.__objc_data: 0x2f68
   __AUTH.__data: 0x260
   __DATA.__objc_ivar: 0x600
   __DATA.__data: 0x1aa8
   __DATA.__bss: 0x33b0
   __DATA.__common: 0x68
-  __DATA_DIRTY.__objc_data: 0x1378
+  __DATA_DIRTY.__objc_data: 0x13c8
   __DATA_DIRTY.__data: 0x48
   __DATA_DIRTY.__bss: 0xc8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: ED73D615-FF5B-35CA-AD8F-7B3499285A95
-  Functions: 4396
-  Symbols:   11625
-  CStrings:  6819
+  UUID: 0F2723D8-91A3-3533-8280-7942AEF185D0
+  Functions: 4419
+  Symbols:   11703
+  CStrings:  6849
 
Symbols:
+ +[STBlueprint _buildConfigurationsByDeclarationIdentifierFromBlueprint:error:].cold.3
+ +[STBlueprint _buildConfigurationsByDeclarationIdentifierFromBlueprint:error:].cold.4
+ +[STBlueprint appExceptionsDeclarationForUser:allowedAppsRating:]
+ +[STBlueprint appExceptionsDeclarationForUser:allowedAppsRating:].cold.1
+ +[STBlueprint fetchRequestForBlueprintsOfType:]
+ +[STBlueprint fetchRequestMatchingUnexpiredOneMoreMinuteBlueprintsForUserWithDSID:]
+ +[STLog appExceptions]
+ +[STRestrictionsFetcher _fetchImageCreationStateForUserDSID:organizationSettingsRestrictionUtility:completionHandler:]
+ +[STRestrictionsFetcher _fetchRestrictionsForUserDSID:inManagedObjectContext:allowImageCreation:withError:]
+ +[STRestrictionsFetcher _fetchRestrictionsForUserDSID:inManagedObjectContext:allowImageCreation:withError:].cold.1
+ +[STRestrictionsFetcher _fetchRestrictionsForUserDSID:inManagedObjectContext:allowImageCreation:withError:].cold.2
+ +[STRestrictionsFetcher _fetchRestrictionsForUserDSID:inManagedObjectContext:allowImageCreation:withError:].cold.3
+ +[STRestrictionsFetcher fetchRestrictionsForUserDSID:persistenceController:completionHandler:]
+ +[STRestrictionsFetcher fetchRestrictionsForUserDSID:persistenceController:organizationSettingsRestrictionUtility:completionHandler:]
+ -[CEMConfigurationBase(ScreenTime) st_containsBundleIdentifier:]
+ -[CEMConfigurationBase(ScreenTime) st_containsCategoryIdentifer:]
+ -[CEMConfigurationBase(ScreenTime) st_containsWebDomain:]
+ -[CEMPolicyAppDeclaration(ScreenTime) st_containsBundleIdentifier:]
+ -[CEMPolicyAppDeclaration(ScreenTime) st_containsCategoryIdentifer:]
+ -[CEMPolicyAppDeclaration(ScreenTime) st_containsWebDomain:]
+ -[CEMPolicyCategoryDeclaration(ScreenTime) st_containsBundleIdentifier:]
+ -[CEMPolicyCategoryDeclaration(ScreenTime) st_containsCategoryIdentifer:]
+ -[CEMPolicyCategoryDeclaration(ScreenTime) st_containsWebDomain:]
+ -[CEMPolicyWebSiteDeclaration(ScreenTime) st_containsBundleIdentifier:]
+ -[CEMPolicyWebSiteDeclaration(ScreenTime) st_containsCategoryIdentifer:]
+ -[CEMPolicyWebSiteDeclaration(ScreenTime) st_containsWebDomain:]
+ _OBJC_CLASS_$_CEMSystemAppExceptionsDeclaration
+ _OBJC_CLASS_$_NSConstantDoubleNumber
+ _STAskForTimeRequestFifteenMinuteInterval
+ _STAskForTimeRequestOneHourInterval
+ _STAskForTimeRequestOneMinuteInterval
+ _STAskForTimeRequestRestOfDayInterval
+ __OBJC_$_CATEGORY_CEMConfigurationBase_$_ScreenTime
+ __OBJC_$_CATEGORY_CEMPolicyAppDeclaration_$_ScreenTime
+ __OBJC_$_CATEGORY_CEMPolicyCategoryDeclaration_$_ScreenTime
+ __OBJC_$_CATEGORY_CEMPolicyWebSiteDeclaration_$_ScreenTime
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_CEMConfigurationBase_$_ScreenTime
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_CEMPolicyAppDeclaration_$_ScreenTime
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_CEMPolicyCategoryDeclaration_$_ScreenTime
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_CEMPolicyWebSiteDeclaration_$_ScreenTime
+ ___118+[STRestrictionsFetcher _fetchImageCreationStateForUserDSID:organizationSettingsRestrictionUtility:completionHandler:]_block_invoke
+ ___133+[STRestrictionsFetcher fetchRestrictionsForUserDSID:persistenceController:organizationSettingsRestrictionUtility:completionHandler:]_block_invoke
+ ___133+[STRestrictionsFetcher fetchRestrictionsForUserDSID:persistenceController:organizationSettingsRestrictionUtility:completionHandler:]_block_invoke.2
+ ___block_descriptor_64_e8_32s40s48bs_e20_v24?0q8"NSError"16ls48l8s32l8s40l8
+ ___block_descriptor_80_e8_32s40s48r56r_e5_v8?0lr48l8s32l8s40l8r56l8
+ ___swift_memcpy8_8
+ _objc_msgSend$_fetchImageCreationStateForUserDSID:organizationSettingsRestrictionUtility:completionHandler:
+ _objc_msgSend$_fetchRestrictionsForUserDSID:inManagedObjectContext:allowImageCreation:withError:
+ _objc_msgSend$appExceptionsDeclarationForUser:allowedAppsRating:
+ _objc_msgSend$blueprintConfigurationTypeForDeclaration:
+ _objc_msgSend$buildWithIdentifier:appsRatingExemptedBundleIDs:
+ _objc_msgSend$fetchRestrictionsForUserDSID:persistenceController:organizationSettingsRestrictionUtility:completionHandler:
+ _objc_msgSend$initWithPersistenceController:restrictionPayloadUtility:
+ _objc_msgSend$isImageGenerationAllowedForUserDSID:completionHandler:
+ _objc_msgSend$payloadHostnames
+ _objc_msgSend$unknownPayloadKeys
- +[STBlueprint fetchRequestMatchingUnexpiredOneMoreMinuteBlueprints]
- +[STRestrictionsFetcher fetchRestrictionsForUserDSID:inManagedObjectContext:withError:]
- +[STRestrictionsFetcher fetchRestrictionsForUserDSID:inManagedObjectContext:withError:].cold.1
- +[STRestrictionsFetcher fetchRestrictionsForUserDSID:inManagedObjectContext:withError:].cold.2
- +[STRestrictionsFetcher fetchRestrictionsForUserDSID:inManagedObjectContext:withError:].cold.3
- _objc_msgSend$setPayloadAppsRatingExemptedBundleIDs:
CStrings:
+ "%K == %@ AND %K == NO"
+ "(ANY %K == %@) AND (%K BEGINSWITH %@) AND (%K >= %@)"
+ "-[CEMConfigurationBase(ScreenTime) st_containsBundleIdentifier:]"
+ "-[CEMConfigurationBase(ScreenTime) st_containsCategoryIdentifer:]"
+ "-[CEMConfigurationBase(ScreenTime) st_containsWebDomain:]"
+ "?"
+ "@\"_TtC14ScreenTimeCore13AlwaysAllowed\""
+ "@\"_TtC14ScreenTimeCore8Downtime\""
+ "@\"_TtC14ScreenTimeCore8Schedule\""
+ "@48@0:8@16@24q32^@40"
+ "CEMConfigurationBase+ScreenTime.m"
+ "CEMSystemAppExceptionsDeclaration created with bundle ids:%{private}@"
+ "Cannot create app exceptions declaration. Invalid user."
+ "Found deprecated appsRatingExemptedBundleIDs key in CEMRatingsDeclaration payload. Bug in migration logic"
+ "Processing system rating declaration"
+ "_fetchImageCreationStateForUserDSID:organizationSettingsRestrictionUtility:completionHandler:"
+ "_fetchRestrictionsForUserDSID:inManagedObjectContext:allowImageCreation:withError:"
+ "appExceptionsDeclarationForUser:allowedAppsRating:"
+ "appsRatingExemptedBundleIDs"
+ "buildWithIdentifier:appsRatingExemptedBundleIDs:"
+ "cannot directly call on CEMConfigurationBase"
+ "fetchRequestForBlueprintsOfType:"
+ "fetchRequestMatchingUnexpiredOneMoreMinuteBlueprintsForUserWithDSID:"
+ "fetchRestrictionsForUserDSID:persistenceController:completionHandler:"
+ "fetchRestrictionsForUserDSID:persistenceController:organizationSettingsRestrictionUtility:completionHandler:"
+ "payloadHostnames"
+ "st_containsBundleIdentifier:"
+ "st_containsCategoryIdentifer:"
+ "st_containsWebDomain:"
+ "unknownPayloadKeys"
- "(%K BEGINSWITH %@) AND (%K >= %@)"
- ".system.webcontentfilter.basic"
- "@\"NSArray\"24@0:8@\"NSArray\"16"
- "buildUpdatedDeclarationsRemovingWebContentFilterAutoFromDeclarations:"
- "fetchRequestMatchingUnexpiredOneMoreMinuteBlueprints"
- "fetchRestrictionsForUserDSID:inManagedObjectContext:withError:"
- "setPayloadAppsRatingExemptedBundleIDs:"

```
