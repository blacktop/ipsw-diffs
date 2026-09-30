## RemoteServiceDiscovery

> `/System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery`

```diff

-202.40.9.0.0
-  __TEXT.__text: 0xf0a0
+202.40.12.0.0
+  __TEXT.__text: 0xf250
   __TEXT.__auth_stubs: 0xab0
   __TEXT.__objc_methlist: 0x4a0
   __TEXT.__const: 0xa8
   __TEXT.__cstring: 0x136a
-  __TEXT.__gcc_except_tab: 0x3bc
-  __TEXT.__oslogstring: 0x1cc3
+  __TEXT.__gcc_except_tab: 0x3e8
+  __TEXT.__oslogstring: 0x1d19
   __TEXT.__unwind_info: 0x500
   __TEXT.__objc_classname: 0xbe
   __TEXT.__objc_methname: 0xa99

   __AUTH_CONST.__const: 0x2c0
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__objc_const: 0xd90
-  __AUTH.__objc_data: 0x78
+  __AUTH.__objc_data: 0x28
   __DATA.__objc_ivar: 0xcc
   __DATA.__data: 0x60
   __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_data: 0x1b8
+  __DATA_DIRTY.__objc_data: 0x208
   __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libFDR.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 46490A40-29BE-3D6E-8673-187562D5BE06
-  Functions: 463
-  Symbols:   1444
-  CStrings:  536
+  UUID: 0295B8A8-C46D-354D-A564-79D239F10CEE
+  Functions: 465
+  Symbols:   1450
+  CStrings:  538
 
Symbols:
+ -[SocketRemoteXpcProxy activate].cold.1
+ -[SocketRemoteXpcProxy activate].cold.2
CStrings:
+ "F_SETNOSIGPIPE failed: %{darwin.errno}d"
+ "duping server socket failed: %{darwin.errno}d"

```
