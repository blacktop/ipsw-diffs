## CoreSuggestions

> `/System/Library/PrivateFrameworks/CoreSuggestions.framework/CoreSuggestions`

```diff

-1294.2.0.0.0
-  __TEXT.__text: 0x8af1c
-  __TEXT.__auth_stubs: 0xe20
-  __TEXT.__objc_methlist: 0x9e4c
+1297.0.1.0.0
+  __TEXT.__text: 0x8b740
+  __TEXT.__auth_stubs: 0xe10
+  __TEXT.__objc_methlist: 0x9f5c
   __TEXT.__const: 0x858
   __TEXT.__dlopen_cstrs: 0x74
-  __TEXT.__gcc_except_tab: 0x858
-  __TEXT.__cstring: 0x7c72
-  __TEXT.__oslogstring: 0x2444
+  __TEXT.__gcc_except_tab: 0x844
+  __TEXT.__cstring: 0x7c71
+  __TEXT.__oslogstring: 0x247a
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x2250
+  __TEXT.__unwind_info: 0x2230
   __TEXT.__objc_classname: 0x1440
-  __TEXT.__objc_methname: 0x11bdb
-  __TEXT.__objc_methtype: 0x5355
-  __TEXT.__objc_stubs: 0x99e0
+  __TEXT.__objc_methname: 0x11e78
+  __TEXT.__objc_methtype: 0x5489
+  __TEXT.__objc_stubs: 0x9a20
   __DATA_CONST.__got: 0x748
-  __DATA_CONST.__const: 0x2868
+  __DATA_CONST.__const: 0x2818
   __DATA_CONST.__objc_classlist: 0x4e0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x40d0
+  __DATA_CONST.__objc_selrefs: 0x4128
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x470
   __DATA_CONST.__objc_arraydata: 0x2b0
-  __AUTH_CONST.__auth_got: 0x720
+  __AUTH_CONST.__auth_got: 0x718
   __AUTH_CONST.__const: 0x5a0
-  __AUTH_CONST.__cfstring: 0xa720
-  __AUTH_CONST.__objc_const: 0xe980
+  __AUTH_CONST.__cfstring: 0xa740
+  __AUTH_CONST.__objc_const: 0xeb00
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x8d0
+  __DATA.__objc_ivar: 0x8ec
   __DATA.__data: 0x1200
   __DATA.__bss: 0x1b8
   __DATA_DIRTY.__objc_data: 0x2e90

   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 71388FED-2EB1-3556-9998-B5B5C3BA2639
-  Functions: 3392
-  Symbols:   11018
-  CStrings:  6513
+  UUID: BEB4DBCC-10B8-3343-AF31-F8AAE968F3A8
+  Functions: 3403
+  Symbols:   11045
+  CStrings:  6533
 
Symbols:
+ -[SGExternalEventExtraction category]
+ -[SGExternalEventExtraction initWithIdentifier:fallbackIdentifier:status:category:title:content:creationDate:startTime:startTimeZone:endTime:endTimeZone:isAllDay:locations:icsAttachmentData:url:]
+ -[SGLocation city]
+ -[SGLocation country]
+ -[SGLocation geocodeCity]
+ -[SGLocation geocodeCountry]
+ -[SGLocation geocodePostalCode]
+ -[SGLocation geocodeState]
+ -[SGLocation geocodeSubThoroughfare]
+ -[SGLocation geocodeThoroughfare]
+ -[SGLocation geocodedLocationWithLabel:address:latitude:longitude:accuracy:handle:country:state:city:thoroughfare:subThoroughfare:postalCode:]
+ -[SGLocation geocodedLocationWithLatitude:longitude:accuracy:handle:country:state:city:thoroughfare:subThoroughfare:postalCode:]
+ -[SGLocation initWithId:origin:type:label:address:airportCode:latitude:longitude:accuracy:quality:handle:country:state:city:thoroughfare:subThoroughfare:postalCode:]
+ -[SGLocation initWithLocation:latitude:longitude:accuracy:handle:country:state:city:thoroughfare:subThoroughfare:postalCode:]
+ -[SGLocation postalCode]
+ -[SGLocation setPostalCode:]
+ -[SGLocation setSubThoroughfare:]
+ -[SGLocation state]
+ -[SGLocation subThoroughfare]
+ -[SGLocation thoroughfare]
+ GCC_except_table1008
+ GCC_except_table1012
+ GCC_except_table1016
+ GCC_except_table1257
+ GCC_except_table1411
+ GCC_except_table1497
+ GCC_except_table1500
+ GCC_except_table1502
+ GCC_except_table1830
+ GCC_except_table2280
+ GCC_except_table2306
+ GCC_except_table2308
+ GCC_except_table2344
+ GCC_except_table2399
+ GCC_except_table2797
+ GCC_except_table3298
+ GCC_except_table3315
+ GCC_except_table3322
+ GCC_except_table3336
+ GCC_except_table616
+ GCC_except_table624
+ GCC_except_table817
+ GCC_except_table820
+ GCC_except_table821
+ GCC_except_table824
+ GCC_except_table831
+ GCC_except_table848
+ _OBJC_IVAR_$_SGExternalEventExtraction._category
+ _OBJC_IVAR_$_SGLocation._city
+ _OBJC_IVAR_$_SGLocation._country
+ _OBJC_IVAR_$_SGLocation._postalCode
+ _OBJC_IVAR_$_SGLocation._state
+ _OBJC_IVAR_$_SGLocation._subThoroughfare
+ _OBJC_IVAR_$_SGLocation._thoroughfare
+ _SGSetAppCanShowSiriSuggestions.8302
+ ___31+[SGEventGeocode geocodeEvent:]_block_invoke.109
+ ___72+[SGEventGeocode geocodeLocation:usingMode:withGeoFilters:withCallback:]_block_invoke.100
+ ___72+[SGEventGeocode geocodeLocation:usingMode:withGeoFilters:withCallback:]_block_invoke.104
+ ___72+[SGEventGeocode geocodeLocation:usingMode:withGeoFilters:withCallback:]_block_invoke.105
+ ___72+[SGEventGeocode geocodeLocation:usingMode:withGeoFilters:withCallback:]_block_invoke.98
+ ___Block_byref_object_copy_.10237
+ ___Block_byref_object_copy_.10347
+ ___Block_byref_object_copy_.1937
+ ___Block_byref_object_copy_.2207
+ ___Block_byref_object_copy_.3100
+ ___Block_byref_object_copy_.5411
+ ___Block_byref_object_copy_.5945
+ ___Block_byref_object_copy_.6352
+ ___Block_byref_object_dispose_.10238
+ ___Block_byref_object_dispose_.10348
+ ___Block_byref_object_dispose_.1938
+ ___Block_byref_object_dispose_.2208
+ ___Block_byref_object_dispose_.3101
+ ___Block_byref_object_dispose_.5412
+ ___Block_byref_object_dispose_.5946
+ ___Block_byref_object_dispose_.6353
+ ___block_descriptor_113_e8_32s40bs48r56r64r72r80r88r96r104r_e22_v16?0"<GEOMapItem>"8lr48l8r56l8r64l8r72l8r80l8r88l8r96l8r104l8s32l8s40l8
+ ___block_descriptor_121_e8_32s40bs48r56r64r72r80r88r96r104r_e22_v16?0"<GEOMapItem>"8lr48l8r56l8r64l8r72l8r80l8r88l8r96l8s32l8r104l8s40l8
+ ___block_descriptor_121_e8_32s40s48bs56r64r72r80r88r96r104r112r_e22_v16?0"<GEOMapItem>"8lr56l8s32l8r64l8r72l8r80l8r88l8r96l8r104l8r112l8s40l8s48l8
+ ___block_descriptor_128_e8_32s40s48bs56r64r72r80r88r96r104r112r_e22_v16?0"<GEOMapItem>"8lr56l8r64l8r72l8r80l8r88l8r96l8r104l8r112l8s32l8s40l8s48l8
+ ___block_descriptor_136_e8_32s40bs48r56r64r72r80r88r96r104r112r_e22_v16?0"<GEOMapItem>"8ls40l8r48l8r56l8r64l8r72l8r80l8r88l8r96l8r104l8r112l8s32l8
+ ___block_literal_global.102.9413
+ ___block_literal_global.10275
+ ___block_literal_global.10356
+ ___block_literal_global.10608
+ ___block_literal_global.1384
+ ___block_literal_global.1939
+ ___block_literal_global.2163
+ ___block_literal_global.24.9111
+ ___block_literal_global.27.2165
+ ___block_literal_global.5054
+ ___block_literal_global.5415
+ ___block_literal_global.5712
+ ___block_literal_global.5932
+ ___block_literal_global.6734
+ ___block_literal_global.7446
+ ___block_literal_global.8147
+ ___block_literal_global.9096
+ ___block_literal_global.9412
+ _objc_msgSend$city
+ _objc_msgSend$geocodedLocationWithLabel:address:latitude:longitude:accuracy:handle:country:state:city:thoroughfare:subThoroughfare:postalCode:
+ _objc_msgSend$geocodedLocationWithLatitude:longitude:accuracy:handle:country:state:city:thoroughfare:subThoroughfare:postalCode:
+ _objc_msgSend$initWithId:origin:type:label:address:airportCode:latitude:longitude:accuracy:quality:handle:country:state:city:thoroughfare:subThoroughfare:postalCode:
+ _objc_msgSend$initWithLocation:latitude:longitude:accuracy:handle:country:state:city:thoroughfare:subThoroughfare:postalCode:
+ _objc_msgSend$isExtractedEventCategory
+ _objc_msgSend$postalCode
+ _objc_msgSend$structuredAddress
+ _objc_msgSend$subThoroughfare
- -[SGExternalEventExtraction initWithIdentifier:fallbackIdentifier:status:title:content:creationDate:startTime:startTimeZone:endTime:endTimeZone:isAllDay:locations:icsAttachmentData:url:]
- -[SGLocation geocodedLocationWithLabel:address:latitude:longitude:accuracy:handle:]
- -[SGLocation geocodedLocationWithLatitude:longitude:accuracy:handle:]
- GCC_except_table1014
- GCC_except_table1018
- GCC_except_table1022
- GCC_except_table1263
- GCC_except_table1417
- GCC_except_table1503
- GCC_except_table1506
- GCC_except_table1508
- GCC_except_table1836
- GCC_except_table2270
- GCC_except_table2296
- GCC_except_table2298
- GCC_except_table2334
- GCC_except_table2389
- GCC_except_table2786
- GCC_except_table3287
- GCC_except_table3304
- GCC_except_table3311
- GCC_except_table3325
- GCC_except_table615
- GCC_except_table618
- GCC_except_table619
- GCC_except_table823
- GCC_except_table827
- GCC_except_table830
- GCC_except_table832
- GCC_except_table837
- GCC_except_table854
- _SGSetAppCanShowSiriSuggestions.8243
- ___31+[SGEventGeocode geocodeEvent:]_block_invoke.114
- ___72+[SGEventGeocode geocodeLocation:usingMode:withGeoFilters:withCallback:]_block_invoke.101
- ___72+[SGEventGeocode geocodeLocation:usingMode:withGeoFilters:withCallback:]_block_invoke.103
- ___72+[SGEventGeocode geocodeLocation:usingMode:withGeoFilters:withCallback:]_block_invoke.107
- ___72+[SGEventGeocode geocodeLocation:usingMode:withGeoFilters:withCallback:]_block_invoke.109
- ___72+[SGEventGeocode geocodeLocation:usingMode:withGeoFilters:withCallback:]_block_invoke.99
- ___72+[SGEventGeocode geocodeLocation:usingMode:withGeoFilters:withCallback:]_block_invoke_2
- ___72+[SGEventGeocode geocodeLocation:usingMode:withGeoFilters:withCallback:]_block_invoke_2.100
- ___72+[SGEventGeocode geocodeLocation:usingMode:withGeoFilters:withCallback:]_block_invoke_2.108
- ___72+[SGEventGeocode geocodeLocation:usingMode:withGeoFilters:withCallback:]_block_invoke_2.110
- ___Block_byref_object_copy_.10177
- ___Block_byref_object_copy_.10287
- ___Block_byref_object_copy_.1954
- ___Block_byref_object_copy_.2225
- ___Block_byref_object_copy_.3106
- ___Block_byref_object_copy_.5375
- ___Block_byref_object_copy_.5900
- ___Block_byref_object_copy_.6301
- ___Block_byref_object_dispose_.10178
- ___Block_byref_object_dispose_.10288
- ___Block_byref_object_dispose_.1955
- ___Block_byref_object_dispose_.2226
- ___Block_byref_object_dispose_.3107
- ___Block_byref_object_dispose_.5376
- ___Block_byref_object_dispose_.5901
- ___Block_byref_object_dispose_.6302
- ___block_descriptor_65_e8_32s40bs48r56r_e22_v16?0"<GEOMapItem>"8lr48l8r56l8s32l8s40l8
- ___block_descriptor_72_e8_32s40bs48r56r_e16_v16?0"NSData"8lr48l8s32l8s40l8r56l8
- ___block_descriptor_73_e8_32s40bs48r56r_e22_v16?0"<GEOMapItem>"8lr48l8s32l8r56l8s40l8
- ___block_descriptor_73_e8_32s40s48bs56r64r_e22_v16?0"<GEOMapItem>"8lr56l8s32l8r64l8s40l8s48l8
- ___block_descriptor_80_e8_32s40s48bs56r64r_e22_v16?0"<GEOMapItem>"8lr56l8r64l8s32l8s40l8s48l8
- ___block_descriptor_88_e8_32s40bs48r56r64r_e22_v16?0"<GEOMapItem>"8ls40l8r48l8r56l8r64l8s32l8
- ___block_descriptor_96_e8_32s40bs48r56r64r_e16_v16?0"NSData"8lr48l8r56l8r64l8s32l8s40l8
- ___block_literal_global.102.9354
- ___block_literal_global.10215
- ___block_literal_global.10296
- ___block_literal_global.10546
- ___block_literal_global.1400
- ___block_literal_global.1956
- ___block_literal_global.2181
- ___block_literal_global.24.9052
- ___block_literal_global.27.2183
- ___block_literal_global.5018
- ___block_literal_global.5379
- ___block_literal_global.5667
- ___block_literal_global.5887
- ___block_literal_global.6683
- ___block_literal_global.7387
- ___block_literal_global.8087
- ___block_literal_global.9037
- ___block_literal_global.9353
- _getDUFoundInEventClass
- _objc_msgSend$geocodeAddressUsingPIR:withCallback:
- _objc_msgSend$geocodedLocationWithLabel:address:latitude:longitude:accuracy:handle:
- _objc_msgSend$geocodedLocationWithLatitude:longitude:accuracy:handle:
- _objc_msgSend$initWithLocation:latitude:longitude:accuracy:handle:
- _objc_msgSend$isPIRGeocodingAvailable
- _objc_msgSend$pirResultFromData:withDistance:fromCoordinates:
- _objc_msgSend$pirResultWithHighestScoreFromData:
- _objc_retain_x9
CStrings:
+ "@104@0:8@16d24d32d40@48@56@64@72@80@88@96"
+ "@112@0:8@\"NSString\"16@\"NSString\"24d32d40d48@\"NSData\"56@\"NSString\"64@\"NSString\"72@\"NSString\"80@\"NSString\"88@\"NSString\"96@\"NSString\"104"
+ "@112@0:8@16@24d32d40d48@56@64@72@80@88@96@104"
+ "@132@0:8@16@24q32q40@48@56@64@72@80@88@96B104@108@116@124"
+ "@152@0:8@16@24Q32@40@48@56d64d72d80d88@96@104@112@120@128@136@144"
+ "@96@0:8d16d24d32@\"NSData\"40@\"NSString\"48@\"NSString\"56@\"NSString\"64@\"NSString\"72@\"NSString\"80@\"NSString\"88"
+ "@96@0:8d16d24d32@40@48@56@64@72@80@88"
+ "SGExternalEventExtraction: invalid categoryValue: %ld"
+ "T@\"NSString\",&,N,V_postalCode"
+ "T@\"NSString\",&,N,V_subThoroughfare"
+ "T@\"NSString\",R,N,V_thoroughfare"
+ "Tq,R,N,V_category"
+ "_subThoroughfare"
+ "geocodeCity"
+ "geocodeCountry"
+ "geocodePostalCode"
+ "geocodeState"
+ "geocodeSubThoroughfare"
+ "geocodeThoroughfare"
+ "geocodedLocationWithLabel:address:latitude:longitude:accuracy:handle:country:state:city:thoroughfare:subThoroughfare:postalCode:"
+ "geocodedLocationWithLatitude:longitude:accuracy:handle:country:state:city:thoroughfare:subThoroughfare:postalCode:"
+ "initWithId:origin:type:label:address:airportCode:latitude:longitude:accuracy:quality:handle:country:state:city:thoroughfare:subThoroughfare:postalCode:"
+ "initWithIdentifier:fallbackIdentifier:status:category:title:content:creationDate:startTime:startTimeZone:endTime:endTimeZone:isAllDay:locations:icsAttachmentData:url:"
+ "initWithLocation:latitude:longitude:accuracy:handle:country:state:city:thoroughfare:subThoroughfare:postalCode:"
+ "setPostalCode:"
+ "setSubThoroughfare:"
+ "structuredAddress"
+ "subThoroughfare"
- "@124@0:8@16@24q32@40@48@56@64@72@80@88B96@100@108@116"
- "@48@0:8d16d24d32@\"NSData\"40"
- "@48@0:8d16d24d32@40"
- "@64@0:8@\"NSString\"16@\"NSString\"24d32d40d48@\"NSData\"56"
- "@64@0:8@16@24d32d40d48@56"
- "geocodedLocationWithLabel:address:latitude:longitude:accuracy:handle:"
- "geocodedLocationWithLatitude:longitude:accuracy:handle:"
- "initWithIdentifier:fallbackIdentifier:status:title:content:creationDate:startTime:startTimeZone:endTime:endTimeZone:isAllDay:locations:icsAttachmentData:url:"
- "isPIRGeocodingAvailable"
- "v16@?0@\"NSData\"8"

```
