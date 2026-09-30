## UAUPlugin

> `/System/Library/PrivateFrameworks/UAUPlugin.framework/Versions/A/UAUPlugin`

```diff

-534.0.0.0.0
-  __TEXT.__text: 0x1ef4
+535.0.0.0.0
+  __TEXT.__text: 0x20f4
   __TEXT.__auth_stubs: 0x200
-  __TEXT.__objc_methlist: 0x3c4
+  __TEXT.__objc_methlist: 0x3ec
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x4e9
+  __TEXT.__cstring: 0x5d0
   __TEXT.__oslogstring: 0x1c
   __TEXT.__gcc_except_tab: 0xc4
   __TEXT.__unwind_info: 0xe0
   __TEXT.__objc_classname: 0x6b
-  __TEXT.__objc_methname: 0xa74
-  __TEXT.__objc_methtype: 0x205
-  __TEXT.__objc_stubs: 0x900
-  __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0x58
+  __TEXT.__objc_methname: 0xb4e
+  __TEXT.__objc_methtype: 0x220
+  __TEXT.__objc_stubs: 0x9c0
+  __DATA_CONST.__got: 0xa8
+  __DATA_CONST.__const: 0x60
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x350
+  __DATA_CONST.__objc_selrefs: 0x388
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__objc_arraydata: 0x8
   __AUTH_CONST.__auth_got: 0x110
   __AUTH_CONST.__const: 0xb0
-  __AUTH_CONST.__cfstring: 0x460
-  __AUTH_CONST.__objc_const: 0x660
+  __AUTH_CONST.__cfstring: 0x520
+  __AUTH_CONST.__objc_const: 0x690
+  __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x38
+  __DATA.__objc_ivar: 0x3c
   __DATA.__data: 0x120
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libDiagnosticMessagesClient.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DCD019BA-0E2B-3973-ACD0-1596F2324FA0
-  Functions: 60
-  Symbols:   264
-  CStrings:  262
+  UUID: 2B005F78-7AEF-32D6-9397-92E61BAC88BC
+  Functions: 63
+  Symbols:   277
+  CStrings:  283
 
Symbols:
+ -[UAUSession shouldAllowPasswordAccessForPlugin:]
+ -[UpdaterSessionParameters password]
+ -[UpdaterSessionParameters setPassword:]
+ OBJC_IVAR_$_UpdaterSessionParameters._password
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSKeyedArchiver
+ _UAUEnvUserPassword
+ __42-[UAUSession processPluginsWithPrivilege:]_block_invoke.135
+ _objc_msgSend$archivedDataWithRootObject:requiringSecureCoding:error:
+ _objc_msgSend$base64EncodedStringWithOptions:
+ _objc_msgSend$containsObject:
+ _objc_msgSend$copy
+ _objc_msgSend$setPassword:
+ _objc_msgSend$shouldAllowPasswordAccessForPlugin:
- __42-[UAUSession processPluginsWithPrivilege:]_block_invoke.129
CStrings:
+ ""
+ "&"
+ "@\"LACSExtractablePassword\""
+ "T@\"LACSExtractablePassword\",&,V_password"
+ "UAU: Plugin %@ allowed to receive LACSExtractablePassword"
+ "UAU: Plugin %@ is not allowed to receive LACSExtractablePassword"
+ "UAUEnvUserPassword"
+ "UAULaunch failed to decode LACSExtractablePassword: %@"
+ "_password"
+ "archivedDataWithRootObject:requiringSecureCoding:error:"
+ "base64EncodedStringWithOptions:"
+ "com.apple.FileVaultUpdaterPlugin"
+ "containsObject:"
+ "copy"
+ "password"
+ "setPassword:"
+ "shouldAllowPasswordAccessForPlugin:"
- "%"

```
