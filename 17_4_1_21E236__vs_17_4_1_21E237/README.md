# 17.4.1 (21E236) .vs 17.4.1 (21E237)

## IPSWs

- `iPhone16,1_17.4.1_21E236_Restore.ipsw`
- `iPhone16,1_17.4.1_21E237_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 17.4.1 *(21E236)* | 23.4.0 | 10063.102.14~67 | Fri, 08Mar2024 23:31:42 PST |
| 17.4.1 *(21E237)* | 23.4.0 | 10063.102.14~67 | Fri, 08Mar2024 23:31:42 PST |

## MachO

### ⬆️ Updated (6)

<details>
  <summary><i>View Updated</i></summary>

#### RecoverDeviceUI

>  `/Applications/RecoverDeviceUI.app/RecoverDeviceUI`

```diff

-1856.100.79.0.3
+1856.102.1.0.0
   __TEXT.__text: 0x47a4
   __TEXT.__auth_stubs: 0x320
   __TEXT.__objc_stubs: 0xda0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 411EBE80-2207-3F99-BBAB-AF5FF7119960
+  UUID: F7309EE4-3F1B-3272-8CB3-E4A3FAE0DACA
   Functions: 79
   Symbols:   762
   CStrings:  483

```

#### MSUDataMigrator

>  `/System/Library/DataClassMigrators/MSUDataMigrator.migrator/MSUDataMigrator`

```diff

-1856.100.79.0.3
+1856.102.1.0.0
   __TEXT.__text: 0x13e4
   __TEXT.__auth_stubs: 0x2c0
   __TEXT.__objc_stubs: 0x2e0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2B853E6B-9781-39A7-9ECE-65C15AF64C05
+  UUID: 8CDB5234-CE25-3374-B87E-F43DA3A72543
   Functions: 13
   Symbols:   171
   CStrings:  99

```

#### softwareupdated

>  `/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/Support/softwareupdated`

```diff

-1856.100.79.0.3
+1856.102.1.0.0
   __TEXT.__text: 0x20f04
   __TEXT.__auth_stubs: 0x12f0
   __TEXT.__objc_stubs: 0x3120

   - /usr/lib/libc++.1.dylib
   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9C97AC55-A32B-33AF-83E7-FB601A1056E4
+  UUID: 5F0EE207-6CC1-3C39-AB30-30AB5D36C155
   Functions: 571
   Symbols:   4560
   CStrings:  3135
Symbols:
+ /AppleInternal/Library/BuildRoots/6b1b8477-e40f-11ee-8175-6e9a50d3f268/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCheckpoint.o)
+ /AppleInternal/Library/BuildRoots/6b1b8477-e40f-11ee-8175-6e9a50d3f268/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventRecorder.o)
+ /AppleInternal/Library/BuildRoots/6b1b8477-e40f-11ee-8175-6e9a50d3f268/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventShim.o)
+ /AppleInternal/Library/BuildRoots/6b1b8477-e40f-11ee-8175-6e9a50d3f268/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventSubmitter.o)
+ /AppleInternal/Library/BuildRoots/6b1b8477-e40f-11ee-8175-6e9a50d3f268/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_error.o)
+ /AppleInternal/Library/BuildRoots/6b1b8477-e40f-11ee-8175-6e9a50d3f268/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_log.o)
+ /AppleInternal/Library/BuildRoots/6b1b8477-e40f-11ee-8175-6e9a50d3f268/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_splat.o)
+ /AppleInternal/Library/BuildRoots/6b1b8477-e40f-11ee-8175-6e9a50d3f268/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libpartition.a(partition.o)
+ /AppleInternal/Library/BuildRoots/6b1b8477-e40f-11ee-8175-6e9a50d3f268/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/librestorecommon.a(RestoreCommon.o)
- /AppleInternal/Library/BuildRoots/2d3303f9-dd50-11ee-ac91-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCheckpoint.o)
- /AppleInternal/Library/BuildRoots/2d3303f9-dd50-11ee-ac91-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventRecorder.o)
- /AppleInternal/Library/BuildRoots/2d3303f9-dd50-11ee-ac91-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventShim.o)
- /AppleInternal/Library/BuildRoots/2d3303f9-dd50-11ee-ac91-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventSubmitter.o)
- /AppleInternal/Library/BuildRoots/2d3303f9-dd50-11ee-ac91-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_error.o)
- /AppleInternal/Library/BuildRoots/2d3303f9-dd50-11ee-ac91-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_log.o)
- /AppleInternal/Library/BuildRoots/2d3303f9-dd50-11ee-ac91-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_splat.o)
- /AppleInternal/Library/BuildRoots/2d3303f9-dd50-11ee-ac91-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libpartition.a(partition.o)
- /AppleInternal/Library/BuildRoots/2d3303f9-dd50-11ee-ac91-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/librestorecommon.a(RestoreCommon.o)

