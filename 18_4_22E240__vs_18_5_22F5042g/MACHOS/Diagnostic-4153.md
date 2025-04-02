## Diagnostic-4153

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4153.appex/Diagnostic-4153`

```diff

-820.100.58.0.0
-  __TEXT.__text: 0x7494
-  __TEXT.__auth_stubs: 0x2e0
-  __TEXT.__objc_stubs: 0x2200
-  __TEXT.__objc_methlist: 0xb20
-  __TEXT.__objc_methname: 0x2a72
-  __TEXT.__objc_classname: 0x12c
-  __TEXT.__objc_methtype: 0xbae
+820.120.55.0.0
+  __TEXT.__text: 0x7b3c
+  __TEXT.__auth_stubs: 0x360
+  __TEXT.__objc_stubs: 0x2340
+  __TEXT.__objc_methlist: 0xb70
+  __TEXT.__cstring: 0x332
+  __TEXT.__objc_classname: 0x13e
+  __TEXT.__objc_methtype: 0xbd4
+  __TEXT.__objc_methname: 0x2b80
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x281
+  __TEXT.__gcc_except_tab: 0x7c
   __TEXT.__oslogstring: 0x22e
-  __TEXT.__unwind_info: 0x180
-  __DATA_CONST.__auth_got: 0x178
-  __DATA_CONST.__got: 0x1d0
-  __DATA_CONST.__const: 0x190
-  __DATA_CONST.__cfstring: 0x580
-  __DATA_CONST.__objc_classlist: 0x28
+  __TEXT.__unwind_info: 0x1a0
+  __DATA_CONST.__auth_got: 0x1c0
+  __DATA_CONST.__got: 0x1f0
+  __DATA_CONST.__const: 0x1b8
+  __DATA_CONST.__cfstring: 0x740
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
+  __DATA_CONST.__objc_intobj: 0xc0
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0x1028
-  __DATA.__objc_selrefs: 0xb98
-  __DATA.__objc_ivar: 0xc8
-  __DATA.__objc_data: 0x190
+  __DATA.__objc_const: 0x10e8
+  __DATA.__objc_selrefs: 0xbe0
+  __DATA.__objc_ivar: 0xcc
+  __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x2a0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 180
-  Symbols:   144
-  CStrings:  655
+  Functions: 186
+  Symbols:   159
+  CStrings:  684
 
Symbols:
+ _MGGetBoolAnswer
+ _OBJC_CLASS_$_DAExclavesSupport
+ _OBJC_CLASS_$_NSMutableDictionary
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
+ _objc_retain
CStrings:
+ "\x12\x1f\x02"
+ "@\"NSDictionary\""
+ "@20@0:8I16"
+ "@24@0:8Q16"
+ "DAExclavesSupport"
+ "ExclaveCapability"
+ "T@\"NSDictionary\",&,N,V_exclavesStatus"
+ "_eicStatusCheck:"
+ "_exclavesStatus"
+ "_stringForSensorStatus:"
+ "addEntriesFromDictionary:"
+ "allowed"
+ "cString"
+ "camera"
+ "com.apple.sensors.cam"
+ "com.apple.sensors.cam_alt_faceid"
+ "com.apple.sensors.mic"
+ "control"
+ "denied"
+ "exclavesStatus"
+ "exclavesStatusForSensors:"
+ "faceid"
+ "mic"
+ "pending"
+ "setExclavesStatus:"
+ "setObject:forKeyedSubscript:"
+ "supported"
+ "testResultOverrideForExclavesStatus:originalResult:"
+ "unknown"
- "\x12\x1f\x01"

```
