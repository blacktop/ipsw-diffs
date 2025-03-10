## launchd

> `/sbin/launchd`

```diff

-2894.100.80.0.0
-  __TEXT.__text: 0x512e8
+2894.100.81.0.0
+  __TEXT.__text: 0x5137c
   __TEXT.__auth_stubs: 0x2110
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x1f4
   __TEXT.__const: 0x2f0
-  __TEXT.__cstring: 0x14783
+  __TEXT.__cstring: 0x14822
   __TEXT.__launchd: 0x1
   __TEXT.__objc_methname: 0x8
   __TEXT.__objc_classname: 0x1ba

   - /usr/lib/libsandbox.1.dylib
   Functions: 1633
   Symbols:   582
-  CStrings:  2621
+  CStrings:  2622
 
CStrings:
+ "@(#)VERSION:Darwin Bootstrapper Version 7.0.0: Sun Mar  2 09:05:42 PST 2025; root:libxpc_executables-2894.100.81~30/launchd/RELEASE_ARM64E"
+ "Cannot remove old socket path; UIDs mismatch: socket owner=%d, path=%d"
+ "Darwin Bootstrapper Version 7.0.0: Sun Mar  2 09:05:42 PST 2025; root:libxpc_executables-2894.100.81~30/launchd/RELEASE_ARM64E"
+ "Failed to basename_r() a socket path: path=%s, error=%s (%d)"
+ "Failed to dirname_r() a socket path: path=%s, error=%s (%d)"
+ "Failed to fchmodat() a socket: path=%s, mode=%o, error=%s (%d)"
+ "Failed to fchown() secure socket directory: path=%s, uid=%d, gid=%d, error=%s (%d)"
+ "Failed to fchownat() a socket: path=%s, uid=%d, gid=%d, error=%s (%d)"
+ "Failed to mkdir() socket directory: path=%s, mode=%o, error=%s (%d)"
+ "Failed to open() socket directory: path=%s, error=%s (%d)"
- "@(#)VERSION:Darwin Bootstrapper Version 7.0.0: Sat Feb 22 03:16:54 PST 2025; root:libxpc_executables-2894.100.80~21/launchd/RELEASE_ARM64E"
- "Cannot remove old socket path; UIDs mismatch: socket owner = %d, path = %d"
- "Darwin Bootstrapper Version 7.0.0: Sat Feb 22 03:16:54 PST 2025; root:libxpc_executables-2894.100.80~21/launchd/RELEASE_ARM64E"
- "Failed to basename_r() a socket path: error=%s (%d)"
- "Failed to dirname_r() a socket path: error=%s (%d)"
- "Failed to fchmodat() a socket: error=%s (%d)"
- "Failed to fchown() secure socket directory: error=%s (%d)"
- "Failed to fchownat() a socket: error=%s (%d)"
- "Failed to open() socket directory: error=%s (%d)"

```
