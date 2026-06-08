## SidebarFileDispatcher

> `/System/Library/PrivateFrameworks/SidebarFileDispatcher.framework/SidebarFileDispatcher`

```diff

-659.122.1.0.0
-  __TEXT.__text: 0x14fc
-  __TEXT.__auth_stubs: 0x210
-  __TEXT.__objc_methlist: 0xd4
-  __TEXT.__const: 0x78
+835.0.0.0.0
+  __TEXT.__text: 0xbf0
+  __TEXT.__objc_methlist: 0xa4
+  __TEXT.__const: 0x70
   __TEXT.__gcc_except_tab: 0x3c
-  __TEXT.__cstring: 0x108
-  __TEXT.__oslogstring: 0x221
-  __TEXT.__unwind_info: 0xd8
-  __TEXT.__objc_classname: 0x40
-  __TEXT.__objc_methname: 0x2cd
-  __TEXT.__objc_methtype: 0x117
-  __TEXT.__objc_stubs: 0x280
-  __DATA_CONST.__got: 0x60
-  __DATA_CONST.__const: 0x110
+  __TEXT.__cstring: 0xd2
+  __TEXT.__oslogstring: 0x1bc
+  __TEXT.__unwind_info: 0xb0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xc8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc0
+  __DATA_CONST.__objc_selrefs: 0xb0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x118
+  __DATA_CONST.__got: 0x60
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x60
-  __AUTH_CONST.__objc_const: 0x118
+  __AUTH_CONST.__objc_const: 0x108
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x8
   __DATA.__data: 0x60
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/AppleNVMe.framework/AppleNVMe
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7B39753F-4468-3890-8CF1-C6F53ABC1526
-  Functions: 37
-  Symbols:   178
-  CStrings:  63
+  UUID: B1485D58-30BE-3697-A1D1-C16A90371EBD
+  Functions: 26
+  Symbols:   152
+  CStrings:  18
 
Symbols:
+ -[SideBarFileDispatcherAPI processSidebarBuffer:bufferSizeBytes:NVMeDeviceID:sbarLba:reply:]
+ _SidebarFileDispatcherServiceErrorDomain
+ ___38-[SideBarFileDispatcherAPI connection]_block_invoke.13
+ ___38-[SideBarFileDispatcherAPI connection]_block_invoke.13.cold.1
+ ___92-[SideBarFileDispatcherAPI processSidebarBuffer:bufferSizeBytes:NVMeDeviceID:sbarLba:reply:]_block_invoke
+ ___92-[SideBarFileDispatcherAPI processSidebarBuffer:bufferSizeBytes:NVMeDeviceID:sbarLba:reply:]_block_invoke.20
+ ___92-[SideBarFileDispatcherAPI processSidebarBuffer:bufferSizeBytes:NVMeDeviceID:sbarLba:reply:]_block_invoke.20.cold.1
+ ___92-[SideBarFileDispatcherAPI processSidebarBuffer:bufferSizeBytes:NVMeDeviceID:sbarLba:reply:]_block_invoke.cold.1
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$processSidebarBuffer:bufferSizeBytes:NVMeDeviceID:sbarLba:reply:
+ _objc_release_x24
+ _objc_release_x25
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x24
+ _objc_retain_x8
- -[SideBarFileDispatcherAPI matchPurgeablePositionsToday:yesterdayF:reply:]
- -[SideBarFileDispatcherAPI printPurgeableFileEntries:reply:]
- -[SideBarFileDispatcherAPI sortAndDeduplicatePurgeableFile:reply:]
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- ___38-[SideBarFileDispatcherAPI connection]_block_invoke.20
- ___38-[SideBarFileDispatcherAPI connection]_block_invoke.20.cold.1
- ___60-[SideBarFileDispatcherAPI printPurgeableFileEntries:reply:]_block_invoke
- ___60-[SideBarFileDispatcherAPI printPurgeableFileEntries:reply:]_block_invoke.29
- ___60-[SideBarFileDispatcherAPI printPurgeableFileEntries:reply:]_block_invoke.29.cold.1
- ___60-[SideBarFileDispatcherAPI printPurgeableFileEntries:reply:]_block_invoke.cold.1
- ___66-[SideBarFileDispatcherAPI sortAndDeduplicatePurgeableFile:reply:]_block_invoke
- ___66-[SideBarFileDispatcherAPI sortAndDeduplicatePurgeableFile:reply:]_block_invoke.27
- ___66-[SideBarFileDispatcherAPI sortAndDeduplicatePurgeableFile:reply:]_block_invoke.27.cold.1
- ___66-[SideBarFileDispatcherAPI sortAndDeduplicatePurgeableFile:reply:]_block_invoke.cold.1
- ___74-[SideBarFileDispatcherAPI matchPurgeablePositionsToday:yesterdayF:reply:]_block_invoke
- ___74-[SideBarFileDispatcherAPI matchPurgeablePositionsToday:yesterdayF:reply:]_block_invoke.30
- ___74-[SideBarFileDispatcherAPI matchPurgeablePositionsToday:yesterdayF:reply:]_block_invoke.30.cold.1
- ___74-[SideBarFileDispatcherAPI matchPurgeablePositionsToday:yesterdayF:reply:]_block_invoke.cold.1
- ___block_descriptor_40_e8_32bs_e28_v24?0"NSData"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32bs_e34_v36?0I8Q12"NSData"20"NSError"28ls32l8
- _objc_msgSend$matchPurgeablePositionsToday:yesterdayF:reply:
- _objc_msgSend$printPurgeableFileEntries:reply:
- _objc_msgSend$sortAndDeduplicatePurgeableFile:reply:
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x20
- _objc_retain_x21
- _objc_retain_x22
CStrings:
+ "Processing sidebar buffer: handle=%@, size=%llu, deviceID=%llu, lba=%llu"
+ "SideBar buffer processing completed successfully"
+ "SideBar buffer processing failed: %{public}@"
+ "SidebarFileDispatcherServiceErrorDomain"
- ".cxx_destruct"
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSXPCConnection\""
- "@16@0:8"
- "Match purgeable positions completed successfully"
- "Match purgeable positions failed: %{public}@"
- "Print entries completed successfully"
- "Print entries failed: %{public}@"
- "Purgable processing completed successfully, status %d"
- "Purgable processing failed: %{public}@, status %d"
- "SideBarFileDispatcherAPI"
- "SidebarFileDispatcherServiceProtocol"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_connectionQueue"
- "T@\"NSXPCConnection\",&,N,V_connectionToService"
- "_connectionQueue"
- "_connectionToService"
- "com.sidebar.filedispatchererror"
- "connection"
- "connectionQueue"
- "connectionToService"
- "dictionaryWithObjects:forKeys:count:"
- "errorWithDomain:code:userInfo:"
- "init"
- "initWithServiceName:"
- "interfaceWithProtocol:"
- "invalidate"
- "matchPurgeablePositionsToday:yesterdayF:reply:"
- "printPurgeableFileEntries:reply:"
- "remoteObjectInterface"
- "resume"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setConnectionQueue:"
- "setConnectionToService:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setRemoteObjectInterface:"
- "setWithObject:"
- "sharedDispatcher"
- "sortAndDeduplicatePurgeableFile:reply:"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "v16@0:8"
- "v24@0:8@16"
- "v24@?0@\"NSData\"8@\"NSError\"16"
- "v32@0:8@\"NSFileHandle\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSFileHandle\"16@?<v@?IQ@\"NSData\"@\"NSError\">24"
- "v32@0:8@16@?24"
- "v36@?0I8Q12@\"NSData\"20@\"NSError\"28"
- "v40@0:8@\"NSFileHandle\"16@\"NSFileHandle\"24@?<v@?@\"NSData\"@\"NSError\">32"
- "v40@0:8@16@24@?32"

```
