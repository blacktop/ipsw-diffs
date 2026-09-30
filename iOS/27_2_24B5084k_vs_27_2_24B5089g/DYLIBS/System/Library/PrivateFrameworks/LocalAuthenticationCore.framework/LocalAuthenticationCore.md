## LocalAuthenticationCore

> `/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`

```diff

-2319.40.29.0.0
-  __TEXT.__text: 0x18a404
-  __TEXT.__objc_methlist: 0xd4b0
+2319.40.35.0.1
+  __TEXT.__text: 0x18a4a0
+  __TEXT.__objc_methlist: 0xd4c0
   __TEXT.__const: 0xaed4
   __TEXT.__gcc_except_tab: 0x17c0
-  __TEXT.__oslogstring: 0xb0f5
+  __TEXT.__oslogstring: 0xb115
   __TEXT.__cstring: 0x10a98
   __TEXT.__dlopen_cstrs: 0x705
   __TEXT.__swift5_typeref: 0x410a

   __TEXT.__swift_as_cont: 0x1f4
   __TEXT.__swift_as_ret: 0x138
   __TEXT.__swift5_mpenum: 0x2c
-  __TEXT.__unwind_info: 0x8f90
+  __TEXT.__unwind_info: 0x8f98
   __TEXT.__eh_frame: 0x3200
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __AUTH_CONST.__objc_intobj: 0x360
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__auth_got: 0x1588
-  __AUTH.__objc_data: 0x7730
-  __AUTH.__data: 0x2558
   __DATA.__objc_ivar: 0x8b4
-  __DATA.__data: 0x7798
-  __DATA.__common: 0x38
-  __DATA_DIRTY.__objc_data: 0xe38
-  __DATA_DIRTY.__data: 0x1938
-  __DATA_DIRTY.__bss: 0x218
-  __DATA_DIRTY.__common: 0x80
+  __DATA.__data: 0x2280
+  __DATA.__common: 0x58
+  __DATA_DIRTY.__objc_data: 0x8568
+  __DATA_DIRTY.__data: 0x9398
+  __DATA_DIRTY.__bss: 0x208
+  __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 10929
-  Symbols:   23938
-  CStrings:  3132
+  Functions: 10930
+  Symbols:   23939
+  CStrings:  3133
 
Symbols:
+ -[LACNWPathMonitorAdapter dealloc]
+ _OBJC_IVAR_$_LACNWPathMonitorAdapter._isForwarding
- _OBJC_IVAR_$_LACNWPathMonitorAdapter._isMonitoring
Functions:
~ -[LACFlags featureFlagDimpleKeySentinelEnabled] : 128 -> 164
+ -[LACNWPathMonitorAdapter dealloc]
~ -[LACNWPathMonitorAdapter startMonitoringOnQueue:] : 1380 -> 1444
~ -[LACNWPathMonitorAdapter stopMonitoring] : 444 -> 168
~ -[LACNWPathMonitorAdapter _handlePathUpdate:] : 492 -> 504
CStrings:
+ "Paused network monitoring"
+ "Resumed network monitoring"
- "Stopped network monitoring"
```
