## Desk View

> `/System/Library/CoreServices/Applications/Desk View.app/Contents/MacOS/Desk View`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__got`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_floatobj`
- `__DATA_CONST.__objc_doubleobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-665.140.4.0.0
-  __TEXT.__text: 0x18474
-  __TEXT.__auth_stubs: 0x5c0
-  __TEXT.__objc_stubs: 0x5100
+665.140.6.0.0
+  __TEXT.__text: 0x15ee4
+  __TEXT.__auth_stubs: 0x5a0
+  __TEXT.__objc_stubs: 0x50a0
   __TEXT.__objc_methlist: 0x1b10
-  __TEXT.__const: 0x3e8
+  __TEXT.__const: 0x3e0
   __TEXT.__gcc_except_tab: 0x244
-  __TEXT.__objc_methname: 0x591d
-  __TEXT.__cstring: 0x12fe
+  __TEXT.__objc_methname: 0x590e
+  __TEXT.__cstring: 0xe31
   __TEXT.__objc_classname: 0x26a
   __TEXT.__objc_methtype: 0xf1b
-  __TEXT.__oslogstring: 0xbf1
-  __TEXT.__unwind_info: 0x688
-  __DATA_CONST.__auth_got: 0x2f0
+  __TEXT.__oslogstring: 0x208
+  __TEXT.__unwind_info: 0x668
+  __DATA_CONST.__auth_got: 0x2e0
   __DATA_CONST.__got: 0x340
-  __DATA_CONST.__const: 0x3c0
-  __DATA_CONST.__cfstring: 0x12a0
+  __DATA_CONST.__const: 0x380
+  __DATA_CONST.__cfstring: 0x11a0
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_intobj: 0x1f8
   __DATA.__objc_const: 0x2d98
-  __DATA.__objc_selrefs: 0x1938
+  __DATA.__objc_selrefs: 0x1930
   __DATA.__objc_ivar: 0x24c
   __DATA.__objc_data: 0x690
   __DATA.__data: 0x2a0
-  __DATA.__common: 0xe0
+  __DATA.__common: 0xc0
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 520
-  Symbols:   216
-  CStrings:  1494
+  Functions: 519
+  Symbols:   214
+  CStrings:  1429
 
Symbols:
- _NSStringFromRect
- _NSStringFromSize
CStrings:
- "-[DCACursiveTextPath initWithURL:resolution:]"
- "-[DCAScreenCaptureSession configureWithSessionID:]"
- "-[DCAScreenCaptureSession shareWindowID:]"
- "-[DCAScreenCaptureSession shareWindowID:]_block_invoke"
- "-[DCAScreenCaptureSession shareWindowID:]_block_invoke_2"
- "-[DCASession _deviceForID:]"
- "-[DCASession _deviceForID:]_block_invoke"
- "-[DCASession _sessionQueue_configureSessionWithPreferredDeviceID:deskViewCameraMode:]"
- "-[DCASession _setOverheadCameraMode:]_block_invoke"
- "-[DCASession deviceConnected:]"
- "-[DCASession deviceDisconnected:]"
- "-[DCASession setGeometry:]"
- "-[DCASession setStatus:]"
- "-[DCASetupInstructionView _iconViewSizeForImage:requestedWidth:containerDimension:]"
- "-[DCASetupOverlayView newCropRegionPathForMetadata:zoomFactor:]"
- "-[DCAViewController _updateForZoomFactor:]"
- "-[DCAViewController deskViewCameraTypeForDevice:]"
- "-[DCAViewController initWithPreferredDeviceID:]"
- "-[DCAViewController setScreenSessionID:]"
- "-[DCAppDelegate application:openURLs:]"
- "<<<< DCACursiveTextPath >>>> %s: Error loading hello.json from file: %@"
- "<<<< DCACursiveTextPath >>>> %s: Error parsing hello.json from data: %@"
- "<<<< DCAScreenCaptureSession >>>> %s: Failed to replace screen share with desk cam window error=%@"
- "<<<< DCAScreenCaptureSession >>>> %s: Failed to start sharing desk cam window error=%@"
- "<<<< DCAScreenCaptureSession >>>> %s: Unable to create sharing session instance from ID: %@"
- "<<<< DCAScreenCaptureSession >>>> %s: Unable to get active shareable destinations error=%@"
- "<<<< DCAScreenCaptureSession >>>> %s: Unable to share window, no sharing picker"
- "<<<< DCAScreenCaptureSession >>>> %s: Unable to share window, no sharing session"
- "<<<< DCASession >>>> %s: %ld. %@ (%@)"
- "<<<< DCASession >>>> %s: Adding input: %@"
- "<<<< DCASession >>>> %s: Attempting to show the desk view with no device"
- "<<<< DCASession >>>> %s: Can not configure the session with a nil device"
- "<<<< DCASession >>>> %s: Could not add video data output to the session"
- "<<<< DCASession >>>> %s: Could not add video device input to the session"
- "<<<< DCASession >>>> %s: Device disconnected: %@ (%@)"
- "<<<< DCASession >>>> %s: Error creating input with device %@"
- "<<<< DCASession >>>> %s: Found %ld DeskCam devices from AVCaptureDeviceDiscoverySession:"
- "<<<< DCASession >>>> %s: New device connected: %@ (%@)"
- "<<<< DCASession >>>> %s: New session geometry (%@ in %@)"
- "<<<< DCASession >>>> %s: New session status (%@)"
- "<<<< DCASession >>>> %s: No DeskCam devices found from AVCaptureDeviceDiscoverySession"
- "<<<< DCASession >>>> %s: Removing input: %@"
- "<<<< DCASession >>>> %s: Skipping adding input %@, it is already in the session"
- "<<<< DCASession >>>> %s: preferredDeviceID was %@ but unable to find an AVCaptureDevice with that id"
- "<<<< DCASetupInstructionView >>>> %s: Icon image with unexpected zero size: %@"
- "<<<< DCASetupOverlayView >>>> %s: Auto zoom factor out of range [1.0, 2.0]: %.3f"
- "<<<< DCAViewController >>>> %s: Failed to persist zoomFactorsByDeviceID dictionary: %{public}@"
- "<<<< DCAViewController >>>> %s: Failed to read in zoomFactorsByDeviceID dictionary: %@"
- "<<<< DCAViewController >>>> %s: New screen session with ID: %{public}@"
- "<<<< DCAViewController >>>> %s: Screen session ID matches existing ID: %{public}@"
- "<<<< DCAViewController >>>> %s: Unknown display PID: %d"
- "<<<< DCAppDelegate >>>> %s: Application reading URL: %@"
- "<<<< DCAppDelegate >>>> %s: No URL was found"
- "<<<< DCAppDelegate >>>> %s: Parsed preferredDeviceID: %@"
- "<<<< DCAppDelegate >>>> %s: Parsed screenSessionID: %@"
- "<<<< DCAppDelegate >>>> %s: Parsed windowFrame: %@"
- "absoluteString"
- "kCGImagePropertyOrientationDown"
- "kCGImagePropertyOrientationDownMirrored"
- "kCGImagePropertyOrientationLeft"
- "kCGImagePropertyOrientationLeftMirrored"
- "kCGImagePropertyOrientationRight"
- "kCGImagePropertyOrientationRightMirrored"
- "kCGImagePropertyOrientationUp"
- "kCGImagePropertyOrientationUpMirrored"
```
