## WiFiSharing

> `/System/Library/CoreAccessories/PlugIns/Platform/WiFiSharing.platform/WiFiSharing`

```diff

-1139.82.1.0.0
+1147.100.12.0.0
   __TEXT.__text: 0x12dc
   __TEXT.__auth_stubs: 0x2c0
   __TEXT.__objc_methlist: 0x204

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7320D034-F4B4-3E85-967A-4CBFBE41CE66
-  Functions: 22
-  Symbols:   165
+  UUID: D5934844-BB82-37D1-B682-EDB18BEE7E5B
+  Functions: 23
+  Symbols:   167
   CStrings:  130
 
Symbols:
+ _OUTLINED_FUNCTION_2
+ _objc_release_x24
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x2
- _objc_retain_x8
Functions:
~ -[ACCPlatformPluginWiFiSharing initPlugin] : 316 -> 300
~ -[ACCPlatformPluginWiFiSharing copyDeviceWiFiNetworkInformation] : 900 -> 924
~ -[ACCPlatformPluginWiFiSharing handleAccessoryWiFiInformationForWirelessCarPlay:] : 1216 -> 1200
~ _OUTLINED_FUNCTION_0 : 24 -> 72
~ _OUTLINED_FUNCTION_1 : 28 -> 24
+ _OUTLINED_FUNCTION_2
~ -[ACCPlatformPluginWiFiSharing initPlugin].cold.1 : 112 -> 56

```
