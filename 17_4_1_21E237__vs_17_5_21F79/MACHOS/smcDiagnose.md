## smcDiagnose

> `/usr/libexec/smcDiagnose`

```diff

-111.0.0.0.0
-  __TEXT.__text: 0x3c08
+113.0.0.0.0
+  __TEXT.__text: 0x3db0
   __TEXT.__auth_stubs: 0x2a0
   __TEXT.__objc_stubs: 0x2c0
   __TEXT.__objc_methlist: 0x74
-  __TEXT.__cstring: 0x86c
+  __TEXT.__cstring: 0x8c0
   __TEXT.__const: 0x1c
   __TEXT.__objc_methname: 0x159
   __TEXT.__objc_classname: 0x10

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 53
+  Functions: 54
   Symbols:   58
-  CStrings:  121
+  CStrings:  123
 
CStrings:
+ "writing key %s to sz %d value %x %x\n"
+ "writing key result = %d  smcpOutput.result %d\n"

```
