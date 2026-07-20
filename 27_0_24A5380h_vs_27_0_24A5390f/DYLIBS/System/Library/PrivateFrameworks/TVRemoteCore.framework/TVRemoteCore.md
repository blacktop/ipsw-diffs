## TVRemoteCore

> `/System/Library/PrivateFrameworks/TVRemoteCore.framework/TVRemoteCore`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__objc_data`

```diff

-627.0.14.0.0
-  __TEXT.__text: 0x483e4
-  __TEXT.__objc_methlist: 0x64d0
+627.0.19.0.0
+  __TEXT.__text: 0x487b4
+  __TEXT.__lazy_helpers: 0x580
+  __TEXT.__objc_methlist: 0x64e0
   __TEXT.__const: 0x2a0
-  __TEXT.__oslogstring: 0x6b0e
+  __TEXT.__oslogstring: 0x6b4c
   __TEXT.__cstring: 0x3784
   __TEXT.__gcc_except_tab: 0xafc
-  __TEXT.__unwind_info: 0x1230
+  __TEXT.__unwind_info: 0x1218
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3090
+  __DATA_CONST.__objc_selrefs: 0x3098
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x210
   __DATA_CONST.__objc_arraydata: 0x120
-  __DATA_CONST.__got: 0x4f0
+  __DATA_CONST.__got: 0x470
   __AUTH_CONST.__const: 0x480
   __AUTH_CONST.__cfstring: 0x4aa0
   __AUTH_CONST.__objc_const: 0x9f88
+  __AUTH_CONST.__lazy_load_got: 0x80
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x60

   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1860
   __DATA.__objc_ivar: 0x698
-  __DATA.__data: 0xa30
+  __DATA.__data: 0xa34
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__bss: 0x170
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/Frameworks/HomeKit.framework/HomeKit
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2137
-  Symbols:   4731
-  CStrings:  1300
+  Functions: 2138
+  Symbols:   4768
+  CStrings:  1301
 
Symbols:
+ -[TVRCMatchPointDeviceQuery _cachedHomeInManager:]
+ _HMAccessoryCategoryTypeTelevisionSetTopBox$lazyGOT
+ _HMAccessoryCategoryTypeTelevisionSetTopBox$lazyGOT$loadHelper_x8
+ _HMAccessoryCategoryTypeTelevisionStreamingStick$lazyGOT
+ _HMAccessoryCategoryTypeTelevisionStreamingStick$lazyGOT$loadHelper_x8
+ _HMCharacteristicTypeActive$lazyGOT
+ _HMCharacteristicTypeActive$lazyGOT$loadHelper_x8
+ _HMCharacteristicTypeActiveIdentifier$lazyGOT
+ _HMCharacteristicTypeActiveIdentifier$lazyGOT$loadHelper_x8
+ _HMCharacteristicTypeMute$lazyGOT
+ _HMCharacteristicTypeMute$lazyGOT$loadHelper_x8
+ _HMCharacteristicTypeRemoteKey$lazyGOT
+ _HMCharacteristicTypeRemoteKey$lazyGOT$loadHelper_x8
+ _HMCharacteristicTypeVolume$lazyGOT
+ _HMCharacteristicTypeVolume$lazyGOT$loadHelper_x8
+ _HMCharacteristicTypeVolumeSelector$lazyGOT
+ _HMCharacteristicTypeVolumeSelector$lazyGOT$loadHelper_x8
+ _HMErrorDomain$lazyGOT
+ _HMErrorDomain$lazyGOT$loadHelper_x8
+ _HMServiceTypeSpeaker$lazyGOT
+ _HMServiceTypeSpeaker$lazyGOT$loadHelper_x8
+ _HMServiceTypeTelevision$lazyGOT
+ _HMServiceTypeTelevision$lazyGOT$loadHelper_x8
+ _OBJC_CLASS_$_HMCharacteristicBatchRequest$lazyGOT
+ _OBJC_CLASS_$_HMCharacteristicBatchRequest$lazyGOT$loadHelper_x8
+ _OBJC_CLASS_$_HMCharacteristicReadRequest$lazyGOT
+ _OBJC_CLASS_$_HMCharacteristicReadRequest$lazyGOT$loadHelper_x8
+ _OBJC_CLASS_$_HMCharacteristicWriteRequest$lazyGOT
+ _OBJC_CLASS_$_HMCharacteristicWriteRequest$lazyGOT$loadHelper_x8
+ _OBJC_CLASS_$_HMCharacteristicWriteRequest$lazyGOT$loadHelper_x8$for$-[TVRCHMServiceWrapper _writeRequestForCharacteristic:withValue:]+0
+ _OBJC_CLASS_$_HMHomeManager$lazyGOT
+ _OBJC_CLASS_$_HMHomeManager$lazyGOT$loadHelper_x8
+ _OBJC_CLASS_$_HMMutableHomeManagerConfiguration$lazyGOT
+ _OBJC_CLASS_$_HMMutableHomeManagerConfiguration$lazyGOT$loadHelper_x8
+ __dyld_lazy_load
+ _lazyLoadFlag$HomeKit
+ _objc_msgSend$_cachedHomeInManager:
Functions:
~ -[TVRCMatchPointDeviceQuery stop] : 304 -> 272
~ -[TVRCMatchPointDeviceQuery homeManagerDidUpdateHomes:] : 292 -> 312
~ -[TVRCMatchPointDeviceQuery homeManagerDidUpdateCurrentHome:] : 428 -> 452
+ -[TVRCMatchPointDeviceQuery _cachedHomeInManager:]
~ ___75-[TVRCRPCompanionLinkClientWrapper sendEvent:options:shouldRetry:response:]_block_invoke : 556 -> 608
~ ___82-[TVRCRPCompanionLinkClientWrapper fetchUpNextInfoWithPaginationToken:completion:]_block_invoke : 276 -> 336
~ ___80-[TVRCRPCompanionLinkClientWrapper markAsWatchedWithMediaIdentifier:completion:]_block_invoke : 200 -> 260
~ ___74-[TVRCRPCompanionLinkClientWrapper addItemWithMediaIdentifier:completion:]_block_invoke : 200 -> 260
~ ___77-[TVRCRPCompanionLinkClientWrapper removeItemWithMediaIdentifier:completion:]_block_invoke : 200 -> 260
~ ___56-[TVRCRPCompanionLinkClientWrapper playItem:completion:]_block_invoke : 200 -> 260
~ ___76-[TVRCRPCompanionLinkClientWrapper fetchLaunchableAppsWithRange:completion:]_block_invoke : 204 -> 264
~ ___69-[TVRCRPCompanionLinkClientWrapper launchAppWithBundleID:completion:]_block_invoke : 200 -> 260
CStrings:
+ "Received request response with ID %@, responseKeyCount %lu, keys %@, error %@"
+ "currentHome is nil, reusing cached home: %@"
- "Received request response with ID %@, response %@, error %@"
```
