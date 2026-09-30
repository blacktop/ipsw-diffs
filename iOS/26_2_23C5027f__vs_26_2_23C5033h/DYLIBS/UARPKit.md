## UARPKit

> `/System/Library/PrivateFrameworks/UARPKit.framework/UARPKit`

```diff

-1338.60.16.0.0
-  __TEXT.__text: 0x1a104
+1338.60.22.0.0
+  __TEXT.__text: 0x1a310
   __TEXT.__auth_stubs: 0x3b0
   __TEXT.__objc_methlist: 0x10d0
   __TEXT.__const: 0x90
   __TEXT.__cstring: 0x1b34
   __TEXT.__gcc_except_tab: 0x12a8
-  __TEXT.__oslogstring: 0x54b
-  __TEXT.__unwind_info: 0x5e0
+  __TEXT.__oslogstring: 0x586
+  __TEXT.__unwind_info: 0x5e8
   __TEXT.__objc_classname: 0x19b
   __TEXT.__objc_methname: 0x3c22
   __TEXT.__objc_methtype: 0x8fd
-  __TEXT.__objc_stubs: 0x1b00
+  __TEXT.__objc_stubs: 0x1b40
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__const: 0x318
   __DATA_CONST.__objc_classlist: 0x48

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 35EC9E89-704D-3772-A3A4-89033E5FDB82
-  Functions: 449
-  Symbols:   1430
-  CStrings:  761
+  UUID: B6D21554-5C4D-371A-8890-15BCDBD7648B
+  Functions: 452
+  Symbols:   1438
+  CStrings:  762
 
Symbols:
+ -[UARPDevice deviceTransportUnavailable].cold.1
+ -[UARPDevice hostEndpointDelegateTransportTeardown:].cold.1
+ _OUTLINED_FUNCTION_8
+ _objc_msgSend$activeFirmwareVersion
+ _objc_msgSend$stagedFirmwareVersion
Functions:
~ -[UARPDevice deviceTransportUnavailable] : 204 -> 240
~ -[UARPDevice hostEndpointDelegateTransportTeardown:] : 216 -> 272
+ _OUTLINED_FUNCTION_8
+ -[UARPDevice deviceTransportUnavailable].cold.1
+ -[UARPDevice hostEndpointDelegateTransportTeardown:].cold.1
CStrings:
+ "%s: Active Firmware Version %@, Staged Firmware Version %@"

```
