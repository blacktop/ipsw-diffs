## CoreThread

> `/System/Library/PrivateFrameworks/CoreThread.framework/CoreThread`

```diff

-333.0.5.0.0
-  __TEXT.__text: 0x23ac
-  __TEXT.__auth_stubs: 0x250
+335.0.15.1.0
+  __TEXT.__text: 0x24e8
+  __TEXT.__auth_stubs: 0x210
   __TEXT.__objc_methlist: 0x598
   __TEXT.__const: 0x5a
   __TEXT.__cstring: 0x100
   __TEXT.__oslogstring: 0x29
-  __TEXT.__unwind_info: 0x110
+  __TEXT.__unwind_info: 0x120
   __TEXT.__objc_classname: 0x124
   __TEXT.__objc_methname: 0xb27
   __TEXT.__objc_methtype: 0x21e

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1e8
   __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x130
+  __AUTH_CONST.__auth_got: 0x110
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x300
   __AUTH_CONST.__objc_const: 0x1348

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 28EB5B71-C77F-3D41-ADE3-D9621F6F73A0
+  UUID: C4CDAE06-3AB4-3CCF-87DD-475330900DE0
   Functions: 104
-  Symbols:   486
+  Symbols:   482
   CStrings:  209
 
Symbols:
+ _objc_autoreleaseReturnValue
+ _objc_retain
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x25
- _objc_retain_x28
- _objc_retain_x6
Functions:
~ -[THFrozenThreadNetwork initWithCredentialsDataSet:creationDate:lastModificationDate:] : 188 -> 172
~ -[THThreadNetworkBorderAgent initWithBaDiscrId:] : 164 -> 160
~ -[THThreadNetworkBorderAgent initWithCoder:] : 120 -> 124
~ -[THThreadNetworkBorderAgent encodeWithCoder:] : 108 -> 112
~ -[THThreadNetworkCredentialsStoreRecord initWithNetwork:credentials:uniqueIdentifier:keychainAccessGroup:creationDate:lastModificationDate:] : 292 -> 272
~ -[THThreadNetworkCredentialsStoreRecord initWithCoder:] : 464 -> 488
~ -[THThreadNetworkCredentialsStoreRecord encodeWithCoder:] : 316 -> 340
~ -[THPreferredThreadNetwork initWithThreadNetwork:networkSignature:credentialsDataSetRecord:creationDate:lastModificationDate:userInfo:] : 296 -> 276
~ -[THPreferredThreadNetwork updateUserInfo:] : 12 -> 64
~ -[THPreferredThreadNetwork initWithCoder:] : 404 -> 424
~ -[THPreferredThreadNetwork encodeWithCoder:] : 316 -> 340
~ -[THThreadNetworkCredentialsDataSet initWithDataSetArray:userInfo:] : 152 -> 144
~ -[THThreadNetworkCredentialsDataSet initWithCoder:] : 164 -> 172
~ -[THThreadNetworkCredentialsDataSet encodeWithCoder:] : 156 -> 164
~ -[THThreadNetworkCredentialsActiveDataSetRecord initWithBorderAgent:credentialsDataSet:network:credentials:uniqueIdentifier:keychainAccessGroup:creationDate:lastModificationDate:] : 360 -> 332
~ -[THThreadNetworkCredentialsActiveDataSetRecord initWithCoder:] : 592 -> 624
~ -[THThreadNetworkCredentialsActiveDataSetRecord encodeWithCoder:] : 396 -> 428
~ -[THThreadNetworkCredentialsActiveDataSetRecord setCredentials:] : 12 -> 64
~ -[THThreadNetworkCredentials initWithMasterKey:passPhrase:PSKc:channel:PANID:userInfo:credentialDataSet:isActiveDevice:] : 320 -> 296
~ -[THThreadNetworkCredentials initWithCoder:] : 472 -> 500
~ -[THThreadNetworkCredentials encodeWithCoder:] : 436 -> 468
~ -[THThreadNetworkCredentials setCredentialsDataSet:] : 12 -> 64
~ -[THNetworkSignature initWithSignatures:ipv6NwSignature:wifSSID:wifiPassword:] : 236 -> 224
~ -[THNetworkSignature initWithCoder:] : 264 -> 280
~ -[THNetworkSignature encodeWithCoder:] : 236 -> 252
~ -[THThreadNetwork initWithName:extendedPANID:] : 192 -> 188
~ -[THThreadNetwork initWithCoder:] : 168 -> 176
~ -[THThreadNetwork encodeWithCoder:] : 156 -> 164
~ _THLogHandleForCategory : 84 -> 92

```
