## CaptiveNetworkSupport

> `/System/Library/SystemConfiguration/CaptiveNetworkSupport.bundle/Contents/MacOS/CaptiveNetworkSupport`

```diff

-514.80.2.0.0
-  __TEXT.__text: 0x263bc
+514.80.3.0.0
+  __TEXT.__text: 0x263cc
   __TEXT.__auth_stubs: 0x10a0
   __TEXT.__objc_stubs: 0x60
   __TEXT.__const: 0x1c0
-  __TEXT.__oslogstring: 0x4310
+  __TEXT.__oslogstring: 0x4308
   __TEXT.__cstring: 0x177f
   __TEXT.__objc_methname: 0x30
-  __TEXT.__unwind_info: 0x708
+  __TEXT.__unwind_info: 0x710
   __DATA_CONST.__auth_got: 0x858
   __DATA_CONST.__got: 0x1f8
   __DATA_CONST.__auth_ptr: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8FDE9692-6BF2-3CA8-BA54-A08E64EC9936
-  Functions: 600
-  Symbols:   1136
+  UUID: 8C36A23D-101C-3DEE-842C-E7255462B35A
+  Functions: 601
+  Symbols:   1138
   CStrings:  1066
 
Symbols:
+ _CNPluginStateForAppOwnedNetwork
+ _NetIFIsAppOwnedNetwork
Functions:
~ _CNScanListFilterHandleScanResults : 1896 -> 1900
~ _CNPluginHandlerNetworkInformationChanged : 2604 -> 2588
+ _NetIFIsAppOwnedNetwork
CStrings:
+ "CaptiveNetworkSupport-514.80.3"
+ "[%@] is pre-evaluated"
- "CaptiveNetworkSupport-514.80.2"
- "[%@] is pre-evaluated by [%@]"

```
