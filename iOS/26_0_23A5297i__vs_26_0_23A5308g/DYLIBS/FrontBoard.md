## FrontBoard

> `/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`

```diff

-998.0.0.0.0
-  __TEXT.__text: 0x8c9bc
+1000.0.0.0.0
+  __TEXT.__text: 0x8d784
   __TEXT.__auth_stubs: 0xfd0
   __TEXT.__objc_methlist: 0x5b10
-  __TEXT.__const: 0x314
-  __TEXT.__cstring: 0xb0e4
-  __TEXT.__oslogstring: 0x5ea4
+  __TEXT.__const: 0x324
+  __TEXT.__cstring: 0xb484
+  __TEXT.__oslogstring: 0x5f72
   __TEXT.__gcc_except_tab: 0x18c8
   __TEXT.__dlopen_cstrs: 0x20a
-  __TEXT.__unwind_info: 0x21e0
-  __TEXT.__objc_classname: 0x11cf
-  __TEXT.__objc_methname: 0xf5e6
+  __TEXT.__unwind_info: 0x21e8
+  __TEXT.__objc_classname: 0x11d0
+  __TEXT.__objc_methname: 0xf8d9
   __TEXT.__objc_methtype: 0x3847
-  __TEXT.__objc_stubs: 0xb100
+  __TEXT.__objc_stubs: 0xb120
   __DATA_CONST.__got: 0x900
-  __DATA_CONST.__const: 0x2708
+  __DATA_CONST.__const: 0x2728
   __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3780
+  __DATA_CONST.__objc_selrefs: 0x37a0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x238
   __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__auth_got: 0x7f8
-  __AUTH_CONST.__const: 0x880
-  __AUTH_CONST.__cfstring: 0x8dc0
-  __AUTH_CONST.__objc_const: 0xb820
+  __AUTH_CONST.__const: 0x840
+  __AUTH_CONST.__cfstring: 0x9160
+  __AUTH_CONST.__objc_const: 0xbb20
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0xcd0
-  __DATA.__objc_ivar: 0x94c
+  __DATA.__objc_ivar: 0x9ac
   __DATA.__data: 0x1d40
-  __DATA.__bss: 0x210
+  __DATA.__bss: 0x1f8
   __DATA_DIRTY.__objc_data: 0xeb0
-  __DATA_DIRTY.__bss: 0x1a0
+  __DATA_DIRTY.__bss: 0x1a8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 525BB3C7-3C77-3ED0-819C-4946A6FF4654
+  UUID: A15B55CA-167E-3546-98D6-C52F3E7CE3CC
   Functions: 3046
-  Symbols:   10512
-  CStrings:  6022
+  Symbols:   10527
+  CStrings:  6109
 
Symbols:
+ +[FBWorkspaceAssertionAttributes sharedAttributes]
+ -[FBWorkspaceAssertionAttributes assertionAttributesForLaunchIntent:assertsVisibility:outWorkspaceState:outProcessVisibility:]
+ -[FBWorkspaceAssertionAttributes assertionAttributesForLaunchIntent:assertsVisibility:outWorkspaceState:outProcessVisibility:].cold.1
+ -[FBWorkspaceAssertionAttributes assertionAttributesForLaunchIntent:assertsVisibility:outWorkspaceState:outProcessVisibility:].cold.2
+ -[FBWorkspaceAssertionAttributes assertionAttributesForWorkspaceState:assertsVisibility:isBootstrapping:]
+ -[FBWorkspaceAssertionAttributes assertionAttributesForWorkspaceState:assertsVisibility:isBootstrapping:].cold.1
+ -[FBWorkspaceAssertionAttributes selfAssertionAttributesWithForeground:outWorkspaceState:]
+ -[FBWorkspaceAssertionAttributes selfAssertionAttributesWithForeground:outWorkspaceState:].cold.1
+ -[FBWorkspaceAssertionAttributes selfAssertionAttributesWithForeground:outWorkspaceState:].cold.2
+ -[FBWorkspaceDomain assertionAttributesForLaunchIntent:outWorkspaceState:outProcessVisibility:]
+ _FBWorkspaceActivityIsValid
+ _FBWorkspaceStateGetActivity
+ _NSStringFromFBWorkspaceActivity
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._activityLimitActiveUI
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._activityLimitPreserveNonUI
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._activityRunReasonResume
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._activityRunReasonSuspend
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._bootstrap
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._fixedMinute
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._jetsamPriorityActive
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._jetsamPriorityBackground
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._jetsamPriorityForeground
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._jetsamPriorityForegroundFocal
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._jetsamPriorityForegroundSupport
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._jetsamPriorityOpportunistic
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._jetsamPriorityUISupport
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._jetsamPriorityUtility
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._jetsamPriorityUtility2
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._jetsamPriorityUtility3
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._maintainSelfForBGHosting
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._maintainSelfForFGHosting
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._roleNonUI
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._roleOpportunistic
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._roleUIFocal
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._roleUINonFocal
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._roleUtility
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._usesLegacyAssertions
+ _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._visibility
+ ___50+[FBWorkspaceAssertionAttributes sharedAttributes]_block_invoke
+ ___54-[FBWorkspaceDomain endpointInjectorTargetingProcess:]_block_invoke.109
+ ___54-[FBWorkspaceScene workspace:sendActions:toExtension:]_block_invoke.121
+ ___54-[FBWorkspaceScene workspace:sendActions:toExtension:]_block_invoke_2.122
+ ___63-[FBWorkspaceDomain listener:didReceiveConnection:withContext:]_block_invoke.171
+ ___79-[FBWorkspaceScene workspace:sendInvalidationWithTransitionContext:completion:]_block_invoke.115
+ ___88-[FBWorkspaceScene workspace:sendUpdatedSettings:withDiff:transitionContext:completion:]_block_invoke.102
+ ___88-[FBWorkspaceScene workspace:sendUpdatedSettings:withDiff:transitionContext:completion:]_block_invoke.108
+ ___88-[FBWorkspaceScene workspace:sendUpdatedSettings:withDiff:transitionContext:completion:]_block_invoke_2.104
+ _objc_msgSend$arrayWithCapacity:
+ _sharedAttributes.attrs
+ _sharedAttributes.onceToken
- +[FBWorkspaceAssertionAttributes assertsVisibilityAttributes]
- +[FBWorkspaceAssertionAttributes assertsVisibilityAttributes].cold.1
- +[FBWorkspaceAssertionAttributes attributeForJetsamBand:]
- +[FBWorkspaceAssertionAttributes baseAttributes]
- +[FBWorkspaceAssertionAttributes baseAttributes].cold.1
- -[FBWorkspaceAssertionAttributes assertionAttributesForLaunchIntent:]
- -[FBWorkspaceAssertionAttributes assertionAttributesForWorkspaceState:]
- -[FBWorkspaceAssertionAttributes injectorAttributes]
- -[FBWorkspaceDomain _assertionAttrs]
- -[FBWorkspaceDomain assertionAttributesForLaunchIntent:]
- -[FBWorkspaceScene _workspaceQueue_updateAssertion].cold.1
- _FBWorkspaceStateGetVisibility
- _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._visibilityAttribute
- ___48+[FBWorkspaceAssertionAttributes baseAttributes]_block_invoke
- ___54-[FBWorkspaceDomain endpointInjectorTargetingProcess:]_block_invoke.108
- ___54-[FBWorkspaceScene workspace:sendActions:toExtension:]_block_invoke.124
- ___54-[FBWorkspaceScene workspace:sendActions:toExtension:]_block_invoke_2.125
- ___61+[FBWorkspaceAssertionAttributes assertsVisibilityAttributes]_block_invoke
- ___63-[FBWorkspaceDomain listener:didReceiveConnection:withContext:]_block_invoke.177
- ___79-[FBWorkspaceScene workspace:sendInvalidationWithTransitionContext:completion:]_block_invoke.118
- ___88-[FBWorkspaceScene workspace:sendUpdatedSettings:withDiff:transitionContext:completion:]_block_invoke.105
- ___88-[FBWorkspaceScene workspace:sendUpdatedSettings:withDiff:transitionContext:completion:]_block_invoke.111
- ___88-[FBWorkspaceScene workspace:sendUpdatedSettings:withDiff:transitionContext:completion:]_block_invoke_2.107
- ___block_literal_global.338
- ___block_literal_global.381
- _assertsVisibilityAttributes.attrs
- _assertsVisibilityAttributes.onceToken
- _baseAttributes.attrs
- _baseAttributes.onceToken
CStrings:
+ "Duration-Fixed-60-1-Invalidate"
+ "FBWorkspaceAssertionAttributes:%p using legacy assertions because we found 'Workspace-Test'."
+ "FBWorkspaceAssertionAttributes:%p using v2 assertions because we failed acquiring 'Workspace-Test' with error=%@"
+ "FV"
+ "Has 'Workspace-Test' been removed indicating support for composableV2 assertions?"
+ "MaintainSelfForBGHosting"
+ "MaintainSelfForFGHosting"
+ "SuspendableBootstrapping"
+ "SuspendableJetsamLimit-ActiveUI"
+ "SuspendableJetsamLimit-PreserveNonUI"
+ "SuspendableJetsamPriority-Active"
+ "SuspendableJetsamPriority-Background"
+ "SuspendableJetsamPriority-Foreground"
+ "SuspendableJetsamPriority-ForegroundFocal"
+ "SuspendableJetsamPriority-ForegroundSupport"
+ "SuspendableJetsamPriority-Opportunistic"
+ "SuspendableJetsamPriority-UISupport"
+ "SuspendableJetsamPriority-Utility"
+ "SuspendableJetsamPriority-Utility2"
+ "SuspendableJetsamPriority-Utility3"
+ "SuspendableLPRunReason-Resume"
+ "SuspendableLPRunReason-Suspend"
+ "SuspendableRole-NonUI"
+ "SuspendableRole-Opportunistic"
+ "SuspendableRole-UIFocal"
+ "SuspendableRole-UINonFocal"
+ "SuspendableRole-Utility"
+ "Workspace-Test"
+ "XX"
+ "_activityLimitActiveUI"
+ "_activityLimitPreserveNonUI"
+ "_activityRunReasonResume"
+ "_activityRunReasonSuspend"
+ "_bootstrap"
+ "_fixedMinute"
+ "_jetsamPriorityActive"
+ "_jetsamPriorityBackground"
+ "_jetsamPriorityForeground"
+ "_jetsamPriorityForegroundFocal"
+ "_jetsamPriorityForegroundSupport"
+ "_jetsamPriorityOpportunistic"
+ "_jetsamPriorityUISupport"
+ "_jetsamPriorityUtility"
+ "_jetsamPriorityUtility2"
+ "_jetsamPriorityUtility3"
+ "_maintainSelfForBGHosting"
+ "_maintainSelfForFGHosting"
+ "_roleNonUI"
+ "_roleOpportunistic"
+ "_roleUIFocal"
+ "_roleUINonFocal"
+ "_roleUtility"
+ "_usesLegacyAssertions"
+ "arrayWithCapacity:"
+ "assertionAttributesForLaunchIntent:assertsVisibility:outWorkspaceState:outProcessVisibility:"
+ "assertionAttributesForWorkspaceState:assertsVisibility:isBootstrapping:"
+ "outProcessVisibility != ((void *)0)"
+ "outWorkspaceState != ((void *)0)"
+ "requesting assertions for invalid state %@"
+ "selfAssertionAttributesWithForeground:outWorkspaceState:"
- "_visibilityAttribute"
- "bogus jetsam offset %u"

```
