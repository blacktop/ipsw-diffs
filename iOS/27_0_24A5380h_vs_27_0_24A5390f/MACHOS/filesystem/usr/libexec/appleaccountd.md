## appleaccountd

> `/usr/libexec/appleaccountd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_acfuncs`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_data`
- `__DATA.__objc_stublist`
- `__DATA.__common`

```diff

-1063.1.0.0.0
-  __TEXT.__text: 0x3edc54
+1064.0.0.0.0
+  __TEXT.__text: 0x3ef6b0
   __TEXT.__auth_stubs: 0x37d0
-  __TEXT.__objc_stubs: 0x4cc0
+  __TEXT.__objc_stubs: 0x4d00
   __TEXT.__objc_methlist: 0xf80
-  __TEXT.__objc_methname: 0x7705
-  __TEXT.__objc_classname: 0x2e6d
-  __TEXT.__cstring: 0x4579
-  __TEXT.__objc_methtype: 0x2014
+  __TEXT.__objc_methname: 0x7795
+  __TEXT.__objc_classname: 0x2e9d
+  __TEXT.__cstring: 0x4599
+  __TEXT.__objc_methtype: 0x2024
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x13230
-  __TEXT.__constg_swiftt: 0xc4f8
-  __TEXT.__swift5_typeref: 0x7893
+  __TEXT.__const: 0x133b0
+  __TEXT.__constg_swiftt: 0xc578
+  __TEXT.__swift5_typeref: 0x7921
   __TEXT.__swift5_builtin: 0x2bc
-  __TEXT.__swift5_reflstr: 0x6685
-  __TEXT.__swift5_fieldmd: 0x65b8
+  __TEXT.__swift5_reflstr: 0x66b5
+  __TEXT.__swift5_fieldmd: 0x660c
   __TEXT.__swift5_assocty: 0x950
-  __TEXT.__swift5_proto: 0xc6c
-  __TEXT.__swift5_types: 0x630
-  __TEXT.__swift5_capture: 0x6520
-  __TEXT.__oslogstring: 0x2081d
-  __TEXT.__swift5_protos: 0x220
-  __TEXT.__swift_as_entry: 0x664
-  __TEXT.__swift_as_ret: 0x86c
-  __TEXT.__swift_as_cont: 0x11b4
+  __TEXT.__swift5_proto: 0xc7c
+  __TEXT.__swift5_types: 0x638
+  __TEXT.__swift5_capture: 0x654c
+  __TEXT.__oslogstring: 0x2095d
+  __TEXT.__swift5_protos: 0x224
+  __TEXT.__swift_as_entry: 0x674
+  __TEXT.__swift_as_ret: 0x884
+  __TEXT.__swift_as_cont: 0x11d0
   __TEXT.__swift5_acfuncs: 0xb4
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x8480
-  __TEXT.__eh_frame: 0x1464c
-  __DATA_CONST.__const: 0x13d28
-  __DATA_CONST.__objc_classlist: 0x5f8
+  __TEXT.__unwind_info: 0x84f0
+  __TEXT.__eh_frame: 0x147c4
+  __DATA_CONST.__const: 0x13e40
+  __DATA_CONST.__objc_classlist: 0x600
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x1a0
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__auth_got: 0x1bf0
   __DATA_CONST.__got: 0x1570
-  __DATA_CONST.__auth_ptr: 0x1668
-  __DATA.__objc_const: 0x1dd08
-  __DATA.__objc_selrefs: 0x1700
+  __DATA_CONST.__auth_ptr: 0x1670
+  __DATA.__objc_const: 0x1dde0
+  __DATA.__objc_selrefs: 0x1710
   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x3348
-  __DATA.__data: 0x14200
+  __DATA.__data: 0x142c0
   __DATA.__objc_stublist: 0x68
-  __DATA.__bss: 0x13a00
+  __DATA.__bss: 0x13b80
   __DATA.__common: 0x4b8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10200
+  Functions: 10230
   Symbols:   1814
-  CStrings:  4152
+  CStrings:  4164
 
CStrings:
+ "Cache invalidated for account: %{private,mask.hash}s"
+ "Caller-initiated force refresh, bypassing cache reads (writes %s)"
+ "Device list cache enabled via internal override"
+ "Device list cache verdict from URL bag: %{bool}d"
+ "Failed to deserialize account data: account or identifier is nil"
+ "Feature flag disabled, bypassing cache"
+ "Skipping cache write — kill switch engaged"
+ "_TtC13appleaccountd26DeviceListCacheFeatureFlag"
+ "deviceListCacheEnabledWithCompletion:"
+ "featureFlag"
+ "isDeviceListCacheEnabled"
+ "provideDeviceList rejected account with nil identifier"
+ "provideDeviceList-cacheMiss"
+ "provideDeviceList-flagDisabled"
+ "resolvedVerdict"
+ "v12@?0B8"
- "Cache invalidated for account: %{private,mask.hash}@"
- "Failed to deserialize account data: account is nil"
- "Force refresh requested, bypassing cache"
- "provideDeviceList-cached"
```
