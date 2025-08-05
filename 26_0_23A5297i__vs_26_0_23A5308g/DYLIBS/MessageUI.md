## MessageUI

> `/System/Library/Frameworks/MessageUI.framework/MessageUI`

```diff

-3860.100.5.2.1
-  __TEXT.__text: 0x124894
+3863.100.1.2.5
+  __TEXT.__text: 0x124f5c
   __TEXT.__auth_stubs: 0x24e0
   __TEXT.__delay_helper: 0xec
-  __TEXT.__objc_methlist: 0x1257c
-  __TEXT.__gcc_except_tab: 0x25050
-  __TEXT.__cstring: 0x9bd4
+  __TEXT.__objc_methlist: 0x125e4
+  __TEXT.__gcc_except_tab: 0x25104
+  __TEXT.__cstring: 0x9c34
   __TEXT.__const: 0x1424
   __TEXT.__oslogstring: 0x5453
   __TEXT.__dlopen_cstrs: 0x40d

   __TEXT.__swift5_capture: 0x84
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
-  __TEXT.__unwind_info: 0x9db8
+  __TEXT.__unwind_info: 0x9df0
   __TEXT.__eh_frame: 0x328
   __TEXT.__objc_classname: 0x2192
-  __TEXT.__objc_methname: 0x34cc9
+  __TEXT.__objc_methname: 0x34dfd
   __TEXT.__objc_methtype: 0xb9bf
-  __TEXT.__objc_stubs: 0x22ec0
-  __DATA_CONST.__got: 0x1c80
+  __TEXT.__objc_stubs: 0x22fe0
+  __DATA_CONST.__got: 0x1c88
   __DATA_CONST.__const: 0x4700
   __DATA_CONST.__objc_classlist: 0x608
   __DATA_CONST.__objc_catlist: 0x108
   __DATA_CONST.__objc_protolist: 0x410
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbf48
+  __DATA_CONST.__objc_selrefs: 0xbf98
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x4a8
-  __DATA_CONST.__objc_arraydata: 0x608
+  __DATA_CONST.__objc_arraydata: 0x628
   __AUTH_CONST.__auth_got: 0x1280
   __AUTH_CONST.__const: 0x1228
-  __AUTH_CONST.__cfstring: 0x8d00
-  __AUTH_CONST.__objc_const: 0x19ff0
+  __AUTH_CONST.__cfstring: 0x8d60
+  __AUTH_CONST.__objc_const: 0x1a058
   __AUTH_CONST.__objc_intobj: 0x1b0
-  __AUTH_CONST.__objc_dictobj: 0x550
+  __AUTH_CONST.__objc_dictobj: 0x578
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x2da0
   __AUTH.__data: 0x190
-  __DATA.__objc_ivar: 0x10f8
-  __DATA.__data: 0x3314
-  __DATA.__bss: 0x17c8
+  __DATA.__objc_ivar: 0x1100
+  __DATA.__data: 0x3318
+  __DATA.__bss: 0x1808
   __DATA.__common: 0x2f8
   __DATA_DIRTY.__objc_data: 0x11f0
   __DATA_DIRTY.__data: 0x30
-  __DATA_DIRTY.__bss: 0x70
+  __DATA_DIRTY.__bss: 0x60
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A5240204-8F2B-3BCB-88EC-466C8E529970
-  Functions: 6171
-  Symbols:   23991
-  CStrings:  12501
+  UUID: 79905E45-D5A8-3CBD-B49C-E111690E013E
+  Functions: 6182
+  Symbols:   24036
+  CStrings:  12520
 
Symbols:
+ +[UIDevice(MessageUI) mf_isPadIdiom]
+ +[UIDevice(MessageUI) mf_isPadIdiom].cold.1
+ -[MFComposeInputAccessoryView hitTest:withEvent:]
+ -[MFComposeSubjectView needsInputAssistantItemUpdate]
+ -[MFComposeSubjectView setNeedsInputAssistantItemUpdate:]
+ -[MFComposeWebView _updatePocketContainerInteractionVisible:]
+ -[MFComposeWebView didRotateFromInterfaceOrientation:]
+ -[MFMailComposeRecipientTextView becomeFirstResponder]
+ -[MFMailComposeRecipientTextView needsInputAssistantItemUpdate]
+ -[MFMailComposeRecipientTextView setNeedsInputAssistantItemUpdate:]
+ GCC_except_table232
+ GCC_except_table249
+ GCC_except_table263
+ _OBJC_CLASS_$__UIButtonBarButton
+ _OBJC_IVAR_$_MFComposeSubjectView._needsInputAssistantItemUpdate
+ _OBJC_IVAR_$_MFMailComposeRecipientTextView._needsInputAssistantItemUpdate
+ _QuotingColorList.onceToken.566
+ ___36+[UIDevice(MessageUI) mf_isPadIdiom]_block_invoke
+ ___44+[UIColor(MessageUI) mailQuoteColorLevelOne]_block_invoke
+ ___44+[UIColor(MessageUI) mailQuoteColorLevelTwo]_block_invoke
+ ___46+[MFComposeWebView _basicWebViewConfiguration]_block_invoke.87
+ ___46+[UIColor(MessageUI) mailQuoteColorLevelThree]_block_invoke
+ ___60-[MFComposeWebView _webView:didInsertAttachment:withSource:]_block_invoke.552
+ ___60-[MFComposeWebView _webView:didInsertAttachment:withSource:]_block_invoke.553
+ ___block_literal_global.1260
+ ___block_literal_global.236
+ ___block_literal_global.263
+ ___block_literal_global.265
+ ___block_literal_global.320
+ ___block_literal_global.322
+ ___block_literal_global.417
+ ___block_literal_global.423
+ _mailQuoteColorLevelOne.onceToken
+ _mailQuoteColorLevelOne.sInstance
+ _mailQuoteColorLevelThree.onceToken
+ _mailQuoteColorLevelThree.sInstance
+ _mailQuoteColorLevelTwo.onceToken
+ _mailQuoteColorLevelTwo.sInstance
+ _mf_isPadIdiom.isPad
+ _mf_isPadIdiom.onceToken
+ _objc_msgSend$_updatePocketContainerInteractionVisible:
+ _objc_msgSend$effectiveGeometry
+ _objc_msgSend$em_lockdownModeEnabled
+ _objc_msgSend$interactions
+ _objc_msgSend$interfaceOrientation
+ _objc_msgSend$isPad
+ _objc_msgSend$mf_isPadIdiom
+ _objc_msgSend$needsInputAssistantItemUpdate
+ _objc_msgSend$removeInteraction:
+ _objc_msgSend$setNeedsInputAssistantItemUpdate:
- +[UIDevice(MessageUI) mf_isPad]
- +[UIDevice(MessageUI) mf_isPad].cold.1
- GCC_except_table164
- GCC_except_table237
- _QuotingColorList.onceToken.553
- ___31+[UIDevice(MessageUI) mf_isPad]_block_invoke
- ___46+[MFComposeWebView _basicWebViewConfiguration]_block_invoke.84
- ___60-[MFComposeWebView _webView:didInsertAttachment:withSource:]_block_invoke.549
- ___60-[MFComposeWebView _webView:didInsertAttachment:withSource:]_block_invoke.550
- ___block_literal_global.1253
- ___block_literal_global.233
- ___block_literal_global.260
- ___block_literal_global.262
- ___block_literal_global.317
- ___block_literal_global.319
- ___block_literal_global.414
- ___block_literal_global.420
- _mf_isPad.isPad
- _mf_isPad.onceToken
- _objc_msgSend$mf_isPad
CStrings:
+ ":root:not(.apple-mail-supports-explicit-dark-mode)"
+ "?"
+ "TB,N,V_needsInputAssistantItemUpdate"
+ "_needsInputAssistantItemUpdate"
+ "_updatePocketContainerInteractionVisible:"
+ "_webViewWillEnterFullscreen:"
+ "effectiveGeometry"
+ "em_lockdownModeEnabled"
+ "interactions"
+ "interfaceOrientation"
+ "mf_isPadIdiom"
+ "needsInputAssistantItemUpdate"
+ "removeInteraction:"
+ "setNeedsInputAssistantItemUpdate:"
+ "showRemoteImages"
+ "transparent !important"
- "mf_isPad"

```
