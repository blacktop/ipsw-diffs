## PrintKit

> `/System/Library/PrivateFrameworks/PrintKit.framework/PrintKit`

```diff

-319.1.0.0.0
-  __TEXT.__text: 0x4acb0
-  __TEXT.__auth_stubs: 0xb50
+324.0.0.0.0
+  __TEXT.__text: 0x47938
   __TEXT.__objc_methlist: 0x312c
   __TEXT.__const: 0x440
-  __TEXT.__gcc_except_tab: 0x930c
-  __TEXT.__cstring: 0x7cac
+  __TEXT.__gcc_except_tab: 0x8dec
+  __TEXT.__cstring: 0x7ce4
   __TEXT.__oslogstring: 0xef2
-  __TEXT.__unwind_info: 0x2d08
-  __TEXT.__objc_classname: 0x468
-  __TEXT.__objc_methname: 0x69ae
-  __TEXT.__objc_methtype: 0x1002
-  __TEXT.__objc_stubs: 0x55c0
-  __DATA_CONST.__got: 0x2d8
+  __TEXT.__unwind_info: 0x2cd8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xdf68
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_protolist: 0x48

   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x6190
-  __AUTH_CONST.__auth_got: 0x5c0
+  __DATA_CONST.__got: 0x2d8
   __AUTH_CONST.__const: 0xe08
   __AUTH_CONST.__cfstring: 0xd960
   __AUTH_CONST.__objc_const: 0x5478
+  __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x1350
   __AUTH_CONST.__objc_arrayobj: 0x228
-  __AUTH.__data: 0x38
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__data: 0x30
   __DATA.__objc_ivar: 0x324
-  __DATA.__data: 0x2f34
-  __DATA.__bss: 0x174
+  __DATA.__data: 0x2f2c
+  __DATA.__bss: 0x114
   __DATA_DIRTY.__objc_data: 0xf50
+  __DATA_DIRTY.__data: 0x10
+  __DATA_DIRTY.__bss: 0x60
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3E28A547-1088-3051-B87C-2E4AD85BC6EE
+  UUID: F541F533-82BA-38AC-B53C-EE80DEC5E362
   Functions: 1595
-  Symbols:   6041
-  CStrings:  5384
+  Symbols:   6046
+  CStrings:  3798
 
Symbols:
+ ___41-[PKCloudResolveContext _driveResolution]_block_invoke.335
+ ___41-[PKCloudResolveContext _driveResolution]_block_invoke_2.336
+ ____ZL25writeRequestDataToPrinterP17PKPrintJobRequestP6NSDataU13block_pointerFvP8NSNumberE_block_invoke.417
+ ___block_literal_global.102
+ ___block_literal_global.174
+ ___block_literal_global.327
+ ___block_literal_global.398
+ ___block_literal_global.401
+ ___block_literal_global.409
+ ___block_literal_global.55
+ ___block_literal_global.63
+ ___block_literal_global.65
+ ___block_literal_global.67
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x3
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x5
+ _objc_retain_x9
- ___41-[PKCloudResolveContext _driveResolution]_block_invoke.336
- ___41-[PKCloudResolveContext _driveResolution]_block_invoke_2.337
- ____ZL25writeRequestDataToPrinterP17PKPrintJobRequestP6NSDataU13block_pointerFvP8NSNumberE_block_invoke.418
- ___block_literal_global.103
- ___block_literal_global.175
- ___block_literal_global.328
- ___block_literal_global.399
- ___block_literal_global.402
- ___block_literal_global.410
- ___block_literal_global.56
- ___block_literal_global.64
- ___block_literal_global.66
- ___block_literal_global.68
Functions:
~ +[PKPrinterTool_Client sharedClient] : 84 -> 68
~ -[PKPrinterTool_Client ptConn] : 120 -> 112
~ -[PKPrinterTool_Client ptConn_locked] : 644 -> 632
~ ___37-[PKPrinterTool_Client ptConn_locked]_block_invoke : 216 -> 168
~ ___37-[PKPrinterTool_Client ptConn_locked]_block_invoke.4 : 228 -> 172
~ -[PKPrinterTool_Client invalidate] : 144 -> 140
~ -[PKPrinterTool_Client getRecentJobsCompletionHandler:] : 304 -> 300
~ ___55-[PKPrinterTool_Client getRecentJobsCompletionHandler:]_block_invoke : 128 -> 124
~ __ZL13PKLogXPCErrorP13objc_selectorP7NSError : 432 -> 356
~ -[PKPrinterTool_Client getJobUpdateStatus:includeThumbnail:completionHandler:] : 324 -> 320
~ ___78-[PKPrinterTool_Client getJobUpdateStatus:includeThumbnail:completionHandler:]_block_invoke : 124 -> 120
~ -[PKPrinterTool_Client cancelJob:] : 144 -> 136
~ -[PKPrinterTool_Client getLastUsedPrintersForCurrentNetworkCompletionHandler:] : 304 -> 300
~ ___78-[PKPrinterTool_Client getLastUsedPrintersForCurrentNetworkCompletionHandler:]_block_invoke : 128 -> 124
~ -[PKPrinterTool_Client setLastUsedPrintersForCurrentNetwork:] : 176 -> 168
~ -[PKPrinterTool_Client getiCloudPrintersWithCompletionHandler:] : 300 -> 296
~ ___63-[PKPrinterTool_Client getiCloudPrintersWithCompletionHandler:]_block_invoke : 124 -> 120
~ -[PKPrinterTool_Client addPrinterToiCloud:] : 216 -> 204
~ -[PKPrinterTool_Client removePrinterFromiCloud:] : 216 -> 204
~ -[PKPrinterTool_Client updateiCloudPrinter:withInfo:forInfoKey:] : 264 -> 260
~ -[PKPrinterTool_Client setiCloudPrinters:] : 176 -> 168
~ -[PKPrinterTool_Client resetPKCloudData] : 136 -> 128
~ -[PKPrinterTool_Client logiCloudPrintersCompletionHandler:] : 300 -> 296
~ ___59-[PKPrinterTool_Client logiCloudPrintersCompletionHandler:]_block_invoke : 124 -> 120
~ ___71-[PKPrinterTool_Client browseInfoForPrinter:timeout:completionHandler:]_block_invoke : 124 -> 120
~ ___66-[PKPrinterTool_Client endpointResolve:timeout:completionHandler:]_block_invoke : 128 -> 124
~ -[PKPrinterTool_Client printerTool_realPathForTmp:] : 300 -> 296
~ ___51-[PKPrinterTool_Client printerTool_realPathForTmp:]_block_invoke : 124 -> 120
~ -[PKPrinterTool_Client printerTool_removeKeychainItem:] : 176 -> 168
~ ___95-[PKPrinterTool_Client printerTool_getPrinterDescription:assertReachability:completionHandler:]_block_invoke : 128 -> 124
~ ___78-[PKPrinterTool_Client printerTool_queryPrinter:attributes:completionHandler:]_block_invoke : 124 -> 120
~ ___78-[PKPrinterTool_Client printerTool_queryPrinter:attributes:completionHandler:]_block_invoke_2 : 232 -> 228
~ ___71-[PKPrinterTool_Client printerTool_checkAccessState:completionHandler:]_block_invoke : 124 -> 120
~ ___78-[PKPrinterTool_Client startStreamingRequest:printSettings:completionHandler:]_block_invoke : 124 -> 120
~ -[PKPrinterTool_Client finishRequestWithCancel:completionHandler:] : 336 -> 340
~ ___66-[PKPrinterTool_Client finishRequestWithCancel:completionHandler:]_block_invoke : 124 -> 120
~ -[PKPrintdRPC_BrowseClient ptConn_locked] : 332 -> 316
~ -[PKPrintdRPC_BrowseClient startBrowsing] : 144 -> 136
~ __ZN9PrintdRPC18RemoveKeychainItemEP24PKPrinterBonjourEndpoint : 132 -> 128
~ __ZN9PrintdRPC15IdentifyPrinterEP24PKPrinterBonjourEndpointP8NSStringP7NSArrayIS3_E : 184 -> 188
~ __ZN9PrintdRPC27QueryPrinterWithAttributessEP24PKPrinterBonjourEndpointP7NSArrayIP8NSStringEU13block_pointerFvPK17Printd_ParametersE : 184 -> 188
~ __Z12internStringP8NSString : 384 -> 380
~ __ZL17forcedAsciiInternP8NSString : 276 -> 268
~ __ZZZL17internEntriesDictvEUb_EN3$_28__invokeEPKv : 140 -> 136
~ __ZL11entryStringPK10CacheEntry : 96 -> 88
~ __ZZZL17internEntriesDictvEUb_EN3$_78__invokeEPKv : 140 -> 136
~ __Z9ippReadIOPvPFlS_PhmEP8PK_ipp_t : 372 -> 320
~ __ZL17ippReadWithReaderR11IPPIOReaderR11ipp_state_eR9ipp_tag_ebP8PK_ipp_t : 5152 -> 5008
~ __ZN11IPPIOReader4readEPhm : 236 -> 228
~ __ZN11IPPIOReader10THROW_FAILEiP8NSStringS1_ : 392 -> 380
~ __ZN11IPPIOReader10readStringEmb : 264 -> 260
~ __ZN11IPPIOReader9autoAllocEm : 236 -> 228
~ __Z16withNamedAttrGetIbET_P8PK_ipp_tP8NSStringU13block_pointerFS0_P18PK_ipp_attribute_tE : 168 -> 164
~ ____Z12getNamedAttrIbET_P8PK_ipp_tP8NSString_block_invoke : 124 -> 116
~ __Z16withNamedAttrGetIiET_P8PK_ipp_tP8NSStringU13block_pointerFS0_P18PK_ipp_attribute_tE : 168 -> 164
~ ____Z12getNamedAttrIiET_P8PK_ipp_tP8NSString_block_invoke : 124 -> 116
~ __Z12getNamedAttrI12ipp_orient_eET_P8PK_ipp_tP8NSString : 116 -> 120
~ __Z16withNamedAttrGetI17ipp_value_range_tET_P8PK_ipp_tP8NSStringU13block_pointerFS1_P18PK_ipp_attribute_tE : 196 -> 192
~ ____Z12getNamedAttrI17ipp_value_range_tET_P8PK_ipp_tP8NSString_block_invoke : 160 -> 152
~ __Z12getNamedAttrIU8__strongP19PK_ipp_collection_tET_P8PK_ipp_tP8NSString : 56 -> 52
~ __Z16withNamedAttrGetIU8__strongP19PK_ipp_collection_tET_P8PK_ipp_tP8NSStringU13block_pointerFS3_P18PK_ipp_attribute_tE : 192 -> 184
~ ____Z12getNamedAttrIU8__strongP19PK_ipp_collection_tET_P8PK_ipp_tP8NSString_block_invoke : 148 -> 136
~ __Z12getNamedAttrIU8__strongP8NSStringET_P8PK_ipp_tS1_ : 56 -> 52
~ __Z16withNamedAttrGetIU8__strongP8NSStringET_P8PK_ipp_tS1_U13block_pointerFS3_P18PK_ipp_attribute_tE : 192 -> 184
~ ____Z12getNamedAttrIU8__strongP8NSStringET_P8PK_ipp_tS1__block_invoke : 344 -> 328
~ __Z12getNamedAttrIU8__strongP5NSURLET_P8PK_ipp_tP8NSString : 124 -> 116
~ __Z12getNamedAttrIU8__strongP7NSArrayIP8NSStringEET_P8PK_ipp_tS2_ : 56 -> 52
~ __Z16withNamedAttrGetIU8__strongP7NSArrayIP8NSStringEET_P8PK_ipp_tS2_U13block_pointerFS6_P18PK_ipp_attribute_tE : 192 -> 184
~ ____Z12getNamedAttrIU8__strongP7NSArrayIP8NSStringEET_P8PK_ipp_tS2__block_invoke_2 : 156 -> 148
~ __Z12getNamedAttrIU8__strongP7NSArrayIP8NSNumberEET_P8PK_ipp_tP8NSString : 56 -> 52
~ __Z16withNamedAttrGetIU8__strongP7NSArrayIP8NSNumberEET_P8PK_ipp_tP8NSStringU13block_pointerFS6_P18PK_ipp_attribute_tE : 192 -> 184
~ ____Z12getNamedAttrIU8__strongP7NSArrayIP8NSNumberEET_P8PK_ipp_tP8NSString_block_invoke_2 : 164 -> 152
~ __Z12getNamedAttrIU8__strongP7NSArrayIP6NSDataEET_P8PK_ipp_tP8NSString : 248 -> 256
~ __Z16withNamedAttrGetIU8__strongP7NSArrayIP6NSDataEET_P8PK_ipp_tP8NSStringU13block_pointerFS6_P18PK_ipp_attribute_tE : 192 -> 184
~ ____Z12getNamedAttrIU8__strongP7NSArrayIP6NSDataEET_P8PK_ipp_tP8NSString_block_invoke : 480 -> 424
~ ____Z12getNamedAttrIU8__strongP7NSArrayIP6NSDataEET_P8PK_ipp_tP8NSString_block_invoke_2 : 192 -> 176
~ __Z12getNamedAttrIU8__strongP7NSArrayIP19PK_ipp_collection_tEET_P8PK_ipp_tP8NSString : 248 -> 256
~ __Z16withNamedAttrGetIU8__strongP7NSArrayIP19PK_ipp_collection_tEET_P8PK_ipp_tP8NSStringU13block_pointerFS6_P18PK_ipp_attribute_tE : 192 -> 184
~ ____Z12getNamedAttrIU8__strongP7NSArrayIP19PK_ipp_collection_tEET_P8PK_ipp_tP8NSString_block_invoke : 480 -> 424
~ ____Z12getNamedAttrIU8__strongP7NSArrayIP19PK_ipp_collection_tEET_P8PK_ipp_tP8NSString_block_invoke_2 : 192 -> 176
~ __Z12getNamedAttrIU8__strongP11PKMediaSizeET_P8PK_ipp_tP8NSString : 120 -> 116
~ __ZL22getNamedMediaAttrArrayP8PK_ipp_tP8NSStringP10objc_class : 292 -> 284
~ __Z12getNamedAttrIU8__strongP23PKMediaSourcePropertiesET_P8PK_ipp_tP8NSString : 120 -> 116
~ __ZNK17Printd_Parameters43_get_LandscapeOrientationRequestedPreferredEv : 276 -> 220
~ __ZNK17Printd_Parameters26_get_JpegFeaturesSupportedEv : 300 -> 240
~ __ZNK17Printd_Parameters26_get_PrintScalingSupportedEv : 300 -> 240
~ __ZNK17Printd_Parameters34_get_PrinterMandatoryJobAttributesEv : 300 -> 240
~ __ZNK17Printd_Parameters24_get_PrinterStateReasonsEv : 300 -> 240
~ __ZNK17Printd_Parameters20_get_CopiesSupportedEv : 300 -> 244
~ __ZNK17Printd_Parameters25_get_JpegKOctetsSupportedEv : 300 -> 244
~ __ZNK17Printd_Parameters28_get_JpegXDimensionSupportedEv : 300 -> 244
~ __ZNK17Printd_Parameters28_get_JpegYDimensionSupportedEv : 300 -> 244
~ __ZNK17Printd_Parameters24_get_PdfKOctetsSupportedEv : 300 -> 244
~ __ZNK17Printd_Parameters20_get_PrinterDeviceIdEv : 300 -> 240
~ __ZNK17Printd_Parameters25_get_PrinterChargeInfoUriEv : 300 -> 240
~ __ZNK17Printd_Parameters20_get_PrinterMoreInfoEv : 300 -> 240
~ __ZNK17Printd_Parameters25_get_PrinterSupplyInfoURIEv : 300 -> 240
~ __ZNK17Printd_Parameters24_get_JobPresetsSupportedEv : 300 -> 240
~ __ZNK17Printd_Parameters28_get_DocumentFormatSupportedEv : 300 -> 240
~ __ZNK17Printd_Parameters22_get_MediaColSupportedEv : 300 -> 240
~ __ZNK17Printd_Parameters18_get_MediaColReadyEv : 300 -> 240
~ __ZNK17Printd_Parameters21_get_MediaColDatabaseEv : 300 -> 240
~ __ZNK17Printd_Parameters28_get_PrintColorModeSupportedEv : 300 -> 240
~ __ZNK17Printd_Parameters26_get_PrintQualitySupportedEv : 300 -> 240
~ __ZNK17Printd_Parameters19_get_SidesSupportedEv : 300 -> 240
~ __ZNK17Printd_Parameters24_get_FinishingsSupportedEv : 300 -> 240
~ __ZNK17Printd_Parameters26_get_FinishingsColDatabaseEv : 300 -> 240
~ __ZNK17Printd_Parameters21_get_OutputBinDefaultEv : 300 -> 240
~ __ZNK17Printd_Parameters26_get_JobAccountIDSupportedEv : 284 -> 228
~ __ZNK17Printd_Parameters29_get_IdentifyActionsSupportedEv : 300 -> 240
~ __ZNK17Printd_Parameters23_get_MediaTypeSupportedEv : 300 -> 240
~ __ZNK17Printd_Parameters23_get_OutputBinSupportedEv : 300 -> 240
~ __ZNK17Printd_Parameters22_get_PrinterOutputTrayEv : 300 -> 240
~ __ZNK17Printd_Parameters25_get_MediaSourceSupportedEv : 300 -> 240
~ __ZNK17Printd_Parameters21_get_PrinterInputTrayEv : 300 -> 240
~ __ZNK17Printd_Parameters16_get_MarkerNamesEv : 300 -> 240
~ __ZNK17Printd_Parameters17_get_MarkerColorsEv : 300 -> 240
~ __ZNK17Printd_Parameters16_get_MarkerTypesEv : 300 -> 240
~ __ZNK17Printd_Parameters17_get_MarkerLevelsEv : 300 -> 240
~ __ZNK17Printd_Parameters21_get_MarkerHighLevelsEv : 300 -> 240
~ __ZNK17Printd_Parameters20_get_MarkerLowLevelsEv : 300 -> 240
~ __ZNK17Printd_Parameters14_get_MediaSizeEv : 300 -> 240
~ __ZNK17Printd_Parameters26_get_MediaSourcePropertiesEv : 300 -> 240
~ __ZNK17Printd_Parameters16_get_MediaSourceEv : 300 -> 240
~ __ZNK17Printd_Parameters14_get_MediaTypeEv : 300 -> 240
~ __ZNK17Printd_Parameters13_get_MediaKeyEv : 300 -> 240
~ __ZNK17Printd_Parameters18_get_FeedDirectionEv : 300 -> 240
~ __ZNK17Printd_Parameters20_get_FeedOrientationEv : 276 -> 220
~ ____ZL22getNamedMediaAttrArrayP8PK_ipp_tP8NSStringP10objc_class_block_invoke : 220 -> 204
~ __Z10ippWriteIOPvPFlS_PhmEP8PK_ipp_t : 400 -> 348
~ __ZL18ippWriteWithWriterR11IPPIOWriterR11ipp_state_eR9ipp_tag_ebP8PK_ipp_t : 1584 -> 1608
~ __ZN11IPPIOWriter5flushEi : 120 -> 116
~ ____ZL25writeAllCurrentAttributesR11IPPIOWriterR11ipp_state_eR9ipp_tag_eP8PK_ipp_tb_block_invoke : 3928 -> 3880
~ __ZL12writeStringsR11IPPIOWriterP18PK_ipp_attribute_tm : 188 -> 176
~ ____ZL12writeStringsR11IPPIOWriterP18PK_ipp_attribute_tm_block_invoke : 1088 -> 1004
~ ____ZL14writeTextLangsR11IPPIOWriterP18PK_ipp_attribute_t_block_invoke : 1516 -> 1512
~ ____ZL20writeBeginCollectionR11IPPIOWriterR11ipp_state_eR9ipp_tag_eP18PK_ipp_attribute_tP8PK_ipp_t_block_invoke : 700 -> 688
~ ____ZL19writeDefaultUnknownR11IPPIOWriterP18PK_ipp_attribute_t_block_invoke : 780 -> 768
~ __ZL12urf_compressP14_urf_context_s : 1556 -> 1560
~ __Z29getPrintdRPCProtocolInterfacev : 84 -> 68
~ ____Z29getPrintdRPCProtocolInterfacev_block_invoke : 872 -> 824
~ __Z35getPrintdRPCBrowseProtocolInterfacev : 416 -> 400
~ -[PK_ipp_value_t copyWithZone:] : 68 -> 60
~ -[PK_ipp_value_t initWithCoder:] : 424 -> 412
~ -[PK_ipp_value_t setInteger:] : 76 -> 72
~ -[PK_ipp_value_t setBoolean:] : 76 -> 72
~ -[PK_ipp_value_t setDate:] : 140 -> 136
~ -[PK_ipp_value_t setString:] : 264 -> 256
~ -[PK_ipp_value_t string] : 244 -> 236
~ -[PK_ipp_value_t resolution] : 408 -> 392
~ -[PK_ipp_value_t setResolution:] : 292 -> 276
~ -[PK_ipp_value_t range] : 368 -> 352
~ -[PK_ipp_value_t setRange:] : 240 -> 228
~ -[PK_ipp_value_t unknown] : 100 -> 96
~ -[PK_ipp_value_t setUnknown:] : 64 -> 12
~ -[PK_ipp_value_t collection] : 132 -> 128
~ -[PK_ipp_value_t setCollection:] : 64 -> 12
~ -[PK_ipp_value_t description] : 172 -> 164
~ -[PK_ipp_value_t loggingValue:] : 2176 -> 2104
~ +[PK_ipp_value_t valueWithString:] : 144 -> 148
~ -[PK_ipp_attribute_t initWithName:group:value:] : 200 -> 196
~ -[PK_ipp_attribute_t initWithCoder:] : 364 -> 352
~ -[PK_ipp_attribute_t encodeWithCoder:] : 176 -> 168
~ -[PK_ipp_attribute_t name] : 56 -> 8
~ -[PK_ipp_attribute_t loggingDict] : 568 -> 556
~ ___33-[PK_ipp_attribute_t loggingDict]_block_invoke : 160 -> 156
~ -[PK_ipp_attribute_t debugDescription] : 204 -> 192
~ -[PK_ipp_attribute_t(IPPReadMutable) setNSName:] : 124 -> 112
~ -[PK_ipp_t _initWithAttrs:] : 360 -> 372
~ -[PK_ipp_t _addAttrToAppropriateGroup:] : 292 -> 280
~ -[PK_ipp_t _withGroupingBehavior:] : 152 -> 144
~ -[PK_ipp_t initWithCoder:] : 152 -> 148
~ -[PK_ipp_t encodeWithCoder:] : 144 -> 140
~ -[PK_ipp_t description] : 184 -> 176
~ -[PK_ipp_t debugDescription] : 252 -> 232
~ -[PK_ipp_t userCodableDictionary] : 472 -> 456
~ ___33-[PK_ipp_t userCodableDictionary]_block_invoke : 112 -> 108
~ -[PK_ipp_t replaceOrAddAttribute:withAttribute:settingGroup:] : 292 -> 300
~ ___61-[PK_ipp_t replaceOrAddAttribute:withAttribute:settingGroup:]_block_invoke : 92 -> 88
~ -[PK_ipp_t initWithData:] : 380 -> 384
~ -[PK_ipp_t dataRepresentation] : 156 -> 152
~ -[PK_ipp_t isEqual:] : 164 -> 156
~ -[PK_ipp_t hash] : 76 -> 72
~ -[PK_ipp_t copyWithZone:] : 96 -> 92
~ -[PK_ipp_t withNewAttr:groupTag:valueTag:apply:] : 228 -> 232
~ -[PK_ipp_t _addRanges:name:values:] : 252 -> 256
~ ___35-[PK_ipp_t _addRanges:name:values:]_block_invoke_2 : 172 -> 168
~ -[PK_ipp_t _addString:valueTag:name:lang:value:] : 284 -> 288
~ -[PK_ipp_t _addStrings:valueTag:name:lang:values:] : 308 -> 316
~ ___50-[PK_ipp_t _addStrings:valueTag:name:lang:values:]_block_invoke : 580 -> 584
~ __ZL13ipp_lang_codeP8NSString : 148 -> 140
~ ___copy_helper_block_ea8_32c24_ZTS18ipp_value_string_t : 68 -> 60
~ -[PK_ipp_t _addCollection:name:value:] : 232 -> 248
~ ___45-[PK_ipp_t _addOctetString:name:data:length:]_block_invoke_2 : 148 -> 144
~ -[PK_ipp_t _deleteAttribute:] : 128 -> 124
~ -[PK_ipp_t _addIntegers:valueTag:name:count:adder:] : 252 -> 268
~ ___51-[PK_ipp_t _addIntegers:valueTag:name:count:adder:]_block_invoke : 256 -> 248
~ -[PK_ipp_t _findAttribute0:valueTag:] : 376 -> 368
~ ___37-[PK_ipp_t _findAttribute0:valueTag:]_block_invoke : 288 -> 268
~ -[PK_ipp_collection_t initWithCoder:] : 180 -> 176
~ -[PK_ipp_collection_t debugDescription] : 480 -> 468
~ ___39-[PK_ipp_collection_t debugDescription]_block_invoke : 192 -> 176
~ -[PK_ipp_request_t _setupNewRequest] : 228 -> 220
~ -[PK_ipp_request_t opString] : 328 -> 324
~ -[PK_ipp_request_t _descriptionLeader] : 164 -> 156
~ -[PK_ipp_response_t initWithRequest:] : 816 -> 768
~ -[PK_ipp_response_t rewriteURLAttributes:] : 884 -> 860
~ __Z18ippGetIXCollectionP18PK_ipp_attribute_ti : 232 -> 220
~ __Z15ippGetIXIntegerP18PK_ipp_attribute_ti : 232 -> 224
~ __Z13ippGetIXRangeP18PK_ipp_attribute_tiPi : 376 -> 360
~ __Z14ippGetIXStringP18PK_ipp_attribute_ti : 248 -> 240
~ __Z20ippCoerceAttrToValueP8PK_ipp_tP18PK_ipp_attribute_t9ipp_tag_e : 1508 -> 1468
~ ____ZL17pretty_data_linesP6NSData_block_invoke : 128 -> 124
~ __Z17PKLocalizedStringP8NSStringPKc : 164 -> 156
~ __Z28liteFigureOutDriverSetupInfoP16XDriverSetupInfoP13lite_driver_sP12NSDictionaryIP8NSStringS5_E : 1888 -> 1868
~ __Z14pwgMediaForPWGP8NSStringP10pwg_info_t : 620 -> 624
~ __ZN10MediaArray12findPWGMediaEP8NSString : 88 -> 84
~ __ZL17pwgFormatSizeNamePcmPKcS1_iiS1_ : 772 -> 768
~ -[PKNotification start] : 140 -> 136
~ -[PKNotification _makeDict] : 504 -> 472
~ -[PKNotification _interpretResult:responseDict:] : 228 -> 224
~ -[PKAuthNotification _makeFlags] : 116 -> 112
~ -[PKAuthNotification _makeDict] : 692 -> 652
~ +[PKNotifier sharedNotifier] : 176 -> 160
~ -[PKNotifier makeSimpleAlert:message:] : 208 -> 196
~ __ZL16makeNotificationI14PKNotificationEPT_P10PKNotifierP8NSStringS6_12PKNotifyKind : 188 -> 196
~ -[PKNotifier makeQuotaAlert:message:quotaURL:] : 360 -> 372
~ -[PKNotifier makeNotice:message:] : 160 -> 152
~ -[PKNotifier makeRetry:message:] : 208 -> 196
~ -[PKNotifier makeAuthAlert:challenge:] : 464 -> 456
~ -[PKNotifier notification:completedWithResult:] : 276 -> 272
~ -[PKNotifier startNotification:options:dict:] : 464 -> 460
~ __ZL14_notifyCalloutP20__CFUserNotificationm : 120 -> 116
~ -[PKNotifier cancelNotification:] : 152 -> 156
~ _liteInitURF : 3260 -> 3212
~ __ZL16urf_parse_valuesPKcPii : 136 -> 140
~ __ZL14urf_sendpixelsP13lite_driver_sPhi : 344 -> 288
~ -[PKPrinterBonjourEndpoint initWithEndpoint:provenance:provenanceIdentifier:] : 356 -> 340
~ -[PKPrinterBonjourEndpoint initWithURL:txtRecord:provenance:provenanceIdentifier:] : 348 -> 340
~ -[PKPrinterBonjourEndpoint initWithBonjourString:provenance:provenanceIdentifier:] : 964 -> 932
~ -[PKPrinterBonjourEndpoint initWithCoder:] : 640 -> 616
~ -[PKPrinterBonjourEndpoint encodeWithCoder:] : 204 -> 196
~ -[PKPrinterBonjourEndpoint isEqual:] : 220 -> 240
~ -[PKPrinterBonjourEndpoint copyWithZone:] : 40 -> 4
~ -[PKPrinterBonjourEndpoint dataRepresentation] : 296 -> 240
~ +[PKPrinterBonjourEndpoint endpointWithData:] : 296 -> 240
~ -[PKPrinterBonjourEndpoint persistentNameRepresentationForPrintKitUI] : 420 -> 400
~ -[PKPrinterBonjourEndpoint displayNameForPrintKitUI] : 232 -> 224
~ -[PKPrinterBonjourEndpoint description] : 204 -> 192
~ -[PKPrinterBonjourEndpoint debugDescription] : 596 -> 576
~ +[PKPrinterBonjourEndpoint serviceFromEndpoint:] : 224 -> 216
~ -[PKPrinterBonjourEndpoint isIPPS] : 340 -> 332
~ -[PKPrinterBonjourEndpoint _resolveEndpoint:] : 628 -> 616
~ ___45-[PKPrinterBonjourEndpoint _resolveEndpoint:]_block_invoke : 192 -> 176
~ -[PKPrinterBonjourEndpoint _resolve_finish_resolvedURL:resolvedTXT:] : 380 -> 332
~ ___68-[PKPrinterBonjourEndpoint _resolve_finish_resolvedURL:resolvedTXT:]_block_invoke : 92 -> 88
~ -[PKPrinterBonjourEndpoint userCodableDictionary] : 368 -> 352
~ ___48+[PKDefaults lastUsedPrintersCompletionHandler:]_block_invoke : 828 -> 808
~ +[PKDefaults lastUsedPrinters] : 308 -> 292
~ __Z23withDebuggableSemaphoreIU8__strongP7NSArrayET_P8NSStringdU13block_pointerFvU13block_pointerFvS3_EE : 320 -> 324
~ +[PKDefaults lastUsedPrintersForPhoto:completionHandler:] : 1212 -> 1176
~ +[PKDefaults lastUsedPrintersForPhoto:] : 316 -> 300
~ +[PKDefaults addLastUsedPrinter:duplexMode:lastUsedSize:forPhoto:] : 1880 -> 1800
~ +[PKDefaults iCloudPrintersSync] : 684 -> 672
~ __Z23withDebuggableSemaphoreIU8__strongP7NSArrayIP12NSDictionaryEET_P8NSStringdU13block_pointerFvU13block_pointerFvS6_EE : 320 -> 324
~ +[PKDefaults getUpdatediCloudPrintersFromPrinterTool] : 112 -> 108
~ ___53+[PKDefaults getUpdatediCloudPrintersFromPrinterTool]_block_invoke : 608 -> 592
~ +[PKDefaults iCloudPrinters] : 96 -> 80
~ ___34+[PKDefaults startiCloudListening]_block_invoke : 184 -> 180
~ __ZL24pk_iCloudPrintersChangedP22__CFNotificationCenterPvPK10__CFStringPKvPK14__CFDictionary : 120 -> 116
~ +[PKDefaults setICloudPrinters:] : 176 -> 164
~ +[PKDefaults addPrinterToiCloud:displayName:location:] : 164 -> 156
~ +[PKDefaults removePrinterFromiCloud:] : 164 -> 160
~ +[PKDefaults resetPKCloudData] : 192 -> 184
~ +[PKDefaults(PrintKitPrivate) seenPrintersCompletionHandler:] : 132 -> 128
~ +[PKDefaults(PrintKitPrivate) requiredPDL] : 80 -> 64
~ ___45+[PKDefaults(PrintKitPrivate) ippsIsRequired]_block_invoke : 116 -> 112
~ ___59+[PKDefaults(PrintKitPrivate) mcProfilePrintersOnlyAllowed]_block_invoke : 96 -> 92
~ ___61+[PKDefaults(PrintKitPrivate) airPrintBeaconDiscoveryAllowed]_block_invoke : 116 -> 112
~ +[PKDefaults(PrintKitPrivate) uriMatchesMCProfileAdded:] : 468 -> 460
~ +[PKDefaults(PrintKitPrivate) absoluteSpoolDirectory] : 416 -> 400
~ __Z23withDebuggableSemaphoreIU8__strongP5NSURLET_P8NSStringdU13block_pointerFvU13block_pointerFvS3_EE : 320 -> 324
~ +[PKDefaults(Private) setListenerProxy:] : 64 -> 16
~ +[PKDefaults(Private) listenerProxy] : 60 -> 12
~ __ZL10unxferSizeP19NSMutableDictionaryP12NSDictionaryP8NSString : 332 -> 324
~ __ZL27MCProfileConnectionFunctionv : 60 -> 12
~ ____Z23withDebuggableSemaphoreIU8__strongP7NSArrayET_P8NSStringdU13block_pointerFvU13block_pointerFvS3_EE_block_invoke_2 : 112 -> 96
~ ____Z23withDebuggableSemaphoreIU8__strongP7NSArrayIP12NSDictionaryEET_P8NSStringdU13block_pointerFvU13block_pointerFvS6_EE_block_invoke_2 : 112 -> 96
~ ____Z23withDebuggableSemaphoreIU8__strongP5NSURLET_P8NSStringdU13block_pointerFvU13block_pointerFvS3_EE_block_invoke_2 : 112 -> 96
~ -[PKJob initWithCoder:] : 188 -> 184
~ -[PKJob encodeWithCoder:] : 132 -> 124
~ -[PKJob userCodableDictionary] : 268 -> 256
~ -[PKJob initWithUserCodableDictionary:] : 280 -> 272
~ -[PKJob _withPrinterAsync:] : 264 -> 252
~ -[PKJob printer] : 332 -> 312
~ __Z23withDebuggableSemaphoreIU8__strongP9PKPrinterET_P8NSStringdU13block_pointerFvU13block_pointerFvS3_EE : 320 -> 324
~ +[PKJob jobForJobID:] : 312 -> 296
~ __Z23withDebuggableSemaphoreIU8__strongP5PKJobET_P8NSStringdU13block_pointerFvU13block_pointerFvS3_EE : 320 -> 324
~ ___21+[PKJob jobForJobID:]_block_invoke : 184 -> 176
~ +[PKJob jobsCompletionHandler:] : 304 -> 300
~ ___31+[PKJob jobsCompletionHandler:]_block_invoke : 520 -> 508
~ ___31+[PKJob jobsCompletionHandler:]_block_invoke.26 : 320 -> 332
~ ___37+[PKJob currentJobCompletionHandler:]_block_invoke : 536 -> 532
~ +[PKJob jobs] : 308 -> 292
~ +[PKJob currentJob] : 308 -> 292
~ -[PKJob cancel] : 124 -> 120
~ -[PKJob _updateJobState:] : 196 -> 180
~ -[PKJob updateCompletionHandler:] : 292 -> 296
~ -[PKJob update] : 284 -> 272
~ -[PKJob localJobID] : 76 -> 72
~ -[PKJob printerDisplayName] : 100 -> 92
~ -[PKJob printerLocation] : 100 -> 92
~ -[PKJob printerKind] : 76 -> 72
~ -[PKJob settings] : 100 -> 92
~ -[PKJob timeAtCreation] : 100 -> 92
~ -[PKJob state] : 76 -> 72
~ -[PKJob mediaSheetsCompleted] : 76 -> 72
~ -[PKJob timeAtProcessing] : 100 -> 92
~ -[PKJob timeAtCompleted] : 100 -> 92
~ -[PKJob mediaSheets] : 76 -> 72
~ -[PKJob mediaProgress] : 76 -> 72
~ -[PKJob remoteJobId] : 76 -> 72
~ -[PKJob PIN] : 100 -> 92
~ -[PKJob jobPrinterStateMessage] : 100 -> 92
~ -[PKJob jobPrinterStateReasons] : 100 -> 92
~ -[PKJob jobStateMessage] : 100 -> 92
~ -[PKJob jobStateReasons] : 100 -> 92
~ -[PKJob thumbnailImage] : 100 -> 92
~ -[PKJob printerEndpointData] : 100 -> 92
~ -[PKJob localizedStatusString] : 1116 -> 948
~ -[PKJob localizedJobOptions] : 1664 -> 1564
~ __ZL23_printkitJobListChangedP22__CFNotificationCenterPvPK10__CFStringPKvPK14__CFDictionary : 116 -> 112
~ __ZL17_printkitProgressP22__CFNotificationCenterPvPK10__CFStringPKvPK14__CFDictionary : 116 -> 112
~ ____Z23withDebuggableSemaphoreIU8__strongP9PKPrinterET_P8NSStringdU13block_pointerFvU13block_pointerFvS3_EE_block_invoke_2 : 112 -> 96
~ ____Z23withDebuggableSemaphoreIU8__strongP5PKJobET_P8NSStringdU13block_pointerFvU13block_pointerFvS3_EE_block_invoke_2 : 112 -> 96
~ +[PKiCloudPrinter PKiCloudPrinterWithPKPrinter:displayName:location:] : 876 -> 828
~ -[PKiCloudPrinter uuid] : 112 -> 104
~ -[PKiCloudPrinter dnssdName] : 112 -> 104
~ -[PKiCloudPrinter displayName] : 112 -> 104
~ -[PKiCloudPrinter customName] : 112 -> 104
~ -[PKiCloudPrinter location] : 112 -> 104
~ -[PKiCloudPrinter customLocation] : 112 -> 104
~ -[PKiCloudPrinter printerURLs] : 112 -> 104
~ -[PKiCloudPrinter endPoints] : 112 -> 104
~ -[PKiCloudPrinter lastUsedDate] : 112 -> 104
~ -[PKiCloudPrinter printerType] : 128 -> 120
~ -[PKiCloudPrinter isFromMCProfile] : 128 -> 120
~ -[PKiCloudPrinter printerImageData] : 112 -> 104
~ -[PKiCloudPrinter userCodableDictionary] : 1636 -> 1580
~ __PKLogCategory : 144 -> 140
~ __Z23withDebuggableSemaphoreP8NSStringdU13block_pointerFvPU32objcproto21OS_dispatch_semaphore8NSObjectE : 508 -> 452
~ ____ZL7logInitv_block_invoke : 440 -> 436
~ -[PKMediaName parseMediaName:] : 636 -> 612
~ -[PKMediaName isRoll] : 84 -> 80
~ +[PKPaper defaultGenericPaperForLocale:] : 264 -> 248
~ +[PKPaper useMetric] : 152 -> 144
~ +[PKPaper mediaNameForWidth:Height:mediaType:Borderless:Simplex:] : 304 -> 292
~ +[PKPaper paperWithAttributes:] : 1000 -> 940
~ -[PKPaper cutToPWGLength:] : 428 -> 420
~ -[PKPaper initWithWidth:Height:Left:Top:Right:Bottom:localizedName:codeName:mediaInfo:] : 744 -> 724
~ -[PKPaper nameWithoutSuffixes:] : 284 -> 292
~ -[PKPaper baseName] : 184 -> 168
~ -[PKPaper minHeight] : 268 -> 248
~ -[PKPaper maxHeight] : 268 -> 248
~ -[PKPaper isRoll] : 184 -> 172
~ -[PKPaper mediaType] : 132 -> 112
~ -[PKPaper mediaTypeName] : 364 -> 340
~ -[PKPaper createMediaColAndDoMargins:] : 304 -> 296
~ -[PKPaper localizedNameFromDimensions] : 832 -> 784
~ -[PKPaper isEqualSizeAndMediaType:] : 228 -> 220
~ -[PKPaper sizeMediaTypeAndImageableCompare:] : 276 -> 268
~ -[PKPaper localizedName] : 248 -> 232
~ -[PKPaper description] : 204 -> 192
~ -[PKPaper debugDescription] : 316 -> 304
~ +[PKPaper genericWithName:] : 212 -> 208
~ -[PKPaper paperWithMarginsAdjustedForDuplexMode:] : 484 -> 480
~ -[PKPaper isEqual:] : 212 -> 204
~ -[PKPaper hash] : 76 -> 72
~ +[PKPaper photoPapers] : 504 -> 464
~ +[PKPaper documentPapers] : 180 -> 168
~ +[PKPaper mediaNameForWidth:height:borderless:simplex:] : 304 -> 292
~ -[PKPaper mediaInfo] : 56 -> 8
~ -[PKPaper name] : 56 -> 8
~ -[PKPaper copyWithZone:] : 40 -> 4
~ -[PKPaper initWithCoder:] : 608 -> 592
~ -[PKPaper encodeWithCoder:] : 252 -> 244
~ ___41-[PKPaper initWithUserCodableDictionary:]_block_invoke : 204 -> 196
~ -[PKPaper visitProperties:] : 1140 -> 1156
~ ___27-[PKPaper visitProperties:]_block_invoke : 524 -> 476
~ ___27-[PKPaper visitProperties:]_block_invoke_2 : 228 -> 224
~ +[PKPrinterDescription standardRequestedAttributes] : 588 -> 584
~ +[PKPrinterDescription txtRecordReconstructingAttributes] : 300 -> 296
~ -[PKPrinterDescription printInfoSupportedDictionary] : 552 -> 548
~ -[PKPrinterDescription description] : 80 -> 76
~ -[PKPrinterDescription debugDescription] : 260 -> 264
~ ___40-[PKPrinterDescription debugDescription]_block_invoke : 296 -> 280
~ -[PKPrinterDescription initWithCoder:] : 228 -> 224
~ ___54-[PKPrinterDescription initWithUserCodableDictionary:]_block_invoke : 204 -> 196
~ -[PKPrinterDescription makeTXTRecordWithURL:] : 1228 -> 1176
~ +[PKPrinterDescription(PrintertoolSideConstruction) attributesRequiredForPKPaperList] : 144 -> 140
~ -[PKPrinterDescription(PrintertoolSideConstruction) initWithAttributes:translations:] : 160 -> 168
~ -[PKPrinterDescription(PrintertoolSideConstruction) _calcFinishingTemplates:] : 1384 -> 1340
~ __ZL25GetLocalizedNameForOptionP8NSStringS0_ : 176 -> 172
~ ___77-[PKPrinterDescription(PrintertoolSideConstruction) _calcFinishingTemplates:]_block_invoke : 180 -> 168
~ -[PKPrinterDescription(PrintertoolSideConstruction) _calcOutputBins:] : 376 -> 372
~ ___69-[PKPrinterDescription(PrintertoolSideConstruction) _calcOutputBins:]_block_invoke : 516 -> 500
~ -[PKPrinterDescription(PrintertoolSideConstruction) _calcIdentifyActions:] : 440 -> 436
~ -[PKPrinterDescription(PrintertoolSideConstruction) _calcSpecialFeedOrientation:] : 716 -> 692
~ -[PKPrinterDescription(PrintertoolSideConstruction) _calcPrintScalingSupported:] : 188 -> 176
~ -[PKPrinterDescription(PrintertoolSideConstruction) _calculateSides:] : 312 -> 300
~ -[PKPrinterDescription(PrintertoolSideConstruction) _calculateQuality:] : 376 -> 372
~ ___71-[PKPrinterDescription(PrintertoolSideConstruction) _calculateQuality:]_block_invoke : 172 -> 160
~ -[PKPrinterDescription(PrintertoolSideConstruction) _calculateFormats:] : 888 -> 852
~ -[PKPrinterDescription(PrintertoolSideConstruction) _calculateMediaColSupportedArray:] : 200 -> 192
~ -[PKPrinterDescription(PrintertoolSideConstruction) replacePaperList:] : 68 -> 16
~ -[PKPrinterDescription(PrintertoolSideConstruction) _calculatePaperList:] : 288 -> 272
~ -[PKPrinterDescription(PrintertoolSideConstruction) _calculateOutputModes:] : 272 -> 244
~ -[PKPrinterDescription(PrintertoolSideConstruction) _calcInputSlots:] : 620 -> 600
~ -[PKPrinterDescription(PrintertoolSideConstruction) _calcMediaTypes:] : 868 -> 848
~ -[PKPrinterDescription(PrintertoolSideConstruction) _calcJobPresets:] : 852 -> 836
~ ___69-[PKPrinterDescription(PrintertoolSideConstruction) _calcJobPresets:]_block_invoke : 684 -> 616
~ -[PKPrinterDescription(PrintertoolSideConstruction) _calcDeviceID:] : 84 -> 76
~ -[PKPrinterDescription(PrintertoolSideConstruction) _calcPrinterDriverInfo:] : 416 -> 392
~ -[PKPrinterDescription(PrintertoolSideConstruction) _makePrinterDeviceIDFromTxt] : 1464 -> 1440
~ -[PKPrinterDescription(PrintertoolSideConstruction) txtRecordObjectForKey:] : 116 -> 108
~ -[PKPrinterDescription(PrintertoolSideConstruction) _ingestTxtRecord:] : 480 -> 468
~ -[PKPrinterDescription(PrintertoolSideConstruction) _ingestAttrs:] : 1512 -> 1404
~ -[PKCollectionSpecialization debugDescription] : 244 -> 228
~ -[PKCollectionSpecialization collection] : 56 -> 8
~ -[PKMediaSize getThingType:] : 176 -> 168
~ -[PKMediaSize getInt:] : 236 -> 220
~ -[PKMediaSize getRange:] : 396 -> 372
~ -[PKMediaSize userCodableDictionary] : 328 -> 316
~ -[PKMediaCol userCodableDictionary] : 688 -> 644
~ -[PKMediaCol getMargins:] : 372 -> 376
~ -[PKMediaSourceProperties userCodableDictionary] : 196 -> 188
~ -[PKMutableMediaCol setMarginsTop:left:bottom:right:] : 324 -> 328
~ -[PKMutableMediaCol makeMediaCol] : 492 -> 504
~ ____ZL21convertIPPIntsToArrayP18PK_ipp_attribute_t_block_invoke : 164 -> 152
~ ____ZL20ensureLowercasedKeysP12NSDictionaryIP8NSStringS1_E_block_invoke : 148 -> 144
~ -[PKPaperList(PrintertoolSideConstruction) initWithParams:translations:] : 972 -> 944
~ -[PKPaperList(PrintertoolSideConstruction) initWithPapers:] : 272 -> 264
~ -[PKPaperList initWithTXTRecord:] : 292 -> 280
~ -[PKPaperList rolls] : 208 -> 200
~ +[PKPaperList mediaDictFromAttrs:translations:] : 544 -> 540
~ ___47+[PKPaperList mediaDictFromAttrs:translations:]_block_invoke : 728 -> 688
~ -[PKPaperList adjustMargins:forDuplex:] : 444 -> 452
~ -[PKPaperList isPaperReady:] : 188 -> 180
~ -[PKPaperList paperListForDuplexMode:] : 204 -> 192
~ -[PKPaperList papersForPhotoWithSize:] : 324 -> 300
~ -[PKPaperList papersForDocumentWithSize:scaleUpOnRoll:andDuplex:] : 256 -> 236
~ -[PKPaperList matchedPaper:preferBorderless:withDuplexMode:didMatch:] : 664 -> 612
~ -[PKPaperList addPaperSet:withCount:toArrays:] : 168 -> 172
~ -[PKPaperList categorizePapers:] : 1096 -> 1084
~ -[PKPaperList tersePaperFrom:withRequest:] : 744 -> 728
~ -[PKPaperList tersePaperFrom:withMediaInfo:] : 592 -> 580
~ -[PKPaperList rollReadyPaperListWithContentSize:forPhoto:] : 68 -> 60
~ -[PKPaperList rollReadyPaperListForDocumentWithContentSize:scaleUp:] : 580 -> 564
~ -[PKPaperList rollReadyPaperListForPhotoWithContentSize:] : 652 -> 636
~ -[PKPaperList availableRollPapersPreferBorderless:] : 616 -> 624
~ ___51-[PKPaperList availableRollPapersPreferBorderless:]_block_invoke : 236 -> 248
~ -[PKPaperList matchPaper:] : 204 -> 200
~ ___26-[PKPaperList matchPaper:]_block_invoke : 292 -> 280
~ -[PKPaperList matchPaper:inList:] : 276 -> 268
~ ___33-[PKPaperList matchPaper:inList:]_block_invoke : 292 -> 280
~ -[PKPaperList hasMatchingLoadedRoll:] : 260 -> 252
~ ___37-[PKPaperList hasMatchingLoadedRoll:]_block_invoke : 100 -> 96
~ -[PKPaperList filterUsingBlock:] : 152 -> 144
~ -[PKPaperList filterPapers:usingBlock:] : 272 -> 268
~ -[PKPaperList jobTypesSupported:] : 552 -> 548
~ -[PKPaperList conjureMediaFromTXT:] : 2576 -> 2476
~ -[PKPaperList debugDescription] : 260 -> 264
~ ___31-[PKPaperList debugDescription]_block_invoke : 296 -> 280
~ -[PKPaperList setRolls:] : 64 -> 12
~ __ZN11DescVisitor15visitPropertiesEPU30objcproto19PKPropertyVisitable8NSObjectU13block_pointerFvRKS_E : 184 -> 188
~ __ZN13EncodeVisitor15visitPropertiesEPU30objcproto19PKPropertyVisitable8NSObjectP7NSCoder : 168 -> 172
~ __ZN13DecodeVisitor15visitPropertiesEPU30objcproto19PKPropertyVisitable8NSObjectP7NSCoder : 168 -> 172
~ __ZN14CompareVisitor15visitPropertiesEPU30objcproto19PKPropertyVisitable8NSObjectPS0_U13block_pointerFvRKS_E : 216 -> 228
~ __ZN12_DescVisitor5visitEP8NSStringRi : 164 -> 160
~ __ZN12_DescVisitor5visitEP8NSStringRl : 164 -> 160
~ __ZN12_DescVisitor5visitEP8NSStringRm : 164 -> 160
~ __ZN12_DescVisitor5visitEP8NSStringRU8__strongS1_ : 156 -> 152
~ __ZN12_DescVisitor5visitEP8NSStringRU8__strongP5NSURL : 156 -> 152
~ __ZN12_DescVisitor5visitEP8NSStringRU8__strongP6NSData : 156 -> 152
~ __ZN12_DescVisitor5visitEP8NSStringRU8__strongP6NSUUID : 156 -> 152
~ __ZN12_DescVisitor5visitEP8NSStringRU8__strongP6NSDate : 156 -> 152
~ __ZN12_DescVisitor5visitEP8NSStringRU8__strongP12NSDictionaryIS1_S1_E : 156 -> 152
~ __ZN12_DescVisitor5visitEP8NSStringRU8__strongP7NSArrayIP7NSValueE : 156 -> 152
~ __ZN12_DescVisitor5visitEP8NSStringRU8__strongP7NSArrayIP8NSNumberE : 156 -> 152
~ __ZN12_DescVisitor5visitEP8NSStringRU8__strongP7NSArrayIS1_E : 156 -> 152
~ __ZN12_DescVisitor5visitEP8NSStringRU8__strongP5NSSetIS1_E : 156 -> 152
~ __ZN12_DescVisitor5visitEP8NSStringRU8__strongP7NSArrayIP12NSDictionaryE : 156 -> 152
~ __ZN12_DescVisitor5visitEP8NSStringRU8__strongP12NSDictionaryIS1_P8NSNumberE : 156 -> 152
~ __ZN12_DescVisitor5visitEP8NSStringRU8__strongP7PKPaper : 156 -> 152
~ __ZN12_DescVisitor5visitEP8NSStringRU8__strongP11PKPaperList : 156 -> 152
~ __ZN12_DescVisitor5visitEP8NSStringRU8__strongP15PKPrintSettings : 156 -> 152
~ __ZN12_DescVisitor5visitEP8NSStringRU8__strongP7NSArrayIP6PKTrayE : 156 -> 152
~ __ZN12_DescVisitor5visitEP8NSStringRU8__strongP7NSArrayIP7PKPaperE : 156 -> 152
~ __ZNK12_DescVisitor5linesEv : 56 -> 8
~ __ZN12_DescVisitor8addNamedEP8NSStringS1_ : 128 -> 124
~ __ZN12_DescVisitor3seeEP8NSObject : 472 -> 452
~ __ZN14_EncodeVisitor5visitEP8NSStringRU8__strongP5NSSetIS1_E : 148 -> 144
~ __ZN14_DecodeVisitor5visitEP8NSStringRU8__strongS1_ : 144 -> 140
~ __ZN14_DecodeVisitor5visitEP8NSStringRU8__strongP5NSURL : 144 -> 140
~ __ZN14_DecodeVisitor5visitEP8NSStringRU8__strongP6NSData : 144 -> 140
~ __ZN14_DecodeVisitor5visitEP8NSStringRU8__strongP6NSUUID : 144 -> 140
~ __ZN14_DecodeVisitor5visitEP8NSStringRU8__strongP6NSDate : 144 -> 140
~ __ZN14_DecodeVisitor5visitEP8NSStringRU8__strongP12NSDictionaryIS1_S1_E : 168 -> 164
~ __ZN14_DecodeVisitor5visitEP8NSStringRU8__strongP7NSArrayIP7NSValueE : 144 -> 140
~ __ZN14_DecodeVisitor5visitEP8NSStringRU8__strongP7NSArrayIP8NSNumberE : 144 -> 140
~ __ZN14_DecodeVisitor5visitEP8NSStringRU8__strongP7NSArrayIS1_E : 144 -> 140
~ __ZN14_DecodeVisitor5visitEP8NSStringRU8__strongP5NSSetIS1_E : 200 -> 192
~ __ZN14_DecodeVisitor5visitEP8NSStringRU8__strongP7NSArrayIP12NSDictionaryE : 348 -> 336
~ __ZN14_DecodeVisitor5visitEP8NSStringRU8__strongP12NSDictionaryIS1_P8NSNumberE : 172 -> 168
~ __ZN14_DecodeVisitor5visitEP8NSStringRU8__strongP7PKPaper : 144 -> 140
~ __ZN14_DecodeVisitor5visitEP8NSStringRU8__strongP11PKPaperList : 144 -> 140
~ __ZN14_DecodeVisitor5visitEP8NSStringRU8__strongP15PKPrintSettings : 144 -> 140
~ __ZN14_DecodeVisitor5visitEP8NSStringRU8__strongP7NSArrayIP6PKTrayE : 144 -> 140
~ __ZN14_DecodeVisitor5visitEP8NSStringRU8__strongP7NSArrayIP7PKPaperE : 144 -> 140
~ __ZN15_CompareVisitor5visitEP8NSStringRb : 136 -> 132
~ __ZN15_CompareVisitor5visitEP8NSStringRi : 136 -> 132
~ __ZN15_CompareVisitor5visitEP8NSStringRl : 136 -> 132
~ __ZN15_CompareVisitor5visitEP8NSStringRm : 136 -> 132
~ __ZN15_CompareVisitor7getPropIbEET_P8NSString : 92 -> 88
~ __ZN15_CompareVisitor7getPropIiEET_P8NSString : 92 -> 88
~ __ZN15_CompareVisitor7getPropIlEET_P8NSString : 92 -> 88
~ __ZN15_CompareVisitor7getPropImEET_P8NSString : 92 -> 88
~ __ZN15_CompareVisitor7getPropIU8__strongP8NSObjectEET_P8NSString : 116 -> 108
~ __ZN30_UserCodedSerializationVisitor5visitEP8NSStringRb : 188 -> 184
~ __ZN30_UserCodedSerializationVisitor5visitEP8NSStringRi : 188 -> 184
~ __ZN30_UserCodedSerializationVisitor5visitEP8NSStringRl : 188 -> 184
~ __ZN30_UserCodedSerializationVisitor5visitEP8NSStringRm : 188 -> 184
~ __ZN30_UserCodedSerializationVisitor5visitEP8NSStringRU8__strongP7NSArrayIP7NSValueE : 200 -> 192
~ __ZN30_UserCodedSerializationVisitor5visitEP8NSStringRU8__strongP7NSArrayIP8NSNumberE : 180 -> 172
~ __ZN30_UserCodedSerializationVisitor5visitEP8NSStringRU8__strongP7NSArrayIS1_E : 180 -> 172
~ __ZN30_UserCodedSerializationVisitor5visitEP8NSStringRU8__strongP5NSSetIS1_E : 200 -> 192
~ __ZN30_UserCodedSerializationVisitor5visitEP8NSStringRU8__strongP7NSArrayIP12NSDictionaryE : 180 -> 172
~ __ZN30_UserCodedSerializationVisitor5visitEP8NSStringRU8__strongP7NSArrayIP6PKTrayE : 200 -> 192
~ __ZN30_UserCodedSerializationVisitor5visitEP8NSStringRU8__strongP7NSArrayIP7PKPaperE : 180 -> 172
~ ____ZN30XUserCodedSerializationVisitor15makeToUserCodedIU8__strongP8NSNumberEEU13block_pointerFPU28objcproto17PKUserCodableType8NSObjectPS4_Ev_block_invoke : 68 -> 20
~ ____ZN30XUserCodedSerializationVisitor17makeFromUserCodedIU8__strongP8NSNumberEEU13block_pointerFP8NSObjectPU28objcproto17PKUserCodableTypeS4_Ev_block_invoke : 56 -> 8
~ ____ZN30XUserCodedSerializationVisitor15makeToUserCodedIU8__strongP8NSStringEEU13block_pointerFPU28objcproto17PKUserCodableType8NSObjectPS4_Ev_block_invoke : 68 -> 20
~ ____ZN30XUserCodedSerializationVisitor17makeFromUserCodedIU8__strongP8NSStringEEU13block_pointerFP8NSObjectPU28objcproto17PKUserCodableTypeS4_Ev_block_invoke : 56 -> 8
~ ____ZN30XUserCodedSerializationVisitor15makeToUserCodedIU8__strongP5NSURLEEU13block_pointerFPU28objcproto17PKUserCodableType8NSObjectPS4_Ev_block_invoke : 52 -> 48
~ ____ZN30XUserCodedSerializationVisitor17makeFromUserCodedIU8__strongP5NSURLEEU13block_pointerFP8NSObjectPU28objcproto17PKUserCodableTypeS4_Ev_block_invoke : 60 -> 56
~ ____ZN30XUserCodedSerializationVisitor15makeToUserCodedIU8__strongP6NSDataEEU13block_pointerFPU28objcproto17PKUserCodableType8NSObjectPS4_Ev_block_invoke : 56 -> 52
~ ____ZN30XUserCodedSerializationVisitor15makeToUserCodedIU8__strongP6NSUUIDEEU13block_pointerFPU28objcproto17PKUserCodableType8NSObjectPS4_Ev_block_invoke : 52 -> 48
~ ____ZN30XUserCodedSerializationVisitor15makeToUserCodedIU8__strongP6NSDateEEU13block_pointerFPU28objcproto17PKUserCodableType8NSObjectPS4_Ev_block_invoke : 132 -> 124
~ ____ZN30XUserCodedSerializationVisitor15makeToUserCodedIU8__strongP12NSDictionaryEEU13block_pointerFPU28objcproto17PKUserCodableType8NSObjectPS4_Ev_block_invoke : 56 -> 8
~ ____ZN30XUserCodedSerializationVisitor17makeFromUserCodedIU8__strongP12NSDictionaryEEU13block_pointerFP8NSObjectPU28objcproto17PKUserCodableTypeS4_Ev_block_invoke : 56 -> 8
~ ____ZN30XUserCodedSerializationVisitor27makeUserCodedFromTypedArrayIU8__strongP7NSValueEEU13block_pointerFPU28objcproto17PKUserCodableType8NSObjectPS4_Ev_block_invoke : 276 -> 268
~ ____ZN30XUserCodedSerializationVisitor27makeUserCodedFromTypedArrayIU8__strongP7NSValueEEU13block_pointerFPU28objcproto17PKUserCodableType8NSObjectPS4_Ev_block_invoke_2 : 116 -> 112
~ ____ZN30XUserCodedSerializationVisitor15makeToUserCodedIU8__strongP7NSValueEEU13block_pointerFPU28objcproto17PKUserCodableType8NSObjectPS4_Ev_block_invoke : 100 -> 92
~ ____ZN30XUserCodedSerializationVisitor27makeTypedArrayFromUserCodedIU8__strongP7NSValueEEU13block_pointerFP8NSObjectPU28objcproto17PKUserCodableTypeS4_Ev_block_invoke : 436 -> 440
~ ____ZN30XUserCodedSerializationVisitor17makeFromUserCodedIU8__strongP7NSValueEEU13block_pointerFP8NSObjectPU28objcproto17PKUserCodableTypeS4_Ev_block_invoke : 120 -> 112
~ ____ZN30XUserCodedSerializationVisitor27makeUserCodedFromTypedArrayIU8__strongP8NSNumberEEU13block_pointerFPU28objcproto17PKUserCodableType8NSObjectPS4_Ev_block_invoke : 276 -> 268
~ ____ZN30XUserCodedSerializationVisitor27makeUserCodedFromTypedArrayIU8__strongP8NSNumberEEU13block_pointerFPU28objcproto17PKUserCodableType8NSObjectPS4_Ev_block_invoke_2 : 116 -> 112
~ ____ZN30XUserCodedSerializationVisitor27makeTypedArrayFromUserCodedIU8__strongP8NSNumberEEU13block_pointerFP8NSObjectPU28objcproto17PKUserCodableTypeS4_Ev_block_invoke : 436 -> 440
~ ____ZN30XUserCodedSerializationVisitor27makeUserCodedFromTypedArrayIU8__strongP8NSStringEEU13block_pointerFPU28objcproto17PKUserCodableType8NSObjectPS4_Ev_block_invoke : 276 -> 268
~ ____ZN30XUserCodedSerializationVisitor27makeUserCodedFromTypedArrayIU8__strongP8NSStringEEU13block_pointerFPU28objcproto17PKUserCodableType8NSObjectPS4_Ev_block_invoke_2 : 116 -> 112
~ ____ZN30XUserCodedSerializationVisitor27makeTypedArrayFromUserCodedIU8__strongP8NSStringEEU13block_pointerFP8NSObjectPU28objcproto17PKUserCodableTypeS4_Ev_block_invoke : 436 -> 440
~ __ZN30XUserCodedSerializationVisitor15makeToUserCodedIU8__strongP5NSSetIP8NSStringEEEU13block_pointerFPU28objcproto17PKUserCodableType8NSObjectPS7_Ev : 172 -> 168
~ __ZN30XUserCodedSerializationVisitor17makeFromUserCodedIU8__strongP5NSSetIP8NSStringEEEU13block_pointerFP8NSObjectPU28objcproto17PKUserCodableTypeS7_Ev : 172 -> 168
~ ____ZN30XUserCodedSerializationVisitor15makeToUserCodedIU8__strongP5NSSetIP8NSStringEEEU13block_pointerFPU28objcproto17PKUserCodableType8NSObjectPS7_Ev_block_invoke : 124 -> 116
~ ____ZN30XUserCodedSerializationVisitor17makeFromUserCodedIU8__strongP5NSSetIP8NSStringEEEU13block_pointerFP8NSObjectPU28objcproto17PKUserCodableTypeS7_Ev_block_invoke : 128 -> 120
~ ____ZN30XUserCodedSerializationVisitor27makeUserCodedFromTypedArrayIU8__strongP12NSDictionaryEEU13block_pointerFPU28objcproto17PKUserCodableType8NSObjectPS4_Ev_block_invoke : 276 -> 268
~ ____ZN30XUserCodedSerializationVisitor27makeUserCodedFromTypedArrayIU8__strongP12NSDictionaryEEU13block_pointerFPU28objcproto17PKUserCodableType8NSObjectPS4_Ev_block_invoke_2 : 116 -> 112
~ ____ZN30XUserCodedSerializationVisitor27makeTypedArrayFromUserCodedIU8__strongP12NSDictionaryEEU13block_pointerFP8NSObjectPU28objcproto17PKUserCodableTypeS4_Ev_block_invoke : 436 -> 440
~ ____ZN30XUserCodedSerializationVisitor15makeToUserCodedIU8__strongP7PKPaperEEU13block_pointerFPU28objcproto17PKUserCodableType8NSObjectPS4_Ev_block_invoke : 52 -> 48
~ ____ZN30XUserCodedSerializationVisitor15makeToUserCodedIU8__strongP11PKPaperListEEU13block_pointerFPU28objcproto17PKUserCodableType8NSObjectPS4_Ev_block_invoke : 192 -> 180
~ ____ZN30XUserCodedSerializationVisitor27makeUserCodedFromTypedArrayIU8__strongP7PKPaperEEU13block_pointerFPU28objcproto17PKUserCodableType8NSObjectPS4_Ev_block_invoke : 276 -> 268
~ ____ZN30XUserCodedSerializationVisitor27makeUserCodedFromTypedArrayIU8__strongP7PKPaperEEU13block_pointerFPU28objcproto17PKUserCodableType8NSObjectPS4_Ev_block_invoke_2 : 116 -> 112
~ ____ZN30XUserCodedSerializationVisitor17makeFromUserCodedIU8__strongP11PKPaperListEEU13block_pointerFP8NSObjectPU28objcproto17PKUserCodableTypeS4_Ev_block_invoke : 180 -> 168
~ ____ZN30XUserCodedSerializationVisitor27makeTypedArrayFromUserCodedIU8__strongP7PKPaperEEU13block_pointerFP8NSObjectPU28objcproto17PKUserCodableTypeS4_Ev_block_invoke : 436 -> 440
~ ____ZN30XUserCodedSerializationVisitor15makeToUserCodedIU8__strongP15PKPrintSettingsEEU13block_pointerFPU28objcproto17PKUserCodableType8NSObjectPS4_Ev_block_invoke : 52 -> 48
~ ____ZN30XUserCodedSerializationVisitor27makeUserCodedFromTypedArrayIU8__strongP6PKTrayEEU13block_pointerFPU28objcproto17PKUserCodableType8NSObjectPS4_Ev_block_invoke : 276 -> 268
~ ____ZN30XUserCodedSerializationVisitor27makeUserCodedFromTypedArrayIU8__strongP6PKTrayEEU13block_pointerFPU28objcproto17PKUserCodableType8NSObjectPS4_Ev_block_invoke_2 : 116 -> 112
~ ____ZN30XUserCodedSerializationVisitor15makeToUserCodedIU8__strongP6PKTrayEEU13block_pointerFPU28objcproto17PKUserCodableType8NSObjectPS4_Ev_block_invoke : 52 -> 48
~ ____ZN30XUserCodedSerializationVisitor27makeTypedArrayFromUserCodedIU8__strongP6PKTrayEEU13block_pointerFP8NSObjectPU28objcproto17PKUserCodableTypeS4_Ev_block_invoke : 436 -> 440
~ -[PKPrintSettings _setupDefaults] : 124 -> 112
~ -[PKPrintSettings initWithSettings:] : 136 -> 132
~ -[PKPrintSettings encodeWithCoder:] : 124 -> 116
~ +[PKPrintSettings photo] : 176 -> 172
~ -[PKPrintSettings hash] : 76 -> 72
~ ___48-[PKPrintSettings setFromUserCodableDictionary:]_block_invoke : 204 -> 196
~ -[PKPrintSettings debugDescription] : 260 -> 264
~ ___35-[PKPrintSettings debugDescription]_block_invoke : 296 -> 280
~ -[PKPrintSettings keyedNameToVisitName:] : 812 -> 800
~ -[PKPrintSettings setPageRanges:] : 440 -> 444
~ -[PKPrintSettings setObject:forKey:] : 876 -> 844
~ -[PKPrintSettings removeObjectForKey:] : 260 -> 200
~ -[PKPrintSettings objectForKey:] : 572 -> 508
~ ___32-[PKPrintSettings objectForKey:]_block_invoke : 184 -> 180
~ __Z14_visitHexLinesP6NSDatabU13block_pointerFvP8NSStringE : 628 -> 632
~ ____Z14_visitHexLinesP6NSDatabU13block_pointerFvP8NSStringE_block_invoke : 600 -> 616
~ ____Z14_visitHexLinesP6NSDatabU13block_pointerFvP8NSStringE_block_invoke_2 : 148 -> 144
~ -[PKPrinter _allowedToPrintToThisPrinter] : 492 -> 420
~ +[PKPrinter printerWithURL:discoveryTimeout:completionHandler:] : 168 -> 164
~ +[PKPrinter printerWithName:discoveryTimeout:completionHandler:] : 528 -> 456
~ +[PKPrinter printerWithBonjourEndpoint:discoveryTimeout:completionHandler:] : 264 -> 268
~ +[PKPrinter printerWithEndpointData:discoveryTime:completionHandler:] : 196 -> 192
~ +[PKPrinter printerWithiCloudPrinter:discoveryTime:completionHandler:] : 364 -> 308
~ +[PKPrinter printerWithName:] : 52 -> 48
~ +[PKPrinter printerWithName:discoveryTimeout:] : 388 -> 392
~ ___46+[PKPrinter printerWithName:discoveryTimeout:]_block_invoke : 112 -> 96
~ +[PKPrinter printerLookupWithName:andTimeout:] : 56 -> 52
~ -[PKPrinter _updateDescription:browseInfo:] : 248 -> 240
~ -[PKPrinter updateiCloudPrinterInfo] : 332 -> 324
~ -[PKPrinter withDescriptionAsync:] : 712 -> 688
~ -[PKPrinter debugDescription] : 244 -> 228
~ -[PKPrinter printerURL] : 384 -> 368
~ -[PKPrinter nearbyURL] : 748 -> 696
~ -[PKPrinter name] : 140 -> 128
~ -[PKPrinter bonjourName] : 100 -> 92
~ -[PKPrinter bonjourDisplayName] : 152 -> 140
~ -[PKPrinter displayName] : 260 -> 240
~ -[PKPrinter location] : 292 -> 264
~ -[PKPrinter isiCloudPrinter] : 56 -> 52
~ -[PKPrinter lastUsedDate] : 100 -> 92
~ -[PKPrinter printerImageData] : 100 -> 92
~ -[PKPrinter makeAndModel] : 100 -> 92
~ -[PKPrinter uuid] : 140 -> 128
~ -[PKPrinter isFromMCProfile] : 232 -> 216
~ -[PKPrinter type] : 76 -> 72
~ -[PKPrinter kind] : 124 -> 116
~ -[PKPrinter jobAccountIDSupport] : 136 -> 128
~ -[PKPrinter jobTypesSupported] : 536 -> 516
~ -[PKPrinter hasPrintInfoSupported] : 56 -> 52
~ -[PKPrinter printInfoSupported] : 308 -> 292
~ __Z23withDebuggableSemaphoreIU8__strongP12NSDictionaryET_P8NSStringdU13block_pointerFvU13block_pointerFvS3_EE : 320 -> 324
~ ___31-[PKPrinter printInfoSupported]_block_invoke_2 : 120 -> 116
~ -[PKPrinter hasIdentifyPrinterOp] : 80 -> 76
~ ___25-[PKPrinter identifySelf]_block_invoke : 128 -> 120
~ -[PKPrinter _identifySelf:] : 356 -> 344
~ -[PKPrinter _updateAccessState:] : 240 -> 192
~ -[PKPrinter unlockWithCompletionHandler:] : 688 -> 628
~ -[PKPrinter cancelUnlock] : 212 -> 164
~ -[PKPrinter removeCredentialsFromKeychain] : 132 -> 124
~ -[PKPrinter _setInitialAccessStateFromBrowseInfo] : 208 -> 196
~ -[PKPrinter _checkAvailable:queue:completionHandler:] : 1056 -> 984
~ -[PKPrinter pollForPrinterStatusQueue:completionHandler:] : 436 -> 396
~ __ZN22PrinterStatusQueuePoll20requestedAttributessEv : 172 -> 168
~ ___57-[PKPrinter pollForPrinterStatusQueue:completionHandler:]_block_invoke : 1508 -> 1460
~ ___29-[PKPrinter getSupplyLevels:]_block_invoke : 224 -> 220
~ -[PKPrinter(Paper) knowsReadyPaperList] : 116 -> 108
~ -[PKPrinter(Paper) isPaperReady:] : 156 -> 148
~ -[PKPrinter(Paper) availableRollPapersPreferBorderless:] : 148 -> 136
~ -[PKPrinter(Paper) papersForPhotoWithSize:] : 164 -> 152
~ -[PKPrinter(Paper) paperListForDuplexMode:] : 180 -> 168
~ -[PKPrinter(Paper) papersForDocumentWithSize:scaleUpOnRoll:andDuplex:] : 180 -> 168
~ -[PKPrinter(Paper) matchedPaper:preferBorderless:withDuplexMode:didMatch:] : 220 -> 212
~ -[PKPrinter(Printing) printURL:ofType:printSettings:completionHandlerWithLocalJobNumber:] : 936 -> 856
~ ___89-[PKPrinter(Printing) printURL:ofType:printSettings:completionHandlerWithLocalJobNumber:]_block_invoke : 1820 -> 1880
~ __ZL17writeURLToPrinterP17PKPrintJobRequestP5NSURLU13block_pointerFvP8NSNumberE : 228 -> 232
~ -[PKPrinter(Printing) startJob:ofType:] : 952 -> 872
~ -[PKPrinter(Printing) sendData:ofLength:] : 492 -> 432
~ -[PKPrinter(Printing) finalizeJob:completionHandler:] : 420 -> 356
~ -[PKCloudResolveContext initWithPKCloudPrinter:timeout:completionHandler:] : 596 -> 504
~ -[PKCloudResolveContext _complete:] : 468 -> 396
~ -[PKCloudResolveContext start] : 556 -> 464
~ -[PKCloudResolveContext _driveResolution] : 1032 -> 924
~ ___41-[PKCloudResolveContext _driveResolution]_block_invoke : 160 -> 152
~ ___41-[PKCloudResolveContext _driveResolution]_block_invoke.336 -> ___41-[PKCloudResolveContext _driveResolution]_block_invoke.335 : 160 -> 152
~ -[PKCloudResolveContext _checkFound:] : 428 -> 356
~ ___37-[PKCloudResolveContext _checkFound:]_block_invoke : 340 -> 276
~ -[PKCloudResolveContext description] : 236 -> 220
~ -[PKCloudResolveContext dealloc] : 316 -> 244
~ ____ZL27writePersistentURLToPrinterP17PKPrintJobRequestP5NSURLU13block_pointerFvP8NSNumberE_block_invoke : 620 -> 596
~ __ZL25writeRequestDataToPrinterP17PKPrintJobRequestP6NSDataU13block_pointerFvP8NSNumberE : 412 -> 424
~ __ZL22PHFetchOptionsFunctionv : 60 -> 12
~ __ZL15PHAssetFunctionv : 60 -> 12
~ __ZL29PHImageRequestOptionsFunctionv : 60 -> 12
~ __ZL22PHImageManagerFunctionv : 60 -> 12
~ ____ZL25writeRequestDataToPrinterP17PKPrintJobRequestP6NSDataU13block_pointerFvP8NSNumberE_block_invoke : 188 -> 184
~ ____ZL25writeRequestDataToPrinterP17PKPrintJobRequestP6NSDataU13block_pointerFvP8NSNumberE_block_invoke_3 : 248 -> 192
~ __ZL19jpegWithImageSourceP13CGImageSourceh : 580 -> 548
~ ____ZL34convertFromImageSourceAndWriteJPEGP17PKPrintJobRequestP13CGImageSourcebhU13block_pointerFvP8NSNumberE_block_invoke : 160 -> 156
~ ____ZL21convertToSharableJPEGP17PKPrintJobRequestP5NSURLU13block_pointerFvP8NSNumberE_block_invoke : 160 -> 156
~ ____Z23withDebuggableSemaphoreIU8__strongP12NSDictionaryET_P8NSStringdU13block_pointerFvU13block_pointerFvS3_EE_block_invoke_2 : 112 -> 96
~ -[PKPrintJobRequest initWithPrinterName:] : 152 -> 160
~ -[PKPrintJobRequest _establishedJob:fileHandle:] : 124 -> 120
~ -[PKPrintJobRequest startRequestCompletionHandler:] : 556 -> 544
~ ___51-[PKPrintJobRequest startRequestCompletionHandler:]_block_invoke : 256 -> 248
~ ___51-[PKPrintJobRequest startRequestCompletionHandler:]_block_invoke_2 : 200 -> 204
~ -[PKPrintJobRequest writeRequestData:completionHandler:] : 360 -> 368
~ ___56-[PKPrintJobRequest writeRequestData:completionHandler:]_block_invoke : 316 -> 252
~ -[PKPrintJobRequest finishRequest0:completionHandler:] : 316 -> 324
~ -[PKMutableJobState copyWithZone:] : 500 -> 440
~ ___42-[PKMutableJobState userCodableDictionary]_block_invoke : 180 -> 176
~ ___51-[PKMutableJobState initWithUserCodableDictionary:]_block_invoke : 232 -> 220
~ +[PKPrinterBrowser browserWithDelegate:infoDictionary:] : 132 -> 136
~ +[PKPrinterBrowser browserWithDelegate:infoDictionary:provenance:] : 136 -> 140
~ -[PKPrinterBrowser initWithDelegate:infoDictionary:provenance:] : 612 -> 540
~ -[PKPrinterBrowser dealloc] : 240 -> 236
~ -[PKPrinterBrowser setDelegate:] : 156 -> 148
~ -[PKPrinterBrowser btleRssiUpdated:rssi:] : 940 -> 904
~ ___41-[PKPrinterBrowser btleRssiUpdated:rssi:]_block_invoke : 132 -> 128
~ -[PKPrinterBrowser browserAdded:removed:] : 440 -> 444
~ -[PKPrinterBrowser printerAdded:more:] : 1476 -> 1420
~ ___38-[PKPrinterBrowser printerAdded:more:]_block_invoke : 276 -> 268
~ -[PKPrinterBrowser printerRemoved:more:] : 516 -> 492
~ ___40-[PKPrinterBrowser printerRemoved:more:]_block_invoke : 180 -> 176
~ -[PKPrinterBrowser btlePrinterFound:] : 1292 -> 1252
~ ___37-[PKPrinterBrowser btlePrinterFound:]_block_invoke : 176 -> 172
~ -[PKPrinterBrowser setPrinters:] : 64 -> 12
~ -[PKPrinterBrowser setBtDevices:] : 64 -> 12
~ -[PKSupply initWithName:markerType:colors:level:lowLevel:highLevel:] : 764 -> 748
~ -[PKSupply description] : 832 -> 788
~ -[PKSupply userCodableDictionary] : 768 -> 728
~ __ZL15UIColorFunctionv : 60 -> 12
~ ____ZL21makeUserCodableColorsP7NSArray_block_invoke : 116 -> 112
~ __ZN12SuppliesPoll20requestedAttributessEv : 200 -> 196
~ __Z23suppliesForPollResponsePK12SuppliesPoll : 1828 -> 1728
~ ___47+[PKTXTRecord txtRecordDictionaryForTxtRecord:]_block_invoke : 200 -> 192
~ -[PKTXTRecord initWithDictionary:] : 476 -> 468
~ -[PKTXTRecord initWithTXTRecordData:] : 272 -> 268
~ ___37-[PKTXTRecord initWithTXTRecordData:]_block_invoke : 208 -> 212
~ -[PKTXTRecord initWithNWTXTRecord:] : 116 -> 112
~ -[PKTXTRecord initWithCoder:] : 168 -> 164
~ -[PKTXTRecord _stringValueForKey:] : 196 -> 184
~ -[PKTXTRecord _checkMake:propertyName:maker:] : 360 -> 348
~ -[PKTXTRecord _checkMakeInt:propertyName:] : 100 -> 96
~ ___42-[PKTXTRecord _checkMakeInt:propertyName:]_block_invoke : 116 -> 108
~ -[PKTXTRecord _checkMakeString:propertyName:] : 56 -> 52
~ ___45-[PKTXTRecord _checkMakeString:propertyName:]_block_invoke : 56 -> 8
~ -[PKTXTRecord _checkMakeStringArray:propertyName:] : 56 -> 52
~ ___50-[PKTXTRecord _checkMakeStringArray:propertyName:]_block_invoke : 60 -> 56
~ -[PKTXTRecord _checkMakeAvail:propertyName:] : 100 -> 96
~ ___44-[PKTXTRecord _checkMakeAvail:propertyName:]_block_invoke : 132 -> 124
~ -[PKTXTRecord _checkMakeUUID:propertyName:] : 56 -> 52
~ -[PKTXTRecord _checkMakeURL:propertyName:] : 56 -> 52
~ ___42-[PKTXTRecord _checkMakeURL:propertyName:]_block_invoke : 52 -> 48
~ -[PKTXTRecord _checkMakeTLS:propertyName:] : 384 -> 328
~ -[PKTXTRecord _wrapProduct:] : 160 -> 152
~ -[PKTXTRecord printerProduct] : 128 -> 120
~ +[PKTray traysWithMediaSourceSupported:printerInputTrays:] : 284 -> 280
~ ___58+[PKTray traysWithMediaSourceSupported:printerInputTrays:]_block_invoke : 284 -> 276
~ +[PKTray filter:withBlock:] : 404 -> 408
~ +[PKTray trayWithString:andMediaSource:] : 128 -> 132
~ -[PKTray initWithString:andMediaSource:] : 816 -> 804
~ -[PKTray name] : 120 -> 112
~ -[PKTray localizedName] : 172 -> 160
~ -[PKTray mediaName] : 108 -> 100
~ -[PKTray isEmpty] : 148 -> 140
~ -[PKTray description] : 144 -> 136
~ -[PKTray initWithCoder:] : 212 -> 208
~ -[PKTray isEqual:] : 192 -> 184
~ -[PKPrinterBrowseInfo initWithBonjourName:txtRecord:] : 256 -> 252
~ __ZL28dictionaryWithLowercasedKeysP12NSDictionary : 620 -> 604
~ -[PKPrinterBrowseInfo initWithResolvedBonjourName:] : 268 -> 256
~ -[PKPrinterBrowseInfo printerURL] : 344 -> 340
~ -[PKPrinterBrowseInfo initWithCoder:] : 388 -> 372
~ -[PKPrinterBrowseInfo encodeWithCoder:] : 264 -> 244
~ -[PKPrinterBrowseInfo isEphemeral] : 84 -> 80
~ -[PKPrinterBrowseInfo compare:] : 1136 -> 1124
~ -[PKPrinterBrowseInfo hash] : 572 -> 536
~ -[PKPrinterBrowseInfo txtRecordObjectForKey:] : 248 -> 232
~ -[PKPrinterBrowseInfo type] : 380 -> 360
~ -[PKPrinterBrowseInfo uuid] : 228 -> 208
~ -[PKPrinterBrowseInfo isIPPS] : 76 -> 72
~ -[PKPrinterBrowseInfo makeAndModel] : 176 -> 168
~ -[PKPrinterBrowseInfo debugDescription] : 236 -> 220
~ -[PKPrinterBrowseInfo userCodableDictionary] : 208 -> 200
~ +[PKPrinterBrowseInfo(PrintKit) rollCacheGeneration] : 88 -> 84
~ -[PKPrinterBrowseInfo(PrintKit) resolveOnMainQueue:] : 336 -> 328
~ __ZL17findOrMakePrinterP19PKPrinterBrowseInfo : 664 -> 640
~ +[PKPrinterBrowseInfo(PrintKit) findPrinterWithBonjourEndpoint:withTimeout:completionHandler:] : 252 -> 256
~ ___94+[PKPrinterBrowseInfo(PrintKit) findPrinterWithBonjourEndpoint:withTimeout:completionHandler:]_block_invoke : 180 -> 168
~ ____ZL17findOrMakePrinterP19PKPrinterBrowseInfo_block_invoke : 192 -> 188
~ _PKParsePrinterStateReasons : 1000 -> 988
~ _PKCopyLocalizedPrinterStateReasons : 1476 -> 1460
~ _PKDefaultPortForScheme : 336 -> 268
~ _PKURLWithString : 516 -> 436
~ _PKURLWithUTF8String : 124 -> 116
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<PKPrintdRPC_BrowseClient_ClientProtocol>\""
- "@\"<PKPrinterBrowserDelegate>\""
- "@\"NSArray\""
- "@\"NSArray\"16@0:8"
- "@\"NSData\""
- "@\"NSData\"16@0:8"
- "@\"NSDate\""
- "@\"NSDate\"16@0:8"
- "@\"NSDictionary\""
- "@\"NSDictionary\"16@0:8"
- "@\"NSEnumerator\""
- "@\"NSFileHandle\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSObject\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@\"NSURLCredential\""
- "@\"NSUUID\""
- "@\"NSXPCConnection\""
- "@\"NWEndpoint\""
- "@\"PKMediaSize\""
- "@\"PKMutableJobState\""
- "@\"PKNotification\""
- "@\"PKNotifier\""
- "@\"PKPaper\""
- "@\"PKPaperList\""
- "@\"PKPrintJobRequest\""
- "@\"PKPrintSettings\""
- "@\"PKPrintSettings\"16@0:8"
- "@\"PKPrintdRPC_BrowseClient\""
- "@\"PKPrinter\""
- "@\"PKPrinterBonjourEndpoint\""
- "@\"PKPrinterBrowseInfo\""
- "@\"PKPrinterDescription\""
- "@\"PKPrinterTool_Client\""
- "@\"PK_ipp_collection_t\""
- "@\"PKiCloudPrinter\""
- "@16@0:8"
- "@20@0:8B16"
- "@20@0:8S16"
- "@20@0:8i16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@\"NSDictionary\"16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8d16"
- "@24@0:8i16i20"
- "@24@0:8q16"
- "@24@0:8r^{GET_PRINTER_ATTRIBUTES_Response=@}16"
- "@28@0:8@16i24"
- "@28@0:8i16@20"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16@?24"
- "@32@0:8@16d24"
- "@32@0:8@16i24i28"
- "@32@0:8i16i20B24B28"
- "@32@0:8r^{GET_PRINTER_ATTRIBUTES_Response=@}16@24"
- "@32@0:8{CGSize=dd}16"
- "@36@0:8@16i24@28"
- "@36@0:8{CGSize=dd}16B32"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24@?32"
- "@40@0:8@16@24Q32"
- "@40@0:8@16Q24@32"
- "@40@0:8@16d24@?32"
- "@40@0:8i16i20@24B32B36"
- "@40@0:8r^{GET_PRINTER_ATTRIBUTES_Response=@}16@24@32"
- "@40@0:8{CGSize=dd}16B32B36"
- "@44@0:8@16@24i32@36"
- "@44@0:8@16B24@28^B36"
- "@52@0:8r*16r*24r*32i40i44i48"
- "@64@0:8i16i20i24i28i32i36@40@48@56"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^{pwg_size_s=iiiiii}16"
- "B24@0:8r*16"
- "B24@0:8r^{GET_PRINTER_ATTRIBUTES_Response=@}16"
- "B32@0:8@16d24"
- "C"
- "I16@0:8"
- "IPPReadMutable"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "PKAuthNotification"
- "PKCloudResolveContext"
- "PKCollectionSpecialization"
- "PKDefaults"
- "PKFinishBailing"
- "PKFinishBinding"
- "PKFinishCoating"
- "PKFinishCovering"
- "PKFinishFinishingTemplate"
- "PKFinishFolding"
- "PKFinishImpositionTemplate"
- "PKFinishLaminating"
- "PKFinishMediaSheetsSupported"
- "PKFinishMediaSizeName"
- "PKFinishPunching"
- "PKFinishStitching"
- "PKFinishTrimming"
- "PKIPP"
- "PKJob"
- "PKJobUpdatableState"
- "PKMediaCol"
- "PKMediaName"
- "PKMediaSize"
- "PKMediaSourceProperties"
- "PKMutableJobState"
- "PKMutableMediaCol"
- "PKNotification"
- "PKNotifier"
- "PKPaper"
- "PKPaperList"
- "PKPrintJobRequest"
- "PKPrintSettings"
- "PKPrintdRPC_BrowseClient"
- "PKPrintdRPC_BrowseClient_ClientProtocol"
- "PKPrinter"
- "PKPrinterBonjourEndpoint"
- "PKPrinterBrowseInfo"
- "PKPrinterBrowser"
- "PKPrinterDescription"
- "PKPrinterTool_Client"
- "PKPropertyVisitable"
- "PKQuotaNotification"
- "PKSupply"
- "PKTXTRecord"
- "PKTray"
- "PKUserCodable"
- "PK_ipp_attribute_t"
- "PK_ipp_request_t"
- "PK_ipp_response_t"
- "PK_ipp_t"
- "PK_ipp_value_t"
- "PKiCloudPrinter"
- "PKiCloudPrinterWithInfo:"
- "PKiCloudPrinterWithPKPrinter:displayName:location:"
- "Paper"
- "PrintKit"
- "PrintKitPrivate"
- "PrintdRPCProtocol"
- "PrintertoolSideConstruction"
- "Printing"
- "Private"
- "Q16@0:8"
- "Q24@0:8@16"
- "Q24@0:8r^{GET_PRINTER_ATTRIBUTES_Response=@}16"
- "Q32@0:8@16@24"
- "S"
- "S16@0:8"
- "S32@0:8@16@24"
- "T#,R"
- "T@\"<PKPrinterBrowserDelegate>\",N,V_delegate"
- "T@\"NSArray\",&"
- "T@\"NSArray\",&,N,V_rolls"
- "T@\"NSArray\",&,V_duplexPapers"
- "T@\"NSArray\",&,V_photoPapers"
- "T@\"NSArray\",&,V_simplexPapers"
- "T@\"NSArray\",C"
- "T@\"NSArray\",C,V_finishings"
- "T@\"NSArray\",C,V_jobPrinterStateReasons"
- "T@\"NSArray\",C,V_jobStateReasons"
- "T@\"NSArray\",C,V_pageRanges_asStringArray"
- "T@\"NSArray\",C,V_papers"
- "T@\"NSArray\",R"
- "T@\"NSArray\",R,C"
- "T@\"NSArray\",R,D"
- "T@\"NSArray\",R,V_attrs_media_source_supported"
- "T@\"NSArray\",R,V_colors"
- "T@\"NSArray\",R,V_finishingTemplates"
- "T@\"NSArray\",R,V_finishings"
- "T@\"NSArray\",R,V_formats"
- "T@\"NSArray\",R,V_inputSlots"
- "T@\"NSArray\",R,V_jobPresets"
- "T@\"NSArray\",R,V_mediaColSupportedArray"
- "T@\"NSArray\",R,V_mediaTypes"
- "T@\"NSArray\",R,V_orientations"
- "T@\"NSArray\",R,V_outputBins"
- "T@\"NSArray\",R,V_outputModes"
- "T@\"NSArray\",R,V_quality"
- "T@\"NSArray\",R,V_sides"
- "T@\"NSArray\",R,V_trays"
- "T@\"NSData\",&,D"
- "T@\"NSData\",C,V_printerEndpointData"
- "T@\"NSData\",C,V_thumbnailImage"
- "T@\"NSData\",R"
- "T@\"NSData\",R,C"
- "T@\"NSData\",R,V_dataRemaining"
- "T@\"NSDate\",&,V_printerDescriptionTime"
- "T@\"NSDate\",&,V_startTime"
- "T@\"NSDate\",C,V_timeAtCompleted"
- "T@\"NSDate\",C,V_timeAtCreation"
- "T@\"NSDate\",C,V_timeAtProcessing"
- "T@\"NSDate\",R"
- "T@\"NSDate\",R,C"
- "T@\"NSDate\",R,V_endTime"
- "T@\"NSDate\",R,V_startTime"
- "T@\"NSDictionary\",&,V_iCloudInfo"
- "T@\"NSDictionary\",&,V_resolvedTXT"
- "T@\"NSDictionary\",&,V_trayDict"
- "T@\"NSDictionary\",R"
- "T@\"NSDictionary\",R,V_dids"
- "T@\"NSDictionary\",R,V_specialFeedOrientation"
- "T@\"NSDictionary\",R,V_translations"
- "T@\"NSDictionary\",R,V_txtRecord"
- "T@\"NSEnumerator\",&,V_enumerator"
- "T@\"NSMutableArray\",R,V_attrs"
- "T@\"NSMutableArray\",R,V_values"
- "T@\"NSMutableDictionary\",&,N,V_btDevices"
- "T@\"NSMutableDictionary\",&,N,V_printers"
- "T@\"NSNumber\",R"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_queue"
- "T@\"NSObject<OS_dispatch_queue>\",V_resultQueue"
- "T@\"NSSet\",R,V_attrs_document_format_supported"
- "T@\"NSSet\",R,V_attrs_printer_native_formats"
- "T@\"NSSet\",R,V_jpegFeatures"
- "T@\"NSSet\",R,V_mandatoryJobAttributes"
- "T@\"NSString\",&,V_alternateButtonTitle"
- "T@\"NSString\",&,V_baseName"
- "T@\"NSString\",&,V_defaultButtonTitle"
- "T@\"NSString\",&,V_defaultUsername"
- "T@\"NSString\",&,V_headerString"
- "T@\"NSString\",&,V_mediaClass"
- "T@\"NSString\",&,V_mediaName"
- "T@\"NSString\",&,V_messageString"
- "T@\"NSString\",&,V_passwordField"
- "T@\"NSString\",&,V_tag"
- "T@\"NSString\",&,V_usernameField"
- "T@\"NSString\",&,V_widthStr"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C"
- "T@\"NSString\",C,V_PIN"
- "T@\"NSString\",C,V_documentPassword"
- "T@\"NSString\",C,V_duplex"
- "T@\"NSString\",C,V_fileType"
- "T@\"NSString\",C,V_finishingTemplate"
- "T@\"NSString\",C,V_inputSlot"
- "T@\"NSString\",C,V_jobAccountID"
- "T@\"NSString\",C,V_jobName"
- "T@\"NSString\",C,V_jobPresetName"
- "T@\"NSString\",C,V_jobPrinterStateMessage"
- "T@\"NSString\",C,V_jobStateMessage"
- "T@\"NSString\",C,V_mediaType"
- "T@\"NSString\",C,V_orientation"
- "T@\"NSString\",C,V_outputBin"
- "T@\"NSString\",C,V_outputMode"
- "T@\"NSString\",C,V_pageScale"
- "T@\"NSString\",C,V_pageStackOrder"
- "T@\"NSString\",C,V_printQuality"
- "T@\"NSString\",C,V_printerDisplayName"
- "T@\"NSString\",C,V_printerLocation"
- "T@\"NSString\",C,V_thumbnailPosition"
- "T@\"NSString\",R"
- "T@\"NSString\",R,&,D"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,D"
- "T@\"NSString\",R,V_deviceID"
- "T@\"NSString\",R,V_driverformat"
- "T@\"NSString\",R,V_markerType"
- "T@\"NSString\",R,V_name"
- "T@\"NSString\",R,V_provenanceIdentifier"
- "T@\"NSURL\",&,V_quotaURL"
- "T@\"NSURL\",&,V_resolvedURL"
- "T@\"NSURL\",C,V_printerInfoURL"
- "T@\"NSURL\",C,V_printerSuppliesURL"
- "T@\"NSURL\",R"
- "T@\"NSURL\",R,D"
- "T@\"NSURL\",R,V_printerInfoURL"
- "T@\"NSURL\",R,V_quotaManagementURL"
- "T@\"NSURL\",R,V_suppliesInfoURL"
- "T@\"NSURLCredential\",R,V_credential"
- "T@\"NSUUID\",&,V_btleUUID"
- "T@\"NSUUID\",R,D"
- "T@\"NSXPCListener\",&"
- "T@\"NWEndpoint\",&,V_nwEndpoint"
- "T@\"PKMediaSize\",C,V_mediaSize"
- "T@\"PKMediaSize\",R"
- "T@\"PKMediaSourceProperties\",R"
- "T@\"PKMutableJobState\",R,C,V_updatableState"
- "T@\"PKNotifier\",R,V_notifier"
- "T@\"PKPaper\",C,V_paper"
- "T@\"PKPaperList\",R,V_paperList"
- "T@\"PKPrintJobRequest\",&,V_job_request"
- "T@\"PKPrintSettings\",C,V_printSettings"
- "T@\"PKPrintSettings\",C,V_settings"
- "T@\"PKPrintSettings\",R,C"
- "T@\"PKPrinter\",R,C"
- "T@\"PKPrinterBonjourEndpoint\",R,V_bonjourName"
- "T@\"PKPrinterBonjourEndpoint\",R,V_printerName"
- "T@\"PKPrinterBrowseInfo\",R,V_browseInfo"
- "T@\"PKPrinterDescription\",&,V_printerDescription"
- "T@\"PK_ipp_collection_t\",&,D"
- "T@\"PKiCloudPrinter\",&,V_iCloudPrinter"
- "T@\"PKiCloudPrinter\",&,V_icloudPrinter"
- "T@?,C,V_resultHandler"
- "TB,D"
- "TB,R"
- "TB,R,D"
- "TB,R,V_delegateRespondsToProximityUpdate"
- "TB,R,V_pin_required"
- "TB,R,V_print_scaling_supported"
- "TB,R,V_supportsColor"
- "TB,R,V_supportsDuplex"
- "TB,R,V_supportsPrintColorMode"
- "TB,R,V_type_has_color"
- "TB,R,V_type_has_duplex"
- "TB,V_annotationsImaged"
- "TB,V_hasMediaReady"
- "TI,V_request_id"
- "TQ,R"
- "TQ,R,D"
- "TQ,R,V_jobAccountIDSupport"
- "TQ,R,V_printer_type_from_cups_scalar"
- "TS,R,D"
- "TS,V_op_or_status"
- "Td,R,D"
- "Td,V_conversionFactor"
- "Td,V_heightInUnits"
- "Td,V_timeout"
- "Td,V_widthInUnits"
- "Ti,D"
- "Ti,R"
- "Ti,R,N"
- "Ti,R,V_documentPasswordSupported"
- "Ti,R,V_group_tag"
- "Ti,R,V_highLevel"
- "Ti,R,V_identifyActions"
- "Ti,R,V_kind"
- "Ti,R,V_level"
- "Ti,R,V_lowLevel"
- "Ti,R,V_max_jpeg"
- "Ti,R,V_max_jpeg_x"
- "Ti,R,V_max_jpeg_y"
- "Ti,R,V_max_pdf"
- "Ti,R,V_preferred_landscape"
- "Ti,R,V_provenance"
- "Ti,R,V_value_tag"
- "Ti,V_copies"
- "Ti,V_state"
- "Tq,R"
- "Tq,R,D"
- "Tq,R,V_accessState"
- "Tq,R,V_supplyType"
- "Tq,V_btleMeasuredPower"
- "Tq,V_localJobID"
- "Tq,V_mediaProgress"
- "Tq,V_mediaSheets"
- "Tq,V_mediaSheetsCompleted"
- "Tq,V_printerKind"
- "Tq,V_proximity"
- "Tq,V_remoteJobId"
- "Tq,V_state"
- "Tq,V_units"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R"
- "T{CGSize=dd},R"
- "T{_NSRange=QQ},R"
- "T{ipp_status_t=i},R"
- "T{ipp_value_date_t=[11C]},D"
- "T{ipp_value_range_t=ii},D"
- "T{ipp_value_resolution_t=iii},D"
- "T{ipp_value_string_t=@@},D"
- "URL"
- "URLByAppendingPathComponent:"
- "URLHostAllowedCharacterSet"
- "URLWithString:"
- "UTF8String"
- "UUIDString"
- "Vv16@0:8"
- "^{Printd_Parameters_ForColTypes=@}"
- "^{_NSZone=}16@0:8"
- "^{__CFRunLoopSource=}"
- "^{__CFUserNotification=}"
- "_PIN"
- "_accessState"
- "_addAttrToAppropriateGroup:"
- "_addAttributesInAppropriateGroups"
- "_addBoolean:name:value:"
- "_addCollection:name:value:"
- "_addInteger:valueTag:name:value:"
- "_addIntegers:valueTag:name:count:adder:"
- "_addOctetString:name:data:length:"
- "_addRange:name:lower:upper:"
- "_addRanges:name:values:"
- "_addResolution:name:unit:xres:yres:"
- "_addString:valueTag:name:lang:value:"
- "_addStrings:valueTag:name:lang:values:"
- "_allowedToPrintToThisPrinter"
- "_alternateButtonTitle"
- "_annotationsImaged"
- "_attrs_document_format_supported"
- "_attrs_media_source_supported"
- "_attrs_printer_native_formats"
- "_baseName"
- "_bonjourName"
- "_browseInfo"
- "_browserClient"
- "_btDevices"
- "_btleMeasuredPower"
- "_btleUUID"
- "_cachedBaseName"
- "_cachedPrinter"
- "_cachedUUID"
- "_calcDeviceID:"
- "_calcFinishingTemplates:"
- "_calcIdentifyActions:"
- "_calcInputSlots:"
- "_calcJobAccountIDSupport:"
- "_calcJobPresets:"
- "_calcMediaTypes:"
- "_calcOutputBins:"
- "_calcPrintScalingSupported:"
- "_calcPrinterDriverInfo:"
- "_calcSpecialFeedOrientation:"
- "_calculateFormats:"
- "_calculateMediaColSupportedArray:"
- "_calculateOutputModes:"
- "_calculatePaperList:"
- "_calculateQuality:"
- "_calculateSides:"
- "_checkAccessState:reply:"
- "_checkAvailable:queue:completionHandler:"
- "_checkFound:"
- "_checkMake:propertyName:maker:"
- "_checkMakeAvail:propertyName:"
- "_checkMakeInt:propertyName:"
- "_checkMakeString:propertyName:"
- "_checkMakeStringArray:propertyName:"
- "_checkMakeTLS:propertyName:"
- "_checkMakeURL:propertyName:"
- "_checkMakeUUID:propertyName:"
- "_collection"
- "_colors"
- "_complete:"
- "_completionHandler"
- "_conn_needsLock"
- "_conversionFactor"
- "_copies"
- "_copySettingGroup:"
- "_credential"
- "_dataRemaining"
- "_defaultButtonTitle"
- "_defaultUsername"
- "_delegate"
- "_delegateRespondsToProximityUpdate"
- "_deleteAttribute:"
- "_descriptionLeader"
- "_deviceID"
- "_dict"
- "_dids"
- "_documentPassword"
- "_documentPasswordSupported"
- "_driveResolution"
- "_driverformat"
- "_duplex"
- "_duplexPapers"
- "_endTime"
- "_endpointResolve:timeout:reply:"
- "_enumerator"
- "_establishedJob:fileHandle:"
- "_fileType"
- "_findAttribute0:valueTag:"
- "_finishingTemplate"
- "_finishingTemplates"
- "_finishings"
- "_formats"
- "_getPrinterDescription:assertReachability:reply:"
- "_hasMediaReady"
- "_headerString"
- "_heightInUnits"
- "_highLevel"
- "_iCloudInfo"
- "_iCloudPrinter"
- "_icloudPrinter"
- "_identifyActions"
- "_identifyPrinter:message:actions:"
- "_identifySelf:"
- "_infoDictionary"
- "_ingestAttrs:"
- "_ingestTxtRecord:"
- "_initWithAttrs:"
- "_initWithLowercasedDictionary:"
- "_inputSlot"
- "_inputSlots"
- "_interpretResult:responseDict:"
- "_jobAccountID"
- "_jobAccountIDSupport"
- "_jobName"
- "_jobPresetName"
- "_jobPresets"
- "_jobPrinterStateMessage"
- "_jobPrinterStateReasons"
- "_jobStateMessage"
- "_jobStateReasons"
- "_job_connection"
- "_job_request"
- "_jpegFeatures"
- "_kind"
- "_level"
- "_lowLevel"
- "_makeDict"
- "_makeFlags"
- "_makePrinterDeviceIDFromTxt"
- "_mandatoryJobAttributes"
- "_markerType"
- "_max_jpeg"
- "_max_jpeg_x"
- "_max_jpeg_y"
- "_max_pdf"
- "_mediaClass"
- "_mediaColSupportedArray"
- "_mediaName"
- "_mediaProgress"
- "_mediaSheets"
- "_mediaSheetsCompleted"
- "_mediaSize"
- "_mediaType"
- "_mediaTypes"
- "_messageString"
- "_notifier"
- "_nwEndpoint"
- "_op_or_status"
- "_orientation"
- "_orientations"
- "_originalCellFlag"
- "_originalWifiFlag"
- "_outputBin"
- "_outputBins"
- "_outputMode"
- "_outputModes"
- "_outstandingNote"
- "_outstandingRef"
- "_outstandingSource"
- "_pageRanges_asStringArray"
- "_pageScale"
- "_pageStackOrder"
- "_paper"
- "_paperList"
- "_papers"
- "_params"
- "_passwordField"
- "_photoPapers"
- "_pin_required"
- "_preferred_landscape"
- "_printQuality"
- "_printSettings"
- "_print_scaling_supported"
- "_printerDescription"
- "_printerDescriptionTime"
- "_printerDisplayName"
- "_printerEndpointData"
- "_printerInfoURL"
- "_printerKind"
- "_printerLocation"
- "_printerName"
- "_printerSuppliesURL"
- "_printer_type_from_cups_scalar"
- "_printers"
- "_provenance"
- "_provenanceIdentifier"
- "_proximity"
- "_quality"
- "_queryPrinter:attributes:reply:"
- "_queue"
- "_quotaManagementURL"
- "_quotaURL"
- "_realPathForTmpReply:"
- "_remoteJobId"
- "_removeKeychainItem:"
- "_request_id"
- "_resolveEndpoint:"
- "_resolve_finish_resolvedURL:resolvedTXT:"
- "_resolvedCallouts"
- "_resolvedTXT"
- "_resolvedURL"
- "_resultHandler"
- "_resultQueue"
- "_rolls"
- "_seenDict"
- "_setInitialAccessStateFromBrowseInfo"
- "_settings"
- "_setupDefaults"
- "_setupNewRequest"
- "_sides"
- "_simplexPapers"
- "_specialFeedOrientation"
- "_startTime"
- "_state"
- "_streamHandle"
- "_stringDict"
- "_stringValueForKey:"
- "_suppliesInfoURL"
- "_supplyType"
- "_supportsColor"
- "_supportsDuplex"
- "_supportsPrintColorMode"
- "_tag"
- "_thumbnailImage"
- "_thumbnailPosition"
- "_timeAtCompleted"
- "_timeAtCreation"
- "_timeAtProcessing"
- "_timeout"
- "_translations"
- "_trayDict"
- "_trays"
- "_type_has_color"
- "_type_has_duplex"
- "_units"
- "_updateAccessState:"
- "_updateDescription:browseInfo:"
- "_updateJobState:"
- "_usernameField"
- "_wantsComprehensivePaperList"
- "_widthInUnits"
- "_widthStr"
- "_withGroupingBehavior:"
- "_withPrinterAsync:"
- "_wrapProduct:"
- "abortJobCompletionHandler:"
- "absoluteSpoolDirectory"
- "absoluteString"
- "accessState"
- "activate"
- "addLastUsedPrinter:duplexMode:lastUsedSize:forPhoto:"
- "addNewEmptyAttribute:groupTag:valueTag:"
- "addNewEmptyValue"
- "addObject:"
- "addObjectsFromArray:"
- "addObserverForName:object:queue:usingBlock:"
- "addPaperSet:withCount:toArrays:"
- "addPrinter:moreComing:"
- "addPrinterToiCloud:"
- "addPrinterToiCloud:displayName:"
- "addPrinterToiCloud:displayName:location:"
- "addPrinterToiCloudWithInfo:"
- "addRSSIValue:"
- "addTimeInterval:"
- "addToMediaCol:"
- "adjustMargins:forDuplex:"
- "airPrintBeaconDiscoveryAllowed"
- "allKeys"
- "allObjects"
- "allValues"
- "alternateButtonTitle"
- "appendBytes:length:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "array"
- "arrayByAddingObject:"
- "arrayByAddingObjectsFromArray:"
- "arrayWithArray:"
- "arrayWithCapacity:"
- "arrayWithObject:"
- "arrayWithObjects:"
- "arrayWithObjects:count:"
- "attributesRequiredForPKPaperList"
- "attrs"
- "autorelease"
- "availableRollPapersPreferBorderless:"
- "base64EncodedStringWithOptions:"
- "baseName"
- "bonjourDisplayName"
- "boolValue"
- "bottomMarginInPoints"
- "browseInfo"
- "browseInfoForPrinter:timeout:completionHandler:"
- "browseInfoForPrinter:timeout:reply:"
- "browserAdded:removed:"
- "browserWithDelegate:"
- "browserWithDelegate:infoDictionary:"
- "browserWithDelegate:infoDictionary:provenance:"
- "btDevices"
- "btleMeasuredPower"
- "btlePrinterFound:"
- "btleRssiUpdated:rssi:"
- "btleUUID"
- "bundleWithIdentifier:"
- "bytes"
- "cancel"
- "cancelJob:"
- "cancelNotification:"
- "capitalizedString"
- "caseInsensitiveCompare:"
- "categorizePapers:"
- "class"
- "classesForSelector:argumentIndex:ofReply:"
- "closeAndReturnError:"
- "closeFile"
- "code"
- "compare:"
- "compare:options:"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "componentsWithString:encodingInvalidCharacters:"
- "conformsToProtocol:"
- "conjureMediaFromTXT:"
- "containsObject:"
- "containsString:"
- "containsValueForKey:"
- "conversionFactor"
- "copy"
- "copyCEndpoint"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createMediaColAndDoMargins:"
- "credential"
- "currentJob"
- "currentJobCompletionHandler:"
- "currentLocale"
- "customLocation"
- "customName"
- "cutToLength:"
- "cutToPWGLength:"
- "d16@0:8"
- "dataRemaining"
- "dataRepresentation"
- "dataWithBytes:length:"
- "dataWithCapacity:"
- "dataWithContentsOfURL:options:error:"
- "dataWithLength:"
- "date"
- "dateWithTimeIntervalSince1970:"
- "dealloc"
- "debugDescription"
- "decodeArrayOfObjectsOfClass:forKey:"
- "decodeBoolForKey:"
- "decodeDictionaryWithKeysOfClass:objectsOfClass:forKey:"
- "decodeIntForKey:"
- "decodeIntegerForKey:"
- "decodeObjectForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "defaultButtonTitle"
- "defaultCenter"
- "defaultGenericPaperForLocale:"
- "defaultManager"
- "defaultUsername"
- "delegate"
- "delegateRespondsToProximityUpdate"
- "description"
- "dictionary"
- "dictionaryFromTXTRecordData:"
- "dictionaryWithCapacity:"
- "dictionaryWithObjects:forKeys:count:"
- "dictionaryWithObjectsAndKeys:"
- "displayNameForPrintKitUI"
- "documentPapers"
- "doubleValue"
- "encodeBool:forKey:"
- "encodeInt:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "endTime"
- "endpointResolve:timeout:completionHandler:"
- "endpointWithBonjourString:"
- "endpointWithCEndpoint:"
- "endpointWithData:"
- "endpointWithURL:"
- "enumerateAttributes:"
- "enumerateByteRangesUsingBlock:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "enumerateValues:"
- "enumerator"
- "exceptionWithName:reason:userInfo:"
- "feedDirection"
- "feedOrientation"
- "fetchAssetsWithALAssetURLs:options:"
- "fileURLWithPath:isDirectory:"
- "filter:withBlock:"
- "filterPapers:usingBlock:"
- "filterUsingBlock:"
- "filteredArrayUsingPredicate:"
- "finalizeJob:completionHandler:"
- "findPrinterWithBonjourEndpoint:withTimeout:completionHandler:"
- "finishJobCompletionHandler:"
- "finishRequest0:completionHandler:"
- "finishRequest:completionHandler:"
- "finishRequestWithCancel:completionHandler:"
- "finishRequestWithCancel:reply:"
- "firstObject"
- "generic3_5x5Paper"
- "generic4x6Paper"
- "genericA4Paper"
- "genericA6Paper"
- "genericBorderlessWithName:"
- "genericHagakiPaper"
- "genericLegalPaper"
- "genericLetterPaper"
- "genericPRC32KPaper"
- "genericWithName:"
- "getBytes:range:"
- "getInt:"
- "getJobUpdateStatus:includeThumbnail:completionHandler:"
- "getJobUpdateStatus:includeThumbnail:reply:"
- "getLastUsedPrintersForCurrentNetworkCompletionHandler:"
- "getLastUsedPrintersForCurrentNetworkReply:"
- "getMargins:"
- "getRange:"
- "getRecentJobsCompletionHandler:"
- "getRecentJobsReply:"
- "getSupplyLevels:"
- "getThingType:"
- "getUpdatediCloudPrintersFromPrinterTool"
- "getiCloudPrintersReply:"
- "getiCloudPrintersWithCompletionHandler:"
- "globallyUniqueString"
- "group_tag"
- "hasIdentifyPrinterOp"
- "hasMatchingLoadedRoll:"
- "hasPrefix:"
- "hasPrintInfoSupported"
- "hasSuffix:"
- "hasValidIntegerTypesForXAndY"
- "hash"
- "headerString"
- "heightInUnits"
- "i16@0:8"
- "i24@0:8@16"
- "iCloudInfo"
- "iCloudPrinter"
- "iCloudPrinters"
- "iCloudPrintersSync"
- "icloudPrinter"
- "identifySelf"
- "imageableArea"
- "imageableAreaRect"
- "indexOfObject:"
- "indexOfObjectPassingTest:"
- "init"
- "initPKPrinterWithBrowseInfo:"
- "initWithAttributes:translations:"
- "initWithAttributes:txtRecord:translations:"
- "initWithBase64EncodedString:options:"
- "initWithBonjourName:txtRecord:"
- "initWithBonjourString:provenance:provenanceIdentifier:"
- "initWithBytes:length:encoding:"
- "initWithCoder:"
- "initWithCollection:"
- "initWithData:"
- "initWithData:encoding:"
- "initWithDelegate:infoDictionary:provenance:"
- "initWithDictionary:"
- "initWithEndpoint:provenance:provenanceIdentifier:"
- "initWithInfo:provenance:delegate:"
- "initWithJobID:updateState:"
- "initWithListenerEndpoint:"
- "initWithNWTXTRecord:"
- "initWithName:group:value:"
- "initWithName:markerType:colors:level:lowLevel:highLevel:"
- "initWithNotifier:notifyKind:"
- "initWithObjects:"
- "initWithOp:"
- "initWithPKCloudPrinter:timeout:completionHandler:"
- "initWithPaper:"
- "initWithPapers:"
- "initWithParams:translations:"
- "initWithPrinterName:"
- "initWithRed:green:blue:alpha:"
- "initWithRequest:"
- "initWithResolvedBonjourName:"
- "initWithServiceName:"
- "initWithSettings:"
- "initWithString:"
- "initWithString:andMediaSource:"
- "initWithTXT:"
- "initWithTXTRecord:"
- "initWithTXTRecordData:"
- "initWithTimeIntervalSince1970:"
- "initWithURL:txtRecord:provenance:provenanceIdentifier:"
- "initWithUUIDString:"
- "initWithUserCodableDictionary:"
- "initWithValidatedFormat:validFormatSpecifiers:error:"
- "initWithWidth:Height:Left:Top:Right:Bottom:localizedName:codeName:mediaInfo:"
- "insertObject:atIndex:"
- "intValue"
- "integerValue"
- "interfaceWithProtocol:"
- "intersectSet:"
- "intersectsSet:"
- "invalidate"
- "ippsIsRequired"
- "isAirPrintAllowed"
- "isAirPrintTrustedTLSRequirementEnforced"
- "isAirPrintiBeaconDiscoveryAllowed"
- "isBorderless"
- "isEmpty"
- "isEphemeral"
- "isEqual:"
- "isEqualSize:"
- "isEqualSizeAndMediaType:"
- "isEqualToBrowseInfo:"
- "isEqualToDictionary:"
- "isEqualToString:"
- "isFromMCProfile"
- "isIPPS"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isPaperReady:"
- "isProxy"
- "isRoll"
- "isValidColorString:"
- "isiCloudPrinter"
- "jobForJobID:"
- "jobTypesSupported"
- "jobTypesSupported:"
- "job_request"
- "jobs"
- "jobsCompletionHandler:"
- "keyedNameToVisitName:"
- "knownAirPrintIPPURLStrings"
- "knowsReadyPaperList"
- "lastObject"
- "lastUsedPrinters"
- "lastUsedPrintersCompletionHandler:"
- "lastUsedPrintersForPhoto:"
- "lastUsedPrintersForPhoto:completionHandler:"
- "length"
- "listenerProxy"
- "localizedJobOptions"
- "localizedName"
- "localizedNameFromDimensions"
- "localizedStatusString"
- "localizedStringForKey:value:table:"
- "localizedStringFromNumber:numberStyle:"
- "loggingDict"
- "loggingValue:"
- "logiCloudPrintersCompletionHandler:"
- "logiCloudPrintersReply:"
- "lowercaseString"
- "makeAndModel"
- "makeAuthAlert:challenge:"
- "makeEmptyResponse"
- "makeMediaCol"
- "makeNotice:message:"
- "makeQuotaAlert:message:quotaURL:"
- "makeRetry:message:"
- "makeSimpleAlert:message:"
- "makeTXTRecordWithURL:"
- "matchPaper:"
- "matchPaper:inList:"
- "matchedPaper:preferBorderless:withDuplexMode:didMatch:"
- "maxCutLength"
- "maxHeight"
- "mcProfilePrintersOnlyAllowed"
- "mediaClass"
- "mediaDictFromAttrs:translations:"
- "mediaInfo"
- "mediaKey"
- "mediaName"
- "mediaNameForWidth:Height:mediaType:Borderless:Simplex:"
- "mediaNameForWidth:height:borderless:simplex:"
- "mediaSize"
- "mediaSizeWithWidth:height:"
- "mediaSource"
- "mediaSourceProperties"
- "mediaTypeName"
- "messageString"
- "minCutLength"
- "minHeight"
- "mutableBytes"
- "mutableCopy"
- "nameWithoutSuffixes:"
- "nearbyURL"
- "nextObject"
- "notification:completedWithResult:"
- "notifier"
- "now"
- "null"
- "num_values"
- "number"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithFloat:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "nwEndpoint"
- "objectAtIndexedSubscript:"
- "objectEnumerator"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "opString"
- "op_or_status"
- "paperListForDuplexMode:"
- "paperListWithAttrs:translations:"
- "paperListWithPapers:"
- "paperListWithTXTRecord:"
- "paperSize"
- "paperWithAttributes:"
- "paperWithMarginsAdjustedForDuplexMode:"
- "papersForDocumentWithSize:andDuplex:"
- "papersForDocumentWithSize:scaleUpOnRoll:andDuplex:"
- "papersForPhotoWithSize:"
- "params"
- "parseMediaName:"
- "passwordField"
- "path"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "persistentNameRepresentationForPrintKitUI"
- "pkMediaNameWithString:"
- "pollForPrinterAttributes:completionHandler:"
- "pollForPrinterStatusQueue:completionHandler:"
- "port"
- "postNotificationName:object:"
- "predicateWithBlock:"
- "printInfoSupported"
- "printInfoSupportedDictionary"
- "printSettings"
- "printURL:ofType:printSettings:completionHandler:"
- "printURL:ofType:printSettings:completionHandlerWithLocalJobNumber:"
- "printer"
- "printerAdded:more:"
- "printerDescription"
- "printerDescriptionTime"
- "printerImageData"
- "printerLookupWithName:andTimeout:"
- "printerName"
- "printerRemoved:more:"
- "printerTool_checkAccessState:completionHandler:"
- "printerTool_getPrinterDescription:assertReachability:completionHandler:"
- "printerTool_identifyPrinter:message:actions:"
- "printerTool_queryPrinter:attributes:completionHandler:"
- "printerTool_realPathForTmp:"
- "printerTool_removeKeychainItem:"
- "printerURL"
- "printerWithBonjourEndpoint:discoveryTimeout:completionHandler:"
- "printerWithEndpointData:discoveryTime:completionHandler:"
- "printerWithName:"
- "printerWithName:discoveryTimeout:"
- "printerWithName:discoveryTimeout:completionHandler:"
- "printerWithURL:discoveryTimeout:completionHandler:"
- "printerWithiCloudPrinter:discoveryTime:completionHandler:"
- "printers"
- "processInfo"
- "proximity"
- "proximityUpdatedForPrinter:"
- "ptConn"
- "ptConn_locked"
- "q16@0:8"
- "q24@0:8@16"
- "q24@0:8r^{GET_PRINTER_ATTRIBUTES_Response=@}16"
- "q32@0:8@16@24"
- "q32@0:8r*16q24"
- "queue"
- "quotaURL"
- "r^{Printd_Parameters_ForColTypes=@}16@0:8"
- "range"
- "rangeOfData:options:range:"
- "rangeOfString:"
- "rangeOfString:options:"
- "rangeValue"
- "release"
- "remoteObjectProxy"
- "remoteObjectProxyWithErrorHandler:"
- "removeAllObjects"
- "removeCredentialsFromKeychain"
- "removeItemAtURL:error:"
- "removeLastObject"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "removeObserver:"
- "removePrinter:moreGoing:"
- "removePrinterFromiCloud:"
- "removePrinterFromiCloudWithInfo:"
- "replaceObjectAtIndex:withObject:"
- "replaceOrAddAttribute:withAttribute:settingGroup:"
- "replacePaperList:"
- "requestFromData:"
- "requestImageDataForAsset:options:resultHandler:"
- "request_id"
- "requiredPDL"
- "resetPKCloudData"
- "resolveOnMainQueue:"
- "resolveWithinPrinterToolWithTimeout:completionHandler:"
- "resolvedTXT"
- "resolvedURL"
- "respondsToSelector:"
- "responseFromData:"
- "responseFromRequest:"
- "resultHandler"
- "resultQueue"
- "retain"
- "retainCount"
- "rewriteURLAttributes:"
- "rollCacheGeneration"
- "rollReadyPaperListForDocumentWithContentSize:scaleUp:"
- "rollReadyPaperListForPhotoWithContentSize:"
- "rollReadyPaperListWithContentSize:forPhoto:"
- "scheme"
- "seenPrintersCompletionHandler:"
- "self"
- "serviceFromEndpoint:"
- "setAlternateButtonTitle:"
- "setAnnotationsImaged:"
- "setBaseName:"
- "setBoolean:"
- "setBtDevices:"
- "setBtleMeasuredPower:"
- "setBtleUUID:"
- "setByAddingObjectsFromArray:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setCollection:"
- "setConversionFactor:"
- "setCopies:"
- "setDate:"
- "setDefaultButtonTitle:"
- "setDefaultUsername:"
- "setDelegate:"
- "setDeliveryMode:"
- "setDocumentPassword:"
- "setDuplex:"
- "setDuplexPapers:"
- "setEnumerator:"
- "setExportedInterface:"
- "setExportedObject:"
- "setFileType:"
- "setFinishingTemplate:"
- "setFinishings:"
- "setFromUserCodableDictionary:"
- "setHasMediaReady:"
- "setHeaderString:"
- "setHeightInUnits:"
- "setHost:"
- "setICloudInfo:"
- "setICloudPrinter:"
- "setICloudPrinters:"
- "setIcloudPrinter:"
- "setInputSlot:"
- "setInteger:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setJobAccountID:"
- "setJobName:"
- "setJobPresetName:"
- "setJobPrinterStateMessage:"
- "setJobPrinterStateReasons:"
- "setJobStateMessage:"
- "setJobStateReasons:"
- "setJob_request:"
- "setLastUsedPrintersForCurrentNetwork:"
- "setLength:"
- "setListenerProxy:"
- "setLocalJobID:"
- "setMarginsTop:left:bottom:right:"
- "setMaximumFractionDigits:"
- "setMediaClass:"
- "setMediaName:"
- "setMediaProgress:"
- "setMediaSheets:"
- "setMediaSheetsCompleted:"
- "setMediaSize:"
- "setMediaSource:"
- "setMediaType:"
- "setMessageString:"
- "setNSName:"
- "setNetworkAccessAllowed:"
- "setNwEndpoint:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOp_or_status:"
- "setOrientation:"
- "setOutputBin:"
- "setOutputMode:"
- "setPIN:"
- "setPageRanges:"
- "setPageRanges_asStringArray:"
- "setPageScale:"
- "setPageStackOrder:"
- "setPaper:"
- "setPapers:"
- "setPasswordField:"
- "setPath:"
- "setPhotoPapers:"
- "setPort:"
- "setPrintQuality:"
- "setPrintSettings:"
- "setPrinterDescription:"
- "setPrinterDescriptionTime:"
- "setPrinterDisplayName:"
- "setPrinterEndpointData:"
- "setPrinterInfoURL:"
- "setPrinterKind:"
- "setPrinterLocation:"
- "setPrinterSuppliesURL:"
- "setPrinters:"
- "setProximity:"
- "setQuery:"
- "setQueue:"
- "setQuotaURL:"
- "setRange:"
- "setRemoteJobId:"
- "setRemoteObjectInterface:"
- "setRequest_id:"
- "setResolution:"
- "setResolvedTXT:"
- "setResolvedURL:"
- "setResultHandler:"
- "setResultQueue:"
- "setRolls:"
- "setScheme:"
- "setSettings:"
- "setSimplexPapers:"
- "setStartTime:"
- "setState:"
- "setString:"
- "setSynchronous:"
- "setTag:"
- "setThumbnailImage:"
- "setThumbnailPosition:"
- "setTimeAtCompleted:"
- "setTimeAtCreation:"
- "setTimeAtProcessing:"
- "setTimeout:"
- "setTrayDict:"
- "setUnits:"
- "setUnknown:"
- "setUsernameField:"
- "setValue:forKey:"
- "setValueTag:"
- "setVersion:"
- "setWantsIncrementalChangeDetails:"
- "setWidthInUnits:"
- "setWidthStr:"
- "setWithArray:"
- "setiCloudPrinters:"
- "sharedClient"
- "sharedConnection"
- "sharedNotifier"
- "sizeAndImageableCompare:"
- "sizeMediaTypeAndImageableCompare:"
- "sortedArrayUsingComparator:"
- "sortedArrayUsingSelector:"
- "standardRequestedAttributes"
- "start"
- "startBrowsing"
- "startBrowsing:provenance:"
- "startNotification:options:dict:"
- "startRequestCompletionHandler:"
- "startStreamingRequest:printSettings:completionHandler:"
- "startStreamingRequest:printSettings:reply:"
- "startTime"
- "startiCloudListening"
- "string"
- "stringByAddingPercentEncodingWithAllowedCharacters:"
- "stringByAppendingString:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringFromNumber:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "stringWithValidatedFormat:validFormatSpecifiers:error:"
- "subarrayWithRange:"
- "subdataWithRange:"
- "substringFromIndex:"
- "substringToIndex:"
- "substringWithRange:"
- "superclass"
- "supportsJobAccountID"
- "supportsSecureCoding"
- "tag"
- "tersePaperFrom:withMediaInfo:"
- "tersePaperFrom:withRequest:"
- "timeIntervalSince1970"
- "timeIntervalSinceDate:"
- "timeout"
- "topMarginInPoints"
- "toss_last_value"
- "trayWithString:andMediaSource:"
- "traysWithMediaSourceSupported:printerInputTrays:"
- "txtRecord"
- "txtRecordDictionaryForTxtRecord:"
- "txtRecordObjectForKey:"
- "txtRecordReconstructingAttributes"
- "unarchivedObjectOfClass:fromData:error:"
- "unitStr"
- "units"
- "unlockWithCompletionHandler:"
- "unsignedIntValue"
- "unsignedIntegerValue"
- "update"
- "updateCompletionHandler:"
- "updateiCloudPrinter:withInfo:forInfoKey:"
- "updateiCloudPrinterCustomLocation:customLocation:"
- "updateiCloudPrinterCustomName:customName:"
- "updateiCloudPrinterDisplayName:displayName:"
- "updateiCloudPrinterInfo"
- "updateiCloudPrinterInfo:withNewInfo:forInfoKey:"
- "updateiCloudPrinterLocation:location:"
- "urfIsOptional"
- "uriMatchesMCProfileAdded:"
- "useMetric"
- "userCodableDictionary"
- "usernameField"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v20@0:8S16"
- "v20@0:8i16"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"PKPrinterBonjourEndpoint\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSArray\">16"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSArray\">16"
- "v24@0:8@?<v@?@\"NSString\"@\"NSArray\">16"
- "v24@0:8@?<v@?@\"NSURL\">16"
- "v24@0:8^{Visitor=^^?}16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v24@0:8r^{GET_PRINTER_ATTRIBUTES_Response=@}16"
- "v24@0:8{ipp_value_range_t=ii}16"
- "v27@0:8{ipp_value_date_t=[11C]}16"
- "v28@0:8@16B24"
- "v28@0:8B16@?20"
- "v28@0:8B16@?<v@?@\"NSNumber\">20"
- "v28@0:8{ipp_value_resolution_t=iii}16"
- "v32@0:8@\"NSDictionary\"16Q24"
- "v32@0:8@\"NSSet\"16@\"NSSet\"24"
- "v32@0:8@\"PKPrinterBonjourEndpoint\"16@?<v@?q>24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16Q24"
- "v32@0:8Q16@24"
- "v32@0:8^{__CFUserNotification=}16Q24"
- "v32@0:8i16@20B28"
- "v32@0:8i16B20@?24"
- "v32@0:8i16B20@?<v@?@\"PKMutableJobState\">24"
- "v32@0:8i16i20i24i28"
- "v32@0:8{ipp_value_string_t=@@}16"
- "v36@0:8@\"PKPrinterBonjourEndpoint\"16B24@?<v@?@\"PKPrinterDescription\"@\"PKPrinterBrowseInfo\">28"
- "v36@0:8@16@24i32"
- "v36@0:8@16B24@?28"
- "v36@0:8^@16i24^@28"
- "v36@0:8i16@20@28"
- "v36@0:8i16@20i28i32"
- "v36@0:8i16i20@24i32"
- "v40@0:8@\"NSDictionary\"16@\"NSObject\"24@\"NSString\"32"
- "v40@0:8@\"NWEndpoint\"16d24@?<v@?@\"NSURL\"@\"NSDictionary\">32"
- "v40@0:8@\"PKPrinterBonjourEndpoint\"16@\"NSArray\"24@?<v@?@\"NSData\">32"
- "v40@0:8@\"PKPrinterBonjourEndpoint\"16@\"NSString\"24@\"NSArray\"32"
- "v40@0:8@\"PKPrinterBonjourEndpoint\"16@\"PKPrintSettings\"24@?<v@?@\"NSFileHandle\">32"
- "v40@0:8@\"PKPrinterBonjourEndpoint\"16d24@?<v@?@\"PKPrinterBrowseInfo\">32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16Q24@32"
- "v40@0:8@16d24@?32"
- "v40@0:8@16i24i28@?32"
- "v40@0:8d16@24@?32"
- "v40@0:8i16@20i28i32i36"
- "v40@0:8i16@20r^v28i36"
- "v48@0:8@16@24@32@?40"
- "v48@0:8i16i20@24@32@40"
- "v48@0:8i16i20@24Q32@?40"
- "v52@0:8@16@24{CGSize=dd}32B48"
- "valueWithBoolean:"
- "valueWithBytes:objCType:"
- "valueWithInteger:"
- "valueWithRange:"
- "valueWithString:"
- "value_tag"
- "visitProperties:"
- "wantsComprehensivePaperList"
- "widthInUnits"
- "widthStr"
- "willAdjustMarginsForDuplexMode:"
- "withDescriptionAsync:"
- "withNewAttr:groupTag:valueTag:apply:"
- "withNewEmptyValue:"
- "withResolvedTXT:"
- "withResolvedURL:"
- "writeData:error:"
- "writeRequestData:completionHandler:"
- "xDimension"
- "x_name"
- "x_payload"
- "yDimension"
- "yDimensionIsRange"
- "yRange"
- "zone"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "{CGSize=dd}16@0:8"
- "{_NSRange=QQ}16@0:8"
- "{_NSRange=QQ}24@0:8@16"
- "{ipp_status_t=i}16@0:8"
- "{ipp_value_date_t=[11C]}16@0:8"
- "{ipp_value_range_t=ii}16@0:8"
- "{ipp_value_resolution_t=iii}16@0:8"
- "{ipp_value_string_t=@@}16@0:8"

```
