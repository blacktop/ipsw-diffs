## Required

> `/System/Library/Trace/Providers/Required.bundle/Required`

```diff

-38.1.0.0.0
-  __TEXT.__text: 0xa34c
-  __TEXT.__auth_stubs: 0x7b0
-  __TEXT.__objc_stubs: 0x580
-  __TEXT.__objc_methlist: 0x1b4
+38.2.0.0.0
+  __TEXT.__text: 0xa940
+  __TEXT.__auth_stubs: 0x7d0
+  __TEXT.__objc_stubs: 0x720
+  __TEXT.__objc_methlist: 0x214
   __TEXT.__const: 0x100
-  __TEXT.__cstring: 0x91a
-  __TEXT.__objc_methname: 0x642
+  __TEXT.__cstring: 0x9ad
+  __TEXT.__objc_methname: 0x7a6
   __TEXT.__objc_classname: 0x79
-  __TEXT.__objc_methtype: 0x20c
+  __TEXT.__objc_methtype: 0x272
   __TEXT.__gcc_except_tab: 0x39c
-  __TEXT.__unwind_info: 0x3dc
+  __TEXT.__unwind_info: 0x3ec
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0x3e8
+  __DATA_CONST.__auth_got: 0x3f8
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__const: 0x1c8
-  __DATA_CONST.__cfstring: 0x4e0
+  __DATA_CONST.__cfstring: 0x540
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x698
-  __DATA.__objc_selrefs: 0x1d0
-  __DATA.__objc_classrefs: 0x80
+  __DATA.__objc_selrefs: 0x238
+  __DATA.__objc_classrefs: 0x88
   __DATA.__objc_superrefs: 0x20
   __DATA.__objc_ivar: 0x34
   __DATA.__objc_data: 0x190

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BC82DDE2-C0ED-37DC-BC32-48939513E7E4
-  Functions: 227
-  Symbols:   176
-  CStrings:  230
+  UUID: 3307F651-7021-399D-902B-F8E9B0ECB774
+  Functions: 233
+  Symbols:   179
+  CStrings:  254
 
Symbols:
+ _OBJC_CLASS_$_NSSet
+ _mach_error_string
+ _objc_release_x27
CStrings:
+ "@24@0:8r*16"
+ "@28@0:8I16r*20"
+ "Failed to create properties for service %s: %s"
+ "Failed to get service matching %s: %s"
+ "Failed to serialize AGX and IOMFB metadata dictionary: %@"
+ "Failed to serialize IOMFB and AGX metadata"
+ "^{__CFArray=}24@0:8r*16"
+ "^{__CFData=}16@0:8"
+ "_copyPropertiesOfIOService:"
+ "_fullySerializeService:planeName:"
+ "_mergeIOServicePropertiesIntoDictionary:name:"
+ "_removeSetsFromArray:"
+ "_removeSetsFromDict:"
+ "_serializeFullIOKitPlane:"
+ "_serializeIOMFBAGXServices"
+ "_serializeServicePlaneRecursively:planeName:"
+ "allObjects"
+ "mutableCopy"
+ "objectAtIndexedSubscript:"
+ "objectForKeyedSubscript:"
+ "setObject:atIndexedSubscript:"
+ "v32@0:8^{__CFDictionary=}16r*24"
- "Failed to serialize IOMFB service data"

```
