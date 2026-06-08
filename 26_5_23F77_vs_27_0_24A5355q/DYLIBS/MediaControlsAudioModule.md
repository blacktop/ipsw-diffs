## MediaControlsAudioModule

> `/System/Library/ControlCenter/Bundles/MediaControlsAudioModule.bundle/MediaControlsAudioModule`

```diff

-4025.610.1.0.0
-  __TEXT.__text: 0x33c
-  __TEXT.__auth_stubs: 0xb0
-  __TEXT.__objc_methlist: 0x284
-  __TEXT.__unwind_info: 0x70
-  __TEXT.__objc_classname: 0x80
-  __TEXT.__objc_methname: 0x69f
-  __TEXT.__objc_methtype: 0x366
-  __TEXT.__objc_stubs: 0x180
-  __DATA_CONST.__got: 0x20
+4026.100.60.1.0
+  __TEXT.__text: 0x2fc
+  __TEXT.__objc_methlist: 0x2b4
+  __TEXT.__cstring: 0x2
+  __TEXT.__unwind_info: 0x78
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x190
-  __AUTH_CONST.__auth_got: 0x60
-  __AUTH_CONST.__objc_const: 0x3d8
+  __DATA_CONST.__objc_selrefs: 0x1d0
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__objc_const: 0x3e0
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0xc
   __DATA.__data: 0x180
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/ControlCenterUIKit.framework/ControlCenterUIKit
   - /System/Library/PrivateFrameworks/MediaControls.framework/MediaControls
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3EC46DB5-4FCD-393C-8EDF-286E71AF7CAA
-  Functions: 16
-  Symbols:   21
-  CStrings:  101
+  UUID: D75BEAD1-7981-3475-A5E8-41C1E5FB9714
+  Functions: 17
+  Symbols:   24
+  CStrings:  0
 
Symbols:
+ _OBJC_CLASS_$_CCUIContentModulePreviewProvider
+ _OBJC_CLASS_$_CCUIContentModuleSliderPreviewDescription
+ _OBJC_CLASS_$_MRUOutputDeviceAsset
+ _OBJC_CLASS_$_MRUSystemVolumeController
+ _OBJC_CLASS_$_UIColor
+ _objc_alloc_init
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x20
+ _objc_retainAutoreleaseReturnValue
- _OBJC_CLASS_$_MRUFeatureFlagProvider
- _objc_release
- _objc_release_x22
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x20
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"CCUIContentModuleContext\""
- "@\"MRUVisualStylingProvider\"16@0:8"
- "@\"MRUVolumeBackgroundViewController\""
- "@\"MRUVolumeViewController\""
- "@\"NSString\"16@0:8"
- "@\"UIViewController<CCUIContentModuleBackgroundViewController>\"16@0:8"
- "@\"UIViewController<CCUIContentModuleBackgroundViewController>\"24@0:8@\"CCUIContentModulePresentationContext\"16"
- "@\"UIViewController<CCUIContentModuleContentViewController>\"16@0:8"
- "@\"UIViewController<CCUIContentModuleContentViewController>\"24@0:8@\"CCUIContentModulePresentationContext\"16"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "CCUIContentModule"
- "MRUVolumeBackgroundViewControllerDelegate"
- "MRUVolumeViewControllerDelegate"
- "MediaControlsAudioModule"
- "NSObject"
- "Q16@0:8"
- "T#,R"
- "T@\"CCUIContentModuleContext\",&,N,V_contentModuleContext"
- "T@\"MRUVolumeBackgroundViewController\",&,N,V_volumeBackgroundViewController"
- "T@\"MRUVolumeViewController\",&,N,V_volumeViewController"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",?,R,C,N"
- "T@\"NSString\",R,C"
- "T@\"UIViewController<CCUIContentModuleBackgroundViewController>\",?,R,N"
- "T@\"UIViewController<CCUIContentModuleContentViewController>\",?,R,N"
- "TB,?,R,N"
- "TQ,?,R,N"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_contentModuleContext"
- "_volumeBackgroundViewController"
- "_volumeViewController"
- "autorelease"
- "backgroundViewController"
- "backgroundViewControllerForContext:"
- "class"
- "conformsToProtocol:"
- "contentModuleContext"
- "contentViewController"
- "contentViewControllerForContext:"
- "debugDescription"
- "description"
- "environment"
- "expandsGridSizeClassesForAccessibility"
- "hash"
- "initWithAudioModuleController:"
- "invalidateContainerViewsForPlatterTreatment"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isNewControlsEnabled"
- "isProxy"
- "moduleDescription"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "release"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setContentModuleContext:"
- "setDelegate:"
- "setPrimaryGlyphShouldBeTinted:"
- "setPrimaryInteractionEnabled:"
- "setSecondaryInteractionEnabled:"
- "setSystemVolumeValue:"
- "setVolumeBackgroundViewController:"
- "setVolumeViewController:"
- "sharedController"
- "stylingProvider"
- "superclass"
- "supportedGridSizeClasses"
- "v16@0:8"
- "v24@0:8@\"CCUIContentModuleContext\"16"
- "v24@0:8@\"MRUVolumeViewController\"16"
- "v24@0:8@16"
- "v28@0:8@\"MRUVolumeBackgroundViewController\"16B24"
- "v28@0:8@\"MRUVolumeViewController\"16f24"
- "v28@0:8@16B24"
- "v28@0:8@16f24"
- "volumeBackgroundViewController"
- "volumeBackgroundViewController:didUpdatePrimaryInteractionEnabled:"
- "volumeBackgroundViewController:didUpdateSecondaryInteractionEnabled:"
- "volumeBackgroundViewControllerStylingProvider"
- "volumeViewController"
- "volumeViewController:didChangeSystemVolumeValue:"
- "volumeViewControllerDidInvalidateContainerViewsForPlatterTreatment:"
- "zone"

```
