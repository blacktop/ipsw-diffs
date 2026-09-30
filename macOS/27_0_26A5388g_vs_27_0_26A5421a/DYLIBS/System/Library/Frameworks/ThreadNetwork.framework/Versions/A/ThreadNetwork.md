## ThreadNetwork

> `/System/Library/Frameworks/ThreadNetwork.framework/Versions/A/ThreadNetwork`

```diff

-438.0.0.0.0
-  __TEXT.__text: 0x106bc
-  __TEXT.__objc_methlist: 0xdc0
+442.0.0.0.0
+  __TEXT.__text: 0xf770
+  __TEXT.__objc_methlist: 0xe18
   __TEXT.__const: 0xb8
-  __TEXT.__cstring: 0x18e8
+  __TEXT.__cstring: 0x1913
   __TEXT.__oslogstring: 0xc67
   __TEXT.__gcc_except_tab: 0x190
-  __TEXT.__unwind_info: 0x3e0
+  __TEXT.__unwind_info: 0x3e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7f0
+  __DATA_CONST.__objc_selrefs: 0x830
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__got: 0x138
   __AUTH_CONST.__const: 0x600
-  __AUTH_CONST.__cfstring: 0x880
-  __AUTH_CONST.__objc_const: 0x1bd0
+  __AUTH_CONST.__cfstring: 0x8a0
+  __AUTH_CONST.__objc_const: 0x1be8
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0xfc

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 392
-  Symbols:   893
-  CStrings:  234
+  Functions: 399
+  Symbols:   906
+  CStrings:  235
 
Symbols:
+ -[THClient enableCredentialSharingModeForExtendedPANID:completion:]
+ -[THClient enableCredentialSharingModeInternallyForExtendedPANID:completion:]
+ -[THClient handleActiveNearbyNetworksResponse:error:isInternal:completion:]
+ -[THClient retrieveActiveCredentialsForNearbyNetworksInternallyWithCompletion:]
+ -[THClient retrieveActiveCredentialsForNearbyNetworksWithCompletion:]
+ -[THClient storeCredentialsForBorderAgentInternally:networkName:extendedPANId:activeOperationalDataSet:teamID:completion:]
+ -[THCredentials initWithActiveDataSetRecord:]
+ __67-[THClient enableCredentialSharingModeForExtendedPANID:completion:]_block_invoke
+ __77-[THClient enableCredentialSharingModeInternallyForExtendedPANID:completion:]_block_invoke
+ ___122-[THClient storeCredentialsForBorderAgentInternally:networkName:extendedPANId:activeOperationalDataSet:teamID:completion:]_block_invoke
+ ___67-[THClient enableCredentialSharingModeForExtendedPANID:completion:]_block_invoke
+ ___69-[THClient retrieveActiveCredentialsForNearbyNetworksWithCompletion:]_block_invoke
+ ___77-[THClient enableCredentialSharingModeInternallyForExtendedPANID:completion:]_block_invoke
+ ___79-[THClient retrieveActiveCredentialsForNearbyNetworksInternallyWithCompletion:]_block_invoke
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
- __68-[THClient enableCredentialSharingModeWithExtendedPANId:completion:]_block_invoke
- __78-[THClient enableCredentialSharingModeInternallyWithExtendedPANId:completion:]_block_invoke
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
