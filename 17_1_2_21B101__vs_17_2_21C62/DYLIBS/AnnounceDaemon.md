## AnnounceDaemon

> `/System/Library/PrivateFrameworks/AnnounceDaemon.framework/AnnounceDaemon`

```diff

-217.10.3.0.0
-  __TEXT.__text: 0x4de24
-  __TEXT.__auth_stubs: 0xf80
+217.20.3.0.0
+  __TEXT.__text: 0x4e024
+  __TEXT.__auth_stubs: 0xfb0
   __TEXT.__objc_methlist: 0x2e0c
   __TEXT.__const: 0x26c
   __TEXT.__cstring: 0x2558
-  __TEXT.__oslogstring: 0x5743
+  __TEXT.__oslogstring: 0x5824
   __TEXT.__gcc_except_tab: 0xacc
   __TEXT.__swift5_typeref: 0x1eb
   __TEXT.__swift5_capture: 0x54

   __TEXT.__swift5_fieldmd: 0xe4
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_proto: 0xc
-  __TEXT.__unwind_info: 0x1200
+  __TEXT.__unwind_info: 0x120c
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_classname: 0x9d2
   __TEXT.__objc_methname: 0xb45c

   __AUTH_CONST.__objc_const: 0x12e8
   __AUTH_CONST.__cfstring: 0x13a0
   __AUTH_CONST.__objc_intobj: 0x78
-  __AUTH_CONST.__auth_got: 0x7d0
+  __AUTH_CONST.__auth_got: 0x7e8
   __AUTH.__objc_data: 0x598
   __AUTH.__data: 0x68
   __DATA.__objc_protorefs: 0x48

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 42037284-EEB1-3487-94A5-8330CEDC5177
-  Functions: 1460
-  Symbols:   5413
-  CStrings:  3111
+  UUID: F1002147-3967-3CD5-96A6-9B4282A092F6
+  Functions: 1461
+  Symbols:   5418
+  CStrings:  3115
 
Symbols:
+ GCC_except_table46
+ GCC_except_table58
+ GCC_except_table60
+ GCC_except_table70
+ ___34-[ANRapportConnection _setupLink:]_block_invoke.41
+ ___46-[ANRapportConnection _linkForDevice:handler:]_block_invoke.44
+ ___53-[ANRapportConnection _registerMessageRequestHandler]_block_invoke.46
+ ___64-[ANRapportConnection _registerHomeLocationStatusRequestHandler]_block_invoke.50
+ ___block_descriptor_64_e8_32s40bs48bs_e17_v16?0"NSError"8ls40l8s48l8s32l8
+ ___block_literal_global.216
+ _dispatch_block_cancel
+ _dispatch_block_create
+ _dispatch_block_testcancel
- GCC_except_table39
- GCC_except_table45
- GCC_except_table55
- GCC_except_table57
- GCC_except_table59
- GCC_except_table69
- ___46-[ANRapportConnection _linkForDevice:handler:]_block_invoke.43
- ___53-[ANRapportConnection _registerMessageRequestHandler]_block_invoke.45
- ___64-[ANRapportConnection _registerHomeLocationStatusRequestHandler]_block_invoke.49
- ___block_descriptor_56_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
- ___block_literal_global.215
CStrings:
+ "%@### Activation handler already called. Skipping."
+ "%@### Updated Devices (%lu)"
+ "%@Current User Announce Notification Mode: %ld"
+ "%@Current User is not in Home %@ (Current Home Location Status = %ld). Not posting user notification."
+ "%@Override Home Location Status: %ld, Current Home Location Status: %ld, Home: %@"
+ "%@Rapport Link Activated"
+ "%@Tearing Down Companion Link: %@"
+ "Already playing. Current playback state = %{public}lu. Stopping before proceeding."
- "%@### Updated Devices (%@)"
- "%@Current User Announce Notification Mode: %@"
- "%@Current User is not in Home (%@) [%@] (Location Status %@). Not posting user notification. Current Home: (%@) [%@]"
- "%@Override Home Location Status: %ld"

```
