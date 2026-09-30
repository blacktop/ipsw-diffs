## findmydeviced

> `/usr/libexec/findmydeviced`

```diff

-455.30.6.9.18
-  __TEXT.__text: 0x22df1c
+455.30.6.9.20
+  __TEXT.__text: 0x22d160
   __TEXT.__auth_stubs: 0x10d0
-  __TEXT.__objc_stubs: 0x172e0
-  __TEXT.__objc_methlist: 0xf9ac
+  __TEXT.__objc_stubs: 0x173a0
+  __TEXT.__objc_methlist: 0xf9f4
   __TEXT.__const: 0x2dc60
-  __TEXT.__gcc_except_tab: 0x2dcc
-  __TEXT.__objc_methname: 0x1d0d3
-  __TEXT.__oslogstring: 0x11e1c
-  __TEXT.__cstring: 0x9298
-  __TEXT.__objc_classname: 0x1a9a
-  __TEXT.__objc_methtype: 0x3175
+  __TEXT.__gcc_except_tab: 0x2e24
+  __TEXT.__objc_methname: 0x1d0d9
+  __TEXT.__oslogstring: 0x11d50
+  __TEXT.__cstring: 0x90d8
+  __TEXT.__objc_classname: 0x1aa7
+  __TEXT.__objc_methtype: 0x31a7
   __TEXT.__constg_swiftt: 0x58
   __TEXT.__swift5_typeref: 0x77
   __TEXT.__swift5_reflstr: 0x8

   __TEXT.__swift5_types: 0x4
   __TEXT.__swift_as_entry: 0x24
   __TEXT.__swift_as_ret: 0x24
-  __TEXT.__unwind_info: 0x3678
+  __TEXT.__unwind_info: 0x3688
   __TEXT.__eh_frame: 0x3a0
   __DATA_CONST.__auth_got: 0x878
-  __DATA_CONST.__got: 0x8e8
+  __DATA_CONST.__got: 0x8f8
   __DATA_CONST.__auth_ptr: 0x20
   __DATA_CONST.__const: 0xecf8
-  __DATA_CONST.__cfstring: 0xab80
-  __DATA_CONST.__objc_classlist: 0x6e0
+  __DATA_CONST.__cfstring: 0xab20
+  __DATA_CONST.__objc_classlist: 0x6e8
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x1e0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x568
+  __DATA_CONST.__objc_superrefs: 0x570
   __DATA_CONST.__objc_intobj: 0x420
   __DATA_CONST.__objc_doubleobj: 0x5a0
   __DATA_CONST.__objc_arraydata: 0x5f8

   __DATA_CONST.__objc_floatobj: 0x30
   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__linkguard: 0xe
-  __DATA.__objc_const: 0x19f40
-  __DATA.__objc_selrefs: 0x6950
-  __DATA.__objc_ivar: 0x10f0
-  __DATA.__objc_data: 0x4540
+  __DATA.__objc_const: 0x1a010
+  __DATA.__objc_selrefs: 0x6978
+  __DATA.__objc_ivar: 0x10f4
+  __DATA.__objc_data: 0x4590
   __DATA.__data: 0x2400
   __DATA.__bss: 0x818
   __DATA.__common: 0x69

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5379220D-ED2B-34CA-B553-B09E5D595FDF
-  Functions: 6137
-  Symbols:   640
-  CStrings:  10109
+  UUID: 5F7A3E13-B214-346A-B62D-758B2DE98890
+  Functions: 6128
+  Symbols:   642
+  CStrings:  10096
 
Symbols:
+ _FMDRepairDeviceThisDeviceIdentifier
+ _OBJC_CLASS_$_FMDRepairDevice
CStrings:
+ "@\"NSExtension\""
+ "@56@0:8@16@24@32@40q48"
+ "Extension request invalidated (extension='%@', request='%@')"
+ "Extension with id = %@ not found"
+ "FMDExtExtension"
+ "Request begin (extension='%@', request='%@')"
+ "Request cancelled (extension='%@', request='%@')"
+ "Request completed (extension='%@', request='%@')"
+ "Request interrupted (extension='%@', request='%@')"
+ "Request is not for the current device"
+ "T@\"NSExtension\",&,V_extension"
+ "T@\"NSObject<OS_dispatch_queue>\",&,V_queue"
+ "T@\"NSUUID\",&,V_requestIdentifier"
+ "Unable to get connection to extension %@"
+ "XPCConnection interrupted (extension='%@', request='%@', connection='%@')"
+ "XPCConnection invalidated (extension='%@', request='%@', connection='%@')"
+ "_extension"
+ "_requestIdentifier"
+ "allExtensionIdentifiers"
+ "beginExtensionRequestWithOptions failed (extension='%@', error='%@')"
+ "cancelExtensionRequestWithIdentifier:"
+ "com.apple.icloud.findmydevice.fmd-ext-extension"
+ "connectWithDelegate:"
+ "deviceEligibleForRepairWithContext for repairMode"
+ "deviceEligibleForRepairWithContext for trade in mode"
+ "deviceEligibleForRepairWithContext:completion:"
+ "extension"
+ "extensionWithIdentifier:"
+ "initWithClientIdentifier:isThisDevice:"
+ "initWithDeviceIdentifier:ephemeralToken:dsid:callingClient:mode:"
+ "initWithExtension:"
+ "invalidateRequestWithIdentifier:"
+ "isThisDevice"
+ "repair"
+ "requestIdentifier"
+ "requestTheftAndLossCFUWithStrings:andReply:"
+ "searchIdentifiers"
+ "selectedDevices"
+ "setExtension:"
+ "setRequestIdentifier:"
+ "setupCompletionBlocks"
+ "v32@0:8@\"FMDSharedConfigurationFollowUpEntry\"16@?<v@?@\"NSError\">24"
- "#ext Extension with id = %@ not found"
- "#ext Unable to get connection to extension %@"
- "#ext beginExtensionRequestWithOptions failed with error  %@"
- "#ext extension request completed for %@"
- "#ext extension request interrupted for %@"
- "%s: Cleared CFU for %@"
- "%s: Failed with error: %@"
- "%s: Requested a CFU for %@"
- "%s: Timed out"
- "%s: timed out"
- "-[FMDFMIPXPCServer clearRepairCFUWithDeviceID:reply:]"
- "-[FMDFMIPXPCServer postRepairCFUWithDeviceID:reply:]"
- "-[FMDSharedConfigurationManager clearRepairCFUWithDeviceID:completion:]_block_invoke"
- "-[FMDSharedConfigurationManager clearRepairCFUWithDeviceID:completion:]_block_invoke_2"
- "-[FMDSharedConfigurationManager postRepairCFUWithDeviceID:completion:]_block_invoke"
- "-[FMDSharedConfigurationManager postRepairCFUWithDeviceID:completion:]_block_invoke_2"
- "@64@0:8@16@24@32@40q48@56"
- "@72@0:8@16@24@32@40q48@56@64"
- "AUTHORIZE_REPAIR"
- "AUTHORIZE_REPAIR_TEARDOWN"
- "Clear repair CFU for deviceID %@"
- "Cleared the Enable Repair CFU for %@"
- "Create repair CFU for deviceID %@"
- "Enable Repair CFU posted for %@"
- "Failed to clear the Enable Repair CFU for %@ with error: %@"
- "Failed to post Enable Repair CFU for %@ with error: %@"
- "Missing device serial number."
- "No serial number or device identifier"
- "REL"
- "REPAIR"
- "Repair CFU intent is missing deviceID"
- "T@\"NSString\",R,N,V_deviceIdentifier"
- "T@\"NSString\",R,N,V_serialNumber"
- "Unhandled cmd %@"
- "XPC connection interrupted for identifier %@ and  connection = %@"
- "XPC connection invalidated for identifier %@ and conection = %@"
- "XPC error for %s: %li"
- "_deviceIdentifier"
- "_handleRepairCFUIntent:serverContext:"
- "_initWithAccount:ephemeralToken:dsid:callingClient:mode:serialNumber:deviceIdentifier:"
- "_setCompleteionBlocksForExtension:"
- "clearRepairCFUWithDeviceID:completion:"
- "clearRepairCFUWithDeviceID:reply:"
- "deviceForRepair"
- "deviceIdentifier"
- "extension request cancelled for %@"
- "initWithAccount:ephemeralToken:dsid:callingClient:mode:deviceIdentifier:"
- "initWithAccount:ephemeralToken:dsid:callingClient:mode:serialNumber:"
- "postRepairCFUWithDeviceID:completion:"
- "postRepairCFUWithDeviceID:reply:"
- "processRepairRequest:"
- "processRepairTeardownRequest:"

```
