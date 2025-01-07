## GenerativeAssistantCommon

> `/System/Library/PrivateFrameworks/GenerativeAssistantCommon.framework/GenerativeAssistantCommon`

```diff

-3403.6.1.0.0
-  __TEXT.__text: 0xb414
-  __TEXT.__auth_stubs: 0x6f0
+3403.9.3.0.0
+  __TEXT.__text: 0x10520
+  __TEXT.__auth_stubs: 0x810
   __TEXT.__objc_methlist: 0x38
-  __TEXT.__const: 0xf86
-  __TEXT.__cstring: 0xa29
-  __TEXT.__swift5_typeref: 0x34e
-  __TEXT.__constg_swiftt: 0x398
-  __TEXT.__swift5_reflstr: 0x2f9
-  __TEXT.__swift5_fieldmd: 0x348
-  __TEXT.__swift5_proto: 0xcc
-  __TEXT.__swift5_types: 0x4c
-  __TEXT.__oslogstring: 0x333
+  __TEXT.__const: 0xff8
+  __TEXT.__cstring: 0xa96
+  __TEXT.__swift5_typeref: 0x366
+  __TEXT.__constg_swiftt: 0x3fc
+  __TEXT.__swift5_reflstr: 0x331
+  __TEXT.__swift5_fieldmd: 0x37c
+  __TEXT.__swift5_proto: 0xd0
+  __TEXT.__swift5_types: 0x50
+  __TEXT.__oslogstring: 0x65e
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0x3b8
-  __TEXT.__eh_frame: 0x80
-  __TEXT.__objc_methname: 0x164
-  __DATA_CONST.__got: 0x98
+  __TEXT.__unwind_info: 0x4b8
+  __TEXT.__eh_frame: 0x280
+  __TEXT.__objc_methname: 0x18c
+  __DATA_CONST.__got: 0xa8
   __DATA_CONST.__const: 0x120
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb8
-  __AUTH_CONST.__auth_got: 0x378
-  __AUTH_CONST.__auth_ptr: 0x1b8
-  __AUTH_CONST.__const: 0x628
+  __DATA_CONST.__objc_selrefs: 0xc0
+  __AUTH_CONST.__auth_got: 0x408
+  __AUTH_CONST.__auth_ptr: 0x1c0
+  __AUTH_CONST.__const: 0x700
   __AUTH_CONST.__objc_const: 0xc8
   __AUTH.__objc_data: 0x120
   __AUTH.__data: 0x28
-  __DATA.__data: 0x2b0
-  __DATA.__bss: 0x1880
+  __DATA.__data: 0x308
+  __DATA.__bss: 0x1900
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/Anvil.framework/Anvil
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_errno.dylib
   - /usr/lib/swift/libswift_math.dylib
   - /usr/lib/swift/libswift_signal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 380
-  Symbols:   110
-  CStrings:  105
+  Functions: 457
+  Symbols:   114
+  CStrings:  119
 
Symbols:
+ _swift_task_alloc
+ _swift_task_dealloc
+ _swift_task_switch
CStrings:
+ "%s.%s External intelligence sign in is restricted -- signing out."
+ "%s: %s is not allowed"
+ "%s: %{bool}d"
+ "%s: a workspace is required, but the credentials have none"
+ "%s: allowExternalIntelligenceIntegrationsSignIn does not allow sign in, but allowedExternalIntelligenceWorkspaceIDs requires it."
+ "%s: allowedExternalIntelligenceWorkspaceIDs is set but empty."
+ "%s: an empty value for allowedExternalIntelligenceWorkspaceIDs was provided, unable to validate any credentials."
+ "%s: no workspace restriction"
+ "%s: workspace id %s matched. User signed in with an accepted workspace."
+ "Montara: isMontaraAllowed %{bool}d -- afMontaraRestricted %{bool}d isMisconfigured %{bool}d userNeedsToSignInToWorkspace %{bool}d userShouldBeAnonymous %{bool}d"
+ "allowedExternalIntelligenceWorkspaceIDs"
+ "allowedExternalIntelligenceWorkspaceIDs %s"
+ "isExternalIntelligenceSignInRequired"
+ "signOutIfRestricted()"
+ "workspaceAllowed(workspaceId:)"
- "Montara: isMontaraAllowed %{bool}d"

```
