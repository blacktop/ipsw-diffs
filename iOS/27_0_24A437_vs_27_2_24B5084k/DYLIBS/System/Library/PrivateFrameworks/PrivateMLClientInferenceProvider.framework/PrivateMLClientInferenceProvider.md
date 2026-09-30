## PrivateMLClientInferenceProvider

> `/System/Library/PrivateFrameworks/PrivateMLClientInferenceProvider.framework/PrivateMLClientInferenceProvider`

```diff

-215.2.0.0.0
-  __TEXT.__text: 0x90844
-  __TEXT.__const: 0x1ff8
+218.5.0.0.0
+  __TEXT.__text: 0x9a2f8
+  __TEXT.__const: 0x1fe8
   __TEXT.__constg_swiftt: 0x68c
-  __TEXT.__swift5_typeref: 0xb6e
+  __TEXT.__swift5_typeref: 0xba2
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_reflstr: 0xc2f
   __TEXT.__swift5_fieldmd: 0x938
   __TEXT.__swift5_types: 0x78
-  __TEXT.__cstring: 0xe6b
-  __TEXT.__oslogstring: 0x3e8b
+  __TEXT.__cstring: 0xef1
+  __TEXT.__oslogstring: 0x3f1b
   __TEXT.__swift5_assocty: 0x138
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_proto: 0xfc
-  __TEXT.__swift_as_entry: 0x104
-  __TEXT.__swift_as_cont: 0x24c
-  __TEXT.__swift5_capture: 0x7ac
-  __TEXT.__swift_as_ret: 0x110
+  __TEXT.__swift_as_entry: 0x10c
+  __TEXT.__swift_as_cont: 0x270
+  __TEXT.__swift5_capture: 0x7b4
+  __TEXT.__swift_as_ret: 0x124
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0xff0
-  __TEXT.__eh_frame: 0x2b48
+  __TEXT.__unwind_info: 0x11a8
+  __TEXT.__eh_frame: 0x2f78
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__const: 0x98
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe0
+  __DATA_CONST.__objc_selrefs: 0xb8
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x1a38
+  __AUTH_CONST.__const: 0x1a60
   __AUTH_CONST.__objc_const: 0x720
-  __AUTH_CONST.__auth_got: 0x1ac8
+  __AUTH_CONST.__auth_got: 0x1ca8
   __AUTH.__objc_data: 0xf0
   __AUTH.__data: 0x620
-  __DATA.__data: 0x518
-  __DATA.__common: 0x8
+  __DATA.__data: 0x560
+  __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__data: 0x920
+  __DATA_DIRTY.__data: 0x8e8
   __DATA_DIRTY.__common: 0x20
   __DATA_DIRTY.__bss: 0x300
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 960
-  Symbols:   554
-  CStrings:  388
+  Functions: 1044
+  Symbols:   549
+  CStrings:  395
 
Symbols:
+ ___swift_closure_destructor.37Tm
+ ___swift_closure_destructor.41Tm
+ ___swift_closure_destructor.55Tm
+ ___swift_closure_destructor.7Tm
+ ___swift_destroy_boxed_opaque_existential_0Tm
+ __swiftEmptySetSingleton
+ _objc_retain_x23
+ _symbolic _____Sg 20ModelManagerServices10ClientDataV
+ _symbolic _____XDXMT 32PrivateMLClientInferenceProvider03NewcD0C
+ _symbolic ___________t 29GenerativeFunctionsFoundation0A5ErrorV06PromptD0V0D4TypeO0e17InjectionRejectedD4InfoV 15TokenGeneration0jkD0O7ContextV
+ _symbolic _____ySSG s11_SetStorageC
+ _symbolic _____ySS_____G s18_DictionaryStorageC 15PrivateMLClient30Tie_CloudGuardrailsInputPolicyV26UntrustedToolResultContentV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 29GenerativeFunctionsFoundation0D5ErrorV06PromptG0V0G4TypeO0h17InjectionRejectedG4InfoV17UnverifiedContentV
- _OBJC_CLASS_$_RBSAssertion
- _OBJC_CLASS_$_RBSAttribute
- _OBJC_CLASS_$_RBSDomainAttribute
- _OBJC_CLASS_$_RBSTarget
- ___swift_closure_destructor.140Tm
- ___swift_closure_destructor.185Tm
- ___swift_closure_destructor.19Tm
- _objc_msgSend$acquireWithError:
- _objc_msgSend$attributeWithDomain:name:
- _objc_msgSend$currentProcess
- _objc_msgSend$initWithExplanation:target:attributes:
- _objc_msgSend$invalidate
- _objc_retain_x19
- _objc_retain_x21
- _objc_retain_x24
- _swift_deallocBox
- _symbolic _____yyXlG s23_ContiguousArrayStorageC
- _symbolic _____z_Xx 15TokenGeneration23StreamingRequestPayloadO
CStrings:
+ " requestOneShot replay write"
+ " requestOneShot transparency reporter"
+ " requestStream replay write"
+ " streaming replay write"
+ "%s donation locale source: %{public}s count: %{public}ld"
+ "%s failed to materialize image surfaces for request payload: %@"
+ "%s failed to materialize image surfaces for streaming payload: %@"
+ "%s max tokens not set will be overridden."
+ "%s prewarm failed. sessionUUID=%s modelBundleIdentifier=%s featureIdentifier=%s bundleIdentifier=%s error=%@"
+ "%{private}s failed due to prompt injection rejection"
+ "%{public}s"
+ "Dropping incomplete media candidate; no last chunk received. media_id=%{private}s"
+ "Prompt injection rejected: "
+ "cloudGuardrailsEnvelope: unrecognized untrusted-content case, sending no IPI coverage"
+ "networkPayload"
+ "none (donation will use the device locale)"
+ "sessionHint status `terminated` failed for sessionID:%s"
- "%s max tokens not set will be overriden."
- "%s prewarm failed. sessionUUID=%s modelBundleIdentifier=%s featureIdentifier=%s bundleIdentifier=%s"
- "%s: Failed to acquire RBS assertion for requestOneShot replay write: %@"
- "%s: Failed to acquire RBS assertion for requestOneShot transparency reporter: %@"
- "%s: Failed to acquire RBS assertion for requestStream replay write: %@"
- "%s: Failed to acquire RBS assertion for streaming replay write: %@"
- "FinishTaskUninterruptable"
- "PrivateMLClient post-request tasks"
- "com.apple.common"
- "sessionHint status `terminated` failed for sessionID:%s "
```
