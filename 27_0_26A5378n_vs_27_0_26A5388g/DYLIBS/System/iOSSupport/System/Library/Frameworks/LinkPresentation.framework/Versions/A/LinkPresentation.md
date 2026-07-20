## LinkPresentation

> `/System/iOSSupport/System/Library/Frameworks/LinkPresentation.framework/Versions/A/LinkPresentation`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__ustring`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__data`

```diff

-310.0.0.0.0
-  __TEXT.__text: 0xfd038
-  __TEXT.__objc_methlist: 0x10314
+311.0.0.0.0
+  __TEXT.__text: 0xfd158
+  __TEXT.__objc_methlist: 0x1033c
   __TEXT.__cstring: 0x80d1
-  __TEXT.__gcc_except_tab: 0x20fac
-  __TEXT.__const: 0x2264
+  __TEXT.__gcc_except_tab: 0x20f7c
+  __TEXT.__const: 0x2274
   __TEXT.__ustring: 0x46a
   __TEXT.__oslogstring: 0x371b
   __TEXT.__dlopen_cstrs: 0x8bf

   __TEXT.__swift_as_ret: 0x28
   __TEXT.__swift_as_cont: 0x4c
   __TEXT.__swift5_assocty: 0x108
-  __TEXT.__unwind_info: 0x7a68
+  __TEXT.__unwind_info: 0x7a80
   __TEXT.__eh_frame: 0xd18
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7420
+  __DATA_CONST.__objc_selrefs: 0x7428
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x548
   __DATA_CONST.__objc_arraydata: 0x1630
-  __DATA_CONST.__got: 0xd60
+  __DATA_CONST.__got: 0xe08
   __AUTH_CONST.__const: 0x1e98
   __AUTH_CONST.__cfstring: 0xca00
-  __AUTH_CONST.__objc_const: 0x2bcd8
+  __AUTH_CONST.__objc_const: 0x2bd08
   __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_arrayobj: 0x630
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__auth_got: 0x1028
-  __AUTH.__objc_data: 0x2fc0
+  __AUTH.__objc_data: 0x2908
   __AUTH.__data: 0x2f8
-  __DATA.__objc_ivar: 0x16f4
+  __DATA.__objc_ivar: 0x16f8
   __DATA.__data: 0x1a78
   __DATA.__bss: 0x19b0
   __DATA.__common: 0x1d8
-  __DATA_DIRTY.__objc_data: 0x22f8
+  __DATA_DIRTY.__objc_data: 0x29b0
   __DATA_DIRTY.__data: 0x208
   __DATA_DIRTY.__bss: 0x1c9
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6587
-  Symbols:   14416
+  Functions: 6591
+  Symbols:   14419
   CStrings:  2138
 
Symbols:
+ -[LPCircularProgressIndicator tintColorDidChange]
+ -[LPCircularProgressIndicatorStyle setTrackColor:]
+ -[LPCircularProgressIndicatorStyle trackColor]
+ -[LPLinkMetadataPresentationTransformer setSupportsInlineSymbolImages:]
+ -[LPLinkMetadataPresentationTransformer setSupportsOverlaidMediaCaptionBars:]
+ -[LPLinkMetadataPresentationTransformer supportsInlineSymbolImages]
+ -[LPLinkMetadataPresentationTransformer supportsOverlaidMediaCaptionBars]
+ GCC_except_table281
+ OBJC_IVAR_$_LPCircularProgressIndicatorStyle._trackColor
+ OBJC_IVAR_$_LPLinkMetadataPresentationTransformer._supportsInlineSymbolImages
+ OBJC_IVAR_$_LPLinkMetadataPresentationTransformer._supportsOverlaidMediaCaptionBars
+ _joinSymbolWithText
+ _objc_msgSend$bezierPathWithArcCenter:radius:startAngle:endAngle:clockwise:
+ _objc_msgSend$setTrackColor:
+ _objc_msgSend$supportsInlineSymbolImages
+ _objc_msgSend$supportsOverlaidMediaCaptionBars
+ _objc_msgSend$trackColor
- -[LPCircularProgressIndicatorStyle borderColor]
- -[LPCircularProgressIndicatorStyle fillColor]
- -[LPCircularProgressIndicatorStyle setBorderColor:]
- -[LPCircularProgressIndicatorStyle setFillColor:]
- GCC_except_table283
- GCC_except_table423
- OBJC_IVAR_$_LPCircularProgressIndicatorStyle._borderColor
- OBJC_IVAR_$_LPCircularProgressIndicatorStyle._fillColor
- _objc_msgSend$addArcWithCenter:radius:startAngle:endAngle:clockwise:
- _objc_msgSend$addLineToPoint:
- _objc_msgSend$bezierPath
- _objc_msgSend$fillColor
- _objc_msgSend$lightGrayColor
- _objc_msgSend$moveToPoint:
```
