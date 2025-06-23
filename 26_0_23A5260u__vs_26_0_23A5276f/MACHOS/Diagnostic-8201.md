## Diagnostic-8201

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8201.appex/Diagnostic-8201`

```diff

-54.0.0.0.0
-  __TEXT.__text: 0x242ac
+56.0.0.0.0
+  __TEXT.__text: 0x24394
   __TEXT.__auth_stubs: 0x800
   __TEXT.__objc_stubs: 0xa00
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x31c
-  __TEXT.__gcc_except_tab: 0x2570
+  __TEXT.__gcc_except_tab: 0x2598
   __TEXT.__const: 0x100
-  __TEXT.__cstring: 0x56f6
+  __TEXT.__cstring: 0x5773
   __TEXT.__objc_classname: 0x55
   __TEXT.__objc_methname: 0xb71
   __TEXT.__objc_methtype: 0x657

   __DATA_CONST.__auth_got: 0x410
   __DATA_CONST.__got: 0x350
   __DATA_CONST.__const: 0x558
-  __DATA_CONST.__cfstring: 0x3b00
+  __DATA_CONST.__cfstring: 0x3b40
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 73EB70B0-476B-3B80-8582-E9807CAA7E97
+  UUID: 5D017C7F-5F9A-3C30-9B63-6A50AF4E6D01
   Functions: 439
   Symbols:   407
-  CStrings:  1410
+  CStrings:  1414
 
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
