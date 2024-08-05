## HealthKitUI

> `/System/Library/Frameworks/HealthKitUI.framework/HealthKitUI`

```diff

-5132.0.0.0.0
+5138.0.1.1.0
   __TEXT.__text: 0x6494
   __TEXT.__auth_stubs: 0x670
   __TEXT.__objc_methlist: 0x2f0
   __TEXT.__const: 0x1b6
   __TEXT.__cstring: 0x233
   __TEXT.__constg_swiftt: 0x2d4
-  __TEXT.__swift5_typeref: 0x173
+  __TEXT.__swift5_typeref: 0x175
   __TEXT.__swift5_reflstr: 0x64
   __TEXT.__swift5_fieldmd: 0xb0
   __TEXT.__swift5_assocty: 0x30

   __TEXT.__swift5_types: 0x8
   __TEXT.__unwind_info: 0x248
   __TEXT.__objc_classname: 0x60
-  __TEXT.__objc_methname: 0xd5b
+  __TEXT.__objc_methname: 0xd5d
   __TEXT.__objc_methtype: 0x1a4
   __TEXT.__objc_stubs: 0xae0
   __DATA_CONST.__got: 0x100
-  __DATA_CONST.__const: 0xb8
+  __DATA_CONST.__const: 0xf8
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 161
-  Symbols:   205
-  CStrings:  0
+  Symbols:   213
+  CStrings:  84
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "ETACLASS_$_FPDMoveReader"
+ "_$s19RemotePairingDevice0abcB17ServiceConnectionC08listHostB7RecordsSayAA06PairedG4InfoVGyKF"
+ "_$s19RemotePairingDevice0abcB17ServiceConnectionCMa"
+ "_$s19RemotePairingDevice18HostDeletionTargetO06singleD0yAC10Foundation4UUIDV_tcACmFWC"
+ "_$s7Mercury12RemoteDeviceC16remoteConnection10forService12handlerQueueSo07OS_xpc_D11_connectionCSgSS_So0J15_dispatch_queueCSgtFTj"
+ "_$s7Mercury12RemoteDeviceC4nameSSvgTj"
+ "_$s7Mercury12RemoteDeviceC4uuid10Foundation4UUIDVvgTj"
+ "_$s7Mercury12RemoteDeviceC5stateSo014remote_device_D2_tavgTj"
+ "_$s7Mercury12RemoteDeviceCMa"
+ "_$s7Mercury13XPCConnectionC14setTargetQueueyySo17OS_dispatch_queueCSgFTj"
+ "_$s7Mercury13XPCConnectionC30withUnsafeUnderlyingConnectionyxxSo13OS_xpc_object_pKXEKlFTj"
+ "_$s7Mercury13XPCConnectionC4send5value10replyQueue16errorWrapperType0E7Handleryx_So17OS_dispatch_queueCSgq0_mys6ResultOyq_s5Error_pGctKSeRzSERzSeR_SER_AA14DynamicCodableR0_sAN_p7WrappedRt0_r1_lF"
+ "_$s7Mercury13XPCConnectionC4send5valueyx_tKSeRzSERzlF"
+ "_$s7Mercury13XPCConnectionC6cancelyyFTj"
+ "_$s7Mercury13XPCConnectionC8activateyyFTj"
+ "_$s7Mercury13XPCConnectionC8sendSync5value16errorWrapperTypeq_x_q0_mtKSeRzSERzSeR_SER_AA14DynamicCodableR0_s5Error_p7WrappedRt0_r1_lF"
+ "_$s7Mercury13XPCConnectionC8sendSync5valueq_x_tKSeRzSERzSeR_SER_r0_lF"
+ "_$s7Mercury13XPCConnectionCMa"
+ "_$s7Mercury13XPCDictionaryV11createReplyACSgyF"
+ "_$s7Mercury13XPCDictionaryV9sendReplySbyF"
+ "_$s7Mercury13XPCDictionaryVMa"
+ "_$s7Mercury13XPCDictionaryVyACSo13OS_xpc_object_pcfC"
+ "_$s7Mercury13XPCDictionaryVySSSgSScig"
+ "_$s7Mercury16NSErrorContainerVMa"
+ "_$s7Mercury16XPCObjectDecoderCACycfc"
+ "_$s7Mercury16XPCObjectDecoderCMa"
+ "_$s7Mercury16XPCObjectEncoderCACycfc"
+ "_$s7Mercury16XPCObjectEncoderCMa"
+ "_$s7Mercury17XPCPeerConnectionPAAE15setEventHandleryyys6ResultOyqd__s5Error_pGcSeRd__SERd__lF"
+ "_$s7Mercury18XPCObjectContainerV12wrappedValueACSo13OS_xpc_object_p_tcfC"
+ "_$s7Mercury18XPCObjectContainerV12wrappedValueSo13OS_xpc_object_pvM"
+ "_$s7Mercury18XPCObjectContainerV12wrappedValueSo13OS_xpc_object_pvg"
+ "_$s7Mercury18XPCObjectContainerV12wrappedValueSo13OS_xpc_object_pvs"
+ "_$s7Mercury18XPCObjectContainerVMa"
+ "_$s7Mercury19RemoteXPCConnectionC10unsafePeer4fromAA17XPCPeerConnection_pSo24OS_xpc_remote_connectionC_tFZ"
+ "_$s7Mercury19SystemXPCConnectionC10unsafePeer4fromAA17XPCPeerConnection_pSo13OS_xpc_object_p_tFZ"
+ "_$s7Mercury19SystemXPCConnectionC23connectionToMachService4name010privilegedG011targetQueueAA17XPCPeerConnection_pSS_SbSo17OS_dispatch_queueCSgtFZ"
+ "_$s7Mercury19SystemXPCConnectionC27anonymousListenerConnection11targetQueueAA011XPCListenerF0_pSo17OS_dispatch_queueCSg_tFZ"
+ "_$s7Mercury23RemoteXPCPeerConnectionCMa"
+ "_$s7Mercury23SystemXPCPeerConnectionCMa"
+ "_$s7Mercury27SystemXPCListenerConnectionC07setPeerD7Handleryyys6ResultOyAA07XPCPeerD0_pAA8XPCErrorVGcFTj"
+ "_$s7Mercury27SystemXPCListenerConnectionCMa"
+ "_$s7Mercury6_ErrorPAAE8wrappingyxs0B0_pSgF"
+ "_$s7Mercury8XPCErrorV21connectionInterruptedACvgZ"
+ "_$s7Mercury8XPCErrorVMa"
+ "_$sSo21remote_device_state_ta7MercuryE9connectedABvgZ"
+ "_$sSo7NSErrorC7MercuryE24setNormalizationProvider9forDomain13normalizingAs8providerySS_xms5Error_pSgABctAC01_K0RzlFZ"
+ "_$sSo7NSErrorC7MercuryE4fromABs7Decoder_p_tKcfC"
+ "_$sSo7NSErrorC7MercuryE6encode2toys7Encoder_p_tKF"
+ "_$ss5ErrorP7MercuryAC01_A0RzrlE010networkingA0xvgZ"
+ "_$ss5ErrorP7MercuryAC01_A0RzrlE13dataCorruptedxvgZ"
+ "_$ss5ErrorP7MercuryAC01_A0RzrlE_8userInfo011defaultUserD0xx_SDySSypGAGtcfC"
+ "_$ss5ErrorP7MercuryAC01_A0RzrlEyxs5Int32V_SStcfC"
+ "_$ss5ErrorP7MercuryAC01_A0RzrlEyxx_SSSgtcfC"
+ "_$ss5ErrorP7MercuryE10normalized2assAA_pqd__m_tAC01_A0Rd__lF"
+ "_METACLASS_$_FPDSyncBubble"
+ "_OBJC_CLASS_$_FPDAppMonitor"
+ "_OBJC_CLASS_$_FPDConfigurationStore"
+ "_OBJC_CLASS_$_FPDDomain"
+ "_OBJC_CLASS_$_FPDDomainExtensionBackend"
+ "_OBJC_CLASS_$_FPDDomainIndexerSchedulerAssertion"
+ "_OBJC_CLASS_$_FPDDomainIndexerState"
+ "_OBJC_CLASS_$_FPDMoveAtom"
+ "_OBJC_CLASS_$_FPDMoveWriter"
+ "_OBJC_CLASS_$_FPDSharedScheduler"
+ "_OBJC_CLASS_$_FPDVolume"
+ "_OBJC_CLASS_$_FPDVolumeManager"
+ "_OBJC_CLASS_$_RPPairableHost"
+ "_OBJC_CLASS_$_RPPairableHostBrowser"
+ "_OBJC_CLASS_$_RPPairingChallenge"
+ "_OBJC_CLASS_$_RPWirelessPairingSession"
+ "_OBJC_METACLASS_$_FPDConfigurationStore"
+ "_OBJC_METACLASS_$_FPDDomainIndexerSchedulerAssertion"
+ "_OBJC_METACLASS_$_FPDDomainIndexerState"
+ "_OBJC_METACLASS_$_FPDMoveAtom"
+ "_OBJC_METACLASS_$_FPDSharedScheduler"
+ "_OBJC_METACLASS_$_FPDVolume"
+ "_OBJC_METACLASS_$_FPDVolumeManager"
+ "_OBJC_METACLASS_$_RPPairableHost"
+ "_OBJC_METACLASS_$_RPPairableHostBrowser"
+ "_OBJC_METACLASS_$_RPPairingChallenge"
+ "_OBJC_METACLASS_$_RPWirelessPairingSession"
+ "ispatch_queueCSgys5Error_pSgctF"
+ "mXPCConnectionCMa"

```
