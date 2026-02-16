## CentauriAlphaPatchBay

> `/System/Library/PrivateFrameworks/CentauriAlphaPatchBay.framework/CentauriAlphaPatchBay`

```diff

-71.13.34.0.0
-  __TEXT.__text: 0x1fc
-  __TEXT.__auth_stubs: 0x60
+72.29.700.0.0
+  __TEXT.__text: 0xf34
+  __TEXT.__auth_stubs: 0x100
   __TEXT.__const: 0x10
-  __TEXT.__oslogstring: 0x35
-  __TEXT.__cstring: 0x1e
-  __TEXT.__unwind_info: 0x60
-  __DATA_CONST.__got: 0x18
-  __AUTH_CONST.__auth_got: 0x30
+  __TEXT.__cstring: 0x12e
+  __TEXT.__oslogstring: 0x1cf
+  __TEXT.__unwind_info: 0x78
+  __DATA_CONST.__got: 0x20
+  __AUTH_CONST.__auth_got: 0x80
+  __AUTH_CONST.__cfstring: 0x100
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
-  UUID: E08D7D56-16A7-31D3-82ED-0DE5F23E3989
-  Functions: 2
-  Symbols:   12
-  CStrings:  3
+  UUID: 0DB89872-6312-3D2B-ABF4-D6251FA066F7
+  Functions: 26
+  Symbols:   72
+  CStrings:  35
 
Symbols:
+ _CFDataGetBytePtr
+ _CFDataGetTypeID
+ _CFGetTypeID
+ _CFRelease
+ _CFStringGetCString
+ _CFStringGetSystemEncoding
+ _CentauriAlphaPatchBayCopyData.cold.2
+ _IOObjectRelease
+ _IORegistryEntryCreateCFProperty
+ _IOServiceGetMatchingService
+ _IOServiceNameMatching
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ ___CFConstantStringClassReference
+ _getFloatFromIOReg
+ _getFloatFromIOReg.cold.1
+ _getFloatFromIOReg.cold.2
+ _getFloatFromIOReg.cold.3
+ _getFloatFromIOReg.cold.4
+ _getTableFromIOReg
+ _getTableFromIOReg.cold.1
+ _getTableFromIOReg.cold.2
+ _getTableFromIOReg.cold.3
+ _getTableFromIOReg.cold.4
+ _getTableFromIOReg.cold.5
+ _getTableFromIOReg.cold.6
+ _getUint8FromIOReg
+ _getUint8FromIOReg.cold.1
+ _getUint8FromIOReg.cold.2
+ _getUint8FromIOReg.cold.3
+ _getUint8FromIOReg.cold.4
+ _getUint8FromIOReg.cold.5
+ _kIOMainPortDefault
CStrings:
+ "%s: failed to create matching dict"
+ "%s: failed to load all TVPM data"
+ "%s: number bigger than UINT8_MAX"
+ "%s: property %s found"
+ "%s: property has wrong type"
+ "%s: property length is bigger than buffer size"
+ "%s: property length is not float_t size"
+ "%s: property length is not uint32_t size"
+ "%s: property not found"
+ "%s: property not found or wrong type"
+ "%s: service not found"
+ "%s: table cell with number bigger than UINT8_MAX"
+ "centauri"
+ "getFloatFromIOReg"
+ "getTableFromIOReg"
+ "getUint8FromIOReg"
+ "wifi_duty_cycle_table"
+ "wifi_duty_cycle_temp_threshold"
+ "wifi_power_bo_2g_table"
+ "wifi_power_bo_2g_temp_threshold"
+ "wifi_power_bo_5g_table"
+ "wifi_power_bo_5g_temp_threshold"
+ "wifi_volt_hi_threshold"
+ "wifi_volt_lo_threshold"

```
