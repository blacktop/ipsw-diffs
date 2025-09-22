## remoted

> `/usr/libexec/remoted`

```diff

-202.0.1.0.0
-  __TEXT.__text: 0x43c90
-  __TEXT.__auth_stubs: 0x1840
-  __TEXT.__objc_stubs: 0x2420
-  __TEXT.__objc_methlist: 0x14e4
-  __TEXT.__const: 0x1fa
-  __TEXT.__oslogstring: 0x8456
+202.40.9.0.0
+  __TEXT.__text: 0x43998
+  __TEXT.__auth_stubs: 0x1830
+  __TEXT.__objc_stubs: 0x2460
+  __TEXT.__objc_methlist: 0x1550
+  __TEXT.__const: 0x1f2
+  __TEXT.__oslogstring: 0x844c
   __TEXT.__cstring: 0x20dd
-  __TEXT.__objc_methname: 0x247d
-  __TEXT.__objc_classname: 0x2e1
-  __TEXT.__objc_methtype: 0x72f
-  __TEXT.__gcc_except_tab: 0x1628
-  __TEXT.__unwind_info: 0xf30
-  __DATA_CONST.__auth_got: 0xc30
-  __DATA_CONST.__got: 0x228
+  __TEXT.__objc_methname: 0x24f5
+  __TEXT.__objc_classname: 0x2f4
+  __TEXT.__objc_methtype: 0x79b
+  __TEXT.__gcc_except_tab: 0x15dc
+  __TEXT.__unwind_info: 0xf28
+  __DATA_CONST.__auth_got: 0xc28
+  __DATA_CONST.__got: 0x230
   __DATA_CONST.__const: 0x1368
   __DATA_CONST.__cfstring: 0xe80
   __DATA_CONST.__objc_classlist: 0xd8
+  __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0xb0
   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x2760
-  __DATA.__objc_selrefs: 0x950
-  __DATA.__objc_ivar: 0x218
+  __DATA.__objc_const: 0x2810
+  __DATA.__objc_selrefs: 0x970
+  __DATA.__objc_ivar: 0x21c
   __DATA.__objc_data: 0x870
-  __DATA.__data: 0x674
+  __DATA.__data: 0x6d4
   __DATA.__bss: 0x3f0
   __DATA.__common: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3EEBAE3A-5334-3A23-98EF-AA0BE9566844
-  Functions: 1387
+  UUID: 699DC4A6-C9F1-363F-82E9-C37EB4817379
+  Functions: 1390
   Symbols:   494
-  CStrings:  1902
+  CStrings:  1913
 
Symbols:
+ _OBJC_CLASS_$_RemoteDeviceQuery
+ _remote_device_matches
- _strcasestr
- _xpc_uint64_get_value
CStrings:
+ "%{public}@> timesync failed: timesync already in progress"
+ "@\"NSObject<OS_xpc_object>\"28@0:8*16B24"
+ "@28@0:8*16B24"
+ "B32@0:8r*16@\"NSObject<OS_xpc_object>\"24"
+ "B32@0:8r*16@24"
+ "Get device query: %{public}@ (client=\"%s\")"
+ "RemoteDeviceCommon"
+ "T*,R,N"
+ "_timesync_in_progress"
+ "copyProperty:allowSensitive:"
+ "device_get: Returning device of type %d (client=\"%s\")"
+ "device_get: Unable to find device with type %d (client=\"%s\")"
+ "hasServiceWithName:peerMessage:"
+ "setAvailableService:"
+ "wildcard"
- "GET query with invalid criteria (t:%d n:%d u:%d)"
- "GET query with invalid criteria (trust:%d u:%d)"
- "device_get_unique: Returning device of type %d (client=\"%s\")"
- "device_get_unique: Unable to find device with type %d (client=\"%s\")"

```
