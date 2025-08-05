## TVRemoteCore

> `/System/Library/PrivateFrameworks/TVRemoteCore.framework/TVRemoteCore`

```diff

-548.0.10.0.0
-  __TEXT.__text: 0x62de8
+548.0.15.0.0
+  __TEXT.__text: 0x63498
   __TEXT.__auth_stubs: 0xb50
-  __TEXT.__objc_methlist: 0x85bc
+  __TEXT.__objc_methlist: 0x85d4
   __TEXT.__const: 0x230
   __TEXT.__gcc_except_tab: 0xd9c
-  __TEXT.__cstring: 0x4ffb
-  __TEXT.__oslogstring: 0x6d76
-  __TEXT.__unwind_info: 0x1710
-  __TEXT.__objc_classname: 0xd38
-  __TEXT.__objc_methname: 0xf7a0
-  __TEXT.__objc_methtype: 0x29eb
-  __TEXT.__objc_stubs: 0x9980
+  __TEXT.__cstring: 0x509e
+  __TEXT.__oslogstring: 0x6f20
+  __TEXT.__unwind_info: 0x1720
+  __TEXT.__objc_classname: 0xd3a
+  __TEXT.__objc_methname: 0xf857
+  __TEXT.__objc_methtype: 0x2a08
+  __TEXT.__objc_stubs: 0x99c0
   __DATA_CONST.__got: 0x570
   __DATA_CONST.__const: 0x1800
   __DATA_CONST.__objc_classlist: 0x380
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b38
+  __DATA_CONST.__objc_selrefs: 0x3b50
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x2e0
   __DATA_CONST.__objc_arraydata: 0xd0
   __AUTH_CONST.__auth_got: 0x5b8
   __AUTH_CONST.__const: 0x538
   __AUTH_CONST.__cfstring: 0x6d20
-  __AUTH_CONST.__objc_const: 0xcfc8
+  __AUTH_CONST.__objc_const: 0xcff8
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH.__objc_data: 0x21c0
-  __DATA.__objc_ivar: 0x8ac
+  __DATA.__objc_ivar: 0x8b0
   __DATA.__data: 0xb50
   __DATA.__bss: 0x120
   __DATA_DIRTY.__objc_data: 0x140

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0BF0CB79-BB1F-35C1-A659-324B0E3F2309
-  Functions: 2799
-  Symbols:   9073
-  CStrings:  5642
+  UUID: F7DB17DD-CE3E-326C-88AB-6D31D8623475
+  Functions: 2801
+  Symbols:   9080
+  CStrings:  5661
 
Symbols:
+ -[TVRCRapportRemoteTextInputKeyboardImpl cachedInputSystemDataPayload]
+ -[TVRCRapportRemoteTextInputKeyboardImpl setCachedInputSystemDataPayload:]
+ _OBJC_IVAR_$_TVRCRapportRemoteTextInputKeyboardImpl._cachedInputSystemDataPayload
+ _objc_msgSend$_stopObservingTelevisionEditingSession
+ _objc_msgSend$device:didUpdateNameFrom:
CStrings:
+ "$"
+ "%s - payload: %@"
+ "-[TVRCRapportDeviceImpl _setupKeyboardController]"
+ "-[TVRCRapportRemoteTextInputKeyboardImpl setTextActionPayload:]"
+ "-[TVRXKeyboardController sendTextActionPayload:]"
+ "@\"RTIInputSystemDataPayload\""
+ "Disconnected. Stop observing TV editing session"
+ "Found matching IDS identifiers - old: %@ new: %@"
+ "Keyboard RemoteTextInput received payload string length: %lu"
+ "Keyboard RemoteTextInput received text action payload: %{public}@"
+ "Keyboard RemoteTextInput send payload string length: %lu"
+ "Remote keyboard returning RTI text: length: %lu"
+ "Setting kbimpl: new: %@ old: %@"
+ "Stop observing TV editing session"
+ "T@\"RTIInputSystemDataPayload\",&,N,V_cachedInputSystemDataPayload"
+ "TVRCDevice disconnecting with type: %ld"
+ "Updating identifer - old: %@ new: %@"
+ "_cachedInputSystemDataPayload"
+ "_receivedInputSourceSession: newSession: %@ currentSession: %@"
+ "cachedInputSystemDataPayload"
+ "device:didUpdateNameFrom:"
+ "setCachedInputSystemDataPayload:"
- "IDS identifiers match old: %@ new: %@"
- "Keyboard RemoteTextInput received text action payload"
- "Keyboard returning RTI text as %@"

```
