## ReplayKitModule

> `/System/Library/ControlCenter/Bundles/ReplayKitModule.bundle/ReplayKitModule`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-740.57.1.0.0
-  __TEXT.__text: 0xbb48
-  __TEXT.__auth_stubs: 0x540
-  __TEXT.__objc_stubs: 0x1fc0
-  __TEXT.__objc_methlist: 0xdb0
-  __TEXT.__const: 0xb8
-  __TEXT.__cstring: 0x1f96
-  __TEXT.__objc_methname: 0x2fa9
-  __TEXT.__oslogstring: 0x1011
+740.63.1.1.0
+  __TEXT.__text: 0xbf6c
+  __TEXT.__auth_stubs: 0x530
+  __TEXT.__objc_stubs: 0x20e0
+  __TEXT.__objc_methlist: 0xde0
+  __TEXT.__const: 0xc0
+  __TEXT.__cstring: 0x1fcf
+  __TEXT.__objc_methname: 0x307a
+  __TEXT.__oslogstring: 0x1049
   __TEXT.__objc_classname: 0x178
-  __TEXT.__objc_methtype: 0x965
+  __TEXT.__objc_methtype: 0x967
   __TEXT.__gcc_except_tab: 0x19c
-  __TEXT.__unwind_info: 0x350
+  __TEXT.__unwind_info: 0x360
   __DATA_CONST.__const: 0x4a0
   __DATA_CONST.__cfstring: 0x660
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x30
-  __DATA_CONST.__auth_got: 0x2b0
-  __DATA_CONST.__got: 0x168
-  __DATA.__objc_const: 0x1ed8
-  __DATA.__objc_selrefs: 0xc60
-  __DATA.__objc_ivar: 0xd0
+  __DATA_CONST.__auth_got: 0x2a8
+  __DATA_CONST.__got: 0x170
+  __DATA.__objc_const: 0x1ef8
+  __DATA.__objc_selrefs: 0xca8
+  __DATA.__objc_ivar: 0xd4
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x2a0
   __DATA.__bss: 0x20

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 240
-  Symbols:   154
-  CStrings:  816
+  Functions: 244
+  Symbols:   153
+  CStrings:  829
 
Symbols:
+ _CGRectIsEmpty
+ _objc_opt_isKindOfClass
- _CCUIIsPortrait
- _CCUIReferenceScreenBounds
- _CCUIScreenBounds
CStrings:
+ " [INFO] %{public}s:%d %p module no longer visible, tearing down stale ScreenCaptureKit picker"
+ " [INFO] %{public}s:%d %p userVisibilityStatus %ld -> %ld isSCKPicker=%i"
+ " [INFO] %{public}s:%d Dismissing ScreenCaptureKit picker"
+ " [INFO] %{public}s:%d End ScreenCaptureKit picker"
+ "-[RPControlCenterMenuModuleViewController dismissScreenCaptureKitPicker]"
+ "-[RPControlCenterMenuModuleViewController setUserVisibilityStatus:]"
+ "_geometryProvider"
+ "_referenceBounds"
+ "_userVisibilityStatus"
+ "_usesVerticallyStackedLayout"
+ "controlCenterOrientation"
+ "dismissScreenCaptureKitPicker"
+ "geometryProvider"
+ "maximumExpandedContentModuleHeight"
+ "pickerDidDismiss:forStreamInfo:isCancelled:"
+ "q"
+ "screen"
+ "supportsEdgeAlignedLayout"
+ "viewIfLoaded"
+ "windowScene"
- " [INFO] %{public}s:%d Cancel ScreenCaptureKit picker, will call dismissModule"
- " [INFO] %{public}s:%d End ScreenCaptureKit picker, will call dismissModule"
- " [INFO] %{public}s:%d ScreenCaptureKit picker cancelled by user"
- "-[RPControlCenterMenuModuleViewController cancelScreenCaptureKitPickerWithDismiss:]"
- "cancelScreenCaptureKitPickerWithDismiss:"
- "dismissModule"
- "pickerDidCancel:forStreamInfo:"
```
