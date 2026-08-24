## JournalDataclassOwner

> `/System/Library/Accounts/DataclassOwners/JournalDataclassOwner.bundle/Contents/MacOS/JournalDataclassOwner`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_protos`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-94.0.0.0.0
-  __TEXT.__text: 0xbe78
+99.1.2.0.0
+  __TEXT.__text: 0xbf6c
   __TEXT.__auth_stubs: 0x890
   __TEXT.__objc_stubs: 0x520
   __TEXT.__objc_methlist: 0x23c
-  __TEXT.__const: 0x7b8
+  __TEXT.__const: 0x7a8
   __TEXT.__constg_swiftt: 0x208
-  __TEXT.__swift5_typeref: 0x25f
+  __TEXT.__swift5_typeref: 0x259
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_reflstr: 0x135
   __TEXT.__swift5_fieldmd: 0x154

   __TEXT.__objc_classname: 0xe1
   __TEXT.__objc_methname: 0x733
   __TEXT.__objc_methtype: 0x263
-  __TEXT.__oslogstring: 0xbbd
+  __TEXT.__oslogstring: 0xcfd
   __TEXT.__cstring: 0x1c3
   __TEXT.__swift5_capture: 0x58
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x278
+  __TEXT.__unwind_info: 0x280
   __TEXT.__eh_frame: 0x218
-  __DATA_CONST.__const: 0x408
+  __DATA_CONST.__const: 0x430
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_const: 0x350
   __DATA.__objc_selrefs: 0x250
   __DATA.__objc_data: 0x230
-  __DATA.__data: 0x498
+  __DATA.__data: 0x490
   __DATA.__common: 0x48
   __DATA.__bss: 0xb80
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 190
   Symbols:   112
-  CStrings:  169
+  CStrings:  171
 
Functions:
~ sub_37b4 : 2348 -> 2676
~ sub_47ac -> sub_48f4 : 4684 -> 4672
~ sub_5a38 -> sub_5b74 : 76 -> 68
~ sub_5a84 -> sub_5bb8 : 16 -> 76
~ sub_5a94 -> sub_5c04 : 4 -> 16
~ sub_5a98 -> sub_5c14 : 68 -> 4
~ sub_7194 -> sub_72d0 : 1592 -> 1620
~ sub_7f00 -> sub_8058 : 2152 -> 2052
~ sub_97d0 -> sub_98c4 : 84 -> 76
~ sub_9824 -> sub_9910 : 76 -> 312
~ sub_9870 -> sub_9a48 : 312 -> 244
~ sub_99a8 -> sub_9b3c : 244 -> 116
~ sub_9a9c -> sub_9bb0 : 116 -> 244
~ sub_9b10 -> sub_9ca4 : 244 -> 84
CStrings:
+ "%{public}s called, but calling through to DataclassOwner.actionsForDisablingDataclass(on:forDataclass:)"
+ "%{public}s called, but calling through to DataclassOwner.actionsForEnablingDataclass(on:forDataclass:)"
+ "Error trying to mark all records as not uploaded; will attempt to flag for re-uploading on next app launch. Error: %@"
+ "Error trying to persist old account identifier: %@"
+ "Failed to delete all local data; will attempt to delete all local data on next app launch. Error: %@"
+ "Ignoring supported action %{public}@"
+ "Ignoring unsupported action .refresh, previously treated as delete"
+ "New account id differs from the one used when disabling dataclass. Resetting local sync state to fetch all Journal CloudKit data for the new account, while also forcing an upload of all local Journal data. New id: %{private,mask.hash}s, old id: %{private,mask.hash}s."
+ "No %{public}s records found"
+ "Performing DataClass action %{public}@ for account %{private,mask.hash}@"
- "%s called, but calling through to DataclassOwner.actionsForDisablingDataclass(on:forDataclass:)"
- "%s called, but calling through to DataclassOwner.actionsForEnablingDataclass(on:forDataclass:)"
- "Error trying to mark all records as not uploaded: %@"
- "Failed to delete all local data: %@"
- "Ignoring supported action %@"
- "Ignoring unsupported action %@, (though previously treated as delete)"
- "New account id differs from the one used when disabling dataclass. Resetting local sync state to fetch all Journal CloudKit data for the new account, while also forcing an upload of all local Journal data. New id: %s, old id: %s."
- "Performing DataClass action %{public}@ for account %@"
```
