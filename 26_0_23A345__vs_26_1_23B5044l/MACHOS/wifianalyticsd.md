## wifianalyticsd

> `/usr/libexec/wifianalyticsd`

```diff

-776.90.4.2.0
-  __TEXT.__text: 0x99730
-  __TEXT.__auth_stubs: 0x15b0
+785.10.0.0.0
+  __TEXT.__text: 0x99b50
+  __TEXT.__auth_stubs: 0x15f0
   __TEXT.__objc_stubs: 0x8ba0
   __TEXT.__objc_methlist: 0x350c
   __TEXT.__const: 0x3d8
   __TEXT.__dlopen_cstrs: 0x1e2
-  __TEXT.__cstring: 0x142d7
+  __TEXT.__cstring: 0x1431b
   __TEXT.__constg_swiftt: 0x494
   __TEXT.__swift5_typeref: 0x276
   __TEXT.__swift5_fieldmd: 0x1ec
-  __TEXT.__oslogstring: 0x145ed
+  __TEXT.__oslogstring: 0x14753
   __TEXT.__swift5_types: 0x30
   __TEXT.__swift5_reflstr: 0x12b
-  __TEXT.__objc_methname: 0xdb99
+  __TEXT.__objc_methname: 0xdb9a
   __TEXT.__swift5_capture: 0xec
-  __TEXT.__gcc_except_tab: 0x52d4
+  __TEXT.__gcc_except_tab: 0x52f8
   __TEXT.__objc_classname: 0x334
   __TEXT.__objc_methtype: 0x1103
-  __TEXT.__unwind_info: 0x1068
+  __TEXT.__unwind_info: 0x1078
   __TEXT.__eh_frame: 0x90
-  __DATA_CONST.__auth_got: 0xaf0
+  __DATA_CONST.__auth_got: 0xb10
   __DATA_CONST.__got: 0x440
   __DATA_CONST.__auth_ptr: 0x88
   __DATA_CONST.__const: 0x1a88
-  __DATA_CONST.__cfstring: 0x10760
+  __DATA_CONST.__cfstring: 0x10740
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__data: 0x998
   __DATA.__bss: 0x208
   __DATA.__common: 0x88
-  - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreML.framework/CoreML
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices
+  - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: C66C6C3F-DFE6-3575-843C-4E7514D3C049
-  Functions: 1498
-  Symbols:   523
-  CStrings:  8406
+  UUID: 3D6F5BD1-93D0-3D85-BA82-D348744E7291
+  Functions: 1499
+  Symbols:   527
+  CStrings:  8412
 
Symbols:
+ ___error
+ _getnameinfo
+ _nw_array_get_count
+ _nw_array_get_object_at_index
+ _nw_endpoint_create_host
+ _nw_endpoint_get_address
+ _nw_resolver_cancel
+ _nw_resolver_create_with_endpoint
+ _nw_resolver_set_update_handler
- _CFDataGetBytePtr
- _CFHostCreateWithName
- _CFHostGetAddressing
- _CFHostStartInfoResolution
- _inet_ntop
CStrings:
+ "\"WiFiAnalytics_executables-785.10\""
+ "%{public}s::%d:Could not getnameinfo %p: errno=%d"
+ "%{public}s::%d:DNS Resolution (captive.apple.com): COMPLETED (status:Fail)"
+ "%{public}s::%d:DNS Resolution (captive.apple.com): COMPLETED (status:Success) IPAddresses:(%@)"
+ "%{public}s::%d:DNS Resolution (captive.apple.com): COMPLETED (status:Timeout)"
+ "%{public}s::%d:DNS Resolution (captive.apple.com): forced COMPLETE (status:Timeout)"
+ "%{public}s::%d:DNS Resolution handler aborting"
+ "%{public}s::%d:nw_resolver_set_update_handler failed to set handler"
+ "%{public}s::%d:nwhostname creation error"
+ "%{public}s::%d:resolver creation error"
+ "%{public}s::%d:semaphore creation error"
+ "%{public}s::%d:serialQueue cannot be nil"
+ "-[WAEngine testDNSResolution:]"
+ "-[WAEngine testDNSResolution:]_block_invoke"
+ "Sep 11 2025 20:21:33"
+ "WiFiAnalytics_executables-785.10"
+ "WiFiAnalytics_executables-785.10 Sep 11 2025 20:21:30"
+ "testDNSResolution:"
+ "v20@?0i8@\"NSObject<OS_nw_array>\"12"
- "\"WiFiAnalytics_executables-776.90.4.2\""
- "%{public}s::%d:SDNS: DNS resolution timeout..."
- "%{public}s::%d:SDNS: Failed to create hostRef"
- "%{public}s::%d:SDNS: Failed to start resolution: domain = %ld, error = %d"
- "%{public}s::%d:SDNS: IPv4 Address: %s"
- "%{public}s::%d:SDNS: IPv6 Address: %s"
- "%{public}s::%d:SDNS: Trying to resolve captive.apple.com"
- "-[WAEngine testDNSResolution]"
- "Aug  6 2025 21:32:25"
- "WiFiAnalytics_executables-776.90.4.2"
- "WiFiAnalytics_executables-776.90.4.2 Aug  6 2025 21:32:23"
- "testDNSResolution"

```
