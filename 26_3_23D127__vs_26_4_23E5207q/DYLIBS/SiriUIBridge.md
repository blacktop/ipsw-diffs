## SiriUIBridge

> `/System/Library/PrivateFrameworks/SiriUIBridge.framework/SiriUIBridge`

```diff

-3500.14.1.0.0
-  __TEXT.__text: 0x19690
-  __TEXT.__auth_stubs: 0xf40
-  __TEXT.__objc_methlist: 0x1080
-  __TEXT.__const: 0x468
-  __TEXT.__cstring: 0xccb
-  __TEXT.__constg_swiftt: 0x764
-  __TEXT.__swift5_typeref: 0x6bc
+3520.29.1.0.0
+  __TEXT.__text: 0x25ff0
+  __TEXT.__auth_stubs: 0xfa0
+  __TEXT.__objc_methlist: 0x17d4
+  __TEXT.__const: 0x4e0
+  __TEXT.__cstring: 0x113a
+  __TEXT.__constg_swiftt: 0x814
+  __TEXT.__swift5_typeref: 0x8ae
   __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_types: 0x2c
-  __TEXT.__swift5_fieldmd: 0x1d4
-  __TEXT.__swift5_reflstr: 0x1fb
+  __TEXT.__swift5_types: 0x34
+  __TEXT.__swift5_fieldmd: 0x200
+  __TEXT.__swift5_reflstr: 0x20b
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__oslogstring: 0xd03
-  __TEXT.__swift5_capture: 0x790
-  __TEXT.__unwind_info: 0x7f0
-  __TEXT.__eh_frame: 0xa0
-  __TEXT.__objc_classname: 0x374
-  __TEXT.__objc_methname: 0x1996
-  __TEXT.__objc_methtype: 0x8ff
-  __TEXT.__objc_stubs: 0x6a0
-  __DATA_CONST.__got: 0x270
-  __DATA_CONST.__const: 0x3b8
-  __DATA_CONST.__objc_classlist: 0xe0
-  __DATA_CONST.__objc_protolist: 0xa8
+  __TEXT.__swift5_capture: 0x8c8
+  __TEXT.__oslogstring: 0xdf3
+  __TEXT.__unwind_info: 0x988
+  __TEXT.__eh_frame: 0x1b8
+  __TEXT.__objc_classname: 0x707
+  __TEXT.__objc_methname: 0x2371
+  __TEXT.__objc_methtype: 0xf59
+  __TEXT.__objc_stubs: 0x1180
+  __DATA_CONST.__got: 0x2d0
+  __DATA_CONST.__const: 0x4a0
+  __DATA_CONST.__objc_classlist: 0x140
+  __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5a8
+  __DATA_CONST.__objc_selrefs: 0x700
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_superrefs: 0x58
-  __AUTH_CONST.__auth_got: 0x7a8
-  __AUTH_CONST.__const: 0x1cc8
-  __AUTH_CONST.__cfstring: 0x300
-  __AUTH_CONST.__objc_const: 0x21e0
-  __AUTH.__objc_data: 0x7b8
-  __AUTH.__data: 0x68
-  __DATA.__objc_ivar: 0x94
-  __DATA.__data: 0x6a8
-  __DATA_DIRTY.__objc_data: 0x700
-  __DATA_DIRTY.__data: 0x3c8
+  __DATA_CONST.__objc_superrefs: 0xa0
+  __AUTH_CONST.__auth_got: 0x7d8
+  __AUTH_CONST.__const: 0x2068
+  __AUTH_CONST.__cfstring: 0x580
+  __AUTH_CONST.__objc_const: 0x3030
+  __AUTH.__objc_data: 0x858
+  __AUTH.__data: 0x108
+  __DATA.__objc_ivar: 0xf8
+  __DATA.__data: 0x648
+  __DATA_DIRTY.__objc_data: 0xa20
+  __DATA_DIRTY.__data: 0x4c8
   __DATA_DIRTY.__common: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/SiriRequestDispatcher.framework/SiriRequestDispatcher
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F14EC596-03EE-3B98-ADB7-D6C8E4A4F075
-  Functions: 1067
-  Symbols:   1613
-  CStrings:  537
+  UUID: EF7B925E-711C-3FCC-B9DF-5C30D77C7D94
+  Functions: 1395
+  Symbols:   2328
+  CStrings:  725
 
Symbols:
+ +[SUIBSessionRetrieved supportsSecureCoding]
+ +[SUIBSessionRetrievedPayload supportsSecureCoding]
+ +[SUIBSystemTurnInterruptionEndedContext supportsSecureCoding]
+ +[SUIBSystemTurnInterruptionStartedContext supportsSecureCoding]
+ +[SUIBUserSpeechPresence supportsSecureCoding]
+ +[SUIBUserTurnEndedContext supportsSecureCoding]
+ +[SUIBUserTurnFinalizedContext supportsSecureCoding]
+ -[SUIBSessionRetrieved .cxx_destruct]
+ -[SUIBSessionRetrieved description]
+ -[SUIBSessionRetrieved encodeWithCoder:]
+ -[SUIBSessionRetrieved hash]
+ -[SUIBSessionRetrieved initWithBuilder:]
+ -[SUIBSessionRetrieved initWithCoder:]
+ -[SUIBSessionRetrieved isEqual:]
+ -[SUIBSessionRetrieved outcome]
+ -[SUIBSessionRetrieved retrievedPayload]
+ -[SUIBSessionRetrievedMutation .cxx_destruct]
+ -[SUIBSessionRetrievedMutation init]
+ -[SUIBSessionRetrievedMutation outcome]
+ -[SUIBSessionRetrievedMutation retrievedPayload]
+ -[SUIBSessionRetrievedMutation setOutcome:]
+ -[SUIBSessionRetrievedMutation setRetrievedPayload:]
+ -[SUIBSessionRetrievedPayload .cxx_destruct]
+ -[SUIBSessionRetrievedPayload description]
+ -[SUIBSessionRetrievedPayload encodeWithCoder:]
+ -[SUIBSessionRetrievedPayload errorDescription]
+ -[SUIBSessionRetrievedPayload hash]
+ -[SUIBSessionRetrievedPayload initWithBuilder:]
+ -[SUIBSessionRetrievedPayload initWithCoder:]
+ -[SUIBSessionRetrievedPayload isEqual:]
+ -[SUIBSessionRetrievedPayload messages]
+ -[SUIBSessionRetrievedPayload outcome]
+ -[SUIBSessionRetrievedPayload sessionId]
+ -[SUIBSessionRetrievedPayloadMutation .cxx_destruct]
+ -[SUIBSessionRetrievedPayloadMutation errorDescription]
+ -[SUIBSessionRetrievedPayloadMutation init]
+ -[SUIBSessionRetrievedPayloadMutation messages]
+ -[SUIBSessionRetrievedPayloadMutation outcome]
+ -[SUIBSessionRetrievedPayloadMutation sessionId]
+ -[SUIBSessionRetrievedPayloadMutation setErrorDescription:]
+ -[SUIBSessionRetrievedPayloadMutation setMessages:]
+ -[SUIBSessionRetrievedPayloadMutation setOutcome:]
+ -[SUIBSessionRetrievedPayloadMutation setSessionId:]
+ -[SUIBSystemTurnInterruptionEndedContext .cxx_destruct]
+ -[SUIBSystemTurnInterruptionEndedContext copyWithZone:]
+ -[SUIBSystemTurnInterruptionEndedContext description]
+ -[SUIBSystemTurnInterruptionEndedContext encodeWithCoder:]
+ -[SUIBSystemTurnInterruptionEndedContext hash]
+ -[SUIBSystemTurnInterruptionEndedContext initWithBuilder:]
+ -[SUIBSystemTurnInterruptionEndedContext initWithCoder:]
+ -[SUIBSystemTurnInterruptionEndedContext init]
+ -[SUIBSystemTurnInterruptionEndedContext isEqual:]
+ -[SUIBSystemTurnInterruptionEndedContext mitigationResultToString:]
+ -[SUIBSystemTurnInterruptionEndedContext mitigationResult]
+ -[SUIBSystemTurnInterruptionEndedContext userTurnID]
+ -[SUIBSystemTurnInterruptionEndedContextMutation .cxx_destruct]
+ -[SUIBSystemTurnInterruptionEndedContextMutation mitigationResult]
+ -[SUIBSystemTurnInterruptionEndedContextMutation setMitigationResult:]
+ -[SUIBSystemTurnInterruptionEndedContextMutation setUserTurnID:]
+ -[SUIBSystemTurnInterruptionEndedContextMutation userTurnID]
+ -[SUIBSystemTurnInterruptionStartedContext .cxx_destruct]
+ -[SUIBSystemTurnInterruptionStartedContext copyWithZone:]
+ -[SUIBSystemTurnInterruptionStartedContext description]
+ -[SUIBSystemTurnInterruptionStartedContext encodeWithCoder:]
+ -[SUIBSystemTurnInterruptionStartedContext hash]
+ -[SUIBSystemTurnInterruptionStartedContext initWithBuilder:]
+ -[SUIBSystemTurnInterruptionStartedContext initWithCoder:]
+ -[SUIBSystemTurnInterruptionStartedContext init]
+ -[SUIBSystemTurnInterruptionStartedContext isEqual:]
+ -[SUIBSystemTurnInterruptionStartedContext userTurnID]
+ -[SUIBSystemTurnInterruptionStartedContextMutation .cxx_destruct]
+ -[SUIBSystemTurnInterruptionStartedContextMutation setUserTurnID:]
+ -[SUIBSystemTurnInterruptionStartedContextMutation userTurnID]
+ -[SUIBUserSpeechPresence .cxx_destruct]
+ -[SUIBUserSpeechPresence copyWithZone:]
+ -[SUIBUserSpeechPresence encodeWithCoder:]
+ -[SUIBUserSpeechPresence hash]
+ -[SUIBUserSpeechPresence initWithCoder:]
+ -[SUIBUserSpeechPresence init]
+ -[SUIBUserSpeechPresence isEqual:]
+ -[SUIBUserSpeechPresence isInvocationUser]
+ -[SUIBUserSpeechPresence isSameUser]
+ -[SUIBUserSpeechPresence setIsInvocationUser:]
+ -[SUIBUserSpeechPresence setIsSameUser:]
+ -[SUIBUserSpeechPresence setUserTurnID:]
+ -[SUIBUserSpeechPresence userTurnID]
+ -[SUIBUserTurnEndedContext .cxx_destruct]
+ -[SUIBUserTurnEndedContext copyWithZone:]
+ -[SUIBUserTurnEndedContext description]
+ -[SUIBUserTurnEndedContext encodeWithCoder:]
+ -[SUIBUserTurnEndedContext hash]
+ -[SUIBUserTurnEndedContext initWithCoder:]
+ -[SUIBUserTurnEndedContext init]
+ -[SUIBUserTurnEndedContext isEqual:]
+ -[SUIBUserTurnEndedContext mitigationResultToString:]
+ -[SUIBUserTurnEndedContext mitigationResult]
+ -[SUIBUserTurnEndedContext setMitigationResult:]
+ -[SUIBUserTurnEndedContext setUserTurnID:]
+ -[SUIBUserTurnEndedContext userTurnID]
+ -[SUIBUserTurnFinalizedContext .cxx_destruct]
+ -[SUIBUserTurnFinalizedContext copyWithZone:]
+ -[SUIBUserTurnFinalizedContext decisionToString:]
+ -[SUIBUserTurnFinalizedContext decision]
+ -[SUIBUserTurnFinalizedContext description]
+ -[SUIBUserTurnFinalizedContext encodeWithCoder:]
+ -[SUIBUserTurnFinalizedContext hash]
+ -[SUIBUserTurnFinalizedContext initWithCoder:]
+ -[SUIBUserTurnFinalizedContext init]
+ -[SUIBUserTurnFinalizedContext isEqual:]
+ -[SUIBUserTurnFinalizedContext setDecision:]
+ -[SUIBUserTurnFinalizedContext setUserTurnID:]
+ -[SUIBUserTurnFinalizedContext userTurnID]
+ _NSStringFromClass
+ _OBJC_CLASS_$_SUIBSessionRetrieved
+ _OBJC_CLASS_$_SUIBSessionRetrievedMutation
+ _OBJC_CLASS_$_SUIBSessionRetrievedPayload
+ _OBJC_CLASS_$_SUIBSessionRetrievedPayloadMutation
+ _OBJC_CLASS_$_SUIBSystemTurnInterruptionEndedContext
+ _OBJC_CLASS_$_SUIBSystemTurnInterruptionEndedContextMutation
+ _OBJC_CLASS_$_SUIBSystemTurnInterruptionStartedContext
+ _OBJC_CLASS_$_SUIBSystemTurnInterruptionStartedContextMutation
+ _OBJC_CLASS_$_SUIBUserSpeechPresence
+ _OBJC_CLASS_$_SUIBUserTurnEndedContext
+ _OBJC_CLASS_$_SUIBUserTurnFinalizedContext
+ _OBJC_CLASS_$__TtC12SiriUIBridge18UIBridgeServiceSRD
+ _OBJC_IVAR_$_SUIBSessionRetrieved._outcome
+ _OBJC_IVAR_$_SUIBSessionRetrieved._retrievedPayload
+ _OBJC_IVAR_$_SUIBSessionRetrievedMutation._outcome
+ _OBJC_IVAR_$_SUIBSessionRetrievedMutation._retrievedPayload
+ _OBJC_IVAR_$_SUIBSessionRetrievedPayload._errorDescription
+ _OBJC_IVAR_$_SUIBSessionRetrievedPayload._messages
+ _OBJC_IVAR_$_SUIBSessionRetrievedPayload._outcome
+ _OBJC_IVAR_$_SUIBSessionRetrievedPayload._sessionId
+ _OBJC_IVAR_$_SUIBSessionRetrievedPayloadMutation._errorDescription
+ _OBJC_IVAR_$_SUIBSessionRetrievedPayloadMutation._messages
+ _OBJC_IVAR_$_SUIBSessionRetrievedPayloadMutation._outcome
+ _OBJC_IVAR_$_SUIBSessionRetrievedPayloadMutation._sessionId
+ _OBJC_IVAR_$_SUIBSystemTurnInterruptionEndedContext._mitigationResult
+ _OBJC_IVAR_$_SUIBSystemTurnInterruptionEndedContext._userTurnID
+ _OBJC_IVAR_$_SUIBSystemTurnInterruptionEndedContextMutation._mitigationResult
+ _OBJC_IVAR_$_SUIBSystemTurnInterruptionEndedContextMutation._userTurnID
+ _OBJC_IVAR_$_SUIBSystemTurnInterruptionStartedContext._userTurnID
+ _OBJC_IVAR_$_SUIBSystemTurnInterruptionStartedContextMutation._userTurnID
+ _OBJC_IVAR_$_SUIBUserSpeechPresence._isInvocationUser
+ _OBJC_IVAR_$_SUIBUserSpeechPresence._isSameUser
+ _OBJC_IVAR_$_SUIBUserSpeechPresence._userTurnID
+ _OBJC_IVAR_$_SUIBUserTurnEndedContext._mitigationResult
+ _OBJC_IVAR_$_SUIBUserTurnEndedContext._userTurnID
+ _OBJC_IVAR_$_SUIBUserTurnFinalizedContext._decision
+ _OBJC_IVAR_$_SUIBUserTurnFinalizedContext._userTurnID
+ _OBJC_METACLASS_$_SUIBSessionRetrieved
+ _OBJC_METACLASS_$_SUIBSessionRetrievedMutation
+ _OBJC_METACLASS_$_SUIBSessionRetrievedPayload
+ _OBJC_METACLASS_$_SUIBSessionRetrievedPayloadMutation
+ _OBJC_METACLASS_$_SUIBSystemTurnInterruptionEndedContext
+ _OBJC_METACLASS_$_SUIBSystemTurnInterruptionEndedContextMutation
+ _OBJC_METACLASS_$_SUIBSystemTurnInterruptionStartedContext
+ _OBJC_METACLASS_$_SUIBSystemTurnInterruptionStartedContextMutation
+ _OBJC_METACLASS_$_SUIBUserSpeechPresence
+ _OBJC_METACLASS_$_SUIBUserTurnEndedContext
+ _OBJC_METACLASS_$_SUIBUserTurnFinalizedContext
+ _OBJC_METACLASS_$__TtC12SiriUIBridge18UIBridgeServiceSRD
+ _OUTLINED_FUNCTION_100
+ _OUTLINED_FUNCTION_101
+ _OUTLINED_FUNCTION_102
+ _OUTLINED_FUNCTION_103
+ _OUTLINED_FUNCTION_104
+ _OUTLINED_FUNCTION_105
+ _OUTLINED_FUNCTION_106
+ _OUTLINED_FUNCTION_107
+ _OUTLINED_FUNCTION_108
+ _OUTLINED_FUNCTION_109
+ _OUTLINED_FUNCTION_110
+ _OUTLINED_FUNCTION_111
+ _OUTLINED_FUNCTION_112
+ _OUTLINED_FUNCTION_113
+ _OUTLINED_FUNCTION_114
+ _OUTLINED_FUNCTION_115
+ _OUTLINED_FUNCTION_116
+ _OUTLINED_FUNCTION_117
+ _OUTLINED_FUNCTION_118
+ _OUTLINED_FUNCTION_119
+ _OUTLINED_FUNCTION_120
+ _OUTLINED_FUNCTION_121
+ _OUTLINED_FUNCTION_122
+ _OUTLINED_FUNCTION_123
+ _OUTLINED_FUNCTION_124
+ _OUTLINED_FUNCTION_125
+ _OUTLINED_FUNCTION_126
+ _OUTLINED_FUNCTION_127
+ _OUTLINED_FUNCTION_128
+ _OUTLINED_FUNCTION_129
+ _OUTLINED_FUNCTION_130
+ _OUTLINED_FUNCTION_131
+ _OUTLINED_FUNCTION_132
+ _OUTLINED_FUNCTION_133
+ _OUTLINED_FUNCTION_134
+ _OUTLINED_FUNCTION_135
+ _OUTLINED_FUNCTION_136
+ _OUTLINED_FUNCTION_137
+ _OUTLINED_FUNCTION_138
+ _OUTLINED_FUNCTION_139
+ _OUTLINED_FUNCTION_140
+ _OUTLINED_FUNCTION_141
+ _OUTLINED_FUNCTION_53
+ _OUTLINED_FUNCTION_54
+ _OUTLINED_FUNCTION_55
+ _OUTLINED_FUNCTION_56
+ _OUTLINED_FUNCTION_57
+ _OUTLINED_FUNCTION_58
+ _OUTLINED_FUNCTION_59
+ _OUTLINED_FUNCTION_60
+ _OUTLINED_FUNCTION_61
+ _OUTLINED_FUNCTION_62
+ _OUTLINED_FUNCTION_63
+ _OUTLINED_FUNCTION_64
+ _OUTLINED_FUNCTION_65
+ _OUTLINED_FUNCTION_66
+ _OUTLINED_FUNCTION_67
+ _OUTLINED_FUNCTION_68
+ _OUTLINED_FUNCTION_69
+ _OUTLINED_FUNCTION_70
+ _OUTLINED_FUNCTION_71
+ _OUTLINED_FUNCTION_72
+ _OUTLINED_FUNCTION_73
+ _OUTLINED_FUNCTION_74
+ _OUTLINED_FUNCTION_75
+ _OUTLINED_FUNCTION_76
+ _OUTLINED_FUNCTION_77
+ _OUTLINED_FUNCTION_78
+ _OUTLINED_FUNCTION_79
+ _OUTLINED_FUNCTION_80
+ _OUTLINED_FUNCTION_81
+ _OUTLINED_FUNCTION_82
+ _OUTLINED_FUNCTION_83
+ _OUTLINED_FUNCTION_84
+ _OUTLINED_FUNCTION_85
+ _OUTLINED_FUNCTION_86
+ _OUTLINED_FUNCTION_87
+ _OUTLINED_FUNCTION_88
+ _OUTLINED_FUNCTION_89
+ _OUTLINED_FUNCTION_90
+ _OUTLINED_FUNCTION_91
+ _OUTLINED_FUNCTION_92
+ _OUTLINED_FUNCTION_93
+ _OUTLINED_FUNCTION_94
+ _OUTLINED_FUNCTION_95
+ _OUTLINED_FUNCTION_96
+ _OUTLINED_FUNCTION_97
+ _OUTLINED_FUNCTION_98
+ _OUTLINED_FUNCTION_99
+ __DATA__TtC12SiriUIBridge18UIBridgeServiceSRD
+ __DATA__TtC12SiriUIBridge24ProgressUpdateTranslator
+ __INSTANCE_METHODS__TtC12SiriUIBridge18UIBridgeServiceSRD
+ __IVARS__TtC12SiriUIBridge18UIBridgeServiceSRD
+ __METACLASS_DATA__TtC12SiriUIBridge18UIBridgeServiceSRD
+ __METACLASS_DATA__TtC12SiriUIBridge24ProgressUpdateTranslator
+ __OBJC_$_CLASS_METHODS_SUIBSessionRetrieved
+ __OBJC_$_CLASS_METHODS_SUIBSessionRetrievedPayload
+ __OBJC_$_CLASS_METHODS_SUIBSystemTurnInterruptionEndedContext
+ __OBJC_$_CLASS_METHODS_SUIBSystemTurnInterruptionStartedContext
+ __OBJC_$_CLASS_METHODS_SUIBUserSpeechPresence
+ __OBJC_$_CLASS_METHODS_SUIBUserTurnEndedContext
+ __OBJC_$_CLASS_METHODS_SUIBUserTurnFinalizedContext
+ __OBJC_$_CLASS_PROP_LIST_SUIBSessionRetrieved
+ __OBJC_$_CLASS_PROP_LIST_SUIBSessionRetrievedPayload
+ __OBJC_$_CLASS_PROP_LIST_SUIBSystemTurnInterruptionEndedContext
+ __OBJC_$_CLASS_PROP_LIST_SUIBSystemTurnInterruptionStartedContext
+ __OBJC_$_CLASS_PROP_LIST_SUIBUserSpeechPresence
+ __OBJC_$_CLASS_PROP_LIST_SUIBUserTurnEndedContext
+ __OBJC_$_CLASS_PROP_LIST_SUIBUserTurnFinalizedContext
+ __OBJC_$_INSTANCE_METHODS_SUIBSessionRetrieved
+ __OBJC_$_INSTANCE_METHODS_SUIBSessionRetrievedMutation
+ __OBJC_$_INSTANCE_METHODS_SUIBSessionRetrievedPayload
+ __OBJC_$_INSTANCE_METHODS_SUIBSessionRetrievedPayloadMutation
+ __OBJC_$_INSTANCE_METHODS_SUIBSystemTurnInterruptionEndedContext
+ __OBJC_$_INSTANCE_METHODS_SUIBSystemTurnInterruptionEndedContextMutation
+ __OBJC_$_INSTANCE_METHODS_SUIBSystemTurnInterruptionStartedContext
+ __OBJC_$_INSTANCE_METHODS_SUIBSystemTurnInterruptionStartedContextMutation
+ __OBJC_$_INSTANCE_METHODS_SUIBUserSpeechPresence
+ __OBJC_$_INSTANCE_METHODS_SUIBUserTurnEndedContext
+ __OBJC_$_INSTANCE_METHODS_SUIBUserTurnFinalizedContext
+ __OBJC_$_INSTANCE_VARIABLES_SUIBSessionRetrieved
+ __OBJC_$_INSTANCE_VARIABLES_SUIBSessionRetrievedMutation
+ __OBJC_$_INSTANCE_VARIABLES_SUIBSessionRetrievedPayload
+ __OBJC_$_INSTANCE_VARIABLES_SUIBSessionRetrievedPayloadMutation
+ __OBJC_$_INSTANCE_VARIABLES_SUIBSystemTurnInterruptionEndedContext
+ __OBJC_$_INSTANCE_VARIABLES_SUIBSystemTurnInterruptionEndedContextMutation
+ __OBJC_$_INSTANCE_VARIABLES_SUIBSystemTurnInterruptionStartedContext
+ __OBJC_$_INSTANCE_VARIABLES_SUIBSystemTurnInterruptionStartedContextMutation
+ __OBJC_$_INSTANCE_VARIABLES_SUIBUserSpeechPresence
+ __OBJC_$_INSTANCE_VARIABLES_SUIBUserTurnEndedContext
+ __OBJC_$_INSTANCE_VARIABLES_SUIBUserTurnFinalizedContext
+ __OBJC_$_PROP_LIST_SUIBSessionRetrieved
+ __OBJC_$_PROP_LIST_SUIBSessionRetrievedMutation
+ __OBJC_$_PROP_LIST_SUIBSessionRetrievedPayload
+ __OBJC_$_PROP_LIST_SUIBSessionRetrievedPayloadMutation
+ __OBJC_$_PROP_LIST_SUIBSystemTurnInterruptionEndedContext
+ __OBJC_$_PROP_LIST_SUIBSystemTurnInterruptionEndedContextMutation
+ __OBJC_$_PROP_LIST_SUIBSystemTurnInterruptionStartedContext
+ __OBJC_$_PROP_LIST_SUIBSystemTurnInterruptionStartedContextMutation
+ __OBJC_$_PROP_LIST_SUIBUserSpeechPresence
+ __OBJC_$_PROP_LIST_SUIBUserTurnEndedContext
+ __OBJC_$_PROP_LIST_SUIBUserTurnFinalizedContext
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
+ __OBJC_CLASS_PROTOCOLS_$_SUIBSessionRetrieved
+ __OBJC_CLASS_PROTOCOLS_$_SUIBSessionRetrievedPayload
+ __OBJC_CLASS_PROTOCOLS_$_SUIBSystemTurnInterruptionEndedContext
+ __OBJC_CLASS_PROTOCOLS_$_SUIBSystemTurnInterruptionStartedContext
+ __OBJC_CLASS_PROTOCOLS_$_SUIBUserSpeechPresence
+ __OBJC_CLASS_PROTOCOLS_$_SUIBUserTurnEndedContext
+ __OBJC_CLASS_PROTOCOLS_$_SUIBUserTurnFinalizedContext
+ __OBJC_CLASS_RO_$_SUIBSessionRetrieved
+ __OBJC_CLASS_RO_$_SUIBSessionRetrievedMutation
+ __OBJC_CLASS_RO_$_SUIBSessionRetrievedPayload
+ __OBJC_CLASS_RO_$_SUIBSessionRetrievedPayloadMutation
+ __OBJC_CLASS_RO_$_SUIBSystemTurnInterruptionEndedContext
+ __OBJC_CLASS_RO_$_SUIBSystemTurnInterruptionEndedContextMutation
+ __OBJC_CLASS_RO_$_SUIBSystemTurnInterruptionStartedContext
+ __OBJC_CLASS_RO_$_SUIBSystemTurnInterruptionStartedContextMutation
+ __OBJC_CLASS_RO_$_SUIBUserSpeechPresence
+ __OBJC_CLASS_RO_$_SUIBUserTurnEndedContext
+ __OBJC_CLASS_RO_$_SUIBUserTurnFinalizedContext
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_METACLASS_RO_$_SUIBSessionRetrieved
+ __OBJC_METACLASS_RO_$_SUIBSessionRetrievedMutation
+ __OBJC_METACLASS_RO_$_SUIBSessionRetrievedPayload
+ __OBJC_METACLASS_RO_$_SUIBSessionRetrievedPayloadMutation
+ __OBJC_METACLASS_RO_$_SUIBSystemTurnInterruptionEndedContext
+ __OBJC_METACLASS_RO_$_SUIBSystemTurnInterruptionEndedContextMutation
+ __OBJC_METACLASS_RO_$_SUIBSystemTurnInterruptionStartedContext
+ __OBJC_METACLASS_RO_$_SUIBSystemTurnInterruptionStartedContextMutation
+ __OBJC_METACLASS_RO_$_SUIBUserSpeechPresence
+ __OBJC_METACLASS_RO_$_SUIBUserTurnEndedContext
+ __OBJC_METACLASS_RO_$_SUIBUserTurnFinalizedContext
+ __OBJC_PROTOCOL_$_NSCopying
+ __PROTOCOLS__TtC12SiriUIBridge18UIBridgeServiceSRD
+ __PROTOCOLS__TtC12SiriUIBridge18UIBridgeServiceSRD.68
+ __PROTOCOLS__TtC12SiriUIBridge26UIBridgeConnectionListener.12
+ __PROTOCOL_INSTANCE_METHODS_OPT__TtP12SiriUIBridge38UIBridgeServiceDelegateWrapperProtocol_
+ __PROTOCOL_INSTANCE_METHODS__TtP12SiriUIBridge38UIBridgeServiceDelegateWrapperProtocol_
+ __PROTOCOL_METHOD_TYPES__TtP12SiriUIBridge38UIBridgeServiceDelegateWrapperProtocol_
+ ___46-[SUIBSystemTurnInterruptionEndedContext init]_block_invoke
+ ___48-[SUIBSystemTurnInterruptionStartedContext init]_block_invoke
+ ___56-[SUIBSystemTurnInterruptionEndedContext initWithCoder:]_block_invoke
+ ___58-[SUIBSystemTurnInterruptionStartedContext initWithCoder:]_block_invoke
+ ___NSArray0__struct
+ ___block_descriptor_32_e56_v16?0"SUIBSystemTurnInterruptionEndedContextMutation"8l
+ ___block_descriptor_32_e58_v16?0"SUIBSystemTurnInterruptionStartedContextMutation"8l
+ ___block_descriptor_40_e8_32s_e58_v16?0"SUIBSystemTurnInterruptionStartedContextMutation"8ls32l8
+ ___block_descriptor_48_e8_32s_e56_v16?0"SUIBSystemTurnInterruptionEndedContextMutation"8ls32l8
+ ___swift_memcpy0_1
+ ___swift_noop_void_return
+ _block_copy_helper.105
+ _block_copy_helper.111
+ _block_copy_helper.117
+ _block_copy_helper.123
+ _block_copy_helper.128
+ _block_copy_helper.129
+ _block_copy_helper.135
+ _block_copy_helper.139
+ _block_copy_helper.141
+ _block_copy_helper.147
+ _block_copy_helper.150
+ _block_copy_helper.153
+ _block_copy_helper.159
+ _block_copy_helper.161
+ _block_copy_helper.165
+ _block_copy_helper.171
+ _block_copy_helper.177
+ _block_copy_helper.180
+ _block_copy_helper.183
+ _block_copy_helper.189
+ _block_copy_helper.191
+ _block_copy_helper.195
+ _block_copy_helper.201
+ _block_copy_helper.210
+ _block_copy_helper.218
+ _block_copy_helper.37
+ _block_copy_helper.38
+ _block_copy_helper.43
+ _block_copy_helper.49
+ _block_copy_helper.61
+ _block_copy_helper.79
+ _block_copy_helper.8
+ _block_copy_helper.81
+ _block_copy_helper.93
+ _block_copy_helper.98
+ _block_copy_helper.99
+ _block_descriptor.10
+ _block_descriptor.100
+ _block_descriptor.101
+ _block_descriptor.107
+ _block_descriptor.113
+ _block_descriptor.119
+ _block_descriptor.125
+ _block_descriptor.130
+ _block_descriptor.131
+ _block_descriptor.137
+ _block_descriptor.141
+ _block_descriptor.143
+ _block_descriptor.149
+ _block_descriptor.152
+ _block_descriptor.155
+ _block_descriptor.161
+ _block_descriptor.163
+ _block_descriptor.167
+ _block_descriptor.173
+ _block_descriptor.179
+ _block_descriptor.182
+ _block_descriptor.185
+ _block_descriptor.191
+ _block_descriptor.193
+ _block_descriptor.197
+ _block_descriptor.203
+ _block_descriptor.212
+ _block_descriptor.220
+ _block_descriptor.39
+ _block_descriptor.40
+ _block_descriptor.45
+ _block_descriptor.51
+ _block_descriptor.63
+ _block_descriptor.81
+ _block_descriptor.83
+ _block_descriptor.95
+ _block_destroy_helper.100
+ _block_destroy_helper.106
+ _block_destroy_helper.112
+ _block_destroy_helper.118
+ _block_destroy_helper.124
+ _block_destroy_helper.129
+ _block_destroy_helper.130
+ _block_destroy_helper.136
+ _block_destroy_helper.140
+ _block_destroy_helper.142
+ _block_destroy_helper.148
+ _block_destroy_helper.151
+ _block_destroy_helper.154
+ _block_destroy_helper.160
+ _block_destroy_helper.162
+ _block_destroy_helper.166
+ _block_destroy_helper.172
+ _block_destroy_helper.178
+ _block_destroy_helper.181
+ _block_destroy_helper.184
+ _block_destroy_helper.190
+ _block_destroy_helper.192
+ _block_destroy_helper.196
+ _block_destroy_helper.202
+ _block_destroy_helper.211
+ _block_destroy_helper.219
+ _block_destroy_helper.38
+ _block_destroy_helper.39
+ _block_destroy_helper.44
+ _block_destroy_helper.50
+ _block_destroy_helper.62
+ _block_destroy_helper.80
+ _block_destroy_helper.82
+ _block_destroy_helper.9
+ _block_destroy_helper.94
+ _block_destroy_helper.99
+ _free
+ _objc_msgSend$UUIDString
+ _objc_msgSend$_setQueue:
+ _objc_msgSend$allocWithZone:
+ _objc_msgSend$connectionInterrupted
+ _objc_msgSend$connectionInvalidated
+ _objc_msgSend$count
+ _objc_msgSend$decision
+ _objc_msgSend$decisionToString:
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$decodeIntegerForKey:
+ _objc_msgSend$decodeObjectOfClasses:forKey:
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$encodeInteger:forKey:
+ _objc_msgSend$errorDescription
+ _objc_msgSend$extendRequestTimeoutBy:forRequestID:
+ _objc_msgSend$floatForKey:
+ _objc_msgSend$hash
+ _objc_msgSend$init
+ _objc_msgSend$initWithArray:
+ _objc_msgSend$initWithDelegate:
+ _objc_msgSend$initWithDelegate:delegateQueue:
+ _objc_msgSend$initWithMachServiceName:
+ _objc_msgSend$initWithMachServiceName:options:
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$interfaceWithProtocol:
+ _objc_msgSend$invalidate
+ _objc_msgSend$isEqual:
+ _objc_msgSend$isInvocationUser
+ _objc_msgSend$isSameUser
+ _objc_msgSend$messages
+ _objc_msgSend$mitigationResult
+ _objc_msgSend$mitigationResultToString:
+ _objc_msgSend$notifyClientWithBlock:
+ _objc_msgSend$notifySpeechDetectedIsUndirected
+ _objc_msgSend$notifyTypingStartedWith:
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$outcome
+ _objc_msgSend$preheat
+ _objc_msgSend$processIdentifier
+ _objc_msgSend$remoteObjectProxy
+ _objc_msgSend$resume
+ _objc_msgSend$resumeConnectionWithBridgeProxy:
+ _objc_msgSend$retrievedPayload
+ _objc_msgSend$sessionId
+ _objc_msgSend$setClasses:forSelector:argumentIndex:ofReply:
+ _objc_msgSend$setDecision:
+ _objc_msgSend$setDelegate:
+ _objc_msgSend$setExportedInterface:
+ _objc_msgSend$setExportedObject:
+ _objc_msgSend$setInterruptionHandler:
+ _objc_msgSend$setInvalidationHandler:
+ _objc_msgSend$setIsInvocationUser:
+ _objc_msgSend$setIsSameUser:
+ _objc_msgSend$setMitigationResult:
+ _objc_msgSend$setRemoteObjectInterface:
+ _objc_msgSend$setUserTurnID:
+ _objc_msgSend$setWithObjects:
+ _objc_msgSend$siriDismissed
+ _objc_msgSend$siriPrompted
+ _objc_msgSend$siriWillPrompt
+ _objc_msgSend$startAttendingWithReason:deviceId:
+ _objc_msgSend$stopAttendingForReason:
+ _objc_msgSend$uiBridgeServiceDetectedSiriDirectedSpeech
+ _objc_msgSend$uiBridgeServiceDetectedSpeechStart
+ _objc_msgSend$uiBridgeServiceDetectedSpeechStart:
+ _objc_msgSend$uiBridgeServiceDidDetectLanguageMismatch:
+ _objc_msgSend$uiBridgeServiceDidDetectUserSpeechWithContext:
+ _objc_msgSend$uiBridgeServiceDidEndSystemTurnInterruptionWithContext:
+ _objc_msgSend$uiBridgeServiceDidEndUserTurnWithContext:
+ _objc_msgSend$uiBridgeServiceDidFinalizeUserTurnWithContext:
+ _objc_msgSend$uiBridgeServiceDidReceiveTasks:
+ _objc_msgSend$uiBridgeServiceDidStartAttending
+ _objc_msgSend$uiBridgeServiceDidStartAttendingWithRootRequestId:
+ _objc_msgSend$uiBridgeServiceDidStartSystemTurnInterruptionWithContext:
+ _objc_msgSend$uiBridgeServiceDidStopAttendingUnexpectedlyWithReason:
+ _objc_msgSend$uiBridgeServiceReceivedNLRoutingDecision:
+ _objc_msgSend$uiBridgeServiceReceivedRequestProgress:
+ _objc_msgSend$uiBridgeServiceReceivedSessionRetrieved:
+ _objc_msgSend$uiBridgeServiceReceivedShowAssetsDownloadPrompt
+ _objc_msgSend$uiBridgeServiceReceivedSiriResponse:
+ _objc_msgSend$uiBridgeServiceReceivedSpeechMitigationResult:
+ _objc_msgSend$uiBridgeServiceTaskDidCancel:
+ _objc_msgSend$uiBridgeServiceTaskDidEnd:
+ _objc_msgSend$uiBridgeServiceWillStartAttending
+ _objc_msgSend$userTurnID
+ _objc_msgSend$valueForEntitlement:
+ _objc_opt_isKindOfClass
+ _objc_retain_x27
+ _objectdestroy.43Tm
+ _swift_coroFrameAlloc
+ _swift_endAccess
+ _symbolic So20SUIBSessionRetrievedC
+ _symbolic So20SUIBSessionRetrievedCm
+ _symbolic So22SUIBUserSpeechPresenceC
+ _symbolic So22SUIBUserSpeechPresenceCm
+ _symbolic So24SUIBUserTurnEndedContextC
+ _symbolic So24SUIBUserTurnEndedContextCm
+ _symbolic So27SUIBSessionRetrievedPayloadCm
+ _symbolic So28SUIBUserTurnFinalizedContextC
+ _symbolic So28SUIBUserTurnFinalizedContextCm
+ _symbolic So38SUIBSystemTurnInterruptionEndedContextC
+ _symbolic So38SUIBSystemTurnInterruptionEndedContextCm
+ _symbolic So40SUIBSystemTurnInterruptionStartedContextC
+ _symbolic So40SUIBSystemTurnInterruptionStartedContextCm
+ _symbolic _____ 12SiriUIBridge0B10ServiceSRDC
+ _symbolic _____ 12SiriUIBridge24ProgressUpdateTranslatorC
+ _symbolic _____ 12SiriUIBridge6LoggerO
+ _symbolic _____SgXw 12SiriUIBridge0B10ServiceSRDC
+ _symbolic _____SgXwz_Xx 12SiriUIBridge0B10ServiceSRDC
+ _symbolic _____Xo 12SiriUIBridge0B10ServiceSRDC
+ _symbolic ______pSgXw 12SiriUIBridge0B30ServiceDelegateWrapperProtocolP
+ _symbolic ______pSgXw So27SUIBUIBridgeServiceProtocolP
- _OBJC_CLASS_$__TtC12SiriUIBridge15UIBridgeService
- _OBJC_METACLASS_$__TtC12SiriUIBridge15UIBridgeService
- __DATA__TtC12SiriUIBridge15UIBridgeService
- __INSTANCE_METHODS__TtC12SiriUIBridge15UIBridgeService
- __IVARS__TtC12SiriUIBridge15UIBridgeService
- __METACLASS_DATA__TtC12SiriUIBridge15UIBridgeService
- __PROTOCOLS__TtC12SiriUIBridge15UIBridgeService
- __PROTOCOLS__TtC12SiriUIBridge15UIBridgeService.32
- __PROTOCOLS__TtC12SiriUIBridge26UIBridgeConnectionListener.2
- __swift_FORCE_LOAD_$_swiftAVFoundation
- __swift_FORCE_LOAD_$_swiftAVFoundation_$_SiriUIBridge
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_SiriUIBridge
- _block_copy_helper.103
- _block_copy_helper.109
- _block_copy_helper.114
- _block_copy_helper.115
- _block_copy_helper.125
- _block_copy_helper.136
- _block_copy_helper.142
- _block_copy_helper.144
- _block_copy_helper.148
- _block_copy_helper.152
- _block_copy_helper.154
- _block_copy_helper.160
- _block_copy_helper.166
- _block_copy_helper.178
- _block_copy_helper.184
- _block_copy_helper.190
- _block_copy_helper.196
- _block_copy_helper.244
- _block_copy_helper.25
- _block_copy_helper.91
- _block_copy_helper.95
- _block_descriptor.105
- _block_descriptor.111
- _block_descriptor.116
- _block_descriptor.117
- _block_descriptor.127
- _block_descriptor.138
- _block_descriptor.144
- _block_descriptor.146
- _block_descriptor.150
- _block_descriptor.154
- _block_descriptor.156
- _block_descriptor.162
- _block_descriptor.168
- _block_descriptor.180
- _block_descriptor.186
- _block_descriptor.192
- _block_descriptor.198
- _block_descriptor.246
- _block_descriptor.27
- _block_descriptor.93
- _block_descriptor.97
- _block_destroy_helper.104
- _block_destroy_helper.110
- _block_destroy_helper.115
- _block_destroy_helper.116
- _block_destroy_helper.126
- _block_destroy_helper.137
- _block_destroy_helper.143
- _block_destroy_helper.145
- _block_destroy_helper.149
- _block_destroy_helper.153
- _block_destroy_helper.155
- _block_destroy_helper.161
- _block_destroy_helper.167
- _block_destroy_helper.179
- _block_destroy_helper.185
- _block_destroy_helper.191
- _block_destroy_helper.197
- _block_destroy_helper.245
- _block_destroy_helper.26
- _block_destroy_helper.92
- _block_destroy_helper.96
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x28
- _objectdestroy.32Tm
- _symbolic _____ 12SiriUIBridge0B7ServiceC
- _symbolic _____SgXw 12SiriUIBridge0B7ServiceC
- _symbolic _____SgXwz_Xx 12SiriUIBridge0B7ServiceC
- _symbolic _____Xo 12SiriUIBridge0B7ServiceC
CStrings:
+ "<%@: %p, outcome=%lu, payloads=%lu>"
+ "<%@: %p, sessionId=%@, outcome=%lu, messages=%lu, errorDescription=%@>"
+ "<%@: %p; userTurnID=%@; decision=%@>"
+ "<%@: %p; userTurnID=%@; mitigationResult=%@>"
+ "<%@: %p; userTurnID=%@>"
+ "@\"NSArray\""
+ "@24@0:8Q16"
+ "@24@0:8^{_NSZone=}16"
+ "AFUIBAttendingStopReasonToSMTAttendingStopReason(reason:)"
+ "B"
+ "Invalid"
+ "MaybeMitigated"
+ "Mitigated"
+ "NSCopying"
+ "SUIBAttendingStartReasonToSMTAttendingStartReason(reason:)"
+ "SUIBAttendingStopReasonToSMTAttendingStopReason(reason:)"
+ "SUIBSessionRetrieved"
+ "SUIBSessionRetrievedMutation"
+ "SUIBSessionRetrievedPayload"
+ "SUIBSessionRetrievedPayloadMutation"
+ "SUIBSystemTurnInterruptionEndedContext"
+ "SUIBSystemTurnInterruptionEndedContextMutation"
+ "SUIBSystemTurnInterruptionStartedContext"
+ "SUIBSystemTurnInterruptionStartedContextMutation"
+ "SUIBUserSpeechPresence"
+ "SUIBUserTurnEndedContext"
+ "SUIBUserTurnFinalizedContext"
+ "Selected"
+ "SessionHandler not found in UIBridgeServiceSRD"
+ "SiriUIBridge.UIBridgeServiceSRD"
+ "T@\"NSArray\",C,N,V_messages"
+ "T@\"NSArray\",C,N,V_retrievedPayload"
+ "T@\"NSArray\",R,C,N,V_messages"
+ "T@\"NSArray\",R,C,N,V_retrievedPayload"
+ "T@\"NSString\",C,N,V_errorDescription"
+ "T@\"NSString\",C,N,V_sessionId"
+ "T@\"NSString\",R,C,N,V_errorDescription"
+ "T@\"NSString\",R,C,N,V_sessionId"
+ "T@\"NSUUID\",C,N,V_userTurnID"
+ "T@\"NSUUID\",R,C,N,V_userTurnID"
+ "TB,N,V_isInvocationUser"
+ "TB,N,V_isSameUser"
+ "TQ,N,V_decision"
+ "TQ,N,V_mitigationResult"
+ "TQ,N,V_outcome"
+ "TQ,R,N,V_mitigationResult"
+ "TQ,R,N,V_outcome"
+ "UIBridgeServiceSRD expired"
+ "UUIDString"
+ "Unknown"
+ "Vv24@0:8@\"SUIBSessionRetrieved\"16"
+ "Vv24@0:8@\"SUIBSystemTurnInterruptionEndedContext\"16"
+ "Vv24@0:8@\"SUIBSystemTurnInterruptionStartedContext\"16"
+ "Vv24@0:8@\"SUIBUserSpeechPresence\"16"
+ "Vv24@0:8@\"SUIBUserTurnEndedContext\"16"
+ "Vv24@0:8@\"SUIBUserTurnFinalizedContext\"16"
+ "[UIBridgeServiceSRD:%s]"
+ "[UIBridgeServiceSRD] Calling delegate's didReceive with %s"
+ "[UIBridgeServiceSRD] Calling delegate's receivedRequestProgress with %@"
+ "[UIBridgeServiceSRD] Calling delegate's receivedSiriResponse with %@"
+ "[UIBridgeServiceSRD] Calling delegate's uiBridgeServiceReceivedNLRoutingDecision with %s"
+ "[UIBridgeServiceSRD] Received call in preheat()"
+ "[UIBridgeServiceSRD] Received notifyTypingStarted from the UI"
+ "[UIBridgeServiceSRD] Received siriWillPrompt from the UI, this is not expected. Ignoring"
+ "[UIBridgeServiceSRD] Received status update message with status: %s for rootRequestId: %s"
+ "[UIBridgeServiceSRD] UIBridgeListener connection interrupted"
+ "[UIBridgeServiceSRD] UIBridgeListener connection invalidated"
+ "[UIBridgeServiceSRD] startAttending reason=%s device=%s"
+ "[[UIBridgeServiceSRD] Received siriPrompted"
+ "_TtC12SiriUIBridge18UIBridgeServiceSRD"
+ "_TtC12SiriUIBridge24ProgressUpdateTranslator"
+ "_decision"
+ "_errorDescription"
+ "_isInvocationUser"
+ "_isSameUser"
+ "_messages"
+ "_mitigationResult"
+ "_outcome"
+ "_retrievedPayload"
+ "_sessionId"
+ "_userTurnID"
+ "allocWithZone:"
+ "attendingStartedWithRootRequestId(_:)"
+ "attendingStoppedUnexpectedly()"
+ "attendingStoppedUnexpectedly(with:)"
+ "attendingWillStart()"
+ "copyWithZone:"
+ "count"
+ "decision"
+ "decisionToString:"
+ "decodeBoolForKey:"
+ "decodeIntegerForKey:"
+ "decodeObjectOfClasses:forKey:"
+ "encodeBool:forKey:"
+ "encodeInteger:forKey:"
+ "errorDescription"
+ "handleAttendingStartedMessage(_:)"
+ "handleAttendingStoppedUnexpectedlyMessage(_:)"
+ "handleAttendingWillStartMessage(_:)"
+ "handleEndRequest(_:)"
+ "handleFlowOutputMessage(_:)"
+ "handleIntelligenceFlowActionSummaryMessage(_:)"
+ "handleIntelligenceFlowOutputMessage(_:)"
+ "handleIntelligenceFlowStatusUpdateMessage(_:)"
+ "handleMagusAttentionAssetDownloadRequestedMessage(_:)"
+ "handleMitigationDecisionFinalizedMessage(_:)"
+ "handleNLRoutingDecisionMessage(_:)"
+ "handleOrchestrationTaskCompletedMessage(_:)"
+ "handleOrchestrationTasksCreatedMessage(_:)"
+ "handleSessionEndedMessage(_:)"
+ "handleSessionStartedMessage(_:)"
+ "handleSiriWillPromptMessage(_:)"
+ "handleSpeechStartDetectedMessage(_:)"
+ "handleStartRequest(_:)"
+ "handleStartRootSpeechRequestMessage(_:)"
+ "handleUnsupportedLanguageMessage(_:)"
+ "isInvocationUser"
+ "isSameUser"
+ "logUUFRReadyEvent:"
+ "messages"
+ "mitigationResult"
+ "mitigationResultToString:"
+ "numberWithBool:"
+ "outcome"
+ "performCleanupOnAbnormalConnectionTermination()"
+ "receivedFlowOutputMessage(_:)"
+ "receivedIntelligenceFlowActionSummaryMessage(_:)"
+ "receivedIntelligenceFlowOutputMessage(_:)"
+ "receivedNLRoutingDecisionMessage(_:)"
+ "receivedShowAssetsDownloadPrompt()"
+ "receivedSpeechMitigationResult(isMitigated:)"
+ "receivedUnsupportedLanguage(requestLanguage:)"
+ "requestClosed:forRequestID:"
+ "retrievedPayload"
+ "serviceDelegate"
+ "setDecision:"
+ "setErrorDescription:"
+ "setIsInvocationUser:"
+ "setIsSameUser:"
+ "setMessages:"
+ "setMitigationResult:"
+ "setOutcome:"
+ "setRetrievedPayload:"
+ "setSessionId:"
+ "setUserTurnID:"
+ "setWithObjects:"
+ "siriDirectedSpeechDetected()"
+ "speechStartDetected(shouldDuckTTS:)"
+ "startAttending()"
+ "startRequestWith:"
+ "stopAttending(for:)"
+ "stopAttending(with:)"
+ "topicChangedForRequestID:"
+ "uiBridgeServiceDidDetectUserSpeechWithContext:"
+ "uiBridgeServiceDidEndSystemTurnInterruptionWithContext:"
+ "uiBridgeServiceDidEndUserTurnWithContext:"
+ "uiBridgeServiceDidFinalizeUserTurnWithContext:"
+ "uiBridgeServiceDidStartSystemTurnInterruptionWithContext:"
+ "uiBridgeServiceReceivedSessionRetrieved:"
+ "userTurnID"
+ "v16@?0@\"SUIBSystemTurnInterruptionEndedContextMutation\"8"
+ "v16@?0@\"SUIBSystemTurnInterruptionStartedContextMutation\"8"
+ "v24@0:8@\"<AFIntelligenceFlowActionDescriptor>\"16"
+ "v24@0:8@\"NSString\"16"
+ "v24@0:8@\"NSUUID\"16"
+ "v24@0:8@\"SUIBSessionRetrieved\"16"
+ "v24@0:8@\"SUIBSystemTurnInterruptionEndedContext\"16"
+ "v24@0:8@\"SUIBSystemTurnInterruptionStartedContext\"16"
+ "v24@0:8@\"SUIBUserSpeechPresence\"16"
+ "v24@0:8@\"SUIBUserTurnEndedContext\"16"
+ "v24@0:8@\"SUIBUserTurnFinalizedContext\"16"
+ "v28@0:8B16@\"NSString\"20"
+ "v28@0:8B16@20"
- "Calling delegate's didReceive with %s"
- "Calling delegate's receivedRequestProgress with %@"
- "Calling delegate's receivedSiriResponse with %@"
- "Calling delegate's uiBridgeServiceReceivedNLRoutingDecision with %s"
- "Received call in preheat()"
- "Received notifyTypingStarted from the UI"
- "Received siriPrompted"
- "Received siriWillPrompt from the UI, this is not expected. Ignoring"
- "Received status update message with status: %s for rootRequestId: %s"
- "SessionHandler not found in UIBridgeService"
- "SiriUIBridge.UIBridgeService"
- "UIBridgeListener connection interrupted"
- "UIBridgeListener connection invalidated"
- "UIBridgeService expired"
- "_TtC12SiriUIBridge15UIBridgeService"
- "startAttending reason=%s device=%s"

```
