## nesessionmanager

> `/usr/libexec/nesessionmanager`

```diff

-1838.102.2.0.0
-  __TEXT.__text: 0x8fd80
+1838.122.1.0.0
+  __TEXT.__text: 0x90420
   __TEXT.__auth_stubs: 0x1920
   __TEXT.__objc_stubs: 0x7080
-  __TEXT.__objc_methlist: 0x27ac
+  __TEXT.__objc_methlist: 0x27bc
   __TEXT.__const: 0x88
-  __TEXT.__gcc_except_tab: 0x14bc
+  __TEXT.__gcc_except_tab: 0x14b0
   __TEXT.__objc_classname: 0x8a9
   __TEXT.__objc_methname: 0x7fd0
   __TEXT.__objc_methtype: 0x1b3a
-  __TEXT.__oslogstring: 0xb084
-  __TEXT.__cstring: 0x3dc3
-  __TEXT.__unwind_info: 0x1208
+  __TEXT.__oslogstring: 0xb11d
+  __TEXT.__cstring: 0x3e93
+  __TEXT.__unwind_info: 0x120c
   __DATA_CONST.__auth_got: 0xca0
   __DATA_CONST.__got: 0x320
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1990
-  __DATA_CONST.__cfstring: 0x2100
+  __DATA_CONST.__const: 0x1970
+  __DATA_CONST.__cfstring: 0x2140
   __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0xf8

   __DATA_CONST.__objc_intobj: 0x1f8
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA.__objc_const: 0x72e0
-  __DATA.__objc_selrefs: 0x1d58
+  __DATA.__objc_selrefs: 0x1d60
   __DATA.__objc_ivar: 0x5e0
   __DATA.__objc_data: 0x1220
   __DATA.__data: 0xbb8

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B91877A1-5E39-359E-913A-A88217632C68
-  Functions: 1517
+  UUID: 6B99D02E-AF96-32BD-A159-BC7F38E3316A
+  Functions: 1519
   Symbols:   606
-  CStrings:  3570
+  CStrings:  3585
 
CStrings:
+ "%s: DeviceCommunication exception %s %s"
+ "%s: process %sallowed to %s DeviceCommunication exception"
+ "-[NEPolicySession(AlwaysOnVPN) addPortPoliciesWithOrder:eAppUUID:appUUID:port:local:]"
+ "-[NESMServer handleDeviceCommunicationException:initialMessage:]"
+ "979C0A62-49FE-4739-BDCB-CAC584AC832D"
+ "DeviceCommunicationExceptionEnable"
+ "DeviceCommunicationExceptionResult"
+ "Failed to create NESMServer control policy session"
+ "Found %lu registrations for %@ (%@)"
+ "Got a new client connection for DeviceCommunicationException %s(%d)"
+ "NESMServer Control"
+ "com.apple.PrintKit.PrinterTool"
+ "disable"
+ "enable"
+ "failed"
+ "not "
+ "succeeded"
+ "{\x13\x11\x11\x12\x15)"
- "-[NEPolicySession(AlwaysOnVPN) addPortPoliciesWithOrder:appUUID:port:local:]"
- "/System/Library/PrivateFrameworks/PrintKit.framework/printd"
- "Found %lu (%lu active) registrations for %@ (%@)"
- "Skipping inactive provider registration token %llu"
- "{\x13\x11\x11\x12\x15("

```
