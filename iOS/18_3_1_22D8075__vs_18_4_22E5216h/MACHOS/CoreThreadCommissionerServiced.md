## CoreThreadCommissionerServiced

> `/System/Library/PrivateFrameworks/CoreThreadCommissionerService.framework/CoreThreadCommissionerServiced`

```diff

-265.0.53.0.0
-  __TEXT.__text: 0x5228c
-  __TEXT.__auth_stubs: 0xa90
-  __TEXT.__objc_stubs: 0x2fe0
-  __TEXT.__objc_methlist: 0x1814
-  __TEXT.__cstring: 0x7c33
-  __TEXT.__objc_methname: 0x533f
+275.0.103.0.0
+  __TEXT.__text: 0x53124
+  __TEXT.__auth_stubs: 0xa80
+  __TEXT.__objc_stubs: 0x3060
+  __TEXT.__objc_methlist: 0x2060
+  __TEXT.__cstring: 0x7d5a
+  __TEXT.__objc_methname: 0x54f6
   __TEXT.__objc_classname: 0x2ea
-  __TEXT.__objc_methtype: 0x153f
+  __TEXT.__objc_methtype: 0x1632
   __TEXT.__const: 0x130
-  __TEXT.__gcc_except_tab: 0x1a58
-  __TEXT.__oslogstring: 0x8344
-  __TEXT.__unwind_info: 0xfa0
-  __DATA_CONST.__auth_got: 0x560
+  __TEXT.__gcc_except_tab: 0x1aa8
+  __TEXT.__oslogstring: 0x8447
+  __TEXT.__unwind_info: 0x1000
+  __DATA_CONST.__auth_got: 0x558
   __DATA_CONST.__got: 0x298
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xbf0
-  __DATA_CONST.__cfstring: 0x1300
+  __DATA_CONST.__const: 0xc68
+  __DATA_CONST.__cfstring: 0x1320
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
   __DATA.__bss: 0x98
+  __DATA.__common: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1276
-  Symbols:   265
-  CStrings:  2329
+  Functions: 1259
+  Symbols:   264
+  CStrings:  2342
 
Symbols:
- _objc_retainAutoreleasedReturnValue
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
