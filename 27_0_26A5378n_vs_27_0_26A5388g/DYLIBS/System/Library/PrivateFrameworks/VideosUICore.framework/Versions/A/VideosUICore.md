## VideosUICore

> `/System/Library/PrivateFrameworks/VideosUICore.framework/Versions/A/VideosUICore`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-1145.0.2.0.1
-  __TEXT.__text: 0x36d84
-  __TEXT.__objc_methlist: 0x5894
+1145.0.6.0.0
+  __TEXT.__text: 0x36c14
+  __TEXT.__objc_methlist: 0x58f4
   __TEXT.__const: 0x4e6
   __TEXT.__cstring: 0x3509
   __TEXT.__oslogstring: 0x121c

   __TEXT.__swift5_typeref: 0x6
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x10c8
+  __TEXT.__unwind_info: 0x10c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x108
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3bc0
+  __DATA_CONST.__objc_selrefs: 0x3bf8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__got: 0x6d0
-  __AUTH_CONST.__const: 0x1180
+  __AUTH_CONST.__const: 0x1150
   __AUTH_CONST.__cfstring: 0x6300
-  __AUTH_CONST.__objc_const: 0x9118
+  __AUTH_CONST.__objc_const: 0x9148
   __AUTH_CONST.__objc_intobj: 0x2e8
   __AUTH_CONST.__objc_doubleobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xbe0
   __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0x5dc
+  __DATA.__objc_ivar: 0x5e0
   __DATA.__data: 0x768
   __DATA.__bss: 0x91
   __DATA_DIRTY.__objc_data: 0xdc0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1956
-  Symbols:   4983
+  Functions: 1963
+  Symbols:   4993
   CStrings:  927
 
Symbols:
+ +[VUIImageFactory _imageProxyWithURL:impressionIDWrapper:]
+ +[VUIImageFactory makeImageProxyWithDescriptor:impressionIDWrapper:]
+ +[VUIImageFactory makeImageViewWithDescriptor:existingView:impressionIDWrapper:]
+ +[VUIImageFactory makeImageViewWithDescriptor:imageProxy:existingView:impressionIDWrapper:]
+ -[VUIImageProxy initWithObject:imageLoader:groupType:impressionIDWrapper:]
+ -[VUINSNavigationController _postFlowForPush:]
+ -[VUINSNavigationController _preFlowForPop]
+ -[VUINSNavigationController _preFlowForPush:animated:]
+ -[VUINSNavigationController lastNavigationAction]
+ -[VUINSNavigationController sendDidHideViewController:animated:]
+ -[VUINSNavigationController sendDidShowViewController:animated:]
+ -[VUINSNavigationController sendWillHideViewController:animated:]
+ -[VUINSNavigationController sendWillShowViewController:animated:]
+ -[VUINSNavigationController setLastNavigationAction:]
+ GCC_except_table31
+ OBJC_IVAR_$_VUINSNavigationController._lastNavigationAction
+ _objc_msgSend$_imageProxyWithURL:impressionIDWrapper:
+ _objc_msgSend$_postFlowForPush:
+ _objc_msgSend$_preFlowForPop
+ _objc_msgSend$_preFlowForPush:animated:
+ _objc_msgSend$impressionIDWrapper
+ _objc_msgSend$initWithObject:imageLoader:groupType:impressionIDWrapper:
+ _objc_msgSend$lastNavigationAction
+ _objc_msgSend$makeImageProxyWithDescriptor:impressionIDWrapper:
+ _objc_msgSend$makeImageViewWithDescriptor:imageProxy:existingView:impressionIDWrapper:
+ _objc_msgSend$setImpressionIDWrapper:
+ _objc_msgSend$setLastNavigationAction:
- -[VUINSNavigationController _finishLocalPopForController:]
- -[VUINSNavigationController _finishPopForController:]
- -[VUINSNavigationController _finishPopForController:animated:]
- -[VUINSNavigationController _finishPushForController:animated:]
- -[VUINSNavigationController _transitionFromViewController:toViewController:action:animated:completionHandler:]
- -[VUINoClickThroughView mouseDown:]
- GCC_except_table30
- GCC_except_table40
- ___110-[VUINSNavigationController _transitionFromViewController:toViewController:action:animated:completionHandler:]_block_invoke
- ___block_descriptor_58_e8_32s40s48bs_e5_v8?0l
- _objc_msgSend$_finishLocalPopForController:
- _objc_msgSend$_imageProxyWithURL:
- _objc_msgSend$isVisible
- _objc_msgSend$makeImageProxyWithDescriptor:
- _objc_msgSend$prepareForReuse
- _objc_msgSend$setVuiAlpha:
- _objc_msgSend$vui_layoutIfNeeded
```
