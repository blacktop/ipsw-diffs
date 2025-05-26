## AdCore

> `/System/Library/PrivateFrameworks/AdCore.framework/AdCore`

```diff

-602.0.0.0.0
-  __TEXT.__text: 0x29090
+608.0.0.0.0
+  __TEXT.__text: 0x28da4
   __TEXT.__auth_stubs: 0x900
-  __TEXT.__objc_methlist: 0x3918
+  __TEXT.__objc_methlist: 0x38c4
   __TEXT.__const: 0x178
-  __TEXT.__cstring: 0x3b31
+  __TEXT.__cstring: 0x3b18
   __TEXT.__gcc_except_tab: 0x430
   __TEXT.__ustring: 0x8
   __TEXT.__oslogstring: 0xb
-  __TEXT.__unwind_info: 0xb0c
-  __TEXT.__objc_classname: 0x355
-  __TEXT.__objc_methname: 0x6b98
-  __TEXT.__objc_methtype: 0x934
+  __TEXT.__unwind_info: 0xaf8
+  __TEXT.__objc_classname: 0x370
+  __TEXT.__objc_methname: 0x6b6a
+  __TEXT.__objc_methtype: 0xa67
   __TEXT.__objc_stubs: 0x3ba0
   __DATA_CONST.__got: 0x140
-  __DATA_CONST.__const: 0x668
+  __DATA_CONST.__const: 0x690
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x20
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x41c0
+  __DATA_CONST.__objc_const: 0x42f0
   __DATA_CONST.__objc_selrefs: 0x1cd0
   __DATA_CONST.__objc_arraydata: 0x188
   __AUTH_CONST.__const: 0x360

   __DATA.__objc_protorefs: 0x8
   __DATA.__objc_classrefs: 0x200
   __DATA.__objc_superrefs: 0x130
-  __DATA.__objc_ivar: 0x394
-  __DATA.__data: 0x180
+  __DATA.__objc_ivar: 0x390
+  __DATA.__data: 0x1e0
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x960
   __DATA_DIRTY.__bss: 0x220

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1284
-  Symbols:   4055
-  CStrings:  2095
+  Functions: 1275
+  Symbols:   4041
+  CStrings:  2103
 
Symbols:
+ -[ADCoreDefaults _defaultValueForKey:valueClass:]
+ -[ADCoreDefaults _setDefaultValue:forKey:]
+ -[ADCoreDefaults arrayForKey:]
+ -[ADCoreDefaults boolForKey:]
+ -[ADCoreDefaults defaultIsSetForKey:]
+ -[ADCoreDefaults doubleForKey:]
+ -[ADCoreDefaults integerForKey:]
+ -[ADCoreDefaults setArray:forKey:]
+ -[ADCoreDefaults setBool:forKey:]
+ -[ADCoreDefaults setDouble:forKey:]
+ -[ADCoreDefaults setInteger:forKey:]
+ -[ADCoreDefaults setString:forKey:]
+ -[ADCoreDefaults stringForKey:]
+ -[ADRoutingInfoMessage initWithRoutingType:preferencesStore:]
+ -[ADRoutingInfoMessage payload]
+ -[ADRoutingInfoMessage routingInfoType]
+ -[ADRoutingInfoMessage setRoutingInfoType:]
+ -[ADRoutingInfoMessage setStorage:]
+ -[ADRoutingInfoMessage storage]
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_IVAR_$_ADRoutingInfoMessage._routingInfoType
+ _OBJC_IVAR_$_ADRoutingInfoMessage._storage
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ADCorePreferencesStoring
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ADCorePreferencesStoring
+ __OBJC_CLASS_PROTOCOLS_$_ADCoreDefaults
+ __OBJC_LABEL_PROTOCOL_$_ADCorePreferencesStoring
+ __OBJC_PROTOCOL_$_ADCorePreferencesStoring
+ ___22-[ADCoreSettings init]_block_invoke
+ ___46-[ADCoreSettings reloadNoServicesRestrictions]_block_invoke
+ ___block_descriptor_40_e8_32s_e30_v24?0"NSNumber"8"NSError"16ls32l8
+ ___block_literal_global.212
+ ___block_literal_global.215
+ _objc_msgSend$environmentURL
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$routingInfoType
+ _objc_msgSend$storage
- +[ADCoreDefaults _defaultValueForKey:valueClass:]
- +[ADCoreDefaults _setDefaultValue:forKey:]
- +[ADCoreDefaults arrayForKey:]
- +[ADCoreDefaults boolForKey:]
- +[ADCoreDefaults defaultIsSetForKey:]
- +[ADCoreDefaults doubleForKey:]
- +[ADCoreDefaults integerForKey:]
- +[ADCoreDefaults setArray:forKey:]
- +[ADCoreDefaults setBool:forKey:]
- +[ADCoreDefaults setDouble:forKey:]
- +[ADCoreDefaults setInteger:forKey:]
- +[ADCoreDefaults setString:forKey:]
- +[ADCoreDefaults stringForKey:]
- -[ADRoutingInfoMessage copyTo:]
- -[ADRoutingInfoMessage copyWithZone:]
- -[ADRoutingInfoMessage hash]
- -[ADRoutingInfoMessage isEqual:]
- -[ADRoutingInfoMessage mergeFrom:]
- -[ADRoutingInfoMessage protoVersion]
- -[ADRoutingInfoMessage readFrom:]
- -[ADRoutingInfoMessage searchType]
- -[ADRoutingInfoMessage setEnvironmentURL:]
- -[ADRoutingInfoMessage setProtoVersion:]
- -[ADRoutingInfoMessage setSearchType:]
- -[ADRoutingInfoMessage writeTo:]
- -[ADRoutingInfoMessage writeTo:].cold.1
- -[ADRoutingInfoMessage writeTo:].cold.2
- -[ADRoutingInfoMessage writeTo:].cold.3
- -[ADServer routingHeaderForClass:serverURL:]
- OBJC_IVAR_$_ADRoutingInfoMessage._environmentURL
- OBJC_IVAR_$_ADRoutingInfoMessage._protoVersion
- OBJC_IVAR_$_ADRoutingInfoMessage._searchType
- _ADRoutingInfoMessageReadFrom
- __OBJC_CLASS_PROTOCOLS_$_ADRoutingInfoMessage
- ___block_literal_global.207
- ___block_literal_global.210
- _objc_msgSend$resultWithError:
- _objc_msgSend$setEnvironmentURL:
- _objc_msgSend$setProtoVersion:
- _objc_msgSend$setSearchType:
CStrings:
+ "\x11"
+ "@\"<ADCorePreferencesStoring>\""
+ "@\"NSArray\"24@0:8@\"NSString\"16"
+ "@\"NSString\"24@0:8@\"NSString\"16"
+ "@32@0:8Q16@24"
+ "ADCorePreferencesStoring"
+ "AutomationLoggingEnabled"
+ "B24@0:8@\"NSString\"16"
+ "Device IDs:%@\n"
+ "GibraltarAdServerURL"
+ "T@\"<ADCorePreferencesStoring>\",&,N,V_storage"
+ "TQ,N,V_routingInfoType"
+ "[%@] RoutingInfo dictionary failed to serialize"
+ "[%@] RoutingInfo dictionary isn't a valid dictionary"
+ "_routingInfoType"
+ "_storage"
+ "d24@0:8@\"NSString\"16"
+ "environmentUrl"
+ "initWithRoutingType:preferencesStore:"
+ "initWithSuiteName:"
+ "payload"
+ "q24@0:8@\"NSString\"16"
+ "routingInfoType"
+ "setRoutingInfoType:"
+ "setStorage:"
+ "storage"
+ "v24@?0@\"NSNumber\"8@\"NSError\"16"
+ "v28@0:8B16@\"NSString\"20"
+ "v32@0:8@\"NSArray\"16@\"NSString\"24"
+ "v32@0:8@\"NSString\"16@\"NSString\"24"
+ "v32@0:8d16@\"NSString\"24"
+ "v32@0:8q16@\"NSString\"24"
- "-[ADRoutingInfoMessage writeTo:]"
- "ADRoutingInfoMessage.m"
- "Routing Info: %@"
- "SS"
- "T@\"NSString\",&,N,V_environmentURL"
- "T@\"NSString\",&,N,V_protoVersion"
- "T@\"NSString\",&,N,V_searchType"
- "_environmentURL"
- "_protoVersion"
- "_searchType"
- "https://tr.iadsdk.apple.com/adserver"
- "nil != self->_environmentURL"
- "nil != self->_protoVersion"
- "nil != self->_searchType"
- "protoVersion"
- "resultWithError:"
- "routingHeaderForClass:serverURL:"
- "searchType"
- "setEnvironmentURL:"
- "setProtoVersion:"
- "setSearchType:"

```
