## TextInputCJK

> `/System/Library/PrivateFrameworks/TextInputCJK.framework/Versions/A/TextInputCJK`

```diff

-3567.400.0.0.0
-  __TEXT.__text: 0x20f68
+3568.1.8.0.0
+  __TEXT.__text: 0x213b4
   __TEXT.__init_offsets: 0x2c
-  __TEXT.__objc_methlist: 0x1f00
+  __TEXT.__objc_methlist: 0x1f50
   __TEXT.__const: 0xc0
   __TEXT.__cstring: 0xeb0
-  __TEXT.__ustring: 0x4fa
+  __TEXT.__ustring: 0x502
   __TEXT.__oslogstring: 0x36d
-  __TEXT.__unwind_info: 0x718
+  __TEXT.__unwind_info: 0x720
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c28
+  __DATA_CONST.__objc_selrefs: 0x1c70
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0xdd0
-  __DATA_CONST.__got: 0x3e0
-  __AUTH_CONST.__const: 0x8f0
-  __AUTH_CONST.__cfstring: 0x2860
-  __AUTH_CONST.__objc_const: 0x29b8
+  __DATA_CONST.__got: 0x3f0
+  __AUTH_CONST.__const: 0x910
+  __AUTH_CONST.__cfstring: 0x2880
+  __AUTH_CONST.__objc_const: 0x2a18
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x348
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_intobj: 0x150
-  __AUTH_CONST.__auth_got: 0x410
+  __AUTH_CONST.__auth_got: 0x418
   __AUTH_CONST.__auth_ptr: 0x0
   __AUTH.__objc_data: 0xa00
-  __DATA.__objc_ivar: 0x1ac
+  __DATA.__objc_ivar: 0x1b4
   __DATA.__data: 0x2d8
-  __DATA.__bss: 0x110
+  __DATA.__bss: 0x120
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libmecabra.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 733
-  Symbols:   2200
-  CStrings:  369
+  Functions: 740
+  Symbols:   2221
+  CStrings:  370
 
Symbols:
+ +[TIChineseExtras stringContainsOffensiveCharacter:]
+ -[TIWordSearchChinesePhonetic chaiziCandidatesWithOperation:candidateResultSet:useDictionaryReadingForFirstCandidate:]
+ -[TIWordSearchChinesePhonetic chaiziMecabraEnvironment]
+ -[TIWordSearchChinesePhonetic chaiziMecabraWrapper]
+ -[TIWordSearchChinesePhonetic dictionaryReadingForCandidate:candidateResultSet:]
+ -[TIWordSearchChinesePhonetic setChaiziMecabraEnvironment:]
+ -[TIWordSearchChinesePhonetic setChaiziMecabraWrapper:]
+ OBJC_IVAR_$_TIWordSearchChinesePhonetic._chaiziMecabraEnvironment
+ OBJC_IVAR_$_TIWordSearchChinesePhonetic._chaiziMecabraWrapper
+ _OBJC_CLASS_$_TIMecabraComposedCharacterCandidate
+ _OBJC_CLASS_$_TIMecabraWrapper
+ ___52+[TIChineseExtras stringContainsOffensiveCharacter:]_block_invoke
+ _objc_msgSend$chaiziCandidatesWithOperation:candidateResultSet:useDictionaryReadingForFirstCandidate:
+ _objc_msgSend$chaiziMecabraEnvironment
+ _objc_msgSend$chaiziMecabraWrapper
+ _objc_msgSend$dictionaryReadingForCandidate:candidateResultSet:
+ _objc_msgSend$initWithInputMethodType:learningDictionaryDirectoryURL:creationOptions:
+ _objc_msgSend$initWithMecabraEngine:language:
+ _objc_msgSend$mecabraRef
+ _objc_msgSend$stringContainsOffensiveCharacter:
+ _objc_retainAutoreleasedReturnValue
+ stringContainsOffensiveCharacter:.offensiveCharacterSet
+ stringContainsOffensiveCharacter:.onceToken
- -[TIWordSearchChinesePhonetic chaiziCandidatesWithOperation:candidateResultSet:]
- _objc_msgSend$chaiziCandidatesWithOperation:candidateResultSet:
CStrings:
+ "屄屌肏"
```
