## WritingToolsUI

> `/System/Library/PrivateFrameworks/WritingToolsUI.framework/WritingToolsUI`

```diff

-79.100.0.0.0
-  __TEXT.__text: 0x32e1c
-  __TEXT.__auth_stubs: 0xc90
-  __TEXT.__objc_methlist: 0x3cec
+82.1.0.0.0
+  __TEXT.__text: 0x334bc
+  __TEXT.__auth_stubs: 0xbb0
+  __TEXT.__objc_methlist: 0x3d2c
   __TEXT.__const: 0xa44
-  __TEXT.__cstring: 0x234e
-  __TEXT.__oslogstring: 0xfe5
-  __TEXT.__gcc_except_tab: 0xa70
+  __TEXT.__cstring: 0x238e
+  __TEXT.__oslogstring: 0x11ac
+  __TEXT.__gcc_except_tab: 0xaa8
   __TEXT.__dlopen_cstrs: 0xb4
-  __TEXT.__constg_swiftt: 0x5a8
+  __TEXT.__constg_swiftt: 0x590
   __TEXT.__swift5_typeref: 0x2dc
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_reflstr: 0x311

   __TEXT.__swift5_types: 0x38
   __TEXT.__swift5_capture: 0x70
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0xef8
+  __TEXT.__unwind_info: 0xf08
   __TEXT.__eh_frame: 0xf8
   __TEXT.__objc_classname: 0x662
-  __TEXT.__objc_methname: 0x9e8c
-  __TEXT.__objc_methtype: 0x211c
-  __TEXT.__objc_stubs: 0x6aa0
-  __DATA_CONST.__got: 0x4f8
-  __DATA_CONST.__const: 0x9a0
+  __TEXT.__objc_methname: 0x9f26
+  __TEXT.__objc_methtype: 0x2128
+  __TEXT.__objc_stubs: 0x6b40
+  __DATA_CONST.__got: 0x4d8
+  __DATA_CONST.__const: 0x9c8
   __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2710
+  __DATA_CONST.__objc_selrefs: 0x2720
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xb0
-  __AUTH_CONST.__auth_got: 0x658
-  __AUTH_CONST.__const: 0x760
+  __AUTH_CONST.__auth_got: 0x5e8
+  __AUTH_CONST.__const: 0x7a0
   __AUTH_CONST.__cfstring: 0xa60
-  __AUTH_CONST.__objc_const: 0x53a0
+  __AUTH_CONST.__objc_const: 0x53d0
   __AUTH_CONST.__objc_intobj: 0x480
   __AUTH.__objc_data: 0x1050
-  __AUTH.__data: 0x208
-  __DATA.__objc_ivar: 0x2b8
+  __AUTH.__data: 0x1f0
+  __DATA.__objc_ivar: 0x2bc
   __DATA.__data: 0xc40
   __DATA.__bss: 0x8c0
-  __DATA.__common: 0x78
+  __DATA.__common: 0x80
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__data: 0x20
   __DATA_DIRTY.__bss: 0x10
-  __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/BrowserEngineKit.framework/BrowserEngineKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/GenerativeAssistantSettings.framework/GenerativeAssistantSettings
-  - /System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
-  - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/RenderBox.framework/RenderBox
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4DF8C9B7-A68A-3118-9BCB-F3A7B3CC768F
-  Functions: 1512
-  Symbols:   4175
-  CStrings:  2395
+  UUID: C0503F0A-2477-3F93-95EA-90E7C36DF4C3
+  Functions: 1526
+  Symbols:   4213
+  CStrings:  2415
 
Symbols:
+ +[WTUIActionClientToHost actionForEnrollmentDismissedWithCompletion:]
+ -[WTFormSheetViewController enrollmentDismissedWithCompletion:]
+ -[WTFullScreenContainerViewController _showAlertWithTitle:message:buttonTitle:buttonAction:]
+ -[WTFullScreenContainerViewController enrollmentDismissedWithCompletion:]
+ -[WTFullScreenContainerViewController pendingHandoffHandler]
+ -[WTFullScreenContainerViewController setPendingHandoffHandler:]
+ -[WTFullScreenContainerViewController viewDidAppear:]
+ -[WTMainPopoverViewController enrollmentDismissedWithCompletion:]
+ -[WTMainPopoverViewController handoffFromUCBFromTool:withPrompt:]
+ -[WTSceneHostedInputDashboardViewController enrollmentDismissedWithCompletion:]
+ -[WTWritingToolsController enrollmentDismissedWithCompletion:]
+ -[WTWritingToolsController presentFullScreenViewController].cold.2
+ -[WTWritingToolsController presentFullScreenViewController].cold.3
+ GCC_except_table113
+ GCC_except_table128
+ GCC_except_table131
+ GCC_except_table159
+ GCC_except_table22
+ GCC_except_table28
+ GCC_except_table43
+ GCC_except_table77
+ _OBJC_CLASS_$_WTAvailability
+ _OBJC_IVAR_$_WTFullScreenContainerViewController._pendingHandoffHandler
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ ___43-[WTWritingToolsController enrollmentBegan]_block_invoke
+ ___53-[WTWritingToolsController endWritingToolsWithError:]_block_invoke.473
+ ___58-[WTUIActionClientToHost performActionForSceneController:]_block_invoke_4
+ ___58-[WTWritingToolsController itemProviderForAttributedText:]_block_invoke.568
+ ___62-[WTWritingToolsController enrollmentDismissedWithCompletion:]_block_invoke
+ ___62-[WTWritingToolsController handoffFromUCBFromTool:withPrompt:]_block_invoke
+ ___69+[WTUIActionClientToHost actionForEnrollmentDismissedWithCompletion:]_block_invoke
+ ___75-[WTWritingToolsController _presentSuggestionViewControllerWithCompletion:]_block_invoke.656
+ ___87+[WTUIActionClientToHost actionForShowAlertWithTitle:message:buttonTitle:buttonAction:]_block_invoke.cold.1
+ ___92-[WTFullScreenContainerViewController _showAlertWithTitle:message:buttonTitle:buttonAction:]_block_invoke
+ ___92-[WTFullScreenContainerViewController _showAlertWithTitle:message:buttonTitle:buttonAction:]_block_invoke_2
+ ___92-[WTFullScreenContainerViewController _showAlertWithTitle:message:buttonTitle:buttonAction:]_block_invoke_3
+ ___block_descriptor_72_e8_32s40s48s56bs64w_e5_v8?0lw64l8s32l8s40l8s48l8s56l8
+ ___block_literal_global.524
+ ___swift_memcpy0_1
+ _dispatch_assert_queue$V2
+ _objc_msgSend$_showAlertWithTitle:message:buttonTitle:buttonAction:
+ _objc_msgSend$enrollmentDismissedWithCompletion:
+ _objc_msgSend$error
+ _objc_msgSend$formSheetViewController
+ _objc_msgSend$pendingHandoffHandler
+ _objc_msgSend$setPendingHandoffHandler:
- +[WTUIActionClientToHost actionForEnrollmentDismissed]
- -[WTFormSheetViewController enrollmentDismissed]
- -[WTFullScreenContainerViewController enrollmentDismissed]
- -[WTMainPopoverViewController enrollmentDismissed]
- -[WTSceneHostedInputDashboardViewController enrollmentDismissed]
- -[WTWritingToolsController enrollmentDismissed]
- GCC_except_table111
- GCC_except_table126
- GCC_except_table129
- GCC_except_table156
- GCC_except_table75
- _OBJC_CLASS_$_MCProfileConnection
- ___47-[WTWritingToolsController enrollmentDismissed]_block_invoke
- ___58-[WTWritingToolsController itemProviderForAttributedText:]_block_invoke.567
- ___75-[WTWritingToolsController _presentSuggestionViewControllerWithCompletion:]_block_invoke.655
- ___91-[WTFullScreenContainerViewController showAlertWithTitle:message:buttonTitle:buttonAction:]_block_invoke_2
- ___91-[WTFullScreenContainerViewController showAlertWithTitle:message:buttonTitle:buttonAction:]_block_invoke_3
- ___block_literal_global.523
- ___swift_allocate_value_buffer
- ___swift_project_value_buffer
- _objc_msgSend$enrollmentDismissed
- _swift_once
- _swift_slowAlloc
- _swift_slowDealloc
CStrings:
+ "?"
+ "@\"NSAttributedString\""
+ "@24@0:8@?16"
+ "Began partner enrollment..."
+ "Fullscreen view controller didAppear, with pending handler: %d"
+ "Handling handoff post enablement."
+ "Presenting fullScreenViewController for %ld..."
+ "Received show alert request, pending until viewDidAppear..."
+ "Received show alert request, proceeding..."
+ "T@?,C,N,V_pendingHandoffHandler"
+ "Unexpected error when showing alert: %@"
+ "Unexpected existing presented view controller (%@)"
+ "Unexpected full screen view controller already being presented"
+ "Will proceed for ipad"
+ "Will proceed for phone"
+ "_pendingHandoffHandler"
+ "_showAlertWithTitle:message:buttonTitle:buttonAction:"
+ "actionForEnrollmentDismissedWithCompletion:"
+ "dismissViewController (Formsheet) for endWritingTools"
+ "dismissViewController (Fullscreen) for endWritingTools"
+ "enrollmentDismissedWithCompletion:"
+ "error"
+ "handoffFromUCBFromTool: %@"
+ "pendingHandoffHandler"
+ "setPendingHandoffHandler:"
+ "updateSourceView shouldHostInAppSizedContainerView (%d)"
- "Presenting fullScreenViewController..."
- "actionForEnrollmentDismissed"
- "dismissViewController (FS) for endWritingTools"
- "enrollmentDismissed"
- "handoffFromUCBFromTool: %@."
- "isAvailable value changed: isMDMAllowed = %{bool}d, gmAvailable (current) = %{bool}d"
- "isWritingToolsAllowed"
- "sharedConnection"

```
