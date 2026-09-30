## managedappdistributiond

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-4.1.9.0.0
-  __TEXT.__text: 0x6a24b4
-  __TEXT.__auth_stubs: 0x7070
+4.1.11.0.0
+  __TEXT.__text: 0x6a51ac
+  __TEXT.__auth_stubs: 0x7080
   __TEXT.__objc_stubs: 0x48e0
   __TEXT.__objc_methlist: 0x1424
   __TEXT.__const: 0x40070

   __TEXT.__objc_methname: 0x6af5
   __TEXT.__constg_swiftt: 0x75cc
   __TEXT.__swift5_typeref: 0x651c
-  __TEXT.__oslogstring: 0x15ef2
+  __TEXT.__oslogstring: 0x15f02
   __TEXT.__swift5_proto: 0x19ec
   __TEXT.__swift5_types: 0xa7c
-  __TEXT.__swift_as_entry: 0xc40
-  __TEXT.__swift_as_ret: 0x19f8
-  __TEXT.__swift_as_cont: 0x3584
+  __TEXT.__swift_as_entry: 0xc48
+  __TEXT.__swift_as_ret: 0x1a10
+  __TEXT.__swift_as_cont: 0x35fc
   __TEXT.__swift5_protos: 0x88
-  __TEXT.__unwind_info: 0x14600
-  __TEXT.__eh_frame: 0x3a470
-  __DATA_CONST.__const: 0x2f588
+  __TEXT.__unwind_info: 0x146b0
+  __TEXT.__eh_frame: 0x3a780
+  __DATA_CONST.__const: 0x2f560
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_classlist: 0x300
   __DATA_CONST.__objc_protolist: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xc8
-  __DATA_CONST.__auth_got: 0x3848
-  __DATA_CONST.__got: 0x1f70
+  __DATA_CONST.__auth_got: 0x3850
+  __DATA_CONST.__got: 0x1f78
   __DATA_CONST.__auth_ptr: 0x1ae8
   __DATA.__objc_const: 0x6f08
   __DATA.__objc_selrefs: 0x1800
   __DATA.__objc_data: 0x1ea0
-  __DATA.__data: 0x10f78
+  __DATA.__data: 0x10f90
   __DATA.__common: 0xef8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AdAttributionKit.framework/AdAttributionKit

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 16667
-  Symbols:   3269
+  Functions: 16702
+  Symbols:   3271
   CStrings:  4095
 
Symbols:
+ _$s22ManagedAppDistribution19MessageRegistrationO15isLibraryScopedSbvg
+ _$s22ManagedAppDistribution19MessageRegistrationOs23CustomStringConvertibleAAMc
CStrings:
+ "[%@] Client %{public}s is entitled to no library; refusing registration for %{public}s"
- "[%@] Client %{public}s is entitled to no library; refusing registration"
```
