## mDNSResponder

> `/usr/sbin/mDNSResponder`

```diff

-2881.120.11.0.0
-  __TEXT.__text: 0x107760
-  __TEXT.__auth_stubs: 0x2f00
+2881.160.2.0.0
+  __TEXT.__text: 0x1076e4
+  __TEXT.__auth_stubs: 0x2ef0
   __TEXT.__objc_stubs: 0x2020
   __TEXT.__objc_methlist: 0x694
   __TEXT.__const: 0x1170
-  __TEXT.__cstring: 0x179bd
+  __TEXT.__cstring: 0x179bc
   __TEXT.__gcc_except_tab: 0x338
   __TEXT.__oslogstring: 0x1f627
   __TEXT.__objc_classname: 0x649
   __TEXT.__objc_methname: 0x1db6
   __TEXT.__objc_methtype: 0x64d
-  __TEXT.__unwind_info: 0x16a0
+  __TEXT.__unwind_info: 0x16a8
   __TEXT.__eh_frame: 0x74
-  __DATA_CONST.__auth_got: 0x1790
+  __DATA_CONST.__auth_got: 0x1788
   __DATA_CONST.__got: 0x3e8
   __DATA_CONST.__auth_ptr: 0x78
   __DATA_CONST.__const: 0x6440

   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: E2392592-ADE6-339F-B9B3-0CD9B6E773F8
+  UUID: 3D15DFE1-71B5-3B89-89E5-14F96E583964
   Functions: 1845
-  Symbols:   4611
+  Symbols:   4610
   CStrings:  4914
 
Symbols:
- _strtol
Functions:
~ _mDNSCoreReceive : 4168 -> 4112
~ _handleLNTDeviceDescriptionResponse : 1204 -> 1108
~ _handleLNTGetExternalAddressResponse : 504 -> 488
~ _ParseHttpUrl : 496 -> 540
CStrings:
+ "mDNSResponder-2881.160.2"
- "mDNSResponder-2881.120.11"

```
