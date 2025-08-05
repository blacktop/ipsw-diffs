## FinHealthXPCServices

> `/System/Library/PrivateFrameworks/FinHealth.framework/XPCServices/FinHealthXPCServices.xpc/FinHealthXPCServices`

```diff

-1.8.1.48.0
-  __TEXT.__text: 0x12bcc
+1.8.1.51.0
+  __TEXT.__text: 0x12f00
   __TEXT.__auth_stubs: 0x630
   __TEXT.__objc_stubs: 0x3620
-  __TEXT.__objc_methlist: 0xd54
-  __TEXT.__const: 0xb0
+  __TEXT.__objc_methlist: 0xd5c
+  __TEXT.__const: 0xb8
   __TEXT.__gcc_except_tab: 0x574
-  __TEXT.__objc_methname: 0x468a
-  __TEXT.__cstring: 0x10d1
-  __TEXT.__oslogstring: 0xc0a
+  __TEXT.__objc_methname: 0x46cd
+  __TEXT.__cstring: 0x10fb
+  __TEXT.__oslogstring: 0xcd8
   __TEXT.__objc_classname: 0x13b
-  __TEXT.__objc_methtype: 0xe07
-  __TEXT.__unwind_info: 0x3b0
+  __TEXT.__objc_methtype: 0xe09
+  __TEXT.__unwind_info: 0x3b8
   __DATA_CONST.__auth_got: 0x328
-  __DATA_CONST.__got: 0x708
+  __DATA_CONST.__got: 0x710
   __DATA_CONST.__const: 0x7a0
-  __DATA_CONST.__cfstring: 0x8c0
+  __DATA_CONST.__cfstring: 0x920
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0x1820
-  __DATA.__objc_selrefs: 0x1168
+  __DATA.__objc_selrefs: 0x1170
   __DATA.__objc_ivar: 0x88
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x180

   - /System/Library/PrivateFrameworks/PersonalizationPortrait.framework/PersonalizationPortrait
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 203591BC-C703-32CD-B8FD-96BFDE655156
-  Functions: 255
-  Symbols:   355
-  CStrings:  1055
+  UUID: 6E006A4C-D3FB-32E7-84C9-87F58BD2A656
+  Functions: 257
+  Symbols:   356
+  CStrings:  1064
 
Symbols:
+ _FHGeoMaxAllowedRecords
CStrings:
+ "-[FinHealthStateController _processAggregateFeaturesWithHardReset:forceStalenessCheck:]_block_invoke"
+ "FALSE"
+ "Resetting fhGeoFeatures records processed counter: _totalRecordsProcessed: %lu, _numberOfSkippedBatches: %lu"
+ "Skipping GEO for %lu records"
+ "TRUE"
+ "_processAggregateFeaturesWithHardReset:forceStalenessCheck:"
+ "_totalRecordsProcessed: %lu, maxAllowedRecords: %lu, thresholdOrBypass: %@, bypassMapService: %@"
+ "aggregateFeaturesWithProcessSource:completion:"
+ "bypassMapService: %@"
+ "finhealthd"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSString\"@\"NSError\">24"
- "-[FinHealthStateController _processAggregateFeaturesWithHardReset:]_block_invoke"
- "@20@0:8B16"
- "Resetting fhGeoFeatures records processed counter"
- "_processAggregateFeaturesWithHardReset:"
- "v24@0:8@?<v@?@\"NSString\"@\"NSError\">16"

```
