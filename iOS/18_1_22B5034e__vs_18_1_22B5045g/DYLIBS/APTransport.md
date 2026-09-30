## APTransport

> `/System/Library/PrivateFrameworks/APTransport.framework/APTransport`

```diff

-830.4.1.0.0
-  __TEXT.__text: 0x8e33c
-  __TEXT.__auth_stubs: 0x2f90
+830.6.1.0.0
+  __TEXT.__text: 0x8f088
+  __TEXT.__auth_stubs: 0x2fe0
   __TEXT.__objc_methlist: 0x93c
-  __TEXT.__cstring: 0x280e0
-  __TEXT.__const: 0x248
+  __TEXT.__cstring: 0x285e5
+  __TEXT.__const: 0x2c8
   __TEXT.__gcc_except_tab: 0x394
   __TEXT.__oslogstring: 0x16e
-  __TEXT.__unwind_info: 0x1600
+  __TEXT.__unwind_info: 0x1630
   __TEXT.__objc_classname: 0x111
   __TEXT.__objc_methname: 0x3135
   __TEXT.__objc_methtype: 0xb27

   __DATA_CONST.__objc_selrefs: 0xd20
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x17d8
+  __AUTH_CONST.__auth_got: 0x1800
   __AUTH_CONST.__const: 0x29f8
   __AUTH_CONST.__cfstring: 0x5680
   __AUTH_CONST.__objc_const: 0x1790
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0xf0
-  __AUTH.__data: 0xb8
+  __AUTH.__data: 0x2b0
   __DATA.__objc_ivar: 0x118
-  __DATA.__data: 0xf30
+  __DATA.__data: 0xfb0
   __DATA.__bss: 0x17c
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__data: 0xa18

   - /usr/lib/libIOReport.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1842
-  Symbols:   3029
-  CStrings:  4539
+  Functions: 1852
+  Symbols:   3044
+  CStrings:  4563
 
Symbols:
+ _APSHierarchyReporterProtocolGetProtocolID
+ _FigCFDictionaryGetValue
+ _FigCFWeakReferenceTableCopyValues
+ _FigCFDictionaryCopyArrayOfValues
+ _APSGetCurrentLocalTimeString
CStrings:
+ "Listener (IPv4) Local:%!a(MISSING) Parent:[%!{(MISSING)ptr}]\n"
+ "Connection:[%!{(MISSING)ptr}] (UDP) %!'(MISSING)'@ (Not Connected) Parent:[%!{(MISSING)ptr}]\n"
+ "    AdvertiserInfo:%!s(MISSING)"
+ "R"
+ "Listener (IPv6) Local:%!a(MISSING) Parent:[%!{(MISSING)ptr}]\n"
+ "[Error] Object:[%!{(MISSING)ptr}]%!?(MISSING)s%!?(MISSING)''@ cannot be dumped (error %!m(MISSING)) Parent:[%!{(MISSING)ptr}]\n"
+ "Listener Local:%!a(MISSING) Parent:[%!{(MISSING)ptr}]\n"
+ "udpconnection_DumpHierarchy"
+ "Connection:[%!{(MISSING)ptr}] (TCPUnbufferedNW) %!'(MISSING)'@ (Not Connected) Parent:[%!{(MISSING)ptr}]\n"
+ " "
+ "Connection:[%!{(MISSING)ptr}] (UDP) %!'(MISSING)'@ Remote:%!a(MISSING)%!?(MISSING)s%!?(MISSING)lu Parent:[%!{(MISSING)ptr}]\n"
+ "session_DumpHierarchy"
+ " eventDispatched:%!@(MISSING)"
+ "TransportSession:[%!{(MISSING)ptr}] %!'(MISSING)'@ Parent:[%!{(MISSING)ptr}]\n"
+ "Connection:[%!{(MISSING)ptr}] (HTTP) %!'(MISSING)'@ (Not Connected) Parent:[%!{(MISSING)ptr}]\n"
+ " _airplay=%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)"
+ "Connection:[%!{(MISSING)ptr}] (UDPNW) %!'(MISSING)'@ Remote:%!a(MISSING)%!?(MISSING)s%!?(MISSING)lu Parent:[%!{(MISSING)ptr}]\n"
+ "Connection:[%!{(MISSING)ptr}] (TCPUnbuffered) %!'(MISSING)'@ (Not Connected) Parent:[%!{(MISSING)ptr}]\n"
+ "Stream:[%!{(MISSING)ptr}] (Buffered) %!'(MISSING)'@ Parent:[%!{(MISSING)ptr}]\n"
+ "Device %!@(MISSING) transports: _airplay=%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING) _raop=%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING) _airplay-p2p=%!s(MISSING)%!s(MISSING) cached=%!s(MISSING)\n"
+ "Connection:[%!{(MISSING)ptr}] (UDPNW) %!'(MISSING)'@ (Not Connected) Parent:[%!{(MISSING)ptr}]\n"
+ "    DeviceID:%!@(MISSING) transports:"
+ "Connection:[%!{(MISSING)ptr}] (TCPUnbuffered) %!'(MISSING)'@ Ports:%!a(MISSING) -> %!a(MISSING)%!?(MISSING)s%!?(MISSING)lu Parent:[%!{(MISSING)ptr}]\n"
+ " IDX:"
+ "Connection:[%!{(MISSING)ptr}] (TCP) %!'(MISSING)'@ Ports:%!a(MISSING) -> %!a(MISSING)%!?(MISSING)s%!?(MISSING)lu Parent:[%!{(MISSING)ptr}]\n"
+ "Connection:[%!{(MISSING)ptr}] (TCP) %!'(MISSING)'@ (Not Connected) Parent:[%!{(MISSING)ptr}]\n"
+ "stream_DumpHierarchy"
+ "Stream:[%!{(MISSING)ptr}] (Unbuffered) %!'(MISSING)'@ Parent:[%!{(MISSING)ptr}]\n"
+ "Connection:[%!{(MISSING)ptr}] (TCPUnbufferedNW) %!'(MISSING)'@ Ports:%!a(MISSING) -> %!a(MISSING) Parent:[%!{(MISSING)ptr}]\n"
+ "[%!{(MISSING)ptr}] %!s(MISSING) '%!a(MISSING)' err=%!m(MISSING)"
+ "830.6.1"
+ "    Name:%!s(MISSING)"
+ "Connection:[%!{(MISSING)ptr}] (HTTP) %!'(MISSING)'@ Ports:%!a(MISSING) -> %!a(MISSING) CID:0x%!X(MISSING) Parent:[%!{(MISSING)ptr}]\n"
- " legacy=%!@(MISSING) modern=%!@(MISSING) eventDispatched=<%!@(MISSING)>"
- "    DeviceID:%!@(MISSING)"
- "830.4.1"
- " Name:%!s(MISSING)"
- " AdvertiserInfo:%!s(MISSING)"
- "%!N(MISSING)"
- "[%!{(MISSING)ptr}] %!s(MISSING) to '%!a(MISSING)' err=%!m(MISSING)"
- " _airplay=%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)"
- "Device %!@(MISSING) transports: _airplay=%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING) _raop=%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING) _airplay-p2p=%!s(MISSING)%!s(MISSING) cached=%!s(MISSING)\n"

```
