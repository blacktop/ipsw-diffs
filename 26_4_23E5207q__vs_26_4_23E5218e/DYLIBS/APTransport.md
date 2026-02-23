## APTransport

> `/System/Library/PrivateFrameworks/APTransport.framework/APTransport`

```diff

-940.19.1.0.0
-  __TEXT.__text: 0xa5a24
-  __TEXT.__auth_stubs: 0x3240
+940.21.1.0.0
+  __TEXT.__text: 0xa5c94
+  __TEXT.__auth_stubs: 0x3260
   __TEXT.__objc_methlist: 0x13d4
-  __TEXT.__cstring: 0x2c221
-  __TEXT.__const: 0x398
-  __TEXT.__gcc_except_tab: 0x70c
+  __TEXT.__cstring: 0x2c39d
+  __TEXT.__const: 0x3e0
+  __TEXT.__gcc_except_tab: 0x71c
   __TEXT.__oslogstring: 0x16e
   __TEXT.__dlopen_cstrs: 0x1f3
-  __TEXT.__unwind_info: 0x2860
+  __TEXT.__unwind_info: 0x2868
   __TEXT.__objc_classname: 0x1f5
   __TEXT.__objc_methname: 0x4bf8
   __TEXT.__objc_methtype: 0x100e

   __DATA_CONST.__objc_selrefs: 0x14d0
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0x1930
+  __AUTH_CONST.__auth_got: 0x1940
   __AUTH_CONST.__const: 0x2b68
-  __AUTH_CONST.__cfstring: 0x5e40
+  __AUTH_CONST.__cfstring: 0x5e80
   __AUTH_CONST.__objc_const: 0x1ce0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x30

   - /usr/lib/libIOReport.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6C94C5E9-5F6B-3A63-89D0-FFFCB2A59B63
-  Functions: 4917
-  Symbols:   12616
-  CStrings:  5934
+  UUID: 90A8D236-AB17-3DEF-B6BC-C8E6EF86BC2B
+  Functions: 4923
+  Symbols:   12630
+  CStrings:  5943
 
Symbols:
+ _CFDictionaryGetValueIfPresent
+ ___block_descriptor_80_e8_32o40o48o56r_e5_v8?0lr56l8s32l8s40l8s48l8
+ _browser_removeDeviceIfNoServicesRemain
+ _browser_removeDeviceIfNoServicesRemain.cold.1
+ _browser_removeDeviceIfNoServicesRemain.cold.2
+ _browser_removeDeviceIfNoServicesRemain.cold.3
+ _browser_removeDeviceIfNoServicesRemain.cold.4
+ _browser_removeDeviceIfNoServicesRemain.cold.5
+ _usleep
- ___block_descriptor_88_e8_32o40o48o56o64r_e5_v8?0lr64l8s32l8s40l8s48l8s56l8
CStrings:
+ "%sDNS (forceModern=%s forceBroker=%s) for deviceID %llu: %'s.\n"
+ "940.21.1"
+ "Device with id: %@ is being tracked in Presence mode. Suppressing remove notification."
+ "NANDS [%{ptr}] Previous NANDS is terminating."
+ "OSStatus browser_removeDeviceIfNoServicesRemain(APBrowserRef, CFNumberRef, CFMutableDictionaryRef, Boolean)"
+ "OSStatus browser_removeP2PServicesForNearbyDevices(APBrowserRef)"
+ "[%{ptr}] NANDS [%{ptr}] previous WFA DataSession still terminating, retrying (%d of %d) after %dms"
+ "[%{ptr}] Removed %#{flags} for device with id: %@"
+ "browser_removeDeviceIfNoServicesRemain"
+ "nanActivationRetries"
+ "nanActivationRetryInitialBackoffMs"
- "### NANDS [%{ptr}] Timed out waiting for previous termination to complete"
- "%sDNS (forceModern=%s forceBroker=%s) for deviceID %llu: %s.\n"
- "940.19.1"
- "Device with id: %@ name: %@ is being tracked in Presence mode. Suppressing remove notification.\n"

```
