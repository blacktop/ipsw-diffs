## GAXSpringboardServer

> `/System/Library/AccessibilityBundles/GAXSpringboardServer.bundle/GAXSpringboardServer`

```diff

-973.8.0.0.0
-  __TEXT.__text: 0x14028
-  __TEXT.__auth_stubs: 0x690
+973.11.0.0.0
+  __TEXT.__text: 0x141bc
+  __TEXT.__auth_stubs: 0x6a0
   __TEXT.__objc_stubs: 0x2a20
   __TEXT.__objc_methlist: 0x152c
   __TEXT.__const: 0x58
-  __TEXT.__gcc_except_tab: 0x378
+  __TEXT.__gcc_except_tab: 0x3a4
   __TEXT.__cstring: 0x4d1f
   __TEXT.__objc_methname: 0x507c
-  __TEXT.__oslogstring: 0xedd
+  __TEXT.__oslogstring: 0x1045
   __TEXT.__objc_classname: 0xdcd
   __TEXT.__objc_methtype: 0xe60
   __TEXT.__dlopen_cstrs: 0xaa
-  __TEXT.__unwind_info: 0x6a4
-  __DATA_CONST.__auth_got: 0x358
+  __TEXT.__unwind_info: 0x6ac
+  __DATA_CONST.__auth_got: 0x360
   __DATA_CONST.__got: 0x98
   __DATA_CONST.__const: 0x10a0
   __DATA_CONST.__cfstring: 0x4800

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 527
-  Symbols:   539
-  CStrings:  1565
+  Functions: 528
+  Symbols:   540
+  CStrings:  1569
 
Symbols:
+ __os_log_debug_impl
CStrings:
+ "App visibility: %d state: %d (bundleID %@)"
+ "Guided Access did finish launching app with bundle ID: %@"
+ "Handling app launch request; need to make SpringBoard frontmost"
+ "Making a new application object from AXSpringBoardServer to make sure we're not stuck on a stale one (if the app is being reinstalled or updated)"
+ "Trying to launch the app. Capped by the launch timer beginning roughly now..."
- "App visibility: %d state: %d"

```
