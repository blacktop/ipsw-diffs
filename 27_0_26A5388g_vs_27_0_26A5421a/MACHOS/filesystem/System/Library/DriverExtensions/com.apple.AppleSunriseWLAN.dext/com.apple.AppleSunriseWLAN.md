## com.apple.AppleSunriseWLAN

> `/System/Library/DriverExtensions/com.apple.AppleSunriseWLAN.dext/com.apple.AppleSunriseWLAN`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__osclassinfo`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA.__data`

```diff

-340.66.0.0.0
-  __TEXT.__text: 0x39bf0c
+340.71.0.0.0
+  __TEXT.__text: 0x39c3e4
   __TEXT.__auth_stubs: 0x1410
-  __TEXT.__cstring: 0xe7751
+  __TEXT.__cstring: 0xe78ca
   __TEXT.__const: 0xd380
-  __TEXT.__unwind_info: 0x4c80
+  __TEXT.__unwind_info: 0x4c88
   __TEXT.__oslogstring: 0x18f
-  __DATA_CONST.__const: 0xe718
+  __DATA_CONST.__const: 0xe740
   __DATA_CONST.__osclassinfo: 0xd8
   __DATA_CONST.__auth_got: 0xa08
   __DATA_CONST.__got: 0xf0
   __DATA.__data: 0xd7c8
-  __DATA.__common: 0x1f6320
-  __DATA.__bss: 0xefe8
+  __DATA.__common: 0x1f6420
+  __DATA.__bss: 0xf000
   - /System/DriverKit/System/Library/Frameworks/DriverKit.framework/DriverKit
   - /System/DriverKit/System/Library/Frameworks/NetworkingDriverKit.framework/NetworkingDriverKit
   - /System/DriverKit/System/Library/Frameworks/PCIDriverKit.framework/PCIDriverKit

   - /System/DriverKit/System/Library/PrivateFrameworks/IO80211DriverKit.framework/IO80211DriverKit
   - /System/DriverKit/System/Library/PrivateFrameworks/IOFileValidation.framework/IOFileValidation
   - /System/DriverKit/usr/lib/libc++.dylib
-  Functions: 8051
-  Symbols:   10146
-  CStrings:  20351
+  Functions: 8055
+  Symbols:   10154
+  CStrings:  20357
 
Symbols:
+ __ZN17IO80211Controller34reportsPerInterfacePeerCacheLimitsEv
+ __ZN28AppleSunriseWLANNANInterface26getPEER_CACHE_MAXIMUM_SIZEEP34apple80211_peer_cache_maximum_size
+ __ZThn112_N28AppleSunriseWLANNANInterface26getPEER_CACHE_MAXIMUM_SIZEEP34apple80211_peer_cache_maximum_size
+ __ZThn128_N28AppleSunriseWLANNANInterface26getPEER_CACHE_MAXIMUM_SIZEEP34apple80211_peer_cache_maximum_size
+ __ZThn48_N17IO80211Controller34reportsPerInterfacePeerCacheLimitsEv
+ _g_arNanMgmtRxCaches
+ _g_rNanMgmtRxCacheList
+ _nanMgmtCheckDuplicatedRx
CStrings:
+ "\"AppleSunriseWLAN_driverkit-340.71\""
+ "%llu-%u-[%d]%s:(NAN INFO) age mgmt,subtype,%u,sn,%u,TA,%02x:%02x:%02x:%02x:%02x:%02x\n"
+ "%llu-%u-[%d]%s:(NAN INFO) dup mgmt,subtype,%u,sn,%u,TA,%02x:%02x:%02x:%02x:%02x:%02x\n"
+ "%llu-%u-[%d]%s:(NAN LOUD) rx cache,subtype,%u,sn,%u,TA,%02x:%02x:%02x:%02x:%02x:%02x\n"
+ "%llu-%u-[%d]%s:(NAN WARN) Check Rx dup fail\n"
+ "AppleSunrise-user: [NAN] get peer cache max size"
+ "AppleSunriseWLAN_driverkit-340.71"
+ "Aug  9 2026 22:30:52"
+ "nanMgmtCheckDuplicatedRx"
- "\"AppleSunriseWLAN_driverkit-340.66\""
- "AppleSunriseWLAN_driverkit-340.66"
- "Jul 10 2026 22:08:32"
```
