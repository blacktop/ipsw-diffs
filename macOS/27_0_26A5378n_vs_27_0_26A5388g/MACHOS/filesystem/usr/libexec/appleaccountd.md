## appleaccountd

> `/usr/libexec/appleaccountd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_acfuncs`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_catlist`
- `__DATA.__objc_stublist`
- `__DATA.__bss`

```diff

-1063.1.0.0.0
-  __TEXT.__text: 0x3d24c4
-  __TEXT.__auth_stubs: 0x2f60
-  __TEXT.__objc_stubs: 0x4a20
-  __TEXT.__objc_methlist: 0xe18
+1064.0.0.0.0
+  __TEXT.__text: 0x3e0984
+  __TEXT.__auth_stubs: 0x3360
+  __TEXT.__objc_stubs: 0x4ac0
+  __TEXT.__objc_methlist: 0xee8
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x11b60
-  __TEXT.__constg_swiftt: 0xbb2c
-  __TEXT.__swift5_typeref: 0x6fb1
+  __TEXT.__const: 0x11e40
+  __TEXT.__constg_swiftt: 0xbc44
+  __TEXT.__swift5_typeref: 0x72a1
   __TEXT.__swift5_builtin: 0x280
-  __TEXT.__swift5_reflstr: 0x6135
-  __TEXT.__swift5_fieldmd: 0x602c
+  __TEXT.__swift5_reflstr: 0x61f5
+  __TEXT.__swift5_fieldmd: 0x60d4
   __TEXT.__swift5_assocty: 0x870
-  __TEXT.__swift5_proto: 0xb90
-  __TEXT.__swift5_types: 0x5cc
-  __TEXT.__objc_classname: 0x2aad
-  __TEXT.__objc_methtype: 0x1e14
-  __TEXT.__objc_methname: 0x6f95
-  __TEXT.__swift5_capture: 0x6268
-  __TEXT.__swift5_protos: 0x1f8
-  __TEXT.__oslogstring: 0x1f50d
-  __TEXT.__cstring: 0x4269
+  __TEXT.__swift5_proto: 0xb94
+  __TEXT.__swift5_types: 0x5d4
+  __TEXT.__objc_classname: 0x2b3d
+  __TEXT.__objc_methname: 0x71e5
+  __TEXT.__objc_methtype: 0x1f04
+  __TEXT.__swift5_capture: 0x6370
+  __TEXT.__swift5_protos: 0x1fc
+  __TEXT.__oslogstring: 0x1fa0d
+  __TEXT.__cstring: 0x42d9
   __TEXT.__swift5_acfuncs: 0xa0
-  __TEXT.__swift_as_entry: 0x588
-  __TEXT.__swift_as_ret: 0x744
-  __TEXT.__swift_as_cont: 0xf90
+  __TEXT.__swift_as_entry: 0x5c8
+  __TEXT.__swift_as_ret: 0x7a0
+  __TEXT.__swift_as_cont: 0x102c
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x7c80
-  __TEXT.__eh_frame: 0x120c4
-  __DATA_CONST.__const: 0x13320
-  __DATA_CONST.__objc_classlist: 0x578
+  __TEXT.__unwind_info: 0x7ed0
+  __TEXT.__eh_frame: 0x1291c
+  __DATA_CONST.__const: 0x13650
+  __DATA_CONST.__objc_classlist: 0x580
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x180
+  __DATA_CONST.__objc_protolist: 0x1a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0xc0
-  __DATA_CONST.__auth_got: 0x17b8
-  __DATA_CONST.__got: 0x12c0
-  __DATA_CONST.__auth_ptr: 0x14a0
-  __DATA.__objc_const: 0x1c008
-  __DATA.__objc_selrefs: 0x1610
-  __DATA.__objc_data: 0x2f30
-  __DATA.__data: 0x12e28
+  __DATA_CONST.__objc_protorefs: 0xd0
+  __DATA_CONST.__auth_got: 0x19b8
+  __DATA_CONST.__got: 0x1480
+  __DATA_CONST.__auth_ptr: 0x1560
+  __DATA.__objc_const: 0x1cd00
+  __DATA.__objc_selrefs: 0x1660
+  __DATA.__objc_data: 0x2ff8
+  __DATA.__data: 0x13140
   __DATA.__objc_stublist: 0x68
   __DATA.__bss: 0x12480
