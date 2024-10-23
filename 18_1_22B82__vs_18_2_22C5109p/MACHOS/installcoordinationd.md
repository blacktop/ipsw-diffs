## installcoordinationd

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordinationd`

```diff

-628.40.3.0.0
-  __TEXT.__text: 0x8d308
-  __TEXT.__auth_stubs: 0xf50
-  __TEXT.__objc_stubs: 0x9700
-  __TEXT.__objc_methlist: 0x4638
+631.60.23.502.2
+  __TEXT.__text: 0x9226c
+  __TEXT.__auth_stubs: 0x1050
+  __TEXT.__objc_stubs: 0x9f20
+  __TEXT.__objc_methlist: 0x4988
   __TEXT.__const: 0x1a8
-  __TEXT.__cstring: 0x14e6c
-  __TEXT.__objc_classname: 0x8a7
-  __TEXT.__oslogstring: 0xc251
-  __TEXT.__objc_methtype: 0x201b
-  __TEXT.__objc_methname: 0xe973
-  __TEXT.__gcc_except_tab: 0x27e0
-  __TEXT.__ustring: 0x26c
+  __TEXT.__cstring: 0x15db5
+  __TEXT.__objc_classname: 0x957
+  __TEXT.__oslogstring: 0xc961
+  __TEXT.__objc_methtype: 0x2100
+  __TEXT.__objc_methname: 0xf3f3
+  __TEXT.__gcc_except_tab: 0x28a4
+  __TEXT.__ustring: 0x580
   __TEXT.__dlopen_cstrs: 0x68
-  __TEXT.__unwind_info: 0x20b0
-  __DATA_CONST.__auth_got: 0x7b8
-  __DATA_CONST.__got: 0x3b0
+  __TEXT.__unwind_info: 0x21c8
+  __DATA_CONST.__auth_got: 0x838
+  __DATA_CONST.__got: 0x3f0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x2610
-  __DATA_CONST.__cfstring: 0x7d60
-  __DATA_CONST.__objc_classlist: 0x1f8
+  __DATA_CONST.__const: 0x27c8
+  __DATA_CONST.__cfstring: 0x8580
+  __DATA_CONST.__objc_classlist: 0x220
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x78
+  __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x1a8
-  __DATA_CONST.__objc_intobj: 0x108
-  __DATA_CONST.__objc_arraydata: 0x40
+  __DATA_CONST.__objc_superrefs: 0x1c8
+  __DATA_CONST.__objc_intobj: 0x150
+  __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0xbf90
-  __DATA.__objc_selrefs: 0x2c20
-  __DATA.__objc_ivar: 0x40c
-  __DATA.__objc_data: 0x13b0
-  __DATA.__data: 0x5f0
+  __DATA_CONST.__objc_dictobj: 0x28
+  __DATA.__objc_const: 0xc7e0
+  __DATA.__objc_selrefs: 0x2e38
+  __DATA.__objc_ivar: 0x42c
+  __DATA.__objc_data: 0x1540
+  __DATA.__data: 0x650
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x1e0
+  __DATA.__bss: 0x238
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2845
-  Symbols:   377
-  CStrings:  4808
+  Functions: 2956
+  Symbols:   402
+  CStrings:  5021
 
