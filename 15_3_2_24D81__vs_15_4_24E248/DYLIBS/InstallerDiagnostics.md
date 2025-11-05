## InstallerDiagnostics

> `/System/Library/PrivateFrameworks/InstallerDiagnostics.framework/Versions/A/InstallerDiagnostics`

```diff

 79.0.0.0.0
-  __TEXT.__text: 0x9e1c
+  __TEXT.__text: 0x9da8
   __TEXT.__auth_stubs: 0x2f0
-  __TEXT.__objc_methlist: 0x4b8
+  __TEXT.__objc_methlist: 0x634
   __TEXT.__const: 0xa8
   __TEXT.__cstring: 0x1e27
   __TEXT.__oslogstring: 0x613

   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x430
+  __DATA_CONST.__objc_selrefs: 0x4c8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x620
   __AUTH_CONST.__auth_got: 0x188
   __AUTH_CONST.__const: 0x300
   __AUTH_CONST.__cfstring: 0x20a0
-  __AUTH_CONST.__objc_const: 0x1190
+  __AUTH_CONST.__objc_const: 0xed0
   __AUTH_CONST.__objc_intobj: 0x11d0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x1e0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 23397D5C-F71E-3EA2-8A81-232CC2E4AA06
-  Functions: 135
-  Symbols:   467
+  UUID: 74C7868B-0E71-390D-A56F-ECE10E110B46
+  Functions: 138
+  Symbols:   471
   CStrings:  794
 
Symbols:
+ +[IDDiagnosticsConnection sharedConnection].cold.1
+ +[IDDiagnosticsManager sharedManager].cold.1
+ +[IDDiagnosticsServer sharedServer].cold.1
+ _IDGetDefaultLogger.cold.1
Functions:
~ +[IDDiagnosticsConnection sharedConnection] : 84 -> 68
~ __IDGetDefaultLogger : 84 -> 68
~ +[IDDiagnosticsTransport convertJSONStringToDictionary:error:] : 252 -> 248
~ +[IDDiagnosticsTransport createPayloadFromData:currentBuild:seedProgram:watcherSession:forClient:] : 14232 -> 14160
- sub_1ad214f14
~ +[IDDiagnosticsManager sharedManager] : 84 -> 68
~ -[IDDiagnosticsStore(Compression) _compressData:forMessage:error:] : 348 -> 344
~ -[IDDiagnosticsStore(Compression) _decompressData:error:] : 320 -> 316
~ +[IDDiagnosticsServer sharedServer] : 84 -> 68
~ -[IDDiagnosticsServer listener:shouldAcceptNewConnection:] : 672 -> 668
~ __58-[IDDiagnosticsServer listener:shouldAcceptNewConnection:]_block_invoke.11 : 196 -> 192

```
