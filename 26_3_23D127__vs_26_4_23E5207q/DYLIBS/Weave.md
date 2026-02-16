## Weave

> `/System/Library/PrivateFrameworks/Weave.framework/Weave`

```diff

-5.0.1.0.0
-  __TEXT.__text: 0x76a8
-  __TEXT.__auth_stubs: 0x510
-  __TEXT.__objc_methlist: 0x97c
-  __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x23d
-  __TEXT.__oslogstring: 0xb41
-  __TEXT.__gcc_except_tab: 0x118
-  __TEXT.__unwind_info: 0x230
-  __TEXT.__objc_classname: 0x208
-  __TEXT.__objc_methname: 0x14c3
-  __TEXT.__objc_methtype: 0x599
-  __TEXT.__objc_stubs: 0x12a0
+5.100.6.0.0
+  __TEXT.__text: 0x882c
+  __TEXT.__auth_stubs: 0x4f0
+  __TEXT.__objc_methlist: 0xa1c
+  __TEXT.__const: 0x80
+  __TEXT.__cstring: 0x269
+  __TEXT.__oslogstring: 0xd4b
+  __TEXT.__gcc_except_tab: 0x108
+  __TEXT.__unwind_info: 0x260
+  __TEXT.__objc_classname: 0x209
+  __TEXT.__objc_methname: 0x1633
+  __TEXT.__objc_methtype: 0x5dc
+  __TEXT.__objc_stubs: 0x1420
   __DATA_CONST.__got: 0x98
-  __DATA_CONST.__const: 0x1a8
+  __DATA_CONST.__const: 0x1d0
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x660
+  __DATA_CONST.__objc_selrefs: 0x6c8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x298
-  __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x120
-  __AUTH_CONST.__objc_const: 0x1328
-  __AUTH.__objc_data: 0x410
-  __DATA.__objc_ivar: 0xb4
+  __AUTH_CONST.__auth_got: 0x288
+  __AUTH_CONST.__const: 0x100
+  __AUTH_CONST.__cfstring: 0x1a0
+  __AUTH_CONST.__objc_const: 0x1398
+  __DATA.__objc_ivar: 0xbc
   __DATA.__data: 0x480
-  __DATA.__bss: 0x10
+  __DATA.__bss: 0x1
+  __DATA_DIRTY.__objc_data: 0x410
+  __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/Polaris.framework/Polaris
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 464EC6C6-2177-30F7-90CE-AB1143A294E3
-  Functions: 160
-  Symbols:   805
-  CStrings:  477
+  UUID: D1A2848E-D504-3284-B90A-9643990A45F1
+  Functions: 180
+  Symbols:   864
+  CStrings:  509
 
Symbols:
+ -[WVGraphProviderParameters copyWithZone:]
+ -[WVGraphProviderParameters initWithIsReplayEnabled:replayURL:]
+ -[WVGraphProviderParameters initWithReplayURL:]
+ -[WVGraphProviderParameters init]
+ -[WVServer computeInputKeysFromGraphs:]
+ -[WVServer computeOutputKeysFromGraphs:]
+ -[WVServer configureServerWithParameters:]
+ -[WVServer createSessionIfNeeded].cold.1
+ -[WVServer updateParametersForGraphProvider:]
+ -[WVService configureServerWithParameters:]
+ -[WVService serviceDidInterrupt]
+ -[WVService serviceDidInvalidate]
+ _OBJC_IVAR_$_WVServer._graphProviderParameters
+ _OBJC_IVAR_$_WVServer._serverParameters
+ _WVGetBootArgs
+ _WVGetBootArgs.bootArgs
+ _WVGetBootArgs.cold.1
+ _WVGetBootArgs.onceToken
+ _WVPolarisOOLBootArgSet
+ _WVPolarisOOLBootArgSet.cold.1
+ _WVPolarisOOLBootArgSet.isBootArgSet
+ _WVPolarisOOLBootArgSet.onceToken
+ __OBJC_CLASS_PROTOCOLS_$_WVGraphProviderParameters
+ ___19-[WVServer _update]_block_invoke.94
+ ___32-[WVService initWithConnection:]_block_invoke_2
+ ___32-[WVService initWithConnection:]_block_invoke_3
+ ___33-[WVServer createSessionIfNeeded]_block_invoke.77
+ ___42-[WVServer configureServerWithParameters:]_block_invoke
+ ___WVGetBootArgs_block_invoke
+ ___WVPolarisOOLBootArgSet_block_invoke
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_literal_global.59
+ ___block_literal_global.9
+ _createSessionIfNeeded.onceToken
+ _objc_msgSend$componentsSeparatedByString:
+ _objc_msgSend$computeInputKeysFromGraphs:
+ _objc_msgSend$computeOutputKeysFromGraphs:
+ _objc_msgSend$configureServerWithParameters:
+ _objc_msgSend$configureWithParameters:
+ _objc_msgSend$graphsWillBeRemoved:
+ _objc_msgSend$rangeOfString:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$substringFromIndex:
+ _objc_msgSend$substringToIndex:
+ _objc_msgSend$updateParametersForGraphProvider:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x24
+ _objc_retain_x27
+ _sysctlbyname
- ___19-[WVServer _update]_block_invoke.89
- ___32-[WVService initWithConnection:]_block_invoke.56
- ___32-[WVService initWithConnection:]_block_invoke.59
- ___block_literal_global.61
- ___chkstk_darwin
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x22
- _objc_retain_x25
CStrings:
+ " "
+ "%04d: Graph Provider Parameter Update: %@ doesn't implement configureWithParameters but tracking parameter update "
+ "%04d: Graph Provider Parameter Update: %@ updating parameters to %@ "
+ "%04d: Graph provider configuration requested from service "
+ "%04d: Graph to add %@ "
+ "%04d: Graph to remove %@ "
+ "%04d: Removed deallocated graph provider %@ from parameters dictionary "
+ "%04d: Service: %@ serviceDidInterrupt "
+ "%04d: Service: %@ serviceDidInvalidate "
+ "%04d: Submitted graphs successfully "
+ "%04d: WARNING: ool_port_array_enforced=0 boot arg is not set! Polaris functionality is disabled. "
+ "%04d: unable to query sysctl 'kern.bootargs' "
+ "0"
+ "="
+ "@\"WVGraphProviderParameters\""
+ "_graphProviderParameters"
+ "_serverParameters"
+ "componentsSeparatedByString:"
+ "computeInputKeysFromGraphs:"
+ "computeOutputKeysFromGraphs:"
+ "configureServerWithParameters:"
+ "configureWithParameters:"
+ "graphsWillBeRemoved:"
+ "initWithIsReplayEnabled:replayURL:"
+ "kern.bootargs"
+ "ool_port_array_enforced"
+ "rangeOfString:"
+ "setObject:forKey:"
+ "stringWithUTF8String:"
+ "substringFromIndex:"
+ "substringToIndex:"
+ "updateParametersForGraphProvider:"
+ "v24@0:8@\"WVGraphProviderParameters\"16"
- "%04d: %@ interrupted "
- "%04d: %@ invalidated "
- "%04d: Added %@ "
- "%04d: Removed %@ "
- "%04d: Submitted graphs "

```
