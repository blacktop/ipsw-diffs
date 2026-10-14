## bluetoothd

> `/usr/sbin/bluetoothd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-2701.7.0.0.0
-  __TEXT.__text: 0x8f6ffc
-  __TEXT.__auth_stubs: 0x52e0
-  __TEXT.__objc_stubs: 0x19ce0
+2701.7.1.0.0
+  __TEXT.__text: 0x8fa904
+  __TEXT.__auth_stubs: 0x52f0
+  __TEXT.__objc_stubs: 0x1a160
   __TEXT.__init_offsets: 0x70
-  __TEXT.__objc_methlist: 0x9c24
-  __TEXT.__const: 0x25ec0
-  __TEXT.__gcc_except_tab: 0x70f5c
-  __TEXT.__cstring: 0xc8287
-  __TEXT.__objc_classname: 0xa45
-  __TEXT.__objc_methname: 0x1f7b1
-  __TEXT.__objc_methtype: 0x5ac0
-  __TEXT.__oslogstring: 0xc1891
+  __TEXT.__objc_methlist: 0x9e94
+  __TEXT.__const: 0x25f60
+  __TEXT.__gcc_except_tab: 0x71128
+  __TEXT.__cstring: 0xc8708
+  __TEXT.__objc_classname: 0xabf
+  __TEXT.__objc_methname: 0x1fcf7
+  __TEXT.__objc_methtype: 0x5af2
+  __TEXT.__oslogstring: 0xc1d08
   __TEXT.__swift5_typeref: 0x176
   __TEXT.__swift5_capture: 0xbc
   __TEXT.__constg_swiftt: 0x50

   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift_as_cont: 0x18
+  __TEXT.__dlopen_cstrs: 0x120
   __TEXT.__ustring: 0x34
-  __TEXT.__dlopen_cstrs: 0xd4
-  __TEXT.__unwind_info: 0x2e8b0
+  __TEXT.__unwind_info: 0x2e9a8
   __TEXT.__eh_frame: 0x2b0
-  __DATA_CONST.__const: 0x344f0
-  __DATA_CONST.__cfstring: 0x27a60
-  __DATA_CONST.__objc_classlist: 0x300
+  __DATA_CONST.__const: 0x34648
+  __DATA_CONST.__cfstring: 0x27ca0
+  __DATA_CONST.__objc_classlist: 0x328
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x220
+  __DATA_CONST.__objc_superrefs: 0x238
   __DATA_CONST.__objc_intobj: 0xa98
-  __DATA_CONST.__objc_arraydata: 0x408
+  __DATA_CONST.__objc_arraydata: 0x410
   __DATA_CONST.__objc_dictobj: 0x2d0
-  __DATA_CONST.__objc_arrayobj: 0x1e0
-  __DATA_CONST.__auth_got: 0x2988
+  __DATA_CONST.__objc_arrayobj: 0x1f8
+  __DATA_CONST.__auth_got: 0x2990
   __DATA_CONST.__got: 0xe70
   __DATA_CONST.__auth_ptr: 0x268
-  __DATA.__objc_const: 0x10a58
-  __DATA.__objc_selrefs: 0x77d0
-  __DATA.__objc_ivar: 0x11d8
-  __DATA.__objc_data: 0x1e70
-  __DATA.__data: 0x4f30
+  __DATA.__objc_const: 0x11038
+  __DATA.__objc_selrefs: 0x78f0
+  __DATA.__objc_ivar: 0x1214
+  __DATA.__objc_data: 0x2000
+  __DATA.__data: 0x4f38
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x17ca0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 37401
-  Symbols:   1818
-  CStrings:  43137
+  Functions: 37471
+  Symbols:   1819
+  CStrings:  43263
 
Symbols:
+ _abort_report_np
CStrings:
+ "\"items\" key is not an array"
+ "### Failed to decrypt HomeKitAccessoryControl beacon [%@]: %@"
+ "-[CBDaemonServer _decryptAndReportHomeKitAccessoryControlDevice:]_block_invoke_2"
+ "245b126d262dfe728b314ee4d1d1091bf7b406c8b7edd85b798173be285059e0"
+ "74f61a772a9da1812f68ab5854db675447cde80c20675e52a70ac43a7601865d"
+ "<%@: %p plaintextLen=%lu>"
+ "@\"HMProxBeaconKeybagXPCClient\""
+ "@\"NSError\""
+ "Beacon service data has unexpected length %lu"
+ "CoreHAP soft-link failed; cannot decrypt proximity beacons"
+ "Decrypted proximity control from HAP accessory - VID: 0x%08X, PID: 0x%08X, deviceID: %{private}02X:%{private}02X:%{private}02X:%{private}02X:%{private}02X:%{private}02X"
+ "Decrypted proximity control from Matter accessory - VID: 0x%04X, PID: 0x%04X, deviceID: 0x%{private}016llX"
+ "Decrypted proximity control with invalid configFeatures: 0x%02X, length: %lu"
+ "Failed to create XPC connection"
+ "Failed to create XPC connection to %{public}@"
+ "Failed to fetch beacon keybag from homed: domain=%{public}@ code=%ld"
+ "Fetched %lu beacon keybag items from homed"
+ "Fetched %lu beacon keys from homed"
+ "HAPECDSAKeyPairVerifySession"
+ "HAPECDSAKeyPairVerifySession class is unavailable (CoreHAP soft-link returned nil)"
+ "HMProxBeaconDecryptResult"
+ "HMProxBeaconDecryption"
+ "HMProxBeaconDecryptionErrorDomain"
+ "HMProxBeaconKeybagItem"
+ "HMProxBeaconKeybagXPCClient"
+ "HMProxBeaconKeybagXPCErrorDomain"
+ "HomeKitAccessoryControl decrypt success, parsing plaintext %@ with length=%lu"
+ "J490Setup"
+ "J491Setup"
+ "KatsuraA"
+ "Keybag fetch failed with XPC error: %{public}@"
+ "Keybag fetch timed out after %.1fs; homed may be hung"
+ "MRC logging for TVRemote LE link: %s"
+ "Mask gattName as Apple TV in gattDatabaseAccessedCb"
+ "Mask name as Apple TV in notifyHostnameChanged"
+ "Mask productType as Apple TV in readHostname"
+ "Mask productType as Apple TV in readProductType"
+ "MaskLocalNameAsAppleTV"
+ "MatsuA"
+ "MatsuB"
+ "RemoteConnectionImprovement"
+ "Reply is not a dictionary"
+ "Skipping scan prioritization over WiFi (highest agent scan percent:%d%%)"
+ "T@\"HMProxBeaconKeybagXPCClient\",&,N,V_xpcClient"
+ "T@\"NSArray\",&,N,V_keys"
+ "T@\"NSData\",R,C,N,V_bpk"
+ "T@\"NSData\",R,C,N,V_plaintext"
+ "T@\"NSDate\",&,N,V_lastFetchAttempt"
+ "T@\"NSError\",&,N,V_lastFetchError"
+ "T@\"NSMutableArray\",&,N,V_pendingCompletions"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
+ "T@\"NSObject<OS_xpc_object>\",&,N,V_connection"
+ "T@\"NSUUID\",R,C,N,V_homeIdentifier"
+ "TB,N,V_hasFetched"
+ "TB,N,V_isFetching"
+ "TQ,N,V_preferredVariantIndex"
+ "Ti,N,V_notifyToken"
+ "Unable to find class %s"
+ "Unexpected plaintext length"
+ "XPC connection interrupted (auto-recoverable)"
+ "XPC connection invalidated; clearing cache"
+ "XPC reply timeout"
+ "_HMProxBeaconKeyCache"
+ "_bpk"
+ "_decryptAndReportHomeKitAccessoryControlDevice:"
+ "_hasFetched"
+ "_homeIdentifier"
+ "_isFetching"
+ "_keybagItemsFromReply:error:"
+ "_keys"
+ "_lastFetchAttempt"
+ "_lastFetchError"
+ "_lockedEnsureConnection"
+ "_notifyToken"
+ "_parseProximityServiceHomeKitAccessoryControlPtr:end:"
+ "_pendingCompletions"
+ "_plaintext"
+ "_preferredVariantIndex"
+ "_xpcClient"
+ "accessory"
+ "bbb07f3ec1b610c6e72cd1cbb77b3971c9ad7a8c03a609b7d00a1854e9eee042"
+ "bpk"
+ "com.apple.HMProxBeacon"
+ "com.apple.HMProxBeacon.KeyCache"
+ "com.apple.HMProxBeacon.KeybagXPC"
+ "com.apple.HomeKit.proxBeaconKeybagChanged"
+ "com.apple.homed.beacon-keybag"
+ "decrypt"
+ "decryptBeaconPayload:completion:"
+ "decryptBeaconWithKey:nonce:aad:ciphertext:authTag:error:"
+ "failed"
+ "fetchKeybagWithCompletion:"
+ "getKeybag"
+ "hasFetched"
+ "homeID"
+ "homeIdentifier"
+ "initWithHomeIdentifier:bpk:"
+ "initWithPlaintext:"
+ "isFetching"
+ "items"
+ "keybag-xpc"
+ "keys"
+ "lastFetchAttempt"
+ "lastFetchError"
+ "nearbyActionColorCode"
+ "notifyToken"
+ "op"
+ "pendingCompletions"
+ "plaintext"
+ "preferredVariantIndex"
+ "refreshKeysWithCompletion:"
+ "registerForKeybagChangeNotification"
+ "setHasFetched:"
+ "setIsFetching:"
+ "setKeys:"
+ "setLastFetchAttempt:"
+ "setLastFetchError:"
+ "setNotifyToken:"
+ "setPendingCompletions:"
+ "setPreferredVariantIndex:"
+ "setXpcClient:"
+ "sharedCache"
+ "shouldRetryFetch"
+ "softlink:r:path:/System/Library/PrivateFrameworks/CoreHAP.framework/CoreHAP"
+ "v24@?0@\"HMProxBeaconDecryptResult\"8@\"NSError\"16"
+ "xpcClient"
```
