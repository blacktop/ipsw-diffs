## AutoBugCaptureCore

> `/System/Library/PrivateFrameworks/AutoBugCaptureCore.framework/Versions/A/AutoBugCaptureCore`

```diff

-469.0.0.0.0
-  __TEXT.__text: 0x78280
+469.40.3.0.0
+  __TEXT.__text: 0x78074
   __TEXT.__objc_methlist: 0x5bcc
-  __TEXT.__cstring: 0x4ed3
+  __TEXT.__cstring: 0x4e5a
   __TEXT.__const: 0x290
   __TEXT.__oslogstring: 0xe43b
   __TEXT.__gcc_except_tab: 0xdb4

   __DATA_CONST.__objc_selrefs: 0x3490
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1e0
-  __DATA_CONST.__objc_arraydata: 0x630
+  __DATA_CONST.__objc_arraydata: 0x5a8
   __DATA_CONST.__got: 0x4d8
   __AUTH_CONST.__const: 0x1eb0
-  __AUTH_CONST.__cfstring: 0x6900
+  __AUTH_CONST.__cfstring: 0x6800
   __AUTH_CONST.__objc_const: 0xb990
-  __AUTH_CONST.__objc_dictobj: 0x640
+  __AUTH_CONST.__objc_dictobj: 0x5a0
   __AUTH_CONST.__objc_intobj: 0x2d0
-  __AUTH_CONST.__objc_arrayobj: 0x468
+  __AUTH_CONST.__objc_arrayobj: 0x3f0
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__auth_got: 0x758
   __AUTH.__objc_data: 0x7d0

   - /usr/lib/libobjc.A.dylib
   Functions: 2268
   Symbols:   5517
-  CStrings:  2189
+  CStrings:  2181
 
Functions:
~ -[SystemProperties init] : 1504 -> 1508
~ +[CaseDampeningExceptions allowDampeningExceptionFor:] : 2280 -> 2060
~ -[DiagnosticsController addSpecialProjectsDiagnosticActions:] : 316 -> 8
CStrings:
+ "Lazuli"
+ "RCSGroupForking"
- "4388"
- "4399"
- "7932"
- "Proxima"
- "Thread"
- "WiFi Watchdog"
- "com.apple.DiagnosticExtensions.ConnectivityDE"
- "proxima"
- "proxima-diags"
- "smsType: Emergency rat: Unknown"
```
