## securityresearchdevice-init

> `/usr/libexec/securityresearchdevice-init`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__TEXT.__cstring`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`

```diff

-274.0.8.0.0
-  __TEXT.__text: 0x1db44
+274.40.9.0.0
+  __TEXT.__text: 0x1fb30
   __TEXT.__auth_stubs: 0x1140
   __TEXT.__objc_stubs: 0x340
-  __TEXT.__const: 0x938
+  __TEXT.__const: 0x9b8
   __TEXT.__swift5_entry: 0x8
   __TEXT.__cstring: 0x6dc
-  __TEXT.__swift_as_entry: 0x94
-  __TEXT.__swift_as_ret: 0xc8
-  __TEXT.__swift_as_cont: 0x178
-  __TEXT.__oslogstring: 0x9bc
-  __TEXT.__swift5_typeref: 0x1a4
-  __TEXT.__constg_swiftt: 0x21c
+  __TEXT.__swift_as_entry: 0xa0
+  __TEXT.__swift_as_ret: 0xdc
+  __TEXT.__swift_as_cont: 0x19c
+  __TEXT.__oslogstring: 0xa2c
+  __TEXT.__swift5_typeref: 0x1cc
+  __TEXT.__constg_swiftt: 0x228
   __TEXT.__swift5_reflstr: 0x554
   __TEXT.__swift5_fieldmd: 0x34c
   __TEXT.__swift5_builtin: 0x8c
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__swift5_capture: 0x44
+  __TEXT.__swift5_capture: 0x54
   __TEXT.__objc_methtype: 0x25
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x2c
   __TEXT.__swift5_types: 0x30
   __TEXT.__objc_classname: 0x2b
   __TEXT.__objc_methname: 0x2a0
-  __TEXT.__unwind_info: 0x850
-  __TEXT.__eh_frame: 0x1dc8
-  __DATA_CONST.__const: 0x588
+  __TEXT.__unwind_info: 0x8d0
+  __TEXT.__eh_frame: 0x2008
+  __DATA_CONST.__const: 0x5b0
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__auth_got: 0x8a8
-  __DATA_CONST.__got: 0x208
-  __DATA_CONST.__auth_ptr: 0x198
+  __DATA_CONST.__got: 0x220
+  __DATA_CONST.__auth_ptr: 0x1b0
   __DATA.__objc_const: 0xb8
   __DATA.__objc_selrefs: 0xd0
-  __DATA.__data: 0x538
+  __DATA.__data: 0x568
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 391
-  Symbols:   389
-  CStrings:  134
+  Functions: 409
+  Symbols:   395
+  CStrings:  135
 
Symbols:
+ _$sScP8rawValues5UInt8Vvg
+ _$sScPMa
+ _$sScS10makeStream2of15bufferingPolicyScSyxG6stream_ScS12ContinuationVyx_G12continuationtxm_AG09BufferingE0Oyx__GtFZ
+ _$sScS12ContinuationV11YieldResultOMn
+ _$sScS12ContinuationV15BufferingPolicyO15bufferingNewestyADyx__GSicAFmlFWC
+ _$sScS12ContinuationV15BufferingPolicyOMn
+ _$sScS12ContinuationV5yieldAB11YieldResultOyyt__GyytRszlF
+ _$sScS12ContinuationVMn
+ _$sScS17makeAsyncIteratorScS0C0Vyx_GyF
+ _$sScS8IteratorV4next9isolationxSgScA_pSgYi_tYaF
+ _$sScS8IteratorV4next9isolationxSgScA_pSgYi_tYaFTu
+ _$sScS8IteratorVMn
+ _$sScT6cancelyyF
+ _$sScTss5NeverORszABRs_rlE11isCancelledSbvgZ
- _$sSo17OS_dispatch_groupC8DispatchE4waityyF
- _dispatch_group_create
- _dispatch_group_enter
- _dispatch_group_leave
- _swift_beginAccess
- _swift_endAccess
- _swift_release_x24
- _swift_retain_x24
CStrings:
+ "Personalize failed on iteration "
+ "device has already been through first unlock"
+ "failed to get lock state, treating as locked: %@"
+ "failed to register for lock status notification, proceeding without waiting"
+ "proceeding while device still appears before first unlock"
- "Personalize failed on iteration: "
- "device appears before first unlock even after notification"
- "failed to get lock state: %@"
- "failed to register for lock status notification"
```
