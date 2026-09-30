## TextInputCJK

> `/System/Library/PrivateFrameworks/TextInputCJK.framework/TextInputCJK`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__data`

```diff

-3559.100.0.0.0
-  __TEXT.__text: 0x1f228
+3562.0.0.0.0
+  __TEXT.__text: 0x1f1d4
   __TEXT.__init_offsets: 0x2c
   __TEXT.__objc_methlist: 0x1f00
   __TEXT.__const: 0xc0
-  __TEXT.__cstring: 0x1006
+  __TEXT.__cstring: 0xfe8
   __TEXT.__ustring: 0x4fa
   __TEXT.__oslogstring: 0x3b4
   __TEXT.__unwind_info: 0x6c0

   __DATA_CONST.__objc_arraydata: 0xdc0
   __DATA_CONST.__got: 0x420
   __AUTH_CONST.__const: 0x260
-  __AUTH_CONST.__cfstring: 0x28c0
+  __AUTH_CONST.__cfstring: 0x2880
   __AUTH_CONST.__objc_const: 0x29b8
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x330

   - /usr/lib/libobjc.A.dylib
   Functions: 695
   Symbols:   2219
-  CStrings:  375
+  CStrings:  373
 
Symbols:
+ _objc_msgSend$onScreenContextForCandidates
- _objc_msgSend$onScreenTextAsString
Functions:
~ -[TIKeyboardInputManagerChinese generateCompletions] : 784 -> 668
~ +[TIKeyboardInputManagerChinese closingPunctuationMarkForContextBeforeInput:contextAfterInput:] : 540 -> 572
CStrings:
- "com.tencent.xin"
- "jp.naver.line"
```
