## DiagnosticExtensionsDaemon

> `/System/Library/PrivateFrameworks/DiagnosticExtensionsDaemon.framework/DiagnosticExtensionsDaemon`

```diff

-198.0.0.0.0
-  __TEXT.__text: 0x6faa0
+199.0.0.0.0
+  __TEXT.__text: 0x6f9ac
   __TEXT.__auth_stubs: 0x950
   __TEXT.__objc_methlist: 0x6a2c
   __TEXT.__const: 0x278
-  __TEXT.__cstring: 0x520e
-  __TEXT.__gcc_except_tab: 0x1da8
-  __TEXT.__oslogstring: 0x84e0
+  __TEXT.__cstring: 0x520b
+  __TEXT.__gcc_except_tab: 0x1dbc
+  __TEXT.__oslogstring: 0x8525
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x1a88
-  __TEXT.__objc_classname: 0x88f
-  __TEXT.__objc_methname: 0xee31
-  __TEXT.__objc_methtype: 0x234d
+  __TEXT.__unwind_info: 0x1aa8
+  __TEXT.__objc_classname: 0x892
+  __TEXT.__objc_methname: 0xee9e
+  __TEXT.__objc_methtype: 0x2332
   __TEXT.__objc_stubs: 0xbd20
   __DATA_CONST.__got: 0x6b0
   __DATA_CONST.__const: 0x2058

   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3918
+  __DATA_CONST.__objc_selrefs: 0x3930
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x1a8
   __DATA_CONST.__objc_arraydata: 0x48
   __AUTH_CONST.__auth_got: 0x4b8
   __AUTH_CONST.__const: 0xc00
-  __AUTH_CONST.__cfstring: 0x4c80
-  __AUTH_CONST.__objc_const: 0x12890
+  __AUTH_CONST.__cfstring: 0x4ce0
+  __AUTH_CONST.__objc_const: 0x12898
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0xf00
-  __DATA.__objc_ivar: 0x5a8
+  __DATA.__objc_ivar: 0x5ac
   __DATA.__data: 0xa40
   __DATA.__bss: 0x188
   __DATA_DIRTY.__objc_data: 0x8c0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 38944CD7-7B18-342D-956C-8DC584C880B1
-  Functions: 2718
-  Symbols:   9483
-  CStrings:  5093
+  UUID: DDF01847-0DB8-3765-8810-9409F2769750
+  Functions: 2719
+  Symbols:   9482
+  CStrings:  5106
 
Symbols:
+ +[DEDDeferredExtensionInfo activityStringForBugSessionIdentifier:dedIdentifier:].cold.1
+ -[DEDAEAEncryptor encryptLogsAtPath:toDirectory:withMetadata:anonymousDeviceUUID:]
+ -[DEDAEAEncryptor encryptLogsAtPath:toDirectory:withMetadata:anonymousDeviceUUID:].cold.1
+ -[DEDAEAEncryptor encryptLogsAtPath:toDirectory:withMetadata:anonymousDeviceUUID:].cold.2
+ -[DEDAEAEncryptor encryptLogsAtPath:toDirectory:withMetadata:anonymousDeviceUUID:].cold.3
+ -[DEDAEAEncryptor encryptLogsAtPath:toDirectory:withMetadata:anonymousDeviceUUID:].cold.4
+ -[DEDAEAEncryptor encryptLogsAtPath:toDirectory:withMetadata:anonymousDeviceUUID:].cold.5
+ -[DEDAEAEncryptor encryptLogsAtPath:toDirectory:withMetadata:anonymousDeviceUUID:].cold.6
+ -[DEDAEAEncryptor encryptLogsAtPath:toDirectory:withMetadata:anonymousDeviceUUID:].cold.7
+ -[DEDCloudKitFinisher anonymousDeviceUUID]
+ -[DEDCloudKitFinisher setAnonymousDeviceUUID:]
+ -[DEDHealthLogsEncryptor encryptLogsAtPath:toDirectory:withMetadata:anonymousDeviceUUID:]
+ -[DEDHealthLogsEncryptor encryptLogsAtPath:toDirectory:withMetadata:anonymousDeviceUUID:].cold.1
+ -[DEDHealthLogsEncryptor encryptLogsAtPath:toDirectory:withMetadata:anonymousDeviceUUID:].cold.2
+ -[DEDHealthLogsEncryptor encryptLogsAtPath:toDirectory:withMetadata:anonymousDeviceUUID:].cold.3
+ -[DEDHealthLogsEncryptor encryptLogsAtPath:toDirectory:withMetadata:anonymousDeviceUUID:].cold.4
+ -[DEDHealthLogsEncryptor encryptLogsAtPath:toDirectory:withMetadata:anonymousDeviceUUID:].cold.5
+ _OBJC_IVAR_$_DEDCloudKitFinisher._anonymousDeviceUUID
+ ___55-[DEDCloudKitFinisher finishSession:withConfiguration:]_block_invoke.125
+ _objc_msgSend$anonymousDeviceUUID
+ _objc_msgSend$decodeObjectForKey:
+ _objc_msgSend$encryptLogsAtPath:toDirectory:withMetadata:anonymousDeviceUUID:
+ _objc_msgSend$substringWithRange:
- -[DEDAEAEncryptor encryptLogsAtPath:outputDirectory:withMetadata:]
- -[DEDAEAEncryptor encryptLogsAtPath:outputDirectory:withMetadata:].cold.1
- -[DEDAEAEncryptor encryptLogsAtPath:outputDirectory:withMetadata:].cold.2
- -[DEDAEAEncryptor encryptLogsAtPath:outputDirectory:withMetadata:].cold.3
- -[DEDAEAEncryptor encryptLogsAtPath:outputDirectory:withMetadata:].cold.4
- -[DEDAEAEncryptor encryptLogsAtPath:outputDirectory:withMetadata:].cold.5
- -[DEDAEAEncryptor encryptLogsAtPath:outputDirectory:withMetadata:].cold.6
- -[DEDAEAEncryptor encryptLogsAtPath:outputDirectory:withMetadata:].cold.7
- -[DEDAEAEncryptor encryptLogsAtPath:outputDirectory:withPublicKey:]
- -[DEDHealthLogsEncryptor encryptLogsAtPath:outputDirectory:withMetadata:]
- -[DEDHealthLogsEncryptor encryptLogsAtPath:outputDirectory:withMetadata:].cold.1
- -[DEDHealthLogsEncryptor encryptLogsAtPath:outputDirectory:withMetadata:].cold.2
- -[DEDHealthLogsEncryptor encryptLogsAtPath:outputDirectory:withMetadata:].cold.3
- -[DEDHealthLogsEncryptor encryptLogsAtPath:outputDirectory:withMetadata:].cold.4
- -[DEDHealthLogsEncryptor encryptLogsAtPath:outputDirectory:withMetadata:].cold.5
- -[DEDHealthLogsEncryptor encryptLogsAtPath:outputDirectory:withPublicKey:]
- -[DEDHealthLogsEncryptor encryptLogsAtPath:outputDirectory:withPublicKey:].cold.1
- -[DEDHealthLogsEncryptor encryptLogsAtPath:outputDirectory:withPublicKey:].cold.2
- ___55-[DEDCloudKitFinisher finishSession:withConfiguration:]_block_invoke.112
- _objc_msgSend$encryptLogsAtPath:outputDirectory:withMetadata:
- _objc_msgSend$setAttachments:
- _objc_msgSend$setSandboxEnvironment:
- _objc_msgSend$setUploadedBytes:
CStrings:
+ ".%ld"
+ "1"
+ "@\"NSURL\"48@0:8@\"NSURL\"16@\"NSURL\"24@\"NSDictionary\"32@\"NSUUID\"40"
+ "@\"NSUUID\""
+ "T@\"NSUUID\",&,N,V_anonymousDeviceUUID"
+ "XPC activity identifier %@ is longer than %lu characters; truncating"
+ "_anonymousDeviceUUID"
+ "anonymousDeviceUUID"
+ "com.apple.diagnosticextensionsd.CloudKitMarkUploadComplete.%@"
+ "com.apple.diagnosticextensionsd.CloudKitUpload.%@"
+ "decodeObjectForKey:"
+ "deviceUUID"
+ "encryptLogsAtPath:toDirectory:withMetadata:anonymousDeviceUUID:"
+ "modelID"
+ "originalFilename"
+ "setAnonymousDeviceUUID:"
+ "substringWithRange:"
- "@\"NSURL\"40@0:8@\"NSURL\"16@\"NSURL\"24@\"NSDictionary\"32"
- "@\"NSURL\"40@0:8@\"NSURL\"16@\"NSURL\"24@\"NSString\"32"
- "com.apple.diagnosticextensionsd.%@.CloudKitMarkAttachmentUploadComplete"
- "com.apple.diagnosticextensionsd.%@.CloudKitUploadAttachments"
- "encryptLogsAtPath:outputDirectory:withMetadata:"
- "encryptLogsAtPath:outputDirectory:withPublicKey:"
- "timberlorry_archive"
- "v1-timberlorry_archive"

```
