## DiagnosticExtensionsDaemon

> `/System/Library/PrivateFrameworks/DiagnosticExtensionsDaemon.framework/DiagnosticExtensionsDaemon`

```diff

-199.0.0.0.0
-  __TEXT.__text: 0x6f9ac
+201.0.0.0.0
+  __TEXT.__text: 0x6fa90
   __TEXT.__auth_stubs: 0x950
   __TEXT.__objc_methlist: 0x6a2c
   __TEXT.__const: 0x278
   __TEXT.__cstring: 0x520b
   __TEXT.__gcc_except_tab: 0x1dbc
-  __TEXT.__oslogstring: 0x8525
+  __TEXT.__oslogstring: 0x8558
   __TEXT.__ustring: 0xc
   __TEXT.__unwind_info: 0x1aa8
   __TEXT.__objc_classname: 0x892

   __DATA_CONST.__objc_superrefs: 0x1a8
   __DATA_CONST.__objc_arraydata: 0x48
   __AUTH_CONST.__auth_got: 0x4b8
-  __AUTH_CONST.__const: 0xc00
+  __AUTH_CONST.__const: 0xc20
   __AUTH_CONST.__cfstring: 0x4ce0
   __AUTH_CONST.__objc_const: 0x12898
   __AUTH_CONST.__objc_arrayobj: 0x78

   __AUTH.__objc_data: 0xf00
   __DATA.__objc_ivar: 0x5ac
   __DATA.__data: 0xa40
-  __DATA.__bss: 0x188
+  __DATA.__bss: 0x198
   __DATA_DIRTY.__objc_data: 0x8c0
   __DATA_DIRTY.__bss: 0x228
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DDF01847-0DB8-3765-8810-9409F2769750
-  Functions: 2719
-  Symbols:   9482
+  UUID: 338FBF25-1476-3C10-AF1D-9548F13B70E3
+  Functions: 2721
+  Symbols:   9485
   CStrings:  5106
 
Symbols:
+ _LogEncryptor
+ _LogEncryptor.cold.1
+ _LogEncryptor.log
+ _LogEncryptor.onceToken
+ ___LogEncryptor_block_invoke
- -[DEDHealthLogsEncryptor encryptLogsAtPath:toDirectory:withMetadata:anonymousDeviceUUID:].cold.5
CStrings:
+ "Tried to use HealthLogsEncryptor without necessary parameters. The files at path: %{public}@ will be skipped. channel: %@, payloadType: %@, caseID: %@"
- "Tried to use HealthWrapEncryptor without a caseID specified. The files at path: %@ will be skipped."

```
