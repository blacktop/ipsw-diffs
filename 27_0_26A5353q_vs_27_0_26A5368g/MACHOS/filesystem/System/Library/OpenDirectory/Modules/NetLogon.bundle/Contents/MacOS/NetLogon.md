## NetLogon

> `/System/Library/OpenDirectory/Modules/NetLogon.bundle/Contents/MacOS/NetLogon`

```diff

 114.0.0.0.0
-  __TEXT.__text: 0x1250 sha256:3e26f61d1f425b568fd2b57f92e4f76a4ee0c066c5ac1f37f391176b850715ef
+  __TEXT.__text: 0x1258 sha256:e62328fc5af7cbf18f98c41b91709bbd879fed93ddb08de596403e3ba3d365b0
   __TEXT.__auth_stubs: 0x2d0 sha256:79c9b566013f7f7cc686f87534ff0d040c9ac73021fecfaa4845779bc68e62cc
   __TEXT.__const: 0x78 sha256:816096ae04ac69f79ded002407aa49b52c495b09e75e93e4c7b1143901d75806
   __TEXT.__cstring: 0x11c sha256:fcc78a18b4491d3e1bf8b3953171b3b757a89e9d1a73300788275392a7c94204
   __TEXT.__oslogstring: 0x107 sha256:aaeb6bef653e0261ab76515342f1464dc20503b6a981dec2985d2a8daa35b0de
-  __TEXT.__unwind_info: 0xa0 sha256:a53ef1ae2b409bdb94cf1b19f90cdfb21af93ecd466121d65296a3728f471ed2
-  __DATA_CONST.__const: 0x70 sha256:2126f7a41f3dc9580eafe9c21e75712e1587ba8fd6d0a0aaa151f68c685a4e14
-  __DATA_CONST.__cfstring: 0xa0 sha256:e547ba530ae924f3b3b8843d5876a752020bff2d546c14d03a5940e1f04b763d
+  __TEXT.__unwind_info: 0xa0 sha256:52f583fd55d28ee233d6de3f838b2e673414768c28d7dca8b17c253a044578b2
+  __DATA_CONST.__const: 0x70 sha256:97aa9b5164d14c85dc3fee845ed51a77e0264b2a134df1fd059cc6d6b207a96b
+  __DATA_CONST.__cfstring: 0xa0 sha256:f017b6a28ae74cd964288fa20f05130259f3c3681c6fc3d192076841bed66aa1
   __DATA_CONST.__auth_got: 0x168 sha256:0dd0aea78460197a7663ecca15841ccbe7c679e36e473008dddd1e34314df2fb
   __DATA_CONST.__got: 0x50 sha256:45fdd698b83fc2afc6ce5cd8636bc5c633f949bbe283d94c894cff70306d1b48
   __DATA.__bss: 0x10 sha256:b0f5f25a57a16bcd2661bd673c0bf7ea0623c2b87066588b9d5874314a83f554

   - /System/Library/PrivateFrameworks/CommonAuth.framework/Versions/A/CommonAuth
   - /System/Library/PrivateFrameworks/nt.framework/Versions/A/nt
   - /usr/lib/libSystem.B.dylib
-  UUID: 5A99FF9E-B70E-385B-ABBD-16E4345789BD
+  UUID: 0C3085EA-8D20-303E-91D6-99273F926798
   Functions: 16
   Symbols:   64
   CStrings:  32
Functions:
~ _odm_copy_auth_information : sha256 3dad59bc8bea8752b45ffc72cba47872fa7a47268fca87a2748e05476cfc252e -> 719527111d406e54959f6000a94dee872d2a3f39a4ea5268a2a220ea7144316a
~ _odm_RecordVerifyPassword : sha256 afd135c3d8594d3758d007f4afd19fe2af2529bac1493f1f2e0c64ff38ea1103 -> d2da2f25fa36da63c0fdc2ce5aff4c9cec2c35dfd0045d0d56bef987f09468ce
~ sub_ad0 : sha256 df94b6c7cdbb863df7708757bfef47a07a78a807a8065acfdeba5e9c75da3b3e -> 0cf94ef343d81c3fca96b7272e078067e56d6f4cecfc20eef44f02e86d672187
~ sub_bc8 : sha256 2802c579b13f02b2337eb5d9f178426a4f5859256170dc28486af6d2cb62edda -> 94c4de2ff96c825db56074d13feb7fe0e98a34fdcd5a463aa619e71b1490c95a
~ sub_c28 : sha256 2a36eb73e3cc3ee13e30a8fc4a9b44eb1e3e8bb738160c5c26456020cfbf0549 -> 01ca920b883f9ef419758c477420e465e4eed76c4666467ee7b6a2d95d754d10
~ sub_c78 : sha256 a65c3da51c1d917382ce8d66fb8a17fb07648d254ccb2d36095ac463053378ea -> f120083a3645d12ce3f4c209b271dde5696ced4d48ef6d10bdb4f29433d23ca7
~ _odm_RecordVerifyPasswordExtended : sha256 99ad08e6a2267f36438dded62ad7e69b8ae33f54cf449b08ea11ddb1d1376bb1 -> 649f80041cc8531c299005f0ecd7e526868a57fde9a7532c36d04f3ff99791ff
~ sub_10a8 : 988 -> 996
~ _odm_NodeVerifyCredentialsExtended : sha256 f78563f416486816eeb33c17663035f8000a3a9433d61dd8cbe3d1c9148a685f -> 1c9d1071a23eb3efdf570daec49737d3b38b08323622c6ea604945a3654dc32a
~ sub_16c8 -> sub_16d0 : sha256 89db6ce3d5ed1c644f450d31d95e87dc113bbd4efa11e2a344178130601d56a6 -> 8cacbefbc73770e49def7a367046555e31ecac89aa9d757d021d3fe9e2a03ba4
~ sub_18ac -> sub_18b4 : sha256 e98990c848d1f3b728c647c87ac28ca62fb8662979368fd2d0edaddb742e8184 -> be61ad1f64486c179b5953ea9fbf5f77c1ce5243e0795032fbb66228ec95730e
~ sub_1908 -> sub_1910 : sha256 6fad7cfd577c726e412f1535ebcb3cedb24bd0544437434246d737b5abfb1f3a -> 0da9e2bf2fede3f72902c36330eeb935c4670f80f307e8c0c5045c5ee0ab9861
~ sub_1948 -> sub_1950 : sha256 f1662b3933767dcb24f97483c4ee767edcab2114da8ecde234b7369081210a29 -> 9bf8883ccf65a47ea62bac70ab62f241b12341baf3559a787f6bffb41d4e1432

```
