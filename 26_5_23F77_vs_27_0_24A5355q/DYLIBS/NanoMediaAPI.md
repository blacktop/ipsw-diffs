## NanoMediaAPI

> `/System/Library/PrivateFrameworks/NanoMediaAPI.framework/NanoMediaAPI`

```diff

-2023.600.2.0.0
-  __TEXT.__text: 0x8e50
-  __TEXT.__auth_stubs: 0x2f0
-  __TEXT.__objc_methlist: 0x764
+2024.100.38.0.0
+  __TEXT.__text: 0x7228
+  __TEXT.__objc_methlist: 0x62c
   __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x827
-  __TEXT.__oslogstring: 0xac6
-  __TEXT.__unwind_info: 0x1f0
-  __TEXT.__objc_classname: 0x27b
-  __TEXT.__objc_methname: 0x12ee
-  __TEXT.__objc_methtype: 0x32b
-  __TEXT.__objc_stubs: 0x11e0
-  __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0x2b0
-  __DATA_CONST.__objc_classlist: 0xb0
+  __TEXT.__cstring: 0x7af
+  __TEXT.__oslogstring: 0xa7b
+  __TEXT.__unwind_info: 0x1b8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x2a0
+  __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x608
-  __DATA_CONST.__objc_superrefs: 0x68
-  __DATA_CONST.__objc_arraydata: 0xb0
-  __AUTH_CONST.__auth_got: 0x180
+  __DATA_CONST.__objc_selrefs: 0x5c0
+  __DATA_CONST.__objc_superrefs: 0x50
+  __DATA_CONST.__objc_arraydata: 0xa8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0xfa0
-  __AUTH_CONST.__objc_const: 0x1340
+  __AUTH_CONST.__cfstring: 0xea0
+  __AUTH_CONST.__objc_const: 0xff8
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH.__objc_data: 0x550
-  __DATA.__objc_ivar: 0x5c
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x410
+  __DATA.__objc_ivar: 0x4c
   __DATA.__data: 0x120
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__bss: 0x80

   - /System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3F68BA1F-2919-3101-9A4F-95EBF74410D6
-  Functions: 179
-  Symbols:   870
-  CStrings:  625
+  UUID: 4A874A9C-5110-339F-98F7-480394BFD94A
+  Functions: 150
+  Symbols:   763
+  CStrings:  299
 
Symbols:
+ -[NMAPIRequestOperation _writeResponseDictionaryToDisk:].cold.5
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSUUID
+ ___79-[NMAPIDefaultSectionedCollectionDataSource _storeBrowseSectionWithDictionary:]_block_invoke_2
+ ___block_descriptor_32_e25_v16?0"MPIdentifierSet"8l
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$URLByDeletingLastPathComponent
+ _objc_msgSend$UUID
+ _objc_msgSend$UUIDString
+ _objc_msgSend$createDirectoryAtURL:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$defaultManager
+ _objc_msgSend$initWithBlock:
+ _objc_msgSend$setContentItemID:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x25
+ _objc_retain_x3
+ _objc_retain_x8
- -[NMAPIModelObjectRequest .cxx_destruct]
- -[NMAPIModelObjectRequest copyWithZone:]
- -[NMAPIModelObjectRequest initWithModelObject:]
- -[NMAPIModelObjectRequest modelObject]
- -[NMAPIModelObjectRequest responseParserClass]
- -[NMAPIModelObjectRequest setModelObject:]
- -[NMAPIModelObjectRequest urlComponentsWithStoreURLBag:error:]
- -[NMAPIModelObjectRequest urlComponentsWithStoreURLBag:error:].cold.1
- -[NMAPIModelObjectRequest urlComponentsWithStoreURLBag:error:].cold.2
- -[NMAPIModelObjectRequest urlComponentsWithStoreURLBag:error:].cold.3
- -[NMAPIModelObjectRequest urlComponentsWithStoreURLBag:error:].cold.4
- -[NMAPISearchGroupRequest copyWithZone:]
- -[NMAPISearchGroupRequest responseParserClass]
- -[NMAPISearchGroupRequest resultsPerSection]
- -[NMAPISearchGroupRequest setResultsPerSection:]
- -[NMAPISearchGroupRequest urlComponentsWithStoreURLBag:error:]
- -[NMAPISearchRequest .cxx_destruct]
- -[NMAPISearchRequest copyWithZone:]
- -[NMAPISearchRequest initWithSearchString:]
- -[NMAPISearchRequest responseParserClass]
- -[NMAPISearchRequest resultsPerSection]
- -[NMAPISearchRequest searchString]
- -[NMAPISearchRequest setResultsPerSection:]
- -[NMAPISearchRequest setSearchString:]
- -[NMAPISearchRequest urlComponentsWithStoreURLBag:error:]
- -[NMAPISearchRequest urlComponentsWithStoreURLBag:error:].cold.1
- -[NMAPISearchRequest urlComponentsWithStoreURLBag:error:].cold.2
- -[NMAPISearchResponseParser resultsWithDictionary:error:]
- _MediaAPIRadioStationsIncludeKeyString
- _MediaAPIRadioStationsIncludeQueryValue
- _OBJC_CLASS_$_MPModelAlbum
- _OBJC_CLASS_$_MPModelArtist
- _OBJC_CLASS_$_MPModelPlaylist
- _OBJC_CLASS_$_NMAPIModelObjectRequest
- _OBJC_CLASS_$_NMAPISearchGroupRequest
- _OBJC_CLASS_$_NMAPISearchRequest
- _OBJC_CLASS_$_NMAPISearchResponseParser
- _OBJC_CLASS_$_NSNumber
- _OBJC_IVAR_$_NMAPIModelObjectRequest._modelObject
- _OBJC_IVAR_$_NMAPISearchGroupRequest._resultsPerSection
- _OBJC_IVAR_$_NMAPISearchRequest._resultsPerSection
- _OBJC_IVAR_$_NMAPISearchRequest._searchString
- _OBJC_METACLASS_$_NMAPIModelObjectRequest
- _OBJC_METACLASS_$_NMAPISearchGroupRequest
- _OBJC_METACLASS_$_NMAPISearchRequest
- _OBJC_METACLASS_$_NMAPISearchResponseParser
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6
- __OBJC_$_INSTANCE_METHODS_NMAPIModelObjectRequest
- __OBJC_$_INSTANCE_METHODS_NMAPISearchGroupRequest
- __OBJC_$_INSTANCE_METHODS_NMAPISearchRequest
- __OBJC_$_INSTANCE_METHODS_NMAPISearchResponseParser
- __OBJC_$_INSTANCE_VARIABLES_NMAPIModelObjectRequest
- __OBJC_$_INSTANCE_VARIABLES_NMAPISearchGroupRequest
- __OBJC_$_INSTANCE_VARIABLES_NMAPISearchRequest
- __OBJC_$_PROP_LIST_NMAPIModelObjectRequest
- __OBJC_$_PROP_LIST_NMAPISearchGroupRequest
- __OBJC_$_PROP_LIST_NMAPISearchRequest
- __OBJC_CLASS_PROTOCOLS_$_NMAPISearchResponseParser
- __OBJC_CLASS_RO_$_NMAPIModelObjectRequest
- __OBJC_CLASS_RO_$_NMAPISearchGroupRequest
- __OBJC_CLASS_RO_$_NMAPISearchRequest
- __OBJC_CLASS_RO_$_NMAPISearchResponseParser
- __OBJC_METACLASS_RO_$_NMAPIModelObjectRequest
- __OBJC_METACLASS_RO_$_NMAPISearchGroupRequest
- __OBJC_METACLASS_RO_$_NMAPISearchRequest
- __OBJC_METACLASS_RO_$_NMAPISearchResponseParser
- ___62-[NMAPISearchGroupRequest urlComponentsWithStoreURLBag:error:]_block_invoke
- ___block_descriptor_32_e41_B24?0"NSURLQueryItem"8"NSDictionary"16l
- _objc_msgSend$adamID
- _objc_msgSend$emptyIdentifierSet
- _objc_msgSend$globalPlaylistID
- _objc_msgSend$identifiers
- _objc_msgSend$name
- _objc_msgSend$numberWithLongLong:
- _objc_msgSend$numberWithUnsignedInteger:
- _objc_msgSend$setModelObject:
- _objc_msgSend$setSearchString:
- _objc_msgSend$stringValue
- _objc_msgSend$universalStore
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x26
- _objc_retain_x28
CStrings:
+ "[NMAPIRequestOperation] Failed to create response cache directory for %@ due to error: %@"
+ "v16@?0@\"MPIdentifierSet\"8"
- "#16@0:8"
- ".cxx_destruct"
- "@\"ICURLBag\""
- "@\"MPIdentifierSet\"24@0:8@\"NSIndexPath\"16"
- "@\"MPIdentifierSet\"24@0:8q16"
- "@\"MPModelObject\""
- "@\"NMAPIRequest\""
- "@\"NSArray\""
- "@\"NSArray\"16@0:8"
- "@\"NSArray\"32@0:8@\"NSDictionary\"16^@24"
- "@\"NSCache\""
- "@\"NSDictionary\""
- "@\"NSIndexPath\"24@0:8@\"MPIdentifierSet\"16"
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@16@0:8"
- "@20@0:8B16"
- "@24@0:8:16"
- "@24@0:8@\"NSIndexPath\"16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8q16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16@?24"
- "@32@0:8@16^@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"<MPLazySectionedCollectionDataSource>\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@?0@\"NSURLQueryItem\"8@\"NSDictionary\"16"
- "Catalog Search (%@)"
- "JSONObjectWithData:options:error:"
- "MPLazySectionedCollectionDataSource"
- "Model Object: %@"
- "NMAPIAnyResponseParser"
- "NMAPIArtistResponseParser"
- "NMAPICollectionResponseParser"
- "NMAPIDefaultSectionedCollectionDataSource"
- "NMAPIFitnessMultiroomRequest"
- "NMAPIHeavyRotationRequest"
- "NMAPIItemListResponseParser"
- "NMAPIModelObjectRequest"
- "NMAPIMultiplexResponseParser"
- "NMAPIMultiroomResponseParser"
- "NMAPIRadioGenreRoomRequest"
- "NMAPIRadioRequest"
- "NMAPIRadioResponseParser"
- "NMAPIRequest"
- "NMAPIRequestOperation"
- "NMAPIResponseParser"
- "NMAPIRoomResponseParser"
- "NMAPISearchGroupRequest"
- "NMAPISearchRequest"
- "NMAPISearchResponseParser"
- "NMAPISectionResult"
- "NMAPIStarterPackMultiplexRequest"
- "NMAPIURLRequest"
- "NSObject"
- "NanoMusic"
- "Q"
- "Q16@0:8"
- "Q24@0:8Q16"
- "T#,R"
- "T@\"MPModelObject\",&,N,V_modelObject"
- "T@\"NMAPIRequest\",C,D,N"
- "T@\"NSArray\",R,N,V_itemsArray"
- "T@\"NSDictionary\",R,N,V_sectionDictionary"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_searchString"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V_sectionIdentifier"
- "T@\"NSURL\",&,N,V_cacheURL"
- "T@\"NSURL\",C,N,V_URL"
- "TB,N,GisUnderageUser,V_underageUser"
- "TQ,N,V_cachePolicy"
- "TQ,N,V_resultsPerSection"
- "TQ,R"
- "URL"
- "Vv16@0:8"
- "[NMAPIRequest] Missing identifier."
- "[NMAPIRequest] Missing modelObject parameter."
- "[NMAPIRequest] Missing resourceType."
- "[NMAPIRequest] Missing searchString parameter."
- "^{_NSZone=}16@0:8"
- "_URL"
- "_addItemsFromArray:"
- "_addSectionWithIdentifier:dictionary:"
- "_adjustedPayload:path:"
- "_bagRoomURLRegularExpressionWithStoreURLBag:"
- "_cachePolicy"
- "_cacheURL"
- "_cachedItems"
- "_cachedSections"
- "_finishWithResponse:error:"
- "_fitnessMultiroomIdentifierWithStoreURLBag:"
- "_importedIdentifierSets"
- "_isSupportedItem:"
- "_itemResults"
- "_itemsArray"
- "_modelObject"
- "_musicURLWithPartialURLString:"
- "_parseResults"
- "_personalizeResponse:completion:"
- "_readResponseDictionaryFromDisk"
- "_request"
- "_results"
- "_resultsPerSection"
- "_roomIdentifierWithStoreURLBag:"
- "_searchString"
- "_sectionDictionary"
- "_sectionIdentifier"
- "_sectionResultIDs"
- "_sectionResults"
- "_sectionedItemResultIDs"
- "_storeBrowseSectionWithDictionary:"
- "_storeURLBag"
- "_underageUser"
- "_updateImportedIdentifierSetsWithIdentifier:dictionary:"
- "_writeResponseDictionaryToDisk:"
- "absoluteString"
- "adamID"
- "addObject:"
- "addOperation:"
- "allSupportedItemProperties"
- "allSupportedProperties"
- "allSupportedSectionProperties"
- "annotatedPayload"
- "anyObject"
- "appendItem:"
- "appendSection:"
- "arrayByAddingObject:"
- "arrayByAddingObjectsFromArray:"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "autorelease"
- "cachePolicy"
- "cacheURL"
- "class"
- "clientPlatformIdentifier"
- "componentsJoinedByString:"
- "componentsWithString:"
- "componentsWithURL:resolvingAgainstBaseURL:"
- "configurationForLoadingModelDataWithStoreURLBag:error:"
- "conformsToProtocol:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentQueue"
- "dataWithContentsOfURL:options:error:"
- "dataWithJSONObject:options:error:"
- "debugDescription"
- "description"
- "dictionaryForBagKey:"
- "dictionaryWithObjects:forKeys:count:"
- "emptyIdentifierSet"
- "emptyPropertySet"
- "enumerateItemsInSectionAtIndex:usingBlock:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "enumerateSectionsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "events"
- "execute"
- "filteredArrayUsingPredicate:"
- "firstObject"
- "globalPlaylistID"
- "hasSameContentAsDataSource:"
- "hasSuffix:"
- "hash"
- "host"
- "identifiers"
- "identifiersForItemAtIndexPath:"
- "identifiersForSectionAtIndex:"
- "importObjectsFromRequest:options:error:"
- "include[stations]"
- "indexOfSectionForSectionIndexTitleAtIndex:"
- "indexPathForItemWithIdentifiersIntersectingSet:"
- "init"
- "initWithDataSource:"
- "initWithIdentifiers:block:"
- "initWithModel:personalizationStyle:"
- "initWithModelObject:"
- "initWithName:value:"
- "initWithPayload:"
- "initWithProperties:relationships:"
- "initWithRequest:"
- "initWithRequest:responseHandler:"
- "initWithRequest:results:storeURLBag:"
- "initWithSearchString:"
- "initWithSectionIdentifier:sectionDictionary:itemsArray:"
- "initWithURL:"
- "initWithURLRequests:"
- "initWithUnderageUser:"
- "initWithUnpersonalizedRequest:unpersonalizedContentDescriptors:"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isUnderageUser"
- "item"
- "itemAtIndexPath:"
- "itemProperties"
- "itemsArray"
- "length"
- "matchesInString:options:range:"
- "meta.results.order"
- "modelObject"
- "modelObjectMatchingIdentifierSet:propertySet:"
- "mutableCopy"
- "newOperationWithResponseHandler:"
- "numberOfItemsInSection:"
- "numberOfSections"
- "numberWithLongLong:"
- "numberWithUnsignedInteger:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "optionalSectionIndexTitlesRange"
- "pathWithComponents:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performWithResponseHandler:"
- "predicateWithBlock:"
- "produceResponseWithLoadedOutput:completion:"
- "propertySetByCombiningWithPropertySet:"
- "propertySetWithProperties:"
- "q24@0:8q16"
- "queryItemWithName:value:"
- "queryItems"
- "rangeWithName:"
- "regularExpressionWithPattern:options:error:"
- "release"
- "remainingTimeInterval"
- "removeObjectForKey:"
- "request"
- "requestWithURL:"
- "respondsToSelector:"
- "responseParserClass"
- "resultKey"
- "results"
- "resultsOrder"
- "resultsPerSection"
- "resultsWithDictionary:error:"
- "retain"
- "retainCount"
- "scheme"
- "searchString"
- "sectionAtIndex:"
- "sectionDictionary"
- "sectionIndexTitles"
- "sectionProperties"
- "self"
- "setAuthenticationOptions:"
- "setCachePolicy:"
- "setCacheURL:"
- "setClientIdentifier:"
- "setClientPlatformIdentifier:"
- "setClientVersion:"
- "setDefaultMusicRequestProperties"
- "setEditorialRequestProperties"
- "setHTTPMethod:"
- "setHost:"
- "setLabel:"
- "setLoadAdditionalContentURL:"
- "setModelObject:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setPath:"
- "setQueryItems:"
- "setRequest:"
- "setResults:"
- "setResultsPerSection:"
- "setScheme:"
- "setSearchString:"
- "setSectionType:"
- "setTimeoutInterval:"
- "setTitle:"
- "setURL:"
- "setUnderageUser:"
- "setUserIdentity:"
- "setValue:forKey:"
- "sharedServerObjectDatabase"
- "stringByAppendingFormat:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringForBagKey:"
- "stringValue"
- "stringWithFormat:"
- "substringWithRange:"
- "superclass"
- "underageUser"
- "universalStore"
- "urlComponentsWithStoreURLBag:error:"
- "userIdentity"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "valueForKeyPath:"
- "writeToURL:options:error:"
- "zone"
- "{_NSRange=QQ}16@0:8"

```
