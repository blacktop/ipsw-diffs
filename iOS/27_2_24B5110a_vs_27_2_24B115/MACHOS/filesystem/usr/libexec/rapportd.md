## rapportd

> `/usr/libexec/rapportd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_acfuncs`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-751.200.92.0.0
-  __TEXT.__text: 0x19d7d0
+751.200.101.0.0
+  __TEXT.__text: 0x19da80
   __TEXT.__auth_stubs: 0x3a50
   __TEXT.__objc_stubs: 0x145c0
   __TEXT.__objc_methlist: 0xae28
   __TEXT.__const: 0x6700
-  __TEXT.__cstring: 0x3e016
+  __TEXT.__cstring: 0x3e426
   __TEXT.__objc_classname: 0x11af
   __TEXT.__objc_methtype: 0x4f81
   __TEXT.__gcc_except_tab: 0x2600
-  __TEXT.__objc_methname: 0x1eac0
+  __TEXT.__objc_methname: 0x1eaf0
   __TEXT.__oslogstring: 0x3682
   __TEXT.__swift5_typeref: 0x17d8
   __TEXT.__swift5_capture: 0xb78

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_acfuncs: 0x104
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x78e0
+  __TEXT.__unwind_info: 0x78e8
   __TEXT.__eh_frame: 0x4c8c
   __DATA_CONST.__const: 0x88a0
-  __DATA_CONST.__cfstring: 0xa400
+  __DATA_CONST.__cfstring: 0xa6a0
   __DATA_CONST.__objc_classlist: 0x3d0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x1a0

   __DATA_CONST.__auth_got: 0x1d38
   __DATA_CONST.__got: 0xad8
   __DATA_CONST.__auth_ptr: 0x670
-  __DATA.__objc_const: 0x12d18
+  __DATA.__objc_const: 0x12d58
   __DATA.__objc_selrefs: 0x6600
-  __DATA.__objc_ivar: 0x1200
+  __DATA.__objc_ivar: 0x1208
   __DATA.__objc_data: 0x2f70
   __DATA.__data: 0x3e18
   __DATA.__common: 0xd0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9008
+  Functions: 9010
   Symbols:   1464
-  CStrings:  11947
+  CStrings:  11971
 
CStrings:
+ "Debouncing stale BLE prune, deferring %.1fs"
+ "_lastBLEStalePruneTime"
+ "_pendingBLEStalePruneTimer"
+ "com.apple.SpeakerGroupSetup.calibrationConfiguration"
+ "com.apple.SpeakerGroupSetup.client.done"
+ "com.apple.SpeakerGroupSetup.client.invalidated"
+ "com.apple.SpeakerGroupSetup.done"
+ "com.apple.SpeakerGroupSetup.highlightPing"
+ "com.apple.SpeakerGroupSetup.ping"
+ "com.apple.SpeakerGroupSetup.playCelebration"
+ "com.apple.SpeakerGroupSetup.startScene"
+ "com.apple.SpeakerGroupSetup.stop"
+ "com.apple.SpeakerGroupSetup.stopScene"
+ "com.apple.audio.acousticcalibrationd.NetworkInterfaceRequest"
+ "com.apple.audio.acousticcalibrationd.StopSceneRequest"
+ "com.apple.audio.acousticcalibrationd.StopSessionRequest"
+ "com.apple.audio.acousticcalibrationd.collectCapturesRequest"
+ "com.apple.audio.acousticcalibrationd.derivedDataRequest"
+ "com.apple.audio.acousticcalibrationd.performTimeSyncRequest"
+ "com.apple.audio.acousticcalibrationd.prepareParticipantRequest"
+ "com.apple.audio.acousticcalibrationd.scheduleCalibrationRequest"
+ "com.apple.audio.acousticcalibrationd.setRolesRequest"
+ "requestSetupStateFromSurroundCompanions"
+ "synchSetupStateFromSurroundCompanions"
```
