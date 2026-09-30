## AppConduit

> `/System/Library/PrivateFrameworks/AppConduit.framework/AppConduit`

```diff

   __TEXT.__cstring: 0x60cc
   __TEXT.__gcc_except_tab: 0x4e4
   __TEXT.__oslogstring: 0x7d
-  __TEXT.__unwind_info: 0x7c0
+  __TEXT.__unwind_info: 0x7c8
   __TEXT.__objc_classname: 0x147
   __TEXT.__objc_methname: 0x50f4
   __TEXT.__objc_methtype: 0xb0b

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1EBE2507-7D69-3680-8F90-03E829C19A90
+  UUID: 4D90218B-9FF1-34BD-8D3D-03DE46E67C38
   Functions: 564
   Symbols:   2105
   CStrings:  1615
Functions:
~ _ACXBooleanValue -> -[ACXDeviceConnection internalQueue] : 88 -> 8
~ __CreateAndLogErrorV -> -[ACXDeviceConnection observers] : 512 -> 8
~ __CreateAndLogError -> _ACXBooleanValue : 64 -> 88
~ -[ACXDeviceConnection _onQueue_beginMonitoringNanoRegistryDeviceState] -> -[ACXDeviceConnection xpcConnection] : 260 -> 8
~ -[ACXDeviceConnection observers] -> __CreateAndLogError : 8 -> 64
~ -[ACXDeviceConnection internalQueue] -> __CreateAndLogErrorV : 8 -> 512
~ -[ACXDeviceConnection monitoringForDeviceChanges] -> -[ACXDeviceConnection _onQueue_beginMonitoringNanoRegistryDeviceState] : 8 -> 260

```
