## powerd

> `/System/Library/CoreServices/powerd.bundle/powerd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2043.60.6.0.0
-  __TEXT.__text: 0x77548
+2043.60.10.0.1
+  __TEXT.__text: 0x77e14
   __TEXT.__auth_stubs: 0x1c10
-  __TEXT.__objc_stubs: 0x59a0
-  __TEXT.__objc_methlist: 0x2cbc
+  __TEXT.__objc_stubs: 0x5a80
+  __TEXT.__objc_methlist: 0x2d0c
   __TEXT.__const: 0x540
-  __TEXT.__cstring: 0x6ee1
-  __TEXT.__objc_methname: 0x7303
-  __TEXT.__oslogstring: 0xe309
+  __TEXT.__cstring: 0x6f12
+  __TEXT.__objc_methname: 0x73b3
+  __TEXT.__oslogstring: 0xe450
   __TEXT.__objc_classname: 0x3f3
   __TEXT.__objc_methtype: 0xaa4
-  __TEXT.__gcc_except_tab: 0x50c
+  __TEXT.__gcc_except_tab: 0x518
   __TEXT.__dlopen_cstrs: 0x300
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x23b8
-  __DATA_CONST.__const: 0x2680
-  __DATA_CONST.__cfstring: 0x7720
+  __TEXT.__unwind_info: 0x23e0
+  __DATA_CONST.__const: 0x26a0
+  __DATA_CONST.__cfstring: 0x77a0
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__auth_got: 0xe18
   __DATA_CONST.__got: 0x3c0
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA.__objc_const: 0x5718
-  __DATA.__objc_selrefs: 0x1c58
-  __DATA.__objc_ivar: 0x3dc
+  __DATA.__objc_const: 0x5748
+  __DATA.__objc_selrefs: 0x1c90
+  __DATA.__objc_ivar: 0x3e0
   __DATA.__objc_data: 0x910
   __DATA.__data: 0xbb4
   __DATA.__common: 0x1270

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libenergytrace.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2658
+  Functions: 2668
   Symbols:   577
-  CStrings:  4088
+  CStrings:  4106
 
CStrings:
+ ":apsd"
+ "CSPN: Skipping update state for client %@ (Trial sendCSPNStatusUpdateToAPSD is off)"
+ "CSPN: Trial sendCSPNStatusUpdateToAPSD turned off. Update state for client %@ to %d"
+ "CoreSmartPowerNap: Trial %@ = %d (iPad %d)"
+ "Current ports %@"
+ "Initial active state %@ for registryID %llu"
+ "T@\"NSMutableDictionary\",&,N,V_ports"
+ "TB,V_send_status_to_apsd"
+ "_ports"
+ "_send_status_to_apsd"
+ "active"
+ "hasSuffix:"
+ "isAPSDClientIdentifier:"
+ "messageType: kIOMessageServicePropertyChange active: %@ for registryID: %llu"
+ "portInfoForKey:"
+ "ports"
+ "resetAPSDClientsToOff"
+ "sendCSPNStatusUpdateToAPSD"
+ "send_status_to_apsd"
+ "setPorts:"
+ "setSend_status_to_apsd:"
+ "shouldSendStateToClient:"
- "Current date roles %@"
- "T@\"NSMutableDictionary\",&,N,V_dataRole"
- "_dataRole"
- "setDataRole:"
```
