## SafariShared

> `/System/Library/PrivateFrameworks/SafariShared.framework/SafariShared`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-625.2.4.1.0
-  __TEXT.__text: 0x2a1d3c
+625.2.5.10.1
+  __TEXT.__text: 0x2a442c
   __TEXT.__objc_methlist: 0x1617c
-  __TEXT.__const: 0xa3734
+  __TEXT.__const: 0xa3854
   __TEXT.__gcc_except_tab: 0x1ebe0
   __TEXT.__cstring: 0x23827
   __TEXT.__ustring: 0xcec0
-  __TEXT.__oslogstring: 0x15ce2
+  __TEXT.__oslogstring: 0x15cc2
   __TEXT.__dlopen_cstrs: 0x2b7
-  __TEXT.__swift5_typeref: 0x368a
-  __TEXT.__swift5_fieldmd: 0x1884
-  __TEXT.__constg_swiftt: 0x2144
-  __TEXT.__swift5_builtin: 0x140
-  __TEXT.__swift5_reflstr: 0x1638
+  __TEXT.__swift5_typeref: 0x36ca
+  __TEXT.__swift5_fieldmd: 0x18c4
+  __TEXT.__constg_swiftt: 0x21c0
+  __TEXT.__swift5_builtin: 0x190
+  __TEXT.__swift5_reflstr: 0x1668
   __TEXT.__swift5_assocty: 0x450
   __TEXT.__swift5_protos: 0x38
   __TEXT.__swift5_proto: 0x400
-  __TEXT.__swift5_types: 0x194
-  __TEXT.__swift5_capture: 0x1010
-  __TEXT.__swift_as_entry: 0x180
-  __TEXT.__swift_as_ret: 0x168
-  __TEXT.__swift_as_cont: 0x2ec
-  __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__unwind_info: 0x11420
-  __TEXT.__eh_frame: 0x54e0
+  __TEXT.__swift5_types: 0x1a0
+  __TEXT.__swift5_capture: 0x1154
+  __TEXT.__swift5_mpenum: 0x30
+  __TEXT.__swift_as_entry: 0x184
+  __TEXT.__swift_as_ret: 0x16c
+  __TEXT.__swift_as_cont: 0x2f0
+  __TEXT.__unwind_info: 0x114c0
+  __TEXT.__eh_frame: 0x5590
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x165a8
+  __DATA_CONST.__const: 0x16630
   __DATA_CONST.__objc_classlist: 0xcb8
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x2c8

   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x960
   __DATA_CONST.__objc_arraydata: 0xb00
-  __DATA_CONST.__got: 0x2028
-  __AUTH_CONST.__const: 0xb440
+  __DATA_CONST.__got: 0x2120
+  __AUTH_CONST.__const: 0xb4f0
   __AUTH_CONST.__cfstring: 0x1b0c0
   __AUTH_CONST.__objc_const: 0x285f8
   __AUTH_CONST.__weak_auth_got: 0x28

   __AUTH_CONST.__objc_arrayobj: 0x360
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__objc_doubleobj: 0xa0
-  __AUTH_CONST.__auth_got: 0x2bd0
+  __AUTH_CONST.__auth_got: 0x2d70
   __AUTH.__objc_data: 0x7c78
-  __AUTH.__data: 0x17a0
+  __AUTH.__data: 0x1798
   __DATA.__objc_ivar: 0x1940
-  __DATA.__data: 0x5778
+  __DATA.__data: 0x57c8
   __DATA.__common: 0xa0
   __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__bss: 0x9

   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /System/Library/PrivateFrameworks/UnilogCommonLibrary.framework/UnilogCommonLibrary
   - /System/Library/PrivateFrameworks/UnilogInstrumentation.framework/UnilogInstrumentation
+  - /System/Library/PrivateFrameworks/UnilogSafariFeatureLibrary.framework/UnilogSafariFeatureLibrary
   - /System/Library/PrivateFrameworks/UnilogSafariSearchLibrary.framework/UnilogSafariSearchLibrary
   - /System/Library/PrivateFrameworks/UsageTracking.framework/UsageTracking
   - /usr/lib/libCTGreenTeaLogger.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 14807
-  Symbols:   23780
+  Functions: 14790
+  Symbols:   23790
   CStrings:  6158
 
Symbols:
+ ___swift_closure_destructor.246Tm
+ _symbolic _____ 12SafariShared24WBSUsageRetentionVariantO
+ _symbolic _____ So30WBSUsageRetentionExtensionTypeV
+ _symbolic _____ So33WBSUsageRetentionAutoFillCategoryV
+ _symbolic _____ So34WBSUsageRetentionPrivacyReportKindV
+ _symbolic _____Sg 26UnilogSafariFeatureLibrary0C5EventV12PayloadUnionO
+ _symbolic _____Sg 26UnilogSafariFeatureLibrary13ExtensionTypeO
+ _symbolic _____Sg 26UnilogSafariFeatureLibrary16AutoFillCategoryO
+ _symbolic _____Sg 26UnilogSafariFeatureLibrary17PrivacyReportTypeO
+ _symbolic _____Sg 26UnilogSafariFeatureLibrary7TriggerO
CStrings:
+ "8625.2.5.10.1"
+ "Donating feature usage: %{public}s/%{public}s%{public}s x%{public}ld"
+ "Donating settings snapshot: nonDefaultProfile=%{bool,public}d iCloudTabs=%{bool,public}d sync=%{bool,public}d extensions=%{bool,public}d"
+ "Pruned donated feature events since %{public}s."
- "8625.2.4.1"
- "Pending feature usage donation: %{public}s/%{public}s%{public}s x%{public}ld"
- "Pending prune of donated feature events since %{public}s."
- "Pending settings snapshot donation: nonDefaultProfile=%{bool,public}d iCloudTabs=%{bool,public}d sync=%{bool,public}d extensions=%{bool,public}d"
```
