## libnwswifttls.dylib

> `/usr/lib/libnwswifttls.dylib`

```diff

 108.100.36.0.0
-  __TEXT.__text: 0xe8880
-  __TEXT.__auth_stubs: 0x2110
+  __TEXT.__text: 0xe8850
+  __TEXT.__auth_stubs: 0x2100
   __TEXT.__objc_methlist: 0x5ac
   __TEXT.__const: 0x6d84
   __TEXT.__cstring: 0x1476

   __TEXT.__swift5_builtin: 0xc8
   __TEXT.__swift5_mpenum: 0x68
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x2550
-  __TEXT.__eh_frame: 0x3b88
+  __TEXT.__unwind_info: 0x2548
+  __TEXT.__eh_frame: 0x3b60
   __TEXT.__objc_classname: 0x1d3
   __TEXT.__objc_methname: 0x11ed
   __TEXT.__objc_methtype: 0x6b2

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x300
   __DATA_CONST.__objc_protorefs: 0x18
-  __AUTH_CONST.__auth_got: 0x1098
+  __AUTH_CONST.__auth_got: 0x1090
   __AUTH_CONST.__const: 0x2f08
   __AUTH_CONST.__cfstring: 0x40
   __AUTH_CONST.__objc_const: 0x2070

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 413811CA-3918-380C-9863-7BB07CE07B99
-  Functions: 3326
-  Symbols:   12047
+  UUID: 004C2E35-FCC0-35F6-AC75-2784E47166CD
+  Functions: 3325
+  Symbols:   12044
   CStrings:  747
 
Symbols:
+ _$s15SwiftTLSLibrary4EPSKVWObTm
+ _$s9CryptoKit4HMACV18authenticationCode3for5usingAA020HashedAuthenticationE0VyxGqd___AA12SymmetricKeyVt10Foundation12DataProtocolRd__lFZ
- _$s15SwiftTLSLibrary11GeneralEPSKVWObTm
- _$s9CryptoKit4HMACV18authenticationCode3for5usingAA020HashedAuthenticationE0VyxGSW_AA12SymmetricKeyVtFZ
- _objc_retain_x9
Functions:
~ ___nwswifttls_configure_with_sec_protocol_options_block_invoke : 2004 -> 1996
~ _$s10nwswifttls20STLSClientHandshakerC14startHandshakeSo6NSDataCSgyF : 1812 -> 1852
~ _$s10nwswifttls20STLSClientHandshakerC17continueHandshakeySo6NSDataCSgAGF : 2996 -> 3036
~ _$s15SwiftTLSLibrary21HandshakeStateMachineV05startC0AA07PartialC6ResultVyAA8TLSErrorOYKF : 12276 -> 12324
~ _$s15SwiftTLSLibrary14HandshakeStateO011ServerHelloD0V08originalD006serverF00hF5Bytes5clockAeC06ClientfD0V_AA0eF0VAA10ByteBufferVxtAA8TLSErrorOYKcAA0A8TLSClockRzlufC : 17092 -> 17080
- _$s9CryptoKit4HMACV15SwiftTLSLibraryE18authenticationCode5bytes5usingAA020HashedAuthenticationG0VyxGqd___AA12SymmetricKeyVt10Foundation15ContiguousBytesRd__lFZAJSWXEfU_AA6SHA384V_AA0Q6DigestVTg5TA
~ ___nwswifttlsrecord_configure_with_sec_protocol_options_block_invoke : 2100 -> 2092
~ _$s10nwswifttls17STLSRecordHandlerC_4alpn12sessionState13ticketRequest11pakeContext0I14ClientIdentity0i6ServerL00iK16PasswordVerifier6logStrACSgSo8NSStringCSg_So7NSArrayCSgSo6NSDataCSgSays5UInt8VGSgA4tNtcfc : 6216 -> 6212
~ _$s10nwswifttls17STLSRecordHandlerC_4alpn11pakeContext0E14ClientIdentity0e6ServerH00E16PasswordVerifier6logStrACSgSo8NSStringCSg_So7NSArrayCSgSo6NSDataCA3rLtcfc : 3620 -> 3648
~ _$s10nwswifttls17STLSRecordHandlerC18addApplicationDatayy10Foundation0F0VF : 940 -> 952
~ _$s10nwswifttls17STLSRecordHandlerC18processNetworkData07networkF2Iny10Foundation0F0V_tF : 1440 -> 1484
~ _$s10nwswifttls17STLSRecordHandlerC9getOutput10Foundation4DataVSgyF : 1076 -> 1092
~ _$s10nwswifttls17STLSRecordHandlerC9getOutput8numBytes10Foundation4DataVSgSi_tF : 1096 -> 1116
~ _$s10nwswifttls17STLSRecordHandlerC12getErrorCodes5Int32VyF : 3156 -> 3136
~ _$s10nwswifttls17STLSRecordHandlerC_10serverName4alpn12sessionState13ticketRequest16keyExchangeGroup20externalPreSharedKey15rawEPSKsEnabled15enableEarlyData23pakeClientConfiguration6logStrACSgSo7NSArrayCSg_So8NSStringCSgAQSo6NSDataCSgSays5UInt8VGSgs6UInt16VSgSo016SwiftTLSExternalopQ0CSgS2b15SwiftTLSLibrary010PAKEClientZ0VSgAStcfcTf4ggggnngnnggn_n : 2900 -> 2952
~ _$s10nwswifttls17STLSRecordHandlerC_9serverKey4alpn5EPSKs18epskSelectionBlock03rawG7Enabled17pakeServerRecords0mn9ChallengeJ015enableEarlyData6logStrACSgSo8NSStringCSg_So03SecE3RefaSgSo7NSArrayCSgSaySo025SwiftTLSExternalPreSharedE0CGSgySaySo0Z14TLSOfferedEPSKCG_ySo0w17ExternalPreSharedE0CSgctcSgSbSay0Z10TLSLibrary16PAKEServerRecordVGSgySo0Z22TLSOfferedPAKEIdentityC_ySo15OS_sec_identity_pSgctcSgSbAOtcfcTf4gggngnngngn_n : 2384 -> 2468
~ _$s10nwswifttls20STLSServerHandshakerC17continueHandshakeySo6NSDataCSgAGF : 4660 -> 4704
~ _$s15SwiftTLSLibrary27ServerHandshakeStateMachineV5epsks21epskSelectionCallback13configurationACSayAA4EPSKVG_ySayAA0a7OfferedL0VG_ySi_AHSgtctcSgAC13ConfigurationVtAA8TLSErrorOYKcfC : 3100 -> 3164
~ _$s15SwiftTLSLibrary27ServerHandshakeStateMachineV20logUnexpectedMessage33_FF812F446598104118BFC43FA404A9AFLL7messageyAA0dI0O_tF : 924 -> 908
~ _$s15SwiftTLSLibrary18TLSRecordProtectorV7protect9plaintext17actualContentType13paddingLengthAA13TLSCiphertextVSays5UInt8VG_AA0hI0VSitAA8TLSErrorOYKF : 1552 -> 1544
~ _$s15SwiftTLSLibrary21HandshakeStateMachineV13ConfigurationV4hash4intoys6HasherVz_tF : 680 -> 760
~ _$s15SwiftTLSLibrary20ServerHandshakeStateO011ClientHelloE0V07readingfG008originalE006clientG00jG5Bytes28externalPSKSelectionCallback15transportIsQUICAeC04IdleE0V_AA0fG0VAA10ByteBufferVySayAA0A11OfferedEPSKVG_ySi_AA0V0VSgtctcSgSbtAA8TLSErrorOYKFZ : 10076 -> 10072
~ _$s15SwiftTLSLibrary20ServerHandshakeStateO19ClientHelloVerifierV12negotiatePSK14externalPSKKDFAE20negotiatedEPSKResultVSgAA16TLSKDFIdentifierV_tAA8TLSErrorOYKF : 9780 -> 9792
~ _$s15SwiftTLSLibrary21HandshakeStateMachineV28generateHMACForAuthenticator10transcript3keyAA10ByteBufferVSgAH_9CryptoKit12SymmetricKeyVtF : 1188 -> 928
~ _$s15SwiftTLSLibrary21HandshakeStateMachineV20logUnexpectedMessage33_0FE61F88EEA52334A02606E049165857LL7messageyAA0cH0O_tF : 1284 -> 1256
~ _$s9CryptoKit4HMACV15SwiftTLSLibraryE18authenticationCode5bytes5usingAA020HashedAuthenticationG0VyxGqd___AA12SymmetricKeyVt10Foundation15ContiguousBytesRd__lFZAJSWXEfU_AA6SHA384V_AA0Q6DigestVTg5 : 160 -> 180
~ _$s15SwiftTLSLibrary14HandshakeStateO05ReadyD0V28generateHMACForAuthenticator10transcript3keyAA10ByteBufferVAJ_9CryptoKit12SymmetricKeyVtF : 1000 -> 772
~ _$s15SwiftTLSLibrary15PAKEClientStateV18processServerHelloyyAA9ExtensionO4PAKEO010PAKEServerG0VAA8TLSErrorOYKF : 1080 -> 1088
~ _$s15SwiftTLSLibrary15PAKEClientStateV15deriveSharedKey33_D47F730883CC8E2AE40D0B8BEB52DCE8LLy9CryptoKit09SymmetricG0V10Foundation4DataVAA8TLSErrorOYKF : 2640 -> 2636
~ _$s15SwiftTLSLibrary10ByteBufferV11writeRecordySixAA17TLSRecordProtocolRzlFAA13TLSCiphertextV_Tg5 : 1156 -> 1152
~ _$s15SwiftTLSLibrary16TLSRecordHandlerV15sendCloseNotifyyyF : 628 -> 672
~ _$s15SwiftTLSLibrary16TLSRecordHandlerV18processNetworkData07networkG2InyAA10ByteBufferVz_tAA8TLSErrorOYKF : 1800 -> 1792
~ _$s9CryptoKit4HMACV15SwiftTLSLibraryE18authenticationCode5bytes5usingAA020HashedAuthenticationG0VyxGqd___AA12SymmetricKeyVt10Foundation15ContiguousBytesRd__lFZAJSWXEfU_TA : 52 -> 120

```
