## UAUPlugin

> `/System/Library/PrivateFrameworks/UAUPlugin.framework/Versions/A/UAUPlugin`

```diff

 533.0.0.0.0
-  __TEXT.__text: 0x1df4
+  __TEXT.__text: 0x1dbc
   __TEXT.__auth_stubs: 0x200
-  __TEXT.__objc_methlist: 0x248
+  __TEXT.__objc_methlist: 0x3c4
   __TEXT.__const: 0x50
   __TEXT.__cstring: 0x48e
   __TEXT.__oslogstring: 0x1c

   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b8
+  __DATA_CONST.__objc_selrefs: 0x350
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __AUTH_CONST.__auth_got: 0x110
   __AUTH_CONST.__const: 0xb0
   __AUTH_CONST.__cfstring: 0x420
-  __AUTH_CONST.__objc_const: 0x910
+  __AUTH_CONST.__objc_const: 0x660
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x38
   __DATA.__data: 0x120

   - /usr/lib/libDiagnosticMessagesClient.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 51BE570E-37ED-3034-A83F-1DC90623D2C7
-  Functions: 59
-  Symbols:   263
+  UUID: 4155F9CA-1E94-3492-9875-E071BEB22446
+  Functions: 60
+  Symbols:   264
   CStrings:  258
 
Symbols:
+ +[UAULogging logHandle].cold.1
Functions:
~ +[UAULogging logType:withString:] : 372 -> 324
~ +[UAULogging logHandle] : 84 -> 68
~ -[UAUSession runOnePlugin:withPrivilege:withCompletedSet:andQueue:] : 1052 -> 1048
~ -[UAUSession processPluginsWithPrivilege:] : 1132 -> 1124

```
