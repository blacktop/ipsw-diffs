## fskitd

> `/usr/libexec/fskitd`

```diff

-737.0.14.0.1
-  __TEXT.__text: 0x43c94
-  __TEXT.__auth_stubs: 0xb00
-  __TEXT.__objc_stubs: 0x4960
-  __TEXT.__objc_methlist: 0x1e84
+737.0.17.0.2
+  __TEXT.__text: 0x445a0
+  __TEXT.__auth_stubs: 0xb10
+  __TEXT.__objc_stubs: 0x49c0
+  __TEXT.__objc_methlist: 0x1efc
   __TEXT.__const: 0x130
-  __TEXT.__gcc_except_tab: 0x2358
-  __TEXT.__oslogstring: 0x39f8
-  __TEXT.__cstring: 0x2ca6
+  __TEXT.__gcc_except_tab: 0x234c
+  __TEXT.__oslogstring: 0x3a21
+  __TEXT.__cstring: 0x2dbc
   __TEXT.__objc_classname: 0x223
-  __TEXT.__objc_methname: 0x5715
-  __TEXT.__objc_methtype: 0x1e6d
-  __TEXT.__unwind_info: 0xf70
-  __DATA_CONST.__auth_got: 0x590
+  __TEXT.__objc_methname: 0x5860
+  __TEXT.__objc_methtype: 0x1e88
+  __TEXT.__unwind_info: 0xf88
+  __DATA_CONST.__auth_got: 0x598
   __DATA_CONST.__got: 0x350
   __DATA_CONST.__const: 0x20f8
   __DATA_CONST.__cfstring: 0x860

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x2190
-  __DATA.__objc_selrefs: 0x1688
+  __DATA.__objc_const: 0x21b0
+  __DATA.__objc_selrefs: 0x16b8
   __DATA.__objc_ivar: 0x170
   __DATA.__objc_data: 0x5a0
   __DATA.__data: 0x6b0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: 882C37CA-5365-384F-8BB5-C6687975D515
-  Functions: 1272
-  Symbols:   296
-  CStrings:  1938
+  UUID: 92C6C9EE-8292-3589-BD64-4B4AB92AC6F8
+  Functions: 1283
+  Symbols:   297
+  CStrings:  1950
 
Symbols:
+ _objc_retain_x9
CStrings:
+ "%s: No module found with short name '%@'"
+ "-[fskitdXPCServer activateVolume:shortName:options:auditToken:replyHandler:]"
+ "-[fskitdXPCServer deactivateVolume:shortName:numericOptions:auditToken:replyHandler:]"
+ "-[fskitdXPCServer getModuleIdentityFromShortName:user:]_block_invoke"
+ "-[fskitdXPCServer loadResource:shortName:options:auditToken:replyHandler:]"
+ "-[fskitdXPCServer unloadResource:shortName:options:auditToken:replyHandler:]"
+ "activateVolume:shortName:options:auditToken:replyHandler:"
+ "cleanupTaskAfterError:resource:bundleIdentifier:token:"
+ "deactivateVolume:shortName:numericOptions:auditToken:replyHandler:"
+ "getModuleIdentityFromShortName:user:"
+ "loadResource:shortName:options:auditToken:replyHandler:"
+ "unloadResource:shortName:options:auditToken:replyHandler:"
+ "v72@0:8@16@24@32{?=[8I]}40"
- "-[fskitdXPCServer _formatResource:usingBundle:options:auditToken:connection:replyHandler:]_block_invoke_3"

```
