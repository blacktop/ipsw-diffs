## batteryintelligenced

> `/usr/libexec/batteryintelligenced`

```diff

-174.0.0.0.0
-  __TEXT.__text: 0x30b80
+175.0.0.0.0
+  __TEXT.__text: 0x30ee0
   __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__objc_stubs: 0x3660
+  __TEXT.__objc_stubs: 0x3680
   __TEXT.__objc_methlist: 0x1f8c
-  __TEXT.__cstring: 0x29b3
+  __TEXT.__cstring: 0x29da
   __TEXT.__objc_classname: 0x5d9
   __TEXT.__objc_methtype: 0x771
   __TEXT.__const: 0x1f8
   __TEXT.__objc_methname: 0x42b2
-  __TEXT.__oslogstring: 0x54bb
+  __TEXT.__oslogstring: 0x55e1
   __TEXT.__gcc_except_tab: 0x278
   __TEXT.__unwind_info: 0x890
   __DATA_CONST.__auth_got: 0x468
   __DATA_CONST.__got: 0x230
   __DATA_CONST.__const: 0x9a8
-  __DATA_CONST.__cfstring: 0x2ee0
+  __DATA_CONST.__cfstring: 0x2f40
   __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x150
-  __DATA_CONST.__objc_arraydata: 0x6a0
-  __DATA_CONST.__objc_arrayobj: 0x480
-  __DATA_CONST.__objc_intobj: 0x840
-  __DATA_CONST.__objc_doubleobj: 0x50
+  __DATA_CONST.__objc_arraydata: 0x6f0
+  __DATA_CONST.__objc_arrayobj: 0x498
+  __DATA_CONST.__objc_intobj: 0x888
+  __DATA_CONST.__objc_doubleobj: 0x40
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0x5038
   __DATA.__objc_selrefs: 0x1088
   __DATA.__objc_ivar: 0x23c
   __DATA.__objc_data: 0xe60
-  __DATA.__data: 0x2e0
+  __DATA.__data: 0x2e8
   __DATA.__bss: 0x1d8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreML.framework/CoreML

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ACD4E385-D214-310D-9FE3-31439F4349BB
+  UUID: F7FF7E76-277D-3BEC-99C6-074EC5E0B1F7
   Functions: 993
   Symbols:   226
-  CStrings:  2170
+  CStrings:  2178
 
CStrings:
+ "Could not load battery_analysis_tt80_model_xtgs7ejyqa.mlmodelc in the bundle resource"
+ "Device does not contain power telemetry table. Substituting default (median) values for system power (= %@ mW) and system load (%@ mW) instead (model version = %@)"
+ "Device does not contain power telemetry table. Substituting with default sentinel value (%@) for system power and system load (model version = %@)"
+ "Loaded unsupported model version from trial (%@). Defaulting to model version %@ at %@."
+ "SystemLoad"
+ "battery_analysis_tt80_model_xtgs7ejyqa"
+ "battery_analysis_tt80_model_xtgs7ejyqaInput"
+ "battery_analysis_tt80_model_xtgs7ejyqaOutput"
+ "curr_system_load"
+ "systemLoad"
+ "xtgs7ejyqa"
- "Could not load battery_analysis_tt80_model_ypt4vmy8c3.mlmodelc in the bundle resource"
- "Device does not contain power telemetry table. Using default (median) system power value instead: %@ mW."
- "battery_analysis_tt80_model_ypt4vmy8c3"
- "battery_analysis_tt80_model_ypt4vmy8c3Input"
- "battery_analysis_tt80_model_ypt4vmy8c3Output"
- "ypt4vmy8c3"

```
