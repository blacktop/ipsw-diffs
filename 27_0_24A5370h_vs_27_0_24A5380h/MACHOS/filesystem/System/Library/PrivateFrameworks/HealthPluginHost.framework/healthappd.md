## healthappd

> `/System/Library/PrivateFrameworks/HealthPluginHost.framework/healthappd`

```diff

-  __TEXT.__text: 0x311c0
-  __TEXT.__auth_stubs: 0x2360
+  __TEXT.__text: 0x317d0
+  __TEXT.__auth_stubs: 0x2380
   __TEXT.__objc_stubs: 0x720
   __TEXT.__objc_methlist: 0x4e4
   __TEXT.__const: 0x9e8
   __TEXT.__cstring: 0x7f9
   __TEXT.__objc_methtype: 0x44c
-  __TEXT.__oslogstring: 0x1f31
+  __TEXT.__oslogstring: 0x2001
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x62c
   __TEXT.__swift5_typeref: 0x6cc

   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__auth_got: 0x11b8
-  __DATA_CONST.__got: 0x6c0
+  __DATA_CONST.__auth_got: 0x11c8
+  __DATA_CONST.__got: 0x6b0
   __DATA_CONST.__auth_ptr: 0x3d8
   __DATA.__objc_const: 0x1140
   __DATA.__objc_selrefs: 0x3b0

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 707
+  Functions: 706
   Symbols:   880
-  CStrings:  400
+  CStrings:  402
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__swift5_entry : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _$s14HealthPlatform21GenerationWorkRequestV11environment24pluginIdentifierSetToRun16generationPhases23commitUrgentTransaction04makecD5Block010completionR0022notStartedCancellationR0AcA26FeedItemContextEnvironmentO_AA06PluginhI0OShyAA0C5PhaseOGSbAA0cD0_pACYbcySbYbcyyYbctcfC
+ _$s14HealthPlatform21GenerationWorkRequestV15completionBlockyySbYbcvg
+ _$s14HealthPlatform21GenerationWorkRequestV15completionBlockyySbYbcvs
- _$s14HealthPlatform21GenerationWorkRequestV15completionBlockyyYbcvg
- _$s14HealthPlatform21GenerationWorkRequestV15completionBlockyyYbcvs
- _swift_willThrowTypedImpl
CStrings:
+ "[%{public}s]: Background generation completed/cancelled, and is completion from coalesced work, so skipping feed population"
+ "[%{public}s]: DAS background was part of coalesced work, skip populating feed"

```
