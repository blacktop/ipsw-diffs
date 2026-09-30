## FeedbackCore

> `/System/Library/PrivateFrameworks/FeedbackCore.framework/Versions/A/FeedbackCore`

```diff

-150.8.1.0.0
-  __TEXT.__text: 0xf45cc
+150.10.0.0.0
+  __TEXT.__text: 0xf4754
   __TEXT.__auth_stubs: 0x1990
-  __TEXT.__objc_methlist: 0x6cdc
+  __TEXT.__objc_methlist: 0x6ce4
   __TEXT.__const: 0xe14
-  __TEXT.__cstring: 0x83ec
+  __TEXT.__cstring: 0x83fc
   __TEXT.__oslogstring: 0x85f2
   __TEXT.__gcc_except_tab: 0x1734
   __TEXT.__ustring: 0xdc

   __TEXT.__unwind_info: 0x31a0
   __TEXT.__eh_frame: 0x1388
   __TEXT.__objc_classname: 0xa10
-  __TEXT.__objc_methname: 0x1204d
+  __TEXT.__objc_methname: 0x120cf
   __TEXT.__objc_methtype: 0x18e6
-  __TEXT.__objc_stubs: 0xda60
-  __DATA_CONST.__got: 0xba0
+  __TEXT.__objc_stubs: 0xdac0
+  __DATA_CONST.__got: 0xba8
   __DATA_CONST.__const: 0xf58
   __DATA_CONST.__objc_classlist: 0x320
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4ba8
+  __DATA_CONST.__objc_selrefs: 0x4bc0
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x1b8
   __DATA_CONST.__objc_arraydata: 0x4c8
   __AUTH_CONST.__auth_got: 0xcd8
   __AUTH_CONST.__auth_ptr: 0x3c8
   __AUTH_CONST.__const: 0x54b8
-  __AUTH_CONST.__cfstring: 0x8280
-  __AUTH_CONST.__objc_const: 0xdd18
+  __AUTH_CONST.__cfstring: 0x82c0
+  __AUTH_CONST.__objc_const: 0xdd28
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x468

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 4602
-  Symbols:   7724
-  CStrings:  5675
+  Symbols:   7728
+  CStrings:  5681
 
Symbols:
+ -[FBKFileCollector getUniqueFileNameForAttachmentType:utTypeIdentifier:]
+ -[FBKFileCollector newAttachmentWithType:utTypeIdentifier:]
+ GCC_except_table74
+ _UTTypeHEIC
+ __44-[FBKFileCollector _attachURL:toAttachment:]_block_invoke.118
+ __49-[FBKHTTPClient jsonForURLRequest:success:error:]_block_invoke.133
+ __50-[FBKFileCollector commitWithForm:withCompletion:]_block_invoke.105
+ __61-[FBKHTTPClient dataForURLRequest:successWithResponse:error:]_block_invoke.109
+ __61-[FBKHTTPClient dataForURLRequest:successWithResponse:error:]_block_invoke.116
+ ___72-[FBKFileCollector getUniqueFileNameForAttachmentType:utTypeIdentifier:]_block_invoke
+ ___72-[FBKFileCollector getUniqueFileNameForAttachmentType:utTypeIdentifier:]_block_invoke_2
+ __block_literal_global.101
+ __block_literal_global.107
+ __block_literal_global.116
+ _objc_msgSend$getUniqueFileNameForAttachmentType:utTypeIdentifier:
+ _objc_msgSend$newAttachmentWithType:utTypeIdentifier:
+ _objc_msgSend$preferredFilenameExtension
+ _objc_msgSend$setShouldHideTitle:
- -[FBKFileCollector addImageWithItemProvider:]
- -[FBKFileCollector addImageWithItemProvider:].cold.1
- GCC_except_table73
- __44-[FBKFileCollector _attachURL:toAttachment:]_block_invoke.114
- __49-[FBKHTTPClient jsonForURLRequest:success:error:]_block_invoke.130
- __50-[FBKFileCollector commitWithForm:withCompletion:]_block_invoke.101
- __61-[FBKHTTPClient dataForURLRequest:successWithResponse:error:]_block_invoke.106
- __61-[FBKHTTPClient dataForURLRequest:successWithResponse:error:]_block_invoke.113
- ___55-[FBKFileCollector getUniqueFileNameForAttachmentType:]_block_invoke
- ___55-[FBKFileCollector getUniqueFileNameForAttachmentType:]_block_invoke_2
- __block_literal_global.108
- __block_literal_global.110
- __block_literal_global.97
- _objc_msgSend$getUniqueFileNameForAttachmentType:
CStrings:
+ ".%@"
+ "Using filing device OS version: [%{public}@]"
+ "X-OS-Version"
+ "getUniqueFileNameForAttachmentType:utTypeIdentifier:"
+ "newAttachmentWithType:utTypeIdentifier:"
+ "preferredFilenameExtension"
+ "setShouldHideTitle:"
+ "shouldHideTitle"
- "addImageWithItemProvider not implemented on macOS"
- "addImageWithItemProvider:"

```
