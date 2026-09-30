## findmydeviced

> `/usr/libexec/findmydeviced`

```diff

-455.33.11.19.3
-  __TEXT.__text: 0x2412b8
-  __TEXT.__auth_stubs: 0x1a60
-  __TEXT.__objc_stubs: 0x17700
-  __TEXT.__objc_methlist: 0xfb64
-  __TEXT.__const: 0x2f3d6
-  __TEXT.__gcc_except_tab: 0x3090
-  __TEXT.__objc_methname: 0x1d551
-  __TEXT.__oslogstring: 0x124d9
-  __TEXT.__cstring: 0x97ce
-  __TEXT.__objc_classname: 0x1aa5
-  __TEXT.__objc_methtype: 0x320e
-  __TEXT.__constg_swiftt: 0x534
+455.34.7.18.21
+  __TEXT.__text: 0x260804
+  __TEXT.__auth_stubs: 0x1a40
+  __TEXT.__objc_stubs: 0x176e0
+  __TEXT.__objc_methlist: 0xfb2c
+  __TEXT.__const: 0x2f2c6
+  __TEXT.__gcc_except_tab: 0x2eb4
+  __TEXT.__objc_methname: 0x1d528
+  __TEXT.__cstring: 0x95fc
+  __TEXT.__oslogstring: 0x125c9
+  __TEXT.__objc_classname: 0x1ba6
+  __TEXT.__objc_methtype: 0x323c
   __TEXT.__swift5_typeref: 0x47a
-  __TEXT.__swift5_reflstr: 0x479
-  __TEXT.__swift5_fieldmd: 0x618
   __TEXT.__swift5_capture: 0x270
-  __TEXT.__swift5_types: 0x7c
-  __TEXT.__swift_as_entry: 0x58
-  __TEXT.__swift_as_ret: 0x40
+  __TEXT.__swift5_reflstr: 0x459
   __TEXT.__swift5_assocty: 0x60
+  __TEXT.__constg_swiftt: 0x534
+  __TEXT.__swift5_fieldmd: 0x618
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x10c
+  __TEXT.__swift5_types: 0x7c
+  __TEXT.__swift_as_entry: 0x58
+  __TEXT.__swift_as_ret: 0x40
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x3cc0
-  __TEXT.__eh_frame: 0x11c4
-  __DATA_CONST.__auth_got: 0xd40
-  __DATA_CONST.__got: 0x9e8
-  __DATA_CONST.__auth_ptr: 0x280
-  __DATA_CONST.__const: 0xfed0
-  __DATA_CONST.__cfstring: 0xac40
-  __DATA_CONST.__objc_classlist: 0x700
+  __TEXT.__unwind_info: 0x4f40
+  __TEXT.__eh_frame: 0x1254
+  __DATA_CONST.__auth_got: 0xd30
+  __DATA_CONST.__got: 0x9e0
+  __DATA_CONST.__auth_ptr: 0x288
+  __DATA_CONST.__const: 0xf9a8
+  __DATA_CONST.__cfstring: 0xada0
+  __DATA_CONST.__objc_classlist: 0x708
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x1e0
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_floatobj: 0x30
   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__linkguard: 0xe
-  __DATA.__objc_const: 0x1a260
-  __DATA.__objc_selrefs: 0x6a90
-  __DATA.__objc_ivar: 0x10f8
-  __DATA.__objc_data: 0x4690
-  __DATA.__data: 0x2870
-  __DATA.__bss: 0x2a00
+  __DATA.__objc_const: 0x1a308
+  __DATA.__objc_selrefs: 0x6a60
+  __DATA.__objc_ivar: 0x10fc
+  __DATA.__objc_data: 0x46e0
+  __DATA.__data: 0x28b8
+  __DATA.__bss: 0x29f0
   __DATA.__common: 0xa8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 91DFDB3C-C15D-33F4-B00C-B01D7F728836
-  Functions: 6636
-  Symbols:   900
-  CStrings:  10246
+  UUID: F8A21DBF-B739-3FD2-BDF2-67700F332C8F
+  Functions: 6655
+  Symbols:   898
+  CStrings:  10262
 
Symbols:
+ _$sSL2leoiySbx_xtFZTj
+ _$sSQ2eeoiySbx_xtFZTj
+ _OBJC_CLASS_$_OTControl
+ _OTDefaultContext
+ _objc_setProperty_atomic_copy
+ _objc_sync_enter
+ _objc_sync_exit
- _$sSL1loiySbx_xtFZTj
- _$sSY8rawValue03RawB0QzvgTj
- _FMDRepairDeviceThisDeviceIdentifier
- _OBJC_CLASS_$_FMDRepairDevice
- _OBJC_CLASS_$_FMDRepairDeviceResult
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x5
- _xpc_copy_code_signing_identity_for_token
CStrings:
+ "%@ request is unexpectedly nil. This should never happen. controller=%@, actionCompletion=%p"
+ "02168E84-332F-481C-B7DE-7E80973B07BF"
+ "7275F1C6-332F-481C-B7DE-7E80973B07BF"
+ "@\"NSLock\""
+ "Could not get the BT paired device identifiers, error %@"
+ "Could not get the BT paired device identifiers, timeout error %ld"
+ "Error creating OTControl object: %@"
+ "FMDBluetoothDiscoveryCoordinator stopping current scan before restarting with new duration"
+ "FMDExtAccesoryManager LostHandler - only known devices are processed, ignoring device (%@) with MAC (%@)"
+ "FMDOctStatusUtil"
+ "FM_ACTIVATION_LOCK_ENABLED_VISION_TEXT"
+ "KeyState: %@"
+ "OT status does not have a self"
+ "OT status is not 'ready': %@"
+ "OT status self is not included in the peer list - selfID : %@, peerIDs: %@"
+ "OTControl status fetch error: %@"
+ "OTStatus: success"
+ "QCAction waiting for WipeAction to complete"
+ "T&L device coverage timed out"
+ "T@\"CBDevice\",&,V_bluetoothDevice"
+ "T@\"NSLock\",&,N,V_retryCountLock"
+ "T@\"NSString\",C,V_blePowerStatus"
+ "_ackWipeCommand:withStatus:completion:"
+ "_bluetoothPairedDeviceIdentifiers"
+ "_retryCountLock"
+ "_sendWipeAckWithCompletion:"
+ "_wipeNowWithCompletion:"
+ "contextDump"
+ "controlObject:error:"
+ "dynamicInfo"
+ "fetchOctStatusWithCompletion:"
+ "getDevicesWithFlags:completionHandler:"
+ "good"
+ "included"
+ "not removing still paired accessory = %@"
+ "peerID"
+ "performWipeWithCompletion:"
+ "retryCountLock"
+ "self not in peer list. Peers: %ld"
+ "selfAbsent"
+ "selfNotAPeer"
+ "setRetryCountLock:"
+ "stateNotReady"
+ "status:context:reply:"
+ "theftAndLossCoverageWithUDIDs:completion:"
+ "v40@0:8@16q24@?32"
- "02168E84-5DD8-4B19-9204-A79F04B33A32"
- "7275F1C6-7EB4-4406-B552-DC910FBFD07C"
- "Could not get ephemeral token for repair device: %@."
- "FMDExtAccesoryManager LostHandler - only BT classic devices are supported, ignoring device (%@) with MAC (%@)"
- "Got ephemeral token for repair device."
- "Request is not for the current device"
- "Sending request to repair device."
- "T@\"CBDevice\",&,N,V_bluetoothDevice"
- "T@\"NSString\",&,N,V_blePowerStatus"
- "Vv32@0:8@\"FMDRepairDeviceContext\"16@?<v@?@\"FMDRepairDeviceResult\"@\"NSError\">24"
- "_ackWipeCommand:withStatus:"
- "_enableRepairWithContext:callingClient:completion:"
- "_sendWipeAck"
- "_wipeNow"
- "auditToken"
- "deviceCoverageWithUDIDs: %@ timed out"
- "deviceEligibleForRepairWithContext for repairMode"
- "deviceEligibleForRepairWithContext for trade in mode"
- "deviceEligibleForRepairWithContext for unknown"
- "deviceEligibleForRepairWithContext:completion:"
- "dsid is nil"
- "enableRepairWithContext for repairMode"
- "enableRepairWithContext for trade in mode"
- "enableRepairWithContext:callingClient:completion:"
- "enableRepairWithContext:completion:"
- "getTheftAndLossCoverageWithUDIDs:reply:"
- "initWithClientIdentifier:isThisDevice:"
- "initWithEligibleDevices:devicesInRepairMode:"
- "isThisDevice"
- "performWipe"
- "repairDevice"
- "repairDeviceMode"
- "requestTheftAndLossCFUWithStrings:andReply:"
- "searchIdentifiers"
- "selectedDevices"
- "setCompletionHandlerForRepairDeviceRequest:thisDevice:completion:"
- "v32@0:8@\"FMDSharedConfigurationFollowUpEntry\"16@?<v@?@\"NSError\">24"

```
