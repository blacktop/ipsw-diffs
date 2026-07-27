## storekitagent

> `/System/Library/Frameworks/StoreKit.framework/Support/storekitagent`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__got`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_classrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__bss`
- `__DATA.__common`

```diff

-815.6.3.0.0
-  __TEXT.__text: 0x4fd418
-  __TEXT.__auth_stubs: 0x3ed0
+815.6.5.0.0
+  __TEXT.__text: 0x504db4
+  __TEXT.__auth_stubs: 0x3ef0
   __TEXT.__objc_stubs: 0xd840
   __TEXT.__objc_methlist: 0x8570
-  __TEXT.__const: 0x4b790
-  __TEXT.__cstring: 0x157d3
+  __TEXT.__const: 0x4b820
+  __TEXT.__cstring: 0x15f53
   __TEXT.__oslogstring: 0xa4fe
   __TEXT.__objc_classname: 0x27a7
   __TEXT.__objc_methname: 0x1361d
-  __TEXT.__objc_methtype: 0x44e2
+  __TEXT.__objc_methtype: 0x44d2
   __TEXT.__gcc_except_tab: 0x21bc
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x6f18
-  __TEXT.__swift5_typeref: 0x7c11
-  __TEXT.__swift5_reflstr: 0x502f
-  __TEXT.__swift5_fieldmd: 0x86c4
+  __TEXT.__constg_swiftt: 0x6f40
+  __TEXT.__swift5_typeref: 0x7c3d
+  __TEXT.__swift5_reflstr: 0x505f
+  __TEXT.__swift5_fieldmd: 0x8710
   __TEXT.__swift5_builtin: 0x2e4
   __TEXT.__swift5_assocty: 0x11c0
   __TEXT.__swift5_proto: 0x1d4c
-  __TEXT.__swift5_types: 0x9a4
-  __TEXT.__swift5_capture: 0x5630
-  __TEXT.__swift_as_entry: 0xa24
-  __TEXT.__swift_as_ret: 0x11a0
+  __TEXT.__swift5_types: 0x9a8
+  __TEXT.__swift5_capture: 0x56b4
+  __TEXT.__swift_as_entry: 0xa3c
+  __TEXT.__swift_as_ret: 0x11e0
   __TEXT.__swift5_mpenum: 0x60
   __TEXT.__swift5_protos: 0x60
-  __TEXT.__unwind_info: 0x10490
-  __TEXT.__eh_frame: 0x23cf8
-  __DATA_CONST.__auth_got: 0x1f78
+  __TEXT.__unwind_info: 0x10638
+  __TEXT.__eh_frame: 0x243d0
+  __DATA_CONST.__auth_got: 0x1f88
   __DATA_CONST.__got: 0xe40
-  __DATA_CONST.__auth_ptr: 0x12b8
-  __DATA_CONST.__const: 0x312d0
+  __DATA_CONST.__auth_ptr: 0x12c0
+  __DATA_CONST.__const: 0x31480
   __DATA_CONST.__cfstring: 0x5d60
   __DATA_CONST.__objc_classlist: 0x6a0
   __DATA_CONST.__objc_catlist: 0xa0

   __DATA.__objc_selrefs: 0x4818
   __DATA.__objc_ivar: 0x6a8
   __DATA.__objc_data: 0x57f0
-  __DATA.__data: 0xee48
+  __DATA.__data: 0xeed8
   __DATA.__bss: 0x391f8
   __DATA.__common: 0xe70
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 22984
-  Symbols:   1664
-  CStrings:  6839
+  Functions: 23128
+  Symbols:   1666
+  CStrings:  6875
 
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
+ "21:07:25"
+ "Error retrieving short bundle version: "
+ "Jul 11 2026"
+ "[ReviewManager] Creating database entry for review token"
+ "[ReviewManager] Fetching review constants from bag"
+ "[ReviewManager] Generating review token for bundle: "
+ "[ReviewManager] Querying review entries for bundle: "
+ "[ReviewManager] Retrieved "
+ "[ReviewManager] Successfully generated review token: "
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
+ "com.apple.storekit.StoreKitPushSyncHandler"
- "07:42:54"
- "Jun 17 2026"
- "[ReviewManager] Review requests are not allowed in seed."
```
