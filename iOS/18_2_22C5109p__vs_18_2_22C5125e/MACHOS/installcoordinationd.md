## installcoordinationd

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordinationd`

```diff

-631.60.23.502.2
-  __TEXT.__text: 0x9226c
-  __TEXT.__auth_stubs: 0x1050
-  __TEXT.__objc_stubs: 0x9f20
-  __TEXT.__objc_methlist: 0x4988
-  __TEXT.__const: 0x1a8
-  __TEXT.__cstring: 0x15db5
-  __TEXT.__objc_classname: 0x957
-  __TEXT.__oslogstring: 0xc961
-  __TEXT.__objc_methtype: 0x2100
-  __TEXT.__objc_methname: 0xf3f3
+631.60.47.0.0
+  __TEXT.__text: 0x93574
+  __TEXT.__auth_stubs: 0x1060
+  __TEXT.__objc_stubs: 0xa1c0
+  __TEXT.__objc_methlist: 0x49d0
+  __TEXT.__const: 0x1f8
+  __TEXT.__cstring: 0x16844
+  __TEXT.__objc_classname: 0x945
+  __TEXT.__oslogstring: 0xcaba
+  __TEXT.__objc_methtype: 0x2131
+  __TEXT.__objc_methname: 0xf77f
   __TEXT.__gcc_except_tab: 0x28a4
-  __TEXT.__ustring: 0x580
+  __TEXT.__ustring: 0x22d0
   __TEXT.__dlopen_cstrs: 0x68
-  __TEXT.__unwind_info: 0x21c8
-  __DATA_CONST.__auth_got: 0x838
-  __DATA_CONST.__got: 0x3f0
+  __TEXT.__unwind_info: 0x21f8
+  __DATA_CONST.__auth_got: 0x840
+  __DATA_CONST.__got: 0x400
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x27c8
-  __DATA_CONST.__cfstring: 0x8580
-  __DATA_CONST.__objc_classlist: 0x220
+  __DATA_CONST.__const: 0x27e8
+  __DATA_CONST.__cfstring: 0x8f20
+  __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x1c8
+  __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_intobj: 0x150
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0xc7e0
-  __DATA.__objc_selrefs: 0x2e38
-  __DATA.__objc_ivar: 0x42c
-  __DATA.__objc_data: 0x1540
+  __DATA.__objc_const: 0xc820
+  __DATA.__objc_selrefs: 0x2ee0
+  __DATA.__objc_ivar: 0x43c
+  __DATA.__objc_data: 0x14f0
   __DATA.__data: 0x650
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x238

   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/PlugInKit.framework/PlugInKit
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
+  - /System/Library/PrivateFrameworks/SEService.framework/SEService
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2956
-  Symbols:   402
-  CStrings:  5021
+  Functions: 2976
+  Symbols:   405
+  CStrings:  5106
 
