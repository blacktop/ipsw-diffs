## CloudSubscriptionFeatures

> `/System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures`

```diff

-301.22.0.26.8
-  __TEXT.__text: 0x91d90
-  __TEXT.__auth_stubs: 0x1a00
-  __TEXT.__objc_methlist: 0x9fc
-  __TEXT.__const: 0x4188
-  __TEXT.__gcc_except_tab: 0x80
-  __TEXT.__cstring: 0x3cc1
-  __TEXT.__oslogstring: 0x5a2c
+301.22.1.2.2
+  __TEXT.__text: 0x93b04
+  __TEXT.__auth_stubs: 0x1a10
+  __TEXT.__objc_methlist: 0xa1c
+  __TEXT.__const: 0x4178
+  __TEXT.__gcc_except_tab: 0x90
+  __TEXT.__cstring: 0x3db1
+  __TEXT.__oslogstring: 0x5d9c
   __TEXT.__dlopen_cstrs: 0x62
-  __TEXT.__swift5_typeref: 0x15da
-  __TEXT.__swift5_fieldmd: 0x119c
+  __TEXT.__swift5_typeref: 0x1600
+  __TEXT.__swift5_fieldmd: 0x11a8
   __TEXT.__constg_swiftt: 0x1690
-  __TEXT.__swift5_reflstr: 0xcfd
+  __TEXT.__swift5_reflstr: 0xd0d
   __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_assocty: 0x240
-  __TEXT.__swift5_capture: 0x8cc
+  __TEXT.__swift5_capture: 0xb00
   __TEXT.__swift5_protos: 0x54
   __TEXT.__swift5_proto: 0x3a4
   __TEXT.__swift5_types: 0x180
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x2450
-  __TEXT.__eh_frame: 0x4f18
+  __TEXT.__unwind_info: 0x25e0
+  __TEXT.__eh_frame: 0x5388
   __TEXT.__objc_classname: 0xda
-  __TEXT.__objc_methname: 0x1973
-  __TEXT.__objc_methtype: 0x250
-  __TEXT.__objc_stubs: 0xa80
+  __TEXT.__objc_methname: 0x1a27
+  __TEXT.__objc_methtype: 0x268
+  __TEXT.__objc_stubs: 0xaa0
   __DATA_CONST.__got: 0x420
-  __DATA_CONST.__const: 0x378
+  __DATA_CONST.__const: 0x420
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x790
+  __DATA_CONST.__objc_selrefs: 0x7a0
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0xd10
-  __AUTH_CONST.__auth_ptr: 0x628
-  __AUTH_CONST.__const: 0x3cd8
+  __AUTH_CONST.__auth_got: 0xd18
+  __AUTH_CONST.__auth_ptr: 0x640
+  __AUTH_CONST.__const: 0x4140
   __AUTH_CONST.__cfstring: 0x400
-  __AUTH_CONST.__objc_const: 0x2ae0
-  __AUTH.__objc_data: 0x9e0
-  __AUTH.__data: 0x550
+  __AUTH_CONST.__objc_const: 0x2ab8
+  __AUTH.__objc_data: 0x158
   __DATA.__objc_ivar: 0x2c
-  __DATA.__data: 0x1040
-  __DATA.__bss: 0x55b0
-  __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x7f0
-  __DATA_DIRTY.__data: 0x1040
-  __DATA_DIRTY.__bss: 0x1420
-  __DATA_DIRTY.__common: 0x38
+  __DATA.__data: 0xf70
+  __DATA.__bss: 0x5010
+  __DATA.__common: 0x8
+  __DATA_DIRTY.__objc_data: 0x1078
+  __DATA_DIRTY.__data: 0x17d8
+  __DATA_DIRTY.__bss: 0x19c0
+  __DATA_DIRTY.__common: 0x40
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2787
-  Symbols:   548
-  CStrings:  1189
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 2886
+  Symbols:   558
+  CStrings:  1208
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _objc_retain_x10
CStrings:
+ "%!s(MISSING) Getting device asset status."
+ "%!s(MISSING) Received device asset status - assetsFinishedDownloading? %!{(MISSING)public}@, hasEnoughStorage? %!{(MISSING)public}@"
+ "%!s(MISSING) Returning result: %!{(MISSING)public}@"
+ "%!s(MISSING) device is eligible, will use GM temporary TTL value of 1 hour: %!f(MISSING)"
+ "%!s(MISSING) device is not GM eligible, will use default ttlFallbackDate: %!f(MISSING)"
+ "+[CSFAvailability _handleFeatureResponseWithFeatureObject:error:reasons:shouldBypassEligibility:completionHandler:]"
+ "+[CSFAvailability currentAvailability]_block_invoke"
+ "Assets are not ready. Device has enough storage? %!{(MISSING)bool,public}d"
+ "Assets are ready. Returning true."
+ "Bailing to prevent a loop."
+ "Eligibility changed while network request was in progress. Will not stub feature to force a new network request."
+ "Eligibility is the same as before the network request was made. Will stub feature to prevent new network requests."
+ "Error getting eligibility: %!{(MISSING)public}s"
+ "Nested feature request call returning attempt #%!l(MISSING)d."
+ "Too many attempts to fetch the same feature."
+ "Try again later."
+ "We have attempted %!l(MISSING)d times already, bailing out of %!s(MISSING)"
+ "Will not stub feature - making additional feature call and returning."
+ "_handleFeatureResponseWithFeatureObject:error:reasons:shouldBypassEligibility:completionHandler:"
+ "assetStatusWithCompletionHandler:"
+ "assetsFinishedDownloadingWithCompletionHandler:"
+ "gmBypass is enabled, opt-in status checks."
+ "postFollowUpItem:completion:"
+ "requestFeature(id:ignoreCache:attemptNumber:completion:)"
+ "userHasEnoughStorageWithCompletionHandler:"
+ "v16@?0B8B12"
+ "v24@0:8@?<v@?BB>16"
+ "v52@0:8@16@24q32B40@?44"
- "+[CSFAvailability currentAvailabilityWithCompletionHandler:]_block_invoke_2"
- "Asset has finished downloading."
- "User does not have enough storage."
- "assetsFinishedDownloading"
- "assetsFinishedDownloading"
- "gmBypass is enabled, skipping the asset and opt-in status checks."
- "postFollowUpItem:error:"
- "userHasEnoughStorage"
- "userHasEnoughStorage"

```
