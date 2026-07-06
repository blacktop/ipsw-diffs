## assessmentagent

> `/usr/libexec/assessmentagent`

```diff

-  __TEXT.__text: 0xb3020
-  __TEXT.__auth_stubs: 0x21f0
-  __TEXT.__objc_stubs: 0x27e0
+  __TEXT.__text: 0xb4ee8
+  __TEXT.__auth_stubs: 0x2210
+  __TEXT.__objc_stubs: 0x2800
   __TEXT.__objc_methlist: 0xfc8
-  __TEXT.__const: 0x8fe8
-  __TEXT.__cstring: 0x35a1
-  __TEXT.__objc_methname: 0x3b29
+  __TEXT.__const: 0x9158
+  __TEXT.__cstring: 0x3691
+  __TEXT.__objc_methname: 0x3b49
   __TEXT.__objc_classname: 0x185f
   __TEXT.__objc_methtype: 0xd03
   __TEXT.__gcc_except_tab: 0x20
-  __TEXT.__swift5_typeref: 0x3e92
+  __TEXT.__swift5_typeref: 0x3e98
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x4ae8
-  __TEXT.__swift5_builtin: 0x1cc
-  __TEXT.__swift5_reflstr: 0x3aed
-  __TEXT.__swift5_fieldmd: 0x3724
+  __TEXT.__constg_swiftt: 0x4b48
+  __TEXT.__swift5_builtin: 0x1e0
+  __TEXT.__swift5_reflstr: 0x3b0d
+  __TEXT.__swift5_fieldmd: 0x3780
   __TEXT.__swift5_assocty: 0x350
-  __TEXT.__swift5_proto: 0x520
-  __TEXT.__swift5_types: 0x380
-  __TEXT.__oslogstring: 0x244b
+  __TEXT.__swift5_proto: 0x528
+  __TEXT.__swift5_types: 0x388
+  __TEXT.__oslogstring: 0x249b
   __TEXT.__swift_as_entry: 0x1f8
   __TEXT.__swift_as_ret: 0x180
   __TEXT.__swift_as_cont: 0x334
   __TEXT.__swift5_capture: 0x1040
   __TEXT.__swift5_protos: 0xdc
-  __TEXT.__swift5_mpenum: 0x154
-  __TEXT.__unwind_info: 0x2738
-  __TEXT.__eh_frame: 0x4550
-  __DATA_CONST.__const: 0x8ea8
-  __DATA_CONST.__cfstring: 0x400
+  __TEXT.__swift5_mpenum: 0x15c
+  __TEXT.__unwind_info: 0x2740
+  __TEXT.__eh_frame: 0x4518
+  __DATA_CONST.__const: 0x8fc0
+  __DATA_CONST.__cfstring: 0x4a0
   __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_protolist: 0x2d8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x168
   __DATA_CONST.__objc_superrefs: 0x58
-  __DATA_CONST.__auth_got: 0x1108
-  __DATA_CONST.__got: 0x770
+  __DATA_CONST.__objc_arraydata: 0x18
+  __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA_CONST.__auth_got: 0x1118
+  __DATA_CONST.__got: 0x788
   __DATA_CONST.__auth_ptr: 0xb20
-  __DATA.__objc_const: 0x6318
-  __DATA.__objc_selrefs: 0xb88
+  __DATA.__objc_const: 0x6338
+  __DATA.__objc_selrefs: 0xb90
   __DATA.__objc_ivar: 0x5c
   __DATA.__objc_data: 0x1028
-  __DATA.__data: 0x7240
+  __DATA.__data: 0x7268
   __DATA.__common: 0x2e8
-  __DATA.__bss: 0x6210
+  __DATA.__bss: 0x6310
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/AVRouting.framework/Versions/A/AVRouting
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3288
-  Symbols:   951
-  CStrings:  1397
+  Functions: 3302
+  Symbols:   955
+  CStrings:  1410
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__swift5_entry : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift5_protos : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_data : content changed
Symbols:
+ _$s6Darwin5errnos5Int32Vvg
+ _AECoreErrorUserInfo
+ _AECoreNotAliveParticipantPIDsKey
+ _OBJC_CLASS_$_NSConstantArray
+ _kill
- _swift_coroFrameAlloc
CStrings:
+ "/System/Library/PrivateFrameworks/DeviceCheckInternal.framework/devicecheckd"
+ "/System/Library/PrivateFrameworks/Heimdal.framework/Helpers/kcm"
+ "/usr/libexec/odproxyd"
+ "/usr/libexec/trustd"
+ "/usr/sbin/gssd"
+ "Refusing to start session — participant PIDs not alive: %{public}s"
+ "com.apple.CharacterPaletteIM"
+ "pid"

```
