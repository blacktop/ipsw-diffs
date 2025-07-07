## nanotimekitcompaniond

> `/System/Library/PrivateFrameworks/NanoTimeKit.framework/nanotimekitcompaniond`

```diff

-2483.297.0.0.0
-  __TEXT.__text: 0x3f8d4
+2483.306.0.0.0
+  __TEXT.__text: 0x3f768
   __TEXT.__auth_stubs: 0xbd0
-  __TEXT.__objc_stubs: 0x5e00
-  __TEXT.__objc_methlist: 0x25d0
+  __TEXT.__objc_stubs: 0x5dc0
+  __TEXT.__objc_methlist: 0x2638
   __TEXT.__gcc_except_tab: 0xb0c
-  __TEXT.__cstring: 0x239a
-  __TEXT.__objc_methname: 0x6de9
-  __TEXT.__objc_classname: 0x62c
-  __TEXT.__objc_methtype: 0x1515
+  __TEXT.__cstring: 0x232b
+  __TEXT.__objc_methname: 0x6e20
+  __TEXT.__objc_classname: 0x627
+  __TEXT.__objc_methtype: 0x159c
   __TEXT.__const: 0xf0
-  __TEXT.__oslogstring: 0x5539
+  __TEXT.__oslogstring: 0x554c
   __TEXT.__ustring: 0x1ae
-  __TEXT.__unwind_info: 0x1078
+  __TEXT.__unwind_info: 0x1070
   __DATA_CONST.__auth_got: 0x5f8
-  __DATA_CONST.__got: 0x410
-  __DATA_CONST.__const: 0x1bc0
-  __DATA_CONST.__cfstring: 0x1540
+  __DATA_CONST.__got: 0x408
+  __DATA_CONST.__const: 0x1ba0
+  __DATA_CONST.__cfstring: 0x14e0
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xd8

   __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x38a8
-  __DATA.__objc_selrefs: 0x1b88
+  __DATA.__objc_const: 0x38f0
+  __DATA.__objc_selrefs: 0x1bc0
   __DATA.__objc_ivar: 0x2b8
   __DATA.__objc_data: 0x9b0
   __DATA.__data: 0xa28
-  __DATA.__bss: 0x1f8
+  __DATA.__bss: 0x1e8
   - /System/Library/Frameworks/ClockKit.framework/ClockKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/NanoPhotosCore.framework/NanoPhotosCore
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/NanoTimeKit.framework/NanoTimeKit
+  - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
   - /System/Library/PrivateFrameworks/PairedSync.framework/PairedSync
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/RelevanceEngine.framework/RelevanceEngine
   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 10060BD4-4BB4-348B-8800-C683DEC1C5D8
-  Functions: 1267
-  Symbols:   332
-  CStrings:  2153
+  UUID: EF6AF6A1-253D-3C89-A9D0-D17E148644CA
+  Functions: 1265
+  Symbols:   331
+  CStrings:  2159
 
Symbols:
+ _OBJC_CLASS_$_PDRRegistry
+ _PDRDevicePropertyKeySystemBuildVersion
- _NRDevicePropertyPairingID
- _NRDevicePropertySystemBuildVersion
- _OBJC_CLASS_$_NRPairedDeviceRegistry
CStrings:
+ "Current device forced update - _device: %{public}@ - pairingID: %{public}@"
+ "NTKDSyncController received CLKActiveDeviceChangedTinkerState"
+ "PDRDevicePropertySystemBuildVersion did change. enqueuing sync request"
+ "PDRRegistryDelegate"
+ "SYNC SHOULD BE %{public}@. isDemoMode: %lu, altdv: %lu, deviceSupportsCapability: %lu, paired: %lu, deviceUUID: %{public}@"
+ "Skipping snapshot migration - Bridge manages it"
+ "addDelegate:"
+ "all"
+ "deviceForPDRDevice:"
+ "deviceForPairingID:"
+ "devices"
+ "getActivePairedDeviceExcludingAltAccount"
+ "isPaired"
+ "isRunningNapiliGMOrLater"
+ "paired sync restriction lifted but we don't have a nano registry device. pairingID: %{public}@"
+ "pdrDevice"
+ "pdrDeviceForPairingID:"
+ "pdrDeviceVersion"
+ "registry:added:"
+ "registry:changed:properties:"
+ "registry:compatibilityStateChanged:"
+ "registry:didActivate:"
+ "registry:didDeactivate:"
+ "registry:didPair:"
+ "registry:didSetup:"
+ "registry:didUnpair:"
+ "registry:removed:"
+ "registryChanged:"
+ "supportsPDRCapability:"
+ "v24@0:8@\"PDRRegistry\"16"
+ "v32@0:8@\"PDRRegistry\"16@\"NSUUID\"24"
+ "v32@0:8@\"PDRRegistry\"16@\"PDRDevice\"24"
+ "v32@0:8@\"PDRRegistry\"16q24"
+ "v40@0:8@\"PDRRegistry\"16@\"PDRDevice\"24@\"NSSet\"32"
- "2CE80E5D-FA17-4BD4-A48C-DFC3A79FB8ED"
- "AE03A48B-6794-4978-96CC-425A7F6443DA"
- "CLKDeviceUUIDForNRDevice:"
- "Current device forced update - _device: %{public}@ - activeNRDevice: %{public}@"
- "D0D02931-2190-4E71-B843-C73C4ADB3F27"
- "NRDevicePropertyObserver"
- "NRDevicePropertySystemBuildVersion did change. enqueuing sync request"
- "NRProductVersionForNRDevice:"
- "NTKDSyncController received NRPairedDeviceRegistryDeviceDidPairNotification"
- "SYNC SHOULD BE %{public}@. isDemoMode: %lu, altdv: %lu, deviceSupportsCapability: %lu, has nrDevice: %lu, deviceUUID: %{public}@"
- "activeNRDevice"
- "activePairedDeviceSelectorBlock"
- "addPropertyObserver:forPropertyChanges:"
- "device:propertyDidChange:fromValue:"
- "deviceForNRDevice:"
- "deviceForNRDeviceUUID:"
- "getAllDevices"
- "getAllDevicesWithArchivedAltAccountDevicesMatching:"
- "getPairedDevices"
- "nrDeviceForNRDeviceUUID:"
- "nrDeviceUUID"
- "nrDeviceVersion"
- "paired sync restriction lifted but we don't have a nano registry device. activeNRDevice: %{public}@"
- "supportsCapability:"
- "v40@0:8@\"NRDevice\"16@\"NSString\"24@32"

```
