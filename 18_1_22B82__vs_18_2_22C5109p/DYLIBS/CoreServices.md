## CoreServices

> `/System/Library/Frameworks/CoreServices.framework/CoreServices`

```diff

-1355.4.0.0.0
-  __TEXT.__text: 0x18012c
+1367.1.0.0.0
+  __TEXT.__text: 0x18c800
   __TEXT.__auth_stubs: 0x3200
-  __TEXT.__objc_methlist: 0xaf08
+  __TEXT.__objc_methlist: 0xb070
   __TEXT.__const: 0x8f0
-  __TEXT.__cstring: 0x1ec47
-  __TEXT.__oslogstring: 0x11fe7
-  __TEXT.__gcc_except_tab: 0x21878
-  __TEXT.__ustring: 0x132
-  __TEXT.__unwind_info: 0x9b48
+  __TEXT.__cstring: 0x1fa77
+  __TEXT.__oslogstring: 0x1279f
+  __TEXT.__gcc_except_tab: 0x22c30
+  __TEXT.__ustring: 0x23c
+  __TEXT.__unwind_info: 0x9fe0
   __TEXT.__eh_frame: 0x60
-  __TEXT.__objc_classname: 0x1b1f
-  __TEXT.__objc_methname: 0x1ae99
-  __TEXT.__objc_methtype: 0x9f16
-  __TEXT.__objc_stubs: 0xec60
+  __TEXT.__objc_classname: 0x1b7a
+  __TEXT.__objc_methname: 0x1b2f9
+  __TEXT.__objc_methtype: 0xa90e
+  __TEXT.__objc_stubs: 0xef80
   __DATA_CONST.__got: 0x9e8
-  __DATA_CONST.__const: 0x6588
-  __DATA_CONST.__objc_classlist: 0x600
+  __DATA_CONST.__const: 0x6730
+  __DATA_CONST.__objc_classlist: 0x610
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5760
+  __DATA_CONST.__objc_selrefs: 0x5830
   __DATA_CONST.__objc_protorefs: 0x98
-  __DATA_CONST.__objc_superrefs: 0x4c0
-  __DATA_CONST.__objc_arraydata: 0x158
+  __DATA_CONST.__objc_superrefs: 0x4d0
+  __DATA_CONST.__objc_arraydata: 0x178
   __AUTH_CONST.__auth_got: 0x1918
   __AUTH_CONST.__auth_ptr: 0x48
-  __AUTH_CONST.__const: 0x2fb0
-  __AUTH_CONST.__cfstring: 0x15240
-  __AUTH_CONST.__objc_const: 0x12e30
-  __AUTH_CONST.__objc_intobj: 0x750
-  __AUTH_CONST.__objc_arrayobj: 0x78
+  __AUTH_CONST.__const: 0x3288
+  __AUTH_CONST.__cfstring: 0x15a60
+  __AUTH_CONST.__objc_const: 0x130a8
+  __AUTH_CONST.__objc_intobj: 0x780
+  __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH.__objc_data: 0x2580
-  __AUTH.__data: 0x318
-  __DATA.__objc_ivar: 0x9a0
+  __AUTH.__objc_data: 0x2620
+  __AUTH.__data: 0x320
+  __DATA.__objc_ivar: 0x9b0
   __DATA.__data: 0x1250
-  __DATA.__bss: 0xea0
+  __DATA.__bss: 0xed0
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x1680
   __DATA_DIRTY.__data: 0x98
   __DATA_DIRTY.__crash_info: 0x40
-  __DATA_DIRTY.__bss: 0x7d8
+  __DATA_DIRTY.__bss: 0x7d0
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 7645
-  Symbols:   9334
-  CStrings:  9905
+  Functions: 7831
+  Symbols:   9534
+  CStrings:  10074
 
Symbols:
+ _LSDefaultAppCategoryForMask
+ _LSDefaultAppCategoryGetFromName
+ _LSDefaultAppCategoryMaskForCategory
+ __LSSetContentTypeHandler
CStrings:
+ "\n\n[Apple Internal Engineering Note]\nFeature flags configuration indicates 135298349 is not complete. Therefore you will be brought to Settings instead of automatically kicking off the restore."
+ "+[LSApplicationRecord(Enumeration) displayOrderEnumeratorForViableDefaultAppsForCategory:options:]"
+ "+[LSApplicationRecord(Enumeration) enumeratorForViableDefaultAppsForCategory:options:]"
+ "-[LSApplicationWorkspace(DefaultApps) defaultApplicationForCategory:error:]"
+ "-[LSApplicationWorkspace(DefaultApps) setDefaultApplicationForCategory:toApplicationRecord:completionHandler:]_block_invoke"
+ "-[_LSDModifyClient performUpdateOfPersonasOfBundleIDs:toPersonaUniqueStrings:operationUUID:reply:]"
+ "-[_LSDModifyClient performUpdateOfPersonasOfBundleIDs:toPersonaUniqueStrings:operationUUID:reply:]_block_invoke"
+ "-[_LSDModifyClient setPreferredAppMarketplaces:completion:]"
+ "-[_LSDReadClient getHasEverChangedPreferredAppForCategory:completion:]"
+ "-[_LSDReadClient getPreferredAppMarketplacesWithCompletion:]"
+ ".safesave"
+ "@\"LSApplicationProxy\"16@?0@\"NSString\"8"
+ "@32@0:8Q16Q24"
+ "@32@0:8^{LSContext=@}16r^v24"
+ "@32@0:8^{LSContext=@}16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}24"
+ "@36@0:8@16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}28"
+ "@36@0:8^{LSContext=@}16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}28"
+ "@40@0:8^{LSContext=@}16I24I28r^{LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}32"
+ "@40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
+ "@40@0:8^{LSContext=@}16I24I28r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}32"
+ "@44@0:8B16^{LSContext=@}20I28I32r^{LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}36"
+ "@44@0:8B16^{LSContext=@}20I28I32r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}36"
+ "@44@0:8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20@28^@36"
+ "@44@0:8^{LSContext=@}16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}28^@36"
+ "@44@0:8^{LSContext=@}16I24r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}28^@36"
+ "@48@0:8^{LSContext=@}16Q24r^I32Q40"
+ "@52@0:8^{LSContext=@}16I24r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}28@36^@44"
+ "@64@0:8@16@24^{LSContext=@}32I40I44r^{LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}48^@56"
+ "APP_REMOVAL_PROMPT_DETAIL_APP_STORE_DELETED"
+ "APP_REMOVAL_PROMPT_DETAIL_APP_STORE_DELETED_SELF"
+ "AppStoreComponents"
+ "B24@0:8Q16"
+ "B24@?0@\"NSNumber\"8^B16"
+ "B28@?0@\"_LSDatabase\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20"
+ "B28@?0^{LSContext=@}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20"
+ "B36@0:8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20^{LSContext=@}28"
+ "B36@0:8I16r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}20@28"
+ "B40@0:8I16r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}20I28^{LSContext=@}32"
+ "B40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
+ "B52@0:8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20^{LSContext=@}28@36^@44"
+ "B60@0:8^@16^@24I32r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}36@44^@52"
+ "BOOL _LSServer_HasPreferenceEverBeenSetForDefaultAppCategory(LSDefaultAppCategory)"
+ "Bundle 0x%!l(MISSING)lx has an unsupported format, so it cannot be a default app."
+ "Bundle 0x%!l(MISSING)lx is a placeholder, so it cannot be a default app."
+ "Bundle 0x%!l(MISSING)lx is in an unsupported location, so it cannot be a default app."
+ "Bundle 0x%!l(MISSING)lx is not an application, so it cannot be a default app."
+ "Bundle unit %!l(MISSING)lx went missing after we just enumerated it!"
+ "C40@0:8^{LSContext=@}16I24I28r^{LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}32"
+ "C40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
+ "Can't change category %!l(MISSING)u!"
+ "Category %!l(MISSING)lu is out of range"
+ "Couldn't get answer for boron domain: %!@(MISSING)"
+ "Couldn't get answer for eligibility domain %!d(MISSING): %!@(MISSING)"
+ "Couldn't lookup unit %!l(MISSING)lx to find its localized name: %!@(MISSING)"
+ "Couldn't remove handler for %!@(MISSING): %!l(MISSING)d"
+ "Couldn't remove handler for subordinate claim %!@(MISSING): %!l(MISSING)d"
+ "Couldn't set handler for %!@(MISSING): %!l(MISSING)d"
+ "Default Apps Claim"
+ "DefaultAppCategorization"
+ "Done migrating preferences for default apps, made changes? %!{(MISSING)BOOL}d"
+ "Error"
+ "FBSOpenApplicationOptionKeyIsSensitiveURL"
+ "FirstParty"
+ "I40@0:8^{LSContext=@}16I24I28r^{LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}32"
+ "I40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
+ "I40@0:8^{LSContext=@}16I24I28r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}32"
+ "LSDefaultAppCategoryContactlessPayment"
+ "LSDefaultAppCategoryInvalid"
+ "LSDefaultAppCategoryMailClient"
+ "LSDefaultAppCategoryMessaging"
+ "LSDefaultAppCategoryPhoneCalls"
+ "LSDefaultAppCategoryWebBrowser"
+ "LSDefaultAppsCore.mm"
+ "LSEligibilityDeletionDomain"
+ "LSMarketplacesPreferences"
+ "Marketplaces"
+ "Migrating preferences for default apps"
+ "NSError * _Nullable _LSServer_LSMigratePreferencesForDefaultApps(LSContext * _Nonnull)"
+ "No known bundle for %!@(MISSING)"
+ "Not all persona updates were successful, but %!z(MISSING)u were, so arming save timer"
+ "OSStatus _LSServer_LSRemoveDefaultApp(LSDefaultAppCategory)"
+ "OSStatus _LSServer_LSSetDefaultAppByTypeIdentifier(LSDefaultAppCategory, NSString *__strong _Nonnull, LSVersionNumber)"
+ "Override allowed for content type %!{(MISSING)public}@"
+ "Override not allowed for content type %!{(MISSING)public}@"
+ "PreviouslySetCategories"
+ "Q40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
+ "RESTORE_APP_BUTTON"
+ "Record with unit 0x%!l(MISSING)lx does not claim %!@(MISSING)"
+ "Registering synthesized claim for default app categories: %!@(MISSING)"
+ "Restore Now"
+ "Rolling UUID on %!@(MISSING) and marking not eligible for redaction"
+ "Save after update personas for bundles %!@(MISSING) attempted: %!d(MISSING) save error: %!@(MISSING)"
+ "Showing removed app prompt for %!@(MISSING) (%!@(MISSING)), restore source %!l(MISSING)d"
+ "SpecialAppEligibilityState.plist"
+ "T@\"NSArray\",C,N,V_preferredMarketplaces"
+ "ThirdParty"
+ "T{LSBundleBaseFlags=b1b1b1b1b1b1b1},R"
+ "T{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1},R"
+ "URLWithString:"
+ "Unable to create appex record for unit ID 0x%!l(MISSING)lx: %!@(MISSING)"
+ "Unable to get database in %!s(MISSING): %!@(MISSING)"
+ "Unsetting redactible for unit %!l(MISSING)lx"
+ "Utility"
+ "_LSApplicationRecordSpecificUnitsEnumerator"
+ "_modifiedPlugins"
+ "_preferredMarketplaces"
+ "_unitIDs"
+ "adding claim for default app types %!@(MISSING) for bundle %!l(MISSING)lx"
+ "appMarketplacesPreferencesStateURL"
+ "appexRecordsForUnitIDsWithContext:unitIDs:"
+ "apple-otpauth"
+ "apple-otpauth-migration"
+ "appstore-ui://restoreAppStore"
+ "as_restore_deeplink"
+ "attempting to set personas %!@(MISSING) for bundleIDs %!@(MISSING) from pid %!l(MISSING)d"
+ "bad_function_call was thrown in -fno-exceptions mode"
+ "bestRecordForScheme"
+ "bundleUnitsClaimingDefaultAppCategory"
+ "c40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
+ "canChangeDefaultAppForCategory:"
+ "category %!l(MISSING)u"
+ "claim for %!@(MISSING), which is a default app type. Ignoring this entire claim"
+ "closeAndReturnError:"
+ "com.apple.LaunchServices.DefaultAppCategory.Calling"
+ "com.apple.LaunchServices.DefaultAppCategory.ContactlessPayment"
+ "com.apple.LaunchServices.DefaultAppCategory.MailClient"
+ "com.apple.LaunchServices.DefaultAppCategory.Marketplace"
+ "com.apple.LaunchServices.DefaultAppCategory.Messaging"
+ "com.apple.LaunchServices.DefaultAppCategory.WebBrowser"
+ "com.apple.Passbook"
+ "com.apple.Preferences"
+ "com.apple.default-app-category"
+ "com.apple.default-app.contactless-payment"
+ "com.apple.default-app.mail-client"
+ "com.apple.default-app.messaging"
+ "com.apple.default-app.phone"
+ "com.apple.default-app.web-browser"
+ "com.apple.developer.calling-app"
+ "com.apple.developer.embedded-web-browser-engine"
+ "com.apple.developer.messaging-app"
+ "com.apple.developer.phone-app"
+ "com.apple.ios.StoreKitUIService"
+ "com.apple.launchservices.appmarketplaces.plist"
+ "com.apple.private.coreservices.appmarketplace.read"
+ "com.apple.private.coreservices.appmarketplace.write"
+ "const struct LSDefaultAppCategoryInfo *LSGetDefaultAppCategoryInfoForCategory(LSDefaultAppCategory)"
+ "could not get affected bundle info for persona change: %!@(MISSING)"
+ "could not update personas for %!@(MISSING) (bundle unit %!l(MISSING)lx): %!@(MISSING)"
+ "couldn't bind %!@(MISSING): %!@(MISSING)"
+ "couldn't fetch whether preference has ever been set for category %!l(MISSING)u: %!@(MISSING)"
+ "couldn't get to database in %!s(MISSING): %!@(MISSING)"
+ "couldn't load default apps set state, returning %!{(MISSING)BOOL}d for %!l(MISSING)u"
+ "couldn't read default apps set state to modify it, starting with default state: %!@(MISSING)"
+ "couldn't write default apps state: %!@(MISSING)"
+ "couldn't write plist: %!@(MISSING)"
+ "currentPreferencesWithError:"
+ "default-apps-claim"
+ "defaultApplicationForCategory:error:"
+ "detachAndSendNotification:forApplicationExtensionRecords:"
+ "displayOrderEnumeratorForViableDefaultAppsForCategory:options:"
+ "eligibility-checked-browser-engine-embedder"
+ "eligibilityDeletionDomain"
+ "enumeratorForViableDefaultAppsForCategory:options:"
+ "error binding %!{(MISSING)public}@ in %!s(MISSING): %!@(MISSING)"
+ "found handler %!@(MISSING) for subordinate claim %!@(MISSING); will set handler for %!@(MISSING)"
+ "getAffectedBundleInfoForIdentifiers"
+ "getDefaultApplicationCategories:withCurrentDefaultApplication:error:"
+ "getHasEverChangedPreferredAppForCategory:completion:"
+ "getPreferredAppMarketplacesWithCompletion:"
+ "getPreferredAppMarketplacesWithError:"
+ "handler preference for %!{(MISSING)public}@ for %!{(MISSING)public}@ %!{(MISSING)public}@ failed validation"
+ "has-eligibility-deletion-domain"
+ "i32@0:8@16^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}24"
+ "i36@0:8@16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}28"
+ "i40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
+ "im"
+ "initWithContext:options:unitIDs:unitCount:"
+ "initWithValidatedPlist:"
+ "loadIfNeeded"
+ "localizedStandardCompare:"
+ "migrateDefaultAppsToNewWorld_block_invoke"
+ "modifyPreferencesWithBlock:"
+ "newDefaultApps2024"
+ "no bindings for %!@(MISSING): %!@(MISSING)"
+ "no bundle for %!@(MISSING): %!l(MISSING)u"
+ "no category for type %!{(MISSING)public}@ in default apps claim of bundle %!{(MISSING)public}@!"
+ "objectsPassingTest:"
+ "open_dprotected_np failed"
+ "otpauth"
+ "otpauth-migration"
+ "parsed plist failed validation"
+ "performUpdateOfPersonasOfBundleIDs:toPersonaUniqueStrings:operationUUID:reply:"
+ "pid %!l(MISSING)d removing default app for category %!l(MISSING)u -> %!l(MISSING)d"
+ "pid %!l(MISSING)d setting handler for content type %!{(MISSING)public}@ set default app category %!l(MISSING)u -> %!l(MISSING)d"
+ "pid %!l(MISSING)d setting handler for scheme %!{(MISSING)public}@ set default app category %!l(MISSING)u -> %!l(MISSING)d "
+ "preferredMarketplaces"
+ "redactible"
+ "relaxed-default-apps-claim"
+ "rename failed"
+ "setDefaultApplicationForCategory:toApplicationRecord:completionHandler:"
+ "setPersonaUniqueStrings:forApplicationsWithBundleIdentifiers:operationUUID:requestContext:saveObserver:error:"
+ "setPreferredAppMarketplaces:completion:"
+ "setPreferredAppMarketplaces:error:"
+ "setPreferredMarketplaces:"
+ "settings-navigation://com.apple.Settings.AppInstallation/#ADRestoreAppStore"
+ "specialAppEligibilityStateURL"
+ "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /Library/Caches/com.apple.xbs/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1355:63)]"
+ "supportedDefaultAppCategories"
+ "toPlist"
+ "transform lost the plist object!"
+ "uncommon answer for domain %!d(MISSING): %!d(MISSING)"
+ "v16@?0@\"LSMarketplacesPreferences\"8"
+ "v24@?0r^{LSDefaultAppCategoryInfo=Q^{__CFString}^{__CFString}Q^?^{LSDefaultAppCategorySubordinateClaim}Q}8^B16"
+ "v28@?0@\"NSString\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20"
+ "v28@?0@\"NSString\"8I16r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}20"
+ "v28@?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}12*20"
+ "v36@0:8^{LSContext=@}16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}28"
+ "v40@0:8Q16@24@?32"
+ "v48@0:8@\"NSSet\"16@\"NSSet\"24@\"NSUUID\"32@?<v@?@\"<_LSPendingSaveToken>\"@\"NSError\">40"
+ "void _LSServer_NotePreferenceSetForCategory(LSDefaultAppCategory)"
+ "writeData:error:"
+ "{LSBundleBaseFlags=\"appleInternal\"b1\"requiresObjCGarbageCollection\"b1\"builtWithTSan\"b1\"isLinkEnabled\"b1\"isSecuredSystemContent\"b1\"redactible\"b1\"_reserved\"b1}"
+ "{LSBundleBaseFlags=b1b1b1b1b1b1b1}16@0:8"
+ "{LSBundleBaseFlags=b1b1b1b1b1b1b1}40@0:8^{LSContext=@}16I24I28r^{LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}32"
+ "{LSBundleData=\"base\"{LSBundleBaseData=\"bookmark\"I\"container\"I\"execPath\"I\"exactIdentifier\"I\"teamID\"I\"platform\"I\"registrationTime\"i\"version\"{LSVersionNumber=\"_opaque\"[32C]}\"execSDKVersion\"{LSVersionNumber=\"_opaque\"[32C]}\"machOUUIDs\"I\"dataContainerAlias\"I\"bundleName\"I\"localizedShortDisplayName\"I\"displayName\"I\"localizedDisplayName\"I\"localizedMicrophoneUsageDescription\"I\"localizedIdentityUsageDescription\"I\"codeInfoIdentifier\"I\"signerOrganization\"I\"signerIdentity\"I\"infoDictionary\"I\"entitlements\"I\"groupContainers\"I\"containingDirectoryClass\"C\"profileValidationState\"C\"intentDefinitionURLs\"I\"_sliceMask\"S\"signatureVersion\"I\"flags\"{LSBundleBaseFlags=\"appleInternal\"b1\"requiresObjCGarbageCollection\"b1\"builtWithTSan\"b1\"isLinkEnabled\"b1\"isSecuredSystemContent\"b1\"redactible\"b1\"_reserved\"b1}}\"_clas\"I\"_bundleFlags\"Q\"_plistContentFlags\"I\"_itemFlags\"I\"_iconFlags\"C\"moreFlags\"{LSBundleMoreFlags=\"isWebBrowser\"b1\"isMailClient\"b1\"supportsControllerUserInteraction\"b1\"supportsSpotlightQueryContinuation\"b1\"supportsSpotlightActions\"b1\"isCodeSigningInfoNotAuthoritative\"b1\"applicationQueriesSchemesTooBig\"b1\"isUpdateAvailable\"b1\"isPlaygroundsApp\"b1\"supportsAlwaysOnDisplay\"b1\"defaultsToPrivateAlwaysOnDisplayTreatment\"b1\"supportsLiveActivities\"b1\"supportsLiveActivitiesFrequentUpdates\"b1\"requiresPostprocessing\"b1\"hasShellRole\"b1\"requiresSecureLaunch\"b1\"eligibleForWatchAppInstall\"b1\"isEligibilityCheckedBrowser\"b1\"isEligibilityCheckedBrowserEngineEmbedder\"b1\"isManagedAppDistributor\"b1\"isHiddenByAppProtection\"b1\"isLockedByAppProtection\"b1\"_reserved\"b1}\"_hfsType\"I\"_mtime\"i\"minSystemVersionPlatform\"I\"_minSystemVersion\"{LSVersionNumber=\"_opaque\"[32C]}\"_maxSystemVersion\"{LSVersionNumber=\"_opaque\"[32C]}\"appStoreToolsBuildVersion\"I\"sequenceNumber\"Q\"compatibilityState\"Q\"itemID\"Q\"deviceFamilies\"I\"identifier\"I\"counterpartIdentifiers\"I\"equivalentBundleIdentifiers\"I\"categoryType\"I\"secondaryCategoryType\"I\"filename\"I\"bundleVersion\"I\"shortVersionString\"I\"installType\"I\"installFailureReason\"Q\"vendorName\"I\"appType\"I\"staticDiskUsage\"Q\"purchaserDSID\"Q\"downloaderDSID\"Q\"familyID\"Q\"itemName\"I\"storefront\"Q\"versionIdentifier\"Q\"sourceAppBundleID\"I\"appVariant\"I\"managementDeclarationIdentifier\"I\"ratingRank\"Q\"ratingLabel\"I\"genreID\"Q\"genre\"I\"distributorInfo\"I\"primaryIconName\"I\"alternatePrimaryIconName\"I\"iconsDict\"I\"iconFileNames\"I\"libraryPath\"I\"libraryItems\"I\"claims\"I\"types\"I\"plugins\"I\"driverExtensions\"I\"extensionPoints\"I\"activityTypes\"I\"queriableSchemes\"I\"bgPermittedIDs\"I\"carPlayInstrumentClusterURLSchemes\"I\"appContainerAlias\"I\"revision\"C\"retries\"C\"_reserved4\"C\"sandboxEnvironmentVariables\"I\"localizedNameWithContext\"[1I]\"bundlePersonas\"I\"bundlePersonaTypes\"I\"appClipFields\"{LSAppClipFields=\"parentAppIDs\"I}\"recordModificationTime\"i\"supportedGameControllers\"I\"mobileInstallIDs\"I\"applicationManagementDomain\"I\"stashedAppDict\"I\"linkedParentBundleIdentifier\"I\"_reserved5\"I}"
+ "{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32@0:8@16^@24"
+ "{LSBundleMoreFlags=\"isWebBrowser\"b1\"isMailClient\"b1\"supportsControllerUserInteraction\"b1\"supportsSpotlightQueryContinuation\"b1\"supportsSpotlightActions\"b1\"isCodeSigningInfoNotAuthoritative\"b1\"applicationQueriesSchemesTooBig\"b1\"isUpdateAvailable\"b1\"isPlaygroundsApp\"b1\"supportsAlwaysOnDisplay\"b1\"defaultsToPrivateAlwaysOnDisplayTreatment\"b1\"supportsLiveActivities\"b1\"supportsLiveActivitiesFrequentUpdates\"b1\"requiresPostprocessing\"b1\"hasShellRole\"b1\"requiresSecureLaunch\"b1\"eligibleForWatchAppInstall\"b1\"isEligibilityCheckedBrowser\"b1\"isEligibilityCheckedBrowserEngineEmbedder\"b1\"isManagedAppDistributor\"b1\"isHiddenByAppProtection\"b1\"isLockedByAppProtection\"b1\"_reserved\"b1}"
+ "{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}16@0:8"
+ "{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
+ "{LSVersionNumber=[32C]}40@0:8^{LSContext=@}16I24I28r^{LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1b1}}32"
+ "{unordered_map<unsigned int, LSPluginData, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, LSPluginData>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, LSPluginData>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, LSPluginData>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, LSPluginData>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, LSPluginData>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, LSPluginData>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, LSPluginData>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, LSPluginData>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, LSPluginData>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, LSPluginData>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, LSPluginData>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, LSPluginData>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<unsigned int, LSPluginData>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, LSPluginData>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, LSPluginData>, std::hash<unsigned int>, std::equal_to<unsigned int>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, LSPluginData>, std::equal_to<unsigned int>, std::hash<unsigned int>>>=\"__value_\"f}}}"
- "-[_LSDModifyClient performUpdateOfPersonasOfBundleID:toPersonaUniqueStrings:operationUUID:reply:]"
- "-[_LSDModifyClient performUpdateOfPersonasOfBundleID:toPersonaUniqueStrings:operationUUID:reply:]_block_invoke"
- "@32@0:8^{LSContext=@}16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}24"
- "@36@0:8@16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}28"
- "@36@0:8^{LSContext=@}16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}28"
- "@40@0:8^{LSContext=@}16I24I28r^{LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}32"
- "@40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
- "@40@0:8^{LSContext=@}16I24I28r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}32"
- "@44@0:8B16^{LSContext=@}20I28I32r^{LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}36"
- "@44@0:8B16^{LSContext=@}20I28I32r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}36"
- "@44@0:8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20@28^@36"
- "@44@0:8^{LSContext=@}16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}28^@36"
- "@44@0:8^{LSContext=@}16I24r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}28^@36"
- "@52@0:8^{LSContext=@}16I24r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}28@36^@44"
- "@64@0:8@16@24^{LSContext=@}32I40I44r^{LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}48^@56"
- "B28@?0@\"_LSDatabase\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20"
- "B28@?0^{LSContext=@}8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20"
- "B36@0:8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20^{LSContext=@}28"
- "B36@0:8I16r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}20@28"
- "B40@0:8I16r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}20I28^{LSContext=@}32"
- "B40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
- "B52@0:8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20^{LSContext=@}28@36^@44"
- "B60@0:8^@16^@24I32r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}36@44^@52"
- "Bundle 0x%!l(MISSING)lx is a placeholder, so it cannot be the default web browser or mail client."
- "Bundle 0x%!l(MISSING)lx is in an unsupported location, so it cannot be the default web browser or mail client."
- "Bundle 0x%!l(MISSING)lx is not an application, so it cannot be the default web browser or mail client."
- "C40@0:8^{LSContext=@}16I24I28r^{LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}32"
- "C40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
- "I40@0:8^{LSContext=@}16I24I28r^{LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}32"
- "I40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
- "I40@0:8^{LSContext=@}16I24I28r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}32"
- "Override allowed for content type %!{(MISSING)public}@, roles 0x%!{(MISSING)public}x"
- "Override not allowed for content type %!{(MISSING)public}@, roles 0x%!{(MISSING)public}x"
- "Q40@0:8^{LSContext=@}16I24I28r^{?=IIIsSIII[8I]III}32"
- "Q40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
- "Save after update personas for bundle %!@(MISSING) attempted: %!d(MISSING) save error: %!@(MISSING)"
- "Showing removed app prompt for %!@(MISSING)"
- "T{LSBundleBaseFlags=b1b1b1b1b1b1},R"
- "T{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1},R"
- "_LSRecord_resolve__flags"
- "_flagsWithContext:tableID:unitID:unitBytes:"
- "attempting to set personas %!@(MISSING) for bundleID %!@(MISSING) from pid %!l(MISSING)d"
- "c40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
- "i32@0:8@16^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}24"
- "i36@0:8@16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}28"
- "i40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
- "performUpdateOfPersonasOfBundleID:toPersonaUniqueStrings:operationUUID:reply:"
- "process may not map database, so it may not get eligibility"
- "sendNotification:forApplicationExtensionRecords:"
- "static NSInteger LaunchServices::PrefsStorage::_GetIndexOfValueInPrefsArrayWithPredicate(NSArray *__strong, const Pred &) [Pred = (lambda at /Library/Caches/com.apple.xbs/Sources/CoreServices/LaunchServices.subprj/Source/LaunchServices/Info/LSPrefs.mm:1294:63)]"
- "v28@?0@\"NSString\"8I16r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}20"
- "v28@?0@\"NSString\"8I16r^{LSPluginData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}IIIII{LSVersionNumber=[32C]}IIII}20"
- "v28@?0I8r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}12*20"
- "v36@0:8^{LSContext=@}16I24r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}28"
- "v48@0:8@\"NSString\"16@\"NSSet\"24@\"NSUUID\"32@?<v@?@\"<_LSPendingSaveToken>\"@\"NSError\">40"
- "{LSBundleBaseFlags=\"appleInternal\"b1\"requiresObjCGarbageCollection\"b1\"builtWithTSan\"b1\"isLinkEnabled\"b1\"isSecuredSystemContent\"b1\"_reserved\"b1}"
- "{LSBundleBaseFlags=b1b1b1b1b1b1}16@0:8"
- "{LSBundleBaseFlags=b1b1b1b1b1b1}40@0:8^{LSContext=@}16I24I28r^{LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}32"
- "{LSBundleData=\"base\"{LSBundleBaseData=\"bookmark\"I\"container\"I\"execPath\"I\"exactIdentifier\"I\"teamID\"I\"platform\"I\"registrationTime\"i\"version\"{LSVersionNumber=\"_opaque\"[32C]}\"execSDKVersion\"{LSVersionNumber=\"_opaque\"[32C]}\"machOUUIDs\"I\"dataContainerAlias\"I\"bundleName\"I\"localizedShortDisplayName\"I\"displayName\"I\"localizedDisplayName\"I\"localizedMicrophoneUsageDescription\"I\"localizedIdentityUsageDescription\"I\"codeInfoIdentifier\"I\"signerOrganization\"I\"signerIdentity\"I\"infoDictionary\"I\"entitlements\"I\"groupContainers\"I\"containingDirectoryClass\"C\"profileValidationState\"C\"intentDefinitionURLs\"I\"_sliceMask\"S\"signatureVersion\"I\"flags\"{LSBundleBaseFlags=\"appleInternal\"b1\"requiresObjCGarbageCollection\"b1\"builtWithTSan\"b1\"isLinkEnabled\"b1\"isSecuredSystemContent\"b1\"_reserved\"b1}}\"_clas\"I\"_bundleFlags\"Q\"_plistContentFlags\"I\"_itemFlags\"I\"_iconFlags\"C\"moreFlags\"{LSBundleMoreFlags=\"isWebBrowser\"b1\"isMailClient\"b1\"supportsControllerUserInteraction\"b1\"supportsSpotlightQueryContinuation\"b1\"supportsSpotlightActions\"b1\"isCodeSigningInfoNotAuthoritative\"b1\"applicationQueriesSchemesTooBig\"b1\"isUpdateAvailable\"b1\"isPlaygroundsApp\"b1\"supportsAlwaysOnDisplay\"b1\"defaultsToPrivateAlwaysOnDisplayTreatment\"b1\"supportsLiveActivities\"b1\"supportsLiveActivitiesFrequentUpdates\"b1\"requiresPostprocessing\"b1\"hasShellRole\"b1\"requiresSecureLaunch\"b1\"eligibleForWatchAppInstall\"b1\"isEligibilityCheckedBrowser\"b1\"isManagedAppDistributor\"b1\"isHiddenByAppProtection\"b1\"isLockedByAppProtection\"b1\"_reserved\"b1}\"_hfsType\"I\"_mtime\"i\"minSystemVersionPlatform\"I\"_minSystemVersion\"{LSVersionNumber=\"_opaque\"[32C]}\"_maxSystemVersion\"{LSVersionNumber=\"_opaque\"[32C]}\"appStoreToolsBuildVersion\"I\"sequenceNumber\"Q\"compatibilityState\"Q\"itemID\"Q\"deviceFamilies\"I\"identifier\"I\"counterpartIdentifiers\"I\"equivalentBundleIdentifiers\"I\"categoryType\"I\"secondaryCategoryType\"I\"filename\"I\"bundleVersion\"I\"shortVersionString\"I\"installType\"I\"installFailureReason\"Q\"vendorName\"I\"appType\"I\"staticDiskUsage\"Q\"purchaserDSID\"Q\"downloaderDSID\"Q\"familyID\"Q\"itemName\"I\"storefront\"Q\"versionIdentifier\"Q\"sourceAppBundleID\"I\"appVariant\"I\"managementDeclarationIdentifier\"I\"ratingRank\"Q\"ratingLabel\"I\"genreID\"Q\"genre\"I\"distributorInfo\"I\"primaryIconName\"I\"alternatePrimaryIconName\"I\"iconsDict\"I\"iconFileNames\"I\"libraryPath\"I\"libraryItems\"I\"claims\"I\"types\"I\"plugins\"I\"driverExtensions\"I\"extensionPoints\"I\"activityTypes\"I\"queriableSchemes\"I\"bgPermittedIDs\"I\"carPlayInstrumentClusterURLSchemes\"I\"appContainerAlias\"I\"revision\"C\"retries\"C\"_reserved4\"C\"sandboxEnvironmentVariables\"I\"localizedNameWithContext\"[1I]\"bundlePersonas\"I\"bundlePersonaTypes\"I\"appClipFields\"{LSAppClipFields=\"parentAppIDs\"I}\"recordModificationTime\"i\"supportedGameControllers\"I\"mobileInstallIDs\"I\"applicationManagementDomain\"I\"stashedAppDict\"I\"linkedParentBundleIdentifier\"I\"_reserved5\"I}"
- "{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32@0:8@16^@24"
- "{LSBundleMoreFlags=\"isWebBrowser\"b1\"isMailClient\"b1\"supportsControllerUserInteraction\"b1\"supportsSpotlightQueryContinuation\"b1\"supportsSpotlightActions\"b1\"isCodeSigningInfoNotAuthoritative\"b1\"applicationQueriesSchemesTooBig\"b1\"isUpdateAvailable\"b1\"isPlaygroundsApp\"b1\"supportsAlwaysOnDisplay\"b1\"defaultsToPrivateAlwaysOnDisplayTreatment\"b1\"supportsLiveActivities\"b1\"supportsLiveActivitiesFrequentUpdates\"b1\"requiresPostprocessing\"b1\"hasShellRole\"b1\"requiresSecureLaunch\"b1\"eligibleForWatchAppInstall\"b1\"isEligibilityCheckedBrowser\"b1\"isManagedAppDistributor\"b1\"isHiddenByAppProtection\"b1\"isLockedByAppProtection\"b1\"_reserved\"b1}"
- "{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}16@0:8"
- "{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}40@0:8^{LSContext=@}16I24I28r^{LSBundleData={LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}IQIIC{LSBundleMoreFlags=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}IiI{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IQQQIIIIIIIIIIQIIQQQQIQQIIIQIQIIIIIIIIIIIIIIIIIICCCI[1I]II{LSAppClipFields=I}iIIIIII}32"
- "{LSVersionNumber=[32C]}40@0:8^{LSContext=@}16I24I28r^{LSBundleBaseData=IIIIIIi{LSVersionNumber=[32C]}{LSVersionNumber=[32C]}IIIIIIIIIIIIIICCISI{LSBundleBaseFlags=b1b1b1b1b1b1}}32"

```
