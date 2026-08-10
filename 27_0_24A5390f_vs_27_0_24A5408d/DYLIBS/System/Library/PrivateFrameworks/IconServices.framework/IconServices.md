## IconServices

> `/System/Library/PrivateFrameworks/IconServices.framework/IconServices`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__eh_frame`
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
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-788.0.0.0.0
-  __TEXT.__text: 0x66840
+792.100.0.0.0
+  __TEXT.__text: 0x666ec
   __TEXT.__delay_stubs: 0x80
   __TEXT.__delay_helper: 0xa4
   __TEXT.__objc_methlist: 0x6934
   __TEXT.__const: 0x8840
-  __TEXT.__cstring: 0x45c3
+  __TEXT.__cstring: 0x45df
   __TEXT.__oslogstring: 0x3cb3
   __TEXT.__gcc_except_tab: 0x650
-  __TEXT.__unwind_info: 0x19d8
+  __TEXT.__unwind_info: 0x19d0
   __TEXT.__eh_frame: 0x80
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3178
+  __DATA_CONST.__objc_selrefs: 0x3180
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x408
   __DATA_CONST.__objc_arraydata: 0xb0
-  __DATA_CONST.__got: 0x6a8
+  __DATA_CONST.__got: 0x6b0
   __AUTH_CONST.__const: 0x11a8
-  __AUTH_CONST.__cfstring: 0x49c0
+  __AUTH_CONST.__cfstring: 0x49e0
   __AUTH_CONST.__objc_const: 0x13f98
   __AUTH_CONST.__objc_intobj: 0x528
   __AUTH_CONST.__objc_arrayobj: 0x108

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 2599
-  Symbols:   6198
-  CStrings:  1076
+  Symbols:   6200
+  CStrings:  1077
 
Symbols:
+ _OBJC_CLASS_$_IFImageInspector
+ _objc_msgSend$isCenterPixelTransparent
Functions:
~ _ISShouldSkipCacheForIcon : 156 -> 236
~ _ISIsTransparent : 256 -> 72
~ -[ISIconStackCompositeResource iconStackForSize:scale:] : 292 -> 320
~ -[ISIconStackComposer iconStackForSize:scale:desiredAssetAppearance:designGeneration:returningGenerationReport:] : 4748 -> 4472
~ -[ISIconStackComposer iconStackForSize:scale:desiredAssetAppearance:designGeneration:returningGenerationReport:].cold.2 -> -[ISIconStackComposer iconStackForSize:scale:desiredAssetAppearance:designGeneration:returningGenerationReport:].cold.1 : 64 -> 76
CStrings:
+ "23:13:26"
+ "com.apple.graphic-icon.siri"
- "20:59:25"
```
