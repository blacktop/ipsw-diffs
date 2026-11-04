## IOKit

> `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`

```diff

-100288.40.8.0.1
-  __TEXT.__text: 0xa1d30
+100288.60.4.0.0
+  __TEXT.__text: 0xa1d00
   __TEXT.__objc_methlist: 0x150
   __TEXT.__const: 0x104bc
-  __TEXT.__oslogstring: 0x58c8
-  __TEXT.__cstring: 0xbea3
+  __TEXT.__oslogstring: 0x590b
+  __TEXT.__cstring: 0xbe60
   __TEXT.__unwind_info: 0x30f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/libenergytrace.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 3586
-  Symbols:   3969
-  CStrings:  2601
+  Functions: 3590
+  Symbols:   3970
+  CStrings:  2597
 
Symbols:
+ _IOHIDEventSystemConnectionGetCaller
Functions:
~ _OUTLINED_FUNCTION_14 : 24 -> 12
+ _OUTLINED_FUNCTION_4
~ _OUTLINED_FUNCTION_17 : 12 -> 20
~ _OUTLINED_FUNCTION_17 : 20 -> 12
~ _OUTLINED_FUNCTION_17 : 12 -> 16
- _OUTLINED_FUNCTION_17
~ _OUTLINED_FUNCTION_8 : 16 -> 12
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_9
~ __IOHIDServiceCopyPropertyForClient : 716 -> 764
~ _OUTLINED_FUNCTION_16 : 12 -> 24
~ _OUTLINED_FUNCTION_4 : 24 -> 16
~ _OUTLINED_FUNCTION_4 : 16 -> 20
~ _OUTLINED_FUNCTION_4 : 20 -> 12
~ _OUTLINED_FUNCTION_4 : 12 -> 20
~ _OUTLINED_FUNCTION_4 : 20 -> 16
~ _OUTLINED_FUNCTION_4 : 16 -> 12
- _OUTLINED_FUNCTION_4
~ _OUTLINED_FUNCTION_11 : 12 -> 20
+ _OUTLINED_FUNCTION_11
~ _OUTLINED_FUNCTION_12 : 12 -> 16
~ _OUTLINED_FUNCTION_12 : 16 -> 12
- _OUTLINED_FUNCTION_12
~ _OUTLINED_FUNCTION_15 : 20 -> 16
~ _OUTLINED_FUNCTION_15 : 12 -> 20
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_18
~ _OUTLINED_FUNCTION_10 : 20 -> 16
- _OUTLINED_FUNCTION_10
~ ___IOHIDEventTypeDescriptorAmbientLightSensor : 440 -> 256
+ _IOHIDEventSystemConnectionGetCaller
~ ___IOHIDServiceInit.cold.1 : 148 -> 144
+ __IOHIDServiceCopyPropertyForClient.cold.1
~ ___IOHIDServiceHandleCancelTimerTimeout.cold.2 : 100 -> 88
~ _____IOHIDServiceHandleCancelTimerTimeout_block_invoke.cold.1 : 92 -> 84
~ _IOHIDServiceConformsTo.cold.1 : 112 -> 108
CStrings:
+ "0x%llx: Denied serial number read for unentitled client %{public}@"
+ "OSKEXT_BUILD_DATE 23:19:39 Oct 22 2026"
- "ColorComponent0:"
- "ColorComponent1:"
- "ColorComponent2:"
- "ColorSpace:"
- "OSKEXT_BUILD_DATE 15:35:00 Oct  3 2026"
- "XYZ"
```
