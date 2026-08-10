## RemoteManagementStore

> `/System/Library/PrivateFrameworks/RemoteManagementStore.framework/RemoteManagementStore`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-624.0.10.0.0
-  __TEXT.__text: 0x3aef0
-  __TEXT.__objc_methlist: 0x2420
-  __TEXT.__const: 0x53c
+624.2.3.0.0
+  __TEXT.__text: 0x3b9b0
+  __TEXT.__objc_methlist: 0x2468
+  __TEXT.__const: 0x54c
   __TEXT.__cstring: 0x112c
-  __TEXT.__oslogstring: 0x3407
+  __TEXT.__oslogstring: 0x3437
   __TEXT.__gcc_except_tab: 0x3a4
   __TEXT.__swift5_typeref: 0x2d3
-  __TEXT.__swift5_fieldmd: 0xd0
+  __TEXT.__swift5_fieldmd: 0xdc
   __TEXT.__constg_swiftt: 0xc4
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_reflstr: 0x164
+  __TEXT.__swift5_reflstr: 0x184
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x24

   __TEXT.__swift_as_entry: 0x34
   __TEXT.__swift_as_ret: 0x5c
   __TEXT.__swift_as_cont: 0xb8
-  __TEXT.__unwind_info: 0xea0
+  __TEXT.__unwind_info: 0xec8
   __TEXT.__eh_frame: 0xb68
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1598
+  __DATA_CONST.__objc_selrefs: 0x15c0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x108
   __DATA_CONST.__objc_arraydata: 0x50
-  __DATA_CONST.__got: 0x400
+  __DATA_CONST.__got: 0x410
   __AUTH_CONST.__const: 0x818
   __AUTH_CONST.__cfstring: 0x1040
-  __AUTH_CONST.__objc_const: 0x36b8
+  __AUTH_CONST.__objc_const: 0x36f0
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x6b0
   __AUTH.__objc_data: 0x48
-  __DATA.__objc_ivar: 0x1b0
+  __DATA.__objc_ivar: 0x1b4
   __DATA.__data: 0x5d0
   __DATA.__bss: 0x570
   __DATA.__common: 0x18

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1351
-  Symbols:   2311
+  Functions: 1362
+  Symbols:   2325
   CStrings:  469
 
Symbols:
+ +[RMAssetResolverController _fetchDeclarationWithAssetIdentifier:storeIdentifier:scope:completionHandler:]
+ +[RMAssetResolverController _resolveDataAsset:assetIdentifier:store:completionHandler:]
+ +[RMAssetResolverController resolveDataAssetWithAssetIdentifier:storeIdentifier:scope:completionHandler:]
+ -[RMStoreResolvedAsset serverReportedContentType]
+ -[RMStoreResolvedAsset setServerReportedContentType:]
+ _OBJC_CLASS_$_RMModelSecurityCertificateDeclaration
+ _OBJC_IVAR_$_RMStoreResolvedAsset._serverReportedContentType
+ _RMConfigurationTypeExtensibleSSO
+ ___105+[RMAssetResolverController resolveDataAssetWithAssetIdentifier:storeIdentifier:scope:completionHandler:]_block_invoke
+ ___106+[RMAssetResolverController _fetchDeclarationWithAssetIdentifier:storeIdentifier:scope:completionHandler:]_block_invoke
+ ___106+[RMAssetResolverController _fetchDeclarationWithAssetIdentifier:storeIdentifier:scope:completionHandler:]_block_invoke_2
+ ___87+[RMAssetResolverController _resolveDataAsset:assetIdentifier:store:completionHandler:]_block_invoke
+ ___87+[RMAssetResolverController _resolveDataAsset:assetIdentifier:store:completionHandler:]_block_invoke_2
+ ___block_descriptor_56_e8_32s40bs_e66_v32?0"RMModelDeclarationBase"8"RMSubscriberStore"16"NSError"24ls40l8s32l8
+ ___block_descriptor_64_e8_32s40s48bs_e66_v32?0"RMModelDeclarationBase"8"RMSubscriberStore"16"NSError"24ls48l8s32l8s40l8
+ _objc_msgSend$_fetchDeclarationWithAssetIdentifier:storeIdentifier:scope:completionHandler:
+ _objc_msgSend$_resolveDataAsset:assetIdentifier:store:completionHandler:
- ___117+[RMAssetResolverController resolveDataAssetWithAssetIdentifier:downloadURL:storeIdentifier:scope:completionHandler:]_block_invoke_2
- ___block_descriptor_64_e8_32s40s48bs_e39_v24?0"RMSubscriberStore"8"NSError"16ls48l8s32l8s40l8
- ___block_descriptor_72_e8_32s40s48s56bs_e44_v24?0"RMModelDeclarationBase"8"NSError"16ls56l8s32l8s40l8s48l8
CStrings:
+ "Activation does not reference configuration %s: %s"
+ "Missing app configuration"
+ "Missing extensible SSO configuration or legacy profile"
- "Activation does not reference configuration: %s"
- "Missing configuration"
- "No app configuration found"
```
