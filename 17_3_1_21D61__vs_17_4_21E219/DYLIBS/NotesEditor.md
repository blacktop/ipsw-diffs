## NotesEditor

> `/System/Library/PrivateFrameworks/NotesEditor.framework/NotesEditor`

```diff

-2485.0.0.0.0
-  __TEXT.__text: 0x200d40
-  __TEXT.__auth_stubs: 0x3e70
-  __TEXT.__objc_methlist: 0x120ec
-  __TEXT.__const: 0x2f14
-  __TEXT.__gcc_except_tab: 0x29ec
-  __TEXT.__cstring: 0xf5eb
-  __TEXT.__oslogstring: 0x3391
-  __TEXT.__ustring: 0x138
+2511.0.0.0.0
+  __TEXT.__text: 0x202e00
+  __TEXT.__auth_stubs: 0x3f20
+  __TEXT.__objc_methlist: 0x11fac
+  __TEXT.__const: 0x3374
+  __TEXT.__gcc_except_tab: 0x29e8
+  __TEXT.__cstring: 0xf8cb
+  __TEXT.__oslogstring: 0x32ac
+  __TEXT.__ustring: 0x276
   __TEXT.__dlopen_cstrs: 0x187
-  __TEXT.__swift5_typeref: 0x5874
-  __TEXT.__swift5_reflstr: 0x23b0
-  __TEXT.__swift5_assocty: 0x2a0
-  __TEXT.__constg_swiftt: 0x2660
-  __TEXT.__swift5_builtin: 0x168
-  __TEXT.__swift5_fieldmd: 0x1a98
-  __TEXT.__swift5_proto: 0x190
-  __TEXT.__swift5_types: 0x17c
-  __TEXT.__swift5_capture: 0x1658
+  __TEXT.__swift5_typeref: 0x594a
+  __TEXT.__swift5_reflstr: 0x2410
+  __TEXT.__swift5_assocty: 0x330
+  __TEXT.__constg_swiftt: 0x270c
+  __TEXT.__swift5_builtin: 0x1a4
+  __TEXT.__swift5_fieldmd: 0x1b04
+  __TEXT.__swift5_proto: 0x1d8
+  __TEXT.__swift5_types: 0x18c
+  __TEXT.__swift5_capture: 0x1678
   __TEXT.__swift5_protos: 0x20
-  __TEXT.__unwind_info: 0x7980
-  __TEXT.__eh_frame: 0x2a58
-  __TEXT.__objc_classname: 0x1eb8
-  __TEXT.__objc_methname: 0x41b5e
-  __TEXT.__objc_methtype: 0x85ee
-  __TEXT.__objc_stubs: 0x2c2e0
-  __DATA_CONST.__got: 0x1108
-  __DATA_CONST.__const: 0x3d50
+  __TEXT.__unwind_info: 0x7b70
+  __TEXT.__eh_frame: 0x2b48
+  __TEXT.__objc_classname: 0x1e83
+  __TEXT.__objc_methname: 0x41780
+  __TEXT.__objc_methtype: 0x8626
+  __TEXT.__objc_stubs: 0x2c0c0
+  __DATA_CONST.__got: 0x1128
+  __DATA_CONST.__const: 0x3cd8
   __DATA_CONST.__objc_classlist: 0x618
   __DATA_CONST.__objc_catlist: 0x188
-  __DATA_CONST.__objc_protolist: 0x490
+  __DATA_CONST.__objc_protolist: 0x480
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1cbc8
-  __DATA_CONST.__objc_selrefs: 0xddf8
+  __DATA_CONST.__objc_const: 0x1ca30
+  __DATA_CONST.__objc_selrefs: 0xdd58
+  __DATA_CONST.__objc_protorefs: 0x118
+  __DATA_CONST.__objc_classrefs: 0x1200
+  __DATA_CONST.__objc_superrefs: 0x428
   __DATA_CONST.__objc_arraydata: 0x38
   __AUTH_CONST.__cfstring: 0x5a40
-  __AUTH_CONST.__objc_const: 0x4048
-  __AUTH_CONST.__const: 0x69c0
+  __AUTH_CONST.__objc_const: 0x4000
+  __AUTH_CONST.__const: 0x6a58
   __AUTH_CONST.__objc_intobj: 0x408
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__auth_ptr: 0x128
-  __AUTH_CONST.__auth_got: 0x1f48
-  __AUTH.__objc_data: 0x3be0
-  __AUTH.__data: 0xa80
-  __DATA.__objc_protorefs: 0x120
-  __DATA.__objc_classrefs: 0x1208
-  __DATA.__objc_superrefs: 0x430
-  __DATA.__objc_ivar: 0x10a4
-  __DATA.__objc_data: 0x2a0
-  __DATA.__data: 0x4f08
-  __DATA.__bss: 0x2d10
-  __DATA.__common: 0x228
-  __DATA_DIRTY.__objc_data: 0x2f18
-  __DATA_DIRTY.__data: 0x840
-  __DATA_DIRTY.__bss: 0x298
-  __DATA_DIRTY.__common: 0x30
+  __AUTH_CONST.__auth_got: 0x1fa0
+  __AUTH.__objc_data: 0x3ca8
+  __AUTH.__data: 0xac0
+  __DATA.__objc_ivar: 0x1098
+  __DATA.__objc_data: 0x280
+  __DATA.__data: 0x5228
+  __DATA.__bss: 0x3590
+  __DATA.__common: 0x148
+  __DATA_DIRTY.__objc_data: 0x2ec8
+  __DATA_DIRTY.__data: 0x8f0
+  __DATA_DIRTY.__bss: 0x310
+  __DATA_DIRTY.__common: 0xd8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AVKit.framework/AVKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10954
-  Symbols:   25640
-  CStrings:  12843
+  Functions: 11021
+  Symbols:   25532
+  CStrings:  12831
 
Symbols:
+ -[ICBaseTextView beginSelectionChange]
+ -[ICBaseTextView endSelectionChange]
+ -[ICNoteEditorViewController eventReporterLostSession:]
+ -[ICNoteEditorViewController eventReporter]
+ -[ICNoteEditorViewController setEventReporter:]
+ -[ICNoteEditorViewController updateUnsupportedNoteView]
+ -[ICTK2TextLayoutManager viewProviderClassForTextAttachment:]
+ -[ICUnsupportedNoteView .cxx_destruct]
+ -[ICUnsupportedNoteView actionButton]
+ -[ICUnsupportedNoteView action]
+ -[ICUnsupportedNoteView createLayout]
+ -[ICUnsupportedNoteView didTapActionButton]
+ -[ICUnsupportedNoteView initWithReason:]
+ -[ICUnsupportedNoteView init]
+ -[ICUnsupportedNoteView isActionDestructive]
+ -[ICUnsupportedNoteView reason]
+ -[ICUnsupportedNoteView setDidTapActionButton:]
+ -[ICUnsupportedNoteView stackView]
+ -[ICUnsupportedNoteView summaryLabel]
+ -[ICUnsupportedNoteView summary]
+ -[ICUnsupportedNoteView titleLabel]
+ -[ICUnsupportedNoteView title]
+ GCC_except_table102
+ GCC_except_table111
+ GCC_except_table300
+ GCC_except_table344
+ GCC_except_table461
+ GCC_except_table489
+ GCC_except_table494
+ GCC_except_table516
+ GCC_except_table554
+ GCC_except_table592
+ GCC_except_table605
+ _.compoundliteral.2802
+ _.compoundliteral.629
+ _ICTextViewSelectedTextRangeDidChangeNotification
+ _OBJC_IVAR_$_ICNoteEditorViewController._eventReporter
+ _OBJC_IVAR_$_ICUnsupportedNoteView._actionButton
+ _OBJC_IVAR_$_ICUnsupportedNoteView._didTapActionButton
+ _OBJC_IVAR_$_ICUnsupportedNoteView._reason
+ _OBJC_IVAR_$_ICUnsupportedNoteView._stackView
+ _OBJC_IVAR_$_ICUnsupportedNoteView._summaryLabel
+ _OBJC_IVAR_$_ICUnsupportedNoteView._titleLabel
+ _OBJC_METACLASS_$__TtCFC11NotesEditorP33_B1771FC5B77E2D60FA249C310C92C62226PaperDocumentContainerViewcFT10inlineViewC8PaperKit23PaperDocumentInlineView21initialShowThumbnailsSb_S0_L_32TraitCollectionDidChangeObserver
+ _PDFViewScaleChangedNotification
+ _UIAccessibilityAcceptedInlineTextCompletion
+ _UIFontDescriptorTraitsAttribute
+ _UIFontWeightTrait
+ __DATA__TtCFC11NotesEditorP33_B1771FC5B77E2D60FA249C310C92C62226PaperDocumentContainerViewcFT10inlineViewC8PaperKit23PaperDocumentInlineView21initialShowThumbnailsSb_S0_L_32TraitCollectionDidChangeObserver
+ __IVARS__TtCFC11NotesEditorP33_B1771FC5B77E2D60FA249C310C92C62226PaperDocumentContainerViewcFT10inlineViewC8PaperKit23PaperDocumentInlineView21initialShowThumbnailsSb_S0_L_32TraitCollectionDidChangeObserver
+ __METACLASS_DATA__TtCFC11NotesEditorP33_B1771FC5B77E2D60FA249C310C92C62226PaperDocumentContainerViewcFT10inlineViewC8PaperKit23PaperDocumentInlineView21initialShowThumbnailsSb_S0_L_32TraitCollectionDidChangeObserver
+ __OBJC_$_INSTANCE_METHODS__TtCFC11NotesEditorP33_B1771FC5B77E2D60FA249C310C92C62226PaperDocumentContainerViewcFT10inlineViewC8PaperKit23PaperDocumentInlineView21initialShowThumbnailsSb_S0_L_32TraitCollectionDidChangeObserver
+ __OBJC_$_INSTANCE_VARIABLES_ICUnsupportedNoteView
+ __OBJC_$_PROP_LIST_ICUnsupportedNoteView
+ __PROTOCOLS__TtC11NotesEditor37SystemPaperViewControllerLinkDelegate.36
+ __PROTOCOLS__TtCC11NotesEditor30NestedScrollViewPanInteraction26ExclusionGestureRecognizer.44
+ ___107-[ICAttachmentImageModel(ItemProviderWriting) loadDataWithTypeIdentifier:forItemProviderCompletionHandler:]_block_invoke.79
+ ___116-[ICBaseTextView(DragAndDrop) handleURLDropForItemProvider:atTextPosition:pasteSession:outProgress:completionBlock:]_block_invoke.146
+ ___137-[ICNoteEditorViewController documentCameraPresentingViewController:didFinishWithInfoCollection:imageCache:warnUser:closeViewController:]_block_invoke.707
+ ___37-[ICUnsupportedNoteView actionButton]_block_invoke
+ ___43-[ICAttachmentPresenter presentSynapseLink]_block_invoke.156
+ ___43-[ICAttachmentPresenter presentSynapseLink]_block_invoke.156.cold.1
+ ___55-[ICNoteEditorViewController updateUnsupportedNoteView]_block_invoke
+ ___57-[ICNoteEditorViewController insertSidecarItems:service:]_block_invoke.844
+ ___block_descriptor_72_e8_32s40s48s56s64r_e27_v40?08{_NSRange=QQ}16^B32ls32l8s40l8s48l8s56l8r64l8
+ ___block_descriptor_72_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.127
+ ___block_literal_global.191
+ ___block_literal_global.223
+ ___block_literal_global.463
+ ___block_literal_global.840
+ ___block_literal_global.847
+ _associated conformance So12UIFontWeightaSHSCSQ
+ _associated conformance So12UIFontWeightas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So12UIFontWeightas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _associated conformance So24UIFontDescriptorTraitKeyaSHSCSQ
+ _associated conformance So24UIFontDescriptorTraitKeyas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So24UIFontDescriptorTraitKeyas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _associated conformance So29UIFontDescriptorAttributeNameaSHSCSQ
+ _associated conformance So29UIFontDescriptorAttributeNameas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So29UIFontDescriptorAttributeNameas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _block_copy_helper.154
+ _block_copy_helper.174
+ _block_copy_helper.177
+ _block_copy_helper.183
+ _block_copy_helper.194
+ _block_copy_helper.204
+ _block_copy_helper.215
+ _block_copy_helper.225
+ _block_copy_helper.240
+ _block_copy_helper.246
+ _block_copy_helper.25
+ _block_copy_helper.255
+ _block_copy_helper.272
+ _block_copy_helper.289
+ _block_copy_helper.300
+ _block_copy_helper.317
+ _block_copy_helper.323
+ _block_copy_helper.329
+ _block_copy_helper.376
+ _block_copy_helper.382
+ _block_copy_helper.386
+ _block_copy_helper.423
+ _block_copy_helper.429
+ _block_copy_helper.434
+ _block_copy_helper.469
+ _block_copy_helper.487
+ _block_copy_helper.495
+ _block_copy_helper.50
+ _block_copy_helper.504
+ _block_copy_helper.53
+ _block_copy_helper.56
+ _block_copy_helper.62
+ _block_copy_helper.74
+ _block_descriptor.156
+ _block_descriptor.176
+ _block_descriptor.179
+ _block_descriptor.185
+ _block_descriptor.196
+ _block_descriptor.206
+ _block_descriptor.217
+ _block_descriptor.227
+ _block_descriptor.242
+ _block_descriptor.248
+ _block_descriptor.257
+ _block_descriptor.27
+ _block_descriptor.274
+ _block_descriptor.291
+ _block_descriptor.302
+ _block_descriptor.319
+ _block_descriptor.325
+ _block_descriptor.331
+ _block_descriptor.378
+ _block_descriptor.384
+ _block_descriptor.388
+ _block_descriptor.425
+ _block_descriptor.431
+ _block_descriptor.436
+ _block_descriptor.471
+ _block_descriptor.489
+ _block_descriptor.497
+ _block_descriptor.506
+ _block_descriptor.52
+ _block_descriptor.55
+ _block_descriptor.58
+ _block_descriptor.64
+ _block_descriptor.76
+ _block_destroy_helper.155
+ _block_destroy_helper.175
+ _block_destroy_helper.178
+ _block_destroy_helper.184
+ _block_destroy_helper.195
+ _block_destroy_helper.205
+ _block_destroy_helper.216
+ _block_destroy_helper.226
+ _block_destroy_helper.241
+ _block_destroy_helper.247
+ _block_destroy_helper.256
+ _block_destroy_helper.26
+ _block_destroy_helper.273
+ _block_destroy_helper.290
+ _block_destroy_helper.301
+ _block_destroy_helper.318
+ _block_destroy_helper.324
+ _block_destroy_helper.330
+ _block_destroy_helper.377
+ _block_destroy_helper.383
+ _block_destroy_helper.387
+ _block_destroy_helper.424
+ _block_destroy_helper.430
+ _block_destroy_helper.435
+ _block_destroy_helper.470
+ _block_destroy_helper.488
+ _block_destroy_helper.496
+ _block_destroy_helper.505
+ _block_destroy_helper.51
+ _block_destroy_helper.54
+ _block_destroy_helper.57
+ _block_destroy_helper.63
+ _block_destroy_helper.75
+ _get_witness_table 10Foundation19AttributedStringKeyRzlAA15AttributeScopesO5UIKitE0G10AttributesV015ForegroundColorE0OAaBHPyHC.456
+ _get_witness_table 10Foundation19AttributedStringKeyRzlAA15AttributeScopesO5UIKitE0G10AttributesV04FontE0OAaBHPyHC.450
+ _keypath_get.451Tm
+ _objc_msgSend$actionButton
+ _objc_msgSend$addArrangedSubview:
+ _objc_msgSend$addTextView:
+ _objc_msgSend$allDocumentMergeControllers
+ _objc_msgSend$beginBlockingMergeWithReason:textView:
+ _objc_msgSend$canAuthenticate
+ _objc_msgSend$createLayout
+ _objc_msgSend$didTapActionButton
+ _objc_msgSend$documentMergeController
+ _objc_msgSend$endBlockingMergeWithReason:textView:
+ _objc_msgSend$hasMissingKeychainItem
+ _objc_msgSend$initWithReason:
+ _objc_msgSend$initWithSubTrackerName:
+ _objc_msgSend$isActionDestructive
+ _objc_msgSend$reason
+ _objc_msgSend$removeTextView:
+ _objc_msgSend$setCustomSpacing:afterView:
+ _objc_msgSend$setDidTapActionButton:
+ _objc_msgSend$stackView
+ _objc_msgSend$summary
+ _objc_msgSend$summaryLabel
+ _objc_msgSend$systemRedColor
+ _objc_msgSend$undoablyTrashOrDeleteNotes:
+ _objc_msgSend$updateUnsupportedNoteView
+ _objc_msgSend$viewProviderClassForTextAttachment:
+ _objectdestroy.150Tm
+ _objectdestroy.169Tm
+ _objectdestroy.399Tm
+ _objectdestroy.48Tm
+ _symbolic SDy__________G So24UIFontDescriptorTraitKeya So0A6Weighta
+ _symbolic SaySo13UIMenuElementCG
+ _symbolic SaySo14NSUserActivityCG
+ _symbolic SaySo36ICTTMergeableStringVersionedDocumentCG
+ _symbolic So8NSNumberC
+ _symbolic _____ 11NotesEditor26PaperDocumentContainerView33_B1771FC5B77E2D60FA249C310C92C622LLC06inlineF021initialShowThumbnailsAD0C3Kit0cd6InlineF0C_Sbtcfc32TraitCollectionDidChangeObserverL_C
+ _symbolic _____ So12UIFontWeighta
+ _symbolic _____ So24UIFontDescriptorTraitKeya
+ _symbolic _____ So29UIFontDescriptorAttributeNamea
+ _symbolic _____SgXw 8PaperKit0A21DocumentThumbnailViewC
+ _symbolic _____So6UIFontCIegyo_ So12UIFontWeighta
+ _symbolic ______ypt So29UIFontDescriptorAttributeNamea
+ _symbolic _____y__________G s18_DictionaryStorageC So24UIFontDescriptorTraitKeya So0C6Weighta
+ _symbolic _____y___________tG s23_ContiguousArrayStorageC So24UIFontDescriptorTraitKeya So0D6Weighta
+ _symbolic _____y______yptG s23_ContiguousArrayStorageC So29UIFontDescriptorAttributeNamea
+ _symbolic _____y_____ypG s18_DictionaryStorageC So29UIFontDescriptorAttributeNamea
- -[ICBaseTextView dragMergeabilityController]
- -[ICBaseTextView dropMergeabilityController]
- -[ICBaseTextView setDragMergeabilityController:]
- -[ICBaseTextView setDropMergeabilityController:]
- -[ICNoteEditorViewController mergeabilityController]
- -[ICNoteEditorViewController setMergeabilityController:]
- -[ICNoteEditorViewController startBlockingMerge]
- -[ICNoteEditorViewController stopBlockingMerge]
- -[ICNoteEditorViewController updateMergeabilityController]
- -[ICNoteMergeabilityController .cxx_destruct]
- -[ICNoteMergeabilityController addNotificationCenterObservers]
- -[ICNoteMergeabilityController attemptedToMergeWhenEditingMarkedText]
- -[ICNoteMergeabilityController blockingMergeStack]
- -[ICNoteMergeabilityController dealloc]
- -[ICNoteMergeabilityController hasBlockedMergeRequest]
- -[ICNoteMergeabilityController hasMarkedText]
- -[ICNoteMergeabilityController initWithNote:]
- -[ICNoteMergeabilityController markedTextRange]
- -[ICNoteMergeabilityController mergeIsBlocked]
- -[ICNoteMergeabilityController note]
- -[ICNoteMergeabilityController performBlockToMergeNoteData:]
- -[ICNoteMergeabilityController performMerge]
- -[ICNoteMergeabilityController performPreviouslyBlockedMergeIfNecessary]
- -[ICNoteMergeabilityController removeNotificationCenterObservers]
- -[ICNoteMergeabilityController requestMergeNotePrimitiveData]
- -[ICNoteMergeabilityController requestMerge]
- -[ICNoteMergeabilityController resetBlockingMergeStack]
- -[ICNoteMergeabilityController resetUnmarkTextTimerIfNeeded]
- -[ICNoteMergeabilityController resetUnmarkTextTimerIfNeeded].cold.1
- -[ICNoteMergeabilityController setAttemptedToMergeWhenEditingMarkedText:]
- -[ICNoteMergeabilityController setBlockingMergeStack:]
- -[ICNoteMergeabilityController setBlockingMergeStack:].cold.1
- -[ICNoteMergeabilityController setHasBlockedMergeRequest:]
- -[ICNoteMergeabilityController setShouldBypassDidUnmarkTextCallback:]
- -[ICNoteMergeabilityController setShouldUseLongDelayWhenSchedulingUnmarkTextTimer:]
- -[ICNoteMergeabilityController setUnmarkTextTimer:]
- -[ICNoteMergeabilityController shouldBypassDidUnmarkTextCallback]
- -[ICNoteMergeabilityController shouldUseLongDelayWhenSchedulingUnmarkTextTimer]
- -[ICNoteMergeabilityController startBlockingMerge]
- -[ICNoteMergeabilityController startUnmarkTextTimerIfNeeded]
- -[ICNoteMergeabilityController startUnmarkTextTimerIfNeeded].cold.1
- -[ICNoteMergeabilityController stopBlockingMerge]
- -[ICNoteMergeabilityController stopUnmarkTextTimerIfNeeded]
- -[ICNoteMergeabilityController stopUnmarkTextTimerIfNeeded].cold.1
- -[ICNoteMergeabilityController textStorageDidEndEditingNotification:]
- -[ICNoteMergeabilityController textStorage]
- -[ICNoteMergeabilityController textViewDidEndSelectionChange:]
- -[ICNoteMergeabilityController textViewWillStartSelectionChange:]
- -[ICNoteMergeabilityController unmarkTextIfNecessary]
- -[ICNoteMergeabilityController unmarkTextIfNecessary].cold.1
- -[ICNoteMergeabilityController unmarkTextTimerTimeout]
- -[ICNoteMergeabilityController unmarkTextTimer]
- -[ICNoteMergeabilityController userExpandedOrClosedKeyboardCandidateCollectionView:]
- -[ICTextView beginSelectionChange]
- -[ICTextView endSelectionChange]
- -[ICUnsupportedNoteView commonInit]
- -[ICUnsupportedNoteView initWithCoder:]
- -[ICUnsupportedNoteView initWithFrame:]
- GCC_except_table100
- GCC_except_table109
- GCC_except_table342
- GCC_except_table462
- GCC_except_table490
- GCC_except_table495
- GCC_except_table517
- GCC_except_table555
- GCC_except_table593
- GCC_except_table606
- _.compoundliteral.2810
- _.compoundliteral.628
- _ICTextViewDidEndSelectionChangeNotification
- _ICTextViewWillStartSelectionChangeNotification
- _ICUIKeyboardCandidateGridCollectionViewDidShowOrHideNotification
- _OBJC_CLASS_$_ICNoteMergeabilityController
- _OBJC_IVAR_$_ICBaseTextView._dragMergeabilityController
- _OBJC_IVAR_$_ICBaseTextView._dropMergeabilityController
- _OBJC_IVAR_$_ICNoteEditorViewController._mergeabilityController
- _OBJC_IVAR_$_ICNoteMergeabilityController._attemptedToMergeWhenEditingMarkedText
- _OBJC_IVAR_$_ICNoteMergeabilityController._blockingMergeStack
- _OBJC_IVAR_$_ICNoteMergeabilityController._hasBlockedMergeRequest
- _OBJC_IVAR_$_ICNoteMergeabilityController._note
- _OBJC_IVAR_$_ICNoteMergeabilityController._shouldBypassDidUnmarkTextCallback
- _OBJC_IVAR_$_ICNoteMergeabilityController._shouldUseLongDelayWhenSchedulingUnmarkTextTimer
- _OBJC_IVAR_$_ICNoteMergeabilityController._unmarkTextTimer
- _OBJC_METACLASS_$_ICNoteMergeabilityController
- __OBJC_$_INSTANCE_METHODS_ICNoteMergeabilityController
- __OBJC_$_INSTANCE_VARIABLES_ICNoteMergeabilityController
- __OBJC_$_PROP_LIST_ICNoteMergeabilityController
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_ICNoteMergeabilityDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_ICNoteMergeabilityDelegate
- __OBJC_$_PROTOCOL_REFS_ICNoteMergeabilityDelegate
- __OBJC_CLASS_PROTOCOLS_$_ICNoteMergeabilityController
- __OBJC_CLASS_RO_$_ICNoteMergeabilityController
- __OBJC_LABEL_PROTOCOL_$_ICNoteMergeabilityDelegate
- __OBJC_METACLASS_RO_$_ICNoteMergeabilityController
- __OBJC_PROTOCOL_$_ICNoteMergeabilityDelegate
- __PROTOCOLS__TtC11NotesEditor37SystemPaperViewControllerLinkDelegate.37
- __PROTOCOLS__TtCC11NotesEditor30NestedScrollViewPanInteraction26ExclusionGestureRecognizer.45
- __PROTOCOL_INSTANCE_METHODS_OPT__TtP11NotesEditor25ICPPKThumbnailViewStaging_
- __PROTOCOL_METHOD_TYPES__TtP11NotesEditor25ICPPKThumbnailViewStaging_
- __PROTOCOL__TtP11NotesEditor25ICPPKThumbnailViewStaging_
- ___107-[ICAttachmentImageModel(ItemProviderWriting) loadDataWithTypeIdentifier:forItemProviderCompletionHandler:]_block_invoke.77
- ___116-[ICBaseTextView(DragAndDrop) handleURLDropForItemProvider:atTextPosition:pasteSession:outProgress:completionBlock:]_block_invoke.145
- ___137-[ICNoteEditorViewController documentCameraPresentingViewController:didFinishWithInfoCollection:imageCache:warnUser:closeViewController:]_block_invoke.706
- ___43-[ICAttachmentPresenter presentSynapseLink]_block_invoke.155
- ___43-[ICAttachmentPresenter presentSynapseLink]_block_invoke.155.cold.1
- ___45-[ICNoteMergeabilityController hasMarkedText]_block_invoke
- ___47-[ICNoteMergeabilityController markedTextRange]_block_invoke
- ___53-[ICNoteMergeabilityController unmarkTextIfNecessary]_block_invoke
- ___53-[ICNoteMergeabilityController unmarkTextIfNecessary]_block_invoke.36
- ___53-[ICNoteMergeabilityController unmarkTextIfNecessary]_block_invoke_2
- ___53-[ICNoteMergeabilityController unmarkTextIfNecessary]_block_invoke_2.cold.1
- ___57-[ICNoteEditorViewController insertSidecarItems:service:]_block_invoke.843
- ___60-[ICNoteMergeabilityController performBlockToMergeNoteData:]_block_invoke
- ___60-[ICNoteMergeabilityController performBlockToMergeNoteData:]_block_invoke_2
- ___block_descriptor_32_e27_v32?0"UITextView"8Q16^B24l
- ___block_descriptor_40_e8_32s_e24_B24?0"UITextView"8^B16ls32l8
- ___block_descriptor_48_e27_v32?0"UITextView"8Q16^B24l
- ___block_descriptor_48_e8_32s40r_e24_v24?0"UITextView"8^B16ls32l8r40l8
- ___block_descriptor_72_e8_32s40s48s56s64r_e45_v40?0"NSTextAttachment"8{_NSRange=QQ}16^B32ls32l8s40l8s48l8s56l8r64l8
- ___block_literal_global.126
- ___block_literal_global.190
- ___block_literal_global.222
- ___block_literal_global.455
- ___block_literal_global.839
- ___block_literal_global.846
- ___swift_assign_boxed_opaque_existential_1
- _block_copy_helper.147
- _block_copy_helper.167
- _block_copy_helper.170
- _block_copy_helper.176
- _block_copy_helper.187
- _block_copy_helper.190
- _block_copy_helper.208
- _block_copy_helper.211
- _block_copy_helper.233
- _block_copy_helper.239
- _block_copy_helper.248
- _block_copy_helper.265
- _block_copy_helper.268
- _block_copy_helper.293
- _block_copy_helper.296
- _block_copy_helper.325
- _block_copy_helper.331
- _block_copy_helper.335
- _block_copy_helper.36
- _block_copy_helper.366
- _block_copy_helper.372
- _block_copy_helper.378
- _block_copy_helper.383
- _block_copy_helper.426
- _block_copy_helper.435
- _block_copy_helper.438
- _block_copy_helper.443
- _block_copy_helper.449
- _block_copy_helper.484
- _block_copy_helper.52
- _block_copy_helper.64
- _block_copy_helper.70
- _block_copy_helper.76
- _block_copy_helper.8
- _block_descriptor.10
- _block_descriptor.149
- _block_descriptor.169
- _block_descriptor.172
- _block_descriptor.178
- _block_descriptor.189
- _block_descriptor.192
- _block_descriptor.210
- _block_descriptor.213
- _block_descriptor.235
- _block_descriptor.241
- _block_descriptor.250
- _block_descriptor.267
- _block_descriptor.270
- _block_descriptor.295
- _block_descriptor.298
- _block_descriptor.327
- _block_descriptor.333
- _block_descriptor.337
- _block_descriptor.368
- _block_descriptor.374
- _block_descriptor.38
- _block_descriptor.380
- _block_descriptor.385
- _block_descriptor.428
- _block_descriptor.437
- _block_descriptor.440
- _block_descriptor.445
- _block_descriptor.451
- _block_descriptor.486
- _block_descriptor.54
- _block_descriptor.66
- _block_descriptor.72
- _block_descriptor.78
- _block_destroy_helper.148
- _block_destroy_helper.168
- _block_destroy_helper.171
- _block_destroy_helper.177
- _block_destroy_helper.188
- _block_destroy_helper.191
- _block_destroy_helper.209
- _block_destroy_helper.212
- _block_destroy_helper.234
- _block_destroy_helper.240
- _block_destroy_helper.249
- _block_destroy_helper.266
- _block_destroy_helper.269
- _block_destroy_helper.294
- _block_destroy_helper.297
- _block_destroy_helper.326
- _block_destroy_helper.332
- _block_destroy_helper.336
- _block_destroy_helper.367
- _block_destroy_helper.37
- _block_destroy_helper.373
- _block_destroy_helper.379
- _block_destroy_helper.384
- _block_destroy_helper.427
- _block_destroy_helper.436
- _block_destroy_helper.439
- _block_destroy_helper.444
- _block_destroy_helper.450
- _block_destroy_helper.485
- _block_destroy_helper.53
- _block_destroy_helper.65
- _block_destroy_helper.71
- _block_destroy_helper.77
- _block_destroy_helper.9
- _get_witness_table 10Foundation19AttributedStringKeyRzlAA15AttributeScopesO5UIKitE0G10AttributesV015ForegroundColorE0OAaBHPyHC.404
- _get_witness_table 10Foundation19AttributedStringKeyRzlAA15AttributeScopesO5UIKitE0G10AttributesV04FontE0OAaBHPyHC.398
- _kICMergeDelayLongTimeOut
- _kICMergeDelayTimeOut
- _keypath_get.399Tm
- _objc_msgSend$addNotificationCenterObservers
- _objc_msgSend$attemptedToMergeWhenEditingMarkedText
- _objc_msgSend$blockingMergeStack
- _objc_msgSend$dragMergeabilityController
- _objc_msgSend$dropMergeabilityController
- _objc_msgSend$hasBlockedMergeRequest
- _objc_msgSend$hasMarkedText
- _objc_msgSend$isValid
- _objc_msgSend$mergeIsBlocked
- _objc_msgSend$mergeNotePrimitiveData
- _objc_msgSend$mergeabilityController
- _objc_msgSend$mergeabilityDelegate
- _objc_msgSend$performMerge
- _objc_msgSend$performPreviouslyBlockedMergeIfNecessary
- _objc_msgSend$performWithoutAffectingCalloutBar:
- _objc_msgSend$performWithoutAffectingSharedCalloutBar:
- _objc_msgSend$removeNotificationCenterObservers
- _objc_msgSend$requestMerge
- _objc_msgSend$resetBlockingMergeStack
- _objc_msgSend$resetUnmarkTextTimerIfNeeded
- _objc_msgSend$setAttemptedToMergeWhenEditingMarkedText:
- _objc_msgSend$setBlockingMergeStack:
- _objc_msgSend$setDragMergeabilityController:
- _objc_msgSend$setDragTextViewStrongReference:
- _objc_msgSend$setDropMergeabilityController:
- _objc_msgSend$setFireDate:
- _objc_msgSend$setHasBlockedMergeRequest:
- _objc_msgSend$setIsChangingSelectionByGestures:
- _objc_msgSend$setMergeabilityController:
- _objc_msgSend$setMergeabilityDelegate:
- _objc_msgSend$setShouldBypassDidUnmarkTextCallback:
- _objc_msgSend$setShouldUseLongDelayWhenSchedulingUnmarkTextTimer:
- _objc_msgSend$setUnmarkTextTimer:
- _objc_msgSend$shouldUseLongDelayWhenSchedulingUnmarkTextTimer
- _objc_msgSend$startBlockingMerge
- _objc_msgSend$startUnmarkTextTimerIfNeeded
- _objc_msgSend$stopBlockingMerge
- _objc_msgSend$stopUnmarkTextTimerIfNeeded
- _objc_msgSend$textViewHasMarkedText:
- _objc_msgSend$unmarkTextTimer
- _objc_msgSend$unmarkTextTimerTimeout
- _objc_msgSend$updateMergeabilityController
- _objectdestroy.143Tm
- _objectdestroy.162Tm
- _objectdestroy.19Tm
- _objectdestroy.348Tm
- _objectdestroy.50Tm
- _symbolic $s11NotesEditor25ICPPKThumbnailViewStagingP
- _symbolic Say_____G 11NotesShared14LinkSuggestionV
- _symbolic So6UIFontC
- _symbolic _____ySSSgG s23_ContiguousArrayStorageC
- _symbolic _____ySo13UIMenuElementCSgG s23_ContiguousArrayStorageC
- _symbolic _____y_____G s10ArraySliceV 11NotesShared14LinkSuggestionV
CStrings:
+ "\x04\x11"
+ "((participants) != nil)"
+ "-[ICBaseTextView updateKeyboardSuggestions:mentionsController:mentionString:]"
+ "C$1\x12\x17"
+ "Can't construct Array with count < 0"
+ "Division by zero"
+ "Division results in an overflow"
+ "ICTextViewSelectedTextRangeDidChangeNotification"
+ "Index out of range"
+ "Insert from photo library, iPhone, or iPad"
+ "Negative value is not representable"
+ "NotesEditor.TraitCollectionDidChangeObserver"
+ "Range requires lowerBound <= upperBound"
+ "Swift/Array.swift"
+ "Swift/IntegerTypes.swift"
+ "Swift/Integers.swift"
+ "Swift/Range.swift"
+ "Swift/UnsafePointer.swift"
+ "T@\"ICTTTextStorage\",?,R,N"
+ "T@\"NSArray\",?,R,C,N"
+ "T@\"NSString\",?,C,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",?,R,N"
+ "T@\"NSURL\",?,R,N"
+ "T@\"UIButton\",R,N,V_actionButton"
+ "T@\"UILabel\",R,N,V_summaryLabel"
+ "T@\"UILabel\",R,N,V_titleLabel"
+ "T@\"UIStackView\",R,N,V_stackView"
+ "T@\"UITextInputPasswordRules\",?,C,N"
+ "T@\"UIView\",?,R,N"
+ "T@,?,R,N"
+ "T@?,C,N,V_didTapActionButton"
+ "TB,?,N"
+ "TB,?,N,GisSecureTextEntry"
+ "TQ,R,N,V_reason"
+ "Tq,?,N"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "_TtCFC11NotesEditorP33_B1771FC5B77E2D60FA249C310C92C62226PaperDocumentContainerViewcFT10inlineViewC8PaperKit23PaperDocumentInlineView21initialShowThumbnailsSb_S0_L_32TraitCollectionDidChangeObserver"
+ "_actionButton"
+ "_didTapActionButton"
+ "_reason"
+ "_stackView"
+ "_summaryLabel"
+ "actionButton"
+ "addTextView:"
+ "allDocumentMergeControllers"
+ "beginBlockingMergeWithReason:textView:"
+ "canAuthenticate"
+ "caretTransformForPosition:"
+ "convertPoint:fromPage:"
+ "createLayout"
+ "didScheduleUpdate"
+ "didTapActionButton"
+ "documentMergeController"
+ "endBlockingMergeWithReason:textView:"
+ "fontDescriptorByAddingAttributes:"
+ "hasMissingKeychainItem"
+ "initWithReason:"
+ "initWithSubTrackerName:"
+ "isActionDestructive"
+ "isZoomBouncing"
+ "lastPDFScaleFactorForInterpageSpacingUpdate"
+ "preferredFontForTextStyle:compatibleWithTraitCollection:"
+ "r!q\xf0\x81\xf1\xf0A"
+ "reason"
+ "removeTextView:"
+ "setDidTapActionButton:"
+ "setMinimumContentSizeCategory:"
+ "summary"
+ "summaryLabel"
+ "systemRedColor"
+ "traitCollectionDidChangeHandler"
+ "undoablyTrashOrDeleteNotes:"
+ "updateUnsupportedNoteView"
+ "viewProviderClassForTextAttachment:"
+ "{CGAffineTransform=dddddd}24@0:8@\"UITextPosition\"16"
+ "{CGAffineTransform=dddddd}24@0:8@16"
+ "\x92\x17\x1f\x06\x11\x133\x15\x16\x1c\x1f\x05"
- "@\"ICNoteMergeabilityController\""
- "B24@?0@\"UITextView\"8^B16"
- "C$1\x12\x19"
- "ICNoteMergeabilityController"
- "ICNoteMergeabilityDelegate"
- "ICPaperDocumentTextAttachmentViewDebugFrames"
- "ICTextViewDidEndSelectionChangeNotification"
- "ICTextViewWillStartSelectionChangeNotification"
- "ICUIKeyboardCandidateGridCollectionViewDidShowOrHideNotification"
- "Open the photo library, or insert from iPhone or iPad"
- "Over-popping blocking merge stack in ICNoteMergeabilityController %@ for note: %@"
- "PDFScrollViewPageMayHaveChangedNotification"
- "Resetting unmark text timer..."
- "Starting unmark text timer..."
- "Stopping unmark text timer..."
- "T@\"ICNoteMergeabilityController\",&,N,V_dragMergeabilityController"
- "T@\"ICNoteMergeabilityController\",&,N,V_dropMergeabilityController"
- "T@\"ICNoteMergeabilityController\",&,N,V_mergeabilityController"
- "T@\"NSString\",C,N"
- "T@\"NSTimer\",&,N,V_unmarkTextTimer"
- "T@\"UITextInputPasswordRules\",C,N"
- "T@,R,N"
- "TB,N,GisSecureTextEntry"
- "TB,N,V_attemptedToMergeWhenEditingMarkedText"
- "TB,N,V_hasBlockedMergeRequest"
- "TB,N,V_shouldBypassDidUnmarkTextCallback"
- "TB,N,V_shouldUseLongDelayWhenSchedulingUnmarkTextTimer"
- "Tq,N"
- "Tq,V_blockingMergeStack"
- "Unmark text timer fired"
- "Unmarking text for textView: %@"
- "_TtP11NotesEditor25ICPPKThumbnailViewStaging_"
- "_attemptedToMergeWhenEditingMarkedText"
- "_blockingMergeStack"
- "_dragMergeabilityController"
- "_dropMergeabilityController"
- "_hasBlockedMergeRequest"
- "_mergeabilityController"
- "_shouldBypassDidUnmarkTextCallback"
- "_shouldUseLongDelayWhenSchedulingUnmarkTextTimer"
- "_unmarkTextTimer"
- "addNotificationCenterObservers"
- "attemptedToMergeWhenEditingMarkedText"
- "blockingMergeStack"
- "dragMergeabilityController"
- "dropMergeabilityController"
- "greenColor"
- "hasBlockedMergeRequest"
- "hasMarkedText"
- "mergeIsBlocked"
- "mergeNotePrimitiveData"
- "mergeabilityController"
- "mergeabilityDelegate"
- "performBlockToMergeNoteData:"
- "performMerge"
- "performPreviouslyBlockedMergeIfNecessary"
- "performWithoutAffectingCalloutBar:"
- "performWithoutAffectingSharedCalloutBar:"
- "r!a\xf0\x91\xf1\xf0A"
- "removeNotificationCenterObservers"
- "requestMerge"
- "requestMergeNotePrimitiveData"
- "resetBlockingMergeStack"
- "resetUnmarkTextTimerIfNeeded"
- "setAttemptedToMergeWhenEditingMarkedText:"
- "setBlockingMergeStack:"
- "setDragMergeabilityController:"
- "setDropMergeabilityController:"
- "setFireDate:"
- "setHasBlockedMergeRequest:"
- "setIsChangingSelectionByGestures:"
- "setMergeabilityController:"
- "setMergeabilityDelegate:"
- "setShouldBypassDidUnmarkTextCallback:"
- "setShouldUseLongDelayWhenSchedulingUnmarkTextTimer:"
- "setThumbnailSize:"
- "setUnmarkTextTimer:"
- "shouldBypassDidUnmarkTextCallback"
- "shouldUseLongDelayWhenSchedulingUnmarkTextTimer"
- "startBlockingMerge"
- "startUnmarkTextTimerIfNeeded"
- "stopBlockingMerge"
- "stopUnmarkTextTimerIfNeeded"
- "textViewDidEndSelectionChange:"
- "textViewHasMarkedText:"
- "textViewWillStartSelectionChange:"
- "unmarkTextIfNecessary"
- "unmarkTextTimer"
- "unmarkTextTimerTimeout"
- "updateMergeabilityController"
- "userExpandedOrClosedKeyboardCandidateCollectionView:"
- "v24@?0@\"UITextView\"8^B16"
- "v32@?0@\"UITextView\"8Q16^B24"
- "\x92\x16\x1f\a\x11\x133\x15\x16\x1c\x1f\x05"

```
