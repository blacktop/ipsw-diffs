## CoreThreadCommissionerServiced

> `/System/Library/PrivateFrameworks/CoreThreadCommissionerService.framework/CoreThreadCommissionerServiced`

```diff

-265.0.53.0.0
-  __TEXT.__text: 0x59bdc
+275.0.104.0.0
+  __TEXT.__text: 0x5ac80
   __TEXT.__auth_stubs: 0x940
-  __TEXT.__objc_stubs: 0x2fe0
-  __TEXT.__objc_methlist: 0x1814
-  __TEXT.__cstring: 0x7974
-  __TEXT.__objc_methname: 0x533f
+  __TEXT.__objc_stubs: 0x3040
+  __TEXT.__objc_methlist: 0x2060
+  __TEXT.__cstring: 0x7a9b
+  __TEXT.__objc_methname: 0x54f6
   __TEXT.__objc_classname: 0x2ea
-  __TEXT.__objc_methtype: 0x153f
+  __TEXT.__objc_methtype: 0x1632
   __TEXT.__const: 0x140
-  __TEXT.__gcc_except_tab: 0x1a90
-  __TEXT.__oslogstring: 0x84a0
-  __TEXT.__unwind_info: 0x1018
+  __TEXT.__gcc_except_tab: 0x1abc
+  __TEXT.__oslogstring: 0x85a3
+  __TEXT.__unwind_info: 0x1068
   __DATA_CONST.__auth_got: 0x4b8
   __DATA_CONST.__got: 0x2a8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xc60
-  __DATA_CONST.__cfstring: 0x12c0
+  __DATA_CONST.__const: 0xcf0
+  __DATA_CONST.__cfstring: 0x12e0
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x60
-  __DATA.__objc_const: 0x3b08
-  __DATA.__objc_selrefs: 0x1058
+  __DATA.__objc_const: 0x2c10
+  __DATA.__objc_selrefs: 0x1140
   __DATA.__objc_ivar: 0xb4
   __DATA.__objc_data: 0x500
   __DATA.__data: 0x430
-  __DATA.__common: 0x80
   __DATA.__bss: 0x88
+  __DATA.__common: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3B286F39-6BD8-349E-934A-36345581FEF8
-  Functions: 1320
+  UUID: 725EC6D0-47B0-3482-9502-11570A9F65DC
+  Functions: 1304
   Symbols:   246
-  CStrings:  2472
+  CStrings:  2486
 
CStrings:
+ "%s: %d : credentials dataset record is present for preferred network entry : %@, ssid : %@"
+ "%s: Preferred Network for network name : %@, Deletion result :(err=%d)"
+ "%s: Request to DELETE Preferred Network"
+ "%s: Request to DELETE Preferred Network Entry"
+ "%s: [%s]:KEY_NOT_FOUND in Frameworks, fallback to Default:[%d]"
+ "%s:%d: Request to fetch list of Preferred Network Entries"
+ "%s:Create CF String failed!"
+ "-[CTCSXPCService ctcsServerDeletePreferredNetworkForNetworkSignatureInternallyWithCompletion:extendedPANId:ipV4NwSignature:ipv6NwSignature:wifiSSID:completion:]"
+ "-[THThreadNetworkCredentialsKeychainBackingStore deletePreferredNetworkForNetworkSignatureInternallyWithCompletion:ipv4NwSignature:ipv6NwSignature:wifiSSID:completion:]_block_invoke"
+ "-[THThreadNetworkCredentialsKeychainBackingStore retrieveListOfPreferredNetworksInternallyWithCompletion:ipV4NwSignature:ipv6NwSignature:wifiSSID:showCurrentEntry:completion:]_block_invoke"
+ "Failed deleting Preferred Network name : %@, error :  %@"
+ "Failed to create query to delete preferred network for network name"
+ "Failed to read Preferred network entries; Backing store is nil"
+ "Unable to delete preferred network"
+ "Unable to read current preferred network"
+ "ctcsServerDeletePreferredNetworkForNetworkSignatureInternallyWithCompletion:extendedPANId:ipV4NwSignature:ipv6NwSignature:wifiSSID:completion:"
+ "ctcsServerRetrieveListOfPreferredNetworkEntriesInternallyWithCompletion:ipV4NwSignature:ipv6NwSignature:wifiSSID:showCurrentEntry:completion:"
+ "deletePreferredNetworkForNetworkSignatureInternallyWithCompletion:ipv4NwSignature:ipv6NwSignature:wifiSSID:completion:"
+ "getBoolValue_isFeatureEnabled"
+ "keyChainQueryForDeletePreferredNetworkRecordWithNetworkName:"
+ "keyChainQueryForPreferredNetworkRecordsOperationForNetworkName:"
+ "retrieveListOfPreferredNetworksInternallyWithCompletion:ipV4NwSignature:ipv6NwSignature:wifiSSID:showCurrentEntry:completion:"
+ "v56@0:8@\"THThreadNetwork\"16@\"NSData\"24@\"NSData\"32@\"NSString\"40@?<v@?@\"NSError\">48"
+ "v56@0:8@16@24@32@40@?48"
+ "v60@0:8@\"NSString\"16@\"NSData\"24@\"NSData\"32@\"NSString\"40B48@?<v@?@\"NSSet\"@\"NSError\">52"
+ "v64@0:8@\"NSString\"16@\"NSData\"24@\"NSData\"32@\"NSData\"40@\"NSString\"48@?<v@?@\"NSError\">56"
+ "v64@0:8@16@24@32@40@48@?56"
- "%s: %d : credentials dataset record is present for preferred network entry : %@"
- "%s: [%s]:KEY_NOT_FOUND in Frameworks"
- "-[CTCSXPCService ctcsServerDeletePreferredNetworkForNetworkSignatureInternallyWithCompletion:ipv6NwSignature:wifiSSID:completion:]"
- "-[THThreadNetworkCredentialsKeychainBackingStore deletePreferredNetworkForNetworkSignatureInternallyWithCompletion:ipv6NwSignature:wifiSSID:completion:]_block_invoke"
- "EnableAudioNoThreadFeature"
- "EnableThreadAlwaysOnFeature"
- "Request to DELETE Preferred Network"
- "Request to DELETE Preferred Network Entry"
- "ctcsServerDeletePreferredNetworkForNetworkSignatureInternallyWithCompletion:ipv6NwSignature:wifiSSID:completion:"
- "deletePreferredNetworkForNetworkSignatureInternallyWithCompletion:ipv6NwSignature:wifiSSID:completion:"
- "getBoolValue_isAudioNoThreadFeatureEnabled"
- "getBoolValue_isStateMachineEnabled"
- "getBoolValue_isThreadAlwaysOnFeatureEnabled"
- "v48@0:8@\"NSData\"16@\"NSData\"24@\"NSString\"32@?<v@?@\"NSError\">40"

```
