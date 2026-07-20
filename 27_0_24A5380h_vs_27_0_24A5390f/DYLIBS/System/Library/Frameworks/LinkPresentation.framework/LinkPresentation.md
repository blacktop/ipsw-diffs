## LinkPresentation

> `/System/Library/Frameworks/LinkPresentation.framework/LinkPresentation`

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

```diff

-310.0.0.0.0
-  __TEXT.__text: 0x10be24
-  __TEXT.__objc_methlist: 0x11154
+311.0.0.0.0
+  __TEXT.__text: 0x10bf5c
+  __TEXT.__objc_methlist: 0x1117c
   __TEXT.__cstring: 0x8c01
-  __TEXT.__gcc_except_tab: 0x23408
-  __TEXT.__const: 0x2344
+  __TEXT.__gcc_except_tab: 0x233d8
+  __TEXT.__const: 0x2354
   __TEXT.__ustring: 0x3f6
   __TEXT.__oslogstring: 0x3b8b
   __TEXT.__dlopen_cstrs: 0x9c7

   __TEXT.__swift_as_ret: 0x28
   __TEXT.__swift_as_cont: 0x4c
   __TEXT.__swift5_assocty: 0x108
-  __TEXT.__unwind_info: 0x83d8
+  __TEXT.__unwind_info: 0x83f0
   __TEXT.__eh_frame: 0xd18
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x240
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7b38
+  __DATA_CONST.__objc_selrefs: 0x7b40
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x5f0
   __DATA_CONST.__objc_arraydata: 0x1640
-  __DATA_CONST.__got: 0xe08
+  __DATA_CONST.__got: 0xed0
   __AUTH_CONST.__const: 0x1ed8
   __AUTH_CONST.__cfstring: 0xdc00
-  __AUTH_CONST.__objc_const: 0x2ddf0
+  __AUTH_CONST.__objc_const: 0x2de20
   __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_arrayobj: 0x648
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__auth_got: 0x1060
-  __AUTH.__objc_data: 0x3e40
-  __AUTH.__data: 0x4d8
-  __DATA.__objc_ivar: 0x1804
-  __DATA.__data: 0x1c28
-  __DATA.__bss: 0x1b20
+  __AUTH.__objc_data: 0x36e8
+  __AUTH.__data: 0x4d0
+  __DATA.__objc_ivar: 0x1808
+  __DATA.__data: 0x1c18
+  __DATA.__bss: 0x1b10
   __DATA.__common: 0x1d8
-  __DATA_DIRTY.__objc_data: 0x1b58
-  __DATA_DIRTY.__data: 0x8
+  __DATA_DIRTY.__objc_data: 0x22b0
+  __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x108
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6856
-  Symbols:   15107
+  Functions: 6860
+  Symbols:   15114
   CStrings:  2319
 
Symbols:
+ -[LPCircularProgressIndicator tintColorDidChange]
+ -[LPCircularProgressIndicatorStyle setTrackColor:]
+ -[LPCircularProgressIndicatorStyle trackColor]
+ -[LPLinkMetadataPresentationTransformer setSupportsInlineSymbolImages:]
+ -[LPLinkMetadataPresentationTransformer setSupportsOverlaidMediaCaptionBars:]
+ -[LPLinkMetadataPresentationTransformer supportsInlineSymbolImages]
+ -[LPLinkMetadataPresentationTransformer supportsOverlaidMediaCaptionBars]
+ GCC_except_table281
+ GCC_except_table419
+ GCC_except_table420
+ _OBJC_IVAR_$_LPCircularProgressIndicatorStyle._trackColor
+ _OBJC_IVAR_$_LPLinkMetadataPresentationTransformer._supportsInlineSymbolImages
+ _OBJC_IVAR_$_LPLinkMetadataPresentationTransformer._supportsOverlaidMediaCaptionBars
+ _joinSymbolWithText
+ _objc_msgSend$bezierPathWithArcCenter:radius:startAngle:endAngle:clockwise:
+ _objc_msgSend$setSupportsInlineSymbolImages:
+ _objc_msgSend$setSupportsOverlaidMediaCaptionBars:
+ _objc_msgSend$setTrackColor:
+ _objc_msgSend$supportsInlineSymbolImages
+ _objc_msgSend$supportsOverlaidMediaCaptionBars
+ _objc_msgSend$trackColor
- -[LPCircularProgressIndicatorStyle borderColor]
- -[LPCircularProgressIndicatorStyle fillColor]
- -[LPCircularProgressIndicatorStyle setBorderColor:]
- -[LPCircularProgressIndicatorStyle setFillColor:]
- GCC_except_table174
- GCC_except_table283
- _OBJC_IVAR_$_LPCircularProgressIndicatorStyle._borderColor
- _OBJC_IVAR_$_LPCircularProgressIndicatorStyle._fillColor
- _objc_msgSend$addArcWithCenter:radius:startAngle:endAngle:clockwise:
- _objc_msgSend$addLineToPoint:
- _objc_msgSend$bezierPath
- _objc_msgSend$fillColor
- _objc_msgSend$lightGrayColor
- _objc_msgSend$moveToPoint:
```
