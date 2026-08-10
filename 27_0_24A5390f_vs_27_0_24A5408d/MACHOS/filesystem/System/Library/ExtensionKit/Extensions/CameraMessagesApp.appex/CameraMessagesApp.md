## CameraMessagesApp

> `/System/Library/ExtensionKit/Extensions/CameraMessagesApp.appex/CameraMessagesApp`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-4174.0.0.0.0
-  __TEXT.__text: 0x6500
-  __TEXT.__auth_stubs: 0x4b0
-  __TEXT.__objc_stubs: 0x1e00
-  __TEXT.__objc_methlist: 0x890
-  __TEXT.__objc_methname: 0x280a
+4177.22.3.0.0
+  __TEXT.__text: 0x6844
+  __TEXT.__auth_stubs: 0x4c0
+  __TEXT.__objc_stubs: 0x1ea0
+  __TEXT.__objc_methlist: 0x8a8
+  __TEXT.__objc_methname: 0x28d3
   __TEXT.__cstring: 0x2a0
   __TEXT.__objc_classname: 0x213
-  __TEXT.__objc_methtype: 0xb03
-  __TEXT.__const: 0xa8
-  __TEXT.__oslogstring: 0x82c
+  __TEXT.__objc_methtype: 0xb13
+  __TEXT.__const: 0xb0
+  __TEXT.__oslogstring: 0x986
   __TEXT.__gcc_except_tab: 0x44
   __TEXT.__unwind_info: 0x258
   __DATA_CONST.__const: 0x360

   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__auth_got: 0x268
-  __DATA_CONST.__got: 0x188
-  __DATA.__objc_const: 0xba8
-  __DATA.__objc_selrefs: 0x970
-  __DATA.__objc_ivar: 0x54
+  __DATA_CONST.__auth_got: 0x270
+  __DATA_CONST.__got: 0x190
+  __DATA.__objc_const: 0xbd8
+  __DATA.__objc_selrefs: 0x998
+  __DATA.__objc_ivar: 0x58
   __DATA.__objc_data: 0x230
   __DATA.__data: 0x360
   __DATA.__bss: 0x38

   - /System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 167
-  Symbols:   150
-  CStrings:  515
+  Functions: 170
+  Symbols:   152
+  CStrings:  528
 
Symbols:
+ _OBJC_CLASS_$_NSMutableSet
+ _objc_retain_x21
CStrings:
+ "@\"NSMutableSet\""
+ "Creating photo PHAsset with UUID %{public}@"
+ "Creating video PHAsset with UUID %{public}@"
+ "Handling review completion for asset UUID %{public}@ (action=%ld)"
+ "Ignoring repeat review completion for asset UUID %{public}@; already handled this capture."
+ "T@\"NSMutableSet\",&,N,S_setHandledCompletionAssetUUIDs:,V__handledCompletionAssetUUIDs"
+ "__handledCompletionAssetUUIDs"
+ "_handledCompletionAssetUUIDs"
+ "_setHandledCompletionAssetUUIDs:"
+ "addObject:"
+ "allKeys"
+ "didPerformCompletionAction: action=%ld selectedAssetUUIDs=%{public}@ substituteAssetUUIDs=%{public}@"
+ "set"
```
