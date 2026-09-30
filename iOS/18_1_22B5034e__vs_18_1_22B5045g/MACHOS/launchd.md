## launchd

> `/sbin/launchd`

```diff

-2866.40.7.0.0
-  __TEXT.__text: 0x4e934
-  __TEXT.__auth_stubs: 0x2050
+2866.40.9.0.0
+  __TEXT.__text: 0x4ea34
+  __TEXT.__auth_stubs: 0x2060
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x1f4
   __TEXT.__const: 0x2d0
-  __TEXT.__cstring: 0x13bc9
+  __TEXT.__cstring: 0x13bd6
   __TEXT.__launchd: 0x1
   __TEXT.__objc_methname: 0x8
   __TEXT.__objc_classname: 0x1ba
   __TEXT.__objc_methtype: 0x8
   __TEXT.__config: 0x2544
   __TEXT.__dof_launchd: 0x67c
-  __TEXT.__unwind_info: 0x1158
-  __DATA_CONST.__auth_got: 0x1028
+  __TEXT.__unwind_info: 0x1160
+  __DATA_CONST.__auth_got: 0x1030
   __DATA_CONST.__got: 0x188
   __DATA_CONST.__auth_ptr: 0x28
   __DATA_CONST.__const: 0x4ea0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  Functions: 1566
-  Symbols:   570
+  Functions: 1568
+  Symbols:   571
   CStrings:  2543
 
Symbols:
+ _fdopen
+ _renamex_np
- _rename
CStrings:
+ "launchd.log: fdopen(%!s(MISSING)): %!d(MISSING)\n"
+ "@(#)VERSION:Darwin Bootstrapper Version 7.0.0: Fri Aug 30 00:24:05 PDT 2024; root:libxpc_executables-2866.40.9~42/launchd/RELEASE_ARM64E"
+ "SERVICE CACHE DELETE UNEXPECTEDLY DELAYED: %!s(MISSING) replaced: %!s(MISSING) by %!s(MISSING), %!s(MISSING) by %!s(MISSING)"
+ "launchd.log: open(%!s(MISSING)): %!d(MISSING)\n"
+ "SERVICE CACHE DELETE INVARIANT VIOLATED: %!s(MISSING) not found"
+ "Darwin Bootstrapper Version 7.0.0: Fri Aug 30 00:24:05 PDT 2024; root:libxpc_executables-2866.40.9~42/launchd/RELEASE_ARM64E"
- "System session daemon must not bootstrap_look_up User session services (rdar://77349945): endpoint = %!s(MISSING)"
- "com.apple.IDSBlastDoorService"
- "@(#)VERSION:Darwin Bootstrapper Version 7.0.0: Wed Aug 14 04:34:36 PDT 2024; root:libxpc_executables-2866.40.7~20/launchd/RELEASE_ARM64E"
- "xpc-fault"
- "Darwin Bootstrapper Version 7.0.0: Wed Aug 14 04:34:36 PDT 2024; root:libxpc_executables-2866.40.7~20/launchd/RELEASE_ARM64E"
- "launchd.log: fopen(%!s(MISSING)): %!d(MISSING)\n"

```
