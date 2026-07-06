## RemoteManagement

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/RemoteManagement`

```diff

-  __TEXT.__text: 0x4bd30
+  __TEXT.__text: 0x4bc50
   __TEXT.__objc_methlist: 0x1bd0
-  __TEXT.__const: 0x17fc
-  __TEXT.__cstring: 0x2337
-  __TEXT.__oslogstring: 0x49ab
+  __TEXT.__const: 0x180c
+  __TEXT.__cstring: 0x2357
+  __TEXT.__oslogstring: 0x492b
   __TEXT.__gcc_except_tab: 0x41c
   __TEXT.__swift5_typeref: 0x63b
-  __TEXT.__constg_swiftt: 0x9a0
+  __TEXT.__constg_swiftt: 0x9a8
   __TEXT.__swift5_reflstr: 0x303
   __TEXT.__swift5_fieldmd: 0x488
   __TEXT.__swift5_proto: 0x114

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0xf50
-  __TEXT.__eh_frame: 0x15a4
+  __TEXT.__unwind_info: 0xf60
+  __TEXT.__eh_frame: 0x15d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_selrefs: 0x13e8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x68
-  __DATA_CONST.__got: 0x590
+  __DATA_CONST.__got: 0x598
   __AUTH_CONST.__const: 0xbf0
-  __AUTH_CONST.__cfstring: 0x1ac0
+  __AUTH_CONST.__cfstring: 0x1ae0
   __AUTH_CONST.__objc_const: 0x2ea8
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH_CONST.__auth_got: 0xb50
-  __AUTH.__objc_data: 0x568
-  __AUTH.__data: 0x828
+  __AUTH_CONST.__auth_got: 0xb68
+  __AUTH.__objc_data: 0x7f0
+  __AUTH.__data: 0xab8
   __DATA.__objc_ivar: 0xc8
   __DATA.__data: 0x6c8
-  __DATA.__bss: 0x23d0
+  __DATA.__bss: 0x23c0
   __DATA.__common: 0x30
-  __DATA_DIRTY.__objc_data: 0x670
-  __DATA_DIRTY.__data: 0x290
+  __DATA_DIRTY.__objc_data: 0x3e8
+  __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x68
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   Functions: 1387
-  Symbols:   3067
-  CStrings:  904
+  Symbols:   3054
+  CStrings:  905
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift5_protos : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __DATA.__data : content changed
Symbols:
+ +[RMErrorUtilities createMissingStatusValueErrorWithKeyPath:]
+ _RMSwitchToDaemonUserIfNeeded
+ _RMSwitchToMobileUserIfNeeded
+ _geteuid
+ _getpwnam
+ _setuid
- +[RMLocations _applicationSupportChildDirectoryURLInDomain:createIfNeeded:childName:descriptor:]
- ___96+[RMLocations _applicationSupportChildDirectoryURLInDomain:createIfNeeded:childName:descriptor:]_block_invoke
- __applicationSupportChildDirectoryURLInDomain:createIfNeeded:childName:descriptor:.onceToken
- _objc_msgSend$_oneTimeDataVaultConversionInDomain:dataVaultDirectoryURL:
CStrings:
+ "Darwin User directory is %{public}@"
+ "Error.MissingStatusValue_%@"
+ "mobile"
- "Failed to find Application Support directory: %{public}@"
- "Failed to find Data Vault directory: %{public}@"
- "Unable to create Data Vault at %{public}@: %{public}@"

```
