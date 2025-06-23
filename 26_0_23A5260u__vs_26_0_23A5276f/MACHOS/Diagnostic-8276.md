## Diagnostic-8276

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8276.appex/Diagnostic-8276`

```diff

-54.0.0.0.0
-  __TEXT.__text: 0x1ace0
+56.0.0.0.0
+  __TEXT.__text: 0x1adc8
   __TEXT.__auth_stubs: 0xb20
   __TEXT.__objc_stubs: 0x1b60
   __TEXT.__objc_methlist: 0x8a4
-  __TEXT.__gcc_except_tab: 0x2c34
+  __TEXT.__gcc_except_tab: 0x2c5c
   __TEXT.__const: 0x128
   __TEXT.__objc_methname: 0x221f
-  __TEXT.__cstring: 0x4186
+  __TEXT.__cstring: 0x4203
   __TEXT.__objc_classname: 0xca
   __TEXT.__objc_methtype: 0x9fe
   __TEXT.__oslogstring: 0x11d

   __DATA_CONST.__auth_got: 0x5a8
   __DATA_CONST.__got: 0x418
   __DATA_CONST.__const: 0x5e8
-  __DATA_CONST.__cfstring: 0x31c0
+  __DATA_CONST.__cfstring: 0x3200
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A5AB8581-BAD0-3D00-8A33-2D4709DA0131
+  UUID: 2022F0BA-264C-3840-BE36-1223B161720E
   Functions: 345
   Symbols:   460
-  CStrings:  1450
+  CStrings:  1454
 
Functions:
~ __ZN17DeviceCMInterface23enumerateStreamsIndicesEv : 728 -> 960
CStrings:
+ "IR Stream id not found, (NOTE: possibly not required if not pearl device)"
+ "NULL Type"
+ "com.apple.sensors.cam"
+ "enumeration encountered in unexpected results or retVal = %d and type = %@"
+ "unable to enumerate devices"
- "IR Stream id not found"
- "com.apple.sensors.cam_alt_faceid"
- "unable to enumirate devices"

```
