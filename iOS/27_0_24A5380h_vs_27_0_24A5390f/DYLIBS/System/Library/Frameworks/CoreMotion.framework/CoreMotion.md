## CoreMotion

> `/System/Library/Frameworks/CoreMotion.framework/CoreMotion`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-3176.0.0.0.0
-  __TEXT.__text: 0x3ad4c0
-  __TEXT.__objc_methlist: 0xd04c
-  __TEXT.__const: 0xc510
+3183.0.0.0.0
+  __TEXT.__text: 0x3ae150
+  __TEXT.__objc_methlist: 0xd0b4
+  __TEXT.__const: 0xc530
   __TEXT.__swift5_typeref: 0x257
   __TEXT.__swift5_reflstr: 0x2e
   __TEXT.__swift5_assocty: 0x90
   __TEXT.__constg_swiftt: 0xb8
   __TEXT.__swift5_fieldmd: 0x70
   __TEXT.__swift5_capture: 0x40
-  __TEXT.__oslogstring: 0x2d00c
-  __TEXT.__cstring: 0x45640
+  __TEXT.__oslogstring: 0x2d130
+  __TEXT.__cstring: 0x457a3
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0x10
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x18
   __TEXT.__swift_as_cont: 0x30
-  __TEXT.__gcc_except_tab: 0xc9e4
-  __TEXT.__unwind_info: 0xb690
+  __TEXT.__gcc_except_tab: 0xca1c
+  __TEXT.__unwind_info: 0xb6e0
   __TEXT.__eh_frame: 0x178
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3a50
+  __DATA_CONST.__const: 0x3a48
   __DATA_CONST.__objc_classlist: 0x880
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x5440
+  __DATA_CONST.__objc_selrefs: 0x5488
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x770
   __DATA_CONST.__objc_arraydata: 0x240
   __DATA_CONST.__got: 0x7e8
-  __AUTH_CONST.__const: 0x14f98
-  __AUTH_CONST.__cfstring: 0x13540
-  __AUTH_CONST.__objc_const: 0x1c990
+  __AUTH_CONST.__const: 0x14fc0
+  __AUTH_CONST.__cfstring: 0x135c0
+  __AUTH_CONST.__objc_const: 0x1c9f8
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x258
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_floatobj: 0x30
-  __AUTH_CONST.__auth_got: 0x1488
+  __AUTH_CONST.__auth_got: 0x1490
   __AUTH.__objc_data: 0x3f20
   __AUTH.__data: 0x220
   __DATA.__objc_ivar: 0x16d8
   __DATA.__data: 0xde8
   __DATA.__bss: 0x4b0
   __DATA.__common: 0xf8
-  __DATA_DIRTY.__objc_ivar: 0x178
+  __DATA_DIRTY.__objc_ivar: 0x180
   __DATA_DIRTY.__objc_data: 0x15e0
   __DATA_DIRTY.__data: 0x138
   __DATA_DIRTY.__common: 0x89
-  __DATA_DIRTY.__bss: 0x1028
+  __DATA_DIRTY.__bss: 0x1038
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 12347
-  Symbols:   1770
-  CStrings:  11056
+  Functions: 12363
+  Symbols:   1772
+  CStrings:  11072
 
