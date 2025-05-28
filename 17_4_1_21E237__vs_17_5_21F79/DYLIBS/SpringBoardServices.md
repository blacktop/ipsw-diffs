## SpringBoardServices

> `/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices`

```diff

-4416.132.102.1.0
-  __TEXT.__text: 0x5f144
+4416.306.103.0.0
+  __TEXT.__text: 0x6193c
   __TEXT.__auth_stubs: 0xf50
-  __TEXT.__objc_methlist: 0x5548
-  __TEXT.__cstring: 0xb509
-  __TEXT.__oslogstring: 0x3272
-  __TEXT.__const: 0x4b8
-  __TEXT.__gcc_except_tab: 0x774
+  __TEXT.__objc_methlist: 0x5910
+  __TEXT.__cstring: 0xb72a
+  __TEXT.__oslogstring: 0x32c7
+  __TEXT.__const: 0x508
+  __TEXT.__gcc_except_tab: 0x7c4
   __TEXT.__dlopen_cstrs: 0x17a
   __TEXT.__ustring: 0x58
-  __TEXT.__unwind_info: 0x1d1c
-  __TEXT.__objc_classname: 0x1dc4
-  __TEXT.__objc_methname: 0xca59
-  __TEXT.__objc_methtype: 0x2316
-  __TEXT.__objc_stubs: 0x7320
+  __TEXT.__unwind_info: 0x1ed0
+  __TEXT.__objc_classname: 0x2015
+  __TEXT.__objc_methname: 0xcdf9
+  __TEXT.__objc_methtype: 0x23c8
+  __TEXT.__objc_stubs: 0x7440
   __DATA_CONST.__got: 0x190
-  __DATA_CONST.__const: 0x2e20
-  __DATA_CONST.__objc_classlist: 0x4e0
+  __DATA_CONST.__const: 0x2e88
+  __DATA_CONST.__objc_classlist: 0x538
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x1e0
+  __DATA_CONST.__objc_protolist: 0x200
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x17680
-  __DATA_CONST.__objc_selrefs: 0x27e8
-  __DATA_CONST.__objc_protorefs: 0x138
-  __DATA_CONST.__objc_classrefs: 0x560
-  __DATA_CONST.__objc_superrefs: 0x308
-  __AUTH_CONST.__cfstring: 0x89e0
-  __AUTH_CONST.__objc_const: 0x3cb8
-  __AUTH_CONST.__const: 0x23f0
+  __DATA_CONST.__objc_const: 0x19628
+  __DATA_CONST.__objc_selrefs: 0x2890
+  __DATA_CONST.__objc_protorefs: 0x150
+  __DATA_CONST.__objc_classrefs: 0x5a0
+  __DATA_CONST.__objc_superrefs: 0x340
+  __AUTH_CONST.__cfstring: 0x8b80
+  __AUTH_CONST.__objc_const: 0x4138
+  __AUTH_CONST.__const: 0x2470
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__auth_ptr: 0x20
   __AUTH_CONST.__auth_got: 0x7b8
   __AUTH.__objc_data: 0x1fe0
-  __DATA.__objc_ivar: 0x5c4
-  __DATA.__data: 0x1ce0
-  __DATA.__bss: 0x1d8
-  __DATA_DIRTY.__objc_data: 0x10e0
-  __DATA_DIRTY.__data: 0x48
-  __DATA_DIRTY.__bss: 0x1f0
+  __DATA.__objc_ivar: 0x5f8
+  __DATA.__data: 0x1e98
+  __DATA.__bss: 0x200
+  __DATA_DIRTY.__objc_data: 0x1450
+  __DATA_DIRTY.__data: 0x40
+  __DATA_DIRTY.__bss: 0x1e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3070
-  Symbols:   10433
-  CStrings:  4117
+  Functions: 3174
+  Symbols:   10845
+  CStrings:  4191
 
Symbols:
+ +[SBSApplicationRestrictionMonitoringService registerMonitor:]
+ +[SBSApplicationRestrictionMonitoringServiceInterfaceSpecification domain]
+ +[SBSApplicationRestrictionMonitoringServiceInterfaceSpecification identifier]
+ +[SBSApplicationRestrictionMonitoringServiceInterfaceSpecification interface]
+ +[SBSApplicationRestrictionMonitoringServiceInterfaceSpecification serviceQuality]
+ +[SBSApplicationRestrictionState supportsSecureCoding]
+ +[SBSHomeScreenConfiguration supportsBSXPCSecureCoding]
+ +[SBSHomeScreenConfigurationLayout supportsBSXPCSecureCoding]
+ +[SBSHomeScreenConfigurationService beginConfigurationSessionWithInvalidationHandler:completion:]
+ +[SBSHomeScreenConfigurationServiceInterfaceSpecification domain]
+ +[SBSHomeScreenConfigurationServiceInterfaceSpecification identifier]
+ +[SBSHomeScreenConfigurationServiceInterfaceSpecification interface]
+ +[SBSHomeScreenConfigurationServiceInterfaceSpecification serviceQuality]
+ +[SBSHomeScreenItem supportsBSXPCSecureCoding]
+ +[SBSHomeScreenItemApplication supportsBSXPCSecureCoding]
+ -[SBSApplicationRestrictionMonitorProxy .cxx_destruct]
+ -[SBSApplicationRestrictionMonitorProxy connection]
+ -[SBSApplicationRestrictionMonitorProxy dealloc]
+ -[SBSApplicationRestrictionMonitorProxy didInvalidate]
+ -[SBSApplicationRestrictionMonitorProxy initWithMonitor:]
+ -[SBSApplicationRestrictionMonitorProxy invalidate]
+ -[SBSApplicationRestrictionMonitorProxy makeConnection]
+ -[SBSApplicationRestrictionMonitorProxy monitor]
+ -[SBSApplicationRestrictionMonitorProxy observeUpdateWithApplicationRestrictState:]
+ -[SBSApplicationRestrictionMonitorProxy queue]
+ -[SBSApplicationRestrictionState .cxx_destruct]
+ -[SBSApplicationRestrictionState allowedBundleIdentifiers]
+ -[SBSApplicationRestrictionState encodeWithCoder:]
+ -[SBSApplicationRestrictionState initWithAllowedIdentifiers:restrictedIdentifiers:]
+ -[SBSApplicationRestrictionState initWithCoder:]
+ -[SBSApplicationRestrictionState restrictedBundleIdentifiers]
+ -[SBSHomeScreenConfiguration .cxx_destruct]
+ -[SBSHomeScreenConfiguration copyWithZone:]
+ -[SBSHomeScreenConfiguration description]
+ -[SBSHomeScreenConfiguration encodeWithBSXPCCoder:]
+ -[SBSHomeScreenConfiguration hash]
+ -[SBSHomeScreenConfiguration initWithBSXPCCoder:]
+ -[SBSHomeScreenConfiguration isEqual:]
+ -[SBSHomeScreenConfiguration layout]
+ -[SBSHomeScreenConfiguration name]
+ -[SBSHomeScreenConfiguration setLayout:]
+ -[SBSHomeScreenConfiguration setName:]
+ -[SBSHomeScreenConfigurationLayout .cxx_destruct]
+ -[SBSHomeScreenConfigurationLayout copyWithZone:]
+ -[SBSHomeScreenConfigurationLayout description]
+ -[SBSHomeScreenConfigurationLayout dockItems]
+ -[SBSHomeScreenConfigurationLayout encodeWithBSXPCCoder:]
+ -[SBSHomeScreenConfigurationLayout hash]
+ -[SBSHomeScreenConfigurationLayout initWithBSXPCCoder:]
+ -[SBSHomeScreenConfigurationLayout initWithItems:dockItems:]
+ -[SBSHomeScreenConfigurationLayout isEqual:]
+ -[SBSHomeScreenConfigurationLayout items]
+ -[SBSHomeScreenConfigurationServiceProxy .cxx_destruct]
+ -[SBSHomeScreenConfigurationServiceProxy applyConfiguration:completion:]
+ -[SBSHomeScreenConfigurationServiceProxy beginConfigurationSessionWithCompletion:]
+ -[SBSHomeScreenConfigurationServiceProxy connectionDidInvalidate]
+ -[SBSHomeScreenConfigurationServiceProxy connection]
+ -[SBSHomeScreenConfigurationServiceProxy endConfigurationSessionWithCompletion:]
+ -[SBSHomeScreenConfigurationServiceProxy initWithInvalidationHandler:]
+ -[SBSHomeScreenConfigurationServiceProxy invalidationHandler]
+ -[SBSHomeScreenConfigurationServiceProxy makeConnection]
+ -[SBSHomeScreenConfigurationServiceProxy queue]
+ -[SBSHomeScreenConfigurationServiceProxy setInvalidationHandler:]
+ -[SBSHomeScreenItem copyWithZone:]
+ -[SBSHomeScreenItem description]
+ -[SBSHomeScreenItem encodeWithBSXPCCoder:]
+ -[SBSHomeScreenItem hash]
+ -[SBSHomeScreenItem initWithBSXPCCoder:]
+ -[SBSHomeScreenItem isEqual:]
+ -[SBSHomeScreenItem kind]
+ -[SBSHomeScreenItemApplication .cxx_destruct]
+ -[SBSHomeScreenItemApplication bundleIdentifier]
+ -[SBSHomeScreenItemApplication copyWithZone:]
+ -[SBSHomeScreenItemApplication description]
+ -[SBSHomeScreenItemApplication encodeWithBSXPCCoder:]
+ -[SBSHomeScreenItemApplication hash]
+ -[SBSHomeScreenItemApplication initWithBSXPCCoder:]
+ -[SBSHomeScreenItemApplication initWithBundleIdentifier:]
+ -[SBSHomeScreenItemApplication isEqual:]
+ -[SBSHomeScreenItemApplication kind]
+ GCC_except_table10
+ _OBJC_CLASS_$_SBSApplicationRestrictionMonitorProxy
+ _OBJC_CLASS_$_SBSApplicationRestrictionMonitoringService
+ _OBJC_CLASS_$_SBSApplicationRestrictionMonitoringServiceInterfaceSpecification
+ _OBJC_CLASS_$_SBSApplicationRestrictionState
+ _OBJC_CLASS_$_SBSHomeScreenConfiguration
+ _OBJC_CLASS_$_SBSHomeScreenConfigurationLayout
+ _OBJC_CLASS_$_SBSHomeScreenConfigurationService
+ _OBJC_CLASS_$_SBSHomeScreenConfigurationServiceInterfaceSpecification
+ _OBJC_CLASS_$_SBSHomeScreenConfigurationServiceProxy
+ _OBJC_CLASS_$_SBSHomeScreenItem
+ _OBJC_CLASS_$_SBSHomeScreenItemApplication
+ _OBJC_IVAR_$_SBSApplicationRestrictionMonitorProxy._connection
+ _OBJC_IVAR_$_SBSApplicationRestrictionMonitorProxy._monitor
+ _OBJC_IVAR_$_SBSApplicationRestrictionMonitorProxy._queue
+ _OBJC_IVAR_$_SBSApplicationRestrictionState._allowedBundleIdentifiers
+ _OBJC_IVAR_$_SBSApplicationRestrictionState._restrictedBundleIdentifiers
+ _OBJC_IVAR_$_SBSHomeScreenConfiguration._layout
+ _OBJC_IVAR_$_SBSHomeScreenConfiguration._name
+ _OBJC_IVAR_$_SBSHomeScreenConfigurationLayout._dockItems
+ _OBJC_IVAR_$_SBSHomeScreenConfigurationLayout._items
+ _OBJC_IVAR_$_SBSHomeScreenConfigurationServiceProxy._connection
+ _OBJC_IVAR_$_SBSHomeScreenConfigurationServiceProxy._invalidationHandler
+ _OBJC_IVAR_$_SBSHomeScreenConfigurationServiceProxy._queue
+ _OBJC_IVAR_$_SBSHomeScreenItemApplication._bundleIdentifier
+ _OBJC_METACLASS_$_SBSApplicationRestrictionMonitorProxy
+ _OBJC_METACLASS_$_SBSApplicationRestrictionMonitoringService
+ _OBJC_METACLASS_$_SBSApplicationRestrictionMonitoringServiceInterfaceSpecification
+ _OBJC_METACLASS_$_SBSApplicationRestrictionState
+ _OBJC_METACLASS_$_SBSHomeScreenConfiguration
+ _OBJC_METACLASS_$_SBSHomeScreenConfigurationLayout
+ _OBJC_METACLASS_$_SBSHomeScreenConfigurationService
+ _OBJC_METACLASS_$_SBSHomeScreenConfigurationServiceInterfaceSpecification
+ _OBJC_METACLASS_$_SBSHomeScreenConfigurationServiceProxy
+ _OBJC_METACLASS_$_SBSHomeScreenItem
+ _OBJC_METACLASS_$_SBSHomeScreenItemApplication
+ _SBDisplayLayoutBacklightTransitionReasonMagicKeyboardExtended
+ _SBLogApplicationRestrictionMonitoring
+ _SBLogApplicationRestrictionMonitoring.__logObj
+ _SBLogApplicationRestrictionMonitoring.onceToken
+ _SBLogHomeScreenConfiguration
+ _SBLogHomeScreenConfiguration.__logObj
+ _SBLogHomeScreenConfiguration.onceToken
+ _SBSHomeScreenConfigurationErrorDomain
+ __OBJC_$_CLASS_METHODS_SBSApplicationRestrictionMonitoringService
+ __OBJC_$_CLASS_METHODS_SBSApplicationRestrictionMonitoringServiceInterfaceSpecification
+ __OBJC_$_CLASS_METHODS_SBSApplicationRestrictionState
+ __OBJC_$_CLASS_METHODS_SBSHomeScreenConfiguration
+ __OBJC_$_CLASS_METHODS_SBSHomeScreenConfigurationLayout
+ __OBJC_$_CLASS_METHODS_SBSHomeScreenConfigurationService
+ __OBJC_$_CLASS_METHODS_SBSHomeScreenConfigurationServiceInterfaceSpecification
+ __OBJC_$_CLASS_METHODS_SBSHomeScreenItem
+ __OBJC_$_CLASS_METHODS_SBSHomeScreenItemApplication
+ __OBJC_$_CLASS_PROP_LIST_SBSApplicationRestrictionMonitoringServiceInterfaceSpecification
+ __OBJC_$_CLASS_PROP_LIST_SBSApplicationRestrictionState
+ __OBJC_$_CLASS_PROP_LIST_SBSHomeScreenConfigurationServiceInterfaceSpecification
+ __OBJC_$_INSTANCE_METHODS_SBSApplicationRestrictionMonitorProxy
+ __OBJC_$_INSTANCE_METHODS_SBSApplicationRestrictionState
+ __OBJC_$_INSTANCE_METHODS_SBSHomeScreenConfiguration
+ __OBJC_$_INSTANCE_METHODS_SBSHomeScreenConfigurationLayout
+ __OBJC_$_INSTANCE_METHODS_SBSHomeScreenConfigurationServiceProxy
+ __OBJC_$_INSTANCE_METHODS_SBSHomeScreenItem
+ __OBJC_$_INSTANCE_METHODS_SBSHomeScreenItemApplication
+ __OBJC_$_INSTANCE_VARIABLES_SBSApplicationRestrictionMonitorProxy
+ __OBJC_$_INSTANCE_VARIABLES_SBSApplicationRestrictionState
+ __OBJC_$_INSTANCE_VARIABLES_SBSHomeScreenConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_SBSHomeScreenConfigurationLayout
+ __OBJC_$_INSTANCE_VARIABLES_SBSHomeScreenConfigurationServiceProxy
+ __OBJC_$_INSTANCE_VARIABLES_SBSHomeScreenItemApplication
+ __OBJC_$_PROP_LIST_SBSApplicationRestrictionMonitorProxy
+ __OBJC_$_PROP_LIST_SBSApplicationRestrictionState
+ __OBJC_$_PROP_LIST_SBSHomeScreenConfiguration
+ __OBJC_$_PROP_LIST_SBSHomeScreenConfigurationLayout
+ __OBJC_$_PROP_LIST_SBSHomeScreenConfigurationServiceProxy
+ __OBJC_$_PROP_LIST_SBSHomeScreenItem
+ __OBJC_$_PROP_LIST_SBSHomeScreenItemApplication
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBSApplicationRestrictionMonitorClientInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBSHomeScreenConfigurationClientToServerInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBSHomeScreenConfigurationSession
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBSApplicationRestrictionMonitorClientInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBSHomeScreenConfigurationClientToServerInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBSHomeScreenConfigurationSession
+ __OBJC_$_PROTOCOL_REFS_SBSApplicationRestrictionMonitorClientInterface
+ __OBJC_$_PROTOCOL_REFS_SBSApplicationRestrictionMonitorServerInterface
+ __OBJC_$_PROTOCOL_REFS_SBSHomeScreenConfigurationClientToServerInterface
+ __OBJC_$_PROTOCOL_REFS_SBSHomeScreenConfigurationSession
+ __OBJC_CLASS_PROTOCOLS_$_SBSApplicationRestrictionMonitorProxy
+ __OBJC_CLASS_PROTOCOLS_$_SBSApplicationRestrictionState
+ __OBJC_CLASS_PROTOCOLS_$_SBSHomeScreenConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_SBSHomeScreenConfigurationLayout
+ __OBJC_CLASS_PROTOCOLS_$_SBSHomeScreenConfigurationServiceProxy
+ __OBJC_CLASS_PROTOCOLS_$_SBSHomeScreenItem
+ __OBJC_CLASS_RO_$_SBSApplicationRestrictionMonitorProxy
+ __OBJC_CLASS_RO_$_SBSApplicationRestrictionMonitoringService
+ __OBJC_CLASS_RO_$_SBSApplicationRestrictionMonitoringServiceInterfaceSpecification
+ __OBJC_CLASS_RO_$_SBSApplicationRestrictionState
+ __OBJC_CLASS_RO_$_SBSHomeScreenConfiguration
+ __OBJC_CLASS_RO_$_SBSHomeScreenConfigurationLayout
+ __OBJC_CLASS_RO_$_SBSHomeScreenConfigurationService
+ __OBJC_CLASS_RO_$_SBSHomeScreenConfigurationServiceInterfaceSpecification
+ __OBJC_CLASS_RO_$_SBSHomeScreenConfigurationServiceProxy
+ __OBJC_CLASS_RO_$_SBSHomeScreenItem
+ __OBJC_CLASS_RO_$_SBSHomeScreenItemApplication
+ __OBJC_LABEL_PROTOCOL_$_SBSApplicationRestrictionMonitorClientInterface
+ __OBJC_LABEL_PROTOCOL_$_SBSApplicationRestrictionMonitorServerInterface
+ __OBJC_LABEL_PROTOCOL_$_SBSHomeScreenConfigurationClientToServerInterface
+ __OBJC_LABEL_PROTOCOL_$_SBSHomeScreenConfigurationSession
+ __OBJC_METACLASS_RO_$_SBSApplicationRestrictionMonitorProxy
+ __OBJC_METACLASS_RO_$_SBSApplicationRestrictionMonitoringService
+ __OBJC_METACLASS_RO_$_SBSApplicationRestrictionMonitoringServiceInterfaceSpecification
+ __OBJC_METACLASS_RO_$_SBSApplicationRestrictionState
+ __OBJC_METACLASS_RO_$_SBSHomeScreenConfiguration
+ __OBJC_METACLASS_RO_$_SBSHomeScreenConfigurationLayout
+ __OBJC_METACLASS_RO_$_SBSHomeScreenConfigurationService
+ __OBJC_METACLASS_RO_$_SBSHomeScreenConfigurationServiceInterfaceSpecification
+ __OBJC_METACLASS_RO_$_SBSHomeScreenConfigurationServiceProxy
+ __OBJC_METACLASS_RO_$_SBSHomeScreenItem
+ __OBJC_METACLASS_RO_$_SBSHomeScreenItemApplication
+ __OBJC_PROTOCOL_$_SBSApplicationRestrictionMonitorClientInterface
+ __OBJC_PROTOCOL_$_SBSApplicationRestrictionMonitorServerInterface
+ __OBJC_PROTOCOL_$_SBSHomeScreenConfigurationClientToServerInterface
+ __OBJC_PROTOCOL_$_SBSHomeScreenConfigurationSession
+ __OBJC_PROTOCOL_REFERENCE_$_SBSApplicationRestrictionMonitorClientInterface
+ __OBJC_PROTOCOL_REFERENCE_$_SBSApplicationRestrictionMonitorServerInterface
+ __OBJC_PROTOCOL_REFERENCE_$_SBSHomeScreenConfigurationClientToServerInterface
+ ___29-[SBSHomeScreenItem isEqual:]_block_invoke
+ ___38-[SBSHomeScreenConfiguration isEqual:]_block_invoke
+ ___38-[SBSHomeScreenConfiguration isEqual:]_block_invoke_2
+ ___40-[SBSHomeScreenItemApplication isEqual:]_block_invoke
+ ___44-[SBSHomeScreenConfigurationLayout isEqual:]_block_invoke
+ ___44-[SBSHomeScreenConfigurationLayout isEqual:]_block_invoke_2
+ ___54-[SBSApplicationRestrictionMonitorProxy didInvalidate]_block_invoke
+ ___55-[SBSApplicationRestrictionMonitorProxy makeConnection]_block_invoke
+ ___55-[SBSApplicationRestrictionMonitorProxy makeConnection]_block_invoke.8
+ ___55-[SBSApplicationRestrictionMonitorProxy makeConnection]_block_invoke.8.cold.1
+ ___55-[SBSApplicationRestrictionMonitorProxy makeConnection]_block_invoke_2
+ ___56-[SBSHomeScreenConfigurationServiceProxy makeConnection]_block_invoke
+ ___56-[SBSHomeScreenConfigurationServiceProxy makeConnection]_block_invoke.5
+ ___56-[SBSHomeScreenConfigurationServiceProxy makeConnection]_block_invoke.5.cold.1
+ ___56-[SBSHomeScreenConfigurationServiceProxy makeConnection]_block_invoke_2
+ ___68+[SBSHomeScreenConfigurationServiceInterfaceSpecification interface]_block_invoke
+ ___77+[SBSApplicationRestrictionMonitoringServiceInterfaceSpecification interface]_block_invoke
+ ___80-[SBSHomeScreenConfigurationServiceProxy endConfigurationSessionWithCompletion:]_block_invoke
+ ___83-[SBSApplicationRestrictionMonitorProxy observeUpdateWithApplicationRestrictState:]_block_invoke
+ ___97+[SBSHomeScreenConfigurationService beginConfigurationSessionWithInvalidationHandler:completion:]_block_invoke
+ ___SBLogApplicationRestrictionMonitoring_block_invoke
+ ___SBLogHomeScreenConfiguration_block_invoke
+ ___block_descriptor_40_e8_32s_e17_"<NSObject>"8?0ls32l8
+ ___block_descriptor_40_e8_32s_e5_Q8?0ls32l8
+ ___block_literal_global.195
+ ___block_literal_global.198
+ ___block_literal_global.224
+ ___block_literal_global.227
+ _interface.interface
+ _objc_msgSend$appendUnsignedInteger:
+ _objc_msgSend$appendUnsignedInteger:counterpart:
+ _objc_msgSend$applyConfiguration:completion:
+ _objc_msgSend$beginConfigurationSessionWithCompletion:
+ _objc_msgSend$endConfigurationSessionWithCompletion:
+ _objc_msgSend$initWithAllowedIdentifiers:restrictedIdentifiers:
+ _objc_msgSend$kind
+ _objc_msgSend$monitorDidLoseConnection
+ _objc_msgSend$monitorDidUpdateApplicationRestrictionState:
- ___block_literal_global.194
- ___block_literal_global.197
CStrings:
+ "@\"<NSObject>\"8@?0"
+ "@\"<SBSApplicationRestrictionMonitoring>\""
+ "@\"SBSHomeScreenConfigurationLayout\""
+ "ApplicationRestrictionMonitoring"
+ "Client invalidated connection"
+ "HomeScreenConfiguration"
+ "Notifying monitor of an application restriction update"
+ "Q8@?0"
+ "SBSApplicationRestrictionMonitorClientInterface"
+ "SBSApplicationRestrictionMonitorProxy"
+ "SBSApplicationRestrictionMonitorServerInterface"
+ "SBSApplicationRestrictionMonitoringService"
+ "SBSApplicationRestrictionMonitoringServiceInterfaceSpecification"
+ "SBSApplicationRestrictionState"
+ "SBSHomeScreenConfiguration"
+ "SBSHomeScreenConfigurationClientToServerInterface"
+ "SBSHomeScreenConfigurationErrorDomain"
+ "SBSHomeScreenConfigurationLayout"
+ "SBSHomeScreenConfigurationService"
+ "SBSHomeScreenConfigurationServiceInterfaceSpecification"
+ "SBSHomeScreenConfigurationServiceProxy"
+ "SBSHomeScreenConfigurationSession"
+ "SBSHomeScreenItem"
+ "SBSHomeScreenItemApplication"
+ "T@\"NSArray\",R,C,N,V_dockItems"
+ "T@\"NSArray\",R,C,N,V_items"
+ "T@\"NSSet\",R,C,N,V_allowedBundleIdentifiers"
+ "T@\"NSSet\",R,C,N,V_restrictedBundleIdentifiers"
+ "T@\"NSString\",C,N,V_name"
+ "T@\"NSString\",R,C,N,V_bundleIdentifier"
+ "T@\"SBSHomeScreenConfigurationLayout\",C,N,V_layout"
+ "_allowedBundleIdentifiers"
+ "_bundleIdentifier"
+ "_dockItems"
+ "_items"
+ "_layout"
+ "_monitor"
+ "_name"
+ "_restrictedBundleIdentifiers"
+ "allowedBundleIdentifiers"
+ "appendUnsignedInteger:"
+ "appendUnsignedInteger:counterpart:"
+ "applyConfiguration:completion:"
+ "beginConfigurationSessionWithCompletion:"
+ "beginConfigurationSessionWithInvalidationHandler:completion:"
+ "com.apple.SpringBoard.backlight.transitionReason.magicKeyboardExtended"
+ "com.apple.springboard.application-restriction-monitoring-service"
+ "com.apple.springboard.application-restriction-monitoring-service.connectionQueue-%p"
+ "com.apple.springboard.home-screen-configuration-service"
+ "com.apple.springboard.home-screen-configuration.connectionQueue"
+ "dockItems"
+ "endConfigurationSessionWithCompletion:"
+ "initWithAllowedIdentifiers:restrictedIdentifiers:"
+ "initWithBundleIdentifier:"
+ "initWithItems:dockItems:"
+ "items"
+ "kind"
+ "layout"
+ "monitorDidLoseConnection"
+ "monitorDidUpdateApplicationRestrictionState:"
+ "observeUpdateWithApplicationRestrictState:"
+ "registerMonitor:"
+ "restrictedBundleIdentifiers"
+ "setLayout:"
+ "setName:"
+ "v24@0:8@\"SBSApplicationRestrictionState\"16"
+ "v32@0:8@\"SBSHomeScreenConfiguration\"16@?<v@?@\"NSError\">24"

```
