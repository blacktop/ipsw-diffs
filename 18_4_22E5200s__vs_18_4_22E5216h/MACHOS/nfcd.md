## nfcd

> `/usr/libexec/nfcd`

```diff

-354.19.0.0.0
-  __TEXT.__text: 0x275de0
+354.25.0.0.0
+  __TEXT.__text: 0x2777c4
   __TEXT.__auth_stubs: 0x17e0
   __TEXT.__delay_helper: 0xec
-  __TEXT.__objc_stubs: 0xd940
-  __TEXT.__objc_methlist: 0x98c8
+  __TEXT.__objc_stubs: 0xd980
+  __TEXT.__objc_methlist: 0x98e0
   __TEXT.__const: 0x12e0
   __TEXT.__dlopen_cstrs: 0x5a1
-  __TEXT.__oslogstring: 0x24b67
-  __TEXT.__cstring: 0x2ef52
-  __TEXT.__objc_classname: 0x1bd8
-  __TEXT.__objc_methname: 0x17462
-  __TEXT.__objc_methtype: 0x5460
-  __TEXT.__gcc_except_tab: 0x7f38
-  __TEXT.__unwind_info: 0x3908
+  __TEXT.__oslogstring: 0x24df4
+  __TEXT.__cstring: 0x2f20e
+  __TEXT.__objc_classname: 0x1bd9
+  __TEXT.__objc_methname: 0x175ca
+  __TEXT.__objc_methtype: 0x547a
+  __TEXT.__gcc_except_tab: 0x7f2c
+  __TEXT.__unwind_info: 0x3920
   __DATA_CONST.__auth_got: 0xc00
   __DATA_CONST.__got: 0x448
-  __DATA_CONST.__const: 0x7518
-  __DATA_CONST.__cfstring: 0x10a60
+  __DATA_CONST.__const: 0x7590
+  __DATA_CONST.__cfstring: 0x10b40
   __DATA_CONST.__objc_classlist: 0x5d0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x378
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x1c8
-  __DATA_CONST.__objc_superrefs: 0x408
+  __DATA_CONST.__objc_superrefs: 0x420
   __DATA_CONST.__objc_intobj: 0x6f18
-  __DATA_CONST.__objc_arraydata: 0x1ce8
+  __DATA_CONST.__objc_arraydata: 0x1cf8
   __DATA_CONST.__objc_arrayobj: 0x2b8
   __DATA_CONST.__objc_dictobj: 0xe88
-  __DATA.__objc_const: 0x13900
-  __DATA.__objc_selrefs: 0x54c0
-  __DATA.__objc_ivar: 0xfd0
+  __DATA.__objc_const: 0x13970
+  __DATA.__objc_selrefs: 0x5508
+  __DATA.__objc_ivar: 0xfdc
   __DATA.__objc_data: 0x3a20
   __DATA.__data: 0x2a48
   __DATA.__bss: 0x500

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4471
+  Functions: 4481
   Symbols:   529
-  CStrings:  12334
+  CStrings:  12372
 
CStrings:
+ "\x03\x11\x19\x1f\x13\xa9"
+ "%c[%{public}s %{public}s]:%i %{public}@ error=%{public}@"
+ "%c[%{public}s %{public}s]:%i %{public}@, appState=%lu"
+ "%c[%{public}s %{public}s]:%i Assertion in place for %{public}@"
+ "%c[%{public}s %{public}s]:%i CH field detect overridden"
+ "%c[%{public}s %{public}s]:%i Client (%{public}@) is no longer suspended"
+ "%c[%{public}s %{public}s]:%i Override as initiator detected"
+ "%c[%{public}s %{public}s]:%i Override as receiver detected"
+ "%c[%{public}s %{public}s]:%i Refreshed: %{public}@, appState=%lu"
+ "%c[%{public}s %{public}s]:%i Removing XPC connection (invalidated=%d, isRBSApp=%d) for %{public}@ - %{public}@ "
+ "%c[%{public}s %{public}s]:%i Unexpected appState!"
+ "%c[%{public}s %{public}s]:%i Unexpected connection: %{public}@"
+ "%d (%@)"
+ "@36@0:8@16@24I32"
+ "ConnectTime"
+ "NFCD built from (B&I) Stockholm_Base-354.25"
+ "RBSApp"
+ "TQ,N,V_state"
+ "Vv68@0:8@\"NSArray\"16@\"NFApplet\"24@\"NSArray\"32@\"NSData\"40Q48I56@?<v@?@\"NSError\">60"
+ "Vv68@0:8@16@24@32@40Q48I56@?60"
+ "_asserterListFromConnection:"
+ "_connectionHandoverFieldDetectOverride"
+ "_isLaunchServiceBundle:record:"
+ "_secureElementInfoLock"
+ "_startCardEmulationWithApplet:externalAuth:ceType:"
+ "_sync_dequeueAllXPCSessionFromConnection:"
+ "appState"
+ "appStateFromConnection:"
+ "assertOnXPCClientRunningScheduled:"
+ "backgroundTagReading"
+ "chFieldDetectOverride"
+ "client app %@ suspended / background running"
+ "clientAppStateUpdate:appState:"
+ "connectionHandover"
+ "deassertOnXPCClientSuspension:"
+ "didCloseXPCConnection:invalidated:"
+ "isApplication"
+ "rbsInfoFromConnection:bundleIdentifier:isRBSApp:"
+ "removing XPC connection (invalidated=%d, isRBSApp=%d) for %@"
+ "requestApplets:selectOnStart:AIDAllowList:externalAuth:mode:ceType:completion:"
+ "setState:"
+ "v32@0:8@\"NSXPCConnection\"16Q24"
- "\x03\x1a\x1f\x13\xa9"
- "%c[%{public}s %{public}s]:%i Client is no longer suspended"
- "%c[%{public}s %{public}s]:%i Getting JCOP applets"
- "NFCD built from (B&I) Stockholm_Base-354.19"
- "Vv64@0:8@\"NSArray\"16@\"NFApplet\"24@\"NSArray\"32@\"NSData\"40Q48@?<v@?@\"NSError\">56"
- "Vv64@0:8@16@24@32@40Q48@?56"
- "_startCardEmulationWithApplet:externalAuth:"
- "bundleIdentifierFromConnection:error:"
- "client app %@ suspended"
- "clientAppIsSuspended:"
- "removing XPC connection for %@"
- "requestApplets:selectOnStart:AIDAllowList:externalAuth:mode:completion:"
- "v24@0:8@\"NSXPCConnection\"16"

```
