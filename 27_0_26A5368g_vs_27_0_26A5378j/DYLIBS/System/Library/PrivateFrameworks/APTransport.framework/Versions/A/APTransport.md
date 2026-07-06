## APTransport

> `/System/Library/PrivateFrameworks/APTransport.framework/Versions/A/APTransport`

```diff

-  __TEXT.__text: 0x8d2c0
+  __TEXT.__text: 0x8d864
   __TEXT.__objc_methlist: 0x1a54
   __TEXT.__const: 0x3f0
-  __TEXT.__gcc_except_tab: 0x834
-  __TEXT.__cstring: 0x240ef
+  __TEXT.__gcc_except_tab: 0x820
+  __TEXT.__cstring: 0x243bf
   __TEXT.__dlopen_cstrs: 0xfe
   __TEXT.__oslogstring: 0x1af
-  __TEXT.__unwind_info: 0x2360
+  __TEXT.__unwind_info: 0x2378
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x30
-  __DATA_CONST.__got: 0x358
-  __AUTH_CONST.__const: 0x3840
+  __DATA_CONST.__got: 0x360
+  __AUTH_CONST.__const: 0x3820
   __AUTH_CONST.__cfstring: 0x57c0
   __AUTH_CONST.__objc_const: 0x20c0
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__objc_intobj: 0x60
+  __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x190
+  __AUTH.__objc_data: 0xf0
   __AUTH.__data: 0x2c0
   __DATA.__objc_ivar: 0x174
-  __DATA.__data: 0xf90
-  __DATA.__bss: 0xe8
-  __DATA_DIRTY.__objc_data: 0x1e0
-  __DATA_DIRTY.__data: 0xa10
+  __DATA.__data: 0xeb0
+  __DATA.__bss: 0xd8
+  __DATA_DIRTY.__objc_data: 0x280
+  __DATA_DIRTY.__data: 0xaf0
   __DATA_DIRTY.__bss: 0x240
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/Versions/A/WiFiPeerToPeer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4200
-  Symbols:   6839
-  CStrings:  4289
+  Functions: 4209
+  Symbols:   6847
+  CStrings:  4299
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__data : content changed
Symbols:
+ APTNANDataSessionGetPerformanceForecast
+ APTransportDeviceIsTransportRecommended
+ GCC_except_table39
+ _APSGetNANPerformanceForecastThresholds
+ _APTNANDataSessionGetPerformanceForecast
+ _APTransportDeviceIsTransportRecommended
+ _BonjourBrowser_SetNANUserID
+ _objc_msgSend$localInfrastructureThroughputCapacityRatio
+ _objc_msgSend$localThroughputCapacityMbps
+ _objc_msgSend$performanceForecast
+ _objc_msgSend$setUserID:
+ _objc_msgSend$signalStrength
+ _objc_msgSend$unavailabilityLatencyCeilingMs
- _NSSelectorFromString
- _OBJC_CLASS_$_NSInvocation
- ____APBonjourBrowserStartOpenNAN_block_invoke
- _objc_msgSend$invocationWithMethodSignature:
- _objc_msgSend$invoke
- _objc_msgSend$methodSignatureForSelector:
- _objc_msgSend$setArgument:atIndex:
- _objc_msgSend$setSelector:
- _objc_msgSend$setTarget:
CStrings:
+ "980.67.2"
+ "APTNANDataSessionGetPerformanceForecast"
+ "APTransportDeviceIsTransportRecommended"
+ "Boolean transportDevice_isNANRecommended(APTransportDeviceRef, OSStatus *)"
+ "NANDS [%{ptr}] Failed to obtain NANEndpoint with error: %#m"
+ "NANDS [%{ptr}] perfForecast=%@"
+ "OSStatus APTNANDataSessionGetPerformanceForecast(APTNANDataSessionRef, APSTransportPerformanceInfo *)"
+ "Terminus_ExplicitNANControl"
+ "[%{ptr}] NAN [%{ptr}] not recommended due to NAN throughput of %f with threshold of %f"
+ "[%{ptr}] NAN [%{ptr}] not recommended due to infra throughput ratio of %f with threshold of %f"
+ "[%{ptr}] NAN [%{ptr}] not recommended due to latency of %f with threshold of %f"
+ "[%{ptr}] NAN [%{ptr}] not recommended due to signal strength of %f with threshold of %f"
+ "transportDevice_isNANRecommended"
- "980.63.2"
- "BonjourBrowser_SetNANUserID"
- "setUserID:"

```
