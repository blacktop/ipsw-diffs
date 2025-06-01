## lockdownd

> `/usr/libexec/lockdownd`

```diff

-1302.120.2.0.0
-  __TEXT.__text: 0xf92e0
-  __TEXT.__auth_stubs: 0x2a80
+1302.140.2.0.0
+  __TEXT.__text: 0xf98e0
+  __TEXT.__auth_stubs: 0x2ab0
   __TEXT.__objc_stubs: 0x4120
   __TEXT.__objc_methlist: 0x31ec
-  __TEXT.__cstring: 0x48595
+  __TEXT.__cstring: 0x487f0
   __TEXT.__const: 0x18130
   __TEXT.__oslogstring: 0x6bc
-  __TEXT.__gcc_except_tab: 0x34c0
+  __TEXT.__gcc_except_tab: 0x34bc
   __TEXT.__objc_classname: 0xb52
   __TEXT.__objc_methname: 0x4697
   __TEXT.__objc_methtype: 0xd9c
   __TEXT.__services: 0x2d8f
-  __TEXT.__unwind_info: 0x2d60
+  __TEXT.__unwind_info: 0x2d6c
   __TEXT.__eh_frame: 0x11b8
-  __DATA_CONST.__auth_got: 0x1558
+  __DATA_CONST.__auth_got: 0x1570
   __DATA_CONST.__got: 0x4b0
   __DATA_CONST.__auth_ptr: 0x60
-  __DATA_CONST.__const: 0xa378
-  __DATA_CONST.__cfstring: 0x16e80
+  __DATA_CONST.__const: 0xa308
+  __DATA_CONST.__cfstring: 0x16fe0
   __DATA_CONST.__objc_classlist: 0x260
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30

   __DATA.__objc_ivar: 0x3d8
   __DATA.__objc_data: 0x17c0
   __DATA.__data: 0x2598
-  __DATA.__bss: 0xfd0
-  __DATA.__common: 0x1a40
+  __DATA.__bss: 0xfd2
+  __DATA.__common: 0x1a50
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 4068B16A-4853-3646-BA33-B577DD0439AF
-  Functions: 2829
-  Symbols:   879
-  CStrings:  11753
+  UUID: 0E46563E-9F7E-325F-8EE0-525AE31F6413
+  Functions: 2830
+  Symbols:   882
+  CStrings:  11790
 
Symbols:
+ _CFUUIDGetConstantUUIDWithBytes
+ _CFUUIDGetUUIDBytes
+ _IOCreatePlugInInterfaceForService
CStrings:
+ "%s%d,%s"
+ "AppleHPMARM"
+ "Checking LUN%d\n"
+ "Checking LUN=%u\n"
+ "Could not get nonceHash!\n"
+ "Couldn't find RID for service!\n"
+ "Error finding IOKit service\n"
+ "Error when reading usbc-update-protocol\n"
+ "Flipping nonce for LUN=%u\n"
+ "Found no matching services\n"
+ "Found updatable Ace based on usbc-update-protocol value\n"
+ "IONameMatch"
+ "Number of updatable USBPortControllers = %u\n"
+ "QueryInterface failed\n"
+ "RID"
+ "Running Ace3 mode check\n"
+ "USBPortController"
+ "Unexpected usbc-update-protocol value\n"
+ "User said trust at time ptp %llu connection %llu."
+ "VinylRestore-50~99"
+ "check_in_adfu failed, rid=0x%X\n"
+ "could not create EDT property dict\n"
+ "getAHPMLibInterfaceForRID failed for rid=0x%X\n"
+ "get_mode failed\n"
+ "new nonce %@\n"
+ "old nonce %@\n"
+ "rid"
+ "usbc,sn201202x,iic"
+ "usbc,sn201202x,spmi"
+ "usbc-update-protocol"
- "User said trust ptp at time %llu connection %llu."
- "VinylRestore-49.0.1~3535"
- "ask_user_to_trust_ptp_block_invoke_5"
- "ask_user_to_trust_ptp_block_invoke_6"

```
