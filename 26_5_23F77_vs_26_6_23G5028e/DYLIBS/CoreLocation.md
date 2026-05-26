## CoreLocation

> `/System/Library/Frameworks/CoreLocation.framework/CoreLocation`

```diff

-3075.0.8.0.0
-  __TEXT.__text: 0x2098f0
+3077.0.2.0.0
+  __TEXT.__text: 0x209d08
   __TEXT.__auth_stubs: 0x1b20
-  __TEXT.__objc_methlist: 0xa5e4
+  __TEXT.__objc_methlist: 0xa5f4
   __TEXT.__const: 0x4ad8
   __TEXT.__gcc_except_tab: 0xf8e4
   __TEXT.__oslogstring: 0x3c017
-  __TEXT.__cstring: 0x265e8
+  __TEXT.__cstring: 0x26785
   __TEXT.__ustring: 0x70a
-  __TEXT.__unwind_info: 0x59d8
+  __TEXT.__unwind_info: 0x59e8
   __TEXT.__objc_classname: 0x13a5
-  __TEXT.__objc_methname: 0x1d317
+  __TEXT.__objc_methname: 0x1d34a
   __TEXT.__objc_methtype: 0x5e06
   __TEXT.__objc_stubs: 0xeb60
-  __DATA_CONST.__got: 0x748
-  __DATA_CONST.__const: 0x2170
+  __DATA_CONST.__got: 0x740
+  __DATA_CONST.__const: 0x2198
   __DATA_CONST.__objc_classlist: 0x540
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x55a0
+  __DATA_CONST.__objc_selrefs: 0x55a8
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x4d0
   __DATA_CONST.__objc_arraydata: 0x90
   __AUTH_CONST.__auth_got: 0xda8
   __AUTH_CONST.__const: 0x3bf0
-  __AUTH_CONST.__cfstring: 0xc180
+  __AUTH_CONST.__cfstring: 0xc380
   __AUTH_CONST.__objc_const: 0x11a10
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  UUID: C79BC252-923E-346E-8B79-C6689D42618D
-  Functions: 5343
-  Symbols:   1115
-  CStrings:  12175
+  UUID: 6A5123C0-7CCA-3E77-A7C8-0F85159CE1D8
+  Functions: 5345
+  Symbols:   1114
+  CStrings:  12209
 
Symbols:
- _kCLDistanceFilterNone
CStrings:
+ "+[CLReductiveFilterSuite deriveLocationFromLocations:options:analyticsDict:]"
+ "23:11:45"
+ "@\"NSMutableDictionary\"8@?0"
+ "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/044FDE39-C39B-4CD1-8604-4B26BEE2E49C/TemporaryDirectory.RK2mtX/Sources/CoreLocationFramework/Oscar/Math/CMFactoredMatrix.h, line 237,invalid col %zu > %zu."
+ "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/044FDE39-C39B-4CD1-8604-4B26BEE2E49C/TemporaryDirectory.RK2mtX/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 71,invalid col %zu > %zu."
+ "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/044FDE39-C39B-4CD1-8604-4B26BEE2E49C/TemporaryDirectory.RK2mtX/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 78,invalid col %zu > %zu."
+ "Assertion failed: col > row, file /Library/Caches/com.apple.xbs/044FDE39-C39B-4CD1-8604-4B26BEE2E49C/TemporaryDirectory.RK2mtX/Sources/CoreLocationFramework/Oscar/Math/CMFactoredMatrix.h, line 238,invalid element %zu <= %zu."
+ "Assertion failed: i < N, file /Library/Caches/com.apple.xbs/044FDE39-C39B-4CD1-8604-4B26BEE2E49C/TemporaryDirectory.RK2mtX/Sources/CoreLocationFramework/Oscar/Math/CMVector.h, line 273,invalid index %zu >= %zu."
+ "Assertion failed: i < N, file /Library/Caches/com.apple.xbs/044FDE39-C39B-4CD1-8604-4B26BEE2E49C/TemporaryDirectory.RK2mtX/Sources/CoreLocationFramework/Oscar/Math/CMVector.h, line 279,invalid index %zu >= %zu."
+ "Assertion failed: ldx < M*N, file /Library/Caches/com.apple.xbs/044FDE39-C39B-4CD1-8604-4B26BEE2E49C/TemporaryDirectory.RK2mtX/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 84,invalid element %zu >= %zu."
+ "Assertion failed: row < M, file /Library/Caches/com.apple.xbs/044FDE39-C39B-4CD1-8604-4B26BEE2E49C/TemporaryDirectory.RK2mtX/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 70,invalid row %zu > %zu."
+ "Assertion failed: row < M, file /Library/Caches/com.apple.xbs/044FDE39-C39B-4CD1-8604-4B26BEE2E49C/TemporaryDirectory.RK2mtX/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 77,invalid row %zu > %zu."
+ "May 15 2026"
+ "accuracyDeltaToBestInput"
+ "bestInputHorizontalAccuracy"
+ "com.apple.locationd.framework.reductivefilter"
+ "deriveLocationFromLocations:options:analyticsDict:"
+ "filterDuration"
+ "mostRecentInputHorizontalAccuracy"
+ "numFutureRejected"
+ "numInputObservations"
+ "numLowAccuracyRejected"
+ "numOutliersRejected"
+ "numReachabilityRejected"
+ "numSkippedEarlyTermination"
+ "numTotalRejected"
+ "numUsed"
+ "outputHorizontalAccuracy"
+ "timestampOffsetFromMostRecent"
- "+[CLReductiveFilterSuite deriveLocationFromLocations:options:]"
- "17:48:28"
- "Apr 18 2026"
- "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/204B7BCE-D382-4A05-987A-1F1AA4085DE7/TemporaryDirectory.Td3n1B/Sources/CoreLocationFramework/Oscar/Math/CMFactoredMatrix.h, line 237,invalid col %zu > %zu."
- "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/204B7BCE-D382-4A05-987A-1F1AA4085DE7/TemporaryDirectory.Td3n1B/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 71,invalid col %zu > %zu."
- "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/204B7BCE-D382-4A05-987A-1F1AA4085DE7/TemporaryDirectory.Td3n1B/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 78,invalid col %zu > %zu."
- "Assertion failed: col > row, file /Library/Caches/com.apple.xbs/204B7BCE-D382-4A05-987A-1F1AA4085DE7/TemporaryDirectory.Td3n1B/Sources/CoreLocationFramework/Oscar/Math/CMFactoredMatrix.h, line 238,invalid element %zu <= %zu."
- "Assertion failed: i < N, file /Library/Caches/com.apple.xbs/204B7BCE-D382-4A05-987A-1F1AA4085DE7/TemporaryDirectory.Td3n1B/Sources/CoreLocationFramework/Oscar/Math/CMVector.h, line 273,invalid index %zu >= %zu."
- "Assertion failed: i < N, file /Library/Caches/com.apple.xbs/204B7BCE-D382-4A05-987A-1F1AA4085DE7/TemporaryDirectory.Td3n1B/Sources/CoreLocationFramework/Oscar/Math/CMVector.h, line 279,invalid index %zu >= %zu."
- "Assertion failed: ldx < M*N, file /Library/Caches/com.apple.xbs/204B7BCE-D382-4A05-987A-1F1AA4085DE7/TemporaryDirectory.Td3n1B/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 84,invalid element %zu >= %zu."
- "Assertion failed: row < M, file /Library/Caches/com.apple.xbs/204B7BCE-D382-4A05-987A-1F1AA4085DE7/TemporaryDirectory.Td3n1B/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 70,invalid row %zu > %zu."
- "Assertion failed: row < M, file /Library/Caches/com.apple.xbs/204B7BCE-D382-4A05-987A-1F1AA4085DE7/TemporaryDirectory.Td3n1B/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 77,invalid row %zu > %zu."

```
