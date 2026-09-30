## MDMClientLibrary

> `/System/Library/PrivateFrameworks/MDMClientLibrary.framework/Versions/A/MDMClientLibrary`

```diff

-113.1.9.0.0
-  __TEXT.__text: 0x1c230
-  __TEXT.__objc_methlist: 0x1c2c
+113.40.17.0.0
+  __TEXT.__text: 0x1c71c
+  __TEXT.__objc_methlist: 0x1c6c
   __TEXT.__const: 0xc1
   __TEXT.__gcc_except_tab: 0x4c4
-  __TEXT.__cstring: 0x2388
-  __TEXT.__oslogstring: 0x239c
+  __TEXT.__cstring: 0x2372
+  __TEXT.__oslogstring: 0x24e1
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x9c8
+  __TEXT.__unwind_info: 0x9d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xa68
+  __DATA_CONST.__const: 0xa78
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12a8
+  __DATA_CONST.__objc_selrefs: 0x12d0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x70
-  __DATA_CONST.__got: 0x410
+  __DATA_CONST.__got: 0x418
   __AUTH_CONST.__const: 0x930
-  __AUTH_CONST.__cfstring: 0x3200
-  __AUTH_CONST.__objc_const: 0x39c0
+  __AUTH_CONST.__cfstring: 0x3260
+  __AUTH_CONST.__objc_const: 0x39c8
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1e0

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 660
-  Symbols:   2012
-  CStrings:  595
+  Functions: 665
+  Symbols:   2022
+  CStrings:  601
 
Symbols:
+ +[MDMCheckInRequest responseFromTransaction:]
+ +[MDMMAIDBearerTokenAuthenticator _createMissingAltDSIDErrorWithAccountID:]
+ -[MDMClientCore executeDeclarativeManagementRequestForEndpoint:requestData:completion:]
+ -[MDMCloudConfiguration organizationID]
+ -[MDMCloudConfiguration organizationType]
+ -[MDMConfigurationBase _nameForChannelType:]
+ GCC_except_table101
+ GCC_except_table91
+ GCC_except_table94
+ ___87-[MDMClientCore executeDeclarativeManagementRequestForEndpoint:requestData:completion:]_block_invoke
+ ___block_descriptor_56_e8_32s40bs_e5_v8?0l
+ _kCCOrganizationIDKey
+ _kCCOrganizationTypeKey
+ _kMDMChannelStringDevice
+ _kMDMChannelStringUser
+ _objc_msgSend$_createMissingAltDSIDErrorWithAccountID:
+ _objc_msgSend$_nameForChannelType:
+ _objc_msgSend$clientWithChannelType:
+ _objc_msgSend$dataWithContentsOfFile:options:error:
+ _objc_msgSend$executeDeclarativeManagementRequestForEndpoint:requestData:completion:
+ _objc_msgSend$responseFromTransaction:
- +[MDMProvisioningProfileTrust manualTrustSignerIdentities:]
- +[MDMProvisioningProfileTrust signerIdentitiesFromProvisioningProfileUUID:]
- GCC_except_table23
- GCC_except_table25
- GCC_except_table29
- GCC_except_table33
- GCC_except_table89
- GCC_except_table92
- GCC_except_table99
- ___block_descriptor_40_e8_32bs_e57_v32?0"MDMHTTPTransaction"8"NSDictionary"16"NSError"24l
- _objc_msgSend$executeRequestForMessageType:channelType:requestDict:completionHandler:
CStrings:
+ "DMC_MISSING_ALT_DSID_%@"
+ "Device"
+ "Failed to execute DeclarativeManagement request. Error: %{public}@"
+ "MDMConfigurationBase: dataWithContentsOfFile (%@) failed with error: %{public}@"
+ "Not exchanging MAID for bearer token, RM account %{public}@ has no altDSID"
+ "Not exchanging MAID for bearer token, no RM account with ID %{public}@: %{public}@"
+ "Refreshing MDM details. Channel: %{public}@"
+ "User"
- "Refreshing MDM details."
- "v32@?0@\"MDMHTTPTransaction\"8@\"NSDictionary\"16@\"NSError\"24"
```
