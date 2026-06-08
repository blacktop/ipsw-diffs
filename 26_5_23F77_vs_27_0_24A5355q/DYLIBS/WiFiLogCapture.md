## WiFiLogCapture

> `/System/Library/PrivateFrameworks/WiFiLogCapture.framework/WiFiLogCapture`

```diff

-1175.1.0.0.0
-  __TEXT.__text: 0x72c
-  __TEXT.__auth_stubs: 0x1c0
+1185.5.0.0.0
+  __TEXT.__text: 0x714
   __TEXT.__objc_methlist: 0x74
   __TEXT.__const: 0x58
   __TEXT.__gcc_except_tab: 0x30
-  __TEXT.__cstring: 0x20f
-  __TEXT.__unwind_info: 0xa0
-  __TEXT.__objc_classname: 0x13
-  __TEXT.__objc_methname: 0x16a
-  __TEXT.__objc_methtype: 0xba
-  __TEXT.__objc_stubs: 0x80
-  __DATA_CONST.__got: 0x20
+  __TEXT.__cstring: 0x211
+  __TEXT.__unwind_info: 0x98
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xa0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xf0
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__cfstring: 0xc0
   __AUTH_CONST.__objc_const: 0x110
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0xc
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/CoreCaptureControl.framework/CoreCaptureControl
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3CB29386-1FE5-37F0-B4B4-3C57C1C10EBE
+  UUID: EF3E3457-7952-3B79-B613-D92A3AEC0291
   Functions: 13
-  Symbols:   85
-  CStrings:  54
+  Symbols:   88
+  CStrings:  28
 
Symbols:
+ _objc_retain_x1
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x8
- _objc_retain_x22
Functions:
~ -[WiFiLogDumpTaker XPCConnection:] : 260 -> 256
~ -[WiFiLogDumpTaker takeWiFiCoreCaptureDumpWithReason:callback:] : 196 -> 192
~ ___68-[WiFiLogDumpTaker takeWiFiDiagnosticsDumpWithPath:reason:callback:]_block_invoke : 224 -> 216
~ -[WiFiLogDumpTaker takeWiFiDiagnosticsDumpWithPath:reason:shouldTryFallback:callback:] : 196 -> 188
CStrings:
- ".cxx_destruct"
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_xpc_object>\""
- "@16@0:8"
- "@24@0:8r*16"
- "B"
- "B16@0:8"
- "TB,R,N,V_didLastCaptureFallback"
- "WiFiLogDumpTaker"
- "XPCConnection:"
- "_didLastCaptureFallback"
- "didLastCaptureFallback"
- "event_queue"
- "handleConnection:"
- "init"
- "takeWiFiCoreCaptureDumpWithReason:callback:"
- "takeWiFiDiagnosticsDumpWithPath:reason:callback:"
- "takeWiFiDiagnosticsDumpWithPath:reason:shouldTryFallback:callback:"
- "takeWiFiDiagnosticsDumpWithPathAndReason:::"
- "v16@0:8"
- "v24@0:8@16"
- "v32@0:8r*16@?24"
- "v40@0:8@?16r*24r*32"
- "v40@0:8r*16r*24@?32"
- "v44@0:8r*16r*24B32@?36"
- "xpc_connection"

```
