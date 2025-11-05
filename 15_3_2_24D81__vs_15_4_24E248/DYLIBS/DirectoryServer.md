## DirectoryServer

> `/System/Library/PrivateFrameworks/DirectoryServer.framework/Versions/A/DirectoryServer`

```diff

 65.0.0.0.0
-  __TEXT.__text: 0x5904
-  __TEXT.__auth_stubs: 0x300
+  __TEXT.__text: 0x5800
+  __TEXT.__auth_stubs: 0x2f0
   __TEXT.__objc_methlist: 0x2bc
   __TEXT.__const: 0x10
   __TEXT.__gcc_except_tab: 0x10c
-  __TEXT.__cstring: 0xe97
+  __TEXT.__cstring: 0xe94
   __TEXT.__unwind_info: 0x168
   __TEXT.__objc_classname: 0x11
   __TEXT.__objc_methname: 0xaa4

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x408
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x190
+  __AUTH_CONST.__auth_got: 0x188
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__cfstring: 0xca0
   __AUTH_CONST.__objc_const: 0x268

   - /System/Library/PrivateFrameworks/DirectoryServer.framework/Frameworks/CFDirectoryServer.framework/Versions/A/CFDirectoryServer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1D576B72-DC62-3455-8BB3-D0A22DA13D8F
+  UUID: 04F287ED-8C8B-388F-9C43-E40B00B2C0FE
   Functions: 81
-  Symbols:   321
-  CStrings:  379
+  Symbols:   320
+  CStrings:  378
 
Symbols:
- _strncmp
Functions:
~ -[DSLocale description] : 524 -> 520
~ -[DSLocale addSubnet:] : 1108 -> 1092
~ -[DSLocale addServer:withIPAddr:] : 1268 -> 1152
~ -[DSLocale removeServer:withIPAddr:] : 876 -> 820
~ -[DSLocale updateXMLPlistInCompRec:withIPAddr:usingBlock:] : 1280 -> 1292
~ +[DSLocale createLocaleConfig:] : 684 -> 608
~ +[DSLocale createInterfaceLocales] : 564 -> 572
~ -[DSLog initWithName:andLogFilePath:] : 404 -> 392
~ -[DSLog logMessage:] : 164 -> 160
~ _DSRunTask : 1808 -> 1812
CStrings:
- "lo"

```
