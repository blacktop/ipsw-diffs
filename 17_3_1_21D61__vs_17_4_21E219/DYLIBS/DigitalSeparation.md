## DigitalSeparation

> `/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation`

```diff

-355.0.3.0.0
-  __TEXT.__text: 0x19c28
-  __TEXT.__auth_stubs: 0x620
-  __TEXT.__objc_methlist: 0xf6c
-  __TEXT.__cstring: 0xf51
-  __TEXT.__const: 0x20
-  __TEXT.__gcc_except_tab: 0x37c
-  __TEXT.__oslogstring: 0x1555
+360.0.26.0.0
+  __TEXT.__text: 0x1afc0
+  __TEXT.__auth_stubs: 0x650
+  __TEXT.__objc_methlist: 0xfec
+  __TEXT.__cstring: 0xfe2
+  __TEXT.__const: 0x28
+  __TEXT.__gcc_except_tab: 0x488
+  __TEXT.__oslogstring: 0x1600
   __TEXT.__dlopen_cstrs: 0x68
-  __TEXT.__unwind_info: 0x54c
-  __TEXT.__objc_classname: 0x16e
-  __TEXT.__objc_methname: 0x32eb
-  __TEXT.__objc_methtype: 0x7b5
-  __TEXT.__objc_stubs: 0x2d80
+  __TEXT.__unwind_info: 0x594
+  __TEXT.__objc_classname: 0x17e
+  __TEXT.__objc_methname: 0x359f
+  __TEXT.__objc_methtype: 0x7cf
+  __TEXT.__objc_stubs: 0x3000
   __DATA_CONST.__got: 0x170
-  __DATA_CONST.__const: 0x9f0
-  __DATA_CONST.__objc_classlist: 0x88
+  __DATA_CONST.__const: 0xab0
+  __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1de8
-  __DATA_CONST.__objc_selrefs: 0xd58
-  __AUTH_CONST.__cfstring: 0xf40
-  __AUTH_CONST.__const: 0x1a0
-  __AUTH_CONST.__objc_const: 0x8d0
-  __AUTH_CONST.__auth_got: 0x320
-  __AUTH.__objc_data: 0x550
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x1b8
-  __DATA.__objc_superrefs: 0x40
-  __DATA.__objc_ivar: 0xc8
+  __DATA_CONST.__objc_const: 0x1ea0
+  __DATA_CONST.__objc_selrefs: 0xe08
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x1d0
+  __DATA_CONST.__objc_superrefs: 0x40
+  __AUTH_CONST.__cfstring: 0xfe0
+  __AUTH_CONST.__const: 0x1c0
+  __AUTH_CONST.__objc_const: 0x918
+  __AUTH_CONST.__auth_got: 0x338
+  __AUTH.__objc_data: 0x5a0
+  __DATA.__objc_ivar: 0xd0
   __DATA.__data: 0x1e8
-  __DATA.__bss: 0xd0
+  __DATA.__bss: 0xd8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
   - /System/Library/Frameworks/NetworkExtension.framework/NetworkExtension
   - /System/Library/PrivateFrameworks/ContactsFoundation.framework/ContactsFoundation
+  - /System/Library/PrivateFrameworks/DSRemotePairing.framework/DSRemotePairing
   - /System/Library/PrivateFrameworks/InstallCoordination.framework/InstallCoordination
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking

   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EFDD13AF-16AC-3BF3-8CBD-86895D95C49E
-  Functions: 483
-  Symbols:   1892
-  CStrings:  1052
+  UUID: C8C3DC9A-3CE6-3906-BFFB-AC4A9C6BEC0C
+  Functions: 508
+  Symbols:   1985
+  CStrings:  1096
 
Symbols:
+ -[DSWifiSyncStore .cxx_destruct]
+ -[DSWifiSyncStore fetchPairedDevicesOnQueue:completion:]
+ -[DSWifiSyncStore init]
+ -[DSWifiSyncStore remotePairing]
+ -[DSWifiSyncStore removeAllPairedDevicesOnQueue:completion:]
+ -[DSWifiSyncStore removeComputersFromRemotePairing:withCompletion:]
+ -[DSWifiSyncStore removePairedDevices:onQueue:withCompletion:]
+ -[DSWifiSyncStore setRemotePairing:]
+ -[DSWifiSyncStore setWorkQueue:]
+ -[DSWifiSyncStore workQueue]
+ _OBJC_CLASS_$_DSPairedComputer
+ _OBJC_CLASS_$_DSRemotePairingWrapper
+ _OBJC_CLASS_$_DSWifiSyncStore
+ _OBJC_CLASS_$_NSDate
+ _OBJC_IVAR_$_DSWifiSyncStore._remotePairing
+ _OBJC_IVAR_$_DSWifiSyncStore._workQueue
+ _OBJC_METACLASS_$_DSWifiSyncStore
+ __OBJC_$_INSTANCE_METHODS_DSWifiSyncStore
+ __OBJC_$_INSTANCE_VARIABLES_DSWifiSyncStore
+ __OBJC_$_PROP_LIST_DSWifiSyncStore
+ __OBJC_CLASS_RO_$_DSWifiSyncStore
+ __OBJC_METACLASS_RO_$_DSWifiSyncStore
+ ___50-[DSSharingType stopAllSharingOnQueue:completion:]_block_invoke.261
+ ___50-[DSSharingType stopAllSharingOnQueue:completion:]_block_invoke.261.cold.1
+ ___50-[DSSharingType stopAllSharingOnQueue:completion:]_block_invoke.263
+ ___52-[DSSharingType stopSharingPeople:queue:completion:]_block_invoke.267
+ ___54-[DSAppSharing resetShortcutsAutomationTimer:handler:]_block_invoke.328
+ ___55-[DSSharingPerson stopSharingSources:queue:completion:]_block_invoke.277
+ ___56-[DSWifiSyncStore fetchPairedDevicesOnQueue:completion:]_block_invoke
+ ___56-[DSWifiSyncStore fetchPairedDevicesOnQueue:completion:]_block_invoke.21
+ ___56-[DSWifiSyncStore fetchPairedDevicesOnQueue:completion:]_block_invoke.4
+ ___56-[DSWifiSyncStore fetchPairedDevicesOnQueue:completion:]_block_invoke.4.cold.1
+ ___56-[DSWifiSyncStore fetchPairedDevicesOnQueue:completion:]_block_invoke_2
+ ___60-[DSWifiSyncStore removeAllPairedDevicesOnQueue:completion:]_block_invoke
+ ___60-[DSWifiSyncStore removeAllPairedDevicesOnQueue:completion:]_block_invoke.25
+ ___60-[DSWifiSyncStore removeAllPairedDevicesOnQueue:completion:]_block_invoke.cold.1
+ ___60-[DSWifiSyncStore removeAllPairedDevicesOnQueue:completion:]_block_invoke.cold.2
+ ___62-[DSWifiSyncStore removePairedDevices:onQueue:withCompletion:]_block_invoke
+ ___62-[DSWifiSyncStore removePairedDevices:onQueue:withCompletion:]_block_invoke_2
+ ___62-[DSWifiSyncStore removePairedDevices:onQueue:withCompletion:]_block_invoke_3
+ ___62-[DSWifiSyncStore removePairedDevices:onQueue:withCompletion:]_block_invoke_4
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___block_descriptor_32_e47_q24?0"DSPairedComputer"8"DSPairedComputer"16l
+ ___block_descriptor_40_e8_32r_e17_v16?0"NSError"8lr32l8
+ ___block_descriptor_56_e8_32s40bs48r_e5_v8?0ls40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s48l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_literal_global.279
+ ___block_literal_global.280
+ ___block_literal_global.297
+ _lockdown_copy_paired_host_info
+ _lockdown_delete_pair_records
+ _lockdown_unpair_host_by_id
+ _objc_msgSend$compare:
+ _objc_msgSend$datePaired
+ _objc_msgSend$dateWithTimeIntervalSince1970:
+ _objc_msgSend$earlierDate:
+ _objc_msgSend$getPairedDevicesWithCompletion:
+ _objc_msgSend$initWithDeviceName:
+ _objc_msgSend$lockdownFrameworkIdentifier
+ _objc_msgSend$lockdownFrameworkKey
+ _objc_msgSend$marketingName
+ _objc_msgSend$remotePairing
+ _objc_msgSend$remotePairingFrameworkIdentifier
+ _objc_msgSend$removeAllPairedDevices
+ _objc_msgSend$removeComputersFromRemotePairing:withCompletion:
+ _objc_msgSend$removeSelectedDevices:onQueue:withCompletion:
+ _objc_msgSend$setDatePaired:
+ _objc_msgSend$setLockdownFrameworkIdentifier:
+ _objc_msgSend$setLockdownFrameworkKey:
+ _objc_msgSend$setMarketingName:
+ _objc_msgSend$setRemotePairing:
+ _objc_msgSend$setSerialNumber:
- ___50-[DSSharingType stopAllSharingOnQueue:completion:]_block_invoke.237
- ___50-[DSSharingType stopAllSharingOnQueue:completion:]_block_invoke.237.cold.1
- ___50-[DSSharingType stopAllSharingOnQueue:completion:]_block_invoke.239
- ___52-[DSSharingType stopSharingPeople:queue:completion:]_block_invoke.243
- ___54-[DSAppSharing resetShortcutsAutomationTimer:handler:]_block_invoke.304
- ___55-[DSSharingPerson stopSharingSources:queue:completion:]_block_invoke.253
- ___block_literal_global.255
- ___block_literal_global.256
- ___block_literal_global.273
CStrings:
+ "@\"DSRemotePairingWrapper\""
+ "DSWifiSyncStore"
+ "Error retrieving at least one paired device: %@"
+ "HostName"
+ "MarketingName"
+ "Remote Pairing - Error removing at least one paired device: %@"
+ "SerialNumber"
+ "SystemBUID"
+ "T@\"DSRemotePairingWrapper\",&,N,V_remotePairing"
+ "T@\"NSArray\",?,R,C,N"
+ "T@\"NSString\",?,R,C"
+ "WallTimeWhenCreated"
+ "WifiSyncQueue"
+ "_remotePairing"
+ "datePaired"
+ "dateWithTimeIntervalSince1970:"
+ "earlierDate:"
+ "fetchPairedDevicesOnQueue:completion:"
+ "getPairedDevicesWithCompletion:"
+ "initWithDeviceName:"
+ "liblockdown - Error removing at least one paired device: %d"
+ "lockdownFrameworkIdentifier"
+ "lockdownFrameworkKey"
+ "marketingName"
+ "q24@?0@\"DSPairedComputer\"8@\"DSPairedComputer\"16"
+ "remotePairing"
+ "remotePairingFrameworkIdentifier"
+ "removeAllPairedDevices"
+ "removeAllPairedDevicesOnQueue:completion:"
+ "removeComputersFromRemotePairing:withCompletion:"
+ "removePairedDevices:onQueue:withCompletion:"
+ "removeSelectedDevices:onQueue:withCompletion:"
+ "setDatePaired:"
+ "setLockdownFrameworkIdentifier:"
+ "setLockdownFrameworkKey:"
+ "setMarketingName:"
+ "setRemotePairing:"
+ "setSerialNumber:"

```
