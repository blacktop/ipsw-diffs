## wifivelocityd

> `/usr/libexec/wifivelocityd`

```diff

-1160.11.0.0.0
-  __TEXT.__text: 0x9cfa0
+1166.1.0.0.0
+  __TEXT.__text: 0x9c42c
   __TEXT.__auth_stubs: 0x13f0
-  __TEXT.__objc_stubs: 0xd320
-  __TEXT.__objc_methlist: 0x53cc
+  __TEXT.__objc_stubs: 0xd2c0
+  __TEXT.__objc_methlist: 0x53c4
   __TEXT.__dlopen_cstrs: 0x31a
   __TEXT.__const: 0x398
-  __TEXT.__gcc_except_tab: 0x189c
-  __TEXT.__objc_methname: 0xddf9
-  __TEXT.__oslogstring: 0xb178
-  __TEXT.__cstring: 0xc499
+  __TEXT.__gcc_except_tab: 0x1914
+  __TEXT.__objc_methname: 0xdd84
+  __TEXT.__oslogstring: 0xb26e
+  __TEXT.__cstring: 0xc4d3
   __TEXT.__objc_classname: 0x832
   __TEXT.__objc_methtype: 0x23e9
   __TEXT.__ustring: 0x8c
-  __TEXT.__unwind_info: 0x1b78
+  __TEXT.__unwind_info: 0x1b38
   __DATA_CONST.__auth_got: 0xa08
   __DATA_CONST.__got: 0x590
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x2940
-  __DATA_CONST.__cfstring: 0xaf80
+  __DATA_CONST.__const: 0x29b8
+  __DATA_CONST.__cfstring: 0xaf20
   __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x88

   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x240
   __DATA_CONST.__objc_intobj: 0xe88
-  __DATA_CONST.__objc_arraydata: 0x23a0
+  __DATA_CONST.__objc_arraydata: 0x2390
   __DATA_CONST.__objc_dictobj: 0x14f0
-  __DATA_CONST.__objc_arrayobj: 0x14e8
+  __DATA_CONST.__objc_arrayobj: 0x14b8
   __DATA_CONST.__objc_doubleobj: 0x80
-  __DATA.__objc_const: 0x8be0
-  __DATA.__objc_selrefs: 0x3ae8
-  __DATA.__objc_ivar: 0x6e4
+  __DATA.__objc_const: 0x8b70
+  __DATA.__objc_selrefs: 0x3ad0
+  __DATA.__objc_ivar: 0x6d8
   __DATA.__objc_data: 0x1770
   __DATA.__data: 0x660
   __DATA.__bss: 0x140

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
   - @rpath/BloodhoundKit.framework/BloodhoundKit
-  UUID: CD68B286-4229-3934-93E9-789A2A54F7ED
-  Functions: 2363
+  UUID: CC9A0425-414D-36D7-B8FA-1FA2B3F35676
+  Functions: 2344
   Symbols:   510
-  CStrings:  6739
+  CStrings:  6732
 
CStrings:
+ "-[W5WiFiInterface disassociate]"
+ "-[W5WiFiInterface setUserAutoJoinDisabled:error:]"
+ "-[W5WiFiInterface userAutoJoinDisabled]"
+ "CWFDisassocReasonUnspecified"
+ "ForWiFiDiagnosticsApp"
+ "[wifivelocity] %s (%s:%u) Disassociate w/reason '%{public}@'/%ld"
+ "[wifivelocity] %s (%s:%u) setUserAutoJoinDisabled: disabled[%u], bRet[%u] error: '%{public}@'"
+ "[wifivelocity] %s (%s:%u) tcpdump started, userAutoJoinDisabled[%u]"
+ "[wifivelocity] %s (%s:%u) userAutoJoinDisabled: disabled[%u]"
- "-dbg=print_nan_avail"
- "-nan"
- "-nan_peers"
- "Filtered known networks for customer install without MegaWiFi profile\n"
- "T@\"W5WiFiInterface\",R,&,V_nan"
- "[wifivelocity] %s (%s:%u) tcpdump started"
- "__startNANPerfLogging"
- "__startNANQueryTimer"
- "_nan"
- "_nanQueryFileHandle"
- "_nanQueryTimer"
- "nan"
- "nan_%@"

```
