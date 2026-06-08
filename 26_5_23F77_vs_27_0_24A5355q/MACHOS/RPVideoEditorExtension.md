## RPVideoEditorExtension

> `/System/Library/Frameworks/ReplayKit.framework/PlugIns/RPVideoEditorExtension.appex/RPVideoEditorExtension`

```diff

-710.1.1.0.0
-  __TEXT.__text: 0xbcd0
-  __TEXT.__auth_stubs: 0x440
-  __TEXT.__objc_stubs: 0x2bc0
-  __TEXT.__objc_methlist: 0xee0
-  __TEXT.__const: 0xb8
-  __TEXT.__cstring: 0x7c5
-  __TEXT.__oslogstring: 0x797
-  __TEXT.__objc_classname: 0x20d
-  __TEXT.__objc_methtype: 0x75e
-  __TEXT.__gcc_except_tab: 0x24c
-  __TEXT.__objc_methname: 0x2e93
-  __TEXT.__unwind_info: 0x440
-  __DATA_CONST.__auth_got: 0x230
-  __DATA_CONST.__got: 0x248
-  __DATA_CONST.__const: 0x420
+740.44.1.0.0
+  __TEXT.__text: 0xb69c
+  __TEXT.__auth_stubs: 0x480
+  __TEXT.__objc_stubs: 0x2e20
+  __TEXT.__objc_methlist: 0xf28
+  __TEXT.__const: 0x98
+  __TEXT.__cstring: 0xa11
+  __TEXT.__oslogstring: 0x741
+  __TEXT.__objc_classname: 0x1fb
+  __TEXT.__objc_methname: 0x30d0
+  __TEXT.__objc_methtype: 0x76c
+  __TEXT.__gcc_except_tab: 0x214
+  __TEXT.__unwind_info: 0x298
+  __DATA_CONST.__const: 0x400
   __DATA_CONST.__cfstring: 0x300
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA.__objc_const: 0x1ad8
-  __DATA.__objc_selrefs: 0xda8
-  __DATA.__objc_ivar: 0x134
+  __DATA_CONST.__auth_got: 0x250
+  __DATA_CONST.__got: 0x248
+  __DATA.__objc_const: 0x1b68
+  __DATA.__objc_selrefs: 0xe48
+  __DATA.__objc_ivar: 0x140
   __DATA.__objc_data: 0x320
-  __DATA.__data: 0x3d0
-  __DATA.__bss: 0x38
+  __DATA.__data: 0x3c8
+  __DATA.__bss: 0x30
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 03A83A60-1765-3479-AB15-31B2AD5592A6
-  Functions: 304
-  Symbols:   184
-  CStrings:  807
+  UUID: 6A3CA05C-A74F-3D9C-93E7-09CF82D57954
+  Functions: 305
+  Symbols:   188
+  CStrings:  840
 
Symbols:
+ _AVAssetExportPresetPassthroughVideoAACAudio
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
- _CGRectIsEmpty
- _CGRectNull
- _MGGetSInt32Answer
- _objc_retainAutoreleasedReturnValue
CStrings:
+ " [ERROR] %{public}s:%d Error loading input item for type, error=%@"
+ " [ERROR] %{public}s:%d error calling extension, error=%@"
+ " [INFO] %{public}s:%d %s"
+ " [INFO] %{public}s:%d did save final video to videoURL=%@"
+ " [INFO] %{public}s:%d isInternalTestMode: %@"
+ " [INFO] %{public}s:%d loaded input items"
+ " [INFO] %{public}s:%d will save video to videoURL=%@"
+ "-[RPVideoEditorExtensionContext doAction:]"
+ "-[RPVideoEditorExtensionContext extensionObjectProxy]_block_invoke"
+ "-[RPVideoEditorExtensionViewController inputItemsFromClientWithCompletionHandler:]"
+ "-[RPVideoEditorExtensionViewController inputItemsFromClientWithCompletionHandler:]_block_invoke_2"
+ "-[RPVideoEditorExtensionViewController setupChildViewControllers]"
+ "-[RPVideoEditorExtensionViewController videoEditor:didFinishWithActivityTypes:]"
+ "-[RPVideoEditorExtensionViewController viewDidDisappear:]"
+ "-[RPVideoEditorViewController saveAction]_block_invoke_2"
+ "-[RPVideoEditorViewController saveAction]_block_invoke_3"
+ "@48@0:8@16@24@32@40"
+ "T@\"UILabel\",&,N,V_titleSubtitleLabel"
+ "T@\"UIView\",&,N,V_backgroundView"
+ "T@\"UIView\",&,N,V_titleContainer"
+ "T{CGSize=dd},N,V_videoOverlayPlayButtonSize"
+ "_backgroundView"
+ "_titleContainer"
+ "_titleSubtitleLabel"
+ "_videoOverlayPlayButtonSize"
+ "activateConstraints:"
+ "addConstraints:"
+ "applyCommonConstraints"
+ "backgroundView"
+ "bottomAnchor"
+ "centerXAnchor"
+ "centerYAnchor"
+ "com.apple.ScreenCaptureKitTestRunneriOS"
+ "constraintEqualToAnchor:"
+ "constraintEqualToAnchor:constant:"
+ "constraintEqualToConstant:"
+ "heightAnchor"
+ "initWithBundleIdentifier:URL:applicationName:overrideTintColor:"
+ "labelColor"
+ "leadingAnchor"
+ "numberWithBool:"
+ "safeAreaLayoutGuide"
+ "setBackgroundView:"
+ "setNeedsLayout"
+ "setPreferredVibrancy:"
+ "setTitleContainer:"
+ "setTitleSubtitleLabel:"
+ "setVideoOverlayPlayButtonSize:"
+ "titleContainer"
+ "titleSubtitleLabel"
+ "topAnchor"
+ "trailingAnchor"
+ "v32@0:8{CGSize=dd}16"
+ "videoOverlayPlayButtonSize"
+ "widthAnchor"
+ "{CGSize=\"width\"d\"height\"d}"
- "%s"
- "%s isInternalTestMode: %d"
- "-[RPVideoEditorViewController saveAction]_block_invoke_4"
- "@80@0:8@16@24@32@40{CGRect={CGPoint=dd}{CGSize=dd}}48"
- "Error loading input item for type"
- "JwLB44/jEB8aFDpXQ16Tuw"
- "RPVideoEditorExtensionContext:doAction"
- "RPVideoEditorExtensionViewController -inputItemsFromClientWithCompletionHandler:"
- "RPVideoEditorExtensionViewController -setupChildViewControllers"
- "RPVideoEditorExtensionViewController -videoEditorViewDidFinishWithActivityTypes:"
- "RPVideoEditorExtensionViewController -viewDidDisappear:"
- "TB,V_hasHomeButton"
- "_hasHomeButton"
- "deviceHasHomeButton"
- "error calling extension - %i"
- "hasHomeButton"
- "initWithBundleIdentifier:URL:applicationName:overrideTintColor:size:"
- "loaded input items"
- "setClipsToBounds:"
- "setHasHomeButton:"
- "traitCollection"
- "userInterfaceStyle"
- "whiteColor"

```
