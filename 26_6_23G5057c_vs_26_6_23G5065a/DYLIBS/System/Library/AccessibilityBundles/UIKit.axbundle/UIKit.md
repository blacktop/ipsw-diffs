## UIKit

> `/System/Library/AccessibilityBundles/UIKit.axbundle/UIKit`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-  __TEXT.__text: 0x19a2e4
+  __TEXT.__text: 0x19aa94
   __TEXT.__auth_stubs: 0x1520
-  __TEXT.__objc_methlist: 0xfadc
+  __TEXT.__objc_methlist: 0xfb24
   __TEXT.__const: 0xa0
   __TEXT.__cstring: 0x1959c
   __TEXT.__oslogstring: 0x2494
   __TEXT.__gcc_except_tab: 0x36f0
   __TEXT.__dlopen_cstrs: 0xb8
   __TEXT.__ustring: 0x78
-  __TEXT.__unwind_info: 0x2d70
-  __TEXT.__objc_classname: 0x9286
-  __TEXT.__objc_methname: 0x16277
-  __TEXT.__objc_methtype: 0x2160
-  __TEXT.__objc_stubs: 0x108c0
-  __DATA_CONST.__got: 0xfa8
+  __TEXT.__unwind_info: 0x2d80
+  __TEXT.__objc_classname: 0x92a0
+  __TEXT.__objc_methname: 0x16317
+  __TEXT.__objc_methtype: 0x2175
+  __TEXT.__objc_stubs: 0x10940
+  __DATA_CONST.__got: 0xfb0
   __DATA_CONST.__const: 0x1ea8
-  __DATA_CONST.__objc_classlist: 0x1b88
+  __DATA_CONST.__objc_classlist: 0x1b90
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5c68
+  __DATA_CONST.__objc_selrefs: 0x5c88
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0xa90
-  __DATA_CONST.__objc_arraydata: 0x190
+  __DATA_CONST.__objc_superrefs: 0xa98
+  __DATA_CONST.__objc_arraydata: 0x160
   __AUTH_CONST.__auth_got: 0xaa0
-  __AUTH_CONST.__const: 0x17a0
+  __AUTH_CONST.__const: 0x17c0
   __AUTH_CONST.__cfstring: 0x1e200
-  __AUTH_CONST.__objc_const: 0x209c0
+  __AUTH_CONST.__objc_const: 0x20af0
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0x140
-  __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH.__objc_data: 0x1f90
-  __DATA.__objc_ivar: 0x114
+  __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH.__objc_data: 0x1fe0
+  __DATA.__objc_ivar: 0x120
   __DATA.__data: 0x6b8
-  __DATA.__bss: 0x3fe
+  __DATA.__bss: 0x416
   __DATA_DIRTY.__objc_data: 0xf3c0
   __DATA_DIRTY.__common: 0x8
   __DATA_DIRTY.__bss: 0x1e8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5916
-  Symbols:   13852
-  CStrings:  7423
+  Functions: 5924
+  Symbols:   13875
+  CStrings:  7434
 
Symbols:
+ -[_AXBarButtonReferenceIcon .cxx_destruct]
+ -[_AXBarButtonReferenceIcon identifier]
+ -[_AXBarButtonReferenceIcon image]
+ -[_AXBarButtonReferenceIcon initWithIdentifier:kitImageName:]
+ -[_AXBarButtonReferenceIcon pngRep]
+ _OBJC_CLASS_$__AXBarButtonReferenceIcon
+ _OBJC_IVAR_$__AXBarButtonReferenceIcon._identifier
+ _OBJC_IVAR_$__AXBarButtonReferenceIcon._image
+ _OBJC_IVAR_$__AXBarButtonReferenceIcon._pngRep
+ _OBJC_METACLASS_$__AXBarButtonReferenceIcon
+ __AXBarButtonReferenceIcons
+ __AXBarButtonReferenceIcons.icons
+ __AXBarButtonReferenceIcons.once
+ __OBJC_$_INSTANCE_METHODS__AXBarButtonReferenceIcon
+ __OBJC_$_INSTANCE_VARIABLES__AXBarButtonReferenceIcon
+ __OBJC_$_PROP_LIST__AXBarButtonReferenceIcon
+ __OBJC_CLASS_RO_$__AXBarButtonReferenceIcon
+ __OBJC_METACLASS_RO_$__AXBarButtonReferenceIcon
+ ____AXBarButtonReferenceIcons_block_invoke
+ _objc_msgSend$initWithIdentifier:kitImageName:
+ _objc_msgSend$pngRep
+ _objc_msgSend$scale
+ _objc_msgSend$size
CStrings:
+ "@\"NSData\""
+ "@\"UIImage\""
+ "T@\"NSData\",R,C,N,V_pngRep"
+ "T@\"NSString\",R,C,N,V_identifier"
+ "T@\"UIImage\",R,N,V_image"
+ "_AXBarButtonReferenceIcon"
+ "_image"
+ "_pngRep"
+ "initWithIdentifier:kitImageName:"
+ "pngRep"
+ "scale"
```
