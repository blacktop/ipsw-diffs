## dmd

> `/usr/libexec/dmd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
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

-260.0.0.0.0
-  __TEXT.__text: 0x81558
-  __TEXT.__auth_stubs: 0xf00
-  __TEXT.__objc_stubs: 0xe980
+261.2.5.0.0
+  __TEXT.__text: 0x822c0
+  __TEXT.__auth_stubs: 0xf60
+  __TEXT.__objc_stubs: 0xea00
   __TEXT.__objc_methlist: 0x7fdc
-  __TEXT.__const: 0x168
+  __TEXT.__const: 0x180
   __TEXT.__objc_classname: 0x1e43
-  __TEXT.__objc_methname: 0x1186f
+  __TEXT.__objc_methname: 0x118ed
   __TEXT.__objc_methtype: 0x1d98
-  __TEXT.__cstring: 0x54ae
-  __TEXT.__oslogstring: 0xb2a0
+  __TEXT.__cstring: 0x57ff
+  __TEXT.__oslogstring: 0xb69f
   __TEXT.__gcc_except_tab: 0x10bc
   __TEXT.__ustring: 0x80a
   __TEXT.__dlopen_cstrs: 0xaf
   __TEXT.__unwind_info: 0x2218
   __DATA_CONST.__const: 0x2748
-  __DATA_CONST.__cfstring: 0x5800
+  __DATA_CONST.__cfstring: 0x5920
   __DATA_CONST.__objc_classlist: 0x6f8
   __DATA_CONST.__objc_catlist: 0x1a0
   __DATA_CONST.__objc_protolist: 0x108

   __DATA_CONST.__objc_intobj: 0x318
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x790
-  __DATA_CONST.__got: 0x13e0
+  __DATA_CONST.__auth_got: 0x7c0
+  __DATA_CONST.__got: 0x13e8
   __DATA.__objc_const: 0x1d6e8
-  __DATA.__objc_selrefs: 0x41a0
+  __DATA.__objc_selrefs: 0x41c0
   __DATA.__objc_ivar: 0x430
   __DATA.__objc_data: 0x45b0
   __DATA.__data: 0xc60

   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
-  Functions: 3220
-  Symbols:   919
-  CStrings:  4522
+  Functions: 3231
+  Symbols:   926
+  CStrings:  4548
 
Symbols:
+ _MOScreenTimeShieldPolicyBlocked
+ _close
+ _fts_close
+ _fts_open
+ _fts_read
+ _lstat
+ _open
CStrings:
+ "Requested application %{public}@ is exempt from the application-category shield because its associated site %{private}@ is excluded from the web-category shield"
+ "Requested website %{sensitive}@ is excepted (%{private}@ excluded from the web-category shield); dropping any associated-app direct shield so it does not re-shield via its app"
+ "Requested website %{sensitive}@ is exempt from the web-category shield because its associated app %{public}@ is excluded from the application-category shield"
+ "applicationShieldPolicies"
+ "dmd data vault: dmd_vaultDied_childUnreadable (errno=%d)"
+ "dmd data vault: dmd_vaultDied_cleanButFailed (errno=%d)"
+ "dmd data vault: dmd_vaultDied_dirUnreadable (errno=%d)"
+ "dmd data vault: dmd_vaultDied_notDirectory (errno=%d)"
+ "dmd data vault: dmd_vaultDied_openOther (errno=%d)"
+ "dmd data vault: dmd_vaultDied_ownerOther (errno=%d)"
+ "dmd data vault: dmd_vaultDied_ownerRoot (errno=%d)"
+ "dmd data vault: dmd_vaultDied_statENOENT (errno=%d)"
+ "dmd data vault: dmd_vaultDied_statOther (errno=%d)"
+ "dmd data vault: dmd_vaultDied_symlink (errno=%d)"
+ "excludesIdentifier:"
+ "policyByAddingExcludedIdentifiers:"
+ "policyByRemovingIdentifiers:minimumPriority:"
+ "void dmd_vaultDied_childUnreadable(int)"
+ "void dmd_vaultDied_cleanButFailed(int)"
+ "void dmd_vaultDied_dirUnreadable(int)"
+ "void dmd_vaultDied_notDirectory(int)"
+ "void dmd_vaultDied_openOther(int)"
+ "void dmd_vaultDied_ownerOther(int)"
+ "void dmd_vaultDied_ownerRoot(int)"
+ "void dmd_vaultDied_statENOENT(int)"
+ "void dmd_vaultDied_statOther(int)"
+ "void dmd_vaultDied_symlink(int)"
- "Failed to enable data vault: %@ (%d)"
```
