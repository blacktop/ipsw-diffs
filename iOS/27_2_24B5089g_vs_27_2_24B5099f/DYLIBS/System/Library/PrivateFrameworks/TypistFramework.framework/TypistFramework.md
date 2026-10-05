## TypistFramework

> `/System/Library/PrivateFrameworks/TypistFramework.framework/TypistFramework`

```diff

-499.1.0.0.0
-  __TEXT.__text: 0x425a4
-  __TEXT.__objc_methlist: 0x3a2c
-  __TEXT.__const: 0x422
+501.0.0.0.0
+  __TEXT.__text: 0x432e4
+  __TEXT.__objc_methlist: 0x3b04
+  __TEXT.__const: 0x462
   __TEXT.__ustring: 0x13ea
-  __TEXT.__cstring: 0x5ac2
+  __TEXT.__cstring: 0x5c72
   __TEXT.__gcc_except_tab: 0xd34
   __TEXT.__dlopen_cstrs: 0x6d
   __TEXT.__oslogstring: 0xc

   __TEXT.__swift5_fieldmd: 0x94
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0x11a0
+  __TEXT.__unwind_info: 0x11c8
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x25d0
+  __DATA_CONST.__objc_selrefs: 0x2660
   __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__objc_arraydata: 0x3c18
-  __DATA_CONST.__got: 0x538
+  __DATA_CONST.__got: 0x540
   __AUTH_CONST.__const: 0x788
-  __AUTH_CONST.__cfstring: 0x11820
-  __AUTH_CONST.__objc_const: 0x4be8
+  __AUTH_CONST.__cfstring: 0x11920
+  __AUTH_CONST.__objc_const: 0x4ca8
   __AUTH_CONST.__objc_intobj: 0xbb8
   __AUTH_CONST.__objc_arrayobj: 0x390
   __AUTH_CONST.__objc_dictobj: 0x3e8
   __AUTH_CONST.__objc_doubleobj: 0xa0
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH_CONST.__auth_got: 0x6f8
+  __AUTH_CONST.__auth_got: 0x700
   __AUTH.__objc_data: 0xe08
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x2c8
+  __DATA.__objc_ivar: 0x2d8
   __DATA.__data: 0x1e8
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x1b8

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 1379
-  Symbols:   2377
-  CStrings:  2295
+  Functions: 1397
+  Symbols:   2400
+  CStrings:  2303
 
Symbols:
+ +[TypistKeyboardUtilities(MathUtilities) generateThumbArcPointForKeyCenter:reference:errorScale:overextensionRate:crampingRate:millimetresPerPoint:]
+ +[TypistKeyboardUtilities(MathUtilities) generateTwoThumbArcPointForKeyCenter:leftReference:rightReference:errorScale:overextensionRate:crampingRate:millimetresPerPoint:]
+ +[TypistKeyboardUtilities(MathUtilities) thumbArcBaseSigmaMMForBaseErrorMM:lengthCM:]
+ +[TypistKeyboardUtilities(MathUtilities) thumbArcTuningForTwoHanded:baseErrorMM:overextensionRate:crampingRate:]
+ -[TYPathData anchorX]
+ -[TYPathData initWithArray:width:height:isCursive:advanceWidth:anchorX:]
+ -[TYPathData setAnchorX:]
+ -[TypistKeyboard _isBothThumbsOption:]
+ -[TypistKeyboard _isTwoHandedPosture]
+ -[TypistKeyboard _resolvedThumbArcTuning]
+ -[TypistKeyboard _thumbArcReferenceForRightThumb:twoHanded:]
+ -[TypistKeyboard _thumbReferenceForRightThumb:twoHanded:]
+ -[TypistKeyboard setTapThumbArcCrampingRate:]
+ -[TypistKeyboard setTapThumbArcOverextensionRate:]
+ -[TypistKeyboard setTapThumbBaseErrorMM:]
+ -[TypistKeyboard tapThumbArcCrampingRate]
+ -[TypistKeyboard tapThumbArcOverextensionRate]
+ -[TypistKeyboard tapThumbBaseErrorMM]
+ GCC_except_table94
+ _OBJC_IVAR_$_TYPathData._anchorX
+ _OBJC_IVAR_$_TypistKeyboard._tapThumbArcCrampingRate
+ _OBJC_IVAR_$_TypistKeyboard._tapThumbArcOverextensionRate
+ _OBJC_IVAR_$_TypistKeyboard._tapThumbBaseErrorMM
+ _sqlite3_column_double
- GCC_except_table89
CStrings:
+ "/AppleInternal/Library/Frameworks/TypistHandwriting.bundle/strokes.db"
+ "/AppleInternal/Library/Typist/Handwriting/strokes.db"
+ "No readable handwriting stroke database; nothing will be drawn. Searched: %@"
+ "SELECT pathData.pathData, pathData.width, pathData.height, characters.character, pathData.variant_id, pathData.isCursive, pathData.advances, COALESCE(characterAnchors.anchor_x, 0.0) AS anchor_x FROM pathData INNER JOIN characters ON characters.characterid = pathData.character_id LEFT JOIN characterAnchors ON characterAnchors.character_id = characters.characterid"
+ "both"
+ "tapNoiseThumbArcCrampingRate"
+ "tapNoiseThumbArcOverextensionRate"
+ "tapNoiseThumbBaseErrorMM"
+ "thumbArc"
- "SELECT pathData.pathData, pathData.width, pathData.height, characters.character, pathData.variant_id, pathData.isCursive, pathData.advances FROM pathData INNER JOIN characters ON characters.characterid = pathData.character_id"
```
