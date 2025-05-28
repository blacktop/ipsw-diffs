## gputoolsserviced

> `/usr/libexec/gputoolsserviced`

```diff

-240.9.0.0.0
-  __TEXT.__text: 0x17a00
+270.12.0.0.0
+  __TEXT.__text: 0x1a854
   __TEXT.__auth_stubs: 0xa30
-  __TEXT.__objc_stubs: 0x2440
-  __TEXT.__objc_methlist: 0x20cc
-  __TEXT.__const: 0x174
-  __TEXT.__cstring: 0x157c
-  __TEXT.__objc_methname: 0x45d3
-  __TEXT.__oslogstring: 0x482
-  __TEXT.__objc_classname: 0x620
-  __TEXT.__objc_methtype: 0xf02
-  __TEXT.__unwind_info: 0x618
+  __TEXT.__objc_stubs: 0x2620
+  __TEXT.__objc_methlist: 0x22ec
+  __TEXT.__const: 0x17c
+  __TEXT.__cstring: 0x1a04
+  __TEXT.__objc_methname: 0x494f
+  __TEXT.__oslogstring: 0x53a
+  __TEXT.__objc_classname: 0x67d
+  __TEXT.__objc_methtype: 0xfb0
+  __TEXT.__unwind_info: 0x68c
   __DATA_CONST.__auth_got: 0x520
-  __DATA_CONST.__got: 0xf0
-  __DATA_CONST.__const: 0x758
-  __DATA_CONST.__cfstring: 0x1a40
-  __DATA_CONST.__objc_classlist: 0x1e8
-  __DATA_CONST.__objc_protolist: 0xb8
+  __DATA_CONST.__got: 0x108
+  __DATA_CONST.__const: 0x6e0
+  __DATA_CONST.__cfstring: 0x1e20
+  __DATA_CONST.__objc_classlist: 0x200
+  __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x48
+  __DATA_CONST.__objc_classrefs: 0x208
+  __DATA_CONST.__objc_superrefs: 0x1d0
   __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x6008
-  __DATA.__objc_selrefs: 0xfc8
-  __DATA.__objc_protorefs: 0x38
-  __DATA.__objc_classrefs: 0x1f0
-  __DATA.__objc_superrefs: 0x1b8
-  __DATA.__objc_ivar: 0x364
-  __DATA.__objc_data: 0x1310
-  __DATA.__data: 0x8b0
+  __DATA.__objc_const: 0x64b0
+  __DATA.__objc_selrefs: 0x1080
+  __DATA.__objc_ivar: 0x3a4
+  __DATA.__objc_data: 0x1400
+  __DATA.__data: 0x910
   __DATA.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 720
-  Symbols:   228
-  CStrings:  1367
+  Functions: 760
+  Symbols:   231
+  CStrings:  1453
 
Symbols:
+ _FBSOpenApplicationOptionKeyPromptUnlockDevice
+ _NSLocalizedFailureReasonErrorKey
+ _NSLocalizedRecoverySuggestionErrorKey
+ _fsync
+ _objc_retain_x9
- _objc_retain_x27
- _objc_retain_x28
CStrings:
+ "\x06"
+ "\b"
+ "\n\n%@"
+ " "
+ "%@[%@%@]"
+ "&\x15"
+ "-"
+ "<%@: processName=%@ arguments=%@ environment=%@ bundleIdentifier=%@ processIdentifier=%d ppid=%d>"
+ "<%@: protocolName=%@ protocolMethods=%@ servicePort=%llu platform=%u deviceUDID=%@ version=%llu>"
+ "<%@: serviceProperties=%@ processInfo=%@>"
+ "@\"<GTConnectionProvider>\""
+ "@\"<GTXPCConnection>\"24@0:8Q16"
+ "@\"GTDeviceProperties\"32@0:8@\"NSString\"16^@24"
+ "@\"GTServiceVendor\""
+ "@36@0:8@16Q24i32"
+ "@48@0:8@16@24@32@40"
+ "B24@0:8@\"NSString\"16"
+ "B32@0:8@16@24"
+ "Capturing %@ is not supported."
+ "Capturing disabled. Unsupported API usage."
+ "Failed to close file"
+ "Failed to find URL access provider"
+ "Failed to find remote file writer service for device %@"
+ "Failed to flush file"
+ "Failed to transfer archive, %@"
+ "File should exist locally at %@ but can't be found on disk"
+ "GTConnectionProvider"
+ "GTRelayedXPCConnection"
+ "GTServiceVendor"
+ "GTSimulatorDeviceBrowser"
+ "GTSimulatorDeviceBrowserXPCProxy"
+ "Initiate transfer basePath:%@ device:%@ toURL:%@ chunkSize:%lu compression:%s"
+ "Invalid device UDID passed to beginTransferSessionWithFileEntries"
+ "Invalid device UDID passed to copyIdentifier"
+ "Invalid device UDID passed to initiateTransfer"
+ "Invalid device UDID passed to startTransfer"
+ "Invalid message"
+ "Invalid path passed to beginTransferSessionWithFileEntries"
+ "Invalid path passed to initiateTransfer"
+ "Invalid path passed to startTransfer"
+ "Invalid processInfo argument passed to registerService"
+ "Invalid protocol name"
+ "Invalid sandbox ID"
+ "Invalid serviceProperties argument passed to registerService"
+ "Missing file writer service for device: %@"
+ "Missing remote connection for %@"
+ "Reality"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",C,N,V_Reality"
+ "T@\"NSString\",R,N,V_customRecoverySuggestion"
+ "To enable capturing, disable calls to unsupported APIs and relaunch your application."
+ "Transfer session %llu completed successfully"
+ "Transfer session %llu failed with error \"%@\""
+ "Unsupported method: %@"
+ "_Reality"
+ "_closeCurrentFileDescriptor:"
+ "_connectionForServicePort:"
+ "_connectionProvider"
+ "_currentRemoteRelayPid"
+ "_currentRemoteRelayPort"
+ "_customRecoverySuggestion"
+ "_daemon"
+ "_handleDeviceLocally"
+ "_portToService"
+ "_relayPid"
+ "_relayPort"
+ "_remoteDeviceRelayPid"
+ "_remoteDeviceRelayPort"
+ "_serviceDaemonConnection"
+ "_serviceVendor"
+ "_sharesFileSystemWith:remoteConnection:"
+ "addLocalService:forPort:"
+ "asError"
+ "com.apple.gputools.capture"
+ "com.apple.gputools.serviceprovider"
+ "connectionForServicePort:"
+ "customRecoverySuggestion"
+ "dataWithBytes:length:"
+ "deviceIsHandledLocally:"
+ "deviceProperties:error:"
+ "fileExistsAtPath:"
+ "getSimulatorDeviceBrowserService:"
+ "handleMessageDaemon:fromConnection:"
+ "hasPrefix:"
+ "initWithConnection:"
+ "initWithConnection:relayPort:relayPid:"
+ "initWithConnectionProvider:"
+ "initWithConnectionProvider:deviceUDID:urlAccessProvider:"
+ "initWithFenum:category:customMessage:customRecoverySuggestion:"
+ "initWithServiceProvider:connectionProvider:serviceVendor:"
+ "isSimulatorDevice:"
+ "kDYFE"
+ "objectForKey:"
+ "rangeOfString:"
+ "reality"
+ "setHandleDeviceLocally"
+ "setReality:"
+ "setServiceDaemonConnection:"
+ "stringByReplacingOccurrencesOfString:withString:options:range:"
+ "substringFromIndex:"
+ "updateRelayPort:pid:"
+ "v28@0:8Q16i24"
- "\a"
- "%\x15"
- "%@ API is not yet supported on this platform."
- "@\"<GTRemoteConnectionProvider>\""
- "GTRemoteConnectionProvider"
- "Initiate transfer basePath:%@ device:%@ chunkSize:%lu compression:%s"
- "Message targets remote device but remote device browser isn't registered"
- "No remote connection"
- "Transfer session complete"
- "Unsupported selector: %s"
- "_closeCurrentFileDescriptor"
- "_remoteConnectionProvider"
- "_urlProviderQueue"
- "com.apple.gputools.urlProvider"
- "dispatchMessage:"
- "finishSession %llu"
- "initWithDeviceUDID:remoteConnectionProvider:"
- "initWithFenum:category:customMessage:"
- "initWithRemoteConnectionProvider:deviceUDID:urlAccessProvider:"
- "reason"

```
