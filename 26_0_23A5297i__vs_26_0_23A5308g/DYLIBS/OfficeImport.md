## OfficeImport

> `/System/Library/PrivateFrameworks/OfficeImport.framework/OfficeImport`

```diff

 310.0.0.0.0
-  __TEXT.__text: 0x427bf0
+  __TEXT.__text: 0x427a30
   __TEXT.__auth_stubs: 0x2d10
   __TEXT.__objc_methlist: 0x373dc
   __TEXT.__const: 0x1679a
-  __TEXT.__gcc_except_tab: 0x520a4
+  __TEXT.__gcc_except_tab: 0x52054
   __TEXT.__cstring: 0x24f73
   __TEXT.__ustring: 0x9f8
-  __TEXT.__unwind_info: 0x1c6d8
+  __TEXT.__unwind_info: 0x1c6d0
   __TEXT.__objc_classname: 0x6dae
   __TEXT.__objc_methname: 0x5549d
   __TEXT.__objc_methtype: 0x14cdc
   __TEXT.__objc_stubs: 0x452c0
-  __DATA_CONST.__got: 0xc38
+  __DATA_CONST.__got: 0xc30
   __DATA_CONST.__const: 0x82a8
   __DATA_CONST.__objc_classlist: 0x2fd8
   __DATA_CONST.__objc_catlist: 0x110

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 17962925-BB2A-377D-B118-71340CCA5CC6
+  UUID: 77C6BEAB-52EF-3AD9-9233-112127AA6B69
   Functions: 29340
-  Symbols:   94686
+  Symbols:   94684
   CStrings:  32260
 
Symbols:
- _xmlFree
Functions:
~ __Z11CXBoolValueP8_xmlAttr : 152 -> 140
~ __Z19CXUnsignedLongValueP8_xmlAttr : 148 -> 136
~ _sfaxmlGetNSStringAnyNsProp : 160 -> 128
~ _sfaxmlGetBoolAnyNsProp : 120 -> 108
~ __Z13CXDoubleValueP8_xmlAttr : 152 -> 140
~ -[NSString(TCStringAdditions_XmlString) tc_initWithValueOfXmlAttribute:] : 204 -> 196
~ -[NSString(TCStringAdditions_XmlString) tc_initWithContentOfXmlNode:] : 148 -> 132
~ -[NSString(TCStringAdditions_XmlString) tc_initFromXmlNode:ns:attributeName:] : 144 -> 128
~ __Z19CXRequiredLongChildP8_xmlNodeP11CXNamespacePKc6CXUnit : 88 -> 76
~ __Z11CXLongValueP8_xmlAttr6CXUnit : 156 -> 144
~ -[TCXmlEnumMap readFromNode:ns:name:value:] : 220 -> 204
~ +[CXNamespace isPrefixSupportedFromNodeContext:prefix:] : 168 -> 156
~ +[ODXData(Private) readPointTypeFromNode:] : 316 -> 304
~ +[ODXData(Private) readConnectionTypeFromNode:] : 208 -> 196
~ __ZL41pOCXReplaceAlternateContentChildrenOfNodeP8_xmlNode : 688 -> 676
~ __Z28OCXReplaceChoiceWithFallbackP8_xmlNode : 140 -> 128
~ -[OCPPackageRelationship(OCPPrivate) readFromElement:baseLocation:] : 648 -> 640
~ __Z11OCXReadBoolP8_xmlNodePKhPKcb : 88 -> 76
~ +[EXRow readRowsFrom:state:] : 1260 -> 1248
~ +[EXRow(Private) edRowFrom:edRowInfo:edRowBlock:edRowBlocks:state:] : 940 -> 908
~ +[EXWorksheet readDistinctSheetElementsFrom:state:] : 664 -> 652
~ +[WXCharacterRun readFrom:to:] : 512 -> 488
~ +[WXDocument(Private) readDocumentSettings:to:state:] : 3444 -> 3412
~ +[WXFieldMarker readFrom:to:] : 396 -> 384
~ +[WXSection(Private) mapHeader:toSection:state:] : 1160 -> 1148
~ +[WXSection(Private) mapFooter:toSection:state:] : 1160 -> 1148
~ +[WXSymbol readFrom:parentRElement:to:state:] : 588 -> 576
~ +[WXSymbol readFrom:to:state:] : 476 -> 464
~ +[WXTableCellProperties readFrom:to:state:] : 2912 -> 2900
~ +[PXOfficeArtClient(Private) readPlaceholderBoundsTrackFromNode:] : 136 -> 124
~ -[OISpotlightImporter textFromElementsNamed:skippingElementsNamed:insertingNewlinesOnElementsNamed:tabulationsOnElementsNamed:inNamespaces:inPackagePart:] : 664 -> 652

```