```

#### com.apple.MobileSoftwareUpdate.CleanupPreparePathService

>  `/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/XPCServices/com.apple.MobileSoftwareUpdate.CleanupPreparePathService.xpc/com.apple.MobileSoftwareUpdate.CleanupPreparePathService`

```diff

-1856.100.79.0.3
-  __TEXT.__text: 0x21d64
+1856.102.1.0.0
+  __TEXT.__text: 0x21e5c
   __TEXT.__auth_stubs: 0x1400
   __TEXT.__objc_stubs: 0x34a0
   __TEXT.__objc_methlist: 0x1284

   __TEXT.__objc_methname: 0x3914
   __TEXT.__objc_classname: 0x166
   __TEXT.__objc_methtype: 0xc1b
-  __TEXT.__unwind_info: 0x6e0
+  __TEXT.__unwind_info: 0x6e4
   __DATA_CONST.__auth_got: 0xa10
   __DATA_CONST.__got: 0x198
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x910
+  __DATA_CONST.__const: 0x920
   __DATA_CONST.__cfstring: 0x8fc0
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 81B2C550-AAC4-3A4E-AD11-300706245113
-  Functions: 615
-  Symbols:   4757
+  UUID: 664605E7-2527-3040-8B6D-5EF86D894EBD
+  Functions: 616
+  Symbols:   4762
   CStrings:  3599
 
