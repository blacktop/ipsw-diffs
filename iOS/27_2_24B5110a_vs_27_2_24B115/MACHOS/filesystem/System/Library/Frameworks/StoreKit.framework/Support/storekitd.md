## storekitd

> `/System/Library/Frameworks/StoreKit.framework/Support/storekitd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

 816.1.16.0.0
-  __TEXT.__text: 0x59de3c
-  __TEXT.__auth_stubs: 0x4370
-  __TEXT.__objc_stubs: 0xc5e0
+  __TEXT.__text: 0x5a70b8
+  __TEXT.__auth_stubs: 0x4390
+  __TEXT.__objc_stubs: 0xc620
   __TEXT.__objc_methlist: 0x7974
-  __TEXT.__const: 0x3f8b0
-  __TEXT.__cstring: 0x1eb45
+  __TEXT.__const: 0x3f930
+  __TEXT.__cstring: 0x1f395
   __TEXT.__oslogstring: 0x69c2
   __TEXT.__objc_classname: 0x269f
-  __TEXT.__objc_methname: 0x11759
+  __TEXT.__objc_methname: 0x11779
   __TEXT.__objc_methtype: 0x4108
   __TEXT.__gcc_except_tab: 0x10a0
   __TEXT.__dlopen_cstrs: 0x68
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x949c
-  __TEXT.__swift5_typeref: 0xbe10
+  __TEXT.__constg_swiftt: 0x94c4
+  __TEXT.__swift5_typeref: 0xbe3c
   __TEXT.__swift5_builtin: 0x334
-  __TEXT.__swift5_reflstr: 0x749f
-  __TEXT.__swift5_fieldmd: 0xcc18
+  __TEXT.__swift5_reflstr: 0x74df
+  __TEXT.__swift5_fieldmd: 0xcc64
   __TEXT.__swift5_assocty: 0x17a0
   __TEXT.__swift5_proto: 0x2d50
-  __TEXT.__swift5_types: 0xda8
-  __TEXT.__swift5_capture: 0x1eff8
-  __TEXT.__swift_as_entry: 0x100c
-  __TEXT.__swift_as_ret: 0x1ed0
-  __TEXT.__swift_as_cont: 0x2f1c
+  __TEXT.__swift5_types: 0xdac
+  __TEXT.__swift5_capture: 0x1f67c
+  __TEXT.__swift_as_entry: 0x1024
+  __TEXT.__swift_as_ret: 0x1f04
+  __TEXT.__swift_as_cont: 0x2f84
   __TEXT.__swift5_mpenum: 0x8c
   __TEXT.__swift5_protos: 0x7c
-  __TEXT.__unwind_info: 0x1a0d0
-  __TEXT.__eh_frame: 0x37808
-  __DATA_CONST.__const: 0x71198
+  __TEXT.__unwind_info: 0x1a738
+  __TEXT.__eh_frame: 0x37ec0
+  __DATA_CONST.__const: 0x72248
   __DATA_CONST.__cfstring: 0x4ec0
   __DATA_CONST.__objc_classlist: 0x628
   __DATA_CONST.__objc_catlist: 0xa8

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_intobj: 0xf0
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__auth_got: 0x21c8
+  __DATA_CONST.__auth_got: 0x21d8
   __DATA_CONST.__got: 0x1088
-  __DATA_CONST.__auth_ptr: 0x18e0
+  __DATA_CONST.__auth_ptr: 0x18f0
   __DATA.__objc_const: 0x1d0e8
-  __DATA.__objc_selrefs: 0x4400
+  __DATA.__objc_selrefs: 0x4410
   __DATA.__objc_ivar: 0x5c8
   __DATA.__objc_data: 0x5218
-  __DATA.__data: 0x13550
+  __DATA.__data: 0x135f0
   __DATA.__common: 0x1080
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AdAttributionKit.framework/AdAttributionKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 38135
-  Symbols:   1815
-  CStrings:  7151
+  Functions: 38381
+  Symbols:   1817
+  CStrings:  7193
 
Symbols:
+ _$s10Foundation4DateV12timeInterval5sinceACSd_ACtcfC
+ _$s10Foundation4DateV7compareySo18NSComparisonResultVACF
CStrings:
+ " existing entries"
+ " review entries from database"
+ ", latest rating allowed: "
+ ", requestsPerWindowLimit: "
+ ", requireNewVersionAfterReview: "
+ ", requiredDaysAfterReview: "
+ "Error retrieving short bundle version: "
+ "UseSandboxReviewPromptModeForSystemApps"
+ "[ReviewManager] Creating database entry for review token"
+ "[ReviewManager] Failed to check for ad-hoc signing: "
+ "[ReviewManager] Fetching review constants from bag"
+ "[ReviewManager] Forcing sandbox for ad-hoc signed app"
+ "[ReviewManager] Forcing sandbox for system app"
+ "[ReviewManager] Generating review token for bundle: "
+ "[ReviewManager] Querying review entries for bundle: "
+ "[ReviewManager] Retrieved "
+ "[ReviewManager] Successfully generated review token: "
+ "[ReviewManager] System: "
+ "[ReviewManager] Token generation complete, returning token"
+ "[ReviewManager] Using bag value for requestLimitWindow: "
+ "] Determining whether to generate review token for bundle: "
+ "] Error generating review token: "
+ "] Evaluating review eligibility with "
+ "] Failed to insert review request entry in database"
+ "] Rejecting review request because there is no account."
+ "] Retrieved review constants - requestLimitWindow: "
+ "] Review request rejected based on eligibility criteria"
+ "] Review request rejected because requests per window limit reached."
+ "] Review request rejected because the user has already rated this version."
+ "] Review request rejected because the user has rated past the last rating allowed date."
+ "] Review window: "
+ "] Using bag value for requestsPerWindowLimit: "
+ "] Using bag value for requireNewVersionAfterReview: "
+ "] Using bag value for requiredDaysAfterReview: "
+ "] Using default value for requestLimitWindow: "
+ "] Using default value for requestsPerWindowLimit: "
+ "] Using default value for requireNewVersionAfterReview: "
+ "] Using default value for requiredDaysAfterReview: "
+ "]: Creating review entry"
+ "]: Getting review entries"
+ "]: Invalid review entry "
+ "isAdHocCodeSigned"
+ "shortVersionString"
- "[ReviewManager] Review requests are not allowed in seed."
```
