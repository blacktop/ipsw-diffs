## GeoAnalytics

> `/System/Library/PrivateFrameworks/GeoAnalytics.framework/GeoAnalytics`

```diff

-1986.32.8.22.7
-  __TEXT.__text: 0x9bdfc
+1986.32.8.22.11
+  __TEXT.__text: 0x9d834
   __TEXT.__auth_stubs: 0x820
-  __TEXT.__objc_methlist: 0x1974
+  __TEXT.__objc_methlist: 0x1a6c
   __TEXT.__const: 0x620
   __TEXT.__gcc_except_tab: 0x448
-  __TEXT.__cstring: 0xfaad
-  __TEXT.__oslogstring: 0xba5
+  __TEXT.__cstring: 0xfc9b
+  __TEXT.__oslogstring: 0xc44
   __TEXT.__dlopen_cstrs: 0x126
-  __TEXT.__unwind_info: 0xe38
-  __TEXT.__objc_classname: 0x30d
-  __TEXT.__objc_methname: 0x111a4
-  __TEXT.__objc_methtype: 0x17ff
-  __TEXT.__objc_stubs: 0xd3e0
+  __TEXT.__unwind_info: 0xe28
+  __TEXT.__objc_classname: 0x34a
+  __TEXT.__objc_methname: 0x114bd
+  __TEXT.__objc_methtype: 0x1973
+  __TEXT.__objc_stubs: 0xd520
   __DATA_CONST.__got: 0x638
-  __DATA_CONST.__const: 0x4f40
-  __DATA_CONST.__objc_classlist: 0xb0
+  __DATA_CONST.__const: 0x4fb0
+  __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x20
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b18
-  __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x68
-  __DATA_CONST.__objc_arraydata: 0x750
+  __DATA_CONST.__objc_selrefs: 0x3b88
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_superrefs: 0x70
+  __DATA_CONST.__objc_arraydata: 0x758
   __AUTH_CONST.__auth_got: 0x428
-  __AUTH_CONST.__const: 0x30c0
-  __AUTH_CONST.__cfstring: 0x12a40
-  __AUTH_CONST.__objc_const: 0x1de8
+  __AUTH_CONST.__const: 0x3100
+  __AUTH_CONST.__cfstring: 0x12ba0
+  __AUTH_CONST.__objc_const: 0x2100
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__objc_intobj: 0x1038
+  __AUTH_CONST.__objc_intobj: 0x10f8
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0x398
-  __DATA.__objc_ivar: 0xcc
-  __DATA.__data: 0x1520
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0xdc
+  __DATA.__data: 0x15a0
   __DATA.__bss: 0x18
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_ivar: 0x4c

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1410
-  Symbols:   1981
-  CStrings:  4810
+  Functions: 1437
+  Symbols:   2009
+  CStrings:  4857
 
Symbols:
+ _GeoAnalyticsConfig__debug_UploadCountersEnabled
+ _GeoAnalyticsUserActionConfig_visualIntelligenceShortUserActions_dropRate
CStrings:
+ "\x04"
+ "+[GEOAPPortal(UserActionCodeGen) captureVisualIntelligenceShortUserActionsWithAction:target:value:moduleType:moduleMetadata:richProviderId:additionalStates:providedDropRate:completionQueue:completionBlock:]"
+ "@32@0:8@?16@?24"
+ "Assertion failed: _completionBlock != ((void *)0)"
+ "Assertion failed: _historyVisitorBlock != ((void *)0)"
+ "Assertion failed: _inflightVisitorBlock != ((void *)0)"
+ "DOWNLOAD_OFFLINE_MAP"
+ "EXPAND_DETECTION_LIST"
+ "GEOAPShowUploadInfoHandler"
+ "GEOAPXPCMapsDebugPanelExporting"
+ "GeoAnalyticsEvent_visualIntelligenceShortUserActions_dropRate"
+ "OFFLINE"
+ "REVEAL_DETECTION_LIST"
+ "TAP_EXPAND"
+ "TAP_RECOMMENDATION"
+ "VISUAL_INTELLIGENCE_DETECTION"
+ "VISUAL_INTELLIGENCE_DETECTION_LIST"
+ "VISUAL_INTELLIGENCE_SNIPPET"
+ "_completionBlock"
+ "_daemonConnectionWithExportedProtocol:instance:"
+ "_debug_UploadCountersEnabled"
+ "_historyVisitorBlock"
+ "_inflightVisitorBlock"
+ "captureVisualIntelligenceShortUserActionsWithAction:target:value:moduleType:moduleMetadata:richProviderId:additionalStates:providedDropRate:completionQueue:completionBlock:"
+ "endHistoricalData"
+ "endInflightData"
+ "flushUploadHistoryWithCompletion:"
+ "inflightBatchUUID:createTime:analyticSessionType:eventCount:uploadSize:urlSessionType:stageNumber:"
+ "initWithHistoryVisitorBlock:completion:"
+ "initWithInflightVisitorBlock:completion:"
+ "mapsInOfflineMode"
+ "setHasRotated:"
+ "shared"
+ "showHistoryOfAge:"
+ "showHistoryOfAge:withVisitorBlock:completion:"
+ "showInflight"
+ "showInflightUploadsWithVisitorBlock:completion:"
+ "showUploadCounts:"
+ "uploadHistoryForBatchUUID:endDate:uploadLatency:analyticSessionType:eventCount:uploadSize:urlSessionType:stageNumber:"
+ "v20@0:8I16"
+ "v24@0:8@?<v@?@\"NSError\">16"
+ "v24@0:8@?<v@?II>16"
+ "v32@0:8@?16@?24"
+ "v32@0:8@?<v@?@\"NSString\"@\"NSDate\"iIIiI>16@?<v@?>24"
+ "v36@0:8I16@?20@?28"
+ "v36@0:8I16@?<v@?@\"NSString\"@\"NSDate\"IiIIiI>20@?<v@?>28"
+ "v52@0:8@\"NSString\"16@\"NSDate\"24i32I36I40i44I48"
+ "v52@0:8@16@24i32I36I40i44I48"
+ "v56@0:8@\"NSString\"16@\"NSDate\"24I32i36I40I44i48I52"
+ "v56@0:8@16@24I32i36I40I44i48I52"
- "setDidPreviouslyRotate:"
- "stream"
- "visit"

```
