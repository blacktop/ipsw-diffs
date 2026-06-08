## SpotlightFoundation

> `/System/Library/PrivateFrameworks/SpotlightFoundation.framework/SpotlightFoundation`

```diff

-2418.5.9.101.0
-  __TEXT.__text: 0x85b4
-  __TEXT.__auth_stubs: 0x310
+2444.104.0.0.0
+  __TEXT.__text: 0x8044
   __TEXT.__objc_methlist: 0x4d0
-  __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x312
+  __TEXT.__const: 0x78
+  __TEXT.__cstring: 0x319
   __TEXT.__oslogstring: 0x7f1
-  __TEXT.__gcc_except_tab: 0x1c4
-  __TEXT.__unwind_info: 0x220
-  __TEXT.__objc_classname: 0x79
-  __TEXT.__objc_methname: 0x113a
-  __TEXT.__objc_methtype: 0x20f
-  __TEXT.__objc_stubs: 0x11c0
-  __DATA_CONST.__got: 0x140
+  __TEXT.__gcc_except_tab: 0x1cc
+  __TEXT.__unwind_info: 0x218
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x160
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x510
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x198
+  __DATA_CONST.__got: 0x140
   __AUTH_CONST.__const: 0x180
   __AUTH_CONST.__cfstring: 0x720
   __AUTH_CONST.__objc_const: 0x670
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x10
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x2c
   __DATA.__data: 0x60
   __DATA_DIRTY.__objc_data: 0x1e0

   - /System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0C81FF9E-C30F-3809-A4CA-1756098D7640
-  Functions: 160
+  UUID: D09730C0-2B26-39E7-90C9-016B1994F2F7
+  Functions: 156
   Symbols:   644
-  CStrings:  395
+  CStrings:  162
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x6
+ _objc_retain_x8
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x26
CStrings:
- ".cxx_destruct"
- "@\"NSData\""
- "@\"NSData\"16@0:8"
- "@\"NSDate\""
- "@\"NSDate\"16@0:8"
- "@\"NSNumber\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"PARSession\""
- "@\"SFTopic\""
- "@16@0:8"
- "@24@0:8@16"
- "@32@0:8@16@24"
- "@32@0:8@16@?24"
- "@32@0:8@16Q24"
- "@36@0:8@16i24@28"
- "@40@0:8@16@24@32"
- "@40@0:8@16i24@28B36"
- "@44@0:8@16i24@28@36"
- "@48@0:8@16@24@32@40"
- "@56@0:8@16@24@32@40@48"
- "B32@0:8@16@24"
- "SFEngagedResult"
- "SPCacheManager"
- "SPCachedResult"
- "SPLocalTopic"
- "SPProactiveTopic"
- "SPRecentTopic"
- "SPSpotlightRecentsCache"
- "T@\"NSData\",?,C,N"
- "T@\"NSData\",C,N,V_encodedNormalizedTopic"
- "T@\"NSDate\",R,C,N"
- "T@\"NSDate\",R,C,N,V_engagementTime"
- "T@\"NSDate\",R,N"
- "T@\"NSNumber\",R,N"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,C,N,V_searchString"
- "T@\"NSString\",R,C,N,V_title"
- "T@\"SFTopic\",R,N"
- "T@\"SPCacheManager\",R"
- "Td,R,N"
- "Td,R,N,V_freshnessScore"
- "Td,R,N,V_score"
- "Ti,R,N"
- "Ti,R,N,V_type"
- "UTF8String"
- "UUID"
- "_createRecentsFromEngagedResults:maxCount:"
- "_encodedNormalizedTopic"
- "_engagementDate"
- "_engagementTime"
- "_freshnessScore"
- "_score"
- "_searchString"
- "_session"
- "_title"
- "_topic"
- "_type"
- "addEngagedResults:completion:"
- "addObject:"
- "addObjectsFromArray:"
- "allEngagedResultsForInput:maxAmount:completion:"
- "allObjects"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "arrayWithObjects:count:"
- "boolValue"
- "cacheContact:contactIdentifier:score:searchString:"
- "cacheLocalResult:identifier:bundleIdentifier:protectionClass:searchString:"
- "cachePerson:personQueryIdentifier:score:searchString:"
- "cacheResult:title:searchString:"
- "cacheSuggestion:type:score:searchString:"
- "clearEngagedResult:completion:"
- "clearEngagementsFromDate:toDate:"
- "clearEngagementsWithTitle:type:"
- "compare:"
- "completion"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "containsObject:"
- "containsString:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "d"
- "d16@0:8"
- "dateWithTimeIntervalSince1970:"
- "defaultManager"
- "defaultProperties"
- "defaultValueWithKey:"
- "defaults"
- "deleteAllRecentResults"
- "deleteAllResults"
- "deleteContact:contactIdentifier:score:"
- "deleteLocalResult:identifier:bundleIdentifier:protectionClass:"
- "deletePerson:personQueryIdentifier:score:"
- "deleteResult:title:"
- "deleteSuggestion:type:score:"
- "description"
- "dictionaryRepresentation"
- "dictionaryWithObjects:forKeys:count:"
- "doubleValue"
- "enabledStatus"
- "encodedNormalizedTopic"
- "engagementDate"
- "engagementTime"
- "enumerateLinguisticTagsInRange:scheme:options:orthography:usingBlock:"
- "enumerateRecentCompletionsWithSearchString:usingBlock:"
- "enumerateRecentResultsUsingBlock:"
- "filteredTopics:"
- "firstObject"
- "freshnessScore"
- "i16@0:8"
- "identifier"
- "init"
- "initWithContactName:contactIdentifier:detailText:"
- "initWithContactName:contactIdentifier:score:searchString:"
- "initWithContactName:emails:phones:detailText:"
- "initWithDictionaryResult:"
- "initWithEngagedResult:"
- "initWithId:userAgent:factory:"
- "initWithIdentifier:"
- "initWithPersonName:personQueryIdentifier:score:searchString:"
- "initWithResult:identifier:"
- "initWithResult:identifier:bundleIdentifier:protectionClass:searchString:"
- "initWithResult:topic:title:searchString:"
- "initWithSuiteName:"
- "initWithTitle:type:score:isCached:"
- "initWithTitle:type:score:searchString:"
- "initWithTopic:score:engagementDate:"
- "initWithTopicIdentifier:"
- "initWithType:query:identifier:"
- "intValue"
- "integerValue"
- "isEqual:"
- "isEqualToString:"
- "keysSortedByValueUsingSelector:"
- "lastObject"
- "length"
- "localTopicWithContactName:contactIdentifier:"
- "localTopicWithContactName:contactIdentifier:detailText:"
- "localTopicWithContactName:emails:phones:detailText:"
- "localTopicWithDictionaryResult:"
- "localTopicWithTitle:"
- "localTopicWithTitle:type:score:"
- "localTopicWithTitle:type:score:isCached:"
- "localTopicWithTopicIdentifier:"
- "lowercaseString"
- "mutableCopy"
- "normalizedTopic"
- "now"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithUnsignedInteger:"
- "objectAtIndex:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "proactiveTopicWithIdentifier:bundleIdentifier:protectionClass:detailText:"
- "proactiveTopicWithResult:"
- "q16@0:8"
- "rankingScore"
- "recentResults"
- "recentResultsWithOptions:"
- "recentResultsWithOptions:rankAndDeduplicate:"
- "recentTopic"
- "removeAllObjects"
- "removeDefaults"
- "removeKey:"
- "removeObjectForKey:"
- "removePersistentDomainForName:"
- "requestedTopic"
- "resetStandardUserDefaults"
- "result"
- "resultBundleId"
- "resultFromTopic:"
- "reverseObjectEnumerator"
- "score"
- "searchResult"
- "searchString"
- "sessionWithConfiguration:"
- "setBundleIdentifier:"
- "setCardSections:"
- "setCommand:"
- "setCompletion:"
- "setContactIdentifier:"
- "setDefaultWithKey:value:"
- "setDescriptions:"
- "setEncodedNormalizedTopic:"
- "setIdentifier:"
- "setInlineCard:"
- "setIsTemplate:"
- "setMaxLines:"
- "setObject:forKey:"
- "setQuerySource:"
- "setRankingScore:"
- "setResultBundleId:"
- "setSearchString:"
- "setSecondaryTitle:"
- "setSectionBundleIdentifier:"
- "setShouldUseCompactDisplay:"
- "setSymbolName:"
- "setThumbnail:"
- "setTitle:"
- "setType:"
- "setVersionWithValue:"
- "sortUsingComparator:"
- "sortedArrayUsingSelector:"
- "standardUserDefaults"
- "stringWithFormat:"
- "substringToIndex:"
- "substringWithRange:"
- "textWithString:"
- "title"
- "topEngagedResultsForInput:maxAmount:completion:"
- "topic"
- "topic:isSameAsTopic:"
- "type"
- "unarchivedObjectOfClass:fromData:error:"
- "updateApplicationContexts:"
- "updateRecentsWithBundleIdentifiers:"
- "v16@0:8"
- "v24@0:8@\"NSData\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8q16"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v36@0:8@16i24@28"
- "v40@0:8@16@24@32"
- "v44@0:8@16i24@28@36"
- "v48@0:8@16@24@32@40"
- "v56@0:8@16@24@32@40@48"
- "version"

```
