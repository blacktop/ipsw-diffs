## Diagnostic-8288

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8288.appex/Diagnostic-8288`

```diff

-54.0.0.0.0
-  __TEXT.__text: 0xd868
+56.0.0.0.0
+  __TEXT.__text: 0xd950
   __TEXT.__auth_stubs: 0x6d0
   __TEXT.__objc_stubs: 0x3c0
   __TEXT.__objc_methlist: 0x50
-  __TEXT.__cstring: 0x2f5c
-  __TEXT.__gcc_except_tab: 0x1604
+  __TEXT.__cstring: 0x2fe4
+  __TEXT.__gcc_except_tab: 0x162c
   __TEXT.__const: 0x18
   __TEXT.__oslogstring: 0x1d
   __TEXT.__objc_classname: 0x1a

   __DATA_CONST.__auth_got: 0x378
   __DATA_CONST.__got: 0x2f8
   __DATA_CONST.__const: 0x480
-  __DATA_CONST.__cfstring: 0x20c0
+  __DATA_CONST.__cfstring: 0x2100
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x90

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0A02DDDB-9B4E-3C53-BE11-507458BF848B
+  UUID: FB855A47-F4CA-3BCA-9AF4-546F67EA8C24
   Functions: 145
   Symbols:   324
-  CStrings:  634
+  CStrings:  638
 
Functions:
~ __ZN17DeviceCMInterface23enumerateStreamsIndicesEv : 728 -> 960
CStrings:
+ "IR Stream id not found, (NOTE: possibly not required if not pearl device)"
+ "NULL Type"
+ "enumeration encountered in unexpected results or retVal = %d and type = %@"
- "IR Stream id not found"

```
