## TranslationDaemon

> `/System/Library/PrivateFrameworks/TranslationDaemon.framework/TranslationDaemon`

```diff

-355.6.1.0.0
-  __TEXT.__text: 0x196670
+355.5.2.0.0
+  __TEXT.__text: 0x1966fc
   __TEXT.__auth_stubs: 0xd40
   __TEXT.__objc_methlist: 0x19db8
   __TEXT.__const: 0x4b0
   __TEXT.__gcc_except_tab: 0x1b3f0
   __TEXT.__cstring: 0x5dc0
-  __TEXT.__oslogstring: 0xc562
+  __TEXT.__oslogstring: 0xc5db
   __TEXT.__dlopen_cstrs: 0xb2
   __TEXT.__unwind_info: 0xf530
   __TEXT.__objc_classname: 0x477b
-  __TEXT.__objc_methname: 0x1b70d
+  __TEXT.__objc_methname: 0x1b706
   __TEXT.__objc_methtype: 0xdfe8
-  __TEXT.__objc_stubs: 0x12d60
+  __TEXT.__objc_stubs: 0x12d80
   __DATA_CONST.__got: 0xca8
-  __DATA_CONST.__const: 0x4018
+  __DATA_CONST.__const: 0x4010
   __DATA_CONST.__objc_classlist: 0x11a8
   __DATA_CONST.__objc_catlist: 0x138
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x68c0
+  __DATA_CONST.__objc_selrefs: 0x68c8
   __DATA_CONST.__objc_superrefs: 0x1118
   __DATA_CONST.__objc_arraydata: 0x3f0
   __AUTH_CONST.__auth_got: 0x6b8
-  __AUTH_CONST.__const: 0xba0
+  __AUTH_CONST.__const: 0xbc0
   __AUTH_CONST.__cfstring: 0x7a20
   __AUTH_CONST.__objc_const: 0x2c788
   __AUTH_CONST.__objc_arrayobj: 0xf0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmorphun.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 320DECA9-D286-3317-9AB3-576777B6191D
-  Functions: 10035
-  Symbols:   34057
-  CStrings:  9202
+  UUID: E9868DD4-F6EF-3502-B9CC-ACD0F4F33026
+  Functions: 10036
+  Symbols:   34061
+  CStrings:  9204
 
Symbols:
+ ___82-[_LTTranslationResult(Daemon) updateAlignmentWithSourceSpans:offlineTargetSpans:]_block_invoke.cold.2
+ ___block_descriptor_32_e36_"FTSpan"16?0"_LTTranslationSpan"8l
+ _objc_msgSend$codePointsRange
+ _objc_msgSend$codeUnitsRange
- ___block_descriptor_40_ea8_32s_e36_"FTSpan"16?0"_LTTranslationSpan"8ls32l8
- _objc_msgSend$lt_codePointsRangeFromCodeUnitsRange:
Functions:
~ -[_LTOnlineTranslationEngine _createOrUpdateBatchTranslationRequestWithParagraph:index:context:completion:] : 2444 -> 2352
~ ___107-[_LTOnlineTranslationEngine _createOrUpdateBatchTranslationRequestWithParagraph:index:context:completion:]_block_invoke : 348 -> 324
~ ___82-[_LTTranslationResult(Daemon) updateAlignmentWithSourceSpans:offlineTargetSpans:]_block_invoke : 564 -> 652
+ ___82-[_LTTranslationResult(Daemon) updateAlignmentWithSourceSpans:offlineTargetSpans:]_block_invoke.cold.2
CStrings:
+ "Unexpectedly cannot convert Unicode code points range into UTF-16 code units range for span with identifier '%{public}@'"
+ "codePointsRange"
+ "codeUnitsRange"
- "lt_codePointsRangeFromCodeUnitsRange:"

```
