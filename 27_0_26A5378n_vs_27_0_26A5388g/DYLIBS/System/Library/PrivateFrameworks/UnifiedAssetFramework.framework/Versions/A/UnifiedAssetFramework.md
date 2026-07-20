## UnifiedAssetFramework

> `/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/Versions/A/UnifiedAssetFramework`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_types`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-3600.70.1.0.0
-  __TEXT.__text: 0x7fc30
-  __TEXT.__objc_methlist: 0x3658
+3600.74.1.0.0
+  __TEXT.__text: 0x801c8
+  __TEXT.__objc_methlist: 0x3670
   __TEXT.__const: 0x198
   __TEXT.__constg_swiftt: 0x48
   __TEXT.__swift5_typeref: 0x67
   __TEXT.__swift5_reflstr: 0x9
   __TEXT.__swift5_fieldmd: 0x1c
-  __TEXT.__cstring: 0xb7ad
-  __TEXT.__oslogstring: 0xeffd
+  __TEXT.__cstring: 0xb7e7
+  __TEXT.__oslogstring: 0xf115
   __TEXT.__swift5_types: 0x4
   __TEXT.__gcc_except_tab: 0xe30
-  __TEXT.__unwind_info: 0x1228
+  __TEXT.__unwind_info: 0x1230
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2678
+  __DATA_CONST.__objc_selrefs: 0x2688
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x130

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1514
-  Symbols:   3836
-  CStrings:  2115
+  Functions: 1517
+  Symbols:   3841
+  CStrings:  2120
 
Symbols:
+ -[UAFRootsV2AssetSet assetWithName:specifier:experiment:]
+ -[UAFRootsV2AssetSet availableExperimentalSpecifiersForExperiment:]
+ ___57-[UAFRootsV2AssetSet assetWithName:specifier:experiment:]_block_invoke
+ ___67-[UAFRootsV2AssetSet availableExperimentalSpecifiersForExperiment:]_block_invoke
+ _objc_msgSend$assetWithName:specifier:experiment:
+ _objc_msgSend$availableExperimentalSpecifiersForExperiment:
- __44-[UAFRootsV2AssetSet loadAssets:experiment:]_block_invoke
CStrings:
+ "%s %{public}@: Cannot resolve %{public}@ from roots V2 for %{public}@: lock not held"
+ "%s %{public}@: No Roots V2 asset for %{public}@, returning nil (exclusive)"
+ "%s %{public}@: No specifier for %{public}@ in roots V2 for %{public}@"
+ "%s %{public}@: Returning %{public}@ from Roots V2"
+ "-[UAFRootsV2AssetSet assetWithName:specifier:experiment:]"
```
