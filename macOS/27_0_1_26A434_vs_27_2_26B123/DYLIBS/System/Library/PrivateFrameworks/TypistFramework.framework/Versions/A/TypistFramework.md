## TypistFramework

> `/System/Library/PrivateFrameworks/TypistFramework.framework/Versions/A/TypistFramework`

```diff

-493.0.0.0.0
-  __TEXT.__text: 0x11e8c
-  __TEXT.__objc_methlist: 0x1404
-  __TEXT.__const: 0x1c2
-  __TEXT.__gcc_except_tab: 0x1fc
+501.0.0.0.0
+  __TEXT.__text: 0x132fc
+  __TEXT.__objc_methlist: 0x1594
+  __TEXT.__const: 0x272
+  __TEXT.__ustring: 0xaa0
   __TEXT.__cstring: 0x2a72
-  __TEXT.__ustring: 0xa18
+  __TEXT.__gcc_except_tab: 0x1fc
   __TEXT.__oslogstring: 0xc
   __TEXT.__swift5_typeref: 0xaa
   __TEXT.__constg_swiftt: 0xb0

   __TEXT.__swift5_fieldmd: 0x94
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0x480
+  __TEXT.__unwind_info: 0x4a8
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xe8
-  __DATA_CONST.__objc_classlist: 0xb0
+  __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe98
+  __DATA_CONST.__objc_selrefs: 0xf90
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x1fa0
   __DATA_CONST.__got: 0x1e0
-  __AUTH_CONST.__const: 0x788
-  __AUTH_CONST.__cfstring: 0x9b80
-  __AUTH_CONST.__objc_const: 0x2250
-  __AUTH_CONST.__objc_doubleobj: 0x50
+  __AUTH_CONST.__const: 0x8e8
+  __AUTH_CONST.__cfstring: 0x9cc0
+  __AUTH_CONST.__objc_const: 0x2310
   __AUTH_CONST.__objc_intobj: 0x1308
-  __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__auth_got: 0x410
+  __AUTH_CONST.__objc_dictobj: 0x78
+  __AUTH_CONST.__objc_doubleobj: 0x50
+  __AUTH_CONST.__auth_got: 0x430
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x548
+  __AUTH.__objc_data: 0x598
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x138
+  __DATA.__objc_ivar: 0x13c
   __DATA.__data: 0x1e0
-  __DATA.__bss: 0x1b0
+  __DATA.__bss: 0x260
   __DATA_DIRTY.__objc_data: 0x1b8
   __DATA_DIRTY.__bss: 0x58
   - /System/Library/Frameworks/Carbon.framework/Versions/A/Carbon

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 505
-  Symbols:   1253
-  CStrings:  1270
+  Functions: 559
+  Symbols:   1340
+  CStrings:  1280
 
Symbols:
+ +[NSCharacterSet(Devanagari) bottomMarkCharacterSet]
+ +[NSCharacterSet(Devanagari) centerStemConsonantCharacterSet]
+ +[NSCharacterSet(Devanagari) devanagariCharacterSet]
+ +[NSCharacterSet(Devanagari) halantCharacterSet]
+ +[NSCharacterSet(Devanagari) khariPaiConsonantCharacterSet]
+ +[NSCharacterSet(Devanagari) leftMatraCharacterSet]
+ +[NSCharacterSet(Devanagari) openTopCharacterSet]
+ +[NSCharacterSet(Devanagari) raCharacterSet]
+ +[NSCharacterSet(Devanagari) rightMatraCharacterSet]
+ +[NSCharacterSet(Devanagari) roundedConsonantCharacterSet]
+ +[NSCharacterSet(Devanagari) topMarkCharacterSet]
+ +[TypistDevanagariSyllable isCenterStemConsonant:]
+ +[TypistDevanagariSyllable isDevanagariCharacter:]
+ +[TypistDevanagariSyllable isHalant:]
+ +[TypistDevanagariSyllable isKhariPaiConsonant:]
+ +[TypistDevanagariSyllable isOpenTopCharacter:]
+ +[TypistDevanagariSyllable isRa:]
+ +[TypistDevanagariSyllable isRoundedConsonant:]
+ +[TypistKeyboardUtilities(MathUtilities) _clampedThumbLengthCM:]
+ +[TypistKeyboardUtilities(MathUtilities) generatePerimeterPointWithCenter:bounds:offset:]
+ +[TypistKeyboardUtilities(MathUtilities) generateThumbArcPointForKeyCenter:reference:errorScale:overextensionRate:crampingRate:millimetresPerPoint:]
+ +[TypistKeyboardUtilities(MathUtilities) generateThumbReachPointForKeyCenter:reference:errorScale:millimetresPerPoint:]
+ +[TypistKeyboardUtilities(MathUtilities) generateTwoThumbArcPointForKeyCenter:leftReference:rightReference:errorScale:overextensionRate:crampingRate:millimetresPerPoint:]
+ +[TypistKeyboardUtilities(MathUtilities) thumbArcBaseSigmaMMForBaseErrorMM:lengthCM:]
+ +[TypistKeyboardUtilities(MathUtilities) thumbArcTuningForTwoHanded:baseErrorMM:overextensionRate:crampingRate:]
+ +[TypistKeyboardUtilities(MathUtilities) thumbBaseSigmaMMForLengthCM:]
+ +[TypistKeyboardUtilities(MathUtilities) thumbReachRadiusMMForLengthCM:]
+ +[TypistKeyboardUtilities(MathUtilities) thumbReachReferenceForLengthCM:anchor:isRightThumb:]
+ +[TypistKeyboardUtilities(MathUtilities) validateTouchPoint:withinBounds:]
+ -[TYPathData anchorX]
+ -[TYPathData initWithArray:width:height:isCursive:advanceWidth:anchorX:]
+ -[TYPathData setAnchorX:]
+ -[TypistHWKeyboard senderProperties]
+ -[TypistHWKeyboard setSenderProperties:]
+ OBJC_IVAR_$_TYPathData._anchorX
+ OBJC_IVAR_$_TypistHWKeyboard._senderProperties
+ _OBJC_CLASS_$_TypistDevanagariSyllable
+ _OBJC_METACLASS_$_TypistDevanagariSyllable
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSString_$_ArabicFormConverter
+ __OBJC_$_CATEGORY_NSCharacterSet_$_Arabic
+ __OBJC_$_CATEGORY_NSString_$_ArabicFormConverter
+ __OBJC_$_CLASS_METHODS_NSCharacterSet(Arabic|Cursive|Devanagari|Hangul|Latex)
+ __OBJC_$_CLASS_METHODS_TypistDevanagariSyllable
+ __OBJC_$_CLASS_METHODS_TypistKeyboardUtilities(KeyboardSettings|MathUtilities|RecapUtilities)
+ __OBJC_$_INSTANCE_METHODS_NSString(ArabicFormConverter|TYTextDirectionAnnotations|Grapheme)
+ __OBJC_CLASS_RO_$_TypistDevanagariSyllable
+ __OBJC_METACLASS_RO_$_TypistDevanagariSyllable
+ ___44+[NSCharacterSet(Devanagari) raCharacterSet]_block_invoke
+ ___48+[NSCharacterSet(Devanagari) halantCharacterSet]_block_invoke
+ ___49+[NSCharacterSet(Devanagari) openTopCharacterSet]_block_invoke
+ ___49+[NSCharacterSet(Devanagari) topMarkCharacterSet]_block_invoke
+ ___51+[NSCharacterSet(Devanagari) leftMatraCharacterSet]_block_invoke
+ ___52+[NSCharacterSet(Devanagari) bottomMarkCharacterSet]_block_invoke
+ ___52+[NSCharacterSet(Devanagari) devanagariCharacterSet]_block_invoke
+ ___52+[NSCharacterSet(Devanagari) rightMatraCharacterSet]_block_invoke
+ ___58+[NSCharacterSet(Devanagari) roundedConsonantCharacterSet]_block_invoke
+ ___59+[NSCharacterSet(Devanagari) khariPaiConsonantCharacterSet]_block_invoke
+ ___61+[NSCharacterSet(Devanagari) centerStemConsonantCharacterSet]_block_invoke
+ ___sincos_stret
+ _atan2
+ _hypot
+ _objc_msgSend$_clampedThumbLengthCM:
+ _objc_msgSend$centerStemConsonantCharacterSet
+ _objc_msgSend$generateGaussianPointWithMean:andSigma:
+ _objc_msgSend$generateThumbArcPointForKeyCenter:reference:errorScale:overextensionRate:crampingRate:millimetresPerPoint:
+ _objc_msgSend$halantCharacterSet
+ _objc_msgSend$initWithArray:width:height:isCursive:advanceWidth:anchorX:
+ _objc_msgSend$khariPaiConsonantCharacterSet
+ _objc_msgSend$openTopCharacterSet
+ _objc_msgSend$raCharacterSet
+ _objc_msgSend$roundedConsonantCharacterSet
+ _objc_msgSend$senderProperties
+ _objc_msgSend$setAnchorX:
+ _objc_msgSend$thumbBaseSigmaMMForLengthCM:
+ _objc_msgSend$thumbReachRadiusMMForLengthCM:
+ _sin
+ bottomMarkCharacterSet.onceToken
+ bottomMarkCharacterSet.set
+ centerStemConsonantCharacterSet.onceToken
+ centerStemConsonantCharacterSet.set
+ devanagariCharacterSet.onceToken
+ devanagariCharacterSet.set
+ halantCharacterSet.onceToken
+ halantCharacterSet.set
+ khariPaiConsonantCharacterSet.onceToken
+ khariPaiConsonantCharacterSet.set
+ leftMatraCharacterSet.onceToken
+ leftMatraCharacterSet.set
+ openTopCharacterSet.onceToken
+ openTopCharacterSet.set
+ raCharacterSet.onceToken
+ raCharacterSet.set
+ rightMatraCharacterSet.onceToken
+ rightMatraCharacterSet.set
+ roundedConsonantCharacterSet.onceToken
+ roundedConsonantCharacterSet.set
+ topMarkCharacterSet.onceToken
+ topMarkCharacterSet.set
- -[TypistHWKeyboard propertyDictionary]
- -[TypistHWKeyboard setPropertyDictionary:]
- OBJC_IVAR_$_TypistHWKeyboard._propertyDictionary
- __OBJC_$_CATEGORY_NSCharacterSet_$_Cursive
- __OBJC_$_CATEGORY_NSString_$_TYTextDirectionAnnotations
- __OBJC_$_CLASS_METHODS_NSCharacterSet(Cursive|Arabic|Latex|Hangul)
- __OBJC_$_CLASS_METHODS_NSString(TYTextDirectionAnnotations|Grapheme|ArabicFormConverter)
- __OBJC_$_CLASS_METHODS_TypistKeyboardUtilities(MathUtilities|RecapUtilities|KeyboardSettings)
- __OBJC_$_INSTANCE_METHODS_NSString(TYTextDirectionAnnotations|Grapheme|ArabicFormConverter)
- _objc_msgSend$propertyDictionary
- _objc_msgSend$setPropertyDictionary:
CStrings:
+ "कफ"
+ "खगघचजझञणतथधनपबभमयलवशषस"
+ "टठडढदछह"
+ "धभथझशअआओऔ"
+ "र"
+ "ाीोौॉ"
+ "ि"
+ "ुूृ़्"
+ "ेैॅंँ"
+ "्"
```
