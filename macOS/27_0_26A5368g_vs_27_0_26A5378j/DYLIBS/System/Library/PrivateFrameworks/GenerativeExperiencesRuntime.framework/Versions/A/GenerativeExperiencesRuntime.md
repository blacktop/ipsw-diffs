## GenerativeExperiencesRuntime

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/Versions/A/GenerativeExperiencesRuntime`

```diff

-  __TEXT.__text: 0xe6d34
-  __TEXT.__objc_methlist: 0x964
-  __TEXT.__const: 0x5cb8
-  __TEXT.__cstring: 0x1df7
-  __TEXT.__constg_swiftt: 0x1f3c
-  __TEXT.__swift5_typeref: 0x28ee
+  __TEXT.__text: 0xe8db4
+  __TEXT.__objc_methlist: 0x974
+  __TEXT.__const: 0x5c18
+  __TEXT.__cstring: 0x1d87
+  __TEXT.__constg_swiftt: 0x1ec8
+  __TEXT.__swift5_typeref: 0x287e
   __TEXT.__swift5_builtin: 0xa0
-  __TEXT.__swift5_reflstr: 0xfed
-  __TEXT.__swift5_fieldmd: 0x1498
-  __TEXT.__swift5_assocty: 0x450
-  __TEXT.__oslogstring: 0x8430
-  __TEXT.__swift5_proto: 0x31c
-  __TEXT.__swift5_types: 0x22c
-  __TEXT.__swift_as_entry: 0x320
-  __TEXT.__swift_as_ret: 0x32c
-  __TEXT.__swift_as_cont: 0x6a0
-  __TEXT.__swift5_capture: 0x23b8
+  __TEXT.__swift5_reflstr: 0xffd
+  __TEXT.__swift5_fieldmd: 0x1444
+  __TEXT.__swift5_assocty: 0x430
+  __TEXT.__oslogstring: 0x8420
+  __TEXT.__swift5_proto: 0x318
+  __TEXT.__swift5_types: 0x220
+  __TEXT.__swift_as_entry: 0x330
+  __TEXT.__swift_as_ret: 0x344
+  __TEXT.__swift_as_cont: 0x6ec
+  __TEXT.__swift5_capture: 0x265c
   __TEXT.__swift5_protos: 0x54
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__unwind_info: 0x3248
-  __TEXT.__eh_frame: 0x8bc4
+  __TEXT.__unwind_info: 0x32c0
+  __TEXT.__eh_frame: 0x8eb4
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x690
+  __DATA_CONST.__objc_selrefs: 0x6b0
   __DATA_CONST.__objc_protorefs: 0x90
-  __DATA_CONST.__got: 0x13c8
-  __AUTH_CONST.__const: 0x7ab0
+  __DATA_CONST.__got: 0x1408
+  __AUTH_CONST.__const: 0x8158
   __AUTH_CONST.__cfstring: 0x40
-  __AUTH_CONST.__objc_const: 0x3198
-  __AUTH_CONST.__auth_got: 0x25f8
-  __AUTH.__objc_data: 0x428
-  __AUTH.__data: 0x5f8
-  __DATA.__data: 0xc60
-  __DATA.__bss: 0x27f0
-  __DATA.__common: 0xd0
-  __DATA_DIRTY.__objc_data: 0x6e8
-  __DATA_DIRTY.__data: 0x30c0
-  __DATA_DIRTY.__bss: 0x2c80
-  __DATA_DIRTY.__common: 0x288
+  __AUTH_CONST.__objc_const: 0x31e0
+  __AUTH_CONST.__auth_got: 0x2608
+  __AUTH.__objc_data: 0x3b8
+  __AUTH.__data: 0x430
+  __DATA.__data: 0xa18
+  __DATA.__bss: 0x25f0
+  __DATA.__common: 0x70
+  __DATA_DIRTY.__objc_data: 0x718
+  __DATA_DIRTY.__data: 0x33a0
+  __DATA_DIRTY.__bss: 0x2d80
+  __DATA_DIRTY.__common: 0x2b8
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftRegexBuilder.dylib
+  - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5003
-  Symbols:   232
-  CStrings:  637
+  Functions: 5076
+  Symbols:   231
+  CStrings:  634
 
Sections:
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __AUTH_CONST.__cfstring : content changed
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