Symbols:
+ _LSDefaultAppCategoryForMask
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_RBSProcessIdentity
+ _OBJC_CLASS_$_SBSRemoteAlertActivationContext
+ _OBJC_CLASS_$_SBSRemoteAlertConfigurationContext
+ _OBJC_CLASS_$_SBSRemoteAlertDefinition
+ _OBJC_CLASS_$_SBSRemoteAlertHandle
+ __xpc_type_connection
+ __xpc_type_dictionary
+ __xpc_type_error
+ _os_eligibility_get_domain_answer
+ _xpc_bool_create
+ _xpc_bool_get_value
+ _xpc_connection_activate
+ _xpc_connection_cancel
+ _xpc_connection_create
+ _xpc_connection_send_message
+ _xpc_connection_set_event_handler
+ _xpc_connection_set_target_queue
+ _xpc_copy_description
+ _xpc_dictionary_create
+ _xpc_dictionary_get_value
+ _xpc_endpoint_create
+ _xpc_get_type
+ _xpc_int64_get_value
CStrings:
+ "\x12"
+ "\x12\""
+ "%!@(MISSING)\n\n%!@(MISSING)"
+ "%!@(MISSING) %!@(MISSING)"
+ "%!s(MISSING): Client %!@(MISSING) attempted to set MIInstallOptions with the installationRequestorAuditToken property set, but did not have the required entitlement. : %!@(MISSING)"
+ "%!s(MISSING): Deletion UI host app %!@(MISSING) is not installed so we can't show a deletion prompt for %!@(MISSING)"
+ "%!s(MISSING): Failed to construct alert relevant data : %!@(MISSING)"
+ "%!s(MISSING): Failed to dismiss remote alert; no serviceConnection found"
+ "%!s(MISSING): Failed to find SAD App Type for bundleID %!@(MISSING)"
+ "%!s(MISSING): Failed to find default app categories applicable to bundleID %!@(MISSING) : %!@(MISSING)"
+ "%!s(MISSING): Failed to get list of preferred app marketplaces : %!@(MISSING)"
+ "%!s(MISSING): Failed to identify sheet disposition from user response : %!@(MISSING)"
+ "%!s(MISSING): Failed to load expected classes from IMCore.framework: CloudKitHooks : %!p(MISSING)"
+ "%!s(MISSING): Failed to load expected classes from Photos.framework: PHPhotoLibrary : %!p(MISSING), PHAsset : %!p(MISSING)"
+ "%!s(MISSING): Failed to open IMCore framework: %!s(MISSING)"
+ "%!s(MISSING): Failed to open Photos framework: %!s(MISSING)"
+ "%!s(MISSING): Failed to open settings pane; unknown app type encountered"
+ "%!s(MISSING): Failed to resolve persona for %!@(MISSING) : %!@(MISSING). Skipping without setting conditional removability"
+ "%!s(MISSING): Found invalid LS category for default app type %!l(MISSING)u : %!@(MISSING)"
+ "%!s(MISSING): Found unknown app category for bundleID %!@(MISSING); assuming default app alerts aren't required and allowing deletion"
+ "%!s(MISSING): Found unknown default app type : %!@(MISSING)"
+ "%!s(MISSING): Got XPC error on listenerConnection handler: %!@(MISSING)"
+ "%!s(MISSING): Got XPC error on serviceConnection handler: %!@(MISSING)"
+ "%!s(MISSING): Got buttonClicked: %!l(MISSING)u"
+ "%!s(MISSING): Got connection from service"
+ "%!s(MISSING): Got unknown XPC event on listenerConnection handler: %!s(MISSING)"
+ "%!s(MISSING): Got unknown XPC event on serviceConnection handler: %!s(MISSING)"
+ "%!s(MISSING): No LSApplicationRecord found for %!@(MISSING), assuming uninstalled, skipping"
+ "%!s(MISSING): Processed eligibility change : %!@(MISSING)"
+ "%!s(MISSING): Received object from service connection"
+ "%!s(MISSING): Setting IXAppRemovability to %!@(MISSING) for %!@(MISSING)"
+ "%!s(MISSING): Unable to query eligibility deletion for domain %!l(MISSING)lu : %!s(MISSING)"
+ "%!s(MISSING): Unable to set IXAppRemovability for %!@(MISSING) to %!@(MISSING): %!@(MISSING)"
+ "+[IXSRemoteDeletionPromptManager sharedInstance]_block_invoke"
+ "-[IXSAppDeletionEligibilityManager _domainToAppIdentitySetMap]"
+ "-[IXSAppDeletionEligibilityManager _eligibilityAnswerForDomain:]"
+ "-[IXSAppDeletionEligibilityManager _onQueue_processEligibilityDomainChange]"
+ "-[IXSAppDeletionEligibilityManager _onQueue_setAppRemovabilityForSystemAppPlaceholder:]"
+ "-[IXSAppDeletionEligibilityManager _onQueue_setRemovabilityForAppWithIdentity:usingEligibilityAnswer:]"
+ "-[IXSAppDeletionEligibilityManager _onQueue_updateRemovabilityForAppIdentities:usingEligibilityAnswer:]_block_invoke"
+ "-[IXSAppUninstallAlert initWithAppRecord:bundleIdentifier:removability:isManagedByManagedSettings:]"
+ "-[IXSAppUninstaller _finalDeletionPromptWithRecord:identity:clientName:flags:completion:removability:]"
+ "-[IXSAppUninstaller _finalDeletionPromptWithRecord:identity:clientName:flags:completion:removability:]_block_invoke"
+ "-[IXSAppUninstaller _promptForDeletionWithRecord:identity:clientName:flags:completion:removability:]"
+ "-[IXSAppUninstaller _promptForDeletionWithRecord:identity:clientName:flags:completion:removability:]_block_invoke"
+ "-[IXSAppUninstaller _promptForGatingDefaultAppDeletionWithRecord:identity:clientName:flags:removability:completion:]_block_invoke"
+ "-[IXSAppUninstaller _promptForUnlockOfAppRecord:identity:clientName:flags:completion:removability:]"
+ "-[IXSAppUninstaller _promptForUnlockOfAppRecord:identity:clientName:flags:completion:removability:]_block_invoke"
+ "-[IXSAppUninstaller _promptForUnlockOfAppRecord:identity:clientName:flags:completion:removability:]_block_invoke_2"
+ "-[IXSAppUninstaller _uninstallAppWithRecord:identity:clientName:flags:removability:completion:]"
+ "-[IXSAppUninstaller _uninstallAppWithRecord:identity:clientName:flags:removability:completion:]_block_invoke"
+ "-[IXSDefaultAppDeletionManager getAppRecordNeedsDefaultAppDeletionAlert:forRecord:defaultAppType:error:]"
+ "-[IXSDefaultAppDeletionManager getOtherAppsAreInstalled:forDefaultAppType:exceptBundleID:error:]"
+ "-[IXSDefaultAppSelectAlert openSettings]"
+ "-[IXSRemoteDeletionPromptManager _constructRelevantAppData:]"
+ "-[IXSRemoteDeletionPromptManager dismissRemoteAlert]"
+ "-[IXSRemoteDeletionPromptManager displayDeletionAlertForRecord:completion:]"
+ "-[IXSRemoteDeletionPromptManager displayDeletionAlertForRecord:completion:]_block_invoke"
+ "-[IXSUninstallAlert initWithAppRecord:bundleIdentifier:removability:]"
+ "/System/Library/Frameworks/Photos.framework/Photos"
+ "/System/Library/PrivateFrameworks/IMCore.framework/IMCore"
+ "10:45:15"
+ "@\"NSObject<OS_xpc_object>\""
+ "@\"SBSRemoteAlertHandle\""
+ "@40@0:8@16@24Q32"
+ "@40@0:8@16Q24Q32"
+ "@44@0:8@16@24Q32B40"
+ "AppDeletionUI"
+ "At least one %!@(MISSING) is required on this iPhone."
+ "B48@0:8^B16@24^Q32^@40"
+ "B48@0:8^B16Q24@32^@40"
+ "Client %!@(MISSING) attempted to set MIInstallOptions with the installationRequestorAuditToken property set, but did not have the required entitlement."
+ "DEFAULT_APP_APPSTORE_NOT_AVAILABLE_DELETE_APP_TITLE"
+ "DEFAULT_APP_APPSTORE_SELECT_DELETE_APP_TITLE"
+ "DEFAULT_APP_APP_MARKETPLACE"
+ "DEFAULT_APP_BROWSER_APP"
+ "DEFAULT_APP_MESSAGES_SELECT_DELETE_APP_TITLE"
+ "DEFAULT_APP_MESSAGING_APP"
+ "DEFAULT_APP_MESSAGING_NOT_AVAILABLE_DELETE_APP_TITLE"
+ "DEFAULT_APP_NOT_AVAILABLE_DELETE_APP_BODY_FIRST"
+ "DEFAULT_APP_NOT_AVAILABLE_DELETE_APP_BODY_SECOND"
+ "DEFAULT_APP_NOT_AVAILABLE_DELETE_APP_DISMISS"
+ "DEFAULT_APP_SAFARI_NOT_AVAILABLE_DELETE_APP_TITLE"
+ "DEFAULT_APP_SAFARI_SELECT_DELETE_APP_TITLE"
+ "DEFAULT_APP_SELECT_DELETE_APP_BODY"
+ "DEFAULT_APP_SELECT_DELETE_APP_OPEN_SETTINGS"
+ "Deleting this app will not delete your messages stored in iCloud."
+ "Deleting this app will prevent %!l(MISSING)u other apps from receiving future software updates. These apps will not be updated by another app marketplace."
+ "Download App Marketplace"
+ "Download Browser App"
+ "Download Default App"
+ "Download Messaging App"
+ "Eligibility"
+ "Failed to construct alert relevant data"
+ "Failed to find default app categories applicable to bundleID %!@(MISSING)"
+ "Failed to get list of preferred app marketplaces"
+ "Failed to identify sheet disposition from user response"
+ "Found invalid LS category for default app type %!l(MISSING)u"
+ "Found unknown default app type"
+ "Go to Settings"
+ "IMCloudKitHooks"
+ "IXSAppDeletionEligibilityManager"
+ "IXSDefaultAppDeletionManager"
+ "IXSDefaultAppDownloadAlert"
+ "IXSDefaultAppSelectAlert"
+ "IXSRemoteDeletionPromptManager"
+ "IsICloudOn"
+ "NumAppsInstalled"
+ "Oct 16 2024"
+ "PHAsset"
+ "PHPhotoLibrary"
+ "PPBundleMetadata"
+ "Q24@0:8Q16"
+ "RelevantAppData"
+ "SADAppType"
+ "SBSRemoteAlertHandleObserver"
+ "Select Another Default"
+ "Select Default App"
+ "Select Default Browser"
+ "SharedMedia"
+ "T@\"NSMutableDictionary\",&,N,V_domainToEligibilityAnswerMap"
+ "T@\"NSObject<OS_xpc_object>\",&,N,V_serviceConnection"
+ "T@\"SBSRemoteAlertHandle\",&,N,V_alertHandle"
+ "TB,N,V_lastDismissWasSwipeDown"
+ "TEST_MODE_APP_DELETION_UI_SAD_APP_TYPE_KEY"
+ "TEST_MODE_RESTRICT_DEFAULT_APP_DELETION_DEFAULT_APP_TYPE_KEY"
+ "TEST_MODE_RESTRICT_DEFAULT_APP_DELETION_OTHER_APPS_AVAILABLE_KEY"
+ "TQ,R,N,V_appRemovability"
+ "TQ,R,N,V_appType"
+ "UNINSTALL_ICON_BODY_DELETE_DATA_APPSTORE"
+ "UNINSTALL_ICON_BODY_DELETE_DATA_MESSAGES_FIRST"
+ "UNINSTALL_ICON_BODY_DELETE_DATA_MESSAGES_SECOND"
+ "UNINSTALL_ICON_BODY_DELETE_DATA_MESSAGES_SECOND_WITHOUT_ICLOUD"
+ "_alertHandle"
+ "_appRemovability"
+ "_appType"
+ "_appTypeForLSDefaultAppCategory:"
+ "_constructRelevantAppData:"
+ "_customDeleteMessageForDeletableSystemApp"
+ "_domainToAppIdentitySetMap"
+ "_domainToEligibilityAnswerMap"
+ "_eligibilityAnswerForDomain:"
+ "_finalDeletionPromptWithRecord:identity:clientName:flags:completion:removability:"
+ "_lastDismissWasSwipeDown"
+ "_lsDefaultAppCategoryForAppType:"
+ "_onQueue_enumerateSystemAppPlaceholdersAndSetAppRemovability:"
+ "_onQueue_processEligibilityDomainChange"
+ "_onQueue_setAppRemovabilityForSystemAppPlaceholder:"
+ "_onQueue_setRemovabilityForAppWithIdentity:usingEligibilityAnswer:"
+ "_onQueue_updateRemovabilityForAppIdentities:usingEligibilityAnswer:"
+ "_promptForDeletionWithRecord:identity:clientName:flags:completion:removability:"
+ "_promptForGatingDefaultAppDeletionWithRecord:identity:clientName:flags:removability:completion:"
+ "_promptForUnlockOfAppRecord:identity:clientName:flags:completion:removability:"
+ "_serviceConnection"
+ "_systemAppPlaceholderEnumerator"
+ "_testAppRemovabilityBundleID"
+ "_test_domainToEligibilityAnswerMap"
+ "_test_modifyDomainToEligibilityAnswerMap:"
+ "_uninstallAppWithRecord:identity:clientName:flags:removability:completion:"
+ "activateWithContext:"
+ "alertHandle"
+ "app marketplace"
+ "appRemovability"
+ "appType"
+ "appTypeForBundleID:"
+ "browser app"
+ "com.apple.AppDeletionUIHost"
+ "com.apple.MobileSMS"
+ "com.apple.installcoordination.AppDeletionEligibilityManager.internal"
+ "com.apple.mobileslideshow"
+ "com.apple.os-eligibility-domain.change"
+ "com.apple.private.install.can-set-install-requestor"
+ "dismiss"
+ "dismissRemoteAlert"
+ "displayDeletionAlertForRecord:completion:"
+ "distributorType"
+ "domainToEligibilityAnswerMap"
+ "eligibilityDeletionDomain"
+ "eligibilityDidChange"
+ "enumerateObjectsUsingBlock:"
+ "enumeratorForViableDefaultAppsForCategory:options:"
+ "fetchGuestAssetsWithOptions:"
+ "getAppRecordNeedsDefaultAppDeletionAlert:forRecord:defaultAppType:error:"
+ "getDefaultApplicationCategories:withCurrentDefaultApplication:error:"
+ "getOtherAppsAreInstalled:forDefaultAppType:exceptBundleID:error:"
+ "getPreferredAppMarketplacesWithError:"
+ "healthAppSupportedOnDevice"
+ "healthKitDataSupportedOnDevice"
+ "iCloudIsEnabledForMessages"
+ "iCloudIsEnabledForPhotos"
+ "identityForApplicationJobLabel:"
+ "initWithAppRecord:bundleIdentifier:removability:"
+ "initWithAppRecord:bundleIdentifier:removability:isManagedByManagedSettings:"
+ "initWithAppRecord:removability:defaultAppType:"
+ "initWithSceneProvidingProcess:configurationIdentifier:"
+ "installationRequestorAuditToken"
+ "installedAppsFromAppStoreCount"
+ "isCloudPhotoLibraryEnabled"
+ "isEnabled"
+ "isValidBundleIDForRemoteAlert:"
+ "lastDismissWasSwipeDown"
+ "librarySpecificFetchOptions"
+ "longLongValue"
+ "messaging app"
+ "newHandleWithDefinition:configurationContext:"
+ "notificationFlags"
+ "numberWithLongLong:"
+ "openSettings"
+ "prefs:root"
+ "reconcileAppRemovabilityForSystemAppPlaceholders"
+ "registerObserver:"
+ "remoteAlertHandle:didInvalidateWithError:"
+ "remoteAlertHandleDidActivate:"
+ "remoteAlertHandleDidDeactivate:"
+ "result"
+ "serviceConnection"
+ "setAlertHandle:"
+ "setDomainToEligibilityAnswerMap:"
+ "setIncludeGuestAssets:"
+ "setLastDismissWasSwipeDown:"
+ "setServiceConnection:"
+ "setUserInfo:"
+ "setXpcEndpoint:"
+ "sharedMediaInMessagesCount"
+ "sharedPhotoLibrary"
+ "systemPlaceholderEnumerator"
+ "v24@0:8@\"SBSRemoteAlertHandle\"16"
+ "v24@?0@\"IXApplicationIdentity\"8^B16"
+ "v32@0:8@\"SBSRemoteAlertHandle\"16@\"NSError\"24"
+ "v64@0:8@16@24@32Q40@?48Q56"
+ "v64@0:8@16@24@32Q40Q48@?56"
- "\x12\x12"
- "-[IXSAppUninstallAlert initWithAppRecord:bundleIdentifier:isRemovable:isManagedByManagedSettings:]"
- "-[IXSAppUninstaller _promptForDeletionWithRecord:identity:clientName:flags:completion:isRemovable:]"
- "-[IXSAppUninstaller _promptForDeletionWithRecord:identity:clientName:flags:completion:isRemovable:]_block_invoke"
- "-[IXSAppUninstaller _promptForUnlockOfAppRecord:identity:clientName:flags:completion:isRemovable:]"
- "-[IXSAppUninstaller _promptForUnlockOfAppRecord:identity:clientName:flags:completion:isRemovable:]_block_invoke"
- "-[IXSAppUninstaller _promptForUnlockOfAppRecord:identity:clientName:flags:completion:isRemovable:]_block_invoke_2"
- "-[IXSAppUninstaller _uninstallAppWithRecord:identity:clientName:flags:completion:]"
- "-[IXSAppUninstaller _uninstallAppWithRecord:identity:clientName:flags:completion:]_block_invoke"
- "-[IXSUninstallAlert initWithAppRecord:bundleIdentifier:isRemovable:]"
- "00:55:19"
- "@36@0:8@16@24B32"
- "@40@0:8@16@24B32B36"
- "Sep 29 2024"
- "_promptForDeletionWithRecord:identity:clientName:flags:completion:isRemovable:"
- "_promptForUnlockOfAppRecord:identity:clientName:flags:completion:isRemovable:"
- "_uninstallAppWithRecord:identity:clientName:flags:completion:"
- "initWithAppRecord:bundleIdentifier:isRemovable:"
- "initWithAppRecord:bundleIdentifier:isRemovable:isManagedByManagedSettings:"
- "v60@0:8@16@24@32Q40@?48B56"

```
