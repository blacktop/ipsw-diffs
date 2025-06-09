## IntelligentRouting

> `/System/Library/PrivateFrameworks/IntelligentRouting.framework/IntelligentRouting`

```diff

-96.0.6.0.1
-  __TEXT.__text: 0x90e4
-  __TEXT.__auth_stubs: 0x380
-  __TEXT.__objc_methlist: 0xfec
+96.0.18.0.0
+  __TEXT.__text: 0x9f84
+  __TEXT.__auth_stubs: 0x360
+  __TEXT.__objc_methlist: 0x1104
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0xdb7
+  __TEXT.__cstring: 0xffb
   __TEXT.__gcc_except_tab: 0x80
-  __TEXT.__oslogstring: 0x975
-  __TEXT.__unwind_info: 0x328
-  __TEXT.__objc_classname: 0x15d
-  __TEXT.__objc_methname: 0x183c
-  __TEXT.__objc_methtype: 0x44a
-  __TEXT.__objc_stubs: 0x1080
+  __TEXT.__oslogstring: 0x9a1
+  __TEXT.__unwind_info: 0x340
+  __TEXT.__objc_classname: 0x169
+  __TEXT.__objc_methname: 0x1962
+  __TEXT.__objc_methtype: 0x48c
+  __TEXT.__objc_stubs: 0x10c0
   __DATA_CONST.__got: 0xe0
-  __DATA_CONST.__const: 0x1f0
-  __DATA_CONST.__objc_classlist: 0x80
+  __DATA_CONST.__const: 0x240
+  __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x640
+  __DATA_CONST.__objc_selrefs: 0x658
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x80
-  __AUTH_CONST.__auth_got: 0x1d0
+  __DATA_CONST.__objc_superrefs: 0x88
+  __AUTH_CONST.__auth_got: 0x1c0
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x1080
-  __AUTH_CONST.__objc_const: 0x1838
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0xc4
+  __AUTH_CONST.__cfstring: 0x1240
+  __AUTH_CONST.__objc_const: 0x1a00
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0xdc
   __DATA.__data: 0x248
   __DATA_DIRTY.__objc_data: 0x4b0
   __DATA_DIRTY.__bss: 0x8

   - /System/Library/PrivateFrameworks/IntelligentRoutingServices.framework/IntelligentRoutingServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 640DCCB7-532F-35EC-B852-6AB70B7287DE
-  Functions: 299
-  Symbols:   1053
-  CStrings:  710
+  UUID: 7CC47C3E-A915-3189-9DB4-85F8BFAD25BC
+  Functions: 324
+  Symbols:   1120
+  CStrings:  756
 
Symbols:
+ +[IRHomeEvent new]
+ +[IRHomeEvent supportsSecureCoding]
+ -[IRContext initWithCandidateResults:isBannerClassificationUnavailable:bundleIdentifier:]
+ -[IRHomeEvent .cxx_destruct]
+ -[IRHomeEvent _isEventSubTypeValid:]
+ -[IRHomeEvent _isEventTypeValid:]
+ -[IRHomeEvent bundleID]
+ -[IRHomeEvent contextIdentifier]
+ -[IRHomeEvent copyWithZone:]
+ -[IRHomeEvent description]
+ -[IRHomeEvent encodeWithCoder:]
+ -[IRHomeEvent eventSubType]
+ -[IRHomeEvent eventType]
+ -[IRHomeEvent hash]
+ -[IRHomeEvent initWithCoder:]
+ -[IRHomeEvent initWithEventType:eventSubType:]
+ -[IRHomeEvent init]
+ -[IRHomeEvent isEqual:]
+ -[IRHomeEvent setBundleID:]
+ -[IRHomeEvent setContextIdentifier:]
+ -[IRNode HKAccessoryUniqueIdentifier]
+ -[IRNode HKRoomUniqueIdentifier]
+ -[IRNode setHKAccessoryUniqueIdentifier:]
+ -[IRNode setHKRoomUniqueIdentifier:]
+ -[IRSession requestCurrentContextWithReply:]
+ -[IRSession requestCurrentContextWithReply:].cold.1
+ GCC_except_table35
+ _IRContextHomeKey
+ _IRHomeEventSubTypeToString
+ _IRHomeEventTypeToString
+ _OBJC_CLASS_$_IRHomeEvent
+ _OBJC_IVAR_$_IRHomeEvent._bundleID
+ _OBJC_IVAR_$_IRHomeEvent._contextIdentifier
+ _OBJC_IVAR_$_IRHomeEvent._eventSubType
+ _OBJC_IVAR_$_IRHomeEvent._eventType
+ _OBJC_IVAR_$_IRNode._HKAccessoryUniqueIdentifier
+ _OBJC_IVAR_$_IRNode._HKRoomUniqueIdentifier
+ _OBJC_METACLASS_$_IRHomeEvent
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ __OBJC_$_CLASS_METHODS_IRHomeEvent
+ __OBJC_$_INSTANCE_METHODS_IRHomeEvent
+ __OBJC_$_INSTANCE_VARIABLES_IRHomeEvent
+ __OBJC_$_PROP_LIST_IRHomeEvent
+ __OBJC_CLASS_RO_$_IRHomeEvent
+ __OBJC_METACLASS_RO_$_IRHomeEvent
+ ___44-[IRSession requestCurrentContextWithReply:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e31_v24?0"IRContext"8"NSError"16ls32l8
+ _kIREventNameHome
+ _objc_msgSend$HKAccessoryUniqueIdentifier
+ _objc_msgSend$HKRoomUniqueIdentifier
+ _objc_msgSend$_requestCurrentContextWithReply:
- +[IRContext new]
- -[IRContext addCandidateResult:]
- -[IRContext init]
- -[IRContext updateBundleIdentifier:]
- -[IRContext updateIsBannerClassificationUnavailable:]
- GCC_except_table33
- _objc_msgSend$addObject:
- _objc_release_x27
- _objc_release_x28
CStrings:
+ "+[IRHomeEvent new]"
+ ", HKAccessoryUniqueIdentifier: %@"
+ ", HKRoomUniqueIdentifier: %@"
+ "-[IRHomeEvent init]"
+ "@\"NSUUID\""
+ "@36@0:8@16B24@28"
+ "HKAccessoryUniqueIdentifier"
+ "HKRoomUniqueIdentifier"
+ "IRAppleTVControlEvent.m"
+ "IRContextHomeKey"
+ "IRHomeEvent"
+ "IRHomeEvent.m"
+ "IRMediaEvent.m"
+ "Requesting current context with reply has failed"
+ "ServicePackageHome"
+ "T@\"NSUUID\",&,N,V_HKAccessoryUniqueIdentifier"
+ "T@\"NSUUID\",&,N,V_HKRoomUniqueIdentifier"
+ "UserInteraction"
+ "[IRSession]: requestCurrentContextWithReply"
+ "_HKAccessoryUniqueIdentifier"
+ "_HKRoomUniqueIdentifier"
+ "_requestCurrentContextWithReply:"
+ "com.apple.IntelligentRoutingHostTests.xctrunner.AppleTVControl"
+ "com.apple.IntelligentRoutingHostTests.xctrunner.Home"
+ "com.apple.IntelligentRoutingHostTests.xctrunner.Media"
+ "com.apple.intelligentroutingclient.Home"
+ "com.vpg.Rover"
+ "initWithCandidateResults:isBannerClassificationUnavailable:bundleIdentifier:"
+ "kIREventNameHome"
+ "requestCurrentContextWithReply:"
+ "setHKAccessoryUniqueIdentifier:"
+ "setHKRoomUniqueIdentifier:"
+ "v24@0:8@?<v@?@\"IRContext\"@\"NSError\">16"
+ "v24@?0@\"IRContext\"8@\"NSError\"16"
- "addCandidateResult:"
- "addObject:"
- "updateBundleIdentifier:"
- "updateIsBannerClassificationUnavailable:"

```
