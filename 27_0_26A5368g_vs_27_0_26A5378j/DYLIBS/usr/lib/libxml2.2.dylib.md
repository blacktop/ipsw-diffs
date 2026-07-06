## libxml2.2.dylib

> `/usr/lib/libxml2.2.dylib`

```diff

-  __TEXT.__text: 0xc6d38
+  __TEXT.__text: 0xc672c
   __TEXT.__cstring: 0x19c1e
   __TEXT.__const: 0x3890
   __TEXT.__oslogstring: 0xa2
-  __TEXT.__unwind_info: 0x1b90
+  __TEXT.__unwind_info: 0x1b98
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x7b88
   __DATA_CONST.__got: 0x0
Sections:
~ __TEXT.__cstring : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__data : content changed
Functions:
~ _xmlParseGetLasts : 288 -> 308
~ _xmlParsePubidLiteral : 740 -> 744
~ _xmlParseStartTag2 : 3944 -> 3948
~ _xmlParseAttValueInternal : 3600 -> 3508
~ _xmlParse3986URIReference : 1356 -> 1360
~ _nsPush : 360 -> 364
~ _xmlGetNamespace : 100 -> 104
~ _xmlParseEndTag2 : 804 -> 812
~ _xmlCopyCharMultiByte : 264 -> 272
~ _xmlStrQEqual : 160 -> 152
~ _xmlParseXMLDecl : 800 -> 788
~ _xmlGetPropNodeInternal : 628 -> 612
~ _xmlEncodeSpecialChars : 472 -> 464
~ _xmlBufWriteQuotedString : 376 -> 380
~ _xmlStrchr : 52 -> 36
~ _xmlInitializeCatalog : 440 -> 420
~ _xmlStrcasestr : 220 -> 216
~ _xmlC11NNormalizeString : 580 -> 572
~ _xmlParseSGMLCatalog : 1444 -> 1400
~ _xmlLoadCatalogs : 224 -> 216
~ _xmlParseSGMLCatalogName : 392 -> 364
~ _xmlShell : 5192 -> 5184
~ _xmlAddEncodingAlias : 480 -> 492
~ _xmlDelEncodingAlias : 200 -> 212
~ _UTF8ToUTF16LE : 404 -> 392
~ _UTF8ToUTF16BE : 448 -> 436
~ _UTF8Toascii : 340 -> 328
~ _xmlEncodeEntitiesInternal : 1524 -> 1516
~ _xmlParserPrintFileContextInternal : 428 -> 416
~ _UTF8ToHtml : 636 -> 632
~ _htmlParseHTMLAttribute : 1056 -> 1048
~ _htmlParseEndTag : 1040 -> 1044
~ _xmlNanoFTPReadResponse : 588 -> 576
~ _xmlNanoFTPGetConnection : 1032 -> 1036
~ _xmlNanoFTPList : 2340 -> 2188
~ _xmlNanoHTTPMethodRedir : 2768 -> 2756
~ _xmlCheckLanguageID : 572 -> 592
~ _xmlParseCatalogPI : 484 -> 476
~ _xmlAttrNormalizeSpace : 92 -> 76
~ _xmlParseTextDecl : 560 -> 548
~ _xmlPatterncompile : 2992 -> 2920
~ _xmlStreamCtxtAddState : 288 -> 284
~ _xmlCompileStepPattern : 1348 -> 1340
~ _xmlCompileAttributeTest : 804 -> 796
~ _xmlPatScanNCName : 628 -> 616
~ _xmlPatScanName : 644 -> 632
~ _xmlRelaxNGComputeInterleaves : 1040 -> 1032
~ _xmlRelaxNGNormalize : 292 -> 280
~ _xmlRelaxNGNormExtSpace : 300 -> 276
~ _xmlRelaxNGValidateValue : 1284 -> 1288
~ _xmlValidateQName : 1492 -> 1500
~ _xmlStringLenGetNodeList : 1276 -> 1296
~ _xmlReconciliateNs : 616 -> 624
~ _xmlBufferWriteQuotedString : 444 -> 448
~ _xmlDOMWrapRemoveNode : 480 -> 476
~ _xmlDOMWrapReconcileNamespaces : 1200 -> 1196
~ _xmlSaveUri : 2696 -> 2624
~ _xmlNormalizeURIPath : 572 -> 528
~ _xmlURIEscapeStr : 604 -> 588
~ _xmlBuildRelativeURI : 968 -> 960
~ _xmlValidNormalizeString : 92 -> 80
~ _xmlValidateAttributeValue2 : 604 -> 576
~ _xmlWalkValidateList : 640 -> 608
~ _xmlXIncludeDoProcess : 7368 -> 7380
~ _xmlRegStrEqualWildcard : 168 -> 144
~ _xmlRegCopyAtom : 344 -> 364
~ _xmlSchemaVCheckCVCSimpleType : 1968 -> 1908
~ _xmlSchemaPValAttrBlockFinal : 620 -> 628
~ _xmlSchemaParseWildcardNs : 820 -> 828
~ _xmlSchemaParseUnion : 1108 -> 1104
~ _xmlSchemaValidateElem : 3476 -> 3532
~ _xmlSchemaComplexTypeErr : 756 -> 748
~ _xmlSchemaWhiteSpaceReplace : 188 -> 148
~ _xmlSchemaCollapseString : 456 -> 460
~ _xmlSchemaValAtomicType : 8700 -> 8612
~ _xmlSchemaValAtomicListNode : 384 -> 396
~ _xmlSchemaStrip : 280 -> 256
~ _xmlSchemaCompareNormStrings : 424 -> 396
~ _xmlSchemaNormLen : 284 -> 276
~ _xmlStrstr : 188 -> 184
~ _xmlEscapeFormatString : 268 -> 280
~ _xmlXPathNsLookup : 208 -> 220
~ _xmlXPathCastNumberToString : 972 -> 928
~ _xmlXPathStringEvalNumber : 608 -> 612
~ _xmlXPathGetElementsByIds : 344 -> 332
~ _xmlXPathNormalizeFunction : 588 -> 576
~ _xmlXPathCompileExpr : 524 -> 496
~ _xmlXPathEscapeUriFunction : 680 -> 672
~ _xmlXPathCompAndExpr : 336 -> 308
~ _xmlXPathCompEqualityExpr : 400 -> 356
~ _xmlXPathCompRelationalExpr : 364 -> 332
~ _xmlXPathCompAdditiveExpr : 324 -> 296
~ _xmlXPathCompMultiplicativeExpr : 412 -> 384
~ _xmlXPathCompUnaryExpr : 588 -> 552
~ _xmlXPathCompPathExpr : 3980 -> 3856
~ _xmlXPathCompRelativeLocationPath : 584 -> 540
~ _xmlXPathCompPredicate : 380 -> 368
~ _xmlXPathCompStep : 2600 -> 2508
~ _xmlXPtrEval : 1764 -> 1716
~ _xmlXPtrEvalRangePredicate : 692 -> 680
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.PbE6l6/Sources/libxml2/libxml2/relaxng.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.PbE6l6/Sources/libxml2/libxml2/schematron.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.PbE6l6/Sources/libxml2/libxml2/xmlreader.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.PbE6l6/Sources/libxml2/libxml2/xmlregexp.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.PbE6l6/Sources/libxml2/libxml2/xmlschemas.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.PbE6l6/Sources/libxml2/libxml2/xmlschemastypes.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.PbE6l6/Sources/libxml2/libxml2/xpath.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.PbE6l6/Sources/libxml2/libxml2/xpointer.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HgcvOu/Sources/libxml2/libxml2/relaxng.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HgcvOu/Sources/libxml2/libxml2/schematron.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HgcvOu/Sources/libxml2/libxml2/xmlreader.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HgcvOu/Sources/libxml2/libxml2/xmlregexp.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HgcvOu/Sources/libxml2/libxml2/xmlschemas.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HgcvOu/Sources/libxml2/libxml2/xmlschemastypes.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HgcvOu/Sources/libxml2/libxml2/xpath.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HgcvOu/Sources/libxml2/libxml2/xpointer.c"

```
