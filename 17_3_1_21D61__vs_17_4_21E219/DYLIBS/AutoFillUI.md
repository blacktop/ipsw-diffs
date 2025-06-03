## AutoFillUI

> `/System/Library/PrivateFrameworks/AutoFillUI.framework/AutoFillUI`

```diff

-56.210.1.0.0
-  __TEXT.__text: 0x1c3dc
-  __TEXT.__auth_stubs: 0x640
-  __TEXT.__objc_methlist: 0x17ac
+56.308.0.0.0
+  __TEXT.__text: 0x1d060
+  __TEXT.__auth_stubs: 0x650
+  __TEXT.__objc_methlist: 0x183c
   __TEXT.__const: 0xd8
-  __TEXT.__cstring: 0x1684
-  __TEXT.__gcc_except_tab: 0x4f8
+  __TEXT.__cstring: 0x1746
+  __TEXT.__gcc_except_tab: 0x4c0
   __TEXT.__ustring: 0xb0
   __TEXT.__dlopen_cstrs: 0x104
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0x7b0
-  __TEXT.__objc_classname: 0x42c
-  __TEXT.__objc_methname: 0x6f5a
-  __TEXT.__objc_methtype: 0x1aaf
-  __TEXT.__objc_stubs: 0x5420
+  __TEXT.__unwind_info: 0x7ac
+  __TEXT.__objc_classname: 0x4e1
+  __TEXT.__objc_methname: 0x83b6
+  __TEXT.__objc_methtype: 0x24ba
+  __TEXT.__objc_stubs: 0x5500
   __DATA_CONST.__got: 0x258
-  __DATA_CONST.__const: 0x8a0
+  __DATA_CONST.__const: 0x8d8
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x98
+  __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x52b0
-  __DATA_CONST.__objc_selrefs: 0x17e8
+  __DATA_CONST.__objc_const: 0x7990
+  __DATA_CONST.__objc_selrefs: 0x1820
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_classrefs: 0x2b8
+  __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_arraydata: 0xc8
-  __AUTH_CONST.__cfstring: 0x1460
+  __AUTH_CONST.__cfstring: 0x14e0
   __AUTH_CONST.__objc_const: 0x9b8
   __AUTH_CONST.__const: 0x3e0
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x330
+  __AUTH_CONST.__auth_got: 0x338
   __AUTH.__objc_data: 0x550
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x2c0
-  __DATA.__objc_superrefs: 0x88
-  __DATA.__objc_ivar: 0x1cc
-  __DATA.__data: 0x768
-  __DATA.__bss: 0xf0
+  __DATA.__objc_ivar: 0x1d4
+  __DATA.__data: 0xa08
+  __DATA.__bss: 0xe8
   __DATA_DIRTY.__objc_data: 0x1e0
-  __DATA_DIRTY.__bss: 0xe0
+  __DATA_DIRTY.__bss: 0xe8
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/ContactsUI.framework/ContactsUI
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/WebKitLegacy.framework/WebKitLegacy
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CF0CE668-BE46-3262-B088-29B00BD0997F
-  Functions: 696
-  Symbols:   2951
-  CStrings:  1733
+  UUID: 2D7CC898-8E17-343F-A806-8EA0CC01825C
+  Functions: 713
+  Symbols:   3045
+  CStrings:  1991
 
Symbols:
+ -[AFUIExplicitAutoFillController contactsUIDidEndForSessionUUID:completion:]
+ -[AFUIExplicitAutoFillController contactsUIWillBeginForSessionUUID:completion:]
+ -[AFUIExplicitAutoFillController passwordsUIDidEndForSessionUUID:completion:]
+ -[AFUIExplicitAutoFillController passwordsUIWillBeginForSessionUUID:completion:]
+ -[AFUIPanel passwordsUIWillBeginForSessionUUID:completion:]
+ -[AFUIPasswordsController presentPasswordPickerFromViewController:didFinishAuthenticationBlock:]
+ -[AFUIServiceDelegate contactsUIShowingForSessionId]
+ -[AFUIServiceDelegate inputSystemService:inputSessionDidBegin:options:].cold.6
+ -[AFUIServiceDelegate inputSystemService:inputSessionDidBegin:options:].cold.7
+ -[AFUIServiceDelegate inputSystemService:inputSessionDidEnd:options:].cold.4
+ -[AFUIServiceDelegate inputSystemService:inputSessionDidEnd:options:].cold.5
+ -[AFUIServiceDelegate passwordsUIShowingForSessionId]
+ -[AFUIServiceDelegate passwordsUIWillBeginForSessionUUID:completion:]
+ -[AFUIServiceDelegate setContactsUIShowingForSessionId:]
+ -[AFUIServiceDelegate setPasswordsUIShowingForSessionId:]
+ -[AFUITargetDetectionController cellularAutoFillModeWithCurrentResponder:currentTraits:allResponders:indexOfCurrent:]
+ GCC_except_table45
+ GCC_except_table47
+ GCC_except_table49
+ GCC_except_table69
+ _AFTextContentTypeCellularEIDStaging
+ _AFTextContentTypeCellularIMEIStaging
+ _AFTextContentTypeIsInCellularSet
+ _OBJC_IVAR_$_AFUIServiceDelegate._contactsUIShowingForSessionId
+ _OBJC_IVAR_$_AFUIServiceDelegate._passwordsUIShowingForSessionId
+ _OUTLINED_FUNCTION_8
+ __OBJC_$_PROP_LIST_BETextInput
+ __OBJC_$_PROP_LIST_UIAsyncTextInput
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BETextInput
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BETextSelectionDirectionNavigation
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BEResponderEditActions
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIAsyncTextInput
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIResponderStandardEditActions
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIWKInteractionViewProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_UITextSelectionDirectionNavigation
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_UIWKInteractionViewProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BEResponderEditActions
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BETextInput
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BETextSelectionDirectionNavigation
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UIAsyncTextInput
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UIResponderStandardEditActions
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UITextSelectionDirectionNavigation
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UIWKInteractionViewProtocol
+ __OBJC_$_PROTOCOL_REFS_BEResponderEditActions
+ __OBJC_$_PROTOCOL_REFS_BETextInput
+ __OBJC_$_PROTOCOL_REFS_UIAsyncTextInput
+ __OBJC_$_PROTOCOL_REFS_UIResponderStandardEditActions
+ __OBJC_LABEL_PROTOCOL_$_BEResponderEditActions
+ __OBJC_LABEL_PROTOCOL_$_BETextInput
+ __OBJC_LABEL_PROTOCOL_$_BETextSelectionDirectionNavigation
+ __OBJC_LABEL_PROTOCOL_$_UIAsyncTextInput
+ __OBJC_LABEL_PROTOCOL_$_UIResponderStandardEditActions
+ __OBJC_LABEL_PROTOCOL_$_UITextSelectionDirectionNavigation
+ __OBJC_LABEL_PROTOCOL_$_UIWKInteractionViewProtocol
+ __OBJC_PROTOCOL_$_BEResponderEditActions
+ __OBJC_PROTOCOL_$_BETextInput
+ __OBJC_PROTOCOL_$_BETextSelectionDirectionNavigation
+ __OBJC_PROTOCOL_$_UIAsyncTextInput
+ __OBJC_PROTOCOL_$_UIResponderStandardEditActions
+ __OBJC_PROTOCOL_$_UITextSelectionDirectionNavigation
+ __OBJC_PROTOCOL_$_UIWKInteractionViewProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_BETextInput
+ __OBJC_PROTOCOL_REFERENCE_$_UIAsyncTextInput
+ __OBJC_PROTOCOL_REFERENCE_$_UIWKInteractionViewProtocol
+ ___72-[AFUIExplicitAutoFillController _showPasswordsPanelFromViewController:]_block_invoke
+ ___72-[AFUIExplicitAutoFillController _showPasswordsPanelFromViewController:]_block_invoke_2
+ ___96-[AFUIPasswordsController presentPasswordPickerFromViewController:didFinishAuthenticationBlock:]_block_invoke
+ ___block_descriptor_56_e8_32s40s48bs_e8_v12?0B8ls48l8s32l8s40l8
+ ___block_literal_global.126
+ ___block_literal_global.141
+ ___block_literal_global.244
+ ___block_literal_global.307
+ ___block_literal_global.316
+ ___block_literal_global.61
+ __unnamed_array_storage.138
+ _objc_msgSend$cellularAutoFillModeWithCurrentResponder:currentTraits:allResponders:indexOfCurrent:
+ _objc_msgSend$contactsUIShowingForSessionId
+ _objc_msgSend$extendedTextInputTraits
+ _objc_msgSend$extendedTraitsDelegate
+ _objc_msgSend$passwordsUIShowingForSessionId
+ _objc_msgSend$passwordsUIWillBeginForSessionUUID:completion:
+ _objc_msgSend$presentPasswordPickerFromViewController:didFinishAuthenticationBlock:
+ _objc_msgSend$setContactsUIShowingForSessionId:
+ _objc_msgSend$setPasswordsUIShowingForSessionId:
+ _objc_retain_x26
- -[AFUIPasswordsController presentPasswordPickerFromViewController:]
- GCC_except_table44
- GCC_except_table46
- GCC_except_table48
- GCC_except_table68
- _OBJC_CLASS_$_DOMHTMLInputElement
- ___60-[AFUIExplicitAutoFillController presentFromViewController:]_block_invoke
- ___60-[AFUIExplicitAutoFillController presentFromViewController:]_block_invoke_2
- ___67-[AFUIPasswordsController presentPasswordPickerFromViewController:]_block_invoke
- ___block_literal_global.127
- ___block_literal_global.142
- ___block_literal_global.240
- ___block_literal_global.289
- ___block_literal_global.298
- ___block_literal_global.55
- ___block_literal_global.75
- __unnamed_array_storage.139
- _objc_msgSend$presentPasswordPickerFromViewController:
- _objc_msgSend$size
CStrings:
+ "\t"
+ "%s %@ is for a session being targeted by AutoFill which is in the Contact Picker UI %@"
+ "%s %@ is for a session being targeted by AutoFill which is in the Password Picker UI %@"
+ "@\"<BEExtendedTextInputTraits>\"16@0:8"
+ "@\"<BETextInputDelegate>\"16@0:8"
+ "@\"<UIAsyncTextInputDelegate>\"16@0:8"
+ "@\"<UIExtendedTextInputTraits>\"16@0:8"
+ "@\"<UITextInputTraits>\"16@0:8"
+ "@\"NSArray\"16@0:8"
+ "@\"NSAttributedString\"16@0:8"
+ "B32@0:8:16@24"
+ "B32@0:8{CGPoint=dd}16"
+ "B40@0:8q16{CGPoint=dd}24"
+ "BEResponderEditActions"
+ "BETextInput"
+ "BETextSelectionDirectionNavigation"
+ "T@\"<BEExtendedTextInputTraits>\",R,N"
+ "T@\"<BETextInputDelegate>\",W,N"
+ "T@\"<UIAsyncTextInputDelegate>\",?,W,N"
+ "T@\"<UIExtendedTextInputTraits>\",?,R,N"
+ "T@\"<UITextInputTraits>\",?,R,N"
+ "T@\"NSArray\",?,R,N"
+ "T@\"NSAttributedString\",?,R,N"
+ "T@\"NSAttributedString\",R,N"
+ "T@\"NSString\",?,C,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",?,R,N"
+ "T@\"NSString\",R"
+ "T@\"NSString\",R,N"
+ "T@\"NSUUID\",&,V_contactsUIShowingForSessionId"
+ "T@\"NSUUID\",&,V_passwordsUIShowingForSessionId"
+ "T@\"UITextInputPasswordRules\",?,C,N"
+ "T@\"UITextRange\",?,C"
+ "T@\"UITextRange\",?,R,N"
+ "T@\"UIView\",?,R,N"
+ "T@,?,R,N"
+ "TB,?,N"
+ "TB,?,N,GisSecureTextEntry"
+ "TB,?,R,N"
+ "TB,?,R,N,GisReplaceAllowed"
+ "TB,R,N,GisEditable"
+ "TB,R,N,GisReplaceAllowed"
+ "TB,R,N,GisSelectionAtDocumentStart"
+ "Tq,?,N"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},?,R,N"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N"
+ "UIAsyncTextInput"
+ "UIResponderStandardEditActions"
+ "UITextSelectionDirectionNavigation"
+ "UIWKInteractionViewProtocol"
+ "_cancelLongPressGestureRecognizer"
+ "_contactsUIShowingForSessionId"
+ "_passwordsUIShowingForSessionId"
+ "addShortcut:"
+ "addTextAlternatives:"
+ "adjustSelectionBoundaryToPoint:touchPhase:baseIsStart:flags:"
+ "adjustSelectionByRange:completionHandler:"
+ "adjustSelectionWithDelta:completionHandler:"
+ "alternativesForSelectedText"
+ "applyAutocorrection:toString:shouldUnderline:withCompletionHandler:"
+ "applyAutocorrection:toString:withCompletionHandler:"
+ "asyncInputDelegate"
+ "asyncSystemInputDelegate"
+ "attributedMarkedText"
+ "automaticallyPresentEditMenu"
+ "autoscrollToPoint:"
+ "beginSelectionInDirection:completionHandler:"
+ "canPerformAction:withSender:"
+ "cancelAutoscroll"
+ "caretTransformForPosition:"
+ "cellularAutoFillModeWithCurrentResponder:currentTraits:allResponders:indexOfCurrent:"
+ "changeSelectionWithGestureAt:withGesture:withState:"
+ "changeSelectionWithTouchAt:withSelectionTouch:baseIsStart:withFlags:"
+ "changeSelectionWithTouchesFrom:to:withGesture:withState:"
+ "clearSelection"
+ "contactsUIShowingForSessionId"
+ "copy:"
+ "cut:"
+ "decreaseSize:"
+ "delete:"
+ "deleteInDirection:toGranularity:"
+ "didInsertFinalDictationResult"
+ "duplicate:"
+ "editable"
+ "esim-eid"
+ "esim-imei"
+ "export:"
+ "extendInDirection:byGranularity:"
+ "extendInLayoutDirection:"
+ "extendInStorageDirection:byGranularity:"
+ "extendedTextInputTraits"
+ "extendedTraitsDelegate"
+ "find:"
+ "findAndReplace:"
+ "findNext:"
+ "findPrevious:"
+ "findSelected:"
+ "handleAsyncKeyEvent:withCompletionHandler:"
+ "handleKeyEntry:withCompletionHandler:"
+ "hasMarkedText"
+ "hasSelectablePositionAtPoint:"
+ "increaseSize:"
+ "insertTextAlternatives:"
+ "insertTextPlaceholderWithSize:completionHandler:"
+ "insertTextSuggestion:"
+ "inverseScale"
+ "isEditable"
+ "isPointNearMarkedText:"
+ "isReplaceAllowed"
+ "isSelectionAtDocumentStart"
+ "lookup:"
+ "makeTextWritingDirectionLeftToRight:"
+ "makeTextWritingDirectionRightToLeft:"
+ "markedText"
+ "move:"
+ "moveByOffset:"
+ "moveInDirection:byGranularity:"
+ "moveInLayoutDirection:"
+ "moveInStorageDirection:byGranularity:"
+ "moveSelectionAtBoundary:inDirection:completionHandler:"
+ "moveSelectionAtBoundary:inStorageDirection:completionHandler:"
+ "passwordViewController:fillText:"
+ "passwordsUIShowingForSessionId"
+ "passwordsUIWillBeginForSessionUUID:completion:"
+ "paste:"
+ "pasteAndGo:"
+ "pasteAndMatchStyle:"
+ "pasteAndSearch:"
+ "pasteWithCompletionHandler:"
+ "pointIsNearMarkedText:"
+ "prepareSelectionForContextMenuWithLocationInView:completionHandler:"
+ "presentPasswordPickerFromViewController:didFinishAuthenticationBlock:"
+ "print:"
+ "promptForReplace:"
+ "removeAnnotation:forSelectionOffset:length:"
+ "removeTextPlaceholder:willInsertText:completionHandler:"
+ "rename:"
+ "replace:"
+ "replaceAllowed"
+ "replaceDictatedText:withText:"
+ "replaceSelectedText:withText:"
+ "replaceSelectionOffset:length:withAnnotatedString:relativeReplacementRange:"
+ "replaceText:withText:"
+ "replaceText:withText:options:completionHandler:"
+ "replaceText:withText:options:withCompletionHandler:"
+ "replacedAllowed"
+ "requestAutocorrectionContextWithCompletionHandler:"
+ "requestAutocorrectionRectsForString:withCompletionHandler:"
+ "requestDictationContext:"
+ "requestDocumentContext:completionHandler:"
+ "requestPreferredArrowDirectionForEditMenuWithCompletionHandler:"
+ "requestRVItemInSelectedRangeWithCompletionHandler:"
+ "requestTextContextForAutocorrectionWithCompletionHandler:"
+ "requestTextRectsForString:withCompletionHandler:"
+ "select:"
+ "selectAll:"
+ "selectPositionAtBoundary:inDirection:fromPoint:completionHandler:"
+ "selectPositionAtPoint:completionHandler:"
+ "selectPositionAtPoint:withContextRequest:completionHandler:"
+ "selectTextForEditMenuWithLocationInView:completionHandler:"
+ "selectTextInGranularity:atPoint:completionHandler:"
+ "selectTextWithGranularity:atPoint:completionHandler:"
+ "selectWordBackward"
+ "selectWordForReplacement"
+ "selectedText"
+ "selectionAtDocumentStart"
+ "selectionClipRect"
+ "setAsyncInputDelegate:"
+ "setAsyncSystemInputDelegate:"
+ "setContactsUIShowingForSessionId:"
+ "setPasswordsUIShowingForSessionId:"
+ "setSelectionFromPoint:toPoint:gesture:state:"
+ "share:"
+ "shiftKeyStateChangedFrom:to:"
+ "shiftKeyStateChangedFromState:toState:"
+ "shouldAllowHidingSelectionCommands"
+ "shouldSuppressUpdateCandidateView"
+ "systemWillDismissEditMenuWithAnimator:"
+ "systemWillPresentEditMenuWithAnimator:"
+ "textFirstRect"
+ "textInteractionGesture:shouldBeginAtPoint:"
+ "textLastRect"
+ "toggleBoldface:"
+ "toggleItalics:"
+ "toggleUnderline:"
+ "translate:"
+ "transliterateChinese:"
+ "transposeCharacters"
+ "transposeCharactersAroundSelection"
+ "unobscuredContentRect"
+ "unscaledView"
+ "updateCurrentSelectionTo:fromGesture:inState:"
+ "updateSelectionWithExtentPoint:boundary:completionHandler:"
+ "updateSelectionWithExtentPoint:completionHandler:"
+ "updateSelectionWithExtentPoint:withBoundary:completionHandler:"
+ "updateTextAttributesWithConversionHandler:"
+ "useSelectionForFind:"
+ "v24@0:8@\"<BETextInputDelegate>\"16"
+ "v24@0:8@\"<UIAsyncTextInputDelegate>\"16"
+ "v24@0:8@\"BETextAlternatives\"16"
+ "v24@0:8@\"BETextSuggestion\"16"
+ "v24@0:8@\"NSTextAlternatives\"16"
+ "v24@0:8@\"UITextSuggestion\"16"
+ "v24@0:8@?<@\"NSDictionary\"@?@\"NSDictionary\">16"
+ "v24@0:8@?<v@?>16"
+ "v24@0:8@?<v@?@\"BETextDocumentContext\">16"
+ "v24@0:8@?<v@?@\"NSString\"@\"NSString\"@\"NSString\">16"
+ "v24@0:8@?<v@?@\"RVItem\">16"
+ "v24@0:8@?<v@?@\"UIWKAutocorrectionContext\">16"
+ "v24@0:8@?<v@?@\"UIWKDocumentContext\">16"
+ "v24@0:8@?<v@?q>16"
+ "v32@0:8@\"BEKeyEntry\"16@?<v@?@\"BEKeyEntry\"B>24"
+ "v32@0:8@\"BETextDocumentRequest\"16@?<v@?@\"BETextDocumentContext\">24"
+ "v32@0:8@\"NSString\"16@\"NSString\"24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSArray\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"UIWKAutocorrectionRects\">24"
+ "v32@0:8@\"UIKeyEvent\"16@?<v@?@\"UIKeyEvent\"B>24"
+ "v32@0:8@\"UIWKDocumentRequest\"16@?<v@?@\"UIWKDocumentContext\">24"
+ "v32@0:8q16@?24"
+ "v32@0:8q16@?<v@?B>24"
+ "v32@0:8q16q24"
+ "v36@0:8@\"UITextPlaceholder\"16B24@?<v@?>28"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"UIWKAutocorrectionRects\">32"
+ "v40@0:8@\"NSString\"16q24Q32"
+ "v40@0:8@16q24Q32"
+ "v40@0:8q16q24@?32"
+ "v40@0:8q16q24@?<v@?>32"
+ "v40@0:8{?=qq}16@?32"
+ "v40@0:8{?=qq}16@?<v@?>32"
+ "v40@0:8{CGPoint=dd}16@?32"
+ "v40@0:8{CGPoint=dd}16@?<v@?>32"
+ "v40@0:8{CGPoint=dd}16@?<v@?B>32"
+ "v40@0:8{CGPoint=dd}16@?<v@?B@\"NSString\"{_NSRange=QQ}>32"
+ "v40@0:8{CGPoint=dd}16@?<v@?B@\"RVItem\">32"
+ "v40@0:8{CGSize=dd}16@?32"
+ "v40@0:8{CGSize=dd}16@?<v@?@\"UITextPlaceholder\">32"
+ "v40@0:8{_NSRange=QQ}16@?32"
+ "v40@0:8{_NSRange=QQ}16@?<v@?>32"
+ "v44@0:8@\"NSString\"16@\"NSString\"24B32@?<v@?@\"UIWKAutocorrectionRects\">36"
+ "v44@0:8@16@24B32@?36"
+ "v48@0:8@\"NSString\"16@\"NSString\"24Q32@?<v@?@\"NSArray\">40"
+ "v48@0:8@16@24Q32@?40"
+ "v48@0:8q16{CGPoint=dd}24@?40"
+ "v48@0:8q16{CGPoint=dd}24@?<v@?>40"
+ "v48@0:8{CGPoint=dd}16@\"BETextDocumentRequest\"32@?<v@?@\"BETextDocumentContext\">40"
+ "v48@0:8{CGPoint=dd}16@\"UIWKDocumentRequest\"32@?<v@?@\"UIWKDocumentContext\">40"
+ "v48@0:8{CGPoint=dd}16@32@?40"
+ "v48@0:8{CGPoint=dd}16q32@?40"
+ "v48@0:8{CGPoint=dd}16q32@?<v@?B>40"
+ "v48@0:8{CGPoint=dd}16q32q40"
+ "v52@0:8{CGPoint=dd}16q32B40Q44"
+ "v52@0:8{CGPoint=dd}16q32B40q44"
+ "v56@0:8q16Q24@\"NSAttributedString\"32{_NSRange=QQ}40"
+ "v56@0:8q16Q24@32{_NSRange=QQ}40"
+ "v56@0:8q16q24{CGPoint=dd}32@?48"
+ "v56@0:8q16q24{CGPoint=dd}32@?<v@?>48"
+ "v64@0:8{CGPoint=dd}16{CGPoint=dd}32q48q56"
+ "webSelectionRects"
+ "willFinishIgnoringCalloutBarFadeAfterPerformingAction"
+ "willInsertFinalDictationResult"
+ "{CGAffineTransform=dddddd}24@0:8@\"UITextPosition\"16"
+ "{CGAffineTransform=dddddd}24@0:8@16"
- "\a"
- "T@\"NSString\",C,N"
- "T@\"UITextInputPasswordRules\",C,N"
- "T@,R,N"
- "TB,N,GisSecureTextEntry"
- "Tq,N"
- "presentPasswordPickerFromViewController:"
- "size"

```
