## nehelper

> `/usr/libexec/nehelper`

```diff

-2205.82.1.0.0
-  __TEXT.__text: 0x25794
-  __TEXT.__auth_stubs: 0x1130
-  __TEXT.__objc_stubs: 0x28c0
+2226.100.24.0.0
+  __TEXT.__text: 0x2657c
+  __TEXT.__auth_stubs: 0x1070
+  __TEXT.__objc_stubs: 0x2980
   __TEXT.__objc_methlist: 0x44c
   __TEXT.__const: 0x11c
-  __TEXT.__gcc_except_tab: 0xa68
-  __TEXT.__objc_methname: 0x1f16
-  __TEXT.__oslogstring: 0x4abe
-  __TEXT.__cstring: 0x5e4b
-  __TEXT.__objc_classname: 0x1a5
-  __TEXT.__objc_methtype: 0x261
-  __TEXT.__unwind_info: 0x418
-  __DATA_CONST.__auth_got: 0x8a8
+  __TEXT.__gcc_except_tab: 0xa24
+  __TEXT.__objc_methname: 0x1f39
+  __TEXT.__oslogstring: 0x496b
+  __TEXT.__cstring: 0x5e3f
+  __TEXT.__objc_classname: 0x1a4
+  __TEXT.__objc_methtype: 0x26e
+  __TEXT.__unwind_info: 0x420
+  __DATA_CONST.__auth_got: 0x848
   __DATA_CONST.__got: 0x390
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0xc98
-  __DATA_CONST.__cfstring: 0x5140
+  __DATA_CONST.__cfstring: 0x5120
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x1330
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x17e8
-  __DATA.__objc_selrefs: 0xad0
-  __DATA.__objc_ivar: 0xe8
+  __DATA.__objc_const: 0x1788
+  __DATA.__objc_selrefs: 0xb00
+  __DATA.__objc_ivar: 0xdc
   __DATA.__objc_data: 0x500
   __DATA.__data: 0xc8
-  __DATA.__bss: 0x298
+  __DATA.__bss: 0x290
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DAC88C22-D842-34B7-AC36-721E313BCE6C
-  Functions: 248
-  Symbols:   388
-  CStrings:  2345
+  UUID: C3A461EA-F94D-38E8-B030-72AB193529F0
+  Functions: 245
+  Symbols:   376
+  CStrings:  2340
 
Symbols:
- _WiFiDeviceClientCopyCurrentNetwork
- _WiFiManagerClientGetDevice
- _WiFiNetworkGetSSIDData
- _WiFiNetworkIsEAP
- _WiFiNetworkIsOpen
- _WiFiNetworkIsSAE
- _WiFiNetworkIsWEP
- _WiFiNetworkIsWPAWPA2PSK
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x9
CStrings:
+ "%@ [%@] is denied Wi-Fi information access since it's linked with iOS SDK 26.0 or later. Use replacement API [NEHotspotNetwork fetchCurrentWithCompletionHandler:]"
+ "%@ device is associated to Wi-Fi network %{private}@"
+ "@\"CWFInterface\""
+ "_wifiInterface"
+ "currentKnownNetworkProfile"
+ "invalidate"
+ "networkName"
+ "numberWithUnsignedInt:"
- "%@ processing Wi-Fi information request for %s"
- "(nil)"
- "[%@] is denied Wi-Fi information access since it's linked with iOS SDK 26.0 or later. Use replacement API [NEHotspotNetwork fetchCurrentWithCompletionHandler:]"
- "[NEHelperWiFiInfoManager] Failed to get WiFi Manager Client instance"
- "[NEHelperWiFiInfoManager] WiFiManager restarted"
- "[NEHelperWiFiInfoManager] WiFiManagerClientCopyDevices() returned no devices"
- "[NEHelperWiFiInfoManager] WiFiManagerClientGetDevice for %@ returned NULL"
- "[NEHelperWiFiInfoManager] currently associated to a session based Wi-Fi network"
- "^v"
- "_interfaceName"
- "_isLegacyAPICaller"
- "_isSecurityTypeRequested"
- "_network"

```
