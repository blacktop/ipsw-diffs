## CPAnalytics

> `/System/Library/PrivateFrameworks/CPAnalytics.framework/Versions/A/CPAnalytics`

```diff

-741.0.130.0.0
-  __TEXT.__text: 0x13514
+751.0.104.0.0
+  __TEXT.__text: 0x13638
   __TEXT.__auth_stubs: 0x420
-  __TEXT.__objc_methlist: 0x11a8
+  __TEXT.__objc_methlist: 0x138c
   __TEXT.__const: 0x178
   __TEXT.__gcc_except_tab: 0x174
-  __TEXT.__cstring: 0x1d9a
-  __TEXT.__oslogstring: 0xf5b
+  __TEXT.__cstring: 0x1df0
+  __TEXT.__oslogstring: 0xfa3
   __TEXT.__unwind_info: 0x4e8
   __TEXT.__objc_classname: 0x3c1
-  __TEXT.__objc_methname: 0x34b9
+  __TEXT.__objc_methname: 0x352c
   __TEXT.__objc_methtype: 0x4c0
-  __TEXT.__objc_stubs: 0x2de0
-  __DATA_CONST.__got: 0x278
-  __DATA_CONST.__const: 0x668
+  __TEXT.__objc_stubs: 0x2e40
+  __DATA_CONST.__got: 0x280
+  __DATA_CONST.__const: 0x688
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc28
+  __DATA_CONST.__objc_selrefs: 0xcc8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__auth_got: 0x220
   __AUTH_CONST.__const: 0x320
-  __AUTH_CONST.__cfstring: 0x2500
-  __AUTH_CONST.__objc_const: 0x2908
+  __AUTH_CONST.__cfstring: 0x2580
+  __AUTH_CONST.__objc_const: 0x25c0
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x280

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftDemangle.dylib
-  UUID: F28DCCE6-A9F4-3B5E-8250-B509CAA6D72B
+  UUID: 3E7D233F-D765-3176-BD82-0284E82E9E69
   Functions: 390
-  Symbols:   1449
-  CStrings:  1337
+  Symbols:   1457
+  CStrings:  1349
 
Symbols:
+ _CPAnalyticsBiomeMemoryCreationQueryActivityEntities
+ _CPAnalyticsBiomeMemoryCreationSanitizedPromptKey
+ _CPAnalyticsMemoryCreationIsUserPromptUnSafeKey
+ _CPAnalyticsMemoryCreationMemoryPromptSuggestionSourceKey
+ _OBJC_CLASS_$_NSLocale
+ __block_literal_global.1129
+ __block_literal_global.742
+ _objc_msgSend$currentLocale
+ _objc_msgSend$initWithIdentifier:queryContainsPersonEntity:queryContainsActivityEntity:queryContainsTimeEntity:queryContainsLocationEntity:queryContainsTripEntity:queryContainsMusicArtist:queryContainsMusicSong:queryContainsMusicGenre:queryContainsMusicMood:globalTraits:memoryGenerated:memoryAssetCount:rawPrompt:queryActivityEntities:language:region:memoryPromptSuggestionSource:
+ _objc_msgSend$languageCode
+ _objc_msgSend$regionCode
- __block_literal_global.1119
- __block_literal_global.744
- _objc_msgSend$initWithIdentifier:queryContainsPersonEntity:queryContainsActivityEntity:queryContainsTimeEntity:queryContainsLocationEntity:queryContainsTripEntity:queryContainsMusicArtist:queryContainsMusicSong:queryContainsMusicGenre:queryContainsMusicMood:globalTraits:memoryGenerated:memoryAssetCount:
Functions:
~ -[CPAnalyticsBiomeDestination _donateGenerativeMemoryCreationWithBaseSample:andEvent:] : 952 -> 1320
~ -[CPAnalyticsDestinationsRegistry _parseDestinationsFromConfig:cpAnalyticsInstance:] : 1616 -> 1604
~ -[CPAnalyticsLogEventMatcher initWithConfig:] : 1608 -> 1600
~ -[CPAnalytics generateNextSignpostID] : 288 -> 296
~ -[CPAnalytics updateWithConfiguration:] : 264 -> 260
~ -[CPAnalytics updateWithConfigurationFilename:inBundle:] : 308 -> 304
~ -[CPAnalytics setupWithConfigurationFilename:inBundle:] : 308 -> 304
~ -[CPAnalytics setupWithConfigurationAtURL:] : 264 -> 260
~ +[CPAnalytics timeIntervalBetweenReferenceDateAndCurrentDate] : 124 -> 112
~ +[CPAnalytics currentDate] : 88 -> 92
~ +[CPAnalytics isAllowed] : 68 -> 72
~ -[CPAnalyticsAppStateDestination updateWithConfig:] : 2772 -> 2728
CStrings:
+ "[Biome][Donation][MemoryCreation] No donation due to unsafe user prompt"
+ "currentLocale"
+ "initWithIdentifier:queryContainsPersonEntity:queryContainsActivityEntity:queryContainsTimeEntity:queryContainsLocationEntity:queryContainsTripEntity:queryContainsMusicArtist:queryContainsMusicSong:queryContainsMusicGenre:queryContainsMusicMood:globalTraits:memoryGenerated:memoryAssetCount:rawPrompt:queryActivityEntities:language:region:memoryPromptSuggestionSource:"
+ "isUserPromptUnSafe"
+ "languageCode"
+ "memoryPromptSuggestionSource"
+ "queryActivityEntities"
+ "regionCode"
+ "sanitizedPrompt"
- "initWithIdentifier:queryContainsPersonEntity:queryContainsActivityEntity:queryContainsTimeEntity:queryContainsLocationEntity:queryContainsTripEntity:queryContainsMusicArtist:queryContainsMusicSong:queryContainsMusicGenre:queryContainsMusicMood:globalTraits:memoryGenerated:memoryAssetCount:"

```
