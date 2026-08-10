## NotesUI

> `/System/Library/PrivateFrameworks/NotesUI.framework/NotesUI`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_catlist2`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA.__objc_stublist`
- `__DATA_DIRTY.__objc_data`

```diff

-2998.0.0.0.0
-  __TEXT.__text: 0x2bb898
+3001.2.1.0.0
+  __TEXT.__text: 0x2bfd78
   __TEXT.__delay_stubs: 0x40
   __TEXT.__delay_helper: 0x6ec
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x16ff8
-  __TEXT.__const: 0x9ff4
-  __TEXT.__cstring: 0x13ffd
-  __TEXT.__gcc_except_tab: 0x4924
-  __TEXT.__oslogstring: 0xa155
+  __TEXT.__objc_methlist: 0x17168
+  __TEXT.__const: 0xa034
+  __TEXT.__cstring: 0x141cd
+  __TEXT.__gcc_except_tab: 0x4a1c
+  __TEXT.__oslogstring: 0xa215
   __TEXT.__ustring: 0x13896
-  __TEXT.__swift5_typeref: 0xc8c4
+  __TEXT.__swift5_typeref: 0xc942
   __TEXT.__constg_swiftt: 0x3b78
   __TEXT.__swift5_reflstr: 0x2284
   __TEXT.__swift5_fieldmd: 0x2560

   __TEXT.__swift5_assocty: 0x7f0
   __TEXT.__swift5_proto: 0x404
   __TEXT.__swift5_types: 0x30c
-  __TEXT.__swift5_capture: 0x202c
+  __TEXT.__swift5_capture: 0x2040
   __TEXT.__swift5_protos: 0x24
   __TEXT.__swift_as_entry: 0xf8
   __TEXT.__swift_as_ret: 0x108
   __TEXT.__swift_as_cont: 0x1e0
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x9bf8
-  __TEXT.__eh_frame: 0x46e8
+  __TEXT.__unwind_info: 0x9cb8
+  __TEXT.__eh_frame: 0x4718
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6508
+  __DATA_CONST.__const: 0x65f8
   __DATA_CONST.__objc_classlist: 0xac8
   __DATA_CONST.__objc_catlist: 0x2c8
   __DATA_CONST.__objc_catlist2: 0x10
-  __DATA_CONST.__objc_protolist: 0x3c0
+  __DATA_CONST.__objc_protolist: 0x3c8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xff68
+  __DATA_CONST.__objc_selrefs: 0x10088
   __DATA_CONST.__objc_protorefs: 0x178
   __DATA_CONST.__objc_superrefs: 0x6a0
   __DATA_CONST.__objc_arraydata: 0x328
-  __DATA_CONST.__got: 0x2ee8
-  __AUTH_CONST.__const: 0xa2e0
-  __AUTH_CONST.__cfstring: 0xc1a0
-  __AUTH_CONST.__objc_const: 0x242b0
+  __DATA_CONST.__got: 0x2f08
+  __AUTH_CONST.__const: 0xa3a8
+  __AUTH_CONST.__cfstring: 0xc340
+  __AUTH_CONST.__objc_const: 0x24400
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x1e0
   __AUTH_CONST.__objc_intobj: 0x660
   __AUTH_CONST.__objc_doubleobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0x3320
+  __AUTH_CONST.__auth_got: 0x3360
   __AUTH.__objc_data: 0x40c8
-  __AUTH.__data: 0x1c48
-  __DATA.__objc_ivar: 0x11d0
-  __DATA.__data: 0x56e4
+  __AUTH.__data: 0x1c50
+  __DATA.__objc_ivar: 0x11d4
+  __DATA.__data: 0x57d4
   __DATA.__objc_stublist: 0x28
   __DATA.__bss: 0x4160
   __DATA.__common: 0x70
   __DATA_DIRTY.__objc_data: 0x40c8
-  __DATA_DIRTY.__data: 0x25e0
+  __DATA_DIRTY.__data: 0x25c0
   __DATA_DIRTY.__bss: 0x4550
   __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 14892
-  Symbols:   22085
-  CStrings:  3246
+  Functions: 14940
+  Symbols:   22166
+  CStrings:  3268
 
Symbols:
+ +[ICDeviceSupport(UI) isEnhancedSiriAvailable]
+ +[UIAction(IC) ic_actionWithAttributedTitle:image:handler:]
+ -[ICCreateHTMLNoteAction performWithAttributedTitle:contents:pinned:stylesTitle:error:]
+ -[ICCreateModernNoteAction performWithAttributedTitle:contents:pinned:stylesTitle:error:]
+ -[ICCreateNoteAction performWithAttributedTitle:contents:pinned:container:error:]
+ -[ICDividerLineTextAttachmentView contextMenuInteraction:configurationForMenuAtLocation:]
+ -[ICDividerLineTextAttachmentView dividerContextMenuInteraction]
+ -[ICDividerLineTextAttachmentView dividerLineEditMenu]
+ -[ICDividerLineTextAttachmentView dividerLineRangeInTextView:]
+ -[ICDividerLineTextAttachmentView enclosingTextView]
+ -[ICDividerLineTextAttachmentView handleDoubleTap:]
+ -[ICDividerLineTextAttachmentView performDividerLineEdit:]
+ -[ICDividerLineTextAttachmentView selectDividerLine]
+ -[ICDividerLineTextAttachmentView setDividerContextMenuInteraction:]
+ -[ICDividerLineTextAttachmentView setupDividerInteractions]
+ -[ICNote(UI) exportDataForUTI:]
+ -[UITextView(IC) ic_availableWidthForFullWidthAttachmentInTextContainer:]
+ -[UITraitCollection(IC) ic_sceneActivationAllowed]
+ GCC_except_table124
+ GCC_except_table126
+ GCC_except_table128
+ GCC_except_table135
+ GCC_except_table137
+ GCC_except_table141
+ GCC_except_table157
+ GCC_except_table159
+ GCC_except_table69
+ GCC_except_table76
+ GCC_except_table78
+ GCC_except_table81
+ _ICStringFromSplitViewControllerDisplayMode
+ _OBJC_CLASS_$_UIContextMenuInteraction
+ _OBJC_CLASS_$_WTAvailability
+ _OBJC_IVAR_$_ICDividerLineTextAttachmentView._dividerContextMenuInteraction
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIContextMenuInteractionDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_UIContextMenuInteractionDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UIContextMenuInteractionDelegate
+ __OBJC_$_PROTOCOL_REFS_UIContextMenuInteractionDelegate
+ __OBJC_CLASS_PROTOCOLS_$_ICDividerLineTextAttachmentView
+ __OBJC_LABEL_PROTOCOL_$_UIContextMenuInteractionDelegate
+ __OBJC_PROTOCOL_$_UIContextMenuInteractionDelegate
+ ___54-[ICDividerLineTextAttachmentView dividerLineEditMenu]_block_invoke
+ ___54-[ICDividerLineTextAttachmentView dividerLineEditMenu]_block_invoke_2
+ ___54-[ICDividerLineTextAttachmentView dividerLineEditMenu]_block_invoke_3
+ ___54-[ICDividerLineTextAttachmentView dividerLineEditMenu]_block_invoke_4
+ ___54-[ICDividerLineTextAttachmentView dividerLineEditMenu]_block_invoke_5
+ ___54-[ICDividerLineTextAttachmentView dividerLineEditMenu]_block_invoke_6
+ ___54-[ICDividerLineTextAttachmentView dividerLineEditMenu]_block_invoke_7
+ ___54-[ICDividerLineTextAttachmentView dividerLineEditMenu]_block_invoke_8
+ ___60-[ICMarkdownRepresentation createRenderableAttributedString]_block_invoke_11
+ ___62-[ICDividerLineTextAttachmentView dividerLineRangeInTextView:]_block_invoke
+ ___81-[ICCreateNoteAction performWithAttributedTitle:contents:pinned:container:error:]_block_invoke
+ ___81-[ICCreateNoteAction performWithAttributedTitle:contents:pinned:container:error:]_block_invoke_2
+ ___83+[ICNote(AirDropDocumentUI) createNoteForAirDropDocument:legacyContext:completion:]_block_invoke_2
+ ___87-[ICCreateHTMLNoteAction performWithAttributedTitle:contents:pinned:stylesTitle:error:]_block_invoke
+ ___89-[ICCreateModernNoteAction performWithAttributedTitle:contents:pinned:stylesTitle:error:]_block_invoke
+ ___89-[ICDividerLineTextAttachmentView contextMenuInteraction:configurationForMenuAtLocation:]_block_invoke
+ ___93+[ICTextController attributedStringToPasteWithAdaptedParagraphStyles:pasteRange:textStorage:]_block_invoke
+ ___93+[ICTextController attributedStringToPasteWithAdaptedParagraphStyles:pasteRange:textStorage:]_block_invoke_2
+ ___block_descriptor_32_e20_v16?0"UITextView"8l
+ ___block_descriptor_32_e39_"NSArray"16?0"NSPresentationIntent"8l
+ ___block_descriptor_40_e8_32r_e47_v40?0"ICTTParagraphStyle"8{_NSRange=QQ}16^B32lr32l8
+ ___block_descriptor_40_e8_32w_e18_v16?0"UIAction"8lw32l8
+ ___block_descriptor_40_e8_32w_e25_"UIMenu"16?0"NSArray"8lw32l8
+ ___block_descriptor_88_e8_32s40s48s56bs64bs72r80r_e27_v40?08{_NSRange=QQ}16^B32ls56l8s32l8r72l8s40l8s48l8r80l8s64l8
+ _objc_msgSend$_activationInteractionPolicy
+ _objc_msgSend$_presentMenuAtLocation:
+ _objc_msgSend$copy:
+ _objc_msgSend$cut:
+ _objc_msgSend$deleteBackward
+ _objc_msgSend$dividerContextMenuInteraction
+ _objc_msgSend$dividerLineEditMenu
+ _objc_msgSend$dividerLineRangeInTextView:
+ _objc_msgSend$enclosingTextView
+ _objc_msgSend$ic_actionWithAttributedTitle:image:handler:
+ _objc_msgSend$isEnhancedSiriAvailable
+ _objc_msgSend$isEqualToNumber:
+ _objc_msgSend$isFiringFromMaximumDelay
+ _objc_msgSend$isFiringImmediately
+ _objc_msgSend$linkedNoteIsPasswordProtected
+ _objc_msgSend$menuWithTitle:children:
+ _objc_msgSend$paste:
+ _objc_msgSend$performDividerLineEdit:
+ _objc_msgSend$performWithAttributedTitle:contents:pinned:container:error:
+ _objc_msgSend$performWithAttributedTitle:contents:pinned:stylesTitle:error:
+ _objc_msgSend$selectDividerLine
+ _objc_msgSend$setDividerContextMenuInteraction:
+ _objc_msgSend$setNumberOfTapsRequired:
+ _objc_msgSend$setPaperHasGraph:
+ _objc_msgSend$setupDividerInteractions
+ _symbolic SDy__________G 10Foundation4UUIDV So29ICCalculateDocumentControllerC7NotesUIE5IndexC
+ _symbolic _____Sg 8PaperKit19SharedCanvasElementO
+ _symbolic ___________t 10Foundation4UUIDV So29ICCalculateDocumentControllerC7NotesUIE5IndexC
+ _symbolic _____y_____G 9Coherence12CROrderedSetV 8PaperKit19SharedCanvasElementO
+ _symbolic _____y_____GSg_ADt 9Coherence3RefV 8PaperKit12GraphElementV
+ _symbolic _____y______G 9Coherence12CROrderedSetV8IteratorV 8PaperKit19SharedCanvasElementO
+ _symbolic _____y__________G s18_DictionaryStorageC 10Foundation4UUIDV So29ICCalculateDocumentControllerC7NotesUIE5IndexC
+ _symbolic _____y_____yAAySSGGG s18ReversedCollectionV s5SliceV
- GCC_except_table101
- GCC_except_table123
- GCC_except_table127
- GCC_except_table134
- GCC_except_table136
- GCC_except_table140
- GCC_except_table145
- GCC_except_table156
- GCC_except_table80
- ___71-[ICCreateNoteAction performWithTitle:contents:pinned:container:error:]_block_invoke
- ___71-[ICCreateNoteAction performWithTitle:contents:pinned:container:error:]_block_invoke_2
- ___77-[ICCreateHTMLNoteAction performWithTitle:contents:pinned:stylesTitle:error:]_block_invoke
- ___79-[ICCreateModernNoteAction performWithTitle:contents:pinned:stylesTitle:error:]_block_invoke
- ___block_descriptor_80_e8_32s40s48s56bs64r72r_e27_v40?08{_NSRange=QQ}16^B32ls56l8s32l8r64l8s40l8s48l8r72l8
- _objc_msgSend$isStringMarkdown:
- _objc_msgSend$linkedNoteIsPasswordProtectedAndLocked
- _objc_msgSend$performWithTitle:contents:pinned:stylesTitle:error:
CStrings:
+ "-[ICCreateNoteAction performWithAttributedTitle:contents:pinned:container:error:]"
+ "@\"NSArray\"16@?0@\"NSPresentationIntent\"8"
+ "Automatic"
+ "Cut"
+ "Dropping non-NSTextAttachment attachment value before serialization: %@"
+ "In the middle of drawing a stroke, deferring paperDidChange for %@"
+ "Insert Graph (undo)"
+ "NotesUI/CalculateDocumentController.swift"
+ "OneBesideSecondary"
+ "OneOverSecondary"
+ "Paste"
+ "Retaining save block until merges unblock…"
+ "SecondaryOnly"
+ "Suggestion"
+ "TwoBesideSecondary"
+ "TwoDisplaceSecondary"
+ "TwoOverSecondary"
+ "Unknown(%ld)"
+ "cachedIndex(of:) must be called on the main thread"
+ "doc.on.clipboard"
+ "rebuildExpressionIndexCache() must be called on the main thread"
+ "scissors"
+ "v16@?0@\"UITextView\"8"
- "-[ICCreateNoteAction performWithTitle:contents:pinned:container:error:]"
```
