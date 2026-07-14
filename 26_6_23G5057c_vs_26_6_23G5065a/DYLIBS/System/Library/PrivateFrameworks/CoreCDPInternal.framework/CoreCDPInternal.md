## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-  __TEXT.__text: 0x96be0
+  __TEXT.__text: 0x96c30
   __TEXT.__auth_stubs: 0x1160
-  __TEXT.__objc_methlist: 0x567c
+  __TEXT.__objc_methlist: 0x568c
   __TEXT.__const: 0x850
   __TEXT.__oslogstring: 0x14a5e
   __TEXT.__cstring: 0xdda5

   __TEXT.__swift5_capture: 0x200
   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x58
-  __TEXT.__unwind_info: 0x1f98
+  __TEXT.__unwind_info: 0x1fa0
   __TEXT.__eh_frame: 0x958
   __TEXT.__objc_classname: 0xdbd
-  __TEXT.__objc_methname: 0xfb5f
+  __TEXT.__objc_methname: 0xfbaf
   __TEXT.__objc_methtype: 0x2aa7
-  __TEXT.__objc_stubs: 0xcd80
+  __TEXT.__objc_stubs: 0xcda0
   __DATA_CONST.__got: 0x10b8
   __DATA_CONST.__const: 0x25c0
   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3900
+  __DATA_CONST.__objc_selrefs: 0x3908
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x208

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3165
-  Symbols:   5767
-  CStrings:  5395
+  Functions: 3166
+  Symbols:   5769
+  CStrings:  5396
 
Symbols:
+ -[CDPDStateMachine _handleSecureBackupEnablementDidEnable:error:circleJoinResult:completion:]
+ GCC_except_table121
+ ___block_descriptor_56_e8_32s40s48bs_e8_v12?0B8ls32l8s48l8s40l8
+ _objc_msgSend$_handleSecureBackupEnablementDidEnable:error:circleJoinResult:completion:
- GCC_except_table120
- ___block_descriptor_56_e8_32s40s48bs_e8_v12?0B8ls48l8s32l8s40l8
Functions:
~ -[CDPDStateMachine _enableSecureBackupWithJoinResult:completion:] : 420 -> 424
~ ___65-[CDPDStateMachine _enableSecureBackupWithJoinResult:completion:]_block_invoke : 308 -> 328
~ ___65-[CDPDStateMachine _enableSecureBackupWithJoinResult:completion:]_block_invoke.111 : 464 -> 24
+ -[CDPDStateMachine _handleSecureBackupEnablementDidEnable:error:circleJoinResult:completion:]
CStrings:
+ "_handleSecureBackupEnablementDidEnable:error:circleJoinResult:completion:"
```
