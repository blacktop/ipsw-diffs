## NanoPassKit

> `/System/Library/PrivateFrameworks/NanoPassKit.framework/NanoPassKit`

```diff

-1214.0.0.0.0
-  __TEXT.__text: 0x23fcf0
+1215.1.0.0.0
+  __TEXT.__text: 0x241744
   __TEXT.__auth_stubs: 0x1d70
-  __TEXT.__objc_methlist: 0x22860
-  __TEXT.__cstring: 0x17662
+  __TEXT.__objc_methlist: 0x22a70
+  __TEXT.__cstring: 0x17772
   __TEXT.__const: 0x71c
-  __TEXT.__oslogstring: 0x2b47c
-  __TEXT.__gcc_except_tab: 0x6a38
+  __TEXT.__oslogstring: 0x2b77c
+  __TEXT.__gcc_except_tab: 0x6aa4
   __TEXT.__dlopen_cstrs: 0x2eb
   __TEXT.__ustring: 0x160
   __TEXT.__constg_swiftt: 0x1c0

   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x8bc0
+  __TEXT.__unwind_info: 0x8c68
   __TEXT.__eh_frame: 0x310
-  __TEXT.__objc_classname: 0x6b56
-  __TEXT.__objc_methname: 0x3ec4e
-  __TEXT.__objc_methtype: 0xa241
-  __TEXT.__objc_stubs: 0x219e0
-  __DATA_CONST.__got: 0x1e58
-  __DATA_CONST.__const: 0x6c88
-  __DATA_CONST.__objc_classlist: 0x11c8
+  __TEXT.__objc_classname: 0x6ba6
+  __TEXT.__objc_methname: 0x3f189
+  __TEXT.__objc_methtype: 0xa29a
+  __TEXT.__objc_stubs: 0x21cc0
+  __DATA_CONST.__got: 0x1e68
+  __DATA_CONST.__const: 0x6d28
+  __DATA_CONST.__objc_classlist: 0x11d8
   __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x278
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbeb8
+  __DATA_CONST.__objc_selrefs: 0xbf98
   __DATA_CONST.__objc_protorefs: 0x90
-  __DATA_CONST.__objc_superrefs: 0x10f8
+  __DATA_CONST.__objc_superrefs: 0x1108
   __DATA_CONST.__objc_arraydata: 0x88
   __AUTH_CONST.__auth_got: 0xec8
   __AUTH_CONST.__auth_ptr: 0xc8
-  __AUTH_CONST.__const: 0x11f8
-  __AUTH_CONST.__cfstring: 0xe9a0
-  __AUTH_CONST.__objc_const: 0x49e30
+  __AUTH_CONST.__const: 0x1218
+  __AUTH_CONST.__cfstring: 0xea20
+  __AUTH_CONST.__objc_const: 0x4a100
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH.__objc_data: 0xb130
+  __AUTH.__objc_data: 0xb1d0
   __AUTH.__data: 0x180
-  __DATA.__objc_ivar: 0x1c20
+  __DATA.__objc_ivar: 0x1c40
   __DATA.__data: 0x1ef0
   __DATA.__bss: 0x898
   __DATA.__common: 0x98

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 14162
-  Symbols:   16243
-  CStrings:  15025
+  Functions: 14214
+  Symbols:   16299
+  CStrings:  15087
 
Symbols:
+ _NPKIDVRemoteDeviceProtoUpdatePrearmStatusRequestReadFrom
+ _NSStringFromNPKLockStatusChangeEvent
+ _OBJC_CLASS_$_NPKIDVRemoteDeviceProtoUpdatePrearmStatusRequest
+ _OBJC_CLASS_$_NPKLockStatusChangeCoordinator
+ _OBJC_METACLASS_$_NPKIDVRemoteDeviceProtoUpdatePrearmStatusRequest
+ _OBJC_METACLASS_$_NPKLockStatusChangeCoordinator
CStrings:
+ "-[NPKIDVRemoteDeviceConnectionCoordinator updatePrearmStatus]"
+ "@\"<NPKLockStatusChangeCoordinatorDelegate>\""
+ "@\"NPKLockStatusChangeCoordinator\""
+ "B20@0:8i16"
+ "ExtendedDeviceLockState"
+ "NPKIDVRemoteDeviceProtoUpdatePrearmStatusRequest"
+ "NPKLockStatusChangeCoordinator"
+ "NPKLockStatusChangeEventLock"
+ "NPKLockStatusChangeEventUnlock"
+ "Notice: %!{(MISSING)public}@: Device is locked"
+ "Notice: %!{(MISSING)public}@: Device is unlocked"
+ "Notice: %!{(MISSING)public}@: Handling lock state change"
+ "Notice: %!{(MISSING)public}@: Performing work in response to device lock - %!l(MISSING)u block(s) to execute"
+ "Notice: %!{(MISSING)public}@: Performing work in response to device unlock - %!l(MISSING)u block(s) to execute"
+ "Notice: %!{(MISSING)public}@: Registering for lock state notifications"
+ "Notice: %!{(MISSING)public}@: Requested perform blocks if possible."
+ "Notice: %!{(MISSING)public}@: Unhandled lock state with value %!i(MISSING)"
+ "Notice: NPKIDVRemoteDeviceService: Reminder: remote device Needs biometric authentication token"
+ "Notice: NPKIDVRemoteDeviceService: Setup biometric authentication token reminder for deviceID:%!@(MISSING)"
+ "Notice: NPKIDVRemoteDeviceService: tear down biometric authentication token reminder for deviceID:%!@(MISSING)"
+ "T@\"<NPKLockStatusChangeCoordinatorDelegate>\",W,N,V_delegate"
+ "T@\"NSMutableArray\",&,N,V_blocksToPerformAfterDeviceLock"
+ "T@\"NSMutableArray\",&,N,V_blocksToPerformAfterDeviceUnlock"
+ "TB,V_wipeBlocksAfterPerform"
+ "Ti,N,V_notifyLockStatesToken"
+ "_blocksToPerformAfterDeviceLock"
+ "_blocksToPerformAfterDeviceUnlock"
+ "_handleLockStateChange"
+ "_hasLockBlocksToPerform"
+ "_hasUnlockBlocksToPerform"
+ "_insideLockSetupBiometricAuthenticationTokenReminderForDeviceID:serviceNames:"
+ "_insideLockTeardownBiometricAuthenticationTokenReminderForDeviceID:"
+ "_isLockedForLockState:"
+ "_isUnlockedForLockState:"
+ "_lockState"
+ "_lockStatusChangeCoordinator"
+ "_lockStatusChangeCoordinatorQueue"
+ "_notifyLockStatesToken"
+ "_performLockWork"
+ "_performUnlockWork"
+ "_performWorkForEvent:withBlocks:"
+ "_registerForLockStatusChanges"
+ "_wipeBlocksAfterPerform"
+ "blocksToPerformAfterDeviceLock"
+ "blocksToPerformAfterDeviceUnlock"
+ "com.apple.NanoPassKit.RemoteDeviceServiceEventsCoordinator.lockStatus"
+ "descriptionOfLockStatusChangeEvent:"
+ "hasBlocksToPerform"
+ "lockStatusChangeCoordinator:didFinishPerformingBlocksForLockStatusEvent:"
+ "lockStatusChangeCoordinator:willBeginPerformingBlocksForLockStatusEvent:"
+ "notifyLockStatesToken"
+ "performBlocksIfPossible"
+ "performSubjectToEvent:blockToPerform:"
+ "readerIdentifierForAccessory:withPass:"
+ "setBlocksToPerformAfterDeviceLock:"
+ "setBlocksToPerformAfterDeviceUnlock:"
+ "setNotifyLockStatesToken:"
+ "setWipeBlocksAfterPerform:"
+ "updatePrearmStatus"
+ "v32@?0@\"NSData\"8@\"PKHMAccessory\"16^B24"
+ "wipeBlocksAfterPerform"

```
