## misd

> `/usr/libexec/misd`

```diff

-370.0.0.0.0
-  __TEXT.__text: 0x208e0
+377.0.0.0.0
+  __TEXT.__text: 0x20a3c
   __TEXT.__auth_stubs: 0x11f0
   __TEXT.__objc_stubs: 0x4e0
   __TEXT.__objc_methlist: 0x38c
   __TEXT.__const: 0x158
-  __TEXT.__cstring: 0xb108
+  __TEXT.__cstring: 0xb1d7
   __TEXT.__oslogstring: 0x1e
   __TEXT.__objc_methname: 0x8f6
   __TEXT.__objc_classname: 0x74
   __TEXT.__objc_methtype: 0x69e
-  __TEXT.__unwind_info: 0x4e8
+  __TEXT.__unwind_info: 0x4f0
   __DATA_CONST.__auth_got: 0x900
   __DATA_CONST.__got: 0x2b0
   __DATA_CONST.__const: 0x9e8

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libmrc.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E0FA0271-CBB3-3002-930D-21D720A826A2
-  Functions: 444
+  UUID: BB6E6910-23B4-307E-B301-4D1FF63DD0F2
+  Functions: 445
   Symbols:   381
-  CStrings:  1804
+  CStrings:  1808
 
CStrings:
+ "%s: an internal interface name is unexpectedly BLANK, aborting"
+ "%s: skipping AUTH interface for bridgeability check"
+ "%s: skipping bridging, gwy if '%s'"
+ "int_if->mi_name[0] != '\\0'"
+ "network %s internal interface: '%s' (devtype %d, netrbtype %d)"
- "%s: skipping bridging, gwy if %s"

```
