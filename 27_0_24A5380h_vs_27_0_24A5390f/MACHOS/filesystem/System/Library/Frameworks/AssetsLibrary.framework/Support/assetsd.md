## assetsd

> `/System/Library/Frameworks/AssetsLibrary.framework/Support/assetsd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`

```diff

-910.27.103.0.0
-  __TEXT.__text: 0x180a4
+910.33.102.0.0
+  __TEXT.__text: 0x1827c
   __TEXT.__auth_stubs: 0xb40
-  __TEXT.__objc_stubs: 0x4a60
-  __TEXT.__objc_methlist: 0xdec
+  __TEXT.__objc_stubs: 0x4ac0
+  __TEXT.__objc_methlist: 0xe14
   __TEXT.__dlopen_cstrs: 0x11b
   __TEXT.__const: 0x110
   __TEXT.__gcc_except_tab: 0x554
-  __TEXT.__objc_classname: 0x6bb
-  __TEXT.__objc_methname: 0x554b
-  __TEXT.__objc_methtype: 0x91d
-  __TEXT.__oslogstring: 0x3fa6
-  __TEXT.__cstring: 0x174a
-  __TEXT.__unwind_info: 0x540
+  __TEXT.__objc_classname: 0x6e1
+  __TEXT.__objc_methname: 0x563c
+  __TEXT.__objc_methtype: 0x98d
+  __TEXT.__oslogstring: 0x3ff7
+  __TEXT.__cstring: 0x175e
+  __TEXT.__unwind_info: 0x548
   __DATA_CONST.__const: 0xf10
-  __DATA_CONST.__cfstring: 0xb20
+  __DATA_CONST.__cfstring: 0xb60
   __DATA_CONST.__objc_classlist: 0x160
-  __DATA_CONST.__objc_protolist: 0x40
+  __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_intobj: 0x78

   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__auth_got: 0x5b0
   __DATA_CONST.__got: 0x700
-  __DATA.__objc_const: 0x2cd0
-  __DATA.__objc_selrefs: 0x1468
-  __DATA.__objc_ivar: 0x80
+  __DATA.__objc_const: 0x2cd8
+  __DATA.__objc_selrefs: 0x1490
+  __DATA.__objc_ivar: 0x7c
   __DATA.__objc_data: 0xdc0
-  __DATA.__data: 0x300
+  __DATA.__data: 0x360
   __DATA.__bss: 0x58
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 357
+  Functions: 358
   Symbols:   416
-  CStrings:  1247
+  CStrings:  1257
 
CStrings:
+ "@\"PLManagedAsset\"48@0:8@\"PHServerResourceRequestRunner\"16@\"NSURL\"24@\"PLPhotoLibrary\"32^@40"
+ "@48@0:8@16@24@32^@40"
+ "PHServerResourceRequestRunnerDelegate"
+ "[RM]: unable to access asset with object ID %{public}@ for client %{public}@: %@"
+ "authorizedAssetForObjectIDURL:relationshipKeyPathsForPrefetching:inLibrary:error:"
+ "connectionAuthorization"
+ "initWithLibraryServicesManager:connectionAuthorization:"
+ "initWithLibraryServicesManager:connectionAuthorization:shellObject:clientPid:"
+ "initWithTaskIdentifier:delegate:"
+ "master"
+ "modernResources"
+ "resourceRequestRunner:authorizedAssetForObjectIDURL:inLibrary:error:"
+ "trustedCallerBundleID"
- "_trustedCallerBundleID"
- "initWithLibraryServicesManager:shellObject:trustedCallerBundleID:clientPid:"
- "initWithTaskIdentifier:"
```
