## SampleAnalysis

> `/System/Library/PrivateFrameworks/SampleAnalysis.framework/SampleAnalysis`

```diff

-415.0.0.0.0
-  __TEXT.__text: 0xf0200
+415.0.1.0.0
+  __TEXT.__text: 0xf0180
   __TEXT.__auth_stubs: 0x1760
   __TEXT.__objc_methlist: 0x5e9c
-  __TEXT.__const: 0x348
+  __TEXT.__const: 0x358
   __TEXT.__dlopen_cstrs: 0x108
-  __TEXT.__cstring: 0x18399
-  __TEXT.__oslogstring: 0xc615
+  __TEXT.__cstring: 0x1833c
+  __TEXT.__oslogstring: 0xc5dd
   __TEXT.__gcc_except_tab: 0x9d64
   __TEXT.__unwind_info: 0x2118
   __TEXT.__objc_classname: 0xb34

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 62776516-FBA6-3037-B1A3-FED20B1544EC
+  UUID: B8177F4D-2B3D-3D15-9633-51352AF133BD
   Functions: 2829
   Symbols:   9702
-  CStrings:  8564
+  CStrings:  8561
 
Functions:
~ -[SAThreadCallTree initWithThread:dispatchQueue:swiftTask:rootObjects:] : 304 -> 176
CStrings:
- "Neither thread nor dispatchQueue nor swiftTask provided"
- "thread || dispatchQueue || swiftTask"

```
