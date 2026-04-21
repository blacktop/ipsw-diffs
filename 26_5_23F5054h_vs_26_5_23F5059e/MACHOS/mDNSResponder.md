## mDNSResponder

> `/usr/sbin/mDNSResponder`

```diff

-2881.120.6.0.0
-  __TEXT.__text: 0x1074a4
-  __TEXT.__auth_stubs: 0x2ef0
+2881.120.8.0.1
+  __TEXT.__text: 0x1074d4
+  __TEXT.__auth_stubs: 0x2f00
   __TEXT.__objc_stubs: 0x2020
   __TEXT.__objc_methlist: 0x694
-  __TEXT.__const: 0x1170
-  __TEXT.__cstring: 0x178fe
+  __TEXT.__const: 0x1178
+  __TEXT.__cstring: 0x17902
   __TEXT.__gcc_except_tab: 0x338
   __TEXT.__oslogstring: 0x1f627
   __TEXT.__objc_classname: 0x649

   __TEXT.__objc_methtype: 0x64d
   __TEXT.__unwind_info: 0x16a0
   __TEXT.__eh_frame: 0x74
-  __DATA_CONST.__auth_got: 0x1788
+  __DATA_CONST.__auth_got: 0x1790
   __DATA_CONST.__got: 0x3e8
   __DATA_CONST.__auth_ptr: 0x78
   __DATA_CONST.__const: 0x6440

   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 5650D4DB-6287-37FF-8BA1-B0F1A03AC454
+  UUID: 4D932B7A-30BD-3B8F-8BB3-F1C78EEA43A1
   Functions: 1845
-  Symbols:   4610
+  Symbols:   4611
   CStrings:  4911
 
Symbols:
+ _nw_resolver_config_get_no_cname_recursion
Functions:
~ ___mDNSPlatformGetDNSRoutePolicy_block_invoke : 128 -> 176
CStrings:
+ "mDNSResponder-2881.120.8.0.1"
- "mDNSResponder-2881.120.6"

```
