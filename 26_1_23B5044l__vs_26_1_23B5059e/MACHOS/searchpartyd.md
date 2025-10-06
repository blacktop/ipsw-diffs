## searchpartyd

> `/usr/libexec/searchpartyd`

```diff

-423.31.7.14.8
-  __TEXT.__text: 0x12a92fc
-  __TEXT.__auth_stubs: 0x7b10
+423.31.7.14.16
+  __TEXT.__text: 0x12dd12c
+  __TEXT.__auth_stubs: 0x7b20
   __TEXT.__objc_stubs: 0xc0
-  __TEXT.__objc_methlist: 0x3bb4
-  __TEXT.__objc_methname: 0xe1f6
-  __TEXT.__cstring: 0x394fd
+  __TEXT.__objc_methlist: 0x3bfc
+  __TEXT.__objc_methname: 0xe23b
+  __TEXT.__cstring: 0x399ed
   __TEXT.__objc_classname: 0x5ad
   __TEXT.__objc_methtype: 0x48b0
-  __TEXT.__const: 0x83280
-  __TEXT.__oslogstring: 0x423ec
-  __TEXT.__swift5_typeref: 0x21b4a
-  __TEXT.__constg_swiftt: 0x1e8dc
-  __TEXT.__swift5_reflstr: 0x20c3f
-  __TEXT.__swift5_fieldmd: 0x2260c
+  __TEXT.__const: 0x83f20
+  __TEXT.__oslogstring: 0x42e5c
+  __TEXT.__swift5_typeref: 0x21d04
+  __TEXT.__swift5_fieldmd: 0x2297c
+  __TEXT.__constg_swiftt: 0x1ea9c
   __TEXT.__swift5_builtin: 0x938
-  __TEXT.__swift5_assocty: 0x2aa0
-  __TEXT.__swift5_capture: 0x173c4
-  __TEXT.__swift5_proto: 0x5994
-  __TEXT.__swift5_types: 0x1d6c
-  __TEXT.__swift_as_entry: 0x2878
-  __TEXT.__swift_as_ret: 0x5470
-  __TEXT.__swift5_protos: 0x2e8
-  __TEXT.__swift5_mpenum: 0x858
+  __TEXT.__swift5_reflstr: 0x2105f
+  __TEXT.__swift5_assocty: 0x2ae8
+  __TEXT.__swift5_protos: 0x2ec
+  __TEXT.__swift5_proto: 0x5a08
+  __TEXT.__swift5_types: 0x1d90
+  __TEXT.__swift_as_entry: 0x2924
+  __TEXT.__swift5_capture: 0x17674
+  __TEXT.__swift_as_ret: 0x5654
+  __TEXT.__swift5_mpenum: 0x880
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x3bb58
-  __TEXT.__eh_frame: 0xb6954
-  __DATA_CONST.__auth_got: 0x3d90
-  __DATA_CONST.__got: 0x3180
-  __DATA_CONST.__auth_ptr: 0x4288
-  __DATA_CONST.__const: 0x68c68
+  __TEXT.__unwind_info: 0x3ba78
+  __TEXT.__eh_frame: 0xb9c84
+  __DATA_CONST.__auth_got: 0x3d98
+  __DATA_CONST.__got: 0x3188
+  __DATA_CONST.__auth_ptr: 0x42d0
+  __DATA_CONST.__const: 0x695d8
   __DATA_CONST.__cfstring: 0x80
-  __DATA_CONST.__objc_classlist: 0x818
+  __DATA_CONST.__objc_classlist: 0x828
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x338
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x1a8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__linkguard: 0x15
-  __DATA.__objc_const: 0x19970
-  __DATA.__objc_selrefs: 0x31a0
+  __DATA.__objc_const: 0x19ba0
+  __DATA.__objc_selrefs: 0x31b0
   __DATA.__objc_ivar: 0x10
-  __DATA.__objc_data: 0x3698
-  __DATA.__data: 0x39740
-  __DATA.__common: 0x2a78
-  __DATA.__bss: 0xab7c0
+  __DATA.__objc_data: 0x3688
+  __DATA.__data: 0x39a20
+  __DATA.__bss: 0xac640
+  __DATA.__common: 0x2a80
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 34F3B0F8-DBD5-361B-B78F-7BAA66932939
-  Functions: 57613
-  Symbols:   4115
-  CStrings:  12529
+  UUID: D1B12AB9-BF4A-352E-9884-D74B85B42D31
+  Functions: 58112
+  Symbols:   4117
+  CStrings:  12608
 
Symbols:
+ _$s10Foundation4DateV10FindMyBaseE7iso8601SSvg
+ _$s10Foundation8CalendarV19autoupdatingCurrentACvgZ
+ _$s10Foundation8TimeZoneV19autoupdatingCurrentACvgZ
+ _$s15FindMyBluetooth14ConnectUseCaseO04findB11UTTransientyA2CmFWC
- _$s10Foundation8TimeZoneV10FindMyBaseE3gmtACvgZ
- _$ss6ResultO10FindMyBaseE5errorq_Sgvg
CStrings:
+ "%s %{private,mask.hash}s"
+ "%s %{public}s. %{public}@"
+ "%s %{public}s. %{public}@. Error: %{public}@"
+ "%s Connected to classic peripheral: %{public}s"
+ "%s Invalid Config response!"
+ "%s Invalid Non-owner response!"
+ "%s Invalid Owner response!"
+ "%s Invalid iCloudResponse!"
+ "%s Invalid keyAlignmentResponse!"
+ "%s Invalid primaryKeyResponse!"
+ "%s Missing beacon info for %{private,mask.hash}s."
+ "%s Missing beacon record for %{private,mask.hash}s."
+ "%s Missing primaryKey for %{private,mask.hash}s."
+ "%s No base date for beacon %{private,mask.hash}s."
+ "%s No beacon matching %{private,mask.hash}s!"
+ "%s Non-owner stop sound on device: %{private,mask.hash}s"
+ "%s Received keyAlignmentResponse: %s"
+ "%s Retrieved %{public}s for unknownBeaconId %{public}s"
+ "%s Skipping .unpaired part %{private,mask.hash}s"
+ "%s Unable to compute next 4am date"
+ "%s Unsupported command %s"
+ "%s beacon record for %{private,mask.hash}s!"
+ "%s beacon:%{private,mask.hash}s serialNumber:%{private,mask.hash}s, primaryIndex:%{public}s primaryKey:%s, nextPrimaryKeyRoll:%ums secondaryKeyEvaluationIndex:%u"
+ "%s beacon:%{public}s"
+ "%s beacon:%{public}s %{public}@"
+ "%s error is expected from BT callback but it is nil! %{public}s. %{public}@."
+ "%s failed on device %{public}s commandId: %{public}s. Error: %{public}@"
+ "%s for unknownBeaconId %{public}s"
+ "%s on device %{public}s commandId: %{public}s."
+ "%s peer cannot be nil!"
+ "%s succeeded on device %{public}s commandId: %{public}s."
+ "%s: %{public}s. Disabling pairing agent %{public}@"
+ "%s: No pairing subject for %s. Peers %{public}s."
+ ".getCurrentPrimaryKey"
+ ".keyAlignmentConfig"
+ ".keyAlignmentConfigResponse"
+ ".missingPrimaryKey"
+ ".startNonOwnerBTFinding("
+ ".startNonOwnerSound"
+ ".stopNonOwnerBTFinding"
+ ".stopNonOwnerSound"
+ "Can't monitor beacon: %s before first unlock."
+ "Can't monitor beacon: %s due to: missing services BeaconStoreActor / ObservationStoreService."
+ "Discovered FindMy services and characteristic."
+ "EnableKeyAlignmentOverClassicForAll"
+ "Error handling connection event for %{public}s: %{public}@"
+ "Failed to configure key alignment for %{private,mask.hash}s error %{public}@"
+ "Failed to fetch latest beacon observation. Error: %{public}@"
+ "Failed to get BeaconStoreActor"
+ "KeyAlignmentIndexOffsetOverride"
+ "LocalPairingMonitorService"
+ "Looking for beacon group matching %{public}s"
+ "No beacon group was found for connected peripheral: %{public}s"
+ "No beacons for UUID: %{private,mask.hash}s"
+ "No previous BT pairing event when unpairing %{private,mask.hash}s, do NOT BT unpair."
+ "PID:%ld is not supported and `supportKeyAlignmentOverClassic` is false"
+ "Received KeyAlignmentResponse %s. Beacon %{private,mask.hash}s Command %{public}s."
+ "Received iCloudIdentifierResponse %{public}s. Beacon %{private,mask.hash}s Command %{public}s."
+ "Received primaryKeyResponse %{public}s. Beacon %{private,mask.hash}s Command %{public}s."
+ "Received soundCompleted response. Beacon %{private,mask.hash}s Command %{public}s."
+ "Remote UI did invalidate, setting isCurrentlyPresentingAlert to false"
+ "Scheduled connection expiry for beacon %{private,mask.hash}s."
+ "Separation monitoring is paused for beacon: %{private,mask.hash}s"
+ "Separation monitoring is paused for beacon: %{private,mask.hash}s without observation."
+ "Session %{public}s, %{public}s update: %ld, remove: %ld, initial: %{bool}d."
+ "State is not interruptible!"
+ "Stored last connectable device count %{public}s."
+ "Unable to retrieve lastPairingEvents due to %{public}s"
+ "_TtC12searchpartyd26LocalPairingMonitorService"
+ "_TtC12searchpartyd29AccessoryConfigurationService"
+ "accessoryConfigService"
+ "appBundleID"
+ "associatedBeaconsCount"
+ "classic(peripheral:"
+ "configureKeyAlignment(peripheral:serialNumber:pairingState:)"
+ "connectNonOwner(unknownBeaconId:connectUseCase:)"
+ "connectedStateClients"
+ "didInvalidateRemoteUI()"
+ "fetchCurrentPrimaryKey(_:completion:)"
+ "fetchCurrentPrimaryKey(beaconId:)"
+ "fetchCurrentPrimaryKey:completion:"
+ "fetchiCloudIdentifier(_:completion:)"
+ "fetchiCloudIdentifier(beaconId:)"
+ "fetchiCloudIdentifier:completion:"
+ "lastObservedIndex(for:)"
+ "lastObservedIndex:%s offsetOverride:%ld"
+ "lastPairingEvents"
+ "monitor"
+ "numberOfKeysBefore4amRoll"
+ "numberOfKeysBefore4amRoll: now:%s wild4amDate:%s\nremainingTimeInSeconds:%f"
+ "pairingAgent(_:peerDidCompletePairing:)"
+ "pairingAgent(_:peerDidFailToCompletePairing:error:)"
+ "peerDidCompletePairing(peer:error:)"
+ "received(response:command:)"
+ "spNonOwnerStopSound(wildBeacon:commandId:)"
+ "supportKeyAlignmentOverClassic"
- "Can't monitor beacon: %s due to: airpods but expired (%f > %f sec ago)"
- "Can't monitor beacon: %s due to: airpods but missing last BT observation."
- "Enabling separation monitoring for %{private,mask.hash}s"
- "Failed to enable separation monitoring for %{private,mask.hash}s error: %@"
- "Session %{public}s, %{public}s update: %ld, remove: %ld."
- "Stored last connectable device count %ld."
- "UserDefaults value has changed: %s"
- "Will monitor beacon: %s due to: airpods, not expired (%f < %f sec ago)"
- "disablePairing()"
- "enableSeparationMonitoring(for:)"
- "pairingEvents"
- "peerDidCompletePairing: %{public}s. %{public}@"
- "peerDidCompletePairing: No pairing subject for %s. Peers %{public}s."
- "peerDidCompletePairing: peer cannot be nil!"
- "peerDidFailToCompletePairing: %{public}s. %{public}@"
- "peerDidFailToCompletePairing: No pairing subject for %s. Peers %{public}s."
- "peerDidFailToCompletePairing: peer cannot be nil!"

```
