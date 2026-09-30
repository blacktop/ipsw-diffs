## Portrait

> `/System/Library/PrivateFrameworks/Portrait.framework/Portrait`

```diff

-560.22.1.0.0
-  __TEXT.__text: 0x88a44
+560.22.2.0.0
+  __TEXT.__text: 0x88b78
   __TEXT.__delay_helper: 0x264
   __TEXT.__objc_methlist: 0x936c
   __TEXT.__const: 0x20a70
   __TEXT.__cstring: 0x4e42
-  __TEXT.__oslogstring: 0x4b3b
+  __TEXT.__oslogstring: 0x4b9a
   __TEXT.__gcc_except_tab: 0x19e0
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0x1e90
+  __TEXT.__unwind_info: 0x1e98
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __AUTH.__objc_data: 0x460
   __DATA.__objc_ivar: 0x1778
   __DATA.__data: 0x7b0
-  __DATA.__bss: 0x234
+  __DATA.__bss: 0x23c
   __DATA_DIRTY.__objc_data: 0x2e90
   __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3717
-  Symbols:   8427
-  CStrings:  1384
+  Functions: 3718
+  Symbols:   8429
+  CStrings:  1385
 
Symbols:
+ ___56+[PTTuningParameters hwModelIDFromFigModelSpecificName:]_block_invoke
+ _hwModelIDFromFigModelSpecificName:.onceToken
Functions:
~ +[PTTuningParameters hwModelIDFromFigModelSpecificName:] : 80 -> 232
+ ___56+[PTTuningParameters hwModelIDFromFigModelSpecificName:]_block_invoke
- _OUTLINED_FUNCTION_2
~ ___60+[PTTuningParameters noiseScaleFactorForHwModelID:sensorID:]_block_invoke.cold.1 : 96 -> 104
+ ___56+[PTTuningParameters hwModelIDFromFigModelSpecificName:]_block_invoke.cold.1
CStrings:
+ "Unknown figModelSpecificName %s - device specific tuning parameters will fall back to defaults"
```
