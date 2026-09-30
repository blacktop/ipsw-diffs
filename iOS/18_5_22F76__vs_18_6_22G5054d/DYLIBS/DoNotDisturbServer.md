## DoNotDisturbServer

> `/System/Library/PrivateFrameworks/DoNotDisturbServer.framework/DoNotDisturbServer`

```diff

-433.6.1.0.0
-  __TEXT.__text: 0xc2d18
+433.7.1.0.0
+  __TEXT.__text: 0xc2f64
   __TEXT.__auth_stubs: 0x1340
-  __TEXT.__objc_methlist: 0xa908
-  __TEXT.__const: 0x458
-  __TEXT.__cstring: 0x8894
-  __TEXT.__oslogstring: 0x11270
+  __TEXT.__objc_methlist: 0xa920
+  __TEXT.__const: 0x520
+  __TEXT.__cstring: 0x88d4
+  __TEXT.__oslogstring: 0x11300
   __TEXT.__gcc_except_tab: 0xf74
   __TEXT.__dlopen_cstrs: 0x59
   __TEXT.__constg_swiftt: 0x14c

   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_ret: 0x2c
-  __TEXT.__unwind_info: 0x2800
+  __TEXT.__unwind_info: 0x2818
   __TEXT.__eh_frame: 0x540
   __TEXT.__objc_classname: 0x28c2
-  __TEXT.__objc_methname: 0x19818
+  __TEXT.__objc_methname: 0x19837
   __TEXT.__objc_methtype: 0x7570
-  __TEXT.__objc_stubs: 0x10ae0
+  __TEXT.__objc_stubs: 0x10b20
   __DATA_CONST.__got: 0xe58
   __DATA_CONST.__const: 0x25d8
   __DATA_CONST.__objc_classlist: 0x5f8
   __DATA_CONST.__objc_catlist: 0x148
   __DATA_CONST.__objc_protolist: 0x3d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4c58
+  __DATA_CONST.__objc_selrefs: 0x4c68
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x3e0
   __DATA_CONST.__objc_arraydata: 0x330
   __AUTH_CONST.__auth_got: 0x9b0
   __AUTH_CONST.__const: 0x1030
-  __AUTH_CONST.__cfstring: 0x7940
+  __AUTH_CONST.__cfstring: 0x7980
   __AUTH_CONST.__objc_const: 0x25f38
   __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_dictobj: 0x488
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH.__objc_data: 0x808
   __DATA.__objc_ivar: 0xa38
-  __DATA.__data: 0x3330
+  __DATA.__data: 0x3260
   __DATA.__bss: 0x1c0
   __DATA_DIRTY.__objc_data: 0x3568
   __DATA_DIRTY.__data: 0xa8

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 38377036-0F65-3F1A-B74C-C5AE20E839DD
-  Functions: 3786
-  Symbols:   14317
-  CStrings:  7604
+  UUID: 3D0A9CAD-5650-3C67-85C3-1C5F9E5AFBA3
+  Functions: 3792
+  Symbols:   14331
+  CStrings:  7612
 
Symbols:
+ -[DNDSMeDeviceService devicesChanged]
+ -[DNDSMeDeviceService meDeviceChanged]
+ ___37-[DNDSMeDeviceService devicesChanged]_block_invoke
+ ___38-[DNDSMeDeviceService meDeviceChanged]_block_invoke
+ ___48-[DNDSMeDeviceService _loadDataFromBackingStore]_block_invoke.26
+ ___53-[DNDSMeDeviceService startMonitoringMeDeviceChanges]_block_invoke.14
+ ___53-[DNDSMeDeviceService startMonitoringMeDeviceChanges]_block_invoke.15
+ _fmlDevicesChangedNotificationCallback
+ _fmlMeDeviceChangedNotificationCallback
+ _objc_msgSend$devicesChanged
+ _objc_msgSend$meDeviceChanged
- ___48-[DNDSMeDeviceService _loadDataFromBackingStore]_block_invoke.20
- ___53-[DNDSMeDeviceService startMonitoringMeDeviceChanges]_block_invoke.8
- ___53-[DNDSMeDeviceService startMonitoringMeDeviceChanges]_block_invoke.9
CStrings:
+ "FMLDevicesChangedNotification"
+ "FMLMeDeviceChangedNotification"
+ "devicesChanged"
+ "meDeviceChanged"
+ "received notification that 'Me Device' devices changed fetching Me Device"
+ "received notification that 'Me Device' status changed fetching Me Device"

```
