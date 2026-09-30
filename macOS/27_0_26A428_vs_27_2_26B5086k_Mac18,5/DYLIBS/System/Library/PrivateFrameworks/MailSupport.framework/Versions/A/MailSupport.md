## MailSupport

> `/System/Library/PrivateFrameworks/MailSupport.framework/Versions/A/MailSupport`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-3901.100.1.1.11
-  __TEXT.__text: 0x23578
-  __TEXT.__objc_methlist: 0x19b0
-  __TEXT.__gcc_except_tab: 0x26e4
-  __TEXT.__cstring: 0x4c1b
+3901.200.34.0.0
+  __TEXT.__text: 0x23994
+  __TEXT.__objc_methlist: 0x19c0
+  __TEXT.__gcc_except_tab: 0x2714
   __TEXT.__const: 0x482
+  __TEXT.__cstring: 0x4c1b
   __TEXT.__oslogstring: 0x678
   __TEXT.__dlopen_cstrs: 0x52
   __TEXT.__ustring: 0x18
   __TEXT.__swift5_typeref: 0x3d2
+  __TEXT.__swift5_capture: 0xdc
   __TEXT.__constg_swiftt: 0x140
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_reflstr: 0xae

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x1c
   __TEXT.__swift5_types: 0x10
-  __TEXT.__swift5_capture: 0xdc
-  __TEXT.__unwind_info: 0x1200
+  __TEXT.__unwind_info: 0x1220
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1260
+  __DATA_CONST.__const: 0x1270
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1670
+  __DATA_CONST.__objc_selrefs: 0x1680
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x108
+  __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x18
-  __DATA_CONST.__got: 0x548
-  __AUTH_CONST.__const: 0x9e8
+  __DATA_CONST.__got: 0x550
+  __AUTH_CONST.__const: 0x9c8
   __AUTH_CONST.__cfstring: 0x49c0
-  __AUTH_CONST.__objc_const: 0x4478
-  __AUTH_CONST.__objc_intobj: 0x168
+  __AUTH_CONST.__objc_const: 0x4458
+  __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x530
   __AUTH.__objc_data: 0x170
   __DATA.__objc_ivar: 0x1bc
-  __DATA.__data: 0xc18
+  __DATA.__data: 0xc40
   __DATA_DIRTY.__objc_data: 0x11c8
-  __DATA_DIRTY.__data: 0x438
-  __DATA_DIRTY.__bss: 0x180
+  __DATA_DIRTY.__data: 0x440
+  __DATA_DIRTY.__bss: 0x170
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 993
-  Symbols:   2540
-  CStrings:  720
+  Functions: 998
+  Symbols:   2542
+  CStrings:  722
 
Symbols:
+ +[MSCustomProtocolURLSchemeHandler handlerForURLScheme:]
+ -[MSCustomProtocolURLSchemeHandler .cxx_destruct]
+ -[MSCustomProtocolURLSchemeHandler initWithAllowedScheme:]
+ -[MSParsecSearchIndexState initWithPercentMessagesIndexed:percentMessageBodiesIndexed:percentAttachmentsIndexed:totalMessageCount:indexedMessageCount:]
+ GCC_except_table50
+ GCC_except_table56
+ GCC_except_table61
+ OBJC_IVAR_$_MSCustomProtocolURLSchemeHandler._allowedScheme
+ _NSURLErrorDomain
+ _OBJC_CLASS_$_NSError
+ __OBJC_$_INSTANCE_VARIABLES_MSCustomProtocolURLSchemeHandler
+ _objc_msgSend$ef_hasScheme:
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$initWithAllowedScheme:
+ _objc_msgSend$initWithPercentMessagesIndexed:percentMessageBodiesIndexed:percentAttachmentsIndexed:totalMessageCount:indexedMessageCount:
- +[MSCustomProtocolURLSchemeHandler sharedHandler]
- -[MSParsecSearchIndexState indexType]
- -[MSParsecSearchIndexState initWithPercentMessagesIndexed:percentMessageBodiesIndexed:percentAttachmentsIndexed:totalMessageCount:indexedMessageCount:indexType:]
- GCC_except_table51
- GCC_except_table58
- GCC_except_table62
- OBJC_IVAR_$_MSParsecSearchIndexState._indexType
- __OBJC_$_CLASS_PROP_LIST_MSCustomProtocolURLSchemeHandler
- ___49+[MSCustomProtocolURLSchemeHandler sharedHandler]_block_invoke
- _objc_msgSend$indexType
- _objc_msgSend$initWithPercentMessagesIndexed:percentMessageBodiesIndexed:percentAttachmentsIndexed:totalMessageCount:indexedMessageCount:indexType:
- sharedHandler.handler
- sharedHandler.onceToken
CStrings:
+ "WebKitImageMetadata"
+ "i"
+ "percentMessagesIndexed: %ld percentMessageBodiesIndexed: %ld percentAttachmentsIndexed: %ld totalMessageCount: %ld indexedMessageCount: %ld "
- "indexType: %ld percentMessagesIndexed: %ld percentMessageBodiesIndexed: %ld percentAttachmentsIndexed: %ld totalMessageCount: %ld indexedMessageCount: %ld "
```
