## lockdownd

> `/usr/libexec/lockdownd`

```diff

-1329.120.12.0.0
-  __TEXT.__text: 0x10b808
-  __TEXT.__auth_stubs: 0x2d50
+1329.140.5.0.0
+  __TEXT.__text: 0x10b948
+  __TEXT.__auth_stubs: 0x2d60
   __TEXT.__objc_stubs: 0x4400
   __TEXT.__objc_methlist: 0x3520
-  __TEXT.__cstring: 0x5098c
+  __TEXT.__cstring: 0x50b1d
   __TEXT.__const: 0x161f0
   __TEXT.__oslogstring: 0x788
   __TEXT.__gcc_except_tab: 0x3d28

   __TEXT.__objc_methname: 0x4784
   __TEXT.__objc_methtype: 0xeb1
   __TEXT.__services: 0x2d8f
-  __TEXT.__unwind_info: 0x3018
+  __TEXT.__unwind_info: 0x3020
   __TEXT.__eh_frame: 0x10a0
-  __DATA_CONST.__auth_got: 0x16c0
+  __DATA_CONST.__auth_got: 0x16c8
   __DATA_CONST.__got: 0x680
   __DATA_CONST.__auth_ptr: 0x60
   __DATA_CONST.__const: 0xadd8
-  __DATA_CONST.__cfstring: 0x182e0
+  __DATA_CONST.__cfstring: 0x18360
   __DATA_CONST.__objc_classlist: 0x280
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30

   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 36DBC0EA-3293-3220-880E-1786053FA9E1
-  Functions: 3465
-  Symbols:   932
-  CStrings:  12856
+  UUID: 6D3C92F8-1E6D-35B9-9B8F-720420241C61
+  Functions: 3466
+  Symbols:   933
+  CStrings:  12869
 
Symbols:
+ __os_feature_enabled_impl
CStrings:
+ "DisablePairingRecordSecurityRolling"
+ "MobileLockdown"
+ "Pair record rolling is disabled by %s. Should not roll pair records."
+ "Passcode changed (invalidating pair records as buddy is complete)."
+ "Passcode changed (skipping invalidation of pair records as feature is explicitly disabled)."
+ "Passcode changed (skipping invalidation of pair records as we're still in buddy)."
+ "VinylRestore-78~7570"
+ "automation mode"
+ "boot-arg"
+ "feature flag"
+ "path %s has more than one link, something fishy is going on"
- "Automation mode is enabled. Should not roll pair records."
- "VinylRestore-78~7252"

```
