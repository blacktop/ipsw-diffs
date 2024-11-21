## transparencyd

> `/usr/libexec/transparencyd`

```diff

-1218.60.64.0.0
-  __TEXT.__text: 0x2133cc
+1218.60.67.0.0
+  __TEXT.__text: 0x213d9c
   __TEXT.__auth_stubs: 0x2df0
   __TEXT.__objc_stubs: 0x1b360
   __TEXT.__objc_methlist: 0x125fc
-  __TEXT.__cstring: 0x11030
+  __TEXT.__cstring: 0x11120
   __TEXT.__objc_classname: 0x2bb9
   __TEXT.__objc_methname: 0x21535
-  __TEXT.__objc_methtype: 0x6fd6
+  __TEXT.__objc_methtype: 0x6fca
   __TEXT.__const: 0x5fb8
-  __TEXT.__gcc_except_tab: 0x4b04
-  __TEXT.__oslogstring: 0x10a82
+  __TEXT.__gcc_except_tab: 0x4b44
+  __TEXT.__oslogstring: 0x10af2
   __TEXT.__swift5_typeref: 0x19c0
   __TEXT.__swift5_reflstr: 0xeda
   __TEXT.__swift5_assocty: 0x2d0
-  __TEXT.__constg_swiftt: 0x2230
-  __TEXT.__swift5_fieldmd: 0x1600
+  __TEXT.__constg_swiftt: 0x223c
+  __TEXT.__swift5_fieldmd: 0x160c
   __TEXT.__swift5_proto: 0x410
   __TEXT.__swift5_types: 0x1a4
-  __TEXT.__swift5_capture: 0xd74
+  __TEXT.__swift5_capture: 0xd78
   __TEXT.__swift5_builtin: 0xa0
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x8328
+  __TEXT.__unwind_info: 0x8340
   __TEXT.__eh_frame: 0x3438
   __DATA_CONST.__auth_got: 0x1708
-  __DATA_CONST.__got: 0xe20
-  __DATA_CONST.__auth_ptr: 0x538
-  __DATA_CONST.__const: 0x14060
-  __DATA_CONST.__cfstring: 0xd820
+  __DATA_CONST.__got: 0xe28
+  __DATA_CONST.__auth_ptr: 0x548
+  __DATA_CONST.__const: 0x14088
+  __DATA_CONST.__cfstring: 0xd8c0
   __DATA_CONST.__objc_classlist: 0xc50
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x390

   __DATA_CONST.__objc_arraydata: 0x1b0
   __DATA_CONST.__objc_dictobj: 0x118
   __DATA_CONST.__objc_arrayobj: 0x1e0
-  __DATA.__objc_const: 0x302c8
+  __DATA.__objc_const: 0x302a0
   __DATA.__objc_selrefs: 0x7f20
   __DATA.__objc_ivar: 0x1068
-  __DATA.__objc_data: 0x8ea0
+  __DATA.__objc_data: 0x8ef0
   __DATA.__data: 0x84b8
   __DATA.__thread_vars: 0x48
   __DATA.__thread_bss: 0xc
-  __DATA.__bss: 0x8e28
-  __DATA.__common: 0x3d8
+  __DATA.__bss: 0x8e38
+  __DATA.__common: 0x3e0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 12192
-  Symbols:   1350
-  CStrings:  11213
+  Functions: 12199
+  Symbols:   1351
+  CStrings:  11221
 
Symbols:
+ _kTransparencyAnalyticsEventOptIn
CStrings:
+ "Failure found for element %{public}s when checking on-by-default eligibility"
+ "Invalid sample range"
+ "KTEligibilityStatusReporting"
+ "No CloudKit, can't opt out"
+ "No entries for given element %{public}s. Returning aggregate result of false"
+ "No success in the last sample for element %{public}s. Returning aggregate result of false"
+ "Present rate of %f is too low for element %{public}s. Returning aggregate result of false"
+ "cdp"
+ "com.apple.Transparency.EligibilityDB"
+ "com.apple.transparency.eligibilityCLIQueue"
+ "newState"
+ "transparencydEligibilityMultiSampler"
+ "v44@0:8@\"NSString\"16@\"NSArray\"24B32@?<v@?@\"NSError\">36"
- "No entries for given element %s. Returning aggregate result of false"
- "No success in the last sample. Returning aggregate result of false"
- "Present rate of %f is too low. Returning aggregate result of false"

```
