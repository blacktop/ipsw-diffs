## launchd

> `/sbin/launchd`

```diff

-3089.0.5.0.0
-  __TEXT.__text: 0x53ee0
+3089.0.11.0.0
+  __TEXT.__text: 0x53f00
   __TEXT.__auth_stubs: 0x21e0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x20c
   __TEXT.__const: 0x340
-  __TEXT.__cstring: 0x14ff0
+  __TEXT.__cstring: 0x1500b
   __TEXT.__launchd: 0x1
   __TEXT.__objc_methname: 0x8
   __TEXT.__objc_classname: 0x1d5

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  UUID: DA02ABEA-7F3F-3BC2-A46E-7B8C1DAB51CD
+  UUID: 25981827-D1E2-36DB-B5B7-6AD01937C26E
   Functions: 1709
   Symbols:   597
-  CStrings:  2692
+  CStrings:  2693
 
Functions:
~ sub_10000310c : 1836 -> 1916
~ sub_100006cf4 -> sub_100006d44 : 1856 -> 1788
~ sub_10001212c -> sub_100012138 : 468 -> 488
CStrings:
+ "@(#)VERSION:Darwin Bootstrapper Version 7.0.0: Thu Jul 24 23:59:18 PDT 2025; root:libxpc_executables-3089.0.11~31/launchd/RELEASE_ARM64E"
+ "Darwin Bootstrapper Version 7.0.0: Thu Jul 24 23:59:18 PDT 2025; root:libxpc_executables-3089.0.11~31/launchd/RELEASE_ARM64E"
+ "SanitizersAllocationTraces"
- "@(#)VERSION:Darwin Bootstrapper Version 7.0.0: Fri Jul 11 02:14:32 PDT 2025; root:libxpc_executables-3089.0.5~129/launchd/RELEASE_ARM64E"
- "Darwin Bootstrapper Version 7.0.0: Fri Jul 11 02:14:32 PDT 2025; root:libxpc_executables-3089.0.5~129/launchd/RELEASE_ARM64E"

```
