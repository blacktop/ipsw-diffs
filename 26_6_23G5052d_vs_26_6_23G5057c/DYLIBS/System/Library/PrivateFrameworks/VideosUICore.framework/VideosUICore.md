## VideosUICore

> `/System/Library/PrivateFrameworks/VideosUICore.framework/VideosUICore`

```diff

-  __TEXT.__text: 0x30ff0
+  __TEXT.__text: 0x31030
   __TEXT.__auth_stubs: 0xbc0
-  __TEXT.__objc_methlist: 0x4ea4
+  __TEXT.__objc_methlist: 0x4efc
   __TEXT.__const: 0x1e0
-  __TEXT.__cstring: 0x2de5
+  __TEXT.__cstring: 0x2dd7
   __TEXT.__oslogstring: 0xda7
-  __TEXT.__gcc_except_tab: 0x7d8
+  __TEXT.__gcc_except_tab: 0x7c0
   __TEXT.__ustring: 0x6a
-  __TEXT.__unwind_info: 0x1128
+  __TEXT.__unwind_info: 0x1140
   __TEXT.__objc_classname: 0x8e3
-  __TEXT.__objc_methname: 0xda53
-  __TEXT.__objc_methtype: 0x22fe
-  __TEXT.__objc_stubs: 0x89c0
+  __TEXT.__objc_methname: 0xdb6e
+  __TEXT.__objc_methtype: 0x2312
+  __TEXT.__objc_stubs: 0x8a20
   __DATA_CONST.__got: 0x5d8
   __DATA_CONST.__const: 0x1ba8
   __DATA_CONST.__objc_classlist: 0x230
   __DATA_CONST.__objc_catlist: 0xb0
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x34b8
+  __DATA_CONST.__objc_selrefs: 0x34e0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x198
   __AUTH_CONST.__auth_got: 0x5f0
   __AUTH_CONST.__const: 0x580
-  __AUTH_CONST.__cfstring: 0x59e0
-  __AUTH_CONST.__objc_const: 0x7f30
+  __AUTH_CONST.__cfstring: 0x59c0
+  __AUTH_CONST.__objc_const: 0x7f60
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_doubleobj: 0xc0
   __AUTH.__objc_data: 0x780
-  __DATA.__objc_ivar: 0x53c
+  __DATA.__objc_ivar: 0x540
   __DATA.__data: 0x858
   __DATA.__bss: 0x90
   __DATA_DIRTY.__objc_data: 0xe60

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1685
-  Symbols:   6195
-  CStrings:  4277
+  Functions: 1692
+  Symbols:   6213
+  CStrings:  4281
 
Sections:
~ __TEXT.__objc_classname : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ +[VUIImageFactory _imageProxyWithURL:impressionIDWrapper:]
+ +[VUIImageFactory makeImageProxyWithDescriptor:impressionIDWrapper:]
+ +[VUIImageFactory makeImageViewWithDescriptor:existingView:impressionIDWrapper:]
+ +[VUIImageFactory makeImageViewWithDescriptor:imageProxy:existingView:impressionIDWrapper:]
+ -[VUIImageProxy initWithObject:imageLoader:groupType:impressionIDWrapper:]
+ -[VUILayeredImageProxy impressionIDWrapper]
+ -[VUILayeredImageProxy setImpressionIDWrapper:]
+ GCC_except_table14
+ _OBJC_IVAR_$_VUILayeredImageProxy._impressionIDWrapper
+ _objc_msgSend$_imageProxyWithURL:impressionIDWrapper:
+ _objc_msgSend$impressionIDWrapper
+ _objc_msgSend$initWithObject:imageLoader:groupType:impressionIDWrapper:
+ _objc_msgSend$makeImageProxyWithDescriptor:impressionIDWrapper:
+ _objc_msgSend$makeImageViewWithDescriptor:imageProxy:existingView:impressionIDWrapper:
+ _objc_msgSend$setImpressionIDWrapper:
- GCC_except_table24
- GCC_except_table28
- _objc_msgSend$URLForObject:
- _objc_msgSend$_imageProxyWithURL:
- _objc_msgSend$makeImageProxyWithDescriptor:
CStrings:
+ "@48@0:8@16@24q32@40"
+ "_imageProxyWithURL:impressionIDWrapper:"
+ "initWithObject:imageLoader:groupType:impressionIDWrapper:"
+ "makeImageProxyWithDescriptor:impressionIDWrapper:"
+ "makeImageViewWithDescriptor:existingView:impressionIDWrapper:"
+ "makeImageViewWithDescriptor:imageProxy:existingView:impressionIDWrapper:"
- "imageKey://%@"

```
