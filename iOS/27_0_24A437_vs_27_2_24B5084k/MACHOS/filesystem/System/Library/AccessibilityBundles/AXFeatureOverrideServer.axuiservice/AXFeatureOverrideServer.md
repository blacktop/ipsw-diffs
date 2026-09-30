## AXFeatureOverrideServer

> `/System/Library/AccessibilityBundles/AXFeatureOverrideServer.axuiservice/AXFeatureOverrideServer`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_types`

```diff

-3240.9.0.0.0
-  __TEXT.__text: 0x31b4
-  __TEXT.__auth_stubs: 0x5f0
-  __TEXT.__objc_stubs: 0xc0
-  __TEXT.__objc_methlist: 0x22c
-  __TEXT.__const: 0x342
-  __TEXT.__cstring: 0x122
-  __TEXT.__oslogstring: 0x172
-  __TEXT.__objc_methname: 0x723
-  __TEXT.__objc_classname: 0x2d
-  __TEXT.__objc_methtype: 0x315
-  __TEXT.__constg_swiftt: 0x120
-  __TEXT.__swift5_typeref: 0x117
-  __TEXT.__swift5_reflstr: 0x1a5
-  __TEXT.__swift5_fieldmd: 0xd8
-  __TEXT.__swift5_builtin: 0x28
+3245.7.1.0.0
+  __TEXT.__text: 0x5100
+  __TEXT.__auth_stubs: 0x710
+  __TEXT.__objc_stubs: 0x300
+  __TEXT.__objc_methlist: 0x298
+  __TEXT.__const: 0x460
+  __TEXT.__swift5_typeref: 0x27a
+  __TEXT.__swift5_capture: 0x78
+  __TEXT.__objc_methtype: 0x4a5
+  __TEXT.__objc_methname: 0x923
+  __TEXT.__swift5_fieldmd: 0x1a4
+  __TEXT.__constg_swiftt: 0x1c0
+  __TEXT.__objc_classname: 0xca
+  __TEXT.__swift5_reflstr: 0x205
+  __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_assocty: 0x60
-  __TEXT.__swift5_capture: 0x10
-  __TEXT.__swift5_proto: 0x14
+  __TEXT.__cstring: 0x122
+  __TEXT.__oslogstring: 0x256
+  __TEXT.__swift5_protos: 0xc
+  __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0x18
-  __TEXT.__unwind_info: 0x168
-  __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__const: 0x218
-  __DATA_CONST.__objc_classlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x20
+  __TEXT.__unwind_info: 0x208
+  __TEXT.__eh_frame: 0x60
+  __DATA_CONST.__const: 0x418
+  __DATA_CONST.__objc_classlist: 0x18
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__auth_got: 0x300
-  __DATA_CONST.__got: 0x70
-  __DATA_CONST.__auth_ptr: 0x148
-  __DATA.__objc_const: 0x368
-  __DATA.__objc_selrefs: 0x158
-  __DATA.__objc_data: 0x110
-  __DATA.__data: 0x1b0
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__auth_got: 0x390
+  __DATA_CONST.__got: 0xa8
+  __DATA_CONST.__auth_ptr: 0x178
+  __DATA.__objc_const: 0x5a8
+  __DATA.__objc_selrefs: 0x1f0
+  __DATA.__objc_data: 0x140
+  __DATA.__data: 0x380
   __DATA.__common: 0x18
   - /System/Library/Frameworks/Accessibility.framework/Accessibility
-  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities
   - /System/Library/PrivateFrameworks/AccessibilityUIService.framework/AccessibilityUIService
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
+  - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 91
-  Symbols:   107
-  CStrings:  112
+  Functions: 142
+  Symbols:   128
+  CStrings:  154
 
Symbols:
+ _OBJC_CLASS_$_RBSProcessEndowmentInfo
+ _OBJC_CLASS_$_RBSProcessMonitor
+ _OBJC_CLASS_$_RBSProcessPredicate
+ _OBJC_CLASS_$_RBSProcessStateDescriptor
+ _OBJC_CLASS_$_RBSTarget
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ _RBSTaskStateIsRunning
+ _objc_release_x22
+ _objc_release_x26
+ _objc_retain_x22
+ _swift_deallocClassInstance
+ _swift_deletedMethodError
+ _swift_isEscapingClosureAtFileLocation
+ _swift_release_n
+ _swift_release_x19
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x8
+ _swift_retain_x19
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x24
+ _swift_unknownObjectRelease
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
- _CFNotificationCenterAddObserver
- _CFNotificationCenterGetDarwinNotifyCenter
- _objc_release_x25
- _objc_release_x27
- _objc_release_x9
- _objc_retain_x8
- _swift_release_x27
CStrings:
+ "@52@0:8@16q24@32i40^@44"
+ "No owner pid available; override lifecycle will rely on the session timer only"
+ "Owner backgrounded; suspending override session [%s]"
+ "Owner foregrounded; reinstating override session [%s]"
+ "Owner process terminated; tearing down override session [%s]"
+ "Owning client connection interrupted; tearing down override session"
+ "RBSProcessMonitorConfiguring"
+ "_TtC23AXFeatureOverrideServer23RBSOverrideOwnerMonitor"
+ "_TtC23AXFeatureOverrideServer26AXAccessQueueOverrideTimer"
+ "com.apple.frontboard.visibility"
+ "currentState"
+ "endowmentInfos"
+ "endowmentNamespace"
+ "endowmentNamespaces"
+ "featureProvider"
+ "invalidate"
+ "isSuspended"
+ "monitor"
+ "monitorWithConfiguration:"
+ "ownerClientIdentifier"
+ "ownerMonitor"
+ "ownerMonitorFactory"
+ "ownerPID"
+ "performAsynchronousWritingBlock:"
+ "predicateMatchingTarget:"
+ "setEndowmentNamespaces:"
+ "setEvents:"
+ "setPredicates:"
+ "setPreventLaunchUpdateHandle:"
+ "setServiceClass:"
+ "setStateDescriptor:"
+ "setUpdateHandler:"
+ "setValues:"
+ "state"
+ "targetWithPid:"
+ "taskState"
+ "timer"
+ "timerFactory"
+ "v16@?0@\"<RBSProcessMonitorConfiguring>\"8"
+ "v20@0:8I16"
+ "v24@0:8@\"NSArray\"16"
+ "v24@0:8@\"RBSProcessStateDescriptor\"16"
+ "v24@0:8@?16"
+ "v24@0:8@?<v@?@\"RBSProcessMonitor\"@\"NSSet\">16"
+ "v24@0:8@?<v@?@\"RBSProcessMonitor\"@\"RBSProcessHandle\"@\"RBSProcessStateUpdate\">16"
+ "v24@0:8Q16"
+ "v32@?0@\"RBSProcessMonitor\"8@\"RBSProcessHandle\"16@\"RBSProcessStateUpdate\"24"
- "Observed application state change"
- "Reverting to prior feature enablement and removing active overrides"
- "SBSubstantialTransitionNotification"
- "applicationStateChanged"
- "com.apple.mobile.SubstantialTransition"
```