Symbols:
+ /AppleInternal/Library/BuildRoots/6b1b8477-e40f-11ee-8175-6e9a50d3f268/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCheckpoint.o)
+ /AppleInternal/Library/BuildRoots/6b1b8477-e40f-11ee-8175-6e9a50d3f268/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCleanup.o)
+ /AppleInternal/Library/BuildRoots/6b1b8477-e40f-11ee-8175-6e9a50d3f268/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventRecorder.o)
+ /AppleInternal/Library/BuildRoots/6b1b8477-e40f-11ee-8175-6e9a50d3f268/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventShim.o)
+ /AppleInternal/Library/BuildRoots/6b1b8477-e40f-11ee-8175-6e9a50d3f268/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventSubmitter.o)
+ /AppleInternal/Library/BuildRoots/6b1b8477-e40f-11ee-8175-6e9a50d3f268/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(DevNodeWriter.o)
+ /AppleInternal/Library/BuildRoots/6b1b8477-e40f-11ee-8175-6e9a50d3f268/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IODualSPIWriter.o)
+ /AppleInternal/Library/BuildRoots/6b1b8477-e40f-11ee-8175-6e9a50d3f268/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IOServiceWriter.o)
+ /AppleInternal/Library/BuildRoots/6b1b8477-e40f-11ee-8175-6e9a50d3f268/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareError.o)
+ /AppleInternal/Library/BuildRoots/6b1b8477-e40f-11ee-8175-6e9a50d3f268/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareUpdater.o)
+ /AppleInternal/Library/BuildRoots/6b1b8477-e40f-11ee-8175-6e9a50d3f268/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(Image3.o)
+ /AppleInternal/Library/BuildRoots/6b1b8477-e40f-11ee-8175-6e9a50d3f268/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_error.o)
+ /AppleInternal/Library/BuildRoots/6b1b8477-e40f-11ee-8175-6e9a50d3f268/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_iokit_helpers.o)
+ /AppleInternal/Library/BuildRoots/6b1b8477-e40f-11ee-8175-6e9a50d3f268/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_lib.o)
+ /AppleInternal/Library/BuildRoots/6b1b8477-e40f-11ee-8175-6e9a50d3f268/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_log.o)
+ /AppleInternal/Library/BuildRoots/6b1b8477-e40f-11ee-8175-6e9a50d3f268/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_splat.o)
+ /AppleInternal/Library/BuildRoots/6b1b8477-e40f-11ee-8175-6e9a50d3f268/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_ticket.o)
+ /AppleInternal/Library/BuildRoots/6b1b8477-e40f-11ee-8175-6e9a50d3f268/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_update.o)
+ /AppleInternal/Library/BuildRoots/6b1b8477-e40f-11ee-8175-6e9a50d3f268/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libpartition.a(AMRestorePartition.o)
+ /AppleInternal/Library/BuildRoots/6b1b8477-e40f-11ee-8175-6e9a50d3f268/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libpartition.a(partition.o)
+ _UMEventCleanupNVRAMInternal
- /AppleInternal/Library/BuildRoots/2d3303f9-dd50-11ee-ac91-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCheckpoint.o)
- /AppleInternal/Library/BuildRoots/2d3303f9-dd50-11ee-ac91-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventCleanup.o)
- /AppleInternal/Library/BuildRoots/2d3303f9-dd50-11ee-ac91-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventRecorder.o)
- /AppleInternal/Library/BuildRoots/2d3303f9-dd50-11ee-ac91-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventShim.o)
- /AppleInternal/Library/BuildRoots/2d3303f9-dd50-11ee-ac91-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/lib/libUpdateMetrics.a(UMEventSubmitter.o)
- /AppleInternal/Library/BuildRoots/2d3303f9-dd50-11ee-ac91-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(DevNodeWriter.o)
- /AppleInternal/Library/BuildRoots/2d3303f9-dd50-11ee-ac91-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IODualSPIWriter.o)
- /AppleInternal/Library/BuildRoots/2d3303f9-dd50-11ee-ac91-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(IOServiceWriter.o)
- /AppleInternal/Library/BuildRoots/2d3303f9-dd50-11ee-ac91-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareError.o)
- /AppleInternal/Library/BuildRoots/2d3303f9-dd50-11ee-ac91-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libMSUBootFirmwareUpdater.a(MSUBootFirmwareUpdater.o)
- /AppleInternal/Library/BuildRoots/2d3303f9-dd50-11ee-ac91-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(Image3.o)
- /AppleInternal/Library/BuildRoots/2d3303f9-dd50-11ee-ac91-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_error.o)
- /AppleInternal/Library/BuildRoots/2d3303f9-dd50-11ee-ac91-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_iokit_helpers.o)
- /AppleInternal/Library/BuildRoots/2d3303f9-dd50-11ee-ac91-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_lib.o)
- /AppleInternal/Library/BuildRoots/2d3303f9-dd50-11ee-ac91-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_log.o)
- /AppleInternal/Library/BuildRoots/2d3303f9-dd50-11ee-ac91-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_splat.o)
- /AppleInternal/Library/BuildRoots/2d3303f9-dd50-11ee-ac91-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_ticket.o)
- /AppleInternal/Library/BuildRoots/2d3303f9-dd50-11ee-ac91-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libRamrodUpdateBrain.a(ramrod_update.o)
- /AppleInternal/Library/BuildRoots/2d3303f9-dd50-11ee-ac91-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libpartition.a(AMRestorePartition.o)
- /AppleInternal/Library/BuildRoots/2d3303f9-dd50-11ee-ac91-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libpartition.a(partition.o)

