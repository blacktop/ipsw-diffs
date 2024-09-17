## libReverseProxyDevice.dylib

> `/usr/lib/libReverseProxyDevice.dylib`

```diff

-88.0.0.0.0
-  __TEXT.__text: 0x41fc
-  __TEXT.__auth_stubs: 0x6a0
-  __TEXT.__gcc_except_tab: 0x80
+90.0.0.0.0
+  __TEXT.__text: 0x4650
+  __TEXT.__auth_stubs: 0x6b0
   __TEXT.__const: 0x28
-  __TEXT.__cstring: 0xc15
-  __TEXT.__unwind_info: 0x158
+  __TEXT.__gcc_except_tab: 0x84
+  __TEXT.__cstring: 0xd87
+  __TEXT.__unwind_info: 0x160
   __DATA_CONST.__got: 0x78
-  __DATA_CONST.__const: 0xd0
+  __DATA_CONST.__const: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__auth_got: 0x358
+  __AUTH_CONST.__auth_got: 0x360
   __AUTH_CONST.__const: 0x178
-  __AUTH_CONST.__cfstring: 0x900
+  __AUTH_CONST.__cfstring: 0x9e0
   __DATA.__data: 0x4
   __DATA.__bss: 0x68
   __DATA_DIRTY.__data: 0x110

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 69
-  Symbols:   194
-  CStrings:  133
+  Functions: 71
+  Symbols:   197
+  CStrings:  144
 
Symbols:
+ _dispatch_async
CStrings:
+ "fd fd=%!d(MISSING)"
+ "set_client"
+ "Creating RPSocket_fd: %!p(MISSING) for fd: %!d(MISSING) and mode: %!d(MISSING)"
+ "<RPSocket %!p(MISSING) %!p(MISSING): %!@(MISSING) %!@(MISSING)>"
+ "Releasing RPSocket_fd: %!p(MISSING)"
+ "Creating RPSocket: %!p(MISSING) (_sockRef: %!p(MISSING))"
+ "RPSocket %!p(MISSING) (ref: %!p(MISSING)): got signal with event %!d(MISSING) and current _cb: %!p(MISSING)"
+ "<RPSocket %!p(MISSING) %!p(MISSING): %!@(MISSING)>"
+ "Releasing RPSocket: %!p(MISSING) (_sockRef: %!p(MISSING))"
+ "RPSocketRead"
+ "%!@(MISSING) (%!p(MISSING)): connected to %!s(MISSING) as %!s(MISSING)"
+ "~RPSocket"
+ "~RPSocket_fd"
+ "No client callback, missing event %!d(MISSING) for socket %!p(MISSING)"
+ "RPSocket %!p(MISSING): setting client. old: %!p(MISSING). new: %!p(MISSING)"
+ "Reading %!l(MISSING)u bytes from socket %!p(MISSING) to buffer %!p(MISSING)"
- "<RPSocket %!p(MISSING): %!@(MISSING) %!@(MISSING)>"
- "<RPSocket %!p(MISSING): %!@(MISSING)>"
- "No client callback, missing event %!d(MISSING) for socket %!p(MISSING)\n"
- "fd=%!d(MISSING)"
- "%!@(MISSING): connected to %!s(MISSING) as %!s(MISSING)"

```
