## PurpleReverseProxy

> `/usr/libexec/PurpleReverseProxy`

```diff

-88.0.0.0.0
-  __TEXT.__text: 0x5e90
+90.0.0.0.0
+  __TEXT.__text: 0x6530
   __TEXT.__auth_stubs: 0x7c0
-  __TEXT.__gcc_except_tab: 0xb8
   __TEXT.__const: 0x6c
-  __TEXT.__cstring: 0x1191
-  __TEXT.__unwind_info: 0x1b0
+  __TEXT.__gcc_except_tab: 0xc0
+  __TEXT.__cstring: 0x1379
+  __TEXT.__unwind_info: 0x1b8
   __DATA_CONST.__auth_got: 0x3e8
   __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0x458
-  __DATA_CONST.__cfstring: 0xd60
+  __DATA_CONST.__const: 0x478
+  __DATA_CONST.__cfstring: 0xe80
   __DATA.__data: 0x19c
   __DATA.__bss: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 95
+  Functions: 99
   Symbols:   143
-  CStrings:  186
+  CStrings:  200
 
CStrings:
+ "~RPSocket_lockdown_service"
+ "Releasing RPSocket_fd: %!p(MISSING)"
+ "Creating RPSocket_fd: %!p(MISSING) for fd: %!d(MISSING) and mode: %!d(MISSING)"
+ "Releasing RPSocket_lockdown_service: %!p(MISSING)"
+ "set_client"
+ "<RPSocket %!p(MISSING) %!p(MISSING): %!@(MISSING) %!@(MISSING)>"
+ "Creating RPSocket: %!p(MISSING) (_sockRef: %!p(MISSING))"
+ "Releasing RPSocket: %!p(MISSING) (_sockRef: %!p(MISSING))"
+ "~RPSocket_fd"
+ "RPSocket %!p(MISSING): setting client. old: %!p(MISSING). new: %!p(MISSING)"
+ "fd fd=%!d(MISSING)"
+ "No client callback, missing event %!d(MISSING) for socket %!p(MISSING)"
+ "<RPSocket %!p(MISSING) %!p(MISSING): %!@(MISSING)>"
+ "RPSocketRead"
+ "Reading %!l(MISSING)u bytes from socket %!p(MISSING) to buffer %!p(MISSING)"
+ "%!@(MISSING): with unknown mode with address: %!s(MISSING)"
+ "RPSocket %!p(MISSING) (ref: %!p(MISSING)): got signal with event %!d(MISSING) and current _cb: %!p(MISSING)"
+ "~RPSocket"
+ "lockdown_service service=%!s(MISSING)"
- "<RPSocket %!p(MISSING): %!@(MISSING)>"
- "service=%!s(MISSING)"
- "No client callback, missing event %!d(MISSING) for socket %!p(MISSING)\n"
- "fd=%!d(MISSING)"
- "<RPSocket %!p(MISSING): %!@(MISSING) %!@(MISSING)>"

```
