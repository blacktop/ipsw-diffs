## UARPKit

> `/System/Library/PrivateFrameworks/UARPKit.framework/UARPKit`

```diff

-1345.100.155.0.0
-  __TEXT.__text: 0x1de84
-  __TEXT.__auth_stubs: 0x390
-  __TEXT.__objc_methlist: 0x1200
+1345.100.162.0.0
+  __TEXT.__text: 0x1e234
+  __TEXT.__auth_stubs: 0x3a0
+  __TEXT.__objc_methlist: 0x1210
   __TEXT.__const: 0x90
-  __TEXT.__cstring: 0x20d4
-  __TEXT.__gcc_except_tab: 0x1324
-  __TEXT.__oslogstring: 0x7cf
+  __TEXT.__cstring: 0x2106
+  __TEXT.__gcc_except_tab: 0x132c
+  __TEXT.__oslogstring: 0x88e
   __TEXT.__unwind_info: 0x608
   __TEXT.__objc_classname: 0x1a8
-  __TEXT.__objc_methname: 0x4263
+  __TEXT.__objc_methname: 0x42d0
   __TEXT.__objc_methtype: 0x9b2
-  __TEXT.__objc_stubs: 0x1da0
+  __TEXT.__objc_stubs: 0x1e40
   __DATA_CONST.__got: 0xc8
   __DATA_CONST.__const: 0x368
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xcb0
+  __DATA_CONST.__objc_selrefs: 0xcd8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x1d8
+  __AUTH_CONST.__auth_got: 0x1e0
   __AUTH_CONST.__cfstring: 0x320
   __AUTH_CONST.__objc_const: 0x14e8
   __AUTH.__objc_data: 0x2d0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F83848D0-63CB-3D41-8054-3CE4091328BB
-  Functions: 502
-  Symbols:   1576
-  CStrings:  830
+  UUID: 4AADF49C-5F2B-3460-8FDB-D50BAC3471E4
+  Functions: 505
+  Symbols:   1580
+  CStrings:  839
 
Symbols:
+ -[UARPDevice(TapToRadar) tapToRadarClearBaseURL:]
+ -[UARPDevice(TapToRadar) tapToRadarClearBaseURL:].cold.1
+ -[UARPDevice(TapToRadar) tapToRadarStart:error:].cold.2
+ _objc_msgSend$enumeratorAtPath:
+ _objc_msgSend$nextObject
+ _objc_msgSend$removeItemAtPath:error:
+ _objc_msgSend$stringByAppendingPathComponent:
+ _objc_msgSend$tapToRadarClearBaseURL:
+ _objc_retain_x27
- _OUTLINED_FUNCTION_14
Functions:
~ -[UARPDevice(TapToRadar) tapToRadarStart:error:] : 588 -> 644
+ -[UARPDevice(TapToRadar) tapToRadarClearBaseURL:]
~ -[UARPDevice queryActiveFirmwareVersion].cold.1 : 96 -> 112
~ -[UARPDevice queryStagedFirmwareVersion].cold.1 : 96 -> 112
~ -[UARPDevice(TapToRadar) tapToRadarStart:error:].cold.1 : 96 -> 88
+ -[UARPDevice(TapToRadar) tapToRadarStart:error:].cold.2
CStrings:
+ "%s: Failed to clear contents of base URL: %@, cannot start TapToRadar"
+ "%s: Failed to remove item in TapToRadar folder: %@ with error: %@"
+ "%s: Successfully removed item in TapToRadar folder: %@"
+ "-[UARPDevice(TapToRadar) tapToRadarClearBaseURL:]"
+ "enumeratorAtPath:"
+ "nextObject"
+ "removeItemAtPath:error:"
+ "stringByAppendingPathComponent:"
+ "tapToRadarClearBaseURL:"

```
