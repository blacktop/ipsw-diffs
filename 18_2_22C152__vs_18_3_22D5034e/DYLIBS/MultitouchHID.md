## MultitouchHID

> `/System/Library/Extensions/AppleMultitouchSPI.kext/PlugIns/MultitouchHID.plugin/MultitouchHID`

```diff

-8120.4.0.0.0
-  __TEXT.__text: 0x50f50
-  __TEXT.__auth_stubs: 0x1790
+8130.2.0.0.0
+  __TEXT.__text: 0x510d0
+  __TEXT.__auth_stubs: 0x17a0
   __TEXT.__objc_methlist: 0x1d0
   __TEXT.__const: 0x1871
-  __TEXT.__cstring: 0x52be
+  __TEXT.__cstring: 0x52f6
   __TEXT.__gcc_except_tab: 0xc64
-  __TEXT.__oslogstring: 0x3423
+  __TEXT.__oslogstring: 0x3468
   __TEXT.__unwind_info: 0x1508
   __TEXT.__objc_classname: 0x3e
   __TEXT.__objc_methname: 0x7cb

   __DATA_CONST.__objc_selrefs: 0x2c8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0xbd8
+  __AUTH_CONST.__auth_got: 0xbe0
   __AUTH_CONST.__const: 0x2a48
-  __AUTH_CONST.__cfstring: 0x5ce0
+  __AUTH_CONST.__cfstring: 0x5d00
   __AUTH_CONST.__objc_const: 0x300
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__data: 0xa8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1574
-  Symbols:   2187
-  CStrings:  1390
+  Symbols:   2188
+  CStrings:  1393
 
Symbols:
+ _MTDeviceSetParserEnabled
CStrings:
+ "TrackpadExternallyDisabled"
+ "[HID] [MT] %s%s%s Dropped relative pointer event. Parser is disabled"
+ "dispatchRelativePointerEvent"

```
