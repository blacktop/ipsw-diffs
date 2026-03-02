## LocalAuthenticationCore

> `/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`

```diff

-2005.100.182.0.0
-  __TEXT.__text: 0x16223c
+2005.100.183.0.0
+  __TEXT.__text: 0x16243c
   __TEXT.__auth_stubs: 0x2710
-  __TEXT.__objc_methlist: 0xbf18
+  __TEXT.__objc_methlist: 0xbf30
   __TEXT.__const: 0x913c
   __TEXT.__gcc_except_tab: 0x1b38
-  __TEXT.__oslogstring: 0x9419
+  __TEXT.__oslogstring: 0x94a9
   __TEXT.__cstring: 0xeb7b
   __TEXT.__dlopen_cstrs: 0x60e
   __TEXT.__swift5_typeref: 0x3366

   __TEXT.__unwind_info: 0x60c0
   __TEXT.__eh_frame: 0x3120
   __TEXT.__objc_classname: 0x4395
-  __TEXT.__objc_methname: 0x14715
+  __TEXT.__objc_methname: 0x14755
   __TEXT.__objc_methtype: 0x5f61
-  __TEXT.__objc_stubs: 0xd920
+  __TEXT.__objc_stubs: 0xd900
   __DATA_CONST.__got: 0xc98
   __DATA_CONST.__const: 0x5160
   __DATA_CONST.__objc_classlist: 0xac0

   __AUTH_CONST.__auth_got: 0x1398
   __AUTH_CONST.__const: 0x7318
   __AUTH_CONST.__cfstring: 0x7000
-  __AUTH_CONST.__objc_const: 0x4fc18
+  __AUTH_CONST.__objc_const: 0x4fc78
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH.__objc_data: 0x3a00
   __AUTH.__data: 0x1d68
-  __DATA.__objc_ivar: 0x8a4
+  __DATA.__objc_ivar: 0x8b0
   __DATA.__data: 0x6ba0
   __DATA.__bss: 0x5e79
   __DATA.__common: 0x40

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 806F8C58-C182-30B8-9FD2-83258E23AF63
-  Functions: 9357
-  Symbols:   31902
-  CStrings:  8015
+  UUID: 43EC6889-60A5-3FD1-8C4C-E876AF5B3261
+  Functions: 9359
+  Symbols:   31908
+  CStrings:  8020
 
Symbols:
+ -[LACNRDeviceMonitorAdapter deviceIsConnectedDidChange:isConnected:]
+ -[LACNRDeviceMonitorAdapter reportReachableStateIfChanged]
+ _OBJC_IVAR_$_LACNRDeviceMonitorAdapter._isConnected
+ _OBJC_IVAR_$_LACNRDeviceMonitorAdapter._isNearby
+ _OBJC_IVAR_$_LACNRDeviceMonitorAdapter._lastReportedReachable
+ __OBJC_$_PROP_LIST_LACNRDeviceMonitorAdapter.94
+ _objc_msgSend$reportReachableStateIfChanged
- __OBJC_$_PROP_LIST_LACNRDeviceMonitorAdapter.90
- _objc_msgSend$isNearby
- _objc_msgSend$isReachable
CStrings:
+ "Device connected (WiFi fallback) changed: %{public}@"
+ "Device nearby (Bluetooth) changed: %{public}@"
+ "Effective reachable state changed: %{public}@ (nearby=%{public}@, connected=%{public}@)"
+ "_isConnected"
+ "_isNearby"
+ "_lastReportedReachable"
+ "reportReachableStateIfChanged"
- "Device reachable status changed: %{public}@"
- "isNearby"

```
