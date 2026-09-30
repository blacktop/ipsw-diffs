## CPAnalytics

> `/System/Library/PrivateFrameworks/CPAnalytics.framework/Versions/A/CPAnalytics`

```diff

-700.21.101.0.0
-  __TEXT.__text: 0x108bc
-  __TEXT.__auth_stubs: 0x400
-  __TEXT.__objc_methlist: 0x1020
+700.27.103.0.0
+  __TEXT.__text: 0x1172c
+  __TEXT.__auth_stubs: 0x420
+  __TEXT.__objc_methlist: 0x10e8
   __TEXT.__const: 0x70
   __TEXT.__gcc_except_tab: 0x174
-  __TEXT.__cstring: 0x1848
-  __TEXT.__oslogstring: 0xb71
-  __TEXT.__unwind_info: 0x480
-  __TEXT.__objc_classname: 0x38a
-  __TEXT.__objc_methname: 0x2e12
+  __TEXT.__cstring: 0x1a98
+  __TEXT.__oslogstring: 0xc16
+  __TEXT.__unwind_info: 0x4a8
+  __TEXT.__objc_classname: 0x3c1
+  __TEXT.__objc_methname: 0x3006
   __TEXT.__objc_methtype: 0x4b8
-  __TEXT.__objc_stubs: 0x27c0
-  __DATA_CONST.__got: 0x1f8
-  __DATA_CONST.__const: 0x4d0
-  __DATA_CONST.__objc_classlist: 0xc8
+  __TEXT.__objc_stubs: 0x2a40
+  __DATA_CONST.__got: 0x220
+  __DATA_CONST.__const: 0x560
+  __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa98
+  __DATA_CONST.__objc_selrefs: 0xb38
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xa0
-  __AUTH_CONST.__auth_got: 0x210
+  __DATA_CONST.__objc_superrefs: 0xb0
+  __AUTH_CONST.__auth_got: 0x220
   __AUTH_CONST.__const: 0x2f0
-  __AUTH_CONST.__cfstring: 0x1e80
-  __AUTH_CONST.__objc_const: 0x2670
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x110
+  __AUTH_CONST.__cfstring: 0x20c0
+  __AUTH_CONST.__objc_const: 0x28d8
+  __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH.__objc_data: 0x280
+  __DATA.__objc_ivar: 0x120
   __DATA.__data: 0x248
   __DATA.__bss: 0x38
   __DATA_DIRTY.__objc_data: 0x5f0
   __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/Versions/A/BiomeLibrary
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreDuet.framework/Versions/A/CoreDuet
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftDemangle.dylib
-  Functions: 358
-  Symbols:   1277
-  CStrings:  267
+  Functions: 373
+  Symbols:   1355
+  CStrings:  286
 
Symbols:
+ -[CPAnalyticsBiomeBaseSample .cxx_destruct]
+ -[CPAnalyticsBiomeBaseSample date]
+ -[CPAnalyticsBiomeBaseSample identifier]
+ -[CPAnalyticsBiomeBaseSample initWithIdentifier:andDate:forSubset:]
+ -[CPAnalyticsBiomeBaseSample subset]
+ -[CPAnalyticsBiomeDestination .cxx_destruct]
+ -[CPAnalyticsBiomeDestination _baseSampleFromEvent:matcher:]
+ -[CPAnalyticsBiomeDestination _donateMemorySharedWithBaseSample:andEvent:]
+ -[CPAnalyticsBiomeDestination _dondateGenerativeMemoryCreationWithBaseSample:andEvent:]
+ -[CPAnalyticsBiomeDestination _sendBiomeEvent:matcher:]
+ -[CPAnalyticsBiomeDestination _updateWithConfig:]
+ -[CPAnalyticsBiomeDestination eventMatchers]
+ -[CPAnalyticsBiomeDestination initWithConfig:cpAnalyticsInstance:]
+ -[CPAnalyticsBiomeDestination processEvent:]
+ -[CPAnalyticsBiomeDestination updateWithConfig:]
+ GCC_except_table134
+ GCC_except_table140
+ GCC_except_table141
+ GCC_except_table142
+ GCC_except_table143
+ GCC_except_table146
+ GCC_except_table181
+ GCC_except_table185
+ GCC_except_table187
+ GCC_except_table355
+ OBJC_IVAR_$_CPAnalyticsBiomeBaseSample._date
+ OBJC_IVAR_$_CPAnalyticsBiomeBaseSample._identifier
+ OBJC_IVAR_$_CPAnalyticsBiomeBaseSample._subset
+ OBJC_IVAR_$_CPAnalyticsBiomeDestination._eventMatchers
+ _BiomeLibrary
+ _CPAnalyticsBiomeConfigEventsKey
+ _CPAnalyticsBiomeMemoryCreationGlobalTraitsKey
+ _CPAnalyticsBiomeMemoryCreationMaxGlobalTraitsToDonate
+ _CPAnalyticsBiomePayloadActivityTypeKey
+ _CPAnalyticsMemoryCreationDatasetNameKey
+ _CPAnalyticsMemoryCreationMemoryAssetCountKey
+ _CPAnalyticsMemoryCreationMemoryIsGeneratedKey
+ _CPAnalyticsMemoryCreationQueryHasActivityKey
+ _CPAnalyticsMemoryCreationQueryHasArtistKey
+ _CPAnalyticsMemoryCreationQueryHasGenreKey
+ _CPAnalyticsMemoryCreationQueryHasLocationKey
+ _CPAnalyticsMemoryCreationQueryHasMoodKey
+ _CPAnalyticsMemoryCreationQueryHasPersonKey
+ _CPAnalyticsMemoryCreationQueryHasSongKey
+ _CPAnalyticsMemoryCreationQueryHasTimeKey
+ _CPAnalyticsMemoryCreationQueryHasTripKey
+ _CPAnalyticsMemorySharedDatasetNameKey
+ _CPAnalyticsMemorySharedIsThirdPartyShareDestinationKey
+ _NSSelectorFromString
+ _OBJC_CLASS_$_BMPhotosMemoriesShared
+ _OBJC_CLASS_$_BMPhotosMemoryCreation
+ _OBJC_CLASS_$_CPAnalyticsBiomeBaseSample
+ _OBJC_CLASS_$_CPAnalyticsBiomeDestination
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSInvocation
+ _OBJC_METACLASS_$_CPAnalyticsBiomeBaseSample
+ _OBJC_METACLASS_$_CPAnalyticsBiomeDestination
+ __OBJC_$_INSTANCE_METHODS_CPAnalyticsBiomeBaseSample
+ __OBJC_$_INSTANCE_METHODS_CPAnalyticsBiomeDestination
+ __OBJC_$_INSTANCE_VARIABLES_CPAnalyticsBiomeBaseSample
+ __OBJC_$_INSTANCE_VARIABLES_CPAnalyticsBiomeDestination
+ __OBJC_$_PROP_LIST_CPAnalyticsBiomeBaseSample
+ __OBJC_$_PROP_LIST_CPAnalyticsBiomeDestination
+ __OBJC_CLASS_PROTOCOLS_$_CPAnalyticsBiomeDestination
+ __OBJC_CLASS_RO_$_CPAnalyticsBiomeBaseSample
+ __OBJC_CLASS_RO_$_CPAnalyticsBiomeDestination
+ __OBJC_METACLASS_RO_$_CPAnalyticsBiomeBaseSample
+ __OBJC_METACLASS_RO_$_CPAnalyticsBiomeDestination
+ __block_literal_global.1099
+ __block_literal_global.790
+ _objc_msgSend$Memories
+ _objc_msgSend$MemoryCreation
+ _objc_msgSend$Photos
+ _objc_msgSend$Shared
+ _objc_msgSend$_baseSampleFromEvent:matcher:
+ _objc_msgSend$_donateMemorySharedWithBaseSample:andEvent:
+ _objc_msgSend$_dondateGenerativeMemoryCreationWithBaseSample:andEvent:
+ _objc_msgSend$_sendBiomeEvent:matcher:
+ _objc_msgSend$_updateWithConfig:
+ _objc_msgSend$eventMatchers
+ _objc_msgSend$getReturnValue:
+ _objc_msgSend$initWithIdentifier:subset:isThirdPartyShareDestination:
+ _objc_msgSend$instanceMethodSignatureForSelector:
+ _objc_msgSend$invocationWithMethodSignature:
+ _objc_msgSend$invoke
+ _objc_msgSend$sendEvent:timestamp:
+ _objc_msgSend$setArgument:atIndex:
+ _objc_msgSend$setSelector:
+ _objc_msgSend$setTarget:
+ _objc_msgSend$source
- GCC_except_table124
- GCC_except_table130
- GCC_except_table131
- GCC_except_table132
- GCC_except_table133
- GCC_except_table136
- GCC_except_table167
- GCC_except_table171
- GCC_except_table175
- GCC_except_table340
- __block_literal_global.680
- __block_literal_global.961
CStrings:
+ "/photos/generativeMemory/create"
+ "/photos/memories/share"
+ "activityType"
+ "biome"
+ "i"
+ "initWithIdentifier:queryContainsPersonEntity:queryContainsActivityEntity:queryContainsTimeEntity:queryContainsLocationEntity:queryContainsTripEntity:queryContainsMusicArtist:queryContainsMusicSong:queryContainsMusicGenre:queryContainsMusicMood:globalTraits:memoryGenerated:memoryAssetCount:"
+ "isThirdPartyShareDestination"
+ "memoryAssetCount"
+ "memoryIsGenerated"
+ "queryHasActivity"
+ "queryHasArtist"
+ "queryHasGenre"
+ "queryHasLocation"
+ "queryHasMood"
+ "queryHasPerson"
+ "queryHasSong"
+ "queryHasTime"
+ "queryHasTrip"
+ "sampledGlobalTraitsForFedStats"

```
