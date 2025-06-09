## ApplePhotonDetectorServices

> `/System/Library/PrivateFrameworks/ApplePhotonDetectorServices.framework/ApplePhotonDetectorServices`

```diff

-10.51.0.0.0
-  __TEXT.__text: 0x3394
-  __TEXT.__auth_stubs: 0x250
+10.52.0.0.0
+  __TEXT.__text: 0x419c
+  __TEXT.__auth_stubs: 0x270
   __TEXT.__const: 0x90
-  __TEXT.__gcc_except_tab: 0x10c
-  __TEXT.__cstring: 0x48a
-  __TEXT.__oslogstring: 0x6ed
-  __TEXT.__unwind_info: 0x100
+  __TEXT.__gcc_except_tab: 0x148
+  __TEXT.__cstring: 0x633
+  __TEXT.__oslogstring: 0x80b
+  __TEXT.__unwind_info: 0x148
   __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0x218
-  __AUTH_CONST.__auth_got: 0x130
-  __AUTH_CONST.__const: 0x40
+  __DATA_CONST.__const: 0x2a0
+  __AUTH_CONST.__auth_got: 0x140
+  __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0xe0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 5A627D28-B467-36FA-A573-87F945754290
-  Functions: 27
-  Symbols:   121
-  CStrings:  83
+  UUID: A4665B8A-AC50-36E4-BB43-7CB5AA59963C
+  Functions: 37
+  Symbols:   145
+  CStrings:  98
 
Symbols:
+ GCC_except_table22
+ GCC_except_table27
+ _ApplePhotonDetectorServicesConfigureCILDutyCycle
+ _ApplePhotonDetectorServicesConfigureCILDutyCycleAsync
+ _ApplePhotonDetectorServicesGetCILDutyCycleRange
+ _ApplePhotonDetectorServicesSetCILDutyCycle
+ _ApplePhotonDetectorServicesSetupConnection
+ _ApplePhotonDetectorServicesTearDownConnection
+ ___ApplePhotonDetectorServicesSetCILDutyCycle_block_invoke
+ ___ApplePhotonDetectorServicesSetCILDutyCycle_block_invoke.33
+ ___ApplePhotonDetectorServicesSetupConnection_block_invoke
+ ___ApplePhotonDetectorServicesTearDownConnection_block_invoke
+ ___block_descriptor_tmp.30
+ ___block_descriptor_tmp.34
+ ___block_descriptor_tmp.36
+ ___block_descriptor_tmp.39
+ ___block_descriptor_tmp.52
+ ___block_literal_global.32
+ ___block_literal_global.38
+ _xpc_connection_send_message
+ _xpc_dictionary_get_int64
- ___block_descriptor_tmp.42
Functions:
~ __Z30sendSynchronousXpcMsgWithReplyP13xpcConnection25ISPServicesRemoteProperty29ISPServicesRemotePropertyTypeP28ISPServicesRemotePropertySet : 1092 -> 1144
CStrings:
+ "%s: Could not connect to the daemon, ret = 0x%x\n"
+ "%s: Could not create an xpc connection object\n"
+ "%s: Did not receive a reply from the daemon\n"
+ "%s: Error: Received incorrect duty cycle ranges min (%u), max (%u)\n"
+ "%s: Invalid pointer to the connection object\n"
+ "%s: Received return code 0x%x\n"
+ "ApplePhotonDetectorServicesConfigureCILDutyCycle"
+ "ApplePhotonDetectorServicesConfigureCILDutyCycleAsync"
+ "ApplePhotonDetectorServicesGetCILDutyCycleRange"
+ "ApplePhotonDetectorServicesSetCILDutyCycle"
+ "ApplePhotonDetectorServicesSetCILDutyCycle_block_invoke"
+ "ApplePhotonDetectorServicesSetupConnection"
+ "ApplePhotonDetectorServicesSetupConnection_block_invoke"
+ "ApplePhotonDetectorServicesTearDownConnection"
+ "H16ISPServicesRemoteReturnKey"

```
