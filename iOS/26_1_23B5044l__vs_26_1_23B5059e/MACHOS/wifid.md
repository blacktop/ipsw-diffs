## wifid

> `/usr/sbin/wifid`

```diff

-1980.10.0.0.0
-  __TEXT.__text: 0x1ae3b0
+1980.15.0.0.0
+  __TEXT.__text: 0x1ae6d8
   __TEXT.__auth_stubs: 0x2990
   __TEXT.__objc_stubs: 0x12d40
   __TEXT.__objc_methlist: 0x5ba0
   __TEXT.__gcc_except_tab: 0x1c38
   __TEXT.__const: 0x9eb
-  __TEXT.__cstring: 0x6abd7
+  __TEXT.__cstring: 0x6ad51
   __TEXT.__objc_methname: 0x17911
   __TEXT.__objc_classname: 0x7c2
   __TEXT.__objc_methtype: 0x2f36
   __TEXT.__oslogstring: 0x2080
   __TEXT.__ustring: 0x4c2
   __TEXT.__dlopen_cstrs: 0x1a5
-  __TEXT.__unwind_info: 0x3d10
+  __TEXT.__unwind_info: 0x3d18
   __DATA_CONST.__auth_got: 0x14d8
   __DATA_CONST.__got: 0x12f0
   __DATA_CONST.__auth_ptr: 0x158
-  __DATA_CONST.__const: 0x72f0
-  __DATA_CONST.__cfstring: 0x1af60
+  __DATA_CONST.__const: 0x7320
+  __DATA_CONST.__cfstring: 0x1af80
   __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xc0

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  UUID: 474F7C7C-6AF7-3667-93AC-02534ED7051E
-  Functions: 7568
+  UUID: B69ED35A-012D-34A9-8EC3-F4D08A04E777
+  Functions: 7572
   Symbols:   1286
-  CStrings:  19280
+  CStrings:  19287
 
CStrings:
+ "%s: KnownNetworks sync is not OS-eligible"
+ "%s: WFMacRandomisation : Captive probe failure for network <%@>. Recover assuming probe failure"
+ "PrivateMacQuickProbeRequested"
+ "Remove network configuration <%@>, requested by \"%@\""
+ "WiFiManager-1980.15 Sep 29 2025 20:40:57"
+ "WiFiManager-1980.15 Sep 29 2025 20:41:31"
+ "__WiFiManagerPrivateMacApplyQuickProbeResult"
+ "kern_return_t _wifi_manager_remove_network_configuration(mach_port_t, vm_offset_t, mach_msg_type_number_t, int)"
- "WiFiManager-1980.10 Sep 11 2025 20:23:57"
- "WiFiManager-1980.10 Sep 11 2025 20:24:18"

```
