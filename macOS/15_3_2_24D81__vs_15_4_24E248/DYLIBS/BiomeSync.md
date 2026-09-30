## BiomeSync

> `/System/Library/PrivateFrameworks/BiomeSync.framework/Versions/A/BiomeSync`

```diff

-165.7.0.0.0
-  __TEXT.__text: 0x3750
+166.17.1.0.0
+  __TEXT.__text: 0x3700
   __TEXT.__auth_stubs: 0x180
-  __TEXT.__objc_methlist: 0x16c
-  __TEXT.__const: 0x50
+  __TEXT.__objc_methlist: 0x210
+  __TEXT.__const: 0x58
   __TEXT.__cstring: 0xf8
-  __TEXT.__gcc_except_tab: 0x288
+  __TEXT.__gcc_except_tab: 0x28c
   __TEXT.__oslogstring: 0x63
-  __TEXT.__unwind_info: 0x198
+  __TEXT.__unwind_info: 0x1a0
   __TEXT.__objc_classname: 0x6a
   __TEXT.__objc_methname: 0x5ca
   __TEXT.__objc_methtype: 0x191

   __AUTH_CONST.__auth_got: 0xd0
   __AUTH_CONST.__const: 0x140
   __AUTH_CONST.__cfstring: 0x100
-  __AUTH_CONST.__objc_const: 0x410
+  __AUTH_CONST.__objc_const: 0x2f0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x14
   __DATA.__data: 0x180

   - /System/Library/PrivateFrameworks/BiomeStorage.framework/Versions/A/BiomeStorage
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E3E7E802-22AE-39BE-BF8B-0D6C18B3CF0A
+  UUID: 841EA117-9F7B-3E0C-8670-E22AFC47C81C
   Functions: 66
   Symbols:   208
   CStrings:  116
Functions:
~ -[BMDevice initWithCoder:] : 364 -> 368
~ -[BMSyncService connection] : 1360 -> 1356
~ -[BMSyncService remoteDevicesWithReply:] : 464 -> 456
~ -[BMSyncService remoteDevicesForAccount:reply:] : 496 -> 488
~ -[BMSyncService triggerRapportSyncWithReply:] : 460 -> 452
~ -[BMSyncService triggerCloudKitSyncWithReply:] : 460 -> 452
~ -[BMSyncService remoteDevicesWithError:] : 672 -> 664
~ -[BMSyncService remoteDevicesForAccount:error:] : 692 -> 684
~ -[BMSyncService rapportSyncWithErrors:] : 676 -> 668
~ -[BMSyncService cascadeRapportSyncWithErrors:] : 676 -> 668
~ -[BMSyncService cloudKitSyncWithErrors:] : 676 -> 668
~ -[BMSyncService peerInformationWithError:] : 668 -> 660

```
