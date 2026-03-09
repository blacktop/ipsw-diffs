## GenerativePartnerService

> `/System/Library/PrivateFrameworks/GenerativePartnerService.framework/GenerativePartnerService`

```diff

-222.35.2.0.0
-  __TEXT.__text: 0x1c17c
-  __TEXT.__auth_stubs: 0xe10
+222.35.4.0.1
+  __TEXT.__text: 0x22454
+  __TEXT.__auth_stubs: 0xee0
   __TEXT.__objc_methlist: 0x70
-  __TEXT.__cstring: 0x76b
-  __TEXT.__swift5_typeref: 0x4ee
-  __TEXT.__const: 0x1398
-  __TEXT.__swift5_reflstr: 0x4a6
-  __TEXT.__swift5_assocty: 0xa8
-  __TEXT.__constg_swiftt: 0x5e4
-  __TEXT.__swift5_fieldmd: 0x4e8
+  __TEXT.__cstring: 0x7fb
+  __TEXT.__swift5_typeref: 0x5ae
+  __TEXT.__const: 0x17e8
+  __TEXT.__swift5_reflstr: 0x5c6
+  __TEXT.__swift5_assocty: 0xf0
+  __TEXT.__constg_swiftt: 0x674
+  __TEXT.__swift5_fieldmd: 0x5c4
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_proto: 0x104
-  __TEXT.__swift5_types: 0x5c
-  __TEXT.__oslogstring: 0xbdd
+  __TEXT.__swift5_proto: 0x128
+  __TEXT.__swift5_types: 0x6c
+  __TEXT.__oslogstring: 0xd2d
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__swift5_capture: 0x90
-  __TEXT.__swift_as_entry: 0xc
-  __TEXT.__swift_as_ret: 0x8
+  __TEXT.__swift5_capture: 0x2e8
+  __TEXT.__swift_as_entry: 0x34
+  __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x830
-  __TEXT.__eh_frame: 0x538
-  __TEXT.__objc_classname: 0x140
-  __TEXT.__objc_methname: 0x295
+  __TEXT.__unwind_info: 0xa50
+  __TEXT.__eh_frame: 0xb58
+  __TEXT.__objc_classname: 0x1a0
+  __TEXT.__objc_methname: 0x325
   __TEXT.__objc_methtype: 0x35
   __TEXT.__objc_stubs: 0x260
-  __DATA_CONST.__got: 0x220
-  __DATA_CONST.__const: 0x108
-  __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__got: 0x2c8
+  __DATA_CONST.__const: 0x138
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xb0
-  __AUTH_CONST.__auth_got: 0x710
-  __AUTH_CONST.__const: 0xfc0
-  __AUTH_CONST.__objc_const: 0x2c8
+  __AUTH_CONST.__auth_got: 0x778
+  __AUTH_CONST.__const: 0x16d0
+  __AUTH_CONST.__objc_const: 0x3c0
   __AUTH.__objc_data: 0x168
-  __AUTH.__data: 0xe8
-  __DATA.__data: 0x1e8
-  __DATA.__bss: 0x1600
+  __AUTH.__data: 0x198
+  __DATA.__data: 0x250
+  __DATA.__bss: 0x1a80
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x78
   __DATA_DIRTY.__data: 0x498

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
+  - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7E9982D9-6043-37CE-9A3E-1CB7100286AE
-  Functions: 1065
-  Symbols:   132
-  CStrings:  124
+  UUID: E84B349E-0637-3815-9B66-0698B680B9FB
+  Functions: 1294
+  Symbols:   138
+  CStrings:  141
 
Symbols:
+ _bzero
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _swift_runtimeSupportsNoncopyableTypes
+ _swift_task_immediate
+ _swift_task_isCurrentExecutorWithFlags
CStrings:
+ "[AvailabilityStore.GMAvailability.current()] Retrieved GM status: .%{public}s, info: %{public}s"
+ "[AvailabilityStore.PerProviderAvailability.current(for:)] Retrieved provider status for %{public}s: .%{public}s, info: %{public}s"
+ "[AvailabilityStore.UserFacingExternalAIRestrictedReason.current()] retrieved value: %s"
+ "_TtCC24GenerativePartnerService32GenerativePartnerServiceProvider17AvailabilityStore"
+ "_cachedAppleIntelligenceAvailability"
+ "_cachedRawPerProviderAvailability"
+ "_cachedUserFacingRestrictedReason"
+ "assetNotReady"
+ "available"
+ "childAccount"
+ "forciblyHidden"
+ "ineligible"
+ "notOptedIn"
+ "otherRestricted"
+ "parentalRestriction"
+ "regionIPRestricted"
+ "retrieved GM availability: %{public}s"
+ "retrieved availability for LLM with id \"%{public}s\" is: %{public}s"
+ "starting AvailabilityStore.GMAvailability.current()"
+ "starting AvailabilityStore.PerProviderAvailability.current(for:)"
+ "starting AvailabilityStore.UserFacingExternalAIRestrictedReason.current()"
- "Selected LLM id: %{public}s was disabled due to availability change"
- "updateLLMAvailability: LLM %{public}s use case %{public}s is available"
- "updateLLMAvailability: LLM %{public}s use case %{public}s is restricted: %{public}s"
- "updateLLMAvailability: LLM %{public}s use case %{public}s is unavailable: %{public}s"

```
