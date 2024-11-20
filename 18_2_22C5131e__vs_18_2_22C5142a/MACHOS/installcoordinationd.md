## installcoordinationd

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordinationd`

```diff

-631.60.50.0.0
-  __TEXT.__text: 0x9668c
+631.62.3.0.0
+  __TEXT.__text: 0x974b8
   __TEXT.__auth_stubs: 0x1060
-  __TEXT.__objc_stubs: 0xa3c0
-  __TEXT.__objc_methlist: 0x4bc8
+  __TEXT.__objc_stubs: 0xa460
+  __TEXT.__objc_methlist: 0x4c18
   __TEXT.__const: 0x1f8
-  __TEXT.__cstring: 0x16e84
-  __TEXT.__objc_classname: 0x99e
-  __TEXT.__oslogstring: 0xccb0
-  __TEXT.__objc_methtype: 0x21a9
-  __TEXT.__objc_methname: 0xfab1
+  __TEXT.__cstring: 0x17032
+  __TEXT.__objc_classname: 0x9c1
+  __TEXT.__oslogstring: 0xcfaf
+  __TEXT.__objc_methtype: 0x21ad
+  __TEXT.__objc_methname: 0xfb4b
   __TEXT.__gcc_except_tab: 0x28b0
-  __TEXT.__ustring: 0x22d0
+  __TEXT.__ustring: 0x1966
   __TEXT.__dlopen_cstrs: 0x68
-  __TEXT.__unwind_info: 0x22a0
+  __TEXT.__unwind_info: 0x22b0
   __DATA_CONST.__auth_got: 0x840
   __DATA_CONST.__got: 0x408
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x2918
-  __DATA_CONST.__cfstring: 0x91a0
-  __DATA_CONST.__objc_classlist: 0x230
+  __DATA_CONST.__const: 0x29a0
+  __DATA_CONST.__cfstring: 0x90a0
+  __DATA_CONST.__objc_classlist: 0x238
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x1d8
+  __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_intobj: 0x150
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0xcc00
-  __DATA.__objc_selrefs: 0x2f78
-  __DATA.__objc_ivar: 0x448
-  __DATA.__objc_data: 0x15e0
+  __DATA.__objc_const: 0xccd0
+  __DATA.__objc_selrefs: 0x2fa0
+  __DATA.__objc_ivar: 0x44c
+  __DATA.__objc_data: 0x1630
   __DATA.__data: 0x650
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x240
+  __DATA.__bss: 0x260
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3057
+  Functions: 3079
   Symbols:   406
-  CStrings:  5176
+  CStrings:  5204
 
