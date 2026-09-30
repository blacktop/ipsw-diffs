## lockdownd

> `/usr/libexec/lockdownd`

```diff

-1365.100.4.0.0
-  __TEXT.__text: 0xb0520
-  __TEXT.__auth_stubs: 0x1cf0
-  __TEXT.__objc_stubs: 0x1360
-  __TEXT.__objc_methlist: 0xe8
-  __TEXT.__cstring: 0x3ba0b
-  __TEXT.__const: 0x10f50
-  __TEXT.__oslogstring: 0x1e6
-  __TEXT.__gcc_except_tab: 0x9b8
-  __TEXT.__objc_classname: 0x27
-  __TEXT.__objc_methname: 0xd61
-  __TEXT.__objc_methtype: 0x120
+1365.100.8.0.0
+  __TEXT.__text: 0xaa930
+  __TEXT.__auth_stubs: 0x1db0
+  __TEXT.__objc_stubs: 0x15c0
+  __TEXT.__objc_methlist: 0x180
+  __TEXT.__cstring: 0x3bd14
+  __TEXT.__const: 0x10fc0
+  __TEXT.__gcc_except_tab: 0xaf0
+  __TEXT.__objc_methname: 0xf22
+  __TEXT.__oslogstring: 0x319
+  __TEXT.__objc_classname: 0x4c
+  __TEXT.__objc_methtype: 0x15a
   __TEXT.__services: 0x2d43
-  __TEXT.__unwind_info: 0xb98
+  __TEXT.__unwind_info: 0xbf8
   __TEXT.__eh_frame: 0x80
-  __DATA_CONST.__auth_got: 0xe88
-  __DATA_CONST.__got: 0x408
+  __DATA_CONST.__auth_got: 0xee8
+  __DATA_CONST.__got: 0x430
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x8398
-  __DATA_CONST.__cfstring: 0xdac0
-  __DATA_CONST.__objc_classlist: 0x8
+  __DATA_CONST.__const: 0x70b8
+  __DATA_CONST.__cfstring: 0xdc60
+  __DATA_CONST.__objc_classlist: 0x10
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x1c0
-  __DATA.__objc_selrefs: 0x510
-  __DATA.__objc_ivar: 0x14
-  __DATA.__objc_data: 0x50
-  __DATA.__data: 0x21b8
+  __DATA.__objc_const: 0x330
+  __DATA.__objc_selrefs: 0x5a8
+  __DATA.__objc_ivar: 0x20
+  __DATA.__objc_data: 0xa0
+  __DATA.__data: 0x21b0
   __DATA.__bss: 0x1e8
-  __DATA.__common: 0xab8
+  __DATA.__common: 0xaa8
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
+  - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport

   - /System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore
   - /System/Library/PrivateFrameworks/CoreTime.framework/CoreTime
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
+  - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice
   - /System/Library/PrivateFrameworks/IntlPreferences.framework/IntlPreferences

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libramrod.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 8D7CD309-1B1E-302B-B57B-0F874216747F
-  Functions: 880
-  Symbols:   620
-  CStrings:  7391
+  UUID: 37B983A2-88B2-3DB8-B3C5-360FFFA99AD6
+  Functions: 918
+  Symbols:   637
+  CStrings:  7471
 
Symbols:
+ _CFNotificationCenterGetLocalCenter
+ _CWFEventLinkChangeStatusKey
+ _CryptoHKDF
+ _CryptoHMACOneShot
+ _OBJC_CLASS_$_CWFInterface
+ _OBJC_CLASS_$_NSUUID
+ __os_log_debug_impl
+ _dispatch_block_cancel
+ _dispatch_block_create
+ _dispatch_queue_attr_make_initially_inactive
+ _kCryptoHashDescriptor_SHA256
+ _kCryptoHashDescriptor_SHA512
+ _nw_txt_record_access_bytes
+ _nw_txt_record_create_dictionary
+ _nw_txt_record_set_key
+ _objc_retain_x26
+ _xpc_dictionary_set_data
CStrings:
+ "-[LockdownWiFiMonitor init]"
+ "@\"CWFInterface\""
+ "@\"NSObject<OS_dispatch_queue>\""
+ "@24@0:8@16"
+ "B24@?0r*8Q16"
+ "Connection to CoreWiFi daemon invalidated"
+ "EnablePrivatizedBonjourAdvertisement"
+ "Failed to build TXTRecord."
+ "Failed to convert hostID into data."
+ "Failed to convert uuid into data."
+ "Failed to create WiFiMonitor queue"
+ "Failed to create initial state WiFiMonitor block"
+ "Failed to encode auth tag."
+ "Failed to enumerate pair records to generate auth tag keys."
+ "Failed to initialize WiFi monitor."
+ "Failed to set \"%s\" value in Bonjour TXTRecord."
+ "Failed to start WiFi monitoring: %@"
+ "Initial WiFi Link State: Down"
+ "Initial WiFi Link State: Up"
+ "LockdownWiFiMonitor"
+ "MACAddress"
+ "No WiFi interface"
+ "Pairing record missing hostID."
+ "SSID"
+ "T@\"CWFInterface\",R,N,V_interface"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
+ "TB,V_cachedLinkDownStatus"
+ "TXTRecord"
+ "UUIDString"
+ "WiFi link debounce in progress..."
+ "WiFi link down."
+ "WiFi link status changed with no info..."
+ "WiFi link up."
+ "_cachedLinkDownStatus"
+ "_interface"
+ "_queue"
+ "authTag"
+ "authTag#%u"
+ "build_bonjour_TXTRecord"
+ "cachedLinkDownStatus"
+ "com.apple.mobile.lockdown.wifi_link_down"
+ "com.apple.mobile.lockdown.wifi_link_up"
+ "com.apple.mobile.lockdownd.WiFiMonitor"
+ "dataFromString:"
+ "data_ark_remove_attr"
+ "generate_auth_tag_keys"
+ "generate_auth_tag_keys_block_invoke"
+ "handleEvent:"
+ "initWithBytesNoCopy:length:freeWhenDone:"
+ "initialize_wifi_syncing"
+ "interface"
+ "isLinkDown"
+ "isLinkDownDebounceInProgress"
+ "linkDown"
+ "linkUp"
+ "mutableBytes"
+ "queue"
+ "setCachedLinkDownStatus:"
+ "setEventHandler:"
+ "setInvalidationHandler:"
+ "startMonitoringEventType:error:"
+ "type"
+ "update_bonjour_service_instance_name"
+ "v16@?0@\"CWFEvent\"8"
+ "wifi_link_down_callback"
+ "wifi_link_up_callback"
- "intialize_wifi_syncing"

```
