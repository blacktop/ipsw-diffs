## IntelligentRoutingDaemon

> `/System/Library/PrivateFrameworks/IntelligentRoutingDaemon.framework/IntelligentRoutingDaemon`

```diff

-125.0.13.0.0
-  __TEXT.__text: 0xb6ee8
-  __TEXT.__objc_methlist: 0x77a4
+125.1.4.0.0
+  __TEXT.__text: 0xb7768
+  __TEXT.__objc_methlist: 0x77ac
   __TEXT.__const: 0x3670
-  __TEXT.__cstring: 0xafad
-  __TEXT.__oslogstring: 0x5d7a
+  __TEXT.__cstring: 0xafdd
+  __TEXT.__oslogstring: 0x5dd1
   __TEXT.__gcc_except_tab: 0x1670
-  __TEXT.__swift5_typeref: 0xfbe
+  __TEXT.__swift5_typeref: 0xfca
   __TEXT.__swift5_fieldmd: 0xf48
   __TEXT.__constg_swiftt: 0xf74
   __TEXT.__swift5_builtin: 0x104

   __TEXT.__swift_as_entry: 0x74
   __TEXT.__swift_as_ret: 0x64
   __TEXT.__swift_as_cont: 0x64
-  __TEXT.__unwind_info: 0x3708
-  __TEXT.__eh_frame: 0x17a8
+  __TEXT.__unwind_info: 0x3710
+  __TEXT.__eh_frame: 0x17b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1ce0
+  __DATA_CONST.__const: 0x1cc8
   __DATA_CONST.__objc_classlist: 0x4b8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x168
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x42c0
+  __DATA_CONST.__objc_selrefs: 0x42c8
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x2b0
   __DATA_CONST.__objc_arraydata: 0x98
-  __DATA_CONST.__got: 0x11b8
+  __DATA_CONST.__got: 0x11c0
   __AUTH_CONST.__const: 0x2428
-  __AUTH_CONST.__cfstring: 0x6680
-  __AUTH_CONST.__objc_const: 0xec20
+  __AUTH_CONST.__cfstring: 0x66a0
+  __AUTH_CONST.__objc_const: 0xec50
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_intobj: 0x3d8
   __AUTH_CONST.__objc_doubleobj: 0xe0
-  __AUTH_CONST.__auth_got: 0xde8
+  __AUTH_CONST.__auth_got: 0xe00
   __AUTH.__objc_data: 0xc20
   __AUTH.__data: 0x2d0
-  __DATA.__objc_ivar: 0x960
-  __DATA.__data: 0x1a58
+  __DATA.__objc_ivar: 0x964
+  __DATA.__data: 0x1a68
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x2668
   __DATA_DIRTY.__data: 0xba0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4339
-  Symbols:   11247
-  CStrings:  1526
+  Functions: 4341
+  Symbols:   11262
+  CStrings:  1528
 
Symbols:
+ -[IRPreferences proximitySessionRetryBaseDelaySeconds]
+ -[IRPreferences proximitySessionRetryMaxDelaySeconds]
+ -[IRProximityProvider _retryDelayForCount:]
+ _$s10Foundation4UUIDVACSQAAWL
+ _$s10Foundation4UUIDVACSQAAWl
+ _$s10Foundation4UUIDVSQAAMc
+ _$s10Foundation4UUIDVSgWOhTm
+ _$s10Foundation4UUIDVSg_ADtMR
+ _$s10Foundation4UUIDVSg_ADtMd
+ _$sSQ2eeoiySbx_xtFZTj
+ _OBJC_IVAR_$_IRPreferences._proximitySessionRetryBaseDelaySeconds
+ _OBJC_IVAR_$_IRPreferences._proximitySessionRetryMaxDelaySeconds
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_IntelligentRoutingDaemon
+ __swift_FORCE_LOAD_$_swiftIntents
+ __swift_FORCE_LOAD_$_swiftIntents_$_IntelligentRoutingDaemon
+ _dispatch_after
+ _exp2
+ _objc_msgSend$_retryDelayForCount:
+ _objc_msgSend$proximitySessionRetryBaseDelaySeconds
+ _objc_msgSend$proximitySessionRetryMaxDelaySeconds
+ _objc_msgSend$roomForEntireHome
+ _symbolic _____Sg_ABt 10Foundation4UUIDV
- -[IRPreferences proximitySessionRetryCountThreshold]
- -[IRProximityProvider _incrementRetryCount:]
- -[IRProximityProvider _resetRetryCount:]
- _OBJC_IVAR_$_IRPreferences._proximitySessionRetryCountThreshold
- ___block_descriptor_64_e8_32s40s48s56w_e5_v8?0lw56l8s32l8s40l8s48l8
- _objc_msgSend$_incrementRetryCount:
- _objc_msgSend$_resetRetryCount:
- _objc_msgSend$proximitySessionRetryCountThreshold
CStrings:
+ "#proximity-provider, Bridge failed: %@, retry #%@ in %@s"
+ "#proximity-provider, Skipping delayed retry, bridge %@ was torn down"
+ "IRproximitySessionRetryBaseDelaySeconds"
+ "IRproximitySessionRetryMaxDelaySeconds"
- "#proximity-provider, Bridge failed: %@"
- "IRproximitySessionRetryCountThreshold"
```
