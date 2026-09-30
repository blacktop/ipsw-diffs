## CentauriBetaPatchBay

> `/System/Library/PrivateFrameworks/CentauriBetaPatchBay.framework/CentauriBetaPatchBay`

```diff

-1.542.0.0.0
-  __TEXT.__text: 0x850 sha256:d000726ce9b61993d3071fe8f2af96fd960bc7b59adf4ecef4616ab0cfac7de5
-  __TEXT.__auth_stubs: 0x140 sha256:f67b4617f0a631f71db3cbe192d49b57c8d288956266c20bddf8105cc194b075
-  __TEXT.__const: 0x20 sha256:edb9c03542e4b616c23b55d2e77734aeede6718d694c8f5ce29db7c5fdae7ef6
-  __TEXT.__cstring: 0x92 sha256:ac44f7bfcf4b655cda09995e55dcce0d1da1e8ad728521c9a3a6e59b4450ea9e
-  __TEXT.__oslogstring: 0x13c sha256:c635c639a34193763d323b043dd7a645627f35a596f1ef36fdfef441af986373
-  __TEXT.__unwind_info: 0x78 sha256:535c4aad96110af5f0e7a1a725e463e5d144ba6d80369418736a4652e60dacce
-  __DATA_CONST.__got: 0x20 sha256:66687aadf862bd776c8fc18b8e9f8e20089714856ee233b3902a591d0d5f2925
-  __AUTH_CONST.__auth_got: 0xa0 sha256:b393978842a0fa3d3e1470196f098f473f9678e72463cb65ec4ab5581856c2e4
-  __AUTH_CONST.__cfstring: 0x20 sha256:ce4586774bbe2c37033be0a83d860fc6cdad460fe7aa1b5c53b4069035a16562
+26.64.4.1.0
+  __TEXT.__text: 0xe48 sha256:981f732e659fe044a7c177196c6ed877fbb8cdf855f2af92116a6d7e8eeb06a4
+  __TEXT.__const: 0x20 sha256:383132bb323f5eb374468e1d6f9a6aa6ef1227c6cc6cce8519302e519d47891b
+  __TEXT.__cstring: 0x10a sha256:32d052bf376da26384bdffa815e09a060c7387eba18aff026595e8f7ee63cec8
+  __TEXT.__oslogstring: 0x24a sha256:b9755e8aa05c6a56d63d8ee747738caadad321fe4e3b3521baed07701c5a8106
+  __TEXT.__unwind_info: 0x90 sha256:93c8d1291884a014183777078d5af28430fc15e47ba42a85dad1bb19da1628e1
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x30 sha256:c79969ff4ab4175c5564bcd6335f1c44fc7081a2e11f1033d7c2c909d3eac08e
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__cfstring: 0x60 sha256:6faa582b222872fe30158033b381cf01a35827cfbf5b720753b21e875e53550d
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
