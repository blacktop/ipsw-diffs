## AVRouting

> `/System/Library/Frameworks/AVRouting.framework/AVRouting`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-360.66.1.11.1
-  __TEXT.__text: 0x63edc
+360.70.2.0.0
+  __TEXT.__text: 0x63f34
   __TEXT.__objc_methlist: 0x6728
   __TEXT.__const: 0x10c
   __TEXT.__gcc_except_tab: 0x6c4
-  __TEXT.__cstring: 0xed51
+  __TEXT.__cstring: 0xed92
   __TEXT.__oslogstring: 0xc989
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__unwind_info: 0x18a0

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1270
+  __DATA_CONST.__const: 0x1278
   __DATA_CONST.__objc_classlist: 0x3b8
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x2f8
   __DATA_CONST.__got: 0x1108
   __AUTH_CONST.__const: 0x410
-  __AUTH_CONST.__cfstring: 0x4660
+  __AUTH_CONST.__cfstring: 0x46a0
   __AUTH_CONST.__objc_const: 0xc100
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__auth_got: 0x0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 2572
-  Symbols:   5487
-  CStrings:  1709
+  Symbols:   5488
+  CStrings:  1711
 
Symbols:
+ _AVOutputContextManagerFailureDetailsMediaAppNameKey
Functions:
~ -[AVFigEndpointUIAgentOutputContextManagerImpl _showErrorPromptForRouteDescriptor:reason:didFailToConnectToOutputDeviceDictionary:failureDetails:] : 992 -> 1080
CStrings:
+ "AVOutputContextManagerFailureDetailsMediaAppNameKey"
+ "MediaAppName"
```