CStrings:
+ "%!s(MISSING): Failed to get localized name for bundleID %!@(MISSING): %!@(MISSING)"
+ "%!s(MISSING): Failed to load expected classes from ScreenTimeCore.framework: STManagementState : %!p(MISSING)"
+ "%!s(MISSING): Failed to load expected classes from WebBookmarks.framework: WBWebFilterSettings : %!p(MISSING)"
+ "%!s(MISSING): Failed to open ScreenTimeCore framework: %!s(MISSING)"
+ "%!s(MISSING): Failed to open WebBookmarks framework: %!s(MISSING)"
+ "%!s(MISSING): Failed to query STManagementState for screen time passcode management"
+ "%!s(MISSING): Failed to query WBWebFilterSettings for web content filtering restrictions"
+ "%!s(MISSING): Recevied communication from the UI host; successfully started displaying the deletion sheet"
+ "%!s(MISSING): Showing deletion sheet for %!@(MISSING) with data %!@(MISSING)"
+ "%!s(MISSING): Unexpectedly found empty list for preferred app marketplaces : %!@(MISSING)"
+ "%!s(MISSING): Unsupported app type for content restriction based app deletion alert"
+ "-[IXSAppUninstaller _screenTimeManagementEnabled]"
+ "-[IXSAppUninstaller _screenTimeManagementEnabled]_block_invoke"
+ "-[IXSAppUninstaller _webContentFilterEnabled]"
+ "-[IXSAppUninstaller _webContentFilterEnabled]_block_invoke"
+ "-[IXSContentRestrictedAppDeleteAlert message]"
+ "-[IXSDefaultAppDownloadAlert _bundleIDForDefaultAppMarketplace:]"
+ "-[IXSDefaultAppDownloadAlert _localizedNameForDefaultAppMarketplace]"
+ "-[IXSRemoteDeletionPromptManager isValidBundleIDForRemoteAlert:withAppType:numAppsInstalled:]"
+ "/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore"
+ "/System/Library/PrivateFrameworks/WebBookmarks.framework/WebBookmarks"
+ "19:07:25"
+ "B40@0:8@16^Q24^Q32"
+ "DEFAULT_APP_NOT_AVAILABLE_DELETE_APP_OPEN_APP_MARKETPLACE"
+ "Delete Content Restricted App"
+ "IXSContentRestrictedAppDeleteAlert"
+ "Nov 15 2024"
+ "NumInstalledApps"
+ "Open %!@(MISSING)"
+ "STManagementState"
+ "TEST_MODE_APP_DELETION_UI_SAD_KILL_FOR_TESTING_KEY"
+ "TEST_MODE_APP_DELETION_UI_SAD_NUM_INSTALLED_APPS_KEY"
+ "TEST_MODE_CONTENT_RESTRICTION_MANAGEMENT_TYPE"
+ "TestCrash"
+ "This app cannot be deleted while web content restrictions are enabled."
+ "This app is managed by your parent or guardian and cannot be deleted."
+ "UNINSTALL_ICON_BODY_DELETE_CONTENT_RESTRICTED_APPS_SCREENTIME_PASSCODE_AND_REMOTE_MANAGED"
+ "UNINSTALL_ICON_BODY_DELETE_CONTENT_RESTRICTED_APPS_WEB_CONTENT_FILTERING_SET"
+ "UNINSTALL_ICON_TITLE_DELETE_CONTENT_RESTRICTED_APPS"
+ "Unable to Delete App"
+ "Unexpectedly found empty list for preferred app marketplaces"
+ "WBWebFilterSettings"
+ "_bundleIDForDefaultAppMarketplace:"
+ "_contentRestrictionIsEnabledForBundleID:"
+ "_iCloudIsEnabledForPhotos"
+ "_localizedNameForDefaultAppMarketplace"
+ "_screenTimeManagementEnabled"
+ "_watchIsPaired"
+ "_webContentFilterEnabled"
+ "begin"
+ "com.apple.mobilesafari"
+ "initWithAppRecord:removability:appType:"
+ "isRestrictionsPasscodeSet"
+ "isValidBundleIDForRemoteAlert:withAppType:numAppsInstalled:"
+ "isWebFilterEnabled"
+ "sharedWebFilterSettings"
+ "shouldRequestMoreTime"
- "-[IXSDefaultAppDownloadAlert openDefaultAppStoreWithError:]"
- "-[IXSRemoteDeletionPromptManager iCloudIsEnabledForPhotos]"
- "-[IXSRemoteDeletionPromptManager isValidBundleIDForRemoteAlert:withAppType:]"
- "-[IXSRemoteDeletionPromptManager watchIsPaired]"
- "18:23:04"
- "B32@0:8@16^Q24"
- "DEFAULT_APP_NOT_AVAILABLE_DELETE_APP_OPEN_APP_STORE"
- "Deleting this app will not delete your photos and videos on this iPhone or any stored in iCloud."
- "Deleting this app will not delete your photos and videos on this iPhone."
- "Nov  2 2024"
- "Open App Store"
- "UNINSTALL_ICON_BODY_DELETE_DATA_APPSTORE"
- "UNINSTALL_ICON_BODY_DELETE_DATA_APPSTORE_EIGHT"
- "UNINSTALL_ICON_BODY_DELETE_DATA_APPSTORE_FIVE"
- "UNINSTALL_ICON_BODY_DELETE_DATA_APPSTORE_FOUR"
- "UNINSTALL_ICON_BODY_DELETE_DATA_APPSTORE_NINE"
- "UNINSTALL_ICON_BODY_DELETE_DATA_APPSTORE_ONE"
- "UNINSTALL_ICON_BODY_DELETE_DATA_APPSTORE_SEVEN"
- "UNINSTALL_ICON_BODY_DELETE_DATA_APPSTORE_SIX"
- "UNINSTALL_ICON_BODY_DELETE_DATA_APPSTORE_THREE"
- "UNINSTALL_ICON_BODY_DELETE_DATA_APPSTORE_TWO"
- "UNINSTALL_ICON_BODY_DELETE_DATA_PHOTOS"
- "UNINSTALL_ICON_BODY_DELETE_DATA_PHOTOS_WITHOUT_ICLOUD"
- "_customDeleteMessageForDeletableSystemApp"
- "_customDeleteStringForAppMarketplace"
- "iCloudIsEnabledForPhotos"
- "installedAppsFromAppMarketplaceWithBundleID:"
- "isValidBundleIDForRemoteAlert:withAppType:"
- "watchIsPaired"

```
