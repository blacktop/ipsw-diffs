## DeviceDataResetXPCServiceWorker

> `/System/Library/PrivateFrameworks/EmbeddedDataReset.framework/XPCServices/DeviceDataResetXPCServiceWorker.xpc/DeviceDataResetXPCServiceWorker`

```diff

-55.0.0.0.0
-  __TEXT.__text: 0x78c8
+56.0.0.0.0
+  __TEXT.__text: 0x7b4c
   __TEXT.__auth_stubs: 0x7b0
-  __TEXT.__objc_stubs: 0x1720
-  __TEXT.__objc_methlist: 0x1064
+  __TEXT.__objc_stubs: 0x1740
+  __TEXT.__objc_methlist: 0x1094
   __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0x1084
-  __TEXT.__oslogstring: 0xf8d
-  __TEXT.__objc_classname: 0x5f8
+  __TEXT.__cstring: 0x10d1
+  __TEXT.__oslogstring: 0xff6
+  __TEXT.__objc_classname: 0x61d
   __TEXT.__objc_methtype: 0x3bb
-  __TEXT.__objc_methname: 0x1758
+  __TEXT.__objc_methname: 0x177f
   __TEXT.__gcc_except_tab: 0x64
-  __TEXT.__unwind_info: 0x2e8
+  __TEXT.__unwind_info: 0x2f0
   __DATA_CONST.__auth_got: 0x3e8
-  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__got: 0x1e8
   __DATA_CONST.__const: 0x250
-  __DATA_CONST.__cfstring: 0xe20
-  __DATA_CONST.__objc_classlist: 0x190
+  __DATA_CONST.__cfstring: 0xe60
+  __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0x88
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x2a98
-  __DATA.__objc_selrefs: 0x700
+  __DATA.__objc_const: 0x2b28
+  __DATA.__objc_selrefs: 0x708
   __DATA.__objc_ivar: 0xb0
-  __DATA.__objc_data: 0xfa0
+  __DATA.__objc_data: 0xff0
   __DATA.__data: 0x240
   __DATA.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/Netrb.framework/Netrb
   - /System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy
   - /System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore
+  - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FEBB3DA2-6356-3589-9128-558584F5D2B7
-  Functions: 319
-  Symbols:   302
-  CStrings:  750
+  UUID: 5B37612B-D2FC-340D-8E97-E66656909CFA
+  Functions: 325
+  Symbols:   305
+  CStrings:  758
 
Symbols:
+ _OBJC_CLASS_$_DDRTaskRegenerateRapportSelfIdentity
+ _OBJC_CLASS_$_RPClient
+ _OBJC_METACLASS_$_DDRTaskRegenerateRapportSelfIdentity
CStrings:
+ "DDRTaskRegenerateRapportSelfIdentity"
+ "Failed regenerating Rapport self identity due to timeout."
+ "Failed to regenerate Rapport self identity: %@"
+ "ResetNetworkSettings"
+ "com.apple.devicedatareset.regenerateRapportSelfIdentity"
+ "regenerateSelfIdentity:withCompletion:"

```
