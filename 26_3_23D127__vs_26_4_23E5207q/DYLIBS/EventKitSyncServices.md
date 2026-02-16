## EventKitSyncServices

> `/System/Library/PrivateFrameworks/EventKitSyncServices.framework/EventKitSyncServices`

```diff

-420.0.0.0.0
-  __TEXT.__text: 0xdd8
-  __TEXT.__auth_stubs: 0x1e0
+420.1.0.0.0
+  __TEXT.__text: 0xea0
+  __TEXT.__auth_stubs: 0x1a0
   __TEXT.__objc_methlist: 0x254
   __TEXT.__const: 0x58
   __TEXT.__gcc_except_tab: 0x30
   __TEXT.__cstring: 0x141
   __TEXT.__oslogstring: 0x66
-  __TEXT.__unwind_info: 0xb8
+  __TEXT.__unwind_info: 0xd0
   __TEXT.__objc_classname: 0x6d
   __TEXT.__objc_methname: 0x45c
   __TEXT.__objc_methtype: 0x15a

   __DATA_CONST.__objc_selrefs: 0x1b8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x100
+  __AUTH_CONST.__auth_got: 0xe0
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x100
   __AUTH_CONST.__objc_const: 0x320

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EA2687D6-FE68-3B52-B021-3D7F88409585
+  UUID: 6DAA7213-2267-3E62-976B-FD61109F8B08
   Functions: 34
-  Symbols:   205
+  Symbols:   201
   CStrings:  120
 
Symbols:
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x8
Functions:
~ +[EKSSDiagnosticsService log] : 68 -> 84
~ -[EKSSDiagnosticsService init] : 100 -> 104
~ ___43-[EKSSDiagnosticsService _createConnection]_block_invoke : 176 -> 180
~ ___43-[EKSSDiagnosticsService _createConnection]_block_invoke.6 : 176 -> 180
~ -[EKSSDiagnosticsService dumpDiagnosticsWithCompletion:] : 172 -> 176
~ ___56-[EKSSDiagnosticsService dumpDiagnosticsWithCompletion:]_block_invoke : 180 -> 184
~ _EKSSServiceXPCInterface : 68 -> 84
~ ___EKSSServiceXPCInterface_block_invoke : 72 -> 76
~ _EKSSClientXPCInterface : 68 -> 84
~ ___EKSSClientXPCInterface_block_invoke : 72 -> 76
~ _EKSSDiagnosticsDirectory : 252 -> 264
~ +[EKSSLogger log] : 68 -> 84
~ -[EKSSLogger timestampLogForString:] : 172 -> 184
~ -[EKSSLogger mergeLogger:] : 108 -> 116
~ -[EKSSLogger writeLogFileWithDirectory:andFileName:] : 348 -> 364
~ -[EKSSLogger initWithCoder:] : 200 -> 208
~ -[EKSSLogger setLogText:] : 12 -> 64

```
