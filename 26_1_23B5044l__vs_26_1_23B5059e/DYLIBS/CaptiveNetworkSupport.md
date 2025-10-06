## CaptiveNetworkSupport

> `/System/Library/SystemConfiguration/CaptiveNetworkSupport.bundle/CaptiveNetworkSupport`

```diff

-513.0.0.0.0
-  __TEXT.__text: 0x30834
+514.0.0.0.1
+  __TEXT.__text: 0x308c0
   __TEXT.__auth_stubs: 0x15f0
   __TEXT.__objc_methlist: 0x45c
   __TEXT.__const: 0x200
   __TEXT.__gcc_except_tab: 0x218
-  __TEXT.__oslogstring: 0x579d
-  __TEXT.__cstring: 0x2069
+  __TEXT.__oslogstring: 0x57d2
+  __TEXT.__cstring: 0x2096
   __TEXT.__unwind_info: 0x900
   __TEXT.__objc_classname: 0x8e
   __TEXT.__objc_methname: 0xc8c

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B11EEA1F-78A1-3BAC-AFCD-20D281DAC344
+  UUID: 5A974952-CAF3-3E29-BC41-F3D0CCBD0306
   Functions: 758
   Symbols:   2344
-  CStrings:  1590
+  CStrings:  1591
 
Functions:
~ _CaptiveBuiltinPluginProcessCommand : 3936 -> 4076
~ _CNInfoEvaluating : 3408 -> 3376
~ _CNInfoNetworkActive : 1320 -> 1352
CStrings:
+ "%@ quick probe %s required"
+ "%@: SSID '%@' reporting quick probe %s"
+ "CaptiveNetworkSupport-514.0.0.0.1"
+ "MAC randomization requires a quick probe"
+ "all the plugins/providers responded to Evaluate command"
+ "failure"
+ "received evaluation response from [%@]"
- "%@: SSID '%@' reporting quick probe failure"
- "%@: SSID '%@' reporting quick probe success"
- "CaptiveNetworkSupport-513"
- "quick probe %s used"
- "was"
- "was not"

```
