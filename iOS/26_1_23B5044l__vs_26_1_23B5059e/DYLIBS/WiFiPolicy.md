## WiFiPolicy

> `/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`

```diff

-1035.2.0.0.0
-  __TEXT.__text: 0xbf21c
-  __TEXT.__auth_stubs: 0x1620
+1035.3.0.0.0
+  __TEXT.__text: 0xbf46c
+  __TEXT.__auth_stubs: 0x1630
   __TEXT.__objc_methlist: 0x11700
   __TEXT.__const: 0x648
-  __TEXT.__cstring: 0x1ce0b
-  __TEXT.__oslogstring: 0x3d90
+  __TEXT.__cstring: 0x1ce78
+  __TEXT.__oslogstring: 0x3e14
   __TEXT.__gcc_except_tab: 0x1980
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__unwind_info: 0x2200
   __TEXT.__objc_classname: 0x1407
-  __TEXT.__objc_methname: 0x32bc9
+  __TEXT.__objc_methname: 0x32bc8
   __TEXT.__objc_methtype: 0x3bb9
-  __TEXT.__objc_stubs: 0x18ae0
+  __TEXT.__objc_stubs: 0x18b00
   __DATA_CONST.__got: 0xa60
   __DATA_CONST.__const: 0x2300
   __DATA_CONST.__objc_classlist: 0x530

   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x438
   __DATA_CONST.__objc_arraydata: 0xac0
-  __AUTH_CONST.__auth_got: 0xb28
+  __AUTH_CONST.__auth_got: 0xb30
   __AUTH_CONST.__const: 0x440
-  __AUTH_CONST.__cfstring: 0x192a0
+  __AUTH_CONST.__cfstring: 0x192e0
   __AUTH_CONST.__objc_const: 0x217f0
   __AUTH_CONST.__objc_intobj: 0x1848
   __AUTH_CONST.__objc_arrayobj: 0x3a8
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x7d0
+  __AUTH.__objc_data: 0x7a8
   __DATA.__objc_ivar: 0x215c
   __DATA.__data: 0x1bc0
   __DATA.__bss: 0x2a
-  __DATA_DIRTY.__objc_data: 0x2c10
+  __DATA_DIRTY.__objc_data: 0x2c38
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x2c0
   __DATA_DIRTY.__common: 0x20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7194E63D-897C-3CB6-B946-BC282B901797
-  Functions: 6169
-  Symbols:   20135
-  CStrings:  16698
+  UUID: C021BB0E-D18F-3F31-84C4-2157620DF2E4
+  Functions: 6170
+  Symbols:   20139
+  CStrings:  16706
 
Symbols:
+ -[WiFiDiagnosticReporter isWiFiABCSignatureUnblocked:]
+ ___block_literal_global.43
+ __os_log_debug_impl
+ _objc_msgSend$isWiFiABCSignatureUnblocked:
- -[WiFiDiagnosticReporter SubmitDiagnosticSignatureLazy]
- ___block_literal_global.34
Functions:
- -[WiFiDiagnosticReporter SubmitDiagnosticSignatureLazy]
+ _OUTLINED_FUNCTION_0
~ -[WiFiUsageSession processDriverAvailability:available:version:flags:eventID:reason:subReason:minorReason:reasonString:] : 2868 -> 2920
+ -[WiFiDiagnosticReporter isWiFiABCSignatureUnblocked:]
CStrings:
+ "%s: ABC signature is currently blocked by request until %@"
+ "%s: ABC signature is unblocked: %@"
+ "%s: testing for key %@ have %@ and %@"
+ "-[WiFiDiagnosticReporter isWiFiABCSignatureUnblocked:]"
+ "com.apple.wifi.abc"
+ "isWiFiABCSignatureUnblocked:"
+ "mute-abc-driver-availability-until"
- "SubmitDiagnosticSignatureLazy"

```
