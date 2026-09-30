## lockdownd

> `/usr/libexec/lockdownd`

```diff

-1365.100.8.0.0
-  __TEXT.__text: 0xaacac
+1365.160.1.0.0
+  __TEXT.__text: 0xaac74
   __TEXT.__auth_stubs: 0x1db0
   __TEXT.__objc_stubs: 0x15c0
   __TEXT.__objc_methlist: 0x180
-  __TEXT.__cstring: 0x3c0d3
+  __TEXT.__cstring: 0x3c127
   __TEXT.__const: 0x10fc0
   __TEXT.__gcc_except_tab: 0xaf0
   __TEXT.__objc_methname: 0xf22

   __TEXT.__objc_classname: 0x4c
   __TEXT.__objc_methtype: 0x15a
   __TEXT.__services: 0x2d43
-  __TEXT.__unwind_info: 0xbf8
+  __TEXT.__unwind_info: 0xc00
   __TEXT.__eh_frame: 0x80
   __DATA_CONST.__auth_got: 0xee8
   __DATA_CONST.__got: 0x430
   __DATA_CONST.__auth_ptr: 0x28
   __DATA_CONST.__const: 0x70b8
-  __DATA_CONST.__cfstring: 0xdc60
+  __DATA_CONST.__cfstring: 0xdca0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libramrod.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 716C03BE-0923-3001-98D7-B20F3A84DD67
+  UUID: AE5C9217-BF4C-32EE-91C0-B6D54E27A990
   Functions: 918
   Symbols:   637
-  CStrings:  7488
+  CStrings:  7492
 
Functions:
~ sub_100009940 : 636 -> 712
~ sub_100025e7c -> sub_100025ec8 : 1516 -> 1524
~ sub_100026a80 -> sub_100026ad4 : 164 -> 24
CStrings:
+ "%02x:%02x:%02x:%02x:%02x:%02x"
+ "WiFi link down; keeping Bonjour advertisement active."

```
