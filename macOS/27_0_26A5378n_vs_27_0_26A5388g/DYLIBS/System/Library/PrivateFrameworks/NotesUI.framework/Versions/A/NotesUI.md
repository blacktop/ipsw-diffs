## NotesUI

> `/System/Library/PrivateFrameworks/NotesUI.framework/Versions/A/NotesUI`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__oslogstring`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__DATA.__data`
- `__DATA.__objc_stublist`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-3190.0.0.500.1
-  __TEXT.__text: 0x26ed90
+3192.0.0.0.0
+  __TEXT.__text: 0x271dec
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x12000
-  __TEXT.__const: 0x8f34
-  __TEXT.__cstring: 0x1180c
+  __TEXT.__objc_methlist: 0x12060
+  __TEXT.__const: 0x8f44
+  __TEXT.__cstring: 0x1192c
   __TEXT.__gcc_except_tab: 0x419c
   __TEXT.__oslogstring: 0x8bd7
   __TEXT.__ustring: 0x14c06
-  __TEXT.__constg_swiftt: 0x31c4
+  __TEXT.__constg_swiftt: 0x3204
   __TEXT.__swift5_typeref: 0xbe16
-  __TEXT.__swift5_reflstr: 0x1bc3
-  __TEXT.__swift5_fieldmd: 0x1e90
+  __TEXT.__swift5_reflstr: 0x1bf3
+  __TEXT.__swift5_fieldmd: 0x1e9c
   __TEXT.__swift5_builtin: 0x21c
   __TEXT.__swift5_assocty: 0x7c0
   __TEXT.__swift5_proto: 0x3a8
   __TEXT.__swift5_types: 0x280
   __TEXT.__swift5_capture: 0x1980
-  __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift_as_entry: 0xc4
   __TEXT.__swift_as_ret: 0xe0
   __TEXT.__swift_as_cont: 0x17c
-  __TEXT.__unwind_info: 0x8348
+  __TEXT.__swift5_protos: 0x1c
+  __TEXT.__unwind_info: 0x8398
   __TEXT.__eh_frame: 0x3bd8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x15e8
-  __DATA_CONST.__objc_classlist: 0x820
+  __DATA_CONST.__const: 0x1610
+  __DATA_CONST.__objc_classlist: 0x828
   __DATA_CONST.__objc_catlist: 0x268
   __DATA_CONST.__objc_protolist: 0x298
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd3d0
+  __DATA_CONST.__objc_selrefs: 0xd438
   __DATA_CONST.__objc_protorefs: 0xf8
-  __DATA_CONST.__objc_superrefs: 0x530
+  __DATA_CONST.__objc_superrefs: 0x538
   __DATA_CONST.__objc_arraydata: 0x2e0
-  __DATA_CONST.__got: 0x2798
-  __AUTH_CONST.__const: 0xce28
-  __AUTH_CONST.__cfstring: 0xa920
-  __AUTH_CONST.__objc_const: 0x1c610
+  __DATA_CONST.__got: 0x27a8
+  __AUTH_CONST.__const: 0xcfa8
+  __AUTH_CONST.__cfstring: 0xa940
+  __AUTH_CONST.__objc_const: 0x1c738
   __AUTH_CONST.__objc_arrayobj: 0x1c8
-  __AUTH_CONST.__objc_intobj: 0x4c8
+  __AUTH_CONST.__objc_intobj: 0x4f8
   __AUTH_CONST.__objc_doubleobj: 0x190
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x2b98
-  __AUTH.__objc_data: 0x2368
-  __AUTH.__data: 0x1788
-  __DATA.__objc_ivar: 0xeb8
+  __AUTH_CONST.__auth_got: 0x2ba0
+  __AUTH.__objc_data: 0x23b8
+  __AUTH.__data: 0x17d8
+  __DATA.__objc_ivar: 0xec0
   __DATA.__data: 0x4598
   __DATA.__objc_stublist: 0x20
-  __DATA.__bss: 0x3860
+  __DATA.__bss: 0x3870
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x3a88
   __DATA_DIRTY.__data: 0x2500

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12599
-  Symbols:   18459
-  CStrings:  2850
+  Functions: 12644
+  Symbols:   18504
+  CStrings:  2857
 
