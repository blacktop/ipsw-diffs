## SpringBoardUIServices

> `/System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices`

```diff

-4557.0.10.114.0
-  __TEXT.__text: 0x9f6a0
+4557.1.8.105.0
+  __TEXT.__text: 0x9ff30
   __TEXT.__auth_stubs: 0x1620
-  __TEXT.__objc_methlist: 0xe2a4
+  __TEXT.__objc_methlist: 0xe2ec
   __TEXT.__const: 0xa08
-  __TEXT.__gcc_except_tab: 0x98c
-  __TEXT.__cstring: 0xa597
+  __TEXT.__gcc_except_tab: 0x9ac
+  __TEXT.__cstring: 0xa5e3
   __TEXT.__dlopen_cstrs: 0x42e
   __TEXT.__ustring: 0x4
-  __TEXT.__oslogstring: 0x43d8
-  __TEXT.__unwind_info: 0x3020
+  __TEXT.__oslogstring: 0x4581
+  __TEXT.__unwind_info: 0x3058
   __TEXT.__objc_classname: 0x3e49
-  __TEXT.__objc_methname: 0x23de8
+  __TEXT.__objc_methname: 0x23ecf
   __TEXT.__objc_methtype: 0x6129
-  __TEXT.__objc_stubs: 0x16b60
+  __TEXT.__objc_stubs: 0x16c20
   __DATA_CONST.__got: 0x1028
-  __DATA_CONST.__const: 0x2c08
+  __DATA_CONST.__const: 0x2c68
   __DATA_CONST.__objc_classlist: 0x910
   __DATA_CONST.__objc_catlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x4c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7a48
+  __DATA_CONST.__objc_selrefs: 0x7a70
   __DATA_CONST.__objc_protorefs: 0x150
   __DATA_CONST.__objc_superrefs: 0x5c8
   __DATA_CONST.__objc_arraydata: 0xd8
   __AUTH_CONST.__auth_got: 0xb20
-  __AUTH_CONST.__const: 0x960
-  __AUTH_CONST.__cfstring: 0x9d60
-  __AUTH_CONST.__objc_const: 0x2cd80
+  __AUTH_CONST.__const: 0x940
+  __AUTH_CONST.__cfstring: 0x9e00
+  __AUTH_CONST.__objc_const: 0x2ce10
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_doubleobj: 0x150
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH.__objc_data: 0x4dd0
-  __DATA.__objc_ivar: 0xce8
+  __DATA.__objc_ivar: 0xcf0
   __DATA.__data: 0x3928
   __DATA.__bss: 0x3d8
   __DATA_DIRTY.__objc_data: 0xcd0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6920F38A-CE30-36BF-9873-445764D07408
-  Functions: 4602
-  Symbols:   17434
-  CStrings:  9472
+  UUID: F9DCA0F9-64BF-30C7-A30C-189513D5CD7C
+  Functions: 4615
+  Symbols:   17470
+  CStrings:  9493
 
Symbols:
+ -[SBUIPhoneUnlockWithRemoteDeviceCoordinator handleScreenOff:]
+ -[SBUIPhoneUnlockWithRemoteDeviceCoordinator isPhoneUnlockEnabledAndRequirementsMet]
+ -[SBUIPhoneUnlockWithVisionController _beginObservingSharingStartedNotification]
+ -[SBUIPhoneUnlockWithVisionController _beginObservingSharingStartedNotification].cold.1
+ -[SBUIPhoneUnlockWithVisionController _endObservingSharingStartedNotification]
+ -[SBUIPhoneUnlockWithVisionController _isPhoneUnlockWithVisionSupportedAndEnabled]
+ -[SBUIPhoneUnlockWithVisionController _sharingDidRestart]
+ -[SBUIPhoneUnlockWithVisionController _updateUserActivityRequirementsWithBlock:]
+ -[SBUIPhoneUnlockWithVisionController _userActivityUnlockRequirementsMet]
+ -[SBUIPhoneUnlockWithVisionController dealloc]
+ -[SBUIPhoneUnlockWithVisionController handleScreenOff:]
+ -[SBUIPhoneUnlockWithVisionController isPhoneUnlockEnabledAndRequirementsMet]
+ -[SBUIPhoneUnlockWithWatchController handleScreenOff:]
+ -[SBUIPhoneUnlockWithWatchController isPhoneUnlockEnabledAndRequirementsMet]
+ _OBJC_IVAR_$_SBUIPhoneUnlockWithVisionController._attemptCancellationInProgress
+ _OBJC_IVAR_$_SBUIPhoneUnlockWithVisionController._inProgressAuthenticationSessionID
+ _OBJC_IVAR_$_SBUIPhoneUnlockWithVisionController._screenOn
+ _OBJC_IVAR_$_SBUIPhoneUnlockWithVisionController._sharingDaemonStartedNotificationToken
+ _SBStringFromUIRectCorner
+ __OBJC_$_PROP_LIST_SBUIPhoneUnlockWithRemoteDeviceHandler
+ ___55-[SBUIPhoneUnlockWithVisionController handleScreenOff:]_block_invoke
+ ___62-[SBUIPhoneUnlockWithRemoteDeviceCoordinator handleScreenOff:]_block_invoke
+ ___67-[SBUIPhoneUnlockWithVisionController handleWakeSourceIsUserActive]_block_invoke
+ ___79-[SBUIPhoneUnlockWithVisionController handleSignificantUserInteractionOccurred]_block_invoke
+ ___80-[SBUIPhoneUnlockWithVisionController _beginObservingSharingStartedNotification]_block_invoke
+ ___84-[SBUIPhoneUnlockWithRemoteDeviceCoordinator isPhoneUnlockEnabledAndRequirementsMet]_block_invoke
+ ___SBStringFromUIRectCorner_block_invoke
+ ___block_descriptor_33_e54_v24?0"<SBUIPhoneUnlockWithRemoteDeviceHandler>"8^B16l
+ _objc_msgSend$_beginObservingSharingStartedNotification
+ _objc_msgSend$_endObservingSharingStartedNotification
+ _objc_msgSend$_isPhoneUnlockWithVisionSupportedAndEnabled
+ _objc_msgSend$_sharingDidRestart
+ _objc_msgSend$_updateUserActivityRequirementsWithBlock:
+ _objc_msgSend$_userActivityUnlockRequirementsMet
+ _objc_msgSend$cancelAuthenticationSessionWithID:
+ _objc_msgSend$handleScreenOff:
+ _objc_msgSend$isPhoneUnlockEnabledAndRequirementsMet
- -[SBUIPhoneUnlockWithRemoteDeviceCoordinator handleScreenOff]
- -[SBUIPhoneUnlockWithRemoteDeviceCoordinator phoneUnlockEnabledAndRequirementsMet]
- -[SBUIPhoneUnlockWithVisionController handleScreenOff]
- -[SBUIPhoneUnlockWithVisionController isPhoneUnlockWithVisionSupportedAndEnabled]
- -[SBUIPhoneUnlockWithVisionController unlockEnabledAndRequirementsMet]
- -[SBUIPhoneUnlockWithWatchController handleScreenOff]
- -[SBUIPhoneUnlockWithWatchController unlockEnabledAndRequirementsMet]
- _OBJC_IVAR_$_SBUIPhoneUnlockWithVisionController._authenticationAttemptInProgress
- _OBJC_IVAR_$_SBUIPhoneUnlockWithVisionController._isKeybagUnlocked
- ___61-[SBUIPhoneUnlockWithRemoteDeviceCoordinator handleScreenOff]_block_invoke
- ___82-[SBUIPhoneUnlockWithRemoteDeviceCoordinator phoneUnlockEnabledAndRequirementsMet]_block_invoke
- ___block_literal_global.10
- _objc_msgSend$handleScreenOff
- _objc_msgSend$isPhoneUnlockWithVisionSupportedAndEnabled
- _objc_msgSend$unlockEnabledAndRequirementsMet
CStrings:
+ "BottomLeft"
+ "BottomRight"
+ "Failed to register for sharing daemon started notification, status: %d"
+ "Phone unlock with vision - Reattempting unlock due to sharing daemon restart"
+ "Phone unlock with vision - attempt started with session ID %{public}@"
+ "Phone unlock with vision - cancelling attempt with session ID %{public}@ due to screen off"
+ "Phone unlock with vision - not attempting due to in progress attempt with session ID %{public}@"
+ "Phone unlock with vision - not attempting due to user active requirements not met or not supported or enabled"
+ "Phone unlock with vision - sharing daemon restarted"
+ "Phone unlock with vision - user activity unlock requirements met"
+ "Phone unlock with vision - user activity unlock requirements no longer met"
+ "TB,R,N,GisPhoneUnlockEnabledAndRequirementsMet"
+ "TopLeft"
+ "TopRight"
+ "_attemptCancellationInProgress"
+ "_beginObservingSharingStartedNotification"
+ "_endObservingSharingStartedNotification"
+ "_inProgressAuthenticationSessionID"
+ "_isPhoneUnlockWithVisionSupportedAndEnabled"
+ "_sharingDaemonStartedNotificationToken"
+ "_sharingDidRestart"
+ "_updateUserActivityRequirementsWithBlock:"
+ "_userActivityUnlockRequirementsMet"
+ "cancelAuthenticationSessionWithID:"
+ "com.apple.sharingd.daemon.started"
+ "handleScreenOff:"
+ "isPhoneUnlockEnabledAndRequirementsMet"
+ "|"
- "Phone unlock with vision - attempt started."
- "Phone unlock with vision - authentication attempt in progress."
- "Phone unlock with vision - not enabled, skipping error handling"
- "Phone unlock with vision - not supported or enabled."
- "Phone unlock with vision received user action wake source"
- "TB,R,N,GisPhoneUnlockWithVisionSupportedAndEnabled"
- "_authenticationAttemptInProgress"
- "_isKeybagUnlocked"
- "handleScreenOff"
- "isPhoneUnlockWithVisionSupportedAndEnabled"
- "phoneUnlockWithVisionSupportedAndEnabled"
- "unlockEnabledAndRequirementsMet"

```
