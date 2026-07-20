## VideosUICore

> `/System/Library/PrivateFrameworks/VideosUICore.framework/VideosUICore`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-1145.0.2.0.1
-  __TEXT.__text: 0x35308
-  __TEXT.__objc_methlist: 0x560c
+1145.0.6.0.0
+  __TEXT.__text: 0x353f0
+  __TEXT.__objc_methlist: 0x5664
   __TEXT.__const: 0x546
   __TEXT.__cstring: 0x3435
   __TEXT.__oslogstring: 0x165b

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1ed0
+  __DATA_CONST.__const: 0x1ef8
   __DATA_CONST.__objc_classlist: 0x238
   __DATA_CONST.__objc_catlist: 0x128
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3c70
+  __DATA_CONST.__objc_selrefs: 0x3c98
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x1a8
   __DATA_CONST.__got: 0x650
   __AUTH_CONST.__const: 0x6e0
   __AUTH_CONST.__cfstring: 0x6260
-  __AUTH_CONST.__objc_const: 0x8658
+  __AUTH_CONST.__objc_const: 0x8688
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_doubleobj: 0xc0
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x780
   __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0x55c
+  __DATA.__objc_ivar: 0x560
   __DATA.__data: 0x8f8
   __DATA.__bss: 0xd1
   __DATA_DIRTY.__objc_data: 0xe60

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1873
-  Symbols:   4937
+  Functions: 1880
+  Symbols:   4949
   CStrings:  952
 
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
+ ___block_descriptor_89_e8_32s40s48s56w_e5_v8?0lw56l8s32l8s40l8s48l8
+ _objc_msgSend$_imageProxyWithURL:impressionIDWrapper:
+ _objc_msgSend$impressionIDWrapper
+ _objc_msgSend$initWithObject:imageLoader:groupType:impressionIDWrapper:
+ _objc_msgSend$makeImageProxyWithDescriptor:impressionIDWrapper:
+ _objc_msgSend$makeImageViewWithDescriptor:imageProxy:existingView:impressionIDWrapper:
+ _objc_msgSend$setImpressionIDWrapper:
- GCC_except_table24
- GCC_except_table28
- _objc_msgSend$_imageProxyWithURL:
- _objc_msgSend$makeImageProxyWithDescriptor:
```
