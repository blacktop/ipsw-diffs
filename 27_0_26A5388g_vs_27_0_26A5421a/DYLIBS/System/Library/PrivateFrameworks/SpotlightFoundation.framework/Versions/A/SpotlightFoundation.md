## SpotlightFoundation

> `/System/Library/PrivateFrameworks/SpotlightFoundation.framework/Versions/A/SpotlightFoundation`

```diff

-2454.100.0.0.0
-  __TEXT.__text: 0x8c54
-  __TEXT.__objc_methlist: 0x4d0
-  __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x319
-  __TEXT.__oslogstring: 0x7f1
+2459.405.0.0.0
+  __TEXT.__text: 0x95d4
+  __TEXT.__objc_methlist: 0x4d8
+  __TEXT.__const: 0xa0
+  __TEXT.__cstring: 0x32b
+  __TEXT.__oslogstring: 0x99c
   __TEXT.__gcc_except_tab: 0x1cc
-  __TEXT.__unwind_info: 0x218
+  __TEXT.__unwind_info: 0x210
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x510
+  __DATA_CONST.__objc_selrefs: 0x528
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__got: 0x140
   __AUTH_CONST.__const: 0x2a0
-  __AUTH_CONST.__cfstring: 0x720
+  __AUTH_CONST.__cfstring: 0x760
   __AUTH_CONST.__objc_const: 0x670
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x10

   - /System/Library/PrivateFrameworks/SearchFoundation.framework/Versions/A/SearchFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 168
-  Symbols:   450
-  CStrings:  106
+  Functions: 172
+  Symbols:   454
+  CStrings:  120
 
Symbols:
+ -[SPLocalTopic normalizedTopic]
+ _objc_msgSend$copy
+ _objc_msgSend$initWithSearchResult:
+ _objc_msgSend$setResult:
CStrings:
+ "6"
+ "MobileMailIndex"
+ "cacheContact contactName=%{sensitive}@ contactIdentifier=%{sensitive}@"
+ "cacheLocalResult identifier=%{sensitive}@ bundleId=%{sensitive}@ protectionClass=%@ type=%d topicId=%{sensitive}@"
+ "cachePerson personName=%{sensitive}@ personQueryIdentifier=%{sensitive}@"
+ "cacheResult normalizedTopic=%{sensitive}@ identifier=%{sensitive}@ bundleId=%{sensitive}@ type=%d"
+ "cacheSuggestion title=%{sensitive}@ type=%d"
+ "caching contact with type"
+ "caching person with type"
+ "caching result with type: %d"
+ "caching suggestion with type: %d"
+ "could not add contact result to cache"
+ "could not add local result to cache"
+ "could not add person result to cache"
+ "could not add result to cache"
+ "could not add suggestion to cache"
+ "could not create cached contact result"
+ "could not create cached person result"
+ "could not create cached result with result: %d"
+ "could not create cached result with suggestion: %d"
+ "could not create search result with engaged result"
+ "could not delete cached contact result"
+ "could not delete cached person result"
+ "could not delete cached result"
+ "could not delete cached result with result: %d"
+ "could not delete cached result with suggestion: %d"
+ "could not encode cached topic: %d"
+ "could not encode generic topic"
+ "could not encode generic topic. error: %@"
+ "could not encode local cached topic: %d"
+ "could not encode local contact topic"
+ "could not encode local person topic"
+ "deleteAllResults"
+ "deleteContact contactName=%{sensitive}@ contactIdentifier=%{sensitive}@"
+ "deleteLocalResult identifier=%{sensitive}@ bundleId=%{sensitive}@ protectionClass=%@ type=%d topicId=%{sensitive}@"
+ "deletePerson personName=%{sensitive}@ personQueryIdentifier=%{sensitive}@"
+ "deleteResult normalizedTopic=%{sensitive}@ identifier=%{sensitive}@ bundleId=%{sensitive}@ type=%d"
+ "deleteResult requestedTopic=%{sensitive}@ identifier=%{sensitive}@ bundleId=%{sensitive}@ type=%d"
+ "deleteSuggestion title=%{sensitive}@ type=%d"
+ "enumerateCompletion title=%{sensitive}@ type=%d"
+ "enumerateRecent identifier=%{sensitive}@ type=%d title=%{sensitive}@"
+ "error when clearing engaged result with normalized topic: %@"
+ "error when clearing engaged result with requested topic: %@"
+ "filtered to %ld engaged results"
+ "found %ld engaged results"
+ "found all %ld engaged results"
+ "found top %ld engaged results"
+ "getting top engaged results"
+ "initializing session with configuration: %@"
+ "ranking, getting all engaged results"
+ "recentResultsWithOptions: %{sensitive}@"
+ "returning %ld engaged completions"
+ "showRecent topicId=%{sensitive}@ title=%{sensitive}@ type=%d"
- "spotlight cache: caching contact with type"
- "spotlight cache: caching person with type"
- "spotlight cache: caching result with type: %d"
- "spotlight cache: caching suggestion with type: %d"
- "spotlight cache: could not add contact result to cache"
- "spotlight cache: could not add local result to cache"
- "spotlight cache: could not add person result to cache"
- "spotlight cache: could not add result to cache"
- "spotlight cache: could not add suggestion to cache"
- "spotlight cache: could not create cached contact result"
- "spotlight cache: could not create cached person result"
- "spotlight cache: could not create cached result with result: %d"
- "spotlight cache: could not create cached result with suggestion: %d"
- "spotlight cache: could not create search result with engaged result"
- "spotlight cache: could not delete cached contact result"
- "spotlight cache: could not delete cached person result"
- "spotlight cache: could not delete cached result"
- "spotlight cache: could not delete cached result with result: %d"
- "spotlight cache: could not delete cached result with suggestion: %d"
- "spotlight cache: could not encode cached topic: %d"
- "spotlight cache: could not encode generic topic"
- "spotlight cache: could not encode generic topic. error: %@"
- "spotlight cache: could not encode local cached topic: %d"
- "spotlight cache: could not encode local contact topic"
- "spotlight cache: could not encode local person topic"
- "spotlight cache: deleting contact with type"
- "spotlight cache: deleting local result with type: %d"
- "spotlight cache: deleting person with type"
- "spotlight cache: deleting result with type: %d"
- "spotlight cache: filtered to %ld engaged results"
- "spotlight cache: found %ld engaged results"
- "spotlight cache: found all %ld engaged results"
- "spotlight cache: found top %ld engaged results"
- "spotlight cache: getting top engaged results"
- "spotlight cache: initializing session with configuration: %@"
- "spotlight cache: meh"
- "spotlight cache: ranking, getting all engaged results"
- "spotlight cache: returning %ld engaged completions"
- "spotlight cache: spotlight cache: caching result with type: %d"
```
