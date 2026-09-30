## libMobileCheckpoint.dylib

> `/usr/lib/libMobileCheckpoint.dylib`

```diff

 40.0.0.0.0
-  __TEXT.__text: 0x874 sha256:609c82ee9ebe22e79ad060e1eca6ad04cea86bfef77d5c777087980d27f91839
-  __TEXT.__auth_stubs: 0x1e0 sha256:4aed59ece31205a72c6f55ff5754c86e5a91715bc9a993a5b1bd24bb2255baa5
-  __TEXT.__cstring: 0x1dd sha256:59457ce34406af5ede4c21d8b2a774c20f01db44d4cfaa9efe626d8ea019834d
-  __TEXT.__unwind_info: 0x78 sha256:029a9d651e269c9697daf73414d1cd692c3a7f2bb0986783601227d6c24e5ed4
-  __TEXT.__objc_methname: 0x109 sha256:2b6744c3cd0e3f668e51ffa5f7746c91b940dd46841088c14be1b0e076e8f040
-  __TEXT.__objc_stubs: 0x160 sha256:f6bc0741a62561cef7105fbb96750ee937baca20ba720c4c6a1b774d7525ba4f
-  __DATA_CONST.__got: 0x38 sha256:d4817aa5497628e7c77e6b606107042bbba3130888c5f47a375e6179be789fbb
+  __TEXT.__text: 0x81c sha256:fec0852399f034ecbfffcfd71bc65c32d031edf3b07b8b2ba1e5158029c6bf01
+  __TEXT.__cstring: 0x1dd sha256:e087a8202e299b5e9195d89b3aeffbabab48dcef60115eb41b174cd523120858
+  __TEXT.__unwind_info: 0x78 sha256:60d396e5201fa3500f96eb6f26cd0d14e46b1d5fbcb651dfef09451d941499a3
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_methname: 0x0
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
-  __DATA_CONST.__objc_selrefs: 0x58 sha256:7c6a37ca836f9112a0bf338895694b51a925d1c0a319b274526b4ac14bad129d
-  __AUTH_CONST.__auth_got: 0xf8 sha256:b3ab6982980fddf460a2f47adb428475ce9afa89092fd034499d017a35993f05
-  __AUTH_CONST.__cfstring: 0x100 sha256:5fa9095ac4c49b6a7d7c88a32d32b77bbf4f0d101ef23a6bec9431c0da3495b1
+  __DATA_CONST.__objc_selrefs: 0x58 sha256:d3e6ee2addcc1798c83fac7cdb039249ab851f92efc5c3fe5bd4a1d027f4e14b
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__cfstring: 0x100 sha256:fad5019e8906476759585ae8de6fc1c952aef257bb39938797fa36104adaab48
+  __AUTH_CONST.__auth_got: 0x0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/MobileSystemServices.framework/MobileSystemServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 046DC12A-C965-3951-BD0A-35410A9E73A8
+  UUID: CED260CA-52F7-3791-88C2-A56326404FD7
   Functions: 5
-  Symbols:   57
-  CStrings:  31
+  Symbols:   56
+  CStrings:  20
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x20
- _objc_retain_x23
Functions:
~ _MCCopyCheckpoint : 592 -> 560
~ __cacheValid : 336 -> 324
~ _MCCopyCheckpointData : 352 -> 340
~ _MCCopyCheckpointValue : 644 -> 620
~ _getResponseForCommand : 240 -> 232
CStrings:
- "UTF8String"
- "dataWithPropertyList:format:options:error:"
- "dictionaryWithObjects:forKeys:count:"
- "initWithContentsOfFile:"
- "initWithContentsOfFile:options:error:"
- "initWithObjects:"
- "lastPathComponent"
- "numberWithUnsignedInt:"
- "objectForKey:"
- "stringWithFormat:"
- "stringWithUTF8String:"

```
