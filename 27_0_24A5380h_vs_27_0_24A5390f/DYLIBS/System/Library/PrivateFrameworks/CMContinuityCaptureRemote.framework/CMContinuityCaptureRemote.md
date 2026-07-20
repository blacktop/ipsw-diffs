## CMContinuityCaptureRemote

> `/System/Library/PrivateFrameworks/CMContinuityCaptureRemote.framework/CMContinuityCaptureRemote`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_acfuncs`
- `__TEXT.__swift5_builtin`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-758.0.0.122.2
-  __TEXT.__text: 0xafa64
-  __TEXT.__objc_methlist: 0x5fa4
+761.0.0.0.3
+  __TEXT.__text: 0xaf9ec
+  __TEXT.__objc_methlist: 0x5fb4
   __TEXT.__const: 0x13d0
   __TEXT.__cstring: 0xa9c5
   __TEXT.__oslogstring: 0xb8cd
-  __TEXT.__gcc_except_tab: 0x33ec
+  __TEXT.__gcc_except_tab: 0x33b8
   __TEXT.__dlopen_cstrs: 0x54
   __TEXT.__swift5_typeref: 0x905
   __TEXT.__swift5_capture: 0x69c

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1f28
+  __DATA_CONST.__const: 0x1f30
   __DATA_CONST.__objc_classlist: 0x228
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x1a8

   __DATA_CONST.__got: 0xb98
   __AUTH_CONST.__const: 0x15b8
   __AUTH_CONST.__cfstring: 0x3d20
-  __AUTH_CONST.__objc_const: 0xac50
+  __AUTH_CONST.__objc_const: 0xac90
   __AUTH_CONST.__objc_intobj: 0x528
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_dictobj: 0x50

   __AUTH_CONST.__auth_got: 0x1058
   __AUTH.__objc_data: 0x1c00
   __AUTH.__data: 0x2c8
-  __DATA.__objc_ivar: 0x834
+  __DATA.__objc_ivar: 0x83c
   __DATA.__data: 0x15b0
   __DATA.__bss: 0xc60
   __DATA.__common: 0xf0

   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 3185
-  Symbols:   5806
+  Symbols:   5809
   CStrings:  1877
 
Symbols:
+ -[CMContinuityCaptureDServer _releaseShieldUIResources]
+ -[CMContinuityCaptureRemoteServer _releaseShieldUIResources]
+ GCC_except_table65
+ GCC_except_table99
+ _OBJC_IVAR_$_CMContinuityCaptureDServer._shieldUIObserversRegistered
+ _OBJC_IVAR_$_CMContinuityCaptureRemoteServer._shieldUIObserversRegistered
+ ___55-[CMContinuityCaptureDServer _releaseShieldUIResources]_block_invoke
+ ___60-[CMContinuityCaptureRemoteServer _releaseShieldUIResources]_block_invoke
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private_$_CMContinuityCaptureRemote
+ _objc_msgSend$_releaseShieldUIResources
- -[CMContinuityCaptureDServer teardownShieldUI]
- GCC_except_table100
- GCC_except_table89
- GCC_except_table93
- ___46-[CMContinuityCaptureDServer teardownShieldUI]_block_invoke
- ___47-[CMContinuityCaptureDServer _teardownShieldUI]_block_invoke
- ___52-[CMContinuityCaptureRemoteServer _teardownShieldUI]_block_invoke
- _objc_msgSend$teardownShieldUI
```
