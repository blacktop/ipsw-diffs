## VideosUICore

> `/System/Library/PrivateFrameworks/VideosUICore.framework/Versions/A/VideosUICore`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-1061.60.14.0.0
-  __TEXT.__text: 0x35630
+1061.60.17.0.0
+  __TEXT.__text: 0x35634
   __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__objc_methlist: 0x5334
+  __TEXT.__objc_methlist: 0x536c
   __TEXT.__const: 0x1a0
-  __TEXT.__cstring: 0x2f6a
+  __TEXT.__cstring: 0x2f5c
   __TEXT.__oslogstring: 0xc4b
-  __TEXT.__gcc_except_tab: 0x684
+  __TEXT.__gcc_except_tab: 0x66c
   __TEXT.__ustring: 0x6a
   __TEXT.__unwind_info: 0x11a8
   __TEXT.__objc_classname: 0x9e1
-  __TEXT.__objc_methname: 0xe0e9
-  __TEXT.__objc_methtype: 0x1c20
-  __TEXT.__objc_stubs: 0x8920
+  __TEXT.__objc_methname: 0xe204
+  __TEXT.__objc_methtype: 0x1c34
+  __TEXT.__objc_stubs: 0x8980
   __DATA_CONST.__got: 0x670
   __DATA_CONST.__const: 0xeb8
   __DATA_CONST.__objc_classlist: 0x290
   __DATA_CONST.__objc_catlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3680
+  __DATA_CONST.__objc_selrefs: 0x36a8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1c8
   __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__auth_got: 0x470
   __AUTH_CONST.__const: 0x10a0
-  __AUTH_CONST.__cfstring: 0x5aa0
+  __AUTH_CONST.__cfstring: 0x5a80
   __AUTH_CONST.__objc_const: 0x8b18
   __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH_CONST.__objc_doubleobj: 0xc0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1828
-  Symbols:   4589
-  CStrings:  3603
+  Functions: 1833
+  Symbols:   4596
+  CStrings:  3608
 
Symbols:
+ +[VUIImageFactory _imageProxyWithURL:impressionIDWrapper:]
+ +[VUIImageFactory makeImageProxyWithDescriptor:impressionIDWrapper:]
+ +[VUIImageFactory makeImageViewWithDescriptor:existingView:impressionIDWrapper:]
+ +[VUIImageFactory makeImageViewWithDescriptor:imageProxy:existingView:impressionIDWrapper:]
+ -[VUIImageProxy initWithObject:imageLoader:groupType:impressionIDWrapper:]
+ GCC_except_table31
+ _objc_msgSend$_imageProxyWithURL:impressionIDWrapper:
+ _objc_msgSend$impressionIDWrapper
+ _objc_msgSend$initWithObject:imageLoader:groupType:impressionIDWrapper:
+ _objc_msgSend$makeImageProxyWithDescriptor:impressionIDWrapper:
+ _objc_msgSend$makeImageViewWithDescriptor:imageProxy:existingView:impressionIDWrapper:
+ _objc_msgSend$setImpressionIDWrapper:
- GCC_except_table30
- GCC_except_table40
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
