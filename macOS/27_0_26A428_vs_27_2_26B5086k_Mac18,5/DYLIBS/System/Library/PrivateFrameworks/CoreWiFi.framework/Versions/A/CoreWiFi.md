## CoreWiFi

> `/System/Library/PrivateFrameworks/CoreWiFi.framework/Versions/A/CoreWiFi`

```diff

-1040.69.0.0.0
-  __TEXT.__text: 0x457774
-  __TEXT.__objc_methlist: 0x12548
+1042.4.0.0.0
+  __TEXT.__text: 0x45c018
+  __TEXT.__objc_methlist: 0x12660
   __TEXT.__const: 0x9bf8
-  __TEXT.__cstring: 0x2b68e
-  __TEXT.__oslogstring: 0x20a2c
-  __TEXT.__gcc_except_tab: 0x15de8
+  __TEXT.__cstring: 0x2b7ce
+  __TEXT.__oslogstring: 0x20d6c
+  __TEXT.__gcc_except_tab: 0x15ec0
   __TEXT.__dlopen_cstrs: 0x9cc
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x16b1

   __TEXT.__swift5_types: 0x1bc
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_capture: 0x1e0
-  __TEXT.__unwind_info: 0xc128
+  __TEXT.__unwind_info: 0xc1d0
   __TEXT.__eh_frame: 0x1278
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x10c8
-  __DATA_CONST.__objc_classlist: 0x400
+  __DATA_CONST.__objc_classlist: 0x418
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x91d0
+  __DATA_CONST.__objc_selrefs: 0x9228
   __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__objc_superrefs: 0x390
+  __DATA_CONST.__objc_superrefs: 0x3a0
   __DATA_CONST.__objc_arraydata: 0x1df8
-  __DATA_CONST.__got: 0xa78
-  __AUTH_CONST.__const: 0x9378
-  __AUTH_CONST.__cfstring: 0x1cb60
-  __AUTH_CONST.__objc_const: 0x18180
-  __AUTH_CONST.__objc_intobj: 0x3e28
+  __DATA_CONST.__got: 0xa88
+  __AUTH_CONST.__const: 0x93e8
+  __AUTH_CONST.__cfstring: 0x1cb80
+  __AUTH_CONST.__objc_const: 0x18468
+  __AUTH_CONST.__objc_intobj: 0x3e40
   __AUTH_CONST.__objc_arrayobj: 0x4c8
   __AUTH_CONST.__objc_dictobj: 0x230
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x1080
-  __AUTH.__objc_data: 0x1448
+  __AUTH.__objc_data: 0x1538
   __AUTH.__data: 0x1c8
-  __DATA.__objc_ivar: 0x157c
+  __DATA.__objc_ivar: 0x1594
   __DATA.__data: 0x1d30
   __DATA.__common: 0x38
   __DATA_DIRTY.__objc_data: 0x12e8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 11093
-  Symbols:   22686
-  CStrings:  6784
+  Functions: 11129
+  Symbols:   22756
+  CStrings:  6802
 
Symbols:
+ -[CWFAutoJoinManager __channelListContains6GHz:]
+ -[CWFAutoJoinManager __lowPowerScanCore6GHzUnsupported]
+ -[CWFAutoJoinManager cardCapabilities]
+ -[CWFAutoJoinManager setCardCapabilities:]
+ -[CWFColocatedConsentResult .cxx_destruct]
+ -[CWFColocatedConsentResult __initWithStatus:networks:]
+ -[CWFColocatedConsentResult description]
+ -[CWFColocatedConsentResult networks]
+ -[CWFColocatedConsentResult status]
+ -[CWFInterface(WiFiNetworkSharing) performColocatedNetworkScanWithConsentStatus:]
+ -[CWFNetworkWarningFlagsMonitor .cxx_destruct]
+ -[CWFNetworkWarningFlagsMonitor flagsForInterface:]
+ -[CWFNetworkWarningFlagsMonitor init]
+ -[CWFNetworkWarningFlagsMonitor recordFlags:forNetwork:onInterface:]
+ -[CWFNetworkWarningFlagsMonitor resetInterface:]
+ -[_CWFNetworkWarningFlagsEntry .cxx_destruct]
+ -[_CWFNetworkWarningFlagsEntry flags]
+ -[_CWFNetworkWarningFlagsEntry setFlags:]
+ -[_CWFNetworkWarningFlagsEntry setSsid:]
+ -[_CWFNetworkWarningFlagsEntry ssid]
+ CWFIsCarrierProfileAllowedInLockdownMode.allowCarrier
+ CWFIsCarrierProfileAllowedInLockdownMode.once
+ GCC_except_table214
+ GCC_except_table222
+ GCC_except_table231
+ GCC_except_table240
+ GCC_except_table246
+ GCC_except_table252
+ GCC_except_table271
+ GCC_except_table277
+ GCC_except_table295
+ GCC_except_table312
+ GCC_except_table319
+ GCC_except_table556
+ GCC_except_table567
+ GCC_except_table624
+ GCC_except_table638
+ OBJC_IVAR_$_CWFAutoJoinManager._cardCapabilities
+ OBJC_IVAR_$_CWFColocatedConsentResult._networks
+ OBJC_IVAR_$_CWFColocatedConsentResult._status
+ OBJC_IVAR_$_CWFNetworkWarningFlagsMonitor._entriesByInterface
+ OBJC_IVAR_$_CWFXPCRequestProxy._networkWarningFlagsMonitor
+ OBJC_IVAR_$__CWFNetworkWarningFlagsEntry._flags
+ OBJC_IVAR_$__CWFNetworkWarningFlagsEntry._ssid
+ _CWFIsCarrierProfileAllowedInLockdownMode
+ _OBJC_CLASS_$_CWFColocatedConsentResult
+ _OBJC_CLASS_$_CWFNetworkWarningFlagsMonitor
+ _OBJC_CLASS_$__CWFNetworkWarningFlagsEntry
+ _OBJC_METACLASS_$_CWFColocatedConsentResult
+ _OBJC_METACLASS_$_CWFNetworkWarningFlagsMonitor
+ _OBJC_METACLASS_$__CWFNetworkWarningFlagsEntry
+ __OBJC_$_INSTANCE_METHODS_CWFColocatedConsentResult
+ __OBJC_$_INSTANCE_METHODS_CWFNetworkWarningFlagsMonitor
+ __OBJC_$_INSTANCE_METHODS__CWFNetworkWarningFlagsEntry
+ __OBJC_$_INSTANCE_VARIABLES_CWFColocatedConsentResult
+ __OBJC_$_INSTANCE_VARIABLES_CWFNetworkWarningFlagsMonitor
+ __OBJC_$_INSTANCE_VARIABLES__CWFNetworkWarningFlagsEntry
+ __OBJC_$_PROP_LIST_CWFColocatedConsentResult
+ __OBJC_$_PROP_LIST__CWFNetworkWarningFlagsEntry
+ __OBJC_CLASS_RO_$_CWFColocatedConsentResult
+ __OBJC_CLASS_RO_$_CWFNetworkWarningFlagsMonitor
+ __OBJC_CLASS_RO_$__CWFNetworkWarningFlagsEntry
+ __OBJC_METACLASS_RO_$_CWFColocatedConsentResult
+ __OBJC_METACLASS_RO_$_CWFNetworkWarningFlagsMonitor
+ __OBJC_METACLASS_RO_$__CWFNetworkWarningFlagsEntry
+ ___55-[CWFColocatedConsentResult __initWithStatus:networks:]_block_invoke
+ ___CWFClassifyColocated
+ ___CWFColocatedScanParameters
+ ___CWFIsCarrierProfileAllowedInLockdownMode_block_invoke
+ ___CWFPerformColocatedNetworkScan
+ ___CWFPerformColocatedNetworkScanForInterface
+ ____CWFPerformColocatedNetworkScanForInterface_block_invoke
+ _____CWFPerformColocatedNetworkScanForInterface_block_invoke
+ _____CWFPerformColocatedNetworkScanForInterface_block_invoke_2
+ ___block_descriptor_48_e8_32s40r_e49_?<v?"CWFColocatedConsentResult""NSError">8?0l
+ ___os_log_helper_16_2_7_8_34_8_34_4_0_8_0_8_0_8_0_8_64
+ _objc_msgSend$__channelListContains6GHz:
+ _objc_msgSend$__initWithStatus:networks:
+ _objc_msgSend$__lowPowerScanCore6GHzUnsupported
+ _objc_msgSend$cardCapabilities
+ _objc_msgSend$currentScanResult
+ _objc_msgSend$performScanWithParameters:error:
+ _objc_msgSend$recordFlags:forNetwork:onInterface:
+ _objc_msgSend$resetInterface:
+ _objc_msgSend$setCardCapabilities:
+ _objc_msgSend$setSsid:
+ _objc_msgSend$ssid
- GCC_except_table186
- GCC_except_table220
- GCC_except_table229
- GCC_except_table238
- GCC_except_table244
- GCC_except_table258
- GCC_except_table279
- GCC_except_table285
- GCC_except_table301
- GCC_except_table310
- GCC_except_table321
- GCC_except_table544
- GCC_except_table566
- GCC_except_table594
- GCC_except_table612
- GCC_except_table629
- OBJC_IVAR_$_CWFXPCRequestProxy._mutableNetworkWarningFlags
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
+ "__CWFPerformColocatedNetworkScanForInterface_block_invoke"
- "[corewifi] Network warning flags changed previous=%lu current=%lu interfaceName=%@, posting XPC event"
- "[corewifi] Network warning flags did not change, skipping event, previous=%lu current=%lu interfaceName=%@"
```