```

#### SoftwareUpdateSubscriber

>  `/System/Library/PrivateFrameworks/RemoteManagement.framework/XPCServices/SoftwareUpdateSubscriber.xpc/SoftwareUpdateSubscriber`

```diff

-1856.100.79.0.3
+1856.102.1.0.0
   __TEXT.__text: 0x2310
   __TEXT.__auth_stubs: 0x260
   __TEXT.__objc_stubs: 0x6c0

   - /System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3661D7D3-ABEA-3094-966D-AD84D5057D91
+  UUID: 2A489E0B-F482-3B57-B7E9-9DE0BFD5BF17
   Functions: 18
   Symbols:   357
   CStrings:  208

```

#### MSUEarlyBootTask

>  `/usr/libexec/MSUEarlyBootTask`

```diff

-1856.100.79.0.3
+1856.102.1.0.0
   __TEXT.__text: 0x4024
   __TEXT.__auth_stubs: 0x710
   __TEXT.__objc_stubs: 0x440

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8E4EFBF6-3C1E-358B-B162-E6448640D8DE
+  UUID: 840F546D-B950-3FE0-AF1D-09E984C2C25D
   Functions: 23
   Symbols:   309
   CStrings:  325
Symbols:
+ /AppleInternal/Library/BuildRoots/6b1b8477-e40f-11ee-8175-6e9a50d3f268/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libpartition.a(partition.o)
- /AppleInternal/Library/BuildRoots/2d3303f9-dd50-11ee-ac91-22c3409c8aad/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS17.4.Internal.sdk/usr/local/lib/libpartition.a(partition.o)

```


</details>

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 17.4.1 *(21E236)* | 618.1.15.10.15 |
| 17.4.1 *(21E237)* | 618.1.15.10.15 |

### Dylibs

#### ⬆️ Updated (4)

<details>
  <summary><i>View Updated</i></summary>

#### MobileSoftwareUpdate

>  `/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/MobileSoftwareUpdate`

```diff

-1856.100.79.0.3
+1856.102.1.0.0
   __TEXT.__text: 0xc1a8
   __TEXT.__auth_stubs: 0x670
   __TEXT.__objc_methlist: 0x100

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 02FAFA02-CD1F-3A38-8BDF-61B7B421EB40
+  UUID: 3DC41868-0F90-3B36-A104-087AC45389A0
   Functions: 201
   Symbols:   730
   CStrings:  806

```

#### SoftwareUpdateCore

>  `/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore`

```diff

-1856.100.79.0.3
+1856.102.1.0.0
   __TEXT.__text: 0xf7574
   __TEXT.__auth_stubs: 0x690
   __TEXT.__objc_methlist: 0x6710

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 945445AB-0E72-3848-B7A6-3F5CFBBCADEE
+  UUID: 29280048-0F88-34C2-92D6-897CB55F9A9E
   Functions: 2577
   Symbols:   8749
   CStrings:  7761

```

#### SoftwareUpdateCoreConnect

>  `/System/Library/PrivateFrameworks/SoftwareUpdateCoreConnect.framework/SoftwareUpdateCoreConnect`

```diff

-1856.100.79.0.3
+1856.102.1.0.0
   __TEXT.__text: 0xae98
   __TEXT.__auth_stubs: 0x400
   __TEXT.__objc_methlist: 0x6b4

   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C8342D8E-89DE-3F53-8F1B-F78B24957801
+  UUID: 86009222-B4DC-30B5-93CD-8CB7F31A7614
   Functions: 232
   Symbols:   903
   CStrings:  594

```

#### SoftwareUpdateCoreSupport

>  `/System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport`

```diff

-1856.100.79.0.3
+1856.102.1.0.0
   __TEXT.__text: 0x32644
   __TEXT.__auth_stubs: 0x680
   __TEXT.__objc_methlist: 0x3020

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 16AE0C5A-05B9-3835-8ACF-0EDD447EFC96
+  UUID: DBABF3CC-1291-3F55-97D9-785E5841ABED
   Functions: 1193
   Symbols:   4193
   CStrings:  4033

```


</details>

## EOF
