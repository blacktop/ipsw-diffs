## timemachinehelper

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/osx-timemachine.appex/Contents/XPCServices/timemachinehelper`

```diff

-130.0.0.0.0
-  __TEXT.__text: 0x1104
-  __TEXT.__auth_stubs: 0x130
+131.0.0.0.0
+  __TEXT.__text: 0x1144
+  __TEXT.__auth_stubs: 0x110
   __TEXT.__objc_stubs: 0x460
-  __TEXT.__objc_methlist: 0x2c
+  __TEXT.__objc_methlist: 0x17c
   __TEXT.__objc_classname: 0x5f
   __TEXT.__objc_methname: 0x4a8
   __TEXT.__objc_methtype: 0x149
   __TEXT.__cstring: 0x18c
   __TEXT.__oslogstring: 0x11c
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
-  UUID: F65ECAF4-EE47-3292-849C-CC012B3CD8FB
+  UUID: 80666646-058A-32AC-ABE6-6033DF94E4EA
   Functions: 14
-  Symbols:   215
+  Symbols:   210
   CStrings:  118
 
Symbols:
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/DiagnosticExtensions/install/TempContent/Objects/DiagnosticExtensions.build/timemachinehelper.build/Objects-normal/arm64e/main.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DiagnosticExtensions/extensions/macosx/TimeMachine.extension/timemachinehelper/
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Binaries/DiagnosticExtensions/install/TempContent/Objects/DiagnosticExtensions.build/timemachinehelper.build/Objects-normal/arm64e/main.o
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/DiagnosticExtensions/extensions/macosx/TimeMachine.extension/timemachinehelper/
Functions:
~ -[HelperDelegate listener:shouldAcceptNewConnection:] : 308 -> 316
~ ___53-[HelperDelegate listener:shouldAcceptNewConnection:]_block_invoke : 164 -> 160
~ _Log : 140 -> 136
~ __53-[HelperDelegate listener:shouldAcceptNewConnection:]_block_invoke.6 : 164 -> 160
~ -[HelperDelegate runDiagnosticWithDestinationDir:sandboxExtension:replyURL:] : 552 -> 560
~ ___76-[HelperDelegate runDiagnosticWithDestinationDir:sandboxExtension:replyURL:]_block_invoke : 2384 -> 2436
~ ___Log_block_invoke : 80 -> 88

```
