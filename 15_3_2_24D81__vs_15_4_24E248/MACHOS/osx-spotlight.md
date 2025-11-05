## osx-spotlight

> `/System/Library/PrivateFrameworks/DiagnosticExtensions.framework/PlugIns/osx-spotlight.appex/Contents/MacOS/osx-spotlight`

```diff

-130.0.0.0.0
-  __TEXT.__text: 0x2b2c
-  __TEXT.__auth_stubs: 0x230
+131.0.0.0.0
+  __TEXT.__text: 0x2b80
+  __TEXT.__auth_stubs: 0x210
   __TEXT.__objc_stubs: 0x720
-  __TEXT.__objc_methlist: 0x44
-  __TEXT.__const: 0x8
+  __TEXT.__objc_methlist: 0x8c
   __TEXT.__gcc_except_tab: 0x2a0
   __TEXT.__cstring: 0x601
   __TEXT.__oslogstring: 0x300

   __TEXT.__objc_methname: 0x4d6
   __TEXT.__objc_methtype: 0x73
   __TEXT.__unwind_info: 0xc8
-  __DATA_CONST.__auth_got: 0x128
-  __DATA_CONST.__got: 0x98
+  __DATA_CONST.__auth_got: 0x118
+  __DATA_CONST.__got: 0xa8
   __DATA_CONST.__const: 0x1a0
   __DATA_CONST.__cfstring: 0x540
   __DATA_CONST.__objc_classlist: 0x8

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x80
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x138
-  __DATA.__objc_selrefs: 0x1d8
+  __DATA.__objc_const: 0xd8
+  __DATA.__objc_selrefs: 0x1e0
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x120
   __DATA.__bss: 0x10

   - /System/Library/PrivateFrameworks/LoggingSupport.framework/Versions/A/LoggingSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0FE1CD54-AF66-3C98-9E67-9B9F200CD81D
+  UUID: 7608AAC2-54BA-39C0-BD26-C3A698618566
   Functions: 29
-  Symbols:   366
+  Symbols:   363
   CStrings:  182
 
Symbols:
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/DiagnosticExtensions/install/TempContent/Objects/DiagnosticExtensions.build/osx-spotlight.build/Objects-normal/arm64e/DEOSXSpotlightExtension.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DiagnosticExtensions/extensions/macosx/Spotlight.extension/
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Binaries/DiagnosticExtensions/install/TempContent/Objects/DiagnosticExtensions.build/osx-spotlight.build/Objects-normal/arm64e/DEOSXSpotlightExtension.o
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/DiagnosticExtensions/extensions/macosx/Spotlight.extension/
Functions:
~ -[DEOSXSpotlightExtension attachmentsForParameters:] : 1200 -> 1196
~ _Log : 140 -> 136
~ -[DEOSXSpotlightExtension collectIndexDropLogsOnSeedBuild] : 3896 -> 3928
~ __58-[DEOSXSpotlightExtension collectIndexDropLogsOnSeedBuild]_block_invoke.130 : 844 -> 884
~ __58-[DEOSXSpotlightExtension collectIndexDropLogsOnSeedBuild]_block_invoke.137 : 312 -> 300
~ -[DEOSXSpotlightExtension runUserDiagnosticsWithDestination:] : 1144 -> 1164
~ ___61-[DEOSXSpotlightExtension runUserDiagnosticsWithDestination:]_block_invoke : 312 -> 304
~ -[DEOSXSpotlightExtension runMDDiagnoseWithDestination:] : 1140 -> 1160
~ ___56-[DEOSXSpotlightExtension runMDDiagnoseWithDestination:]_block_invoke : 312 -> 304
~ ___Log_block_invoke : 80 -> 88

```
