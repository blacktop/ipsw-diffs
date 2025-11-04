## BrowserEngineCore

> `/System/Library/Frameworks/BrowserEngineCore.framework/BrowserEngineCore`

```diff

-7622.1.19.2.0
-  __TEXT.__text: 0x1bd8
-  __TEXT.__auth_stubs: 0x380
-  __TEXT.__objc_methlist: 0x9c
-  __TEXT.__const: 0x272
-  __TEXT.__cstring: 0x2a8
-  __TEXT.__swift5_typeref: 0x8e
+7623.1.11.4.0
+  __TEXT.__text: 0x2ad4
+  __TEXT.__auth_stubs: 0x580
+  __TEXT.__objc_methlist: 0xc0
+  __TEXT.__const: 0x288
+  __TEXT.__cstring: 0x462
+  __TEXT.__swift5_typeref: 0xb0
   __TEXT.__swift5_reflstr: 0x61
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__constg_swiftt: 0x108

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0x14
-  __TEXT.__unwind_info: 0x120
-  __TEXT.__eh_frame: 0x48
+  __TEXT.__oslogstring: 0x92
+  __TEXT.__unwind_info: 0x170
+  __TEXT.__eh_frame: 0x88
   __TEXT.__objc_classname: 0x8
-  __TEXT.__objc_methname: 0x101
-  __TEXT.__objc_methtype: 0x11
-  __TEXT.__objc_stubs: 0x40
-  __DATA_CONST.__got: 0x48
+  __TEXT.__objc_methname: 0x192
+  __TEXT.__objc_methtype: 0x2c
+  __TEXT.__objc_stubs: 0xa0
+  __DATA_CONST.__got: 0x80
   __DATA_CONST.__const: 0xd0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x60
-  __AUTH_CONST.__auth_got: 0x1c8
+  __DATA_CONST.__objc_selrefs: 0x90
+  __AUTH_CONST.__auth_got: 0x2c8
   __AUTH_CONST.__const: 0x1b0
-  __AUTH_CONST.__cfstring: 0xa0
+  __AUTH_CONST.__cfstring: 0x100
   __AUTH_CONST.__objc_const: 0x190
   __AUTH.__objc_data: 0x148
   __AUTH.__data: 0x28
-  __DATA.__data: 0x50
+  __DATA.__data: 0x80
   __DATA.__bss: 0x230
+  __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0xb0
   __DATA_DIRTY.__data: 0x30
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: EC3587E5-F131-3892-A69E-3D56446F010C
-  Functions: 72
-  Symbols:   159
-  CStrings:  43
+  UUID: 763C4510-9FB4-37F5-BD3E-99BC93C46295
+  Functions: 93
+  Symbols:   212
+  CStrings:  68
 
Symbols:
+ +[_BEUtil checkEligibility]
+ +[_BEUtil checkEligibility].cold.1
+ +[_BEUtil checkEligibility].cold.2
+ +[_BEUtil checkEligibility].cold.3
+ +[_BEUtil currentProcessIsPlatformBinary]
+ +[_BEUtil setEligibilityForTesting:]
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSException
+ _SecTaskCreateFromSelf
+ _SecTaskGetCodeSignStatus
+ ___assert_rtn
+ ___swift_allocate_value_buffer
+ ___swift_project_value_buffer
+ __os_log_error_impl
+ __os_log_impl
+ __swiftEmptyDictionarySingleton
+ _abort
+ _kCFAllocatorDefault
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$currentProcessIsPlatformBinary
+ _objc_msgSend$exceptionWithName:reason:userInfo:
+ _objc_msgSend$raise
+ _objc_retain_x2
+ _os_eligibility_get_domain_answer
+ _os_log_create
+ _os_log_type_enabled
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _s_cachedEligibility
+ _s_cachedEligibilitySet
+ _s_eligibilityForTesting
+ _s_eligibilityForTestingSet
+ _s_eligibilityLock
+ _swift_beginAccess
+ _swift_endAccess
+ _swift_getErrorValue
+ _swift_initStackObject
+ _swift_retain
+ _swift_setDeallocating
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _symbolic SS_ypt
+ _symbolic _____ySS_yptG s23_ContiguousArrayStorageC
+ _symbolic _____ySSypG s18_DictionaryStorageC
CStrings:
+ "+[_BEUtil checkEligibility]"
+ "B16@0:8"
+ "BEUtil.m"
+ "BrowserEngineCore/BEUtil_Internal.swift"
+ "BrowserEngineKitOperationNotPermitted"
+ "Crashing due to unsanctioned BrowserEngineKit operation in an ineligible context."
+ "Failed to retrieve eligibility answer for provided domain."
+ "This operation occurred in an ineligible context."
+ "This operation was forced to execute in an ineligible context."
+ "Unexpected eligibility check error in BEAudioSession init: "
+ "cachedEligibility"
+ "checkEligibility"
+ "com.apple.browserEngineKit"
+ "com.apple.security.get-task-allow"
+ "currentProcessIsPlatformBinary"
+ "exceptionWithName:reason:userInfo:"
+ "general"
+ "initWithDomain:code:userInfo:"
+ "raise"
+ "setEligibilityForTesting:"
+ "v20@0:8B16"

```
