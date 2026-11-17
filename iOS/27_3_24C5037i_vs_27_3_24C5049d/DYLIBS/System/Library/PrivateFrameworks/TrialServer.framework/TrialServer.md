## TrialServer

> `/System/Library/PrivateFrameworks/TrialServer.framework/TrialServer`

```diff

-511.2.2.0.0
-  __TEXT.__text: 0x14ee08
+511.2.4.0.0
+  __TEXT.__text: 0x150020
   __TEXT.__delay_stubs: 0x80
   __TEXT.__delay_helper: 0x794
   __TEXT.__lazy_helpers: 0xe8
-  __TEXT.__objc_methlist: 0xc8bc
-  __TEXT.__const: 0xef4
+  __TEXT.__objc_methlist: 0xc984
+  __TEXT.__const: 0xef8
   __TEXT.__dlopen_cstrs: 0x54
-  __TEXT.__cstring: 0x16be0
+  __TEXT.__cstring: 0x16c0e
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_typeref: 0x14
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__oslogstring: 0x1e287
-  __TEXT.__gcc_except_tab: 0x7f74
-  __TEXT.__unwind_info: 0x50d8
+  __TEXT.__oslogstring: 0x1e43a
+  __TEXT.__gcc_except_tab: 0x7fdc
+  __TEXT.__unwind_info: 0x5120
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6a30
-  __DATA_CONST.__objc_classlist: 0x9c0
+  __DATA_CONST.__const: 0x6a08
+  __DATA_CONST.__objc_classlist: 0x9c8
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6608
+  __DATA_CONST.__objc_selrefs: 0x6678
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_superrefs: 0x630
+  __DATA_CONST.__objc_superrefs: 0x638
   __DATA_CONST.__objc_arraydata: 0x398
-  __DATA_CONST.__got: 0x1430
+  __DATA_CONST.__got: 0x1448
   __AUTH_CONST.__const: 0x1320
   __AUTH_CONST.__cfstring: 0xf0e0
-  __AUTH_CONST.__objc_const: 0x18368
+  __AUTH_CONST.__objc_const: 0x18458
   __AUTH_CONST.__lazy_load_got: 0x10
   __AUTH_CONST.__objc_intobj: 0xe40
   __AUTH_CONST.__objc_arrayobj: 0x378
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x1258
+  __AUTH.__objc_data: 0x12a8
   __AUTH.__data: 0x6e0
-  __DATA.__objc_ivar: 0x974
+  __DATA.__objc_ivar: 0x97c
   __DATA.__data: 0x2b40
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x28

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 5007
-  Symbols:   9436
-  CStrings:  4268
+  Functions: 5023
+  Symbols:   9466
+  CStrings:  4279
 
Symbols:
+ +[NSFileManager(TRIServer) _triTakeOwnershipOfItemAtPath:]
+ +[NSFileManager(TRIServer) _triTakeOwnershipOfTreeAtPath:]
+ +[NSFileManager(TRIServer) triCopyDirectoryWithoutFollowingLinksFromPath:toNewPath:]
+ +[TRIInternalAgentToSystemServiceRequestHandler _areValidFactorNames:]
+ +[TRIInternalAgentToSystemServiceRequestHandler _isValidGlobalFactorPackPath:treatmentsDir:]
+ -[TRIFBFactorPackStorage _removeUnreferencedFactorLevelsWithExternalReferenceStore:removedCount:]
+ -[TRIFBFactorPackStorage _removeUnreferencedFactorPackSetsWithNamespaceName:externalReferenceStore:removedCount:]
+ -[TRIFBFactorPackStorage _removeUnreferencedFactorPackSetsWithParentDir:externalReferenceStore:removedCount:]
+ -[TRIFBFactorPackStorage removeUnreferencedFactorLevelsWithServerContext:removedCount:]
+ -[TRIFactorPackStorage _removeUnreferencedFactorPackSetsWithNamespaceName:externalReferenceStore:removedCount:]
+ -[TRIFactorPackStorage _removeUnreferencedFactorPackSetsWithParentDir:externalReferenceStore:removedCount:]
+ -[TRIFactorPackStorage _removeUnreferencedFactorPacksWithExternalReferenceStore:removedCount:]
+ -[TRIFactorPackStorage removeUnreferencedFactorPacksWithServerContext:removedCount:]
+ -[TRIGlobalFactorPackExternalReferenceStore .cxx_destruct]
+ -[TRIGlobalFactorPackExternalReferenceStore hasReferenceToPath:]
+ -[TRIGlobalFactorPackExternalReferenceStore initWithServerContext:]
+ -[TRIInternalAgentToSystemServiceRequestHandler _ensureGlobalFactorPackIsOwnedByCurrentProcessAtPath:]
+ -[TRIInternalAgentToSystemServiceRequestHandler _replaceGlobalFactorPackAtPath:withCopyOfDirectory:]
+ _NSFileGroupOwnerAccountID
+ _NSFileOwnerAccountID
+ _NSFilePosixPermissions
+ _OBJC_CLASS_$_TRIGlobalFactorPackExternalReferenceStore
+ _OBJC_IVAR_$_TRIGlobalFactorPackExternalReferenceStore._activeFactorPackIds
+ _OBJC_IVAR_$_TRIGlobalFactorPackExternalReferenceStore._context
+ _OBJC_METACLASS_$_TRIGlobalFactorPackExternalReferenceStore
+ __OBJC_$_CLASS_METHODS_TRIInternalAgentToSystemServiceRequestHandler
+ __OBJC_$_INSTANCE_METHODS_TRIGlobalFactorPackExternalReferenceStore
+ __OBJC_$_INSTANCE_VARIABLES_TRIGlobalFactorPackExternalReferenceStore
+ __OBJC_CLASS_PROTOCOLS_$_TRIGlobalFactorPackExternalReferenceStore
+ __OBJC_CLASS_RO_$_TRIGlobalFactorPackExternalReferenceStore
+ __OBJC_METACLASS_RO_$_TRIGlobalFactorPackExternalReferenceStore
+ ___107-[TRIFactorPackStorage _removeUnreferencedFactorPackSetsWithParentDir:externalReferenceStore:removedCount:]_block_invoke
+ ___109-[TRIFBFactorPackStorage _removeUnreferencedFactorPackSetsWithParentDir:externalReferenceStore:removedCount:]_block_invoke
+ ___58+[NSFileManager(TRIServer) _triTakeOwnershipOfTreeAtPath:]_block_invoke
+ _copyfile
+ _getegid
+ _geteuid
- -[TRIFBFactorPackStorage _removeUnreferencedFactorPackSetsWithParentDir:removedCount:]
- -[TRIFBFactorPackStorage removeUnreferencedFactorLevelsWithRemovedCount:]
- -[TRIFactorPackStorage _removeUnreferencedFactorPackSetsWithParentDir:removedCount:]
- GCC_except_table50
- ___84-[TRIFactorPackStorage _removeUnreferencedFactorPackSetsWithParentDir:removedCount:]_block_invoke
- ___86-[TRIFBFactorPackStorage _removeUnreferencedFactorPackSetsWithParentDir:removedCount:]_block_invoke
- ___block_descriptor_56_e8_32s40r_e22_v24?0"NSString"8^B16lr40l8s32l8
CStrings:
+ "-[TRIFBFactorPackStorage _removeUnreferencedFactorPackSetsWithNamespaceName:externalReferenceStore:removedCount:]"
+ "-[TRIFactorPackStorage _removeUnreferencedFactorPackSetsWithNamespaceName:externalReferenceStore:removedCount:]"
+ "Cannot copy %{public}@, not a directory"
+ "Cannot copy to %{public}@, already exists"
+ "Could not update ownership of factor pack: %@"
+ "Failed to copy %{public}@ to %{public}@: %s (%d)"
+ "Failed to read %{public}@: %{public}@"
+ "Failed to read attributes of %{public}@: %{public}@"
+ "Failed to take ownership of %{public}@: %{public}@"
+ "Failed to write users per factor file with error: %{public}@"
+ "Global factor pack at %@ is not a directory"
+ "Invalid factor names: %@"
+ "Rejecting invalid factor name: %@"
+ "Rejecting invalid global factor pack path: %@"
+ "Replacing global factor pack at %@ owned by uid %u with a copy"
+ "TrialXP-511.2.4"
- "-[TRIFBFactorPackStorage _removeUnreferencedFactorPackSetsWithNamespaceName:removedCount:]"
- "-[TRIFactorPackStorage _removeUnreferencedFactorPackSetsWithNamespaceName:removedCount:]"
- "Asked to delete factor pack at non-global or non-treatment directory location: %@"
- "Failed to write users per factor file to temp path with error: %{public}@"
- "TrialXP-511.2.2"
```
