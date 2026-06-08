## NPKCompanionAgent

> `/System/Library/PrivateFrameworks/NanoPassKit.framework/NPKCompanionAgent`

```diff

-1289.24.0.0.0
-  __TEXT.__text: 0x47c50
-  __TEXT.__auth_stubs: 0xce0
-  __TEXT.__objc_stubs: 0x7960
-  __TEXT.__objc_methlist: 0x34c0
+1329.0.0.0.0
+  __TEXT.__text: 0x421ac
+  __TEXT.__auth_stubs: 0xd40
+  __TEXT.__objc_stubs: 0x7bc0
+  __TEXT.__objc_methlist: 0x3580
   __TEXT.__const: 0xf8
-  __TEXT.__gcc_except_tab: 0x1264
-  __TEXT.__cstring: 0x2781
-  __TEXT.__objc_methname: 0xc04b
-  __TEXT.__oslogstring: 0x98dd
-  __TEXT.__objc_classname: 0x6e4
-  __TEXT.__objc_methtype: 0x3603
-  __TEXT.__unwind_info: 0xf70
-  __DATA_CONST.__auth_got: 0x680
-  __DATA_CONST.__got: 0x6c0
-  __DATA_CONST.__const: 0x1e48
-  __DATA_CONST.__cfstring: 0x1180
+  __TEXT.__gcc_except_tab: 0x1054
+  __TEXT.__cstring: 0x2872
+  __TEXT.__objc_methname: 0xc461
+  __TEXT.__oslogstring: 0x9aa4
+  __TEXT.__objc_classname: 0x6c3
+  __TEXT.__objc_methtype: 0x3666
+  __TEXT.__dlopen_cstrs: 0x56
+  __TEXT.__unwind_info: 0xe68
+  __DATA_CONST.__const: 0x1f20
+  __DATA_CONST.__cfstring: 0x1200
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x108

   __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x5b30
-  __DATA.__objc_selrefs: 0x27f0
-  __DATA.__objc_ivar: 0x1a8
+  __DATA_CONST.__auth_got: 0x6b0
+  __DATA_CONST.__got: 0x6e0
+  __DATA.__objc_const: 0x5c28
+  __DATA.__objc_selrefs: 0x2898
+  __DATA.__objc_ivar: 0x1bc
   __DATA.__objc_data: 0x5f0
   __DATA.__data: 0xc68
-  __DATA.__bss: 0x20
+  __DATA.__bss: 0x30
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/PairedSync.framework/PairedSync
   - /System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2054D9E4-B271-3D4D-8A3A-3C446689F9A1
-  Functions: 1129
-  Symbols:   437
-  CStrings:  2830
+  UUID: F2AB2660-3E11-34CA-BCD1-8FFBC8330203
+  Functions: 1152
+  Symbols:   447
+  CStrings:  2885
 
Symbols:
+ _NPKSecureElementIdentifiersForDevice
+ _NRDevicePropertyIsSetup
+ _NSLocalizedRecoverySuggestionErrorKey
+ _OBJC_CLASS_$_NPKOutstandingRemotePassSettingsStore
+ _PKDisplayableErrorDomain
+ __sl_dlopen
+ _abort_report_np
+ _free
+ _objc_claimAutoreleasedReturnValue
+ _objc_getClass
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x4
+ _objc_retain_x5
- _NPKPairedDeviceSecureElementIdentifiers
- _NPKSupportedBarcodesFromDataAccessor
- _PKEqualObjects
CStrings:
+ "%s"
+ "@\"NPKOutstandingRemotePassSettingsStore\""
+ "@\"NRDevice\""
+ "@\"PUConnection\""
+ "@72@0:8@16@24@32@40B48B52@56@64"
+ "Error: Error retrieving companion passcode state: %@"
+ "NPKMigrationResyncPaymentOptions_v1"
+ "Notice: %@: requested insert notification with title:%@ message:%@ shouldIgnoreDoNotDisturb:%@ playSound:%@, notificationIdentifier:%@, expirationDate:%@"
+ "Notice: Companion pass library get image set for unique ID %@, type %llu, displayProfile %@"
+ "Notice: Device Setup complete - executing migrations."
+ "Notice: Device Setup not complete yet, migration will complete during setupCompleteHandler."
+ "Notice: Executing migration: Resyncing payment options."
+ "Notice: Fetching passcode state for classic device"
+ "Notice: Fetching passcode state for tinker device"
+ "Notice: Suppressing remote initiated settings change of setting: %lu for pass: %@"
+ "PUConnection"
+ "T@\"NPKOutstandingRemotePassSettingsStore\",&,N,V_outstandingRemotePassSettingsStore"
+ "T@\"NRDevice\",&,N,V_device"
+ "T@\"NRDevice\",&,N,V_initializedDevice"
+ "T@\"NSArray\",C,N,V_initializedDeviceSEIDs"
+ "T@\"PUConnection\",&,N,V_passcodeConnection"
+ "UNLOCK_REQUIRED_ALERT_MESSAGE"
+ "Unable to find class %s"
+ "Warning: No device found on companionPaymentPassDatabase"
+ "Warning: Not saving invalid web service context (%@) for %@ watch"
+ "Warning: Watch is locked; cannot remove card"
+ "_checkCompanionUnlockStatusWithCompletion:"
+ "_device"
+ "_deviceScopedSecureElementIdentifiers"
+ "_executeMigrations"
+ "_initializedDevice"
+ "_initializedDeviceSEIDs"
+ "_migration_resyncPaymentOptions"
+ "_outstandingRemotePassSettingsStore"
+ "_passcodeConnection"
+ "_performMigrationsIfNecessary"
+ "_removePaymentPassWithUniqueID:waitForConfirmation:completion:"
+ "_userNotificationWithTitle:message:actionURL:forPass:shouldIgnoreDoNotDisturb:playSound:notificationIdentifier:expirationDate:"
+ "allPassTransactionActivitySummariesWithCompletion:"
+ "consumeMatchingRemoteSettings:forPassWithUniqueID:"
+ "current"
+ "device"
+ "fetchRemoteDevicePasscodeStateWithCompletion:"
+ "getRemoteDeviceState:"
+ "hasShouldIgnoreDoNotDisturb"
+ "initializedDevice"
+ "initializedDeviceSEIDs"
+ "insertBridgeBulletinWithTitle:message:actionURL:forPass:shouldIgnoreDoNotDisturb:playSound:notificationIdentifier:expirationDate:"
+ "non-current"
+ "outstandingRemotePassSettingsStore"
+ "passcodeConnection"
+ "precursorPassesWithHandler:"
+ "recordPendingSettings:forPassWithUniqueID:"
+ "reset"
+ "setDevice:"
+ "setInitializedDevice:"
+ "setInitializedDeviceSEIDs:"
+ "setOutstandingRemotePassSettingsStore:"
+ "setOwningDevice:"
+ "setPasscodeConnection:"
+ "setShouldIgnoreDoNotDisturb:"
+ "shouldIgnoreDoNotDisturb"
+ "softlink:r:path:/System/Library/PrivateFrameworks/PairedUnlock.framework/PairedUnlock"
+ "v24@0:8@?<v@?QQ@\"PKRestrictionsProfile\"@\"NSError\">16"
+ "v24@?0B8B12@\"NSError\"16"
+ "v28@?0B8B12B16@\"NSError\"20"
+ "v40@?0Q8Q16@\"PKRestrictionsProfile\"24@\"NSError\"32"
+ "v72@0:8@16@24@32@40B48B52@56@64"
- "@68@0:8@16@24@32@40B48@52@60"
- "Notice: %@: requested insert notification with title:%@ message:%@ playSound:%d, notificationIdentifier:%@, expirationDate:%@"
- "Notice: Companion pass library get image set for unique ID %@ %llu %@"
- "Notice: Replacing 1D barcode with barcode of format %d"
- "Warning: Not saving invalid web service context (%@) for current watch"
- "Warning: Not saving invalid web service context (%@) for non-current watch"
- "_performMigrations"
- "_userNotificationWithTitle:message:actionURL:forPass:playSound:notificationIdentifier:expirationDate:"
- "allPaymentApplicationUsageSummaries:"
- "allPaymentApplicationUsageSummariesWithCompletion:"
- "barcode"
- "format"
- "insertBridgeBulletinWithTitle:message:actionURL:forPass:playSound:notificationIdentifier:expirationDate:"
- "setBarcodes:"
- "v24@0:8@?<v@?QQ@\"NSError\">16"
- "v32@?0Q8Q16@\"NSError\"24"
- "v68@0:8@16@24@32@40B48@52@60"

```
