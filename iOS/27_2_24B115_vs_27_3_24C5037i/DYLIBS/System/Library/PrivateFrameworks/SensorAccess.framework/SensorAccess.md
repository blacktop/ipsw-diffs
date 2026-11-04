## SensorAccess

> `/System/Library/PrivateFrameworks/SensorAccess.framework/SensorAccess`

```diff

-27.0.0.0.0
-  __TEXT.__text: 0x3388
-  __TEXT.__objc_methlist: 0x1b4
-  __TEXT.__const: 0x302
-  __TEXT.__constg_swiftt: 0x90
-  __TEXT.__swift5_typeref: 0x76
+29.60.1.0.0
+  __TEXT.__text: 0x418c
+  __TEXT.__objc_methlist: 0x234
+  __TEXT.__const: 0x342
+  __TEXT.__cstring: 0x674
+  __TEXT.__constg_swiftt: 0xcc
+  __TEXT.__swift5_typeref: 0x7c
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_reflstr: 0x1b
-  __TEXT.__swift5_fieldmd: 0x2c
+  __TEXT.__swift5_fieldmd: 0x3c
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x24
-  __TEXT.__swift5_types: 0xc
-  __TEXT.__cstring: 0x564
-  __TEXT.__swift5_capture: 0x50
-  __TEXT.__oslogstring: 0x184
-  __TEXT.__unwind_info: 0x208
-  __TEXT.__eh_frame: 0x130
+  __TEXT.__swift5_types: 0x10
+  __TEXT.__swift5_capture: 0x80
+  __TEXT.__oslogstring: 0x291
+  __TEXT.__unwind_info: 0x270
+  __TEXT.__eh_frame: 0x1d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x38
-  __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__const: 0x50
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd8
-  __DATA_CONST.__got: 0xa0
-  __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__objc_const: 0x388
-  __AUTH_CONST.__auth_got: 0x328
-  __AUTH.__objc_data: 0x170
-  __AUTH.__data: 0xe8
-  __DATA.__data: 0xb0
+  __DATA_CONST.__objc_selrefs: 0x130
+  __DATA_CONST.__got: 0xb0
+  __AUTH_CONST.__const: 0xe8
+  __AUTH_CONST.__objc_const: 0x4e0
+  __AUTH_CONST.__auth_got: 0x388
+  __AUTH.__objc_data: 0x1e0
+  __AUTH.__data: 0x1a8
+  __DATA.__data: 0xc8
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 118
-  Symbols:   154
-  CStrings:  46
+  - /usr/lib/swift/libswiftsimd.dylib
+  Functions: 143
+  Symbols:   183
+  CStrings:  59
 
Symbols:
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_SensorAccessChillPillState
+ _OBJC_METACLASS_$_SensorAccessChillPillState
+ __DATA_SensorAccessChillPillState
+ __DATA__TtC12SensorAccess22SensorAccessSteadyTime
+ __INSTANCE_METHODS_SensorAccessChillPillState
+ __IVARS_SensorAccessChillPillState
+ __METACLASS_DATA_SensorAccessChillPillState
+ __METACLASS_DATA__TtC12SensorAccess22SensorAccessSteadyTime
+ __PROPERTIES_SensorAccessChillPillState
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftMetal_$_SensorAccess
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftQuartzCore_$_SensorAccess
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_SensorAccess
+ _exclaves_indicator_chillpill_state
+ _objc_release_x24
+ _objc_release_x26
+ _objc_release_x28
+ _objc_retain_x2
+ _objc_retain_x20
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_retain_x26
+ _swift_release_x23
+ _swift_retain_n
+ _swift_retain_x23
+ _symbolic _____ 12SensorAccess0aB10SteadyTimeC
CStrings:
+ "%{public}s"
+ "Chill pill not in effect"
+ "Chill pill usage %llu ms exceeds budget %llu ms"
+ "Chill pill usage: "
+ "CoreAnimation could not determine the %{public}s deadline"
+ "GetChillPillStateFailed"
+ "GetChillPillStateNotSupported"
+ "GetRemainingSteadyTimeFailed"
+ "GetRemainingSteadyTimeNotSupported"
+ "Remaining %{public}s time %llu ns (curr_time %llu deadline %llu)"
+ "SteadyDeadlineUnknown"
+ "exclaves_indicator_chillpill_state failed with code: %d"
+ "mach_timebase_info failed"
```
