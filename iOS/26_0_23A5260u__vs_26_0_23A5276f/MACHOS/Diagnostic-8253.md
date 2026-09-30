## Diagnostic-8253

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8253.appex/Diagnostic-8253`

```diff

-54.0.0.0.0
-  __TEXT.__text: 0x127b8
+56.0.0.0.0
+  __TEXT.__text: 0x128a0
   __TEXT.__auth_stubs: 0x6d0
   __TEXT.__objc_stubs: 0x780
   __TEXT.__objc_methlist: 0xe0
-  __TEXT.__gcc_except_tab: 0x2070
+  __TEXT.__gcc_except_tab: 0x2098
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x39f5
+  __TEXT.__cstring: 0x3a72
   __TEXT.__objc_classname: 0x20
   __TEXT.__objc_methname: 0x5a1
   __TEXT.__objc_methtype: 0x7bd

   __DATA_CONST.__auth_got: 0x378
   __DATA_CONST.__got: 0x320
   __DATA_CONST.__const: 0x4f8
-  __DATA_CONST.__cfstring: 0x2f60
+  __DATA_CONST.__cfstring: 0x2fa0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x120

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 016A0BA4-7241-3F83-9E0D-D98C1F8D7387
+  UUID: D7C7323A-E720-3245-8DE7-CC2F8EB7F222
   Functions: 204
   Symbols:   351
-  CStrings:  917
+  CStrings:  921
 
Functions:
~ __ZN17DeviceCMInterface23enumerateStreamsIndicesEv : 728 -> 960
CStrings:
+ "IR Stream id not found, (NOTE: possibly not required if not pearl device)"
+ "NULL Type"
+ "com.apple.sensors.cam"
+ "enumeration encountered in unexpected results or retVal = %d and type = %@"
- "IR Stream id not found"
- "com.apple.sensors.cam_alt_faceid"

```
