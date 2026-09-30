## webbookmarksd

> `/usr/libexec/webbookmarksd`

```diff

-7621.2.5.10.10
-  __TEXT.__text: 0x1594c
-  __TEXT.__auth_stubs: 0x9b0
-  __TEXT.__objc_stubs: 0x3340
-  __TEXT.__objc_methlist: 0xbc4
+7622.1.14.10.4
+  __TEXT.__text: 0x15f78
+  __TEXT.__auth_stubs: 0x9d0
+  __TEXT.__objc_stubs: 0x34a0
+  __TEXT.__objc_methlist: 0xbdc
   __TEXT.__const: 0xb8
-  __TEXT.__gcc_except_tab: 0x5b0
-  __TEXT.__objc_methname: 0x3ef5
-  __TEXT.__cstring: 0xd08
-  __TEXT.__oslogstring: 0x200c
+  __TEXT.__gcc_except_tab: 0x5d8
+  __TEXT.__objc_methname: 0x406c
+  __TEXT.__cstring: 0xe36
+  __TEXT.__oslogstring: 0x2055
   __TEXT.__objc_classname: 0x271
-  __TEXT.__objc_methtype: 0x614
-  __TEXT.__unwind_info: 0x650
-  __DATA_CONST.__auth_got: 0x4f0
-  __DATA_CONST.__got: 0x620
-  __DATA_CONST.__const: 0x11d8
-  __DATA_CONST.__cfstring: 0x5a0
+  __TEXT.__objc_methtype: 0x62a
+  __TEXT.__unwind_info: 0x670
+  __DATA_CONST.__auth_got: 0x500
+  __DATA_CONST.__got: 0x680
+  __DATA_CONST.__const: 0x1218
+  __DATA_CONST.__cfstring: 0x600
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA.__objc_const: 0x1120
-  __DATA.__objc_selrefs: 0xf60
+  __DATA.__objc_selrefs: 0xfb8
   __DATA.__objc_ivar: 0xa4
   __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x368
   __DATA.__bss: 0x178
   - /System/Library/Frameworks/Accounts.framework/Accounts
+  - /System/Library/Frameworks/BrowserEngineCore.framework/BrowserEngineCore
+  - /System/Library/Frameworks/BrowserEngineKit.framework/BrowserEngineKit
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete
+  - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
+  - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/MobileInstallation.framework/MobileInstallation
   - /System/Library/PrivateFrameworks/MobileSafari.framework/MobileSafari
+  - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SafariCore.framework/SafariCore
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/WebBookmarks.framework/WebBookmarks

   - /usr/lib/libc++.1.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 69658AAD-923D-396A-9AC8-4E42861DE17F
-  Functions: 478
-  Symbols:   365
-  CStrings:  945
+  UUID: F3778C17-65CF-33C3-A81F-5C7AFE441FBC
+  Functions: 484
+  Symbols:   379
+  CStrings:  967
 
Symbols:
+ _FBSSceneVisibilityEndowmentNamespace
+ _MCEffectiveSettingsChangedNotification
+ _OBJC_CLASS_$_RBSProcessHandle
+ _OBJC_CLASS_$_RBSProcessIdentifier
+ _OBJC_CLASS_$_WBSFeatureAvailability
+ _WebBookmarksDidReloadDistributedNotification
+ __BEBrowserEngineEntitlementHost
+ __BECheckEntitlmentForAuditToken
+ _kWebBookmarksOpenSafariExportSettings
+ _kWebBookmarksOpenSafariExportSettingsFailedKey
+ _kWebBookmarksOpenSafariExportSettingsMissingEntitlementKey
+ _kWebBookmarksOpenSafariExportSettingsNotRunningForegroundKey
+ _kWebBookmarksOpenSafariExportSettingsTestingModeKey
+ _xpc_connection_get_audit_token
CStrings:
+ "XPC connection must have either the %{public}@ or %{public}@ entitlement"
+ "_connection:openSafariExportSettingsWithMessage:"
+ "addObserverForName:object:queue:usingBlock:"
+ "addVisitWithURLString:visitTime:title:loadSuccessful:httpGet:redirectSourceURLString:redirectSourceVisitTime:redirectDestinationURLString:redirectDestinationVisitTime:visitCount:"
+ "clientIsDefaultBrowserEntitledWithConnection:message:"
+ "com.apple.developer.web-browser"
+ "com.apple.private.webbookmarks.appmigration"
+ "com.apple.safari.history.export"
+ "com.apple.safari.history.get-number-of-sites"
+ "com.apple.safari.history.import"
+ "currentState"
+ "endowmentNamespaces"
+ "handleForIdentifier:error:"
+ "identifierWithPid:"
+ "isApplication"
+ "isInternalInstall"
+ "openSensitiveURL:withOptions:"
+ "postNotificationName:object:"
+ "settings-navigation://com.apple.Settings.Apps/com.apple.mobilesafari?action=showExportSheet"
+ "v16@?0@\"NSNotification\"8"
+ "v88@0:8@\"NSString\"16d24@\"NSString\"32B40B44@\"NSString\"48d56@\"NSString\"64d72Q80"
+ "v88@0:8@16d24@32B40B44@48d56@64d72Q80"
- "addVisitWithURLString:visitTime:title:loadSuccessful:httpGet:redirectSourceURLString:redirectSourceVisitTime:visitCount:"
- "v72@0:8@\"NSString\"16d24@\"NSString\"32B40B44@\"NSString\"48d56Q64"
- "v72@0:8@16d24@32B40B44@48d56Q64"

```
