## WiFiLogCapture

> `/System/Library/PrivateFrameworks/WiFiLogCapture.framework/WiFiLogCapture`

```diff

-1160.1.0.0.0
-  __TEXT.__text: 0x714
-  __TEXT.__auth_stubs: 0x1f0
+1166.5.0.0.0
+  __TEXT.__text: 0x72c
+  __TEXT.__auth_stubs: 0x1c0
   __TEXT.__objc_methlist: 0x74
   __TEXT.__const: 0x58
   __TEXT.__gcc_except_tab: 0x30
   __TEXT.__cstring: 0x20f
-  __TEXT.__unwind_info: 0x98
+  __TEXT.__unwind_info: 0xa0
   __TEXT.__objc_classname: 0x13
   __TEXT.__objc_methname: 0x16a
   __TEXT.__objc_methtype: 0xba

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x108
+  __AUTH_CONST.__auth_got: 0xf0
   __AUTH_CONST.__cfstring: 0xc0
   __AUTH_CONST.__objc_const: 0x110
   __AUTH.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/CoreCaptureControl.framework/CoreCaptureControl
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5E4642EE-4A6C-305E-AFAA-EB429AD51B8D
+  UUID: C099BC2A-F675-305E-8575-2251151E6C07
   Functions: 13
-  Symbols:   88
+  Symbols:   85
   CStrings:  54
 
Symbols:
+ _objc_retain_x22
- _objc_retain_x1
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x8
Functions:
~ -[WiFiLogDumpTaker XPCConnection:] : 256 -> 260
~ -[WiFiLogDumpTaker takeWiFiCoreCaptureDumpWithReason:callback:] : 192 -> 196
~ ___68-[WiFiLogDumpTaker takeWiFiDiagnosticsDumpWithPath:reason:callback:]_block_invoke : 216 -> 224
~ -[WiFiLogDumpTaker takeWiFiDiagnosticsDumpWithPath:reason:shouldTryFallback:callback:] : 188 -> 196

```