Symbols:
+ -[ICAttachment(UI) imageActivityItemProvider]
+ -[ICAuthorHighlightsController flashNavigationHighlightForRange:color:duration:inTextStorage:]
+ -[ICCreateHTMLNoteAction performWithTitle:contents:pinned:stylesTitle:error:]
+ -[ICCreateModernNoteAction performWithTitle:contents:pinned:stylesTitle:error:]
+ -[ICCreateNoteAction setStylesTitle:]
+ -[ICCreateNoteAction stylesTitle]
+ -[ICMAttachmentImageActivityItemProvider .cxx_destruct]
+ -[ICMAttachmentImageActivityItemProvider initWithAttachment:]
+ -[ICMAttachmentImageActivityItemProvider itemProvider]
+ GCC_except_table60
+ GCC_except_table71
+ OBJC_IVAR_$_ICCreateNoteAction._stylesTitle
+ OBJC_IVAR_$_ICMAttachmentImageActivityItemProvider._itemProvider
+ _ICAuthorHighlightAnimationDefaultNavigationFlashDuration
+ _ICNoteExporterAIGCDocumentCommentSentinel
+ _NSCommentDocumentAttribute
+ _OBJC_CLASS_$_ICMAttachmentImageActivityItemProvider
+ _OBJC_METACLASS_$_ICMAttachmentImageActivityItemProvider
+ __45-[ICAttachment(UI) imageActivityItemProvider]_block_invoke
+ __45-[ICAttachment(UI) imageActivityItemProvider]_block_invoke_2
+ __OBJC_$_INSTANCE_METHODS_ICMAttachmentImageActivityItemProvider
+ __OBJC_$_INSTANCE_VARIABLES_ICMAttachmentImageActivityItemProvider
+ __OBJC_$_PROP_LIST_ICMAttachmentImageActivityItemProvider
+ __OBJC_CLASS_RO_$_ICMAttachmentImageActivityItemProvider
+ __OBJC_METACLASS_RO_$_ICMAttachmentImageActivityItemProvider
+ ___45-[ICAttachment(UI) imageActivityItemProvider]_block_invoke
+ ___45-[ICAttachment(UI) imageActivityItemProvider]_block_invoke_2
+ ___45-[ICAttachment(UI) imageActivityItemProvider]_block_invoke_3
+ ___45-[ICAttachment(UI) imageActivityItemProvider]_block_invoke_4
+ ___77-[ICCreateHTMLNoteAction performWithTitle:contents:pinned:stylesTitle:error:]_block_invoke
+ ___79-[ICCreateModernNoteAction performWithTitle:contents:pinned:stylesTitle:error:]_block_invoke
+ ___94-[ICAuthorHighlightsController flashNavigationHighlightForRange:color:duration:inTextStorage:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e22_v16?0"ICAttachment"8l
+ ___block_descriptor_40_e8_32bs_e45_"NSProgress"16?0?<v?"NSData""NSError">8l
+ ___block_descriptor_40_e8_32bs_e45_"NSProgress"16?0?<v?"NSURL"B"NSError">8l
+ ___block_descriptor_40_e8_32bs_e62_"NSProgress"16?0?<v?"<NSItemProviderWriting>""NSError">8l
+ ___block_descriptor_40_e8_32bs_e63_v32?0?<v?"<NSSecureCoding>""NSError">8#16"NSDictionary"24l
+ ___block_descriptor_48_e8_32s40s_e29_v16?0?<v?"ICAttachment">8l
+ ___block_descriptor_64_e8_32s40s48s56s_e20_v24?0{_NSRange=QQ}8l
+ ___block_descriptor_66_e8_32s40s48r56r_e5_v8?0l
+ _objc_msgSend$allowsAccessRequests
+ _objc_msgSend$ic_containsAttribute:
+ _objc_msgSend$imageActivityItemProvider
+ _objc_msgSend$itemProvider
+ _objc_msgSend$linkedNoteIsPasswordProtectedAndLocked
+ _objc_msgSend$performWithTitle:contents:pinned:stylesTitle:error:
+ _objc_msgSend$predicateForNotesWithIdentifier:
+ _objc_msgSend$registerDataRepresentationForTypeIdentifier:visibility:loadHandler:
+ _objc_msgSend$registerFileRepresentationForTypeIdentifier:fileOptions:visibility:loadHandler:
+ _objc_msgSend$registerItemForTypeIdentifier:loadHandler:
+ _objc_msgSend$registerObjectOfClass:visibility:loadHandler:
+ _objc_msgSend$setAllowsAnimations:
+ _objc_msgSend$stylesTitle
+ _objc_msgSend$useAILabeling
+ keypath_get.134Tm
- -[ICCreateHTMLNoteAction performWithTitle:contents:pinned:error:]
- -[ICCreateModernNoteAction performWithTitle:contents:pinned:error:]
- GCC_except_table30
- GCC_except_table52
- GCC_except_table53
- ___65-[ICCreateHTMLNoteAction performWithTitle:contents:pinned:error:]_block_invoke
- ___67-[ICCreateModernNoteAction performWithTitle:contents:pinned:error:]_block_invoke
- _objc_msgSend$newNoteWithAttributedString:inFolder:error:
- _objc_msgSend$performWithTitle:contents:pinned:error:
- keypath_get.124Tm
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YHiENJ/Sources/NotesFramework/NotesUI/Mac/ICMAlertSheetTouchBarController.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YHiENJ/Sources/NotesFramework/NotesUI/Text/TextAttachments/ICBaseAttachmentView.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YHiENJ/Sources/NotesFramework/NotesUI/Utilities/ICLongRunningTaskController.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YHiENJ/Sources/NotesFramework/NotesUI/Views/ICLoadingPieLayer.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YHiENJ/Sources/NotesFramework/NotesUI/WebView/NoteHTMLEditorView.m"
+ "@\"NSProgress\"16@?0@?<v@?@\"<NSItemProviderWriting>\"@\"NSError\">8"
+ "@\"NSProgress\"16@?0@?<v@?@\"NSData\"@\"NSError\">8"
+ "@\"NSProgress\"16@?0@?<v@?@\"NSURL\"B@\"NSError\">8"
+ "AIGC=1;src=writingTools"
+ "v16@?0@\"ICAttachment\"8"
+ "v16@?0@?<v@?@\"ICAttachment\">8"
+ "v32@?0@?<v@?@\"<NSSecureCoding>\"@\"NSError\">8#16@\"NSDictionary\"24"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ek15qR/Sources/NotesFramework/NotesUI/Mac/ICMAlertSheetTouchBarController.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ek15qR/Sources/NotesFramework/NotesUI/Text/TextAttachments/ICBaseAttachmentView.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ek15qR/Sources/NotesFramework/NotesUI/Utilities/ICLongRunningTaskController.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ek15qR/Sources/NotesFramework/NotesUI/Views/ICLoadingPieLayer.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ek15qR/Sources/NotesFramework/NotesUI/WebView/NoteHTMLEditorView.m"
```
