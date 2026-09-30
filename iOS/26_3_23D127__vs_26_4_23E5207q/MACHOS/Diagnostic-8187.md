## Diagnostic-8187

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8187.appex/Diagnostic-8187`

```diff

-1066.80.3.0.0
-  __TEXT.__text: 0xa684
-  __TEXT.__auth_stubs: 0x650
+1066.100.26.0.0
+  __TEXT.__text: 0xacb4
+  __TEXT.__auth_stubs: 0x620
   __TEXT.__objc_stubs: 0x2760
   __TEXT.__objc_methlist: 0xfe4
-  __TEXT.__gcc_except_tab: 0x91c
-  __TEXT.__const: 0x224
+  __TEXT.__gcc_except_tab: 0x8bc
+  __TEXT.__const: 0x1fc
   __TEXT.__objc_methname: 0x3063
   __TEXT.__objc_classname: 0x1b0
   __TEXT.__objc_methtype: 0xb3d
-  __TEXT.__cstring: 0x7da
+  __TEXT.__cstring: 0x94c
   __TEXT.__oslogstring: 0xce7
-  __TEXT.__unwind_info: 0x3b0
-  __DATA_CONST.__auth_got: 0x340
+  __TEXT.__unwind_info: 0x458
+  __DATA_CONST.__auth_got: 0x328
   __DATA_CONST.__got: 0x1c0
   __DATA_CONST.__const: 0xe0
   __DATA_CONST.__cfstring: 0x7a0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0ABDACC5-ADE6-3543-8AE4-00BA7ED4105B
-  Functions: 288
-  Symbols:   222
-  CStrings:  938
+  UUID: AB165D75-6684-3C15-84E1-554E6BF3B107
+  Functions: 294
+  Symbols:   219
+  CStrings:  939
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x23
- _objc_retain_x8
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CIZYugAMHJKkrO-LGeoAgmlsSrfqhix-Wb9fGYQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/Library/Caches/com.apple.xbs/773BF30D-B716-47C5-A91A-A1D640A76A3A/TemporaryDirectory.QegTFD/Sources/Diagnostics/DiagnosticsService/Diagnostic-8187/CPUDrainOperation.m"
- "/Library/Caches/com.apple.xbs/Sources/Diagnostics/DiagnosticsService/Diagnostic-8187/CPUDrainOperation.m"

```
