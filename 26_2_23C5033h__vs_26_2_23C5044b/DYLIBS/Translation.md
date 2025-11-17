## Translation

> `/System/Library/Frameworks/Translation.framework/Translation`

```diff

-355.6.1.0.0
-  __TEXT.__text: 0x4fc38
+355.5.2.0.0
+  __TEXT.__text: 0x4fdf8
   __TEXT.__auth_stubs: 0x10c0
-  __TEXT.__objc_methlist: 0x53d8
+  __TEXT.__objc_methlist: 0x53e8
   __TEXT.__const: 0xa78
-  __TEXT.__cstring: 0x2fbe
+  __TEXT.__cstring: 0x304e
   __TEXT.__oslogstring: 0x4aa6
   __TEXT.__gcc_except_tab: 0xb50
   __TEXT.__ustring: 0x90

   __TEXT.__unwind_info: 0x18e8
   __TEXT.__eh_frame: 0x7a8
   __TEXT.__objc_classname: 0xb36
-  __TEXT.__objc_methname: 0xb2a6
-  __TEXT.__objc_methtype: 0x1c3a
-  __TEXT.__objc_stubs: 0x6560
+  __TEXT.__objc_methname: 0xb339
+  __TEXT.__objc_methtype: 0x1c58
+  __TEXT.__objc_stubs: 0x65a0
   __DATA_CONST.__got: 0x500
   __DATA_CONST.__const: 0x1cb8
   __DATA_CONST.__objc_classlist: 0x2c8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x24c8
+  __DATA_CONST.__objc_selrefs: 0x24d0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x268
   __DATA_CONST.__objc_arraydata: 0xf0
   __AUTH_CONST.__auth_got: 0x870
   __AUTH_CONST.__const: 0xce8
-  __AUTH_CONST.__cfstring: 0x34c0
-  __AUTH_CONST.__objc_const: 0xaa40
+  __AUTH_CONST.__cfstring: 0x34e0
+  __AUTH_CONST.__objc_const: 0xaa70
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x11f0
   __AUTH.__data: 0x480
-  __DATA.__objc_ivar: 0x7e0
+  __DATA.__objc_ivar: 0x7e4
   __DATA.__data: 0xa30
   __DATA.__bss: 0xa00
   __DATA.__common: 0x48

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0297F5E8-F50D-3D0E-B660-2F41226A68F6
-  Functions: 2502
-  Symbols:   7242
-  CStrings:  3492
+  UUID: 09590278-0838-386B-963D-35FE9D75F203
+  Functions: 2504
+  Symbols:   7249
+  CStrings:  3498
 
Symbols:
+ -[_LTTranslationSpan codePointsRange]
+ -[_LTTranslationSpan codeUnitsRange]
+ -[_LTTranslationSpan initWithIdentifier:codePointsRange:codeUnitsRange:]
+ -[_LTTranslationSpan initWithIdentifier:codePointsRange:codeUnitsRange:shouldTranslate:metaInfoData:]
+ _OBJC_IVAR_$__LTTranslationSpan._codePointsRange
+ _OBJC_IVAR_$__LTTranslationSpan._codeUnitsRange
+ ___45-[_LTTranslationParagraph splitIntoSentences]_block_invoke_3.cold.2
+ ___block_descriptor_48_e8_32s40s_e41_v40?0"NSDictionary"8{_NSRange=QQ}16^B32ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e36_v32?0"_LTTranslationRange"8Q16^B24ls32l8r48l8s40l8
+ ___block_descriptor_64_e8_32s40s_e45_v32?0"NSString"8"_LTTranslationSpan"16^B24ls32l8s40l8
+ _objc_msgSend$codePointsRange
+ _objc_msgSend$codeUnitsRange
+ _objc_msgSend$initWithIdentifier:codePointsRange:codeUnitsRange:
+ _objc_msgSend$initWithIdentifier:codePointsRange:codeUnitsRange:shouldTranslate:metaInfoData:
+ _objc_msgSend$lt_codePointsRangeFromCodeUnitsRange:
- -[_LTTranslationSpan initWithIdentifier:range:]
- -[_LTTranslationSpan initWithIdentifier:range:shouldTranslate:metaInfoData:]
- -[_LTTranslationSpan range]
- _OBJC_IVAR_$__LTTranslationSpan._range
- ___block_descriptor_40_e8_32s_e41_v40?0"NSDictionary"8{_NSRange=QQ}16^B32ls32l8
- ___block_descriptor_56_e8_32s40s48r_e36_v32?0"_LTTranslationRange"8Q16^B24lr48l8s32l8s40l8
- ___block_descriptor_56_e8_32s_e45_v32?0"NSString"8"_LTTranslationSpan"16^B24ls32l8
- _objc_msgSend$initWithIdentifier:range:
- _objc_msgSend$initWithIdentifier:range:shouldTranslate:metaInfoData:
- _objc_msgSend$range
CStrings:
+ "@56@0:8@16{_NSRange=QQ}24{_NSRange=QQ}40"
+ "@68@0:8@16{_NSRange=QQ}24{_NSRange=QQ}40B56@60"
+ "T{_NSRange=QQ},R,N,V_codePointsRange"
+ "T{_NSRange=QQ},R,N,V_codeUnitsRange"
+ "_codePointsRange"
+ "_codeUnitsRange"
+ "codePointsRange"
+ "codeUnitsRange"
+ "initWithIdentifier:codePointsRange:codeUnitsRange:"
+ "initWithIdentifier:codePointsRange:codeUnitsRange:shouldTranslate:metaInfoData:"
+ "previousSpan.codePointsRange.location + previousSpan.codePointsRange.length == codePointsRange.location"
+ "previousSpan.codeUnitsRange.location + previousSpan.codeUnitsRange.length == textRange.location"
- "@40@0:8@16{_NSRange=QQ}24"
- "@52@0:8@16{_NSRange=QQ}24B40@44"
- "T{_NSRange=QQ},R,N,V_range"
- "_range"
- "initWithIdentifier:range:"
- "initWithIdentifier:range:shouldTranslate:metaInfoData:"
- "previousSpan.range.location + previousSpan.range.length == textRange.location"
- "range"

```
