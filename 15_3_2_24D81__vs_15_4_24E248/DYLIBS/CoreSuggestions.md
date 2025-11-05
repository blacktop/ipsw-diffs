## CoreSuggestions

> `/System/Library/PrivateFrameworks/CoreSuggestions.framework/Versions/A/CoreSuggestions`

```diff

-1271.10.0.0.0
-  __TEXT.__text: 0x8c090
-  __TEXT.__auth_stubs: 0xb70
-  __TEXT.__objc_methlist: 0x8294
-  __TEXT.__const: 0x868
-  __TEXT.__gcc_except_tab: 0x800
-  __TEXT.__cstring: 0x7753
-  __TEXT.__oslogstring: 0x218d
+1276.10.4.0.0
+  __TEXT.__text: 0x91280
+  __TEXT.__auth_stubs: 0xbd0
+  __TEXT.__objc_methlist: 0x9bfc
+  __TEXT.__const: 0x858
+  __TEXT.__dlopen_cstrs: 0x74
+  __TEXT.__gcc_except_tab: 0x868
+  __TEXT.__cstring: 0x7981
+  __TEXT.__oslogstring: 0x21c9
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x2170
-  __TEXT.__objc_classname: 0x139c
-  __TEXT.__objc_methname: 0x10ec4
-  __TEXT.__objc_methtype: 0x5241
-  __TEXT.__objc_stubs: 0x9160
-  __DATA_CONST.__got: 0x6f8
-  __DATA_CONST.__const: 0x1550
-  __DATA_CONST.__objc_classlist: 0x4a8
+  __TEXT.__unwind_info: 0x2260
+  __TEXT.__objc_classname: 0x13f1
+  __TEXT.__objc_methname: 0x11709
+  __TEXT.__objc_methtype: 0x52a0
+  __TEXT.__objc_stubs: 0x9760
+  __DATA_CONST.__got: 0x728
+  __DATA_CONST.__const: 0x1588
+  __DATA_CONST.__objc_classlist: 0x4d8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3cf8
+  __DATA_CONST.__objc_selrefs: 0x3fc8
   __DATA_CONST.__objc_protorefs: 0x70
-  __DATA_CONST.__objc_superrefs: 0x438
+  __DATA_CONST.__objc_superrefs: 0x468
   __DATA_CONST.__objc_arraydata: 0x280
-  __AUTH_CONST.__auth_got: 0x5c8
-  __AUTH_CONST.__const: 0x1b90
-  __AUTH_CONST.__cfstring: 0xa0c0
-  __AUTH_CONST.__objc_const: 0xfe70
-  __AUTH_CONST.__objc_intobj: 0x120
+  __AUTH_CONST.__auth_got: 0x5f8
+  __AUTH_CONST.__const: 0x1c50
+  __AUTH_CONST.__cfstring: 0xa380
+  __AUTH_CONST.__objc_const: 0xe428
+  __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH.__objc_data: 0x640
-  __DATA.__objc_ivar: 0x824
+  __AUTH.__objc_data: 0x820
+  __DATA.__objc_ivar: 0x884
   __DATA.__data: 0x1150
-  __DATA.__bss: 0x3e8
+  __DATA.__bss: 0x400
   __DATA_DIRTY.__objc_data: 0x2850
   __DATA_DIRTY.__data: 0x100
   __DATA_DIRTY.__bss: 0x40

   - /System/Library/PrivateFrameworks/ProactiveEventTracker.framework/Versions/A/ProactiveEventTracker
   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/Versions/A/ProactiveSupport
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E3AF7174-CEDE-3C5A-9874-DFBEEDC64015
-  Functions: 3254
-  Symbols:   7300
-  CStrings:  6214
+  UUID: 0E7CB872-9703-37C9-9090-38F6DAF2C40E
+  Functions: 3383
+  Symbols:   7583
+  CStrings:  6383
 
Symbols:
+ +[SGEntityTag cascadeEntitySetVersion:]
+ +[SGEntityTag eventExtractedFromLLM]
+ +[SGEventGeocode addressStringFromPIRStructuredAddress:]
+ +[SGEventGeocode appendToAddress:addressComponentToAppend:withSeparator:]
+ +[SGEventGeocode geocodeAddressUsingPIR:withCallback:]
+ +[SGEventGeocode pirResultFromData:withDistance:fromCoordinates:]
+ +[SGEventGeocode pirResultWithHighestScoreFromData:]
+ +[SGGeoListSnippet poisType]
+ +[SGPreferenceStorage preExtractionMaxDocumentAgeDays]
+ +[SGStructuredAddress dependentLocalityType]
+ -[SGAspireResult .cxx_destruct]
+ -[SGAspireResult copyTo:]
+ -[SGAspireResult copyWithZone:]
+ -[SGAspireResult description]
+ -[SGAspireResult dictionaryRepresentation]
+ -[SGAspireResult geoList]
+ -[SGAspireResult hasGeoList]
+ -[SGAspireResult hash]
+ -[SGAspireResult isEqual:]
+ -[SGAspireResult mergeFrom:]
+ -[SGAspireResult readFrom:]
+ -[SGAspireResult setGeoList:]
+ -[SGAspireResult writeTo:]
+ -[SGEntityTag eventSourceMetadata]
+ -[SGEntityTag isCascadeEntitySetVersion]
+ -[SGGeoListSnippet .cxx_destruct]
+ -[SGGeoListSnippet addPois:]
+ -[SGGeoListSnippet clearPois]
+ -[SGGeoListSnippet copyTo:]
+ -[SGGeoListSnippet copyWithZone:]
+ -[SGGeoListSnippet description]
+ -[SGGeoListSnippet dictionaryRepresentation]
+ -[SGGeoListSnippet hash]
+ -[SGGeoListSnippet isEqual:]
+ -[SGGeoListSnippet mergeFrom:]
+ -[SGGeoListSnippet poisAtIndex:]
+ -[SGGeoListSnippet poisCount]
+ -[SGGeoListSnippet pois]
+ -[SGGeoListSnippet readFrom:]
+ -[SGGeoListSnippet setPois:]
+ -[SGGeoListSnippet writeTo:]
+ -[SGGeoPoi .cxx_destruct]
+ -[SGGeoPoi address]
+ -[SGGeoPoi copyTo:]
+ -[SGGeoPoi copyWithZone:]
+ -[SGGeoPoi description]
+ -[SGGeoPoi dictionaryRepresentation]
+ -[SGGeoPoi hasAddress]
+ -[SGGeoPoi hasPrefGeocode]
+ -[SGGeoPoi hasTitle]
+ -[SGGeoPoi hasUrl]
+ -[SGGeoPoi hash]
+ -[SGGeoPoi isEqual:]
+ -[SGGeoPoi mergeFrom:]
+ -[SGGeoPoi prefGeocode]
+ -[SGGeoPoi readFrom:]
+ -[SGGeoPoi setAddress:]
+ -[SGGeoPoi setPrefGeocode:]
+ -[SGGeoPoi setTitle:]
+ -[SGGeoPoi setUrl:]
+ -[SGGeoPoi title]
+ -[SGGeoPoi url]
+ -[SGGeoPoi writeTo:]
+ -[SGPIRResult .cxx_destruct]
+ -[SGPIRResult address]
+ -[SGPIRResult initWithLabel:address:latitude:longitude:timezone:]
+ -[SGPIRResult label]
+ -[SGPIRResult latitude]
+ -[SGPIRResult longitude]
+ -[SGPIRResult timezone]
+ -[SGPoint copyTo:]
+ -[SGPoint copyWithZone:]
+ -[SGPoint description]
+ -[SGPoint dictionaryRepresentation]
+ -[SGPoint hasLat]
+ -[SGPoint hasLng]
+ -[SGPoint hash]
+ -[SGPoint isEqual:]
+ -[SGPoint lat]
+ -[SGPoint lng]
+ -[SGPoint mergeFrom:]
+ -[SGPoint readFrom:]
+ -[SGPoint setHasLat:]
+ -[SGPoint setHasLng:]
+ -[SGPoint setLat:]
+ -[SGPoint setLng:]
+ -[SGPoint writeTo:]
+ -[SGStructuredAddress .cxx_destruct]
+ -[SGStructuredAddress addDependentLocality:]
+ -[SGStructuredAddress administrativeAreaCode]
+ -[SGStructuredAddress administrativeArea]
+ -[SGStructuredAddress clearDependentLocalitys]
+ -[SGStructuredAddress copyTo:]
+ -[SGStructuredAddress copyWithZone:]
+ -[SGStructuredAddress countryCode]
+ -[SGStructuredAddress country]
+ -[SGStructuredAddress dependentLocalityAtIndex:]
+ -[SGStructuredAddress dependentLocalitysCount]
+ -[SGStructuredAddress dependentLocalitys]
+ -[SGStructuredAddress description]
+ -[SGStructuredAddress dictionaryRepresentation]
+ -[SGStructuredAddress hasAdministrativeAreaCode]
+ -[SGStructuredAddress hasAdministrativeArea]
+ -[SGStructuredAddress hasCountryCode]
+ -[SGStructuredAddress hasCountry]
+ -[SGStructuredAddress hasLocality]
+ -[SGStructuredAddress hasPostCode]
+ -[SGStructuredAddress hasSubAdministrativeArea]
+ -[SGStructuredAddress hasSubThroughfare]
+ -[SGStructuredAddress hasThoroughfare]
+ -[SGStructuredAddress hash]
+ -[SGStructuredAddress isEqual:]
+ -[SGStructuredAddress locality]
+ -[SGStructuredAddress mergeFrom:]
+ -[SGStructuredAddress postCode]
+ -[SGStructuredAddress readFrom:]
+ -[SGStructuredAddress setAdministrativeArea:]
+ -[SGStructuredAddress setAdministrativeAreaCode:]
+ -[SGStructuredAddress setCountry:]
+ -[SGStructuredAddress setCountryCode:]
+ -[SGStructuredAddress setDependentLocalitys:]
+ -[SGStructuredAddress setLocality:]
+ -[SGStructuredAddress setPostCode:]
+ -[SGStructuredAddress setSubAdministrativeArea:]
+ -[SGStructuredAddress setSubThroughfare:]
+ -[SGStructuredAddress setThoroughfare:]
+ -[SGStructuredAddress subAdministrativeArea]
+ -[SGStructuredAddress subThroughfare]
+ -[SGStructuredAddress thoroughfare]
+ -[SGStructuredAddress writeTo:]
+ DocumentUnderstandingClientLibraryCore.frameworkLibrary
+ GCC_except_table1052
+ GCC_except_table1056
+ GCC_except_table1060
+ GCC_except_table1294
+ GCC_except_table1443
+ GCC_except_table1529
+ GCC_except_table1532
+ GCC_except_table1534
+ GCC_except_table1862
+ GCC_except_table2309
+ GCC_except_table2311
+ GCC_except_table2348
+ GCC_except_table2403
+ GCC_except_table2774
+ GCC_except_table3275
+ GCC_except_table3294
+ GCC_except_table3301
+ GCC_except_table3315
+ GCC_except_table389
+ GCC_except_table494
+ GCC_except_table513
+ GCC_except_table522
+ GCC_except_table527
+ GCC_except_table528
+ GCC_except_table530
+ GCC_except_table541
+ GCC_except_table622
+ GCC_except_table632
+ GCC_except_table633
+ GCC_except_table636
+ GCC_except_table637
+ GCC_except_table849
+ GCC_except_table852
+ GCC_except_table854
+ GCC_except_table859
+ GCC_except_table864
+ GCC_except_table883
+ OBJC_IVAR_$_SGAspireResult._geoList
+ OBJC_IVAR_$_SGGeoListSnippet._pois
+ OBJC_IVAR_$_SGGeoPoi._address
+ OBJC_IVAR_$_SGGeoPoi._prefGeocode
+ OBJC_IVAR_$_SGGeoPoi._title
+ OBJC_IVAR_$_SGGeoPoi._url
+ OBJC_IVAR_$_SGPIRResult._address
+ OBJC_IVAR_$_SGPIRResult._label
+ OBJC_IVAR_$_SGPIRResult._latitude
+ OBJC_IVAR_$_SGPIRResult._longitude
+ OBJC_IVAR_$_SGPIRResult._timezone
+ OBJC_IVAR_$_SGPoint._has
+ OBJC_IVAR_$_SGPoint._lat
+ OBJC_IVAR_$_SGPoint._lng
+ OBJC_IVAR_$_SGStructuredAddress._administrativeArea
+ OBJC_IVAR_$_SGStructuredAddress._administrativeAreaCode
+ OBJC_IVAR_$_SGStructuredAddress._country
+ OBJC_IVAR_$_SGStructuredAddress._countryCode
+ OBJC_IVAR_$_SGStructuredAddress._dependentLocalitys
+ OBJC_IVAR_$_SGStructuredAddress._locality
+ OBJC_IVAR_$_SGStructuredAddress._postCode
+ OBJC_IVAR_$_SGStructuredAddress._subAdministrativeArea
+ OBJC_IVAR_$_SGStructuredAddress._subThroughfare
+ OBJC_IVAR_$_SGStructuredAddress._thoroughfare
+ _OBJC_CLASS_$_SGAspireResult
+ _OBJC_CLASS_$_SGGeoListSnippet
+ _OBJC_CLASS_$_SGGeoPoi
+ _OBJC_CLASS_$_SGPIRResult
+ _OBJC_CLASS_$_SGPoint
+ _OBJC_CLASS_$_SGStructuredAddress
+ _OBJC_METACLASS_$_SGAspireResult
+ _OBJC_METACLASS_$_SGGeoListSnippet
+ _OBJC_METACLASS_$_SGGeoPoi
+ _OBJC_METACLASS_$_SGPIRResult
+ _OBJC_METACLASS_$_SGPoint
+ _OBJC_METACLASS_$_SGStructuredAddress
+ _PBDataWriterWriteDoubleField
+ _PBDataWriterWriteSubmessage
+ _PBReaderPlaceMark
+ _PBReaderRecallMark
+ _SGAspireResultReadFrom
+ _SGGeoListSnippetReadFrom
+ _SGGeoPoiReadFrom
+ _SGPointReadFrom
+ _SGStructuredAddressReadFrom
+ __110-[SGSuggestionsService namesForDetail:limitTo:prependMaybe:onlySignificant:supportsInfoLookup:withCompletion:]_block_invoke.645
+ __110-[SGSuggestionsService namesForDetail:limitTo:prependMaybe:onlySignificant:supportsInfoLookup:withCompletion:]_block_invoke.646
+ __110-[SGSuggestionsService namesForDetail:limitTo:prependMaybe:onlySignificant:supportsInfoLookup:withCompletion:]_block_invoke.666
+ __110-[SGSuggestionsService namesForDetail:limitTo:prependMaybe:onlySignificant:supportsInfoLookup:withCompletion:]_block_invoke.667
+ __16-[SGFuture wait]_block_invoke.25
+ __29-[SGFuture _wait:forSyncAPI:]_block_invoke.27
+ __29-[SGFuture _wait:forSyncAPI:]_block_invoke.28
+ __31+[SGEventGeocode geocodeEvent:]_block_invoke.124
+ __31+[SGEventGeocode geocodeEvent:]_block_invoke.126
+ __36-[SGSuggestionsService sendRTCLogs:]_block_invoke.773
+ __38-[SGDaemonConnection _connectToServer]_block_invoke.12
+ __39+[SGSuggestionsService prepareForQuery]_block_invoke.461
+ __41+[SGDSuggestManagerInterface _initialize]_block_invoke.305
+ __41+[SGDSuggestManagerInterface _initialize]_block_invoke_2.332
+ __43-[SGSuggestionsService cacheSnapshotFuture]_block_invoke.618
+ __43-[SGSuggestionsService cacheSnapshotFuture]_block_invoke.619
+ __43-[SGSuggestionsService cacheSnapshotFuture]_block_invoke.629
+ __45+[SGFuture futureForObject:withKey:onCreate:]_block_invoke.56
+ __47-[SGRemoteObjectProxy _forwardStackInvocation:]_block_invoke.23
+ __47-[SGRemoteObjectProxy _forwardStackInvocation:]_block_invoke.36
+ __47-[SGRemoteObjectProxy _forwardStackInvocation:]_block_invoke.39
+ __47-[SGRemoteObjectProxy _forwardStackInvocation:]_block_invoke.48
+ __47-[SGRemoteObjectProxy _forwardStackInvocation:]_block_invoke_2.27
+ __56-[SGDaemonConnection waitUntilReturn:withTimeout:error:]_block_invoke.18
+ __56-[SGDaemonConnection waitUntilReturn:withTimeout:error:]_block_invoke.19
+ __65-[SGKeyValueCacheFile setValueIfNotPresentWithDict:fromRecordId:]_block_invoke.43
+ __70-[NSString(SGNSString) sg_dataEnumeratorUsingEncoding:nullTerminated:]_block_invoke.35
+ __72+[SGEventGeocode geocodeLocation:usingMode:withGeoFilters:withCallback:]_block_invoke.102
+ __72+[SGEventGeocode geocodeLocation:usingMode:withGeoFilters:withCallback:]_block_invoke.103
+ __72+[SGEventGeocode geocodeLocation:usingMode:withGeoFilters:withCallback:]_block_invoke.105
+ __72+[SGEventGeocode geocodeLocation:usingMode:withGeoFilters:withCallback:]_block_invoke.113
+ __72+[SGEventGeocode geocodeLocation:usingMode:withGeoFilters:withCallback:]_block_invoke.117
+ __72+[SGEventGeocode geocodeLocation:usingMode:withGeoFilters:withCallback:]_block_invoke.91
+ __72+[SGEventGeocode geocodeLocation:usingMode:withGeoFilters:withCallback:]_block_invoke_2.114
+ __72+[SGEventGeocode geocodeLocation:usingMode:withGeoFilters:withCallback:]_block_invoke_2.118
+ __81-[SGMessagesSuggestionsService suggestionsFromMessage:options:completionHandler:]_block_invoke.106
+ __Block_byref_object_copy_.10024
+ __Block_byref_object_copy_.1013
+ __Block_byref_object_copy_.1360
+ __Block_byref_object_copy_.1958
+ __Block_byref_object_copy_.2229
+ __Block_byref_object_copy_.23
+ __Block_byref_object_copy_.3143
+ __Block_byref_object_copy_.5304
+ __Block_byref_object_copy_.5833
+ __Block_byref_object_copy_.6252
+ __Block_byref_object_copy_.9906
+ __Block_byref_object_dispose_.10025
+ __Block_byref_object_dispose_.1014
+ __Block_byref_object_dispose_.1361
+ __Block_byref_object_dispose_.1959
+ __Block_byref_object_dispose_.2230
+ __Block_byref_object_dispose_.24
+ __Block_byref_object_dispose_.3144
+ __Block_byref_object_dispose_.5305
+ __Block_byref_object_dispose_.5834
+ __Block_byref_object_dispose_.6253
+ __Block_byref_object_dispose_.9907
+ __OBJC_$_CLASS_METHODS_SGGeoListSnippet
+ __OBJC_$_CLASS_METHODS_SGStructuredAddress
+ __OBJC_$_INSTANCE_METHODS_SGAspireResult
+ __OBJC_$_INSTANCE_METHODS_SGGeoListSnippet
+ __OBJC_$_INSTANCE_METHODS_SGGeoPoi
+ __OBJC_$_INSTANCE_METHODS_SGPIRResult
+ __OBJC_$_INSTANCE_METHODS_SGPoint
+ __OBJC_$_INSTANCE_METHODS_SGStructuredAddress
+ __OBJC_$_INSTANCE_VARIABLES_SGAspireResult
+ __OBJC_$_INSTANCE_VARIABLES_SGGeoListSnippet
+ __OBJC_$_INSTANCE_VARIABLES_SGGeoPoi
+ __OBJC_$_INSTANCE_VARIABLES_SGPIRResult
+ __OBJC_$_INSTANCE_VARIABLES_SGPoint
+ __OBJC_$_INSTANCE_VARIABLES_SGStructuredAddress
+ __OBJC_$_PROP_LIST_SGAspireResult
+ __OBJC_$_PROP_LIST_SGGeoListSnippet
+ __OBJC_$_PROP_LIST_SGGeoPoi
+ __OBJC_$_PROP_LIST_SGPIRResult
+ __OBJC_$_PROP_LIST_SGPoint
+ __OBJC_$_PROP_LIST_SGStructuredAddress
+ __OBJC_CLASS_PROTOCOLS_$_SGAspireResult
+ __OBJC_CLASS_PROTOCOLS_$_SGGeoListSnippet
+ __OBJC_CLASS_PROTOCOLS_$_SGGeoPoi
+ __OBJC_CLASS_PROTOCOLS_$_SGPoint
+ __OBJC_CLASS_PROTOCOLS_$_SGStructuredAddress
+ __OBJC_CLASS_RO_$_SGAspireResult
+ __OBJC_CLASS_RO_$_SGGeoListSnippet
+ __OBJC_CLASS_RO_$_SGGeoPoi
+ __OBJC_CLASS_RO_$_SGPIRResult
+ __OBJC_CLASS_RO_$_SGPoint
+ __OBJC_CLASS_RO_$_SGStructuredAddress
+ __OBJC_METACLASS_RO_$_SGAspireResult
+ __OBJC_METACLASS_RO_$_SGGeoListSnippet
+ __OBJC_METACLASS_RO_$_SGGeoPoi
+ __OBJC_METACLASS_RO_$_SGPIRResult
+ __OBJC_METACLASS_RO_$_SGPoint
+ __OBJC_METACLASS_RO_$_SGStructuredAddress
+ __SGThrottle_block_invoke.6
+ ___54+[SGEventGeocode geocodeAddressUsingPIR:withCallback:]_block_invoke
+ ___54+[SGEventGeocode geocodeAddressUsingPIR:withCallback:]_block_invoke_2
+ ___72+[SGEventGeocode geocodeLocation:usingMode:withGeoFilters:withCallback:]_block_invoke_2
+ ___DocumentUnderstandingClientLibraryCore_block_invoke
+ ___block_descriptor_40_e8_32r_e5_v8?0l
+ ___block_descriptor_48_e8_32bs_e28_v24?0"NSData"8"NSError"16l
+ ___block_descriptor_72_e8_32s40bs48r56r_e16_v16?0"NSData"8l
+ ___block_descriptor_96_e8_32s40bs48r56r64r_e16_v16?0"NSData"8l
+ ___getDUFoundInEventClass_block_invoke
+ __block_literal_global.10035
+ __block_literal_global.102
+ __block_literal_global.102.9081
+ __block_literal_global.10286
+ __block_literal_global.12
+ __block_literal_global.121
+ __block_literal_global.1408
+ __block_literal_global.15
+ __block_literal_global.18
+ __block_literal_global.1962
+ __block_literal_global.21
+ __block_literal_global.2184
+ __block_literal_global.22
+ __block_literal_global.228
+ __block_literal_global.249
+ __block_literal_global.25
+ __block_literal_global.25.7800
+ __block_literal_global.270
+ __block_literal_global.289
+ __block_literal_global.29
+ __block_literal_global.30
+ __block_literal_global.33
+ __block_literal_global.340
+ __block_literal_global.372
+ __block_literal_global.427
+ __block_literal_global.4951
+ __block_literal_global.52
+ __block_literal_global.5310
+ __block_literal_global.56
+ __block_literal_global.5601
+ __block_literal_global.5820
+ __block_literal_global.648
+ __block_literal_global.652
+ __block_literal_global.6624
+ __block_literal_global.7139
+ __block_literal_global.751
+ __block_literal_global.78
+ __block_literal_global.7820
+ __block_literal_global.8769
+ __block_literal_global.9080
+ __block_literal_global.9948
+ __sl_dlopen
+ _audit_stringDocumentUnderstandingClient
+ _entitlements_block_invoke._pasExprOnceResult.650
+ _entitlements_block_invoke._pasOnceToken69
+ _eventExtractedFromLLM
+ _forwardStackInvocation:._pasExprOnceResult.22
+ _forwardStackInvocation:._pasExprOnceResult.26
+ _forwardStackInvocation:._pasExprOnceResult.31
+ _getDUFoundInEventClass
+ _kSGPreExtractionMaxDocumentAgeDays
+ _objc_alloc_init
+ _objc_getClass
+ _objc_msgSend$addDependentLocality:
+ _objc_msgSend$addPois:
+ _objc_msgSend$addressStringFromPIRStructuredAddress:
+ _objc_msgSend$administrativeArea
+ _objc_msgSend$appendToAddress:addressComponentToAppend:withSeparator:
+ _objc_msgSend$clearDependentLocalitys
+ _objc_msgSend$clearPois
+ _objc_msgSend$country
+ _objc_msgSend$dependentLocalityAtIndex:
+ _objc_msgSend$dependentLocalitysCount
+ _objc_msgSend$geoList
+ _objc_msgSend$geocodeAddress:withTimeout:completionHandler:
+ _objc_msgSend$geocodeAddressUsingPIR:withCallback:
+ _objc_msgSend$hasAddress
+ _objc_msgSend$hasGeoList
+ _objc_msgSend$hasPrefGeocode
+ _objc_msgSend$hasTitle
+ _objc_msgSend$initWithData:
+ _objc_msgSend$initWithLabel:address:latitude:longitude:timezone:
+ _objc_msgSend$isEventSourceMetadata
+ _objc_msgSend$isPIRGeocodingAvailable
+ _objc_msgSend$lat
+ _objc_msgSend$lng
+ _objc_msgSend$locality
+ _objc_msgSend$mergeFrom:
+ _objc_msgSend$pirResultFromData:withDistance:fromCoordinates:
+ _objc_msgSend$pirResultWithHighestScoreFromData:
+ _objc_msgSend$pois
+ _objc_msgSend$poisAtIndex:
+ _objc_msgSend$poisCount
+ _objc_msgSend$postCode
+ _objc_msgSend$preExtractionMaxDocumentAgeDays
+ _objc_msgSend$prefGeocode
+ _objc_msgSend$setAdministrativeArea:
+ _objc_msgSend$setAdministrativeAreaCode:
+ _objc_msgSend$setCountry:
+ _objc_msgSend$setCountryCode:
+ _objc_msgSend$setGeoList:
+ _objc_msgSend$setLocality:
+ _objc_msgSend$setPostCode:
+ _objc_msgSend$setPrefGeocode:
+ _objc_msgSend$setSubAdministrativeArea:
+ _objc_msgSend$setSubThroughfare:
+ _objc_msgSend$setThoroughfare:
+ _objc_msgSend$setUrl:
+ _objc_msgSend$stringByAppendingFormat:
+ _objc_msgSend$subThroughfare
+ _objc_msgSend$thoroughfare
+ getDUFoundInEventClass.softClass
+ instance._instance.225
+ instance._instance.246
+ instance._instance.267
+ instance._instance.99
+ instance.onceToken.100
+ instance.onceToken.226
+ instance.onceToken.247
+ instance.onceToken.268
- GCC_except_table1026
- GCC_except_table1030
- GCC_except_table1034
- GCC_except_table1268
- GCC_except_table1417
- GCC_except_table1503
- GCC_except_table1506
- GCC_except_table1508
- GCC_except_table1836
- GCC_except_table2257
- GCC_except_table2285
- GCC_except_table2322
- GCC_except_table2377
- GCC_except_table2747
- GCC_except_table3130
- GCC_except_table3149
- GCC_except_table3156
- GCC_except_table3170
- GCC_except_table385
- GCC_except_table490
- GCC_except_table509
- GCC_except_table518
- GCC_except_table523
- GCC_except_table524
- GCC_except_table526
- GCC_except_table537
- GCC_except_table611
- GCC_except_table621
- GCC_except_table623
- GCC_except_table821
- GCC_except_table824
- GCC_except_table826
- GCC_except_table831
- GCC_except_table833
- GCC_except_table838
- __110-[SGSuggestionsService namesForDetail:limitTo:prependMaybe:onlySignificant:supportsInfoLookup:withCompletion:]_block_invoke.638
- __110-[SGSuggestionsService namesForDetail:limitTo:prependMaybe:onlySignificant:supportsInfoLookup:withCompletion:]_block_invoke.639
- __110-[SGSuggestionsService namesForDetail:limitTo:prependMaybe:onlySignificant:supportsInfoLookup:withCompletion:]_block_invoke.659
- __110-[SGSuggestionsService namesForDetail:limitTo:prependMaybe:onlySignificant:supportsInfoLookup:withCompletion:]_block_invoke.660
- __16-[SGFuture wait]_block_invoke.19
- __29-[SGFuture _wait:forSyncAPI:]_block_invoke.21
- __29-[SGFuture _wait:forSyncAPI:]_block_invoke.22
- __31+[SGEventGeocode geocodeEvent:]_block_invoke.63
- __31+[SGEventGeocode geocodeEvent:]_block_invoke.65
- __36-[SGSuggestionsService sendRTCLogs:]_block_invoke.766
- __38-[SGDaemonConnection _connectToServer]_block_invoke.6
- __39+[SGSuggestionsService prepareForQuery]_block_invoke.455
- __41+[SGDSuggestManagerInterface _initialize]_block_invoke.301
- __41+[SGDSuggestManagerInterface _initialize]_block_invoke_2.328
- __43-[SGSuggestionsService cacheSnapshotFuture]_block_invoke.611
- __43-[SGSuggestionsService cacheSnapshotFuture]_block_invoke.612
- __43-[SGSuggestionsService cacheSnapshotFuture]_block_invoke.615
- __45+[SGFuture futureForObject:withKey:onCreate:]_block_invoke.50
- __47-[SGRemoteObjectProxy _forwardStackInvocation:]_block_invoke.17
- __47-[SGRemoteObjectProxy _forwardStackInvocation:]_block_invoke.30
- __47-[SGRemoteObjectProxy _forwardStackInvocation:]_block_invoke.33
- __47-[SGRemoteObjectProxy _forwardStackInvocation:]_block_invoke.42
- __47-[SGRemoteObjectProxy _forwardStackInvocation:]_block_invoke_2.21
- __56-[SGDaemonConnection waitUntilReturn:withTimeout:error:]_block_invoke.12
- __56-[SGDaemonConnection waitUntilReturn:withTimeout:error:]_block_invoke.13
- __65-[SGKeyValueCacheFile setValueIfNotPresentWithDict:fromRecordId:]_block_invoke.37
- __70-[NSString(SGNSString) sg_dataEnumeratorUsingEncoding:nullTerminated:]_block_invoke.29
- __72+[SGEventGeocode geocodeLocation:usingMode:withGeoFilters:withCallback:]_block_invoke.45
- __72+[SGEventGeocode geocodeLocation:usingMode:withGeoFilters:withCallback:]_block_invoke.50
- __72+[SGEventGeocode geocodeLocation:usingMode:withGeoFilters:withCallback:]_block_invoke.56
- __72+[SGEventGeocode geocodeLocation:usingMode:withGeoFilters:withCallback:]_block_invoke.57
- __81-[SGMessagesSuggestionsService suggestionsFromMessage:options:completionHandler:]_block_invoke.100
- __Block_byref_object_copy_.1028
- __Block_byref_object_copy_.1354
- __Block_byref_object_copy_.17
- __Block_byref_object_copy_.1938
- __Block_byref_object_copy_.2202
- __Block_byref_object_copy_.3150
- __Block_byref_object_copy_.5310
- __Block_byref_object_copy_.5839
- __Block_byref_object_copy_.6246
- __Block_byref_object_copy_.9506
- __Block_byref_object_copy_.9623
- __Block_byref_object_dispose_.1029
- __Block_byref_object_dispose_.1355
- __Block_byref_object_dispose_.18
- __Block_byref_object_dispose_.1939
- __Block_byref_object_dispose_.2203
- __Block_byref_object_dispose_.3151
- __Block_byref_object_dispose_.5311
- __Block_byref_object_dispose_.5840
- __Block_byref_object_dispose_.6247
- __Block_byref_object_dispose_.9507
- __Block_byref_object_dispose_.9624
- __SGThrottle_block_invoke.2
- __block_literal_global.11
- __block_literal_global.115
- __block_literal_global.1388
- __block_literal_global.14
- __block_literal_global.14.8768
- __block_literal_global.17
- __block_literal_global.17.8771
- __block_literal_global.19
- __block_literal_global.1942
- __block_literal_global.20
- __block_literal_global.2157
- __block_literal_global.222
- __block_literal_global.23
- __block_literal_global.23.8777
- __block_literal_global.243
- __block_literal_global.264
- __block_literal_global.283
- __block_literal_global.334
- __block_literal_global.368
- __block_literal_global.421
- __block_literal_global.44
- __block_literal_global.46
- __block_literal_global.4953
- __block_literal_global.5316
- __block_literal_global.5604
- __block_literal_global.5826
- __block_literal_global.641
- __block_literal_global.645
- __block_literal_global.6615
- __block_literal_global.7133
- __block_literal_global.72
- __block_literal_global.744
- __block_literal_global.7806
- __block_literal_global.8
- __block_literal_global.8758
- __block_literal_global.9073
- __block_literal_global.9548
- __block_literal_global.96
- __block_literal_global.96.9074
- __block_literal_global.9635
- __block_literal_global.9882
- _entitlements_block_invoke._pasExprOnceResult.643
- _entitlements_block_invoke._pasOnceToken67
- _forwardStackInvocation:._pasExprOnceResult.16
- _forwardStackInvocation:._pasExprOnceResult.20
- _forwardStackInvocation:._pasExprOnceResult.25
- _strcmp
- instance._instance.219
- instance._instance.240
- instance._instance.261
- instance._instance.93
- instance.onceToken.220
- instance.onceToken.241
- instance.onceToken.262
- instance.onceToken.94
CStrings:
+ "%iu"
+ "%s"
+ ", %@"
+ "/System/Library/PrivateFrameworks/DocumentUnderstandingClient.framework/Contents/MacOS/DocumentUnderstandingClient"
+ "@\"SGGeoListSnippet\""
+ "@\"SGPoint\""
+ "@\"SGStructuredAddress\""
+ "@48@0:8@16d24{?=dd}32"
+ "CESV"
+ "Class getDUFoundInEventClass(void)_block_invoke"
+ "DUFoundInEvent"
+ "Max allowed document age is %ld days"
+ "SGAspireResult"
+ "SGGeoListSnippet"
+ "SGGeoPoi"
+ "SGPIRResult"
+ "SGPoint"
+ "SGStructuredAddress"
+ "SuggestionsPreExtractionMaxDocumentAgeDays"
+ "T@\"NSMutableArray\",&,N,V_dependentLocalitys"
+ "T@\"NSMutableArray\",&,N,V_pois"
+ "T@\"NSNumber\",R,N,V_latitude"
+ "T@\"NSNumber\",R,N,V_longitude"
+ "T@\"NSString\",&,N,V_administrativeArea"
+ "T@\"NSString\",&,N,V_administrativeAreaCode"
+ "T@\"NSString\",&,N,V_country"
+ "T@\"NSString\",&,N,V_countryCode"
+ "T@\"NSString\",&,N,V_locality"
+ "T@\"NSString\",&,N,V_postCode"
+ "T@\"NSString\",&,N,V_subAdministrativeArea"
+ "T@\"NSString\",&,N,V_subThroughfare"
+ "T@\"NSString\",&,N,V_thoroughfare"
+ "T@\"NSString\",&,N,V_title"
+ "T@\"NSString\",&,N,V_url"
+ "T@\"NSTimeZone\",R,N,V_timezone"
+ "T@\"SGGeoListSnippet\",&,N,V_geoList"
+ "T@\"SGPoint\",&,N,V_prefGeocode"
+ "T@\"SGStructuredAddress\",&,N,V_address"
+ "Td,N,V_lat"
+ "Td,N,V_lng"
+ "Unable to find class %s"
+ "_administrativeArea"
+ "_administrativeAreaCode"
+ "_countryCode"
+ "_dependentLocalitys"
+ "_geoList"
+ "_lat"
+ "_lng"
+ "_locality"
+ "_pois"
+ "_postCode"
+ "_prefGeocode"
+ "_subThroughfare"
+ "_thoroughfare"
+ "addDependentLocality:"
+ "addPois:"
+ "addressStringFromPIRStructuredAddress:"
+ "administrativeArea"
+ "administrativeAreaCode"
+ "administrative_area"
+ "administrative_area_code"
+ "appendToAddress:addressComponentToAppend:withSeparator:"
+ "cascadeEntitySetVersion:"
+ "clearDependentLocalitys"
+ "clearPois"
+ "countryCode"
+ "country_code"
+ "dependentLocalityAtIndex:"
+ "dependentLocalityType"
+ "dependentLocalitys"
+ "dependentLocalitysCount"
+ "dependent_locality"
+ "eventExtractedFromLLM"
+ "eventSourceMetadata"
+ "extracted location: %@"
+ "geoList"
+ "geo_list"
+ "geocodeAddress:withTimeout:completionHandler:"
+ "geocodeAddressUsingPIR:withCallback:"
+ "hasAddress"
+ "hasAdministrativeArea"
+ "hasAdministrativeAreaCode"
+ "hasCountry"
+ "hasCountryCode"
+ "hasGeoList"
+ "hasLat"
+ "hasLng"
+ "hasLocality"
+ "hasPostCode"
+ "hasPrefGeocode"
+ "hasSubAdministrativeArea"
+ "hasSubThroughfare"
+ "hasThoroughfare"
+ "hasTitle"
+ "hasUrl"
+ "initWithData:"
+ "initWithLabel:address:latitude:longitude:timezone:"
+ "isCascadeEntitySetVersion"
+ "isPIRGeocodingAvailable"
+ "lat"
+ "lng"
+ "locality"
+ "pirResultFromData:withDistance:fromCoordinates:"
+ "pirResultWithHighestScoreFromData:"
+ "pois"
+ "poisAtIndex:"
+ "poisCount"
+ "poisType"
+ "postCode"
+ "post_code"
+ "preExtractionMaxDocumentAgeDays"
+ "prefGeocode"
+ "pref_geocode"
+ "setAdministrativeArea:"
+ "setAdministrativeAreaCode:"
+ "setCountry:"
+ "setCountryCode:"
+ "setDependentLocalitys:"
+ "setGeoList:"
+ "setHasLat:"
+ "setHasLng:"
+ "setLat:"
+ "setLng:"
+ "setLocality:"
+ "setPois:"
+ "setPostCode:"
+ "setPrefGeocode:"
+ "setSubAdministrativeArea:"
+ "setSubThroughfare:"
+ "setThoroughfare:"
+ "setUrl:"
+ "softlink:o:path:/System/Library/PrivateFrameworks/DocumentUnderstandingClient.framework/DocumentUnderstandingClient"
+ "stringByAppendingFormat:"
+ "subThroughfare"
+ "sub_administrative_area"
+ "sub_throughfare"
+ "thoroughfare"
+ "v16@?0@\"NSData\"8"
+ "v24@?0@\"NSData\"8@\"NSError\"16"
+ "void *DocumentUnderstandingClientLibrary(void)"
+ "{?=\"lat\"b1\"lng\"b1}"

```
