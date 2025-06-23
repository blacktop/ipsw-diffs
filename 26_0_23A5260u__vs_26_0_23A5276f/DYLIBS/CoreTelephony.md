## CoreTelephony

> `/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`

```diff

-13071.5.0.0.0
-  __TEXT.__text: 0x18d528
+13077.0.0.0.0
+  __TEXT.__text: 0x18d588
   __TEXT.__auth_stubs: 0x1980
-  __TEXT.__objc_methlist: 0x1b2e4
+  __TEXT.__objc_methlist: 0x1b29c
   __TEXT.__const: 0x100a
-  __TEXT.__gcc_except_tab: 0x1dd58
-  __TEXT.__cstring: 0x1f780
+  __TEXT.__gcc_except_tab: 0x1dc8c
+  __TEXT.__cstring: 0x1f745
   __TEXT.__oslogstring: 0x4368
   __TEXT.__swift5_typeref: 0x17
-  __TEXT.__unwind_info: 0xd150
-  __TEXT.__objc_classname: 0x5915
-  __TEXT.__objc_methname: 0x22a5d
-  __TEXT.__objc_methtype: 0x724e
-  __TEXT.__objc_stubs: 0x16b40
-  __DATA_CONST.__got: 0xb00
-  __DATA_CONST.__const: 0x74c8
-  __DATA_CONST.__objc_classlist: 0x1528
+  __TEXT.__unwind_info: 0xd0f8
+  __TEXT.__objc_classname: 0x58f3
+  __TEXT.__objc_methname: 0x22aeb
+  __TEXT.__objc_methtype: 0x7286
+  __TEXT.__objc_stubs: 0x16ba0
+  __DATA_CONST.__got: 0xaf0
+  __DATA_CONST.__const: 0x74b0
+  __DATA_CONST.__objc_classlist: 0x1520
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7780
+  __DATA_CONST.__objc_selrefs: 0x7798
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0x1798
+  __DATA_CONST.__objc_superrefs: 0x1790
   __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__auth_got: 0xcd8
   __AUTH_CONST.__const: 0x1ec0
-  __AUTH_CONST.__cfstring: 0x1d900
-  __AUTH_CONST.__objc_const: 0x2f730
+  __AUTH_CONST.__cfstring: 0x1d980
+  __AUTH_CONST.__objc_const: 0x2f658
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0xa910
-  __DATA.__objc_ivar: 0x1418
+  __AUTH.__objc_data: 0xa8c0
+  __DATA.__objc_ivar: 0x1420
   __DATA.__data: 0x1f88
   __DATA.__bss: 0x198
   __DATA.__common: 0x10

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
-  UUID: 65C6F541-4BCA-3260-A246-45EC07947B10
-  Functions: 11242
-  Symbols:   38157
-  CStrings:  17051
+  UUID: E3301E91-CFE9-3F2C-B5D6-DF45CA005A9D
+  Functions: 11239
+  Symbols:   38133
+  CStrings:  17063
 
Symbols:
+ +[CTCellularConfigUpdateInfo supportsSecureCoding]
+ -[CTCellularConfigUpdateInfo .cxx_destruct]
+ -[CTCellularConfigUpdateInfo configType]
+ -[CTCellularConfigUpdateInfo copyWithZone:]
+ -[CTCellularConfigUpdateInfo description]
+ -[CTCellularConfigUpdateInfo encodeWithCoder:]
+ -[CTCellularConfigUpdateInfo initWithCoder:]
+ -[CTCellularConfigUpdateInfo init]
+ -[CTCellularConfigUpdateInfo setConfigType:]
+ -[CTCellularConfigUpdateInfo setUpdatedDetails:]
+ -[CTCellularConfigUpdateInfo setUpdatedTime:]
+ -[CTCellularConfigUpdateInfo updatedDetails]
+ -[CTCellularConfigUpdateInfo updatedTime]
+ -[CoreTelephonyClient(Radio) checkBasebandConfigUpdateInfo:]
+ _OBJC_CLASS_$_CTCellularConfigUpdateInfo
+ _OBJC_IVAR_$_CTCellularConfigUpdateInfo._configType
+ _OBJC_IVAR_$_CTCellularConfigUpdateInfo._updatedDetails
+ _OBJC_IVAR_$_CTCellularConfigUpdateInfo._updatedTime
+ _OBJC_METACLASS_$_CTCellularConfigUpdateInfo
+ __OBJC_$_CLASS_METHODS_CTCellularConfigUpdateInfo
+ __OBJC_$_CLASS_PROP_LIST_CTCellularConfigUpdateInfo
+ __OBJC_$_INSTANCE_METHODS_CTCellularConfigUpdateInfo
+ __OBJC_$_INSTANCE_VARIABLES_CTCellularConfigUpdateInfo
+ __OBJC_$_PROP_LIST_CTCellularConfigUpdateInfo
+ __OBJC_CLASS_PROTOCOLS_$_CTCellularConfigUpdateInfo
+ __OBJC_CLASS_RO_$_CTCellularConfigUpdateInfo
+ __OBJC_METACLASS_RO_$_CTCellularConfigUpdateInfo
+ ___60-[CoreTelephonyClient(Radio) checkBasebandConfigUpdateInfo:]_block_invoke
+ ___60-[CoreTelephonyClient(Radio) checkBasebandConfigUpdateInfo:]_block_invoke_2
+ ___block_descriptor_48_ea8_32r40r_e48_v24?0"CTCellularConfigUpdateInfo"8"NSError"16lr32l8r40l8
+ ___block_literal_global.1016
+ ___block_literal_global.1021
+ ___block_literal_global.1025
+ _objc_msgSend$checkBasebandConfigUpdateInfo:
+ _objc_msgSend$configType
+ _objc_msgSend$setConfigType:
+ _objc_msgSend$setUpdatedDetails:
+ _objc_msgSend$setUpdatedTime:
+ _objc_msgSend$updatedDetails
+ _objc_msgSend$updatedTime
- +[CTStewieWeatherRequestMessage supportsSecureCoding]
- +[CTStewieWeatherResponseMessage supportsSecureCoding]
- -[CTStewieWeatherRequestMessage copyWithZone:]
- -[CTStewieWeatherRequestMessage description]
- -[CTStewieWeatherRequestMessage encodeWithCoder:]
- -[CTStewieWeatherRequestMessage initWithCoder:]
- -[CTStewieWeatherRequestMessage init]
- -[CTStewieWeatherRequestMessage isEqual:]
- -[CTStewieWeatherRequestMessage isEqualToWeatherRequestMessage:]
- -[CTStewieWeatherResponseMessage .cxx_destruct]
- -[CTStewieWeatherResponseMessage copyWithZone:]
- -[CTStewieWeatherResponseMessage description]
- -[CTStewieWeatherResponseMessage encodeWithCoder:]
- -[CTStewieWeatherResponseMessage fPayload]
- -[CTStewieWeatherResponseMessage initWithCoder:]
- -[CTStewieWeatherResponseMessage initWithPayload:error:]
- -[CTStewieWeatherResponseMessage isEqual:]
- -[CTStewieWeatherResponseMessage isEqualToOther:]
- -[CTStewieWeatherResponseMessage setFPayload:]
- _OBJC_CLASS_$_CTStewieWeatherRequestMessage
- _OBJC_CLASS_$_CTStewieWeatherResponseMessage
- _OBJC_IVAR_$_CTStewieWeatherResponseMessage._fPayload
- _OBJC_METACLASS_$_CTStewieWeatherRequestMessage
- _OBJC_METACLASS_$_CTStewieWeatherResponseMessage
- __OBJC_$_CLASS_METHODS_CTStewieWeatherRequestMessage
- __OBJC_$_CLASS_METHODS_CTStewieWeatherResponseMessage
- __OBJC_$_CLASS_PROP_LIST_CTStewieWeatherRequestMessage
- __OBJC_$_CLASS_PROP_LIST_CTStewieWeatherResponseMessage
- __OBJC_$_INSTANCE_METHODS_CTStewieWeatherRequestMessage
- __OBJC_$_INSTANCE_METHODS_CTStewieWeatherResponseMessage
- __OBJC_$_INSTANCE_VARIABLES_CTStewieWeatherResponseMessage
- __OBJC_$_PROP_LIST_CTStewieWeatherRequestMessage
- __OBJC_$_PROP_LIST_CTStewieWeatherResponseMessage
- __OBJC_CLASS_PROTOCOLS_$_CTStewieWeatherRequestMessage
- __OBJC_CLASS_PROTOCOLS_$_CTStewieWeatherResponseMessage
- __OBJC_CLASS_RO_$_CTStewieWeatherRequestMessage
- __OBJC_CLASS_RO_$_CTStewieWeatherResponseMessage
- __OBJC_METACLASS_RO_$_CTStewieWeatherRequestMessage
- __OBJC_METACLASS_RO_$_CTStewieWeatherResponseMessage
- ___block_literal_global.1014
- ___block_literal_global.1019
- ___block_literal_global.1023
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_CoreTelephony
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_CoreTelephony
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_CoreTelephony
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_CoreTelephony
- _objc_msgSend$fPayload
- _objc_msgSend$initWithPayload:error:
- _objc_msgSend$isEqualToWeatherRequestMessage:
- _objc_msgSend$setFPayload:
CStrings:
+ ", config type=%@"
+ ", updated details=%@"
+ ", updated time=%@"
+ "13077"
+ "13077~26"
+ "CTCellularConfigUpdateInfo"
+ "T@\"NSString\",&,N,V_configType"
+ "T@\"NSString\",&,N,V_updatedDetails"
+ "T@\"NSString\",&,N,V_updatedTime"
+ "_configType"
+ "_updatedDetails"
+ "_updatedTime"
+ "checkBasebandConfigUpdateInfo:"
+ "configType"
+ "configTypeKey"
+ "setConfigType:"
+ "setUpdatedDetails:"
+ "setUpdatedTime:"
+ "updatedDetails"
+ "updatedDetailsKey"
+ "updatedTime"
+ "updatedTimeKey"
+ "v24@0:8@?<v@?@\"CTCellularConfigUpdateInfo\"@\"NSError\">16"
+ "v24@?0@\"CTCellularConfigUpdateInfo\"8@\"NSError\"16"
- "13071.5"
- "13071.5~293"
- "CTCAStewieExitReasonWeather"
- "CTCATransmissionPayloadTypeWeatherRequestMessage"
- "CTStewieExitReasonWeather"
- "CTStewieRequestReasonWeather"
- "CTStewieWeatherRequestMessage"
- "CTStewieWeatherResponseMessage"
- "One or more required parameters are missing"
- "T@\"NSData\",&,N,V_fPayload"
- "_fPayload"
- "fPayload"
- "initWithPayload:error:"
- "isEqualToWeatherRequestMessage:"
- "setFPayload:"

```
