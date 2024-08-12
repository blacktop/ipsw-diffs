## LockedContentServices

> `/System/Library/PrivateFrameworks/LockedContentServices.framework/LockedContentServices`

```diff

-52.0.0.0.0
-  __TEXT.__text: 0x6ed4
-  __TEXT.__auth_stubs: 0x3f0
-  __TEXT.__objc_methlist: 0x45c
+56.100.0.0.0
+  __TEXT.__text: 0x7bb4
+  __TEXT.__auth_stubs: 0x470
+  __TEXT.__objc_methlist: 0x53c
   __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x55b
-  __TEXT.__oslogstring: 0xb6b
-  __TEXT.__gcc_except_tab: 0x6c
-  __TEXT.__unwind_info: 0x208
-  __TEXT.__objc_classname: 0x19a
-  __TEXT.__objc_methname: 0x17bf
-  __TEXT.__objc_methtype: 0x4ff
-  __TEXT.__objc_stubs: 0x1340
-  __DATA_CONST.__got: 0x178
-  __DATA_CONST.__const: 0x248
-  __DATA_CONST.__objc_classlist: 0x38
+  __TEXT.__gcc_except_tab: 0x15c
+  __TEXT.__cstring: 0x611
+  __TEXT.__oslogstring: 0xbb1
+  __TEXT.__unwind_info: 0x268
+  __TEXT.__objc_classname: 0x1b2
+  __TEXT.__objc_methname: 0x1af6
+  __TEXT.__objc_methtype: 0x57a
+  __TEXT.__objc_stubs: 0x15e0
+  __DATA_CONST.__got: 0x1a0
+  __DATA_CONST.__const: 0x2f0
+  __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5a8
-  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__objc_selrefs: 0x650
+  __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x208
-  __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x4c0
-  __AUTH_CONST.__objc_const: 0x2070
+  __AUTH_CONST.__auth_got: 0x248
+  __AUTH_CONST.__const: 0x100
+  __AUTH_CONST.__cfstring: 0x500
+  __AUTH_CONST.__objc_const: 0x2290
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x6c
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x98
   __DATA.__data: 0x4e0
   __DATA.__bss: 0x28
   __DATA_DIRTY.__objc_data: 0x140

   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/LinkMetadata.framework/LinkMetadata
   - /System/Library/PrivateFrameworks/LinkServices.framework/LinkServices
+  - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 171
-  Symbols:   307
-  CStrings:  440
+  Functions: 196
+  Symbols:   346
+  CStrings:  490
 
Symbols:
+ _AKSEventsRegister
+ _AKSEventsUnregister
+ _BSDispatchQueueCreateWithQualityOfService
+ _LNMetadataChangedNotification
+ _LNMetadataChangedNotificationBundlesKey
+ _MKBDeviceUnlockedSinceBoot
+ _OBJC_CLASS_$_BSCompoundAssertion
+ _OBJC_CLASS_$_LCSFirstUnlockManager
+ _OBJC_CLASS_$_NSNotificationCenter
+ _OBJC_METACLASS_$_LCSFirstUnlockManager
+ _objc_alloc_init
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
- _objc_retain_x4
CStrings:
+ "\x04\x13"
+ "\x11\x11"
+ "@\"<NSObject>\""
+ "@\"BSCompoundAssertion\""
+ "@\"LCSFirstUnlockManager\""
+ "@\"LNAction\""
+ "@?"
+ "@?16@0:8"
+ "B20@0:8B16"
+ "Clearing cached link action for %!@(MISSING)"
+ "LCSFirstUnlockManager"
+ "Prewarming link action for %!@(MISSING)"
+ "T@?,C,N,V_postFirstUnlockHandler"
+ "TB,N,V_hasUnlockedSinceBoot"
+ "Unable to resolve link action for capture application: %!@(MISSING)"
+ "^{_AKSEvent=}"
+ "_aksEvent"
+ "_beginObservingMetadataChanges"
+ "_cachedLinkAction"
+ "_captureApplicationsFromKnownExtensions:"
+ "_clearCachedLinkAction"
+ "_endObservingMetadataChanges"
+ "_evaluateCaptureApplicationRequirementsForKnownExtensions:"
+ "_evaluateLaunchPrewarmAssertions"
+ "_firstUnlockManager"
+ "_generateCachedLinkAction"
+ "_hasUnlockedSinceBoot"
+ "_launchIsPrewarmed"
+ "_launchPrewarmCompoundAssertion"
+ "_linkActionQueue"
+ "_lock_isInvalidating"
+ "_metadataChangedObserverToken"
+ "_postFirstUnlockHandler"
+ "_reevaluateCaptureApplicationRequirements"
+ "_resolvedLinkAction"
+ "acquireForReason:"
+ "acquireLaunchPrewarmAssertionForReason:"
+ "addObserverForName:object:queue:usingBlock:"
+ "assertionWithIdentifier:stateDidChangeHandler:"
+ "com.apple.LockedContentServices.CaptureApplicationLinkAction"
+ "com.apple.LockedContentServices.FirstUnlockManager"
+ "dealloc"
+ "defaultCenter"
+ "endObservingForFirstUnlock"
+ "hasUnlockedSinceBoot"
+ "isActive"
+ "launchPrewarm"
+ "postFirstUnlockHandler"
+ "setHasUnlockedSinceBoot:"
+ "setLog:"
+ "setPostFirstUnlockHandler:"
+ "userInfo"
+ "v16@?0@\"<BSCompoundAssertionState>\"8"
+ "v16@?0@\"NSNotification\"8"
+ "v20@?0i8^{__CFDictionary=}12"
+ "v24@0:8@?16"
- "\x03"
- "\x04"
- "@16@?0@\"<LCSExtensionDescribing>\"8"
- "No action metadata found for capture application: %!@(MISSING)"
- "bs_compactMap:"
- "captureApplicationProvider:updatedKnownApplicationsFrom:to:"

```
