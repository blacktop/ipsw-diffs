## MobileWiFi

> `/System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi`

```diff

-2031.4.0.0.0
-  __TEXT.__text: 0x2ede8
+2031.5.0.0.0
+  __TEXT.__text: 0x2edc8
   __TEXT.__objc_methlist: 0x94
   __TEXT.__cstring: 0x46d5
   __TEXT.__const: 0x710
Symbols:
+ _os_unfair_recursive_lock_lock
- _os_unfair_recursive_lock_lock_with_options
Functions:
~ _WiFiManagerClientGetDevice : 124 -> 120
~ ___WiFiManagerClientGetOrReconnectServerPort : 1028 -> 1024
~ ___WiFiManagerClientAddDevice : 408 -> 404
~ _WiFiManagerClientCopyDevices : 312 -> 308
~ ___WiFiManagerClientGetRootDevice : 224 -> 220
~ _WiFiManagerClientCopyInterfaces : 260 -> 256
~ _WiFiManagerClientRemoveDevice : 312 -> 308
~ ___WiFiManagerClientClearDevicePorts : 256 -> 252
```
