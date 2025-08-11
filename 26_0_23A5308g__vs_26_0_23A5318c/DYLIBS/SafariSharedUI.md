## SafariSharedUI

> `/System/Library/PrivateFrameworks/SafariSharedUI.framework/SafariSharedUI`

```diff

-622.1.21.10.3
-  __TEXT.__text: 0x108400
-  __TEXT.__auth_stubs: 0x1f70
+622.1.22.10.4
+  __TEXT.__text: 0x108150
+  __TEXT.__auth_stubs: 0x1f80
   __TEXT.__delay_stubs: 0x58
   __TEXT.__delay_helper: 0x110
-  __TEXT.__objc_methlist: 0xc3f4
+  __TEXT.__objc_methlist: 0xc3e4
   __TEXT.__const: 0x3178
-  __TEXT.__oslogstring: 0x93ed
-  __TEXT.__cstring: 0x11206
-  __TEXT.__gcc_except_tab: 0xecd4
+  __TEXT.__oslogstring: 0x934d
+  __TEXT.__cstring: 0x11196
+  __TEXT.__gcc_except_tab: 0xebf4
   __TEXT.__ustring: 0x2a20
   __TEXT.__dlopen_cstrs: 0x3b5
   __TEXT.__constg_swiftt: 0x24c

   __TEXT.__swift5_capture: 0x238
   __TEXT.__swift_as_entry: 0x3c
   __TEXT.__swift_as_ret: 0x4c
-  __TEXT.__unwind_info: 0x6d10
+  __TEXT.__unwind_info: 0x6d08
   __TEXT.__eh_frame: 0xac0
-  __TEXT.__objc_classname: 0x1f01
-  __TEXT.__objc_methname: 0x2c32a
-  __TEXT.__objc_methtype: 0x5a81
+  __TEXT.__objc_classname: 0x1f00
+  __TEXT.__objc_methname: 0x2c2e2
+  __TEXT.__objc_methtype: 0x5a6d
   __TEXT.__objc_stubs: 0x1a440
   __DATA_CONST.__got: 0x1508
   __DATA_CONST.__const: 0x6e88

   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x490
   __DATA_CONST.__objc_arraydata: 0x19f0
-  __AUTH_CONST.__auth_got: 0xfe0
-  __AUTH_CONST.__const: 0x2498
+  __AUTH_CONST.__auth_got: 0xfe8
+  __AUTH_CONST.__const: 0x2478
   __AUTH_CONST.__cfstring: 0xffa0
-  __AUTH_CONST.__objc_const: 0x15f40
+  __AUTH_CONST.__objc_const: 0x15f38
   __AUTH_CONST.__objc_intobj: 0x690
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x720
   __AUTH_CONST.__objc_dictobj: 0x1e0
   __AUTH.__objc_data: 0x3af0
   __AUTH.__data: 0x388
-  __DATA.__objc_ivar: 0xf78
-  __DATA.__data: 0x1c84
-  __DATA.__bss: 0xe68
-  __DATA.__common: 0x38
+  __DATA.__objc_ivar: 0xf74
+  __DATA.__data: 0x1c94
+  __DATA.__bss: 0xe58
+  __DATA.__common: 0x50
   __DATA_DIRTY.__objc_data: 0x370
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 08648277-ADA7-38A9-AF84-CFCF1C52CB08
-  Functions: 6128
-  Symbols:   21580
-  CStrings:  11886
+  UUID: 85DD0D9D-1734-322B-9BD3-8478FE5F85B5
+  Functions: 6126
+  Symbols:   21567
+  CStrings:  11880
 
Symbols:
+ -[WBSExtensionsController initWithProfileServerID:userContentController:forceExtensionLoadingAfterDiscovery:]
- -[WBSExtensionsController initWithProfileServerID:userContentController:forceExtensionLoadingAfterDiscovery:willBeUsedForAppMigrationExport:]
- -[WBSExtensionsController(ExtensionsExportDataSource) extensionsDataForAppMigrationExport]
- GCC_except_table191
- _OBJC_IVAR_$_WBSExtensionsController._isUsedForAppMigrationExport
- _WBS_LOG_CHANNEL_PREFIXAppMigration
- _WBS_LOG_CHANNEL_PREFIXAppMigration.cold.1
- _WBS_LOG_CHANNEL_PREFIXAppMigration.log
- _WBS_LOG_CHANNEL_PREFIXAppMigration.onceToken
- ___WBS_LOG_CHANNEL_PREFIXAppMigration_block_invoke
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~B6_nugDO7V9pwAROgwWEPWpfINYT10-MzReyS7k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/wtf/HashTable.h"
+ "Aborted displaying history clearing denial alert because a different alert is already shown."
+ "Aborted displaying private browsing denial alert because a different alert is already shown."
+ "Attempting to display history clearing denial alert. isHistoryClearingEnabled=%{bool}d"
+ "Attempting to display private browsing denial alert. isPrivateBrowsingEnabled=%{bool}d"
+ "Clearing History Unavailable"
+ "ManagedFeatureRestrictions"
+ "Private Browsing Unavailable"
+ "This setting has been configured by an app or device management."
+ "fallbackAlertMessage"
+ "initWithProfileServerID:userContentController:forceExtensionLoadingAfterDiscovery:"
+ "isHistoryClearingEnabled"
- "/AppleInternal/Library/BuildRoots/4~B6jFugDjnE_G3dGnxh4Ud8pJYpI_Sz2tzdj3fFA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/wtf/HashTable.h"
- "@40@0:8@16@24B32B36"
- "AppMigration"
- "Clearing your history is not available because it has been restricted by the organization managing your device."
- "Exporting extension data: %{sensitive}@"
- "Finished generating extension export data for profile %{public}@"
- "Generating extension export data for profile %{public}@"
- "No extensions to export because extensions are disabled"
- "No extensions to export because there is no saved extension state"
- "Private Browsing is not available because it has been restricted by the organization managing your device."
- "Skipping export of disabled extension %{sensitive, mask.hash}@"
- "Skipping export of extension %{sensitive, mask.hash}@ because _extensionFromComposedIdentifier returned nil"
- "Skipping export of extension %{sensitive, mask.hash}@ because initWithExtension returned nil"
- "Unable to Clear History"
- "Unable to enter Private Browsing"
- "_isUsedForAppMigrationExport"
- "extensionsDataForAppMigrationExport"
- "initWithProfileServerID:userContentController:forceExtensionLoadingAfterDiscovery:willBeUsedForAppMigrationExport:"

```
