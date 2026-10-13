## PerfPowerServicesReader

> `/System/Library/PrivateFrameworks/PerfPowerServicesReader.framework/PerfPowerServicesReader`

```diff

-3486.40.112.0.0
-  __TEXT.__text: 0x151140
+3486.42.1.0.0
+  __TEXT.__text: 0x152434
   __TEXT.__init_offsets: 0xdc
-  __TEXT.__objc_methlist: 0x139ac
+  __TEXT.__objc_methlist: 0x13a34
   __TEXT.__const: 0x5fe2
-  __TEXT.__cstring: 0xe156
-  __TEXT.__gcc_except_tab: 0x4b10
+  __TEXT.__cstring: 0xe1d0
+  __TEXT.__gcc_except_tab: 0x4bc8
   __TEXT.__oslogstring: 0xe59
-  __TEXT.__unwind_info: 0x54a8
+  __TEXT.__unwind_info: 0x54e8
   __TEXT.__eh_frame: 0xa0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2bd8
+  __DATA_CONST.__const: 0x2c28
   __DATA_CONST.__objc_classlist: 0x590
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x368
-  __DATA_CONST.__objc_selrefs: 0x60c0
+  __DATA_CONST.__objc_selrefs: 0x6118
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x508
   __DATA_CONST.__objc_arraydata: 0x110
-  __DATA_CONST.__got: 0x758
+  __DATA_CONST.__got: 0x760
   __AUTH_CONST.__const: 0x3090
-  __AUTH_CONST.__cfstring: 0x10be0
-  __AUTH_CONST.__objc_const: 0x179e0
+  __AUTH_CONST.__cfstring: 0x10c60
+  __AUTH_CONST.__objc_const: 0x17a10
   __AUTH_CONST.__weak_auth_got: 0xb0
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x78

   __AUTH_CONST.__auth_got: 0x6e0
   __AUTH.__objc_data: 0x2c10
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x11b0
+  __DATA.__objc_ivar: 0x11b4
   __DATA.__data: 0x521
   __DATA_DIRTY.__objc_data: 0xb90
   __DATA_DIRTY.__data: 0xad8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 8166
-  Symbols:   12067
-  CStrings:  2363
+  Functions: 8182
+  Symbols:   12086
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
+ _OBJC_CLASS_$_PPSMetric
+ _OBJC_IVAR_$_PPSSQLiteEntity._arrayTableNamesByProperty
+ _PPSCollectPredicateKeyPaths
+ ___101-[PPSSQLiteTimeSeriesIngester _appendValuesForArrayMetric:fromTable:toContainersByID:database:error:]_block_invoke
+ ___101-[PPSSQLiteTimeSeriesIngester _appendValuesForArrayMetric:fromTable:toContainersByID:database:error:]_block_invoke_2
+ ___119-[PPSSQLiteTimeSeriesIngester _convertSQLiteDataFromQuery:withMetricDefinitions:arrayTableNamesByMetric:groupId:error:]_block_invoke
+ ___119-[PPSSQLiteTimeSeriesIngester _convertSQLiteDataFromQuery:withMetricDefinitions:arrayTableNamesByMetric:groupId:error:]_block_invoke_2
+ ___87+[PPSOffDeviceIngesterUtilities allDataSourcesForMetadataHistories:subsystem:category:]_block_invoke
+ ___block_descriptor_106_e8_32s40s48s56s64r72r80r88r_e39_B32?0"NSArray"8^{PPSSQLiteRow=}16^24ls32l8r64l8s40l8s48l8s56l8r72l8r80l8r88l8
+ ___block_descriptor_120_e8_32s40s48s56s64s72s80s88r96r104r_e18_16?0^{sqlite3=}8ls32l8r88l8s40l8s48l8r96l8s56l8s64l8r104l8s72l8s80l8
+ ___block_descriptor_40_e8_32s_e23_v16?0^{sqlite3_stmt=}8ls32l8
+ ___block_descriptor_56_e8_32s40s48s_e27_B24?0^{PPSSQLiteRow=}8^16ls32l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48r_e15_"PPSEvent"8?0ls32l8r48l8s40l8
- -[PPSSQLiteTimeSeriesIngester _convertSQLiteDataFromQuery:withMetricDefinitions:error:]
- ___78+[PPSOffDeviceIngesterUtilities allDataSourcesForFilepath:subsystem:category:]_block_invoke
- ___87-[PPSSQLiteTimeSeriesIngester _convertSQLiteDataFromQuery:withMetricDefinitions:error:]_block_invoke
- ___block_descriptor_104_e8_32s40s48s56s64s72s80r88r96r_e18_16?0^{sqlite3=}8ls32l8r80l8s40l8s48l8r88l8s56l8s64l8r96l8s72l8
- ___block_descriptor_88_e8_32s40s48s56s64r_e15_"PPSEvent"8?0ls32l8s40l8s48l8r64l8s56l8
- ___block_descriptor_99_e8_32s40s48s56s64r72r80r88r_e39_B32?0"NSArray"8^{PPSSQLiteRow=}16^24ls32l8r64l8s40l8s48l8s56l8r72l8r80l8r88l8
CStrings:
+ " WHERE %@ IN (?"
+ "'%d'.%@"
+ "('%d'.%@ IN (SELECT %@ FROM '%@' WHERE %@))"
+ "B24@?0^{PPSSQLiteRow=}8^@16"
+ "SELECT %@, \"%@\" FROM '%@'"
```
