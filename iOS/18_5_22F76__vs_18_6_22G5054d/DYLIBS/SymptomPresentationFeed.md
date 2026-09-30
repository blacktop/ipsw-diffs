## SymptomPresentationFeed

> `/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomPresentationFeed.framework/SymptomPresentationFeed`

```diff

-2022.120.2.0.0
-  __TEXT.__text: 0x206c8
+2022.140.3.0.0
+  __TEXT.__text: 0x207cc
   __TEXT.__auth_stubs: 0x4a0
   __TEXT.__objc_methlist: 0x894
-  __TEXT.__cstring: 0x1503
-  __TEXT.__const: 0x100
+  __TEXT.__cstring: 0x153f
+  __TEXT.__const: 0xe8
   __TEXT.__gcc_except_tab: 0x69c
-  __TEXT.__oslogstring: 0x25b9
-  __TEXT.__unwind_info: 0x480
+  __TEXT.__oslogstring: 0x25e3
+  __TEXT.__unwind_info: 0x488
   __TEXT.__objc_classname: 0xdb
-  __TEXT.__objc_methname: 0x27ca
+  __TEXT.__objc_methname: 0x27dd
   __TEXT.__objc_methtype: 0xb7f
-  __TEXT.__objc_stubs: 0x1bc0
-  __DATA_CONST.__got: 0x3d0
+  __TEXT.__objc_stubs: 0x1be0
+  __DATA_CONST.__got: 0x3d8
   __DATA_CONST.__const: 0x10a8
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x980
+  __DATA_CONST.__objc_selrefs: 0x988
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x50
   __AUTH_CONST.__auth_got: 0x260
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x2100
+  __AUTH_CONST.__cfstring: 0x2140
   __AUTH_CONST.__objc_const: 0xbc0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x30

   - /System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomAnalytics.framework/SymptomAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 02193252-A401-38F3-A616-751EF136C79F
+  UUID: BA22693A-5872-360A-B505-B3602167957B
   Functions: 307
-  Symbols:   1371
-  CStrings:  1195
+  Symbols:   1373
+  CStrings:  1201
 
Symbols:
+ _OBJC_CLASS_$_NSUserDefaults
+ ___100-[UsageFeed(NetworkDomains) _networkDomainsQueryViewTypeApp:entityName:limit:actions:callbackBlock:]_block_invoke.623
+ ___108-[UsageFeed(NetworkDomains) networkDomainsToDateWithOptionsFor:nameKind:domainType:startTime:options:reply:]_block_invoke.587
+ ___123-[UsageFeed(NetworkDomains) _legacyNetworkDomainsQueryOnService:entityName:pred:limit:actions:options:postProcessingBlock:]_block_invoke.691
+ ___123-[UsageFeed(NetworkDomains) _legacyNetworkDomainsQueryOnService:entityName:pred:limit:actions:options:postProcessingBlock:]_block_invoke.693
+ ___123-[UsageFeed(NetworkDomains) _legacyNetworkDomainsQueryOnService:entityName:pred:limit:actions:options:postProcessingBlock:]_block_invoke.695
+ ___124-[UsageFeed(NetworkDomains) networkDomainsToDateWithOptionsFor:nameKind:domainType:startTime:options:fetchProperties:reply:]_block_invoke.580
+ ___124-[UsageFeed(NetworkDomains) networkDomainsToDateWithOptionsFor:nameKind:domainType:startTime:options:fetchProperties:reply:]_block_invoke.583
+ ___124-[UsageFeed(NetworkDomains) networkDomainsToDateWithOptionsFor:nameKind:domainType:startTime:options:fetchProperties:reply:]_block_invoke.584
+ ___164-[UsageFeed(NetworkDomains) _performNetDomainsQueryOnService:entityName:fetchProps:pred:sort:actions:queryTimer:replyProcessBlock:accumulatedResults:callbackBlock:]_block_invoke.576
+ ___237-[UsageFeed(NetworkDomains) __networkDomainsQueryDomains:entityName:unnamedDomainsOption:limit:actions:accumulatedResults:aggregateProperty:predicate:altAggregateProperty:altPredicate:ipAggregateProperty:replyProcessBlock:callbackBlock:]_block_invoke.651
+ ___237-[UsageFeed(NetworkDomains) __networkDomainsQueryDomains:entityName:unnamedDomainsOption:limit:actions:accumulatedResults:aggregateProperty:predicate:altAggregateProperty:altPredicate:ipAggregateProperty:replyProcessBlock:callbackBlock:]_block_invoke.654
+ ___237-[UsageFeed(NetworkDomains) __networkDomainsQueryDomains:entityName:unnamedDomainsOption:limit:actions:accumulatedResults:aggregateProperty:predicate:altAggregateProperty:altPredicate:ipAggregateProperty:replyProcessBlock:callbackBlock:]_block_invoke_2.652
+ ___34-[UsageFeed getUsageOption:reply:]_block_invoke.494
+ ___34-[UsageFeed setUsageOption:reply:]_block_invoke.493
+ ___37-[UsageFeed identifierForUUID:reply:]_block_invoke.497
+ ___46-[UsageFeed resetUsageDataFor:nameKind:reply:]_block_invoke.495
+ ___57-[UsageFeed typicalUsageFor:nameKind:intervalKind:reply:]_block_invoke.470
+ ___60-[UsageFeed(NetworkDomains) getNetworkDomainsOptions:reply:]_block_invoke.703
+ ___60-[UsageFeed(NetworkDomains) setNetworkDomainsOptions:reply:]_block_invoke.702
+ ___62-[UsageFeed usageToDateWithOptionsFor:nameKind:options:reply:]_block_invoke.408
+ ___62-[UsageFeed usageToDateWithOptionsFor:nameKind:options:reply:]_block_invoke.443
+ ___62-[UsageFeed usageToDateWithOptionsFor:nameKind:options:reply:]_block_invoke.446
+ ___62-[UsageFeed usageToDateWithOptionsFor:nameKind:options:reply:]_block_invoke.449
+ ___62-[UsageFeed usageToDateWithOptionsFor:nameKind:options:reply:]_block_invoke_2.451
+ ___74-[UsageFeed(NetworkDomains) performNetworkDomainsActionWithOptions:reply:]_block_invoke.704
+ ___76-[UsageFeed calendarUsageFor:nameKind:dayResolution:daySlot:weekSlot:reply:]_block_invoke.482
+ ___76-[UsageFeed calendarUsageFor:nameKind:dayResolution:daySlot:weekSlot:reply:]_block_invoke.486
+ ___76-[UsageFeed calendarUsageFor:nameKind:dayResolution:daySlot:weekSlot:reply:]_block_invoke.490
+ ___77-[UsageFeed algosScoreToDateWithOptionsFor:nameKind:startTime:options:reply:]_block_invoke.492
+ ___80-[UsageFeed networkBitmapsToDateWithOptionsFor:startTime:endTime:options:reply:]_block_invoke.406
+ ___Block_byref_object_copy_.577
+ ___Block_byref_object_dispose_.578
+ ___block_literal_global.590
+ ___block_literal_global.596
+ ___block_literal_global.605
+ _objc_msgSend$initWithSuiteName:
- ___100-[UsageFeed(NetworkDomains) _networkDomainsQueryViewTypeApp:entityName:limit:actions:callbackBlock:]_block_invoke.616
- ___108-[UsageFeed(NetworkDomains) networkDomainsToDateWithOptionsFor:nameKind:domainType:startTime:options:reply:]_block_invoke.580
- ___123-[UsageFeed(NetworkDomains) _legacyNetworkDomainsQueryOnService:entityName:pred:limit:actions:options:postProcessingBlock:]_block_invoke.684
- ___123-[UsageFeed(NetworkDomains) _legacyNetworkDomainsQueryOnService:entityName:pred:limit:actions:options:postProcessingBlock:]_block_invoke.686
- ___123-[UsageFeed(NetworkDomains) _legacyNetworkDomainsQueryOnService:entityName:pred:limit:actions:options:postProcessingBlock:]_block_invoke.688
- ___124-[UsageFeed(NetworkDomains) networkDomainsToDateWithOptionsFor:nameKind:domainType:startTime:options:fetchProperties:reply:]_block_invoke.573
- ___124-[UsageFeed(NetworkDomains) networkDomainsToDateWithOptionsFor:nameKind:domainType:startTime:options:fetchProperties:reply:]_block_invoke.576
- ___124-[UsageFeed(NetworkDomains) networkDomainsToDateWithOptionsFor:nameKind:domainType:startTime:options:fetchProperties:reply:]_block_invoke.577
- ___164-[UsageFeed(NetworkDomains) _performNetDomainsQueryOnService:entityName:fetchProps:pred:sort:actions:queryTimer:replyProcessBlock:accumulatedResults:callbackBlock:]_block_invoke.569
- ___237-[UsageFeed(NetworkDomains) __networkDomainsQueryDomains:entityName:unnamedDomainsOption:limit:actions:accumulatedResults:aggregateProperty:predicate:altAggregateProperty:altPredicate:ipAggregateProperty:replyProcessBlock:callbackBlock:]_block_invoke.644
- ___237-[UsageFeed(NetworkDomains) __networkDomainsQueryDomains:entityName:unnamedDomainsOption:limit:actions:accumulatedResults:aggregateProperty:predicate:altAggregateProperty:altPredicate:ipAggregateProperty:replyProcessBlock:callbackBlock:]_block_invoke.647
- ___237-[UsageFeed(NetworkDomains) __networkDomainsQueryDomains:entityName:unnamedDomainsOption:limit:actions:accumulatedResults:aggregateProperty:predicate:altAggregateProperty:altPredicate:ipAggregateProperty:replyProcessBlock:callbackBlock:]_block_invoke_2.645
- ___34-[UsageFeed getUsageOption:reply:]_block_invoke.487
- ___34-[UsageFeed setUsageOption:reply:]_block_invoke.486
- ___37-[UsageFeed identifierForUUID:reply:]_block_invoke.490
- ___46-[UsageFeed resetUsageDataFor:nameKind:reply:]_block_invoke.488
- ___57-[UsageFeed typicalUsageFor:nameKind:intervalKind:reply:]_block_invoke.463
- ___60-[UsageFeed(NetworkDomains) getNetworkDomainsOptions:reply:]_block_invoke.696
- ___60-[UsageFeed(NetworkDomains) setNetworkDomainsOptions:reply:]_block_invoke.695
- ___62-[UsageFeed usageToDateWithOptionsFor:nameKind:options:reply:]_block_invoke.401
- ___62-[UsageFeed usageToDateWithOptionsFor:nameKind:options:reply:]_block_invoke.436
- ___62-[UsageFeed usageToDateWithOptionsFor:nameKind:options:reply:]_block_invoke.439
- ___62-[UsageFeed usageToDateWithOptionsFor:nameKind:options:reply:]_block_invoke.442
- ___62-[UsageFeed usageToDateWithOptionsFor:nameKind:options:reply:]_block_invoke_2.444
- ___74-[UsageFeed(NetworkDomains) performNetworkDomainsActionWithOptions:reply:]_block_invoke.697
- ___76-[UsageFeed calendarUsageFor:nameKind:dayResolution:daySlot:weekSlot:reply:]_block_invoke.475
- ___76-[UsageFeed calendarUsageFor:nameKind:dayResolution:daySlot:weekSlot:reply:]_block_invoke.479
- ___76-[UsageFeed calendarUsageFor:nameKind:dayResolution:daySlot:weekSlot:reply:]_block_invoke.483
- ___77-[UsageFeed algosScoreToDateWithOptionsFor:nameKind:startTime:options:reply:]_block_invoke.485
- ___80-[UsageFeed networkBitmapsToDateWithOptionsFor:startTime:endTime:options:reply:]_block_invoke.399
- ___Block_byref_object_copy_.570
- ___Block_byref_object_dispose_.571
- ___block_literal_global.583
- ___block_literal_global.589
- ___block_literal_global.598
CStrings:
+ "++ Overriding database fetch limit to %ld"
+ "com.apple.symptomframework.usagefeed"
+ "db_records_fetch_limit"
+ "initWithSuiteName:"

```
