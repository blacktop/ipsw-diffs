## meshnetd

> `/usr/libexec/meshnetd`

```diff

-222.0.0.0.0
-  __TEXT.__text: 0x4eac
-  __TEXT.__auth_stubs: 0x740
+222.42.1.0.0
+  __TEXT.__text: 0x4f74
+  __TEXT.__auth_stubs: 0x750
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x6c8
-  __TEXT.__gcc_except_tab: 0x190
+  __TEXT.__gcc_except_tab: 0x1e0
   __TEXT.__cstring: 0x12c
   __TEXT.__oslogstring: 0x3ee
   __TEXT.__swift5_entry: 0x8

   __TEXT.__swift5_assocty: 0x20
   __TEXT.__swift5_proto: 0x60
   __TEXT.__swift5_types: 0x24
-  __TEXT.__unwind_info: 0x298
+  __TEXT.__unwind_info: 0x2b0
   __TEXT.__eh_frame: 0x198
-  __DATA_CONST.__auth_got: 0x3a8
+  __DATA_CONST.__auth_got: 0x3b0
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__auth_ptr: 0x148
   __DATA_CONST.__const: 0x388

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 81EBE15C-9853-30E4-B7D6-84FCDB584BAF
-  Functions: 197
-  Symbols:   1572
+  UUID: 0C38C561-9327-357D-B8F7-9B5BBFE93A31
+  Functions: 199
+  Symbols:   1585
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
