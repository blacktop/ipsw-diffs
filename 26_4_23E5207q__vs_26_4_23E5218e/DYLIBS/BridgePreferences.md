## BridgePreferences

> `/System/Library/PrivateFrameworks/BridgePreferences.framework/BridgePreferences`

```diff

-1310.9.0.0.0
-  __TEXT.__text: 0x38b70
-  __TEXT.__auth_stubs: 0x1290
-  __TEXT.__objc_methlist: 0x3008
-  __TEXT.__const: 0x1924
+1310.10.0.0.0
+  __TEXT.__text: 0x395a0
+  __TEXT.__auth_stubs: 0x12b0
+  __TEXT.__objc_methlist: 0x31c0
+  __TEXT.__const: 0x1914
   __TEXT.__gcc_except_tab: 0x4d4
-  __TEXT.__cstring: 0x4482
-  __TEXT.__oslogstring: 0x1b68
+  __TEXT.__cstring: 0x4562
+  __TEXT.__oslogstring: 0x1cf8
   __TEXT.__dlopen_cstrs: 0x336
   __TEXT.__ustring: 0x46
   __TEXT.__swift5_typeref: 0x33c

   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0xf40
+  __TEXT.__unwind_info: 0xf80
   __TEXT.__eh_frame: 0x148
-  __TEXT.__objc_classname: 0x861
-  __TEXT.__objc_methname: 0x9716
-  __TEXT.__objc_methtype: 0x1358
-  __TEXT.__objc_stubs: 0x7020
-  __DATA_CONST.__got: 0x730
+  __TEXT.__objc_classname: 0x891
+  __TEXT.__objc_methname: 0x9ce6
+  __TEXT.__objc_methtype: 0x14d8
+  __TEXT.__objc_stubs: 0x7120
+  __DATA_CONST.__got: 0x758
   __DATA_CONST.__const: 0xe70
-  __DATA_CONST.__objc_classlist: 0x1b0
-  __DATA_CONST.__objc_protolist: 0x70
+  __DATA_CONST.__objc_classlist: 0x1b8
+  __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2890
+  __DATA_CONST.__objc_selrefs: 0x29b0
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0xb8
+  __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x140
-  __AUTH_CONST.__auth_got: 0x958
+  __AUTH_CONST.__auth_got: 0x968
   __AUTH_CONST.__const: 0xa88
   __AUTH_CONST.__cfstring: 0x4360
-  __AUTH_CONST.__objc_const: 0x4b58
+  __AUTH_CONST.__objc_const: 0x4e10
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x14d8
+  __AUTH.__objc_data: 0x1528
   __AUTH.__data: 0x400
-  __DATA.__objc_ivar: 0x2b4
-  __DATA.__data: 0x5d0
+  __DATA.__objc_ivar: 0x2cc
+  __DATA.__data: 0x630
   __DATA.__bss: 0x4d8
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0xf0

   - /System/Library/PrivateFrameworks/MobileIcons.framework/MobileIcons
   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
+  - /System/Library/PrivateFrameworks/NetworkRelay.framework/NetworkRelay
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/PBBridgeSupport.framework/PBBridgeSupport
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 30161E20-9849-327D-A17A-30F2403EFAB1
-  Functions: 1359
-  Symbols:   4416
-  CStrings:  3235
+  UUID: 22B6310A-3275-39B4-A355-02CFD3D1100F
+  Functions: 1379
+  Symbols:   4490
+  CStrings:  3313
 
Symbols:
+ -[BPSAWDLLinkBooster .cxx_destruct]
+ -[BPSAWDLLinkBooster currentLinkSubtype]
+ -[BPSAWDLLinkBooster dealloc]
+ -[BPSAWDLLinkBooster delegate]
+ -[BPSAWDLLinkBooster deviceIsConnectedDidChange:isConnected:]
+ -[BPSAWDLLinkBooster deviceLinkTypeDidChange:linkType:linkSubtype:]
+ -[BPSAWDLLinkBooster device]
+ -[BPSAWDLLinkBooster initWithDevice:]
+ -[BPSAWDLLinkBooster isHoldingLinkBoostAssertion]
+ -[BPSAWDLLinkBooster networkRelayDeviceMonitor]
+ -[BPSAWDLLinkBooster networkRelayDevicePreferences]
+ -[BPSAWDLLinkBooster referenceCount]
+ -[BPSAWDLLinkBooster releaseAWDLLinkBoost]
+ -[BPSAWDLLinkBooster requestAWDLLinkBoost]
+ -[BPSAWDLLinkBooster setCurrentLinkSubtype:]
+ -[BPSAWDLLinkBooster setDelegate:]
+ -[BPSAWDLLinkBooster setDevice:]
+ -[BPSAWDLLinkBooster setNetworkRelayDeviceMonitor:]
+ -[BPSAWDLLinkBooster setNetworkRelayDevicePreferences:]
+ -[BPSAWDLLinkBooster setReferenceCount:]
+ _OBJC_CLASS_$_BPSAWDLLinkBooster
+ _OBJC_CLASS_$_NRCompanionLinkPreferences
+ _OBJC_CLASS_$_NRDeviceIdentifier
+ _OBJC_CLASS_$_NRDeviceMonitor
+ _OBJC_CLASS_$_NRDevicePreferences
+ _OBJC_IVAR_$_BPSAWDLLinkBooster._currentLinkSubtype
+ _OBJC_IVAR_$_BPSAWDLLinkBooster._delegate
+ _OBJC_IVAR_$_BPSAWDLLinkBooster._device
+ _OBJC_IVAR_$_BPSAWDLLinkBooster._networkRelayDeviceMonitor
+ _OBJC_IVAR_$_BPSAWDLLinkBooster._networkRelayDevicePreferences
+ _OBJC_IVAR_$_BPSAWDLLinkBooster._referenceCount
+ _OBJC_METACLASS_$_BPSAWDLLinkBooster
+ __NRDevicePropertyBluetoothIdentifier
+ __OBJC_$_INSTANCE_METHODS_BPSAWDLLinkBooster
+ __OBJC_$_INSTANCE_VARIABLES_BPSAWDLLinkBooster
+ __OBJC_$_PROP_LIST_BPSAWDLLinkBooster
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NRDeviceMonitorDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NRDeviceMonitorDelegate
+ __OBJC_$_PROTOCOL_REFS_NRDeviceMonitorDelegate
+ __OBJC_CLASS_PROTOCOLS_$_BPSAWDLLinkBooster
+ __OBJC_CLASS_RO_$_BPSAWDLLinkBooster
+ __OBJC_LABEL_PROTOCOL_$_NRDeviceMonitorDelegate
+ __OBJC_METACLASS_RO_$_BPSAWDLLinkBooster
+ __OBJC_PROTOCOL_$_NRDeviceMonitorDelegate
+ _createStringFromNRLinkSubtype
+ _createStringFromNRLinkType
+ _objc_msgSend$initForHighThroughputWithServiceClass:includeP2P:
+ _objc_msgSend$initWithDeviceIdentifier:
+ _objc_msgSend$initWithDeviceIdentifier:delegate:queue:
+ _objc_msgSend$linkBooster:didUpgradeLinkToAWDL:
+ _objc_msgSend$linkBooster:linkSubtypeDidChange:
+ _objc_msgSend$linkSubtype
+ _objc_msgSend$newDeviceIdentifierWithBluetoothUUID:
+ _objc_msgSend$setCompanionLinkPreferences:
CStrings:
+ "%s: AWDL link boost requested successfully, reference count = 1"
+ "%s: Decremented reference count to %lu"
+ "%s: Device connected: %d"
+ "%s: Incrementing reference count to %lu"
+ "%s: Link changed - type: %@ (%d), subtype: %@ -> %@"
+ "%s: No Bluetooth identifier available for device"
+ "%s: No valid device to request link boost"
+ "%s: Releasing AWDL link boost"
+ "%s: Requesting AWDL link boost for device with BT ID: %@"
+ "-[BPSAWDLLinkBooster deviceIsConnectedDidChange:isConnected:]"
+ "-[BPSAWDLLinkBooster deviceLinkTypeDidChange:linkType:linkSubtype:]"
+ "-[BPSAWDLLinkBooster releaseAWDLLinkBoost]"
+ "-[BPSAWDLLinkBooster requestAWDLLinkBoost]"
+ "01299775-e611-4f05-8bff-abbd9995f4b8"
+ "01ef2814-5c39-4b0e-84b9-7b8e2cc06aa3"
+ "02168e84-5dd8-4b19-9204-a79f04b33a32"
+ "02979f49-fafa-49cc-8478-c2562bc81fb6"
+ "033c7b1f-5b25-459a-8cc7-4824b9c219f7"
+ "07e81b2d-193a-4898-bba4-b15e85a96be5"
+ "0c599fd8-cc9f-48c9-bc37-c764a8b0527c"
+ "0d852855-e6cf-45fa-b786-b26be87ff939"
+ "0e581e21-36ba-4770-9408-0467585e8495"
+ "0fc0e189-59f0-4bb1-acfc-570b13b35974"
+ "1171f09a-b15f-4c2c-a315-1a7a125ca54f"
+ "132c0e45-0099-4fc6-9fc2-d2c1f22bcc0e"
+ "135cfeb8-d730-40de-aa77-7668663f72c4"
+ "15afbf9d-37e7-4b41-8698-b0e518a0f6dc"
+ "15bf559d-d50b-44fe-ac84-dfba323ec985"
+ "1c82900f-82dc-41a4-a79f-5f107794c4a9"
+ "1cfaccb8-ffeb-4682-a50e-16f853583912"
+ "1e189be1-6a71-44aa-b116-0066a83035e8"
+ "210c1233-537b-4a1e-8ee0-253962851b43"
+ "2523bb16-06c1-4dec-bd23-cc0613ab0bdf"
+ "282f1ee6-a144-4106-affb-2bdb5b59fd0d"
+ "2a51e7b3-1b80-4981-9f09-f725bc3a8065"
+ "307631af-b309-4885-a4f2-122f156af14b"
+ "330af1f2-fd8f-40e4-b79c-2b0c476e6eaf"
+ "3955ca84-b333-44e3-b8c3-a420085151ee"
+ "39f111d2-c3d1-4ccc-ab05-e464de58625d"
+ "46526f47-0b4b-41ff-a959-ac358550958c"
+ "4aa3ff3b-3224-42e6-995e-481f49ae9260"
+ "4e8c3265-3d65-4e94-8bcd-23dc8c4fc8cf"
+ "506b78d5-f8ad-489a-8bf7-ad41268d0ff2"
+ "5b2ccb95-1760-430c-97b9-34bebb5bd70b"
+ "5c64c95b-8e7c-46ab-a110-1e51c93d7b7f"
+ "62aa8ec5-64fc-43d1-b856-d28d6520fa30"
+ "68ab2987-ce75-463c-9eaf-9861b292f01e"
+ "68e9d2af-a820-45fc-8fb3-92a04428cbf8"
+ "6aabb66b-8e1b-4cab-8fc4-ac577ba0afb0"
+ "6ade877a-70eb-43a1-a4d1-3e4bb50efa54"
+ "6b0579f9-ed84-4e5e-b753-83d35793f919"
+ "75584707-d2c4-481e-b8e8-3d8edd459b61"
+ "871e76a4-ad36-4aaf-b894-13caf677c531"
+ "8a7396ee-44e9-401d-8546-9f60232b29e7"
+ "90b8a394-4493-444d-aaa4-ddf6d6b68bc2"
+ "90f4ead7-dc19-4601-adb1-d1cee0c99ef8"
+ "91499922-4c63-41cf-884a-686713ce2738"
+ "939b3e66-90bd-4c9e-9fe5-150d338fb4e8"
+ "96b0dd78-1f0e-4f92-875f-dd6374fccb10"
+ "9b2fb519-d14b-49ab-bb91-67a6bf4e2b9a"
+ "9e6855a3-f1fd-444c-acb5-000f4203ef76"
+ "9eafa034-bab5-455f-a122-c2eb399e8fce"
+ "@\"<BPSAWDLLinkBoosterDelegate>\""
+ "@\"NRDeviceMonitor\""
+ "@\"NRDevicePreferences\""
+ "BPSAWDLLinkBooster"
+ "C"
+ "C16@0:8"
+ "NRDeviceMonitorDelegate"
+ "T@\"<BPSAWDLLinkBoosterDelegate>\",W,N,V_delegate"
+ "T@\"NRDevice\",&,N,V_device"
+ "T@\"NRDeviceMonitor\",&,N,V_networkRelayDeviceMonitor"
+ "T@\"NRDevicePreferences\",&,N,V_networkRelayDevicePreferences"
+ "TC,N,V_currentLinkSubtype"
+ "TQ,N,V_referenceCount"
+ "_currentLinkSubtype"
+ "_device"
+ "_networkRelayDeviceMonitor"
+ "_networkRelayDevicePreferences"
+ "_referenceCount"
+ "a4f025dd-e3e3-4886-8189-676ce98a6926"
+ "ab764ce8-d4df-4db6-991c-3a298e380bd1"
+ "b4b27f79-6817-4254-9232-37bfb09ce1b5"
+ "badf6e3e-9021-4b23-8ada-045a705dadc6"
+ "bd0302dd-00bc-43c2-81e9-48c038e6f8bb"
+ "bd3a4341-7090-4622-9694-2ac0f536c478"
+ "bf083122-a7ba-478f-a94e-e3f337f1177e"
+ "c0f3c2c3-0cde-4df9-a95a-789ac9a0348b"
+ "cb81f0ae-3f2f-4d57-8c90-f0d1a4add373"
+ "cbc78224-8f5e-4d43-8666-69adbe2a6277"
+ "cbf3763a-5f42-4463-b714-39903987fe90"
+ "currentLinkSubtype"
+ "d1c41a00-1654-467c-8793-6b4299699982"
+ "d1e83259-f3fc-4f20-82c3-c528d45560c3"
+ "d5737c61-3ee6-43da-b714-00f3746c50e1"
+ "d5834418-f4a0-4c74-aa38-8ed5f7765bd1"
+ "device"
+ "deviceHasUnpairedBluetooth:"
+ "deviceInfoDidChange:deviceInfo:"
+ "deviceIsAsleepDidChange:isAsleep:"
+ "deviceIsClassCConnectedDidChange:isClassCConnected:"
+ "deviceIsCloudConnectedDidChange:isCloudConnected:"
+ "deviceIsConnectedDidChange:isConnected:"
+ "deviceIsEnabledDidChange:isEnabled:"
+ "deviceIsNearbyDidChange:isNearby:"
+ "deviceIsRegisteredDidChange:isRegistered:"
+ "deviceLinkTypeDidChange:linkType:"
+ "deviceLinkTypeDidChange:linkType:linkSubtype:"
+ "devicePluggedInStateDidChange:pluggedIn:"
+ "deviceProxyServiceInterfaceNameDidChange:interfaceName:"
+ "deviceThermalPressureLevelDidChange:thermalPressureLevel:"
+ "deviceUsesAPLDidChange:usesAPL:"
+ "df99f619-b83a-4084-a29c-f15a82de2b15"
+ "e17d2903-b868-4e6c-8e76-6d4939beed44"
+ "e553d9c1-2587-4142-b286-c556e89f51f3"
+ "e7995851-d32d-4a4f-b12c-3dd8d0252581"
+ "e9cd3885-6bae-44af-8a2e-d2ac35470d03"
+ "ed2b57b6-9ea3-4ed9-843d-fe92f74b2de0"
+ "ed96b2dc-49dd-470d-bfe6-1f112af20308"
+ "ee952af6-9a20-42fc-b4cb-992d2c6aefea"
+ "efaf2aee-778b-4ccf-a640-ebd8c662d59b"
+ "f06861ae-125a-424b-af25-c1daa8f7aebc"
+ "f5c2dad0-38fb-4b3b-86d3-b264f4f8cbda"
+ "initForHighThroughputWithServiceClass:includeP2P:"
+ "initWithDeviceIdentifier:"
+ "initWithDeviceIdentifier:delegate:queue:"
+ "isHoldingLinkBoostAssertion"
+ "linkBooster:didUpgradeLinkToAWDL:"
+ "linkBooster:linkSubtypeDidChange:"
+ "linkSubtype"
+ "networkRelayDeviceMonitor"
+ "networkRelayDevicePreferences"
+ "newDeviceIdentifierWithBluetoothUUID:"
+ "referenceCount"
+ "releaseAWDLLinkBoost"
+ "requestAWDLLinkBoost"
+ "setCompanionLinkPreferences:"
+ "setCurrentLinkSubtype:"
+ "setDevice:"
+ "setNetworkRelayDeviceMonitor:"
+ "setNetworkRelayDevicePreferences:"
+ "setReferenceCount:"
+ "v20@0:8C16"
+ "v24@0:8@\"NRDeviceMonitor\"16"
+ "v28@0:8@\"NRDeviceMonitor\"16B24"
+ "v28@0:8@\"NRDeviceMonitor\"16C24"
+ "v28@0:8@\"NRDeviceMonitor\"16i24"
+ "v28@0:8@16C24"
+ "v28@0:8@16i24"
+ "v32@0:8@\"NRDeviceMonitor\"16@\"NRDeviceInfo\"24"
+ "v32@0:8@\"NRDeviceMonitor\"16@\"NSString\"24"
+ "v32@0:8@\"NRDeviceMonitor\"16C24C28"
+ "v32@0:8@16C24C28"
- "01299775-332F-481C-B7DE-7E80973B07BF"
- "01EF2814-332F-481C-B7DE-7E80973B07BF"
- "02168E84-332F-481C-B7DE-7E80973B07BF"
- "02979F49-332F-481C-B7DE-7E80973B07BF"
- "033C7B1F-332F-481C-B7DE-7E80973B07BF"
- "07E81B2D-332F-481C-B7DE-7E80973B07BF"
- "0C599FD8-332F-481C-B7DE-7E80973B07BF"
- "0D852855-332F-481C-B7DE-7E80973B07BF"
- "0E581E21-332F-481C-B7DE-7E80973B07BF"
- "0FC0E189-332F-481C-B7DE-7E80973B07BF"
- "1171F09A-332F-481C-B7DE-7E80973B07BF"
- "132C0E45-332F-481C-B7DE-7E80973B07BF"
- "135CFEB8-332F-481C-B7DE-7E80973B07BF"
- "15AFBF9D-332F-481C-B7DE-7E80973B07BF"
- "15BF559D-332F-481C-B7DE-7E80973B07BF"
- "1C82900F-332F-481C-B7DE-7E80973B07BF"
- "1CFACCB8-332F-481C-B7DE-7E80973B07BF"
- "1E189BE1-332F-481C-B7DE-7E80973B07BF"
- "210C1233-332F-481C-B7DE-7E80973B07BF"
- "2523BB16-332F-481C-B7DE-7E80973B07BF"
- "282F1EE6-332F-481C-B7DE-7E80973B07BF"
- "2A51E7B3-332F-481C-B7DE-7E80973B07BF"
- "307631AF-332F-481C-B7DE-7E80973B07BF"
- "330AF1F2-332F-481C-B7DE-7E80973B07BF"
- "3955CA84-332F-481C-B7DE-7E80973B07BF"
- "39F111D2-332F-481C-B7DE-7E80973B07BF"
- "46526F47-332F-481C-B7DE-7E80973B07BF"
- "4AA3FF3B-332F-481C-B7DE-7E80973B07BF"
- "4E8C3265-332F-481C-B7DE-7E80973B07BF"
- "506B78D5-332F-481C-B7DE-7E80973B07BF"
- "5B2CCB95-332F-481C-B7DE-7E80973B07BF"
- "5C64C95B-332F-481C-B7DE-7E80973B07BF"
- "62AA8EC5-332F-481C-B7DE-7E80973B07BF"
- "68AB2987-332F-481C-B7DE-7E80973B07BF"
- "68E9D2AF-332F-481C-B7DE-7E80973B07BF"
- "6AABB66B-332F-481C-B7DE-7E80973B07BF"
- "6ADE877A-332F-481C-B7DE-7E80973B07BF"
- "6B0579F9-332F-481C-B7DE-7E80973B07BF"
- "75584707-332F-481C-B7DE-7E80973B07BF"
- "871E76A4-332F-481C-B7DE-7E80973B07BF"
- "8A7396EE-332F-481C-B7DE-7E80973B07BF"
- "90B8A394-332F-481C-B7DE-7E80973B07BF"
- "90F4EAD7-332F-481C-B7DE-7E80973B07BF"
- "91499922-332F-481C-B7DE-7E80973B07BF"
- "939B3E66-332F-481C-B7DE-7E80973B07BF"
- "96B0DD78-332F-481C-B7DE-7E80973B07BF"
- "9B2FB519-332F-481C-B7DE-7E80973B07BF"
- "9E6855A3-332F-481C-B7DE-7E80973B07BF"
- "9EAFA034-332F-481C-B7DE-7E80973B07BF"
- "A4F025DD-332F-481C-B7DE-7E80973B07BF"
- "AB764CE8-332F-481C-B7DE-7E80973B07BF"
- "B4B27F79-332F-481C-B7DE-7E80973B07BF"
- "BADF6E3E-332F-481C-B7DE-7E80973B07BF"
- "BD0302DD-332F-481C-B7DE-7E80973B07BF"
- "BD3A4341-332F-481C-B7DE-7E80973B07BF"
- "BF083122-332F-481C-B7DE-7E80973B07BF"
- "C0F3C2C3-332F-481C-B7DE-7E80973B07BF"
- "CB81F0AE-332F-481C-B7DE-7E80973B07BF"
- "CBC78224-332F-481C-B7DE-7E80973B07BF"
- "CBF3763A-332F-481C-B7DE-7E80973B07BF"
- "D1C41A00-332F-481C-B7DE-7E80973B07BF"
- "D1E83259-332F-481C-B7DE-7E80973B07BF"
- "D5737C61-332F-481C-B7DE-7E80973B07BF"
- "D5834418-332F-481C-B7DE-7E80973B07BF"
- "DF99F619-332F-481C-B7DE-7E80973B07BF"
- "E17D2903-332F-481C-B7DE-7E80973B07BF"
- "E553D9C1-332F-481C-B7DE-7E80973B07BF"
- "E7995851-332F-481C-B7DE-7E80973B07BF"
- "E9CD3885-332F-481C-B7DE-7E80973B07BF"
- "ED2B57B6-332F-481C-B7DE-7E80973B07BF"
- "ED96B2DC-332F-481C-B7DE-7E80973B07BF"
- "EE952AF6-332F-481C-B7DE-7E80973B07BF"
- "EFAF2AEE-332F-481C-B7DE-7E80973B07BF"
- "F06861AE-332F-481C-B7DE-7E80973B07BF"
- "F5C2DAD0-332F-481C-B7DE-7E80973B07BF"

```
