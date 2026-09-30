## GameController

> `/System/iOSSupport/System/Library/Frameworks/GameController.framework/Versions/A/GameController`

```diff

-12.0.32.0.0
-  __TEXT.__text: 0xe2b10
-  __TEXT.__auth_stubs: 0x1830
+12.0.33.0.0
+  __TEXT.__text: 0xe3e48
+  __TEXT.__auth_stubs: 0x1860
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0xc004
   __TEXT.__const: 0x3344
-  __TEXT.__cstring: 0x9150
-  __TEXT.__gcc_except_tab: 0x47fc
-  __TEXT.__oslogstring: 0x91be
+  __TEXT.__cstring: 0x9180
+  __TEXT.__gcc_except_tab: 0x4820
+  __TEXT.__oslogstring: 0x936f
   __TEXT.__dlopen_cstrs: 0x49
   __TEXT.__swift5_typeref: 0x3be
   __TEXT.__swift5_reflstr: 0x17f

   __TEXT.__swift5_proto: 0x6c
   __TEXT.__swift5_types: 0x24
   __TEXT.__swift5_capture: 0x30
-  __TEXT.__unwind_info: 0x40f4
+  __TEXT.__unwind_info: 0x4114
   __TEXT.__eh_frame: 0xc8
   __TEXT.__objc_classname: 0x3bec
-  __TEXT.__objc_methname: 0x17792
-  __TEXT.__objc_methtype: 0x739b
-  __TEXT.__objc_stubs: 0xe3a0
+  __TEXT.__objc_methname: 0x177c8
+  __TEXT.__objc_methtype: 0x73c1
+  __TEXT.__objc_stubs: 0xe3c0
   __DATA_CONST.__got: 0x570
-  __DATA_CONST.__const: 0x2bf0
+  __DATA_CONST.__const: 0x2c48
   __DATA_CONST.__objc_classlist: 0x820
   __DATA_CONST.__objc_catlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x748
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3de18
-  __DATA_CONST.__objc_selrefs: 0x4bf0
+  __DATA_CONST.__objc_const: 0x3de58
+  __DATA_CONST.__objc_selrefs: 0x4bf8
   __DATA_CONST.__objc_protorefs: 0x480
   __DATA_CONST.__objc_classrefs: 0x950
   __DATA_CONST.__objc_superrefs: 0x7a8
   __DATA_CONST.__objc_arraydata: 0x770
   __AUTH_CONST.__objc_const: 0x68d0
   __AUTH_CONST.__cfstring: 0xa720
-  __AUTH_CONST.__const: 0x17e8
+  __AUTH_CONST.__const: 0x1808
   __AUTH_CONST.__objc_intobj: 0x1458
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH_CONST.__auth_got: 0xc30
+  __AUTH_CONST.__auth_got: 0xc48
   __AUTH.__objc_data: 0x5050
   __AUTH.__data: 0xb0
-  __DATA.__objc_ivar: 0x1580
+  __DATA.__objc_ivar: 0x1588
   __DATA.__data: 0x5750
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x1670
+  __DATA.__bss: 0x1680
   __DATA.__common: 0x48
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__bss: 0x60

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5872
-  Symbols:   16390
-  CStrings:  1570
+  Functions: 5876
+  Symbols:   16408
+  CStrings:  1572
 
Symbols:
+ -[GCAnalytics(HapticsAnalytics) sendHapticsPlayerDestroyedEventForBundleID:productCategory:totalEventsProcessed:transientEventsProcessed:continuousEventsProcessed:parameterCurvesProcessed:sessionTotalDuration:sessionActiveDuration:].cold.1
+ OBJC_IVAR_$_GCAnalytics._lastHapticsEvent
+ OBJC_IVAR_$_GCAnalytics._timebaseInfo
+ __38-[_GCHapticServerManager enterRunloop]_block_invoke.24
+ __43-[GCControllerButtonInput _setValue:queue:]_block_invoke.86
+ __43-[GCControllerButtonInput _setValue:queue:]_block_invoke.87
+ __45-[_GCHapticServerManager removeHapticClient:]_block_invoke.17
+ __55-[_GCHapticServerManager logicalDeviceWasUnregistered:]_block_invoke.23
+ ___block_descriptor_48_ea8_32s40s_e42_v32?0"NSNumber"8"_GCHapticPlayer"16^B24ls32l8s40l8
+ ___block_descriptor_84_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
+ ___block_descriptor_85_e8_32s40s48s56bs_e5_v8?0ls56l8s32l8s40l8s48l8
+ ___block_descriptor_86_e8_32s40s48s56bs_e5_v8?0ls56l8s32l8s40l8s48l8
+ ___block_descriptor_88_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
+ ___block_descriptor_89_e8_32s40s48s56bs_e5_v8?0ls56l8s32l8s40l8s48l8
+ ___getGCSignpostLogger_block_invoke
+ __block_literal_global.62
+ __os_signpost_emit_with_name_impl
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_GameController
+ _gcSignpostLogger
+ _getGCSignpostLogger
+ _objc_msgSend$removeObjectsForKeys:
+ _os_signpost_enabled
+ _os_signpost_id_generate
+ getGCSignpostLogger.onceToken
- __38-[_GCHapticServerManager enterRunloop]_block_invoke.22
- __55-[_GCHapticServerManager logicalDeviceWasUnregistered:]_block_invoke.21
- ___43-[GCControllerButtonInput _setValue:queue:]_block_invoke_2
- ___43-[GCControllerButtonInput _setValue:queue:]_block_invoke_3
- ___block_descriptor_52_e8_32s40bs_e5_v8?0ls40l8s32l8
- ___block_descriptor_53_e8_32s40bs_e5_v8?0ls40l8s32l8
- ___block_descriptor_54_e8_32s40bs_e5_v8?0ls40l8s32l8
- ___block_descriptor_57_e8_32s40bs_e5_v8?0ls40l8s32l8
CStrings:
+ "Signposts"
+ "v32@?0@\"NSNumber\"8@\"_GCHapticPlayer\"16^B24"

```
