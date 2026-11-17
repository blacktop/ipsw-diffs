## dmd

> `/usr/libexec/dmd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methtype`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-269.0.0.0.0
-  __TEXT.__text: 0x7fce8
-  __TEXT.__auth_stubs: 0xf60
-  __TEXT.__objc_stubs: 0xea40
-  __TEXT.__objc_methlist: 0x7fdc
-  __TEXT.__const: 0x178
+269.60.2.0.0
+  __TEXT.__text: 0x7ff30
+  __TEXT.__auth_stubs: 0xf00
+  __TEXT.__objc_stubs: 0xeaa0
+  __TEXT.__objc_methlist: 0x8004
+  __TEXT.__const: 0x188
   __TEXT.__objc_classname: 0x1e43
-  __TEXT.__objc_methname: 0x1190f
+  __TEXT.__objc_methname: 0x119cc
   __TEXT.__objc_methtype: 0x1d98
-  __TEXT.__cstring: 0x581c
-  __TEXT.__oslogstring: 0xb6e2
+  __TEXT.__cstring: 0x54a6
+  __TEXT.__oslogstring: 0xb654
   __TEXT.__gcc_except_tab: 0x10d4
   __TEXT.__ustring: 0x80a
   __TEXT.__dlopen_cstrs: 0xaf
-  __TEXT.__unwind_info: 0x2bf0
+  __TEXT.__unwind_info: 0x2be8
   __DATA_CONST.__const: 0x2750
-  __DATA_CONST.__cfstring: 0x5940
+  __DATA_CONST.__cfstring: 0x5800
   __DATA_CONST.__objc_classlist: 0x6f8
   __DATA_CONST.__objc_catlist: 0x1a0
   __DATA_CONST.__objc_protolist: 0x108

   __DATA_CONST.__objc_intobj: 0x318
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x7c0
-  __DATA_CONST.__got: 0x13e8
+  __DATA_CONST.__auth_got: 0x790
+  __DATA_CONST.__got: 0x13e0
   __DATA.__objc_const: 0x1d6e8
-  __DATA.__objc_selrefs: 0x41d0
+  __DATA.__objc_selrefs: 0x41f0
   __DATA.__objc_ivar: 0x430
   __DATA.__objc_data: 0x45b0
   __DATA.__data: 0xc60

   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
-  Functions: 3232
-  Symbols:   926
-  CStrings:  4552
+  Functions: 3227
+  Symbols:   920
+  CStrings:  4540
 
Symbols:
- _close
- _fts_close
- _fts_open
- _fts_read
- _lstat
- _open
CStrings:
+ "%{public}@: Failed to fetch installed declarations: %{public}@"
+ "%{public}@: Failed to remove leftover state after failed install: %{public}@"
+ "%{public}@: Removing leftover state after failed install"
+ "%{public}@: Superseding declaration of type %{public}@ will install. Skipping uninstall of the superseded declaration"
+ "Failed to convert %{public}s to a data vault, continuing without: %{darwin.errno}d"
+ "Failed to fetch declarations pending install while scrubbing policy orphans %{public}@"
+ "_endOperationMarkingPayloadMetadata:failedWithError:configuration:"
+ "_hasInstalledDeclarationWithIdentifierOfPayloadMetadata:"
+ "_leftoverStateRemovalOperationDidFinish:installError:"
+ "countForFetchRequest:error:"
- "%{public}@: Newer declaration of type %{public}@ found. Removing old one from DB to skip uninstall"
- "dmd data vault: dmd_vaultDied_childUnreadable (errno=%d)"
- "dmd data vault: dmd_vaultDied_cleanButFailed (errno=%d)"
- "dmd data vault: dmd_vaultDied_dirUnreadable (errno=%d)"
- "dmd data vault: dmd_vaultDied_notDirectory (errno=%d)"
- "dmd data vault: dmd_vaultDied_openOther (errno=%d)"
- "dmd data vault: dmd_vaultDied_ownerOther (errno=%d)"
- "dmd data vault: dmd_vaultDied_ownerRoot (errno=%d)"
- "dmd data vault: dmd_vaultDied_statENOENT (errno=%d)"
- "dmd data vault: dmd_vaultDied_statOther (errno=%d)"
- "dmd data vault: dmd_vaultDied_symlink (errno=%d)"
- "initWithObjects:"
- "void dmd_vaultDied_childUnreadable(int)"
- "void dmd_vaultDied_cleanButFailed(int)"
- "void dmd_vaultDied_dirUnreadable(int)"
- "void dmd_vaultDied_notDirectory(int)"
- "void dmd_vaultDied_openOther(int)"
- "void dmd_vaultDied_ownerOther(int)"
- "void dmd_vaultDied_ownerRoot(int)"
- "void dmd_vaultDied_statENOENT(int)"
- "void dmd_vaultDied_statOther(int)"
- "void dmd_vaultDied_symlink(int)"
```
