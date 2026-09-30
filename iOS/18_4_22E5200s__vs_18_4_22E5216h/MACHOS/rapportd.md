## rapportd

> `/usr/libexec/rapportd`

```diff

-650.12.3.0.0
-  __TEXT.__text: 0xf9e50
+650.15.1.0.0
+  __TEXT.__text: 0xfd6c8
   __TEXT.__auth_stubs: 0x2b40
-  __TEXT.__objc_stubs: 0xf9e0
-  __TEXT.__objc_methlist: 0x7ce4
-  __TEXT.__cstring: 0x2a361
-  __TEXT.__objc_classname: 0xa49
+  __TEXT.__objc_stubs: 0xfa80
+  __TEXT.__objc_methlist: 0x7d24
+  __TEXT.__cstring: 0x2a3a1
+  __TEXT.__objc_classname: 0xa4a
   __TEXT.__objc_methtype: 0x3ac0
-  __TEXT.__objc_methname: 0x16479
+  __TEXT.__objc_methname: 0x16538
   __TEXT.__const: 0x34c6
   __TEXT.__gcc_except_tab: 0x1ed0
   __TEXT.__oslogstring: 0x102f

   __TEXT.__swift5_assocty: 0x90
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_acfuncs: 0x3c
-  __TEXT.__unwind_info: 0x3a60
-  __TEXT.__eh_frame: 0x26a8
+  __TEXT.__unwind_info: 0x3ac0
+  __TEXT.__eh_frame: 0x2840
   __DATA_CONST.__auth_got: 0x15b0
   __DATA_CONST.__got: 0x6f8
-  __DATA_CONST.__auth_ptr: 0x390
-  __DATA_CONST.__const: 0x5700
+  __DATA_CONST.__auth_ptr: 0x398
+  __DATA_CONST.__const: 0x5720
   __DATA_CONST.__cfstring: 0x5ac0
   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_protolist: 0x168

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0xd680
-  __DATA.__objc_selrefs: 0x4d30
-  __DATA.__objc_ivar: 0xdf0
+  __DATA.__objc_const: 0xd6a0
+  __DATA.__objc_selrefs: 0x4d58
+  __DATA.__objc_ivar: 0xdf4
   __DATA.__objc_data: 0x1c60
   __DATA.__data: 0x2e80
   __DATA.__bss: 0x2560

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 5693
+  Functions: 5701
   Symbols:   1060
-  CStrings:  8752
+  CStrings:  8760
 
Symbols:
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_initStructMetadataWithLayoutString
CStrings:
+ "\x12\x11\x14\x12Z#\x11\x13\x11\x14\x13\"\x11\x12\x12\x12\x13\x12\x12\x11\x11\x14\x16\x14\x12=\x14\x11\x111\x11\x11\x1a"
+ "+[RPNWEndpoint findEndpoint:discoverySessionID:]"
+ "+[RPNWEndpoint findEndpoint:endpointArray:]"
+ "-[RPIdentityDaemon getIdentitiesWithFlags:]"
+ "650.15.1"
+ "AppleIDSignInFamily"
+ "Did not find endpoint:%@ in session:%@, not starting age-out"
+ "Failed to create outgoing connection\n"
+ "InviteHome"
+ "_applicationServiceMonitorStarted"
+ "_clientReportLostDevice:cnx:"
+ "_startApplicationServiceMonitorIfNecessary"
+ "findEndpoint:discoverySessionID:"
+ "findEndpoint:endpointArray:"
+ "getIdentitiesWithFlags:"
- "\x12\x15\x12Z#\x11\x13\x11\x14\x13\"\x11\x12\x12\x12\x13\x12\x12\x11\x11\x14\x16\x14\x12=\x14\x11\x111\x11\x11\x1a"
- "-[RPDaemonXPCConnection getIdentitiesWithFlags:completion:]"
- "650.12.3"
- "Age out endpoint with ID '%@'"
- "Did not find endpoint with ID '%@'"
- "Failed to find endpoint from ID=%@\n"
- "Failed to get UUID from endpoint=%@\n"

```
