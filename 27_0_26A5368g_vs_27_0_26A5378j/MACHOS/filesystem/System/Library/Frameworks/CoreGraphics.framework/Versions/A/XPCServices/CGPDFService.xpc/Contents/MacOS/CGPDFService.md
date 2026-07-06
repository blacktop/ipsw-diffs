## CGPDFService

> `/System/Library/Frameworks/CoreGraphics.framework/Versions/A/XPCServices/CGPDFService.xpc/Contents/MacOS/CGPDFService`

```diff

-  __TEXT.__text: 0x2acc
-  __TEXT.__auth_stubs: 0x430
-  __TEXT.__objc_stubs: 0x2e0
-  __TEXT.__objc_methlist: 0x364
-  __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x38f
+  __TEXT.__text: 0x2ec0
+  __TEXT.__auth_stubs: 0x450
+  __TEXT.__objc_stubs: 0x320
+  __TEXT.__objc_methlist: 0x374
+  __TEXT.__const: 0x80
+  __TEXT.__cstring: 0x425
   __TEXT.__oslogstring: 0x1b5
-  __TEXT.__objc_methname: 0x47b
+  __TEXT.__objc_methname: 0x4e8
   __TEXT.__objc_classname: 0xb0
-  __TEXT.__objc_methtype: 0x42f
-  __TEXT.__gcc_except_tab: 0x4c0
-  __TEXT.__unwind_info: 0x278
-  __DATA_CONST.__const: 0x130
-  __DATA_CONST.__cfstring: 0x80
+  __TEXT.__objc_methtype: 0x475
+  __TEXT.__gcc_except_tab: 0x540
+  __TEXT.__unwind_info: 0x298
+  __DATA_CONST.__const: 0x170
+  __DATA_CONST.__cfstring: 0xc0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__auth_got: 0x228
-  __DATA_CONST.__got: 0x98
-  __DATA.__objc_const: 0x6c0
-  __DATA.__objc_selrefs: 0x1e8
+  __DATA_CONST.__auth_got: 0x238
+  __DATA_CONST.__got: 0xb8
+  __DATA.__objc_const: 0x6c8
+  __DATA.__objc_selrefs: 0x200
   __DATA.__objc_ivar: 0x24
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x1e0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 78
-  Symbols:   306
-  CStrings:  166
+  Functions: 82
+  Symbols:   324
+  CStrings:  175
 
Sections:
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ -[CGPDFService newPDFDocumentWithData:withReplyOrError:]
+ GCC_except_table19
+ GCC_except_table24
+ GCC_except_table30
+ GCC_except_table6
+ GCC_except_table7
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
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$errorWithDomain:code:userInfo:
- GCC_except_table22
- GCC_except_table28
- GCC_except_table3
- GCC_except_table8
CStrings:
+ "%s caught CGPDFServiceException: code=%ld"
+ "-[CGPDFService newPDFDocumentWithData:withReplyOrError:]_block_invoke"
+ "CGPDFServiceErrorDataProviderCreationFailed"
+ "CGPDFServiceErrorInvalidPDFData"
+ "CGPDFServiceErrorUnknown"
+ "dictionaryWithObjects:forKeys:count:"
+ "errorWithDomain:code:userInfo:"
+ "newPDFDocumentWithData:withReplyOrError:"
+ "v32@0:8@\"NSData\"16@?<v@?@\"<CGRemotePDFDocumentProtocol>\"@\"NSError\">24"
- "Failed to create CGDataProvoder"
- "Failed to create CGPDFDocument"

```
