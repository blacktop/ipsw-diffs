## CoreThread

> `/System/Library/PrivateFrameworks/CoreThread.framework/CoreThread`

```diff

-335.0.200.0.0
-  __TEXT.__text: 0x24e8
-  __TEXT.__auth_stubs: 0x210
+431.0.2.0.0
+  __TEXT.__text: 0x2354
   __TEXT.__objc_methlist: 0x598
   __TEXT.__const: 0x5a
-  __TEXT.__cstring: 0x100
+  __TEXT.__cstring: 0x10e
   __TEXT.__oslogstring: 0x29
-  __TEXT.__unwind_info: 0x120
-  __TEXT.__objc_classname: 0x124
-  __TEXT.__objc_methname: 0xb27
-  __TEXT.__objc_methtype: 0x21e
-  __TEXT.__objc_stubs: 0x540
-  __DATA_CONST.__got: 0x60
+  __TEXT.__unwind_info: 0x110
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x20
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1e8
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x110
+  __DATA_CONST.__got: 0x58
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x300
   __AUTH_CONST.__objc_const: 0x1348
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0xa0
   __DATA.__data: 0xc0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 550C3252-EB5B-3C44-910D-6C4054F5C877
+  UUID: EA66E8BA-7215-352E-BD6F-F3174F4A29F6
   Functions: 104
-  Symbols:   482
-  CStrings:  209
+  Symbols:   484
+  CStrings:  54
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x2
+ _objc_retain_x25
+ _objc_retain_x28
+ _objc_retain_x6
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_autoreleaseReturnValue
- _objc_retain
Functions:
~ -[THFrozenThreadNetwork initWithCredentialsDataSet:creationDate:lastModificationDate:] : 172 -> 188
~ -[THThreadNetworkBorderAgent initWithBaDiscrId:] : 160 -> 164
~ -[THThreadNetworkBorderAgent initWithCoder:] : 124 -> 120
~ -[THThreadNetworkBorderAgent encodeWithCoder:] : 112 -> 108
~ -[THThreadNetworkCredentialsStoreRecord initWithNetwork:credentials:uniqueIdentifier:keychainAccessGroup:creationDate:lastModificationDate:] : 272 -> 292
~ -[THThreadNetworkCredentialsStoreRecord initWithCoder:] : 488 -> 464
~ -[THThreadNetworkCredentialsStoreRecord encodeWithCoder:] : 340 -> 316
~ -[THPreferredThreadNetwork initWithThreadNetwork:networkSignature:credentialsDataSetRecord:creationDate:lastModificationDate:userInfo:] : 276 -> 296
~ -[THPreferredThreadNetwork updateUserInfo:] : 64 -> 12
~ -[THPreferredThreadNetwork initWithCoder:] : 424 -> 404
~ -[THPreferredThreadNetwork encodeWithCoder:] : 340 -> 316
~ -[THThreadNetworkCredentialsDataSet initWithDataSetArray:userInfo:] : 144 -> 152
~ -[THThreadNetworkCredentialsDataSet initWithCoder:] : 172 -> 164
~ -[THThreadNetworkCredentialsDataSet encodeWithCoder:] : 164 -> 156
~ -[THThreadNetworkCredentialsActiveDataSetRecord initWithBorderAgent:credentialsDataSet:network:credentials:uniqueIdentifier:keychainAccessGroup:creationDate:lastModificationDate:] : 332 -> 360
~ -[THThreadNetworkCredentialsActiveDataSetRecord initWithCoder:] : 624 -> 592
~ -[THThreadNetworkCredentialsActiveDataSetRecord encodeWithCoder:] : 428 -> 396
~ -[THThreadNetworkCredentialsActiveDataSetRecord setCredentials:] : 64 -> 12
~ -[THThreadNetworkCredentials initWithMasterKey:passPhrase:PSKc:channel:PANID:userInfo:credentialDataSet:isActiveDevice:] : 296 -> 320
~ -[THThreadNetworkCredentials initWithCoder:] : 500 -> 472
~ -[THThreadNetworkCredentials encodeWithCoder:] : 468 -> 436
~ -[THThreadNetworkCredentials setCredentialsDataSet:] : 64 -> 12
~ -[THNetworkSignature initWithSignatures:ipv6NwSignature:wifSSID:wifiPassword:] : 224 -> 236
~ -[THNetworkSignature initWithCoder:] : 280 -> 264
~ -[THNetworkSignature encodeWithCoder:] : 252 -> 236
~ -[THThreadNetwork initWithName:extendedPANID:] : 188 -> 192
~ -[THThreadNetwork initWithCoder:] : 176 -> 168
~ -[THThreadNetwork encodeWithCoder:] : 164 -> 156
~ _THLogHandleForCategory : 92 -> 84
~ -[THThreadNetworkCredentialsStoreRecord initWithCoder:].cold.1 : 148 -> 104
~ -[THThreadNetworkCredentialsActiveDataSetRecord initWithCoder:].cold.1 : 148 -> 104
CStrings:
- ".cxx_destruct"
- "@\"NSData\""
- "@\"NSDate\""
- "@\"NSString\""
- "@\"NSUUID\""
- "@\"THNetworkSignature\""
- "@\"THThreadNetwork\""
- "@\"THThreadNetworkBorderAgent\""
- "@\"THThreadNetworkCredentials\""
- "@\"THThreadNetworkCredentialsActiveDataSetRecord\""
- "@\"THThreadNetworkCredentialsDataSet\""
- "@16@0:8"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@32@0:8@16@24"
- "@40@0:8@16@24@32"
- "@48@0:8@16@24@32@40"
- "@56@0:8*16i24*28i36@40@48"
- "@60@0:8@16@24@32C40@44@52"
- "@64@0:8@16@24@32@40@48@56"
- "@72@0:8@16@24@32C40@44@52@60B68"
- "@80@0:8@16@24@32@40@48@56@64@72"
- "B"
- "B16@0:8"
- "C"
- "C16@0:8"
- "NSCoding"
- "NSSecureCoding"
- "PANID"
- "PSKc"
- "T@\"NSData\",C,N,V_PANID"
- "T@\"NSData\",C,N,V_PSKc"
- "T@\"NSData\",C,N,V_dataSetArray"
- "T@\"NSData\",C,N,V_masterKey"
- "T@\"NSData\",R,N,V_discriminatorId"
- "T@\"NSData\",R,N,V_extendedPANID"
- "T@\"NSData\",R,N,V_ipv4NwSignature"
- "T@\"NSData\",R,N,V_ipv6NwSignature"
- "T@\"NSDate\",R,N,V_creationDate"
- "T@\"NSDate\",R,N,V_lastModificationDate"
- "T@\"NSString\",C,N,V_passPhrase"
- "T@\"NSString\",C,N,V_userInfo"
- "T@\"NSString\",R,N,V_keychainAccessGroup"
- "T@\"NSString\",R,N,V_networkName"
- "T@\"NSString\",R,N,V_wifiPassword"
- "T@\"NSString\",R,N,V_wifiSSID"
- "T@\"NSUUID\",R,N,V_uniqueIdentifier"
- "T@\"THNetworkSignature\",R,N,V_networkSignature"
- "T@\"THThreadNetwork\",R,N,V_network"
- "T@\"THThreadNetworkBorderAgent\",R,N,V_borderAgent"
- "T@\"THThreadNetworkCredentials\",&,N,V_credentials"
- "T@\"THThreadNetworkCredentials\",R,N,V_credentials"
- "T@\"THThreadNetworkCredentialsActiveDataSetRecord\",R,N,V_credentialsDataSetRecord"
- "T@\"THThreadNetworkCredentialsDataSet\",&,N,V_credentialsDataSet"
- "T@\"THThreadNetworkCredentialsDataSet\",R,N,V_credentialsDataSet"
- "TB,N,V_isActiveDevice"
- "TB,R"
- "TC,N,V_channel"
- "THFrozenThreadNetwork"
- "THNetworkSignature"
- "THPreferredThreadNetwork"
- "THThreadNetwork"
- "THThreadNetworkBorderAgent"
- "THThreadNetworkCredentials"
- "THThreadNetworkCredentialsActiveDataSetRecord"
- "THThreadNetworkCredentialsDataSet"
- "THThreadNetworkCredentialsStoreRecord"
- "_PANID"
- "_PSKc"
- "_borderAgent"
- "_channel"
- "_creationDate"
- "_credentials"
- "_credentialsDataSet"
- "_credentialsDataSetRecord"
- "_dataSetArray"
- "_discriminatorId"
- "_extendedPANID"
- "_ipv4NwSignature"
- "_ipv6NwSignature"
- "_isActiveDevice"
- "_keychainAccessGroup"
- "_lastModificationDate"
- "_masterKey"
- "_network"
- "_networkName"
- "_networkSignature"
- "_passPhrase"
- "_uniqueIdentifier"
- "_userInfo"
- "_wifiPassword"
- "_wifiSSID"
- "borderAgent"
- "channel"
- "charValue"
- "copy"
- "creationDate"
- "credentialsDataSet"
- "credentialsDataSetRecord"
- "dataSetArray"
- "dataWithBytes:length:"
- "decodeBoolForKey:"
- "decodeObjectOfClass:forKey:"
- "discriminatorId"
- "encodeBool:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "extendedPANID"
- "init"
- "initSignaturesWithArrays:ipv4BytesLen:ipv6Bytes:ipv6BytesLen:wifSSID:wifiPassword:"
- "initWithBaDiscrId:"
- "initWithBorderAgent:credentialsDataSet:network:credentials:uniqueIdentifier:keychainAccessGroup:creationDate:lastModificationDate:"
- "initWithCoder:"
- "initWithCredentialsDataSet:creationDate:lastModificationDate:"
- "initWithDataSetArray:userInfo:"
- "initWithMasterKey:passPhrase:PSKc:channel:PANID:userInfo:"
- "initWithMasterKey:passPhrase:PSKc:channel:PANID:userInfo:credentialDataSet:isActiveDevice:"
- "initWithName:extendedPANID:"
- "initWithNetwork:credentials:uniqueIdentifier:keychainAccessGroup:creationDate:lastModificationDate:"
- "initWithSignatures:ipv6NwSignature:wifSSID:wifiPassword:"
- "initWithThreadNetwork:networkSignature:credentialsDataSetRecord:creationDate:lastModificationDate:userInfo:"
- "ipv4NwSignature"
- "ipv6NwSignature"
- "isActiveDevice"
- "keychainAccessGroup"
- "lastModificationDate"
- "length"
- "masterKey"
- "network"
- "networkName"
- "networkSignature"
- "numberWithUnsignedChar:"
- "passPhrase"
- "setChannel:"
- "setCredentials:"
- "setCredentialsDataSet:"
- "setDataSetArray:"
- "setIsActiveDevice:"
- "setMasterKey:"
- "setPANID:"
- "setPSKc:"
- "setPassPhrase:"
- "setUserInfo:"
- "supportsSecureCoding"
- "uniqueIdentifier"
- "updateUserInfo:"
- "userInfo"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8C16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "wifiPassword"
- "wifiSSID"

```
