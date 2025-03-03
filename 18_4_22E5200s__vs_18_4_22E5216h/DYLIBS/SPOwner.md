## SPOwner

> `/System/Library/PrivateFrameworks/SPOwner.framework/SPOwner`

```diff

-396.34.7.11.29
-  __TEXT.__text: 0x70c4c
+396.34.7.11.35
+  __TEXT.__text: 0x73ac4
   __TEXT.__auth_stubs: 0xc60
-  __TEXT.__objc_methlist: 0xad64
-  __TEXT.__cstring: 0x64b7
+  __TEXT.__objc_methlist: 0xb13c
+  __TEXT.__cstring: 0x6687
   __TEXT.__const: 0x3e8
   __TEXT.__gcc_except_tab: 0x1c20
-  __TEXT.__oslogstring: 0x7498
+  __TEXT.__oslogstring: 0x7588
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x124
   __TEXT.__swift5_fieldmd: 0xfc

   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift5_capture: 0x50
   __TEXT.__swift_as_ret: 0x18
-  __TEXT.__unwind_info: 0x24f8
-  __TEXT.__eh_frame: 0x250
-  __TEXT.__objc_classname: 0x124f
-  __TEXT.__objc_methname: 0x122da
-  __TEXT.__objc_methtype: 0x385b
-  __TEXT.__objc_stubs: 0xa740
-  __DATA_CONST.__got: 0x590
-  __DATA_CONST.__const: 0x2040
-  __DATA_CONST.__objc_classlist: 0x400
-  __DATA_CONST.__objc_protolist: 0x1b8
+  __TEXT.__unwind_info: 0x25c0
+  __TEXT.__eh_frame: 0x278
+  __TEXT.__objc_classname: 0x1311
+  __TEXT.__objc_methname: 0x12578
+  __TEXT.__objc_methtype: 0x38ca
+  __TEXT.__objc_stubs: 0xa7e0
+  __DATA_CONST.__got: 0x5a0
+  __DATA_CONST.__const: 0x2048
+  __DATA_CONST.__objc_classlist: 0x418
+  __DATA_CONST.__objc_protolist: 0x1d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3910
-  __DATA_CONST.__objc_protorefs: 0xc8
-  __DATA_CONST.__objc_superrefs: 0x338
+  __DATA_CONST.__objc_selrefs: 0x3998
+  __DATA_CONST.__objc_protorefs: 0xd8
+  __DATA_CONST.__objc_superrefs: 0x350
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x640
   __AUTH_CONST.__auth_ptr: 0x120
-  __AUTH_CONST.__const: 0xb50
-  __AUTH_CONST.__cfstring: 0x5900
-  __AUTH_CONST.__objc_const: 0x128c0
+  __AUTH_CONST.__const: 0xbd0
+  __AUTH_CONST.__cfstring: 0x5980
+  __AUTH_CONST.__objc_const: 0x13000
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0xd8c
-  __DATA.__data: 0x1530
+  __AUTH.__objc_data: 0x370
+  __DATA.__objc_ivar: 0xde8
+  __DATA.__data: 0x1650
   __DATA.__bss: 0x5f0
   __DATA_DIRTY.__objc_data: 0x2590
   __DATA_DIRTY.__data: 0x1b8
-  __DATA_DIRTY.__bss: 0x350
+  __DATA_DIRTY.__bss: 0x370
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4021
-  Symbols:   4566
-  CStrings:  5060
+  Functions: 4128
+  Symbols:   4677
+  CStrings:  5108
 
Symbols:
+ _OBJC_CLASS_$_SPCertificationAssistantBeacon
+ _OBJC_CLASS_$_SPMetadataFetchingSession
+ _OBJC_METACLASS_$_SPCertificationAssistantBeacon
+ _OBJC_METACLASS_$_SPMetadataFetchingSession
+ _SPCertificationAssistantErrorDomain
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_initStructMetadataWithLayoutString
CStrings:
+ "\x06#"
+ "\x15\x11\x11$\x16+"
+ "\x15!"
+ "-[SPCertificationAssistantSession startUpdatingBeaconsWithContext:collectionDifference:completion:]"
+ "-[SPCertificationAssistantSession stopUpdatingBeaconsWithCompletion:]"
+ "-[SPMetadataFetchingSession fetchHawkeyeAIS]"
+ "@\"<SPMetadataFetchingXPCProtocol>\""
+ "@\"SPRawAccessoryMetadata\""
+ "SPCertificationAssistantBeacon"
+ "SPCertificationAssistantProtocol"
+ "SPCertificationAssistantSession"
+ "SPMetadataFetchingSession"
+ "SPMetadataFetchingSession.fetchHawkeyeAIS"
+ "SPMetadataFetchingSession: Establishing XPC connection to %@"
+ "SPMetadataFetchingSession: interruptionHandler %@"
+ "SPMetadataFetchingSession: invalidationHandler %@"
+ "SPMetadataFetchingXPCClientProtocol"
+ "SPMetadataFetchingXPCProtocol"
+ "T@\"<SPMetadataFetchingXPCProtocol>\",&,N,V_proxy"
+ "T@\"NSData\",C,N,V_networkId"
+ "T@\"NSData\",C,N,V_protocolVersion"
+ "T@\"SPRawAccessoryMetadata\",C,N,V_rawMetadata"
+ "_networkId"
+ "_rawMetadata"
+ "certificationAssistantSession"
+ "com.apple.SPOwner.SPCertificationAssistant.ErrorDomain"
+ "com.apple.SPOwner.SPCertificationAssistantSession"
+ "com.apple.icloud.searchpartyd.SPMetadataFetchingSession"
+ "com.apple.icloud.searchpartyd.SPMetadataFetchingSession.callback"
+ "com.apple.searchparty.MetadataFetchingSession"
+ "fetchAccessoryCapabilitiesData:completion:"
+ "fetchAccessoryCategoryData:completion:"
+ "fetchBatteryStatusData:completion:"
+ "fetchBatteryTypeData:completion:"
+ "fetchFirmwareVersionData:completion:"
+ "fetchHawkeyeAIS:metadataType:completion:"
+ "fetchManufacturerNameData:completion:"
+ "fetchModelColorCodeData:completion:"
+ "fetchModelNameData:completion:"
+ "fetchProductData:completion:"
+ "fetchProtocolVersionData:completion:"
+ "fmcaContext"
+ "networkId"
+ "rawMetadata"
+ "setNetworkId:"
+ "setRawMetadata:"
+ "v40@0:8@\"NSUUID\"16Q24@?<v@?@\"NSData\"@\"NSError\">32"
- "\x15\x11\x11$\x16*"

```