Symbols:
+ _CLPromoteSystemService
+ _dispatch_assert_queue_not$V2
CStrings:
+ "#Spi, CLPromoteSystemService failed"
+ "%@ state=%ld, type=%ld, config=%ld, propertyC=%ld, orientation=%d, @ %f"
+ "%f: Device Stationary?, %s, Orientation, %s, Proximity, %s, AllowInPocket, %s, State, %s"
+ "+[CMWakeGestureManager toConfig:]"
+ "-[CLLocationInternalClient_CoreMotion promoteSystemServiceWithBundlePath:]_block_invoke"
+ "0 in-pocket disallowed"
+ "19:30:32"
+ "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMMatrix.h, line 73,invalid col %zu > %zu."
+ "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMMatrix.h, line 80,invalid col %zu > %zu."
+ "Assertion failed: i < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMVector.h, line 299,invalid index %zu >= %zu."
+ "Assertion failed: i < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMVector.h, line 305,invalid index %zu >= %zu."
+ "Assertion failed: ldx < M*N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMMatrix.h, line 86,invalid element %zu >= %zu."
+ "Assertion failed: row < M, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMMatrix.h, line 72,invalid row %zu > %zu."
+ "Assertion failed: row < M, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMMatrix.h, line 79,invalid row %zu > %zu."
+ "CL: CLPromoteSystemService"
+ "CMWakeGesturePhone.mm"
+ "Device Stationary?, %s, Orientation, %s, Proximity, %s, AllowInPocket, %s"
+ "Jul 11 2026"
+ "SimulateAOP2MotionPlatform"
+ "[%{public}ld][%{public}@][%{public}ld] ==== Updating current suppression event: %{public}@ (%{public}@) @ %{public}f"
+ "[%{public}ld][%{public}@][%{public}ld] Next: %{public}@ (%{public}@) @ %{public}f"
+ "[%{public}ld][%{public}@][%{public}ld] No Transition: %{public}@ (%{public}@) @ %{public}f"
+ "[%{public}ld][%{public}@][%{public}ld] Previous: %{public}@ (%{public}@) @ %{public}f"
+ "[%{public}ld][%{public}@][%{public}ld] Sending to client: %{public}@,now,%{public}f"
+ "[%{public}ld][%{public}@][%{public}ld] Significant user interaction detected"
+ "[%{public}ld][%{public}@][%{public}ld] Starting suppression updates with useViewObstructed,%{public}u,useSmartPowerNap,%{public}u,useWatchPresence,%{public}u,useAlwaysOnViewObstructed,%{public}u,useFacedown,%{public}u"
+ "[%{public}ld][%{public}@][%{public}ld] Stopping suppression updates. Final states: VO: %{public}@ @ %{public}f, SPN: %{public}@ @ %{public}f, DP: %{public}@ @ %{public}f"
+ "gpsAltitudeUncertainty"
+ "imuIndex"
+ "kCMWakeGestureEventCodingKeyConfig"
+ "kCMWakeGestureEventCodingKeyPropertyC"
+ "no"
+ "propertyA0"
+ "propertyA1"
+ "yes"
+ "{\"msg%{public}.0s\":\"CLPromoteSystemService\", \"event\":%{public, location:escape_only}s}"
- "%@ state=%ld, type=%ld, orientation=%d, @ %f"
- "%f: Device Stationary?, %s, Orientation, %s, Proximity, %s, State, %s"
- "21:54:52"
- "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMMatrix.h, line 81,invalid col %zu > %zu."
- "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMMatrix.h, line 88,invalid col %zu > %zu."
- "Assertion failed: i < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMVector.h, line 292,invalid index %zu >= %zu."
- "Assertion failed: i < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMVector.h, line 298,invalid index %zu >= %zu."
- "Assertion failed: ldx < M*N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMMatrix.h, line 94,invalid element %zu >= %zu."
- "Assertion failed: row < M, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMMatrix.h, line 80,invalid row %zu > %zu."
- "Assertion failed: row < M, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreMotionFramework/Oscar/Math/CMMatrix.h, line 87,invalid row %zu > %zu."
- "Device Stationary?, %s, Orientation, %s, Proximity, %s"
- "Jun 27 2026"
- "[%{public}ld][%{public}@] ==== Updating current suppression event: %{public}@ (%{public}@) @ %{public}f"
- "[%{public}ld][%{public}@] Next: %{public}@ (%{public}@) @ %{public}f"
- "[%{public}ld][%{public}@] No Transition: %{public}@ (%{public}@) @ %{public}f"
- "[%{public}ld][%{public}@] Previous: %{public}@ (%{public}@) @ %{public}f"
- "[%{public}ld][%{public}@] Sending to client: %{public}@,now,%{public}f"
- "[%{public}ld][%{public}@] Significant user interaction detected"
- "[%{public}ld][%{public}@] Starting suppression updates with useViewObstructed,%{public}u,useSmartPowerNap,%{public}u,useWatchPresence,%{public}u,useAlwaysOnViewObstructed,%{public}u,useFacedown,%{public}u"
- "[%{public}ld][%{public}@] Stopping suppression updates. Final states: VO: %{public}@ @ %{public}f, SPN: %{public}@ @ %{public}f, DP: %{public}@ @ %{public}f"
```
