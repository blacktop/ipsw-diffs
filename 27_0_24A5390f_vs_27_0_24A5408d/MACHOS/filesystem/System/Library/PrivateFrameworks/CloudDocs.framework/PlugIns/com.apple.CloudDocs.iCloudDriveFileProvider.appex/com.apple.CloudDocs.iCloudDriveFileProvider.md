## com.apple.CloudDocs.iCloudDriveFileProvider

> `/System/Library/PrivateFrameworks/CloudDocs.framework/PlugIns/com.apple.CloudDocs.iCloudDriveFileProvider.appex/com.apple.CloudDocs.iCloudDriveFileProvider`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-5168.0.5.0.2
-  __TEXT.__text: 0x23e98
-  __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_stubs: 0x2c80
+5168.0.55.0.0
+  __TEXT.__text: 0x23ebc
+  __TEXT.__auth_stubs: 0x640
+  __TEXT.__objc_stubs: 0x2c60
   __TEXT.__objc_methlist: 0x1e1c
-  __TEXT.__const: 0xb0
+  __TEXT.__const: 0xb8
   __TEXT.__gcc_except_tab: 0x23b8
-  __TEXT.__objc_methname: 0x5385
+  __TEXT.__objc_methname: 0x5366
   __TEXT.__cstring: 0x44f8
   __TEXT.__oslogstring: 0x247e
   __TEXT.__objc_classname: 0x6d5

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xc0
-  __DATA_CONST.__auth_got: 0x318
+  __DATA_CONST.__auth_got: 0x330
   __DATA_CONST.__got: 0x270
   __DATA.__objc_const: 0x7d70
-  __DATA.__objc_selrefs: 0x1280
+  __DATA.__objc_selrefs: 0x1278
   __DATA.__objc_ivar: 0x138
   __DATA.__objc_data: 0x8c0
   __DATA.__data: 0xae0

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   Functions: 609
-  Symbols:   186
-  CStrings:  1439
+  Symbols:   189
+  CStrings:  1438
 
Symbols:
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _voucher_process_can_use_arbitrary_personas
Functions:
~ sub_100008f9c : 1096 -> 1088
~ sub_100009444 -> sub_10000943c : 1084 -> 1076
~ sub_1000136c8 -> sub_1000136b8 : 1252 -> 1312
~ sub_100013bc4 -> sub_100013bf0 : 248 -> 280
~ sub_10001819c -> sub_1000181e8 : 960 -> 952
~ sub_1000185bc -> sub_100018600 : 972 -> 964
~ sub_1000192b0 -> sub_1000192ec : 960 -> 952
~ sub_1000196d0 -> sub_100019704 : 972 -> 964
~ sub_100020038 -> sub_100020064 : 968 -> 960
CStrings:
- "processCanUseArbitraryPersonas"
```
