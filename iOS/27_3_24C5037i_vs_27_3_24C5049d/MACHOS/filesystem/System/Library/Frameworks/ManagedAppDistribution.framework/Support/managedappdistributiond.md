## managedappdistributiond

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-4.2.3.0.0
-  __TEXT.__text: 0x6a6070
-  __TEXT.__auth_stubs: 0x7090
+4.2.6.0.0
+  __TEXT.__text: 0x6a844c
+  __TEXT.__auth_stubs: 0x70a0
   __TEXT.__objc_stubs: 0x48e0
   __TEXT.__objc_methlist: 0x1424
-  __TEXT.__const: 0x400e0
+  __TEXT.__const: 0x400f0
   __TEXT.__swift5_entry: 0x8
   __TEXT.__gcc_except_tab: 0x220
-  __TEXT.__cstring: 0xfe0d
+  __TEXT.__cstring: 0xfddd
   __TEXT.__objc_classname: 0x1db6
   __TEXT.__objc_methtype: 0x18e5
   __TEXT.__dlopen_cstrs: 0xc8
   __TEXT.__objc_methname: 0x6af5
   __TEXT.__constg_swiftt: 0x75e0
-  __TEXT.__swift5_typeref: 0x651c
-  __TEXT.__oslogstring: 0x16022
+  __TEXT.__swift5_typeref: 0x6538
+  __TEXT.__oslogstring: 0x160a2
   __TEXT.__swift5_proto: 0x19f0
   __TEXT.__swift5_types: 0xa80
   __TEXT.__swift_as_entry: 0xc4c
   __TEXT.__swift_as_ret: 0x1a10
   __TEXT.__swift_as_cont: 0x3608
   __TEXT.__swift5_protos: 0x88
-  __TEXT.__unwind_info: 0x146d8
-  __TEXT.__eh_frame: 0x3a798
+  __TEXT.__unwind_info: 0x146e0
+  __TEXT.__eh_frame: 0x3a778
   __DATA_CONST.__const: 0x2f5d0
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_classlist: 0x300
   __DATA_CONST.__objc_protolist: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xc8
-  __DATA_CONST.__auth_got: 0x3858
+  __DATA_CONST.__auth_got: 0x3860
   __DATA_CONST.__got: 0x1f78
-  __DATA_CONST.__auth_ptr: 0x1ae8
+  __DATA_CONST.__auth_ptr: 0x1ae0
   __DATA.__objc_const: 0x6f08
   __DATA.__objc_selrefs: 0x1800
   __DATA.__objc_data: 0x1ea0
-  __DATA.__data: 0x10f80
+  __DATA.__data: 0x10f90
   __DATA.__common: 0xef8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AdAttributionKit.framework/AdAttributionKit

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 16717
-  Symbols:   3271
+  Functions: 16722
+  Symbols:   3272
   CStrings:  4098
 
Symbols:
+ _$s10Foundation3URLV4pathSSvg
CStrings:
+ "Cannot request %{public}s transaction reporting token: %{public}s has third party distributor info but no itemID"
+ "Using production for %{public}s transaction reporting token: %{public}s is a third party marketplace app with itemID:%{public}@"
+ "Using sandbox for %{public}s transaction reporting token: %{public}s is a profile validated development build"
- "ManagedAppDistributionDaemon/Dependencies.swift"
- "Transaction reporting token request %{public}s called for 3rd party marketplace app with bundleID:%{public}s itemID:%{public}@"
- "Transaction reporting token request %{public}s called for Xcode built app with bundleID:%{public}s"
```
