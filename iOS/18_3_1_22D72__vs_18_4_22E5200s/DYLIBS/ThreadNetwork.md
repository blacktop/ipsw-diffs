## ThreadNetwork

> `/System/Library/Frameworks/ThreadNetwork.framework/ThreadNetwork`

```diff

-265.0.53.0.0
-  __TEXT.__text: 0xceac
-  __TEXT.__auth_stubs: 0x420
-  __TEXT.__objc_methlist: 0x788
-  __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x1366
-  __TEXT.__oslogstring: 0x49a
+275.0.101.1.0
+  __TEXT.__text: 0xe7e8
+  __TEXT.__auth_stubs: 0x430
+  __TEXT.__objc_methlist: 0xb20
+  __TEXT.__const: 0xb0
+  __TEXT.__cstring: 0x14ec
+  __TEXT.__oslogstring: 0x4d1
   __TEXT.__gcc_except_tab: 0x1a4
-  __TEXT.__unwind_info: 0x360
-  __TEXT.__objc_classname: 0x11e
-  __TEXT.__objc_methname: 0x1c8a
-  __TEXT.__objc_methtype: 0x725
-  __TEXT.__objc_stubs: 0xda0
-  __DATA_CONST.__got: 0xc0
+  __TEXT.__unwind_info: 0x3c0
+  __TEXT.__objc_classname: 0x164
+  __TEXT.__objc_methname: 0x21e8
+  __TEXT.__objc_methtype: 0x83a
+  __TEXT.__objc_stubs: 0xf60
+  __DATA_CONST.__got: 0xd8
   __DATA_CONST.__const: 0x2c8
-  __DATA_CONST.__objc_classlist: 0x48
+  __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x508
+  __DATA_CONST.__objc_selrefs: 0x598
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x220
+  __DATA_CONST.__objc_superrefs: 0x58
+  __AUTH_CONST.__auth_got: 0x228
   __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x3a0
-  __AUTH_CONST.__objc_const: 0x1638
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0xa0
+  __AUTH_CONST.__cfstring: 0x4c0
+  __AUTH_CONST.__objc_const: 0x1a50
+  __AUTH.__objc_data: 0x1e0
+  __DATA.__objc_ivar: 0xe8
   __DATA.__data: 0x130
   __DATA.__bss: 0x28
   __DATA_DIRTY.__objc_data: 0x1e0

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 299
-  Symbols:   414
-  CStrings:  434
+  Functions: 344
+  Symbols:   469
+  CStrings:  492
 
Symbols:
+ _OBJC_CLASS_$_THNetworkSignature
+ _OBJC_CLASS_$_THPreferredNetworkEntry
+ _OBJC_CLASS_$_THPreferredThreadNetwork
+ _OBJC_METACLASS_$_THNetworkSignature
+ _OBJC_METACLASS_$_THPreferredNetworkEntry
+ _OBJC_METACLASS_$_THPreferredThreadNetwork
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x7
- _objc_retain_x5
CStrings:
+ "\x04"
+ "-[THClient ctcsDeletePreferredNetworkForNetworkSignatureInternallyWithCompletion:extendedPANId:ipV4NwSignature:ipv6NwSignature:wifiSSID:completion:]_block_invoke"
+ "-[THClient retrieveListOfPreferredNetworkEntriesInternally:ipV4NwSignature:ipv6NwSignature:wifiSSID:showCurrentEntry:completion:]"
+ "-[THClient retrieveListOfPreferredNetworkEntriesInternally:ipV4NwSignature:ipv6NwSignature:wifiSSID:showCurrentEntry:completion:]_block_invoke"
+ "@\"THCredentials\""
+ "@\"THNetworkSignature\""
+ "@\"THThreadNetworkCredentialsActiveDataSetRecord\""
+ "@48@0:8@16@24@32@40"
+ "@56@0:8*16i24*28i36@40@48"
+ "Client: %s:%d - Read list of Preferred Network Entries"
+ "Failed to retrieve Preferred Network Entry"
+ "T@\"NSData\",R,N,V_ipv4NwSignature"
+ "T@\"NSData\",R,N,V_ipv4Signature"
+ "T@\"NSData\",R,N,V_ipv6NwSignature"
+ "T@\"NSData\",R,N,V_ipv6Signature"
+ "T@\"NSString\",R,N,V_wifiPassword"
+ "T@\"NSString\",R,N,V_wifiSSID"
+ "T@\"THCredentials\",R,N,V_credentialsRecord"
+ "T@\"THNetworkSignature\",R,N,V_networkSignature"
+ "T@\"THThreadNetworkCredentialsActiveDataSetRecord\",R,N,V_credentialsDataSetRecord"
+ "THNetworkSignature"
+ "THPreferredNetworkEntry"
+ "THPreferredThreadNetwork"
+ "_credentialsDataSetRecord"
+ "_credentialsRecord"
+ "_ipv4NwSignature"
+ "_ipv4Signature"
+ "_ipv6NwSignature"
+ "_ipv6Signature"
+ "_networkSignature"
+ "_wifiPassword"
+ "_wifiSSID"
+ "credentialsDataSetRecord"
+ "credentialsRecord"
+ "creds"
+ "ctcsDeletePreferredNetworkForNetworkSignatureInternallyWithCompletion:extendedPANId:ipV4NwSignature:ipv6NwSignature:wifiSSID:completion:"
+ "ctcsServerDeletePreferredNetworkForNetworkSignatureInternallyWithCompletion:extendedPANId:ipV4NwSignature:ipv6NwSignature:wifiSSID:completion:"
+ "ctcsServerRetrieveListOfPreferredNetworkEntriesInternallyWithCompletion:ipV4NwSignature:ipv6NwSignature:wifiSSID:showCurrentEntry:completion:"
+ "dataWithBytes:length:"
+ "initPrefEntry:extendedPANID:ipv4Signature:ipv6Signature:wifiSSID:creationDate:lastModificationDate:credentialsRecord:"
+ "initSignaturesWithArrays:ipv4BytesLen:ipv6Bytes:ipv6BytesLen:wifSSID:wifiPassword:"
+ "initWithSignatures:ipv6NwSignature:wifSSID:wifiPassword:"
+ "initWithThreadNetwork:networkSignature:credentialsDataSetRecord:creationDate:lastModificationDate:userInfo:"
+ "ipv4"
+ "ipv4NwSignature"
+ "ipv4Signature"
+ "ipv6"
+ "ipv6NwSignature"
+ "ipv6Signature"
+ "networkSignature"
+ "passwd"
+ "retrieveListOfPreferredNetworkEntriesInternally:ipV4NwSignature:ipv6NwSignature:wifiSSID:showCurrentEntry:completion:"
+ "sig"
+ "ssid"
+ "ui"
+ "updateUserInfo:"
+ "v60@0:8@\"NSString\"16@\"NSData\"24@\"NSData\"32@\"NSString\"40B48@?<v@?@\"NSSet\"@\"NSError\">52"
+ "v60@0:8@16@24@32@40B48@?52"
+ "v64@0:8@\"NSString\"16@\"NSData\"24@\"NSData\"32@\"NSData\"40@\"NSString\"48@?<v@?@\"NSError\">56"
+ "v64@0:8@16@24@32@40@48@?56"
+ "wifiPassword"
+ "wifiSSID"
+ "wifissid"
- "-[THClient ctcsDeletePreferredNetworkForNetworkSignatureInternallyWithCompletion:ipv6NwSignature:wifiSSID:completion:]_block_invoke"
- "ctcsDeletePreferredNetworkForNetworkSignatureInternallyWithCompletion:ipv6NwSignature:wifiSSID:completion:"
- "ctcsServerDeletePreferredNetworkForNetworkSignatureInternallyWithCompletion:ipv6NwSignature:wifiSSID:completion:"
- "v48@0:8@\"NSData\"16@\"NSData\"24@\"NSString\"32@?<v@?@\"NSError\">40"
- "v48@0:8@16@24@32@?40"

```
