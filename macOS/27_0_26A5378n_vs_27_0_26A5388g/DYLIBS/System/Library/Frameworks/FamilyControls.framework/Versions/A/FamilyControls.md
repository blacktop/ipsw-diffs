## FamilyControls

> `/System/Library/Frameworks/FamilyControls.framework/Versions/A/FamilyControls`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift_as_ret`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__AUTH.__data`

```diff

-1244.0.0.0.0
+1245.0.0.0.0
   __TEXT.__text: 0x25dd0
   __TEXT.__objc_methlist: 0x2fc
   __TEXT.__const: 0x1db4

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1b8
+  __DATA_CONST.__const: 0x1c0
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8

   __AUTH_CONST.__auth_got: 0x848
   __AUTH.__objc_data: 0xa0
   __AUTH.__data: 0x7c0
-  __DATA.__data: 0x728
+  __DATA.__data: 0x708
   __DATA.__bss: 0x2790
   __DATA.__common: 0x10
-  __DATA_DIRTY.__data: 0x400
+  __DATA_DIRTY.__data: 0x410
   __DATA_DIRTY.__bss: 0x280
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 1309
-  Symbols:   545
+  Symbols:   547
   CStrings:  89
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_FamilyControls
```
