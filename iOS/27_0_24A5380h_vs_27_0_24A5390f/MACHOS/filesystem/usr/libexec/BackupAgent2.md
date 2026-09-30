## BackupAgent2

> `/usr/libexec/BackupAgent2`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-3038.0.0.0.0
-  __TEXT.__text: 0x907ec
+3039.0.1.0.0
+  __TEXT.__text: 0x90c98
   __TEXT.__auth_stubs: 0x1850
-  __TEXT.__objc_stubs: 0xc9a0
+  __TEXT.__objc_stubs: 0xc9c0
   __TEXT.__objc_methlist: 0x5ffc
-  __TEXT.__const: 0x4b8
-  __TEXT.__cstring: 0x18eed
-  __TEXT.__oslogstring: 0xdeda
-  __TEXT.__objc_methname: 0xe7e3
+  __TEXT.__const: 0x4c8
+  __TEXT.__cstring: 0x18fb5
+  __TEXT.__oslogstring: 0xdf81
+  __TEXT.__objc_methname: 0xe80d
   __TEXT.__objc_classname: 0xa09
   __TEXT.__objc_methtype: 0x1e9d
-  __TEXT.__gcc_except_tab: 0x2100
-  __TEXT.__unwind_info: 0x1948
-  __DATA_CONST.__const: 0x1418
-  __DATA_CONST.__cfstring: 0x94e0
+  __TEXT.__gcc_except_tab: 0x210c
+  __TEXT.__unwind_info: 0x1940
+  __DATA_CONST.__const: 0x1438
+  __DATA_CONST.__cfstring: 0x9500
   __DATA_CONST.__objc_classlist: 0x388
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x98

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x230
   __DATA_CONST.__objc_intobj: 0xa8
-  __DATA_CONST.__objc_arraydata: 0x110
-  __DATA_CONST.__objc_arrayobj: 0xd8
+  __DATA_CONST.__objc_arraydata: 0x120
+  __DATA_CONST.__objc_arrayobj: 0xf0
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__auth_got: 0xc38
   __DATA_CONST.__got: 0x588

   __DATA.__objc_ivar: 0x558
   __DATA.__objc_data: 0x2350
   __DATA.__data: 0x818
-  __DATA.__bss: 0x220
+  __DATA.__bss: 0x230
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2452
+  Functions: 2455
   Symbols:   558
-  CStrings:  5759
+  CStrings:  5763
 
CStrings:
+ "%@ is a local storage app domain - not removing from the disabled domains list"
+ "%s local files domains \"%{public}@\""
+ "AppDomain-com.apple.DocumentsApp"
+ "Failed to remove incomplete restore directories: %@"
+ "_dependentDomainsForDisabledDomains:"
+ "createIncompleteRestoreDirectoriesWithError:"
+ "removeIncompleteRestoreDirectoriesWithError:"
+ "removeIntermediateRestoreDirectoriesWithError:"
+ "syncDisabledDomainsWithInstalledAppDomains:persona:"
- "_subdomainNamesForAppDomainNames:"
- "_syncDisabledDomainsWithAllInstalledAppDomains:persona:"
- "allDisabledDomainNames"
- "cleanupRestoreDirectoriesWithError:"
- "createRestoreDirectoriesWithError:"
```
