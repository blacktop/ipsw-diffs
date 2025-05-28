## searchpartyd

> `/usr/libexec/searchpartyd`

```diff

-355.1.6.0.1
-  __TEXT.__text: 0xffaf7c
-  __TEXT.__auth_stubs: 0x5ce0
+356.7.0.0.0
+  __TEXT.__text: 0x1008464
+  __TEXT.__auth_stubs: 0x5de0
   __TEXT.__objc_stubs: 0x40
   __TEXT.__objc_methlist: 0x13e8
   __TEXT.__oslogstring: 0x10c
   __TEXT.__objc_classname: 0x519
-  __TEXT.__objc_methname: 0xcbb0
+  __TEXT.__objc_methname: 0xcbfc
   __TEXT.__objc_methtype: 0x3f9c
-  __TEXT.__cstring: 0x67533
-  __TEXT.__swift5_typeref: 0x1d2e8
-  __TEXT.__const: 0x48bc8
-  __TEXT.__constg_swiftt: 0x1966c
+  __TEXT.__cstring: 0x67b43
+  __TEXT.__swift5_typeref: 0x1d518
+  __TEXT.__const: 0x48d58
+  __TEXT.__constg_swiftt: 0x1973c
   __TEXT.__swift5_builtin: 0x820
-  __TEXT.__swift5_reflstr: 0x1a902
-  __TEXT.__swift5_fieldmd: 0x1b0f0
+  __TEXT.__swift5_reflstr: 0x1a9b2
+  __TEXT.__swift5_fieldmd: 0x1b190
   __TEXT.__swift5_assocty: 0x25e0
-  __TEXT.__swift5_proto: 0x44fc
-  __TEXT.__swift5_types: 0x16bc
-  __TEXT.__swift5_capture: 0x15e94
-  __TEXT.__swift5_protos: 0x27c
+  __TEXT.__swift5_proto: 0x4514
+  __TEXT.__swift5_types: 0x16c4
+  __TEXT.__swift5_capture: 0x15418
+  __TEXT.__swift5_protos: 0x284
   __TEXT.__swift5_mpenum: 0x3c4
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x2ed30
-  __TEXT.__eh_frame: 0x67778
-  __DATA_CONST.__auth_got: 0x2e78
-  __DATA_CONST.__got: 0x1b80
-  __DATA_CONST.__auth_ptr: 0xd68
-  __DATA_CONST.__const: 0x6a9e0
+  __TEXT.__unwind_info: 0x2ea3c
+  __TEXT.__eh_frame: 0x682f8
+  __DATA_CONST.__auth_got: 0x2ef8
+  __DATA_CONST.__got: 0x1b98
+  __DATA_CONST.__auth_ptr: 0xd70
+  __DATA_CONST.__const: 0x690e0
   __DATA_CONST.__objc_classlist: 0x6a8
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x318
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__linkguard: 0x15
-  __DATA.__objc_const: 0x1a790
+  __DATA.__objc_const: 0x1a840
   __DATA.__objc_selrefs: 0x2290
   __DATA.__objc_protorefs: 0x198
   __DATA.__objc_classrefs: 0x638
   __DATA.__objc_data: 0x38b8
-  __DATA.__data: 0x37b58
-  __DATA.__bss: 0x835b0
-  __DATA.__common: 0x1bb0
+  __DATA.__data: 0x37c00
+  __DATA.__bss: 0x837b0
+  __DATA.__common: 0x1bd0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 64451
-  Symbols:   2791
-  CStrings:  10821
+  Functions: 64190
+  Symbols:   2807
+  CStrings:  10841
 
Symbols:
+ _$s8SPShared21BluetoothPairingStateV10isUnpairedSbvg
+ _$sSS5index_8offsetBySS5IndexVAD_SitF
+ _$sSs10lowercasedSSyF
+ _MobileGestalt_copy_buildVersion_obj
+ _MobileGestalt_copy_cpuArchitecture_obj
+ _MobileGestalt_copy_hwModelStr_obj
+ _MobileGestalt_copy_lowPowerExpressModesSupported_obj
+ _MobileGestalt_copy_productType_obj
+ _MobileGestalt_copy_productVersion_obj
+ _MobileGestalt_copy_regionCode_obj
+ _MobileGestalt_copy_serialNumber_obj
+ _MobileGestalt_copy_uniqueDeviceID_obj
+ _MobileGestalt_copy_userAssignedDeviceName_obj
+ _MobileGestalt_get_chipID
+ _MobileGestalt_get_current_device
+ _MobileGestalt_get_uniqueChipID
+ _MobileGestalt_get_wapiCapability
- _MGCopyAnswerWithError
CStrings:
+ "BeaconManagerService"
+ "BeaconPayloadPublisher checked-in %{public}s publish activity %s."
+ "BeaconPayloadPublisher expected to run %{public}s with new criteria delay %lld, gracePeriod %lld."
+ "Cannot create client beacon share for owner circle: %{private,mask.hash}s."
+ "Could not prepare analytics event for sytem error display id prefix."
+ "Display identifiers contain unexpected prefix. Owner: %ld, member: %ld."
+ "Expired share cleanup filed due to error: %{public}s"
+ "Failed running publish block: %{public}s."
+ "Failed to remove orphaned owner sharing circle: %{private,mask.hash}s,\nbeacon: %{private,mask.hash}s, Error: %{public}s."
+ "Failure on handleCircleTrust, accepting of already accepted share: no  owner peer trust record!"
+ "Failure on share accept, can't fetch locations, no shared beacon record for: %{private,mask.hash}s"
+ "FinderStateManager state changed %{public}s."
+ "Found %ld orphaned secrets for %{private,mask.hash}s share."
+ "Handle incoming share suggestion"
+ "Looking for orphaned sharing circle secrets..."
+ "Missing member peer trust for member in member circle: %{private,mask.hash}s,\n owner: %{private,mask.hash}s."
+ "Missing member peer trust for owner in member circle: %{private,mask.hash}s,\n owner: %{private,mask.hash}s."
+ "No BeaconManagerService available!"
+ "Orphaned sharing circle secrets cleanup failed due to error: %{public}s"
+ "Orphaned sharing circles cleanup failed due to error: %{public}s"
+ "Potential key sync update for beacon %{private,mask.hash}s, advertisementAddress: %{private,mask.hash}s, index: %llu, indexObservationDate %{public}s."
+ "Ran publish block without specifying policy - no budgets needing bypass."
+ "Running publish activity %{public}s."
+ "SendDisplayIdPrefixAnalyticsError"
+ "Share request data for unknownBeacon: %{private,mask.hash}s,\nowner peer trust: %{private,mask.hash}s,\nshare: %{private,mask.hash}s."
+ "SubscribeAndFetch: cached location for id: %s, sending before subscribe %s"
+ "SubscribeAndFetch: cached location for id: %s- no cached location, moving on"
+ "TB,R,N,G_isPartiallyClientized"
+ "_isPartiallyClientized"
+ "com.apple.bluetooth.pairingWithReason"
+ "com.apple.icloud.searchpartyd.itemSharing.systemErrorDisplayIdPrefix"
+ "familyMemberCount"
+ "isPartiallyClientized"
+ "locationsFetcher"
+ "memberTrustDisplayIdPrefix"
+ "ownerTrustDisplayIdPrefix"
+ "previousLoggedDisplayIdentifierErrors"
+ "renewCriteria"
+ "shareAcceptanceExecutor"
- "%{public}@: getCriteria called on invalidated XPCActivity"
- "%{public}@: nil dictionary is found"
- "/YYygAofPDbhrwToVsXdeA"
- "BeaconPayloadPublisher checked-in %{public}@ publish activity %{public}@"
- "BeaconPayloadPublisher expected to run with existing criteria: %@"
- "BeaconPayloadPublisher expected to run with new criteria: %@"
- "Failed to remove orphaned owner sharing circle: %{private,mask.hash}s,\nbeacon: %{private,mask.hash}s, Error: %{public}@."
- "FinderStateManager state changed %@."
- "JHXk7RXOxvlqK+SxkwcM2A"
- "MGCopyAnswerWithError error for key: %@ -> %@"
- "Missing ownerTrust for owner in member circle: %{private,mask.hash}s,\n owner: %{private,mask.hash}s."
- "Running publish activity %@"
- "UserAssignedDeviceName"
- "activitiesCheckedIn"
- "chipId is not available."
- "com.apple.bluetooth.pairing"
- "ecid is not available."
- "h63QSdBCiT/z0WU6rdQv6Q"
- "k7QIBwZJJOVw+Sej/8h8VA"

```
