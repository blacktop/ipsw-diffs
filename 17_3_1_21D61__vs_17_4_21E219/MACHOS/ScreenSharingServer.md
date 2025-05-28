## ScreenSharingServer

> `/System/Library/CoreServices/ScreenSharingServer.app/ScreenSharingServer`

```diff

-85.1.0.0.0
-  __TEXT.__text: 0x2ceb4
-  __TEXT.__auth_stubs: 0xcb0
-  __TEXT.__objc_stubs: 0x37a0
-  __TEXT.__objc_methlist: 0x1304
+105.3.0.0.0
+  __TEXT.__text: 0x31c10
+  __TEXT.__auth_stubs: 0xdf0
+  __TEXT.__objc_stubs: 0x3980
+  __TEXT.__objc_methlist: 0x1390
   __TEXT.__const: 0x68
-  __TEXT.__objc_methname: 0x51e5
-  __TEXT.__cstring: 0x9730
-  __TEXT.__oslogstring: 0x4758
-  __TEXT.__objc_classname: 0x1de
-  __TEXT.__objc_methtype: 0x2f63
-  __TEXT.__gcc_except_tab: 0x70
-  __TEXT.__unwind_info: 0x464
-  __DATA_CONST.__auth_got: 0x668
-  __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__const: 0x560
+  __TEXT.__objc_methname: 0x5413
+  __TEXT.__cstring: 0x99a6
+  __TEXT.__oslogstring: 0x4954
+  __TEXT.__objc_classname: 0x217
+  __TEXT.__objc_methtype: 0x2f7f
+  __TEXT.__gcc_except_tab: 0xac
+  __TEXT.__unwind_info: 0x4f4
+  __DATA_CONST.__auth_got: 0x708
+  __DATA_CONST.__got: 0x1a8
+  __DATA_CONST.__const: 0x5e0
   __DATA_CONST.__cfstring: 0x18a0
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x208
+  __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0xc0
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x2d90
-  __DATA.__objc_selrefs: 0x10f0
-  __DATA.__objc_classrefs: 0x1f8
-  __DATA.__objc_superrefs: 0x48
+  __DATA.__objc_const: 0x2db0
+  __DATA.__objc_selrefs: 0x1178
   __DATA.__objc_ivar: 0x20c
   __DATA.__objc_data: 0x370
   __DATA.__data: 0x410
-  __DATA.__bss: 0x310
+  __DATA.__bss: 0x328
   __DATA.__common: 0x19
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/GameKitServices.framework/GameKitServices
   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
+  - /System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities
   - /System/Library/PrivateFrameworks/LimitAdTracking.framework/LimitAdTracking
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi
+  - /System/Library/PrivateFrameworks/SettingsCellular.framework/SettingsCellular
+  - /System/Library/PrivateFrameworks/SettingsCellularUI.framework/SettingsCellularUI
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
   - /System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 562
-  Symbols:   319
-  CStrings:  2871
+  Functions: 586
+  Symbols:   342
+  CStrings:  2924
 
Symbols:
+ _CFURLCreateWithFileSystemPath
+ _IMSharedHelperDeviceHasMultipleSubscriptions
+ _OBJC_CLASS_$_IMCTSMSUtilities
+ _OBJC_CLASS_$_IMCTSubscriptionUtilities
+ _kCFUserNotificationIconURLKey
+ _objc_autoreleaseReturnValue
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x1
+ _objc_release_x22
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x20
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_storeStrong
- _CFMakeCollectable
- _CFRetain
- __Block_object_assign
- _objc_autorelease
- _objc_setProperty_nonatomic
CStrings:
+ "\x01B\x14\x12\x15"
+ "\x01Y\x12!\x13\x12\x12#"
+ "\x02"
+ "\x03\x12"
+ "\x13"
+ "-[IDSSessionEmbeddedControllerBase addNotificationIconTo:]"
+ ".cxx_destruct"
+ "2"
+ "GetMMSEnabled"
+ "Has a single SIM"
+ "Has multiple SIMs"
+ "IMMMSEnabledForPhoneNumber:simID:"
+ "SelectedPlanDataRoamingEnabled"
+ "SelectedPlanDataRoamingEnabled: Failed to get the CoreTelephonyClient"
+ "SelectedPlanDataRoamingEnabled: failed to get the roaming enabled value, error = %s"
+ "SelectedPlanDataRoamingEnabled: no data service descriptor available, error = %s"
+ "T@\"NSObject<OS_dispatch_semaphore>\",&,V_vsSemaphore"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_touchEventTimer"
+ "T@\"NSObject<OS_os_transaction>\",&,V_osTransaction"
+ "T@\"NSString\",?,R,C"
+ "T@\"SBSStatusBarStyleOverridesAssertion\",&,V_doubleHeightStatusBarAssertion"
+ "addNotificationIconTo:"
+ "ctServiceSubscriptions"
+ "ctSubscriptionInfoWithError:"
+ "doubleHeightStatusBarAssertion"
+ "error getting the active subscription %s"
+ "getActiveContexts:"
+ "getCurrentDataServiceDescriptorSync:"
+ "getInternationalDataAccessSync:error:"
+ "ignoring invitation because allowRemoteScreenObservation restriction set"
+ "inviterIconPath is nil, did a subclass override the method?"
+ "isAppleSupportRequest"
+ "isMultiSim"
+ "isMultiSim: Failed to get the CoreTelephonyClient"
+ "isMultiSim: error getting activeContexts, error = %s"
+ "labelID"
+ "messages - MMS enabled"
+ "osTransaction"
+ "phoneNumber"
+ "preferredOrDefaultSubscriptionContext"
+ "released status bar assertion"
+ "returning sessionState: %s"
+ "sendSessionInfoToClient"
+ "setDoubleHeightStatusBarAssertion:"
+ "setOsTransaction:"
+ "subscriptions"
+ "v24@0:8^{__CFDictionary=}16"
+ "\x81"
+ "\xd3\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf1\xf0!\xa1\xa1\""
- "T@\"NSObject<OS_dispatch_semaphore>\",V_vsSemaphore"
- "T@\"NSObject<OS_dispatch_source>\",N,V_touchEventTimer"
- "ignoring invitation because  allowRemoteScreenObservation restriction set"
- "isAppleSupport"
- "released status bar asserion"
- "treansaction %p"

```
