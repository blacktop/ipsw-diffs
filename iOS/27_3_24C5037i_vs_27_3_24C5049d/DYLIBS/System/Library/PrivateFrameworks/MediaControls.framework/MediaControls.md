## MediaControls

> `/System/Library/PrivateFrameworks/MediaControls.framework/MediaControls`

```diff

-4026.300.11.0.0
-  __TEXT.__text: 0x21c278
-  __TEXT.__objc_methlist: 0x15f0c
-  __TEXT.__cstring: 0x6fa4
+4026.310.18.1.0
+  __TEXT.__text: 0x21df30
+  __TEXT.__objc_methlist: 0x1604c
+  __TEXT.__cstring: 0x6ff4
   __TEXT.__ustring: 0x28
   __TEXT.__const: 0xbdc4
   __TEXT.__gcc_except_tab: 0x15d8

   __TEXT.__dlopen_cstrs: 0x64
   __TEXT.__constg_swiftt: 0x78c0
   __TEXT.__swift5_typeref: 0x341a
-  __TEXT.__swift5_reflstr: 0x4c8d
-  __TEXT.__swift5_fieldmd: 0x4c84
+  __TEXT.__swift5_reflstr: 0x4cad
+  __TEXT.__swift5_fieldmd: 0x4c9c
   __TEXT.__swift5_types: 0x614
   __TEXT.__swift5_capture: 0x1500
   __TEXT.__swift5_protos: 0xb8

   __TEXT.__swift_as_ret: 0x3c
   __TEXT.__swift_as_cont: 0x7c
   __TEXT.__swift5_assocty: 0x390
-  __TEXT.__unwind_info: 0xab00
+  __TEXT.__unwind_info: 0xab50
   __TEXT.__eh_frame: 0x1a08
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x30b8
-  __DATA_CONST.__objc_classlist: 0x9b8
+  __DATA_CONST.__const: 0x3158
+  __DATA_CONST.__objc_classlist: 0x9c8
   __DATA_CONST.__objc_catlist: 0xa8
-  __DATA_CONST.__objc_protolist: 0x480
+  __DATA_CONST.__objc_protolist: 0x488
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa8d8
+  __DATA_CONST.__objc_selrefs: 0xa968
   __DATA_CONST.__objc_protorefs: 0xa8
-  __DATA_CONST.__objc_superrefs: 0x608
+  __DATA_CONST.__objc_superrefs: 0x618
   __DATA_CONST.__objc_arraydata: 0x1e8
-  __DATA_CONST.__got: 0x18e0
-  __AUTH_CONST.__const: 0xad00
-  __AUTH_CONST.__cfstring: 0x5280
-  __AUTH_CONST.__objc_const: 0x44b38
+  __DATA_CONST.__got: 0x18e8
+  __AUTH_CONST.__const: 0xad08
+  __AUTH_CONST.__cfstring: 0x52a0
+  __AUTH_CONST.__objc_const: 0x44df0
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__objc_doubleobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__auth_got: 0x2108
-  __AUTH.__objc_data: 0x8300
+  __AUTH.__objc_data: 0x83a0
   __AUTH.__data: 0x34d8
-  __DATA.__objc_ivar: 0x18e4
-  __DATA.__data: 0x4e08
-  __DATA.__common: 0x1260
+  __DATA.__objc_ivar: 0x1900
+  __DATA.__data: 0x4e68
+  __DATA.__common: 0x1280
   __DATA_DIRTY.__objc_data: 0x2908
   __DATA_DIRTY.__data: 0x5c8
   __DATA_DIRTY.__bss: 0x3f0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 14533
-  Symbols:   13931
-  CStrings:  1632
+  Functions: 14565
+  Symbols:   13989
+  CStrings:  1634
 
Symbols:
+ -[MRUDevicePropertyCacheItem headTrackingAvailable]
+ -[MRUDevicePropertyCacheItem initWithStereoHFPStatus:headTrackingAvailable:]
+ -[MRUDevicePropertyCacheItem setHeadTrackingAvailable:]
+ -[MRUDevicePropertyCacheItem setStereoHFPStatus:]
+ -[MRUDevicePropertyCacheItem stereoHFPStatus]
+ -[MRUSpatialAudioController invalidate]
+ -[MRUSpatialAudioController preferencesController]
+ -[MRUSpatialAudioController setPreferencesController:]
+ -[MRUSpatialAudioController spatialAudioPreferencesControllerDidUpdateCache:]
+ -[MRUSpatialAudioMode hash]
+ -[MRUSpatialAudioPreferencesController .cxx_destruct]
+ -[MRUSpatialAudioPreferencesController bluetoothQueue]
+ -[MRUSpatialAudioPreferencesController cacheGeneration]
+ -[MRUSpatialAudioPreferencesController delegate]
+ -[MRUSpatialAudioPreferencesController deviceCache]
+ -[MRUSpatialAudioPreferencesController finishRefreshWithKey:generation:preferences:bundleID:deviceProperties:uid:]
+ -[MRUSpatialAudioPreferencesController headTrackingAvailableForOutputDevice:]
+ -[MRUSpatialAudioPreferencesController init]
+ -[MRUSpatialAudioPreferencesController invalidateCache]
+ -[MRUSpatialAudioPreferencesController pendingRefreshKeys]
+ -[MRUSpatialAudioPreferencesController preferencesCache]
+ -[MRUSpatialAudioPreferencesController preferencesForBundleID:outputDevice:]
+ -[MRUSpatialAudioPreferencesController refreshCacheForBundleID:uid:]
+ -[MRUSpatialAudioPreferencesController setBluetoothQueue:]
+ -[MRUSpatialAudioPreferencesController setCacheGeneration:]
+ -[MRUSpatialAudioPreferencesController setDelegate:]
+ -[MRUSpatialAudioPreferencesController setDeviceCache:]
+ -[MRUSpatialAudioPreferencesController setPendingRefreshKeys:]
+ -[MRUSpatialAudioPreferencesController setPreferences:forBundleID:outputDevice:]
+ -[MRUSpatialAudioPreferencesController setPreferencesCache:]
+ -[MRUSpatialAudioPreferencesController stereoHFPStatusForOutputDevice:]
+ -[MRUTransportButton dimsInAlwaysOn]
+ -[MRUTransportButton setDimsInAlwaysOn:]
+ _MRUActivityNowPlayingCompactArtworkLengthForSlotArrangement
+ _MRUActivityNowPlayingSlotArrangementForSlots
+ _OBJC_CLASS_$_MRUDevicePropertyCacheItem
+ _OBJC_CLASS_$_MRUSpatialAudioPreferencesController
+ _OBJC_IVAR_$_MRUDevicePropertyCacheItem._headTrackingAvailable
+ _OBJC_IVAR_$_MRUDevicePropertyCacheItem._stereoHFPStatus
+ _OBJC_IVAR_$_MRUSpatialAudioController._preferencesController
+ _OBJC_IVAR_$_MRUSpatialAudioPreferencesController._bluetoothQueue
+ _OBJC_IVAR_$_MRUSpatialAudioPreferencesController._cacheGeneration
+ _OBJC_IVAR_$_MRUSpatialAudioPreferencesController._delegate
+ _OBJC_IVAR_$_MRUSpatialAudioPreferencesController._deviceCache
+ _OBJC_IVAR_$_MRUSpatialAudioPreferencesController._pendingRefreshKeys
+ _OBJC_IVAR_$_MRUSpatialAudioPreferencesController._preferencesCache
+ _OBJC_IVAR_$_MRUTransportButton._dimsInAlwaysOn
+ _OBJC_METACLASS_$_MRUDevicePropertyCacheItem
+ _OBJC_METACLASS_$_MRUSpatialAudioPreferencesController
+ __OBJC_$_INSTANCE_METHODS_MRUDevicePropertyCacheItem
+ __OBJC_$_INSTANCE_METHODS_MRUSpatialAudioPreferencesController
+ __OBJC_$_INSTANCE_VARIABLES_MRUDevicePropertyCacheItem
+ __OBJC_$_INSTANCE_VARIABLES_MRUSpatialAudioPreferencesController
+ __OBJC_$_PROP_LIST_MRUDevicePropertyCacheItem
+ __OBJC_$_PROP_LIST_MRUSpatialAudioPreferencesController
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MRUSpatialAudioPreferencesControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MRUSpatialAudioPreferencesControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_MRUSpatialAudioPreferencesControllerDelegate
+ __OBJC_CLASS_RO_$_MRUDevicePropertyCacheItem
+ __OBJC_CLASS_RO_$_MRUSpatialAudioPreferencesController
+ __OBJC_LABEL_PROTOCOL_$_MRUSpatialAudioPreferencesControllerDelegate
+ __OBJC_METACLASS_RO_$_MRUDevicePropertyCacheItem
+ __OBJC_METACLASS_RO_$_MRUSpatialAudioPreferencesController
+ __OBJC_PROTOCOL_$_MRUSpatialAudioPreferencesControllerDelegate
+ ___68-[MRUSpatialAudioPreferencesController refreshCacheForBundleID:uid:]_block_invoke
+ ___80-[MRUSpatialAudioPreferencesController setPreferences:forBundleID:outputDevice:]_block_invoke
+ ___block_descriptor_72_e8_32s40s48s56w_e5_v8?0ls32l8s40l8w56l8s48l8
+ ___block_descriptor_73_e8_32s40s48s56w_e5_v8?0lw56l8s32l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s64w_e5_v8?0ls32l8s40l8s48l8w64l8s56l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72w_e5_v8?0lw72l8s32l8s40l8s48l8s56l8s64l8
+ ___swift_memcpy168_8
+ ___swift_memcpy72_8
- -[MRUSpatialAudioController accessibilityHeadTrackChangedNotification]
- -[MRUSpatialAudioController accessoryStereoHFPStatus]
- -[MRUSpatialAudioController cache]
- -[MRUSpatialAudioController isHeadTrackingAvailable]
- -[MRUSpatialAudioController preferenceForBundleID:outputDevice:]
- -[MRUSpatialAudioController setAccessoryStereoHFPStatus:]
- -[MRUSpatialAudioController setCache:]
- -[MRUSpatialAudioController setIsHeadTrackingAvailable:]
- -[MRUSpatialAudioController setPreferences:forBundleID:outputDevice:]
- -[MRUSpatialAudioController updateHeadTrackingAvailable]
- _OBJC_IVAR_$_MRUSpatialAudioController._accessoryStereoHFPStatus
- _OBJC_IVAR_$_MRUSpatialAudioController._cache
- _OBJC_IVAR_$_MRUSpatialAudioController._isHeadTrackingAvailable
- ___swift_memcpy136_8
CStrings:
+ "%@/%@"
+ "com.apple.MediaControls.MRUSpatialAudioPreferencesController/bluetoothQueue"
```
