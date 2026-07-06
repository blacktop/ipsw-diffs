## NPKCompanionAgent

> `/System/Library/PrivateFrameworks/NanoPassKit.framework/NPKCompanionAgent`

```diff

-  __TEXT.__text: 0x423a8
-  __TEXT.__auth_stubs: 0xd40
+  __TEXT.__text: 0x423f0
+  __TEXT.__auth_stubs: 0xd60
   __TEXT.__objc_stubs: 0x7be0
-  __TEXT.__objc_methlist: 0x3588
+  __TEXT.__objc_methlist: 0x3590
   __TEXT.__const: 0xf8
   __TEXT.__gcc_except_tab: 0x1054
   __TEXT.__cstring: 0x28ba
-  __TEXT.__objc_methname: 0xc472
-  __TEXT.__oslogstring: 0x9ad3
+  __TEXT.__objc_methname: 0xc4d2
+  __TEXT.__oslogstring: 0x9ae7
   __TEXT.__objc_classname: 0x6c3
-  __TEXT.__objc_methtype: 0x3621
+  __TEXT.__objc_methtype: 0x3665
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__unwind_info: 0xe78
   __DATA_CONST.__const: 0x1f48

   __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__auth_got: 0x6b0
-  __DATA_CONST.__got: 0x6e0
-  __DATA.__objc_const: 0x5c20
-  __DATA.__objc_selrefs: 0x28a0
+  __DATA_CONST.__auth_got: 0x6c0
+  __DATA_CONST.__got: 0x6e8
+  __DATA.__objc_const: 0x5c28
+  __DATA.__objc_selrefs: 0x28a8
   __DATA.__objc_ivar: 0x1bc
   __DATA.__objc_data: 0x5f0
   __DATA.__data: 0xc68

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1155
-  Symbols:   447
-  CStrings:  2888
+  Symbols:   449
+  CStrings:  2890
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _NPKGetRemoteBiometricAuthenticationStatusSuspensionReason
+ _NSStringFromNPKIDVDeviceCredentialPrearmStatus
Functions:
~ sub_10001dd78 : 404 -> 476
CStrings:
+ "Notice: NPKIDVRemoteDeviceService: Found trustLost:%@ suspensionReason:%@ for remoteBiometricAuthenticationStatusForCredentialType:%@"
+ "paymentWebService:didFailToDownloadRemoteCloudStoreAssetWithLocalURL:forPassWithUniqueID:error:"
+ "v40@0:8@\"NPKIDVRemoteDevicesManager\"16Q24@?<v@?Bq>32"
+ "v48@0:8@\"PKPaymentWebService\"16@\"NSURL\"24@\"NSString\"32@\"NSError\"40"
- "Notice: NPKIDVRemoteDeviceService: Found trustLost:%@ for remoteBiometricAuthenticationStatusForCredentialType:%@"
- "v40@0:8@\"NPKIDVRemoteDevicesManager\"16Q24@?<v@?B>32"

```
