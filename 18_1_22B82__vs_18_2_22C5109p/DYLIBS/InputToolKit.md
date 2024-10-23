## InputToolKit

> `/System/Library/PrivateFrameworks/InputToolKit.framework/InputToolKit`

```diff

-26.100.0.0.0
-  __TEXT.__text: 0xc054
-  __TEXT.__auth_stubs: 0x720
-  __TEXT.__objc_methlist: 0x708
+26.203.3.0.0
+  __TEXT.__text: 0xd3e8
+  __TEXT.__auth_stubs: 0x820
+  __TEXT.__objc_methlist: 0x738
   __TEXT.__const: 0x1a0
-  __TEXT.__cstring: 0x6a0
-  __TEXT.__oslogstring: 0x1e3
-  __TEXT.__gcc_except_tab: 0xe0
-  __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x488
-  __TEXT.__objc_classname: 0x4f
-  __TEXT.__objc_methname: 0x1b3c
+  __TEXT.__cstring: 0x6f7
+  __TEXT.__oslogstring: 0x24c
+  __TEXT.__gcc_except_tab: 0x350
+  __TEXT.__ustring: 0x18
+  __TEXT.__unwind_info: 0x530
+  __TEXT.__objc_classname: 0x61
+  __TEXT.__objc_methname: 0x1cd7
   __TEXT.__objc_methtype: 0x384
-  __TEXT.__objc_stubs: 0x1580
-  __DATA_CONST.__got: 0x110
-  __DATA_CONST.__const: 0x2b8
-  __DATA_CONST.__objc_classlist: 0x18
+  __TEXT.__objc_stubs: 0x1720
+  __DATA_CONST.__got: 0x158
+  __DATA_CONST.__const: 0x2e0
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x800
+  __DATA_CONST.__objc_selrefs: 0x880
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_arraydata: 0xf0
-  __AUTH_CONST.__auth_got: 0x3a0
+  __DATA_CONST.__objc_arraydata: 0x1c0
+  __AUTH_CONST.__auth_got: 0x428
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x760
-  __AUTH_CONST.__objc_const: 0xbf0
-  __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0xf0
+  __AUTH_CONST.__const: 0x180
+  __AUTH_CONST.__cfstring: 0x8a0
+  __AUTH_CONST.__objc_const: 0xc80
+  __AUTH_CONST.__objc_arrayobj: 0x90
+  __AUTH_CONST.__objc_dictobj: 0xa0
+  __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x10
   __DATA.__data: 0xc0
-  __DATA.__bss: 0xa0
+  __DATA.__bss: 0xd0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
+  - /System/Library/PrivateFrameworks/Lexicon.framework/Lexicon
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/TextRecognition.framework/TextRecognition
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 411
-  Symbols:   586
-  CStrings:  447
+  Functions: 430
+  Symbols:   633
+  CStrings:  474
 
Symbols:
+ _CFStringGetCStringPtr
+ _CFStringGetCharacters
+ _CFStringGetCharactersPtr
+ _CFStringGetLength
+ _LXEntryCopyString
+ _LXLexiconCreate
+ _LXLexiconEnumerateEntriesForString
+ _OBJC_CLASS_$_ITKLexiconChecker
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSMutableCharacterSet
+ _OBJC_METACLASS_$_ITKLexiconChecker
+ __ZNSt11logic_errorC2EPKc
+ __ZNSt12length_errorD1Ev
+ __ZNSt20bad_array_new_lengthC1Ev
+ __ZNSt20bad_array_new_lengthD1Ev
+ __ZTISt12length_error
+ __ZTISt20bad_array_new_length
+ __ZTVSt12length_error
+ __ZdlPv
+ __Znwm
+ ___cxa_allocate_exception
+ ___cxa_free_exception
+ ___cxa_throw
+ ___gxx_personality_v0
+ _bzero
+ _kLXLexiconDataFileKey
+ _kLXLexiconLocaleKey
+ _objc_retainBlock
CStrings:
+ "-"
+ "0123456789"
+ "ITKLexiconChecker"
+ "The allow list lexicon could not be discovered in the supplied bundle"
+ "URLForResource:withExtension:"
+ "addCharactersInString:"
+ "al-lexicon"
+ "bundleWithIdentifier:"
+ "com.apple.InputToolKit"
+ "compare:options:range:locale:"
+ "componentsSeparatedByCharactersInSet:"
+ "createEnglishNormalizedString:"
+ "dat"
+ "dictionaryWithObjects:forKeys:count:"
+ "en-US"
+ "englishLexiconCheck:"
+ "failed to load lexicon: %!{(MISSING)public}@"
+ "initWithLocaleIdentifier:"
+ "isStringEnglish:"
+ "longCharacterIsMember:"
+ "path"
+ "precomposedStringWithCanonicalMapping"
+ "punctuationCharacterSet"
+ "rangeOfString:options:"
+ "v24@?0^{_LXEntry=}8*16"
+ "vector"
+ "whitespaceCharacterSet"

```
