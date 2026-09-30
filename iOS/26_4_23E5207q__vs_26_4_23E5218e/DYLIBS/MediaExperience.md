## MediaExperience

> `/System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience`

```diff

-320.18.1.0.0
-  __TEXT.__text: 0x2abe24
-  __TEXT.__auth_stubs: 0x1ff0
+320.20.1.11.3
+  __TEXT.__text: 0x2ad38c
+  __TEXT.__auth_stubs: 0x2070
   __TEXT.__delay_helper: 0x1b8
-  __TEXT.__objc_methlist: 0x61e4
-  __TEXT.__cstring: 0x431bb
+  __TEXT.__objc_methlist: 0x6214
+  __TEXT.__cstring: 0x43425
   __TEXT.__const: 0x1bb8
   __TEXT.__gcc_except_tab: 0x2cb0
-  __TEXT.__oslogstring: 0x664a5
+  __TEXT.__oslogstring: 0x6680d
   __TEXT.__dlopen_cstrs: 0x5bd
-  __TEXT.__unwind_info: 0x4f08
+  __TEXT.__unwind_info: 0x4f48
   __TEXT.__objc_classname: 0x7b6
-  __TEXT.__objc_methname: 0x16660
-  __TEXT.__objc_methtype: 0x2225
-  __TEXT.__objc_stubs: 0xdcc0
-  __DATA_CONST.__got: 0xab0
-  __DATA_CONST.__const: 0x6790
+  __TEXT.__objc_methname: 0x1671f
+  __TEXT.__objc_methtype: 0x2240
+  __TEXT.__objc_stubs: 0xdd20
+  __DATA_CONST.__got: 0xab8
+  __DATA_CONST.__const: 0x67c8
   __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d70
+  __DATA_CONST.__objc_selrefs: 0x3d90
   __DATA_CONST.__objc_superrefs: 0x1f0
   __DATA_CONST.__objc_arraydata: 0x70
-  __AUTH_CONST.__auth_got: 0x1010
-  __AUTH_CONST.__const: 0x3fc8
-  __AUTH_CONST.__cfstring: 0x19560
-  __AUTH_CONST.__objc_const: 0x9078
+  __AUTH_CONST.__auth_got: 0x1050
+  __AUTH_CONST.__const: 0x3fe8
+  __AUTH_CONST.__cfstring: 0x195c0
+  __AUTH_CONST.__objc_const: 0x9118
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH_CONST.__objc_intobj: 0x228
+  __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xaf0
   __AUTH.__data: 0x570
-  __DATA.__objc_ivar: 0x8c8
+  __DATA.__objc_ivar: 0x8dc
   __DATA.__data: 0x1000
-  __DATA.__bss: 0x1940
+  __DATA.__bss: 0x1950
   __DATA.__common: 0x548
   __DATA_DIRTY.__objc_data: 0x960
   __DATA_DIRTY.__bss: 0x440

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B924CF10-E280-3FA7-ABE2-62806F066C88
-  Functions: 7879
-  Symbols:   24584
-  CStrings:  18861
+  UUID: 021CA67D-982C-3579-AAA5-E509BC8A9C73
+  Functions: 7899
+  Symbols:   24652
+  CStrings:  18905
 
Symbols:
+ -[AVSystemController(InternalUse) copyFigControllerInternal]
+ -[AVSystemController(InternalUse) handleServerReset]
+ -[AVSystemControllerCommon avscServerReset]
+ -[AVSystemControllerCommon commonSetup]
+ -[AVSystemControllerCommon init].cold.1
+ -[AVSystemControllerCommon init].cold.2
+ -[AVSystemControllerCommon init].cold.3
+ _CMSMDeviceState_DeviceHasExclaveMicInputCapability
+ _CMSMDeviceState_DeviceHasExclaveMicInputCapability.cold.1
+ _CMSMDeviceState_DeviceHasExclaveMicInputCapability.deviceHasExclaveMicInputCapability
+ _CMSMDeviceState_DeviceHasExclaveMicInputCapability.once
+ _FigEndpointCreateCentral.cold.2
+ _FigReadWriteLockCreate
+ _FigReadWriteLockDestroy
+ _FigReadWriteLockLockForRead
+ _FigReadWriteLockLockForWrite
+ _FigReadWriteLockUnlockForRead
+ _FigReadWriteLockUnlockForWrite
+ _FigStarkModeControllerGetCurrentInternalMode
+ _FigSystemControllerGetServerPID
+ _FigXPCRemoteClientGetServerPIDSync
+ _OBJC_IVAR_$_AVSystemController.mFigControllerLock
+ _OBJC_IVAR_$_AVSystemControllerCommon.mFigControllerReadWriteLock
+ _OBJC_IVAR_$_AVSystemControllerCommon.mServerPID
+ _OBJC_IVAR_$_AVSystemControllerCommon.mServerResetNotificationToken
+ _OBJC_IVAR_$_AVSystemControllerCommon.mServerResetNotificationsQueue
+ ___32-[AVSystemControllerCommon init]_block_invoke
+ ___CMSMDeviceState_DeviceHasExclaveMicInputCapability_block_invoke
+ ___FigRoutingManagerStartDeactivateAirPlayEndpointTimer_block_invoke.72
+ ___FigStarkModeControllerGetCurrentInternalMode_block_invoke
+ ___block_descriptor_40_e8_32o_e8_v12?0i8ls32l8
+ ___block_literal_global.129
+ ___block_literal_global.191
+ ___block_literal_global.747
+ ___block_literal_global.86
+ _central_copyCurrentMainAudioBorrowID
+ _kFigEndpointActivateOptionKey_NumberOfEndpoints
+ _kFigStarkModeBorrowerDetails_BorrowID
+ _kFigStarkModeBorrowerDetails_BorrowSucceeded
+ _objc_loadWeakRetained
+ _objc_msgSend$avscServerReset
+ _objc_msgSend$commonSetup
+ _objc_msgSend$copyFigControllerInternal
+ _objc_msgSend$handleServerReset
- GCC_except_table43
- ___FigRoutingManagerStartDeactivateAirPlayEndpointTimer_block_invoke.75
- ___block_literal_global.121
- ___block_literal_global.124
- ___block_literal_global.132
- ___block_literal_global.186
- ___block_literal_global.744
- ___block_literal_global.87
- _objc_msgSend$releaseSharedInstance
CStrings:
+ "! actualEndpoint"
+ "-AVSystemController- %s: Failed to create lock, abandon the object"
+ "-AVSystemController_Common-"
+ "-AVSystemController_Common- %s: Error adding listeners for AVSystemController={self:%p, mFigController:%p, error:%d}"
+ "-AVSystemController_Common- %s: Handling server reset for %p"
+ "-AVSystemController_Common- %s: Received process up notification"
+ "-AVSystemController_Common- %s: Received reset notification from server"
+ "-CMSMDevState- %s: This device %{public}s have exclave input capability"
+ "-MXExclaves- %s: Cannot create MXExclaves on devices that don't have exclave mic input capability!"
+ "-[AVSystemControllerCommon avscServerReset]"
+ "-[AVSystemControllerCommon commonSetup]"
+ "-[AVSystemControllerCommon init]"
+ "-[AVSystemControllerCommon init]_block_invoke"
+ "-endpoint_central- %s: Failed to get current internal mode, err=%d"
+ "-endpoint_central- %s: Found borrowID for current main audio holder: %@"
+ "-endpoint_central- %s: No borrowID available for main audio"
+ "-endpoint_central- %s: Posting notification with borrowID: %@"
+ "-endpoint_central- %s: Returning kFigEndpointProperty_CarEntityMainAudioBorrowID: %@"
+ "-endpoint_central- %s: storage or starkModeController is NULL"
+ "/AppleInternal/Library/BuildRoots/4~CJagugBVm8q05Yn6LAXNW5khWCE0bk79DuP9PGA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "19:53:57"
+ "A"
+ "AudioExclaveMicInputCapability"
+ "CMSMDeviceState_DeviceHasExclaveMicInputCapability_block_invoke"
+ "CurrentMainAudioBorrowID"
+ "Feb 19 2026"
+ "FigStarkModeControllerGetCurrentInternalMode"
+ "^{OpaqueFigReadWriteLock=}"
+ "avscServerReset"
+ "central_copyCurrentMainAudioBorrowID"
+ "com.apple.MediaExperience.AVSCDQ"
+ "com.apple.audiomxd.up"
+ "commonSetup"
+ "copyFigControllerInternal"
+ "failed to register for notification"
+ "got a nil deathQueue"
+ "got a nil rwLock"
+ "handleServerReset"
+ "kMXSystemControllerError_AllocationFailed"
+ "kMXSystemController_AllocationFailed"
+ "mFigControllerLock"
+ "mFigControllerReadWriteLock"
+ "mServerPID"
+ "mServerResetNotificationToken"
+ "mServerResetNotificationsQueue"
- "-MXExclaves- %s: Cannot create MXExclaves on devices that don't have Exclave capability!"
- "/AppleInternal/Library/BuildRoots/4~CH4mugD7wbItlL12g23DApPtknAXvU_n-9gC0fA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "22:36:57"
- "Jan 29 2026"

```
