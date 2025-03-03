## FrontBoard

> `/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`

```diff

-943.3.9.0.0
-  __TEXT.__text: 0x83150
-  __TEXT.__auth_stubs: 0xff0
-  __TEXT.__objc_methlist: 0x4c24
-  __TEXT.__const: 0x360
-  __TEXT.__cstring: 0xa9c7
-  __TEXT.__oslogstring: 0x56f3
-  __TEXT.__gcc_except_tab: 0x14dc
+943.5.16.0.0
+  __TEXT.__text: 0x83978
+  __TEXT.__auth_stubs: 0x1010
+  __TEXT.__objc_methlist: 0x5c38
+  __TEXT.__const: 0x378
+  __TEXT.__cstring: 0xab15
+  __TEXT.__oslogstring: 0x589c
+  __TEXT.__gcc_except_tab: 0x14b0
   __TEXT.__dlopen_cstrs: 0x1b2
-  __TEXT.__unwind_info: 0x1f10
+  __TEXT.__unwind_info: 0x2030
   __TEXT.__objc_classname: 0x10ed
-  __TEXT.__objc_methname: 0xf6c5
+  __TEXT.__objc_methname: 0xf74c
   __TEXT.__objc_methtype: 0x38a7
-  __TEXT.__objc_stubs: 0xb2c0
-  __DATA_CONST.__got: 0x8e8
-  __DATA_CONST.__const: 0x2688
+  __TEXT.__objc_stubs: 0xb340
+  __DATA_CONST.__got: 0x8f0
+  __DATA_CONST.__const: 0x26b8
   __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x240
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3610
+  __DATA_CONST.__objc_selrefs: 0x3778
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x220
-  __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x808
+  __DATA_CONST.__objc_arraydata: 0x20
+  __AUTH_CONST.__auth_got: 0x818
   __AUTH_CONST.__const: 0x8a0
-  __AUTH_CONST.__cfstring: 0x8500
-  __AUTH_CONST.__objc_const: 0xd1e0
+  __AUTH_CONST.__cfstring: 0x8660
+  __AUTH_CONST.__objc_const: 0xb590
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0xf50
-  __DATA.__objc_ivar: 0x910
+  __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH.__objc_data: 0xe60
+  __DATA.__objc_ivar: 0x918
   __DATA.__data: 0x1b00
-  __DATA.__bss: 0x270
-  __DATA_DIRTY.__objc_data: 0xc30
-  __DATA_DIRTY.__bss: 0x198
+  __DATA.__bss: 0x238
+  __DATA_DIRTY.__objc_data: 0xd20
+  __DATA_DIRTY.__bss: 0x1d0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2814
-  Symbols:   3764
-  CStrings:  4789
+  Functions: 2957
+  Symbols:   3805
+  CStrings:  4814
 
Symbols:
+ _BSLogAddStateCaptureBlockForUserRequestsOnlyWithTitle
+ _SANDBOX_CHECK_NO_REPORT
+ _objc_retain_x10
+ _sandbox_check
- _BSLogAddStateCaptureBlockWithTitle
CStrings:
+ "%{public}@ Workspace assertion invalidated: %{public}@"
+ "%{public}@ Workspace assertion will expire."
+ "/\v"
+ "/System/AppleInternal/Library/Frameworks/ManagedConfiguration.framework/ManagedConfiguration"
+ "/System/AppleInternal/Library/Frameworks/UIKit.framework/UIKit"
+ "FBWorkspaceConnectionsStateStore: %@ denied for %@"
+ "FBWorkspaceConnectionsStateStore: error in sandbox_check %@ for %@ : errno=%i (%s)"
+ "FBWorkspaceDomain:%p no access to defaultShmemIdentifier \"%@\" - disabling reconnection support"
+ "FBWorkspaceDomain:%p unrecognized ReconnectShmemIdentifier \"%@\" - disabling reconnection support"
+ "ReconnectShmemIdentifier"
+ "Thermal State:   %@"
+ "Unable to establish XPC connection."
+ "Value for '%@' was unexpectedly nil. Expected %@."
+ "_reconnectShmemIdentifier"
+ "_reconnectableWorkspaces"
+ "arrayByAddingObject:"
+ "critical"
+ "fair"
+ "hasSandboxAccessForIdentifier:"
+ "identifierForName:"
+ "improper length identifier : \"%@\""
+ "ipc-posix-shm-read-data"
+ "ipc-posix-shm-write-create"
+ "ipc-posix-shm-write-unlink"
+ "nominal"
+ "reconnectShmem"
+ "serious"
+ "shmPath"
+ "thermalState"
- "/\t"
- "[_bs_assert_object isKindOfClass:FBWorkspaceConnectionsStateClass]"
- "identifier is too long"

```
