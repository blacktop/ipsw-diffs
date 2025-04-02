## MailSupport

> `/System/Library/PrivateFrameworks/MailSupport.framework/Versions/A/MailSupport`

```diff

-3826.500.181.1.5
-  __TEXT.__text: 0x1c7e0
+3826.600.15.1.1
+  __TEXT.__text: 0x1c8a8
   __TEXT.__auth_stubs: 0x9f0
-  __TEXT.__objc_methlist: 0x17c0
-  __TEXT.__gcc_except_tab: 0x2980
-  __TEXT.__cstring: 0x46fd
+  __TEXT.__objc_methlist: 0x17d8
+  __TEXT.__gcc_except_tab: 0x2988
+  __TEXT.__cstring: 0x471d
   __TEXT.__const: 0x3a4
   __TEXT.__oslogstring: 0x6e6
   __TEXT.__dlopen_cstrs: 0x52

   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0x8
   __TEXT.__swift5_capture: 0x68
-  __TEXT.__unwind_info: 0xd00
+  __TEXT.__unwind_info: 0xd08
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x650
-  __TEXT.__objc_methname: 0x547a
-  __TEXT.__objc_methtype: 0x850
-  __TEXT.__objc_stubs: 0x3b40
+  __TEXT.__objc_methname: 0x55af
+  __TEXT.__objc_methtype: 0x85c
+  __TEXT.__objc_stubs: 0x3b60
   __DATA_CONST.__got: 0x4e0
   __DATA_CONST.__const: 0xff0
   __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14c8
+  __DATA_CONST.__objc_selrefs: 0x14d8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x100
   __DATA_CONST.__objc_arraydata: 0x10

   __AUTH_CONST.__auth_ptr: 0x108
   __AUTH_CONST.__const: 0x888
   __AUTH_CONST.__cfstring: 0x4980
-  __AUTH_CONST.__objc_const: 0x3ef0
+  __AUTH_CONST.__objc_const: 0x3f50
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x860
   __AUTH.__data: 0x58
-  __DATA.__objc_ivar: 0x198
+  __DATA.__objc_ivar: 0x1a0
   __DATA.__data: 0x6d0
   __DATA.__bss: 0x598
   __DATA_DIRTY.__objc_data: 0x820

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 672
-  Symbols:   2556
-  CStrings:  1781
+  Functions: 674
+  Symbols:   2561
+  CStrings:  1787
 
Symbols:
+ +[MSParsecSearchIndexState indexStateForMessagesIndexed:messageBodiesIndexed:indexableMessages:percentUnindexedBodiesInFrecent:attachmentsIndexed:indexableAttachments:]
+ -[MSParsecSearchIndexState initWithPercentMessagesIndexed:percentMessageBodiesIndexed:percentUnindexedBodiesInFrecent:percentAttachmentsIndexed:totalMessageCount:indexedMessageCount:indexType:]
+ -[MSParsecSearchIndexState percentMessageBodiesIndexed]
+ -[MSParsecSearchIndexState percentUnindexedBodiesInFrecent]
+ GCC_except_table47
+ GCC_except_table48
+ GCC_except_table52
+ OBJC_IVAR_$_MSParsecSearchIndexState._percentMessageBodiesIndexed
+ OBJC_IVAR_$_MSParsecSearchIndexState._percentUnindexedBodiesInFrecent
+ _objc_msgSend$initWithPercentMessagesIndexed:percentMessageBodiesIndexed:percentUnindexedBodiesInFrecent:percentAttachmentsIndexed:totalMessageCount:indexedMessageCount:indexType:
+ _objc_msgSend$percentMessageBodiesIndexed
- +[MSParsecSearchIndexState indexStateForMessagesIndexed:indexableMessages:attachmentsIndexed:indexableAttachments:]
- -[MSParsecSearchIndexState initWithPercentMessagesIndexed:percentAttachmentsIndexed:totalMessageCount:indexedMessageCount:indexType:]
- GCC_except_table45
- GCC_except_table46
- GCC_except_table50
- _objc_msgSend$initWithPercentMessagesIndexed:percentAttachmentsIndexed:totalMessageCount:indexedMessageCount:indexType:
CStrings:
+ "@64@0:8@16@24@32@40@48@56"
+ "@72@0:8q16q24q32q40q48q56q64"
+ "Tq,R,V_percentMessageBodiesIndexed"
+ "Tq,R,V_percentUnindexedBodiesInFrecent"
+ "_percentMessageBodiesIndexed"
+ "_percentUnindexedBodiesInFrecent"
+ "indexStateForMessagesIndexed:messageBodiesIndexed:indexableMessages:percentUnindexedBodiesInFrecent:attachmentsIndexed:indexableAttachments:"
+ "indexType: %ld percentMessagesIndexed: %ld percentMessageBodiesIndexed: %ld percentAttachmentsIndexed: %ld totalMessageCount: %ld indexedMessageCount: %ld "
+ "initWithPercentMessagesIndexed:percentMessageBodiesIndexed:percentUnindexedBodiesInFrecent:percentAttachmentsIndexed:totalMessageCount:indexedMessageCount:indexType:"
+ "percentMessageBodiesIndexed"
+ "percentUnindexedBodiesInFrecent"
- "@48@0:8@16@24@32@40"
- "@56@0:8q16q24q32q40q48"
- "indexStateForMessagesIndexed:indexableMessages:attachmentsIndexed:indexableAttachments:"
- "indexType: %ld percentMessagesIndexed: %ld percentAttachmentsIndexed: %ld totalMessageCount: %ld indexedMessageCount: %ld "
- "initWithPercentMessagesIndexed:percentAttachmentsIndexed:totalMessageCount:indexedMessageCount:indexType:"

```
