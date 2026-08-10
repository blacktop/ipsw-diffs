## DataDeliveryServices

> `/System/Library/PrivateFrameworks/DataDeliveryServices.framework/DataDeliveryServices`

### Sections with Same Size but Changed Content

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
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-114.0.0.0.0
-  __TEXT.__text: 0x29fb8
-  __TEXT.__objc_methlist: 0x2a64
+115.0.0.0.0
+  __TEXT.__text: 0x2a060
+  __TEXT.__objc_methlist: 0x2a7c
   __TEXT.__const: 0x180
   __TEXT.__gcc_except_tab: 0x61c
   __TEXT.__cstring: 0x16c2
-  __TEXT.__oslogstring: 0x3dbf
-  __TEXT.__unwind_info: 0xc90
+  __TEXT.__oslogstring: 0x3dfd
+  __TEXT.__unwind_info: 0xc98
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1610
+  __DATA_CONST.__objc_selrefs: 0x1618
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x118
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__got: 0x338
   __AUTH_CONST.__const: 0x360
   __AUTH_CONST.__cfstring: 0x1980
-  __AUTH_CONST.__objc_const: 0x8e10
+  __AUTH_CONST.__objc_const: 0x8e18
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1042
-  Symbols:   2570
-  CStrings:  561
+  Functions: 1043
+  Symbols:   2572
+  CStrings:  562
 
Symbols:
+ -[DDSAssetObserver notifyDelegateAssetsUpdatedForType:]
+ _objc_msgSend$notifyDelegateAssetsUpdatedForType:
Functions:
+ -[DDSAssetObserver notifyDelegateAssetsUpdatedForType:]
CStrings:
+ "Notifying local delegate of asset update for type: %{public}@"
```
