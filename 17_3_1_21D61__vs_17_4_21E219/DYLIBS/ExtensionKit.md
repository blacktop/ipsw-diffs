## ExtensionKit

> `/System/Library/Frameworks/ExtensionKit.framework/ExtensionKit`

```diff

-145.5.7.0.0
-  __TEXT.__text: 0x28f80
-  __TEXT.__auth_stubs: 0x12f0
-  __TEXT.__objc_methlist: 0x122c
-  __TEXT.__const: 0x12ac
-  __TEXT.__oslogstring: 0x158f
-  __TEXT.__cstring: 0x1c23
-  __TEXT.__gcc_except_tab: 0x1e0
-  __TEXT.__constg_swiftt: 0x156c
-  __TEXT.__swift5_typeref: 0xc0f
-  __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_reflstr: 0x56c
-  __TEXT.__swift5_fieldmd: 0x754
-  __TEXT.__swift5_types: 0xc0
-  __TEXT.__swift5_capture: 0x340
-  __TEXT.__swift5_proto: 0xb4
-  __TEXT.__swift5_assocty: 0x2a8
+145.5.14.9.0
+  __TEXT.__text: 0x2ce9c
+  __TEXT.__auth_stubs: 0x1480
+  __TEXT.__objc_methlist: 0x134c
+  __TEXT.__const: 0x14bc
+  __TEXT.__oslogstring: 0x15f4
+  __TEXT.__cstring: 0x24b3
+  __TEXT.__gcc_except_tab: 0x27c
+  __TEXT.__constg_swiftt: 0xe88
+  __TEXT.__swift5_typeref: 0xc6c
+  __TEXT.__swift5_builtin: 0x50
+  __TEXT.__swift5_reflstr: 0x59c
+  __TEXT.__swift5_fieldmd: 0x7a8
+  __TEXT.__swift5_assocty: 0x2d8
+  __TEXT.__swift5_proto: 0xcc
+  __TEXT.__swift5_types: 0xcc
+  __TEXT.__swift5_capture: 0x3a0
   __TEXT.__swift5_protos: 0x24
-  __TEXT.__unwind_info: 0x15a0
-  __TEXT.__eh_frame: 0x6c0
-  __TEXT.__objc_classname: 0x537
-  __TEXT.__objc_methname: 0x4129
-  __TEXT.__objc_methtype: 0x144e
-  __TEXT.__objc_stubs: 0x22c0
-  __DATA_CONST.__got: 0x1e0
-  __DATA_CONST.__const: 0x3e0
-  __DATA_CONST.__objc_classlist: 0x130
+  __TEXT.__unwind_info: 0x1650
+  __TEXT.__eh_frame: 0x6b0
+  __TEXT.__objc_classname: 0x5cd
+  __TEXT.__objc_methname: 0x44d6
+  __TEXT.__objc_methtype: 0x15e2
+  __TEXT.__objc_stubs: 0x2440
+  __DATA_CONST.__got: 0x200
+  __DATA_CONST.__const: 0x470
+  __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x108
+  __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6d28
-  __DATA_CONST.__objc_selrefs: 0xc58
+  __DATA_CONST.__objc_const: 0x8078
+  __DATA_CONST.__objc_selrefs: 0xd18
+  __DATA_CONST.__objc_protorefs: 0xa8
+  __DATA_CONST.__objc_classrefs: 0x290
+  __DATA_CONST.__objc_superrefs: 0x98
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__cfstring: 0x220
+  __AUTH_CONST.__objc_const: 0x9b0
+  __AUTH_CONST.__const: 0x1f78
+  __AUTH_CONST.__cfstring: 0x260
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__const: 0xb10
-  __AUTH_CONST.__auth_ptr: 0x50
-  __AUTH_CONST.__auth_got: 0x988
-  __AUTH.__objc_data: 0x0
-  __DATA.__objc_protorefs: 0x88
-  __DATA.__objc_classrefs: 0x250
-  __DATA.__objc_superrefs: 0x98
-  __DATA.__objc_ivar: 0x15c
-  __DATA.__data: 0xe10
+  __AUTH_CONST.__auth_ptr: 0x60
+  __AUTH_CONST.__auth_got: 0xa50
+  __AUTH.__objc_data: 0xf30
+  __AUTH.__data: 0x8c0
+  __DATA.__objc_ivar: 0x16c
+  __DATA.__data: 0x1050
   __DATA.__common: 0x490
-  __DATA.__bss: 0x11e0
-  __DATA_DIRTY.__const: 0x1218
-  __DATA_DIRTY.__objc_const: 0x9b0
-  __DATA_DIRTY.__objc_data: 0x10c8
-  __DATA_DIRTY.__data: 0xa28
+  __DATA.__bss: 0x14e0
+  __DATA_DIRTY.__objc_data: 0x350
+  __DATA_DIRTY.__data: 0x1b8
   __DATA_DIRTY.__bss: 0x90
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
+  - /System/Library/PrivateFrameworks/BoardServices.framework/BoardServices
   - /System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1531
-  Symbols:   2600
-  CStrings:  1157
+  Functions: 1616
+  Symbols:   2756
+  CStrings:  1254
 
Symbols:
+ -[_EXHostSessionDriver hostSessionViewControllerReady:].cold.6
+ -[_EXHostViewController innerConfiguration]
+ -[_EXHostViewController setInnerConfiguration:]
+ -[_EXHostViewControllerConfiguration sceneIdentifier]
+ -[_EXHostViewControllerConfiguration setSceneIdentifier:]
+ -[_EXHostViewControllerSession clientIsReady]
+ -[_EXHostViewControllerSession clientIsReady].cold.1
+ -[_EXHostViewControllerSession invalidationHandler]
+ -[_EXHostViewControllerSession requestRemoteViewController].cold.1
+ -[_EXHostViewControllerSession requestRemoteViewController].cold.2
+ -[_EXHostViewControllerSession requiresFBSceneHosting]
+ -[_EXHostViewControllerSession sceneViewController]
+ -[_EXHostViewControllerSession setInvalidationHandler:]
+ -[_EXHostViewControllerSession setSceneViewController:]
+ -[_EXRunningUISceneExtension startWithArguments:count:].cold.3
+ -[_EXRunningUIViewServiceExtension listener:didReceiveConnection:withContext:]
+ -[_EXRunningUIViewServiceExtension listener:didReceiveConnection:withContext:].cold.1
+ -[_EXRunningUIViewServiceExtension listener:didReceiveConnection:withContext:].cold.2
+ -[_EXRunningUIViewServiceExtension listener:didReceiveConnection:withContext:].cold.3
+ GCC_except_table1
+ GCC_except_table13
+ GCC_except_table39
+ GCC_except_table52
+ GCC_except_table79
+ _OBJC_CLASS_$_BSServiceConnectionListener
+ _OBJC_CLASS_$_BSServicesConfiguration
+ _OBJC_CLASS_$_EXRemoteSceneDelegate
+ _OBJC_CLASS_$_NSThread
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_CLASS_$_UIResponder
+ _OBJC_CLASS_$_UISceneConfiguration
+ _OBJC_CLASS_$_UIWindow
+ _OBJC_CLASS_$_UIWindowScene
+ _OBJC_CLASS_$__EXRunningUIKitSceneHostedExtension
+ _OBJC_CLASS_$__UISceneHostingController
+ _OBJC_CLASS_$__UISceneHostingControllerAdvancedConfiguration
+ _OBJC_CLASS_$__UISceneHostingSceneSpecification
+ _OBJC_IVAR_$__EXHostViewController._innerConfiguration
+ _OBJC_IVAR_$__EXHostViewControllerSession._hostingController
+ _OBJC_IVAR_$__EXHostViewControllerSession._invalidationHandler
+ _OBJC_IVAR_$__EXHostViewControllerSession._requiresFBSceneHosting
+ _OBJC_IVAR_$__EXHostViewControllerSession._sceneViewController
+ _OBJC_METACLASS_$_EXRemoteSceneDelegate
+ _OBJC_METACLASS_$_UIResponder
+ _OBJC_METACLASS_$__EXRunningUIKitSceneHostedExtension
+ _OUTLINED_FUNCTION_17
+ __DATA_EXRemoteSceneDelegate
+ __DATA__EXRunningUIKitSceneHostedExtension
+ __IVARS_EXRemoteSceneDelegate
+ __METACLASS_DATA_EXRemoteSceneDelegate
+ __METACLASS_DATA__EXRunningUIKitSceneHostedExtension
+ __OBJC_$_INSTANCE_METHODS_EXRemoteSceneDelegate
+ __OBJC_$_INSTANCE_METHODS__EXRunningUIKitSceneHostedExtension
+ __OBJC_$_PROP_LIST_UIWindowSceneDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BSServiceConnectionListenerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIWindowSceneDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__UISceneHostingControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BSServiceConnectionListenerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UIWindowSceneDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES__UISceneHostingControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_BSServiceConnectionListenerDelegate
+ __OBJC_$_PROTOCOL_REFS_UIWindowSceneDelegate
+ __OBJC_$_PROTOCOL_REFS__UIHostedWindowSceneDelegate
+ __OBJC_$_PROTOCOL_REFS__UISceneHostingControllerDelegate
+ __OBJC_LABEL_PROTOCOL_$_BSServiceConnectionListenerDelegate
+ __OBJC_LABEL_PROTOCOL_$_UIWindowSceneDelegate
+ __OBJC_LABEL_PROTOCOL_$__EXHostViewDelegateProtocol
+ __OBJC_LABEL_PROTOCOL_$__UIHostedWindowSceneDelegate
+ __OBJC_LABEL_PROTOCOL_$__UISceneHostingControllerDelegate
+ __OBJC_PROTOCOL_$_BSServiceConnectionListenerDelegate
+ __OBJC_PROTOCOL_$_UIWindowSceneDelegate
+ __OBJC_PROTOCOL_$__EXHostViewDelegateProtocol
+ __OBJC_PROTOCOL_$__UIHostedWindowSceneDelegate
+ __OBJC_PROTOCOL_$__UISceneHostingControllerDelegate
+ __PROPERTIES_EXRemoteSceneDelegate
+ __PROTOCOLS_EXRemoteSceneDelegate
+ __PROTOCOLS_EXRemoteSceneDelegate.1
+ __PROTOCOLS__EXRunningUIKitSceneHostedExtension
+ __PROTOCOLS__EXRunningUIKitSceneHostedExtension.1
+ __PROTOCOLS__TtC12ExtensionKit13_SceneFactory.19
+ __PROTOCOLS__TtC12ExtensionKitP33_B73671B6E3271B2B0FF13F0EEBE6E03017_ViewSceneAdaptor.10
+ __PROTOCOLS__TtC12ExtensionKitP33_B73671B6E3271B2B0FF13F0EEBE6E03017_ViewSceneFactory.8
+ __PROTOCOLS__TtCC12ExtensionKit13_SceneFactory6_Scene.24
+ ___53-[_EXHostViewControllerSession processDidInvalidate:]_block_invoke_2
+ ___55-[_EXRunningUISceneExtension startWithArguments:count:]_block_invoke
+ ___59-[_EXHostViewControllerSession requestRemoteViewController]_block_invoke.149
+ ___59-[_EXHostViewControllerSession requestRemoteViewController]_block_invoke.149.cold.1
+ ___59-[_EXHostViewControllerSession requestRemoteViewController]_block_invoke.149.cold.2
+ ___60-[_EXHostViewControllerSession _internalQueue_prepareToHost]_block_invoke.132
+ ___60-[_EXHostViewControllerSession _internalQueue_prepareToHost]_block_invoke.132.cold.1
+ ___60-[_EXHostViewControllerSession _internalQueue_prepareToHost]_block_invoke.136
+ ___60-[_EXHostViewControllerSession _internalQueue_prepareToHost]_block_invoke.141
+ ___60-[_EXHostViewControllerSession _internalQueue_prepareToHost]_block_invoke.141.cold.1
+ ___61-[_EXRunningUIViewServiceExtension startWithArguments:count:]_block_invoke.42
+ ___61-[_EXRunningUIViewServiceExtension startWithArguments:count:]_block_invoke_2
+ ___78-[_EXRunningUIViewServiceExtension listener:didReceiveConnection:withContext:]_block_invoke
+ ___block_descriptor_32_e40_v16?0"<BSNSXPCConnectionConfiguring>"8l
+ ___block_descriptor_32_e8_B12?0B8l
+ ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_40_e8_32w_e50_v16?0"<BSServiceConnectionListenerConfiguring>"8lw32l8
+ ___swift_memcpy80_8
+ _associated conformance So29UIApplicationLaunchOptionsKeyaSHSCSQ
+ _associated conformance So29UIApplicationLaunchOptionsKeyas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So29UIApplicationLaunchOptionsKeyas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _block_copy_helper.10
+ _block_descriptor.12
+ _block_destroy_helper.11
+ _get_witness_table 12ExtensionKit012PrimitiveAppA5SceneVAA0daE0HPyHC.25
+ _get_witness_table 12ExtensionKit07_AnyAppA5SceneVAA0daE0HPyHC.32
+ _get_witness_table 12ExtensionKit0A34HostingViewControllerRepresentableV7SwiftUI0D0HPyHC.14
+ _get_witness_table 7SwiftUI6HStackVyAA9TupleViewVyAA5ImageVSg_AA4TextVAA6SpacerVAA0E0PAAE11toggleStyleyQrqd__AA06ToggleJ0Rd__lFQOyAA0K0VyAJG_AA06SwitchkJ0VQo_tGGAaMHPyHC.50
+ _get_witness_table 7SwiftUI6VStackVyAA9TupleViewVyAA15ModifiedContentVyAA4TextVAA14_PaddingLayoutVG_AA4FormVyAA7ForEachVySay12ExtensionKit12ContainerApp33_ABD14ED04C699754E7718E30E84C391ALLVG10Foundation3URLVAQ0pqE0ASLLVGGAA6SpacerVtGGAA0E0HPyHC.49
+ _get_witness_table 7SwiftUI7AnyViewVAA0D0HPyHC.19
+ _get_witness_table 7SwiftUI7SectionVyAA6HStackVyAA9TupleViewVyAA5ImageV_AA4TextVtGGAA7ForEachVySay19ExtensionFoundation04_AppK8IdentityVG0L04UUIDV0K3Kit0mkF033_ABD14ED04C699754E7718E30E84C391ALLVGAA05EmptyF0VGAA0F0HPAmAA3_HPyHC_A_AAA3_HPAzAA3_HPyHC_HCA1_AAA3_HPyHCHC.54
+ _get_witness_table 7SwiftUI9EmptyViewVAA0D0HPyHC.11
+ _objc_msgSend$_beginDelayingPresentation:cancellationHandler:
+ _objc_msgSend$_endDelayingPresentation
+ _objc_msgSend$activateXPCService
+ _objc_msgSend$didMoveToParentViewController:
+ _objc_msgSend$extensionProcessWithConfiguration:error:
+ _objc_msgSend$extractNSXPCConnectionWithConfigurator:
+ _objc_msgSend$initWithAdvancedConfiguration:
+ _objc_msgSend$initWithProcessIdentity:
+ _objc_msgSend$invalidationHandler
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$isMainThread
+ _objc_msgSend$listenerWithConfigurator:
+ _objc_msgSend$processIdentity
+ _objc_msgSend$requiresFBSceneHosting
+ _objc_msgSend$requiresUIKitSceneHosting
+ _objc_msgSend$sceneViewController
+ _objc_msgSend$service
+ _objc_msgSend$setActivateOnResume
+ _objc_msgSend$setDomain:
+ _objc_msgSend$setFaultOnSuspend
+ _objc_msgSend$setSceneSpecification:
+ _objc_msgSend$setSceneViewController:
+ _objc_msgSend$setService:
+ _objc_retain_x26
+ _objc_setProperty_nonatomic_copy
+ _objectdestroy.17Tm
+ _objectdestroy.34Tm
+ _swift_dynamicCastObjCProtocolUnconditional
+ _swift_isEscapingClosureAtFileLocation
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
+ _symbolic $ss21_ObjectiveCBridgeableP
+ _symbolic So11UIResponderC
+ _symbolic So21_EXRunningUIExtensionC
+ _symbolic So38BSServiceConnectionListenerConfiguring_pIgg_
+ _symbolic So8NSStringC
+ _symbolic So8UIWindowCSg
+ _symbolic _____ 12ExtensionKit026_EXRunningUIKitSceneHostedA0C
+ _symbolic _____ 12ExtensionKit21EXRemoteSceneDelegateC
+ _symbolic _____ So29UIApplicationLaunchOptionsKeya
+ _symbolic _____Sg 10Foundation4UUIDV
+ _symbolic _____SgXw 12ExtensionKit026_EXRunningUIKitSceneHostedA0C
- -[_EXHostViewControllerSession requiresSceneHosting]
- GCC_except_table37
- GCC_except_table49
- GCC_except_table72
- _OBJC_CLASS_$__EXExtensionProcessMannger
- _OBJC_CLASS_$__EXLaunchConfiguration
- _OBJC_IVAR_$__EXHostViewControllerSession._requiresSceneHosting
- _UIApplicationMain
- __PROTOCOLS__TtC12ExtensionKit13_SceneFactory.24
- __PROTOCOLS__TtC12ExtensionKitP33_B73671B6E3271B2B0FF13F0EEBE6E03017_ViewSceneAdaptor.12
- __PROTOCOLS__TtC12ExtensionKitP33_B73671B6E3271B2B0FF13F0EEBE6E03017_ViewSceneFactory.9
- __PROTOCOLS__TtCC12ExtensionKit13_SceneFactory6_Scene.30
- ___59-[_EXHostViewControllerSession requestRemoteViewController]_block_invoke.cold.1
- ___59-[_EXHostViewControllerSession requestRemoteViewController]_block_invoke.cold.2
- ___60-[_EXHostViewControllerSession _internalQueue_prepareToHost]_block_invoke.131
- ___60-[_EXHostViewControllerSession _internalQueue_prepareToHost]_block_invoke.131.cold.1
- ___60-[_EXHostViewControllerSession _internalQueue_prepareToHost]_block_invoke.135
- ___60-[_EXHostViewControllerSession _internalQueue_prepareToHost]_block_invoke.140
- ___60-[_EXHostViewControllerSession _internalQueue_prepareToHost]_block_invoke.140.cold.1
- ___swift_memcpy72_8
- _dispatch_assert_queue_not$V2
- _get_witness_table 12ExtensionKit012PrimitiveAppA5SceneVAA0daE0HPyHC.28
- _get_witness_table 12ExtensionKit03AppA5SceneRzAaBR_AaBR0_AaBR1_AaBR2_AaBR3_AaBR4_AaBR5_AaBR6_AaBR7_r8_lSayAA04_AnycaD0VGAaBHpAdaBHPyHC_HC.9
- _get_witness_table 12ExtensionKit03AppA5SceneRzAaBR_AaBR0_AaBR1_AaBR2_AaBR3_AaBR4_AaBR5_AaBR6_r7_lSayAA04_AnycaD0VGAaBHpAdaBHPyHC_HC.8
- _get_witness_table 12ExtensionKit03AppA5SceneRzAaBR_AaBR0_AaBR1_AaBR2_AaBR3_AaBR4_AaBR5_r6_lSayAA04_AnycaD0VGAaBHpAdaBHPyHC_HC.7
- _get_witness_table 12ExtensionKit03AppA5SceneRzAaBR_AaBR0_AaBR1_AaBR2_AaBR3_AaBR4_r5_lSayAA04_AnycaD0VGAaBHpAdaBHPyHC_HC.6
- _get_witness_table 12ExtensionKit03AppA5SceneRzAaBR_AaBR0_AaBR1_AaBR2_AaBR3_r4_lSayAA04_AnycaD0VGAaBHpAdaBHPyHC_HC.5
- _get_witness_table 12ExtensionKit03AppA5SceneRzAaBR_AaBR0_AaBR1_AaBR2_r3_lSayAA04_AnycaD0VGAaBHpAdaBHPyHC_HC.4
- _get_witness_table 12ExtensionKit03AppA5SceneRzAaBR_AaBR0_AaBR1_r2_lSayAA04_AnycaD0VGAaBHpAdaBHPyHC_HC.3
- _get_witness_table 12ExtensionKit03AppA5SceneRzAaBR_AaBR0_r1_lSayAA04_AnycaD0VGAaBHpAdaBHPyHC_HC.2
- _get_witness_table 12ExtensionKit03AppA5SceneRzAaBR_r0_lSayAA04_AnycaD0VGAaBHpAdaBHPyHC_HC.1
- _get_witness_table 12ExtensionKit03AppA5SceneRzlxAaBHD1_.37
- _get_witness_table 12ExtensionKit07_AnyAppA5SceneVAA0daE0HPyHC.39
- _get_witness_table 12ExtensionKit0A34HostingViewControllerRepresentableV7SwiftUI0D0HPyHC.15
- _get_witness_table 7SwiftUI6HStackVyAA9TupleViewVyAA5ImageVSg_AA4TextVAA6SpacerVAA0E0PAAE11toggleStyleyQrqd__AA06ToggleJ0Rd__lFQOyAA0K0VyAJG_AA06SwitchkJ0VQo_tGGAaMHPyHC.53
- _get_witness_table 7SwiftUI6VStackVyAA9TupleViewVyAA15ModifiedContentVyAA4TextVAA14_PaddingLayoutVG_AA4FormVyAA7ForEachVySay12ExtensionKit12ContainerApp33_ABD14ED04C699754E7718E30E84C391ALLVG10Foundation3URLVAQ0pqE0ASLLVGGAA6SpacerVtGGAA0E0HPyHC.52
- _get_witness_table 7SwiftUI7AnyViewVAA0D0HPyHC.29
- _get_witness_table 7SwiftUI7SectionVyAA6HStackVyAA9TupleViewVyAA5ImageV_AA4TextVtGGAA7ForEachVySay19ExtensionFoundation04_AppK8IdentityVG0L04UUIDV0K3Kit0mkF033_ABD14ED04C699754E7718E30E84C391ALLVGAA05EmptyF0VGAA0F0HPAmAA3_HPyHC_A_AAA3_HPAzAA3_HPyHC_HCA1_AAA3_HPyHCHC.57
- _get_witness_table 7SwiftUI9EmptyViewVAA0D0HPyHC.13
- _objc_msgSend$_queue
- _objc_msgSend$initWithMachServiceName:
- _objc_msgSend$internalServiceName
- _objc_msgSend$preferredLanguages
- _objc_msgSend$processWithLaunchConfiguration:error:
- _objc_msgSend$sandboxProfileName
- _objc_msgSend$serviceListener
- _objc_msgSend$serviceName
- _objc_msgSend$setPreferredLanguages:
- _objc_msgSend$setRole:
- _objc_msgSend$setSandboxProfileName:
- _objectdestroy.21Tm
- _objectdestroy.41Tm
- _symbolic Say_____G 12ExtensionKit07_AnyAppA5SceneV
- _symbolic q0_
- _symbolic q1_
- _symbolic q2_
- _symbolic q3_
- _symbolic q4_
- _symbolic q5_
- _symbolic q6_
- _symbolic q7_
CStrings:
+ "\x01\x12$#\x14!"
+ "\x01\x15"
+ "%s - %s:%d: Cannot vend a scene to an extension when the extension point does not require FBScene hosting"
+ "%s - %s:%d: Unexpected nil scene view controller"
+ "@\"_EXHostViewControllerConfiguration\""
+ "@\"_UISceneHostingController\""
+ "AQ"
+ "B12@?0B8"
+ "BSServiceConnectionListenerDelegate"
+ "Can't construct Array with count < 0"
+ "Could not fetch view controller for session: %{public}@ scene id: %{public}s"
+ "Could not find _EXRunningUIKitSceneHostedExtension when configuring listener"
+ "Creating AppExtensionWrapper with content %s"
+ "Creating _UIAppExtensionSceneConfigWrapper with content %s"
+ "Creating _UIAppExtensionWrapper with content %s"
+ "Division by zero"
+ "Division results in an overflow"
+ "ExtensionKit/EXRunningUIKitSceneHostedExtension.swift"
+ "Insufficient space allocated to copy string contents"
+ "InternalService"
+ "Launching UI AppExtension %@"
+ "Launching UI _AppExtension %@"
+ "Launching UI _AppExtension for scene configuration %@"
+ "MainService"
+ "Received connection request on unknown listener "
+ "Received scene connection request from host: %{public}s"
+ "Requesting scene view from: %{public}@"
+ "Session ID could not be found for scene id: %{public}s"
+ "Swift/Array.swift"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/IntegerTypes.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",C,D,N"
+ "T@\"NSString\",C,N,V_sceneIdentifier"
+ "T@\"UIViewController\",&,N,V_sceneViewController"
+ "T@\"UIWindow\",?,&,N"
+ "T@\"UIWindow\",N,&,Vwindow"
+ "T@\"_EXHostViewControllerConfiguration\",C,N,V_innerConfiguration"
+ "T@,?,&"
+ "TB,R,V_requiresFBSceneHosting"
+ "UISceneHostingController is ready"
+ "UIWindowSceneDelegate"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "Using legacy view services path"
+ "XPCService"
+ "_EXHostViewDelegateProtocol"
+ "_UIHostedScene-%@"
+ "_UIHostedWindowSceneDelegate"
+ "_UISceneHostingControllerDelegate"
+ "_beginDelayingPresentation:cancellationHandler:"
+ "_endDelayingPresentation"
+ "_hostingController"
+ "_innerConfiguration"
+ "_requiresFBSceneHosting"
+ "_sceneViewController"
+ "activateXPCService"
+ "application(_:configurationForConnecting:options:)"
+ "applicationDidBecomeActive(_:)"
+ "applicationWillResignActive(_:)"
+ "clientDidUpdatePreferredContentSize:"
+ "clientIsReady"
+ "didMoveToParentViewController:"
+ "extensionProcessWithConfiguration:error:"
+ "extractNSXPCConnectionWithConfigurator:"
+ "initWithAdvancedConfiguration:"
+ "initWithName:sessionRole:"
+ "initWithProcessIdentity:"
+ "initWithWindowScene:"
+ "innerConfiguration"
+ "invalid Collection: less than 'count' elements in collection"
+ "isEqualToString:"
+ "isMainThread"
+ "listener:didReceiveConnection:withContext:"
+ "listenerWithConfigurator:"
+ "makeKeyAndVisible"
+ "processIdentity"
+ "requiresFBSceneHosting"
+ "requiresUIKitSceneHosting"
+ "sceneViewController"
+ "service"
+ "session == nil || session.detached"
+ "session.sceneViewController"
+ "setActivateOnResume"
+ "setDomain:"
+ "setFaultOnSuspend"
+ "setInnerConfiguration:"
+ "setSceneSpecification:"
+ "setSceneViewController:"
+ "setService:"
+ "v16@?0@\"<BSNSXPCConnectionConfiguring>\"8"
+ "v16@?0@\"<BSServiceConnectionListenerConfiguring>\"8"
+ "v32@0:8@\"UIWindowScene\"16@\"CKShareMetadata\"24"
+ "v32@0:8{CGSize=dd}16"
+ "v40@0:8@\"BSServiceConnectionListener\"16@\"BSServiceConnection<BSServiceConnectionHost>\"24@\"<BSXPCDecoding>\"32"
+ "v40@0:8@\"UIWindowScene\"16@\"UIApplicationShortcutItem\"24@?<v@?B>32"
+ "v48@0:8@\"UIWindowScene\"16@\"<UICoordinateSpace>\"24q32@\"UITraitCollection\"40"
+ "v48@0:8@16@24q32@40"
+ "windowScene:didUpdateCoordinateSpace:interfaceOrientation:traitCollection:"
+ "windowScene:performActionForShortcutItem:completionHandler:"
+ "windowScene:userDidAcceptCloudKitShareWithMetadata:"
- "\x01\x14"
- "\x11$\"\x14!"
- "!Q"
- "%s - %s:%d: Cannot vend a scene to an extension when the extension point does not require scene hosting"
- "Configuring internal mach service listener: %{public}@"
- "Creating _SwiftUIExtension with content %s"
- "Launching UI extension %@"
- "T@\"NSString\",&,N,V_sceneIdentifier"
- "T@\"UIWindow\",&,N"
- "T@,&"
- "TB,R,V_requiresSceneHosting"
- "_queue"
- "_requiresSceneHosting"
- "initWithMachServiceName:"
- "internalServiceName"
- "preferredLanguages"
- "processWithLaunchConfiguration:error:"
- "sandboxProfileName"
- "serviceName"
- "session.detached"
- "setPreferredLanguages:"
- "setSandboxProfileName:"

```
