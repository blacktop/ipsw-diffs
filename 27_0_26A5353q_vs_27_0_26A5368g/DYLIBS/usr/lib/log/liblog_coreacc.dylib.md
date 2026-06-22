## liblog_coreacc.dylib

> `/usr/lib/log/liblog_coreacc.dylib`

```diff

-1176.0.26.0.0
-  __TEXT.__text: 0x1544 sha256:80b45ed2b27901aa8b2e639adc89d2bd0bae1191cc7c7b95efb8fd981a555cc7
+1196.0.0.0.0
+  __TEXT.__text: 0x1530 sha256:7d6218433f1c7d8c1b09f343e958b0e7c5390829f4de6bdb671f1003b2e10a9f
   __TEXT.__ustring: 0xa sha256:b0e464e7e73416f02b2e55653e73a1d6e086fa3944db7dfc2f50c9776fd541dd
   __TEXT.__cstring: 0xb83 sha256:f1359d821d2e35b3dfeadc39cf7662f7ec8931c36683e40dcafc86c627170302
-  __TEXT.__unwind_info: 0x98 sha256:814e446b2e50051b3cf9bcb31ce4876b297b0adad0f61a6e0d6d7d38373ebaa4
+  __TEXT.__unwind_info: 0x98 sha256:5a70e7b8599aebcddfd6588a8fae2849de845db97504121ce154d5e41283d26b
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_methname: 0x0
-  __DATA_CONST.__const: 0x408 sha256:3e25939bad2ec2e150352893d486bd4f359b600e17b0c29e9683608d708ec592
+  __DATA_CONST.__const: 0x408 sha256:42a6faed4f796606ba5b37be598736fa8971534eb372fbf4ecd114f9201fa5aa
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
-  __DATA_CONST.__objc_selrefs: 0x108 sha256:0ba6eee4dc7e7727b2bbcbfcab74af7c95f6d60d29bb36b4df83e5a40bf12d7e
+  __DATA_CONST.__objc_selrefs: 0x108 sha256:dd4a25b8b5535128b791f212cb8e1e48506fb80fac511995bc8c8558eb450d05
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__cfstring: 0xf60 sha256:ab1543173d9b608717d8efb3550b49d097fe544feb68b50044d12a5019f7122a
+  __AUTH_CONST.__cfstring: 0xf60 sha256:81c69c0aa5f886109ce8378721921e78a0b63572c336730aa31d8cce0b9fe41f
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__data: 0x190 sha256:2403def80689590044236fbc5835b6ffb15558104dc1af0d8053dc300c1e551f
+  __DATA.__data: 0x190 sha256:9ef530bb936193affef94dd8683ad2c6e3b453e31941e7717ac3ed3e13151d14
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ACF06147-6004-3BDE-B33D-62A63FBD08FC
+  UUID: A1979716-8F53-36A7-8B43-92E9952A2AD6
   Functions: 14
   Symbols:   84
   CStrings:  317
Functions:
~ _convertNSDataToNSString : 276 -> 272
~ _trimBidirectionalUnicodeCharacters : sha256 9245844f37c923c134d4a5563f4bbd1f14d7a7fe40b27e246892f4e61fbc4514 -> 9e05be5ca6ef93ba5907fd030747a354f1dff85aec840ca61ef6fc3d43674c44
~ _removeBidirectionalUnicodeCharacters : sha256 27e36d6bbeb8779551e3a8471ef73c63a664f955f5380939c14b443a8f8a8b47 -> 3d2f88bd38d0a28b7e66fdebb791f1a05458e403d879680cd70b98632e0e4791
~ _convertNSStringToNSData : 464 -> 460
~ _classImplementsMethodsInProtocol : 320 -> 316
~ _isNSObjectNull : sha256 1822edf5124ad57de751457f0129a8a9b8b095618670d01a6cb266f217615084 -> 17b9c38a04bc047d04b7680d63751b21c5401fe8d96fe4191c29df1a29c4f966
~ _NSObjectIfNotNull : sha256 33960bb19263d1f360c3e773ef54dec2d14ace40294b5e28e617b0ec6f5661f3 -> 601f52b03b703b931c764cee5bbe65fb97428cbe90604ef6bf2e8fc39bb59f96
~ _isNSObjectEqual : sha256 ce1de90eb8467b6cb8c8c4753e365175a83f6d3bd41016ff29827d2387d8fd6f -> 53ec8c6a0d997cdf112c8fabd33b122900596517919401da1e46eb4a9c8adf75
~ _castNSObjectToType : sha256 89b2396ba9c81919a421d23f49e0a547bc67b4228dc95ae082ef62ef3ff1b94a -> c2d899e0327818a92714ed882ec3f7a604f09157d4aa02f1d1b8c37610136b8e
~ _readJSONFile : sha256 522b6a19b6b3d921265e5527e5b795adfb8b6b3047f3272a0c1963f76344662e -> 26618c0fd661d7599d791e2e16dc18e40bcc1c0a43906d034fb132c38e2bc76d
~ _writeJSONFile : sha256 f7324d438cb7c589565680398b8c199fd842a1908904f7c622d2be9a3caf4e6e -> 8125c1d817caef9d6f7fac21d468863f4a0f405c9b2229813edb27caf02ae9cf
~ _base64EncodeArray : 344 -> 340
~ _base64DecodeArray : 356 -> 352
~ _OSLogCopyFormattedString : sha256 7e10c16e79a89c59783e3b799193a101d79d542d6bb7eb8b964f7ae58e2d049f -> 60d4c8a9fcbdcd187686457d7ac8b65fd455b5b4f0967ddbd341d73415b4fc58

```
