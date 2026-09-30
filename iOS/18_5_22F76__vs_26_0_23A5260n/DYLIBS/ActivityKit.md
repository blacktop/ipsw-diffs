## ActivityKit

> `/System/Library/Frameworks/ActivityKit.framework/ActivityKit`

```diff

-203.6.5.0.0
-  __TEXT.__text: 0xa8a58
-  __TEXT.__auth_stubs: 0x17c0
-  __TEXT.__objc_methlist: 0xdbc
-  __TEXT.__const: 0xcbfa
-  __TEXT.__cstring: 0x2c51
+255.0.1.0.0
+  __TEXT.__text: 0xacf5c
+  __TEXT.__auth_stubs: 0x18d0
+  __TEXT.__objc_methlist: 0xe7c
+  __TEXT.__const: 0xcffa
+  __TEXT.__cstring: 0x2d61
   __TEXT.__gcc_except_tab: 0x18
-  __TEXT.__swift5_typeref: 0x395a
-  __TEXT.__swift5_fieldmd: 0x29a0
-  __TEXT.__constg_swiftt: 0x34a4
+  __TEXT.__swift5_typeref: 0x3aae
+  __TEXT.__swift5_fieldmd: 0x2c50
+  __TEXT.__constg_swiftt: 0x3580
   __TEXT.__swift5_builtin: 0xb4
-  __TEXT.__swift5_reflstr: 0x1d70
+  __TEXT.__swift5_reflstr: 0x203e
   __TEXT.__swift5_protos: 0x28
-  __TEXT.__swift5_types: 0x3b0
+  __TEXT.__swift5_types: 0x3c0
   __TEXT.__swift5_assocty: 0x700
-  __TEXT.__swift5_proto: 0xc58
+  __TEXT.__swift5_proto: 0xc64
   __TEXT.__oslogstring: 0x1a9f
-  __TEXT.__swift5_capture: 0x90c
-  __TEXT.__swift_as_entry: 0x88
-  __TEXT.__swift_as_ret: 0x80
+  __TEXT.__swift5_capture: 0x9b4
+  __TEXT.__swift_as_entry: 0x94
+  __TEXT.__swift_as_ret: 0x8c
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__unwind_info: 0x3168
-  __TEXT.__eh_frame: 0x3b18
-  __TEXT.__objc_classname: 0x496
-  __TEXT.__objc_methname: 0x1ae4
-  __TEXT.__objc_methtype: 0x7f0
-  __TEXT.__objc_stubs: 0x540
-  __DATA_CONST.__got: 0x410
-  __DATA_CONST.__const: 0x240
-  __DATA_CONST.__objc_classlist: 0x148
-  __DATA_CONST.__objc_protolist: 0x1b8
+  __TEXT.__unwind_info: 0x32c0
+  __TEXT.__eh_frame: 0x3d70
+  __TEXT.__objc_classname: 0x4bc
+  __TEXT.__objc_methname: 0x1e35
+  __TEXT.__objc_methtype: 0x870
+  __TEXT.__objc_stubs: 0x600
+  __DATA_CONST.__got: 0x448
+  __DATA_CONST.__const: 0x220
+  __DATA_CONST.__objc_classlist: 0x150
+  __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5b8
-  __DATA_CONST.__objc_protorefs: 0xd8
+  __DATA_CONST.__objc_selrefs: 0x628
+  __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0xbf0
-  __AUTH_CONST.__const: 0x7848
+  __AUTH_CONST.__auth_got: 0xc78
+  __AUTH_CONST.__const: 0x7b48
   __AUTH_CONST.__cfstring: 0xe0
-  __AUTH_CONST.__objc_const: 0x4e40
+  __AUTH_CONST.__objc_const: 0x5298
   __AUTH.__objc_data: 0x1138
-  __AUTH.__data: 0xb70
-  __DATA.__objc_ivar: 0x80
-  __DATA.__data: 0x2e50
-  __DATA.__bss: 0x11bb0
+  __AUTH.__data: 0xcf0
+  __DATA.__objc_ivar: 0x94
+  __DATA.__data: 0x2f18
+  __DATA.__bss: 0x107b0
   __DATA.__common: 0x38
   __DATA_DIRTY.__objc_data: 0x830
-  __DATA_DIRTY.__data: 0x21b0
-  __DATA_DIRTY.__bss: 0x6b80
+  __DATA_DIRTY.__data: 0x2638
+  __DATA_DIRTY.__bss: 0x8100
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

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
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 08060227-A988-3C65-A583-F016167D2BD0
-  Functions: 4665
-  Symbols:   2756
-  CStrings:  839
+  UUID: 98ABBC9C-2240-3D70-80C2-6935B9AAE400
+  Functions: 4840
+  Symbols:   2871
+  CStrings:  879
 
Symbols:
+ -[ACActivityDescriptor alertContentTypeForDestination:]
+ -[ACActivityDescriptor alertContentTypesByDestination]
+ -[ACActivityDescriptor alertSceneTargetBundleIdentifiers]
+ -[ACActivityDescriptor contentTypeForDestination:]
+ -[ACActivityDescriptor contentTypesByDestination]
+ -[ACActivityDescriptor initWithIdentifier:sceneTargets:alertSceneTargets:presentationOptions:isEphemeral:isMomentary:isImportant:createdDate:descriptorData:contentTypesByDestination:alertContentTypesByDestination:remoteDeviceIdentifier:localizedAppName:protectionClass:]
+ -[ACActivityDescriptor isImportant]
+ -[ACActivityDescriptor sceneTargetBundleIdentifiers]
+ -[ACActivityDescriptor setAlertContentTypesByDestination:]
+ -[ACActivityDescriptor setAlertSceneTargetBundleIdentifiers:]
+ -[ACActivityDescriptor setContentTypesByDestination:]
+ -[ACActivityDescriptor setIsImportant:]
+ -[ACActivityDescriptor setSceneTargetBundleIdentifiers:]
+ -[ACActivityPresentationDestination hash]
+ -[ACActivityPresentationDestination isEqual:]
+ -[ACActivityPresentationOptions setShouldShowSystemAperture:]
+ -[ACActivityPresentationOptions shouldShowSystemAperture]
+ _OBJC_IVAR_$_ACActivityDescriptor._alertContentTypesByDestination
+ _OBJC_IVAR_$_ACActivityDescriptor._alertSceneTargetBundleIdentifiers
+ _OBJC_IVAR_$_ACActivityDescriptor._contentTypesByDestination
+ _OBJC_IVAR_$_ACActivityDescriptor._isImportant
+ _OBJC_IVAR_$_ACActivityDescriptor._sceneTargetBundleIdentifiers
+ _OBJC_IVAR_$_ACActivityPresentationOptions._shouldShowSystemAperture
+ __DATA__TtC11ActivityKit21OpaqueActivityManager
+ __IVARS__TtC11ActivityKit21OpaqueActivityManager
+ __METACLASS_DATA__TtC11ActivityKit21OpaqueActivityManager
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSServiceConnectionCommonConfiguring
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BSServiceConnectionCommonConfiguring
+ __OBJC_$_PROTOCOL_REFS_BSServiceConnectionConfiguring
+ __OBJC_LABEL_PROTOCOL_$_BSServiceConnectionCommonConfiguring
+ __OBJC_PROTOCOL_$_BSServiceConnectionCommonConfiguring
+ ___swift_get_extra_inhabitant_index.68Tm
+ ___swift_memcpy32_8
+ ___swift_store_extra_inhabitant_index.69Tm
+ ___unnamed_17
+ ___unnamed_22
+ ___unnamed_6
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_ActivityKit
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_ActivityKit
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_ActivityKit
+ _associated conformance 11ActivityKit0A5StateO17PendingCodingKeys33_7479A81CBD973C41DEB4E01A204B8250LLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 11ActivityKit0A5StateO17PendingCodingKeys33_7479A81CBD973C41DEB4E01A204B8250LLOs0E3KeyAAs28CustomDebugStringConvertible
+ _block_copy_helper.111
+ _block_copy_helper.19
+ _block_copy_helper.41
+ _block_copy_helper.55
+ _block_copy_helper.67
+ _block_descriptor.113
+ _block_descriptor.21
+ _block_descriptor.43
+ _block_descriptor.57
+ _block_descriptor.69
+ _block_destroy_helper.112
+ _block_destroy_helper.20
+ _block_destroy_helper.42
+ _block_destroy_helper.56
+ _block_destroy_helper.68
+ _objc_msgSend$alertSceneTargetBundleIdentifiers
+ _objc_msgSend$destination
+ _objc_msgSend$initWithDestination:
+ _objc_msgSend$initWithIdentifier:sceneTargets:alertSceneTargets:presentationOptions:isEphemeral:isMomentary:isImportant:createdDate:descriptorData:contentTypesByDestination:alertContentTypesByDestination:remoteDeviceIdentifier:localizedAppName:protectionClass:
+ _objc_msgSend$integerValue
+ _objc_msgSend$isImportant
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$sceneTargetBundleIdentifiers
+ _objc_msgSend$setShouldShowSystemAperture:
+ _objc_opt_class
+ _objc_opt_isKindOfClass
+ _objc_release_x9
+ _objc_retain_x9
+ _objectdestroyTm
+ _swift_coroFrameAlloc
+ _swift_unknownObjectRelease_n
+ _swift_unknownObjectRetain_n
+ _swift_willThrowTypedImpl
+ _symbolic SDy__________G 11ActivityKit0A19PresentationOptionsV0aC11DestinationO AA11SceneTargetO
+ _symbolic SDy__________G 11ActivityKit0A19PresentationOptionsV0aC11DestinationO AA11SceneTargetO7RequestO
+ _symbolic _____ 11ActivityKit06OpaqueA7ManagerC
+ _symbolic _____ 11ActivityKit06OpaqueA7ManagerC7RequestV
+ _symbolic _____ 11ActivityKit0A0C7RequestV
+ _symbolic _____ 11ActivityKit0A5StateO17PendingCodingKeys33_7479A81CBD973C41DEB4E01A204B8250LLO
+ _symbolic _____Sg 11ActivityKit0A5StateO
+ _symbolic ______AAt 11ActivityKit04PushA13ContentSourceV0C4TypeO
+ _symbolic ______AAt 11ActivityKit0A13ContentSourceO
+ _symbolic ______AAt 11ActivityKit0A13ContentSourceO7RequestO
+ _symbolic ___________t 11ActivityKit0A19PresentationOptionsV0aC11DestinationO AA11SceneTargetO
+ _symbolic ___________t 11ActivityKit0A19PresentationOptionsV0aC11DestinationO AA11SceneTargetO7RequestO
+ _symbolic _____ySo33ACActivityPresentationDestinationCSSG s18_DictionaryStorageC
+ _symbolic _____ySo33ACActivityPresentationDestinationCSo8NSNumberCG s18_DictionaryStorageC
+ _symbolic _____y_____G s22KeyedDecodingContainerV 11ActivityKit0D5StateO17PendingCodingKeys33_7479A81CBD973C41DEB4E01A204B8250LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 11ActivityKit0D5StateO17PendingCodingKeys33_7479A81CBD973C41DEB4E01A204B8250LLO
+ _symbolic _____y__________G s18_DictionaryStorageC 11ActivityKit0C19PresentationOptionsV0cE11DestinationO AC11SceneTargetO
+ _symbolic _____y__________G s18_DictionaryStorageC 11ActivityKit0C19PresentationOptionsV0cE11DestinationO AC11SceneTargetO7RequestO
+ _symbolic _____y___________tG s23_ContiguousArrayStorageC 11ActivityKit0D19PresentationOptionsV0dF11DestinationO AC11SceneTargetO
+ _symbolic _____y___________tG s23_ContiguousArrayStorageC 11ActivityKit0D19PresentationOptionsV0dF11DestinationO AC11SceneTargetO7RequestO
- -[ACActivityDescriptor initWithIdentifier:target:presentationOptions:isEphemeral:isMomentary:createdDate:descriptorData:contentType:remoteDeviceIdentifier:localizedAppName:protectionClass:]
- -[ACActivityDescriptor setContentType:]
- -[ACActivityDescriptor setPlatterTargetBundleIdentifier:]
- _OBJC_IVAR_$_ACActivityDescriptor._platterTargetBundleIdentifier
- ___swift_get_extra_inhabitant_index.38Tm
- ___swift_store_extra_inhabitant_index.39Tm
- ___unnamed_16
- ___unnamed_18
- ___unnamed_5
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_ActivityKit
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_ActivityKit
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_ActivityKit
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_ActivityKit
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_ActivityKit
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_ActivityKit
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_ActivityKit
- _block_copy_helper.113
- _block_copy_helper.33
- _block_copy_helper.46
- _block_copy_helper.56
- _block_copy_helper.62
- _block_copy_helper.65
- _block_copy_helper.68
- _block_copy_helper.79
- _block_descriptor.115
- _block_descriptor.35
- _block_descriptor.48
- _block_descriptor.58
- _block_descriptor.64
- _block_descriptor.67
- _block_descriptor.70
- _block_descriptor.81
- _block_destroy_helper.114
- _block_destroy_helper.34
- _block_destroy_helper.47
- _block_destroy_helper.57
- _block_destroy_helper.63
- _block_destroy_helper.66
- _block_destroy_helper.69
- _block_destroy_helper.80
- _objc_msgSend$contentType
- _objc_msgSend$initWithIdentifier:target:presentationOptions:isEphemeral:isMomentary:createdDate:descriptorData:contentType:remoteDeviceIdentifier:localizedAppName:protectionClass:
- _objc_msgSend$platterTargetBundleIdentifier
- _objc_retain_x13
- _objc_retain_x14
- _swift_release_n
- _symbolic _____Sg 11ActivityKit11SceneTargetO
CStrings:
+ "@\"NSData\"40@0:8@\"NSData\"16@\"NSData\"24o^@32"
+ "@\"NSDictionary\""
+ "@116@0:8@16@24@32@40B48B52B56@60@68@76@84@92@100q108"
+ "@40@0:8@16@24o^@32"
+ "Alert Presentation Targets: "
+ "BSServiceConnectionCommonConfiguring"
+ "Presentation Targets: "
+ "Should Show System Aperture: "
+ "T@\"NSDictionary\",C,N,V_alertContentTypesByDestination"
+ "T@\"NSDictionary\",C,N,V_alertSceneTargetBundleIdentifiers"
+ "T@\"NSDictionary\",C,N,V_contentTypesByDestination"
+ "T@\"NSDictionary\",C,N,V_sceneTargetBundleIdentifiers"
+ "T@\"NSString\",R,C,N"
+ "TB,N,V_isImportant"
+ "TB,N,V_shouldShowSystemAperture"
+ "Tq,R,N,V_contentType"
+ "_TtC11ActivityKit21OpaqueActivityManager"
+ "_alertContentTypesByDestination"
+ "_alertSceneTargetBundleIdentifiers"
+ "_contentTypesByDestination"
+ "_isImportant"
+ "_sceneTargetBundleIdentifiers"
+ "_shouldShowSystemAperture"
+ "alertContentTypeForDestination:"
+ "alertContentTypesByDestination"
+ "alertSceneTargetBundleIdentifiers"
+ "alertSceneTargets"
+ "breaksThroughFocus"
+ "carPlay"
+ "com.apple.chrono.WidgetRenderer-Activities"
+ "contentTypeForDestination:"
+ "contentTypesByDestination"
+ "delayedStartParticipant"
+ "fullScreen"
+ "initWithIdentifier:sceneTargets:alertSceneTargets:presentationOptions:isEphemeral:isMomentary:isImportant:createdDate:descriptorData:contentTypesByDestination:alertContentTypesByDestination:remoteDeviceIdentifier:localizedAppName:protectionClass:"
+ "isImportant"
+ "objectForKeyedSubscript:"
+ "q24@0:8@16"
+ "requestActivityWithRequest:alertConfiguration:error:"
+ "sceneTargetBundleIdentifiers"
+ "setAlertContentTypesByDestination:"
+ "setAlertSceneTargetBundleIdentifiers:"
+ "setContentTypesByDestination:"
+ "setIsImportant:"
+ "setQueue:"
+ "setSceneTargetBundleIdentifiers:"
+ "setShouldShowSystemAperture:"
+ "shouldShowSystemAperture"
+ "v24@0:8@\"BSServiceQueue\"16"
- "@96@0:8@16@24@32B40B44@48@56q64@72@80q88"
- "Platter Target: "
- "T@\"NSString\",C,N,V_platterTargetBundleIdentifier"
- "Tq,N,V_contentType"
- "_platterTargetBundleIdentifier"
- "com.apple.chronod"
- "initWithIdentifier:target:presentationOptions:isEphemeral:isMomentary:createdDate:descriptorData:contentType:remoteDeviceIdentifier:localizedAppName:protectionClass:"
- "requestActivityWithRequest:error:"
- "setContentType:"
- "setPlatterTargetBundleIdentifier:"

```
