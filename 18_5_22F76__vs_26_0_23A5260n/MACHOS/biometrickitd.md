## biometrickitd

> `/usr/libexec/biometrickitd`

```diff

-511.100.15.0.0
-  __TEXT.__text: 0xb0c
+544.0.0.0.0
+  __TEXT.__text: 0xd04
   __TEXT.__auth_stubs: 0x1e0
   __TEXT.__objc_stubs: 0x240
   __TEXT.__const: 0x18
-  __TEXT.__cstring: 0x18f
-  __TEXT.__oslogstring: 0x153
+  __TEXT.__cstring: 0x1a0
+  __TEXT.__oslogstring: 0x19b
   __TEXT.__objc_methname: 0x10a
-  __TEXT.__unwind_info: 0x70
+  __TEXT.__unwind_info: 0x80
   __DATA_CONST.__auth_got: 0xf8
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__const: 0x60

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9FC5879A-BF26-3E8A-8EF3-3CAAF24FFB83
-  Functions: 5
+  UUID: EDC1D4CC-869E-389D-9356-5F201C372261
+  Functions: 11
   Symbols:   45
-  CStrings:  45
+  CStrings:  47
 
Symbols:
+ __os_crash
+ _objc_retain_x28
- _objc_release_x22
- _objc_release_x25
CStrings:
+ "0"
+ "Error initializing BKDM plugin from %@: err=0x%x\n"
+ "Error loading BKDM plugin from %@: %s\n"
+ "Failed to initialize biometrickitd"
+ "No BKDM plugin initialized\n"
- "!err || (err == 19)"
- "EXIT\n"
- "error loading BKDM plugin from %@: %s\n"

```
