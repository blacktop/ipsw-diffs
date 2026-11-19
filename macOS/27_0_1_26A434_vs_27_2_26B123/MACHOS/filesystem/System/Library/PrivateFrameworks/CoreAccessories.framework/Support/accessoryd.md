## accessoryd

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/Support/accessoryd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__info_plist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1216.0.0.0.0
-  __TEXT.__text: 0x18b100
+1219.40.10.0.0
+  __TEXT.__text: 0x18c994
   __TEXT.__auth_stubs: 0x1860
-  __TEXT.__objc_stubs: 0x9060
-  __TEXT.__objc_methlist: 0x6dbc
+  __TEXT.__objc_stubs: 0x90c0
+  __TEXT.__objc_methlist: 0x6dec
   __TEXT.__const: 0x1b31
   __TEXT.__gcc_except_tab: 0x1ec4
   __TEXT.__objc_classname: 0xff5
-  __TEXT.__objc_methname: 0xfaae
-  __TEXT.__objc_methtype: 0x3399
-  __TEXT.__cstring: 0xe802
-  __TEXT.__oslogstring: 0x38365
+  __TEXT.__objc_methname: 0xfb22
+  __TEXT.__objc_methtype: 0x33a6
+  __TEXT.__cstring: 0xe928
+  __TEXT.__oslogstring: 0x388b2
   __TEXT.__ustring: 0x232
   __TEXT.__info_plist: 0x509
-  __TEXT.__unwind_info: 0x63d0
-  __DATA_CONST.__const: 0x9d88
-  __DATA_CONST.__cfstring: 0x7580
+  __TEXT.__unwind_info: 0x6430
+  __DATA_CONST.__const: 0x9f80
+  __DATA_CONST.__cfstring: 0x7660
   __DATA_CONST.__objc_classlist: 0x308
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x188

   __DATA_CONST.__objc_arrayobj: 0xd8
   __DATA_CONST.__objc_intobj: 0xf0
   __DATA_CONST.__auth_got: 0xc40
-  __DATA_CONST.__got: 0xc50
+  __DATA_CONST.__got: 0xc68
   __DATA_CONST.__auth_ptr: 0x90
-  __DATA.__objc_const: 0xae60
-  __DATA.__objc_selrefs: 0x3338
-  __DATA.__objc_ivar: 0x778
+  __DATA.__objc_const: 0xae90
+  __DATA.__objc_selrefs: 0x3350
+  __DATA.__objc_ivar: 0x77c
   __DATA.__objc_data: 0x1e50
   __DATA.__data: 0x1910
-  __DATA.__bss: 0xb68
+  __DATA.__bss: 0xb78
   __DATA.__common: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
-  Functions: 8226
-  Symbols:   10791
-  CStrings:  8624
+  Functions: 8254
+  Symbols:   10814
+  CStrings:  8658
 
