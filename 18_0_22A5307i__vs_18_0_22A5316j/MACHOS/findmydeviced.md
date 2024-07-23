## findmydeviced

> `/usr/libexec/findmydeviced`

```diff

-438.30.6.4.4
-  __TEXT.__text: 0x23cf44
+438.30.7.10.7
+  __TEXT.__text: 0x23a8ac
   __TEXT.__auth_stubs: 0xe60
-  __TEXT.__objc_stubs: 0x16500
-  __TEXT.__objc_methlist: 0xdfcc
-  __TEXT.__const: 0x2cd50
+  __TEXT.__objc_stubs: 0x16740
+  __TEXT.__objc_methlist: 0xe0d4
+  __TEXT.__const: 0x2cd30
   __TEXT.__gcc_except_tab: 0x2b40
-  __TEXT.__objc_methname: 0x1bf01
-  __TEXT.__oslogstring: 0x106b9
-  __TEXT.__cstring: 0x8869
-  __TEXT.__objc_classname: 0x1a57
-  __TEXT.__objc_methtype: 0x3007
+  __TEXT.__objc_methname: 0x1c1b6
+  __TEXT.__oslogstring: 0x108c8
+  __TEXT.__cstring: 0x8981
+  __TEXT.__objc_classname: 0x1a6e
+  __TEXT.__objc_methtype: 0x3056
   __TEXT.__info_plist: 0x57c
-  __TEXT.__unwind_info: 0x3260
+  __TEXT.__unwind_info: 0x3290
   __TEXT.__eh_frame: 0x50
   __DATA_CONST.__auth_got: 0x740
-  __DATA_CONST.__got: 0x8b0
+  __DATA_CONST.__got: 0x8c8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xc9e0
-  __DATA_CONST.__cfstring: 0xa620
-  __DATA_CONST.__objc_classlist: 0x6b8
+  __DATA_CONST.__const: 0xc9f8
+  __DATA_CONST.__cfstring: 0xa720
+  __DATA_CONST.__objc_classlist: 0x6c0
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x558
+  __DATA_CONST.__objc_superrefs: 0x560
   __DATA_CONST.__objc_intobj: 0x498
   __DATA_CONST.__objc_doubleobj: 0x5a0
   __DATA_CONST.__objc_arraydata: 0x5f8

   __DATA_CONST.__objc_floatobj: 0x30
   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__linkguard: 0xe
-  __DATA.__objc_const: 0x1c0f8
-  __DATA.__objc_selrefs: 0x6480
-  __DATA.__objc_ivar: 0x109c
-  __DATA.__objc_data: 0x4330
+  __DATA.__objc_const: 0x1c268
+  __DATA.__objc_selrefs: 0x6518
+  __DATA.__objc_ivar: 0x10a8
+  __DATA.__objc_data: 0x4380
   __DATA.__data: 0x2480
-  __DATA.__bss: 0x7c0
+  __DATA.__bss: 0x7d0
   __DATA.__common: 0x69
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5780
-  Symbols:   577
-  CStrings:  8420
+  Functions: 5812
+  Symbols:   580
+  CStrings:  8466
 
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
