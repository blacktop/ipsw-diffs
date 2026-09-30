## MailSupport

> `/System/Library/PrivateFrameworks/MailSupport.framework/Versions/A/MailSupport`

```diff

-  __TEXT.__text: 0x23a14
-  __TEXT.__objc_methlist: 0x19c0
-  __TEXT.__gcc_except_tab: 0x26c0
+  __TEXT.__text: 0x23a3c
+  __TEXT.__objc_methlist: 0x19b0
+  __TEXT.__gcc_except_tab: 0x26bc
   __TEXT.__cstring: 0x49fb
   __TEXT.__const: 0x482
   __TEXT.__oslogstring: 0x668

   __TEXT.__swift5_proto: 0x1c
   __TEXT.__swift5_types: 0x10
   __TEXT.__swift5_capture: 0xdc
-  __TEXT.__unwind_info: 0xff8
+  __TEXT.__unwind_info: 0x1000
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1230
+  __DATA_CONST.__const: 0x1238
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1670
+  __DATA_CONST.__objc_selrefs: 0x1668
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x108
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__got: 0x548
   __AUTH_CONST.__const: 0x9e8
   __AUTH_CONST.__cfstring: 0x4980
-  __AUTH_CONST.__objc_const: 0x44a8
+  __AUTH_CONST.__objc_const: 0x4478
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x528
-  __AUTH.__objc_data: 0x260
-  __DATA.__objc_ivar: 0x1c0
+  __AUTH_CONST.__auth_got: 0x530
+  __AUTH.__objc_data: 0x7b0
+  __DATA.__objc_ivar: 0x1bc
   __DATA.__data: 0xbf8
   __DATA.__bss: 0x338
-  __DATA_DIRTY.__objc_data: 0x10d8
+  __DATA_DIRTY.__objc_data: 0xb88
   __DATA_DIRTY.__data: 0x3f8
   __DATA_DIRTY.__bss: 0x180
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 977
-  Symbols:   2751
+  Symbols:   2752
   CStrings:  1301
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
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
~ __DATA.__data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ +[MSParsecSearchIndexState indexStateForMessagesIndexed:messageBodiesIndexed:indexableMessages:attachmentsIndexed:indexableAttachments:]
+ -[MSParsecSearchIndexState initWithPercentMessagesIndexed:percentMessageBodiesIndexed:percentAttachmentsIndexed:totalMessageCount:indexedMessageCount:indexType:]
+ GCC_except_table51
+ GCC_except_table57
+ GCC_except_table62
+ _EMIsEnhancedSiriAvailable
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCompression_$_MailSupport
+ _objc_msgSend$initWithPercentMessagesIndexed:percentMessageBodiesIndexed:percentAttachmentsIndexed:totalMessageCount:indexedMessageCount:indexType:
- +[MSParsecSearchIndexState indexStateForMessagesIndexed:messageBodiesIndexed:indexableMessages:percentUnindexedBodiesInFrecent:attachmentsIndexed:indexableAttachments:]
- -[MSParsecSearchIndexState initWithPercentMessagesIndexed:percentMessageBodiesIndexed:percentUnindexedBodiesInFrecent:percentAttachmentsIndexed:totalMessageCount:indexedMessageCount:indexType:]
- -[MSParsecSearchIndexState percentUnindexedBodiesInFrecent]
- GCC_except_table52
- GCC_except_table59
- GCC_except_table63
- OBJC_IVAR_$_MSParsecSearchIndexState._percentUnindexedBodiesInFrecent
- _objc_msgSend$initWithPercentMessagesIndexed:percentMessageBodiesIndexed:percentUnindexedBodiesInFrecent:percentAttachmentsIndexed:totalMessageCount:indexedMessageCount:indexType:

```
