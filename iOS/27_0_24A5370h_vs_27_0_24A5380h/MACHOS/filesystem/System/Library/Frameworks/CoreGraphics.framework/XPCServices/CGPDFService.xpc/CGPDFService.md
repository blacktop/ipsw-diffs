## CGPDFService

> `/System/Library/Frameworks/CoreGraphics.framework/XPCServices/CGPDFService.xpc/CGPDFService`

```diff

-  __TEXT.__text: 0x22cc
-  __TEXT.__auth_stubs: 0x420
-  __TEXT.__objc_stubs: 0x2e0
-  __TEXT.__objc_methlist: 0x364
-  __TEXT.__const: 0x58
-  __TEXT.__objc_methname: 0x47b
-  __TEXT.__cstring: 0x34e
+  __TEXT.__text: 0x26d0
+  __TEXT.__auth_stubs: 0x460
+  __TEXT.__objc_stubs: 0x320
+  __TEXT.__objc_methlist: 0x374
+  __TEXT.__const: 0x70
+  __TEXT.__cstring: 0x408
+  __TEXT.__objc_methname: 0x4e8
   __TEXT.__objc_classname: 0xb0
-  __TEXT.__objc_methtype: 0x42f
-  __TEXT.__gcc_except_tab: 0x4a8
+  __TEXT.__objc_methtype: 0x475
+  __TEXT.__gcc_except_tab: 0x52c
   __TEXT.__oslogstring: 0x25
-  __TEXT.__unwind_info: 0x230
-  __DATA_CONST.__const: 0x130
-  __DATA_CONST.__cfstring: 0x80
+  __TEXT.__unwind_info: 0x250
+  __DATA_CONST.__const: 0x170
+  __DATA_CONST.__cfstring: 0xc0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__auth_got: 0x220
-  __DATA_CONST.__got: 0x88
-  __DATA.__objc_const: 0x6c0
-  __DATA.__objc_selrefs: 0x1e8
+  __DATA_CONST.__auth_got: 0x240
+  __DATA_CONST.__got: 0xb0
+  __DATA.__objc_const: 0x6c8
+  __DATA.__objc_selrefs: 0x200
   __DATA.__objc_ivar: 0x24
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x1e0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 56
-  Symbols:   279
-  CStrings:  154
+  Functions: 60
+  Symbols:   300
+  CStrings:  164
 
Sections:
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ -[CGPDFService newPDFDocumentWithData:withReplyOrError:]
+ GCC_except_table17
+ GCC_except_table22
+ _NSDebugDescriptionErrorKey
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSError
+ __ZN21CGPDFServiceExceptionD0Ev
+ __ZN21CGPDFServiceExceptionD1Ev
+ __ZNKSt9exception4whatEv
+ __ZNSt9exceptionD2Ev
+ __ZTI21CGPDFServiceException
+ __ZTS21CGPDFServiceException
+ __ZTV21CGPDFServiceException
+ __ZTVN10__cxxabiv120__si_class_type_infoE
+ __ZdlPvSt19__type_descriptor_t
+ ___56-[CGPDFService newPDFDocumentWithData:withReplyOrError:]_block_invoke
+ ___stack_chk_fail
+ ___stack_chk_guard
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_release_x22
- GCC_except_table20
- GCC_except_table3
- GCC_except_table6
CStrings:
+ "%s caught CGPDFServiceException: code=%ld"
+ "-[CGPDFService newPDFDocumentWithData:withReplyOrError:]_block_invoke"
+ "CGPDFServiceErrorDataProviderCreationFailed"
+ "CGPDFServiceErrorInvalidPDFData"
+ "CGPDFServiceErrorUnknown"
+ "com.apple.CoreGraphics.CGPDFService"
+ "dictionaryWithObjects:forKeys:count:"
+ "errorWithDomain:code:userInfo:"
+ "newPDFDocumentWithData:withReplyOrError:"
+ "v32@0:8@\"NSData\"16@?<v@?@\"<CGRemotePDFDocumentProtocol>\"@\"NSError\">24"
- "Failed to create CGDataProvoder"
- "Failed to create CGPDFDocument"

```
