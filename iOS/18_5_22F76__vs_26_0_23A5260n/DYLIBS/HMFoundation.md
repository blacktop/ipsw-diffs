## HMFoundation

> `/System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation`

```diff

-856.6.8.0.0
-  __TEXT.__text: 0x81628
-  __TEXT.__auth_stubs: 0x1ea0
-  __TEXT.__objc_methlist: 0x75a4
-  __TEXT.__const: 0x2158
+875.0.0.0.0
+  __TEXT.__text: 0x83ac0
+  __TEXT.__auth_stubs: 0x20e0
+  __TEXT.__objc_methlist: 0x75cc
+  __TEXT.__const: 0x25c8
   __TEXT.__dlopen_cstrs: 0xf8
-  __TEXT.__cstring: 0x3129
-  __TEXT.__swift5_typeref: 0xb35
-  __TEXT.__swift5_capture: 0x59c
-  __TEXT.__swift_as_entry: 0x184
-  __TEXT.__swift_as_ret: 0x1ac
-  __TEXT.__swift5_reflstr: 0x463
-  __TEXT.__swift5_assocty: 0x98
-  __TEXT.__constg_swiftt: 0xef8
-  __TEXT.__swift5_fieldmd: 0x6b0
-  __TEXT.__swift5_proto: 0x48
-  __TEXT.__swift5_types: 0xa0
-  __TEXT.__swift5_protos: 0x28
-  __TEXT.__oslogstring: 0x3fca
+  __TEXT.__cstring: 0x3163
+  __TEXT.__swift5_typeref: 0x9d3
+  __TEXT.__swift5_capture: 0x5f0
+  __TEXT.__swift_as_entry: 0x168
+  __TEXT.__swift_as_ret: 0x194
+  __TEXT.__constg_swiftt: 0xd38
+  __TEXT.__swift5_reflstr: 0x367
+  __TEXT.__swift5_fieldmd: 0x670
+  __TEXT.__swift5_types: 0x9c
+  __TEXT.__swift5_proto: 0x3c
+  __TEXT.__swift5_protos: 0x1c
+  __TEXT.__oslogstring: 0x4108
+  __TEXT.__swift5_assocty: 0x18
   __TEXT.__gcc_except_tab: 0x1b6c
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x2da8
-  __TEXT.__eh_frame: 0x2fc0
-  __TEXT.__objc_classname: 0x10cd
-  __TEXT.__objc_methname: 0xbf80
-  __TEXT.__objc_methtype: 0x2682
-  __TEXT.__objc_stubs: 0x8a00
-  __DATA_CONST.__got: 0x758
-  __DATA_CONST.__const: 0x1578
+  __TEXT.__unwind_info: 0x2d60
+  __TEXT.__eh_frame: 0x2e5c
+  __TEXT.__objc_classname: 0x10cb
+  __TEXT.__objc_methname: 0xc0d3
+  __TEXT.__objc_methtype: 0x26ca
+  __TEXT.__objc_stubs: 0x8a80
+  __DATA_CONST.__got: 0x7e8
+  __DATA_CONST.__const: 0x1558
   __DATA_CONST.__objc_classlist: 0x458
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x1a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2eb0
+  __DATA_CONST.__objc_selrefs: 0x2ed8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x380
-  __AUTH_CONST.__auth_got: 0xf60
-  __AUTH_CONST.__const: 0x1ee8
+  __AUTH_CONST.__auth_got: 0x1080
+  __AUTH_CONST.__const: 0x1f90
   __AUTH_CONST.__cfstring: 0x4cc0
-  __AUTH_CONST.__objc_const: 0xe188
+  __AUTH_CONST.__objc_const: 0xe218
   __AUTH.__objc_data: 0x1130
-  __AUTH.__data: 0x248
+  __AUTH.__data: 0x150
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
   __DATA.__objc_ivar: 0x198
-  __DATA.__data: 0x2868
-  __DATA.__bss: 0x6c0
-  __DATA_DIRTY.__objc_ivar: 0x59c
+  __DATA.__data: 0x23a0
+  __DATA.__bss: 0x514
+  __DATA_DIRTY.__objc_ivar: 0x5a8
   __DATA_DIRTY.__objc_data: 0x19f0
-  __DATA_DIRTY.__bss: 0x510
+  __DATA_DIRTY.__bss: 0x538
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: F43959AC-40C6-34B5-8522-800B94CF10DD
-  Functions: 3357
-  Symbols:   9137
-  CStrings:  4513
+  UUID: E8E8A068-6E8F-3DB3-B707-BFA137EE2F38
+  Functions: 3356
+  Symbols:   9143
+  CStrings:  4530
 
Symbols:
+ +[HMFProcessInfo bundleIdentifierAndTeamIdentifierFromApplicationIdentifier:bundleIdentifier:teamIdentifier:]
+ -[HMFMessageBinding initWithName:policies:selector:messageReceiver:]
+ -[HMFMessageBinding messageReceiver]
+ -[HMFMessageDispatcher messageBindingForReceiver:forMessage:]
+ -[HMFMessageDispatcher messageRegistrationsForReceiver:name:policies:selector:]
+ -[HMFMessageDispatcher msgBindingsCache]
+ -[HMFProcessInfo auditToken]
+ -[HMFProcessInfo bundleIdentifier]
+ -[HMFProcessInfo initWithXPCConnection:]
+ -[HMFProcessInfo teamIdentifier]
+ _HMFCreateMessageBinding
+ _HMFCreateMessageBindingWithReceiver
+ _HMFProductInfoCharismaOSVersion
+ _HMFProductInfoCheerOSVersion
+ _HMFProductInfoDiscoveryOSVersion
+ _HMFProductInfoLuckOSVersion
+ _HMFProductInfoNapiliOSVersion
+ _OBJC_CLASS_$_OS_dispatch_queue
+ ___block_literal_global.20
+ ___unnamed_23
+ ___unnamed_24
+ ___unnamed_25
+ ___unnamed_26
+ ___unnamed_27
+ ___unnamed_28
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_HMFoundation
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_HMFoundation
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_HMFoundation
+ _generic environment 12HMFoundation012StateMachineB5ValueRzAA0bC5EventR_AaCR0_s23CustomStringConvertible0B9LabelTypeRpzr1_l
+ _nw_endpoint_get_hostname
+ _objc_copyStruct
+ _objc_msgSend$bundleIdentifierAndTeamIdentifierFromApplicationIdentifier:bundleIdentifier:teamIdentifier:
+ _objc_msgSend$characterAtIndex:
+ _objc_msgSend$initWithName:policies:selector:messageReceiver:
+ _objc_msgSend$initWithXPCConnection:
+ _objc_msgSend$messageBindingForDispatcher:message:receiver:
+ _objc_msgSend$messageBindingForReceiver:forMessage:
+ _objc_msgSend$messageReceiver
+ _objc_msgSend$messageRegistrationsForReceiver:name:policies:selector:
+ _objc_msgSend$msgBindingsCache
+ _swift_coroFrameAlloc
+ _swift_getObjCClassMetadata
+ _swift_weakDestroy
+ _swift_weakInit
+ _swift_weakLoadStrong
+ _symbolic $s12HMFoundation012StateMachineB10TransitionP
+ _symbolic $s12HMFoundation012StateMachineB5ValueP
+ _symbolic $s12HMFoundation17StateMachineEventP
+ _symbolic $s12HMFoundation25StateMachineEventReactionP
+ _symbolic 14StateLabelType_____Qz 12HMFoundation012StateMachineB5ValueP
+ _symbolic 14StateLabelType_____Qz05stateB0______yxq_q0__Gq__x_____yxq_q0__GztYaYbc12eventHandlery_____yxq_q0__G_AHztYaYbc0d10TransitionF0t 12HMFoundation012StateMachineB5ValueP AA012HierarchicalbC0C13EventReactionO AE15HandlerDelegateV AE0B10TransitionO
+ _symbolic SS4name_SS4typeSS6domain_____Sg9interfacet 7Network11NWInterfaceV
+ _symbolic SS______Sgt 7Network11NWInterfaceV
+ _symbolic SS______t 7Network10NWEndpointO4PortV
+ _symbolic SS______tSg 7Network10NWEndpointO4PortV
+ _symbolic ScSySS______tG 7Network10NWEndpointO4PortV
+ _symbolic _____ 12HMFoundation17StateMachineErrorO
+ _symbolic _____4host______4portt 7Network10NWEndpointO4HostO AC4PortV
+ _symbolic _____Sg 7Network10NWEndpointO4PortV
+ _symbolic _____Sg 7Network11NWInterfaceV
+ _symbolic _____Sg 7Network12NWConnectionC19EstablishmentReportV
+ _symbolic _____SgXw 7Network12NWConnectionC
+ _symbolic _____SgXwz_Xx 7Network12NWConnectionC
+ _symbolic _____ySS______t_G ScS12ContinuationV 7Network10NWEndpointO4PortV
+ _symbolic _____ySS______t_G ScS8IteratorV 7Network10NWEndpointO4PortV
+ _symbolic _____ySS______t__G ScS12ContinuationV11YieldResultO 7Network10NWEndpointO4PortV
+ _symbolic _____ySS______t__G ScS12ContinuationV15BufferingPolicyO 7Network10NWEndpointO4PortV
+ _symbolic _____yxq_q0__Gq__x_____yxq_q0__GztYaYbc 12HMFoundation24HierarchicalStateMachineC13EventReactionO AC15HandlerDelegateV
+ _symbolic _____yxq_q0___G9nodeState______yxq_q0__Gq__x_____yxq_q0__GztYaYbc12eventHandlery_____yxq_q0__G_AGztYaYbc015stateTransitionD0Say_____yxq_q0__GG9substatest 12HMFoundation24HierarchicalStateMachineC4NodeO0eC4TypeO AC13EventReactionO AC15HandlerDelegateV AC0C10TransitionO AE
+ _type_layout_string 12HMFoundation012StateMachineB5ValueRzAA0bC5EventR_AaCR0_r1_lAA012HierarchicalbC0C04RootB0V09CompositeB7BuilderO10ComponentsVyxq_q0____G
+ _type_layout_string 12HMFoundation012StateMachineB5ValueRzAA0bC5EventR_AaCR0_r1_lAA012HierarchicalbC0C04RootB0V0B7BuilderO10ComponentsVyxq_q0____G
+ _type_layout_string 12HMFoundation012StateMachineB5ValueRzAA0bC5EventR_AaCR0_r1_lAA012HierarchicalbC0C04RootB0V0gB7BuilderO10ComponentsVyxq_q0____G
+ _type_layout_string 12HMFoundation012StateMachineB5ValueRzAA0bC5EventR_AaCR0_r1_lAA012HierarchicalbC0C04RootB0V12BuilderTypesO010OnDelegateE0Vyxq_q0____G
+ _type_layout_string 12HMFoundation012StateMachineB5ValueRzAA0bC5EventR_AaCR0_r1_lAA012HierarchicalbC0C04RootB0V12BuilderTypesO02OnB10TransitionVyxq_q0____G
+ _type_layout_string 12HMFoundation012StateMachineB5ValueRzAA0bC5EventR_AaCR0_r1_lAA012HierarchicalbC0C04RootB0V12BuilderTypesO02OnE0Vyxq_q0____G
+ _type_layout_string 12HMFoundation012StateMachineB5ValueRzAA0bC5EventR_AaCR0_r1_lAA012HierarchicalbC0C04RootB0V12BuilderTypesO05TraceE8ReactionVyxq_q0____G
+ _type_layout_string 12HMFoundation012StateMachineB5ValueRzAA0bC5EventR_AaCR0_r1_lAA012HierarchicalbC0C04RootB0V12BuilderTypesO12OnInitializeVyxq_q0____G
+ _type_layout_string 12HMFoundation012StateMachineB5ValueRzAA0bC5EventR_AaCR0_r1_lAA012HierarchicalbC0C15HandlerDelegateVyxq_q0__G
+ _type_layout_string 12HMFoundation17StateMachineErrorO
- -[HMFMessageDispatcher bindingsCache]
- -[HMFMessageDispatcher messageBindingsForReceiver:]
- -[HMFMessageDispatcher messageRegistrationForReceiver:name:policies:selector:]
- -[HMFProcessInfo dealloc]
- -[HMFProcessInfo initWithIdentifier:]
- -[HMFTimer options]
- GCC_except_table33
- _HMF_MESSAGE_BINDING
- ___block_literal_global.22
- ___unnamed_14
- ___unnamed_15
- ___unnamed_17
- ___unnamed_18
- ___unnamed_3
- ___unnamed_7
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_HMFoundation
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_HMFoundation
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_HMFoundation
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_HMFoundation
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_HMFoundation
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_HMFoundation
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_HMFoundation
- _associated conformance 12HMFoundation24HierarchicalStateMachineC04RootC0Vyxq_q0__GAA0cD0OAdA0C14TransitionTypeAhDP_AH0cF0
- _associated conformance 12HMFoundation24HierarchicalStateMachineC04RootC0Vyxq_q0__GAA0cD0OAdA0C9ValueTypeAhDP_AH0cF0
- _associated conformance 12HMFoundation24HierarchicalStateMachineC04RootC0Vyxq_q0__GAA0cD0OAdA16IsolationContextAhDP_ScA
- _associated conformance 12HMFoundation24HierarchicalStateMachineC04RootC0Vyxq_q0__GAA0cD0OAdA17EventReactionTypeAhDP_AH0fG0
- _associated conformance 12HMFoundation24HierarchicalStateMachineC04RootC0Vyxq_q0__GAA0cD0OAdA19HandlerDelegateTypeAhDP_AH0fG0
- _associated conformance 12HMFoundation24HierarchicalStateMachineC15HandlerDelegateVyxq_q0__GAA0cD0OAdA0F9EventTypeAhDP_AH0G0
- _associated conformance 12HMFoundation24HierarchicalStateMachineC15HandlerDelegateVyxq_q0__GAA0cD0OAdA9EventTypeAhDP_AH0G0
- _associated conformance 12HMFoundation24HierarchicalStateMachineCyxq_q0_GAA0cD0O14EngineProtocolAA04RootC4TypeAfGP_AF0gC0
- _generic environment 12HMFoundation12StateMachineO0B5ValueRzAC5EventR_AcER0_s23CustomStringConvertible0B9LabelTypeRpzr1_l
- _objc_msgSend$initWithIdentifier:
- _objc_msgSend$initWithName:policies:selector:
- _objc_msgSend$messageBindingsForDispatcher:
- _objc_msgSend$messageBindingsForReceiver:
- _objc_msgSend$messageRegistrationForReceiver:name:policies:selector:
- _swift_errorRetain
- _symbolic $s12HMFoundation12StateMachineO04RootB0P
- _symbolic $s12HMFoundation12StateMachineO0B10TransitionP
- _symbolic $s12HMFoundation12StateMachineO0B5ValueP
- _symbolic $s12HMFoundation12StateMachineO13EventReactionP
- _symbolic $s12HMFoundation12StateMachineO14EngineProtocolP
- _symbolic $s12HMFoundation12StateMachineO15HandlerDelegateP
- _symbolic $s12HMFoundation12StateMachineO5EventP
- _symbolic 13RootStateType_____Qz 12HMFoundation12StateMachineO14EngineProtocolP
- _symbolic 14StateLabelType_____Qz 12HMFoundation12StateMachineO0B5ValueP
- _symbolic 14StateLabelType_____Qz05stateB0______yxq_q0__Gq_______yxq_q0__GztYaYbc12eventHandlery_____yxq_q0__G_AHztYaYbc0d10TransitionF0t 12HMFoundation12StateMachineO0B5ValueP AA012HierarchicalbC0C13EventReactionO AG15HandlerDelegateV AG0B10TransitionO
- _symbolic 14StateValueType_____Qz 12HMFoundation12StateMachineO04RootB0P
- _symbolic 16IsolationContext_____Qz 12HMFoundation12StateMachineO04RootB0P
- _symbolic 17DelegateEventType_____Qz 12HMFoundation12StateMachineO04RootB0P
- _symbolic 17DelegateEventType_____Qz 12HMFoundation12StateMachineO15HandlerDelegateP
- _symbolic 17EventReactionType_____Qz 12HMFoundation12StateMachineO04RootB0P
- _symbolic 19HandlerDelegateType_____Qz 12HMFoundation12StateMachineO04RootB0P
- _symbolic 19HandlerDelegateType______05EventC0_____QZ 12HMFoundation12StateMachineO04RootB0P AC15HandlerDelegateP
- _symbolic 19HandlerDelegateType______0b5EventC0_____QZ 12HMFoundation12StateMachineO04RootB0P AC15HandlerDelegateP
- _symbolic 19StateTransitionType_____Qz 12HMFoundation12StateMachineO04RootB0P
- _symbolic 9EventType_____Qz 12HMFoundation12StateMachineO04RootB0P
- _symbolic 9EventType_____Qz 12HMFoundation12StateMachineO15HandlerDelegateP
- _symbolic _____ 12HMFoundation12StateMachineO
- _symbolic _____ 12HMFoundation12StateMachineO5ErrorO
- _symbolic _____yxq_q0__G 12HMFoundation24HierarchicalStateMachineC0C10TransitionO
- _symbolic _____yxq_q0__G 12HMFoundation24HierarchicalStateMachineC13EventReactionO
- _symbolic _____yxq_q0__G 12HMFoundation24HierarchicalStateMachineC15HandlerDelegateV
- _symbolic _____yxq_q0__Gq_______yxq_q0__GztYaYbc 12HMFoundation24HierarchicalStateMachineC13EventReactionO AC15HandlerDelegateV
- _symbolic _____yxq_q0___G9nodeState______yxq_q0__Gq_______yxq_q0__GztYaYbc12eventHandlery_____yxq_q0__G_AGztYaYbc015stateTransitionD0Say_____yxq_q0__GG9substatest 12HMFoundation24HierarchicalStateMachineC4NodeO0eC4TypeO AC13EventReactionO AC15HandlerDelegateV AC0C10TransitionO AE
- _type_layout_string 12HMFoundation12StateMachineO0B5ValueRzAC5EventR_AcER0_r1_lAA012HierarchicalbC0C04RootB0V09CompositeB7BuilderO10ComponentsVyxq_q0____G
- _type_layout_string 12HMFoundation12StateMachineO0B5ValueRzAC5EventR_AcER0_r1_lAA012HierarchicalbC0C04RootB0V0B7BuilderO10ComponentsVyxq_q0____G
- _type_layout_string 12HMFoundation12StateMachineO0B5ValueRzAC5EventR_AcER0_r1_lAA012HierarchicalbC0C04RootB0V0gB7BuilderO10ComponentsVyxq_q0____G
- _type_layout_string 12HMFoundation12StateMachineO0B5ValueRzAC5EventR_AcER0_r1_lAA012HierarchicalbC0C04RootB0V12BuilderTypesO010OnDelegateE0Vyxq_q0____G
- _type_layout_string 12HMFoundation12StateMachineO0B5ValueRzAC5EventR_AcER0_r1_lAA012HierarchicalbC0C04RootB0V12BuilderTypesO02OnB10TransitionVyxq_q0____G
- _type_layout_string 12HMFoundation12StateMachineO0B5ValueRzAC5EventR_AcER0_r1_lAA012HierarchicalbC0C04RootB0V12BuilderTypesO02OnE0Vyxq_q0____G
- _type_layout_string 12HMFoundation12StateMachineO0B5ValueRzAC5EventR_AcER0_r1_lAA012HierarchicalbC0C04RootB0V12BuilderTypesO05TraceE8ReactionVyxq_q0____G
- _type_layout_string 12HMFoundation12StateMachineO0B5ValueRzAC5EventR_AcER0_r1_lAA012HierarchicalbC0C04RootB0V12BuilderTypesO12OnInitializeVyxq_q0____G
- _type_layout_string 12HMFoundation12StateMachineO0B5ValueRzAC5EventR_AcER0_r1_lAA012HierarchicalbC0C15HandlerDelegateVyxq_q0__G
- _type_layout_string 12HMFoundation12StateMachineO5ErrorO
CStrings:
+ "%{public}@Failed to get audit token for current process: %d"
+ "@\"HMFTimer\"28@0:8d16I24"
+ "@\"HMFTimer\"44@0:8d16d24q32I40"
+ "@28@0:8I16@20"
+ "@28@0:8d16I24"
+ "@44@0:8d16d24q32I40"
+ "@48@0:8@16@24:32@40"
+ "HMFoundation: NWConnection+ResolveHostAndPort encountered unexpected 'NWEndpoint' type."
+ "HMFoundation: NWConnection+ResolveHostAndPort received unexpected 'NWEndpoint.hostPort(host:port:)' arg for 'host'."
+ "HMFoundation: NWEndpoint+ResolveHostAndPort received unexpected 'NWConnection.State' value."
+ "No results from server search"
+ "T@\"<HMFMessageReceiver>\",R,N,V_messageReceiver"
+ "T@\"NSCache\",R,N,V_msgBindingsCache"
+ "T@\"NSString\",R,C,V_teamIdentifier"
+ "TB,R,GisCodeSigned"
+ "TB,R,GisPlatformBinary"
+ "T{?=[8I]},R,V_auditToken"
+ "_Concurrency/arm64e-apple-ios.private.swiftinterface"
+ "_messageReceiver"
+ "_msgBindingsCache"
+ "_teamIdentifier"
+ "bundleIdentifierAndTeamIdentifierFromApplicationIdentifier:bundleIdentifier:teamIdentifier:"
+ "characterAtIndex:"
+ "initWithName:policies:selector:messageReceiver:"
+ "initWithXPCConnection:"
+ "messageBindingForDispatcher:message:receiver:"
+ "messageBindingForReceiver:forMessage:"
+ "messageReceiver"
+ "messageRegistrationsForReceiver:name:policies:selector:"
+ "msgBindingsCache"
+ "teamIdentifier"
+ "v40@0:8@16^@24^@32"
+ "{?=\"val\"[8I]}"
+ "{?=[8I]}16@0:8"
- "%{public}@Unable to determine current audit token"
- "@\"HMFTimer\"32@0:8d16Q24"
- "@\"HMFTimer\"48@0:8d16d24q32Q40"
- "@32@0:8d16Q24"
- "@48@0:8d16d24q32Q40"
- "T@\"HMFBoolean\",R,C,GisCodeSigned"
- "T@\"HMFBoolean\",R,C,GisPlatformBinary"
- "T@\"NSCache\",R,N,V_bindingsCache"
- "^{?=[8I]}"
- "_Concurrency/TaskGroup.swift"
- "_bindingsCache"
- "bindingsCache"
- "initWithIdentifier:"
- "messageBindingsForDispatcher:"
- "messageBindingsForReceiver:"
- "messageRegistrationForReceiver:name:policies:selector:"

```
