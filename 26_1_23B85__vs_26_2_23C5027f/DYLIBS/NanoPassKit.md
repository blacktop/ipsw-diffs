## NanoPassKit

> `/System/Library/PrivateFrameworks/NanoPassKit.framework/NanoPassKit`

```diff

-1288.0.0.0.0
-  __TEXT.__text: 0x25831c
+1289.1.2.0.0
+  __TEXT.__text: 0x258314
   __TEXT.__auth_stubs: 0x1e80
   __TEXT.__objc_methlist: 0x25c28
   __TEXT.__cstring: 0x18108

   __TEXT.__unwind_info: 0x8fa0
   __TEXT.__eh_frame: 0x378
   __TEXT.__objc_classname: 0x6b98
-  __TEXT.__objc_methname: 0x3fe1e
+  __TEXT.__objc_methname: 0x3fe26
   __TEXT.__objc_methtype: 0xa1b6
   __TEXT.__objc_stubs: 0x22160
   __DATA_CONST.__got: 0x1e78

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5528C5E6-B902-33FA-A463-D98F40AA9D31
+  UUID: 3D3C3925-9BE9-3567-AC88-42EE6BBAA9F5
   Functions: 14524
   Symbols:   42582
   CStrings:  17105
Symbols:
+ -[NPKIDVRemoteDevicesManager _initRemoteDeviceServiceIfNeeded]
+ _objc_msgSend$_initRemoteDeviceServiceIfNeeded
- -[NPKIDVRemoteDevicesManager _initRemoteDeviceService]
- _objc_msgSend$_initRemoteDeviceService
Functions:
~ -[NPKIDVRemoteDevicesManager _teardownConnections] : 72 -> 60
~ -[NPKIDVRemoteDevicesManager _initRemoteDeviceService] -> -[NPKIDVRemoteDevicesManager _initRemoteDeviceServiceIfNeeded] : 92 -> 104
~ sub_25b5583b4 -> sub_25c76e3b4 : 1204 -> 1196
CStrings:
+ "_initRemoteDeviceServiceIfNeeded"
- "_initRemoteDeviceService"

```
