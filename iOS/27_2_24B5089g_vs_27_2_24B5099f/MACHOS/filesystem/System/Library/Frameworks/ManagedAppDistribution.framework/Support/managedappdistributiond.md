## managedappdistributiond

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-4.1.11.0.0
-  __TEXT.__text: 0x6a51ac
-  __TEXT.__auth_stubs: 0x7080
+4.1.14.0.0
+  __TEXT.__text: 0x6a6070
+  __TEXT.__auth_stubs: 0x7090
   __TEXT.__objc_stubs: 0x48e0
   __TEXT.__objc_methlist: 0x1424
-  __TEXT.__const: 0x40070
+  __TEXT.__const: 0x400e0
   __TEXT.__swift5_entry: 0x8
   __TEXT.__gcc_except_tab: 0x220
-  __TEXT.__cstring: 0xfdfd
+  __TEXT.__cstring: 0xfe0d
   __TEXT.__objc_classname: 0x1db6
   __TEXT.__objc_methtype: 0x18e5
   __TEXT.__dlopen_cstrs: 0xc8
   __TEXT.__objc_methname: 0x6af5
-  __TEXT.__constg_swiftt: 0x75cc
+  __TEXT.__constg_swiftt: 0x75e0
   __TEXT.__swift5_typeref: 0x651c
-  __TEXT.__oslogstring: 0x15f02
-  __TEXT.__swift5_proto: 0x19ec
-  __TEXT.__swift5_types: 0xa7c
-  __TEXT.__swift_as_entry: 0xc48
+  __TEXT.__oslogstring: 0x16022
+  __TEXT.__swift5_proto: 0x19f0
+  __TEXT.__swift5_types: 0xa80
+  __TEXT.__swift_as_entry: 0xc4c
   __TEXT.__swift_as_ret: 0x1a10
-  __TEXT.__swift_as_cont: 0x35fc
+  __TEXT.__swift_as_cont: 0x3608
   __TEXT.__swift5_protos: 0x88
-  __TEXT.__unwind_info: 0x146b0
-  __TEXT.__eh_frame: 0x3a780
-  __DATA_CONST.__const: 0x2f560
+  __TEXT.__unwind_info: 0x146d8
+  __TEXT.__eh_frame: 0x3a798
+  __DATA_CONST.__const: 0x2f5d0
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_classlist: 0x300
   __DATA_CONST.__objc_protolist: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xc8
-  __DATA_CONST.__auth_got: 0x3850
+  __DATA_CONST.__auth_got: 0x3858
   __DATA_CONST.__got: 0x1f78
   __DATA_CONST.__auth_ptr: 0x1ae8
   __DATA.__objc_const: 0x6f08
   __DATA.__objc_selrefs: 0x1800
   __DATA.__objc_data: 0x1ea0
-  __DATA.__data: 0x10f90
+  __DATA.__data: 0x10f80
   __DATA.__common: 0xef8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AdAttributionKit.framework/AdAttributionKit

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 16702
+  Functions: 16717
   Symbols:   3271
-  CStrings:  4095
+  CStrings:  4098
 
Symbols:
+ _$s10Foundation4DateV2leoiySbAC_ACtFZ
- _$s10Foundation4DateVSLAAMc
CStrings:
+ "ManagedAppDistribution.AskForException.Prompt.Body.Web.V2"
+ "ManagedAppDistribution.InstallSheet.AppStore.Body.NoLink.V2"
+ "Pending marketplace expiration fired for %s, but it is no longer pending. Ignoring."
+ "Received application unregistered notification for %{public}s (isPlaceholder: %{bool,public}d)"
+ "Skipping cleanup for %{public}s - unregistered notification was for a placeholder"
+ "The information below was provided by the developer."
+ "Your content restrictions are enabled. Updates and purchases in this app will be managed by the developer “@@developer@@”, who provided the information below."
+ "[%@] Client %s not found in registry for registration: %s"
- "ManagedAppDistribution.AskForException.Prompt.Body.Web"
- "ManagedAppDistribution.InstallSheet.AppStore.Body.NoLink"
- "Received application unregistered notification for %{public}s"
- "Verify the information before installing."
- "Your content restrictions are enabled. Updates and purchases in this app will be managed by the developer “@@developer@@”. Verify the information below before installing."
```
