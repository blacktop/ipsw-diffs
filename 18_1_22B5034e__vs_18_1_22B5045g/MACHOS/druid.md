## druid

> `/System/Library/PrivateFrameworks/DragUI.framework/Support/druid`

```diff

-8104.1.0.0.0
-  __TEXT.__text: 0x2e41c
-  __TEXT.__auth_stubs: 0xe90
-  __TEXT.__objc_stubs: 0x7a80
-  __TEXT.__objc_methlist: 0x29f4
+8108.0.0.0.0
+  __TEXT.__text: 0x2e514
+  __TEXT.__auth_stubs: 0xe50
+  __TEXT.__objc_stubs: 0x7aa0
+  __TEXT.__objc_methlist: 0x2a6c
   __TEXT.__const: 0x220
   __TEXT.__cstring: 0x14e1
-  __TEXT.__oslogstring: 0x275e
-  __TEXT.__objc_methname: 0xb79c
-  __TEXT.__objc_classname: 0x70b
-  __TEXT.__objc_methtype: 0x2c01
-  __TEXT.__gcc_except_tab: 0x6a4
+  __TEXT.__oslogstring: 0x2786
+  __TEXT.__objc_methname: 0xb93a
+  __TEXT.__objc_classname: 0x72a
+  __TEXT.__objc_methtype: 0x2c0a
+  __TEXT.__gcc_except_tab: 0x698
   __TEXT.__ustring: 0x20
-  __TEXT.__dlopen_cstrs: 0x4f
   __TEXT.__constg_swiftt: 0x58
   __TEXT.__swift5_typeref: 0x33
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0xc50
+  __TEXT.__unwind_info: 0xc48
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__auth_got: 0x758
-  __DATA_CONST.__got: 0x3b0
+  __DATA_CONST.__auth_got: 0x738
+  __DATA_CONST.__got: 0x3a8
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x1ad8
+  __DATA_CONST.__const: 0x1ae0
   __DATA_CONST.__cfstring: 0xfc0
-  __DATA_CONST.__objc_classlist: 0x188
+  __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x100
+  __DATA_CONST.__objc_superrefs: 0x108
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x7d28
-  __DATA.__objc_selrefs: 0x2458
-  __DATA.__objc_ivar: 0x4cc
-  __DATA.__objc_data: 0xfc8
+  __DATA.__objc_const: 0x7e78
+  __DATA.__objc_selrefs: 0x2480
+  __DATA.__objc_ivar: 0x4dc
+  __DATA.__objc_data: 0x1018
   __DATA.__data: 0xd70
-  __DATA.__bss: 0x348
+  __DATA.__bss: 0x340
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/PlatterKit.framework/PlatterKit
   - /System/Library/PrivateFrameworks/PrototypeTools.framework/PrototypeTools
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /System/Library/PrivateFrameworks/UniversalControl.framework/UniversalControl

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1241
-  Symbols:   397
-  CStrings:  2671
+  Functions: 1249
+  Symbols:   393
+  CStrings:  2681
 
Symbols:
+ _FPURLIsLocatedOnRemovableStorage
- _dlsym
- _free
- _abort_report_np
- _dlerror
- __sl_dlopen
CStrings:
+ "notifySessionWillBegin:configuration:completion:"
+ "Oneness session %!@(MISSING) - disableDragDisplay"
+ "_shouldNotifyForSession:"
+ "setContinuityDisplayWantsDragsHidden:"
+ "@68@0:8I16@20@28@36@44@52@60"
+ "DROnenessDragMonitorConnection"
+ "TB,N,V_continuityDisplayWantsDragsHidden"
+ "sourceIsHostedOnContinuityDisplay"
+ "_originatedFromContinuityDisplay"
+ "continuityDisplayWantsDragsHidden"
+ "_sourceIsHostedOnContinuityDisplay"
+ "NotifyPhoneMirroringOutsideContinuityShell"
+ "T@\"DRTouchTrackingWindow\",R,W,N,V_sourceInteractionWindow"
+ "com.apple.screencontinuity.dragserver"
+ "_notifyListenersSessionWillBegin:configuration:completion:"
+ "setSourceIsHostedOnContinuityDisplay:"
+ "_continuityDisplayWantsDragsHidden"
+ "com.apple.DragUI.NotifyPhoneMirroringOutsideContinuityShell"
+ "originatedFromContinuityDisplay"
+ "v40@0:8@\"DRDragSession\"16@\"UIDraggingSessionConfiguration\"24@?<v@?>32"
+ "disableDragDisplay"
+ "initWithIdentifier:configuration:mainWindow:sourceConnection:accessibilityConnection:clientSource:delegate:"
+ "TB,N,V_sourceIsHostedOnContinuityDisplay"
+ "TB,R,N,V_originatedFromContinuityDisplay"
+ "isHostedOnContinuityDisplayForDragSession:"
- "T@\"DRTouchTrackingWindow\",W,N,V_sourceInteractionWindow"
- "FPURLIsLocatedOnRemovableStorage"
- "v32@0:8@\"DRDragSession\"16@\"UIDraggingSessionConfiguration\"24"
- "softlink:r:path:/System/Library/Frameworks/FileProvider.framework/FileProvider"
- "%!s(MISSING)"
- "_notifyListenersSessionWillBegin:configuration:"
- "notifySessionWillBegin:configuration:"
- "@64@0:8I16@20I28@32@40@48@56"
- "initWithIdentifier:configuration:mainWindowContextID:sourceConnection:accessibilityConnection:clientSource:delegate:"
- "com.apple.oneness.dragserver"
- "_sourceInteractionWindowForDragSession:"
- "setSourceInteractionWindow:"
- "_windowWithContextId:"
- "HidePreviewsInPhoneMirroring"
- "com.apple.DragUI.HidePreviewsInPhoneMirroring"

```
