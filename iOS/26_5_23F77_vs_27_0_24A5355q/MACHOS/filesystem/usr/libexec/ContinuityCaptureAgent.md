## ContinuityCaptureAgent

> `/usr/libexec/ContinuityCaptureAgent`

```diff

-665.120.8.0.0
-  __TEXT.__text: 0x280 sha256:635e20b3bc4da90d821ec609335b382f5980aa469b74f45ac156c98003a78240
-  __TEXT.__auth_stubs: 0x110 sha256:758be2c62e4546994b1e9679fbb67b025eb5f176c5714cc5d0b2db9a65b05468
-  __TEXT.__objc_stubs: 0xa0 sha256:5948a94273a42bd369d384fc51e809b4a4d99307fe51f5ebcf361704a760e52b
-  __TEXT.__const: 0x8 sha256:23839b32ea31a65d07e1d97755c9bcda9f3700cca0cf54beaccf954db44fc032
-  __TEXT.__cstring: 0x168 sha256:4b671aec266c1f290ed25d2492880c7868bfbc885c02c7862c37e260f3b7cc99
-  __TEXT.__oslogstring: 0x84 sha256:49b34bbddee2698c345aecc59d9e90d21e8f8c82cb283d553c784cdb138719b5
-  __TEXT.__objc_methname: 0x65 sha256:df1ae56a410aea163940a1033bc526422870732f1de28aaf4a265ff9c7339699
-  __TEXT.__unwind_info: 0x58 sha256:41840c33b931437a7972b6aafabece1aaf23bbb7cf3aac3262449dd93521b925
-  __DATA_CONST.__auth_got: 0x90 sha256:a6725f094753f245bed63e86bedcfbc5be6cc48866dfae54492d02b7d2e8cc24
-  __DATA_CONST.__got: 0x18 sha256:7bceafd9bc60d88bd000e62d15b84e95aac26191f51f1e2c8669858b53965d08
-  __DATA_CONST.__cfstring: 0xa0 sha256:3b46ee6ee348e338ccebf8d72db3dfd277c38314d721db19834b641f81ff5c91
+748.0.0.122.2
+  __TEXT.__text: 0x384 sha256:a3e9d437a487cd654997bcc4ae33fd8f659bd4c17e4d490bbfac52951ce9da8e
+  __TEXT.__auth_stubs: 0x120 sha256:4c265065394b01eb8c80bd8be2506bd65075bf4fbeef4a9e1e76614b9d7c8a9e
+  __TEXT.__objc_stubs: 0x20 sha256:1aadd03dd10c8bdec839486772ca376cc4f520b9a156b3109ea5c1069bf4f831
+  __TEXT.__const: 0x10 sha256:910690b0a2327b0e8eb82939436bdde900a5a0f142e1f5b63bdd246e4a370976
+  __TEXT.__cstring: 0x12c sha256:f3073db52cad7d5c3443012eac5ee2651125ea995a56cc4b144cad3867bcd1d4
+  __TEXT.__oslogstring: 0xf4 sha256:51b517e84a174ca3fb0a9e113e171aa94365fbd049ca37e215a81ad592c67021
+  __TEXT.__objc_methname: 0x19 sha256:1a8d82c5c44ef8b0b36f08dd3efcdb6a8094553fc4ed00250797f0169c09eb76
+  __TEXT.__unwind_info: 0x58 sha256:e9d878f7750a1740f37eccb2c9cc1e7563dda2993ee921c2df87004dfe467c55
+  __DATA_CONST.__const: 0x60 sha256:ebaf45ab6759a000b605a6ef0312a893aa673269bb501100333d50584d1e3984
+  __DATA_CONST.__cfstring: 0x60 sha256:7ceaad70d73ade0c89b657ec826acb0d153ef308d5348e24378e42670434ef49
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:1fa65ffcccc24c72d5d7f804a2be05ae57dfbb8769ffb33c4272ed6795b7e61c
-  __DATA.__objc_selrefs: 0x28 sha256:c89c8768864fc2fd2646ee2c1f61e769678dfcee2144d78e5ddd7841544f557c
-  __DATA.__bss: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
+  __DATA_CONST.__auth_got: 0x98 sha256:f5d5398f446364fbfa8c5fb67a55f79920aad8ac45edb19587e096b353ac71cf
+  __DATA_CONST.__got: 0x18 sha256:26b977e7b9b70c4d7fa9b1fcb2a53fb591986ba28cdf94299135089bdfc0040c
+  __DATA.__objc_selrefs: 0x10 sha256:9edcd4dffb0d95dec5b0203efd3d4d32d2c3ef4db4a9009a7d488400c2d61289
+  - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreMediaIO.framework/CoreMediaIO
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/PrivateFrameworks/CMContinuityCaptureCore.framework/CMContinuityCaptureCore
+  - /System/Library/PrivateFrameworks/CMContinuityCaptureHost.framework/CMContinuityCaptureHost
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 046D8A04-2F2E-32F6-9C42-BA2D6A0E70BC
-  Functions: 2
-  Symbols:   24
-  CStrings:  23
+  UUID: C311B137-2262-39C1-9615-57DE1996B603
+  Functions: 3
+  Symbols:   26
+  CStrings:  20
 
Symbols:
+ _CMContinuityCaptureLog
+ __NSConcreteGlobalBlock
+ __xpc_event_key_name
+ __xpc_type_dictionary
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _xpc_dictionary_create_reply
+ _xpc_dictionary_get_bool
+ _xpc_dictionary_get_string
+ _xpc_dictionary_send_reply
+ _xpc_get_type
+ _xpc_set_event_stream_handler
- _CFRunLoopRun
- _FigGetCFPreferenceBooleanWithDefault
- _OBJC_CLASS_$_CMContinuityCaptureProvider
- _OBJC_CLASS_$_NSFileManager
- _objc_alloc
- _objc_release_x8
- _objc_retainAutoreleasedReturnValue
- _objc_unsafeClaimAutoreleasedReturnValue
- _xpc_dictionary_create
- _xpc_dictionary_set_string
CStrings:
+ "ContinuityCaptureAgent stream event %s"
+ "Received launch event from CMIO %@"
+ "Received launch event from rapport %@"
+ "com.apple.cmio.ContinuityCaptureAgent.discovery"
+ "com.apple.rapport.matching"
+ "ignoreSIGTERM"
+ "replyRequired"
+ "v16@?0@\"NSObject<OS_xpc_object>\"8"
- "CMIOExtensionBundleIdentifier"
- "activate"
- "com.apple.cameracapture"
- "com.apple.cmio.ContinuityCaptureAgent"
- "com.apple.continuitycapture.hostLocalServer"
- "containerURLForSecurityApplicationGroupIdentifier:"
- "defaultManager"
- "group.com.apple.portrait.BackgroundReplacement"
- "initWithQueue:"

```
