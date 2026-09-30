## NotesUI

> `/System/Library/PrivateFrameworks/NotesUI.framework/Versions/A/NotesUI`

```diff

-3192.0.0.0.0
-  __TEXT.__text: 0x271dec
+3195.0.0.0.0
+  __TEXT.__text: 0x2757f0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x12060
-  __TEXT.__const: 0x8f44
-  __TEXT.__cstring: 0x1192c
-  __TEXT.__gcc_except_tab: 0x419c
-  __TEXT.__oslogstring: 0x8bd7
+  __TEXT.__objc_methlist: 0x120e0
+  __TEXT.__const: 0x8f84
+  __TEXT.__cstring: 0x11a1c
+  __TEXT.__gcc_except_tab: 0x4274
+  __TEXT.__oslogstring: 0x8c47
   __TEXT.__ustring: 0x14c06
   __TEXT.__constg_swiftt: 0x3204
-  __TEXT.__swift5_typeref: 0xbe16
+  __TEXT.__swift5_typeref: 0xbeb2
   __TEXT.__swift5_reflstr: 0x1bf3
   __TEXT.__swift5_fieldmd: 0x1e9c
   __TEXT.__swift5_builtin: 0x21c
   __TEXT.__swift5_assocty: 0x7c0
   __TEXT.__swift5_proto: 0x3a8
   __TEXT.__swift5_types: 0x280
-  __TEXT.__swift5_capture: 0x1980
+  __TEXT.__swift5_capture: 0x1994
   __TEXT.__swift_as_entry: 0xc4
   __TEXT.__swift_as_ret: 0xe0
   __TEXT.__swift_as_cont: 0x17c
   __TEXT.__swift5_protos: 0x1c
-  __TEXT.__unwind_info: 0x8398
-  __TEXT.__eh_frame: 0x3bd8
+  __TEXT.__unwind_info: 0x8418
+  __TEXT.__eh_frame: 0x3c00
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1610
+  __DATA_CONST.__const: 0x1630
   __DATA_CONST.__objc_classlist: 0x828
   __DATA_CONST.__objc_catlist: 0x268
   __DATA_CONST.__objc_protolist: 0x298
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd438
+  __DATA_CONST.__objc_selrefs: 0xd490
   __DATA_CONST.__objc_protorefs: 0xf8
   __DATA_CONST.__objc_superrefs: 0x538
   __DATA_CONST.__objc_arraydata: 0x2e0
-  __DATA_CONST.__got: 0x27a8
-  __AUTH_CONST.__const: 0xcfa8
-  __AUTH_CONST.__cfstring: 0xa940
-  __AUTH_CONST.__objc_const: 0x1c738
+  __DATA_CONST.__got: 0x27c0
+  __AUTH_CONST.__const: 0xd048
+  __AUTH_CONST.__cfstring: 0xa960
+  __AUTH_CONST.__objc_const: 0x1c7a8
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_intobj: 0x4f8
   __AUTH_CONST.__objc_doubleobj: 0x190
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x2ba0
+  __AUTH_CONST.__auth_got: 0x2be8
   __AUTH.__objc_data: 0x23b8
-  __AUTH.__data: 0x17d8
+  __AUTH.__data: 0x17d0
   __DATA.__objc_ivar: 0xec0
-  __DATA.__data: 0x4598
+  __DATA.__data: 0x4628
   __DATA.__objc_stublist: 0x20
   __DATA.__bss: 0x3870
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x3a88
-  __DATA_DIRTY.__data: 0x2500
+  __DATA_DIRTY.__data: 0x2530
   __DATA_DIRTY.__bss: 0x42b0
   __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12644
-  Symbols:   18504
-  CStrings:  2857
+  Functions: 12674
+  Symbols:   18530
+  CStrings:  2864
 
Symbols:
+ -[ICCreateHTMLNoteAction performWithAttributedTitle:contents:pinned:stylesTitle:error:]
+ -[ICCreateModernNoteAction performWithAttributedTitle:contents:pinned:stylesTitle:error:]
+ -[ICCreateNoteAction performWithAttributedTitle:contents:pinned:container:error:]
+ -[ICNote(UI) exportDataForUTI:]
+ GCC_except_table108
+ GCC_except_table130
+ GCC_except_table134
+ GCC_except_table136
+ GCC_except_table143
+ GCC_except_table145
+ GCC_except_table149
+ GCC_except_table156
+ GCC_except_table167
+ GCC_except_table186
+ GCC_except_table84
+ __101+[ICTTTextStorage(UI) fixAttachmentsForRenderingInAttributedString:forPlainText:forStandardizedText:]_block_invoke
+ __81-[ICCreateNoteAction performWithAttributedTitle:contents:pinned:container:error:]_block_invoke
+ __93+[ICTextController attributedStringToPasteWithAdaptedParagraphStyles:pasteRange:textStorage:]_block_invoke
+ ___37-[ICInlineAttachmentView updateLabel]_block_invoke
+ ___81-[ICCreateNoteAction performWithAttributedTitle:contents:pinned:container:error:]_block_invoke
+ ___83+[ICNote(AirDropDocumentUI) createNoteForAirDropDocument:legacyContext:completion:]_block_invoke_2
+ ___87-[ICCreateHTMLNoteAction performWithAttributedTitle:contents:pinned:stylesTitle:error:]_block_invoke
+ ___89-[ICCreateModernNoteAction performWithAttributedTitle:contents:pinned:stylesTitle:error:]_block_invoke
+ ___93+[ICTextController attributedStringToPasteWithAdaptedParagraphStyles:pasteRange:textStorage:]_block_invoke
+ ___block_descriptor_32_e39_"NSArray"16?0"NSPresentationIntent"8l
+ ___block_descriptor_40_e8_32r_e47_v40?0"ICTTParagraphStyle"8{_NSRange=QQ}16^B32l
+ ___block_descriptor_88_e8_32s40s48s56bs64bs72r80r_e27_v40?08{_NSRange=QQ}16^B32l
+ ___copy_helper_block_e8_32s40s48s56b64b72r80r
+ _objc_msgSend$containsRange:
+ _objc_msgSend$isEqualToNumber:
+ _objc_msgSend$linkedNoteIsPasswordProtected
+ _objc_msgSend$performWithAttributedTitle:contents:pinned:container:error:
+ _objc_msgSend$performWithAttributedTitle:contents:pinned:stylesTitle:error:
+ _objc_msgSend$setPaperHasGraph:
+ _symbolic SDy__________G 10Foundation4UUIDV So29ICCalculateDocumentControllerC7NotesUIE5IndexC
+ _symbolic _____Sg 8PaperKit19SharedCanvasElementO
+ _symbolic ___________t 10Foundation4UUIDV So29ICCalculateDocumentControllerC7NotesUIE5IndexC
+ _symbolic _____y_____G 9Coherence12CROrderedSetV 8PaperKit19SharedCanvasElementO
+ _symbolic _____y_____G 9Coherence3RefV 8PaperKit12GraphElementV
+ _symbolic _____y_____GSg 9Coherence3RefV 8PaperKit12GraphElementV
+ _symbolic _____y_____GSg_ADt 9Coherence3RefV 8PaperKit12GraphElementV
+ _symbolic _____y______G 9Coherence12CROrderedSetV8IteratorV 8PaperKit19SharedCanvasElementO
+ _symbolic _____y__________G s18_DictionaryStorageC 10Foundation4UUIDV So29ICCalculateDocumentControllerC7NotesUIE5IndexC
+ _symbolic _____y_____yAAySSGGG s18ReversedCollectionV s5SliceV
- GCC_except_table107
- GCC_except_table129
- GCC_except_table142
- GCC_except_table144
- GCC_except_table148
- GCC_except_table155
- GCC_except_table166
- GCC_except_table78
- GCC_except_table83
- __71-[ICCreateNoteAction performWithTitle:contents:pinned:container:error:]_block_invoke
- ___71-[ICCreateNoteAction performWithTitle:contents:pinned:container:error:]_block_invoke
- ___77-[ICCreateHTMLNoteAction performWithTitle:contents:pinned:stylesTitle:error:]_block_invoke
- ___79-[ICCreateModernNoteAction performWithTitle:contents:pinned:stylesTitle:error:]_block_invoke
- ___block_descriptor_80_e8_32s40s48s56bs64r72r_e27_v40?08{_NSRange=QQ}16^B32l
- _objc_msgSend$ic_darkModeEnabled
- _objc_msgSend$isStringMarkdown:
- _objc_msgSend$linkedNoteIsPasswordProtectedAndLocked
- _objc_msgSend$performWithTitle:contents:pinned:stylesTitle:error:
CStrings:
+ "-[ICCreateNoteAction performWithAttributedTitle:contents:pinned:container:error:]"
+ "@\"NSArray\"16@?0@\"NSPresentationIntent\"8"
+ "Dropping non-NSTextAttachment attachment value before serialization: %@"
+ "NotesUI/CalculateDocumentController.swift"
+ "Retaining save block until merges unblock…"
+ "Suggestion"
+ "cachedIndex(of:) must be called on the main thread"
+ "rebuildExpressionIndexCache() must be called on the main thread"
- "-[ICCreateNoteAction performWithTitle:contents:pinned:container:error:]"
```
