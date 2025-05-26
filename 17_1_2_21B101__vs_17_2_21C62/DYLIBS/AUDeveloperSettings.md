## AUDeveloperSettings

> `/System/Library/PrivateFrameworks/AUDeveloperSettings.framework/AUDeveloperSettings`

```diff

-916.40.22.0.2
-  __TEXT.__text: 0xbfa8
-  __TEXT.__auth_stubs: 0x4c0
-  __TEXT.__objc_methlist: 0x7d8
+916.60.6.0.0
+  __TEXT.__text: 0xc8d0
+  __TEXT.__auth_stubs: 0x4e0
+  __TEXT.__objc_methlist: 0x830
   __TEXT.__const: 0x74
   __TEXT.__oslogstring: 0x257
-  __TEXT.__cstring: 0x2256
-  __TEXT.__gcc_except_tab: 0x2e0
+  __TEXT.__cstring: 0x2422
+  __TEXT.__gcc_except_tab: 0x304
   __TEXT.__dlopen_cstrs: 0xb0
-  __TEXT.__unwind_info: 0x324
-  __TEXT.__objc_classname: 0x265
-  __TEXT.__objc_methname: 0x2012
+  __TEXT.__unwind_info: 0x344
+  __TEXT.__objc_classname: 0x267
+  __TEXT.__objc_methname: 0x215c
   __TEXT.__objc_methtype: 0x661
-  __TEXT.__objc_stubs: 0x1ee0
-  __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__const: 0xdd0
+  __TEXT.__objc_stubs: 0x1fc0
+  __DATA_CONST.__got: 0x100
+  __DATA_CONST.__const: 0xe18
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1fc8
-  __DATA_CONST.__objc_selrefs: 0x8f0
+  __DATA_CONST.__objc_const: 0x2008
+  __DATA_CONST.__objc_selrefs: 0x950
   __AUTH_CONST.__objc_const: 0x550
   __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0x2c80
-  __AUTH_CONST.__auth_got: 0x270
+  __AUTH_CONST.__cfstring: 0x2e20
+  __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__auth_got: 0x280
   __AUTH.__objc_data: 0x410
   __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x1a8
+  __DATA.__objc_classrefs: 0x1b8
   __DATA.__objc_superrefs: 0x60
-  __DATA.__objc_ivar: 0xe0
+  __DATA.__objc_ivar: 0xe8
   __DATA.__data: 0x2a0
   __DATA.__bss: 0x80
   __DATA_DIRTY.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 224
-  Symbols:   1437
-  CStrings:  889
+  Functions: 233
+  Symbols:   1482
+  CStrings:  919
 
Symbols:
+ -[AUDeveloperSettingsAboutListController confirmUpdateNow]
+ -[AUDeveloperSettingsAboutListController getDownloadedVersion:]
+ -[AUDeveloperSettingsAboutListController isAuthListingEnabled]
+ -[AUDeveloperSettingsAboutListController setAuthListingStatus:]
+ -[AUDeveloperSettingsAboutListController shouldDisplayAuthListingOption]
+ -[AUDeveloperSettingsAboutListController updateNow]
+ -[AUInternalSettingsController selectSpecifier:]
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_PSBadgedTableCell
+ _OBJC_CLASS_$_PSConfirmationSpecifier
+ _OBJC_IVAR_$_AUDeveloperSettingsAboutListController._authListingEnabledSwitchSpecifier
+ _OBJC_IVAR_$_AUDeveloperSettingsAboutListController._updateNowButtonSpecifier
+ _PSBadgeNumberKey
+ _PSConfirmationCancelKey
+ _PSConfirmationOKKey
+ _PSConfirmationPromptKey
+ _PSConfirmationTitleKey
+ ___51-[AUDeveloperSettingsAboutListController updateNow]_block_invoke
+ ___block_literal_global.639
+ ___block_literal_global.641
+ _cleanupPersonalizedUpdateAvailable
+ _kAUSettingsAccessoryDownloadedVersion
+ _kAUSettingsAccessoryEnableAuthlisting
+ _kAUSettingsAccessoryPersonalizationHeader
+ _kAUSettingsAccessoryUpdateNow
+ _kAUSettingsTableFooterText
+ _kAuthListingEnabledKey
+ _kDownloadedVersionKey
+ _kPersonalizationRequiredKey
+ _kUARPStandaloneFirmwareDirectory
+ _notify_post
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$setButtonAction:
+ _objc_msgSend$setConfirmationAction:
+ _objc_msgSend$setTarget:
+ _objc_msgSend$setupWithDictionary:
+ _objc_msgSend$shouldDisplayAuthListingOption
+ _objc_msgSend$showConfirmationViewForSpecifier:
+ _objc_unsafeClaimAutoreleasedReturnValue
- ___block_literal_global.636
- ___block_literal_global.638
CStrings:
+ "\t"
+ "%s%@"
+ "/usr/standalone/firmware/accessoryupdater/UARP"
+ "Cancel"
+ "Downloaded Version"
+ "Enable Auth Listing"
+ "FooterText"
+ "If this accessory is not auth listed, select 'Update Now' to personalize FW via AppleConnect (prompt should show in the next couple seconds). Otherwise, enable auth listing and the updates will run automatically."
+ "Ok"
+ "Personalization"
+ "Update Now"
+ "_authListingEnabledSwitchSpecifier"
+ "_updateNowButtonSpecifier"
+ "authListingEnabled"
+ "com.apple.accessoryUpdater.uarp.fwUpdateNow."
+ "confirmUpdateNow"
+ "dictionaryWithObjects:forKeys:count:"
+ "downloadedVersion"
+ "getDownloadedVersion:"
+ "i"
+ "isAuthListingEnabled"
+ "personalizationRequired"
+ "setAuthListingStatus:"
+ "setButtonAction:"
+ "setConfirmationAction:"
+ "setTarget:"
+ "setupWithDictionary:"
+ "shouldDisplayAuthListingOption"
+ "showConfirmationViewForSpecifier:"
+ "updateNow"

```
