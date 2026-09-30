## PhotosUIService

> `/Applications/PhotosUIService.app/PhotosUIService`

```diff

-760.6.150.0.0
-  __TEXT.__text: 0x1558
-  __TEXT.__auth_stubs: 0x210
-  __TEXT.__objc_stubs: 0x6a0
-  __TEXT.__objc_methlist: 0x624
-  __TEXT.__const: 0x8
-  __TEXT.__gcc_except_tab: 0xd4
-  __TEXT.__objc_methname: 0x12e5
-  __TEXT.__cstring: 0x336
-  __TEXT.__objc_classname: 0x14a
-  __TEXT.__objc_methtype: 0xb40
-  __TEXT.__unwind_info: 0x118
-  __DATA_CONST.__auth_got: 0x118
-  __DATA_CONST.__got: 0x78
-  __DATA_CONST.__const: 0xf0
-  __DATA_CONST.__cfstring: 0x260
+800.14.111.0.0
+  __TEXT.__text: 0x190c
+  __TEXT.__auth_stubs: 0x260
+  __TEXT.__objc_stubs: 0x8a0
+  __TEXT.__objc_methlist: 0x654
+  __TEXT.__const: 0x18
+  __TEXT.__gcc_except_tab: 0xe0
+  __TEXT.__objc_methname: 0x155f
+  __TEXT.__cstring: 0x369
+  __TEXT.__objc_classname: 0x14c
+  __TEXT.__objc_methtype: 0xbd0
+  __TEXT.__oslogstring: 0xa5
+  __TEXT.__unwind_info: 0x128
+  __DATA_CONST.__auth_got: 0x140
+  __DATA_CONST.__got: 0xa0
+  __DATA_CONST.__const: 0x158
+  __DATA_CONST.__cfstring: 0x280
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x20
-  __DATA.__objc_const: 0x850
-  __DATA.__objc_selrefs: 0x4a8
-  __DATA.__objc_ivar: 0x8
+  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA.__objc_const: 0x890
+  __DATA.__objc_selrefs: 0x538
+  __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x180
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Photos.framework/Photos
+  - /System/Library/Frameworks/SensitiveContentAnalysis.framework/SensitiveContentAnalysis
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit

   - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1E89F3B6-E115-3077-96D1-A0F558108FCB
-  Functions: 39
-  Symbols:   59
-  CStrings:  295
+  UUID: 1739A0F1-78F4-363D-B5AC-0E944ADA4D2E
+  Functions: 43
+  Symbols:   70
+  CStrings:  325
 
Symbols:
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_PHAsset
+ _OBJC_CLASS_$_PHFetchOptions
+ _OBJC_CLASS_$_PXSensitivityInterventionManager
+ _OBJC_CLASS_$_SCSensitivityAnalysis
+ _PLPickerGetLog
+ __NSConcreteGlobalBlock
+ ___stack_chk_fail
+ ___stack_chk_guard
+ __os_log_impl
+ _objc_retain_x21
+ _os_log_type_enabled
- _OBJC_CLASS_$_PXSharingUserSafetyController
CStrings:
+ "@\"PXSensitivityInterventionManager\""
+ "@\"UISceneWindowingControlStyle\"24@0:8@\"UIWindowScene\"16"
+ "B12@?0B8"
+ "Error prefetching sensitive content analysis policy: %@"
+ "No asset fetched for localIdentifier: %{public}@"
+ "Sensitive content analysis policy prefetch did not complete"
+ "T@\"PXSensitivityInterventionManager\",&,N,V_sensitivityInterventionManager"
+ "_beginDelayingPresentation:cancellationHandler:"
+ "_displayInterventionController"
+ "_endDelayingPresentation"
+ "_sensitivityInterventionManager"
+ "arrayWithObjects:count:"
+ "canPresentIntervention"
+ "fetchAssetsWithLocalIdentifiers:options:"
+ "firstObject"
+ "initWithAsset:interventionType:"
+ "localIdentifierWithUUID:"
+ "nonPreviewableAssetUUID"
+ "objectForKeyedSubscript:"
+ "preferredWindowingControlStyleForScene:"
+ "prefetchSensitiveContentPolicy:"
+ "presentFromViewController:completionHandler:"
+ "px_standardFetchOptions"
+ "sensitivityInterventionManager"
+ "setAllowsAlertStacking:"
+ "setSensitivityInterventionManager:"
+ "userInfo"
+ "v16@?0@\"NSError\"8"
+ "v32@0:8@\"UIWindowScene\"16@\"UIWindowSceneGeometry\"24"
+ "windowScene:didUpdateEffectiveGeometry:"
- "interventionViewControllerWithAction:"

```
