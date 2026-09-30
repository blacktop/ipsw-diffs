## IntelligentRoutingDaemon

> `/System/Library/PrivateFrameworks/IntelligentRoutingDaemon.framework/Versions/A/IntelligentRoutingDaemon`

```diff

-125.0.13.0.0
-  __TEXT.__text: 0xbcfc0
-  __TEXT.__objc_methlist: 0x771c
+125.1.4.0.0
+  __TEXT.__text: 0xbd7e8
+  __TEXT.__objc_methlist: 0x7724
   __TEXT.__const: 0x3660
-  __TEXT.__cstring: 0xaabd
-  __TEXT.__oslogstring: 0x59a6
+  __TEXT.__cstring: 0xaadd
+  __TEXT.__oslogstring: 0x59fd
   __TEXT.__gcc_except_tab: 0x156c
-  __TEXT.__swift5_typeref: 0xfbe
+  __TEXT.__swift5_typeref: 0xfca
   __TEXT.__swift5_fieldmd: 0xf48
   __TEXT.__constg_swiftt: 0xf74
   __TEXT.__swift5_builtin: 0x104

   __TEXT.__swift_as_entry: 0x74
   __TEXT.__swift_as_ret: 0x64
   __TEXT.__swift_as_cont: 0x64
-  __TEXT.__unwind_info: 0x35d8
-  __TEXT.__eh_frame: 0x17a8
+  __TEXT.__unwind_info: 0x35d0
+  __TEXT.__eh_frame: 0x17b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x870
+  __DATA_CONST.__const: 0x880
   __DATA_CONST.__objc_classlist: 0x4b8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x168
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x41e8
+  __DATA_CONST.__objc_selrefs: 0x41f0
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x2b0
   __DATA_CONST.__objc_arraydata: 0x58
-  __DATA_CONST.__got: 0x1140
-  __AUTH_CONST.__const: 0x3b48
-  __AUTH_CONST.__cfstring: 0x6220
-  __AUTH_CONST.__objc_const: 0xebe8
+  __DATA_CONST.__got: 0x1148
+  __AUTH_CONST.__const: 0x3b18
+  __AUTH_CONST.__cfstring: 0x6240
+  __AUTH_CONST.__objc_const: 0xec18
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x3d8
   __AUTH_CONST.__objc_doubleobj: 0xe0
-  __AUTH_CONST.__auth_got: 0xc30
+  __AUTH_CONST.__auth_got: 0xc48
   __AUTH.__objc_data: 0xbd0
   __AUTH.__data: 0x2d0
-  __DATA.__objc_ivar: 0x95c
-  __DATA.__data: 0x1a68
+  __DATA.__objc_ivar: 0x960
+  __DATA.__data: 0x1a78
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x26b8
   __DATA_DIRTY.__data: 0xbc0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
+  - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 4366
-  Symbols:   11184
-  CStrings:  1473
+  Symbols:   11199
+  CStrings:  1475
 
Symbols:
+ -[IRPreferences proximitySessionRetryBaseDelaySeconds]
+ -[IRPreferences proximitySessionRetryMaxDelaySeconds]
+ -[IRProximityProvider _retryDelayForCount:]
+ GCC_except_table39
+ OBJC_IVAR_$_IRPreferences._proximitySessionRetryBaseDelaySeconds
+ OBJC_IVAR_$_IRPreferences._proximitySessionRetryMaxDelaySeconds
+ _$s10Foundation4UUIDVACSQAAWL
+ _$s10Foundation4UUIDVACSQAAWl
+ _$s10Foundation4UUIDVSQAAMc
+ _$s10Foundation4UUIDVSgWOhTm
+ _$s10Foundation4UUIDVSg_ADtMR
+ _$s10Foundation4UUIDVSg_ADtMd
+ _$sSQ2eeoiySbx_xtFZTj
+ __37-[IRProximityProvider didBridgeFail:]_block_invoke
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
- OBJC_IVAR_$_IRPreferences._proximitySessionRetryCountThreshold
- ___block_descriptor_64_e8_32s40s48s56w_e5_v8?0l
- ___copy_helper_block_e8_32s40s48s56w
- ___destroy_helper_block_e8_32s40s48s56w
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
