## Silex

> `/System/Library/PrivateFrameworks/Silex.framework/Silex`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-5926.0.0.0.0
-  __TEXT.__text: 0x1188f0
-  __TEXT.__objc_methlist: 0x1e6bc
+5934.2.0.0.0
+  __TEXT.__text: 0x118cf8
+  __TEXT.__objc_methlist: 0x1e6fc
   __TEXT.__const: 0x5bc
   __TEXT.__cstring: 0xa09c
   __TEXT.__gcc_except_tab: 0x2498
   __TEXT.__oslogstring: 0x293c
   __TEXT.__ustring: 0x74
-  __TEXT.__unwind_info: 0x4f28
+  __TEXT.__unwind_info: 0x4f20
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0xc8
   __DATA_CONST.__objc_protolist: 0xd30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb830
+  __DATA_CONST.__objc_selrefs: 0xb858
   __DATA_CONST.__objc_protorefs: 0x598
   __DATA_CONST.__objc_superrefs: 0x1038
   __DATA_CONST.__objc_arraydata: 0x3cc8
   __DATA_CONST.__got: 0x2590
   __AUTH_CONST.__const: 0x3c80
   __AUTH_CONST.__cfstring: 0x98e0
-  __AUTH_CONST.__objc_const: 0x51c78
+  __AUTH_CONST.__objc_const: 0x51c90
   __AUTH_CONST.__objc_intobj: 0x3d8
   __AUTH_CONST.__objc_arrayobj: 0x300
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x2aa8
-  __AUTH_CONST.__auth_got: 0x7c8
+  __AUTH_CONST.__auth_got: 0x7d0
   __AUTH.__objc_data: 0x2f58
   __DATA.__objc_ivar: 0x1fac
   __DATA.__data: 0x9f58

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8569
-  Symbols:   25278
+  Functions: 8573
+  Symbols:   25288
   CStrings:  1844
 
Symbols:
+ +[SXEmbedComponentView installUserScriptsIntoContentController:userScript:]
+ +[SXEmbedComponentView resetUserScriptsInContentController:userScript:]
+ -[SXScrollViewController dismissPresentedFullscreenCanvas]
+ -[TSDCanvasView(SXAccessibility) _sxaxCollectImageViewsInView:intoArray:]
+ _OBJC_CLASS_$_NSTextAttachment
+ _UIAccessibilityConvertAttachmentsInAttributedStringToAX
+ __OBJC_$_CLASS_METHODS_SXEmbedComponentView
+ _objc_msgSend$_sxaxCollectImageViewsInView:intoArray:
+ _objc_msgSend$attributedStringWithAttachment:
+ _objc_msgSend$installUserScriptsIntoContentController:userScript:
+ _objc_msgSend$removeAllUserScripts
+ _objc_msgSend$resetUserScriptsInContentController:userScript:
- _OBJC_CLASS_$_AXAttributedString
- _objc_msgSend$initWithStringOrAttributedString:
CStrings:
+ "1.32"
- "1.31"
```
