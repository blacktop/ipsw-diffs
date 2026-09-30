## UIFoundation

> `/System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation`

```diff

-1015.6.0.0.0
-  __TEXT.__text: 0x105ac4
+1016.0.0.0.0
+  __TEXT.__text: 0x105a08
   __TEXT.__auth_stubs: 0x25a0
   __TEXT.__objc_methlist: 0xbacc
   __TEXT.__const: 0x73c

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D0C60048-4C0B-3204-898F-8612F9F57395
+  UUID: 64FDD128-71FB-321F-BA69-89E0E46337FD
   Functions: 5257
   Symbols:   17918
   CStrings:  10611
Functions:
~ _OUTLINED_FUNCTION_8 : 48 -> 16
~ _OUTLINED_FUNCTION_13 : 32 -> 24
~ _OUTLINED_FUNCTION_13 : 12 -> 32
~ -[NSRTFReader mutableAttributes] -> _OUTLINED_FUNCTION_13 : 76 -> 12
~ -[NSATSTypesetter _bidiLevels] -> -[NSRTFReader mutableAttributes] : 100 -> 76
~ _OUTLINED_FUNCTION_23 -> -[NSATSTypesetter _bidiLevels] : 12 -> 100
~ -[NSRTFReader _updateAttributes] -> _OUTLINED_FUNCTION_23 : 876 -> 12
~ -[NSATSTypesetter limitsLayoutForSuspiciousContents] -> -[NSRTFReader _updateAttributes] : 68 -> 876
~ _OUTLINED_FUNCTION_7 -> -[NSATSTypesetter limitsLayoutForSuspiciousContents] : 20 -> 68
~ _OUTLINED_FUNCTION_7 : 16 -> 20
~ _OUTLINED_FUNCTION_7 : 40 -> 20
~ _OUTLINED_FUNCTION_7 : 12 -> 40
~ -[NSRTFReader documentAttributes] -> _OUTLINED_FUNCTION_7 : 884 -> 12
~ _OUTLINED_FUNCTION_6 -> -[NSRTFReader documentAttributes] : 20 -> 884
~ _OUTLINED_FUNCTION_6 : 32 -> 20
~ _OUTLINED_FUNCTION_6 : 20 -> 32
~ _OUTLINED_FUNCTION_15 : 20 -> 24
~ -[NSATSGlyphStorage _invalidate] : 100 -> 96
~ -[NSATSGlyphStorage _flushCachedObjects] : 100 -> 108
~ -[NSRTFReader _determineSourceTextScalingType] : 188 -> 184
~ -[NSRTFReader _determineFinalTextScalingType] : 156 -> 152
~ _OUTLINED_FUNCTION_9 : 12 -> 48
~ _OUTLINED_FUNCTION_10 : 28 -> 12
~ _OUTLINED_FUNCTION_11 : 24 -> 28
~ _OUTLINED_FUNCTION_14 -> _OUTLINED_FUNCTION_16 : 24 -> 20
~ -[NSTextContainer lineFragmentRectForProposedRect:atIndex:writingDirection:remainingRect:] : 1524 -> 1420
~ -[_NSOptimalLineBreaker _resetOptions] : 236 -> 232
~ -[_NSOptimalLineBreaker _computeParagraphStyleValues] : 320 -> 316
~ -[_NSOptimalLineBreaker _getNaturalWidth:expand:contract:fromBreak:toBreak:] : 420 -> 416
~ -[_NSOptimalLineBreaker _getMinWidth:maxWidth:whenJustifyingLineFromBreak:toBreak:] : 308 -> 304
~ -[_NSOptimalLineBreaker _breakPenaltyForHyphenationFactor:] : 120 -> 116
~ -[_NSOptimalLineBreaker _demeritFromBreak:toBreak:] : 84 -> 96
~ -[_NSOptimalLineBreaker _lineBreakTokenizer] : 136 -> 132
~ -[_NSOptimalLineBreaker _minimumDemeritForLineEndingAtBreak:withExpansionRatio:] : 128 -> 124
~ -[__NSLMMarkedTextUnderlineRenderer processMarkedTextUnderlineStartX:endX:yPosition:underlineColor:selected:] : 416 -> 412
~ -[NSATSLineFragment layoutForStartingGlyphAtIndex:characterIndex:minPosition:maxPosition:lineFragmentRect:] : 3104 -> 3100
~ -[NSATSLineFragment getTypographicLineHeight:baselineOffset:leading:] : 1228 -> 1224
~ -[NSATSLineFragment justifyWithFactor:] : 160 -> 156
~ -[NSATSLineFragment resolveOpticalAlignmentUpdatingMinPosition:maxPosition:] : 140 -> 136
~ -[NSATSLineFragment _copyRenderingContextWithGlyphOrigin:] : 264 -> 288
~ -[__NSATSStringSegment _setOriginalString:range:] : 244 -> 240
~ -[__NSWritingToolsEdit range] : 76 -> 72
~ -[_NSTextHighlightRun cornerRadius] : 204 -> 200
~ -[_NSTextHighlightRun cornerOutset] : 148 -> 144
~ -[_NSTextHighlightRun getMetricsForTextSize:cornerRadius:cornerOutset:] : 212 -> 208
~ -[_NSTextHighlightRun combinedPaths] : 240 -> 236
~ -[_NSTextHighlightCluster addRunsWithTextRangeArray:] : 96 -> 92
~ -[NSAttributedString _ui_attributedStringScaledByScaleFactor:] : 200 -> 196
~ -[_NSCoreTypesetterLayoutCache setCount:glyphs:advances:elasticAdvances:resolvedFont:textAlignment:] : 232 -> 228
~ -[_NSCoreTypesetterLayoutCache getCount:glyphs:advances:elasticAdvances:resolvedFont:textAlignment:] : 128 -> 124
~ -[_NSCoreTypesetterLayoutCache setCTLine:attachmentLayoutContext:validForDrawing:] : 128 -> 124
~ -[NSTextBlockLayoutHelper initWithTextBlock:charRange:text:layoutManager:containerWidth:collapseBorders:] : 324 -> 320
~ -[NSTextBlockLayoutHelper initWithTextBlock:charIndex:text:layoutManager:containerWidth:collapseBorders:] : 276 -> 272
~ -[NSTextBlockLayoutHelper initWithTextTable:charIndex:text:layoutManager:containerWidth:collapseBorders:] : 276 -> 272
~ -[NSRTFReader _ensureTableCells] : 340 -> 336
~ -[NSRTFReader _beginTableRow] : 184 -> 192
~ -[NSRTFReader _pushTableState] : 212 -> 224
~ -[NSRTFReader _popTableState] : 216 -> 212
~ -[NSRTFReader _setTableCells] : 268 -> 264
~ -[NSRTFReader _clearTableCells] : 72 -> 68
~ -[NSRTFReader _documentInfoDictionary] : 72 -> 68
~ -[NSRTFWriter writeEscapedUTF8String:] : 204 -> 216
~ -[NSRTFWriter _mostCompatibleCharset:] : 416 -> 408
~ -[NSRTFWriter RTFD] : 72 -> 68
~ -[NSRTFWriter RTFDFileWrapper] : 220 -> 232
~ -[NSRTFWriter _setRTFDFileWrapper:] : 64 -> 60
~ -[NSRTFWriter RTF] : 48 -> 44
~ -[NSRTFWriter setDocumentAttributes:] : 660 -> 656
~ -[NSRTFWriter writeHeader] : 144 -> 152
~ -[NSRTFWriter _canWriteColor:] : 96 -> 92
~ -[NSRTFWriter restoreAttributes:] : 944 -> 940
~ -[NSRTFWriter writeCharacterAttributes:previousAttributes:] : 1980 -> 1976
~ -[NSRTFWriter _attachmentData] : 104 -> 100
~ -[NSRTFWriter writeLinkInfo:] : 388 -> 384

```
