## libRemoteTelephonyTransport.dylib

> `/usr/lib/libRemoteTelephonyTransport.dylib`

```diff

-6159.0.0.0.0
-  __TEXT.__text: 0x21470
-  __TEXT.__auth_stubs: 0x7c0
-  __TEXT.__const: 0x3533
-  __TEXT.__gcc_except_tab: 0xf98
-  __TEXT.__oslogstring: 0xcae
-  __TEXT.__cstring: 0x3c8
-  __TEXT.__unwind_info: 0xe88
+6161.0.0.0.0
+  __TEXT.__text: 0x2330c
+  __TEXT.__auth_stubs: 0x850
+  __TEXT.__const: 0x3a3b
+  __TEXT.__gcc_except_tab: 0x10dc
+  __TEXT.__oslogstring: 0xe4d
+  __TEXT.__cstring: 0x441
+  __TEXT.__unwind_info: 0xfc8
   __DATA_CONST.__got: 0x70
-  __DATA_CONST.__const: 0xc0
-  __AUTH_CONST.__auth_got: 0x3e8
-  __AUTH_CONST.__const: 0x2280
-  __DATA.__bss: 0x18
+  __DATA_CONST.__const: 0xe0
+  __AUTH_CONST.__auth_got: 0x430
+  __AUTH_CONST.__const: 0x2610
+  __AUTH_CONST.__cfstring: 0x40
+  __DATA.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libpcap.A.dylib
-  Functions: 906
-  Symbols:   1176
-  CStrings:  159
+  Functions: 981
+  Symbols:   1254
+  CStrings:  175
 
Symbols:
+ _TelephonyUtilIsBBPlatformSimulationEnabled
+ _TelephonyUtilIsOversteerEnabled
+ __ZN18telephonytransport9PCIClient14sharedInstanceEv
CStrings:
+ "Emplace failed while inserting token"
+ "Failed to create PCIClientTransport"
+ "Not instantiating PCI client because oversteer and bbsimulation are disabled"
+ "Oversteer: Starting PCIClient"
+ "Oversteer: Waiting for connection..."
+ "PCI transport for Oversteer created successfully with token %u"
+ "PCIClientContext"
+ "PCIClientTCPServer"
+ "PCIClientTransport"
+ "Received another connection. Restarting process..."
+ "Sending notification to indicate that PCIClient is ready"
+ "TTPCIClientReadyNotification"
+ "TTStartPCIClientNotification"
+ "Unable to start tcp server"
+ "lo0"
+ "pci"

```
