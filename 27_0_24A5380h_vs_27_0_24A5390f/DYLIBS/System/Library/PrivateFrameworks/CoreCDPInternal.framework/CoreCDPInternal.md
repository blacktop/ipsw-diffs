## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
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
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-444.0.0.0.0
-  __TEXT.__text: 0x8db84
-  __TEXT.__objc_methlist: 0x567c
+445.0.0.0.0
+  __TEXT.__text: 0x8dbdc
+  __TEXT.__objc_methlist: 0x568c
   __TEXT.__const: 0x888
   __TEXT.__oslogstring: 0x14a5e
   __TEXT.__cstring: 0xe055

   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x58
   __TEXT.__swift_as_cont: 0x68
-  __TEXT.__unwind_info: 0x1df0
+  __TEXT.__unwind_info: 0x1df8
   __TEXT.__eh_frame: 0x8f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3900
+  __DATA_CONST.__objc_selrefs: 0x3908
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x220

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3157
-  Symbols:   5789
+  Functions: 3158
+  Symbols:   5791
   CStrings:  2806
 
Symbols:
+ -[CDPDStateMachine _handleSecureBackupEnablementDidEnable:error:circleJoinResult:completion:]
+ GCC_except_table121
+ ___block_descriptor_56_e8_32s40s48bs_e8_v12?0B8ls32l8s48l8s40l8
+ _objc_msgSend$_handleSecureBackupEnablementDidEnable:error:circleJoinResult:completion:
- GCC_except_table120
- ___block_descriptor_56_e8_32s40s48bs_e8_v12?0B8ls48l8s32l8s40l8
Functions:
~ -[CDPDStateMachine _enableSecureBackupWithJoinResult:completion:] : 412 -> 416
~ ___65-[CDPDStateMachine _enableSecureBackupWithJoinResult:completion:]_block_invoke : 304 -> 324
~ ___65-[CDPDStateMachine _enableSecureBackupWithJoinResult:completion:]_block_invoke.111 : 408 -> 24
+ -[CDPDStateMachine _handleSecureBackupEnablementDidEnable:error:circleJoinResult:completion:]
```
