## HIServices

> `/System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/HIServices.framework/Versions/A/HIServices`

```diff

 807.2.0.0.0
-  __TEXT.__text: 0x5c6e4
-  __TEXT.__auth_stubs: 0x3280
+  __TEXT.__text: 0x5bb74
+  __TEXT.__auth_stubs: 0x3270
   __TEXT.__objc_methlist: 0x10c
-  __TEXT.__const: 0x1640
+  __TEXT.__const: 0x1620
   __TEXT.__cstring: 0x5e1d
   __TEXT.__oslogstring: 0x20c7
   __TEXT.__dlopen_cstrs: 0xfc
   __TEXT.__ustring: 0xd2
-  __TEXT.__gcc_except_tab: 0x358
+  __TEXT.__gcc_except_tab: 0x354
   __TEXT.__dof_Accessibi: 0x90c
-  __TEXT.__unwind_info: 0xd48
+  __TEXT.__unwind_info: 0xdc8
   __TEXT.__objc_classname: 0x30
   __TEXT.__objc_methname: 0x4e3
   __TEXT.__objc_methtype: 0xb0
   __TEXT.__objc_stubs: 0x700
-  __DATA_CONST.__got: 0x4f0
+  __DATA_CONST.__got: 0x4e0
   __DATA_CONST.__const: 0x11a0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x210
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1958
+  __AUTH_CONST.__auth_got: 0x1950
   __AUTH_CONST.__const: 0x17b8
   __AUTH_CONST.__cfstring: 0x5c80
   __AUTH_CONST.__objc_const: 0x230

   __DATA.__objc_ivar: 0x1c
   __DATA.__data: 0x460
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x1020
+  __DATA.__bss: 0x1048
   __DATA.__common: 0x54
   __DATA_DIRTY.__data: 0x230
-  __DATA_DIRTY.__bss: 0x320
+  __DATA_DIRTY.__bss: 0x2d0
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/QD.framework/Versions/A/QD

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5AF090D7-4D2E-3263-9BEC-687BC2058651
-  Functions: 1613
-  Symbols:   3309
+  UUID: FCB9EA71-5118-331B-9070-BA311437EAFB
+  Functions: 1790
+  Symbols:   3556
   CStrings:  2048
 
Symbols:
+ +[HIRunLoopSemaphore _observe:whilePerforming:].cold.1
+ +[HIRunLoopSemaphore _observe:whilePerforming:].cold.2
+ +[HIRunLoopSemaphore _observe:whilePerforming:].cold.3
+ +[HIRunLoopSemaphore _observe:whilePerforming:].cold.4
+ +[HIRunLoopSemaphore _observe:whilePerforming:].cold.5
+ +[HIRunLoopSemaphore _observe:whilePerforming:].cold.6
+ +[HIRunLoopSemaphore _observe:whilePerforming:].cold.7
+ +[HIRunLoopUtilities addRunLoopModesForDeferredActions:].cold.1
+ -[HIRunLoopSemaphore dealloc].cold.1
+ -[HIRunLoopSemaphore initWithMode:].cold.1
+ -[HIRunLoopSemaphore initWithMode:].cold.2
+ -[HIRunLoopSemaphore init].cold.1
+ -[HIRunLoopSemaphore init].cold.2
+ -[HIRunLoopSemaphore signal].cold.1
+ -[HIRunLoopSemaphore signal].cold.2
+ -[HIRunLoopSemaphore wait:].cold.1
+ -[HIRunLoopSemaphore wait:].cold.2
+ -[HIRunLoopSemaphore wait:].cold.3
+ -[HIRunLoopSemaphore wait:].cold.4
+ -[HIRunLoopSemaphore wait].cold.1
+ -[HIRunLoopSemaphore whileInhibitingCFRunLoopRunFinished:perform:].cold.1
+ AXIsProcessTrustedWithOptions.cold.1
+ AXUIElementCopyActionDescription.cold.1
+ AXUIElementCopyActionNames.cold.1
+ AXUIElementCopyAttributeNames.cold.1
+ AXUIElementCopyAttributeValue.cold.1
+ AXUIElementCopyAttributeValues.cold.1
+ AXUIElementCopyMultipleAttributeValues.cold.1
+ AXUIElementCopyParameterizedAttributeNames.cold.1
+ AXUIElementCopyParameterizedAttributeValue.cold.1
+ AXUIElementGetAttributeValueCount.cold.1
+ AXUIElementIsAttributeSettable.cold.1
+ AXUIElementPerformAction.cold.1
+ AXUIElementPostKeyboardEvent.cold.1
+ AXUIElementSetAttributeValue.cold.1
+ CGPointInIconRef.cold.1
+ CGRectInIconRef.cold.1
+ CoreDragGetDropLocation.cold.1
+ CoreDragSetDropLocation.cold.1
+ CoreMenuExtraRemoveMenuExtra.cold.1
+ GetApplicationIsDaemon.cold.1
+ GetGlobalIconImagesCacheMaxEntriesAndMaxDataSize.cold.1
+ GetIconFamilyData.cold.1
+ GetIconRefVariant.cold.1
+ GetProcessForPID.cold.1
+ HIS_XPCImp_RevealFileInFinder.cold.1
+ HIS_XPC_CFPreferencesCopyValue.cold.1
+ HIS_XPC_CFPreferencesCopyValue.cold.2
+ HIShapeCreateEmpty.cold.1
+ IPCFlockPingProc.cold.1
+ IconRefContainsCGPoint.cold.1
+ IconRefIntersectsCGRect.cold.1
+ IconRefToHIShape.cold.1
+ IconRefToIconFamily.cold.1
+ IsIconRefMaskEmpty.cold.1
+ KillProcess.cold.1
+ KillProcess.cold.2
+ LaunchApplication.cold.1
+ PlotIconRefInContext.cold.1
+ ProcessInformationCopyDictionary.cold.1
+ SetApplicationIsDaemon.cold.1
+ SetFrontProcessWithOptions.cold.1
+ SetFrontProcessWithOptions.cold.2
+ SetGlobalIconImagesCacheMaxEntriesAndMaxDataSize.cold.1
+ SetIconFamilyData.cold.1
+ ShowHideProcess.cold.1
+ ShowHideProcess.cold.2
+ ShowHideProcess.cold.3
+ TransformProcessType.cold.1
+ TransformProcessType.cold.2
+ TransformProcessType.cold.3
+ _AXUIElementCopyElementAtPositionIncludeIgnored.cold.1
+ _AXXMIGCopyHierarchy.cold.1
+ _GDBIconsCGCacheList.cold.1
+ _HIRLU_AddRunLoopModeForDeferredActions.cold.1
+ _HIRLU_AddRunLoopModeForDeferredActions.cold.2
+ _HIRLU_DeferActions.cold.1
+ _HIRunLoopSemaphoreCreateWithRunLoopMode.cold.1
+ _HIRunLoopSemaphoreCreateWithRunLoopMode.cold.2
+ _HIRunLoopSemaphoreSetLegend.cold.1
+ _HIRunLoopSemaphoreSetLegend.cold.2
+ _HIRunLoopSemaphoreSetLegend.cold.3
+ _HIRunLoopSemaphoreSignal.cold.1
+ _HIRunLoopSemaphoreWait.cold.1
+ _ISCreateCGImageForType.cold.1
+ _ISCreateCGImageForTypeAtScale.cold.1
+ _IconServicesGetCGImageRefFromIconRef.cold.1
+ _IconServicesGetCGImageRefFromURL.cold.1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _RegisterApplication.cold.10
+ _RegisterApplication.cold.11
+ _RegisterApplication.cold.12
+ _RegisterApplication.cold.13
+ _RegisterApplication.cold.14
+ _RegisterApplication.cold.15
+ _RegisterApplication.cold.16
+ _RegisterApplication.cold.17
+ _RegisterApplication.cold.18
+ _RegisterApplication.cold.19
+ _RegisterApplication.cold.20
+ _RegisterApplication.cold.21
+ _RegisterApplication.cold.22
+ _RegisterApplication.cold.23
+ _RegisterApplication.cold.24
+ _RegisterApplication.cold.25
+ _RegisterApplication.cold.26
+ _RegisterApplication.cold.27
+ _RegisterApplication.cold.28
+ _RegisterApplication.cold.29
+ _RegisterApplication.cold.30
+ _RegisterApplication.cold.31
+ _RegisterApplication.cold.32
+ _RegisterApplication.cold.33
+ _RegisterApplication.cold.34
+ _RegisterApplication.cold.35
+ _RegisterApplication.cold.36
+ _RegisterApplication.cold.37
+ _RegisterApplication.cold.38
+ _RegisterApplication.cold.39
+ _RegisterApplication.cold.4
+ _RegisterApplication.cold.40
+ _RegisterApplication.cold.41
+ _RegisterApplication.cold.42
+ _RegisterApplication.cold.43
+ _RegisterApplication.cold.44
+ _RegisterApplication.cold.45
+ _RegisterApplication.cold.5
+ _RegisterApplication.cold.6
+ _RegisterApplication.cold.7
+ _RegisterApplication.cold.8
+ _RegisterApplication.cold.9
+ _RegisterAsSessionLauncherApplication.cold.1
+ _SendMessageToHISService.cold.1
+ _SignalApplicationReady.cold.1
+ _Z40SetFrontProcessWithWindowIDAndCPSOptionsPK19ProcessSerialNumberjm.cold.1
+ _Z40SetFrontProcessWithWindowIDAndCPSOptionsPK19ProcessSerialNumberjm.cold.2
+ _ZL17wakeUpMainRunLoopP11objc_object.cold.1
+ _ZL17wakeUpMainRunLoopP11objc_object.cold.2
+ _ZL17wakeUpMainRunLoopP11objc_object.cold.3
+ _ZL17wakeUpMainRunLoopP11objc_object.cold.4
+ _ZL19_HIE_EmbellishCrashP11NSExceptionPKc.cold.1
+ _ZL19_HIE_EmbellishCrashP11NSExceptionPKc.cold.2
+ _ZL19_HIE_EmbellishCrashP11NSExceptionPKc.cold.3
+ _ZL19_HIE_EmbellishCrashP11NSExceptionPKc.cold.4
+ _ZL19_HIE_EmbellishCrashP11NSExceptionPKc.cold.5
+ _ZL19_HIE_EmbellishCrashP11NSExceptionPKc.cold.6
+ _ZL19_HIE_EmbellishCrashPKcS0_S0_.cold.1
+ _ZL19_HIE_EmbellishCrashPKcS0_S0_.cold.2
+ _ZL19_HIE_EmbellishCrashPKcS0_S0_.cold.3
+ _ZL19_HIE_EmbellishCrashRKSt9exceptionPKc.cold.1
+ _ZL19_HIE_EmbellishCrashRKSt9exceptionPKc.cold.2
+ _ZL19_HIE_EmbellishCrashRKSt9exceptionPKc.cold.3
+ _ZL19_HIE_EmbellishCrashRKSt9exceptionPKc.cold.4
+ _ZL19_HIE_EmbellishCrashRKSt9exceptionPKc.cold.5
+ _ZL19mainThreadHasAwokenP12__CFMachPortPvlS1_.cold.1
+ _ZL23RegisterAllTranslationsv.cold.1
+ _ZL23RegisterAllTranslationsv.cold.2
+ _ZL24deferredBlockOpportunity_block_invoke_2.cold.1
+ _ZL24deferredBlockOpportunity_block_invoke_2.cold.2
+ _ZL25handleBringForwardRequestPK14__CFDictionaryPK7__LSASNb.cold.1
+ _ZL25handleBringForwardRequestPK14__CFDictionaryPK7__LSASNb.cold.2
+ _ZL25handleBringForwardRequestPK14__CFDictionaryPK7__LSASNb.cold.3
+ _ZL36HIServicesLSNotificationCallbackFunc18LSNotificationCodedPKvPK7__LSASNS1_11LSSessionIDS1_.cold.1
+ _ZL36HIServicesLSNotificationCallbackFunc18LSNotificationCodedPKvPK7__LSASNS1_11LSSessionIDS1_.cold.2
+ _ZL36HIServicesLSNotificationCallbackFunc18LSNotificationCodedPKvPK7__LSASNS1_11LSSessionIDS1_.cold.3
+ _ZL36HIServicesLSNotificationCallbackFunc18LSNotificationCodedPKvPK7__LSASNS1_11LSSessionIDS1_.cold.4
+ _ZN14ICDefaultPrefs28GetStandardDefaultDictionaryEv.cold.1
+ __27-[HIRunLoopSemaphore wait:]_block_invoke_4.cold.1
+ __32+[HIRunLoopUtilities initialize]_block_invoke.cold.1
+ __32+[HIRunLoopUtilities initialize]_block_invoke.cold.2
+ __34+[HIRunLoopSemaphore _invocations]_block_invoke.cold.1
+ __47+[HIRunLoopSemaphore _observe:whilePerforming:]_block_invoke.cold.1
+ __47+[HIRunLoopSemaphore _observe:whilePerforming:]_block_invoke.cold.2
+ __47+[HIRunLoopSemaphore _observe:whilePerforming:]_block_invoke_2.cold.1
+ __47+[HIRunLoopSemaphore _observe:whilePerforming:]_block_invoke_2.cold.2
+ __47+[HIRunLoopSemaphore _observe:whilePerforming:]_block_invoke_2.cold.3
+ __56+[HIRunLoopUtilities addRunLoopModesForDeferredActions:]_block_invoke.cold.1
+ __56+[HIRunLoopUtilities addRunLoopModesForDeferredActions:]_block_invoke.cold.2
+ __56+[HIRunLoopUtilities addRunLoopModesForDeferredActions:]_block_invoke.cold.3
+ __HIServicesLogDragAndDrop.cold.1
+ __ZL24TranslateCGSErrorToOSErr7CGError
+ ___CoreEnsembleForceSpinDragLoop_block_invoke.cold.1
+ ___CoreEnsemblePerformOnRunLoop_block_invoke.cold.1
+ ___ZL10initializeP11objc_object_block_invoke.cold.1
+ ___ZL10initializeP11objc_object_block_invoke.cold.2
+ ___ZL10initializeP11objc_object_block_invoke.cold.3
+ ___ZL10initializeP11objc_object_block_invoke.cold.4
+ ___ZL16_HIRLU_ShouldLogv_block_invoke.cold.1
+ ___axRequester_block_invoke.cold.1
+ _axIPCRequester.cold.1
+ _copyAutomationTypeAttribute.cold.1
+ _getIconServicesLibraryHandle.cold.1
+ hasAuthorizationForControlComputer.cold.1
+ hasAuthorizationForControlComputer.cold.2
- CoreDragCreateInternal.cold.1
- CoreDragCreateInternal.token
- CoreDragMessageHandler.cold.1
- CoreDragMessageHandler.cold.10
- CoreDragMessageHandler.cold.11
- CoreDragMessageHandler.cold.12
- CoreDragMessageHandler.cold.13
- CoreDragMessageHandler.cold.14
- CoreDragMessageHandler.cold.15
- CoreDragMessageHandler.cold.16
- CoreDragMessageHandler.cold.17
- CoreDragMessageHandler.cold.18
- CoreDragMessageHandler.cold.19
- CoreDragMessageHandler.cold.2
- CoreDragMessageHandler.cold.20
- CoreDragMessageHandler.cold.21
- CoreDragMessageHandler.cold.22
- CoreDragMessageHandler.cold.23
- CoreDragMessageHandler.cold.24
- CoreDragMessageHandler.cold.25
- CoreDragMessageHandler.cold.26
- CoreDragMessageHandler.cold.3
- CoreDragMessageHandler.cold.4
- CoreDragMessageHandler.cold.5
- CoreDragMessageHandler.cold.6
- CoreDragMessageHandler.cold.7
- CoreDragMessageHandler.cold.8
- CoreDragMessageHandler.cold.9
- CoreDragMessageHandler.sState
- InitializeDragIPC._initialized
- InitializeDragIPC.cold.1
- SendDragIPCMessage.cold.1
- __ZGVZL22GetEmptySingletonShapevE11sEmptyShape
- __ZL19__kPasteboardTypeID
- __ZL24TranslateCGSErrorToOSErri
- __ZL25gPasteboardOwnershipCache
- __ZL26sProcessManagerInitialized
- __ZL28gPasteboardTypeIDInitialized
- __ZL33gPasteboardOwnershipCacheInitLock
- __ZL35CorePasteboardUnicodeLineFeedMungerPtj
- __ZL36gPasteboardOwnershipCacheInitialized
- __ZL7sOurASN
- __ZZ15GetFrontProcessE29sNeverSeenAFrontProcessBefore
- __ZZL16_HIRLU_ShouldLogvE4once
- __ZZL16_HIRLU_ShouldLogvE6result
- __ZZL17FSRefToStaticPathPK5FSRefE4path
- __ZZL22GetEmptySingletonShapevE11sEmptyShape
- __ZZL32ProcessManagerLazyInitializationhPK19ProcessSerialNumberE42sCheckedApplicationTypeToCauseRegistration
- __ZZL33GetPerPasteboardLookupCollectionsP19OpaquePasteboardRefPP14__CFDictionaryPP9__CFArrayE19sIndexToItemLookups
- __ZZL33GetPerPasteboardLookupCollectionsP19OpaquePasteboardRefPP14__CFDictionaryPP9__CFArrayE19sItemToIndexLookups
- _fmod
- _gDragInfoDict
- _isAppSandboxed.onceToken
- _isAppSandboxed.sIsAppSandboxed
- _sClientMessageProc
- _sClientMessageProcData
- _sClientPort
- _sClientSource
- _sDockDeathSource
- _sPreventDockCommunication
- _sRunLoop
- _sTransactionList
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/HIServices/Accessibility.subproj/Accessibility.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/HIServices/Accessibility.subproj/Accessibility.c"

```
