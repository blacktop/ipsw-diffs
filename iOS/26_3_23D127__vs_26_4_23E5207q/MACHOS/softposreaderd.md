## softposreaderd

> `/usr/libexec/softposreaderd`

```diff

-41.3.0.0.0
-  __TEXT.__text: 0x2b50bc
-  __TEXT.__auth_stubs: 0x38b0
-  __TEXT.__objc_stubs: 0x100
+44.12.0.0.0
+  __TEXT.__text: 0x378610
+  __TEXT.__auth_stubs: 0x3900
+  __TEXT.__objc_stubs: 0x2120
   __TEXT.__objc_methlist: 0xae4
-  __TEXT.__const: 0x81d40
-  __TEXT.__cstring: 0x10625
-  __TEXT.__swift5_typeref: 0x1bc8
-  __TEXT.__objc_methname: 0x1f8f
-  __TEXT.__oslogstring: 0xb1ae
+  __TEXT.__const: 0x83200
+  __TEXT.__cstring: 0xd81b
+  __TEXT.__swift5_typeref: 0x1c32
+  __TEXT.__objc_methtype: 0x1035
+  __TEXT.__oslogstring: 0xb45e
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x5934
-  __TEXT.__swift5_proto: 0x9d8
-  __TEXT.__swift5_types: 0x3fc
-  __TEXT.__objc_classname: 0x1b6
-  __TEXT.__objc_methtype: 0xc22
-  __TEXT.__swift5_protos: 0xd8
+  __TEXT.__constg_swiftt: 0x59f0
+  __TEXT.__swift5_proto: 0x9f4
+  __TEXT.__swift5_types: 0x408
+  __TEXT.__objc_methname: 0x3b1d
+  __TEXT.__objc_classname: 0x12e3
+  __TEXT.__swift5_protos: 0xdc
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__unwind_info: 0x3730
-  __TEXT.__eh_frame: 0x8468
-  __DATA_CONST.__auth_got: 0x1c60
-  __DATA_CONST.__got: 0xbb8
-  __DATA_CONST.__auth_ptr: 0xb28
-  __DATA_CONST.__const: 0x14ee0
-  __DATA_CONST.__objc_classlist: 0x2b8
+  __TEXT.__unwind_info: 0x3710
+  __TEXT.__eh_frame: 0x82f8
+  __DATA_CONST.__auth_got: 0x1c88
+  __DATA_CONST.__got: 0xbe0
+  __DATA_CONST.__auth_ptr: 0xbd8
+  __DATA_CONST.__const: 0x14300
+  __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA.__objc_const: 0x6f40
+  __DATA.__objc_const: 0x7050
   __DATA.__objc_selrefs: 0xac8
   __DATA.__objc_data: 0x18b8
-  __DATA.__data: 0x9650
-  __DATA.__common: 0x650
-  __DATA.__bss: 0x10ce0
+  __DATA.__data: 0x97d8
+  __DATA.__common: 0x660
+  __DATA.__bss: 0x10f60
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSCLM.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 36653C11-1E34-305A-B982-EF023B2FEB32
-  Functions: 4571
-  Symbols:   1454
-  CStrings:  3028
+  UUID: F0BF915B-F8B0-3D36-9FC5-0E03FDBFCEBA
+  Functions: 4553
+  Symbols:   1463
+  CStrings:  3011
 
Symbols:
+ _$s10Foundation20ParseableFormatStylePAASo9NSDecimalaAAE0cD0VRszrlE6numberAGvgZ
+ _$s10Foundation4DataV15_RepresentationOys5UInt8VSicis
+ _$s10Foundation4DateVSQAAMc
+ _$s7SPRCore3TLVVSQAAMc
+ _$sSL2geoiySbx_xtFZTj
+ _$sSdSesWP
+ _$sSo9NSDecimala10FoundationE11FormatStyleVMa
+ _$sSo9NSDecimala10FoundationE2eeoiySbAB_ABtFZ
+ _$sSo9NSDecimala10FoundationE_6format7lenientABSS_AbCE11FormatStyleVSbtKcfC
+ _$sSo9NSDecimalaSE10FoundationMc
+ _$sSo9NSDecimalaSe10FoundationMc
+ _$ss15ContiguousArrayV28_allocateBufferUninitialized15minimumCapacitys01_abD0VyxGSi_tFZ
- _$s10Foundation13__DataStorageC27ensureUniqueBufferReference9growingTo5clearySi_SbtF
- __swift_FORCE_LOAD_$_swiftAccelerate
- _objc_retain_x9
CStrings:
+ "%s timer already started"
+ "%s timer started"
+ ", pinRequiredThresholds: "
+ ", pinSuppressionThresholds: "
+ "Certificate verification failed (AAA): %{public}s"
+ "Certificate verification failed (BAA) %{public}s"
+ "Certificate verification failed (BAA): %{public}s"
+ "Certificate verification failed (SES): %{public}s"
+ "Logging"
+ "Not overriding PIN: No boolean value for isSAF."
+ "Not overriding PIN: in SAF mode."
+ "Not requiring PIN: Amount less than or equal to threshold."
+ "Not requiring PIN: No threshold set for AID %s."
+ "Not requiring PIN: PIN already required."
+ "Not requiring PIN: no boolean value for PIN required."
+ "Not suppressing PIN: Amount greater than or equal to threshold."
+ "Not suppressing PIN: No boolean value for PIN required."
+ "Not suppressing PIN: No threshold set for AID %s."
+ "Not suppressing PIN: PIN not required."
+ "OTA decoding error: %@"
+ "PayAppletTagParserProtocol"
+ "Requiring PIN."
+ "Suppressing PIN."
+ "_TtC14softposreaderd25DefaultPayAppletTagParser"
+ "findDefaultTags(from:populate:postAnalyticsWith:)"
+ "init(mpocMonitorManager:mpocAttestationManager:safAllowedDuration:queue:certificateManager:signerFactory:secureTimeKeeper:auditor:analytics:managedData:systemInfo:secureElement:enforceJCOPVersion:profileManager:launchFeedbackFramework:payAppletTagParser:)"
+ "payAppletTagParser"
+ "pinRequiredThresholds"
+ "pinSuppressionThresholds"
- "Cannot refresh token when not online"
- "Certificate verification failed: %s"
- "Empty MPOC monitor backend returned response"
- "OTA decoding error: %s"
- "PIN timer already started"
- "PIN timer started"
- "cardEffectiveState"
- "cardExpirationState"
- "clearTransactionAndCompleteOperation()"
- "closePayment(isClearingTransaction:)"
- "errorIndicationMsgOnError"
- "errorIndicationStatusWord"
- "init(mpocMonitorManager:mpocAttestationManager:safAllowedDuration:queue:certificateManager:signerFactory:secureTimeKeeper:auditor:analytics:managedData:systemInfo:secureElement:enforceJCOPVersion:profileManager:launchFeedbackFramework:)"
- "isPINBypassEnabled"
- "kernelIdentityKeyAttestation"
- "languagePreference"
- "payAppletFinalStatus"
- "switchInterfaceOrNoCVMSuccess"
- "transactionResultData"

```
