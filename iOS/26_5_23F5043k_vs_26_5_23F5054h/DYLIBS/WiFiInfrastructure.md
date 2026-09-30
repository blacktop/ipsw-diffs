## WiFiInfrastructure

> `/System/Library/Frameworks/WiFiInfrastructure.framework/WiFiInfrastructure`

```diff

-1005.4.0.0.0
-  __TEXT.__text: 0x3cd30
-  __TEXT.__auth_stubs: 0xed0
-  __TEXT.__const: 0x7ef0
+1005.5.0.0.0
+  __TEXT.__text: 0x3dd40
+  __TEXT.__auth_stubs: 0xef0
+  __TEXT.__const: 0x8480
   __TEXT.__swift5_typeref: 0x18ee
-  __TEXT.__cstring: 0x582
+  __TEXT.__cstring: 0x1a1a
   __TEXT.__swift5_reflstr: 0x72d
   __TEXT.__swift5_assocty: 0x1c8
   __TEXT.__constg_swiftt: 0x1434

   __TEXT.__swift_as_ret: 0x68
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x1740
+  __TEXT.__unwind_info: 0x1758
   __TEXT.__eh_frame: 0x2290
   __TEXT.__objc_classname: 0x4df
   __TEXT.__objc_methname: 0x6d9

   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x210
-  __AUTH_CONST.__auth_got: 0x770
+  __AUTH_CONST.__auth_got: 0x780
   __AUTH_CONST.__const: 0x2f30
   __AUTH_CONST.__objc_const: 0xa98
   __AUTH.__objc_data: 0x140
   __AUTH.__data: 0xc80
-  __DATA.__data: 0x1530
-  __DATA.__bss: 0xeb80
+  __DATA.__data: 0x1568
+  __DATA.__bss: 0xecd0
   - /System/Library/Frameworks/AccessorySetupKit.framework/AccessorySetupKit
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6B99140E-AD9F-35A7-97EB-80F78263271A
-  Functions: 2005
-  Symbols:   1023
-  CStrings:  136
+  UUID: 24CECEDC-2463-33FE-9AAB-59043D8637F9
+  Functions: 2011
+  Symbols:   1024
+  CStrings:  208
 
Symbols:
+ _block_copy_helper.492
+ _block_copy_helper.498
+ _block_copy_helper.501
+ _block_copy_helper.584
+ _block_copy_helper.587
+ _block_descriptor.494
+ _block_descriptor.500
+ _block_descriptor.503
+ _block_descriptor.586
+ _block_descriptor.589
+ _block_destroy_helper.493
+ _block_destroy_helper.499
+ _block_destroy_helper.502
+ _block_destroy_helper.585
+ _block_destroy_helper.588
+ _objectdestroy.486Tm
+ _swift_getKeyPath
- _block_copy_helper.469
- _block_copy_helper.475
- _block_copy_helper.478
- _block_copy_helper.500
- _block_copy_helper.503
- _block_descriptor.471
- _block_descriptor.477
- _block_descriptor.480
- _block_descriptor.502
- _block_descriptor.505
- _block_destroy_helper.470
- _block_destroy_helper.476
- _block_destroy_helper.479
- _block_destroy_helper.501
- _block_destroy_helper.504
- _objectdestroy.463Tm
CStrings:
+ "Array<WINetworkSharingProvider.AccessPointConnection.Link>"
+ "Optional<WINetworkSharingProvider.Network.CaptivePortalLogin>"
+ "Optional<WINetworkSharingProvider.Network.Credentials.EAPCredentials.ClientIdentity>"
+ "Optional<WINetworkSharingProvider.Network.Credentials.EAPCredentials.FASTConfiguration>"
+ "Optional<WINetworkSharingProvider.Network.Credentials.EAPCredentials.TLSConfiguration.TLSVersion>"
+ "Optional<WINetworkSharingProvider.Network.Credentials.EAPCredentials.TLSConfiguration>"
+ "Optional<WINetworkSharingProvider.Network.Credentials.EAPCredentials.TTLSConfiguration.InnerAuthentication>"
+ "Optional<WINetworkSharingProvider.Network.Credentials.EAPCredentials.TTLSConfiguration>"
+ "Optional<WINetworkSharingProvider.Network.Credentials.EAPCredentials.UserLogin>"
+ "Set<WINetworkSharingProvider.Network.Credentials.EAPCredentials.EAPType>"
+ "Set<WINetworkSharingProvider.Network.SecurityPolicy>"
+ "WIChannel.number"
+ "WIMACAddress.Hash"
+ "WIMACAddress.Hash.Method"
+ "WIMACAddress.Hash.hash"
+ "WIMACAddress.Hash.method"
+ "WIMACAddress.Hash.salt"
+ "WINetworkSharingProvider.AccessPointConnection"
+ "WINetworkSharingProvider.AccessPointConnection.ID"
+ "WINetworkSharingProvider.AccessPointConnection.Link"
+ "WINetworkSharingProvider.AccessPointConnection.Link.ID"
+ "WINetworkSharingProvider.AccessPointConnection.Link.bssidHash"
+ "WINetworkSharingProvider.AccessPointConnection.Link.channel"
+ "WINetworkSharingProvider.AccessPointConnection.Link.id"
+ "WINetworkSharingProvider.AccessPointConnection.id"
+ "WINetworkSharingProvider.AccessPointConnection.links"
+ "WINetworkSharingProvider.AccessPointConnection.ssid"
+ "WINetworkSharingProvider.Network"
+ "WINetworkSharingProvider.Network.CaptivePortalLogin"
+ "WINetworkSharingProvider.Network.CaptivePortalLogin.userEnteredFormValues"
+ "WINetworkSharingProvider.Network.Credentials"
+ "WINetworkSharingProvider.Network.Credentials.EAPCredentials"
+ "WINetworkSharingProvider.Network.Credentials.EAPCredentials.ClientIdentity"
+ "WINetworkSharingProvider.Network.Credentials.EAPCredentials.ClientIdentity.certificate"
+ "WINetworkSharingProvider.Network.Credentials.EAPCredentials.ClientIdentity.certificateChain"
+ "WINetworkSharingProvider.Network.Credentials.EAPCredentials.ClientIdentity.privateKey"
+ "WINetworkSharingProvider.Network.Credentials.EAPCredentials.EAPType"
+ "WINetworkSharingProvider.Network.Credentials.EAPCredentials.FASTConfiguration"
+ "WINetworkSharingProvider.Network.Credentials.EAPCredentials.FASTConfiguration.provisionPACAnonymously"
+ "WINetworkSharingProvider.Network.Credentials.EAPCredentials.FASTConfiguration.usePAC"
+ "WINetworkSharingProvider.Network.Credentials.EAPCredentials.TLSConfiguration"
+ "WINetworkSharingProvider.Network.Credentials.EAPCredentials.TLSConfiguration.TLSVersion"
+ "WINetworkSharingProvider.Network.Credentials.EAPCredentials.TLSConfiguration.isCertificateRequired"
+ "WINetworkSharingProvider.Network.Credentials.EAPCredentials.TLSConfiguration.maximumTLSVersion"
+ "WINetworkSharingProvider.Network.Credentials.EAPCredentials.TLSConfiguration.minimumTLSVersion"
+ "WINetworkSharingProvider.Network.Credentials.EAPCredentials.TTLSConfiguration"
+ "WINetworkSharingProvider.Network.Credentials.EAPCredentials.TTLSConfiguration.InnerAuthentication"
+ "WINetworkSharingProvider.Network.Credentials.EAPCredentials.TTLSConfiguration.innerAuthentication"
+ "WINetworkSharingProvider.Network.Credentials.EAPCredentials.TrustedServers"
+ "WINetworkSharingProvider.Network.Credentials.EAPCredentials.TrustedServers.certificates"
+ "WINetworkSharingProvider.Network.Credentials.EAPCredentials.TrustedServers.names"
+ "WINetworkSharingProvider.Network.Credentials.EAPCredentials.UserLogin"
+ "WINetworkSharingProvider.Network.Credentials.EAPCredentials.UserLogin.password"
+ "WINetworkSharingProvider.Network.Credentials.EAPCredentials.UserLogin.username"
+ "WINetworkSharingProvider.Network.Credentials.EAPCredentials.acceptedEAPTypes"
+ "WINetworkSharingProvider.Network.Credentials.EAPCredentials.clientIdentity"
+ "WINetworkSharingProvider.Network.Credentials.EAPCredentials.fastConfiguration"
+ "WINetworkSharingProvider.Network.Credentials.EAPCredentials.outerIdentity"
+ "WINetworkSharingProvider.Network.Credentials.EAPCredentials.tlsConfiguration"
+ "WINetworkSharingProvider.Network.Credentials.EAPCredentials.trustedServers"
+ "WINetworkSharingProvider.Network.Credentials.EAPCredentials.ttlsConfiguration"
+ "WINetworkSharingProvider.Network.Credentials.EAPCredentials.userLogin"
+ "WINetworkSharingProvider.Network.ID"
+ "WINetworkSharingProvider.Network.SecurityPolicy"
+ "WINetworkSharingProvider.Network.captivePortalLogin"
+ "WINetworkSharingProvider.Network.credentials"
+ "WINetworkSharingProvider.Network.firstShared"
+ "WINetworkSharingProvider.Network.id"
+ "WINetworkSharingProvider.Network.isSSIDBroadcast"
+ "WINetworkSharingProvider.Network.lastModified"
+ "WINetworkSharingProvider.Network.securityPolicy"
+ "WINetworkSharingProvider.Network.ssid"

```
