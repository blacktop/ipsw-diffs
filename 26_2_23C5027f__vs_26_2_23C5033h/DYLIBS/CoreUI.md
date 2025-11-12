## CoreUI

> `/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`

```diff

-971.6.0.0.0
-  __TEXT.__text: 0xca1d8
+972.0.0.0.0
+  __TEXT.__text: 0xca248
   __TEXT.__auth_stubs: 0x2c10
   __TEXT.__delay_stubs: 0x2c
   __TEXT.__delay_helper: 0xa4

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: CE0B0852-5A42-3F72-BE6C-891525243838
+  UUID: 0DE42402-C03E-34C7-A518-84FBBEAC7DC7
   Functions: 5313
   Symbols:   15868
   CStrings:  12119
Functions:
~ -[_CUIThemeColorRendition cgColor] : 216 -> 232
~ _OUTLINED_FUNCTION_19 : 20 -> 16
~ -[CSIBitmapWrapper destImage] : 72 -> 68
~ -[CUINamedVectorGlyph multicolorLayerGroup] : 252 -> 248
~ -[CUINamedVectorGlyph hierarchicalLayerGroup] : 252 -> 248
~ +[CUINamedVectorGlyph _createSCurveGradientWithStartColor:endColor:height:] : 524 -> 540
~ __ZNSt3__16vectorI15CPSDLayerRecordNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJS1_EEEPS1_DpOT_ : 328 -> 332
~ __ZNSt3__16vectorI23CPSDChannelBlendingInfoNS_9allocatorIS1_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNSt3__16vectorI21CPSDChannelLengthInfoNS_9allocatorIS1_EEE8__appendEm : 436 -> 444
~ __ZNSt3__16vectorI10CPSDStringNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_ : 300 -> 312
~ __ZNSt3__16vectorI15CPSDLayerRecordNS_9allocatorIS1_EEE8__appendEm : 392 -> 408
~ __ZNSt3__16vectorI23CPSDChannelBlendingInfoNS_9allocatorIS1_EEE8__appendEm : 428 -> 436
~ __ZNSt3__16vectorI19CPSDActionKeyedItemNS_9allocatorIS1_EEE8__appendEm : 504 -> 512
~ __ZNSt3__16vectorI19CPSDActionKeyedItemNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJS1_EEEPS1_DpOT_ : 408 -> 412
~ __ZN2RB4Path10ClipStroke12_GLOBAL__N_111BisectState9cut_rangeERKNS0_7SubpathEffNSt3__14spanIK24CGPathClipStrokeKeyframeLm18446744073709551615EEEmj : 720 -> 708
~ __ZNK2RB4Path10ClipStroke9Transform10record_capEDv2_dS3_RNSt3__16vectorIjNS4_9allocatorIjEEEE : 368 -> 372
~ +[CUIVectorGlyphMutator createInterpolatedPointsFromPoints:ultralightDeltas:blackDeltas:withScalars:] : 240 -> 260
~ -[CUINamedVectorGlyph _performWithLockedRenditions:] : 268 -> 264
~ -[CUINamedVectorGlyph _drawInContext:scaleFactor:targetSize:primaryColor:tertiaryColor:] : 384 -> 376
~ -[CUINamedVectorGlyph _drawMulticolorLayersInContext:scaleFactor:targetSize:colorResolver:] : 476 -> 480
~ -[CUINamedVectorGlyph _drawHierarchicalLayersInContext:scaleFactor:targetSize:colorResolver:] : 556 -> 560
~ -[CUINamedVectorGlyph _drawPaletteLayersInContext:scaleFactor:targetSize:colorResolver:] : 556 -> 560
~ -[CUINamedImageAtlas _dimension1ExistsInKeyFormatForThemeRef:] : 56 -> 52
~ -[CSIGenerator _shouldUseCompactCompressionForBitmap:] : 152 -> 148
~ -[CSIGenerator _updateCompressionInfoFor:] : 272 -> 284
~ -[CSIGenerator formatCSIHeader:] : 548 -> 544
~ -[CSIGenerator writeRawDataToData:] : 296 -> 292
~ -[CSIGenerator writeRecognitionObjectToData:] : 148 -> 160
~ -[CSIGenerator CSIRepresentationWithCompression:] : 1152 -> 1172
~ -[CUIRuntimeStatistics _logStatistics:] : 244 -> 240
~ -[CUIThemeFacet _initWithRenditionKey:] : 148 -> 144
~ -[CUIThemeFacet _makeLayerFromCAPackageData] : 164 -> 160
~ -[CUIThemeFacet _drawSpecificRenditionKey:inFrame:context:isFocused:focusRingColor:isFlipped:effects:] : 160 -> 156
~ -[CUIThemeFacet _drawSpecificRenditionKey:inFrame:context:alpha:operation:isFocused:focusRingColor:isFlipped:effects:] : 228 -> 224
~ -[CUIThemeFacet _drawMaskFromSpecificRenditionKey:inFrame:alpha:operation:isFocused:focusRingColor:context:] : 184 -> 212
~ -[CUIRenditionKey _expandKeyIfNecessaryForCount:] : 136 -> 132
~ -[CUIRenditionMetrics initwithImageSize:scale:] : 108 -> 104
~ -[CUIRenditionMetrics initWithImageSize:defaultImageSize:edgeBottomLeft:edgeTopRight:contentBottomLeft:contentTopRight:baseline:auxiliary1BottomLeft:auxiliary1TopRight:auxiliary2BottomLeft:auxiliary2TopRight:scalesVertically:scalesHorizontally:scale:] : 252 -> 248
~ -[_CSIRenditionBlockData setRowBytes:] : 132 -> 128

```
