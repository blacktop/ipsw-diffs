## UIFoundation

> `/System/Library/PrivateFrameworks/UIFoundation.framework/Versions/A/UIFoundation`

```diff

-  __TEXT.__text: 0x145a24
+  __TEXT.__text: 0x145904
   __TEXT.__objc_methlist: 0xd10c
   __TEXT.__const: 0x12e4
   __TEXT.__cstring: 0x17397
   __TEXT.__ustring: 0x31a
-  __TEXT.__gcc_except_tab: 0x3794
+  __TEXT.__gcc_except_tab: 0x3784
   __TEXT.__oslogstring: 0xb
   __TEXT.__dlopen_cstrs: 0x41
   __TEXT.__dof_UIFoundat: 0x2bd

   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x470
   __DATA_CONST.__objc_arraydata: 0xa8
-  __DATA_CONST.__got: 0xab8
+  __DATA_CONST.__got: 0xad8
   __AUTH_CONST.__const: 0x4718
   __AUTH_CONST.__cfstring: 0x10700
   __AUTH_CONST.__objc_const: 0x14e68

   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x13e0
   __AUTH.__objc_data: 0x1630
-  __AUTH.__data: 0x1c8
+  __AUTH.__data: 0x1d0
   __DATA.__objc_ivar: 0x1608
   __DATA.__data: 0x1370
   __DATA.__bss: 0xb58
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x1a90
-  __DATA_DIRTY.__data: 0x461
+  __DATA_DIRTY.__data: 0x459
   __DATA_DIRTY.__bss: 0xa78
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 6118
-  Symbols:   14642
+  Functions: 6119
+  Symbols:   14643
   CStrings:  6036
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__dof_UIFoundat : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Functions:
~ +[NSAttributeDictionary newWithDictionary:] : 952 -> 956
~ -[NSAttributeDictionary __apply:context:] : 156 -> 164
~ -[NSAttributeDictionary newWithKey:object:] : 1184 -> 1188
~ -[NSLayoutManager(NSPrivate) _rectArrayForRange:withinSelectionRange:rangeIsCharRange:singleRectOnly:fullLineRectsOnly:inTextContainer:rectCount:rangeWithinContainer:glyphsDrawOutsideLines:rectArray:rectArrayCapacity:] : 6876 -> 6888
~ -[_NSCachedAttributedString attributesAtIndex:effectiveRange:] : 180 -> 172
~ -[NSATSGlyphStorage setGlyphRange:characterRange:] : 3420 -> 3408
~ -[_NSCachedAttributedString attributesAtIndex:longestEffectiveRange:inRange:] : 268 -> 260
~ -[NSATSGlyphStorage _resolvePositionalStakeGlyphsForLineFragment:lineFragmentRect:minPosition:maxPosition:maxLineFragmentWidth:breakHint:] : 3260 -> 3200
~ -[NSATSLineFragment getTypographicLineHeight:baselineOffset:leading:] : 1308 -> 1292
~ -[NSATSGlyphStorage _collectElasticRangeSurroundingCharacterAtIndex:minimumCharacterIndex:] : 1952 -> 1956
~ -[NSATSLineFragment saveMorphedGlyphs:] : 2504 -> 2516
~ -[NSATSLineFragment saveWithGlyphOrigin:] : 3028 -> 2788
~ -[NSLayoutManager(NSPrivate) _drawGlyphsForGlyphRange:atPoint:] : 12020 -> 12004
~ -[NSATSGlyphStorage getCustomAdvance:forIndex:] : 192 -> 204
~ -[NSATSGlyphStorage childGlyphStorageWithCharacterRange:] : 380 -> 384
~ ___87+[NSAttributedString(NSAttributedStringUIFoundationAdditions) _isAttributedStringAgent]_block_invoke : 68 -> 100
~ _ReadFontTbl : 1204 -> 1216
~ _ReadExpandedColorTbl : 772 -> 784
~ -[NSRTFWriter textFlowWithAttributes:range:] : 260 -> 236
~ -[NSAttributedString(NSAttributedStringUIFoundationAdditions) nextWordFromIndex:forward:] : 2460 -> 2456
~ -[NSATSGlyphStorage createCopy:] : 1232 -> 1228
~ -[NSLayoutManager characterIndexForPoint:inTextContainer:fractionOfDistanceBetweenInsertionPoints:] : 1284 -> 1288
~ -[NSLineFragmentRenderingContext getMaximumAscender:minimumDescender:] : 388 -> 364
~ -[NSLineFragmentRenderingContext initWithTextStorage:runs:glyphOrigin:lineFragmentWidth:elasticWidth:usesScreenFonts:isRTL:applicationFrameworkContext:] : 2636 -> 2608
~ _OUTLINED_FUNCTION_6 : 20 -> 24
~ _OUTLINED_FUNCTION_7 : 16 -> 20
~ _OUTLINED_FUNCTION_8 : 12 -> 16
~ _OUTLINED_FUNCTION_9 : 16 -> 12
~ _OUTLINED_FUNCTION_12 : 20 -> 16
~ _OUTLINED_FUNCTION_13 : 12 -> 20
~ _OUTLINED_FUNCTION_14 : 12 -> 20
~ _OUTLINED_FUNCTION_15 : 16 -> 12
~ _OUTLINED_FUNCTION_16 : 32 -> 12
~ _OUTLINED_FUNCTION_18 : 40 -> 32
~ _OUTLINED_FUNCTION_19 : 12 -> 40
~ _OUTLINED_FUNCTION_22 : 20 -> 12
~ _OUTLINED_FUNCTION_23 : 44 -> 20
~ _OUTLINED_FUNCTION_24 : 16 -> 44
~ _OUTLINED_FUNCTION_25 : 16 -> 44
~ _OUTLINED_FUNCTION_27 : 16 -> 20
~ _OUTLINED_FUNCTION_28 : 12 -> 16
~ _OUTLINED_FUNCTION_29 : 40 -> 16
~ _OUTLINED_FUNCTION_30 : 40 -> 16
~ _OUTLINED_FUNCTION_32 : 32 -> 12
~ _OUTLINED_FUNCTION_33 : 12 -> 40
~ _OUTLINED_FUNCTION_34 : 12 -> 40
~ _OUTLINED_FUNCTION_36 : 16 -> 12
~ _OUTLINED_FUNCTION_37 : 16 -> 32
~ _OUTLINED_FUNCTION_38 : 16 -> 12
~ _OUTLINED_FUNCTION_39 : 16 -> 12
~ _OUTLINED_FUNCTION_40 : 16 -> 12
~ _OUTLINED_FUNCTION_42 : 40 -> 16
~ _OUTLINED_FUNCTION_43 : 12 -> 16
~ _OUTLINED_FUNCTION_44 : 12 -> 16
~ _OUTLINED_FUNCTION_46 : 28 -> 12
~ _OUTLINED_FUNCTION_47 : 36 -> 12
~ _OUTLINED_FUNCTION_48 : 36 -> 28
~ _OUTLINED_FUNCTION_50 : 20 -> 36
~ _OUTLINED_FUNCTION_51 : 20 -> 36
~ _OUTLINED_FUNCTION_52 : 12 -> 36
~ _OUTLINED_FUNCTION_53 : 20 -> 36
~ _OUTLINED_FUNCTION_57 : 12 -> 20
~ _OUTLINED_FUNCTION_58 : 12 -> 20
~ _OUTLINED_FUNCTION_60 : 20 -> 12
~ _OUTLINED_FUNCTION_64 : 20 -> 12
~ _OUTLINED_FUNCTION_66 : 32 -> 12
~ _OUTLINED_FUNCTION_67 : 32 -> 12
~ _OUTLINED_FUNCTION_68 : 12 -> 32
+ _OUTLINED_FUNCTION_69
~ -[NSConcreteGlyphGenerator generateGlyphsForGlyphStorage:desiredNumberOfCharacters:glyphIndex:characterIndex:] : 3612 -> 3608
~ -[NSLayoutManager(NSPrivate) _selectionRangesForInsertionPointRange:] : 1044 -> 1048
~ __NSReadAttributedStringFromURLOrDataCommon : 13112 -> 13052
~ +[NSParagraphArbitrator _lineBreakStyleForFont:] : 316 -> 324
~ -[__NSTextSelectionLineFragmentInfo _resolveTrailingEdges] : 1156 -> 1172
~ ___NSRunCopyStringCallback : 144 -> 140
~ -[_NSOptimalLineBreaker _calculateFirstFitWrapping] : 568 -> 608

```
