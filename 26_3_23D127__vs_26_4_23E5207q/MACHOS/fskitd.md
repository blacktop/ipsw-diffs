## fskitd

> `/usr/libexec/fskitd`

```diff

-737.80.2.0.0
-  __TEXT.__text: 0x44a58
-  __TEXT.__auth_stubs: 0xb10
-  __TEXT.__objc_stubs: 0x4a00
-  __TEXT.__objc_methlist: 0x1f1c
+737.100.107.0.0
+  __TEXT.__text: 0x43d64
+  __TEXT.__auth_stubs: 0xaa0
+  __TEXT.__objc_stubs: 0x4a20
+  __TEXT.__objc_methlist: 0x1ee4
   __TEXT.__const: 0x130
-  __TEXT.__gcc_except_tab: 0x2384
-  __TEXT.__oslogstring: 0x3b1f
-  __TEXT.__cstring: 0x2d4f
-  __TEXT.__objc_classname: 0x223
-  __TEXT.__objc_methname: 0x58a0
-  __TEXT.__objc_methtype: 0x1e8b
-  __TEXT.__unwind_info: 0xf90
-  __DATA_CONST.__auth_got: 0x598
-  __DATA_CONST.__got: 0x338
-  __DATA_CONST.__const: 0x20f8
-  __DATA_CONST.__cfstring: 0x840
+  __TEXT.__gcc_except_tab: 0x23f0
+  __TEXT.__oslogstring: 0x3bd0
+  __TEXT.__cstring: 0x2dce
+  __TEXT.__objc_classname: 0x22d
+  __TEXT.__objc_methname: 0x5824
+  __TEXT.__objc_methtype: 0x1e1d
+  __TEXT.__unwind_info: 0xfa0
+  __DATA_CONST.__auth_got: 0x560
+  __DATA_CONST.__got: 0x340
+  __DATA_CONST.__const: 0x2080
+  __DATA_CONST.__cfstring: 0x7a0
   __DATA_CONST.__objc_classlist: 0x90
-  __DATA_CONST.__objc_protolist: 0x48
+  __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x68

   __DATA.__objc_selrefs: 0x16c8
   __DATA.__objc_ivar: 0x174
   __DATA.__objc_data: 0x5a0
-  __DATA.__data: 0x6b0
+  __DATA.__data: 0x710
   __DATA.__common: 0x88
-  __DATA.__bss: 0x51
+  __DATA.__bss: 0x61
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: 5E3AC0E8-DA62-3BC2-B3C5-ADA14AE30A93
-  Functions: 1290
-  Symbols:   294
-  CStrings:  1959
+  UUID: E9D85916-879B-34B9-9D3B-D21B39E730A3
+  Functions: 1298
+  Symbols:   288
+  CStrings:  1951
 
Symbols:
+ _OBJC_CLASS_$_FSSharedMutableBuffer
+ _OBJC_CLASS_$_NSLock
+ _objc_retainAutoreleasedReturnValue
- _OBJC_CLASS_$_LiveFSSharedMutableBuffer
- _dispatch_time
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x10
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _objc_retain_x9
CStrings:
+ "%s: No extension with fsShortName (%@) found"
+ "-[fskitdXPCServer installedExtensionWithShortName:user:replyHandler:]_block_invoke"
+ "-[fskitdXPCServer installedExtensionWithShortName:user:replyHandler:]_block_invoke_2"
+ "Call fskit_agent to get NSXPCListenerEndpoint for bundleID (%@), instanceUUID (%@)"
+ "Call fskit_agent to startExtension for bundleID (%@), instanceUUID (%@)"
+ "Call fskit_agent to stop extension for bundleID (%@), instanceUUID (%@)"
+ "Could not obtain NSXPCListerner fskitdListener"
+ "FSMounter"
+ "Resuming fskitdListener"
+ "Returning set %@"
+ "audit_token"
+ "fsShortName"
+ "fskitdLiveFSMachServiceName"
+ "fskitdMachServiceName"
+ "initialize"
+ "serviceName"
+ "v20@?0i8@\"FSMachPort\"12"
+ "v24@0:8^{_FSFileAttributes=QQQIIIIIIQQQQ{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}II}16"
+ "v32@0:8@\"FSMachPort\"16@?<v@?@\"NSError\">24"
+ "v40@0:8@\"NSString\"16Q24@?<v@?i@\"FSMachPort\">32"
+ "v56@0:8@\"NSString\"16Q24@\"FSSharedMutableBuffer\"32Q40@?<v@?iQ@\"NSData\">48"
+ "v56@0:8@\"NSString\"16Q24@\"FSSharedMutableBuffer\"32Q40@?<v@?iQ@\"NSData\"@\"NSData\">48"
+ "v64@0:8@\"NSString\"16@\"FSSharedMutableBuffer\"24Q32Q40Q48@?<v@?iqQ>56"
+ "v72@0:8@\"NSString\"16@\"FSSharedMutableBuffer\"24Q32Q40Q48Q56@?<v@?iqQ>64"
- "%s: start"
- "About to call to fskit_agent"
- "About to call to fskit_agent, bundle ID %@, instanceUUID %@"
- "About to filter"
- "Getting extensions"
- "Hello FSClient! entitlement %s"
- "MSDOS"
- "Returniong set %@"
- "_installedExtensionWithBundleID:user:replyHandler:"
- "_installedExtensionWithShortName:user:replyHandler:"
- "com.apple.fskit.msdos"
- "com.apple.fskit.passthroughfs"
- "installedExtensionWithBundleID:replyHandler:"
- "localizedCaseInsensitiveContainsString:"
- "newByCopyingPort:"
- "passthroughfs"
- "switchToFSKit:"
- "v20@?0i8@\"LiveFSMachPort\"12"
- "v20@?0i8Q12"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8^{_LIFileAttributes=QQQIIIIIIQQQQ{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}II}16"
- "v32@0:8@\"LiveFSMachPort\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"FSModuleIdentity\"@\"NSError\">24"
- "v40@0:8@\"NSString\"16Q24@?<v@?i@\"LiveFSMachPort\">32"
- "v56@0:8@\"NSString\"16Q24@\"LiveFSSharedMutableBuffer\"32Q40@?<v@?iQ@\"NSData\">48"
- "v56@0:8@\"NSString\"16Q24@\"LiveFSSharedMutableBuffer\"32Q40@?<v@?iQ@\"NSData\"@\"NSData\">48"
- "v64@0:8@\"NSString\"16@\"LiveFSSharedMutableBuffer\"24Q32Q40Q48@?<v@?iqQ>56"
- "v72@0:8@\"NSString\"16@\"LiveFSSharedMutableBuffer\"24Q32Q40Q48Q56@?<v@?iqQ>64"

```
