## MediaMiningKit

> `/System/Library/PrivateFrameworks/MediaMiningKit.framework/MediaMiningKit`

```diff

-832.0.107.0.0
-  __TEXT.__text: 0x7fb34
-  __TEXT.__auth_stubs: 0x19d0
-  __TEXT.__objc_methlist: 0x7090
-  __TEXT.__const: 0xaf0
-  __TEXT.__cstring: 0x42ee
-  __TEXT.__swift5_typeref: 0x4da
-  __TEXT.__swift5_capture: 0x1b4
-  __TEXT.__oslogstring: 0x3843
-  __TEXT.__constg_swiftt: 0x27c
+840.1.220.0.0
+  __TEXT.__text: 0x896e0
+  __TEXT.__auth_stubs: 0x1a50
+  __TEXT.__objc_methlist: 0x7208
+  __TEXT.__const: 0xb70
+  __TEXT.__cstring: 0x3f90
+  __TEXT.__swift5_typeref: 0x54f
+  __TEXT.__swift5_capture: 0x23c
+  __TEXT.__oslogstring: 0x3c2d
+  __TEXT.__constg_swiftt: 0x28c
   __TEXT.__swift5_reflstr: 0x155
   __TEXT.__swift5_fieldmd: 0x12c
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x18
-  __TEXT.__swift_as_entry: 0x54
-  __TEXT.__swift_as_ret: 0x54
-  __TEXT.__gcc_except_tab: 0x2ca0
+  __TEXT.__swift_as_entry: 0x70
+  __TEXT.__swift_as_ret: 0x6c
+  __TEXT.__gcc_except_tab: 0x2da0
   __TEXT.__ustring: 0xec
-  __TEXT.__unwind_info: 0x2118
-  __TEXT.__eh_frame: 0xd6c
-  __TEXT.__objc_classname: 0xec7
-  __TEXT.__objc_methname: 0x12b1c
-  __TEXT.__objc_methtype: 0x1b7e
-  __TEXT.__objc_stubs: 0xc7c0
-  __DATA_CONST.__got: 0xae0
-  __DATA_CONST.__const: 0x2098
-  __DATA_CONST.__objc_classlist: 0x420
+  __TEXT.__unwind_info: 0x24e0
+  __TEXT.__eh_frame: 0xf48
+  __TEXT.__objc_classname: 0x1003
+  __TEXT.__objc_methname: 0x132af
+  __TEXT.__objc_methtype: 0x1d2e
+  __TEXT.__objc_stubs: 0xca60
+  __DATA_CONST.__got: 0xb18
+  __DATA_CONST.__const: 0x21a8
+  __DATA_CONST.__objc_classlist: 0x430
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x41a0
+  __DATA_CONST.__objc_selrefs: 0x4250
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x2d8
+  __DATA_CONST.__objc_superrefs: 0x2e8
   __DATA_CONST.__objc_arraydata: 0x2b0
-  __AUTH_CONST.__auth_got: 0xcf8
-  __AUTH_CONST.__const: 0x878
-  __AUTH_CONST.__cfstring: 0x5280
-  __AUTH_CONST.__objc_const: 0xd4c0
+  __AUTH_CONST.__auth_got: 0xd38
+  __AUTH_CONST.__const: 0x968
+  __AUTH_CONST.__cfstring: 0x5340
+  __AUTH_CONST.__objc_const: 0xd780
   __AUTH_CONST.__objc_arrayobj: 0x258
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x3f0
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x6b8
-  __AUTH.__data: 0x50
-  __DATA.__objc_ivar: 0x8e8
-  __DATA.__data: 0xa00
-  __DATA.__bss: 0x128
+  __AUTH.__objc_data: 0x770
+  __AUTH.__data: 0x58
+  __DATA.__objc_ivar: 0x904
+  __DATA.__data: 0xa98
+  __DATA.__bss: 0x130
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x2680
-  __DATA_DIRTY.__data: 0x238
-  __DATA_DIRTY.__bss: 0x120
+  __DATA_DIRTY.__objc_data: 0x2678
+  __DATA_DIRTY.__data: 0x218
+  __DATA_DIRTY.__bss: 0x118
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F2977D2A-4F58-3655-AACD-0B5E9AB43009
-  Functions: 2667
-  Symbols:   9222
-  CStrings:  5173
+  UUID: 9EFABA1E-3AD6-3C85-90D1-969D1A20DE25
+  Functions: 2743
+  Symbols:   9357
+  CStrings:  5221
 
Symbols:
+ +[CLSPublicEventCache timeIntervalForDate:]
+ +[CLSPublicEventStaleTuplesResult emptyResult]
+ -[CLSCachedTimeLocationTuple .cxx_destruct]
+ -[CLSCachedTimeLocationTuple coordinates]
+ -[CLSCachedTimeLocationTuple endDate]
+ -[CLSCachedTimeLocationTuple initWithQueryLocation:lastValidatedDate:]
+ -[CLSCachedTimeLocationTuple initWithStartDate:endDate:coordinates:lastValidatedDate:]
+ -[CLSCachedTimeLocationTuple lastValidatedDate]
+ -[CLSCachedTimeLocationTuple startDate]
+ -[CLSCachedTimeLocationTuple timeLocationIdentifier]
+ -[CLSPublicEventCache _processQueryLocationsInContext:matchingPredicate:processingBlock:error:]
+ -[CLSPublicEventCache _removeQueryLocationsForTimeLocationTuples:inContext:error:]
+ -[CLSPublicEventCache invalidateCacheItemsBeforeDateWithTimestamp:error:]
+ -[CLSPublicEventCache invalidateCacheItemsWithTimeLocationTuples:error:]
+ -[CLSPublicEventCache timeLocationTuplesFromCacheWithError:]
+ -[CLSPublicEventCache updateTimeLocationTuples:withTimestamp:error:]
+ -[CLSPublicEventManager _invalidateStaleTimeLocationTuplesInResult:allCachedTimeLocationTuples:analyticsPayload:error:]
+ -[CLSPublicEventManager invalidateAllCaches]
+ -[CLSPublicEventManager invalidateAllTimeLocationTuplesWithError:]
+ -[CLSPublicEventManager invalidateCacheItemsBeforeDateWithTimestamp:error:]
+ -[CLSPublicEventManager invalidateStaleCacheItemsUsingServiceWithCompletionBlock:]
+ -[CLSPublicEventManager invalidateTimeLocationTuplesBeforeDate:error:]
+ -[CLSPublicEventManager invalidateTimeLocationTuplesFromTuples:error:]
+ -[CLSPublicEventManager staleTuplesWithCompletionBlock:]
+ -[CLSPublicEventManager updateAllTimeLocationTuplesWithDate:error:]
+ -[CLSPublicEventStaleTuplesResult .cxx_destruct]
+ -[CLSPublicEventStaleTuplesResult initWithStaleLocationTuples:lastQueriedDate:]
+ -[CLSPublicEventStaleTuplesResult lastQueriedDate]
+ -[CLSPublicEventStaleTuplesResult staleTimeLocationTuples]
+ GCC_except_table1058
+ GCC_except_table1151
+ GCC_except_table1318
+ GCC_except_table1325
+ GCC_except_table1328
+ GCC_except_table1354
+ GCC_except_table1356
+ GCC_except_table1406
+ GCC_except_table1412
+ GCC_except_table1418
+ GCC_except_table1437
+ GCC_except_table1616
+ GCC_except_table1621
+ GCC_except_table1628
+ GCC_except_table1636
+ GCC_except_table1639
+ GCC_except_table1641
+ GCC_except_table1642
+ GCC_except_table1644
+ GCC_except_table1649
+ GCC_except_table1651
+ GCC_except_table1662
+ GCC_except_table1664
+ GCC_except_table1665
+ GCC_except_table1702
+ GCC_except_table1745
+ GCC_except_table1797
+ GCC_except_table1798
+ GCC_except_table1799
+ GCC_except_table1803
+ GCC_except_table1815
+ GCC_except_table1818
+ GCC_except_table1837
+ GCC_except_table1840
+ GCC_except_table1846
+ GCC_except_table1847
+ GCC_except_table1848
+ GCC_except_table1853
+ GCC_except_table1856
+ GCC_except_table1894
+ GCC_except_table1896
+ GCC_except_table1899
+ GCC_except_table1901
+ GCC_except_table1961
+ GCC_except_table1965
+ GCC_except_table1967
+ GCC_except_table2016
+ GCC_except_table2039
+ GCC_except_table2244
+ GCC_except_table2248
+ GCC_except_table2250
+ GCC_except_table2252
+ GCC_except_table2256
+ GCC_except_table2258
+ GCC_except_table2262
+ GCC_except_table2266
+ GCC_except_table2271
+ GCC_except_table2275
+ GCC_except_table2278
+ GCC_except_table2280
+ GCC_except_table2361
+ GCC_except_table2362
+ GCC_except_table2363
+ GCC_except_table2364
+ GCC_except_table2365
+ GCC_except_table2366
+ GCC_except_table2372
+ GCC_except_table2377
+ _CLSExpandedDateIntervalForTimeLocationTuple
+ _CLSExpandedEndDateForTimeLocationTuple
+ _CLSExpandedStartDateForTimeLocationTuple
+ _CLSPublicEventAnalyticsKeyInvalidatedStaleTuples
+ _CLSPublicEventAnalyticsKeyNumberOfInvalidatedStaleTuples
+ _CLSPublicEventAnalyticsKeyPercentOfTuplesInvalidated
+ _CLSPublicEventAnalyticsKeyUpdatedTupleTimestamps
+ _CLSPublicEventManagerErrorDomain
+ _CLSPublicEventManagerFullResetTupleThreshold
+ _CLSPublicEventTimeLocationTupleMaxFetchBatchSize
+ _CLSTimeLocationTupleIdentifier
+ _OBJC_CLASS_$_CLSCachedTimeLocationTuple
+ _OBJC_CLASS_$_CLSPublicEventStaleTuplesResult
+ _OBJC_IVAR_$_CLSCachedTimeLocationTuple._coordinates
+ _OBJC_IVAR_$_CLSCachedTimeLocationTuple._endDate
+ _OBJC_IVAR_$_CLSCachedTimeLocationTuple._lastValidatedDate
+ _OBJC_IVAR_$_CLSCachedTimeLocationTuple._startDate
+ _OBJC_IVAR_$_CLSCachedTimeLocationTuple._timeLocationIdentifier
+ _OBJC_IVAR_$_CLSPublicEventStaleTuplesResult._lastQueriedDate
+ _OBJC_IVAR_$_CLSPublicEventStaleTuplesResult._staleTimeLocationTuples
+ _OBJC_METACLASS_$_CLSCachedTimeLocationTuple
+ _OBJC_METACLASS_$_CLSPublicEventStaleTuplesResult
+ __IVARS_CLSPublicEventGeoServiceClient
+ __OBJC_$_CLASS_METHODS_CLSPublicEventStaleTuplesResult
+ __OBJC_$_INSTANCE_METHODS_CLSCachedTimeLocationTuple
+ __OBJC_$_INSTANCE_METHODS_CLSPublicEventStaleTuplesResult
+ __OBJC_$_INSTANCE_VARIABLES_CLSCachedTimeLocationTuple
+ __OBJC_$_INSTANCE_VARIABLES_CLSPublicEventStaleTuplesResult
+ __OBJC_$_PROP_LIST_CLSCachedTimeLocationTuple
+ __OBJC_$_PROP_LIST_CLSPublicEventStaleTuplesResult
+ __OBJC_CLASS_PROTOCOLS_$_CLSCachedTimeLocationTuple
+ __OBJC_CLASS_RO_$_CLSCachedTimeLocationTuple
+ __OBJC_CLASS_RO_$_CLSPublicEventStaleTuplesResult
+ __OBJC_METACLASS_RO_$_CLSCachedTimeLocationTuple
+ __OBJC_METACLASS_RO_$_CLSPublicEventStaleTuplesResult
+ __PROTOCOLS_CLSPublicEventGeoServiceClient.6
+ __PROTOCOLS_CLSPublicEventShazamServiceClient.6
+ ___56-[CLSPublicEventManager staleTuplesWithCompletionBlock:]_block_invoke
+ ___60-[CLSPublicEventCache timeLocationTuplesFromCacheWithError:]_block_invoke
+ ___68-[CLSPublicEventCache updateTimeLocationTuples:withTimestamp:error:]_block_invoke
+ ___68-[CLSPublicEventCache updateTimeLocationTuples:withTimestamp:error:]_block_invoke_2
+ ___72-[CLSPublicEventCache invalidateCacheItemsWithTimeLocationTuples:error:]_block_invoke
+ ___73-[CLSPublicEventCache invalidateCacheItemsBeforeDateWithTimestamp:error:]_block_invoke
+ ___73-[CLSPublicEventCache invalidateCacheItemsBeforeDateWithTimestamp:error:]_block_invoke_2
+ ___82-[CLSPublicEventCache _removeQueryLocationsForTimeLocationTuples:inContext:error:]_block_invoke
+ ___82-[CLSPublicEventManager invalidateStaleCacheItemsUsingServiceWithCompletionBlock:]_block_invoke
+ ___Block_byref_object_copy_.3850
+ ___Block_byref_object_copy_.4322
+ ___Block_byref_object_copy_.5667
+ ___Block_byref_object_copy_.6330
+ ___Block_byref_object_copy_.7371
+ ___Block_byref_object_dispose_.3851
+ ___Block_byref_object_dispose_.4323
+ ___Block_byref_object_dispose_.5668
+ ___Block_byref_object_dispose_.6331
+ ___Block_byref_object_dispose_.7372
+ ___block_descriptor_40_e21_B24?0"NSArray"8^16l
+ ___block_descriptor_40_e8_32bs_e53_v24?0"CLSPublicEventStaleTuplesResult"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e21_B24?0"NSArray"8^16ls32l8
+ ___block_descriptor_56_e8_32s40r48r_e5_v8?0ls32l8r40l8r48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e53_v24?0"CLSPublicEventStaleTuplesResult"8"NSError"16ls56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48r56r_e5_v8?0lr48l8s32l8s40l8r56l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e5_v8?0lr56l8s32l8s40l8s48l8r64l8
+ ___block_literal_global.3005
+ ___block_literal_global.3492
+ ___block_literal_global.3847
+ ___block_literal_global.4349
+ ___block_literal_global.5068
+ ___block_literal_global.5721
+ ___block_literal_global.5822
+ ___block_literal_global.6118
+ ___block_literal_global.6455
+ ___block_literal_global.7816
+ ___block_literal_global.7881
+ _objc_msgSend$_invalidateStaleTimeLocationTuplesInResult:allCachedTimeLocationTuples:analyticsPayload:error:
+ _objc_msgSend$_processQueryLocationsInContext:matchingPredicate:processingBlock:error:
+ _objc_msgSend$_removeQueryLocationsForTimeLocationTuples:inContext:error:
+ _objc_msgSend$dateWithTimeIntervalSince1970:
+ _objc_msgSend$emptyResult
+ _objc_msgSend$initWithCategory:localizedName:localizedSubcategories:
+ _objc_msgSend$initWithMapsIdentifierString:
+ _objc_msgSend$initWithQueryLocation:lastValidatedDate:
+ _objc_msgSend$initWithStaleLocationTuples:lastQueriedDate:
+ _objc_msgSend$initWithStartDate:endDate:coordinates:lastValidatedDate:
+ _objc_msgSend$initWithTimeLocationTuples:radius:
+ _objc_msgSend$initWithVersionString:dateOfServerUpdate:
+ _objc_msgSend$invalidateCacheItemsBeforeDateWithTimestamp:error:
+ _objc_msgSend$invalidateCacheItemsWithTimeLocationTuples:error:
+ _objc_msgSend$invalidateTimeLocationTuplesFromTuples:error:
+ _objc_msgSend$lastQueriedDate
+ _objc_msgSend$lastValidatedDate
+ _objc_msgSend$maxParametersCountForSpatialEventLookup
+ _objc_msgSend$orPredicateWithSubpredicates:
+ _objc_msgSend$staleTimeLocationTuples
+ _objc_msgSend$staleTimeLocationTuplesFromTuples:queryRadius:completionBlock:
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$timeIntervalForDate:
+ _objc_msgSend$timeLocationTuplesFromCacheWithError:
+ _objc_msgSend$updateTimeLocationTuples:withTimestamp:error:
+ _objc_msgSend$updateTimestamp
+ _objectdestroy.12Tm
+ _objectdestroy.19Tm
+ _sCLSDateHelperGMTTimeZone.5060
+ _swift_arrayInitWithCopy
+ _symbolic So31CLSPublicEventStaleTuplesResultCSgSo7NSErrorCSgIeyBhyy_
+ _symbolic So7NSArrayC
+ _symbolic _____ySS______pG s18_DictionaryStorageC So20CLSTimeLocationTupleP
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 10Foundation4DateV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 12ShazamEvents12EventServiceV19GeoRegionDescriptorV
- -[CLSPublicEventCache invalidateCacheItemsBeforeDateWithTimestamp:]
- -[CLSPublicEventManager invalidateCacheItemsBeforeDateWithTimestamp:]
- GCC_except_table1054
- GCC_except_table1147
- GCC_except_table1314
- GCC_except_table1321
- GCC_except_table1324
- GCC_except_table1350
- GCC_except_table1352
- GCC_except_table1402
- GCC_except_table1408
- GCC_except_table1410
- GCC_except_table1433
- GCC_except_table1612
- GCC_except_table1613
- GCC_except_table1618
- GCC_except_table1619
- GCC_except_table1620
- GCC_except_table1629
- GCC_except_table1632
- GCC_except_table1640
- GCC_except_table1643
- GCC_except_table1645
- GCC_except_table1650
- GCC_except_table1656
- GCC_except_table1657
- GCC_except_table1698
- GCC_except_table1731
- GCC_except_table1775
- GCC_except_table1783
- GCC_except_table1784
- GCC_except_table1785
- GCC_except_table1801
- GCC_except_table1804
- GCC_except_table1811
- GCC_except_table1819
- GCC_except_table1823
- GCC_except_table1826
- GCC_except_table1832
- GCC_except_table1834
- GCC_except_table1842
- GCC_except_table1880
- GCC_except_table1882
- GCC_except_table1885
- GCC_except_table1887
- GCC_except_table1942
- GCC_except_table1946
- GCC_except_table1948
- GCC_except_table1997
- GCC_except_table2020
- GCC_except_table2216
- GCC_except_table2220
- GCC_except_table2222
- GCC_except_table2224
- GCC_except_table2226
- GCC_except_table2230
- GCC_except_table2234
- GCC_except_table2239
- GCC_except_table2323
- GCC_except_table2324
- GCC_except_table2325
- GCC_except_table2326
- GCC_except_table2327
- GCC_except_table2328
- GCC_except_table2334
- GCC_except_table2339
- __IVARS_CLSPublicEventShazamServiceClient
- __PROTOCOLS_CLSPublicEventGeoServiceClient.4
- __PROTOCOLS_CLSPublicEventShazamServiceClient.4
- ___67-[CLSPublicEventCache invalidateCacheItemsBeforeDateWithTimestamp:]_block_invoke
- ___67-[CLSPublicEventCache invalidateCacheItemsBeforeDateWithTimestamp:]_block_invoke_2
- ___Block_byref_object_copy_.3842
- ___Block_byref_object_copy_.4314
- ___Block_byref_object_copy_.5623
- ___Block_byref_object_copy_.6256
- ___Block_byref_object_copy_.7241
- ___Block_byref_object_dispose_.3843
- ___Block_byref_object_dispose_.4315
- ___Block_byref_object_dispose_.5624
- ___Block_byref_object_dispose_.6257
- ___Block_byref_object_dispose_.7242
- ___block_descriptor_40_e8_32s_e49_v24?0"NSManagedObjectContext"8"NSMutableSet"16ls32l8
- ___block_literal_global.2997
- ___block_literal_global.3484
- ___block_literal_global.3839
- ___block_literal_global.4341
- ___block_literal_global.5060
- ___block_literal_global.5677
- ___block_literal_global.5778
- ___block_literal_global.6044
- ___block_literal_global.6381
- ___block_literal_global.7652
- ___block_literal_global.7717
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$expandedEndDate
- _objc_msgSend$expandedStartDate
- _objc_msgSend$invalidateCacheItemsBeforeDateWithTimestamp:
- _objc_msgSend$processPendingChanges
- _objc_msgSend$queryLocations
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x5
- _objectdestroy.18Tm
- _objectdestroy.9Tm
- _sCLSDateHelperGMTTimeZone.5052
CStrings:
+ "%f-%f-%f-%f"
+ "@24@0:8^@16"
+ "@56@0:8@16@24{CLLocationCoordinate2D=dd}32@48"
+ "B24@?0@\"NSArray\"8^@16"
+ "B32@0:8@16^@24"
+ "B32@0:8d16^@24"
+ "B40@0:8@16@24^@32"
+ "B40@0:8@16d24^@32"
+ "B48@0:8@16@24@32^@40"
+ "B48@0:8@16@24@?32^@40"
+ "CLSCachedTimeLocationTuple"
+ "CLSPublicEventCache - An error occured fetching or saving to the database: \"%@\""
+ "CLSPublicEventCache - An error occured invalidating time location tuples: %@"
+ "CLSPublicEventCache - failed to remove query locations, error: %@"
+ "CLSPublicEventCache failed to save with error: %@"
+ "CLSPublicEventStaleTuplesResult"
+ "CLSVisualUnderstandingServiceClient"
+ "PublicEventManager - event service client determined that %lu tuples are stale out of a total %lu tuples in cache"
+ "PublicEventManager - failed to update %lu tuples in cache with new timestamp %f, error: %@"
+ "PublicEventManager - invalidateStaleCacheItemsUsingServiceWithCompletionBlock cache read failed with error: %@)"
+ "PublicEventManager - invalidateStaleCacheItemsUsingServiceWithCompletionBlock failed to invalidate %lu time location tuples, error: %@"
+ "PublicEventManager - staleTuplesWithCompletionBlock - no tuples in cache, so nothing to check"
+ "PublicEventManager - updated %lu tuples in cache with new timestamp %f"
+ "T@\"NSArray\",R,N,V_staleTimeLocationTuples"
+ "T@\"NSDate\",R,N,V_endDate"
+ "T@\"NSDate\",R,N,V_lastQueriedDate"
+ "T@\"NSDate\",R,N,V_lastValidatedDate"
+ "T@\"NSDate\",R,N,V_startDate"
+ "T@\"NSString\",R,N,V_timeLocationIdentifier"
+ "T{CLLocationCoordinate2D=dd},R,N,V_coordinates"
+ "_coordinates"
+ "_invalidateStaleTimeLocationTuplesInResult:allCachedTimeLocationTuples:analyticsPayload:error:"
+ "_lastQueriedDate"
+ "_lastValidatedDate"
+ "_processQueryLocationsInContext:matchingPredicate:processingBlock:error:"
+ "_removeQueryLocationsForTimeLocationTuples:inContext:error:"
+ "_staleTimeLocationTuples"
+ "_timeLocationIdentifier"
+ "com.apple.mediaminingkit.CLSPublicEventManagerErrorDomain"
+ "dateWithTimeIntervalSince1970:"
+ "emptyResult"
+ "initWithQueryLocation:lastValidatedDate:"
+ "initWithStaleLocationTuples:lastQueriedDate:"
+ "initWithStartDate:endDate:coordinates:lastValidatedDate:"
+ "invalidateAllCaches"
+ "invalidateAllTimeLocationTuplesWithError:"
+ "invalidateCacheItemsBeforeDateWithTimestamp:error:"
+ "invalidateCacheItemsWithTimeLocationTuples:error:"
+ "invalidateStaleCacheItemsUsingServiceWithCompletionBlock:"
+ "invalidateTimeLocationTuplesBeforeDate:error:"
+ "invalidateTimeLocationTuplesFromTuples:error:"
+ "invalidatedStaleTuples"
+ "lastQueriedDate"
+ "lastValidatedDate"
+ "numberOfInvalidatedStaleTuples"
+ "orPredicateWithSubpredicates:"
+ "percentOfTuplesInvalidated"
+ "staleTimeLocationTuples"
+ "staleTimeLocationTuples not implemented for PublicEventGeoServiceClient, will not mark any tuples as stale."
+ "staleTimeLocationTuplesFromTuples:queryRadius:completionBlock:"
+ "staleTuplesWithCompletionBlock:"
+ "timeIntervalForDate:"
+ "timeLocationTuplesFromCacheWithError:"
+ "updateAllTimeLocationTuplesWithDate:error:"
+ "updateTimeLocationTuples:withTimestamp:error:"
+ "updatedTupleTimestamps"
+ "v24@?0@\"CLSPublicEventStaleTuplesResult\"8@\"NSError\"16"
+ "v40@0:8@\"NSArray\"16d24@?<v@?@\"CLSPublicEventStaleTuplesResult\"@\"NSError\">32"
+ "v40@0:8@16d24@?32"
- "expandedEndDate"
- "expandedStartDate"
- "processPendingChanges"
- "v24@?0@\"NSManagedObjectContext\"8@\"NSMutableSet\"16"

```
