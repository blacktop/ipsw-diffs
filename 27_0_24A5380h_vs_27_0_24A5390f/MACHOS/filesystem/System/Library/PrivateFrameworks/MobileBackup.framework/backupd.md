## backupd

> `/System/Library/PrivateFrameworks/MobileBackup.framework/backupd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__objc_methname`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3038.0.0.0.0
-  __TEXT.__text: 0x2471c8
-  __TEXT.__auth_stubs: 0x32b0
-  __TEXT.__objc_stubs: 0x280a0
+3039.0.1.0.0
+  __TEXT.__text: 0x247b64
+  __TEXT.__auth_stubs: 0x32a0
+  __TEXT.__objc_stubs: 0x280e0
   __TEXT.__objc_methlist: 0x15ea4
   __TEXT.__const: 0x1820
   __TEXT.__objc_classname: 0x2140

   __TEXT.__swift5_fieldmd: 0xca0
   __TEXT.__swift5_builtin: 0xf0
   __TEXT.__swift5_assocty: 0x90
-  __TEXT.__cstring: 0x6860c
+  __TEXT.__cstring: 0x687bb
   __TEXT.__swift5_proto: 0x98
   __TEXT.__swift5_types: 0xa4
   __TEXT.__swift5_capture: 0x3cc
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__oslogstring: 0x31263
-  __TEXT.__gcc_except_tab: 0x9d48
+  __TEXT.__oslogstring: 0x313eb
+  __TEXT.__gcc_except_tab: 0x9d54
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x61f8
+  __TEXT.__unwind_info: 0x6200
   __TEXT.__eh_frame: 0x1cd8
-  __DATA_CONST.__const: 0x7da0
-  __DATA_CONST.__cfstring: 0x1aec0
+  __DATA_CONST.__const: 0x7dc0
+  __DATA_CONST.__cfstring: 0x1aee0
   __DATA_CONST.__objc_classlist: 0x990
   __DATA_CONST.__objc_catlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x270

   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x6a0
   __DATA_CONST.__objc_intobj: 0x3d8
-  __DATA_CONST.__objc_arraydata: 0xc88
+  __DATA_CONST.__objc_arraydata: 0xca0
   __DATA_CONST.__objc_dictobj: 0x230
-  __DATA_CONST.__objc_arrayobj: 0x528
-  __DATA_CONST.__auth_got: 0x1968
+  __DATA_CONST.__objc_arrayobj: 0x540
+  __DATA_CONST.__auth_got: 0x1960
   __DATA_CONST.__got: 0xf30
   __DATA_CONST.__auth_ptr: 0x298
-  __DATA.__objc_const: 0x23760
-  __DATA.__objc_selrefs: 0xb7a8
-  __DATA.__objc_ivar: 0x199c
+  __DATA.__objc_const: 0x23740
+  __DATA.__objc_selrefs: 0xb7b0
+  __DATA.__objc_ivar: 0x1998
   __DATA.__objc_data: 0x6b30
   __DATA.__data: 0x2378
-  __DATA.__bss: 0x1928
+  __DATA.__bss: 0x1938
   __DATA.__common: 0x48
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8925
-  Symbols:   1317
-  CStrings:  18396
+  Functions: 8928
+  Symbols:   1316
+  CStrings:  18401
 
Symbols:
- _MBDeviceCoverGlassColor
CStrings:
+ "%@ is a local storage app domain - not removing from the disabled domains list"
+ "%s local files domains \"%{public}@\""
+ "=backoff= ServerKeySync failureCount:%lu, backoff:%G"
+ "=ckrestore-engine= Failed to remove incomplete restore directories: %@"
+ "=quota-calculation= Adding local storage domain size %@ to DocumentsApp (total: %@)"
+ "AppDomain-com.apple.DocumentsApp"
+ "Cleanup: Failed to remove incomplete restore dirs: %@"
+ "Cleanup: Removing stale incomplete restore dirs"
+ "Failed to remove incomplete restore directories: %@"
+ "ServerKeySyncFailureCount"
+ "ServerKeySyncRetryAfter"
+ "_dependentDomainsForDisabledDomains:"
+ "_shortenRetryAfterOnUnlockForFailureCountKey:retryAfterKey:"
+ "createIncompleteRestoreDirectoriesWithError:"
+ "isRetryableServerKeySyncError:"
+ "removeIncompleteRestoreDirectoriesWithError:"
+ "removeIntermediateRestoreDirectoriesWithError:"
+ "syncDisabledDomainsWithInstalledAppDomains:persona:"
- "Cleanup: Failed to remove %@ : %@"
- "Cleanup: Finished removing %@"
- "Cleanup: Removing %@"
- "DeviceCoverGlassColor"
- "T@\"NSString\",R,V_deviceCoverGlassColor"
- "_cleanupStaleRestorePath:"
- "_deviceCoverGlassColor"
- "_subdomainNamesForAppDomainNames:"
- "_syncDisabledDomainsWithAllInstalledAppDomains:persona:"
- "allDisabledDomainNames"
- "cleanupRestoreDirectoriesWithError:"
- "createRestoreDirectoriesWithError:"
- "deviceCoverGlassColor"
```
