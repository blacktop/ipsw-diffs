## FrontBoard

> `/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`

```diff

-1000.0.1.0.0
-  __TEXT.__text: 0x8d828
+1000.1.4.0.0
+  __TEXT.__text: 0x8cd44
   __TEXT.__auth_stubs: 0xfd0
-  __TEXT.__objc_methlist: 0x5b28
+  __TEXT.__objc_methlist: 0x5b38
   __TEXT.__const: 0x324
-  __TEXT.__cstring: 0xb484
-  __TEXT.__oslogstring: 0x5f90
+  __TEXT.__cstring: 0xb23c
+  __TEXT.__oslogstring: 0x5ec2
   __TEXT.__gcc_except_tab: 0x18c8
   __TEXT.__dlopen_cstrs: 0x20a
-  __TEXT.__unwind_info: 0x21e0
-  __TEXT.__objc_classname: 0x11d0
-  __TEXT.__objc_methname: 0xf90d
+  __TEXT.__unwind_info: 0x21f8
+  __TEXT.__objc_classname: 0x11cf
+  __TEXT.__objc_methname: 0xf78b
   __TEXT.__objc_methtype: 0x3847
-  __TEXT.__objc_stubs: 0xb140
-  __DATA_CONST.__got: 0x900
+  __TEXT.__objc_stubs: 0xb100
+  __DATA_CONST.__got: 0x8f8
   __DATA_CONST.__const: 0x2728
   __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x37b0
+  __DATA_CONST.__objc_selrefs: 0x37a8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x238
   __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__auth_got: 0x7f8
-  __AUTH_CONST.__const: 0x840
-  __AUTH_CONST.__cfstring: 0x9160
-  __AUTH_CONST.__objc_const: 0xbb60
+  __AUTH_CONST.__const: 0x860
+  __AUTH_CONST.__cfstring: 0x8e20
+  __AUTH_CONST.__objc_const: 0xb900
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0xcd0
-  __DATA.__objc_ivar: 0x9b0
+  __DATA.__objc_ivar: 0x964
   __DATA.__data: 0x1d40
   __DATA.__bss: 0x1f8
   __DATA_DIRTY.__objc_data: 0xeb0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ED43ADA7-7107-3242-928F-09708F2FD9F3
-  Functions: 3048
-  Symbols:   10533
-  CStrings:  6114
+  UUID: 7BF318BD-7A2D-3E56-AE0E-2DA81A078EE0
+  Functions: 3051
+  Symbols:   10520
+  CStrings:  6040
 
Symbols:
+ +[FBWorkspaceAssertionAttributes sharedAttributes].cold.1
+ +[FBWorkspaceDomain backgroundUserInitiatedBootstrapAttributes]
+ -[FBScene _setContentState:notifyObservers:]
+ -[FBScene _setContentState:notifyObservers:].cold.1
+ -[FBScene _setContentState:notifyObservers:].cold.2
+ -[FBScene _setContentState:notifyObservers:].cold.3
+ GCC_except_table161
+ GCC_except_table163
+ ___44-[FBScene _setContentState:notifyObservers:]_block_invoke
+ ___block_literal_global.303
- -[FBScene _setContentState:]
- -[FBScene _setContentState:].cold.1
- -[FBScene _setContentState:].cold.2
- GCC_except_table157
- GCC_except_table162
- _OBJC_CLASS_$_RBSAcquisitionCompletionAttribute
- _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._UIAttributes
- _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._activeAttributes
- _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._bgActiveAttributes
- _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._bgLaunchAttributes
- _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._bgUserInitiatedAttributes
- _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._bgUtilityAttributes
- _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._fgFocalAttributes
- _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._fgLaunchAttributes
- _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._fgNonFocalAttributes
- _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._fgSupportLaunchAttributes
- _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._fgSuspendedAttributes
- _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._fgUtilityAttributes
- _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._focalAttributes
- _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._interactiveAttributes
- _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._nonUIAttributes
- _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._opportunisticAttributes
- _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._usesLegacyAssertions
- _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._utLaunchAttributes
- _OBJC_IVAR_$_FBWorkspaceAssertionAttributes._utilityAttributes
- ___28-[FBScene _setContentState:]_block_invoke
- _objc_msgSend$arrayWithCapacity:
- _objc_msgSend$attributeWithCompletionPolicy:
CStrings:
+ "_setContentState:notifyObservers:"
+ "backgroundUserInitiatedBootstrapAttributes"
- "Bootstrap-Background"
- "Bootstrap-BackgroundUserInitiated"
- "Bootstrap-Foreground"
- "Bootstrap-ForegroundSupport"
- "Bootstrap-Utility"
- "FBWorkspaceAssertionAttributes:%p using legacy assertions because we found 'Workspace-Test'."
- "FBWorkspaceAssertionAttributes:%p using v2 assertions because we failed acquiring 'Workspace-Test' with error=%@"
- "Has 'Workspace-Test' been removed indicating support for composableV2 assertions?"
- "Jetsam-Active"
- "Jetsam-Background"
- "Jetsam-FGSupport"
- "Jetsam-Focal"
- "Jetsam-Foreground"
- "Jetsam-Opportunistic"
- "Jetsam-UISupport"
- "Jetsam-Utility"
- "Jetsam-Utility2"
- "Jetsam-Utility3"
- "Workspace-Active"
- "Workspace-BackgroundActive-NoSuspend"
- "Workspace-Focal"
- "Workspace-ForegroundActive-NoSuspend"
- "Workspace-Interactive"
- "Workspace-NonUI"
- "Workspace-Opportunistic"
- "Workspace-Test"
- "Workspace-UI"
- "Workspace-Utility"
- "_UIAttributes"
- "_activeAttributes"
- "_bgActiveAttributes"
- "_bgLaunchAttributes"
- "_bgUserInitiatedAttributes"
- "_bgUtilityAttributes"
- "_fgFocalAttributes"
- "_fgLaunchAttributes"
- "_fgNonFocalAttributes"
- "_fgSupportLaunchAttributes"
- "_fgSuspendedAttributes"
- "_fgUtilityAttributes"
- "_focalAttributes"
- "_interactiveAttributes"
- "_nonUIAttributes"
- "_opportunisticAttributes"
- "_setContentState:"
- "_usesLegacyAssertions"
- "_utLaunchAttributes"
- "_utilityAttributes"
- "arrayWithCapacity:"
- "attributeWithCompletionPolicy:"

```
