## SiriUIBridge

> `/System/Library/PrivateFrameworks/SiriUIBridge.framework/Versions/A/SiriUIBridge`

```diff

-3403.3.1.0.0
-  __TEXT.__text: 0x18268
-  __TEXT.__auth_stubs: 0xd00
-  __TEXT.__objc_methlist: 0x8bc
-  __TEXT.__const: 0x322
-  __TEXT.__cstring: 0xd0b
-  __TEXT.__constg_swiftt: 0x714
-  __TEXT.__swift5_typeref: 0x63a
+3404.11.1.0.0
+  __TEXT.__text: 0x1ad9c
+  __TEXT.__auth_stubs: 0xd60
+  __TEXT.__objc_methlist: 0x1008
+  __TEXT.__const: 0x342
+  __TEXT.__cstring: 0xb0b
+  __TEXT.__constg_swiftt: 0x724
+  __TEXT.__swift5_typeref: 0x6b0
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_types: 0x2c
   __TEXT.__swift5_fieldmd: 0x1c8
   __TEXT.__swift5_reflstr: 0x1db
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__oslogstring: 0xbb3
-  __TEXT.__swift5_capture: 0x710
-  __TEXT.__unwind_info: 0x728
-  __TEXT.__eh_frame: 0xe8
-  __TEXT.__objc_classname: 0x2e4
-  __TEXT.__objc_methname: 0x16e0
-  __TEXT.__objc_methtype: 0x881
-  __TEXT.__objc_stubs: 0x5c0
-  __DATA_CONST.__got: 0x240
-  __DATA_CONST.__const: 0x1f0
-  __DATA_CONST.__objc_classlist: 0xc0
+  __TEXT.__oslogstring: 0xc73
+  __TEXT.__swift5_capture: 0x734
+  __TEXT.__unwind_info: 0x750
+  __TEXT.__eh_frame: 0x120
+  __TEXT.__objc_classname: 0x374
+  __TEXT.__objc_methname: 0x191d
+  __TEXT.__objc_methtype: 0x8f7
+  __TEXT.__objc_stubs: 0x680
+  __DATA_CONST.__got: 0x268
+  __DATA_CONST.__const: 0x220
+  __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x338
+  __DATA_CONST.__objc_selrefs: 0x578
   __DATA_CONST.__objc_protorefs: 0x50
-  __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x688
-  __AUTH_CONST.__const: 0x1c28
-  __AUTH_CONST.__cfstring: 0x1e0
-  __AUTH_CONST.__objc_const: 0x2868
-  __AUTH.__objc_data: 0xd38
-  __AUTH.__data: 0x310
-  __DATA.__objc_ivar: 0x7c
-  __DATA.__data: 0x728
-  __DATA.__common: 0x78
+  __DATA_CONST.__objc_superrefs: 0x58
+  __AUTH_CONST.__auth_got: 0x6b8
+  __AUTH_CONST.__const: 0x1d68
+  __AUTH_CONST.__cfstring: 0x240
+  __AUTH_CONST.__objc_const: 0x21b0
+  __AUTH.__objc_data: 0xe80
+  __AUTH.__data: 0x328
+  __DATA.__objc_ivar: 0x94
+  __DATA.__data: 0x718
+  __DATA.__common: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/AssistantServices

   - /System/Library/PrivateFrameworks/SiriRequestDispatcher.framework/Versions/A/SiriRequestDispatcher
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 4D30719C-DCD3-3C33-BEFA-98FEBEFDBF24
-  Functions: 996
-  Symbols:   1074
-  CStrings:  492
+  UUID: 57EC335F-4C4D-31D1-BB26-D9224EFB1094
+  Functions: 1055
+  Symbols:   1176
+  CStrings:  512
 
Symbols:
+ +[SUIBIntelligenceFlowStatusNotification supportsSecureCoding]
+ +[SUIBTypingSessionStarted supportsSecureCoding]
+ -[SUIBIntelligenceFlowStatusNotification .cxx_destruct]
+ -[SUIBIntelligenceFlowStatusNotification encodeWithCoder:]
+ -[SUIBIntelligenceFlowStatusNotification initWithBuilder:]
+ -[SUIBIntelligenceFlowStatusNotification initWithCoder:]
+ -[SUIBIntelligenceFlowStatusNotification init]
+ -[SUIBIntelligenceFlowStatusNotification statusString]
+ -[SUIBIntelligenceFlowStatusNotificationMutation .cxx_destruct]
+ -[SUIBIntelligenceFlowStatusNotificationMutation setStatusString:]
+ -[SUIBIntelligenceFlowStatusNotificationMutation statusString]
+ -[SUIBRequestProgress intelligenceFlowStatusNotification]
+ -[SUIBRequestProgressMutation intelligenceFlowStatusNotification]
+ -[SUIBRequestProgressMutation setIntelligenceFlowStatusNotification:]
+ -[SUIBTypingSessionStarted .cxx_destruct]
+ -[SUIBTypingSessionStarted encodeWithCoder:]
+ -[SUIBTypingSessionStarted initWithBuilder:]
+ -[SUIBTypingSessionStarted initWithCoder:]
+ -[SUIBTypingSessionStarted init]
+ -[SUIBTypingSessionStarted typingSessionId]
+ -[SUIBTypingSessionStartedMutation .cxx_destruct]
+ -[SUIBTypingSessionStartedMutation setTypingSessionId:]
+ -[SUIBTypingSessionStartedMutation typingSessionId]
+ OBJC_IVAR_$_SUIBIntelligenceFlowStatusNotification._statusString
+ OBJC_IVAR_$_SUIBIntelligenceFlowStatusNotificationMutation._statusString
+ OBJC_IVAR_$_SUIBRequestProgress._intelligenceFlowStatusNotification
+ OBJC_IVAR_$_SUIBRequestProgressMutation._intelligenceFlowStatusNotification
+ OBJC_IVAR_$_SUIBTypingSessionStarted._typingSessionId
+ OBJC_IVAR_$_SUIBTypingSessionStartedMutation._typingSessionId
+ _OBJC_CLASS_$_SUIBIntelligenceFlowStatusNotification
+ _OBJC_CLASS_$_SUIBIntelligenceFlowStatusNotificationMutation
+ _OBJC_CLASS_$_SUIBTypingSessionStarted
+ _OBJC_CLASS_$_SUIBTypingSessionStartedMutation
+ _OBJC_METACLASS_$_SUIBIntelligenceFlowStatusNotification
+ _OBJC_METACLASS_$_SUIBIntelligenceFlowStatusNotificationMutation
+ _OBJC_METACLASS_$_SUIBTypingSessionStarted
+ _OBJC_METACLASS_$_SUIBTypingSessionStartedMutation
+ _OUTLINED_FUNCTION_56
+ _OUTLINED_FUNCTION_57
+ _OUTLINED_FUNCTION_58
+ _OUTLINED_FUNCTION_59
+ _OUTLINED_FUNCTION_60
+ _OUTLINED_FUNCTION_61
+ _PROTOCOLS__TtC12SiriUIBridge15UIBridgeService.32
+ __OBJC_$_CLASS_METHODS_SUIBIntelligenceFlowStatusNotification
+ __OBJC_$_CLASS_METHODS_SUIBTypingSessionStarted
+ __OBJC_$_CLASS_PROP_LIST_SUIBIntelligenceFlowStatusNotification
+ __OBJC_$_CLASS_PROP_LIST_SUIBTypingSessionStarted
+ __OBJC_$_INSTANCE_METHODS_SUIBIntelligenceFlowStatusNotification
+ __OBJC_$_INSTANCE_METHODS_SUIBIntelligenceFlowStatusNotificationMutation
+ __OBJC_$_INSTANCE_METHODS_SUIBTypingSessionStarted
+ __OBJC_$_INSTANCE_METHODS_SUIBTypingSessionStartedMutation
+ __OBJC_$_INSTANCE_VARIABLES_SUIBIntelligenceFlowStatusNotification
+ __OBJC_$_INSTANCE_VARIABLES_SUIBIntelligenceFlowStatusNotificationMutation
+ __OBJC_$_INSTANCE_VARIABLES_SUIBTypingSessionStarted
+ __OBJC_$_INSTANCE_VARIABLES_SUIBTypingSessionStartedMutation
+ __OBJC_$_PROP_LIST_SUIBIntelligenceFlowStatusNotification
+ __OBJC_$_PROP_LIST_SUIBIntelligenceFlowStatusNotificationMutation
+ __OBJC_$_PROP_LIST_SUIBTypingSessionStarted
+ __OBJC_$_PROP_LIST_SUIBTypingSessionStartedMutation
+ __OBJC_CLASS_PROTOCOLS_$_SUIBIntelligenceFlowStatusNotification
+ __OBJC_CLASS_PROTOCOLS_$_SUIBTypingSessionStarted
+ __OBJC_CLASS_RO_$_SUIBIntelligenceFlowStatusNotification
+ __OBJC_CLASS_RO_$_SUIBIntelligenceFlowStatusNotificationMutation
+ __OBJC_CLASS_RO_$_SUIBTypingSessionStarted
+ __OBJC_CLASS_RO_$_SUIBTypingSessionStartedMutation
+ __OBJC_METACLASS_RO_$_SUIBIntelligenceFlowStatusNotification
+ __OBJC_METACLASS_RO_$_SUIBIntelligenceFlowStatusNotificationMutation
+ __OBJC_METACLASS_RO_$_SUIBTypingSessionStarted
+ __OBJC_METACLASS_RO_$_SUIBTypingSessionStartedMutation
+ ___32-[SUIBTypingSessionStarted init]_block_invoke
+ ___42-[SUIBTypingSessionStarted initWithCoder:]_block_invoke
+ ___46-[SUIBIntelligenceFlowStatusNotification init]_block_invoke
+ ___56-[SUIBIntelligenceFlowStatusNotification initWithCoder:]_block_invoke
+ ___block_descriptor_32_e42_v16?0"SUIBTypingSessionStartedMutation"8l
+ ___block_descriptor_32_e56_v16?0"SUIBIntelligenceFlowStatusNotificationMutation"8l
+ ___block_descriptor_40_e8_32s_e42_v16?0"SUIBTypingSessionStartedMutation"8l
+ ___block_descriptor_40_e8_32s_e56_v16?0"SUIBIntelligenceFlowStatusNotificationMutation"8l
+ ___block_descriptor_72_e8_32s40s48s56s_e37_v16?0"SUIBRequestProgressMutation"8l
+ ___copy_helper_block_e8_32s40s48s56s
+ ___destroy_helper_block_e8_32s40s48s56s
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_destroy_boxed_opaque_existential_0Tm
+ _objc_msgSend$intelligenceFlowStatusNotification
+ _objc_msgSend$setIntelligenceFlowStatusNotification:
+ _objc_msgSend$setStatusString:
+ _objc_msgSend$setTypingSessionId:
+ _objc_msgSend$statusString
+ _objc_msgSend$typingSessionId
+ _symbolic So24SUIBTypingSessionStartedC
+ _symbolic So24SUIBTypingSessionStartedCm
+ _symbolic So46SUIBIntelligenceFlowStatusNotificationMutationCIgg_
+ block_copy_helper.229
+ block_copy_helper.235
+ block_copy_helper.79
+ block_descriptor.231
+ block_descriptor.237
+ block_descriptor.81
+ block_destroy_helper.230
+ block_destroy_helper.236
+ block_destroy_helper.80
- _PROTOCOLS__TtC12SiriUIBridge15UIBridgeService.26
- ___block_descriptor_64_e8_32s40s48s_e37_v16?0"SUIBRequestProgressMutation"8l
- ___copy_helper_block_e8_32s40s48s
- ___destroy_helper_block_e8_32s40s48s
- __swift_FORCE_LOAD_$_swiftAccelerate
- __swift_FORCE_LOAD_$_swiftAccelerate_$_SiriUIBridge
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_SiriUIBridge
- block_copy_helper.37
- block_descriptor.39
- block_destroy_helper.38
CStrings:
+ "@\"SUIBIntelligenceFlowStatusNotification\""
+ "Failed to build TypingStartedMessage"
+ "Going to post TypingStartedMessage"
+ "Received notifyTypingStarted from the UI"
+ "Received typing started for typingSessionId: %s"
+ "SUIBIntelligenceFlowStatusNotification"
+ "SUIBIntelligenceFlowStatusNotificationMutation"
+ "SUIBIntelligenceFlowStatusStringNotification::statusString"
+ "SUIBRequestProgress::intelligenceFlowStatusNotification"
+ "SUIBTypingSessionStarted"
+ "SUIBTypingSessionStarted::typingSessionId"
+ "SUIBTypingSessionStartedMutation"
+ "T@\"NSString\",C,N,V_statusString"
+ "T@\"NSString\",R,C,N,V_statusString"
+ "T@\"NSUUID\",C,N,V_typingSessionId"
+ "T@\"NSUUID\",R,C,N,V_typingSessionId"
+ "T@\"SUIBIntelligenceFlowStatusNotification\",&,N,V_intelligenceFlowStatusNotification"
+ "T@\"SUIBIntelligenceFlowStatusNotification\",R,N,V_intelligenceFlowStatusNotification"
+ "Vv24@0:8@\"SUIBTypingSessionStarted\"16"
+ "_intelligenceFlowStatusNotification"
+ "_statusString"
+ "_typingSessionId"
+ "intelligenceFlowStatusNotification"
+ "notifyTypingStartedWith:"
+ "registerInternalGestureTestingHandler:"
+ "setIntelligenceFlowStatusNotification:"
+ "setStatusString:"
+ "setTypingSessionId:"
+ "statusString"
+ "typingSessionId"
+ "v16@?0@\"SUIBIntelligenceFlowStatusNotificationMutation\"8"
+ "v16@?0@\"SUIBTypingSessionStartedMutation\"8"
+ "v24@0:8@?<v@?qB@?<v@?B@\"NSString\">>16"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "UnsafeMutableRawPointer.initializeMemory with negative count"
- "invalid Collection: less than 'count' elements in collection"

```
