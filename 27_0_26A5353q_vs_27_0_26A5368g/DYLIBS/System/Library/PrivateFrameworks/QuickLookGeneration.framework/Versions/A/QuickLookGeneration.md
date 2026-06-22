## QuickLookGeneration

> `/System/Library/PrivateFrameworks/QuickLookGeneration.framework/Versions/A/QuickLookGeneration`

```diff

-1110.0.0.0.0
-  __TEXT.__text: 0x464 sha256:8009b20e64754f9482534cfa7be6b341328d33bb090e479879a985a8daf91448
-  __TEXT.__objc_methlist: 0x17c sha256:32f93f9986e5bce76ab318fdc7fd19f9adf68f531a9d778cb764e51684de60d5
+1111.0.0.0.0
+  __TEXT.__text: 0x460 sha256:a13135f53a73a95f8ecf985e1b2822a2f8a4ac9e6cd0e9dd9d43310df7648af5
+  __TEXT.__objc_methlist: 0x17c sha256:bf9bfa11bd809ae16346c59860ccc6ffd1b27b38245371c26f9dee47222dae78
   __TEXT.__const: 0x48 sha256:6b434b24692f0474ccf005336c8949ec090eb98743d6b97245f419104a79f332
   __TEXT.__cstring: 0x25 sha256:ede04704b377ad8df6fd144e11b9a63eaafbb75d772b5592c6830b1f7e957734
-  __TEXT.__unwind_info: 0x70 sha256:4329347ee1dbe0572126834d0383b9f05a74e3aa3affc3215778613e586e5eee
+  __TEXT.__unwind_info: 0x70 sha256:717ced3fd07fef79091cef2407784e4d0bdffc6c274debf6c6bccfc42d49f672
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__objc_classlist: 0x10 sha256:5f07519cf09b6d27ef5ba084c7b7f3e203961dab265e06a9c6f31580d89da590
-  __DATA_CONST.__objc_protolist: 0x10 sha256:4fb4cf31528d303c19d744a4f29a3c5199f165c74ccf0a01e8c644509f260388
+  __DATA_CONST.__objc_classlist: 0x10 sha256:f5cbebcbee6b339a4382b6c53da47bcbe09512577ea10e3d11ce9ca5aec9ebeb
+  __DATA_CONST.__objc_protolist: 0x10 sha256:7bb03004fb91e855a8acb88ae8bf379549625db49dee64db8483a6fa5d7044b4
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
-  __DATA_CONST.__objc_selrefs: 0x110 sha256:d1fbfb094508dba5fa6bacd7363aa589f1c42af33dced02e2a82490cbe6259a5
+  __DATA_CONST.__objc_selrefs: 0x110 sha256:6247a08b715aa405036840d1941b1b190a622f76d2b5b023880d0532cdc84a38
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x30 sha256:37dff708df3b82e7cf28669f283137cf8b78f873807571796138dbbafccd124e
-  __AUTH_CONST.__objc_const: 0x2f8 sha256:937b5a921594bf0a6851764d2ae6126a1a2782ab7d2c2674e15f480b2bc77005
+  __AUTH_CONST.__const: 0x30 sha256:fca03655ce5ee276612e4bc1a8e36b07b07e902b17b86f47f5b87be6b211aa42
+  __AUTH_CONST.__objc_const: 0x2f8 sha256:1f4d4f95c59780d8055078fba132304616486a2e98fcc0631e09f6150292442b
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0xa0 sha256:7dc5af67b1c7d4296b85892b2df65985904c415bad2c2656960c7c81c28a6362
-  __DATA.__data: 0xc0 sha256:315e4afedc4fb6260b8f4c447fac1cbe27e2ff78b5ba5027540488fdfb24615d
+  __AUTH.__objc_data: 0xa0 sha256:3c09a5d2e86de9e221417c1c2f244011af2aa1f6dee8616cfb42c1d74e56261e
+  __DATA.__data: 0xc0 sha256:7c4a3a3e0a53d0e3d9883d1b2211ef52bd46f6d9288d7032b3d21cf890270caf
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /System/Library/PrivateFrameworks/QuickLookSupport.framework/Versions/A/QuickLookSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 608176C9-96BC-323D-B42F-3E83A7723FC8
+  UUID: D56747AA-FF1A-3076-A3C0-BF891E217F6A
   Functions: 6
   Symbols:   76
   CStrings:  1
Functions:
~ +[QLPreviewGenerationProvider providerForType:] : 320 -> 316
~ -[QLPreviewGenerationProvider providePreviewForFileRequest:completionHandler:] : sha256 5ec7a016157ba9a2501dec8efd8dfa21399f6ab9793713603eed7640ca268838 -> 796b18df9a07bad7f53cfa6dc8281e053b82d84830c31903573cbb223da48da6
~ -[QLTextGenerationPreviewProvider providePreviewForFileRequest:completionHandler:] : sha256 af9de2a7bd526d54de8db4e9b5aef35980ccebbd6a3326fc7532d78fe0ace71f -> e72bb5f3f080f5ea384b142eb2fa7ac4ab7ea31fda807823b83734aaceca1f7d
~ ___82-[QLTextGenerationPreviewProvider providePreviewForFileRequest:completionHandler:]_block_invoke : sha256 39595f05795094770384b6c692e5113094144dbb2aebfbb9ed3ce6b4b4efecaf -> e6d937707ebc90a3fc893421838c5cbb01a6ecb4f42d0cf19a94067638830c5c
~ ___copy_helper_block_e8_32s : sha256 1d96eaee8933568d328ba81ac28438e8655c66ca96e400fe815d18e55f2f4020 -> 015081ab7e797beb58c487122170d4c353a1295ef1bd80e59e4f65e4a1d85987
~ ___destroy_helper_block_e8_32s : sha256 2110415abf223ec73cffaebf1306824dbedc6ccff9a62c8071dabe14772af826 -> 8e92cf47c309bee536223c90e91300aa076051a3c35223e8d296c840a0039bd5

```
