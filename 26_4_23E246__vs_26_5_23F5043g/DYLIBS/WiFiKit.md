## WiFiKit

> `/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`

```diff

-1175.17.0.0.0
-  __TEXT.__text: 0xaf8d0
+1180.2.0.0.0
+  __TEXT.__text: 0xafbb8
   __TEXT.__auth_stubs: 0x1a50
-  __TEXT.__objc_methlist: 0x989c
+  __TEXT.__objc_methlist: 0x98c4
   __TEXT.__const: 0x783
-  __TEXT.__oslogstring: 0xb4b6
-  __TEXT.__cstring: 0xbecb
-  __TEXT.__gcc_except_tab: 0x29a8
+  __TEXT.__oslogstring: 0xb514
+  __TEXT.__cstring: 0xbf7b
+  __TEXT.__gcc_except_tab: 0x29e0
   __TEXT.__dlopen_cstrs: 0xac
   __TEXT.__ustring: 0x44
   __TEXT.__swift5_typeref: 0x1f1

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x30
   __TEXT.__swift5_types: 0x18
-  __TEXT.__unwind_info: 0x2538
+  __TEXT.__unwind_info: 0x2548
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0xeea
-  __TEXT.__objc_methname: 0x15cac
-  __TEXT.__objc_methtype: 0x30cc
-  __TEXT.__objc_stubs: 0xe8e0
+  __TEXT.__objc_methname: 0x15d0c
+  __TEXT.__objc_methtype: 0x30fc
+  __TEXT.__objc_stubs: 0xe900
   __DATA_CONST.__got: 0xcf0
-  __DATA_CONST.__const: 0x26f8
+  __DATA_CONST.__const: 0x2728
   __DATA_CONST.__objc_classlist: 0x360
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4df8
+  __DATA_CONST.__objc_selrefs: 0x4e10
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x298
   __DATA_CONST.__objc_arraydata: 0x1a0
   __AUTH_CONST.__auth_got: 0xd38
   __AUTH_CONST.__const: 0xdf0
-  __AUTH_CONST.__cfstring: 0x6f20
-  __AUTH_CONST.__objc_const: 0x192a0
+  __AUTH_CONST.__cfstring: 0x6f40
+  __AUTH_CONST.__objc_const: 0x192d0
   __AUTH_CONST.__objc_intobj: 0x6a8
   __AUTH_CONST.__objc_arrayobj: 0x1e0
   __AUTH.__objc_data: 0x1a08
   __AUTH.__data: 0x78
-  __DATA.__objc_ivar: 0xbc4
+  __DATA.__objc_ivar: 0xbc8
   __DATA.__data: 0x1520
   __DATA.__bss: 0x710
   __DATA_DIRTY.__objc_data: 0xaa0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E2223817-1483-300A-AB0A-10B034B18549
-  Functions: 3793
-  Symbols:   13211
-  CStrings:  7817
+  UUID: 974A7B34-E954-312D-9995-05224D5E6C25
+  Functions: 3797
+  Symbols:   13224
+  CStrings:  7831
 
Symbols:
+ -[WFPersonalHotspotStateMonitor _startMonitoringNETRBState]
+ -[WFPersonalHotspotStateMonitor netrbClient]
+ -[WFPersonalHotspotStateMonitor setNetrbClient:]
+ _OBJC_IVAR_$_WFPersonalHotspotStateMonitor._netrbClient
+ _WFPersonalHotspotNETRBStateChangeNotification
+ ___59-[WFPersonalHotspotStateMonitor _startMonitoringNETRBState]_block_invoke
+ ___block_descriptor_40_e8_32w_e36_i20?0i8"NSObject<OS_xpc_object>"12lw32l8
+ _objc_msgSend$_startMonitoringNETRBState
CStrings:
+ "%s: NETRB state change received (responseID: %d)"
+ "%s: failed to create persistent NETRB client"
+ "-[WFPersonalHotspotStateMonitor _startMonitoringNETRBState]"
+ "-[WFPersonalHotspotStateMonitor _startMonitoringNETRBState]_block_invoke"
+ "T^{NETRBClient=},N,V_netrbClient"
+ "WFPersonalHotspotNETRBStateChangeNotification"
+ "^{NETRBClient=}"
+ "^{NETRBClient=}16@0:8"
+ "_netrbClient"
+ "_startMonitoringNETRBState"
+ "netrbClient"
+ "setNetrbClient:"
+ "v24@0:8^{NETRBClient=}16"

```
