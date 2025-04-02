## threadradiod

> `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/threadradiod`

```diff

-275.0.104.0.0
-  __TEXT.__text: 0x3cb558
+275.0.502.0.0
+  __TEXT.__text: 0x3cb948
   __TEXT.__auth_stubs: 0x11470
   __TEXT.__objc_stubs: 0x9680
   __TEXT.__init_offsets: 0xa4
   __TEXT.__objc_methlist: 0x64f0
   __TEXT.__objc_classname: 0x5f4
   __TEXT.__const: 0x81d0
-  __TEXT.__gcc_except_tab: 0x2a734
+  __TEXT.__gcc_except_tab: 0x2a778
   __TEXT.__objc_methname: 0xe952
-  __TEXT.__cstring: 0x2f2fd
-  __TEXT.__oslogstring: 0x228cc
+  __TEXT.__cstring: 0x2f3a7
+  __TEXT.__oslogstring: 0x2298b
   __TEXT.__objc_methtype: 0x4450
   __TEXT.__unwind_info: 0x7288
   __TEXT.__eh_frame: 0x60

   __DATA.__objc_data: 0xe60
   __DATA.__data: 0x5b8
   __DATA.__common: 0x3fdc4
-  __DATA.__bss: 0x14eab
+  __DATA.__bss: 0x14ec3
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libdns_services.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 15783
-  Symbols:   82242
-  CStrings:  12109
+  Functions: 15784
+  Symbols:   82247
+  CStrings:  12115
 
Symbols:
+ GCC_except_table1106
+ GCC_except_table296
+ GCC_except_table332
+ GCC_except_table406
+ GCC_except_table434
+ GCC_except_table517
+ __ZN15HostInterpreter17btAudioCallStatusEv
+ __block_descriptor_tmp.11
- GCC_except_table1105
- GCC_except_table220
- GCC_except_table230
- GCC_except_table235
- GCC_except_table306
- GCC_except_table310
- GCC_except_table342
- GCC_except_table490
- GCC_except_table514
- __block_descriptor_tmp.10
CStrings:
+ " Morty_Version: V0.275.0.502"
+ "%s: BT Load, Audio detection: First time call threadStart, notify WRM to start to send coex load value."
+ "%s: BT Load: Audio detection: Continue Listening to Coex Load as BT Audio call(2EV3/2EV5)is ongoing"
+ "%s: BT Load: No Audio Detected, Close XPC Connection with WRM"
+ "%s: ThreadSession/ThreadSessionJoin both are OFF, Notify WRM, no need to bring back thread network."
+ "-[ThreadNetworkManagerInstance persistThreadSession:]"
+ "BT Load: %s Receive coex load value when Thread is offline."
+ "WCM: %s ThreadSession = [%d], listenCoexLoadChange = [%d], Notify WRM"
+ "com.apple.private.fillmore.threadMeshInfoForHomeMetrics"
+ "kWCMThreadListenCoexLoadChange"
+ "threadMeshInfoForHomeMetrics"
- " Morty_Version: V0.275.0.103"
- "%s: BT Load, Audio detection: Frist time call threadStart, notify WRM to start to send coex load value."
- "BT Load: ThreadSession/ThreadSessionJoin Both are OFF, Notify WRM"
- "ThreadSession/ThreadSessionJoin both are OFF, Notify WRM, no need to bring back thread network."
- "WCM: %s ThreadSession = %d, Notify WRM"

```
