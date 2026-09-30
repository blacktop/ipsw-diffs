## fskitd

> `/usr/libexec/fskitd`

```diff

-437.0.0.0.1
-  __TEXT.__text: 0x3e32c
+445.0.0.0.0
+  __TEXT.__text: 0x3e510
   __TEXT.__auth_stubs: 0xa90
-  __TEXT.__objc_stubs: 0x4460
-  __TEXT.__objc_methlist: 0x1640
+  __TEXT.__objc_stubs: 0x44a0
+  __TEXT.__objc_methlist: 0x1628
   __TEXT.__const: 0x128
-  __TEXT.__gcc_except_tab: 0x1e18
-  __TEXT.__cstring: 0x264a
-  __TEXT.__oslogstring: 0x3107
+  __TEXT.__gcc_except_tab: 0x1e4c
+  __TEXT.__cstring: 0x269b
+  __TEXT.__oslogstring: 0x3142
   __TEXT.__objc_classname: 0x1f8
-  __TEXT.__objc_methname: 0x51ae
+  __TEXT.__objc_methname: 0x511d
   __TEXT.__objc_methtype: 0x1e59
-  __TEXT.__unwind_info: 0xe90
+  __TEXT.__unwind_info: 0xe98
   __DATA_CONST.__auth_got: 0x558
   __DATA_CONST.__got: 0x2e0
-  __DATA_CONST.__const: 0x1da0
+  __DATA_CONST.__const: 0x1dc0
   __DATA_CONST.__cfstring: 0x9a0
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x48

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x2950
+  __DATA.__objc_const: 0x28f0
   __DATA.__objc_selrefs: 0x13d8
-  __DATA.__objc_ivar: 0x15c
+  __DATA.__objc_ivar: 0x154
   __DATA.__objc_data: 0x500
   __DATA.__data: 0x370
   __DATA.__common: 0x74

   - /usr/lib/libutil.dylib
   Functions: 1179
   Symbols:   275
-  CStrings:  1674
+  CStrings:  1672
 
CStrings:
+ "\x11"
+ "%!s(MISSING):%!@(MISSING): Can't start unload task, previous task (%!@(MISSING)) runs task purpose (%!@(MISSING))"
+ "%!s(MISSING):%!@(MISSING): Resource isn't in loaded/active state, can't start unload task: %!@(MISSING)"
+ "-[fskitdExtensionInstance terminate]_block_invoke"
+ "-[fskitdXPCServer canStartUnloadTask:resource:]_block_invoke"
+ "B16@?0@\"FSModuleIdentity\"8"
+ "fs_filter:"
+ "isSystem"
- "\x13"
- "%!s(MISSING):%!@(MISSING): Resource isn't in loaded state, can't start unload task: %!@(MISSING)"
- "-[fskitdExtensionClient terminateExtension]_block_invoke"
- "Got extension list %!@(MISSING)"
- "T@\"NSString\",R,V_getInitiatorBundleID"
- "T@\"NSString\",R,V_getInitiatorSigningID"
- "_getInitiatorBundleID"
- "_getInitiatorSigningID"
- "getInitiatorBundleID"
- "getInitiatorSigningID"

```
