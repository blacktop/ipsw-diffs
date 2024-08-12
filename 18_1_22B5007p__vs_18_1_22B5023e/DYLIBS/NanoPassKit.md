## NanoPassKit

> `/System/Library/PrivateFrameworks/NanoPassKit.framework/NanoPassKit`

```diff

-1200.0.0.0.0
-  __TEXT.__text: 0x23ec84
+1206.0.0.0.0
+  __TEXT.__text: 0x23f8a4
   __TEXT.__auth_stubs: 0x1d70
-  __TEXT.__objc_methlist: 0x22820
-  __TEXT.__cstring: 0x17502
+  __TEXT.__objc_methlist: 0x22860
+  __TEXT.__cstring: 0x17602
   __TEXT.__const: 0x71c
-  __TEXT.__oslogstring: 0x2b2bc
-  __TEXT.__gcc_except_tab: 0x69b0
+  __TEXT.__oslogstring: 0x2b3ec
+  __TEXT.__gcc_except_tab: 0x6a38
   __TEXT.__dlopen_cstrs: 0x2eb
   __TEXT.__ustring: 0x160
   __TEXT.__constg_swiftt: 0x1c0
-  __TEXT.__swift5_typeref: 0x199
+  __TEXT.__swift5_typeref: 0x197
   __TEXT.__swift5_reflstr: 0xd8
   __TEXT.__swift5_fieldmd: 0x130
   __TEXT.__swift5_types: 0x24

   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x8b90
-  __TEXT.__eh_frame: 0x318
-  __TEXT.__objc_classname: 0x6b6a
-  __TEXT.__objc_methname: 0x3eb0b
-  __TEXT.__objc_methtype: 0xa213
-  __TEXT.__objc_stubs: 0x218e0
-  __DATA_CONST.__got: 0x1e28
-  __DATA_CONST.__const: 0x6bc0
+  __TEXT.__unwind_info: 0x8ba8
+  __TEXT.__eh_frame: 0x310
+  __TEXT.__objc_classname: 0x6b56
+  __TEXT.__objc_methname: 0x3ebf4
+  __TEXT.__objc_methtype: 0xa241
+  __TEXT.__objc_stubs: 0x21980
+  __DATA_CONST.__got: 0x1e40
+  __DATA_CONST.__const: 0x6c70
   __DATA_CONST.__objc_classlist: 0x11c8
   __DATA_CONST.__objc_catlist: 0xe8
-  __DATA_CONST.__objc_protolist: 0x280
+  __DATA_CONST.__objc_protolist: 0x278
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbe88
+  __DATA_CONST.__objc_selrefs: 0xbea8
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x10f8
   __DATA_CONST.__objc_arraydata: 0x88
   __AUTH_CONST.__auth_got: 0xec8
   __AUTH_CONST.__auth_ptr: 0xc8
-  __AUTH_CONST.__const: 0x1218
-  __AUTH_CONST.__cfstring: 0xe8a0
-  __AUTH_CONST.__objc_const: 0x4a150
+  __AUTH_CONST.__const: 0x11f8
+  __AUTH_CONST.__cfstring: 0xe920
+  __AUTH_CONST.__objc_const: 0x49e50
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH.__objc_data: 0xb130
   __AUTH.__data: 0x180
-  __DATA.__objc_ivar: 0x1c20
-  __DATA.__data: 0x1f50
-  __DATA.__bss: 0x878
+  __DATA.__objc_ivar: 0x1c24
+  __DATA.__data: 0x1ef0
+  __DATA.__bss: 0x898
   __DATA.__common: 0x98
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__bss: 0x10

   - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
   - /System/Library/Frameworks/Messages.framework/Messages
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/AppConduit.framework/AppConduit
   - /System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 14145
-  Symbols:   16211
-  CStrings:  15009
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 14158
+  Symbols:   16233
+  CStrings:  15019
 
Symbols:
+ _NPKGetRemoteBiometricAuthenticationStatusTrustLost
+ _NPKNotificationForExpressPassConfigurationChange
+ _NPKSetRemoteBiometricAuthenticationStatusTrustLost
+ _PKUIApplicationDidEnterBackgroundNotification
+ _UIApplicationWillEnterForegroundNotification
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "\x01\x11\x11"
+ "Error: %!@(MISSING): Couldn't get remote object proxy"
+ "Error: NPKIDVRemoteDeviceService: Error during remote biometric authentication status request: %!@(MISSING)"
+ "Error: NPKIDVRemoteDeviceService: Unable to fetch remote biometric authentication status! No data source found."
+ "NPKExpressPassConfigurations"
+ "NPKInternalExpressPassConfigurationsChangedRemotely"
+ "NPKPassbookBridgeSettingsController"
+ "NPKRemoteBiometricAuthenticationStatusCoordinatorTrustLost"
+ "Notice: %!@(MISSING): Transient assertion connection interrupted"
+ "Notice: %!@(MISSING): Transient assertion connection invalidated"
+ "Notice: %!@(MISSING): Transient pass assertion: resyncing state"
+ "Notice: Marking remote biometric authentication status trust lost: %!@(MISSING)"
+ "Notice: NPKCompanionAgentConnection (%!@(MISSING)): Payment pass did update credentials: %!@(MISSING), credentials %!@(MISSING)"
+ "Notice: NPKIDVRemoteDeviceService: Finished request for remote biometric authentication status of type:%!@(MISSING). Trust lost:%!@(MISSING) error:%!@(MISSING)"
+ "Notice: NPKIDVRemoteDeviceService: Received request for remote biometric authentication status"
+ "Notice: NPKPassAssociatedInfoManager: Removing model for pass with unique ID %!@(MISSING)"
+ "Notice: [PaymentSessionManager] Is previous user selected pass (%!@(MISSING)) equal to new pass (%!@(MISSING))? %!@(MISSING)"
+ "ReceiverContentPresented-NanoPassbook-NearbyPeerPayment"
+ "TB,R,N,V_isNFCDisabled"
+ "TI,N,V_supportState"
+ "Warning: Found NFHardwareSupportStateUnSupported."
+ "Warning: Will not use APIs since hw support state is %!d(MISSING)"
+ "Warning: Won't use APIs since hw support state is %!d(MISSING)"
+ "_applicationWillEnterBackground:"
+ "_atomicIsNfcDisabled"
+ "_backgroundQueue_initHWManager"
+ "_fetchNFCState"
+ "_supportState"
+ "applicationIsAtForeground"
+ "clearProvisioningSupportDataOfType:completion:"
+ "com.apple.nanoPassKit.hwManager.background"
+ "com.apple.nanopassbook.expresspassconfigurationschanged"
+ "fetchRemoteBiometricAuthenticationStatusForCredentialType:completion:"
+ "isNfcDisabled"
+ "paymentPassWithUniqueIdentifier:didUpdateWithCredentials:"
+ "registerEventListener:"
+ "remoteDevicesManager:remoteBiometricAuthenticationStatusForCredentialType:completion:"
+ "remoteDevicesSessionServer:remoteBiometricAuthenticationStatusForCredentialType:completion:"
+ "remoteDevicesSessionService:remoteBiometricAuthenticationStatusForCredentialType:completion:"
+ "saveProvisioningSupportData:completion:"
+ "setSupportState:"
+ "supportState"
+ "v32@0:8Q16@?<v@?>24"
+ "v40@0:8@\"NPKIDVRemoteDeviceSessionServer\"16Q24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"NPKIDVRemoteDeviceSessionService\"16Q24@?<v@?B@\"NSError\">32"
- "@\"PKSecureElement\""
- "Error: Couldn't get remote object proxy"
- "Notice: NPKCompanionAgentConnection (%!@(MISSING)): Payment pass did update credentials: %!@(MISSING), credentials %!@(MISSING), completion: %!@(MISSING)"
- "Notice: NPKPassAssociatedInfoModel: action type:%!@(MISSING) relevant:%!@(MISSING) select:%!@(MISSING) enter:%!@(MISSING)"
- "Notice: NPKPassAssociatedInfoModel: fail to find action type:%!@(MISSING) with identifiers:%!@(MISSING)"
- "Notice: NPKPassAssociatedInfoModel: fetching action type:%!@(MISSING) with identifiers:%!@(MISSING)"
- "Notice: Read nfc is disabled from NFHardwareManager"
- "Notice: Transient assertion connection interrupted"
- "Notice: Transient assertion connection invalidated"
- "Notice: Transient pass assertion: resyncing state"
- "Notice: updated restricted mode after start observe secure element updates"
- "PKSecureElementObserver"
- "TB,N,V_isNFCDisabled"
- "Warning: Expected to be able to get express pass from updated pass %!@(MISSING) but fail."
- "Warning: Found NFHardwareSupportStateUnSupported. Cannot determine if NFC is disabled."
- "_initializeSecureElement"
- "_requestFetchNFCState"
- "_secureElement"
- "_setupNearfield"
- "com.apple.nanoPassKit.secureElement.background"
- "paymentPassWithUniqueIdentifier:didUpdateWithCredentials:completion:"
- "principalClass"
- "relevantPropertyIdentifier"
- "requestFetchNFCState"
- "secureElement:deletionOfAppletsDidFinishWithSuccess:"
- "secureElement:deletionOfAppletsDidUpdateToProgress:"
- "secureElementDidEnterRestrictedMode:"
- "secureElementDidLeaveRestrictedMode:"
- "secureElementPairingDidChangeForReason:"
- "setIsNFCDisabled:"
- "shouldObserveSecureElementChanges:"
- "v24@0:8@\"PKSecureElement\"16"
- "v28@0:8@\"PKSecureElement\"16B24"
- "v32@0:8@\"PKSecureElement\"16d24"
- "v32@?0@\"PKPaymentPassAction\"8Q16^B24"

```
