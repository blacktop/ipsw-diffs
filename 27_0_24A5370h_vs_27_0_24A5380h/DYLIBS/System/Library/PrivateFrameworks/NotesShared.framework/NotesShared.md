## NotesShared

> `/System/Library/PrivateFrameworks/NotesShared.framework/NotesShared`

```diff

-  __TEXT.__text: 0x348ae0
+  __TEXT.__text: 0x349430
   __TEXT.__delay_stubs: 0x240
   __TEXT.__delay_helper: 0x830
-  __TEXT.__objc_methlist: 0x1829c
+  __TEXT.__objc_methlist: 0x182dc
   __TEXT.__const: 0xdb68
-  __TEXT.__cstring: 0x19334
-  __TEXT.__gcc_except_tab: 0xf0a8
-  __TEXT.__oslogstring: 0x1c909
+  __TEXT.__cstring: 0x19344
+  __TEXT.__gcc_except_tab: 0xf0a4
+  __TEXT.__oslogstring: 0x1cbc9
   __TEXT.__ustring: 0x39a
   __TEXT.__swift5_typeref: 0x4338
   __TEXT.__swift5_fieldmd: 0x2dc8

   __TEXT.__swift5_capture: 0x1d64
   __TEXT.__swift_as_entry: 0x180
   __TEXT.__swift_as_ret: 0x1b0
-  __TEXT.__swift_as_cont: 0x3ec
+  __TEXT.__swift_as_cont: 0x3e8
   __TEXT.__swift5_mpenum: 0x74
-  __TEXT.__unwind_info: 0xefe0
+  __TEXT.__unwind_info: 0xf018
   __TEXT.__eh_frame: 0x8710
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0xcb80
+  __DATA_CONST.__objc_selrefs: 0xcbc0
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x6c0
   __DATA_CONST.__objc_arraydata: 0x228
-  __DATA_CONST.__got: 0x2120
+  __DATA_CONST.__got: 0x2130
   __AUTH_CONST.__const: 0xdb08
-  __AUTH_CONST.__cfstring: 0xf9e0
-  __AUTH_CONST.__objc_const: 0x223a0
+  __AUTH_CONST.__cfstring: 0xfa00
+  __AUTH_CONST.__objc_const: 0x223a8
   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__objc_intobj: 0x450
   __AUTH_CONST.__objc_arrayobj: 0x258
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x2a50
-  __AUTH.__objc_data: 0x2fe0
+  __AUTH.__objc_data: 0x2d60
   __AUTH.__data: 0x1438
   __DATA.__objc_ivar: 0xd88
-  __DATA.__data: 0x4a8c
+  __DATA.__data: 0x4a5c
   __DATA.__objc_stublist: 0x20
-  __DATA.__bss: 0x10230
+  __DATA.__bss: 0x101a0
   __DATA.__common: 0x180
-  __DATA_DIRTY.__objc_data: 0x4748
-  __DATA_DIRTY.__data: 0x1c58
-  __DATA_DIRTY.__bss: 0x2930
+  __DATA_DIRTY.__objc_data: 0x49c8
+  __DATA_DIRTY.__data: 0x1c88
+  __DATA_DIRTY.__bss: 0x29d0
   __DATA_DIRTY.__common: 0x1f0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 18515
-  Symbols:   39559
-  CStrings:  7234
+  Functions: 18521
+  Symbols:   39580
+  CStrings:  7242
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__data : content changed
~ __DATA.__objc_ivar : content changed
~ __DATA.__objc_stublist : content changed
Symbols:
+ +[ICInlineAttachment refreshDisplayTextForParagraphLinkAttachments:reason:]
+ +[ICReindexer migrateSearchIndexVersionIfNeeded]
+ -[ICNote(SearchIndexableNote) shouldDeferIndexingInMemoryConstrainedExtension]
+ -[ICNoteContext finishPendingSearchIndexingSynchronously]
+ -[ICNoteContext startSearchIndexerChangeObservingSynchronously]
+ GCC_except_table158
+ ___57-[ICNoteContext finishPendingSearchIndexingSynchronously]_block_invoke
+ ___block_descriptor_56_e8_32s40s48r_e27_v40?08{_NSRange=QQ}16^B32ls32l8s40l8r48l8
+ _kICReindexAttachmentsOnLaunchKey
+ _objc_msgSend$finishObservedChangesAndRemainingOperationsWithCompletionHandler:
+ _objc_msgSend$indexingScope
+ _objc_msgSend$paragraphLinkDisplayTextForRTL:
+ _objc_msgSend$startObservingChangesAndWait
- ___block_descriptor_56_e8_32s40s48r_e27_v40?08{_NSRange=QQ}16^B32ls32l8r48l8s40l8
CStrings:
+ "No need to delete search indexing before reindexing. Updating the indexing version to expected version"
+ "Search index does not need to be upgraded although indexing version does not match. Current version = %lu, expected version = %lu. Directly updating the indexing version to expected version"
+ "Search index needs to be upgraded because indexing version does not match. Current version = %lu, expected version = %lu"
+ "allIndexableObjectIDsInReversedReindexingOrderWithContext: data source %@ skipping attachments (ICIndexingScopeExcludingAttachments)"
+ "rdar23306437-memcal: indexing note %@ charCount=%lu serializedNoteData=%lu bytes"
+ "rdar23306437-memcal: note %@ serializedNoteData=%lu bytes threshold=%lu defer=%@"
+ "reindexAttachmentsOnLaunch"

```
