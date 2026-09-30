## GuidedAccess

> `/System/Library/AccessibilityBundles/GuidedAccess.axuiservice/GuidedAccess`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1061.0.0.0.0
-  __TEXT.__text: 0x2f1b0
+1064.0.0.0.0
+  __TEXT.__text: 0x2f6fc
   __TEXT.__auth_stubs: 0xc60
-  __TEXT.__objc_stubs: 0x8e20
-  __TEXT.__objc_methlist: 0x36bc
-  __TEXT.__const: 0x1a0
+  __TEXT.__objc_stubs: 0x8ee0
+  __TEXT.__objc_methlist: 0x36cc
+  __TEXT.__const: 0x1b0
   __TEXT.__objc_classname: 0x75f
   __TEXT.__constg_swiftt: 0x50
   __TEXT.__swift5_typeref: 0x6
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
   __TEXT.__gcc_except_tab: 0x974
-  __TEXT.__objc_methname: 0xc4fc
-  __TEXT.__cstring: 0x3e06
-  __TEXT.__oslogstring: 0xec3
-  __TEXT.__objc_methtype: 0x24ee
+  __TEXT.__oslogstring: 0x1244
+  __TEXT.__objc_methname: 0xc5f6
+  __TEXT.__cstring: 0x3e48
+  __TEXT.__objc_methtype: 0x24f1
   __TEXT.__unwind_info: 0xd50
-  __DATA_CONST.__const: 0x1b08
-  __DATA_CONST.__cfstring: 0x29e0
+  __DATA_CONST.__const: 0x1b38
+  __DATA_CONST.__cfstring: 0x2a00
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xc8

   __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__objc_doubleobj: 0x50
   __DATA_CONST.__auth_got: 0x640
-  __DATA_CONST.__got: 0x4f0
+  __DATA_CONST.__got: 0x520
   __DATA.__objc_const: 0x47b8
-  __DATA.__objc_selrefs: 0x2a68
+  __DATA.__objc_selrefs: 0x2a98
   __DATA.__objc_ivar: 0x264
   __DATA.__objc_data: 0xc80
   __DATA.__data: 0xa08

   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/AACCore.framework/AACCore
   - /System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities
   - /System/Library/PrivateFrameworks/AXFrontBoardUtils.framework/AXFrontBoardUtils
   - /System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1176
-  Symbols:   662
-  CStrings:  2553
+  Functions: 1178
+  Symbols:   669
+  CStrings:  2569
 
Symbols:
+ _GAXUIMessageKeyShouldDriveSiriAssessmentRestriction
+ _MCFeatureControlCenterAllowed
+ _MCFeatureEmojiKeyboardAllowed
+ _MCFeatureKeyboardPeriodShortcutAllowed
+ _MCFeatureLiveVoicemailAllowed
+ _OBJC_CLASS_$_AEAssessmentModeRestrictionEnforcerProxy
+ _OBJC_CLASS_$_NSThread
CStrings:
+ "GAXUIServer dealloc starting (this is not expected to happen while the service is registered with AXUIServer, since GAXUIServer has no way to remove its scene for identifier %@ outside of this teardown path)"
+ "GAXUIServer init starting. Caller: %@"
+ "Received CompleteHidingWorkspaceAndEnterSession, clearing activeContentViewController %@. Note: this only removes the content view controller, it does not release the scene requested for identifier %@."
+ "Received CompleteHidingWorkspaceAndReturnToApplication, clearing activeContentViewController %@. Note: this only removes the content view controller, it does not release the scene requested for identifier %@."
+ "Siri assessment-mode restriction %{public}s failed: %{public}@"
+ "Siri assessment-mode restriction %{public}s succeeded"
+ "Unmanaged ASAM restriction state changed: enabled=%d shouldDriveSiri=%d"
+ "_changeUnmanagedASAMRestrictionStateEnabled:style:managedConfigurationSettings:shouldDriveSiriAssessmentRestriction:"
+ "_driveSiriAssessmentModeRestriction:"
+ "activeContentViewController changing from %@ to %@"
+ "callStackSymbols"
+ "com.apple.siri.assessment-mode-restriction"
+ "end"
+ "initWithMachServiceName:queue:"
+ "safeAreaLayoutGuide"
+ "should drive siri assessment restriction"
+ "shouldBeginRestrictingForAssessmentModeWithCompletion:"
+ "shouldEndRestrictingForAssessmentModeWithCompletion:"
+ "v40@0:8B16q20@28B36"
- "_changeUnmanagedASAMRestrictionStateEnabled:style:managedConfigurationSettings:"
- "allowKeyboardPeriodShortcut"
- "v36@0:8B16q20@28"
```
