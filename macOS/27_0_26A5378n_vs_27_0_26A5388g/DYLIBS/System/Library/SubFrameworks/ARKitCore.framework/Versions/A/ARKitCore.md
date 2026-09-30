## ARKitCore

> `/System/Library/SubFrameworks/ARKitCore.framework/Versions/A/ARKitCore`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_classrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__DATA_DIRTY.__objc_data`

```diff

-781.0.2.0.1
-  __TEXT.__text: 0x4f650
-  __TEXT.__objc_methlist: 0x2bb4
+781.0.4.0.0
+  __TEXT.__text: 0x500e4
+  __TEXT.__objc_methlist: 0x2c9c
   __TEXT.__const: 0x3650
-  __TEXT.__cstring: 0xbd3f
-  __TEXT.__gcc_except_tab: 0x1bf0
-  __TEXT.__oslogstring: 0x5f86
+  __TEXT.__cstring: 0xbd71
+  __TEXT.__gcc_except_tab: 0x1c0c
+  __TEXT.__oslogstring: 0x5fc1
   __TEXT.__ustring: 0xde
-  __TEXT.__unwind_info: 0x19f8
+  __TEXT.__unwind_info: 0x1a38
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x10d0
-  __DATA_CONST.__objc_classlist: 0x1f8
+  __DATA_CONST.__objc_classlist: 0x210
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x1798
+  __DATA_CONST.__objc_selrefs: 0x1820
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_classrefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x1c8
+  __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x448
-  __DATA_CONST.__got: 0x4d8
-  __AUTH_CONST.__const: 0x1af0
-  __AUTH_CONST.__cfstring: 0x5c80
-  __AUTH_CONST.__objc_const: 0x6fa0
+  __DATA_CONST.__got: 0x508
+  __AUTH_CONST.__const: 0x1b70
+  __AUTH_CONST.__cfstring: 0x5ca0
+  __AUTH_CONST.__objc_const: 0x72c8
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x1b0
   __AUTH_CONST.__objc_intobj: 0x1818
   __AUTH_CONST.__objc_doubleobj: 0xd0
   __AUTH_CONST.__auth_got: 0xb58
-  __AUTH.__objc_data: 0xd20
-  __DATA.__objc_ivar: 0x280
-  __DATA.__data: 0xac0
+  __AUTH.__objc_data: 0xe10
+  __DATA.__objc_ivar: 0x2a4
+  __DATA.__data: 0xac8
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x658
   __DATA_DIRTY.__objc_data: 0x690
-  __DATA_DIRTY.__bss: 0x328
+  __DATA_DIRTY.__bss: 0x338
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vImage.framework/Versions/A/vImage
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libchannel.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/librealtime_safety.dylib
-  Functions: 2324
-  Symbols:   4559
-  CStrings:  1455
+  Functions: 2346
+  Symbols:   4628
+  CStrings:  1458
 
