## HeadphoneConfigs

> `/System/Library/PrivateFrameworks/HeadphoneConfigs.framework/HeadphoneConfigs`

```diff

 2700.17.1.1.0
-  __TEXT.__text: 0xc9614
-  __TEXT.__objc_methlist: 0x4fa8
-  __TEXT.__const: 0x2414
-  __TEXT.__cstring: 0x9643
-  __TEXT.__oslogstring: 0xa3db
+  __TEXT.__text: 0xca3e4
+  __TEXT.__objc_methlist: 0x4fd8
+  __TEXT.__const: 0x2434
+  __TEXT.__cstring: 0x9723
+  __TEXT.__oslogstring: 0xa59b
   __TEXT.__gcc_except_tab: 0x7ec
   __TEXT.__dlopen_cstrs: 0x68
   __TEXT.__constg_swiftt: 0x12b0

   __TEXT.__swift5_proto: 0xe4
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x2428
+  __TEXT.__unwind_info: 0x2458
   __TEXT.__eh_frame: 0x3e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x11b0
+  __DATA_CONST.__const: 0x1200
   __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3680
+  __DATA_CONST.__objc_selrefs: 0x36c0
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x1d0
   __DATA_CONST.__got: 0xba0
-  __AUTH_CONST.__const: 0x22a0
-  __AUTH_CONST.__cfstring: 0x95e0
+  __AUTH_CONST.__const: 0x22e0
+  __AUTH_CONST.__cfstring: 0x96c0
   __AUTH_CONST.__objc_const: 0xa7a8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0xfa0
+  __AUTH_CONST.__auth_got: 0xfa8
   __AUTH.__objc_data: 0x26e8
   __AUTH.__data: 0x550
   __DATA.__objc_ivar: 0x78c

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4195
-  Symbols:   4900
-  CStrings:  2248
+  Functions: 4204
+  Symbols:   4919
+  CStrings:  2264
 
Symbols:
+ +[HPSProductUtils isShortScreenDevice]
+ +[HPSProductUtils stringForUIInterfaceOrientation:]
+ -[HPSSpatialProfileSingeStepEnrollmentController showNonLandscapeLeftAlert]
+ -[HPSSpatialProfileSingeStepEnrollmentController viewWillTransitionToSize:withTransitionCoordinator:]
+ _MGGetProductType
+ _MGIsDeviceOfType
+ ___101-[HPSSpatialProfileSingeStepEnrollmentController viewWillTransitionToSize:withTransitionCoordinator:]_block_invoke
+ ___38+[HPSProductUtils isShortScreenDevice]_block_invoke
+ ___75-[HPSSpatialProfileSingeStepEnrollmentController showNonLandscapeLeftAlert]_block_invoke
+ ___76-[HPSSpatialProfileManagementController presentProfileEnrollmentController:]_block_invoke
+ ___block_descriptor_40_e8_32s_e56_v16?0"<UIViewControllerTransitionCoordinatorContext>"8ls32l8
+ _isShortScreenDevice.onceToken
+ _isShortScreenDevice.sIsShortScreenDevice
+ _objc_msgSend$animateAlongsideTransition:completion:
+ _objc_msgSend$effectiveGeometry
+ _objc_msgSend$interfaceOrientation
+ _objc_msgSend$isShortScreenDevice
+ _objc_msgSend$showNonLandscapeLeftAlert
+ _objc_msgSend$stringForUIInterfaceOrientation:
+ _objc_msgSend$windowScene
- _swift_release_x10
CStrings:
+ "HPSProductUtils: isShortScreenDevice -> %s"
+ "LandscapeLeft"
+ "LandscapeRight"
+ "NON_LANDSCAPE_LEFT_MODE_ALERT_DETAIL"
+ "NON_LANDSCAPE_LEFT_MODE_ALERT_TITLE"
+ "Portrait"
+ "PortraitUpsideDown"
+ "Spatial Profile: Enrollment not supported, Tall Screen: %u, Orientation: %@, Show pop up alert"
+ "Spatial Profile: Force hiding Prox Card"
+ "Spatial Profile: Interface Orientation Changed"
+ "Spatial Profile: Non Landscape Left Mode Detected, not supported, show pop up alert"
+ "Spatial Profile: Tall Screen: %u (%f), Orientation: %@"
+ "Spatial Profile: V68: localHardwareSupport was %s, forced to True for V68"
+ "True"
+ "Unrecognized (%ld)"
+ "v16@?0@\"<UIViewControllerTransitionCoordinatorContext>\"8"
```
