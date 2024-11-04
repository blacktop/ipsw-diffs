## akd

> `/System/Library/PrivateFrameworks/AuthKit.framework/akd`

```diff

-493.225.2.0.0
-  __TEXT.__text: 0x18be94
+493.226.2.0.0
+  __TEXT.__text: 0x18e51c
   __TEXT.__auth_stubs: 0x1d20
-  __TEXT.__objc_stubs: 0x17f60
-  __TEXT.__objc_methlist: 0x8f44
-  __TEXT.__const: 0x2bf0
-  __TEXT.__cstring: 0xb123
+  __TEXT.__objc_stubs: 0x18040
+  __TEXT.__objc_methlist: 0x8f8c
+  __TEXT.__const: 0x2c50
+  __TEXT.__cstring: 0xb233
   __TEXT.__objc_classname: 0x18a3
-  __TEXT.__objc_methname: 0x21cac
+  __TEXT.__objc_methname: 0x21e0c
   __TEXT.__objc_methtype: 0x5a7d
-  __TEXT.__gcc_except_tab: 0x22bc
-  __TEXT.__oslogstring: 0x1ffe8
+  __TEXT.__gcc_except_tab: 0x22ec
+  __TEXT.__oslogstring: 0x200f8
   __TEXT.__dlopen_cstrs: 0xb8
-  __TEXT.__swift5_typeref: 0x1580
+  __TEXT.__swift5_typeref: 0x15be
   __TEXT.__swift5_fieldmd: 0xb6c
-  __TEXT.__constg_swiftt: 0x1190
+  __TEXT.__constg_swiftt: 0x11b8
   __TEXT.__swift5_reflstr: 0xae0
-  __TEXT.__swift5_assocty: 0x150
-  __TEXT.__swift5_capture: 0xff8
-  __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_proto: 0x118
-  __TEXT.__swift5_types: 0xec
+  __TEXT.__swift5_assocty: 0x168
+  __TEXT.__swift5_capture: 0x1088
+  __TEXT.__swift5_builtin: 0x8c
+  __TEXT.__swift5_proto: 0x11c
+  __TEXT.__swift5_types: 0xf0
   __TEXT.__swift5_protos: 0x34
-  __TEXT.__unwind_info: 0x56a0
-  __TEXT.__eh_frame: 0x76f0
+  __TEXT.__unwind_info: 0x5748
+  __TEXT.__eh_frame: 0x7970
   __DATA_CONST.__auth_got: 0xea0
-  __DATA_CONST.__got: 0x1640
+  __DATA_CONST.__got: 0x1650
   __DATA_CONST.__auth_ptr: 0x510
-  __DATA_CONST.__const: 0xc4d0
+  __DATA_CONST.__const: 0xc640
   __DATA_CONST.__cfstring: 0x6f20
   __DATA_CONST.__objc_classlist: 0x708
   __DATA_CONST.__objc_catlist: 0x38

   __DATA_CONST.__linkguard: 0x3e
   __DATA_CONST.__objc_dictobj: 0x118
   __DATA.__objc_const: 0x25480
-  __DATA.__objc_selrefs: 0x70e0
+  __DATA.__objc_selrefs: 0x7128
   __DATA.__objc_ivar: 0xa04
-  __DATA.__objc_data: 0x5568
-  __DATA.__data: 0x3c18
-  __DATA.__bss: 0x21a0
+  __DATA.__objc_data: 0x5570
+  __DATA.__data: 0x3c58
+  __DATA.__bss: 0x2220
   __DATA.__common: 0x111
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Combine.framework/Combine

   - /System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation
   - /System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
-  - /System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/PlugInKit.framework/PlugInKit
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 6898
-  Symbols:   1319
-  CStrings:  9530
+  Functions: 6947
+  Symbols:   1321
+  CStrings:  9545
 
Symbols:
+ _$ss15_print_unlockedyyx_q_zts16TextOutputStreamR_r0_lF
+ _$ss26DefaultStringInterpolationVN
+ _$ss26DefaultStringInterpolationVs16TextOutputStreamsWP
- _MAEIssueDCRTWithCompletion
CStrings:
+ "Attempted to show UI, AuthKit does not supportUI on audio accessory!"
+ "Device list cache updated with error - %!@(MISSING)"
+ "DeviceListStoreManager - Unable to create MID hash mismatch event for altDSID - %!s(MISSING)."
+ "DeviceListStoreManager - Unable to report MID hash mismatch event. No idms account found for altDSID - %!s(MISSING)."
+ "MAEIssueDCRTWithCompletion"
+ "Verified device list cache in background with success - %!d(MISSING) and error - %!@(MISSING)"
+ "_canShowUI"
+ "_clearDeviceListCacheForAltDSID:"
+ "_clearDeviceListForAltDSID:"
+ "_clearStaleCachedDevices"
+ "_configureDeviceListCacheInBackgroundWithContext:response:"
+ "deletedDevicesClientHash"
+ "trustedDevicesClientHash"
+ "updateCacheWithContext:deviceListResponse:completionHandler:"
+ "v40@0:8@\"AKDeviceListRequestContext\"16@\"AKDeviceListResponse\"24@?<v@?@\"NSError\">32"
+ "v56@0:8@\"AKDeviceListResponse\"16@\"AKDeviceListRequestContext\"24@\"AKAccountManager\"32@\"AAFAnalyticsReporter\"40@?<v@?B@\"NSError\">48"
+ "verifyCacheSyncStatusFromResponse:context:accountManager:reporter:completionHandler:"
- "Attempted to show UI on HomePod, AuthKit does not support HomePod UI!"
- "DeviceListCache feature is not enabled."

```
