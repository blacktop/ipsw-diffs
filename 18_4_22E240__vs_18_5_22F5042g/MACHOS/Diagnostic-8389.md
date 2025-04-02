## Diagnostic-8389

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8389.appex/Diagnostic-8389`

```diff

-820.100.58.0.0
-  __TEXT.__text: 0x1ddcc
-  __TEXT.__auth_stubs: 0xcc0
-  __TEXT.__objc_methlist: 0x4fc
-  __TEXT.__cstring: 0x14dd
+820.120.55.0.0
+  __TEXT.__text: 0x20044
+  __TEXT.__auth_stubs: 0xd60
+  __TEXT.__objc_stubs: 0x180
+  __TEXT.__objc_methlist: 0x534
+  __TEXT.__cstring: 0x158d
+  __TEXT.__objc_classname: 0x12e
+  __TEXT.__objc_methname: 0xe15
+  __TEXT.__objc_methtype: 0x6bb
   __TEXT.__const: 0x3428
-  __TEXT.__constg_swiftt: 0xd88
-  __TEXT.__swift5_typeref: 0xb93
+  __TEXT.__constg_swiftt: 0xda0
+  __TEXT.__swift5_typeref: 0xbb5
   __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_reflstr: 0x673
+  __TEXT.__swift5_reflstr: 0x682
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x340
   __TEXT.__swift5_types: 0xfc
-  __TEXT.__objc_classname: 0x11c
-  __TEXT.__objc_methname: 0xccc
-  __TEXT.__objc_methtype: 0x68c
-  __TEXT.__swift5_fieldmd: 0xb88
+  __TEXT.__swift5_fieldmd: 0xb94
   __TEXT.__swift5_capture: 0xe4
   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x8b0
-  __TEXT.__eh_frame: 0x858
-  __DATA_CONST.__auth_got: 0x660
-  __DATA_CONST.__got: 0x1f8
+  __TEXT.__unwind_info: 0x8d8
+  __TEXT.__eh_frame: 0x8a0
+  __DATA_CONST.__auth_got: 0x6b8
+  __DATA_CONST.__got: 0x228
   __DATA_CONST.__auth_ptr: 0x198
-  __DATA_CONST.__const: 0x2120
-  __DATA_CONST.__objc_classlist: 0x18
+  __DATA_CONST.__const: 0x2140
+  __DATA_CONST.__cfstring: 0x1c0
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x78
-  __DATA.__objc_const: 0xa08
-  __DATA.__objc_selrefs: 0x410
-  __DATA.__objc_data: 0x728
+  __DATA_CONST.__objc_intobj: 0x48
+  __DATA.__objc_const: 0xab8
+  __DATA.__objc_selrefs: 0x480
+  __DATA.__objc_data: 0x798
   __DATA.__data: 0x11d0
   __DATA.__bss: 0x6780
-  __DATA.__common: 0x30
+  __DATA.__common: 0x38
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 845
-  Symbols:   150
-  CStrings:  365
+  Functions: 858
+  Symbols:   169
+  CStrings:  399
 
Symbols:
+ _MGGetBoolAnswer
+ _OBJC_CLASS_$_DAExclavesSupport
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_METACLASS_$_DAExclavesSupport
+ ___CFConstantStringClassReference
+ ___kCFBooleanFalse
+ ___kCFBooleanTrue
+ _exclaves_sensor_create
+ _exclaves_sensor_status
+ _mach_port_deallocate
+ _mach_task_self_
+ _objc_alloc_init
+ _objc_autoreleaseReturnValue
+ _objc_claimAutoreleasedReturnValue
+ _objc_enumerationMutation
+ _objc_retainAutorelease
CStrings:
+ "@20@0:8I16"
+ "@24@0:8@16"
+ "@24@0:8Q16"
+ "@32@0:8@16@24"
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
+ "countByEnumeratingWithState:objects:count:"
+ "data"
+ "denied"
+ "dictionaryWithObjects:forKeys:count:"
+ "exclavesStatus"
+ "exclavesStatusForSensors:"
+ "faceid"
+ "isEqualToNumber:"
+ "isEqualToString:"
+ "mic"
+ "objectForKeyedSubscript:"
+ "pending"
+ "q"
+ "setObject:forKeyedSubscript:"
+ "supported"
+ "testResultOverrideForExclavesStatus:originalResult:"
+ "unknown"

```
