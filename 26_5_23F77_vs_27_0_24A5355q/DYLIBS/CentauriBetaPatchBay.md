## CentauriBetaPatchBay

> `/System/Library/PrivateFrameworks/CentauriBetaPatchBay.framework/CentauriBetaPatchBay`

```diff

-1.542.0.0.0
-  __TEXT.__text: 0x850
-  __TEXT.__auth_stubs: 0x140
+26.64.4.1.0
+  __TEXT.__text: 0xe48
   __TEXT.__const: 0x20
-  __TEXT.__cstring: 0x92
-  __TEXT.__oslogstring: 0x13c
-  __TEXT.__unwind_info: 0x78
-  __DATA_CONST.__got: 0x20
-  __AUTH_CONST.__auth_got: 0xa0
-  __AUTH_CONST.__cfstring: 0x20
+  __TEXT.__cstring: 0x10a
+  __TEXT.__oslogstring: 0x24a
+  __TEXT.__unwind_info: 0x90
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x30
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__cfstring: 0x60
+  __AUTH_CONST.__auth_got: 0x0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
-  UUID: 6EC0E8EE-D777-3C8E-A7C5-81F77C3EA837
-  Functions: 17
-  Symbols:   58
-  CStrings:  19
+  UUID: DC44FC24-36EF-327A-9442-F72A3DA1A7A7
+  Functions: 28
+  Symbols:   88
+  CStrings:  37
 
Symbols:
+ _CFDataGetBytePtr
+ _free
+ _getAuxSimulationBootArg
+ _getAuxSimulationBootArg.cold.1
+ _getAuxSimulationBootArg.cold.2
+ _getGpioConfigType
+ _getHostModelName
+ _getHostModelName.cold.1
+ _getHostModelName.cold.2
+ _getHostModelName.cold.3
+ _getHostModelName.cold.4
+ _getHostModelName.cold.5
+ _getHostModelType
+ _getHostModelType.modelPrefixes
+ _getHwLogsConfig
+ _getStringFromNVRAM
+ _getStringFromNVRAM.cold.1
+ _getStringFromNVRAM.cold.2
+ _getStringFromNVRAM.cold.3
+ _strlen
+ _strncmp
+ _strtok
+ _strtoul
+ _sysctlbyname_get_data_np
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- _getCoexSpmiDisable.cold.1
- _getCoexSpmiDisable.cold.2
- _getCoexSpmiDisable.cold.3
CStrings:
+ " "
+ "%s: arg not found"
+ "%s: data property string value: %s\n"
+ "%s: failed to get boot-args"
+ "%s: property length is bigger than buffer size"
+ "%s: property not found"
+ "%s: property wrong type"
+ "%s: version=%d, hostPlatformName=%s, isDevBoard=%d, coexSpmiExists=%d, coexSpmiDisable=%d, hostModelName=%s, hostModelType=%d, gpioConfigType=%d, auxSimulation=%d, hwLogsConfig=0x%04X"
+ "Mac"
+ "bt-hwlogs-config"
+ "getAuxSimulationBootArg"
+ "getDataFromIOReg"
+ "iPad"
+ "iPhone"
+ "kern.bootargs"
+ "model"
+ "proxima-aux-simulation="
- "%s: version=%d, hostPlatformName=%s, isDevBoard=%d, coexSpmiExists=%d, coexSpmiDisable=%d"

```
