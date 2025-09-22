## MicroLocationDaemon

> `/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`

```diff

-28.0.15.0.0
-  __TEXT.__text: 0x225408
+31.0.2.0.0
+  __TEXT.__text: 0x225d80
   __TEXT.__auth_stubs: 0x2a00
-  __TEXT.__objc_methlist: 0x5ed8
+  __TEXT.__objc_methlist: 0x5f28
   __TEXT.__const: 0xc246
-  __TEXT.__gcc_except_tab: 0x27e7c
-  __TEXT.__cstring: 0x1192c
-  __TEXT.__oslogstring: 0x2a289
+  __TEXT.__gcc_except_tab: 0x27e70
+  __TEXT.__cstring: 0x1191c
+  __TEXT.__oslogstring: 0x2a459
   __TEXT.__constg_swiftt: 0xe84
   __TEXT.__swift5_typeref: 0xd92
   __TEXT.__swift5_builtin: 0xc8

   __TEXT.__swift5_capture: 0x244
   __TEXT.__swift_as_entry: 0x34
   __TEXT.__swift_as_ret: 0x28
-  __TEXT.__unwind_info: 0xc780
+  __TEXT.__unwind_info: 0xc7d0
   __TEXT.__eh_frame: 0xfa4
   __TEXT.__objc_classname: 0xf2c
-  __TEXT.__objc_methname: 0xe8a5
-  __TEXT.__objc_methtype: 0xdaed
-  __TEXT.__objc_stubs: 0xb9a0
-  __DATA_CONST.__got: 0x8b8
+  __TEXT.__objc_methname: 0xe90b
+  __TEXT.__objc_methtype: 0xdb7d
+  __TEXT.__objc_stubs: 0xba00
+  __DATA_CONST.__got: 0x8b0
   __DATA_CONST.__const: 0x18c8
   __DATA_CONST.__objc_classlist: 0x548
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3630
+  __DATA_CONST.__objc_selrefs: 0x3648
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0x1d8
+  __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0xba0
   __AUTH_CONST.__auth_got: 0x1518
-  __AUTH_CONST.__const: 0xc258
-  __AUTH_CONST.__cfstring: 0x4fe0
-  __AUTH_CONST.__objc_const: 0xbcd0
-  __AUTH_CONST.__objc_intobj: 0x17d0
-  __AUTH_CONST.__objc_doubleobj: 0x8a0
+  __AUTH_CONST.__const: 0xc278
+  __AUTH_CONST.__cfstring: 0x4f80
+  __AUTH_CONST.__objc_const: 0xbd18
+  __AUTH_CONST.__objc_intobj: 0x17e8
+  __AUTH_CONST.__objc_doubleobj: 0x8b0
   __AUTH_CONST.__objc_dictobj: 0x8c0
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH.__objc_data: 0xf08
   __AUTH.__data: 0x6b0
-  __DATA.__objc_ivar: 0x3f0
+  __DATA.__objc_ivar: 0x3f8
   __DATA.__data: 0xdb8
   __DATA.__common: 0x68
-  __DATA.__bss: 0x10b0
+  __DATA.__bss: 0x10c0
   __DATA_DIRTY.__objc_data: 0x2c58
   __DATA_DIRTY.__data: 0x6f0
   __DATA_DIRTY.__bss: 0xdb0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: DC2A32A9-60C9-3192-A5E0-7603554EF08B
-  Functions: 9534
-  Symbols:   30145
-  CStrings:  7565
+  UUID: 77E63A87-1D32-3877-B3CA-A15E6051B7EF
+  Functions: 9549
+  Symbols:   30195
+  CStrings:  7573
 
Symbols:
+ +[ULOdometryStore bufferMaxSize]
+ -[ULOdometryStore .cxx_construct]
+ -[ULOdometryStore .cxx_destruct]
+ -[ULOdometryStore deleteRecordsOlderThan:orNewerThan:]
+ -[ULOdometryStore flushStoreBuffer]
+ -[ULOdometryStore flushStoreBuffer].cold.1
+ -[ULOdometryStore initWithDbStore:]
+ -[ULOdometryStore insertDataObjectsBuffered:atLoiUUID:]
+ _OBJC_IVAR_$_ULOdometryStore._currentLoiUUID
+ _OBJC_IVAR_$_ULOdometryStore._dataObjectBuffer
+ __OBJC_$_INSTANCE_VARIABLES_ULOdometryStore
+ __ZN25CLMicroLocationLoiManager18handleGeofenceListEP7NSArrayIP23CLMicroLocationGeofenceE16ULLoiBridgeError
+ __ZN25CLMicroLocationLoiManager20handleLocationUpdateEP10CLLocation16ULLoiBridgeError
+ __ZN25CLMicroLocationLoiManager20handleLocationUpdateEP10CLLocation16ULLoiBridgeError.cold.1
+ __ZN25CLMicroLocationLoiManager20handleLocationUpdateEP10CLLocation16ULLoiBridgeError.cold.2
+ __ZN25CLMicroLocationLoiManager20handleLocationUpdateEP10CLLocation16ULLoiBridgeError.cold.3
+ __ZN25CLMicroLocationLoiManager23didRemoveGeofenceWithIdEP8NSString16ULLoiBridgeError
+ __ZN25CLMicroLocationLoiManager23didRemoveGeofenceWithIdEP8NSString16ULLoiBridgeError.cold.1
+ __ZN25CLMicroLocationLoiManager23didRemoveGeofenceWithIdEP8NSString16ULLoiBridgeError.cold.2
+ __ZN25CLMicroLocationLoiManager23didRemoveGeofenceWithIdEP8NSString16ULLoiBridgeError.cold.3
+ __ZN25CLMicroLocationLoiManager23handleRelatedLoisForLoiEP7NSArray16ULLoiBridgeError
+ __ZN25CLMicroLocationLoiManager23handleRelatedLoisForLoiEP7NSArray16ULLoiBridgeError.cold.1
+ __ZN25CLMicroLocationLoiManager23handleRelatedLoisForLoiEP7NSArray16ULLoiBridgeError.cold.2
+ __ZN25CLMicroLocationLoiManager28handleFetchedPlaceInferencesEP7NSArrayIP17_CLPlaceInferenceE16ULLoiBridgeError
+ __ZN25CLMicroLocationLoiManager28handleFetchedPlaceInferencesEP7NSArrayIP17_CLPlaceInferenceE16ULLoiBridgeError.cold.1
+ __ZN25CLMicroLocationLoiManager28handleFetchedPlaceInferencesEP7NSArrayIP17_CLPlaceInferenceE16ULLoiBridgeError.cold.2
+ __ZN25CLMicroLocationLoiManager28handleFetchedPlaceInferencesEP7NSArrayIP17_CLPlaceInferenceE16ULLoiBridgeError.cold.3
+ __ZN25CLMicroLocationLoiManager28handleFetchedPlaceInferencesEP7NSArrayIP17_CLPlaceInferenceE16ULLoiBridgeError.cold.4
+ __ZN25CLMicroLocationLoiManager36didCompleteSettingGeofenceAtLocationEP10CLLocationN5boost5uuids4uuidE16ULLoiBridgeError
+ __ZN25CLMicroLocationLoiManager36didCompleteSettingGeofenceAtLocationEP10CLLocationN5boost5uuids4uuidE16ULLoiBridgeError.cold.1
+ __ZN25CLMicroLocationLoiManager36didCompleteSettingGeofenceAtLocationEP10CLLocationN5boost5uuids4uuidE16ULLoiBridgeError.cold.2
+ __ZN25CLMicroLocationLoiManager41handleFetchedLocationOfInterestAtLocationEP18CLMicroLocationLoiP10CLLocation16ULLoiBridgeError
+ __ZN25CLMicroLocationLoiManager41handleFetchedLocationOfInterestAtLocationEP18CLMicroLocationLoiP10CLLocation16ULLoiBridgeError.cold.1
+ __ZNKSt3__111__copy_implclB8ne200100IPK12ULOdometryDOS4_PS2_EENS_4pairIT_T1_EES7_T0_S8_
+ __ZNKSt3__120__move_backward_implINS_17_ClassicAlgPolicyEEclB8ne200100IP12ULOdometryDOS5_S5_EENS_4pairIT_T1_EES7_T0_S8_
+ __ZNSt3__114__split_bufferI12ULOdometryDORNS_9allocatorIS1_EEE28__construct_at_end_with_sizeINS_11__wrap_iterIPKS1_EEEEvT_m
+ __ZNSt3__16vectorI12ULOdometryDONS_9allocatorIS1_EEE12__move_rangeEPS1_S5_S5_
+ __ZNSt3__16vectorI12ULOdometryDONS_9allocatorIS1_EEE18__insert_with_sizeB8ne200100INS_11__wrap_iterIPKS1_EES9_EENS6_IPS1_EES9_T_T0_l
+ __ZNSt3__16vectorI12ULOdometryDONS_9allocatorIS1_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS1_RS3_EEPS1_
+ __ZThn8_N25CLMicroLocationLoiManager18handleGeofenceListEP7NSArrayIP23CLMicroLocationGeofenceE16ULLoiBridgeError
+ __ZThn8_N25CLMicroLocationLoiManager20handleLocationUpdateEP10CLLocation16ULLoiBridgeError
+ __ZThn8_N25CLMicroLocationLoiManager23didRemoveGeofenceWithIdEP8NSString16ULLoiBridgeError
+ __ZThn8_N25CLMicroLocationLoiManager23handleRelatedLoisForLoiEP7NSArray16ULLoiBridgeError
+ __ZThn8_N25CLMicroLocationLoiManager28handleFetchedPlaceInferencesEP7NSArrayIP17_CLPlaceInferenceE16ULLoiBridgeError
+ __ZThn8_N25CLMicroLocationLoiManager36didCompleteSettingGeofenceAtLocationEP10CLLocationN5boost5uuids4uuidE16ULLoiBridgeError
+ __ZThn8_N25CLMicroLocationLoiManager41handleFetchedLocationOfInterestAtLocationEP18CLMicroLocationLoiP10CLLocation16ULLoiBridgeError
+ ___51-[CLMicroLocationLoiBridge fetchRelatedLoisForLoi:]_block_invoke_3.cold.2
+ ___56-[ULPersistenceStore _getVersionNumberFromModelVersion:]_block_invoke
+ ___56-[ULPersistenceStore _getVersionNumberFromModelVersion:]_block_invoke.cold.1
+ ___62-[CLMicroLocationLoiBridge fetchLocationOfInterestAtLocation:]_block_invoke_3.cold.1
+ ___75-[CLMicroLocationLoiBridge fetchPlaceInferenceAtCurrentLocationWithPolicy:]_block_invoke_2.cold.3
+ ___block_descriptor_72_ea8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_literal_global.74
+ __getVersionNumberFromModelVersion:.onceToken
+ __getVersionNumberFromModelVersion:.versionRegex
+ _objc_msgSend$bufferMaxSize
+ _objc_msgSend$flushStoreBuffer
+ _objc_msgSend$insertDataObjectsBuffered:atLoiUUID:
- GCC_except_table343
- __ZN25CLMicroLocationLoiManager18handleGeofenceListEP7NSArrayIP23CLMicroLocationGeofenceEP7NSError
- __ZN25CLMicroLocationLoiManager20handleLocationUpdateEP10CLLocationP7NSError
- __ZN25CLMicroLocationLoiManager20handleLocationUpdateEP10CLLocationP7NSError.cold.1
- __ZN25CLMicroLocationLoiManager20handleLocationUpdateEP10CLLocationP7NSError.cold.2
- __ZN25CLMicroLocationLoiManager20handleLocationUpdateEP10CLLocationP7NSError.cold.3
- __ZN25CLMicroLocationLoiManager23didRemoveGeofenceWithIdEP8NSStringP7NSError
- __ZN25CLMicroLocationLoiManager23didRemoveGeofenceWithIdEP8NSStringP7NSError.cold.1
- __ZN25CLMicroLocationLoiManager23didRemoveGeofenceWithIdEP8NSStringP7NSError.cold.2
- __ZN25CLMicroLocationLoiManager23didRemoveGeofenceWithIdEP8NSStringP7NSError.cold.3
- __ZN25CLMicroLocationLoiManager23handleRelatedLoisForLoiEP7NSArrayP7NSError
- __ZN25CLMicroLocationLoiManager23handleRelatedLoisForLoiEP7NSArrayP7NSError.cold.1
- __ZN25CLMicroLocationLoiManager23handleRelatedLoisForLoiEP7NSArrayP7NSError.cold.2
- __ZN25CLMicroLocationLoiManager28handleFetchedPlaceInferencesEP7NSArrayIP17_CLPlaceInferenceEP7NSError
- __ZN25CLMicroLocationLoiManager28handleFetchedPlaceInferencesEP7NSArrayIP17_CLPlaceInferenceEP7NSError.cold.1
- __ZN25CLMicroLocationLoiManager28handleFetchedPlaceInferencesEP7NSArrayIP17_CLPlaceInferenceEP7NSError.cold.2
- __ZN25CLMicroLocationLoiManager28handleFetchedPlaceInferencesEP7NSArrayIP17_CLPlaceInferenceEP7NSError.cold.3
- __ZN25CLMicroLocationLoiManager28handleFetchedPlaceInferencesEP7NSArrayIP17_CLPlaceInferenceEP7NSError.cold.4
- __ZN25CLMicroLocationLoiManager36didCompleteSettingGeofenceAtLocationEP10CLLocationN5boost5uuids4uuidEP7NSError
- __ZN25CLMicroLocationLoiManager36didCompleteSettingGeofenceAtLocationEP10CLLocationN5boost5uuids4uuidEP7NSError.cold.1
- __ZN25CLMicroLocationLoiManager36didCompleteSettingGeofenceAtLocationEP10CLLocationN5boost5uuids4uuidEP7NSError.cold.2
- __ZN25CLMicroLocationLoiManager41handleFetchedLocationOfInterestAtLocationEP18CLMicroLocationLoiP10CLLocationP7NSError
- __ZN25CLMicroLocationLoiManager41handleFetchedLocationOfInterestAtLocationEP18CLMicroLocationLoiP10CLLocationP7NSError.cold.1
- __ZThn8_N25CLMicroLocationLoiManager18handleGeofenceListEP7NSArrayIP23CLMicroLocationGeofenceEP7NSError
- __ZThn8_N25CLMicroLocationLoiManager20handleLocationUpdateEP10CLLocationP7NSError
- __ZThn8_N25CLMicroLocationLoiManager23didRemoveGeofenceWithIdEP8NSStringP7NSError
- __ZThn8_N25CLMicroLocationLoiManager23handleRelatedLoisForLoiEP7NSArrayP7NSError
- __ZThn8_N25CLMicroLocationLoiManager28handleFetchedPlaceInferencesEP7NSArrayIP17_CLPlaceInferenceEP7NSError
- __ZThn8_N25CLMicroLocationLoiManager36didCompleteSettingGeofenceAtLocationEP10CLLocationN5boost5uuids4uuidEP7NSError
- __ZThn8_N25CLMicroLocationLoiManager41handleFetchedLocationOfInterestAtLocationEP18CLMicroLocationLoiP10CLLocationP7NSError
- ___block_descriptor_72_ea8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
- _kCLErrorDomainPrivate
CStrings:
+ "#Warning LOI Manager, Error retrieving the current LOI. Error code: %d"
+ "/AppleInternal/Library/BuildRoots/4~B9_yugBPwIQoWNqMjKqYSKIxaRarLRoPLYYgAYQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/boost/uuid/detail/random_provider_posix.ipp"
+ "/AppleInternal/Library/BuildRoots/4~B9_yugBPwIQoWNqMjKqYSKIxaRarLRoPLYYgAYQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
+ "/AppleInternal/Library/BuildRoots/4~B9_yugBPwIQoWNqMjKqYSKIxaRarLRoPLYYgAYQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "ULDatabaseMaintenanceKeepPercentage"
+ "ULOdometryBufferMaxSize"
+ "ULOdometryBufferingEnabled"
+ "ULOdometryStore: flushing %zu buffered odometry entries"
+ "_currentLoiUUID"
+ "_dataObjectBuffer"
+ "bufferMaxSize"
+ "flushStoreBuffer"
+ "insertDataObjectsBuffered:atLoiUUID:"
+ "{\"msg%{public}.0s\":\"#LOI Manager, Failed to RemoveGeofence\", \"regionId\":%{private, location:escape_only}@, \"error code\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#LOI Manager, didRemoveGeofenceWithId\", \"regionId\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#LOI Manager, failed to get current location to enable MiLo\", \"Error code\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#LOI Manager, failed to set geofence at current location to enable MiLo\", \"Error code\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#Warning LOI Manager, Error retrieving related LOIs for Loi\", \"error code\":%{private}d}"
+ "{\"msg%{public}.0s\":\"LOI Bridge, Failed To fetch place inferences\", \"Error code:\":%{private}d}"
+ "{\"msg%{public}.0s\":\"error creating regex\", \"error domain\":%{private, location:escape_only}@, \"error code\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"fetchLocationOfInterestAtLocation, failed with error\", \"error_domain\":%{private, location:escape_only}s, \"error_code\":%{private}d}"
+ "{\"msg%{public}.0s\":\"fetchPlaceInferenceAtCurrentLocation, failed to request place inference with error\", \"error_domain\":%{private, location:escape_only}s, \"error_code\":%{private}d}"
+ "{\"msg%{public}.0s\":\"fetchRelatedLoisForLoi, failed with error\", \"error_domain\":%{private, location:escape_only}s, \"error_code\":%{private}d}"
+ "{uuid=\"data\"[16C]}"
+ "{vector<ULOdometryDO, std::allocator<ULOdometryDO>>=\"__begin_\"^{ULOdometryDO}\"__end_\"^{ULOdometryDO}\"__cap_\"^{ULOdometryDO}}"
- "#Warning LOI Manager, Error retrieving the current LOI. %{private}s"
- "/AppleInternal/Library/BuildRoots/4~B6tNugCrdi9LcrgNkFqNsTuNURAg6rOSI9pDJfk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/boost/uuid/detail/random_provider_posix.ipp"
- "/AppleInternal/Library/BuildRoots/4~B6tNugCrdi9LcrgNkFqNsTuNURAg6rOSI9pDJfk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
- "/AppleInternal/Library/BuildRoots/4~B6tNugCrdi9LcrgNkFqNsTuNURAg6rOSI9pDJfk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "Location Manager not available"
- "Request to fetch place inference timed out"
- "Routine Monitor is not active"
- "{\"msg%{public}.0s\":\"#LOI Manager, Failed to RemoveGeofence\", \"regionId\":%{private, location:escape_only}@, \"error\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#LOI Manager, didRemoveGeofenceWithId\", \"regionId\":%{private, location:escape_only}@, \"error\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#LOI Manager, failed to get current location to enable MiLo\", \"Error\":%{public, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#LOI Manager, failed to set geofence at current location to enable MiLo\", \"Error\":%{public, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#Warning LOI Manager, Error retrieving related LOIs for Loi\", \"error\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"LOI Bridge, Failed To fetch place inferences\", \"Error:\":%{private, location:escape_only}s}"
- "{\"msg%{public}.0s\":\"error creating regex\", \"error\":%{private, location:escape_only}@}"

```
