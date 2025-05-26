## MessageUI

> `/System/Library/Frameworks/MessageUI.framework/MessageUI`

```diff

-3774.200.91.2.1
-  __TEXT.__text: 0xfa030
+3774.300.61.2.4
+  __TEXT.__text: 0xfa4a4
   __TEXT.__auth_stubs: 0x1b50
-  __TEXT.__objc_methlist: 0xd364
-  __TEXT.__gcc_except_tab: 0x20210
+  __TEXT.__objc_methlist: 0xd36c
+  __TEXT.__gcc_except_tab: 0x20280
   __TEXT.__cstring: 0x89c6
   __TEXT.__const: 0x744
-  __TEXT.__oslogstring: 0x4436
+  __TEXT.__oslogstring: 0x46ef
   __TEXT.__ustring: 0x4d2
   __TEXT.__swift5_typeref: 0x192
   __TEXT.__swift5_reflstr: 0x8d

   __TEXT.__swift5_capture: 0x28
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__objc_const_ax: 0x4c4
-  __TEXT.__unwind_info: 0x94f4
+  __TEXT.__unwind_info: 0x94ec
   __TEXT.__eh_frame: 0x1f8
   __TEXT.__objc_classname: 0x20fc
-  __TEXT.__objc_methname: 0x31b9a
+  __TEXT.__objc_methname: 0x31c18
   __TEXT.__objc_methtype: 0xa9d8
-  __TEXT.__objc_stubs: 0x21a40
+  __TEXT.__objc_stubs: 0x21a80
   __DATA_CONST.__got: 0x9f8
   __DATA_CONST.__const: 0x41c8
   __DATA_CONST.__objc_classlist: 0x5d0
   __DATA_CONST.__objc_catlist: 0x128
   __DATA_CONST.__objc_protolist: 0x3c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1ac70
-  __DATA_CONST.__objc_selrefs: 0xa260
+  __DATA_CONST.__objc_const: 0x1ac90
+  __DATA_CONST.__objc_selrefs: 0xa270
   __DATA_CONST.__objc_arraydata: 0x5f8
   __AUTH_CONST.__cfstring: 0x8b80
   __AUTH_CONST.__objc_const: 0x55c0

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 5435
-  Symbols:   22850
-  CStrings:  10680
+  Symbols:   22851
+  CStrings:  10692
 
Symbols:
+ -[MFMessageComposeViewController setMessage:withExtensionBundleIdentifier:]
+ ___60-[MFComposeWebView _webView:didInsertAttachment:withSource:]_block_invoke.478
+ ___60-[MFComposeWebView _webView:didInsertAttachment:withSource:]_block_invoke.479
+ ___block_literal_global.1022
+ ___block_literal_global.212
+ ___block_literal_global.359
+ ___block_literal_global.365
+ ___block_literal_global.416
+ ___block_literal_global.435
+ ___block_literal_global.442
+ ___block_literal_global.452
+ _objc_msgSend$insertMessage:extensionBundleIdentifier:
+ _objc_msgSend$setMessage:withExtensionBundleIdentifier:
- -[MFComposeWebView _webView:didInsertAttachment:withSource:].cold.1
- ___60-[MFComposeWebView _webView:didInsertAttachment:withSource:]_block_invoke.481
- ___60-[MFComposeWebView _webView:didInsertAttachment:withSource:]_block_invoke_2
- ___block_literal_global.1024
- ___block_literal_global.210
- ___block_literal_global.362
- ___block_literal_global.368
- ___block_literal_global.412
- ___block_literal_global.431
- ___block_literal_global.438
- ___block_literal_global.448
CStrings:
+ "<%p> Adding attachment: %{public}@"
+ "<%p> Did not find the contentID for identifier: %{public}@, looking into _attachmentsByUniqueIdentifier."
+ "<%p> Failed to insert attachment %{public}@, content ID: %{public}@"
+ "<%p> Found attachment %{public}@, for wkAttachment info: %{public}@"
+ "<%p> Found existing: %{BOOL}d contentID: %{public}@ in context"
+ "<%p> Loaded attachment with info: %{public}@"
+ "<%p> Removing attachment: %{public}@, content ID: %{public}@"
+ "<%p> Replacing attachment: %{public}@"
+ "<%p> Replacing placehold with attachment for content ID: %{public}@, file name: %{public}@"
+ "<%p> WebView didInsertAttachment: %{public}@"
+ "<%p> Webview did insert attachment: %{public}@, for content ID: %{public}@"
+ "<%p> Webview did invalidate data for attachment: %{public}@"
+ "<%p> Webview did remove attachment: %{public}@"
+ "<%p> _addInlineAttachmentWithData for content ID: %{public}@, file name: %{public}@"
+ "Attempting to request content representation for contentItem: %{public}@, download: %{BOOL}d, isMaildrop: %{BOOL}d, networkUsage: %ld"
+ "Passing override extensionBundleIdentifier: '%@' to CKSMSComposeController."
+ "autoFillDidInsertWithExplicitInvocationMode:"
+ "insertMessage:extensionBundleIdentifier:"
+ "setMessage:withExtensionBundleIdentifier:"
- "Adding attachment: %{public}@"
- "Failed to insert attachment %{public}@, content ID: %{public}@"
- "Removing attachment: %{public}@, content ID: %{public}@"
- "Replacing placehold with attachment for content ID: %{public}@, file name: %{public}@"
- "Webview did insert attachment: %{public}@, content ID: %{public}@"
- "Webview did invalidate data for attachment: %{public}@"
- "Webview did remove attachment: %{public}@"

```
