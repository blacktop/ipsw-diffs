## DiagnosticExtensionsDaemon

> `/System/Library/PrivateFrameworks/DiagnosticExtensionsDaemon.framework/DiagnosticExtensionsDaemon`

```diff

-178.0.0.0.0
-  __TEXT.__text: 0x6e2e4
+181.0.0.0.0
+  __TEXT.__text: 0x6e348
   __TEXT.__auth_stubs: 0x980
   __TEXT.__objc_methlist: 0x5e2c
   __TEXT.__const: 0xd0
   __TEXT.__cstring: 0x5053
   __TEXT.__gcc_except_tab: 0x1438
-  __TEXT.__oslogstring: 0x8345
+  __TEXT.__oslogstring: 0x83a9
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x1930
+  __TEXT.__unwind_info: 0x18e0
   __TEXT.__objc_classname: 0x875
-  __TEXT.__objc_methname: 0xec53
+  __TEXT.__objc_methname: 0xec51
   __TEXT.__objc_methtype: 0x230a
   __TEXT.__objc_stubs: 0xbbc0
   __DATA_CONST.__got: 0x1c0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A7B933C5-6578-32DF-B559-CFBBE417D60D
-  Functions: 2737
-  Symbols:   9351
-  CStrings:  5067
+  UUID: 5392FE24-1B5F-3867-A375-DA3808D9E7DD
+  Functions: 2738
+  Symbols:   9353
+  CStrings:  5068
 
Symbols:
+ -[DEDCloudKitFinisher performCloudKitOperations]
+ -[DEDHealthLogsEncryptor encryptLogsAtPath:outputDirectory:withMetadata:].cold.5
+ ___48-[DEDCloudKitFinisher performCloudKitOperations]_block_invoke
+ ___48-[DEDCloudKitFinisher performCloudKitOperations]_block_invoke_2
+ _objc_msgSend$performCloudKitOperations
- -[DEDCloudKitFinisher _performCloudKitOperations]
- ___49-[DEDCloudKitFinisher _performCloudKitOperations]_block_invoke
- ___49-[DEDCloudKitFinisher _performCloudKitOperations]_block_invoke_2
- _objc_msgSend$_performCloudKitOperations
CStrings:
+ "Tried to use HealthWrapEncryptor without a caseID specified. The files at path: %@ will be skipped."
+ "performCloudKitOperations"
- "_performCloudKitOperations"

```
