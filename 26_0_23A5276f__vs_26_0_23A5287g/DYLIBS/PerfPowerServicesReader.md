## PerfPowerServicesReader

> `/System/Library/PrivateFrameworks/PerfPowerServicesReader.framework/PerfPowerServicesReader`

```diff

-2964.0.40.502.1
-  __TEXT.__text: 0x131120
-  __TEXT.__auth_stubs: 0xf20
+2964.0.64.0.0
+  __TEXT.__text: 0x1317e0
+  __TEXT.__auth_stubs: 0xf30
   __TEXT.__init_offsets: 0xdc
-  __TEXT.__objc_methlist: 0x127bc
+  __TEXT.__objc_methlist: 0x127d4
   __TEXT.__const: 0x605e
-  __TEXT.__cstring: 0xc004
-  __TEXT.__gcc_except_tab: 0x4a1c
-  __TEXT.__oslogstring: 0xc92
-  __TEXT.__unwind_info: 0x4710
+  __TEXT.__cstring: 0xc05c
+  __TEXT.__gcc_except_tab: 0x4ad0
+  __TEXT.__oslogstring: 0xcf0
+  __TEXT.__unwind_info: 0x4738
   __TEXT.__eh_frame: 0x98
   __TEXT.__objc_classname: 0x1963
-  __TEXT.__objc_methname: 0x194a3
+  __TEXT.__objc_methname: 0x1950c
   __TEXT.__objc_methtype: 0x2748
-  __TEXT.__objc_stubs: 0x96e0
-  __DATA_CONST.__got: 0xa78
-  __DATA_CONST.__const: 0x2890
+  __TEXT.__objc_stubs: 0x9780
+  __DATA_CONST.__got: 0xa80
+  __DATA_CONST.__const: 0x28d8
   __DATA_CONST.__objc_classlist: 0x548
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5d38
+  __DATA_CONST.__objc_selrefs: 0x5d60
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x4c0
   __DATA_CONST.__objc_arraydata: 0x110
-  __AUTH_CONST.__auth_got: 0x7a8
-  __AUTH_CONST.__const: 0x3090
-  __AUTH_CONST.__cfstring: 0xdc60
+  __AUTH_CONST.__auth_got: 0x7b0
+  __AUTH_CONST.__const: 0x30d0
+  __AUTH_CONST.__cfstring: 0xdc80
   __AUTH_CONST.__objc_const: 0x165a8
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x78

   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x10ac
   __DATA.__data: 0x581
-  __DATA.__bss: 0x48
+  __DATA.__bss: 0x58
   __DATA_DIRTY.__objc_data: 0xb40
   __DATA_DIRTY.__data: 0xad8
   __DATA_DIRTY.__bss: 0xa0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 64063372-29DF-3B48-87E2-21517A820A90
-  Functions: 7725
-  Symbols:   20876
-  CStrings:  8143
+  UUID: 8D54FB58-26A7-33C1-873C-858765FAB4C9
+  Functions: 7736
+  Symbols:   20911
+  CStrings:  8154
 
Symbols:
+ +[PPSSQLiteTimeSeriesIngester databaseQueue]
+ +[PPSSQLiteTimeSeriesIngester databaseQueue].cold.1
+ +[PPSSQLiteTimeSeriesIngester evicttriggering]
+ +[PPSSQLiteTimeSeriesIngester evicttriggering].cold.1
+ _OBJC_CLASS_$_NSNotificationCenter
+ ___38-[PPSSQLiteTimeSeriesIngester dealloc]_block_invoke
+ ___38-[PPSSQLiteTimeSeriesIngester dealloc]_block_invoke.cold.1
+ ___44+[PPSSQLiteTimeSeriesIngester databaseQueue]_block_invoke
+ ___53+[PPSSQLiteTimeSeriesIngester cache:willEvictObject:]_block_invoke
+ ___53+[PPSSQLiteTimeSeriesIngester cache:willEvictObject:]_block_invoke.cold.1
+ ___54+[PPSSQLiteTimeSeriesIngester databaseConnectionCache]_block_invoke.7
+ ___54+[PPSSQLiteTimeSeriesIngester databaseConnectionCache]_block_invoke.cold.1
+ ___60-[PPSSQLiteTimeSeriesIngester parseDataForRequest:outError:]_block_invoke
+ ___60-[PPSSQLiteTimeSeriesIngester parseDataForRequest:outError:]_block_invoke.cold.1
+ ___87-[PPSSQLiteTimeSeriesIngester _convertSQLiteDataFromQuery:withMetricDefinitions:error:]_block_invoke.69
+ ___87-[PPSSQLiteTimeSeriesIngester _convertSQLiteDataFromQuery:withMetricDefinitions:error:]_block_invoke.69.cold.1
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80r88r96r_e5_v8?0ls32l8r80l8s40l8s48l8r88l8s56l8s64l8r96l8s72l8
+ ___block_descriptor_32_e24_v16?0"NSNotification"8l
+ ___block_literal_global.10
+ _databaseQueue.databaseQueue
+ _databaseQueue.onceToken
+ _dispatch_async
+ _objc_msgSend$addObserverForName:object:queue:usingBlock:
+ _objc_msgSend$cache:willEvictObject:
+ _objc_msgSend$databaseQueue
+ _objc_msgSend$defaultCenter
+ _objc_msgSend$evicttriggering
+ _objc_msgSend$fileURLWithPath:
- +[PPSSQLiteTimeSeriesIngester cache:willEvictObject:].cold.1
- -[PPSSQLiteTimeSeriesIngester dealloc].cold.1
- -[PPSSQLiteTimeSeriesIngester parseDataForRequest:outError:].cold.1
- ___87-[PPSSQLiteTimeSeriesIngester _convertSQLiteDataFromQuery:withMetricDefinitions:error:]_block_invoke.48
- ___87-[PPSSQLiteTimeSeriesIngester _convertSQLiteDataFromQuery:withMetricDefinitions:error:]_block_invoke.48.cold.1
- _objc_msgSend$cachedDatabaseForURL:
CStrings:
+ "EvictionNotification"
+ "[eviction] Evicting DB on-demand"
+ "[eviction] Subscribing to eviction notification DB on-demand"
+ "addObserverForName:object:queue:usingBlock:"
+ "com.apple.perfpowerservices.databaseQueue"
+ "databaseQueue"
+ "defaultCenter"
+ "evicttriggering"
+ "fileURLWithPath:"
+ "v16@?0@\"NSNotification\"8"

```
