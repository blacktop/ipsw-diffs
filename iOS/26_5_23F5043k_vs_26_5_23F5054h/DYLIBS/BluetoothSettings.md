## BluetoothSettings

> `/System/Library/PreferenceBundles/BluetoothSettings.bundle/BluetoothSettings`

```diff

-455.2.1.1.0
-  __TEXT.__text: 0x233b8
+455.4.0.0.0
+  __TEXT.__text: 0x2363c
   __TEXT.__auth_stubs: 0xc20
-  __TEXT.__objc_methlist: 0x18bc
-  __TEXT.__cstring: 0x1771
+  __TEXT.__objc_methlist: 0x18d4
+  __TEXT.__cstring: 0x1831
   __TEXT.__const: 0x498
   __TEXT.__gcc_except_tab: 0x320
   __TEXT.__oslogstring: 0x21c2

   __TEXT.__unwind_info: 0x750
   __TEXT.__eh_frame: 0x258
   __TEXT.__objc_classname: 0x237
-  __TEXT.__objc_methname: 0x4f05
+  __TEXT.__objc_methname: 0x4fa5
   __TEXT.__objc_methtype: 0x1090
-  __TEXT.__objc_stubs: 0x4420
+  __TEXT.__objc_stubs: 0x4460
   __DATA_CONST.__got: 0x5e8
   __DATA_CONST.__const: 0x578
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x16e0
+  __DATA_CONST.__objc_selrefs: 0x16f0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__auth_got: 0x620
   __AUTH_CONST.__const: 0x200
-  __AUTH_CONST.__cfstring: 0x1ac0
-  __AUTH_CONST.__objc_const: 0x2610
+  __AUTH_CONST.__cfstring: 0x1b40
+  __AUTH_CONST.__objc_const: 0x2650
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x478
   __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x198
+  __DATA.__objc_ivar: 0x1a0
   __DATA.__data: 0x530
   __DATA.__common: 0x30
   __DATA.__bss: 0x130

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 88B9BF63-5766-3A34-BF1D-0153EA0FCBAC
-  Functions: 593
-  Symbols:   2275
-  CStrings:  1698
+  UUID: DC85F40C-D72B-3E30-9956-762BBDDA580A
+  Functions: 595
+  Symbols:   2283
+  CStrings:  1711
 
Symbols:
+ -[BTSDevicesController _tryPushPendingDeviceWithID:subDetailKey:]
+ -[BTSDevicesController forcePushDetailViewForDevice:pendingSubDetailKey:]
+ GCC_except_table196
+ GCC_except_table201
+ GCC_except_table206
+ _OBJC_IVAR_$_BTSDevicesController._pendingLiveActivitiesForwardingDeviceID
+ _OBJC_IVAR_$_BTSDevicesController._pendingNotificationForwardingDeviceID
+ ___44-[BTSDevicesController _updateHealthDevices]_block_invoke.648
+ ___44-[BTSDevicesController _updateHealthDevices]_block_invoke.650
+ ___50-[BTSDevicesController startOutgoingCarPlaySetup:]_block_invoke.839
+ ___50-[BTSDevicesController startOutgoingCarPlaySetup:]_block_invoke_2.840
+ ___52-[BTSDevicesController migrateHKPairedHealthDevices]_block_invoke.853
+ ___52-[BTSDevicesController migrateHKPairedHealthDevices]_block_invoke.853.cold.1
+ ___52-[BTSDevicesController migrateHKPairedHealthDevices]_block_invoke.857
+ ___52-[BTSDevicesController migrateHKPairedHealthDevices]_block_invoke.857.cold.1
+ ___52-[BTSDevicesController migrateHKPairedHealthDevices]_block_invoke.858
+ ___58-[BTSDevicesController tableView:didSelectRowAtIndexPath:]_block_invoke.744
+ ___block_literal_global.671
+ ___block_literal_global.746
+ ___block_literal_global.799
+ ___block_literal_global.813
+ _objc_msgSend$_tryPushPendingDeviceWithID:subDetailKey:
+ _objc_msgSend$forcePushDetailViewForDevice:pendingSubDetailKey:
- GCC_except_table194
- GCC_except_table199
- GCC_except_table204
- ___44-[BTSDevicesController _updateHealthDevices]_block_invoke.636
- ___44-[BTSDevicesController _updateHealthDevices]_block_invoke.638
- ___50-[BTSDevicesController startOutgoingCarPlaySetup:]_block_invoke.827
- ___50-[BTSDevicesController startOutgoingCarPlaySetup:]_block_invoke_2.828
- ___52-[BTSDevicesController migrateHKPairedHealthDevices]_block_invoke.841
- ___52-[BTSDevicesController migrateHKPairedHealthDevices]_block_invoke.841.cold.1
- ___52-[BTSDevicesController migrateHKPairedHealthDevices]_block_invoke.845
- ___52-[BTSDevicesController migrateHKPairedHealthDevices]_block_invoke.845.cold.1
- ___52-[BTSDevicesController migrateHKPairedHealthDevices]_block_invoke.846
- ___58-[BTSDevicesController tableView:didSelectRowAtIndexPath:]_block_invoke.732
- ___block_literal_global.659
- ___block_literal_global.734
- ___block_literal_global.787
- ___block_literal_global.801
CStrings:
+ "-[BTSDevicesController forcePushDetailViewForDevice:pendingSubDetailKey:]"
+ "AccessoryLiveActivitiesForwardingSettings"
+ "AccessoryNotificationForwardingSettings"
+ "B32@0:8@16@24"
+ "_pendingLiveActivitiesForwardingDeviceID"
+ "_pendingNotificationForwardingDeviceID"
+ "_tryPushPendingDeviceWithID:subDetailKey:"
+ "bts-push-live-activities-forwarding-settings"
+ "bts-push-notification-forwarding-settings"
+ "forcePushDetailViewForDevice:pendingSubDetailKey:"
- "-[BTSDevicesController forcePushDetailViewForDevice:]"

```
