## MailCore

> `/System/Library/PrivateFrameworks/MailCore.framework/Versions/A/MailCore`

```diff

-3897.100.8.1.1
-  __TEXT.__text: 0x84cc8
-  __TEXT.__objc_methlist: 0x819c
-  __TEXT.__cstring: 0x7fc8
+3901.100.1.1.11
+  __TEXT.__text: 0x84f90
+  __TEXT.__objc_methlist: 0x81b4
+  __TEXT.__cstring: 0x801e
   __TEXT.__gcc_except_tab: 0x1684
   __TEXT.__const: 0x4b0
   __TEXT.__oslogstring: 0x1e68

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1210
+  __DATA_CONST.__const: 0x1220
   __DATA_CONST.__objc_classlist: 0x370
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5418
+  __DATA_CONST.__objc_selrefs: 0x5430
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x288
   __DATA_CONST.__objc_arraydata: 0x1b0
   __DATA_CONST.__got: 0x1100
   __AUTH_CONST.__const: 0x1350
-  __AUTH_CONST.__cfstring: 0x9180
+  __AUTH_CONST.__cfstring: 0x91c0
   __AUTH_CONST.__objc_const: 0xcc70
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0xa8

   __DATA.__objc_ivar: 0x7a8
   __DATA.__data: 0xda8
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x1f2
+  __DATA.__bss: 0x1fa
   __DATA_DIRTY.__objc_data: 0x1720
-  __DATA_DIRTY.__bss: 0x410
+  __DATA_DIRTY.__bss: 0x408
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AddressBook.framework/Versions/A/AddressBook
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2882
-  Symbols:   7604
-  CStrings:  1472
+  Functions: 2884
+  Symbols:   7612
+  CStrings:  1474
 
Symbols:
+ -[MCMimePart _parseSubpartsFromBodyData:boundary:encodingHint:hasVisualEncoding:depth:]
+ -[MCMimePart _searchMIMEBoundaryFromBodyData:]
+ GCC_except_table147
+ GCC_except_table164
+ _MCProgressManagerProgressEntryDidFinishNotification
+ _MCProgressManagerProgressSliceKey
+ ___46-[MCMimePart _searchMIMEBoundaryFromBodyData:]_block_invoke
+ ___87-[MCMimePart _parseSubpartsFromBodyData:boundary:encodingHint:hasVisualEncoding:depth:]_block_invoke
+ _objc_msgSend$URLByDeletingLastPathComponent
+ _objc_msgSend$_parseSubpartsFromBodyData:boundary:encodingHint:hasVisualEncoding:depth:
+ _objc_msgSend$_searchMIMEBoundaryFromBodyData:
+ _parseSubpartsFromBodyData:boundary:encodingHint:hasVisualEncoding:depth:.onceToken
+ _parseSubpartsFromBodyData:boundary:encodingHint:hasVisualEncoding:depth:.separator
+ _searchMIMEBoundaryFromBodyData:.mimeBoundaryRegularExpression
+ _searchMIMEBoundaryFromBodyData:.onceToken
- GCC_except_table145
- GCC_except_table162
- ___69-[MCMimePart _parseSubpartsWithEncodingHint:hasVisualEncoding:depth:]_block_invoke
- ___69-[MCMimePart _parseSubpartsWithEncodingHint:hasVisualEncoding:depth:]_block_invoke_2
- _parseSubpartsWithEncodingHint:hasVisualEncoding:depth:.mimeBoundaryRegularExpression
- _parseSubpartsWithEncodingHint:hasVisualEncoding:depth:.onceToken
- _parseSubpartsWithEncodingHint:hasVisualEncoding:depth:.separator
CStrings:
+ "MCProgressManagerProgressEntryDidFinishNotification"
+ "MCProgressManagerProgressSliceKey"
```
