## fileproviderd

> `/System/Library/Frameworks/FileProvider.framework/Support/fileproviderd`

```diff

-1703.62.4.0.0
-  __TEXT.__text: 0x86f6d0
-  __TEXT.__auth_stubs: 0x4cd0
+1703.80.16.0.0
+  __TEXT.__text: 0x8742a8
+  __TEXT.__auth_stubs: 0x4ce0
   __TEXT.__objc_stubs: 0x1c40
   __TEXT.__objc_methlist: 0x13d0
-  __TEXT.__const: 0x175ec
-  __TEXT.__cstring: 0x324be
+  __TEXT.__const: 0x177fc
+  __TEXT.__cstring: 0x3256e
   __TEXT.__objc_classname: 0x2e3
-  __TEXT.__objc_methname: 0x8834
+  __TEXT.__objc_methname: 0x883e
   __TEXT.__objc_methtype: 0x2869
   __TEXT.__oslogstring: 0xdd8
-  __TEXT.__constg_swiftt: 0xd8d8
-  __TEXT.__swift5_typeref: 0xd263
-  __TEXT.__swift5_fieldmd: 0x7308
+  __TEXT.__constg_swiftt: 0xd910
+  __TEXT.__swift5_typeref: 0xd273
+  __TEXT.__swift5_fieldmd: 0x7344
   __TEXT.__swift5_types: 0x784
   __TEXT.__ustring: 0x30
-  __TEXT.__swift5_reflstr: 0x7c2e
-  __TEXT.__swift5_capture: 0x11208
+  __TEXT.__swift5_reflstr: 0x7d5e
+  __TEXT.__swift5_capture: 0x11228
   __TEXT.__swift5_proto: 0x1110
   __TEXT.__gcc_except_tab: 0x424
   __TEXT.__swift5_builtin: 0x5b4
   __TEXT.__swift5_mpenum: 0xd4
   __TEXT.__swift5_protos: 0x68
   __TEXT.__swift5_assocty: 0x18e0
-  __TEXT.__unwind_info: 0x105b4
-  __TEXT.__eh_frame: 0x1ee10
-  __DATA_CONST.__auth_got: 0x2678
+  __TEXT.__unwind_info: 0xf7e8
+  __TEXT.__eh_frame: 0x1f028
+  __DATA_CONST.__auth_got: 0x2680
   __DATA_CONST.__got: 0xd28
   __DATA_CONST.__auth_ptr: 0x428
-  __DATA_CONST.__const: 0x3bc50
+  __DATA_CONST.__const: 0x3bc78
   __DATA_CONST.__cfstring: 0x820
   __DATA_CONST.__objc_classlist: 0x228
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x158
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0xcea8
-  __DATA.__objc_selrefs: 0x2158
+  __DATA.__objc_const: 0xcf48
+  __DATA.__objc_selrefs: 0x2150
   __DATA.__objc_protorefs: 0xa8
   __DATA.__objc_classrefs: 0x360
   __DATA.__objc_superrefs: 0x48
   __DATA.__objc_ivar: 0x118
-  __DATA.__objc_data: 0x2720
-  __DATA.__data: 0x12830
+  __DATA.__objc_data: 0x2758
+  __DATA.__data: 0x12868
   __DATA.__common: 0x548
   __DATA.__bss: 0x215a0
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 52C1642D-41FE-3E54-8A3E-22EE6617D19C
-  Functions: 27453
-  Symbols:   1992
-  CStrings:  5524
+  UUID: 08D6249A-A1EA-3C9E-81CE-7732D5BF7A10
+  Functions: 27477
+  Symbols:   1993
+  CStrings:  5527
 
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
