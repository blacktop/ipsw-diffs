## HomeKitMatter

> `/System/Library/PrivateFrameworks/HomeKitMatter.framework/Versions/A/HomeKitMatter`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
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
-  __TEXT.__text: 0x1869f0
+1490.2.0.0.0
+  __TEXT.__text: 0x186758
   __TEXT.__objc_methlist: 0xa6ec
   __TEXT.__const: 0x250
   __TEXT.__dlopen_cstrs: 0x58
   __TEXT.__gcc_except_tab: 0x2f44
   __TEXT.__cstring: 0x6924
-  __TEXT.__oslogstring: 0x49912
+  __TEXT.__oslogstring: 0x498af
   __TEXT.__ustring: 0x68
-  __TEXT.__unwind_info: 0x2f70
+  __TEXT.__unwind_info: 0x2f78
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA.__data: 0xe40
   __DATA.__bss: 0x478
   __DATA_DIRTY.__objc_data: 0xc80
-  __DATA_DIRTY.__bss: 0xb8
+  __DATA_DIRTY.__bss: 0xa0
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 4395
-  Symbols:   10048
-  CStrings:  5417
+  Symbols:   10045
+  CStrings:  5415
 
Symbols:
+ -[HMMTRProtocolMap getCHIPAttributesForCharacteristic:endpointID:clusterIDCharacteristicMap:]
+ _objc_msgSend$getCHIPAttributesForCharacteristic:endpointID:clusterIDCharacteristicMap:
+ logCategory._hmf_once_t208
+ logCategory._hmf_once_v209
- -[HMMTRProtocolMap getCHIPAttributesForCharacteristic:]
- __windowBeginSeconds
- __windowBoundariesInitialized
- __windowEndSeconds
- _objc_msgSend$getCHIPAttributesForCharacteristic:
- logCategory._hmf_once_t210
- logCategory._hmf_once_v211
Functions:
~ -[HMMTRDescriptorClusterManager _verifyHAPOptionalCharacteristicSupportAtCHIPEndpoint:device:endpointDeviceTypes:callbackQueue:clusterClassToQueryForAttributes:hapServicesToCheckForOptionalMatterAttribute:clusterAttributesSupported:hapServicesInUse:deviceTopology:bridgeAggregateNodeEndpoint:server:lastError:completionHandler:] : 3068 -> 3104
~ -[HMMTRAnnounceOtaScheduler init:] : 1132 -> 1016
~ -[HMMTRAnnounceOtaScheduler _isWithinUpdateTimeWindowForComponents:windowBegin:windowEnd:] : 1244 -> 1112
~ -[HMMTRAnnounceOtaScheduler isWithinUpdateTimeWindow] : 88 -> 172
~ -[HMMTRProtocolMap getCHIPAttributesForCharacteristic:] -> -[HMMTRProtocolMap getCHIPAttributesForCharacteristic:endpointID:clusterIDCharacteristicMap:] : 756 -> 220
CStrings:
- "Window boundaries not initialized properly"
- "[%{public}@] Window boundaries not initialized properly"
```
