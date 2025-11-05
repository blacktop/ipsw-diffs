## SystemExtensions

> `/System/Library/Frameworks/SystemExtensions.framework/Versions/A/SystemExtensions`

```diff

-187.80.3.0.0
-  __TEXT.__text: 0xaa1c
+214.0.0.0.0
+  __TEXT.__text: 0xab18
   __TEXT.__auth_stubs: 0x540
-  __TEXT.__objc_methlist: 0xbb0
-  __TEXT.__const: 0x90
+  __TEXT.__objc_methlist: 0xf74
+  __TEXT.__const: 0x88
   __TEXT.__gcc_except_tab: 0x1f0
-  __TEXT.__cstring: 0x910
+  __TEXT.__cstring: 0x92d
   __TEXT.__oslogstring: 0x402
-  __TEXT.__unwind_info: 0x328
-  __TEXT.__objc_classname: 0x333
-  __TEXT.__objc_methname: 0x228f
-  __TEXT.__objc_methtype: 0x81c
-  __TEXT.__objc_stubs: 0x19e0
+  __TEXT.__unwind_info: 0x338
+  __TEXT.__objc_classname: 0x335
+  __TEXT.__objc_methname: 0x233b
+  __TEXT.__objc_methtype: 0x822
+  __TEXT.__objc_stubs: 0x1a40
   __DATA_CONST.__got: 0x118
   __DATA_CONST.__const: 0xc0
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x858
+  __DATA_CONST.__objc_selrefs: 0x8f8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x38
   __AUTH_CONST.__auth_got: 0x2b0
   __AUTH_CONST.__const: 0x590
-  __AUTH_CONST.__cfstring: 0x660
-  __AUTH_CONST.__objc_const: 0x1f40
+  __AUTH_CONST.__cfstring: 0x6a0
+  __AUTH_CONST.__objc_const: 0x1910
   __AUTH.__objc_data: 0x410
-  __DATA.__objc_ivar: 0xdc
+  __DATA.__objc_ivar: 0xe4
   __DATA.__data: 0x440
   __DATA.__common: 0x10
   __DATA.__bss: 0x40

   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 27496DE7-9804-3285-8DF4-C1566F8863AD
-  Functions: 317
-  Symbols:   932
-  CStrings:  660
+  UUID: 1060D938-C58B-3FC8-9493-81133F6602C3
+  Functions: 325
+  Symbols:   945
+  CStrings:  671
 
Symbols:
+ +[OSSystemExtensionManager sharedManager].cold.1
+ +[OSSystemExtensionsWorkspace sharedWorkspace].cold.1
+ -[OSSystemExtensionDeactivationRequest didConnectToDaemon].cold.1
+ -[OSSystemExtensionProperties displayName]
+ -[OSSystemExtensionProperties initWithURL:bundleIdentifier:version:shortVersion:isEnabled:isAwaitingUserApproval:isUninstalling:displayName:usageDescription:]
+ -[OSSystemExtensionProperties setDisplayName:]
+ -[OSSystemExtensionProperties setUsageDescription:]
+ -[OSSystemExtensionProperties usageDescription]
+ AppMoveHandle.cold.1
+ OBJC_IVAR_$_OSSystemExtensionProperties._displayName
+ OBJC_IVAR_$_OSSystemExtensionProperties._usageDescription
+ __43-[OSSystemExtensionRequest connectToDaemon]_block_invoke.178
+ __block_literal_global.238
+ __block_literal_global.265
+ _objc_msgSend$displayName
+ _objc_msgSend$setDisplayName:
+ _objc_msgSend$setUsageDescription:
- -[OSSystemExtensionProperties initWithURL:bundleIdentifier:version:shortVersion:isEnabled:isAwaitingUserApproval:isUninstalling:]
- __43-[OSSystemExtensionRequest connectToDaemon]_block_invoke.162
- __block_literal_global.222
- __block_literal_global.249
CStrings:
+ "@76@0:8@16@24@32@40B48B52B56@60@68"
+ "T@\"NSString\",&,V_displayName"
+ "T@\"NSString\",&,V_usageDescription"
+ "_displayName"
+ "_usageDescription"
+ "displayName"
+ "initWithURL:bundleIdentifier:version:shortVersion:isEnabled:isAwaitingUserApproval:isUninstalling:displayName:usageDescription:"
+ "setDisplayName:"
+ "setUsageDescription:"
- "@60@0:8@16@24@32@40B48B52B56"
- "initWithURL:bundleIdentifier:version:shortVersion:isEnabled:isAwaitingUserApproval:isUninstalling:"

```
