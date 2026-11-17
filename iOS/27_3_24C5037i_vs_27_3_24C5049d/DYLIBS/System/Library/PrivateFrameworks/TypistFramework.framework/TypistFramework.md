## TypistFramework

> `/System/Library/PrivateFrameworks/TypistFramework.framework/TypistFramework`

```diff

-505.0.0.0.0
-  __TEXT.__text: 0x51320
-  __TEXT.__objc_methlist: 0x4254
+508.1.0.0.0
+  __TEXT.__text: 0x55760
+  __TEXT.__objc_methlist: 0x444c
   __TEXT.__const: 0x602
-  __TEXT.__ustring: 0x1464
-  __TEXT.__cstring: 0x6e42
-  __TEXT.__gcc_except_tab: 0xf70
+  __TEXT.__ustring: 0x14bc
+  __TEXT.__cstring: 0x7122
+  __TEXT.__gcc_except_tab: 0xf88
   __TEXT.__dlopen_cstrs: 0x6d
   __TEXT.__oslogstring: 0xc
   __TEXT.__swift5_typeref: 0xaa

   __TEXT.__swift5_fieldmd: 0x94
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0x1480
+  __TEXT.__unwind_info: 0x1520
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xbd8
+  __DATA_CONST.__const: 0xc28
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2d38
+  __DATA_CONST.__objc_selrefs: 0x2ef8
   __DATA_CONST.__objc_superrefs: 0x138
-  __DATA_CONST.__objc_arraydata: 0x3c98
-  __DATA_CONST.__got: 0x5a8
-  __AUTH_CONST.__const: 0x828
-  __AUTH_CONST.__cfstring: 0x129c0
-  __AUTH_CONST.__objc_const: 0x55f0
+  __DATA_CONST.__objc_arraydata: 0x3cd0
+  __DATA_CONST.__got: 0x5b8
+  __AUTH_CONST.__const: 0x888
+  __AUTH_CONST.__cfstring: 0x12e00
+  __AUTH_CONST.__objc_const: 0x57b0
   __AUTH_CONST.__objc_intobj: 0xbd0
-  __AUTH_CONST.__objc_arrayobj: 0x3d8
+  __AUTH_CONST.__objc_arrayobj: 0x3f0
   __AUTH_CONST.__objc_dictobj: 0x3e8
   __AUTH_CONST.__objc_doubleobj: 0xe0
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH_CONST.__auth_got: 0x798
+  __AUTH_CONST.__auth_got: 0x7a0
   __AUTH.__objc_data: 0xef8
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x368
+  __DATA.__objc_ivar: 0x394
   __DATA.__data: 0x200
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x1b8

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 1594
-  Symbols:   2717
-  CStrings:  2442
+  Functions: 1643
+  Symbols:   2791
+  CStrings:  2477
 
Symbols:
+ +[NSCharacterSet(Devanagari) devanagariConsonantCharacterSet]
+ +[NSCharacterSet(Devanagari) devanagariIrregularRaVowelCharacterSet]
+ +[NSCharacterSet(Devanagari) devanagariSubjoinedCaretRakarCharacterSet]
+ +[TypistDevanagariSyllable consonantIndicesInGrapheme:]
+ +[TypistDevanagariSyllable isConsonant:]
+ +[TypistDevanagariSyllable isIrregularRaVowel:]
+ +[TypistDevanagariSyllable isShortUMatra:]
+ +[TypistDevanagariSyllable isSubjoinedCaretRakarBase:]
+ +[TypistKeyboardUtilities(KeyboardSettings) injectLearningDictionaryFiles:fromDirectory:matchedFileNames:error:]
+ +[TypistKeyboardUtilities(KeyboardSettings) resetLearningDictionary:]
+ +[TypistKeyboardUtilities(MathUtilities) keycapForKey:]
+ +[TypistKeyboardUtilities(MathUtilities) spaceCompletesPeriodShortcutAfter:]
+ +[TypistKeyboardUtilities(MathUtilities) tapLandingForPoint:amongKeys:]
+ +[TypistKeyboardUtilities(RecapUtilities) actionsWithoutPlaneChecks:typeInterval:]
+ +[TypistKeyboardUtilities(SystemSettings) askHostToRotateToDeviceOrientation:]
+ +[TypistKeyboardUtilities(SystemSettings) currentDeviceOrientation]
+ +[TypistPathUtilities _appendAnchorAlignedStrokesFrom:targetAnchorX:toStrokes:]
+ +[TypistPathUtilities _appendHalfFormForConsonant:withData:nextConsonant:nextData:atOffsetX:withPathMap:toStrokes:]
+ +[TypistPathUtilities _appendMarksInGrapheme:fromIndex:withPathMap:finalConsonant:raBodyBounds:hasRakar:effectiveStemX:currentAdvance:rightMatraStemX:toStrokes:]
+ +[TypistPathUtilities _appendRakarStrokesForConsonant:withBodyStrokes:halantData:effectiveStemX:toStrokes:]
+ +[TypistPathUtilities _combinedBoundsOfStrokes:]
+ +[TypistPathUtilities _effectiveAnchorXForPathData:]
+ +[TypistPathUtilities _extractCenterStemHalfFormStrokesFrom:withTransform:bridgeEndX:]
+ +[TypistPathUtilities _extractKhariPaiHalfFormStrokesFrom:withTransform:]
+ +[TypistPathUtilities _headlineStartXForCharacter:withPathData:]
+ +[TypistPathUtilities _maxStrokeXInArray:]
+ +[TypistPathUtilities _minBodyInkXForPathData:character:]
+ +[TypistPathUtilities _synthesizeIrregularRaVowelForMark:withMarkData:raBodyBounds:effectiveStemX:]
+ +[TypistPathUtilities _synthesizeRephStrokeFromRaData:atAnchorX:]
+ -[TypistKeyboard _logKeyplaneGeometryOnce:]
+ -[TypistKeyboard _logTapLandings]
+ -[TypistKeyboard _recordPlayedRecapCommands:]
+ -[TypistKeyboard _recordTapLandingForAction:textIndex:]
+ -[TypistKeyboard collectsRecapCommands]
+ -[TypistKeyboard ignoresPlaneChecks]
+ -[TypistKeyboard lastRecapCommands]
+ -[TypistKeyboard lastTapCount]
+ -[TypistKeyboard lastTapLandings]
+ -[TypistKeyboard recordsTapLandings]
+ -[TypistKeyboard setCollectsRecapCommands:]
+ -[TypistKeyboard setIgnoresPlaneChecks:]
+ -[TypistKeyboard setRecordsTapLandings:]
+ GCC_except_table123
+ GCC_except_table38
+ GCC_except_table83
+ _CGPathApplyWithBlock
+ _NSCocoaErrorDomain
+ _OBJC_CLASS_$_NSMutableData
+ _OBJC_IVAR_$_TypistKeyboard._collectsRecapCommands
+ _OBJC_IVAR_$_TypistKeyboard._ignoresPlaneChecks
+ _OBJC_IVAR_$_TypistKeyboard._lastRecapCommands
+ _OBJC_IVAR_$_TypistKeyboard._lastTapCount
+ _OBJC_IVAR_$_TypistKeyboard._lastTapLandings
+ _OBJC_IVAR_$_TypistKeyboard._loggedKeyplaneGeometry
+ _OBJC_IVAR_$_TypistKeyboard._nestedTapStreams
+ _OBJC_IVAR_$_TypistKeyboard._outerTextIndex
+ _OBJC_IVAR_$_TypistKeyboard._recordsTapLandings
+ _OBJC_IVAR_$_TypistKeyboard._tapCount
+ _OBJC_IVAR_$_TypistKeyboard._tapLandings
+ ___61+[NSCharacterSet(Devanagari) devanagariConsonantCharacterSet]_block_invoke
+ ___68+[NSCharacterSet(Devanagari) devanagariIrregularRaVowelCharacterSet]_block_invoke
+ ___71+[NSCharacterSet(Devanagari) devanagariSubjoinedCaretRakarCharacterSet]_block_invoke
+ ___86+[TypistPathUtilities _extractCenterStemHalfFormStrokesFrom:withTransform:bridgeEndX:]_block_invoke
+ ___block_descriptor_40_e8_32s_e36_v16?0r^{CGPathElement=i^{CGPoint}}8ls32l8
+ _devanagariConsonantCharacterSet.onceToken
+ _devanagariConsonantCharacterSet.set
+ _devanagariIrregularRaVowelCharacterSet.onceToken
+ _devanagariIrregularRaVowelCharacterSet.set
+ _devanagariSubjoinedCaretRakarCharacterSet.onceToken
+ _devanagariSubjoinedCaretRakarCharacterSet.set
+ _kDevanagariHalantString
+ _kDevanagariLeftMatraString
+ _kDevanagariLongUUMatraString
+ _kDevanagariRaString
+ _kDevanagariShortUMatraString
- GCC_except_table80
CStrings:
+ " between keys"
+ " keycap %.2f %.2f %.2f %.2f"
+ "%@ '%@'>'%@'%@ (%@, %@)"
+ "%@_%lu"
+ "'%@' %@ %@ %.2f %.2f"
+ "/var/mobile/Documents/com.apple.Typist/HostRotation"
+ "/var/mobile/Library/Keyboard"
+ ": "
+ "; "
+ "AutocorrectionRejections"
+ "Filters"
+ "Typology"
+ "Ubiquity"
+ "VulgarWordUsage"
+ "[ROTATION]: The host did not acknowledge a turn to device orientation %d within %.0f seconds"
+ "acknowledgement.json"
+ "deviceOrientation"
+ "id"
+ "ignoresPlaneChecks"
+ "index"
+ "injectLearningDictionaryFiles: Copying the given lm and dat files into %@"
+ "inside"
+ "keyplane geometry [%@]: %@"
+ "landed"
+ "request.json"
+ "resetLearningDictionary: Removing lm and dat files inside %@"
+ "shapestore"
+ "tap landings: %lu taps, %lu off their key%@%@"
+ "textIndex"
+ "user_model_database"
+ "v16@?0r^{CGPathElement=i^{CGPoint}}8"
+ "कखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहळ"
+ "टठडढछङळ"
+ "ु"
+ "ुू"
+ "ू"
- "ि_%lu"
```
