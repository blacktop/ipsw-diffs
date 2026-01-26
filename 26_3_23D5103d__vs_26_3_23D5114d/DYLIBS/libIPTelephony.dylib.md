## libIPTelephony.dylib

> `/System/Library/PrivateFrameworks/IPTelephony.framework/Support/libIPTelephony.dylib`

```diff

-2613.2.0.0.0
-  __TEXT.__text: 0x52dbb8
+2615.0.0.0.0
+  __TEXT.__text: 0x52d5a0
   __TEXT.__auth_stubs: 0x2ee0
   __TEXT.__init_offsets: 0x15c
   __TEXT.__objc_methlist: 0x748
   __TEXT.__const: 0x20b4a
-  __TEXT.__cstring: 0x379e9
-  __TEXT.__gcc_except_tab: 0x4ecc8
-  __TEXT.__oslogstring: 0xf1e1
-  __TEXT.__unwind_info: 0x19278
+  __TEXT.__cstring: 0x37927
+  __TEXT.__gcc_except_tab: 0x4ec60
+  __TEXT.__oslogstring: 0xf317
+  __TEXT.__unwind_info: 0x19258
   __TEXT.__objc_classname: 0x12f
   __TEXT.__objc_methname: 0x1de8
   __TEXT.__objc_methtype: 0x1118

   __DATA_CONST.__objc_selrefs: 0x968
   __DATA_CONST.__objc_superrefs: 0x38
   __AUTH_CONST.__auth_got: 0x1780
-  __AUTH_CONST.__const: 0x3c2c8
+  __AUTH_CONST.__const: 0x3c2c0
   __AUTH_CONST.__cfstring: 0x26e0
   __AUTH_CONST.__objc_const: 0xbf8
   __AUTH_CONST.__objc_intobj: 0x60

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 521FA9AA-1BE4-347E-ACD2-41B9E3208A97
-  Functions: 17132
-  Symbols:   51468
-  CStrings:  9959
+  UUID: B87807BD-33CD-3597-A4DC-7B6D6CC4D946
+  Functions: 17129
+  Symbols:   51458
+  CStrings:  9957
 
Symbols:
+ __ZN10SDPSession17handleOfferAnswerENSt3__110shared_ptrI8SDPModelEES3_yRKNS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZN12SipUserAgent20initializeAuthClientEb
+ __ZN13SipDialogFork20handleRemoteSdpOfferENSt3__110shared_ptrI8SDPModelEEN3xpc4dictERKNS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZN14SipOfferAnswer25updateWithIncomingRequestENSt3__110shared_ptrIK10SipRequestEERKNS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZN9BambiCall20handleSdpOfferInForkENSt3__110shared_ptrI8SDPModelEENS1_I13SipDialogForkEERKNS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZNSt3__123__optional_storage_baseI19SDPMediaTTYSettingsLb0EE13__assign_fromB8ne200100IRKNS_27__optional_copy_assign_baseIS1_Lb0EEEEEvOT_
+ __ZThn144_N13SipDialogFork20handleRemoteSdpOfferENSt3__110shared_ptrI8SDPModelEEN3xpc4dictERKNS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
- __ZN10SDPSession17handleOfferAnswerENSt3__110shared_ptrI8SDPModelEES3_y
- __ZN13SipDialogFork20handleRemoteSdpOfferENSt3__110shared_ptrI8SDPModelEEN3xpc4dictE
- __ZN14SipOfferAnswer25updateWithIncomingRequestENSt3__110shared_ptrIK10SipRequestEERKNS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERK8ImsPrefs
- __ZN20SipServerTransaction29handleConversationIdCollisionEv
- __ZN9BambiCall20handleSdpOfferInForkENSt3__110shared_ptrI8SDPModelEENS1_I13SipDialogForkEE
- __ZNK14SipOfferAnswer13answerPendingEv
- __ZNK16SipDialogManager24dialogWithConversationIdERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
- __ZNK9SipDialog9confirmedEv
- __ZNKSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI9SipDialogEEEENS_22__unordered_map_hasherIS7_SB_NS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SB_SG_SE_Lb1EEENS5_ISB_EEE4findIS7_EENS_21__hash_const_iteratorIPNS_11__hash_nodeISB_PvEEEERKT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrI9SipDialogEEEENS_22__unordered_map_hasherIS7_SB_NS_4hashIS7_EENS_8equal_toIS7_EELb1EEENS_21__unordered_map_equalIS7_SB_SG_SE_Lb1EEENS5_ISB_EEE5clearEv
- __ZThn144_N13SipDialogFork20handleRemoteSdpOfferENSt3__110shared_ptrI8SDPModelEEN3xpc4dictE
CStrings:
+ "#D %{private, mask.hash}sCreating PAT auth client. replacing=%{BOOL}d actualPR=%{BOOL}d intendedPR=%{BOOL}d"
+ "#D %{private, mask.hash}sCreating normal auth client. replacing=%{BOOL}d actualPR=%{BOOL}d intendedPR=%{BOOL}d"
+ "#D %{private, mask.hash}sTransport init success. isPrivateRelayActive=%{BOOL}d"
+ "#E %{private, mask.hash}sReturning deregistered state due to uninitialized registration client"
+ "#E %{private, mask.hash}sReturning deregistered state due to uninitialized user agent"
+ "/AppleInternal/Library/BuildRoots/4~CHXlugA6SWPXsEEWi2E6NYnTYvLbRsMW5T16D2k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
+ "/AppleInternal/Library/BuildRoots/4~CHXlugA6SWPXsEEWi2E6NYnTYvLbRsMW5T16D2k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "added [Dialog "
+ "no existing dialog with callId "
+ "we have dialog weak reference. But dialog is gone "
- " conversationID="
- "#I %{private, mask.hash}sno existing dialog with callId %s"
- "#I %{private, mask.hash}sno existing dialog with conversationId %s"
- "#W %{private, mask.hash}sDialog is null %s"
- "/AppleInternal/Library/BuildRoots/4~CGHougDSa5Sf3dZFfHbvss--iRJqqxvJl2ywTd8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h"
- "/AppleInternal/Library/BuildRoots/4~CGHougDSa5Sf3dZFfHbvss--iRJqqxvJl2ywTd8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "Conversation ID collision detected, sending 491 Status Request Pending"
- "Creating PAT auth client"
- "Creating normal auth client"
- "added [Dialog callId="
- "received UPDATE w/ no SDP while in state: "
- "received UPDATE w/ no SDP. Starting new offer/answer exchange so we can send an offer"

```
