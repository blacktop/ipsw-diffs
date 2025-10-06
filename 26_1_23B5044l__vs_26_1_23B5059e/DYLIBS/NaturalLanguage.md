## NaturalLanguage

> `/System/Library/Frameworks/NaturalLanguage.framework/NaturalLanguage`

```diff

-172.2.0.0.0
-  __TEXT.__text: 0x53e68
+172.4.0.0.0
+  __TEXT.__text: 0x53eb0
   __TEXT.__auth_stubs: 0x16b0
   __TEXT.__objc_methlist: 0x3684
   __TEXT.__const: 0x53c
   __TEXT.__cstring: 0x354d
   __TEXT.__ustring: 0x32
-  __TEXT.__gcc_except_tab: 0x2c64
+  __TEXT.__gcc_except_tab: 0x2c68
   __TEXT.__oslogstring: 0x128
   __TEXT.__unwind_info: 0x1720
   __TEXT.__objc_classname: 0x5f5
-  __TEXT.__objc_methname: 0x6cda
-  __TEXT.__objc_methtype: 0x1c4e
+  __TEXT.__objc_methname: 0x6ced
+  __TEXT.__objc_methtype: 0x1c51
   __TEXT.__objc_stubs: 0x4f20
   __DATA_CONST.__got: 0x650
   __DATA_CONST.__const: 0x1368

   __DATA_CONST.__objc_selrefs: 0x19f0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1f8
-  __DATA_CONST.__objc_arraydata: 0xd0
+  __DATA_CONST.__objc_arraydata: 0xe8
   __AUTH_CONST.__auth_got: 0xb70
   __AUTH_CONST.__const: 0x650
   __AUTH_CONST.__cfstring: 0x4740
   __AUTH_CONST.__objc_const: 0x6798
   __AUTH_CONST.__objc_intobj: 0xa8
-  __AUTH_CONST.__objc_arrayobj: 0xd8
+  __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x140

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E502766A-C6C4-386C-AE5D-24C7D9623435
+  UUID: B6DA8AE7-5BC0-3E74-9EEA-EB735E381E7F
   Functions: 1588
   Symbols:   5852
   CStrings:  2580
Symbols:
+ +[NLLanguageRecognizer(Preferences) _isString:words:plausiblyInLanguage:increasedThreshold:]
+ ___92+[NLLanguageRecognizer(Preferences) _isString:words:plausiblyInLanguage:increasedThreshold:]_block_invoke
+ _objc_msgSend$_isString:words:plausiblyInLanguage:increasedThreshold:
- +[NLLanguageRecognizer(Preferences) _isString:words:plausiblyInLanguage:]
- ___73+[NLLanguageRecognizer(Preferences) _isString:words:plausiblyInLanguage:]_block_invoke
- _objc_msgSend$_isString:words:plausiblyInLanguage:
Functions:
~ +[NLLanguageRecognizer(Preferences) _isString:words:plausiblyInLanguage:] -> +[NLLanguageRecognizer(Preferences) _isString:words:plausiblyInLanguage:increasedThreshold:] : 1656 -> 1680
~ +[NLLanguageRecognizer(Preferences) mostAppropriateLanguageForString:candidateLanguages:preferredLanguages:] : 1504 -> 1552
CStrings:
+ "B44@0:8@16@24@32B40"
+ "_isString:words:plausiblyInLanguage:increasedThreshold:"
- "B40@0:8@16@24@32"
- "_isString:words:plausiblyInLanguage:"

```
