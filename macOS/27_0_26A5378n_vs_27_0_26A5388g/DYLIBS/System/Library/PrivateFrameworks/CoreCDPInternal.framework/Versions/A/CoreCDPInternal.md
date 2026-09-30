## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/Versions/A/CoreCDPInternal`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
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
-  __TEXT.__text: 0x93a64
-  __TEXT.__objc_methlist: 0x5554
+445.0.0.0.0
+  __TEXT.__text: 0x93acc
+  __TEXT.__objc_methlist: 0x555c
   __TEXT.__const: 0x890
   __TEXT.__oslogstring: 0x145fa
   __TEXT.__cstring: 0xdae6

   __TEXT.__swift_as_ret: 0x58
   __TEXT.__swift_as_cont: 0x68
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1df8
+  __TEXT.__unwind_info: 0x1e00
   __TEXT.__eh_frame: 0x8f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3870
+  __DATA_CONST.__objc_selrefs: 0x3878
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_arraydata: 0x220

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3169
-  Symbols:   5869
+  Functions: 3170
+  Symbols:   5871
   CStrings:  2753
 
Symbols:
+ -[CDPDStateMachine _handleSecureBackupEnablementDidEnable:error:circleJoinResult:completion:]
+ GCC_except_table130
+ _objc_msgSend$_handleSecureBackupEnablementDidEnable:error:circleJoinResult:completion:
- GCC_except_table129
Functions:
~ ___65-[CDPDStateMachine _enableSecureBackupWithJoinResult:completion:]_block_invoke : 312 -> 336
~ __65-[CDPDStateMachine _enableSecureBackupWithJoinResult:completion:]_block_invoke.130 : 432 -> 24
+ -[CDPDStateMachine _handleSecureBackupEnablementDidEnable:error:circleJoinResult:completion:]
```
