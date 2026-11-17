## iTunesCloud

> `/System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud`

```diff

-4026.300.13.0.0
-  __TEXT.__text: 0x3c3af8
+4026.300.16.0.0
+  __TEXT.__text: 0x3c3ab0
   __TEXT.__objc_methlist: 0x189e4
   __TEXT.__const: 0x225f8
   __TEXT.__dlopen_cstrs: 0x4cf

   __AUTH_CONST.__objc_intobj: 0x480
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x258
-  __AUTH_CONST.__auth_got: 0xa68
+  __AUTH_CONST.__auth_got: 0xa70
   __AUTH.__objc_data: 0x230
   __DATA.__objc_ivar: 0x24f0
   __DATA.__data: 0x30d0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   Functions: 10203
-  Symbols:   17912
+  Symbols:   17913
   CStrings:  5506
 
Symbols:
+ _os_unfair_recursive_lock_lock
Functions:
~ -[ICNetworkMonitor _onQueue_updateNetworkStateWithTelephonyChangeType:andNotifyDelegate:] : 1072 -> 1080
~ -[ICNetworkMonitor _onQueue_updateTelephonyState] : 768 -> 760
~ -[ICNetworkMonitor isRemoteServerLikelyReachable] : 224 -> 220
~ -[ICNetworkMonitor _onQueue_setup] : 1348 -> 1336
~ -[ICNetworkMonitor networkType] : 224 -> 220
~ -[ICNetworkMonitor cellMonitorUpdate:info:] : 484 -> 480
~ -[ICNetworkMonitor isEthernetWired] : 224 -> 220
~ -[ICNetworkMonitor isWiFiAssociated] : 224 -> 220
~ -[ICNetworkMonitor lastKnownNetworkType] : 224 -> 220
~ -[ICNetworkMonitor isRemoteServerReachable] : 224 -> 220
~ -[ICNetworkMonitor currentNetworkLinkQuality] : 224 -> 220
~ -[ICNetworkMonitor isCurrentNetworkLinkExpensive] : 224 -> 220
~ -[ICNetworkMonitor isWifiActive] : 224 -> 220
~ -[ICNetworkMonitor isNetworkConstrained] : 224 -> 220
~ -[ICNetworkMonitor telephonyOperatorName] : 284 -> 280
~ -[ICNetworkMonitor telephonyRegistrationStatus] : 284 -> 280
~ -[ICNetworkMonitor signalInfo] : 856 -> 852
~ -[ICNetworkMonitor signalStrength] : 1272 -> 1268
```
