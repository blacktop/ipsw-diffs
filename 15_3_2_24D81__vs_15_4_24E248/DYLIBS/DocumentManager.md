## DocumentManager

> `/System/iOSSupport/System/Library/PrivateFrameworks/DocumentManager.framework/Versions/A/DocumentManager`

```diff

-337.4.0.0.0
-  __TEXT.__text: 0x313a8
+337.5.1.3.0
+  __TEXT.__text: 0x31aec
   __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__objc_methlist: 0x2590
-  __TEXT.__const: 0x190
+  __TEXT.__objc_methlist: 0x2ddc
+  __TEXT.__const: 0x170
   __TEXT.__cstring: 0x4740
   __TEXT.__ustring: 0x644
   __TEXT.__oslogstring: 0x2d4d
-  __TEXT.__gcc_except_tab: 0x898
-  __TEXT.__unwind_info: 0xc40
+  __TEXT.__gcc_except_tab: 0x888
+  __TEXT.__unwind_info: 0xcf0
   __TEXT.__objc_classname: 0x7b1
-  __TEXT.__objc_methname: 0xa9f8
-  __TEXT.__objc_methtype: 0x164f
+  __TEXT.__objc_methname: 0xaa44
+  __TEXT.__objc_methtype: 0x1690
   __TEXT.__objc_stubs: 0x7aa0
   __DATA_CONST.__got: 0x5d8
   __DATA_CONST.__const: 0x1510

   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x26e0
+  __DATA_CONST.__objc_selrefs: 0x2930
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x468
   __AUTH_CONST.__const: 0x460
   __AUTH_CONST.__cfstring: 0x3780
-  __AUTH_CONST.__objc_const: 0x5430
+  __AUTH_CONST.__objc_const: 0x4520
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xbe0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 6A1C9C69-7F6A-3D09-8096-709BC257A405
-  Functions: 1161
-  Symbols:   3417
-  CStrings:  3085
+  UUID: 459FE2E4-391F-3D18-93A5-376230FFD058
+  Functions: 1205
+  Symbols:   3464
+  CStrings:  3090
 
Symbols:
+ +[DOCConcreteLocation recentDocumentsLocation].cold.1
+ +[DOCConcreteLocation searchLocation].cold.1
+ +[DOCConcreteLocation trashedItemsLocation].cold.1
+ +[DOCExtensionInterface hostProtocol].cold.1
+ +[DOCExtensionInterface vendorProtocol].cold.1
+ +[DOCIconService SFSymbolImageProviderIcon:].cold.1
+ +[DOCIconService shared].cold.1
+ +[DOCRemoteUIBarButtonItemRegistry shared].cold.1
+ +[DOCRemoteViewController serviceExtension].cold.1
+ +[DOCUISession shared].cold.1
+ +[DOCUserInterfaceStateStore sharedStore].cold.1
+ +[UIDocumentBrowserViewController placeholderURLForDownloadsFolder].cold.1
+ -[DOCActivity initWithIdentifier:actionPerformer:forBrowserAction:].cold.1
+ -[DOCActivity initWithIdentifier:actionPerformer:forBrowserAction:].cold.2
+ -[DOCIconService _fetchIconFromIconService:size:triggerDiskUpdate:].cold.1
+ -[DOCIconService _loadIconsFromDiskForSize:fileManager:].cold.2
+ -[DOCIconService _persistCacheForSize:bundles:fileManager:].cold.2
+ -[DOCItemBookmark coordinatedFileURL].cold.1
+ -[DOCItemBookmark prepareForMode:usingBookmark:shouldConvert:conversionRules:completionBlock:].cold.1
+ -[DOCKeyCommandController buildWithBuilder:].cold.1
+ -[DOCSmartFolderDatabase registerFilenameHit:fileTypeHit:smartScoreBlock:].cold.1
+ -[DOCSmartFolderDatabase registerFilenameHit:fileTypeHit:smartScoreBlock:].cold.2
+ -[DOCWeakProxy forwardingTargetForSelector:].cold.1
+ -[UIDocumentBrowserViewController _requestAnimationInfoForDocumentAtURL:completion:].cold.1
+ -[UIDocumentBrowserViewController _requestAnimationInfoForDocumentAtURL:completion:].cold.2
+ -[UIDocumentBrowserViewController recentDocumentsContentTypesFromInfoPlist].cold.1
+ -[UIDocumentBrowserViewController remoteViewControllerDidTerminateViewServiceWithError:].cold.4
+ -[UIDocumentBrowserViewController renameDocumentAtURL:proposedName:completionHandler:].cold.1
+ -[UIDocumentBrowserViewController renameDocumentAtURL:proposedName:completionHandler:].cold.2
+ -[UIDocumentBrowserViewController renameDocumentAtURL:proposedName:completionHandler:].cold.3
+ DOCAssertWithIntenalBuildAlert.cold.2
+ DOCDebugMenuEnabled.cold.1
+ DOCDebugMenuEnabled.cold.2
+ DOCDeviceHasHomeButton.cold.1
+ DOCFrameworkBundle.cold.1
+ DOCIsInternalBuild.cold.1
+ DOCScreenSizePad12_9.cold.1
+ DOCScreenSizeSEPhone.cold.1
+ _DOCMainScreenClass.cold.1
+ _DOCMainScreenSize.cold.1
+ __38-[DOCSmartFolderDatabase previousHits]_block_invoke.cold.2
+ __40-[DOCSmartFolderDatabase registerEvent:]_block_invoke.cold.5
+ __41-[DOCSmartFolderDatabase purgeOldEntries]_block_invoke.cold.8
+ __48-[DOCSmartFolderDatabase _setUpDatabaseWatcher:]_block_invoke.cold.3
+ __73-[DOCSmartFolderDatabase deleteFolderWithIdentifier:appBundleIdentifier:]_block_invoke.cold.7
+ __73-[DOCSmartFolderDatabase previousEventsForAppBundleIdentifier:excluding:]_block_invoke.cold.2
+ __74-[DOCSmartFolderDatabase registerFilenameHit:fileTypeHit:smartScoreBlock:]_block_invoke.cold.2
+ __77-[UIDocumentBrowserViewController(UIKit_macOS) updateSceneSettingsForWindow:]_block_invoke.cold.1
+ __94-[DOCItemBookmark prepareForMode:usingBookmark:shouldConvert:conversionRules:completionBlock:]_block_invoke_3.cold.2
+ __block_literal_global.189
- GCC_except_table25
- _OUTLINED_FUNCTION_15
- __block_literal_global.183
CStrings:
+ "@\"UIConversationContext\"16@0:8"
+ "T@\"UIConversationContext\",?,&,N"
+ "conversationContext"
+ "setConversationContext:"
+ "v24@0:8@\"UIConversationContext\"16"

```
