## CoreHAP

> `/System/Library/PrivateFrameworks/CoreHAP.framework/CoreHAP`

```diff

-1241.4.11.0.0
-  __TEXT.__text: 0x1a4294
-  __TEXT.__auth_stubs: 0x1580
-  __TEXT.__objc_methlist: 0x11954
-  __TEXT.__const: 0x700
-  __TEXT.__gcc_except_tab: 0x6188
-  __TEXT.__cstring: 0xfd88
-  __TEXT.__oslogstring: 0x1f876
+1277.0.0.1.2
+  __TEXT.__text: 0x1a3f14
+  __TEXT.__auth_stubs: 0x1590
+  __TEXT.__objc_methlist: 0x136c0
+  __TEXT.__const: 0x6f0
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__unwind_info: 0x5f28
+  __TEXT.__gcc_except_tab: 0x622c
+  __TEXT.__cstring: 0x1085b
+  __TEXT.__oslogstring: 0x1fa09
+  __TEXT.__unwind_info: 0x5cb0
   __TEXT.__objc_classname: 0x2ddd
-  __TEXT.__objc_methname: 0x261a2
-  __TEXT.__objc_methtype: 0x8ee7
-  __TEXT.__objc_stubs: 0x18300
-  __DATA_CONST.__got: 0xa60
-  __DATA_CONST.__const: 0x4fd8
+  __TEXT.__objc_methname: 0x26368
+  __TEXT.__objc_methtype: 0x8f28
+  __TEXT.__objc_stubs: 0x18400
+  __DATA_CONST.__got: 0xa68
+  __DATA_CONST.__const: 0x4fc8
   __DATA_CONST.__objc_classlist: 0x960
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x330
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6ce8
+  __DATA_CONST.__objc_selrefs: 0x6e48
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x7e0
   __DATA_CONST.__objc_arraydata: 0x208
-  __AUTH_CONST.__auth_got: 0xad0
+  __AUTH_CONST.__auth_got: 0xad8
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x800
-  __AUTH_CONST.__cfstring: 0xd380
-  __AUTH_CONST.__objc_const: 0x25158
-  __AUTH_CONST.__objc_intobj: 0x678
+  __AUTH_CONST.__cfstring: 0xd940
+  __AUTH_CONST.__objc_const: 0x21e30
+  __AUTH_CONST.__objc_intobj: 0x6a8
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH.__objc_data: 0x4e70
-  __DATA.__objc_ivar: 0x14c0
-  __DATA.__data: 0x2662
-  __DATA.__bss: 0x499
+  __DATA.__objc_ivar: 0x14c4
+  __DATA.__data: 0x266a
+  __DATA.__bss: 0x4a9
   __DATA_DIRTY.__objc_data: 0xf50
-  __DATA_DIRTY.__bss: 0xc8
+  __DATA_DIRTY.__bss: 0xb8
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/HomeKitFeatures.framework/HomeKitFeatures
   - /System/Library/PrivateFrameworks/HomeKitMetrics.framework/HomeKitMetrics
   - /System/Library/PrivateFrameworks/MobileBluetooth.framework/MobileBluetooth
+  - /System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit
   - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi
   - /System/Library/PrivateFrameworks/NearField.framework/NearField
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 7513
-  Symbols:   8717
-  CStrings:  11046
+  Functions: 7446
+  Symbols:   8733
+  CStrings:  11115
 
Symbols:
+ _HMMInternalErrorMarkerKey
+ _HTTPClientGetClientID
+ _WiFiJoinNetwork_b
- _WiFiJoinNetwork
CStrings:
+ "%@\x1e%@"
+ "%@ Canceling connection idle timer of: %fs"
+ "%@ Failed to parse protocol version from string: %@"
+ "%{public}@Canceling connection idle timer of: %0.3fs"
+ "%{public}@Creating socket connection using both IP and DNS Name: %@ ... %@ with output string: %@"
+ "%{public}@Received Bonjour event - canceling timer"
+ "%{public}@WiFiJoinNetwork_b called completion after self had been destroyed"
+ "%{public}@[HAP HTTP Client] Setting destination to %@:%@ with CoreUtils client ID: %x"
+ "%{public}@pending bonjour remove event for suspended accessory server: %{public}@ with suspendedState %lu"
+ "%{public}@pending bonjour remove event for suspended accessory server: %{public}@ with wake number %lu"
+ "@56@0:8@16@24@32@40q48"
+ "@64@0:8q16@24@32@40@48q56"
+ "Accessory server transport no longer open after sending request"
+ "Attempting to create HDS keys without an active session"
+ "Base class HAPAccessoryServer does not implement validatePairingAuthMethod"
+ "COAP Response Code: %ldd"
+ "Cannot disable notifications on unpaired accessory server"
+ "Cannot enable notifications on unpaired accessory server"
+ "Cannot get characteristics while unpaired"
+ "Cannot read characteristics on unpaired accessory server"
+ "Cannot update notification configuration while unpaired"
+ "Cannot write characteristics on unpaired accessory server"
+ "DEMO"
+ "Error Allocating HAPWACAccessoryClient"
+ "Failed instantiating easy config with scan result: %@"
+ "Failed to handle request because httpClient has been deallocated"
+ "HAP2 Accessory server state != HAP2AccessoryServerTransportStateOpen during completion handler of sendRequest"
+ "HAP2 CoAP failed due to HAP2CoAPIOConsumerFailureReasonNotDeliverable"
+ "HAP2AccessoryServer cannot send request when transport not open"
+ "HAP2AccessoryServer.isPaired is false during _readValuesForCharacteristics"
+ "HAP2AccessoryServer.isPaired is false during disableNotificationsForCharacteristics"
+ "HAP2AccessoryServer.isPaired is false during enableNotificationsForCharacteristics"
+ "HAP2AccessoryServer.isPaired is false during writeValuesForCharacteristics"
+ "HAP2AccessoryServerTransport state != HAP2AccessoryServerTransportStateOpen when calling sendRequestWithOperation"
+ "HAP2AccessoryServerTransportCoAP discovered 0 addresses during call to _resolveAddress"
+ "HAPAccessoryServerHAP2Adapter has nil pairedServer during _enableEvents:forCharacteristics"
+ "HAPAccessoryServerHAP2Adapter.pairedServer is nil during _hap2CharacteristicTuplesForHAPCharacteristics"
+ "HAPAccessoryServerIP._pairingSession nil during createKeysForDataStream"
+ "HAPAccessoryServerIP.hapWACAccessoryClient is null after _joinAccessoryNetworkWithCompletion"
+ "HAPWACAccessoryClient.ezConfigDevice is nil during performEasyConfigWithPairingPrompt"
+ "Lost discovery advertisement while accessory was reporting reachable"
+ "Lost paired accessory server"
+ "Lost unpaired accessory server"
+ "No advertisement"
+ "Not sending auth challenge request because the accessory doesn't claim to support it"
+ "On demand connections are enabled and the accessory is marked as reachable but lacks an advertisement"
+ "Owner Pairing"
+ "Received txtRecord that has a bad value for key '%@' ('%@'): %@"
+ "Resolved no addresses"
+ "TB"
+ "Tq,N,V_currentSocketUpdateType"
+ "[inKeychainItem.accessGroup isEqual:kWillowKeychainAccessGroup]"
+ "_currentSocketUpdateType"
+ "_populateSocketUpdateType"
+ "_socketUpdateTypeForCachedSocketInfo:newSocketInfo:"
+ "_userInfoWithDescription:reason:suggestion:underlyingError:marker:"
+ "addKeychainItem:error:"
+ "currentSocketUpdateType"
+ "decryptData:additionalAuthenticatedData not supported on HAP2AccessoryServerSecureTransportBase"
+ "encryptData:additionalAuthenticatedData not supported on HAP2AccessoryServerSecureTransportBase"
+ "getClientID"
+ "hapErrorWithCode:description:reason:suggestion:underlyingError:marker:"
+ "hapHMErrorWithCode:description:reason:suggestion:underlyingError:marker:"
+ "i24@0:8^{HTTPMessagePrivate={__CFRuntimeBase=QAQ}^{HTTPMessagePrivate}{?=[8192c]Q*Q*Qi*Q{?=*Q*Q*Q*Q*Q*Q*Q***Q*Q}*Qi*QCQCi}CiC*QQQ[1000C]*^{?}*Q[2{iovec=^vQ}]^{iovec}iQiii^v^v^v^v^v^v^?^?@?iCq*iQI*}16"
+ "inKeychainItem.accessGroup"
+ "inKeychainItem.account"
+ "inKeychainItem.creationDate"
+ "inKeychainItem.type"
+ "inKeychainItem.viewHint"
+ "lost discovery advertisement"
+ "mtr2"
+ "mtrS"
+ "nfcA"
+ "q32@0:8@16@24"
+ "serializeDictionary:options:"
+ "serializeImmutableDictionary:"
+ "setCurrentSocketUpdateType:"
+ "setUseDeferredResolutionStrategy:"
+ "useDeferredResolutionStrategy"
+ "v16@?0^{HTTPMessagePrivate={__CFRuntimeBase=QAQ}^{HTTPMessagePrivate}{?=[8192c]Q*Q*Qi*Q{?=*Q*Q*Q*Q*Q*Q*Q***Q*Q}*Qi*QCQCi}CiC*QQQ[1000C]*^{?}*Q[2{iovec=^vQ}]^{iovec}iQiii^v^v^v^v^v^v^?^?@?iCq*iQI*}8"
+ "v32@0:8^{HTTPMessagePrivate={__CFRuntimeBase=QAQ}^{HTTPMessagePrivate}{?=[8192c]Q*Q*Qi*Q{?=*Q*Q*Q*Q*Q*Q*Q***Q*Q}*Qi*QCQCi}CiC*QQQ[1000C]*^{?}*Q[2{iovec=^vQ}]^{iovec}iQiii^v^v^v^v^v^v^?^?@?iCq*iQI*}16@?24"
+ "validatePairingAuthMethod not supported on HAPAccessoryServerHAP2Adapter"
+ "\x83\"\x13\x11m\x12"
+ "\xf0\xb1"
- "%@ Failed to parse protocol version: %@"
- "%@ Suspending connection idle timer of: %fs"
- "%{public}@Received Bonjour event - suspending timer"
- "%{public}@Suspending connection idle timer of: %0.3fs"
- "%{public}@[HAP HTTP Client] Setting destination to %@:%@"
- "%{public}@pending bonjour remove event for suspended accessory server: %{public}@"
- "1.1"
- "_userInfoWithDescription:reason:suggestion:underlyingError:"
- "i24@0:8^{HTTPMessagePrivate={__CFRuntimeBase=QAQ}^{HTTPMessagePrivate}{?=[8192c]Q*Q*Qi*Q{?=*Q*Q*Q*Q*Q*Q*Q***Q*Q}*Qi*QCQCi}CiC*QQQ[1000C]*^{?}*Q[2{iovec=^vQ}]^{iovec}iQiii^v^v^v^v^v^v^?^?@?iCq*iQI}16"
- "inKeychainItem.platformReference"
- "initWithVersionString:"
- "serializeDictionary:"
- "v16@?0^{HTTPMessagePrivate={__CFRuntimeBase=QAQ}^{HTTPMessagePrivate}{?=[8192c]Q*Q*Qi*Q{?=*Q*Q*Q*Q*Q*Q*Q***Q*Q}*Qi*QCQCi}CiC*QQQ[1000C]*^{?}*Q[2{iovec=^vQ}]^{iovec}iQiii^v^v^v^v^v^v^?^?@?iCq*iQI}8"
- "v32@0:8^{HTTPMessagePrivate={__CFRuntimeBase=QAQ}^{HTTPMessagePrivate}{?=[8192c]Q*Q*Qi*Q{?=*Q*Q*Q*Q*Q*Q*Q***Q*Q}*Qi*QCQCi}CiC*QQQ[1000C]*^{?}*Q[2{iovec=^vQ}]^{iovec}iQiii^v^v^v^v^v^v^?^?@?iCq*iQI}16@?24"
- "\x83\"\x13\x11]\x12"
- "\xf0\xa1"

```
