## accessoryd

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/Support/accessoryd`

```diff

-1025.40.1.0.0
-  __TEXT.__text: 0x1956ac
+1025.40.2.0.0
+  __TEXT.__text: 0x1a27d4
   __TEXT.__auth_stubs: 0x17d0
-  __TEXT.__objc_stubs: 0x8a00
+  __TEXT.__objc_stubs: 0x8a20
   __TEXT.__objc_methlist: 0x5798
-  __TEXT.__const: 0x2038
-  __TEXT.__cstring: 0xb9e8
-  __TEXT.__oslogstring: 0x3385e
+  __TEXT.__const: 0x2048
+  __TEXT.__cstring: 0xc05c
+  __TEXT.__oslogstring: 0x351d2
   __TEXT.__gcc_except_tab: 0x1de4
   __TEXT.__objc_methname: 0xf08c
   __TEXT.__objc_classname: 0x1025
   __TEXT.__objc_methtype: 0x2f7c
   __TEXT.__ustring: 0x232
-  __TEXT.__unwind_info: 0x3540
+  __TEXT.__unwind_info: 0x35e0
   __DATA_CONST.__auth_got: 0xbf8
-  __DATA_CONST.__got: 0xb70
-  __DATA_CONST.__auth_ptr: 0xb0
-  __DATA_CONST.__const: 0x6450
-  __DATA_CONST.__cfstring: 0x6720
+  __DATA_CONST.__got: 0xb88
+  __DATA_CONST.__auth_ptr: 0xb8
+  __DATA_CONST.__const: 0x65e0
+  __DATA_CONST.__cfstring: 0x6900
   __DATA_CONST.__objc_classlist: 0x308
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x180

   __DATA_CONST.__objc_arrayobj: 0x108
   __DATA_CONST.__objc_intobj: 0xd8
   __DATA.__objc_const: 0xd028
-  __DATA.__objc_selrefs: 0x3000
+  __DATA.__objc_selrefs: 0x3008
   __DATA.__objc_ivar: 0x718
   __DATA.__objc_data: 0x1e50
-  __DATA.__data: 0x1a98
+  __DATA.__data: 0x1aa0
   __DATA.__bss: 0x10b8
   __DATA.__common: 0x24
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 6099
-  Symbols:   42038
-  CStrings:  7883
+  Functions: 6221
+  Symbols:   42860
+  CStrings:  8048
 
