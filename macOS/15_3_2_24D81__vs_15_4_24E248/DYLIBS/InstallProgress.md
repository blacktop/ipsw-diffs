## InstallProgress

> `/System/Library/PrivateFrameworks/InstallProgress.framework/Versions/A/InstallProgress`

```diff

 8.1.0.0.0
-  __TEXT.__text: 0xfaa8
+  __TEXT.__text: 0xfa8c
   __TEXT.__auth_stubs: 0x400
-  __TEXT.__objc_methlist: 0xe34
+  __TEXT.__objc_methlist: 0x1254
   __TEXT.__const: 0xd8
-  __TEXT.__gcc_except_tab: 0x360
+  __TEXT.__gcc_except_tab: 0x384
   __TEXT.__cstring: 0x6ac
   __TEXT.__oslogstring: 0xcd2
-  __TEXT.__unwind_info: 0x5a0
+  __TEXT.__unwind_info: 0x5d0
   __TEXT.__objc_classname: 0x4ea
   __TEXT.__objc_methname: 0x221b
   __TEXT.__objc_methtype: 0xd3f

   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7e8
+  __DATA_CONST.__objc_selrefs: 0x878
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xd8
   __AUTH_CONST.__auth_got: 0x210
   __AUTH_CONST.__const: 0x6f0
   __AUTH_CONST.__cfstring: 0x2a0
-  __AUTH_CONST.__objc_const: 0x3178
+  __AUTH_CONST.__objc_const: 0x2a48
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH.__objc_data: 0x910
   __DATA.__objc_ivar: 0x17c

   - /System/Library/PrivateFrameworks/UserManagement.framework/Versions/A/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 43B88B4B-3BE2-32B0-B18A-8AA4287E102D
-  Functions: 448
-  Symbols:   1285
+  UUID: 743387D9-E5B4-3C70-85A0-561A6925FC2C
+  Functions: 462
+  Symbols:   1301
   CStrings:  691
 
Symbols:
+ +[IPGlobalInstallableStateSource sharedAllAppStateSource].cold.1
+ +[IPGlobalInstallableStateSourceDefaultBehavior sharedInstance].cold.1
+ +[IPProgressServer defaultAccessAdjudicator].cold.1
+ +[IPProgressServer defaultBehavior].cold.1
+ +[IPServerXPCTransport defaultXPCTransport].cold.1
+ -[IPInstallableProgressData setInstallPhase:].cold.1
+ -[IPProgressStubBehavior queue].cold.1
+ GCC_except_table3
+ IPClientExportedInterface.cold.1
+ IPServerExportedInterface.cold.1
+ _IPClientLog.cold.1
+ _IPDefaultLog.cold.1
+ _IPServerLog.cold.1
+ __63+[IPGlobalInstallableStateSourceDefaultBehavior sharedInstance]_block_invoke.cold.1
+ defaultBehaviorQueue.cold.1

```
