## CoreSuggestions

> `/System/Library/PrivateFrameworks/CoreSuggestions.framework/CoreSuggestions`

```diff

-1276.17.0.3.0
-  __TEXT.__text: 0x87f70
+1294.2.0.0.0
+  __TEXT.__text: 0x8af1c
   __TEXT.__auth_stubs: 0xe20
-  __TEXT.__objc_methlist: 0x9c74
+  __TEXT.__objc_methlist: 0x9e4c
   __TEXT.__const: 0x858
   __TEXT.__dlopen_cstrs: 0x74
   __TEXT.__gcc_except_tab: 0x858
-  __TEXT.__cstring: 0x7c3c
-  __TEXT.__oslogstring: 0x23cb
+  __TEXT.__cstring: 0x7c72
+  __TEXT.__oslogstring: 0x2444
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x2248
-  __TEXT.__objc_classname: 0x13f1
-  __TEXT.__objc_methname: 0x118a4
-  __TEXT.__objc_methtype: 0x52a0
-  __TEXT.__objc_stubs: 0x98c0
-  __DATA_CONST.__got: 0x760
-  __DATA_CONST.__const: 0x2870
-  __DATA_CONST.__objc_classlist: 0x4d8
+  __TEXT.__unwind_info: 0x2250
+  __TEXT.__objc_classname: 0x1440
+  __TEXT.__objc_methname: 0x11bdb
+  __TEXT.__objc_methtype: 0x5355
+  __TEXT.__objc_stubs: 0x99e0
+  __DATA_CONST.__got: 0x748
+  __DATA_CONST.__const: 0x2868
+  __DATA_CONST.__objc_classlist: 0x4e0
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x170
+  __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4040
+  __DATA_CONST.__objc_selrefs: 0x40d0
   __DATA_CONST.__objc_protorefs: 0x70
-  __DATA_CONST.__objc_superrefs: 0x468
+  __DATA_CONST.__objc_superrefs: 0x470
   __DATA_CONST.__objc_arraydata: 0x2b0
   __AUTH_CONST.__auth_got: 0x720
   __AUTH_CONST.__const: 0x5a0
-  __AUTH_CONST.__cfstring: 0xa640
-  __AUTH_CONST.__objc_const: 0xe448
+  __AUTH_CONST.__cfstring: 0xa720
+  __AUTH_CONST.__objc_const: 0xe980
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x884
-  __DATA.__data: 0x1140
-  __DATA.__bss: 0x1e8
+  __AUTH.__objc_data: 0x230
+  __DATA.__objc_ivar: 0x8d0
+  __DATA.__data: 0x1200
+  __DATA.__bss: 0x1b8
   __DATA_DIRTY.__objc_data: 0x2e90
   __DATA_DIRTY.__data: 0x110
-  __DATA_DIRTY.__bss: 0x268
+  __DATA_DIRTY.__bss: 0x298
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/PhoneNumbers.framework/PhoneNumbers

   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 00CE8402-4425-355F-A184-F3ABD36C5334
-  Functions: 3357
-  Symbols:   10906
-  CStrings:  6458
+  UUID: 71388FED-2EB1-3556-9998-B5B5C3BA2639
+  Functions: 3392
+  Symbols:   11018
+  CStrings:  6513
 
Symbols:
+ +[SGExternalEventExtraction supportsSecureCoding]
+ +[SGOrigin originForMailSearchableItem:]
+ -[SGExternalEventExtraction .cxx_destruct]
+ -[SGExternalEventExtraction content]
+ -[SGExternalEventExtraction creationDate]
+ -[SGExternalEventExtraction encodeWithCoder:]
+ -[SGExternalEventExtraction endTimeZone]
+ -[SGExternalEventExtraction endTime]
+ -[SGExternalEventExtraction fallbackIdentifier]
+ -[SGExternalEventExtraction icsAttachmentData]
+ -[SGExternalEventExtraction identifier]
+ -[SGExternalEventExtraction initWithCoder:]
+ -[SGExternalEventExtraction initWithIdentifier:fallbackIdentifier:status:title:content:creationDate:startTime:startTimeZone:endTime:endTimeZone:isAllDay:locations:icsAttachmentData:url:]
+ -[SGExternalEventExtraction init]
+ -[SGExternalEventExtraction isAllDay]
+ -[SGExternalEventExtraction locations]
+ -[SGExternalEventExtraction startTimeZone]
+ -[SGExternalEventExtraction startTime]
+ -[SGExternalEventExtraction status]
+ -[SGExternalEventExtraction title]
+ -[SGExternalEventExtraction url]
+ -[SGLocation initWithMailAccountIdentifier:messageIdentifier:type:label:address:airportCode:latitude:longitude:]
+ -[SGRealtimeContact extractionSource]
+ -[SGRealtimeContact setExtractionSource:]
+ -[SGRealtimeEvent extractionSource]
+ -[SGRealtimeEvent setExtractionSource:]
+ -[SGRealtimeReminder extractionSource]
+ -[SGRealtimeReminder setExtractionSource:]
+ -[SGRealtimeWalletOrder extractionSource]
+ -[SGRealtimeWalletOrder setExtractionSource:]
+ -[SGRealtimeWalletPass extractionSource]
+ -[SGRealtimeWalletPass setExtractionSource:]
+ -[SGSuggestionsService filteredSuggestionsFromExtractions:origin:options:error:]
+ -[SGSuggestionsService filteredSuggestionsFromExtractions:origin:options:withCompletion:]
+ GCC_except_table1417
+ GCC_except_table1506
+ GCC_except_table1508
+ GCC_except_table1836
+ GCC_except_table2270
+ GCC_except_table2296
+ GCC_except_table2298
+ GCC_except_table2334
+ GCC_except_table2389
+ GCC_except_table2786
+ GCC_except_table3287
+ GCC_except_table3304
+ GCC_except_table3311
+ GCC_except_table3325
+ _OBJC_CLASS_$_SGExternalEventExtraction
+ _OBJC_IVAR_$_SGExternalEventExtraction._content
+ _OBJC_IVAR_$_SGExternalEventExtraction._creationDate
+ _OBJC_IVAR_$_SGExternalEventExtraction._endTime
+ _OBJC_IVAR_$_SGExternalEventExtraction._endTimeZone
+ _OBJC_IVAR_$_SGExternalEventExtraction._fallbackIdentifier
+ _OBJC_IVAR_$_SGExternalEventExtraction._icsAttachmentData
+ _OBJC_IVAR_$_SGExternalEventExtraction._identifier
+ _OBJC_IVAR_$_SGExternalEventExtraction._isAllDay
+ _OBJC_IVAR_$_SGExternalEventExtraction._locations
+ _OBJC_IVAR_$_SGExternalEventExtraction._startTime
+ _OBJC_IVAR_$_SGExternalEventExtraction._startTimeZone
+ _OBJC_IVAR_$_SGExternalEventExtraction._status
+ _OBJC_IVAR_$_SGExternalEventExtraction._title
+ _OBJC_IVAR_$_SGExternalEventExtraction._url
+ _OBJC_IVAR_$_SGRealtimeContact._extractionSource
+ _OBJC_IVAR_$_SGRealtimeEvent._extractionSource
+ _OBJC_IVAR_$_SGRealtimeReminder._extractionSource
+ _OBJC_IVAR_$_SGRealtimeWalletOrder._extractionSource
+ _OBJC_IVAR_$_SGRealtimeWalletPass._extractionSource
+ _OBJC_METACLASS_$_SGExternalEventExtraction
+ _SGSetAppCanShowSiriSuggestions.8243
+ __OBJC_$_CLASS_METHODS_SGExternalEventExtraction
+ __OBJC_$_CLASS_PROP_LIST_SGExternalEventExtraction
+ __OBJC_$_INSTANCE_METHODS_SGExternalEventExtraction
+ __OBJC_$_INSTANCE_VARIABLES_SGExternalEventExtraction
+ __OBJC_$_PROP_LIST_SGExternalEventExtraction
+ __OBJC_$_PROP_LIST_SGRealtimeSuggestion_Private
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SGRealtimeSuggestion_Private
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SGRealtimeSuggestion_Private
+ __OBJC_$_PROTOCOL_REFS_SGExternalExtraction
+ __OBJC_$_PROTOCOL_REFS_SGRealtimeSuggestion_Private
+ __OBJC_CLASS_PROTOCOLS_$_SGExternalEventExtraction
+ __OBJC_CLASS_RO_$_SGExternalEventExtraction
+ __OBJC_LABEL_PROTOCOL_$_SGExternalExtraction
+ __OBJC_LABEL_PROTOCOL_$_SGRealtimeSuggestion_Private
+ __OBJC_METACLASS_RO_$_SGExternalEventExtraction
+ __OBJC_PROTOCOL_$_SGExternalExtraction
+ __OBJC_PROTOCOL_$_SGRealtimeSuggestion_Private
+ ___110-[SGSuggestionsService namesForDetail:limitTo:prependMaybe:onlySignificant:supportsInfoLookup:withCompletion:]_block_invoke.595
+ ___110-[SGSuggestionsService namesForDetail:limitTo:prependMaybe:onlySignificant:supportsInfoLookup:withCompletion:]_block_invoke.596
+ ___110-[SGSuggestionsService namesForDetail:limitTo:prependMaybe:onlySignificant:supportsInfoLookup:withCompletion:]_block_invoke.614
+ ___39+[SGSuggestionsService prepareForQuery]_block_invoke.457
+ ___43-[SGSuggestionsService cacheSnapshotFuture]_block_invoke.581
+ ___43-[SGSuggestionsService cacheSnapshotFuture]_block_invoke.582
+ ___43-[SGSuggestionsService cacheSnapshotFuture]_block_invoke.587
+ ___80-[SGSuggestionsService filteredSuggestionsFromExtractions:origin:options:error:]_block_invoke
+ ___80-[SGSuggestionsService filteredSuggestionsFromExtractions:origin:options:error:]_block_invoke_2
+ ___89-[SGSuggestionsService filteredSuggestionsFromExtractions:origin:options:withCompletion:]_block_invoke
+ ___Block_byref_object_copy_.10177
+ ___Block_byref_object_copy_.10287
+ ___Block_byref_object_copy_.2225
+ ___Block_byref_object_copy_.3106
+ ___Block_byref_object_copy_.5375
+ ___Block_byref_object_copy_.5900
+ ___Block_byref_object_copy_.6301
+ ___Block_byref_object_dispose_.10178
+ ___Block_byref_object_dispose_.10288
+ ___Block_byref_object_dispose_.2226
+ ___Block_byref_object_dispose_.3107
+ ___Block_byref_object_dispose_.5376
+ ___Block_byref_object_dispose_.5901
+ ___Block_byref_object_dispose_.6302
+ ___block_literal_global.102.9354
+ ___block_literal_global.10215
+ ___block_literal_global.10296
+ ___block_literal_global.10546
+ ___block_literal_global.2181
+ ___block_literal_global.24.9052
+ ___block_literal_global.27.2183
+ ___block_literal_global.338
+ ___block_literal_global.378
+ ___block_literal_global.426
+ ___block_literal_global.5018
+ ___block_literal_global.5379
+ ___block_literal_global.5667
+ ___block_literal_global.5887
+ ___block_literal_global.598
+ ___block_literal_global.602
+ ___block_literal_global.6683
+ ___block_literal_global.683
+ ___block_literal_global.7387
+ ___block_literal_global.8087
+ ___block_literal_global.9037
+ ___block_literal_global.9353
+ __entitlements_block_invoke._pasExprOnceResult.600
+ _objc_msgSend$_setError
+ _objc_msgSend$accountIdentifier
+ _objc_msgSend$caseInsensitiveCompare:
+ _objc_msgSend$emailHeaders
+ _objc_msgSend$filteredSuggestionsFromExtractions:origin:options:withCompletion:
+ _objc_msgSend$hasError
+ _objc_msgSend$position
+ _objc_msgSend$setPosition:
+ _objc_msgSend$uniqueIdentifier
- +[SGPreferenceStorage EventMLRegexEnsembleExtractionEnabled]
- +[SGPreferenceStorage setEnableEventsMLRegexEnsembleExtraction:]
- GCC_except_table1412
- GCC_except_table1498
- GCC_except_table1501
- GCC_except_table1829
- GCC_except_table2259
- GCC_except_table2285
- GCC_except_table2287
- GCC_except_table2323
- GCC_except_table2378
- GCC_except_table2749
- GCC_except_table3252
- GCC_except_table3269
- GCC_except_table3276
- GCC_except_table3290
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _SGSetAppCanShowSiriSuggestions.8034
- ___110-[SGSuggestionsService namesForDetail:limitTo:prependMaybe:onlySignificant:supportsInfoLookup:withCompletion:]_block_invoke.593
- ___110-[SGSuggestionsService namesForDetail:limitTo:prependMaybe:onlySignificant:supportsInfoLookup:withCompletion:]_block_invoke.594
- ___110-[SGSuggestionsService namesForDetail:limitTo:prependMaybe:onlySignificant:supportsInfoLookup:withCompletion:]_block_invoke.612
- ___39+[SGSuggestionsService prepareForQuery]_block_invoke.455
- ___43-[SGSuggestionsService cacheSnapshotFuture]_block_invoke.579
- ___43-[SGSuggestionsService cacheSnapshotFuture]_block_invoke.580
- ___43-[SGSuggestionsService cacheSnapshotFuture]_block_invoke.585
- ___Block_byref_object_copy_.10081
- ___Block_byref_object_copy_.2231
- ___Block_byref_object_copy_.3160
- ___Block_byref_object_copy_.5396
- ___Block_byref_object_copy_.5915
- ___Block_byref_object_copy_.6319
- ___Block_byref_object_copy_.9971
- ___Block_byref_object_dispose_.10082
- ___Block_byref_object_dispose_.2232
- ___Block_byref_object_dispose_.3161
- ___Block_byref_object_dispose_.5397
- ___Block_byref_object_dispose_.5916
- ___Block_byref_object_dispose_.6320
- ___Block_byref_object_dispose_.9972
- ___block_literal_global.10009
- ___block_literal_global.10090
- ___block_literal_global.102.9148
- ___block_literal_global.10335
- ___block_literal_global.2183
- ___block_literal_global.24.8846
- ___block_literal_global.27.2185
- ___block_literal_global.336
- ___block_literal_global.374
- ___block_literal_global.424
- ___block_literal_global.5055
- ___block_literal_global.5399
- ___block_literal_global.5683
- ___block_literal_global.5902
- ___block_literal_global.596
- ___block_literal_global.600
- ___block_literal_global.6688
- ___block_literal_global.681
- ___block_literal_global.7199
- ___block_literal_global.7877
- ___block_literal_global.8831
- ___block_literal_global.9147
- __entitlements_block_invoke._pasExprOnceResult.598
- _kSGEventsMLRegexEnsembleExtractionEnabled
CStrings:
+ "@124@0:8@16@24q32@40@48@56@64@72@80@88B96@100@108@116"
+ "SGExternalEventExtraction"
+ "SGExternalEventExtraction: invalid statusValue: %ld"
+ "SGExternalExtraction"
+ "SGExternalExtraction.m"
+ "SGOrigin: Unable to construct origin from searchableItem: %{public}@"
+ "SGRealtimeSuggestion_Private"
+ "T@\"NSData\",R,N,V_icsAttachmentData"
+ "T@\"NSDate\",R,N,V_endTime"
+ "T@\"NSDate\",R,N,V_startTime"
+ "T@\"NSString\",R,N,V_content"
+ "T@\"NSString\",R,N,V_fallbackIdentifier"
+ "Ti,N"
+ "Ti,N,V_extractionSource"
+ "Tq,R,N,V_status"
+ "_content"
+ "_endTime"
+ "_extractionSource"
+ "_fallbackIdentifier"
+ "_icsAttachmentData"
+ "_setError"
+ "_startTime"
+ "_status"
+ "accountIdentifier"
+ "caseInsensitiveCompare:"
+ "content"
+ "emailHeaders"
+ "endTime"
+ "extractionSource"
+ "fallbackIdentifier"
+ "filteredSuggestionsFromExtractions:origin:options:error:"
+ "filteredSuggestionsFromExtractions:origin:options:withCompletion:"
+ "hasError"
+ "initWithIdentifier:fallbackIdentifier:status:title:content:creationDate:startTime:startTimeZone:endTime:endTimeZone:isAllDay:locations:icsAttachmentData:url:"
+ "initWithMailAccountIdentifier:messageIdentifier:type:label:address:airportCode:latitude:longitude:"
+ "message-id"
+ "originForMailSearchableItem:"
+ "position"
+ "setExtractionSource:"
+ "setPosition:"
+ "startTime"
+ "status"
+ "uniqueIdentifier"
+ "v48@0:8@\"NSArray\"16@\"SGOrigin\"24Q32@?<v@?@\"NSArray\"@\"NSError\">40"
+ "v48@0:8@\"NSArray\"16@\"SGOrigin\"24Q32@?<v@?@\"SGXPCResponse1\">40"
- "EventMLRegexEnsembleExtractionEnabled"
- "SuggestionsEventsMLRegexEnsembleExtractionEnabled"
- "setEnableEventsMLRegexEnsembleExtraction:"

```