Symbols:
+ +[ARViewRotationContext replayContext]
+ -[ARRotationCoordinatorPreviewAngleSource .cxx_destruct]
+ -[ARRotationCoordinatorPreviewAngleSource dealloc]
+ -[ARRotationCoordinatorPreviewAngleSource initWithLayer:device:previewAngleChangeHandler:]
+ -[ARRotationCoordinatorPreviewAngleSource observeValueForKeyPath:ofObject:change:context:]
+ -[ARViewRotationAngleProvider .cxx_destruct]
+ -[ARViewRotationAngleProvider _deliverPreviewAngle:]
+ -[ARViewRotationAngleProvider _updatePreviewAngleSource]
+ -[ARViewRotationAngleProvider initWithLayer:handler:context:]
+ -[ARViewRotationAngleProvider updateContext:]
+ -[ARViewRotationAngleProvider weakLayer]
+ -[ARViewRotationContext .cxx_destruct]
+ -[ARViewRotationContext defaultVideoRotationAngle]
+ -[ARViewRotationContext device]
+ -[ARViewRotationContext initWithDevice:defaultVideoRotationAngle:]
+ -[ARViewRotationContext isEqual:]
+ OBJC_IVAR_$_ARRotationCoordinatorPreviewAngleSource._coordinator
+ OBJC_IVAR_$_ARRotationCoordinatorPreviewAngleSource._previewAngleChangeHandler
+ OBJC_IVAR_$_ARViewRotationAngleProvider._context
+ OBJC_IVAR_$_ARViewRotationAngleProvider._handler
+ OBJC_IVAR_$_ARViewRotationAngleProvider._lastRotationAngle
+ OBJC_IVAR_$_ARViewRotationAngleProvider._previewAngleSource
+ OBJC_IVAR_$_ARViewRotationAngleProvider._weakLayer
+ OBJC_IVAR_$_ARViewRotationContext._defaultVideoRotationAngle
+ OBJC_IVAR_$_ARViewRotationContext._device
+ _ARRotationCoordinatorPreviewAngleSourceKVOContext
+ _ARViewRotationAngleFromFrontPreviewAngle
+ _ARViewRotationAngleFromRearPreviewAngle
+ _AVMediaTypeVideo
+ _OBJC_CLASS_$_ARRotationCoordinatorPreviewAngleSource
+ _OBJC_CLASS_$_ARViewRotationAngleProvider
+ _OBJC_CLASS_$_ARViewRotationContext
+ _OBJC_CLASS_$_AVCaptureDevice
+ _OBJC_CLASS_$_AVCaptureDeviceRotationCoordinator
+ _OBJC_CLASS_$_NSThread
+ _OBJC_METACLASS_$_ARRotationCoordinatorPreviewAngleSource
+ _OBJC_METACLASS_$_ARViewRotationAngleProvider
+ _OBJC_METACLASS_$_ARViewRotationContext
+ __OBJC_$_CLASS_METHODS_ARViewRotationContext
+ __OBJC_$_INSTANCE_METHODS_ARRotationCoordinatorPreviewAngleSource
+ __OBJC_$_INSTANCE_METHODS_ARViewRotationAngleProvider
+ __OBJC_$_INSTANCE_METHODS_ARViewRotationContext
+ __OBJC_$_INSTANCE_VARIABLES_ARRotationCoordinatorPreviewAngleSource
+ __OBJC_$_INSTANCE_VARIABLES_ARViewRotationAngleProvider
+ __OBJC_$_INSTANCE_VARIABLES_ARViewRotationContext
+ __OBJC_$_PROP_LIST_ARViewRotationAngleProvider
+ __OBJC_$_PROP_LIST_ARViewRotationContext
+ __OBJC_CLASS_RO_$_ARRotationCoordinatorPreviewAngleSource
+ __OBJC_CLASS_RO_$_ARViewRotationAngleProvider
+ __OBJC_CLASS_RO_$_ARViewRotationContext
+ __OBJC_METACLASS_RO_$_ARRotationCoordinatorPreviewAngleSource
+ __OBJC_METACLASS_RO_$_ARViewRotationAngleProvider
+ __OBJC_METACLASS_RO_$_ARViewRotationContext
+ ___52-[ARViewRotationAngleProvider _deliverPreviewAngle:]_block_invoke
+ ___56-[ARViewRotationAngleProvider _updatePreviewAngleSource]_block_invoke
+ ___block_descriptor_40_e8_32w_e8_v16?0d8l
+ ___block_descriptor_48_e8_32bs_e5_v8?0l
+ _objc_msgSend$_deliverPreviewAngle:
+ _objc_msgSend$_updatePreviewAngleSource
+ _objc_msgSend$addObserver:forKeyPath:options:context:
+ _objc_msgSend$defaultDeviceWithDeviceType:mediaType:position:
+ _objc_msgSend$defaultVideoRotationAngle
+ _objc_msgSend$initWithDevice:defaultVideoRotationAngle:
+ _objc_msgSend$initWithDevice:previewLayer:
+ _objc_msgSend$initWithLayer:device:previewAngleChangeHandler:
+ _objc_msgSend$isMainThread
+ _objc_msgSend$position
+ _objc_msgSend$removeObserver:forKeyPath:context:
+ _objc_msgSend$videoRotationAngleForHorizonLevelPreview
CStrings:
+ "%{public}@ <%p>: Delivering view rotation angle %f degrees"
+ "v16@?0d8"
+ "videoRotationAngleForHorizonLevelPreview"
```
