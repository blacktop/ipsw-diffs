## AVRouting

> `/System/Library/Frameworks/AVRouting.framework/Versions/A/AVRouting`

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

-360.66.1.0.0
-  __TEXT.__text: 0x5bf30
+360.70.2.0.0
+  __TEXT.__text: 0x5bf88
   __TEXT.__objc_methlist: 0x6278
   __TEXT.__const: 0x110
-  __TEXT.__cstring: 0xe01c
+  __TEXT.__cstring: 0xe05d
   __TEXT.__oslogstring: 0xb3aa
   __TEXT.__gcc_except_tab: 0x5b8
   __TEXT.__unwind_info: 0x1668

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x7a0
+  __DATA_CONST.__const: 0x7a8
   __DATA_CONST.__objc_classlist: 0x370
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x2c8
   __DATA_CONST.__got: 0xfd8
   __AUTH_CONST.__const: 0xe50
-  __AUTH_CONST.__cfstring: 0x4340
+  __AUTH_CONST.__cfstring: 0x4380
   __AUTH_CONST.__objc_const: 0xb6a8
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__auth_got: 0x0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 2490
-  Symbols:   5224
-  CStrings:  1561
+  Symbols:   5225
+  CStrings:  1563
 
Symbols:
+ _AVOutputContextManagerFailureDetailsMediaAppNameKey
Functions:
~ -[AVFigEndpointUIAgentOutputContextManagerImpl _showErrorPromptForRouteDescriptor:reason:didFailToConnectToOutputDeviceDictionary:failureDetails:] : 992 -> 1080
CStrings:
+ "AVOutputContextManagerFailureDetailsMediaAppNameKey"
+ "MediaAppName"
```
