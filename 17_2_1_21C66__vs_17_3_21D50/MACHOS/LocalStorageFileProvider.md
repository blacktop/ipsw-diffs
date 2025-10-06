## LocalStorageFileProvider

> `/System/Library/Frameworks/FileProvider.framework/PlugIns/LocalStorageFileProvider.appex/LocalStorageFileProvider`

```diff

-1703.62.4.0.0
-  __TEXT.__text: 0x8dc9d8
-  __TEXT.__auth_stubs: 0x4ee0
+1703.80.16.0.0
+  __TEXT.__text: 0x8e15b0
+  __TEXT.__auth_stubs: 0x4ef0
   __TEXT.__objc_stubs: 0x1c20
   __TEXT.__objc_methlist: 0x1868
   __TEXT.__gcc_except_tab: 0x468
-  __TEXT.__const: 0x18d4c
-  __TEXT.__cstring: 0x34d2e
-  __TEXT.__objc_methname: 0x9bdc
+  __TEXT.__const: 0x18f5c
+  __TEXT.__cstring: 0x34dde
+  __TEXT.__objc_methname: 0x9be6
   __TEXT.__objc_classname: 0x3ef
   __TEXT.__objc_methtype: 0x2e32
-  __TEXT.__constg_swiftt: 0xdf4c
-  __TEXT.__swift5_typeref: 0xd953
+  __TEXT.__constg_swiftt: 0xdf84
+  __TEXT.__swift5_typeref: 0xd973
   __TEXT.__swift5_builtin: 0x5dc
-  __TEXT.__swift5_reflstr: 0x87ee
-  __TEXT.__swift5_fieldmd: 0x7c94
+  __TEXT.__swift5_reflstr: 0x891e
+  __TEXT.__swift5_fieldmd: 0x7cd0
   __TEXT.__swift5_assocty: 0x1a18
   __TEXT.__swift5_proto: 0x12bc
   __TEXT.__swift5_types: 0x838
-  __TEXT.__swift5_capture: 0x11904
+  __TEXT.__swift5_capture: 0x11924
   __TEXT.__swift5_protos: 0x6c
   __TEXT.__ustring: 0x30
   __TEXT.__oslogstring: 0xc6e
   __TEXT.__swift5_mpenum: 0xd4
-  __TEXT.__unwind_info: 0x109d4
-  __TEXT.__eh_frame: 0x20380
-  __DATA_CONST.__auth_got: 0x2780
+  __TEXT.__unwind_info: 0x10c18
+  __TEXT.__eh_frame: 0x20598
+  __DATA_CONST.__auth_got: 0x2788
   __DATA_CONST.__got: 0xd98
   __DATA_CONST.__auth_ptr: 0x4c0
-  __DATA_CONST.__const: 0x3e3b8
+  __DATA_CONST.__const: 0x3e3e0
   __DATA_CONST.__cfstring: 0x840
   __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x1e0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x11960
-  __DATA.__objc_selrefs: 0x23d8
+  __DATA.__objc_const: 0x11a00
+  __DATA.__objc_selrefs: 0x23d0
   __DATA.__objc_protorefs: 0xf0
   __DATA.__objc_classrefs: 0x350
   __DATA.__objc_superrefs: 0x50
   __DATA.__objc_ivar: 0x124
-  __DATA.__objc_data: 0x2ee0
-  __DATA.__data: 0x140e8
+  __DATA.__objc_data: 0x2f18
+  __DATA.__data: 0x14110
   __DATA.__bss: 0x24920
   __DATA.__common: 0x728
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 15470434-054E-3548-997C-CAC289AE7001
-  Functions: 28762
-  Symbols:   866
-  CStrings:  6017
+  UUID: CD912703-8110-3B63-8D18-AA66F7906E49
+  Functions: 28786
+  Symbols:   867
+  CStrings:  6020
 
Symbols:
+ _fpfs_lp_faccessat
CStrings:
+ "\n\n  UNION -- We may have cycles, don't use UNION ALL\n\n  SELECT "
+ "%s bitmapvalue exceeded alloted %ld bits"
+ ".vfs_fileid\n      ELSE 0\n    END\n    FROM "
+ "FPCKPendingSetInternalErrorCodeFileLockErrorWithoutReconciliationEntry"
+ "FPCKPendingSetInternalErrorCodePOSIXEACCESHasReadPermission"
+ "FPCKPendingSetInternalErrorCodePOSIXEACCESMissingReadPermission"
+ "FPCKPendingSetInternalErrorCodePOSIXEACCESUnknown"
+ "WITH RECURSIVE parent_dirs(id, parent_id, closest_sync_root) AS (\n  SELECT id, parent_id,\n    CASE\n      WHEN metadata_is_syncroot != 0 THEN vfs_fileid\n      ELSE 0\n    END\n    FROM "
+ "etagForVersion:providerDomainID:"
+ "lastTransactionError"
- ".metadata_closest_syncroot\n      ELSE 0\n    END\n    FROM "
- ".metadata_closest_syncroot != 0 THEN "
- ".vfs_fileid\n      WHEN "
- "WITH RECURSIVE parent_dirs(id, parent_id, closest_sync_root) AS (\n  SELECT id, parent_id,\n    CASE\n      WHEN metadata_is_syncroot != 0 THEN vfs_fileid\n      WHEN metadata_closest_syncroot != 0 THEN metadata_closest_syncroot\n      ELSE 0\n    END\n    FROM "
- "etagHash"
- "groupInBatch:"
- "runAfterNextDurableFlush(function:side:isIngestion:cancelBlock:_:)"

```
