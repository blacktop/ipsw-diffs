## MorphunAssets

> `/System/Library/PrivateFrameworks/MorphunAssets.framework/MorphunAssets`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA_DIRTY.__objc_data`

```diff

-3600.35.1.0.0
-  __TEXT.__text: 0x8a18
+3600.36.1.0.0
+  __TEXT.__text: 0x8b08
   __TEXT.__objc_methlist: 0x410
   __TEXT.__const: 0x68
   __TEXT.__cstring: 0xd2c
   __TEXT.__gcc_except_tab: 0x77c
   __TEXT.__oslogstring: 0x1035
-  __TEXT.__unwind_info: 0x2f8
+  __TEXT.__unwind_info: 0x2f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__const: 0x278
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4c0
+  __DATA_CONST.__objc_selrefs: 0x4c8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x198
   __DATA_CONST.__got: 0xf0

   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x20
-  __DATA.__data: 0x8
+  __DATA.__data: 0x10
+  __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x78
+  __DATA_DIRTY.__bss: 0x68
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libmorphun.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 145
-  Symbols:   447
+  Symbols:   448
   CStrings:  172
 
Symbols:
+ _objc_msgSend$copy
Functions:
~ -[MorphunAssets(MorphunAssetsSubscription) referenceCountsFromSubscriptionView] : 620 -> 672
~ -[MorphunAssets(MorphunAssetsSubscription) isSubscribedToLocale:] : 224 -> 284
~ -[MorphunAssets(MorphunAssetsSubscription) listSubscriptions] : 4 -> 132
```
