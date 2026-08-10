## NanoResourceGrabber

> `/System/Library/PrivateFrameworks/NanoResourceGrabber.framework/NanoResourceGrabber`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__objc_const`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-117.0.0.0.0
-  __TEXT.__text: 0x3c48
+118.0.0.0.0
+  __TEXT.__text: 0x3de8
   __TEXT.__objc_methlist: 0x374
-  __TEXT.__const: 0x48
-  __TEXT.__oslogstring: 0x79d
-  __TEXT.__cstring: 0x3fe
+  __TEXT.__const: 0x60
+  __TEXT.__oslogstring: 0x8b7
+  __TEXT.__cstring: 0x40a
   __TEXT.__gcc_except_tab: 0x68
-  __TEXT.__unwind_info: 0x198
+  __TEXT.__unwind_info: 0x1a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b8
+  __DATA_CONST.__objc_selrefs: 0x3a8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0xd8
-  __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x340
+  __AUTH_CONST.__const: 0x100
+  __AUTH_CONST.__cfstring: 0x380
   __AUTH_CONST.__objc_const: 0x3d0
-  __AUTH_CONST.__objc_intobj: 0x348
+  __AUTH_CONST.__objc_intobj: 0x390
+  __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x10
   __DATA.__data: 0xc0
-  __DATA.__bss: 0x10
+  __DATA.__bss: 0x30
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 105
+  Functions: 109
   Symbols:   318
-  CStrings:  75
+  CStrings:  81
 
Symbols:
+ +[NanoResourceGrabber liIconVariantsSyncedToPhone]
+ +[NanoResourceGrabber liIconVariantsSyncedToWatch]
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSSet
+ ___50+[NanoResourceGrabber liIconVariantsSyncedToPhone]_block_invoke
+ ___50+[NanoResourceGrabber liIconVariantsSyncedToWatch]_block_invoke
+ ___block_descriptor_68_e8_32s40s48bs56w_e20_v20?0"UIImage"8B16ls32l8s48l8s40l8w56l8
+ _liIconVariantsSyncedToPhone.onceToken
+ _liIconVariantsSyncedToPhone.variants
+ _liIconVariantsSyncedToWatch.onceToken
+ _liIconVariantsSyncedToWatch.variants
+ _objc_msgSend$setWithArray:
- +[NanoResourceGrabber liIconVariants]
- +[NanoResourceGrabber nrgIconVariants]
- _OBJC_CLASS_$_NSMutableArray
- ___99-[NanoResourceGrabber getCachedIconForBundleID:iconVariant:outIconImage:queue:updateBlock:timeout:]_block_invoke_2
- ___99-[NanoResourceGrabber getCachedIconForBundleID:iconVariant:outIconImage:queue:updateBlock:timeout:]_block_invoke_3
- ___block_descriptor_68_e8_32s40s48bs56w_e20_v20?0"UIImage"8B16ls48l8s32l8w56l8s40l8
- _objc_enumerationMutation
- _objc_msgSend$addObject:
- _objc_msgSend$copy
- _objc_msgSend$countByEnumeratingWithState:objects:count:
- _objc_msgSend$liIconVariants
- _objc_release_x25
CStrings:
+ "getCachedIconForBundleID: caching icon for %{public}@ variant %ld"
+ "getCachedIconForBundleID: delivering icon for %{public}@ variant %ld (image %@, cache %d)"
+ "invalidatePairedDevice: clearing cache for pairedDeviceStorePath=%@"
+ "nil"
+ "present"
+ "setIcon: cached icon for %@ variant %ld (%lu bytes) at %@"
```
