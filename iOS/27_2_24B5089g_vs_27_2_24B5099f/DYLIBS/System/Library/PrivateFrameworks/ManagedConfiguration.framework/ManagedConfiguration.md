## ManagedConfiguration

> `/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration`

```diff

-2483.40.14.0.0
-  __TEXT.__text: 0xf2380
-  __TEXT.__objc_methlist: 0xb2ec
+2483.40.19.0.0
+  __TEXT.__text: 0xf2ae8
+  __TEXT.__objc_methlist: 0xb35c
   __TEXT.__const: 0x1584
-  __TEXT.__cstring: 0x1878f
-  __TEXT.__oslogstring: 0x96c3
-  __TEXT.__gcc_except_tab: 0x1048
+  __TEXT.__cstring: 0x187d2
+  __TEXT.__oslogstring: 0x9892
+  __TEXT.__gcc_except_tab: 0x1080
   __TEXT.__dlopen_cstrs: 0xac
   __TEXT.__ustring: 0x50
-  __TEXT.__unwind_info: 0x45f0
+  __TEXT.__unwind_info: 0x4618
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4dd8
+  __DATA_CONST.__const: 0x4e00
   __DATA_CONST.__objc_classlist: 0x3d8
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5e00
+  __DATA_CONST.__objc_selrefs: 0x5e48
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x2d0
   __DATA_CONST.__objc_arraydata: 0xe8
   __DATA_CONST.__got: 0xac0
   __AUTH_CONST.__const: 0x2110
-  __AUTH_CONST.__cfstring: 0x19720
-  __AUTH_CONST.__objc_const: 0xd7e8
+  __AUTH_CONST.__cfstring: 0x19760
+  __AUTH_CONST.__objc_const: 0xd850
   __AUTH_CONST.__objc_intobj: 0x4f8
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__auth_got: 0xbf8
   __AUTH.__objc_data: 0x2350
-  __DATA.__objc_ivar: 0x994
+  __DATA.__objc_ivar: 0x99c
   __DATA.__data: 0xcc8
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x320

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5814
-  Symbols:   9726
-  CStrings:  4629
+  Functions: 5824
+  Symbols:   9740
+  CStrings:  4637
 
Symbols:
+ +[MCManifest _fileDataIfPresentAtPath:error:]
+ +[MCManifest installedProfileDataWithIdentifier:error:]
+ +[MCManifest installedSystemProfileDataWithIdentifier:error:]
+ +[MCManifest installedUserProfileDataWithIdentifier:error:]
+ -[MCManifest identifiersOfProfilesWithFilterFlags:error:]
+ -[MCManifest setSystemManifestLoadError:]
+ -[MCManifest setUserManifestLoadError:]
+ -[MCManifest systemManifestLoadError]
+ -[MCManifest userManifestLoadError]
+ _OBJC_IVAR_$_MCManifest._systemManifestLoadError
+ _OBJC_IVAR_$_MCManifest._userManifestLoadError
+ __OBJC_$_PROP_LIST_MCManifest
+ ___57-[MCManifest identifiersOfProfilesWithFilterFlags:error:]_block_invoke
+ ___block_descriptor_72_e8_32s40r48r56r64r_e5_v8?0lr40l8s32l8r48l8r56l8r64l8
CStrings:
+ "Account %{public}@ is already owned by %{public}@; nothing to transfer"
+ "ERROR_ACCOUNT_TAKEOVER_ALREADY_MANAGED_P_ID"
+ "MCManifest could not load the system manifest at %{public}@: %{public}@"
+ "MCManifest could not load the user manifest at %{public}@: %{public}@"
+ "MCManifest could not parse the system manifest at %{public}@: %{public}@"
+ "MCManifest could not parse the user manifest at %{public}@: %{public}@"
+ "MCManifest not writing the system manifest because the one on disk could not be loaded."
+ "MCManifest not writing the user manifest because the one on disk could not be loaded."
+ "com.apple.NanoMessages"
- "Account %{public}@ already owned by %{public}@; nothing to transfer"
```
