## skywalkctl

> `/usr/sbin/skywalkctl`

```diff

-157.0.0.0.0
-  __TEXT.__text: 0xfff0
-  __TEXT.__auth_stubs: 0x660
-  __TEXT.__cstring: 0xbb4a
+163.0.0.0.0
+  __TEXT.__text: 0x10b50
+  __TEXT.__auth_stubs: 0x680
+  __TEXT.__cstring: 0xc104
   __TEXT.__const: 0x60
-  __TEXT.__unwind_info: 0x238
-  __DATA_CONST.__auth_got: 0x330
+  __TEXT.__unwind_info: 0x240
+  __DATA_CONST.__auth_got: 0x340
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x3938
+  __DATA_CONST.__const: 0x42d8
   __DATA.__data: 0x47c
-  __DATA.__common: 0xb0
+  __DATA.__common: 0xb8
   __DATA.__bss: 0x765
   - /usr/lib/libSystem.B.dylib
-  UUID: 12C33F47-8B78-3D4F-8632-434DA1CA0F17
-  Functions: 157
-  Symbols:   112
-  CStrings:  2011
+  UUID: DA5C71EA-D68B-3A35-A6B0-084648932DA8
+  Functions: 158
+  Symbols:   114
+  CStrings:  2065
 
Symbols:
+ _ether_aton
+ _ether_ntoa
CStrings:
+ "\t\t%llu dropped, flow Rx disabled\n"
+ "\t\t%llu dropped, flow tx disabled\n"
+ "\t%llu rx flow steering add failure\n"
+ "\t%llu rx flow steering add success\n"
+ "\t%llu rx flow steering remove failure\n"
+ "\t%llu rx flow steering remove skipped\n"
+ "\t%llu rx flow steering remove success\n"
+ "\t%llu total Rx dropped\n"
+ "\t%llu total Tx dropped\n"
+ "\t%llu total pending Rx not completed\n"
+ "\t%llu total pending Tx not completed\n"
+ "\tCell: Start = %llu, Bitmap = %s\n"
+ "\tWiFi: Start = %llu, Bitmap = %s\n"
+ "%-20s\n"
+ "%-5s %-45s %-45s %-12s %-12s %-18s %-18s %-3s %-8s %-4s %-3s %-17s %-12s %-12s %-10s %-10s %36s %s\n"
+ "%-5s %-45s %-45s %-12s %-12s %-18s %-18s %-3s %-8s %-4s %-3s %-17s %-12s %-12s %-10s %-10s %s\n"
+ "%016llx"
+ "%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c "
+ "0x"
+ "AOP:"
+ "Activity Bitmap:"
+ "C:hI:nJp:P:w:v"
+ "Error, mismatching activity bitmap stats, quit\n"
+ "Error, mismatching aop_driver_stats, quit\n"
+ "Error, mismatching aop_proc_activity_bitmap, quit\n"
+ "RxDisabled"
+ "RxDrop"
+ "RxFSAddFailure"
+ "RxFSAddSuccess"
+ "RxFSRemoveFailure"
+ "RxFSRemoveSkipped"
+ "RxFSRemoveSuccess"
+ "RxPending"
+ "TxDisabled"
+ "TxDrop"
+ "TxPending"
+ "UUID"
+ "Usage aop [ OPTIONS ] show AOP statistics\n   -h, --help          this message\n   -b, --bitmap        show AOP activity bitmaps\n"
+ "Usage: netstat [ OPTIONS ]\n   -h, --help            this message\n   -a, --all             show all flows\n   -C, --command=CMD     show memory usage from process matching CMD\n   -G, --global          show folded global stats\n   -I, --interface=IF    show memory usage matching IF\n   -n, --numeric         show network address as number\n   -o, --aop             show AOP stats\n   -P, --pid=PID         match based on PID\n   -p, --protocol=PROTO  match based on PROTO\n   -s, --statistics      show per-protocol statistics\n   -U, --uuid=UUID       match based on nexus uuid\n   -v, --verbose         verbose output\n   -z, --zero            show zero fields in statistics\n"
+ "Usage: traffic-rule add [ OPTIONS ]\n\t-t, --type <typename>     Supported rule type: inet, eth\n\tThese options only apply to rule type 'inet':\n\t\t-p, --proto <protocol>    Transport Protocol: tcp, udp\n\t\t-l, --laddr <localaddr>   Local IP address: v4 or v6 address\n\t\t-r, --raddr <remoteaddr>  Remote IP address: v4 or v6 address\n\t\t-L, --lport <localport>   Local port\n\t\t-R, --rport <remoteport>  Remote port\n\tThese options only apply to rule type 'eth':\n\t\t-e, --ethertype <ether type>   Ether type: eap, wai\n\t\t-m, --rmac <remotemac>  Remote mac address\n\tThese options are common for all rules:\n\t\t-q, --qset <qset>         Queue set ID\n\t\t-i, --interface <ifname>  Interface name: e.g. en0\n"
+ "__SK_VERB_12"
+ "aC:GI:nop:P:sU:vz"
+ "aop"
+ "at least one parameter is needed\n"
+ "bh"
+ "bitmap"
+ "eap"
+ "end of driver stats"
+ "eth"
+ "ethertype"
+ "filter: %s\n"
+ "invalid ether type: %s\n"
+ "invalid remote mac addr: %s\n"
+ "net.aop.driver_stats"
+ "net.aop.proc_activity_bitmaps"
+ "net.aop.protocol_stats"
+ "rmac"
+ "rmacaddr %s"
+ "t:p:l:r:L:R:q:i:e:m:"
+ "type: eth"
+ "type: inet"
+ "wai"
- "%-5s %-45s %-45s %-12s %-12s %-18s %-18s %-3s %-8s %-4s %-3s %-14s %-12s %-12s %-10s %-10s %s\n"
- "%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c "
- "C:hI:nJp:P:w:"
- "SK_VERB_MONITOR"
- "Usage: netstat [ OPTIONS ]\n   -h, --help            this message\n   -a, --all             show all flows\n   -C, --command=CMD     show memory usage from process matching CMD\n   -G, --global          show folded global stats\n   -I, --interface=IF    show memory usage matching IF\n   -n, --numeric         show network address as number\n   -P, --pid=PID         match based on PID\n   -p, --protocol=PROTO  match based on PROTO\n   -s, --statistics      show per-protocol statistics\n   -U, --uuid=UUID       match based on nexus uuid\n   -v, --verbose         verbose output\n   -z, --zero            show zero fields in statistics\n"
- "Usage: traffic-rule add [ OPTIONS ]\n\t-t, --type <typename>     Supported rule type: inet\n\tThese options only apply to rule type 'inet':\n\t\t-p, --proto <protocol>    Transport Protocol: tcp, udp\n\t\t-l, --laddr <localaddr>   Local IP address: v4 or v6 address\n\t\t-r, --raddr <remoteaddr>  Remote IP address: v4 or v6 address\n\t\t-L, --lport <localport>   Local port\n\t\t-R, --rport <remoteport>  Remote port\n\tThese options are common for all rules:\n\t\t-q, --qset <qset>         Queue set ID\n\t\t-i, --interface <ifname>  Interface name: e.g. en0\n"
- "aC:GI:np:P:sU:vz"
- "t:p:l:r:L:R:q:i:"

```
