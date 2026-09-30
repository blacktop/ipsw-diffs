## com.apple.iokit.IOHDCPFamily

> `com.apple.iokit.IOHDCPFamily`

```diff

-65.0.0.0.0
+68.0.0.0.0
   __TEXT.__const: 0x38
-  __TEXT.__cstring: 0x4553
-  __TEXT.__os_log: 0x162e
-  __TEXT_EXEC.__text: 0xef6c
+  __TEXT.__cstring: 0x4547
+  __TEXT.__os_log: 0x1626
+  __TEXT_EXEC.__text: 0xf45c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x178

   __DATA_CONST.__mod_term_func: 0x48
   __DATA_CONST.__const: 0x2b50
   __DATA_CONST.__kalloc_type: 0x340
-  UUID: 251DF82C-4C91-350B-B9F4-F22FE557AEFD
-  Functions: 353
-  Symbols:   937
+  UUID: 020FD095-22C3-30AE-9886-EF4BDB2247F4
+  Functions: 382
+  Symbols:   974
   CStrings:  557
 
Symbols:
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _ZN15IOHDCPInterface11handleStartEP9IOService.cold.1
+ _ZN15IOHDCPInterface13hdcpInterfaceEP6OSDataP12OSDictionaryS3_y.cold.1
+ _ZN15IOHDCPInterface13hdcpInterfaceEP9IOService14IOHDCPProtocol16IOHDCPDeviceRolejy.cold.1
+ _ZN15IOHDCPInterface13hdcpInterfaceEP9IOService14IOHDCPProtocol16IOHDCPDeviceRolejy.cold.2
+ _ZN15IOHDCPInterface13hdcpInterfaceEP9IOService14IOHDCPProtocol16IOHDCPDeviceRolejy.cold.3
+ _ZN15IOHDCPInterface13hdcpInterfaceEP9IOService14IOHDCPProtocol16IOHDCPDeviceRolejy.cold.4
+ _ZN15IOHDCPInterface13hdcpInterfaceEP9IOService14IOHDCPProtocol16IOHDCPDeviceRolejy.cold.5
+ _ZN15IOHDCPInterface13hdcpInterfaceEP9IOService14IOHDCPProtocol16IOHDCPDeviceRolejy.cold.6
+ _ZN15IOHDCPInterface5startEP9IOService.cold.1
+ _ZN18IOHDCP2AuthSession11setWorkLoopEP10IOWorkLoop.cold.3
+ _ZN18IOHDCP2AuthSession11setWorkLoopEP10IOWorkLoop.cold.4
+ _ZN18IOHDCP2AuthSession23messageCountWaitForZeroEv.cold.1
+ _ZN18IOHDCP2AuthSession4initEP8OSObjectPFvS1_P17IOHDCPAuthSessionEP22IOHDCPMessageTransportP15IOHDCPInterface.cold.1
+ _ZN26IOHDCP2ReceiverAuthSession16fillAKE_Send_rrxEPN14IOHDCP2Message12AKE_Send_rrxE.cold.1
+ _ZN26IOHDCP2ReceiverAuthSession17fillAKE_Send_CertEPN14IOHDCP2Message13AKE_Send_CertE.cold.1
+ _ZN26IOHDCP2ReceiverAuthSession17takeAKE_Stored_kmEPN14IOHDCP2Message13AKE_Stored_kmE.cold.1
+ _ZN26IOHDCP2ReceiverAuthSession19fillLC_Send_L_primeEPN14IOHDCP2Message15LC_Send_L_primeE.cold.1
+ _ZN26IOHDCP2ReceiverAuthSession20takeAKE_No_Stored_kmEPN14IOHDCP2Message16AKE_No_Stored_kmE.cold.1
+ _ZN26IOHDCP2ReceiverAuthSession25fillAKE_Send_Pairing_InfoEPN14IOHDCP2Message21AKE_Send_Pairing_InfoE.cold.1
+ _ZN28IOHDCP2LocalMessageTransport11takeMessageEP14IOHDCP2Message.cold.1
+ _ZN29IOHDCP2TransmitterAuthSession11fillLC_InitEPN14IOHDCP2Message7LC_InitE.cold.1
+ _ZN29IOHDCP2TransmitterAuthSession15hPrimeAvailableEv.cold.1
+ _ZN29IOHDCP2TransmitterAuthSession16takeAKE_Send_rrxEPN14IOHDCP2Message12AKE_Send_rrxE.cold.1
+ _ZN29IOHDCP2TransmitterAuthSession17takeAKE_Send_CertEPN14IOHDCP2Message13AKE_Send_CertE.cold.1
+ _ZN29IOHDCP2TransmitterAuthSession20fillAKE_No_Stored_kmEPN14IOHDCP2Message16AKE_No_Stored_kmE.cold.1
+ _ZN29IOHDCP2TransmitterAuthSession20pairingInfoAvailableEv.cold.1
+ _ZN29IOHDCP2TransmitterAuthSession23receiverIDListAvailableEv.cold.1
+ _ZN29IOHDCP2TransmitterAuthSession25takeAKE_Send_Pairing_InfoEPN14IOHDCP2Message21AKE_Send_Pairing_InfoE.cold.1
+ _ZN31IOHDCP2DPTransmitterAuthSession17takeAKE_Send_CertEPN14IOHDCP2Message16DP_AKE_Send_CertE.cold.1
+ _ZN31IOHDCP2DPTransmitterAuthSession20fillAKE_No_Stored_kmEPN14IOHDCP2Message16AKE_No_Stored_kmE.cold.1
+ _ZN31IOHDCP2DPTransmitterAuthSession25fillRepeaterAuth_Send_AckEPN14IOHDCP2Message21RepeaterAuth_Send_AckE.cold.1
+ _ZN31IOHDCP2DPTransmitterAuthSession29takeRepeaterAuth_Stream_ReadyEPN14IOHDCP2Message25RepeaterAuth_Stream_ReadyE.cold.1
+ __ZN15IOHDCPInterface12consumeNewKmE14IOHDCP_EKpubKm
- _ZN31IOHDCP2DPTransmitterAuthSession37takeRepeaterAuth_Send_ReceiverID_ListEPN14IOHDCP2Message36DP_RepeaterAuth_Send_ReceiverID_ListE.cold.1
- _ZN31IOHDCP2DPTransmitterAuthSession37takeRepeaterAuth_Send_ReceiverID_ListEPN14IOHDCP2Message36DP_RepeaterAuth_Send_ReceiverID_ListE.cold.2
- __ZN15IOHDCPInterface16writeEncryptedKmE14IOHDCP_EKpubKm
CStrings:
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOHDCPFamily/IOHDCP2AuthSession.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOHDCPFamily/IOHDCP2DPTransmitterAuthSession.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOHDCPFamily/IOHDCP2LocalMessageTransport.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOHDCPFamily/IOHDCP2ReceiverAuthSession.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOHDCPFamily/IOHDCP2TransmitterAuthSession.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOHDCPFamily/IOHDCPAuthSession.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IOHDCPFamily/IOHDCPInterface.cpp"
+ "after consumeNewKm: E_kpub_km[%zu] = { %*D }\n"
+ "before consumeNewKm: E_kpub_km[%zu] = { %*D }\n"
+ "ret = getInterface()->consumeNewKm(AKE_No_Stored_km->E_kpub_km) == 0 "
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/IOHDCPFamily/IOHDCP2AuthSession.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/IOHDCPFamily/IOHDCP2DPTransmitterAuthSession.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/IOHDCPFamily/IOHDCP2LocalMessageTransport.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/IOHDCPFamily/IOHDCP2ReceiverAuthSession.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/IOHDCPFamily/IOHDCP2TransmitterAuthSession.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/IOHDCPFamily/IOHDCPAuthSession.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/IOHDCPFamily/IOHDCPInterface.cpp"
- "after writeEncryptedKm: E_kpub_km[%zu] = { %*D }\n"
- "before writeEncryptedKm: E_kpub_km[%zu] = { %*D }\n"
- "ret = getInterface()->writeEncryptedKm(AKE_No_Stored_km->E_kpub_km) == 0 "

```
