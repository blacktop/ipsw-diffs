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
-  UUID: 53299020-9AD9-3148-AECE-8CF37EF41D7B
-  Functions: 53
+  UUID: C59941BE-74D7-33EA-AEE9-8D2D2B543B80
+  Functions: 54
   Symbols:   58
-  CStrings:  141
+  CStrings:  143
 
CStrings:
+ "writing key %s to sz %d value %x %x\n"
+ "writing key result = %d  smcpOutput.result %d\n"

```
