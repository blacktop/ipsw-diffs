## FileProviderDaemon

> `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon`

```diff

-4018.120.17.0.0
-  __TEXT.__text: 0xadfba4
+4018.120.21.0.0
+  __TEXT.__text: 0xae0a18
   __TEXT.__auth_stubs: 0x5db0
-  __TEXT.__objc_methlist: 0x9d04
-  __TEXT.__const: 0x2bf30
-  __TEXT.__cstring: 0x41ef5
-  __TEXT.__oslogstring: 0x1ee92
-  __TEXT.__gcc_except_tab: 0xe778
+  __TEXT.__objc_methlist: 0x9d14
+  __TEXT.__const: 0x2bf40
+  __TEXT.__cstring: 0x41f35
+  __TEXT.__oslogstring: 0x1eea2
+  __TEXT.__gcc_except_tab: 0xe784
   __TEXT.__ustring: 0x176e
   __TEXT.__dlopen_cstrs: 0xc3
   __TEXT.__constg_swiftt: 0x13628
   __TEXT.__swift5_typeref: 0x13524
   __TEXT.__swift5_builtin: 0x8d4
-  __TEXT.__swift5_reflstr: 0xeb5d
-  __TEXT.__swift5_fieldmd: 0xc890
+  __TEXT.__swift5_reflstr: 0xeb7d
+  __TEXT.__swift5_fieldmd: 0xc89c
   __TEXT.__swift5_mpenum: 0x134
   __TEXT.__swift5_assocty: 0x2988
-  __TEXT.__swift5_capture: 0x16f68
+  __TEXT.__swift5_capture: 0x16f6c
   __TEXT.__swift5_proto: 0x1c88
   __TEXT.__swift5_types: 0xbe4
   __TEXT.__swift5_types2: 0x4
   __TEXT.__swift5_protos: 0xb4
   __TEXT.__swift_as_entry: 0xb0
   __TEXT.__swift_as_ret: 0xa4
-  __TEXT.__unwind_info: 0x14cd0
-  __TEXT.__eh_frame: 0x2699c
+  __TEXT.__unwind_info: 0x14ce8
+  __TEXT.__eh_frame: 0x269d4
   __TEXT.__objc_classname: 0x2473
-  __TEXT.__objc_methname: 0x22ef5
+  __TEXT.__objc_methname: 0x22f55
   __TEXT.__objc_methtype: 0x7c96
-  __TEXT.__objc_stubs: 0x15160
+  __TEXT.__objc_stubs: 0x151a0
   __DATA_CONST.__got: 0x1878
   __DATA_CONST.__const: 0x45b0
   __DATA_CONST.__objc_classlist: 0x5a0
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x350
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x62c0
+  __DATA_CONST.__objc_selrefs: 0x62d0
   __DATA_CONST.__objc_protorefs: 0x188
   __DATA_CONST.__objc_superrefs: 0x290
   __DATA_CONST.__objc_arraydata: 0x128
   __AUTH_CONST.__auth_got: 0x2ee8
   __AUTH_CONST.__const: 0x428b0
   __AUTH_CONST.__cfstring: 0x72c0
-  __AUTH_CONST.__objc_const: 0x2cab8
+  __AUTH_CONST.__objc_const: 0x2cad8
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x78

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 39DC9B78-DD7B-3A91-A42B-CC78FCEEFFFE
-  Functions: 29402
-  Symbols:   26042
-  CStrings:  14073
+  UUID: C9FD7EDF-E4BB-3361-A236-A10704E96FD1
+  Functions: 29405
+  Symbols:   26058
+  CStrings:  14075
 
Symbols:
+ -[FPDDomainDeadEndBackend _materializationErrorOrFallbackError]
+ -[FPDDomainDeadEndBackend startProvidingItemAtURL:readerID:readingOptions:request:completionHandler:].cold.1
+ -[FPDDomainDeadEndBackend startProvidingItemAtURL:readerID:readingOptions:request:completionHandler:].cold.2
+ _objc_msgSend$_materializationErrorOrFallbackError
+ _objc_msgSend$setDeletedDirectoryFileID:
+ _symbolic _____Sg 18FileProviderDaemon4FPCKC13ExtendedErrorV
- _symbolic Say______pG s5ErrorP
CStrings:
+ ".id = parent_dirs.parent_id AND parent_dirs.id != parent_dirs.parent_id\n)\n\nSELECT p.id, (jobs.reason | jobs.pending_reason)\n  FROM parent_dirs AS p\n INNER JOIN "
+ "[ERROR] [deadend] failed to provide item at %@, iterator error: %@"
+ "[ERROR] [deadend] failed to provide item at %@, lstat failed: %@"
+ "_materializationErrorOrFallbackError"
+ "delete(_:recursively:baseVersion:domainVersion:oldVersionCapturedContent:deletedDirectoryFileID:completion:)"
+ "deletedDirectoryFileID"
+ "setDeletedDirectoryFileID:"
- ".id = parent_dirs.parent_id AND parent_dirs.id != parent_dirs.parent_id\n)\n\nSELECT 1\n  FROM parent_dirs AS p\n INNER JOIN "
- "delete(_:recursively:baseVersion:domainVersion:oldVersionCapturedContent:completion:)"
- "no entry.a.id for entry: %s"
- "no parent ID in snapshot for %s"
- "no parentRec in RT for parent %s of %s"

```
