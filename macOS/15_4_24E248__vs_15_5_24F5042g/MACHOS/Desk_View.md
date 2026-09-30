## Desk View

> `/System/Library/CoreServices/Applications/Desk View.app/Contents/MacOS/Desk View`

```diff

-587.101.4.0.0
-  __TEXT.__text: 0x13e90
-  __TEXT.__auth_stubs: 0x5a0
-  __TEXT.__objc_stubs: 0x4ea0
+587.120.2.0.1
+  __TEXT.__text: 0x16600
+  __TEXT.__auth_stubs: 0x5c0
+  __TEXT.__objc_stubs: 0x4f00
   __TEXT.__objc_methlist: 0x1ad0
-  __TEXT.__const: 0x3c0
+  __TEXT.__const: 0x3e0
   __TEXT.__gcc_except_tab: 0x2dc
-  __TEXT.__objc_methname: 0x5762
-  __TEXT.__cstring: 0xca5
+  __TEXT.__objc_methname: 0x5771
+  __TEXT.__cstring: 0x1140
   __TEXT.__objc_classname: 0x26a
   __TEXT.__objc_methtype: 0xefb
-  __TEXT.__oslogstring: 0x96
-  __TEXT.__unwind_info: 0x448
-  __DATA_CONST.__auth_got: 0x2e0
+  __TEXT.__oslogstring: 0xa47
+  __TEXT.__unwind_info: 0x468
+  __DATA_CONST.__auth_got: 0x2f0
   __DATA_CONST.__got: 0x320
-  __DATA_CONST.__const: 0x378
-  __DATA_CONST.__cfstring: 0x10c0
+  __DATA_CONST.__const: 0x3b8
+  __DATA_CONST.__cfstring: 0x11c0
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_intobj: 0x1f8
   __DATA.__objc_const: 0x2d90
-  __DATA.__objc_selrefs: 0x18a8
+  __DATA.__objc_selrefs: 0x18b0
   __DATA.__objc_ivar: 0x24c
   __DATA.__objc_data: 0x690
   __DATA.__data: 0x2a0
-  __DATA.__common: 0xc0
+  __DATA.__common: 0xe0
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 513
-  Symbols:   210
-  CStrings:  1430
+  Functions: 514
+  Symbols:   212
+  CStrings:  1493
 
Symbols:
+ _NSStringFromRect
+ _NSStringFromSize
CStrings:
+ "-[DCACursiveTextPath initWithURL:resolution:]"
+ "-[DCAScreenCaptureSession configureWithSessionID:]"
+ "-[DCAScreenCaptureSession shareWindowID:]"
+ "-[DCAScreenCaptureSession shareWindowID:]_block_invoke"
+ "-[DCAScreenCaptureSession shareWindowID:]_block_invoke_2"
+ "-[DCASession _deviceForID:]"
+ "-[DCASession _deviceForID:]_block_invoke"
+ "-[DCASession _sessionQueue_configureSessionWithPreferredDeviceID:deskViewCameraMode:]"
+ "-[DCASession _setOverheadCameraMode:]_block_invoke"
+ "-[DCASession deviceConnected:]"
+ "-[DCASession deviceDisconnected:]"
+ "-[DCASession setGeometry:]"
+ "-[DCASession setStatus:]"
+ "-[DCASetupInstructionView _iconViewSizeForImage:requestedWidth:containerDimension:]"
+ "-[DCASetupOverlayView newCropRegionPathForMetadata:zoomFactor:]"
+ "-[DCAViewController _updateForZoomFactor:]"
+ "-[DCAViewController initWithPreferredDeviceID:]"
+ "-[DCAViewController setScreenSessionID:]"
+ "-[DCAppDelegate application:openURLs:]"
+ "<<<< DCACursiveTextPath >>>> %s: Error loading hello.json from file: %@"
+ "<<<< DCACursiveTextPath >>>> %s: Error parsing hello.json from data: %@"
+ "<<<< DCAScreenCaptureSession >>>> %s: Failed to replace screen share with desk cam window error=%@"
+ "<<<< DCAScreenCaptureSession >>>> %s: Failed to start sharing desk cam window error=%@"
+ "<<<< DCAScreenCaptureSession >>>> %s: Unable to create sharing session instance from ID: %@"
+ "<<<< DCAScreenCaptureSession >>>> %s: Unable to get active shareable destinations error=%@"
+ "<<<< DCAScreenCaptureSession >>>> %s: Unable to share window, no sharing picker"
+ "<<<< DCAScreenCaptureSession >>>> %s: Unable to share window, no sharing session"
+ "<<<< DCASession >>>> %s: %ld. %@ (%@)"
+ "<<<< DCASession >>>> %s: Adding input: %@"
+ "<<<< DCASession >>>> %s: Attempting to show the desk view with no device"
+ "<<<< DCASession >>>> %s: Can not configure the session with a nil device"
+ "<<<< DCASession >>>> %s: Could not add video data output to the session"
+ "<<<< DCASession >>>> %s: Could not add video device input to the session"
+ "<<<< DCASession >>>> %s: Device disconnected: %@ (%@)"
+ "<<<< DCASession >>>> %s: Error creating input with device %@"
+ "<<<< DCASession >>>> %s: Found %ld DeskCam devices from AVCaptureDeviceDiscoverySession:"
+ "<<<< DCASession >>>> %s: New device connected: %@ (%@)"
+ "<<<< DCASession >>>> %s: New session geometry (%@ in %@)"
+ "<<<< DCASession >>>> %s: New session status (%@)"
+ "<<<< DCASession >>>> %s: No DeskCam devices found from AVCaptureDeviceDiscoverySession"
+ "<<<< DCASession >>>> %s: Removing input: %@"
+ "<<<< DCASession >>>> %s: Skipping adding input %@, it is already in the session"
+ "<<<< DCASession >>>> %s: preferredDeviceID was %@ but unable to find an AVCaptureDevice with that id"
+ "<<<< DCASetupInstructionView >>>> %s: Icon image with unexpected zero size: %@"
+ "<<<< DCASetupOverlayView >>>> %s: Auto zoom factor out of range [1.0, 2.0]: %.3f"
+ "<<<< DCAViewController >>>> %s: Failed to persist zoomFactorsByDeviceID dictionary: %{public}@"
+ "<<<< DCAViewController >>>> %s: Failed to read in zoomFactorsByDeviceID dictionary: %@"
+ "<<<< DCAViewController >>>> %s: New screen session with ID: %{public}@"
+ "<<<< DCAViewController >>>> %s: Screen session ID matches existing ID: %{public}@"
+ "<<<< DCAppDelegate >>>> %s: Application reading URL: %@"
+ "<<<< DCAppDelegate >>>> %s: No URL was found"
+ "<<<< DCAppDelegate >>>> %s: Parsed preferredDeviceID: %@"
+ "<<<< DCAppDelegate >>>> %s: Parsed screenSessionID: %@"
+ "<<<< DCAppDelegate >>>> %s: Parsed windowFrame: %@"
+ "absoluteString"
+ "kCGImagePropertyOrientationDown"
+ "kCGImagePropertyOrientationDownMirrored"
+ "kCGImagePropertyOrientationLeft"
+ "kCGImagePropertyOrientationLeftMirrored"
+ "kCGImagePropertyOrientationRight"
+ "kCGImagePropertyOrientationRightMirrored"
+ "kCGImagePropertyOrientationUp"
+ "kCGImagePropertyOrientationUpMirrored"

```
