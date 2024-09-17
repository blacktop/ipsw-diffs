## threadradiod

> `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/threadradiod`

```diff

-263.0.1.0.0
-  __TEXT.__text: 0x3ca4b4
+263.0.3.0.0
+  __TEXT.__text: 0x3cb9c8
   __TEXT.__auth_stubs: 0x11140
   __TEXT.__objc_stubs: 0x94a0
   __TEXT.__init_offsets: 0x9c
   __TEXT.__objc_methlist: 0x5d60
   __TEXT.__objc_classname: 0x5f4
-  __TEXT.__const: 0x7fbb
-  __TEXT.__gcc_except_tab: 0x28bb8
+  __TEXT.__const: 0x805b
+  __TEXT.__gcc_except_tab: 0x28c6c
   __TEXT.__objc_methname: 0xe6b0
-  __TEXT.__cstring: 0x2c988
-  __TEXT.__oslogstring: 0x20a65
+  __TEXT.__cstring: 0x2cb36
+  __TEXT.__oslogstring: 0x20b5b
   __TEXT.__objc_methtype: 0x44f1
-  __TEXT.__unwind_info: 0x7670
+  __TEXT.__unwind_info: 0x7680
   __DATA_CONST.__auth_got: 0x88b8
   __DATA_CONST.__got: 0x900
   __DATA_CONST.__auth_ptr: 0x60
-  __DATA_CONST.__const: 0xae28
-  __DATA_CONST.__cfstring: 0x5660
+  __DATA_CONST.__const: 0xae40
+  __DATA_CONST.__cfstring: 0x56e0
   __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x50

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libdns_services.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 15861
-  Symbols:   81238
-  CStrings:  11710
+  Functions: 15872
+  Symbols:   81304
+  CStrings:  11735
 
Symbols:
+ _ZN15HostInterpreter22ProcessReconnectThreadEhPPcPv.cold.1
+ GCC_except_table367
+ GCC_except_table1078
+ __block_descriptor_tmp.185
+ __block_descriptor_tmp.86
+ GCC_except_table353
+ GCC_except_table346
+ __Z6isiPadv
+ _Z5isMacv.cold.1
+ main.cold.46
+ _ZN15HostInterpreter14processCommandEN5boost10shared_ptrI11HostCmdTaskEE.cold.41
+ _Z6isiPadv.cold.1
+ __block_descriptor_tmp.48
+ main.cold.43
+ __block_descriptor_tmp.54
+ __Z5isMacv
+ GCC_except_table180
+ __ZN14RcpHostContext23add_cmd_ReconnectThreadE15HostTaskCommandP26_RECONNECT_THREAD_CMD_DATA
+ __block_descriptor_tmp.44
+ GCC_except_table226
+ __ZN26_RECONNECT_THREAD_CMD_DATAD1Ev
+ _Z5isMacv.cold.2
+ GCC_except_table472
+ main.cold.44
+ GCC_except_table283
+ GCC_except_table246
+ _ZN16XPCIPCAPI_v1_rcp26interface_prop_get_handlerEPvNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEN8dispatch8callbackIU13block_pointerFvhN3xpc4dictEEEE.cold.5
+ __ZN15HostInterpreter22ProcessReconnectThreadEhPPcPv
+ _ZN11HostCmdTask12free_apidataEv.cold.35
+ GCC_except_table461
+ _Z6isiPadv.cold.2
+ GCC_except_table463
+ _otLinkRegenerateMleIid
+ GCC_except_table410
+ _ZN16XPCIPCAPI_v1_rcp26interface_prop_get_handlerEPvNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEN8dispatch8callbackIU13block_pointerFvhN3xpc4dictEEEE.cold.6
+ main.cold.45
+ GCC_except_table177
+ __block_descriptor_tmp.40
+ __block_descriptor_tmp.190
+ __ZN2ot3Mle3Mle14GenerateMleIidEv
+ __block_descriptor_tmp.541
- __block_descriptor_tmp.184
- GCC_except_table357
- __block_descriptor_tmp.47
- GCC_except_table462
- GCC_except_table198
- __block_descriptor_tmp.43
- GCC_except_table220
- __block_descriptor_tmp.51
- GCC_except_table1076
- GCC_except_table297
- GCC_except_table176
- GCC_except_table395
- GCC_except_table174
- __block_descriptor_tmp.49
- __block_descriptor_tmp.189
- GCC_except_table227
- __block_descriptor_tmp.540
- GCC_except_table179
- GCC_except_table250
CStrings:
+ "bool isiPad()"
+ "ProcessReconnectThread"
+ "int main(int, char **)"
+ "Thread:Reconnect"
+ "MatteriPhoneOnlyPairingForMacEnabled"
+ "%!s(MISSING): It is an iPad"
+ "MatteriPhoneOnlyPairingForiPad"
+ "MatteriPhoneOnlyPairingForIPadEnabled"
+ "MatteriPhoneOnlyPairingForMac"
+ "free_apidata -> HOST_CMD_RECONNECT_THREAD"
+ "%!s(MISSING) unpack parse error: MAC-data"
+ "%!s(MISSING): reconnect_thread_network"
+ "%!s(MISSING): Thread feature is disabled for iPads"
+ "%!s(MISSING) Invoked"
+ "%!s(MISSING) Rx from %!s(MISSING) linkFrameCounter=%!d(MISSING) mleFrameCounter=%!d(MISSING)"
+ "bool isMac()"
+ "receiveError < OT_NUM_ERRORS, receiveError[%!d(MISSING)]"
+ "ReconnectThread"
+ "interface_prop_get_handler"
+ "%!s(MISSING): Thread feature is disabled for Macs"
+ " Morty_Version: V0.263.0.3"
+ "%!s(MISSING) unpack parse error: Frame "
+ "Mac"
+ "HandleParentResponse"
+ "%!s(MISSING): It is a Mac"
+ "=====> processHostCmd[HOST_CMD_RECONNECT_THREAD]"
+ "receiveError > OT_NUM_ERRORS. receiveError[%!d(MISSING)]"
- "MleRouter::HandleChildRequest: Rx linkFrameCounter=%!d(MISSING) mleFrameCounter=%!d(MISSING)"
- " Morty_Version: V0.263.0.1"

```
