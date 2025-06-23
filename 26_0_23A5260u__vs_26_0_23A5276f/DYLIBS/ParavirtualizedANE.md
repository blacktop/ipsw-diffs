## ParavirtualizedANE

> `/System/Library/PrivateFrameworks/ParavirtualizedANE.framework/ParavirtualizedANE`

```diff

-380.7.0.0.0
-  __TEXT.__text: 0x1a180
+380.9.0.0.0
+  __TEXT.__text: 0x1a23c
   __TEXT.__auth_stubs: 0x5e0
   __TEXT.__objc_methlist: 0x638
   __TEXT.__const: 0x190
-  __TEXT.__cstring: 0xe00
-  __TEXT.__oslogstring: 0x4e5f
-  __TEXT.__gcc_except_tab: 0x36e0
+  __TEXT.__cstring: 0xe08
+  __TEXT.__oslogstring: 0x4e9c
+  __TEXT.__gcc_except_tab: 0x36e8
   __TEXT.__unwind_info: 0x5c8
   __TEXT.__objc_classname: 0x2f
   __TEXT.__objc_methname: 0x1eb7

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4D41AD7F-14DA-35CC-B29A-D8765AD3CDAE
+  UUID: 88BAD729-6353-3B60-B010-339299D1EC00
   Functions: 429
   Symbols:   1418
-  CStrings:  953
+  CStrings:  954
 
Functions:
~ -[_ANEVirtualPlatformClient loadModelNewInstance:] : 4936 -> 5124
CStrings:
+ "%@: .asset directory found in path=%@, searching for fileName=%@"
+ "%@: could not find .asset directory in path=%@, searching for fileName=%@ only"
+ "end_model_dump.txt"
+ "end_request_dump.txt"
- "%@: ERROR loadModelNewInstance failed, could not find .asset directory in path=%@!"
- "model_dump.txt"
- "request_dump.txt"

```
