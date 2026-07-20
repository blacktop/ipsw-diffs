## HomeKitMatter

> `/System/Library/PrivateFrameworks/HomeKitMatter.framework/HomeKitMatter`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-1484.2.0.0.0
-  __TEXT.__text: 0x1815cc
+1490.2.0.1.1
+  __TEXT.__text: 0x1813a8
   __TEXT.__objc_methlist: 0xad0c
   __TEXT.__const: 0x298
   __TEXT.__dlopen_cstrs: 0x58
   __TEXT.__gcc_except_tab: 0x302c
-  __TEXT.__cstring: 0x6e9e
-  __TEXT.__oslogstring: 0x4f5a5
+  __TEXT.__cstring: 0x6ed0
+  __TEXT.__oslogstring: 0x4f542
   __TEXT.__ustring: 0x68
-  __TEXT.__unwind_info: 0x3140
+  __TEXT.__unwind_info: 0x3148
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7098
+  __DATA_CONST.__objc_selrefs: 0x7090
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x310
   __DATA_CONST.__objc_arraydata: 0x240
   __DATA_CONST.__got: 0x9f8
   __AUTH_CONST.__const: 0x1140
-  __AUTH_CONST.__cfstring: 0x6ce0
+  __AUTH_CONST.__cfstring: 0x6d20
   __AUTH_CONST.__objc_const: 0x10238
   __AUTH_CONST.__objc_intobj: 0x1740
   __AUTH_CONST.__objc_arrayobj: 0x168

   __DATA.__data: 0xea0
   __DATA.__bss: 0x478
   __DATA_DIRTY.__objc_data: 0xd20
-  __DATA_DIRTY.__bss: 0xd8
+  __DATA_DIRTY.__bss: 0xc0
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 4477
-  Symbols:   10310
+  Symbols:   10306
   CStrings:  5772
 
Symbols:
+ -[HMMTRProtocolMap getCHIPAttributesForCharacteristic:endpointID:clusterIDCharacteristicMap:]
+ _OBJC_CLASS_$_CoreHAPHKDF
+ _logCategory._hmf_once_t208
+ _logCategory._hmf_once_v209
+ _objc_msgSend$getCHIPAttributesForCharacteristic:endpointID:clusterIDCharacteristicMap:
+ _objc_msgSend$hkdfSHA512DeriveKeyFromIKM:salt:info:outputByteCount:error:
- -[HMMTRProtocolMap getCHIPAttributesForCharacteristic:]
- _OBJC_CLASS_$_HAPECDSAKeyPairVerifySession
- __windowBeginSeconds
- __windowBoundariesInitialized
- __windowEndSeconds
- _logCategory._hmf_once_t210
- _logCategory._hmf_once_v211
- _objc_msgSend$bpkFromTLK:error:
- _objc_msgSend$getCHIPAttributesForCharacteristic:
- _objc_msgSend$tlkFromIKM:error:
Functions:
~ +[HMMTRBeaconProtectionKey bpkFromMatterFabricRawIPK:compressedFabricId:error:] : 588 -> 708
~ -[HMMTRDescriptorClusterManager _verifyHAPOptionalCharacteristicSupportAtCHIPEndpoint:device:endpointDeviceTypes:callbackQueue:clusterClassToQueryForAttributes:hapServicesToCheckForOptionalMatterAttribute:clusterAttributesSupported:hapServicesInUse:deviceTopology:bridgeAggregateNodeEndpoint:server:lastError:completionHandler:] : 2828 -> 2824
~ -[HMMTRAnnounceOtaScheduler init:] : 1044 -> 928
~ -[HMMTRAnnounceOtaScheduler _isWithinUpdateTimeWindowForComponents:windowBegin:windowEnd:] : 1216 -> 1088
~ -[HMMTRAnnounceOtaScheduler isWithinUpdateTimeWindow] : 84 -> 168
~ -[HMMTRProtocolMap getCHIPAttributesForCharacteristic:] -> -[HMMTRProtocolMap getCHIPAttributesForCharacteristic:endpointID:clusterIDCharacteristicMap:] : 696 -> 192
CStrings:
+ "HK Matter Privacy v1 BPK"
+ "HK Matter Privacy v1 TLK"
- "Window boundaries not initialized properly"
- "[%{public}@] Window boundaries not initialized properly"
```
