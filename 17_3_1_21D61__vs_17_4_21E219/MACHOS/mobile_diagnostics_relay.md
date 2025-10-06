## mobile_diagnostics_relay

> `/usr/libexec/mobile_diagnostics_relay`

```diff

-29.0.0.0.0
-  __TEXT.__text: 0x306c
-  __TEXT.__auth_stubs: 0x650
-  __TEXT.__cstring: 0x10af
+32.0.0.0.0
+  __TEXT.__text: 0x2e58
+  __TEXT.__auth_stubs: 0x610
+  __TEXT.__cstring: 0x10b3
   __TEXT.__ustring: 0x1b0
-  __TEXT.__unwind_info: 0xc0
-  __DATA_CONST.__auth_got: 0x328
-  __DATA_CONST.__got: 0xb0
+  __TEXT.__unwind_info: 0xcc
+  __DATA_CONST.__auth_got: 0x308
+  __DATA_CONST.__got: 0xa8
   __DATA_CONST.__const: 0x10
-  __DATA_CONST.__cfstring: 0xfa0
+  __DATA_CONST.__cfstring: 0xf80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/MobileObliteration.framework/MobileObliteration
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
-  UUID: CD90923D-DBF6-378C-8B46-D689E586FDD6
+  UUID: 139125CE-74B2-3A17-9290-401CBC61ED27
   Functions: 33
-  Symbols:   126
-  CStrings:  308
+  Symbols:   121
+  CStrings:  302
 
Symbols:
+ _IOObjectConformsTo
- _CFDataCreate
- _IOConnectCallStructMethod
- _IORegistryEntryGetLocationInPlane
- _IOServiceOpen
- ___strcat_chk
- _mach_task_self_
CStrings:
+ "%s, Bad parameter."
+ "Can't create CFNumber for regEntry"
+ "Can't create CFString for className."
+ "Can't create CFString for entry name."
+ "Can't create CFString for state."
+ "Could not gather the NAND information as this function has been deprecated"
+ "Could not gather the Wifi information as this function has been deprecated"
+ "Failed to get space for state string."
+ "IOReg query class %s"
+ "IOReg query entry %s"
+ "IOReg query plane %s"
+ "IOService"
+ "MobileGestalt query function has been deprecated"
+ "MobileGestaltDeprecated"
+ "NANDInfoDeprecated"
+ "Received request."
+ "Request Key received: %s"
+ "WifiInfoDeprecated"
+ "can't obtain I/O Kit's master port"
- "@"
- "AND_STRUCT_WMR_EXPORT_ALL"
- "Active"
- "AppleNANDFTL"
- "Can't create CFDictionary."
- "Can't create CFNumber"
- "Can't create CFString."
- "Could not create CFData"
- "Could not gather the NAND information"
- "Could not get connection to service"
- "Could not get matching service for AppleNANDFTL"
- "Could not malloc %d bytes"
- "Could not retrieve data from driver"
- "Failed to create dict, status=%d"
- "IO80211Interface"
- "IOConnectCallStructMethod: %d"
- "IORegistryEntryGetLocationInPlane has failed with error %d."
- "NANDInfoFailed"
- "NO"
- "YES"
- "_load_nand_infoCould not get matching IOKit service for AppleNANDFTL"
- "create_property_dict"
- "gather_nand_data"
- "properties"

```
