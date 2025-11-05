## libtzupdate.dylib

> `/usr/lib/libtzupdate.dylib`

```diff

 88.0.0.0.0
-  __TEXT.__text: 0x3424
+  __TEXT.__text: 0x340c
   __TEXT.__auth_stubs: 0x220
-  __TEXT.__objc_methlist: 0x3f8
+  __TEXT.__objc_methlist: 0x418
   __TEXT.__const: 0x50
   __TEXT.__cstring: 0xe36
-  __TEXT.__unwind_info: 0x118
+  __TEXT.__unwind_info: 0x120
   __TEXT.__objc_classname: 0x96
   __TEXT.__objc_methname: 0xe8e
   __TEXT.__objc_methtype: 0x127

   __AUTH_CONST.__auth_got: 0x118
   __AUTH_CONST.__const: 0x110
   __AUTH_CONST.__cfstring: 0x940
-  __AUTH_CONST.__objc_const: 0x930
+  __AUTH_CONST.__objc_const: 0x8f8
   __AUTH.__objc_data: 0x280
   __DATA.__objc_ivar: 0x50
   __DATA.__data: 0x60

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 98CC3D9E-6F02-323C-8C06-2EB483DA0AB1
-  Functions: 87
-  Symbols:   323
+  UUID: C18DDA1B-39CD-334A-B8B2-3CAF2FD04C97
+  Functions: 90
+  Symbols:   326
   CStrings:  368
 
Symbols:
+ +[TZFileSystemInterface sharedInstance].cold.1
+ +[TZUpdate sharedInstance].cold.1
+ -[TZPreferencesController loggingLevel].cold.1
Functions:
~ +[TZFileSystemInterface sharedInstance] : 84 -> 68
~ -[TZFileSystemInterface systemICUTZSchemaVersion] : 320 -> 316
~ +[TZVersionInfo versionInfoWithDictionary:isPartial:] : 168 -> 164
~ +[TZVersionInfo _verifyVersionInfoDictionary:] : 1892 -> 1880
~ +[TZVersionInfo _tzDataVersionFromZoneinfoDirectory:withError:] : 388 -> 384
~ +[TZUpdate sharedInstance] : 84 -> 68
~ __42-[TZUpdate isUpdateWaitingWithCompletion:]_block_invoke.26 : 172 -> 168
~ ___41-[TZUpdate purgeAllAssetsWithCompletion:]_block_invoke_2 : 196 -> 192
~ -[TZPreferencesController loggingLevel] : 252 -> 232

```