Symbols:
+ -[ACCExternalAccessory EAPPIDVersionUID]
+ -[ACCTransportServer isConnectionEntitled:]
+ -[ACCTransportServer shouldAcceptConnection:]
+ -[NSXPCConnection(Entitlements) hasBooleanEntitlement:]
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libaks.a(der_utils.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libaks.a(libaks_internal.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.2.Internal.sdk/usr/local/lib/libaks.a(libaks_ref_key.o)
+ /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Binaries/CoreAccessories/install/Symbols/BuiltProducts/libAccessoryCore.a(acc_internal_settings.o)
+ OBJC_IVAR_$_ACCExternalAccessory._EAPPIDVersionUID
+ ____genericMFi_appLaunch_setDialogActive_block_invoke
+ ____genericMFi_appLaunch_setDialogActive_block_invoke_2
+ ____mfi4Auth_endpoint_releaseSourceUUIDsOnCancel_block_invoke
+ ___acc_internalSettings_isInternalBuild_block_invoke
+ ___mfi4Auth_endpoint_create_block_invoke_2
+ __createError
+ __genericMFi_appLaunch_setDialogActive
+ __mfi4Auth_endpoint_create_block_invoke_2
+ _acc_internalSettings_boolForKey
+ _kACCExternalAccessoryPPIDVersionUIDKey
+ _kCFACCInfo_PPIDVersionUID
+ _kCFACCUserDefaultsKey_AllowACCAuthProtocolOnAllTransport
+ _kCFACCUserDefaultsKey_AllowMFi4DevCertsOnProdDevice
+ _kCFACCUserDefaultsKey_DisableACCAuthProtocolOnInductive
+ _kCFACCUserDefaultsKey_EnableACCAuthProtocolOnNFC
+ _kCFErrorUnderlyingErrorKey
+ _objc_msgSend$EAPPIDVersionUID
+ _objc_msgSend$hasBooleanEntitlement:
+ _objc_msgSend$isConnectionEntitled:
+ acc_internalSettings_boolForKey
+ acc_internalSettings_isInternalBuild.isInternalBuild
+ acc_internalSettings_isInternalBuild.onceToken
+ acc_internal_settings.c
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libaks.a(der_utils.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libaks.a(libaks_internal.o)
- /AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX27.0.Internal.sdk/usr/local/lib/libaks.a(libaks_ref_key.o)
- _ACCUserDefaultsKey_AllowACCAuthProtocolOnAllTransport
- _ACCUserDefaultsKey_AllowMFi4DevCertsOnProdDevice
- _ACCUserDefaultsKey_DisableACCAuthProtocolOnInductive
- _ACCUserDefaultsKey_EnableACCAuthProtocolOnNFC
- ____genericMFi_appLaunch_RequestUserForAppLaunch_block_invoke_2
- ____genericMFi_appLaunch_RequestUserForAppLaunch_block_invoke_3
CStrings:
+ "%s: !sendOutgoingHandler"
+ "%s: %@ is not installed - no dialog to present"
+ "%s: %@, requestAppLaunch: unknown launchMethod %d - treating as WithUserAlert"
+ "%s: No connection for endpoint %@ - dialogActive not updated"
+ "%s: No dialog presented for %@ (appName %@) - clearing dialogActive"
+ "%s: authSession(%d), keepOpen %d, error %d"
+ "(user approved)"
+ "Adding accessory info: name %@, model %@, manufacturer %@, serial %@, firmware revision (active) %@, firmware revision (pending) %@, hardware revision %@, ppid %@, ppidVersionUID: %@, regionCode %@, hideFromUI: %s"
+ "B32@?0^v8^{iAP2Msg_t_st=*III**^?^vB^?}16^^{__CFError}24"
+ "EAPPIDVersionUID"
+ "PPIDVersionUID"
+ "T@\"NSString\",R,N,V_EAPPIDVersionUID"
+ "Unentitled XPC connection from pid %d! (Missing entitlement: '%@')! (API: ACCTransportClient / acc_transport_client)"
+ "_EAPPIDVersionUID"
+ "_genericMFi_appLaunch_setDialogActive"
+ "accAuthProtocol sendAuthSetupStart (manager2): connection gone for endpointUUID %@ !!"
+ "accAuthProtocol sendAuthSetupStart timer: no endpointUUID/connectionUUID for endpoint!!"
+ "acc_internalSettings: internal-only setting %{public}@ active"
+ "authSetupStart: initMessage_RequestAuthSetup failed: %d"
+ "authSetupStartTimer (manager2): connection gone for endpoint %@ !!"
+ "authSetupStartTimer: no endpointUUID/connectionUUID for endpoint!!"
+ "authTimer: connection gone for endpointUUID %@, no timeout to post"
+ "authTimer: endpoint not found for endpointUUID %@ !!"
+ "com.apple.mfi4Auth.decrypt"
+ "com.apple.mfi4Auth.encrypt"
+ "com.apple.mfi4Auth.process"
+ "com.apple.mfi4Auth.protocol"
+ "com.apple.mfi4Auth.receive"
+ "com.apple.mfi4Auth.send"
+ "com.apple.private.accessories.transport-client"
+ "decryptIncomingData: decryptPayload rc=%d"
+ "decryptIncomingData: failed: %d"
+ "encryptOutgoingData: encryptPayload rc=%d"
+ "failed to handle refresh access state response"
+ "hasBooleanEntitlement:"
+ "isConnectionEntitled:"
+ "mfi4Auth_protocol_handle_AuthCert: Accessory did NOT provide PrivacyPrefix!"
+ "mfi4Auth_protocol_processIncomingMessage: error: %d"
+ "mfi4Auth_protocol_processIncomingMessageExtra: error: %d"
+ "processIncomingMessageExtra: non-Extra message id 0x%04x — falling through to relay"
+ "processIncomingMessageRelay: error: %d"
+ "processIncomingMessageRelay: non-relay message id 0x%04x — no relay action"
+ "processOutgoingSecureTunnelDataForClient: sendOutgoingData failed"
+ "receiveIncomingData: sendOutgoingData failed"
+ "timerSource: endpoint %@ already gone, nothing to close"
+ "v24@?0^v8B16i20"
+ "v32@0:8^{?=^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFArray}^{__CFNumber}^{__CFNumber}^{__CFNumber}{_opaque_pthread_mutex_t=q[56c]}}16Q24"
- "%s: authSession(%d), keepOpen %d"
- "Adding accessory info: name %@, model %@, manufacturer %@, serial %@, firmware revision (active) %@, firmware revision (pending) %@, hardware revision %@, ppid %@, regionCode %@, hideFromUI: %s"
- "Data not passed in"
- "accAuthProtocol sendAuthSetupStart timer: no endpointUUID for endpoint!!"
- "decryptIncomingData: failed"
- "encryptOutgoingData: encryptPayload: error: %d"
- "failed to handle auth failed"
- "mfi4Auth_protocol_processIncomingMessage: error"
- "mfi4Auth_protocol_processIncomingMessageExtra: error"
- "processIncomingMessageRelay: error"
- "v20@?0^v8B16"
- "v24@?0^v8^{iAP2Msg_t_st=*III**^?^vB^?}16"
- "v32@0:8^{?=^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFString}^{__CFArray}^{__CFNumber}^{__CFNumber}^{__CFNumber}{_opaque_pthread_mutex_t=q[56c]}}16Q24"
```
