## findmydeviced

> `/usr/libexec/findmydeviced`

```diff

-424.7.0.0.0
-  __TEXT.__text: 0x23a52c
+424.9.0.0.0
+  __TEXT.__text: 0x23c1d0
   __TEXT.__auth_stubs: 0xdf0
-  __TEXT.__objc_stubs: 0x16480
-  __TEXT.__objc_methlist: 0xdfa0
+  __TEXT.__objc_stubs: 0x166c0
+  __TEXT.__objc_methlist: 0xe0a8
   __TEXT.__const: 0x2e1f0
   __TEXT.__gcc_except_tab: 0x1ef0
-  __TEXT.__objc_methname: 0x1bfad
-  __TEXT.__oslogstring: 0x10673
-  __TEXT.__cstring: 0x87af
-  __TEXT.__objc_classname: 0x1a57
-  __TEXT.__objc_methtype: 0x3007
+  __TEXT.__objc_methname: 0x1c25d
+  __TEXT.__oslogstring: 0x10882
+  __TEXT.__cstring: 0x88c7
+  __TEXT.__objc_classname: 0x1a6e
+  __TEXT.__objc_methtype: 0x3056
   __TEXT.__info_plist: 0x57c
-  __TEXT.__unwind_info: 0x326c
+  __TEXT.__unwind_info: 0x32a4
   __TEXT.__eh_frame: 0x50
   __DATA_CONST.__auth_got: 0x708
-  __DATA_CONST.__got: 0x498
+  __DATA_CONST.__got: 0x4a0
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0xc9a8
-  __DATA_CONST.__cfstring: 0xa5c0
-  __DATA_CONST.__objc_classlist: 0x6b8
+  __DATA_CONST.__const: 0xca68
+  __DATA_CONST.__cfstring: 0xa6c0
+  __DATA_CONST.__objc_classlist: 0x6c0
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_classrefs: 0xa70
-  __DATA_CONST.__objc_superrefs: 0x558
+  __DATA_CONST.__objc_classrefs: 0xa88
+  __DATA_CONST.__objc_superrefs: 0x560
   __DATA_CONST.__objc_intobj: 0x480
   __DATA_CONST.__objc_doubleobj: 0x5a0
   __DATA_CONST.__objc_arraydata: 0x5f8

   __DATA_CONST.__objc_floatobj: 0x30
   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__linkguard: 0xe
-  __DATA.__objc_const: 0x1c090
-  __DATA.__objc_selrefs: 0x6460
-  __DATA.__objc_ivar: 0x1098
-  __DATA.__objc_data: 0x4330
+  __DATA.__objc_const: 0x1c200
+  __DATA.__objc_selrefs: 0x64f8
+  __DATA.__objc_ivar: 0x10a4
+  __DATA.__objc_data: 0x4380
   __DATA.__data: 0x2480
-  __DATA.__bss: 0x7c0
+  __DATA.__bss: 0x7d0
   __DATA.__common: 0x74
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5935
-  Symbols:   568
-  CStrings:  8404
+  Functions: 5969
+  Symbols:   571
+  CStrings:  8450
 
Symbols:
+ _FMDRepairDeviceThisDeviceIdentifier
+ _OBJC_CLASS_$_FMDRepairDevice
+ _OBJC_CLASS_$_FMDRepairDeviceResult
CStrings:
+ "${scheme}://${hostname}/fmipservice/findme/%!@(MISSING)/${udid}/repairDeviceV2"
+ "Cannot find an ephemeral token, please provide one"
+ "Checking ratchet for the context: %!l(MISSING)u."
+ "Could not get ephemeral token for repair device: %!@(MISSING)."
+ "Default Button Text"
+ "FMDRepairDeviceRequest"
+ "Failed to instantiate authContext: %!@(MISSING)"
+ "Got ephemeral token for repair device."
+ "Ratchet Permitted for this context: %!l(MISSING)u. Allowing disable FMIP. Permission Granted, peforming unregister"
+ "Request is not for the current device"
+ "Sending request to repair device."
+ "T@\"FMDAccount\",C,N,V_accountForRepair"
+ "T@\"NSString\",C,N,V_dsid"
+ "T@\"NSString\",C,N,V_ephemeralToken"
+ "Vv32@0:8@\"FMDRepairDeviceContext\"16@?<v@?@\"FMDRepairDeviceResult\"@\"NSError\">24"
+ "We are in a ratchet state %!l(MISSING)u. Denying disable FMIP."
+ "_accountForRepair"
+ "_enableRepairWithContext:completion:"
+ "_ephemeralToken"
+ "_hasRepairDeviceAccessEntitlement"
+ "accountForRepair"
+ "com.apple.icloud.FindMyDevice.RepairDevice.access"
+ "deviceEligibleForRepairWithContext for repairMode"
+ "deviceEligibleForRepairWithContext for trade in mode"
+ "deviceEligibleForRepairWithContext for unknown"
+ "deviceEligibleForRepairWithContext:completion:"
+ "dsid is nil"
+ "enableRepairWithContext for repairMode"
+ "enableRepairWithContext for trade in mode"
+ "enableRepairWithContext:completion:"
+ "ephemeralToken"
+ "ephemeralTokenForUserWithCompletion:"
+ "initWithClientIdentifier:isThisDevice:"
+ "initWithDeviceIdentifier:ephemeralToken:dsid:"
+ "initWithEligibleDevices:devicesInRepairMode:"
+ "isThisDevice"
+ "repairDevice"
+ "repairDeviceMode"
+ "requestingUserPrsId"
+ "searchIdentifiers"
+ "selectedDevices"
+ "setAccountForRepair:"
+ "setCompletionHandlerForRepairDeviceRequest:thisDevice:completion:"
+ "setDefaultButtonString:"
+ "setEphemeralToken:"
+ "setIsEphemeral:"
- "No ratchet defined for this context: %!l(MISSING)u. Allowing disable FMIP."

```
