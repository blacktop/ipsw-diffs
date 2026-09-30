## WritingToolsUI

> `/System/Library/PrivateFrameworks/WritingToolsUI.framework/WritingToolsUI`

```diff

-68.0.0.0.0
-  __TEXT.__text: 0x3299c
-  __TEXT.__auth_stubs: 0xca0
-  __TEXT.__objc_methlist: 0x3bc4
-  __TEXT.__const: 0xb04
-  __TEXT.__cstring: 0x249e
-  __TEXT.__oslogstring: 0xf70
+72.0.0.0.0
+  __TEXT.__text: 0x32ca4
+  __TEXT.__auth_stubs: 0xc90
+  __TEXT.__objc_methlist: 0x3cc4
+  __TEXT.__const: 0xa54
+  __TEXT.__cstring: 0x234e
+  __TEXT.__oslogstring: 0xf55
   __TEXT.__gcc_except_tab: 0xa58
   __TEXT.__dlopen_cstrs: 0xb4
-  __TEXT.__constg_swiftt: 0x5ac
-  __TEXT.__swift5_typeref: 0x2ea
+  __TEXT.__constg_swiftt: 0x5a8
+  __TEXT.__swift5_typeref: 0x2dc
   __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_reflstr: 0x4fe
-  __TEXT.__swift5_fieldmd: 0x440
+  __TEXT.__swift5_reflstr: 0x311
+  __TEXT.__swift5_fieldmd: 0x364
   __TEXT.__swift5_assocty: 0xa8
-  __TEXT.__swift5_proto: 0x44
-  __TEXT.__swift5_types: 0x3c
+  __TEXT.__swift5_proto: 0x38
+  __TEXT.__swift5_types: 0x38
   __TEXT.__swift5_capture: 0x70
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0xef8
+  __TEXT.__unwind_info: 0xef0
   __TEXT.__eh_frame: 0xf8
-  __TEXT.__objc_classname: 0x645
-  __TEXT.__objc_methname: 0x9c9c
-  __TEXT.__objc_methtype: 0x2111
-  __TEXT.__objc_stubs: 0x6940
-  __DATA_CONST.__got: 0x500
-  __DATA_CONST.__const: 0x9d8
+  __TEXT.__objc_classname: 0x662
+  __TEXT.__objc_methname: 0x9e37
+  __TEXT.__objc_methtype: 0x211c
+  __TEXT.__objc_stubs: 0x6ac0
+  __DATA_CONST.__got: 0x4f8
+  __DATA_CONST.__const: 0x9c8
   __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0xd8
+  __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2680
+  __DATA_CONST.__objc_selrefs: 0x26f8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xb0
-  __AUTH_CONST.__auth_got: 0x660
-  __AUTH_CONST.__const: 0x7d8
+  __AUTH_CONST.__auth_got: 0x658
+  __AUTH_CONST.__const: 0x760
   __AUTH_CONST.__cfstring: 0xa60
-  __AUTH_CONST.__objc_const: 0x5298
-  __AUTH_CONST.__objc_intobj: 0x438
-  __AUTH.__objc_data: 0x1030
+  __AUTH_CONST.__objc_const: 0x5378
+  __AUTH_CONST.__objc_intobj: 0x480
+  __AUTH.__objc_data: 0x1050
   __AUTH.__data: 0x208
-  __DATA.__objc_ivar: 0x2b0
-  __DATA.__data: 0xbe8
-  __DATA.__bss: 0x9c0
-  __DATA.__common: 0x70
+  __DATA.__objc_ivar: 0x2b8
+  __DATA.__data: 0xc40
+  __DATA.__bss: 0x8c0
+  __DATA.__common: 0x78
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__data: 0x28
-  __DATA_DIRTY.__bss: 0x90
+  __DATA_DIRTY.__data: 0x20
+  __DATA_DIRTY.__bss: 0x10
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/BrowserEngineKit.framework/BrowserEngineKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
-  - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/GenerativeAssistantSettings.framework/GenerativeAssistantSettings
   - /System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 537B5946-2FB9-3156-A1A3-B5E69BDAFAC5
-  Functions: 1503
-  Symbols:   4144
-  CStrings:  2381
+  UUID: 97FD4455-9ABB-3832-8948-A3B576C4BF4E
+  Functions: 1511
+  Symbols:   4174
+  CStrings:  2390
 
Symbols:
+ +[WTUIActionHostToClient actionForSetRemainingRedoCount:]
+ +[WTUIActionHostToClient actionForSetRemainingUndoCount:]
+ -[WTMainPopoverViewController setRemainingRedoCount:]
+ -[WTMainPopoverViewController setRemainingUndoCount:]
+ -[WTSceneHostedInputDashboardViewController setRemainingRedoCount:]
+ -[WTSceneHostedInputDashboardViewController setRemainingUndoCount:]
+ -[WTWritingToolsController _sendUpdatedUndoRedoCounts]
+ -[WTWritingToolsController remainingRedoCount]
+ -[WTWritingToolsController remainingUndoCount]
+ -[WTWritingToolsController setRemainingRedoCount:]
+ -[WTWritingToolsController setRemainingUndoCount:]
+ GCC_except_table111
+ GCC_except_table129
+ GCC_except_table156
+ _OBJC_IVAR_$_WTWritingToolsController._remainingRedoCount
+ _OBJC_IVAR_$_WTWritingToolsController._remainingUndoCount
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_WTTextViewDelegate_Internal
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WTTextViewDelegate_Internal
+ __OBJC_$_PROTOCOL_REFS_WTTextViewDelegate_Internal
+ __OBJC_LABEL_PROTOCOL_$_WTTextViewDelegate_Internal
+ __OBJC_PROTOCOL_$_WTTextViewDelegate_Internal
+ ___75-[WTWritingToolsController _presentSuggestionViewControllerWithCompletion:]_block_invoke.652
+ _keypath_get.20Tm
+ _keypath_get.22Tm
+ _keypath_get.28Tm
+ _keypath_get.40Tm
+ _keypath_set.23Tm
+ _objc_msgSend$_sendUpdatedUndoRedoCounts
+ _objc_msgSend$actionForSetRemainingRedoCount:
+ _objc_msgSend$actionForSetRemainingUndoCount:
+ _objc_msgSend$canRedo
+ _objc_msgSend$canUndo
+ _objc_msgSend$includesTextListMarkers
+ _objc_msgSend$remainingRedoCount
+ _objc_msgSend$remainingUndoCount
+ _objc_msgSend$setIncludesTextListMarkers:
+ _objc_msgSend$setRemainingRedoCount:
+ _objc_msgSend$setRemainingUndoCount:
+ _objc_msgSend$unsignedIntValue
+ _objc_retain_x28
- GCC_except_table108
- GCC_except_table123
- GCC_except_table153
- GCC_except_table43
- _OBJC_CLASS_$_UITraitCollection
- ___75-[WTWritingToolsController _presentSuggestionViewControllerWithCompletion:]_block_invoke.648
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_WritingToolsUI
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_WritingToolsUI
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_WritingToolsUI
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_WritingToolsUI
- _associated conformance 14WritingToolsUI0aB0OSHAASQ
- _keypath_get.19Tm
- _keypath_get.21Tm
- _keypath_get.27Tm
- _keypath_get.39Tm
- _keypath_set.22Tm
- _objc_retain_x26
- _symbolic _____ 14WritingToolsUI0aB0O
CStrings:
+ "@24@0:8Q16"
+ "TB,N,VincludesTextListMarkers"
+ "TQ,N,V_remainingRedoCount"
+ "TQ,N,V_remainingUndoCount"
+ "WTTextViewDelegate_Internal"
+ "_remainingRedoCount"
+ "_remainingUndoCount"
+ "_sendUpdatedUndoRedoCounts"
+ "actionForSetRemainingRedoCount:"
+ "actionForSetRemainingUndoCount:"
+ "canRedo"
+ "canUndo"
+ "hostDidAddRemoteView"
+ "inputWarningDidDismiss"
+ "isAvailable value changed: isMDMAllowed = %{bool}d, gmAvailable (current) = %{bool}d"
+ "notifyHostIsReady"
+ "popoverDidCloseTransiently"
+ "popoverDidDetach"
+ "remainingRedoCount"
+ "remainingUndoCount"
+ "setIncludesTextListMarkers:"
+ "setRemainingRedoCount:"
+ "setRemainingUndoCount:"
+ "unsignedIntValue"
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
- "currentTraitCollection"
- "isAvailable value changed: featureEnabled = %{bool}d, isMDMAllowed = %{bool}d, gmAvailable (current) = %{bool}d"

```