Symbols:
+ _MCFeatureAppRemovalAllowed
+ _MGGetStringAnswer
+ _OBJC_CLASS_$_SESNFCAppSettingsContext
CStrings:
+ "\x12\x11"
+ "\"\x17S!\x15\x19!\x13\x16\""
+ "%!s(MISSING): %!@(MISSING) cannot be uninstalled: deletableAccordingToLS:%!c(MISSING) deletionIsRestricted:%!c(MISSING) ignoreRestrictions:%!c(MISSING) hasBundleContainer:%!c(MISSING)"
+ "%!s(MISSING): Acquiring termination assertion to install %!@(MISSING)"
+ "%!s(MISSING): Acquiring termination assertion to install placeholder for %!@(MISSING)"
+ "%!s(MISSING): Failed to determine whether app type needs to gate deletion of last default app"
+ "%!s(MISSING): Failed to get list of preferred app marketplaces"
+ "%!s(MISSING): Failed to launch app with bundleID %!@(MISSING): %!@(MISSING)"
+ "%!s(MISSING): Failed to open default app marketplace : %!@(MISSING)"
+ "%!s(MISSING): Failed to query IMCloudKitHooks for iCloud state"
+ "%!s(MISSING): Failed to query PHPhotoLibrary and PHAsset for shared media count"
+ "%!s(MISSING): Failed to query PHPhotoLibrary for iCloud state"
+ "%!s(MISSING): IMCloudKitHooks returned %!c(MISSING) for iCloud state"
+ "%!s(MISSING): PHPhotoLibrary and PHAsset returned %!l(MISSING)u for shared media count"
+ "%!s(MISSING): PHPhotoLibrary returned %!c(MISSING) for iCloud state"
+ "%!s(MISSING): Registering opportunistic install for %!@(MISSING)"
+ "-[IXSAppUninstallAlert initWithAppRecord:bundleIdentifier:removability:isManagedByManagedSettings:deletionIsRestricted:]"
+ "-[IXSAppUninstaller _displayAuthenticationErrorForApp:]_block_invoke"
+ "-[IXSAppUninstaller _finalDeletionPromptWithRecord:identity:clientName:flags:removability:completion:]"
+ "-[IXSAppUninstaller _finalDeletionPromptWithRecord:identity:clientName:flags:removability:completion:]_block_invoke"
+ "-[IXSAppUninstaller _promptForMoveOrDeleteAppRecord:identity:clientName:flags:completion:removability:]"
+ "-[IXSAppUninstaller _promptForMoveOrDeleteAppRecord:identity:clientName:flags:completion:removability:]_block_invoke"
+ "-[IXSAppUpdateScheduler _onQueue_invokeInstallerForTask:]"
+ "-[IXSAppUpdateScheduler _scheduleNextTask]_block_invoke"
+ "-[IXSDefaultAppDeletionManager _shouldGateDeletionForAppType:]"
+ "-[IXSDefaultAppDownloadAlert openDefaultAppStoreWithError:]"
+ "-[IXSDefaultAppDownloadAlert openDefaultAppStoreWithError:]_block_invoke"
+ "-[IXSDefaultAppSelectAlert openSettingsWithBundleID:]"
+ "-[IXSRemoteDeletionPromptManager iCloudIsEnabledForMessages]"
+ "-[IXSRemoteDeletionPromptManager iCloudIsEnabledForPhotos]"
+ "-[IXSRemoteDeletionPromptManager isValidBundleIDForRemoteAlert:withAppType:]"
+ "-[IXSRemoteDeletionPromptManager sharedMediaInMessagesCount]"
+ "-[IXSUninstallAlert initWithAppRecord:bundleIdentifier:removability:deletionIsRestricted:]"
+ "10:20:08"
+ "@48@0:8@16@24Q32B40B44"
+ "App Marketplace Required"
+ "At least one app marketplace is required on this iPhone."
+ "At least one browser app is required on this iPhone."
+ "At least one messaging app is required on this iPhone."
+ "B24@0:8Q16"
+ "B32@0:8@16^Q24"
+ "DEFAULT_APP_CONTACTLESS_SELECT_DELETE_APP_TITLE"
+ "DEFAULT_APP_DOWNLOAD_APP_MARKETPLACE_BODY_FIRST"
+ "DEFAULT_APP_DOWNLOAD_APP_MARKETPLACE_BODY_SECOND"
+ "DEFAULT_APP_DOWNLOAD_BROWSER_APP_BODY_FIRST"
+ "DEFAULT_APP_DOWNLOAD_BROWSER_APP_BODY_SECOND"
+ "DEFAULT_APP_DOWNLOAD_MESSAGING_APP_BODY_FIRST"
+ "DEFAULT_APP_DOWNLOAD_MESSAGING_APP_BODY_SECOND"
+ "DEFAULT_APP_MAIL_SELECT_DELETE_APP_TITLE"
+ "DEFAULT_APP_NOT_AVAILABLE_DELETE_APP_OPEN_APP_STORE"
+ "DEFAULT_APP_PHONE_SELECT_DELETE_APP_TITLE"
+ "DEFAULT_APP_SELECT_APP_MARKETPLACE_BODY"
+ "DEFAULT_APP_SELECT_BROWSER_APP_BODY"
+ "DEFAULT_APP_SELECT_CONTACTLESS_APP_BODY"
+ "DEFAULT_APP_SELECT_MAIL_APP_BODY"
+ "DEFAULT_APP_SELECT_MESSAGING_APP_BODY"
+ "DEFAULT_APP_SELECT_PHONE_APP_BODY"
+ "Default Messaging App Required"
+ "Deleting this app will not delete your photos and videos on this iPhone or any stored in iCloud."
+ "Deleting this app will not delete your photos and videos on this iPhone."
+ "DeviceClass"
+ "Failed to open default app marketplace"
+ "Oct 26 2024"
+ "Open App Store"
+ "Select Another Default Calling App"
+ "Select Another Default Contactless App"
+ "Select Another Default Mail App"
+ "Select Another Default Messaging App"
+ "Select Default App Marketplace"
+ "Select Default Browser App"
+ "T@?,C,N,V_schedulerCallback"
+ "TB,N,V_isPreferredButton"
+ "TB,N,V_scheduledInstallIsRunning"
+ "TB,R,N,V_deletionIsRestricted"
+ "UNINSTALL_ICON_BODY_DELETE_DATA_APPSTORE_EIGHT"
+ "UNINSTALL_ICON_BODY_DELETE_DATA_APPSTORE_FIVE"
+ "UNINSTALL_ICON_BODY_DELETE_DATA_APPSTORE_FOUR"
+ "UNINSTALL_ICON_BODY_DELETE_DATA_APPSTORE_NINE"
+ "UNINSTALL_ICON_BODY_DELETE_DATA_APPSTORE_ONE"
+ "UNINSTALL_ICON_BODY_DELETE_DATA_APPSTORE_SEVEN"
+ "UNINSTALL_ICON_BODY_DELETE_DATA_APPSTORE_SIX"
+ "UNINSTALL_ICON_BODY_DELETE_DATA_APPSTORE_THREE"
+ "UNINSTALL_ICON_BODY_DELETE_DATA_APPSTORE_TWO"
+ "UNINSTALL_ICON_BODY_DELETE_DATA_MESSAGES_SECOND_EIGHT"
+ "UNINSTALL_ICON_BODY_DELETE_DATA_MESSAGES_SECOND_FIVE"
+ "UNINSTALL_ICON_BODY_DELETE_DATA_MESSAGES_SECOND_FOUR"
+ "UNINSTALL_ICON_BODY_DELETE_DATA_MESSAGES_SECOND_NINE"
+ "UNINSTALL_ICON_BODY_DELETE_DATA_MESSAGES_SECOND_ONE"
+ "UNINSTALL_ICON_BODY_DELETE_DATA_MESSAGES_SECOND_SEVEN"
+ "UNINSTALL_ICON_BODY_DELETE_DATA_MESSAGES_SECOND_SIX"
+ "UNINSTALL_ICON_BODY_DELETE_DATA_MESSAGES_SECOND_THREE"
+ "UNINSTALL_ICON_BODY_DELETE_DATA_MESSAGES_SECOND_TWO"
+ "UNINSTALL_ICON_BODY_DELETE_DATA_MESSAGES_SECOND_WITHOUT_ICLOUD_EIGHT"
+ "UNINSTALL_ICON_BODY_DELETE_DATA_MESSAGES_SECOND_WITHOUT_ICLOUD_FIVE"
+ "UNINSTALL_ICON_BODY_DELETE_DATA_MESSAGES_SECOND_WITHOUT_ICLOUD_FOUR"
+ "UNINSTALL_ICON_BODY_DELETE_DATA_MESSAGES_SECOND_WITHOUT_ICLOUD_NINE"
+ "UNINSTALL_ICON_BODY_DELETE_DATA_MESSAGES_SECOND_WITHOUT_ICLOUD_ONE"
+ "UNINSTALL_ICON_BODY_DELETE_DATA_MESSAGES_SECOND_WITHOUT_ICLOUD_SEVEN"
+ "UNINSTALL_ICON_BODY_DELETE_DATA_MESSAGES_SECOND_WITHOUT_ICLOUD_SIX"
+ "UNINSTALL_ICON_BODY_DELETE_DATA_MESSAGES_SECOND_WITHOUT_ICLOUD_THREE"
+ "UNINSTALL_ICON_BODY_DELETE_DATA_MESSAGES_SECOND_WITHOUT_ICLOUD_TWO"
+ "UNINSTALL_ICON_BODY_DELETE_DATA_PHOTOS"
+ "UNINSTALL_ICON_BODY_DELETE_DATA_PHOTOS_WITHOUT_ICLOUD"
+ "URLQueryAllowedCharacterSet"
+ "_customDeleteStringForAppMarketplace"
+ "_customDeleteStringForMessagesApp"
+ "_deletionIsRestricted"
+ "_displayAuthenticationErrorForApp:"
+ "_finalDeletionPromptWithRecord:identity:clientName:flags:removability:completion:"
+ "_isPreferredButton"
+ "_onQueue_acquireAssertionForPlaceholder:"
+ "_onQueue_invokeInstallerForTask:"
+ "_promptForMoveOrDeleteAppRecord:identity:clientName:flags:completion:removability:"
+ "_scheduleNextTask"
+ "_scheduledInstallIsRunning"
+ "_schedulerCallback"
+ "_shouldGateDeletionForAppType:"
+ "app-prefs:%!@(MISSING)&target=com.apple.settings.default-applications"
+ "bundleId"
+ "contextWithBundleId:onChange:"
+ "defaultAppCandidates"
+ "deletionIsRestricted"
+ "effectiveBoolValueForSetting:"
+ "getDefaultNFCApplication"
+ "iPad"
+ "initWithAppRecord:bundleIdentifier:removability:deletionIsRestricted:"
+ "initWithAppRecord:bundleIdentifier:removability:isManagedByManagedSettings:deletionIsRestricted:"
+ "installedAppsFromAppMarketplaceWithBundleID:"
+ "isDeviceBasedVPP"
+ "isPreferredButton"
+ "isValidBundleIDForRemoteAlert:withAppType:"
+ "isiPad"
+ "managedAppBundleIDs"
+ "openDefaultAppStoreWithError:"
+ "openSettingsWithBundleID:"
+ "scheduledAppUpdateReadyToExecuteAndRunBlockWhenComplete:"
+ "scheduledInstallIsRunning"
+ "schedulerCallback"
+ "setIsPreferredButton:"
+ "setScheduledInstallIsRunning:"
+ "setSchedulerCallback:"
+ "stringByAddingPercentEncodingWithAllowedCharacters:"
+ "v24@0:8@?<v@?>16"
- "\x02\x11"
- "\"\x17S!\x15\x19!\x13\x16!"
- "%!s(MISSING): %!@(MISSING) cannot be uninstalled: deletableAccordingToLS:%!c(MISSING) ignoreRestrictions:%!c(MISSING) hasBundleContainer:%!c(MISSING)"
- "%!s(MISSING): Acquiring termination assertion (if needed) to install %!@(MISSING)"
- "%!s(MISSING): Acquiring termination assertion (if needed) to install placeholder for %!@(MISSING)"
- "%!s(MISSING): Auth was unsuccessful. Error: %!@(MISSING)"
- "%!s(MISSING): Developer install - not acquiring termination assertion to install %!@(MISSING)"
- "%!s(MISSING): Developer install - not acquiring termination assertion to install placeholder for %!@(MISSING)"
- "%!s(MISSING): Failed to create app unlock alert for app with bundle ID %!@(MISSING) : %!@(MISSING)"
- "-[IXSAppUninstallAlert initWithAppRecord:bundleIdentifier:removability:isManagedByManagedSettings:]"
- "-[IXSAppUninstaller _displayAuthenticationError]_block_invoke"
- "-[IXSAppUninstaller _finalDeletionPromptWithRecord:identity:clientName:flags:completion:removability:]"
- "-[IXSAppUninstaller _finalDeletionPromptWithRecord:identity:clientName:flags:completion:removability:]_block_invoke"
- "-[IXSAppUninstaller _promptForUnlockOfAppRecord:identity:clientName:flags:completion:removability:]_block_invoke"
- "-[IXSAppUninstaller _promptForUnlockOfAppRecord:identity:clientName:flags:completion:removability:]_block_invoke_2"
- "-[IXSAppUninstaller _uninstallAppWithRecord:identity:clientName:flags:removability:completion:]_block_invoke"
- "-[IXSAppUpdateScheduler invokeInstallerForTask:]"
- "-[IXSAppUpdateScheduler scheduleNextTask]_block_invoke"
- "-[IXSDefaultAppSelectAlert openSettings]"
- "-[IXSUninstallAlert initWithAppRecord:bundleIdentifier:removability:]"
- "10:45:15"
- "@40@0:8@16@24Q32"
- "AUTHENTICATE"
- "At least one %!@(MISSING) is required on this iPhone."
- "Authenticate"
- "Authenticate To Delete \"%!@(MISSING)\""
- "Authentication is required to delete this app."
- "DEFAULT_APP_APP_MARKETPLACE"
- "DEFAULT_APP_BROWSER_APP"
- "DEFAULT_APP_MESSAGING_APP"
- "DEFAULT_APP_NOT_AVAILABLE_DELETE_APP_BODY_FIRST"
- "DEFAULT_APP_NOT_AVAILABLE_DELETE_APP_BODY_SECOND"
- "DEFAULT_APP_SELECT_DELETE_APP_BODY"
- "Deleting this app will prevent %!l(MISSING)u other apps from receiving future software updates. These apps will not be updated by another app marketplace."
- "Download App Marketplace"
- "Download Messaging App"
- "Failed to create app unlock alert for app with bundle ID %!@(MISSING)"
- "IXSAppUnlockAlert"
- "Oct 16 2024"
- "Select Another Default"
- "Select Default Browser"
- "_displayAuthenticationError"
- "_finalDeletionPromptWithRecord:identity:clientName:flags:completion:removability:"
- "_onQueue_acquireAssertionIfNeededForPlaceholder:"
- "app marketplace"
- "appTypeForBundleID:"
- "browser app"
- "initWithAppRecord:bundleIdentifier:removability:"
- "initWithAppRecord:bundleIdentifier:removability:isManagedByManagedSettings:"
- "installedAppsFromAppStoreCount"
- "invokeInstallerForTask:"
- "isValidBundleIDForRemoteAlert:"
- "messaging app"
- "openSettings"
- "prefs:root"
- "scheduleNextTask"
- "scheduledAppUpdateReadyToExecute"

```
