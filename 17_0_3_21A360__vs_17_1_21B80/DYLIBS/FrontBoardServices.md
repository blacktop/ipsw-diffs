## FrontBoardServices

> `/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`

```diff

-867.3.1.0.0
-  __TEXT.__text: 0x8c1f8
-  __TEXT.__auth_stubs: 0x1080
-  __TEXT.__objc_methlist: 0x65dc
+867.8.2.0.0
+  __TEXT.__text: 0x8d1fc
+  __TEXT.__auth_stubs: 0x10a0
+  __TEXT.__objc_methlist: 0x681c
   __TEXT.__const: 0x168
-  __TEXT.__cstring: 0xa840
-  __TEXT.__oslogstring: 0x2d28
+  __TEXT.__cstring: 0xa8be
+  __TEXT.__oslogstring: 0x2d67
   __TEXT.__gcc_except_tab: 0x1264
-  __TEXT.__unwind_info: 0x25d8
-  __TEXT.__objc_classname: 0x1200
-  __TEXT.__objc_methname: 0xe7c7
-  __TEXT.__objc_methtype: 0x30d2
-  __TEXT.__objc_stubs: 0x9900
-  __DATA_CONST.__got: 0x108
-  __DATA_CONST.__const: 0x2c48
-  __DATA_CONST.__objc_classlist: 0x438
+  __TEXT.__unwind_info: 0x2674
+  __TEXT.__objc_classname: 0x121e
+  __TEXT.__objc_methname: 0xe7c1
+  __TEXT.__objc_methtype: 0x30ce
+  __TEXT.__objc_stubs: 0x9920
+  __DATA_CONST.__got: 0x118
+  __DATA_CONST.__const: 0x2c50
+  __DATA_CONST.__objc_classlist: 0x440
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x1d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1a920
-  __DATA_CONST.__objc_selrefs: 0x33a0
+  __DATA_CONST.__objc_const: 0x1aad0
+  __DATA_CONST.__objc_selrefs: 0x3478
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__cfstring: 0x8500
+  __AUTH_CONST.__cfstring: 0x8580
   __AUTH_CONST.__objc_const: 0x36f0
-  __AUTH_CONST.__const: 0x620
+  __AUTH_CONST.__const: 0x660
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_got: 0x850
-  __AUTH.__objc_data: 0xf00
+  __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH_CONST.__auth_got: 0x860
+  __AUTH.__objc_data: 0xf50
   __DATA.__objc_protorefs: 0x68
-  __DATA.__objc_classrefs: 0x5a0
-  __DATA.__objc_superrefs: 0x2f0
-  __DATA.__objc_ivar: 0x994
-  __DATA.__data: 0x17d0
-  __DATA.__bss: 0x1b8
+  __DATA.__objc_classrefs: 0x5a8
+  __DATA.__objc_superrefs: 0x300
+  __DATA.__objc_ivar: 0x97c
+  __DATA.__data: 0x17d8
+  __DATA.__bss: 0x1c8
   __DATA_DIRTY.__objc_data: 0x1b30
   __DATA_DIRTY.__bss: 0x120
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0F222382-24F8-33BC-AD5F-B2C750D6008D
-  Functions: 3820
-  Symbols:   12387
-  CStrings:  5946
+  UUID: 53361056-035F-3739-9565-8DC51796B102
+  Functions: 3873
+  Symbols:   12509
+  CStrings:  5959
 
Symbols:
+ +[FBSSceneTransitionContextCore protocol]
+ -[FBSApplicationDataStore setObject:forKey:].cold.2
+ -[FBSApplicationLibrary _synchronizationQueue]
+ -[FBSSceneClientSettingsCore preferredInterfaceOrientation]
+ -[FBSSceneClientSettingsCore preferredLevel]
+ -[FBSSceneClientSettingsCore preferredSceneHostIdentifier]
+ -[FBSSceneClientSettingsCore preferredSceneHostIdentity]
+ -[FBSSceneClientSettingsCore setPreferredInterfaceOrientation:]
+ -[FBSSceneClientSettingsCore setPreferredLevel:]
+ -[FBSSceneClientSettingsCore setPreferredSceneHostIdentifier:]
+ -[FBSSceneClientSettingsCore setPreferredSceneHostIdentity:]
+ -[FBSSceneClientSettingsDiffInspector init]
+ -[FBSSceneSettingsCore activityMode]
+ -[FBSSceneSettingsCore displayConfiguration]
+ -[FBSSceneSettingsCore frame:]
+ -[FBSSceneSettingsCore frame]
+ -[FBSSceneSettingsCore interfaceOrientation]
+ -[FBSSceneSettingsCore interruptionPolicy]
+ -[FBSSceneSettingsCore isClientFuture]
+ -[FBSSceneSettingsCore isForeground]
+ -[FBSSceneSettingsCore isOccluded]
+ -[FBSSceneSettingsCore jetsamMode]
+ -[FBSSceneSettingsCore level]
+ -[FBSSceneSettingsCore prefersProcessTaskSuspensionWhileSceneForeground]
+ -[FBSSceneSettingsCore setActivityMode:]
+ -[FBSSceneSettingsCore setClientFuture:]
+ -[FBSSceneSettingsCore setForeground:]
+ -[FBSSceneSettingsCore setInterfaceOrientation:]
+ -[FBSSceneSettingsCore setInterruptionPolicy:]
+ -[FBSSceneSettingsCore setJetsamMode:]
+ -[FBSSceneSettingsCore setLevel:]
+ -[FBSSceneSettingsCore setOccluded:]
+ -[FBSSceneSettingsCore setPrefersProcessTaskSuspensionWhileSceneForeground:]
+ -[FBSSceneSettingsDiffInspector init]
+ -[FBSSceneTransitionContextCore allowCPUThrottling]
+ -[FBSSceneTransitionContextCore animationFence]
+ -[FBSSceneTransitionContextCore animationSettings]
+ -[FBSSceneTransitionContextCore clientProcessHandle]
+ -[FBSSceneTransitionContextCore executionContext]
+ -[FBSSceneTransitionContextCore isRunningBoardAssertionDisabled]
+ -[FBSSceneTransitionContextCore originatingProcess]
+ -[FBSSceneTransitionContextCore setAllowCPUThrottling:]
+ -[FBSSceneTransitionContextCore setAnimationFence:]
+ -[FBSSceneTransitionContextCore setAnimationSettings:]
+ -[FBSSceneTransitionContextCore setClientProcessHandle:]
+ -[FBSSceneTransitionContextCore setExecutionContext:]
+ -[FBSSceneTransitionContextCore setOriginatingProcess:]
+ -[FBSSceneTransitionContextCore setRunningBoardAssertionDisabled:]
+ -[FBSSceneTransitionContextCore setUpdateContext:]
+ -[FBSSceneTransitionContextCore setWatchdogTransitionContext:]
+ -[FBSSceneTransitionContextCore updateContext]
+ -[FBSSceneTransitionContextCore watchdogTransitionContext]
+ -[FBSSettings _setValue:forSetting:inSettings:]
+ GCC_except_table113
+ GCC_except_table120
+ GCC_except_table123
+ GCC_except_table126
+ _CFPropertyListCreateDeepCopy
+ _OBJC_CLASS_$_BKSAnimationFenceHandle
+ _OBJC_CLASS_$_BSAnimationSettings
+ _OBJC_CLASS_$_FBSSceneTransitionContextCore
+ _OBJC_IVAR_$_FBSScene._calloutQueue_animationFence
+ _OBJC_METACLASS_$_FBSSceneTransitionContextCore
+ __FBSRealizedKey
+ __OBJC_$_CLASS_METHODS_FBSSceneTransitionContextCore
+ __OBJC_$_INSTANCE_METHODS_FBSSceneTransitionContextCore
+ __OBJC_$_PROP_LIST_FBSProcess.111
+ __OBJC_$_PROP_LIST_FBSSceneClientSettings.70
+ __OBJC_$_PROP_LIST_FBSSceneClientSettingsCore
+ __OBJC_$_PROP_LIST_FBSSceneSettings.165
+ __OBJC_$_PROP_LIST_FBSSceneSettingsCore
+ __OBJC_$_PROP_LIST_FBSSceneTransitionContext.141
+ __OBJC_$_PROP_LIST_FBSSceneTransitionContextCore
+ __OBJC_CLASS_PROTOCOLS_$_FBSSceneClientSettingsCore
+ __OBJC_CLASS_PROTOCOLS_$_FBSSceneSettingsCore
+ __OBJC_CLASS_PROTOCOLS_$_FBSSceneTransitionContextCore
+ __OBJC_CLASS_RO_$_FBSSceneTransitionContextCore
+ __OBJC_METACLASS_RO_$_FBSSceneTransitionContextCore
+ ___37-[FBSSceneSettingsDiffInspector init]_block_invoke
+ ___43-[FBSSceneClientSettingsDiffInspector init]_block_invoke
+ ___block_descriptor_48_e8_32s40s_e69_v24?0"FBSMutableSceneClientSettings"8"FBSSceneTransitionContext"16ls32l8s40l8
+ _init.onceToken
+ _kCFAllocatorDefault
+ _kCFBooleanFalse
+ _objc_msgSend$bs_CGFloatValue
+ _objc_msgSend$numberWithChar:
+ _objc_msgSend$objCType
+ _strcmp
- +[FBSSceneClientSettingsDiffInspector initialize]
- +[FBSSceneSettingsDiffInspector initialize]
- GCC_except_table112
- GCC_except_table119
- GCC_except_table122
- GCC_except_table125
- _OBJC_IVAR_$_FBSApplicationDataStore._applicationIdentifier
- _OBJC_IVAR_$_FBSApplicationInfo._fallbackFolderName
- _OBJC_IVAR_$_FBSApplicationInfo._folderNames
- _OBJC_IVAR_$_FBSApplicationInfo._isManaged
- _OBJC_IVAR_$_FBSApplicationInfo._lazy_fallbackFolderName
- _OBJC_IVAR_$_FBSApplicationInfo._lazy_folderNames
- _OBJC_IVAR_$_FBSProcess._running
- __OBJC_$_CLASS_METHODS_FBSSceneClientSettingsDiffInspector
- __OBJC_$_CLASS_METHODS_FBSSceneSettingsDiffInspector
- __OBJC_$_PROP_LIST_FBSProcess.113
- __OBJC_$_PROP_LIST_FBSSceneClientSettings.67
- __OBJC_$_PROP_LIST_FBSSceneSettings.159
- __OBJC_$_PROP_LIST_FBSSceneTransitionContext.123
- ___block_descriptor_40_e8_32s_e69_v24?0"FBSMutableSceneClientSettings"8"FBSSceneTransitionContext"16ls32l8
- _objc_msgSend$bs_isPlistableType
- _objc_msgSend$extensionForProtocol:
CStrings:
+ "\x01\x116\x16\x14!%"
+ "\x01\x14\x13\x16"
+ "\x02\x12"
+ "\x03\x11\x11"
+ "\""
+ "@\"BKSAnimationFenceHandle\""
+ "Dev Mode Required"
+ "ERROR: unable to store value of class \"%{public}@\" for nil key"
+ "ERROR: value provided for key \"%{public}@\" is not a valid property list"
+ "FBProcessExecutionContext"
+ "FBSSceneTransitionContextCore"
+ "FBSceneUpdateContext"
+ "FBWatchdogTransitionContext"
+ "T@\"<FBSApplicationIdentifying>\",R,N,V_identifier"
+ "T@\"FBProcessExecutionContext\",&,D,N"
+ "T@\"RBSProcessHandle\",&,D,N"
+ "TB,D,N"
+ "TB,D,N,GisRunningBoardAssertionDisabled"
+ "TB,R,N,GisRunning"
+ "_calloutQueue_animationFence"
+ "_synchronizationQueue"
+ "bs_CGFloatValue"
+ "frame:"
+ "numberWithChar:"
+ "objCType"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}"
+ "\xa1"
- "\x01\x13\x13\x16"
- "\x02\x13"
- "\x03b"
- "\x06\x15\x12\x12#!!\x15!\x12"
- "@\"<FBSApplicationIdentifying>\""
- "ERROR: unable to store value of class \"%{public}@\" for key \"%{public}@\""
- "T@\"<FBSApplicationIdentifying>\",R,N,V_applicationIdentifier"
- "T@\"NSArray\",R,N,V_folderNames"
- "T@\"NSString\",R,N,V_fallbackFolderName"
- "TB,R,N,GisRunning,V_running"
- "_applicationIdentifier"
- "_fallbackFolderName"
- "_folderNames"
- "_lazy_fallbackFolderName"
- "_lazy_folderNames"
- "_running"
- "bs_isPlistableType"

```
