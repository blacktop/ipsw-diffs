## OSAnalyticsPrivate

> `/System/Library/PrivateFrameworks/OSAnalyticsPrivate.framework/OSAnalyticsPrivate`

```diff

-927.40.4.0.0
-  __TEXT.__text: 0x169b0
-  __TEXT.__auth_stubs: 0x9e0
-  __TEXT.__objc_methlist: 0xe9c
+927.60.5.0.0
+  __TEXT.__text: 0x17270
+  __TEXT.__auth_stubs: 0x9b0
+  __TEXT.__objc_methlist: 0xeb4
   __TEXT.__const: 0x110
-  __TEXT.__gcc_except_tab: 0xd4
-  __TEXT.__cstring: 0x1452
-  __TEXT.__oslogstring: 0x222e
+  __TEXT.__gcc_except_tab: 0xbc
+  __TEXT.__cstring: 0x1451
+  __TEXT.__oslogstring: 0x2381
   __TEXT.__unwind_info: 0x360
   __TEXT.__objc_classname: 0x1ec
-  __TEXT.__objc_methname: 0x2d97
-  __TEXT.__objc_methtype: 0x14bb
-  __TEXT.__objc_stubs: 0x2540
-  __DATA_CONST.__got: 0x258
+  __TEXT.__objc_methname: 0x2f1f
+  __TEXT.__objc_methtype: 0x14da
+  __TEXT.__objc_stubs: 0x2720
+  __DATA_CONST.__got: 0x268
   __DATA_CONST.__const: 0x3c8
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc88
+  __DATA_CONST.__objc_selrefs: 0xd00
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0xf8
-  __AUTH_CONST.__auth_got: 0x500
+  __AUTH_CONST.__auth_got: 0x4e8
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x2380
   __AUTH_CONST.__objc_const: 0x26a0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 21C566E6-9599-3BE0-9649-D5410C0E4E6B
-  Functions: 301
-  Symbols:   1459
-  CStrings:  1516
+  UUID: F26C1BB7-610B-3FB1-B30C-C0F580FA40EA
+  Functions: 308
+  Symbols:   1489
+  CStrings:  1540
 
Symbols:
+ -[PCCProxiedDevice acceptTaskingFile:forRouting:withId:]
+ -[PCCProxiedDevice acceptTaskingFile:forRouting:withId:].cold.1
+ -[PCCProxiedDevice acceptTaskingFile:forRouting:withId:].cold.2
+ -[PCCProxiedDevice validateFirstLineAsJSON:]
+ -[PCCProxyingDevice deliver:taskingFile:routing:taskId:asMessage:overRSD:]
+ -[PCCProxyingDevice deliver:taskingFile:routing:taskId:asMessage:overRSD:].cold.1
+ -[PCCProxyingDevice deliver:taskingFile:routing:taskId:asMessage:overRSD:].cold.2
+ _NSURLFileSizeKey
+ _OBJC_CLASS_$_FileUtils
+ ___42-[PCCProxyingDevice finishRequest:result:]_block_invoke.428
+ ___47-[PCCBridgeEndpoint setupIncomingEventListener]_block_invoke.13.cold.3
+ ___47-[PCCBridgeEndpoint setupIncomingEventListener]_block_invoke.30
+ ___47-[PCCBridgeEndpoint setupIncomingEventListener]_block_invoke.30.cold.1
+ ___47-[PCCBridgeEndpoint setupIncomingEventListener]_block_invoke.30.cold.2
+ ___block_descriptor_72_e8_32s40s48s56s64r_e8_v12?0i8ls32l8s40l8s48l8r64l8s56l8
+ _objc_msgSend$JSONObjectWithData:options:error:
+ _objc_msgSend$URLByAppendingPathExtension:
+ _objc_msgSend$acceptTaskingFile:forRouting:withId:
+ _objc_msgSend$closeFile
+ _objc_msgSend$data
+ _objc_msgSend$dataWithContentsOfURL:options:error:
+ _objc_msgSend$deliver:taskingFile:routing:taskId:asMessage:overRSD:
+ _objc_msgSend$dictionaryWithContentsOfURL:error:
+ _objc_msgSend$fileHandleForReadingFromURL:error:
+ _objc_msgSend$fileURLWithPathComponents:
+ _objc_msgSend$getResourceValue:forKey:error:
+ _objc_msgSend$getXattrBoolValWithName:at:
+ _objc_msgSend$getXattrWithName:at:
+ _objc_msgSend$installCATasking:withId:untasked:
+ _objc_msgSend$readDataOfLength:
+ _objc_msgSend$temporaryFileWithPrefix:fd:
+ _objc_msgSend$validateFirstLineAsJSON:
- -[PCCProxyingDevice deliver:tasking:taskId:fromBlob:]
- _NSTemporaryDirectory
- ___42-[PCCProxyingDevice finishRequest:result:]_block_invoke.422
- ___47-[PCCBridgeEndpoint setupIncomingEventListener]_block_invoke.29
- ___47-[PCCBridgeEndpoint setupIncomingEventListener]_block_invoke.29.cold.1
- ___47-[PCCBridgeEndpoint setupIncomingEventListener]_block_invoke.29.cold.2
- ___block_descriptor_72_e8_32s40s48s56r_e8_v12?0i8ls32l8s40l8r56l8s48l8
- _mkstemp
- _objc_msgSend$deliver:tasking:taskId:fromBlob:
- _objc_msgSend$fileURLWithFileSystemRepresentation:isDirectory:relativeToURL:
- _strcpy
CStrings:
+ "CA tasking results: %@"
+ "Failed to read tasking payload at %@: %@"
+ "Failed to read tasking update content: %@"
+ "Failed to send tasking payload to target '%@': %@"
+ "Failed to validate CA tasking file: first line was not valid JSON"
+ "JSONObjectWithData:options:error:"
+ "PCCProxiedDevice asked to handle an unexpected file"
+ "URLByAppendingPathExtension:"
+ "acceptTaskingFile:forRouting:withId:"
+ "bridge-xfer"
+ "closeFile"
+ "da3 tasking results: %@"
+ "data"
+ "dataWithContentsOfURL:options:error:"
+ "deliver:taskingFile:routing:taskId:asMessage:overRSD:"
+ "dictionaryWithContentsOfURL:error:"
+ "failed to transfer file to remote device: failed to create temporary file"
+ "failed to write tmp remote file: [%d] %s"
+ "fileHandleForReadingFromURL:error:"
+ "fileURLWithPathComponents:"
+ "getResourceValue:forKey:error:"
+ "getXattrBoolValWithName:at:"
+ "getXattrWithName:at:"
+ "installCATasking:withId:untasked:"
+ "readDataOfLength:"
+ "received request %@-%@ '%@'"
+ "sendAsMessage"
+ "temporaryFileWithPrefix:fd:"
+ "v56@0:8@\"NSString\"16@\"NSURL\"24@\"NSString\"32@\"NSString\"40B48B52"
+ "v56@0:8@16@24@32@40B48B52"
+ "validateFirstLineAsJSON:"
- "PCCProxiedDevice unexpectedly asked to handle a file. This is a no-op"
- "bridge-xfer.XXXXXX"
- "deliver:tasking:taskId:fromBlob:"
- "failed to write tmp remote file"
- "fileURLWithFileSystemRepresentation:isDirectory:relativeToURL:"
- "payload"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSData\"40"

```
