## PerfPowerServicesReader

> `/System/Library/PrivateFrameworks/PerfPowerServicesReader.framework/PerfPowerServicesReader`

```diff

-2954.0.0.502.3
-  __TEXT.__text: 0x12d844
+2964.0.40.502.1
+  __TEXT.__text: 0x131120
   __TEXT.__auth_stubs: 0xf20
   __TEXT.__init_offsets: 0xdc
-  __TEXT.__objc_methlist: 0x12354
+  __TEXT.__objc_methlist: 0x127bc
   __TEXT.__const: 0x605e
-  __TEXT.__cstring: 0xbf92
-  __TEXT.__gcc_except_tab: 0x4984
-  __TEXT.__oslogstring: 0xc21
-  __TEXT.__unwind_info: 0x4658
+  __TEXT.__cstring: 0xc004
+  __TEXT.__gcc_except_tab: 0x4a1c
+  __TEXT.__oslogstring: 0xc92
+  __TEXT.__unwind_info: 0x4710
   __TEXT.__eh_frame: 0x98
-  __TEXT.__objc_classname: 0x18d8
-  __TEXT.__objc_methname: 0x191e0
-  __TEXT.__objc_methtype: 0x2723
-  __TEXT.__objc_stubs: 0x9540
-  __DATA_CONST.__got: 0xa60
-  __DATA_CONST.__const: 0x2840
-  __DATA_CONST.__objc_classlist: 0x530
+  __TEXT.__objc_classname: 0x1963
+  __TEXT.__objc_methname: 0x194a3
+  __TEXT.__objc_methtype: 0x2748
+  __TEXT.__objc_stubs: 0x96e0
+  __DATA_CONST.__got: 0xa78
+  __DATA_CONST.__const: 0x2890
+  __DATA_CONST.__objc_classlist: 0x548
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x48
+  __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5c98
+  __DATA_CONST.__objc_selrefs: 0x5d38
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x4a8
+  __DATA_CONST.__objc_superrefs: 0x4c0
   __DATA_CONST.__objc_arraydata: 0x110
   __AUTH_CONST.__auth_got: 0x7a8
   __AUTH_CONST.__const: 0x3090
-  __AUTH_CONST.__cfstring: 0xdba0
-  __AUTH_CONST.__objc_const: 0x16010
+  __AUTH_CONST.__cfstring: 0xdc60
+  __AUTH_CONST.__objc_const: 0x165a8
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x28a0
+  __AUTH.__objc_data: 0x2990
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x1074
-  __DATA.__data: 0x521
-  __DATA.__bss: 0x38
+  __DATA.__objc_ivar: 0x10ac
+  __DATA.__data: 0x581
+  __DATA.__bss: 0x48
   __DATA_DIRTY.__objc_data: 0xb40
   __DATA_DIRTY.__data: 0xad8
   __DATA_DIRTY.__bss: 0xa0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 90419A2B-E702-34B6-A713-673987603897
-  Functions: 7630
-  Symbols:   20628
-  CStrings:  8098
+  UUID: 64063372-29DF-3B48-87E2-21517A820A90
+  Functions: 7725
+  Symbols:   20876
+  CStrings:  8143
 
Symbols:
+ +[AWDMETRICSKCellularPowerLogSFTRxTxHist binType]
+ +[AWDMETRICSMetricLogPower kCellularPowerLogSFTRxTxType]
+ +[AWDMETRICSMetricLogPower kCellularPowerLogSFTStateType]
+ +[PPSSQLiteTimeSeriesIngester cache:willEvictObject:]
+ +[PPSSQLiteTimeSeriesIngester cache:willEvictObject:].cold.1
+ +[PPSSQLiteTimeSeriesIngester cachedDatabaseForURL:]
+ +[PPSSQLiteTimeSeriesIngester databaseConnectionCache]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHist .cxx_destruct]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHist addBin:]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHist binAtIndex:]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHist binsCount]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHist bins]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHist clearBins]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHist copyTo:]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHist copyWithZone:]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHist description]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHist dictionaryRepresentation]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHist durationMs]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHist hasDurationMs]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHist hasSubsId]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHist hasTimestamp]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHist hash]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHist isEqual:]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHist mergeFrom:]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHist readFrom:]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHist setBins:]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHist setDurationMs:]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHist setHasDurationMs:]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHist setHasSubsId:]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHist setHasTimestamp:]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHist setSubsId:]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHist setTimestamp:]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHist subsId]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHist timestamp]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHist writeTo:]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHistMBin StringAsBinId:]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHistMBin binIdAsString:]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHistMBin binId]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHistMBin copyTo:]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHistMBin copyWithZone:]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHistMBin description]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHistMBin dictionaryRepresentation]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHistMBin duration]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHistMBin hasBinId]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHistMBin hasDuration]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHistMBin hash]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHistMBin isEqual:]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHistMBin mergeFrom:]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHistMBin readFrom:]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHistMBin setBinId:]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHistMBin setDuration:]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHistMBin setHasBinId:]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHistMBin setHasDuration:]
+ -[AWDMETRICSKCellularPowerLogSFTRxTxHistMBin writeTo:]
+ -[AWDMETRICSKCellularPowerLogSFTStateEvent StringAsEvent:]
+ -[AWDMETRICSKCellularPowerLogSFTStateEvent copyTo:]
+ -[AWDMETRICSKCellularPowerLogSFTStateEvent copyWithZone:]
+ -[AWDMETRICSKCellularPowerLogSFTStateEvent description]
+ -[AWDMETRICSKCellularPowerLogSFTStateEvent dictionaryRepresentation]
+ -[AWDMETRICSKCellularPowerLogSFTStateEvent eventAsString:]
+ -[AWDMETRICSKCellularPowerLogSFTStateEvent event]
+ -[AWDMETRICSKCellularPowerLogSFTStateEvent hasEvent]
+ -[AWDMETRICSKCellularPowerLogSFTStateEvent hasSubsId]
+ -[AWDMETRICSKCellularPowerLogSFTStateEvent hasTimestamp]
+ -[AWDMETRICSKCellularPowerLogSFTStateEvent hash]
+ -[AWDMETRICSKCellularPowerLogSFTStateEvent isEqual:]
+ -[AWDMETRICSKCellularPowerLogSFTStateEvent mergeFrom:]
+ -[AWDMETRICSKCellularPowerLogSFTStateEvent readFrom:]
+ -[AWDMETRICSKCellularPowerLogSFTStateEvent setEvent:]
+ -[AWDMETRICSKCellularPowerLogSFTStateEvent setHasEvent:]
+ -[AWDMETRICSKCellularPowerLogSFTStateEvent setHasSubsId:]
+ -[AWDMETRICSKCellularPowerLogSFTStateEvent setHasTimestamp:]
+ -[AWDMETRICSKCellularPowerLogSFTStateEvent setSubsId:]
+ -[AWDMETRICSKCellularPowerLogSFTStateEvent setTimestamp:]
+ -[AWDMETRICSKCellularPowerLogSFTStateEvent subsId]
+ -[AWDMETRICSKCellularPowerLogSFTStateEvent timestamp]
+ -[AWDMETRICSKCellularPowerLogSFTStateEvent writeTo:]
+ -[AWDMETRICSMetricLogPower addKCellularPowerLogSFTRxTx:]
+ -[AWDMETRICSMetricLogPower addKCellularPowerLogSFTState:]
+ -[AWDMETRICSMetricLogPower clearKCellularPowerLogSFTRxTxs]
+ -[AWDMETRICSMetricLogPower clearKCellularPowerLogSFTStates]
+ -[AWDMETRICSMetricLogPower kCellularPowerLogSFTRxTxAtIndex:]
+ -[AWDMETRICSMetricLogPower kCellularPowerLogSFTRxTxsCount]
+ -[AWDMETRICSMetricLogPower kCellularPowerLogSFTRxTxs]
+ -[AWDMETRICSMetricLogPower kCellularPowerLogSFTStateAtIndex:]
+ -[AWDMETRICSMetricLogPower kCellularPowerLogSFTStatesCount]
+ -[AWDMETRICSMetricLogPower kCellularPowerLogSFTStates]
+ -[AWDMETRICSMetricLogPower setKCellularPowerLogSFTRxTxs:]
+ -[AWDMETRICSMetricLogPower setKCellularPowerLogSFTStates:]
+ -[PPSSQLiteTimeSeriesIngester dealloc]
+ -[PPSSQLiteTimeSeriesIngester dealloc].cold.1
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogSFTRxTxHist._bins
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogSFTRxTxHist._durationMs
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogSFTRxTxHist._has
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogSFTRxTxHist._subsId
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogSFTRxTxHist._timestamp
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogSFTRxTxHistMBin._binId
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogSFTRxTxHistMBin._duration
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogSFTRxTxHistMBin._has
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogSFTStateEvent._event
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogSFTStateEvent._has
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogSFTStateEvent._subsId
+ OBJC_IVAR_$_AWDMETRICSKCellularPowerLogSFTStateEvent._timestamp
+ OBJC_IVAR_$_AWDMETRICSMetricLogPower._kCellularPowerLogSFTRxTxs
+ OBJC_IVAR_$_AWDMETRICSMetricLogPower._kCellularPowerLogSFTStates
+ _AWDMETRICSKCellularPowerLogSFTRxTxHistMBinReadFrom
+ _AWDMETRICSKCellularPowerLogSFTRxTxHistReadFrom
+ _AWDMETRICSKCellularPowerLogSFTStateEventReadFrom
+ _OBJC_CLASS_$_AWDMETRICSKCellularPowerLogSFTRxTxHist
+ _OBJC_CLASS_$_AWDMETRICSKCellularPowerLogSFTRxTxHistMBin
+ _OBJC_CLASS_$_AWDMETRICSKCellularPowerLogSFTStateEvent
+ _OBJC_METACLASS_$_AWDMETRICSKCellularPowerLogSFTRxTxHist
+ _OBJC_METACLASS_$_AWDMETRICSKCellularPowerLogSFTRxTxHistMBin
+ _OBJC_METACLASS_$_AWDMETRICSKCellularPowerLogSFTStateEvent
+ __OBJC_$_CLASS_METHODS_AWDMETRICSKCellularPowerLogSFTRxTxHist
+ __OBJC_$_CLASS_PROP_LIST_PPSSQLiteTimeSeriesIngester
+ __OBJC_$_INSTANCE_METHODS_AWDMETRICSKCellularPowerLogSFTRxTxHist
+ __OBJC_$_INSTANCE_METHODS_AWDMETRICSKCellularPowerLogSFTRxTxHistMBin
+ __OBJC_$_INSTANCE_METHODS_AWDMETRICSKCellularPowerLogSFTStateEvent
+ __OBJC_$_INSTANCE_VARIABLES_AWDMETRICSKCellularPowerLogSFTRxTxHist
+ __OBJC_$_INSTANCE_VARIABLES_AWDMETRICSKCellularPowerLogSFTRxTxHistMBin
+ __OBJC_$_INSTANCE_VARIABLES_AWDMETRICSKCellularPowerLogSFTStateEvent
+ __OBJC_$_PROP_LIST_AWDMETRICSKCellularPowerLogSFTRxTxHist
+ __OBJC_$_PROP_LIST_AWDMETRICSKCellularPowerLogSFTRxTxHistMBin
+ __OBJC_$_PROP_LIST_AWDMETRICSKCellularPowerLogSFTStateEvent
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSCacheDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCacheDelegate
+ __OBJC_$_PROTOCOL_REFS_NSCacheDelegate
+ __OBJC_CLASS_PROTOCOLS_$_AWDMETRICSKCellularPowerLogSFTRxTxHist
+ __OBJC_CLASS_PROTOCOLS_$_AWDMETRICSKCellularPowerLogSFTRxTxHistMBin
+ __OBJC_CLASS_PROTOCOLS_$_AWDMETRICSKCellularPowerLogSFTStateEvent
+ __OBJC_CLASS_RO_$_AWDMETRICSKCellularPowerLogSFTRxTxHist
+ __OBJC_CLASS_RO_$_AWDMETRICSKCellularPowerLogSFTRxTxHistMBin
+ __OBJC_CLASS_RO_$_AWDMETRICSKCellularPowerLogSFTStateEvent
+ __OBJC_LABEL_PROTOCOL_$_NSCacheDelegate
+ __OBJC_METACLASS_RO_$_AWDMETRICSKCellularPowerLogSFTRxTxHist
+ __OBJC_METACLASS_RO_$_AWDMETRICSKCellularPowerLogSFTRxTxHistMBin
+ __OBJC_METACLASS_RO_$_AWDMETRICSKCellularPowerLogSFTStateEvent
+ __OBJC_PROTOCOL_$_NSCacheDelegate
+ ___54+[PPSSQLiteTimeSeriesIngester databaseConnectionCache]_block_invoke
+ ___87-[PPSSQLiteTimeSeriesIngester _convertSQLiteDataFromQuery:withMetricDefinitions:error:]_block_invoke.48
+ ___87-[PPSSQLiteTimeSeriesIngester _convertSQLiteDataFromQuery:withMetricDefinitions:error:]_block_invoke.48.cold.1
+ _databaseConnectionCache.connectionCache
+ _databaseConnectionCache.onceToken
+ _objc_msgSend$addKCellularPowerLogSFTRxTx:
+ _objc_msgSend$addKCellularPowerLogSFTState:
+ _objc_msgSend$cachedDatabaseForURL:
+ _objc_msgSend$clearKCellularPowerLogSFTRxTxs
+ _objc_msgSend$clearKCellularPowerLogSFTStates
+ _objc_msgSend$databaseConnectionCache
+ _objc_msgSend$kCellularPowerLogSFTRxTxAtIndex:
+ _objc_msgSend$kCellularPowerLogSFTRxTxsCount
+ _objc_msgSend$kCellularPowerLogSFTStateAtIndex:
+ _objc_msgSend$kCellularPowerLogSFTStatesCount
+ _objc_msgSend$setDelegate:
+ _objc_msgSend$setName:
+ _objc_msgSend$setTotalCostLimit:
- ___87-[PPSSQLiteTimeSeriesIngester _convertSQLiteDataFromQuery:withMetricDefinitions:error:]_block_invoke.42
- ___87-[PPSSQLiteTimeSeriesIngester _convertSQLiteDataFromQuery:withMetricDefinitions:error:]_block_invoke.42.cold.1
CStrings:
+ "AWDMETRICSKCellularPowerLogSFTRxTxHist"
+ "AWDMETRICSKCellularPowerLogSFTRxTxHistMBin"
+ "AWDMETRICSKCellularPowerLogSFTStateEvent"
+ "Closed database connection due to cache eviction: %@"
+ "Closed database connection due to ingester deallocation: %@"
+ "NSCacheDelegate"
+ "RX"
+ "SCC8"
+ "T@\"NSCache\",R"
+ "T@\"NSMutableArray\",&,N,V_kCellularPowerLogSFTRxTxs"
+ "T@\"NSMutableArray\",&,N,V_kCellularPowerLogSFTStates"
+ "TX"
+ "_kCellularPowerLogSFTRxTxs"
+ "_kCellularPowerLogSFTStates"
+ "addKCellularPowerLogSFTRxTx:"
+ "addKCellularPowerLogSFTState:"
+ "cache:willEvictObject:"
+ "cachedDatabaseForURL:"
+ "clearKCellularPowerLogSFTRxTxs"
+ "clearKCellularPowerLogSFTStates"
+ "com.apple.perfpowerservices.databaseConnectionCache"
+ "databaseConnectionCache"
+ "kCellularPowerLogSFTRxTx"
+ "kCellularPowerLogSFTRxTxAtIndex:"
+ "kCellularPowerLogSFTRxTxType"
+ "kCellularPowerLogSFTRxTxs"
+ "kCellularPowerLogSFTRxTxsCount"
+ "kCellularPowerLogSFTState"
+ "kCellularPowerLogSFTStateAtIndex:"
+ "kCellularPowerLogSFTStateType"
+ "kCellularPowerLogSFTStates"
+ "kCellularPowerLogSFTStatesCount"
+ "setDelegate:"
+ "setKCellularPowerLogSFTRxTxs:"
+ "setKCellularPowerLogSFTStates:"
+ "setName:"
+ "setTotalCostLimit:"
+ "v32@0:8@\"NSCache\"16@24"
+ "v32@0:8@16@24"

```
