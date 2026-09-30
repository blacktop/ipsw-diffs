## MailSupport

> `/System/Library/PrivateFrameworks/MailSupport.framework/MailSupport`

```diff

-  __TEXT.__text: 0x225c4
-  __TEXT.__objc_methlist: 0x19c0
+  __TEXT.__text: 0x225f8
+  __TEXT.__objc_methlist: 0x19b0
   __TEXT.__gcc_except_tab: 0x27e4
   __TEXT.__cstring: 0x4bbb
   __TEXT.__const: 0x472

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1560
+  __DATA_CONST.__const: 0x1568
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1678
+  __DATA_CONST.__objc_selrefs: 0x1670
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x108
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__got: 0x558
   __AUTH_CONST.__const: 0x628
   __AUTH_CONST.__cfstring: 0x4980
-  __AUTH_CONST.__objc_const: 0x44b8
+  __AUTH_CONST.__objc_const: 0x4488
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x6a0
-  __AUTH.__objc_data: 0x260
-  __DATA.__objc_ivar: 0x1c0
-  __DATA.__data: 0xbb8
+  __AUTH_CONST.__auth_got: 0x6a8
+  __AUTH.__objc_data: 0x120
+  __DATA.__objc_ivar: 0x1bc
+  __DATA.__data: 0xb78
   __DATA.__bss: 0x348
-  __DATA_DIRTY.__objc_data: 0x10d8
-  __DATA_DIRTY.__data: 0x430
+  __DATA_DIRTY.__objc_data: 0x1218
+  __DATA_DIRTY.__data: 0x458
   __DATA_DIRTY.__bss: 0x1a0
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
Symbols:
+ +[MSParsecSearchIndexState indexStateForMessagesIndexed:messageBodiesIndexed:indexableMessages:attachmentsIndexed:indexableAttachments:]
+ -[MSParsecSearchIndexState initWithPercentMessagesIndexed:percentMessageBodiesIndexed:percentAttachmentsIndexed:totalMessageCount:indexedMessageCount:indexType:]
+ GCC_except_table51
+ GCC_except_table57
+ GCC_except_table60
+ _EMIsEnhancedSiriAvailable
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCompression_$_MailSupport
+ _objc_msgSend$initWithPercentMessagesIndexed:percentMessageBodiesIndexed:percentAttachmentsIndexed:totalMessageCount:indexedMessageCount:indexType:
- +[MSParsecSearchIndexState indexStateForMessagesIndexed:messageBodiesIndexed:indexableMessages:percentUnindexedBodiesInFrecent:attachmentsIndexed:indexableAttachments:]
- -[MSParsecSearchIndexState initWithPercentMessagesIndexed:percentMessageBodiesIndexed:percentUnindexedBodiesInFrecent:percentAttachmentsIndexed:totalMessageCount:indexedMessageCount:indexType:]
- -[MSParsecSearchIndexState percentUnindexedBodiesInFrecent]
- GCC_except_table52
- GCC_except_table59
- GCC_except_table61
- _OBJC_IVAR_$_MSParsecSearchIndexState._percentUnindexedBodiesInFrecent
- _objc_msgSend$initWithPercentMessagesIndexed:percentMessageBodiesIndexed:percentUnindexedBodiesInFrecent:percentAttachmentsIndexed:totalMessageCount:indexedMessageCount:indexType:

```
