## dhcp6d

> `/usr/libexec/dhcp6d`

```diff

-529.0.0.0.0
-  __TEXT.__text: 0x7ccc
-  __TEXT.__auth_stubs: 0x6c0
+531.0.0.0.0
+  __TEXT.__text: 0x8124
+  __TEXT.__auth_stubs: 0x6d0
   __TEXT.__const: 0xe0
-  __TEXT.__cstring: 0x984
-  __TEXT.__oslogstring: 0x55b
+  __TEXT.__cstring: 0x9b7
+  __TEXT.__oslogstring: 0x5ae
   __TEXT.__unwind_info: 0x1d0
-  __DATA_CONST.__auth_got: 0x360
+  __DATA_CONST.__auth_got: 0x368
   __DATA_CONST.__got: 0xa0
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0x1e0

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /usr/lib/libSystem.B.dylib
-  UUID: 102EB39C-AC6F-3626-B2FA-864FFA58C356
-  Functions: 105
-  Symbols:   135
-  CStrings:  245
+  UUID: FAAA1748-BE2E-36C5-AE4D-4942DC38071D
+  Functions: 107
+  Symbols:   136
+  CStrings:  249
 
Symbols:
+ _unlink
CStrings:
+ "%s re-using flags 0x%x (generation %qu)\n"
+ "%s: SIOCGIFGENERATIONID failed status, %s"
+ "open(%s) failed with ELOOP\n"
+ "unlink(%s) failed, %s\n"

```
