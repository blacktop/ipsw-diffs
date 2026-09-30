## libWISSupport.dylib

> `/usr/lib/libWISSupport.dylib`

```diff

-283.0.0.0.0
-  __TEXT.__text: 0x287fc sha256:fb0b48ad116e4dddd5b3f639ad835979eac774afe7df90aa302513b9a96e96d7
-  __TEXT.__auth_stubs: 0x880 sha256:c4e52d4d0388013c309d04bf9dc6fe3697f41c9dca8dcfd1757c9df3793199ca
-  __TEXT.__gcc_except_tab: 0x309c sha256:ebd6992997f562edd6b3c7c7fa3923226b12d0a23d8557d2e73bb7d9dcac414f
-  __TEXT.__cstring: 0x638 sha256:abf43335baabe76fdcb947f4baeed7d02dd58c156e7698e3012fea273b5fd555
-  __TEXT.__const: 0xdfa sha256:f59dc45acd688246be1ae9e810f2fba63ff105a5bb81b1d32da6b3506635b467
+335.0.0.0.0
+  __TEXT.__text: 0x281fc sha256:6c95f8acb94ab85ac874533ed613d6c5799e4702ddc7f7f89e1981b6c1b7aae6
+  __TEXT.__gcc_except_tab: 0x2fdc sha256:2218ea6db583c597d5aaed8b86f580debe17bd239725020a6283e025b1b0c01f
+  __TEXT.__cstring: 0x710 sha256:640874852feec002ac2397742a57de179294055a96794d6e235a1d51e1fd5008
+  __TEXT.__const: 0xdfb sha256:cd13ff95688b6e5bad97cc8c94ffb614ab0f6f5dc0d92aa74cc1140f1cc7b887
   __TEXT.__oslogstring: 0x7a sha256:cc4eb59657ea1280797cb3fda85a6707e65de1fec59fe8584e23a4cb5f7247a5
-  __TEXT.__unwind_info: 0x11c8 sha256:e6a06facc53cfd6672aa89b3ae5d0b7ed6083f8dcf22a6b80c49fc56ba58f7b0
-  __DATA_CONST.__got: 0xb0 sha256:633fbd28ecd9f37ea3d9ef0b9044d8234ab96b8b74b2752f4f4df9ec49db10a5
-  __DATA_CONST.__const: 0x138 sha256:81c230c21ae0c843f1fc316304169d88532e89fa199b1287e4891c739d43dcde
-  __AUTH_CONST.__auth_got: 0x448 sha256:42244758ae3f6345ca6dc08e45c625003589519b9bcfcbc7f6b92b2a2744e09f
-  __AUTH_CONST.__const: 0x1580 sha256:9a1b64ebe9c79291d000aa18cca1e09127ed8e2483f20a38f5a31394380ef90f
-  __AUTH_CONST.__cfstring: 0x180 sha256:97d03e8faf1b9c1d6137de45cc2b64ab3111ae4768f6fe4de2af4c87c07daa63
+  __TEXT.__unwind_info: 0x1238 sha256:a2ebf9ff286d153bf5a94bbe534d014dde035bfba3d12b3099fcda0de22a3fa1
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x160 sha256:aa4534f7cd7c85050364120d434d18bbfb8d61d53c7c36f499f5a01a03aa24ab
+  __DATA_CONST.__weak_got: 0x8 sha256:12c913733859c0e4217f18f19ac6dd650e1008891e1bda30011c56564326abea
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x1580 sha256:61343b0b148c67ff2e73fbd59fd55aaccbacf283ecce6ddbaa51eede2bdade89
+  __AUTH_CONST.__cfstring: 0x220 sha256:d375f72f92f0135d214dd725a254361f93a01b3c2f60e729d2dd2c71d4560afb
+  __AUTH_CONST.__weak_auth_got: 0x18 sha256:c4f685488ee12499860f131fd37a6f4fe49fe5255e7ca8c7761452c34ebde4a0
+  __AUTH_CONST.__auth_got: 0x0
+  __DATA.__data: 0x28 sha256:77bf8686a9075f5e6fc7ab8d31d6fcbd2aca6271a258faf7cad9613c370162f2
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libprotobuf-lite.dylib
-  UUID: 680BCB76-832D-332A-9DF8-4364AC3EAC60
-  Functions: 810
-  Symbols:   312
-  CStrings:  153
+  UUID: 735F359A-81A2-3BBD-96F4-983569D4D231
+  Functions: 822
+  Symbols:   322
+  CStrings:  168
 
Symbols:
+ __ZN3wis23kWISAnomalyLearnMoreKeyE
+ __ZN3wis24kWISAnomalyResolutionKeyE
+ __ZN3wis25kWISAnomalyCarrierNameKeyE
+ __ZN3wis37kWISAnomalySubCategoryOutageConfirmedE
+ __ZN3wis37kWISAnomalySubCategoryOutagePotentialE
+ __ZN3wis44WISCellularOutageAwarenessDataRequestMessageE
+ __ZN3wis46WISCellularQualityGetCurrentDataRequestMessageE
+ __ZN3wis49WISCellularQualityDataAvailabilityCallbackMessageE
+ __ZN3wis64WISCellularQualityRegisterDataAvailabilityCallbackRequestMessageE
+ __ZN3wis66WISCellularQualityUnregisterDataAvailabilityCallbackRequestMessageE
CStrings:
+ "CarrierName"
+ "GetCellularOutageDetails"
+ "GetCurrentData"
+ "LearnMore"
+ "OutageConfirmed"
+ "OutagePotential"
+ "RegisterDataAvailabilityCallback"
+ "Resolution"
+ "UnregisterDataAvailabilityCallback"
+ "WISCellularQualityDataAvailabilityCallback"

```
