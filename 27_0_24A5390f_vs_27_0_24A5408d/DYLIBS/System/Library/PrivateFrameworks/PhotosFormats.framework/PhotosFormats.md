## PhotosFormats

> `/System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-910.33.102.0.0
-  __TEXT.__text: 0xd6824
+912.0.111.0.0
+  __TEXT.__text: 0xd6810
   __TEXT.__objc_methlist: 0xc8b8
   __TEXT.__const: 0x2db0
   __TEXT.__dlopen_cstrs: 0x1b7

   - /System/Library/PrivateFrameworks/CMPhoto.framework/CMPhoto
   - /System/Library/PrivateFrameworks/MMCS.framework/MMCS
   - /System/Library/PrivateFrameworks/PhotoFoundation.framework/PhotoFoundation
+  - /System/Library/PrivateFrameworks/Portrait.framework/Portrait
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libAppleArchive.dylib
   - /usr/lib/libMobileGestalt.dylib
Functions:
~ -[PFPosterDynamicDeviceConfiguration initWithCoder:] : 624 -> 660
~ +[PFParallaxLayoutConfiguration configurationForScreenSize:screenScale:determinedConfiguration:orientation:] : 640 -> 600
~ -[PFPosterOrientedLayout layoutByUpdatingImageSize:] : 1724 -> 1708
```
