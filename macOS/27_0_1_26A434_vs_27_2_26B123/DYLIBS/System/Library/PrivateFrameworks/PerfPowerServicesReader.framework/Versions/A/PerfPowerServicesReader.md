## PerfPowerServicesReader

> `/System/Library/PrivateFrameworks/PerfPowerServicesReader.framework/Versions/A/PerfPowerServicesReader`

```diff

-3486.1.2.0.0
-  __TEXT.__text: 0x15fcec
+3486.41.1.0.0
+  __TEXT.__text: 0x161704
   __TEXT.__init_offsets: 0xdc
-  __TEXT.__objc_methlist: 0x13994
-  __TEXT.__const: 0x5fda
-  __TEXT.__cstring: 0xe092
-  __TEXT.__gcc_except_tab: 0x4b10
-  __TEXT.__oslogstring: 0xda1
-  __TEXT.__unwind_info: 0x4ca0
+  __TEXT.__objc_methlist: 0x13a34
+  __TEXT.__const: 0x5fea
+  __TEXT.__cstring: 0xe1d0
+  __TEXT.__gcc_except_tab: 0x4c00
+  __TEXT.__oslogstring: 0xe59
+  __TEXT.__unwind_info: 0x4cd8
   __TEXT.__eh_frame: 0x98
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x368
-  __DATA_CONST.__objc_selrefs: 0x60a8
+  __DATA_CONST.__objc_selrefs: 0x6118
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x508
   __DATA_CONST.__objc_arraydata: 0x110
-  __DATA_CONST.__got: 0x758
-  __AUTH_CONST.__const: 0x36f0
-  __AUTH_CONST.__cfstring: 0x10b80
-  __AUTH_CONST.__objc_const: 0x179e0
+  __DATA_CONST.__got: 0x760
+  __AUTH_CONST.__const: 0x3750
+  __AUTH_CONST.__cfstring: 0x10c60
+  __AUTH_CONST.__objc_const: 0x17a10
   __AUTH_CONST.__weak_auth_got: 0xb0
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x78

   __AUTH_CONST.__auth_ptr: 0x0
   __AUTH.__objc_data: 0x2c10
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x11b0
+  __DATA.__objc_ivar: 0x11b4
   __DATA.__data: 0x521
   __DATA.__bss: 0x38
   __DATA_DIRTY.__objc_data: 0xb90

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 8204
-  Symbols:   13428
-  CStrings:  2358
+  Functions: 8222
+  Symbols:   13463
+  CStrings:  2368
 
Symbols:
+ +[PPSDataIngesterCommonUtilities arrayTableNameForEntryKey:metricName:]
+ +[PPSDataIngesterCommonUtilities arrayTableNamesByMetricForMetadataHistory:withEntryKey:]
+ +[PPSDataIngesterCommonUtilities dynamicTableNameForEntryKey:]
+ +[PPSOffDeviceIngesterUtilities allDataSourcesForMetadataHistories:subsystem:category:]
+ +[PPSOffDeviceIngesterUtilities dataSourceForMetadataHistories:subsystem:category:]
+ +[PPSSQLiteTimeSeriesIngester _joinedTableNamesForPrimaryTableName:tableNames:histories:definitions:predicate:]
+ -[PPSSQLiteEntity arrayTableNamesByProperty]
+ -[PPSSQLiteEntity initWithTableNames:arrayTableNamesByProperty:]
+ -[PPSSQLiteEntity sqlForCondition:onProperty:]
+ -[PPSSQLiteTimeSeriesIngester _appendValuesForArrayMetric:fromTable:toContainersByID:database:error:]
+ -[PPSSQLiteTimeSeriesIngester _convertSQLiteDataFromQuery:withMetricDefinitions:arrayTableNamesByMetric:groupId:error:]
+ -[PPSSQLiteTimeSeriesIngester _convertedValue:forMetric:]
+ -[PPSTimeSeriesRequest initWithDistinctMetrics:predicate:timeFilter:]
+ -[PPSTimestampConverter monotonicRangeForStartEpoch:endEpoch:startMonotonic:endMonotonic:]
+ OBJC_IVAR_$_PPSSQLiteEntity._arrayTableNamesByProperty
+ _OBJC_CLASS_$_PPSMetric
+ _PPSCollectPredicateKeyPaths
+ __101-[PPSSQLiteTimeSeriesIngester _appendValuesForArrayMetric:fromTable:toContainersByID:database:error:]_block_invoke
+ __119-[PPSSQLiteTimeSeriesIngester _convertSQLiteDataFromQuery:withMetricDefinitions:arrayTableNamesByMetric:groupId:error:]_block_invoke_2
+ ___101-[PPSSQLiteTimeSeriesIngester _appendValuesForArrayMetric:fromTable:toContainersByID:database:error:]_block_invoke
+ ___119-[PPSSQLiteTimeSeriesIngester _convertSQLiteDataFromQuery:withMetricDefinitions:arrayTableNamesByMetric:groupId:error:]_block_invoke
+ ___119-[PPSSQLiteTimeSeriesIngester _convertSQLiteDataFromQuery:withMetricDefinitions:arrayTableNamesByMetric:groupId:error:]_block_invoke_2
+ ___87+[PPSOffDeviceIngesterUtilities allDataSourcesForMetadataHistories:subsystem:category:]_block_invoke
+ ___block_descriptor_106_e8_32s40s48s56s64r72r80r88r_e39_B32?0"NSArray"8^{PPSSQLiteRow=}16^24l
+ ___block_descriptor_120_e8_32s40s48s56s64s72s80s88r96r104r_e18_16?0^{sqlite3=}8l
+ ___block_descriptor_40_e8_32s_e23_v16?0^{sqlite3_stmt=}8l
+ ___block_descriptor_56_e8_32s40s48s_e27_B24?0^{PPSSQLiteRow=}8^16l
+ ___block_descriptor_80_e8_32s40s48r_e15_"PPSEvent"8?0l
+ ___copy_helper_block_e8_32s40s48s
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88r96r104r
+ ___destroy_helper_block_e8_32s40s48s
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s88r96r104r
+ _objc_msgSend$_appendValuesForArrayMetric:fromTable:toContainersByID:database:error:
+ _objc_msgSend$_convertSQLiteDataFromQuery:withMetricDefinitions:arrayTableNamesByMetric:groupId:error:
+ _objc_msgSend$_convertedValue:forMetric:
+ _objc_msgSend$_joinedTableNamesForPrimaryTableName:tableNames:histories:definitions:predicate:
+ _objc_msgSend$allDataSourcesForMetadataHistories:subsystem:category:
+ _objc_msgSend$arrayTableNameForEntryKey:metricName:
+ _objc_msgSend$arrayTableNamesByMetricForMetadataHistory:withEntryKey:
+ _objc_msgSend$arrayTableNamesByProperty
+ _objc_msgSend$dataSourceForMetadataHistories:subsystem:category:
+ _objc_msgSend$database
+ _objc_msgSend$dynamicTableNameForEntryKey:
+ _objc_msgSend$initWithTableNames:arrayTableNamesByProperty:
+ _objc_msgSend$lastPathComponent
+ _objc_msgSend$monotonicRangeForStartEpoch:endEpoch:startMonotonic:endMonotonic:
+ _objc_msgSend$sqlForCondition:onProperty:
- -[PPSSQLiteTimeSeriesIngester _convertSQLiteDataFromQuery:withMetricDefinitions:error:]
- __87-[PPSSQLiteTimeSeriesIngester _convertSQLiteDataFromQuery:withMetricDefinitions:error:]_block_invoke
- ___78+[PPSOffDeviceIngesterUtilities allDataSourcesForFilepath:subsystem:category:]_block_invoke
- ___87-[PPSSQLiteTimeSeriesIngester _convertSQLiteDataFromQuery:withMetricDefinitions:error:]_block_invoke
- ___block_descriptor_104_e8_32s40s48s56s64s72s80r88r96r_e18_16?0^{sqlite3=}8l
- ___block_descriptor_88_e8_32s40s48s56s64r_e15_"PPSEvent"8?0l
- ___block_descriptor_99_e8_32s40s48s56s64r72r80r88r_e39_B32?0"NSArray"8^{PPSSQLiteRow=}16^24l
- ___copy_helper_block_e8_32s40s48s56s64r
- ___copy_helper_block_e8_32s40s48s56s64s72s80r88r96r
- ___destroy_helper_block_e8_32s40s48s56s64r
- ___destroy_helper_block_e8_32s40s48s56s64s72s80r88r96r
- _objc_msgSend$_convertSQLiteDataFromQuery:withMetricDefinitions:error:
CStrings:
+ " WHERE %@ IN (?"
+ "'%d'.%@"
+ "('%d'.%@ IN (SELECT %@ FROM '%@' WHERE %@))"
+ "B24@?0^{PPSSQLiteRow=}8^@16"
+ "Distinct requests cannot select the timestampEnd metric."
+ "Distinct requests cannot select variable-length array metric '%@'."
+ "Distinct requests cannot use limitCount, offsetCount, or readDirection."
+ "Epoch range [%.6f, %.6f] has no monotonic preimage in %{public}@ (%zu system-offset entries)."
+ "Inverted timestamp range for key-path %{public}@: [%.6f, %.6f]. Query will match no rows."
+ "SELECT %@, \"%@\" FROM '%@'"
```
