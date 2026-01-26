## mDNSResponder

> `/usr/sbin/mDNSResponder`

```diff

-2881.80.3.0.0
-  __TEXT.__text: 0x106af8
+2881.80.4.0.1
+  __TEXT.__text: 0x106c14
   __TEXT.__auth_stubs: 0x2f00
   __TEXT.__objc_stubs: 0x1d00
   __TEXT.__objc_methlist: 0x664
   __TEXT.__const: 0x1180
-  __TEXT.__cstring: 0x17584
+  __TEXT.__cstring: 0x17588
   __TEXT.__gcc_except_tab: 0x334
-  __TEXT.__oslogstring: 0x1eee6
+  __TEXT.__oslogstring: 0x1ef61
   __TEXT.__objc_classname: 0x649
   __TEXT.__objc_methname: 0x1b39
   __TEXT.__objc_methtype: 0x62a

   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: F954F9D3-76FB-3CCC-8AA1-736656BBAC7B
+  UUID: D1B03DF7-AF68-3699-ADFC-7006C123D28F
   Functions: 1838
   Symbols:   4577
-  CStrings:  4853
+  CStrings:  4854
 
Functions:
~ _request_callback : 43640 -> 43924
CStrings:
+ "[R%u] Attempting to start non-lightweight operation on non-shared connection -- operation: %u, client pid: %d (%{public}s)"
+ "mDNSResponder-2881.80.4.0.1"
- "mDNSResponder-2881.80.3"

```
