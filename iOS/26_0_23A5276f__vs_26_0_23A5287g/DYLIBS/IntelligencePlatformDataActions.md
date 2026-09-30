## IntelligencePlatformDataActions

> `/System/Library/PrivateFrameworks/IntelligencePlatformDataActions.framework/IntelligencePlatformDataActions`

```diff

-149.0.4.0.0
-  __TEXT.__text: 0x2bd60
-  __TEXT.__auth_stubs: 0x1650
+151.0.3.0.0
+  __TEXT.__text: 0x2e4e8
+  __TEXT.__auth_stubs: 0x16a0
   __TEXT.__objc_methlist: 0x1bc
-  __TEXT.__const: 0x1c88
-  __TEXT.__cstring: 0x135c
-  __TEXT.__constg_swiftt: 0xa04
-  __TEXT.__swift5_typeref: 0xc08
-  __TEXT.__swift5_reflstr: 0xc03
-  __TEXT.__swift5_fieldmd: 0xeac
+  __TEXT.__const: 0x1cc8
+  __TEXT.__cstring: 0x13dc
+  __TEXT.__constg_swiftt: 0xa90
+  __TEXT.__swift5_typeref: 0xc74
+  __TEXT.__swift5_reflstr: 0xc13
+  __TEXT.__swift5_fieldmd: 0xef0
   __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_assocty: 0x258
   __TEXT.__swift5_proto: 0x100
-  __TEXT.__swift5_types: 0xc8
-  __TEXT.__oslogstring: 0xa5a
+  __TEXT.__swift5_types: 0xd0
+  __TEXT.__oslogstring: 0xb08
   __TEXT.__swift_as_entry: 0x34
-  __TEXT.__swift5_capture: 0xf4
+  __TEXT.__swift5_capture: 0x114
   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift_as_ret: 0x2c
-  __TEXT.__unwind_info: 0xc60
-  __TEXT.__eh_frame: 0x1390
+  __TEXT.__unwind_info: 0xce8
+  __TEXT.__eh_frame: 0x14f0
   __TEXT.__objc_methname: 0x33a
   __DATA_CONST.__got: 0x2e0
   __DATA_CONST.__const: 0x168
-  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x178
   __DATA_CONST.__objc_protorefs: 0x8
-  __AUTH_CONST.__auth_got: 0xb28
-  __AUTH_CONST.__const: 0x1520
-  __AUTH_CONST.__objc_const: 0x978
+  __AUTH_CONST.__auth_got: 0xb50
+  __AUTH_CONST.__const: 0x1570
+  __AUTH_CONST.__objc_const: 0xa30
   __AUTH.__objc_data: 0x408
-  __AUTH.__data: 0xb78
-  __DATA.__data: 0x620
+  __AUTH.__data: 0xcb0
+  __DATA.__data: 0x670
   __DATA.__bss: 0x1e00
   __DATA.__common: 0x58
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BF07AB98-F5B0-31F9-9299-E4AD55BA55E6
-  Functions: 1269
+  UUID: D088C586-7D9E-3CDE-AB1D-D314D325A901
+  Functions: 1302
   Symbols:   171
-  CStrings:  213
+  CStrings:  218
 
CStrings:
+ "    SELECT DISTINCT umcId, name, leagueName, imageBytes FROM \"IntelligencePlatform.Entity\".\"SportsTeams\" ORDER BY leagueName, name;"
+ "    SELECT DISTINCT umcId, name, leagueName, imageBytes FROM \"IntelligencePlatform.Entity\".\"SportsTeams\" WHERE umcId = ?;"
+ "SportsAction: Cache contains %ld items"
+ "SportsAction: Cache key %{sensitive}s, timestamp: %s"
+ "SportsAction: Using cached games for: %{sensitive}s"
+ "SportsAction: processEventDetails: liveGlobalKnowledgeQuerySource is nil"
+ "SportsAction: processEventDetails: sqlConnection is nil"
+ "_TtCV31IntelligencePlatformDataActions12SportsActionP33_C18F9F702776B996567DC0073DDFD73912CacheStorage"
+ "cache"
- "    SELECT umcId, name, leagueName, imageBytes FROM \"IntelligencePlatform.Entity\".\"SportsTeams\" ORDER BY leagueName, name;"
- "    SELECT umcId, name, leagueName, imageBytes FROM \"IntelligencePlatform.Entity\".\"SportsTeams\" WHERE umcId = ?;"
- "SportsAction: processEventDetaitls: liveGlobalKnowledgeQuerySource is nil"
- "SportsAction: processEventDetaitls: sqlConnection is nil"

```
