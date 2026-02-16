## FindMyDevice

> `/System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice`

```diff

-455.33.11.19.3
-  __TEXT.__text: 0x22698
-  __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_methlist: 0x2814
+455.34.7.18.21
+  __TEXT.__text: 0x230cc
+  __TEXT.__auth_stubs: 0x410
+  __TEXT.__objc_methlist: 0x2884
   __TEXT.__const: 0xb8
-  __TEXT.__oslogstring: 0x2ac7
-  __TEXT.__cstring: 0x4105
-  __TEXT.__gcc_except_tab: 0x2d4
-  __TEXT.__unwind_info: 0x7e8
-  __TEXT.__objc_classname: 0x669
-  __TEXT.__objc_methname: 0x5172
-  __TEXT.__objc_methtype: 0x127f
+  __TEXT.__oslogstring: 0x2af1
+  __TEXT.__cstring: 0x4147
+  __TEXT.__gcc_except_tab: 0x2e4
+  __TEXT.__unwind_info: 0xa08
+  __TEXT.__objc_classname: 0x6a2
+  __TEXT.__objc_methname: 0x5174
+  __TEXT.__objc_methtype: 0x11ed
   __TEXT.__objc_stubs: 0x3780
   __DATA_CONST.__got: 0x188
-  __DATA_CONST.__const: 0x11c8
-  __DATA_CONST.__objc_classlist: 0x140
+  __DATA_CONST.__const: 0x11f0
+  __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12c8
+  __DATA_CONST.__objc_selrefs: 0x12d8
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x118
-  __AUTH_CONST.__auth_got: 0x240
+  __AUTH_CONST.__auth_got: 0x218
   __AUTH_CONST.__const: 0x500
-  __AUTH_CONST.__cfstring: 0x3c60
-  __AUTH_CONST.__objc_const: 0x7488
+  __AUTH_CONST.__cfstring: 0x3ce0
+  __AUTH_CONST.__objc_const: 0x7758
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x730
+  __AUTH.__objc_data: 0x7d0
   __DATA.__objc_ivar: 0x228
   __DATA.__data: 0x970
   __DATA.__bss: 0x128

   - /System/Library/PrivateFrameworks/InternationalSupport.framework/InternationalSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0AE748F9-D834-33CA-AAD7-CD7FF19093C5
-  Functions: 1004
-  Symbols:   3993
-  CStrings:  2424
+  UUID: D6F436AD-6070-362D-ADE5-FEA7058A4262
+  Functions: 1020
+  Symbols:   4077
+  CStrings:  2436
 
Symbols:
+ +[FMDRepairDevice objectForThisDevice]
+ +[FMDRepairDeviceLookupContext fromDevices:]
+ +[FMDRepairDeviceLookupContext supportsSecureCoding]
+ +[FMDRepairDeviceLookupResult supportsSecureCoding]
+ -[FMDFMIPManager getRepairStateWithContext:reply:]
+ -[FMDRepairDeviceLookupContext devicesToLookUp]
+ -[FMDRepairDeviceLookupContext encodeWithCoder:]
+ -[FMDRepairDeviceLookupContext initWithCoder:]
+ -[FMDRepairDeviceLookupResult devicesInRepairMode]
+ -[FMDRepairDeviceLookupResult encodeWithCoder:]
+ -[FMDRepairDeviceLookupResult initWithCoder:]
+ -[FMDSharedConfiguration _followUpFileURL:]
+ -[FMDSharedConfiguration _followUpFileURL:].cold.1
+ -[FMDSharedConfiguration _followUpFileURL:].cold.2
+ _OBJC_CLASS_$_FMDRepairDeviceLookupContext
+ _OBJC_CLASS_$_FMDRepairDeviceLookupResult
+ _OBJC_METACLASS_$_FMDRepairDeviceLookupContext
+ _OBJC_METACLASS_$_FMDRepairDeviceLookupResult
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __OBJC_$_CLASS_METHODS_FMDRepairDeviceLookupContext
+ __OBJC_$_CLASS_METHODS_FMDRepairDeviceLookupResult
+ __OBJC_$_CLASS_PROP_LIST_FMDRepairDeviceLookupContext
+ __OBJC_$_CLASS_PROP_LIST_FMDRepairDeviceLookupResult
+ __OBJC_$_INSTANCE_METHODS_FMDRepairDeviceLookupContext
+ __OBJC_$_INSTANCE_METHODS_FMDRepairDeviceLookupResult
+ __OBJC_$_PROP_LIST_FMDRepairDeviceLookupContext
+ __OBJC_$_PROP_LIST_FMDRepairDeviceLookupResult
+ __OBJC_CLASS_PROTOCOLS_$_FMDRepairDeviceLookupContext
+ __OBJC_CLASS_PROTOCOLS_$_FMDRepairDeviceLookupResult
+ __OBJC_CLASS_RO_$_FMDRepairDeviceLookupContext
+ __OBJC_CLASS_RO_$_FMDRepairDeviceLookupResult
+ __OBJC_METACLASS_RO_$_FMDRepairDeviceLookupContext
+ __OBJC_METACLASS_RO_$_FMDRepairDeviceLookupResult
+ _kFMDCoreFollowUpRepairTimestampKey
+ _kFMDRepairIntentCommandKey
+ _kFMDRepairIntentCommandRepair
+ _kFMDRepairIntentCommandRepairTeardown
+ _kFMDRepairIntentDeviceKey
+ _objc_msgSend$_followUpFileURL:
+ _objc_msgSend$initWithClientIdentifier:isThisDevice:
+ _objc_retainAutoreleasedReturnValue
- -[FMDFMIPManager deviceEligibleForRepairWithContext:completion:]
- -[FMDSharedConfiguration signOutTimestampFileURL].cold.1
- -[FMDSharedConfiguration signOutTimestampFileURL].cold.2
- ___53-[FMDFMIPManager enableRepairWithContext:completion:]_block_invoke
- ___53-[FMDFMIPManager enableRepairWithContext:completion:]_block_invoke.cold.1
- ___64-[FMDFMIPManager deviceEligibleForRepairWithContext:completion:]_block_invoke
- ___64-[FMDFMIPManager deviceEligibleForRepairWithContext:completion:]_block_invoke.cold.1
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$deviceEligibleForRepairWithContext:completion:
- _objc_msgSend$enableRepairWithContext:completion:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x8
CStrings:
+ "AUTHORIZE_REPAIR"
+ "AUTHORIZE_REPAIR_TEARDOWN"
+ "FMDRepairDeviceLookupContext"
+ "FMDRepairDeviceLookupResult"
+ "RepairTimestamp"
+ "T@\"NSArray\",R,C,N"
+ "T@\"NSArray\",R,N"
+ "_followUpFileURL:"
+ "device"
+ "devicesToLookUp"
+ "enableRepairWithContext:completion: is deprecated and stubbed out - returning nil"
+ "fromDevices:"
+ "getRepairStateWithContext:reply:"
+ "getRepairStateWithContext:reply: is deprecated and stubbed out - returning nil"
+ "objectForThisDevice"
+ "theftAndLossCoverageWithUDIDs:completion:"
- "Vv32@0:8@\"FMDRepairDeviceContext\"16@?<v@?@\"FMDRepairDeviceResult\"@\"NSError\">24"
- "XPC error for deviceEligibleForRepairWithContext:completion: %li"
- "XPC error for enableRepairWithContext:completion: %li"
- "deviceEligibleForRepairWithContext:completion:"
- "getTheftAndLossCoverageWithUDIDs:reply:"
- "requestTheftAndLossCFUWithString:andReply:"
- "requestTheftAndLossCFUWithStrings:andReply:"
- "v32@0:8@\"FMDSharedConfigurationFollowUpEntry\"16@?<v@?@\"NSError\">24"

```