-  __DATA.__common: 0x490
+  __DATA.__common: 0x498
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts
+  - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/Versions/A/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /System/Library/PrivateFrameworks/IMFoundation.framework/Versions/A/IMFoundation
   - /System/Library/PrivateFrameworks/IntelligencePlatform.framework/Versions/A/IntelligencePlatform
   - /System/Library/PrivateFrameworks/ProtectedCloudStorage.framework/Versions/A/ProtectedCloudStorage
+  - /System/Library/PrivateFrameworks/SetupKit.framework/Versions/A/SetupKit
   - /System/Library/PrivateFrameworks/StorageContainersPrivate.framework/Versions/A/StorageContainersPrivate
   - /System/Library/PrivateFrameworks/XPCDistributed.framework/Versions/A/XPCDistributed
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9643
-  Symbols:   1579
-  CStrings:  3969
+  Functions: 9783
+  Symbols:   1707
+  CStrings:  4025
 
Symbols:
+ _$s12AppleAccount10XPCCodablePAAE6decode4fromx10Foundation4DataV_tKFZ
+ _$s12AppleAccount10XPCCodablePAAE6encode10Foundation4DataVyKF
+ _$s12AppleAccount13BluetoothBaseMp
+ _$s12AppleAccount13BluetoothBaseP10invalidateyyFTj
+ _$s12AppleAccount13BluetoothBaseP10submitCode_4typeySS_AA0cD13ConfigurationV0F4TypeOtFTj
+ _$s12AppleAccount13BluetoothBaseP11stateStreamScSyAA0cD5StateOGvgTj
+ _$s12AppleAccount13BluetoothBaseP14changeCodeType2toyAA0cD13ConfigurationV0fG0O_tFTj
+ _$s12AppleAccount13BluetoothBaseP8activateSo16CUMessageSessionCyYaKFTj
+ _$s12AppleAccount13BluetoothBaseP8activateSo16CUMessageSessionCyYaKFTjTu
+ _$s12AppleAccount14RecoveryResultMp
+ _$s12AppleAccount14XPCConvertibleP4into8XPCModelQzyFTj
+ _$s12AppleAccount14XPCConvertiblePAAE6encode10Foundation4DataVyKF
+ _$s12AppleAccount18BluetoothBaseStateO25advertisingAddressRotatedyAC10Foundation4DataVcACmFWC
+ _$s12AppleAccount18BluetoothBaseStateO6pairedyA2CmFWC
+ _$s12AppleAccount18BluetoothBaseStateOMa
+ _$s12AppleAccount18BluetoothBaseStateOMn
+ _$s12AppleAccount22BluetoothStateProviderCMa
+ _$s12AppleAccount26BluetoothBaseConfigurationV15DigitCodeLengthO3sixyA2EmFWC
+ _$s12AppleAccount26BluetoothBaseConfigurationV15DigitCodeLengthOMa
+ _$s12AppleAccount26BluetoothBaseConfigurationV8CodeTypeO05digitF0yAeC05DigitF6LengthOcAEmFWC
+ _$s12AppleAccount26BluetoothBaseConfigurationV8CodeTypeOMa
+ _$s12AppleAccount26BluetoothBaseConfigurationV8CodeTypeOMn
+ _$s12AppleAccount26BluetoothBaseConfigurationV8CodeTypeOs23CustomStringConvertibleAAMc
+ _$s12AppleAccount26BluetoothBaseConfigurationVMa
+ _$s12AppleAccount26ProximityCustodianRecoveryO0D0V5StateOAA14XPCConvertibleAAMc
+ _$s12AppleAccount26ProximityCustodianRecoveryO0D0V5StateOAC0eF0AAMc
+ _$s12AppleAccount26ProximityCustodianRecoveryO0D0V5StateOMa
+ _$s12AppleAccount26ProximityCustodianRecoveryO0D0V5StateOMn
+ _$s12AppleAccount26ProximityCustodianRecoveryO0D0VAA14XPCConvertibleAAMc
+ _$s12AppleAccount26ProximityCustodianRecoveryO0D0VAC4RoleAAMc
+ _$s12AppleAccount26ProximityCustodianRecoveryO0D0VMa
+ _$s12AppleAccount26ProximityCustodianRecoveryO0D0VMn
+ _$s12AppleAccount26ProximityCustodianRecoveryO0E12FlowExecutorP07executeE017stateContinuation19custodianController13bluetoothBase9messengers6ResultOyAA0eP0_ps5Error_pGScS0J0Vy5Model_5StateQZ_G_So011AACustodianL0CAA09BluetoothN0_pAC9Messenger_ptYaFTj
+ _$s12AppleAccount26ProximityCustodianRecoveryO0E12FlowExecutorP07executeE017stateContinuation19custodianController13bluetoothBase9messengers6ResultOyAA0eP0_ps5Error_pGScS0J0Vy5Model_5StateQZ_G_So011AACustodianL0CAA09BluetoothN0_pAC9Messenger_ptYaFTjTu
+ _$s12AppleAccount26ProximityCustodianRecoveryO0E12FlowExecutorP14handleBLEState_17stateContinuationyAA18BluetoothBaseStateO_ScS0K0Vy5Model_0N0QZ_GtFTj
+ _$s12AppleAccount26ProximityCustodianRecoveryO0E12FlowExecutorP18handleSessionError_17stateContinuations6ResultOyAA0eM0_ps0J0_pGsAK_p_ScS0L0Vy5Model_5StateQZ_GtFTj
+ _$s12AppleAccount26ProximityCustodianRecoveryO0E12FlowExecutorP23shouldRetrySessionErrorySbs0K0_pFTj
+ _$s12AppleAccount26ProximityCustodianRecoveryO0E12FlowExecutorPyx5ModelQzcfCTj
+ _$s12AppleAccount26ProximityCustodianRecoveryO0E5StateP7initialxvgZTj
+ _$s12AppleAccount26ProximityCustodianRecoveryO11HasherErrorOMa
+ _$s12AppleAccount26ProximityCustodianRecoveryO11HasherErrorOs0G0AAMc
+ _$s12AppleAccount26ProximityCustodianRecoveryO3XPCO4RoleO5owneryAgC5OwnerVcAGmFWC
+ _$s12AppleAccount26ProximityCustodianRecoveryO3XPCO4RoleO9custodianyAgC0D0VcAGmFWC
+ _$s12AppleAccount26ProximityCustodianRecoveryO3XPCO4RoleOAA10XPCCodableAAMc
+ _$s12AppleAccount26ProximityCustodianRecoveryO3XPCO4RoleOMa
+ _$s12AppleAccount26ProximityCustodianRecoveryO3XPCO4RoleOMn
+ _$s12AppleAccount26ProximityCustodianRecoveryO3XPCO6ActionO17submitPairingCodeyAGSS_AA26BluetoothBaseConfigurationV0J4TypeOtcAGmFWC
+ _$s12AppleAccount26ProximityCustodianRecoveryO3XPCO6ActionO22requestManualCodeEntryyA2GmFWC
+ _$s12AppleAccount26ProximityCustodianRecoveryO3XPCO6ActionO6cancelyA2GmFWC
+ _$s12AppleAccount26ProximityCustodianRecoveryO3XPCO6ActionOAA10XPCCodableAAMc
+ _$s12AppleAccount26ProximityCustodianRecoveryO3XPCO6ActionOMa
+ _$s12AppleAccount26ProximityCustodianRecoveryO3XPCO6ResultO4fromAgA0eG0_p_tcfC
+ _$s12AppleAccount26ProximityCustodianRecoveryO3XPCO6ResultOAA10XPCCodableAAMc
+ _$s12AppleAccount26ProximityCustodianRecoveryO3XPCO6ResultOMa
+ _$s12AppleAccount26ProximityCustodianRecoveryO4RoleMp
+ _$s12AppleAccount26ProximityCustodianRecoveryO4RoleP9bleConfigAA26BluetoothBaseConfigurationVvgTj
+ _$s12AppleAccount26ProximityCustodianRecoveryO4RolePAAE18sendTelemetryEvent_5error11extraFieldsySo011AAAnalyticsI0a_s5Error_pSgSDyS2SGtF
+ _$s12AppleAccount26ProximityCustodianRecoveryO4RoleTL
+ _$s12AppleAccount26ProximityCustodianRecoveryO5OwnerV14custodianUUIDsSaySSGvg
+ _$s12AppleAccount26ProximityCustodianRecoveryO5OwnerV5StateOAA14XPCConvertibleAAMc
+ _$s12AppleAccount26ProximityCustodianRecoveryO5OwnerV5StateOAC0eG0AAMc
+ _$s12AppleAccount26ProximityCustodianRecoveryO5OwnerV5StateOMa
+ _$s12AppleAccount26ProximityCustodianRecoveryO5OwnerV5StateOMn
+ _$s12AppleAccount26ProximityCustodianRecoveryO5OwnerVAA14XPCConvertibleAAMc
+ _$s12AppleAccount26ProximityCustodianRecoveryO5OwnerVAC4RoleAAMc
+ _$s12AppleAccount26ProximityCustodianRecoveryO5OwnerVMa
+ _$s12AppleAccount26ProximityCustodianRecoveryO5OwnerVMn
+ _$s12AppleAccount26ProximityCustodianRecoveryO6HasherV25generateAdvertisementData14custodianUUIDs4with10Foundation0I0VSaySSG_AKtAC0F5ErrorOYKFZ
+ _$s12AppleAccount26ProximityCustodianRecoveryO9MessengerMp
+ _$s12AppleAccount26ProximityCustodianRecoveryO9MessengerP08registerC9Transport7sessionySo16CUMessageSessionC_tYaKFTj
+ _$s12AppleAccount26ProximityCustodianRecoveryO9MessengerP08registerC9Transport7sessionySo16CUMessageSessionC_tYaKFTjTu
+ _$s12AppleAccount26ProximityCustodianRecoveryO9MessengerP10invalidateyyFTj
+ _$s12AppleAccount26ProximityCustodianRecoveryOMn
+ _$s12AppleAccount31ProximityCustodianRecoveryErrorO19xpcConnectionFailedyA2CmFWC
+ _$s12AppleAccount31ProximityCustodianRecoveryErrorOMa
+ _$s12AppleAccount31ProximityCustodianRecoveryErrorOs0F0AAMc
+ _$s12AppleAccount34OwnerProximityRecoveryFlowExecutorCAA0d9CustodianE0O0efG0AAMc
+ _$s12AppleAccount34OwnerProximityRecoveryFlowExecutorCMa
+ _$s12AppleAccount34OwnerProximityRecoveryFlowExecutorCMn
+ _$s12AppleAccount35ProximityCustodianRecoveryMessengerC4roleACyxGx_tcfC
+ _$s12AppleAccount35ProximityCustodianRecoveryMessengerCMn
+ _$s12AppleAccount35ProximityCustodianRecoveryMessengerCyxGAA0cdE0O0F0AAMc
+ _$s12AppleAccount38CustodianProximityRecoveryFlowExecutorCAA0dcE0O0efG0AAMc
+ _$s12AppleAccount38CustodianProximityRecoveryFlowExecutorCMa
+ _$s12AppleAccount38CustodianProximityRecoveryFlowExecutorCMn
+ _$s12AppleAccount9SetupBaseC7context4base16btAddressMonitor0G13StateProviderACyxGAA09BluetoothD13ConfigurationV_xSo13CBActivatable_So013CBAdvertisingH9ReportingpAA0ljK0Ctcfc
+ _$s12AppleAccount9SetupBaseCAASo07SKSetupA14IDSignInServerCRszrlE23setAdvertisementPayloadyy10Foundation4DataVSgF
+ _$s12AppleAccount9SetupBaseCMn
+ _$s12AppleAccount9SetupBaseCyxGAA09BluetoothD0AAMc
+ _$s2os12OSSignpostIDV8rawValues6UInt64Vvg
+ _$s2os12OSSignposterV6loggerAcA6LoggerV_tcfC
+ _$s2os12OSSignposterV9logHandleSo03OS_a1_C0Cvg
+ _$s2os12OSSignposterVMa
+ _$s2os15OSSignpostErrorO9doubleEndyA2CmFWC
+ _$s2os15OSSignpostErrorOMa
+ _$s2os23OSSignpostIntervalStateC10signpostIDAA0bF0Vvg
+ _$s2os23OSSignpostIntervalStateC2id6isOpenAcA0B2IDV_Sbtcfc
+ _$s2os23OSSignpostIntervalStateCMa
+ _$s2os28checkForErrorAndConsumeState5stateAA010OSSignpostD0OAA0i8IntervalG0C_tF
+ _$s2os6LoggerV12AppleAccountE9proximityACvgZ
+ _$s5State12AppleAccount26ProximityCustodianRecoveryO4RolePTl
+ _$s8Executor12AppleAccount26ProximityCustodianRecoveryO4RolePTl
+ _$sScS10makeStream2of15bufferingPolicyScSyxG6stream_ScS12ContinuationVyx_G12continuationtxm_AG09BufferingE0Oyx__GtFZ
+ _$sScS12ContinuationV11YieldResultOMn
+ _$sScS12ContinuationV15BufferingPolicyO9unboundedyADyx__GAFmlFWC
+ _$sScS12ContinuationV15BufferingPolicyOMn
+ _$sScS12ContinuationV5yieldyAB11YieldResultOyx__GxnF
+ _$sScS12ContinuationV6finishyyF
+ _$sScS12ContinuationVMa
+ _$sScS12ContinuationVMn
+ _$sScS17makeAsyncIteratorScS0C0Vyx_GyF
+ _$sScS8IteratorV4next9isolationxSgScA_pSgYi_tYaF
+ _$sScS8IteratorV4next9isolationxSgScA_pSgYi_tYaFTu
+ _$sScS8IteratorVMn
+ _$sScSMa
+ _$sScTss5NeverORs_rlE5valuexvg
+ _$sScTss5NeverORs_rlE5valuexvgTu
+ _$sSo9OS_os_logC0B0E16signpostsEnabledSbvg
+ _$ss27_diagnoseUnexpectedEnumCase4types5NeverOxm_tlF
+ _CFAbsoluteTimeGetCurrent
+ _OBJC_CLASS_$_AACustodianController
+ _OBJC_CLASS_$_AAProximityRecoveryClientInterface
+ _OBJC_CLASS_$_CBAdvertiser
+ _OBJC_CLASS_$_SKSetupAppleIDSignInClient
+ _OBJC_CLASS_$_SKSetupAppleIDSignInServer
+ __os_signpost_emit_with_name_impl
+ _kAAAnalyticsEventRCOwnerPrivateChannelCreated
+ _swift_getAssociatedTypeWitness
CStrings:
+ "?"
+ "@\"<AACustodianDaemonProtocol>\"24@0:8@?<v@?@\"NSError\">16"
+ "@\"<AAProximityRecoveryClientProtocol>\"16@0:8"
+ "@24@0:8@?16"
+ "AACustodianDaemonConnectionProviding"
+ "AAProximityRecoveryClientProtocol"
+ "Activating BLE transport"
+ "BEGIN [%llu]: %{public}s"
+ "BLE state monitoring ended"
+ "BLE transport activated successfully, registering with messenger"
+ "Custodian XPC connection invalidated — cleaning up proximity session"
+ "END [%llu] %.*fs: %{public}s"
+ "END [%llu] %.*fs: %{public}s error: %@"
+ "Failed to decode proximity action"
+ "Failed to encode proximity state for XPC: %@ — state update dropped"
+ "Failed to update advertisement payload: %@"
+ "Failed to update advertisement payload: model or bluetoothBase type mismatch (model: %s, bluetoothBase: %s)"
+ "Peer disconnected during pairing — restarting BLE session"
+ "Proximity action received but no active session"
+ "Proximity transport registered with messenger"
+ "ProximityCustodianRecovery"
+ "ProximityCustodianRecovery.Session deinitializing"
+ "ProximityCustodianRecovery.Session<%s> initialized"
+ "ProximityRecoverySession cancelled"
+ "Requesting manual code entry for BLE pairing"
+ "Session failed with unexpected error: %@"
+ "Starting BLE state monitoring"
+ "Starting executor: %s"
+ "Starting recovery flow execution for %s"
+ "Submitting pairing code to BLE transport (type: %s)"
+ "T@\"<AAProximityRecoveryClientProtocol>\",N,W,VproximityRecoveryStateDelegate"
+ "T@\"<AAProximityRecoveryClientProtocol>\",W,N"
+ "XPC client proxy error during proximity recovery: %@"
+ "[Error] Interval already ended"
+ "_TtC13appleaccountd33CustodianDaemonConnectionProvider"
+ "activeProximitySession"
+ "appleaccountd.CustodianDaemonConnectionProvider"
+ "bluetoothBase"
+ "custodianController"
+ "didReceiveProximityRecoveryState:"
+ "executor"
+ "initWithDaemonConnectionProvider:analyticsReporter:"
+ "model"
+ "proximityRecoveryStateDelegate"
+ "remoteObjectProxyWithErrorHandler:"
+ "sendProximityAction:"
+ "setInvalidationHandler:"
+ "setProximityRecoveryStateDelegate:"
+ "setRemoteObjectInterface:"
+ "startProximityRecoveryWithData:completion:"
+ "stateContinuation"
+ "stateStream"
+ "synchronousRemoteObjectProxyWithErrorHandler:"
+ "v24@0:8@\"<AAProximityRecoveryClientProtocol>\"16"
+ "v24@0:8@\"NSData\"16"
+ "v32@0:8@\"NSData\"16@?<v@?@\"NSData\"@\"NSError\">24"
```
