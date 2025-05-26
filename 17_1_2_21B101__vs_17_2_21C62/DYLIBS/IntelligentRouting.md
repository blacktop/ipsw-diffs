## IntelligentRouting

> `/System/Library/PrivateFrameworks/IntelligentRouting.framework/IntelligentRouting`

```diff

-55.0.0.0.0
-  __TEXT.__text: 0x727c
+64.0.0.0.0
+  __TEXT.__text: 0x79a8
   __TEXT.__auth_stubs: 0x380
-  __TEXT.__objc_methlist: 0xb28
+  __TEXT.__objc_methlist: 0xbd8
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x995
+  __TEXT.__cstring: 0xa7b
   __TEXT.__gcc_except_tab: 0x4c
-  __TEXT.__oslogstring: 0x722
-  __TEXT.__unwind_info: 0x298
-  __TEXT.__objc_classname: 0x133
-  __TEXT.__objc_methname: 0x12cb
-  __TEXT.__objc_methtype: 0x3f9
-  __TEXT.__objc_stubs: 0xdc0
+  __TEXT.__oslogstring: 0x8d1
+  __TEXT.__unwind_info: 0x2a8
+  __TEXT.__objc_classname: 0x155
+  __TEXT.__objc_methname: 0x1435
+  __TEXT.__objc_methtype: 0x427
+  __TEXT.__objc_stubs: 0xe60
   __DATA_CONST.__got: 0x18
-  __DATA_CONST.__const: 0x200
-  __DATA_CONST.__objc_classlist: 0x68
+  __DATA_CONST.__const: 0x218
+  __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1118
-  __DATA_CONST.__objc_selrefs: 0x4b8
-  __AUTH_CONST.__cfstring: 0xa60
-  __AUTH_CONST.__objc_const: 0x700
+  __DATA_CONST.__objc_const: 0x1200
+  __DATA_CONST.__objc_selrefs: 0x500
+  __AUTH_CONST.__cfstring: 0xb60
+  __AUTH_CONST.__objc_const: 0x790
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__auth_got: 0x1d0
-  __AUTH.__objc_data: 0x50
+  __AUTH.__objc_data: 0xa0
   __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0xc0
-  __DATA.__objc_superrefs: 0x68
-  __DATA.__objc_ivar: 0xa8
+  __DATA.__objc_classrefs: 0xc8
+  __DATA.__objc_superrefs: 0x70
+  __DATA.__objc_ivar: 0xb0
   __DATA.__data: 0x248
   __DATA_DIRTY.__objc_data: 0x3c0
   __DATA_DIRTY.__bss: 0x8

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 249
-  Symbols:   897
-  CStrings:  468
+  Functions: 266
+  Symbols:   948
+  CStrings:  497
 
Symbols:
+ +[IRSessionSpotOnLocationParameters supportsSecureCoding]
+ -[IRCandidateResult isCallToAction]
+ -[IRCandidateResult setIsCallToAction:]
+ -[IRSession _didSpotOnLocationComplete:]
+ -[IRSession setSpotOnLocationWithParameters:]
+ -[IRSession setSpotOnLocationWithParameters:].cold.1
+ -[IRSession setSpotOnLocationWithParameters:].cold.2
+ -[IRSessionSpotOnLocationParameters copyWithZone:]
+ -[IRSessionSpotOnLocationParameters description]
+ -[IRSessionSpotOnLocationParameters encodeWithCoder:]
+ -[IRSessionSpotOnLocationParameters hash]
+ -[IRSessionSpotOnLocationParameters initWithCoder:]
+ -[IRSessionSpotOnLocationParameters isEqual:]
+ -[IRSessionSpotOnLocationParameters resetAllBrokerDiscoveredCandidates]
+ -[IRSessionSpotOnLocationParameters setResetAllBrokerDiscoveredCandidates:]
+ GCC_except_table9
+ _OBJC_CLASS_$_IRSessionSpotOnLocationParameters
+ _OBJC_IVAR_$_IRCandidateResult._isCallToAction
+ _OBJC_IVAR_$_IRSessionSpotOnLocationParameters._resetAllBrokerDiscoveredCandidates
+ _OBJC_METACLASS_$_IRSessionSpotOnLocationParameters
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ __OBJC_$_CLASS_METHODS_IRSessionSpotOnLocationParameters
+ __OBJC_$_CLASS_PROP_LIST_IRSessionSpotOnLocationParameters
+ __OBJC_$_INSTANCE_METHODS_IRSessionSpotOnLocationParameters
+ __OBJC_$_INSTANCE_VARIABLES_IRSessionSpotOnLocationParameters
+ __OBJC_$_PROP_LIST_IRSessionSpotOnLocationParameters
+ __OBJC_CLASS_PROTOCOLS_$_IRSessionSpotOnLocationParameters
+ __OBJC_CLASS_RO_$_IRSessionSpotOnLocationParameters
+ __OBJC_METACLASS_RO_$_IRSessionSpotOnLocationParameters
+ _objc_msgSend$_setSpotOnLocationWithParameters:
+ _objc_msgSend$boolValue
+ _objc_msgSend$isCallToAction
+ _objc_msgSend$resetAllBrokerDiscoveredCandidates
+ _objc_msgSend$session:didSpotOnLocationComplete:
- GCC_except_table0
CStrings:
+ "\x11\x12"
+ ", is Call To Action: %@"
+ ", resetAllBrokerDiscoveredCandidates: %@"
+ "BrokeredDeviceScanMainDevice"
+ "BrokeredDeviceScanSecondaryDevice"
+ "CallToActionPresented"
+ "IRSessionSpotOnLocationParameters"
+ "TB,N,V_isCallToAction"
+ "TB,N,V_resetAllBrokerDiscoveredCandidates"
+ "[ErrorId - IRSession setSpotOnLocationWithParameters error] [IRSession]: parameters must not be nil"
+ "[ErrorId - IRSession setSpotOnLocationWithParameters error] [IRSession]: session was never run: isSessionInvalidated: %@"
+ "[IRSession]: didSpotOnLocationComplete"
+ "[IRSession]: setting current location spotOnLocation"
+ "[IRSession]: spotOnDelegate does not respond to session:didSpotOnLocationComplete:"
+ "[IRSession]: spotOnDelegate is nil"
+ "_didSpotOnLocationComplete:"
+ "_isCallToAction"
+ "_resetAllBrokerDiscoveredCandidates"
+ "_setSpotOnLocationWithParameters:"
+ "boolValue"
+ "isCallToAction"
+ "resetAllBrokerDiscoveredCandidates"
+ "session:didSpotOnLocationComplete:"
+ "set spotOnLocation has failed"
+ "setIsCallToAction:"
+ "setResetAllBrokerDiscoveredCandidates:"
+ "setSpotOnLocationWithParameters:"
+ "v24@0:8@\"IRSessionSpotOnLocationParameters\"16"
- "\x01\x12"

```
