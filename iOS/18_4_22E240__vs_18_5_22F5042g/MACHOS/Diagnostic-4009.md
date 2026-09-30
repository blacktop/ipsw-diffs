## Diagnostic-4009

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4009.appex/Diagnostic-4009`

```diff

-820.100.58.0.0
-  __TEXT.__text: 0x689c
-  __TEXT.__auth_stubs: 0x630
-  __TEXT.__objc_stubs: 0x1580
-  __TEXT.__objc_methlist: 0xc7c
-  __TEXT.__cstring: 0x98c
+820.120.55.0.0
+  __TEXT.__text: 0x6f68
+  __TEXT.__auth_stubs: 0x660
+  __TEXT.__objc_stubs: 0x16c0
+  __TEXT.__objc_methlist: 0xccc
+  __TEXT.__cstring: 0xa3d
   __TEXT.__const: 0x40
   __TEXT.__gcc_except_tab: 0x188
-  __TEXT.__objc_classname: 0x139
-  __TEXT.__objc_methname: 0x17ce
-  __TEXT.__objc_methtype: 0x6dd
+  __TEXT.__objc_classname: 0x14b
+  __TEXT.__objc_methname: 0x18d0
+  __TEXT.__objc_methtype: 0x70c
   __TEXT.__oslogstring: 0x2dd
-  __TEXT.__unwind_info: 0x270
-  __DATA_CONST.__auth_got: 0x328
-  __DATA_CONST.__got: 0x1a8
-  __DATA_CONST.__const: 0x1f0
-  __DATA_CONST.__cfstring: 0x660
-  __DATA_CONST.__objc_classlist: 0x58
+  __TEXT.__unwind_info: 0x278
+  __DATA_CONST.__auth_got: 0x340
+  __DATA_CONST.__got: 0x1b0
+  __DATA_CONST.__const: 0x210
+  __DATA_CONST.__cfstring: 0x820
+  __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x30
-  __DATA_CONST.__objc_intobj: 0x1b0
+  __DATA_CONST.__objc_intobj: 0x1f8
   __DATA_CONST.__objc_doubleobj: 0x30
-  __DATA.__objc_const: 0x11c0
-  __DATA.__objc_selrefs: 0x6b0
-  __DATA.__objc_ivar: 0xa4
-  __DATA.__objc_data: 0x370
+  __DATA.__objc_const: 0x1280
+  __DATA.__objc_selrefs: 0x6f8
+  __DATA.__objc_ivar: 0xa8
+  __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x308
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 223
-  Symbols:   194
-  CStrings:  514
+  Functions: 229
+  Symbols:   200
+  CStrings:  544
 
Symbols:
+ _OBJC_CLASS_$_DAExclavesSupport
+ _OBJC_METACLASS_$_DAExclavesSupport
+ _exclaves_sensor_create
+ _exclaves_sensor_status
+ _mach_port_deallocate
+ _mach_task_self_
CStrings:
+ "4"
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
+ "isEqualToNumber:"
+ "mic"
+ "pending"
+ "setExclavesStatus:"
+ "supported"
+ "testResultOverrideForExclavesStatus:originalResult:"
+ "unknown"
- "3"

```
