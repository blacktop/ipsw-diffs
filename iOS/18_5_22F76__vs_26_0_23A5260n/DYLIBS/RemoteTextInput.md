## RemoteTextInput

> `/System/Library/PrivateFrameworks/RemoteTextInput.framework/RemoteTextInput`

```diff

-159.310.0.0.0
-  __TEXT.__text: 0x211d8
+167.0.0.0.0
+  __TEXT.__text: 0x214e8
   __TEXT.__auth_stubs: 0x770
-  __TEXT.__objc_methlist: 0x2b64
+  __TEXT.__objc_methlist: 0x2ba4
   __TEXT.__const: 0x108
-  __TEXT.__cstring: 0x2f26
+  __TEXT.__cstring: 0x2f76
   __TEXT.__oslogstring: 0xccc
   __TEXT.__gcc_except_tab: 0x2a8
   __TEXT.__dlopen_cstrs: 0xf6
-  __TEXT.__unwind_info: 0x930
+  __TEXT.__unwind_info: 0x900
   __TEXT.__objc_classname: 0x419
-  __TEXT.__objc_methname: 0x748a
-  __TEXT.__objc_methtype: 0x1745
-  __TEXT.__objc_stubs: 0x4740
+  __TEXT.__objc_methname: 0x7543
+  __TEXT.__objc_methtype: 0x1760
+  __TEXT.__objc_stubs: 0x47e0
   __DATA_CONST.__got: 0x260
   __DATA_CONST.__const: 0xc90
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1938
+  __DATA_CONST.__objc_selrefs: 0x1968
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xd8
+  __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x3c8
   __AUTH_CONST.__const: 0x220
-  __AUTH_CONST.__cfstring: 0x2d60
-  __AUTH_CONST.__objc_const: 0x68f8
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x328
+  __AUTH_CONST.__cfstring: 0x2de0
+  __AUTH_CONST.__objc_const: 0x6938
+  __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x32c
   __DATA.__data: 0x480
-  __DATA.__bss: 0x90
-  __DATA_DIRTY.__objc_data: 0x9b0
-  __DATA_DIRTY.__bss: 0x58
+  __DATA.__bss: 0x78
+  __DATA_DIRTY.__objc_data: 0xa00
+  __DATA_DIRTY.__bss: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8113F6F7-43C4-34E1-A1AF-E189C5652541
-  Functions: 1010
-  Symbols:   3654
-  CStrings:  2317
+  UUID: FDF95B3E-F260-3CA4-8E85-B2FBF6623CA1
+  Functions: 1016
+  Symbols:   3673
+  CStrings:  2334
 
Symbols:
+ +[RTIUtilities makeClientCodingQueuePthreadKeyOnce]
+ +[RTIUtilities makeClientCodingQueuePthreadKeyOnce].cold.1
+ -[RTIDocumentState displayZoom]
+ -[RTIDocumentState setDisplayZoom:]
+ -[RTIDocumentTraits setSupportsGenmojiCreation:]
+ -[RTIDocumentTraits supportsGenmojiCreation]
+ GCC_except_table26
+ GCC_except_table8
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_IVAR_$_RTIDocumentState._displayZoom
+ __RTI_NSStringFromCGSize
+ ___51+[RTIUtilities makeClientCodingQueuePthreadKeyOnce]_block_invoke
+ ___block_literal_global.113
+ ___block_literal_global.46
+ ___block_literal_global.48
+ ___block_literal_global.82
+ _makeClientCodingQueuePthreadKeyOnce.onceToken
+ _objc_msgSend$displayZoom
+ _objc_msgSend$initWithString:attributes:
+ _objc_msgSend$makeClientCodingQueuePthreadKeyOnce
+ _objc_msgSend$setDisplayZoom:
+ _objc_msgSend$supportsGenmojiCreation
- +[RTIUtilities performClientCoding:withServiceOptions:].cold.1
- GCC_except_table24
- GCC_except_table7
- ___55+[RTIUtilities performClientCoding:withServiceOptions:]_block_invoke
- ___block_literal_global.110
- ___block_literal_global.43
- ___block_literal_global.45
- ___block_literal_global.79
- _performClientCoding:withServiceOptions:.onceToken
CStrings:
+ "(?=\"integerValue\"I\"fields\"{?=\"shouldLoadAutofillSignUp\"b1\"supportsImagePaste\"b1\"devicePasscodeEntry\"b1\"disableInputBars\"b1\"disablePrediction\"b1\"hidePrediction\"b1\"disableAutomaticKeyboardUI\"b1\"shouldReverseLayoutDirection\"b1\"explicitAutoFillMode\"b1\"singleLineDocument\"b1\"supportsAdaptiveImageGlyph\"b1\"supportsGenmojiCreation\"b1})"
+ "; displayZoom = %@"
+ "; supportsGenmojiCreation = YES"
+ "T{CGSize=dd},N,V_displayZoom"
+ "_displayZoom"
+ "displayZoom"
+ "initWithString:attributes:"
+ "makeClientCodingQueuePthreadKeyOnce"
+ "setDisplayZoom:"
+ "setSupportsGenmojiCreation:"
+ "supportsGenmojiCreation"
+ "{{%.*g, %.*g}}"
- "(?=\"integerValue\"I\"fields\"{?=\"shouldLoadAutofillSignUp\"b1\"supportsImagePaste\"b1\"devicePasscodeEntry\"b1\"disableInputBars\"b1\"disablePrediction\"b1\"hidePrediction\"b1\"disableAutomaticKeyboardUI\"b1\"shouldReverseLayoutDirection\"b1\"explicitAutoFillMode\"b1\"singleLineDocument\"b1\"supportsAdaptiveImageGlyph\"b1})"

```
