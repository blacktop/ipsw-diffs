## AXHapticMusicServer

> `/System/Library/AccessibilityBundles/AXHapticMusicServer.axuiservice/AXHapticMusicServer`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__auth_ptr`

```diff

-3245.8.4.2.0
-  __TEXT.__text: 0x2b0a4
-  __TEXT.__auth_stubs: 0x10f0
-  __TEXT.__objc_stubs: 0xb40
+3245.8.9.0.0
+  __TEXT.__text: 0x2bc28
+  __TEXT.__auth_stubs: 0x10e0
+  __TEXT.__objc_stubs: 0xb00
   __TEXT.__objc_methlist: 0x3fc
   __TEXT.__dlopen_cstrs: 0x68
-  __TEXT.__const: 0xb30
-  __TEXT.__cstring: 0x5eb
-  __TEXT.__swift5_typeref: 0x625
-  __TEXT.__oslogstring: 0x13e8
-  __TEXT.__swift5_capture: 0x778
-  __TEXT.__objc_methtype: 0x5b5
-  __TEXT.__objc_methname: 0x153d
+  __TEXT.__const: 0xb20
+  __TEXT.__cstring: 0x61b
+  __TEXT.__swift5_typeref: 0x675
+  __TEXT.__oslogstring: 0x14f8
+  __TEXT.__swift5_capture: 0x7fc
+  __TEXT.__objc_methtype: 0x5b2
+  __TEXT.__objc_methname: 0x157d
   __TEXT.__objc_classname: 0xef
   __TEXT.__constg_swiftt: 0x224
-  __TEXT.__swift5_reflstr: 0x4b2
-  __TEXT.__swift5_fieldmd: 0x358
+  __TEXT.__swift5_reflstr: 0x512
+  __TEXT.__swift5_fieldmd: 0x37c
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_assocty: 0x90
   __TEXT.__swift5_proto: 0x6c

   __TEXT.__swift_as_ret: 0x1c
   __TEXT.__swift_as_cont: 0x54
   __TEXT.__gcc_except_tab: 0x4c
-  __TEXT.__unwind_info: 0x768
+  __TEXT.__unwind_info: 0x780
   __TEXT.__eh_frame: 0x530
-  __DATA_CONST.__const: 0x1c98
+  __DATA_CONST.__const: 0x1db0
   __DATA_CONST.__cfstring: 0x80
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__auth_got: 0x888
-  __DATA_CONST.__got: 0x2e0
+  __DATA_CONST.__auth_got: 0x880
+  __DATA_CONST.__got: 0x2d8
   __DATA_CONST.__auth_ptr: 0x180
-  __DATA.__objc_const: 0x9f0
-  __DATA.__objc_selrefs: 0x498
-  __DATA.__objc_data: 0x208
-  __DATA.__data: 0x750
+  __DATA.__objc_const: 0xa50
+  __DATA.__objc_selrefs: 0x488
+  __DATA.__objc_data: 0x220
+  __DATA.__data: 0x770
   __DATA.__common: 0x18
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accessibility.framework/Accessibility

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 675
-  Symbols:   269
-  CStrings:  427
+  Functions: 689
+  Symbols:   267
+  CStrings:  433
 
Symbols:
- _AVAudioSessionInterruptionNotification
- _swift_retain_x23
CStrings:
+ "Already fetching haptic track %s, not loading it again"
+ "Backing off engine creation, last failure "
+ "Checking status of server: Enabled: %{bool}d, active: %{bool}d, session valid: %{bool}d, thermal state: %{bool}d, siri active: %{bool}d, camera active: %{bool}d, engine: %{bool}d, engine running: %{bool}d"
+ "Engine stopped handler called for a stale engine. Ignoring"
+ "EngineCreationRetryInterval"
+ "Started a stale haptic engine, ignoring"
+ "Stopped a stale haptic engine, leaving current engine alone"
+ "Stopping and clearing out haptic engine: %s"
+ "fetchingTrackIdentifier"
+ "lastEngineCreationFailureTime"
- "Checking status of server: Enabled: %{bool}d, active: %{bool}d, session valid: %{bool}d, thermal state: %{bool}d, siri active: %{bool}d, camera active: %{bool}d"
- "Stopping and clearing out haptic engine: %@"
- "removeObserver:name:object:"
- "setAutoShutdownTimeout:"
```
