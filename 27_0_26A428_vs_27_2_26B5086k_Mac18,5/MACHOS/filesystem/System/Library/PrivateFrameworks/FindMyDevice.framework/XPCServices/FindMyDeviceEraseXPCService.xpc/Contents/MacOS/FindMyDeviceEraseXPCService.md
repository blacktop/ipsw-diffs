## FindMyDeviceEraseXPCService

> `/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceEraseXPCService.xpc/Contents/MacOS/FindMyDeviceEraseXPCService`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_protorefs`

```diff

-482.20.6.14.14
-  __TEXT.__text: 0x38c0
-  __TEXT.__auth_stubs: 0x290
-  __TEXT.__objc_stubs: 0xa60
-  __TEXT.__objc_methlist: 0x31c
-  __TEXT.__cstring: 0x24c4
-  __TEXT.__const: 0x90
-  __TEXT.__oslogstring: 0x742
-  __TEXT.__objc_classname: 0xa4
-  __TEXT.__objc_methname: 0xa4d
-  __TEXT.__objc_methtype: 0x2b3
+482.21.6.16.10
+  __TEXT.__text: 0x262c
+  __TEXT.__auth_stubs: 0x230
+  __TEXT.__objc_stubs: 0x720
+  __TEXT.__objc_methlist: 0x1f4
+  __TEXT.__cstring: 0x21b8
+  __TEXT.__const: 0x88
+  __TEXT.__oslogstring: 0x486
+  __TEXT.__objc_classname: 0x7f
+  __TEXT.__objc_methname: 0x694
+  __TEXT.__objc_methtype: 0x159
   __TEXT.__gcc_except_tab: 0x6c
-  __TEXT.__unwind_info: 0x1c0
-  __DATA_CONST.__const: 0xdf0
-  __DATA_CONST.__cfstring: 0x3080
-  __DATA_CONST.__objc_classlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x20
+  __TEXT.__unwind_info: 0x190
+  __DATA_CONST.__const: 0xdd0
+  __DATA_CONST.__cfstring: 0x2dc0
+  __DATA_CONST.__objc_classlist: 0x18
+  __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__auth_got: 0x158
-  __DATA_CONST.__got: 0x120
-  __DATA.__objc_const: 0x4f0
-  __DATA.__objc_selrefs: 0x398
-  __DATA.__objc_ivar: 0x10
-  __DATA.__objc_data: 0x140
-  __DATA.__data: 0x2b0
+  __DATA_CONST.__auth_got: 0x128
+  __DATA_CONST.__got: 0xe0
+  __DATA.__objc_const: 0x380
+  __DATA.__objc_selrefs: 0x298
+  __DATA.__objc_ivar: 0x4
+  __DATA.__objc_data: 0xf0
+  __DATA.__data: 0x250
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/DiskArbitration.framework/Versions/A/DiskArbitration
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/BiometricKit.framework/Versions/A/BiometricKit
-  - /System/Library/PrivateFrameworks/BridgeOSObliteration.framework/Versions/A/BridgeOSObliteration
   - /System/Library/PrivateFrameworks/DiskManagement.framework/Versions/A/DiskManagement
   - /System/Library/PrivateFrameworks/FMCore.framework/Versions/A/FMCore
   - /System/Library/PrivateFrameworks/FMCoreLite.framework/Versions/A/FMCoreLite

   - /System/Library/PrivateFrameworks/NearField.framework/Versions/A/NearField
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 113
-  Symbols:   111
-  CStrings:  613
+  Functions: 95
+  Symbols:   98
+  CStrings:  536
 
Symbols:
- _BridgeOS_Obliterate
- _DASessionCreate
- _OBJC_CLASS_$_DMEraseDisk
- _OBJC_CLASS_$_DMFilesystem
- _OBJC_CLASS_$_DMManager
- _OBJC_CLASS_$_DMPartitionDisk
- _OBJC_CLASS_$_NSMutableArray
- _dispatch_group_create
- _dispatch_group_enter
- _dispatch_group_leave
- _dispatch_group_wait
- _kCFAllocatorDefault
- _kObliterateDataPartition
CStrings:
- "- [FMDFMMStorageManager eraseInternalDrive]"
- "- [FMDFMMStorageManager obliterateBridgeOS]"
- "- [FMDFMMStorageManager obliterateBridgeOS]??"
- "@\"DMManager\""
- "@\"NSObject<OS_dispatch_group>\""
- "@24@0:8^{__DADisk=}16"
- "All disks have been erased. Can proceed to obliteration."
- "Could not create DMEraseDisk."
- "Could not create DMPartitionDisk."
- "Could not create DiskManager."
- "Could not get all disks."
- "Could not get top level disks."
- "Could not remove partition. Error - %oi"
- "Could not unmount disk"
- "DMAsyncDelegate"
- "Erase Mac. Taking bridgeOS obliterate path"
- "Erasing all disks did not complete in 10 seconds. Proceeding with obliteration."
- "Erasing all disks that are not partitions."
- "Erasing disk : %@"
- "Error in operation type [%i]. Detail - %d"
- "FMDFMMStorageManager"
- "Journaled HFS+"
- "Name - [%@], UUID - [%@], volumeUUID - [%@], description - %@"
- "Removing all partitions"
- "Result from erase - %@"
- "T@\"DMManager\",&,N,V_dmManager"
- "T@\"NSObject<OS_dispatch_group>\",&,N,V_volumeEraseDispatchGroup"
- "T^{__DASession=},N,V_daSession"
- "Trying to remove partition: %@"
- "Trying to unmount: %@"
- "Unmounting all disks"
- "^{__DASession=}"
- "^{__DASession=}16@0:8"
- "_daSession"
- "_dmManager"
- "_volumeEraseDispatchGroup"
- "arrayWithArray:"
- "daSession"
- "daSessionRef"
- "descriptionForDisk:"
- "diskDetails:"
- "diskUUIDForDisk:error:"
- "disks"
- "dmAsyncFinishedForDisk with dict - %@"
- "dmAsyncFinishedForDisk:mainError:detailError:dictionary:"
- "dmAsyncMessageForDisk:string:dictionary:"
- "dmAsyncProgressForDisk:barberPole:percent:"
- "dmAsyncStartedForDisk:"
- "dmInterruptibilityChanged:"
- "dmManager"
- "eraseDisk:synchronous:filesystem:bootable:name:doNewfs:doBooterCleanup:"
- "eraseInternalDriveAndObliterate"
- "filesystemForPersonality:"
- "hasBridgeCoProcessor"
- "initWithManager:"
- "isInternalDisk:error:"
- "isPartitionDisk:error:"
- "isRootVolume:error:"
- "obliterateBridgeOS"
- "removePartition:wipe:options:"
- "setDaSession:"
- "setDefaultDASession:"
- "setDmManager:"
- "setVolumeEraseDispatchGroup:"
- "topLevelDisks"
- "unmountDisk:entireDisk:force:"
- "v20@0:8B16"
- "v24@0:8^{__DADisk=}16"
- "v24@0:8^{__DASession=}16"
- "v32@0:8^{__DADisk=}16B24f28"
- "v40@0:8^{__DADisk=}16@\"NSString\"24@\"NSDictionary\"32"
- "v40@0:8^{__DADisk=}16@24@32"
- "v40@0:8^{__DADisk=}16i24i28@\"NSDictionary\"32"
- "v40@0:8^{__DADisk=}16i24i28@32"
- "volumeEraseDispatchGroup"
- "volumeNameForDisk:error:"
- "volumeUUIDForDisk:error:"
```
