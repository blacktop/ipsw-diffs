## BTLEServer

> `/usr/sbin/BTLEServer`

```diff

-331.4.0.0.0
-  __TEXT.__text: 0x4e014
+334.14.0.0.0
+  __TEXT.__text: 0x4f0a4
   __TEXT.__auth_stubs: 0x1000
-  __TEXT.__objc_stubs: 0x99a0
-  __TEXT.__objc_methlist: 0x4e44
-  __TEXT.__const: 0x2e8
+  __TEXT.__objc_stubs: 0x9aa0
+  __TEXT.__objc_methlist: 0x4f34
+  __TEXT.__const: 0x2f8
   __TEXT.__gcc_except_tab: 0x7ac
-  __TEXT.__cstring: 0x25ce
-  __TEXT.__oslogstring: 0x64a4
-  __TEXT.__objc_methname: 0xd116
+  __TEXT.__cstring: 0x25fe
+  __TEXT.__oslogstring: 0x6549
+  __TEXT.__objc_methname: 0xd1ca
   __TEXT.__objc_classname: 0x670
   __TEXT.__objc_methtype: 0x1f16
   __TEXT.__ustring: 0xc6
-  __TEXT.__unwind_info: 0x11b4
+  __TEXT.__unwind_info: 0x11cc
   __DATA_CONST.__auth_got: 0x810
   __DATA_CONST.__got: 0x450
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x1148
-  __DATA_CONST.__cfstring: 0x3600
+  __DATA_CONST.__const: 0x1170
+  __DATA_CONST.__cfstring: 0x3620
   __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x3c8
+  __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_intobj: 0x540
   __DATA_CONST.__objc_arraydata: 0x188
   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA_CONST.__objc_dictobj: 0x118
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0xc460
-  __DATA.__objc_selrefs: 0x2ec0
-  __DATA.__objc_classrefs: 0x3c8
-  __DATA.__objc_superrefs: 0x1c0
+  __DATA.__objc_const: 0xc688
+  __DATA.__objc_selrefs: 0x2ef0
   __DATA.__objc_ivar: 0x59c
   __DATA.__objc_data: 0x13b0
   __DATA.__data: 0x788
-  __DATA.__bss: 0xf8
+  __DATA.__bss: 0x100
   __DATA.__common: 0x10
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 50B755DB-D315-3960-99A9-014260239F5F
-  Functions: 2153
+  UUID: 3084FE75-08B1-3B92-800F-76DBE111C7AD
+  Functions: 2168
   Symbols:   483
-  CStrings:  4110
+  CStrings:  4126
 
CStrings:
+ "%@ _authStatus = %u, _accdPairingFinished = %u"
+ "%@ authCompleted: %{BOOL}d"
+ "%@ authFailureNotification"
+ "%@ authSuccessNotification"
+ "%@ publishing device with properties: %@"
+ "%@ received pairing info"
+ "%@ unpublishing device properties"
+ "B32@?0@\"CBPeer\"8Q16^B24"
+ "Initializing ClientServiceManager for \"%@\"..."
+ "Not tracking an Mfi peripheral"
+ "Start stiction collection timer"
+ "Stop stiction collection timer"
+ "T@\"NSString\",?,R,C"
+ "assetAvailablityUpdateForAccessory:assetID:"
+ "com.apple.bluetooth.doap"
+ "didDiscoverServices for \"%@\", %@..."
+ "indexOfObjectPassingTest:"
+ "microsecToMachTime:"
+ "needsMFiAuthentication4.0"
+ "requireServicesAndMFi:"
+ "retrievePairedPeers"
+ "sharedPairingAgent"
+ "startCollectionTimer"
+ "stopCollectionTimer"
- "Publishing device with properties: %@"
- "Received pairing info"
- "Unpublishing device properties"
- "_authStatus = %u, _accdPairingFinished = %u"
- "authCompleted: %u"
- "com.apple.bluetooth.system"
- "stictionCollectionStartTimer"
- "stictionCollectionStartTimer: create timer"
- "stictionCollectionStopTimer: destroy timer"

```
