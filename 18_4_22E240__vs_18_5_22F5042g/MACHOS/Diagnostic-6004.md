## Diagnostic-6004

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6004.appex/Diagnostic-6004`

```diff

-820.100.58.0.0
-  __TEXT.__text: 0x12144
-  __TEXT.__auth_stubs: 0xbe0
-  __TEXT.__objc_stubs: 0x160
-  __TEXT.__objc_methlist: 0x364
-  __TEXT.__cstring: 0xef9
-  __TEXT.__objc_methname: 0x8f6
-  __TEXT.__objc_classname: 0x45
-  __TEXT.__objc_methtype: 0xce
+820.120.55.0.0
+  __TEXT.__text: 0x135c8
+  __TEXT.__auth_stubs: 0xc60
+  __TEXT.__objc_stubs: 0x2a0
+  __TEXT.__objc_methlist: 0x39c
+  __TEXT.__cstring: 0xfb9
+  __TEXT.__objc_methname: 0x9fe
+  __TEXT.__objc_classname: 0x57
+  __TEXT.__objc_methtype: 0xfd
   __TEXT.__const: 0x9c8
-  __TEXT.__swift5_typeref: 0x149a
-  __TEXT.__constg_swiftt: 0x664
-  __TEXT.__swift5_reflstr: 0x5a3
-  __TEXT.__swift5_fieldmd: 0x3ac
+  __TEXT.__swift5_typeref: 0x14bc
+  __TEXT.__constg_swiftt: 0x67c
+  __TEXT.__swift5_reflstr: 0x5b3
+  __TEXT.__swift5_fieldmd: 0x3b8
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_capture: 0x264
   __TEXT.__oslogstring: 0x9e
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x34
-  __TEXT.__unwind_info: 0x460
-  __TEXT.__eh_frame: 0x120
-  __DATA_CONST.__auth_got: 0x5f8
-  __DATA_CONST.__got: 0x260
+  __TEXT.__unwind_info: 0x480
+  __TEXT.__eh_frame: 0x168
+  __DATA_CONST.__auth_got: 0x638
+  __DATA_CONST.__got: 0x290
   __DATA_CONST.__auth_ptr: 0x2d8
-  __DATA_CONST.__const: 0xe00
-  __DATA_CONST.__cfstring: 0x20
-  __DATA_CONST.__objc_classlist: 0x50
+  __DATA_CONST.__const: 0xe20
+  __DATA_CONST.__cfstring: 0x1e0
+  __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA.__objc_const: 0xa28
-  __DATA.__objc_selrefs: 0x398
-  __DATA.__objc_data: 0x6d8
-  __DATA.__data: 0xae8
+  __DATA_CONST.__objc_intobj: 0x48
+  __DATA.__objc_const: 0xad8
+  __DATA.__objc_selrefs: 0x3f0
+  __DATA.__objc_data: 0x728
+  __DATA.__data: 0xb10
   __DATA.__bss: 0x400
   __DATA.__common: 0x30
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 452
-  Symbols:   160
-  CStrings:  258
+  Functions: 467
+  Symbols:   176
+  CStrings:  290
 
Symbols:
+ _MGGetBoolAnswer
+ _OBJC_CLASS_$_DAExclavesSupport
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_METACLASS_$_DAExclavesSupport
+ ___kCFBooleanFalse
+ ___kCFBooleanTrue
+ _exclaves_sensor_create
+ _exclaves_sensor_status
+ _mach_port_deallocate
+ _mach_task_self_
+ _objc_alloc_init
+ _objc_autoreleaseReturnValue
+ _objc_retainAutorelease
CStrings:
+ "@20@0:8I16"
+ "@24@0:8Q16"
+ "DAExclavesSupport"
+ "ExclaveCapability"
+ "_eicStatusCheck:"
+ "_stringForSensorStatus:"
+ "allowed"
+ "arrayWithObjects:count:"
+ "cString"
+ "camera"
+ "com.apple.sensors.cam"
+ "com.apple.sensors.cam_alt_faceid"
+ "com.apple.sensors.mic"
+ "control"
+ "copy"
+ "denied"
+ "dictionaryWithObjects:forKeys:count:"
+ "exclavesData"
+ "exclavesStatus"
+ "exclavesStatusForSensors:"
+ "faceid"
+ "isEqualToNumber:"
+ "mic"
+ "objectForKeyedSubscript:"
+ "pending"
+ "q"
+ "setObject:forKeyedSubscript:"
+ "supported"
+ "testResultOverrideForExclavesStatus:originalResult:"
+ "unknown"

```
