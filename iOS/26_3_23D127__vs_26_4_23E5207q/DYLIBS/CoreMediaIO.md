## CoreMediaIO

> `/System/Library/Frameworks/CoreMediaIO.framework/CoreMediaIO`

```diff

-5617.80.3.0.0
-  __TEXT.__text: 0x46e04
+5617.100.3.0.0
+  __TEXT.__text: 0x422f0
   __TEXT.__auth_stubs: 0xe30
-  __TEXT.__objc_methlist: 0x202c
+  __TEXT.__objc_methlist: 0x204c
   __TEXT.__const: 0xe8
-  __TEXT.__gcc_except_tab: 0x16b8
-  __TEXT.__cstring: 0x8505
-  __TEXT.__oslogstring: 0x4280
+  __TEXT.__gcc_except_tab: 0x16b0
+  __TEXT.__cstring: 0x877b
+  __TEXT.__oslogstring: 0x4266
   __TEXT.__dlopen_cstrs: 0xb8
   __TEXT.__unwind_info: 0xcb0
   __TEXT.__objc_classname: 0x3bc
-  __TEXT.__objc_methname: 0x4cca
-  __TEXT.__objc_methtype: 0x10e4
-  __TEXT.__objc_stubs: 0x3180
+  __TEXT.__objc_methname: 0x4d8f
+  __TEXT.__objc_methtype: 0x10f5
+  __TEXT.__objc_stubs: 0x31c0
   __DATA_CONST.__got: 0x270
   __DATA_CONST.__const: 0xd68
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xff0
+  __DATA_CONST.__objc_selrefs: 0x1008
   __DATA_CONST.__objc_superrefs: 0xd8
   __AUTH_CONST.__auth_got: 0x728
   __AUTH_CONST.__const: 0x340
   __AUTH_CONST.__cfstring: 0x2120
   __AUTH_CONST.__objc_const: 0x3a20
-  __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x368
   __DATA.__data: 0x4b0
   __DATA.__bss: 0xf8
-  __DATA_DIRTY.__objc_data: 0x820
+  __DATA_DIRTY.__objc_data: 0x870
   __DATA_DIRTY.__bss: 0x70
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7F5A97C0-CB24-351C-A390-6E87A47AC43E
-  Functions: 1331
-  Symbols:   4380
-  CStrings:  2231
+  UUID: 98D5C7F9-1125-340E-A910-116B6E78FF85
+  Functions: 1380
+  Symbols:   4534
+  CStrings:  2234
 
Symbols:
+ -[CMIOExtensionProvider _addSystemStatusAttributionsForClient:stream:requestVideo:requestAudio:]
+ -[CMIOExtensionProvider _removeSystemStatusAttributionsForClient:stream:allowAudioRemoval:]
+ -[CMIOExtensionProvider toggleVideoSystemStatusAttributionsForAllClientsOfStream:]
+ GCC_except_table280
+ GCC_except_table281
+ GCC_except_table285
+ GCC_except_table293
+ GCC_except_table295
+ GCC_except_table297
+ GCC_except_table306
+ GCC_except_table316
+ GCC_except_table329
+ GCC_except_table333
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_30
+ _objc_msgSend$_addSystemStatusAttributionsForClient:stream:requestVideo:requestAudio:
+ _objc_msgSend$_removeSystemStatusAttributionsForClient:stream:allowAudioRemoval:
- GCC_except_table276
- GCC_except_table277
- GCC_except_table278
- GCC_except_table290
- GCC_except_table292
- GCC_except_table294
- GCC_except_table300
- GCC_except_table313
- GCC_except_table326
- GCC_except_table327
CStrings:
+ "/Library/Caches/com.apple.xbs/716FD27A-9C9F-41F9-A2A1-5BA49DE92721/TemporaryDirectory.P4WHqp/Sources/CoreMediaIO/Sources/Common/Sources/CMIOSampleBuffer.c"
+ "/Library/Caches/com.apple.xbs/716FD27A-9C9F-41F9-A2A1-5BA49DE92721/TemporaryDirectory.P4WHqp/Sources/CoreMediaIO/Sources/Extensions/Sources/CMIOExtensionDiscoverySession.m"
+ "/Library/Caches/com.apple.xbs/716FD27A-9C9F-41F9-A2A1-5BA49DE92721/TemporaryDirectory.P4WHqp/Sources/CoreMediaIO/Sources/Extensions/Sources/CMIOExtensionProperties.m"
+ "/Library/Caches/com.apple.xbs/716FD27A-9C9F-41F9-A2A1-5BA49DE92721/TemporaryDirectory.P4WHqp/Sources/CoreMediaIO/Sources/Extensions/Sources/CMIOExtensionProvider.m"
+ "/Library/Caches/com.apple.xbs/716FD27A-9C9F-41F9-A2A1-5BA49DE92721/TemporaryDirectory.P4WHqp/Sources/CoreMediaIO/Sources/Extensions/Sources/CMIOExtensionProviderContext.m"
+ "/Library/Caches/com.apple.xbs/716FD27A-9C9F-41F9-A2A1-5BA49DE92721/TemporaryDirectory.P4WHqp/Sources/CoreMediaIO/Sources/Extensions/Sources/CMIOExtensionProviderHostContext.m"
+ "/Library/Caches/com.apple.xbs/716FD27A-9C9F-41F9-A2A1-5BA49DE92721/TemporaryDirectory.P4WHqp/Sources/CoreMediaIO/Sources/Extensions/Sources/CMIOExtensionProviderServer.m"
+ "/Library/Caches/com.apple.xbs/716FD27A-9C9F-41F9-A2A1-5BA49DE92721/TemporaryDirectory.P4WHqp/Sources/CoreMediaIO/Sources/Extensions/Sources/CMIOExtensionProxy.m"
+ "/Library/Caches/com.apple.xbs/716FD27A-9C9F-41F9-A2A1-5BA49DE92721/TemporaryDirectory.P4WHqp/Sources/CoreMediaIO/Sources/Extensions/Sources/CMIOExtensionSession.m"
+ "/Library/Caches/com.apple.xbs/716FD27A-9C9F-41F9-A2A1-5BA49DE92721/TemporaryDirectory.P4WHqp/Sources/CoreMediaIO/Sources/Extensions/Sources/CMIOExtensionUtilities.m"
+ "_addSystemStatusAttributionsForClient:stream:requestVideo:requestAudio:"
+ "_removeSystemStatusAttributionsForClient:stream:allowAudioRemoval:"
+ "toggleVideoSystemStatusAttributionsForAllClientsOfStream:"
+ "v36@0:8@16@24B32"
- "%s:%d:%s SetProperty - %@"
- "/Library/Caches/com.apple.xbs/Sources/CoreMediaIO/Sources/Common/Sources/CMIOSampleBuffer.c"
- "/Library/Caches/com.apple.xbs/Sources/CoreMediaIO/Sources/Extensions/Sources/CMIOExtensionDiscoverySession.m"
- "/Library/Caches/com.apple.xbs/Sources/CoreMediaIO/Sources/Extensions/Sources/CMIOExtensionProperties.m"
- "/Library/Caches/com.apple.xbs/Sources/CoreMediaIO/Sources/Extensions/Sources/CMIOExtensionProvider.m"
- "/Library/Caches/com.apple.xbs/Sources/CoreMediaIO/Sources/Extensions/Sources/CMIOExtensionProviderContext.m"
- "/Library/Caches/com.apple.xbs/Sources/CoreMediaIO/Sources/Extensions/Sources/CMIOExtensionProviderHostContext.m"
- "/Library/Caches/com.apple.xbs/Sources/CoreMediaIO/Sources/Extensions/Sources/CMIOExtensionProviderServer.m"
- "/Library/Caches/com.apple.xbs/Sources/CoreMediaIO/Sources/Extensions/Sources/CMIOExtensionProxy.m"
- "/Library/Caches/com.apple.xbs/Sources/CoreMediaIO/Sources/Extensions/Sources/CMIOExtensionSession.m"
- "/Library/Caches/com.apple.xbs/Sources/CoreMediaIO/Sources/Extensions/Sources/CMIOExtensionUtilities.m"

```
