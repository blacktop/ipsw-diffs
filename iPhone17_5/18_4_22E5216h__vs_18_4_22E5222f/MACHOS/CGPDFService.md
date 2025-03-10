## CGPDFService

> `/System/Library/Frameworks/CoreGraphics.framework/XPCServices/CGPDFService.xpc/CGPDFService`

```diff

-1889.4.4.0.0
-  __TEXT.__text: 0x1a14
-  __TEXT.__auth_stubs: 0x3d0
-  __TEXT.__objc_stubs: 0x2a0
+1889.4.8.0.0
+  __TEXT.__text: 0x2370
+  __TEXT.__auth_stubs: 0x450
+  __TEXT.__objc_stubs: 0x2e0
   __TEXT.__objc_methlist: 0x364
-  __TEXT.__const: 0x48
-  __TEXT.__gcc_except_tab: 0x248
-  __TEXT.__objc_methname: 0x44d
-  __TEXT.__cstring: 0xbb
+  __TEXT.__const: 0x58
+  __TEXT.__gcc_except_tab: 0x4a0
+  __TEXT.__objc_methname: 0x47b
+  __TEXT.__cstring: 0x34a
   __TEXT.__objc_classname: 0xb4
   __TEXT.__objc_methtype: 0x487
-  __TEXT.__unwind_info: 0x1f8
-  __DATA_CONST.__auth_got: 0x1f8
-  __DATA_CONST.__got: 0x70
-  __DATA_CONST.__const: 0xf0
+  __TEXT.__oslogstring: 0x25
+  __TEXT.__unwind_info: 0x258
+  __DATA_CONST.__auth_got: 0x238
+  __DATA_CONST.__got: 0x90
+  __DATA_CONST.__const: 0x130
   __DATA_CONST.__cfstring: 0x80
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA.__objc_const: 0x6c0
-  __DATA.__objc_selrefs: 0x1d8
+  __DATA.__objc_selrefs: 0x1e8
   __DATA.__objc_ivar: 0x24
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x1e0
+  __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 57
-  Symbols:   257
-  CStrings:  134
+  Functions: 60
+  Symbols:   289
+  CStrings:  152
 
Symbols:
+ GCC_except_table17
+ _CGRectZero
+ _OBJC_CLASS_$_NSString
+ _PDFLog.cold.1
+ _PDFLog.onceToken
+ __NSConcreteGlobalBlock
+ __PDFLog
+ __ZTISt9exception
+ ____PDFLog_block_invoke
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_52_ea8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_ea8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_ea8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global
+ ___cxa_end_catch
+ ___stack_chk_fail
+ ___stack_chk_guard
+ __os_log_impl
+ _dispatch_once
+ _getprogname
+ _objc_msgSend$initWithFormat:arguments:
+ _objc_msgSend$initWithUTF8String:
+ _objc_release_x1
+ _os_log_create
+ _os_log_type_enabled
+ _sLog
- GCC_except_table6
- ___block_descriptor_52_ea8_32s40bs_e5_v8?0ls40l8s32l8
- ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_56_ea8_32s40bs_e5_v8?0ls40l8s32l8
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
