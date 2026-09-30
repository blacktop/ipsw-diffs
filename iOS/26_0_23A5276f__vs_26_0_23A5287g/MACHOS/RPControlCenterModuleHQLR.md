## RPControlCenterModuleHQLR

> `/System/Library/ControlCenter/Bundles/RPControlCenterModuleHQLR.bundle/RPControlCenterModuleHQLR`

```diff

-650.42.1.0.0
-  __TEXT.__text: 0x1a0f0
-  __TEXT.__auth_stubs: 0xfb0
-  __TEXT.__objc_stubs: 0x1660
-  __TEXT.__objc_methlist: 0xbb0
-  __TEXT.__const: 0xfa8
-  __TEXT.__cstring: 0x19ab
-  __TEXT.__objc_methname: 0x283d
+650.45.2.0.0
+  __TEXT.__text: 0x1b330
+  __TEXT.__auth_stubs: 0xfa0
+  __TEXT.__objc_stubs: 0x1740
+  __TEXT.__objc_methlist: 0xbf0
+  __TEXT.__const: 0x1028
+  __TEXT.__cstring: 0x19db
+  __TEXT.__objc_methname: 0x2965
   __TEXT.__objc_classname: 0x115
-  __TEXT.__objc_methtype: 0x678
+  __TEXT.__objc_methtype: 0x6ba
   __TEXT.__gcc_except_tab: 0x54
-  __TEXT.__oslogstring: 0x7bc
-  __TEXT.__swift5_typeref: 0x1ef8
-  __TEXT.__swift5_capture: 0x104
-  __TEXT.__swift5_reflstr: 0x2c4
+  __TEXT.__oslogstring: 0x99e
+  __TEXT.__swift5_typeref: 0x1b1e
+  __TEXT.__swift5_capture: 0xd4
+  __TEXT.__swift5_reflstr: 0x2f4
   __TEXT.__swift5_assocty: 0x140
-  __TEXT.__constg_swiftt: 0x6e8
+  __TEXT.__constg_swiftt: 0x7a0
   __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_fieldmd: 0x2fc
+  __TEXT.__swift5_fieldmd: 0x320
   __TEXT.__swift5_proto: 0x54
   __TEXT.__swift5_types: 0x54
-  __TEXT.__unwind_info: 0x7d0
-  __DATA_CONST.__auth_got: 0x7e8
-  __DATA_CONST.__got: 0x300
-  __DATA_CONST.__auth_ptr: 0x360
-  __DATA_CONST.__const: 0xab0
+  __TEXT.__unwind_info: 0x7f8
+  __DATA_CONST.__auth_got: 0x7e0
+  __DATA_CONST.__got: 0x2d8
+  __DATA_CONST.__auth_ptr: 0x350
+  __DATA_CONST.__const: 0xab8
   __DATA_CONST.__cfstring: 0x400
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0x1a38
-  __DATA.__objc_selrefs: 0xa68
-  __DATA.__objc_ivar: 0xc0
-  __DATA.__objc_data: 0x808
-  __DATA.__data: 0xb10
-  __DATA.__bss: 0xc98
+  __DATA.__objc_const: 0x1ae8
+  __DATA.__objc_selrefs: 0xab0
+  __DATA.__objc_ivar: 0xc4
+  __DATA.__objc_data: 0x690
+  __DATA.__data: 0xd40
+  __DATA.__bss: 0xcc8
   __DATA.__common: 0xb8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: AA2A50EF-C514-3F24-95F5-84B19B749210
-  Functions: 756
-  Symbols:   233
-  CStrings:  739
+  UUID: 965AE29C-E786-34B6-9C90-5B1FBD1DF096
+  Functions: 780
+  Symbols:   236
+  CStrings:  765
 
Symbols:
+ _NSStringFromCGSize
+ _dispatch_assert_queue$V2
+ _objc_retain_x26
+ _swift_deletedMethodError
+ _swift_weakDestroy
+ _swift_weakInit
+ _swift_weakLoadStrong
- _OBJC_CLASS_$_UIDevice
- _objc_retain_x10
- _objc_retain_x24
- _objc_retain_x3
CStrings:
+ " [INFO] %{public}s:%d currentRotation=%@ newRotation=%@ mirrorType=%d _orientation=%@ orientation=%@ portType=%@ deviceType=%@"
+ " [INFO] %{public}s:%d size=%@"
+ "-[RPCCUIVideoView updateIntrinsicContentSize:]"
+ "B24@0:8^{opaqueCMSampleBuffer=}16"
+ "NOT isZeroOr180"
+ "RPCCUICallRecordingView: prepare video effects preview"
+ "RPCCUICallRecordingView: preview.videoView == nil"
+ "RPCCUICallRecordingView: will start frame receiver"
+ "RPCCUICallRecordingView: will stop frame receiver"
+ "T{CGSize=dd},R,N"
+ "VideoViewRep: makeUIView %@"
+ "VideoViewRep: updateUIView %@"
+ "YES isZeroOr180"
+ "_currentAffineTransform"
+ "_intrinsic"
+ "_isLandscape"
+ "containsString:"
+ "currentInterfaceOrientation"
+ "defaultSize"
+ "flushWithRemovalOfDisplayedImage:completionHandler:"
+ "intrinsicContentSize"
+ "invalidateIntrinsicContentSize"
+ "isLandscape"
+ "maxDimensions"
+ "numberWithInteger:"
+ "preview"
+ "sampleBufferRenderer"
+ "set aspect ratio %f (w:%f, h:%f), isLandscape:%{bool}d, transform %s, videoView intrinsicContentSize %s"
+ "setupVideoEffectsPreviewForAppear"
+ "teardownVideoEffectsPreviewForDisappear"
+ "transform rotation component %f"
+ "updateIntrinsicContentSize:"
+ "updating the transform, width and height"
+ "v32@0:8{CGSize=dd}16"
+ "{CGSize=\"width\"d\"height\"d}"
+ "{CGSize=dd}16@0:8"
- " [INFO] %{public}s:%d currentRotation=%@ newRotation=%@ mirrorType=%d orientation=%ld portType=%@ deviceType=%@"
- "FrameReceiver View appeared"
- "FrameReceiver View dissappeared"
- "availableFrameSenderEndpointsbyPID"
- "currentAffineTransform"
- "currentDevice"
- "flushAndRemoveImage"
- "orientation"
- "set aspect ratio %f, transform %s"
- "v24@0:8^{opaqueCMSampleBuffer=}16"

```
