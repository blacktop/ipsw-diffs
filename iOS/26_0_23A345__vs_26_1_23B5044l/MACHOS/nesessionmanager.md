## nesessionmanager

> `/usr/libexec/nesessionmanager`

```diff

-2205.0.0.0.0
-  __TEXT.__text: 0xb2584
-  __TEXT.__auth_stubs: 0x1d20
+2205.40.9.0.0
+  __TEXT.__text: 0xb26dc
+  __TEXT.__auth_stubs: 0x1d40
   __TEXT.__objc_stubs: 0x7fe0
   __TEXT.__objc_methlist: 0x3d94
   __TEXT.__const: 0x188
   __TEXT.__gcc_except_tab: 0x2368
   __TEXT.__objc_methname: 0x9168
-  __TEXT.__oslogstring: 0xf38a
+  __TEXT.__oslogstring: 0xf3c8
   __TEXT.__cstring: 0x535e
   __TEXT.__objc_classname: 0xbac
   __TEXT.__objc_methtype: 0x210d
   __TEXT.__unwind_info: 0x1660
-  __DATA_CONST.__auth_got: 0xea0
+  __DATA_CONST.__auth_got: 0xeb0
   __DATA_CONST.__got: 0x770
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x1d80

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 11657D99-C93B-325E-8135-472A304107B7
+  UUID: C5979C00-6564-314D-8D72-FC2867819D5F
   Functions: 1883
-  Symbols:   689
-  CStrings:  4320
+  Symbols:   691
+  CStrings:  4321
 
Symbols:
+ _nw_interface_copy_delegate_interface
+ _nw_path_monitor_prohibit_interface_type
Functions:
~ sub_100011598 : 1808 -> 1816
~ sub_100015400 -> sub_100015408 : 232 -> 248
~ sub_100015780 -> sub_100015798 : 816 -> 1136
CStrings:
+ "%@ [wifiMatch: %s] [cellMatch: %s] [ethMatch: %s]"
+ "%@ network path over effective interface [%s] is satisfied"
- "[wifiMatch: %s] [cellMatch: %s] [ethMatch: %s]"

```
