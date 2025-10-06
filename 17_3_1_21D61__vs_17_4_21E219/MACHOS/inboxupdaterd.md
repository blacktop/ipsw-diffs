## inboxupdaterd

> `/usr/libexec/inboxupdaterd`

```diff

-47.0.0.0.0
-  __TEXT.__text: 0x4251c
+50.0.0.0.0
+  __TEXT.__text: 0x43f88
   __TEXT.__auth_stubs: 0xad0
-  __TEXT.__objc_stubs: 0x4260
-  __TEXT.__objc_methlist: 0x193c
-  __TEXT.__cstring: 0x17e2
-  __TEXT.__objc_methname: 0x433e
+  __TEXT.__objc_stubs: 0x43e0
+  __TEXT.__objc_methlist: 0x19dc
+  __TEXT.__cstring: 0x1859
+  __TEXT.__objc_methname: 0x4530
   __TEXT.__objc_classname: 0x368
   __TEXT.__objc_methtype: 0xe78
-  __TEXT.__oslogstring: 0x3eb7
-  __TEXT.__const: 0x12c0
-  __TEXT.__gcc_except_tab: 0x818
-  __TEXT.__unwind_info: 0xb58
+  __TEXT.__oslogstring: 0x410c
+  __TEXT.__const: 0x13c1
+  __TEXT.__gcc_except_tab: 0x878
+  __TEXT.__unwind_info: 0xbb0
   __DATA_CONST.__auth_got: 0x578
   __DATA_CONST.__got: 0x140
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x4d58
-  __DATA_CONST.__cfstring: 0x19c0
+  __DATA_CONST.__const: 0x5110
+  __DATA_CONST.__cfstring: 0x1a40
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x1080
-  __DATA_CONST.__objc_arraydata: 0x238
-  __DATA_CONST.__objc_arrayobj: 0x228
-  __DATA.__objc_const: 0x5798
-  __DATA.__objc_selrefs: 0x11f0
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x1f0
-  __DATA.__objc_superrefs: 0x98
-  __DATA.__objc_ivar: 0x1cc
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x1f0
+  __DATA_CONST.__objc_superrefs: 0x98
+  __DATA_CONST.__objc_intobj: 0x10e0
+  __DATA_CONST.__objc_arraydata: 0x248
+  __DATA_CONST.__objc_arrayobj: 0x240
+  __DATA.__objc_const: 0x5868
+  __DATA.__objc_selrefs: 0x1260
+  __DATA.__objc_ivar: 0x1d8
   __DATA.__objc_data: 0x8c0
   __DATA.__data: 0x4e8
   __DATA.__bss: 0xb8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 591E6FA9-7964-381C-9FC0-612C2CC4A27F
-  Functions: 1843
+  UUID: 144D8420-38DE-35ED-A1A4-8E048B825A00
+  Functions: 1901
   Symbols:   261
-  CStrings:  1880
+  CStrings:  1923
 
CStrings:
+ "\x17!"
+ "Device already in state: %lu. No additional handling required"
+ "Failed configureNFC cmd serialization; no %{public}@ key"
+ "Failed to deserialize ConfigureNFC command"
+ "Failed to deserialize configureNFC command"
+ "Failed to deserialize nfcInactivity timeout from configureNFC APDU"
+ "Handling configureNFC command..."
+ "Handling nfcActivity timeout"
+ "Invalid nfcInactivity timeout %lfs"
+ "NFC Inactivity timer Fired!"
+ "NFC has already been configured. Rejecting command"
+ "NFCInactivityTimeout"
+ "Starting nfcInactivityTimer with timeout: %lf"
+ "Stopping isNFCActive Timer..."
+ "Stopping nfcInactivityTimer..."
+ "T@\"NSString\",?,R,C"
+ "T@\"PCPersistentTimer\",&,N,V_nfcInactivityTimer"
+ "TB,N,V_isNFCConfigured"
+ "Td,N,V_nfcInactivityTimeout"
+ "_deserializeConfigureNFC"
+ "_handleConfigureNFC:"
+ "_isNFCConfigured"
+ "_nfcInactivityTimeout"
+ "_nfcInactivityTimeoutHandler:"
+ "_nfcInactivityTimer"
+ "_resetNFCInactivityTimer"
+ "_serializeConfigureNFC"
+ "_startNFCInactivityTimer:"
+ "_stopNFCInactivityTimer"
+ "com.apple.mibu_nfc_inactivity_timer"
+ "isNFCConfigured"
+ "nfcActivityDidTimeout"
+ "nfcInactivity timeout value must be >= 0"
+ "nfcInactivity timeout: %{public}@ seconds"
+ "nfcInactivityTimeout"
+ "nfcInactivityTimer"
+ "setIsNFCConfigured:"
+ "setNfcInactivityTimeout:"
+ "setNfcInactivityTimer:"
- "\x16\x11"

```
