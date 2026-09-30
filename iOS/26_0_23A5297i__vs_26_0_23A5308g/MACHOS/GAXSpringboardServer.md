## GAXSpringboardServer

> `/System/Library/AccessibilityBundles/GAXSpringboardServer.bundle/GAXSpringboardServer`

```diff

-1023.0.0.0.0
-  __TEXT.__text: 0x14914
-  __TEXT.__auth_stubs: 0x680
-  __TEXT.__objc_stubs: 0x2a40
-  __TEXT.__objc_methlist: 0x1db4
-  __TEXT.__const: 0xa0
-  __TEXT.__gcc_except_tab: 0x540
-  __TEXT.__cstring: 0x4e35
-  __TEXT.__objc_methname: 0x536a
-  __TEXT.__oslogstring: 0x1180
-  __TEXT.__objc_classname: 0xdcd
+1025.0.0.0.0
+  __TEXT.__text: 0x14fdc
+  __TEXT.__auth_stubs: 0x6c0
+  __TEXT.__objc_stubs: 0x2ba0
+  __TEXT.__objc_methlist: 0x1e74
+  __TEXT.__const: 0xa8
+  __TEXT.__gcc_except_tab: 0x55c
+  __TEXT.__cstring: 0x4f81
+  __TEXT.__objc_methname: 0x54df
+  __TEXT.__oslogstring: 0x1381
+  __TEXT.__objc_classname: 0xe23
   __TEXT.__objc_methtype: 0xeb7
   __TEXT.__dlopen_cstrs: 0xaa
-  __TEXT.__unwind_info: 0x6d8
-  __DATA_CONST.__auth_got: 0x350
-  __DATA_CONST.__got: 0x228
-  __DATA_CONST.__const: 0x1088
-  __DATA_CONST.__cfstring: 0x48e0
-  __DATA_CONST.__objc_classlist: 0x2d8
+  __TEXT.__unwind_info: 0x6f0
+  __DATA_CONST.__auth_got: 0x370
+  __DATA_CONST.__got: 0x230
+  __DATA_CONST.__const: 0x10a0
+  __DATA_CONST.__cfstring: 0x4a80
+  __DATA_CONST.__objc_classlist: 0x2e8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x168
+  __DATA_CONST.__objc_superrefs: 0x170
   __DATA_CONST.__objc_arraydata: 0xa0
   __DATA_CONST.__objc_arrayobj: 0x1b0
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__objc_doubleobj: 0x20
+  __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x3e50
-  __DATA.__objc_selrefs: 0x1320
+  __DATA.__objc_const: 0x3f78
+  __DATA.__objc_selrefs: 0x13a0
   __DATA.__objc_ivar: 0x4c
-  __DATA.__objc_data: 0x1c70
+  __DATA.__objc_data: 0x1d10
   __DATA.__data: 0x188
   __DATA.__bss: 0x72
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities
+  - /System/Library/PrivateFrameworks/AXGuestPassServices.framework/AXGuestPassServices
   - /System/Library/PrivateFrameworks/AXSpringBoardServerInstance.framework/AXSpringBoardServerInstance
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /System/Library/PrivateFrameworks/BaseBoardUI.framework/BaseBoardUI

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3EF7865A-20F8-3F16-A119-7EFBCA7BB37B
-  Functions: 543
-  Symbols:   541
-  CStrings:  2186
+  UUID: 7722A54D-0678-3BC7-B6E5-B89C1663D22A
+  Functions: 558
+  Symbols:   550
+  CStrings:  2238
 
Symbols:
+ _AXGuestPassManager
+ _OBJC_CLASS_$_GAXSBIdleTimerPolicyAggregatorOverride
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_CLASS_$___GAXSBIdleTimerPolicyAggregatorOverride_super
+ _OBJC_METACLASS_$_GAXSBIdleTimerPolicyAggregatorOverride
+ _OBJC_METACLASS_$___GAXSBIdleTimerPolicyAggregatorOverride_super
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
- _objc_retain_x25
CStrings:
+ "ACActivityDescriptor"
+ "Error fetching AXGuestPassManager"
+ "GAXSBChamoisWindowingPreviouslyEnabled"
+ "GAXSBIdleTimerPolicyAggregatorOverride"
+ "GAXSBMedusaMultitaskingPreviouslyEnabled"
+ "Gudied Access is refreshing idle timers because Guest Pass changed to: %@"
+ "Guest Pass expired in Single App Mode. Success: %d, error: %@"
+ "Guided Access detected active Guest Pass session - will automatically release after inactivity."
+ "Guided Access is preventing warn/dim during active Guest Pass"
+ "Reinstating multitasking since Guided Access is ending and we found that multitasking was previously enabled"
+ "SBActivityItem"
+ "SBChamoisWindowingEnabled"
+ "SBIdleTimerPolicyAggregator"
+ "SBMedusaMultitaskingEnabled"
+ "Turning off multitasking, enforcing Full Screen Apps mode for Guided Access"
+ "__GAXSBIdleTimerPolicyAggregatorOverride_super"
+ "active"
+ "boolForKey:"
+ "com.apple.NetworkEndpointPickerUI"
+ "currentMultitaskingMode"
+ "descriptor"
+ "endGuestPassSessionWithCompletionBlock:"
+ "guestPassSessionIsActive"
+ "handleGuestPassSessionChanged:"
+ "idleTimerDidExpire:"
+ "idleTimerDidWarn:"
+ "inactive"
+ "isChamoisOrFlexibleWindowingEnabledWithServerInstance:"
+ "localizedDescription"
+ "platterTargetBundleIdentifier"
+ "previouslyEnabledStageManager"
+ "previouslyEnabledWindowedApps"
+ "registerUpdateBlock:forRetrieveSelector:withListener:"
+ "setBool:forKey:"
+ "setCurrentMultitaskingMode:"
+ "setPreviouslyEnabledStageManager:"
+ "setPreviouslyEnabledWindowedApps:"
+ "setupGuestPassSessionMonitoring"
+ "springBoardDefaults"
+ "standardUserDefaults"
+ "v20@?0B8@\"NSError\"12"
- "guidedAccessUserPrefersMirroringForExternalDisplays"
- "localDefaults.externalDisplayDefaults"
- "mirroringEnabled"
- "setGuidedAccessUserPrefersMirroringForExternalDisplays:"

```
