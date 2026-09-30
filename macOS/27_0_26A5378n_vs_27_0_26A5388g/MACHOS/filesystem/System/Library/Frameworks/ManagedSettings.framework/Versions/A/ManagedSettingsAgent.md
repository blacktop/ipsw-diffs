## ManagedSettingsAgent

> `/System/Library/Frameworks/ManagedSettings.framework/Versions/A/ManagedSettingsAgent`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__objc_methname`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_capture`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__bss`

```diff

-302.0.0.0.0
-  __TEXT.__text: 0x665e0
-  __TEXT.__auth_stubs: 0x1af0
+304.0.0.0.0
+  __TEXT.__text: 0x68630
+  __TEXT.__auth_stubs: 0x1b20
   __TEXT.__objc_stubs: 0x900
   __TEXT.__objc_methlist: 0x4b4
   __TEXT.__const: 0x1b4c
-  __TEXT.__cstring: 0x7c5
+  __TEXT.__cstring: 0x7e5
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0xf20
+  __TEXT.__constg_swiftt: 0xf38
   __TEXT.__swift5_typeref: 0xe71
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_reflstr: 0xae1
-  __TEXT.__swift5_fieldmd: 0x948
+  __TEXT.__swift5_reflstr: 0xaf1
+  __TEXT.__swift5_fieldmd: 0x954
   __TEXT.__swift5_assocty: 0xa8
   __TEXT.__swift5_proto: 0x128
   __TEXT.__swift5_types: 0x88
   __TEXT.__objc_classname: 0x68c
   __TEXT.__objc_methtype: 0x992
   __TEXT.__objc_methname: 0x1649
-  __TEXT.__oslogstring: 0x2a02
+  __TEXT.__oslogstring: 0x2aa2
   __TEXT.__swift5_protos: 0x2c
   __TEXT.__swift5_capture: 0x2cc
-  __TEXT.__unwind_info: 0xb60
-  __TEXT.__eh_frame: 0x1b88
+  __TEXT.__unwind_info: 0xb70
+  __TEXT.__eh_frame: 0x1bf8
   __DATA_CONST.__const: 0x16b8
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x70
-  __DATA_CONST.__auth_got: 0xd80
+  __DATA_CONST.__auth_got: 0xd98
   __DATA_CONST.__got: 0x480
   __DATA_CONST.__auth_ptr: 0x3e0
-  __DATA.__objc_const: 0x1a48
+  __DATA.__objc_const: 0x1a68
   __DATA.__objc_selrefs: 0x390
   __DATA.__objc_data: 0x180
-  __DATA.__data: 0x1d28
+  __DATA.__data: 0x1d48
   __DATA.__common: 0x48
   __DATA.__bss: 0x1c00
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 948
-  Symbols:   672
-  CStrings:  485
+  Functions: 949
+  Symbols:   675
+  CStrings:  489
 
Symbols:
+ _$s19DeviceConfiguration5StoreV09valuesForB2IDSDySSSDySSs8Sendable_pGGvg
+ _$s19DeviceConfiguration8ProviderP23getStoreIdentifiersSync3forSayAA0E10IdentifierCGSS_tKFZTj
+ _$sSo13os_log_type_ta0A0E5faultABvgZ
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
