## UIKitServices

> `/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`

```diff

-8506.1.101.0.0
-  __TEXT.__text: 0x1e578
-  __TEXT.__auth_stubs: 0xf30
-  __TEXT.__objc_methlist: 0x2b94
-  __TEXT.__const: 0x2b8
+9071.1.107.0.0
+  __TEXT.__text: 0x2097c
+  __TEXT.__auth_stubs: 0xf80
+  __TEXT.__objc_methlist: 0x2d2c
+  __TEXT.__const: 0x2c8
   __TEXT.__dlopen_cstrs: 0x2fc
-  __TEXT.__cstring: 0x3f66
-  __TEXT.__oslogstring: 0x62b
-  __TEXT.__gcc_except_tab: 0x438
-  __TEXT.__unwind_info: 0xac8
-  __TEXT.__objc_classname: 0x992
-  __TEXT.__objc_methname: 0x621a
-  __TEXT.__objc_methtype: 0x166c
-  __TEXT.__objc_stubs: 0x3ec0
+  __TEXT.__cstring: 0x44a9
+  __TEXT.__oslogstring: 0x671
+  __TEXT.__gcc_except_tab: 0x498
+  __TEXT.__unwind_info: 0xb10
+  __TEXT.__objc_classname: 0xa6a
+  __TEXT.__objc_methname: 0x6479
+  __TEXT.__objc_methtype: 0x1767
+  __TEXT.__objc_stubs: 0x3fa0
   __DATA_CONST.__got: 0x468
-  __DATA_CONST.__const: 0x938
-  __DATA_CONST.__objc_classlist: 0x218
+  __DATA_CONST.__const: 0xa20
+  __DATA_CONST.__objc_classlist: 0x238
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x98
+  __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x16c0
-  __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x1c0
-  __DATA_CONST.__objc_arraydata: 0x6d0
-  __AUTH_CONST.__auth_got: 0x7b0
-  __AUTH_CONST.__const: 0x260
-  __AUTH_CONST.__cfstring: 0x3480
-  __AUTH_CONST.__objc_const: 0x59e0
+  __DATA_CONST.__objc_selrefs: 0x1720
+  __DATA_CONST.__objc_protorefs: 0x38
+  __DATA_CONST.__objc_superrefs: 0x1d0
+  __DATA_CONST.__objc_arraydata: 0x720
+  __AUTH_CONST.__auth_got: 0x7d8
+  __AUTH_CONST.__const: 0x2e0
+  __AUTH_CONST.__cfstring: 0x37c0
+  __AUTH_CONST.__objc_const: 0x5ef8
   __AUTH_CONST.__objc_intobj: 0x1e0
-  __AUTH_CONST.__objc_arrayobj: 0x198
+  __AUTH_CONST.__objc_arrayobj: 0x1b0
   __AUTH_CONST.__objc_doubleobj: 0x80
-  __AUTH_CONST.__objc_dictobj: 0x438
-  __AUTH.__objc_data: 0xcd0
+  __AUTH_CONST.__objc_dictobj: 0x460
+  __AUTH.__objc_data: 0xe60
   __AUTH.__data: 0x50
-  __DATA.__objc_ivar: 0x270
-  __DATA.__data: 0x740
+  __DATA.__objc_ivar: 0x298
+  __DATA.__data: 0x7a0
   __DATA.__bss: 0x88
   __DATA_DIRTY.__objc_ivar: 0x44
-  __DATA_DIRTY.__objc_data: 0x820
-  __DATA_DIRTY.__bss: 0x160
+  __DATA_DIRTY.__objc_data: 0x7d0
+  __DATA_DIRTY.__bss: 0x168
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4E37FF33-CD77-3266-8D98-6F6A6C9B0F2A
-  Functions: 926
-  Symbols:   3640
-  CStrings:  2314
+  UUID: 7919B303-0BC8-371E-ABC5-4A84B10ABB91
+  Functions: 969
+  Symbols:   3802
+  CStrings:  2400
 
Symbols:
+ +[UISSceneConnectionValueAction actionWithFlag:forKey:responder:]
+ +[UISSceneConnectionValueAction actionWithValue:forKey:responder:]
+ +[UISSceneHostingExternalSettingsModifierClient defaultShellEndpoint]
+ +[UISSceneHostingSettingsModifier supportsBSXPCSecureCoding]
+ -[UISIntentForwardingAction initWithIntent:responseQueue:reply:]
+ -[UISIntentForwardingAction initWithIntentForwardingAction:responseQueue:responseHandler:]
+ -[UISSceneConnectionValueAction UIActionType]
+ -[UISSceneHostingExternalSettingsModifierClient .cxx_destruct]
+ -[UISSceneHostingExternalSettingsModifierClient dealloc]
+ -[UISSceneHostingExternalSettingsModifierClient initWithServerEndpoint:]
+ -[UISSceneHostingExternalSettingsModifierClient init]
+ -[UISSceneHostingExternalSettingsModifierClient invalidate]
+ -[UISSceneHostingExternalSettingsModifierClient requestSettingsModifiersForProcessIdentity:withCompletion:]
+ -[UISSceneHostingExternalSettingsModifierService .cxx_destruct]
+ -[UISSceneHostingExternalSettingsModifierService dealloc]
+ -[UISSceneHostingExternalSettingsModifierService delegate]
+ -[UISSceneHostingExternalSettingsModifierService endpoint]
+ -[UISSceneHostingExternalSettingsModifierService initWithCalloutQueue:]
+ -[UISSceneHostingExternalSettingsModifierService init]
+ -[UISSceneHostingExternalSettingsModifierService invalidate]
+ -[UISSceneHostingExternalSettingsModifierService listener:didReceiveConnection:withContext:]
+ -[UISSceneHostingExternalSettingsModifierService requestSettingsModifiersForProcessIdentity:withCompletion:]
+ -[UISSceneHostingExternalSettingsModifierService setDelegate:]
+ -[UISSceneHostingSettingsModifier encodeWithBSXPCCoder:]
+ -[UISSceneHostingSettingsModifier initWithBSXPCCoder:]
+ -[UISSceneHostingSettingsModifier updaterForProposedSettings:withSettingsDiff:]
+ GCC_except_table15
+ GCC_except_table16
+ GCC_except_table6
+ GCC_except_table7
+ _BSDispatchMain
+ _BSDispatchQueueAssertMain
+ _NSStringFromClass
+ _NSStringFromSelector
+ _OBJC_CLASS_$_BSMutableKeyedSettings
+ _OBJC_CLASS_$_BSServiceDispatchQueue
+ _OBJC_CLASS_$_UISSceneConnectionValueAction
+ _OBJC_CLASS_$_UISSceneHostingExternalSettingsModifierClient
+ _OBJC_CLASS_$_UISSceneHostingExternalSettingsModifierService
+ _OBJC_CLASS_$_UISSceneHostingSettingsModifier
+ _OBJC_IVAR_$_UISSceneHostingExternalSettingsModifierClient._endpoint
+ _OBJC_IVAR_$_UISSceneHostingExternalSettingsModifierClient._queue
+ _OBJC_IVAR_$_UISSceneHostingExternalSettingsModifierClient._queue_connection
+ _OBJC_IVAR_$_UISSceneHostingExternalSettingsModifierClient._queue_invalidated
+ _OBJC_IVAR_$_UISSceneHostingExternalSettingsModifierService._calloutQueue
+ _OBJC_IVAR_$_UISSceneHostingExternalSettingsModifierService._lock
+ _OBJC_IVAR_$_UISSceneHostingExternalSettingsModifierService._lock_delegate
+ _OBJC_IVAR_$_UISSceneHostingExternalSettingsModifierService._lock_delegateFlags
+ _OBJC_IVAR_$_UISSceneHostingExternalSettingsModifierService._lock_invalidated
+ _OBJC_IVAR_$_UISSceneHostingExternalSettingsModifierService._lock_listener
+ _OBJC_METACLASS_$_UISSceneConnectionValueAction
+ _OBJC_METACLASS_$_UISSceneHostingExternalSettingsModifierClient
+ _OBJC_METACLASS_$_UISSceneHostingExternalSettingsModifierService
+ _OBJC_METACLASS_$_UISSceneHostingSettingsModifier
+ _UISDisplayConfigurationChangedNotification
+ _UISDisplayConfigurationForContextID
+ _UISRequestDisplayConfigurationForContextID
+ _UISSDisplayConfigurationAffectedContextIDsKey
+ _UISSceneConnectionValueErrorDomain
+ _UISSceneHostingExternalSettingsModifierServiceErrorDomain
+ _UISSceneHostingExternalSettingsModifierServiceIdentifier
+ _UISSetDisplayConfigurationDataSource
+ __OBJC_$_CLASS_METHODS_UISSceneConnectionValueAction
+ __OBJC_$_CLASS_METHODS_UISSceneHostingExternalSettingsModifierClient
+ __OBJC_$_CLASS_METHODS_UISSceneHostingSettingsModifier
+ __OBJC_$_CLASS_PROP_LIST_UISSceneHostingExternalSettingsModifierClient
+ __OBJC_$_INSTANCE_METHODS_UISSceneConnectionValueAction
+ __OBJC_$_INSTANCE_METHODS_UISSceneHostingExternalSettingsModifierClient
+ __OBJC_$_INSTANCE_METHODS_UISSceneHostingExternalSettingsModifierService
+ __OBJC_$_INSTANCE_METHODS_UISSceneHostingSettingsModifier
+ __OBJC_$_INSTANCE_VARIABLES_UISSceneHostingExternalSettingsModifierClient
+ __OBJC_$_INSTANCE_VARIABLES_UISSceneHostingExternalSettingsModifierService
+ __OBJC_$_PROP_LIST_UISSceneHostingExternalSettingsModifierClient
+ __OBJC_$_PROP_LIST_UISSceneHostingExternalSettingsModifierService
+ __OBJC_$_PROP_LIST_UISSceneHostingSettingsModifier
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_UISSceneHostingExternalSettingsModifierXPCServerInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UISSceneHostingExternalSettingsModifierXPCServerInterface
+ __OBJC_$_PROTOCOL_REFS_UISSceneHostingExternalSettingsModifierXPCServerInterface
+ __OBJC_CLASS_PROTOCOLS_$_UISSceneHostingExternalSettingsModifierClient
+ __OBJC_CLASS_PROTOCOLS_$_UISSceneHostingExternalSettingsModifierService
+ __OBJC_CLASS_PROTOCOLS_$_UISSceneHostingSettingsModifier
+ __OBJC_CLASS_RO_$_UISSceneConnectionValueAction
+ __OBJC_CLASS_RO_$_UISSceneHostingExternalSettingsModifierClient
+ __OBJC_CLASS_RO_$_UISSceneHostingExternalSettingsModifierService
+ __OBJC_CLASS_RO_$_UISSceneHostingSettingsModifier
+ __OBJC_LABEL_PROTOCOL_$_UISSceneHostingExternalSettingsModifierXPCServerInterface
+ __OBJC_METACLASS_RO_$_UISSceneConnectionValueAction
+ __OBJC_METACLASS_RO_$_UISSceneHostingExternalSettingsModifierClient
+ __OBJC_METACLASS_RO_$_UISSceneHostingExternalSettingsModifierService
+ __OBJC_METACLASS_RO_$_UISSceneHostingSettingsModifier
+ __OBJC_PROTOCOL_$_UISSceneHostingExternalSettingsModifierXPCServerInterface
+ __OBJC_PROTOCOL_REFERENCE_$_UISSceneHostingExternalSettingsModifierXPCServerInterface
+ __ZNSt3__16vectorIdNS_9allocatorIdEEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIdNS_9allocatorIdEEE9push_backB8nn200100EOd
+ __ZSt28__throw_bad_array_new_lengthB8nn200100v
+ __ZnwmSt19__type_descriptor_t
+ ___107-[UISSceneHostingExternalSettingsModifierClient requestSettingsModifiersForProcessIdentity:withCompletion:]_block_invoke
+ ___107-[UISSceneHostingExternalSettingsModifierClient requestSettingsModifiersForProcessIdentity:withCompletion:]_block_invoke_2
+ ___108-[UISApplicationSupportService destroyScenesPersistentIdentifiers:animationType:destroySessions:completion:]_block_invoke.139
+ ___59-[UISSceneHostingExternalSettingsModifierClient invalidate]_block_invoke
+ ___62-[UISSceneHostingExternalSettingsModifierClient _remoteTarget]_block_invoke
+ ___62-[UISSceneHostingExternalSettingsModifierClient _remoteTarget]_block_invoke_2
+ ___62-[UISSceneHostingExternalSettingsModifierClient _remoteTarget]_block_invoke_3
+ ___62-[UISSceneHostingExternalSettingsModifierClient _remoteTarget]_block_invoke_4
+ ___62-[UISSceneHostingExternalSettingsModifierClient _remoteTarget]_block_invoke_5
+ ___64-[UISIntentForwardingAction initWithIntent:responseQueue:reply:]_block_invoke
+ ___71-[UISSceneHostingExternalSettingsModifierService initWithCalloutQueue:]_block_invoke
+ ___74-[UISApplicationSupportService initializeClientWithParameters:completion:]_block_invoke.111
+ ___90-[UISIntentForwardingAction initWithIntentForwardingAction:responseQueue:responseHandler:]_block_invoke
+ ___92-[UISSceneHostingExternalSettingsModifierService listener:didReceiveConnection:withContext:]_block_invoke
+ ___92-[UISSceneHostingExternalSettingsModifierService listener:didReceiveConnection:withContext:]_block_invoke_2
+ ___92-[UISSceneHostingExternalSettingsModifierService listener:didReceiveConnection:withContext:]_block_invoke_3
+ ___block_descriptor_32_e25_v16?0"<BSXPCEncoding>"8l
+ ___block_descriptor_40_e8_32bs_e64_v24?0"NSSet<__UISSceneHostingSettingsModifier__>"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32w_e29_v16?0"BSServiceConnection"8lw32l8
+ ___block_descriptor_48_e8_32s40s_e50_v16?0"<BSServiceConnectionListenerConfiguring>"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48w_e42_v16?0"<BSServiceConnectionConfiguring>"8ls32l8s40l8w48l8
+ ___block_literal_global.73
+ ___block_literal_global.75
+ ___block_literal_global.82
+ ___block_literal_global.92
+ ___block_literal_global.94
+ ___dataSource
+ __bs_set_crash_log_message
+ _objc_msgSend$assertBarrierOnQueue
+ _objc_msgSend$bs_isPlistableType
+ _objc_msgSend$displayConfigurationForContextID:
+ _objc_msgSend$endpoint
+ _objc_msgSend$initWithIntent:responseQueue:reply:
+ _objc_msgSend$initWithIntentForwardingAction:responseQueue:responseHandler:
+ _objc_msgSend$queueWithName:serviceQuality:
+ _objc_msgSend$remoteToken
+ _objc_msgSend$requestDisplayConfiguration:forContextID:
+ _objc_msgSend$requestSettingsModifiersForProcessIdentity:withCompletion:
+ _objc_msgSend$setFlag:forKey:
+ _objc_msgSend$settingsModifiersForClientProcessIdentity:hostedBy:
+ _objc_retain_x4
- GCC_except_table14
- GCC_except_table5
- _BSDispatchQueueCreate
- _OBJC_CLASS_$_BSDispatchQueueAttributes
- _OBJC_CLASS_$_FBSSerialQueue
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIdEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZSt28__throw_bad_array_new_lengthB8nn190102v
- __Znwm
- ___108-[UISApplicationSupportService destroyScenesPersistentIdentifiers:animationType:destroySessions:completion:]_block_invoke.140
- ___50-[UISIntentForwardingAction initWithIntent:reply:]_block_invoke
- ___74-[UISApplicationSupportService initializeClientWithParameters:completion:]_block_invoke.112
- ___76-[UISIntentForwardingAction initWithIntentForwardingAction:responseHandler:]_block_invoke
- ___block_literal_global.71
- ___block_literal_global.93
- ___block_literal_global.95
- _objc_msgSend$assertOnQueue
- _objc_msgSend$queueWithDispatchQueue:
- _objc_msgSend$serial
- _objc_msgSend$serviceClass:
- _objc_msgSend$setTargetDispatchingQueue:
CStrings:
+ "!_lock_invalidated"
+ "(none found, is the service specified in this process's BSServiceDomains?)"
+ "-[UISIntentForwardingAction initWithIntent:responseQueue:reply:]"
+ "-[UISIntentForwardingAction initWithIntentForwardingAction:responseQueue:responseHandler:]"
+ "-[UISSceneHostingSettingsModifier encodeWithBSXPCCoder:]"
+ "-[UISSceneHostingSettingsModifier initWithBSXPCCoder:]"
+ "-[UISSceneHostingSettingsModifier updaterForProposedSettings:withSettingsDiff:]"
+ "-init is not allowed on UISSceneHostingExternalSettingsModifierClient"
+ "@\"<UISSceneHostingExternalSettingsModifierServiceDelegate>\""
+ "@\"BSServiceConnectionEndpoint\""
+ "@\"BSServiceQueue\""
+ "@36@0:8B16@20@28"
+ "@?32@0:8@16@24"
+ "Implementation required for abstract method %s"
+ "Invalid condition not satisfying: %@"
+ "New from Clipboard"
+ "T@\"<UISSceneHostingExternalSettingsModifierServiceDelegate>\",W,N"
+ "T@\"BSServiceConnectionEndpoint\",R,N"
+ "UISDisplayConfigurationChangedNotification"
+ "UISSDisplayConfigurationAffectedContextIDsKey"
+ "UISSceneConnectionValueAction"
+ "UISSceneConnectionValueAction.m"
+ "UISSceneConnectionValueErrorDomain"
+ "UISSceneHostingExternalSettingsModifierClient"
+ "UISSceneHostingExternalSettingsModifierClient must be invalidated before dealloc"
+ "UISSceneHostingExternalSettingsModifierClient.m"
+ "UISSceneHostingExternalSettingsModifierService"
+ "UISSceneHostingExternalSettingsModifierService.m"
+ "UISSceneHostingExternalSettingsModifierServiceErrorDomain"
+ "UISSceneHostingExternalSettingsModifierXPCServerInterface"
+ "UISSceneHostingSettingsModifier"
+ "UISSceneHostingSettingsModifier.m"
+ "Value must be a Plistable type"
+ "Vv32@0:8@\"RBSProcessIdentity\"16@?<v@?@\"NSSet<__UISSceneHostingSettingsModifier__>\"@\"NSError\">24"
+ "Vv32@0:8@16@?24"
+ "_endpoint"
+ "_lock_invalidated"
+ "_lock_listener"
+ "actionWithFlag:forKey:responder:"
+ "actionWithValue:forKey:responder:"
+ "assertBarrierOnQueue"
+ "bs_isPlistableType"
+ "com.apple.Journal"
+ "com.apple.MomentsUIService"
+ "com.apple.action.newFromPasteboard"
+ "com.apple.uikit.sceneHostingExternalSettingsModifierClient"
+ "com.apple.uis.scene-hosting-external-settings-modifier-service"
+ "com.apple.uis.scene-hosting-external-settings-modifier-service.server"
+ "defaultShellEndpoint"
+ "displayConfigurationForContextID:"
+ "endpoint"
+ "failure in %{public}@ of <%{public}@:%p> (%{public}@:%i) : %{public}@"
+ "initWithIntent:responseQueue:reply:"
+ "initWithIntentForwardingAction:responseQueue:responseHandler:"
+ "initWithServerEndpoint:"
+ "must call invalidate before dealloc"
+ "queue"
+ "queueWithName:serviceQuality:"
+ "remoteToken"
+ "requestDisplayConfiguration:forContextID:"
+ "requestSettingsModifiersForProcessIdentity:withCompletion:"
+ "serverEndpoint"
+ "setFlag:forKey:"
+ "settingsModifiersForClientProcessIdentity:hostedBy:"
+ "updaterForProposedSettings:withSettingsDiff:"
+ "v24@?0@\"NSSet<__UISSceneHostingSettingsModifier__>\"8@\"NSError\"16"
+ "{?=\"delegateSupportsSettingsModifiersForClientProcessIdentityHostedByAuditToken\"b1}"
+ "{vector<double, std::allocator<double>>=\"__begin_\"^d\"__end_\"^d\"__cap_\"^d}"
- "-[UISIntentForwardingAction initWithIntent:reply:]"
- "-[UISIntentForwardingAction initWithIntentForwardingAction:responseHandler:]"
- "@\"FBSSerialQueue\""
- "assertOnQueue"
- "queueWithDispatchQueue:"
- "serial"
- "serviceClass:"
- "setTargetDispatchingQueue:"
- "{vector<double, std::allocator<double>>=\"__begin_\"^d\"__end_\"^d\"__end_cap_\"{__compressed_pair<double *, std::allocator<double>>=\"__value_\"^d}}"

```
