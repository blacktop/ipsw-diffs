## lockdownd

> `/usr/libexec/lockdownd`

```diff

-1350.0.1.0.0
-  __TEXT.__text: 0x97dcc
+1350.2.1.0.0
+  __TEXT.__text: 0x97ca8
   __TEXT.__auth_stubs: 0x1d40
   __TEXT.__objc_stubs: 0x1360
   __TEXT.__objc_methlist: 0xe8
-  __TEXT.__cstring: 0x39f6d
+  __TEXT.__cstring: 0x39f0a
   __TEXT.__const: 0x10e90
   __TEXT.__oslogstring: 0x1e6
-  __TEXT.__gcc_except_tab: 0x9c8
+  __TEXT.__gcc_except_tab: 0x9b4
   __TEXT.__objc_classname: 0x27
   __TEXT.__objc_methname: 0xd61
   __TEXT.__objc_methtype: 0x120
   __TEXT.__services: 0x2d8e
-  __TEXT.__unwind_info: 0xb78
+  __TEXT.__unwind_info: 0xb68
   __TEXT.__eh_frame: 0x80
   __DATA_CONST.__auth_got: 0xeb0
   __DATA_CONST.__got: 0x3e8
   __DATA_CONST.__auth_ptr: 0x28
   __DATA_CONST.__const: 0x7da8
-  __DATA_CONST.__cfstring: 0xda00
+  __DATA_CONST.__cfstring: 0xd9c0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libramrod.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 5B441120-98F4-3E04-BC1B-3BFCB5641DA5
-  Functions: 863
+  UUID: 57074204-8DE6-3A68-93C9-BF8A1B6CA5CB
+  Functions: 861
   Symbols:   616
-  CStrings:  7247
+  CStrings:  7243
 
CStrings:
+ "non kernel peer, pid %d!\n"
- "Peer is unsafe (generic failure)."
- "Peer is unsafe (non kernel peer, pid %d)"
- "Peer is unsafe (usbmux is not connected to host)."

```
