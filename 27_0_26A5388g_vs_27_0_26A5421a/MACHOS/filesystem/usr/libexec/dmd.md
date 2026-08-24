## dmd

> `/usr/libexec/dmd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-260.0.0.0.0
-  __TEXT.__text: 0x607c4
-  __TEXT.__auth_stubs: 0x9a0
-  __TEXT.__objc_stubs: 0x9980
+261.1.5.0.0
+  __TEXT.__text: 0x615d0
+  __TEXT.__auth_stubs: 0xa00
+  __TEXT.__objc_stubs: 0x9a00
   __TEXT.__objc_methlist: 0x6724
-  __TEXT.__const: 0x150
+  __TEXT.__const: 0x170
   __TEXT.__objc_classname: 0x1b16
-  __TEXT.__objc_methname: 0xc3aa
+  __TEXT.__objc_methname: 0xc428
   __TEXT.__objc_methtype: 0x16be
-  __TEXT.__cstring: 0x43dc
-  __TEXT.__oslogstring: 0x6c4a
+  __TEXT.__cstring: 0x472d
+  __TEXT.__oslogstring: 0x7049
   __TEXT.__gcc_except_tab: 0xc04
   __TEXT.__ustring: 0x498
-  __TEXT.__unwind_info: 0x1a20
+  __TEXT.__unwind_info: 0x1a30
   __DATA_CONST.__const: 0x1880
-  __DATA_CONST.__cfstring: 0x4820
+  __DATA_CONST.__cfstring: 0x4940
   __DATA_CONST.__objc_classlist: 0x638
   __DATA_CONST.__objc_catlist: 0x170
   __DATA_CONST.__objc_protolist: 0xf8

   __DATA_CONST.__objc_intobj: 0x2d0
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x140
-  __DATA_CONST.__auth_got: 0x4e0
-  __DATA_CONST.__got: 0xf90
+  __DATA_CONST.__auth_got: 0x510
+  __DATA_CONST.__got: 0xf98
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x1ab28
-  __DATA.__objc_selrefs: 0x2c20
+  __DATA.__objc_selrefs: 0x2c40
   __DATA.__objc_ivar: 0x37c
   __DATA.__objc_data: 0x3e30
   __DATA.__data: 0xba8

   - /System/Library/PrivateFrameworks/login.framework/Versions/A/login
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2416
-  Symbols:   700
-  CStrings:  3237
+  Functions: 2431
+  Symbols:   707
+  CStrings:  3263
 
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
