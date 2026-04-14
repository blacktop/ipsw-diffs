## MediaRemote

> `/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote`

```diff

-4025.600.4.0.0
-  __TEXT.__text: 0x316df4
+4025.600.6.0.0
+  __TEXT.__text: 0x3170a8
   __TEXT.__auth_stubs: 0x16c0
-  __TEXT.__objc_methlist: 0x2b430
+  __TEXT.__objc_methlist: 0x2b438
   __TEXT.__const: 0x5f0
-  __TEXT.__cstring: 0x2c6f0
-  __TEXT.__oslogstring: 0xdc9e
+  __TEXT.__cstring: 0x2c740
+  __TEXT.__oslogstring: 0xdcab
   __TEXT.__gcc_except_tab: 0x6588
   __TEXT.__dlopen_cstrs: 0x6b1
   __TEXT.__ustring: 0x7b8
   __TEXT.__unwind_info: 0xcd40
-  __TEXT.__objc_classname: 0x4e1c
-  __TEXT.__objc_methname: 0x4dabe
+  __TEXT.__objc_classname: 0x4e1d
+  __TEXT.__objc_methname: 0x4db0a
   __TEXT.__objc_methtype: 0x913a
   __TEXT.__objc_stubs: 0x28780
   __DATA_CONST.__got: 0x1450

   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x268
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf138
+  __DATA_CONST.__objc_selrefs: 0xf140
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0xfe8
   __DATA_CONST.__objc_arraydata: 0x260
   __AUTH_CONST.__auth_got: 0xb70
-  __AUTH_CONST.__const: 0x3100
-  __AUTH_CONST.__cfstring: 0x23500
-  __AUTH_CONST.__objc_const: 0x46188
+  __AUTH_CONST.__const: 0x3120
+  __AUTH_CONST.__cfstring: 0x23560
+  __AUTH_CONST.__objc_const: 0x461b8
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_intobj: 0x4f8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x8340
-  __DATA.__objc_ivar: 0x3268
+  __DATA.__objc_ivar: 0x326c
   __DATA.__data: 0x1d40
   __DATA.__bss: 0x8c0
   __DATA.__common: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F204ED9A-E18F-3CE9-8542-E7420FB8F34B
-  Functions: 20494
-  Symbols:   56383
-  CStrings:  24544
+  UUID: 5C30BDC1-6925-3AE8-9DEE-E4C0DD4EDC60
+  Functions: 20497
+  Symbols:   56391
+  CStrings:  24553
 
Symbols:
+ -[MRAVConcreteRoutingDiscoverySession ignoreNonLocalDevices]
+ _OBJC_IVAR_$_MRAVConcreteRoutingDiscoverySession._ignoreNonLocalDevices
+ ___60-[MRAVConcreteRoutingDiscoverySession _onReloadQueue_reload]_block_invoke_3
+ ___93-[MRAVConcreteRoutingDiscoverySession _onReloadQueue_createOutputDevicesFromAVOutputDevices:]_block_invoke.42
- ___93-[MRAVConcreteRoutingDiscoverySession _onReloadQueue_createOutputDevicesFromAVOutputDevices:]_block_invoke.40
Functions:
~ -[MRAVConcreteOutputDevice _loadLocalOverridesWithOutputContext:outputDevice:] : 1364 -> 1536
~ -[MRAVConcreteRoutingDiscoverySession _loadDefaults] : 864 -> 1284
~ -[MRAVConcreteRoutingDiscoverySession _onReloadQueue_reload] : 460 -> 516
~ _OUTLINED_FUNCTION_4 : 32 -> 20
~ _OUTLINED_FUNCTION_4 : 24 -> 32
~ _OUTLINED_FUNCTION_4 : 16 -> 24
+ _OUTLINED_FUNCTION_4
+ ___93-[MRAVConcreteRoutingDiscoverySession _onReloadQueue_createOutputDevicesFromAVOutputDevices:]_block_invoke.42
+ -[MRAVConcreteRoutingDiscoverySession userDefaults]
CStrings:
+ "TB,R,N,V_ignoreNonLocalDevices"
+ "[MRAVConcreteOutputDevice] ParentGroupID mismatch on <%@:%@> : <%@> -> <%@>"
+ "_ignoreNonLocalDevices"
+ "audio-ignore-non-local-devices"
+ "ignoreNonLocalDevices"
+ "stress-cycler-enabled-mode"
- "[MRAVConcreteOutputDevice] GroupID mismatch on %@:%@: %@ -> %@"

```
