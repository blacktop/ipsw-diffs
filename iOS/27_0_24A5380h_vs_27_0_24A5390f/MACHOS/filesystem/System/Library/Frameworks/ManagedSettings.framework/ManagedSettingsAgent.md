## ManagedSettingsAgent

> `/System/Library/Frameworks/ManagedSettings.framework/ManagedSettingsAgent`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__objc_methname`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_capture`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-302.0.0.0.0
-  __TEXT.__text: 0x70910
-  __TEXT.__auth_stubs: 0x1f40
+304.0.0.0.0
+  __TEXT.__text: 0x72f28
+  __TEXT.__auth_stubs: 0x1f60
   __TEXT.__objc_stubs: 0xb60
   __TEXT.__objc_methlist: 0x608
-  __TEXT.__const: 0x1c4c
+  __TEXT.__const: 0x1c3c
   __TEXT.__objc_classname: 0x77c
   __TEXT.__objc_methtype: 0xba2
   __TEXT.__objc_methname: 0x19e5
-  __TEXT.__cstring: 0x7c5
+  __TEXT.__cstring: 0x7e5
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x1000
+  __TEXT.__constg_swiftt: 0x1038
   __TEXT.__swift5_typeref: 0x1031
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_reflstr: 0xb85
-  __TEXT.__swift5_fieldmd: 0x9e8
+  __TEXT.__swift5_reflstr: 0xb95
+  __TEXT.__swift5_fieldmd: 0x9f4
   __TEXT.__swift5_assocty: 0xa8
   __TEXT.__swift5_proto: 0x128
   __TEXT.__swift5_types: 0x90
-  __TEXT.__oslogstring: 0x2e42
+  __TEXT.__oslogstring: 0x2ee2
   __TEXT.__swift5_protos: 0x34
   __TEXT.__swift5_capture: 0x3a0
-  __TEXT.__unwind_info: 0xc78
-  __TEXT.__eh_frame: 0x1cc8
-  __DATA_CONST.__const: 0x1c30
+  __TEXT.__unwind_info: 0xc98
+  __TEXT.__eh_frame: 0x1d38
+  __DATA_CONST.__const: 0x1be0
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x78
-  __DATA_CONST.__auth_got: 0xfa8
+  __DATA_CONST.__auth_got: 0xfb8
   __DATA_CONST.__got: 0x490
   __DATA_CONST.__auth_ptr: 0x400
-  __DATA.__objc_const: 0x1e58
+  __DATA.__objc_const: 0x1e78
   __DATA.__objc_selrefs: 0x428
   __DATA.__objc_data: 0x2c0
-  __DATA.__data: 0x1ed0
+  __DATA.__data: 0x1f18
   __DATA.__bss: 0x1a90
   __DATA.__common: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1064
-  Symbols:   748
-  CStrings:  547
+  Functions: 1063
+  Symbols:   750
+  CStrings:  551
 
Symbols:
+ _$s19DeviceConfiguration5StoreV09valuesForB2IDSDySSSDySSs8Sendable_pGGvg
+ _$s19DeviceConfiguration8ProviderP23getStoreIdentifiersSync3forSayAA0E10IdentifierCGSS_tKFZTj
CStrings:
+ ".tokenized.plist"
+ "Failed to purge DC store. Error: %@"
+ "Failed to update store in DC. Error: %@"
+ "Unable to check tokenized.plist for store with name %{public}s."
+ "Unable to delete %{public}s: Path doesn't exist."
+ "deleted now-empty store %{public}s"
+ "no DC store for %{public}s, skipping property update"
- "Failed to update store in DC. Erro: %@"
- "Unable to delete %{public}s: Path doesn't exist!"
- "Unable to settings files for store with name %{public}s."
```
