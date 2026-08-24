## FrontBoard

> `/System/Library/PrivateFrameworks/FrontBoard.framework/Versions/A/FrontBoard`

```diff

-1150.0.0.0.0
-  __TEXT.__text: 0x8211c
-  __TEXT.__objc_methlist: 0x54c8
+1153.0.0.0.0
+  __TEXT.__text: 0x8281c
+  __TEXT.__objc_methlist: 0x5488
   __TEXT.__const: 0x29c
-  __TEXT.__cstring: 0xa94d
+  __TEXT.__cstring: 0xab5b
   __TEXT.__oslogstring: 0x5d2e
   __TEXT.__gcc_except_tab: 0xaf4
   __TEXT.__dlopen_cstrs: 0x58

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6c8
-  __DATA_CONST.__objc_classlist: 0x2a0
+  __DATA_CONST.__const: 0x6d8
+  __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x248
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3490
+  __DATA_CONST.__objc_selrefs: 0x34a8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x210
+  __DATA_CONST.__objc_superrefs: 0x208
   __DATA_CONST.__objc_arraydata: 0x20
-  __DATA_CONST.__got: 0x898
+  __DATA_CONST.__got: 0x890
   __AUTH_CONST.__const: 0x2b90
-  __AUTH_CONST.__cfstring: 0x8900
-  __AUTH_CONST.__objc_const: 0xae88
+  __AUTH_CONST.__cfstring: 0x89e0
+  __AUTH_CONST.__objc_const: 0xae00
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x0

   __DATA.__objc_ivar: 0x8f4
   __DATA.__data: 0x1b60
   __DATA.__bss: 0xd0
-  __DATA_DIRTY.__objc_data: 0x1450
+  __DATA_DIRTY.__objc_data: 0x1400
   __DATA_DIRTY.__bss: 0x228
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3006
-  Symbols:   5901
-  CStrings:  1674
+  Functions: 3013
+  Symbols:   5896
+  CStrings:  1682
 
Symbols:
+ -[FBProcess allowsTerminatingOnWatchdogViolations]
+ -[FBWorkspaceDomain allowsTerminatingOnWatchdogViolations]
+ -[FBWorkspaceScene _workspaceQueue_createWatchdogForProcess:sceneAction:settings:transitionContext:]
+ GCC_except_table105
+ GCC_except_table12
+ GCC_except_table15
+ GCC_except_table4
+ GCC_except_table42
+ GCC_except_table90
+ GCC_except_table93
+ OBJC_IVAR_$_FBWorkspaceDomain._allowsTerminatingOnWatchdogViolations
+ OBJC_IVAR_$_FBWorkspaceScene._isUISubclass
+ OBJC_IVAR_$_FBWorkspaceScene._queue_allWatchdogs
+ OBJC_IVAR_$_FBWorkspaceScene._queue_watchdogStack
+ _NSStringFromFBSDefaultWatchdogBehavior
+ ___100-[FBWorkspaceScene _workspaceQueue_createWatchdogForProcess:sceneAction:settings:transitionContext:]_block_invoke
+ ___100-[FBWorkspaceScene _workspaceQueue_createWatchdogForProcess:sceneAction:settings:transitionContext:]_block_invoke_2
+ ___block_descriptor_56_e8_32s40s_e34_v16?0"<FBProcessBootstrapping>"8l
+ ___block_descriptor_93_e8_32s40s48s56s64s72s80bs_e46_v16?0"<FBSWorkspaceServiceServerInterface>"8l
+ _objc_msgSend$_workspaceQueue_createWatchdogForProcess:sceneAction:settings:transitionContext:
+ _objc_msgSend$allowsTerminatingOnWatchdogViolations
+ _objc_msgSend$defaultWatchdogBehavior
+ _objc_msgSend$removeObjectAtIndex:
- -[FBUIApplicationWorkspaceScene .cxx_destruct]
- -[FBUIApplicationWorkspaceScene _workspaceQueue_cancelWatchdogTimer:]
- -[FBUIApplicationWorkspaceScene _workspaceQueue_createWatchdogForProcess:sceneAction:transitionContext:]
- -[FBUIApplicationWorkspaceScene _workspaceQueue_invalidate]
- -[FBUIApplicationWorkspaceScene initWithConnection:host:settings:clientSettings:fromRemnant:]
- -[FBWorkspaceScene _workspaceQueue_createWatchdogForProcess:sceneAction:transitionContext:]
- GCC_except_table104
- GCC_except_table21
- GCC_except_table41
- GCC_except_table5
- GCC_except_table73
- GCC_except_table88
- GCC_except_table91
- OBJC_IVAR_$_FBUIApplicationWorkspaceScene._allWatchdogs
- OBJC_IVAR_$_FBUIApplicationWorkspaceScene._sentSceneCreate
- OBJC_IVAR_$_FBUIApplicationWorkspaceScene._watchdogStack
- OBJC_IVAR_$_FBWorkspaceScene._lock_sentSceneCreate
- _OBJC_CLASS_$_FBUIApplicationWorkspaceScene
- _OBJC_METACLASS_$_FBUIApplicationWorkspaceScene
- __OBJC_$_INSTANCE_METHODS_FBUIApplicationWorkspaceScene
- __OBJC_$_INSTANCE_VARIABLES_FBUIApplicationWorkspaceScene
- __OBJC_CLASS_RO_$_FBUIApplicationWorkspaceScene
- __OBJC_METACLASS_RO_$_FBUIApplicationWorkspaceScene
- ___104-[FBUIApplicationWorkspaceScene _workspaceQueue_createWatchdogForProcess:sceneAction:transitionContext:]_block_invoke
- ___104-[FBUIApplicationWorkspaceScene _workspaceQueue_createWatchdogForProcess:sceneAction:transitionContext:]_block_invoke_2
- ___block_descriptor_48_e8_32s40s_e34_v16?0"<FBProcessBootstrapping>"8l
- ___block_descriptor_85_e8_32s40s48s56s64s72bs_e46_v16?0"<FBSWorkspaceServiceServerInterface>"8l
- _objc_msgSend$_workspaceQueue_createWatchdogForProcess:sceneAction:transitionContext:
CStrings:
+ "AllowTerminatingOnWatchdogViolations"
+ "BOOL _shouldRunWatchdog(FBProcess *__strong, _FBSceneAction, FBSSceneSettings *__strong, BOOL, FBWatchdogTransitionContext *__strong)"
+ "Create Active"
+ "Create Inactive"
+ "already have a source registered for pid=%i: new=%@:%@ existing=%@:%@"
+ "attempting to add a process with a pid that is already tracked : new=<%p %@:%@> existing=<%p %@:%@>"
+ "attempting to add a process with a vpid that is already tracked : new=<%p %@:%@> existing=<%p %@:%@>"
+ "unknown sceneBehavior (%@) for action=%@ on %@"
+ "unknown transitionBehavior (%@) for action=%@ on %@"
- "already have a source registered for %@: %@"
```
