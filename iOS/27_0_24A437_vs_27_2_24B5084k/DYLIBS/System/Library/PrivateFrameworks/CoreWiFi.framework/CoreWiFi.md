## CoreWiFi

> `/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`

```diff

-1030.84.4.1.0
-  __TEXT.__text: 0x1f65f8
-  __TEXT.__objc_methlist: 0x12674
+1032.5.0.0.0
+  __TEXT.__text: 0x1f816c
+  __TEXT.__objc_methlist: 0x12794
   __TEXT.__const: 0x7cc0
   __TEXT.__dlopen_cstrs: 0xab0
   __TEXT.__swift5_typeref: 0x13b4

   __TEXT.__swift5_assocty: 0x108
   __TEXT.__constg_swiftt: 0xe88
   __TEXT.__swift5_fieldmd: 0x108c
-  __TEXT.__cstring: 0x258be
+  __TEXT.__cstring: 0x259e6
   __TEXT.__swift5_proto: 0x6b4
   __TEXT.__swift5_types: 0x1b0
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__oslogstring: 0x2115b
-  __TEXT.__gcc_except_tab: 0x7694
+  __TEXT.__oslogstring: 0x21496
+  __TEXT.__gcc_except_tab: 0x76d0
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x8348
+  __TEXT.__unwind_info: 0x83c0
   __TEXT.__eh_frame: 0x1498
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5cc8
-  __DATA_CONST.__objc_classlist: 0x400
+  __DATA_CONST.__const: 0x5cf0
+  __DATA_CONST.__objc_classlist: 0x418
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9358
+  __DATA_CONST.__objc_selrefs: 0x93b8
   __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA_CONST.__objc_superrefs: 0x390
+  __DATA_CONST.__objc_superrefs: 0x3a0
   __DATA_CONST.__objc_arraydata: 0x2080
-  __DATA_CONST.__got: 0x9c0
-  __AUTH_CONST.__const: 0x50d8
-  __AUTH_CONST.__cfstring: 0x1d1e0
-  __AUTH_CONST.__objc_const: 0x182b0
-  __AUTH_CONST.__objc_intobj: 0x3e28
+  __DATA_CONST.__got: 0x9d0
+  __AUTH_CONST.__const: 0x5118
+  __AUTH_CONST.__cfstring: 0x1d200
+  __AUTH_CONST.__objc_const: 0x185a0
+  __AUTH_CONST.__objc_intobj: 0x3e40
   __AUTH_CONST.__objc_arrayobj: 0x498
   __AUTH_CONST.__objc_dictobj: 0x230
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1078
-  __AUTH.__objc_data: 0x1448
+  __AUTH_CONST.__auth_got: 0x1070
+  __AUTH.__objc_data: 0x1538
   __AUTH.__data: 0x1b8
-  __DATA.__objc_ivar: 0x1500
+  __DATA.__objc_ivar: 0x1518
   __DATA.__data: 0x2200
   __DATA.__common: 0x48
   __DATA_DIRTY.__objc_ivar: 0x84
   __DATA_DIRTY.__objc_data: 0x12e8
   __DATA_DIRTY.__data: 0x200
-  __DATA_DIRTY.__bss: 0x2e0
+  __DATA_DIRTY.__bss: 0x2e8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 9449
-  Symbols:   1185
-  CStrings:  6362
+  Functions: 9481
+  Symbols:   1187
+  CStrings:  6380
 
Symbols:
+ _OBJC_CLASS_$_CWFColocatedConsentResult
+ _OBJC_METACLASS_$_CWFColocatedConsentResult
CStrings:
+ "<%@: status=%ld, networks=%@>"
+ "@?<v@?@\"CWFColocatedConsentResult\"@\"NSError\">8@?0"
+ "DisallowCarrierProfileNetworksInLockdownMode"
+ "[corewifi] %{public}s (%{public}s:%u) Colocated consent evaluation timed out"
+ "[corewifi] %{public}s (%{public}s:%u) Colocated consent for %@: %@"
+ "[corewifi] %{public}s (%{public}s:%u) Colocated consent scan failed, reporting no candidate (%@)"
+ "[corewifi] %{public}s (%{public}s:%u) Colocated consent scanned %lu channel(s) in %llums, %lu result(s): %@"
+ "[corewifi] %{public}s (%{public}s:%u) No 5GHz channel to scan for %@, nothing colocated can qualify"
+ "[corewifi] %{public}s (%{public}s:%u) Split-SSID candidate %@ has no same-LAN history, consent required"
+ "[corewifi] %{public}s (%{public}s:%u) interface was NULL"
+ "[corewifi] AUTO-JOIN: Card capabilities not configured"
+ "[corewifi] AUTO-JOIN: Skipping known network that is not allowed in lockdown mode (network=%{public}@, addReason=%{public}@)"
+ "[corewifi] AUTO-JOIN: Will NOT use low power scan core (LPSC)"
+ "[corewifi] Network warning flags changed, current=%lu interfaceName=%@, posting XPC event"
+ "[corewifi] Network warning flags did not change, skipping event, current=%lu interfaceName=%@"
+ "__CWFClassifyColocated"
+ "__CWFColocatedScanParameters"
+ "__CWFPerformColocatedNetworkScan"
+ "__CWFPerformColocatedNetworkScanForInterface"
+ "__CWFPerformColocatedNetworkScanForInterface_block_invoke_2"
- "[corewifi] Network warning flags changed previous=%lu current=%lu interfaceName=%@, posting XPC event"
- "[corewifi] Network warning flags did not change, skipping event, previous=%lu current=%lu interfaceName=%@"
```
