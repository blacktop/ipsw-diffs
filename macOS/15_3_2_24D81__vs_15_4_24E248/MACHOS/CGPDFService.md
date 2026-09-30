## CGPDFService

> `/System/Library/Frameworks/CoreGraphics.framework/Versions/A/XPCServices/CGPDFService.xpc/Contents/MacOS/CGPDFService`

```diff

-1889.3.2.0.0
-  __TEXT.__text: 0x2328
-  __TEXT.__auth_stubs: 0x3e0
-  __TEXT.__objc_stubs: 0x2a0
-  __TEXT.__objc_methlist: 0x198
-  __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x11a
-  __TEXT.__oslogstring: 0x190
-  __TEXT.__gcc_except_tab: 0x24c
-  __TEXT.__objc_methname: 0x44d
+1889.4.8.0.0
+  __TEXT.__text: 0x2c98
+  __TEXT.__auth_stubs: 0x440
+  __TEXT.__objc_stubs: 0x2e0
+  __TEXT.__objc_methlist: 0x364
+  __TEXT.__const: 0x68
+  __TEXT.__cstring: 0x3a9
+  __TEXT.__oslogstring: 0x1b5
+  __TEXT.__gcc_except_tab: 0x4a8
+  __TEXT.__objc_methname: 0x47b
   __TEXT.__objc_classname: 0xb4
   __TEXT.__objc_methtype: 0x487
-  __TEXT.__unwind_info: 0x210
-  __DATA_CONST.__auth_got: 0x200
-  __DATA_CONST.__got: 0x80
-  __DATA_CONST.__const: 0xf0
+  __TEXT.__unwind_info: 0x278
+  __DATA_CONST.__auth_got: 0x230
+  __DATA_CONST.__got: 0x98
+  __DATA_CONST.__const: 0x130
   __DATA_CONST.__cfstring: 0x80
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA.__objc_const: 0xa08
-  __DATA.__objc_selrefs: 0x138
+  __DATA.__objc_const: 0x6c0
+  __DATA.__objc_selrefs: 0x1e8
   __DATA.__objc_ivar: 0x24
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x1e0
+  __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0CDA14C6-BBBC-3341-B124-4179BCF04470
-  Functions: 74
-  Symbols:   276
-  CStrings:  149
+  UUID: A6602FA9-C501-3C04-B658-39BABF3CFCA0
+  Functions: 77
+  Symbols:   305
+  CStrings:  167
 
Symbols:
+ _CGRectZero
+ _OBJC_CLASS_$_NSString
+ _PDFLog.cold.1
+ _PDFLog.onceToken
+ __NSConcreteGlobalBlock
+ __PDFLog
+ __ZNKSt3__16vectorIU8__strongP13CGPDFPageImplNS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIU8__strongP13CGPDFPageImplEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__16vectorIU8__strongP13CGPDFPageImplNS_9allocatorIS3_EEE16__destroy_vectorclB8ne190102Ev
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ __ZTISt9exception
+ ____PDFLog_block_invoke
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_56_ea8_32s40s48bs_e5_v8?0l
+ ___block_literal_global
+ ___copy_helper_block_ea8_32s40s48b
+ ___cxa_end_catch
+ ___destroy_helper_block_ea8_32s40s48s
+ __os_log_impl
+ _dispatch_once
+ _getprogname
+ _memcpy
+ _objc_msgSend$initWithFormat:arguments:
+ _objc_msgSend$initWithUTF8String:
+ _os_log_create
+ _sLog
- GCC_except_table8
- __ZNKSt3__16vectorIU8__strongP13CGPDFPageImplNS_9allocatorIS3_EEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIU8__strongP13CGPDFPageImplEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__16vectorIU8__strongP13CGPDFPageImplNS_9allocatorIS3_EEE16__destroy_vectorclB8ne180100Ev
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- ___block_descriptor_56_e8_32s40s48bs_e5_v8?0l
- ___copy_helper_block_e8_32s40s48b
- ___destroy_helper_block_e8_32s40s48s
CStrings:
+ "%s caught an unknown exception"
+ "%s caught exception: %s"
+ "%{public}20s | %{public}@"
+ "%{public}@"
+ "-[CGPDFDocumentImpl getInfo:]_block_invoke"
+ "-[CGPDFDocumentImpl getIsEncrypted:]_block_invoke"
+ "-[CGPDFDocumentImpl getIsUnlocked:]_block_invoke"
+ "-[CGPDFDocumentImpl getPageAtIndex:completion:]_block_invoke"
+ "-[CGPDFDocumentImpl getPageCount:]_block_invoke"
+ "-[CGPDFDocumentImpl getVersion:]_block_invoke"
+ "-[CGPDFPageImpl drawWithBox:size:colorSpace:options:completion:]_block_invoke"
+ "-[CGPDFPageImpl getBoxRect:completion:]_block_invoke"
+ "-[CGPDFPageImpl getPageText:]_block_invoke"
+ "-[CGPDFPageImpl getRotation:]_block_invoke"
+ "-[CGPDFService newPDFDocumentWithData:withReply:]_block_invoke"
+ "com.apple.CGPDFService"
+ "initWithFormat:arguments:"
+ "initWithUTF8String:"

```
