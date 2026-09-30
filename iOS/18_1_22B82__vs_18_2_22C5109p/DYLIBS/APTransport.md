## APTransport

> `/System/Library/PrivateFrameworks/APTransport.framework/APTransport`

```diff

-830.10.1.1.0
-  __TEXT.__text: 0x8f08c
-  __TEXT.__auth_stubs: 0x2fe0
+835.13.1.11.1
+  __TEXT.__text: 0x8f258
+  __TEXT.__auth_stubs: 0x3000
   __TEXT.__objc_methlist: 0x93c
-  __TEXT.__cstring: 0x287d9
+  __TEXT.__cstring: 0x28724
   __TEXT.__const: 0x2c8
   __TEXT.__gcc_except_tab: 0x394
   __TEXT.__oslogstring: 0x16e

   __DATA_CONST.__objc_selrefs: 0xd20
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x1800
+  __AUTH_CONST.__auth_got: 0x1810
   __AUTH_CONST.__const: 0x29f8
-  __AUTH_CONST.__cfstring: 0x5680
+  __AUTH_CONST.__cfstring: 0x56c0
   __AUTH_CONST.__objc_const: 0x1790
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x30

   - /usr/lib/libIOReport.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1852
-  Symbols:   3044
-  CStrings:  4570
+  Functions: 1853
+  Symbols:   3047
+  CStrings:  4572
 
Symbols:
+ _APSStallMonitorActivityBegin
+ _APSStallMonitorActivityCreate
+ _APSStallMonitorActivityEnd
+ _APTransportDeviceParseInterfaceIndexFromDNSName
+ _strpbrk
- _APSGetCurrentLocalTimeString
- _FigCFDictionaryGetValue
CStrings:
+ "    DeviceID:%!@(MISSING)"
+ " AdvertiserInfo:%!s(MISSING)"
+ " Name:%!s(MISSING)"
+ " _airplay=%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)"
+ " legacy=%!@(MISSING) modern=%!@(MISSING) eventDispatched=<%!@(MISSING)>"
+ "%!N(MISSING)"
+ "835.13.1.11.1"
+ ":]"
+ "APTransportDeviceParseInterfaceIndexFromDNSName"
+ "Device %!@(MISSING) transports: _airplay=%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING) _raop=%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING) _airplay-p2p=%!s(MISSING)%!s(MISSING) cached=%!s(MISSING)\n"
+ "TCPUnbufNW[%!{(MISSING)ptr}]::RequestData"
+ "[%!{(MISSING)ptr}] %!s(MISSING) to '%!a(MISSING)' err=%!m(MISSING)"
+ "[%!{(MISSING)ptr}] APTKeepAliveControllerLowPower finalizing for stream [%!{(MISSING)ptr}]\n"
+ "[%!{(MISSING)ptr}] APTransportConnectionHTTP finalizing"
+ "[%!{(MISSING)ptr}] APTransportConnectionHTTP invalidating"
+ "[%!{(MISSING)ptr}] APTransportConnectionHTTP with name %!'(MISSING)@ created. QoS: %!d(MISSING) Priority: %!u(MISSING)"
+ "[%!{(MISSING)ptr}] APTransportConnectionHTTP with name %!@(MISSING) invalidating"
+ "[%!{(MISSING)ptr}] APTransportKeepAliveControllerStandard finalizing for stream [%!{(MISSING)ptr}]\n"
+ "[%!{(MISSING)ptr}] Address resolution failed with error %!m(MISSING)"
+ "[%!{(MISSING)ptr}] Address resolved to %!@(MISSING):%!d(MISSING), ifIndex: %!u(MISSING)"
+ "[%!{(MISSING)ptr}] Async connecting to '%!s(MISSING)' port %!d(MISSING) ifIndex: %!u(MISSING)"
+ "[%!{(MISSING)ptr}] Configuring encryption"
+ "[%!{(MISSING)ptr}] Connected to address: %!a(MISSING)"
+ "[%!{(MISSING)ptr}] Connecting failed with error %!m(MISSING)"
+ "[%!{(MISSING)ptr}] Connecting to '%!s(MISSING)' over %!s(MISSING)..."
+ "[%!{(MISSING)ptr}] Connecting to '%!s(MISSING)'..."
+ "[%!{(MISSING)ptr}] Connecting to address: %!a(MISSING)"
+ "[%!{(MISSING)ptr}] Connection [%!{(MISSING)ptr}] closed to %!a(MISSING) (from %!a(MISSING))"
+ "[%!{(MISSING)ptr}] Connection already resumed"
+ "[%!{(MISSING)ptr}] Connection no longer stalled"
+ "[%!{(MISSING)ptr}] Connection stalled for %!f(MISSING) seconds"
+ "[%!{(MISSING)ptr}] Created HTTP package [%!{(MISSING)ptr}]"
+ "[%!{(MISSING)ptr}] Deregister traffic failed with error %!m(MISSING)"
+ "[%!{(MISSING)ptr}] Don't know how to open a network connection (no Bonjour info or destination IP address/port)"
+ "[%!{(MISSING)ptr}] Event message received from %!a(MISSING), Header %!z(MISSING)u bytes, Body %!z(MISSING)u bytes, ID 0x%!X(MISSING)"
+ "[%!{(MISSING)ptr}] Event was not handled"
+ "[%!{(MISSING)ptr}] Expected NAN interface but received non-NAN interface"
+ "[%!{(MISSING)ptr}] Expected P2P interface but received non-P2P interface"
+ "[%!{(MISSING)ptr}] Failed to handle incoming connection. Error: %!m(MISSING)"
+ "[%!{(MISSING)ptr}] Failed with error %!m(MISSING)"
+ "[%!{(MISSING)ptr}] Forcing iPv4 addressing mode"
+ "[%!{(MISSING)ptr}] HTTP %!s(MISSING) connection established"
+ "[%!{(MISSING)ptr}] HTTP connection connected"
+ "[%!{(MISSING)ptr}] HTTPClient connected to %!a(MISSING) (from %!a(MISSING)) with CID 0x%!X(MISSING)"
+ "[%!{(MISSING)ptr}] HTTPServer connected to %!a(MISSING) (from %!a(MISSING))"
+ "[%!{(MISSING)ptr}] Incoming http connection connected"
+ "[%!{(MISSING)ptr}] Initial traffic registration %!s(MISSING) by prefs"
+ "[%!{(MISSING)ptr}] Invalid APTransportConnectionStallState = %!d(MISSING)"
+ "[%!{(MISSING)ptr}] Invalid traffic PeerGroupIdentifier for connections to multiple peers"
+ "[%!{(MISSING)ptr}] Invalidate with reason %!m(MISSING). Connection to %!a(MISSING) (from %!a(MISSING)) closed"
+ "[%!{(MISSING)ptr}] Message read finished%!?(MISSING)s%!?(MISSING)#m.\n"
+ "[%!{(MISSING)ptr}] Message read started, type = %!d(MISSING).\n"
+ "[%!{(MISSING)ptr}] Package send timeout set to %!d(MISSING) seconds"
+ "[%!{(MISSING)ptr}] Peer's MAC address is not available. Cannot perform Traffic Registration"
+ "[%!{(MISSING)ptr}] Querying SRV: %!s(MISSING)"
+ "[%!{(MISSING)ptr}] Received response for httpMessage [%!{(MISSING)ptr}] groupID %!d(MISSING)"
+ "[%!{(MISSING)ptr}] Register traffic failed with error %!m(MISSING)"
+ "[%!{(MISSING)ptr}] Resolving DNS: %!s(MISSING)"
+ "[%!{(MISSING)ptr}] Resuming connection"
+ "[%!{(MISSING)ptr}] Sending package [%!{(MISSING)ptr}] groupID %!d(MISSING) httpMessage [%!{(MISSING)ptr}]"
+ "[%!{(MISSING)ptr}] Set connect timeout to %!f(MISSING) seconds"
+ "err = "
- "    AdvertiserInfo:%!s(MISSING)"
- "    DeviceID:%!@(MISSING) transports:"
- "    Name:%!s(MISSING)"
- " _airplay=%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)"
- " eventDispatched:%!@(MISSING)"
- "### [%!{(MISSING)ptr}] %!s(MISSING) Don't know how to open a network connection (no Bonjour info or destination IP address/port).\n"
- "### [%!{(MISSING)ptr}] %!s(MISSING): connecting failed with error %!m(MISSING).\n"
- "### [%!{(MISSING)ptr}] %!s(MISSING): connection %!{(MISSING)ptr} closed to %!a(MISSING) (from %!a(MISSING))\n"
- "### [%!{(MISSING)ptr}] %!s(MISSING): failed with error %!m(MISSING).\n"
- "### [%!{(MISSING)ptr}] %!s(MISSING): invalidate with reason %!m(MISSING).\n"
- "%!s(MISSING), interface didn't match\n"
- "%!s(MISSING): de-register traffic failed with error %!m(MISSING)\n"
- "830.10.1.1"
- "APTKeepAliveControllerLowPower finalizing\n"
- "APTransportConnectionHTTP %!{(MISSING)ptr} invalid traffic PeerGroupIdentifier for connections to multiple peers.\n"
- "APTransportConnectionHTTP %!{(MISSING)ptr} set connect timeout to %!f(MISSING) seconds.\n"
- "APTransportConnectionHTTP %!{(MISSING)ptr} with name %!@(MISSING) invalidating.\n"
- "Device %!@(MISSING) transports: _airplay=%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING) _raop=%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING) _airplay-p2p=%!s(MISSING)%!s(MISSING) cached=%!s(MISSING)\n"
- "Initial traffic registration %!s(MISSING) by prefs.\n"
- "Invalid APTransportConnectionStallState = %!d(MISSING)\n"
- "OSStatus session_suspendKeepAliveInternal(void *)"
- "R"
- "[%!p(MISSING)] %!s(MISSING) called.\n"
- "[%!{(MISSING)ptr}] %!s(MISSING) Connecting to '%!s(MISSING)' over %!s(MISSING)...\n"
- "[%!{(MISSING)ptr}] %!s(MISSING) Connecting to '%!s(MISSING)'...\n"
- "[%!{(MISSING)ptr}] %!s(MISSING) Connection already resumed.\n"
- "[%!{(MISSING)ptr}] %!s(MISSING) called.\n"
- "[%!{(MISSING)ptr}] %!s(MISSING): %!m(MISSING) -- creating HTTP %!s(MISSING)\n"
- "[%!{(MISSING)ptr}] %!s(MISSING): -- configuring encryption.\n"
- "[%!{(MISSING)ptr}] %!s(MISSING): Connected to address: %!a(MISSING)\n"
- "[%!{(MISSING)ptr}] %!s(MISSING): Connecting to address: %!a(MISSING)\n"
- "[%!{(MISSING)ptr}] %!s(MISSING): HTTPClient connected to %!a(MISSING) (from %!a(MISSING)) with CID 0x%!X(MISSING)\n"
- "[%!{(MISSING)ptr}] %!s(MISSING): HTTPServer connected to %!a(MISSING) (from %!a(MISSING))\n"
- "[%!{(MISSING)ptr}] %!s(MISSING): Incoming http connection connected \n"
- "[%!{(MISSING)ptr}] %!s(MISSING): Querying SRV: %!s(MISSING)\n"
- "[%!{(MISSING)ptr}] %!s(MISSING): Resolving DNS: %!s(MISSING)\n"
- "[%!{(MISSING)ptr}] %!s(MISSING): WARNING: Forcing iPv4 addressing mode.\n"
- "[%!{(MISSING)ptr}] %!s(MISSING): http connection connected \n"
- "[%!{(MISSING)ptr}] %!s(MISSING): register traffic failed with error %!m(MISSING)\n"
- "[%!{(MISSING)ptr}] %!s(MISSING) '%!a(MISSING)' err=%!m(MISSING)"
- "[%!{(MISSING)ptr}] APTransportConnectionHTTP created HTTP package %!{(MISSING)ptr}.\n"
- "[%!{(MISSING)ptr}] APTransportConnectionHTTP finalizing.\n"
- "[%!{(MISSING)ptr}] APTransportConnectionHTTP invalidating\n"
- "[%!{(MISSING)ptr}] APTransportConnectionHTTP received response for httpMessage %!{(MISSING)ptr} groupID %!d(MISSING).\n"
- "[%!{(MISSING)ptr}] APTransportConnectionHTTP sending package %!{(MISSING)ptr} groupID %!d(MISSING) httpMessage %!{(MISSING)ptr}.\n"
- "[%!{(MISSING)ptr}] APTransportConnectionHTTP with name %!'(MISSING)@ created. QoS: %!d(MISSING) Priority: %!u(MISSING)\n"
- "[%!{(MISSING)ptr}] APTransportKeepAliveControllerStandard finalizing\n"
- "[%!{(MISSING)ptr}] Address resolution failed with error %!m(MISSING)\n"
- "[%!{(MISSING)ptr}] Address resolved to %!@(MISSING):%!d(MISSING), ifIndex: %!u(MISSING)\n"
- "[%!{(MISSING)ptr}] Async connecting to '%!s(MISSING)' port %!d(MISSING) ifIndex: %!u(MISSING)\n"
- "[%!{(MISSING)ptr}] Connection no longer stalled\n"
- "[%!{(MISSING)ptr}] Connection stalled for %!f(MISSING) seconds\n"
- "[%!{(MISSING)ptr}] Event message received from %!a(MISSING), Header %!z(MISSING)u bytes, Body %!z(MISSING)u bytes, ID 0x%!X(MISSING)\n"
- "[%!{(MISSING)ptr}] Event was not handled.\n"
- "[%!{(MISSING)ptr}] Invalidated keep alive controller [%!{(MISSING)ptr}] from stream [%!{(MISSING)ptr}].\n"
- "[%!{(MISSING)ptr}] Invalidated low power keep alive controller [%!{(MISSING)ptr}] from stream [%!{(MISSING)ptr}].\n"
- "[%!{(MISSING)ptr}] Message read finished.\n"
- "[%!{(MISSING)ptr}] Message read started.\n"
- "[%!{(MISSING)ptr}] Peer's MAC address is not available. Cannot perform Traffic Registration."
- "aptransportdevice_parseInterfaceIndexFromDNSName"

```
