## CoreNameParser

> `/System/Library/PrivateFrameworks/CoreNameParser.framework/Versions/A/CoreNameParser`

```diff

-13.0.2.0.0
-  __TEXT.__text: 0x6384
+14.0.0.0.0
+  __TEXT.__text: 0x6700
   __TEXT.__auth_stubs: 0x260
   __TEXT.__objc_methlist: 0x3dc
   __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x25e
+  __TEXT.__cstring: 0x397
   __TEXT.__gcc_except_tab: 0xe8
   __TEXT.__ustring: 0x3c
-  __TEXT.__unwind_info: 0x1c8
+  __TEXT.__unwind_info: 0x1d0
   __TEXT.__objc_classname: 0x4e
-  __TEXT.__objc_methname: 0x1039
+  __TEXT.__objc_methname: 0x10cd
   __TEXT.__objc_methtype: 0x2a1
-  __TEXT.__objc_stubs: 0x11e0
-  __DATA_CONST.__got: 0xc0
+  __TEXT.__objc_stubs: 0x1260
+  __DATA_CONST.__got: 0xc8
   __DATA_CONST.__const: 0x88
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4e0
+  __DATA_CONST.__objc_selrefs: 0x500
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x140
   __AUTH_CONST.__const: 0x1f0
-  __AUTH_CONST.__cfstring: 0x500
+  __AUTH_CONST.__cfstring: 0x620
   __AUTH_CONST.__objc_const: 0x528
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28

   - /System/Library/PrivateFrameworks/CoreEmoji.framework/Versions/A/CoreEmoji
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7C00B316-9FAA-3BED-80BC-AB2AC9DEF01A
-  Functions: 113
-  Symbols:   418
-  CStrings:  309
+  UUID: 9620FAB7-2B20-3348-A49A-26E93D5EF6B6
+  Functions: 126
+  Symbols:   438
+  CStrings:  332
 
Symbols:
+ -[NPHMMClassifier compoundsFromName:includeSpaceAsDelimiter:].cold.1
+ -[NPHMMClassifier compoundsFromName:includeSpaceAsDelimiter:].cold.2
+ -[NPHMMClassifier initWithHMMProbabilities:nameComponentsDate:].cold.1
+ -[NPHMMClassifier isInitial:].cold.1
+ -[NPHMMClassifier probabilityForHiddenSequence:knowingObservationSequence:boost:].cold.1
+ -[NPHMMClassifier probabilityForHiddenSequence:knowingObservationSequence:boost:].cold.2
+ -[NPNameParser namingTraditionForName:].cold.1
+ -[NPNameParser namingTraditionForName:].cold.2
+ -[NPNameParser namingTraditionForName:].cold.3
+ -[NPNameParser namingTraditionForName:].cold.4
+ -[NPNameParser parseJapaneseName:normalize:].cold.1
+ _NPStripQuotationMarks.cold.1
+ _NPTrimNonLetters.cold.1
+ _OBJC_CLASS_$_NSAssertionHandler
+ __block_literal_global.112
+ __block_literal_global.114
+ __block_literal_global.116
+ __block_literal_global.27
+ __block_literal_global.46
+ __block_literal_global.52
+ __block_literal_global.58
+ _objc_msgSend$currentHandler
+ _objc_msgSend$handleFailureInFunction:file:lineNumber:description:
+ _objc_msgSend$handleFailureInMethod:object:file:lineNumber:description:
+ _objc_msgSend$stringWithUTF8String:
+ charSetWithEndpoints.cold.1
+ charSetWithEndpoints.cold.2
+ compoundsFromName:includeSpaceAsDelimiter:.onceToken.56
- __block_literal_global.105
- __block_literal_global.107
- __block_literal_global.109
- __block_literal_global.14
- __block_literal_global.36
- __block_literal_global.42
- __block_literal_global.48
- compoundsFromName:includeSpaceAsDelimiter:.onceToken.46
Functions:
~ -[NPNameParser namingTraditionForName:] : 1536 -> 1464
~ -[NPNameParser personNameComponentsFromString:] : 256 -> 252
- sub_195989dbc
~ -[NPNameParser parseFullnameWithDefaultHMMClassifier:normalize:score:] : 1820 -> 1812
~ -[NPNameParser parseChineseName:normalize:] : 1096 -> 1092
- sub_19598ab90
~ -[NPNameParser parseJapaneseName:normalize:] : 1736 -> 1760
~ -[NPHMMClassifier initWithHMMProbabilities:nameComponentsDate:] : 396 -> 428
~ -[NPHMMClassifier hiddenStatesFromObservationSequence:] : 2468 -> 2484
~ -[NPHMMClassifier isCoupleName:] : 168 -> 164
~ -[NPHMMClassifier probabilityForHiddenSequence:knowingObservationSequence:boost:] : 1008 -> 1036
~ -[NPHMMClassifier isInitial:] : 144 -> 128
~ -[NPHMMClassifier compoundsFromName:includeSpaceAsDelimiter:] : 200 -> 168
~ _charSetWithEndpoints : 184 -> 228
~ __NPCollapseWhitespaceAndStrip : 896 -> 888
~ __NPStripQuotationMarks : 232 -> 216
~ __NPTrimNonLetters : 132 -> 116
~ __NPTokenizeName : 720 -> 716
CStrings:
+ "Could not load ja_surname trie"
+ "Could not load name frequency trie data"
+ "Hidden sequence and observation sequence should have the same counts"
+ "Invalid parameter not satisfying: %@"
+ "NPHMMClassifier.m"
+ "NPNameParser.m"
+ "NPStringUtils.m"
+ "NSCharacterSet *charSetWithEndpoints(int, ...)"
+ "currentHandler"
+ "handleFailureInFunction:file:lineNumber:description:"
+ "handleFailureInMethod:object:file:lineNumber:description:"
+ "n_args && (n_args % 2) == 0"
+ "start < end"
+ "stringWithUTF8String:"

```
