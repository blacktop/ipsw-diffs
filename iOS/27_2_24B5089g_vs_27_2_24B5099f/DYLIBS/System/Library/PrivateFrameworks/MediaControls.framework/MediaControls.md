## MediaControls

> `/System/Library/PrivateFrameworks/MediaControls.framework/MediaControls`

### Sections with Same Size but Changed Content

- `__TEXT.__oslogstring`

```diff

-4026.200.15.0.0
-  __TEXT.__text: 0x218310
-  __TEXT.__objc_methlist: 0x15de4
-  __TEXT.__cstring: 0x6f74
+4026.200.23.0.0
+  __TEXT.__text: 0x218c6c
+  __TEXT.__objc_methlist: 0x15e2c
+  __TEXT.__cstring: 0x6ec4
   __TEXT.__ustring: 0x28
-  __TEXT.__const: 0xbd04
+  __TEXT.__const: 0xbd24
   __TEXT.__gcc_except_tab: 0x1598
   __TEXT.__oslogstring: 0x86d9
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__constg_swiftt: 0x77fc
-  __TEXT.__swift5_typeref: 0x3398
+  __TEXT.__constg_swiftt: 0x7804
+  __TEXT.__swift5_typeref: 0x33aa
   __TEXT.__swift5_reflstr: 0x4bcd
   __TEXT.__swift5_fieldmd: 0x4c14
   __TEXT.__swift5_types: 0x614

   __TEXT.__swift_as_ret: 0x34
   __TEXT.__swift_as_cont: 0x6c
   __TEXT.__swift5_assocty: 0x390
-  __TEXT.__unwind_info: 0xaa18
+  __TEXT.__unwind_info: 0xaa48
   __TEXT.__eh_frame: 0x18b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3090
+  __DATA_CONST.__const: 0x30b8
   __DATA_CONST.__objc_classlist: 0x9b8
   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x480
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa7e8
+  __DATA_CONST.__objc_selrefs: 0xa818
   __DATA_CONST.__objc_protorefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0x608
   __DATA_CONST.__objc_arraydata: 0x1e8
-  __DATA_CONST.__got: 0x18a8
+  __DATA_CONST.__got: 0x18b0
   __AUTH_CONST.__const: 0xab98
   __AUTH_CONST.__cfstring: 0x5200
-  __AUTH_CONST.__objc_const: 0x44848
+  __AUTH_CONST.__objc_const: 0x44878
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__objc_doubleobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x140
-  __AUTH_CONST.__auth_got: 0x2030
-  __AUTH.__objc_data: 0x82a8
+  __AUTH_CONST.__auth_got: 0x2058
+  __AUTH.__objc_data: 0x82b0
   __AUTH.__data: 0x34d8
-  __DATA.__objc_ivar: 0x18d4
-  __DATA.__data: 0x4d68
+  __DATA.__objc_ivar: 0x18d8
+  __DATA.__data: 0x4d98
   __DATA.__common: 0x1250
   __DATA_DIRTY.__objc_data: 0x28a0
   __DATA_DIRTY.__data: 0x5b8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 14463
-  Symbols:   13884
-  CStrings:  1624
+  Functions: 14478
+  Symbols:   13898
+  CStrings:  1620
 
Symbols:
+ -[MRUSpatialAudioController bluetoothQueue]
+ -[MRUSpatialAudioController didRetrievePreferences:forBundleID:]
+ -[MRUSpatialAudioController didSetPreferences:forBundleID:success:]
+ -[MRUSpatialAudioController requestPreferenceForBundleID:outputDevice:]
+ -[MRUSpatialAudioController setBluetoothQueue:]
+ -[MRUSpatialAudioController updateAccessoryStereoHFPStatus:headTrackingAvailable:]
+ _OBJC_IVAR_$_MRUSpatialAudioController._bluetoothQueue
+ ___56-[MRUSpatialAudioController updateHeadTrackingAvailable]_block_invoke
+ ___57-[MRUSpatialAudioController headTrackChangedNotification]_block_invoke
+ ___69-[MRUSpatialAudioController setPreferences:forBundleID:outputDevice:]_block_invoke
+ ___70-[MRUSpatialAudioController accessibilityHeadTrackChangedNotification]_block_invoke
+ ___71-[MRUSpatialAudioController requestPreferenceForBundleID:outputDevice:]_block_invoke
+ ___block_descriptor_57_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ _symbolic Say_____G So6UIViewC5UIKitE14ReservedRegionV12QueryOptionsV
+ _symbolic _____Sg So6UIViewC5UIKitE14ReservedRegionV
- __UISheetContainerInsets
CStrings:
+ "[%s] foldAvoidanceInsets=%s"
+ "com.apple.MediaControls.MRUSpatialAudioController/bluetoothQueue"
- "[%s] _UISheetContainerInsets=%s"
- "cayenne.debugSheetContainerInsets.bottom"
- "cayenne.debugSheetContainerInsets.left"
- "cayenne.debugSheetContainerInsets.right"
- "cayenne.debugSheetContainerInsets.top"
- "cayenne.usesDebugSheetContainerInsets"
```
