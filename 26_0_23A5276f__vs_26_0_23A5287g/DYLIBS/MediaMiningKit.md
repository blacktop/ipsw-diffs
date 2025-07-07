## MediaMiningKit

> `/System/Library/PrivateFrameworks/MediaMiningKit.framework/MediaMiningKit`

```diff

-800.20.101.0.0
-  __TEXT.__text: 0x7a6e4
-  __TEXT.__auth_stubs: 0x1920
-  __TEXT.__objc_methlist: 0x6e08
-  __TEXT.__const: 0x900
-  __TEXT.__cstring: 0x40dc
-  __TEXT.__swift5_typeref: 0x442
-  __TEXT.__oslogstring: 0x37fe
-  __TEXT.__swift5_capture: 0x114
-  __TEXT.__constg_swiftt: 0x264
+800.26.109.0.0
+  __TEXT.__text: 0x7f738
+  __TEXT.__auth_stubs: 0x19d0
+  __TEXT.__objc_methlist: 0x7068
+  __TEXT.__const: 0x928
+  __TEXT.__cstring: 0x42d6
+  __TEXT.__swift5_typeref: 0x4da
+  __TEXT.__swift5_capture: 0x1b4
+  __TEXT.__oslogstring: 0x3843
+  __TEXT.__constg_swiftt: 0x27c
   __TEXT.__swift5_reflstr: 0x155
   __TEXT.__swift5_fieldmd: 0x12c
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x18
-  __TEXT.__swift_as_entry: 0x40
-  __TEXT.__swift_as_ret: 0x44
-  __TEXT.__gcc_except_tab: 0x2bc8
+  __TEXT.__swift_as_entry: 0x54
+  __TEXT.__swift_as_ret: 0x54
+  __TEXT.__gcc_except_tab: 0x2cb8
   __TEXT.__ustring: 0xec
-  __TEXT.__unwind_info: 0x1fa8
-  __TEXT.__eh_frame: 0xab8
-  __TEXT.__objc_classname: 0xe9f
-  __TEXT.__objc_methname: 0x1235a
-  __TEXT.__objc_methtype: 0x1ac3
-  __TEXT.__objc_stubs: 0xc240
-  __DATA_CONST.__got: 0xaa8
-  __DATA_CONST.__const: 0x1fa0
-  __DATA_CONST.__objc_classlist: 0x418
+  __TEXT.__unwind_info: 0x2130
+  __TEXT.__eh_frame: 0xd6c
+  __TEXT.__objc_classname: 0xec4
+  __TEXT.__objc_methname: 0x12aa1
+  __TEXT.__objc_methtype: 0x1b7e
+  __TEXT.__objc_stubs: 0xc760
+  __DATA_CONST.__got: 0xad8
+  __DATA_CONST.__const: 0x2098
+  __DATA_CONST.__objc_classlist: 0x420
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4008
+  __DATA_CONST.__objc_selrefs: 0x4188
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x2d0
+  __DATA_CONST.__objc_superrefs: 0x2d8
   __DATA_CONST.__objc_arraydata: 0x2b0
-  __AUTH_CONST.__auth_got: 0xca0
-  __AUTH_CONST.__const: 0x738
-  __AUTH_CONST.__cfstring: 0x5040
-  __AUTH_CONST.__objc_const: 0xd220
+  __AUTH_CONST.__auth_got: 0xcf8
+  __AUTH_CONST.__const: 0x878
+  __AUTH_CONST.__cfstring: 0x5260
+  __AUTH_CONST.__objc_const: 0xd4b0
   __AUTH_CONST.__objc_arrayobj: 0x258
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x3f0
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x898
-  __AUTH.__data: 0x80
-  __DATA.__objc_ivar: 0x8c4
-  __DATA.__data: 0x928
-  __DATA.__bss: 0x130
+  __AUTH.__objc_data: 0x948
+  __AUTH.__data: 0x78
+  __DATA.__objc_ivar: 0x8e8
+  __DATA.__data: 0x950
+  __DATA.__bss: 0x140
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x2438
-  __DATA_DIRTY.__data: 0x378
+  __DATA_DIRTY.__objc_data: 0x23f0
+  __DATA_DIRTY.__data: 0x328
   __DATA_DIRTY.__bss: 0x108
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6F5EE79C-50C2-33A2-BC32-0791DB5724F9
-  Functions: 2568
-  Symbols:   9019
-  CStrings:  5058
+  UUID: 5EF3E1CA-9D32-3C62-9807-2CE6DCDEB0F2
+  Functions: 2667
+  Symbols:   9211
+  CStrings:  5166
 
Symbols:
+ +[CLSCalendar _calendarForIdentifier:]
+ +[CLSCalendar components:fromDate:withCalendarIdentifier:]
+ +[CLSCalendar countOfWeekday:inMonthOfDate:withCalendarIdentifier:]
+ +[CLSCalendar dateByAddingDays:toDate:withCalendarIdentifier:]
+ +[CLSCalendar dateByAddingYears:toDate:withCalendarIdentifier:]
+ +[CLSCalendar dateFromComponents:inTimeZone:withCalendarIdentifier:]
+ +[CLSCalendar isLeapYearForDate:withCalendarIdentifier:]
+ +[CLSCalendar monthFromDate:withCalendarIdentifier:]
+ +[CLSCalendar rangeOfUnit:inUnit:forDate:withCalendarIdentifier:]
+ +[CLSCalendar yearFromDate:withCalendarIdentifier:]
+ +[CLSHolidayCalendarEventDateRule _dateComponentsFromRuleDescription:]
+ +[CLSManagedPublicEventServerVersion entityName]
+ -[CLSDBCache _saveWithError:]
+ -[CLSHolidayCalendarEventDateRule _endDate]
+ -[CLSHolidayCalendarEventDateRule _estimateBestEventDateComponentsToMatchDate:]
+ -[CLSHolidayCalendarEventDateRule _startDate]
+ -[CLSHolidayCalendarEventDateRule calendarIdentifier]
+ -[CLSHolidayCalendarEventDateRule endEra]
+ -[CLSHolidayCalendarEventDateRule enumerateDatesFromStartDate:toEndDate:usingBlock:]
+ -[CLSHolidayCalendarEventDateRule hasEndEra]
+ -[CLSHolidayCalendarEventDateRule hasExplicitEra]
+ -[CLSHolidayCalendarEventDateRule hasStartEra]
+ -[CLSHolidayCalendarEventDateRule leapYearOverrideComponents]
+ -[CLSHolidayCalendarEventDateRule localDateByEvaluatingRuleForDate:]
+ -[CLSHolidayCalendarEventDateRule matchesExplicitEra:]
+ -[CLSHolidayCalendarEventDateRule setEndEra:]
+ -[CLSHolidayCalendarEventDateRule setStartEra:]
+ -[CLSHolidayCalendarEventDateRule startEra]
+ -[CLSHolidayCalendarEventRule _dateRuleForDate:countryCode:]
+ -[CLSHolidayCalendarEventRule _dateRuleForDate:supportedLocale:]
+ -[CLSHolidayCalendarEventRule _enumerateDatesFromStartDate:toEndDate:supportedLocale:usingBlock:]
+ -[CLSHolidayCalendarEventRule enumerateDatesFromStartDate:toEndDate:countryCode:usingBlock:]
+ -[CLSHolidayCalendarEventRule localDateByEvaluatingRuleForDate:countryCode:]
+ -[CLSHolidayCalendarEventRule localDateByEvaluatingRuleForDate:languageCode:]
+ -[CLSHolidayCalendarEventService dateForRuleWithUUID:byEvaluatingForDate:]
+ -[CLSPublicEventCache _fetchRequestForLatestServerVersionForEventSourceService:]
+ -[CLSPublicEventCache getCachedServiceVersion:forEventSourceService:error:]
+ -[CLSPublicEventCache getScheduledCacheInvalidationDate:forEventSourceService:error:]
+ -[CLSPublicEventCache setLatestVersionScheduledInvalidationDate:forEventSourceService:error:]
+ -[CLSPublicEventCache setNewCachedServiceVersion:forEventSourceService:error:]
+ -[CLSPublicEventCacheCreator _queryEventsForTimeLocationTuples:invalidationTokens:queryContext:analyticsPayload:progressBlock:error:]
+ -[CLSPublicEventCacheCreator initWithCache:queryRadius:analytics:]
+ -[CLSPublicEventCachingOptions jobContext]
+ -[CLSPublicEventCachingOptions setJobContext:]
+ -[CLSPublicEventManager getCachedServiceVersion:forEventSourceService:error:]
+ -[CLSPublicEventManager getScheduledCacheInvalidationDate:forEventSourceService:error:]
+ -[CLSPublicEventManager initWithURL:analytics:]
+ -[CLSPublicEventManager requestCurrentServiceVersionWithCompletionBlock:]
+ -[CLSPublicEventManager setLatestVersionScheduledInvalidationDate:forEventSourceService:error:]
+ -[CLSPublicEventManager setNewCachedServiceVersion:forEventSourceService:error:]
+ -[CLSPublicEventServerVersion .cxx_destruct]
+ -[CLSPublicEventServerVersion dateOfServerUpdate]
+ -[CLSPublicEventServerVersion initWithVersionString:dateOfServerUpdate:]
+ -[CLSPublicEventServerVersion versionString]
+ GCC_except_table103
+ GCC_except_table1033
+ GCC_except_table1038
+ GCC_except_table1039
+ GCC_except_table105
+ GCC_except_table1053
+ GCC_except_table114
+ GCC_except_table1146
+ GCC_except_table116
+ GCC_except_table120
+ GCC_except_table128
+ GCC_except_table1313
+ GCC_except_table132
+ GCC_except_table1320
+ GCC_except_table1323
+ GCC_except_table1349
+ GCC_except_table1351
+ GCC_except_table1401
+ GCC_except_table1407
+ GCC_except_table1409
+ GCC_except_table1413
+ GCC_except_table1432
+ GCC_except_table145
+ GCC_except_table146
+ GCC_except_table149
+ GCC_except_table152
+ GCC_except_table153
+ GCC_except_table156
+ GCC_except_table16
+ GCC_except_table1612
+ GCC_except_table1616
+ GCC_except_table1618
+ GCC_except_table1619
+ GCC_except_table1621
+ GCC_except_table1622
+ GCC_except_table1623
+ GCC_except_table1625
+ GCC_except_table1631
+ GCC_except_table1632
+ GCC_except_table1633
+ GCC_except_table1634
+ GCC_except_table1636
+ GCC_except_table1637
+ GCC_except_table1639
+ GCC_except_table1642
+ GCC_except_table1644
+ GCC_except_table1646
+ GCC_except_table1649
+ GCC_except_table165
+ GCC_except_table1653
+ GCC_except_table1655
+ GCC_except_table1656
+ GCC_except_table1657
+ GCC_except_table1659
+ GCC_except_table166
+ GCC_except_table1660
+ GCC_except_table167
+ GCC_except_table168
+ GCC_except_table169
+ GCC_except_table1697
+ GCC_except_table1729
+ GCC_except_table1773
+ GCC_except_table1781
+ GCC_except_table1783
+ GCC_except_table1787
+ GCC_except_table1799
+ GCC_except_table1802
+ GCC_except_table1809
+ GCC_except_table1817
+ GCC_except_table1821
+ GCC_except_table1823
+ GCC_except_table1824
+ GCC_except_table1830
+ GCC_except_table1831
+ GCC_except_table1832
+ GCC_except_table1837
+ GCC_except_table1840
+ GCC_except_table1878
+ GCC_except_table1880
+ GCC_except_table1883
+ GCC_except_table1885
+ GCC_except_table1940
+ GCC_except_table1944
+ GCC_except_table1946
+ GCC_except_table1995
+ GCC_except_table200
+ GCC_except_table2018
+ GCC_except_table22
+ GCC_except_table2214
+ GCC_except_table2218
+ GCC_except_table2220
+ GCC_except_table2222
+ GCC_except_table2224
+ GCC_except_table2226
+ GCC_except_table2228
+ GCC_except_table2232
+ GCC_except_table2237
+ GCC_except_table2321
+ GCC_except_table2322
+ GCC_except_table2323
+ GCC_except_table2324
+ GCC_except_table2325
+ GCC_except_table2326
+ GCC_except_table2332
+ GCC_except_table2337
+ GCC_except_table258
+ GCC_except_table292
+ GCC_except_table312
+ GCC_except_table323
+ GCC_except_table327
+ GCC_except_table331
+ GCC_except_table335
+ GCC_except_table344
+ GCC_except_table361
+ GCC_except_table367
+ GCC_except_table368
+ GCC_except_table38
+ GCC_except_table444
+ GCC_except_table446
+ GCC_except_table462
+ GCC_except_table463
+ GCC_except_table465
+ GCC_except_table466
+ GCC_except_table489
+ GCC_except_table529
+ GCC_except_table549
+ GCC_except_table552
+ GCC_except_table556
+ GCC_except_table558
+ GCC_except_table597
+ GCC_except_table600
+ GCC_except_table611
+ GCC_except_table613
+ GCC_except_table617
+ GCC_except_table619
+ GCC_except_table623
+ GCC_except_table627
+ GCC_except_table630
+ GCC_except_table664
+ GCC_except_table665
+ GCC_except_table666
+ GCC_except_table691
+ GCC_except_table696
+ GCC_except_table700
+ GCC_except_table708
+ GCC_except_table711
+ GCC_except_table824
+ GCC_except_table895
+ GCC_except_table900
+ GCC_except_table91
+ GCC_except_table957
+ GCC_except_table961
+ GCC_except_table975
+ GCC_except_table976
+ GCC_except_table977
+ _NSCalendarIdentifierHebrew
+ _OBJC_CLASS_$_CLSManagedPublicEventServerVersion
+ _OBJC_CLASS_$_CLSPublicEventServerVersion
+ _OBJC_CLASS_$_NSISO8601DateFormatter
+ _OBJC_IVAR_$_CLSHolidayCalendarEventDateRule._calendarIdentifier
+ _OBJC_IVAR_$_CLSHolidayCalendarEventDateRule._endEra
+ _OBJC_IVAR_$_CLSHolidayCalendarEventDateRule._leapYearOverrideComponents
+ _OBJC_IVAR_$_CLSHolidayCalendarEventDateRule._startEra
+ _OBJC_IVAR_$_CLSPublicEventCacheCreator._analytics
+ _OBJC_IVAR_$_CLSPublicEventCachingOptions._jobContext
+ _OBJC_IVAR_$_CLSPublicEventManager._analytics
+ _OBJC_IVAR_$_CLSPublicEventServerVersion._dateOfServerUpdate
+ _OBJC_IVAR_$_CLSPublicEventServerVersion._versionString
+ _OBJC_METACLASS_$_CLSManagedPublicEventServerVersion
+ _OBJC_METACLASS_$_CLSPublicEventServerVersion
+ __OBJC_$_CLASS_METHODS_CLSHolidayCalendarEventDateRule
+ __OBJC_$_CLASS_METHODS_CLSManagedPublicEventServerVersion
+ __OBJC_$_CLASS_PROP_LIST_CLSManagedPublicEventServerVersion
+ __OBJC_$_INSTANCE_METHODS_CLSPublicEventServerVersion
+ __OBJC_$_INSTANCE_VARIABLES_CLSPublicEventServerVersion
+ __OBJC_$_PROP_LIST_CLSManagedPublicEventServerVersion
+ __OBJC_$_PROP_LIST_CLSPublicEventServerVersion
+ __OBJC_CLASS_RO_$_CLSManagedPublicEventServerVersion
+ __OBJC_CLASS_RO_$_CLSPublicEventServerVersion
+ __OBJC_METACLASS_RO_$_CLSManagedPublicEventServerVersion
+ __OBJC_METACLASS_RO_$_CLSPublicEventServerVersion
+ __PROTOCOLS_CLSPublicEventGeoServiceClient.4
+ __PROTOCOLS_CLSPublicEventShazamQueryHelper.8
+ __PROTOCOLS_CLSPublicEventShazamServiceClient.4
+ ___126-[CLSHolidayCalendarEventService _enumerateEventRulesWithNames:betweenLocalDate:andLocalDate:supportedCountryCode:usingBlock:]_block_invoke
+ ___133-[CLSPublicEventCacheCreator _queryEventsForTimeLocationTuples:invalidationTokens:queryContext:analyticsPayload:progressBlock:error:]_block_invoke
+ ___133-[CLSPublicEventCacheCreator _queryEventsForTimeLocationTuples:invalidationTokens:queryContext:analyticsPayload:progressBlock:error:]_block_invoke_2
+ ___133-[CLSPublicEventCacheCreator _queryEventsForTimeLocationTuples:invalidationTokens:queryContext:analyticsPayload:progressBlock:error:]_block_invoke_3
+ ___45-[CLSQueueBasedGeoMapQueryHelper _startQuery]_block_invoke.12
+ ___75-[CLSPublicEventCache getCachedServiceVersion:forEventSourceService:error:]_block_invoke
+ ___78-[CLSPublicEventCache setNewCachedServiceVersion:forEventSourceService:error:]_block_invoke
+ ___80-[CLSQueueBasedGeoMapQueryHelper launchQueryWithCancellerBlock:completionBlock:]_block_invoke
+ ___85-[CLSPublicEventCache getScheduledCacheInvalidationDate:forEventSourceService:error:]_block_invoke
+ ___91-[CLSQueueBasedGeoMapQueryHelper launchPublicEventQueryWithCancellerBlock:completionBlock:]_block_invoke_2
+ ___93-[CLSPublicEventCache setLatestVersionScheduledInvalidationDate:forEventSourceService:error:]_block_invoke
+ ___98-[CLSPublicEventCacheCreator createCacheForTimeLocationTuples:cachingOptions:progressBlock:error:]_block_invoke.101
+ ___Block_byref_object_copy_.1019
+ ___Block_byref_object_copy_.1244
+ ___Block_byref_object_copy_.3836
+ ___Block_byref_object_copy_.4309
+ ___Block_byref_object_copy_.5618
+ ___Block_byref_object_copy_.6254
+ ___Block_byref_object_copy_.718
+ ___Block_byref_object_copy_.7238
+ ___Block_byref_object_copy_.77
+ ___Block_byref_object_copy_.819
+ ___Block_byref_object_copy_.907
+ ___Block_byref_object_dispose_.1020
+ ___Block_byref_object_dispose_.1245
+ ___Block_byref_object_dispose_.3837
+ ___Block_byref_object_dispose_.4310
+ ___Block_byref_object_dispose_.5619
+ ___Block_byref_object_dispose_.6255
+ ___Block_byref_object_dispose_.719
+ ___Block_byref_object_dispose_.7239
+ ___Block_byref_object_dispose_.78
+ ___Block_byref_object_dispose_.820
+ ___Block_byref_object_dispose_.908
+ ___block_descriptor_168_e8_32s40s48s56s64s72s80s88s96bs104bs112r120r128r136r144r152r_e5_v8?0lr112l8s32l8s40l8s48l8s56l8s64l8s96l8s72l8s80l8r120l8r128l8s88l8r136l8s104l8r144l8r152l8
+ ___block_descriptor_40_e8_32bs_e54_v28?0B8"NSError"12"<CLSPublicEventQueryProtocol>"20ls32l8
+ ___block_descriptor_40_e8_32bs_e71_v36?0B8"NSError"12"<CLSPublicEventQueryProtocol>"20"NSDictionary"28ls32l8
+ ___block_descriptor_40_e8_32s_e20_v24?0"NSDate"8^B16ls32l8
+ ___block_descriptor_80_e8_32bs40r48r56r64r72r_e71_v36?0B8"NSError"12"<CLSPublicEventQueryProtocol>"20"NSDictionary"28lr40l8r48l8r56l8r64l8r72l8s32l8
+ ___block_descriptor_80_e8_32s40s48r56r64r_e5_v8?0ls32l8s40l8r48l8r56l8r64l8
+ ___block_descriptor_80_e8_32s40s48r56r_e5_v8?0ls32l8s40l8r48l8r56l8
+ ___block_descriptor_80_e8_32s40s48s56r64r_e5_v8?0ls32l8s40l8r56l8r64l8s48l8
+ ___block_literal_global.1023
+ ___block_literal_global.1047
+ ___block_literal_global.1119
+ ___block_literal_global.112
+ ___block_literal_global.1365
+ ___block_literal_global.159
+ ___block_literal_global.1601
+ ___block_literal_global.1930
+ ___block_literal_global.2090
+ ___block_literal_global.2135
+ ___block_literal_global.2436
+ ___block_literal_global.3002
+ ___block_literal_global.303
+ ___block_literal_global.3483
+ ___block_literal_global.3833
+ ___block_literal_global.4336
+ ___block_literal_global.5057
+ ___block_literal_global.5672
+ ___block_literal_global.5774
+ ___block_literal_global.598
+ ___block_literal_global.6042
+ ___block_literal_global.6379
+ ___block_literal_global.7648
+ ___block_literal_global.7713
+ ___block_literal_global.904
+ ___kCFBooleanFalse
+ __swift_FORCE_LOAD_$_swiftSpatial
+ __swift_FORCE_LOAD_$_swiftSpatial_$_MediaMiningKit
+ _kCLSHolidayCalendarEventRuleKeyCalendarIdentifier
+ _kCLSHolidayCalendarEventRuleKeyEndEra
+ _kCLSHolidayCalendarEventRuleKeyEra
+ _kCLSHolidayCalendarEventRuleKeyLeapYearOverride
+ _kCLSHolidayCalendarEventRuleKeyStartEra
+ _objc_msgSend$_calendarForIdentifier:
+ _objc_msgSend$_dateComponentsFromRuleDescription:
+ _objc_msgSend$_dateRuleForDate:countryCode:
+ _objc_msgSend$_dateRuleForDate:supportedLocale:
+ _objc_msgSend$_endDate
+ _objc_msgSend$_enumerateDatesFromStartDate:toEndDate:supportedLocale:usingBlock:
+ _objc_msgSend$_estimateBestEventDateComponentsToMatchDate:
+ _objc_msgSend$_fetchRequestForLatestServerVersionForEventSourceService:
+ _objc_msgSend$_queryEventsForTimeLocationTuples:invalidationTokens:queryContext:analyticsPayload:progressBlock:error:
+ _objc_msgSend$_saveWithError:
+ _objc_msgSend$_startDate
+ _objc_msgSend$components:fromDate:withCalendarIdentifier:
+ _objc_msgSend$countOfWeekday:inMonthOfDate:withCalendarIdentifier:
+ _objc_msgSend$dateByAddingDays:toDate:withCalendarIdentifier:
+ _objc_msgSend$dateByAddingYears:toDate:
+ _objc_msgSend$dateByAddingYears:toDate:withCalendarIdentifier:
+ _objc_msgSend$dateForRuleWithUUID:byEvaluatingForDate:
+ _objc_msgSend$dateFromComponents:inTimeZone:withCalendarIdentifier:
+ _objc_msgSend$dateOfScheduledCacheInvalidationForVersion
+ _objc_msgSend$dateOfServerUpdate
+ _objc_msgSend$endEra
+ _objc_msgSend$enumerateDatesFromStartDate:toEndDate:countryCode:usingBlock:
+ _objc_msgSend$enumerateDatesFromStartDate:toEndDate:usingBlock:
+ _objc_msgSend$getCachedServiceVersion:forEventSourceService:error:
+ _objc_msgSend$getScheduledCacheInvalidationDate:forEventSourceService:error:
+ _objc_msgSend$hasEndEra
+ _objc_msgSend$hasExplicitEra
+ _objc_msgSend$hasStartEra
+ _objc_msgSend$initWithCache:queryRadius:analytics:
+ _objc_msgSend$initWithDictionary:
+ _objc_msgSend$initWithURL:analytics:
+ _objc_msgSend$isLeapYearForDate:withCalendarIdentifier:
+ _objc_msgSend$jobContext
+ _objc_msgSend$localDateByEvaluatingRuleForDate:
+ _objc_msgSend$localDateByEvaluatingRuleForDate:countryCode:
+ _objc_msgSend$matchesExplicitEra:
+ _objc_msgSend$monthFromDate:withCalendarIdentifier:
+ _objc_msgSend$now
+ _objc_msgSend$numberWithLongLong:
+ _objc_msgSend$rangeOfUnit:inUnit:forDate:withCalendarIdentifier:
+ _objc_msgSend$serverVersionWithCompletionBlock:
+ _objc_msgSend$setDateOfLastCachedVersion:
+ _objc_msgSend$setDateOfScheduledCacheInvalidationForVersion:
+ _objc_msgSend$setDateOfServerUpdate:
+ _objc_msgSend$setEra:
+ _objc_msgSend$setLatestVersionScheduledInvalidationDate:forEventSourceService:error:
+ _objc_msgSend$setNewCachedServiceVersion:forEventSourceService:error:
+ _objc_msgSend$setVersion:
+ _objc_msgSend$startEra
+ _objc_msgSend$version
+ _objc_msgSend$versionString
+ _objc_msgSend$yearFromDate:withCalendarIdentifier:
+ _objectdestroy.35Tm
+ _objectdestroy.5Tm
+ _objectdestroy.9Tm
+ _sCLSDateHelperCalendarByIdentifier
+ _sCLSDateHelperGMTTimeZone.5049
+ _sCLSDefaultCalendarIdentifier
+ _swift_arrayDestroy
+ _swift_unknownObjectRelease_n
+ _symbolic Sb______pSg______pSgSDySSypGIegyggg_ s5ErrorP So27CLSPublicEventQueryProtocolP
+ _symbolic So27CLSPublicEventServerVersionCSgSo7NSErrorCSgIeyBhyy_
+ _symbolic Spy_____GIegy_ 10ObjectiveC8ObjCBoolV
+ _symbolic _____Sg 10Foundation4DateV
+ _symbolic _____So7NSErrorCSg______pSgSo12NSDictionaryCIeyByyyy_ 10ObjectiveC8ObjCBoolV So27CLSPublicEventQueryProtocolP
+ _symbolic _____ySSypG s18_DictionaryStorageC
+ _symbolic ypSg
- +[CLSCalendar rangeOfUnit:inUnit:forDate:]
- -[CLSFaceIdentificationOnDemand requestIdentificationOfFaces:error:]
- -[CLSHolidayCalendarEventDateRule localDateByEvaluatingRuleForYear:]
- -[CLSHolidayCalendarEventRule _dateRuleForYear:countryCode:]
- -[CLSHolidayCalendarEventRule _dateRuleForYear:supportedLocale:]
- -[CLSHolidayCalendarEventRule localDateByEvaluatingRuleForYear:countryCode:]
- -[CLSHolidayCalendarEventRule localDateByEvaluatingRuleForYear:languageCode:]
- -[CLSHolidayCalendarEventService dateForRuleWithUUID:byEvaluatingForYear:]
- -[CLSPublicEventCacheCreator _queryEventsForTimeLocationTuples:invalidationTokens:queryContext:progressBlock:error:]
- GCC_except_table100
- GCC_except_table1022
- GCC_except_table1027
- GCC_except_table1028
- GCC_except_table1042
- GCC_except_table109
- GCC_except_table111
- GCC_except_table1120
- GCC_except_table115
- GCC_except_table1183
- GCC_except_table122
- GCC_except_table123
- GCC_except_table124
- GCC_except_table125
- GCC_except_table1291
- GCC_except_table1298
- GCC_except_table1301
- GCC_except_table131
- GCC_except_table1327
- GCC_except_table1329
- GCC_except_table137
- GCC_except_table1379
- GCC_except_table138
- GCC_except_table1385
- GCC_except_table1387
- GCC_except_table1391
- GCC_except_table14
- GCC_except_table1410
- GCC_except_table151
- GCC_except_table154
- GCC_except_table155
- GCC_except_table158
- GCC_except_table1588
- GCC_except_table1589
- GCC_except_table1593
- GCC_except_table1594
- GCC_except_table1595
- GCC_except_table1597
- GCC_except_table1598
- GCC_except_table1599
- GCC_except_table1600
- GCC_except_table1601
- GCC_except_table1602
- GCC_except_table1603
- GCC_except_table1604
- GCC_except_table1605
- GCC_except_table1606
- GCC_except_table1607
- GCC_except_table1608
- GCC_except_table1609
- GCC_except_table161
- GCC_except_table1610
- GCC_except_table1613
- GCC_except_table1615
- GCC_except_table162
- GCC_except_table1620
- GCC_except_table1624
- GCC_except_table1627
- GCC_except_table1666
- GCC_except_table1691
- GCC_except_table1734
- GCC_except_table1742
- GCC_except_table1743
- GCC_except_table1744
- GCC_except_table1748
- GCC_except_table1760
- GCC_except_table1763
- GCC_except_table1770
- GCC_except_table1778
- GCC_except_table1784
- GCC_except_table1785
- GCC_except_table1791
- GCC_except_table1792
- GCC_except_table1793
- GCC_except_table1798
- GCC_except_table1801
- GCC_except_table1839
- GCC_except_table1841
- GCC_except_table1844
- GCC_except_table1846
- GCC_except_table1901
- GCC_except_table1905
- GCC_except_table1907
- GCC_except_table195
- GCC_except_table1956
- GCC_except_table1979
- GCC_except_table20
- GCC_except_table2173
- GCC_except_table2177
- GCC_except_table2179
- GCC_except_table2183
- GCC_except_table2188
- GCC_except_table2272
- GCC_except_table2273
- GCC_except_table2274
- GCC_except_table2275
- GCC_except_table2276
- GCC_except_table2277
- GCC_except_table2283
- GCC_except_table2288
- GCC_except_table253
- GCC_except_table287
- GCC_except_table307
- GCC_except_table318
- GCC_except_table322
- GCC_except_table326
- GCC_except_table330
- GCC_except_table339
- GCC_except_table35
- GCC_except_table356
- GCC_except_table358
- GCC_except_table362
- GCC_except_table439
- GCC_except_table441
- GCC_except_table455
- GCC_except_table457
- GCC_except_table458
- GCC_except_table461
- GCC_except_table484
- GCC_except_table524
- GCC_except_table544
- GCC_except_table547
- GCC_except_table551
- GCC_except_table553
- GCC_except_table592
- GCC_except_table595
- GCC_except_table606
- GCC_except_table608
- GCC_except_table612
- GCC_except_table614
- GCC_except_table618
- GCC_except_table620
- GCC_except_table622
- GCC_except_table655
- GCC_except_table658
- GCC_except_table659
- GCC_except_table685
- GCC_except_table690
- GCC_except_table694
- GCC_except_table702
- GCC_except_table705
- GCC_except_table813
- GCC_except_table86
- GCC_except_table884
- GCC_except_table889
- GCC_except_table946
- GCC_except_table950
- GCC_except_table953
- GCC_except_table954
- GCC_except_table966
- GCC_except_table98
- _OBJC_CLASS_$_CLSFaceIdentificationOnDemand
- _OBJC_CLASS_$_VCPMediaAnalysisService
- _OBJC_METACLASS_$_CLSFaceIdentificationOnDemand
- __OBJC_$_INSTANCE_METHODS_CLSFaceIdentificationOnDemand
- __OBJC_CLASS_PROTOCOLS_$_CLSFaceIdentificationOnDemand
- __OBJC_CLASS_RO_$_CLSFaceIdentificationOnDemand
- __OBJC_METACLASS_RO_$_CLSFaceIdentificationOnDemand
- __PROTOCOLS_CLSPublicEventGeoServiceClient.2
- __PROTOCOLS_CLSPublicEventShazamQueryHelper.12
- __PROTOCOLS_CLSPublicEventShazamServiceClient.2
- ___116-[CLSPublicEventCacheCreator _queryEventsForTimeLocationTuples:invalidationTokens:queryContext:progressBlock:error:]_block_invoke
- ___116-[CLSPublicEventCacheCreator _queryEventsForTimeLocationTuples:invalidationTokens:queryContext:progressBlock:error:]_block_invoke_2
- ___116-[CLSPublicEventCacheCreator _queryEventsForTimeLocationTuples:invalidationTokens:queryContext:progressBlock:error:]_block_invoke_3
- ___45-[CLSQueueBasedGeoMapQueryHelper _startQuery]_block_invoke.10
- ___68-[CLSFaceIdentificationOnDemand requestIdentificationOfFaces:error:]_block_invoke
- ___98-[CLSPublicEventCacheCreator createCacheForTimeLocationTuples:cachingOptions:progressBlock:error:]_block_invoke.69
- ___Block_byref_object_copy_.1204
- ___Block_byref_object_copy_.3326
- ___Block_byref_object_copy_.3725
- ___Block_byref_object_copy_.4195
- ___Block_byref_object_copy_.5473
- ___Block_byref_object_copy_.6108
- ___Block_byref_object_copy_.62
- ___Block_byref_object_copy_.678
- ___Block_byref_object_copy_.7075
- ___Block_byref_object_copy_.780
- ___Block_byref_object_copy_.870
- ___Block_byref_object_copy_.985
- ___Block_byref_object_dispose_.1205
- ___Block_byref_object_dispose_.3327
- ___Block_byref_object_dispose_.3726
- ___Block_byref_object_dispose_.4196
- ___Block_byref_object_dispose_.5474
- ___Block_byref_object_dispose_.6109
- ___Block_byref_object_dispose_.63
- ___Block_byref_object_dispose_.679
- ___Block_byref_object_dispose_.7076
- ___Block_byref_object_dispose_.781
- ___Block_byref_object_dispose_.871
- ___Block_byref_object_dispose_.986
- ___block_descriptor_144_e8_32s40s48s56s64s72bs80bs88r96r104r112r120r128r_e5_v8?0lr88l8s32l8s40l8s48l8s72l8s56l8s64l8r96l8r104l8r112l8s80l8r120l8r128l8
- ___block_descriptor_56_e8_32s40r48r_e34_v24?0"NSDictionary"8"NSError"16lr40l8r48l8s32l8
- ___block_descriptor_72_e8_32bs40r48r56r64r_e54_v28?0B8"NSError"12"<CLSPublicEventQueryProtocol>"20lr40l8r48l8r56l8r64l8s32l8
- ___block_literal_global.1013
- ___block_literal_global.1083
- ___block_literal_global.1323
- ___block_literal_global.137
- ___block_literal_global.1546
- ___block_literal_global.1859
- ___block_literal_global.1996
- ___block_literal_global.2040
- ___block_literal_global.2341
- ___block_literal_global.278
- ___block_literal_global.2919
- ___block_literal_global.3367
- ___block_literal_global.3722
- ___block_literal_global.4222
- ___block_literal_global.4929
- ___block_literal_global.5527
- ___block_literal_global.5626
- ___block_literal_global.569
- ___block_literal_global.5896
- ___block_literal_global.6232
- ___block_literal_global.7481
- ___block_literal_global.7547
- ___block_literal_global.78
- ___block_literal_global.867
- ___block_literal_global.989
- _kCLSHolidayCalendarEventRuleLastWeekdayOrdinal
- _objc_msgSend$_dateRuleForYear:countryCode:
- _objc_msgSend$_dateRuleForYear:supportedLocale:
- _objc_msgSend$_queryEventsForTimeLocationTuples:invalidationTokens:queryContext:progressBlock:error:
- _objc_msgSend$analysisService
- _objc_msgSend$cancelRequest:
- _objc_msgSend$dateForRuleWithUUID:byEvaluatingForYear:
- _objc_msgSend$initWithCache:queryRadius:
- _objc_msgSend$localDateByEvaluatingRuleForYear:
- _objc_msgSend$localDateByEvaluatingRuleForYear:countryCode:
- _objc_msgSend$pl_analysisErrorWithCode:
- _objc_msgSend$requestIdentificationOfFaces:withCompletionHandler:
- _objectdestroy.25Tm
- _objectdestroy.29Tm
- _sCLSDateHelperGMTTimeZone.4922
- _symbolic _____So7NSErrorCSg______pSgIeyBhyyy_ 10ObjectiveC8ObjCBoolV So27CLSPublicEventQueryProtocolP
CStrings:
+ "@\"CPAnalytics\""
+ "@\"NSDate\"32@0:8@\"NSString\"16@\"NSDate\"24"
+ "@40@0:8Q16@24@32"
+ "@40@0:8q16@24@32"
+ "@64@0:8@16o^@24@32@40@?48^@56"
+ "Already found cached version %@ for source service %lld"
+ "An error occured saving to the database: \"%@\""
+ "B24@0:8^@16"
+ "B40@0:8@16q24^@32"
+ "B40@0:8^@16q24^@32"
+ "CLSManagedPublicEventServerVersion"
+ "CLSPublicEventServerVersion"
+ "Fetched new Shazam server version %s, server updated %s"
+ "Geo static version"
+ "No cached version found on which to set invalidation date"
+ "PublicEventQueryFactory - creating PublicEventGeoServiceClient"
+ "PublicEventQueryFactory - creating PublicEventShazamServiceClient"
+ "PublicEventServerVersion"
+ "Sent %@ with payload: %@"
+ "T@\"NSDate\",R,N,V_dateOfServerUpdate"
+ "T@\"NSDateComponents\",R,C,N,V_leapYearOverrideComponents"
+ "T@\"NSString\",R,C,N,V_calendarIdentifier"
+ "T@\"NSString\",R,N,V_versionString"
+ "Tq,N,V_endEra"
+ "Tq,N,V_jobContext"
+ "Tq,N,V_startEra"
+ "Traits succeeded %@ : location %@ (given %lu, needed %lu), people %@ (given %lu, needed %lu), minimumPeopleCount %@ (given %lu, needed %lu), mustContainMe %@ (given %d, needed %d)"
+ "Unsupported calendar identifier for SPI: %@"
+ "_analytics"
+ "_calendarForIdentifier:"
+ "_dateComponentsFromRuleDescription:"
+ "_dateOfServerUpdate"
+ "_dateRuleForDate:countryCode:"
+ "_dateRuleForDate:supportedLocale:"
+ "_endEra"
+ "_enumerateDatesFromStartDate:toEndDate:supportedLocale:usingBlock:"
+ "_estimateBestEventDateComponentsToMatchDate:"
+ "_fetchRequestForLatestServerVersionForEventSourceService:"
+ "_jobContext"
+ "_leapYearOverrideComponents"
+ "_queryEventsForTimeLocationTuples:invalidationTokens:queryContext:analyticsPayload:progressBlock:error:"
+ "_saveWithError:"
+ "_startEra"
+ "_versionString"
+ "batchSize"
+ "batchSucceeded"
+ "com.apple.photos.publicEvents.fetching"
+ "components:fromDate:withCalendarIdentifier:"
+ "countOfWeekday:inMonthOfDate:withCalendarIdentifier:"
+ "dateByAddingDays:toDate:withCalendarIdentifier:"
+ "dateByAddingYears:toDate:withCalendarIdentifier:"
+ "dateForRuleWithUUID:byEvaluatingForDate:"
+ "dateFromComponents:inTimeZone:withCalendarIdentifier:"
+ "dateOfLastCachedVersion"
+ "dateOfScheduledCacheInvalidationForVersion"
+ "dateOfServerUpdate"
+ "didRequestTimeout"
+ "endEra"
+ "enumerateDatesFromStartDate:toEndDate:countryCode:usingBlock:"
+ "enumerateDatesFromStartDate:toEndDate:usingBlock:"
+ "getCachedServiceVersion does not accept NULL version"
+ "getCachedServiceVersion:forEventSourceService:error:"
+ "getScheduledCacheInvalidationDate does not accept NULL date"
+ "getScheduledCacheInvalidationDate:forEventSourceService:error:"
+ "hasEndEra"
+ "hasExplicitEra"
+ "hasStartEra"
+ "initWithCache:queryRadius:analytics:"
+ "initWithDictionary:"
+ "initWithURL:analytics:"
+ "initWithVersionString:dateOfServerUpdate:"
+ "isLeapYearForDate:withCalendarIdentifier:"
+ "jobContext"
+ "leapYearOverride"
+ "leapYearOverrideComponents"
+ "localDateByEvaluatingRuleForDate:"
+ "localDateByEvaluatingRuleForDate:countryCode:"
+ "localDateByEvaluatingRuleForDate:languageCode:"
+ "matchesExplicitEra:"
+ "monthFromDate:withCalendarIdentifier:"
+ "now"
+ "numberOfTuples"
+ "numberWithLongLong:"
+ "q40@0:8q16@24@32"
+ "rangeOfUnit:inUnit:forDate:withCalendarIdentifier:"
+ "requestContext"
+ "requestCurrentServiceVersionWithCompletionBlock:"
+ "requestDuration"
+ "requestTimeoutValue"
+ "serverVersionWithCompletionBlock:"
+ "setDateOfLastCachedVersion:"
+ "setDateOfScheduledCacheInvalidationForVersion:"
+ "setDateOfServerUpdate:"
+ "setEndEra:"
+ "setEra:"
+ "setJobContext:"
+ "setLatestVersionScheduledInvalidationDate:forEventSourceService:error:"
+ "setNewCachedServiceVersion:forEventSourceService:error:"
+ "setStartEra:"
+ "setVersion:"
+ "startEra"
+ "stringFromDate:"
+ "v24@0:8@?<v@?@\"CLSPublicEventServerVersion\"@\"NSError\">16"
+ "v32@0:8@?<v@?^B>16@?<v@?B@\"NSError\"@\"<CLSPublicEventQueryProtocol>\"@\"NSDictionary\">24"
+ "v36@?0B8@\"NSError\"12@\"<CLSPublicEventQueryProtocol>\"20@\"NSDictionary\"28"
+ "versionString"
+ "yearFromDate:withCalendarIdentifier:"
+ "{_NSRange=QQ}48@0:8Q16Q24@32@40"
- "@\"NSDate\"32@0:8@\"NSString\"16q24"
- "@32@0:8@16q24"
- "@56@0:8@16o^@24@32@?40^@48"
- "An error occured saving parent context to the database: \"%@\""
- "CLSFaceIdentificationOnDemand"
- "CLSPublicEventServiceFactory - creating PublicEventGeoServiceClient"
- "CLSPublicEventServiceFactory - creating PublicEventShazamServiceClient"
- "Traits failed: location %d (given %lu, needed %lu), people %d (given %lu, needed %lu), minimumPeopleCount %d (given %lu, needed %lu), mustContainMe %d (given %d, needed %d)"
- "[CLSMediaAnalysisHelper] -requestIdentificationOfFaces:withCompletionHandler: returned error: %@"
- "_dateRuleForYear:countryCode:"
- "_dateRuleForYear:supportedLocale:"
- "_queryEventsForTimeLocationTuples:invalidationTokens:queryContext:progressBlock:error:"
- "analysisService"
- "cancelRequest:"
- "dateForRuleWithUUID:byEvaluatingForYear:"
- "localDateByEvaluatingRuleForYear:"
- "localDateByEvaluatingRuleForYear:countryCode:"
- "localDateByEvaluatingRuleForYear:languageCode:"
- "pl_analysisErrorWithCode:"
- "requestIdentificationOfFaces:withCompletionHandler:"
- "v24@?0@\"NSDictionary\"8@\"NSError\"16"
- "v32@0:8@?<v@?^B>16@?<v@?B@\"NSError\"@\"<CLSPublicEventQueryProtocol>\">24"
- "{_NSRange=QQ}40@0:8Q16Q24@32"

```
