## GenerativeExperiencesRuntime

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/GenerativeExperiencesRuntime`

```diff

-  __TEXT.__text: 0xe5084
-  __TEXT.__objc_methlist: 0x94c
-  __TEXT.__const: 0x5afc
-  __TEXT.__cstring: 0x1ed5
-  __TEXT.__constg_swiftt: 0x1f1c
-  __TEXT.__swift5_typeref: 0x28dc
+  __TEXT.__text: 0xe7014
+  __TEXT.__objc_methlist: 0x95c
+  __TEXT.__const: 0x5a7c
+  __TEXT.__cstring: 0x1e65
+  __TEXT.__constg_swiftt: 0x1ea8
+  __TEXT.__swift5_typeref: 0x286c
   __TEXT.__swift5_builtin: 0x8c
-  __TEXT.__swift5_reflstr: 0xfed
-  __TEXT.__swift5_fieldmd: 0x147c
-  __TEXT.__swift5_assocty: 0x420
-  __TEXT.__oslogstring: 0x8770
-  __TEXT.__swift5_proto: 0x304
-  __TEXT.__swift5_types: 0x228
-  __TEXT.__swift_as_entry: 0x324
-  __TEXT.__swift_as_ret: 0x33c
-  __TEXT.__swift_as_cont: 0x6b0
-  __TEXT.__swift5_capture: 0x24c8
+  __TEXT.__swift5_reflstr: 0xffd
+  __TEXT.__swift5_fieldmd: 0x1428
+  __TEXT.__swift5_assocty: 0x400
+  __TEXT.__oslogstring: 0x8760
+  __TEXT.__swift5_proto: 0x300
+  __TEXT.__swift5_types: 0x21c
+  __TEXT.__swift_as_entry: 0x334
+  __TEXT.__swift_as_ret: 0x354
+  __TEXT.__swift_as_cont: 0x6fc
+  __TEXT.__swift5_capture: 0x276c
   __TEXT.__swift5_protos: 0x54
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__unwind_info: 0x3330
-  __TEXT.__eh_frame: 0x8e1c
+  __TEXT.__unwind_info: 0x33a0
+  __TEXT.__eh_frame: 0x90ec
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6c0
+  __DATA_CONST.__objc_selrefs: 0x6e0
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x7d80
-  __AUTH_CONST.__objc_const: 0x3108
-  __AUTH_CONST.__auth_got: 0x2770
-  __AUTH.__objc_data: 0x428
-  __AUTH.__data: 0x5f8
-  __DATA.__data: 0xd00
-  __DATA.__bss: 0x29f0
-  __DATA.__common: 0xd8
-  __DATA_DIRTY.__objc_data: 0x698
-  __DATA_DIRTY.__data: 0x2ff0
-  __DATA_DIRTY.__bss: 0x2780
-  __DATA_DIRTY.__common: 0x280
+  __AUTH_CONST.__const: 0x8428
+  __AUTH_CONST.__objc_const: 0x3150
+  __AUTH_CONST.__auth_got: 0x2780
+  __AUTH.__objc_data: 0x3b8
+  __AUTH.__data: 0x430
+  __DATA.__data: 0xad8
+  __DATA.__bss: 0x2770
+  __DATA.__common: 0x78
+  __DATA_DIRTY.__objc_data: 0x6c8
+  __DATA_DIRTY.__data: 0x32d0
+  __DATA_DIRTY.__bss: 0x2900
+  __DATA_DIRTY.__common: 0x2b0
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftRegexBuilder.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
+  - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5048
-  Symbols:   283
-  CStrings:  650
+  Functions: 5122
+  Symbols:   282
+  CStrings:  647
 
Sections:
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
Symbols:
+ _OBJC_CLASS_$_BGNonRepeatingSystemTaskRequest
- _OBJC_CLASS_$_NSXPCListenerEndpoint
- _swift_getFunctionTypeMetadata0
CStrings:
+ "ExternalProviderServiceXPC.Server init"
+ "PQAReadinessPollOneShot.schedule: FF off; no-op"
+ "PQAReadinessPollOneShot.schedule: submitTaskRequest returned: %{public}@"
+ "PQAReadinessPollOneShot.schedule: submitted"
+ "PeriodicTask: Running task for %{public}s with priority %{public}s"
+ "XPC: client subscribed to provider changes"
+ "XPC: client unsubscribed from provider changes"
+ "XPC: failed to forward provider change: %@"
+ "XPC: forwarding provider change to client: %{public}s"
+ "com.apple.GenerativeFunctions.PeriodicTasks.AvailabilityUpdateTask.PQAReadinessPollOneShot"
+ "runEnhancedSiriOnboardingCheck()"
- "ExternalProviderServiceXPC.ResidentService: sending change notification: %{public}s"
- "ExternalProviderServiceXPC.Server: Deinitializing"
- "ExternalProviderServiceXPC.init"
- "ResidentService deinitializing"
- "ResidentService initializing"
- "ResidentService: registered ExternalProviderServiceXPC.ResidentService as an observer"
- "XPC: Invalid observer ID: %s"
- "XPC: Registered observer: %s"
- "XPC: Unregistered observer: %s, success: %{bool}d"
- "XPC: registerObserver() called with ID: %s"
- "XPC: unregisterObserver() called with ID: %s"
- "com.apple.generativeexperiences.ExternalPartnerCredentialStorage"
- "com.apple.generativeexperiences.ExternalProviderService"
- "com.apple.generativeexperiences.ExternalProviderTCCManagingXPC"

```
