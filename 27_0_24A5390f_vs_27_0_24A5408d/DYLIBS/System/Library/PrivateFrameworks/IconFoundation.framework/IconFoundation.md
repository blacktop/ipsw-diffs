## IconFoundation

> `/System/Library/PrivateFrameworks/IconFoundation.framework/IconFoundation`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-788.0.0.0.0
-  __TEXT.__text: 0x39540
-  __TEXT.__objc_methlist: 0x30ac
-  __TEXT.__cstring: 0x12cb1
+792.100.0.0.0
+  __TEXT.__text: 0x39ad0
+  __TEXT.__objc_methlist: 0x3164
+  __TEXT.__cstring: 0x12ce1
   __TEXT.__const: 0x998
-  __TEXT.__oslogstring: 0xc2c
+  __TEXT.__oslogstring: 0xc46
   __TEXT.__gcc_except_tab: 0x108
   __TEXT.__constg_swiftt: 0x174
   __TEXT.__swift5_typeref: 0x48
   __TEXT.__swift5_fieldmd: 0xb0
   __TEXT.__swift5_types: 0x2c
-  __TEXT.__unwind_info: 0xf08
+  __TEXT.__unwind_info: 0xf38
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x7528
-  __DATA_CONST.__objc_classlist: 0x190
+  __DATA_CONST.__const: 0x7550
+  __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ef0
-  __DATA_CONST.__objc_superrefs: 0x110
+  __DATA_CONST.__objc_selrefs: 0x1f40
+  __DATA_CONST.__objc_superrefs: 0x118
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__got: 0x3d0
   __AUTH_CONST.__const: 0x8c8
   __AUTH_CONST.__cfstring: 0x1ba0
-  __AUTH_CONST.__objc_const: 0x4cc8
+  __AUTH_CONST.__objc_const: 0x4e08
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__auth_got: 0x8d8
-  __AUTH.__objc_data: 0x410
-  __DATA.__objc_ivar: 0x33c
+  __AUTH_CONST.__auth_got: 0x8e8
+  __AUTH.__objc_data: 0x460
+  __DATA.__objc_ivar: 0x348
   __DATA.__data: 0x2e8
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x2d8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1533
-  Symbols:   3171
-  CStrings:  2888
+  Functions: 1548
+  Symbols:   3206
+  CStrings:  2890
 
Symbols:
+ -[IFBundle _platformWithLaunchServicesUsageAllowed:]
+ -[IFBundle computedPlatformWithLS]
+ -[IFBundle computedPlatformWithoutLS]
+ -[IFBundle init]
+ -[IFBundle setComputedPlatformWithLS:]
+ -[IFBundle setComputedPlatformWithoutLS:]
+ -[IFImageInspector dealloc]
+ -[IFImageInspector hasNoAlpha]
+ -[IFImageInspector image]
+ -[IFImageInspector initWithCGImage:]
+ -[IFImageInspector isCenterPixelTransparent]
+ -[IFImageInspector isSampleTransparentAtX:y:imageWidth:imageHeight:]
+ -[IFImageInspector isTransparentUsingSampleCount:]
+ -[IFSymbol resolvedName]
+ GCC_except_table40
+ _CGImageGetAlphaInfo
+ _CGImageRetain
+ _OBJC_CLASS_$_IFImageInspector
+ _OBJC_IVAR_$_IFBundle._computedPlatformWithLS
+ _OBJC_IVAR_$_IFBundle._computedPlatformWithoutLS
+ _OBJC_IVAR_$_IFImageInspector._image
+ _OBJC_METACLASS_$_IFImageInspector
+ __OBJC_$_INSTANCE_METHODS_IFImageInspector
+ __OBJC_$_INSTANCE_VARIABLES_IFImageInspector
+ __OBJC_$_PROP_LIST_IFImageInspector
+ __OBJC_CLASS_RO_$_IFImageInspector
+ __OBJC_METACLASS_RO_$_IFImageInspector
+ ___31-[IFSymbol imageForDescriptor:]_block_invoke
+ ___block_descriptor_40_e8_32s_e54_"CUINamedVectorGlyph"24?0"CUICatalog"8"NSString"16ls32l8
+ _objc_msgSend$_platformWithLaunchServicesUsageAllowed:
+ _objc_msgSend$computedPlatformWithLS
+ _objc_msgSend$computedPlatformWithoutLS
+ _objc_msgSend$hasNoAlpha
+ _objc_msgSend$isSampleTransparentAtX:y:imageWidth:imageHeight:
+ _objc_msgSend$setComputedPlatformWithLS:
+ _objc_msgSend$setComputedPlatformWithoutLS:
- GCC_except_table39
CStrings:
+ "%@ Resolved name %@ -> %@"
+ "@\"CUINamedVectorGlyph\"24@?0@\"CUICatalog\"8@\"NSString\"16"
+ "A"
- "!"
```
