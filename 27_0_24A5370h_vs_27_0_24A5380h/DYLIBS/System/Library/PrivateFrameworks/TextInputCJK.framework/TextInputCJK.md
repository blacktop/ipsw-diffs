## TextInputCJK

> `/System/Library/PrivateFrameworks/TextInputCJK.framework/TextInputCJK`

```diff

-  __TEXT.__text: 0x1edd8
+  __TEXT.__text: 0x1f228
   __TEXT.__init_offsets: 0x2c
-  __TEXT.__objc_methlist: 0x1f08
+  __TEXT.__objc_methlist: 0x1f00
   __TEXT.__const: 0xc0
-  __TEXT.__cstring: 0xfbc
+  __TEXT.__cstring: 0x1006
   __TEXT.__ustring: 0x4fa
   __TEXT.__oslogstring: 0x3b4
   __TEXT.__unwind_info: 0x6c0

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x758
+  __DATA_CONST.__const: 0x780
   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c68
+  __DATA_CONST.__objc_selrefs: 0x1c88
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0xdc0
-  __DATA_CONST.__got: 0x418
+  __DATA_CONST.__got: 0x420
   __AUTH_CONST.__const: 0x260
-  __AUTH_CONST.__cfstring: 0x2880
+  __AUTH_CONST.__cfstring: 0x28c0
   __AUTH_CONST.__objc_const: 0x29b8
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x330

   __AUTH.__objc_data: 0xa00
   __DATA.__objc_ivar: 0x1ac
   __DATA.__data: 0x2d8
-  __DATA.__bss: 0x100
+  __DATA.__bss: 0x110
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmecabra.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 691
-  Symbols:   2933
-  CStrings:  552
+  Functions: 695
+  Symbols:   2949
+  CStrings:  556
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__objc_ivar : content changed
~ __DATA.__data : content changed
Symbols:
+ +[TIKeyboardInputManagerChinese closingPunctuationMarkForContextBeforeInput:contextAfterInput:]
+ +[TIKeyboardInputManagerChinese closingPunctuationMarkSet]
+ -[TIKeyboardInputManagerPinyin supportsPairedPunctutationInput]
+ _OBJC_CLASS_$_NSSet
+ __ZZ58+[TIKeyboardInputManagerChinese closingPunctuationMarkSet]E11__onceToken
+ __ZZ58+[TIKeyboardInputManagerChinese closingPunctuationMarkSet]E27__closingPunctuationMarkSet
+ ___58+[TIKeyboardInputManagerChinese closingPunctuationMarkSet]_block_invoke
+ ___95+[TIKeyboardInputManagerChinese closingPunctuationMarkForContextBeforeInput:contextAfterInput:]_block_invoke
+ ___block_descriptor_72_a8_32s40s48r56r64r_e52_v56?0"NSString"8{_NSRange=QQ}16{_NSRange=QQ}32^B48lr48l8s32l8r56l8s40l8r64l8
+ ___block_descriptor_88_a8_32s40s48s56s64s72s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ _objc_msgSend$allValues
+ _objc_msgSend$closingPunctuationMarkForContextBeforeInput:contextAfterInput:
+ _objc_msgSend$closingPunctuationMarkSet
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$onScreenContext
+ _objc_msgSend$setOnScreenContext:
- -[TIKeyboardInputManagerChinese rightContextAdjacentToCaretContainsText]
- -[TIKeyboardInputManagerChinese shouldUsePairedPunctuationWhenCharacterAfterCaretIsText]
- -[TIKeyboardInputManagerChinesePhonetic shouldUsePairedPunctuationWhenCharacterAfterCaretIsText]
- ___block_descriptor_80_a8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- _objc_msgSend$rightContextAdjacentToCaretContainsText
- _objc_msgSend$shouldUsePairedPunctuationWhenCharacterAfterCaretIsText
CStrings:
+ "%s [Environment] Set left context: %{sensitive}@, Right context: %{sensitive}@, On-screen length: %@"
+ "com.tencent.xin"
+ "jp.naver.line"
- "%s [Environment] Set left context: %@, Right context: %@"

```
