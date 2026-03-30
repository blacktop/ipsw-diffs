## storekitd

> `/System/Library/Frameworks/StoreKit.framework/Support/storekitd`

```diff

-815.4.22.2.3
-  __TEXT.__text: 0x416654
-  __TEXT.__auth_stubs: 0x3f40
-  __TEXT.__objc_stubs: 0xe3e0
+815.5.2.0.0
+  __TEXT.__text: 0x40dc70
+  __TEXT.__auth_stubs: 0x3f20
+  __TEXT.__objc_stubs: 0xe380
   __TEXT.__objc_methlist: 0x875c
-  __TEXT.__const: 0x32b50
-  __TEXT.__cstring: 0x16a0a
+  __TEXT.__const: 0x32a80
+  __TEXT.__cstring: 0x1617a
   __TEXT.__oslogstring: 0xb472
   __TEXT.__objc_classname: 0x2593
-  __TEXT.__objc_methname: 0x13f8d
-  __TEXT.__objc_methtype: 0x45f8
+  __TEXT.__objc_methname: 0x13f5d
+  __TEXT.__objc_methtype: 0x45c8
   __TEXT.__gcc_except_tab: 0x2458
   __TEXT.__dlopen_cstrs: 0x68
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x6f38
-  __TEXT.__swift5_typeref: 0x7c3f
+  __TEXT.__constg_swiftt: 0x6ef4
+  __TEXT.__swift5_typeref: 0x7bcd
   __TEXT.__swift5_builtin: 0x2e4
-  __TEXT.__swift5_reflstr: 0x4fe0
-  __TEXT.__swift5_fieldmd: 0x86d8
+  __TEXT.__swift5_reflstr: 0x4ff0
+  __TEXT.__swift5_fieldmd: 0x8688
   __TEXT.__swift5_assocty: 0x11d8
-  __TEXT.__swift5_proto: 0x1da8
-  __TEXT.__swift5_types: 0x9b4
-  __TEXT.__swift5_capture: 0x5838
-  __TEXT.__swift_as_entry: 0xaac
-  __TEXT.__swift_as_ret: 0x1288
+  __TEXT.__swift5_proto: 0x1d9c
+  __TEXT.__swift5_types: 0x9ac
+  __TEXT.__swift5_capture: 0x57b0
+  __TEXT.__swift_as_entry: 0xa94
+  __TEXT.__swift_as_ret: 0x124c
   __TEXT.__swift5_mpenum: 0x60
   __TEXT.__swift5_protos: 0x60
-  __TEXT.__unwind_info: 0x10a08
-  __TEXT.__eh_frame: 0x253f0
-  __DATA_CONST.__auth_got: 0x1fb0
-  __DATA_CONST.__got: 0xf80
-  __DATA_CONST.__auth_ptr: 0x1310
-  __DATA_CONST.__const: 0x2a020
+  __TEXT.__unwind_info: 0x10760
+  __TEXT.__eh_frame: 0x24c38
+  __DATA_CONST.__auth_got: 0x1fa0
+  __DATA_CONST.__got: 0xf78
+  __DATA_CONST.__auth_ptr: 0x12f8
+  __DATA_CONST.__const: 0x29d80
   __DATA_CONST.__cfstring: 0x5ee0
   __DATA_CONST.__objc_classlist: 0x6a0
   __DATA_CONST.__objc_catlist: 0xa0

   __DATA_CONST.__objc_intobj: 0x210
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA.__objc_const: 0x1f3a8
-  __DATA.__objc_selrefs: 0x4a18
+  __DATA.__objc_selrefs: 0x4a00
   __DATA.__objc_ivar: 0x6f0
   __DATA.__objc_data: 0x56b8
-  __DATA.__data: 0xeec0
-  __DATA.__bss: 0x39b28
-  __DATA.__common: 0xeb4
+  __DATA.__data: 0xee00
+  __DATA.__bss: 0x399a8
+  __DATA.__common: 0xeac
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AdAttributionKit.framework/AdAttributionKit
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A0526B7D-8401-3A7D-A093-D203B7083E95
-  Functions: 23552
-  Symbols:   1722
-  CStrings:  7992
+  UUID: 2FA75794-6DB7-3E3B-A9C6-A2F1BB281398
+  Functions: 23393
+  Symbols:   1719
+  CStrings:  7948
 
Symbols:
- _$s10Foundation4DateV12timeInterval5sinceACSd_ACtcfC
- _$s10Foundation4DateV7compareySo18NSComparisonResultVACF
- _LSSystemApplicationType
CStrings:
+ "00:03:49"
+ "Mar 17 2026"
+ "[ReviewManager] Review requests are not allowed in seed."
+ "payOverTimeSubscriptions"
- " existing entries"
- " review entries from database"
- ", latest rating allowed: "
- ", requestsPerWindowLimit: "
- ", requireNewVersionAfterReview: "
- ", requiredDaysAfterReview: "
- "19:01:19"
- "Error retrieving short bundle version: "
- "Mar 19 2026"
- "No additional items to include in product fetch request"
- "[ReviewManager] Creating database entry for review token"
- "[ReviewManager] Failed to check for ad-hoc signing: "
- "[ReviewManager] Fetching review constants from bag"
- "[ReviewManager] Forcing sandbox for ad-hoc signed app"
- "[ReviewManager] Generating review token for bundle: "
- "[ReviewManager] Querying review entries for bundle: "
- "[ReviewManager] Retrieved "
- "[ReviewManager] Successfully generated review token: "
- "[ReviewManager] System: "
- "[ReviewManager] Token generation complete, returning token"
- "[ReviewManager] Using bag value for requestLimitWindow: "
- "] Determining whether to generate review token for bundle: "
- "] Error generating review token: "
- "] Evaluating review eligibility with "
- "] Failed to insert review request entry in database"
- "] Rejecting review request because there is no account."
- "] Retrieved review constants - requestLimitWindow: "
- "] Review request rejected based on eligibility criteria"
- "] Review request rejected because requests per window limit reached."
- "] Review request rejected because the user has already rated this version."
- "] Review request rejected because the user has rated past the last rating allowed date."
- "] Review window: "
- "] Using bag value for requestsPerWindowLimit: "
- "] Using bag value for requireNewVersionAfterReview: "
- "] Using bag value for requiredDaysAfterReview: "
- "] Using default value for requestLimitWindow: "
- "] Using default value for requestsPerWindowLimit: "
- "] Using default value for requireNewVersionAfterReview: "
- "] Using default value for requiredDaysAfterReview: "
- "]: Creating review entry"
- "]: Getting review entries"
- "]: Invalid review entry "
- "additional-product-fetch-query-items"
- "ed1d4075e1d0f393345ed591bae437060d4123c52e791175d8a5cb0c25afa859"
- "isAdHocCodeSigned"
- "shortVersionString"
- "typeForInstallMachinery"
- "v28@?0@\"NSDictionary\"8B16@\"NSError\"20"

```
