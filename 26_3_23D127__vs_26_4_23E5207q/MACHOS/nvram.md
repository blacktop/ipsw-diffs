## nvram

> `/usr/sbin/nvram`

```diff

-1039.0.0.0.0
-  __TEXT.__text: 0x212c
+1042.100.6.0.0
+  __TEXT.__text: 0x21dc
   __TEXT.__auth_stubs: 0x470
-  __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x9cb
-  __TEXT.__unwind_info: 0xb8
+  __TEXT.__const: 0x48
+  __TEXT.__cstring: 0x9fa
+  __TEXT.__unwind_info: 0xd0
   __DATA_CONST.__auth_got: 0x238
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__auth_ptr: 0x8

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
-  UUID: 4D82A9B7-CB31-310A-8429-18898B4DFB1D
-  Functions: 37
+  UUID: 0A0E8A8B-FEC3-3E58-B899-C7D896915021
+  Functions: 48
   Symbols:   87
-  CStrings:  83
+  CStrings:  84
 
CStrings:
+ "\t-s         force sync changes to storage"
+ "nvram [-x|-X] [-p] [-f filename] [-d name] [-c] [-s] name[=value] ..."
- "nvram [-x|-X] [-p] [-f filename] [-d name] [-c] name[=value] ..."

```
