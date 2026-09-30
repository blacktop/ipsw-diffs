## ScreenTimeCore

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore`

```diff

-605.1.8.0.0
-  __TEXT.__text: 0xba940
+605.1.15.100.0
+  __TEXT.__text: 0xbb68c
   __TEXT.__auth_stubs: 0x1660
-  __TEXT.__objc_methlist: 0x8ba8
-  __TEXT.__const: 0x2028
-  __TEXT.__cstring: 0xa6a8
-  __TEXT.__oslogstring: 0x9a2f
-  __TEXT.__gcc_except_tab: 0x1b90
+  __TEXT.__objc_methlist: 0x8be0
+  __TEXT.__const: 0x2038
+  __TEXT.__cstring: 0xa718
+  __TEXT.__oslogstring: 0x9c9f
+  __TEXT.__gcc_except_tab: 0x1be4
   __TEXT.__constg_swiftt: 0x8b4
   __TEXT.__swift5_typeref: 0xba4
   __TEXT.__swift5_builtin: 0x78

   __TEXT.__swift_as_ret: 0x64
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x2e48
+  __TEXT.__unwind_info: 0x2e88
   __TEXT.__eh_frame: 0x1628
   __TEXT.__objc_classname: 0x18d3
-  __TEXT.__objc_methname: 0x16ef6
+  __TEXT.__objc_methname: 0x16fee
   __TEXT.__objc_methtype: 0x24f8
-  __TEXT.__objc_stubs: 0xd5c0
+  __TEXT.__objc_stubs: 0xd640
   __DATA_CONST.__got: 0xbc8
-  __DATA_CONST.__const: 0x1b38
+  __DATA_CONST.__const: 0x1b68
   __DATA_CONST.__objc_classlist: 0x610
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x1e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4b98
+  __DATA_CONST.__objc_selrefs: 0x4bc0
   __DATA_CONST.__objc_protorefs: 0x110
   __DATA_CONST.__objc_superrefs: 0x470
   __DATA_CONST.__objc_arraydata: 0x260
   __AUTH_CONST.__auth_got: 0xb40
-  __AUTH_CONST.__const: 0x1cc0
+  __AUTH_CONST.__const: 0x1ce0
   __AUTH_CONST.__cfstring: 0x8ce0
-  __AUTH_CONST.__objc_const: 0x10640
+  __AUTH_CONST.__objc_const: 0x10648
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0xf0
-  __AUTH.__objc_data: 0x3118
+  __AUTH.__objc_data: 0x30c8
   __AUTH.__data: 0x340
   __DATA.__objc_ivar: 0x620
   __DATA.__data: 0x1b98
-  __DATA.__bss: 0x3550
+  __DATA.__bss: 0x3560
   __DATA.__common: 0x68
-  __DATA_DIRTY.__objc_data: 0x13c8
-  __DATA_DIRTY.__data: 0x48
+  __DATA_DIRTY.__objc_data: 0x1418
+  __DATA_DIRTY.__data: 0x50
   __DATA_DIRTY.__bss: 0xc8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FA689B80-799F-3BA3-AC60-378C2BE014EF
-  Functions: 4584
-  Symbols:   11880
-  CStrings:  7001
+  UUID: 5501F716-A7FE-3A9F-A76C-5901A0453B00
+  Functions: 4595
+  Symbols:   11914
+  CStrings:  7019
 
