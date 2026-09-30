## spotlighthelper

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/osx-spotlight.appex/Contents/XPCServices/spotlighthelper`

```diff

-130.0.0.0.0
-  __TEXT.__text: 0x107c
-  __TEXT.__auth_stubs: 0x130
+131.0.0.0.0
+  __TEXT.__text: 0x10c0
+  __TEXT.__auth_stubs: 0x110
   __TEXT.__objc_stubs: 0x460
-  __TEXT.__objc_methlist: 0x2c
+  __TEXT.__objc_methlist: 0x17c
   __TEXT.__objc_classname: 0x60
   __TEXT.__objc_methname: 0x4a8
   __TEXT.__objc_methtype: 0x149
   __TEXT.__cstring: 0x167
   __TEXT.__oslogstring: 0xf5
   __TEXT.__unwind_info: 0x80
-  __DATA_CONST.__auth_got: 0xa0
-  __DATA_CONST.__got: 0x78
+  __DATA_CONST.__auth_got: 0x90
+  __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0xb0
   __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA.__objc_const: 0x478
-  __DATA.__objc_selrefs: 0x130
+  __DATA.__objc_const: 0x228
+  __DATA.__objc_selrefs: 0x1d0
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x180
   __DATA.__bss: 0x10

   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/Versions/A/DiagnosticExtensions
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6395A30D-008C-30AA-A431-8CE8B736AD48
+  UUID: 1CAD5923-F7CC-30BD-8493-B27DA13D1637
   Functions: 14
-  Symbols:   215
+  Symbols:   210
   CStrings:  117
 
Symbols:
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/DiagnosticExtensions/install/TempContent/Objects/DiagnosticExtensions.build/spotlighthelper.build/Objects-normal/arm64e/main.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DiagnosticExtensions/extensions/macosx/Spotlight.extension/spotlighthelper/
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Binaries/DiagnosticExtensions/install/TempContent/Objects/DiagnosticExtensions.build/spotlighthelper.build/Objects-normal/arm64e/main.o
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/DiagnosticExtensions/extensions/macosx/Spotlight.extension/spotlighthelper/
Functions:
~ -[HelperDelegate listener:shouldAcceptNewConnection:] : 308 -> 316
~ ___53-[HelperDelegate listener:shouldAcceptNewConnection:]_block_invoke : 164 -> 160
~ _Log : 140 -> 136
~ __53-[HelperDelegate listener:shouldAcceptNewConnection:]_block_invoke.6 : 164 -> 160
~ -[HelperDelegate runDiagnosticWithDestinationDir:sandboxExtension:replyURL:] : 552 -> 560
~ ___76-[HelperDelegate runDiagnosticWithDestinationDir:sandboxExtension:replyURL:]_block_invoke : 2248 -> 2304
~ ___Log_block_invoke : 80 -> 88

```