Symbols:
+ _mfi4Auth_relay_handle_AccessoryInformationUpdate.cold.12
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_shift_left_arm64.o)
+ mfi4Auth_relay_handle_iAP2RelayRemote.cold.20
+ t56_protocol_start.cold.2
+ _t56_util_cleanup
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cczp_common.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_cp256_asm.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cc_try_abort.o)
+ acc_manager_checkForInductiveCTA.cold.9
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccrng_schedule.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_cp256.o)
+ _t56_protocol_handleRequest_POLL.cold.3
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccdrbg_nistctr.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccmode_ccm_reset.o)
+ _kCFACCUserDefaultsKey_PretendNFCAuthTimeout
+ acc_manager_checkForInductiveCTA.cold.6
+ _t56_endpoint_sendOutgoingData
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_cmp-500c58650b2463f61cd9d5df32539886.o)
+ acc_manager_checkForInductiveCTA.cold.10
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cccbc.o)
+ _acc_auth_protocol_handleSessionAuthenticationState.cold.2
+ _mfi4Auth_relay_initMessage_DeviceiAP2RelayRemote_RequestAccessoryInfoUpdate
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccder_blob_encode_len.o)
+ _CFDictionaryApplierFunction_findInductiveCTADonorCapableConnection.cold.1
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccder_blob_decode_uint64.o)
+ t56_protocol_checkValidMessageHeaderAndSize.cold.4
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccmode_ccm_finalize.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_mul1.o)
+ ___block_descriptor_52_e8_32s40r_e237_B24?0^{ACCConnection_s=^{__CFString}i^{__CFString}?Q^{__CFDictionary}{?=[5i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8r40l8
+ _t56_protocol_handleRequest_DATA.cold.5
+ _mfi4Auth_relay_handle_AccessoryInformationUpdate.cold.9
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_sign_composite.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccder_blob_encode_body_tl.o)
+ mfi4Auth_protocol_handle_AuthCert.cold.20
+ /Library/Caches/com.apple.xbs/Sources/CoreAccessories/Apple/accessoryd/Platform_Protocol_Implementations/t56/
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_sign_internal.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccdigest.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_export_pub.o)
+ _CFDictionaryApplierFunction_findInductiveCTAReceiverCapableConnection.cold.4
+ _CFDictionaryApplierFunction_findInductiveAuthEndpoint.cold.1
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccaes_cbc_encrypt_mode.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cc_lock.o)
+ _t56_protocol_msgTypeString
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_mux.o)
+ _t56_endpoint_dispatchQueueFinalizer.cold.1
+ t56_endpoint_sendOutgoingData.cold.3
+ mfi4Auth_relay_StartRelayForT56.cold.8
+ _t56_protocol_handleResponse_DATA.cold.7
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_signature_r_s_size.o)
+ _t56_protocol_handleResponse_STATUS.cold.2
+ /Library/Caches/com.apple.xbs/Sources/CoreAccessories/Common/AccessoryCore/t56/
+ _t56_protocol_handleRequest_DATA.cold.1
+ acc_manager_checkForInductiveCTA.cold.8
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccaes_ccm_encrypt_mode.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cccmac_generate_subkey.o)
+ t56_protocol_checkValidMessageHeaderAndSize.cold.3
+ _t56_protocol_handleRequest_DATA.cold.2
+ __t56_protocol_handleResponse_STATUS
+ t56_util_ios_getT56Endpoint.cold.1
+ __mfi4Auth_endpoint_firstUnlockHandler
+ _t56_protocol_handleResponse_DISCOVER_RSP.cold.6
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_common.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_generate_key_fips.o)
+ ___block_descriptor_61_e8_32s40s48r_e237_B24?0^{ACCConnection_s=^{__CFString}i^{__CFString}?Q^{__CFDictionary}{?=[5i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8s40l8r48l8
+ t56_util_cancelTimer.cold.3
+ t56_endpoint_sendOutgoingData.cold.5
+ t56_protocol_checkValidMessageHeaderAndSize.cold.1
+ acc_manager_checkForInductiveCTA.cold.3
+ accAuthProtocol_endpoint_publish.cold.7
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccmode_ccm_encrypt.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccm-decrypt-3d98bad873178684405c1aebec7e8538.o)
+ t56_protocol_initMsg_DATA.cold.1
+ mfi4Auth_relay_StartRelayForType.cold.15
+ /Library/Caches/com.apple.xbs/Sources/CoreAccessories/PublicShared/t56/
+ t56_protocol_initMsg_DISCOVER.cold.2
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_subn.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_shift_right-d9572f405a1bc8758eb209492b4b0148.o)
+ _t56_protocol_handleRequest_SESSION.cold.1
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccrng_static.o)
+ __CFDictionaryApplierFunction_findInductiveCTAReceiverCapableConnection
+ /Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessoryd.build/Objects-normal/arm64e/t56_util_ios.o
+ acc_connection_setProperty.cold.5
+ t56_endpoint_sendOutgoingDataCF.cold.8
+ _t56_protocol_handleRequest_DISCOVER.cold.4
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccder_sizeof_tag.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_sqr.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccsigma_mfi.o)
+ _t56_protocol_handleRequest_SESSION.cold.5
+ _t56_endpoint_handleMessage.cold.1
+ t56_util_ios_getT56Endpoint.cold.3
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_add-6bbaf80cd023f341e4d7979b160719af.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccsha1_vng_arm.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_pairwise_consistency_check.o)
+ _t56_protocol_handleRequest_DISCOVER.cold.3
+ _mfi4Auth_relay_handle_AccessoryInformationUpdate.cold.1
+ _acc_endpoint_copyParentEndpointUUID
+ mfi4Auth_relay_StartRelayForT56.cold.4
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccsha256_di.o)
+ _t56_protocol_handleRequest_TERMINATE.cold.4
+ _t56_protocol_handleResponse_DISCOVER_RSP.cold.3
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_x963_import_pub.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_double.o)
+ _t56_protocol_handleRequest_POLL.cold.4
+ _t56_protocol_handleRequest_SESSION.cold.2
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cczp_from.o)
+ _acc_policies_nfcTagUseKeys
+ acc_manager_checkForInductiveCTA.cold.11
+ mfi4Auth_relay_initMessage_DeviceiAP2RelayRemote_RequestAccessoryInfoUpdate.cold.4
+ t56_endpoint_sendOutgoingDataCF.cold.9
+ _T56Protocol_timeoutCallback.cold.1
+ t56_protocol_timeoutForRequest.cold.2
+ _mfi4Auth_relay_StartRelayForType
+ _t56_protocol_handleRequest_SESSION.cold.3
+ _kCFACCProperties_Endpoint_ParentEndpointUUID
+ acc_manager_checkForInductiveCTA.cold.4
+ _t56_protocol_sendData
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libCoreTrust.a(DERUtils.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_cmp-arm64.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccaes_vng_ccm_encrypt.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cccmac_final.o)
+ mfi4Auth_relay_StartRelayForType.cold.2
+ t56_endpoint_sendOutgoingDataCF.cold.3
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_twin_mult.o)
+ _t56_protocol_handleResponse_DATA.cold.4
+ _t56_protocol_handleRequest_DATA.cold.4
+ acc_manager_checkForInductiveCTA.cold.1
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_cp521.o)
+ _mfi4Auth_relay_handle_AccessoryInformationUpdate.cold.7
+ mfi4Auth_relay_StartRelayForType.cold.8
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Policy.o)
+ mfi4Auth_relay_StartRelayForT56.cold.10
+ mfi4Auth_relay_StartRelayForType.cold.9
+ mfi4Auth_relay_StartRelayForType.cold.4
+ _t56_protocol_handleResponse_DATA.cold.8
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_cond_add.o)
+ _t56_util_notifyRxID
+ t56_util_callbackOnTimer.cold.2
+ t56_endpoint_sendOutgoingData.cold.1
+ t56_protocol_initMsg_STATUS.cold.2
+ __t56_endpoint_handleMessage
+ _t56_protocol_handleResponse_STATUS.cold.1
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccdrbg_df.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_divmod.o)
+ _t56_protocol_init
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_compressed_x962_export_pub.o)
+ mfi4Auth_relay_StartRelayForType.cold.13
+ mfi4Auth_relay_StartRelayForType.cold.3
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccrng_crypto.o)
+ _kCFACCProperties_Connection_Inductive_RxID
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_write_uint.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ctr-arm64.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cczp_mul.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_generate_key_internal_fips.o)
+ t56_protocol_processIncomingData.cold.5
+ mfi4Auth_protocol_processIncomingMessageRelay.cold.22
+ _t56_protocol_handleRequest_DATA.cold.3
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_verify_composite.o)
+ _t56_util_callbackOnTimer
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_add1-arm64.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cccmac_init.o)
+ ___block_descriptor_56_e8_32s40s48r_e237_B24?0^{ACCConnection_s=^{__CFString}i^{__CFString}?Q^{__CFDictionary}{?=[5i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8s40l8r48l8
+ acc_manager_checkForInductiveCTA.cold.7
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cc_memory.o)
+ t56_protocol_init.cold.3
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccentropy_rng.o)
+ t56_protocol_initMsg_SESSION.cold.1
+ _t56_protocol_handleRequest_POLL.cold.1
+ _t56_endpoint_sendOutgoingDataCF
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccsha1_initial_state.o)
+ ___t56_endpoint_publish_block_invoke
+ mfi4Auth_relay_initMessage_DeviceiAP2RelayRemote_RequestAccessoryInfoUpdate.cold.1
+ __t56_endpoint_processIncomingData_block_invoke.cold.1
+ mfi4Auth_endpoint_publish.cold.5
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccder_blob_decode_tag.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cccmac_one_shot.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_mult.o)
+ iAP2MsgGetNextParamWithError.cold.2
+ _mfi4Auth_relay_handle_AccessoryInformationUpdate.cold.13
+ _t56_protocol_handleResponse_SESSION_RSP.cold.3
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccsha512_K.o)
+ _t56_protocol_handleResponse_DATA.cold.3
+ __t56_protocol_handleRequest_TERMINATE
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccder_blob_decode_bitstring.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccsha256_vng_arm_di.o)
+ _t56_protocol_handleResponse_STATUS.cold.3
+ t56_protocol_initMsg_POLL.cold.1
+ _t56_protocol_initMsg_DISCOVER
+ acc_connection_destroy.cold.7
+ _mfi4Auth_relay_handle_AccessoryInformationUpdate.cold.11
+ _t56_protocol_handleResponse_DATA.cold.1
+ _t56_protocol_handleRequest_DISCOVER.cold.2
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccmode_ccm_cbcmac.o)
+ _t56_protocol_checkValidMessageHeaderAndSize
+ acc_platform_packetLogging_logT56Msg.cold.3
+ ___block_descriptor_40_e8_32r_e237_B24?0^{ACCConnection_s=^{__CFString}i^{__CFString}?Q^{__CFDictionary}{?=[5i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}}8^v16lr32l8
+ t56_endpoint.c
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluate.o)
+ _t56_protocol_initMsg_STATUS
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccm-encrypt-540acaa315e66d78856969cd113f2071.o)
+ t56_protocol_start.cold.1
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_addmul1.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cczp_sub.o)
+ acc_connection_setAuthStatus.cold.6
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_sub-cdd78c10573f74a5ec5028711cf309f3.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccdigest_init.o)
+ mfi4Auth_relay_initMessage_DeviceiAP2RelayRemote_RequestAccessoryInfoUpdate.cold.3
+ _t56_protocol_initMsg_DATA
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccaes_arm_cbc_encrypt_mode.o)
+ _t56_util_cancelTimer
+ /Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessoryd.build/Objects-normal/arm64e/t56_endpoint.o
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_shift_right_multi.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_n-arm64.o)
+ _t56_util_init
+ _CFDictionaryApplierFunction_findInductiveCTAReceiverCapableConnection.cold.3
+ t56_protocol_init.cold.1
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_generate_scalar_fips_retry.o)
+ _t56_protocol_handleRequest_TERMINATE.cold.2
+ t56_endpoint_create.cold.1
+ t56_protocol_processIncomingData.cold.2
+ t56_util_callbackOnTimer.cold.3
+ mfi4Auth_relay_StartRelayForType.cold.5
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_set-f878490e7e92a54090b4bf80e4cdb7a4.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cc_fault_canary.o)
+ __t56_protocol_handleResponse_SESSION_RSP
+ _t56_protocol_cleanup
+ t56_protocol_sendData.cold.2
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_shift_right-a5bf4b9c8c049197c10410e37c19a019.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cc_cmp_safe.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_import_pub.o)
+ _t56_protocol_handleResponse_DISCOVER_RSP.cold.1
+ t56_endpoint_sendOutgoingDataCF.cold.2
+ t56_protocol_timeoutForRequest.cold.1
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_affine_point_from_x.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cc_clear.o)
+ _T56Protocol_timeoutCallback.cold.4
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_cmpn.o)
+ mfi4Auth_relay_StartRelayForType.cold.10
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_cp384.o)
+ _t56_protocol_handleResponse_DISCOVER_RSP.cold.2
+ _t56_protocol_handleRequest_DISCOVER.cold.1
+ t56_protocol_checkValidMessageHeaderAndSize.cold.7
+ t56_protocol_initMsg_DATA.cold.2
+ t56_protocol_initMsg_POLL.cold.3
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(aeskey.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccctr.o)
+ _kCFACCUserDefaultsKey_IgnoreAccInfoUpdateRelaySupport
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_add1.o)
+ t56_endpoint_publish.cold.2
+ t56_endpoint_sendOutgoingDataCF.cold.4
+ _t56_protocol_handleRequest_TERMINATE.cold.5
+ t56_endpoint_sendOutgoingDataCF.cold.5
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cczp_inv_field.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_mul1-arm64.o)
+ _t56_protocol_handleResponse_DISCOVER_RSP.cold.7
+ acc_connection_destroy.cold.8
+ t56_protocol_start.cold.3
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_mulmod_p384-arm64.o)
+ t56_util_cancelTimer.cold.2
+ t56_util_ios.m
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_is_point.o)
+ _mfi4Auth_relay_handle_AccessoryInformationUpdate.cold.14
+ __block_literal_global.271
+ _t56_protocol_handleRequest_TERMINATE.cold.1
+ ___t56_endpoint_create_block_invoke
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(aesencbc.o)
+ mfi4Auth_protocol_processIncomingMessageRelay.cold.23
+ _t56_protocol_timeoutForRequest
+ _t56_protocol_handleResponse_DATA.cold.9
+ t56_endpoint_destroy.cold.1
+ _kCFACCUserDefaultsKey_ForceT56RelaySupport
+ _CFDictionaryApplierFunction_findInductiveAuthEndpoint.cold.2
+ mfi4Auth_relay_StartRelayForType.cold.12
+ __block_literal_global.273
+ _T56Protocol_timeoutCallback.cold.5
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_compressed_x962_import_pub.o)
+ t56_endpoint_sendOutgoingDataCF.cold.6
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_projectify.o)
+ mfi4Auth_endpoint_publish.cold.6
+ _t56_util_sendData
+ t56_util_callbackOnTimer.cold.4
+ acc_connection_setProperties.cold.6
+ __mfi4Auth_relay_StartRelayForT56_block_invoke.cold.1
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccrng_getentropy.o)
+ __t56_endpoint_publish_block_invoke.cold.1
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccder_blob_decode_tl.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccmode_ctr_init.o)
+ _t56_protocol_handleRequest_POLL.cold.2
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Certificate.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccder_sizeof.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_verify_internal.o)
+ _acc_endpoint_setParentEndpointUUID
+ accAuthProtocol_endpoint_publish.cold.6
+ _T56Protocol_timeoutCallback.cold.3
+ _t56_protocol_start
+ t56_protocol_cleanup.cold.1
+ _mfi4Auth_relay_handle_AccessoryInformationUpdate.cold.2
+ __t56_endpoint_dispatchQueueFinalizer
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccder_sizeof_len.o)
+ ___t56_endpoint_processIncomingData_block_invoke
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccdigest_final_64be.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccrng_process.o)
+ _mfi4Auth_relay_handle_AccessoryInformationUpdate.cold.15
+ _acc_manager_checkForInductiveCTA
+ ___block_descriptor_40_e8_32s_e35_v24?0^{__CFString=}8^{__CFData=}16ls32l8
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_n-22916d0ab6c49a12764b75756a57ca03.o)
+ mfi4Auth_relay_StartRelayForT56.cold.2
+ _t56_util_ios_getT56Endpoint
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccder_blob_encode_body.o)
+ _mfi4Auth_relay_StartRelayForT56
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_cond_clear.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccmode_ccm_init.o)
+ _t56_protocol_handleResponse_DISCOVER_RSP.cold.4
+ __t56_protocol_handleRequest_DISCOVER
+ acc_connection_setProperty.cold.6
+ __t56_endpoint_create_block_invoke.cold.1
+ mfi4Auth_relay_StartRelayForT56.cold.6
+ t56_protocol_processIncomingData.cold.1
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccsha256_initial_state.o)
+ _mfi4Auth_relay_handle_AccessoryInformationUpdate.cold.5
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_cond_neg.o)
+ _t56_endpoint_destroy
+ t56_protocol_checkValidMessageHeaderAndSize.cold.2
+ _kCFACCUserDefaultsKey_DontSkipInductiveAuthOnCTA
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccgcm.o)
+ mfi4Auth_relay_StartRelayForT56.cold.5
+ _CFDictionaryApplierFunction_findInductiveCTADonorCapableConnection.cold.3
+ mfi4Auth_relay_StartRelayForType.cold.1
+ __mfi4Auth_relay_handle_AccessoryInformationUpdate
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccder_blob_decode_len.o)
+ mfi4Auth_protocol_handle_RequestAuthCert.cold.5
+ ___block_descriptor_49_e8_32s40r_e237_B24?0^{ACCConnection_s=^{__CFString}i^{__CFString}?Q^{__CFDictionary}{?=[5i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8r40l8
+ __t56_protocol_handleRequest_POLL
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccder_blob_decode_range.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccaes_vng_ctr_crypt.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccsigma.o)
+ acc_manager_checkForInductiveCTA.cold.2
+ _mfi4Auth_endpoint_firstUnlockHandler.cold.2
+ _CFDictionaryApplierFunction_findInductiveCTAReceiverCapableConnection.cold.2
+ _t56_protocol_handleResponse_DATA.cold.6
+ _objc_msgSend$startObservingFirstUnlockNotification
+ _t56_protocol_handleResponse_DATA.cold.5
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_mulmod_p256-arm64.o)
+ mfi4Auth_relay_StartRelayForT56.cold.7
+ t56_endpoint_sendOutgoingDataCF.cold.7
+ _mfi4Auth_relay_handle_AccessoryInformationUpdate.cold.3
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_addmul1-arm64.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cczp_to.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_read_uint.o)
+ t56_util_callbackOnTimer.cold.1
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cczp_power_fast.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cczp_prime.o)
+ __t56_protocol_handleResponse_DATA
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libCoreTrust.a(CryptoUtils.o)
+ _t56_protocol_initMsg_POLL
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_mult_blinded.o)
+ _t56_protocol_handleResponse_DATA.cold.2
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccaes_ccm_decrypt_mode.o)
+ mfi4Auth_relay_initMessage_DeviceiAP2RelayRemote_RequestAccessoryInfoUpdate.cold.2
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_add-58666b8c3e0ab18cabd648bafb5c7bb4.o)
+ mfi4Auth_relay_StartRelayForT56.cold.1
+ mfi4Auth_protocol_processIncomingMessageRelay.cold.24
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(sha256_compress_arm64.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libCoreTrust.a(CTCompress.o)
+ t56_util_ios_getT56Endpoint.cold.4
+ _t56_protocol_handleResponse_STATUS.cold.5
+ _kCFACCUserDefaultsKey_ForceAccInfoUpdateRelaySupport
+ t56_protocol_processIncomingData.cold.3
+ t56_endpoint_sendOutgoingData.cold.4
+ mfi4Auth_relay_StartRelayForType.cold.11
+ _kCFACCUserDefaultsKey_InductiveAuthPretendMatchRxID
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cc_abort.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_trailing_zeros.o)
+ _t56_protocol_processIncomingData
+ t56_endpoint_publish.cold.3
+ t56_protocol_checkValidMessageHeaderAndSize.cold.6
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_validate_point_and_projectify.o)
+ t56_protocol_checkValidMessageHeaderAndSize.cold.5
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccentropy.o)
+ _platform_system_startObservingFirstUnlockNotification
+ _t56_endpoint_publish
+ mfi4Auth_relay_StartRelayForT56.cold.3
+ _t56_protocol_handleResponse_SESSION_RSP.cold.4
+ t56_protocol_initMsg_DISCOVER.cold.3
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccdrbg.o)
+ t56_endpoint_sendOutgoingData.cold.2
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cc_dit.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_recode_jsf.o)
+ _mfi4Auth_relay_handle_AccessoryInformationUpdate.cold.4
+ acc_platform_packetLogging_logT56Msg.cold.2
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_random_bits.o)
+ _t56_protocol_handleResponse_DISCOVER_RSP.cold.5
+ _acc_platform_packetLogging_logT56Msg
+ __CFDictionaryApplierFunction_findInductiveCTADonorCapableConnection
+ _T56Protocol_timeoutCallback.cold.2
+ t56_endpoint_sendOutgoingDataCF.cold.1
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_full_add.o)
+ /Library/Caches/com.apple.xbs/Binaries/CoreAccessories/install/TempContent/Objects/CoreAccessories.build/accessoryd.build/Objects-normal/arm64e/t56_protocol.o
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_cp384_asm.o)
+ iAP2MsgGetNextParamWithError.cold.3
+ __CFDictionaryApplierFunction_findInductiveAuthEndpoint
+ mfi4Auth_relay_StartRelayForT56.cold.9
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccmode_ccm_set_iv.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_mul-2f7cf86de06386312707ba78fdd5f171.o)
+ __t56_protocol_handleRequest_SESSION
+ _kCFACCProperties_Endpoint_Inductive_RxID
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccder_blob_reserve.o)
+ t56_protocol.c
+ t56_protocol_initMsg_STATUS.cold.1
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_cond_rsub.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccccm.o)
+ __block_literal_global.10
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccaes_ctr_crypt_mode.o)
+ _mfi4Auth_relay_handle_AccessoryInformationUpdate.cold.6
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccmode_ctr_setctr.o)
+ ___block_descriptor_48_e8_32s40r_e237_B24?0^{ACCConnection_s=^{__CFString}i^{__CFString}?Q^{__CFDictionary}{?=[5i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8r40l8
+ mfi4Auth_relay_handle_iAP2RelayRemote.cold.21
+ t56_protocol_init.cold.2
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccder_blob_encode_tl.o)
+ _T56Protocol_timeoutCallback.cold.6
+ __t56_protocol_handleResponse_DISCOVER_RSP
+ t56_protocol_initMsg_POLL.cold.2
+ t56_util_callbackOnTimer.cold.6
+ _t56_protocol_handleResponse_SESSION_RSP.cold.2
+ t56_protocol_cleanup.cold.3
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cccmac_update.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(encrypt_ecb.o)
+ t56_protocol_initMsg_SESSION.cold.2
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cczp_sqr.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_x963_import_priv.o)
+ t56_protocol_processIncomingData.cold.4
+ __T56Protocol_timeoutCallback
+ _CFDictionaryApplierFunction_findInductiveCTAReceiverCapableConnection.cold.1
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_make_pub_from_priv.o)
+ iAP2MsgGetNextParamWithError.cold.1
+ _mfi4Auth_relay_handle_AccessoryInformationUpdate.cold.10
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cc_log.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_sub1-e65e5ad58ec65fa52769f7cb37cbcc48.o)
+ acc_connection_setProperties.cold.5
+ __t56_endpoint_processIncomingData_block_invoke.cold.2
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_import_affine_point.o)
+ t56_protocol_initMsg_DISCOVER.cold.1
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_bitlen.o)
+ _kCFACCUserDefaultsKey_PretendNFCAuthFailed
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ghash-arm64.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(sha1_compress_arm64.o)
+ _mfi4Auth_endpoint_firstUnlockHandler.cold.1
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(sha512_compress_arm64hw.o)
+ _t56_protocol_handleResponse_STATUS.cold.4
+ _t56_protocol_handleResponse_SESSION_RSP.cold.5
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cczp_mm_redc.o)
+ _t56_protocol_initMsg_SESSION
+ platform_system_startObservingFirstUnlockNotification.cold.1
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccnistkdf_ctr_cmac.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_sub-a773f541494c090466ddb983ed9b11b1.o)
+ ___mfi4Auth_relay_StartRelayForT56_block_invoke
+ t56_util_ios_getT56Endpoint.cold.2
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cczp_inv.o)
+ ___block_descriptor_41_e8_32s_e237_B24?0^{ACCConnection_s=^{__CFString}i^{__CFString}?Q^{__CFDictionary}{?=[5i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8
+ _t56_endpoint_processIncomingData
+ _CFDictionaryApplierFunction_findInductiveCTADonorCapableConnection.cold.2
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_full_sub.o)
+ _t56_endpoint_handleMessage.cold.2
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccaes_arm_ecb_encrypt_mode.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_mul-efe8a8912dccd210e69687a9ddedb900.o)
+ t56_util_callbackOnTimer.cold.5
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_export_affine_point.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cczp_mod.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccaes_vng_ccm_decrypt.o)
+ acc_connection_setAuthStatus.cold.5
+ mfi4Auth_protocol_handle_RequestAuthCert.cold.6
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cczp_funcs.o)
+ ___block_descriptor_44_e8_32r_e237_B24?0^{ACCConnection_s=^{__CFString}i^{__CFString}?Q^{__CFDictionary}{?=[5i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}}8^v16lr32l8
+ _kCFACCUserDefaultsKey_SkipNFCAuth
+ __t56_protocol_handleRequest_DATA
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccecdh_compute_shared_secret.o)
+ accAuthProtocol_endpoint_publish.cold.5
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccsha1.o)
+ t56_endpoint_publish.cold.1
+ _mfi4Auth_relay_handle_AccessoryInformationUpdate.cold.8
+ _t56_protocol_handleResponse_SESSION_RSP.cold.1
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cczp_negate.o)
+ mfi4Auth_relay_StartRelayForType.cold.6
+ _t56_protocol_handleRequest_TERMINATE.cold.3
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cczp_add.o)
+ acc_platform_packetLogging_logT56Msg.cold.1
+ _t56_endpoint_create
+ mfi4Auth_relay_StartRelayForType.cold.7
+ __block_descriptor_tmp.18
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccdigest_update.o)
+ t56_protocol_cleanup.cold.2
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccaes_ecb_encrypt_mode.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccder_blob_encode_tag.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_affinify.o)
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cczp_is_quadratic_residue.o)
+ t56_util_cancelTimer.cold.1
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cczp_div2.o)
+ acc_manager_checkForInductiveCTA.cold.5
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_validate_scalar.o)
+ t56_protocol_sendData.cold.1
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_cond_swap.o)
+ _t56_protocol_handleRequest_SESSION.cold.4
+ mfi4Auth_relay_StartRelayForType.cold.14
+ /AppleInternal/Library/BuildRoots/473de0b3-6a21-11ef-b572-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cczp_sqrt.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccentropy_rng.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_x963_import_pub.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cc_dit.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_add-6bbaf80cd023f341e4d7979b160719af.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cczp_add.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cc_lock.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_export_pub.o)
- ___block_descriptor_40_e8_32r_e237_B24?0^{ACCConnection_s=^{__CFString}i^{__CFString}?Q^{__CFDictionary}{?=[4i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}}8^v16lr32l8
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_mux.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_mul1.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccctr.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cczp_from.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccm-decrypt-3d98bad873178684405c1aebec7e8538.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_n-22916d0ab6c49a12764b75756a57ca03.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cccmac_generate_subkey.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_addmul1.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cczp_is_quadratic_residue.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_import_affine_point.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccder_blob_decode_tag.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cc_memory.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccgcm.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_pairwise_consistency_check.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_full_sub.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_cp384.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccaes_arm_ecb_encrypt_mode.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_mult.o)
- ___block_descriptor_56_e8_32s40s48r_e237_B24?0^{ACCConnection_s=^{__CFString}i^{__CFString}?Q^{__CFDictionary}{?=[4i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8s40l8r48l8
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccecdh_compute_shared_secret.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(encrypt_ecb.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccder_blob_encode_body.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cczp_inv.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_random_bits.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccnistkdf_ctr_cmac.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_cond_swap.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccdigest_final_64be.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_validate_scalar.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_sqr.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_common.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cczp_mod.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cczp_div2.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccrng_process.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccder_blob_decode_range.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_recode_jsf.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_subn.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(aeskey.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_mulmod_p384-arm64.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libCoreTrust.a(CryptoUtils.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_shift_left_arm64.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccaes_ccm_decrypt_mode.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccentropy.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_sign_internal.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ghash-arm64.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libCoreTrust.a(DERUtils.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccdigest.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccder_blob_decode_uint64.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_x963_import_priv.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_verify_composite.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cczp_sqr.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccsha256_initial_state.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_trailing_zeros.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccaes_ecb_encrypt_mode.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_cond_add.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_addmul1-arm64.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cc_cmp_safe.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccsigma.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_projectify.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_mul-2f7cf86de06386312707ba78fdd5f171.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cczp_sub.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccccm.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(sha256_compress_arm64.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_shift_right_multi.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_cond_clear.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_n-arm64.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccder_blob_decode_bitstring.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccsha512_K.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccrng_getentropy.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(aesencbc.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_sub-a773f541494c090466ddb983ed9b11b1.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccdigest_update.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Policy.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccm-encrypt-540acaa315e66d78856969cd113f2071.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccaes_vng_ccm_decrypt.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(sha1_compress_arm64.o)
- __block_literal_global.253
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccder_blob_encode_len.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccder_blob_decode_tl.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_import_pub.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_divmod.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccdrbg_nistctr.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cccmac_update.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccder_sizeof.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cc_fault_canary.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_shift_right-d9572f405a1bc8758eb209492b4b0148.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cc_try_abort.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_cp521.o)
- __block_descriptor_tmp.16
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccsha256_di.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cczp_negate.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cczp_common.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccaes_ctr_crypt_mode.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cczp_sqrt.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_validate_point_and_projectify.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccaes_vng_ccm_encrypt.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccaes_cbc_encrypt_mode.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_bitlen.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccmode_ccm_finalize.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_cp256.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_cp384_asm.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccrng_schedule.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cc_abort.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccder_blob_decode_len.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccaes_arm_cbc_encrypt_mode.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_verify_internal.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libCoreTrust.a(X509Certificate.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_add1-arm64.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_is_point.o)
- ___block_descriptor_41_e8_32s_e237_B24?0^{ACCConnection_s=^{__CFString}i^{__CFString}?Q^{__CFDictionary}{?=[4i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_sign_composite.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ctr-arm64.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cczp_to.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_add-58666b8c3e0ab18cabd648bafb5c7bb4.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccder_blob_encode_tl.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccmode_ccm_cbcmac.o)
- __block_literal_global.9
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccaes_ccm_encrypt_mode.o)
- ___block_descriptor_48_e8_32s40r_e237_B24?0^{ACCConnection_s=^{__CFString}i^{__CFString}?Q^{__CFDictionary}{?=[4i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8r40l8
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_set-f878490e7e92a54090b4bf80e4cdb7a4.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccder_blob_encode_body_tl.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccsha1_vng_arm.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cczp_mul.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_shift_right-a5bf4b9c8c049197c10410e37c19a019.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_sub1-e65e5ad58ec65fa52769f7cb37cbcc48.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_twin_mult.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_mulmod_p256-arm64.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_affinify.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cc_log.o)
- __block_literal_global.255
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_mul1-arm64.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccaes_vng_ctr_crypt.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cczp_prime.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_add1.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccsha1.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccmode_ccm_encrypt.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_mult_blinded.o)
- ___block_descriptor_61_e8_32s40s48r_e237_B24?0^{ACCConnection_s=^{__CFString}i^{__CFString}?Q^{__CFDictionary}{?=[4i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8s40l8r48l8
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cczp_inv_field.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_cmp-500c58650b2463f61cd9d5df32539886.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cc_clear.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccdigest_init.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccmode_ctr_init.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cczp_funcs.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_cmpn.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_full_add.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libCoreTrust.a(CTCompress.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccder_sizeof_len.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_cond_neg.o)
- ___block_descriptor_49_e8_32s40r_e237_B24?0^{ACCConnection_s=^{__CFString}i^{__CFString}?Q^{__CFDictionary}{?=[4i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8r40l8
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_make_pub_from_priv.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccsha1_initial_state.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_generate_key_fips.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_sub-cdd78c10573f74a5ec5028711cf309f3.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccder_sizeof_tag.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_write_uint.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_double.o)
- ___block_descriptor_52_e8_32s40r_e237_B24?0^{ACCConnection_s=^{__CFString}i^{__CFString}?Q^{__CFDictionary}{?=[4i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}}8^v16ls32l8r40l8
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_mul-efe8a8912dccd210e69687a9ddedb900.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_read_uint.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccsigma_mfi.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccder_blob_reserve.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccrng_static.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_affine_point_from_x.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccsha256_vng_arm_di.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cccmac_init.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccmode_ccm_init.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccdrbg.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_cp256_asm.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libCoreTrust.a(CTEvaluate.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_signature_r_s_size.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccmode_ctr_setctr.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_generate_key_internal_fips.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccmode_ccm_set_iv.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cczp_mm_redc.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_cmp-arm64.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cccmac_final.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_compressed_x962_export_pub.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccmode_ccm_reset.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cczp_power_fast.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(sha512_compress_arm64hw.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccdrbg_df.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_generate_scalar_fips_retry.o)
- ___block_descriptor_44_e8_32r_e237_B24?0^{ACCConnection_s=^{__CFString}i^{__CFString}?Q^{__CFDictionary}{?=[4i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}}8^v16lr32l8
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccn_cond_rsub.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccder_blob_encode_tag.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccrng_crypto.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cccbc.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_export_affine_point.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(cccmac_one_shot.o)
- /AppleInternal/Library/BuildRoots/ec822f1e-5bf2-11ef-bec5-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/lib/libcorecrypto_static.a(ccec_compressed_x962_import_pub.o)
CStrings:
+ "_t56_protocol_handleResponse_DATA"
+ "%!s(MISSING):%!d(MISSING) paramMask 0x%!x(MISSING), CertHash paramMask 0x%!x(MISSING), CertKeyID paramMask 0x%!x(MISSING) "
+ "%!s(MISSING):%!d(MISSING) result %!d(MISSING), role %!d(MISSING)X"
+ "%!s(MISSING):%!d(MISSING) result %!d(MISSING), msgType %!d(MISSING)(%!s(MISSING)), msgHeader 0x%!X(MISSING), msgDataLen %!d(MISSING)"
+ "mfi4Auth_relay_initMessage_DeviceiAP2RelayRemote_RequestAccessoryInfoUpdate"
+ "acc_connection_setProperty: call acc_manager_checkForInductiveCTA"
+ "%!s(MISSING): PretendNFCAuthTimeout!!!, ignore status(%!d(MISSING))"
+ "t56_endpoint_sendOutgoingDataCF"
+ "%!s(MISSING):%!d(MISSING) reached end of message buffer (%!d(MISSING) bytes)\n"
+ "%!s(MISSING):%!d(MISSING) sessionID %!d(MISSING), status %!d(MISSING), status 0x%!x(MISSING)"
+ "DATA-RxID"
+ "ForceAccInfoUpdateRelaySupport"
+ "_mfi4Auth_endpoint_firstUnlockHandler FIRED!!"
+ "%!s(MISSING): %!@(MISSING), secureTunnelType %!d(MISSING)"
+ "%!s(MISSING):%!d(MISSING) Device, msgType %!d(MISSING)(%!s(MISSING)), msgHeader 0x%!X(MISSING), msgDataLen %!d(MISSING)"
+ "%!s(MISSING):%!d(MISSING) role %!d(MISSING), msgType %!d(MISSING)(%!s(MISSING)), sessionID %!d(MISSING), clientID %!d(MISSING), Unknown RxID command 0x%!x(MISSING) (%!d(MISSING))"
+ "%!s(MISSING):%!d(MISSING) ERROR: Protocol context is NULL!!!!"
+ "t56_protocol_cleanup"
+ "%!s(MISSING): wrong messageID"
+ "%!s(MISSING):%!d(MISSING) role %!d(MISSING), msgType %!d(MISSING)(%!s(MISSING)), sessionID %!d(MISSING), client[%!d(MISSING)]: clientID 0x%!x(MISSING)(%!d(MISSING)), identifier 0x%!x(MISSING)(%!d(MISSING) '%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)')"
+ "processIncomingMessageRelay: %!@(MISSING), initMessage RequestAccessoryInfoUpdate"
+ "T56Endpoint"
+ "B24@?0^{ACCConnection_s=^{__CFString}i^{__CFString}@?Q^{__CFDictionary}{?=[5i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}}8^v16"
+ "%!s(MISSING):%!d(MISSING) enter"
+ "%!s(MISSING): paramID: %!d(MISSING)"
+ "processIncomingMessageRelay: override supportedSecureTunnelCapabilitiesMask 0x%!l(MISSING)lx &= 0x%!x(MISSING)"
+ "%!s(MISSING): Checking if device has been unlocked since first boot"
+ "%!s(MISSING):%!d(MISSING) role %!d(MISSING), msgType %!d(MISSING)(%!s(MISSING)), sessionID %!d(MISSING), version %!d(MISSING), sessionCommand %!d(MISSING)"
+ "Check for InductiveCTA: No donor! Maintain auth state for receiver %!@(MISSING) (authStatus %!{(MISSING)coreacc:ACCAuthInfo_Status_t}d / %!{(MISSING)coreacc:ACCAuthInfo_Status_t}d)"
+ "LOG; %!f(MISSING); %!@(MISSING); %!s(MISSING); %!@(MISSING); msg %!d(MISSING)(%!s(MISSING)); payload(len=%!u(MISSING))="
+ "t56_protocol_init"
+ "findInductiveCTADonorCapableConnection: %!@(MISSING) type %!{(MISSING)coreacc:ACCConnection_Type_t}d, isAuthenticated %!d(MISSING), ident: %!@(MISSING)"
+ "t56_protocol_start"
+ "%!s(MISSING): parentEndpoint %!@(MISSING), dataOut %!@(MISSING)"
+ "processIncomingMessageRelay: override supportedSecureTunnelCapabilitiesMask 0x%!l(MISSING)lx |= 0x%!x(MISSING)"
+ "%!s(MISSING): pProtocolEndpoint %!@(MISSING), dataOut %!@(MISSING)"
+ "%!s(MISSING):%!d(MISSING) role %!d(MISSING), msgType %!d(MISSING)(%!s(MISSING)), sessionID %!d(MISSING), numClients %!d(MISSING)"
+ "Check for InductiveCTA"
+ "%!s(MISSING):%!d(MISSING) numClients(%!d(MISSING)) too large! (max %!d(MISSING)), role %!d(MISSING), msgType %!d(MISSING)(%!s(MISSING)), sessionID %!d(MISSING), numClients %!d(MISSING)"
+ "%!s(MISSING):%!d(MISSING) role %!d(MISSING), msgType %!d(MISSING)(%!s(MISSING)), sessionID %!d(MISSING), clientID %!d(MISSING), expecting payloadLen at least %!d(MISSING)!!!"
+ "mfi4Auth_protocol_handle_RequestAuthCert"
+ "%!s(MISSING):%!d(MISSING) role %!d(MISSING), dataInLen %!d(MISSING), dataOutSize %!d(MISSING)"
+ "hardwareVersionString %!@(MISSING)"
+ "%!s(MISSING):%!d(MISSING) role %!d(MISSING), msgType %!d(MISSING)(%!s(MISSING))"
+ "%!s(MISSING):%!d(MISSING) msgType %!d(MISSING)(%!s(MISSING)), msgHeader 0x%!X(MISSING), msgDataLen %!d(MISSING)"
+ "iAP2MsgGetNextParamWithError"
+ "t56_protocol_initMsg_SESSION"
+ "%!s(MISSING): unable to allocate outMsg!"
+ "t56_protocol_initMsg_POLL"
+ "processOutgoingSecureTunnelDataForClient: %!@(MISSING), data %!@(MISSING)"
+ "findInductiveCTAReceiverCapableConnection: %!@(MISSING) type %!{(MISSING)coreacc:ACCConnection_Type_t}d, isAuthenticated %!d(MISSING), found rxID %!@(MISSING)"
+ "t56_endpoint_processIncomingData_block_invoke"
+ "%!s(MISSING):%!d(MISSING) Accessory: Unexpected MsgType!!! msgType %!d(MISSING)(%!s(MISSING)), msgHeader 0x%!X(MISSING), msgDataLen %!d(MISSING)"
+ "%!s(MISSING):%!d(MISSING) reached end of parameter (%!d(MISSING) bytes), grplen %!d(MISSING)\n"
+ "DISCOVER_RSP"
+ "_t56_protocol_handleRequest_POLL"
+ "PretendNFCAuthFailed"
+ "firmwareVersionString %!@(MISSING)"
+ "%!s(MISSING): PretendNFCAuthFailed(%!d(MISSING))/PretendNFCAuthTimeout(%!d(MISSING)) !!!, rxIDMatch %!d(MISSING) -> %!d(MISSING)"
+ "pDataOut = NULL"
+ "pProtocolEndpoint->pEndpoint = NULL"
+ "SESSION"
+ "T56"
+ "Check for InductiveCTA: attempt to find... donor %!d(MISSING), receiver %!d(MISSING)"
+ "processOutgoingSecureTunnelDataForClient: SecureTunnelType(%!d(MISSING)) not supported!"
+ "missing outMessage"
+ "_t56_protocol_handleResponse_STATUS"
+ "%!s(MISSING):%!d(MISSING) role %!d(MISSING), clear tx digest / cert cache"
+ "mfi4Auth_relay_StartRelayForType"
+ "Check for InductiveCTA: Found match! donor %!@(MISSING), receiver %!@(MISSING)"
+ "%!s(MISSING): unable to allocate outMsg buffer!"
+ "_mfi4Auth_endpoint_firstUnlockHandler endpoint Found: %!@(MISSING)"
+ "%!s(MISSING):%!d(MISSING) ERROR: Endpoint not found!!!!"
+ "%!s(MISSING):%!d(MISSING) Device: Unhandled timeoutType %!d(MISSING) !!!"
+ "T56 Endpoint Destroy. NULL ppProtocolEndpoint!"
+ "t56_protocol_initMsg_DISCOVER"
+ "%!s(MISSING):%!d(MISSING) Unknown Role! %!d(MISSING), result %!d(MISSING), msgType %!d(MISSING)(%!s(MISSING)), msgHeader 0x%!X(MISSING), msgDataLen %!d(MISSING)"
+ "ForceT56RelaySupport"
+ "%!s(MISSING):%!d(MISSING) role %!d(MISSING), msgType %!d(MISSING)(%!s(MISSING)), sessionID %!d(MISSING), version %!d(MISSING), maxLength %!d(MISSING), status %!d(MISSING), info %!d(MISSING)"
+ "t56_protocol_sendData"
+ "_t56_protocol_handleRequest_TERMINATE"
+ "_t56_protocol_handleResponse_DISCOVER_RSP"
+ "SkipNFCAuth"
+ "T56 accessory detached!"
+ "t56_util_ios_getT56Endpoint"
+ "_t56_protocol_handleRequest_DATA"
+ "%!s(MISSING):%!d(MISSING) sessionID %!d(MISSING), clientID %!d(MISSING), remaining %!d(MISSING), payloadLen %!d(MISSING)"
+ "%!s(MISSING): PretendNFCAuthFailed!!!, set status(%!d(MISSING))"
+ "%!s(MISSING): rxIDMatch %!d(MISSING), -> pretend matching rxID !!!"
+ "%!s(MISSING): donor %!@(MISSING), receiver %!@(MISSING), rxIDMatch %!d(MISSING), donorRxID %!@(MISSING), receiverRxID %!@(MISSING), pAccAuthEndpointFound %!@(MISSING)"
+ "acc_connection_setAuthStatus: auth passed for NFC connection, call acc_manager_checkForInductiveCTA"
+ "%!s(MISSING):%!d(MISSING) role %!d(MISSING), msgType %!d(MISSING)(%!s(MISSING)), sessionID %!d(MISSING), clientID %!d(MISSING), remaining %!d(MISSING), payloadLen %!d(MISSING)"
+ "_T56Protocol_timeoutCallback"
+ "iPod-T56"
+ "findInductiveCTAReceiverCapableConnection: %!@(MISSING) type %!{(MISSING)coreacc:ACCConnection_Type_t}d"
+ "DontSkipInductiveAuthOnCTA"
+ "_t56_protocol_handleRequest_DISCOVER"
+ "%!s(MISSING):%!d(MISSING) sessionID %!d(MISSING), version %!d(MISSING), sessionCommand %!d(MISSING)"
+ "processIncomingMessageRelay: %!@(MISSING), supportedSecureTunnelCapabilitiesMask 0x%!l(MISSING)lx, currentType/Mask %!d(MISSING)/0x%!l(MISSING)lx"
+ "t56_protocol_processIncomingData"
+ "%!s(MISSING):%!d(MISSING) Invalid message size %!d(MISSING) vs %!d(MISSING), role %!d(MISSING), msgType %!d(MISSING)(%!s(MISSING)), sessionID %!d(MISSING), numClients %!d(MISSING)"
+ "%!s(MISSING): Already Authenticated, notifyAuthStatus %!{(MISSING)coreacc:ACCAuthInfo_Status_t}d"
+ "PretendNFCAuthTimeout"
+ "Check for InductiveCTA: Found donor %!@(MISSING), receiver %!@(MISSING), but data/info doesn't match or doesn't exist! donor %!@(MISSING), receiver %!@(MISSING)"
+ "%!s(MISSING):%!d(MISSING) Device: Unexpected MsgType!!! msgType %!d(MISSING)(%!s(MISSING)), msgHeader 0x%!X(MISSING), msgDataLen %!d(MISSING)"
+ "t56_protocol_timeoutForRequest"
+ "%!s(MISSING):%!d(MISSING) role %!d(MISSING), msgType %!d(MISSING)(%!s(MISSING)), sessionID %!d(MISSING)"
+ "%!s(MISSING):%!d(MISSING) Accessory, msgType %!d(MISSING)(%!s(MISSING)), msgHeader 0x%!X(MISSING), msgDataLen %!d(MISSING)"
+ "T56 Endpoint Destroy. *ppProtocolEndpoint is null!"
+ "_mfi4Auth_relay_handle_AccessoryInformationUpdate: finish"
+ "T56 endpoint_publish"
+ "Acc-T56"
+ "%!s(MISSING):%!d(MISSING) role %!d(MISSING)"
+ "%!s(MISSING):%!d(MISSING) Device: Unexpected MsgType!!! ver %!d(MISSING), msgType %!d(MISSING)(%!s(MISSING))"
+ "%!s(MISSING):%!d(MISSING) sessionID %!d(MISSING)"
+ "accAuthProtocol_endpoint_publish"
+ "SESSION_RSP"
+ "_t56_protocol_handleResponse_SESSION_RSP"
+ "%!s(MISSING): pProtocolEndpoint %!@(MISSING), dataOutLen %!d(MISSING)"
+ "IgnoreAccInfoUpdateRelaySupport"
+ "%!s(MISSING): Setting sleep assertion"
+ "t56_protocol_initMsg_DATA"
+ "T56 accessory attached!"
+ "_mfi4Auth_relay_handle_AccessoryInformationUpdate"
+ "ACCPlatformApplicationFirstUnlockNotification"
+ "Check for InductiveCTA: receiver %!@(MISSING), already authenticated! %!{(MISSING)coreacc:ACCAuthInfo_Status_t}d"
+ "dataOut = NULL"
+ "t56_util_cancelTimer"
+ "processOutgoingSecureTunnelDataForClient: SecureTunnelType(%!d(MISSING)), Failed to publish endpoint %!@(MISSING) !"
+ "unable to find connection UUID for endpoint %!@(MISSING)"
+ "%!s(MISSING):%!d(MISSING) role %!d(MISSING), msgType %!d(MISSING)(%!s(MISSING)), sessionID %!d(MISSING), status %!d(MISSING), errorCode %!d(MISSING)"
+ "findInductiveAuthEndpoint: %!@(MISSING) protocol %!{(MISSING)coreacc:ACCEndpoint_Protocol_t}d"
+ "acc_manager_checkForInductiveCTA"
+ "mfi4Auth_relay_handle_iAP2RelayRemote: unable to create parser!!!"
+ "%!s(MISSING):%!d(MISSING) result %!d(MISSING), sessionID %!u(MISSING), msgType %!d(MISSING)(%!s(MISSING)), msgDataOutLen %!d(MISSING)"
+ "acc_connection_setProperties: call acc_manager_checkForInductiveCTA"
+ "t56_endpoint_sendOutgoingData"
+ "POLL"
+ "acc_connection_destroy: call acc_manager_checkForInductiveCTA"
+ "%!s(MISSING): SkipNFCAuth!!!"
+ "_t56_protocol_handleRequest_SESSION"
+ "[AccAuth] oldAuthStatus %!d(MISSING), oldCTAAuthStatus %!d(MISSING) \n"
+ "T56 publish: transportType %!{(MISSING)coreacc:ACCEndpoint_TransportType_t}d, parentEndpointUUID %!@(MISSING), start protocol!!!"
+ "InductiveAuthPretendMatchRxID"
+ "STATUS"
+ "t56_util_callbackOnTimer"
+ "findInductiveCTAReceiverCapableConnection: %!@(MISSING) type %!{(MISSING)coreacc:ACCConnection_Type_t}d, isAuthenticated %!d(MISSING), pretend found rxID !!!"
+ "%!s(MISSING):%!d(MISSING) result %!d(MISSING) sessionID %!d(MISSING), msgType %!d(MISSING)(%!s(MISSING)), msgDataOutLen %!d(MISSING)"
+ "t56_protocol_checkValidMessageHeaderAndSize"
+ "DISCOVER"
+ "%!s(MISSING):%!d(MISSING) role %!d(MISSING), msgType %!d(MISSING)(%!s(MISSING)), sessionID %!d(MISSING), clientID %!d(MISSING), received rxID 0x%!x(MISSING) (%!d(MISSING))"
+ "mfi4Auth_relay_handle_iAP2RelayRemote: failed to parse AccessoryInformationUpdate message!!!"
+ "dataOutLen = 0"
+ "mfi4Auth_protocol_handle_AuthCert"
+ "RequestAuthCert: paramId %!d(MISSING) (0x%!x(MISSING))"
+ "findInductiveCTADonorCapableConnection: %!@(MISSING) type %!{(MISSING)coreacc:ACCConnection_Type_t}d, isAuthenticated %!d(MISSING), found rxID %!@(MISSING)"
+ "T56 publish: transportType %!{(MISSING)coreacc:ACCEndpoint_TransportType_t}d, parentEndpointUUID %!@(MISSING)"
+ "%!s(MISSING): parentEndpoint NULL, dataOut %!@(MISSING)"
+ "%!s(MISSING): copy certData from %!@(MISSING) to %!@(MISSING) : %!@(MISSING)"
+ "t56_protocol_initMsg_STATUS"
+ "%!s(MISSING): Device has not been unlocked since last boot. Setting up observer"
+ "%!s(MISSING):%!d(MISSING) Device: Unexpected MsgType!!! ver %!d(MISSING), msgType %!d(MISSING)(%!s(MISSING)), dataInLen %!d(MISSING)"
+ "T56 timer source fired!!! T56TimerCallback(%!d(MISSING)), timerID %!d(MISSING)"
+ "RxID: %!@(MISSING) / 0x%!X(MISSING)"
+ "Check for InductiveCTA: Inform authProtocol endpoint %!{(MISSING)coreacc:ACCAuthInfo_Status_t}d"
+ "T56 publish: transportType %!{(MISSING)coreacc:ACCEndpoint_TransportType_t}d, parentEndpointUUID %!@(MISSING), after delay, call t56_protocol_start"
+ "%!s(MISSING): string parameter not NUL terminated! (paramID %!d(MISSING))"
+ "%!s(MISSING):%!d(MISSING) Accessory: Unexpected MsgType!!! ver %!d(MISSING), msgType %!d(MISSING)(%!s(MISSING)), dataInLen %!d(MISSING)"
- "%!s(MISSING): Device has not been unlocked since last boot."
- "mfi4Auth_endpoint_publish: Setting sleep assertion"
- "B24@?0^{ACCConnection_s=^{__CFString}i^{__CFString}@?Q^{__CFDictionary}{?=[4i]i^{__CFData}^{__CFData}^{__CFString}^{__CFData}{?=i}{?=}B}{?=i}^{?}^{__CFDictionary}BBBSB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}}8^v16"

```
