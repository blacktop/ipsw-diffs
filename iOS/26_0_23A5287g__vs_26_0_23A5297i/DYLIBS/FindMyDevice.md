## FindMyDevice

> `/System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice`

```diff

-455.30.6.9.11
-  __TEXT.__text: 0x2229c
+455.30.6.9.18
+  __TEXT.__text: 0x2282c
   __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_methlist: 0x2744
+  __TEXT.__objc_methlist: 0x2794
   __TEXT.__const: 0xb8
-  __TEXT.__oslogstring: 0x2a5c
-  __TEXT.__cstring: 0x40a8
+  __TEXT.__oslogstring: 0x2af3
+  __TEXT.__cstring: 0x40bc
   __TEXT.__gcc_except_tab: 0x2d4
-  __TEXT.__unwind_info: 0x7c8
+  __TEXT.__unwind_info: 0x7e0
   __TEXT.__objc_classname: 0x63d
-  __TEXT.__objc_methname: 0x5073
-  __TEXT.__objc_methtype: 0x11f4
-  __TEXT.__objc_stubs: 0x3780
+  __TEXT.__objc_methname: 0x5099
+  __TEXT.__objc_methtype: 0x11f9
+  __TEXT.__objc_stubs: 0x3800
   __DATA_CONST.__got: 0x188
-  __DATA_CONST.__const: 0x11a0
+  __DATA_CONST.__const: 0x11c8
   __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12a0
+  __DATA_CONST.__objc_selrefs: 0x12c8
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x110
   __AUTH_CONST.__auth_got: 0x240
-  __AUTH_CONST.__const: 0x4e0
-  __AUTH_CONST.__cfstring: 0x3bc0
-  __AUTH_CONST.__objc_const: 0x7270
+  __AUTH_CONST.__const: 0x500
+  __AUTH_CONST.__cfstring: 0x3c20
+  __AUTH_CONST.__objc_const: 0x7258
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x6e0
-  __DATA.__objc_ivar: 0x21c
+  __DATA.__objc_ivar: 0x218
   __DATA.__data: 0x970
   __DATA.__bss: 0x128
   __DATA.__common: 0x8

   - /System/Library/PrivateFrameworks/InternationalSupport.framework/InternationalSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 32F55358-6EFA-3B86-9F2A-308A893B5AFB
-  Functions: 988
-  Symbols:   3936
-  CStrings:  2400
+  UUID: 0F1DC1F8-DB23-3FB1-83EE-5AD57F5C755B
+  Functions: 996
+  Symbols:   3961
+  CStrings:  2412
 
Symbols:
+ -[FMDFMIPManager(Private) primaryAppleAccountRemoved]
+ -[FMDRepairDevice deviceIdentifier]
+ -[FMDRepairDevice initWithDeviceIdentifier:]
+ -[FMDRepairDevice initWithSerialNumber:]
+ -[FMDRepairDevice serialNumber]
+ -[FMDRepairDevice setDeviceIdentifier:]
+ -[FMDRepairDevice setSerialNumber:]
+ -[FMDRepairDeviceContext deviceForRepair]
+ -[FMDRepairDeviceContext setDeviceForRepair:]
+ -[FMDSharedConfiguration _followUpFileURL:]
+ -[FMDSharedConfiguration _followUpFileURL:].cold.1
+ -[FMDSharedConfiguration _followUpFileURL:].cold.2
+ -[FMDSharedConfiguration clearRepairCFUWithDeviceID:reply:]
+ -[FMDSharedConfiguration postRepairCFUWithDeviceID:reply:]
+ _OBJC_IVAR_$_FMDRepairDevice._deviceIdentifier
+ _OBJC_IVAR_$_FMDRepairDevice._serialNumber
+ _OBJC_IVAR_$_FMDRepairDeviceContext._deviceForRepair
+ ___53-[FMDFMIPManager(Private) primaryAppleAccountRemoved]_block_invoke
+ ___53-[FMDFMIPManager(Private) primaryAppleAccountRemoved]_block_invoke.cold.1
+ ___58-[FMDSharedConfiguration postRepairCFUWithDeviceID:reply:]_block_invoke
+ ___58-[FMDSharedConfiguration postRepairCFUWithDeviceID:reply:]_block_invoke_2
+ ___59-[FMDSharedConfiguration clearRepairCFUWithDeviceID:reply:]_block_invoke
+ ___59-[FMDSharedConfiguration clearRepairCFUWithDeviceID:reply:]_block_invoke_2
+ ___block_literal_global.25
+ _kFMDCoreFollowUpRepairTimestampKey
+ _kFMDRepairIntentCommandKey
+ _kFMDRepairIntentCommandRepair
+ _kFMDRepairIntentCommandRepairTeardown
+ _kFMDRepairIntentDeviceKey
+ _kIntentRepairCFUKey
+ _objc_msgSend$_followUpFileURL:
+ _objc_msgSend$clearRepairCFUWithDeviceID:reply:
+ _objc_msgSend$copy
+ _objc_msgSend$postRepairCFUWithDeviceID:reply:
+ _objc_msgSend$primaryAppleAccountRemoved
- -[FMDFMIPManager deviceEligibleForRepairWithContext:completion:]
- -[FMDRepairDevice identifier]
- -[FMDRepairDevice initWithClientIdentifier:isThisDevice:]
- -[FMDRepairDevice isThisDevice]
- -[FMDRepairDeviceContext searchIdentifiers]
- -[FMDRepairDeviceContext selectedDevices]
- -[FMDRepairDeviceContext setSearchIdentifiers:]
- -[FMDRepairDeviceContext setSelectedDevices:]
- -[FMDSharedConfiguration signOutTimestampFileURL].cold.1
- -[FMDSharedConfiguration signOutTimestampFileURL].cold.2
- _FMDRepairDeviceThisDeviceIdentifier
- _OBJC_IVAR_$_FMDRepairDevice._identifier
- _OBJC_IVAR_$_FMDRepairDevice._isThisDevice
- _OBJC_IVAR_$_FMDRepairDeviceContext._searchIdentifiers
- _OBJC_IVAR_$_FMDRepairDeviceContext._selectedDevices
- ___64-[FMDFMIPManager deviceEligibleForRepairWithContext:completion:]_block_invoke
- ___64-[FMDFMIPManager deviceEligibleForRepairWithContext:completion:]_block_invoke.cold.1
- _objc_msgSend$deviceEligibleForRepairWithContext:completion:
CStrings:
+ "@\"FMDRepairDevice\""
+ "AUTHORIZE_REPAIR"
+ "AUTHORIZE_REPAIR_TEARDOWN"
+ "Cleared a CFU for deviceID: %@"
+ "Failure to request a CFU for deviceID: %@ with error: %@"
+ "Framework (Private) : primaryAppleAccountRemoved"
+ "REL"
+ "RepairTimestamp"
+ "Requested a CFU for deviceID: %@"
+ "T@\"FMDRepairDevice\",&,N,V_deviceForRepair"
+ "T@\"NSString\",C,N,V_deviceIdentifier"
+ "XPC error for primaryAppleAccountRemoved: %li"
+ "_deviceForRepair"
+ "_deviceIdentifier"
+ "_followUpFileURL:"
+ "clearRepairCFUWithDeviceID:completion:"
+ "clearRepairCFUWithDeviceID:reply:"
+ "copy"
+ "device"
+ "deviceForRepair"
+ "deviceIdentifier"
+ "initWithDeviceIdentifier:"
+ "initWithSerialNumber:"
+ "postRepairCFUWithDeviceID:completion:"
+ "postRepairCFUWithDeviceID:reply:"
+ "primaryAppleAccountRemoved"
+ "setDeviceForRepair:"
+ "setDeviceIdentifier:"
- "@28@0:8@16B24"
- "FMDRepairDeviceThisDeviceIdentifier"
- "T@\"NSArray\",&,N,V_searchIdentifiers"
- "T@\"NSArray\",&,N,V_selectedDevices"
- "T@\"NSString\",R,N,V_identifier"
- "TB,R,N,V_isThisDevice"
- "XPC error for deviceEligibleForRepairWithContext:completion: %li"
- "_isThisDevice"
- "_searchIdentifiers"
- "_selectedDevices"
- "deviceEligibleForRepairWithContext:completion:"
- "initWithClientIdentifier:isThisDevice:"
- "isThisDevice"
- "requestTheftAndLossCFUWithStrings:andReply:"
- "searchIdentifiers"
- "selectedDevices"
- "setSearchIdentifiers:"
- "setSelectedDevices:"

```
