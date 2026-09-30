## managedappdistributiond

> `/System/Library/Frameworks/ManagedAppDistribution.framework/Support/managedappdistributiond`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_ivar`
- `__DATA.__common`

```diff

-4.0.37.0.0
-  __TEXT.__text: 0x6df1ac
-  __TEXT.__auth_stubs: 0x74e0
+4.0.39.0.0
+  __TEXT.__text: 0x6e5e34
+  __TEXT.__auth_stubs: 0x7520
   __TEXT.__objc_stubs: 0x5ae0
   __TEXT.__objc_methlist: 0x23cc
-  __TEXT.__const: 0x3fc10
+  __TEXT.__const: 0x3fe60
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__objc_methname: 0x8575
-  __TEXT.__cstring: 0xf915
-  __TEXT.__oslogstring: 0x16002
-  __TEXT.__objc_classname: 0x1ee6
-  __TEXT.__objc_methtype: 0x1ebf
+  __TEXT.__cstring: 0xf9cd
+  __TEXT.__objc_methname: 0x85b5
+  __TEXT.__oslogstring: 0x160f2
+  __TEXT.__objc_classname: 0x1f76
+  __TEXT.__objc_methtype: 0x1ec5
   __TEXT.__gcc_except_tab: 0x50c
   __TEXT.__dlopen_cstrs: 0xc8
-  __TEXT.__constg_swiftt: 0x7468
-  __TEXT.__swift5_typeref: 0x652a
-  __TEXT.__swift5_proto: 0x19c8
-  __TEXT.__swift5_types: 0xa64
-  __TEXT.__swift_as_entry: 0xc20
-  __TEXT.__swift_as_ret: 0x19b4
-  __TEXT.__swift_as_cont: 0x3524
+  __TEXT.__constg_swiftt: 0x7578
+  __TEXT.__swift5_typeref: 0x6560
+  __TEXT.__swift5_proto: 0x19d8
+  __TEXT.__swift5_types: 0xa78
+  __TEXT.__swift_as_entry: 0xc38
+  __TEXT.__swift_as_ret: 0x19d8
+  __TEXT.__swift_as_cont: 0x3558
   __TEXT.__swift5_protos: 0x88
-  __TEXT.__unwind_info: 0x128e0
-  __TEXT.__eh_frame: 0x39c20
-  __DATA_CONST.__const: 0x2f458
+  __TEXT.__unwind_info: 0x12520
+  __TEXT.__eh_frame: 0x3a178
+  __DATA_CONST.__const: 0x2f4a8
   __DATA_CONST.__cfstring: 0xae0
-  __DATA_CONST.__objc_classlist: 0x380
+  __DATA_CONST.__objc_classlist: 0x390
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xd0
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x3a80
-  __DATA_CONST.__got: 0x1fb8
-  __DATA_CONST.__auth_ptr: 0x5eb0
-  __DATA.__objc_const: 0x8460
+  __DATA_CONST.__auth_got: 0x3aa0
+  __DATA_CONST.__got: 0x1fd8
+  __DATA_CONST.__auth_ptr: 0x5e60
+  __DATA.__objc_const: 0x8600
   __DATA.__objc_selrefs: 0x1ea8
   __DATA.__objc_ivar: 0xcc
-  __DATA.__objc_data: 0x23f8
-  __DATA.__data: 0x10d48
-  __DATA.__bss: 0x2ea50
+  __DATA.__objc_data: 0x2448
+  __DATA.__data: 0x11038
+  __DATA.__bss: 0x2ec50
   __DATA.__common: 0xef0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AdAttributionKit.framework/AdAttributionKit

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 16856
-  Symbols:   3339
-  CStrings:  4572
+  Functions: 16941
+  Symbols:   3348
+  CStrings:  4583
 
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
+ "AsyncBufferedPipe:read"
+ "Installation already in progress"
+ "ManagedAppDistributionDaemon/AsyncBufferedPipe.swift"
+ "[%@] Declaration already pinned for installation"
+ "[%@] Retried installation but it was already in progress"
+ "[%@] Updating backoff date for declaration %{public}s also encountered an error: %{public}@"
+ "[%@][EnterpriseUpdates] Installation of '%{public}s' is already in progress"
+ "_TtC28ManagedAppDistributionDaemon12BufferedPipe"
+ "_TtC28ManagedAppDistributionDaemon17AsyncBufferedPipe"
+ "buffer"
+ "nextPendingID"
+ "underestimatedLimit"
- "[%@] Client %s not found in registry for registration: %s"
```
