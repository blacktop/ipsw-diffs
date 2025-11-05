## HIToolbox

> `/System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/HIToolbox.framework/Versions/A/HIToolbox`

```diff

-1219.3.0.0.0
-  __TEXT.__text: 0x2a1728
-  __TEXT.__auth_stubs: 0x6240
-  __TEXT.__objc_methlist: 0x3248
-  __TEXT.__gcc_except_tab: 0x6f9c
-  __TEXT.__const: 0xaa54
-  __TEXT.__cstring: 0x2dfb1
+1220.2.0.0.0
+  __TEXT.__text: 0x29fab0
+  __TEXT.__auth_stubs: 0x6250
+  __TEXT.__objc_methlist: 0x3ce4
+  __TEXT.__gcc_except_tab: 0x7124
+  __TEXT.__const: 0xab24
+  __TEXT.__cstring: 0x2d7d2
   __TEXT.__ustring: 0x9e
-  __TEXT.__oslogstring: 0x460
-  __TEXT.__unwind_info: 0xa658
+  __TEXT.__oslogstring: 0xc69
+  __TEXT.__unwind_info: 0xa858
   __TEXT.__eh_frame: 0x350
   __TEXT.__objc_classname: 0x53a
   __TEXT.__objc_methname: 0x790e
   __TEXT.__objc_methtype: 0x22e4
   __TEXT.__objc_stubs: 0x6e60
   __DATA_CONST.__got: 0xcb8
-  __DATA_CONST.__const: 0x79f0
+  __DATA_CONST.__const: 0x79f8
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1fb0
+  __DATA_CONST.__objc_selrefs: 0x20c8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x250
-  __AUTH_CONST.__auth_got: 0x3140
-  __AUTH_CONST.__const: 0x151c8
-  __AUTH_CONST.__cfstring: 0x1bde0
-  __AUTH_CONST.__objc_const: 0x5d88
+  __AUTH_CONST.__auth_got: 0x3148
+  __AUTH_CONST.__const: 0x151e8
+  __AUTH_CONST.__cfstring: 0x1baa0
+  __AUTH_CONST.__objc_const: 0x4938
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xb40
-  __AUTH.__data: 0x3a0
+  __AUTH.__data: 0x3e0
   __DATA.__objc_ivar: 0x498
-  __DATA.__data: 0xd38
+  __DATA.__data: 0xcf0
   __DATA.__crash_info: 0x40
   __DATA.__common: 0x378
-  __DATA.__bss: 0x3dc8
+  __DATA.__bss: 0x3d60
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
-  UUID: 950F1236-ACAF-379D-819F-6C6B0B5DEABD
-  Functions: 12279
-  Symbols:   19016
-  CStrings:  10739
+  UUID: 6CC82A38-F1B5-3F2B-876B-9B3D7B278490
+  Functions: 13884
+  Symbols:   20573
+  CStrings:  10712
 
Symbols:
+ +[IMKClient_Legacy(IMKClientConnection_XPC) privateRunLoopMode].cold.1
+ +[IMKClient_Legacy(IMKClient_Main_Thread_Tracking) IMKRunLoopGetMain].cold.1
+ +[IMKClient_Modern(IMKClientConnection_XPC) privateRunLoopMode].cold.1
+ +[IMKInputSession_Legacy IMKCFRunLoopSetup].cold.1
+ +[IMKInputSession_Legacy IMKXPCPerformBlockOnMainThreadInMode:performHow:callerCmd:workBlock:].cold.1
+ +[IMKInputSession_Legacy IMKXPCPerformBlockOnMainThreadInMode:performHow:callerCmd:workBlock:].cold.2
+ +[IMKInputSession_Modern IMKCFRunLoopSetup].cold.1
+ -[IMKClient_Legacy switchedInputMode:].cold.1
+ -[IMKClient_Modern switchedInputMode:].cold.1
+ -[IMKEvent initWithCoder:].cold.1
+ -[IMKInputSession_Legacy _copyUniCharsForRange:intoBuffer:ofLength:completionHandler:].cold.1
+ -[IMKInputSession_Legacy _coreAttributesFromRange:whichAttributes:completionHandler:].cold.1
+ -[IMKInputSession_Legacy firstRectForCharacterRange:completionHandler:].cold.1
+ -[IMKInputSession_Legacy invalidateClientGeometry].cold.1
+ -[IMKInputSession_Legacy invalidateClientGeometry].cold.2
+ -[IMKInputSession_Legacy presentFunctionRowItemTextInputViewWithEndpoint:completionHandler:].cold.1
+ -[IMKInputSession_Legacy selectedRange].cold.1
+ -[IMKInputSession_Legacy validAttributesForMarkedText].cold.1
+ -[IMKInputSession_Legacy wouldHandleEvent:completionHandler:].cold.1
+ -[IMKInputSession_Modern _copyUniCharsForRange:intoBuffer:ofLength:completionHandler:].cold.1
+ -[IMKInputSession_Modern _coreAttributesFromRange:whichAttributes:completionHandler:].cold.1
+ -[IMKInputSession_Modern firstRectForCharacterRange:completionHandler:].cold.1
+ -[IMKInputSession_Modern invalidateClientGeometry].cold.1
+ -[IMKInputSession_Modern invalidateClientGeometry].cold.2
+ -[IMKInputSession_Modern presentFunctionRowItemTextInputViewWithEndpoint:completionHandler:].cold.1
+ -[IMKInputSession_Modern selectedRange].cold.1
+ -[IMKInputSession_Modern validAttributesForMarkedText].cold.1
+ -[IMKInputSession_Modern wouldHandleEvent:completionHandler:].cold.1
+ -[IPMDEventParameter initWithCoder:].cold.1
+ AttachPlatformWindow.cold.1
+ AutoShowMenuBarIfAllowed.cold.1
+ CancelMenuTracking.cold.1
+ CharacterPaletteLaunchLog.cold.1
+ CheckEventQueueForUserCancel.cold.1
+ ClearDeadKeyInlineSession_WithCompletionHandler.cold.1
+ CreateEventTarget.cold.1
+ CreateInputMethodInstance.cold.1
+ DisableWindowServerConnection.cold.1
+ EventTimeToMachTime.cold.1
+ FindSpecificEventInQueue.cold.1
+ FlushSpecificEventsFromQueue.cold.1
+ GCC_except_table315
+ GCC_except_table499
+ GCC_except_table524
+ GetControlBounds.cold.1
+ GetMacModifiers.cold.1
+ GetSystemUIMode.cold.1
+ HIObjectPrintDebugInfo.cold.1
+ HandleKeyFocusHotKey.cold.1
+ HandleKeyFocusHotKey.cold.2
+ HandleKeyFocusHotKey.cold.3
+ IMKCopyExtensionBundlePaths.cold.1
+ IMKInitializeNSRemoteView.cold.1
+ IMServerDiedAbnormally.cold.1
+ INIT_AppleEvents.cold.1
+ InputModeListApplier.cold.1
+ InputModeListApplier.cold.2
+ InputSourceToolboxListenerWithInternalHint.cold.1
+ InstallInputSourceMgrHandlers.cold.1
+ InvalidateAllSelectedInputSourceState.cold.1
+ IsAppKitMenuSystemEnabled.cold.1
+ IsMenuBarAvailableInProcess.cold.1
+ IsNSTextInputContextCompletionHandling.cold.1
+ LocalCFPrefsAPI_EvenIfAppSandboxed.cold.1
+ MBHeightClient.cold.1
+ MBNotchFrameClient.cold.1
+ MachTimeConversionRate.cold.1
+ MachTimeToEventTime.cold.1
+ MenuSelect.cold.1
+ MyActivateTSMDocument.cold.1
+ MyActivateTSMDocument.cold.2
+ MyActivateTSMDocument.cold.3
+ MyActivateTSMDocument.cold.4
+ NewControl.cold.1
+ NotifyVisibleWindowsOfCoreUIChange.cold.1
+ PostFilterTextInputEvent.cold.1
+ ProcessKanaEisuKey.cold.1
+ RebuildSectionHeads.cold.1
+ ReceiveNextEventCommon.cold.1
+ SendDocumentAccessGetFontEvent_WithCompletionHandler.cold.1
+ SendRestrictEnabledInputSourcesMessageToUIServer.cold.1
+ SendRestrictEnabledInputSourcesMessageToUIServer.cold.2
+ SetWindowGroupByLevel.cold.1
+ Start_CapsLock_KBLayoutDelayOverride_ForTyping_Timer.cold.1
+ TISCopyInputSourcesForAttachedKeyboardsFilteredByLocale.cold.1
+ TISGetRomanSwitchState.cold.1
+ TISIsRomanSwitchEnabled.cold.1
+ TISLaunchCharacterPalette.cold.1
+ TISUpdateIntlFileCache.cold.1
+ TSMAdjustDoubleTapAction.cold.1
+ TSMAdjustDoubleTapAction.cold.2
+ TSMAdjustDoubleTapAction.cold.3
+ TSMAdjustDoubleTapAction.cold.4
+ TSMAdjustDoubleTapAction.cold.5
+ TSMAdjustDoubleTapAction.cold.6
+ TSMCurrentAsciiCapableInputSourceRefCreate.cold.1
+ TSMCurrentAsciiCapableKeyboardLayoutInputSourceRefCreate.cold.1
+ TSMCurrentAsciiCapableKeyboardLayoutInputSourceRefCreate.cold.2
+ TSMCurrentAsciiCapableKeyboardLayoutInputSourceRefCreate.cold.3
+ TSMCurrentKeyboardLayoutInputSourceRefCreate.cold.1
+ TSMEnsureIronwoodLoadedForHotKey.cold.1
+ TSMGetKeyboardLayoutOverride_Internal.cold.1
+ TSMLaunchCharacterPalette.cold.1
+ TSMLaunchCharacterPalette.cold.2
+ TSMMessagePortCallBack.cold.1
+ TSMMessagePortCallBack.cold.2
+ TSMMessagePortCallBack.cold.3
+ TSMPreviousKeyboardInputSourceRefCreate.cold.1
+ TSMProcessRawKeyEventWithOptionsAndCompletionHandler.cold.1
+ TSMProcessRawKeyEventWithOptionsAndCompletionHandler.cold.2
+ TSMProcessRawKeyEventWithOptionsAndCompletionHandler.cold.3
+ TSMProcessRawKeyEventWithOptionsAndCompletionHandler.cold.4
+ TSMProcessRawKeyEventWithOptionsAndCompletionHandler.cold.5
+ TSMSetDocumentProperty.cold.1
+ TSMSetDocumentProperty.cold.10
+ TSMSetDocumentProperty.cold.2
+ TSMSetDocumentProperty.cold.3
+ TSMSetDocumentProperty.cold.4
+ TSMSetDocumentProperty.cold.5
+ TSMSetDocumentProperty.cold.6
+ TSMSetDocumentProperty.cold.7
+ TSMSetDocumentProperty.cold.8
+ TSMSetDocumentProperty.cold.9
+ TSMTestTextFilterHandler.cold.1
+ TSMToolboxListener.cold.1
+ TSMTranslateKeyEvent.cold.1
+ TSMTranslateKeyEvent.cold.2
+ TSMTranslateKeyEvent.cold.3
+ TSMTranslateKeyEvent.cold.4
+ UpdateSourceIndicatorMode.cold.1
+ _BeginEventReceiptOnThreadWithFilter.cold.2
+ _ConvertMatchingCGEvents.cold.1
+ _EventThreadLock.cold.1
+ _FirstEventTime.cold.1
+ _HIMagnifiedMode.cold.1
+ _HIMenuBarPositionLock.cold.2
+ _HIMenuBarPositionLock.cold.3
+ _HIMenuBarPositionLock.cold.4
+ _HIMenuBarPositionLock.cold.5
+ _HIMenuBarPositionUnlock.cold.2
+ _HIMenuBarPositionUnlock.cold.3
+ _HIMenuBarRequestVisibility.cold.1
+ _HIMenuBarSetAppearanceOverride.cold.1
+ _HIMenuBarSetAutoHideHeight.cold.1
+ _HIMenuBarSetAutoShowDelay.cold.1
+ _HIMenuBarSetTransitionDuration.cold.1
+ _HIThemeGetSymbolImage.cold.1
+ _HIThemeIsCondensedLineLayoutEnabled.cold.1
+ _HIThemeIsCondensedLineLayoutEnabled.cold.2
+ _HIThemeThreadLock.cold.1
+ _IMKClientCopyMenuItems.cold.1
+ _MergedGlobals.1057
+ _MergedGlobals.12
+ _MergedGlobals.58
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_39
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_41
+ _OUTLINED_FUNCTION_42
+ _OUTLINED_FUNCTION_43
+ _OUTLINED_FUNCTION_44
+ _OUTLINED_FUNCTION_45
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _ReactivateTSMDocumentAfterMenuTracking.cold.1
+ _SetAppleMenuInstallerMode.cold.2
+ _SetCapsLockModifierState.cold.1
+ _SystemUIModeFromProcessAttributes.cold.1
+ _TSMCopySelectableInputSourcesInUIOrder.cold.1
+ _TSMSetInputSourceSelected.cold.1
+ _TSMSetRemoteViewActivation.cold.1
+ _Z10client_logv.cold.1
+ _Z12CheckForDashP8MenuDatathPKhPK10__CFString.cold.1
+ _Z12CheckForDashP8MenuDatathPKhPK10__CFString.cold.2
+ _Z12CheckForDashP8MenuDatathPKhPK10__CFString.cold.3
+ _Z12xpcreply_logv.cold.1
+ _Z15_IsMenuKeyEventP8MenuDataP14OpaqueEventRefjPS0_Pt.cold.1
+ _Z16ThemeFontReleaseP10TThemeFont.cold.1
+ _Z16_DisableMenuItemP8MenuDatat.cold.1
+ _Z16_DisableMenuItemP8MenuDatat.cold.2
+ _Z18PromoteFrontWindowP13WindowContextP10WindowDatahPh.cold.1
+ _Z18PromoteFrontWindowP13WindowContextP10WindowDatahPh.cold.2
+ _Z19FetchItemCommandKeyP8MenuDatai15MenuItemDataRefjP14MenuCommandKey.cold.1
+ _Z19FetchItemCommandKeyP8MenuDatai15MenuItemDataRefjP14MenuCommandKey.cold.2
+ _Z19RemoveCustomAppMenuv.cold.1
+ _Z22DebugPrintMenuKeyCachev.cold.1
+ _Z25AdjustActivationOnOrderInP10WindowDataS0_.cold.1
+ _Z27UseSymbolImagesForModifiersji.cold.1
+ _Z27UseSymbolImagesForModifiersji.cold.2
+ _Z31_HIObjectSendCreatedFromArchiveP17OpaqueHIObjectRefh.cold.1
+ _Z33FullScreenModeWindowToBeDestroyedP10WindowData.cold.1
+ _Z33_HIMenuGetEffectiveDirectionalityP8MenuData.cold.1
+ _Z33_HIMenuGetEffectiveDirectionalityP8MenuData.cold.2
+ _Z34CreateWindowViaNSMenuWindowManager6CGRect.cold.1
+ _Z34WindowStateDetectRestoreAppleEventPK6AEDescjj.cold.1
+ _Z49AttemptFullScreenForWindowCreatedInFullScreenModeP10WindowData.cold.1
+ _Z8_MBarHitP8MenuData5PointhPhPS0_.cold.1
+ _ZL10MODES_LOCKv.cold.1
+ _ZL11MBLogUIModePKcP15MenuBarInstancej.cold.1
+ _ZL11MBLogUIModePKcP15MenuBarInstancej.cold.2
+ _ZL11MBLogUIModePKcP15MenuBarInstancej.cold.3
+ _ZL11MBLogUIModePKcP15MenuBarInstancej.cold.4
+ _ZL11initADMUserv.cold.1
+ _ZL12HelpTagTimerP16__EventLoopTimerPv.cold.1
+ _ZL12PopulateMenuP8MenuDataP20OpaqueEventTargetRefP13CheckMenuDatajd.cold.1
+ _ZL12PopulateMenuP8MenuDataP20OpaqueEventTargetRefP13CheckMenuDatajd.cold.2
+ _ZL13GetRecentMenuv.cold.1
+ _ZL13HILogInternalPU19objcproto9OS_os_log8NSObjectbPKc.cold.2
+ _ZL13HILogInternalPU19objcproto9OS_os_log8NSObjectbPKc.cold.3
+ _ZL14HandleKeyEventP14OpaqueEventRefR14MenuSelectData.cold.1
+ _ZL14HandleKeyEventP14OpaqueEventRefR14MenuSelectData.cold.2
+ _ZL14HandleKeyEventP14OpaqueEventRefR14MenuSelectData.cold.3
+ _ZL14MBLogUIOptionsPKcP15MenuBarInstancej.cold.1
+ _ZL14MBLogUIOptionsPKcP15MenuBarInstancej.cold.2
+ _ZL14MBLogUIOptionsPKcP15MenuBarInstancej.cold.3
+ _ZL14MBLogUIOptionsPKcP15MenuBarInstancej.cold.4
+ _ZL15ConfiguredImageP7NSImage18NSImageSymbolScaledd.cold.1
+ _ZL15GetKeyFocusInfo11KeyFocusKeyPjPtS0_Ph.cold.1
+ _ZL15GetLocationMenuv.cold.1
+ _ZL15RemoveFromGroupP15WindowGroupDataPvh.cold.1
+ _ZL15TrackMenuCommonR14MenuSelectDataPhP13SelectionDataP10MenuResultS5_.cold.1
+ _ZL16AppleMenuHandlerP25OpaqueEventHandlerCallRefP14OpaqueEventRefPv.cold.1
+ _ZL17ActivationHandlerP25OpaqueEventHandlerCallRefP14OpaqueEventRefPv.cold.1
+ _ZL17ActivationHandlerP25OpaqueEventHandlerCallRefP14OpaqueEventRefPv.cold.2
+ _ZL17GetGlobalRegistryv.cold.1
+ _ZL18BringWindowToFrontP10WindowDataP13WindowContextP20OpaqueWindowGroupRefh.cold.1
+ _ZL18PushToCGEventQueueP9__CGEventjhP17__CFMachPortBoost.cold.1
+ _ZL18SearchCacheEntriesP16OpaqueCollectionjmP13CheckMenuDataP14MenuKeyResultsPP8MenuDataPm.cold.1
+ _ZL19AdjustFlushObserverPFvP11__CFRunLoopP19__CFRunLoopObserverPK10__CFStringE.cold.1
+ _ZL19IsLockScreenEnabledv.cold.1
+ _ZL19PopUpMenuSelectCoreP8MenuData5PointdS1_tjjPK4RecttjS4_S4_PK14__CFDictionaryPK10__CFStringPP13OpaqueMenuRefPt.cold.1
+ _ZL19PopUpMenuSelectCoreP8MenuData5PointdS1_tjjPK4RecttjS4_S4_PK14__CFDictionaryPK10__CFStringPP13OpaqueMenuRefPt.cold.2
+ _ZL19PopUpMenuSelectCoreP8MenuData5PointdS1_tjjPK4RecttjS4_S4_PK14__CFDictionaryPK10__CFStringPP13OpaqueMenuRefPt.cold.3
+ _ZL19PopUpMenuSelectCoreP8MenuData5PointdS1_tjjPK4RecttjS4_S4_PK14__CFDictionaryPK10__CFStringPP13OpaqueMenuRefPt.cold.4
+ _ZL19PopUpMenuSelectCoreP8MenuData5PointdS1_tjjPK4RecttjS4_S4_PK14__CFDictionaryPK10__CFStringPP13OpaqueMenuRefPt.cold.5
+ _ZL19PopUpMenuSelectCoreP8MenuData5PointdS1_tjjPK4RecttjS4_S4_PK14__CFDictionaryPK10__CFStringPP13OpaqueMenuRefPt.cold.6
+ _ZL19PopUpMenuSelectCoreP8MenuData5PointdS1_tjjPK4RecttjS4_S4_PK14__CFDictionaryPK10__CFStringPP13OpaqueMenuRefPt.cold.7
+ _ZL20MenuTrackingListenerjPvS_.cold.1
+ _ZL20ShowHideMBarListenerjPvS_.cold.1
+ _ZL20ShowHideMBarListenerjPvS_.cold.2
+ _ZL20SyncEventMonitorMaskv.cold.1
+ _ZL20init_NSGetAppKitMenuP13OpaqueMenuRef.cold.1
+ _ZL21Check1MenuForKeyEventP8MenuDataP13CheckMenuData.cold.1
+ _ZL21CheckMenusForKeyEventP8MenuDataP13CheckMenuData.cold.1
+ _ZL21CheckMenusForKeyEventP8MenuDataP13CheckMenuData.cold.2
+ _ZL21CheckMenusForKeyEventP8MenuDataP13CheckMenuData.cold.3
+ _ZL21CheckMenusForKeyEventP8MenuDataP13CheckMenuData.cold.4
+ _ZL21CreateElementFromDataPK8__CFDatajPPK13__AXUIElement.cold.1
+ _ZL21HideActiveBarIfNeededhh.cold.1
+ _ZL21initNSApplicationLoadv.cold.1
+ _ZL22AcquireCoalescingStackh.cold.1
+ _ZL22GetAndResolveProxyDataP10WindowDataPPP11AliasRecordP5FSRef.cold.1
+ _ZL22IsMatchingMenuKeyEventP8MenuDataP14OpaqueEventRefjhPS0_Pt.cold.1
+ _ZL22IsMatchingMenuKeyEventP8MenuDataP14OpaqueEventRefjhPS0_Pt.cold.2
+ _ZL22IsMatchingMenuKeyEventP8MenuDataP14OpaqueEventRefjhPS0_Pt.cold.3
+ _ZL22IsMatchingMenuKeyEventP8MenuDataP14OpaqueEventRefjhPS0_Pt.cold.4
+ _ZL22IsMatchingMenuKeyEventP8MenuDataP14OpaqueEventRefjhPS0_Pt.cold.5
+ _ZL22IsMatchingMenuKeyEventP8MenuDataP14OpaqueEventRefjhPS0_Pt.cold.6
+ _ZL22ReleaseCoalescingStackv.cold.1
+ _ZL23GetSpecialMenuMarkImageP8NSStringtd.cold.1
+ _ZL23ReleaseWindowsAndGroupsP15WindowGroupData.cold.1
+ _ZL24RegisterAsDockClientPrivv.cold.1
+ _ZL25PopulateWindowMenuHandlerP25OpaqueEventHandlerCallRefP14OpaqueEventRefPv.cold.1
+ _ZL25initTUIInputModeAccessoryv.cold.1
+ _ZL27initTUINSCursorUIControllerv.cold.1
+ _ZL28GetSpecialMenuMarkImageNamestRK15TThemeDrawStatejiPK10__CFStringPP7NSArrayIP8NSStringEPS4_.cold.1
+ _ZL28GetSpecialMenuMarkImageNamestRK15TThemeDrawStatejiPK10__CFStringPP7NSArrayIP8NSStringEPS4_.cold.2
+ _ZL28__CUICopyNamedColorConvertedPK10__CFString.cold.1
+ _ZL29initNetFSClearAllURLApprovalsv.cold.1
+ _ZL30CopyMenuWindowShadowParametersP10WindowDatahh.cold.1
+ _ZL31GetEventParameterAsPropertyListP14OpaqueEventRefjPK10__CFStringPKvPS5_Ph.cold.1
+ _ZL31GetEventParameterAsPropertyListP14OpaqueEventRefjPK10__CFStringPKvPS5_Ph.cold.2
+ _ZL33initTUIInputModeSwitcherAccessoryv.cold.1
+ _ZL39initHIS_XPC_CopyPrimaryKeyboardLanguagev.cold.1
+ _ZL5MBLogPKch.cold.1
+ _ZL5MBLogPKch.cold.2
+ _ZL5MBLogPKch.cold.3
+ _ZN10Accessible18PerformNamedActionEPK10__CFString.cold.1
+ _ZN10MBDisplays14DisplayChangedEjj.cold.1
+ _ZN10MBDisplays14GetNotchBoundsEj.cold.1
+ _ZN10MBDisplays17CreateDisplayDataEj.cold.1
+ _ZN10MBDisplays17CreateDisplayDataEj.cold.2
+ _ZN10MBDisplays17LogActiveDisplaysEv.cold.1
+ _ZN10MBDisplays19SafeApertureChangedE19CGSNotificationTypePvjS1_j.cold.1
+ _ZN10MBDisplays19SafeApertureChangedE19CGSNotificationTypePvjS1_j.cold.2
+ _ZN10MBDisplays19SafeApertureChangedE19CGSNotificationTypePvjS1_j.cold.3
+ _ZN10MBDisplays31InvalidateSafeApertureOnDisplayEjPKc.cold.1
+ _ZN10TTableView29GetItemAndPropertyOfSelectionEbPmS0_.cold.1
+ _ZN10WindowData16UpdateColorSpaceEh.cold.1
+ _ZN10WindowData18GetNSWindowManagerEv.cold.1
+ _ZN10WindowData24NSWindowConfiguresShadowEv.cold.1
+ _ZN10WindowData34GetAllAccessibleAttributeNamesSelfEyP9__CFArray.cold.1
+ _ZN11HIClockView11SetModifiedEbb.cold.1
+ _ZN11HIClockView19ClockAnimationTimerEP16__EventLoopTimerPv.cold.1
+ _ZN11HIClockView31GetNamedAccessibleAttributeSelfEyPK10__CFStringjP14OpaqueEventRef.cold.1
+ _ZN11HIClockView31GetNamedAccessibleAttributeSelfEyPK10__CFStringjP14OpaqueEventRef.cold.2
+ _ZN11HIClockView31GetNamedAccessibleAttributeSelfEyPK10__CFStringjP14OpaqueEventRef.cold.3
+ _ZN11HIClockView31GetNamedAccessibleAttributeSelfEyPK10__CFStringjP14OpaqueEventRef.cold.4
+ _ZN11HIClockView31GetNamedAccessibleAttributeSelfEyPK10__CFStringjP14OpaqueEventRef.cold.5
+ _ZN11HIClockView31SetNamedAccessibleAttributeSelfEyPK10__CFStringjP14OpaqueEventRef.cold.1
+ _ZN11TResizeTest11ResizeFrameEv.cold.1
+ _ZN11TypeManager20InstallStandardProcsEv.cold.1
+ _ZN12HIScrollView17BoundsChangedSelfEjRK6CGRectS2_.cold.1
+ _ZN12HITabbedView11GetDataSelfEjslPlPv.cold.1
+ _ZN12HITabbedView11GetDataSelfEjslPlPv.cold.2
+ _ZN12HITabbedView12SyncTabCountEs.cold.1
+ _ZN12HITabbedView19AcceptTextInputSelfEtjP14OpaqueEventRef.cold.1
+ _ZN12HITabbedView29GetAccessibleChildAtFocusSelfEyPPK13__AXUIElement.cold.1
+ _ZN12HITabbedView29GetAccessibleChildAtPointSelfEyRK7CGPointPPK13__AXUIElement.cold.1
+ _ZN12HITabbedView31GetNamedAccessibleAttributeSelfEyPK10__CFStringjP14OpaqueEventRef.cold.1
+ _ZN13CheckMenuData9AddResultER14MenuKeyResultsRK10MenuResulth.cold.1
+ _ZN13CheckMenuData9AddResultER14MenuKeyResultsRK10MenuResulth.cold.2
+ _ZN13HIApplication12EventHandlerEP25OpaqueEventHandlerCallRefP14OpaqueEventRefPv.cold.1
+ _ZN13HIBevelButton22BevelButtonMenuHandlerEP25OpaqueEventHandlerCallRefP14OpaqueEventRefPv.cold.1
+ _ZN13HIMenuBarView14LogTitleWidthsEi.cold.1
+ _ZN13HIMenuBarView17InitialTitleExtraEv.cold.1
+ _ZN13HIMenuBarView17InitialTitleExtraEv.cold.2
+ _ZN13HIMenuBarView17InitialTitleExtraEv.cold.3
+ _ZN13HIMenuBarView17InitialTitleExtraEv.cold.4
+ _ZN13HIMenuBarView17InitialTitleExtraEv.cold.5
+ _ZN13HIMenuBarView17InitialTitleExtraEv.cold.6
+ _ZN13HIMenuBarView18IdealExtraForWidthEfi.cold.1
+ _ZN13HIMenuBarView18MeasureTitleWidthsEv.cold.1
+ _ZN13HIMenuBarView19TruncateWidestTitleEv.cold.1
+ _ZN13HIMenuBarView19TruncateWidestTitleEv.cold.2
+ _ZN13HIMenuBarView19TruncateWidestTitleEv.cold.3
+ _ZN13HIMenuBarView20AttemptLayoutAtWidthEPff.cold.1
+ _ZN13HIMenuBarView20AttemptLayoutAtWidthEPff.cold.2
+ _ZN13HIMenuBarView20AttemptLayoutAtWidthEPff.cold.3
+ _ZN13HIMenuBarView20AttemptLayoutAtWidthEPff.cold.4
+ _ZN13HIMenuBarView22AttemptCondensingExtraEfiPf.cold.1
+ _ZN13HIMenuBarView22AttemptCondensingExtraEfiPf.cold.2
+ _ZN13HIMenuBarView22AttemptCondensingExtraEfiPf.cold.3
+ _ZN13HIMenuBarView22AttemptCondensingExtraEfiPf.cold.4
+ _ZN13HIMenuBarView22AttemptCondensingExtraEfiPf.cold.5
+ _ZN13HIMenuBarView23ReservedStatusItemSpaceEv.cold.1
+ _ZN13HIMenuBarView26ReallocateSpaceBeforeNotchEv.cold.1
+ _ZN13HIMenuBarView26ReallocateSpaceBeforeNotchEv.cold.2
+ _ZN13HIMenuBarView26ReallocateSpaceBeforeNotchEv.cold.3
+ _ZN13HIMenuBarView26ReallocateSpaceBeforeNotchEv.cold.4
+ _ZN13HIMenuBarView26ReallocateSpaceBeforeNotchEv.cold.5
+ _ZN13HIMenuBarView26ReallocateSpaceBeforeNotchEv.cold.6
+ _ZN13HIMenuBarView26ReallocateSpaceBeforeNotchEv.cold.7
+ _ZN13HIMenuBarView26ReallocateSpaceBeforeNotchEv.cold.8
+ _ZN13HIMenuBarView26ReallocateSpaceBeforeNotchEv.cold.9
+ _ZN13HIMenuBarView30AdjustBoundsForSmallTitleExtraEiP6CGRect.cold.1
+ _ZN13HIMenuBarView30AdjustBoundsForSmallTitleExtraEiP6CGRect.cold.2
+ _ZN13HIMenuBarView8DrawOnceE6CGRectS0_b23HIMenuBarTextAppearanceP9CGContext.cold.1
+ _ZN13HIMenuBarView8DrawOnceE6CGRectS0_b23HIMenuBarTextAppearanceP9CGContext.cold.2
+ _ZN13HIMenuBarView8DrawOnceE6CGRectS0_b23HIMenuBarTextAppearanceP9CGContext.cold.3
+ _ZN13HIMenuBarView8DrawOnceE6CGRectS0_b23HIMenuBarTextAppearanceP9CGContext.cold.4
+ _ZN13HIMenuBarView8DrawSelfEsPK9__HIShapeP9CGContext.cold.1
+ _ZN13HIMenuBarView9LogLayoutEv.cold.1
+ _ZN13HIMenuBarView9LogLayoutEv.cold.10
+ _ZN13HIMenuBarView9LogLayoutEv.cold.11
+ _ZN13HIMenuBarView9LogLayoutEv.cold.12
+ _ZN13HIMenuBarView9LogLayoutEv.cold.13
+ _ZN13HIMenuBarView9LogLayoutEv.cold.14
+ _ZN13HIMenuBarView9LogLayoutEv.cold.15
+ _ZN13HIMenuBarView9LogLayoutEv.cold.16
+ _ZN13HIMenuBarView9LogLayoutEv.cold.17
+ _ZN13HIMenuBarView9LogLayoutEv.cold.18
+ _ZN13HIMenuBarView9LogLayoutEv.cold.19
+ _ZN13HIMenuBarView9LogLayoutEv.cold.2
+ _ZN13HIMenuBarView9LogLayoutEv.cold.20
+ _ZN13HIMenuBarView9LogLayoutEv.cold.3
+ _ZN13HIMenuBarView9LogLayoutEv.cold.4
+ _ZN13HIMenuBarView9LogLayoutEv.cold.5
+ _ZN13HIMenuBarView9LogLayoutEv.cold.6
+ _ZN13HIMenuBarView9LogLayoutEv.cold.7
+ _ZN13HIMenuBarView9LogLayoutEv.cold.8
+ _ZN13HIMenuBarView9LogLayoutEv.cold.9
+ _ZN13HIObjectClass8RegisterEPK10__CFStringS2_jPFiP25OpaqueEventHandlerCallRefP14OpaqueEventRefPvEmPK13EventTypeSpecS7_PPS_.cold.1
+ _ZN13HIPopupButton11SetDataSelfEjslPKv.cold.1
+ _ZN13HIProgressBar7AnimateEv.cold.1
+ _ZN13HIToolbarItem11AddMenuItemEP13OpaqueMenuRefP15OpaqueWindowPtrPt.cold.1
+ _ZN14MenuElementRow10RemoveDataEPK10__CFString.cold.1
+ _ZN14MenuElementRow10RemoveDataEPK10__CFString.cold.2
+ _ZN14MenuElementRow10RemoveDataEPK10__CFString.cold.3
+ _ZN14MenuElementRow10RemoveDataEPK10__CFString.cold.4
+ _ZN14MenuElementRow10RemoveDataEPK10__CFString.cold.5
+ _ZN14MenuElementRow10RemoveDataEPK10__CFString.cold.6
+ _ZN14MenuElementRow10RemoveDataEPK10__CFString.cold.7
+ _ZN14MenuElementRow10RemoveDataEPK10__CFString.cold.8
+ _ZN14MenuKeyResults12ChooseResultEv.cold.1
+ _ZN14MenuKeyResults8HasMatchEv.cold.1
+ _ZN14MenuKeyResults9AddResultERK10MenuResulth.cold.1
+ _ZN15HIChasingArrows14AnimationTimerEv.cold.1
+ _ZN15MenuBarInstance14AppendSettingsEP9__CFArray.cold.1
+ _ZN15MenuBarInstance15ForEachWindowDoEhU13block_pointerFbP15OpaqueWindowPtrjE.cold.1
+ _ZN15MenuBarInstance18HandleAutoShowHideEv.cold.1
+ _ZN15MenuBarInstance18HandleAutoShowHideEv.cold.2
+ _ZN15MenuBarInstance21UpdateAggregateUIModeE21MenuBarAnimationStylehhh.cold.1
+ _ZN15MenuBarInstance23GetMBarHeightForDisplayEjj.cold.1
+ _ZN15MenuBarInstance24UpdateAutoShowVisibilityE5Pointh.cold.1
+ _ZN15MenuBarInstance24UpdateAutoShowVisibilityE5Pointh.cold.2
+ _ZN15MenuBarInstance28SetBoundsAndUpdateResolutionEh.cold.1
+ _ZN16HIStaticTextView31GetNamedAccessibleAttributeSelfEyPK10__CFStringjP14OpaqueEventRef.cold.1
+ _ZN17HIWindowFrameView10InitializeEP14OpaqueEventRef.cold.1
+ _ZN17HIWindowFrameView12EventHandlerEP25OpaqueEventHandlerCallRefP14OpaqueEventRefPv.cold.1
+ _ZN18HIMenuBarFrameView10InitializeEP14OpaqueEventRef.cold.1
+ _ZN18HIStandardMenuView10InitializeEP14OpaqueEventRef.cold.1
+ _ZN18HIStandardMenuView11MenuHandlerEP25OpaqueEventHandlerCallRefP14OpaqueEventRefPv.cold.1
+ _ZN18HIStandardMenuView14EnsureBackdropEPK6CGRectj.cold.1
+ _ZN18HIStandardMenuView15DrawItemContentEPK6CGRectS2_ffjsP9CGContextP20OpaqueCUIRendererRef.cold.1
+ _ZN18HIStandardMenuView16AddVibrantBoundsEPK6CGRect.cold.1
+ _ZN18HIStandardMenuView17PositionItemViewsEv.cold.1
+ _ZN18HIStandardMenuView22MeasureCmdKeyModifiersEjtPK8__CTFonthiP10TextLayout.cold.1
+ _ZN18HIStandardMenuView25HasMirroredKeyboardLayoutEv.cold.1
+ _ZN18HIStandardMenuView25HasMirroredKeyboardLayoutEv.cold.2
+ _ZN18HIStandardMenuView8DrawItemEhP9CGContexth.cold.1
+ _ZN18HIStandardMenuView8DrawSelfEsPK9__HIShapeP9CGContext.cold.1
+ _ZN21PersistentWindowState27CreatePersistentWindowStateEP10WindowData.cold.1
+ _ZN6HIView10InvalidateEP15OpaqueRgnHandle.cold.1
+ _ZN6HIView11GetVisAboveEv.cold.1
+ _ZN6HIView12EventHandlerEP25OpaqueEventHandlerCallRefP14OpaqueEventRefPv.cold.1
+ _ZN6HIView12EventHandlerEP25OpaqueEventHandlerCallRefP14OpaqueEventRefPv.cold.2
+ _ZN6HIView12EventHandlerEP25OpaqueEventHandlerCallRefP14OpaqueEventRefPv.cold.3
+ _ZN6HIView12EventHandlerEP25OpaqueEventHandlerCallRefP14OpaqueEventRefPv.cold.4
+ _ZN6HIView12EventHandlerEP25OpaqueEventHandlerCallRefP14OpaqueEventRefPv.cold.5
+ _ZN6HIView12EventHandlerEP25OpaqueEventHandlerCallRefP14OpaqueEventRefPv.cold.6
+ _ZN6HIView12EventHandlerEP25OpaqueEventHandlerCallRefP14OpaqueEventRefPv.cold.7
+ _ZN6HIView12EventHandlerEP25OpaqueEventHandlerCallRefP14OpaqueEventRefPv.cold.8
+ _ZN6HIView12EventHandlerEP25OpaqueEventHandlerCallRefP14OpaqueEventRefPv.cold.9
+ _ZN6HIView16ReshapeStructureEv.cold.1
+ _ZN6HIView16ScrollToLocationERK7CGPoint.cold.1
+ _ZN6HIView18CopyClickableShapeEv.cold.1
+ _ZN6HIView20CreateOffscreenImageEP6CGRectd.cold.1
+ _ZN6HIView20CreateOffscreenImageEP6CGRectd.cold.2
+ _ZN6HIView20CreateOffscreenImageEP6CGRectd.cold.3
+ _ZN6HIView20CreateOffscreenImageEP6CGRectd.cold.4
+ _ZN6HIView22DecodeEmbeddedSubviewsEP18OpaqueHIArchiveRef.cold.1
+ _ZN6HIView24InvalidateForOrderChangeEbPS_.cold.1
+ _ZN6HIView25CopyCommandClickableShapeEv.cold.1
+ _ZN6HIView32InvalidateForSizeChangeOptimallyERK6CGRectS2_.cold.1
+ _ZN6HIView9RecalcVisEv.cold.1
+ _ZN6TTheme15ToolboxListenerEjPvS0_.cold.1
+ _ZN8HISlider22HandleStateChangedHookEP25OpaqueEventHandlerCallRefP14OpaqueEventRefPv.cold.1
+ _ZN8HISlider22HandleStateChangedHookEP25OpaqueEventHandlerCallRefP14OpaqueEventRefPv.cold.2
+ _ZN8RowStore10RemoveDataElPK10__CFString.cold.1
+ _ZN9MBWindows12CreateWindowE6CGRectj.cold.1
+ _ZN9TDelegate11HandleEventEP25OpaqueEventHandlerCallRefR12TCarbonEvent.cold.1
+ _ZN9TDelegate11HandleEventEP25OpaqueEventHandlerCallRefR12TCarbonEvent.cold.2
+ _ZN9TDelegate11HandleEventEP25OpaqueEventHandlerCallRefR12TCarbonEvent.cold.3
+ _ZN9TListView15RowGetAttributeERKNS_15AccessibilityIDEPK10__CFStringjP14OpaqueEventRef.cold.1
+ _ZN9TListView19OutlineSetAttributeERKNS_15AccessibilityIDEPK10__CFStringjP14OpaqueEventRef.cold.1
+ _ZN9TListView19OutlineSetAttributeERKNS_15AccessibilityIDEPK10__CFStringjP14OpaqueEventRef.cold.2
+ _ZNK10MenuResult3LogEPKc.cold.1
+ _ZNK10MenuResult3LogEPKc.cold.2
+ _ZNK10MenuResult3LogEPKc.cold.3
+ _ZNK10MenuResult3LogEPKc.cold.4
+ __21+[IMKClient subclass]_block_invoke.cold.1
+ __27+[IMKInputSession subclass]_block_invoke.cold.1
+ __34-[IMKInputSession_Modern activate]_block_invoke_2.cold.1
+ __36-[IMKInputSession_Modern deactivate]_block_invoke_3.cold.1
+ __42-[IMKInputSession_Modern setValue:forTag:]_block_invoke_3.cold.1
+ __43+[IMKInputSession_Legacy IMKCFRunLoopSetup]_block_invoke.cold.1
+ __43-[IMKInputSession_Modern commitComposition]_block_invoke_3.cold.1
+ __55-[IMKInputSession_Legacy _eventIsOn:completionHandler:]_block_invoke.765
+ __55-[IMKInputSession_Legacy _eventIsOn:completionHandler:]_block_invoke.781
+ __55-[IMKInputSession_Legacy _eventIsOn:completionHandler:]_block_invoke_2.769
+ __55-[IMKInputSession_Legacy _eventIsOn:completionHandler:]_block_invoke_2.782
+ __55-[IMKInputSession_Modern _eventIsOn:completionHandler:]_block_invoke.612
+ __55-[IMKInputSession_Modern _eventIsOn:completionHandler:]_block_invoke.628
+ __55-[IMKInputSession_Modern _eventIsOn:completionHandler:]_block_invoke_2.616
+ __55-[IMKInputSession_Modern _eventIsOn:completionHandler:]_block_invoke_2.629
+ __55-[IMKInputSession_Modern _eventIsOn:completionHandler:]_block_invoke_3.cold.1
+ __56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke.419
+ __56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke.432
+ __56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke.440
+ __56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke.465
+ __56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke.cold.1
+ __56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke_2.420
+ __56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke_2.420.cold.1
+ __56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke_2.434
+ __56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke_2.442
+ __56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke_2.442.cold.1
+ __56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke_2.457
+ __56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke_3.435
+ __56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke_3.446
+ __56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke_4.436
+ __56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke_4.450
+ __56-[IMKInputSession_Legacy valueForTag:completionHandler:]_block_invoke.598
+ __56-[IMKInputSession_Legacy valueForTag:completionHandler:]_block_invoke.611
+ __56-[IMKInputSession_Legacy valueForTag:completionHandler:]_block_invoke_2.602
+ __56-[IMKInputSession_Legacy valueForTag:completionHandler:]_block_invoke_2.612
+ __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke.288
+ __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke.301
+ __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke.306
+ __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke.311
+ __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke.322
+ __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke.334
+ __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke.335
+ __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke.cold.1
+ __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke_2.289
+ __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke_2.289.cold.1
+ __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke_2.303
+ __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke_2.307
+ __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke_2.313
+ __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke_2.313.cold.1
+ __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke_2.326
+ __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke_2.336
+ __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke_2.336.cold.1
+ __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke_3.314
+ __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke_4.319
+ __56-[IMKInputSession_Modern valueForTag:completionHandler:]_block_invoke.459
+ __56-[IMKInputSession_Modern valueForTag:completionHandler:]_block_invoke.470
+ __56-[IMKInputSession_Modern valueForTag:completionHandler:]_block_invoke_2.463
+ __56-[IMKInputSession_Modern valueForTag:completionHandler:]_block_invoke_2.471
+ __56-[IMKInputSession_Modern valueForTag:completionHandler:]_block_invoke_3.cold.1
+ __60-[IMKInputSession_Legacy stringFromRange:completionHandler:]_block_invoke.1413
+ __60-[IMKInputSession_Modern stringFromRange:completionHandler:]_block_invoke.1264
+ __64-[IMKInputSession_Modern doCommandBySelector:commandDictionary:]_block_invoke_3.cold.1
+ __65-[IMKInputSession_Legacy didCommandBySelector:completionHandler:]_block_invoke.680
+ __65-[IMKInputSession_Legacy didCommandBySelector:completionHandler:]_block_invoke_2.681
+ __65-[IMKInputSession_Modern didCommandBySelector:completionHandler:]_block_invoke.532
+ __65-[IMKInputSession_Modern didCommandBySelector:completionHandler:]_block_invoke_2.533
+ __65-[IMKInputSession_Modern didCommandBySelector:completionHandler:]_block_invoke_3.534
+ __65-[IMKInputSession_Modern didCommandBySelector:completionHandler:]_block_invoke_3.534.cold.1
+ __67+[IMKClient_Modern(IMKClientConnection_XPC) imExtensionBundlePaths]_block_invoke_2.84.cold.1
+ __77-[IMKInputSession_Legacy _createAndSendOffsetToPointEvent:completionHandler:]_block_invoke.cold.1
+ __77-[IMKInputSession_Modern _createAndSendOffsetToPointEvent:completionHandler:]_block_invoke.cold.1
+ __79-[IMKInputSession_Legacy _updateIMKMarkedRange:markedLength:completionHandler:]_block_invoke.796
+ __79-[IMKInputSession_Legacy _updateIMKMarkedRange:markedLength:completionHandler:]_block_invoke.802
+ __79-[IMKInputSession_Modern _updateIMKMarkedRange:markedLength:completionHandler:]_block_invoke.645
+ __79-[IMKInputSession_Modern _updateIMKMarkedRange:markedLength:completionHandler:]_block_invoke.651
+ __84-[IMKInputSession_Legacy attributesForCharacterIndex_andLineRect:completionHandler:]_block_invoke.cold.1
+ __84-[IMKInputSession_Modern attributesForCharacterIndex_andLineRect:completionHandler:]_block_invoke.cold.1
+ __85-[IMKInputSession_Legacy _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke.cold.1
+ __85-[IMKInputSession_Legacy _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_10.cold.1
+ __85-[IMKInputSession_Legacy _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_14.cold.1
+ __85-[IMKInputSession_Legacy _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_6.cold.1
+ __85-[IMKInputSession_Modern _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke.cold.1
+ __85-[IMKInputSession_Modern _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_10.cold.1
+ __85-[IMKInputSession_Modern _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_14.cold.1
+ __85-[IMKInputSession_Modern _coreAttributesFromRange:whichAttributes:completionHandler:]_block_invoke_6.cold.1
+ __86-[IMKInputSession_Legacy _copyUniCharsForRange:intoBuffer:ofLength:completionHandler:]_block_invoke.cold.1
+ __86-[IMKInputSession_Modern _copyUniCharsForRange:intoBuffer:ofLength:completionHandler:]_block_invoke.cold.1
+ __Block_byref_object_copy_.1120
+ __Block_byref_object_copy_.1269
+ __Block_byref_object_copy_.1341
+ __Block_byref_object_dispose_.1121
+ __Block_byref_object_dispose_.1270
+ __Block_byref_object_dispose_.1342
+ __CreateSourceIndicatorInfoForTISwitcher_WithCompletionHandler_block_invoke.cold.1
+ __IsAppKitMenuSystemEnabled_block_invoke.cold.1
+ __MergedGlobals
+ __ProcessDeadKeyInlineSession_WithCompletionHandler_block_invoke.cold.1
+ __ProcessDeadKeyInlineSession_WithCompletionHandler_block_invoke.cold.2
+ __SetMenuBarObscured_block_invoke.cold.1
+ __SetPhysicalKeyboardCapsLockDelayOverride_block_invoke.cold.1
+ __Z10client_logv
+ __ZL13GetRecentMenuv
+ __ZL14IsSleepEnabledv
+ __ZL14SwitchLocationP13OpaqueMenuReft
+ __ZL15ConfiguredImageP7NSImage18NSImageSymbolScaledd
+ __ZL15GetLocationMenuv
+ __ZL16ClearRecentItemsP13OpaqueMenuRef
+ __ZL18UpdateAppStoreItemP13OpaqueMenuRef
+ __ZL21UpdateStartupDiskItemP13OpaqueMenuRef
+ __ZL22UpdateAboutThisMacItemP13OpaqueMenuRef
+ __ZL24ShouldDisplayRecentsMenuv
+ __ZL24UpdateSystemSettingsItemP13OpaqueMenuRef
+ __ZL25ShouldDisplayLocationMenuv
+ __ZL27SafelyFindCGSWindowAndOwnerjj10CGSOrderOpbPK7CGPointPS0_PjS4_
+ __ZL30ReservedStatusItemSpaceChanged19CGSNotificationTypePvjS0_j
+ __ZN10MBDisplays18ActiveSpaceChangedE19CGSNotificationTypePvjS1_j
+ __ZN10MBDisplays19SafeApertureChangedE19CGSNotificationTypePvjS1_j
+ __ZN10WindowData13OrderNSWindowE10CGSOrderOpj
+ __ZZ10client_logvE3log
+ __ZZ10client_logvE9onceToken
+ __ZZL24GetSubstituteColorCursorjE11sCursorSubs
+ ___ISGetCapsLockModifierState_block_invoke.cold.1
+ ___ISSetPhysicalKeyboardCapsLockLED_block_invoke.cold.1
+ ___ZL11SearchCacheP16OpaqueCollectionbbP13CheckMenuDataP14MenuKeyResults_block_invoke.42.cold.1
+ ___ZL11SearchCacheP16OpaqueCollectionbbP13CheckMenuDataP14MenuKeyResults_block_invoke.46.cold.1
+ ___ZL11SearchCacheP16OpaqueCollectionbbP13CheckMenuDataP14MenuKeyResults_block_invoke_2.cold.1
+ ___ZN10MBDisplays17LogActiveDisplaysEv_block_invoke.cold.1
+ ___ZN15MenuBarInstance14AppendSettingsEP9__CFArray_block_invoke.cold.1
+ ___ZN15MenuBarInstance28SetBoundsAndUpdateResolutionEh_block_invoke.cold.1
+ ____Z10client_logv_block_invoke
+ ____ZN10MBDisplays18ActiveSpaceChangedE19CGSNotificationTypePvjS1_j_block_invoke
+ ____ZN10WindowData13OrderNSWindowE10CGSOrderOpj_block_invoke
+ __block_literal_global.1099
+ __block_literal_global.1106
+ __block_literal_global.1113
+ __block_literal_global.1118
+ __block_literal_global.1250
+ __block_literal_global.1257
+ __block_literal_global.1262
+ __block_literal_global.1267
+ __block_literal_global.1932
+ __block_literal_global.378
+ __block_literal_global.517
+ __block_literal_global.598
+ __block_literal_global.751
+ __send_doublekeypress_event_block_invoke.cold.1
+ __utOpenIM4Document_block_invoke.cold.1
+ __utSetupInputMethodMenuFromDeferredBlock_block_invoke.cold.1
+ __utTryToSetupInputMethodMenu_block_invoke.50.cold.1
+ _atan
+ checkForSlug.cold.1
+ initanalytics_send_event.cold.1
+ isCreateCurrentKeyboardInputSourceRef.cold.1
+ isPrefsCreateCacheFromEnabledAndDefaultInputSources.cold.1
+ isPrefsCreateEnabledInputSourcePrefsSnapshot.cold.1
+ isPrefsCreateEnabledInputSourcePrefsSnapshot.cold.2
+ islCreateInputModeInvisible.cold.1
+ islCreateInputModeIsSelectable_Common.cold.1
+ islCreateNonExistentInputSourcePrefsDescriptor.cold.1
+ islCreateResyncPasteboardInputSourcePrefsDescriptor.cold.1
+ islGetFnUsageType.cold.1
+ islGetInputSourceBundleID.cold.1
+ islGetInputSourceBundleID.cold.2
+ islGetInputSourceCapsLockIsSwitch.cold.1
+ islGetInputSourceCapsLockIsSwitchToRomanMode.cold.1
+ islGetInputSourceCapsLockResetOnModeSwitch.cold.1
+ islGetInputSourceDoubleSpaceSubstitution.cold.1
+ islGetInputSourceIconLabels.cold.1
+ islGetInputSourceInputKind.cold.1
+ islGetInputSourceInputKind.cold.2
+ islGetInputSourceInputMode.cold.1
+ islGetInputSourceInputMode.cold.2
+ islGetInputSourceInputSourceID.cold.1
+ islGetInputSourceListWithAdditions.cold.2
+ islGetInputSourceListWithAdditions.cold.3
+ islGetInputSourceLocalePartsForPreferred.cold.1
+ islGetInputSourceLocaleString.cold.1
+ islGetInputSourceOverrideCapsLockDelay.cold.1
+ islGetInputSourceParticipatesInTouchBar.cold.1
+ islGetInputSourceProperty.cold.1
+ islcCreateCapsLockResetOnModeSwitchFromCacheElem.cold.1
+ islcCreateCapsLockSwitchToIMRomanModeFromCacheElem.cold.1
+ islcCreateInputKindFromCacheElem.cold.1
+ islcCreateInputMethodArchFromCacheElem.cold.1
+ islcCreateInputModeFromCacheElem.cold.1
+ islcCreateParticipatesInTouchBarFromCacheElem.cold.1
+ islcGetInputTISTypeFromCacheElem.cold.1
+ showHideLog.cold.1
- CheckNonMigratedDictationAutoEnable.sCheckSpeechPref
- CheckNonMigratedDictationAutoEnable.sDetermined
- CreateEvent.firstEvent
- DefaultAsciiKeyboardLayoutGetPasteboard.sDefaultAsciiKeyboardLayoutPasteboard
- EventIsTSMKeyTest.sIsTextFilterInstalled
- EventIsTSMKeyTest.sTextFilterEventHandlerRef
- GCC_except_table123
- GetCapsLockPressAndHoldModifiers.sCapsLockPressAndHoldModifiersDetermined
- GetCapsLockPressAndHoldModifiers.sCapsLockPressAndHoldModsCGFlagsState
- GetDoubleTapModsPref.sDetermined
- GetDoubleTapModsPref.sModifiers
- GetIronwoodModOnlyTapPref.sDetermined
- GetIronwoodModOnlyTapPref.sModOnlyTap
- GetTapOnlyModsPref.sDetermined
- GetTapOnlyModsPref.sModifiers
- GetTimerRefTable.sTable
- InputSourceHistoryGetPasteboard.sInputSourceHistoryPasteboard
- InputSourcesInUIOrderGetPasteboard.sInputSourcesInUIOrderPasteboard
- IsCapsLockKeyDetectionEnabled.isCapsLockKeyDetectionEnabled
- IsCapsLockKeyDetectionEnabled.sDetermined
- IsCharacterOKForPressAndHold.sPressAndHoldExclusionSet
- IsOKToUseAssistiveTouch.sDetermined
- IsOKToUseIronwood.isOKToUseIronwood
- IsOKToUseIronwood.sDetermined
- IsOKToUsePressAndHold.sDetermined
- IsTISTracingCacheRebuild.sDetermined
- IsTSMTracingAssistiveTouch.sAssistiveTouchTracing
- IsTSMTracingAssistiveTouch.sAssistiveTouchTracingDetermined
- IsTSMTracingCapsLockPressAndHold.sIronwoodTracing
- IsTSMTracingCapsLockPressAndHold.sIronwoodTracingDetermined
- IsTSMTracingDocumentProperties.sDocPropertyTracing
- IsTSMTracingDocumentProperties.sDocPropertyTracingDetermined
- IsTSMTracingForAsyncClient.sAsyncTracing
- IsTSMTracingForAsyncClient.sAsyncTracingDetermined
- IsTSMTracingInputSourceNotifications.sNotificationTracing
- IsTSMTracingInputSourceNotifications.sNotificationTracingDetermined
- IsTSMTracingInputSourceSelection.sSelectionTracing
- IsTSMTracingInputSourceSelection.sSelectionTracingDetermined
- IsTSMTracingIronwood.sIronwoodTracing
- IsTSMTracingIronwood.sIronwoodTracingDetermined
- IsTSMTracingPressAndHold.sPressAndHoldTracing
- IsTSMTracingPressAndHold.sPressAndHoldTracingDetermined
- IsTracingTSMEvents.sEventTracing
- IsTracingTSMEvents.sEventTracingDetermined
- KeyboardLayoutOverrideGetPasteboard.sKBOverridePasteboard
- PerContextInputGetPasteboard.sPerContextInputPasteboard
- ProcessInputSourceSwitchEventCandidate.sInputSourceSwitchContext
- ProcessInputSourceSwitchEventCandidate.sPreviousCGSEventModifiers
- ProcessInputSourceSwitchEventCandidate.sPreviousEventModifiers
- SMHandleAppActivatedEvent.sSMHandleAppActivatedEventLevel
- TSMDisableInputSource_Internal.cold.1
- TSMEnableInputSource_Internal.cold.1
- TSMTracingEvents.sTracing
- TSMTracingEvents.sTracingDetermined
- _ZZ22CreateEventWithCGEventE23sMomentumGlobalLocation.0
- _ZZ22CreateEventWithCGEventE23sMomentumGlobalLocation.1
- __55-[IMKInputSession_Legacy _eventIsOn:completionHandler:]_block_invoke.814
- __55-[IMKInputSession_Legacy _eventIsOn:completionHandler:]_block_invoke.830
- __55-[IMKInputSession_Legacy _eventIsOn:completionHandler:]_block_invoke_2.818
- __55-[IMKInputSession_Legacy _eventIsOn:completionHandler:]_block_invoke_2.831
- __55-[IMKInputSession_Modern _eventIsOn:completionHandler:]_block_invoke.663
- __55-[IMKInputSession_Modern _eventIsOn:completionHandler:]_block_invoke.679
- __55-[IMKInputSession_Modern _eventIsOn:completionHandler:]_block_invoke_2.667
- __55-[IMKInputSession_Modern _eventIsOn:completionHandler:]_block_invoke_2.680
- __56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke.431
- __56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke.478
- __56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke.479
- __56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke_2.432
- __56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke_2.455
- __56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke_2.470
- __56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke_3.447
- __56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke_3.459
- __56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke_4.449
- __56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke_4.463
- __56-[IMKInputSession_Legacy valueForTag:completionHandler:]_block_invoke.623
- __56-[IMKInputSession_Legacy valueForTag:completionHandler:]_block_invoke.636
- __56-[IMKInputSession_Legacy valueForTag:completionHandler:]_block_invoke_2.627
- __56-[IMKInputSession_Legacy valueForTag:completionHandler:]_block_invoke_2.637
- __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke.300
- __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke.321
- __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke.326
- __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke.337
- __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke.349
- __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke.350
- __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke_2.301
- __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke_2.322
- __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke_2.328
- __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke_2.341
- __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke_2.351
- __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke_3.316
- __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke_3.329
- __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke_4.318
- __56-[IMKInputSession_Modern handleEvent:completionHandler:]_block_invoke_4.334
- __56-[IMKInputSession_Modern valueForTag:completionHandler:]_block_invoke.486
- __56-[IMKInputSession_Modern valueForTag:completionHandler:]_block_invoke.497
- __56-[IMKInputSession_Modern valueForTag:completionHandler:]_block_invoke_2.490
- __56-[IMKInputSession_Modern valueForTag:completionHandler:]_block_invoke_2.498
- __60-[IMKInputSession_Legacy stringFromRange:completionHandler:]_block_invoke.1483
- __60-[IMKInputSession_Modern stringFromRange:completionHandler:]_block_invoke.1336
- __65-[IMKInputSession_Legacy didCommandBySelector:completionHandler:]_block_invoke.711
- __65-[IMKInputSession_Legacy didCommandBySelector:completionHandler:]_block_invoke_2.712
- __65-[IMKInputSession_Modern didCommandBySelector:completionHandler:]_block_invoke.565
- __65-[IMKInputSession_Modern didCommandBySelector:completionHandler:]_block_invoke_2.566
- __65-[IMKInputSession_Modern didCommandBySelector:completionHandler:]_block_invoke_3.567
- __79-[IMKInputSession_Legacy _updateIMKMarkedRange:markedLength:completionHandler:]_block_invoke.848
- __79-[IMKInputSession_Legacy _updateIMKMarkedRange:markedLength:completionHandler:]_block_invoke.854
- __79-[IMKInputSession_Modern _updateIMKMarkedRange:markedLength:completionHandler:]_block_invoke.699
- __79-[IMKInputSession_Modern _updateIMKMarkedRange:markedLength:completionHandler:]_block_invoke.705
- __Block_byref_object_copy_.1264
- __Block_byref_object_copy_.1339
- __Block_byref_object_copy_.1411
- __Block_byref_object_dispose_.1265
- __Block_byref_object_dispose_.1340
- __Block_byref_object_dispose_.1412
- __ZGVZ34_SystemUIModeFromProcessAttributesE4refs
- __ZGVZL30CopyMenuWindowShadowParametersP10WindowDatahhE4keys
- __ZGVZN15MenuBarInstance21UpdateAggregateUIModeE21MenuBarAnimationStylehhhE5kKeys
- __ZL10sAppUIMode
- __ZL10sQuickMode
- __ZL11sFocusStack
- __ZL11sTierGroups
- __ZL12sCGEventLock
- __ZL12sCGEventLoop
- __ZL12sFocusTokens
- __ZL12sMasterValid
- __ZL12sMonitorPort
- __ZL13gNextMenuTime
- __ZL13sAppUIOptions
- __ZL13sExitTimerRef
- __ZL13sPlatformMask
- __ZL13sResizeHotKey
- __ZL14sCustomAppMenu
- __ZL14sKbdAccessMode
- __ZL14sLiveMenuValid
- __ZL14sMonitorSource
- __ZL15ConfiguredImageP7NSImageldd
- __ZL15gInMenuTracking
- __ZL15gNextMenuResult
- __ZL15gThemeFontCache
- __ZL15sActivationSeed
- __ZL15sCurrentHelpTag
- __ZL15sIronwoodHotKey
- __ZL15sKeyFocusStolen
- __ZL15sLiveWindowMenu
- __ZL15sLogTransitions
- __ZL15sRestoringState
- __ZL15sShowHelpString
- __ZL16gNextMenuOptions
- __ZL16sDebugAnimations
- __ZL16sModalStateCount
- __ZL16sPreservingState
- __ZL16sUnifiedMenuList
- __ZL17gNextMenuLocation
- __ZL17sAppleMenuHandler
- __ZL17sHasCustomAppMenu
- __ZL17sHelpContentIndex
- __ZL17sLastMouseCGEvent
- __ZL17sMenuForRendering
- __ZL17sRestoringAtLogin
- __ZL18__kHIArchiveTypeID
- __ZL18gNextExclusionRect
- __ZL18sKbdModePrefsValid
- __ZL18sMenuBarRegistered
- __ZL18sMonitorConnection
- __ZL18sSharedTSMDocument
- __ZL19sAutoShowAppHandler
- __ZL19sDocumentsToRestore
- __ZL19sIgnoreNextActivate
- __ZL20sCUIShowPiecesHotKey
- __ZL20sDebugAnimationSteps
- __ZL20sDebugAnimationsDone
- __ZL20sDrawMenuItemOptions
- __ZL21gNextMenuOptionsValid
- __ZL21sAsyncTransitionCount
- __ZL21sLiveMenuNeedsHandler
- __ZL22sDebugWindowListHotKey
- __ZL23gNextMenuResultRootMenu
- __ZL23sFlushObserverInstalled
- __ZL23sMouseButtonStatesValid
- __ZL23sRestoreWindowIDMapping
- __ZL24gNextMenuResultModifiers
- __ZL24sCGEventEnqueueingFilter
- __ZL25sCGEventConsumedUserEvent
- __ZL25sCUIShowInputBoundsHotKey
- __ZL25sRotatableDocumentWindows
- __ZL25sRotatableFloatingWindows
- __ZL26sAnimStyleForPreventedHide
- __ZL26sDebugAnimationCurrentStep
- __ZL26sEnteringFullScreenDisplay
- __ZL26sPreventHidingMenuBarCount
- __ZL26sShowHideHandwritingHotKey
- __ZL27SafelyFindCGSWindowAndOwnerjjibPK7CGPointPS_PjS3_
- __ZL27gHIArchiveTypeIDInitialized
- __ZL27sDebugAnimationsStepChanged
- __ZL27sMenuBarPositionLockCounter
- __ZL27sMenuBarPreventedFromHiding
- __ZL29sHelpPreviewHandlerDictionary
- __ZL30ReservedStatusItemSpaceChangedjPvjS_j
- __ZL46sModalStateAllowModalLevelZeroEquivalenceCount
- __ZL48sToolboxEventNotifyDoubleTapModifierInvalidation
- __ZL9gProcList
- __ZL9sHelpMenu
- __ZL9sProcLock
- __ZN10MBDisplays18ActiveSpaceChangedEjPvjS0_j
- __ZN10MBDisplays19SafeApertureChangedEjPvjS0_j
- __ZN10WindowData13OrderNSWindowEij
- __ZN15TCoreTextEngine27GetTextInfoOutputParametersEP16THIThemeTextInfo
- __ZZ11showHideLogE4sLog
- __ZZ11showHideLogE5sOnce
- __ZZ13_GetAppleMenuE10sAppleMenu
- __ZZ14CondenseByFontvE5sOnce
- __ZZ14CondenseByFontvE7sResult
- __ZZ14CondenseByJustvE5sOnce
- __ZZ14CondenseByJustvE7sResult
- __ZZ21EnableSmallTitleExtravE5sOnce
- __ZZ21EnableSmallTitleExtravE7sResult
- __ZZ21HIThemeDrawBackgroundE17sPlasticImageTall
- __ZZ21HIThemeDrawBackgroundE18sPlasticImageSmall
- __ZZ22CreateEventWithCGEventE11sDeactivate
- __ZZ22CreateEventWithCGEventE15sMomentumWindow
- __ZZ22CreateEventWithCGEventE23sMomentumWindowLocation
- __ZZ22CreateEventWithCGEventE25sMomentumScrollInProgress
- __ZZ22CreateEventWithCGEventE9sActivate
- __ZZ22ShowPressedImageBoundsvE5sOnce
- __ZZ22ShowPressedImageBoundsvE7sResult
- __ZZ23_HIMenuCopyNewItemsTextE13sAlertsFormat
- __ZZ23_HIMenuCopyNewItemsTextE14sUpdatesFormat
- __ZZ23_HIMenuCopyNewItemsTextE15sNewItemsFormat
- __ZZ25HIThemeDrawTitleBarWidgetE18sAdjustForAdobeOwl
- __ZZ25HIThemeDrawTitleBarWidgetE31sCheckedShouldAdjustForAdobeOwl
- __ZZ25IsAppKitMenuSystemEnabledE5sOnce
- __ZZ25IsAppKitMenuSystemEnabledE8sEnabled
- __ZZ27_EnsureFirstMenuTimeActionsE21sFirstMenuTimeActions
- __ZZ28WindowStateSetRestoringStatehE24sDidFinishRestoringState
- __ZZ28_HIThemeDrawBevelButtonInsetPK6CGRectPK21HIThemeButtonDrawInfoP9CGContextjPS_E13sPressedGrays
- __ZZ28_HIThemeDrawBevelButtonInsetPK6CGRectPK21HIThemeButtonDrawInfoP9CGContextjPS_E14sDisabledGrays
- __ZZ28_HIThemeDrawBevelButtonInsetPK6CGRectPK21HIThemeButtonDrawInfoP9CGContextjPS_E6sGrays
- __ZZ30GetTextAndEncodingFromCFStringE9converter
- __ZZ34_HIThemeGetDefaultMenuItemFontSizeE24sDefaultMenuItemFontSize
- __ZZ34_SystemUIModeFromProcessAttributesE4refs
- __ZZ54-[IMKInputSession_Legacy validAttributesForMarkedText]E8theArray
- __ZZ54-[IMKInputSession_Modern validAttributesForMarkedText]E8theArray
- __ZZL11PopupClientvE5sOnce
- __ZZL11PopupClientvE7sClient
- __ZZL13GetModalStackvE6sStack
- __ZZL13GetTierLevelsvE7sLevels
- __ZZL14MBarViewClientvE5sOnce
- __ZZL14MBarViewClientvE7sClient
- __ZZL15FirstWindowTimevE5sOnce
- __ZZL16UIMenuSystemMainvE15sMainMenuSystem
- __ZZL16UIMenuSystemMainvE5sOnce
- __ZZL17SetupMenuTrackingR14MenuSelectDatah5PointdP8MenuDatajtPK4RectS6_PK14__CFDictionaryjjS6_PK10__CFStringE28sMenuTrackingModeInitialized
- __ZZL18CoalesceMouseEventP14OpaqueEventRefE18sLastTabletButtons
- __ZZL19CreateHelpTagWindowP7HelpTagE19sOpaqueContentColor
- __ZZL19CreateHelpTagWindowP7HelpTagE21sBackdropContentColor
- __ZZL20CoalesceMouseCGEventP9__CGEventjE18sLastTabletButtons
- __ZZL20SetWindowGroupForTagP15OpaqueWindowPtriE14sHelpTagGroups
- __ZZL21GetHLEventObserverUPPvE4sUPP
- __ZZL23GetWindowMenuMasterListPP13OpaqueMenuRefE8windMenu
- __ZZL23InitContextualMenuStuffvE7sInited
- __ZZL24GetSystemCharFallbackUPPvE12sFallbackUPP
- __ZZL24ThemeFontReleaseMetaFontP10TThemeFontE8useCache
- __ZZL29GetTiledImageFromRGBA32ImagesPK11RGBA32ImageS1_f6CGRectE10bufferSize
- __ZZL29GetTiledImageFromRGBA32ImagesPK11RGBA32ImageS1_f6CGRectE6buffer
- __ZZL30CopyMenuWindowShadowParametersP10WindowDatahhE4keys
- __ZZL31GetTSMTraceCapsLockPressAndHoldvE10determined
- __ZZL31GetTSMTraceCapsLockPressAndHoldvE6result
- __ZZL34EnsureSpaceChangedDisplaysListenervE18sListenerInstalled
- __ZZL34GetPersistenceDictionariesAtLaunchvE24sPersistenceDictionaries
- __ZZL34GetPersistenceDictionariesAtLaunchvE8sChecked
- __ZZL36GetHandlerExternalRefFromInternalRefP10HandlerRecE11sOverflowed
- __ZZL36GetHandlerExternalRefFromInternalRefP10HandlerRecE16sLastExternalRef
- __ZZN15MenuBarInstance21UpdateAggregateUIModeE21MenuBarAnimationStylehhhE5kKeys
- __ZZN21PersistentWindowState21SynchronizeWindowListEvE11sWindowList
- __ZZN21PersistentWindowState28GetPersistentWindowStateListEvE26sPersistentWindowStateList
- ___56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke_5
- ___56-[IMKInputSession_Legacy handleEvent:completionHandler:]_block_invoke_6
- ____ZN10MBDisplays18ActiveSpaceChangedEjPvjS0_j_block_invoke
- ____ZN10WindowData13OrderNSWindowEij_block_invoke
- __block_literal_global.1171
- __block_literal_global.1178
- __block_literal_global.1185
- __block_literal_global.1190
- __block_literal_global.1320
- __block_literal_global.1327
- __block_literal_global.1332
- __block_literal_global.1337
- __block_literal_global.2005
- __block_literal_global.533
- __block_literal_global.643
- __block_literal_global.794
- __kEventLoopTimerClass
- __kEventLoopTimerID
- __kTSMInputMethodInstanceID
- _gApplicationRegionCode
- _gApplicationScriptCode
- _gIntlValueChanged
- _gKeyboardMenuChanged
- _gNextObserver
- _gObserverList
- _gObserverTimeBitField
- _gSelectedItemsChanged
- _isAppSandboxed.onceToken
- _isAppSandboxed.sIsAppSandboxed
- _sActiveDocIDBeforeFocusTheft
- _sApplicationMenuStateInvalidated
- _sAutoEnableIronwoodValid
- _sCachedCurrentInputSource
- _sCachedCurrentKeyboardLayoutHasUchr
- _sCachedCurrentKeyboardLayoutInpSrc
- _sCapsLockSequenceContextPtr
- _sCapsLockSwitchModifierChangedEventBeforeIOHID
- _sCapsLockSwitchPreviousEventModifiers
- _sCurrentKeyboardInputSource
- _sDefaultAsciiKeyboardLayout
- _sDoubleTapModifiersDetermined
- _sDoubleTapModsCGFlagsState
- _sDoubleTapModsEnabled
- _sEnabledInputSourcesArray
- _sFocusHasBeenStolen
- _sIdleLevel
- _sIdleTimers
- _sInputMethodInstanceArray
- _sInputSourceCacheData
- _sInputSourcesInUIOrderArray
- _sInputSourcesInUIOrderResolvedArray
- _sInvalidateEnabledInputSources
- _sInvalidateSelectedInputSources
- _sIsOKToAutoEnableIronwood
- _sIsTISPrefsConfigSandboxed
- _sKeyboardInputSourcesArray
- _sKeyboardLayoutOverrideInvalidated
- _sKeyboardLayoutOverrideRef
- _sMenuKeyEventTransLevel
- _sMenuKeyEventTransUserEventModifiers
- _sPBDefaultAsciiKeyboardLayout
- _sPasteboardKBInputMethods
- _sPerContextInputSetting
- _sPool
- _sProcessRemoteViewRegistered
- _sProcessingTapOnlyEvent
- _sReadMachineOnlyNotUserPrefs
- _sRemoteViewActivation
- _sSavedModifierChangedEvent
- _sSelectableInputSourceArray
- _sSelectedHandwritingLanguage
- _sSelectedHandwritingLanguageIsValid
- _sSessionBegunFromTap
- _sSystemRomanInputSource
- _sTISPrefsConfigSandboxedChecked
- _sTISSelectInputMethodCompletionBlockSource
- _sTISSelectInputSourceCompletionBlock
- _sTapDown1Time
- _sTapDown1UpTime
- _sTapDown2Time
- _sTapOnlyModifiersDetermined
- _sTapOnlyModsCGFlagsState
- _sTapSequenceStarted
- _sTapSequenceStartedFromTapOnly
- _sTimerListLock
- doubleKeyPressDuration.keyCodeCache
- sPasteboardInputMethodErrorInfo.0
- send_doublekeypress_event.sHasFunction
- send_doublekeypress_event.sOnce
CStrings:
+ "Client"
- "Horizontal Zoom"
- "Vertical Zoom"
- "zh_"

```
