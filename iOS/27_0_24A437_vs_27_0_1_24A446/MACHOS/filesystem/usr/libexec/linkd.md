## linkd

> `/usr/libexec/linkd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-301.0.51.1.104
+301.0.51.1.105
   __TEXT.__text: 0x1a4d80
   __TEXT.__auth_stubs: 0x3c40
   __TEXT.__objc_stubs: 0x3b40

   __TEXT.__swift_as_entry: 0xab0
   __TEXT.__swift_as_ret: 0xa64
   __TEXT.__swift_as_cont: 0xc88
-  __TEXT.__oslogstring: 0x658f
+  __TEXT.__oslogstring: 0x659f
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__unwind_info: 0x8e60
-  __TEXT.__eh_frame: 0x156ac
+  __TEXT.__unwind_info: 0x8e58
+  __TEXT.__eh_frame: 0x15684
   __DATA_CONST.__const: 0x10d10
   __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_protolist: 0x1c0
Symbols:
+ _$s15AppIntentsIndex08MetadataC0V23appShortcutsUnprocessed3forSbSS_tKF
- _$s15AppIntentsIndex08MetadataC0V21appShortcutsProcessedySbSSKF
Functions:
~ sub_10000b038 : 12 -> 32
~ sub_1000104f4 -> sub_100010508 : 16 -> 12
~ sub_100010504 -> sub_100010514 : 12 -> 20
~ sub_100010510 -> sub_100010528 : 20 -> 12
~ sub_100012b4c -> sub_100012b5c : 24 -> 16
~ sub_100012b64 -> sub_100012b6c : 32 -> 24
~ sub_10001faec : 28 -> 12
~ sub_1001502a0 -> sub_100150290 : 872 -> 876
~ sub_100150828 -> sub_10015081c : 96 -> 92
~ sub_10015df6c -> sub_10015df5c : 12 -> 28
CStrings:
+ "AppShortcuts for %{public}s does not need processing, unblocking"
- "AppShortcuts for %{public}s appear processed, unblocking"
```
