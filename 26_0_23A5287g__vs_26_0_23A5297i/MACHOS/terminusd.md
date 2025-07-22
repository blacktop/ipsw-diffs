## terminusd

> `/usr/libexec/terminusd`

```diff

-673.0.0.0.0
-  __TEXT.__text: 0x180aec
+676.0.3.0.0
+  __TEXT.__text: 0x182d2c
   __TEXT.__auth_stubs: 0x2bd0
-  __TEXT.__objc_stubs: 0x8720
-  __TEXT.__objc_methlist: 0x53a8
+  __TEXT.__objc_stubs: 0x84c0
+  __TEXT.__objc_methlist: 0x52a0
   __TEXT.__const: 0x24c
   __TEXT.__gcc_except_tab: 0x420c
-  __TEXT.__objc_methname: 0x119f9
-  __TEXT.__cstring: 0x410b1
+  __TEXT.__objc_methname: 0x11420
+  __TEXT.__cstring: 0x41347
   __TEXT.__oslogstring: 0x247e
-  __TEXT.__objc_classname: 0xe91
+  __TEXT.__objc_classname: 0xe92
   __TEXT.__objc_methtype: 0x382c
-  __TEXT.__unwind_info: 0x2450
+  __TEXT.__unwind_info: 0x2460
   __DATA_CONST.__auth_got: 0x15f8
   __DATA_CONST.__got: 0xa00
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x3418
-  __DATA_CONST.__cfstring: 0xbea0
+  __DATA_CONST.__const: 0x3458
+  __DATA_CONST.__cfstring: 0xbd20
   __DATA_CONST.__objc_classlist: 0x430
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x108
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x152e8
-  __DATA.__objc_selrefs: 0x2d50
-  __DATA.__objc_ivar: 0x1a80
+  __DATA.__objc_const: 0x15038
+  __DATA.__objc_selrefs: 0x2cc0
+  __DATA.__objc_ivar: 0x1a4c
   __DATA.__objc_data: 0x29e0
   __DATA.__data: 0xce8
   __DATA.__bss: 0x6b8

   - /usr/lib/libdns_services.dylib
   - /usr/lib/libmrc.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 142EC419-BC9B-36F0-B53C-2AE568BDA64D
-  Functions: 3101
+  UUID: 1FBA3609-AD68-3C89-8D93-A112A9F84CF8
+  Functions: 3085
   Symbols:   1036
-  CStrings:  11589
+  CStrings:  11530
 
CStrings:
+ "%s%.30s:%-4d \t\"%@\""
+ "%s%.30s:%-4d %@ failed to add removeProxyPolicyForListener %@ to session %@"
+ "%s%.30s:%-4d %@ failed to add removeProxyPolicyForResolver %@ to session %@"
+ "%s%.30s:%-4d %@ will start observing changes"
+ "%s%.30s:%-4d %@ will stop observing changes"
+ "%s%.30s:%-4d Client %@ scrubbing %@"
+ "%s%.30s:%-4d Client %@ scrubbing all devices"
+ "%s%.30s:%-4d Did not scrub enabled NRUUID %@"
+ "%s%.30s:%-4d Did not scrub registered NRUUID %@"
+ "%s%.30s:%-4d Did not scrub unknown NRUUID %@"
+ "%s%.30s:%-4d NRDLocalDevice observed properties:"
+ "%s%.30s:%-4d No remote %@ address recieved for %@"
+ "%s%.30s:%-4d Not scrubbing enabled NRUUID %@"
+ "%s%.30s:%-4d Not scrubbing registered NRUUID %@"
+ "%s%.30s:%-4d Scrubbed all devices"
+ "%s%.30s:%-4d Scrubbed device %@"
+ "+[NRDLocalDevice scrubAllDevicesWithCompletionBlock:]"
+ "+[NRDLocalDevice scrubDeviceWithNRUUID:completionBlock:]"
+ "-[NRDLocalDevice initWithNRUUID:]"
+ "02:12:34"
+ "676.0.3"
+ "Enabled NRUUID %@"
+ "Failed to add removeProxyPolicyForListener"
+ "Failed to add removeProxyPolicyForListener %@ to session %@"
+ "Failed to add removeProxyPolicyForResolver"
+ "Failed to add removeProxyPolicyForResolver %@ to session %@"
+ "Jul 11 2025"
+ "Registered NRUUID %@"
+ "TQ,N,V_databaseFlags"
+ "_catchAllMigrationInfoAgent"
+ "_databaseFlags"
+ "containsValueForKey:"
+ "databaseFlags"
+ "handleScrubAllDevices"
+ "handleScrubDeviceByNRUUID"
+ "keysSortedByValueUsingComparator:"
+ "q24@?0@\"NRDLocalDevice\"8@\"NRDLocalDevice\"16"
+ "setDatabaseFlags:"
- "%s%.30s:%-4d NRDLocalDevice observed proprties: %@"
- "+[NRDLocalDevice newLocalDeviceWithRandomNRUUID]"
- "-[NRDLocalDevice initWithoutObservingChangesWithNRUUID:]"
- "-[NRDLocalDevice initWithoutObservingChanges]"
- "01:24:59"
- "673"
- "Jun 25 2025"
- "T@\"NSDate\",&,N,V_dateCreated"
- "TB,N,V_hasAuthenticatedWithIdentity"
- "TB,N,V_hasCompletedBluetoothPairing"
- "TB,N,V_hasConfirmedClassAKeys"
- "TB,N,V_hasConfirmedClassCKeys"
- "TB,N,V_hasConfirmedClassDKeys"
- "TB,N,V_hasSavedClassCKeysInKeychain"
- "TB,N,V_hasSavedPairingInfoInKeychain"
- "TB,N,V_isAltAccountDevice"
- "TB,N,V_isEmptyPairing"
- "TB,N,V_isEnabled"
- "TB,N,V_isExternalDevice"
- "TB,N,V_isModernPairing"
- "TB,N,V_isRegistered"
- "TB,N,V_lastSeenAlwaysOnWiFiSupported"
- "TB,N,V_selfManagedBluetoothPairing"
- "TB,N,V_wasInitiallySetupUsingIDSPairing"
- "_hasAuthenticatedWithIdentity"
- "_hasCompletedBluetoothPairing"
- "_hasConfirmedClassAKeys"
- "_hasConfirmedClassCKeys"
- "_hasConfirmedClassDKeys"
- "_hasSavedClassCKeysInKeychain"
- "_hasSavedPairingInfoInKeychain"
- "_isAltAccountDevice"
- "_isModernPairing"
- "_lastSeenAlwaysOnWiFiSupported"
- "_selfManagedBluetoothPairing"
- "_wasInitiallySetupUsingIDSPairing"
- "classAKeychainItemsLegacyOnly"
- "classCKeychainItems"
- "classDKeychainItems"
- "ephemeralBluetoothOutOfBandKey"
- "hasCompletedBluetoothPairing"
- "hasCompletedPairing"
- "hasOutOfBandKey"
- "isChanged"
- "isCompanionLinkCheckedOnce"
- "isEnabledAndHasCompletedPairing"
- "isEphemeral"
- "isObservingChanges"
- "observedProperties"
- "outOfBandKeychainItem"
- "requiresAuthenticationWithIdentity"
- "selfManagedBluetoothPairing"
- "setDateCreated:"
- "setHasAuthenticatedWithIdentity:"
- "setHasCompletedBluetoothPairing:"
- "setHasConfirmedClassAKeys:"
- "setHasConfirmedClassCKeys:"
- "setHasConfirmedClassDKeys:"
- "setHasSavedClassCKeysInKeychain:"
- "setHasSavedPairingInfoInKeychain:"
- "setIsAltAccountDevice:"
- "setIsEmptyPairing:"
- "setIsEnabled:"
- "setIsExternalDevice:"
- "setIsModernPairing:"
- "setIsRegistered:"
- "setLastSeenAlwaysOnWiFiSupported:"
- "setSelfManagedBluetoothPairing:"
- "setWasInitiallySetupUsingIDSPairing:"
- "suspendNonNearbyLinks"

```
