## HomeKitMatter

> `/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter`

```diff

-1278.5.13.1.5
-  __TEXT.__text: 0x130200
+1278.6.20.0.1
+  __TEXT.__text: 0x132aa4
   __TEXT.__auth_stubs: 0xa40
-  __TEXT.__objc_methlist: 0x9b4c
+  __TEXT.__objc_methlist: 0x9c54
   __TEXT.__const: 0x158
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__gcc_except_tab: 0x2ac0
-  __TEXT.__cstring: 0x61b7
-  __TEXT.__oslogstring: 0x254ee
+  __TEXT.__gcc_except_tab: 0x2b80
+  __TEXT.__cstring: 0x6262
+  __TEXT.__oslogstring: 0x25b8f
   __TEXT.__ustring: 0x68
-  __TEXT.__unwind_info: 0x2c48
-  __TEXT.__objc_classname: 0x1337
-  __TEXT.__objc_methname: 0x23640
-  __TEXT.__objc_methtype: 0x37a2
-  __TEXT.__objc_stubs: 0x15320
+  __TEXT.__unwind_info: 0x2cb8
+  __TEXT.__objc_classname: 0x133b
+  __TEXT.__objc_methname: 0x23b8b
+  __TEXT.__objc_methtype: 0x3817
+  __TEXT.__objc_stubs: 0x156a0
   __DATA_CONST.__got: 0x990
-  __DATA_CONST.__const: 0x4370
+  __DATA_CONST.__const: 0x4550
   __DATA_CONST.__objc_classlist: 0x3e8
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6658
+  __DATA_CONST.__objc_selrefs: 0x6738
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x2c8
   __DATA_CONST.__objc_arraydata: 0x228
   __AUTH_CONST.__auth_got: 0x530
   __AUTH_CONST.__const: 0xf00
   __AUTH_CONST.__cfstring: 0x6620
-  __AUTH_CONST.__objc_const: 0xe950
+  __AUTH_CONST.__objc_const: 0xe9a8
   __AUTH_CONST.__objc_intobj: 0x15d8
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x1db0
-  __DATA.__objc_ivar: 0xa4c
+  __DATA.__objc_ivar: 0xa50
   __DATA.__data: 0xd80
   __DATA.__bss: 0x408
   __DATA_DIRTY.__objc_data: 0x960

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4049
-  Symbols:   4808
-  CStrings:  8188
+  Functions: 4079
+  Symbols:   4838
+  CStrings:  8249
 
CStrings:
+ "\x02\x12"
+ "\x11A"
+ "\"\x11\x11"
+ "%{public}@Accessory server already purged by the time user responded"
+ "%{public}@Accessory server purged by the time user responded"
+ "%{public}@Accessory server was purged by the time device attestation completed"
+ "%{public}@Cleaning up stale MTRDevices"
+ "%{public}@Locally discovered server %@ matches the discriminator %@ (short %@)"
+ "%{public}@Notifying delegate of accessory vendor ID %@, product ID %@, device type %@"
+ "%{public}@Notifying matter accessory matching commissioning discriminator discovered"
+ "%{public}@Notifying supported link layer types: %@"
+ "%{public}@Removing unpaired node %@ from fabric %@ controller %@"
+ "%{public}@[Flow: %@] Credential exists at slot %ld for credentialType %ld"
+ "%{public}@[Flow: %@] Exhausted full occupied user sweep: %@"
+ "%{public}@[Flow: %@] Exhausted search for occupied credentials with result %@"
+ "%{public}@[Flow: %@] No user uniqueIDS and corresponding issuer keys to add"
+ "%{public}@[Flow: %@] Number of users with credentials: %ld are more than what is available on the lock: %lu"
+ "%{public}@[Flow: %@] Number of users with credentials: %ld are more than what the lock supports: %@"
+ "%{public}@[Flow: %@] Number of users: %ld are more than what the lock supports: %@"
+ "%{public}@[Flow: %@] Number of users: %ld are more than what the lock supports: %lu"
+ "%{public}@[Flow: %@] availableUserSlots: %@ | availableCredentialSlots %@"
+ "%{public}@[Flow: %@] findAllOccupiedCredentialSlotsForCredentialType: %ld startingAtSlot: %ld assumingTotalNumberOfSlots: %ld"
+ "%{public}@accessoryWithSameDiscriminatorDiscovered -> NO as setupPayload is missing"
+ "%{public}@accessoryWithSameDiscriminatorDiscovered -> YES as server was locally discovered"
+ "%{public}@announceOtaProvider for %@, immediateAnnouncement: %@, delayCounter: %lu"
+ "%{public}@isLocallyDiscoveredAndMatchesDiscriminatorOfSetupPayload compares short discriminator %@ against its own %@"
+ "%{public}@isLocallyDiscoveredAndMatchesDiscriminatorOfSetupPayload failed to match discriminator %@ against its own %@"
+ "%{public}@isLocallyDiscoveredAndMatchesDiscriminatorOfSetupPayload matched discriminator %@ against server's own"
+ "@56@0:8q16q24@32@40@48"
+ "@56@0:8q16q24q32@40@48"
+ "T@\"HMMTRAccessoryServer\",W,N,V_accessoryServer"
+ "TB,R,D,N"
+ "TQ,N,V_otaAnnounceDelayCounter"
+ "_cleanUpMTRDevicesWithFabricUUID:"
+ "_notifyDelegateOfAccessoryMatchingCommissioningDiscriminatorDiscovered"
+ "_notifyDelegateOfMatterAccessoryVendorID:productID:deviceType:"
+ "_notifyDelegateOfSupportedLinkLayerTypes:"
+ "_otaAnnounceDelayCounter"
+ "_updatePairingMetricsUponAccessoryDiscovery"
+ "accessoryWithSameDiscriminatorDiscovered"
+ "announceOtaProvider:providerEndpoint:immediateAnnouncement:delayCounter:completionHandler:"
+ "announceOtaProviderForNodeID:isRetry:"
+ "currentDeviceTypeFromDCL"
+ "fetchAvailableCredentialSlotsWithLimit:forCredentialType:flow:"
+ "fetchAvailableUserSlotsWithLimit:flow:"
+ "forgetDeviceWithNodeID:"
+ "getAllUsersStartingAtSlot:assumingTotalNumberOfSlots:users:temporaryCachedAliroCredentials:flow:"
+ "handleHomeAddedAccessoryWithNodeID:fabricUUID:"
+ "handleHomeRemovedAccessoryWithNodeID:fabricUUID:"
+ "hapIPErrorWithCode:marker:"
+ "incrementOtaAnnounceDelayCounter"
+ "initWithCapacity:"
+ "isLocallyDiscoveredAndMatchesDiscriminatorOfSetupPayload:"
+ "isUserSlotAvailableForUserResponse:"
+ "locallyDiscoveredAccessoryServerMatchesDiscriminatorOfSetupPayload:"
+ "na_safeAddObject:"
+ "nodesWithStoredData"
+ "notifyDelegateOfAccessoryMatchingCommissioningDiscriminatorDiscovered"
+ "notifyMatterAccessoryMatchingCommissioningDiscriminatorDiscovered"
+ "notifyMatterAccessoryVendorID:productID:deviceType:"
+ "notifySupportedLinkLayerTypes:"
+ "notifyUpdateRequestedForNodeID:isUserTriggered:isRetry:"
+ "otaAnnounceDelayCounter"
+ "resetOtaAnnounceDelayCounter"
+ "setOtaAnnounceDelayCounter:"
+ "totalNumberOfAliroDeviceKeyCredentialsSupportedWithFlow:"
+ "totalNumberOfAliroIssuerKeyCredentialsSupportedWithFlow:"
+ "totalNumberOfCredentialSlotsSupportedForCredentialType:flow:"
+ "v24@0:8@\"NSNumber\"16"
+ "v28@?0@\"HMMTRAccessoryServer\"8B16@\"NSError\"20"
+ "v32@?0@\"MTRDoorLockClusterGetUserResponseParams\"8Q16^B24"
+ "v32@?0@\"NSNumber\"8Q16^B24"
+ "v40@0:8@\"NSNumber\"16@\"NSNumber\"24@\"NSNumber\"32"
+ "v52@0:8@16@24B32q36@?44"
+ "{_HMFFutureBlockOutcome=q@}16@?0@\"NSSet\"8"
- "\x111"
- "#\x11"
- "%{public}@[Flow: %@] Adding issuerKey: %@ to userUniqueID: %@ toCredentialSlot: %ld"
- "%{public}@[Flow: %@] Credential slot resources have been exhausted"
- "%{public}@[Flow: %@] Error while reading number of aliro issuer key credentials supported: %@"
- "%{public}@[Flow: %@] userIndex is nil when trying to add credential to new user. Possible firmware issue."
- "%{public}@announceOtaProvider for %@"
- "addNewUsersWithUserUniqueIDs:withCorrespondingIssuerKeys:withIncrementor:forCredentialSlot:flow:"
- "announceOtaProvider:providerEndpoint:immediateAnnouncement:completionHandler:"
- "announceOtaProviderForNodeID:"
- "handleHomeAddedAccessoryWithNodeID:fabric:"
- "handleHomeRemovedAccessoryWithNodeID:"
- "notifyUpdateRequestedForNodeID:isUserTriggered:"
- "v44@0:8@16@24B32@?36"

```
