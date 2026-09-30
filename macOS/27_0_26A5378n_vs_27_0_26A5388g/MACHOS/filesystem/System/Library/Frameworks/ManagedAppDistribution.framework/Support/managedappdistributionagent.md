## managedappdistributionagent

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributionagent`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_ivar`
- `__DATA.__objc_data`
- `__DATA.__bss`

```diff

-4.0.37.0.0
-  __TEXT.__text: 0x4408dc
-  __TEXT.__auth_stubs: 0x5b90
+4.0.39.0.0
+  __TEXT.__text: 0x444560
+  __TEXT.__auth_stubs: 0x5bd0
   __TEXT.__objc_stubs: 0x53c0
   __TEXT.__objc_methlist: 0x1ecc
-  __TEXT.__const: 0x25470
+  __TEXT.__const: 0x254a0
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__cstring: 0x62c5
-  __TEXT.__oslogstring: 0xd0e2
-  __TEXT.__swift5_typeref: 0x5ce0
-  __TEXT.__objc_methname: 0x7985
-  __TEXT.__objc_classname: 0x1de6
-  __TEXT.__objc_methtype: 0x1d5f
+  __TEXT.__cstring: 0x628d
+  __TEXT.__oslogstring: 0xd172
+  __TEXT.__swift5_typeref: 0x5cd2
+  __TEXT.__objc_methname: 0x7965
+  __TEXT.__objc_classname: 0x1e06
+  __TEXT.__objc_methtype: 0x1d2c
   __TEXT.__gcc_except_tab: 0x30c
   __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__constg_swiftt: 0x71c0
+  __TEXT.__constg_swiftt: 0x7200
   __TEXT.__swift5_proto: 0x1830
-  __TEXT.__swift5_types: 0x948
-  __TEXT.__swift_as_entry: 0x9e0
-  __TEXT.__swift_as_ret: 0x103c
-  __TEXT.__swift_as_cont: 0x28c0
+  __TEXT.__swift5_types: 0x94c
+  __TEXT.__swift_as_entry: 0x9ec
+  __TEXT.__swift_as_ret: 0x104c
+  __TEXT.__swift_as_cont: 0x28d8
   __TEXT.__swift5_protos: 0x88
-  __TEXT.__unwind_info: 0xee78
-  __TEXT.__eh_frame: 0x2bf30
-  __DATA_CONST.__const: 0x1f178
+  __TEXT.__unwind_info: 0xe5c0
+  __TEXT.__eh_frame: 0x2bdd4
+  __DATA_CONST.__const: 0x1f148
   __DATA_CONST.__cfstring: 0xae0
   __DATA_CONST.__objc_classlist: 0x370
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x2dd8
-  __DATA_CONST.__got: 0x1858
-  __DATA_CONST.__auth_ptr: 0x5040
-  __DATA.__objc_const: 0x8610
+  __DATA_CONST.__auth_got: 0x2df8
+  __DATA_CONST.__got: 0x1878
+  __DATA_CONST.__auth_ptr: 0x4fb0
+  __DATA.__objc_const: 0x8630
   __DATA.__objc_selrefs: 0x1b18
   __DATA.__objc_ivar: 0xcc
   __DATA.__objc_data: 0x2220
-  __DATA.__data: 0x10138
+  __DATA.__data: 0x100f8
   __DATA.__bss: 0x2bee8
-  __DATA.__common: 0xd34
+  __DATA.__common: 0xd24
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/BackgroundAssets.framework/Versions/A/BackgroundAssets

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 13762
-  Symbols:   2672
+  Functions: 13744
+  Symbols:   2681
   CStrings:  3239
 
Symbols:
+ _$s15Synchronization19AtomicRepresentableP06decodeB14Representationyx0bE0QznFZTj
+ _$s15Synchronization19AtomicRepresentableTL
+ _$s20AtomicRepresentation15Synchronization0A13RepresentablePTl
+ _$s22ManagedAppDistribution08InternalaB14InstallRequestV6ResultV6StatusO6deniedyA2GmFWC
+ _$s22ManagedAppDistribution08InternalaB14InstallRequestV6ResultV6StatusO6failedyA2GmFWC
+ _$s22ManagedAppDistribution08InternalaB14InstallRequestV6ResultV6StatusO7allowedyA2GmFWC
+ _$s22ManagedAppDistribution08InternalaB14InstallRequestV6ResultV6StatusOMa
+ _$s22ManagedAppDistribution08InternalaB14InstallRequestV6ResultV6statusA2E6StatusO_tcfC
+ _$s22ManagedAppDistribution08InternalaB14InstallRequestV6ResultVMn
+ _$sScCMa
- _$s22ManagedAppDistribution19MessageRegistrationOs23CustomStringConvertibleAAMc
CStrings:
+ "Installation already in progress"
+ "[%@] Declaration already pinned for installation"
+ "[%@] Retried installation but it was already in progress"
+ "[%@] Updating backoff date for declaration %{public}s also encountered an error: %{public}@"
+ "nextPendingID"
- "DDMAutomaticUpdatePolicy"
- "DDMBlockedReason"
- "DDMCellularPolicy"
- "DDMInstallTiming"
- "[%@] Client %s not found in registry for registration: %s"
```
