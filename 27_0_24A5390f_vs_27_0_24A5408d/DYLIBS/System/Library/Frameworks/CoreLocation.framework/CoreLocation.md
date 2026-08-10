## CoreLocation

> `/System/Library/Frameworks/CoreLocation.framework/CoreLocation`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-3183.0.0.0.0
-  __TEXT.__text: 0x205ef0
-  __TEXT.__objc_methlist: 0x9b74
-  __TEXT.__const: 0x4cd0
-  __TEXT.__gcc_except_tab: 0xf1fc
-  __TEXT.__oslogstring: 0x3ab5c
-  __TEXT.__cstring: 0x24f39
+3185.0.6.0.1
+  __TEXT.__text: 0x206ef8
+  __TEXT.__objc_methlist: 0x9bd4
+  __TEXT.__const: 0x4d10
+  __TEXT.__gcc_except_tab: 0xf264
+  __TEXT.__oslogstring: 0x3abea
+  __TEXT.__cstring: 0x2514e
   __TEXT.__ustring: 0x70a
-  __TEXT.__unwind_info: 0x5688
+  __TEXT.__unwind_info: 0x56c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2158
-  __DATA_CONST.__objc_classlist: 0x498
+  __DATA_CONST.__const: 0x21b0
+  __DATA_CONST.__objc_classlist: 0x4a0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x52a0
+  __DATA_CONST.__objc_selrefs: 0x52d0
   __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__objc_superrefs: 0x420
+  __DATA_CONST.__objc_superrefs: 0x428
   __DATA_CONST.__objc_arraydata: 0xa0
   __DATA_CONST.__got: 0x690
-  __AUTH_CONST.__const: 0x3d10
-  __AUTH_CONST.__cfstring: 0xb920
-  __AUTH_CONST.__objc_const: 0x10298
+  __AUTH_CONST.__const: 0x3d30
+  __AUTH_CONST.__cfstring: 0xba40
+  __AUTH_CONST.__objc_const: 0x10468
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__auth_got: 0xdb8
-  __AUTH.__objc_data: 0x2800
-  __DATA.__objc_ivar: 0xb00
+  __AUTH.__objc_data: 0x2850
+  __DATA.__objc_ivar: 0xb24
   __DATA.__data: 0x1eb0
   __DATA.__bss: 0xa90
   __DATA.__common: 0x58

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 5203
-  Symbols:   1083
-  CStrings:  5541
+  Functions: 5216
+  Symbols:   1084
+  CStrings:  5556
 
Symbols:
+ _CLFlushErrorDomain
CStrings:
+ "-[CLLocationManager notifyWhenFlushedBufferedLocationsThroughDate:timeout:completion:]"
+ "-[CLLocationManager notifyWhenFlushedBufferedLocationsThroughDate:timeout:completion:]_block_invoke"
+ "00:18:13"
+ "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreLocationFramework/Oscar/Math/CMFactoredMatrix.h, line 255,invalid col %zu > %zu."
+ "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 71,invalid col %zu > %zu."
+ "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 78,invalid col %zu > %zu."
+ "Assertion failed: col > row, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreLocationFramework/Oscar/Math/CMFactoredMatrix.h, line 256,invalid element %zu <= %zu."
+ "Assertion failed: i < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreLocationFramework/Oscar/Math/CMVector.h, line 321,invalid index %zu >= %zu."
+ "Assertion failed: ldx < M*N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 84,invalid element %zu >= %zu."
+ "Assertion failed: row < M, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 70,invalid row %zu > %zu."
+ "Assertion failed: row < M, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 77,invalid row %zu > %zu."
+ "Aug  5 2026"
+ "CLFlushErrorDomain"
+ "CLMM,%{public}.1lf,Propagating,lat,%{sensitive}.8lf,lon,%{sensitive}.8lf,course,%{public}.3lf,speed,%{public}.1lf,speedLimit,%{public}.1lf,rampSpeed,%{public}.1lf,speedAtPropagationStart,%{public}.1lf"
+ "SimulateBufferedGnssPlatform"
+ "com.apple.corelocation.bufferedlocationflushmonitor"
+ "flush aborted: location updates stopped"
+ "flush aborted: manager invalidated"
+ "flush called with a nil completion; nothing to signal"
+ "flush completion will run on the shared queue; this manager is not backed by a dispatch delegate queue"
+ "flush not supported on this device"
+ "flush rejected: %{public}@"
+ "flush requires a non-nil date"
+ "flush requires an active rhythmic-waking session"
+ "flush superseded by a newer flush"
+ "flush timeout must be a positive, finite number"
+ "isContinuationOfPriorBatch"
+ "v24@?0q8@\"NSString\"16"
- "19:39:25"
- "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreLocationFramework/Oscar/Math/CMFactoredMatrix.h, line 242,invalid col %zu > %zu."
- "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 73,invalid col %zu > %zu."
- "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 80,invalid col %zu > %zu."
- "Assertion failed: col > row, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreLocationFramework/Oscar/Math/CMFactoredMatrix.h, line 243,invalid element %zu <= %zu."
- "Assertion failed: i < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreLocationFramework/Oscar/Math/CMVector.h, line 299,invalid index %zu >= %zu."
- "Assertion failed: i < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreLocationFramework/Oscar/Math/CMVector.h, line 305,invalid index %zu >= %zu."
- "Assertion failed: ldx < M*N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 86,invalid element %zu >= %zu."
- "Assertion failed: row < M, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 72,invalid row %zu > %zu."
- "Assertion failed: row < M, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 79,invalid row %zu > %zu."
- "Jul 11 2026"
- "T CMVector<double, 2>::operator[](const size_t) const [T = double, N = 2]"
- "[Umeyama]:problem is infeasible"
```
