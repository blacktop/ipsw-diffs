## NRDUpdated

> `/usr/libexec/NRDUpdated`

```diff

-2422.40.19.502.1
+2422.40.31.0.4
   __TEXT.__text: 0xbaf8
-  __TEXT.__auth_stubs: 0x660
+  __TEXT.__auth_stubs: 0x680
   __TEXT.__objc_stubs: 0x1b40
   __TEXT.__objc_methlist: 0xc54
   __TEXT.__const: 0x90
   __TEXT.__cstring: 0x10b0
   __TEXT.__gcc_except_tab: 0x1a4
-  __TEXT.__objc_methname: 0x1a67
+  __TEXT.__objc_methname: 0x1a65
   __TEXT.__objc_classname: 0x20f
   __TEXT.__objc_methtype: 0x833
   __TEXT.__oslogstring: 0x1792
   __TEXT.__unwind_info: 0x338
-  __DATA_CONST.__auth_got: 0x340
+  __DATA_CONST.__auth_got: 0x350
   __DATA_CONST.__got: 0x168
   __DATA_CONST.__const: 0x6b0
   __DATA_CONST.__cfstring: 0xe40

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 16F4325C-4C8F-3EF9-ABD7-1290FDEF9FB9
+  UUID: DA4E6C99-2080-371E-8F1C-4B76552D998F
   Functions: 271
-  Symbols:   2149
+  Symbols:   2151
   CStrings:  846
 
Symbols:
+ _objc_getProperty
+ _objc_setProperty_atomic
Functions:
~ -[NRDUpdateDaemonServerImpl needsRelaunchError] : 8 -> 12
~ -[NRDUpdateDaemonServerImpl setNeedsRelaunchError:] : 12 -> 8
CStrings:
+ "22:13:20"
+ "Sep 28 2025"
+ "T@\"NSError\",&,V_needsRelaunchError"
- "20:45:38"
- "Sep 16 2025"
- "T@\"NSError\",&,N,V_needsRelaunchError"

```
