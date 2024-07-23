## LocalStorageFileProvider

> `/System/Library/Frameworks/FileProvider.framework/PlugIns/LocalStorageFileProvider.appex/LocalStorageFileProvider`

```diff

-2732.0.26.0.0
-  __TEXT.__text: 0x910e64
-  __TEXT.__auth_stubs: 0x50e0
+2732.0.44.0.0
+  __TEXT.__text: 0x911c20
+  __TEXT.__auth_stubs: 0x50f0
   __TEXT.__objc_stubs: 0x1ec0
   __TEXT.__objc_methlist: 0x1be8
   __TEXT.__gcc_except_tab: 0x564
-  __TEXT.__const: 0x1b45c
-  __TEXT.__cstring: 0x2dbd6
-  __TEXT.__objc_methname: 0xaceb
+  __TEXT.__const: 0x1b84c
+  __TEXT.__cstring: 0x2d7b6
+  __TEXT.__objc_methname: 0xac75
   __TEXT.__objc_classname: 0x470
   __TEXT.__objc_methtype: 0x3550
-  __TEXT.__constg_swiftt: 0xf38c
-  __TEXT.__swift5_typeref: 0xedf5
-  __TEXT.__swift5_builtin: 0x690
-  __TEXT.__swift5_reflstr: 0x981e
-  __TEXT.__swift5_fieldmd: 0x87e0
-  __TEXT.__swift5_assocty: 0x1bd8
-  __TEXT.__swift5_proto: 0x1438
-  __TEXT.__swift5_types: 0x8dc
-  __TEXT.__swift5_capture: 0x13cdc
+  __TEXT.__constg_swiftt: 0xf3d4
+  __TEXT.__swift5_typeref: 0xef15
+  __TEXT.__swift5_builtin: 0x6b8
+  __TEXT.__swift5_reflstr: 0x96ee
+  __TEXT.__swift5_fieldmd: 0x8830
+  __TEXT.__swift5_assocty: 0x1c20
+  __TEXT.__swift5_proto: 0x1464
+  __TEXT.__swift5_types: 0x8e8
+  __TEXT.__swift5_capture: 0x13d94
   __TEXT.__swift5_protos: 0x70
   __TEXT.__ustring: 0x30
   __TEXT.__oslogstring: 0xd6fa
-  __TEXT.__swift5_mpenum: 0xec
-  __TEXT.__unwind_info: 0x10600
-  __TEXT.__eh_frame: 0x22bfc
-  __DATA_CONST.__auth_got: 0x2880
-  __DATA_CONST.__got: 0x1138
-  __DATA_CONST.__auth_ptr: 0x2c30
-  __DATA_CONST.__const: 0x3d8c8
+  __TEXT.__swift5_mpenum: 0x100
+  __TEXT.__unwind_info: 0x10658
+  __TEXT.__eh_frame: 0x22c4c
+  __DATA_CONST.__auth_got: 0x2888
+  __DATA_CONST.__got: 0x1148
+  __DATA_CONST.__auth_ptr: 0x2c68
+  __DATA_CONST.__const: 0x3db08
   __DATA_CONST.__cfstring: 0x860
   __DATA_CONST.__objc_classlist: 0x288
   __DATA_CONST.__objc_catlist: 0x38

   __DATA_CONST.__objc_protorefs: 0x120
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x18028
-  __DATA.__objc_selrefs: 0x26f0
+  __DATA.__objc_const: 0x17e88
+  __DATA.__objc_selrefs: 0x26d8
   __DATA.__objc_ivar: 0x134
-  __DATA.__objc_data: 0x3380
-  __DATA.__data: 0x13b88
-  __DATA.__bss: 0x27820
-  __DATA.__common: 0x880
+  __DATA.__objc_data: 0x3310
+  __DATA.__data: 0x13b68
+  __DATA.__bss: 0x27da0
+  __DATA.__common: 0x890
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
+  - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/FileProvider.framework/FileProvider
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 24934
-  Symbols:   916
-  CStrings:  6600
+  Functions: 24987
+  Symbols:   919
+  CStrings:  6581
 
Symbols:
+ _CSIndexErrorDomain
+ _FPPerformWithPersona
+ _swift_runtimeSupportsNoncopyableTypes
CStrings:
+ "avoidNilErrorItemsForDetailedPayload"
- "/Library/Caches/com.apple.xbs/Sources/FileProviderExtensions/fssync/libfssync/fpck/FPCK.swift"
- "FPCKPendingSetInternalErrorCodeFileLockErrorWithDiffWithContentDiffFP"
- "FPCKPendingSetInternalErrorCodeFileLockErrorWithDiffWithContentDiffFS"
- "FPCKPendingSetInternalErrorCodeFileLockErrorWithDiffWithoutContentDiffFP"
- "FPCKPendingSetInternalErrorCodeFileLockErrorWithDiffWithoutContentDiffFS"
- "FPCKPendingSetInternalErrorCodeFileLockErrorWithoutDiff"
- "FPCKPendingSetInternalErrorCodeFileLockErrorWithoutReconciliationEntry"
- "FPCKPendingSetInternalErrorCodeNilError"
- "FPCKPendingSetInternalErrorCodePOSIXEACCESHasReadPermission"
- "FPCKPendingSetInternalErrorCodePOSIXEACCESMissingReadPermission"
- "FPCKPendingSetInternalErrorCodePOSIXEACCESUnknown"
- "FPCKPendingSetInternalErrorCodePOSIXENOTSUPAFSCCompressedFile"
- "FPCKPendingSetInternalErrorCodePOSIXENOTSUPUnknown"
- "Failed adopting persona "
- "Failed restoring persona "
- "One persona is unexpectedly nil "
- "detachedRootLogicalURL"
- "fp_isFileProviderError:"
- "generateAndRestorePersonaContextWithPersonaUniqueString:"
- "rootItemIDWithProviderIdentifier:domainIdentifier:"

```
