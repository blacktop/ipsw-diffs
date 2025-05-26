## ApplePhotonDetectorServices

> `/System/Library/PrivateFrameworks/ApplePhotonDetectorServices.framework/ApplePhotonDetectorServices`

```diff

-10.7.0.0.0
-  __TEXT.__text: 0x1bac
-  __TEXT.__auth_stubs: 0x210
-  __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x301
-  __TEXT.__oslogstring: 0x39c
-  __TEXT.__gcc_except_tab: 0x60
-  __TEXT.__unwind_info: 0xa0
+10.22.0.0.0
+  __TEXT.__text: 0x310c
+  __TEXT.__auth_stubs: 0x240
+  __TEXT.__const: 0x70
+  __TEXT.__cstring: 0x442
+  __TEXT.__oslogstring: 0x5b3
+  __TEXT.__gcc_except_tab: 0x90
+  __TEXT.__unwind_info: 0xe4
   __DATA_CONST.__got: 0x50
-  __DATA_CONST.__const: 0x120
+  __DATA_CONST.__const: 0x248
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x60
-  __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0x110
+  __AUTH_CONST.__auth_ptr: 0x10
+  __AUTH_CONST.__auth_got: 0x128
+  __DATA.__bss: 0x4
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 15
-  Symbols:   83
-  CStrings:  49
+  Functions: 31
+  Symbols:   123
+  CStrings:  65
 
Symbols:
+ GCC_except_table12
+ _ApplePhotonDetectorServicesClose
+ _ApplePhotonDetectorServicesGetLuxAsync
+ _ApplePhotonDetectorServicesOpen
+ __ZL12isIspPoweredP13xpcConnection
+ __ZL20disconnectFromDaemonP27ApplePhotonDetectorServices
+ __ZZL13UpdateLuxInfoP28ISPServicesRemotePropertyGetP34ApplePhotonDetectorServicesLuxInfoPbE1i
+ ___ApplePhotonDetectorServicesGetLuxAsync_block_invoke
+ ___ApplePhotonDetectorServicesGetLuxAsync_block_invoke.21
+ ___ApplePhotonDetectorServicesGetLuxAsync_block_invoke.22
+ ___ApplePhotonDetectorServicesGetLuxAsync_block_invoke.25
+ ___ApplePhotonDetectorServicesGetLuxAsync_block_invoke.29
+ ___ApplePhotonDetectorServicesGetLuxAsync_block_invoke_2
+ ___ApplePhotonDetectorServicesGetLuxAsync_block_invoke_2.28
+ ___Block_byref_object_copy_.18
+ ___Block_byref_object_dispose_.19
+ ____ZL20disconnectFromDaemonP27ApplePhotonDetectorServices_block_invoke
+ ___block_descriptor_tmp.20
+ ___block_descriptor_tmp.23
+ ___block_descriptor_tmp.24
+ ___block_descriptor_tmp.26
+ ___block_descriptor_tmp.27
+ ___block_descriptor_tmp.30
+ ___block_descriptor_tmp.31
+ ___block_descriptor_tmp.33
+ _malloc_type_malloc
+ _os_variant_is_recovery
+ _xpc_connection_send_message_with_reply
+ _xpc_dictionary_set_string
- _IORegistryEntryFromPath
CStrings:
+ "%s: %d: Could not create a serial queue\n"
+ "%s: %d: Could not open an interface to APDS\n"
+ "%s: %d: Invalid handle provided %p\n"
+ "%s: APDS dispatch queue is unavailable. Was it not allocated ?\n"
+ "%s: Could not establish a connection with the daemon, exiting\n"
+ "%s: Could not get the required data\n"
+ "%s: Error! Client has not allocated the required memory: lux samples = %p, abs time = %p, gains = %p, coex = %p\n"
+ "%s: Error! Client requested 0 samples\n"
+ "%s: Invalid arguments, replyQueue = 0x%p, info = 0x%p, UserCallback = 0x%p, handle = %p exiting\n"
+ "ApplePhotonDetectorServicesClose"
+ "ApplePhotonDetectorServicesGetLuxAsync"
+ "ApplePhotonDetectorServicesGetLuxAsync_block_invoke"
+ "ApplePhotonDetectorServicesGetLuxAsync_block_invoke_2"
+ "ApplePhotonDetectorServicesOpen"
+ "H16ISPServicesRemoteIORegPropertyDataKey"
+ "H16ISPServicesRemoteIORegPropertyNameKey"
+ "com.apple.applephotondetectorservicesprivatequeue"
- "IODeviceTree:/chosen"

```
