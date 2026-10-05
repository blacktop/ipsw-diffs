## Bridge

> `/private/var/staged_system_apps/Bridge.app/Bridge`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_entry`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_nlclslist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1372.0.0.0.0
-  __TEXT.__text: 0x23720c
+1377.1.0.0.0
+  __TEXT.__text: 0x238190
   __TEXT.__auth_stubs: 0x5de0
-  __TEXT.__objc_stubs: 0x22a60
-  __TEXT.__objc_methlist: 0x16ba4
-  __TEXT.__const: 0x29216
-  __TEXT.__gcc_except_tab: 0x2a74
-  __TEXT.__objc_methname: 0x3da45
+  __TEXT.__objc_stubs: 0x22c20
+  __TEXT.__objc_methlist: 0x16c74
+  __TEXT.__const: 0x29236
+  __TEXT.__gcc_except_tab: 0x2af8
+  __TEXT.__objc_methname: 0x3df45
   __TEXT.__objc_classname: 0x3f62
-  __TEXT.__objc_methtype: 0x8a49
-  __TEXT.__cstring: 0x1831e
+  __TEXT.__objc_methtype: 0x8a29
+  __TEXT.__cstring: 0x1833e
   __TEXT.__dlopen_cstrs: 0xa4f
-  __TEXT.__oslogstring: 0x15f9a
+  __TEXT.__oslogstring: 0x1611a
   __TEXT.__ustring: 0x2a8
   __TEXT.__constg_swiftt: 0x4428
   __TEXT.__swift5_typeref: 0x8a49

   __TEXT.__swift5_protos: 0x78
   __TEXT.__swift5_mpenum: 0x40
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0xa3d8
+  __TEXT.__unwind_info: 0xa418
   __TEXT.__eh_frame: 0x4204
-  __DATA_CONST.__const: 0xc050
+  __DATA_CONST.__const: 0xc078
   __DATA_CONST.__cfstring: 0x11f40
   __DATA_CONST.__objc_classlist: 0xbc0
   __DATA_CONST.__objc_nlclslist: 0x8

   __DATA_CONST.__objc_doubleobj: 0xf0
   __DATA_CONST.__objc_dictobj: 0x140
   __DATA_CONST.__auth_got: 0x2f08
-  __DATA_CONST.__got: 0x2c98
+  __DATA_CONST.__got: 0x2cc8
   __DATA_CONST.__auth_ptr: 0x1700
-  __DATA.__objc_const: 0x24008
-  __DATA.__objc_selrefs: 0xd510
-  __DATA.__objc_ivar: 0x160c
+  __DATA.__objc_const: 0x24120
+  __DATA.__objc_selrefs: 0xd5c8
+  __DATA.__objc_ivar: 0x1624
   __DATA.__objc_data: 0x8718
   __DATA.__data: 0x86c8
   __DATA.__common: 0x329

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12634
-  Symbols:   3323
-  CStrings:  15647
+  Functions: 12656
+  Symbols:   3329
+  CStrings:  15688
 
Symbols:
+ _AVCaptureSessionInterruptionEndedNotification
+ _AVCaptureSessionInterruptionReasonKey
+ _AVCaptureSessionWasInterruptedNotification
+ _OBJC_CLASS_$_UILayoutGuide
+ _OBJC_CLASS_$_UITraitHorizontalSizeClass
+ _OBJC_CLASS_$_UITraitVerticalSizeClass
CStrings:
+ "@\"UILayoutGuide\""
+ "App Store auto-update follow-up changed, reloading root settings specifiers"
+ "COSAppStoreAutoUpdateFollowUpChangedNotification"
+ "COSCameraInterruptedByMultitasking"
+ "Camera interrupted because Bridge is not the sole foreground app; falling back to manual pairing"
+ "Capture session interrupted (reason %ld)"
+ "Capture session interruption ended"
+ "Enabled multitasking camera access: preview stays live when Bridge is not the sole foreground app"
+ "Multitasking camera access not supported: preview will be interrupted when Bridge is not the sole foreground app"
+ "T@\"NSLayoutConstraint\",&,N,V_contentLayoutGuideTopConstraint"
+ "T@\"NSLayoutConstraint\",&,N,V_contentLayoutGuideTopSafeAreaConstraint"
+ "T@\"NSLayoutConstraint\",&,N,V_preferredScannerSuperviewHeightConstraint"
+ "T@\"NSLayoutConstraint\",&,N,V_preferredScannerSuperviewWidthConstraint"
+ "T@\"UILayoutGuide\",&,N,V_contentLayoutGuide"
+ "T@\"UIWebView\",W,N,V_styledReleaseNotesWebView"
+ "_contentLayoutGuide"
+ "_contentLayoutGuideTopConstraint"
+ "_contentLayoutGuideTopSafeAreaConstraint"
+ "_preferredScannerSuperviewHeightConstraint"
+ "_preferredScannerSuperviewWidthConstraint"
+ "_sizeClassDidChange"
+ "_styledReleaseNotesWebView"
+ "addLayoutGuide:"
+ "appStoreAutoUpdateFollowUpChanged:"
+ "contentLayoutGuide"
+ "contentLayoutGuideTopConstraint"
+ "contentLayoutGuideTopSafeAreaConstraint"
+ "handleCameraInterruptedByMultitasking"
+ "handleSessionInterrupted:"
+ "handleSessionInterruptionEnded:"
+ "html { -webkit-text-size-adjust: 100%%; }\nbody {color: #FFFFFF !important;}\na:link {color: %@;}\n"
+ "isMultitaskingCameraAccessEnabled"
+ "isMultitaskingCameraAccessSupported"
+ "preferredScannerSuperviewHeightConstraint"
+ "preferredScannerSuperviewWidthConstraint"
+ "registerForTraitChanges:withAction:"
+ "setBounces:"
+ "setContentLayoutGuide:"
+ "setContentLayoutGuideTopConstraint:"
+ "setContentLayoutGuideTopSafeAreaConstraint:"
+ "setMultitaskingCameraAccessEnabled:"
+ "setPreferredScannerSuperviewHeightConstraint:"
+ "setPreferredScannerSuperviewWidthConstraint:"
+ "setStyledReleaseNotesWebView:"
+ "styledReleaseNotesWebView"
+ "updateViewConstraints"
+ "viewSafeAreaInsetsDidChange"
+ "\xb1"
- "App Store auto-update follow-up cleared, reloading root settings specifiers"
- "COSAppStoreAutoUpdateFollowUpClearedNotification"
- "Q32@0:8@\"RUIObjectModel\"16@\"RUIPage\"24"
- "appStoreAutoUpdateFollowUpCleared:"
- "document.body.style.color='#FFFFFF';"
- "html { -webkit-text-size-adjust: 100%%; }\na:link {color: %@;}\n"
- "supportedInterfaceOrientationsForObjectModel:page:"
```
