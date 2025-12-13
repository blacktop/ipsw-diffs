## meshnetd

> `/usr/libexec/meshnetd`

```diff

-129.140.18.0.0
-  __TEXT.__text: 0x4fd8
-  __TEXT.__auth_stubs: 0x740
+129.140.18.700.1
+  __TEXT.__text: 0x50a0
+  __TEXT.__auth_stubs: 0x750
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x65a
-  __TEXT.__gcc_except_tab: 0x190
+  __TEXT.__gcc_except_tab: 0x1e0
   __TEXT.__cstring: 0x12c
   __TEXT.__oslogstring: 0x3ee
   __TEXT.__swift5_entry: 0x8

   __TEXT.__swift5_assocty: 0x20
   __TEXT.__swift5_proto: 0x60
   __TEXT.__swift5_types: 0x24
-  __TEXT.__unwind_info: 0x280
+  __TEXT.__unwind_info: 0x298
   __TEXT.__eh_frame: 0x160
-  __DATA_CONST.__auth_got: 0x3a8
+  __DATA_CONST.__auth_got: 0x3b0
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__auth_ptr: 0x150
   __DATA_CONST.__const: 0x3a0

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 9F3BC490-1F41-385B-ABBB-F6D603D3455A
-  Functions: 196
-  Symbols:   1603
+  UUID: 4F447925-59A5-35DF-AEA0-87F92EF0E27A
+  Functions: 198
+  Symbols:   1616
   CStrings:  30
 
Symbols:
+ GCC_except_table12
+ GCC_except_table18
+ GCC_except_table19
+ __ZN17AppleCIOMeshUtils10ScopeGuardIZN15AppleCIOMeshNet13TcpConnection7connectEPU19objcproto9OS_os_log8NSObjectPKctE3$_0ED1Ev
+ __ZN17AppleCIOMeshUtils10ScopeGuardIZN15AppleCIOMeshNet21TcpConnectionListener6listenEPU19objcproto9OS_os_log8NSObjecttE3$_0ED1Ev
+ _objc_release_x23
- GCC_except_table15
Functions:
~ __ZN15AppleCIOMeshNet13TcpConnection7connectEPU19objcproto9OS_os_log8NSObjectPKct : 756 -> 796
+ __ZN17AppleCIOMeshUtils10ScopeGuardIZN15AppleCIOMeshNet13TcpConnection7connectEPU19objcproto9OS_os_log8NSObjectPKctE3$_0ED1Ev
~ __ZN15AppleCIOMeshNet21TcpConnectionListener6listenEPU19objcproto9OS_os_log8NSObjectt : 632 -> 672
+ __ZN17AppleCIOMeshUtils10ScopeGuardIZN15AppleCIOMeshNet21TcpConnectionListener6listenEPU19objcproto9OS_os_log8NSObjecttE3$_0ED1Ev

```
