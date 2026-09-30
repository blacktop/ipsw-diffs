## liblog_coreacc.dylib

> `/usr/lib/log/liblog_coreacc.dylib`

```diff

-1147.120.2.0.0
-  __TEXT.__text: 0x14d8 sha256:18f6e99fa294184da94929bb85836d14ae5a96aea423b4b6aca352c8e14140fe
-  __TEXT.__auth_stubs: 0x190 sha256:cd6db3011cd79ceba6d66b67096a9fb75320a2c739c6d232f77d7b78fb0a2865
+1176.0.26.502.1
+  __TEXT.__text: 0x1488 sha256:430f27055f8493986b96a0f14de40e800d5264c73358a2c479d525ed17030dc1
   __TEXT.__ustring: 0xa sha256:b0e464e7e73416f02b2e55653e73a1d6e086fa3944db7dfc2f50c9776fd541dd
   __TEXT.__cstring: 0xb83 sha256:f1359d821d2e35b3dfeadc39cf7662f7ec8931c36683e40dcafc86c627170302
-  __TEXT.__unwind_info: 0x98 sha256:b3865a3bc294252df4552fea4f1fa8a070a900b78d525f2dc8594173e3c5f8c9
-  __TEXT.__objc_methname: 0x289 sha256:bf082b4762ec5aab33a5b841f6d66527cc18559ec7e617eda9aeb6145336cd6d
-  __TEXT.__objc_stubs: 0x420 sha256:761a0d924b2ee64cbcbf79ff3485fae73a08788e0f65168875e005de075bd209
-  __DATA_CONST.__got: 0x68 sha256:39f37f8d1931b3bdf767e7510dd69509fbf23af1f7654933d0a4d291cbdd4418
-  __DATA_CONST.__const: 0x408 sha256:0fb4115f4ad8c3adabbe823f4df1ae35d1823fed3cd6d5d70b5595dc1c9bf93b
+  __TEXT.__unwind_info: 0x98 sha256:bae1863b6a086e352e9f18ed52cb476e4b4e74f3fc907d872816a02984b7b8d7
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_methname: 0x0
+  __DATA_CONST.__const: 0x408 sha256:457fcc688e71283231a208fd7c399b63a831f5391f9ed6ad4098012b50e560ce
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
-  __DATA_CONST.__objc_selrefs: 0x108 sha256:2a1a7de4ebf22330e051d08eec5a19afd5b31247490cfa11e8dc9ef0d4f53cfb
-  __AUTH_CONST.__auth_got: 0xd0 sha256:46f531b7ea0428fbf2c3ca2b60e8dc33d6bbfa000e0fd1b489c5e39140a47006
-  __AUTH_CONST.__cfstring: 0xf60 sha256:6edcef163bca20464703d11cfa757bec3aef4c6877322f4b701781661957d09c
-  __DATA.__data: 0x190 sha256:c7318e2586a3138b4e5f0026fa8222167e75b00ed9448dd9c7dda37cdcad1721
+  __DATA_CONST.__objc_selrefs: 0x108 sha256:1ab7c6b6a5e89f7154ce0e9b9b44cb14484f418725bda39d638457f532714688
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__cfstring: 0xf60 sha256:b218a6b9f30d1c510f288c92e9f5a5422f7084ee2ae38b9314753c4b0344461f
+  __AUTH_CONST.__auth_got: 0x0
+  __DATA.__data: 0x190 sha256:cd834163409fd6ad7ac9462151f13071db0585ef21d7e5468beccd5e81017e23
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 821458F5-77C2-3C6F-B5F1-A229C89D45AE
+  UUID: 91A28A56-F87A-3501-8489-1E1A1A2C6EA6
   Functions: 14
-  Symbols:   90
-  CStrings:  350
+  Symbols:   92
+  CStrings:  317
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x1
- _objc_retainAutoreleasedReturnValue
Functions:
~ _convertNSDataToNSString : 256 -> 260
~ _trimBidirectionalUnicodeCharacters : 132 -> 124
~ _removeBidirectionalUnicodeCharacters : 164 -> 152
~ _convertNSStringToNSData : 456 -> 444
~ _classImplementsMethodsInProtocol : 316 -> 304
~ _isNSObjectNull : 112 -> 108
~ _NSObjectIfNotNull : 88 -> 84
~ _isNSObjectEqual : sha256 5dd797e6d92adc95afbe975a5a1a04f81d2d6f5a474a48feac1e34ceff8ef56e -> a66c7435770250f0c1293dd282c56da7aca4cfb343366b2a5c5e9925ed05a54e
~ _castNSObjectToType : sha256 5c11e78ce61e2ec7ba8f9eebd42850542ed0da8987e8635e66ff799c237519f5 -> 475d3485fb5f78f1919e1bc4b9af0a4ee87c43302b22aaf30343c084f9730134
~ _readJSONFile : 160 -> 152
~ _writeJSONFile : sha256 1d78f9c61ceab315eb53b38e5084f1449ea3ebe7598be742f1c4078a33cbdd94 -> 2ef1351ecfbca7bf603f8cf7fcfedebc6f78cf4d70a19ec0eebd62cfba962988
~ _base64EncodeArray : 332 -> 328
~ _base64DecodeArray : sha256 a65a57d06aa3fac966538cc56e36bf99a7c4578730cb87644dd30135b83cdfdf -> cf293eee9a3e796c6cad23572272f5820b83371cbab13d7a52c878afdf1a9f9d
~ _OSLogCopyFormattedString : 2660 -> 2640
CStrings:
- "JSONObjectWithData:options:error:"
- "UTF8String"
- "addObject:"
- "appendFormat:"
- "array"
- "base64EncodedStringWithOptions:"
- "boolValue"
- "characterSetWithCharactersInString:"
- "componentsJoinedByString:"
- "componentsSeparatedByCharactersInSet:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dataWithBytes:length:"
- "dataWithContentsOfFile:"
- "dataWithJSONObject:options:error:"
- "hexadecimalCharacterSet"
- "initWithBase64EncodedString:options:"
- "initWithString:"
- "instancesRespondToSelector:"
- "intValue"
- "invertedSet"
- "isEqual:"
- "isValidJSONObject:"
- "length"
- "null"
- "set"
- "setWithSet:"
- "stringByTrimmingCharactersInSet:"
- "stringWithFormat:"
- "stringWithString:"
- "unsignedIntegerValue"
- "writeToFile:atomically:"

```
