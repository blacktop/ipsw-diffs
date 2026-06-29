## DAAccount

> `/System/Library/DataClassMigrators/DAAccount.migrator/DAAccount`

```diff

-2691.4.7.0.0
-  __TEXT.__text: 0xe4 sha256:a95c39507a7330c67617952985f16b2a5af56d9c4c81b60d15d3ce55b01962ea
-  __TEXT.__auth_stubs: 0x50 sha256:f2456d783872e8b4dd43e310f007e912c16732ffd8963f65a30628785e8c07ff
-  __TEXT.__objc_methlist: 0x38 sha256:2cd46fdf5bfd3794dda6cb9c8aac45a43f03f096c4011ed515dabaf330a15941
+2691.6.1.0.0
+  __TEXT.__text: 0xe4 sha256:64a63c905a8e0c0172be87c77e5811494ef3f9051331b4684982da6a1aaba6c7
+  __TEXT.__auth_stubs: 0x50 sha256:82eddafd9e7d1d5ea74ddeb2e38b4f498fa284a7d078e5016396b97524c8e693
+  __TEXT.__objc_methlist: 0x38 sha256:58efa2e723345f69d4e6be31ab07decee629dd5b82df7d67b2bc1ac74d22334c
   __TEXT.__const: 0x4 sha256:fb360f7241a770dc32cade9a1d1273c92b13bd4959b1c130931312b7fe95e63f
   __TEXT.__cstring: 0xc sha256:7c025a28aea1e34899aa4269dea07052b7d1a64d82528bafb6d4afbb88b2d8c4
   __TEXT.__oslogstring: 0x3e sha256:fcb4d19fc3bb8941b583c474257ed9ab2ddbb9b5d90c3e4a7744fab674c78431

   __TEXT.__objc_classname: 0x12 sha256:996470f78aff9a53b9e0a1141a8214e8b67d5930033b5ae9fc3ef73ca81cd7c3
   __TEXT.__objc_methname: 0x98 sha256:4951535350d37c79f0e2949e040b5722f706fecffc82ca3f4d9359403cd3572a
   __TEXT.__objc_methtype: 0x18 sha256:6404870a6dbab538b4bdad51c08745b53e39f57fc4e93f7b87c1fbbc52729c46
-  __TEXT.__objc_stubs: 0x80 sha256:ccb0bafdc4d07a1c11053455cebf28f034b32c66d4f10f9df7d16d74118677a1
+  __TEXT.__objc_stubs: 0x80 sha256:4e944868baedfecd4d17a329b7ca45326ae8110bd829b6fb5e7b986101422b3a
   __DATA_CONST.__got: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
-  __DATA_CONST.__objc_classlist: 0x8 sha256:b7200fc6a4e9ab087366fe1873a1dc5e2bf687810e9c345a2f05163c93bb8cef
+  __DATA_CONST.__objc_classlist: 0x8 sha256:cc392bb3a971f4af8906474d66e754cdaad8525328d51d563ad425810c7ec1cb
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
-  __DATA_CONST.__objc_selrefs: 0x40 sha256:5c6019fa7dfb795a8fc3e394aeaadda5b1a48a368b1a324568e3ed78508b83e5
+  __DATA_CONST.__objc_selrefs: 0x40 sha256:0ec56863ee0da859af67d1ae4a7423105e95edc132a3438e012f47fe30d77044
   __AUTH_CONST.__auth_got: 0x30 sha256:17b0761f87b081d5cf10757ccc89f12be355c70e2e29df288b65b30710dcbcd1
-  __AUTH_CONST.__cfstring: 0x20 sha256:ebc9670f9e26f016ec7ac3dce81407ad9e5d88ddb79b106423518dd7f33f7070
-  __AUTH_CONST.__objc_const: 0x90 sha256:ab920d65041a3c63ec327009c34f4c4990318c4bba83e9303a1ca2ed8d9be039
-  __AUTH.__objc_data: 0x50 sha256:04e01b19d50063290192ff3ee45f8f9f40e41a79cabf36e8c8876b7f723e57d9
+  __AUTH_CONST.__cfstring: 0x20 sha256:4875f0eb281b062a4f424acfd1324a2c96d4071a6d04249a13e1920223444351
+  __AUTH_CONST.__objc_const: 0x90 sha256:348b041eb18f61e2a6b643cbfbeb9e7ba4b6250d7bcb017376fbc3a00d3f4493
+  __AUTH.__objc_data: 0x50 sha256:863659f59b40687d3bcc05be9e5c8086d0cc2ecc7eca10dbb0dc8ed51dfb4ff1
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ADCC1A78-19C7-32CB-8BE9-66E3794A8180
+  UUID: CD16298D-7E25-3E9B-B351-946CF33050E7
   Functions: 4
   Symbols:   30
   CStrings:  15
Functions:
~ -[DAAccountMigrator dataClassName] : sha256 5bd243033fb42bb936e72310da8c2d03a314aa3e316d9dd97ed235fc23e0ad9a -> 9d8ca630860c8eb6731fbe962e596c914fcd79e61c8e76af412197867922c90f
~ -[DAAccountMigrator performMigration] : sha256 b9abeb9048b50e6cd57e0f13c887ef535fe20595224bfb9fb11db14d48479504 -> b30d14825ac5dbb4cabb37d001bbe50ec70c930d3f0df511728d4c754119d92f

```
