## fm

> `/usr/bin/fm`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_entry`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-2.2.6.1.0
-  __TEXT.__text: 0x10275c
-  __TEXT.__auth_stubs: 0x3780
-  __TEXT.__objc_stubs: 0x3c0
+2.2.12.2.0
+  __TEXT.__text: 0x104258
+  __TEXT.__auth_stubs: 0x37f0
+  __TEXT.__objc_stubs: 0x3e0
   __TEXT.__objc_methlist: 0x104
-  __TEXT.__const: 0x677c
+  __TEXT.__const: 0x679c
   __TEXT.__constg_swiftt: 0x13ac
-  __TEXT.__swift5_typeref: 0x19f5
+  __TEXT.__swift5_typeref: 0x1a29
   __TEXT.__swift5_builtin: 0x104
   __TEXT.__swift5_reflstr: 0x17a6
   __TEXT.__swift5_fieldmd: 0x1e30
   __TEXT.__swift5_assocty: 0x140
-  __TEXT.__cstring: 0x82ea
+  __TEXT.__cstring: 0x84ca
   __TEXT.__swift5_proto: 0x4c8
   __TEXT.__swift5_types: 0x220
   __TEXT.__swift_as_entry: 0x140

   __TEXT.__objc_methtype: 0xd4
   __TEXT.__oslogstring: 0x18d
   __TEXT.__objc_classname: 0x181
-  __TEXT.__objc_methname: 0xa8b
+  __TEXT.__objc_methname: 0xaab
   __TEXT.__swift5_mpenum: 0x58
   __TEXT.__swift5_capture: 0xa38
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x2be8
-  __TEXT.__eh_frame: 0x5a38
+  __TEXT.__unwind_info: 0x2c08
+  __TEXT.__eh_frame: 0x5aa0
   __DATA_CONST.__const: 0x4490
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__auth_got: 0x1bc8
+  __DATA_CONST.__auth_got: 0x1c00
   __DATA_CONST.__got: 0x868
-  __DATA_CONST.__auth_ptr: 0x970
+  __DATA_CONST.__auth_ptr: 0x978
   __DATA.__objc_const: 0x10d0
-  __DATA.__objc_selrefs: 0x190
+  __DATA.__objc_selrefs: 0x198
   __DATA.__objc_data: 0x140
-  __DATA.__data: 0x30c0
+  __DATA.__data: 0x30e0
   __DATA.__common: 0x480
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2687
-  Symbols:   1356
-  CStrings:  698
+  Functions: 2694
+  Symbols:   1364
+  CStrings:  710
 
Symbols:
+ _$s16FoundationModels32PrivateCloudComputeLanguageModelC10QuotaUsageV23LimitIncreaseSuggestionV4showyyF
+ _$s16FoundationModels32PrivateCloudComputeLanguageModelC10QuotaUsageV23LimitIncreaseSuggestionVMa
+ _$s16FoundationModels32PrivateCloudComputeLanguageModelC10QuotaUsageV23LimitIncreaseSuggestionVMn
+ _$s16FoundationModels32PrivateCloudComputeLanguageModelC10QuotaUsageV23limitIncreaseSuggestionAE05LimitkL0VSgvg
+ _$s16FoundationModels32PrivateCloudComputeLanguageModelC10quotaUsageAC05QuotaI0Vvg
+ __os_feature_enabled_impl
+ _objc_retain_x28
+ _objc_retain_x9
CStrings:
+ "/increase-limit is only available for the PCC model."
+ "/increase-limit is only available for the PCC model. Switch with /model pcc."
+ "FoundationModels"
+ "Increase PCC usage limit"
+ "No usage limit increase is available for this model."
+ "Open the PCC usage limit increase flow"
+ "Opening quota limit increase options."
+ "Opening quota limit increase options…"
+ "PCCMetering"
+ "Run /increase-limit to view options."
+ "Switch with /model pcc."
+ "createFileAtPath:contents:attributes:"
```
