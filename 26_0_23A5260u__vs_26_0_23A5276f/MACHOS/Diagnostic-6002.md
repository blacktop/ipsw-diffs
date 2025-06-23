## Diagnostic-6002

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6002.appex/Diagnostic-6002`

```diff

-54.0.0.0.0
-  __TEXT.__text: 0x1b3a0
+56.0.0.0.0
+  __TEXT.__text: 0x1bbcc
   __TEXT.__auth_stubs: 0xb30
   __TEXT.__objc_stubs: 0x1d00
   __TEXT.__objc_methlist: 0x8e4
-  __TEXT.__gcc_except_tab: 0x2d08
+  __TEXT.__gcc_except_tab: 0x2f50
   __TEXT.__const: 0x128
   __TEXT.__objc_methname: 0x2381
-  __TEXT.__cstring: 0x42da
+  __TEXT.__cstring: 0x447d
   __TEXT.__objc_classname: 0xc0
   __TEXT.__objc_methtype: 0xa6d
-  __TEXT.__oslogstring: 0xec
-  __TEXT.__unwind_info: 0x7e0
+  __TEXT.__oslogstring: 0x26
+  __TEXT.__unwind_info: 0x7e8
   __DATA_CONST.__auth_got: 0x5b0
   __DATA_CONST.__got: 0x428
   __DATA_CONST.__const: 0x5e8
-  __DATA_CONST.__cfstring: 0x3280
+  __DATA_CONST.__cfstring: 0x3380
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 14CC63B5-50F9-372E-94C1-D5DF8B5A255D
+  UUID: 05B577BD-442B-3DD2-8C48-983DA7E961F9
   Functions: 350
   Symbols:   463
-  CStrings:  1482
+  CStrings:  1493
 
Functions:
~ sub_100005718 : 712 -> 2024
~ sub_100005d44 -> sub_100006264 : 2112 -> 2436
~ sub_10000663c -> sub_100006ca0 : 144 -> 284
~ sub_1000066cc -> sub_100006dbc : 416 -> 500
~ __ZN17DeviceCMInterface23enumerateStreamsIndicesEv : 728 -> 960
CStrings:
+ "/Library/Caches/com.apple.xbs/Sources/DepthDiagnostics/Diagnostic-6002/PeCoNetViewController.mm"
+ "IR Stream id not found, (NOTE: possibly not required if not pearl device)"
+ "NULL Type"
+ "com.apple.sensors.cam"
+ "enumeration encountered in unexpected results or retVal = %d and type = %@"
+ "unable to enumerate devices"
- "IR Stream id not found"
- "com.apple.sensors.cam_alt_faceid"
- "unable to enumirate devices"

```
