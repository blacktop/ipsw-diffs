## uarppersonalizationd

> `/usr/libexec/uarppersonalizationd`

```diff

-1207.120.19.0.0
-  __TEXT.__text: 0x2164
-  __TEXT.__auth_stubs: 0x3b0
-  __TEXT.__objc_stubs: 0x3a0
-  __TEXT.__objc_methlist: 0x88
-  __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x20b
-  __TEXT.__oslogstring: 0x50a
-  __TEXT.__gcc_except_tab: 0x1c
-  __TEXT.__objc_methname: 0x368
-  __TEXT.__objc_classname: 0x38
-  __TEXT.__objc_methtype: 0xf9
-  __TEXT.__unwind_info: 0xe0
-  __DATA_CONST.__auth_got: 0x1e8
-  __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0x108
-  __DATA_CONST.__cfstring: 0xa0
-  __DATA_CONST.__objc_classlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x8
+1338.0.21.0.2
+  __TEXT.__text: 0x43b8
+  __TEXT.__auth_stubs: 0x480
+  __TEXT.__objc_stubs: 0x800
+  __TEXT.__objc_methlist: 0x180
+  __TEXT.__const: 0x68
+  __TEXT.__gcc_except_tab: 0xcc
+  __TEXT.__objc_methname: 0x824
+  __TEXT.__cstring: 0xb23
+  __TEXT.__oslogstring: 0x8df
+  __TEXT.__objc_classname: 0x9b
+  __TEXT.__objc_methtype: 0x1bd
+  __TEXT.__unwind_info: 0x188
+  __DATA_CONST.__auth_got: 0x250
+  __DATA_CONST.__got: 0x100
+  __DATA_CONST.__const: 0x450
+  __DATA_CONST.__cfstring: 0xbc0
+  __DATA_CONST.__objc_classlist: 0x18
+  __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x1d0
-  __DATA.__objc_selrefs: 0x108
-  __DATA.__objc_ivar: 0x20
-  __DATA.__objc_data: 0x50
-  __DATA.__data: 0x60
-  __DATA.__bss: 0x10
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA.__objc_const: 0x4c0
+  __DATA.__objc_selrefs: 0x238
+  __DATA.__objc_ivar: 0x50
+  __DATA.__objc_data: 0xf0
+  __DATA.__data: 0xc0
+  __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreUARP.framework/CoreUARP
+  - /System/Library/PrivateFrameworks/UARPKit.framework/UARPKit
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CBC6CF5B-8C38-370B-9CF3-1439F379D0DF
-  Functions: 53
-  Symbols:   88
-  CStrings:  122
+  UUID: 75AD841F-541B-379D-9C6A-2623D99C081C
+  Functions: 102
+  Symbols:   113
+  CStrings:  392
 
Symbols:
+ _OBJC_CLASS_$_NSFileHandle
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSKeyedUnarchiver
+ _OBJC_CLASS_$_NSUUID
+ _UARPAssetPersonalizationCompleteProtocolSetupInterface
+ _dispatch_async
+ _kUARPDaemonNotificationMatching
+ _kUARPDaemonPersonalization
+ _kUARPServiceBTLEPersonalizationNeededEventName
+ _kUARPServiceHIDPersonalizationNeededEventName
+ _kUARPServicePersonalization
+ _kUARPServicePersonalizationBTLEServer
+ _kUARPServicePersonalizationNeededQueue
+ _kUarpAssetPersonalizationCompleteXpcServiceName
+ _objc_alloc_init
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_opt_isKindOfClass
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_retain_x24
+ _objc_retain_x26
+ _objc_retain_x27
+ _xpc_dictionary_get_data
- _dispatch_sync
- _objc_retain_x25
CStrings:
+ ""
+ "%s: Failed to personalization; Asset UUID is %@, Endpoint UUID is %@, server URL is %@, tss options are %@"
+ "%s: Failed to prepare for personalization; Asset UUID is %@, Endpoint UUID is %@, server URL is %@tss options are %@"
+ "%s: Personalization succeeded; Asset UUID is %@, Endpoint UUID is %@, server URL is %@"
+ "%s: TSS Event"
+ "%s: TSS Request destined for %s"
+ "%s: TSS Request for asset UUID %s"
+ "%s: TSS Request for endpoint UUID %s"
+ "%s: TSS Request is %@"
+ "%s: TSS Request is NULL"
+ "%s: createDirectoryAtPath %@ failed %@ "
+ "%s: createFileAtPath failed %@ "
+ "%s: fileHandleForWritingToURL %@ failed %@ "
+ "%s: removeItemAtPath %@ failed %@ "
+ "%s: ticket is %@"
+ "%s: tss options are %@"
+ "-[UARPHostPersonalizationManager personalizeAssetWithSSO:endpointUUID:tssOptions:tssServerURL:]"
+ "-[UARPHostPersonalizationManager personalizeAssetWithXPCEvent:]_block_invoke"
+ "@\"NSDictionary\""
+ "@\"NSObject<OS_dispatch_queue>\""
+ "@\"NSXPCListener\""
+ "@24@0:8@16"
+ "Asset Corrupt"
+ "Asset Not Found"
+ "Asset Staging Still In Progress"
+ "Attempt AppleConnect"
+ "Attempt Auth Listed"
+ "B"
+ "B32@0:8@16^@24"
+ "Connecting to anonymous listener"
+ "Connection Interrupted"
+ "Connection Invalidated"
+ "Dynamic Asset (RX)"
+ "Dynamic Asset (TX)"
+ "Failed to connect to XPC"
+ "Failure"
+ "Firmware (RX)"
+ "Firmware (TX)"
+ "Idle"
+ "In Flight"
+ "In Use"
+ "Invalid"
+ "Needs Restart"
+ "None"
+ "Not Auth Listed"
+ "Not Needed"
+ "Nothing Staged"
+ "Payload 4CC"
+ "Payload Filepath"
+ "Payload Long Name"
+ "Payload MetaData"
+ "Payload Version"
+ "Personalization Tickets"
+ "Property List Digest Path"
+ "Property List Path"
+ "Property List Version Path"
+ "Request Failure"
+ "SHA-256"
+ "SHA-384"
+ "SHA-512"
+ "Server Unreachable"
+ "Starting XPC connection to %@"
+ "Success"
+ "SuperBinary Firmware Version"
+ "SuperBinary Format Version"
+ "SuperBinary MetaData"
+ "SuperBinary Payloads"
+ "T@\"NSDictionary\",R,V_personalizationOptions"
+ "T@\"NSDictionary\",R,V_personalizationTicket"
+ "T@\"NSURL\",R,V_signingServer"
+ "Ticket"
+ "Ticket Construction Failure"
+ "UARP: TSS Request to %{public}@%{public}@ is %{public}@"
+ "UARP: TSS Request to default server"
+ "UARP: TSS Response from %{public}@%{public}@ is %{public}@"
+ "UARPAssetPersonalizationCompleteProtocol"
+ "UARPAssetPersonalizer"
+ "UARPHostPersonalizationManager"
+ "UARPLayer3UtilsCleanFileHandleForWriting"
+ "UTF8String"
+ "UUIDString"
+ "Unknown"
+ "Upload Abandoned"
+ "Upload Abandoned  - Better Transport"
+ "Upload Abandoned  - Cancelled Asset Tag"
+ "Upload Abandoned  - Device Error"
+ "Upload Abandoned  - Higher Version"
+ "Upload Abandoned  - Higher Version Active"
+ "Upload Abandoned  - Higher Version Staged"
+ "Upload Abandoned  - Low Battery"
+ "Upload Abandoned  - MetaData Overflow"
+ "Upload Abandoned  - Personalization Failure"
+ "Upload Abandoned  - Priority Activity"
+ "Upload Abandoned  - Processing Error"
+ "Upload Abandoned  - Same Asset Tag In Progress"
+ "Upload Abandoned  - Same Version Active"
+ "Upload Abandoned  - Same Version Staged"
+ "Upload Abandoned  - Unsupported Asset Tag"
+ "Upload Abandoned  - Update In Progress"
+ "Upload Complete"
+ "Upload Denied"
+ "Upload Denied  - Better Transport"
+ "Upload Denied  - Cancelled Asset Tag"
+ "Upload Denied  - Device Error"
+ "Upload Denied  - Higher Version"
+ "Upload Denied  - Higher Version Active"
+ "Upload Denied  - Higher Version Staged"
+ "Upload Denied  - Low Battery"
+ "Upload Denied  - MetaData Overflow"
+ "Upload Denied  - Personalization Failure"
+ "Upload Denied  - Priority Activity"
+ "Upload Denied  - Processing Error"
+ "Upload Denied  - Same Asset Tag In Progress"
+ "Upload Denied  - Same Version Active"
+ "Upload Denied  - Same Version Staged"
+ "Upload Denied  - Unsupported Asset Tag"
+ "Upload Denied  - Update In Progress"
+ "XPC connection already started"
+ "^{__AMAuthInstall=}"
+ "_amai"
+ "_mustSuspend"
+ "_personalizationOptions"
+ "_personalizationTicket"
+ "_queue"
+ "_setQueue:"
+ "_signingServer"
+ "_useSSO"
+ "_xpcListener"
+ "_xpcQueue"
+ "activate"
+ "assetPersonalizationComplete:endpointUUID:personalizationTicket:"
+ "assetUUID"
+ "assets"
+ "com.apple.uarp"
+ "com.apple.uarp.layer3"
+ "com.apple.uarp.personalization"
+ "com.apple.uarp.personalization.manager"
+ "com.apple.uarp.personalization.manager.xpc"
+ "compare:"
+ "containsString:"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "createFileAtPath:contents:attributes:"
+ "dataWithBytes:length:"
+ "defaultManager"
+ "device/assets/analytics"
+ "device/assets/crash"
+ "device/assets/logs"
+ "endpoint"
+ "endpointUUID"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "fileExistsAtPath:"
+ "fileHandleForWritingToURL:error:"
+ "handleAppleConnect"
+ "handleAuthListed"
+ "hostpersonalizationmanager"
+ "https://gs.apple.com:443"
+ "initWithListener:"
+ "initWithListenerEndpoint:"
+ "initWithUUIDString:"
+ "main_block_invoke_2"
+ "path"
+ "pcapfiles"
+ "personalizationOptions"
+ "personalizationTicket"
+ "personalizeAssetWithSSO:endpointUUID:tssOptions:tssServerURL:"
+ "personalizeAssetWithXPCEvent:"
+ "personalizeWithOptions:error:"
+ "personalizer"
+ "prepareAsAppleConnectSSO:error:"
+ "prepareAsAuthList:error:"
+ "prepareCommon:error:"
+ "remoteObjectInterface"
+ "remoteObjectProxy"
+ "removeItemAtPath:error:"
+ "reportPersonalizationTicket:endpointUUID:personalizationTicket:"
+ "setExportedInterface:"
+ "setExportedObject:"
+ "setWithObjects:"
+ "setupXpcConnection"
+ "signingServer"
+ "stringByDeletingLastPathComponent"
+ "tatsuRequest"
+ "tatsuResponse"
+ "tatsuServerURL"
+ "unarchivedObjectOfClasses:fromData:error:"
+ "v32@?0@\"NSString\"8@16^B24"
+ "v40@0:8@\"NSUUID\"16@\"NSUUID\"24@\"NSDictionary\"32"
+ "v40@0:8@16@24@32"
+ "v48@0:8@16@24@32@40"
- "btlePersonalizationNeeded"
- "com.apple.notifyd.matching"
- "com.apple.uarp.personalization-needed.dispatchqueue"
- "com.apple.uarppersonalization"
- "com.apple.uarppersonalization.btleserver"
- "com.apple.uarppersonalizationd"
- "hidPersonalizationNeeded"

```
