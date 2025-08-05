## CaptiveNetworkSupport

> `/System/Library/SystemConfiguration/CaptiveNetworkSupport.bundle/CaptiveNetworkSupport`

```diff

-509.0.0.0.0
-  __TEXT.__text: 0x307b8
+511.0.0.0.0
+  __TEXT.__text: 0x308e0
   __TEXT.__auth_stubs: 0x15f0
   __TEXT.__objc_methlist: 0x45c
   __TEXT.__const: 0x200
   __TEXT.__gcc_except_tab: 0x218
-  __TEXT.__oslogstring: 0x5765
-  __TEXT.__cstring: 0x2069
+  __TEXT.__oslogstring: 0x57b8
+  __TEXT.__cstring: 0x2092
   __TEXT.__unwind_info: 0x900
   __TEXT.__objc_classname: 0x8e
   __TEXT.__objc_methname: 0xc8c

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 94E355B9-5475-30D6-BD23-34F37F4BC562
+  UUID: 1418372E-F96D-3DAE-AC51-377673BDAA98
   Functions: 758
   Symbols:   2344
-  CStrings:  1589
+  CStrings:  1592
 
Functions:
~ _CaptiveBuiltinPluginProcessCommand : 3936 -> 4076
~ _CNInfoMaintaining : 1332 -> 1456
~ _CNInfoNetworkActive : 1320 -> 1352
CStrings:
+ "%@ quick probe %s required"
+ "CaptiveNetworkSupport-511"
+ "MAC randomization requires a quick probe"
+ "NetIFWiFiNetworkCopyCaptivePortalAPIURL() returned NULL"
- "CaptiveNetworkSupport-509"

```
