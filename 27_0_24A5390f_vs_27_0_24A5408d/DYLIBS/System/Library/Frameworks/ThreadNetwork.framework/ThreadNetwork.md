## ThreadNetwork

> `/System/Library/Frameworks/ThreadNetwork.framework/ThreadNetwork`

```diff

-438.0.0.0.0
-  __TEXT.__text: 0xe890
-  __TEXT.__objc_methlist: 0xd58
+442.0.0.0.0
+  __TEXT.__text: 0xda20
+  __TEXT.__objc_methlist: 0xdb8
   __TEXT.__const: 0xb8
-  __TEXT.__cstring: 0x16c2
+  __TEXT.__cstring: 0x16ed
   __TEXT.__oslogstring: 0xa7b
   __TEXT.__gcc_except_tab: 0x190
-  __TEXT.__unwind_info: 0x3b0
+  __TEXT.__unwind_info: 0x388
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x440
+  __DATA_CONST.__const: 0x468
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7a8
+  __DATA_CONST.__objc_selrefs: 0x7e8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__got: 0x138
   __AUTH_CONST.__const: 0x180
-  __AUTH_CONST.__cfstring: 0x820
-  __AUTH_CONST.__objc_const: 0x1b98
+  __AUTH_CONST.__cfstring: 0x840
+  __AUTH_CONST.__objc_const: 0x1bb0
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0xf8

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 359
-  Symbols:   854
-  CStrings:  212
+  Functions: 366
+  Symbols:   868
+  CStrings:  213
 
Symbols:
+ -[THClient enableCredentialSharingModeForExtendedPANID:completion:]
+ -[THClient enableCredentialSharingModeInternallyForExtendedPANID:completion:]
+ -[THClient handleActiveNearbyNetworksResponse:error:isInternal:completion:]
+ -[THClient retrieveActiveCredentialsForNearbyNetworksInternallyWithCompletion:]
+ -[THClient retrieveActiveCredentialsForNearbyNetworksWithCompletion:]
+ -[THClient storeCredentialsForBorderAgentInternally:networkName:extendedPANId:activeOperationalDataSet:teamID:completion:]
+ -[THCredentials initWithActiveDataSetRecord:]
+ ___122-[THClient storeCredentialsForBorderAgentInternally:networkName:extendedPANId:activeOperationalDataSet:teamID:completion:]_block_invoke
+ ___67-[THClient enableCredentialSharingModeForExtendedPANID:completion:]_block_invoke
+ ___69-[THClient retrieveActiveCredentialsForNearbyNetworksWithCompletion:]_block_invoke
+ ___77-[THClient enableCredentialSharingModeInternallyForExtendedPANID:completion:]_block_invoke
+ ___79-[THClient retrieveActiveCredentialsForNearbyNetworksInternallyWithCompletion:]_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e27_v24?0"NSSet"8"NSError"16ls32l8s40l8
+ _objc_msgSend$ctcsServerEnableCredentialSharingModeForExtendedPANID:completion:
+ _objc_msgSend$ctcsServerEnableCredentialSharingModeInternallyForExtendedPANID:completion:
+ _objc_msgSend$ctcsServerRetrieveActiveCredentialsForNearbyNetworksInternallyWithCompletion:
+ _objc_msgSend$ctcsServerRetrieveActiveCredentialsForNearbyNetworksWithCompletion:
+ _objc_msgSend$ctcsServerStoreThreadNetworkCredentialActiveDataSetInternally:network:credentialsDataSet:teamID:waitForSync:completion:
+ _objc_msgSend$handleActiveNearbyNetworksResponse:error:isInternal:completion:
+ _objc_msgSend$initWithActiveDataSetRecord:
+ _objc_msgSend$storeCredentialsForBorderAgentInternally:networkName:extendedPANId:activeOperationalDataSet:teamID:completion:
- -[THClient enableCredentialSharingModeInternallyWithExtendedPANId:completion:]
- -[THClient enableCredentialSharingModeWithExtendedPANId:completion:]
- ___115-[THClient storeCredentialsForBorderAgentInternally:networkName:extendedPANId:activeOperationalDataSet:completion:]_block_invoke
- ___68-[THClient enableCredentialSharingModeWithExtendedPANId:completion:]_block_invoke
- ___78-[THClient enableCredentialSharingModeInternallyWithExtendedPANId:completion:]_block_invoke
- _objc_msgSend$ctcsServerEnableCredentialSharingModeInternallyWithExtendedPANId:completion:
- _objc_msgSend$ctcsServerEnableCredentialSharingModeWithExtendedPANId:completion:
CStrings:
+ "-[THClient enableCredentialSharingModeForExtendedPANID:completion:]"
+ "-[THClient enableCredentialSharingModeForExtendedPANID:completion:]_block_invoke"
+ "-[THClient enableCredentialSharingModeInternallyForExtendedPANID:completion:]"
+ "-[THClient enableCredentialSharingModeInternallyForExtendedPANID:completion:]_block_invoke"
+ "Failed to retrieve nearby active record"
+ "Invalid input parameter: extendedPANID is required"
- "-[THClient enableCredentialSharingModeInternallyWithExtendedPANId:completion:]"
- "-[THClient enableCredentialSharingModeInternallyWithExtendedPANId:completion:]_block_invoke"
- "-[THClient enableCredentialSharingModeWithExtendedPANId:completion:]"
- "-[THClient enableCredentialSharingModeWithExtendedPANId:completion:]_block_invoke"
- "Invalid input parameter: xpanId is required"
```
