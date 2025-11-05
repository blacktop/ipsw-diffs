## ShareSheet

> `/System/iOSSupport/System/Library/PrivateFrameworks/ShareSheet.framework/Versions/A/ShareSheet`

```diff

-2060.40.21.0.0
-  __TEXT.__text: 0x36194
-  __TEXT.__auth_stubs: 0x950
-  __TEXT.__objc_methlist: 0x4e64
-  __TEXT.__const: 0x1d8
+2060.50.171.1.2
+  __TEXT.__text: 0x36478
+  __TEXT.__auth_stubs: 0x970
+  __TEXT.__objc_methlist: 0x600c
+  __TEXT.__const: 0x1e8
+  __TEXT.__gcc_except_tab: 0x7f8
   __TEXT.__oslogstring: 0x13a7
-  __TEXT.__cstring: 0x29ef
+  __TEXT.__cstring: 0x2aa1
   __TEXT.__dlopen_cstrs: 0x4e3
-  __TEXT.__gcc_except_tab: 0x79c
   __TEXT.__ustring: 0x84
-  __TEXT.__unwind_info: 0x1078
+  __TEXT.__unwind_info: 0x10c8
   __TEXT.__objc_classname: 0x1042
-  __TEXT.__objc_methname: 0x11ba9
-  __TEXT.__objc_methtype: 0x3041
-  __TEXT.__objc_stubs: 0x9ce0
+  __TEXT.__objc_methname: 0x11c23
+  __TEXT.__objc_methtype: 0x309c
+  __TEXT.__objc_stubs: 0x9d20
   __DATA_CONST.__got: 0x748
-  __DATA_CONST.__const: 0xe38
+  __DATA_CONST.__const: 0xe60
   __DATA_CONST.__objc_classlist: 0x338
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x35b8
+  __DATA_CONST.__objc_selrefs: 0x3a98
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x1f0
-  __AUTH_CONST.__auth_got: 0x4b8
+  __AUTH_CONST.__auth_got: 0x4c8
   __AUTH_CONST.__const: 0x660
-  __AUTH_CONST.__cfstring: 0x22a0
-  __AUTH_CONST.__objc_const: 0x13210
+  __AUTH_CONST.__cfstring: 0x23e0
+  __AUTH_CONST.__objc_const: 0x111c0
   __AUTH.__objc_data: 0x1fe0
-  __AUTH.__data: 0x50
+  __AUTH.__data: 0x40
   __DATA.__objc_ivar: 0x760
   __DATA.__data: 0x1148
-  __DATA.__bss: 0x3a8
+  __DATA.__bss: 0x3b8
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /System/iOSSupport/System/Library/PrivateFrameworks/UIKitCore.framework/Versions/A/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 65216D70-9AA3-312D-9011-F381E795DDF1
-  Functions: 1880
-  Symbols:   5553
-  CStrings:  3942
+  UUID: F3BDC128-3D8F-33F1-8DC6-A7D9E8226676
+  Functions: 1915
+  Symbols:   5604
+  CStrings:  3969
 
Symbols:
+ +[SHSheetContentDataSourceManager contentCustomViewUniqueIdentifier].cold.1
+ +[SHSheetCustomSceneViewController sceneWorkspace].cold.1
+ +[SHSheetHostToClientActionManager shared].cold.1
+ +[SHSheetScene sceneWorkspace].cold.1
+ +[UIDocumentInteractionController _archiveDecompressQueue].cold.1
+ +[_UIActivityUserDefaultsManager requestFavoritesForActivityCategory:completionHandler:].cold.1
+ -[SHSheetRemoteSceneViewController reloadMetadata:].cold.1
+ -[SHSheetSceneViewController reloadMetadata:].cold.1
+ -[SHSheetUIServiceClient _setupNewConnection].cold.1
+ -[UIActivityViewController _bridgedPresentationUnavailable].cold.1
+ -[UIDocumentInteractionController icons].cold.1
+ -[UISUISecurityScopedResource initWithCoder:].cold.1
+ -[_UIDICActivityItemProvider _shouldExecuteItemOperationForActivity:].cold.1
+ -[_UIUserDefaultsActivity _activityImage].cold.1
+ GCC_except_table26
+ GCC_except_table34
+ _ShareSheetCanAccessPeopleSuggestions.cold.1
+ _ShareSheetCanUseCustomViewController.cold.1
+ _ShareSheetCanUseCustomViewController.cold.2
+ _ShareSheetCanUseCustomViewController.cold.3
+ _ShareSheetCanUseCustomViewController.cold.4
+ _ShareSheetCanUseCustomViewController.cold.5
+ _ShareSheetCanUseCustomViewController.cold.6
+ _ShareSheetCanUseCustomViewController.cold.7
+ _ShareSheetCanUseCustomViewController.cold.8
+ _ShareSheetCanUseCustomViewController.cold.9
+ _ShareSheetDeviceScreenScale.cold.1
+ _ShareSheetHostCanRenderInProcess.cold.1
+ _ShareSheetImageAnalysisAllowed.cold.1
+ _ShareSheetIsAppleApp.cold.1
+ _ShareSheetIsBrowser.cold.1
+ _ShareSheetIsCamera.cold.1
+ _ShareSheetIsRealityLauncher.cold.1
+ _ShareSheetIsSafari.cold.1
+ _UIActivityHelperActivityItemsIncludeICloudDriveURL.cold.1
+ _UIKitUserDefaults.cold.1
+ ___41-[UISDActivityItemData canAccessFileURL:]_block_invoke_2
+ ___block_descriptor_48_e8_32s40r_e22_v32?0"NSURL"8Q16^B24ls32l8r40l8
+ ___getSFUILinkMetadataSerializationForLocalUseOnlySymbolLoc_block_invoke
+ _objc_msgSend$URLByResolvingSymlinksInPath
+ _objc_msgSend$setAccessibilityIdentifier:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x28
+ getSFUILinkMetadataSerializationForLocalUseOnlySymbolLoc.ptr
+ initFPExtendBookmarkForDocumentURL.cold.1
+ initFPSandboxingURLWrapper.cold.1
+ initLPButtonAction.cold.1
+ initLPImage.cold.1
+ initLPLinkMetadata.cold.1
+ initQLDismissAction.cold.1
+ initQLPreviewController.cold.1
+ share_sheet_log.cold.1
- -[UIActivityViewController _sourceWindowForPopoverPresentationSourceView:sourceRect:].cold.1
- _initSFUILinkMetadataSerializationForLocalUseOnly
- _softLinkSFUILinkMetadataSerializationForLocalUseOnly
CStrings:
+ "ShareSheet.RemoteContainerView"
+ "URLByResolvingSymlinksInPath"
+ "Unimplemented at /AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ShareSheet_iosmac/ShareSheet/Activity/UIActivityViewController.m:1416 : Not supported on macOS yet."
+ "Unimplemented at /AppleInternal/Library/BuildRoots/5f17400b-fd8b-11ef-934c-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/ShareSheet_iosmac/ShareSheet/Activity/UIActivityViewController.m:1422 : Not supported on macOS yet."
+ "footer.textView"
+ "header.titleLabel"
+ "imageView"
+ "setAccessibilityIdentifier:"
+ "textField:insertInputSuggestion:"
+ "textView:insertInputSuggestion:"
+ "v32@0:8@\"UITextField\"16@\"UIInputSuggestion\"24"
+ "v32@0:8@\"UITextView\"16@\"UIInputSuggestion\"24"
+ "v32@?0@\"NSURL\"8Q16^B24"
- "Unimplemented at /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/ShareSheet_iosmac/ShareSheet/Activity/UIActivityViewController.m:1403 : Not supported on macOS yet."
- "Unimplemented at /AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/ShareSheet_iosmac/ShareSheet/Activity/UIActivityViewController.m:1409 : Not supported on macOS yet."

```
