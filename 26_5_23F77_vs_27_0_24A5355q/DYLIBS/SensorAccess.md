## SensorAccess

> `/System/Library/PrivateFrameworks/SensorAccess.framework/SensorAccess`

```diff

-19.120.2.0.0
-  __TEXT.__text: 0x1854
-  __TEXT.__auth_stubs: 0x440
-  __TEXT.__objc_methlist: 0xc8
-  __TEXT.__const: 0x252
-  __TEXT.__cstring: 0x2b4
-  __TEXT.__swift5_typeref: 0x56
+22.0.0.0.0
+  __TEXT.__text: 0x2dc0
+  __TEXT.__objc_methlist: 0x15c
+  __TEXT.__const: 0x262
+  __TEXT.__cstring: 0x544
+  __TEXT.__swift5_typeref: 0x6a
   __TEXT.__swift5_reflstr: 0x9
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__constg_swiftt: 0x64
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__oslogstring: 0xa9
+  __TEXT.__swift5_capture: 0x40
+  __TEXT.__oslogstring: 0xf4
   __TEXT.__swift5_proto: 0x1c
   __TEXT.__swift5_types: 0x8
   __TEXT.__swift5_fieldmd: 0x10
-  __TEXT.__unwind_info: 0x120
-  __TEXT.__eh_frame: 0x80
-  __TEXT.__objc_classname: 0x66
-  __TEXT.__objc_methname: 0x23e
-  __TEXT.__objc_methtype: 0x4f
-  __TEXT.__objc_stubs: 0x120
-  __DATA_CONST.__got: 0x68
+  __TEXT.__unwind_info: 0x188
+  __TEXT.__eh_frame: 0xf8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x38
-  __DATA_CONST.__objc_classlist: 0x18
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x68
-  __AUTH_CONST.__auth_got: 0x228
-  __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__objc_const: 0x1f8
-  __AUTH.__objc_data: 0xb8
+  __DATA_CONST.__objc_selrefs: 0xb8
+  __DATA_CONST.__got: 0x88
+  __AUTH_CONST.__const: 0x70
+  __AUTH_CONST.__objc_const: 0x2f0
+  __AUTH_CONST.__auth_got: 0x310
+  __AUTH.__objc_data: 0x100
   __AUTH.__data: 0xc0
-  __DATA.__data: 0x88
+  __DATA.__data: 0x98
   __DATA.__bss: 0x380
-  __DATA_DIRTY.__objc_data: 0x28
-  __DATA_DIRTY.__data: 0x28
+  __DATA_DIRTY.__objc_data: 0x50
+  __DATA_DIRTY.__data: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/EXDisplayPipe.framework/EXDisplayPipe
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 80655402-AE26-33D2-9367-FB57D4FE5D52
-  Functions: 63
-  Symbols:   114
-  CStrings:  52
+  UUID: D24C0AAB-3A9C-34FE-A218-1701852A6E39
+  Functions: 103
+  Symbols:   161
+  CStrings:  42
 
Symbols:
+ _EXDisplayPipeClose
+ _EXDisplayPipeGetSCASessionHealth
+ _EXDisplayPipeOpen
+ _OBJC_CLASS_$_SensorAccessIndicatorHealth
+ _OBJC_METACLASS_$_SensorAccessIndicatorHealth
+ __DATA_SensorAccessIndicatorHealth
+ __INSTANCE_METHODS_SensorAccessIndicatorHealth
+ __IVARS_SensorAccessIndicatorHealth
+ __METACLASS_DATA_SensorAccessIndicatorHealth
+ __PROPERTIES_SensorAccessIndicatorHealth
+ ___swift__destructor
+ ___swift_destroy_boxed_opaque_existential_0
+ __swiftImmortalRefCount
+ __swift_stdlib_malloc_size
+ __swift_stdlib_reportUnimplementedInitializer
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_msgSend$healthCheckType
+ _objc_msgSend$healthCheckTypeDescriptionWithHealthCheckType:
+ _objc_msgSend$indicatorHealthy
+ _objc_msgSend$indicatorType
+ _objc_msgSend$indicatorTypeDescriptionWithIndicatorType:
+ _objc_msgSend$initWithIndicatorType:healthCheckType:
+ _objc_msgSend$setIndicatorHealthy:
+ _objc_release_x23
+ _objc_release_x8
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x23
+ _swift_allocObject
+ _swift_bridgeObjectRelease_n
+ _swift_deallocObject
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x22
+ _swift_release_x24
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x28
+ _swift_release_x8
+ _swift_retain_x20
+ _swift_retain_x24
+ _swift_retain_x26
+ _swift_retain_x8
+ _symbolic _____ s6UInt64V
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
- _objc_release_x24
- _objc_retain_x20
- _objc_retain_x24
CStrings:
+ "Camera indicator"
+ "Face ID delayed indicator"
+ "Face ID indicator"
+ "Health check type: "
+ "Indicator healthy: "
+ "Indicator type: "
+ "Microphone Alternate indicator"
+ "Microphone indicator"
+ "SensorAccess.SensorAccessIndicatorHealth"
+ "Unknown health check type"
+ "Unknown indicator type"
+ "init()"
+ "isIndicatorHealthy"
+ "isIndicatorHealthyThrows SecureIndicatorPolicyNotSupported"
+ "isIndicatorHealthyThrows invalidArgument for healthCheckType"
+ "performHealthCheck EXDP status 0b%s"
+ "performHealthCheck EXDisplayPipeGetSCASessionHealth failed"
+ "performHealthCheck Unable to open EXDisplayPipe connection"
+ "performHealthCheck result - %@"
- ".cxx_destruct"
- "@16@0:8"
- "@24@0:8^@16"
- "@40@0:8Q16Q24Q32"
- "B16@0:8"
- "Q"
- "Q16@0:8"
- "SensorAccessDuration"
- "T@\"NSString\",N,R"
- "TQ,N,VremainingCameraDurationNanoSeconds"
- "TQ,N,VremainingFaceIDDurationNanoSeconds"
- "TQ,N,VremainingMicrophoneDurationNanoSeconds"
- "_TtC12SensorAccess17SensorAccessUtils"
- "dealloc"
- "description"
- "getRemainingTimeThrowsAndReturnError:"
- "init"
- "init:::"
- "logger"
- "remainingCameraDurationNanoSeconds"
- "remainingFaceIDDurationNanoSeconds"
- "remainingMicrophoneDurationNanoSeconds"
- "secureIndicatorPolicyEnforced"
- "setRemainingCameraDurationNanoSeconds:"
- "setRemainingFaceIDDurationNanoSeconds:"
- "setRemainingMicrophoneDurationNanoSeconds:"
- "v16@0:8"
- "v24@0:8Q16"

```
