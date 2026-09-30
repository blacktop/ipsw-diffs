## SoftwareUpdateServices

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-  __TEXT.__text: 0xc3ca8
+  __TEXT.__text: 0xc3dd8
   __TEXT.__auth_stubs: 0xe40
-  __TEXT.__objc_methlist: 0xb524
+  __TEXT.__objc_methlist: 0xb51c
   __TEXT.__const: 0x330
-  __TEXT.__cstring: 0x23afe
+  __TEXT.__cstring: 0x23b1d
   __TEXT.__gcc_except_tab: 0x12d4
   __TEXT.__oslogstring: 0x85d
-  __TEXT.__unwind_info: 0x36c0
+  __TEXT.__unwind_info: 0x36d0
   __TEXT.__objc_classname: 0xf76
   __TEXT.__objc_methname: 0x1a4f3
   __TEXT.__objc_methtype: 0x3502

   __DATA_CONST.__objc_arraydata: 0xa0
   __AUTH_CONST.__auth_got: 0x730
   __AUTH_CONST.__const: 0x7e0
-  __AUTH_CONST.__cfstring: 0x14e20
+  __AUTH_CONST.__cfstring: 0x14e40
   __AUTH_CONST.__objc_const: 0x163b8
   __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_dictobj: 0x78

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4703
-  Symbols:   10410
-  CStrings:  8091
+  Functions: 4704
+  Symbols:   10411
+  CStrings:  8092
 
Symbols:
+ +[SUUtility isDescriptorAutoUpdatable:]
+ +[SUUtility modelSpecificLocalizedStringKeyForKey:]
+ GCC_except_table84
+ ___56+[SUSpace makeRoomForUpdate:downloadOptions:completion:]_block_invoke_10
+ ___block_descriptor_80_e8_32s40s48s56bs64r_e17_v16?0"NSError"8ls56l8s32l8s40l8r64l8s48l8
+ ___block_descriptor_88_e8_32s40s48s56bs64r72r_e23_v28?0B8Q12"NSError"20lr64l8s56l8s32l8s40l8r72l8s48l8
- -[SUAppPurgingAlertItem modelSpecificLocalizedStringKeyForKey:]
- -[SUManagerCore isDescriptorAutoUpdatable:]
- GCC_except_table85
- ___block_descriptor_72_e8_32s40s48bs56r_e17_v16?0"NSError"8ls48l8s32l8s40l8r56l8
- ___block_descriptor_80_e8_32s40s48bs56r64r_e23_v28?0B8Q12"NSError"20lr56l8s48l8r64l8s32l8s40l8
Functions:
~ ___56+[SUSpace makeRoomForUpdate:downloadOptions:completion:]_block_invoke_3 : 588 -> 608
~ ___56+[SUSpace makeRoomForUpdate:downloadOptions:completion:]_block_invoke_6 : 828 -> 852
~ ___56+[SUSpace makeRoomForUpdate:downloadOptions:completion:]_block_invoke_7 : 344 -> 456
~ ___56+[SUSpace makeRoomForUpdate:downloadOptions:completion:]_block_invoke_8 : 292 -> 24
~ ___56+[SUSpace makeRoomForUpdate:downloadOptions:completion:]_block_invoke_9 : 36 -> 292
+ ___56+[SUSpace makeRoomForUpdate:downloadOptions:completion:]_block_invoke_10
~ -[SUAppPurgingAlertItem message] : 296 -> 300
- -[SUAppPurgingAlertItem modelSpecificLocalizedStringKeyForKey:]
~ +[SUSFollowUpAutoUpdate informativeTextWithDescriptor:] : 320 -> 512
~ -[SUScanner descriptorToAutoDownload:] : 560 -> 512
+ +[SUUtility modelSpecificLocalizedStringKeyForKey:]
+ +[SUUtility isDescriptorAutoUpdatable:]
~ -[SUManagerCore isAutoUpdateEnabled] : 112 -> 120
- -[SUManagerCore isDescriptorAutoUpdatable:]
~ -[SUDownloader tryAutoDownload] : 1792 -> 1772
CStrings:
+ "AUTO_SU_READY_TO_INSTALL_MAJOR"
```
