## finhealthd

> `/System/Library/PrivateFrameworks/FinHealth.framework/finhealthd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_entry`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`

```diff

-1.9.1.30.0
-  __TEXT.__text: 0xd7b0
-  __TEXT.__auth_stubs: 0xae0
-  __TEXT.__objc_stubs: 0x260
+1.9.2.3.0
+  __TEXT.__text: 0xeab8
+  __TEXT.__auth_stubs: 0xb00
+  __TEXT.__objc_stubs: 0x280
   __TEXT.__objc_methlist: 0x1dc
-  __TEXT.__const: 0x402
+  __TEXT.__const: 0x432
   __TEXT.__swift5_typeref: 0x2d4
-  __TEXT.__swift5_capture: 0x26c
-  __TEXT.__cstring: 0xc7
-  __TEXT.__oslogstring: 0x648
-  __TEXT.__objc_methname: 0x5b2
-  __TEXT.__objc_methtype: 0x217
+  __TEXT.__swift5_capture: 0x27c
+  __TEXT.__cstring: 0xe3
+  __TEXT.__oslogstring: 0x7a8
+  __TEXT.__objc_methname: 0x5f2
+  __TEXT.__objc_methtype: 0x227
   __TEXT.__objc_classname: 0xbb
-  __TEXT.__constg_swiftt: 0x1b4
-  __TEXT.__swift5_reflstr: 0x117
-  __TEXT.__swift5_fieldmd: 0xdc
+  __TEXT.__constg_swiftt: 0x1ac
+  __TEXT.__swift5_reflstr: 0x107
+  __TEXT.__swift5_fieldmd: 0xd0
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_types: 0x14
-  __TEXT.__swift_as_entry: 0x6c
-  __TEXT.__swift_as_ret: 0x78
-  __TEXT.__swift_as_cont: 0xe0
+  __TEXT.__swift_as_entry: 0x74
+  __TEXT.__swift_as_ret: 0x8c
+  __TEXT.__swift_as_cont: 0x104
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x608
-  __TEXT.__eh_frame: 0xf90
-  __DATA_CONST.__const: 0x780
+  __TEXT.__unwind_info: 0x678
+  __TEXT.__eh_frame: 0x11f0
+  __DATA_CONST.__const: 0x7d0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__auth_got: 0x578
+  __DATA_CONST.__auth_got: 0x588
   __DATA_CONST.__got: 0x1b8
-  __DATA_CONST.__auth_ptr: 0xc8
-  __DATA.__objc_const: 0x470
-  __DATA.__objc_selrefs: 0x178
+  __DATA_CONST.__auth_ptr: 0xc0
+  __DATA.__objc_const: 0x450
+  __DATA.__objc_selrefs: 0x180
   __DATA.__objc_data: 0xc8
-  __DATA.__data: 0x488
+  __DATA.__data: 0x478
   __DATA.__common: 0x8
   - /System/Library/Frameworks/FinanceKit.framework/FinanceKit
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 464
+  Functions: 486
   Symbols:   277
-  CStrings:  130
+  CStrings:  137
 
Symbols:
+ _objc_release_x27
+ _swift_retain_x28
- _$s13FinHealthCore0aB11FeatureFlagV0aB8FeaturesO21financekitIntegrationyA2EmFWC
- _swift_deletedAsyncMethodErrorTu
CStrings:
+ "Periodic full sync completed — no grouping-relevant changes"
+ "Periodic full sync completed — triggering grouping recompute"
+ "Periodic full sync failed: %@"
+ "Periodic full sync: BGSystemTask triggered"
+ "Periodic full sync: already ran this lifecycle, skipping"
+ "Periodic full sync: entityGroupWriter failed: %@"
+ "Periodic full sync: incomeInsightWriter failed: %@"
+ "hasRunOvernightSync"
+ "periodic-full-sync"
+ "updateTransactionsAsyncWithForceFullSync:batchSize:completionHandler:"
- "Bypass background group processing"
- "overnightSync"
- "processingRegistration"
```
