## CoreThreadCommissionerServiced

> `/System/Library/PrivateFrameworks/CoreThreadCommissionerService.framework/CoreThreadCommissionerServiced`

```diff

-275.0.504.0.0
-  __TEXT.__text: 0x53110
-  __TEXT.__auth_stubs: 0xa80
-  __TEXT.__objc_stubs: 0x3040
-  __TEXT.__objc_methlist: 0x2060
-  __TEXT.__cstring: 0x7d5a
-  __TEXT.__objc_methname: 0x54f6
+323.0.0.0.0
+  __TEXT.__text: 0x55208
+  __TEXT.__auth_stubs: 0xa90
+  __TEXT.__objc_stubs: 0x31c0
+  __TEXT.__objc_methlist: 0x2088
+  __TEXT.__cstring: 0x7d71
+  __TEXT.__objc_methname: 0x5602
   __TEXT.__objc_classname: 0x2ea
-  __TEXT.__objc_methtype: 0x1632
-  __TEXT.__const: 0x130
-  __TEXT.__gcc_except_tab: 0x1a9c
-  __TEXT.__oslogstring: 0x8447
-  __TEXT.__unwind_info: 0x1000
-  __DATA_CONST.__auth_got: 0x558
-  __DATA_CONST.__got: 0x298
+  __TEXT.__objc_methtype: 0x1648
+  __TEXT.__const: 0x138
+  __TEXT.__gcc_except_tab: 0x1aa8
+  __TEXT.__oslogstring: 0x8b9e
+  __TEXT.__unwind_info: 0x1008
+  __DATA_CONST.__auth_got: 0x560
+  __DATA_CONST.__got: 0x278
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0xc68
-  __DATA_CONST.__cfstring: 0x1320
+  __DATA_CONST.__cfstring: 0x1300
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x58

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA.__objc_const: 0x2c10
-  __DATA.__objc_selrefs: 0x1140
+  __DATA.__objc_selrefs: 0x1198
   __DATA.__objc_ivar: 0xb4
   __DATA.__objc_data: 0x500
   __DATA.__data: 0x430

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 883E6A94-9623-38BB-BE86-81ED17BE4E40
-  Functions: 1259
-  Symbols:   264
-  CStrings:  2489
+  UUID: 912D4C9F-2113-351F-9200-1714F34577C0
+  Functions: 1274
+  Symbols:   261
+  CStrings:  2555
 
Symbols:
+ _bzero
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
CStrings:
+ " ==> Unknown type : %d"
+ " data_len : %d"
+ "%s:%d : Failed to create updated network signature!"
+ "%s:%d : Networks SSIDs (%@) are matching but signatures are not matching!"
+ "%s:%d Failed to create ipv4 temp sig"
+ "%s:%d Failed to create ipv4Key"
+ "%s:%d Failed to create ipv6Key"
+ "%s:%d: No need to update, signature entry for the same thread network exist : %@"
+ "%s:%d: current network signature ( ipv4 : %@, ipv6 : %@)"
+ "%s:%d: preferred network for network signature ( ipv4 : %@, ipv6 : %@)"
+ "-[THThreadNetworkCredentialsKeychainBackingStore areValidDataSetTLVs:creds:updateATS:isATSAppended:]"
+ "-[THThreadNetworkCredentialsKeychainBackingStore checkIfNetworkSignatureUpdateIsRequiredForPreferredNetworkCore:nwSignature:signaturePrefEntries:]"
+ "==> Decoded Channel Mask TLV"
+ "==> Decoded Channel mask, mask entry format is invalid"
+ "==> Decoded Network Name  "
+ "==> Decoded TLV, format is invalid, current position goes out of bound"
+ "==> Decoded XPAN ID"
+ "==> Decoded active timestamp"
+ "==> Decoded channel  "
+ "==> Decoded channel Len : %d"
+ "==> Decoded master key"
+ "==> Decoded mesh local prefix"
+ "==> Decoded pan id  "
+ "==> Decoded pskc"
+ "==> Decoded security policy  , len : %d"
+ "==> Invalid Mesh local prefix length %d"
+ "==> Invalid Security Policy length %d"
+ "==> Invalid extended pan id length %d"
+ "==> Invalid network key length %d"
+ "==> Invalid pan id length %d"
+ "==> Invalid pskc length %d,  "
+ "==> Invalid rotation time"
+ "==> error : Decoded Channel page is neither zero nor 2"
+ "==> error : Decoded entry length is not matching"
+ "Append complete : dataset: %s"
+ "Append complete : datasetTlvs : %@"
+ "Appending Dataset with Active Timestamp TLV"
+ "B44@0:8@16^@24B32^B36"
+ "Before appending - dataset: %s"
+ "Can not parse active timestamp tlv"
+ "Can not parse dataset tlvs"
+ "Channel : %d"
+ "Channel is not in the range : %d"
+ "Credential exists. Update instead."
+ "Credentials record could not be parsed"
+ "Duplicate type is detected:"
+ "Error decoding Network Name"
+ "Error during updating the preferred network with"
+ "Error during updating the record : (err=%d)"
+ "Master Key: %{sensitive}@"
+ "Network Name : %@"
+ "Not a dataset tlv"
+ "PANID : %@"
+ "PSKc : %{sensitive}@"
+ "Parsed dataset tlvs successfully"
+ "Sored Preferred Network with the name : %@"
+ "Validating Dataset"
+ "XPAN ID: %@"
+ "_setError"
+ "appendActiveTimeStampTLV:"
+ "areValidDataSetTLVs:creds:updateATS:isATSAppended:"
+ "borderAgent could not be allocated"
+ "checkAndAppendActiveTimeStampTLV: Invalid Active Timestamp tlv length %d"
+ "checkIfNetworkSignatureUpdateIsRequiredForPreferredNetworkCore:nwSignature:signaturePrefEntries:"
+ "containsObject:"
+ "credDataset could not be allocated"
+ "creds could not be parsed"
+ "creds master_key :%{sensitive}@"
+ "data"
+ "data_len : %d"
+ "dump: %{sensitive}s"
+ "getBytes:range:"
+ "hasError"
+ "network could not be parsed"
+ "numberWithChar:"
+ "position"
+ "security policy : %@"
+ "setPosition:"
- "#MOS borderAgent could not be allocated"
- "#MOS credDataset could not be allocated"
- "%@%@"
- "%s: #MOS : ==> Decoded security policy Line : %d, len : %d"
- "%s: #MOS : security policy : %@"
- "%s: %d: Can not parse dataset tlvs"
- "%s: %d: Not a dataset tlv"
- "%s: %d: Parsed dataset tlvs successfully"
- "%s: Validating Dataset : %d"
- "-[THThreadNetworkCredentialsKeychainBackingStore areValidDataSetTLVs:creds:]"
- "-[THThreadNetworkCredentialsKeychainBackingStore checkIfNetworkSignatureUpdateIsRequiredForPreferredNetwork:nwSignature:signaturePrefEntries:]"

```
