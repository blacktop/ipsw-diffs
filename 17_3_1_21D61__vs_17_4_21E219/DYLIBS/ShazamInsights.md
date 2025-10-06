## ShazamInsights

> `/System/Library/PrivateFrameworks/ShazamInsights.framework/ShazamInsights`

```diff

-236.16.0.0.0
-  __TEXT.__text: 0xa1c0
+238.15.0.0.0
+  __TEXT.__text: 0xb118
   __TEXT.__auth_stubs: 0x4f0
-  __TEXT.__objc_methlist: 0xb84
+  __TEXT.__objc_methlist: 0xb74
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0xb07
+  __TEXT.__cstring: 0xba1
   __TEXT.__gcc_except_tab: 0xb4
   __TEXT.__oslogstring: 0x353
-  __TEXT.__unwind_info: 0x31c
+  __TEXT.__unwind_info: 0x358
   __TEXT.__objc_classname: 0x2e1
-  __TEXT.__objc_methname: 0x2420
+  __TEXT.__objc_methname: 0x24e8
   __TEXT.__objc_methtype: 0x6f6
-  __TEXT.__objc_stubs: 0x2000
+  __TEXT.__objc_stubs: 0x1fe0
   __DATA_CONST.__got: 0x60
-  __DATA_CONST.__const: 0x3e8
+  __DATA_CONST.__const: 0x618
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1828
-  __DATA_CONST.__objc_selrefs: 0x8e0
+  __DATA_CONST.__objc_const: 0x17c8
+  __DATA_CONST.__objc_selrefs: 0x8d0
+  __DATA_CONST.__objc_classrefs: 0x1a8
+  __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0x28
   __AUTH_CONST.__objc_const: 0xaa8
-  __AUTH_CONST.__cfstring: 0x8c0
+  __AUTH_CONST.__cfstring: 0x880
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__auth_got: 0x288
   __AUTH.__objc_data: 0x910
-  __DATA.__objc_classrefs: 0x1a8
-  __DATA.__objc_superrefs: 0x78
   __DATA.__objc_ivar: 0xcc
   __DATA.__data: 0x1e8
   __DATA.__bss: 0x48

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 4E479987-648A-3A72-B54D-CD400D0FE91A
-  Functions: 250
-  Symbols:   1216
-  CStrings:  721
+  UUID: 6B0A5210-D225-32B9-8321-A7F507DD3297
+  Functions: 268
+  Symbols:   1265
+  CStrings:  723
 
Symbols:
+ -[SHInsightsConfiguration artistsCachedDataMaxAgeWithCompletionHandler:]
+ -[SHInsightsConfiguration artistsClusterEndpointWithCompletionHandler:]
+ -[SHInsightsConfiguration artistsEnabledWithCompletionHandler:]
+ -[SHInsightsConfiguration geoChartsEndpointForDate:geoHash:completionHandler:]
+ -[SHInsightsConfiguration geoHashLengthsWithCompletionHandler:]
+ -[SHInsightsConfiguration tokenizedURLForBagPathKey:completionHandler:]
+ -[SHInsightsConfiguration tracksCachedDataMaxAgeWithCompletionHandler:]
+ -[SHInsightsConfiguration tracksClusterEndpointForStorefront:completionHandler:]
+ -[SHInsightsConfiguration tracksEnabledWithCompletionHandler:]
+ GCC_except_table9
+ ___46-[SHClusterQuery statusWithCompletionHandler:]_block_invoke_2
+ ___46-[SHClusterQuery statusWithCompletionHandler:]_block_invoke_3
+ ___61+[SHInsightsConfiguration fetchSharedInstanceWithCompletion:]_block_invoke.38
+ ___62-[SHInsightsConfiguration tracksEnabledWithCompletionHandler:]_block_invoke
+ ___63-[SHInsightsConfiguration artistsEnabledWithCompletionHandler:]_block_invoke
+ ___63-[SHInsightsConfiguration geoHashLengthsWithCompletionHandler:]_block_invoke
+ ___63-[SHInsightsConfiguration geoHashLengthsWithCompletionHandler:]_block_invoke_2
+ ___68-[SHClusterLoaderRequest URLForRequestForStorefront:withCompletion:]_block_invoke_2
+ ___68-[SHClusterLoaderRequest URLForRequestForStorefront:withCompletion:]_block_invoke_3
+ ___68-[SHClusterLoaderRequest URLForRequestForStorefront:withCompletion:]_block_invoke_4
+ ___68-[SHClusterLoaderRequest URLForRequestForStorefront:withCompletion:]_block_invoke_5
+ ___71-[SHInsightsConfiguration artistsClusterEndpointWithCompletionHandler:]_block_invoke
+ ___71-[SHInsightsConfiguration tokenizedURLForBagPathKey:completionHandler:]_block_invoke
+ ___71-[SHInsightsConfiguration tokenizedURLForBagPathKey:completionHandler:]_block_invoke_2
+ ___71-[SHInsightsConfiguration tracksCachedDataMaxAgeWithCompletionHandler:]_block_invoke
+ ___72-[SHInsightsConfiguration artistsCachedDataMaxAgeWithCompletionHandler:]_block_invoke
+ ___75+[SHAffinityGroupQuery affinityGroupsForLocation:atDate:completionHandler:]_block_invoke_3
+ ___75+[SHAffinityGroupQuery affinityGroupsForLocation:atDate:completionHandler:]_block_invoke_4
+ ___78-[SHInsightsConfiguration geoChartsEndpointForDate:geoHash:completionHandler:]_block_invoke
+ ___80-[SHInsightsConfiguration tracksClusterEndpointForStorefront:completionHandler:]_block_invoke
+ ___87-[SHTimeAndPlaceController affinityGroupsFromData:atLocation:onDate:completionHandler:]_block_invoke_2
+ ___block_descriptor_40_e8_32bs_e20_v20?0B8"NSError"12ls32l8
+ ___block_descriptor_40_e8_32bs_e20_v24?0d8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e36_v24?0"SHTokenizedURL"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40bs_e20_v24?0q8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e30_v24?0"NSString"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e36_v24?0"SHTokenizedURL"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e20_v24?0q8"NSError"16ls40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e27_v24?0"NSURL"8"NSError"16ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e27_v24?0"NSURL"8"NSError"16ls48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e30_v24?0"NSString"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e33_v16?0"SHInsightsConfiguration"8ls48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e36_v24?0"SHTokenizedURL"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e8_v16?0d8ls32l8s48l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e23_v32?0q8q16"NSError"24ls56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e33_v16?0"SHInsightsConfiguration"8ls56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e8_v16?0d8ls32l8s40l8s48l8s56l8
+ ___block_literal_global.41
+ _objc_msgSend$artistsCachedDataMaxAgeWithCompletionHandler:
+ _objc_msgSend$artistsClusterEndpointWithCompletionHandler:
+ _objc_msgSend$booleanBackedByStringForKey:completionHandler:
+ _objc_msgSend$doubleBackedByStringForKey:completionHandler:
+ _objc_msgSend$geoChartsEndpointForDate:geoHash:completionHandler:
+ _objc_msgSend$geoHashLengthsWithCompletionHandler:
+ _objc_msgSend$integerBackedByStringForKey:completionHandler:
+ _objc_msgSend$stringForKey:withCompletionHandler:
+ _objc_msgSend$tokenizedURLForBagPathKey:completionHandler:
+ _objc_msgSend$tracksCachedDataMaxAgeWithCompletionHandler:
+ _objc_msgSend$tracksClusterEndpointForStorefront:completionHandler:
- -[SHCDNDataFetcher endpointFromDate:insights:location:]
- -[SHInsightsConfiguration artistsCachedDataMaxAge]
- -[SHInsightsConfiguration artistsClusterEndpoint]
- -[SHInsightsConfiguration artistsEnabled]
- -[SHInsightsConfiguration geoChartsEndpointForDate:geoHash:]
- -[SHInsightsConfiguration maxGeoChartsGeohashLength]
- -[SHInsightsConfiguration minGeoChartsGeohashLength]
- -[SHInsightsConfiguration tokenizedURLForBagPathKey:]
- -[SHInsightsConfiguration tracksCachedDataMaxAge]
- -[SHInsightsConfiguration tracksClusterEndpointForStorefront:]
- -[SHInsightsConfiguration tracksEnabled]
- ___61+[SHInsightsConfiguration fetchSharedInstanceWithCompletion:]_block_invoke.47
- ___block_descriptor_56_e8_32s40s48bs_e33_v16?0"SHInsightsConfiguration"8ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56bs_e33_v16?0"SHInsightsConfiguration"8ls32l8s40l8s48l8s56l8
- ___block_literal_global.50
- _objc_msgSend$artistsCachedDataMaxAge
- _objc_msgSend$artistsClusterEndpoint
- _objc_msgSend$booleanBackedByStringForKey:
- _objc_msgSend$doubleBackedByStringForKey:
- _objc_msgSend$geoChartsEndpointForDate:geoHash:
- _objc_msgSend$integerBackedByStringForKey:
- _objc_msgSend$maxGeoChartsGeohashLength
- _objc_msgSend$minGeoChartsGeohashLength
- _objc_msgSend$stringForKey:
- _objc_msgSend$tokenizedURLForBagPathKey:
- _objc_msgSend$tracksCachedDataMaxAge
- _objc_msgSend$tracksClusterEndpointForStorefront:
CStrings:
+ "T@\"NSString\",?,R,C"
+ "artistsCachedDataMaxAgeWithCompletionHandler:"
+ "artistsClusterEndpointWithCompletionHandler:"
+ "artistsEnabledWithCompletionHandler:"
+ "booleanBackedByStringForKey:completionHandler:"
+ "doubleBackedByStringForKey:completionHandler:"
+ "geoChartsEndpointForDate:geoHash:completionHandler:"
+ "geoHashLengthsWithCompletionHandler:"
+ "integerBackedByStringForKey:completionHandler:"
+ "stringForKey:withCompletionHandler:"
+ "tokenizedURLForBagPathKey:completionHandler:"
+ "tracksCachedDataMaxAgeWithCompletionHandler:"
+ "tracksClusterEndpointForStorefront:completionHandler:"
+ "tracksEnabledWithCompletionHandler:"
+ "v16@?0d8"
+ "v20@?0B8@\"NSError\"12"
+ "v24@?0@\"NSString\"8@\"NSError\"16"
+ "v24@?0@\"NSURL\"8@\"NSError\"16"
+ "v24@?0@\"SHTokenizedURL\"8@\"NSError\"16"
+ "v24@?0d8@\"NSError\"16"
+ "v24@?0q8@\"NSError\"16"
+ "v32@?0q8q16@\"NSError\"24"
- "Td,R,N"
- "artistsCachedDataMaxAge"
- "artistsClusterEndpoint"
- "artistsEnabled"
- "booleanBackedByStringForKey:"
- "doubleBackedByStringForKey:"
- "endpointFromDate:insights:location:"
- "geoChartsEndpointForDate:geoHash:"
- "integerBackedByStringForKey:"
- "maxGeoChartsGeohashLength"
- "minGeoChartsGeohashLength"
- "stringForKey:"
- "tokenizedURLForBagPathKey:"
- "tracks/enabled"
- "tracks/maxAgeInSeconds"
- "tracksCachedDataMaxAge"
- "tracksClusterEndpointForStorefront:"
- "tracksEnabled"

```
