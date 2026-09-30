## DAAccount

> `/System/Library/DataClassMigrators/DAAccount.migrator/DAAccount`

```diff

-2691.4.6.0.0
-  __TEXT.__text: 0xe4 sha256:a9e95aa79dacde7e9ee94702e32c8c28191ec99e6dd7f4fd0e43ccfb170a189a
-  __TEXT.__auth_stubs: 0x50 sha256:382feed0882093b99ea1ac7159305c0de922a7b46b567ade1b345dad55e9500a
-  __TEXT.__objc_methlist: 0x38 sha256:b2f3dafe3a66a5fcb6537439c5a5b13818469c4efef460c1e7fd20ccd8551809
+2691.4.7.0.0
+  __TEXT.__text: 0xe4 sha256:a95c39507a7330c67617952985f16b2a5af56d9c4c81b60d15d3ce55b01962ea
+  __TEXT.__auth_stubs: 0x50 sha256:f2456d783872e8b4dd43e310f007e912c16732ffd8963f65a30628785e8c07ff
+  __TEXT.__objc_methlist: 0x38 sha256:2cd46fdf5bfd3794dda6cb9c8aac45a43f03f096c4011ed515dabaf330a15941
   __TEXT.__const: 0x4 sha256:fb360f7241a770dc32cade9a1d1273c92b13bd4959b1c130931312b7fe95e63f
   __TEXT.__cstring: 0xc sha256:7c025a28aea1e34899aa4269dea07052b7d1a64d82528bafb6d4afbb88b2d8c4
   __TEXT.__oslogstring: 0x3e sha256:fcb4d19fc3bb8941b583c474257ed9ab2ddbb9b5d90c3e4a7744fab674c78431

   __TEXT.__objc_classname: 0x12 sha256:996470f78aff9a53b9e0a1141a8214e8b67d5930033b5ae9fc3ef73ca81cd7c3
   __TEXT.__objc_methname: 0x98 sha256:4951535350d37c79f0e2949e040b5722f706fecffc82ca3f4d9359403cd3572a
   __TEXT.__objc_methtype: 0x18 sha256:6404870a6dbab538b4bdad51c08745b53e39f57fc4e93f7b87c1fbbc52729c46
-  __TEXT.__objc_stubs: 0x80 sha256:19cbc2dc1c469c91142c9ea3b4c11e5043c493eac679b0198ebdda71ab779095
+  __TEXT.__objc_stubs: 0x80 sha256:ccb0bafdc4d07a1c11053455cebf28f034b32c66d4f10f9df7d16d74118677a1
   __DATA_CONST.__got: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
-  __DATA_CONST.__objc_classlist: 0x8 sha256:7270a6acfb29bf63ce306a5819836460dca26737302aab87efe7e10f43fe46a4
+  __DATA_CONST.__objc_classlist: 0x8 sha256:b7200fc6a4e9ab087366fe1873a1dc5e2bf687810e9c345a2f05163c93bb8cef
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
-  __DATA_CONST.__objc_selrefs: 0x40 sha256:7af1e247976899ce975a62cec285d1302f3182eba37f624eca8f8b1305ae4c80
+  __DATA_CONST.__objc_selrefs: 0x40 sha256:5c6019fa7dfb795a8fc3e394aeaadda5b1a48a368b1a324568e3ed78508b83e5
   __AUTH_CONST.__auth_got: 0x30 sha256:17b0761f87b081d5cf10757ccc89f12be355c70e2e29df288b65b30710dcbcd1
-  __AUTH_CONST.__cfstring: 0x20 sha256:83609a7504a88a8b209fa5d4f433b985c4f4f645b8d2cfd63a15d86ff29fd171
-  __AUTH_CONST.__objc_const: 0x90 sha256:e68be7e964fa733b5acb0d6622c3ac98d562e2ad8a86dfbd4f387451595cd81e
-  __AUTH.__objc_data: 0x50 sha256:fa97e007e1f4bf9f528547a8faf00310034425425acf629a4a12282bf60f6643
+  __AUTH_CONST.__cfstring: 0x20 sha256:ebc9670f9e26f016ec7ac3dce81407ad9e5d88ddb79b106423518dd7f33f7070
+  __AUTH_CONST.__objc_const: 0x90 sha256:ab920d65041a3c63ec327009c34f4c4990318c4bba83e9303a1ca2ed8d9be039
+  __AUTH.__objc_data: 0x50 sha256:04e01b19d50063290192ff3ee45f8f9f40e41a79cabf36e8c8876b7f723e57d9
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BAFC2B27-18E7-32AD-8BC2-9767F4280FD3
+  UUID: ADCC1A78-19C7-32CB-8BE9-66E3794A8180
   Functions: 4
   Symbols:   30
   CStrings:  15
Functions:
~ -[DAAccountMigrator dataClassName] : sha256 a01067833902d06e7d7cbe51509085adea43d4d06bc8a593ad81817391421f40 -> 5bd243033fb42bb936e72310da8c2d03a314aa3e316d9dd97ed235fc23e0ad9a
~ -[DAAccountMigrator performMigration] : sha256 f0b0cac27d4f8e7298b51db499e6d85ff6608cb733427d085ad3d56427af3fd0 -> b9abeb9048b50e6cd57e0f13c887ef535fe20595224bfb9fb11db14d48479504

```
