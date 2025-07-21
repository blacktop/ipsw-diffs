## fskitd

> `/usr/libexec/fskitd`

```diff

-531.140.7.0.0
-  __TEXT.__text: 0x404d8
+531.140.7.0.2
+  __TEXT.__text: 0x410f4
   __TEXT.__auth_stubs: 0xb00
-  __TEXT.__objc_stubs: 0x4680
-  __TEXT.__objc_methlist: 0x1d14
+  __TEXT.__objc_stubs: 0x46c0
+  __TEXT.__objc_methlist: 0x1d8c
   __TEXT.__const: 0x130
-  __TEXT.__gcc_except_tab: 0x1fec
-  __TEXT.__cstring: 0x25f5
-  __TEXT.__oslogstring: 0x33d0
+  __TEXT.__gcc_except_tab: 0x2014
+  __TEXT.__cstring: 0x27b4
+  __TEXT.__oslogstring: 0x342a
   __TEXT.__objc_classname: 0x21a
-  __TEXT.__objc_methname: 0x5390
+  __TEXT.__objc_methname: 0x54c3
   __TEXT.__objc_methtype: 0x1fae
-  __TEXT.__unwind_info: 0xee8
+  __TEXT.__unwind_info: 0xf20
   __DATA_CONST.__auth_got: 0x590
   __DATA_CONST.__got: 0x338
   __DATA_CONST.__const: 0x1fc0

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x1fd8
-  __DATA.__objc_selrefs: 0x1548
+  __DATA.__objc_const: 0x1ff8
+  __DATA.__objc_selrefs: 0x1578
   __DATA.__objc_ivar: 0x170
   __DATA.__objc_data: 0x550
   __DATA.__data: 0x6c0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: A2507E47-E433-3E12-B073-FD87B7934E04
-  Functions: 1206
+  UUID: DC63F7B5-4095-317D-BCA9-4D30211B06AE
+  Functions: 1220
   Symbols:   293
-  CStrings:  1824
+  CStrings:  1838
 
Functions (added):
+ sub_10001f15c
+ sub_10001f89c
+ sub_10001f93c
+ sub_10001fb20
+ sub_100022d88
+ sub_100023528
+ sub_100023834
+ sub_100023b1c
+ sub_100039c04
+ sub_100039d64
+ sub_10003ee18
+ sub_10003f14c
+ sub_10003f62c
+ sub_10003fa70
CStrings:
+ "%s: No module found with short name '%@'"
+ "%s: No moduleIdentity found for fsShortName (%@)"
+ "-[fskitdXPCServer activateVolume:shortName:options:auditToken:replyHandler:]"
+ "-[fskitdXPCServer deactivateVolume:shortName:numericOptions:auditToken:replyHandler:]"
+ "-[fskitdXPCServer getBundleIDFromShortName:user:]_block_invoke"
+ "-[fskitdXPCServer getModuleIdentityFromShortName:user:]_block_invoke"
+ "-[fskitdXPCServer loadResource:shortName:options:auditToken:replyHandler:]"
+ "-[fskitdXPCServer unloadResource:shortName:options:auditToken:replyHandler:]"
+ "activateVolume:shortName:options:auditToken:replyHandler:"
+ "deactivateVolume:shortName:numericOptions:auditToken:replyHandler:"
+ "getBundleIDFromShortName:user:"
+ "getModuleIdentityFromShortName:user:"
+ "loadResource:shortName:options:auditToken:replyHandler:"
+ "unloadResource:shortName:options:auditToken:replyHandler:"

```
