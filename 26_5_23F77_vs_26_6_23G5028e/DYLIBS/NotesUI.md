## NotesUI

> `/System/Library/PrivateFrameworks/NotesUI.framework/NotesUI`

```diff

-2952.120.8.0.0
-  __TEXT.__text: 0x2b4d74
+2952.140.1.0.0
+  __TEXT.__text: 0x2b52d4
   __TEXT.__auth_stubs: 0x60c0
   __TEXT.__delay_stubs: 0x40
   __TEXT.__delay_helper: 0x6ec
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x16cb0
+  __TEXT.__objc_methlist: 0x16ce0
   __TEXT.__const: 0xa0a4
-  __TEXT.__cstring: 0x13ab6
+  __TEXT.__cstring: 0x13aa6
   __TEXT.__oslogstring: 0x963c
-  __TEXT.__gcc_except_tab: 0x49ac
+  __TEXT.__gcc_except_tab: 0x49d4
   __TEXT.__ustring: 0x139be
   __TEXT.__swift5_typeref: 0xca2a
   __TEXT.__constg_swiftt: 0x38c0

   __TEXT.__swift_as_ret: 0x108
   __TEXT.__swift5_protos: 0x24
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0xa108
+  __TEXT.__unwind_info: 0xa130
   __TEXT.__eh_frame: 0x4688
   __TEXT.__objc_classname: 0x3566
-  __TEXT.__objc_methname: 0x4aa0d
-  __TEXT.__objc_methtype: 0x9d49
-  __TEXT.__objc_stubs: 0x2fbc0
+  __TEXT.__objc_methname: 0x4aadd
+  __TEXT.__objc_methtype: 0x9d69
+  __TEXT.__objc_stubs: 0x2fc60
   __DATA_CONST.__got: 0x2dd0
   __DATA_CONST.__const: 0x6348
   __DATA_CONST.__objc_classlist: 0xa90

   __DATA_CONST.__objc_catlist2: 0x10
   __DATA_CONST.__objc_protolist: 0x3b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xfc08
+  __DATA_CONST.__objc_selrefs: 0xfc38
   __DATA_CONST.__objc_protorefs: 0x168
   __DATA_CONST.__objc_superrefs: 0x680
   __DATA_CONST.__objc_arraydata: 0x318
   __AUTH_CONST.__auth_got: 0x3080
   __AUTH_CONST.__const: 0x9b40
   __AUTH_CONST.__cfstring: 0xbda0
-  __AUTH_CONST.__objc_const: 0x23c58
+  __AUTH_CONST.__objc_const: 0x23c70
   __AUTH_CONST.__objc_arrayobj: 0x1e0
   __AUTH_CONST.__objc_intobj: 0x648
   __AUTH_CONST.__objc_doubleobj: 0x120

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B6D3682B-0FA0-3496-A55C-A60C883449AD
-  Functions: 14484
-  Symbols:   32156
-  CStrings:  16662
+  UUID: 701BF678-4E26-3EA0-8A6F-9C71C277FC48
+  Functions: 14489
+  Symbols:   32173
+  CStrings:  16669
 
Symbols:
+ -[ICTodoButton(PlatformSpecificResponsibility) pointInside:withEvent:]
+ -[ICVirtualSmartFolderItemIdentifier hasVisibleInvitationsInContext:]
+ -[ICVirtualSmartFolderItemIdentifier hasVisibleNotesInContext:]
+ ___63-[ICVirtualSmartFolderItemIdentifier hasVisibleNotesInContext:]_block_invoke
+ ___69-[ICVirtualSmartFolderItemIdentifier hasVisibleInvitationsInContext:]_block_invoke
+ ___block_literal_global.224
+ _objc_msgSend$hasInvitationMatchingPredicate:context:
+ _objc_msgSend$hasNoteMatchingPredicate:context:
+ _objc_msgSend$hasVisibleInvitationsInContext:
+ _objc_msgSend$hasVisibleNotes
+ _objc_msgSend$hasVisibleNotesInContext:
+ _objc_msgSend$trackedParagraphIsRTL
- ___block_literal_global.204
- ___block_literal_global.220
- _objc_msgSend$visibleItemCountInContext:
CStrings:
+ "         folderType != %d AND          owner.didChooseToMigrate == YES AND          markedForDeletion != YES AND          needsInitialFetchFromCloud != YES AND          (folderType != %d || SUBQUERY(notes, $n, $n.markedForDeletion != YES).@count > 0)"
+ "B40@0:8{CGPoint=dd}16@32"
+ "hasInvitationMatchingPredicate:context:"
+ "hasNoteMatchingPredicate:context:"
+ "hasVisibleInvitationsInContext:"
+ "hasVisibleNotes"
+ "hasVisibleNotesInContext:"
+ "pointInside:withEvent:"
- "         isHiddenNoteContainer != YES AND          owner.didChooseToMigrate == YES AND          markedForDeletion != YES AND          needsInitialFetchFromCloud != YES AND          (folderType != %d || SUBQUERY(notes, $n, $n.markedForDeletion != YES).@count > 0)"

```
