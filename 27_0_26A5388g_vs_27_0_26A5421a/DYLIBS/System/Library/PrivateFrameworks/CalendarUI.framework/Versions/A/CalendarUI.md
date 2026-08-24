## CalendarUI

> `/System/Library/PrivateFrameworks/CalendarUI.framework/Versions/A/CalendarUI`

```diff

-1277.0.0.0.0
-  __TEXT.__text: 0x11ccb8
-  __TEXT.__objc_methlist: 0x142dc
-  __TEXT.__const: 0x1874
-  __TEXT.__cstring: 0x7fef
-  __TEXT.__gcc_except_tab: 0x1160
+1281.0.0.0.0
+  __TEXT.__text: 0x122b20
+  __TEXT.__objc_methlist: 0x144cc
+  __TEXT.__const: 0x1914
+  __TEXT.__cstring: 0x811f
+  __TEXT.__gcc_except_tab: 0x11d0
   __TEXT.__oslogstring: 0x1dfd
   __TEXT.__ustring: 0x492
-  __TEXT.__swift5_typeref: 0x12c2
-  __TEXT.__swift5_capture: 0x568
-  __TEXT.__swift5_fieldmd: 0x64c
-  __TEXT.__constg_swiftt: 0xa64
-  __TEXT.__swift5_reflstr: 0x76f
+  __TEXT.__swift5_typeref: 0x13a6
+  __TEXT.__swift5_capture: 0x67c
+  __TEXT.__swift5_fieldmd: 0x6c4
+  __TEXT.__constg_swiftt: 0xb2c
+  __TEXT.__swift5_reflstr: 0x85f
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_assocty: 0x100
   __TEXT.__swift5_proto: 0x50

   __TEXT.__swift_as_entry: 0x28
   __TEXT.__swift_as_ret: 0x20
   __TEXT.__swift_as_cont: 0x48
-  __TEXT.__unwind_info: 0x4378
+  __TEXT.__unwind_info: 0x44d0
   __TEXT.__eh_frame: 0x8cc
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5c0
-  __DATA_CONST.__objc_classlist: 0x8a0
+  __DATA_CONST.__const: 0x5e0
+  __DATA_CONST.__objc_classlist: 0x8a8
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x280
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb6f0
+  __DATA_CONST.__objc_selrefs: 0xb800
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x650
+  __DATA_CONST.__objc_superrefs: 0x658
   __DATA_CONST.__objc_arraydata: 0x388
-  __DATA_CONST.__got: 0x1888
-  __AUTH_CONST.__const: 0x3278
-  __AUTH_CONST.__cfstring: 0x9d40
-  __AUTH_CONST.__objc_const: 0x1d670
-  __AUTH_CONST.__objc_intobj: 0x690
+  __DATA_CONST.__got: 0x18b8
+  __AUTH_CONST.__const: 0x35b0
+  __AUTH_CONST.__cfstring: 0x9d60
+  __AUTH_CONST.__objc_const: 0x1d998
+  __AUTH_CONST.__objc_intobj: 0x6a8
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x1e0
   __AUTH_CONST.__objc_doubleobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH_CONST.__auth_got: 0x1148
-  __AUTH.__objc_data: 0x3348
+  __AUTH_CONST.__auth_got: 0x1230
+  __AUTH.__objc_data: 0x34a0
   __AUTH.__data: 0x570
-  __DATA.__objc_ivar: 0x13f8
-  __DATA.__data: 0x23e8
-  __DATA.__bss: 0xdc8
-  __DATA.__common: 0x28
+  __DATA.__objc_ivar: 0x1418
+  __DATA.__data: 0x2438
+  __DATA.__bss: 0xdd8
+  __DATA.__common: 0x38
   __DATA_DIRTY.__objc_data: 0x2bc0
   __DATA_DIRTY.__bss: 0x3f0
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7076
-  Symbols:   16100
-  CStrings:  1584
+  Functions: 7197
+  Symbols:   16208
+  CStrings:  1591
 
Symbols:
+ -[EKEventViewControllerDefaultImpl disableMagicComposeForSession]
+ -[EKEventViewControllerDefaultImpl timeImplicitlySetForSuggestedEvents]
+ -[EKEventViewControllerDefaultImpl unminimizeTitleFieldForSummaryButton]
+ -[EKEventViewControllerDefaultImpl updateWithTitle:animate:]
+ -[EKUIColorBarGadgetContainer _animateRevealFieldHidingSummaryButton]
+ -[EKUIColorBarGadgetContainer _resetSummaryButtonTitle]
+ -[EKUIColorBarGadgetContainer _revealSummaryButtonForError]
+ -[EKUIColorBarGadgetContainer _setupSummaryButtonOverMagicComposeView:]
+ -[EKUIColorBarGadgetContainer _summaryButtonTapped:]
+ -[EKUIColorBarGadgetContainer _updateSummaryButtonTitle:]
+ -[EKUIColorBarGadgetContainer setSummaryButton:]
+ -[EKUIColorBarGadgetContainer summaryButton]
+ -[EKUIMagicComposeGadget ignoreChangesForBackwardPassDuringNextSave]
+ -[EKUIMagicComposeGadget prepareForRemovalFromSession]
+ -[EKUIMagicComposeGadget savePendingChanges]
+ -[EKUIMagicComposeGadget setIgnoreChangesForBackwardPassDuringNextSave:]
+ -[EKUIMagicComposeGadget setSummarizerErrorPlaceholderChangedHandler:]
+ -[EKUIMagicComposeGadget summarizeExistingEventIfNeeded:]
+ -[EKUISummaryButton .cxx_destruct]
+ -[EKUISummaryButton _isDarkMode]
+ -[EKUISummaryButton _pinToOverlayFieldIfNeeded]
+ -[EKUISummaryButton hitTest:]
+ -[EKUISummaryButton initWithFrame:]
+ -[EKUISummaryButton interactionDisabled]
+ -[EKUISummaryButton layout]
+ -[EKUISummaryButton mouseEntered:]
+ -[EKUISummaryButton mouseExited:]
+ -[EKUISummaryButton overlayField]
+ -[EKUISummaryButton setInteractionDisabled:]
+ -[EKUISummaryButton setOverlayField:]
+ -[EKUISummaryButton updateConstraints]
+ -[EKUISummaryButton updateLayer]
+ -[EKUISummaryButton updateTrackingAreas]
+ -[EKUISummaryButton wantsUpdateLayer]
+ GCC_except_table23
+ GCC_except_table28
+ GCC_except_table30
+ OBJC_IVAR_$_EKUIColorBarGadgetContainer._linearSplitGeneration
+ OBJC_IVAR_$_EKUIColorBarGadgetContainer._summaryButton
+ OBJC_IVAR_$_EKUIColorBarGadgetContainer._summaryButtonTransitionGeneration
+ OBJC_IVAR_$_EKUIMagicComposeGadget._ignoreChangesForBackwardPassDuringNextSave
+ OBJC_IVAR_$_EKUISummaryButton._interactionDisabled
+ OBJC_IVAR_$_EKUISummaryButton._isHovering
+ OBJC_IVAR_$_EKUISummaryButton._overlayField
+ OBJC_IVAR_$_EKUISummaryButton._pinConstraints
+ OBJC_IVAR_$_EKUISummaryButton._trackingArea
+ _OBJC_CLASS_$_CUIKMagicComposeField
+ _OBJC_CLASS_$_EKUISummaryButton
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_METACLASS_$_EKUISummaryButton
+ __69-[EKUIColorBarGadgetContainer _animateRevealFieldHidingSummaryButton]_block_invoke
+ __CFCharacterSetIsLongCharacterMemberForInline
+ __OBJC_$_INSTANCE_METHODS_EKUISummaryButton
+ __OBJC_$_INSTANCE_VARIABLES_EKUISummaryButton
+ __OBJC_$_PROP_LIST_EKUISummaryButton
+ __OBJC_CLASS_RO_$_EKUISummaryButton
+ __OBJC_METACLASS_RO_$_EKUISummaryButton
+ ___52-[EKUIColorBarGadgetContainer _summaryButtonTapped:]_block_invoke
+ ___53-[EKUIColorBarGadgetContainer setMagicComposeGadget:]_block_invoke
+ ___57-[EKUIMagicComposeGadget summarizeExistingEventIfNeeded:]_block_invoke
+ ___59-[EKUIColorBarGadgetContainer _revealSummaryButtonForError]_block_invoke
+ ___59-[EKUIColorBarGadgetContainer _revealSummaryButtonForError]_block_invoke_2
+ ___60-[EKEventViewControllerDefaultImpl updateWithTitle:animate:]_block_invoke
+ ___65-[EKEventViewControllerDefaultImpl disableMagicComposeForSession]_block_invoke
+ ___69-[EKUIColorBarGadgetContainer _animateRevealFieldHidingSummaryButton]_block_invoke
+ ___71-[EKUIColorBarGadgetContainer _setupSummaryButtonOverMagicComposeView:]_block_invoke
+ ___block_descriptor_40_e8_32w_e18_v16?0"NSString"8l
+ ___block_descriptor_40_e8_32w_e23_"NSViewController"8?0l
+ ___block_descriptor_56_e8_32s40w_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s_e5_v8?0l
+ ___block_descriptor_73_e8_32s40s_e5_v8?0l
+ ___swift_memcpy144_8
+ __swift_closure_destructor.21Tm
+ __swift_closure_destructor.59Tm
+ _objc_msgSend$_animateRevealFieldHidingSummaryButton
+ _objc_msgSend$_isDarkMode
+ _objc_msgSend$_pinToOverlayFieldIfNeeded
+ _objc_msgSend$_resetSummaryButtonTitle
+ _objc_msgSend$_revealSummaryButtonForError
+ _objc_msgSend$_setupSummaryButtonOverMagicComposeView:
+ _objc_msgSend$_updateSummaryButtonTitle:
+ _objc_msgSend$accessibilityDisplayShouldReduceMotion
+ _objc_msgSend$armSummaryLoadingPlaceholderOnFocusWithCompletion:
+ _objc_msgSend$disableMagicComposeForSession
+ _objc_msgSend$disambiguated
+ _objc_msgSend$ignoreChangesForBackwardPassDuringNextSave
+ _objc_msgSend$initWithPresenterProvider:
+ _objc_msgSend$overlayField
+ _objc_msgSend$performWithoutNotifyingOfTextChange:
+ _objc_msgSend$prepareForRemovalFromSession
+ _objc_msgSend$rawPromptText
+ _objc_msgSend$setIgnoreChangesForBackwardPassDuringNextSave:
+ _objc_msgSend$setInteractionDisabled:
+ _objc_msgSend$setMoveCursorToEndOnBecomeFirstResponder:
+ _objc_msgSend$setOnSummarizerErrorPlaceholderChanged:
+ _objc_msgSend$setOverlayField:
+ _objc_msgSend$setRawPromptText:
+ _objc_msgSend$setSummarizerErrorPlaceholderChangedHandler:
+ _objc_msgSend$setSummaryButton:
+ _objc_msgSend$setSuppressSelectionNotifications:
+ _objc_msgSend$summarizeExistingEventIfNeeded:
+ _objc_msgSend$summaryButton
+ _objc_msgSend$timeImplicitlySetForSuggestedEvents
+ _objc_msgSend$updateWithTitle:animate:
+ _objc_msgSend$viewControllerToShowPresentationSheet
+ _swift_weakDestroy
+ _swift_weakInit
+ _swift_weakLoadStrong
+ _symbolic SSSgIegg_
+ _symbolic SSSgytIegnr_
+ _symbolic Say_____G 8Dispatch0A13WorkItemFlagsV
+ _symbolic Si
+ _symbolic So16NSViewControllerCSgIeyBa_
+ _symbolic So16NSViewControllerCSgyc
+ _symbolic So21CUIKMagicComposeFieldC
+ _symbolic So21CUIKMagicComposeFieldCSgXw
+ _symbolic So21CUIKMagicComposeFieldCSgXwz_Xx
+ _symbolic So8NSStringCSgIeyBy_
+ _symbolic _____SgXw 13CalendarUIKit27MagicComposePromptViewModelC
+ _symbolic _____SgXwz_Xx 13CalendarUIKit27MagicComposePromptViewModelC
+ _symbolic ______p s5ErrorP
+ _symbolic ySSSgcSg
- -[EKEventViewControllerDefaultImpl splitMagicComposeOnEventSuggestion]
- -[EKEventViewControllerDefaultImpl updateWithTitle:]
- OBJC_IVAR_$_EKEventViewControllerDefaultImpl._shouldAnimateTitleUpdate
- _CFCharacterSetIsLongCharacterMember
- ___52-[EKEventViewControllerDefaultImpl updateWithTitle:]_block_invoke
- ___70-[EKEventViewControllerDefaultImpl splitMagicComposeOnEventSuggestion]_block_invoke
- ___block_descriptor_64_e8_32s40s_e5_v8?0l
- ___block_descriptor_65_e8_32s40s_e5_v8?0l
- __swift_closure_destructor.53Tm
- _objc_msgSend$initWithPresenter:
- _objc_msgSend$markPromptFieldAsDisambiguated
- _objc_msgSend$splitMagicComposeOnEventSuggestion
- _objc_msgSend$updateWithTitle:
- _symbolic So16NSViewControllerCSgXw
CStrings:
+ "@\"NSViewController\"8@?0"
+ "CalendarUI/CalUIMagicComposeFeedbackHandler.swift"
+ "Error message for summarizer error for Magic Compose"
+ "Event descriptions unavailable. Try again later."
+ "Title or Describe Event"
+ "v16@?0@\"NSString\"8"
+ "viewControllerForPresentation called with no presenter available"
+ "\xc1"
- "Title or Describe your event"
```
