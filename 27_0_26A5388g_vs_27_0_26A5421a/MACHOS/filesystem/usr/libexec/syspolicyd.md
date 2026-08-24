## syspolicyd

> `/usr/libexec/syspolicyd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__const`
- `__TEXT.__objc_methtype`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__dof_security_`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-823.0.3.0.0
-  __TEXT.__text: 0xb1c0c
-  __TEXT.__auth_stubs: 0x2c40
-  __TEXT.__objc_stubs: 0xa4e0
+823.1.1.0.0
+  __TEXT.__text: 0xb3220
+  __TEXT.__auth_stubs: 0x2c50
+  __TEXT.__objc_stubs: 0xa5e0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x5354
+  __TEXT.__objc_methlist: 0x53bc
   __TEXT.__const: 0x1ff8
-  __TEXT.__objc_methname: 0xd091
-  __TEXT.__cstring: 0x11a63
+  __TEXT.__objc_methname: 0xd1f1
+  __TEXT.__cstring: 0x11bb3
   __TEXT.__objc_classname: 0x838
   __TEXT.__objc_methtype: 0x280b
-  __TEXT.__oslogstring: 0x9f06
-  __TEXT.__gcc_except_tab: 0x1ba8
+  __TEXT.__oslogstring: 0xa0d6
+  __TEXT.__gcc_except_tab: 0x1c20
   __TEXT.__swift5_typeref: 0x410
   __TEXT.__swift5_capture: 0x1b4
   __TEXT.__constg_swiftt: 0x4a0

   __TEXT.__swift5_proto: 0x40
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__dof_security_: 0x325
-  __TEXT.__unwind_info: 0x24f0
+  __TEXT.__unwind_info: 0x2528
   __TEXT.__eh_frame: 0x1b8
   __DATA_CONST.__const: 0x3c98
-  __DATA_CONST.__cfstring: 0x8c60
+  __DATA_CONST.__cfstring: 0x8d00
   __DATA_CONST.__objc_classlist: 0x318
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x1f8
-  __DATA_CONST.__objc_intobj: 0x2d0
+  __DATA_CONST.__objc_intobj: 0x2e8
   __DATA_CONST.__objc_arraydata: 0x5a8
   __DATA_CONST.__objc_arrayobj: 0x2a0
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA_CONST.__auth_got: 0x1638
+  __DATA_CONST.__auth_got: 0x1640
   __DATA_CONST.__got: 0x8f8
   __DATA_CONST.__auth_ptr: 0x208
-  __DATA.__objc_const: 0x9f38
-  __DATA.__objc_selrefs: 0x2ed0
-  __DATA.__objc_ivar: 0x810
+  __DATA.__objc_const: 0x9f70
+  __DATA.__objc_selrefs: 0x2f20
+  __DATA.__objc_ivar: 0x814
   __DATA.__objc_data: 0x2208
   __DATA.__data: 0xdb2
   __DATA.__bss: 0xad0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3573
-  Symbols:   1064
-  CStrings:  5545
+  Functions: 3594
+  Symbols:   1065
+  CStrings:  5570
 
Symbols:
+ _getmntinfo_r_np
CStrings:
+ "DELETE FROM policy_cache_by_path_meta WHERE for_entry NOT IN (SELECT pk FROM policy_scan_cache_by_path)"
+ "DELETE FROM policy_scan_cache_by_path WHERE mount_point = ?1"
+ "Ignoring declared bundle path that does not contain target: %@ (target: %@)"
+ "Invalid parameter: non-URL element in kext URL array."
+ "No unmounted policy scan cache entries to purge"
+ "Purged %ld cache entries for mount point: %{public}@"
+ "Purged %ld total cache entries across %lu mount points"
+ "SELECT COUNT(*) FROM policy_scan_cache_by_path WHERE mount_point = ?1"
+ "SELECT DISTINCT mount_point FROM policy_scan_cache_by_path"
+ "Skipping purge: could not determine active mount points"
+ "T@\"NSURL\",&,N,V_quarantineOverrideURL"
+ "URLByStandardizingPath"
+ "Using declared bundle path quarantine status: %@ (target: %@)"
+ "_quarantineOverrideURL"
+ "cachedByPathMountPoints"
+ "com.apple.private.syspolicy.cache-management"
+ "declaredBundlePathURL:containsTargetURL:"
+ "ensureQuarantineStateChecked"
+ "evaluateCodeForUser:withPID:withProcessPath:withParentProcessPath:withResponsibleProcess:withLibraryPath:processIsScript:withValidationCategory:withDeclaredBundlePath:withCompletionCallback:"
+ "gatekeeperEvaluationForUser:withPID:withProcessPath:withParentProcessPath:withResponsibleProcess:withLibraryPath:processIsScript:forEvaluationID:withValidationCategory:withDeclaredBundlePath:"
+ "getmntinfo_r_np failed to enumerate active mounts: %d"
+ "purgeUnmountedPolicyScanCacheEntries"
+ "purgeUnmountedPolicyScanCacheEntriesWithReply:"
+ "quarantineOverrideURL"
+ "removeCacheEntriesForMountPoints:"
+ "setQuarantineOverrideURL:"
+ "setWithCapacity:"
+ "v84@0:8I16i20@24@32@40@48B56@60@68@?76"
+ "v84@0:8I16i20@24@32@40@48B56q60@68@76"
- "evaluateCodeForUser:withPID:withProcessPath:withParentProcessPath:withResponsibleProcess:withLibraryPath:processIsScript:withValidationCategory:withCompletionCallback:"
- "gatekeeperEvaluationForUser:withPID:withProcessPath:withParentProcessPath:withResponsibleProcess:withLibraryPath:processIsScript:forEvaluationID:withValidationCategory:"
- "v76@0:8I16i20@24@32@40@48B56@60@?68"
- "v76@0:8I16i20@24@32@40@48B56q60@68"
```
