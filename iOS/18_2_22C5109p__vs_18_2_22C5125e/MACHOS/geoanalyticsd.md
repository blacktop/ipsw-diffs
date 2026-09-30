## geoanalyticsd

> `/System/Library/PrivateFrameworks/GeoAnalytics.framework/geoanalyticsd`

```diff

-1986.32.8.22.7
-  __TEXT.__text: 0x15a64
-  __TEXT.__auth_stubs: 0x800
-  __TEXT.__objc_stubs: 0x3000
-  __TEXT.__objc_methlist: 0x750
-  __TEXT.__const: 0x110
-  __TEXT.__gcc_except_tab: 0x360
-  __TEXT.__cstring: 0x312d
-  __TEXT.__oslogstring: 0x1151
-  __TEXT.__objc_classname: 0x1f7
-  __TEXT.__objc_methname: 0x29ba
-  __TEXT.__objc_methtype: 0x968
-  __TEXT.__unwind_info: 0x560
-  __DATA_CONST.__auth_got: 0x410
-  __DATA_CONST.__got: 0x268
-  __DATA_CONST.__const: 0xe38
-  __DATA_CONST.__cfstring: 0x2e60
-  __DATA_CONST.__objc_classlist: 0x78
-  __DATA_CONST.__objc_protolist: 0x38
+1986.32.8.22.11
+  __TEXT.__text: 0x183c0
+  __TEXT.__auth_stubs: 0x7f0
+  __TEXT.__objc_stubs: 0x31c0
+  __TEXT.__objc_methlist: 0x884
+  __TEXT.__const: 0x108
+  __TEXT.__gcc_except_tab: 0x448
+  __TEXT.__cstring: 0x38b4
+  __TEXT.__oslogstring: 0x11f1
+  __TEXT.__objc_classname: 0x22d
+  __TEXT.__objc_methname: 0x2ca5
+  __TEXT.__objc_methtype: 0xabc
+  __TEXT.__unwind_info: 0x648
+  __DATA_CONST.__auth_got: 0x408
+  __DATA_CONST.__got: 0x270
+  __DATA_CONST.__const: 0x10b0
+  __DATA_CONST.__cfstring: 0x2fc0
+  __DATA_CONST.__objc_classlist: 0x80
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x60
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x2188
-  __DATA.__objc_selrefs: 0xc68
-  __DATA.__objc_ivar: 0xb8
-  __DATA.__objc_data: 0x4b0
-  __DATA.__data: 0x2a0
-  __DATA.__bss: 0x118
+  __DATA.__objc_const: 0x2798
+  __DATA.__objc_selrefs: 0xce8
+  __DATA.__objc_ivar: 0xc4
+  __DATA.__objc_data: 0x500
+  __DATA.__data: 0x300
+  __DATA.__bss: 0x138
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 336
-  Symbols:   232
-  CStrings:  1218
+  Functions: 390
+  Symbols:   234
+  CStrings:  1285
 
Symbols:
+ _GeoAnalyticsConfig__debug_UploadCountersEnabled
+ _OBJC_CLASS_$_GEOAPDebugPersistence
+ _OBJC_METACLASS_$_GEOAPDebugPersistence
- _objc_retain_x27
CStrings:
+ "(%!@(MISSING)) %!@(MISSING) TTL (%!l(MISSING)d) preferred over %!@(MISSING) (%!l(MISSING)d)"
+ "(%!@(MISSING)) URL task complete for batchId:%!l(MISSING)lu -- %!@(MISSING) / %!@(MISSING) / %!u(MISSING)"
+ "(%!@(MISSING)) batchId %!l(MISSING)lu had %!l(MISSING)lu expired records"
+ "(%!@(MISSING)) batchId:%!l(MISSING)lu -- upload stage %!l(MISSING)u:%!@(MISSING) for %!@(MISSING) ended in error"
+ "(%!@(MISSING)) move %!@(MISSING) to %!@(MISSING) failed (%!@(MISSING))"
+ "(%!@(MISSING)) nothing to upload for batchId %!l(MISSING)lu"
+ "(%!@(MISSING)) remove %!@(MISSING) failed (%!@(MISSING))"
+ "(%!@(MISSING)) starting stage %!@(MISSING) failed"
+ "(%!@(MISSING)) unable to create upload file writer for batch id %!l(MISSING)lu; unable to upload right now"
+ "(%!@(MISSING)) unable to finalize and close upload file for batchId %!l(MISSING)lu; will try upload later"
+ "(%!@(MISSING)) unable to write upload record for batch id %!l(MISSING)lu; stopping here"
+ "(%!@(MISSING)) upload batchId %!l(MISSING)lu is using uploading policy type '%!@(MISSING)' : %!l(MISSING)u messages of size %!l(MISSING)u with TTL %!l(MISSING)d"
+ "(%!@(MISSING)) upload requested for batch id %!l(MISSING)lu / message Type : %!@(MISSING), upload policy : %!@(MISSING), opaqueId : %!u(MISSING)"
+ "(%!@(MISSING)) upload stage %!l(MISSING)u:%!@(MISSING) for batchId %!l(MISSING)lu exhausted the remaining TTL"
+ "(%!@(MISSING)) upload stage finished %!@(MISSING)"
+ "@batchUUID"
+ "@createTime"
+ "@eventCount"
+ "@sessionType"
+ "@stageNum"
+ "@uploadDoneTime"
+ "@uploadLatency"
+ "@uploadPolicy"
+ "@uploadSize"
+ "APDebug.db"
+ "CREATE TABLE IF NOT EXISTS uploadHistory (batchUUID STRING NOT NULL, uploadDoneTime DATETIME DEFAULT CURRENT_TIMESTAMP, uploadLatency INTEGER NOT NULL, sessionType INTEGER NOT NULL, eventCount INTEGER NOT NULL, uploadSize INTEGER NOT NULL, uploadPolicy INTEGER NOT NULL, stageNum INTEGER NOT NULL );"
+ "CREATE TABLE IF NOT EXISTS uploadInflight (batchUUID STRING NOT NULL, createTime DATETIME DEFAULT CURRENT_TIMESTAMP, sessionType INTEGER NOT NULL, eventCount INTEGER NOT NULL, uploadSize INTEGER NOT NULL, uploadPolicy INTEGER NOT NULL, stageNum INTEGER NOT NULL );"
+ "DELETE FROM uploadHistory;"
+ "DELETE FROM uploadInflight WHERE batchUUID=@batchUUID;"
+ "DROP TABLE uploadHistory;"
+ "DROP TABLE uploadInflight;"
+ "DebugPersistence"
+ "GEOAPDebugPersistence"
+ "GEOAPXPCMapsDebugPanelExporting"
+ "INSERT INTO uploadHistory (batchUUID,uploadDoneTime,uploadLatency,sessionType,eventCount,uploadSize,uploadPolicy,stageNum) VALUES ( @batchUUID, DATETIME( @uploadDoneTime, 'UNIXEPOCH') ,@uploadLatency,@sessionType,@eventCount,@uploadSize,@uploadPolicy,@stageNum);"
+ "INSERT INTO uploadInflight (batchUUID,createTime,sessionType,eventCount,uploadSize,uploadPolicy,stageNum)VALUES ( @batchUUID, DATETIME( @createTime, 'UNIXEPOCH') ,@sessionType,@eventCount,@uploadSize,@uploadPolicy,@stageNum);"
+ "SELECT COUNT(1) FROM uploadHistory;"
+ "SELECT COUNT(1) FROM uploadInflight;"
+ "SELECT batchUUID,createTime,sessionType,eventCount,uploadSize,uploadPolicy,stageNum FROM uploadInflight;"
+ "SELECT batchUUID,uploadLatency,sessionType,eventCount,uploadSize,uploadPolicy,stageNum, strftime('%!s(MISSING)',uploadDoneTime) FROM uploadHistory WHERE uploadDoneTime >= DATETIME( @uploadDoneTime, 'UNIXEPOCH');"
+ "_debugUploadCountersEnabled"
+ "addInflightUploadWithBatchUUID:createTime:sessionType:eventCount:uploadSize:uploadPolicy:stageNum:"
+ "addUploadHistoryForBatchUUID:completionTime:latency:sessionType:eventCount:uploadSize:uploadPolicy:stageNum:"
+ "cntH"
+ "cntI"
+ "com.apple.geo.analytics.debugdb"
+ "delAllUH"
+ "delIU"
+ "deleteAllHistory"
+ "endHistoricalData"
+ "endInflightData"
+ "flushUploadHistoryWithCompletion:"
+ "inflightBatchUUID:createTime:analyticSessionType:eventCount:uploadSize:urlSessionType:stageNumber:"
+ "initWithTimeIntervalSince1970:"
+ "insIU"
+ "insUH"
+ "recording upload history for batch %!@(MISSING)"
+ "removeInflightUploadWithBatchUUID:"
+ "selIU"
+ "selUH"
+ "showHistoryOfAge:"
+ "showHistoryOfAge:withVisitorBlock:completion:"
+ "showInflight"
+ "showInflightUploadsWithVisitorBlock:completion:"
+ "showUploadCounts:"
+ "successfully"
+ "unsuccessfully"
+ "uploadHistoryForBatchUUID:endDate:uploadLatency:analyticSessionType:eventCount:uploadSize:urlSessionType:stageNumber:"
+ "v20@0:8I16"
+ "v24@0:8@?<v@?@\"NSError\">16"
+ "v24@0:8@?<v@?II>16"
+ "v32@0:8@?<v@?@\"NSString\"@\"NSDate\"iIIiI>16@?<v@?>24"
+ "v36@0:8I16@?20@?28"
+ "v36@0:8I16@?<v@?@\"NSString\"@\"NSDate\"IiIIiI>20@?<v@?>28"
+ "v44@?0@\"NSString\"8@\"NSDate\"16i24I28I32i36I40"
+ "v48@?0@\"NSString\"8@\"NSDate\"16I24i28I32I36i40I44"
+ "v52@0:8@\"NSString\"16@\"NSDate\"24i32I36I40i44I48"
+ "v52@0:8@16@24i32I36I40i44I48"
+ "v56@0:8@\"NSString\"16@\"NSDate\"24I32i36I40I44i48I52"
+ "v56@0:8@16@24I32i36I40I44i48I52"
+ "v60@?0Q8Q16Q24Q32@\"NSDate\"40i48@\"NSString\"52"
- "%!@(MISSING) TTL (%!l(MISSING)d) preferred over %!@(MISSING) (%!l(MISSING)d)"
- "URL task complete for batchId:%!l(MISSING)lu -- %!@(MISSING) / %!@(MISSING) / %!u(MISSING)"
- "batchId %!l(MISSING)lu had %!l(MISSING)lu expired records"
- "batchId:%!l(MISSING)lu -- upload stage %!l(MISSING)u:%!@(MISSING) for %!@(MISSING) ended in error"
- "move %!@(MISSING) to %!@(MISSING) failed (%!@(MISSING))"
- "nothing to upload for batchId %!l(MISSING)lu"
- "starting stage %!@(MISSING) failed"
- "unable to create upload file writer for batch id %!l(MISSING)lu; unable to upload right now"
- "unable to finalize and close upload file for batchId %!l(MISSING)lu; will try upload later"
- "unable to write upload record for batch id %!l(MISSING)lu; stopping here"
- "upload batchId %!l(MISSING)lu is using uploading policy type '%!@(MISSING)' : %!l(MISSING)u messages of size %!l(MISSING)u with TTL %!l(MISSING)d"
- "upload requested for batch id %!l(MISSING)lu / message Type : %!@(MISSING), upload policy : %!@(MISSING), opaqueId : %!u(MISSING)"
- "upload stage %!l(MISSING)u:%!@(MISSING) for batchId %!l(MISSING)lu exhausted the remaining TTL"
- "v52@?0Q8Q16Q24Q32@\"NSDate\"40i48"

```
