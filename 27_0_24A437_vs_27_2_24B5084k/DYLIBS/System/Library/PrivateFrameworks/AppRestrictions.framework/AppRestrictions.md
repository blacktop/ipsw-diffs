## AppRestrictions

> `/System/Library/PrivateFrameworks/AppRestrictions.framework/AppRestrictions`

```diff

-21.100.0.0.0
-  __TEXT.__text: 0xfbac
-  __TEXT.__objc_methlist: 0x44c
+22.2.2.0.0
+  __TEXT.__text: 0x10374
+  __TEXT.__objc_methlist: 0x464
   __TEXT.__const: 0x948
-  __TEXT.__cstring: 0x4b7
+  __TEXT.__oslogstring: 0x332
+  __TEXT.__cstring: 0x4d7
   __TEXT.__constg_swiftt: 0x328
   __TEXT.__swift5_typeref: 0x5f4
   __TEXT.__swift5_reflstr: 0x2d7

   __TEXT.__swift_as_entry: 0x30
   __TEXT.__swift_as_ret: 0x28
   __TEXT.__swift_as_cont: 0x68
-  __TEXT.__swift5_capture: 0x240
-  __TEXT.__oslogstring: 0x262
+  __TEXT.__swift5_capture: 0x270
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x6f0
+  __TEXT.__unwind_info: 0x728
   __TEXT.__eh_frame: 0x8d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xa0
   __DATA_CONST.__objc_classlist: 0x58
-  __DATA_CONST.__objc_catlist: 0x10
+  __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x358
+  __DATA_CONST.__objc_selrefs: 0x380
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__got: 0x170
-  __AUTH_CONST.__const: 0x738
+  __DATA_CONST.__got: 0x180
+  __AUTH_CONST.__const: 0x7a8
   __AUTH_CONST.__cfstring: 0x40
-  __AUTH_CONST.__objc_const: 0x2b08
-  __AUTH_CONST.__auth_got: 0x650
+  __AUTH_CONST.__objc_const: 0x2b48
+  __AUTH_CONST.__auth_got: 0x678
   __AUTH.__objc_data: 0x108
   __AUTH.__data: 0xd0
-  __DATA.__data: 0x4e0
+  __DATA.__data: 0x510
   __DATA_DIRTY.__objc_data: 0x3b0
   __DATA_DIRTY.__data: 0x5b0
   __DATA_DIRTY.__bss: 0x590

   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
+  - /System/Library/PrivateFrameworks/InstallCoordination.framework/InstallCoordination
   - /System/Library/PrivateFrameworks/PrivacyDisclosureCore.framework/PrivacyDisclosureCore
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/TCC.framework/TCC

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 406
-  Symbols:   483
-  CStrings:  44
+  Functions: 421
+  Symbols:   502
+  CStrings:  49
 
Symbols:
+ -[RBSProcessIdentity(ALRApplicationIdentity) alr_applicationIdentity]
+ _ALRPreflightLog
+ _ALRPreflightLog.log
+ _ALRPreflightLog.onceToken
+ _OBJC_CLASS_$_IXAppInstallCoordinator
+ _OBJC_CLASS_$_IXApplicationIdentity
+ _OUTLINED_FUNCTION_0
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_RBSProcessIdentity_$_ALRApplicationIdentity
+ __OBJC_$_CATEGORY_RBSProcessIdentity_$_ALRApplicationIdentity
+ ___ALRPreflightLog_block_invoke
+ __os_log_error_impl
+ __swift_stdlib_bridgeErrorToNSError
+ _objc_msgSend$alr_applicationIdentity
+ _objc_msgSend$applicationIdentityWithError:
+ _objc_msgSend$firstObject
+ _objc_msgSend$getAppReplacementSource:forAppIdentity:options:error:
+ _objc_msgSend$initWithLSApplicationIdentity:
+ _objc_opt_respondsToSelector
+ _os_log_create
CStrings:
+ "Encountered error for preflight check. Returning false: %@"
+ "No bundleId found for RBSProcessIdentity: %{public}@"
+ "RBSProcessIdentity returned error when fetching LSApplicationIdentity: %{public}@"
+ "Unable to resolve IXApplicationIdentity for %@"
+ "com.apple.CoreServicesUIAgent"
+ "preflight"
- "No bundleId found for rbsIdentity: %@"
```
