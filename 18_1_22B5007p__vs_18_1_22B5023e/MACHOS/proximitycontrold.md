## proximitycontrold

> `/usr/libexec/proximitycontrold`

```diff

-208.0.6.0.0
-  __TEXT.__text: 0x1f9094
-  __TEXT.__auth_stubs: 0x2930
+208.10.3.0.0
+  __TEXT.__text: 0x1f6e74
+  __TEXT.__auth_stubs: 0x2910
   __TEXT.__objc_stubs: 0x220
   __TEXT.__objc_methlist: 0x1058
   __TEXT.__objc_classname: 0x470
-  __TEXT.__objc_methname: 0x6417
+  __TEXT.__objc_methname: 0x642f
   __TEXT.__objc_methtype: 0x2bda
-  __TEXT.__const: 0x1b178
-  __TEXT.__cstring: 0x14239
-  __TEXT.__swift5_typeref: 0x10f54
-  __TEXT.__swift5_fieldmd: 0x85b4
+  __TEXT.__const: 0x1b188
+  __TEXT.__cstring: 0x14399
+  __TEXT.__swift5_typeref: 0x10f26
+  __TEXT.__swift5_fieldmd: 0x85c0
   __TEXT.__constg_swiftt: 0xdf48
-  __TEXT.__swift5_reflstr: 0x8423
+  __TEXT.__swift5_reflstr: 0x8433
   __TEXT.__swift5_builtin: 0x424
   __TEXT.__swift5_assocty: 0xc80
   __TEXT.__swift5_protos: 0x328
   __TEXT.__swift5_proto: 0x1908
   __TEXT.__swift5_types: 0x7b8
-  __TEXT.__swift5_capture: 0x3718
+  __TEXT.__swift5_capture: 0x36b0
   __TEXT.__swift5_mpenum: 0xc0
   __TEXT.__info_plist: 0x7a7
-  __TEXT.__unwind_info: 0x6970
-  __TEXT.__eh_frame: 0x4ed0
-  __DATA_CONST.__auth_got: 0x14a0
-  __DATA_CONST.__got: 0xbd8
-  __DATA_CONST.__auth_ptr: 0x2c10
-  __DATA_CONST.__const: 0x16110
-  __DATA_CONST.__cfstring: 0x3e0
+  __TEXT.__unwind_info: 0x6968
+  __TEXT.__eh_frame: 0x4ea8
+  __DATA_CONST.__auth_got: 0x1490
+  __DATA_CONST.__got: 0xbd0
+  __DATA_CONST.__auth_ptr: 0x29d0
+  __DATA_CONST.__const: 0x16060
+  __DATA_CONST.__cfstring: 0x400
   __DATA_CONST.__objc_classlist: 0x368
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x2e8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x178
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0x16930
-  __DATA.__objc_selrefs: 0x1240
+  __DATA.__objc_const: 0x16b40
+  __DATA.__objc_selrefs: 0x1248
   __DATA.__objc_ivar: 0x54
   __DATA.__objc_data: 0x28c8
-  __DATA.__data: 0x14240
+  __DATA.__data: 0x141b0
   __DATA.__bss: 0x28540
   __DATA.__common: 0x500
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10115
-  Symbols:   1271
-  CStrings:  3625
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 10105
+  Symbols:   1275
+  CStrings:  3635
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
- _$s7Combine10PublishersO7FlatMapVMn
- _$s7Combine10PublishersO7FlatMapVy_xq_GAA9PublisherAAMc
- _$s7Combine11SubscribersO6DemandV9unlimitedAEvgZ
- _$s7Combine9PublisherPAAE7flatMap13maxPublishers_AA0F0O04FlatD0Vy_qd_0_xGAA11SubscribersO6DemandV_qd_0_6OutputQzctAOQyd_0_Rsd__AaBRd_0_7FailureQyd_0_ARRtzr0_lF
CStrings:
+ "Activity not local"
+ "Activity not media"
+ "Determined policy for: activity="
+ "Playback state not advancing"
+ "Remote is on a call"
+ "Remote is playing"
+ "Remote playback state unknown and remote not connected - cannot assume not playing"
+ "XPCServer activated"
+ "XPCServer activation failed: "
+ "activateXPCServer()"
+ "destinationOriginExists"
+ "miniBasalt"
- "Determining policy for: activity="
- "activateXPCServer(completion:)"

```
