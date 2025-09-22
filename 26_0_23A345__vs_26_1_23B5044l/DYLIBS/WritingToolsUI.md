## WritingToolsUI

> `/System/Library/PrivateFrameworks/WritingToolsUI.framework/WritingToolsUI`

```diff

-83.101.0.0.0
-  __TEXT.__text: 0x33c70
-  __TEXT.__auth_stubs: 0xbf0
-  __TEXT.__objc_methlist: 0x3d2c
-  __TEXT.__const: 0xaf4
-  __TEXT.__cstring: 0x251e
-  __TEXT.__oslogstring: 0x11ac
+90.0.0.0.0
+  __TEXT.__text: 0x3397c
+  __TEXT.__auth_stubs: 0xbb0
+  __TEXT.__objc_methlist: 0x3d6c
+  __TEXT.__const: 0xa44
+  __TEXT.__cstring: 0x238e
+  __TEXT.__oslogstring: 0x1328
   __TEXT.__gcc_except_tab: 0xaa8
   __TEXT.__dlopen_cstrs: 0xb4
-  __TEXT.__constg_swiftt: 0x5ac
-  __TEXT.__swift5_typeref: 0x2ea
+  __TEXT.__constg_swiftt: 0x590
+  __TEXT.__swift5_typeref: 0x2dc
   __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_reflstr: 0x521
-  __TEXT.__swift5_fieldmd: 0x458
+  __TEXT.__swift5_reflstr: 0x311
+  __TEXT.__swift5_fieldmd: 0x364
   __TEXT.__swift5_assocty: 0xa8
-  __TEXT.__swift5_proto: 0x44
-  __TEXT.__swift5_types: 0x3c
+  __TEXT.__swift5_proto: 0x38
+  __TEXT.__swift5_types: 0x38
   __TEXT.__swift5_capture: 0x70
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0xf18
+  __TEXT.__unwind_info: 0xf20
   __TEXT.__eh_frame: 0xf8
   __TEXT.__objc_classname: 0x662
-  __TEXT.__objc_methname: 0x9f26
+  __TEXT.__objc_methname: 0xa01a
   __TEXT.__objc_methtype: 0x2120
-  __TEXT.__objc_stubs: 0x6b40
+  __TEXT.__objc_stubs: 0x6bc0
   __DATA_CONST.__got: 0x4d8
   __DATA_CONST.__const: 0x9c8
   __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2720
+  __DATA_CONST.__objc_selrefs: 0x2748
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xb0
-  __AUTH_CONST.__auth_got: 0x608
-  __AUTH_CONST.__const: 0x830
+  __AUTH_CONST.__auth_got: 0x5e8
+  __AUTH_CONST.__const: 0x7a0
   __AUTH_CONST.__cfstring: 0xa60
-  __AUTH_CONST.__objc_const: 0x53d0
+  __AUTH_CONST.__objc_const: 0x5400
   __AUTH_CONST.__objc_intobj: 0x480
   __AUTH.__objc_data: 0x1050
   __AUTH.__data: 0x1f0
-  __DATA.__objc_ivar: 0x2bc
-  __DATA.__data: 0xc58
-  __DATA.__bss: 0x9c0
+  __DATA.__objc_ivar: 0x2c0
+  __DATA.__data: 0xc40
+  __DATA.__bss: 0x8c0
   __DATA.__common: 0x80
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x90
+  __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/BrowserEngineKit.framework/BrowserEngineKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
-  - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/GenerativeAssistantSettings.framework/GenerativeAssistantSettings
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/RenderBox.framework/RenderBox

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2514B530-8651-3396-A0A8-AAF0463EDCE0
-  Functions: 1543
-  Symbols:   4219
-  CStrings:  2429
+  UUID: C891B8E6-0B2A-3CD6-9239-DF921C31B69D
+  Functions: 1536
+  Symbols:   4242
+  CStrings:  2427
 
Symbols:
+ +[WTWritingToolsController feedbackViewHeight]
+ +[_WTTextPlaceholderController _delegateHasOpenPlaceholder:]
+ -[WTWritingToolsController _dismissFullScreenViewControllerWithCompletion:].cold.2
+ -[WTWritingToolsController dismissFormsheetViewControllerWithCompletion:]
+ -[WTWritingToolsController dismissFormsheetViewControllerWithCompletion:].cold.1
+ -[WTWritingToolsController dismissingFullscreenViewController]
+ -[WTWritingToolsController setDismissingFullscreenViewController:]
+ GCC_except_table162
+ _OBJC_IVAR_$_WTWritingToolsController._dismissingFullscreenViewController
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ ___62-[WTWritingToolsController enrollmentDismissedWithCompletion:]_block_invoke.660
+ ___73-[WTWritingToolsController dismissFormsheetViewControllerWithCompletion:]_block_invoke
+ ___75-[WTWritingToolsController _dismissFullScreenViewControllerWithCompletion:]_block_invoke.cold.1
+ _objc_msgSend$dismissFormsheetViewControllerWithCompletion:
+ _objc_msgSend$dismissingFullscreenViewController
+ _objc_msgSend$feedbackViewHeight
+ _objc_msgSend$setDismissingFullscreenViewController:
- GCC_except_table159
- GCC_except_table46
- _MGGetBoolAnswer
- ___62-[WTMainPopoverViewController setFeedbackHiddenDetentEnabled:]_block_invoke
- _associated conformance 14WritingToolsUI0aB0OSHAASQ
- _swift_once
- _symbolic _____ 14WritingToolsUI0aB0O
CStrings:
+ "Requested _dismissFormsheetViewControllerWithCompletion %@ (sourceResponderViewController: %@)"
+ "Skipping dismissFormsheetViewControllerWithCompletion due to already dismissing/dismissed"
+ "Skipping dismissFullScreenViewController due to already dismissing/dismissed"
+ "Skipping updateSourceView due to setting of nil session"
+ "TB,V_dismissingFullscreenViewController"
+ "Unexpected presentFullScreenViewController for nil session (not during handoff)"
+ "Will proceed for phone/compact iPad"
+ "_delegateHasOpenPlaceholder:"
+ "_dismissingFullscreenViewController"
+ "dismissFormsheetViewControllerWithCompletion:"
+ "dismissFullScreenViewController begin"
+ "dismissFullScreenViewController end"
+ "dismissingFullscreenViewController"
+ "feedbackViewHeight"
+ "setDismissingFullscreenViewController:"
- "AlternateQuestionnaire_macOS"
- "CustomQuestionnaireEntry"
- "FeedbackFCSBehavior"
- "Montara"
- "Montara_PersonalInfoSearch"
- "Montara_PersonalInfoSearchRewrite"
- "Montara_PromptEntryView"
- "Montara_SlotFill"
- "Montara_Streaming"
- "OpenEndedAdjustmentV2_FollowUp"
- "Panel_iOS"
- "Panel_iPadOS"
- "Panel_macOS"
- "Panel_visionOS"
- "Skipping dismissFullScreenViewController"
- "Unexpected presentFullScreenViewController while ending session"
- "Will proceed for phone"

```
