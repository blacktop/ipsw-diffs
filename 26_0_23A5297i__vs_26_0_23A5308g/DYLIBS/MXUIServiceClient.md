## MXUIServiceClient

> `/System/Library/PrivateFrameworks/MXUIServiceClient.framework/MXUIServiceClient`

```diff

-270.70.1.0.0
-  __TEXT.__text: 0x1b50
+270.74.1.11.1
+  __TEXT.__text: 0x1d28
   __TEXT.__auth_stubs: 0x170
-  __TEXT.__objc_methlist: 0x264
-  __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x339
-  __TEXT.__oslogstring: 0xc7
-  __TEXT.__unwind_info: 0xd0
+  __TEXT.__objc_methlist: 0x294
+  __TEXT.__const: 0x58
+  __TEXT.__cstring: 0x390
+  __TEXT.__oslogstring: 0x149
+  __TEXT.__unwind_info: 0xd8
   __TEXT.__objc_classname: 0xba
-  __TEXT.__objc_methname: 0x636
-  __TEXT.__objc_methtype: 0x2ed
-  __TEXT.__objc_stubs: 0x500
+  __TEXT.__objc_methname: 0x688
+  __TEXT.__objc_methtype: 0x31e
+  __TEXT.__objc_stubs: 0x540
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__const: 0x148
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x238
+  __DATA_CONST.__objc_selrefs: 0x248
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x18
   __AUTH_CONST.__auth_got: 0xc0
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x1a0
-  __AUTH_CONST.__objc_const: 0x840
+  __AUTH_CONST.__objc_const: 0x868
   __DATA.__objc_ivar: 0x20
   __DATA.__data: 0x180
   __DATA.__common: 0x40

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 257AECFE-E6F8-371D-828E-1128CA289806
-  Functions: 47
-  Symbols:   265
-  CStrings:  170
+  UUID: 3E31D4AD-8F7E-3F22-8F57-4A9E0CD88685
+  Functions: 49
+  Symbols:   271
+  CStrings:  176
 
Symbols:
+ -[MXUIService_Client showInputDeviceReplacementPillForConnectedDevice:replacedDevice:]
+ -[MXUIService_ServerDelegate showInputDeviceReplacementPillForConnectedDevice:replacedDevice:]
+ ___51-[MXUIService_Client recreateConnectionIfNecessary]_block_invoke.81
+ ___51-[MXUIService_Client recreateConnectionIfNecessary]_block_invoke.82
+ ___block_literal_global.60
+ ___block_literal_global.80
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$showInputDeviceReplacementPillForConnectedDevice:replacedDevice:
- ___51-[MXUIService_Client recreateConnectionIfNecessary]_block_invoke.79
- ___51-[MXUIService_Client recreateConnectionIfNecessary]_block_invoke.80
- ___block_literal_global.58
- ___block_literal_global.78
Functions:
+ -[MXUIService_ServerDelegate showInputDeviceReplacementPillForConnectedDevice:replacedDevice:]
+ -[MXUIService_Client showInputDeviceReplacementPillForConnectedDevice:replacedDevice:]
CStrings:
+ "-MXUIServiceClient- %s: Showing input device replacement pill (connectedDeviceName='%{public}@', replacedDeviceName='%{public}@')"
+ "-[MXUIService_Client showInputDeviceReplacementPillForConnectedDevice:replacedDevice:]"
+ "Vv32@0:8@\"NSString\"16@\"NSString\"24"
+ "isEqualToString:"
+ "showInputDeviceReplacementPillForConnectedDevice:replacedDevice:"
+ "v32@0:8@16@24"

```