Symbols:
+ +[STBlueprint appExceptionsDeclarationForBlueprint:usingCache:]
+ +[STBlueprint appExceptionsDeclarationForBlueprint:usingCache:].cold.1
+ +[STBlueprint appExceptionsDeclarationForBlueprint:usingCache:].cold.2
+ +[STBlueprint appExceptionsDeclarationForBlueprint:usingCache:].cold.3
+ +[STBlueprint appExceptionsDeclarationForBlueprint:usingCache:].cold.4
+ -[STExceptionApp description]
+ -[STFamilyOrganizationSettings updateAppExceptionsWithDictionaryRepresentationsIfNeeded:]
+ -[STManagementState isCommunicationSafetyEnabledForUserDSID:error:]
+ -[STManagementState restrictionsForUserDSID:error:]
+ GCC_except_table122
+ GCC_except_table125
+ GCC_except_table134
+ GCC_except_table140
+ ___133+[STRestrictionsFetcher fetchRestrictionsForUserDSID:persistenceController:organizationSettingsRestrictionUtility:completionHandler:]_block_invoke.3
+ ___51-[STManagementState restrictionsForUserDSID:error:]_block_invoke
+ ___51-[STManagementState restrictionsForUserDSID:error:]_block_invoke_2
+ ___67-[STManagementState isCommunicationSafetyEnabledForUserDSID:error:]_block_invoke
+ ___67-[STManagementState isCommunicationSafetyEnabledForUserDSID:error:]_block_invoke_2
+ ___78+[STBlueprint _buildConfigurationsByDeclarationIdentifierFromBlueprint:error:]_block_invoke
+ ___78+[STBlueprint _buildConfigurationsByDeclarationIdentifierFromBlueprint:error:]_block_invoke.cold.1
+ ___block_descriptor_48_e8_32r40r_e36_v24?0"STRestrictions"8"NSError"16lr32l8r40l8
+ ___block_descriptor_72_e8_32s40s48bs_e20_v24?0q8"NSError"16ls48l8s32l8s40l8
+ __buildConfigurationsByDeclarationIdentifierFromBlueprint:error:.exceptionsDeclarationCache
+ __buildConfigurationsByDeclarationIdentifierFromBlueprint:error:.onceToken
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_ScreenTimeCore
+ _objc_msgSend$appExceptionsDeclarationForBlueprint:usingCache:
+ _objc_msgSend$declarationForPayload:error:
+ _objc_msgSend$isCommunicationSafetyEnabledForUserDSID:completionHandler:
+ _objc_msgSend$payloadAppsRatingExemptedBundleIDs
+ _objc_msgSend$setPayloadAppsRatingExemptedBundleIDs:
+ _objc_msgSend$updateAppExceptionsWithDictionaryRepresentationsIfNeeded:
- +[STBlueprint appExceptionsDeclarationForUser:allowedAppsRating:]
- +[STBlueprint appExceptionsDeclarationForUser:allowedAppsRating:].cold.1
- -[STManagementState restrictionsForUserDSID:completionHandler:]
- GCC_except_table130
- GCC_except_table136
- ___133+[STRestrictionsFetcher fetchRestrictionsForUserDSID:persistenceController:organizationSettingsRestrictionUtility:completionHandler:]_block_invoke.2
- ___63-[STManagementState restrictionsForUserDSID:completionHandler:]_block_invoke
- ___block_descriptor_64_e8_32s40s48bs_e20_v24?0q8"NSError"16ls48l8s32l8s40l8
- _objc_msgSend$appExceptionsDeclarationForUser:allowedAppsRating:
- _objc_msgSend$unknownPayloadKeys
CStrings:
+ "-[STFamilyOrganizationSettings updateAppExceptionsWithDictionaryRepresentationsIfNeeded:]"
+ "CEMSystemAppExceptionsDeclaration is in blueprint configurations already. This is not expected:%@"
+ "Creating app exceptions cache. Did ScreenTimeAgent restart?"
+ "Declaration has same bundle IDs. Not updating"
+ "Duplicate exception bundle identifier found:%@"
+ "Failed creating declaration from payload:%@. Error:%@"
+ "Fetch Restrictions Image Creation"
+ "Fetch Restrictions Other"
+ "Fetched CEMSystemAppExceptionsDeclaration payload:%@"
+ "Found %@ app exceptions"
+ "No app exceptions found in family settings. Not modifying app exceptions"
+ "No stored CEMSystemAppExceptionsDeclaration. Storing with bundleIDs:%@"
+ "Not a restriction blueprint. CEMSystemAppExceptionsDeclaration won't be included."
+ "Persisting updated declaration with payload:%@"
+ "Processing app exceptions for restriction blueprint %@"
+ "STExceptionApp(bundleIdentifier:%@ distributorID:%@, adamID:%@, rating:%@)"
+ "Updating declaration's payloadAppsRatingExemptedBundleIDs and hash"
+ "appExceptionsDeclarationForBlueprint:usingCache:"
+ "isCommunicationSafetyEnabledForUserDSID:completionHandler:"
+ "isCommunicationSafetyEnabledForUserDSID:error:"
+ "payloadAppsRatingExemptedBundleIDs"
+ "restrictionsForUserDSID:error:"
+ "setPayloadAppsRatingExemptedBundleIDs:"
+ "updateAppExceptionsWithDictionaryRepresentationsIfNeeded:"
+ "v24@?0@\"STRestrictions\"8@\"NSError\"16"
- "-[STFamilyOrganizationSettings updateWithDictionaryRepresentation:]"
- "CEMSystemAppExceptionsDeclaration created with bundle ids:%{private}@"
- "Found deprecated appsRatingExemptedBundleIDs key in CEMRatingsDeclaration payload. Bug in migration logic"
- "Processing system rating declaration"
- "appExceptionsDeclarationForUser:allowedAppsRating:"
- "appsRatingExemptedBundleIDs"
- "unknownPayloadKeys"

```
