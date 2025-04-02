## Diagnostic-8246

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8246.appex/Diagnostic-8246`

```diff

-820.100.58.0.0
-  __TEXT.__text: 0x3be4
-  __TEXT.__auth_stubs: 0x290
-  __TEXT.__objc_stubs: 0x1360
-  __TEXT.__objc_methlist: 0x5cc
+820.120.55.0.0
+  __TEXT.__text: 0x4298
+  __TEXT.__auth_stubs: 0x320
+  __TEXT.__objc_stubs: 0x1500
+  __TEXT.__objc_methlist: 0x61c
   __TEXT.__const: 0x50
-  __TEXT.__objc_methname: 0x14f9
-  __TEXT.__cstring: 0x87
-  __TEXT.__objc_classname: 0xa4
-  __TEXT.__objc_methtype: 0x35c
+  __TEXT.__objc_methname: 0x162d
+  __TEXT.__cstring: 0x131
+  __TEXT.__objc_classname: 0xb6
+  __TEXT.__objc_methtype: 0x39b
+  __TEXT.__gcc_except_tab: 0x70
   __TEXT.__oslogstring: 0x39e
-  __TEXT.__unwind_info: 0xf8
-  __DATA_CONST.__auth_got: 0x150
-  __DATA_CONST.__got: 0x1b8
-  __DATA_CONST.__const: 0xe8
-  __DATA_CONST.__cfstring: 0x140
-  __DATA_CONST.__objc_classlist: 0x18
+  __TEXT.__unwind_info: 0x120
+  __DATA_CONST.__auth_got: 0x1a0
+  __DATA_CONST.__got: 0x1d0
+  __DATA_CONST.__const: 0x110
+  __DATA_CONST.__cfstring: 0x2e0
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__objc_intobj: 0xc0
-  __DATA.__objc_const: 0x918
-  __DATA.__objc_selrefs: 0x680
-  __DATA.__objc_ivar: 0x6c
-  __DATA.__objc_data: 0xf0
+  __DATA_CONST.__objc_intobj: 0x108
+  __DATA.__objc_const: 0x9d8
+  __DATA.__objc_selrefs: 0x6e0
+  __DATA.__objc_ivar: 0x70
+  __DATA.__objc_data: 0x140
   __DATA.__data: 0x180
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 105
-  Symbols:   114
-  CStrings:  362
+  Functions: 111
+  Symbols:   129
+  CStrings:  395
 
Symbols:
+ _MGGetBoolAnswer
+ _OBJC_CLASS_$_DAExclavesSupport
+ _OBJC_METACLASS_$_DAExclavesSupport
+ __Unwind_Resume
+ ___kCFBooleanFalse
+ ___kCFBooleanTrue
+ ___objc_personality_v0
+ _exclaves_sensor_create
+ _exclaves_sensor_status
+ _mach_port_deallocate
+ _mach_task_self_
+ _objc_copyWeak
+ _objc_initWeak
+ _objc_release_x28
+ _objc_retain
CStrings:
+ "\x11\x19"
+ "@\"NSDictionary\""
+ "@20@0:8I16"
+ "@24@0:8@16"
+ "@24@0:8Q16"
+ "@32@0:8@16@24"
+ "DAExclavesSupport"
+ "ExclaveCapability"
+ "T@\"NSDictionary\",&,N,V_exclavesStatus"
+ "_eicStatusCheck:"
+ "_exclavesStatus"
+ "_stringForSensorStatus:"
+ "allowed"
+ "cString"
+ "com.apple.sensors.cam"
+ "com.apple.sensors.cam_alt_faceid"
+ "com.apple.sensors.mic"
+ "control"
+ "copy"
+ "denied"
+ "exclavesStatus"
+ "exclavesStatusForSensors:"
+ "faceid"
+ "isEqualToNumber:"
+ "isEqualToString:"
+ "mic"
+ "objectForKeyedSubscript:"
+ "pending"
+ "setExclavesStatus:"
+ "setObject:forKeyedSubscript:"
+ "supported"
+ "testResultOverrideForExclavesStatus:originalResult:"
+ "unknown"
- "\x11\x18"

```
