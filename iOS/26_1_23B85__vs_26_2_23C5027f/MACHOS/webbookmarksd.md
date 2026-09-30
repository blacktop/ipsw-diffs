## webbookmarksd

> `/usr/libexec/webbookmarksd`

```diff

-7622.2.11.10.8
-  __TEXT.__text: 0x168c4
-  __TEXT.__auth_stubs: 0x9e0
-  __TEXT.__objc_stubs: 0x3640
-  __TEXT.__objc_methlist: 0xbdc
+7623.1.12.10.4
+  __TEXT.__text: 0x16e90
+  __TEXT.__auth_stubs: 0xab0
+  __TEXT.__objc_stubs: 0x3920
+  __TEXT.__objc_methlist: 0xc64
   __TEXT.__const: 0xe0
-  __TEXT.__gcc_except_tab: 0x5d8
-  __TEXT.__objc_methname: 0x416a
-  __TEXT.__cstring: 0xe2f
+  __TEXT.__gcc_except_tab: 0x5f0
+  __TEXT.__objc_methname: 0x44a5
+  __TEXT.__cstring: 0xe92
   __TEXT.__oslogstring: 0x228d
   __TEXT.__objc_classname: 0x274
-  __TEXT.__objc_methtype: 0x659
-  __TEXT.__unwind_info: 0x690
-  __DATA_CONST.__auth_got: 0x508
-  __DATA_CONST.__got: 0x6a0
-  __DATA_CONST.__const: 0x1260
-  __DATA_CONST.__cfstring: 0x620
+  __TEXT.__objc_methtype: 0x689
+  __TEXT.__unwind_info: 0x6c8
+  __DATA_CONST.__auth_got: 0x570
+  __DATA_CONST.__got: 0x700
+  __DATA_CONST.__const: 0x1170
+  __DATA_CONST.__cfstring: 0x6a0
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x50
+  __DATA_CONST.__objc_intobj: 0x30
+  __DATA_CONST.__objc_arraydata: 0x10
+  __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x10d0
-  __DATA.__objc_selrefs: 0x1018
+  __DATA.__objc_selrefs: 0x10d0
   __DATA.__objc_ivar: 0x9c
   __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x368
-  __DATA.__bss: 0x178
+  __DATA.__bss: 0xe8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/BrowserEngineCore.framework/BrowserEngineCore
   - /System/Library/Frameworks/BrowserEngineKit.framework/BrowserEngineKit
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
+  - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
+  - /System/Library/Frameworks/ExtensionKit.framework/ExtensionKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore
   - /System/Library/Frameworks/SafariServices.framework/SafariServices

   - /usr/lib/libc++.1.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8914D74D-DD9F-36A3-AC8D-FFCED4B0AC8A
-  Functions: 492
-  Symbols:   384
-  CStrings:  990
+  UUID: FF48FAFA-1571-378D-9726-C052E67B1D0D
+  Functions: 474
+  Symbols:   411
+  CStrings:  1015
 
Symbols:
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSExtension
+ _OBJC_CLASS_$_SFExtensionsProfilesDataSource
+ _OBJC_CLASS_$_WBSExtensionsController
+ _OBJC_CLASS_$_WBTabGroupManager
+ _OBJC_CLASS_$__EXQueryController
+ _WBSOSLogBackup
+ _WBSOSLogBookmarks
+ _WBSOSLogCloudHistory
+ _WBSOSLogCloudTabs
+ _WBSOSLogExport
+ _WBSOSLogHistory
+ _WBSOSLogImport
+ _WBSOSLogOther
+ _WBSOSLogPasswordsIcons
+ _WBSOSLogReadingList
+ _WBSOSLogSafariDeletion
+ _WBSOSLogWebsiteData
+ _kWebBookmarksExtensionEnabledKey
+ _kWebBookmarksExtensionIdentifiersKey
+ _kWebBookmarksGetExtensionEnabledState
+ _kWebBookmarksNoExtensionFoundKey
+ _kWebBookmarksOpenSafariWebExtensionsSettings
+ _kWebBookmarksSFSafariSettingsCallingAppBundleIDKey
+ _kWebBookmarksSFSafariSettingsFailedKey
+ _kWebBookmarksSFSafariSettingsMissingEntitlementKey
+ _kWebBookmarksSFSafariSettingsNotRunningForegroundKey
+ _kWebBookmarksSFSafariSettingsTestingModeKey
+ _objc_retain_x5
+ _xpc_dictionary_get_array
- _kWebBookmarksOpenSafariExportSettingsFailedKey
- _kWebBookmarksOpenSafariExportSettingsMissingEntitlementKey
- _kWebBookmarksOpenSafariExportSettingsNotRunningForegroundKey
- _kWebBookmarksOpenSafariExportSettingsTestingModeKey
- _os_log_create
CStrings:
+ "#%@"
+ "@32@0:8@16@24"
+ "@40@0:8@16@24@32"
+ "B16@?0@\"SFWebExtensionsController\"8"
+ "B16@?0@\"_EXExtensionIdentity\"8"
+ "B40@0:8@16@24@32"
+ "_allWebExtensionsControllers"
+ "_callingApplicationIsForegroundWithHandle:connection:message:"
+ "_clientIsDefaultBrowserEntitledWithConnection:message:"
+ "_connection:getEnabledStateForExtensionWithMessage:"
+ "_connection:openSafariWebExtensionsSettingsWithMessage:"
+ "_extensionWithIdentifier:connection:message:"
+ "_extensionsProfilesDataSource"
+ "_handleForCallingProcessWithConnection:message:"
+ "_openSenstiveURL:withOptions:connection:message:"
+ "_tabCollection"
+ "_tabGroupManager"
+ "_webExtensionsSettingsURLWithConnection:message:"
+ "arrayWithObjects:count:"
+ "com.apple.Safari.content-blocker"
+ "com.apple.Safari.web-extension"
+ "containingBundleRecord"
+ "executeQueries:"
+ "extensionIsEnabled:"
+ "extensionKitQueriesWithExtensionPoint:platforms:predicate:"
+ "extensionWithIdentity:error:"
+ "i"
+ "initWithCollection:"
+ "initWithTabGroupManager:shouldDiscoverExtensions:"
+ "profileServerIDToWebExtensionsControllers"
+ "reloadExtensionStateFromStorage"
+ "safari_containsObjectPassingTest:"
+ "settings-navigation://com.apple.Settings.Apps/com.apple.mobilesafari/WEB_EXTENSIONS"
+ "stringByAppendingFormat:"
- "Backup"
- "Bookmarks"
- "CloudHistory"
- "CloudTabs"
- "Export"
- "History"
- "Import"
- "Other"
- "PasswordsIcons"
- "ReadingList"
- "SafariDeletion"
- "WebsiteData"
- "clientIsDefaultBrowserEntitledWithConnection:message:"

```
